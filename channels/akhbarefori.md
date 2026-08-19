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
<p>@akhbarefori • 👥 4.07M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 02:44:33</div>
<hr>

<div class="tg-post" id="msg-682713">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LajcW-5vxOyBJYKg5Eeb0z_oI20LXcWh0ezeJ5d8-XBItfUz31ZzqhoXR1o8FD6A9K7Lo2tBGMzGX3H5HCoLW5z-tXv-_1ziW_OnC8Tzwud4HCBrTGhFuyTUlihcrG27d7GWnYm9WePluHnVdRfjBqPLADTLCTmh9At_ZRmt9aIEGWTSDk7c32TnmvyE5lcc3BDo959ogHfN0bTg849VMx7XRCKQbogUFbm7CVEhuE17LquSAJeOo1_rPBhy0R69Cpglczk87AKgL-WG0dDklHCMegVSBeITb7Ng6ADV5YVX0ONDVS3Tb8Yg_XrNeUeUcWa2uvrv3ekuBgOUB-tEvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد
🔹
رئیس جمهور تروریست آمریکا بامداد پنجشنبه ادعا کرد که «خردکننده‌ترین عملیات اقتصادی» در تاریخ را علیه جمهوری اسلامی ایران آغاز کرده است.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/akhbarefori/682713" target="_blank">📅 02:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682712">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGt3boY6E-99u8IqDbt4lRNOCXBUY4yN-AXv-PkTK_UkMOqDSnI6k5AJpMrK4qqxMSkgeAduIqDnOaYv81oKYmNHZMj4m6t3V9FqnujB_5ycZF3N7g4ANWBL1wrGj8uZoQFMreJdoBsiMRraMUT2YSaqQR9R0O8J8TZ5ldoXNv4rLlXQ_jJGQXSr1Mrgs4UkhbW1l3zhh6DDa2MYKPcqf9cV19ZhHCVlgaVJsetC0xJPD48h_tvGALT_bcrNEjKvvuvd41s5S5aGOaIwtA9g2hI_8t6zzzJ4Z0_GblJigMsTtPiY1QyYw8iWX03V90WNE16oN7OnawoA_md3G_ybzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز توی سوپرمارکت دیجی‌کالا آتیش‌بازی تخفیف به راهه!
🔥
➗
کد تخفیف ۵۰۰ هزار تومانی
➕
تا
۹۹٪ تخفیف
روی کالاهای شگفت‌انگیز
🚚
با
ارسال رایگان
و زیر
۴۵ دقیقه‌
🔥
هرچی برای خونه‌ات میخوایی از  کالاهای
سوپرمارکتی و نان تا پروتئین و میوه
، با تخفیف ویژه موجوده!
🛒
کد تخفیف ۵۰۰ هزارتومانی ویژه کاربر جدید:
DET555
⏰
فقط امروز
⏰
بزن بریم خرید از سوپرمارکت دیجی‌کالا
👇
dgka.me/ATTISHBAZI
dgka.me/ATTISHBAZI</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/akhbarefori/682712" target="_blank">📅 01:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682711">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
رئیس الحشد الشعبی: ایران در برابر یک جنگ شبه‌جهانی ایستادگی کرد
فالح الفیاض:
🔹
جمهوری اسلامی در معرض یک جنگ شبه‌جهانی قرار گرفت و توانست در برابر چالش‌ها ایستادگی کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/682711" target="_blank">📅 01:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682710">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c1ae5df3.mp4?token=bc0pvqDFIWO9_gysrqHpBiV633rtjo2CQO9yaXp1kBYS2MvaSAFMuJbCUrMe3gf3ynEF3sECVj6LS6j0sTPim7zwTy-da-wWl9eGaSS8sNdGzhDlQ7YNPyPrzMoKjDyfyzNwx06iXtvnZOzcYNGpKmWb6T6EjDupubTvzMJMrXLsRpOUkEx-jFB4gw0YY2rk8vi4EUp4hLoaIqECry1fiVjc1_c5xtwHhTxlkw-ujGQKj34ZxCzWR2DH3C-i22Mid_aOpWRs-cT97koirvLSM6fJBfFhWsC0ccCNAR6JZ_2mBeH9r_9eDwkWG82OUyv_j0Hjlw894VFkRuKOWXLT1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c1ae5df3.mp4?token=bc0pvqDFIWO9_gysrqHpBiV633rtjo2CQO9yaXp1kBYS2MvaSAFMuJbCUrMe3gf3ynEF3sECVj6LS6j0sTPim7zwTy-da-wWl9eGaSS8sNdGzhDlQ7YNPyPrzMoKjDyfyzNwx06iXtvnZOzcYNGpKmWb6T6EjDupubTvzMJMrXLsRpOUkEx-jFB4gw0YY2rk8vi4EUp4hLoaIqECry1fiVjc1_c5xtwHhTxlkw-ujGQKj34ZxCzWR2DH3C-i22Mid_aOpWRs-cT97koirvLSM6fJBfFhWsC0ccCNAR6JZ_2mBeH9r_9eDwkWG82OUyv_j0Hjlw894VFkRuKOWXLT1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجارهایی پایتخت اوکراین، کی‌یف، را به لرزه درآورد و مقامات می‌گویند پایتخت هدف حمله موشکی قرار دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/682710" target="_blank">📅 01:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682709">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
انفجارهایی پایتخت اوکراین، کی‌یف، را به لرزه درآورد و مقامات می‌گویند پایتخت هدف حمله موشکی قرار دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/682709" target="_blank">📅 00:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682708">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iL5dZiPA_fsoopmMPNNDmTrX8Lh3x4U47vQh6LCAtc-4K0YjUEvJYxZzbfI_QEowJqw-zu3zDpe9e2eptB3cf3MbNUmCA5NuJUTFODJZsm_cxmKhfMPwv72wiCdhlg4zZGwkNbS4HM7ZUhqf8x8zMM8k0PrjWl838vl2JMSXDt1z5iIrcQ17US1SVuMSR5_ejMVhOakprOamoafoReea9keDy09Zy31j4OpsW0smQxjSqjQH2dWsGlzlnZAjXhdW5nhS-ZY1DYK23glmG3GAJ4iNgxcrTwE1lCoO8-Ga5w3QVpXEd4dhKaCW6tXIqWEvCyoV0g08Wtt0mcVlzYEsww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکایی‌ها واشنگتن را پیروز جنگ می‌دانند یا تهران را؟
🔹
آخرین نظرسنجی اکونومیست/یوگاو نشان می‌دهد ۲۷ درصد آمریکا را پیروز می‌دانند، در مقابل ۲۲ درصد ایران. در حالی که ۳۵ درصد معتقدند فعلاً هیچ‌کدام برتری ندارند.
🔹
۵۴ درصد جمهوری‌خواهان معتقدند آمریکا در حال پیروزی است، در حالی که این رقم میان دموکرات‌ها تنها ۹ درصد است.
🔹
در مقابل، فقط ۳ درصد جمهوری‌خواهان ایران را پیروز می‌دانند این رقم میان دموکرات‌ها به ۳۴ درصد می‌رسد. همچنین ۲۵ درصد جمهوری‌خواهان و ۴۴ درصد دموکرات‌ها معتقدند هیچ‌کدام از دو کشور فعلاً در جنگ برتری ندارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/682708" target="_blank">📅 00:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682702">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Od40Z0AtopeKzNh3g_Ha3tXoOifv_gaMpnIJYYAHn35yakVRpjvWJwSfK3_rPVi5WpyBCYViVLAj_t2n7rqnvKUnqMj7DezH-G24yy7wAiyHJpA2V2Qq3wsPKYxi0W-6_w08SLyrFPZZPGERNGpjOFaEhHL1LAmdrUVPnrFWTNyNGKZbeRHvu7T7-3Z0gurFWpXCV4MG5k44lgO8T6f4fpJ11pI-dfZm7Ry8PfsrEcIwnXjRb4Yt7Z7r6JvB9ynJIELP4jtaYutEqkuPqMFS98h_Z91NNAzt3fctdae2yhp8jNx1JXqYLXXSxyrCBBKDDuzGig-8lOugFN0WkEMonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfeTANbjBY1P7-MObHDytvc0uA-W_x2Lk3sjatqWQErcl7RGMh06Rgjaa8cQWx93lKGS65ACsFTKs-fsCS3pyLaMvY9ZvTkDdlz4UrU8RXb-jfOM-9YIqsj-0zzwEgujDjndjePCLrxccgFW1ybsloDlHsWoFCrSXJ9WRVwr_jJczRpWVxUfq36vLfZE0mWqleSfuIPeqHWw-mRSY0Gru6jubgfTy2CzlwwPKPhda5HiucqDak078chRX4NGZNt6bl3fdRRedEV-PZDoLhiYsXRd86tFYL92MgVaEIKQTsYAd3OFx6P8PceZ471a8RvSepnu63jWbK8DmKn2g5_s3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCa3lIZapG-wJk0s8iWgf3azNrJxmldZTJ6TgvqG4GFmT9CjM6SwDRf4ZJXxfTFUdq9RYR9AbbLcrcHRf5XVjMbt2eR_EHCYL_9j6nV6EcWorb63QLAbyscYHnsZzb0fZNWc5nckkL9F8Lgkbv-MOunwfP6aNRUdJmdMYhakOVDPvjX0VSBid3p4kntwrCyLIVOBnrAjggq9U3t75JtQDR10g-a_wUhH9NKKxmjEMOFlcSKoQ1ohrDyOOWMKxr46knJAJS5cp5VTqE6Cs0dvMRUVqHhouwCv2Sdjy5jFzAhG41B80wEHaZlcfm7zWpbGYjQDZLuc7JZhddKMMoOYyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAmXGCfuBJfu6kOjB0idaj64YhW3z38OHuZtE4kTEVs1Dx51tCEU8ll5KHFzJletqHnyIx0SRoQBxcX6Sy-vSbRrWk3nc5a0kjIXxk4XSL8FOV8pIZ415MnghMOwhdhMqTCtJUgXdYSyY03LP-5OZZhbnJVXMhrDxze8DZ7gMhaiLObghOBKTKgBaKRcYp65cAzgaCUxF4jnOilyIivTIFctS0ZA-BBnrc2QmiuzTqEmUeILT10WzCoRnSlgbZGx4pYwtItEfumSvjKfoMn9KMUH5q4yBPbgW43_FfMu3MIzISwQoN8dOB8_vsW27gSN5WrvC_tTDQWSGJZkJuENzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9qdIk9-TUfv482AKcgzKdlpw_dF8JMba0xHNtVutKQVQNpyrmWAaVsLkwiBCgziqc-H-bv3TXgTpnUVpYeTUiO8cp9s7cq1LPnUQFe6aYAoJb2wCojawN86pau9uB0himEyNFVgVGdZu6c8IhX67FLco_Dh2HRja2zeioAl8isuU8m2p0ERMmadUqxaXIE4Q9zDmK_tRHNF791PH7wbUizM9gg8ulqAi-eT-uSs5IymVi8w8ZP7x_0EVSkICFVUeZLl0-G46wFA-DBKbQI9uMEpV5xIj0gnjveaxYItyBlkarFaxApsui0UFTCWiqQHPbLeqMnqZ-5emXP8ZYhf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D-o9JfanO1V5uCq8k_O6YvcUj6Y77uam6Z-uFkc03hNjV7nCkrhIPxkJ7ZP6BVgZoFiW2db3DFVisBG5gGNbYKDsgQ5oDmGwdIIsQbFG6UOx5D0-qR7QYVU4TG-1g-2Fwd96D5UKCfCeMQm_cKE66E-lC8u08OKller5GMfymDF-f1i-5HawVRio3eeSsaKukf9bf-6xIpXrQflVDFcn5ZzImg0phJTftg44uiKyOz0VYc5nyTeL7Kql1N4u4pwyCFRdP3d7tWx5JzqPX4tOi9npgsErAIOIjpMxrXS1XeFFn5inarNguwhdYMou_dJPUojX8v6UXhtEkgN9Z10sFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نقشه جدید اروپا در جنگ ایران و آمریکا
🔹
اروپا در جنگ میان آمریکا و ایران کجا ایستاد؟ اگر جنگ جدیدی شکل بگیرد، اروپا چه نقشی خواهد داشت؟ پشت خروج ناوها، واگذاری پایگاه‌ها و تحرکات دیپلماتیک، آرایش متفاوتی در  اروپا در حال شکل‌گیری است.
🔹
در این اسلایدها ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/682702" target="_blank">📅 00:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682701">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGHcG-NNfI9wZlpSFnQXrugOUbFgUyCHVugUHJHEJm7qxsCFnCe_xCf0wjRPpjmrLz6Qn_GGpXdwC0_8kjDiG58UTxxXHpot9H9P0WpuRxKgTimysNHq388db08elAtanU94y7C1cKhb_ELKqS3VewuMmaJjyvMya0iMMcyT5KS6w01G_G4f9Q7-hPKWJKitvqCZEPiyPFM6gXFhe6Q1PtP7D78LZ3qPcYCzZpsI8oK-nfstfwqgKVul63mX-O3T5hkSRPRPu8fAT9lx6AjqeVYfpR1qB93iWWdtFKF_740c3vLXx2D3bbqI5cS_bJZF65FSObq71LjnLtUTkvrNzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رتو کارلوس شایعات مربوط به مسلمان شدن خود را تکذیب کرد
اسطوره فوتبال برزیل:
🔹
من برای دین اسلام احترام زیادی قائلم و دیدن اینکه همسرم نماز می‌خواند، بسیار عالی است.
🔹
اما شایعاتی که در مورد مسلمان شدن من منتشر شده، نادرست هستند.
🔹
کارلوس به تازگی با زنی مسلمان ازدواج کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/682701" target="_blank">📅 00:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682700">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69147ef19a.mp4?token=vthOo5rPxyHcHYpHVSQprskYeBBf8ni7UPvBplyXzdqjvTTffrX-826eRqyS986wF7jr1gSw-JBmcXNa1GjYKNrCcfsk_OSkAdhCGkiJK1hh5Q6e5zFNLIKU76HjR1kCJhLHZVcrMlyG6FxCATWpNdXdH6p2qnjIStZZ10_VwNqlXQlbTNe70P_DpnhVMO143MdpiPKL2gmzas_QlEzct6LRH42ICMqjBbr7KkdHwKJBWW6z681C-YSBB7LZVRiQ4M11RDDyO-4SrrYrjECApniGCK0IfW2QcrVGQhLbm2JGJhlEJn_X8jfODqCxNRKxzNcUam_3Dnx92a-PgewZmk4nG_hB3b3nUFB_2AZIa-z3u-ikInzUEor91cGcrM1YVIy-la7eHxnUdjtTrmLHG8yDPenDyh-PdceLgcY51M5XrJX9vNIbefcwu4F2h9ROiCxy5e1uwFFAH8uSOAS1Q9wxD5md2fEP03yoCADyyAtu6RXCFqRNNt6UgQq6IETVZai_vNNx5TYF1S5DPXN_eMObx1Vizhf2WzCmlneWejiStleSbOLqryvlkf60SVV0hgXUF9ziqCyQdq4w7xeDRrdPny4fup-mmZBPeRYceh6ZkirZh0SnzKUYiP-yIvpJH4WTFIvSXnZM8j--ph71UbVScH6qKMUeo_ouqPTV5zY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69147ef19a.mp4?token=vthOo5rPxyHcHYpHVSQprskYeBBf8ni7UPvBplyXzdqjvTTffrX-826eRqyS986wF7jr1gSw-JBmcXNa1GjYKNrCcfsk_OSkAdhCGkiJK1hh5Q6e5zFNLIKU76HjR1kCJhLHZVcrMlyG6FxCATWpNdXdH6p2qnjIStZZ10_VwNqlXQlbTNe70P_DpnhVMO143MdpiPKL2gmzas_QlEzct6LRH42ICMqjBbr7KkdHwKJBWW6z681C-YSBB7LZVRiQ4M11RDDyO-4SrrYrjECApniGCK0IfW2QcrVGQhLbm2JGJhlEJn_X8jfODqCxNRKxzNcUam_3Dnx92a-PgewZmk4nG_hB3b3nUFB_2AZIa-z3u-ikInzUEor91cGcrM1YVIy-la7eHxnUdjtTrmLHG8yDPenDyh-PdceLgcY51M5XrJX9vNIbefcwu4F2h9ROiCxy5e1uwFFAH8uSOAS1Q9wxD5md2fEP03yoCADyyAtu6RXCFqRNNt6UgQq6IETVZai_vNNx5TYF1S5DPXN_eMObx1Vizhf2WzCmlneWejiStleSbOLqryvlkf60SVV0hgXUF9ziqCyQdq4w7xeDRrdPny4fup-mmZBPeRYceh6ZkirZh0SnzKUYiP-yIvpJH4WTFIvSXnZM8j--ph71UbVScH6qKMUeo_ouqPTV5zY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گره فوق العاده عالی برای بستن کیسه‌های پلاستیکی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/682700" target="_blank">📅 00:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682699">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac1dmVeYFCkhuzZFhQm6YVxwsHY566Qlz3RNqINIp9kxgMyZszjyElMG_4bw4HcneykIPhd0MyIz1ZiOj0L3i-MOxCy2w43ylf44rHcuuU7g5fmVyIsocVVZBIE8uvs5H8wgmXhNT0p4PWMKm8zYDGtkJKBsu8ADrCMMJAbVrikz-ciiakWM7QgpiEYrFZZ0eq1Uw1YaCejLcGnLoXgB5owcw804NiQ9KZtBcaxVFkvVHni_XzV4wsVK40f0AxsN7h0OnnG6jlxLkMexPLj9kzOJlF4W7op3LOCKS8Cxsj6L5fGy9SaEW3a5jrvraavoUq0amEYaEaPBq55sGe4xKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بدهی عمومی آمریکا برای نخستین بار در تاریخ رسماً از مرز ۴۰ تریلیون دلار گذشت!
🔹
داده‌های وزارت خزانه‌داری آمریکا نشان می‌دهد که رقم بدهی داخلی دولت این کشور از زمان دوره اول ریاست جمهوری «دونالد ترامپ» در سال ۲۰۱۷، دو برابر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/682699" target="_blank">📅 00:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682698">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBE74-0axrxFwM0lzv3glvGmeuLIk-0N2S1yhfE42kBZrwbXAGGkFBdAbE9GI80KyKQaOQjRoF9FaHF8hOdqVrbVvTlUpBiHu3HBpAJ52mD5Aweh1CCutg0Ir-C94xVvp3aPbU_DgnFR-p2bZz-Bduf051MWFnskTs7hzA_6XtRym46KAZRNhuv-dVKtaV2g252oo3j5NqL4MDQtA568JB9NZuEcNUgHAOgeBPMlSk_BxQVct2AiAZbEunGPeMLWFAWYwS7BZzD8SEfMObCpJSJkiogyfF2ga5vBL4u9gS1vQiTQ1pRrgLhgm_TGT_pfDL4U739UWE8hdpMna76Hwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رنگ دندان فقط یک موضوع زیبایی نیست؛ دندان‌ها با رنگشان هشدار می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/682698" target="_blank">📅 00:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682697">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
اقتصاد ایران از شوک فاصله گرفت، اما هنوز منقبض است
🔹
شامخ کل اقتصاد با ثبت ۴۸.۳ برای شانزدهمین ماه متوالی زیر مرز ۵۰ باقی ماند. نشانه‌ای که می‌گوید اگرچه شدت رکود کمتر شده، اما اقتصاد هنوز از رونق پایدار فاصله دارد.
🔹
شامخ یا شاخص مدیران خرید، یکی از مهم‌ترین نماگرهای سنجش وضعیت فعالیت بنگاه‌هاست؛ عدد بالاتر از ۵۰ نشان‌دهنده بهبود فعالیت و عدد پایین‌تر از ۵۰ بیانگر انقباض اقتصاد است. در همین حال، شاخص تولید و ارائه خدمات برای نخستین‌بار پس از ۱۴ ماه از مرز ۵۰ عبور کرده است.
🔹
اتفاقی که از بازگشت بخشی از فعالیت‌های اقتصادی خبر می‌دهد، اما ضعف سفارش‌های جدید، قطعی برق و اختلال زنجیره تأمین همچنان مانع بازگشت پایدار اقتصاد به مسیر عادی است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/682697" target="_blank">📅 00:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682696">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQWLcW47erbirY_eMkfDcClnmVGDBwMC0j71UebAJOGRSsxGo5BPotk1V-JwUj-3BrXpG-cPqZIS-be_BaxP1hstSEpicyiEStQTraa8gC9cSdRZad4OlsBvZ7rrIi9veIudbJnTGvC5HALZMHBiA1iCqe12gBm91oeEgDW7fYK2WlXZcqgVbJkjCiL8l5HCV2SlUrBLSp84lSbvVTbZZApmFmZsY4ofjZ2ALDaQ-etCrgXlXslWTAZOar5IsFXFFcwQaznmzvxrvkZP3A-GWvDsd8oxVReMriE8iab7-tBvZi4LQ-8FJENBkdo6tLZSQL2DStl-HdrovKd7mKr5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هوش مصنوعی‌های مناسب تولید محتوا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/682696" target="_blank">📅 00:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682695">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
شکایت جمهوری آذربایجان از شبکه سی‌ان‌ان
وبگاه واشنگتن اگزمینر:
🔹
جمهوری آذربایجان از شبکه خبری سی‌ان‌ان به دلیل انتشار گزارشی جنجالی مبنی بر اینکه رژیم اسرائیل تیم‌های پهپادی و کماندویی را از خاک خود علیه ایران به کار گرفت، شکایت کرد.
🔹
در ماه ژوئن، سی‌ان‌ان گزارشی منتشر کرد که در آن ادعا شده بود ده‌ها مأمور موساد و کماندوهای رژیم صهیونیستی از یک پایگاه مخفی در جنوب جمهوری آذربایجان فعالیت می‌کنند و از طریق آن مأموریت‌های جمع‌آوری اطلاعات و حتی ترور با پهپاد را انجام می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/682695" target="_blank">📅 00:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682694">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تغییر نگاه مردم ایران به طلا: طلاسازان بی‌ چاره شدند
عباداله محمدولی، عضو هیئت مدیره اتحادیه فروشندگان طلا در
#گفتگو
با خبرفوری:
🔹
به جای اینکه فقط به ذخایر طلا فکر کنیم باید به سمت تقویت تولید برویم و چیزی که می‌تواند جایگاه طلا را در اقتصاد تقویت کند تولید، فعال شدن کسب‌وکارها، ایجاد اشتغال پایدار و ورود ارز به کشور است.
🔹
امروز حدود ۹۰ درصد مردم طلا را با نگاه سرمایه‌گذاری خریداری می‌کنند و فقط حدود ۱۰ درصد برای زینت و مصنوعات طلا خرید انجام می‌دهند و همین تغییر نگاه باعث شده تولیدکنندگان مصنوعات طلا با کاهش تقاضا مواجه شوند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/682694" target="_blank">📅 00:16 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682692">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ccd0468a.mp4?token=NUedoPa4BbaKM1JrYjOZZIZY-GPo2Tm2E-PL_UPeXzYk3cpSSVYXasl-J2AAGBdZ01Wv5YEsL9s2EgKka5vN65LdyJuU9PxpXnMFThSo8UsGfFWltWDiWb627_-omrZHTyYf2VvjJnJ2CkVwSccDRu22oTh7rtgL-Yb9DVrrFvIFuPdD83xOY6_qgV3HbziNYqnt0XDBcTEHBJjUxwwaV40BVKX-POt8UPPZz0x4mZFXTRGYTlATInoOu39qfD-zr5zhm1jcy-J3JT3Xn_DAIOGfgu7FFXT3fftmRGLycmqYxQiqu-Qzqsv4Z5ZosBABIr3pLefsbzc0NkSoAkeg1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ccd0468a.mp4?token=NUedoPa4BbaKM1JrYjOZZIZY-GPo2Tm2E-PL_UPeXzYk3cpSSVYXasl-J2AAGBdZ01Wv5YEsL9s2EgKka5vN65LdyJuU9PxpXnMFThSo8UsGfFWltWDiWb627_-omrZHTyYf2VvjJnJ2CkVwSccDRu22oTh7rtgL-Yb9DVrrFvIFuPdD83xOY6_qgV3HbziNYqnt0XDBcTEHBJjUxwwaV40BVKX-POt8UPPZz0x4mZFXTRGYTlATInoOu39qfD-zr5zhm1jcy-J3JT3Xn_DAIOGfgu7FFXT3fftmRGLycmqYxQiqu-Qzqsv4Z5ZosBABIr3pLefsbzc0NkSoAkeg1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از فوران آتشفشان اتنا در جزیره سیسیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/682692" target="_blank">📅 00:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682691">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjhuL_EZFW4lrzOp7aksYywefyZtv73ihzdEZzqd3wkw6O528HsZPqUlhBZVXkm1uoENC3TVUSKhMm-UmJgyrEKLRUI7Z6DG19lTtFIyu9LskwitH5p4otZcCVsW_mzN8BDeGAk9OOsKvAHbtsMrwqfgpsEE8Mn41K2o1jrFibsvoCHM8DbQx9gN_EAy-3kUgogYWyICdY7szKmjs8v-L3VbhM7CRswe_F_h1BelT3glLNYMfhEiP4hFOYf7Ot2oH7GwJUWb2zXrnVohSHY9AkkxJ1H0tDg_1kEkDwesXdHgp9i-oqNsNzT3SSgmHQf6ga0Jwc87eI-iAsXduziShw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انس طلا به ۴۵۰۰ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/682691" target="_blank">📅 00:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682690">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0xL5Tusm5ICIczvZkTOpgcmNnml4WmD5L8-kfFy3NVruLhS3GYiivbTjapDfaJaFbrJ-1OwzbMOymPCwsmsFQzMAKdvVctTBGAr99E273DzenBUCfnZ5Gj0QKLX8MEatBud8rKR3jDQePkkLckcP1GZvFz7drzgnvcd65vjKuBOR5w9vspEc2uUw85kKVDOVIbrhLFM074qdcCapZAJApdRAXdFpIzjr-UcLO5prxCPGSHIQtKMDN_CpF9kuiY5xUvkjWRBMuLgZXAz8lIBr7mckU53oDUaCjK7HcoCk1vc-T7EB9glF8-5mKgy-KWJXrK2sgxGqQe-sYzFvLnM7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/akhbarefori/682690" target="_blank">📅 00:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682689">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381825a269.mp4?token=S5hSQn3xz8Tcb-nMKXQpnMPen-UnJyzHiTOFplXeFLfGzCHH_g-J3hOU-ujNbCkD8mwMIPb2kr2LxId4KmkLAqAJRNIofs2-fWCu8S1WRvzrK1HiaXi2iDHUaOPqy5OX962mlQ2D5oMgWLe6PGfr37-gIskHnMfuHGhftSpAPrCEfrK8b2TVrYv-LlcdJpPHV-0o9q_AGWJ--5v3Au0BZN1KSouOnEfOQAPPJ3wMfc7p1cHWWVGXrakk-eGEkS0rHACc6OF-fiuNPNYfTJ9iAAepW1CoMWhaTE5wtMi7Ly0kQRw0HpLH4ogVWCMcMGZa1dct3Ojk29vq_q7oev4zRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381825a269.mp4?token=S5hSQn3xz8Tcb-nMKXQpnMPen-UnJyzHiTOFplXeFLfGzCHH_g-J3hOU-ujNbCkD8mwMIPb2kr2LxId4KmkLAqAJRNIofs2-fWCu8S1WRvzrK1HiaXi2iDHUaOPqy5OX962mlQ2D5oMgWLe6PGfr37-gIskHnMfuHGhftSpAPrCEfrK8b2TVrYv-LlcdJpPHV-0o9q_AGWJ--5v3Au0BZN1KSouOnEfOQAPPJ3wMfc7p1cHWWVGXrakk-eGEkS0rHACc6OF-fiuNPNYfTJ9iAAepW1CoMWhaTE5wtMi7Ly0kQRw0HpLH4ogVWCMcMGZa1dct3Ojk29vq_q7oev4zRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بمب خبری هانتر بایدن: ترامپ از خون و ویرانی در غزه و ایران پول می‌سازد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/682689" target="_blank">📅 23:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682688">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
جان بولتون: عمان مشکوک است
جان بولتون در گفتگو با پایگاه خبری هیل:
🔹
تهدید جدید ترامپ علیه عمان نشانه‌ای از این است که او در دریا گم شده و نمی‌داند در بحبوحه این درگیری چه کار کند.
🔹
عمان «انتخاب مشکوکی» برای میانجیگری در این مذاکرات است. ترامپ استراتژیک فکر نمی‌کند. او دامنه توجه کوتاهی دارد و ما تا حد زیادی به همین دلیل در جایی هستیم که اکنون هستیم./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/682688" target="_blank">📅 23:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682687">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7eYixVcR6igr9aJUfc-YgKn2c79o4T8ZvReI2FvBgWSp4-224BBKdzkTemwENgbNVvLZKeBjhHTB4ZvIznzYUn16rBKAYGoUP9zYP82gvJMm8zJV_1LmC02XxclgcSxMAG9SKdT214bH6ZhfcWNV3qpAl8Nur6330ejLb0QYUCzooK634CZp8Y58a6fQzEjJiZJuUCDO0rxzYYjyflwRW92eV427Mwyyyyfz3rgXQ5N--OePUBH1LC3qrXm4VynFhWM0MZ6ssugQ5zyTVJ3G-dWCmjV7TrwZicqKocHcCBJPaR0M66BzJUjZgutw7bOv5hU5qWahJbeWpXumYAhPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سمت دشمن
🔹
امارات در ادامه هم‌سویی خود با آمریکا و اسرائیل، تمامی مبادلات تجاری و معاملات مالی با ایران را تا اطلاع ثانوی به حالت تعلیق درآورده است. این تصمیم به گفته منابع اماراتی، پس از ادعای شناسایی دو موشک بالستیک ایرانی که مسیرهای کشتیرانی را هدف قرار داده بودند، اعلام شده است.
🔹
هشتصدوسی‌‌وهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/682687" target="_blank">📅 23:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682686">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1w3EPpmRFvXhgqStpKKCt1yQcC7Ga7kxB_n1fsWX6Sst1HyszxMzZn4z5yHvgfAUoE7VQlblHj2JHMMEPwfKsQGcVXOhTNlKiIQqBeim_5U9YHslO8Wex87jIK9sFu0u4LjLJxcJ-m48vqk-zCpakPX3ZWCGQwUVCLDJPAMZvhArASheby6PaM6C-A0EwaYAAk0NBEbIzCMuLfEzN8M11gkABXbjq3tIod1wCpYfMHmaZ0Wd4orjV0r8Ea1ZF1rheY81nEVXAnyrYgKZD7DbSDhxatL59RF0eb0aplIwxQwtV7wm3KKJty__TSZZ_bu6IdtHXZDzF8gjw3GXNq0nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرسودگی ناوگان آمریکا؛ فرصتی تبلیغاتی برای چین در اقیانوس آرام
🔹
به گزارش «اسرائیل هیوم»، ادامه جنگ با ایران فشار زیادی بر نیروی دریایی آمریکا وارد کرده است. ناو هواپیمابر «آبراهام لینکلن» پس از بیش از ۲۵۰ روز حضور پیاپی در دریا، با کمبود غذا، مشکلات آب و فاضلاب و نگرانی‌های فزاینده درباره سلامت روان خدمه روبه‌رو شده است.
🔹
آمریکا برای مدتی نیز هیچ ناو هواپیمابری در اقیانوس آرام نداشت؛ زیرا ناوهایش به خاورمیانه منتقل شده بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/682686" target="_blank">📅 23:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682685">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpRq4GaLaqRCZKrwUb9BOdsTXnvinIouwdRDHCCsE6rdio5ztmy0RgJW9uw5UwHWLtw0m14v8bS5XFd3YNuSf1KwWvUpLn5qOC5IpCD0xrVhYcWwKGNXhb2jUGhzDFEEbWKRXWrB20xH1AFCW04HbnHLscMlG-QCAOiHsp23ZUTbYte9HQ2oTI2dreFRq6ksth2qH9XkLa8NPE1xX_hgR2NF2MPEFeU05LpU7L8goU_Gy7ku6XRCKF_5NX5mM4kIUAL-FPDiLgayHQu64pXUPQViJk0U9vXWWDxro8YkKwWKW82HAWYZg-VZV6Oi2ARfzaSfiQG9vLTZTn6TA6RfiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران و آمریکا در آستانه کدام جنگ؟ / ۵ سناریو درباره آینده رویارویی تهران و واشنگتن
🔹
شش ماه پس از آغاز درگیری، جنگی که قرار بود کوتاه و تعیین‌کننده باشد، به یک بن‌بست فرسایشی تبدیل شده است؛ تنگه هرمز به مرکز ثقل بحران بدل شده و هم‌زمان با عقب‌نشینی دیپلماسی، خطر یک محاسبه اشتباه می‌تواند جنگ را وارد مرحله‌ای کاملاً تازه کند.
گزارش کامل را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3239054</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/682685" target="_blank">📅 23:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682684">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9840899c49.mp4?token=Suux_QfGp4rJ6G84NBYeFeJrO7SDJJXLmlMalDYybDC1baofwILwaVB__Xidq_ngkDyJComvK30WfyvbMGqs5Yqo4WhLcfbUwj6dsS24RDaGWpTvc5ifnfBhCJLnwXHfdHJlwo4u7Vp_eTkOQjJziaLxnZzvoO2VsJccTpjiyYSRqOz8z7uycrD69rdaE4ZzKDRQcg1MnU7xlj3DewJ63spK_zK4xmtlhAQSdMJ7bgcmZDDnLRHtd_4LwrBmwrx11CFqnl0av_RCcM3-k0MWa0T3uklQv6cTHcSliCV-9CJvGzF8Ya3pyCLrIQcYL_pOxBuFh8jL4T5zXFAogAQw1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9840899c49.mp4?token=Suux_QfGp4rJ6G84NBYeFeJrO7SDJJXLmlMalDYybDC1baofwILwaVB__Xidq_ngkDyJComvK30WfyvbMGqs5Yqo4WhLcfbUwj6dsS24RDaGWpTvc5ifnfBhCJLnwXHfdHJlwo4u7Vp_eTkOQjJziaLxnZzvoO2VsJccTpjiyYSRqOz8z7uycrD69rdaE4ZzKDRQcg1MnU7xlj3DewJ63spK_zK4xmtlhAQSdMJ7bgcmZDDnLRHtd_4LwrBmwrx11CFqnl0av_RCcM3-k0MWa0T3uklQv6cTHcSliCV-9CJvGzF8Ya3pyCLrIQcYL_pOxBuFh8jL4T5zXFAogAQw1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با بطری های دور ریختنی گلدان‌های جالب و زیبا بسازید
🪴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/682684" target="_blank">📅 23:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682683">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون بهداشت: مافیا خود ما هستیم
عمر علیپور اقدم، عضو کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
اگر دارویی در کشور پیدا نمی‌شود اما همان دارو در بازار سیاه مانند ناصرخسرو وجود دارد باید پاسخ داده شود که این داروها از چه مسیری خارج می‌شوند و چرا در داروخانه‌های معتبر به دست مردم نمی‌رسند.
🔹
ما همه مسلمانیم و نباید دروغ بگوییم مافیا خود ما هستیم و باید ریشه مشکل را پیدا کنیم و ببینیم داروها از کجا ناپدید می‌شوند و چگونه سر از بازار آزاد درمی‌آورند.
🔹
وقتی دارویی در داروخانه‌های معتبر نیست اما در بازار آزاد پیدا می‌شود یعنی یک جای کار در زنجیره تأمین و توزیع دارو می‌لنگد و باید مسیر خروج داروها بررسی شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/682683" target="_blank">📅 23:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682682">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ترامپ باز هم درباره هرمز به تناقض‌گویی افتاد
🔹
ترامپ متوهم که در داخل آمریکا به دلیل افزایش قیمت بنزین در نتیجه جنگ علیه ایران مورد انتقاد قرار گرفته اظهارات ضد و نقیض خود درباره تنگه هرمز را تکرار کرد.
🔹
او از یک طرف مدعی شد که تنگه هرمز الان باز است و…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/682682" target="_blank">📅 23:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682681">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ژنرال نزدیک به نتانیاهو: اسرائیل برای حمله پیش‌دستانه احتمالی به ایران آماده می‌شود
ادعای میدل‌ایست‌مانیتور:
🔹
سرلشکر اوزی دایان از نزدیکان نتانیاهو گفته که اسرائیل در حال جنگیدن برای "بقای خود" است.
🔹
او هشدار داد که این کشور نمی‌تواند به طور کامل برای مقابله با مسئله ایران بر امریکا تکیه کند.
🔹
دایان گفت که اسرائیل خود را برای امکان انجام یک حمله پیش‌دستانه علیه ایران آماده می‌کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/682681" target="_blank">📅 23:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682680">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e9b4d4640.mp4?token=kXjZl31E3eVvLlRm3MWTTavQxAKIHj7IIl3AW19oW0rYBg_liIjJyrz9Bn7b_WdLsc8clAj72wvjf2i-6dk59lBMj3Dmsu_xMDYhKOPV1dz41hUvexTiuyZVZ19tTFwGG_Pys90oFWUFs46Reu3Oxy04NHqaRX1vvL1XQV1gmbv3_5XZ6V6dOuhT7fuII0ALti7t1MzCWl6bSkQ6I_l90GMx8sPaAhETQx2iuKsmyWRyshQ01Luok2xMvSWrVroMF2_Gh8PsvZ2CD2tFba_kYeGqrKtAO2iII3WkBuJ5LJeF5XxKEhfAn2AxiVGK203vV1o8MR1vBRFU03ZjJBJMpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e9b4d4640.mp4?token=kXjZl31E3eVvLlRm3MWTTavQxAKIHj7IIl3AW19oW0rYBg_liIjJyrz9Bn7b_WdLsc8clAj72wvjf2i-6dk59lBMj3Dmsu_xMDYhKOPV1dz41hUvexTiuyZVZ19tTFwGG_Pys90oFWUFs46Reu3Oxy04NHqaRX1vvL1XQV1gmbv3_5XZ6V6dOuhT7fuII0ALti7t1MzCWl6bSkQ6I_l90GMx8sPaAhETQx2iuKsmyWRyshQ01Luok2xMvSWrVroMF2_Gh8PsvZ2CD2tFba_kYeGqrKtAO2iII3WkBuJ5LJeF5XxKEhfAn2AxiVGK203vV1o8MR1vBRFU03ZjJBJMpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: بخش عمده‌ای از تورم مربوط به تخلفات بانک‌ها است
🔹
به‌هیچ‌وجه در قبال بانک‌های ناتراز مماشات نخواهیم کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/682680" target="_blank">📅 23:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682679">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ed8453ff.mp4?token=T22vh9p-6ti2XFoEPB-8U-FFvd5SW4ZdUn0prAMEXadiKqfRmJSL23YWar87ftKcNG1rxNt88ZutWW31jueY-DjwmXe9p89V4Z-F65gTEpRVVBWX5Ey7oqLXYqGO6yKXivSlO3ivcN08f0egEFKJtnrsdYWfPnKC1RHImzoX5oNt46tFpljIpE3YsN_J59jSeFhN3E0ZMPRie8Ea78bXcc43CtAf5K8awCSzxpMxAO3ITEdEI6-NavJXIqk6tedbLviXprlt5Lu0HjUtFVGdIbAAkxUa6E76Z4XUc2rQlxjtX0VgRg3M8A3AK2Zh7N0WGJRa7O57lqlfMoPLItKCUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ed8453ff.mp4?token=T22vh9p-6ti2XFoEPB-8U-FFvd5SW4ZdUn0prAMEXadiKqfRmJSL23YWar87ftKcNG1rxNt88ZutWW31jueY-DjwmXe9p89V4Z-F65gTEpRVVBWX5Ey7oqLXYqGO6yKXivSlO3ivcN08f0egEFKJtnrsdYWfPnKC1RHImzoX5oNt46tFpljIpE3YsN_J59jSeFhN3E0ZMPRie8Ea78bXcc43CtAf5K8awCSzxpMxAO3ITEdEI6-NavJXIqk6tedbLviXprlt5Lu0HjUtFVGdIbAAkxUa6E76Z4XUc2rQlxjtX0VgRg3M8A3AK2Zh7N0WGJRa7O57lqlfMoPLItKCUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عادت کوچک غلطی که اگر به صورت نادرست هم انجام شود به لثه‌های شما آسیب می‌رساند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/682679" target="_blank">📅 23:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682678">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a488bd8cda.mp4?token=HZv0z13-dh2CwQdtM5ZyExqa6oLawzJr_HnJo8pQUIaf84CYg7ovRytbBWf0lGQaW3OZCUM-cavQ0VcgVJnhGlJ9mIS-czw0WaFZhxOYD7HYJgB6b-ujuEomXPgnJQbid98-bUm613JLYJWp1-47RqrMf2W1fCv2EcnwYnn-8QqBQKuzbDPIFmBaHNyqSFoBkbWMCbrMcL3whp2pKdBTsBoqWHN2-HaloKt23qWZi_s8lJdcWbq-_Z5zkupn73N9e9xE6FAnhUT36PgXq4l8KaUxuhirREFA9hUFBd-HKEiKZ3ZUngwltwVC-4wKmBfpmJYcVIdp2jYFPlBcsAX-yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a488bd8cda.mp4?token=HZv0z13-dh2CwQdtM5ZyExqa6oLawzJr_HnJo8pQUIaf84CYg7ovRytbBWf0lGQaW3OZCUM-cavQ0VcgVJnhGlJ9mIS-czw0WaFZhxOYD7HYJgB6b-ujuEomXPgnJQbid98-bUm613JLYJWp1-47RqrMf2W1fCv2EcnwYnn-8QqBQKuzbDPIFmBaHNyqSFoBkbWMCbrMcL3whp2pKdBTsBoqWHN2-HaloKt23qWZi_s8lJdcWbq-_Z5zkupn73N9e9xE6FAnhUT36PgXq4l8KaUxuhirREFA9hUFBd-HKEiKZ3ZUngwltwVC-4wKmBfpmJYcVIdp2jYFPlBcsAX-yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از قانون نبوغ تا ترامپ نادان!  ترامپ: من قانون "نابغه" را امضا کردم اسم آن را به افتخار خودم گذاشتم
🔹
من نمی‌خواستم از اسم خودم استفاده کنم، بنابراین فقط آن را "قانون نابغه" نامیدم. #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/682678" target="_blank">📅 23:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682677">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
همتی: بسیاری از همسایگان ما حتی جرئت عکس گرفتن با ایران را ندارند
رئیس کل بانک مرکزی:
🔹
بسیاری از کشورهای همسایه می‌گویند حتی برای نشستن، فیلم گرفتن یا عکس گرفتن با ما تحت فشار قرار می‌گیرند.
🔹
جمهوری اسلامی یک‌تنه در برابر استکبار ایستاده و این ایستادگی در جهان بازتاب گسترده‌ای داشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/682677" target="_blank">📅 23:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682676">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g33BY0nRDUYOt10gidWnV1IuCVP-5_bEF-_LTIW4A9CMDXXjoai-1JE1aFNiweBWe4awffOL8fZR77Ii_dTz-I0txypnw5kgEDd5AhCBx_pNQ-2BHMQ5bK9JHyee_aADaH8J_rvOHDgycosNtTvFzbftMboPoT8q2ShvBFM2NwhbbDpZwhM19T3Vm5m7z6Rf_WB1m_ahXFf49i0QseZOy1mej54kQh6BzKhQsAFEba4xz4LEysLWjT0Q5vZz256Nu9G0S5wPdpsiu1bEY9m10QBcnp4Vzy2cF-Ypgbsq0M3sXrjXi5a_JJCceY33eWv-ly6J4bY2VXHZ9ckIW5k5Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بایدها و نبایدهای شب قبل کنکور که لازمه حتما بدانید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/682676" target="_blank">📅 23:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682675">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آمریکا واقعاً می‌تواند وارد جنگ زمینی با ایران شود؟
🔹
پشت تهدیدهای واشنگتن، یک سناریو مطرح شده؛ اما ورود زمینی می‌تواند برای ترامپ از یک عملیات نظامی، به یک کابوس سیاسی تبدیل شود.
🔹
چرا حتی بخشی از جمهوری‌خواهان هم با این گزینه مخالف‌اند؟ پاسخ، معادلات جنگ را عجیب‌تر می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/682675" target="_blank">📅 23:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682674">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای
سی‌ان‌ان: تمایل عراق برای میانجی شدن بین ایران و آمریکا
سی‌ان‌ان:
🔹
احتمالا یکی از اهداف پشت پرده دعوت عراق از قالیباف این بوده که بغداد خود را به‌عنوان یک میانجی بالقوه میان آمریکا و ایران مطرح کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/682674" target="_blank">📅 23:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682673">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
بازار کار کوچک‌تر شد؛ ۶۱۱ هزار بیمه‌شده و ۷۷۰ هزار شاغل کم شدند
🔹
گزارش مرکز پژوهش‌های اتاق ایران نشان می‌دهد بازار کار در سال ۱۴۰۴ تحت تأثیر جنگ، بحران‌های اجتماعی و اختلال اینترنت با فشارهای جدی روبه‌رو شده است.
🔹
تعداد شاغلان از بهار تا زمستان ۷۷۰ هزار نفر کاهش یافته و بیش از یک میلیون و ۳۵۸ هزار نفر از بازار کار خارج شده‌اند. همچنین شمار بیمه‌شدگان ۶۱۱ هزار نفر کمتر شده است.
🔹
در همین حال، افزایش اشتغال ناقص و رشد ۱۲ درصدی کارگاه‌های یک‌نفره در کنار کاهش بنگاه‌های کوچک و متوسط، نشانه‌ای از تغییر نگران‌کننده در ساختار اشتغال ایران است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/682673" target="_blank">📅 23:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682672">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d50b79f5c0.mp4?token=P7ulKC-dVgqZlnryGieb4C2TsNv9_jB022qbSc8IaCgXXltyyhj8JAUBJhuhISxgKYqAJ6UK3VQLFR-HtWWnYEiJW1pLNk87HebmZvnHA6d9R4cfFfuQv019XeX2T4yHEMWBs9yA6e9f6JiCYHIGmpm8pkP4MhTUYEYbrFJzmdwRdHtxtxXRBQurtYspmMaesFBeiDMqQT3x81kGQRqnihCGd384R8Gby1DiPKAtISHoYNpzT0slnp9h-bZVFFi88-QTyQHan1rn9YVHFg-9V2q96XwJ183dE1xwxz56mcA4tZ1_LhMU0pvJRfhtlf0QDSQg2D0Rwt-aiX2tbnRcWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d50b79f5c0.mp4?token=P7ulKC-dVgqZlnryGieb4C2TsNv9_jB022qbSc8IaCgXXltyyhj8JAUBJhuhISxgKYqAJ6UK3VQLFR-HtWWnYEiJW1pLNk87HebmZvnHA6d9R4cfFfuQv019XeX2T4yHEMWBs9yA6e9f6JiCYHIGmpm8pkP4MhTUYEYbrFJzmdwRdHtxtxXRBQurtYspmMaesFBeiDMqQT3x81kGQRqnihCGd384R8Gby1DiPKAtISHoYNpzT0slnp9h-bZVFFi88-QTyQHan1rn9YVHFg-9V2q96XwJ183dE1xwxz56mcA4tZ1_LhMU0pvJRfhtlf0QDSQg2D0Rwt-aiX2tbnRcWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: بخش عمده‌ای از تورم مربوط به تخلفات بانک‌ها است
🔹
به‌هیچ‌وجه در قبال بانک‌های ناتراز مماشات نخواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/682672" target="_blank">📅 23:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682671">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
همتی: بانک مرکزی هیچ برنامه‌ای برای تغییر نرخ سود بانکی ندارد
رئیس کل بانک مرکزی:
🔹
افزایش نرخ سود بانکی نیازمند الزامات ساختاری است که در حال حاضر به‌دلیل ناترازی جدی شبکه بانکی کشور فراهم نیست.
🔹
بانک مرکزی در کوتاه‌مدت هیچ تصمیمی برای تغییر نرخ سود بانکی ندارد و روند سیاست‌گذاری موجود را ادامه خواهد داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/682671" target="_blank">📅 22:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682670">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051dde39f2.mp4?token=oTJ7E7xO1vOgHfdn3ScEEvK0kLsw_M-dHNDfT8xWWb8QVf5JFuuATYDdiAzuJIon3SS1UQ3PeHaBc2rnEEMWe6GHCfUAVICvAiLlMuTXhRLnIBZuso36PO54OCTgJMVfFTxnLP_bkB1VBxYk8Nrv2jjMYmsYEUUDmZLh2XBky2tv6ugtq0kgaiQG6tFVPpq7pM5SGqAx6OIzMT9SKWxGR5LNut4RlG2u0K_r9wWerj5JbO6FbjN7AGMfwMBl8mTRKQEBq8zIxcKASCez8hbI3GlkOScYPjwA-9LLBm5uOd04ytY4RZVq9VEOfoN4i-hULWyJXj3doOwQu1x4s1-Ghg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051dde39f2.mp4?token=oTJ7E7xO1vOgHfdn3ScEEvK0kLsw_M-dHNDfT8xWWb8QVf5JFuuATYDdiAzuJIon3SS1UQ3PeHaBc2rnEEMWe6GHCfUAVICvAiLlMuTXhRLnIBZuso36PO54OCTgJMVfFTxnLP_bkB1VBxYk8Nrv2jjMYmsYEUUDmZLh2XBky2tv6ugtq0kgaiQG6tFVPpq7pM5SGqAx6OIzMT9SKWxGR5LNut4RlG2u0K_r9wWerj5JbO6FbjN7AGMfwMBl8mTRKQEBq8zIxcKASCez8hbI3GlkOScYPjwA-9LLBm5uOd04ytY4RZVq9VEOfoN4i-hULWyJXj3doOwQu1x4s1-Ghg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از قانون نبوغ تا ترامپ نادان!
ترامپ: من قانون "نابغه" را امضا کردم اسم آن را به افتخار خودم گذاشتم
🔹
من نمی‌خواستم از اسم خودم استفاده کنم، بنابراین فقط آن را "قانون نابغه" نامیدم.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/682670" target="_blank">📅 22:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682669">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
همتی، رئیس‌کل بانک‌مرکزی: کالابرگ باید ۲۳ درصد افزایش یابد و به ۱ میلیون و ۲۳۰ هزار تومان برسد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/682669" target="_blank">📅 22:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682668">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d98f856478.mp4?token=fLXXNNisfcsMEIWlFEGoiSNVFXD0YQwEmfOPDGbm8Pj-pjKBn69zt0kVZsoFBwTa-Ppig0pp_Sn6RL-tQ8-VsDd1ngfaZrjetihfJIWjzocMsSUDAzeC_XiIfE6cHRsjyW5haTEYcBAf1xtBZ-D4_4utniPZq1IZ_uMAlYju1WKcH_XIENnihGqWExPzuSW2o78wg1Y6TnYFLq8FRS2_U1iDTwmbMiW-SELIfHnzP8HEIUUN1Dn9L8b0VmKecnr380DMHI7eS__p3vYMR7KE3kmLa-X3T4BbEF4t9oQYGKD7-E5vbhFhq2H-JbcgouYgit2bk7IymJ3zLLHkzu1N-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d98f856478.mp4?token=fLXXNNisfcsMEIWlFEGoiSNVFXD0YQwEmfOPDGbm8Pj-pjKBn69zt0kVZsoFBwTa-Ppig0pp_Sn6RL-tQ8-VsDd1ngfaZrjetihfJIWjzocMsSUDAzeC_XiIfE6cHRsjyW5haTEYcBAf1xtBZ-D4_4utniPZq1IZ_uMAlYju1WKcH_XIENnihGqWExPzuSW2o78wg1Y6TnYFLq8FRS2_U1iDTwmbMiW-SELIfHnzP8HEIUUN1Dn9L8b0VmKecnr380DMHI7eS__p3vYMR7KE3kmLa-X3T4BbEF4t9oQYGKD7-E5vbhFhq2H-JbcgouYgit2bk7IymJ3zLLHkzu1N-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک Y2 Zhuque-3 ساخت چین بازیابی مبتنی بر زمین را برای اولین بار تکمیل کرد و راه را برای موشک‌های قابل استفاده مجدد چه در دریا و چه در خشکی و هزینه‌های پایین‌تر هموار ساخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/682668" target="_blank">📅 22:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682667">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVcpCikZKFJfdFBv_XISZt0YZEukm8ySw3wjBU4_OdJgfJnwD7tq2mUh4GzHj7ZekICQsLU1ZKSv47tSvJRr2ZCBu4H1yv8H7psbiN4IKyEkD9pDhzMU0LyB9hzPNV5QoSfUP762BCvJJVECc65xaBQEQ_mtp1WJY80B-42IXGtFgjta-4096opX-wvySfhKv2NfenWzGXEm7RU3Aj_eunLfeYzxysNIQmM7bVcmXlEIMP3ayUvBNOD1M4K5AywaXZgmMD6VbWuSOg8x1E0FVyivCiU6Jw3hu0dH6h4zQH4UV7g_LxKUh0eAB6ij8BK7J9UyWWN2qLjpT87aEZy5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آناتولی: عراق از ایران خواست تنگه را به روی آنها باز کند
ادعای آناتولی:
🔹
عراق از ایران درخواست بررسی ویژه در مورد صادرات نفت از طریق تنگه هرمز کرد. این درخواست در جلسه‌ای در بغداد بین روسای پارلمان دو کشور مطرح شد.
🔹
عراق همچنان در میان کشورهایی است که بیشترین تأثیر را از تحولات منطقه‌ای می‌پذیرند و بر اهمیت روابط دوجانبه عمیق‌تر و همکاری فزاینده بین بغداد و تهران تأکید کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/682667" target="_blank">📅 22:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682666">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da6b7d5420.mp4?token=azPsQl9kpNhaVZ48b0Cuw5uMX2TczLAxGko0hG3HvUo-c9x5GAl_S_Bgh7rHOnsr0of954jBn8LUI75KPBrFMLqXy3BvahpggrZvsmgeU65YFbofgMBPbIQJilAhE6x9Mqhjz1iOkXcQENh1q3qN_8oFxoXBaKf0tR7TP1fK0sstkLuqHJhK6ogetrWOysEbdk0fZlS84lw1xQoo276HsApGd4OINDOyPju-jtBVZaqNH2FiYU5H0vRYUwjWppjn63OJwW-cp7AiedBE1SQxUl8CS_uDYkR1hI58dBGdu440OKDX_PMVcnVqxbbbx6LJTXLU0syPptt4AapIdKB_wTDDVuTxW9VYrDYCuetAvZzpY7hOAMLvlL_Jixlc29HRjib5OuWVY_lWGhwJhBd-6lu1-hDIM2AAAljjzeDBYgSRHAakEwbUwrhFZhGjcLaNW_0OAh7W9wFD5YRPTUuWNAa2BNILDmNvppy9xaQu7w4DdE_2f0wSNg-XER_0qyvd9stJDWmVtZIzNYsybCQ-OzGaIr2AmGT9bHakIkCIJa7JhOmkwBT3NfQgtQEoXgVodCImAKaOPmHUErGY0BotYyp6V-yKDUzFHPc_v6pbrNjjebR1fHhLcHIssFzz0rOnhg01Tq0SXbkpBDkJXns9A-rylvZj81GN2IjqKNi3sC8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da6b7d5420.mp4?token=azPsQl9kpNhaVZ48b0Cuw5uMX2TczLAxGko0hG3HvUo-c9x5GAl_S_Bgh7rHOnsr0of954jBn8LUI75KPBrFMLqXy3BvahpggrZvsmgeU65YFbofgMBPbIQJilAhE6x9Mqhjz1iOkXcQENh1q3qN_8oFxoXBaKf0tR7TP1fK0sstkLuqHJhK6ogetrWOysEbdk0fZlS84lw1xQoo276HsApGd4OINDOyPju-jtBVZaqNH2FiYU5H0vRYUwjWppjn63OJwW-cp7AiedBE1SQxUl8CS_uDYkR1hI58dBGdu440OKDX_PMVcnVqxbbbx6LJTXLU0syPptt4AapIdKB_wTDDVuTxW9VYrDYCuetAvZzpY7hOAMLvlL_Jixlc29HRjib5OuWVY_lWGhwJhBd-6lu1-hDIM2AAAljjzeDBYgSRHAakEwbUwrhFZhGjcLaNW_0OAh7W9wFD5YRPTUuWNAa2BNILDmNvppy9xaQu7w4DdE_2f0wSNg-XER_0qyvd9stJDWmVtZIzNYsybCQ-OzGaIr2AmGT9bHakIkCIJa7JhOmkwBT3NfQgtQEoXgVodCImAKaOPmHUErGY0BotYyp6V-yKDUzFHPc_v6pbrNjjebR1fHhLcHIssFzz0rOnhg01Tq0SXbkpBDkJXns9A-rylvZj81GN2IjqKNi3sC8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی، رئیس‌کل بانک‌مرکزی: کالابرگ باید ۲۳ درصد افزایش یابد و به ۱ میلیون و ۲۳۰ هزار تومان برسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/682666" target="_blank">📅 22:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682665">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoDUKBHt8Gi6lGY8ubCAOn5dKNcfT5grYw_uQSGVaht8tQGsbo8AwOH9bCgwO5LtmSHJPbceWv281d277lLBMbiZoRewsloPh8ze7W7CuC--vhj81dt8AAPRvKnn297tjYbn4cxV8RrZBTpDJktumVaaj-V8SwQ9yqzG9gm1v0X8r6q0-t16PRXgawmmqOYuyq8SPzya1F0DN04Fa7NWCWa04EkEGj9zoKjVrx5572Gg3PYG2cr4qDmX-qz-Hz-qC_CyoBKw9nS2O-8cZfjVqy5rn_KnEum8fkkAtrT4GaPZiMaZ49xXmtOZ_mXRm3PM35EwFrFFQqgNcvke8uxUig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول لیگ برتر پس از پایان هفته دوم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/682665" target="_blank">📅 22:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682664">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
همتی: نگران تامین کالاهای اساسی و دارو نباشید
🔹
دولت و بانک مرکزی تضمین داده‌اند که این موارد را تامین کنند و حالا هم می‌بینید که در بازار کمبودی در این زمینه وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/682664" target="_blank">📅 22:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682663">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
نیویورک‌تایمز: تهران روی فرسایش آمریکا حساب کرده؛ هر روز ادامه جنگ می‌تواند هزینه بیشتری روی دست واشنگتن بگذارد
🔹
کندشدن روند سقوط ریال و کاهش سرعت تورم، روایت فروپاشی سریع اقتصاد ایران را با تردید مواجه کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/682663" target="_blank">📅 22:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682662">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
عراقچی: تا آخرین نفس و قطره خون‌مان پای منافع ملی می‌ایستیم
وزیر امور خارجه:
🔹
اصل برای وزارت خارجه تحقق منافع ملی مبتنی بر دستورالعمل‌های عالی نظام است و ما تا آخرین نفس و قطره خون‌مان پای منافع ملی می‌ایستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/682662" target="_blank">📅 22:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682661">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cd10c07b.mp4?token=pcBNpevbmTgE0DER7fCt7WHHMsiA9UAsagbo1BHmTqIlENapVB_2M12fRvyh9C-phoGhisYKJHUWEZplskgtSI5NL1urTs4EThPcJqw3G4TpPvjqiDrxbm2eGrd-7w2AFmGT_lMLCtTOuMcD4gnkCo6z9qc8py2HpHSdqhtGbO9SYEj3oQsx1yHhfih3X6lPbuOG3f43kfALLZtpmJfyhs7qs8L3aM5GjdIyuG39cEkZPl___bnIb4HlJ5IkSW46UE9qz6qhFGyjTeA8wahikGaksZuVkpVzvLwlNe64B0tdUYufCtyWqKY2fZby86C_6O1uzvPj52NgOS-Dn0fokzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cd10c07b.mp4?token=pcBNpevbmTgE0DER7fCt7WHHMsiA9UAsagbo1BHmTqIlENapVB_2M12fRvyh9C-phoGhisYKJHUWEZplskgtSI5NL1urTs4EThPcJqw3G4TpPvjqiDrxbm2eGrd-7w2AFmGT_lMLCtTOuMcD4gnkCo6z9qc8py2HpHSdqhtGbO9SYEj3oQsx1yHhfih3X6lPbuOG3f43kfALLZtpmJfyhs7qs8L3aM5GjdIyuG39cEkZPl___bnIb4HlJ5IkSW46UE9qz6qhFGyjTeA8wahikGaksZuVkpVzvLwlNe64B0tdUYufCtyWqKY2fZby86C_6O1uzvPj52NgOS-Dn0fokzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جعبه‌های کاغذی ساده در چین که به کسب‌وکار بسته‌بندی لوکس تبدیل شده
🔹
این جعبه‌ها در چند ثانیه تا می‌شوند و به کیسه هدیه‌ای شیک تبدیل می‌شوند. ساختشان کمتر از ۱ دلار هزینه دارد، اما می‌توانند ۱۰ تا ۲۰ برابر بیشتر فروخته شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/682661" target="_blank">📅 22:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682660">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0026d21b5.mp4?token=QpedyB-q9E1xQD1HaS8iWpYiUJK7Qqq20RGNcZDOIknjYePAQC5VpLwg3gwgVg7G37-BjxbtBwzWYz1cyQ64MhlF1lXfdIzh12-dM7oYMKuKu7-v4kdrUVstUNgmEFtBwCjpt_uZrJUuMwcikljGSaCqOi_A7D7rswGg2mnGBHimJbHhcOdzvcz9VbY7HauBW9_pQDsEb1pV4n_isUpbui35lqi8QGmMF3bm-EECua8hnrOjaqVbc_g6I2SC61KWN1MOwbjhYpsJaO8aV68bM5c_2b4x8yz1rqolETQt26pUn_TvUXi_lAdnhqsGiYKXB5wL7pUFr0Q4mOLPW_c3RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0026d21b5.mp4?token=QpedyB-q9E1xQD1HaS8iWpYiUJK7Qqq20RGNcZDOIknjYePAQC5VpLwg3gwgVg7G37-BjxbtBwzWYz1cyQ64MhlF1lXfdIzh12-dM7oYMKuKu7-v4kdrUVstUNgmEFtBwCjpt_uZrJUuMwcikljGSaCqOi_A7D7rswGg2mnGBHimJbHhcOdzvcz9VbY7HauBW9_pQDsEb1pV4n_isUpbui35lqi8QGmMF3bm-EECua8hnrOjaqVbc_g6I2SC61KWN1MOwbjhYpsJaO8aV68bM5c_2b4x8yz1rqolETQt26pUn_TvUXi_lAdnhqsGiYKXB5wL7pUFr0Q4mOLPW_c3RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: پیشنهاد ایجاد کریدور مالی در بریکس را ارائه کردیم/ باید وابستگی به ارزهای دیگر کاهش یابد   رئیس کل بانک مرکزی:
🔹
اگر بریکس بتواند ایده‌های خود را به مرحله عمل برساند، ظرفیت‌های قابل توجهی خواهد داشت و به آینده آن امیدوارم.
🔹
پیش از جنگ ۱۲ میلیارد دلار…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/682660" target="_blank">📅 22:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682659">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687bb05d6.mp4?token=nq6nN-ZPXs88gMEjGXw343ONFoLyFD6pPp-r5nTH3bUttx4uNsIeCQ_iu02Ulu-eLcX1DjRO0ZTRUhbRROgCq6HAC1c2TaCUtYmB_maaZHLADg5WahEzK7MwXWVNIIO0ojGpdwdsrO1ufqI_X5QS8fqvmHaBkTb7c_FZm-Gu6djPmFvspPxc699MFy6V8h4qpC_tJtP1zCf5IxvESz_yuvDq-C-yVplrdJjTGm1lKV6sf81cTq_piYELdVxpHBJzY6vFpvyWE-JMBUYaG9r9xNYD0gTXXdqy97yknZoBz_qOMVvQ6p50O22YevCb5yJCo8OQss04YDOVGPI-x-igcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687bb05d6.mp4?token=nq6nN-ZPXs88gMEjGXw343ONFoLyFD6pPp-r5nTH3bUttx4uNsIeCQ_iu02Ulu-eLcX1DjRO0ZTRUhbRROgCq6HAC1c2TaCUtYmB_maaZHLADg5WahEzK7MwXWVNIIO0ojGpdwdsrO1ufqI_X5QS8fqvmHaBkTb7c_FZm-Gu6djPmFvspPxc699MFy6V8h4qpC_tJtP1zCf5IxvESz_yuvDq-C-yVplrdJjTGm1lKV6sf81cTq_piYELdVxpHBJzY6vFpvyWE-JMBUYaG9r9xNYD0gTXXdqy97yknZoBz_qOMVvQ6p50O22YevCb5yJCo8OQss04YDOVGPI-x-igcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: پیشنهاد ایجاد کریدور مالی در بریکس را ارائه کردیم/ باید وابستگی به ارزهای دیگر کاهش یابد
رئیس کل بانک مرکزی:
🔹
اگر بریکس بتواند ایده‌های خود را به مرحله عمل برساند، ظرفیت‌های قابل توجهی خواهد داشت و به آینده آن امیدوارم.
🔹
پیش از جنگ ۱۲ میلیارد دلار صادرات به عراق داشتیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/682659" target="_blank">📅 22:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682658">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
مسیر پول در بورس عوض شد
🔹
پول حقیقی‌ها از صندوق‌های درآمد ثابت خارج شد و به سمت صندوق‌های طلا رفت. امروز ۹۶۰ میلیارد تومان از صندوق‌های درآمد ثابت خارج شد، در حالی که صندوق‌های طلا ۹۲۰ میلیارد تومان ورود پول ثبت کردند.
🔹
ارزش معاملات خرد ۳۳ همت بود و با وجود خروج حدود ۲۷ میلیارد تومان پول حقیقی از بازار، ۶۱ درصد نمادها معاملات مثبت داشتند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/682658" target="_blank">📅 22:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682657">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پازوکی، اقتصاددان: اسرائیل و رقبای منطقه‌ای خواستار انزوای ایران هستند
مهدی پازوکی، اقتصاددان در
#گفت‌وگو
با خبرفوری:
🔹
شانس دوبار در خانه ما را زد. یک‌بار پیش از انقلاب که درآمد نفت بالا رفت و شاه با کنارزدن تکنوکرات‌ها، زمینه سقوط خودش را فراهم کرد. یک‌بار هم بعد از انقلاب که برنامه چهارم را کنار زدند.
🔹
در برنامه چهارم، تعامل با جامعه جهانی در چارچوب منافع ملی دیده شده بود، اما هر بار از تعامل حرف زدیم، گفتند وابستگی است. من صراحتاً می‌گویم تعامل اقتصادی ایران با جهان به نفع ملت ایران است.
🔹
اگر انضباط مالی، پولی و اداری را حاکم کنیم و از جوانان تحصیل‌کرده استفاده کنیم، می‌توانیم آقای منطقه شویم؛ نه اینکه نهادهای دولتی محل دفتر و دکان افراد بی‌دانش باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/682657" target="_blank">📅 22:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682656">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17dd06b49a.mp4?token=W1l0FZhBK5cCvVWw0QN8qAHBg7X0BbxNkUad6iLEm8gEcAzxEN5vqKOSKt7S9vs1qMYvoIvCMnIpKkwWJ6xluLT_mT1ehF9h_8Y5KTiMKcE5tr1542iMaR6Bve69ssFZEbrbR7ehSXalBvqOgEmpAw5nG_D4bT7z9CpdXYMLWZtg0EHbV_SXHx6njqbWDYf3J2Q1aky-yMayEPHqI0lx90Uc9ras0O4cx2X3lwUp8U0vJ4-QNKp5rTh4jcwviKhN5KL5DEgABzup8CkCZYQ2J9EhSwtpP91xWvqhyoyNhEIibl7qXkAoBliNi9QJlq44_RDcQCrK81zooKhzQUzHFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17dd06b49a.mp4?token=W1l0FZhBK5cCvVWw0QN8qAHBg7X0BbxNkUad6iLEm8gEcAzxEN5vqKOSKt7S9vs1qMYvoIvCMnIpKkwWJ6xluLT_mT1ehF9h_8Y5KTiMKcE5tr1542iMaR6Bve69ssFZEbrbR7ehSXalBvqOgEmpAw5nG_D4bT7z9CpdXYMLWZtg0EHbV_SXHx6njqbWDYf3J2Q1aky-yMayEPHqI0lx90Uc9ras0O4cx2X3lwUp8U0vJ4-QNKp5rTh4jcwviKhN5KL5DEgABzup8CkCZYQ2J9EhSwtpP91xWvqhyoyNhEIibl7qXkAoBliNi9QJlq44_RDcQCrK81zooKhzQUzHFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: مشکلات بانکی ایران و عراق طی هفته‌های آینده برطرف می‌شود
🔹
عراق صدور ضمانت‌نامه برای پیمانکاران ایرانی را پذیرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/682656" target="_blank">📅 22:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682655">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2770ae392f.mp4?token=Ah5sY2ToZJy27xuV4RFkGhCY3ZM1dL9SSOPS6pyL7oNJwzsahpElKNEY9U57WRtcM92X2HpyFOubrqblVpFHuBq9CNlqEh0VjHp93m0Xu02gndwgRn40Gl5k2t1OO8HybvugRlRPJVXqExu6_seRH4S9OpF2vLNK5Tjn00Yt5D7otLw4DKhB21I-dGzXRUwRv_eA35KND-_5fo9bvLPFKG2o-XbYsKOWfNJOS_tScHh0SzB1R8Aa99-LYc2ZEMuDibeRQDaRzvdggI8iJjHf2-EP73A_ITcHqHZhLE-rhJHiMnVmi79fynaHXJUaG2SPOAoGPH8ZFuXos9qeHrBP0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2770ae392f.mp4?token=Ah5sY2ToZJy27xuV4RFkGhCY3ZM1dL9SSOPS6pyL7oNJwzsahpElKNEY9U57WRtcM92X2HpyFOubrqblVpFHuBq9CNlqEh0VjHp93m0Xu02gndwgRn40Gl5k2t1OO8HybvugRlRPJVXqExu6_seRH4S9OpF2vLNK5Tjn00Yt5D7otLw4DKhB21I-dGzXRUwRv_eA35KND-_5fo9bvLPFKG2o-XbYsKOWfNJOS_tScHh0SzB1R8Aa99-LYc2ZEMuDibeRQDaRzvdggI8iJjHf2-EP73A_ITcHqHZhLE-rhJHiMnVmi79fynaHXJUaG2SPOAoGPH8ZFuXos9qeHrBP0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از لپ‌تاپ دوربین‌دار شیائومی با قابلیت‌های عجیب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/682655" target="_blank">📅 22:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682654">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751a5db559.mp4?token=kdK9_AYN4NS2qCrQHlwrnGlDLOiG3uoncBMu4bZJmJw9cpZqDP3mrftQW4ZojaQCDUv0gzzOXxcpp8ogWbcFjo4_NXzKHMN4tF0ux1gQrNCYoLUe2GIHl_lHxze-9s5qExPrTKOe4EOGlMqN8GsNMQoU8WjPht7lMgHQ6Y2j6j0SySOEWCgbTp6AfosOtWSZsRzX5SfhjnmBrVSG4HndlblZvP2PYxC5Lp_lvehNF5GakEQHvmYfUwvdtNkIckm_rqCJlHouBWSiML-v8CG9mEvFSaGwoLXuRGvDA4HeEot8uTcFev8ZbcohmTnMf4qFBVB0CMELAoOELmWJ2ufYyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751a5db559.mp4?token=kdK9_AYN4NS2qCrQHlwrnGlDLOiG3uoncBMu4bZJmJw9cpZqDP3mrftQW4ZojaQCDUv0gzzOXxcpp8ogWbcFjo4_NXzKHMN4tF0ux1gQrNCYoLUe2GIHl_lHxze-9s5qExPrTKOe4EOGlMqN8GsNMQoU8WjPht7lMgHQ6Y2j6j0SySOEWCgbTp6AfosOtWSZsRzX5SfhjnmBrVSG4HndlblZvP2PYxC5Lp_lvehNF5GakEQHvmYfUwvdtNkIckm_rqCJlHouBWSiML-v8CG9mEvFSaGwoLXuRGvDA4HeEot8uTcFev8ZbcohmTnMf4qFBVB0CMELAoOELmWJ2ufYyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: تاکنون چیزی از پول‌های بلوکه‌شده در راستای تفاهم‌نامه آزاد نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/682654" target="_blank">📅 22:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682653">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6jvkRQ43MdVBvppeEHkRCBlFkdlkcSLm_tVuin9NUBfYmEWM4A-k7TWt3gbYWprVTDhtfxz_GApuQckJs2isKki1XvevQADX3gX9Zjpast67vnEOcr0qvxmgSVJ00DT1yLU5hsvu9Y07R2AEFEuF-kjdEZfPrqJjVXTDizJVgousVZzsCBC_RO2G6FT8eGhxjFYLlghyT7ux6b-IjDm8x4m0XovsjSfpxXaVjILYkRWVtBel0X89jJgi4HIGCOrg_X2cvGtskTqsTTLnkz7npRyb24Cw9G81GUkcZ9udUjBSBmQ_OQ-hJ9_zgYE3yNQYzeTG6oicYCMXOd35Lccmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ مورد از عجیب‌ترین لحظات ترامپ در مورد جنگ ایران | از «ایران توافق کرده» تا «هرمز مال ماست»
🔹
این هفته، دونالد ترامپ، در حالی که جنگ ایران وارد ششمین ماه خود شده، مجموعه‌ای از اظهارات جنجالی و گاه متناقض را مطرح کرده است؛ از تهدید به جنگ با یک کشور دیگر خاورمیانه گرفته تا پیشنهاد تبدیل تنگه هرمز به قلمرو آمریکا و حتی ادعایی که با پیام‌های رسمی دولتش درباره مذاکرات با ایران در تضاد بود. و این تازه تا روز سه‌شنبه ادامه داشته است.
ترجمه گزارش سی‌ان‌ان را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3238948</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/682653" target="_blank">📅 22:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682652">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ترامپ جنایتکار به کانال ۱۲ اسرائیل: من از جزئیات حمله اسرائیل به سوریه مطلع هستم، اما در این مورد صحبت نخواهم کرد
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/682652" target="_blank">📅 22:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682648">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxxqSUG5t4RjwjRvZnBHGCZT26XldzWGHSoL5ph-Nw5dUmUD2GOv0EbKqi2OpFzWpfXOfUqF09IZJdaBzB00u_3w6gSZMLfbaP9A3FugXVrBRh5G2RTXowLb3vYb7BFONSWdbYYnuw3JQXeFqN_jMTRe6hFs7qUNVlDb-kMQQ0PYuyOD3_1MXNB0GpUofe_eIgquy3D8bkmwM6_srFeOETAWDRs-rkDBqCxTJ4YvxoYg_xfMoQVq4eD5pck8mZ8MGrcePhgBHb3IQWc76H-hsc6bJE9lrEDlNggjWIq-d5gS6AAB9ojji6YPPLomriUlGmHXJQbYZrjb6MAk9Rkyeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ietaZ3uqGw9Se-Jk0cYYQn19Lke-3tAykQD4r4dKXiUyXBMfVBsx599HYInufxUsFwx2ogVCaCfQEqiT4p8xCCZzmRCeEZuZEq7Csuy1tc2K6Yjyy8oc4fEhvaion-iFfq-D7rW-i1mOL00IbD2KOdxcSELz64T-3TNIb7W_2hNZsVlsLWppTdc3l4JhFlQOrFjXIqdNSldQeaz-jbDoxaM-2qtXEotWNIMvAzPKAdjtAEKESppbf20ttilRqPLXRZlHuQmqKYSAgkKQVoG7CByRZiQ-4KAnPHo-FtG6N--yCk-lf4dkAZEZlvU_NkVINCYLf10psTT6vCCqnAaNKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b991cf3af0.mp4?token=adR4V_0liKv2GBat-25wREl1q2_Mur9WJomFsFyU2vA0HczRcoZlLSAwLiEN7pSpdndKAf1C15T37PnbPZtJgk3BYnV7_nEfTbRwaT9IIIP0g1no5e-oLsltyd0tiXOAZ1P9Dppyqm5a5Prse3tpnoiboCYtIRYrxoAArAmcsx2cUdYqNiA8QihxcIoklgf4E6hxKgiAt2U392YK4uGpygikJkSdyuk2WaL0TIqNdw76jkOEun15nxofuYUjHdZRNrmeBiAVuXyG7N2h5F7DgAS1ySK7fo_vSpuLyejCvjwP1H9prjAzoRS_zI-5jUp3mzWqXbBTan-c-QhcAhL2Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b991cf3af0.mp4?token=adR4V_0liKv2GBat-25wREl1q2_Mur9WJomFsFyU2vA0HczRcoZlLSAwLiEN7pSpdndKAf1C15T37PnbPZtJgk3BYnV7_nEfTbRwaT9IIIP0g1no5e-oLsltyd0tiXOAZ1P9Dppyqm5a5Prse3tpnoiboCYtIRYrxoAArAmcsx2cUdYqNiA8QihxcIoklgf4E6hxKgiAt2U392YK4uGpygikJkSdyuk2WaL0TIqNdw76jkOEun15nxofuYUjHdZRNrmeBiAVuXyG7N2h5F7DgAS1ySK7fo_vSpuLyejCvjwP1H9prjAzoRS_zI-5jUp3mzWqXbBTan-c-QhcAhL2Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎀
از یک پارچه ساده تا یک کسب‌وکار خانگی
🔹
این بار در
#چرخ_زندگی
رفتیم سراغ یک ایده خلاقانه و کم‌هزینه؛ دوخت کش موهای دست‌دوز.
🔹
با چند وسیله ساده مثل پارچه، کش، نخ و کمی خلاقیت می‌شود محصولی زیبا ساخت و قدم اول یک کسب‌وکار خانگی را برداشت.
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/682648" target="_blank">📅 22:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682647">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
وحشت اسرائیل از حمله پیش دستانه ایران
👇
khabarfoori.com/fa/tiny/news-3238761
🔹
جابه‌جایی ۹ مدیر عالی رتبه در قوه قضائیه
👇
khabarfoori.com/fa/tiny/news-3238863
🔹
حمله پهپادی به کامیون‌های ایرانی در نزدیکی مرز روسیه و بلاروس
👇
khabarfoori.com/fa/tiny/news-3238978
🔹
همسر اکبر عبدی دستور تخریب مزار شوهرش را صادر کرد
👇
khabarfoori.com/fa/tiny/news-3238910
🔹
احتمال حمله آمریکا به ایران در شرایط کنونی چقدر است؟
👇
khabarfoori.com/fa/tiny/news-3238769
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/682647" target="_blank">📅 22:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682646">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goBGpJMI3m4yKkJwX1zQR1x3E9Z58WOhBxtO9QRmRRAND6SrN3kZ2TdwHvUCMRGibZChFZibOW23V8QcBJuwp1P44on9x3kngo45CuXwM9W-_TuZb6ULNnOZlvKNzMGQRNE8uUr5Q2c-0icMf01yj6ugkeBtoZwwgvzkpIcCeouh-wGAYvjQBWRGgyh5i9zcxxu5a_pcQIZ882gJEPk5R1_aDUGF0iWl_hqmEy5hO2ESAOtM4ZSGJcO2ImA03C8VxiGEGsQP5zNVwDkeRtLVpmmwGqkaWLWd7dCIp286KHTodgHQDT2WeHJCB_MhhcvLxJW2Qh_gdJbZvkTmWw363w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دنیا جای ماندن نیست؛ دل‌بستنِ بیش از حد به آن، آرامش را از انسان می‌گیرد
🔹
امام علی(ع) در نهج‌البلاغه یادآوری می‌کند که دنیا برای هیچ‌کس خانه‌ای همیشگی نیست. آنچه می‌ماند، اعمال و انتخاب‌های ماست؛ پس بهتر است دل را به چیزی نبندیم که دیر یا زود باید از آن…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/682646" target="_blank">📅 22:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682645">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4cf96a80.mp4?token=PyBZCNCKakKMMDbIgJWLGHoJk6OfUxfA31ksnAXRc3o5pFYvQcnsiU9dNs2kFB1S5n2X4SkCg6z6gtHtKGlg15ZaOBKV-pSkB-SKX95yujBcTySQz1JzrzCn-yzPCOifOALISRIjL6pHJsqKWPheO3Cp0Q7UFtFJOBLwx28gT3EYcw01R9T4cMcrP-LOUkIoF79xYnsPopw6Ho2DFgSQ01sF5XJybFxIz5ietlUMgINQN1QOuc-zQyu2ENjkJrpN7Sm2OD8AkHvdfkAVqiqktLQ68jX9iyi6pfa2lnJzgFZk5pDUJRPWxl4pTlgxosVt0sbCMfOPLvvCjKAGDmeJWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4cf96a80.mp4?token=PyBZCNCKakKMMDbIgJWLGHoJk6OfUxfA31ksnAXRc3o5pFYvQcnsiU9dNs2kFB1S5n2X4SkCg6z6gtHtKGlg15ZaOBKV-pSkB-SKX95yujBcTySQz1JzrzCn-yzPCOifOALISRIjL6pHJsqKWPheO3Cp0Q7UFtFJOBLwx28gT3EYcw01R9T4cMcrP-LOUkIoF79xYnsPopw6Ho2DFgSQ01sF5XJybFxIz5ietlUMgINQN1QOuc-zQyu2ENjkJrpN7Sm2OD8AkHvdfkAVqiqktLQ68jX9iyi6pfa2lnJzgFZk5pDUJRPWxl4pTlgxosVt0sbCMfOPLvvCjKAGDmeJWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی یک سرک کشیدن، به شلیک مرگبار ختم شد
🔹
یک لحظه کنجکاوی، صحنه‌ای غیرمنتظره و پرتنش را رقم می‌زند؛ اتفاقی که ترامپ حتی کنترلش را از دست می‌دهد....
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/682645" target="_blank">📅 22:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682643">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSXlG6GW5xu_aAYQhYlM_HraVSotG6W4W1dsIw_QFF_M64w9-ry_NBtv8ja2FPtUwZpg2XINkkuOmC9V14EEwo45fOT8JsRAM-9jnxpMS8S2eOmPdZGtjpTL_pndlcZ65f1h-Yh4T68YDM7Jd5HpAaOMKyUupBw2NN7Fg-3KT07AEOc9btyRKoA8-nI7CEZzFhMooi7SAewV4PhQGnCzk---MrSHefCXnpov_N1FVzSG9FT_E0k1kgNrz7jSdscFxlW4OkLyfg8KDIgNPhdKPGSVkaDBWHZT5e1EVAeDnx8tyHECx_wnV1o64Mn-C08rCC19-KEXdP5kOICKWm-QVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a1b218a4.mp4?token=cuxCWocOMP3Nnb3XNzqQKhhoshk8ydaFHEMCAf4U0Z1uqbAdnikRXVCB7Pzyv2JoxpAnANjSimC4WoVBn4s7YCYYOG-BavjcaXptCnalokY71D3R0EndoHKmn1UujUZ7iJt4am_gqh5qAUC1J0Q0mlPIBF9mxubLfVDo0wdMx7fLrNM0yidA6QPxA0wN0NkSScnBg-PP5by6ARZHE3HtrEfLpMTOHWW36Ad5vSxFEL619jQBIUXlIzO2KJo8Crs93QM6tGzK7d_7XsbsNVjpINr6rKn7ax96AtEPyVyJzAedDmMlUCLxR72SFi-KoaYd-wBMGtSXa-LUAXRUuBpzsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a1b218a4.mp4?token=cuxCWocOMP3Nnb3XNzqQKhhoshk8ydaFHEMCAf4U0Z1uqbAdnikRXVCB7Pzyv2JoxpAnANjSimC4WoVBn4s7YCYYOG-BavjcaXptCnalokY71D3R0EndoHKmn1UujUZ7iJt4am_gqh5qAUC1J0Q0mlPIBF9mxubLfVDo0wdMx7fLrNM0yidA6QPxA0wN0NkSScnBg-PP5by6ARZHE3HtrEfLpMTOHWW36Ad5vSxFEL619jQBIUXlIzO2KJo8Crs93QM6tGzK7d_7XsbsNVjpINr6rKn7ax96AtEPyVyJzAedDmMlUCLxR72SFi-KoaYd-wBMGtSXa-LUAXRUuBpzsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عصاره همه سخنرانی‌های ترامپ در مورد ایران
🔹
سفارت ایران در غنا با انتشار ویدیویی طنزآمیز، تناقض‌گویی‌های پی‌درپی ترامپ درباره ایران را به تصویر کشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/682643" target="_blank">📅 21:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682642">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAutonovin.ir</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6jrLDkuej53adJrwhzPamEed_32A3aVDXC7u-GZa76Q_7xzB37-6ERl0fIMiJgdYA_POTKjIgcdVWbJZF-VQggjYF6LJbrJ92v-5TBEnaSuIUIFu2q7NiYo1lLMHZ-4QlXKpgu0uKK6gaKmXtpN_ZYub9tw5p1QAy6U9vN6NQ9AlPD05ScMuVs85IhDXSKxslENUYKXOZJW_k2ikiYWIZVPLkcLFVIX9Hyub0iM3mMA0P9-E273TbBjB5ewnHA4HQJ0TsUKsy0j6UyS6fsDKpR-1DMD9uKmI1KmKAWduqHRsq_YElQkBcVNoaZCmpKrTqo9ZH8uqMbKMV8UFGGfQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آخرین فرصت خرید خودروهای وارداتی اعلام شد
🔹
متقاضیان تا پایان روز دوشنبه ۲ شهریور ۱۴۰۵ فرصت دارند حساب خود را نزد بانک‌های اعلام‌شده در پلتفرم اتونوین وکالتی کرده و ۵۰۰ میلیون تومان مسدود کنند.
🔹
همچنین تا پایان روز سه‌شنبه ۳ شهریور ۱۴۰۵ امکان ثبت‌نام و انتخاب خودروی موردنظر در این طرح فراهم است.
🚘
برندهای عرضه‌شده در این طرح:
Toyota | Nissan | Mazda | Volkswagen | Volvo | BYD
🌐
ثبت‌نام و انتخاب خودرو:
Autonovin.ir</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/682642" target="_blank">📅 21:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682641">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-lTFi7EfbVsX3BpP1hTQ_oiVO54WheRUO7SrkSQc1X_JRZgu42apsQ-RhDTbzbUa3oVVzprmKrnAsbRK6ZwAsBRyVwZkbPfzVbEu0leAGyBsmAPVdSPvkFi97uLJ-8S6PcO1qcSQZGD9D42Ou5JF4HzJMeGw4ZGgCIZUgnuiJylK-IDGiOk0jp5Cl0NkM7axe9g3PTLz8EQowGmsnXXtT3TNW3kDaruKGjaY_Cs7e_pqPopRkaIfk2cYfmt8Ys-TmTZjRXeZ-EMFNnc2123EEhIxdkcqIPp7RpwqRsjsnEywVgI0_2MzqjKlCFFzlICh0J51BRX_J-yLJk2YMkiRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرعامل فولاد خوزستان: بازگشت به تولید در کمتر از ۲۵ روز
🔹
امین ابراهیمی، مدیرعامل فولاد خوزستان، با اشاره به حضور کارکنان و بازنشستگان از نخستین ساعات حادثه گفت: «اقدامات فوری کارکنان در ساعات نخست، از جمله ایمن‌سازی تأسیسات و قطع جریان گاز، از بروز خسارت‌های بیشتر جلوگیری کرد.» این حضور خودجوش نشان داد سرمایه انسانی این مجموعه، مهم‌ترین دارایی آن در لحظات بحرانی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/682641" target="_blank">📅 21:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682640">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQ0xwKXIp-eLJMAPOrqk9HzuE0Q3FvkfcBI6gMGuY4JujCJT1Jb4d9h5ChkNb4LzYFm5JIquIIx8exPxmUQ06Qv3WgsQCxSj03JfNcgfzALbZPooZpX1oeKb2zQw3kf8pm_TVqEi_PrdUGL8A9e-eC89oh-ZDKcGK8e9YfH5C3DmmYVZqAHPBfuDKcDWc-gck7QzwRe0GosFjfSP122GwrDDMhu_64DM9rjXTDjY5M34gvbr065d5lw4CzBXks40vYc1HKY5GghDDt8E8tmn3zJwTHicRC_RakAanPv8vaz4mOzpUDS7EkJWRxEJ55wjHswmbLKkIoTQaEc8-SAmTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روز کنکور نزدیکه، این چند نکته ساده رو از شب قبل جدی بگیرید تا با آرامش و انرژی بیشتری سر جلسه حاضر بشید
🔹
کنکوری‌های عزیز؛ انشاءالله برین و با کلی خبرهای خوب برگردین؛ خدا شاهد تمام تلاش و زحماتتون هست و رهاتون نمی‌کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/682640" target="_blank">📅 21:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682639">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkD8U28s3gR891eauOwdQY2-YMfKcwn8OmG1TtgsS3xh3EESfYG9EMP7eMYjzenCpkWkWO-1zSfrszFa5qswwL7YoMZAuhrvQMcVqdTQmkWeANjaCEuVFiFtYh8ugAknkNd_sGFoEVrWL919bGrsjq2in3H_e4s9ucOyG33qYNUXkGZ28pmcF6MNxc3UFMu5I0QnNhQZthN4AtlWoDm5m8zF1I6UyLsh2sHKxTENKugueQHlregW_LS_-jdanx_OXN_N2LPH4P6QW7Qctp6U1GgcVlDco1LpsdkHtzw08SIKHE8UhtWr90P5DcKEOxAxYqFSujgVOj6PNofeTIfMDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل چهارم پرسپولیس به استقلال خوزستان توسط شهرآبادی در دقیقۀ ۹۳
🔹
پرسپولیس ۴ _ ۱ استقلال خوزستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/682639" target="_blank">📅 21:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682638">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ارتش تروریست آمریکا از ادامه تعرض به کشتی‌های مربوط به ایران خبر داد
سازمان تروریستی ستاد فرماندهی مرکزی ایالات متحده دقایقی پیش در خصوص محاصره دریایی علیه ایران ادعا کرده است:
🔹
از زمان آغاز تحریم‌ها علیه ایران، ۶۵ کشتی تجاری را منحرف، ۳ کشتی را از کار انداخته و ۲ کشتی را توقیف کرده‌ایم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/682638" target="_blank">📅 21:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682637">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
اذعان وقیحانه نفتالی بنت بر تداوم مسیر جنایت و اشغالگری: تا خلع سلاح کامل حماس از «خط زرد» عقب‌نشینی نمی‌کنیم
نخست‌وزیر پیشین رژیم صهیونیستی:
🔹
تا زمانی که حماس کاملاً خلع سلاح نشود، حتی یک میلی‌متر از «خط زرد» عقب‌نشینی نخواهیم کرد.
🔹
آزادی عمل امنیتی خود را در سراسر غزه حفظ می‌کنیم.
🔹
قطر و ترکیه حماس را تقویت می‌کنند؛ باید مصر جایگزین آن‌ها در مدیریت غزه شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/682637" target="_blank">📅 21:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682636">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
زمین‌لرزه‌ای به بزرگی ۴.۲ ریشتر، شامگاه امروز حوالی شهرستان گیلان‌غرب در مرز استان‌های کرمانشاه و ایلام را لرزاند
🔹
تاکنون گزارشی از خسارت‌های احتمالی این زمین‌لرزه اعلام نشده است.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/682636" target="_blank">📅 21:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682635">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21674bfd7.mp4?token=JZcq84SogyS9wwyFUIdmKjWwKh-K3kQJ2ahKOXQ8icIeBBzImblHcuuIx7pPNrOcgtzunBgxJPqTjFRAA5AyCe4OoQEHJARnUatXcarVhHvmye_50ZyNT1-kbHvePars-llesTHghWjSM3sH7CeknHPKeCqotTBa4rvS9fej110VFnk0ZKVuGhKLS78VDN09yvMNVriA7huGwaNI2yJ9-r7ox9U1u2OF5ywBUs6NppmpFGgKAtvyx6hEXQyTlulgxtu_3GOnvD5S0AdYwHtNIfEX76dshBljMF556m-P2yaeglccsrEbwZ88F_8TWvqXGzoG8D7h_jEIT0zP3gomcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21674bfd7.mp4?token=JZcq84SogyS9wwyFUIdmKjWwKh-K3kQJ2ahKOXQ8icIeBBzImblHcuuIx7pPNrOcgtzunBgxJPqTjFRAA5AyCe4OoQEHJARnUatXcarVhHvmye_50ZyNT1-kbHvePars-llesTHghWjSM3sH7CeknHPKeCqotTBa4rvS9fej110VFnk0ZKVuGhKLS78VDN09yvMNVriA7huGwaNI2yJ9-r7ox9U1u2OF5ywBUs6NppmpFGgKAtvyx6hEXQyTlulgxtu_3GOnvD5S0AdYwHtNIfEX76dshBljMF556m-P2yaeglccsrEbwZ88F_8TWvqXGzoG8D7h_jEIT0zP3gomcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یحیی سریع: نیروهای مسلح ۹ عملیات موشکی و پهپادی علیه تأسیسات نفتی عربستان انجام دادند
سخنگوی نیروهای مسلح یمن:
🔹
از ۲۰ ژوئیه تا ۱۹ اوت، نیروهای یمن با هدف‌گیری مستقیم ۸ نفتکش (۵ مورد در دریای سرخ و ۳ مورد در خلیج عدن و دریای عرب) و مجبور کردن ۴۸ نفتکش دیگر به تغییر مسیر و بازگشت، عملاً محاصره دریایی عربستان را اجرایی کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/682635" target="_blank">📅 21:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682634">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
پزشکیان: مذاکره به معنای تسلیم نیست؛ ملت ایران و نیروهای مسلح با ایستادگی در برابر حملات، دنیا را شگفت‌زده کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/682634" target="_blank">📅 21:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682633">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e5061375.mp4?token=D1Ohnc1Dmv4ImSJtys_sYWpscwF_CaUjmqLdJ2IGVoE6GTv_QuHP6SvYazfoQkCYl0UbrSP-8Uk_vqrY8C8yjMx6fMaSsDdzYh7DRjHYpT2oELMXRlfoUQNrvtuE05ZsfLrOHM_A3nxUXVdCGEwTKkKfGuCy4GN7IB_Win6qm6dOWxwz1BUwMH03hqQX-ZCgSjdqU4n5yfulTuEuBnmqK1nQMM08p5UZZBdZ0Qk6OY56TfBc1IJhHGljzJj06VQYeXDe1R9b7rpBVpOhAoaX8RZVVKTui1d9NusvXpPE1S2Ow6scl0GCKsLqaSfR5MWJvJ9esxpRuVDWTeBmvEeugg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e5061375.mp4?token=D1Ohnc1Dmv4ImSJtys_sYWpscwF_CaUjmqLdJ2IGVoE6GTv_QuHP6SvYazfoQkCYl0UbrSP-8Uk_vqrY8C8yjMx6fMaSsDdzYh7DRjHYpT2oELMXRlfoUQNrvtuE05ZsfLrOHM_A3nxUXVdCGEwTKkKfGuCy4GN7IB_Win6qm6dOWxwz1BUwMH03hqQX-ZCgSjdqU4n5yfulTuEuBnmqK1nQMM08p5UZZBdZ0Qk6OY56TfBc1IJhHGljzJj06VQYeXDe1R9b7rpBVpOhAoaX8RZVVKTui1d9NusvXpPE1S2Ow6scl0GCKsLqaSfR5MWJvJ9esxpRuVDWTeBmvEeugg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول استقلال خوزستان به پرسپولیس در دقیقۀ ۶۴
🔹
پرسپولیس ۳ _ ۱ استقلال خوزستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/682633" target="_blank">📅 21:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682632">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfnNJQoDVuW7kpgjbzVdAqf5EKj6HfEevoRRlfgC5LStgRsxR9hu-OXfGGLZay4d3x3nYKknQMvlURAdOXafMB2QVenjXXtfIw1lQmLlNHqVBUiqXaVvEw9hJRMCptVMczEV_-FWEba_surnNS4jpOhBT8_XWbaOdi7Vwu8PkZ4x0FoSUxYwWlzjaCO1sPMLN1Opmp4yheuvUuXq8wi2H8LjkmEYu6VR6bXOSpLwPMRTlPJ4uP4JKjaLVE0leacVGK4hLkmo1hIergsqgQB8l4WtYOMn4pz8eNHosFJGqSB7SRcPl_8Ffcd8Urbnz3IoyRiZa4FORB-iKe2SgVMfjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمسخر رویای ترامپ درباره تنگه هرمز توسط استاد دانشگاه استنفورد
مایکل مک‌فال سفیر پیشین آمریکا در روسیه در واکنش به رویاپردازی‌های ترامپ و تغییر نام تنگه هرمز روی نقشه به عنوان یکی از دارایی‌های آمریکا:
🔹
این دیگر واقعاً دیوانه‌وار است!
🔹
ما دیگر کشوری جدی نیستیم؛ چه رسد به اینکه قدرتی بزرگ و مورد احترام در جهان باشیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/682632" target="_blank">📅 21:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682631">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83e3a6112e.mp4?token=SkTU7H-NIID6aWzUSVg24xFO9-nEOUQIBEoOu0AijPB2lEqZN-5mPh-X-ytDuXWyOtKwsljVLKC51sdXMewZn8QTlpHxwdSDKZKvoUs-fiFqoz5Z4I-GLfTwPq3fAwB1Foa9gip4JRL90ch1jr0YX-JI3O7CUNsWAKj8Yi-0Z3p7ozhtZpML6Ruj7RIy9smjsubRB2SzbA2Ors6r3W8kkXEZsLzitiu9kVLDHm2GKsrztUpkF8JTc1JuAT95b8vOCjJvPk0gFmVrL9WQRP7Tim2YMF3g9sB6IzNmOGqvsaSGfi95SB0fQGVMHat_wVC9V78V40JDJaNxjG2F-aI37YsJwHQjC6sK4o8ewnX7_zkxpO_IdAd9wDkWpmNsrAsW3GEpbt8l-Q3PGOPwHs7zeChbtASmO4eQbd9U81J290tuuiaYPhwPHGASyOjO5u9AM15lKyYJH7RPXPktNeleKIbinl0gbsWvsmer_935CywBWoDHy_ZNeMEi2nx0R2Z2cfaK518FVLhiP2JlWbQXc7NRefzbEWOvmtugpt57csnLAZu94KYhXhWYnGPXe6HTgyZT3MUhqdw4HPkJSq-6269jSTUUP77AybhSp7SLTswqOVIA1RgPFBZB4qXpyEq9sf7rLh1p6klAMi2uMugZKCzTvbI5pg1KJXbouNBX244" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83e3a6112e.mp4?token=SkTU7H-NIID6aWzUSVg24xFO9-nEOUQIBEoOu0AijPB2lEqZN-5mPh-X-ytDuXWyOtKwsljVLKC51sdXMewZn8QTlpHxwdSDKZKvoUs-fiFqoz5Z4I-GLfTwPq3fAwB1Foa9gip4JRL90ch1jr0YX-JI3O7CUNsWAKj8Yi-0Z3p7ozhtZpML6Ruj7RIy9smjsubRB2SzbA2Ors6r3W8kkXEZsLzitiu9kVLDHm2GKsrztUpkF8JTc1JuAT95b8vOCjJvPk0gFmVrL9WQRP7Tim2YMF3g9sB6IzNmOGqvsaSGfi95SB0fQGVMHat_wVC9V78V40JDJaNxjG2F-aI37YsJwHQjC6sK4o8ewnX7_zkxpO_IdAd9wDkWpmNsrAsW3GEpbt8l-Q3PGOPwHs7zeChbtASmO4eQbd9U81J290tuuiaYPhwPHGASyOjO5u9AM15lKyYJH7RPXPktNeleKIbinl0gbsWvsmer_935CywBWoDHy_ZNeMEi2nx0R2Z2cfaK518FVLhiP2JlWbQXc7NRefzbEWOvmtugpt57csnLAZu94KYhXhWYnGPXe6HTgyZT3MUhqdw4HPkJSq-6269jSTUUP77AybhSp7SLTswqOVIA1RgPFBZB4qXpyEq9sf7rLh1p6klAMi2uMugZKCzTvbI5pg1KJXbouNBX244" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توصیه پدرانه رهبر شهید به جوانان و نوجوانان کشور: از کنکور نترسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/682631" target="_blank">📅 21:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682630">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
پاکستان کاردار آمریکا را احضار کرد
🔹
وزارت امور خارجه پاکستان در اقدامی دیپلماتیک، کاردار سفارت آمریکا در اسلام‌آباد را برای ابلاغ اعتراض رسمی دولت این کشور به اظهارات مقامات آمریکایی فراخواند.
🔹
این احضار در پی توصیف «جیمز وکر»، سفیر آمریکا در هند، صورت گرفت که در اظهاراتی جنجالی، منطقه کشمیر را «بخشی از خاک هند» خوانده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/682630" target="_blank">📅 21:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682629">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxZMQbAdrjedR0wHsFrm-Y8AHgMFj9Kr1WKZfM-On0L3D9KxfzEAuqWQwnaal_CqL0Stj-rnbXmsEoWzMrHGoPQnFxn2gJPkEUB4Crtt8OXXfkFYJFKenuKsvSh-XfHidd5JhPyzzojAkhDbZfv-IK3ulglF2maK8RXmGv0SkL0bwcOvrQktxCtEKf-ZrHLlQhCoxcnKgHI5ElLRJsAC9MwQK0Jehi3Qd3dOfUXjveqU0JCLEh0zLvFsAFGjPH9naw1mNCT7lYb7s69pAYbDvhk2t9QlB-6eevS1tOgMV-q1ajdP8qBwz00hKPHYxqJHMjVy_jIuuvRiUMU-uJQRdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس معناداری که قاليباف منتشر کرد
🔹
رئیس مجلس با انتشار تصویری در اکانت خود به زیاده‌خواهی آمریکایی‌ها در خلیج فارس واکنش نشان داد.
🔹
این تصویر که قابی از نقشه خلیج‌فارس و تنگه هرمز را نشان می‌دهد، به‌نوعی بیانگر تسلط ایرانی‌ها بر تنگۀ هرمز و خلیج‌فارس است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/682629" target="_blank">📅 21:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682628">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ادعای فرستادهٔ ترامپ در امور سوریه: دیروز یک قدم با درگیری ترکیه و اسرائیل فاصله داشتیم!  توماس باراک، نمایندهٔ ویژهٔ رئیس‌جمهور آمریکا در امور سوریه:
🔹
ما دیروز تنها یک قدم با رویارویی نظامی مستقیم میان ترکیه و اسرائیل فاصله داشتیم. حملهٔ هوایی اسرائیل…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/682628" target="_blank">📅 21:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682627">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRDcBGnqkSgBv5tFHdraDDIfwgcjLokrvZd2QcN_GMP4ued3L1v5HOireifcBViC5mtzubZIDlz61GRLaj42-PLJdhXKo5RK0kfRc3tIivHu4ZwZ8TcltcTIotjAGC18Ue8J1JfWGEmZQ1MI3NwzTjI_4CTFofv02c4o8pIP9IECI_5TmmuTIkD5mRjSYbvg-uDxcASxDPnwwqHjwkqkgXtXbQVaXHmUsAI30iLtFJMjcFsqryv75U8EHlIwlBws8pUkivvwcQI8AUCYv-ttgJ1ut2saf7XP_nDxTXvtbcmfNLOCYAul07-wFARv-2KM4qDy0g_ptTWC11LpoezIGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷۳ سال پس از یک خیانت به مردم / پشت پرده حادثه ای که باعث جنگ ایران و آمریکا تا امروز شد
🔹
چرا ۲۸ مرداد رخ داد؟ آیا این حادثه ضروری بود یا امکانی؟ آیا اگر مصدق و شاه اقدامات مرتکب شده را مرتکب نمی شدند، این کودتا رخ می داد؟
داستان روزی را بخوانید که آمریکا را از چشم ایرانی‌ها انداخت
👇
khabarfoori.com/fa/tiny/news-3238697</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/682627" target="_blank">📅 21:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682626">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1473988dd2.mp4?token=c6js8eLl_b1eCPaOAHpZE9Ica9KFISYC1yuyd8oSwAbaFQkLGD-4pQitNmD9349FNqMZDkxLGMG8_tFSrlYM-FAaiNv3n5AuuqL8epX4Z-c0duf-WIT4ambj3ny_uEePamZnTGWq61RydrOAcoAyKpuExQKOXtTUE_svjocRxI2ehthOuqn_HtjVsqMJ1P7P7H7_iBjRf9YCAr30BX21aqjaRMjDelmLV3P7BznNBxrij7L3vfgcX-hZXiOgZUNGElA6z-oYyACTEKmp05OjFNGDqXBel-lTlRvJjoAfvXQOyh5nEewyfXUHiUWY9HzMrM9veNqXyU54kfQlECH5kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1473988dd2.mp4?token=c6js8eLl_b1eCPaOAHpZE9Ica9KFISYC1yuyd8oSwAbaFQkLGD-4pQitNmD9349FNqMZDkxLGMG8_tFSrlYM-FAaiNv3n5AuuqL8epX4Z-c0duf-WIT4ambj3ny_uEePamZnTGWq61RydrOAcoAyKpuExQKOXtTUE_svjocRxI2ehthOuqn_HtjVsqMJ1P7P7H7_iBjRf9YCAr30BX21aqjaRMjDelmLV3P7BznNBxrij7L3vfgcX-hZXiOgZUNGElA6z-oYyACTEKmp05OjFNGDqXBel-lTlRvJjoAfvXQOyh5nEewyfXUHiUWY9HzMrM9veNqXyU54kfQlECH5kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم پرسپولیس توسط سرگیف
🔹
پرسپولیس ۳ _ ۰ استقلال خوزستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/682626" target="_blank">📅 21:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682625">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اقدام غیراخلاقی برخی شرکت‌های پیمانکاری: مزایای کارگران را به عنوان سود خودشان دریافت می‌کنند
هاشم خنفری پورجعفری، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
بین یک میلیون و ۳۰۰ هزار تا یک میلیون و ۵۰۰ هزار نیروی شرکتی پیمانکاری در کشور داریم که بخشی از آنها از طریق شرکت‌های پیمانکاری با دستگاه‌های دولتی همکاری می‌کنند و ساماندهی وضعیت آنها در حال پیگیری است.
🔹
شرکت‌های پیمانکاری حداقل حدود ۱۰ درصد از مزایای نیروهای شرکتی را به عنوان سود خود دریافت می‌کنند و این مبلغ می‌تواند به جای واسطه‌ها به رفاهیات و مزایای کارگران اختصاص پیدا کند.
🔹
در برخی قراردادها پیمانکار برای اینکه در مناقصه برنده شود قیمت پایین‌تری پیشنهاد می‌دهد و بعد مجبور می‌شود از مزایا، اضافه‌کاری و رفاهیات کارگران کم کند تا قرارداد برایش صرفه اقتصادی داشته باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/682625" target="_blank">📅 21:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682624">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d27502e1.mp4?token=IYnRWi1ZZxNRo8aNtirULQzCKyXmGIfco9BArnmEpkiHoKNcB8r0QoMOP3gfS9QyOu3I6lzxVuH8Om_g2aTbFqfbOrTA_WqiH7F2ys3_kCwMCMaET22fo8SbMkNDl3wH3ExCBtUrJ1GI17A-J5ByHxffHAZ53eD08VdHDvRwevDZGXdE5Zrx2GEAAo9Ez1Xf7LngMXgCP4JHxTOV9oHpgmAs9LfCE8RJPc9ivr87T1cP_noRIbPbFqzUtxy62hoEjmT8EverUpo-iFTj48LHSLpLugvK3Ziy-TgHd5tURXnylhmBteK6m_SwzApUOnB-IUYz1fYlY5dGwp-idr9Nng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d27502e1.mp4?token=IYnRWi1ZZxNRo8aNtirULQzCKyXmGIfco9BArnmEpkiHoKNcB8r0QoMOP3gfS9QyOu3I6lzxVuH8Om_g2aTbFqfbOrTA_WqiH7F2ys3_kCwMCMaET22fo8SbMkNDl3wH3ExCBtUrJ1GI17A-J5ByHxffHAZ53eD08VdHDvRwevDZGXdE5Zrx2GEAAo9Ez1Xf7LngMXgCP4JHxTOV9oHpgmAs9LfCE8RJPc9ivr87T1cP_noRIbPbFqzUtxy62hoEjmT8EverUpo-iFTj48LHSLpLugvK3Ziy-TgHd5tURXnylhmBteK6m_SwzApUOnB-IUYz1fYlY5dGwp-idr9Nng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط مارشال‌های آمریکا از بالکن به پایین حین تمرین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/682624" target="_blank">📅 20:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682622">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baXxBzg8LtfYFVJ0m9CdaKa60LfgCQZeIXLl6F4CjdSe-LPUOObS6vGXqa50MMEyA9g6M33kd703NLwYDsPh3SUkwmSU8CTbrvy1x2KGYxzKUGpXF67TE7tyhvtvz9QhkHN5uRdEjmYsiLnejkgBHGfOB1Y4kV_FKwdlmT4HOR-QL0LrDgL4-CEIPH55fuxSOgJyLBqCOeF5cxPVdBGxofLkto4iRkGaLJ6DOuHXYeD1sTxYymRHYoUmL3uuMYF22WgRy5gOBoW8LyzM-fFOjhqRNUTgPZ7aKaf-qaMnkRxajlFTWlFkd0QK4wAlaCWbyfq256O5Mh_lCwj8Hhud3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ‌عجیب ارزش بیت‌کوین
🔹
فقط در ۵۰ دقیقه  ۴,۴۰۰ دلار جهش کرد و برای اولین بار در بیش از ۲ ماه گذشته به سقف ۶۹,۷۰۰ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/682622" target="_blank">📅 20:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682620">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4752033f1.mp4?token=E546ABjEc_ZGR6LLB4FEwHQG5rGCzAk4NWKS9SsrH3xlCluBABX3DfF6LMbjRwjsItJkHTq8UqMDpblkbwuzftqti-xvNti3lrKAciIq8jZpDdB2VFXgZzNgIErYPFchVC7aTi7FUcB1EyqkdPMrhFuAM9rJ8PgldY9covCTpxy2-wH58urS7bGTAMc3GPbFg1rk3XLON060IhSiWxPOSOzrvD_XYmTrhJ-XGAUaS_jrqvGGMNkvZhXP_PWxCWkhvrqT_Rj1GU_1-krOZNblgNCdeyAvAqCO7PiV-63dHQTSoyPDtZqJ2PMNzDioLdORbPoqQ5pkChRlFjmRSOfonA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4752033f1.mp4?token=E546ABjEc_ZGR6LLB4FEwHQG5rGCzAk4NWKS9SsrH3xlCluBABX3DfF6LMbjRwjsItJkHTq8UqMDpblkbwuzftqti-xvNti3lrKAciIq8jZpDdB2VFXgZzNgIErYPFchVC7aTi7FUcB1EyqkdPMrhFuAM9rJ8PgldY9covCTpxy2-wH58urS7bGTAMc3GPbFg1rk3XLON060IhSiWxPOSOzrvD_XYmTrhJ-XGAUaS_jrqvGGMNkvZhXP_PWxCWkhvrqT_Rj1GU_1-krOZNblgNCdeyAvAqCO7PiV-63dHQTSoyPDtZqJ2PMNzDioLdORbPoqQ5pkChRlFjmRSOfonA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم پرسپولیس به استقلال خوزستان توسط علیپور در دقیقۀ ۲۰
🔹
پرسپولیس ۲ - ۰ استقلال خوزستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/682620" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682619">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryjjUPqw-VKFeLulTvmXf6XXvroQPrUh_3xvQAtXKDbNTvxVBBCcD2OA90E5ydfklets81EgVPn-tsRzn9WUuqVPrpaf3FCpxtQ5jOEJoq25SndZa4CJv9YleziSngJOshoVJNwmZLkzpRNvUDmxUr8R1BOpWUz-odOG5l-VZsQSfILS7slqcKSdvyOjdpABZlPneO9gc7HC4iurgySUIx-l_UfAxGDE36HgAxTcQEDQvP53UO-FbIMg8_ShynJWcD4fgIZE87eNDGq8XpzC4A6t-hVfRXQSYjoDbGPOAsIXTyNGK-P6flVaSZwJejHQQwGeuhRw6nOi2X9nQtPLsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«گنجینه نوین» اقتصادنوین؛ اولین تلاقی هنر و اقتصاد در ۵۰ سال اخیر
🔹
همزمان با بیست‌وپنجمین سالگرد تأسیس بانک اقتصادنوین، نمایشگاه «گنجینه نوین؛ گزیده آثار گالری نوین» در موزه هنرهای معاصر تهران برگزار شد.
🔹
در سال ۱۳۷۶ خرید آثار هنری توسط وزارتخانه‌ها و بانک‌ها ممنوع بود و این ممنوعیت در سال ۱۳۷۷ با تلاش‌های انجام‌شده برداشته شد.
🔹
در اوایل دهه ۸۰، بانک اقتصادنوین که نخستین بانک خصوصی کشور بود، اولین مجموعه‌ای بود که به شکل جدی به خرید و حمایت از آثار هنری روی آورد⁦.⁩
🔹
در این مراسم با حضور یدالله کابلی، چهره ماندگار خط شکسته ایران، فریدون فرمان‌آرا و علی موسوی‌زاده، قائم‌مقام بانک اقتصادنوین، از اثر خوشنویسی کابلی با عنوان «با شما نوینیم» رونمایی شد؛ اثری که یدالله کابلی آن را برای بانک اقتصادنوین خلق کرده است⁦.⁩
⁦
اطلاعات بیشتر:
https://www.enbank.ir/s/mfa9py</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/682619" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682618">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9956a46472.mp4?token=BaaI3VohrflnTr3DpUCMvWnebbkkVmqpYunLIz5xsRVd45oZdnJGMna_pDJwjYLStwI5EOH-Ubl25KBew9latQH03-_fK9ARjnFGFmAKNQlhIbsSDQtXogXs3dy1biifcPrtTfkDGSEl0Cb2mucXpuv5henElmPlI69IEq5F8vpxRVgcZESUXsbuGM2BA2r10JOdUQjG8JBL9JkZ4eovIsbVGNpJ-8cLLeu0H0VpKK2kxcEdM9MgqWtbdjjaEmiofdrmkoO-kDuPr6ZZ5u4srmOMDr2krM09RpXs9P9DazAWXE-mLAD-nWlcsEAdaLnc9oHUONvFxbnpGYDKDz6SkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9956a46472.mp4?token=BaaI3VohrflnTr3DpUCMvWnebbkkVmqpYunLIz5xsRVd45oZdnJGMna_pDJwjYLStwI5EOH-Ubl25KBew9latQH03-_fK9ARjnFGFmAKNQlhIbsSDQtXogXs3dy1biifcPrtTfkDGSEl0Cb2mucXpuv5henElmPlI69IEq5F8vpxRVgcZESUXsbuGM2BA2r10JOdUQjG8JBL9JkZ4eovIsbVGNpJ-8cLLeu0H0VpKK2kxcEdM9MgqWtbdjjaEmiofdrmkoO-kDuPr6ZZ5u4srmOMDr2krM09RpXs9P9DazAWXE-mLAD-nWlcsEAdaLnc9oHUONvFxbnpGYDKDz6SkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیدمحمد خاتمی: ما در خطیرترین موقعیتی هستیم که جامعه و اسلام و ایران با آن روبرو بوده و ریشه‌اش در انقلاب اسلامی است
🔹
انقلاب اسلامی چه کسی آن را قبول داشته باشد چه نداشته باشد، چه بگوییم به اهدافش رسیده یا نرسیده، چه بگوییم از جهت خودش انحرافاتی پیدا کرده یا نکرده بزرگترین حادثه‌ای بود که در قرن گذشته در دنیا رخ داد و نه تنها وضع ایران و معادلاتی که در منطقه بود، بلکه معادلات جهان را عوض کرد.
🔹
مهمترین جلوه آن جنگ تحمیلی بود که آن را ناکام کردیم ولی دشمنی‌ها برداشته نشد و تحریم‌ها و توطئه‌ها ادامه پیدا کرد تا جنگ ۱۲ روزه و جنگ رمضان رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/682618" target="_blank">📅 20:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682617">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قالیباف: هدف آمریکا چپاول کشورهای خلیج فارس است.
🔹
مصر از برقراری تماس‌های دیپلماتیک با ایران برای کاهش تنش خبر داد
🔹
ارتش رژیم جنایتکار صهیونیستی مدعی شهید شدن چند فرمانده حماس در حمله هوایی به غزه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/682617" target="_blank">📅 20:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682616">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df2fc0de27.mp4?token=LiMQWfNUolZ6Z1ffrW7gTQ9mPLJXIdb8lnG7UywRN5nZm9Pe8qD0uhEtaoFV6CUDN3UP11Kw0kB-VBKhW_f-_BgiJEpQlpYKa7hLZmgSt2KMAznnT6Sywemo_99IKi-sW1zilMcMyTDzn09yZiBkyDhGvXX1SarNkZ02HqNzl-mOO9ICp6qpaQZraTtpwhrwUsQpZ26t9SqCQYErnYIelrfFqVc_exhwr7iFV4SJ5E5FZnWJzJPJr3NLkG5_LGMevT0rPMiMJW-ImgTBk928BwwgdZaly9584uKQOA5s-lzLH1wQv3uK-Kvt3_JwtR66MaG4y8uZORw40dEUyPzsmIqSkxwDMx9Hbq6ePiVO9cw-ReyQ7kwqoYEOuJ6g3nX284Y8noVs-LoQmVVgAhpmuUaU6ulO0VHQsNOlTob16rgUPqUUCkVgyhYRdXNRts6mHQwQjlb89dtHV_YKp77Znzosfnab2oaoZaO9sumkL7q8e0zC44Q_otOLEenMcyf-1aUTli0mo1oAZi_kJge9Vt4r13jIvxfsQT_8MkzWcLAy9oxR651HHzoPIs351cANSirLuTSHTTh_ldAboA2qMZNuzV-FvSeEH62lkKvfrFao9Gtz3bFS-07B_WI1IGzsDvlNiwGKUpOJmmScSUvEWYNQvqHb4kAgAZUZrOKdgLo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df2fc0de27.mp4?token=LiMQWfNUolZ6Z1ffrW7gTQ9mPLJXIdb8lnG7UywRN5nZm9Pe8qD0uhEtaoFV6CUDN3UP11Kw0kB-VBKhW_f-_BgiJEpQlpYKa7hLZmgSt2KMAznnT6Sywemo_99IKi-sW1zilMcMyTDzn09yZiBkyDhGvXX1SarNkZ02HqNzl-mOO9ICp6qpaQZraTtpwhrwUsQpZ26t9SqCQYErnYIelrfFqVc_exhwr7iFV4SJ5E5FZnWJzJPJr3NLkG5_LGMevT0rPMiMJW-ImgTBk928BwwgdZaly9584uKQOA5s-lzLH1wQv3uK-Kvt3_JwtR66MaG4y8uZORw40dEUyPzsmIqSkxwDMx9Hbq6ePiVO9cw-ReyQ7kwqoYEOuJ6g3nX284Y8noVs-LoQmVVgAhpmuUaU6ulO0VHQsNOlTob16rgUPqUUCkVgyhYRdXNRts6mHQwQjlb89dtHV_YKp77Znzosfnab2oaoZaO9sumkL7q8e0zC44Q_otOLEenMcyf-1aUTli0mo1oAZi_kJge9Vt4r13jIvxfsQT_8MkzWcLAy9oxR651HHzoPIs351cANSirLuTSHTTh_ldAboA2qMZNuzV-FvSeEH62lkKvfrFao9Gtz3bFS-07B_WI1IGzsDvlNiwGKUpOJmmScSUvEWYNQvqHb4kAgAZUZrOKdgLo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیت‌الله اعرافی: ملت ما پای انتقام خون امام شهید ایستاده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/682616" target="_blank">📅 20:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682615">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHSeiO1cq7eNelX6nBDvmskxa8bPqUbdH4pannIyftP-dV9ldiGWljd1D2nooDFQCXIzTSpICUa0ZRtX2j6nNGyC4Q5wqHJacc32aZDzRqDFATlRhNIdJPJuRbrKWV69Ny2NES8JSDgfP-lpLMZgoZo88Dup5F9WZGMA7u8PAwHo-MijcbErmXMNHVO08qPvdfozdDWCeS0eX3SFLHjtTllXR4LzFR9BMzTBNcNstoamfPc7GhRMENv5Ovl57LCdLbB3QwtWam8v-OZTcVm2PMG4JDtvY0UTr-19jHB41a37iZLALPUbil6kLBAlLANUta7XqmnwiPC2XJdh7CpuLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزهای حساس پیش‌رو؛ راهبرد جدید ایران چیست؟
🔹
به نظر می‌رسد رویارویی ترکیبی میان ایران و محور مقاومت از یک سو، و آمریکا و رژیم اسرائیل از سوی دیگر، نه تنها اجتناب‌ناپذیر، که در آستانه وقوع است.
تحلیلی دراین‌باره را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3238994</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/682615" target="_blank">📅 20:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682614">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2978f5f65.mp4?token=rzHjBGvR-TcYa2ApRfbRHN3FXXGRthKhTKWDrd76td3VOsgNJUfjOHjz7EnAKSR-BvDzVhAPZcAexcmzzrgmkN1S79XCQYe11X0pzLp0-wyRF18WCNhIXHl6FdNMbCrVpheYYIcjSaHoZJOi5lIKrJAz3DUFZS5NC7uut0B7bS7bcS7fkId07xry-_uHrLEx7eCNlobPrRiyUou72Ep2Ooas7D3NXUsVAQ4iRfeFXGDTRu74SdibQoRW7cRepbJf6kAJpWFv0_VGBTrYUvthtEKwYvLSaLOiZkuUOT3NUXRqIVmxFBOx_MOyPaun2z64NwV7WEnoS_VKsj0IxJgA3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2978f5f65.mp4?token=rzHjBGvR-TcYa2ApRfbRHN3FXXGRthKhTKWDrd76td3VOsgNJUfjOHjz7EnAKSR-BvDzVhAPZcAexcmzzrgmkN1S79XCQYe11X0pzLp0-wyRF18WCNhIXHl6FdNMbCrVpheYYIcjSaHoZJOi5lIKrJAz3DUFZS5NC7uut0B7bS7bcS7fkId07xry-_uHrLEx7eCNlobPrRiyUou72Ep2Ooas7D3NXUsVAQ4iRfeFXGDTRu74SdibQoRW7cRepbJf6kAJpWFv0_VGBTrYUvthtEKwYvLSaLOiZkuUOT3NUXRqIVmxFBOx_MOyPaun2z64NwV7WEnoS_VKsj0IxJgA3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتابک، وزیر صمت: در دی ماه پارسال دو روز پس از جلسه رئیس‌جمهور با اصناف، بازار آرام شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/682614" target="_blank">📅 20:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682613">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
نرخ بیکاری پایتخت به ۱۰.۶ درصد رسید
🔹
بررسی داده‌های بهار ۱۴۰۵ در مقایسه با مدت مشابه سال گذشته نشان می‌دهد نرخ بیکاری در سه استان بیش از ۴ واحد درصد افزایش یافته است.
🔹
خراسان رضوی با رشد ۴.۸ واحد درصدی در صدر قرار دارد و پس از آن هرمزگان با ۴.۱ واحد درصد ایستاده است. در این میان، تهران نیز با افزایش ۴.۲ واحد درصدی نرخ بیکاری، یکی از مهم‌ترین تغییرات را ثبت کرده است.
🔹
نرخ بیکاری پایتخت از حدود ۶ درصد در بهار سال گذشته به ۱۰.۶ درصد در بهار امسال رسیده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/682613" target="_blank">📅 20:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682612">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf711e498.mp4?token=gu828OLsjCe_F39aXNQzaTJFEGtkfv9zQl7ueAZR_6C7gmEH5_IY2PwtaYAnuK-UEfVlhoACnJrCjJ6HZDFJKpxAZP9ybnJ_HcsljFo9S7yXh8GIcKqE2uwk8DveYsEDawOpx0vs4W5TWQzunyRR-kcvYmxelzYIVPoLdPrid1f9PnhqmQScmIZ3E47wNAMZDq3NTHHQQEGAzwjetvabRonDhXP2QjhjnW3V5-_hkL9MpwTWsa76UK5lvf9LP_StlPbgQ-sYGv9yyPQ4k__PbSMfyn4HgZSA7mU4gQm75uMsvUKr3EKDnUNx6Koz6jZ-ueRhPo1UpzcTgBGUwq67Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf711e498.mp4?token=gu828OLsjCe_F39aXNQzaTJFEGtkfv9zQl7ueAZR_6C7gmEH5_IY2PwtaYAnuK-UEfVlhoACnJrCjJ6HZDFJKpxAZP9ybnJ_HcsljFo9S7yXh8GIcKqE2uwk8DveYsEDawOpx0vs4W5TWQzunyRR-kcvYmxelzYIVPoLdPrid1f9PnhqmQScmIZ3E47wNAMZDq3NTHHQQEGAzwjetvabRonDhXP2QjhjnW3V5-_hkL9MpwTWsa76UK5lvf9LP_StlPbgQ-sYGv9yyPQ4k__PbSMfyn4HgZSA7mU4gQm75uMsvUKr3EKDnUNx6Koz6jZ-ueRhPo1UpzcTgBGUwq67Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاوت نوستالژیک و معروف تیتراژ سریال یوسف پیامبر توسط استاد کریم منصوری در محفل اربعین قرآنی‌ترین رهبر جهان اسلام در مشهد مقدس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/682612" target="_blank">📅 20:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682611">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a325a235c2.mp4?token=iS-mCArSZO44ZMoBe5Yby9gjaJB9XH8OSNm9J5SG_Wb3-7T5nhiYJbKrHLH6dGIigw4gd_KmFo6igd-acFy5MBCSyIpr3LA9q6kmMNniec-_qmaY4YzUfbO7uGoyZndopTs-xWo6FhnO2vO_A_D8S-2UAoZPjB7OqKYwcDhxMJ6tauwwXp24PHLUAfVu8xQtLQWFNOpbrbWWZD6AoJkzGTJqcfqmBdvKs5VCKyute1QxzGpBUvynJTH7Le5ZapDz8k44Fzan2M3i16B5_R40Kvi9yFS45XagtVWHjGwSYtrnvjXbMbbkATBIG65Mqm62iBzjI0qIc87UKqy6XOpuKHOL3dLStMIvMh0r2wdKAkAb61imhDHuGgE1r0bc-sZ7qqjjq6_1e_5C3BT7EbY4EwSWxZRSqgeH9HxAuKCMrEMBJNeHl3xWmNNcpCGr_EDl9k5fuxkGtNgaevSQstdqEHazsnjcN9xkomoPQVd02gt3NHG6znFjWxPIM_JrYWPzcH4Y_U55x9CIK0lCPx9Sc6WaNY-svhef6izk2Zz3EbPyR5M6e_9jL0rnnqY7vgt_Vh2Ac28-XXdL9WYme_QqQtZFLBxEqISTmdkYLghiNtWKuAx2y_y2DBeIOLICQrL36jfggqn4cz1_lcySvwDM-FTxjGhKVkRNsZP7mWgjisk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a325a235c2.mp4?token=iS-mCArSZO44ZMoBe5Yby9gjaJB9XH8OSNm9J5SG_Wb3-7T5nhiYJbKrHLH6dGIigw4gd_KmFo6igd-acFy5MBCSyIpr3LA9q6kmMNniec-_qmaY4YzUfbO7uGoyZndopTs-xWo6FhnO2vO_A_D8S-2UAoZPjB7OqKYwcDhxMJ6tauwwXp24PHLUAfVu8xQtLQWFNOpbrbWWZD6AoJkzGTJqcfqmBdvKs5VCKyute1QxzGpBUvynJTH7Le5ZapDz8k44Fzan2M3i16B5_R40Kvi9yFS45XagtVWHjGwSYtrnvjXbMbbkATBIG65Mqm62iBzjI0qIc87UKqy6XOpuKHOL3dLStMIvMh0r2wdKAkAb61imhDHuGgE1r0bc-sZ7qqjjq6_1e_5C3BT7EbY4EwSWxZRSqgeH9HxAuKCMrEMBJNeHl3xWmNNcpCGr_EDl9k5fuxkGtNgaevSQstdqEHazsnjcN9xkomoPQVd02gt3NHG6znFjWxPIM_JrYWPzcH4Y_U55x9CIK0lCPx9Sc6WaNY-svhef6izk2Zz3EbPyR5M6e_9jL0rnnqY7vgt_Vh2Ac28-XXdL9WYme_QqQtZFLBxEqISTmdkYLghiNtWKuAx2y_y2DBeIOLICQrL36jfggqn4cz1_lcySvwDM-FTxjGhKVkRNsZP7mWgjisk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک راه ساده و اثرگذار برای موفقیت مالی
🔹
فکر می‌کنی برای ثروتمند شدن، فقط باید پول بیشتری داشته باشی؟ شاید نه… شاید چیزی که از پول هم باارزش‌تره، سال‌هایی باشه که داری از دست میدی.
یک عدد ساده می‌تونه نشونت بده چرا شروع کردنِ زودتر، گاهی تفاوت بین سرمایه داشتن و ثروت ساختنه.
🔹
در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/682611" target="_blank">📅 20:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682610">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/182eb48064.mp4?token=Pe0QPUJVNLObMFf_zudRJEpl98BP88Rcb7Xy5BkMZimDRhfqlJ1nHUzUIKqNLRyBXaBpevp-KR4-kaV3zobHUh8azglo6-tuB_WFjqunaK_FVwj35Irgnv2TH8ikWdyd_PhU977X3nr7b8uJ9iQS0RV8FsnXQcVHd0Eo_4oyze9pkAT0YnkLNy0zGZuBXF2DaLqo730y-Xzd-XNefsJC-Cnd1NrSUFL79AfmQeQx6D1hr-Hw_qpHa2ypuHvx8sMnyjnxJrTyFC0DDM7y39ivk4iCOuRX7mn1AAXb0IpY0pWqQqfhpO34A7Dg90kcc-Iswu8QI1JhL-ZogeatFlilRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/182eb48064.mp4?token=Pe0QPUJVNLObMFf_zudRJEpl98BP88Rcb7Xy5BkMZimDRhfqlJ1nHUzUIKqNLRyBXaBpevp-KR4-kaV3zobHUh8azglo6-tuB_WFjqunaK_FVwj35Irgnv2TH8ikWdyd_PhU977X3nr7b8uJ9iQS0RV8FsnXQcVHd0Eo_4oyze9pkAT0YnkLNy0zGZuBXF2DaLqo730y-Xzd-XNefsJC-Cnd1NrSUFL79AfmQeQx6D1hr-Hw_qpHa2ypuHvx8sMnyjnxJrTyFC0DDM7y39ivk4iCOuRX7mn1AAXb0IpY0pWqQqfhpO34A7Dg90kcc-Iswu8QI1JhL-ZogeatFlilRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چنگال فقط برای غذا نیست! این ترفندها رو ببین
🤯
🍴
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/682610" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682609">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
شبکه عبری: ایرانی‌ها درس سختی به ترامپ دادند
🔹
«گیل تماری»، تحلیلگر روابط خارجی شبکه ۱۳ اسرائیل در برنامه‌ای اعلام کرد ۶۰ روز از زمانی که ترامپ خودکار معروف خود را برداشت و یادداشت تفاهم با ایران را در کمال افتخار و غرور امضا کرد، می‌گذرد و این به مثابه نشانه آغاز مرحله‌ای از مذاکرات برای حل نهایی برنامه هسته‌ای، موشک‌های بالستیک و نیروهای همسوی با ایران در منطقه بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/682609" target="_blank">📅 20:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682608">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be64cd3c87.mp4?token=qGXct9cT04XDULYpY9Fp5rZdFyGsAggJRFY5j1noaDQHna9fPb36_HRRLT1dPUpC8pXt0sq7PmhM1Qopsp22gU7OCy4xRqvzlk_lU5XYFHITOAkIz4wRq_bThT_7tbeet37twlppboeG5s9EOp7v3VBvP3ubDKUCssir6HnSso1W2ewOJB6_ttwV1cTX_bQs0mKl73CrjmcTrmKlzUhv9xw_Z1ngy9qIun4ZjhiMTNlkoSx1tWlCK_-tH82y_p8TL6uTTuRsXvCqT3x8zEijBBkefWEb23smY3v2P9vsU_BcNSpMmvwwU3dj1Y77ESpti0fifXXpQgd_e-NBLVDgWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be64cd3c87.mp4?token=qGXct9cT04XDULYpY9Fp5rZdFyGsAggJRFY5j1noaDQHna9fPb36_HRRLT1dPUpC8pXt0sq7PmhM1Qopsp22gU7OCy4xRqvzlk_lU5XYFHITOAkIz4wRq_bThT_7tbeet37twlppboeG5s9EOp7v3VBvP3ubDKUCssir6HnSso1W2ewOJB6_ttwV1cTX_bQs0mKl73CrjmcTrmKlzUhv9xw_Z1ngy9qIun4ZjhiMTNlkoSx1tWlCK_-tH82y_p8TL6uTTuRsXvCqT3x8zEijBBkefWEb23smY3v2P9vsU_BcNSpMmvwwU3dj1Y77ESpti0fifXXpQgd_e-NBLVDgWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر صمت: رئیس‌جمهور تکلیف کردند که برق صنایع قطع نشود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/682608" target="_blank">📅 19:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682607">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc02b7aa5.mp4?token=KNWn_cUbc0uBHYyWt5uOTkgMSQ0XYeLmUqsyeYATq1U0am9fD_VQBqMb8flLfrva7BdkFr01srigVz_5xPdBgRO7fTIAK5Lw7nHKExVGTA_3TRpIO4tKJeQHihCgLH89g_cqPl02tc1wm6bfoWzYcSqOQviVZ9NG3Fb5lbEu-K5PixMBvQgEkN-Ov6QrCF761k_Kzj0fdxlIVdn7AN9mmqj-NNP4MAVzJtdngsEsGdmdFnsT_7CeWWRVGN4Rhv8s_gA2w8vUl2s-7MRbRJT9Z8nwLOA_ICwyNmeLzRoVO4-mEzBofUF4vqT_Q1Vl6aIXUJqAUFYJMXCVnVBPdD4rjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc02b7aa5.mp4?token=KNWn_cUbc0uBHYyWt5uOTkgMSQ0XYeLmUqsyeYATq1U0am9fD_VQBqMb8flLfrva7BdkFr01srigVz_5xPdBgRO7fTIAK5Lw7nHKExVGTA_3TRpIO4tKJeQHihCgLH89g_cqPl02tc1wm6bfoWzYcSqOQviVZ9NG3Fb5lbEu-K5PixMBvQgEkN-Ov6QrCF761k_Kzj0fdxlIVdn7AN9mmqj-NNP4MAVzJtdngsEsGdmdFnsT_7CeWWRVGN4Rhv8s_gA2w8vUl2s-7MRbRJT9Z8nwLOA_ICwyNmeLzRoVO4-mEzBofUF4vqT_Q1Vl6aIXUJqAUFYJMXCVnVBPdD4rjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول پرسپولیس به استقلال خوزستان توسط محمد خدابنده‌لو
🔹
پرسپولیس۱ _ ۰ استقلال خوزستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/682607" target="_blank">📅 19:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682606">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keRF6AU0nUms0uF5NiB1ebG9owV_1BNociDw8cIcnd2g7ccJxYWwQrKevOpVnzPCMOR9d2uI8OOOhrcYne7niBbdffl18gjjVPvda-s1FuBHa9dLmIrpq9Bri8UVrYYXsloPydwmikdRDgiYtjN8qvqpBkjdqUaFDe1pS9bIBslY4MQsTl3BTDVrr1rlafgDMaPrPoj82aMrx4aLWPL5yOrtE1xp6TDGBwwHkVZnrNxKORp0iCGZASo_Om1soTba_BqZVnFQnIbYGcB3J1fmup99hD2RPLO_F-kJSsvLhP6S3Izv6WAcx95wnEDKnTjueYNUxei8pQvbjmKvsQoMig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نظرسنجی‌های آمریکا علیه جنگ ایران متحد شدند
🔹
به‌گزارش پایگاه نظرسنجی‌های معتبر، ۱۰ مؤسسه سرشناس در بازه تیر تا مرداد ۱۴۰۵ افکار عمومی آمریکا را درباره جنگ با ایران سنجیده‌اند.
آخرین نظرسنجی هر مؤسسه به تفکیک:
🔹
ایپسوس (رویترز) – ۱۴ تا ۱۷ مرداد: ۳۴ درصد حمایت در برابر ۶۱ درصد مخالفت (اختلاف منفی ۲۷ درصد)
🔹
آر‌ام‌جی ریسرچ (نیوز سرویس ناپولیتن) – ۵ تا ۶ مرداد: ۴۰ درصد حمایت در برابر ۴۹ درصد مخالفت (منفی ۹ درصد)
🔹
دانشگاه کوئینیپیاک – ۱ تا ۵ مرداد: ۳۴ درصد حمایت در برابر ۶۰ درصد مخالفت (منفی ۲۶ درصد)
🔹
گزارش‌های راسموسن – ۱ تا ۶ مرداد: ۳۵ درصد حمایت در برابر ۵۴ درصد مخالفت (منفی ۱۹ درصد)
🔹
ای‌پی نورک – ۱ تا ۵ مرداد: ۳۳ درصد حمایت در برابر ۶۴ درصد مخالفت (منفی ۳۱ درصد)
🔹
گروه استراتژی جهانی / جی‌بی‌ای‌او (پیمایشگر) – ۱ تا ۵ مرداد: ۴۱ درصد حمایت در برابر ۵۲ درصد مخالفت (منفی ۱۱ درصد)
🔹
یوگاو (سی‌بی‌اس نیوز) – ۳۱ تیر تا ۲ مرداد: ۳۹ درصد حمایت در برابر ۶۱ درصد مخالفت (منفی ۲۲ درصد)/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/682606" target="_blank">📅 19:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682605">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ebbb18e20.mp4?token=OUdLLIy8twkH_GUK84Q16akaP6NkCo3m6UQv6HE6cf2ojocksC9pgrTcUG3AKB3EQI9hmpGDVb9XwmsmH0xYImxBeszviAXhVmj-R5Q2_Q0tkQNNkIAYrUmfCiaZ4MIOWIvQi4XICE0nLIxzgcnQdi65HMeBRx6mahmHGmjqbqKj2zEwqKJtevdP5NdH9SSYlQZtec2GH7MYwGjEfyeK7qUTTqZvFmshIbuYGMY-wESPhKbixEQOaAGuXeEC51AfPXaColPmJlb5GMV80X9EHBBCdGSJMWNzVa8dbCdrKlK13CocIPZ7G2TB0zvIqbbKnuMmKF-G4SEq0p9Vwv9ZaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ebbb18e20.mp4?token=OUdLLIy8twkH_GUK84Q16akaP6NkCo3m6UQv6HE6cf2ojocksC9pgrTcUG3AKB3EQI9hmpGDVb9XwmsmH0xYImxBeszviAXhVmj-R5Q2_Q0tkQNNkIAYrUmfCiaZ4MIOWIvQi4XICE0nLIxzgcnQdi65HMeBRx6mahmHGmjqbqKj2zEwqKJtevdP5NdH9SSYlQZtec2GH7MYwGjEfyeK7qUTTqZvFmshIbuYGMY-wESPhKbixEQOaAGuXeEC51AfPXaColPmJlb5GMV80X9EHBBCdGSJMWNzVa8dbCdrKlK13CocIPZ7G2TB0zvIqbbKnuMmKF-G4SEq0p9Vwv9ZaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر صمت: رئیس‌جمهور تکلیف کردند که برق صنایع قطع نشود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/682605" target="_blank">📅 19:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682604">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
پولیتیکو: در حالی که واشنگتن منتظر تسلیم تهران است، مقام‌های پیشین و کارشناسان آمریکایی معتقدند ایران برای حفظ مواضع خود در مذاکرات، در برابر فشار اقتصادی مقاومت خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/682604" target="_blank">📅 19:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682603">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d693137e12.mp4?token=U_tIAJofyok2NqQhsM7FnB8E2eS6MCwnTx_dPgsY6An7qE2VpWw0OBPeeCvnLZu3Cg_S_WRovDKv7ik2uRHlFe-CXf9_eCHuW1OEmKvZVsa5HyPi03_RJpvc6bijsBj6sIf0ECv_mUUK_G2mDuWesaPSJPa2OLGTojUSuExEfp0fSI2roankRKc-LKAVhyHxDAcPg9TMJxktvRm6AhKG3UNROmIsHG_gefdxj6pi1KDR7hK9vqL5nKv6Rmq7YqXOFKc22LBoYSPgY_ulXabmK6Qcftx6SmCzZ15tVZtPLEb9uzrImyTG-X2XrunumTBlqja9Krrr8tp6PjiEG2tSfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d693137e12.mp4?token=U_tIAJofyok2NqQhsM7FnB8E2eS6MCwnTx_dPgsY6An7qE2VpWw0OBPeeCvnLZu3Cg_S_WRovDKv7ik2uRHlFe-CXf9_eCHuW1OEmKvZVsa5HyPi03_RJpvc6bijsBj6sIf0ECv_mUUK_G2mDuWesaPSJPa2OLGTojUSuExEfp0fSI2roankRKc-LKAVhyHxDAcPg9TMJxktvRm6AhKG3UNROmIsHG_gefdxj6pi1KDR7hK9vqL5nKv6Rmq7YqXOFKc22LBoYSPgY_ulXabmK6Qcftx6SmCzZ15tVZtPLEb9uzrImyTG-X2XrunumTBlqja9Krrr8tp6PjiEG2tSfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: ایران نمی‌تواند سلاح هسته‌ای داشته باشد. می‌دانید چرا؟ چون از آن استفاده خواهد کرد و ما اجازه نمی‌دهیم از آن استفاده کنند  ترامپ:
🔹
مردم در حال پیدا کردن جایگزین‌هایی برای تنگه هرمز هستند. می‌دانید جایگزین‌ها کجاست: تگزاس، آلاسکا، لوئیزیانا.…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/682603" target="_blank">📅 19:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682602">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ترامپ متوهم ادعا کرد ایالات متحده «مالک» تنگه هرمز است #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/682602" target="_blank">📅 19:40 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
