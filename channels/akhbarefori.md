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
<img src="https://cdn4.telesco.pe/file/Zeyo_gw63NrJL-D2cnB-jjsLj0E_jYIiqwWYjV1n2lYABGDW4rHIMGYl9qsKaEcqQ_25sGlbMBvx0oVl5lpN70s3vg4bJrW2XNS4vk5wOYYo28qhH9mPx8JqkKchdvmZiF82rL1QzTpnDB-ISjmLBWEklv-DTHowhV-boUEo9VoDV6gq9n_ONI15HgudInbpRALQT3Aa9W8RV0hu3cUx8alCePVOphzIcPCMVK42ppU4Rss0V-MD5MCCFRu-lg2fYiOTbHnbTZS5MZAxHs6yuL2NFk-Ab7mysuOHa7dejp0NFyWjJxC2CzsEgzmljgxNGLN35Q0R1VYiWyORMqNVEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 18:00:25</div>
<hr>

<div class="tg-post" id="msg-671788">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVjguHimMcARc9pOs3mNt0LxBcTgI3hb1M2cW__HkAo7wF9iDd3o9U4KJ4yXSiYFdteR8nHCgB5dYcESkLxrqtAQue0y2QUdzBkszHfrERZ16vHnhlTIZjs7pYBso7uvBNUWS27FxpWhT7am8LmFaVOBfy9uOXyXF58Yb7UtBlV2e4aq9k4KfR-kISHvE7BIpBCZEKo9P63pkAl5st5azoDjMzWqZj4NWDmAAxCPagmapOeb0HkymrRuIm9JWVgjVe41PRyIyZSTZgPfjHODzeUZ7Co5V4-5csg6PCE6nHpNhFxyiMmQqH-kuqS8iZ_iO-08lF7uOnkQnMSZIQn0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مه‌لقا ملاح؛ مادر محیط زیست ایران
🔹
مه‌لقا ملاح، ۱۰۴ سال زندگی کرد و بیش از ۶۰ سال برای نجات طبیعت ایران جنگید. او آن‌قدر به باورهایش پایبند بود که گفته می‌شود در شش دهه فعالیتش حتی یک گرم زباله از خانه‌اش بیرون نگذاشت و از بطری‌های پلاستیکی یک‌بارمصرف…</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/akhbarefori/671788" target="_blank">📅 18:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671787">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a5942b565.mp4?token=eTP1geWcFpPZ0Tdo4uM3772TvUc_tzUx_9cg9BWI3vO7LlqU2olWF3R2Ic8V4TKNf8m-uWSko6dXMFYX_LT7G-b4yYSGSmmY7kE8s5sqGORExTeNzcohMGuUA97QzFgU0RueKZEe37JHmx8ISqEjcuOir_WlHEaMCIvvpVuD0M5RFiKqr9KP6gd_zKJqDbh7JKcYmLNVxkrTvyxehHVnpKiWq6xGmIsyDWrAqUBocJSbDyOMNs4hXPDeftoEd8WLq06tfpp5lmISacYZV0wMkDdsFE3NJeey4ABpC5M-xWcjc-TIZhLTogNfnVqilIAJMblQuldHmbmeifUXCzEcqwfQi1203z5fIuQ1Z4G0bW3dr1jtKt6RqEGpw3YNyXluytedYlWuRPdQOi3SM_loeeFKlWN0OXWXyf7huDO_yezAttrL9EstJtSqiw9RiRhkn8Gi1SxNYEG_L5hTz8zkz3ZGI5X849UmYZmovuf8wd1WG6SXywqhlX5grK4IW7IWzFZqKdjT0Sda6pmj_MXLzSdvDRhm6bUu4gPZtkECiB38GCw2WkAEbtaEw9njaEG7YRfaz_7KpKx3_NOkHdLUrIVEOk_tu4lJRRjKzievtFZL5AwL-tG3-lOY-3-bDlKzbE590fxAw1qzBKxkVRc11G7OF5vtjXuylhdZ4nVgPTE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a5942b565.mp4?token=eTP1geWcFpPZ0Tdo4uM3772TvUc_tzUx_9cg9BWI3vO7LlqU2olWF3R2Ic8V4TKNf8m-uWSko6dXMFYX_LT7G-b4yYSGSmmY7kE8s5sqGORExTeNzcohMGuUA97QzFgU0RueKZEe37JHmx8ISqEjcuOir_WlHEaMCIvvpVuD0M5RFiKqr9KP6gd_zKJqDbh7JKcYmLNVxkrTvyxehHVnpKiWq6xGmIsyDWrAqUBocJSbDyOMNs4hXPDeftoEd8WLq06tfpp5lmISacYZV0wMkDdsFE3NJeey4ABpC5M-xWcjc-TIZhLTogNfnVqilIAJMblQuldHmbmeifUXCzEcqwfQi1203z5fIuQ1Z4G0bW3dr1jtKt6RqEGpw3YNyXluytedYlWuRPdQOi3SM_loeeFKlWN0OXWXyf7huDO_yezAttrL9EstJtSqiw9RiRhkn8Gi1SxNYEG_L5hTz8zkz3ZGI5X849UmYZmovuf8wd1WG6SXywqhlX5grK4IW7IWzFZqKdjT0Sda6pmj_MXLzSdvDRhm6bUu4gPZtkECiB38GCw2WkAEbtaEw9njaEG7YRfaz_7KpKx3_NOkHdLUrIVEOk_tu4lJRRjKzievtFZL5AwL-tG3-lOY-3-bDlKzbE590fxAw1qzBKxkVRc11G7OF5vtjXuylhdZ4nVgPTE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
این روزها با قطعی‌های برق، داشتن یک چراغ‌قوه معمولی کافی نیست!
🔦
چراغ قوه دستی ۸ کاره LED Torch
هم چراغ‌قوه است، هم پاوربانک، هم ابزار نجات!
✅
نور LED پرقدرت
🔋
قابلیت شارژ با USB + استفاده به‌عنوان پاوربانک
🧲
مگنت قوی برای اتصال به سطوح فلزی
🔨
چکش شیشه‌شکن اضطراری
🔪
تیغ برش کمربند ایمنی
🚨
چراغ هشدار برای مواقع اضطراری
🏕
مناسب قطعی برق، خودرو، سفر، کمپینگ و نگهداری در منزل
❌
قیمت قبل: ۱,۴۹۸,۰۰۰ تومان
🔥
قیمت ویژه: فقط ۹۹۸,۰۰۰ تومان
🚚
ارسال به سراسر کشور
💳
پرداخت درب منزل
👇
قبل از قطعی بعدی برق، این ابزار کاربردی را تهیه کنید.
https://memarket24.ir/product/brief/30291/180124/</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/akhbarefori/671787" target="_blank">📅 17:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671786">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a755c6a7f.mp4?token=i6r4hN32hMbw7m6cjItq13CFx8qH5BwHTteMnspliRuO8b3XUr9TDFc7n1kLHN-UmNffNJabaf6ZD4fsf0qX81_SehGfq6T9raqETrNFUCNzdRTjmSGOrzKWp7BvObEAzREesw_hJIMoEovFZVc35IAnrtVvsip8JcRFDp2jmSMF_McDfjKZMyXWacZSKPuiBX6ZHtVX46_0SBe_Z75uBzk7wlUT5JSEjnzmNb2Dqbylf-pTv47rqKrETDWTrSpIAmi6FCzHQnwLad46idvR_gyfaa7P0hE2YeI81BbZiAO_CxmGU87FXh858yZd_eW1boybeoyeMqlqhz23vhtsQFbGSn8ygczf31eBQEdW331_YFX8MAtoN5MLP3t9AiD36we291yFNG4shd7VJpeFt9jKEEku2bvnbwmJnw_EhNRaVkGl615XhScN4Yr3fS6RRuF4pcRwQD8fQBGkLTCc7i98HMpuE2P-OIvltU3pkt5uVamazeKjIvMl6CRHW8BgJ-hH6KWUc1A_e90weTGQP8MQkNguFXUHabJOunKNOPeVUO_UGhh9RErI1P1d0Jr3XCIPF38lE7Qq9mtjrkK49vVFaXjkIpL0Sbt4qX0vBa8o0pRP9YOktnmgniufeuXfnouD62HzeITDcwQLNGft85i9xr2q8g6gJDSp9zzOhYk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a755c6a7f.mp4?token=i6r4hN32hMbw7m6cjItq13CFx8qH5BwHTteMnspliRuO8b3XUr9TDFc7n1kLHN-UmNffNJabaf6ZD4fsf0qX81_SehGfq6T9raqETrNFUCNzdRTjmSGOrzKWp7BvObEAzREesw_hJIMoEovFZVc35IAnrtVvsip8JcRFDp2jmSMF_McDfjKZMyXWacZSKPuiBX6ZHtVX46_0SBe_Z75uBzk7wlUT5JSEjnzmNb2Dqbylf-pTv47rqKrETDWTrSpIAmi6FCzHQnwLad46idvR_gyfaa7P0hE2YeI81BbZiAO_CxmGU87FXh858yZd_eW1boybeoyeMqlqhz23vhtsQFbGSn8ygczf31eBQEdW331_YFX8MAtoN5MLP3t9AiD36we291yFNG4shd7VJpeFt9jKEEku2bvnbwmJnw_EhNRaVkGl615XhScN4Yr3fS6RRuF4pcRwQD8fQBGkLTCc7i98HMpuE2P-OIvltU3pkt5uVamazeKjIvMl6CRHW8BgJ-hH6KWUc1A_e90weTGQP8MQkNguFXUHabJOunKNOPeVUO_UGhh9RErI1P1d0Jr3XCIPF38lE7Qq9mtjrkK49vVFaXjkIpL0Sbt4qX0vBa8o0pRP9YOktnmgniufeuXfnouD62HzeITDcwQLNGft85i9xr2q8g6gJDSp9zzOhYk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ببینید؛ انیمیشن ترامپ و عربستان!
🔹
رویترز: عربستان سعودی به ایالات متحده اجازه داده است از یک پایگاه هوایی در فاصله حدود ۷۰ کیلومتری مکه در جنگ علیه ایران استفاده کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/akhbarefori/671786" target="_blank">📅 17:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671785">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
حفاظت امنیتی نتانیاهو به دلیل وحشت از ایران  مادام‌العمر شد!
🔹
کابینه امنیتی رژیم صهیونیستی در پی ارزیابی‌های نهادهای امنیتی، با طرح ویژه‌ای برای تأمین امنیت خانواده نخست‌وزیر این رژیم موافقت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/akhbarefori/671785" target="_blank">📅 17:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671784">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دستور اتحادیه اروپا به گوگل: دسترسی به اندروید و سرویس جستجو باید برای رقبا بازشود.
🔹
لاوروف: دلار تقریبا به طور کامل از معاملات روسیه و چین حذف شده است.
🔹
وزیر دفاع سابق ترامپ: بمباران هوایی تغییری در موضع ایران ایجاد نخواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/671784" target="_blank">📅 17:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671783">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
صدور کارت ورود به جلسه برای ۵۶۱ هزار داوطلب کارشناسی‌ارشد
🔹
تاکنون بیش از ۵۶۱ هزار داوطلب آزمون کارشناسی ارشد سال ۱۴۰۵ کارت ورود به جلسه خود را گرفتند.
🔹
از بیش از ۶۵۱ هزار متقاضی شرکت‌کننده در آزمون کارشناسی ارشد سال ۱۴۰۵، ۲۴۹۷ نفر از داوطلبان توان‌خواه هستند که برای آن‌ها تمهیدات ویژه‌ای همچون منشی، وقت اضافی و دفترچه بریل یا درشت‌خط در نظر گرفته شده است.
🔹
طبق تأیید سازمان بهزیستی، برای داوطلبان واجد شرایط استفاده از وقت اضافی، زمان آزمون به میزان ۱.۳ برابر داوطلبان عادی در نظر گرفته می‌شود. این زمان اضافی صرفاً به افرادی اختصاص می‌یابد که وضعیت معلولیت و بهره‌مندی از وقت اضافی آن‌ها به تأیید سازمان بهزیستی رسیده باشد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/671783" target="_blank">📅 17:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671782">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5784417b.mp4?token=bk9OmrZlN68QiVQEOCClzEWId6GM2oDKPWFUv1B9W_twPRrV3Zzac_YwTwBQ_KV72CPLrEMtwAVsBuz_XTYdxQQJzO_bH0_pm_FIjKd1N77zk0tocvyvEoQIHUxXCrJzc_BszNtVbpd4ml6ly2U3Sdi6FsG2OusB6FuNl9jLSsC9Rzu4Qf6sGxZ0cuEN3wS3dagbEb0S9EFw3nrvID0XiCiyyglcgLrdYM9oiRH2jPIjZi-osS92DdZ51FLFjHOwsjJDiBbDBvQhfKs13TlAGZYcZNOEoZCkvC7OqmtHug4ok1oTys3mxf0w3MM8zI5rWBTplh981hTDXOsWUXvIpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5784417b.mp4?token=bk9OmrZlN68QiVQEOCClzEWId6GM2oDKPWFUv1B9W_twPRrV3Zzac_YwTwBQ_KV72CPLrEMtwAVsBuz_XTYdxQQJzO_bH0_pm_FIjKd1N77zk0tocvyvEoQIHUxXCrJzc_BszNtVbpd4ml6ly2U3Sdi6FsG2OusB6FuNl9jLSsC9Rzu4Qf6sGxZ0cuEN3wS3dagbEb0S9EFw3nrvID0XiCiyyglcgLrdYM9oiRH2jPIjZi-osS92DdZ51FLFjHOwsjJDiBbDBvQhfKs13TlAGZYcZNOEoZCkvC7OqmtHug4ok1oTys3mxf0w3MM8zI5rWBTplh981hTDXOsWUXvIpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک خوراکی خنک و دلچسب برای این روزها؛ با طالبی و انبه هم عالیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/671782" target="_blank">📅 17:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671781">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
انتقاد رهبر انصارالله یمن از کشورهای اسلامی: فقط بیانیه‌های زیبا صادر می‌کنند که خدایی نکرده آمریکا و اسرائیل عصبانی نشوند
.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/671781" target="_blank">📅 17:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671780">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4a44f052.mp4?token=ma3BTVJmcxfAMG4aDs1HMCCrtz7ARuqsjdGqnA61kwwrsRqjfRNa_L-EevIMNc8OqXzCVf3WyzgtUlZzQkUInaTRMJ4LAuBuYHRxCKRV7fe4YpCJmtWfMDk_aSX5rm4e-AMcW8VWF7QMueslJA4wcsSPdqkgiDX8O7Mv7cC6STLL-8Y4eOk1jetjKGSMUBkcTQxsQqCMsjjy7F-YAiRHwgoHkmqd-LM2SQDfsSHmcuFQJK6QaFhpTbUPqcjVxEqxpUUM5InL8K-m9s3DUBfxy__PDPVZMtBpLsOe576UMLuvlLkpzWvJ6RlPE6IvnJCFUGWAy4UUnzEHv1UOUI9HrDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4a44f052.mp4?token=ma3BTVJmcxfAMG4aDs1HMCCrtz7ARuqsjdGqnA61kwwrsRqjfRNa_L-EevIMNc8OqXzCVf3WyzgtUlZzQkUInaTRMJ4LAuBuYHRxCKRV7fe4YpCJmtWfMDk_aSX5rm4e-AMcW8VWF7QMueslJA4wcsSPdqkgiDX8O7Mv7cC6STLL-8Y4eOk1jetjKGSMUBkcTQxsQqCMsjjy7F-YAiRHwgoHkmqd-LM2SQDfsSHmcuFQJK6QaFhpTbUPqcjVxEqxpUUM5InL8K-m9s3DUBfxy__PDPVZMtBpLsOe576UMLuvlLkpzWvJ6RlPE6IvnJCFUGWAy4UUnzEHv1UOUI9HrDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: عربستان باید مجازات شود
🔹
عربستان حرمت همسایگی را نگه نداشته است و با نظارت آمریکا، شراکت انگلیس و با همکاری اسرائیل از ابتدا علیه یمن تعرض کرده و همچنان ادامه می‌دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/671780" target="_blank">📅 17:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671779">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
توهین بی شرمانه ونس به ایرانیان : اگر نظام ایران سرنگون شود، ۹۴ میلیون درمانده تروریست به اروپا و آمریکا سرازیر می‌شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/671779" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671778">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_48phjmJfMSIQczm6rdvj0_2AG3Hw6VkahrsUgrHmxsR1y9ehQ1zxQn5C0plgkNKXKF-6SmX2En4R87LkQuQ3Gfw7UCO-XFEElspgOohH6U2QQ7qPy8qNUvinbF8gCTrr2pUZKmPZWvq49DUiFUPnfEv7A0rjIlf_smLJbyS6YkpzIYHNQIthezLZtMrFD8f72iAuRrtuWGXkM-enXNkbyFaZhq6tIpRpv0y1jMC1O0fTpvwFaemumyW-fTKqStk9Fr1rZtbBOypAnE_vj0rXLXgnVUcs69POk7NKQ-bCb7FUOb1Gr-6jETjvszau1CFW5hY29tVMwCjL_0FmRP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت داری؟
پس مدرکش هم باید باشه.
با آزمون تخصصی آریاداناک، مهارتت رو به گواهی معتبر تبدیل کن و برای استخدام و رزومه یک قدم جلوتر باش.
✨
آزمون تخصصی | مدرک معتبر | رزومه درخشان
🎁
کدتخفیف: aria25
🔗
ariadanak.com/ariaacademy
📞
مشاوره و راهنمایی:
۰۲۱۲۸۴۲۴۵۴۳
۰۹۹۲۶۶۶۸۴۲۴</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/671778" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671777">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa86c532c.mp4?token=GLx9hPk4oAK3JAAbnHuyesGWmbuE-h3OvNPPrshDAa3f1s-G95-haWBE2mR1KAZjoPKuiWJmsXgbOPVs_gTtVrZR4F-dki_C5qOjbOMtgLz4pLf4jLTU_Bp1_MxKpf2N0LZEpUFQg2lxYRm96Srp1NltkO7eplN2pO0gHh2q6G_dSfR8_rCRlRlvIf91cEuNOiEVQIDGlR9Pi2ahNYsIjXQlxLqH10XYWQ-Id2VS89Ib-DxFMmAgPf5W2J-3yvhQZf7l3FQ4H30y3GpJfkXHjAmkL7iAaIPS_n85cSYlJi8MNdUuFEkynWFB3KD_VZpkg9s8yE_Tugb8XByxfIh6Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa86c532c.mp4?token=GLx9hPk4oAK3JAAbnHuyesGWmbuE-h3OvNPPrshDAa3f1s-G95-haWBE2mR1KAZjoPKuiWJmsXgbOPVs_gTtVrZR4F-dki_C5qOjbOMtgLz4pLf4jLTU_Bp1_MxKpf2N0LZEpUFQg2lxYRm96Srp1NltkO7eplN2pO0gHh2q6G_dSfR8_rCRlRlvIf91cEuNOiEVQIDGlR9Pi2ahNYsIjXQlxLqH10XYWQ-Id2VS89Ib-DxFMmAgPf5W2J-3yvhQZf7l3FQ4H30y3GpJfkXHjAmkL7iAaIPS_n85cSYlJi8MNdUuFEkynWFB3KD_VZpkg9s8yE_Tugb8XByxfIh6Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فواید لیمو رو از زبون خودش بشنوید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/671777" target="_blank">📅 16:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671776">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دولت هند خواستار توقف اعزام دریانوردان به تنگه هرمز شد.
🔹
حزب‌الله لبنان: هرگز سلاح‌هایمان را تحویل نمی‌دهیم.
🔹
یمن حمله آمریکا به بیمارستان کودکان اهواز را «جنایت جنگی» خواند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/671776" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671775">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
آتش‌نشانی: مشاهده دود در منطقه ۲۲ مربوط به آتش‌ زدن ضایعات بوده است
سخنگوی سازمان آتش‌نشانی تهران:
🔹
منشأ دود مشاهده شده در منطقه ۲۲ مربوط به آتش زدن ضایعات در یکی از کارخانجات تولیدی اطراف تهران بوده است.
🔹
این حادثه هیچ ارتباطی با شرکت مینو نداشته است.
🔹
مشکل خاصی در محل وجود نداشت.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/671775" target="_blank">📅 16:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671774">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
هرگونه شایعه درباره نحوه فعالیت مدارس فاقد اعتبار است
وزیر آموزش و پرورش:
🔹
برنامه‌ریزی این وزارتخانه به‌طور کامل بر مبنای آموزش حضوری است؛ شرایط کشور در تصمیم‌گیری‌ها لحاظ می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/671774" target="_blank">📅 16:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671773">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eec695808.mp4?token=tRPJYbjTRAwPMIQnJElHJpdDLHR8XV1-bCvaBxMzOdtx1h7pPfVZs8kdtud0DBCikH6BFludMe3yjSPDpoqLn2oeIpkwUR9k29G5ecYZLcrE2JL7wNtXN1Q-JTvBrWV4ujULsLcWqye7_YKF5K_jNKleHVGn7QWYypb5cv7i-MGnM6JrYpgKeyVWlmiuaABioQ1k2MBS879XeJudyHUL6hcMVdhsLRPSOcT9Tv3DV9fmIA1S90Rj-48NMu_xW6tcQc6CnruegEDQ5Y2HLk9wQCCoT35fszEW9gYOCL27XXglM9tezAWXUkxEqErDIxT12e1Vbeo9M_vKED9N4o6J2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eec695808.mp4?token=tRPJYbjTRAwPMIQnJElHJpdDLHR8XV1-bCvaBxMzOdtx1h7pPfVZs8kdtud0DBCikH6BFludMe3yjSPDpoqLn2oeIpkwUR9k29G5ecYZLcrE2JL7wNtXN1Q-JTvBrWV4ujULsLcWqye7_YKF5K_jNKleHVGn7QWYypb5cv7i-MGnM6JrYpgKeyVWlmiuaABioQ1k2MBS879XeJudyHUL6hcMVdhsLRPSOcT9Tv3DV9fmIA1S90Rj-48NMu_xW6tcQc6CnruegEDQ5Y2HLk9wQCCoT35fszEW9gYOCL27XXglM9tezAWXUkxEqErDIxT12e1Vbeo9M_vKED9N4o6J2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تقابل تاریخی در فینال؛ مسی و یامال: از قاب سال ۲۰۰۷ تا رویارویی در جام جهانی ۲۰۲۶
🔹
سال ۲۰۰۷، خانواده لامین یامال در یک قرعه‌کشی خیریه یونیسف برنده شدند تا نوزاد ۵ ماهه‌شان برای یک تقویم خیریه با مسیِ ۲۰ ساله عکس بگیرد.
🔹
۱۹ سال بعد، آن نوزاد و مسی، حالا به عنوان رقیب در فینال جام جهانی ۲۰۲۶ به مصاف هم می‌روند.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/671773" target="_blank">📅 16:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671771">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLhiQm0-vkXQYt55g9zC1dt5Ofum9UbeHMf7zr8Fbzh5JC9-2fHo1Rw5SVB215GH4fEqgiw1bOwQp9GY2CZasVA3V3hGHG9N_MrVMatzYL97XlyT18U_6YaF98gVVIv1XulQ-nnYHSmSbAIK-UNebzfQwv492AgXkEmnXluCHkgOHJmDaWdMXUPl7vodK9tlrZtKE0gjWLZnuIMS8wjLRXj1jiLBEhwaP3iogsyRgIHB6q8_LvHEmJhS5ELm6XdNVmCq0LZWY__9eYGXIQgpwbBtzPClT9DjWbjkiDp_eciARXqC8L-DFouLs84Yf2IkOqdDuEGLwoEo8lMwC_-9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سایپا محصولاتش را گران کرد!
🔹
شرکت سایپا امروز به صورت رسمی قیمت محصولاتش را ۲۱ درصد گران کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/671771" target="_blank">📅 16:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671769">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCzUxX3QJ3zlaDBFiT5RxX5LTza-m1HulhyMhxrX4Sib4Tr_5SVyMz9voBrCDVIZRp5p3_nIYDDn1fPEnVWFHv2HT9VYcv5IPGJn4cZQwprETMqDn8X6PX7ZRMDmletovszuPFA0HK2aD0zJZWhYkibLINj0a8RasSg2uXaHmsUkWsCfNdeetJV-njNCd-nDHUUVPpFWhUzYm0hHF4nEh8nmfSCWAU2Oyfp5TGKWUAwkBTigcdrurPLvThjeBjetujyhr_e3ZJzRr8HorEkW7QOC9TVMeWSFsZZqMHzV1E4Pop9g4pKuphWhOFEArukVlnKriL9ZMKbUUPnjOFlEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بر فراز دهانه دماوند؛ طلوع ماه کامل در کنار سایه زمین و کمربند زهره
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/671769" target="_blank">📅 16:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671768">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbc5724b26.mp4?token=hfpIZbI_XMsQuOofBXmB9Uxpc5GxTcGNg0cb1kFi11KCf_APG33VazRyhGXDaWT57c-oAdkiMS0dWN8ygNTAEIq663ADIPJ5F266tLNCXEzS2hxAIRH1Wfv31MD_pZN4o7idDclTvknwcqeIcs7DffzjJAiDskmSRcAOIudLQPpEIc3Zkh9yT-XrZdqNssiHEh539XczC_Uzken7pmm_yZA1eYS9u9trFv8PFbwFHno_WXjhOzoRoKTqqtoR-LvFjTDvGkpWGEfUxBj6CmiMFP3FnW732mBplVr6lSH0PPme2Xryo0HqCqOtCk2TMMla3szY2T3WNvkIa7_zM1_YGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbc5724b26.mp4?token=hfpIZbI_XMsQuOofBXmB9Uxpc5GxTcGNg0cb1kFi11KCf_APG33VazRyhGXDaWT57c-oAdkiMS0dWN8ygNTAEIq663ADIPJ5F266tLNCXEzS2hxAIRH1Wfv31MD_pZN4o7idDclTvknwcqeIcs7DffzjJAiDskmSRcAOIudLQPpEIc3Zkh9yT-XrZdqNssiHEh539XczC_Uzken7pmm_yZA1eYS9u9trFv8PFbwFHno_WXjhOzoRoKTqqtoR-LvFjTDvGkpWGEfUxBj6CmiMFP3FnW732mBplVr6lSH0PPme2Xryo0HqCqOtCk2TMMla3szY2T3WNvkIa7_zM1_YGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشف لاشه پهپاد متجاوز MQ۹ ‌آمریکایی در دهلران‌
🔹
یک فروند پهپاد متجاوز MQ۹ دشمن بامداد امروز توسط سامانه نوین پدافند هوایی نیروی هوافضای سپاه در اندیمشک رهگیری و با موفقیت منهدم شد.
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/671768" target="_blank">📅 16:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671767">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4pOjC8wMxrnHbNm2M5V-JzRqoJw8Jok5gEJ8B2HZcndvJoQffw_E6KPxUZqLjl4NaJFkUBP1nUwnrUj3mILTma0L6cKa8nVV1p8GK6VGTbmGItAvfbguN2z4slnzuLxVIsTZEQSqu1wuH9sDmYZMda_G11n1AEuoB-1wh6bLwklWcfkP7yvTdmC_gyEBrykx8Mih5dHOIPIg1wZGwweWTNkkq9F-ID5a7Q-pLE45kMFnJxlC73k33_4UD89u3X1m4PYeYr_GeSvbMSiv-mk-oy4P7hgmU5emznEHus88u0rwwDaG_Q3z743zwF97hDBybHHWEr9bhbZ-S-Y33EgtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام کشورها بیشترین مناطق خودمختار را دارند؟
🔹
روسیه با ۲۶ منطقه خودمختار، بیشترین تعداد مناطق خودمختار را در میان کشورهای منتخب جهان دارد.
🔹
پس از روسیه، بریتانیا و فرانسه (۱۱)، ایتالیا (۸) و چین (۷) قرار گرفته‌اند.
🔹
منطقه خودمختار، بخشی از یک کشور است که با وجود قرار داشتن تحت حاکمیت آن، در اداره امور خود از درجه‌ای از خودگردانی و استقلال برخوردار است.
@amarfact</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/671767" target="_blank">📅 16:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671766">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: هرگونه تعرض به ایران با پاسخ قاطع، مستقیم و بدون تردید مواجه خواهد شد
اسماعیل بقایی با تأکید بر آمادگی کامل نیروهای مسلح برای تمامی سناریوها:
🔹
ایران در دفاع از امنیت ملی دست‌بسته نخواهد بود و همچنان بر اصل «تعهد در برابر تعهد» پایبند است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/671766" target="_blank">📅 16:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671765">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3db11da08b.mp4?token=PDAge_zPFt0NKrqLLgywmCP1Jr1BkAMcg8Il3PXQDaLEDFCVexY6GXQ43tKqpQot9kicHvnQ2nYFp9z4Zq_QIozmX6Mb-e2hFBHPE1EjZN3ziYav5y1-3sPvKVi4AHwliN4cELK3X9jTSTQgud0xK0DSjWuAx6hhkgAXf2LHg7VGSQg-W-hKN3mYIP4pDWomcVVaDW6zi7dKtaDXPCOL1fR_EmQUdzFaxkBYjL2YIAeknHdM7E5suWwO7RuSKgu1KayWbhyPpfWDhQ9LxHDGBDalJ7fSfDIJ6YrINBBnuN--2muFUfzKf5HTgH9rJYMrqphhmzjYpZeoHw2FkVvSow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3db11da08b.mp4?token=PDAge_zPFt0NKrqLLgywmCP1Jr1BkAMcg8Il3PXQDaLEDFCVexY6GXQ43tKqpQot9kicHvnQ2nYFp9z4Zq_QIozmX6Mb-e2hFBHPE1EjZN3ziYav5y1-3sPvKVi4AHwliN4cELK3X9jTSTQgud0xK0DSjWuAx6hhkgAXf2LHg7VGSQg-W-hKN3mYIP4pDWomcVVaDW6zi7dKtaDXPCOL1fR_EmQUdzFaxkBYjL2YIAeknHdM7E5suWwO7RuSKgu1KayWbhyPpfWDhQ9LxHDGBDalJ7fSfDIJ6YrINBBnuN--2muFUfzKf5HTgH9rJYMrqphhmzjYpZeoHw2FkVvSow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیو وایرال شده از میزان احترامی که تیم آرژانتین به مسی میزارن...
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/671765" target="_blank">📅 15:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671764">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZ7axM3vb-O4OJXrnalGRSmISVn-r7tXuhDvYe114pHWidP5gC3eyEHcqZI3yl3J8CLksEapLshi5PI6UXcV4ijoeCs1KlepWMflUgp58DafRc6rtG6jibB5e4qVUA1cMN4XR7gFmuOYDnmbzRNB0f3JHLwJQHs-5zz-xtKRCBn9pxegrP7zAWU5CTmPimLv3Zj-s0x6af_9CdUCGVI7K2E741okWwPv4TTFhNa2_9ookr2asDOQSrcY6wKsCxD5ngWnn_xL4zSnOO5Yldeyl2_ylUpu3ypISW8i5VQ6GpmvRFejm-34DMAD_bQ_dFoZUz-UsYP6caNndw6OvaJrew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
کالکشن ویژه تیشرت‌های اربعین «قرار»
طرح‌های مفهومی و مینیمال، مناسب روزهای اربعین و مسیر عشق و ارادت.
قیمت اصلی: ۱,۴۵۰,۰۰۰ تومان
قیمت با تخفیف: ۹۹۰,۰۰۰ تومان
تعداد محدود؛ برای ثبت سفارش پیام بدهید.
🛍
سفارش:
@gharar_order
👀
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/671764" target="_blank">📅 15:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671763">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU0qTaBBuuShOvv7okeRSJ9jW7h-mFBTlzAfQZk45JFT6Ff9RbjVZ-_Ee3n3ehQQ1CeZ5rLXsbiGH56k5bsNsN46qME5IPMa8jAx9LIlhc7yYFyfyuQal4U4sAbPo8_Es2QJy52MqAr1lW9Npkgqlkq-M0wahvaWF0mrtqKrgbBXEDwWRxB1YPnBEG8YMoD7GMTpUbAh-8EoeP-K7gnha0cEvW1fwNSqD_k9LCXpo7EOdVXkymzMjg-YNBxpmrw1Y243uXs9AHzTPs3cI9u5InJBqAIrcPfa5iW06XyWUy3ZE60hRudA-jy6SFpIUlmPxhpsmBXOWbxEMwKNlA1jTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چطور با خرج‌های روزمره و کوچیک سرمایه طلایی بسازیم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/671763" target="_blank">📅 15:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671762">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8c13c9ef.mp4?token=fZc2_aO4Vc1nrRYRfurZdM4MlLXutwFohP7jf37SZO5tVGaz0nGBWrwHhwHPWESbNfViB63IAUJ3psOH0vU-x6tr-MD9F7EfeaE5hxgrJXWa5nzssNQh3SL6sDSmW7lHSW1tn2zwWyr4AYpyAm2zNEAWTk2zLalqzlV4P3VfzXjNkJg5K1AuPV05QpWV6F9V7JsrbsYt9OxWk0y_DPAUVEd4HUhW3WffQllZ7bsuW4EF9IVmfyg_ZUR51hVTwHfHFf4l-9Upbg8lXalmV_x90svEMYLbJuWUVg0-wKM651bWKh-MBszxfOpCa9J5m9xuV6IWLDRozJd8Y0yV3Jnirw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8c13c9ef.mp4?token=fZc2_aO4Vc1nrRYRfurZdM4MlLXutwFohP7jf37SZO5tVGaz0nGBWrwHhwHPWESbNfViB63IAUJ3psOH0vU-x6tr-MD9F7EfeaE5hxgrJXWa5nzssNQh3SL6sDSmW7lHSW1tn2zwWyr4AYpyAm2zNEAWTk2zLalqzlV4P3VfzXjNkJg5K1AuPV05QpWV6F9V7JsrbsYt9OxWk0y_DPAUVEd4HUhW3WffQllZ7bsuW4EF9IVmfyg_ZUR51hVTwHfHFf4l-9Upbg8lXalmV_x90svEMYLbJuWUVg0-wKM651bWKh-MBszxfOpCa9J5m9xuV6IWLDRozJd8Y0yV3Jnirw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توقیف کامیون در هرمزگان؛ راننده دختر ۱۰ ساله بود
🔹
رئیس پلیس راه هرمزگان از توقیف یک دستگاه کامیون کشنده به دلیل هدایت توسط یک دختر ۱۰ ساله و به خطر انداختن امنیت ترافیکی خبر داد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/671762" target="_blank">📅 15:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671761">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d221f37fe6.mp4?token=gpEi74TTnEjP34XHTCwDcm3DJAjyZlmEPgJUA7R1sBzsCiSHgsx9fd2pUp31ifVtoWl7H48h5TckI9wyaFTsJxw9oUM1A8thK_iftwdHUlRf4iHEiV9ZLWRD1CS_YWcfUuihd9TDqFYFqY3A4CZFB9JmBxyHysN_aITc3u3aL0ubJGSfM8yeTbdk0BPOF02PkbSRumSwyYmaPmRjVw4VF2hd3RFhEOgWhgtWNa95Q0GACSIkcMtl-HAVrwrLzFlmft01EMfgfFzH-8JVTnQ5TqP8t7mEIsJD6i8VhzFlmXNysGi0yMsipZTCDC5OnNgLCeo8BhEq1dp3e583MGXh1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d221f37fe6.mp4?token=gpEi74TTnEjP34XHTCwDcm3DJAjyZlmEPgJUA7R1sBzsCiSHgsx9fd2pUp31ifVtoWl7H48h5TckI9wyaFTsJxw9oUM1A8thK_iftwdHUlRf4iHEiV9ZLWRD1CS_YWcfUuihd9TDqFYFqY3A4CZFB9JmBxyHysN_aITc3u3aL0ubJGSfM8yeTbdk0BPOF02PkbSRumSwyYmaPmRjVw4VF2hd3RFhEOgWhgtWNa95Q0GACSIkcMtl-HAVrwrLzFlmft01EMfgfFzH-8JVTnQ5TqP8t7mEIsJD6i8VhzFlmXNysGi0yMsipZTCDC5OnNgLCeo8BhEq1dp3e583MGXh1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جاسمین کراکت، نماینده کنگره: ترامپ احمق مناسبی برای نتانیاهو است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/671761" target="_blank">📅 15:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671760">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3762a04834.mp4?token=JVog2HCA7b3L3Y77WxOY8lr_Go29rgbdcgxy0buv6yP6ECCrkgaWrlZ_dtLUsnf8GjQcvjESKZdn7IBrvyy4y_3LuhBr3GUK792pNknar5-mgLGs5Ab4t1yuqqlfRQCqfltAauuyhMln8sOAq1TCRNx_hkdVnAy7Yu50PgnnxzJWT4TXDWpWDJHqGXIhagmw7-EHbiA_u1cdZWz6XP0vO86N2HZDSh_0YUUbzKpWzkF_KfjwsQtUzZxrhOACjUg1vb0wz3gTEiCA2xTe_gDGlqy7eQTFkh8jRZv4EAy5oe3u93SCXzMnKHlUygEoDbVwo3Yrum-OX52ZjcTC-U2wKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3762a04834.mp4?token=JVog2HCA7b3L3Y77WxOY8lr_Go29rgbdcgxy0buv6yP6ECCrkgaWrlZ_dtLUsnf8GjQcvjESKZdn7IBrvyy4y_3LuhBr3GUK792pNknar5-mgLGs5Ab4t1yuqqlfRQCqfltAauuyhMln8sOAq1TCRNx_hkdVnAy7Yu50PgnnxzJWT4TXDWpWDJHqGXIhagmw7-EHbiA_u1cdZWz6XP0vO86N2HZDSh_0YUUbzKpWzkF_KfjwsQtUzZxrhOACjUg1vb0wz3gTEiCA2xTe_gDGlqy7eQTFkh8jRZv4EAy5oe3u93SCXzMnKHlUygEoDbVwo3Yrum-OX52ZjcTC-U2wKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فینال جام‌جهانی؛ بازگشت اساطیر در راه است؟
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/671760" target="_blank">📅 15:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671759">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادعای مؤسسه کپلر: طی ۲۴ ساعت گذشته تنها ۱۳ کشتی تجاری از تنگه هرمز عبور کرده‌اند که از این تعداد، فقط یک کشتی از مسیر جنوبی (نزدیک به سواحل عمان) استفاده کرده است/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/671759" target="_blank">📅 15:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671758">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
مدیر بیمارستان شهید بقایی اهواز : پس از حمله تجاوزکارانه آمریکای جنایتکار به اطراف بیمارستان، موظف شدیم ۲۱۱ بیمار بستری را جابه‌جا کنیم
🔹
تمام تخت ها و بیماران بیمارستان شهید بقایی ۲ به علت وقوع شرایط اضطراری تخلیه شدند.  #اخبار_خوزستان در فضای مجازی
👇
@…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/671758" target="_blank">📅 15:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671757">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس فدراسیون فوتبال: نتایج تیم ملی در جام جهانی مطلوب بود!
🔹
مدیر آژانس بین‌المللی انرژی: موجودی جهانی نفت خام در حال کاهش است.
🔹
وزیر جنگ رژیم صهیونیستی: از لبنان، سوریه و غزه خارج نمی‌شویم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/671757" target="_blank">📅 15:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671756">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2569337d78.mp4?token=JYkWCAdTR9Shs1m2QHC-CVm3B1q62nMVxPytBnaTiIUSgiGyiju5JLtf0jQDp62s_5J1pWJmf7w2ERXDfRTsdVXr6TTyuXAtBRueHefKtv6fx_Nn-TKOPRpNRwLHaa2bPRgkgUXIS12lXoTjn7YE7F0dI0hgup3JnrgY3o1fNcq8Px2d52EOHkk4uywajYbROeyJShmXSO3MqAuWjpkc4KsxMc8-tyW4F-COnZ6ZH23yJV48I8fvJRJF79xaaTGOad8p1M2kvBLbGiac2chZupjBtsjxYgSC0RlzKQ39r0JmJS3iY4xotHmh4Eh9g8rw2jOm2sEHmf9FJlF3_BC-7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2569337d78.mp4?token=JYkWCAdTR9Shs1m2QHC-CVm3B1q62nMVxPytBnaTiIUSgiGyiju5JLtf0jQDp62s_5J1pWJmf7w2ERXDfRTsdVXr6TTyuXAtBRueHefKtv6fx_Nn-TKOPRpNRwLHaa2bPRgkgUXIS12lXoTjn7YE7F0dI0hgup3JnrgY3o1fNcq8Px2d52EOHkk4uywajYbROeyJShmXSO3MqAuWjpkc4KsxMc8-tyW4F-COnZ6ZH23yJV48I8fvJRJF79xaaTGOad8p1M2kvBLbGiac2chZupjBtsjxYgSC0RlzKQ39r0JmJS3iY4xotHmh4Eh9g8rw2jOm2sEHmf9FJlF3_BC-7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به شهرک النبطیه الفوقا در جنوب لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/671756" target="_blank">📅 15:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671755">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698b4f5438.mp4?token=FYys03G2WYGnL4fowFpQW1tD43HQiVuDMcwruzww2VLqJVuWo16KZsQSsU1rgzSzIM63MsKsLYR74vyCldMP2GuknwMDNo8Vx_pmV5YvzJe4x6DYH9BwqjKMQaeDywWUrl2xvZIox61f0sIU3a82Zq7aQKYbWFvmTn7NeUx9KxTC9f4ssNAp7s0-8Trcc55bWuBR141uvbirckfhdYY5GGeBqBGU7Hr1ZFj89DwHYvYkLbMiQ-zMH5bXYURqT2uoWYPPT9KYH5NDhpWjP0PHDr-YU0ZF-ZrbLAjYjMPE_c5vqbC4AehKk80cADACmf114ppZFTgr4L-KKQeQNcZVKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698b4f5438.mp4?token=FYys03G2WYGnL4fowFpQW1tD43HQiVuDMcwruzww2VLqJVuWo16KZsQSsU1rgzSzIM63MsKsLYR74vyCldMP2GuknwMDNo8Vx_pmV5YvzJe4x6DYH9BwqjKMQaeDywWUrl2xvZIox61f0sIU3a82Zq7aQKYbWFvmTn7NeUx9KxTC9f4ssNAp7s0-8Trcc55bWuBR141uvbirckfhdYY5GGeBqBGU7Hr1ZFj89DwHYvYkLbMiQ-zMH5bXYURqT2uoWYPPT9KYH5NDhpWjP0PHDr-YU0ZF-ZrbLAjYjMPE_c5vqbC4AehKk80cADACmf114ppZFTgr4L-KKQeQNcZVKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به یاد سربازانی که دیگر بازنگشتند...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/671755" target="_blank">📅 14:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671754">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c19qURHjBBQAvn_WdSHqOkqEsA3WIiF9qmarOoc-qf2tUAJa-jf8X0hXuXZoOism1n4DRDa7NYW32h_dpDp09wVyVe9G1S76YRatdG3YqknxvBRhFXHKHqEGAwejLefkA_SXUWCR3Ub5Dm-mZAS_qXAun5Lipa3u82ia-mAfJjO0ZXHkpJgSdTQYDFls1OrUXc_1TvTfPzaZYMWRNnKS-OBN5nDv8r_sycPx20edhPzIZBco7zw1GzWr_aR_GAj79MThlxvUzbnpFZkCI5xOBbGOwEmu6cztWCA3W38Yzpz3SN5DHK1KkhIKdOQnFUJekF218gvb77T5QxR7zJE2pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران در غنا در پستی، حروف کلمهٔ  HORMUZ را رمزگشایی کرد
Hands
Off!
Recognize
Maritime
Unchallenged
Zone.
🔹
دست (از تنگه هرمز) بردارید؛ منطقه دریایی بلامنازع را به رسمیت بشناسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/671754" target="_blank">📅 14:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671753">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
واکنش خوک زرد به پرسش درباره کشتار دانش‌آموزان میناب
🔹
مجری: آیا متعهد به انتشار یافته‌ها خواهید شد؟
🔹
ترامپ: فکر نمی‌کنم کسی بتواند بگوید آنجا چه اتفاقی افتاده است. در حالی که چنین اتفاقاتی در جنگ رخ می‌دهد، موشک‌ها در همه جا پرواز می‌کردند. و نمی‌دانم چطور…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/671753" target="_blank">📅 14:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671752">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
رسانه‌های عربی از شنیده شدن صدای انفجار در آسمان منطقه «القادسیه» و محدوده بندر در کویت و فعال شدن سامانه‌های پاتریوت آمریکا خبر می‌دهند/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/671752" target="_blank">📅 14:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671751">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7ee4b457d.mp4?token=fnxzsj2-Z7tJICzLWcRZO-UUXQBnTO-zPqmXuyiibPBv13GgFKgA45XObgQf1azdmsQUlcIFM3tJMM5lGaLAFkOC98WZSuvTffgJzJBCIle4onEn37RCid3tGsCjGsguNoJgOVjN241nvUMDnDa-qUDYoFL-eoFl-C-B-8qrsDAxuZ7lPpZ4kYwaGuonrxYmbuGtWIQD6uOQf49r_YQdz8CH_JtASYPnXaalV3gC7LLc7Ff1gUqLMWQu36Awo6XR2ybwUnm6oXKc3ZQHhRTfaSQ0LiKmAC_H2nGg9BcD4GTbrtV9XEAAQoYXIyEqBUvLhIuKQxbBbiDelYvp9beK0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7ee4b457d.mp4?token=fnxzsj2-Z7tJICzLWcRZO-UUXQBnTO-zPqmXuyiibPBv13GgFKgA45XObgQf1azdmsQUlcIFM3tJMM5lGaLAFkOC98WZSuvTffgJzJBCIle4onEn37RCid3tGsCjGsguNoJgOVjN241nvUMDnDa-qUDYoFL-eoFl-C-B-8qrsDAxuZ7lPpZ4kYwaGuonrxYmbuGtWIQD6uOQf49r_YQdz8CH_JtASYPnXaalV3gC7LLc7Ff1gUqLMWQu36Awo6XR2ybwUnm6oXKc3ZQHhRTfaSQ0LiKmAC_H2nGg9BcD4GTbrtV9XEAAQoYXIyEqBUvLhIuKQxbBbiDelYvp9beK0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
انگلیس تا یک‌قدمی فینال رفت، اما آرژانتین رؤیا آن‌ها را دزدید
▪️
قسمت پانزدهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/671751" target="_blank">📅 14:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671750">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4358d8bd7a.mp4?token=huKMcZel0MNhyum_m34MIGSI4EbbaHJR5wOJhWDxyr3KhLd2hamEX372QZwNU-5fn1SghXpsf6QLESms8XFcim_uO_UMEmeDyEvnYNxmhnVdzdnLdbMyRRs9SQWA4E1mySd1eJx-ESOFlDWK3Vmmf7AEN83nDtcTlU3b2X0fEfbkj3gNWdixyluaK9DNk5O24CuHcrbV6qaqkf_KfvZWem4KfgCszc6MIb7v9tBm_QTviAXJXNWnCtLmtWorFN_nV_Tf8vhPQXpKZdnkXcPxl8yZreytm-bqPwpExLPM3V0F2pdsY8nJQns9BvsB0QmbbuM-AlFpyeqQZSImVbhpXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4358d8bd7a.mp4?token=huKMcZel0MNhyum_m34MIGSI4EbbaHJR5wOJhWDxyr3KhLd2hamEX372QZwNU-5fn1SghXpsf6QLESms8XFcim_uO_UMEmeDyEvnYNxmhnVdzdnLdbMyRRs9SQWA4E1mySd1eJx-ESOFlDWK3Vmmf7AEN83nDtcTlU3b2X0fEfbkj3gNWdixyluaK9DNk5O24CuHcrbV6qaqkf_KfvZWem4KfgCszc6MIb7v9tBm_QTviAXJXNWnCtLmtWorFN_nV_Tf8vhPQXpKZdnkXcPxl8yZreytm-bqPwpExLPM3V0F2pdsY8nJQns9BvsB0QmbbuM-AlFpyeqQZSImVbhpXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکورد یک میلیاردی؛ ویدئوی آرامش‌بخش ساخته شده توسط هوش مصنوعی بیش از میلیارد ویو در اینستاگرام گرفت
🤯
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/671750" target="_blank">📅 14:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671749">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVTkzTGI9ib2gvke-WuN3Ntb1iXsOhwgAi2kbiHDG46Xe2TibNlLFm2Hyt_UdcAudMETr1ngjIq7yp5mFw-_qUcwdXcqXkXvTpr8MrIPmUoscUgAXTRAw5gvH9V8ncPlul_CRyMyhwrtzzZL81hj6Pvc09gfpIhVltf2PpQ7dSeL49Unad0S2v6P8IA775SLGTLPfHm9QjuRHUPF97JtRJztRsvNyBOQSkLyRMDPYzoaX4hrC2LkRG3wtFYHbFHlFZYLMBe3HVVXrYDk7AGHG2zwM8MkEQHIc673WESpIhWgpCXyxd0L_AVvbgi2rEXeneMm2U2XCCUlamty4AxD4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک نکته درباره واکنش کاربران شبکه‌های اجتماعی به درگذشت مادر داریوش فرضیایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/671749" target="_blank">📅 14:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671748">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EECpz8-wY470oEbiokAg0tR6rKtT3bP1TYrb-whcFgjgBtQdIpJj6OBRQ0nnrppLflg5zp_GCOdOfJ1DD3PBq55UngAEfzhBsw-Fp5kW1DdlLzBOynBF7dQVRU6_DuHfKip9gyVlGbBJgOXP6E8XoZSZha7h7rWqu2kRmDvMWnipDbNM3-Bb0NDMdl47-QpfBW1wqZ5jKn8iLyTRaJkP9wNlUIRXFHWJsvwujmAQ5woxG3IlOCcXwBGbZUW6j68q_Xh3FOBkPpAYqTL5d3rZeJYo88WV3E_FElL26ulF5l9CCFhN5-O-aihUnN2G-Zpu-AwVNH9FSjG99TRZqiQQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس‌لرزه‌های جنگ بر صنعت بازی‌سازی کشور
🔸
۷۶ درصد اکوسیستم بازی‌سازی همچنان درگیر چالش‌های جنگ است.
🔸
تا خرداد ۱۴۰۵، ۴۸ درصد از استودیوهای بازی‌سازی کشور ناچار به تعدیل نیرو شده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/671748" target="_blank">📅 14:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671744">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0nvbLf0CFyhD7uGOPG_MeStKxU5An9_38dwTUZ2mRZeKuu8YyCT9RtIEIdQxIlLpTy2j012mj0rqnceTwcTAy3uaUKM5WPjZQb4IPpyFGz-uoQnPcuOoy6LFhPMd6hAjjU5Mt5E13C5E4XgM7X2HPv2m85EgjDHlme6bt2uuLWH4Y872mQfq5-IyMDlOmAwEYtTmTiCQQmWPPKJSD9ycILtJcDEt47R2GgOOA7UbQLXS7j9c54Uq-nDYLBfgKQ_HF3Io_UXYE-3Mt4vh3pv9koEGOewv-td3t0cdGaMSH2PBiFGojJTS7kJdc1zxjhAyHjnULpsHNBdyfR8aIymmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gZbwxpA28e7qi84BesFpuqh_do-1s5orFkWQgDnYEN5iBeJcKo_SFGgBMjh2tQkCXGTYJEIXMqSA80Dfyyu-eRAtCU4CVtZz0itCaGoNx5nvgzajIJd5qNHJtYAtJgUuI8-29FaYYVcPndwlNpOJf8_tdx3EqyCMWmJP5AhtgcXoK8lTj3Lr7W1sGFeFKPqgTJsiKoqdPcsJA5KCiMTpF9oSmhRTOBb850GNcbcot2AzmEu3GfP_WmPmOKGNXt-X4qzeoEGMSKTWX-l8cZixfpUIX8X0mqtq_5hIE1wGwScuxjKdNAxiSAO3-_6cugDemXJvMNqfc1rsdfUhdX2hnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OqJ_pCwvPMOYaeGtFfV557if6pxBCSspq0usKyKGwIp48W9DvAKNDEbZARDCYi71zriR3tELgJt_GMQaZsi3u8DDhClJL4xYUzAlg6KQXSsMCrpCGFJG0vJ57VLKiU-jyeA1Xfg4ojxiAM6ZPWSAPtE-vO24c7WLDy1NmALm5c2tbXGo9cuJW7oSpls22z_0zrkGoZNy9kw8g6CmhrOyPGMGPDiIEeTLb9WhU8_6ljjbW5kKao08N_JCP_UPiKyGEY75R_Dv1r_OmtucMgb_jWZCyY88f-HcKH9JGAWPgbLO6KtQOHkYjPD-6BO-jCjS8VsjNWYLp_pg4Qi8W0I9Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YzPVryjUID4oCcGsi5quiFO6hSehSeKF5YeC56Kvg09w4yuquJHd1FbKghDcm_qRbNgrFqgt5fv4yk22-7nZb13ianQwR3Rh_njCm7KA-q8bErRrHG9b-9CVBWzuQ8Hn5bWXuuxVbCKqlhnKPeLyfCN8Bzi3QDHcQv-_S3D2Vjyxx7cnfJMRWsBxePghRdRxMNSy4fEB8Z2CMLdEDB8N5bkHGwDjaPk8n9KyuKWb5mj6T8OUY_0H2HiZDoXctBH0BFyFXlUJsS8RdgCi8s7qqSWP0uaQAORJUrg6g7vRxF6xf3WpxIx-m2UIyKy2Oy1AuUGqrNCf-S6lq5KhK3DtVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این راز ساده، استایل شما را چند برابر شیک‌تر نشان می‌دهد
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/671744" target="_blank">📅 14:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671743">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
تیزر قسمت سوم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ فرهاد یزدان ستا که به دلیل ناراحتی قلبی به طور ناگهانی در منزل روح از جسم جدا شده و خود را در صف بسیار طولانی منتظر و مضطرب می‌بیند و در هنگام عبور از درگاهی، اسم اعظم خداوند را بازگو می‌کند و از خدای مهربان آمرزش و دادن فرصت دوباره جهت جبران اعمال و بدرفتاری با خانواده و اطرافیان را طلب می‌کند ؛ نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: فرهاد یزدان ستا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/671743" target="_blank">📅 14:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671742">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
اجرای عملیات آفندی هوافضا سپاه علیه مواضع آمریکایی در موج های هشت، نه و ده عملیات نصر۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/671742" target="_blank">📅 14:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671737">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pMaONJpD7saiWP5FzWx9CCfYboYjOi7bJxlVekdqrr7Bpg7TFvBk5URy2G6_PvUzuSLCkIuZBO7EdKlXUc_Sh9ufuCyOxDsR4NYhnVdAmQNB2IFvNtsgdwfsFwfhLGqyLayufZ-jkmyghkCQIu8w1TXWsNNlBe4vSeLfm-xzR-fT_WGgOzEgzhe6dV3eYqqbbEhA1ivp0a3VY71yxyHiXK6AMQeCURgVqSdMsd3HgmGkWvMAcQq2O0vJ1_as4hz4libCIuU2wKZwBrngNf7YuSYzjXyZ0cYlf_czc3-IPcW8G_DD3SxFXSOT4PeRcJihf23CFqlXmUx9XxneBm7cxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJo_SbLSwO2J4H52TN5a1C9jh_FNSRykKGcuDpxVDAC_5YkT4yh9pNEAUBM4s88RD_xhdmB8_7XmGWFB7pihY3hQLPBi6U5wDG5Y6G04oiXFHfFsAmNHWsbrRMb2gcUlF72qDKaHvF-qLU-XYMI0LkayRWRPBdQX9dNvXU7igeDj31RPB3Ga7cUL2GWh_i6tkqDAd2MqtC7d4NFhCeAjqGHBBMfOxuOLBj_9botuIYEu5fwNFnAo795uh0vvXXm0h14XLG9ouH-dpgJyaTj9-lK9Pl5IF5PA3q3spU-4t-Ay-WZ5c_5n3WbpGfXvC-NAZzJsnZ3fLEVd9vIxHApSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgVOA1PowBUzAtd9rWnYMhGvF3cSEGgBITXlCFQGh1WzeKw--uETYpAB5C7mf5WIFYc6PShMMxQuKuybkDcPlI7YuvuBPsTqQcSqwY7Ju2h-nybXld4oPvzxlg-m1s5PzUpwrhZV_GZxsQ_wtB_aAk2HV96pv_xsE2u4FaEWhFPmbdckVipW0_GKi4Hxq6FgSu7zMVTFLUxRz6olYBbvSqZg3qHntX7F9UDtOm8kJ0zaiu6-gJcXbt2i28hikG1p-77CLm2IczX9XIcI2IU-0e_lMAgaKoPBBbron9_ndHSeLJfIvTQcCICv1ZPiHzQmy-IbP4BfvZrTV7GyO22W0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLqSZ0c8B5wlcnw3p366RlEPSeZpfI8f0aQtioziKqP_FSI_bvF_xf6AUJADG-bbAcX_hEs6_y3oqQ2eMpy7nbaiAveNO6v6-DGaW0VzF5ZoSmPTHSHzPv7WNgyGLJZaFV9xWzrPGqPwves20Xez-1iEtcJNkeSrXWwng4LWb8HdpyD69rWcpPhKO_B6mpyO4QA_lZRDMTeXwLkSgdEdU6uLfVhFsMnY6bUn3sI1aYqWVAIKknYH05gItblg0oSCIoW9aAUk1X0E50ULHGXsQCZxNm8HI_asUUGbdlN67sS10oCU7tUyispy9OKfREYqdi83zN81gKfeVdbrULauHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYcKTVOw8Xx-4JA2YBNhN9_xTBwcvTPUTeHXitOBFCo1CvmZbqX9wzMJPjylrTHESk1OA8-4ADrNSqd0p3YZ1bLlCBs8yIhfHowaQvnk8nzoisfC9YzUnPpl1oMh5dDoB7bSPS-aJUjBaeKlG7U3B0q17wzlEZizidgb3xMoKGUEPWORec5FoMS8oz9OsIObL_nVcp_wfqw6yD7x93FDgWUNiqy09T3Hz66_pKW78S2uzgL29B3-xAfrNBONqi4S1EjgtuOMMhAoygjYlkKMxI4TsrsWRBUL8oTblwzKvo4I9BxSIs6eivCBmLup4wCjn76LnmtlpatDW_BsdI723A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دود آتش‌سوزی جنگل‌های کانادا، هوای تورنتو و نیویورک را آلوده کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/671737" target="_blank">📅 13:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671735">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY6Cfk1h7da1VJn0VRMo1Sn1Wcd6NfEk2BP0XAwLX-ygkaP5JTqIbDasR1auWAt04kv5fZn7t9mCC1SCdWa74-pyr2LISfvrmk7Ri1L2znAFPYP9h8cwmUkrrt0hrV-oxT6QcTY6bVMnakuDkfPJGrTf-EltKMgO0v_97AnWiJ29z3F4UCsS6so_ej_o0nxEwSGnQpkNtymEjwALsHYAXp0QtOoTG51ZJCMcccp27SRvD0KdPGafHR8JnsMdtvOl2WbXPJgG1l_2SqhbA_nJjM7LtqAu4hycZoEZKc6XxsDcqdp-bbrFWSQvq7lpeLFdAOP5k9tFDOkmzpYFsWuA6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیر بیمارستان شهید بقایی اهواز : پس از حمله تجاوزکارانه آمریکای جنایتکار به اطراف بیمارستان، موظف شدیم ۲۱۱ بیمار بستری را جابه‌جا کنیم
🔹
تمام تخت ها و بیماران بیمارستان شهید بقایی ۲ به علت وقوع شرایط اضطراری تخلیه شدند.  #اخبار_خوزستان در فضای مجازی
👇
@…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/671735" target="_blank">📅 13:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671734">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b5af118ad.mp4?token=jNeFHsCxxOdVylX5EvastTisO2JwnlHTLqPsm0PCl0D5USkW261fitaRHn84qVI1oKHszRO6EDgNNMgnj2nH4l4XMWP4fYGIRRDsVYMPUddQvZiyxXbhWMX9cHeqV1Aws4YKMsp4shaINaz-CzSgqgwGnIrSE8FQfaSLTFW8I4GvLRLW6WMQzxuhsActBKGcPuFapu9TZ-74f3Vc1UsNiVCIwHCVXzpPbwlGOA9o3mMtv20FVwHhtvZWID-nYev2McGoNEl1Nz7atS1b1fEu5wIQXnXCf6n-o7o36BPapw1rYBibtN9dVW7Xva_oJNYnh91vC6kiVmXpfi9GaIuwqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b5af118ad.mp4?token=jNeFHsCxxOdVylX5EvastTisO2JwnlHTLqPsm0PCl0D5USkW261fitaRHn84qVI1oKHszRO6EDgNNMgnj2nH4l4XMWP4fYGIRRDsVYMPUddQvZiyxXbhWMX9cHeqV1Aws4YKMsp4shaINaz-CzSgqgwGnIrSE8FQfaSLTFW8I4GvLRLW6WMQzxuhsActBKGcPuFapu9TZ-74f3Vc1UsNiVCIwHCVXzpPbwlGOA9o3mMtv20FVwHhtvZWID-nYev2McGoNEl1Nz7atS1b1fEu5wIQXnXCf6n-o7o36BPapw1rYBibtN9dVW7Xva_oJNYnh91vC6kiVmXpfi9GaIuwqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دریاچه ارواح نوشهر با فضایی مه آلود و ترسناک یکی از خاص‌ترین جاهای دیدنی ایرانه
👌
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/671734" target="_blank">📅 13:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671733">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
رویترز به نقل از منابع امنیتی و نفتی عراق: یک نفتکش در بندر بصره مورد حمله پهپادی قرار گرفت، اما خسارتی به آن وارد نشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/671733" target="_blank">📅 13:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671732">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfWUQjxmcwaZpd-XWI-X9kv2nPQNnZV4BFfEqCUVG_91kXc05zVDXyUu0Ew61Uv-kATILj2HlVNcs7h02Kl3McHeI2aeDqJ4i9oCKv3d3owOwT9vieMV3DJ64xTLLXzB2OaRWLjwJYSs6zcVYtT20ZDjpYWgVIl575_v9XuKHRwiyZ4sRFtfmtBiwDcjbFPZm1n7XH3xhmyuE7v5fdWS4JmWR2U1Cc5NazGpraGr-MHq1BILtHq5Su2iaOHBj5fH6wj3nIdcrPEenyyWGt3NhNUH-DbxbMNGltFW3vt6Iqoxm9RJyDpzhiQgG9GQxi9o5dl9ktTG4Fp1S4C2uSUAvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکوردشکنی قیمت بلیت فینال جام جهانی؛ میانگین ۱۱ هزار دلار
🔹
براساس گزارش فوربس فینال جام جهانی ۲۰۲۶ بین آرژانتین و اسپانیا به گران‌ترین رویداد ورزشی تاریخ آمریکا در بازار فروش مجدد بلیت تبدیل شده است. میانگین قیمت بلیت به
۱۱ هزار و ۳۲۷ دلار
رسیده، ارزان‌ترین بلیت
۶ هزار و ۹۴۳ دلار
قیمت دارد و گران‌ترین بلیت فروخته‌شده تاکنون
۲۸ هزار و ۴۷۹ دلار
بوده است.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/671732" target="_blank">📅 13:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671730">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lx9m1EFuL94JdvpSwUHURiJrtoaNo_3bb3Mv5XDLs0V198B72MZpIPjz8scbFyj1idpAWPzct2KDncw41g-nOL0qiB1cgEUHHwuMp9iOBD6CyveKrxM18iSYycMKw1ONkFLvzrYixqBGpNHpXpHVTbdxQb-8DO0FBmrcTJukN7dgulrk4ZrkU33CX4tciZEvf3kPlSVeEQUZceB5Z_NiuymMBtlPmRR2g4suhtb0zYW0TQ6q7X3LDu_Bbw6hagt6mWqVd1mmsw7qtYHj3gleUtsftdLUz0QEZI3w6dB-9CsoGpopi5cuPWpVhcjzvC68vUhma_hlzlXG0fFo9RMEAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z41uz_hMGHjWFsPWxLnYcPf3EB6vmRdTAv-psZyNxWInbe5NcITlVAblDuPqPUcyyH3aCcUe9oyOmSsziEcfLnhZ3S8ANnOg3S9fbueo3dpeTBDyJkeQz5mtEbDSD2kfZMVtkocrHCxE6KZefTuB72necPzkJeRE39zvhQOVY9P9AYCXkMVU3NuppqCCLilznv0JSWqKcovUud5tWUWVH-Sy0G8Al6HajXlVfu5Yk0FFzR5jkP9r9Qezfv8ZTEnWvVcBYB5ojkNGpx1FsQwSr4U7rpFWonaAPv-A4RlzkRJo9xs84xR_uvQH6V6Tg724uaDPVYk71LwQnsNIELM7pQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عمق زیبایی در چشم‌های یک نهنگ پنهان شده… فقط کمی زوم کنید
🐋
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/671730" target="_blank">📅 12:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671729">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahXC-5toZ6SsDtfmh-a7E9wjgc56xJJbDn7ucEYt1XAoFwfshkqTOMIr028ARjo3tm5Di6sX1moaTcNtE2e8Do4dHZis3Die3qB-WZee83-5aAE91TrST8FzrvVQVgswgFh-Tl9funBKSpohp6GFWip1cb0q9NahiM5VA_4t_JylxGe6z_fOVPJfmOpRWDL4fqyLJOq2P4BpdwUp45KGwVgb5lvZqUVuQVnTDbv1c1Bt7PpTYMFR8PkPFcX9gZ9AXI6EvbYeUDI1Oe5EZtnn8XTRS-BPXUYnQmQuOWUGJ4nng8A8DRD5qW-uYxlIrY8nb49UzHqKsmzvs35GNMHYjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله با انگیزه نفرت مذهبی در آمریکا: کارمند مسلمان در یوتا هدف ۱۵ ضربه چاقو قرار گرفت  پلیس ایالت یوتا:
🔹
فردی ۴۸ ساله در مرکز خریدی در سالت‌لیک‌سیتی، یک کارمند مسلمان را با انگیزه مذهبی و با ۱۵ ضربه چاقو به شدت مجروح کرد.
🔹
قربانی که تحت عمل جراحی قرار گرفته،…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/671729" target="_blank">📅 12:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671728">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7f25be81.mp4?token=Ym1qTn7YFM5-HTIYLdhWWoaM65R7JnKP5z-sfzZLSoPB-_UCwy66hePNuaXM-XW5wnUXhRCj0CkGVYW9MDToML-oo7aO6wS0vOXYrclRBKwf_MuUAWiYdw5CcKb7CX4W6YsYuPvOFA6EI_JPRye_53-1mm-c8B8RG1hlN0uF4KmJy3oZe_-hv8s-xSD92ySfZLlSB-2AkdA88qxROSZzPD6wNM9soveKwJo_SzMWvtPXh52fcrGzOQ7_xqLT5hgyokOyr3xQoEkfKoQg5yF0zyUgqR3NmU-EuFNLwQzdsqpKyGss6_93iQfBqCkyMszMeutchI7MtPy4N-ls-IFBoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7f25be81.mp4?token=Ym1qTn7YFM5-HTIYLdhWWoaM65R7JnKP5z-sfzZLSoPB-_UCwy66hePNuaXM-XW5wnUXhRCj0CkGVYW9MDToML-oo7aO6wS0vOXYrclRBKwf_MuUAWiYdw5CcKb7CX4W6YsYuPvOFA6EI_JPRye_53-1mm-c8B8RG1hlN0uF4KmJy3oZe_-hv8s-xSD92ySfZLlSB-2AkdA88qxROSZzPD6wNM9soveKwJo_SzMWvtPXh52fcrGzOQ7_xqLT5hgyokOyr3xQoEkfKoQg5yF0zyUgqR3NmU-EuFNLwQzdsqpKyGss6_93iQfBqCkyMszMeutchI7MtPy4N-ls-IFBoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار برای نخستین‌بار | بازدید شهیدان حاجی‌زاده و محمود باقری از شهر موشکی زیر زمینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/671728" target="_blank">📅 12:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671727">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
تلگراف: انصارالله یمن در حال آماده‌سازی برای بستن تنگه باب‌المندب است
🔹
تجارت جهانی با ضربه جدیدی روبه‌رو می‌شود
🔹
حدود ۱۰ تا ۱۲ درصد از تجارت دریایی سالانه جهان از این تنگه عبور می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/671727" target="_blank">📅 12:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671726">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
یارانه نقدی دهک‌های اول تا سوم واریز شد
🔹
یارانه نقدی مرحله ۱۸۵ مربوط به تیر ماه ۱۴۰۵ به حساب سرپرستان خانوارهای دهک‌های اول تا سوم در سراسر کشور واریز و قابل برداشت است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/671726" target="_blank">📅 12:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671724">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e611898e1.mp4?token=TFKjhimef3X3yMPwSs2_vWnu22vb5ucYaxwOIF8kJHEbWJ3sXD5LVEmyq80xUffDZYuhwHrsNwsajKKlP6-iaftD9GnyWuHnVfMa3Egmez7N2t3Oswa03nxaj_hL3CyH2yho2btePF0LONU6VujjvyyknhID23kgNdiSHb230bO75zJvbC04kq8tL8mE4fHm7OP959I4gC2fuaECEQ8UlnehCixFWuK-qUCV8MRrVWPo1RQ1IKQmydy58-5E2N3S6ziTDzBpUKfHizRfOTfzSSxV0JAqsfyMqac9CedAKbs2xNbWYdLrKbn_VgYI_h8nI4j12jhUGC-i6eLSS9yBNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e611898e1.mp4?token=TFKjhimef3X3yMPwSs2_vWnu22vb5ucYaxwOIF8kJHEbWJ3sXD5LVEmyq80xUffDZYuhwHrsNwsajKKlP6-iaftD9GnyWuHnVfMa3Egmez7N2t3Oswa03nxaj_hL3CyH2yho2btePF0LONU6VujjvyyknhID23kgNdiSHb230bO75zJvbC04kq8tL8mE4fHm7OP959I4gC2fuaECEQ8UlnehCixFWuK-qUCV8MRrVWPo1RQ1IKQmydy58-5E2N3S6ziTDzBpUKfHizRfOTfzSSxV0JAqsfyMqac9CedAKbs2xNbWYdLrKbn_VgYI_h8nI4j12jhUGC-i6eLSS9yBNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهار آتش‌سوزی در حرم مطهر رضوی
🔹
ساعتی قبل آتش‌سوزی در کارگاه صحن در حال ساخت حضرت امیرالمومنین (ع) حرم مطهر رضوی (ضلع سمت صحن غدیر) منجر به انتشار دود غلیظ و ترس زائرین شد اما خوشبختانه آتش با حضور خودروهای آتش‌نشانی اطفا شد.
🔹
موضوع حین جوشکاری و آتش گرفتن فوم بوده و هیچ خرابکاری و یا عمدی در کار نبوده است.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/671724" target="_blank">📅 12:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671723">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نتایج اولیه آزمون ارشد اواخر مردادماه اعلام می‌شود.
🔹
آمریکا تعرفه ۲۵ درصدی بر واردات از برزیل وضع کرد.
🔹
سازمان ملل خواستار کاهش تنش در خاورمیانه و بازگشت به مسیر دیپلماسی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/671723" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671722">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhPw9-3TgDUbCbQ9QSRB_TCD71y2qnOrk0cmginjjXrqlDBShIKHhWuhi_xr8ED0Ctn2XlVbYrRm1d8GpZfmyrlFqAutSNvxSihHgro_RLdKuL-ENZQZunveJ0V5mNKyQXAfRlRdPQTYoTXZxW7NJsF6vPN2JPH6sXAJqHpfC3XlFRgF7BHXBZYjy9-lPnSfv3V1IV8UcfwzijNhE6bGpUUwzYJG_TZ3tgBVdHUHhCkpIw3A4t-hiPcvIyijNnsrzt9bYeuOEMQlTyGMF6Dniy0MGSk_331nH1xaEbH99EXYRNpBdeyLcqxXEIGAYeKjrRRkRdoJrJsnMUxXzhoPFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
چهاردهمین نمایشگاه تخصصی صنعت مبلمان(لوستر؛ روشنایی؛ دکوراسیون و معماری داخلی)
🔹
۲۹ تیر لغایت دوم مردادماه ۱۴۰۵
🔹
ساعات بازدید: ۱۷ الی ۲۲
🔹
نمایشگاه بین‌المللی مشهد
☘
اخبار نمایشگاه بین‌المللی مشهد را در کانال ایتا نیز دنبال کنید
https://eitaa.com/nammanegar
☘
روابط عمومی نمایشگاه بین‌المللی مشهد
@Mashadexpo</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/671722" target="_blank">📅 12:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671721">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_5hr_RIHzzC3Rlkri2bBA1wipqoyhSwN--2MZyrOohRwYB9SGcNdyKTrjp3JN4zd-8A8k2phxLesFfx9QPxinyCgEaJXq-VBljORCs8MArDLJRtFrUeOwo2YrrpGJLEgsyxwe69cPVrRkjwkMCIHjtVQnjB6gBhWOeZHsqIK2VlBjQlMB4uOQuqcAYVtN4bhQo7jV8l3rdK3YxTp2JGfHF3oNtLqf58wuTmlfyjhsGFouaSrFDk7qnDt7oiGCfBASyPiyma0mv9M2e90z_uxPFiLS2yYJIRDj417Nkc9C4YUynxnvbmlk6qXNv4rsxKNY_x-EXNxJLTratmfFucLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مکزیک در صدر رشد جمعیت جهان از ۱۹۳۰ تاکنون
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/671721" target="_blank">📅 12:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671720">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aA4_jk89iBO5rvhauMB990irWCuOYG8EIjdniQAapA5_ULegRlq_nxAcbC02YDQrE13XNTyFvCnI2b6zC46ndaBLm-nSudiVrd3wFl8K7cl_eDgjOcfskMaaoZhD7JHFOv_AkAnC1icAy29o82j2bayzmuy8CNA_0LcBUWeTohxtNtdkK-oMT_dYayrWiLMsHqxlM9ymzl1XWwsXzj-rhNZG56YQCUm-tIudEIdcOpeLgrG7k7Da20Xv6n2TsAwAhj5BHqL_eTOh3TiJH9lNinNQ_GeyquZFrg1Wm8a-Lmbv38-HVAmXINZewirGMKa_bCO7pEmaSSz6QTGBhqfjUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علیرضا فغانی داور فینال جام‌جهانی بین اسپانیا و آرژانتین شد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/671720" target="_blank">📅 12:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671719">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/687172f5a5.mp4?token=hYO-PKf2nv5eWONilqkqBAru519LMbO8sVyyTzGs1tj3PPkY1a5AIdegeaug-8G_o1yBaUlTqqernohGpg0m5Xq_z37Dgb1Hgi6VPs4SN-g1OoWW6A_0KVOFf6WJZfXUWMI1AwlMjHZYyIfNBg5VIEbzMA0hytrRyQcvCkr0jv65wztWvEF5BtJpkv7CUT0tbbOOArB2UhpfL3Nn8kLkpimbu9xpLzPQCCMtyeGYhkUBDKbETpIaRvu-FcZeEWxRWQw9Vhjy34j1Jk1DVEYwIws4iMqZHPtsSgcd6E0zrEkNhiuJfHmcr0EH_zqPi0yNWtFaWQplbEETQGhpbLlXWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/687172f5a5.mp4?token=hYO-PKf2nv5eWONilqkqBAru519LMbO8sVyyTzGs1tj3PPkY1a5AIdegeaug-8G_o1yBaUlTqqernohGpg0m5Xq_z37Dgb1Hgi6VPs4SN-g1OoWW6A_0KVOFf6WJZfXUWMI1AwlMjHZYyIfNBg5VIEbzMA0hytrRyQcvCkr0jv65wztWvEF5BtJpkv7CUT0tbbOOArB2UhpfL3Nn8kLkpimbu9xpLzPQCCMtyeGYhkUBDKbETpIaRvu-FcZeEWxRWQw9Vhjy34j1Jk1DVEYwIws4iMqZHPtsSgcd6E0zrEkNhiuJfHmcr0EH_zqPi0yNWtFaWQplbEETQGhpbLlXWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گاهی کسایی که بدون پتو خوابشون نمی‌بره، دنبال یک حس امن می‌گردن! #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/671719" target="_blank">📅 12:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671718">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
لغو سفر نتانیاهو به آمریکا
دفتر نتانیاهو:
🔹
به نظر می‌رسد مراسم سناتور گراهام تا پایان ماه به تعویق افتاده است، و به همین دلیل نخست‌وزیر نتانیاهو هفتهٔ آینده به ایالات متحده سفر نخواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/671718" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671717">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
رویترز: شرکت‌های کشتیرانی به‌ طور فزاینده‌ای از عبور از مسیر تحت هدایت نظامی آمریکا در تنگه هرمز اجتناب می‌کنند
🔹
شرکت‌های امنیت دریایی هشدار می‌دهند که هیچ تضمین قابل اعتمادی برای عبور ایمن وجود ندارد/ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/671717" target="_blank">📅 11:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671716">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کانون بازنشستگان: ۵۰ تا ۶۰ هزار میلیارد تومان از معوقات افزایش دستمزد بازنشستگان پرداخت نشده است
علی دهقان‌کیا، رئیس کانون بازنشستگان تأمین اجتماعی در
#گفتگو
با خبرفوری:
🔹
۲۰ تا ۲۵ درصد بازنشستگان مستأجرند و با رشد شدید اجاره‌بها، بسیاری برای تأمین هزینه مسکن ناچار به دریافت وام شده‌اند؛ موضوعی که توان آن‌ها برای گرفتن وام درمان را نیز از بین برده است.
🔹
با وجود افزایش نیافتن برخی مزایا، حدود دو ماه از معوقات افزایش حقوق بازنشستگان نیز پرداخت نشده که ارزش آن به ۵۰ تا ۶۰ هزار میلیارد تومان می‌رسد. با توجه به کمبود منابع مالی، سازمان تأمین اجتماعی در شرایط فعلی امکان کمک به تأمین اجاره‌بهای بازنشستگان را ندارد.
@TV_Fori</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/671716" target="_blank">📅 11:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671715">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
توانیر: برق تمامی مراکز آزمون کارشناسی ارشد تأمین است.
🔹
آب و فاضلاب تهران: امسال آب در تهران نوبت بندی نمی‌شود.
🔹
مدیر اورژانس غزه: رژیم صهیونیستی بطور نظام‌مند کادر درمان را هدف قرار می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/671715" target="_blank">📅 11:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671714">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0UZRMXI-2AHhF1wHnOiNXvFNmERaUdOhS_szC5-GjjuFcJm2ohvkmQLDq-NPx8bcH5-9hAYnoVAN3iHT3Fe-Y8asKJkVwRp42-oxFmpUo9afxrzt8fhxCyZURTp8XwKWXg71WnObODJKTp2EK7tyFAnwCNptgXFw538J5l-_oCNYzm4GolTZsW5U85TasmvuscnYqiwBOFaoLKgunZ7Xr8_Fx--_Ve3oDP_ndHev1wERQ8gtNAv4SdJdm45or4D8Rr0GKw6ibOxO_NPgosrotn70MscnSFh5DpjKWiZ2_azBK1v6FxJhputxU-xQmdXBBTZpSxwyu9dqN423TcJnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف یک محمولهٔ سلاح در سیستان‌و‌بلوچستان
فرمانده مرزبانی سیستان‌وبلوچستان:
🔹
درپی توقیف محمولهٔ سلاح از قاچاقچیان که قصد انتقال آن به کشور را داشتند، ۱۵ کلت کمری، یک کلاش و ۱۸۶ فشنگ جنگی کشف شد.
🔹
تلاش برای دستگیری عوامل مرتبط با این پرونده ادامه دارد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/671714" target="_blank">📅 11:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671712">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سپاه هرمزگان: به‌دلیل انهدام کنترل‌شدهٔ مهمات باقی‌مانده از حملات دشمن در شرق بندرعباس از ساعت ۱۱:۳۰ تا ۱۴، احتمال شنیدن صدای انفجار ناشی از این عملیات وجود دارد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/671712" target="_blank">📅 11:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671711">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🏆
کامبک جنون‌آمیز آرژانتین مقابل انگلیس؛ انگلیس طبق معمول ۶۰ سال قبل بی‌جام به خانه می‌رود
🏴󠁧󠁢󠁥󠁮󠁧󠁿
1️⃣
🏆
2️⃣
🇦🇷
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/671711" target="_blank">📅 11:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671710">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
شادی کارمندان خبرگزاری آرژانتینی در طول بازی با انگلیس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/671710" target="_blank">📅 11:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671709">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afca301f1.mp4?token=JPn3MVnFyi3eqAWlrjSTCCJDjm2LB8w99JG6KT19-h7sqsQByBWpKs--RVIMKpJK3Y0lEjRMy_l9lBl4iet5vpwEM2SFflJpNwJnz_XaT_D_aFu2dPILP6GsxG49nsGJa9vmJzPU6s-HMyNnP1ZqbOgtp3FVp0IiHTuY8TDXuRV7EBloV8bMsdkuvWEv6VLcwZX11EWQ9tonmBbuailnmfRphc-_awK2ztgp-1PYppMZODXiTbOLg1Fcd1sr3zfDdmhtX_MTyf5jo2Iko3HBY6RgPIJeR5mRJWrr7XPFs8HuZOVQreVkNhgeeSrP0lpPK3UJRYGxqa4Txs1wmOuBgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afca301f1.mp4?token=JPn3MVnFyi3eqAWlrjSTCCJDjm2LB8w99JG6KT19-h7sqsQByBWpKs--RVIMKpJK3Y0lEjRMy_l9lBl4iet5vpwEM2SFflJpNwJnz_XaT_D_aFu2dPILP6GsxG49nsGJa9vmJzPU6s-HMyNnP1ZqbOgtp3FVp0IiHTuY8TDXuRV7EBloV8bMsdkuvWEv6VLcwZX11EWQ9tonmBbuailnmfRphc-_awK2ztgp-1PYppMZODXiTbOLg1Fcd1sr3zfDdmhtX_MTyf5jo2Iko3HBY6RgPIJeR5mRJWrr7XPFs8HuZOVQreVkNhgeeSrP0lpPK3UJRYGxqa4Txs1wmOuBgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات هوایی رژیم صهیونی به خیمهٔ آوارگان غزه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/671709" target="_blank">📅 11:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671708">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXuYrHLXrpT9V-YMn0HO1LM7hyXHvah_CXHh-nodHt0AbMqcIvqhROV2nH_vF1qQivuEeu5WISRHON_Knw8ddXj2T9FIu74PXGtn15Q7tWJmgn8R4MTDrBpwT13w1KEu5bC2NuLoFmOLcMBbdAPY-HEAAx_X49CnQOyKk9ncjw8s1_1LFkesjNrnelVv73YDaUqUmoKLtEwyUJsYAYW0q9RmMxKedXnwmXnlIDzjbTuUXkppx_k66xb-0sa9z2iBkHC5cm3luexayB1QeZIr2HszyOfhXkBUH1CfiqfUFUf9BEgrDXKsKbiygRoMiIWbWdvKEud5UL556Lo4Cy3NXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا آمریکا با نیروی زمینی می تواند تنگه هرمز را تصرف کند؟
🔹
طول تنگه ۲۰۰ کیلومتر است که به همین میزان مقابل سواحل ایران قرار دارد. عمق این سواحل به دلیل اتصال به سرزمین اصلی صدها کیلومتر است. برای بازگشایی تنگه و تسلط بر آن باید قوایی در نظر گرفت که بتوانند بر این جغرافیای بزرگ مسلط گردند.
دراین‌باره بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3230762</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/671708" target="_blank">📅 11:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671707">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بحرین درپی حمله موشکی و پهپادی به این کشور
🔹
ارتش بحرین: مقابله با حملات هوایی ایران؛ امروز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/671707" target="_blank">📅 11:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671706">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a706486b.mp4?token=PA9xSlYj0Fmhb_A6fvSdXuYHna5kRF5l1GI8kFwWup6Whso8hyFggrP8fDg5FQgLdnuEKSFMKPQQYWH5Km9sO6xu9TXl7KN7O-fnmnIsnB0SokW6ytndjvTsSeivB2DsQd97A1DlKGw_USne1No2_YjYYpFKQqSW4h2kvoOmlIdQuv3FsiTs74BsCGVNRScqnahUPUVmb4eQWI7463jzv0BfEz8Mrn6koWh3cwqpQmlmFUPwQEXij9kovDbHJ2VV4-puFGRz-9qjo3L2qUMoTsJfVj4y9k5sTDT5KxxCVG7q9tVp7UkEBNsBOmdiPvofEna_RbKiIxZzLQqc-97iUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a706486b.mp4?token=PA9xSlYj0Fmhb_A6fvSdXuYHna5kRF5l1GI8kFwWup6Whso8hyFggrP8fDg5FQgLdnuEKSFMKPQQYWH5Km9sO6xu9TXl7KN7O-fnmnIsnB0SokW6ytndjvTsSeivB2DsQd97A1DlKGw_USne1No2_YjYYpFKQqSW4h2kvoOmlIdQuv3FsiTs74BsCGVNRScqnahUPUVmb4eQWI7463jzv0BfEz8Mrn6koWh3cwqpQmlmFUPwQEXij9kovDbHJ2VV4-puFGRz-9qjo3L2qUMoTsJfVj4y9k5sTDT5KxxCVG7q9tVp7UkEBNsBOmdiPvofEna_RbKiIxZzLQqc-97iUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ست مولتون، نماینده کنگره آمریکا: «هیچ‌کس به دونالد ترامپ اعتماد ندارد... بیشتر مردم جهان معتقدند که گفتگو با دونالد ترامپ، اتلاف وقت است.»/جماران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/671706" target="_blank">📅 11:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671705">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb2WkH6N4bJWJa0znpDc8Z7aos5Zp1SVTFSqWcm5Ud6l1Se4ndvJWBGqMjwE9YQMTu5qHF-HQNl07898gEmKIhWaIIID_QqJ_cOUOfB-7z1OWpO98rMxWCCHX40mBT47dwEgBHOMvl_QoXzabIyCpSf1Amj9pNaYfhpWy2lVbqiPnqN2ccAV6v-kZXWEAebzJwWDzvkTU0Zj3nwqk8-QUZcCgNdKt01s1-xnkQuX8Bn1VlpJDhUeYB7s6i0dJ9Wg0EvPTB6Q73pS_9RDNjjm2G98TkoVl81kJLx9PQAGNvDhlVqLwHT29QXHVAf7j3F7N0KTA8C7iI9rc6u_oeGYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قابی به یاد ماندنی از حسین محب اهری، امین تارخ، آتیلا پسیانی، داوود رشیدی؛ هنرمندانی که حالا هیچ‌کدام در قید حیات نیستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/671705" target="_blank">📅 10:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671704">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سفارت ایران در انگلیس: حمایت از محاصره دریایی ایران به عنوان همدستی با آمریکا تلقی می‌شود.
🔹
صادرات سوسیس آزاد شد.
🔹
محور هراز  ۲۹ و ۳۰ تیر  مسدود می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/671704" target="_blank">📅 10:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671703">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCXEXqouiMEUZegho8XzRqZLN0pDBh28Vh-VE1Sj4MDX2e3BNg1XbmQoj57e8XIGxeFSabrKh_qpN3_gd9iMjg1aQvuDOWiXyCdijmrQbHfu1hH7vlcEzRVO7Ii1ZiQYXnYG1E1wxjxlnpF4IQVecvgHVvR_oKImFpjETeNdtenVKIuDcYpla1YnV7XdpJ0qNzrXkwUZcZeqqTPDHR5ejHNbZBu2fNlVkhrpY6pV27httUGIjXjPBHU6ZfZAFHRwnNADNhVE0r9UshxCQ5yZECiRcU2yDFDB3I-cnIyl2Hx9RYdGJNClRWcnR1A60MKFT7bCm4PEPLbNPoc2oRXKMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران قهرمان جام جهانی تکواندو در بخش میکس شد
🔹
در دیدار فینال جام جهانی تکواندو ۲۰۲۶ بخش میکس در شهر چونچئون کره جنوبی، تیم ملی ایران موفق شد در دو راند روسیه را شکست دهد و قهرمان جام جهانی در بخش میکس شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/671703" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671701">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9bfa53b18.mp4?token=YZ42gLEdQyANTRVQN9s-8jSmTCGWiwnx1q5m91aJ_tYsdL5guebgnYtbIAkGnGkzmf-RsBEGsaaQYZUKOK5oHJ6e7ym83yADp5cIRByl8bKApFoX9lE0Vx5X866G4bsHN2LbRsk_2or5iJCA8iiC7vaUQrMWyMTv_vXfYkTTVBoCfurW4rpdHkRUhkbXi1FRQ0JqvhUzdJR99tzjFAXdpYnrkWWVTUrP4fL0DW_xwM_7n54XPtmTg9OVR3UkpON0bYpKm8AEAwZgko2Tog7zj43W7mb4UAic4aJ9A7cQjj0BbLoQBN92l1coOtohU3xAiXBQ4eFrevJjnF_urCF-D4t3HwgNeXRhG1fxn73ma0FLYun2Vin7I34-mViwBVP-7kVp02F6B1usQmwRgCUm-PemZlkhmOJ9klzyP2RmlT3plyC1Da7tNuk0cQzSZbMuIkSgr6fFufxBJi0oFREDu1Hzh2ZB_csCYu4QMNDXqamRuUg6TR5IqWTbeiPsV_cGuorQPNBB9ypZECdmrDT_L-IzqdNomYjGeziabl6mTG6i4GXjYaMBNf6S7YBEwtlr_dKAArwYc9MI4gvynQ5slmzbFJNNFKOgLTAtGOy-L7iUVoZqVQOnLTIiu7mCCEFlrBpnVZtww0hjeGHt8t8LIRUbwlrrjCnOzkpZtqxDnTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9bfa53b18.mp4?token=YZ42gLEdQyANTRVQN9s-8jSmTCGWiwnx1q5m91aJ_tYsdL5guebgnYtbIAkGnGkzmf-RsBEGsaaQYZUKOK5oHJ6e7ym83yADp5cIRByl8bKApFoX9lE0Vx5X866G4bsHN2LbRsk_2or5iJCA8iiC7vaUQrMWyMTv_vXfYkTTVBoCfurW4rpdHkRUhkbXi1FRQ0JqvhUzdJR99tzjFAXdpYnrkWWVTUrP4fL0DW_xwM_7n54XPtmTg9OVR3UkpON0bYpKm8AEAwZgko2Tog7zj43W7mb4UAic4aJ9A7cQjj0BbLoQBN92l1coOtohU3xAiXBQ4eFrevJjnF_urCF-D4t3HwgNeXRhG1fxn73ma0FLYun2Vin7I34-mViwBVP-7kVp02F6B1usQmwRgCUm-PemZlkhmOJ9klzyP2RmlT3plyC1Da7tNuk0cQzSZbMuIkSgr6fFufxBJi0oFREDu1Hzh2ZB_csCYu4QMNDXqamRuUg6TR5IqWTbeiPsV_cGuorQPNBB9ypZECdmrDT_L-IzqdNomYjGeziabl6mTG6i4GXjYaMBNf6S7YBEwtlr_dKAArwYc9MI4gvynQ5slmzbFJNNFKOgLTAtGOy-L7iUVoZqVQOnLTIiu7mCCEFlrBpnVZtww0hjeGHt8t8LIRUbwlrrjCnOzkpZtqxDnTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر از یک کشتی مسافربری که ارتش آمریکا آن را منهدم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/671701" target="_blank">📅 10:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671700">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVx1JRFzyY_cCHk84xb7PsYP-ksMxMPwJ-CWg82r9cG_icuNYdvL1y06qHqAJRD1_MiTRAHx-_0Vza50fSyIGoXC98KcjY6SdioUDQ6hGFqIDPZfu3mfeq3BHY0sngRrY1byzYXG4VeOWRM_8fK5JazbQGoQX2tSbuYX-imuzjNQ0zEwYjCOjz42siNmByLHtR6P1wr-CgN7LbL5D1v0p31zrhlH0-K1KaHkVDYMG4UXip7fbJLdvmSNYNOQ6iJ6AXVwguU7vl31654NUf81ddcC87dqxUbw0iEhJJXgwgXA8Ca3CO_R-wR1vsSHk2gCp8jCOK5GYgOPD-V41ZLJ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کشف جالب مسی و یارانش از گلر انگلیس
🔹
بازیکنان آرژانتین پس از پایان بازی با انگلیس به‌طور اتفاقی بطری آب جردن پیکفورد را پیدا کردند. او تمام عادات پنالتی زدن بازیکنان آرژانتین را روی این قمقمه یادداشت کرده بود.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/671700" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671690">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m_o7oIX5XpavsLupQk0zGnN6ixnv5LE865VVD-W7Ado2dbPMxNm7A1pWMQgQd74Tn9GoRB3Dnutn38x_qSOR9j3hv0_pjDXfyO33zASWcTLKZ1SSfZnMoK2TRCHOnJBLcELKLvcvyufMErZaKSc5E4SjgGlsX3oor4WBpM5-gkcp2DAmvKUF11x-vbBrYglVFux7-2iuFHHakI9MRvHoukzFHuuT9VsmGQmNdHYvYa1Dq8gIvLpEF7_PnmPTzuPOaib1h5MJcS1jHbepIU3bsQueo7hF7tHW-vER2_TBRi2Ng7fKOinQGWDwwOUU6_pBk1VhZrSITeZlOly8ylTXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mDsSxYaHhnaw9UQb9A0mi6sbTKNfQNFyLV1EklmM_HFWHnCmQvR4JGDDa2QWqQydyUqgGYbM93aAEbSK2i0C-f1s6GPCy0phDoRtJfLk-fllu1zDt-eUcw2scCXAYNgbgidnCdttLg1c02Pw8HGIN98vjxp1KKwMiPG2PfqxfL6dSVmH-YePMQDkzkPX_trx7ZP8gnCPby3d3m6Fw9DgKc9OTMnD33HHK1gAPMSozcoR1-gPXsQIdz5m5rYVYbhWJVpLv2OJlNHLzxjMyvQc54KUAkgh-alMzOc38l2BPhAfTniFYkd_rNA3IA5l7-UnptbHsdVSk7O3WOYiQTjWvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uyO7-3j_ibFcfNklyOONqcp4kbDBPB5S7drhtoCyb_djGC-BmCJV5MRJOhzw_Rzi0fv1WBIVODtyTUF_ZmlbQyQEyVWJ1FMV-QK3Yq8u6WYzLwIYJ_U2KjtWqSp_LczPrtDeXRJk1cgOQKbJCNnx3qu9-HADEBBenGFfpSrS6KSy9Hu9vSy5dxM6Oo22Oxi2NEtnnZFVHruoafNdU9e8d3yy0Tcwh1-Me9ZKJw9LYW-ksBwV4IJnQnnsIHnxhZ2TfaPovucjxwkT3MXgNFve6FQ1tzPRzt3ngFNSXzgU6B6ZuXPmG0zkplCBPD6OWiXe2j1kg6bFcAEVk2OdIpvTog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hE-7prwvPA69XbP73pd6EZSkKNBLOjpl7anyo8fd4jc2hu6dpn4t1GmCtx-VbfLCBMA5Ru3XvtS_4CzwxOn67KHkMRUluv0bxiCxyEbEw58VR0C7GaQZi2fFuyHkoZbeHDNiauUh7-FYoKboNDI5QubCiSCXcr9jYVbyNf2SRroURTd4DzsQeGtUksWO_bkN0iysAvfC7s3RHZR0rQHvniii3iOzwmBO165QYnMMoVWEA4kxvLNf-qPh1MjccRLDNR0ibrDBWh1cy36I0mDMVXcls1gR8RFDIDaRoGeysr0cuMXMkt4frma8k1gowOvVp4GHK1p04ocZbqThr196NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMI2bKMOVoh6HUR8BG2WG-mMrn4kEMtCL8JIOBl_rQmkB7csHB-biu-2g7CNyC2orkNhdUEh-NrD_UqKtVrn6xor_JiTctixzmoszP0rtYP1ndJSM4BemvRSkcPwGSwLm6O5Bzd8C3VpkeqAVt2TX8MmVYZ-5jbDz2B7bIJZOrd1AsODKv-fy63vhzF8M_1h4Q5AUuwvcEb4dnDNmW7EgPhETeSdY3KA8DZizoxIs7xhx1556ukaYQkY4H0GUmAhQX50YWtapdP_7_u9UllYhTiuCaejtkhWud33borXwCy4-f5u1TLgZWwRQmheSJixYlxbpysUtIbW-jAw4XG4hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/idhip0qeiGqgx25pO_1Y92ieSjvbWEmyfnMsIB4DR3qRP9Kcuh08qsebITyEeOjHuPyVxAM4p_4iCHLg9VvgZoGd68c9yBYJuEpOeSgOW2UEPuUlHBZz7WGau2Y4q9f0XSa0ug0cHOJ06uHg-e2VQH53-eExL1_b_kXDHp99xT4CH2YGTESyThsXHdS3BY8DDS5Asy5frjmaN67MGELrXTYWLgNuTLR01YAdS9_JGx_JsxjU43mRF50n7JLkN1vtP3sHaw_4vyuW2MULOvL_emNPgf3JQDTB8rfvRY8n73uAPZ71qmApYFypFUF6ILNuYGt7xB7E8O03ex8fGAHhSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVYx9G_6cOYGf9l-lvBjZRLEg7qeY2laYmCZm8oCelubXMEIAsXPYP-2b_o3GK2uIuDUY4OZHqDxUQwhq9KA3Kr_4WOvg9VSq217OL3_KLcdOEoZ5Mv5_y6QQ9PA5EqlrvXZMZtmpNVAH4G7p6yINCih7xByVhDYQfcWH-iXsRmS2AQja8mNn6qS2eBN5J42RCE7nsCBqtp47oTgtk5rYdg_AayTkoO4ufrKoDN0omh_x1FQnIVgMtIvzHsuuaeJQmUD5GIq_gUki85EKcf2kcEYLfmUTJ4CUnu90zOuHg1b52w6N_gZZ1S2r22NrbSGN2q3WCH6rdaSiuWyU_pDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3ybDoRCU2zOWuqQhMGghbmcvIEU2J49FYqxcIfwmNJUfiv57H2JOMYUB_ZOCTbmxcEhEE81Bgiq9KW6RX7HgBHUYi-bMhAZWZabQ3DBshwcli35IRjEkOvSJfAUT5PhY83nAw7glXKFKAvh-0IZ36kBZOMPb6f3JifaETvnwbkI58dmRioUK6xZh_B6SjiyiHidEzMS1rPmPYl7ziH8e5GSUAzW9giOup-hdKf94TTK7BLAs7oAWzm14wbsNfUJv2Tq1YF96EoYiflYHq37_aCeamEHKoOc5JyDr4YXfTyoEmTuuUzlBDzhqVKmUnMqohmd5HOZMLC-qnnv_Dsnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTdZbv4s046q47SgeIxkvCc7hhJRWnKOVnwwTowAbThTMFPhilD_hmetDoPSGogq9WASkFc5SRAhWQJsIV6y2pDmWKN85qndWUfh-rQn1-GlzZPiYG3-V-lgABkU2OGgHbLHJgqOiVPaAh0T-itPIhhjihFOlOPc_yROpwogu-Ki0KcO4KSG7RsYMBzDBNsu4kRPY0dig1gXRa_1pk2GOIugBLJ7pyXeNPpBxb689XsS42DbZMgHsx2l4b9Gl9NZVKfTbpY2ZRR7LQqMLozlJlngaTVjKvHZSVSrOqQziDRpizQdPfjihwjGI1qfFuBC9omuNpb_nb7kTVzB_hmrkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnhJtXs8sXkOXbRRF0nEzXtnzE0QNmPGhyZpnjKha66Az64RVentjqw760QYkanr0pSKTkA87GcJhdMK-Ddne3OWJWJNhQ58L9DeWxcJN973NII2YojMA-5YLjoTqaJQ5yzVVQ31dSF4m1n0zi5vsHYXlSSJbyJItDbSvtRgtaYrBhskvzh_hDiPqNj952fr_8O4m41UNRzM3pHYphe0lS_byBirlF9trWBgelmuR9iR4io4JW-meJtuTG2-LBjdJbXnqLKHri4D7PxbnU4igjY3an9Pho_LPmIDXzsV4l2iG7zAFBFAXNf5W5QPOBdi-0OYVbJuaXD70sGDoco11Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بخشی از پیام‌های ارسالی مخاطبان خبرفوری در خصوص قطعی برق خارج از زمان مقرر
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/671690" target="_blank">📅 10:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671689">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
پاکستان خواستار خویشتنداری ایران و آمریکا در تنگه هرمز شد
🔹
سخنگوی وزارت خارجه پاکستان با تأکید بر لزوم بازگشت به وضعیت عادی در دریانوردی، از طرفین خواست با خویشتنداری، مسیر دیپلماسی و گفتگو را برای تأمین صلح و ثبات در پیش بگیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/671689" target="_blank">📅 10:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671688">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
سی‌بی‌اس: ترامپ از رد پیشنهاد توافق هسته‌ای ایران ابراز پشیمانی کرده است
شبکه سی‌بی‌اس:
🔹
دونالد ترامپ در محافل خصوصی، واشنگتن را به‌دلیل رد پیشنهاد تهران برای محدودسازی برنامه هسته‌ای مقصر می‌داند.
🔹
او معتقد است این تصمیم، فرصت کلیدی برای جلوگیری از گسترش درگیری‌ها را از بین برده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/671688" target="_blank">📅 10:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671687">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
بهترین دستور مرغ سوخاری رستورانی همینه، امتحانش کن
😁
مواد لازم:
🔹
سینه مرغ یا فیله مرغ
🔹
ارد ۱لیوان
🔹
نمک، فلفل‌سیاه و قرمز، پاپریکا، پودر سیر و پیاز
🔹
یک عدد تخم‌مرغ
🔹
نصف لیوان‌آب #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/671687" target="_blank">📅 09:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671686">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
سپاه: مرکز ارتباطات ماهواره ای و رادار هشدار اولیه پایگاه هوایی آمریکا در علی السالم و اسکله نظامیان آمریکایی در شعیبیه کویت منهدم گردید
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/671686" target="_blank">📅 09:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671685">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c61d032f9.mp4?token=SDvKgoRGJHZ3g40DrWIluP1lYl1DLfZBsHrXZxbuZ1QaFlJAEiUWfNXnCwFpP38S0S5_6qk7aI1CjEEsOEj2PMN5KqZzJ70wgYFUXbEij9Cex4gfXYJWGjQyYgJyB_GDBn50_7bNbHCfnIh6c23R3KCNS6zim1vbHS5hmM3x-24ELrCEIpkVtuN2IGJkQ3GOn2n8H-pQ5UrKKNfxAWYHJgT7qjmyJ_1u8L5ewpCKGZcgH4fG31N4fA2gAm_bdCjrgB8I-Xnqa3xiH58Nm6OM6NEAW_e_I7IhM2V1e0iFvfGKE33pRnKU3hjGl766a3W_I_nxJVJuXXz0Y4T5garJ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c61d032f9.mp4?token=SDvKgoRGJHZ3g40DrWIluP1lYl1DLfZBsHrXZxbuZ1QaFlJAEiUWfNXnCwFpP38S0S5_6qk7aI1CjEEsOEj2PMN5KqZzJ70wgYFUXbEij9Cex4gfXYJWGjQyYgJyB_GDBn50_7bNbHCfnIh6c23R3KCNS6zim1vbHS5hmM3x-24ELrCEIpkVtuN2IGJkQ3GOn2n8H-pQ5UrKKNfxAWYHJgT7qjmyJ_1u8L5ewpCKGZcgH4fG31N4fA2gAm_bdCjrgB8I-Xnqa3xiH58Nm6OM6NEAW_e_I7IhM2V1e0iFvfGKE33pRnKU3hjGl766a3W_I_nxJVJuXXz0Y4T5garJ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار قاطع سخنگوی قرارگاه مرکزی خاتم‌الانبیا: زیرساخت بزنید، هرچه زیرساخت در منطقه باقی‌مانده را می‌زنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/671685" target="_blank">📅 09:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671682">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33412fc12.mp4?token=KO42oax181Rgsrw7u6N8xPIh1IgkeGyCUOFAASxFQ7wi_05KR74zYvzspMwpOCgPPBa7Wr0flZBsPLFkM44KYTD4TGtmnXe8ubffaQ1HoXsAFoiHJqXVh-nP2fwn0iMYHa7h0oxvkGvdc7lI7UGcS5CoM01YZXJIa42qHXOPXFsCp48x4Omq3ltlVAdSXIg1hyLgRQtsNrIrNWAUx6ggW7DeXgKjQk-ZqeTGPacYxKJEKf7RaJvisC71t6bMgErBR81UZDSjJjnnl69aoNBKML6K_jSgnhrorFElEcxA_h8yKEBFxMCg2l1vDqIs8dNBlyoxE7UsZwTmmaMFpZnJhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33412fc12.mp4?token=KO42oax181Rgsrw7u6N8xPIh1IgkeGyCUOFAASxFQ7wi_05KR74zYvzspMwpOCgPPBa7Wr0flZBsPLFkM44KYTD4TGtmnXe8ubffaQ1HoXsAFoiHJqXVh-nP2fwn0iMYHa7h0oxvkGvdc7lI7UGcS5CoM01YZXJIa42qHXOPXFsCp48x4Omq3ltlVAdSXIg1hyLgRQtsNrIrNWAUx6ggW7DeXgKjQk-ZqeTGPacYxKJEKf7RaJvisC71t6bMgErBR81UZDSjJjnnl69aoNBKML6K_jSgnhrorFElEcxA_h8yKEBFxMCg2l1vDqIs8dNBlyoxE7UsZwTmmaMFpZnJhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیمه نهایی جام جهانی| کامبک رویایی آرژانتین با درخشش مسی؛ تعویض‌های تدافعی توخل کار دست انگلیس داد؛ آرژانتین رقیب اسپانیا در فینال شد
🔹
آرژانتین ۲ انگلیس ۱
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/671682" target="_blank">📅 09:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671681">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سپاه: در «موج هشتم عملیات نصر ۲»، با استفاده از موشک‌های بالستیک «خیبرشکن»، رمپ جنگنده‌ها و مرکز فرماندهی ارتش آمریکا در پایگاه «الازرق» اردن مورد هدف قرار گرفتند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/671681" target="_blank">📅 09:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671680">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
سپاه: در «موج هشتم عملیات نصر ۲»، با استفاده از موشک‌های بالستیک «خیبرشکن»، رمپ جنگنده‌ها و مرکز فرماندهی ارتش آمریکا در پایگاه «الازرق» اردن مورد هدف قرار گرفتند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/671680" target="_blank">📅 09:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671679">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be48491e1.mp4?token=paVM5Uu3ELt-t4cLDhuwCFFzn0X56SYNwj9w1ZJvEul7mwGTn0rT_rm3WfFM4cdmh5wwpVAFLXp0j2l1LkgyBwrhAWklgot3szEGx2pni_e8mRR1nCZjtAiV5gBFDlDyWJq6Vuu8ypkFsfI6Abdc3AU9GNUip1rZdIZJAaRLqraaphTIiryBFkW4kfE40B5JajduOuGmQ2qN2yoXGKapcqSyx47wctjtx7WYzxWopL3RsxC5gK0bShEX4N7EwbTQB6R0J47_4eFF3MK5Uwn8kbqvdBLQIM3dJeKLA1LUG9vvv-IXddLw21GMThAZ91Xyb5BnDm623kbTd3wxk_b5cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be48491e1.mp4?token=paVM5Uu3ELt-t4cLDhuwCFFzn0X56SYNwj9w1ZJvEul7mwGTn0rT_rm3WfFM4cdmh5wwpVAFLXp0j2l1LkgyBwrhAWklgot3szEGx2pni_e8mRR1nCZjtAiV5gBFDlDyWJq6Vuu8ypkFsfI6Abdc3AU9GNUip1rZdIZJAaRLqraaphTIiryBFkW4kfE40B5JajduOuGmQ2qN2yoXGKapcqSyx47wctjtx7WYzxWopL3RsxC5gK0bShEX4N7EwbTQB6R0J47_4eFF3MK5Uwn8kbqvdBLQIM3dJeKLA1LUG9vvv-IXddLw21GMThAZ91Xyb5BnDm623kbTd3wxk_b5cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویرانی گسترده ناشی از حملات وحشیانه اشغالگران صهیونیست در شهر دیر البلح در مرکز نوار غزه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/akhbarefori/671679" target="_blank">📅 09:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671677">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
سخنگوی ارتش: تنگه هرمز تا به رسمیت شناخته شدن نظام ایران بسته می‌ماند
🔹
امیر اکرمی‌نیا ضمن تأکید بر حق حاکمیت ملی بر تنگه هرمز، به همسایگان درباره عواقب میزبانی از پایگاه‌های آمریکایی برای حمله به ایران هشدار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/671677" target="_blank">📅 08:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671676">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
تکذیب شایعه حمله به ۵ نقطه استان کرمان
🔹
معاون امنیتی استاندار کرمان با رد گزارش‌های فضای مجازی، تأکید کرد در پی تحرکات اخیر در جنوب کشور، هیچ نقطه‌ای از این استان هدف تجاوز قرار نگرفته و اخبار منتشرشده کذب است.
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/akhbarefori/671676" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671675">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
حملهٔ بامدادی دشمن به کبودرآهنگ همدان
استانداری همدان:
🔹
بامداد امروز نقاطی در کبودرآهنگ مورد حمله قرار گرفت که این حمله آسیب انسانی درپی نداشته است.
#اخبار_همدان
در فضای مجازی
👇
@akhbarehamedan</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/akhbarefori/671675" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671673">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adefafbaf.mp4?token=MvPj54VqEv0tjgHELf6AO2iu0gbVwUEtaVkLwAKXiWVz3lqlSRJT1OoUSYiX6gi-oRqvdMda19kOh6xniojyZqqvUhPV-1mEcMzVMGhbyVJeDnAp4BWe-xBNhZSZFwzksxyOKvhAI_REsQxwL5Pzv-8Ee8v3PlzVNxGvmup1KeiohFbQjeftMODvuaC9S7DZM2o4fnvBm7lQF_R__DqLtegTH3Hao-8FaA0rlyzj4LJrYO1pFKaLDavMLyYroqitLtphaoePeTFbM_g-TjoleaD4u1Fb5YqzBxqdmJQwLrTBWUCfhKeECcdFKdVkrHnynhG4wIlMym9Uf58JbUOIpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adefafbaf.mp4?token=MvPj54VqEv0tjgHELf6AO2iu0gbVwUEtaVkLwAKXiWVz3lqlSRJT1OoUSYiX6gi-oRqvdMda19kOh6xniojyZqqvUhPV-1mEcMzVMGhbyVJeDnAp4BWe-xBNhZSZFwzksxyOKvhAI_REsQxwL5Pzv-8Ee8v3PlzVNxGvmup1KeiohFbQjeftMODvuaC9S7DZM2o4fnvBm7lQF_R__DqLtegTH3Hao-8FaA0rlyzj4LJrYO1pFKaLDavMLyYroqitLtphaoePeTFbM_g-TjoleaD4u1Fb5YqzBxqdmJQwLrTBWUCfhKeECcdFKdVkrHnynhG4wIlMym9Uf58JbUOIpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش‌های سیل‌آسا در شهر العین امارات
🔹
بارش‌هایی که در سال‌های اخیر به دلیل تغییرات اقلیمی، وقوع آن در این منطقه افزایش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/akhbarefori/671673" target="_blank">📅 08:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671672">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
علی اکبر ولایتی: تنگه هرمز متعلق به ایران است و هیچ قدرتی در دنیا نمی‌تواند تنگه هرمز را از مالکیت ایران خارج کند
مشاور رهبر معظم انقلاب:
🔹
این تنگه با فرمان شجاعانه و خردمندانه مقام معظم رهبری، حضرت آیت‌الله سیدمجتبی خامنه‌ای (مدظله‌العالی)، به‌عنوان یک دستاورد ارزشمند از جنگ ۴۰ روزه، تحت حاکمیت ایران قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/671672" target="_blank">📅 08:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671671">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
اعتبار کالابرگ سرپرستان خانوار دارای رقم پایانی کد ملی ۷، ۸ و ۹ شارژ شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/akhbarefori/671671" target="_blank">📅 08:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671670">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
‌جزئیات حمله بامدادی آمریکا به سمنان  سخنگوی ستاد بحران:
🔹
بامداد پنجشنبه، بخش‌هایی از فرودگاه سمنان هدف حملات هوایی دشمن قرار گرفته است
🔹
خوشبختانه بخش‌های مسکونی در شهرها و روستاهای استان سمنان امشب شاهد حمله‌ای نبودند.  #اخبار_سمنان در فضای مجازی
👇
@Akhbar_Semnan</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/akhbarefori/671670" target="_blank">📅 08:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671668">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
وزیر علوم: کنکور سراسری در زمان مقرر برگزار می‌شود
🔹
برای برگزاری آزمون، هماهنگی‌های لازم از تأمین برق حوزه‌های امتحانی تا هماهنگی‌های امنیتی، با دستگاه‌های مختلف انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/akhbarefori/671668" target="_blank">📅 07:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671667">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc6d27d3b9.mp4?token=DOyzYNe6N-xn2HuQpviccguUkAdxhxAZx7Ea-2QeFxN-S_wss_hazmy_mWQ6_hemz5lhUAjRQHY9Fu4Q5d4InQYFFDo85C2QVqa26zGTn4avReqPF_Rri99gh-k0m8O1rtB4lmgGcay_ObacCRmXKJX_g8alU8FZHvC9ZtPGKsyfb9a0UFG8umzpClz3ssdqEpMD3hov7OnyEFeK80QptVN0LpZScU-ChYsmkTxtLrloCvXfOQGKV9REo-QnvAJ2rGKWDjvA7ZsGQa_Y92-JfyBK-yAQCFLtDuz1EO-gWeliCftoFB7aPMa50VUhOtFCoBDKJWo-zWdmLutmypuyInKuFXKTOXtHAybqa_oG3C8QViTZ3ZWudagIf1jno31p4LlAioOVjQzCKiCjuFx9R-qC-mqwR2yjQfp7wyTqCH9OY3uqunmKrcPnt9OwnG8NwjB2t0e0b55dEqpA3oSwFfXD-wn8Y9DrTZVyRjsO44V5CPlOmMhVxyePyi1qKgo0i_VH1wyhiSuBlHEJrzemViDlrANgeUCEjdNxUngOtShYhcOEaGRLhnBgxX0Wf1JnidB8wNQLCp5BhEMH9NH0LvdNhGN8KTl4EF1MkdJRYnwP9Re0vFAnLFLLUeZQNm3zWK0WqC8u2B6abSJbKXAiU5M9De0sQH0elmD5YElyCg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc6d27d3b9.mp4?token=DOyzYNe6N-xn2HuQpviccguUkAdxhxAZx7Ea-2QeFxN-S_wss_hazmy_mWQ6_hemz5lhUAjRQHY9Fu4Q5d4InQYFFDo85C2QVqa26zGTn4avReqPF_Rri99gh-k0m8O1rtB4lmgGcay_ObacCRmXKJX_g8alU8FZHvC9ZtPGKsyfb9a0UFG8umzpClz3ssdqEpMD3hov7OnyEFeK80QptVN0LpZScU-ChYsmkTxtLrloCvXfOQGKV9REo-QnvAJ2rGKWDjvA7ZsGQa_Y92-JfyBK-yAQCFLtDuz1EO-gWeliCftoFB7aPMa50VUhOtFCoBDKJWo-zWdmLutmypuyInKuFXKTOXtHAybqa_oG3C8QViTZ3ZWudagIf1jno31p4LlAioOVjQzCKiCjuFx9R-qC-mqwR2yjQfp7wyTqCH9OY3uqunmKrcPnt9OwnG8NwjB2t0e0b55dEqpA3oSwFfXD-wn8Y9DrTZVyRjsO44V5CPlOmMhVxyePyi1qKgo0i_VH1wyhiSuBlHEJrzemViDlrANgeUCEjdNxUngOtShYhcOEaGRLhnBgxX0Wf1JnidB8wNQLCp5BhEMH9NH0LvdNhGN8KTl4EF1MkdJRYnwP9Re0vFAnLFLLUeZQNm3zWK0WqC8u2B6abSJbKXAiU5M9De0sQH0elmD5YElyCg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله دهم عملیات صاعقه ارتش؛
پایگاه ها و مراکز آمریکا در کویت و بحرین هدف حملات پهپادی ارتش قرار گرفت
🔹
ارتش جمهوری اسلامی ایران در مرحله دهم عملیات «صاعقه»، سامانه‌های پاتریوت، رادارها و مخازن سوخت پایگاه «علی‌السالم» کویت و تأسیسات راداری و ارتباطی پایگاه «شیخ عیسی» بحرین را هدف حملات موفق پهپادی و موشکی قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/akhbarefori/671667" target="_blank">📅 07:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671666">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
گزارش سی‌بی‌اس از تدارک پنتاگون برای حمله به کوبا
شبکه سی‌بی‌اس به نقل از مقامات آمریکایی:
🔹
پنتاگون در حال بررسی طرح‌های حمله هوایی و تهاجم زمینی به کوبا با مشارکت لشکر ۱۰۱ هوابرد است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/671666" target="_blank">📅 07:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671665">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0I1oSSzID1YXjsC3ISpzDdyFLtzeUZIIVmpb6SCUoGIqtylJDRKprjF8omEfAaBBIyHEeo7ZKE-8U6eGKYSgRFDZ7FdMW-QvwXT6Iw-Ks9pHu2FEmZ15mQ4t3mtytZB7eWIaELbXCGHepcxa0CaHTTlL4vUP8mQOkiL5PRt-HzQ0k4s1yeMx167KN5jBK670awwqcSN0R-1ODrilDcKUIouvKWOl9_qvFG9liBdsWUakfcLsY6tps2dC6SqkkhIvlL96q9f1ZT1G02JDuee3v3UMo0Yrw4nIbXQ5oFAP1UuxdlwGYHS5-dQwTXGOb4kRTzUG7MGr9kRcF8W8xnWZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۲۵ تیر ماه
۱ صفر ۱۴۴۸
۱۶ جولای ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/akhbarefori/671665" target="_blank">📅 07:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671664">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
صدای شنیده‌شده در خرم‌آباد مربوط به پاسخ موشکی نیروهای مسلح کشورمان علیه اهداف و منافع دشمن آمریکایی بوده، و جای نگرانی ندارد
#اخبار_لرستان
در فضای مجازی دعوت
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/akhbarefori/671664" target="_blank">📅 07:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671663">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
خوک هار در پست جدیدی مدعی آزاد شدن یک جاسوس آمریکایی توسط ایران شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/akhbarefori/671663" target="_blank">📅 06:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671661">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf67f9770.mp4?token=lPwcM5iJUAGGz0qrocqBxMU-Z5w-IDlo2KkoPucTm4GW4ZgHxoiNvqi3Y-pcF7h3nOkxIj8AzQCDvLutK0iveYhryWPIb2SrzvGRboE0XdKlwvRDNrVkjpyRTr8dltB_6JDDmeWfT-NTQBCAav35t_FaSYiT5ynQb-A09W38z0z1O6eo02pL8NIHomMpjmEhrT1ykIMOvrmAWj5456I_g5FQhAxIVYEU2Q6-o0PULAwgd9xpp5iRbbvZFrd-qPiMvRJK-l7Dkln4sOMT1VvTofRUfJQqN6kgbouw_OrcAVPaSPHj1KHVJ34rsT4cXffyF5GNq2imfQNPYzEB-7PX5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf67f9770.mp4?token=lPwcM5iJUAGGz0qrocqBxMU-Z5w-IDlo2KkoPucTm4GW4ZgHxoiNvqi3Y-pcF7h3nOkxIj8AzQCDvLutK0iveYhryWPIb2SrzvGRboE0XdKlwvRDNrVkjpyRTr8dltB_6JDDmeWfT-NTQBCAav35t_FaSYiT5ynQb-A09W38z0z1O6eo02pL8NIHomMpjmEhrT1ykIMOvrmAWj5456I_g5FQhAxIVYEU2Q6-o0PULAwgd9xpp5iRbbvZFrd-qPiMvRJK-l7Dkln4sOMT1VvTofRUfJQqN6kgbouw_OrcAVPaSPHj1KHVJ34rsT4cXffyF5GNq2imfQNPYzEB-7PX5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش جمهوری اسلامی ایران، ساعتی پیش در مرحله نهم عملیات صاعقه و در پاسخ به تجاوزات دشمن، سامانه‌های ارتباطی و مخازن سوخت ارتش تروریستی آمریکا در اردن را با پهپادهای انهدامی، هدف قرار داد
🔹
پهپادهای انهدامی ارتش جمهوری اسلامی ایران در مرحله نهم عملیات صاعقه و در پاسخ به تجاوزات دشمن کودک‌کش به  مناطقی از کشورمان و پادگان بمپور ایرانشهر که منجربه شهادت ۷ تن از درجه‌داران و سربازان نیروی زمینی ارتش شد، سایت راداری ثابت، سامانه ارتباط و مخازن سوخت ارتش تروریستی و کودک‌کش آمریکایی در پایگاه الازرق اردن را هدف قرار دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/akhbarefori/671661" target="_blank">📅 05:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671660">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۵/
رادار پیش‌هشدار سامانهء C-RAM در پایگاه علی السالم کویت و نیز محل تجمع سربازان جنایت پیشه ارتش تروریستی آمریکا آماج حملات ترکیبی قرار گرفت‌
.
روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
مردم غیور و بپاخاسته ایران!
در پی تجاوزات شب گذشته دشمن به نقاطی از سواحل و شهرهای جنوبی کشور، فرزندان دلاور و قهرمان شما در نیروی دریایی و هوافضای سپاه، در موج هشتم عملیات نصر ۲ بارمز مبارک یا زینب کبری (س)، در یک عملیات ترکیبی با استفاده از توان موشکی و پهپادی خود، رادار پیش‌هشدار سامانهء C-RAM را در پایگاه علی السالم و نیز محل تجمع سربازان جنایت پیشه ارتش تروریستی آمریکا را آماج حملات خود قرار داده و درهم کوبیدند.
🔹
بار دیگر به مردم شریف کویت یادآوری می‌کنیم که این جنایات توسط آمریکا با استفاده از خاک شما علیه ایران مسلمان انجام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/akhbarefori/671660" target="_blank">📅 05:23 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
