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
<p>@news_hut • 👥 215K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 00:57:54</div>
<hr>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65244">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etppZTAWnDqlgUAy-8IUesOFa-qvngWgdLRHtFWv5JsKmg2SuHoQCWnnoyESGxADmK647bSkDTn22G-G7kUjETHhEFn_7eZrYa1y1Jq7eYFxnCGqPMtBfAHFs5aEs5aAT_oQuvQE_vAOTMuvl6bw9OWPhKcaGD7Ofp71dvaZ75njPlufWaQ1MHnu88LVafWAUnfr1vwRMUukg-GtSWY721WTqtwjqViJyRimOK2zgW-Yv09MaTnnouWH267s0MN_zRJyRs93EFatzuYQ8oF0TuQsrMixmPX9n1tNNqn5FydF_Eg8D6Vw0kQKXGak0yEM8CCgVMA9i4W6fBu0ihV4gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هلند
🇳🇱
-
🇩🇿
الجزایر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
چهارشنبه ساعت ۲۲:۱۵
🏟
ورزشگاه دکویپ
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
هلند در
۱۰
دیدار اخیر خود،
هفت
برد و
سه
تساوی کسب کرده است.
✅
الجزایر در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر هلند
۳.۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر الجزایر
۲.۷
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه : هلند - ضریب :
۱.۳۸
🧠
نه گفتن بخش مهمی از استراتژی است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/news_hut/65244" target="_blank">📅 23:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ku9d9iKsvD22FpmLk2jFwj0_ecmg1Ry5uEO8JlgsFmo3Jl2YMV5J1YF9HjtblXyJTKo80C7Mnold6XoVovYoF02OTIHiPSlDbnBrMoo8YwyomO7MxfzFS7mQ8TBrJAZj63dYIeafSi8CzV5t6GZ_ggzZUsq4aZTk4Jv2l-JL_2zw_4BgwH8zgJB3cfwxEjD0SoBxVwrPDI41badaJAny76gRqnfVuyaudR-X93TlOll7txxX0uJLBsDQ92Zi48eoRR7TB_1rRa4gd2p342LCZ3r7nJmBIj4kojgI9KHub5_6QNyWKJVawvX5PGE0Kp44HWcUWS2R9ICywfFfud5rNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLt6jmARb6ZOmmMrIeLj9LeW-3bzkYr9DQcwOwt2fCDMYWWDDpl7rSU2UWiRdAWMlQagZO9wbN_n9imsNPBslfi5jYJq0KNJWxAe_n85OPBgon_PRiPJwgQXbrAFM5hK9dh9pXr0EK7H7R7I7rFNhb4QA9H5mdNbNGcnJK3csJ_XnN4M49FPO_N24OsdvwO38iztM3qUsW598bPCYij230boaF4-Fkr5eQr_iFEdVN0QpSTyPEMWURGlS5oJIra8k9cS2jl2T6qny0SKZkGXy56MOAXdr9bYoS0aOT4mUOo0UP5dMvERmOVS6HwuD0fpf8sBPUPXnFlz5aIGUSO3GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8M3OwsPa6Pk0mbONLPOXfacatB-sABeZe0duoy6NyptYbZpDpfB00P7UAl66BklKOv6IWouW878iSCyJoL1aqWRGESJBnQbYEC7zuO8XF0PHDHeLTAR7C3Tf9jxaTPn1lM7JEr9-pOBrIg8ERw0KOfshmIfDjX7ILnbEHc8J97ewfWqj78jkGyDIHBl7etlJcqhTR_1Apj9On_hH3u7JScZm_zInIgnEmKvFKD3uS1-gPeV5gxVn3qjz5cP-4jLd-EPOUViqiAxNiK7YymjTS7S-VC9gC5jD67R3SWghLc4rvI9WbEshC2BCansqpKnF6x7PdUDG4NvASrDijnqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Etu05lbtOvyBbiUa8o5fbQR7tmHbcxHgsA26GYvtaahKgW4-TnZwHfvLR5F-z26I6VkJ6dPeMIMgsQvbfVflzMaq2vnwF8Sou7nw2b57qKiJIYE9iY_IbvJemI0CY5Eh5oVHlRatxNOdyz-SdUxf5ISvSXfm_NYG7JPveZsCwZRQlt8lfCRhWva5Y0VCdHR8N3uayZlSkqnSCRnhmyJN20gRTzvy7PzeF80mRDZ5gnX01rpSUx9WlaTNC3t10AVsVz-HB9cF_wI1w_N3Qkud3PXBm0griCI8MVeDr0JQzOMkMebvQVUF3V31FKnCnkQjc1u-ZJoJYFWYT9OLurKwvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMscHHxFCL_aknogGU6wZWj2I7hoc_hGzYx267vywa0REDajKFUI36B4GAxoeIQsReEQ1LDc8PBttBYvBESo9_UnXoKB7uWeXQSneX88EF_IyDDWmI2THIQBZK3By7i24eKRSir_Lp65j3RhSsxSN2ymLq9YmuchuzxboZlq0jNI69TsLSGm4uNCCc6kaFSK4Gf1mIb3HLTyQbb_X_4mRqtBuvoNkenN6fPhA4xW6OHGA1H6FjdQPn3TUaK08qGyDwWTUGPaoy1AUTesAfA18A3QLluPsSsaOmYQqjZAZiwcMmx-jn7rrwSztIl5YnsDMrLIfxwob6cIOx3TzSSFcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=mmPcCkPdnC_pMKeeDK-192HrGpp7N-JOTd37W-Afd8TIg-xYoOiv6lEUnvjZJ2rbhKqdHgJpPErlQuC6Z82YolVI-pW-Z-rDVM5azV6nWk9QYR9X3KwP50qZmzsO0OYZCi-rf-HVXmidb-vG9ogW66DZwHmbQJVpOo7PnSLfZaFpDBOSCcDo6tG4nfcjv5MZ86wAXXrHvxJ4TwNSSWdMcUZqehdvTm0p2aCw8fq1MhNsJqYifsS1qLAD8NzcbswFRUpelpHYABgy8pT_t9j4r3-tpw8N16cy9H1jdPkKEIAqPF9JT5r1sSPrTOITZB0R_Pd21PcmJJmmtKEreXTkCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=mmPcCkPdnC_pMKeeDK-192HrGpp7N-JOTd37W-Afd8TIg-xYoOiv6lEUnvjZJ2rbhKqdHgJpPErlQuC6Z82YolVI-pW-Z-rDVM5azV6nWk9QYR9X3KwP50qZmzsO0OYZCi-rf-HVXmidb-vG9ogW66DZwHmbQJVpOo7PnSLfZaFpDBOSCcDo6tG4nfcjv5MZ86wAXXrHvxJ4TwNSSWdMcUZqehdvTm0p2aCw8fq1MhNsJqYifsS1qLAD8NzcbswFRUpelpHYABgy8pT_t9j4r3-tpw8N16cy9H1jdPkKEIAqPF9JT5r1sSPrTOITZB0R_Pd21PcmJJmmtKEreXTkCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=veCPnEUV4cpojdLmHvthy0yUr-FpRbXGB6OeqaOszyHrzUmZxDAE3C4kpxw3DLayAl1sPsJXVgGhrceulvf1BH5s4CRvf6C3xIUyUhC-hCBZTwyhEQg4NEaNXLV1nK6MLOMffnyPZZNTdqyiIyqsVMXqbfIAr58Au1dOzhWHNYInNLTD9whICKZcBlKxT8XFn4VoWNzjN1AHa-xFtT-5otEsovDHtgbONSoLYfe2wCNzIv96HJP6chz9ql5igLCtCc8QKbgrl87fRdnDwDYSxOzKiorkt89QVxbaOYq8HJoLAYF4CpV1679bSd5EHCycMd-33J2aN9J-NAWBus8AUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=veCPnEUV4cpojdLmHvthy0yUr-FpRbXGB6OeqaOszyHrzUmZxDAE3C4kpxw3DLayAl1sPsJXVgGhrceulvf1BH5s4CRvf6C3xIUyUhC-hCBZTwyhEQg4NEaNXLV1nK6MLOMffnyPZZNTdqyiIyqsVMXqbfIAr58Au1dOzhWHNYInNLTD9whICKZcBlKxT8XFn4VoWNzjN1AHa-xFtT-5otEsovDHtgbONSoLYfe2wCNzIv96HJP6chz9ql5igLCtCc8QKbgrl87fRdnDwDYSxOzKiorkt89QVxbaOYq8HJoLAYF4CpV1679bSd5EHCycMd-33J2aN9J-NAWBus8AUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zbl4PsbquC4mz0muOoRR3_DoLGEa_FvWKedTndHj8LcthbwdHf7SG_BEevZf0Kx1WUgeeUsmtHEBtBcbr5Dy8uWSKwhgnvMpw3zzj3bL8m5DUlPWePJCYLKRxeKyqwYqNA3pCo-83G45BJJf3Bt-uBhMKAtWbzpCsgbSdb-SlP5BhrbmOa6RcN_ByJiXVS7QiE7Y5U6OjLJOXwvu_c3bviF8871niK8sp_DHmLfmy1nv5g7P3yM8oDDUkuEcXGb2icsHxesKg9_-SvOCYCnGd9PKnktvOxXMmwIBuYnNj4zs_396Wini_Mgz37fA7m5kJN4qS58wuOnpWz8A6Yp9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZFpjN70IYsebvtxBxl1mdqP5GKgjE5p5IDIYuvOu4y8iZzJu7wueogz52H5Ijb4OH07BecxZCcaYH0KUGuNXl575Rr57ytV4NSdMaLe370iXT_IhGQ5i15_1QbWQhmrugBAwZng8zr3NVk_DhiIOyJBi56qUkFWPKi1IQGkwBh3S186BsL8gLssm6eDRvOMmInsYTifQPUA0DyNQgqDDaTiGTb2ZdIrv5UnvCuFb8QatH79TK_bzlsqYnT4JKGSjtQew3j61aTcmgac1FCRs1liZuaCJAxzJx2nYunt9w6Du8Ib6Sei43P39qkdaJnPeCDJsdCOpg5Lupf4G8spDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDD1ovtvFSUowgsUgJvBa6rhB3S-xq1kS17DdC1rhFt28ILdWnuY3tJw7WRPkpDnbuN4udE_BaLr3M6EWGciqVuzp1mH7ZYGhShJnaJ5cRFMEMsOAQlxgcIX96Yh2onc0nweG-6SCr_Bmo79pH_jhKxS9WQbTI01b7PIDCEzTotcHkLXC-wjsuzR6uZlcoQhyj8A9ptN6g2nthHNzT-yd_hO31LyZiBvuUXpkW7IoFxhRNajOmeqdktrR0mR6ou7kIAp_tYY6mkS__QOM_mp1Ilk2nSH584TjnhBrtzw7HlHdh8AS0uMjX7jMyMDO1n9QzGyBot8TpYZ_ybqr1DOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E7FUuT7QIn0QajiXroweGSZ210iFboSMGiHtuV5255NgL8DlJo5AULzXvsUq0dAOH8oKWMJ0pYloQB6KyhLXfkyFRE5dvffJf3d_JDxVDGbPUE30BLL-AIl54GIOym1oqUCWxBtcRcX2tYa1GnuosqA5alSmqz-yKGTyz7XUhVoahYZq3LnVQ_8DqGt5NgZPp4BOX7O-sQSe9yPgr2VE9DMisdVJl4HrBKxsGjTRz9KA-LsJGVjxcL1ZOru_A9t__oQKQ92VRHklBDnM3x6WMnWGi-2zZ9TdtXcRzvvqGckv8VpiO7Ae-Z6Cb3TWT2rCEXcRMFQK9Phy7LbysUTK5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rgz2tQTJ8Uuwp7hZl2Tz50EpWa55lLO_SfwYvPR9LgyYksdeCR3U4tjomJf5ENrNXS4BzwTqBKq7L92QlYD7323QifbZi_pJS2s0bYis7Nh3ROLUpNTbHMV_aEMFjSeaZaVffyseC7zmJECXb8D23qkY7_cqR_SfwQCNxhmECqo9qVCZbCW1hYXhR491xRuxoo3hmfFio714Yj0N0IeRQCuMHR26_9DiXraedND0tj8CNJZZENiwGfsb0lMqTz4LFNoo8wnXUyQk8IZNhXE6GMFy6S733nbVUspmRRI8u8_8DgfVBPTOydksJe7UMHu2ryygYRcbHEQVXIrO5ZY4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V65hvx2l_fQr-gpCbfeeq2VCKvldSkDOmVSkptvpNZLXGsN7YK4FVhs6MKWzB2VVOEsfmosE2lWIFAI9fQcBujDpp2mlHjURrKpkEieAiKHvg73k6fo2kSuAPD6FVoMEKRULEs3JbzTzQZYoa5Gu7B4ukoaOX8pCnj9SC7mLTTqm87tIHxzaUoJdsHmu7kugJ-oyYWysSNATcAp7jS_JfaDPSMb34aYbdWZnSwB5ixYeuSKii2KU5_r0BY_Zb-2yGyWE9cYsLZXjnOu-YIaG3nQZ2PB5zbe6HeTEF74MZ7PUlCyhwBUZEKEtrwLiWCrixyKuNcG814fqBKqvnnusdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJ_dhRbkrtypYPRcRk5fDorRUzzMBUnsJAmnbfdjD1UkV8vTdHts7RPDrrFqqatzXzXnSdx40hAHsLw2eyDHV7mL-GMjs1vjGhCipeNO6QGvm8QSF-9j5DNEURn6E36oDdi8WG3BjyXoIvhgcpnf-pufsUqJOAFfsllkJ1WnqMXYpXHt2atGNhxdLaJQvg7EZzwL63Y2F89C8wsQqcNlV2jE1_B7B3MDXJup_SClgVaRwfRJJ3t7iPHCCHwx8jaaIsfJMUAmb5AidQPxAua-NiwYdvpms1crBxUjurM6e1Q4pyeIQa1FcebGH8eDeIAeAWJkEHkQe3mPBgWwjEFTPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIde6lNrIKK9u_kCweyHQdKnpSAT79b5XBF2g55OzkomWt1OFrw4y-2lL91395TOSe-wVI0dfwitL7zXsDA_wJ390c9oDu5tEnbZb67UFxzOkWwJeg2Totp1OwuHqECDxFoEOxFdZa-jO1jBjzTb0GX29YZgQoWC82dLJL1rH2Gp9ieWbcPoOhwvKAon78XxvYOMbWw9hTJHGtazyEHmEfehz9rc2M5tVVEQrSSZcNq6ZcqFfLwnGJ0SmgeWZt4vhk6qtn2KD8cKCkT0jzut_p7Q_vgYXzMGwGc3v2QDlVRfwTfUC4geSz4k6t4MWg6XblRMwNnJUVcxomE0_XPXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sykf177Ml0p8PcYaTgDp_h5iOybmaus347VwE6eOBUb5B1bnRvB7SkLmhdrtB_a6ulvZJK0HfZ3lCP2MTXYgK_9srMiLnIbTZq0esyOzBwK2QoiCvpZS_D1BLP6v3RK82YoSJPrC1qS59ORgbVtJGej6uU-4u0aE9T7noLZiMlmtSd5knCj-zCaSGYeUHTk8SnIy6qFb6R8DcH75RiDdad6fqHALiAlECMrD3kp3LAqF1WOsPLq2ebNB6eLwCuwYs8-syEg5XWikjEoTrahKyJGeg2ps5Ht1sDm5VJbcPraeSLmAFSSVJiAYQF6eQeFq6uxWesWG4hb7OwIiTtReLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH8gqv6rpUb6hvzC6fDJKorWobc_m-qQcOA5OW8H3uc2_ZwXs92q0S84k2lrjs0dnrIWVpRKLjlGHtGERv41t8IMctmF7YtcPG-Hy77KoqE53PuXwAAYqLi7shYJx4vR_98w86cj83TNSROtBah4WTDHEdPjhwGmD5GYb-jDzjlThnQiBz9P6PMtq0pcRKxjLiqTpojWbt5dELOZX48YspQKROTgbA8WJighNydJ4_0w_BWuCAmN0oGTQ6VnuGKZ1E7-k3nIAzAN4IJBfy-7CnUWRp5dKUCcczV03d2KtJKc5rNTggQ_kzgeGEiiqf2B2nP_8gjuKeLui1kBp8DHQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2WayGNHLOSG1fhoKmICngTc19157PPDvnpwSlx25HpeZ5eg62aQ1rP7RbyA_ug3LOQmz0Wh6DB0Htu-oAAEX99NiJmOP_OaPsD-yUGlm6c3zBKgVfBRokIh-PZhco-tNRWbabbCz3K7KwAu7JPbRkkeZQjor1WhTnrnMBtKdjW4OgmI7OuJCa6mSmltpzOm1zgjs1unm7O9GhwoPDYqaf10yNxfB9vP-vnj3SQFa38svk3MFzD73QOEA3vnXt7giGVnxsGHqdWdTaOYEYRrH1ELsibGBZt4qol0dlJpef29k620eKjRQVm742k0pkMEBMeJpoWW1AMixbQt6xuPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iUsmiMVJIeBajX0fpUWeUJjBywfTMyg1b3hFB7KP7Buh2o0J3Fsmmjy2gLWtjCsjt4H3dbLWpRyLlgguyV3LAdbnIDIXqjSOLoTQtb_JsvGpw7C-xkkTpwSjJxUynX3zIEC7QGCdJ3-5NcIEz7Q0-aaV2iRbI36LhYASGdMqEVBSicXvSa3qMbMT6B4r4TcYpEvTmwaU_OVomU-ttjDVDP7sqDKe4hYGMSLHND6Qpei1aSMYBL11XNK2iC0IfMC-beViBUA08IVHJX8m9AxUaqkKrKmVA-Hg_HYXEFuR8V1Y3AzjDHUvK3gwn0KcD0qVYcH6T5J7hgHyPrX6A15cHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=VynAMgVulODf3zQhvVBgq8Mj5Gia3uiAbFSTn8mW2ORISNridL17ujF_5O4yWIsjOvmEyubUwU2mQLmdOnE6EjnRmtMPkNRTZV2B_s66p9-O1zAok3_5Im08EC_xRSWNwNIp3YcE4_Iz3gp5xc-ph0UTYlyiVFzJKMofxC1HReJdYkCho-2bLr6MBj4a6P4CN2WFTsEiV81pkMDzczRIF0Vg35sTzdMGru2sRWF8sVkxiAY-nV5GSzkdUu95N0mDMuf1bph_V2eljKqvynICcUDuZJ_mC29H4q8zm88myE53K7cug2ldeCVGvYRcIj3cwZSZLQv_nXPM-kUFHgBSFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=VynAMgVulODf3zQhvVBgq8Mj5Gia3uiAbFSTn8mW2ORISNridL17ujF_5O4yWIsjOvmEyubUwU2mQLmdOnE6EjnRmtMPkNRTZV2B_s66p9-O1zAok3_5Im08EC_xRSWNwNIp3YcE4_Iz3gp5xc-ph0UTYlyiVFzJKMofxC1HReJdYkCho-2bLr6MBj4a6P4CN2WFTsEiV81pkMDzczRIF0Vg35sTzdMGru2sRWF8sVkxiAY-nV5GSzkdUu95N0mDMuf1bph_V2eljKqvynICcUDuZJ_mC29H4q8zm88myE53K7cug2ldeCVGvYRcIj3cwZSZLQv_nXPM-kUFHgBSFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvEQX5M8AybtMTD_dcaAAwFs2psRaznc3nVGEDhGDYT_TdKfGPT4zbIIgTVK4sek5_A6ZH5wMbcsW8htrYxeMCiICMon-ATFpqPqxZGRRAd1e0Whqh1bpU9gEIbqqG2uwI7JAPmQiC5g9O5BMsTV9dfhKSMaJ0spJVXJumNPoDVROdaa5KQxgmb5HjDyjBFDnO46ORS6LGyc89KA306x72dhYaL2TQh84m_CZ4HaljZM8OASPjguPGzHD4CKae2sgcUU4Di_2pFssj8rSl9sEZGF-xj5Qa6LBKkcZShyvA78IUfvuGvuQGSq0ds958_7Y6deSKFDTsPNyRBWonw2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yw77hwxfDFDddx9uC6HxfFvkbNbgxgSZxnHYNgbEx2LNS2jJohyiIiTUHsN2ckzS_Aq46nUD42pytc0o8pMb4Uz-3zmvzPlrPdUGpcYza1x5J6md-laZXpF5-I_ZmY-WOVlhHQo9-ype7mfT4688lIzrR1Y4OOt_Z_DviOR8Uvh0i8USZnhRNW85M5kLThynNOoNO4RSL0u_PD4QHf8e52B8MVSBBcrZHvC7d18r8PfKrf2LvU8hqcpanqTjvs3JUAdD6WY2a7m-oITTZe8kV7ZWMO7VS5Me6bAmo1UPf_JFbrLD7bg73MDbnoSTMp2wz37idL_QxbV81_gXIWJnsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=ZHy1TElLBps6SiKezGGJ8tnAS-E5OoQkylwffSG2EvbA8y-SPiZ0llGqtR1dqtTUqcVAFGM8jaGstKb049v73cMpyunUrrt3cqlxBPVmppSlwYug-B4d9Nr3CtWyvZOAntWkvm4n_w9rIkgr6aPiArReZQl3hbMHvNFjmGkcGzejHr9cnqaqmeZVQZwaViQsuHt55gtNFRr8svkbGu7A59k8vncCerkqLS-PF0oUEV9yUSDj3YixD5Go9XtxyCbHBnUqwWyGn0K4NtthgDz0on0nUAryWuTh9pHjOs9mqCBdlAZEOVrHVmzANIzUhYzfRSlUnSys0qahgG_x9nMbUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=ZHy1TElLBps6SiKezGGJ8tnAS-E5OoQkylwffSG2EvbA8y-SPiZ0llGqtR1dqtTUqcVAFGM8jaGstKb049v73cMpyunUrrt3cqlxBPVmppSlwYug-B4d9Nr3CtWyvZOAntWkvm4n_w9rIkgr6aPiArReZQl3hbMHvNFjmGkcGzejHr9cnqaqmeZVQZwaViQsuHt55gtNFRr8svkbGu7A59k8vncCerkqLS-PF0oUEV9yUSDj3YixD5Go9XtxyCbHBnUqwWyGn0K4NtthgDz0on0nUAryWuTh9pHjOs9mqCBdlAZEOVrHVmzANIzUhYzfRSlUnSys0qahgG_x9nMbUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=BRBuRI9Ld6adgyp8WJgNbYALNEMXssVdRv3PCJ6QsJx-uKV2_J0Dq4ISxJBxV1T9MU0v-8--7C5zgvMTfELFzGpVf25cNH6nG1eJYGpyHrUWCq9xsnY6B0EAIXFOrk33kY0H1e4UBukzLHRV8RUq7K1gNJXvW-SbI2YCfrwyRGkfr5iMEZFLdTyic9CpJ2wtFXm4aPT8j6Mc23PJHANvCLmQHlR7YyV_ddyzA2v27JSuzLhr-ks0hs6dmzdi7jezgZRtPxeIKtRU7SP2xuodhxefOwIDKprrF7YF67sjmtVjDRW05w-S58-wt2TsC5f7wmHUx2ArDuEUrtjtudl7_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=BRBuRI9Ld6adgyp8WJgNbYALNEMXssVdRv3PCJ6QsJx-uKV2_J0Dq4ISxJBxV1T9MU0v-8--7C5zgvMTfELFzGpVf25cNH6nG1eJYGpyHrUWCq9xsnY6B0EAIXFOrk33kY0H1e4UBukzLHRV8RUq7K1gNJXvW-SbI2YCfrwyRGkfr5iMEZFLdTyic9CpJ2wtFXm4aPT8j6Mc23PJHANvCLmQHlR7YyV_ddyzA2v27JSuzLhr-ks0hs6dmzdi7jezgZRtPxeIKtRU7SP2xuodhxefOwIDKprrF7YF67sjmtVjDRW05w-S58-wt2TsC5f7wmHUx2ArDuEUrtjtudl7_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L35-88uoP4JwJ52gWXCxva9ba0VUeRJUw0Ody8nvYsp5H4Jw4daQp006GNcTu2kqwwXqxTlc4XGZv4DnDeuCZ1arUxQMrknVv2dAeeUHj39Zmv9w2-d5noDuCl-9j9qcdCqqggszzkQFdeOwvEXInPfesaWfNyHoJFSSflQsoMxn5cLzie9oFadWUocWOtko1AL-7xDQr0LwrlCZQ87Ld9M8PiywscR3rP_OoVYE9gps248b1syxsVBPftzzvAdt4kuAZ-tQg-WD3LUvzntu6BR1EPzpTg1EsOUOGWwUGT6SuT-4mRGVFkabxg2b6_ZYugXouUe85lyH749plUqa0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LcvZ2RU5vtp1hWjTI9G8MSpQxbCOAGbKriAwcI9V2hIQL70YlIumLJXbxPsNuYf4sQ0cUmjMwF7LUDbwQhgG7rab4dNfRldq2j_9gudgkSfcZ-X5GbD-QSJ5ybW7s-yeglTrEuOTqMws8J45n3zneTqGOvlTZRmglVNo6xbp-b0EkQxp2ZLSHJBtBKY88NpbQjlyPMWpzafKpa3OO2jQ69DibnLNpo5-ZnIUcjBzxDGZF2O4VfTyV5h4-tVPcmHfqIBDQ0qb3D4IrGa07jgwaTapVsyG8InQY9UbQwe4s11gjUIuizcv_0saX5ApXeGzXE7KSBevbtYK-R25erf0Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=gYSzAm7G1CadfRfGud4EjH1Xg0PTkPDBSyHI0fi-ScJv5O9yWanxrSa9wM0r9dQNMI9bcKzDVehnc9AM96UzPf0JTn5xOT3FU21H5nQ7_vdJv3kvPDRU4RoN5h2Z6zEN0775IZRQUo8qmsSQN9eNt0OgnpwlMsnnkcISZxpj8Y7ho_2fIGWbIJ0XqR3K_vWL5Cu_B3otUp4LT5Zjt2Pbi8iwI6Sj96EmlcnfYPE6J8qpkpg5Dn6UM8VbfiC8xrsusyuKh5hTTcg-Jld9C5F69MQcloTxIjV_D-edrMmdetpjc0dXJkhAXHeWag-uvla7bafmkm5ibww2ILYHdG8XOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=gYSzAm7G1CadfRfGud4EjH1Xg0PTkPDBSyHI0fi-ScJv5O9yWanxrSa9wM0r9dQNMI9bcKzDVehnc9AM96UzPf0JTn5xOT3FU21H5nQ7_vdJv3kvPDRU4RoN5h2Z6zEN0775IZRQUo8qmsSQN9eNt0OgnpwlMsnnkcISZxpj8Y7ho_2fIGWbIJ0XqR3K_vWL5Cu_B3otUp4LT5Zjt2Pbi8iwI6Sj96EmlcnfYPE6J8qpkpg5Dn6UM8VbfiC8xrsusyuKh5hTTcg-Jld9C5F69MQcloTxIjV_D-edrMmdetpjc0dXJkhAXHeWag-uvla7bafmkm5ibww2ILYHdG8XOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عده تو عید قربان خاتمی، روحانی و ظریف رو بنر کنار ترامپ و نتانیاهو چاپ کردن دارن بهشون بعنوان شیطان سنگ میزنن:)))
خوب این ۳ نفر همینجا تو کشورن برین خودشون بزنین
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=tG_H-hVMak4LQrYFHP74rZ2bxZgKc3rUe1iNYhLL-nxoEekPje075f7y1FU8oNkKS8fWF2nnbBNKA3c94PppMFXziikUrLke-3rMXWtqBUX16bdI64A-PKBcSxgh8FswlmMwzl6oxbrSUDsahvZ5zBWZ8suj6nHdLjnBkMKR_o_0EAY-nUIAXyaOb8ulw1CmV8ebN1UHT9xrR-gjH2YwQLAx85xvrPLWiYujVW-CWR1f7i2HJw49DzHrQQ8tvsQT9M_bg_3ye2BPRJDTqCVP6Q81yIJQvGxBWx633qaV_iS0gEoVLc08ssLyOQh14ubuaSdAl60dEruzmmZy4t9o_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=tG_H-hVMak4LQrYFHP74rZ2bxZgKc3rUe1iNYhLL-nxoEekPje075f7y1FU8oNkKS8fWF2nnbBNKA3c94PppMFXziikUrLke-3rMXWtqBUX16bdI64A-PKBcSxgh8FswlmMwzl6oxbrSUDsahvZ5zBWZ8suj6nHdLjnBkMKR_o_0EAY-nUIAXyaOb8ulw1CmV8ebN1UHT9xrR-gjH2YwQLAx85xvrPLWiYujVW-CWR1f7i2HJw49DzHrQQ8tvsQT9M_bg_3ye2BPRJDTqCVP6Q81yIJQvGxBWx633qaV_iS0gEoVLc08ssLyOQh14ubuaSdAl60dEruzmmZy4t9o_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه‌ای که معاون رئیس جمهور آرژانتین نزدیک بود ترور شود، اما اسلحه در چند سانتی متر جلوی صورتش گیر کرد و زنده ماند...
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65165">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا: دنیای آزاد هنوز ماهیت جمهوری اسلامی را درک نکرده است
🔻
شاهزاده رضا پهلوی روز شنبه ۳۰ می در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، با انتقاد از جمهوری اسلامی و سیاست‌های غرب در قبال تهران، گفت که «دنیای آزاد هنوز متوجه ماهیت واقعی جمهوری اسلامی نشده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65165" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65163">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdOjYIZDI1Nog3BYJlAUXdtCkbswz9Yb1988YT4hCPXlcv6ss__Q3OtJikfKD0kcFmuwn-a10ajTbOn7EFzoG7VPOrBMl9ama84HC1CB6Bhdjap2rXBR6iCPKu0M0r_8PjZLfpn1gMUFWeXG5YjunbHqFaXIArIYc4cOiaLGXb_fK8xSGYR70XoFKCDm4pouhL9LwuE_BZnxAGzUzZ-XgBkSKfyRkItPHViW8hZltNpSMLaF6vMJ3p4-pb7QgzO2os7QyRQBeHIkXzTm1K9nQVBtbqZXG1d5urjJHvl47d18oYS7Wojr3mkDycne8HGqTnSPzpVXntB79oexIGV_-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته‌ای که تو تجمعات شبانه دیده شده؛
والله هزینه مذاکره بیشتر از مبارزه است
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65163" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOsd6rpZCg9SfDVnNQsD0W60_6-prwxMe24JRcHMFrp61o380zDUbPciPkNfBdz4CVWLGAM_2c1JB2gGDmjB8esVSDAZRT5_FKOuGrOM2nOZZX6iWBIJyaqL55YpmZbe4cl2zx9UZPyhlcKDJ4KKhLdhSK3Y8OUtTfR2tC671CjY14j4j9kX1TI-thyxL1xY4ukONGdXEyy2Rdqfjq0gDJTFoOV3fzLtiftBGjshQLrjftox5G2Q4-VnjLo8ZeQNX3c8D8CJ3GtCL5HeQ9xrrhbsKkIaA1wNbfwROvDeHfoMWIvYgbvtF1AriU5yfgzGVyOa0IlXNSBFlNIj3KYflQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z_i-bbxvWqRtP7LH8psgXp3LvRCWybbcMvgWw68EasOLeUvhPHL9DdyuGw1CN0npoGYAp8L_pOPHe4fCNN0qc0UGJfWhpqUKCRH38qOXTjPjQ8vQ9lexPaFQ2giwCuldkt1eH69xT537c7x5NkFPUYhENcCfSAhBZLHBh-kg9EexTw__l3l4OrctJf9wWVTyP2RtREvsEALcXMn-9MJhUFEyghMSjIGdk8Tz0psz6hZzwxuJhOJXupaoB1TF-PAV6iWUAGciL0wUnQi4Kpu1zZU-vbM0D6PqetwMLvah8KLYg_LdcFd07Vck5p5HqNqMSkh_zwSoZLvVTdBQREzYFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65155">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HmqMm5cbtJpqM1zKQEOIkq7MVTdLltWGnVJRT9rszdpQTh-7PSYA_w69nmb3fcLtwcolplD0w0cBOm6nMcKaVbPQ9ZjzyK2VLxcWTRl-mi3zrI6VgcjjkHVZiLrILtwM6qKcxRhYlWbWbx6luv6rrgMw-HktkPYIRok28v4wEORl8iGvjXKd6wk_eJb-BdmP7yZ4jZuQ269MYGg3oWHEE0ue4Jl3cnslTGSSa-Z0YOKvFCacmhaeMameyTh4pJP6dVuW-d4z52n1K4owNkcImIITwQlh_FetdO6D5EvlANltV7nZ3fikOhsn8bK6YCAyQYt7Ukhic2E-SROKiOleCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTpHR7WH3RHW_V6d60bfb3bZjh8MCPZO-d_JhDXFdVSy6m9e4La76hgVr0dnflcZlcYTpW-YjpwKv6eA103wMFiEoRrJTovPqvpVtOOYQ6JvUdHrqLExIAE1feOi7QaLqU0jd9Gh0jvgVaZ_kBtutONSEAapZ98TMBfe2vw_1oA3x91j2WBjSO9MLfAJpbJ9EVkSAgeTayEh1M4rxhp7eOceTCc4xgZi3u7deATyT_0NfV_IXrFjWWzcrnpN4c9lb-IKaVW4oeD5aKw_b2pjZDNuFRzGMv63ma8APGE1XX1gZgb9RwU18wqvQ5oc2pFmZHPBPgRVmWSLrdFLLlDPlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ملت اینجوری دارن قربون صدقه‌ پزشکیان میرن چون حق مسلم مردم رو ازش گرفتن و نصف نیمه بهشون برگردوندن!!
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65155" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65154">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m4-AxrwjENGF_vJ-vU06SEis-6D6Pk8j24ujpT7B8r-4ol_0AeXrMwGMbjWglm4LPS4U8LR8Ek_3FLq0rl7Jud0Wl00AsdnaRFZsiWLPQt2YdtLVe4eHRkq5NCnk8WU0WIeg84oxZWm9TmeQYshfuodWOJH843W6qkRIHihJHZT4UG3afr7j3zDzZWE5mMtjjOGztg8yWaQWwFTF_nNYOV2i748poGwPRtIOuBau18S5zL4gsNbsWvLvd5vZVPh2TkAXF6G4CJlaQq25zgy9XSQg-LH4XJ2o1rfBEpJ-UVPwEmC9xdvrwQ3x-pr5IeuzPZi-ozqseo-5M7gCwOwjfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از عروسی‌ها و صیغه‌های نمادین تو تجماعت شبانه حکومتیا یه پسر ۱۷ ساله با یه دختر ۱۶ ساله تو تجمعات عروسی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65154" target="_blank">📅 08:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65151">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65151" target="_blank">📅 00:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65150">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehKET4sGEYmw3SATN0rFZE4B5IQ2Y1zIGezXpcJN4fHq6W2ex39T3TFA6__lnc0kBiq8YrIOtrNZ_cwBMnIdv2iLN2VtwazgkMCA3DT_uPMeQ2hdpnBE-cIaJNTwOqVKuhgOrgA7E5SXgi1SimCm34mVZ3UMsKDDfwDcwBfM6g56cfHoDHRiV1lZbryLy4SGUP9SnWP58cPLK0jcEQdPnN10Ti4tPcoRVekyRtUvxpF3y5lE1OKCDfScvWpnK1ML8LPCMH_77EKSbQBKwkCAxOpTmyzGju5dAoFW_d9Fvg5zC1yVgZLwREXulqNNp3BwWvGSa1GHZj13QXyzHI3M_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویل بگیر آقای املاکی!!
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ترامپ باید بدونه که ایران به عنوان پیروز میدون شرایطو تعیین می‌کنه
نقد مقابل نقد، نسیه مقابل نسیه، هیچ مقابل هیچ
البته برای موضوعاتی که مورد مذاکرست نه آرزوهاش.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65150" target="_blank">📅 23:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65149">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6o1cbeYL9Ux-i2F_scrXMhGjcDnuO0LbOUjvSMyqhekDQoQhfeqqiuPboVCooXPqWwOy8XdLuqbMkehOC2TZYT2t00G47xn5UK4fah7Hn1PjPeqmw-t5fOPuOKllpRNzTWL-EGJu_MNZlV4_v67ucKsWogN5-RuO8bt9DdrgEpNsM_hi3EzF9J4NRwxk7J0H_l4_u-8lc6VZd5Ie1l8ZOvJnx1NyrqtaH4CmsMjgFHxxbEGNi62Pf4TJH97HMilAhaol3NbjK78rwCjTfChFWBjKjiIQgPTYGDKsX7ZcGfvqqqWRbzIpWkXwIsKcsOQUT3kDzGkG6QlTHusAvFv_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمودی، رییس شورای هماهنگی تبلیغات اسلامی تهران: ستاد آماده‌ی تشییع جنازه‌ی علی خامنه‌ای هست و میخوایم با جمعیت میلیونی برگزارش کنیم ولی زمان‌ش هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65149" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65147">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
گزارش فعالیت پدافند قشم
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65147" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65146">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‼️
بقائی، سخنگوی وزارت خارجه: در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم؛ مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65146" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65145">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبرگزاری فارس به تازگی اعلام کرده ترامپ مفاد توافق ایران را تحریف می‌کند.
او ادعا کرد که ایران موافقت کرده تنگه هرمز را به صورت رایگان باز کند و مواد هسته‌ای خود را از بین ببرد هیچ‌کدام در متن اصلی وجود ندارد.
ایالات متحده باید فوراً ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران را قبل از ادامه مذاکرات آزاد کند و آتش‌بس کامل در لبنان (طبق شرایط حزب‌الله) نیز الزامی است.
این توافق هنوز در انتظار تأیید نهایی در ایران است. منابع آگاه اظهارات ترامپ را ترکیبی از حقیقت و دروغ توصیف می‌کنند تلاشی برای ادعای پیروزی زودهنگام.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65145" target="_blank">📅 20:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65142">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSpWn56ddywEvFPGfm6SgJnoSLwUSppaoQYjnpoSAt6Kcvu_AVpzmf2zRTOE-UraUYkGw6AKQ7JJokHIXeeBB8tt3qV0Y61YWcL3jwEv53BC7q3ORWBFJR-SVILIXvCdDLfKUldyD31GsNjfmA0NWl2B5g9s47zxY52_LNyzc3AKDKlTZa9-1MUZpP27eo_Dmztvf6tQEFj5UG08Fp6245359ikoNqYMVzwMuQXLFIPOyUr6CyDFDi6Nv-vNRJYWiIbbQ7eH3Q1rwsyvgdCbdthaoPw0he5PIpFj821RuzeUDoCOG7AgVaPeo_F279bMvC2IR6xTUY5OoAjO2eia1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
۱- امتیاز رو پای میز مذاکره نمی‌گیریم؛ با موشک می‌گیریم، مذاکره فقط برای اینه که طرف مقابل بفهمه قضیه چیه
-۲ به قول و قرار و تضمین کسی اعتماد نداریم؛ فقط عملکرد مهمه. تا طرف مقابل کاری نکنه، ما هم قدمی برنمی‌داریم
-۳ برنده واقعی هر توافق کسیه که از فرداش خودش رو برای جنگ احتمالی آماده‌تر کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65142" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65141">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65141" target="_blank">📅 18:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65140">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFQnLl0Lm92wlOqOcHl0CUg_NLBklF-T5Jhzr2VPLGca8gLslF0UCPiTXJVuSMq8w6-pMem0Xb_LQTnkJGKdRH3PDxVV20QLTtgBrR-F8xlH_Q-lo_ySIp2D3l-_rjlYPeSXMz559L7EWfzBDPqfW0iNaIQQKzFk5HhC41dZxwTAQHxA-b3KEeIP8x8V9eKk2TRkvPTsAW8s37Ro7EMl2xT7jmcio07BGfruRCg-nOGv_GNeAhnWgdUd8gSn5xF1I1u7--NA5nzrp5xaSPPqdmslHELcZAg-ld7mXOuspU0-91baKpug35MsDY1pr9TDAO8IMQ2OBk3-WRtaAES63A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی مشاورین املاکه
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65140" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65137">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bMXu0aj804qHdeeKAfRKr5-1Bf8j-1IsMofBLTG62B4aHFRfRHyMZRSSPzIPGlPgrF2lRspKN-eS0fwk1HHj7pgxSA2VxVehqBxsdWUf5yf7EQDmNNSz21tUHjkz_-S7svvs6ePG69E6TLB6pglXGXupIyaMf6QWX6_N1SXYrecxVGM6j3qGPJkSHTm3ZlHMrBGLxhdahkEQ9_Fzf9qqPOhd69BtIZAnPsBxsSnl2oC64C6RmO44fJMO0eP61-ecNdnhdR7_mzSpnAoLY7_jpiXnn1OLXKIT3CyyXANsMBj3Hc8Q5UoYmlQ9mpUcvDYsnoHqmG1NQpyriQIGaXP09Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نت نداشتین این دوتا شده بودن سمبل شرافت و نجابت حکومتی‌ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65137" target="_blank">📅 14:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65136">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcwqMeOo-WK54bwYZvsvpxPDQvkmOjkSQXpHQyn31PAdVtCFDlpiwHaD-4m2dGwUEly3j3eYPpIJKTf7SuD9n0k7kGmH8paCpaCqni6JLiYMeB9t3w-0C2lXX4lzla5j69LhcXVs0liRAOTCA2dbvOOgR1C8RjJrXLsykJBQje4R95IZ_f4pt2eRySpwyu4wGng2fotRiHvZUn7baDod_ls4j4783D7XzVUJ-FJi1zxJGSIRJWXa71BjZDJcE4EF4iuODCKFbOLwyZDLqlchshwqO1JmU_MGgCDEExUfbS43WD_c7JvvdAD_jpQF6pd-0wQjei1o9VRnPoAhwDV1AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های حمید رسایی تو کانالش درباره چه کسی شایسته جایگاه رهبری است با آیه‌یی از نوح و پسرش که حتی صدای خود طرفداران حکومت رو هم درآورده
خیلی‌ها میگن مجتبی رو به پسر نوح تشبیه کرده
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65136" target="_blank">📅 13:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65135">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=AZ_PgVRGIUkgg2F5-jKMkpYqrOYFpq_lfwCMTVSWjROZHsIUKQ1CiaHCBQG44i_QGIxgEq8USpIuVcK7IpYTFFbFTQnM1ldILlPVn1KcnxmEyNgEHP5ZZ-yRKsdpkUSQ-8yPKcjjGVKQz7WiUBf7FCDkdMP2hEw8m2-cq0nRoTZvGcGCwJlfMWwjuOvTx4rdnxOB-aVYxyuZqNU4vCRsRfBL5Lpj0ROzt-Rl8KZ3chDKSLFBbXCF86cq3WiFMJvkKKeoiaHPCGVa6WvNJD3scpOGkPXFwH79jOkC-wPAgsW1ixfP-7uIOtQ-6w8HSmSfP1z8BEyTvzjF7po_RcDN7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=AZ_PgVRGIUkgg2F5-jKMkpYqrOYFpq_lfwCMTVSWjROZHsIUKQ1CiaHCBQG44i_QGIxgEq8USpIuVcK7IpYTFFbFTQnM1ldILlPVn1KcnxmEyNgEHP5ZZ-yRKsdpkUSQ-8yPKcjjGVKQz7WiUBf7FCDkdMP2hEw8m2-cq0nRoTZvGcGCwJlfMWwjuOvTx4rdnxOB-aVYxyuZqNU4vCRsRfBL5Lpj0ROzt-Rl8KZ3chDKSLFBbXCF86cq3WiFMJvkKKeoiaHPCGVa6WvNJD3scpOGkPXFwH79jOkC-wPAgsW1ixfP-7uIOtQ-6w8HSmSfP1z8BEyTvzjF7po_RcDN7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماهواره فضایی شرکت آمازون دیشب حین پرتاب به این شکل پشم‌ریزون منفجر شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65135" target="_blank">📅 12:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65132">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnAyTOvkN--T9mMU78Z0ImV8IWX0N8Q_8b7HKwZfHbPlPsdWQ-0Dm9faSvsyHXSc4plLrQBSecgwDkDhrJlN8Vv8s4RK9gy-KfJRdnsb9JXmgjS4tc2tL-JL5a_5Xyg5P1U4wtIToPqEf5GdDrepXWP6tM5-c8hDtAw8k9M4IIGHzMIlOznj3GgW4jGfI0aBRS56oMlz0ir2O5NgiYJ27C6r7edTHeCLSjAr6xbdAqG4FA2rlt-_bpQ1l_ZMV89DI6j4cFC-aaADtVrRS86LzZF2F3GoOATnMenS74xLTllfieB9916_eTwRaY3Yfu5p0HyrF_r0eqznNrUg_xE1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
واشنگتن پست: دولت ترامپ داره به اداره چاپ اسکناس فشار میاره تا ۲۵۰ دلاری با عکس ترامپ چاپ کنه
قبلا ترامپ ۱۰۰ دلاری های با امضا خودش تونست به چاپ برسونه و اولین فرد درحال درحال خدمتی بود که این اتفاق براش افتاد
همچنین طبق قوانین امریکا عکس افراد مرده میتونه فقط رو اسکناس چاپ بشه و از سال ۱۸۶۶ که این اتفاق بی سابقه‌ست
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65132" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65131">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=MyuekZlXMRhecEwGn5csLfVl-ql7_oXXS2ogOESbM3Cuq0CW1T90JQL9Im5bye8_neXpi_CrAX_KJkEQ4geSwFmWn25JYHzZVfji-SKDD9-ck3x_E7vSu-n9_Oy8a3HLxt1CIu2li5Rzr5etXd_7fLw0uZNQKrwmwszJMTfXuPyHIKp5TWC73szs9Jj6Kp-FTWknZKIw4_uxtLA7ZXox1MOjbUQechmpNabo19NAd4GqQogfa7SlrHJs_9qUOic4WKqivm68_wPIoY42Sj_RnqQXhQQXBkQ79nBR3QiC6a-LLvb3F8Mkj3eWv3byRKacBBVizZqWfIHwxurESBQmYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=MyuekZlXMRhecEwGn5csLfVl-ql7_oXXS2ogOESbM3Cuq0CW1T90JQL9Im5bye8_neXpi_CrAX_KJkEQ4geSwFmWn25JYHzZVfji-SKDD9-ck3x_E7vSu-n9_Oy8a3HLxt1CIu2li5Rzr5etXd_7fLw0uZNQKrwmwszJMTfXuPyHIKp5TWC73szs9Jj6Kp-FTWknZKIw4_uxtLA7ZXox1MOjbUQechmpNabo19NAd4GqQogfa7SlrHJs_9qUOic4WKqivm68_wPIoY42Sj_RnqQXhQQXBkQ79nBR3QiC6a-LLvb3F8Mkj3eWv3byRKacBBVizZqWfIHwxurESBQmYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: کشور‌های عربی مثل امارات و بحرین و مراکش برای تاسیس دولت فلسطین به پیمان ابراهیم نپیوستن بلکه چون اسرائیل رو یک متحد قدرتمند علیه ایران می‌دیدن به این توافق روی آوردن
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65131" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65130">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDE3ZRHCl03DCzJp5lY9nbaegeAVlH9W9XQmhcTY2dzmlyGz14eBa9zDL948awju2YTwn8l3hks8oFW4RXdfhf-dPDZh-AGBlJqXGFg0ddo2RNB3E0cV_VdVmUjNgc0Mcr5sOtqvDZ22G6B26Sd2ID1qijpQb8ohc4DE8Yy0ivCOg5CdVtpHYi-rr75XhnFjjrAJA22-BDlHkPC7PdxIS0UV2iBrx2ZClyo8tv_WsID_YVlAwpJVLDPAJkSs-qzR0kFmqKfWvliFlR9SS93XWv9TQn7HdrYsgLXMqdtf5tsvbDHBUh-gTkQJvApPEwIeFoQnvJ-2IG_ONJoItHG4Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش دفاعی اسرائیل: از زمان عملیات غرش شیران تقریبا ۲۵۰۰ عضو و فرمانده حزب الله و ۸۰۰ نفر از اعضا رو از زمان شروع آتش‌بس حذف کردیم‌.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65130" target="_blank">📅 08:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65127">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
گزارش صدای انفجار و همچنین پرتاب موشک از شهر جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65127" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65126">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65126" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65124">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🇺🇸
#رسمی
؛ توافق موقت ۶۰ روزه‌ی ایران و آمریکا نهایی شد و متن توافق، فقط منتظر تایید ترامپ است، هرلحظه ممکن است خبر اعلام شود
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65124" target="_blank">📅 22:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65121">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=FnE-CEMKI5vMeRnFX2T1XXSWE3_TTxbDwf-KqFelO25NeJCuYnrwaqmkn5sNcG_afQIFrNyQTQSTnKrU4Uzi2Ju5cgQP970bkuI3JtK0eCHy6dKgRxMFSm1obD-MQHksVGExV1Y7eDJ4NsTjARtxUTuXkgvzlP0XOuVc0Vzk52TrcmzqGbnisqZQ2tHX3W8a3Z3oiD8oQwoscMVaiT0ovG_RdY4uwO4nFOXXep5fAOf2Do8Ec7NGFvyHd2uUOJof6S-E4vFs1NPXQs9Ct0EpYTm-xbGR2AKpPcq5EoUibT4cVejxFSVCyYPUk_LvI9sd-tZXSosARn9Txkt18zleOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=FnE-CEMKI5vMeRnFX2T1XXSWE3_TTxbDwf-KqFelO25NeJCuYnrwaqmkn5sNcG_afQIFrNyQTQSTnKrU4Uzi2Ju5cgQP970bkuI3JtK0eCHy6dKgRxMFSm1obD-MQHksVGExV1Y7eDJ4NsTjARtxUTuXkgvzlP0XOuVc0Vzk52TrcmzqGbnisqZQ2tHX3W8a3Z3oiD8oQwoscMVaiT0ovG_RdY4uwO4nFOXXep5fAOf2Do8Ec7NGFvyHd2uUOJof6S-E4vFs1NPXQs9Ct0EpYTm-xbGR2AKpPcq5EoUibT4cVejxFSVCyYPUk_LvI9sd-tZXSosARn9Txkt18zleOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالی که جمهوری اسلامی اصرار داره یکی از بندهای توافق آتش‌بس تو لبنان باشه  نتانیاهو و اسرائیل در روزهای اخیر بشدت حملات رو علیه حزب‌الله افزایش دادن
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65121" target="_blank">📅 22:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65120">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">به گفته باراک راوید خبرنگار Axios، به نقل از دو مقام آمریکایی، یک تفاهم‌نامه ۶۰ روزه توسط تیم‌های مذاکره‌کننده ایالات متحده و ایران مورد توافق قرار گرفته است و در حال حاضر منتظر تأیید دونالد ترامپ، رئیس جمهور ایالات متحده و تصمیم‌گیرندگان ارشد در ایران است. طبق این گزارش، این تفاهم‌نامه شامل بیانیه‌ای مبنی بر «بدون محدودیت» بودن تردد دریایی از طریق تنگه هرمز، رفع تدریجی محاصره کشتی‌ها به بنادر ایران توسط ایالات متحده متناسب با افزایش تردد آزاد دریایی، تعهد ایران به عدم پیگیری سلاح هسته‌ای و تعهد به برگزاری مذاکرات در مورد از بین بردن اورانیوم غنی‌شده با خلوص بالای ایران در بازه زمانی ۶۰ روزه خواهد بود.
علاوه بر این، طبق این گزارش، این تفاهم‌نامه شامل تعهد ایالات متحده برای بحث در مورد کاهش تحریم‌ها برای ایران و آزاد کردن دارایی‌های مسدود شده ایران خواهد بود. همچنین قرار است در مورد از سرگیری جریان تجارت و کمک‌های بشردوستانه به ایران بحث شود
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65120" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65119">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⭕️
توییت جدید اسکات بسنت وزیر خزانه داری ایالات متحده.
دولت ایالات متحده هیچ تلاشی برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
به ویژه عمان باید بداند که وزارت خزانه‌داری ایالات متحده به شدت هر بازیگری را که مستقیم یا غیرمستقیم در تسهیل عوارض تنگه دخیل باشد، هدف قرار خواهد داد و هر شریک مایل به این کار مجازات خواهد شد.
همه ملت‌ها باید هرگونه تلاش ایران برای ایجاد اختلال در جریان آزاد تجارت را به طور کامل رد کنند. روزهای ارعاب تهران در منطقه و جهان به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65119" target="_blank">📅 19:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65116">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5tJu7diDbU5Tl1tyjxv5JC0Gk6i2NEps_VXxqKd8V5v3NVbD2m01yV01DnL_9-inYE5QQn-5EHjPi4LvDZoBkE_kFC1qF4BbrHMtYY8RSjQtq5bB6LSYvp_eIUmqkG3ByvX9h2a93FoBxa6HdGpCUx1E29bu9t7aszBIiqg9Auozk6QbI5EtMqoNQameI44UbJ1e3nsicHIiSWJGxVxpJGRYpUmp0sgxHB73MR2LQgmsnZzscyM9ktdxSr3O0eu4gwAcyAbYBcqSubeFjowNnQylp75jAnt4QlOS7JIOm3sz-D894l_iPVCHkEr_H3xnCXLFV7gTsCClQ0e89NgAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
آکسیوس: اکثر شرایط تا سه‌شنبه نهایی شده بود و مذاکره‌کنندگان ایرانی بعداً اعلام کردند که تأییدیه‌های لازم برای امضا را دریافت کرده‌اند. ترامپ در جریان توافق قرار گرفت اما به میانجی‌ها گفت که «چند روز» برای بررسی آن می‌خواهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65116" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65115">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNGJgJzvD4FavWhi3iB7EQ6SPS1e4c8rdCJhHchTKQiRk8RYoAx5eVGlbp0iHRnNlJiVZ510K8mWkGwurrYDz5saGGKJVuvowCZ5q_XQcynRi9mNTem98gVe_Fo9nX54sneAV0tFqIojsIh9zyjdHHfCQT1e01CVMSbqNB2CPuEB7ZhbR2QC-rdeK2jbK3aWXBueOq5h8okF1oKdN630dF_cmybvTx7D3gN-vio0PtJe3mBWlOBW2SxQR4KjRJAvaVrFVaVOi3qtxCVSfd5C0ICMWDRqoBuvvLXw_LnfYIVfUgq-ktnUnbgTvYDoTLla96oIdHdyHaWPmPYLAdaa_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوارنگاره جدید میدام فلسطین از حرف جدید مجتبی خامنه‌ای درباره اسرائیل؛
" رژیم صهیونیستی 15 سال آینده را نخواهد دید"
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65115" target="_blank">📅 16:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65113">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBF4hSGVPHcsNUZ1hYH7T0DFM2ESMoAz7Mfu4dSuwykxLraClWC645AZWaLak5TJHGuM3lywFaN6bq8CH8L6BdjRSoENgGvSk8PXQXTqVYWXkjpsgTIr71d4hYAEKJe0C53tocZDZW6WJevXhx4YS-G-hwzgUx0wxGlqRvlNFrYDvZJoe0a6fp2-xYabLYcQQukNIPckEmeOcovUzhJhDo5Efe1WC6e6fVywBj8xTwQ99bMDMIRa5q2xV3bBoZeGzXrCHeCkUZSnI0N6kBoyPI60aPiomYi6vrcVjemFwl59iuSKI-22fSCc9QvT6VCc7ORI6EP50Rn281f3vm2qtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
نت بلاکس
: سه ماه پیش در چنین روزی Iran دسترسی به
اینترنت جهانی
را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با
فیلترینگ
شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65113" target="_blank">📅 16:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65112">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حملات تازه اسرائیل به جنوب لبنان؛ تل‌آویو از هدف قرار دادن زیرساخت‌های حزب‌الله خبر داد
ارتش اسرائیل اعلام کرد حملاتی را در جنوب لبنان انجام داده و زیرساخت‌های متعلق به حزب‌الله را در منطقه صور هدف قرار داده است.
ارتش اسرائیل در بیانیه‌ای کوتاه گفت این عملیات علیه «زیرساخت‌های حزب‌الله» صورت گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65112" target="_blank">📅 13:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65109">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس: ایران ۴ پهپاد یک‌طرفه به یک کشتی تجاری آمریکایی شلیک کرد. ارتش آمریکا این پهپادها را سرنگون کرد و پیش از پرتاب، یک واحد پرتاب پهپاد ایرانی دیگر را در زمین هدف قرار داد.  @News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65109" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65108">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/news_hut/65108" target="_blank">📅 03:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65107">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/news_hut/65107" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65106">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">چرا نت من قبل از وصلی ها بهتر بود، چه وضعشششه آخه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/news_hut/65106" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65105">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">عمو Pishgiri بهم sms زده و گفته خشخاش نکارم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/news_hut/65105" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65104">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/news_hut/65104" target="_blank">📅 15:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65103">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65103" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65102">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:  @News_Hut</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/news_hut/65102" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65101">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbLcRJ6qtycO1GxfW295bRnKjjlAI6k8U6-Dnw6Ek60qXY7lCptCPG9ugL04n7cJL0pzIWNVhtc6Aw58x57DizaGKJ2gs3VBv0fKbJymkoba8wXV133aaaEGUAdcV3K-7heXx2QnFX9WWxqs7x5sfp59ZWhp1ejM7b9v-UvrNlg4usXcxPJHQ5N4Bf2_F42Yn0DJ6jUoyXQhdv0Y_Y1yHD7hLySNzxMUrGW3Djd9Se1FxN8maN-HjgH8TbF10JHUxF5jq0MCdbxyMnik8-CbnXRqRKbMVnBZfVkjDSjK5iNbTeqYAL1qc1O6O6CehCId47BRsZ0j3Bkp6wDKA0xlmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@News_Hut</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/news_hut/65101" target="_blank">📅 08:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65100">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">امروز ۶ خرداد عید قربونه
@News_Hut</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/news_hut/65100" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65099">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHx9EbtZjVgJfv02szZv3_zuFKlC34bVfgEolh1d4HFtnE8yTwS7CkdBUJLUkuYSkyeBJr8YMKSzGo5TFnmG08FX25bC9Q28dfOK9uLeZLzdnksOQQUBpB4UQI9wYRVkbupBulwcqCl-FeptFGE8pdxYDAaneaq0cYOq28GtScPsIwo_V1l25iSBKzKquK4vF16jA11pHTU3rgkwniWJ3_O6DwzSkSEgiFgdaO1jybdoxh3oHFDAJqKr_GJbFNM5xEbmWANmxlwimcqtsxy17R-iZ2YwJLjxyhjd4XaHVzw6RMOxJuEG5M_arl3ob30Oy-yQKtNxx4VdHtcImh_oBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها پارمیدا دیگه بعدش آنلاین نشده
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/news_hut/65099" target="_blank">📅 08:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65098">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اولین صبحِ اتصال اینترنت بخیر جوون ایرانی
🫂
#hjAly</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65098" target="_blank">📅 08:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65097">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">جالبه یه یارو مثلا نورالدین الدغیر خبرنگار الجزیره تو تهران میاد توئیت میزنه همچی تموم شده و فقط امضا بین دوطرف مونده
خبرگزاری داخلی و وابسته به حکومت همینو بعنوان خبر میزنه ینی شما بیصاب شده‌ها به منبع ندارین خودتون؟
@News_Hut</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/news_hut/65097" target="_blank">📅 03:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65096">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iPzx1fNg72vgEduEvStMAq0gxLR6ryDYjtLV6a6jo2K9q24VlJmzPlkEkhObazU62eBrc-tJbKhYt9Q8P4Oe42sQhMXclAemGlMdShMULO_HRphYQ7IkSL_Ewz7fr1ImwkOxr6fZmq_r1dR4blW4dd2TMVPohYY6iIa2tsUZHuoEhhCqhF5vuPYCMbNxEdV3bWchVd9TrthbbjvxUxHnJwH4LPOaPJp4397eoBairUXRcF-YFeE0szS1XaO4_Myw2wvMMmmOl-uqpVE906re30fLy0xU6IbqvUACoS5NubmVeDN6uq7IICa_h5c45lqMmDP_Pd3VTk6PGT_QUT5rgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  «اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/news_hut/65096" target="_blank">📅 23:59 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
