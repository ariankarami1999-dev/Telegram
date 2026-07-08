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
<img src="https://cdn4.telesco.pe/file/EqFI2UokJEolmIbK9pNbdtcJ1NZQQurgw03JUc5bzQVSn_7Zw_QFba2wIJaBfJ4Dv0k93QsTHbAUtxGlBPqQVt_3WYlG7Xi7sUmGrNWCYv6NTq6nIJk6N3eCwif8MSSwIUQTHeUQMsmzP7OQtVLvzlCVg0REnEWNabnNRfu6mwB3l9HNUZnogGONSsTN8RrhNI11N0J-I3HRGz7ouemnTT_TLadha9vbVlJHoXtU000ed42pKxxQWhs9hibs1eOyvTN7i_kri4jx4xX28LHZDSerfA9IUY8TJKQG6xVJlUFnos2CmCmGHNIuOiOMbkTnnAWuI6eo5mvl9-jDZf5aqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 925K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 11:13:54</div>
<hr>

<div class="tg-post" id="msg-132415">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
اولیانوف: حضور کامل آژانس بین‌المللی انرژی اتمی در ایران در آینده نزدیک امکان‌پذیر نخواهد بود
🔴
میخائیل اولیانوف، نماینده دائم روسیه نزد سازمان‌های بین‌المللی در وین به ریانووستی گفت، در آینده نزدیک نباید انتظار حضور کامل بازرسان آژانس بین‌المللی انرژی اتمی در ایران را داشت.
🔴
وی افزود: ممکن است بازدیدهایی از برخی تأسیسات، مانند نیروگاه هسته‌ای بوشهر، که از حملات آمریکا و اسرائیل آسیب ندیده‌اند، انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/alonews/132415" target="_blank">📅 11:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132414">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از آژانس ایمنی هوانوردی اروپا: اپراتورهای هوایی نباید در حریم هوایی ایران پرواز کنند.
🔴
تعلیق پروازها از طریق حریم هوایی ایران و عراق تا پایان ماه اوت ادامه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/alonews/132414" target="_blank">📅 11:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132413">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdFwYQx9VE_bpe1gnGE18buYwgYwoAUMtqHum3YyVSxBHNocnwXZD6tZUNoOzrCyHdnij_gw8-wWCSTdlnT7FD4qqN8u401u9FLI91mi3Ya4tNqh38UBNmJTkfjsb9LSgNb0CqkrjN0AYv4zg2zfAtnXHTnlIYgSSh339PVaBfRWhbf8mqHWx20a6ClLGEatVvjqvWH7zNXNEgk9gJSesT2GHWaKvh70w9H8Iy0H78cxfhkSJa4w8BNCb1iHAiKUvWZcAYMNRYwAISZX06n86QA45YcjSDEWXa-lmmvH2_WDIgSdVObOuVkPPZiNKYWbUn4M_mgop2tQZNjS0U1QdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گابریل ادواردز، فرمانده اسکادران هلیکوپتر نیروی دریایی آمریکا پس از ناپدید شدن در هنگام فرود اضطراری هلیکوپتر در دریای عرب، کشته شد.
🔴
با وجود گشت چهار روزه برای پیدا کردن جنازه او ، تلاش نیروی دریایی با شکست مواجه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/132413" target="_blank">📅 11:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132412">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d638495cb.mp4?token=Tk0OOiA69Qg0LVWFJBJo6TMPoLWGx8jzXHNUIqpvHV_Q6houOhI3H_IWnR1DqRYD9i8LfKlCjGhOHGvvBncZoKjKx633rUvNTGHwJqQLSfAsL54SklznSmlTZY5ndzIxWBFbvidsXMODAQEQK7oyeOZQ0W-pLvjl7tgwpx3lRxSy2u2GY_HBb4ZCNSQbOxxFtcbp6dOQ6j5JpGi52Kg_WKmXo5rbJciOpSEyzFRpdaxfzwcw6MYvZxDw1FFoRiToDNu-rt-X5A6GXBOCeoPeqIyMfaYGVS2I_YXVOUYXK0-5Y6w-RNf35kP9sG-PsqfQPfrqYbt1e3mm5zOUHI3f9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d638495cb.mp4?token=Tk0OOiA69Qg0LVWFJBJo6TMPoLWGx8jzXHNUIqpvHV_Q6houOhI3H_IWnR1DqRYD9i8LfKlCjGhOHGvvBncZoKjKx633rUvNTGHwJqQLSfAsL54SklznSmlTZY5ndzIxWBFbvidsXMODAQEQK7oyeOZQ0W-pLvjl7tgwpx3lRxSy2u2GY_HBb4ZCNSQbOxxFtcbp6dOQ6j5JpGi52Kg_WKmXo5rbJciOpSEyzFRpdaxfzwcw6MYvZxDw1FFoRiToDNu-rt-X5A6GXBOCeoPeqIyMfaYGVS2I_YXVOUYXK0-5Y6w-RNf35kP9sG-PsqfQPfrqYbt1e3mm5zOUHI3f9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مردم عراق میان دست میکشن رو سره عراقچی بعد میمالن به صورتشون
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/132412" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132411">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
معاون امنیتی استاندار بوشهر: امروز یک مقر نظامی در شهرستان دشتی و یک مقر نظامی در حوالی شهر چغادک از توابع بوشهر مورد اصابت پرتابه‌های دشمن قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/132411" target="_blank">📅 10:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132410">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سی‌ان‌ان: پیت هگست برای اولین بار به عنوان وزیر جنگ به اسرائیل سفر کند
🔴
انتظار می‌رود این سفر امروز انجام شود و  هگست با بنیامین نتانیاهو و اسرائیل کاتز (وزیر جنگ اسراییل) دیدار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/132410" target="_blank">📅 10:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132409">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCPJCgbhUZd6s8QTTDQUbqz0gzsRt3ZILJwaV8U-I_bDR9U2nOjhgNQPZgzsz6GeeLiDPwttUhcMKt6z_beu0tfqJlSVv6DIJvXvIyQnQI6dWKp2EW9gWgADkzhe0R2__K-BJHfFLKG2yoky6Ona1oTku-5-LKiOXcWgQ_SP7IZsCnxxuvEbcGMM9CCYlNMCZlanC7YKh5by4anpjLo5946VfoMSNKi94uLZaWOpaPBXGdyM6nCyBik_1ooQLUS7Vh-_TvLEB8Nxg66c8AUOEpFtQJBe8O33hECC-P9CMatlvoH85tjAXduiJCkDAR1cFP2Df3xbfdUrJA_owBrBaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه وزارت خارجه درباره حملات آمریکا و نقض يادداشت تفاهم خاتمه جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/132409" target="_blank">📅 10:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132408">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ارتش کویت مدعی شد ساعاتی پیش چند موشک بالستیک و پهپاد شلیک شده از سمت ایران را منهدم کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/132408" target="_blank">📅 10:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132407">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3ZUIArX71RbcZ_ZcsfK2PN7cC9jOAGw5T_dzxBTKFY-uHKnfIqswyA-YhbStoLIp5qY9lc05aI74CkDwTfBINKc0E0UmFI1N0xMj1EN-eBVjX2GSdVxTdj9fZu4-43l5GCrN3WJl2nzAYdrAHR6D9jrt0dOG50iKxxPGFh4PnaOkiQffX-EDd8vD-5JQ9Ynn4wkRV5uk2xPu-U6lqODq8SC7lnu8x66Rmyxuq_b3rCgPMbj6OysmFqDt3IHhpqTsZPZgiKf-DJVu1l7GkYxC2Yovq3kUMab_ChyZuky2g-gH9Q0GQ1WCSKEsVZ7hibAUSzefVFcKc5naNc1Oy5mBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسام الدین آشنا در واکنش حمله سوپر تندروها به عراقچی: همان که سنگش می‌ز‌نید؛ سنگتان را به سینه می‌زند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/132407" target="_blank">📅 10:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132406">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0X0xeL9XzjgY7bhaA6nTm86-S4jqwbfqTFugNjX0vetpkyIAVLF7hm9ZH4p2-8P2wYBjEZNbv6HdmSGfILgRDIGbafit4jujg_McdmIt6_oV5DEzrXaMZX61UaPu1ZPzBtLwmnfTvqzMdniCwTzChyOUxi9NIMNGf-GHg9wbl4kv8m1LmFWTEZAqv3KJu9ibaA0-51wGP_jbv4DHx3xzI9UkSzhfZ4iLUJa7I9Cp7XWEuRuAwHqfozay69KXqbxzHumDg_AHxirPfrSrdrN-eMxCZ-R5iW9_XGd8A0UjGYPERQ_cEfiwCcbw99Y4Hbyx7oZy5GBaMcGZ33-eY_r8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۱۱ اسرائیل
🔴
ایران: روزنامه «کیهان» که سردبیر آن از سوی دفتر رهبر معظم منصوب می‌شود، به‌طور علنی خواستار ترور دونالد ترامپ و بنیامین نتانیابو شد.
🔴
در این روزنامه همچنین آمده است که بیش از ۱۰۰ میلیون دلار از مردم جمع‌آوری شده و قرار است به‌عنوان جایزه به فردی که ترامپ را ترور کند، پرداخت شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/132406" target="_blank">📅 10:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132405">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Urv9Sick-rRDDOqCKQl__vgboUN4CONZ7t69PrjoZh0RNKmeFghp08l6Y7nmSHdRSyOfwiQhNHr4rYtMqM-o2Vb9P1kKRVXH-gKylM8XKpjLTFr47OBRffMPM6DwC6nwaz_VVayUIyRs7s_6YdEWBwKeahGjFYgyGNb9fEGQFZzqf-mPP-rNkFU4VerHU_lboqMT1McySwSM6Yn8_PM5gwb-2NH285W_UenH1FfAmTaBjXAz8rLHeLkA4RaHduASNbhCIwkpIBCJylSatiPmRF3g3XrhCWC5SzFgPlfcVv3IY1WagmhCj1RTfdu_F6xXBGG_I2bdxM-hU76IsJ4SdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لارا روزن  :از منظر تهران، اهمیت راهبردی و بلندمدت تنگه هرمز بر هرگونه منفعت اقتصادی که ممکن است از توافق با آمریکا یا بهبود روابط با کشورهای خلیج فارس حاصل شود، برتری دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/132405" target="_blank">📅 09:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132404">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
آژیرهای هشدار در بحرین برای بار چهارم به صدا درآمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/132404" target="_blank">📅 09:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132403">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از یک مقام آمریکایی: ما مذاکرات خود با ایران را ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/132403" target="_blank">📅 09:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132402">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
صدای چند انفجار در شهر بوشهر و مناطق پیرامونی شهر شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/132402" target="_blank">📅 09:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132401">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سپاه : پاسخ ما به حملات آمریکایی، در ابتدا از طریق عملیات مشترکی بود که توسط نیروهای دریایی و هوایی ما انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/132401" target="_blank">📅 09:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132400">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
داده‌های ردیابی کشتی‌ها: ۴ نفت‌کش و گازکش از تلاش برای عبور از تنگه هرمز منصرف شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/132400" target="_blank">📅 09:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132399">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8-n14UoMsXiv76oK-xRq7iXZKuk1nsaXCsAQHGB42e6CIA5KXqne-xHcGw8jEdJt5Yf5o5fCd7gbTFNF2pafirS1Hqadwueld2dzODHhokKb3RQNdmhZHYuoLrBxp5W8eiDfd1-cR7jM5mOAwPC0x3xukM0lwXgFRGT1IvryKQbYsloR7GUsxJGCdYA4oEe-aSaeI4FZCSBpTjgEQfiFQzFbdO5pg4AmewSHK2YJ6wxkdJ8v70l6fvlhF9CX9D_Jmb26IW2W5FespL7Ww7fd0wHzfr2o6OVbnUi1k86bwU1BqRVVyBVEiIBwYdS221SUMrXT7IDEIphWt4-TOQF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت تتر ۱۷۷،۴۴۵ تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/132399" target="_blank">📅 09:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132398">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وضعیت در بحرین به حالت عادی بازگشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/132398" target="_blank">📅 09:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132397">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سفارت لبنان در واشنگتن خبر داد که کاخ سفید برای رئیس جمهور لبنان برای سفر به واشنگتن دعوتنامه‌ای ارسال  کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/132397" target="_blank">📅 09:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132396">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
خبرنگار:واکنش شما به حملات اخیر آمریکا به ایران چیست؟
🔴
ادعای روت، نماینده ناتو:به نظر من، این اقدام کاملا ضروری بود. ایران، آتش‌بس را نقض می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/132396" target="_blank">📅 09:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132395">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
عربستان سعودی نقل و انتقالات بانکی از حساب‌های سعودی به حساب‌های دریافت‌کنندگان در امارات متحده عربی، به ویژه در دبی، را به تأخیر انداخته یا مسدود کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/132395" target="_blank">📅 09:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132394">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
انفجارهای شدیدی در منطقه بندری کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/132394" target="_blank">📅 08:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132393">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
پاکستان سقوط هواپیمای ترابری خود در دریای عرب را تایید کرد
🔴
سازمان هواپیمایی کشوری پاکستان (پی آی ای) صبح روز چهارشنبه سانحه سقوط هواپیمای باری از نوع بوئینگ ۷۳۷ متعلق به شرکت کی-۲ در دریا عرب را تایید کرد
🔴
پنج‌ خدمه هواپیمای باری پاکستان از قربانیان این سانحه هوایی هستند.
🔴
مسئولان پاکستانی اعلام کردند: ما به عملیات جستجو و نجات سریع و موفقیت‌آمیز امیدواریم و در این زمینه تمام حمایت‌های ممکن را ارائه داده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/132393" target="_blank">📅 08:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132392">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moAN1OG3dL_M2nXoR1EZ0_G6GXjuekqxh7LB6MVA6UKOO3OTPGvERI21L-kW3okAzkumpTZq9ccwBqBhIbGeEbv9pY2K0Z1sfA_xQfSQtItOc98A1zIOGN5g2As0Psilc7DWxe8j3iZ011BdxKb-djj009nJ1gHWjpfWWfF_hOOBfV7MY7HpJArp2jZDfvgxK4hKLoPRRUQsOtjm6CpCPt90RkuRi_eKuZUZHJfwppu9UsI4DziXcj1Qq_fn5fE6rh-ShY1RtyFCphrBkvqLYaQVdoUDPZsDqnLf8EHXIprD3pToIhhEKvx0rkKFZC9FhLiSkWLeHw63NBLsV7qPEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسمیت، خبرنگار ارشد نیویورک تایمز به نقل از یک منبع نظامی
:
حملات هوایی علیه ایران فعلاً ادامه دارد و قرار است تا مدتی ادامه پیدا کند، تمرکز حملات روی چندین هدف نظامی ایران خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/132392" target="_blank">📅 08:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132391">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWotu2s1HiET30pmGw7JVjp76jBf73LkUJ1goUNOxrSA4LAoD0_DYlWHvSGZ3D02Cy9mH7Lf8Sl5UJ5bEOxvRZMzJWAVtHn7r6ere64iE1HKS0bTpGfy63m6l_XpEbxITNaTSfnDKspDnXB0dfXofCLBc3vIQpDI-fxd9BIeSWNCvB65GIxuofeN36mSpJ1vi2t-WY6N4621AI2uA8cFUEgi_8jR6HjW8475_YjUgJ5UKA4OpomavxyasZ0t0F42JNsMugZ_7OdLZxMFGMNGMxoUvayhP4RH2MQoEblC6TQB2W0D3TPyH_vYgK80oedx-wu3OeZhs_hIxLFDVEn9ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیشب پالایشگاه نفت ساراتوف در روسیه مورد حمله اوکراین قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/132391" target="_blank">📅 08:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132390">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
خبرگزاری رسمی کویت: آژیرهای هشدار در سراسر کشور به صدا درآمدند
🔴
برخی منابع خبری از شنیده شدن صدای چند انفجار مهیب در کویت و بحرین خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/132390" target="_blank">📅 08:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132389">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/132389" target="_blank">📅 03:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132388">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فوری/حمله مجدد به بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/132388" target="_blank">📅 03:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132387">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
عرافی، مدیر حوزه علمیه :
عدم حضور مجتبی خامنه‌ای توی مراسم وداع با پدر، فرضیه غیبت کبری رو تقویت کرده؛ ایشون احتمالا به امام زمان پیوستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/alonews/132387" target="_blank">📅 03:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132386">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
روزنامه نیویورک تایمز به نقل از یک مسئول نظامی آمریکایی: حملات به ايران برای مدتی ادامه خواهد داشت و بر روی مجموعه‌ای از اهداف نظامی متمرکز خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/132386" target="_blank">📅 03:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132385">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
خبرگزاری آکسیوس به نقل از یک مسئول آمریکایی: ترامپ با طرح حمله به ایران موافقت کرد و دستور اجرای آن را در زمان حضورش در تركيه حین شرکت در اجلاس ناتو صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/132385" target="_blank">📅 03:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132384">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
خبرگزاری آکسیوس به نقل از یک مسئول آمریکایی: ترامپ با طرح حمله به ایران موافقت کرد و دستور اجرای آن را در زمان حضورش در تركيه حین شرکت در اجلاس ناتو صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/132384" target="_blank">📅 03:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132383">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سی‌ان‌ان: وزیر جنگ آمریکا روز چهارشنبه به اسرائیل سفر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/132383" target="_blank">📅 02:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132382">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
پزشکیان بعد از شنیدن خبر حمله از عراق به سمت تهران حرکت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/alonews/132382" target="_blank">📅 02:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132381">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19e73648ed.mp4?token=vtw0lQLnf-__xo6KSauyAumia6TMUO9mxBmIuT076MJkdrIEXE1_hsswnkK3J-AhGZ-gPPc4ZGXevYCQQhKXZifZyc47SuVcG6AKBuQEjldsQXExtNvXCN7LU8YoGjb9S2xxC8Od4ALyDwDGpMUZMkeBElw3zgIMVeqxMylXClvtrA1sjplbqSbmb2PYAJjMCJHkJYKLwYH9_8dDyskGe3aqk5bC8n5gX6iyejaD4MhMnzK7sLwr-eTyWKxK5C5Ow19ZA7W5sKpK48uFq1-PJjLBvdWGrNpwM2_Q4CwUWXRHvuz_Brt52BxC1xwOZUSJBF-30TR9y6mxpK2dZub2CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19e73648ed.mp4?token=vtw0lQLnf-__xo6KSauyAumia6TMUO9mxBmIuT076MJkdrIEXE1_hsswnkK3J-AhGZ-gPPc4ZGXevYCQQhKXZifZyc47SuVcG6AKBuQEjldsQXExtNvXCN7LU8YoGjb9S2xxC8Od4ALyDwDGpMUZMkeBElw3zgIMVeqxMylXClvtrA1sjplbqSbmb2PYAJjMCJHkJYKLwYH9_8dDyskGe3aqk5bC8n5gX6iyejaD4MhMnzK7sLwr-eTyWKxK5C5Ow19ZA7W5sKpK48uFq1-PJjLBvdWGrNpwM2_Q4CwUWXRHvuz_Brt52BxC1xwOZUSJBF-30TR9y6mxpK2dZub2CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات هوایی آمریکا به جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/alonews/132381" target="_blank">📅 02:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132380">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
انفجار مجدد در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/alonews/132380" target="_blank">📅 02:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132379">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fw7NPEWAj08nx_J6bEqZf_UmD00vc_ON-1vM8CeYoEJoW5FMSO47kYFz-zZbVGdttQBDJp5Y12h2Cx2Wijfp3FAMcW3wZMRRvDSB6t893BLSyByN9oGpXit7SJ-D28JRxwMtsIxbHr_DoXxK23iwBScL7Gpr7Ked3_zp5Vl6jPMB47cLqdVTBASggwhOyZPAZHfCfGyVqZ_ptO3EP-CBoYfGJv-LJmW1Y8CB3Z-u1R3aY_WaV8SAf0GTjGoguA08hK91_PAkuN_FCgpQk9OhMGAf-GBDHQ1eYMALopoa7Li32HB9qvv_OS_R2NS5CPXs7hCEQQCbVwgV8ai6xOm50w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت خبرگزاری معتبر فارس همزمان با حملات کم سابقه آمریکا به بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/132379" target="_blank">📅 02:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132378">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
اکسیوس به نقل از مقام آمریکایی: حملات آمریکا علیه ایران از نظر گستره و قدرت، چهار یا پنج برابر بزرگ‌تر از حملات قبلی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/132378" target="_blank">📅 02:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132377">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIt4uzxxCCL-Vhy0xurSK6f8L7-Iuj5YO7niUSacplIjM90J0WbXQqSWU_YazccUywuOko7CB8xFvUI1UnHoOB48Vc3CMTIVVP8uOye_EJ2kEi7Dw-dsYlfa_0W7yyIWgD-DbnIWX07j2P4gD1hIvPetYAx8V712gwumQ621jau9AXPTHbrLW2sZVDhoBjEuJiqu401DnlXTeGe91p141-TgNf4QjNujtjZdBPbe7NDEmRR_k8FUtmxlpOlVu8raceORIc5ltC9dfRlDqqHofHGaYlcY2lHzE1EQt-x5HWiky6nIZZQz5eKlZ1wOIjuDAWggO8Gc8D4Qdtf5mx52eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
🤪
💦
🫠
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/alonews/132377" target="_blank">📅 02:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132376">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری/گزارشات از بسته شدن تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/132376" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132375">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری/انفجار مجدد در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/alonews/132375" target="_blank">📅 01:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132374">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
مقام آمریکایی به رویترز: حملات ما در ایران سیستم‌های پدافند هوایی، سیستم‌های نظارت ساحلی و سایت‌های پرتاب پهپاد را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/132374" target="_blank">📅 01:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132373">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
اسرائیل هیوم: اگر ایران تلاش برای جلوگیری از عبور نفتکش‌ها از تنگه هرمز را متوقف نکند، آتش‌بس در خطر فروپاشی قرار خواهد گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/132373" target="_blank">📅 01:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132372">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">اگه جنگ شه و حریم هوایی بسته بشه، مجبور میشن سیدعلی خامنه‌ای رو عراق نگه دارن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/132372" target="_blank">📅 01:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132371">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوووووری/سپاه امشب پاسخ خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/132371" target="_blank">📅 01:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132370">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5fd7843a1.mp4?token=mVsYDFDBTF0h5eoX40nXK4_BIJJm8SMDkcFnLExwSn7SEY9hzfwyVbuePkoDRoUWdbJPdjGqoa1o-MowRALZraB5Iz42WHHpbiBMmHET_c1zq-OItlLRHijO2TeZZXyYUDjeNl1nZL5KR6uXEpNLvpm7cMQUO85I57y0lbndt0UNb9EPbJjJPEm17ZaOwWCqS-s3yuD8MsbaswCdATWtIvXHRMzHNQKjCVn40ypDZjqjObEa-NFWqrnPWdgw3U51h-u2P87MTYLYpp7R8FbDtU_ITpbHOO7oVNKi9En0kmSSfEV4M04EILOuv3wuna5BOdZvbdwokqjc_0EhYrjOCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5fd7843a1.mp4?token=mVsYDFDBTF0h5eoX40nXK4_BIJJm8SMDkcFnLExwSn7SEY9hzfwyVbuePkoDRoUWdbJPdjGqoa1o-MowRALZraB5Iz42WHHpbiBMmHET_c1zq-OItlLRHijO2TeZZXyYUDjeNl1nZL5KR6uXEpNLvpm7cMQUO85I57y0lbndt0UNb9EPbJjJPEm17ZaOwWCqS-s3yuD8MsbaswCdATWtIvXHRMzHNQKjCVn40ypDZjqjObEa-NFWqrnPWdgw3U51h-u2P87MTYLYpp7R8FbDtU_ITpbHOO7oVNKi9En0kmSSfEV4M04EILOuv3wuna5BOdZvbdwokqjc_0EhYrjOCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو لحظه انفجار ها در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/132370" target="_blank">📅 01:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132369">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فووووووری/کان نیوز: در آمریکا برای احتمال چند روز نبرد با ایران آماده میشوند؛ این موضوع با کشور های عربی خلیج‌فارس نیز درمیان گذاشته شده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/132369" target="_blank">📅 01:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132368">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
الاناست که عاصم منیر بیاد تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/132368" target="_blank">📅 01:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132367">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCtsYZZtKzaY35_ei0PMvCs8Z2xFxazBF2SizM3OAH2xGtTiuKLh_MkVUTlljZyuE20aIj-b-XmRTiyvvl7-mmhjERdKN39AC2vzJaXx2JWAxpCniNynANzW2vcHRs3Dwncud2UPqLXd-ef4Cj2qzP8OgBlQ64H2593yrXIt2djjh4VLnxL-urahfvb2iMduP57k531JcggXSlu1Z6Db1_Bbv4oRy_5qYA3TkGBXykvNjmphj58oMtygAdr_dIevYBkzOFhJMlma_CKBiVKV3agJZQ9FWMaDFcnxslyyoGvgZTaoBV8tJMqn2fm0e2mp5WTjePLG2kS_1lIzXM1Row.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارسالی کاربران الونیوز از بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/132367" target="_blank">📅 01:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132366">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1c97f0335.mp4?token=ZLlalnwCkuxc2tOUPj6ve0FrGvvcgmEXDTvBq5n8GgEHCJr_LkxhqLiyFZwfaKC_uOTYKip-NvKxTJtFbHB19bmXuAfVxuRyTTO2etJ1imCQNpql0avfKuAY9UcGFP8y6Cjun4Xn5qwGTHCpern9t1il1wwC81TX-P-MGnKfn9GdQQu8p7YQ08hvqAP13JxfH2ObDWWRlEEDtIGJdevtzCCl2Xt_opNLClCuy9k9nkgbCUyiEokhcmtUKdKZZvTiTTTpI9_uuD4pv-g6FRJIjprK-KtAjjZNuY9xu9IssoM7VseJSNNHAcfJTvjq15_wAp1C64fK6geI1xD0nPvkIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1c97f0335.mp4?token=ZLlalnwCkuxc2tOUPj6ve0FrGvvcgmEXDTvBq5n8GgEHCJr_LkxhqLiyFZwfaKC_uOTYKip-NvKxTJtFbHB19bmXuAfVxuRyTTO2etJ1imCQNpql0avfKuAY9UcGFP8y6Cjun4Xn5qwGTHCpern9t1il1wwC81TX-P-MGnKfn9GdQQu8p7YQ08hvqAP13JxfH2ObDWWRlEEDtIGJdevtzCCl2Xt_opNLClCuy9k9nkgbCUyiEokhcmtUKdKZZvTiTTTpI9_uuD4pv-g6FRJIjprK-KtAjjZNuY9xu9IssoM7VseJSNNHAcfJTvjq15_wAp1C64fK6geI1xD0nPvkIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اولین فیلم از لحظه انفجار عظیم در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/132366" target="_blank">📅 01:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132365">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سی ان ان: آمریکا قصد تنبیه ایران رو داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/132365" target="_blank">📅 01:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132364">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e1d560049.mp4?token=L4ScnbtP7tsLpoTSeJBKEkq0Y6kCEV0atZi73Nfd7CFrTpLAtUorEmr0fzO8RXgzV2378K9qpf_RutpM63APdnGGdtqDHGRTSh2n-D5ywNT7Ptip4Q-n5mNbsra-CMVs_0wVQPM6T4ZrNxPmBwuNOuB7XyHsfyRS5dr5hvL0g_FbIL2VsXWMj3eJEXd-a7rbrh2_F8TVMLpvIQ7ppP9PJd6w52t_S9ghbdLoNfPGiESvII6vZ19Dg-L2N7C3NiIj3fj1uHcbOsDkubatgr9Zh2yXXbQYoNnrM4vyDa515k_P_B0fvO4Saf7DxOQHEeyBaiKOMK0ZavGyr55OyB12zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e1d560049.mp4?token=L4ScnbtP7tsLpoTSeJBKEkq0Y6kCEV0atZi73Nfd7CFrTpLAtUorEmr0fzO8RXgzV2378K9qpf_RutpM63APdnGGdtqDHGRTSh2n-D5ywNT7Ptip4Q-n5mNbsra-CMVs_0wVQPM6T4ZrNxPmBwuNOuB7XyHsfyRS5dr5hvL0g_FbIL2VsXWMj3eJEXd-a7rbrh2_F8TVMLpvIQ7ppP9PJd6w52t_S9ghbdLoNfPGiESvII6vZ19Dg-L2N7C3NiIj3fj1uHcbOsDkubatgr9Zh2yXXbQYoNnrM4vyDa515k_P_B0fvO4Saf7DxOQHEeyBaiKOMK0ZavGyr55OyB12zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارسالی کاربران از بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/132364" target="_blank">📅 01:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132363">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فووووری/حملات مجدد به بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/132363" target="_blank">📅 01:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132362">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a358058b.mp4?token=mNVHgE7Oc2bOq4fooXJ7OWGm-btQ6RzROUP2I8D8-Cz-Q_4XxRemvJ61dHu5DFaStO_TEXxrBxwFBnmFop9dGQaiI-J68I5xMPM81zooTwur6lgWrJFxIKbEKQFnVn-mlKJ43RFJDp5JhZfqTTBaERY7hvi5LAOyq6xuI64FbWZ3QogC9xjzW_6Me9fWxE_yj5CV2Xyl0-QFCJeymF0zgIrSbGjaCOtA2F34uhU3ovJlHbNP6secSxW8az0CpUPTA4HQ1oqm7dzkbHV9ef2R7jZwSZdeB-FP0oOca8yDK1yKDVlp7o18onvSyUdzx_yWdjCtwKAwWoTMUJ6_DYPpdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a358058b.mp4?token=mNVHgE7Oc2bOq4fooXJ7OWGm-btQ6RzROUP2I8D8-Cz-Q_4XxRemvJ61dHu5DFaStO_TEXxrBxwFBnmFop9dGQaiI-J68I5xMPM81zooTwur6lgWrJFxIKbEKQFnVn-mlKJ43RFJDp5JhZfqTTBaERY7hvi5LAOyq6xuI64FbWZ3QogC9xjzW_6Me9fWxE_yj5CV2Xyl0-QFCJeymF0zgIrSbGjaCOtA2F34uhU3ovJlHbNP6secSxW8az0CpUPTA4HQ1oqm7dzkbHV9ef2R7jZwSZdeB-FP0oOca8yDK1yKDVlp7o18onvSyUdzx_yWdjCtwKAwWoTMUJ6_DYPpdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو دیگری از بندر شهید حقانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/132362" target="_blank">📅 01:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132361">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پشمام
😐
بعد از برد دراماتیک آرژانتین گروهی از طرفداران زن این تیم در استادیوم لخت شدن
😐
⚠️
⚠️
مشاهده بدون سانسور فیلم</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/132361" target="_blank">📅 01:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132360">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MX4GAd0UYBAYHa_5FT3UETk3ISDAIX9ryFTYjqm4tP8coP7s8x2L4DfM9CyhogQlhlGOU032rY0HpxgGNCwmRDKxD_A_-z2IJqyTWC2eTB8B0qjQ4lsDw3XmPs6RYlBzBS_JhR3rHrVYNqAzDbacZnsAzSRxUg5eU5mSSdarJlS-OR8iX3IdjCpeXf8FVm6qF8QEOk9lTV5_KhjhnPHl2B_1dxZ333HwlJC36V-whsTj6KprgwkWXNgHy8CAdDQvRgCdlhck4GJyWOANfXM9fGbl8X3N2hcDHCeyIlp3_17qzb1Pq8aKt-Ql9_w8YnR50oAmXT7mQ6DIrk0n_7MtdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/گزارشات از ترور در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/alonews/132360" target="_blank">📅 01:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132359">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffa97fbc4.mp4?token=SNZ9HWwp95g22fTghtU6UVuv_6_qmRCZaijPQKBsb2aCJxHvHf0F5Kk1HdyhYdrqUrhDNd2VQXNonlpPqFsPrfzftizyC05VC00NuRGXL7tV_M292X6uLHJ0W20bbhhC3zHk8Hu6f1fBFwpp5_CW5f20rWsl7RvsH4NHClwCKpryIP8fyO1J1T72JlZwKLbhM8TlcGB_92791YfhZ4jRBWPN23htyokbOv4YgGg9jXYM-pvdvKuovRno4qK2KgNgO8MCZlV6Iz0eWHJURCe7jindR_fqf0heRXFoeACQrWkPWHWuF8d4dNlCqCtdWVsRijI-PZ0i4pnIr84yddoGcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffa97fbc4.mp4?token=SNZ9HWwp95g22fTghtU6UVuv_6_qmRCZaijPQKBsb2aCJxHvHf0F5Kk1HdyhYdrqUrhDNd2VQXNonlpPqFsPrfzftizyC05VC00NuRGXL7tV_M292X6uLHJ0W20bbhhC3zHk8Hu6f1fBFwpp5_CW5f20rWsl7RvsH4NHClwCKpryIP8fyO1J1T72JlZwKLbhM8TlcGB_92791YfhZ4jRBWPN23htyokbOv4YgGg9jXYM-pvdvKuovRno4qK2KgNgO8MCZlV6Iz0eWHJURCe7jindR_fqf0heRXFoeACQrWkPWHWuF8d4dNlCqCtdWVsRijI-PZ0i4pnIr84yddoGcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بندر شهید حقانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/132359" target="_blank">📅 01:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132358">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
مقام آمریکایی به PBS: «ایران به‌وضوح نشان داده که به هشدارها توجهی نمی‌کند. ما در حال افزایش شدت واکنش و فشار خود هستیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/132358" target="_blank">📅 01:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132357">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از مقامات آمریکایی
:
کشتی‌های جنگی ما در حالت آماده‌باش هستند تا در صورت تصمیم رئیس ترامپ ترامپ، بنادر ایران را دوباره محاصره کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/132357" target="_blank">📅 01:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132356">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=t_KVOi9rjaukuA3sp7KXn9tQes1zeyoU1NMHyfWhH0sN8Hlnrm5LJW7c7x17PHRF5K8lkml2WV0dGygf7DFTy8wTQQhAxMX8D32r4wqziJ3hn4hQ-HSdHc-1y0NDxL3g-DTNIuGo39G3mUeS3dqGYjbAFdmkLr_oMBuqO4fzN-jIUQCsKakrteWb_zltVrEspjnOYd9xbUa5vK82lO6ASbQYXQqaiJB2Z1130SSzXtJZpFS_9-MoRi6Ev18rpB8h6UMAWF5dxWFImS3A27IRJHGBu3xBRCaNQ0vRNmEhtxqCfSGcYMgyUT56v2LcNkk9bDXlHiQL_QudEZN502RS6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=t_KVOi9rjaukuA3sp7KXn9tQes1zeyoU1NMHyfWhH0sN8Hlnrm5LJW7c7x17PHRF5K8lkml2WV0dGygf7DFTy8wTQQhAxMX8D32r4wqziJ3hn4hQ-HSdHc-1y0NDxL3g-DTNIuGo39G3mUeS3dqGYjbAFdmkLr_oMBuqO4fzN-jIUQCsKakrteWb_zltVrEspjnOYd9xbUa5vK82lO6ASbQYXQqaiJB2Z1130SSzXtJZpFS_9-MoRi6Ev18rpB8h6UMAWF5dxWFImS3A27IRJHGBu3xBRCaNQ0vRNmEhtxqCfSGcYMgyUT56v2LcNkk9bDXlHiQL_QudEZN502RS6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ما که نقض نمیکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/132356" target="_blank">📅 01:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132355">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlCO67nuQFhuYmNa6hjYTbOlahWFXnymf__gCasXC467xEMI4tHqAL5e2EXDVO8uxqresPW3sWfSm3nM5fBZGZLItzIXBIN2sWWP1y6Lr7vHOEAckUW1RlP1vUF5BoJ8kwr-EQX5tparTga8JOuLFQ8ujoMYolZe497opBvqJxhvibKxZ80qnnL7nzT4pLOzLvZCgjZ8_Qfli4pMkTZDtJGn-tgLeMbfotf2E2tjSz1vJJUDx8z5mgXMpxF_KInDSA_LeB0COCD6bo2CmW7iiEESTo1pGxveQ80B45msYIXZgZ4NO3yvKvvUtUlzylxJaxlYprDwPvqyXMf2c-RfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پنج هواپیمای ترابری سنگین نظامی آمریکا شامل چهار فروند C-17 و یک فروند C-5 از پایگاه‌های آمریکا در اردن، بحرین و امارات به پرواز دراومدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/132355" target="_blank">📅 01:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132354">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6xj0IjJUrRv4ppV296q8e7a7qgY_9O2Vw5ZOiriKzLAp1S73wC3U3nWqblupBVqgmq6EEg5DR6cMCSEUIq8o6XmfKO8UrJ8SfcQpdIcpHsjLZznQ1ukehkacwphqEvovjaT76KQ1yEizjtR2gpaukCGE-qChXKs4OKvDClYzeWtx25VoccGZlpgxIPuNslfeADVUR-stuPH_gfch8n-JToq1tC1NX45tCa8-QhJaRwWFwckdhnIqhH75wdoy6ZT8vtchakfzKgzkmOjCb_LJp0RTFXrK8NaOtZuvSiFhxsgSADiBzZosHMjpChC1Gs0_BKB1DcS3VsvgCnnlWAfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار مهیب در
اسکله‌ی سپاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/132354" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132353">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDeeBa3c9vIDZl9gnFeYXWN85LSNJitRMrauhHolm9jv3k1K9GhN24LfFttUtiPIFvKS-qw7IL8zWjmSMa6W6mremiWSyte00ThoefKythIa5n503Z_YtRCrFYXwjhZqnrrpIW80TuXfOKKvCKGk485oLRURFOTgacskefRG8Py6LMcnNI8bpEnqxz9U05t_AxK5MRO_MGEZdcbrbC6UfO6pCLUrIj4409xiEq0zxsz-A3y_xZQrJLRveWIkrYDHT2Q9QNt4Maa4aFyjxb6w_IvLA23iNpAd05svhR0yQKGu3yddjLxR4e3WsQokfcZYuhNW0RNGeW8n5dLBsV5CpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش اون دکل مخابراتی توی جنوب که آمریکا هر چند وقت یه بار میاد میزنه میره :
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/132353" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132352">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
بندرعباس 11 انفجار رادار های دریایی اسکله رجایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/132352" target="_blank">📅 01:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132351">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
گزارشات تایید نشده از حمله به نفتکش‌ها و تانکرهای سوخت ایرانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/132351" target="_blank">📅 00:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132350">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
حملات همچنان ادامه داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/132350" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132349">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سنتکام: آتش بس همچنان پابرجاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/132349" target="_blank">📅 00:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132348">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eR_6dIkrX1uhXukK2EGKANnWEXQukyTANRHxHfIuPsLuRXG2hG6cBcoDptoSLgGd1oK_1RewtWY7xcsq7ijGRTOyglvKmfqfsxMghZfSmtbD8RShLgG6M911NA9JZqGHFBlW6Kiz_d1dlfHT_iw5XhXn07IHo9chPjfJvukMqOKomFikWWNLCPcoGHKo_H2sLQJS91kGzmoIu0K8Cw1Sq-Ruvwk9qAtC2H_sq9lsLypsPjn4ur6jTzgwmUKlLnN5O3LhtfCgcmFsr8KFGcgR0jtht0Z07_U2rVtwmxN-DSxFUvOx7EGG5utu9ZcIUvdRwnPUn_NdJfBq8j91Et9a2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام):
نیروهای فرماندهی مرکزی ایالات متحده حملات قدرتمندی را علیه ایران آغاز کرده‌اند تا هزینه سنگینی برای هدف‌گیری و حمله به کشتی‌های تجاری که توسط غیرنظامیان بی‌گناه در یک آبراه بین‌المللی اداره می‌شوند، تحمیل کنند.
این حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که از تنگه هرمز عبور می‌کردند. تجاوز آشکار ایران غیرموجه، خطرناک و نقض آشکار آتش‌بس بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/132348" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132347">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوووووووری/سنتکام: در پاسخ هم حملات ایران به کشتی‌های تجاری و نقض آتش بس، مناطقی در جنوب ایران را بمباران کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/132347" target="_blank">📅 00:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132346">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری/با حملات آمریکا و احتمال لغو توافق، حمید رسایی دقایقی قبل ارضا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/132346" target="_blank">📅 00:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132345">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوووووووری/ترامپ از ترکیه و بیخ گوش ایران، دستور حملات به ایران را صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/132345" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132344">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فوری/حملات اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/132344" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132343">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری/انفجارهای پیاپی در حوالی بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/alonews/132343" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132342">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری/با حملات آمریکا و احتمال لغو توافق، حمید رسایی دقایقی قبل ارضا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/132342" target="_blank">📅 00:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132341">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری/انفجار در بندرعباس و قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/132341" target="_blank">📅 00:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132340">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فوری/حملات آمریکا به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/132340" target="_blank">📅 00:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132339">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgBYhSb4X-FKWHKJjfJX4wZEqYBf8QXinYKPBFy32upLns4Q9Tb00ss7koEn0MxC8JmlkZI4d3opzSRrLnAAZqghSo7E5JSDteTO5kA2FHQU0L-wBtCDkLBTRcQ-opuIH3FeFoqzU0TDpBqV5BhoGJ2pa4H3NkUVcdDdtZZI4lofoxTNlt6H-SN0QAGsL8vvS7xIT3Sk7n8QZmuuk1F2U4D7RpsGgDmz23uOkhD8f2ZYD72qmv1q5asYYSiu8XB8h5PRi6huzyzeaqF3ga0K_ivzIqdEwAT2ie6bRtfm6s0eJAwsmOWcHxFQzwtaMnmFMRKmK0iHO2hl6hbNPsAQ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محل اسکان ترامپ تو آنکارا هتل جی دبليو ماريوت تو طبقه 23 هست
🔴
اگه انتقام میخواهید بگیرید بفرمایید اینم‌ مختصات دقیقش، یا انتقام بگیرید یا حضرت عباسی شعار معار ندید بزارید ملت زندگیشون کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/132339" target="_blank">📅 00:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132338">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kP1NVQCjP6FM0ZpbyIihk9hruno7uaNe0r3OeKMVFhxN7ECR4PRYd6JBXGiwscH8qVNxXfyW9XqxphtYOBI7HQpp6bOT9g7ZrGo9fOgEBYBSjJnBeJT9LMYi0mE0FiTlTMyIUM2kRHBNl7OKVXjwFJg5mPWOozW6Ca1NeYouP5JkU3gXZr3epwdvQozJHukoYKvxfFnv2TC2yreDivjuhe7Zbw5nWmiDUDb4qpJ2dRZPl1ypZLvvLoVV_lhzjysP1Ev3RJWd8hvyitsxhYA5N6SK44-hwLsPmS3hlEcMMZWtHg5D849kZMHOTTFM7KXsJyt4t0Jyhw-xRmUJnayNwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری هادی چوپان
"
یار سفرت بی‌خطر
"
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/132338" target="_blank">📅 00:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132337">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBg01GZIvLdR-LhAWKEjI5_dOS0oD72acJGHugs0ChpV9ZG4DZIELJkZNmyk0wyOiB5GNvfL0hJewqNyvQlHOmRkLpJUDhm_SNDjEHhR7svtLYyhxxGN1mHOyEBaPiR2QBR5-St951N20T9a2auptW1LxUn53x4tdKAM4NYbmlj6pFHLb56OUe5skuH7rW61Iv6izg-16fyqEFrL9GHlWaPORV8rRrevB9ZdNklNx1VxDcOVW--HiLAgmfR9FlTEwhesBkZFCCls9iIuJoxHKibYzsRfdX6Gxlwl1mBkK3vdN98IE6nBT0_vE1o15K9IQIfnHxILuOABpgJhuSsZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شب و روزگار خوش
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/132337" target="_blank">📅 00:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132336">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">💢
فوووووووری/پرواز جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/132336" target="_blank">📅 00:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132335">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری / سوخت‌رسان‌ آمریکایی درحال پرواز در نزدیکی مرز های جنوبی ایران است
🔴
پ.ن : ترامپ الان ترکیه‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/132335" target="_blank">📅 23:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132333">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فوری / آکسیوس: آمریکا امشب در جواب نقض تفاهم نامه توسط ایران و حمله به کشتی های باری، حملاتی گسترده انجام خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/132333" target="_blank">📅 23:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132332">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
فرصت ۱۰ روزه آمریکا به مشتریان نفتی ایران
🔴
در مجوز جدید وزارت خزانه‌داری آمریکا به طرف‌ها اجازه داده ظرف حداکثر ۱۰ روز به تمامی‌معاملاتی که قبلا فروش تحویل و فروش نفت خام، محصولات پتروشیمی‌و فراورده‌های نفتی با منشا ایرانی را مجاز می‌کرد پایان دهند.
🔴
در مجوز جدید همچنین تأکید شده است که ایالات متحده آمریکا از امروز (۷ ژوئیه ۲۰۲۶) هیچ‌گونه معامله جدید از جمله خرید یا بارگیری نفت خام، محصولات پتروشیمی‌ یا فرآورده‌های نفتی با منشا ایرانی را مجاز نمی‌شمارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/132332" target="_blank">📅 23:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132331">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
فیلد مارشال رضایی: آمریکا به دنبال عبور دادن ناوهای خودش از تنگه هرمز است
🔴
آمریکا در عمل زیر تفاهم می‌زند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/132331" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132330">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d9920461.mp4?token=bV_jSIp9m-djJxswgdzxHLYgsj2A2qaBj2PYBG1CFQVwIEST5tyz8LduD63djxCiANe44aJBIB3gZFsxInWkLlJntG70GyN0s5cwtH652UxPiBk3uCxDdpp9KeWpyCIiaFYvw13swdC8atvWiOQYhKVilbu8Gw7yQ6koOTbmf2tjzZZzOH4QPph5re3w1mjAaK1pRKLFJbelTEVhc0TQyXUYB_0mqtEbJmM4p4DdU3wFc1fr8C3kXCPy__Z8UD63aVfJpYQHctzf3Nk_fbUGtyo9Rgkdb7_qvvsueKE_qIMEgkQB1iFgCPY0XcTGw-_0FECbToRAjgq6Tt-lRR6c8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d9920461.mp4?token=bV_jSIp9m-djJxswgdzxHLYgsj2A2qaBj2PYBG1CFQVwIEST5tyz8LduD63djxCiANe44aJBIB3gZFsxInWkLlJntG70GyN0s5cwtH652UxPiBk3uCxDdpp9KeWpyCIiaFYvw13swdC8atvWiOQYhKVilbu8Gw7yQ6koOTbmf2tjzZZzOH4QPph5re3w1mjAaK1pRKLFJbelTEVhc0TQyXUYB_0mqtEbJmM4p4DdU3wFc1fr8C3kXCPy__Z8UD63aVfJpYQHctzf3Nk_fbUGtyo9Rgkdb7_qvvsueKE_qIMEgkQB1iFgCPY0XcTGw-_0FECbToRAjgq6Tt-lRR6c8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال رضایی: آمریکا به دنبال عبور دادن ناوهای خودش از تنگه هرمز است
🔴
آمریکا در عمل زیر تفاهم می‌زند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/132330" target="_blank">📅 23:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132329">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbbDwjEZozu0WP_20M29k5sXm6-AU0A7OMo8mg0w0-bF4R2onSu3bv-CRW8sn0E-r39KvCQ98dR41igr4Zu-VPVyiggwnpsASxMkEpwmvdQWz5wCkZqTh2XUqU6KgxhkoGc-TvfUDNJntvmIKcD-I56VaR9lAfjwFJeTZSsgZijuaPFOa70XuzTHNZ69T-fOJ7Q0OYomOwSCaqs8Um3UDf6opAg1TPAtucUuXxRA8tZxQ5zKEe6vCj1rCwZc9IINJpjIPl6oz1CqwxzlgL4-Ev1_QUlSV0jlTpWbNg2svJRAzXKsI7jlQ6umCKrdUF-GK1jE3bacfVeEhCynmsCtAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان قصد دارد قیمت نفت سبک عرب را برای ماه آینده ۱۱ دلار در هر بشکه کاهش می‌دهد و به ۱.۵۰ دلار پایین‌تر از شاخص منطقه‌ای برساند که کمترین میزان از ۲۰۲۰ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/132329" target="_blank">📅 23:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132328">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mb2nyJTF8-io_BzuHup2N_lW5DRpUNg05PjMDbJMfJw7wmbQdtZ4AQ2DgUs5qwp2pD2Ukt2VKo76RB9cuWbJOnHwwN5ehS0cyrEILBNJYKuPTuEd9Ol8iDyplMw0uaUwKTMb6Z6U4yoyNjiritcHjf2QeeDSQC5AL-K87KAgD8mfD2_MpFa4v_YEG_h_z_lyRqzr9wIy97fcLkswxSc3x_iesPDr-zH5bq4SB9t-amIz7XBVpDSiteWb2ORO2bJCSa0RduwTpNQVarmtTdRfLKlUrBmA3Z_Eiha6XqNRgwWFjF4j5bDCTp0hhh93M9dUvNST5iWMA0TK6ahaVJzb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراق قصد دارد از طریق خطوط لوله نفت خلیج فارس را دور بزند و ترکیه بازیگر اصلی این جریان خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/132328" target="_blank">📅 23:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132327">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
کل عراق فردا چهارشنبه تعطیل رسمی اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/132327" target="_blank">📅 23:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132326">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
قیمت نفت از ۷۶ دلار گذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/132326" target="_blank">📅 23:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132325">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
مقام آمریکایی به آکسیوس: تفاهم نامه به عملکرد دو طرف بستگی دارد. رفتار ایران در تنگه هرمز درست نبود و این دلیل تصمیم گرفته شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/132325" target="_blank">📅 23:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132324">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ایتامار بن‌گویر، وزیر امنیت ملی اسرائیل: یک هفته قبل از هفتم اکتبر، من گفتم: «بیایید عملیات‌های ترور هدفمند را در غزه انجام دهیم.»
🔴
به من گفتند که من دیوانه هستم و اینکه درک نمی‌کنم چه اتفاقی در حال رخ دادن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/132324" target="_blank">📅 23:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132323">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152e43cb9e.mp4?token=qegK9pAYfAbdCvMK7lIH4eVLP2gF_9HPqnmMGE7fcIlgcedz_n0OJBvEQrutLIJLK_c1F8z9QA1fDhd-nF5Ash_SqkqmLrUNCNfbKG5czEIKNke0adFwkrsP6BbpQ2wBM-pmopJUXUqZSw-e0yo2YcliRLRqREtO3TFSBa9i6YX3gjoWrC1Bo_DgBdy7YGjzah5jsl9KUPnYNAU5ztejtiyD3YhrbUyetFgC0wNe0g3AVMLPgCfN6vRzUo_DP8mWoUaMCbBhTlDyxt7RoSIXr8yaOFB4s3cg3224rBdKdl74ZlxYZZBbCIBBd9_m_8tFiVU1ZMe04VTc02wGelDFk0TZG6HMD3nvjMj-hDYSQSXddZ3_lH8VJX-RPPK0aTZaNHBvXfFWjUaQ6vEMmbFmQGtHee1Lf5fNUeUFvzrFpsqcSrP2Lv4XjcrW_xhi1EwpLrrIH0csrwWEJk67Q3KfWpx3zv96iirhdiNuhuMOIUXEWgJrrr6S2z_FL93Wl2mNXmLODOh6PkNCPDgvhrMytl1eGkZ2dCXdRRjJsdGbKHYG2f4BTM-fLS7xEVhaSN2s98EI44JOSeCLIqpr3BNzbeOeTyfuC6MxgLRDBuJZxW_8F45Rkfrms8EwejcIHZo4kukPV5qCQxsCqicNRdzcvuVKmkfFIFSULrUHBwkr5AY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152e43cb9e.mp4?token=qegK9pAYfAbdCvMK7lIH4eVLP2gF_9HPqnmMGE7fcIlgcedz_n0OJBvEQrutLIJLK_c1F8z9QA1fDhd-nF5Ash_SqkqmLrUNCNfbKG5czEIKNke0adFwkrsP6BbpQ2wBM-pmopJUXUqZSw-e0yo2YcliRLRqREtO3TFSBa9i6YX3gjoWrC1Bo_DgBdy7YGjzah5jsl9KUPnYNAU5ztejtiyD3YhrbUyetFgC0wNe0g3AVMLPgCfN6vRzUo_DP8mWoUaMCbBhTlDyxt7RoSIXr8yaOFB4s3cg3224rBdKdl74ZlxYZZBbCIBBd9_m_8tFiVU1ZMe04VTc02wGelDFk0TZG6HMD3nvjMj-hDYSQSXddZ3_lH8VJX-RPPK0aTZaNHBvXfFWjUaQ6vEMmbFmQGtHee1Lf5fNUeUFvzrFpsqcSrP2Lv4XjcrW_xhi1EwpLrrIH0csrwWEJk67Q3KfWpx3zv96iirhdiNuhuMOIUXEWgJrrr6S2z_FL93Wl2mNXmLODOh6PkNCPDgvhrMytl1eGkZ2dCXdRRjJsdGbKHYG2f4BTM-fLS7xEVhaSN2s98EI44JOSeCLIqpr3BNzbeOeTyfuC6MxgLRDBuJZxW_8F45Rkfrms8EwejcIHZo4kukPV5qCQxsCqicNRdzcvuVKmkfFIFSULrUHBwkr5AY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حمله وحشیانه آدم‌خوارهای عصر حجری و بی شناسنامه به عباس عراقچی
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/132323" target="_blank">📅 22:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132322">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
یک مقام آمریکایی به رویترز: مذاکره‌کنندگان همچنان با حسن نیت تلاش می‌کنند تا به یک توافق نهایی با ایران دست یابند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/132322" target="_blank">📅 22:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132321">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slFc3ho11BB7ahRLxKr-MVcNJ8nGOHHWBasLjct9NvUIoNY2m4HCFDCUnl8HRYafQZql8j5vWWn18zGrOpMY8d9mmZvguYooF0bIpjXrnWz-4XT5SleGDzjz1m9H0WKl82enu03Gkc6aDhALVfPZEkD5AD360iJ5zlNFYwfMv3HycNAK8LLXxl1xyJjaYKyrWI2x5abRnFgKxl7eM_yAuKUbswrtXpYBEIVyNV3z3YKUzBIW_bXk_OBrYX4cL6TIhtMGX74R_ViKuAakpluYv5HrAl0mkybUxwjwujnL93jHf2ZUyCc9ZD53bEpbloXQ9PvQcSQscOAzpe-14LqHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت‌ نفت پس از لغو مجوز آمریکا برای فروش نفت ایران، افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/132321" target="_blank">📅 22:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132320">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1BcrLo8pKQhoxHXWnuGT_VrDvC5ZAUvWTahiZ9d38Ca_PJ6xIEAt5h2M9ed0AYBypEC_N_8mYaqA-qpNbv3HtPdjTSMar9PQAiCTKu4U83Qz173SHI1xH9Exb1ayVqLJUUIPNE8apPfL1-ooEr1tabwS57UlpV-NrVJ9dM9YOlGocJ4dIlgQqFgDKac1TbBbf16BFzRFDp-_cHaEO6zHJk1Klv2lZpI76CZsDr-ym2eOk7d7e5kI-7PmYw6sh7zZ7uxmInrRR9P4uYn4X2dJd4D4eZbiFbh_6q2jhaxMf1SIzRdimqK3CNo8CDWlkJoZadlc6Shczug1Xyet6JhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام ۵٪ افزایش پیدا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/132320" target="_blank">📅 22:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132319">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
قیمت جهانی نفت در پی لغو تعلیق مجوزهای مرتبط با فروش نفت ایران از سوی آمریکا، روند صعودی به خود گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/132319" target="_blank">📅 22:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132318">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
قطر معاون سفیر ایران را احضار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/132318" target="_blank">📅 22:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132317">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری/مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند
🔴
یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
🔴
به گزارش خبرگزاری رویترز، این مقام آمریکایی هشدار…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/132317" target="_blank">📅 22:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132316">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6798819134.mp4?token=SutHSrx6Cv340uAy29OocWIACH9CNYqMZMe9WtQajo1AovetZBRGEHShPhXQXnkCjp39GcQxtnRsS1JdmRBNj40r2le1HcW0ZmtVlnv4ITLJxzVYsU3ke3vsj3dhXMXkWFTYh8ziCjhzYmQK7-5XPrj_SpAFtT2qhgQNbBcfypg68-3v4BqmiggOloFuTPPR4aBd-7-a6GUl0OqTVVMsyq3P7MIs4ejWHjx0CZG2LoMOmik9pc_zPAlIiw-neLQPu5J-tV5PNTCDvjkBeYBLFmkU9sAVrWUgGn0bo4doNBaA8T3jISWwbD5Uv_XqKBoKCjlupotUpl8S3xxZc1pCqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6798819134.mp4?token=SutHSrx6Cv340uAy29OocWIACH9CNYqMZMe9WtQajo1AovetZBRGEHShPhXQXnkCjp39GcQxtnRsS1JdmRBNj40r2le1HcW0ZmtVlnv4ITLJxzVYsU3ke3vsj3dhXMXkWFTYh8ziCjhzYmQK7-5XPrj_SpAFtT2qhgQNbBcfypg68-3v4BqmiggOloFuTPPR4aBd-7-a6GUl0OqTVVMsyq3P7MIs4ejWHjx0CZG2LoMOmik9pc_zPAlIiw-neLQPu5J-tV5PNTCDvjkBeYBLFmkU9sAVrWUgGn0bo4doNBaA8T3jISWwbD5Uv_XqKBoKCjlupotUpl8S3xxZc1pCqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: چند کشور و سازمان به شبکه‌های اجتماعی نفوذ کرده‌اند.
🔴
آنها از این فضا سوءاستفاده کرده‌اند، به این صورت که از ربات‌ها و سایر ابزارها استفاده می‌کنند، به ویژه با هدف تأثیرگذاری بر جوانان آمریکایی، نه تنها برای ایجاد نفرت از اسرائیل، بلکه برای ایجاد نفرت از خود آمریکا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/132316" target="_blank">📅 22:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132315">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzTrWAMzBUlabXVwVk-kufsO7nzDveOOhsGCkPfagPeV_fbgi3RJHlk3ef6mImHHbXBVKV0jmRcnf_ONMyKoh4rwJrbOFAPwxPhfMQ-Pg60cyxaEPqIcerW8BDKYEOmtyEUFv4asIkWXs9jVtF0rdWCZ3fv36H5EIbw9p4d9C9Z_7SYgxeRwdhrZMI9w8PBqU-MXWWhDf6rxTO2psVikstLd-iJsRxnTK6KrHVOPyMCqYO1lngKrkE4sHRpVE4gZro3rxVrMLRyCzF44qmyLRUJmrhtNQWAASnwAOwfSvpacobV7G-7yIUjDP0GpqxF2mkLf-vFD7pqWP0vN2oDHEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز به نقل از مقام ارشد آمریکایی : کاری که ایران تو تنگه هرمز انجام داده
🔴
از نظر واشنگتن اصلاً قابل قبول نیست و بی‌پاسخ نمی‌مونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/132315" target="_blank">📅 22:38 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
