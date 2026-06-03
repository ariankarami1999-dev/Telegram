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
<img src="https://cdn4.telesco.pe/file/pUdZ3zBioOzRsxJo2WVcvnVfoAvoJaQGSPR52ImHFzLgNXWK1oWuAYXoErm29hY545LbsLyvhZt8lgWI2pSIUdFnFg9mJjYmMJZ3b_j91hl7jahyPFPrO_uBpU_Ng3-Kl6xy8ZzkFYjX9xl3HBCFBn51CQoTsFuPCkg66zl4q2uLYgItnAoI9XuH-j94PmwMenia1vYLWKVHw8dkHg9Oo82YsYzXnO1Pfqg1rj8u4SPADi3k4jOWF52WXaJ2TayF0N8vArtexMUrqrvwIZYM6JiRdA_NAinozhJ5grOyDixlrmxLEOyUcF4ghBAcHPQJV8_fj7TyFhIBTv4iwNbSOw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 220K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 05:34:28</div>
<hr>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚀
فروش ویژه کانفیگ پرسرعت
🚀
🔥
هر گیگ فقط و فقط 8 هزار تومان
💙
🌎
آیپی ثابت
⚡️
پینگ زیر 150
👀
🔗
همراه با لینک ساب
👑
💎
بدون ضریب و کیفیت عالی
❤️‍🔥
📶
مناسب گیم، دانلود و استفاده روزانه
🟢
✅
سرعت بالا
✅
تحویل سریع و آنی
☑️
تست رایگان
🎁
📱
با ورود به ربات…</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65247">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA.R.I.A</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HViQfnAbGpVLI5Gx23cwMXvIIOhEECu6JjxMCUiUeUvbgYGDlO1QkIqwrw9T15vcMAdUL5MK5B4Iw4FGrd_dek9HKNBBdPuf4jzk8ro-w9fDD9nDnDNlEnU258koVUeu7kJ_2Wz9d6NuZ1FsUNr7yRURIj-OqlXI2bxLMcie9aB0oQy03Au_JURNCmaflu_iKNS31AULqVSGdRTjpvtODM7S68E8PRG281jx9g0CJLyeq69fDS1zH1ZKi5gMAw_Z28CmWWmLKEXeknH4Sh8vFL8HnEHb3dsSVqSuN6rBIxgFycd3pWjuzzqBcsP2CU4TDTneiW7_KiKwiykdxr4vfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
فروش ویژه کانفیگ پرسرعت
🚀
🔥
هر گیگ فقط و فقط 8 هزار تومان
💙
🌎
آیپی ثابت
⚡️
پینگ زیر 150
👀
🔗
همراه با لینک ساب
👑
💎
بدون ضریب و کیفیت عالی
❤️‍🔥
📶
مناسب گیم، دانلود و استفاده روزانه
🟢
✅
سرعت بالا
✅
تحویل سریع و آنی
☑️
تست رایگان
🎁
📱
با ورود به ربات ونگارد 20 هزار تومان اعتبار هدیه دریافت کنید
🤖
ثبت سفارش از طریق ربات :
🤖
@Vanguarrdvpn_bot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/65247" target="_blank">📅 01:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ku9d9iKsvD22FpmLk2jFwj0_ecmg1Ry5uEO8JlgsFmo3Jl2YMV5J1YF9HjtblXyJTKo80C7Mnold6XoVovYoF02OTIHiPSlDbnBrMoo8YwyomO7MxfzFS7mQ8TBrJAZj63dYIeafSi8CzV5t6GZ_ggzZUsq4aZTk4Jv2l-JL_2zw_4BgwH8zgJB3cfwxEjD0SoBxVwrPDI41badaJAny76gRqnfVuyaudR-X93TlOll7txxX0uJLBsDQ92Zi48eoRR7TB_1rRa4gd2p342LCZ3r7nJmBIj4kojgI9KHub5_6QNyWKJVawvX5PGE0Kp44HWcUWS2R9ICywfFfud5rNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLt6jmARb6ZOmmMrIeLj9LeW-3bzkYr9DQcwOwt2fCDMYWWDDpl7rSU2UWiRdAWMlQagZO9wbN_n9imsNPBslfi5jYJq0KNJWxAe_n85OPBgon_PRiPJwgQXbrAFM5hK9dh9pXr0EK7H7R7I7rFNhb4QA9H5mdNbNGcnJK3csJ_XnN4M49FPO_N24OsdvwO38iztM3qUsW598bPCYij230boaF4-Fkr5eQr_iFEdVN0QpSTyPEMWURGlS5oJIra8k9cS2jl2T6qny0SKZkGXy56MOAXdr9bYoS0aOT4mUOo0UP5dMvERmOVS6HwuD0fpf8sBPUPXnFlz5aIGUSO3GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8M3OwsPa6Pk0mbONLPOXfacatB-sABeZe0duoy6NyptYbZpDpfB00P7UAl66BklKOv6IWouW878iSCyJoL1aqWRGESJBnQbYEC7zuO8XF0PHDHeLTAR7C3Tf9jxaTPn1lM7JEr9-pOBrIg8ERw0KOfshmIfDjX7ILnbEHc8J97ewfWqj78jkGyDIHBl7etlJcqhTR_1Apj9On_hH3u7JScZm_zInIgnEmKvFKD3uS1-gPeV5gxVn3qjz5cP-4jLd-EPOUViqiAxNiK7YymjTS7S-VC9gC5jD67R3SWghLc4rvI9WbEshC2BCansqpKnF6x7PdUDG4NvASrDijnqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Etu05lbtOvyBbiUa8o5fbQR7tmHbcxHgsA26GYvtaahKgW4-TnZwHfvLR5F-z26I6VkJ6dPeMIMgsQvbfVflzMaq2vnwF8Sou7nw2b57qKiJIYE9iY_IbvJemI0CY5Eh5oVHlRatxNOdyz-SdUxf5ISvSXfm_NYG7JPveZsCwZRQlt8lfCRhWva5Y0VCdHR8N3uayZlSkqnSCRnhmyJN20gRTzvy7PzeF80mRDZ5gnX01rpSUx9WlaTNC3t10AVsVz-HB9cF_wI1w_N3Qkud3PXBm0griCI8MVeDr0JQzOMkMebvQVUF3V31FKnCnkQjc1u-ZJoJYFWYT9OLurKwvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/news_hut/65239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax3l_9pjVyrvlUn1BQAFlYod7_6PkMBscGDNQsgvupI30KklaQKN4g5i2PM6ihZpwBZVZcSLCPs5OFL_cIm_iOTRWiDeFZHwYnLtcC-DrCfmzM729l9wrN7MwetzplqmHwVVlayP5R2_tUElQMmPqn6oam1fGi8BKkPeB2UJPlfwGe_BwszpQYleV-nzXVeIodiPFrZvPF_3w_0m9KVZYvrZG5znwTMokyA6hkY2UQLMM5BIO_4j0Hes0sEXjDFkvzt0KnWLyfZJN0GXWPUXSlNHq-vWF7K7HCVIWx2Ggd6wiSrjtv-WxAt1KdX5Afl2l_rCF8AY9_gK6KSes-sgXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMscHHxFCL_aknogGU6wZWj2I7hoc_hGzYx267vywa0REDajKFUI36B4GAxoeIQsReEQ1LDc8PBttBYvBESo9_UnXoKB7uWeXQSneX88EF_IyDDWmI2THIQBZK3By7i24eKRSir_Lp65j3RhSsxSN2ymLq9YmuchuzxboZlq0jNI69TsLSGm4uNCCc6kaFSK4Gf1mIb3HLTyQbb_X_4mRqtBuvoNkenN6fPhA4xW6OHGA1H6FjdQPn3TUaK08qGyDwWTUGPaoy1AUTesAfA18A3QLluPsSsaOmYQqjZAZiwcMmx-jn7rrwSztIl5YnsDMrLIfxwob6cIOx3TzSSFcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=dWihSjMn3UO9aIv-Z2ipIT4drV0PYV7nML9eyXlrtPlwN-MZKWEOWIXxJP0OtMsgRS2XDSFXJpili6m3-dsvfz-iFyjUDDIPdwj-iJsT4AaBpDJY7FYi2o_EddmErQluXj8laOEsvePkLUpRN5fmDeJoIcGIrB76lypraT9NlU8ezdAx227nhBMaPKQlToxcRpkcLOSqk_v_INEFfouDWUn5L27_4SvKRfUVNk4UppPHfoonXHEclm2uFQ_SA1UBEmuBfyQNTCmINo365FpGgOUIew22fWwnKAAtxi8VWnQ8fMlfZM72C6xhlRPePOS712yic0PO9PlE5vk8sR7LDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=dWihSjMn3UO9aIv-Z2ipIT4drV0PYV7nML9eyXlrtPlwN-MZKWEOWIXxJP0OtMsgRS2XDSFXJpili6m3-dsvfz-iFyjUDDIPdwj-iJsT4AaBpDJY7FYi2o_EddmErQluXj8laOEsvePkLUpRN5fmDeJoIcGIrB76lypraT9NlU8ezdAx227nhBMaPKQlToxcRpkcLOSqk_v_INEFfouDWUn5L27_4SvKRfUVNk4UppPHfoonXHEclm2uFQ_SA1UBEmuBfyQNTCmINo365FpGgOUIew22fWwnKAAtxi8VWnQ8fMlfZM72C6xhlRPePOS712yic0PO9PlE5vk8sR7LDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=i_oVP4NXlYOsiXFj8w-qy54D1bHX7pCmmZc2jXP7OlrCUUqvzRXYkAa6lIiERnhYYI3kd1KVEWciCnTsmri12O2uiFz7sa4fuNLYzbgTYyzVgP5WhMUc_hOZvV4XwbsHV2rxr5AmFSBH-H9oW-u32SaMrJvLvm1rQUbLtQwYSiPChg3vj05YuSjBsNLEztOxcJ9ikbKCcFzui0fZfyY3PbsqC7kzKXnwv36vPWMCZdOyGaU2fe9N0iDD9jqNk4DwHjOjE72UwERreZ_ZoVn9MhdyBcWxpLLnMM6ri1kogZ1VSIMCZ436PaATQotPQwkpcK9RryZfouKRc5vb7HWrFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=i_oVP4NXlYOsiXFj8w-qy54D1bHX7pCmmZc2jXP7OlrCUUqvzRXYkAa6lIiERnhYYI3kd1KVEWciCnTsmri12O2uiFz7sa4fuNLYzbgTYyzVgP5WhMUc_hOZvV4XwbsHV2rxr5AmFSBH-H9oW-u32SaMrJvLvm1rQUbLtQwYSiPChg3vj05YuSjBsNLEztOxcJ9ikbKCcFzui0fZfyY3PbsqC7kzKXnwv36vPWMCZdOyGaU2fe9N0iDD9jqNk4DwHjOjE72UwERreZ_ZoVn9MhdyBcWxpLLnMM6ri1kogZ1VSIMCZ436PaATQotPQwkpcK9RryZfouKRc5vb7HWrFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔝
دیوید بارنیا رئیس موساد:
تغییر رژیم در ایران یک هدف ممکن و قابل دستیابی است. این یک وظیفه قابل انجام است اما نیازمند تعهد، صبر و فداکاری برای هدف خواهد بود. این وظیفه باید در رأس اولویت‌های ما باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=eIg2RWddJ4l1MogXlXl6cEMuORtsGobvXRcopA38uQZTjNcrrZL3okCqVrUA-iUVuAQeWWMTd2n04T4bKLEHwRyIN1YPsb22Q85kLGvdK9OxJGNXClFiS5h-btOKw3yxmdOqBjsMCfITP-yWO6WGvzK_cGG6mkXO-gUXqk_b9ArSoa-deM16zYCgK5qUOCxfir4OnwRZtOgagI-Md19gH3MEK43BAh85IBslDVTV2K7mWvzWIpT3BltfOrAiWzJc17LiNNS7o6dItYMIIO26lHoAORmrYxM2K4rfyrBAaETm-8nF0KnUqxCfYEXCRhQWIRJlN10OwvfGhHDejusGhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=eIg2RWddJ4l1MogXlXl6cEMuORtsGobvXRcopA38uQZTjNcrrZL3okCqVrUA-iUVuAQeWWMTd2n04T4bKLEHwRyIN1YPsb22Q85kLGvdK9OxJGNXClFiS5h-btOKw3yxmdOqBjsMCfITP-yWO6WGvzK_cGG6mkXO-gUXqk_b9ArSoa-deM16zYCgK5qUOCxfir4OnwRZtOgagI-Md19gH3MEK43BAh85IBslDVTV2K7mWvzWIpT3BltfOrAiWzJc17LiNNS7o6dItYMIIO26lHoAORmrYxM2K4rfyrBAaETm-8nF0KnUqxCfYEXCRhQWIRJlN10OwvfGhHDejusGhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVZvvDHgZ5Jwg9yTDpv2Oy17aG_xBP9Gm1ZJWf39Xv-lnrO6BK3pkHg_Fd_XMwSBlC8ow2N0PGZ8Gx3FhUGvjUHOjabZA_pRAg46Js06RQBZqj3MSiRmfsIzPBxA5Uqqg_7wa9gJZgq2cXj_8vjWErLVfsilbakvE3yrfcr70CI9pFYDrA-lcR8mEEJKs199nD6g4_lSzU8W4jI7vr5-QClqjl7zORTrh0DturiTvfS5JQgkk8MZz-ZvYDkJh2d4hdGwHKD0SwKSVUahpibDjIZ9lolb62sXcgA4VrGToiqjV-x0mj6x--WcBQdNnHqcKs1vohArfccDf-0Y-oA-yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=q9m_XUUh0k9T0-3X5RiJh6fbIHAmuF2xekVV38alOFOfE6yp7Hux8NyaGb0Q80qgSWViX1II80v0-s7_i4BE-k3anbxOg16SJVvgZYknp3R681aOQdEITQAgcq8nL_TqgPjeTYD1c4srB0VDIQ6IiY5MCDvTO8rd99tQqQRMgDRCeaziqZHGo3xsaz1VcJJvJWYPAG0D8xdhxkQ-yv404XuJKRadB7RCX6ksmooDxGKyfRNUWF9QscUxGjhzQaPQ-yPlz4NJPJa_Sis6BFxSPtHf284VUZG0KSbHnH6I3rPzh3cC1lxspvWrgL-19atEdVSYcegc4PcPjvOxcxOr-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=q9m_XUUh0k9T0-3X5RiJh6fbIHAmuF2xekVV38alOFOfE6yp7Hux8NyaGb0Q80qgSWViX1II80v0-s7_i4BE-k3anbxOg16SJVvgZYknp3R681aOQdEITQAgcq8nL_TqgPjeTYD1c4srB0VDIQ6IiY5MCDvTO8rd99tQqQRMgDRCeaziqZHGo3xsaz1VcJJvJWYPAG0D8xdhxkQ-yv404XuJKRadB7RCX6ksmooDxGKyfRNUWF9QscUxGjhzQaPQ-yPlz4NJPJa_Sis6BFxSPtHf284VUZG0KSbHnH6I3rPzh3cC1lxspvWrgL-19atEdVSYcegc4PcPjvOxcxOr-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=nlT1eNFgJEGdsfYKNm0trqdWNKnvLWmdQf1FkMPUWuiEfmfAyVSGkYDGZmaHGBU3_ntoPzuZnrs75I3lSlDkAJd2ke1oJWgLlRmCqTGBogX5AOSFSf_FTJ1oh2l-bh7wh0AWiWknWNalLJI_M380MwkfdE9yd6mnHbzGuKsTZTmu72gLCeW1l2wYSdYhyNooO9c4SxDsAg5gIHlTBmlhCzekqx8CAZ9cCcxHIZvDPXK5JdJh4EJXE1nyORaQMIFHD02xqeMbelkZnlFClTK37xrl4hOBAqAPhI_WcGQIgbITdvUVzW6sA6l-vkNEuUrcQdAYoQXvguvNoK42_3L1iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=nlT1eNFgJEGdsfYKNm0trqdWNKnvLWmdQf1FkMPUWuiEfmfAyVSGkYDGZmaHGBU3_ntoPzuZnrs75I3lSlDkAJd2ke1oJWgLlRmCqTGBogX5AOSFSf_FTJ1oh2l-bh7wh0AWiWknWNalLJI_M380MwkfdE9yd6mnHbzGuKsTZTmu72gLCeW1l2wYSdYhyNooO9c4SxDsAg5gIHlTBmlhCzekqx8CAZ9cCcxHIZvDPXK5JdJh4EJXE1nyORaQMIFHD02xqeMbelkZnlFClTK37xrl4hOBAqAPhI_WcGQIgbITdvUVzW6sA6l-vkNEuUrcQdAYoQXvguvNoK42_3L1iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=JeP6l6Y9OsOtAHJYILKjIEWlshZ9z25QYRxxvobkhkE9MAWqOvrncol8U_S0J3Yp9fC-erSt6Q2os03yYmnNK_szGhwx9FxGB3hYoUJ1sdh0FFfQ2BwqPhRfKuaJe4jz4ZCbIFv4XMonk4ByZTA1OX8Dx2VjEmz33YTCcD_-wXdm4sAPeizbugA_5a1bDDPGYiVGK6mn3QpxODbu4D36bmg24P2NzeIIegI86HCcY1ciShWRI3J0jNczV5INUCLGlo4vMtpZWElfy6RKxgCKg_glryi3oV9JArYuD1L9IhziPdQZPZXwPKg3j8THA-ZDRsIEEJqs3i25x6cDy0-bTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=JeP6l6Y9OsOtAHJYILKjIEWlshZ9z25QYRxxvobkhkE9MAWqOvrncol8U_S0J3Yp9fC-erSt6Q2os03yYmnNK_szGhwx9FxGB3hYoUJ1sdh0FFfQ2BwqPhRfKuaJe4jz4ZCbIFv4XMonk4ByZTA1OX8Dx2VjEmz33YTCcD_-wXdm4sAPeizbugA_5a1bDDPGYiVGK6mn3QpxODbu4D36bmg24P2NzeIIegI86HCcY1ciShWRI3J0jNczV5INUCLGlo4vMtpZWElfy6RKxgCKg_glryi3oV9JArYuD1L9IhziPdQZPZXwPKg3j8THA-ZDRsIEEJqs3i25x6cDy0-bTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=vIWnVf3bos8OsPExTjdMH1qkBedu1EpT8wYgnkE7dc9BAMCPzwnF42w9gALIbAQxiwcqeB2BmcYU2NxwNZbwe99kHli9EXC1Op2LqUyGRCGFd-uo6lQbKhOjdfgZ6Z4p1BTunq29p5JR3K3F75wCznCQ-a746XYh0108hQ9SXaJm7UcZDbtpY0CDpy-9waYgzxHAKcC9G0LxPpQu6S-D8-X93qa_yfWecJonuXc3DQRfv8iSU3im-yMmlyetGomaasP2tVxWC9lHz_NBVrF0iMl_ZtYAkt8l_p7cEqVMb2n0JTUnR-AiqI5dmf4WWwrSnVJUhmaL3s0A1lBwlg257A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=vIWnVf3bos8OsPExTjdMH1qkBedu1EpT8wYgnkE7dc9BAMCPzwnF42w9gALIbAQxiwcqeB2BmcYU2NxwNZbwe99kHli9EXC1Op2LqUyGRCGFd-uo6lQbKhOjdfgZ6Z4p1BTunq29p5JR3K3F75wCznCQ-a746XYh0108hQ9SXaJm7UcZDbtpY0CDpy-9waYgzxHAKcC9G0LxPpQu6S-D8-X93qa_yfWecJonuXc3DQRfv8iSU3im-yMmlyetGomaasP2tVxWC9lHz_NBVrF0iMl_ZtYAkt8l_p7cEqVMb2n0JTUnR-AiqI5dmf4WWwrSnVJUhmaL3s0A1lBwlg257A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zbl4PsbquC4mz0muOoRR3_DoLGEa_FvWKedTndHj8LcthbwdHf7SG_BEevZf0Kx1WUgeeUsmtHEBtBcbr5Dy8uWSKwhgnvMpw3zzj3bL8m5DUlPWePJCYLKRxeKyqwYqNA3pCo-83G45BJJf3Bt-uBhMKAtWbzpCsgbSdb-SlP5BhrbmOa6RcN_ByJiXVS7QiE7Y5U6OjLJOXwvu_c3bviF8871niK8sp_DHmLfmy1nv5g7P3yM8oDDUkuEcXGb2icsHxesKg9_-SvOCYCnGd9PKnktvOxXMmwIBuYnNj4zs_396Wini_Mgz37fA7m5kJN4qS58wuOnpWz8A6Yp9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZFpjN70IYsebvtxBxl1mdqP5GKgjE5p5IDIYuvOu4y8iZzJu7wueogz52H5Ijb4OH07BecxZCcaYH0KUGuNXl575Rr57ytV4NSdMaLe370iXT_IhGQ5i15_1QbWQhmrugBAwZng8zr3NVk_DhiIOyJBi56qUkFWPKi1IQGkwBh3S186BsL8gLssm6eDRvOMmInsYTifQPUA0DyNQgqDDaTiGTb2ZdIrv5UnvCuFb8QatH79TK_bzlsqYnT4JKGSjtQew3j61aTcmgac1FCRs1liZuaCJAxzJx2nYunt9w6Du8Ib6Sei43P39qkdaJnPeCDJsdCOpg5Lupf4G8spDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDD1ovtvFSUowgsUgJvBa6rhB3S-xq1kS17DdC1rhFt28ILdWnuY3tJw7WRPkpDnbuN4udE_BaLr3M6EWGciqVuzp1mH7ZYGhShJnaJ5cRFMEMsOAQlxgcIX96Yh2onc0nweG-6SCr_Bmo79pH_jhKxS9WQbTI01b7PIDCEzTotcHkLXC-wjsuzR6uZlcoQhyj8A9ptN6g2nthHNzT-yd_hO31LyZiBvuUXpkW7IoFxhRNajOmeqdktrR0mR6ou7kIAp_tYY6mkS__QOM_mp1Ilk2nSH584TjnhBrtzw7HlHdh8AS0uMjX7jMyMDO1n9QzGyBot8TpYZ_ybqr1DOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E7FUuT7QIn0QajiXroweGSZ210iFboSMGiHtuV5255NgL8DlJo5AULzXvsUq0dAOH8oKWMJ0pYloQB6KyhLXfkyFRE5dvffJf3d_JDxVDGbPUE30BLL-AIl54GIOym1oqUCWxBtcRcX2tYa1GnuosqA5alSmqz-yKGTyz7XUhVoahYZq3LnVQ_8DqGt5NgZPp4BOX7O-sQSe9yPgr2VE9DMisdVJl4HrBKxsGjTRz9KA-LsJGVjxcL1ZOru_A9t__oQKQ92VRHklBDnM3x6WMnWGi-2zZ9TdtXcRzvvqGckv8VpiO7Ae-Z6Cb3TWT2rCEXcRMFQK9Phy7LbysUTK5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rgz2tQTJ8Uuwp7hZl2Tz50EpWa55lLO_SfwYvPR9LgyYksdeCR3U4tjomJf5ENrNXS4BzwTqBKq7L92QlYD7323QifbZi_pJS2s0bYis7Nh3ROLUpNTbHMV_aEMFjSeaZaVffyseC7zmJECXb8D23qkY7_cqR_SfwQCNxhmECqo9qVCZbCW1hYXhR491xRuxoo3hmfFio714Yj0N0IeRQCuMHR26_9DiXraedND0tj8CNJZZENiwGfsb0lMqTz4LFNoo8wnXUyQk8IZNhXE6GMFy6S733nbVUspmRRI8u8_8DgfVBPTOydksJe7UMHu2ryygYRcbHEQVXIrO5ZY4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V65hvx2l_fQr-gpCbfeeq2VCKvldSkDOmVSkptvpNZLXGsN7YK4FVhs6MKWzB2VVOEsfmosE2lWIFAI9fQcBujDpp2mlHjURrKpkEieAiKHvg73k6fo2kSuAPD6FVoMEKRULEs3JbzTzQZYoa5Gu7B4ukoaOX8pCnj9SC7mLTTqm87tIHxzaUoJdsHmu7kugJ-oyYWysSNATcAp7jS_JfaDPSMb34aYbdWZnSwB5ixYeuSKii2KU5_r0BY_Zb-2yGyWE9cYsLZXjnOu-YIaG3nQZ2PB5zbe6HeTEF74MZ7PUlCyhwBUZEKEtrwLiWCrixyKuNcG814fqBKqvnnusdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJ_dhRbkrtypYPRcRk5fDorRUzzMBUnsJAmnbfdjD1UkV8vTdHts7RPDrrFqqatzXzXnSdx40hAHsLw2eyDHV7mL-GMjs1vjGhCipeNO6QGvm8QSF-9j5DNEURn6E36oDdi8WG3BjyXoIvhgcpnf-pufsUqJOAFfsllkJ1WnqMXYpXHt2atGNhxdLaJQvg7EZzwL63Y2F89C8wsQqcNlV2jE1_B7B3MDXJup_SClgVaRwfRJJ3t7iPHCCHwx8jaaIsfJMUAmb5AidQPxAua-NiwYdvpms1crBxUjurM6e1Q4pyeIQa1FcebGH8eDeIAeAWJkEHkQe3mPBgWwjEFTPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65208" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kjp7NtJo7QAlhcpxQt9Cgw1tiqsmTlQO1EdphbQwknEOZHK8APeTQKJVP6xPL1Ael5x5u6szLGDIBUW4NTNj5of1Da_eAs8qKLhS3OT3RDQ7OtHYJ3jZuunAnMqROdEysuSBN6_dncg5r8d5kd89gd0tRE509Y6f5ZVM7aA4aWXESY0Q-wkB6nW4e7laqzZhCfwHb8KstPhJEo_ua6aQiCzggTjdK7RlT9rIUpwoPKXWiIrC1unwfFNpCsXrQnhe0ven3QHF5Yks8niYWqmWid24sSkQl78TKOcapNRSXWXdWCr94xTd6RBDcDw42EPQTBUGIuqEqn1MD7kQyeUI9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIde6lNrIKK9u_kCweyHQdKnpSAT79b5XBF2g55OzkomWt1OFrw4y-2lL91395TOSe-wVI0dfwitL7zXsDA_wJ390c9oDu5tEnbZb67UFxzOkWwJeg2Totp1OwuHqECDxFoEOxFdZa-jO1jBjzTb0GX29YZgQoWC82dLJL1rH2Gp9ieWbcPoOhwvKAon78XxvYOMbWw9hTJHGtazyEHmEfehz9rc2M5tVVEQrSSZcNq6ZcqFfLwnGJ0SmgeWZt4vhk6qtn2KD8cKCkT0jzut_p7Q_vgYXzMGwGc3v2QDlVRfwTfUC4geSz4k6t4MWg6XblRMwNnJUVcxomE0_XPXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=lsGOxVnigDdoonBWhc6LTPvrBYs-betpCKkbet407KYccgKQJWmwFbkG7jtksVVM8Ahm3Q71tl0yVWXlFlZFlfE7WiFGlHj9S6QYqCc4G6pgzYkpQHfUR_K6LQQMgKmmJ-tq_2JFXOzOz5mkJsC-diJXUtV1Ko6KvomE3Tzd_Ax_aNDoB4tNtG62vCU8xR2E1pyBvdWzRzMCUx-iGSWV0R4GcSIUD6uyvhTpOKlyEdIf70ySGmYrlxBdYL9k3qrdMVpvQl9AorrZI-Qr4-bpz19nS51pvt7rHexO3uoU3hCLh-jFU09RQhzcujctFug73Q2Ova5DoPcrU9qp1lyPCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=lsGOxVnigDdoonBWhc6LTPvrBYs-betpCKkbet407KYccgKQJWmwFbkG7jtksVVM8Ahm3Q71tl0yVWXlFlZFlfE7WiFGlHj9S6QYqCc4G6pgzYkpQHfUR_K6LQQMgKmmJ-tq_2JFXOzOz5mkJsC-diJXUtV1Ko6KvomE3Tzd_Ax_aNDoB4tNtG62vCU8xR2E1pyBvdWzRzMCUx-iGSWV0R4GcSIUD6uyvhTpOKlyEdIf70ySGmYrlxBdYL9k3qrdMVpvQl9AorrZI-Qr4-bpz19nS51pvt7rHexO3uoU3hCLh-jFU09RQhzcujctFug73Q2Ova5DoPcrU9qp1lyPCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qnh_x6ZD5R6Yk8BiqJSffFXBQp6c178D8WiLOsHGpoUgh2RJx7K7ZMC_VW5Eq0LwI6Lm_nJudYmmh1kRFMLD3o3bRvGPRCKolZjsWDG0d9ayME_I6SFHgjkVhC_ogeUP_KFOU5y4x8wf7x4QU8qu9nUjqgToWsOzA65rCdZ3LikPXDwbGMi_Owm9gASe3y7lmTLnoW45f9ePFzoq74saAXqdslwMbwViFaHJU94JTsfG7JNuCOTnjjreHHzxsjVPME36BK3GFnJNAAv_3Pq1rbyDLSi6fDHK2zd0smiNu6xiqSHSp1hSRZIjuyXacewiG3lM_0KXb0KOilDByIYh6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH8gqv6rpUb6hvzC6fDJKorWobc_m-qQcOA5OW8H3uc2_ZwXs92q0S84k2lrjs0dnrIWVpRKLjlGHtGERv41t8IMctmF7YtcPG-Hy77KoqE53PuXwAAYqLi7shYJx4vR_98w86cj83TNSROtBah4WTDHEdPjhwGmD5GYb-jDzjlThnQiBz9P6PMtq0pcRKxjLiqTpojWbt5dELOZX48YspQKROTgbA8WJighNydJ4_0w_BWuCAmN0oGTQ6VnuGKZ1E7-k3nIAzAN4IJBfy-7CnUWRp5dKUCcczV03d2KtJKc5rNTggQ_kzgeGEiiqf2B2nP_8gjuKeLui1kBp8DHQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQ0IdOgCtnHSdVEJ9nzRtzBD_OM8eyG5ehDmLq-KNcnUuQd4bBv4TlpvCUis_xZFsNKt7bOytsHu1w6uSX8keDUx0P-mj-Bf81PdfrqTdHYpEnI4TwD9xQIjqC9ggo8sfPjhEIoW8WO3u5RAuPWyUd4aojsuL_CyRHwmE02l8hEFMboZRGddPJNV_qNvoEPSkI9jaRa1Fjgx6uT4PvQzuBdy-K4NnABWkC8BkBJKZn1DZByJnZjfoVhOlLou7RV2jjDZZ_PnlMwwutxHEhGtMKYB1XQrTY8LFYQuGDXCVprvRDp3Hp2UPw-o36xhQRkuWr1Fnbg-DLm3dtL72h_AtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DIjCc1IracwYhJ__ob6bPvZgCCgkuygWogRcMPFiXq_S25jvK_ShHK0L3Mgt_ib7p-bDZPwxqGHIRNoYtlpJdJB1mw0bg_wrejfGhavEmOg4jO7wUwktNoGym-GaJ67AN0rpEZUz12nR55qZwhd8g3S8vhIzstrPS_OjzyExFCVLgctXO5sb15lGIX7JHZxkNfk8T8d2Rh2Ml7BwOMSW2MIgsh9KHro9LHFyHKk770rl6kYxmidQ1hLbJhuud-Z8OB9aEroaVCtF_lIWKATvl8T4lbixbdAa6UHQOjYYDFagk4TyqSf6VoU9K50oA7Koh-7nBZXINOSZ12f9ckev2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=SR26_ZyysScePMKQZTKwige8GhL-U4Lebpv-kyh13-NHAscupvEVLiKt7C07Qdfbse6BJpO1Vwce8CI8NoZ_v62IcmKnYRxerVoVaNYEiy3gla4N6p5N4B2d1WfGquF_OR-zj1St8HJQxQuFN-fKN-cAktc1UUyu21jitOFxMfeDF7tLwJLKxofoRqGI9iJ1hJE9tozo1_in3Gzsh6sPOsaWmxOkMZ8pXw_xZHLLB6ZQDVBJWyTzSpX3-1mStg40DW15a2s8ZWsMDO3vcHoHZnVUSagFJBCt-l4ZhLADoXff9u8Pq7k7IbPIdWWAesCJFImfXrJEIl1yDG2yIg25LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=SR26_ZyysScePMKQZTKwige8GhL-U4Lebpv-kyh13-NHAscupvEVLiKt7C07Qdfbse6BJpO1Vwce8CI8NoZ_v62IcmKnYRxerVoVaNYEiy3gla4N6p5N4B2d1WfGquF_OR-zj1St8HJQxQuFN-fKN-cAktc1UUyu21jitOFxMfeDF7tLwJLKxofoRqGI9iJ1hJE9tozo1_in3Gzsh6sPOsaWmxOkMZ8pXw_xZHLLB6ZQDVBJWyTzSpX3-1mStg40DW15a2s8ZWsMDO3vcHoHZnVUSagFJBCt-l4ZhLADoXff9u8Pq7k7IbPIdWWAesCJFImfXrJEIl1yDG2yIg25LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9tlKlY4EgdIBd39w9tPdqSjrPLm4SAlLZs7fQhJN_ZdVqCgfIeIkpixRGIrLPYtgoGRpMZrPHgUaLP_mcQOtm9BBKiF083OAnFtMrA5OlhEN7R2z9AMu9Voyuh9Iv0i8-p4fni960de0RLoRVUMVBQ-haDU4NtjztN7dgJmuOAtwjlqP0saIi3ZMuyu1vAi89JewaGfxZA7Z7sLm-LDZg0viJNH6KDhnbFC5zHdz92UXvr4yuvAPMEmZX6S_Cy-nuilR-N_61eYriLW9oqUldkkoCRxTsVCCN-a9oMTk9UhwwJMiyn4RZ3_bvMfjURvg-p0d4tI5JyiRIzVb0998w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=N9lcqgb7H6L_UjHGtrH27pGQ2GtSulI76IR3r-ZUE61LaxaEjquZnLB_772Wyxve2PmdG3uvxV7oMJRadsm82hrlSU6iJKNTbklGx4_M_aOvdZajEP-tLI1lHrf1XIkq8wf_L7WarCAiKRRYEIArcnyZZ0hL-zkxpsLWPgHyT-RhZt6VBvwazErY8XZbuo0aMbmqYdYvZ5JYYg0kjsZsML9w9wV5PwfG1ddRGCOri1qhVJTXBC49eO3YSi0S2SuhxOqTcQxvC0AlaqMZaSYG0FOZ4acv8B5OKudDBhIwEx1DS78SufsPkLfWHdey9Jt2qQOhivV2CCzCi_qNiSMV8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=N9lcqgb7H6L_UjHGtrH27pGQ2GtSulI76IR3r-ZUE61LaxaEjquZnLB_772Wyxve2PmdG3uvxV7oMJRadsm82hrlSU6iJKNTbklGx4_M_aOvdZajEP-tLI1lHrf1XIkq8wf_L7WarCAiKRRYEIArcnyZZ0hL-zkxpsLWPgHyT-RhZt6VBvwazErY8XZbuo0aMbmqYdYvZ5JYYg0kjsZsML9w9wV5PwfG1ddRGCOri1qhVJTXBC49eO3YSi0S2SuhxOqTcQxvC0AlaqMZaSYG0FOZ4acv8B5OKudDBhIwEx1DS78SufsPkLfWHdey9Jt2qQOhivV2CCzCi_qNiSMV8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
ولی اونا میگن شکست خوردید! این واقعاً چیز بدیه برای کشور ما
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQG1Bf7K3WoDNZucOQXODHgEBUUZe0OhcUTlynRtVvDbEJHJldxKtSQ_1g-GtgQ6h0IG_R_aZya9fsfHWhvGe8b23S20_Fv0KiSU_GgYuljalTgg6-IPC1cI9UV21S0dYeNYV_sNh--ZHGRi5cBRO3xYE-zpRs-tYDpvxrlDO08kzw0VCpGg5ulNTGwUduIlQzXVqWt167c1VWeetjaaGdRn2xz5E7yWWobRpZTjGV7fZtZGiUqrXer9pswIG8XCDH8hE5oGcrhYtD0GGmxJnIjx6vvRGuXu-_mBA46b6fGzlVsZNCbRQBjDG_1AFGUwgG5MTbnW6NFLybNCAmdOKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=AHsk-AFkV1czkb4uIT1ASaH-0k-xUM5ZbIG1pHTBKLwOBXbqxVqn-2WjlQeeZp5swArT_MIbLIpFlaAfG0DztiLwSxQtEzg4KpjgOjo7cN_Wp-SlvTpnEn2kOGTi2rxTjYpAv5cYMtFs34QqKjjCT4gGMnOEp-qnK-_7dG7nNEuSFU6PflsMwLU4s6FJUNDkPDBnHBsK0TkIV4LqA46I7s_HawsRZUdNLM6PXdxBd3XXLwf2Ed3DJPeo9G62NPMY7CINsAiXwguO9sNZVv2OZeQs2ITM6f3MrxR8YyrUIQfVaSfTQ-NoGAacLur0oa4EvzQrAMcoqqvZwP1bNCro5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=AHsk-AFkV1czkb4uIT1ASaH-0k-xUM5ZbIG1pHTBKLwOBXbqxVqn-2WjlQeeZp5swArT_MIbLIpFlaAfG0DztiLwSxQtEzg4KpjgOjo7cN_Wp-SlvTpnEn2kOGTi2rxTjYpAv5cYMtFs34QqKjjCT4gGMnOEp-qnK-_7dG7nNEuSFU6PflsMwLU4s6FJUNDkPDBnHBsK0TkIV4LqA46I7s_HawsRZUdNLM6PXdxBd3XXLwf2Ed3DJPeo9G62NPMY7CINsAiXwguO9sNZVv2OZeQs2ITM6f3MrxR8YyrUIQfVaSfTQ-NoGAacLur0oa4EvzQrAMcoqqvZwP1bNCro5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=fbtRmvmMhu2juQnT6d82SJYwUX70Y60c9h7czVP7hDIq91Q8IhxHokjUFCt_RfqoGJPQ9TiQGf4x5W5_jLwl2HHd1lNHmw_j7qxntfO-Q6CEwqr17B8rEHXLDoLCTIupF4UOMv8qBGzesNhVBUBzIU1KlcD6jiZUuCHDK8Bgs7uLbuZAQ2tY63sLkvzY-7BIgWCPsnvb3x1Jq9FMe_RLAIGtShSs6n1Sy0mak7stLBv3yl4Wo_ujG-5WcKH-qgTwz-Q1H7beSMRFxJDEaqtmXZxcrqpozF8EnpFyqqINUwtvewikWNgCaXWtvZ-Bnfml5DN5ZhyDVq2D5mMDGk2IYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=fbtRmvmMhu2juQnT6d82SJYwUX70Y60c9h7czVP7hDIq91Q8IhxHokjUFCt_RfqoGJPQ9TiQGf4x5W5_jLwl2HHd1lNHmw_j7qxntfO-Q6CEwqr17B8rEHXLDoLCTIupF4UOMv8qBGzesNhVBUBzIU1KlcD6jiZUuCHDK8Bgs7uLbuZAQ2tY63sLkvzY-7BIgWCPsnvb3x1Jq9FMe_RLAIGtShSs6n1Sy0mak7stLBv3yl4Wo_ujG-5WcKH-qgTwz-Q1H7beSMRFxJDEaqtmXZxcrqpozF8EnpFyqqINUwtvewikWNgCaXWtvZ-Bnfml5DN5ZhyDVq2D5mMDGk2IYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=BRBuRI9Ld6adgyp8WJgNbYALNEMXssVdRv3PCJ6QsJx-uKV2_J0Dq4ISxJBxV1T9MU0v-8--7C5zgvMTfELFzGpVf25cNH6nG1eJYGpyHrUWCq9xsnY6B0EAIXFOrk33kY0H1e4UBukzLHRV8RUq7K1gNJXvW-SbI2YCfrwyRGkfr5iMEZFLdTyic9CpJ2wtFXm4aPT8j6Mc23PJHANvCLmQHlR7YyV_ddyzA2v27JSuzLhr-ks0hs6dmzdi7jezgZRtPxeIKtRU7SP2xuodhxefOwIDKprrF7YF67sjmtVjDRW05w-S58-wt2TsC5f7wmHUx2ArDuEUrtjtudl7_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=BRBuRI9Ld6adgyp8WJgNbYALNEMXssVdRv3PCJ6QsJx-uKV2_J0Dq4ISxJBxV1T9MU0v-8--7C5zgvMTfELFzGpVf25cNH6nG1eJYGpyHrUWCq9xsnY6B0EAIXFOrk33kY0H1e4UBukzLHRV8RUq7K1gNJXvW-SbI2YCfrwyRGkfr5iMEZFLdTyic9CpJ2wtFXm4aPT8j6Mc23PJHANvCLmQHlR7YyV_ddyzA2v27JSuzLhr-ks0hs6dmzdi7jezgZRtPxeIKtRU7SP2xuodhxefOwIDKprrF7YF67sjmtVjDRW05w-S58-wt2TsC5f7wmHUx2ArDuEUrtjtudl7_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eU3Wk2CqRnSJf4L74Zb2QwtGbkM-qDntucju01SpTEKsVZu02qfGh_quDHr7r2vkD-IV1LYfswf519NGCaqsF4EtCTe7SvVcxsxsclBETqT_E8KLlOxITpopbHRB0E7d95Q2Kgd3eVAI2_DzU2N6RG-H6tXq-TfkwPitJE_95WGqzjUYTwV4R2aZOMHrru_nXEQ5tWNTyophPDDZ9rZ4BFnBj6z1tMW0PMLY3uAAGrSnTt4bcbJjvr-Qz92_3_IioaAJX5s_z9P6uJR9nGif4EIlkAsFsBJEbxzk-dOztB0Ws3ssHvhQIKb4VhPx8eXLkFUtUlB_IVTRR35qbW8m1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H-MfbMm_Gvrt2fT-xm-pvz3VBXwGQjL7B74zqYEbmNdEEs3G1-Fjb7T4RHvGg6x4DWcwzMg9Y6TlZqrT7uJ82xzhTdWE7eXuUJGVpvWpetmbniFM51gH2r5p8E-vLtqGObHlMbKlbPvcW3XgDLThiBVOkREdYHjH7wEKMTsb5jXZVwCvartZaHaiygCc1teIxe8VIcoFG-0lzKsnFg-7oEeeJ88fadGGs5sLkqm1xJH2pBAeGsQdmAGTz4JR5DjUzRgaT9riZlfg4Op1J-JuhvrEBXq1gYPLBqUWbYcMZgOdGMBJ3_6nj_JofUmC_cLslvW8c88aSErGQ7w6W4tt8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=cBUCq6tGVDKg9g8SgWXf607D8tfLzTtU804tww1NLJNxk6ModCIAutV_gAaaQRrP84wrBv2vqA68owzrAnpp1Qf13QyXxXOrix9AWb1ZwVzwSlWgamZaAX-qx_1bCAykVXPB7geQbzvg7FZIcycV5GFpctSJX_ob4ffF5a_CykfhIVfrvaGEnV0dBlgmLnGC1QGr0xxyKNUXrwTIClIoCaG_kA9Z-udkNIaAjOgwtxMPiS4Z1SH0TJRXB-_CPSZ8kptI14nuttxC9bvvEWdGYldVEpQk5lvMMv7BAdgtdS3p_XRZqdFyubplBBt9_vGj8qF9kvGawH1w5Vb-g7n-Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=cBUCq6tGVDKg9g8SgWXf607D8tfLzTtU804tww1NLJNxk6ModCIAutV_gAaaQRrP84wrBv2vqA68owzrAnpp1Qf13QyXxXOrix9AWb1ZwVzwSlWgamZaAX-qx_1bCAykVXPB7geQbzvg7FZIcycV5GFpctSJX_ob4ffF5a_CykfhIVfrvaGEnV0dBlgmLnGC1QGr0xxyKNUXrwTIClIoCaG_kA9Z-udkNIaAjOgwtxMPiS4Z1SH0TJRXB-_CPSZ8kptI14nuttxC9bvvEWdGYldVEpQk5lvMMv7BAdgtdS3p_XRZqdFyubplBBt9_vGj8qF9kvGawH1w5Vb-g7n-Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عده تو عید قربان خاتمی، روحانی و ظریف رو بنر کنار ترامپ و نتانیاهو چاپ کردن دارن بهشون بعنوان شیطان سنگ میزنن:)))
خوب این ۳ نفر همینجا تو کشورن برین خودشون بزنین
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=Axo1V3PnzgviSWeFUBS6bsAhaplwoVWbK9RV7oNvMOy9DaJO-TBa9_2g3yOBIXM0GRakjJW9bVffisMU0wYjaKSW0VYYvYjYi3DMv_Eiey_MzLcMPien82MuYUMh6JUeklfIG9zIxKDiNp65heBRQZNMj1hF_PkFJPdRNRaQrAU-nZLHdVH74sjGzdmif9n7iSJrghz97-MQcyQjCNXHuByp7gw-8p5Y0ZY7PyNnRmVAnkTk8UwEV6yxlTAyLy_wirncum4Id8Ficmp0gHuO3aN7mcqn8l6jq8MBanQ8JmE7vcwJpUFkwyoL0MuVU3EcErXV_TMo_mKXcpBs3oBLyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=Axo1V3PnzgviSWeFUBS6bsAhaplwoVWbK9RV7oNvMOy9DaJO-TBa9_2g3yOBIXM0GRakjJW9bVffisMU0wYjaKSW0VYYvYjYi3DMv_Eiey_MzLcMPien82MuYUMh6JUeklfIG9zIxKDiNp65heBRQZNMj1hF_PkFJPdRNRaQrAU-nZLHdVH74sjGzdmif9n7iSJrghz97-MQcyQjCNXHuByp7gw-8p5Y0ZY7PyNnRmVAnkTk8UwEV6yxlTAyLy_wirncum4Id8Ficmp0gHuO3aN7mcqn8l6jq8MBanQ8JmE7vcwJpUFkwyoL0MuVU3EcErXV_TMo_mKXcpBs3oBLyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه‌ای که معاون رئیس جمهور آرژانتین نزدیک بود ترور شود، اما اسلحه در چند سانتی متر جلوی صورتش گیر کرد و زنده ماند...
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65165">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا: دنیای آزاد هنوز ماهیت جمهوری اسلامی را درک نکرده است
🔻
شاهزاده رضا پهلوی روز شنبه ۳۰ می در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، با انتقاد از جمهوری اسلامی و سیاست‌های غرب در قبال تهران، گفت که «دنیای آزاد هنوز متوجه ماهیت واقعی جمهوری اسلامی نشده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65165" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65163">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-d69XVomi5XJw9_bh9cBhxGWybIuqf7DxqKZZ4NiydQXD0-JmQUKu5tc6MNaAzVrEIhgboc1vPOpOSessTsZoKLahEh9jhflGPUSnDSlo_NeHoJqWPLXDFH5FcjTpZMVRAb9J84ciJ8dGjwNSjPMP-rZDU6lP04jS9HVXwAip0VSFnWfzognzW8XCOUdCL3aTHUgLiw6ZpSxNFcrJ4HzG6XuFL_T37ugUhwY-CdF4b0BpQjyz290ut0lXMnIUQd64IRNN66039agV7J3EL6gYx53HfQfMV-TzwqlF3p_HCPFmVFZJ3oH6S-4Aj31UutDuC27ob9rWQDJvrtLy8j-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته‌ای که تو تجمعات شبانه دیده شده؛
والله هزینه مذاکره بیشتر از مبارزه است
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65163" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1Tala-WzMpr4VIVZlfHBSz7domGUez-kDn678KSwlPHNEwDX54HpISgkZ8TSTXU5ZybQ6AJ7sP8WaIMvb_5ppsGy8W-9BZBrp0D4Q78aKwC_2LI2BEbITF2eXuMRMsFOLvF22OE_GJ5g2D8CdkJJou1R0CsQRoeSGAFteFYcVA5Tib6-bikIzGnsegBP5tl4-ISJr29lUGjO5a5h3UsCoAlg_3-Po_oEP7YZOVGp1n4PPl47vDn6F_3xPOj1Q50AdX5tQpGaJL7uGoE6Myrx31nd1Ntg1vhAVm-DaB2kb7JofyGZ_SuYGiQDgcZT4Xkclbw7cBtHifTvBa2AEgQhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ny9zdNYSNlOU9KJQXG3IDAnbZZmJmgdunHEkRKFO19cTz3PGQbyYneWqLIVq8CDvadbKB0axyCm7IhwSyyecjxWqLDnhelk7R6eG_R41Ywl_R_lkRNO9j6d1Obvbfm0p_grG7_okx3srDjL4x5P7qymawM0ZmGoq-97dflCtBUm8a-WBoJipNAjLa6z-1w7lm7385LBhJBJsWE-zMnJ66r70rbVunGEVaqVUP0U5F-5mJS35EE-B-pMeEQUyhTwWKXEYwmA2M1h67VP7zTJFTvxNZie6sdXMGcpZWEpcic7XYDzf53qTyvjVyEsAqoeFUcSiVLav66_nDaN8nYAavA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65155">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sEm86CjlF6VQRM5VqC0bAESXh5oNrKpHOTyWohLtEVMxCBf-FpC9ZH-XYPX59OmoENVLH_iy22-leUydDlpBTb8bp0KalgPiZ_LqcQAIZ9k3AZ4x7oGEbnsPw9hU_NzJa7SNdqfKCua8GvLbAeZu3iBxJKKDkq16KH1qdQxPgCV4nAVmc5Eq0JPu3eQArtst8pOzzZe_yE2YF-CNJ2jGG1ip91uOPNTQYdjQ6MjmTGTCWHVJrprCuUppWvbVhnr8zOMFWqbrdjzJkjr6yqlSjFAZoXfhTGdxi-bDEgyM45kYNcyM5Lsx0MidGPGUkY5oZzl3NzYQdxVqPcTuSaWijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RcvF-Kv0HrXG5cLwdCwEmLe_OaDWS2avINCkz6vusjXxoln1gFJtTsQdnnzZp1Zwk5m-yEE3uWY8njFKkuFKvOpy4_gb0hc8YAnHSCFbR7HwJ1vXjBahfaPMWATyv7kPOBUIjS_ltaKEYUQyTnNNIn7_JqlHsbbk4B7dz3LiRe_Gc5qw07djduSXlmSe5wqoQR90ZGPg7LS7N3xT-xWGxT3IIyn6KLs6tQek5xBlK8mzFu8nfnIwUpC8EiwHEwQadjTPE2omPPVEW0IL5G9ezy9ifDTYd75fsSnagMMdyWtlccqDphhi-29W6OXJrGNrmNlS-2SSVnGcCcbI8x4lwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ملت اینجوری دارن قربون صدقه‌ پزشکیان میرن چون حق مسلم مردم رو ازش گرفتن و نصف نیمه بهشون برگردوندن!!
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65155" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65154">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ixa67y9gGXVGouClLQXfyBwlSk4TgFTZe2iN1ETWlcwYH-uniXjS9xlD8cKWjPquaxObBqgL2Uz0ungcScmN-rJQlFQMfKA-9RLzIlCohFBNG6F8KkwgMNEwfzvdCJtfJHMUNKnwfetbpTreuj6nyPbu9JlVB1ebzY9aSWWewAFcef3FnZDBesEEeeZqjqDBmtg2OJfDuAz93R-QwgTKrvtJ8oBot7Fz78axss4h11ZQuzGplNBtBlr8u7CVS5sk2k9Eye_t0qx1nc4RJAWBYbjer3-bn3tYVpol5iXP1-VK-XFs1yLdxlVvhrzjozwWOmFBEVbr5RtxOcKhacugrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از عروسی‌ها و صیغه‌های نمادین تو تجماعت شبانه حکومتیا یه پسر ۱۷ ساله با یه دختر ۱۶ ساله تو تجمعات عروسی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65154" target="_blank">📅 08:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65151">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=SZa40P2dVOpHT-FXDMTLu0arznfvQIXmtrVWH1VMdwEB_oGb1Db5wkRh6sFmVQsSkxtfuHOHfrvygFO0It8I4w9CbPR6mSRahyLW0zg96geDz0N4QwDaGlrp8aHr_LXEZygge2ghIPjf_SgIXCTPjYTnH2PgDIa8iWhTdJwmUAEb6trXYAlARrMY-Vf56P3bArPlxt4fwnk1HV1EznBdf5kgVS_tyy3Y0t1NCkiFcTNpcG0ViQw-aDWky6N0k-Wuv0dUrYeWnMXSpj9j_FSx1mLtEOYk0vma2frujoYtejvAvy0d3e5k6aLBAGacSBSWaHSoKV_75NCFum_ZDuATWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=SZa40P2dVOpHT-FXDMTLu0arznfvQIXmtrVWH1VMdwEB_oGb1Db5wkRh6sFmVQsSkxtfuHOHfrvygFO0It8I4w9CbPR6mSRahyLW0zg96geDz0N4QwDaGlrp8aHr_LXEZygge2ghIPjf_SgIXCTPjYTnH2PgDIa8iWhTdJwmUAEb6trXYAlARrMY-Vf56P3bArPlxt4fwnk1HV1EznBdf5kgVS_tyy3Y0t1NCkiFcTNpcG0ViQw-aDWky6N0k-Wuv0dUrYeWnMXSpj9j_FSx1mLtEOYk0vma2frujoYtejvAvy0d3e5k6aLBAGacSBSWaHSoKV_75NCFum_ZDuATWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اسکات بسنت، وزیر خزانه‌داری امریکا:
ما حدود ۱ میلیارد دلار از ارزهای دیجیتال ایران را توقیف کرده‌ایم — کیف‌پول‌ها را به‌طور کامل گرفته‌ایم.
برخی از دارندگان ممکن است همین الان در حال تایپ باشند و ندانند که کیف‌پول‌شان گرفته شده است.
این پولی است که از مردم ایران دزدیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65151" target="_blank">📅 00:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65150">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rE48Ip7-4JeNrJXUnt7np4x3tBX-79iyhpSHwUHejYODutB-goKa-NHWqWeEoS85aQfVGLs7daFz_B4brLiQLqUZkNyyr2GiiGYhfKaOyo6vQST7uhidKLdsAtCaVSdK_CHSzilRzRjIRHbk6h6WbAgwPs6rRY98Ji7gTR9UwiMaq42sibFb1yNn5iq9CbRgEFy9XUVEcjbr7GB-OO7DhnHweM3dAag3U4lLaIeBUQ7QLwoi6YVJtcX8rXX1ySY89ivay1UeOr4FbyeoZzNqOyh4fCreZysddjfCTeKMZzf6w_BoeZ9HvN1cPo45uVnCiWvK7AXRIxnDT6C8l6hqPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویل بگیر آقای املاکی!!
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ترامپ باید بدونه که ایران به عنوان پیروز میدون شرایطو تعیین می‌کنه
نقد مقابل نقد، نسیه مقابل نسیه، هیچ مقابل هیچ
البته برای موضوعاتی که مورد مذاکرست نه آرزوهاش.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65150" target="_blank">📅 23:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65149">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohxD7Ac49wldck0Fex8EclhF69gRkWsgdadF6lTVtst8eQoKUsSGZ-KkKnkubX29wrDeTQMQZZZH9OkUZVkJdD2FSS9Cjb-kSuzHG3a-oKPkuxmpiuQNxj39GUHIHIDbzE3VHK9O6SFPUbB8vhfvBPL2I_txhIIPu4iC6XrLijtKedN_boCEzZ-JK18u2qkv5puxP2isJTenAEJWixW347coU0w_NYXEVa-TK6TDCEPQcsAo2VuCphZcjaXu6LjZ48xLkZWkycoOyNpRhBJw3daVRWg7zlWNOH54l1Zx9U_C4watAn3llcKXLVYGo5LQ-UuI_NE4w1H24IahoBhlLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمودی، رییس شورای هماهنگی تبلیغات اسلامی تهران: ستاد آماده‌ی تشییع جنازه‌ی علی خامنه‌ای هست و میخوایم با جمعیت میلیونی برگزارش کنیم ولی زمان‌ش هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65149" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65147">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
گزارش فعالیت پدافند قشم
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65147" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65146">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‼️
بقائی، سخنگوی وزارت خارجه: در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم؛ مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65146" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65145">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خبرگزاری فارس به تازگی اعلام کرده ترامپ مفاد توافق ایران را تحریف می‌کند.
او ادعا کرد که ایران موافقت کرده تنگه هرمز را به صورت رایگان باز کند و مواد هسته‌ای خود را از بین ببرد هیچ‌کدام در متن اصلی وجود ندارد.
ایالات متحده باید فوراً ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران را قبل از ادامه مذاکرات آزاد کند و آتش‌بس کامل در لبنان (طبق شرایط حزب‌الله) نیز الزامی است.
این توافق هنوز در انتظار تأیید نهایی در ایران است. منابع آگاه اظهارات ترامپ را ترکیبی از حقیقت و دروغ توصیف می‌کنند تلاشی برای ادعای پیروزی زودهنگام.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65145" target="_blank">📅 20:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65142">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyQlTawTF2Bvkk53j10AbPs3AECpAvTuNhM3aYtU5cfeJ8wYHxHiXgl9MGUnnufmVg7w95dKFTr1l719gHApfDZQG_CHDwIglrJADU0nKMaUeZich-p45s2PJvvW17yMbqIu05aOTDINTA7wPMltx_EGKyynuolMjAazHsKGY5IzytpfENVl4eBI7yRq_jFZr1Enz7UH2WVOMElcSh2QaP-BLjtW85-hvRGYmlQJlCcc-YyvnM9e_iSP8U38c-Nr0JJK3xFGE1myxtcBw72s-8AsA3yGRWdbuKG_GqPG61inLYC83AckUnFMghBAN1LieZaN2GQCYnegit5twvpCqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
۱- امتیاز رو پای میز مذاکره نمی‌گیریم؛ با موشک می‌گیریم، مذاکره فقط برای اینه که طرف مقابل بفهمه قضیه چیه
-۲ به قول و قرار و تضمین کسی اعتماد نداریم؛ فقط عملکرد مهمه. تا طرف مقابل کاری نکنه، ما هم قدمی برنمی‌داریم
-۳ برنده واقعی هر توافق کسیه که از فرداش خودش رو برای جنگ احتمالی آماده‌تر کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65142" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65141">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⭕️
🇺🇸
🚨
🚨
ترامپ در تروث : «ایران باید موافقت کند که هرگز صاحب سلاح یا بمب هسته‌ای نخواهد شد. تنگه هرمز باید فوراً باز شود؛ بدون هیچ عوارض یا هزینه‌ای، برای عبور آزادانه کشتی‌ها در هر دو جهت.
تمام مین‌های دریایی (بمب‌ها)، اگر وجود داشته باشند، باید از بین بروند. ما با مین‌روب‌های قدرتمند زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز فوراً مین‌های باقی‌مانده را پاکسازی یا منفجر خواهد کرد؛ که تعدادشان زیاد نخواهد بود.
کشتی‌هایی که به‌دلیل محاصره دریایی فوق‌العاده و بی‌سابقه ما در تنگه گرفتار شده بودند محاصره‌ای که اکنون برداشته خواهد شد می‌توانند روند «بازگشت به خانه» را آغاز کنند! از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین، زیر کوه‌هایی که عملاً در اثر حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند، دفن شده است، توسط ایالات متحده بیرون کشیده خواهد شد کشوری که طبق توافق، همراه با چین تنها کشوری است که توانایی فنی و مکانیکی انجام چنین کاری را دارد و این کار در هماهنگی کامل با جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام شده و سپس آن مواد نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی رد و بدل نخواهد شد. درباره موضوعات دیگری که اهمیت بسیار کمتری دارند نیز توافق حاصل شده است.
اکنون به اتاق وضعیت می‌روم تا تصمیم نهایی را اتخاذ کنم.
از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65141" target="_blank">📅 18:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65140">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYGh42H6MNf0qMICRbMhm_EKxZvgGiJ8KaBT7SB5glAabNnInKNECU5Pc5nRrGQUVrLFeq8NniuBcAbwbR_8OspDyR94RQdtN1GVlS8Ohd_I8RMpBfhW8CP5fKEi_mDH4CHJ6_1FhZ7tHsrVFudfnkHBCBR2mw8s0BC-VFy0L2fVinMiKRuc02d8CFcTg7CoHyZmajXn6l9JXBPKl1QSILQX4nPNU-YDpCDAjQv1pomdE_-rH83wpafOsowfuYYUZxXEhB5NgH1Ju1bA69hg4hxc_-9o_ru7tkPz8z3I-hEkOCR-PhimZL1GsSi99HKUFmJAIJyqzcpiCD8yzlCVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی مشاورین املاکه
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65140" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65137">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WmRjxCdSNKL42bi0L_mxPuvqPybg_9jKFvqfJ4vM-cckbNVcQBoaupLAYVNQKGxsrND-YOOlph69UfXEedCJ2exuGM9Qny1xp9uPrdNKg6xokObvoXkDhgDZ5ug3C7B39LzB6mCtaPFFCShrGjx54w6iTGqEAb57hE0lPb9TkxfBsK-hOhOX84ivoBcVr1X2OG3mJc7XYfe6VYJzoPY-gdzoLjGcvzEuz26sMMQFeKHWEXUc58o7SLxlF3dVssssoso-8u4dNyH7pSCSJErZSeYEoChvIt6XKuwqXw1q-SpzNW20qjfAZFavwzpEMesSfpxrecNYlkcAegycX1ngPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نت نداشتین این دوتا شده بودن سمبل شرافت و نجابت حکومتی‌ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65137" target="_blank">📅 14:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65136">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcwqMeOo-WK54bwYZvsvpxPDQvkmOjkSQXpHQyn31PAdVtCFDlpiwHaD-4m2dGwUEly3j3eYPpIJKTf7SuD9n0k7kGmH8paCpaCqni6JLiYMeB9t3w-0C2lXX4lzla5j69LhcXVs0liRAOTCA2dbvOOgR1C8RjJrXLsykJBQje4R95IZ_f4pt2eRySpwyu4wGng2fotRiHvZUn7baDod_ls4j4783D7XzVUJ-FJi1zxJGSIRJWXa71BjZDJcE4EF4iuODCKFbOLwyZDLqlchshwqO1JmU_MGgCDEExUfbS43WD_c7JvvdAD_jpQF6pd-0wQjei1o9VRnPoAhwDV1AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های حمید رسایی تو کانالش درباره چه کسی شایسته جایگاه رهبری است با آیه‌یی از نوح و پسرش که حتی صدای خود طرفداران حکومت رو هم درآورده
خیلی‌ها میگن مجتبی رو به پسر نوح تشبیه کرده
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65136" target="_blank">📅 13:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65135">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=AZ_PgVRGIUkgg2F5-jKMkpYqrOYFpq_lfwCMTVSWjROZHsIUKQ1CiaHCBQG44i_QGIxgEq8USpIuVcK7IpYTFFbFTQnM1ldILlPVn1KcnxmEyNgEHP5ZZ-yRKsdpkUSQ-8yPKcjjGVKQz7WiUBf7FCDkdMP2hEw8m2-cq0nRoTZvGcGCwJlfMWwjuOvTx4rdnxOB-aVYxyuZqNU4vCRsRfBL5Lpj0ROzt-Rl8KZ3chDKSLFBbXCF86cq3WiFMJvkKKeoiaHPCGVa6WvNJD3scpOGkPXFwH79jOkC-wPAgsW1ixfP-7uIOtQ-6w8HSmSfP1z8BEyTvzjF7po_RcDN7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=AZ_PgVRGIUkgg2F5-jKMkpYqrOYFpq_lfwCMTVSWjROZHsIUKQ1CiaHCBQG44i_QGIxgEq8USpIuVcK7IpYTFFbFTQnM1ldILlPVn1KcnxmEyNgEHP5ZZ-yRKsdpkUSQ-8yPKcjjGVKQz7WiUBf7FCDkdMP2hEw8m2-cq0nRoTZvGcGCwJlfMWwjuOvTx4rdnxOB-aVYxyuZqNU4vCRsRfBL5Lpj0ROzt-Rl8KZ3chDKSLFBbXCF86cq3WiFMJvkKKeoiaHPCGVa6WvNJD3scpOGkPXFwH79jOkC-wPAgsW1ixfP-7uIOtQ-6w8HSmSfP1z8BEyTvzjF7po_RcDN7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماهواره فضایی شرکت آمازون دیشب حین پرتاب به این شکل پشم‌ریزون منفجر شد
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65135" target="_blank">📅 12:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65132">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnAyTOvkN--T9mMU78Z0ImV8IWX0N8Q_8b7HKwZfHbPlPsdWQ-0Dm9faSvsyHXSc4plLrQBSecgwDkDhrJlN8Vv8s4RK9gy-KfJRdnsb9JXmgjS4tc2tL-JL5a_5Xyg5P1U4wtIToPqEf5GdDrepXWP6tM5-c8hDtAw8k9M4IIGHzMIlOznj3GgW4jGfI0aBRS56oMlz0ir2O5NgiYJ27C6r7edTHeCLSjAr6xbdAqG4FA2rlt-_bpQ1l_ZMV89DI6j4cFC-aaADtVrRS86LzZF2F3GoOATnMenS74xLTllfieB9916_eTwRaY3Yfu5p0HyrF_r0eqznNrUg_xE1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
واشنگتن پست: دولت ترامپ داره به اداره چاپ اسکناس فشار میاره تا ۲۵۰ دلاری با عکس ترامپ چاپ کنه
قبلا ترامپ ۱۰۰ دلاری های با امضا خودش تونست به چاپ برسونه و اولین فرد درحال درحال خدمتی بود که این اتفاق براش افتاد
همچنین طبق قوانین امریکا عکس افراد مرده میتونه فقط رو اسکناس چاپ بشه و از سال ۱۸۶۶ که این اتفاق بی سابقه‌ست
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65132" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65131">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=nZEPQQ3nEE5A5wVyczy8Eegvb4CzOqBxThzZPeDVQHdQsiFVlJao5tI2-nbOGo1TMiZAae_8yJQAxxfKOf9qSLsyToy36P8WISpx_u5HYsCLQO-sVZlUk-29PqmeG2uirZwdxR9KztzTP-XFjJoLaPhEvetz40r-Q76C3hWTBOdOvofSSGlXpUa8CRiNxkLMU70qfrfFHlbOWidAeXgv5AVY7ug7pEj_EsnOY5oMfodXPIcLWC1tEspY9KxACQRln8Gg8Q0AqXDQCTbNd0Qvv5qlPhXDJiG2Vnt8Jm8yFCgrqSOC4eFAXdTL4lHrUmo6LfpIRKCrvVljmduQZNPiEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=nZEPQQ3nEE5A5wVyczy8Eegvb4CzOqBxThzZPeDVQHdQsiFVlJao5tI2-nbOGo1TMiZAae_8yJQAxxfKOf9qSLsyToy36P8WISpx_u5HYsCLQO-sVZlUk-29PqmeG2uirZwdxR9KztzTP-XFjJoLaPhEvetz40r-Q76C3hWTBOdOvofSSGlXpUa8CRiNxkLMU70qfrfFHlbOWidAeXgv5AVY7ug7pEj_EsnOY5oMfodXPIcLWC1tEspY9KxACQRln8Gg8Q0AqXDQCTbNd0Qvv5qlPhXDJiG2Vnt8Jm8yFCgrqSOC4eFAXdTL4lHrUmo6LfpIRKCrvVljmduQZNPiEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: کشور‌های عربی مثل امارات و بحرین و مراکش برای تاسیس دولت فلسطین به پیمان ابراهیم نپیوستن بلکه چون اسرائیل رو یک متحد قدرتمند علیه ایران می‌دیدن به این توافق روی آوردن
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65131" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65130">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLI3e5raVr3742QNoSfiMvgUyB0Irhumoot_VY-yZR-h6huFkEbUp0mKNwcTohv1f1p9PQXF38brXJZj7uXLtmf4Rndz-8Iz7EXOA6UCwiub8x0xX_hur63GMEl5EmROMweAoRI_4sZVTWBt4-r02daAfV_Uts5VYlJ1Wd4bA3pKOxPTBvQ5ZS2c3mrlHbKNOe2pCpzJOZt2sVsf2exyvl_CMZztspjicn2pPmA89Kno5SHOrLpD0cLEgMA3IyaI95FNB9EPwP7YJQHaxDNcofYay4hTBIYQE7HQ73SuJblB_B2DQNjV6BFRIbi_IzadOfhNfmb_C1oCfqpeJvf4RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش دفاعی اسرائیل: از زمان عملیات غرش شیران تقریبا ۲۵۰۰ عضو و فرمانده حزب الله و ۸۰۰ نفر از اعضا رو از زمان شروع آتش‌بس حذف کردیم‌.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65130" target="_blank">📅 08:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65127">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
گزارش صدای انفجار و همچنین پرتاب موشک از شهر جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65127" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65126">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011753724a.mp4?token=lBgfV1x5Bsuk4DXSincn_v_KHLXb12L3ilRD7KHGfTUrs-PD3urho49j8oig3OJNuW7YyEnNi7TK6BejWz-FqSK5flpdH4uevPx_WgP_o-gVWezrmwKc1B_9roiGvEiw5RWvvby8ABwUDPJ0KXDI6Tsd1t6QB8T4nuF7VhtvnFd5a8oBgqboVJfCuXV6ouyQhZvE3iplojDvbiMqg6abyc6Oghnx42Xnf8En0VhnqzBpsdejonq3H8SWOIH4scYveUAkbzK2_BsvjVOS20OxRMDX5azhBqOw3hlqW7J101N-MF-KsIieve-iHon2yuvKuaulSWitMCg7uzMIxXnbYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011753724a.mp4?token=lBgfV1x5Bsuk4DXSincn_v_KHLXb12L3ilRD7KHGfTUrs-PD3urho49j8oig3OJNuW7YyEnNi7TK6BejWz-FqSK5flpdH4uevPx_WgP_o-gVWezrmwKc1B_9roiGvEiw5RWvvby8ABwUDPJ0KXDI6Tsd1t6QB8T4nuF7VhtvnFd5a8oBgqboVJfCuXV6ouyQhZvE3iplojDvbiMqg6abyc6Oghnx42Xnf8En0VhnqzBpsdejonq3H8SWOIH4scYveUAkbzK2_BsvjVOS20OxRMDX5azhBqOw3hlqW7J101N-MF-KsIieve-iHon2yuvKuaulSWitMCg7uzMIxXnbYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا کاهش تحریم‌ها برای ایران روی میز است؟
اسکات بسنت: هیچ گزینه‌ای روی میز نخواهد بود تا زمانی که تنگه هرمز باز شود و ایرانی‌ها موافقت کنند که باید اورانیوم غنی‌شده با درصد بالا را تحویل دهند و نمی‌توانند برنامه هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65126" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65124">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🇺🇸
#رسمی
؛ توافق موقت ۶۰ روزه‌ی ایران و آمریکا نهایی شد و متن توافق، فقط منتظر تایید ترامپ است، هرلحظه ممکن است خبر اعلام شود
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65124" target="_blank">📅 22:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65121">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=Gi2QR-6KOTboupLcGfUdEwuwPB4N6NrGCU8lvP-k1453vySryw2cj01AYbmyly4e-F7z8ZDqaAWsQdEdMPYGxQUftNnT6G98tv0WIUiYDLns-1iixjLP92fXyzzQjvVQHtoMxyeT5aTBDAS99DfgRD6IfefS6hPPUstNNf2O1vYuQ6fHWTxenAiUEHh4nC9c6VGDCYY_8HGVfoYNG_s1g6zz6wKak5DjLY8x1hH7RjVPNbwba9yCadCeBzW5wHIYCp-274Di441TwYNK-CRNseNT12jVxH7xrVrTB6s4r9vjkbyAWpjvn7bDpI9f_G028WmFxmXFxUFBSIZd44ENRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=Gi2QR-6KOTboupLcGfUdEwuwPB4N6NrGCU8lvP-k1453vySryw2cj01AYbmyly4e-F7z8ZDqaAWsQdEdMPYGxQUftNnT6G98tv0WIUiYDLns-1iixjLP92fXyzzQjvVQHtoMxyeT5aTBDAS99DfgRD6IfefS6hPPUstNNf2O1vYuQ6fHWTxenAiUEHh4nC9c6VGDCYY_8HGVfoYNG_s1g6zz6wKak5DjLY8x1hH7RjVPNbwba9yCadCeBzW5wHIYCp-274Di441TwYNK-CRNseNT12jVxH7xrVrTB6s4r9vjkbyAWpjvn7bDpI9f_G028WmFxmXFxUFBSIZd44ENRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالی که جمهوری اسلامی اصرار داره یکی از بندهای توافق آتش‌بس تو لبنان باشه  نتانیاهو و اسرائیل در روزهای اخیر بشدت حملات رو علیه حزب‌الله افزایش دادن
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65121" target="_blank">📅 22:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65120">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">به گفته باراک راوید خبرنگار Axios، به نقل از دو مقام آمریکایی، یک تفاهم‌نامه ۶۰ روزه توسط تیم‌های مذاکره‌کننده ایالات متحده و ایران مورد توافق قرار گرفته است و در حال حاضر منتظر تأیید دونالد ترامپ، رئیس جمهور ایالات متحده و تصمیم‌گیرندگان ارشد در ایران است. طبق این گزارش، این تفاهم‌نامه شامل بیانیه‌ای مبنی بر «بدون محدودیت» بودن تردد دریایی از طریق تنگه هرمز، رفع تدریجی محاصره کشتی‌ها به بنادر ایران توسط ایالات متحده متناسب با افزایش تردد آزاد دریایی، تعهد ایران به عدم پیگیری سلاح هسته‌ای و تعهد به برگزاری مذاکرات در مورد از بین بردن اورانیوم غنی‌شده با خلوص بالای ایران در بازه زمانی ۶۰ روزه خواهد بود.
علاوه بر این، طبق این گزارش، این تفاهم‌نامه شامل تعهد ایالات متحده برای بحث در مورد کاهش تحریم‌ها برای ایران و آزاد کردن دارایی‌های مسدود شده ایران خواهد بود. همچنین قرار است در مورد از سرگیری جریان تجارت و کمک‌های بشردوستانه به ایران بحث شود
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65120" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65119">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⭕️
توییت جدید اسکات بسنت وزیر خزانه داری ایالات متحده.
دولت ایالات متحده هیچ تلاشی برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
به ویژه عمان باید بداند که وزارت خزانه‌داری ایالات متحده به شدت هر بازیگری را که مستقیم یا غیرمستقیم در تسهیل عوارض تنگه دخیل باشد، هدف قرار خواهد داد و هر شریک مایل به این کار مجازات خواهد شد.
همه ملت‌ها باید هرگونه تلاش ایران برای ایجاد اختلال در جریان آزاد تجارت را به طور کامل رد کنند. روزهای ارعاب تهران در منطقه و جهان به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65119" target="_blank">📅 19:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65116">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5tJu7diDbU5Tl1tyjxv5JC0Gk6i2NEps_VXxqKd8V5v3NVbD2m01yV01DnL_9-inYE5QQn-5EHjPi4LvDZoBkE_kFC1qF4BbrHMtYY8RSjQtq5bB6LSYvp_eIUmqkG3ByvX9h2a93FoBxa6HdGpCUx1E29bu9t7aszBIiqg9Auozk6QbI5EtMqoNQameI44UbJ1e3nsicHIiSWJGxVxpJGRYpUmp0sgxHB73MR2LQgmsnZzscyM9ktdxSr3O0eu4gwAcyAbYBcqSubeFjowNnQylp75jAnt4QlOS7JIOm3sz-D894l_iPVCHkEr_H3xnCXLFV7gTsCClQ0e89NgAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
آکسیوس: اکثر شرایط تا سه‌شنبه نهایی شده بود و مذاکره‌کنندگان ایرانی بعداً اعلام کردند که تأییدیه‌های لازم برای امضا را دریافت کرده‌اند. ترامپ در جریان توافق قرار گرفت اما به میانجی‌ها گفت که «چند روز» برای بررسی آن می‌خواهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65116" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65115">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epbc0shujL3qJ19yxSoN7sSLWYc0wPXoAZ6mHLpx04U9rEoaG_8HTq0YD3yuHXmGvnMbwFJ4N1oMVgc7Jhrc6YyXKL3PZAkWY0XLGCbhohP4Yp4nbMz0AIzSvLj6EZBwJpvUbf6EouHQHf3E3873NVvWwKT8qUCFzXBSekhyY_Iyg2t6qAHQfOsBNpBJXzfiwtJ4f5zRduSJ_z7Ea4iV60pBnl-e469qKOLBDFaX0x9nPk1kWt7BgKcmAjupHH-fVAUzmqau16vTsXLVP8LVtskze00rXV68UNxEwUHsKT6N5sgIzqOSQ2YY95hHnUoQxXCfF5JNbtqhR4C-lCumnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوارنگاره جدید میدام فلسطین از حرف جدید مجتبی خامنه‌ای درباره اسرائیل؛
" رژیم صهیونیستی 15 سال آینده را نخواهد دید"
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65115" target="_blank">📅 16:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65113">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHLoznf0wD87TY2Sk6shVXubRHBXnfG4H9cPLKMAa_6z2g8EQy4E1O-h8RJt_6Eg769QyrOfN0gpRHx0bHwFSXf_d0KJKGOgeDxoX-ExcX7FKXhyOYeHSm6aEmVSDZPYmuq8RKqd1-f9alOmcp5EVMhRi0-HpTTVtIpiPCPYUTdt6IF-PnGuFgrrxyVANH0o4JhjfWTpMtKSCCZYAakw1wUuK83lpLBAk1BOTYjLS7GAJiXEs6BJZ4Dl2UnPq-85oRXWYQ9q9ER7omnkZUIN6gI9WPQcX9Qbt8J70Gq4iOjg81f7-Y-SQbx6QwyRHKrosZmuse4cZdSdqaAVOYzzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
نت بلاکس
: سه ماه پیش در چنین روزی Iran دسترسی به
اینترنت جهانی
را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با
فیلترینگ
شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65113" target="_blank">📅 16:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65112">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حملات تازه اسرائیل به جنوب لبنان؛ تل‌آویو از هدف قرار دادن زیرساخت‌های حزب‌الله خبر داد
ارتش اسرائیل اعلام کرد حملاتی را در جنوب لبنان انجام داده و زیرساخت‌های متعلق به حزب‌الله را در منطقه صور هدف قرار داده است.
ارتش اسرائیل در بیانیه‌ای کوتاه گفت این عملیات علیه «زیرساخت‌های حزب‌الله» صورت گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65112" target="_blank">📅 13:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65109">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس: ایران ۴ پهپاد یک‌طرفه به یک کشتی تجاری آمریکایی شلیک کرد. ارتش آمریکا این پهپادها را سرنگون کرد و پیش از پرتاب، یک واحد پرتاب پهپاد ایرانی دیگر را در زمین هدف قرار داد.  @News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65109" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65108">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/news_hut/65108" target="_blank">📅 03:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65107">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/news_hut/65107" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65106">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">چرا نت من قبل از وصلی ها بهتر بود، چه وضعشششه آخه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/news_hut/65106" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65105">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">عمو Pishgiri بهم sms زده و گفته خشخاش نکارم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/news_hut/65105" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65104">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/news_hut/65104" target="_blank">📅 15:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65103">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/65103" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65102">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:  @News_Hut</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/news_hut/65102" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65101">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLHRnwjx1usDKj8xOcegJT3CjjjhZQK3Fu7z5RYzInwtQz-mkRxd06k-wG3cJroBmk2J9gSLbwPY3TGMvwI7gp7lvcJ064OPLONk-UsXOQzP5vxu7FV10Z46Ie9kVW7Fo9fMpp8mvF6B1C8ESF2CVEzmWySHMti0EBOWaq9bgaCF1HB3NjIRn9nlZTryD_dwEym9w3P2tvkFQtIOA_3kgT5px6A9cpILcTnjcx4KUNHEShWeI0k804NpOPgy7k68sb5I5KjVWomKxcWKJ-PrDJpNKLAl5Hm3p4kLZqCfJPzdO9u_2nIl7kPE0c8puUTS17T2b6_jPY_CR8ewuVrOhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@News_Hut</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/news_hut/65101" target="_blank">📅 08:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65100">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">امروز ۶ خرداد عید قربونه
@News_Hut</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/news_hut/65100" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
