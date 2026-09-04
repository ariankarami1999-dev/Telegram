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
<img src="https://cdn4.telesco.pe/file/pGGFUxPvsnjDETcgdY9M_QgTzzwcPpgCZFDnYH1GM06Szm8wUgCdqwLHbN_dZRbRa_I_Dk2sfFkYYFLWsmeX76E4I0O_61SsahARHuVRNQwzmZFf9B_hxDStVFdSwRnmgdfUh48iSh1wJG2S0a7nFx01a-xEjfqXbavy23GXdoxFkUtBY2IEK-s3MuFlXBMeD1648AonkQY54krU0C9T-1Vy2bMZiH6dEMw0eTUdQjFnK1KRVa2F4vQqB2Th728hhO1jImNssffdaFtgJ9gOduNdjdFeciOpaFXHg4G8Hzi4HVOimKn5yOyCGj9yU31uTtuuc_JnZEWnVuCuMhyNvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.44M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 03:13:40</div>
<hr>

<div class="tg-post" id="msg-687302">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSHFtIZa_X8ZymOjcHyST32fDWJeofpTyEVedT2wWMA7T27uuXIfeXl7db5-034xsvAWc7pZQXYa8pTNnGjway2HfI-IZ7WFT3VvZOprJuYJgZZyq5j1f-vCTQNQ0BbbfezpBGfcjIBN5eJiYjauHOc61khQwU2LnEbAU1Y9tKD-tOBLgaOFyVTSNLy0Xvm2lj9I0QmWRhIwlND39SNnK7QR9ZbfKZokr2axoHnicSN8xxmp-nN85gQoQaFF1WmQk5FokATwT3rnaLONhO4QZyCRm4hlZKOO7jdXHDM7-1TAhsepuIt1aLGDmbDTW-FTYnCz9EcQjVxolXc27XvOUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکات ریتِر، افسر سابق اطلاعاتی آمریکایی: اگر ایرانی بودم، تأسیسات تصفیه آب شور اسرائیل را همین امروز از بین می‌بردم. اسرائیل را نابود می‌کردم
🔹
باید به موجودیت اسرائیل پایان داد. به معنای واقعی کلمه، سرطان سیاره است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/687302" target="_blank">📅 01:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687301">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
آسوشیتدپرس: قیمت گازوییل در آمریکا برای نخستین بار در تاریخ به‌طور میانگین به رکورد بی‌سابقه ۵.۸۵ دلار رسید
🔹
کارشناسان نسبت به پیامدهای اقتصادی آن بر زنجیره تأمین هشدار می‌دهند. افزایش قیمت گازوییل به معنای افزایش هزینه حمل‌ونقل طیف گسترده‌ای از کالاهای روزمره است.
🔹
خریداران باید شاهد افزایش بیشتر قیمت کالاها در فروشگاه‌ها باشند.‏
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/687301" target="_blank">📅 01:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687300">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeNsHbdpuTyENaoEL572zLnVBPLWtkH9oWGPuWp3U9IbXY4z0Umb2_0XZj_pdppSjTPpFUrd7zkU3IwREiyv-x1ZD_mSbARHsBYjDQkleYgn3ScGwCnOBYIVCpRUpeQ_RMFsQQfYv8mTpZLxiwr7XesUyK1kYAsTt1jyeZp2i8YUXu7sfBl4xDgkUNJYhS6z1jApRiepgaRs6tfE6QpL4JsncRgNuUXKVRbjmjlUhle4wgCQ0JHQ4bZr8MXEbWeZV2fL97eznkbtmLM-xxwY-c-Epzcv_HHn9Zt32P6zvFuW7INDBGBmaZcEgUytyPtMS3pe1qGft2TgaqRPgE01RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
هنوز هوا سرد نشده، ولی وقت خرید کاپشنه!
🧥
کاپشن مردانه
Adidas مشکی | داخل تمام خز
💧
پارچه مموری ضدآب + خز تدی گرم و نرم
✨
کلاه‌دار، جیب‌دار و شیک
💰
الان با تخفیف، به قیمت پارسال!
📌
قبل از شروع فصل سرما بخر، چون وقتی فصلش برسه خبری از این قیمت نیست!
💰
قیمت ویژه تخفیف: فقط ۲,۱۹۸,۰۰۰ تومان!
👇
خرید:
https://memarket24.ir/product/brief/50703/180124/</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/687300" target="_blank">📅 01:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687299">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_02t3zaICeNZEeqpX2kptNAlQz_ecwKYfOwf3uCBTDFD9p_kyeCUuOFg2GhBLNrPa0R6287KEK055WzsUxw2rMn-iH9WKQfbNeAUUlum8ibvC2Qe570i7rNKEExsxTB3SWeJBVThULvq2_v94574qA9ebo3jrcfBALkyl-kVdgWhWI5idwxT176ffxEUsbBCzEkmJ7DUHORBiauF5yOclTy3T7moKBA3UDoQb5nnuA807HBL9WdHxaxy3PF-5YyTSzWGTlKwvOzEyi1PvzBgzMvJ9rUc-ggWPzcRWtiGv6ZHELDAgPhpu6FlXneF8PPUDnEMGccWycoD1knlWhZhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال آمریکایی: اگر ترامپ یک کار مثبت کرده باشد، به مردم آمریکا نشان داده اسرائیل، با وجود جمعیت ۹ میلیونی‌اش، عملاً اختیار آمریکا را دارد
🔹
ما به نتانیاهو رأی نداده‌ایم رئیس‌جمهورمان باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/687299" target="_blank">📅 01:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687298">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای معاون اول ترامپ
جی‌دی ونس:
🔹
بله، قیمت بنزین در ایالات متحده بالاست، اما در همه جای دیگر جهان به مراتب بدتر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/687298" target="_blank">📅 01:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687297">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKB8qShhl02IntQiyMkILkTf_hNSWSt-GgZwtn-hh5YSftLN9QjygaV4cic8v6trcZBkxsxGqmURGicUPWCmgLcYKoMo5TJbPnH-aGtb88L7UWiydhso-pvUtDJjd7drfFNlkTwpOyYEtb4BPEqgtUVekz9ncZwdpX_qA_dzGR3KkmG_NHHg7UlpxpymykVoDciDdGWxa_hQpUfGm5BET5uuA3sd-rldCmmbMzOp_Y2J53HXRrE7bh_67lo0L7_7zNO9zjXYUdRW6QcwuQqQXG8WPmnYTloTYWKm6mgGTohIiT9VPrzUW_RpI0iP33R5tNeexzC_5kn63jXzMl4F_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: صندوق ثروت ملی ۲ تریلیون‌دلاری نروژ پیشنهاد کاهش شدید دارایی‌های خود در اوراق خزانه‌داری آمریکا را مطرح کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/687297" target="_blank">📅 01:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687296">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QB1eyt9nm5yWgFlRlPn_QM7I-1YUxb2vWEmxX11bb4N6LDXitxGNR7cfewW6EErEvtIm2EYGd_3lfN6coEcK56iSGQmRmTikYL4nfgod0MGC8caTxTzg9KPst9X3gNLA5YccmNSdNtzZzR1wVgDk0IlYC4yZtHNlIrKkPQhPga1QsLWaAHAO5noVMmoqWevqqxRXuK_h_lmQi1BAC4TEVysdfxiLI6DH6f54_N31B87u9puO6qQo7xW6Gh8gDvsP1-DnPJGUpinCqv5DYLG7qX4zxk_JkXvL4a_SEt00XoUhNuAsH715EQjQvASsMlyrVjsZpbqHw3r-qdUJ84F6ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویب نقشه‌ای با ابعاد واقعی کشورها در سازمان ملل؛ آمریکا تنها مخالف بود!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/687296" target="_blank">📅 01:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687295">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bfdbbddca.mp4?token=p6YC72yTtYoLMprnHofrbrFI4pVVXm-W-RAhThxcvHgbkkdNbAxjWVXjg5Ec8DmDMiRduKxnHg3cKeR1DZ2zKiAsWNsNiQMpdO1YZXCU0e_2a6o08mjhoOJKASvfFEDh-CRPW50dRl6BZjRg1biad9jgvxX0As7CzvyNPUrkRYPllMdxHrZ9m_kBsq9hgRPHZ_LyNNd-4YtXbbXyDOC4xviHOsrPnpuVOVM8h1QpBy8yyYtyyZbUDxKrKPKxAfhMTwVduoC6K2dhIc4hPD6QWYyAPePH1CzDfqT_XCTLPAacfprws2oCYLfLU0bWfGF0sUm5Cv0NqpYaIcbUuJq6WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bfdbbddca.mp4?token=p6YC72yTtYoLMprnHofrbrFI4pVVXm-W-RAhThxcvHgbkkdNbAxjWVXjg5Ec8DmDMiRduKxnHg3cKeR1DZ2zKiAsWNsNiQMpdO1YZXCU0e_2a6o08mjhoOJKASvfFEDh-CRPW50dRl6BZjRg1biad9jgvxX0As7CzvyNPUrkRYPllMdxHrZ9m_kBsq9hgRPHZ_LyNNd-4YtXbbXyDOC4xviHOsrPnpuVOVM8h1QpBy8yyYtyyZbUDxKrKPKxAfhMTwVduoC6K2dhIc4hPD6QWYyAPePH1CzDfqT_XCTLPAacfprws2oCYLfLU0bWfGF0sUm5Cv0NqpYaIcbUuJq6WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزت‌الله ضرغامی: اصولگرایان چنان از خجالت هم در می‌آیند که حاضرند یک اصلاح‌طلب پیروز شود
🔹
اصولگرایان هرچقدر که بتوانند همدیگر را نابود و تخریب می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/687295" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687294">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78221dc9cd.mp4?token=Z2xwEVCERgolJkpIcgFkw9Yt9miBheGlZ7l9S8LwQa26_73zNLQQjNlPYYkvDO-lBAq4xVn995HQIXyQXBx0hu4DtLceOTfLUb8vdLVr3oMVrrG1WYNuwGbCLwiQG7jFmfJDk4GN5NpcJ4hN2a07sV8c3qSO34SxgLEEXUt2v7l8GjofvKN3AxDSwoMbNiPVS2lQCMuG0H4ExChDVqKFvD1-SsRsA4gpTUha9DXkpttcMTE9uKvul1Ecsm3eZs9IHss1FvwzJnkQpM7h-3qbNsTTr61gWeRvw4bWRRT1ub-UX5MQVcD13XIKtF9TkYUcyuDAFCCXa3HBy4vvbZikiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78221dc9cd.mp4?token=Z2xwEVCERgolJkpIcgFkw9Yt9miBheGlZ7l9S8LwQa26_73zNLQQjNlPYYkvDO-lBAq4xVn995HQIXyQXBx0hu4DtLceOTfLUb8vdLVr3oMVrrG1WYNuwGbCLwiQG7jFmfJDk4GN5NpcJ4hN2a07sV8c3qSO34SxgLEEXUt2v7l8GjofvKN3AxDSwoMbNiPVS2lQCMuG0H4ExChDVqKFvD1-SsRsA4gpTUha9DXkpttcMTE9uKvul1Ecsm3eZs9IHss1FvwzJnkQpM7h-3qbNsTTr61gWeRvw4bWRRT1ub-UX5MQVcD13XIKtF9TkYUcyuDAFCCXa3HBy4vvbZikiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به یک واحد مسکونی در جنوب لبنان
🔹
رسانه‌های لبنانی از تجاوز جدید رژیم صهیونیستی به مناطق مسکونی در جنوب لبنان خبر دادند.
🔹
رژیم صهیونیستی دقایقی پیش یک منزل مسکونی را در شهرک «الکفور»  واقع در جنوب لبنان هدف قرار داد.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/687294" target="_blank">📅 01:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687293">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur1ts_xyuC1WpZQBrkM_VubEPNNIaIbcSyjK6G62-IhPsN-l0jURstlOJV1cpPUZx5y2AcmDDifiwFVDvwtOtemn7ZXzrpBfGtQcq3ATQ0TvPyYVjrdDVrjt4qKqa8rAGNtvxsxJDK_X0_Aoe_Mjx2actlYePx_cf2NYOdLUIzErSDn_nxhOCejwQjtAgz5PczOH92wE8Kcqf78tNxzePyU78ZeVYIm15wIgobznIpxFBz7gFWwDtR0hRloZRl6EaMHiYxX0GH4bCCy36Y38cIT0QsDK1zOo-_8CVt4vWxLMIlO6sY-ryuj-T1lYOubnoNlpg1mDSges6CcaVi9geA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت «زینب عواضه» خبرنگار شبکه المنار لبنان(رسانه رسمی حزب‌الله): اعلام سیطره بر تپه علی الطاهر من را به شدت یاد اعلام سیطره بر تنگه هرمز توسط ترامپ می‌اندازد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/687293" target="_blank">📅 00:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687292">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f087e0f339.mp4?token=kTLCUejsAoALgGCbGWK7_jTQGalrxEvmU1I6s-Rvgi8qClXOt4mbM8n-vRmPSHmqwHIO8KvsY0ZXW5t9F-EfZ60_Ytf-y9tplCoXN-CEhSmW6L_hi8L06Ln_K9Z68WKG5bm75Ue4rtePSu-BmMAsxqnC-50bCFA0rquOFp9Bsl9na_bc6oWjlfax40QRTNAK9vchaVxV-kgu01zFJUYfsUBNbIhwdPc63lsmNIk2SHpT82uj9lsD1zTJzCkVBXOJ_Tgld1lcJQNlo0HAxJkPWUMmGqueBWFQpNb0_2McgMoaFVuP0fzbB3kN1sBvaVc57GfKQ6j-Dt-M5_WJ_eltQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f087e0f339.mp4?token=kTLCUejsAoALgGCbGWK7_jTQGalrxEvmU1I6s-Rvgi8qClXOt4mbM8n-vRmPSHmqwHIO8KvsY0ZXW5t9F-EfZ60_Ytf-y9tplCoXN-CEhSmW6L_hi8L06Ln_K9Z68WKG5bm75Ue4rtePSu-BmMAsxqnC-50bCFA0rquOFp9Bsl9na_bc6oWjlfax40QRTNAK9vchaVxV-kgu01zFJUYfsUBNbIhwdPc63lsmNIk2SHpT82uj9lsD1zTJzCkVBXOJ_Tgld1lcJQNlo0HAxJkPWUMmGqueBWFQpNb0_2McgMoaFVuP0fzbB3kN1sBvaVc57GfKQ6j-Dt-M5_WJ_eltQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به یک واحد مسکونی در جنوب لبنان
🔹
رسانه‌های لبنانی از تجاوز جدید رژیم صهیونیستی به مناطق مسکونی در جنوب لبنان خبر دادند.
🔹
رژیم صهیونیستی دقایقی پیش یک منزل مسکونی را در شهرک «الکفور»  واقع در جنوب لبنان هدف قرار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/687292" target="_blank">📅 00:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687291">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NahMtwxnZWdC64en95DtNCHOKkPGiD0ePFL6bCVzaCE5rHjGVtWb4nGf0-h-ciBS3jxFQ5Y2ZPQLWrHEkn0jMSPTLP1hNXcFDU9nau-qPDttt7LcVBu-1_nYbrmOPOeUkHPjfPmRkMC9zYei4BaDkDf0HsbMaymN0RftBQOqVXcnP8mkaU7Zgqa0e7qea9S9fHIrXLDWdezVeAlFwyduDI6Z5Nvqy9dkt5WfjcRoGoHEXuRkCyltPx22wU8dctiHY6B0Tc4LB3VnV5amtAAXAv6Ju_8KEAeLM_w3BVPswqXJhWa_tIRqsNWmBsMx65V4wxssB0iUgKH4XQMyIivPYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: آمریکایی‌ها نباید بهای جنگ‌طلبی اسرائیل را با جان فرزندانشان بپردازند
اسماعیل بقائی سخنگوی وزارت امور خارجه در پیامی در شبکه ایکس با اشاره به مقاله منتشره در یکی از رسانه‌های اسرائیلی که در آن پیشنهاد شده است از دانشجویان بدهکار به شبکه بانکی برای سربازگیری جهت ادامه جنگ با ایران استفاده شود، نوشت:
🔹
آمریکایی‌ها، لطفا فقط یک سؤال از خودتان بپرسید: چرا باید به پسران و دختران شما وعده بخشودگی بدهی بانکی داده شود تا در ازای آن در جنگی بجنگند و کشته شوند که اسرائیل خواهان تداوم و گسترش آن است؟
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/687291" target="_blank">📅 00:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687290">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
پنتاگون از بیم ایران ردیاب‌های تبلیغاتی دستگاه‌های نظامیان را غیرفعال کرد
🔹
پنتاگون در بحبوحه نگرانی‌ها از حملات تلافی‌جویانه ایران، ردیاب‌های تبلیغاتی تلفن‌ها و رایانه‌های نیروهای آمریکایی را غیرفعال کرده است.
🔹
بر اساس گزارش‌هایی که روز جمعه منتشر شد، شاخه‌های مختلف ارتش آمریکا شناسه‌های تبلیغاتی دستگاه‌های الکترونیکی را غیرفعال کرده‌اند، زیرا نگران هستند داده‌های مربوط به موقعیت مکانی بتواند محل استقرار نیروهای آمریکایی را در اختیار ایران قرار دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/687290" target="_blank">📅 00:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687289">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
نیروهای مسلح یمن: هرگونه تجمع نظامی سعودی‌ها، هدف مشروع ماست
🔹
یک منبع نظامی یمنی در گفتگو با خبرگزاری «سبأ» ضمن محکوم کردن جنایات اخیر مزدوران سعودی، نسبت به هرگونه تحرکات نظامی جدید این ائتلاف در یمن هشدار داد.
🔹
حمله به منزل یک شهروند در «الجراحی»، جنایتی تازه در کارنامه سیاه دشمن سعودی و مزدورانش است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/687289" target="_blank">📅 00:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687288">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCFxtooSxU1xdpFaktQcepdT_796OO8ErdUx7LOuSYEXc2ZDTRznkQT6JgEs_-5JPGYFVMBou9Jvt9GCgHRHtu5S8FtXTSowbLGsE7HpD1XFx2waHBop9bjTsfH153n-sRB0vPqE60dACpKIUwDYDtai6wa6bPNTWhS6UJ36gfFc5tgfMYsWlhted-D_QQ-6AUKj4jEECJbWUIPlYFg-yc42GAQ7MykC2SaCTzmXK2LUC7KUg_Ag2d52TDg2-ZDTfxfv3kkA4K1FxiQxmw2mxCWR0GnBQLsbqw_eFX8spYYChbtTLKqXufA4nkvGVbKfLZdCm7ZvJxAeHhdFQG7qCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/687288" target="_blank">📅 00:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687287">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7fa489704.mp4?token=spVcGH-a-o5_XlhSFRCeZyUXTOn9OCxemvml8TRxoR5bZv9oYmj9o-Y8Bo6GhTJdgg-kg91TYZ3eeksYBswAJTtToLz-R_YGQ6ayNRI9dfHZifdIG7D-ppTtYKeSESHwKEQx5e_CsJJS3tt4h5czL49JEpzAqwpo2909Ra4ZMh2FtOkNSoyUOqKFDAXaYzKiQOpUYeVWiIronJh1feJ7vv4qAWrbaxg-aqARelYffmwUXATah6rrqK5MXWAJ0ksvHV8IQAuFwGO3VsxA2V8laNpwolwbes5jUsxjQr5ZhvWq1okyxQF5nXG3ggWLryKlTq8Ztx4t73Q_CMrAZfLoZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7fa489704.mp4?token=spVcGH-a-o5_XlhSFRCeZyUXTOn9OCxemvml8TRxoR5bZv9oYmj9o-Y8Bo6GhTJdgg-kg91TYZ3eeksYBswAJTtToLz-R_YGQ6ayNRI9dfHZifdIG7D-ppTtYKeSESHwKEQx5e_CsJJS3tt4h5czL49JEpzAqwpo2909Ra4ZMh2FtOkNSoyUOqKFDAXaYzKiQOpUYeVWiIronJh1feJ7vv4qAWrbaxg-aqARelYffmwUXATah6rrqK5MXWAJ0ksvHV8IQAuFwGO3VsxA2V8laNpwolwbes5jUsxjQr5ZhvWq1okyxQF5nXG3ggWLryKlTq8Ztx4t73Q_CMrAZfLoZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی مجلس: درصورت حمله به زیرساخت‌های اقتصادی ایران، تجارت منطقه فلج می‌شود
محمدرضا محسنی‌ثانی، عضو کمیسیون امنیت ملی مجلس در گفتگو با شبکه آرتی روسیه:
🔹
مطابق طرح پیشنهادی، کنترل دائمی تنگه هرمز باید به ایران سپرده شود و در عین حال، امکان عبور و مرور را برای همه کشورها - به جز آن‌هایی که دشمن ایران تلقی می‌شوند - فراهم می‌سازد.
🔹
حمله به زیرساخت‌های اقتصادی ایران می‌تواند تجارت منطقه را فلج کرده و طناب خودکشی را به دور گردن واشنگتن تنگ‌تر کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/687287" target="_blank">📅 23:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687286">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
سوخو۳۵ با این سامانه جنگنده‌های رادارگریز را پیدا می‌کند
🔹
سوخو۳۵ برای غلبه بر این چالش، به سامانه الکترواپتیکال و جستجوگر فروسرخ پیشرفته OLS-35 مجهز شده که بدون انتشار کوچک‌ترین سیگنال راداری و کاملاً غیرفعال، امضای حرارتی اهداف هوایی را شکار می‌کند.
🔹
این سامانه با بهره‌گیری از حسگرهای حرارتی با تفکیک‌پذیری بالا، پرتوهای فروسرخ ساطع‌شده از جنگنده‌های رادارگریز را از فاصله ده‌ها کیلومتری شناسایی و قفل می‌کند. مسافت‌یاب و نشان‌گذار لیزری OLS-35 نیز قادر است تا فاصله ۲۰ کیلومتری، اطلاعات دقیق مسافت و مختصات هدف را برای سامانه‌های هدایت سلاح و کامپیوتر کنترل آتش سوخو فراهم کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/687286" target="_blank">📅 23:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687285">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ارتش اسرائیل: پهپادی را که حزب‌الله به سمت نیروهایمان در منطقه امنیتی پرتاب کرد رهگیری کردیم و هم‌اکنون با حملاتی پاسخ می‌دهیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/687285" target="_blank">📅 23:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687284">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JztaNUkWok0i-u6aGaZUDSQk0FG6ZdDPGtD8wcpNynErkfUsC5CbksxeiuUTa-rysI__uuqYVQ1tDaCfd3-xCMsYg4Jpf2kIviy7RG9AayBeJZnEaOT0hxIuOUwiZP0T10m0eCakxJdxUsYjvezTCoqHrLmXdAg269ZNfcE9bzd4g_aNABLhUGHrqseMidoQYXjIgHxH_32OF8uNhbL6qfbg8p3wFs2tJJbJFvlbpuYsKuM4Tp33E-i_4xH8PjoxfovgwCPgbyao5WPqDtYVpAWZW5zjXH6gxtc7UL_vnWSGSHgNiJxY0Jrvc3aZ6Vzh29QxoSppJ0cFzcV_ptZRjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پادکستر سابق کالیفرنیایی به دلیل تهدید علیه جان ترامپ بازداشت شد
وزارت دادگستری آمریکا:
🔹
نیروهای مجری قانون یک پادکستر سابق ساکن کالیفرنیا را به اتهام تهدید علیه جان رئیس‌جمهور آمریکا بازداشت کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/687284" target="_blank">📅 23:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687282">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf5fabb0f.mp4?token=V2M9EvfgpoHs2bA6ZDsSN8AWlYVsI1DBWVl8gefnDFJcoSPMj55bArAtV3qBdiJmXfkDpilFi173p07N_wRBhITGGIUJjEzB_KpA85oZrJ0NRl6eFPE1Z2eTFFAhq1SP6_TeKKZor9txCVkggETw7JVHsG-caIxn9RAsKqtb9knlMOmRS0BTGQwPl7ToPVgyXwCKMm5sM_M9MrB7OOIzc0oS_kSMlbdEWS3BptxfNMzSfsfGWQz8mxv1T1eTDXPoUFY3YpO0z6GffdiOLOGLARTQMyAGx6gohOQJR_3nAlpyeIQaJPxsQ1wYPBfIAdafJzDS6MU_gWEqun8qYrFM2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf5fabb0f.mp4?token=V2M9EvfgpoHs2bA6ZDsSN8AWlYVsI1DBWVl8gefnDFJcoSPMj55bArAtV3qBdiJmXfkDpilFi173p07N_wRBhITGGIUJjEzB_KpA85oZrJ0NRl6eFPE1Z2eTFFAhq1SP6_TeKKZor9txCVkggETw7JVHsG-caIxn9RAsKqtb9knlMOmRS0BTGQwPl7ToPVgyXwCKMm5sM_M9MrB7OOIzc0oS_kSMlbdEWS3BptxfNMzSfsfGWQz8mxv1T1eTDXPoUFY3YpO0z6GffdiOLOGLARTQMyAGx6gohOQJR_3nAlpyeIQaJPxsQ1wYPBfIAdafJzDS6MU_gWEqun8qYrFM2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران آتشفشان بزرگ در آناک کراکاتوآ در اندونزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/687282" target="_blank">📅 23:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687281">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3560fd2134.mp4?token=KjnqUat5r5Nj91qSFQzToiTPNLrIJxpb_KLOK9hM-TzvxT3ZyrG_9YefvDf5DPTIhfNNe-ZwAfybjl1hprbeDbbl4TDUSxP7We96Vndp9ILkebcifJ_VR4e4Kij4EoVgbv5Tq6mn6hGFnvZ6XKFem3f0uL6fPZ3fqNSHWTfkJkSNRDO9hNK-3mBkWCoks2pcJbmXxvIAtyFT3DJ-wl3Zc0OY85ikJuhYhT1C3WXrMjwVyPtvwvOmz3oGue6X9csaMwPxzj_-OgbkFBSavRhGOfKXC-mvV-0u1PjYl71R532jn1yJP5Py_zDUFWb6mb86EQizwQqwMJ4l6AilLkZlbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3560fd2134.mp4?token=KjnqUat5r5Nj91qSFQzToiTPNLrIJxpb_KLOK9hM-TzvxT3ZyrG_9YefvDf5DPTIhfNNe-ZwAfybjl1hprbeDbbl4TDUSxP7We96Vndp9ILkebcifJ_VR4e4Kij4EoVgbv5Tq6mn6hGFnvZ6XKFem3f0uL6fPZ3fqNSHWTfkJkSNRDO9hNK-3mBkWCoks2pcJbmXxvIAtyFT3DJ-wl3Zc0OY85ikJuhYhT1C3WXrMjwVyPtvwvOmz3oGue6X9csaMwPxzj_-OgbkFBSavRhGOfKXC-mvV-0u1PjYl71R532jn1yJP5Py_zDUFWb6mb86EQizwQqwMJ4l6AilLkZlbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«تابان فردا» یکی از ستون‌های انرژی ایران شد
/
موفقیت گروه پتروشیمی «تابان فردا» در عرضه اولیه با مشارکت ۲ میلیون و ۹ هزار نفر در بورس تهران
🔹
مهدی عبوری، مدیرعامل گروه سرمایه‌گذاری اهداف، چند روز پیش از عرضه سهام «تابان فردا» هم‌زمان با ایام هفته دولت خبر داده بود. روز ۹ شهریور، سهام «تابان فردا» عرضه شد و بیش از ۲ میلیون نفر در این عرضه مشارکت کردند.
🔹
بزرگ‌ترین عرضه اولیه تاریخ بورس ایران با تکیه بر پرتفوی بورسی حدود ۴۹۵ همت، دارایی‌های عملیاتی و زنجیره‌ای از پروژه‌های نفت، گاز و پتروشیمی برگزار شد.
🔹
«تابان فردا» دارای پروژه‌ها و مجموعه‌های متنوعی در حوزه‌های پتروشیمی، نفت و گاز است؛ مجموعه‌هایی نو و غیر مستهلک مانند پتروپالایش کنگان، دهلران و فراسکو عسلویه، همچنین «نفت جی» که یک‌پنجم (۲۰ درصد) قیر ایران را تولید می‌کند و «نفت سپاهان».
🔹
طبق برنامه شرکت، حداقل ۷۰ درصد از سود محقق‌شده میان سهام‌داران تقسیم خواهد شد. «تابان فردا» برای سال جاری سود ۲۵ همتی را محقق کرده و این رقم برای سال ۱۴۰۹ به ۳۲۱ همت خواهد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/687281" target="_blank">📅 23:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687280">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
الجزیره: اسرائیل به نبطیه در جنوب لبنان حمله هوایی کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/687280" target="_blank">📅 23:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687279">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
آمریکا سه نهاد مالی را در ترکیه به فهرست تحریم‌های ضدایرانی اضافه کرد
🔹
دفتر کنترل دارایی‌های خزانه‌داری آمریکا نام سه نهاد فعال در زمینه مسائل مالی و بیمه را به فهرست تحریم‌ها علیه ایران اضافه کرده است.
🔹
این شرکت‌ها همه در ترکیه مستقر هستند./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/687279" target="_blank">📅 23:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687278">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
حمله مجدد رژیم صهیونیستی به جنوب لبنان
🔹
شهرک میفدون در شهرستان نبطیه در جنوب لبنان هدف حمله هوایی رژیم صهیونیستی قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/687278" target="_blank">📅 23:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687276">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3456c18c13.mp4?token=dfEeDXUYMWZlrD65u8PbE-MttGmZ6f7mFpTUWjjvdOJ2oIa3aCqcIvQZkmmxz8YRsRC56mNeYS5TXtrowG7zai4lAd4hhqubvzhMBF5bKRICTn8gH9Q-HI0v0Vs5Qvd75bk_vBfFwzBPNC5onM_OTw8ZhuQC_-kO0Et2toOtcSwJx86AzgqPdA9QY2UANMNOVGIFwheWf0fBNiy_i-H5M0lOzFQVQ5iBXqFPsE36SU3fYYchBAvFZ7Ld5Ssc6RocLedKyC7VPIk3YDIEAaYYxgmbApXzyOlhCYRxzCbzN4K5vbTwAjE95jbBQdx1-SLOZauB0vOtZGytrOBcpnB8Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3456c18c13.mp4?token=dfEeDXUYMWZlrD65u8PbE-MttGmZ6f7mFpTUWjjvdOJ2oIa3aCqcIvQZkmmxz8YRsRC56mNeYS5TXtrowG7zai4lAd4hhqubvzhMBF5bKRICTn8gH9Q-HI0v0Vs5Qvd75bk_vBfFwzBPNC5onM_OTw8ZhuQC_-kO0Et2toOtcSwJx86AzgqPdA9QY2UANMNOVGIFwheWf0fBNiy_i-H5M0lOzFQVQ5iBXqFPsE36SU3fYYchBAvFZ7Ld5Ssc6RocLedKyC7VPIk3YDIEAaYYxgmbApXzyOlhCYRxzCbzN4K5vbTwAjE95jbBQdx1-SLOZauB0vOtZGytrOBcpnB8Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شهریور، خریدت با اسنپ‌پی BMW داره!
🚘
✨
از ۱ تا ۳۱ شهریور، با هر خرید از اسنپ‌پی، چه آنلاین، حضوری یا از شبکه‌های اجتماعی شانس برنده شدن
BMW 225L
بگیر تازه با انجام ماموریت‌ها می‌تونی شانست رو بیشتر کنی!
🔥
🎁
هر هفته به مدت ۵ هفته، ۵ برنده:
💻
مک‌بوک ایر M4 |
🪙
۵ گرم طلا |
📱
آیفون ۱۷ |
📲
گلکسی S25 FE |
🎮
PS5
با
اسنپ‌پی ۴ قسطه و تخفیف‌دار
خرید کن و شانس‌هات رو بیشتر کن.
😎
💙
https://l.snpy.ir/j5cfo
https://l.snpy.ir/j5cfo
https://l.snpy.ir/j5cfo</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/687276" target="_blank">📅 23:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687275">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310606bd55.mp4?token=DYBI9cTdDIHrRC0lEG6hQtfBaWXb1n7xz2TzTCqPOZToGttIlL3E8kSOalZgH2Cu9IX4x9dWTuPVOg0oWF6yv2rONzpPXWKFLRzf3ZHPzI53y-1AdjzY1tyrjZvfT0M57odCbKixB0JfIudRVyCtVqJ942yA5boCaWsks6UzioNYiSLb2-jCntefAhpJJ1BhE9f0GoR7yLZo2CrVwy8YVJoYxl9gLNa9EdqRqLVt5MRk6LuDzaAuaux_TRZkd4DICx2qQCy1NDUhHDBTHAJTSj7HrTPntZN5QoPjsySw60VO4hWSxEHbvEeX2AQBiyVsCj4t_BRplg6M0wZhLzjUYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310606bd55.mp4?token=DYBI9cTdDIHrRC0lEG6hQtfBaWXb1n7xz2TzTCqPOZToGttIlL3E8kSOalZgH2Cu9IX4x9dWTuPVOg0oWF6yv2rONzpPXWKFLRzf3ZHPzI53y-1AdjzY1tyrjZvfT0M57odCbKixB0JfIudRVyCtVqJ942yA5boCaWsks6UzioNYiSLb2-jCntefAhpJJ1BhE9f0GoR7yLZo2CrVwy8YVJoYxl9gLNa9EdqRqLVt5MRk6LuDzaAuaux_TRZkd4DICx2qQCy1NDUhHDBTHAJTSj7HrTPntZN5QoPjsySw60VO4hWSxEHbvEeX2AQBiyVsCj4t_BRplg6M0wZhLzjUYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ  دروغگو درباره تنگه هرمز: همین حالا خطوط لوله در حال احداث هستند
🔹
مسیر جاده‌ای از طریق سوریه در حال ساخت است؛ در واقع، این مسیر باز است. مردم با کامیون‌ها از طریق سوریه عبور می‌کنند؛ کامیون‌های بسیار بزرگی که نفت حمل می‌کنند.
🔹
راه‌های جایگزین…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/687275" target="_blank">📅 22:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687274">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
نگرانی نیروی هوایی آمریکا بابت از دست دادن ده‌ها  پهپاد MQ-9 ریپر در جنگ علیه ایران
وبگاه دیفنس اسکوپ:
🔹
نیروی هوایی آمریکا روند جایگزینی پهپادهای MQ-9 ریپر را پس از تلفات جنگی در جنگ با ایران تسریع می‌کند
🔹
از دست دادن ده‌ها فروند پهپاد MQ-9A در طول جنگ با ایران، نیروی هوایی آمریکا را بر آن داشته تا برنامه‌های خود برای جایگزینی این پهپاد را بازنگری کند. مقامات اکنون به دنبال این هستند که یک جانشین ارزان‌تر را در تعداد زیاد و با سرعت بسیار بیشتری به میدان بفرستند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/687274" target="_blank">📅 22:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687273">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
هشدار ایران به کره جنوبی؛ اعتبار خود را فدای آمریکا نکنید
🔹
شبکه خبری المیادین شامگاه امروز جمعه به نقل از یک مسئول بلندپایه امنیتی-سیاسی ایران گزارش داد که کره‌جنوبی نباید منافع و اعتبار خود را فدای سیاست‌های تجاوزکارانه آمریکا کند.
🔹
این مقام که اشاره‌ای به نامش نشده است: به کره‌جنوبی هشدار می‌دهیم که تهران هرگونه مشارکت این کشور علیه ایران در تنگه هرمز را به منزله مشارکت نظامی در جنگ تلقی خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/687273" target="_blank">📅 22:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687272">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار درباره ایران: من به رئیس‌جمهور شی گفتم: «لطفاً درگیر ایران نشوید»
🔹
چین واقعاً درگیر این موضوع نیست؛ دخالت چین بسیار اندک است. چین می‌تواند دخالت بسیار بیشتری داشته باشد. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/687272" target="_blank">📅 22:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687271">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ترامپ متوهم: به جنگ‌ها پایان دادم ولی به من جایزه نوبل ندادند
🔹
من به ۸ جنگ پایان دادم و هیچ اعتباری هم بابت آن نصیبم نشد. آیا جایزه نوبل را گرفتم؟ نه؛ با اینکه کسی که آن را گرفت، آن‌قدر لطف داشت که جایزه‌اش را به من تقدیم کند.
🔹
هیچ‌کس در تاریخ جایزه نوبل…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/687271" target="_blank">📅 22:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687270">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b727bcb7.mp4?token=WhP1ekBWWao9ZCK3nM56qgH4c0KUBO63unULRfMFQEBIuF9DBft3Zr2CVOmTIcTebTcydbpv-bp9YSTnpnmHQHAVxw7hfFDS4IL3yBrCQLylgKdA3P27y1c_d5leJKdnRP9dLy90r1gCM1ondKZq_iY7WQVRZLRjF68jBy3sv9iNgnFnVtr3_6CC5I-CvaX0Y7kjFSOwI3E5ItpBzwDzXKbHFxwzT-58NrMiSiauaEdyGdXT0UJnW1WAjIjIClle4NvTIIaPW3DHHWvb3oO4HBQ0qO2ftdl0kPJ_OoSBY1DP4qWGqNxZ2-_3s-UFkUqJvI1VRbmHGa5hxwow6Pl2-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b727bcb7.mp4?token=WhP1ekBWWao9ZCK3nM56qgH4c0KUBO63unULRfMFQEBIuF9DBft3Zr2CVOmTIcTebTcydbpv-bp9YSTnpnmHQHAVxw7hfFDS4IL3yBrCQLylgKdA3P27y1c_d5leJKdnRP9dLy90r1gCM1ondKZq_iY7WQVRZLRjF68jBy3sv9iNgnFnVtr3_6CC5I-CvaX0Y7kjFSOwI3E5ItpBzwDzXKbHFxwzT-58NrMiSiauaEdyGdXT0UJnW1WAjIjIClle4NvTIIaPW3DHHWvb3oO4HBQ0qO2ftdl0kPJ_OoSBY1DP4qWGqNxZ2-_3s-UFkUqJvI1VRbmHGa5hxwow6Pl2-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ قمارباز: پوتین به دنبال حمله به قلمروی ناتو نیست  رئیس دولت تروریستی آمریکا:
🔹
من با پوتین صحبت می‌کنم، او را خیلی خوب می‌شناسم. پوتین به دنبال حمله به ناتو نیست. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/687270" target="_blank">📅 22:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687269">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b727bcb7.mp4?token=aZ5pDWYexsEMDff1fTNuxoSY1_1HUCeLG5zoDeTNoljfhozvnP1jrb4XQRuYmM52xSfjr3FzxCGEmO3adM3WAijOdV1b3OQTt0Ba5_MV7bpRev41OHtZwpTUsjgljLpgy1O3Ii6VXQufhMHaCeXCT80J9oov41ScxnA3ceCIxTnxCM6As2fX0Yu3l8xywjbr9DxM4uE1PwrfYmtTfWwJnYCGvW4lQCnTP-NL1KDuTg58v848wcD6k5kns8Qm3WpSzxv5t5GxO5t4n0gKnv9e3_k2eZiRE2EdP8svr46lnxfaS_X65Hb1a21TjO-b5lxwOjpoYfj--9qeC5qFMAOKBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b727bcb7.mp4?token=aZ5pDWYexsEMDff1fTNuxoSY1_1HUCeLG5zoDeTNoljfhozvnP1jrb4XQRuYmM52xSfjr3FzxCGEmO3adM3WAijOdV1b3OQTt0Ba5_MV7bpRev41OHtZwpTUsjgljLpgy1O3Ii6VXQufhMHaCeXCT80J9oov41ScxnA3ceCIxTnxCM6As2fX0Yu3l8xywjbr9DxM4uE1PwrfYmtTfWwJnYCGvW4lQCnTP-NL1KDuTg58v848wcD6k5kns8Qm3WpSzxv5t5GxO5t4n0gKnv9e3_k2eZiRE2EdP8svr46lnxfaS_X65Hb1a21TjO-b5lxwOjpoYfj--9qeC5qFMAOKBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: ویتکاف و کوشنر در حال بردن پیشنهادی به مسکو برای پایان دادن به جنگ هستند #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/687269" target="_blank">📅 22:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687268">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJRpvuuWRwWWTz6RvOP_GbFSZepSK-zPkEa-ip8hPnWGOs_aroca2LDnqV_dHtHlnZUywO-2nEbQeTeT5FkazIeD_b4HfGp4OaXmwgg5megSPzsAQg5Z4m5gnhKJ0YfPbWkSmNEfgdTp1psHTcQKRpa6I9_Cc6rLkB2rtVt8j9QP17PyenYiZsH8-v7H2QSuNBbQrZdrBAHlaAP12d4Y-5GXBHf9F1Z1o4RA5KEv1K-HO1i27LWzWxpo5GVlB_74pexPyILOZpsm0PFyv4f-isUQ3MV0mOMQ093h4Sdm7rXy6l7D2crd7fLzLK-YakUdExy2cmJ6nZQskUsWGSWPwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا؛ ابر قدرت زنگ زده‌ای که کسی نباید در مورد آن حرف بزند!
‏ناو آبراهام لینکلن که قرار بود نماد قدرت دریایی آمریکا باشد، بعد از ۲۸۶ روز مأموریت با بدنه‌ای زنگ‌زده و گزارش‌هایی از شرایط سخت زندگی خدمه وارد تایلند شد. حالا گاردین گزارش داده ملوانان این ناو هم از مصاحبه با رسانه‌ها درباره شرایط آن منع شده‌اند.
به توییتر خبرفوری بپیوندید
👇
https://x.com/akhbare_fori/status/2095856638485839910?s=46</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/687268" target="_blank">📅 22:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687267">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار درباره ایران: آنها رادار نصب کردند، زیرا ما قبلاً آن را از کار انداخته بودیم. حالا ما آن را برای بار دوم از کار انداخته‌ایم، اکنون ما هیچ فعالیتی را مشاهده نمی‌کنیم #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/687267" target="_blank">📅 22:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687266">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز درباره ایران: ما همه کسانی را که در «کوه کلنگ» در حال جابه‌جایی هستند، می‌شناسیم
🔹
ما همه کسانی را که در سراسر ایران در حال جابه‌جایی هستند، می‌شناسیم و اگر اتفاق بدی بیفتد، به آنها حمله می‌کنیم؛ آن‌هم به‌شدت #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/687266" target="_blank">📅 22:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687265">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ترامپ قمارباز مدعی شد: ممکن است به‌زودی به کوه کلنگ در ایران ضربه بزنیم #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/687265" target="_blank">📅 22:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687263">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
مدیرعامل رایتل: رقابتی با دو اپراتور دیگر نداریم/ می‌خواهیم زمین بازی را تغییر دهیم
مهدی فقیهی، مدیرعامل رایتل در
#گفتگو
با خبرفوری:
🔹
تلاش می‌کنیم زمین بازی را تغییر دهیم؛ رقابت مستقیم در بازار B2C با دو اپراتور مسلط، برای رایتل می‌تواند هزینه‌بر و دشوار باشد، بنابراین به دنبال ورود به میدان‌های جدید و خلق فرصت‌های تازه هستیم.
🔹
هدف ما این است که با هزینه کمتر و بهره‌وری بیشتر، در این میدان جدید منافع بیشتری برای سهامداران و مردم ایجاد کنیم.
🔹
با وجود تمام چالش‌های اقتصادی، وظیفه حرفه‌ای خود می‌دانیم که برای توسعه و ایفای نقش خود نهایت تلاشمان را به کار بگیریم.
🔹
وظیفه اصلی ما خدمتگزاری به مردم و ایجاد ارزش برای صنعت و ارائه خدمات به دولت است و این مسئولیت را فارغ از شرایط سیاسی و اقتصادی دنبال می‌کنیم.
گفتگوی کامل را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3242716</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/687263" target="_blank">📅 22:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687262">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a67e37317b.mp4?token=kiMqM28JTnW0Ux7SQpwK3v3WSADHs0uMi8-drwrgzpxBp_V47-gX_4wPI1ujdwCGmEptIz9qlU93YYFei4u34hkpArnxZt1dc8UwHCZUNZP5CioqH4Dnz7O2KS9j6t2EEEdbNtDltyczt_3rLI-uATvmzY6zuTC6_qAjiXKXVApsUD1UpCu-XW4mCBLm9KyxCJt0AMYFUvs6k4BOMMM6Ywqejw3aHFLy4dW-2gHtx2TEMM6qvI8AfPArIESrp16SX-KRvA17DEQOJr2os8wAoMn6qv61xnUW7rejpDmQmphzscIJXIXNzy_bdFp9mY4zk7AX8RrkuxSMubt8uhxFtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a67e37317b.mp4?token=kiMqM28JTnW0Ux7SQpwK3v3WSADHs0uMi8-drwrgzpxBp_V47-gX_4wPI1ujdwCGmEptIz9qlU93YYFei4u34hkpArnxZt1dc8UwHCZUNZP5CioqH4Dnz7O2KS9j6t2EEEdbNtDltyczt_3rLI-uATvmzY6zuTC6_qAjiXKXVApsUD1UpCu-XW4mCBLm9KyxCJt0AMYFUvs6k4BOMMM6Ywqejw3aHFLy4dW-2gHtx2TEMM6qvI8AfPArIESrp16SX-KRvA17DEQOJr2os8wAoMn6qv61xnUW7rejpDmQmphzscIJXIXNzy_bdFp9mY4zk7AX8RrkuxSMubt8uhxFtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: اگر درگیری با ایران جنگ نیست، پس دقیقاً چیست؟
ادعای ترامپ:
🔹
من آن را یک «درگیری نظامی» می‌نامم، چون برای ما چیز چندان مهمی نیست؛ مسئله بزرگی نیست
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/687262" target="_blank">📅 22:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687259">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lwopulT2jwmhO-1Zkew1nEs8Ua5Clh5nfVlhS7WRdwH1puDW52_AZlB94IkTFEqYV7kxl-Gf3bEyHVLm5jYbSVblHRZjzpBsIkjR2LZa424F7fnukBZmVtMCw3MbH0rd1aENdJo_UsJ3hpR9QHeL9FDjo0bwhL12Ro8ajvmAE2OSd8aKL7nAOo_72Ycwd2z5AFJYEf_DT9NJFbvMVGKSHa0MpF5v4hDsom_t_2xWAWRDF9kqFR9nqsTVUBQx9og_FOaxoa5pB5dyeIV8CqgnhgxKKbzXsPF5NVJfjdFfmaamRF0L3_vpPvifoq7upu2ngcA6dqusvK4FxUREvRIcAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0Tn_H1-Z10cICrwzKWl_SqAcD5gXWg5jwld_vdffJxEODRT_E3TIbrCQY5JoqYHFqKU4b7zKnEvF5nU8SI_XvIvzbttRAG_vMUNzpc4eZ-nrN3A_BF4V2199h8VcnjJ6XuMGCXo0bewaS11B_HXMaoonePeui9KmCVFqNE5uT-9cqTJwP4tRFuf4gg3cyIhATupMItjJgpA8EXWOCcgq0inoftrmNd9GBYJntoTq5865m75td_byxzuwMarH3fyvJ8fEVDTcdAUOZmOhw_ts9qcd67KFMdL_zPZwRb2mzjwg1uRHRsXEG0GsIdi5Y5A7OltiG5XzxbVP8IuN6EKLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گروه محبوب ماکان بند، پایان فعالیت خود را رسما اعلام کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/687259" target="_blank">📅 22:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687258">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb552738f.mp4?token=tD4j_zE74GEORJgpSdq79P9kCZWTcfLNIPyuS-AJbUD3piD6jQCLNdwDi7b5EUcxDljTWy09O8VwfbjPEbWUDQENupjJSV2OIAmJViV4UqMC3GySfw6ZDdQWr0U0K2EWa8jHuQzRhTDl_xpLqgbmzLku_rHG8f9dPnAaS51krOPuYz1lwGu9LM1XkNW85UbRMOwuQ-kgqvhEii3gLTEsOuCNniK0jZVxREFFs8OJrlp3jFMExWzDIOmvHgsT5OqhdnFW2VNSNMzvcZcLHy7CQ9lAqmApEYYqHbw0NhWBVHeAciAXP2g-ADbmmBmGVeeJX4P2eD1XD2n9PZUZuKi4bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb552738f.mp4?token=tD4j_zE74GEORJgpSdq79P9kCZWTcfLNIPyuS-AJbUD3piD6jQCLNdwDi7b5EUcxDljTWy09O8VwfbjPEbWUDQENupjJSV2OIAmJViV4UqMC3GySfw6ZDdQWr0U0K2EWa8jHuQzRhTDl_xpLqgbmzLku_rHG8f9dPnAaS51krOPuYz1lwGu9LM1XkNW85UbRMOwuQ-kgqvhEii3gLTEsOuCNniK0jZVxREFFs8OJrlp3jFMExWzDIOmvHgsT5OqhdnFW2VNSNMzvcZcLHy7CQ9lAqmApEYYqHbw0NhWBVHeAciAXP2g-ADbmmBmGVeeJX4P2eD1XD2n9PZUZuKi4bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار:‌ اگر کشوری با ما بدرفتاری کند، ما هیچ تعهدی برای انجام هرگونه تجارت با آن‌ها نداریم #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/687258" target="_blank">📅 22:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687257">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ee5445ea.mp4?token=hgf-rgZPNRhwchHBjI05m-EuuC3Dp2OqZzrxy34Yb1xMFJiBlImkUrygbYg8Jgf8YaPFSpI4BkEkp1W_q2L8SjjqSC7NfnlSHGK75OlEVbNVqIYQH8pT0NBRTv7X54mezfrn3sWu8FkayfAgIa5zeRFBTtJn2e4MPhSZWyABQ9THV_lejnwFtuJwWlMHtmynI1vFSFGtYcA934sl9_G1vZj7Z_Yd5uX62IqzrNqTraDgv_tZ-3QUEx-JRL5XaQ5WUUeTiX2M8DKrsNidTXDkwoHSGlUp8-i1sPNZYVVPshKYCBxrQT3OuUEhrAq6YofwA8YHVMGghCLLdOQIPsNWqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ee5445ea.mp4?token=hgf-rgZPNRhwchHBjI05m-EuuC3Dp2OqZzrxy34Yb1xMFJiBlImkUrygbYg8Jgf8YaPFSpI4BkEkp1W_q2L8SjjqSC7NfnlSHGK75OlEVbNVqIYQH8pT0NBRTv7X54mezfrn3sWu8FkayfAgIa5zeRFBTtJn2e4MPhSZWyABQ9THV_lejnwFtuJwWlMHtmynI1vFSFGtYcA934sl9_G1vZj7Z_Yd5uX62IqzrNqTraDgv_tZ-3QUEx-JRL5XaQ5WUUeTiX2M8DKrsNidTXDkwoHSGlUp8-i1sPNZYVVPshKYCBxrQT3OuUEhrAq6YofwA8YHVMGghCLLdOQIPsNWqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار:‌ اگر کشوری با ما بدرفتاری کند، ما هیچ تعهدی برای انجام هرگونه تجارت با آن‌ها نداریم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/687257" target="_blank">📅 22:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687254">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbizleEIR9niTp0LWzXHnwMvG0rqo4HmDEgBq5dmJ6dAwp-4mCLOV8Mfk4GBd4zPDcAo-TMx7mwaXXdlKVy8bIll6uhgya736Goln2Q47qtSpTlYjT0q7t3TypQVQa_NPDfawaWnwYWSklDFQeQQqk2huJUdM5VOPnqUXIK6CnmnPET5yABGFBPXNq5R2f2B8vC2w_6ULmzIGdUko7_smD7Idza18o6nEbH5dxOJ7-BCoacguPeOSnagpdqrpJ_50nLPMaS8w5HLsN7geNGkOZtqs1Z4pw3aiRw3p9y2raQh8KAQBvJ5lobCxzg2seP31cKh9ZGgAfABNATYb6zXig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت بیمه تجارت‌نو از متقاضیان واجد شرایط در سراسر کشور، برای اعطای نمایندگی بیمه دعوت به همکاری می‌کند.
🔹
بدون نیاز به سرمایه اولیه
🔹
آموزش و پشتیبانی مستمر
🔹
امکان فعالیت تمام‌وقت یا پاره‌وقت
🔹
برخورداری از بیمه تکمیلی برای نماینده و خانواده
🔹
تسهیلات و طرح‌های حمایتی ویژه نمایندگان
🔹
امکان رشد و توسعه فعالیت و راه‌اندازی دفتر نمایندگی
این فرصت می‌تواند گزینه‌ای مناسب برای افراد جویای فعالیت حرفه‌ای، شاغلین، دانشجویان و علاقه‌مندان به صنعت بیمه باشد.
📌
ثبت نام مستقیم درخواست نمایندگی
👇
:
🌐
tjrt.ir/a/life-agent
ظرفیت پذیرش در برخی شهرها محدود است.</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/687254" target="_blank">📅 22:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687253">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CES9Q31kdnlpbUkS9LrEaoqDeSQBG39R8-um_sT2Lde0KLzBLjKCD7LZMowPKSI4y1iCCOuqYEwUFT_dgyPjLwzMtdsRP2DQCQH5me98LndnjoFzfzcnIzD4ihBT9YGRTbRqZTqG0eBqVOadV-Anru6oxxUF0mpHTkM3wPQZJ6T4RbYdJ9ROZEtdc-vie0GCq74LYfEi07I4hilF5ZYJWiXAY8X8WLjdK3ZfLoyoH1TGTk7KWlULbdHEIzp0XJCuaLqiHvN34SWoqak_Pee6HVkZ-_a0d1iJr-HzTTT_E7-ze7OHTI2HXpUX5qsC0tbv8RHrFbkGEgBsFENOU1wE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند قدم تا یک فرصت دوباره برای زندگی...
یک دختر ۲۲ ساله، دور از پدر و مادرش و در بهزیستی زندگی می‌کند؛
پدری که به‌دلیل یک پرونده قتل، در انتظار اجرای حکم قصاص است.
در این پرونده، با تلاش خیرین و وساطت انجام‌شده، یکی از فرزندان مقتول رضایت داده و تنها برای جلب رضایت فرزند دیگر، ۲ میلیارد تومان  باقی مانده است.
اگر این مبلغ تأمین شود، یک پدر می‌تواند دوباره در کنار دخترش و حامی و پشتیبان او باشد.
🤍
سهم ما از این بازگشت، هرچقدر هم کوچک، مهم خواهد بود.
💳
شماره کارت: 6037997339543507
شبا: 900170000000315473984001
بانک ملی
به نام خانم محبوبه نوروزی
اگر امکان کمک ندارید، این پیام را منتشر کنید. شاید بازنشر شما، آغاز یک زندگی دوباره باشد.</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/687253" target="_blank">📅 22:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687250">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای وال‌استریت ژورنال؛ پنتاگون برای ادامه جنگ با ایران تا سال ۲۰۲۷ آماده می‌شود
🔹
ترامپ زمان تصمیم‌گیری درباره جنگ، پیامدهای انتخاباتی را در نظر نمی‌گیرد
🔹
جنگ با ایران به یکی از طولانی‌ترین دوره‌های استقرار نیروهای نیروی دریایی آمریکا در تاریخ معاصر منجر شده است
🔹
وال‌استریت ژورنال به نقل از منابع مطلع گزارش داد که پنتاگون در حال تمدید مأموریت نیروها، ناوهای جنگی و یگان‌های پدافندی آمریکا در خاورمیانه است؛ اقدامی که نشان می‌دهد واشنگتن خود را برای تداوم جنگ با ایران تا بخش قابل‌توجهی از سال ۲۰۲۷ آماده می‌کند، هرچند این حضور طولانی‌مدت فشار سنگینی بر نیروها، تجهیزات و توان عملیاتی ارتش آمریکا وارد کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/687250" target="_blank">📅 21:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687248">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔹
خبرهای داغ امروز را در وبسایت خبرفوری کلیک‌کنید
🔹
🔹
حملات پیش دستانه ایران علیه پایگاه آمریکا در اردن؟
👇
khabarfoori.com/fa/tiny/news-3242721
🔹
طلای ۱۸ عیار از ۲۳.۵ میلیون تومان عبور کرد
👇
khabarfoori.com/fa/tiny/news-3242723
🔹
رونمایی از کفش ۱۰ میلیارد تومانی در تهران | جنجال یک جفت کفش به قیمت یک خانه
👇
khabarfoori.com/fa/tiny/news-3242687
🔹
اعتراف ناخواسته ترامپ به عدم پیروزی در جنگ علیه ایران
👇
khabarfoori.com/fa/tiny/news-3242559
🔹
شهرک اکباتان مصادره شد | عکس
👇
khabarfoori.com/fa/tiny/news-3242681
🔹
خبرهای جذاب هر روز را اینجا دنبال کنید
🔹
http://khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/687248" target="_blank">📅 21:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687246">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InfgXL23ZYC2t7AEdvtwhdyHy5nRHa_FgcYyTe0EMC1uqKVVIaj0jQMQJo7DAbQBzl83XC3Txhq3gZzs5p-MhTogJT2Bu58WmUgXz55KHPkfpmn4-mV7H5Npw3vchjVeSPahlHd-kZtgUQAmzXJ_infxpOjGbIkFcBCP5KfzJcv1fJ44kE9baCSu4KCcOAYxgmCFwnNJUrk7r4x0Dx27BQNdTg2cf5XAv3LWMqIXPZVBVj9LEKuXTCwCDyDU3SHBu9N7oI5ADtEwQjxplJSf3MAnVSG7dG42kfojfaOdIhqkOiOT7WiGBHPb4wf0AbUiUdNg-MmCo7bAia8LK5n4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تپه‌ای که می‌تواند جرقه جنگ دوباره باشد | چرا «علی‌الطاهر» به کابوس تازه اسرائیل تبدیل شده است؟
🔹
در چشم‌انداز کوهستانی جنوب لبنان، تپه مرتفع «علی‌الطاهر» به یکی از مناقشه‌برانگیزترین و حساس‌ترین خطوط تماس در درگیری‌های میان ارتش اسرائیل و نیروهای حزب‌الله تبدیل شده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3242622</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/687246" target="_blank">📅 21:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687245">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
وجود روحیه استقلال‌طلبی جوان ایرانی مظهر شکست آمریکاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/687245" target="_blank">📅 21:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687244">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
خبرها از موج انفجارهای جدید در آسمان پایگاه الازرق(محل استقرار تروریست‌های آمریکایی) در اردن حکایت می‌کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/687244" target="_blank">📅 21:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687242">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOryDIYyoO38CW1lXyorNhnl4vDOV5iJgByCPxZUzsO7UYeeHw9urDJNVhAFPGQ76cfkZYC0r-2opr3u3mQuqRcP87pjVDm_qi-N1JV-eIpoC8syzG_kicjO1zuM0jWbAFk_AJHTtO8x-A42Y48uGa3bhvD3Hk8_AIrfj0bIVnA9RoCsBF6pKG8vTRTK_suJYts5pplBhl61hLM0qsDViVBT3qMozfPGaZpU0QwcRjdzs-q8QP33u3natnK3BbzlLirwuVtEKLvm_pwBafPejnH_8i3mYYTybCciRydsB2xW6NqOxI5b2qT5cQNcYumP8zqJ-OakYEfr4OVWkLRSPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه کلیدی دو قدرت بزرگ؛ آمریکا و روسیه
🔸
بررسی آمارهای بین‌المللی نشان می‌دهد آمریکا با بودجه نظامی ۹۵۴ میلیارد دلاری (۵ برابر روسیه) و صادرات ۱.۹ تریلیون دلاری برتری اقتصادی چشمگیری دارد، اما بدهی سنگین ۱۱۵ درصدی از GDP چالش اصلی آن است.
🔸
در آن سو، روسیه با بدهی پایین ۱۸ درصدی، در ذخایر عناصر کمیاب زمین با ۲۸.۷ میلیون تن (۱۵ برابر آمریکا) دست بالا را در اختیار دارد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/687242" target="_blank">📅 21:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687241">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COh2s3sfG_-dsBDqgEXozSDV66_JJFze_PO8Qgrxmbqia69QNpzf8PXIgw_Xmk6wbU7B_PDX-r6fhZANIfaqVGs_SUbI8jxqDR7RPqW2oO9aUzrRpezO6hXLu-T0JD3xmgkvKI8FVfQltv5vbxT4E5-AvI_6cO0clj1Ecx-t7Uy9_zbSL_tTuT4LHojZWe-ye8Z9fx9Vmp37q2GLs-1lBj47kn7iNFcvBIE72-73MeFYosQTxf6mAXOMH15ntdjPJ5eZpLDJ5D3ljUF2XnjvRddFdrRHIoRxYblPzd4NyoIimDuUfNGSoa-HpEoJDqAh5ywy7dqsCyDpKViqsUMhNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: ارزیابی اطلاعاتی آمریکا؛ ایران برای طولانی‌کردن جنگ و تشدید درگیری آماده می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/687241" target="_blank">📅 21:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687239">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bus8vKvIFncd9ZnVVFXB0HDeix-Fi1ecm80nSdVMfIeZlIYQkiKi956oXCAIF-WtYmfgzQrrvmAkmlwcwydmdgDmL7lfJiHoxUTcMiDa9ofshKa-70fUslMQXXkvJf7DlBsdMp1HWeGKoaQ9ka42j2TdvYYN9lmfeT8rKcGFUACxlEbL_pz2jenT9BfBu6M20L-vs4jpnD78Em8tYCrI7l7iI4t3MIQ1qo1PFzpma8DyMg_6-0vHfbnm1LSqYCekVYDOYjQ_O1eljpSWzlDI-h50_EEC452Hi8MMpxPLEmLtLf_fV0qiLMpDJEFOJFrjkACyqq8vVL6uah8FUURw_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احتمال جنگ گسترده بین ایران، آمریکا و اسرائیل وجود دارد/ این نقطه، محور اصلی درگیری واشنگتن و تهران خواهد بود
🔹
یک کارشناس مسائل سیاسی با اشاره به تشدید دوباره درگیری‌ها میان ایران و آمریکا، تنگه هرمز و فشارهای اقتصادی را از مهم‌ترین محورهای تقابل دو کشور دانسته و می‌گوید: واشنگتن پس از ناکامی در دستیابی به اهداف نظامی خود، فشار اقتصادی و تهدید نظامی را همزمان دنبال می‌کند.
مشروح گفتگو را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3242652</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/687239" target="_blank">📅 21:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687237">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24c21344.mp4?token=CS1Zxv--P3-DpJxnhGxbrLUe1WYM08rfP0oxC2rDcSI7h4w8AUMQ4z_aeQx1xuLMukCQwDLVggDybIpJY9K5bhODrrwRcPu1Kb9meao-OCuzLB0l7xmYyr7wLdczPZtQIPv5QFShut_j0rDYFiZ7gzJtx6d6VEu0jsenv9wh_XY-q0Uq_DXtkayRmOhaJI9VpLaCRBdLB5bs85J1m2LQ1i97gK4fdV0u0tk1OGB6WhlO2P8XoK11To02HkV4vTchGRevu8XcS4Ftgkf5G_lu64ondblULEq1PClclzFAhoPRxHl6Y6fiY4p7b5v54nH-yy-9F3xE-5GyIGzHguHQ50W3gBSPsLxW30-uD-ewCdK6AqdQ9_UNEJpVWLp469Am2ujVgHTW1XMTlSICPm9XT_If-HlYyPcTrsnWUwrWsM1X_lbIPpwok_aSNR8YT9KhyQQMiNoNTlAiEaXPWr5reGXNa6B5hNukJMZDwbnlROsacWi_Xx8RTfcLfAy1ZTIvbd__jXoCqBR-UPhEJbc7Ir__2gbEg3MC-FQb1GAAq-Ioe8FMvbIX8zdfWPfnJlWJ2kWuQC5joMepStbN_JCZ0iXmqJ2og2NcWRnL_SaNexx1VdPtgkrpPFnr6tn8DsXF4VgJSdQ_a0oge0cmE-IpCWD-WNWYd_rRaXAOshawr48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24c21344.mp4?token=CS1Zxv--P3-DpJxnhGxbrLUe1WYM08rfP0oxC2rDcSI7h4w8AUMQ4z_aeQx1xuLMukCQwDLVggDybIpJY9K5bhODrrwRcPu1Kb9meao-OCuzLB0l7xmYyr7wLdczPZtQIPv5QFShut_j0rDYFiZ7gzJtx6d6VEu0jsenv9wh_XY-q0Uq_DXtkayRmOhaJI9VpLaCRBdLB5bs85J1m2LQ1i97gK4fdV0u0tk1OGB6WhlO2P8XoK11To02HkV4vTchGRevu8XcS4Ftgkf5G_lu64ondblULEq1PClclzFAhoPRxHl6Y6fiY4p7b5v54nH-yy-9F3xE-5GyIGzHguHQ50W3gBSPsLxW30-uD-ewCdK6AqdQ9_UNEJpVWLp469Am2ujVgHTW1XMTlSICPm9XT_If-HlYyPcTrsnWUwrWsM1X_lbIPpwok_aSNR8YT9KhyQQMiNoNTlAiEaXPWr5reGXNa6B5hNukJMZDwbnlROsacWi_Xx8RTfcLfAy1ZTIvbd__jXoCqBR-UPhEJbc7Ir__2gbEg3MC-FQb1GAAq-Ioe8FMvbIX8zdfWPfnJlWJ2kWuQC5joMepStbN_JCZ0iXmqJ2og2NcWRnL_SaNexx1VdPtgkrpPFnr6tn8DsXF4VgJSdQ_a0oge0cmE-IpCWD-WNWYd_rRaXAOshawr48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات جنجالی خبرنگار ارشد بی‌بی‌سی: ادعای تسلط ارتش اسرائیل بر تأسیسات و نقاط راهبردی حزب‌الله، اقدام انتخاباتی نتانیاهو است و هنوز منبع مستقلی آن‌را تأیید نکرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/687237" target="_blank">📅 21:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687236">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای العربیه: حمله موشکی به شمال اردن گزارش شده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/687236" target="_blank">📅 21:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687235">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
مدیرعامل رایتل: با تعرفه‌های فعلی، کسب‌وکار زیان‌ده است/ هزینه تجهیزات ۴۰ تا ۵۰ درصد گران‌تر از منطقه
مهدی فقیهی، مدیرعامل رایتل در
#گفتگو
با خبرفوری:
🔹
با تعرفه‌های فعلی، کسب‌وکار ما زیان‌ده است؛ قیمت اینترنت ما یک‌شصتم تا یک‌هفتادم کشورهای منطقه است، اما تجهیزات را به دلیل تحریم‌های ظالمانه ۴۰ تا ۵۰ درصد گران‌تر می‌خریم و دخل و خرج کسب‌وکار همخوانی ندارد.
🔹
نیازمند حمایت دولت و رگولاتور هستیم؛ متأسفانه این حمایت‌ها را بسیار کمرنگ می‌بینم. انتظار داریم نهاد رگولاتوری ناملایمات با اپراتورها را کاهش دهد؛ الان فضا، فضای جریمه و برخورد نیست.
🔹
اگر جرایم ادامه پیدا کند، ما را فلج‌تر می‌کند و ارائه سرویس به مردم با مشکل مواجه می‌شود.
گفتگوی کامل را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3242716</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/687235" target="_blank">📅 21:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687234">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvcGH1hzQxmE_WsA_GYqn3T5eBMbl39wUJ6cOov9HUGuqIs3dWWuHgdCyzUZNFznmoxh2F3ywqcCEK-nF6C4KPZ0J1XM4FVQ9LWaoUqiV60m1XzWQyOBImnAZ_jHASeeFehiV9eWcmRFVQI7zGzHIE1qwEu6Bq5SFR1VmpoPvLU-SNWgRwNWc4WHXEw0q97ARt9RViyFR8BZAEzA7PM_l_dzjC4M_X37dlDTJT2mSI3od48mi4zUL5HoRDICIxC4Fp0m7YyfwxJJ5wOty7Lyj3TyagG1JkK4gSz8Ux0ZJLWeXWxD4IAFTbojkn1PVGFHisx6O9lRPYWRS__EzjzEBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین وضعیت قیمت نفت
🔹
نفت آمریکا (WTI) ۹۰.۹۰ دلار
🔹
نفت برنت: ۹۵.۶۵ دلار
🔹
نفت امارات: ۱۰۲.۲ دلار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/687234" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687233">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de0709d3a.mp4?token=C81dE9yjrWtibuL6C5mjHt6uQSb5l-IGbobk-mnj1yhUo79Faqb027uguaiQpes_Sh4RGsUTwmUxKAwg4xVpx4g-CQfGMJlD3OYmXZp54qTG4AvJsOkjn-3q-zTGe4FgpkWv_Dl-YAfjNgivEJ9lCYEdwInqk1MZfQHgIgwU4wb35gr8lvA6bTAP4Nb_KHemqWjNSwyKNa2kUDhspnJ2uD5zKMCKUOk6bKgnWfXjIaj9l8aVA04q2vT8v5_5IdyWv1FKokxty_ck03c4UmcieoND53CFPh4MdUeMeCCvSivElEPqLqwpFhIZt8cog-r_OIJhIo6zevL5BU4khRgtfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de0709d3a.mp4?token=C81dE9yjrWtibuL6C5mjHt6uQSb5l-IGbobk-mnj1yhUo79Faqb027uguaiQpes_Sh4RGsUTwmUxKAwg4xVpx4g-CQfGMJlD3OYmXZp54qTG4AvJsOkjn-3q-zTGe4FgpkWv_Dl-YAfjNgivEJ9lCYEdwInqk1MZfQHgIgwU4wb35gr8lvA6bTAP4Nb_KHemqWjNSwyKNa2kUDhspnJ2uD5zKMCKUOk6bKgnWfXjIaj9l8aVA04q2vT8v5_5IdyWv1FKokxty_ck03c4UmcieoND53CFPh4MdUeMeCCvSivElEPqLqwpFhIZt8cog-r_OIJhIo6zevL5BU4khRgtfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: آن کسی هم که سطل زباله آتش زد، فرزند ماست، با وجود دشمنان، تکرار نشدن حوادث دی‌ماه نیازمند خردمندی و آگاهی مردم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/687233" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687231">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OD8k-sZ7hsnVvmKySCrg-uuyaRxwJgko0nFvuZKwqim_krQCdZqGZGaI-toWA4ZzRANfDLwaPPuUTnFxMg9sfV0i6EWsHhU1JbOCdCqP_IjXiEuNs3FJUa_uh3kw-EH3y6ZDzlic8Af6uReX_fgeKk2Bbqnw_kI2QCNovWLV3b5Sk-4PL7_pSZMkEFgiRrydOcGofHLNjlqlI5zlrdR872VfknOAHh2qglXwAQSL3YoISt6ycOH8hHIeUSRL43Hs8jiud3seup3Y4MvENaYjqhFmoFVrIhQHtXPZSPDb_OPwOsC25lDHYkSe98caLxGAtB5RuncdLq-OAGt9ROKkFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناو زنگ زده آبراهام لینکلن، نماد فرسودگی هژمونی آمریکا
🔹
ناو هواپیمابر «آبراهام لینکلن» متعلق به نیروی دریایی آمریکا که زمانی نماد قدرت و سیطره این کشور بود، این روزها پس از ۲۸۶ روز حضور در دریا، به دلیل فرسودگی و مشکلات فنی فراوان، سرانجام روز دوم سپتامبر ناگزیر در بندر«لائم چابانگ» تایلند پهلو گرفت. دیدن زنگ زدگی و فرسودگی بر بدنه و بخش‌های مختلف این کشتی که دوربین‌ها آن را ثبت کرده‌اند، ناخودآگاه تصویری از یک هژمونی پوسیده و نخ‌نما از آمریکا در ذهن هر بیننده‌ای ایجاد می کند.
در خبرفوری بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3242717</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/687231" target="_blank">📅 20:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687228">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-text">⁨ ⁨ کسب‌وکارتون رو به فرصت‌های بیشتر وصل کنید!
✨
💫
با «شهرآسا» بانک شهر، فعالیت پذیرندگان می‌تونه مزایای بیشتری برای کسب‌وکارشون به همراه داشته باشه؛ از تسهیلات و جوایز ویژه گرفته تا امتیاز و قرعه‌کشی ماهانه.
💳
با اتصال پایانه فروشگاهی یا درگاه پرداخت اینترنتی به حساب بانک شهر، از مزایای ویژه شهرآسا بهره‌مند شوید:
🔸
تا ۷ برابر میانگین حساب دریافت تسهیلات تا سقف ۱۰۰ میلیارد ریال
🔸
جوایز نقدی و هدایای ویژه اصناف
🔸
تجهیزات جانبی ویژه
🔸
تقدیر از پذیرندگان برتر
🎯
به ازای هر ۱۰ میلیون ریال تراکنش در ماه، یک امتیاز کسب کنید و شانس خود را برای برنده‌شدن در قرعه‌کشی جوایز ارزشمند افزایش دهید.
یعنی اینجا، فعالیت بیشتر می‌تونه فرصت‌های بیشتری براتون بسازه.
🚀</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/687228" target="_blank">📅 20:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687227">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lknyHINnZt_qLJB2PnwpwkZipWH3QR0lqnjb9iprYWwGSC208I7rEaRpZ77I6vbBknNQku_Rv47SwzJOnqXcdDXW3GkumRP6Ezjaho5KhCbutoCCBi_xBSJja2voJqrD7K3s86-GymDiieGt4QpqF8ilVzZX5Po2vgJgRxMNL3PoHbYjBS0JvTHGPTRL-q8ZpQ68WCxbq8CkKRwN7lQ9fThhxkDm_o265VvDMc9fEVWCvBFeSgQZSAl12KJNgW39F3zepITviXdfVDGpPn59L60HDEBxCcM-9wTzeem_YeiF3-QIv7rkYOS3yOnSfAAiuiMvvOo122fpT6szLak4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: کشورهای منطقه باید آینده خود را به دستان خود بسپارند
رئیس مجلس:
🔹
تأکید چین بر پرورش امنیت مشترک، اصلی را منعکس می‌کند که ایران مدت‌هاست از آن دفاع کرده است.
🔹
کشورهای منطقه باید آینده خود را به دستان خود بسپارند، و ثبات واقعی تنها از طریق معماری امنیتی جدید بومی می‌تواند به دست آید. ایران آماده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/687227" target="_blank">📅 20:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687225">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
موشک‌های ایران در آسمان اردن  جزئیات کامل
👇
khabarfoori.com/fa/tiny/news-3242721</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/687225" target="_blank">📅 20:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687224">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86f2c982f0.mp4?token=Uf7fTyeTM8MVjFqZLCRw2ZZSr0V3g4nJbQ5Rxc0WeGuSChjgBwOrlvl_S3EVijuiXqaYFyGcIQOtQAvJkpZub5IIrF1PtjWi-SNuTOCfacKv5Fn0drAOECl_qhmOKt1X9g8CB6C_YiFan3ZeqdMJ2Itw4P1PJqDU2xFytI1N5Q9ZD-Qzx95qjEAhuTx0rkJwF530S_pnAnVnDXVLInS5Mmy9a5OFWyT9AA6T8zLstdkG8fG2l_KybbD4P0tJHXTUxjzZYauUsEk9l5UVzdgPXmsW-BDdRwzp77q_rBKCMCUjA6VrRyd4IJ70exKhugB61DK6dayzBwrhsBdRR3qjlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86f2c982f0.mp4?token=Uf7fTyeTM8MVjFqZLCRw2ZZSr0V3g4nJbQ5Rxc0WeGuSChjgBwOrlvl_S3EVijuiXqaYFyGcIQOtQAvJkpZub5IIrF1PtjWi-SNuTOCfacKv5Fn0drAOECl_qhmOKt1X9g8CB6C_YiFan3ZeqdMJ2Itw4P1PJqDU2xFytI1N5Q9ZD-Qzx95qjEAhuTx0rkJwF530S_pnAnVnDXVLInS5Mmy9a5OFWyT9AA6T8zLstdkG8fG2l_KybbD4P0tJHXTUxjzZYauUsEk9l5UVzdgPXmsW-BDdRwzp77q_rBKCMCUjA6VrRyd4IJ70exKhugB61DK6dayzBwrhsBdRR3qjlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌های ایران در آسمان اردن
جزئیات کامل
👇
khabarfoori.com/fa/tiny/news-3242721</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/687224" target="_blank">📅 20:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687223">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">11 Ane Manaee (1403-09-16) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/687223" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه یازدهم
حجت‌الاسلام امینی‌خواه:
🔹
عمل در آیینه هستی؛ تأملی بر جایگاه و معنای آن
🔹
نورِ عمل؛ چراغی که راه‌های بسته را روشن می‌کند [4:20]
🔹
نورانیت نماز شب؛ گشایش قلب، تغییر اخلاق [4:58]
🔹
شرح صدر؛ گنجینه‌ای برای دل‌های نورانی [7:31]
🔹
علم به فایده؛ کلید رفع نیاز و رسیدن به کمال [15:31]
🔹
تشکیک وجود در اندیشه ملاصدرا؛ شعور و محبت، در تمام مراتب هستی [19:27]
🔹
تجربه‌ نزدیک به‌ مرگ؛ وقتی سنگ‌ها هم انس و تعلق دارند [22:03]
🔹
لذت‌های حیوانی؛ وقتی انسان مسیر کمال را گم می‌کند [24:48]
🔹
آنجا که اراده انسان، محض اراده خدا می‌شود [31:25]
🔹
کمال انسانی؛ جایی که هیچ قدرتی را یارای مقابله نیست [35:30]
🔹
حلال و حرام؛ نقشه‌ای برای رسیدن به کمال انسانی [42:11]
🔹
صبر؛ کلید طلایی رسیدن به کمال انسانی [46:59]
🔹
لذت حقیقی؛ در گرو بندگی و انجام وظیفه [50:50]
🔹
چادر فاطمه زهرا (سلام‌الله‌علیها)؛ نجات‌بخش خیل عظیم خلائق در عرصات قیامت [59:11]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/687223" target="_blank">📅 20:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687222">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
فروش تجمیعی شرکت‌های شستا به بیش از ۵۷۰ همت رسید/بیش از ۵۰ هزار نیروی انسانی شستا در دل جنگ پای کار ماندند
محمدرضا سعیدی، مدیرعامل شستا در
#گفتگو
با خبرفوری:
🔹
علیرغم آسیب‌های جنگ، شستا نه‌تنها تولید و پایداری خود را حفظ کرد، بلکه آن را ارتقا داد. تاب‌آوری کشور در دل جنگ با تلاش نیروی انسانی شستا تقویت شد
🔹
یاد و خاطره ۴ شهید والامقام شستا را گرامی می‌دارم و از تلاش همه مدیران و کارکنان این مجموعه بزرگ تقدیر می‌کنیم
گفتگوی کامل را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3242509</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/687222" target="_blank">📅 20:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687221">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
خبرهایی درباره حمله به پایگاه‌های آمریکا در اردن
🔹
منابع خبری گزارش دادند پایگاه‌های آمریکا در اردن هدف حمله قرار گرفته است.
🔹
این منابع گفتند در پی این حملات، صدای چندین انفجار مهیب در مناطق مختلفی از اردن شنیده شده است.
🔹
منابع اردنی اما مدعی شدند این موشک‌ها…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/687221" target="_blank">📅 20:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687220">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
شنیده شدن انفجارهای قوی در اردن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/687220" target="_blank">📅 20:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687217">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
شنیده شدن صدای چندین انفجار در اردن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/687217" target="_blank">📅 20:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687216">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171f23100d.mp4?token=PqgBlhmUEZVWJ4Gf6rSxVQhKEJ5GKRWOYtN_42QV9VvNef1u2e4KUJHvQDxQZpbd6wYbGtlNN5TVOiHgT4Jy1yB26Y-PECtjfG673m-GSAMv4dMTLPtmcGjF0qqNIQ3DwS3r7QoyIdjsFDaQsDYYg6kGyu-EVc0d6gGhok660pZ-Y38wWtCMs2ZHJpuhSLFxxFoiWuG5MYFm3dIT0aO2nIVjMt20UhOx7xDYNJNOqs6t1xGRbRoxB9f2Vv3aTAWCBbR2KHs_cpqqp_JriVG4pXWuU9iOdl1b2lsnhnkDbabfTYX82BoyyzAQiTTNkHGWMnfZhXam6GaXciQ0AGtA9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171f23100d.mp4?token=PqgBlhmUEZVWJ4Gf6rSxVQhKEJ5GKRWOYtN_42QV9VvNef1u2e4KUJHvQDxQZpbd6wYbGtlNN5TVOiHgT4Jy1yB26Y-PECtjfG673m-GSAMv4dMTLPtmcGjF0qqNIQ3DwS3r7QoyIdjsFDaQsDYYg6kGyu-EVc0d6gGhok660pZ-Y38wWtCMs2ZHJpuhSLFxxFoiWuG5MYFm3dIT0aO2nIVjMt20UhOx7xDYNJNOqs6t1xGRbRoxB9f2Vv3aTAWCBbR2KHs_cpqqp_JriVG4pXWuU9iOdl1b2lsnhnkDbabfTYX82BoyyzAQiTTNkHGWMnfZhXam6GaXciQ0AGtA9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: ماجرای قلب نشان دادن سخنگوی دولت به خبرنگاران چه بود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/687216" target="_blank">📅 20:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687215">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
شنیده شدن صدای چندین انفجار در اردن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/687215" target="_blank">📅 20:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687213">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/338f0b7bb5.mp4?token=TZCnhVy45A24vKQFjl2MA8LGhE5iOsb_Slt9lxipbmJQ9tU14MoTdskNyljYKk4H4nkPgnd2dizpVqJTUcYF5KOa7FU40pbFHUxRHQ7BVTE9QDoLcUrRUu3rj_0Vo3sRVz20E140w5sBQZ2_avUkckEp1gVwjzG2KBLs-iPI4IV9crkU7vhvOPjekjTiZ7KM_ZqkouNNcCYrYBDdkyetIsl7epWpIVPu8RJ6-Q27cfxyqdNofPq2laxg0dFNlF9J2lNMsrdvGQA76khotHZq8elLSatBXxa8nNSpoFC-TAI_TiSc-gCo8DZmIczgonW7zXpuiZK8ctIR0Ebne4gi7CVL5UFGE7PKfLmlDm0Qrn6hZ47Z3hkvHMwoHnMT0sYO23ihLiebhD3QR_Tlv7u_JuHsqTVFsjsBhGSlwLu5HbiSi29kRgAchSz-38QGEdrdVLzfn0XjOVQg4pUWfBLprj5kP6Cl2ALrB-gKYWJWl_iRoy_48VS4qjfsoJCywRnV-pLYR8jaJWlL31lOh0CYqUf7__rg64Etg3AgML0S5XSQudZkbFoP773dlhPRPTfseflcTC25CvxLBOxFcv3OnA6I8Bw9rMheoPC-Ipo8Pz5uVXuSlVjj8iO0m08OMksR7j8s4x5Q6825LugtIM_6XoNFFUcz6eWRWalRKZko3SI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/338f0b7bb5.mp4?token=TZCnhVy45A24vKQFjl2MA8LGhE5iOsb_Slt9lxipbmJQ9tU14MoTdskNyljYKk4H4nkPgnd2dizpVqJTUcYF5KOa7FU40pbFHUxRHQ7BVTE9QDoLcUrRUu3rj_0Vo3sRVz20E140w5sBQZ2_avUkckEp1gVwjzG2KBLs-iPI4IV9crkU7vhvOPjekjTiZ7KM_ZqkouNNcCYrYBDdkyetIsl7epWpIVPu8RJ6-Q27cfxyqdNofPq2laxg0dFNlF9J2lNMsrdvGQA76khotHZq8elLSatBXxa8nNSpoFC-TAI_TiSc-gCo8DZmIczgonW7zXpuiZK8ctIR0Ebne4gi7CVL5UFGE7PKfLmlDm0Qrn6hZ47Z3hkvHMwoHnMT0sYO23ihLiebhD3QR_Tlv7u_JuHsqTVFsjsBhGSlwLu5HbiSi29kRgAchSz-38QGEdrdVLzfn0XjOVQg4pUWfBLprj5kP6Cl2ALrB-gKYWJWl_iRoy_48VS4qjfsoJCywRnV-pLYR8jaJWlL31lOh0CYqUf7__rg64Etg3AgML0S5XSQudZkbFoP773dlhPRPTfseflcTC25CvxLBOxFcv3OnA6I8Bw9rMheoPC-Ipo8Pz5uVXuSlVjj8iO0m08OMksR7j8s4x5Q6825LugtIM_6XoNFFUcz6eWRWalRKZko3SI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از معنای پردازش تدریجی هیجانی در روانشناسی
🔹
ذهن مثل همان شن‌هاست، وقتی آسیب می‌بیند، نیاز به زمان و تکرار دارد تا خودش را دوباره شکل بدهد به شرطی که در جریان بمونه و رهاش نکند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/687213" target="_blank">📅 20:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687212">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/687212" target="_blank">📅 19:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687211">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gl7jQ1p6hJ6hTjoqsHqWtYN_-TOqH8rSu5fOyRByXoH80uTEISHfNIJGbscmC358KJWCeFxqrdOpNbHlHKPu9mRrnA-tOr94KRHQKVb3uJYeXngzMO-kNhmjopysp9p2y4i1oe7qgc9FpwHLXMcmNQBSW7pA_q8TAVqQMhmzKR51PZNtIRRgJ4NC_kenQs4n9j_xV_wh9ooR-U_5gN7XxmE_idEdF7HO_IgQym_rJ_T5nPlC3b6NSZuaPYUwt18ZP-e64IJzvVbV6hbqEWguuzrRr0-tttqrdhNNw5WiAUt9SKMulQJfgrxF1GUutfeI2na9y-pKzSQ1e3Q8P9Hstg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشاوره رایگان پزشکی برای متقاضیان کاهش وزن با آمپول‌های لاغری
🔹
با توجه به سیر صعودی مصرف خودسرانه آمپول های لاغری و با همکاری شرکت های دانش بنیان دوراپزشکی ، این امکان فراهم شده تا افرادی که قصد استفاده از آمپول های لاغری را دارند به صورت کاملا رایگان و آنلاین توسط پزشک ویزیت شوند.
🔹
کاربران در این سامانه با تکمیل فرم کوتاه ارزیابی، شرایط خود را از نظر BMI، سوابق بیماری و داروهای مصرفی بررسی کرده و سپس با مشاوره رایگان توسط پزشک از شرایط مصرف آمپول های لاغری با خبر می شوند.
👈
شروع ارزیابی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/687211" target="_blank">📅 19:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687206">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQuFqrwqSf2Jv8ygFjPe3zV4Rx-Vxa63Q1ODScWJYFzPuF1vhCrFL3faK9QvlQwxZbq9VaVp7pG6KyhkxWTdKWVqCStaRec7iedY-7nKBGXz-3XNR0sfo0sqaoFt-ew3qfb9s08azRN2OfjaJ9bYsZ6u1CmBQINWMvDqxIKpusqB-zmh_l65aPW4E0qTAiO6QAQ63NywTlKmMLq0sRrE6TDZgx38wrwNfMjmHyK1M2nsMSSp1Aj1kJlHUvvJ_NEMMgWMzf4wQSaiV0bLY4sEXyvHDgH7zOZyxS5raHtu47FRZ7EM6AamnbdR23KFdC1baMiYnxzvIleIYFcBwUTubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل سازمان منطقه آزاد ارس در مراسم افتتاحیه ارمنستان اکسپو عنوان کرد؛
ضرورت ایجاد «معماری نوین اقتصادی» با همسایگان/ منطقه آزاد ارس، دروازه ورود سرمایه‌گذاران به ایران
متن کامل خبر را در لینک زیر بخوانید
https://t.me/araspres/24095</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/687206" target="_blank">📅 19:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687204">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2356cf30c3.mp4?token=nXTcfij4UYmsjZEgRW6u2qDa2T8JBL8zHW8EObVAerFar8Yr_pEw7eFoCkhjmkahMVjqwRc1BU5pWVjAmS9vkLkydTB6SM-PoaEikujSMVsHJVIEt8ah_WXGoYPOddAg95f1eVsfJS7UePbtP4C2DpM3UYkABZvNeSRjltSltoGr8nFNRbDM7SxgT6o53xwqU8oCFEtmkfLwiC8iRD44i5woKkeioFgZlx0Hr8wFEDzx2Czwf3MvliclDN-DeDZLv1DlJ06kB7bNO91vPKTSa_kxZMY3l0pMDM9aaXb7rY_hQKTiG_-PYGAHA55v1F1Ur6ORZEqVCXm4RISM3tn0ZKizqEHEi15kvZNFnIOSHhV287yPde02use3O0ztocRJmAHtVrDeasH6QtPH9RL2fJuM_mUDQFQGvo0mw3If9czxgoRaoJKPN2bh1bUG2YkGGcv0DjlMXP5RrsNVRWtZqi1JoCgQX4CMR1DQwd6pHTQ4Nx3D2DsoEegaDVkLZpguUDFcH12EGDBTQLBWU1S7TpuSQr9588E-8QmPYsFqrdEuFY6zrfQTdD35R4GtHYNXoq1cLT8h6iy2TWkh7V-pjhVESOL2CZ8Naqu25X2V-4qd50H2sLM3k3Y6d6oYgQiJF5ywt6P7H8YpOPlxARDIkU_pJva0e00MzA1Hv6lFsBY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2356cf30c3.mp4?token=nXTcfij4UYmsjZEgRW6u2qDa2T8JBL8zHW8EObVAerFar8Yr_pEw7eFoCkhjmkahMVjqwRc1BU5pWVjAmS9vkLkydTB6SM-PoaEikujSMVsHJVIEt8ah_WXGoYPOddAg95f1eVsfJS7UePbtP4C2DpM3UYkABZvNeSRjltSltoGr8nFNRbDM7SxgT6o53xwqU8oCFEtmkfLwiC8iRD44i5woKkeioFgZlx0Hr8wFEDzx2Czwf3MvliclDN-DeDZLv1DlJ06kB7bNO91vPKTSa_kxZMY3l0pMDM9aaXb7rY_hQKTiG_-PYGAHA55v1F1Ur6ORZEqVCXm4RISM3tn0ZKizqEHEi15kvZNFnIOSHhV287yPde02use3O0ztocRJmAHtVrDeasH6QtPH9RL2fJuM_mUDQFQGvo0mw3If9czxgoRaoJKPN2bh1bUG2YkGGcv0DjlMXP5RrsNVRWtZqi1JoCgQX4CMR1DQwd6pHTQ4Nx3D2DsoEegaDVkLZpguUDFcH12EGDBTQLBWU1S7TpuSQr9588E-8QmPYsFqrdEuFY6zrfQTdD35R4GtHYNXoq1cLT8h6iy2TWkh7V-pjhVESOL2CZ8Naqu25X2V-4qd50H2sLM3k3Y6d6oYgQiJF5ywt6P7H8YpOPlxARDIkU_pJva0e00MzA1Hv6lFsBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک: ادعای اشغال کامل علی‌الطاهر از سوی رژیم صهیونیستی در حالی مطرح شده که این منطقه ماه‌ها زیر شدیدترین بمباران و محاصره قرار داشته است / مقاومت مدافعان علی‌الطاهر با وجود فشارهای سنگین، به یکی از نبردهای مهم این منطقه تبدیل شده و برای اعلام سرنوشت نهایی باید منتظر بیانیه مقاومت ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/687204" target="_blank">📅 19:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687193">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nS5CHskJ87i4VwtHWTQaJd6Y5j4fz8-oaAhISBB2Owgd8F61vxvTAolaFOvfa35tTaP49jmniblQMuWzJRsOAEAFHNRBTgURoTwPFdOGuAWPJ_TNBgkB2GrX_yw0NVDO0wfM_FT4p-IL7QAy93nepL34qWEWBgBfvm7KdFUQyuMNGyZZijRDsxS15lFM3Dfx9gX47x2Xh4YdV9eHIN8Uy2jxW6IOgjjbWswEhsa-6zNF7-yoeI7tlMa0UF_PP3hoE70_MKbQtthpAJUfTVUPzX7By-UYtwAlPRUazx-3s2o_7zQ0Ne-8AOUu3raHZeyQeXD67rgP0axvt7bSY6FQ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dW-QrFiV1USo56tY-i1jf2pKnXiE87beXfnxhQfu6DC6ixJ_vMopPSrK8pwA2NQuhgY2IXeP22kgFo16YS6kBEjaVytDz2KTPZGYjQ1W8MY3YqbTNxXhcH4nHjmsSkeQLwvEDz3j9hXOEYmOA9dH0pSipAoDWH00frXvZOYZP6syrJXU9YI-Up9Pu8f_9B6nncHeFeOaW6kqCMFP117J9OHxd7ppZaFo4nA4KiVr3IivU43O6YfQuGXZSblgBkmWhZpqrU9RdGKsH24AmgkaqzISddIoAyvhKS0_Q_VbT0JMWqhNZ2wFMXYJfixOkaGXEn7L-i4T-NbHm6tqnTECWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ywm6o-VUL2bQDh7PFuzGpHagdSVLdgTGbCBvq5yXiiPKULnBxdfEitbIxtjxgWzp1P9i74scFeEkRS7TJERxf7arkWHybbkcrLAkTY6LJiiNDz__aArWplo0rOZKCrpBQ5qLWo0u_2AahGV5Cz36hpfPbFe8YQQlSUmdOm1G5FCrkawQJ4LCSSqzBVF_5z0L4Uh5-2nIkiBzyPf6puZf-lSZPZznkRUkxqvyVIV5D4YrIFuKb8lPJeaqKE3SLvh2PhIVKLyutJWdPlStghIkeEv7vxq2SpTn6pwNuz0wYQURqpGgKMwkSPXGLRbMR5qnshQBeAJuALpkvf9q4ygxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A3pKeiAhJwybnklVQpUA9CzEM_ThPEhApL6YQNJmGci8_S9yHqGDsDN-DpoSN36drIKpmsvCWGjfUV169Je0BogETOGWx1sur-OEF4OKKKcC0PQUlj5FniPyXJBW_NazJuNoNmfJPj-zd1apOmxzT0Rv12HfH__OM6d95sdakwfCC08aLqzENPLQon4wfI5JVnnFCAeiy8-lHe-7MrDotx7CeTbD58vl7hpaTMVxdoIGNYSJlEGuhTqQdAHoM5D8jCx2HWuXky4yyQ3nMAp0H1NdupF7ql4aHPkp_xholiHesKmog3A-aMgmZ0J5yPibxaXnVnZ8THgqSxIjQVWgzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X5bzrmUkaTpr1wF5i7KnV74ao5LdZUnaF9ar1oJasEssOxrGKm2d-QAo9SJiD0srCHacmhAoLi3egRtSoPK5McDcShXpKveoWIpiJrew-Nkfc_CFCEzIhJpxzQKSdMIkVWMZRrNU-4XfrcJ5K0Urc58WNt45mybscwIkuX-JsxiJCwM3M377D2ffJgOSBhFB3K8MkiSWs72LKpHrbHwV6CbaCrZPYW0CKYAmFxnCVP9TVmA3wFZQGRRgRSnjGY6L-CyNMs-lO_3ykGNhxWZ5PMF1_KEit01hGkGrdPVN3p84ioJLHlOeTd97H5fUA85s0hqcuIoCNY31QGQbFNxqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/owUr5l1-K4irjYYniSQXixI_LOLTW8U8RDdrozBAfODK-WZIfGhTt4hDcC5G-rs7ezJa-4fn-10nXwWBeYnsXdOhz4k9h2vu-QED4w9SDGBYY4UdGHplmvbKjWQhNmsBVRQnRhwy_TlXnHgmqeDKHURUFG6igV1HCCzBSaJ6w2JekmolI2zofKc5nHtlrMdJYcmOgEnDudNucHhvcLi-0iubHm97KTXb02Xg4FxuJMvCwmFIy9MHr4hO7OscGDN9RG64DFTcRXVoeHwfI4cgwwL8n8-BpOPs8UhE4PqRaav7xQGgfvy2Rid-te_CT8vkYYeAuT6T9-IAUqZyyTCu0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KkFHqi0JO1Crae1Lc_wWmdyFWsOiw9Qspxv1VpIUmawZvfhwbQ6LWGxBdiy8MsgGfX7jX-82Qizz0lNauGfucfILKXI2h2xXvOAh3zQIAGL9UcF3rZK19lyy5gR5saJ9qTZou9XutbP9rAKoIaKA8ugTsFu3YOGNpCiq6_CClc0oHZX9VymVD_i6b9E--H-u-H1gB_7kTb0IzSsTaq6F3tWAtmthU8HG5geDRcv5GtkDMRsLIbMS5dKxbJCOdx-K5akXXPjc_oHf1LEfrCTxGt4HbuP1GGjCRQmpunTuP-vtvAELcn8ajNE99rNXoOvCL3h2p5-BH6z9syGmftxiiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kadp2cCsi-8ksM66BKcNfu4h_prNtenFuClFAU2mTFo9dB0DQNiEK8kXb0vBvYYSFqHcGryScIDaLFSKKnJn-Bthwk7l-RdAhGzVT1kQgkQVBqXIOZ7YZMmW3JNiZ52u7ncxJerSeEtlUSPqK0qdCkjFgFdp77EkEj6tF2Pz16RZC9T1Z3dF_Qll8qB_DMTXlcV1qg_Ikbw_oLUfQKXqHYafZlhVGgIACe3JOj7X8e7HzooJX0zc5MItJ8rPM4-3IEHlyBUMusVwmJZ_kfYdlQXBzUVrwMzEnqrgKSJ2pnNfchtF_HNHXbe5PwfxjVS2YTOYoTId8lH1PvNicMHaKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sAIXcZqOc6xgQiCslff_QMJ_jBNEqd4sGwpJY9jKniwIcnQQeybG8Qfe-3ccmdQw9vJ0fBL0SYSkLPJqmwTL01igOmg1qEu4-Vu35o3FNvUH9s30iDa8Yr6UeH-eBOprmoJ4zse4kwirpozAkL8aN8zbF6fIp98hQ_v_a4mT2boOD2TEaumGqYoDOsxx07zwRTj9oSWNiD9I7SJp6Y1J6RsGkau9dghyiOJg9SbytQSZ4Ys1t6PBRW_8bW2NIn_RdYFwLGxo1zohxGBViHG6lWUbPQ1qJIbow2rhZyev5PhsIZ7I5Ds2z1afPXo7ODgfk3FkqPxnkI51LCMs7JZFfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phDpgNrCZUtdU7zU33Po6O8U2BiVj_j5-aPbw9aMEtQSrEOsgyjtgwTe7PtYMNL_XaI9FMAwaOWng-tvqjfJWaLr67gg8MNwKx3YHwCq2_SqWfUn1Rhyr5qbVZGnxBSjoT3p5fnUThj3GqN8EeObhugPXe2OJGOLgumn0S2pvqGmnrCLwTaOnwcFmON6lKoTJ-qAMOmXT7XpjOXPJiDk83J0B-wniG-MHDWnIVRKVhyjAnTcsqeW-CTKa3JDWUtDVDvkM5hYOfBCuUfy1QhTSG-_kQT_q1dszdt-Ar9F537ka7bHQ_ElXkKoKLw4TDwD2OZE_hGRlT4NM6shfOuW0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
موانع و چالش‌های واقعی در تأمین داروهای ضروری
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/687193" target="_blank">📅 19:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687191">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fff2a5ffec.mp4?token=AEs9O8eMk30W_vwunLhLezy2aVOedo52VEFePxBMVtlld7BGR8oMa2ovHwOJTAYqJGEJBLl86qhZgvKg5sNCknLLwKHqqasWUQzj7-g3NeLvshUhXndXmTzgg95ZXhBcxC14zlkJQGjSFhT8wDu0O4CM1Pq8NZhnz_oWVPjYhvi3X_3Hx-z2hugXMhbLNCDYPVNtEbv5QGa0DYPJHdFqpVbtRGyDwzVo1_H5n7vDH3x4zFlUDeEL68PwwsxtHz8WMAnJR-gDG8bdl0GaV7E9CY5_yap__MmuCznhEZk9_Aj7XiQwxwXkUS_UDQiVJYhSQkBnI5lpsnF4fIWgJfAGSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fff2a5ffec.mp4?token=AEs9O8eMk30W_vwunLhLezy2aVOedo52VEFePxBMVtlld7BGR8oMa2ovHwOJTAYqJGEJBLl86qhZgvKg5sNCknLLwKHqqasWUQzj7-g3NeLvshUhXndXmTzgg95ZXhBcxC14zlkJQGjSFhT8wDu0O4CM1Pq8NZhnz_oWVPjYhvi3X_3Hx-z2hugXMhbLNCDYPVNtEbv5QGa0DYPJHdFqpVbtRGyDwzVo1_H5n7vDH3x4zFlUDeEL68PwwsxtHz8WMAnJR-gDG8bdl0GaV7E9CY5_yap__MmuCznhEZk9_Aj7XiQwxwXkUS_UDQiVJYhSQkBnI5lpsnF4fIWgJfAGSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای بسنت: نفت ۴۰ دلار خواهد شد!
🔹
در واقع فکر می‌کنم بعد از این، در بازار نفت با مازاد عرضه زیادی روبرو خواهیم شد. احتمالاً قیمت نفت خام را در محدوده ۴۰ تا ۵۰ دلار خواهیم دید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/687191" target="_blank">📅 18:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687190">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZp5ZPxipIK6hzrDGL2xLCIHElYf46zR72KO3Bm4VFOE5gC2oPXuiZLdXczFoaEw8wv0-S6_0oJsmZfXGblCj8B42HSF6ZC0o25lHEWurMx7gXt_1MKk2FfJDSRf04p-Tzm88m_4vppZBwjqUgDGBEqWyMWFQigzO-jWqCt6H5fOVCNaKMw1hGOGEUvr9CcGlX6L_Kz8HZHfGp7jlxDb5D2Hl_T6VJEmb0a8xsIqXNN8KTbAJQ63Q4syZav0G0lATigSd1wtBaSUf8S0dallheoc12ePSw0cFSiparGp1ausFqpiRZLCCYjwi1lHWUBrYzV81SuJiBILKqhyYqYx7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابعاد پنهان اثر استروئید روی مردان!
🔸
استروئیدهای بدنسازی فقط توده عضلانی را افزایش نمی‌دهند؛ این مواد بر سلامت قلب، تعادل هورمونی، باروری و سایر اندام‌های داخلی اثر بگذارند.
@amarfact</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/687190" target="_blank">📅 18:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687187">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
سودآوری شستا در سال گذشته بهتر از سال قبل شد/ خروج چندین شرکت از زیان‌دهی در دل جنگ و ناآرامی‌ها
محمدرضا سعیدی، مدیرعامل شستا در
#گفتگو
با خبرفوری:
🔹
با قاطعیت به سهامداران اعلام می‌کنم که سودآوری شستا نسبت به سال گذشته حتماً بهتر بوده است؛ تحت تأثیر خبرهای جعلی قرار نگیرید.
🔹
هلدینگ‌هایی مثل تیپیکو، تاپیکو، تاصیکو، سیمان و شستا هم کپیتال گین بالایی داشتند و هم سود خوبی؛ این نشان‌دهنده قوام سودآوری شستا است.
🔹
به زودی مجمع سالانه شستا برگزار می‌شود و نشان خواهیم داد که شستا در سال گذشته درخشیده است.
🔹
در سال گذشته چندین شرکت را از زیان‌دهی خارج کردیم، آن هم در زیر جنگ و ناآرامی‌ها.
گفتگوی کامل را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3242509</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/687187" target="_blank">📅 18:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687186">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eca538937e.mp4?token=duEcBfdE-SbKNOD-OK-Foewch4lWO_sPIRWOInXbI0IRKDwfi6UTZe9XWm-R97rVhEyeO8ifQ9RyTtDU_iJV-bsy0U68yZ9WnZVVf8UlzYNVF_6hAhu8_IVEpsmIPsNLAC67LtS5Btfq5EvnCX2cNPmalGgdY3zN1SIztOJUVQqjde1lPCWuRO8kLVa-NrmWqoHDW9yI93ZwF2JOn7KU9wkLMnkbnIR0bnvw0180w5yePuxG63Gz6-ZCgWRu_RjTWrcWjIN5VgEulMPkrYKLxZYuXVJ6wA6PjhqSIgKYm-qO5sc3AiMphHCiF-mxPDBB85v1go3zi_khOqZCrvxMDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eca538937e.mp4?token=duEcBfdE-SbKNOD-OK-Foewch4lWO_sPIRWOInXbI0IRKDwfi6UTZe9XWm-R97rVhEyeO8ifQ9RyTtDU_iJV-bsy0U68yZ9WnZVVf8UlzYNVF_6hAhu8_IVEpsmIPsNLAC67LtS5Btfq5EvnCX2cNPmalGgdY3zN1SIztOJUVQqjde1lPCWuRO8kLVa-NrmWqoHDW9yI93ZwF2JOn7KU9wkLMnkbnIR0bnvw0180w5yePuxG63Gz6-ZCgWRu_RjTWrcWjIN5VgEulMPkrYKLxZYuXVJ6wA6PjhqSIgKYm-qO5sc3AiMphHCiF-mxPDBB85v1go3zi_khOqZCrvxMDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش ترفند مخفی کردن بند کفش برای ظاهر شیک‌تر
👟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/687186" target="_blank">📅 18:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687185">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
آمریکا سه نهاد مالی را در ترکیه به فهرست تحریم‌های ضدایرانی اضافه کرد
🔹
دفتر کنترل دارایی‌های خزانه‌داری آمریکا نام سه نهاد فعال در زمینه مسائل مالی و بیمه را به فهرست تحریم‌ها علیه ایران اضافه کرده است.
🔹
این شرکت‌ها همه در ترکیه مستقر هستند./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/687185" target="_blank">📅 18:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687184">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/687184" target="_blank">📅 17:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687180">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/852c8954b8.mp4?token=rk-QPp7MUja4iANxxXWvKlBAupugDngHSpUSHrY6YeScy6c8o9ZzLnNyjrnBThs-_KoQNaoWcfqCWLbGdo5P1BiuebZuoORpsk7R_0do3iYjxvWE2by-PLdBL32ghYgJ_kWhUw-wY6Cy9iqT4jZkCLDdOnaz-p5rzQ_FkjQFoLzaxpIn7EDgoafvfMhAkfG8wNjbJNb9RXU1J7T_4rlsUD6RNAgKOl2nV5D68lTp3yl2-DupkSJ4oXzF-k5ReSzs3KbeYYtqdAMb-A247DB15CxZt56emwRtDzGULAJ2zZJE8InSgIFTGCN5JfMupO8gDvWrnElqqGdMdCzsRM2Uy4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/852c8954b8.mp4?token=rk-QPp7MUja4iANxxXWvKlBAupugDngHSpUSHrY6YeScy6c8o9ZzLnNyjrnBThs-_KoQNaoWcfqCWLbGdo5P1BiuebZuoORpsk7R_0do3iYjxvWE2by-PLdBL32ghYgJ_kWhUw-wY6Cy9iqT4jZkCLDdOnaz-p5rzQ_FkjQFoLzaxpIn7EDgoafvfMhAkfG8wNjbJNb9RXU1J7T_4rlsUD6RNAgKOl2nV5D68lTp3yl2-DupkSJ4oXzF-k5ReSzs3KbeYYtqdAMb-A247DB15CxZt56emwRtDzGULAJ2zZJE8InSgIFTGCN5JfMupO8gDvWrnElqqGdMdCzsRM2Uy4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین چگونه می‌تواند به ایران کمک کند؟
🔹
پکن در شرایط بحرانی که آمریکا جنگ اقتصادی را علیه ایران آغاز کرده، اهرم مهمی دارد که می‌تواند به ایران کمک کند.
🔹
جزئیات را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/687180" target="_blank">📅 17:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687177">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQmhFnAdu3rWGe7JRrTjaDA46hopVnRLsoph7thYrl2RFmMsgtBFzXzKP5e-jqPcoz3NsIZA9dBoCG4qRM7E2HKxsMCCqymHqlaeiKj8VxiLLQ8QjEP4DmIPcT3DyIw0l3fdIKVLX5j31-O0PG-idDJeW0-ALK-jZsRkm28Yvb9wkNJn9f3iVR_e1_wP4aMeb1QWgkIfvMOJ_4IiS9jwyNKul0nGIu0J7w3BJjYLsCIauK8FxQZriRgYruvSiXk5-dXwkA_N9rbBlH468m9OKrSYzEmASw9n124dxrE48uSQogKap3gM9okY7tbHvJGVqbjkyJPbyyv8nZP7Q_6R-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصطفی نجفی با اقتدار قهرمان جهان شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/687177" target="_blank">📅 17:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687176">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eed0161f0.mp4?token=AcyydE0DmmF6gggZVQGqjqoE__U-bU8lCyLtyKV8P9g6dMcq19tR0iQBIXMnQ2eT530iEHCWDku8E_VOnliZF7_1q0q4L7CV-GJ_2JqjrJIf4dHmOZh2s4eqxI_zt62Q9UqpUrOdfVYnfEzBIvZbh91WP_gTBAAYMTX54cg6fnHUaNQDo5FuEt9areNhI3zBM9scLparOLdCrlrj70F7J7wbsHWNnZK2MVAcqIRFh1lwJ0sVLdUAuwZvTDIlB0LMPePp2_ZicT_Uix7Amhx4Ra833nfiFxC6zqUdOrM663Pm2kWu0Nj4ekThaeKN-jaY9QwQvBmEAJtJLaqq9ydRKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eed0161f0.mp4?token=AcyydE0DmmF6gggZVQGqjqoE__U-bU8lCyLtyKV8P9g6dMcq19tR0iQBIXMnQ2eT530iEHCWDku8E_VOnliZF7_1q0q4L7CV-GJ_2JqjrJIf4dHmOZh2s4eqxI_zt62Q9UqpUrOdfVYnfEzBIvZbh91WP_gTBAAYMTX54cg6fnHUaNQDo5FuEt9areNhI3zBM9scLparOLdCrlrj70F7J7wbsHWNnZK2MVAcqIRFh1lwJ0sVLdUAuwZvTDIlB0LMPePp2_ZicT_Uix7Amhx4Ra833nfiFxC6zqUdOrM663Pm2kWu0Nj4ekThaeKN-jaY9QwQvBmEAJtJLaqq9ydRKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روس‌ها دفتر پوک‌لاد، رئیس سرویس امنیتی اوکراین را هدف قرار دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/687176" target="_blank">📅 17:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687175">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lI5zfJUdq4M3EyF4tWlaXYjqOYzfS2_VYePCI6YfCMXUuaGlQIbPNOYbguosr4RczAypWtCbjWYF1DxYUZBLntKxhtSdIZtZmNy3WIBzZYqud1-rfCLUFxl6RFciXexiQSEFWPhOA8c9IGrghSvcE2HJCDbG9-Tb39kFZWOytfM_gfGSadxNe8X0DcNQXvm1NVvEk44sWfDz84wcQ-XK__lskODcNLefiBpPahjVCvAH3joEBeY86yCXEAXup1peY7rCQPIZhQc48U9hxCXRhrlar0oBrQhj7g6YswfoHj-IjHAXOqjMr7sFVfCBNspsUCjinFWWZNa0jpp8b04OAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همزمان با کاهش قیمت طلا، ارزهای دیجیتال هم سقوط کردند!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/687175" target="_blank">📅 17:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687167">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/upxwYOojOjRii4-IWVLhdJbX318r1sZW2Z38ww_QI1bpK8CkA9Wy2jkyK0gKojLIlKGMnFzYlfbXhzKfKvT3s2Tz7c2FM0nIWyv1BXs43duF1QzmFAxkHIi3i1v8JsILN03AAioJRdQ-_Rhdh9kA2wmIWLFdCC_WMP80yXapDPepnsPW6bbLcCb20bKLtxeCd9wrjWuYA__e48U0HwkHRM4R_dPZ2KzhpPDCP0j7D4yA_UwkDzcN7sEaai0_uE6aPfeUdNrOHke9UkjHrprReBg4z1zZTleF0JTMJzjU64DlCLIeBQ3YgyhjNOgrZiU_Rvs4ljj88AysReUpGd1zVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ggu82DT4asbfaHQCVrBSmIB1039p6eYhyFQQ8nJpYvvFs8BSM4cjMaH5Xp0f1Hjayt_2cur8uNGqV2Fl0Wj-KIrRX9tt7lr61qJSnbAVi_EO4e0hnVNqSsEADlcZjm9YqQwdjzAZ3sNXoQmZBwmUgW-MuY7cOYuckUuimd2jIuPJYVBGhDftaSkoZ7X0PKVuQtW9X8PV6YSao3jN5YLDN6HlOl1G4zvQ3LFEc3SCkP9CZ5vl-TVDirs3PT1O9tl48jAD4OO0mIYrlRQHgknxdm362fWe5p9FzGlfetsQs8kI6eYIWvKxWIvGTvQW-k5OHkRG_461J8tCd5k_RUIanw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sRQQKe_ZETGpllwxkSOC5BiWNRDmquMf_S2kAJbACtlChDEqxQcRqr4G8wzHhd6rT2X_HgKbPLIC9tCoVR6RMuxtrbHqru7R8qMyjOHXyvVpMv8qOXdLFjyClywvjgvf_qjVn7urjeZR0Ka9q4mZOegvXHz8bTRZmdnb2PuEoZ4_F-d2fCmujedXTZ-RNooFfIDCXLIwlhDt-T32CdXuYEjjLqXkQ1EOpUe91eYpT8F5JfNHxdsB_chCyazHUjnP4hskGZLzliW0W-dLNgyUqt4sTt3LCj6mnxf1N5IaGG_Xpt7NWMJTuSn2m3JL_XO5m-GSIIXI461b7dzRpCCXDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCEQXghkXMGlvzqvLG0UaKJAj_cQEH_vrFNSo1nT-DOCYDpXv5r17m16yGZRNC89gkrj8xye_9uAImhYCXtWsLA2ANwad_upW-e8F0edoY9SqRozIsNb9USq5hB-e43MfVAWK87MBU_aKVyRHDpGdGNwEIHmB7eWJc_bOvlCffBNncualjF4cXWEPtVuU6nxNWQt0Tgv6eaR9zVF9HToAAr9Iyh2WLwTsP-IIpM_UlnpY2_eEyujToxlOrZLE3uT8fU3hErNuVkgqF9OYFpP6VuqPZ0L4mn0BgXdIW2NNkjLAECxDD2mcdzgFhuVx7fOx-Rf1zH1Z1KLa3CTtV9IJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKxannc4K-zz_cLYO23_LXwczFzhH7pXiUhm_qJRjNCFjTlvCU17HLZFtWBN4A6HlPINxYjfg1RqdcfW3GopJi0ndJmxQjDioNEn6gsHdOLTQA1C45sMmmL4pyPEuxlGGQSCY46RZDaLeP9p2X9utDSZ-Ji_izZqRKdg2DnSGjuZz629c5KQ19xwNU6aX6mHSJ680I7dtd2NjvOF2bNPd5Qov_iKs4_XFw5tfyew4NYVVuBnw1VvkjzAxr_4JthvCKH4JvMQdjsT6PfVASA0nmpNBRTJk-ZuKgSpY-DlTMIbLAMdn1zucTqc9cR_5nCyuTv26F28fBHQQazizIPmqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cji9C0Rc-rT2c8fZLMNO-iAjEqie_zsj2Y3c1cKUqcB5pyb_GlT5o645NuTOm0kzmSwwsBdAVNbbqhE8Wg7G7Guc-ANiY1dTMBZyhqfMc7grzD-MTyI22wQ5dmu5FvgUOO8M9TTpnPVm5OA6isWEwJ65iSrPTZBRYw8Gy09vJf5IRy6Z7WLYT7JarDo9tm0pPHFQIX6d2OpuJU3CN0vRBFRPiKVjW44z1UgX2dKwKZeVgoKwGVkECYzSjh35kVMnfG4PUYdXC7Urzn0gr9nERLAsAKmp1BfBfwO5E78v7MdR0VruGPPtKj-_E3ge2CHE1iNK7Kcrqy7WO5a-6B9PyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzK1RXTJ5lX0MIJDITh2H5f5poFbeZDZ4pLXPpvjOF2nJMx9AppWKoA-k5SVVDYOHzJNlrTKzyuMODMZVgXWpx9_cfc3Mnzdwz1gTX5rBoJ2gccB1SAqbNyB5vwjMuqfZJb7AMjXXlIrs_BPByMuVXmB-0nUivJyUcum85aEUmGuRu3JrjqtnM_9D1H5ewDl0bg5cKR0Kz8-c5JNBsJQwy1xqbn7olAICCjEcrCKu9eDV2bPiGKG2xmgYvJ7anay1L_XWIv8yw8RveTHs9B0yGQ0y6ECxuYjpkLHBn911DpLpzcxXbG8fUqlYL9ZZmuqtFoK8CKCGnfxGuOhN7_qag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cvgg-huPpkUiYkJZDeoCpCcbUHsxIHXu9Q8Fe2AwZmzBy5sjmRl9GxSijWleCi-gUX9qAh11WmV6vJn8X1ISuocTtR39Yu7AyVTAENMvpsFzDpSOHubAjRj5bTjBn4GZrrPvPc0XXlGtpV3D187xuP5HgQR041FUkijYxq_ccf72LIdiGMIzjzYngzSLbyddMsXTnU8j6sEGhFkj35X9_WHv6eqVX0cq0pEufMhYYfvjOGSpBmOrjQ6oim92KC857N8jIQ7FSw4-joHuGmDkq527BqAv78jEfOWtR8t3OXgoYBpPsTvufl9Z1kMEXg7m54HThI_7MTtwyrBNFv1VQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت اثرِ یک همراهی
💫
✨
هر همراهی، وقتی به نیت خیر گره می‌خورد، می‌تواند اثری ماندگار بر جای بگذارد.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های حائز صلاحیت، این اثر را ماندگار می‌کند.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/687167" target="_blank">📅 17:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687166">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO5ybWng5eJuEUPpkKFncJO-1mqUpOSyiiMuTbMXCUZ01U9XbCsIAMGVFy4KEtjiig9oCOhvsKCr_apog4BjCsyU3Bx8uAp5mmJvcvIShO88BoCa6UY4aW78lTeaCmu1-pVJ2oquWHymFuo7f3lHx2eeHbw8gV1s1sYt4Y01DY7_wcHC-gUQhaD2x9dXGvNkZm9yhT3hw6324afuAKwG3V0i1yqsPdJ-aP9tSuiWq0Okt-Ok_J94q_LvbXHGpAio6dkMci-jLoV16uxIHcAzV-UN2c-AkBJxURaj74rFzD-Q0P_BU2iPlz7LRKXPkypkwTYWpdfcaiYfp1h1U5CosA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش وزیر امور خارجه کشورمان به اظهارات اخیر همتای اردنی؛ ایران برای پاسخ به متجاوز چقدر باید منتظر باشد؟!
🔹
به نظر وزیر امور خارجه اردن ایران چه مدت باید منتظر بماند تا به متجاوزی که نه به حاکمیت کشورهای عربی احترام می‌گذارد و نه به حاکمیت ایران پاسخ دهد؟…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/687166" target="_blank">📅 17:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687165">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3GLjugEqLRPsq65aDZdrTMBnUIz6p4Gu3tanTtgGJmfyZPdwKK7LB6TwKIwC0LW5M4n6mR8TROazZgVGRLQfhLgQ0yVGQlzroDcuoIfWBfaX3SJYt6tzCgjkkyoGznA3Fs5peSKUWuvsTuRIKqvIeSMPm5gCPh8gTk_UvYGc6VLRh-9ez1iivhsS3MZ0U5CWDrIgJKKda4ZLzYRnsxnE-fwQusoajcw_biLWzws5I6IjTrapeGwyp2ksO8D7huaDnXuwS6sOvYGBPcKpAhPXMnqF2fgAHQTO5SJpZps1uh8ceFDi3Wns0pYh0lw_o2WWEOp_ahosDhCGE_jJA_k9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۶۰ ثانیه چه اتفاقی در اینترنت می‌افتد؟
🔸
تنها در یک دقیقه، حجم عظیمی از داده در دنیای وب جابه‌جا می‌شود؛ از ارسال ۲۰۴ میلیون ایمیل و انجام ۲ میلیون جست‌وجو در گوگل گرفته تا بارگذاری ۷۲ ساعت ویدئو در یوتیوب.
🔸
در هر ۶۰ ثانیه، ۴۱ هزار پست در ثانیه در فیس‌بوک و ۱۰۴ هزار عکس در اسنپ‌چت به اشتراک گذاشته می‌شود که تنها بخشی از فعالیت لحظه‌ای کاربران در شبکه جهانی است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/687165" target="_blank">📅 16:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687164">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyNKwpsGvTwfWpc22YYZTBbjI9LtjEmgtPRBaWltOMj1E01UEBGI6WMk8WjkVp2JItF-bYHcFQERpxhIbSMkU02t452D3XdYi-T3apJYdyX9H6AvS-6KSOxgRl5F8QAXR4l128WlL4TTfv41koqJdU3lrQxpGgMkbpWntdMbMlpqzqhgKKZphm9Ax3TQYQ-oGYco3EOlqoSiuSismP8IPZE1_kwrXwTcIfOm_-PKDkw0SfL0ilw7WDONoGDGt-fPsb2hnZ6f130ZPwiI9hu23iNCpViXEmWG5e5l-abaoCJ-kzLJrrymhMV_c30qR05ES_u3FDiIlt1U071XI4JdnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره ادعای آمریکا را زیر سوال برد/ تردد کشتی‌ها در تنگه هرمز زیاد نشده است
الجزیره:
🔹
آخرین داده‌های ردیابی کشتی‌ها تصویری متفاوت از ادعاهای امریکا را نشان می‌دهد و تعداد بسیار کمتری کشتی در حال عبور از تنگه ثبت شده‌اند.
🔹
طبق گزارش شرکت تحلیل دریایی کپلر، تنها شش کشتی در روز چهارشنبه، ۱۱ کشتی در روز سه‌شنبه و پنج کشتی در روز دوشنبه از تنگه عبور کردند. این شرکت میانگین ۱۰ روزه را ۱۳ کشتی در روز اعلام کرد.
🔹
سایر سرویس‌های قاچاق کشتی نیز الگوی مشابهی را نشان می‌دهند.
🔹
شرکت داده‌های دریایی لویدز لیست اینتلیجنس، از ۲۶ آگوست تا ۱ سپتامبر به طور متوسط ​​حدود ۱۲ عبور در روز را ثبت کرده است.
🔹
اگرچه بریجت دیاکون، مدیر اطلاعات و تحقیقات دریایی این شرکت، گفت که آخرین داده‌ها ممکن است «به دلیل تأخیر در شناسایی عبورهای تاریک» ناقص باشند.
🔹
این بدان معناست که برخی از کشتی‌ها چراغ‌های ردیابی خود را خاموش می‌کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/687164" target="_blank">📅 16:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687163">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دیدار و ادای احترام وزیر ارتباطات به استاد خود پس از ۳۰ سال در اصفهان
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/687163" target="_blank">📅 16:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687162">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-9b2gsXrYKntHQ7jObtughy4sxm3ddb1EHhE2k55AvwL85V-mWYEcgJpaXSjFDeFwY8NogfEtxzhsSG2pA7JgsSvKrhhUQC2IkuFFqAPzxWit_9Ut6JxIDX0YrprFHq3EGm0A39rWTW9xiCXfdeEhk71OtTgDzX7xzc_Flg5V3i6tBP-JF8mAILqBskDkM-R4C47Z5FXcSpKHONMyQZsTwsfSezc7OXJTmsJZju-EBfyDI02QbJThFic09dNC-SFzvTvO3Qr1Hex7jSe4fVV1o_0rD9-pnI1AGoCc-NJEwuB85AlaTOxTqXTDTfmk8BI9lONXS5ptAB-2UcRBTzOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نیم‌رخ» از امروز در زی‌ویژن
سریال معمایی «نیم‌رخ» به تهیه‌کنندگی علی طلوعی و کارگردانی رضا شریفی، از امروز جمعه ۱۳ شهریور، به‌صورت اختصاصی در پلتفرم زی‌ویژن منتشر می‌شود.
مهدی سلطانی، حامد کمیلی، بهاره کیان‌افشار، سیاوش خیرابی، شیدا یوسفی، مهرداد نیکنام، شهروز دل‌افکار، مهرنوش مسعودیان، مهدی رکنی، پونه عاشورپور، افشین سنگ چاپ، لیلا بوشهری، رضا کریمی، بهزاد خرازی، یوسف مرادیان و محمد شیری بازیگران این مجموعه هستند. سریالی که روایت آن بر پایه رازها و رخدادهایی شکل گرفته که به‌تدریج برای مخاطب آشکار می‌شوند.
زی‌ویژن، پلتفرم نمایش خانگی نبراس پیکچرز، با انتشار «نیم‌رخ» نخستین سریال اختصاصی خود را عرضه می‌کند. نبراس پیکچرز پیش از این تولید آثاری همچون «شغال»، «جادوگر»، «ملکه گدایان» و «مانکن» را در کارنامه داشته است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/687162" target="_blank">📅 16:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687160">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d056894.mp4?token=LfBk4W6AKogc708DwM4TXNuI-jj_t2aHZkAwcN4J28YdiB4ILorzToorb94ISu_NFXtibPYkX3HTNPbo4UFXESCB7VM8bJ0r6OEVhGGFA8z3P6qmT3XaZ2R-BP_bEgLAt79W3GW85vYgdMuMJX57jZxDc3Ar6llhEpSc5gGfl2L-vCDKe9jyoddtU2ZjKZR7ZlZw7By06BUwsZvSxP7av7YT9MAysOQCCV9MsLDVQyivqMls01Is5vGtY7hC-2dpMfM7oRzB9pENM-dfGeJG8EPgHCHyVZBLyQY0FRpJJqnEL-MRESgEzLchFYr1sTa2HsHp3G-KAsbXwdHERtNy7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d056894.mp4?token=LfBk4W6AKogc708DwM4TXNuI-jj_t2aHZkAwcN4J28YdiB4ILorzToorb94ISu_NFXtibPYkX3HTNPbo4UFXESCB7VM8bJ0r6OEVhGGFA8z3P6qmT3XaZ2R-BP_bEgLAt79W3GW85vYgdMuMJX57jZxDc3Ar6llhEpSc5gGfl2L-vCDKe9jyoddtU2ZjKZR7ZlZw7By06BUwsZvSxP7av7YT9MAysOQCCV9MsLDVQyivqMls01Is5vGtY7hC-2dpMfM7oRzB9pENM-dfGeJG8EPgHCHyVZBLyQY0FRpJJqnEL-MRESgEzLchFYr1sTa2HsHp3G-KAsbXwdHERtNy7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه میخوای بدونی پنکه سقفی چجوری کار میکنه این ویدیو رو ببین
#موشکافی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/687160" target="_blank">📅 16:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687159">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWCz4Ju_w2zLTDTqcMetitWaXzIZzloL2jEBokkoFxgKoLwQQy005D7Srj_IC2d8fRpQRj52lAaer4_SfTLt9CAZDojJhWHdlEEB5JETOIEiHge1Gaagt4672wQl6lPXBYcvf-NJ4YxrEtYiSbkHOUA_KVg3o_jol6awhyWiOn2JUgOi6bPMNvTORZ9XJi50AwpZOt3guVdyA5rCVO68Qbx6GiwMYgf1vt7NRvWlmTkkOVCrGOjL74GqETEXktQrh747XZS_8Kb2xyv5hJvjiwH2EGoHhol8E90blM6g2OHWGFLUfaBaCxLJwK3lh0oQAPT5L1iaIFcUfSGerYalXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همزمان با کاهش قیمت طلا، ارزهای دیجیتال هم سقوط کردند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/687159" target="_blank">📅 16:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687158">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
برنامه‌ریزی شستا برای سه وضعیت جنگ، نه جنگ‌نه‌صلح و صلح/ ستاره خلیج‌فارس در مسیر IPO
محمرضا سعیدی، مدیرعامل شستا در
#گفتگو
با خبرفوری:
🔹
شستا برای هر سه وضعیت (جنگ، نه جنگ و نه صلح، و صلح) برنامه‌ریزی دارد و امیدواریم توافق‌ها به نتیجه برسد.
🔹
امیدوارم توافق شود چرا که در سایه آرامش و توافق، کارآفرینی شستا در داخل و ورود به مرزهای بین‌المللی شتاب می‌گیرد.
🔹
سیاست حرکت از بنگاه‌داری به سمت سرمایه‌گذاری، رویکرد اصلی شستا است.
🔹
ستاره خلیج‌فارس در برنامه آی‌پی‌او (IPO) قرار دارد؛ ورود این شرکت به بازار سرمایه، لنگرگاه محکمی برای بازار سرمایه کشور خواهد بود.
گفتگوی کامل را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3242509</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/687158" target="_blank">📅 16:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687157">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
سخنگوی ارتش: پاسخ به تجاوز احتمالی اسرائیل سریع‌تر و کوبنده‌تر خواهد بود
🔹
از بین رفتن سامانه‌های پدافند هوایی دشمن در جنگ ۴۰ روزه به‌معنای بازشدن مسیر حرکت موشک‌ها و پهپادهای ما به‌سمت سرزمین‌های اشغالی است.
🔹
اگر رژیم صهیونیستی دست به حمایت یا تجاوزی بزند، حتماً راحت‌تر، سریع‌تر و کوبنده‌تر از گذشته مورد هدف قرار خواهد گرفت و آثار بسیار مخرب و زیان‌باری را متحمل خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/687157" target="_blank">📅 16:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687156">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1caa70bc30.mp4?token=oaXPlzu0kaWD4o-mzEu6imtMYthrHOISqGSedgv5BNWWyOG29YRhOMA1d6-m5_99s60IOO68ijohsSnyCaOhdjh2aJEbeaS8uvyW7y--RCw-1TiwmPANEdQw8HvS7qlFbuedBGCYu-oZsF42CHtfqUTcfj4EIx53dKQT-lFvmZynJ8nvurnWSaJVAIdVn_Fc7JrY9zaH9LTJuqqfXgQCrCs8MoESVnwjRhez1UivtTPZYEfZnKiG4SF4eATH25dNFEth6tPHqbJGfhhSKTVnoog1dVcR9b2-FyoVMH49302jh-szxzAUJzgSrcNyzb90nIzghHaayIGN9rqZN8fESw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1caa70bc30.mp4?token=oaXPlzu0kaWD4o-mzEu6imtMYthrHOISqGSedgv5BNWWyOG29YRhOMA1d6-m5_99s60IOO68ijohsSnyCaOhdjh2aJEbeaS8uvyW7y--RCw-1TiwmPANEdQw8HvS7qlFbuedBGCYu-oZsF42CHtfqUTcfj4EIx53dKQT-lFvmZynJ8nvurnWSaJVAIdVn_Fc7JrY9zaH9LTJuqqfXgQCrCs8MoESVnwjRhez1UivtTPZYEfZnKiG4SF4eATH25dNFEth6tPHqbJGfhhSKTVnoog1dVcR9b2-FyoVMH49302jh-szxzAUJzgSrcNyzb90nIzghHaayIGN9rqZN8fESw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاوی تصاویر دلخراش| ویدیویی وحشتناک از یک تصادف
!
🔹
هنگام عبور از حاشیه خیابان بسیار دقت کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/687156" target="_blank">📅 16:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687155">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soQOHSB7rLJBkVUml_yqqnXIrzkoBUE_e5gle9LF6xJ6d51FMpA7R6-4HFvMSaZU15Y3qfZtmz7zfj9Va3zZGYr0J888IENkojfd68Fyp9U1Rxcsb6xH91TzsWSg4EtcwSo-rQBsf82BjlSDDcHPxNnRWbdmQQP0ipypNpGJYy5ZEIDBPiaTRpdApe9JRe3hSALm3wTn1t2JYXDTry1qC_XW5qWgP9JZkfbKBAkkPMy2mTnRHLNztPMg3nXsUA6yR3WpoEdxECceyI-KAw9YyfERX3eJDMOpJUyAA9RNsjcc65ED8RXAVXvLRtdsBeVDUzoxeE6cpeSm-JfKwLSNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
سایت گیزمودو تصویری از آیفون ۱۸ منتشر کرده که از وجود احتمالی دکمه جدیدی روی این گوشی خبر می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/687155" target="_blank">📅 16:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687154">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
سازمان اداری و استخدامی: ساعت کاری جدید ادارات شنبه ۱۴ شهریور اعلام می‌شود و بانک‌ها نیز از یکشنبه ۱۵ شهریور مطابق دستورالعمل‌های جدید فعالیت خواهند کرد
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/687154" target="_blank">📅 16:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687153">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501dc301d9.mp4?token=M5XKBpxcoaOgsZnFA5A1upTyJQ3suQkhF3uEuJcjgQifubHYaNHAlXqn5ACPKBfnVM0NFdAlDDSD50-UP2vUfTRVzHVLEqirauUurSWYWQFFazH4Tov300IgtGsk5ReTUPjvWay8piYI84jFbb67Ue4nYHhq_eA0iQ-2CaMpA3pWyPGRknowveQLUX51yu46ZulToQ2bdVOD1Xp71VhMy70vL7f3bFXzSzV64rr_2d021umtGcPX7zjk4T_qwmeO43VxDim1K9zaokwPkd4YHBR7WLLf9PkA8Z0Luwq3a7awNG-bR8jntF9iib2ncOwq0s_uu-w_Zrj7krAg06Vy0IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501dc301d9.mp4?token=M5XKBpxcoaOgsZnFA5A1upTyJQ3suQkhF3uEuJcjgQifubHYaNHAlXqn5ACPKBfnVM0NFdAlDDSD50-UP2vUfTRVzHVLEqirauUurSWYWQFFazH4Tov300IgtGsk5ReTUPjvWay8piYI84jFbb67Ue4nYHhq_eA0iQ-2CaMpA3pWyPGRknowveQLUX51yu46ZulToQ2bdVOD1Xp71VhMy70vL7f3bFXzSzV64rr_2d021umtGcPX7zjk4T_qwmeO43VxDim1K9zaokwPkd4YHBR7WLLf9PkA8Z0Luwq3a7awNG-bR8jntF9iib2ncOwq0s_uu-w_Zrj7krAg06Vy0IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شورای عالی امنیت ملی تصمیم گیرنده درباره آغاز و پایان تعطیلی جلسات در صحن مجلس است/ هیچ کدام از نمایندگان از شهادت نمی‌ترسند
سمیه رفیعی، عضو هیئت رییسه مجلس در
#گفتگو
با خبرفوری:
🔹
مجلس تعطیل نیست بلکه فضای فیزیکی آن بر توصیه و مکاتبه شورای عالی امنیت ملی، جلسات در آن محل برگزار نمی‌شود. پایان این ماجرا نیز باید با توصیه شورای عالی امنیت ملی باشد.
🔹
هیچکدام از نماینده‌ها از وضعیت مجلس به این شکل راضی نیستند. نکته در این است که هیچ قوه‌ای نقش جمهوریت مجلس را ندارد و جایگزین کردن آن هم راحت نیست وگرنه کسی از شهادت نمی‌ترسد. امیدوارم شروع برگزاری جلسات مجلس در همان صحن باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/687153" target="_blank">📅 16:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687152">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1daecf089c.mp4?token=G1EBO0aNQ6H2I2TQXZF4I9wFn6LTjldNLthO1C1eouHZuTNc6-88Zcp9voiQxhzALalJ4UoIgH0mwO2yDc6CtLchIcj_DxvXfFHqotIYzMtHqHqrkkgHBg0cAxMeOcDfG8v3i1AoWkBBR_48UZiKTlxfN1tohovnk58XRT5g5UHuO1TgjvvinGZNv4Oe3G-hpU8NQXhF2NBhvalYNGqYaH7eoAaH0NsINJy36WIOoTVdvrjTahzDbQYd4h_HAF-b5zPLtSLYKA_K7deERpgWuhwCdZkbGckiIuYUStZsfiLkPOzJGs98ZWSjNaEDH01GUZPYmnxs7z5wIRcah-izcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1daecf089c.mp4?token=G1EBO0aNQ6H2I2TQXZF4I9wFn6LTjldNLthO1C1eouHZuTNc6-88Zcp9voiQxhzALalJ4UoIgH0mwO2yDc6CtLchIcj_DxvXfFHqotIYzMtHqHqrkkgHBg0cAxMeOcDfG8v3i1AoWkBBR_48UZiKTlxfN1tohovnk58XRT5g5UHuO1TgjvvinGZNv4Oe3G-hpU8NQXhF2NBhvalYNGqYaH7eoAaH0NsINJy36WIOoTVdvrjTahzDbQYd4h_HAF-b5zPLtSLYKA_K7deERpgWuhwCdZkbGckiIuYUStZsfiLkPOzJGs98ZWSjNaEDH01GUZPYmnxs7z5wIRcah-izcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عرب نیوز: حمله پهیادی دقیق ایران به یک واحد در آخرین طبقه یک برج در کویت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/687152" target="_blank">📅 15:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687150">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
هشدار سازمان غذا و دارو درباره ۱۳ محصول غیرمجاز
🔹
سازمان غذا و دارو اسامی ۱۳ محصول بهداشتی و مصرفی فاقد مجوز را اعلام کرد.
🔹
این محصولات شامل کرم حجم‌دهنده باسن و سینه AICHUN BEAUTY، کرم ترک پا زرین الماس، پماد ترک پا، بادی‌میست GALAXY، ادوتوالت TEA ROSE، ادوپرفیوم DELGADO، مایع سفیدکننده فرنود، ریکا سیاه، شیشه‌شور الماس دریا، پاک‌کننده NANO TAK، نمک ماشین ظرفشویی FINISH و پودر زغال فعال هستند.
🔹
سازمان غذا و دارو با هشدار درباره خطرات احتمالی مصرف فرآورده‌های فاقد مجوز، از شهروندان خواست از خرید آن‌ها خودداری و موارد عرضه را گزارش کنند./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/687150" target="_blank">📅 15:41 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
