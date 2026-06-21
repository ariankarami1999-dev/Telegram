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
<img src="https://cdn4.telesco.pe/file/Mqp4b6MVJutlKUoaHv3Sd5VFu9uSE30R2iJsqVub6gWTOZ42nClqmjnCKG-ohFdRxFLL75yY2PEIhHyVtGAugG9fBrP3id2j-i2libHd3TWahGb5uJKacBODhbAgcl0NM0PyT8_UEgmR_jva7nw8_-4HxcaO1R9U2mlJaFEDdXeeZ8H2Fc0BKE3pNEuPhZD7LlcFvtDz9_qDJX2T0_-8JYfHY6dBcrR9oGW-ia9t4oL1hzOfsTiLlZBF4__POWilEeGmvxXhCGIFMLgFM4JutPqX5NW5WwVRtiRX2z_PM49yxhY5ucBD0O8MGPPAnaU5GhoEU5RN1dQHySaR8FyHzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 955K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 14:21:26</div>
<hr>

<div class="tg-post" id="msg-129526">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
پزشکیان: ادامه جنگ به نفع هیچ فرد یا گروهی نیست
رئیس جمهور:
🔴
ادامه جنگ به نفع هیچ فرد یا گروهی نیست. بر اساس همه تحقیقاتی که در جهان انجام شده است، هر جنگی موجب اختلال در رشد، توسعه اقتصادی و اجتماعی و افزایش فقر و بیکاری می‌شود.
🔴
این سخن به معنای ترس از جنگ نیست. ارتش، سپاه، نیروهای هوافضا و مردم ما نشان دادند که با قدرت در برابر تجاوز ایستادگی می‌کنند و اگر جنگ ادامه پیدا می‌کرد، با قدرت می‌ماندند و مقاومت می‌کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/alonews/129526" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129525">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjrjnvKteWIN3RYTWBwInNWKjzUfK9mEJ2zRfH4F4J0ETIDMliGDXgCpACDx_mrl1403DY7ffKtmMJKkRCOG8XyrVx_-GwslkIeVwnehRoYmHoZv2FJUTy6oHbLNzjd2w4us7wiPOumD3Q6g793VBK6H6E99nII32L3RBRB1ux6fPReI3VgrPKOTtoAgHqZWOomgxgd61M2xge0O_-sTXpv89tgNWTYFXtPZsOaPHCdaNs8TTpbP0FgjiRmz9QfVbVXmFcprmx_7QsIGT0WBsEGwj53pSDnLx37YiiRr_V8kxyKraRhqFwh3OwJ5ieKU652S4oc3Yxt0BETSvKq-Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیام ایگنازیو کاسیس وزیر امور خارجه سوئیس پس از دیدار با عراقچی
🔴
جناب عراقچی به سوئیس خوش آمدید.
🔴
در نشست دریاچه لوسرن، ما چارچوبی برای گفت‌وگو و تبادل نظر فراهم می‌کنیم.
🔴
در شرایطی دشوار و پیچیده، رابطه مبتنی بر اعتماد میان سوئیس و ایران، که در مأموریت ما به عنوان حافظ منافع نیز بازتاب یافته است، همچنان در خدمت دیپلماسی و در راستای صلح و امنیت در خاورمیانه قرار دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/alonews/129525" target="_blank">📅 14:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129524">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
پزشکیان: در شورای‌عالی امنیت ملی تقریباً همه اعضا متفق بودند که این اتفاق باید رخ دهد و تنها یک نفر نظر متفاوت داشت که وجود یک نظر مخالف در یک مجموعه نیز ایرادی ندارد
🔴
مقام معظم رهبری به دولت اختیار داده‌اند تا این مسیر را دنبال کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/129524" target="_blank">📅 14:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129523">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4776c5951.mp4?token=cuLlRRlXyHUdJV3AYuhsBgJaJOWmRcZL4bRfEkjdAQ0vjlJX2bEfG0Abwx-wSHIrqzqBcq8PgUzGQTFJTtU_d9L-rdqAZJKAtGGRr75MThztxkLYRkXx4j2ai-FmOI9nB68yZR5udKyA0SE3n2lYK97laP8ocQgcnAI4OxAI2_Rxic5d9yw3w3FKSmQsI_B0iI5s9_UVnQrOU0sc2vs66l9E1Z2iFWJF66H_rG9uw8krESupAfTvK-t1Izx-msAm--C9w2uoJCE3oh52xqO4AZYYceUvaXuuSZWA6yEkJyfdMmOt3sCTGD7UW4nr5I7wCNfIlXChIVSc03x_sIQbIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4776c5951.mp4?token=cuLlRRlXyHUdJV3AYuhsBgJaJOWmRcZL4bRfEkjdAQ0vjlJX2bEfG0Abwx-wSHIrqzqBcq8PgUzGQTFJTtU_d9L-rdqAZJKAtGGRr75MThztxkLYRkXx4j2ai-FmOI9nB68yZR5udKyA0SE3n2lYK97laP8ocQgcnAI4OxAI2_Rxic5d9yw3w3FKSmQsI_B0iI5s9_UVnQrOU0sc2vs66l9E1Z2iFWJF66H_rG9uw8krESupAfTvK-t1Izx-msAm--C9w2uoJCE3oh52xqO4AZYYceUvaXuuSZWA6yEkJyfdMmOt3sCTGD7UW4nr5I7wCNfIlXChIVSc03x_sIQbIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار تیم مذاکره کننده آمریکا با شهباز شریف
🔴
تیم مذاکره کننده آمریکایی به ریاست ونس امروز در جریان مذاکرات چهارجانبه ایران و آمریکا با مشارکت کشورهای میانجی، با شهباز شریف، نخست وزیر پاکستان دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/129523" target="_blank">📅 13:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129522">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o590J0qTLJfN9oJDk5POoL-YW9dJXTtgQJ5NvQO3Z8xfCMETU98NcrhTaBvMh76Wxs7nd2lYKqH0skt01KFwmv67kO7xVNYpcIG7a2UzJf56FOL2DTAkBMKpo_p1LE-I3QFgFgUjvlYeyuREKX-djaoTzUYWetkB2sEwB-AekUqOGXnKkD1FQpTZvVY_pmtTW4rrlRlHXEROs1BJ6vDPw34jHMz_eOxGdtr8O0guwu77kZwgXRRgOiODyNBGN6iWjaH4ZHe9sr4yTrAsdI934sRggredMEQnb8R3h6eW8NfCGSwCzodKS9aFzzV0b8_p9AmtNXV7srsCZTVY61aFqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیر کل آژانس بین‌المللی انرژی اتمی گروسی گفت که با وزیر امور خارجه سوئیس کاسیس در بویگن‌اشتوک دیدار کرد.
🔴
«در این لحظه حساس، مهم است که به دیپلماسی هر فرصتی برای موفقیت داده شود.»
🔴
گروسی همچنین از حمایت طولانی‌مدت سوئیس از آژانس بین‌المللی انرژی اتمی و تعهد آن به دیپلماسی تشکر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/129522" target="_blank">📅 13:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129521">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
پزشکیان: دوران محاصره دریایی یک بشکه نفت هم صادر نکردیم البته طی دو روز گذشته ۱۶ میلیون بشکه نفت صادر کرده ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/129521" target="_blank">📅 13:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129520">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
شهباز شریف نخست وزیر پاکستان با ونس معاون رییس جمهور امریکا، در حضور کوشنر، ویتکوف و فرمانده ارتش پاکستان دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/129520" target="_blank">📅 13:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129519">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68daaf45ba.mp4?token=oshJPjd0OPh6mK1QFQ1_szVPXkLMtUN9CmwH2DtgHD5juk3ZsfFqtQvek8B7BR9szSaQjv6bYdKxah2Ukuz0v3a7RFPsExH5p1KEJqWyBIntcXTTTpivjLob4FdL4ocvLmjyuDipnFUt8W4QzMWxJLr8RxBVJCUuwmTRtislh8mFsGHhTJrq9peSC2oQ8AINgBj7m-nu3U6xFYIOo-Ws1CDekEcJwCFMl17nYM8TiSqq7fX5CWDlMP_mSqza3DRhPpnBvCHsjgyYh0PpVW34YcJHb3RfdnEOQ1rMPoknsZ3ES_jI66pYYZ6X4Gshl9g_aqdK9SzVhJrHiqkE6ZZ7nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68daaf45ba.mp4?token=oshJPjd0OPh6mK1QFQ1_szVPXkLMtUN9CmwH2DtgHD5juk3ZsfFqtQvek8B7BR9szSaQjv6bYdKxah2Ukuz0v3a7RFPsExH5p1KEJqWyBIntcXTTTpivjLob4FdL4ocvLmjyuDipnFUt8W4QzMWxJLr8RxBVJCUuwmTRtislh8mFsGHhTJrq9peSC2oQ8AINgBj7m-nu3U6xFYIOo-Ws1CDekEcJwCFMl17nYM8TiSqq7fX5CWDlMP_mSqza3DRhPpnBvCHsjgyYh0PpVW34YcJHb3RfdnEOQ1rMPoknsZ3ES_jI66pYYZ6X4Gshl9g_aqdK9SzVhJrHiqkE6ZZ7nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عارف، معاون پزشکیان : دنبال جنگ نیستیم
🔴
ولی اگه کسی بخواد شاخ بشه و جنگ رو تحمیل کنه، جوابش رو جوری می‌دیم که یادش نره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/129519" target="_blank">📅 13:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129518">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZe-4TiOQ2e-TxMsUWMiIGqD6EVfabbBmLti_IDgJGsojgG_hjqMq5g8f6_zQN_ANCwC7eTuupoiWQ4NeWxgFikQ9j-uO-HLLRapFxVo5LC-jjK9noXsSiseUqY4M6conSTg3YDtPExXl7xKSMeDC-qXynovMPUVQP6NlGLzkkgOJsfDzf4Rj6ZTWwtXnQ2QObyxc1M-bpSmOyXmpiI7cWXEPmJHUHzfM5zvTfzftJ--qwOqGVL90cIB_43Oj9xTSjStNHbGYQgM1T8ZMRYcldcCUbFX6u2W360ubvYGLuwT3jpqLTpGjhNBE7lwMU4yxCpU8syV-T25Ui9QrnYPxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با وجود اعلام توقف گران‌فروشی اپراتورها در طرح اینترنت پرو، ایرانسل همچنان هر گیگ اینترنت پرو را با قیمت ۴۰ هزار تومان عرضه می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/129518" target="_blank">📅 12:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129517">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kiq3d45H-g9kBbEGOf8SgDmqMgIYX0Mte5kZdA6XdmU5XJTIwsntf9c68v4GUE13VF_9WyRRVcqkouQEPJORptCP2XpBYH51p4xao0Ar1zSVDQppMnwjBCqljJ4vAuqYp_zzIg92-AjEBFJawINyLo7KugnVsi4vki398DPU43fA4SZrgHKP1417uA-A2amv07IeYm1ZflR9vTXEhe4PEkkcTuQyGReyapc3bJOcSa29obRZImIjbdYcSJCcPksXmaecfaQIVJrF4llgJee6fnUitHJeKSuNKhNY7nmUZHERuGyZzVxgJkKh2Z8NuZJnLmSYTt6XKV8CdlUcbG_h_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمار رسمی اعلام شده از وضعیت پتروشیمی‌های کشور که پس از حمله اسرائیل شاهد حدودا ۸۷ درصد کاهش تولید نسبت به سال گذشته بوده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/129517" target="_blank">📅 12:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129516">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSn88XApNGJ4uxiocdBok4w8-Hx_T--EnBa5OXE1QRQaZt54aqQxt95a8NVYpuJDtUYnfEgQiHBDki1Z71a434_Iyauu9AMiIJkW6Tpx9MIdD6WpnqNFbcWQBwET-NoYBRzSovJ8OflbgTRerx2bXpn5rOdD-44UhXnfJT-NVM8JD0DjuijToiRMQCdz1E4VfYsJoMITRYIzZRHNYlPW968BQgdrodAzQ78NBoyI0AKx1nStZI1wMRGhJmS3jAwFLeXf6BF55ymRboPNInjJ0DABA4NQYqN2R1lmfkMR2TrCU1syj--PnZEW91MVIrwVUwzPfJeCsLHe6P4qKgWC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان : قراره ۶ میلیارد دلار از پول‌های بلوکه‌ شده ایران برگرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/129516" target="_blank">📅 12:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129515">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/056df7a897.mov?token=R6R25U-UBqnkBKOJtAiQTaVYtHEypAfZkTO_54xRfkslRXsZuzvFfIT7J0vMXwQB2DSCo9iNFwcw2_aHeJmLFkqajC7SacKis3W_PehtUzeimV3dUsHBiLjNM1NYIH5TshQMPATFARQXOec8GadiH1M0OZy0O_6xUKiZ3ejdNSxAgSR47DsAAiJnRYBSNg3V9wJ9fWFEXCWK_1quRkJh0HbH2k9tNSSJWucydEFwKFVPyU4HK6rC01VhFEW6pJxn7wPB82RfC4qZs7XAViTNcbw9onh82_CeZT0hLnpSzfKByDNsqQ2TCyR8USuhtwB3nY3j7FC5JlOXLtTEi1SOew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/056df7a897.mov?token=R6R25U-UBqnkBKOJtAiQTaVYtHEypAfZkTO_54xRfkslRXsZuzvFfIT7J0vMXwQB2DSCo9iNFwcw2_aHeJmLFkqajC7SacKis3W_PehtUzeimV3dUsHBiLjNM1NYIH5TshQMPATFARQXOec8GadiH1M0OZy0O_6xUKiZ3ejdNSxAgSR47DsAAiJnRYBSNg3V9wJ9fWFEXCWK_1quRkJh0HbH2k9tNSSJWucydEFwKFVPyU4HK6rC01VhFEW6pJxn7wPB82RfC4qZs7XAViTNcbw9onh82_CeZT0hLnpSzfKByDNsqQ2TCyR8USuhtwB3nY3j7FC5JlOXLtTEi1SOew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیات جمهوری اسلامی عازم ساختمان محل مذاکرات شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/alonews/129515" target="_blank">📅 12:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129514">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9S3zJ5qGoN2mLBo0bLBBzZYwa_INHg4dPzjLkzSNXczPHtJmDL-ciZGcCCChcN6m8ej8Qf1okmdkGvVAN_u4ZGeKm3Ed3bXCZ6Z-WwSqOFvHb-4Fa8x7Ue3HDsNfYpjz8dIShyd-cQ7Cu9kDjOWe6cIUL6nyZd8Tv_3RmKxIH2maXnNjxDjILcYDqnCwg6hXFShV-xEWEt-qgUNMAqJmENxanTaiWnU5-4B3zD7maVo3diD6NsBRSoOdTRRxDtp_zCVdHLVV6zM546nQKJ653zMtNai6bFPvmxBpfmL3zwI5dbrpcRxIzDzO8SG5wIE4V7J_UMowDyMckrFPyQ3IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نمایی از محل مذاکرات در بورگن‌اشتوک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/129514" target="_blank">📅 12:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129513">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
هیات جمهوری اسلامی ایران عازم ساختمان محل مذاکرات شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/alonews/129513" target="_blank">📅 12:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129512">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایران:
برای اطمینان از اجرای یادداشت تفاهم به صورت مستمر از طریق میانجی‌ها تبادل پیام می‌کنیم
🔴
در جلسه بعد از ظهر، هیئت‌های نمایندگان هر ۴ کشور در یک اتاق حضور خواهند داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/129512" target="_blank">📅 11:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129511">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایران: قرار است یک جلسه یک روزه داشته باشیم
🔴
برنامه‌ریزی به این صورت است که صبح دیدار دوجانبه با هیئت ‌های قطری و پاکستانی به عنوان میانجی‌های این روند خواهیم داشت
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/129511" target="_blank">📅 11:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129510">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
فارس به نقل از یک منبع نظامی: تنگۀ هرمز همچنان بسته است و نیروی دریایی سپاه نیز تا اطلاع ثانوی هیچ‌گونه مجوزی برای عبور شناورها صادر نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/129510" target="_blank">📅 11:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129509">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایران:
قرار است یک جلسه یک روزه داشته باشیم
🔴
برنامه‌ریزی به این صورت است که صبح دیدار دوجانبه با هیئت ‌های قطری و پاکستانی به عنوان میانجی‌های این روند خواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/129509" target="_blank">📅 11:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129508">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
اسکای نیوز عربی : پیش از شروع مذاکرات ایران وآمریکا، جلسه‌ای بین هیئت‌های ایرانی و سوئیسی در اقامتگاه بورگن‌اشتوک سوئیس برگزار شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/alonews/129508" target="_blank">📅 11:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129507">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
حمله بن‌گویر به ترامپ: باید بدانیم چگونه به رئیس‌جمهور بگوییم «نه»؛ توقف آتش‌بس یک اشتباه بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/129507" target="_blank">📅 11:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129506">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
تمام مفاد تفاهم‌نامه امضا شده بین ایران و آمریکا به نفع ماست و دستاوردهای این گفت‌وگو و مذاکره عیان خواهد.
🔴
ترامپی که ما را از انجام بسیاری از کارها منع ‌می‌کرد، در سخنرانی اخیر خود تمام آن‌ها را حق مردم و ملت دانست.
🔴
۶ میلیارد دلار پول ما در قطر برخواهد گشت
🔴
نتانیاهو اولین ناراضی از مذاکرات است.
🔴
تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم.
🔴
این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/alonews/129506" target="_blank">📅 11:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129505">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
عراقچی و وزیر خارجه سوئیس در بورگن‌اشتوک دیدار کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/129505" target="_blank">📅 11:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129504">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
پزشکیان: به‌زودی مبلغ کالابرگ را افزایش میدهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/129504" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129503">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
یک منبع مطلع به ای ۲۴ نیوز:  یکی از اولین خواسته‌های آمریکایی‌ها در مسئله هسته‌ای - اجازه دادن به بازرسان آژانس بین‌المللی انرژی اتمی برای بازدید از سایت‌های هسته‌ای در ایران به منظور بررسی وضعیت به‌روز شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129503" target="_blank">📅 11:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129502">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وزیر نفت: پس از توافق، کشور بزرگ‌ترین سکوی سرمایه‌گذاری خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129502" target="_blank">📅 11:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129501">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
تنگه هرمز هنوز به صلح نرسیده است؛ با وجود اعلام صلح، بیش از ۵۰۰ کشتی همچنان در دو سوی تنگه هرمز در انتظارند و بازگشت به شرایط عادی زمان‌بر خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129501" target="_blank">📅 11:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129500">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سی‌ان‌ان‌: در جنگ علیه ایران، قدرت نظامی آمریکا آن‌گونه که واشنگتن تصور می‌کرد، قاطع و تعیین کننده ظاهر نشد
🔴
در چین برخی صراحتاً گفته‌اند که پکن از این جنگ سود برده
🔴
این درگیری بر برداشت جهانی از چین، تأثیر گذاشته
🔴
جنگ مذکور قدرت بازدارندگی کلی آمریکا در موضوع تایوان را به طور قابل توجهی کاهش داده
🔴
بسیاری معتقد هستند که پکن در بهار امسال، تهران را به سمت مذاکرات با واشنگتن سوق داده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129500" target="_blank">📅 11:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129499">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فوری / المیادین نخستین نشست رسمی در سوئیس ساعت ۱۶ به وقت تهران برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129499" target="_blank">📅 10:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129497">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S1EuP3nqA2bZEpZMgjoQfquMO1d-wxnFNqKFZWHM9eb6tGelJAuR2XKNrwIBW3-BEgZVl_amx2_GMhsej6_mZ4AYwzWfYrgIcMkJv7KTt75tdDnZhI0dGfm9KnyZ486Y7l2IfUooGx-APk-TEV_nogUHbOilcpElt6IzIOvUGs6itOOQbHLzGyZ2aTieTVCEuogAe3XvQBPSMHeMNnkLhXVAweRUWZg1RpymcQxafZ0YHDYMXiLO7_vOni_9sgU6vbxxb6sU-SMwefemVqjGVJLn7Hn88cvB9I5tbRAakjOZtGFElYeu9imL2PPcVlVMJt7tll7ww7EGz7u1rxQ4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHqbxv99Kgst0z_NDRO75nzMj8RScq3ACh8sK9Ja9EWmUo7aW-41Yn7_vA7LcfasaO3UagkwYCBt5rquUwJGAXEOUQKELLfc3hh8WQGe3Ucx7gEmSPyB2N73eLaPyKVLfl1jfA-USDPNdAfyRtZpxwPNcdRyxNXuhPopluNjH4yXstK9Lo8a0fCjyvJ37VIT7jOBw74uHkOVhgCzIpyYT9p7UCpbKMWC1UWJIpvR-Ss3t8mVcMEecUpDSNvJh-QhHsgYr8z1ZpvOX7JasIZ2hsw8roD7pHlsKGm-xkiBydx6yc3xK6fDoDqvj3TO1FqD5JW2jTqwcsx_btlzlQBI9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پرادو ۲۰۲۵ در امارات ۵۰ هزار دلاره در ایران ۴۳ میلیارد تومان ، حتی اگر دلار رو ۱۸۰ هزار تومان درنظر بگیریم و ضرب در ۴ بکنیم هم به قیمت ۳۸ الی ۴۳ میلیاردی این خودرو در ایران نمیرسیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129497" target="_blank">📅 10:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129495">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6knQXqsG7tV8jVjMiyHDRs2PI_C0eO9lhE1MfCxrTflUbkKipH10DcQsdeB9G-PGdnXjAEYQLiiTSSZJ_sFJMORAuUWPE34j59qe6_WwWkye4yJtxihUw53hCHLd_QDgpNxjpvFmJr9rCJg7m_LqeJmIxW5VpzhY8BhCoUfG7cSJFMrFt3Oleg2Q9WaF0njDo6KKTHuTGCBAWSIHKwXh_F7kdJmVIIJ1Y0Weoexokj9N0Prt_dUIP4W-9lo2OhruXLypX0Dzy7bdGrgZrG9BoskeKTGRVYDpW5b02WpmOQVeUYKbc0W3AVgJJuqnitgh1GVBmeMk9A3LtxfIYjKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CrxjDcBIWg_oq54VEmT9qNVlWDw49NyH6kdL2mjH20_dO346COTywOWzPgTuZklSeUaB7TBJjyABPWRGluRexDsRo8bOVWZvSPbsgyr9bBxQwbaPdWHfCyqKxYvRbDGYdOe2wDczhiRUkN-v7sa-IssGB_ELqHenEQ1OEBHdbvGGsS0MBDAHaPcYK_AKiq28Og6Oy8XHdp_zQUJ85RSxBWPzQcN4XqMlfUXtxmZMgPc28ITo_XZm6gy5MRVk8lURu9p3GwdrKRf0d4WwGIm_2y2B4gPLxeWT_w73UT9BocPNtZktRkFd4769xCCJT3iDkCPxcGg-AgDEIMfef-fljg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از ورود هیأت ایرانی به سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/129495" target="_blank">📅 10:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129494">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار در دزفول
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/129494" target="_blank">📅 10:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129493">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ: شاید اگر توافق با ایران حاصل نشود، برای عبور از تنگه هرمز تعرفه وضع خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/129493" target="_blank">📅 10:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129492">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw4e8aOt4y63Ol5cYdd2JM5wGsOou8hyn0mFEZd01yJF68zMWH6dBT6BoekIK5QTz2lH4bVWBkJLRGA6x0jMyuQ7W5ueteyIMK1B2jhGVMrf0iUabgP-WzTe_bkBXWoIvywlrIrmDSRFb3hMPAgkL6Y_kAplPzOWlUaZ2LjQKU8f9VE6PYKk34LWE5jpGATyDTX8ZL_mFxQTlsX2q0CdjLDySfxe-5y1SKtfg0QOYA96rik4N3i-SAIkOqAdp2iwP8NkuhzAD9e8stQjoTsLhVtOjb4wYYkT0omcy1BEasvVAGl4RN1e6CaDX_FhwiDxapSqK1WuU752qtL7cfh2Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی: هرگونه خوش‌بینی مورد سوء‌استفادهٔ دشمن قرار می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129492" target="_blank">📅 10:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129491">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
الجزیره: شکاف در روابط ترامپ و نتانیاهو به اوج خود رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129491" target="_blank">📅 10:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129490">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
خبرنگار الجزیره در نزدیکی اقامتگاه بورگن‌‌اشتوک سوئیس : ظهر امروز به وقت محلی قرار‌است مراسم نمادین امضا و مبادله متن توافق مرحله اول میان دو هیات ایران و آمریکا برگزار شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129490" target="_blank">📅 10:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129489">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سی‌بی‌اس به نقل از یک دیپلمات شرکت کننده در مذاکرات سوئیس: ادغام پرونده آتش‌بس لبنان در مذاکره با ایران، یک تحول راهبردی برای دولت ترامپ به شمار می‌رود
🔴
دولت آمریکا از راهبرد جدا نگه داشتن منازعات مختلف در خاورمیانه، دست کشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129489" target="_blank">📅 10:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129488">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5Y7_AD99Xqg5AWTwFwd2J5mo7MKvaMCtXNq1d9CQpJAZh0yIMBM7Wr7iwadhmVumadewmVwi1hdvlPoN2OiCygOj5k5NOf_jYg8oUQPqIXfTvJ0sjDAsE0gubCYfZEdfixAMv2aoz_C4ki-uU8pyi9F43x7IlP3YlrTmJXeAfc2IvIKvPQaxtcqq-_cb8plvjV054MG_z7S4BcDcQ0gF4AP2plLvLtTJjudRFTrO51vY0Y17JAh0h-4SDAdt04RJsuh0t8YlstQG0mcLAG088cxLkKPuyRK1lqMw5l7YJy4XnnTSiVfhRPAR926c_aT8apQXWPH3BJXHY3hhTaO4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترمینال سوخت کرچ که توسط روسیه اشغال شده بود، صبح امروز با حملات پهپادی اوکراین منهدم شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/129488" target="_blank">📅 10:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129487">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
عاصم منیر، فرمانده ارتش پاکستان لحظاتی پیش وارد سوئیس شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129487" target="_blank">📅 09:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129486">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
عاصم منیر، فرمانده ارتش پاکستان لحظاتی پیش وارد سوئیس شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/129486" target="_blank">📅 09:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129485">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک منبع دیپلماتیک: پرونده لبنان نخستین موضوع در نشست اضطراری خواهد بود که به مذاکرات سوئیس افزوده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129485" target="_blank">📅 09:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129484">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193ac2578c.mp4?token=Owld_K1ZeG4v3qbD5np5LHDlHi8GmauVwy7ivRDMlw_rWMtPLg3JcbrVRE5ixbnB8cLfxn1Tn5xlQdx05NU6BFaEncd5eLtW4TeJQbh-eKYP9xGNh4YZ6ugdPU8c6MzAIjV6CEUltTI1bKVwpgpI0_aj0v36zqLqZP0aS9PC1qGv_7gPVP-otBPoo16ZKKR2oicSnAw2h2XiuVnfZJfg4d5zc3x0jTtA97e0iOhmFTfyFYnqHYWdiP1oHylTRysjE2uY1rGRpV7lTzoEmbball-6C5OtsQFsSspDfAj4BUcU2hWFpA389HpdZdYkJ8n5gvM9uYWLPRs74MS3v6C8tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193ac2578c.mp4?token=Owld_K1ZeG4v3qbD5np5LHDlHi8GmauVwy7ivRDMlw_rWMtPLg3JcbrVRE5ixbnB8cLfxn1Tn5xlQdx05NU6BFaEncd5eLtW4TeJQbh-eKYP9xGNh4YZ6ugdPU8c6MzAIjV6CEUltTI1bKVwpgpI0_aj0v36zqLqZP0aS9PC1qGv_7gPVP-otBPoo16ZKKR2oicSnAw2h2XiuVnfZJfg4d5zc3x0jTtA97e0iOhmFTfyFYnqHYWdiP1oHylTRysjE2uY1rGRpV7lTzoEmbball-6C5OtsQFsSspDfAj4BUcU2hWFpA389HpdZdYkJ8n5gvM9uYWLPRs74MS3v6C8tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش پزشکیان به مداحی که می‌خواست با تیغ، حلقومش رو ببُره:
🔴
خو فحش بدن؛ هر چی بیشتر بدن، خدا از گناه‌های من بیشتر کم می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129484" target="_blank">📅 09:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129483">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
به گزارش روزنامه بریتانیایی "آبزرور"، نخست‌وزیر بریتانیا، کی‌یر استارمر، انتظار می‌رود دوشنبه آینده از سمت خود استعفا دهد و قصد کناره‌گیری دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129483" target="_blank">📅 09:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129482">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o0PT_2kU5awM62vadW-x8m51hhu_tfCdLD5oi2ae6K6PHBMxSN9QRZ6kv5Pi9NgTvlOh2_cu85l8tJRU2_FiG5cta4RNbVCcq0THdYz7NCH-MNj0Rn0phU5svh8lEa2PVmyEm1SrKKK3HhkcsLzUpLgY8SM3gAtVky1oF_AYnmiaXmUBLze-RIPKqDQChSH_AgkXi1IGDw4i0-gkrgujVt25HM_LP1LxNbl31Tiwi34_91TQjED0uHadGHiX2F1GYT0G6jcX1hCrISo3w9G9uSFsBSbt0qOh8Vf9421HBdSgah6ddHMPouQ8eOuuHvtRQXTtDuqjx2v2aZCHwpN7cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیر قلعه‌نویی با انتشار این تصویر به شایعات درمورد ساعتش خاتمه داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129482" target="_blank">📅 09:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129481">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
روزنامه وال استریت ژورنال: آمریکا پیشنهاد داد، ایران تنها برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/129481" target="_blank">📅 09:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129480">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک دیپلمات:
یک نشست اضطراری درباره لبنان به مذاکرات ایران و آمریکا در سوئیس اضافه شده؛ این موضوع نخستین دستور کاری است که مورد بررسی قرار می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/129480" target="_blank">📅 09:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129479">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJabPvb1pFkiWwqyp0KF0cfFVTbhBmwCSGoPirIxi5K70ymtml0DbffUw7yqtz7e8Mm1QkRXFLIpSZaYYOLoy0FjMuNVZUgSWyhqoVrS8-KGRyKF8lPBAQFKFborpLzBL1Vlv-yo2CUHCv51FycRlP9t56SJTNxr1L1-tOn0KfAJbckbRMWs36uu9xDnVhgawrnvrbgXqVXyeptVeRS46RXqb0cPG0BrqviXR5HdZ-UhfyqY1j6vydmWnxzRroVzF03QYbXsM95Uj-Wbvt2iaBic9bNpqxtUQXa9sB-zWrq1_AsCoOuixTMxLpabeG10TaKagO14SdTkbUTDgqjBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسین شریعتمداری: مسئولان نظام برای بازگرداندن  بحرین به سرزمین اصلی ایران اقدام کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/129479" target="_blank">📅 08:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129478">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
رادیوی اسرائیل: کشته شدن ۶ سرباز از جمله یک افسر ارشد و مجروح شدن بیش از ۲۰ نفر در حملات حزب الله در لبنان از پنجشنبه گذشته.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/129478" target="_blank">📅 08:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129477">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
خبرنگار الحدث: ونس، معاون رئیس‌جمهور آمریکا برای شرکت در مذاکرات با ایران وارد سوئیس شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/129477" target="_blank">📅 08:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129476">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I93FA1-IW-RrWQWA2luuBnnM633xHp-H3EnoQaN5aazk0WFLg7i-8p9_1ICOUe9yGcpoTvZHZCmmz4c71H7dJukJO1fBDCXu5tOO1IRzhjsxtQhzHDAGRi1_6S94QYATDX3j3W4esiQSwy3ZdJt1oGiQdgU69_nm_Y0m-82D9fbECL-3WBBzAAeiehVBUkAfEQpZiDl52XMLvzMnSaAPgUw4RdF9SsJfrdRNS03LiDlysw3zeLQdEPDWkpH9bpQ7b5DLAeV-jEBZMpoZ9SLT5YZM7UEdOfkznCXZcJtbggNLg6Tix7f8xHHl8vbTxU-YUs775x6yMQe4umLvEbHDDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) روز شنبه، با انتشار تصویری اعلام کرد که یک جنگنده پنهان‌کار F-35 نیروی هوایی آمریکا بر فراز خاورمیانه توسط یک تانکر سوخت‌رسان «کی‌سی-۱۳۵ استراتوتانکر» (KC-135 Stratotanker) سوخت‌گیری کرده است. سنتکام تاکید کرد که نیروهای آمریکایی به گشت‌زنی‌های مداوم خود در آسمان منطقه ادامه می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/129476" target="_blank">📅 08:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129475">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd6e8762e.mp4?token=N4CNkdQegReNyXo8SyiQlVwZSD2zVAZjMkIWuZZNEJcE3ju0hw4gkpDnRy3-O1wj2R0SXJsG8zhRR9l55-wJNMx5CzYnQE1gmoB3qn2jY9fY-4mQpLuKF9g-fXMOxVZWTjcw-zVrHOy9nIvmVabYykq_KoinssHhKAZbcwqLtpL7njo6qlTXdmXMK0lhAxoMnduvlJo3iyQJ2crO8hU03iJ1NPB83D-CSjvf88-AKli1AyiDrEq0YbEOaB3oRpevAzwkRDgU3O4Jb5awZCZEh9a8-LOMhuKXBikio7WDLge8Lg4SgK94pZQ8c9TfzTWyqV1WQqbYGtxLc555hS-C4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd6e8762e.mp4?token=N4CNkdQegReNyXo8SyiQlVwZSD2zVAZjMkIWuZZNEJcE3ju0hw4gkpDnRy3-O1wj2R0SXJsG8zhRR9l55-wJNMx5CzYnQE1gmoB3qn2jY9fY-4mQpLuKF9g-fXMOxVZWTjcw-zVrHOy9nIvmVabYykq_KoinssHhKAZbcwqLtpL7njo6qlTXdmXMK0lhAxoMnduvlJo3iyQJ2crO8hU03iJ1NPB83D-CSjvf88-AKli1AyiDrEq0YbEOaB3oRpevAzwkRDgU3O4Jb5awZCZEh9a8-LOMhuKXBikio7WDLge8Lg4SgK94pZQ8c9TfzTWyqV1WQqbYGtxLc555hS-C4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چند ساعت پیش عباس خوش قدم (سید عباس عراقچی) رسید زوریخِ سوئیس، الانم این شهر طوفان شدیدی شده و کلی درخت افتاده روی مردم و مصدوم زیاد داشته.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/129475" target="_blank">📅 02:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129474">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23c2d0b89.mp4?token=FanCDBxZKjKyM8a8tPVbUvvsAphbH2NjedIbA0s5PBfc8KJqICpPWyJONThMojg6TeQfXI1QttNbFxkslT_dQcC2LBqROklWEGHQBuZ2JveIICqQyye9DawxUujfE-DqVzg5UwKWFTwrAN6W5_lygNc-GvvinU4f86kJ7lwkDD0lqrxIRp9Z9y9DflJ_f0ZJ2NLJF2GuLNYONqw0rym6han3xwPfhc6aMany0LN1OLqQbLDbzEl24U1mH-Cz-VnAdINg0eCVPNaQKM9KxzoyaNVJ3XsQ8gUXburj5jLosNERx4gY_AVCAlnEZpqWApgMSXEErvXRd-9s95E0uWr9mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23c2d0b89.mp4?token=FanCDBxZKjKyM8a8tPVbUvvsAphbH2NjedIbA0s5PBfc8KJqICpPWyJONThMojg6TeQfXI1QttNbFxkslT_dQcC2LBqROklWEGHQBuZ2JveIICqQyye9DawxUujfE-DqVzg5UwKWFTwrAN6W5_lygNc-GvvinU4f86kJ7lwkDD0lqrxIRp9Z9y9DflJ_f0ZJ2NLJF2GuLNYONqw0rym6han3xwPfhc6aMany0LN1OLqQbLDbzEl24U1mH-Cz-VnAdINg0eCVPNaQKM9KxzoyaNVJ3XsQ8gUXburj5jLosNERx4gY_AVCAlnEZpqWApgMSXEErvXRd-9s95E0uWr9mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری تیلیوزیون: باید فرودگاه مهرآباد رو ببندیم تا هی نرن مذاکره کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/129474" target="_blank">📅 01:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129473">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
مراد ویسی: نباید به ترامپ دل میبستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/129473" target="_blank">📅 01:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129471">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qI7rzzWeN7abjxu9EOVhXDakr26DZtjsZCiupAobag8uezbheJwpNjNE-WoIqZf-ATNoSs-3Jc39rbW7NLWAzUwf_I_T-1V4CIaisiqBzJH_1gF7tP5WVavdY3VQYoZbX76k_A6_MFsHYsnjGMyd2qLc7Qk_G8FKbPU6xsNbSPCX-nvBCX3GcYZrSO1_mFqXX14KaKj7QST11NwMKRKANQQUneY8PK1QBvlyjWS2rIw8LaW54xUC-cojZ5utNwW7RMMhfaU0vXryQUiN9fxOhEidFTqaSkfLVcqXLxORmb7h3QmqXQYnyJguCSfpJNmqTEfKYWv5CSrqW3rRUgKa0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gHQUeEqnuR8GtjlwUUkw7yEPcN_asuqID-BJVpbf4lZ3aTDhdzCXz5_4y2ReM3tg08Vz5aSNuKgUQVnfcYDox345oWWYjJ5mHZgvcb9-Osw7Q68BO4d-cJPOjr6p7fe1nef0Hc27pzgnUro1Vxbh7yVikqLYxARYn-9eHOXDpa7tUHZRI4BgNsp5H0aTJWTcGrBb4W1pqmRcag2uCMWEQDzzXsnX1bca1NnlPNsZ-GosYwTbKhUgOu5UWeyTZe4GrhOmqYpNiSSbKVnlqn9lLsMdG_dnYnHXP20DdyvMJS3p0grZxybeQ9F9Aryx4q4GgVGj2EfaYspWwNIsKHJMeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی با پرچم استقلال تو استادیوم داره بازی آلمان - ساحل عاج رو نگاه میکنه!
@AloSport</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/129471" target="_blank">📅 01:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129470">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8f4b679b.mp4?token=IAjQ3Ac6coCjy90FINfyK7TZIeWJuwmRWNGYIMyEeTQl-6UzcSVCctD-CUY2UipaaVD9QjWP3AIe5YzCfO9CATNXTbGGzqXBFGkpp-Vg1cmMBDBg1V25HfHha2pN6XsYUcF29v00sPHoktpPWeCsOxtHWX8fVdabPa5W6mA6pQB74EOmqVQw5bGp6w6POtSHfFjOEr9xCHd0H7ZC2H-YikK1BF3nqZK5fRxVYwn2wAAbM3TfSrYhDR_MyBgXnw0N4XYRQhhdowwi3_wiqCSBoY6CRrxoUG2TVwKHSGAaDRVRQG2P04Miz2KmJ9z7gD6hDspvqp-1joapk7CI9UKZaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8f4b679b.mp4?token=IAjQ3Ac6coCjy90FINfyK7TZIeWJuwmRWNGYIMyEeTQl-6UzcSVCctD-CUY2UipaaVD9QjWP3AIe5YzCfO9CATNXTbGGzqXBFGkpp-Vg1cmMBDBg1V25HfHha2pN6XsYUcF29v00sPHoktpPWeCsOxtHWX8fVdabPa5W6mA6pQB74EOmqVQw5bGp6w6POtSHfFjOEr9xCHd0H7ZC2H-YikK1BF3nqZK5fRxVYwn2wAAbM3TfSrYhDR_MyBgXnw0N4XYRQhhdowwi3_wiqCSBoY6CRrxoUG2TVwKHSGAaDRVRQG2P04Miz2KmJ9z7gD6hDspvqp-1joapk7CI9UKZaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاشخوری عجیب ایرانخودرو
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/129470" target="_blank">📅 01:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129469">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvNAeA8VwsWuNnxSL_3e0Y8ocZV2JoaTmyH0CuDn4fJrEmeDUxxeonctDK45vJvVmiJ0zk-lYxwnFwD8ZoojRm7LH8sR-KREI4u8ho-qL0Evus59zX2DLtglmiv1mgABFTimczGKjfXpr5qddjNp5gdPxxsfshleQ9OwyLOmeNgirtKPsxg0BNGk_1hfDwns8c7pVBkOxI7zXyeywkfkICAkON6lbGjvtaSlqjKRg8zqrXzpZdquDFwxLvmTFf0IUSYK_0RLEbZlHdKmBbRHFncDRFLAw66jORX4Y8wE7CEMcpvlP7G5fa2vTtNTZPsKv3Ym3cOKzb09peMD9ZNpyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی : آقای نبویان اشتباهی نکرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/129469" target="_blank">📅 00:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129468">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
علی زینی‌وند ، سخنگوی وزارت کشور :
به همه کسایی که توی مراسم تشییع و تدفین علی خامنه‌ای شرکت کنن بیمه رایگان تعلق میگیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/129468" target="_blank">📅 00:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129467">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkxHuWo4e5WR52utjGLbCnjzr6TEVTEIn63EwqaMv1ixkRmlaOj0ajICpN0ocI4vKPpkMQ1foj_SWl8GIOWF7kjvMt1d0P_w6SSODaVXcCo1WSFcXTzFlMN5CiTi2Il0z32kxBDje3hzRo8nCLj7hzfNvKC-LjPBLBvTe6_WarQaXqOG1y8FDY_YBLaape5gqVbYGeKb7k6OmyucEbCIZoXn5HZ9fNyjRqL8WEXpcOSo5ywXUOTVKUp6-L9eNlzh0RMIQGhQvPL_sF7sPVRL53cYQ1evMjilytnA6b5KbReTRakC4aDjltgvH7kgcyDV9zkHmVvqIeQWK2M3fwIsrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف بعد ورود به سوئیس:
کودکان مظلوم میناب و تمام شهدای ایران عزیز را هر لحظه ناظر اعمال و رفتار خود می‌دانم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/129467" target="_blank">📅 00:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129466">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0vX5cNWGx9QmpvvmFH9d2pyfKhcoCqPi3yll_M5H3irnk60-DrFxqqPbmLmMJ_f_ccAxqkF2TCU0N8iHhtypcmLLm1a7xB6YHjYkklD7-XTsGloTDe1FyoNZoBnM995YEB5Y8D6l6xT627LecjtKaDnihN0GKJ1XjbQojSGe1TkK-qy8Lz_Y4AvZIUQRV_OWhoosOwhL4XJ3DmPeEijWtMU8azyx2Zs-IuP-9nc9WOowUkAF0DpjOaT9puuUktn9zIshu3YXqtEhy0HRydu53pDqzGR9MXGcrkj49Y3as93FK_CB70YByKOkAaA5Sjn9dOKiWfQ_gelhccp-4WcmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط ساعت رولکس امیر نیوکاسل در مکزیک دزدیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/129466" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129465">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68aa7787ac.mp4?token=I1Ysiz0GT__06qU0RooJxaY10PAVzUQ7BneuOaisAUxgpDxdMIpauwtjvisizN8mA-ZsB-ic-MlW3Z02kCxA4oNXElMjgqBYFOcjU1Nfp151zXdf3GDQnDuT5hSaIRAREmhZ9Xi3kVx0ZdkvYfaxyd-AfzGAzcxEt6U5aPcHnzozLebNcsyiYAa05H06Hei9cbJEKj3sszOEXbe86tJTswDFVQHTNk-doQJ-hzS7AWvR8S8EMQDGgLzws9IRS6QV9g56U31P5wT2ZuEq-adZyED2f1Ncyyiyo5nKpRymSvOlypJ990jbg6NMFZq2qukX3f2pRnsYZQ1ojyp9jsHvSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68aa7787ac.mp4?token=I1Ysiz0GT__06qU0RooJxaY10PAVzUQ7BneuOaisAUxgpDxdMIpauwtjvisizN8mA-ZsB-ic-MlW3Z02kCxA4oNXElMjgqBYFOcjU1Nfp151zXdf3GDQnDuT5hSaIRAREmhZ9Xi3kVx0ZdkvYfaxyd-AfzGAzcxEt6U5aPcHnzozLebNcsyiYAa05H06Hei9cbJEKj3sszOEXbe86tJTswDFVQHTNk-doQJ-hzS7AWvR8S8EMQDGgLzws9IRS6QV9g56U31P5wT2ZuEq-adZyED2f1Ncyyiyo5nKpRymSvOlypJ990jbg6NMFZq2qukX3f2pRnsYZQ1ojyp9jsHvSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس :
«من مشتاقانه منتظر شروع مذاکرات فنی با ایرانی‌ها، پاکستانی‌ها و قطری‌ها هستم...»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/129465" target="_blank">📅 00:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129464">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f204fb86d.mp4?token=hrMl2oX0ITUlB4D8YSNxIvc8FsxQ1Xnu3P4NduZAYp1-45-zW2mxr0kE4EErFEuaqL2KgkAawOfL4j679bgWOwOUK_rb89XT6BPnzzp1tI-1evCGiB0BTiRclZZDA9gFtX3GL-fXs7DA4cHSiMQewCYomo_6YHvzaz02ki932dOyPYf89K4LrXClgByQ8e-4O55eaSR1dkOJhCn8tYExE9GPtYdFYTsH0qm28G6RJDMW5mL0HtxGpnKIzFvmf4tUycAbX46pj5FroKFMxwGr2LedRpXJJ9wxTwX2dmebRfyZKjNyBRUtZHEzo0l1AX5jdjA9GkJxz5hM4UpyBURPXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f204fb86d.mp4?token=hrMl2oX0ITUlB4D8YSNxIvc8FsxQ1Xnu3P4NduZAYp1-45-zW2mxr0kE4EErFEuaqL2KgkAawOfL4j679bgWOwOUK_rb89XT6BPnzzp1tI-1evCGiB0BTiRclZZDA9gFtX3GL-fXs7DA4cHSiMQewCYomo_6YHvzaz02ki932dOyPYf89K4LrXClgByQ8e-4O55eaSR1dkOJhCn8tYExE9GPtYdFYTsH0qm28G6RJDMW5mL0HtxGpnKIzFvmf4tUycAbX46pj5FroKFMxwGr2LedRpXJJ9wxTwX2dmebRfyZKjNyBRUtZHEzo0l1AX5jdjA9GkJxz5hM4UpyBURPXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از راهی شدن جی‌دی ونس به سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/129464" target="_blank">📅 00:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129463">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
همه رفتن سوئیس فقط آقامجتبی مونده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/129463" target="_blank">📅 00:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129462">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaUPve0BlRgkpWmXZJ7ppksQzhbotUc9AyUQMTN4F_tv-c_In9CFJwV1sLmhAXDMklyhuOIlws--Vec6HjLoRR8tISMToaXVRWxYdxxkj6nB11ibgMzvaf5N9sxLYXhksL0cZeTB5xGDxDycr6ntBBHUIhIL5jh2bfkQ0sNC_Bgh6B9HmFaoqJ8QPklH0ABGnA9rvvTaqmuNEXm6G7b9gljtTtD8OI9XXJ_w4O6RdROqoBgLB3Gw1qUuUjaQLCWG3Y6aFIqMu3UKHTjIigWa5sD9rQTz7lKZNCScmAq9hbL6jnyjoGEOK_ZaTQrQfGSJYXxEfocqd2WFaqkDf9s6jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا بعد از اظهارات ضد امنیت ملی توسط نبویان، تنگه وی هم اکنون درحال باز شدن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/129462" target="_blank">📅 00:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129461">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae9096e084.mp4?token=NF5TRfnnrPZdP-Rb3hIjboBsZMtGiTKL3VrlqI0wNbmYGuow0kAKCqLmV6nSIqovgu9g2uua_3XUkk9TCk99jIYMvkPa4aNwW_jld9Hyt7cut9Hc6Nw5i6XpiK3XfI39FVyTz8u7_OQbJAgPBFvwn-7QwWLfNMV3Cbvx35u84weD_1MghJeUOLt9TjoMVw-BsbmrKe7UpOY670PHuNGZf6Uxn-ExTllwxx4FQnP0r_WuvGjHmrbS7V7P2ub58-P9CHg8c9kf9r_5dTjKKIXveyDWUFp7iB-fEiZa2E2avXnLdDNjSLMfp-T0ZQl2stFrUHZOxs7HTBKW2foZdYMGKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae9096e084.mp4?token=NF5TRfnnrPZdP-Rb3hIjboBsZMtGiTKL3VrlqI0wNbmYGuow0kAKCqLmV6nSIqovgu9g2uua_3XUkk9TCk99jIYMvkPa4aNwW_jld9Hyt7cut9Hc6Nw5i6XpiK3XfI39FVyTz8u7_OQbJAgPBFvwn-7QwWLfNMV3Cbvx35u84weD_1MghJeUOLt9TjoMVw-BsbmrKe7UpOY670PHuNGZf6Uxn-ExTllwxx4FQnP0r_WuvGjHmrbS7V7P2ub58-P9CHg8c9kf9r_5dTjKKIXveyDWUFp7iB-fEiZa2E2avXnLdDNjSLMfp-T0ZQl2stFrUHZOxs7HTBKW2foZdYMGKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از ورود تیم مذاکره کننده ایرانی به سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/129461" target="_blank">📅 00:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129460">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ونس هنگام عزیمت به سوئیس: امیدواریم در مسئلهٔ آتش‌بس در لبنان پیشرفت حاصل کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/129460" target="_blank">📅 00:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129459">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
هیئت مذاکره کننده ایران وارد زوریخ سوئیس شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/129459" target="_blank">📅 00:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129458">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری / جی‌دی ونس، معاون رئیس جمهور آمریکا برای پیوستن به مذاکرات بل ایران ، واشنگتن را به مقصد سوئیس ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/129458" target="_blank">📅 00:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129457">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری/ بی‌بی‌سی‌: کیر استارمز نخست وزیر بریتانیا دوشنبه استعفا میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/129457" target="_blank">📅 23:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129456">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
حسین پاک، خبرنگار مستقر در لبنان: ساعاتی قبل عملیات نظامی از سوی اسرائیل متوقف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/129456" target="_blank">📅 23:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129455">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
خبرنگار العربیه: کارشناسانی در سفر ونس به سوئیس او را همراهی می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/129455" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129454">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
محمد مرندی: ایران آماده است تا برای لبنان از توافق چشم‌پوشی کند، زیرا از متحدان خود دست نمی‌کشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/129454" target="_blank">📅 23:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129453">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvsaEZPskSWj94WHWWWvVttYaDw9YWSbT4ohCdxTjwdsf7Rml1PK_qgee4Wh1lJaXPVNyByFgS3r2dDgz2W0k2mv9Ht9WIAj1wMIMrzlEdCtKr181fOEKKRAm5lgsNPzFqUeR7kQGdFW43E2K_ArXG1dMpXBrscgziIHGK3EhlRiGiNFl0R1rcE-Rai3LBQyEkixMFNZ3doIi-nFx1LYiF3lG-ASkAJ3F3nGDBrSrCM-FCGmaoAkCbPCVSM8ATNYlg75D_b_ZDZHsLI26jn-ZaLxGH4uV48LAegOoLtqPli-f7uQr-GKlDVKfFslai6iLcIO0htbdXcB4bguPiXhFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی، عضو تیم مذاکره، خطاب به پست ترامپ : هزنیه‌ای وجود داره، این قطعیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/129453" target="_blank">📅 23:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129452">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ونس: ما به مذاکرات ایران فرصتی خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/129452" target="_blank">📅 23:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129450">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
هواپیمایی حامل هیئت ایرانی به سوئیس رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/129450" target="_blank">📅 23:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129449">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: تصمیم به آتش‌بس در لبنان بعد از فشار شدید آمریکا بر اسرائیل گرفته شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/129449" target="_blank">📅 23:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129448">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
لحظه‌ای که آنتن از نبویان گرفته شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/129448" target="_blank">📅 23:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129447">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
رسانه اسرائیلی آی ۲۴: پشت در‌های بسته در اورشلیم، انتقادات تندی متوجه ترامپ و تیم مذاکره‌کنندهٔ او بر سر رویکردشان به ایران و حزب‌الله شده
🔴
نگرانی در اورشلیم این است که ایران قصد دارد از هر توافقی برای بازسازی اقتصاد و توانایی‌های نظامی خود استفاده کند، در حالی که امتیازی اساسی در برنامهٔ هسته‌ای‌اش ارائه نمی‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/129447" target="_blank">📅 23:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129446">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmDHayKSDlM69REaVyDXlWBsU6U74yXdOkuwMuo0S_jNPzOdQ5xSsdgk5702BjdeTSJ5jBzgZ203g5CEWZzm9BxClw3EqOpU7JPoGQGUQgYlKXIFaNR-XXfLR0YYg4uBKquRbmhtPEAREWUkIQ8SPGPO_ST3k3OepSGsLmH3m_y8ERlpyDXqgGMbpgzv4Dro555VjzDrvljz5idLQReiza7skqPY2ABz9583wpmIGBI03uGp_Uczm0D1jD0SOuT-Hi0SeFq9yxg_d9Zn1m3sGBYdnrLny3c5M4avuJu_L8JlmxZd1_FFuoHGHPkhx4LSW8Pbi_3vkPJI0SREYp6Z8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: در تنگه هرمز در طول ۶۰ روز دوره آتش‌بس، عوارض گمرکی وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز عوارض گمرکی اعمال نخواهد شد، مگر اینکه توسط ایالات متحده آمریکا و برای آنها، در صورتی که معامله به پایان نرسد، به عنوان خدماتی به عنوان فرشته نگهبان برای کشورهای خاورمیانه به منظور جبران هزینه‌های گذشته، حال و آینده اعمال شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/129446" target="_blank">📅 22:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129445">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
کانال ۱۲ عبری: آمریکا در مذاکرات فردا به دنبال دستیابی به توافقی برای بازگشت بازرسان آژانس به ایران است
🔴
در صورت موافقت تهران با بازرسی آژانس از سایت‌های هسته‌ای، آمریکا چند میلیارد دلار از اموال بلوکه‌شده ایران در قطر را آزاد می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/129445" target="_blank">📅 22:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129444">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
الجزیره: شکاف فزاینده بین ایالات متحده و اسرائیل این هفته به اوج خود رسید.
🔴
مقالاتی در نشریات مهم اسرائیلی منتشر شد که ترامپ را متهم می‌کرد که پس از امضای تفاهم‌نامه با ایران، اسرائیل را به ایران واگذار کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/129444" target="_blank">📅 22:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129443">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ‌، درباره نتانیاهو : من کارت‌های ضعیفی درباره نتانیاهو دارم
🔴
من تصمیم می‌گیرم که اون تو انتخابات برنده شه یا نه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/129443" target="_blank">📅 22:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129442">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIi3KE59tjiYM0ckgMYZX_bvigkiMhNcAHmlCyCwVJJ956V6zqNxEC87MsfBxkfts9s6sRBIF9Dxmft1CBhui8V0mqzyi7BSOX2uiZwjNve9Zuleg3-dph3gQyFBg-_QZu1rMny41BeXTgfHKljG5a90f7X06L0YJnDiNPWgD-OmbqnYDxNdyIFCdKZXDjxueYcNJWJCS1TRnuUfzK2k1UwQFBQbPax4xmkhh2hio8ygCRPfKuSR5bwu4GIRbg3piOCVSwNaKQdTzML5_biO-tMzyZ4qDWudE_UsWzDaP8mQrD5FJfSbsQTUFOEMPcXRrxD4shdY9UHWyzoxONWj6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید نبویان بعد از مصاحبه ناقصش توی صداوسیما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/129442" target="_blank">📅 22:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129441">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل به نقل از یک منبع دیپلماتیک: پیام آمریکایی‌ها به ما می‌گوید که در لبنان دست به تشدید نزاع نزنیم تا زمینه برای گفت‌وگوهای سوئیس فراهم شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/129441" target="_blank">📅 22:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129440">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
بیش از ۱۰۰ نماینده خواستار استعفای کیر استارمر شدند
🔴
روزنامه تلگراف از افزایش فشارها بر استارمر، نخست‌وزیر بریتانیا، خبر داده و نوشته است که بیش از ۱۰۰ نماینده حزب کارگر خواستار کناره‌گیری او هستند.
🔴
ستارمر اما هنوز نشانه‌ای از عقب‌نشینی نشان نداده است. او روز جمعه و بلافاصله پس از اعلام نتایج انتخابات میان‌دوره‌ای، در واکنش به سوالات خبرنگاران درباره آینده رهبری خود، با لحنی قاطع اعلام کرد که در صورت بروز رقابت داخلی برای رهبری حزب، «وارد نبرد خواهد شد و از سمت خود کناره‌گیری نخواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/129440" target="_blank">📅 22:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129439">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee12760742.mp4?token=OzlUwMn4Et6NZZwyJkHSrL6e8xjmQSvfCBgerxYsXf5KZGzOjlDQ7qHG7akShRVmrDEVjTSI5LCft8InM9z54UYlWeaI0TR2XCbMMkczxyTK85Gb6uOB5D_DlGh_TQD9MTBVIhNcVPnD6OFCly0s4A0vYptCsvqtQSkMS0Wfiv1dFIQhKw-Fl_J2HGsDTvYsyL9V2ezebcz6yV-f1JIF4DQ-O8xCkdkwKFS4WnCJZGEBelEWRFsEMMI23Su4TQ9uw0nAbpYvkNV8XRDCZEEr5nxTwh8JnU9d8IIld5RYIQUySAEUK3-2AWma33pnguaVXGcCvqWgR1XK9X1lNBNGfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee12760742.mp4?token=OzlUwMn4Et6NZZwyJkHSrL6e8xjmQSvfCBgerxYsXf5KZGzOjlDQ7qHG7akShRVmrDEVjTSI5LCft8InM9z54UYlWeaI0TR2XCbMMkczxyTK85Gb6uOB5D_DlGh_TQD9MTBVIhNcVPnD6OFCly0s4A0vYptCsvqtQSkMS0Wfiv1dFIQhKw-Fl_J2HGsDTvYsyL9V2ezebcz6yV-f1JIF4DQ-O8xCkdkwKFS4WnCJZGEBelEWRFsEMMI23Su4TQ9uw0nAbpYvkNV8XRDCZEEr5nxTwh8JnU9d8IIld5RYIQUySAEUK3-2AWma33pnguaVXGcCvqWgR1XK9X1lNBNGfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زمانی که تیم ملی، تیم‌ِ ملی بود
@AloSport</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/129439" target="_blank">📅 22:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129438">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
المیادین: هیئت آمریکایی پیش از اعلام رسمی ایران وارد سوئیس شده بود/ کوشنر دو روز است در زوریخ منتظر تصمیم تهران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/129438" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129437">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
علی الاصول، هواپیمای حامل هیئت ایرانی تا ۱ساعت دیگه به سوئیس میرسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/129437" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129436">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrsIcdnvTwa20iNSQiwKw-3z7VW7Sh3DE4ecrGqgZ8P6MEScOReamCP1ViP-yBKuDPAvcL14Y7o1m_YxFKYIMXSOB1OgObIkREt6e1zhZLbuvwWKlFSjFwZ9KBL---j_Betm_Efhv7cvD43xWRBx70riX7owKjvp_6_ZnXYe0zliRCOpKK8X2TD0AZ1y3EFNoh96PI4OsoEqctHAyB1WQmFmD0zPoYadOZoZ41wBTOE-LzhARQ75Wcncih_k3qqLJJWQIVDysMIRN1Q7DhWwUIfwwIc5SFA_46toozG7_F0WZv1VCowjyWkz9G29dlir46vYPAumJSXPtV1vd--Q5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ماشین های تک سرنشین وارداتی جدید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/129436" target="_blank">📅 21:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129435">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0BmcxUoUHzrQqN-NbcRzJ6zAowBvV83QU9F0K-eXmpTmedmSijsbFnZo6n7K6ZRrXikh5ZBCJedySxElxY2Mli8j-f2sqKej7p-njqetCv6flfKGFWPUC5ha0Wvj4jg0l2_fErfkQoZU7hbL9FzKWAA11o_2LIV8zHdUPJV-zLe9eU5FogGIvbSLHen1P4dTURjmJdHsogz3_HZqn1nquH6hYRw8acynBzMU7-p_UuFLHIGGIAjnRJ0eSGK1RImpwv-mRLbjP4A_GOlMFKDiDfgNcS6VEyfKpX1oFtxkyDcp3ZMAbWoZrRHUiUfAQoKcXqWFKuDWRTZPLb1dncyNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خانعلی:
رهبری میگفت باید جنگ رو ادامه بدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/129435" target="_blank">📅 21:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129434">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
یک مقام آمریکایی به الجزیره گفت که ارتش اسرائیل به سنتکام اطلاع داده است که به واحدهای خود دستور داده است که به آتش‌بس در لبنان پایبند باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/129434" target="_blank">📅 21:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129433">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvOhnv_DlzfJYgbFIw_nWQcZ9ssDIZJ8c-Bs2HNwO0J04JeA7KUrs6a5Xv1tIlNqoZQvC7zI5Z5WimNKMCw0DbWojECsxMQ14-f_ayex_vJmOxko29DYjJv-uQ-XSwZ08wQNHzCWNHPWPFHqN9bU0ZbbAXBx4vNhbnihpknWxe9K885hprAQnopfMoZMC_pUOi7jwLZn2c3vKs48iXgeao0XhWkNfHOOXg-t5jDWvZu1ZnTg7CFl1LR9MqRvODDWvlVqGvKu4gJ8KeL8zmWvmXoco7w5kawwwcIZfytmWuMIpoJkRLhhoPXnR1ovENVX4TnJvFFFZuEQouAw44rJfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چندین هواپیمای سوخت‌رسان KC-135 نیروی هوایی آمریکا وارد منطقه شدن و یک هواپیمای هشدار زودهنگام E-3 هم در مسیر خلیج فارس قرار داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/129433" target="_blank">📅 21:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129432">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cb7Ed3kzEzoEXeD7PlFa5Zly6KPTGbHP_OecTBDpVmv6S5UsDecr6rBXPyB6If6Xr8vbeHfou1e39KzA5cCzjuK7BRS5lXdjoKlHavH4e9P4IhTAAT8M_USpc9X0IrhkVP9BhicP5uYikyU8DaOZDpjUw2E0sebmqOW_cqqSCqBGF2ryxLKKgDVV7-hHjoWlbDdtdEsFGlE3f2sJ8ZKud-utDxR_Om42e0M_nJhnywgQvVCt8TIZmFhzvF6epnh7rVsjYBnMMc40lQkp2G5-DdOLOsVs-yDTLsvyxhUWa64qsLJ0qib0mYRlNBR-_xmN0ooglKq_auT30BOgKb5Ukg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای هیئت ایرانی از آسمان ترکیه عبور کرد و تا ۲ ساعت دیگر در زوریخ فرود می‌آید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/129432" target="_blank">📅 21:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129431">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWIRpbhXwZ4lbPYag4OPEFa0mJtXXW6bxElVfQbsURmO-f7kAs3nKRSqNBRdHT4VTuPkqnkx98nZUS7_CBWAbUYhanHikuE8IFacEhDKUsQZ1r7_G26hjOKmfEmTOKApb2qhDfFL-Yp0HwFJ5ECzz6LZN2-5A5KDs4HbaTQFZbilumrm_hu7tEp8aUrx3Pe1c6BiVhhI1KYyKKUjSSUZAeq9Az5nD5NaNItw_21arQ6I4AOP56NnZpArerNywiM13bQabcP_avaUMooCpF3wVni-P1hWHnsZqmSAG2TUZ13fjiwiBIxRGH60MSXundd5EuU92LdY33UQ2xrYFWGtng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست وزیر پاکستان و فرمانده ارتش پاکستان هم به سوئیس میرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/129431" target="_blank">📅 21:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129430">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
لحظه‌ای که آنتن از نبویان گرفته شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/129430" target="_blank">📅 21:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129429">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dac5f9d1b.mp4?token=uAH0iJjIAcdu3MgGYYmENvsDSQoaSFHsL-QoMZizl2WKijdNtF4dsFIKIjuB0tAydSA7wflM29RjQw9lqlWGiRnSgduG2tWBhP5m3GaMEm9uo8p1Dfyq23ubqtO_K2w5EsOq-B-4-i_Mf-WCuwsgq1C3eY-Q2Iluy3Ap7_6of9T0WxK49nk77U55AZwlgqiYCU6m_mCaJ3yKa2LH6QGuaGj4nwJa7jOKTLpmDGZfM2Zk64_Xm-4S1nmGmI4Ej4yNXukVC83BCl8TqqNmxZgxi93zi4L8CtnUGnn3uRYXcJbhC2cZFnrIN1axruR4W3CGLqijYcyuul_cgKvtJreGqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dac5f9d1b.mp4?token=uAH0iJjIAcdu3MgGYYmENvsDSQoaSFHsL-QoMZizl2WKijdNtF4dsFIKIjuB0tAydSA7wflM29RjQw9lqlWGiRnSgduG2tWBhP5m3GaMEm9uo8p1Dfyq23ubqtO_K2w5EsOq-B-4-i_Mf-WCuwsgq1C3eY-Q2Iluy3Ap7_6of9T0WxK49nk77U55AZwlgqiYCU6m_mCaJ3yKa2LH6QGuaGj4nwJa7jOKTLpmDGZfM2Zk64_Xm-4S1nmGmI4Ej4yNXukVC83BCl8TqqNmxZgxi93zi4L8CtnUGnn3uRYXcJbhC2cZFnrIN1axruR4W3CGLqijYcyuul_cgKvtJreGqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ای که آنتن از نبویان گرفته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/129429" target="_blank">📅 21:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129428">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428436ebd0.mp4?token=WiLWfr2urro8XdKKjfnlDzLwLYK50txhOZ0xTCFt0nry7NXQe4kAcyIvJVeEYy_xNX5woNAG5tlon4teqXDYNCLiJHvpTUerjjDuU80V9tTo4gcgwY1NwBX5nwtrulysPmJa8B77dbsitLRukwfXMSLeZNZYDJM6QdyfvD0O6xou9X7Ajq_JZ1KOjC7PxWaqbOPfiNAR6VnlM6_Xk_VGxXkU6R3mFTk_flfpiEXSbJLjg1suXokV1C5PGTdVqUKQ_-sX5ouU2Tc5EUsVWK9WbaTVPhpgU95YhxGiDHOjJpRFrHlpuaqti6UfHslwXH-1t5hiNhBlnytTQtWHhiTLoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428436ebd0.mp4?token=WiLWfr2urro8XdKKjfnlDzLwLYK50txhOZ0xTCFt0nry7NXQe4kAcyIvJVeEYy_xNX5woNAG5tlon4teqXDYNCLiJHvpTUerjjDuU80V9tTo4gcgwY1NwBX5nwtrulysPmJa8B77dbsitLRukwfXMSLeZNZYDJM6QdyfvD0O6xou9X7Ajq_JZ1KOjC7PxWaqbOPfiNAR6VnlM6_Xk_VGxXkU6R3mFTk_flfpiEXSbJLjg1suXokV1C5PGTdVqUKQ_-sX5ouU2Tc5EUsVWK9WbaTVPhpgU95YhxGiDHOjJpRFrHlpuaqti6UfHslwXH-1t5hiNhBlnytTQtWHhiTLoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: می‌گویند من به اندازه کافی سخت‌گیر نبودم؛ من بزرگ‌ترین پلشان را ظرف ۳ دقیقه نابود کردم فقط به‌خاطر اینکه دیر در یک جلسه حاضر شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/129428" target="_blank">📅 21:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129427">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhbAdJyHdoPPx46pjrPDVLLEk0gUhL7-e6woqdx8i1zam_-ObIZQ4axw_Xu6C6ejAtuHyJFpWceyCKMbxKZelOH_UOHfCfB8AeS1Ye6BcrTpfxJg5JgewSUFJJp5jQr7f6a-rDi8okPWz8zoqXd6zf-Cc6m5arcxTKqt-the2Z596UYWVgT-1iynKiCdxOwzeGzOu_zJOdgGKGiNztkjsrixhe8Wg_GGVRVo-s8EMzz-_yeE3ihoNLqMOHOiWmmRVXMFsaP_EL7V1u58FKMdFPhg8uZ3JP9ezsqP2vJbWANXhCsnyWBE-sBdprG1fEMNrdXXM4_FTrT5Uw1qz6Zp6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ: سازمان مهاجرت و گمرک (ICE) توسط رسانه‌های جعلی در حدی بی‌سابقه مورد حمله قرار گرفته است. مأموران آن میهن‌پرستان بزرگی هستند که سخت کار می‌کنند و در محیطی بسیار خصمانه وظیفه‌شان را انجام می‌دهند. بخش زیادی از این دشمنی را دموکرات‌ها و رسانه‌های جعلی ایجاد کرده‌اند.
🔴
مدتی است به این فکر می‌کنم که نام ICE را به NICE تغییر دهیم. این کار خبرنگاران و روزنامه‌نگاران فاسد و غیرمیهن‌پرست را کاملاً گیج خواهد کرد!
🔴
تصور کنید مجبور شوند بگویند: "امروز از یک مرکز NICE بازدید کردیم" یا "مأموران NICE یک قاچاقچی خشن مواد مخدر را اخراج کردند." آن‌ها نمی‌توانند تحملش کنند و کاملاً دیوانه می‌شوند!
🔴
فقط کافی است یک حرف N (مخفف National) به ICE (اداره مهاجرت و گمرک) اضافه شود. به نظر من اسم معتبرتری است.
🔴
همه این ایده را دوست دارند، اما تام هومن به من گفته که خود مأموران به اندازه بقیه مردم از آن خوششان نمی‌آید.
🔴
چه کسی موافق است که یک N اضافه کنیم و ICE را به NICE تبدیل کنیم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/129427" target="_blank">📅 20:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129426">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ساعاتی پیش، نبویان نماینده‌ی تندرو‌ مجلس، با حضور در صداوسیما مشغول قرائت بخشی از نامه‌های «به کلی سری» مربوط به آیت الله خامنه شد.
🔴
نبویان با انتخاب بخش‌هایی از نامه و حذف عامدانه‌ی بخش‌های دیگر که شامل چندین نامه و مکاتبه بود، نقل‌قول‌هایی ناقص و تقطیع…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/129426" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129425">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFkYr09-VDj7Tc8V7bpPqZVqHvpB7UtJTcPMVCgkiY69hIa-aeV57CxpVUrjToMbjBp-g_ZIfmGcqdIVNRcvpeuIFdzF7YYZF_TKWUMkCLAeTDTX21AltIsF2ZS-YY1eM1VH8HQ18pl01vN_vImMc0B5un2YsI5HN5-Um7UizDwSzrRTBoDXcOoiSGfW340XTXpTOEQNnF0GxMCKOSuoRRZrjTB3L9clE6CPpFlJgj05N2EwbUr0vVMLE14y6zpCuZdfmh5KscAzbX9M5hlj6CD-8dNxGT1TC7xAjWPUqG6WSUtcqFDbcs6pvZFZl3hVC9BsCuXbCo7hkBnGkgRwLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعاتی پیش، نبویان نماینده‌ی تندرو‌ مجلس، با حضور در صداوسیما مشغول قرائت بخشی از نامه‌های «به کلی سری» مربوط به آیت الله خامنه شد.
🔴
نبویان با انتخاب بخش‌هایی از نامه و حذف عامدانه‌ی بخش‌های دیگر که شامل چندین نامه و مکاتبه بود، نقل‌قول‌هایی ناقص و تقطیع…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/129425" target="_blank">📅 20:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129424">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ساعاتی پیش، نبویان نماینده‌ی تندرو‌ مجلس، با حضور در صداوسیما مشغول قرائت بخشی از نامه‌های «به کلی سری» مربوط به آیت الله خامنه شد.
🔴
نبویان با انتخاب بخش‌هایی از نامه و حذف عامدانه‌ی بخش‌های دیگر که شامل چندین نامه و مکاتبه بود، نقل‌قول‌هایی ناقص و تقطیع شده منسوب به آیت الله خامنه ای را در تلویزیون منعکس کرد.
🔴
اگرچه این برنامه‌ی سازماندهی شده در صدا و سیما یک‌باره از آنتن زنده خارج و «قطع» شد اما رسانه‌های پرتعداد منسوب به این جریان، با ضریب دادن به این اظهارات تقطیع‌شده، به تحریکات علیه تیم مذاکره‌کننده که هم‌اینک عازم ژنو شده‌اند، دامن زدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/129424" target="_blank">📅 20:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129423">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
کانال ۱۵ اسراییل: اسرائیل تلاش کرد مسیر لبنان را از مسیر ایران جدا کند اما شکست خورد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/129423" target="_blank">📅 20:42 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
