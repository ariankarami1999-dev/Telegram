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
<img src="https://cdn4.telesco.pe/file/FndBMVPKIZfOBegxH5jLnafjadZaEVRrJev0Lm217Ei9x8ZL97LI4ptgU5a2VOMcbyQ4FRNQPkr-0BnIpV129S33EcTtI76vipQah_C4IzEihKFqZOq_e_BSUZUzw5nyKHVHgs5W0l_JF2DQSThElX2jpwl5Hu_B5id_npnenOp5Hv_W63hQ9GzmaX8hjfhPZ6lwNJt71EuOS3pjsT2ubGVd9TbsWxb7RvDEfI8md1s1LBhJYJc5QA72yJKBzITEeYZuH8V9E3UkXAjENmYlTLVI6cdR67l5ELR4MwGI6wSd3FAxQeirKRkZg0waxFObmbJCBDskiVO9x_571XCX-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 312K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 18:02:50</div>
<hr>

<div class="tg-post" id="msg-14322">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نتانیاهو خطاب به اردوغان: به من درس اخلاق نده!
نتانیاهو مدعی شد: «اردوغان، دیکتاتور یهودستیز که مرتکب نسل‌کشی علیه کردها می‌شود، از سازمان تروریستی حماس حمایت می‌کند، مردم خود را سرکوب می‌کند و مخالفان سیاسی خود را زندانی می‌کند، او آخرین کسی است که می‌تواند به دولت اسرائیل درس اخلاق بدهد.»
@withyashar</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/withyashar/14322" target="_blank">📅 17:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14321">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ساعت 01:59 به وقت جهانی (UTC)، یک بمب‌افکن B-52H متعلق به نیروی هوایی آمریکا در حال پرواز بود.   این هواپیما از پایگاه ماینوت در آمریکا حرکت کرده و به سمت پایگاه هوایی فِیرفورد در بریتانیا می‌رود.   این پایگاه یکی از مراکز مهم برای استقرار بمب‌افکن‌های راهبردی…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/withyashar/14321" target="_blank">📅 17:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14320">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نتانیاهو رسما نامزد انتخابات آتی اسرائیل شد
@withyashar</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/withyashar/14320" target="_blank">📅 17:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14319">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مقامی آگاه گفت : ترامپ رسما در یک تلفن با شریف نخست وزیر پاکستان و بن حمد امیر قطر، پایان مذاکرات با تهران را اعلام کرد.
@withyashar</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/withyashar/14319" target="_blank">📅 17:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14318">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارش صدای انفجار‌ از محدوده سوهانک / دارآباد تهران
🚨
@withyashar</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/withyashar/14318" target="_blank">📅 17:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14317">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یورو نیوز : در جریان یک رزمایش، تایوان یک موشک‌ آمریکایی به سمت چین شلیک کرد
ارتش تایوان امروز چهارشنبه دهم ژوئن (۲۰ خرداد ۱۴۰۵) در جریان یک رزمایش نظامی، با استفاده از پرتابگرهای سیار موشکی «شلیک و گریز»، به سمت چین راکت‌‌هایی شلیک کرد. این تمرین نشان می‌دهد که تایوان در صورت حمله احتمالی چین چکونه از خود دفاع خواهد کرد.
@withyashar
خوب اینام شروع کنن تیم تکمیله
🤣</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/14317" target="_blank">📅 16:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14316">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت: تهران مذاکرات صلح را به تعویق انداخت که در نهایت منجر به پیشرفت بسیار محدودی شد‌‌
@withyashar</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/withyashar/14316" target="_blank">📅 16:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14315">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">صدای انفجار در کویت
🚨
@withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/14315" target="_blank">📅 16:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14314">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نتانیاهو: اسرائیل به شدت علیه ایران و نمایندگانش که خاورمیانه و جهان را تهدید می‌کنند، به فعالیت خود ادامه خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/14314" target="_blank">📅 16:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14313">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فاکس نیوز به نقل از یک دیپلمات آگاه:
پس از رایزنی با ایالات متحده، مذاکره‌کنندگان قطری امروز صبح برای دیدار با ایرانی‌ها به تهران سفر کردن تا در تلاشی برای رفع اختلافات باقی‌مانده در فرآیند مذاکره باشن.
@withyashar</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/14313" target="_blank">📅 16:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14312">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ در گفتگو با فاکس نیوز: بالگرد آپاچی AH-64 ارتش ایالات متحده که اوایل این هفته سقوط کرد، توسط یک پهپاد که بین دو خلبان خورده بود، مورد اصابت قرار گرفت.
با وجود آتش گرفتن و ایجاد گرمای شدید، پهپاد منفجر نشد و به خلبانان اجازه داد تا در دریا فرود اضطراری داشته باشند.
خدمه حدود دو ساعت بعد توسط یک شناور سطحی بدون سرنشین نیروی دریایی ایالات متحده نجات یافتند.
ترامپ زنده ماندن خلبانان را یک "معجزه" توصیف کرد
@withyashar</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/14312" target="_blank">📅 15:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14311">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">معاون وزیر ارتباطات از بازگشت ۷۸ درصدی ترافیک اینترنت به شرایط پیش از محدودیت‌ها خبر داد و ابراز امیدواری کرد حداکثر طی دو هفته آینده وضعیت به طور کامل عادی شود. وی همچنین شایعه اعمال فیلترینگ جدید را تکذیب کرد
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/14311" target="_blank">📅 15:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14310">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ به فاکس نیوز : فرصت اینو داشتند توافق رو امضا کنند و زنده بمونن
@withyashar</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/14310" target="_blank">📅 15:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14309">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ به کانال ۱۳ اسرائیل:احتمال واقعی وجود دارد که جنگ جدیدی علیه ایران آغاز کنم
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/14309" target="_blank">📅 15:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14308">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">معاون عراقچی به الجزیره: سرنگونی هلی کوپتر آمریکایی عمدی نبوده است
@withyashar
🤣</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/14308" target="_blank">📅 15:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14307">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تحلیلگر عرب:با درگیری‌های دیشب و چند روز پیش آمریکا و اسرائیل به اطمینان رسیدن که قدرت نظامی ایران به مقدار خیلی زیادی نابود شده و این یکی از دلایل برای شروع مجدد جنگ گسترده.
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/14307" target="_blank">📅 15:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14306">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارش صدای انفجار‌ از محدوده سوهانک / دارآباد تهران
🚨
@withyashar</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/14306" target="_blank">📅 15:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14305">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNmu4caTNwMw20j9Is1T4bGT2e-hH2fhL6oSU7aKN6PGyfIpfRwCuiuO4JSY2AhtUTapBP6nUUEmxZYXSwWUXkTMCoJrg3M2hMMxPbo4Itvz01i_d21yB4EHdsMmWDxYoaO4bnBVLNQsOhxXXMCJ99KfF5gkZKizymFZRgYYSIM6O9KaBfVkRGEy7KggYx98-1WoET3oaIpuhUJG2lofqrPRQx5z0CWP4joHA22Olx1KLwWsXSXaeUwGPFVHg6Nq_iNM2EJOIFlC_eFwpNqNHo0a8_CzmDLxHxQSU4asQkyKdzXDXWRKsdwvdskTV2T8SY-pR5-BSh-uAG6Nz7c9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید:
قلدر خاورمیانه مُرده است!!!
@withyashar</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/14305" target="_blank">📅 15:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14304">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ: حملات بیشتر آمریکا به ایران، یک گزینه واقع بینانه است.
@withyashar</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/14304" target="_blank">📅 15:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14303">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/951e923604.mp4?token=pB0uCy-Wla4AzgUYaa2OYLwXWk1lJ8kikJnhLtM_YjZ-TElWq9U9_U9wFJTtr1hqYLZhBabfnoy4Wv1lp8xLs6UDliyu5-zZRfLc1k-psAUaFKVWdeayOCygZipF7PxXtX-82msG27-vKnCgV5gkZ9YsBtFzfjmtBcmqT_AHqra9KTU6sCHgnXUn2ySvC4vdAYTgpR2mJ2BuuyKZ0eb5bioZq6UB5g3Ibeorz7C7EWtNoc-2r6TTLiFWnsTZhXYiWu7dUKJTodNMci5xQidl2mhPLnKg2sSDQjDy5kJLseHzAM5OA3aFSo4vrbadQfuLpBz2ktZgSkU4vVEoz_D3zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/951e923604.mp4?token=pB0uCy-Wla4AzgUYaa2OYLwXWk1lJ8kikJnhLtM_YjZ-TElWq9U9_U9wFJTtr1hqYLZhBabfnoy4Wv1lp8xLs6UDliyu5-zZRfLc1k-psAUaFKVWdeayOCygZipF7PxXtX-82msG27-vKnCgV5gkZ9YsBtFzfjmtBcmqT_AHqra9KTU6sCHgnXUn2ySvC4vdAYTgpR2mJ2BuuyKZ0eb5bioZq6UB5g3Ibeorz7C7EWtNoc-2r6TTLiFWnsTZhXYiWu7dUKJTodNMci5xQidl2mhPLnKg2sSDQjDy5kJLseHzAM5OA3aFSo4vrbadQfuLpBz2ktZgSkU4vVEoz_D3zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل نان استاپ داره لبنان رو میزنه، یه خودرو رو هم با پهپاد نقطه‌زنی کرده، هدفمند.
@withyashar</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/14303" target="_blank">📅 15:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14302">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ: در آتش بس 55 درصد از آنچه که ایران درحال بازسازی آن بود را ویران کردم هنوز با ایران کار دارم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/withyashar/14302" target="_blank">📅 15:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14301">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یک منبع مطلع به i24NEWS می‌گوید:   رئیس‌جمهور ترامپ دیشب با نخست‌وزیر نتانیاهو صحبت کرد و او را در جریان حمله احتمالی امشب قرار داد.  این دو همچنین درباره موضوعات دیگری مرتبط با مذاکرات با ایران بحث کردند.  در آمریکا از وضعیت مذاکرات ناامید شده‌اند و صبرشان رو به پایان است.
@withyashar</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/14301" target="_blank">📅 15:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14300">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ این جمله را برای بار دوم دارد می‌گوید: «بلوکاد «حبس دریایی» ما علیه ایران آنقدر موفق است که حتی خدای آنها (الله) هم دارد علیه آنها کار می‌کند و من را تأیید می‌کند، ستایش بر الله باد!» @withyashar</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/14300" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14299">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نتانیاهو: اسرائیل به شدت علیه ایران و نمایندگانش که خاورمیانه و جهان را تهدید می‌کنند، به فعالیت خود ادامه خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/14299" target="_blank">📅 15:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14298">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پست جدیدتر ترامپ: رسانه‌های اخبار جعلی از گزارش میزان اثربخشی محاصره دریایی ایالات متحده، که موفق‌ترین محاصره در تاریخ جنگ دریایی است، خودداری می‌کنند.  هیچ چیز عبور نمی‌کند مگر اینکه ما بخواهیم. این یک دیوار فولادی است! ایران هیچ تجارتی ندارد، به ارتش خود…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/14298" target="_blank">📅 15:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14297">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ: میدونی خیلی وقت کشی میکنن خیلی باعث میشه تصمیم حمله بگیرم
@withyashar</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/14297" target="_blank">📅 15:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14296">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ داره قاهره رو رد میکنه اقا ترمز کن
🤣
🤣</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/14296" target="_blank">📅 15:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14295">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza</strong></div>
<div class="tg-text">ترامپ داره قاهره رو رد میکنه اقا ترمز کن
🤣
🤣</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/14295" target="_blank">📅 15:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14294">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSfzqskpj2iolNA18eom-vIf7VmVAQR9mB5GlR5849QkmEtr7tI1FEIKdHYZd_hM9l6a5r4zieD4O8DlmUVtr4Sg7FbdprRkOgq-jtZ9-gGwEdg969niJjMG9cxchn6sfZ7LP-NMc3tIq7TJAg-PK_Pv0fyxC12fC9bxjc96RQr5o4cifO7d2k39liyw4qC6ZleSZUESOa6GZrhN3mho_845xH7Gkb94oSO0zmGIfx-jOjxnePJLVHSdNNBGrHUJHjnDCjSsKkUIp0YjRdzi3N_BbSGwOIqgjCzfV9R9YaYCy7wNCBsMZ0ROZPcXsRR4Qx8TaOuPPVI4GKx9bVvQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدیدتر ترامپ:
رسانه‌های اخبار جعلی از گزارش میزان اثربخشی محاصره دریایی ایالات متحده، که موفق‌ترین محاصره در تاریخ جنگ دریایی است، خودداری می‌کنند.
هیچ چیز عبور نمی‌کند مگر اینکه ما بخواهیم. این یک دیوار فولادی است! ایران هیچ تجارتی ندارد، به ارتش خود یا هیچ یک از صورتحساب‌هایش پرداخت نمی‌کند و به سرعت به یک ملت شکست خورده تبدیل می‌شود! نفت زیادی در حال خروج است.
الله  را شکر !
@withyashar</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/14294" target="_blank">📅 15:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14293">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فاکس نیوز: ترامپ در حال مشورت با مشاوران خود برای بازگشت به جنگ با ایران است و گزینه حملات به نیروگاه‌ها و پل‌های ایران را بررسی می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/14293" target="_blank">📅 15:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14292">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قالیباف: با وجود شهادت فرماندهان و دانشمندان در جنگ ۱۲ روزه، نه حرکت علم و دانش در کشور متوقف شد و نه توان دفاعی و بازدارندگی ایران کاهش یافت
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/14292" target="_blank">📅 15:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14291">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ : ما کارمون با ایران رو ادامه می‌دیم و جلو می‌ریم
@withyashar</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/14291" target="_blank">📅 15:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14290">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ به فاکس : به صدور دستور برای حمله‌های جدید به نیروگاه‌ها و پل‌های ایران نزدیک شده‌ام
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/14290" target="_blank">📅 15:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14289">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وزیر فرهنگ اسرائیل:
دیکتاتور اردوغان که دستانش آغشته به خون است باید درباره جنایاتش پاسخگو باشد و به تنها کشور دموکراتیک در خاورمیانه موعظه نکند. اگر جرات کند ما را امتحان کند - سرنوشتش بدتر از رژیم رو به زوال ایران خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/14289" target="_blank">📅 14:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14288">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قالیباف، رئیس مجلس ایران :
توان دفاعی و بازدارندگی ایران همچنان پابرجاست و آسیبی به اون وارد نشده
@withyashar</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/14288" target="_blank">📅 14:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14287">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نتانیاهو بعد توییت ترامپ: ایران نباید سلاح هسته ای داشته باشه.
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/14287" target="_blank">📅 14:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14286">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jc_f2axDfd9LC9OIUneTsGETXI3AuJA3fw4bQiCAIZUfAGUEh2qxsXIeO6uvO1Otl5egDBiQzbMHEF5OyO6FOW_9sU23EiY3rpMBo1RMP_WurDaZ3AJo1rcAX10K67TB3uDXJt71G85wCkBSnCAGAV5Cc2yDlbZMDu3L7SgIbTGTSHcilhCAFNBXwMu3EIkRov7l4ZdYgou_HfVEuQyBZgPhqA6y4uGrmTreB_CsLRvtRfjZ50Esm4AaO9NklVlSjTkCViMZM4R6a0N-U6zSZlJDfNF6Aqdj57EG_VQtJGMJs-nX38DKy0AMbEc8DLIlxwnkxQ5rDxW7jE6JIqMUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:  ارتش ایران کاملاً از هم پاشیده و نابود شده. بخش بزرگی از توان نظامی ایران، از جمله نیروی دریایی و نیروی هوایی، عملاً دیگه وجود نداره. ایران به طور کامل شکست خورده. ایران فقط حرف می‌زنه و کاری انجام نمی‌ده. قلدر خاورمیانه مُرده! خیلی بیشتر از حد لازم برای مذاکره روی توافقی که می‌تونست به نفعشون باشه وقت تلف کردن و حالا باید بهای این کار رو پرداخت کنن
@withyashar</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/14286" target="_blank">📅 14:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14285">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سناتور لیندزی گراهام در رقابت با بازرگان مارک لینچ، در انتخابات مقدماتی سنای جمهوری‌خواهان کارولینای جنوبی پیروز شد.
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/14285" target="_blank">📅 14:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14284">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43d918eef.mp4?token=QZwIdqIa7DoHgV6uotSI1wf0xXXjVfxgOrBn7T_wukdnwD_W5RStFOGMdxYHDfChI6FqbXYhFcHFNOjJd4VGTk3Res3KEY4hY2v32yMBSAAL8smt4TFoLglTpKqPgoAt1c4LMTDwaILT3paydKnAlXSeRPsyHZnuSijYdoqevjEVVUqs4uj8_cD-IIK_F_a0twDx-spKz9yoptCGJkqW6Pu09FzRI06GERcDyvH_u5S1XP0VbERFNTc54-qxtrlLLu9rPd0jIe7oTzTS_ZhLjYQB5l4T-yeYT4K6bUA1BDScOLMMlJdHN0WS9nr2zD2jVfZQypjhP41KR3E_SXtf3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43d918eef.mp4?token=QZwIdqIa7DoHgV6uotSI1wf0xXXjVfxgOrBn7T_wukdnwD_W5RStFOGMdxYHDfChI6FqbXYhFcHFNOjJd4VGTk3Res3KEY4hY2v32yMBSAAL8smt4TFoLglTpKqPgoAt1c4LMTDwaILT3paydKnAlXSeRPsyHZnuSijYdoqevjEVVUqs4uj8_cD-IIK_F_a0twDx-spKz9yoptCGJkqW6Pu09FzRI06GERcDyvH_u5S1XP0VbERFNTc54-qxtrlLLu9rPd0jIe7oTzTS_ZhLjYQB5l4T-yeYT4K6bUA1BDScOLMMlJdHN0WS9nr2zD2jVfZQypjhP41KR3E_SXtf3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان: ما کاملاً آگاهیم که هدف نهایی توهم «اسرائیل بزرگ» چیست.
ان‌شاءالله هرگز اجازه نخواهیم داد.
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/14284" target="_blank">📅 13:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14283">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ایران می‌گوید دیپلماسی با ایالات متحده به دلیل این حملات تضعیف شده است.
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/14283" target="_blank">📅 13:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14282">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اردوغان درباره رئیس جمهور آمریکا، ترامپ: «شرکت او در اجلاس ناتو در آنکارا برای وحدت اتحادها مهم است»
@withyashar
یاشار : امیدوارم ترامپ به این اجلاس نره ! جدا از تمام مسائل مذاکرات، می‌تواند به آخرین تیر ترکش جمهوری اسلامی برای به خطر انداختن جانش هم تمام شود.</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/14282" target="_blank">📅 13:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14281">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO): گزارشی از یک حادثه در فاصله ۲۰ مایل دریایی شمال‌شرق صحار در عمان دریافت کرده است. در پی آتش‌سوزی در اتاق موتور یک نفتکش، یک نفر زخمی و دو نفر از خدمه مفقود شده‌اند؛ این نهاد، هیچ‌گونه آلودگی زیست‌محیطی گزارش نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/14281" target="_blank">📅 13:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14280">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یونی بن مناخیم، تحلیلگر ارشد مرکز اورشلیم، به کانال ۱۴ گفت که ایران سیستم‌های دفاع هوایی که چند هفته پیش توسط ایالات متحده و اسرائیل نابود شده بود را بازسازی کرده بود. بهبودی با این سرعت بدون کمک مستقیم چین امکان‌پذیر نبود.
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/14280" target="_blank">📅 12:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14279">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هم اکنون صدای انفجار‌ در‌ سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/14279" target="_blank">📅 12:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14278">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8515c2be09.mp4?token=eWgqJfvjOr9nzMBajNbMWw_hcRN4cGl-uzY50qGERrHB6fbP6hOlGc6MdKdwR97AOaO9Fdip4e_RkIKZBttjyZtqwIpR5CCXHfbjoVrJra8ON1MTcIN73a9P4jhS4nzE4BWBKEQpIlofHD-Xp327ZTbV7IEn4G3AEU7JGl-RV2NHCVwsabgDHc_dtkinPVNncprw51ED57szfYN5gC1CGV5DvTrYXhPoyN8rz_S9quATzCtbRTrQVwlJvsvtiKIjlfy9PxhuF5AyEgNpg6lLUd53US8PYH5DKxn4BeR4aXzEu4cmLCBzDuGsNbBMMmsRYSvPO2PnD6w5aCOJlagULbIEDZThnjmUVmM2n1xwm-aK_LizXQy3DDQOHWdQk_BGOzMciG-JoRNX73RooKu-5plsUHgu-YBx3qR8nkWbjc2ouzbmTxhzHGAElg9TRLU7vyau3VI4mEEM8ksra2HgBsgw4gNwdbD5GbBSGnhslkSTG42NxxRp9dhh4IwMH720NSVYC6uqTMqP2W4Y40uacOe0c9RKAKyUp-xrTYUUhMBcEzqmtuCeQ_Rh7kbfOkoMYjfvaJxo3Nq-9C_ceczOEot8aX_-oGH008U5zQuZ7jJr8IidZQYGyaHJltiaPh-x1LS-M9WmeNOp3BaVKTNpu-1jV3x1N-BcfE80D1Tirh0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8515c2be09.mp4?token=eWgqJfvjOr9nzMBajNbMWw_hcRN4cGl-uzY50qGERrHB6fbP6hOlGc6MdKdwR97AOaO9Fdip4e_RkIKZBttjyZtqwIpR5CCXHfbjoVrJra8ON1MTcIN73a9P4jhS4nzE4BWBKEQpIlofHD-Xp327ZTbV7IEn4G3AEU7JGl-RV2NHCVwsabgDHc_dtkinPVNncprw51ED57szfYN5gC1CGV5DvTrYXhPoyN8rz_S9quATzCtbRTrQVwlJvsvtiKIjlfy9PxhuF5AyEgNpg6lLUd53US8PYH5DKxn4BeR4aXzEu4cmLCBzDuGsNbBMMmsRYSvPO2PnD6w5aCOJlagULbIEDZThnjmUVmM2n1xwm-aK_LizXQy3DDQOHWdQk_BGOzMciG-JoRNX73RooKu-5plsUHgu-YBx3qR8nkWbjc2ouzbmTxhzHGAElg9TRLU7vyau3VI4mEEM8ksra2HgBsgw4gNwdbD5GbBSGnhslkSTG42NxxRp9dhh4IwMH720NSVYC6uqTMqP2W4Y40uacOe0c9RKAKyUp-xrTYUUhMBcEzqmtuCeQ_Rh7kbfOkoMYjfvaJxo3Nq-9C_ceczOEot8aX_-oGH008U5zQuZ7jJr8IidZQYGyaHJltiaPh-x1LS-M9WmeNOp3BaVKTNpu-1jV3x1N-BcfE80D1Tirh0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar
b52</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/14278" target="_blank">📅 12:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14277">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3cea3e4e8.mp4?token=deknCaN2jqHR-i2mtVvhACwBVRpsYOXAY3jlnwuJ3IqwH85mPoODb_dWqTPvNcwDTM0BjP2CTGxj5UkVzXnuQIXB-jHfATSkWFdGVba5NjtA50T1_uR_kSXA1BPcaiA56MPqS1Pa24cXsGt8kq7w3ktuPIagUFMQRaLQ_8XX5RUjwSsrUs0_Gsm59ht8nyS8h8BVoDu-CjG4mescqepPoe2w8hP1HSEjIQq7O12A3ojCALkjaXGojkpGTdFeKwq9qIRsh5FJEl8HbuPN42Qfj0vd-Y0cdDFOEdCruXMyPYpPjK9K1lihcED06q4lLr00-VqDS-EMy4Z0D2gg1mDjdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3cea3e4e8.mp4?token=deknCaN2jqHR-i2mtVvhACwBVRpsYOXAY3jlnwuJ3IqwH85mPoODb_dWqTPvNcwDTM0BjP2CTGxj5UkVzXnuQIXB-jHfATSkWFdGVba5NjtA50T1_uR_kSXA1BPcaiA56MPqS1Pa24cXsGt8kq7w3ktuPIagUFMQRaLQ_8XX5RUjwSsrUs0_Gsm59ht8nyS8h8BVoDu-CjG4mescqepPoe2w8hP1HSEjIQq7O12A3ojCALkjaXGojkpGTdFeKwq9qIRsh5FJEl8HbuPN42Qfj0vd-Y0cdDFOEdCruXMyPYpPjK9K1lihcED06q4lLr00-VqDS-EMy4Z0D2gg1mDjdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعت 01:59 به وقت جهانی (UTC)، یک بمب‌افکن B-52H متعلق به نیروی هوایی آمریکا در حال پرواز بود.
این هواپیما از پایگاه ماینوت در آمریکا حرکت کرده و به سمت پایگاه هوایی فِیرفورد در بریتانیا می‌رود.
این پایگاه یکی از مراکز مهم برای استقرار بمب‌افکن‌های راهبردی آمریکاست در میانه حمله و در عملیات‌های مرتبط با ایران نیز مورد استفاده قرار گرفت.  نام ارتباطی این پرواز THIRD51 است.  خلبان در مسیر، موقعیت هواپیما را از طریق رادیو به مرکز کنترل بر فراز اقیانوس اطلس گزارش داده است.  بعد از عبور از یک نقطه مشخص، به او گفته شده با برج کنترل شانون در ایرلند روی یک فرکانس جدید تماس بگیرد.
@withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/14277" target="_blank">📅 12:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14276">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کانال ۱۴ اسرائیل فاش کرد:
طبق جزئیات فاش شده از مذاکرات، دولت ترامپ در حال انجام مذاکرات محرمانه پیشرفته با تهران در مورد یک توافق هسته‌ای جدید است که برای متوقف کردن برنامه تسلیحاتی ایران به مدت تقریباً ۱۵ سال طراحی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/14276" target="_blank">📅 11:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14275">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53b13459f9.mp4?token=NgevF9hkA7n35fsdQDJx4qpm3HnAr67OhzHYJDE3aE5BFGD6rJYAYVehoOPEhAeqIjQYKkG7Zf_vYri-YRbtuUpoarSZEC9FhCFr0T_LnHgJdb10-vhFM-T2N7MfhXyDNeAVbU_Fhzcesxi4oNL3tjpxBM2wSreoW_9j-xUo6oHY0n2xHSCGgPkXXSWc_PpUaqkZediU175s74mhT52sX0BMK4YRtRXlBBRgBbUyq35-S-gDzgviZo4k704xA4XztJv_O7Agw1zQ16YoJ7R1xj3UNVfieGyHypUS4mJgB7brPXjvAJhM6ak7m_m9dn-YrcDI7i3WLa2VNpbW74RQpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53b13459f9.mp4?token=NgevF9hkA7n35fsdQDJx4qpm3HnAr67OhzHYJDE3aE5BFGD6rJYAYVehoOPEhAeqIjQYKkG7Zf_vYri-YRbtuUpoarSZEC9FhCFr0T_LnHgJdb10-vhFM-T2N7MfhXyDNeAVbU_Fhzcesxi4oNL3tjpxBM2wSreoW_9j-xUo6oHY0n2xHSCGgPkXXSWc_PpUaqkZediU175s74mhT52sX0BMK4YRtRXlBBRgBbUyq35-S-gDzgviZo4k704xA4XztJv_O7Agw1zQ16YoJ7R1xj3UNVfieGyHypUS4mJgB7brPXjvAJhM6ak7m_m9dn-YrcDI7i3WLa2VNpbW74RQpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاکستان تصاویر هدف قرار دادن اردوگاه‌های تحریک طالبان پاکستان در کنر، پکتیکا و خوست در افغانستان را منتشر کرد.
این هدف‌گیری به وضوح نشان می‌دهد که این سازه توسط بمب‌های هدایت‌شونده لیزری مورد اصابت قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/14275" target="_blank">📅 11:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14274">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کانال 13 اسرائیل: ارتش اسرائیل توصیه کرده در پاسخ به هرگونه شلیک به سمت اسرائیل، حملات گسترده و شدیدی علیه بیروت انجام شود.
@withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/14274" target="_blank">📅 11:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14273">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اتاق جنگ با یاشار : خبر ۳ میلیارد دلار خبر فیک با منبع رسانه داخلیه خودش هم گفته باز به نقل از یک مقام سپاهی!!!! @withyashar اون پرواز هم چک کردم رفته پرسنل رو تخلیه کنه !</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/14273" target="_blank">📅 11:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14271">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گزارشها از صدای انفجار هم اکنون در قشم
@withyashar</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/14271" target="_blank">📅 11:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14270">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCTuXEJGS-SDf_F1Pv0PP7enj1Ct4rRFK2MT0sDwm4P4DnAv9VEBslpq-UhuwSOtGJwwDwUF8qaWwLnivWFrrmuEXfx-B3rst48SvJZGUzsAE3nSfz6H2vtGkgoZEwcT6cwMviNOOXikDm1BgC65-cRDaY6oCf72pZ5tha7RKwyfHQnuqVZi_yHAsNaA0132qJq2YNTdxPqGJK8tfd2KNxev7z6yXwOWFqicWnq6dIStWk0hy35GrJThZoj64FbWAOe071Imdf8NUtzRKFh6e4v29CBnsvejNuepszUFEd0zflPPr3dB7s77DT2jbeNnBnTsZ1tz-EmC0r0YhoglJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از کشف تجهیزات جاسوسی برای پشتیبانی هدایت جنگنده‌ها در لواسان
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/14270" target="_blank">📅 11:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14269">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">صحنه‌ای از پرتاب حداقل ۱۱ فروند موشک سوخت‌جامد بردبلند علیه اهداف آمریکا در منطقه طی حملات موشکی صبح امروز @withyashar</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/14269" target="_blank">📅 10:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14268">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e315ffa564.mp4?token=qSMCvkgUXRqXHnTojR4bTDCFCb414kHEX_LbaPOli34uCFM5bcMWtdsGnm_C6QuPT1-XcH82onUnPlk9g0mBGFlVJn-0wlqHRNtfynkW-U1eCrhlc1W7-eTYisCMv8KmJkrYb_yLnVTPqtIdA37gN-WP032N0IHFBnw5Gtaqy3IqEIzyOkFFo18aPU1NI8on5lCSv55Y3d3dW-hFnb7AZt0mW2n-ktqf0I5s48USW7vTZSZeAdm0Vn5XP_QeXcOYHqVGjoZoy3BNCV-8CdtnbVk1J-PL_oG4HKH-hMLcamyABL4BrwvieoBnqQD8OoCU86drcQ55LPi2v07uuscEyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e315ffa564.mp4?token=qSMCvkgUXRqXHnTojR4bTDCFCb414kHEX_LbaPOli34uCFM5bcMWtdsGnm_C6QuPT1-XcH82onUnPlk9g0mBGFlVJn-0wlqHRNtfynkW-U1eCrhlc1W7-eTYisCMv8KmJkrYb_yLnVTPqtIdA37gN-WP032N0IHFBnw5Gtaqy3IqEIzyOkFFo18aPU1NI8on5lCSv55Y3d3dW-hFnb7AZt0mW2n-ktqf0I5s48USW7vTZSZeAdm0Vn5XP_QeXcOYHqVGjoZoy3BNCV-8CdtnbVk1J-PL_oG4HKH-hMLcamyABL4BrwvieoBnqQD8OoCU86drcQ55LPi2v07uuscEyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحنه‌ای از پرتاب حداقل ۱۱ فروند موشک سوخت‌جامد بردبلند علیه اهداف آمریکا در منطقه طی حملات موشکی صبح امروز
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/14268" target="_blank">📅 10:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14267">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeHD1LRQvuAR2MRav7tJe2GRMrkvq-jBXKxPpiiOTcBa_Mwy-8JyCb6IJyONwkIhnTGKb7pRTSJpXvEzA_wkP_6rUOg21Gl0TVUBpWiLJcPYsxi8JSjeh0YV_G-Dry-VSM5PHixwMgjWHmyuYYhx1VuWLOQRdRQlOxmVlqOhA7YPH-r-YBDzz5wP9W23UIHSP0-XqheSORjTSHAsPHCN4X0VgaYhWERPWwAuASmK3bvo94pXySNZUDbuZpNzbCBYtQeHms02RxelUecj7E3REAOGJLWqVyiBZmdXa4qdqcmt4_UKdWaZSc_W7x8JSrsAOqbAcZgp1kBdQyVXx9XhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو خمین دم صبح موشک اومدن ول بدن برگشته پایین
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14267" target="_blank">📅 10:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14266">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هشدار مسکو به تهران:
صلح، پوشش حمله زمینی است، نقشه پنتاگون برای پایان آتش‌بس دوهفته‌ای
شورای امنیت روسیه در بیانیه‌ای تکان‌دهنده که توسط خبرگزاری «تاس» منتشر شد، هشدار داد آمریکا و اسرائیل از پوشش دیپلماسی و مذاکرات صلح برای آماده‌سازی یک عملیات زمینی گسترده علیه ایران استفاده می‌کنن
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/14266" target="_blank">📅 10:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14265">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سازمان دریانوردی بریتانیا:یک کشتی تجاری گزارش داده که در جنوب غربی بندر بلحاف یمن، یک قایق کوچک حامل ۶ فرد مسلح به آن نزدیک شده است.
به گفته این سازمان، بین قایق مسلح و تیم حفاظت مسلح کشتی تبادل تیراندازی رخ داده و در نهایت قایق از محل دور شده است.
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/14265" target="_blank">📅 10:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14264">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">روزنامه همشهری: خوشبین نباشید، ترامپ از این جنگ دست برنمی دارد
روزنامه همشهری: واقعیت این است که دعوا بر سر چند درصد غنی‌سازی نیست، دعوا بر سر نظم منطقه است؛ بر سر این است که چه‌کسی گلوگاه‌های راهبردی جهان را کنترل کند و چه‌کسی موازنه قدرت آینده را شکل دهد.
برای همین شاید آتش‌بس باشد، شاید وقفه باشد، شاید جابه‌جایی تاکتیک‌ها را ببینیم‌ اما تصور اینکه این کشمکش با چند توافق فنی برای همیشه خاموش شود، خوش‌بینانه است.
@withyashar</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/14264" target="_blank">📅 09:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14263">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حمله سنگین اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/14263" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14262">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pD3J0zeOxO9u1qJJWncnUgVxpcovERYMWEIp2srmS-vCZ8vJ0E6wfE2zROuQrY9P6vlSUkcsq0B_krCjHdt4KPz5iflPZgbQQ-cHD7upWrV_u-jSMmsxKGeCSYi-jOJonmssyZFDAvZEDZ3MCbgLyYH4MgUPXhpA07UDdTZVyxGqjs-rCZt8bPVfwz9T_2gXRE6VZp9uKgfOftd3MwJXnbqvhns13RwbOVPKZSWFV1l1fW7gRQo_hfmJPZOehzEtAqLrXUk3K_E1V8yG3ZuMISoyVTfRkqfAqNyT9RdCVmx_Yw9pHeTn553t5G0mtPBYeB-oiI8CX4r4gsBw1td4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پالایشگاه نفت سامارا روسیه پس از اصابت پهپاد‌های اوکراینی
@withyashar</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/14262" target="_blank">📅 09:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14261">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سخنگوی طالبان:
دیشب ارتش پاکستان حریم هوایی افغانستان رو نقض کرد و چند خونه مسکونی رو در ولایت‌های کنر، خوست و پکتیکا بمباران کرد.
تو این حملات 11 کودک، یک زن و یک مرد سالمند کشته شدن و 14 نفر دیگه زخمی شدن.
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/14261" target="_blank">📅 09:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14260">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">۳پا پاسداران: به دنبال عملیات موفق نیروی دریایی سپاه در اصابت قرار دادن 21 هدف در پایگاه‌های هوایی و دریایی آمریکا در منطقه و ساقط کردن یک فروند پهپاد MQ9 در آسمان شهرستان جم، با توجه به تداوم شرارت‌های دشمن، 4 هدف از جمله آشیانه‌های جنگنده‌های F-35 در پایگاه…</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/14260" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14259">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">۳پا پاسداران:
به دنبال عملیات موفق نیروی دریایی سپاه در اصابت قرار دادن 21 هدف در پایگاه‌های هوایی و دریایی آمریکا در منطقه و ساقط کردن یک فروند پهپاد MQ9 در آسمان شهرستان جم، با توجه به تداوم شرارت‌های دشمن، 4 هدف از جمله آشیانه‌های جنگنده‌های F-35 در پایگاه هوایی ارتش آمریکا در الازرق اردن رو مورد هدف و انهدام قرار دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14259" target="_blank">📅 09:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14258">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خبرنگار وای نت:
در چند ساعت اخیر در رویدادی جالب سامانه‌های پدافندی آمریکا تمامی موشک‌های شلیک شده به 3 کشور مختلف رو رهگیری کردن. صفر اصابت و شاهکار پاتریوت!
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14258" target="_blank">📅 09:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14257">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از مقام‌های آمریکایی نوشت: ترامپ تمایلی به حمله به ایران نداشت، اما پس از توصیه وزیر دفاع و رئیس ستاد مشرک، نظرش را تغییر داد
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14257" target="_blank">📅 09:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14256">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نیروهای مسلح اردن: پنج فروند موشک ایرانی که به سوی پایگاه الازرق شلیک شده بودند را رهگیری و سرنگون کردیم. در پی سقوط بقایای موشک‌های رهگیری‌شده، هیچ‌گونه خسارت یا جراحتی ثبت نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/14256" target="_blank">📅 09:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14255">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">https://t.me/boost/withyashar
۳۹۰ بوست پرمیوم هاااا</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14255" target="_blank">📅 03:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14254">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">۴ انفجار‌شدید بندر عباس
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14254" target="_blank">📅 03:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14253">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هم اکنون انفجار سنگین سیریک و اطراف را لرزاند
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14253" target="_blank">📅 03:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14252">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حملات جدید به بندر عباس و سیریک
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14252" target="_blank">📅 03:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14251">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش انفجار در قشم
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14251" target="_blank">📅 02:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14250">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کانال 12 اسرائیل: در موج دوم حمله‌ها به ایران، آمریکا داره پدافندهای هوایی و رادارها رو هم هدف حمله قرار میده.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14250" target="_blank">📅 02:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14249">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxOd1_FO5uO0P5qnK4_FWbf_o8D2Q7W1bBu4J3lwVXgYTlTfzf_t1YMsXyIx49fKsiBlwJv5yzjU6d-csJzp1WEvpXuccUc3WwtQR2O4HLbEjHPfAgKCRXtmzydqHIzBXBTwtne4uDZsydirn3erqwHnfQFYh0C67zqPm4sfC6KTpE0BXClbRq1f1-zXxVruNkJ8gjLZ4PRe_GfzCStxTsKBbnL2FFP-INayJgJAczN5AxVlDoAglrdD6m7IaHjIEozmtuha3JLrEIZQRwpmDSX1k43Wjwu7Fn3ZTJusBRsJXdGA-LqNS8cJkp288B0UvW3pt2fSrLWHNmF7xZwAIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس نیوز : بر اساس اعلام مقامات نیروی دریایی آمریکا، نزدیک به ۲۰ هزار ملوان و تفنگدار دریایی آمریکایی در حال حاضر در دریا و مستقر بر روی دو ناو هواپیمابر «یواس‌اس آبراهام لینکلن» و «یواس‌اس جرج اچ. دابلیو. بوش» هستند؛ به‌همراه ۱۸ ناوشکن مجهز به موشک‌های هدایت‌شونده، یگان اعزامی سی‌ویکم تفنگداران دریایی، و بیش از دوازده اسکادران هوایی.
این تجهیزات و نیروها در مناطق مختلفی از جمله شرق مدیترانه، دریای سرخ، شمال دریای عرب و دریای عرب پراکنده شده‌اند؛ جایی که نیروهای آمریکایی در حال کمک به دفاع از اسرائیل، مقابله با تهدیدات حوثی‌ها، انجام عملیات مرتبط با ایران، و حمایت از امنیت دریانوردی در اطراف تنگه هرمز هستند.
این نیروی دریایی بخشی از حدود ۵۰ هزار نیروی نظامی آمریکاست که در حال حاضر در سراسر خاورمیانه مستقر هستند.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14249" target="_blank">📅 02:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14248">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دو دقیقه پیش سه انفجار از اسکله جاسک @withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14248" target="_blank">📅 02:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14247">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14247" target="_blank">📅 02:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14246">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14246" target="_blank">📅 02:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14245">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دو دقیقه پیش سه انفجار از اسکله جاسک
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14245" target="_blank">📅 02:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14244">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فارس جوگیر شد و گزارش کرد :
گروه هکری حنظله: مختصات تمام نیروهای نظامی تروریستی آمریکا در کشورهای خلیج‌فارس به سپاه پاسداران انقلاب اسلامی منتقل شد.
به‌زودی به پهپادهای شاهد-۱۳۶ «خوش‌آمد» خواهید گفت.
شما بازی را شروع کردید؛ ما تعیین می‌کنیم چگونه پایان یابد.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14244" target="_blank">📅 02:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14243">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نیویورک تایمز گزارش می‌دهد که حملات هوایی آمریکا به پایگاه‌های نظامی و دریایی، تأسیسات راداری و باتری‌های موشکی در پنج مکان در سواحل جنوبی ایران، از جمله موارد زیر، هدف قرار گرفته‌اند:
پایگاه‌های دریایی در سیریک و جاسک
سایت‌های دفاع هوایی در بندرعباس
باتری‌های موشکی در قشم۶
برخلاف گزارش صداوسیما مخزن آبی در سیریک هدف نگرفته است و مانند مدرسه میناب رو به دروغ آورند!
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14243" target="_blank">📅 02:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14242">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">جنگ امیر تتلو و زندان
امیر تتلو از پشت تلفن زندان موزیک ضبط کرده و همین الان پخش کرده
https://youtu.be/ixhpdO88-IY?si=dmb7e06_W8ShLkkA
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14242" target="_blank">📅 02:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14241">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرنگار صداسیما در سیریک: در پی حمله امشب دشمن آمریکایی به سیریک، ۲ مخزن آب بخش بمانی مورد اصابت قرار گرفته و آب آشامیدنی این بخش قطع شده است.
@withyashar</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/14241" target="_blank">📅 02:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14240">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اتاق جنگ با یاشار : با خسته شدن و خوابیدن ادمین های تلگرام جنگ هم تمام میشود
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14240" target="_blank">📅 02:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14239">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258b122927.mp4?token=c-jbZLshenpxYQHP3Lxtwd9dJ0tYchX5JKelsHEpnTfOdgdoo6nXmt9xmwUuwBB2s1vqTKc8Fs0j6SFQWeNLqDLQ2VjGalKvxI8Liu6W8cqAbgSgAYdvUmVaunkM1jEtxbaRXKXjZX4cmZNYBZAvkn8b9U1fD9UFYZ0TchI8WJB0tlo4DZ5qvfx6631ewSwLPoL-5GczmEQMAStR3f6TnwOnOIK-AJ34Zx_uNxXtq-QntK7MFk35topR8sjAsOMubNY9d0cwZrFNvFQ9WBiO8_b5Pl3uX62UUM7Fn4ustWC_r6lcELZ8ajpMJmMD6pAe1rkD0btKBdHBe4G4PmZNcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258b122927.mp4?token=c-jbZLshenpxYQHP3Lxtwd9dJ0tYchX5JKelsHEpnTfOdgdoo6nXmt9xmwUuwBB2s1vqTKc8Fs0j6SFQWeNLqDLQ2VjGalKvxI8Liu6W8cqAbgSgAYdvUmVaunkM1jEtxbaRXKXjZX4cmZNYBZAvkn8b9U1fD9UFYZ0TchI8WJB0tlo4DZ5qvfx6631ewSwLPoL-5GczmEQMAStR3f6TnwOnOIK-AJ34Zx_uNxXtq-QntK7MFk35topR8sjAsOMubNY9d0cwZrFNvFQ9WBiO8_b5Pl3uX62UUM7Fn4ustWC_r6lcELZ8ajpMJmMD6pAe1rkD0btKBdHBe4G4PmZNcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعالیت پدافند مشهد امشب.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14239" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14238">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جسی واترز از فاکس درباره مذاکرات ایران:
فکر می‌کنم ما همین الان یک پیشنهاد دریافت کردیم/از واشنگتن می‌شنوم که از آنچه می‌بینیم خوششان آمده است.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14238" target="_blank">📅 02:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14237">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f374eeb00.mp4?token=Jt9-8Ci4kd04pb0lZDwaNtbaFQ3rgxjIql8VBmZBJjiBrfIregFI-9wAv8fNcMSPbZfxrXdlchgKWyd11jAhB6eRciwI_KZOOY_JIeHOkraPX2d9kCmtzQvmDFAm9rhk82PBfawKatCC-sdirgkj-QF3H76CWMdcHjgRuP1eLU42rp4rhbEnsdcGsuinH84KXz5HxODzJi3dhFroaV4rSuw7QOONXdYs8JI3aQfWIYRBnKDudZMBMVG3xIbQm7ONCUtxqv6f4TYM2qTcJRIcnpWkSy0EX6CIh-sFE9VYgnGCheqSBUgBk8ZEs_9vHk4TcWJdZqtWWi_DdhcqeV5liw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f374eeb00.mp4?token=Jt9-8Ci4kd04pb0lZDwaNtbaFQ3rgxjIql8VBmZBJjiBrfIregFI-9wAv8fNcMSPbZfxrXdlchgKWyd11jAhB6eRciwI_KZOOY_JIeHOkraPX2d9kCmtzQvmDFAm9rhk82PBfawKatCC-sdirgkj-QF3H76CWMdcHjgRuP1eLU42rp4rhbEnsdcGsuinH84KXz5HxODzJi3dhFroaV4rSuw7QOONXdYs8JI3aQfWIYRBnKDudZMBMVG3xIbQm7ONCUtxqv6f4TYM2qTcJRIcnpWkSy0EX6CIh-sFE9VYgnGCheqSBUgBk8ZEs_9vHk4TcWJdZqtWWi_DdhcqeV5liw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهده پهپادهای انتحاری‌ ایرانی در آسمان عراق
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14237" target="_blank">📅 01:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14236">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پولیتیکو به نقل از یک مقام ارشد در کاخ سفید: هیچ تغییری در شرایط بوجود نیامده و آتش بس کماکان ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14236" target="_blank">📅 01:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14235">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ولی یه حمله شکی توش‌نیست حمله شما به دایرکت اتاق جنگ
😭
🤣
❤️‍🩹
🙌🏾</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14235" target="_blank">📅 01:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14234">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هم اکنون خاورمیانه:  حملات آمریکا به ایران حملات اسرائیل به لبنان حملات پاکستان به افغانستان حملات ترکیه به عراق حملات ایران به بحرین و کویت  @withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14234" target="_blank">📅 01:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14233">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شلیک دو موشک از سیرجان
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14233" target="_blank">📅 01:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14232">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گزارشات از حملات توپخانه ای عربستان به یمن
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14232" target="_blank">📅 01:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14231">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/14231" target="_blank">📅 01:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14230">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سی ان ان به نقل از مقامات آمریکایی:
انتظار می‌رود چندین دور حملات دیگر بر علیه ایران انجام شود.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14230" target="_blank">📅 01:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14229">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">هم اکنون خاورمیانه:
حملات آمریکا به ایران
حملات اسرائیل به لبنان
حملات پاکستان به افغانستان
حملات ترکیه به عراق
حملات ایران به بحرین و کویت
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14229" target="_blank">📅 01:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14228">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هم اکنون حملات ترکیه به شمال عراق
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14228" target="_blank">📅 01:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14227">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اتاق جنگ با یاشار : خدای من و شما شاهد است که هیچ ردبولی رو بیهوده حروم نکردم
🤣
✌🏾
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/14227" target="_blank">📅 01:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14226">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مقام ارشد آمریکایی به باراک راوید خبرنگار آکسیوس: عملیات ادامه داره و آماده‌ایم برای چندین حمله دیگه.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14226" target="_blank">📅 01:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14225">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گزارش
انفجار در اهواز
.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14225" target="_blank">📅 01:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14224">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یک مقام آمریکایی به سی‌ان‌ان:
حملات جدید به منزله یک شلیک هشدارآمیز به ایران است و ایالات متحده معتقد است این حملات مانع مذاکرات برای پایان دادن به جنگ نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14224" target="_blank">📅 01:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14223">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سید مجید موسی : ‏و ما النصر الا من عند الله العزیز الحکیم
@withyashar
🤣</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14223" target="_blank">📅 01:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14222">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گزارش انفجار در بحرین
@withyashar</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/14222" target="_blank">📅 01:28 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
