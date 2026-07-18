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
<img src="https://cdn4.telesco.pe/file/vS-kkNHI9DG3Yrs2s4hsa-O0rAcaNSeq1CHA2GLdfKSHSzTmzT6A8ZwE6ZszRX_m6LUBUrZI2bbbIUUO5eY8n3ddswL2f6Tp_ocgQ-SvhhpeRHToNdjPWgoR9pHlpH7JMzI5w4XGBVDyA_WM2--ZYVone_GKyNeN85-kioVGCXQYmScaCguBlVkdDEAYcsMG4sM_xpxt3LV8LF2jCSKLI4GB8a0MrEqN3UVcYuMEQx_RI71GPIFI0nC2A2CUmkFgu3oKInHCXFROE7m79mrI7hT5ZOTwFCr4s5CI1xwCg_DjiOeaoKESnqhBxTMCcLUZAZbTo_ZAvGZ0ILLMtBfCOw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 آموزش سئو با محسن طاوسی</h1>
<p>@mohsentavoosiseo • 👥 7.64K عضو</p>
<a href="https://t.me/mohsentavoosiseo" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 من تالیف و تولید می کنم✅. نه ترجمه.نه اخبار. نه گرداوریدوره:mohsentavoosi.com/course/seo/خرید دوره:@mohsentavoosisupportyoutube.com/c/MohsenTavoosiInstagram.com/mohsentavoosi.seolinkedin.com/in/mohsentavoosi</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 18:13:51</div>
<hr>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دوستانی که اکانت کلاد خریدند و تجربه موفق دارند و بن نشده لطفا تو دایرکت همین کانال اعلام کنید.   با توجه به نظر سنجی بالا من نمیبینم توی خودم که ماهانه به ۱۰۰۰ نفر بفروشم. نهایت میشه ۱۰۰ نفر با کلی دردسر. میشه حداکثر ماهی ۲۰۰ دلار با کلی مکافات.   پس من ورود…</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/mohsentavoosiseo/846" target="_blank">📅 14:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-844">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دوستانی که اکانت کلاد خریدند و تجربه موفق دارند و بن نشده لطفا تو دایرکت همین کانال اعلام کنید.   با توجه به نظر سنجی بالا من نمیبینم توی خودم که ماهانه به ۱۰۰۰ نفر بفروشم. نهایت میشه ۱۰۰ نفر با کلی دردسر. میشه حداکثر ماهی ۲۰۰ دلار با کلی مکافات.   پس من ورود…</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/mohsentavoosiseo/844" target="_blank">📅 12:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دوستانی که اکانت کلاد خریدند و تجربه موفق دارند و بن نشده لطفا تو دایرکت همین کانال اعلام کنید.
با توجه به نظر سنجی بالا من نمیبینم توی خودم که ماهانه به ۱۰۰۰ نفر بفروشم. نهایت میشه ۱۰۰ نفر با کلی دردسر. میشه حداکثر ماهی ۲۰۰ دلار با کلی مکافات.
پس من ورود نمی کنم به اینکار. و میخوام شما بگید از کجا میگیرید که عمومی بذارم بقیه هم برن بگیرن. کلاد بدون دردسر و بدون محدودیت.
از یک سرویس عمومی که همه بتونن. نه دوست و آشنا و کارت خارجی خودتون.
بگید که منم به بقیه بگم. تو دایرکت کانال بفرستید.
اگر ا......ت بوده فقط اگه بعد از اون بن شدن های دسته جمعیش بوده باشه بگید.</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/mohsentavoosiseo/843" target="_blank">📅 01:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/mohsentavoosiseo/842" target="_blank">📅 15:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-841">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/mohsentavoosiseo/841" target="_blank">📅 15:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ربطی به سوال بالا نداره. کلی هست.
با کلاس و بی کلاس در تعریف من.
پرداخت به هرچیزی جز خود‌ عیب جویی از هرکسی جز خود. مطابق مطالب زرد و سطحی.
#تروما
#آسیب
#سمی
#طرحواره
#تله
#عیب
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/mohsentavoosiseo/840" target="_blank">📅 15:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/mohsentavoosiseo/839" target="_blank">📅 14:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-838">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/mohsentavoosiseo/838" target="_blank">📅 14:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پاسخ سوال بالا، قسمت ششم
در تجارت، تواضع اشتباه هست.منت گذاشتن بسیار مهم و جایز هست. ترکیب تضادها در کار.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/mohsentavoosiseo/837" target="_blank">📅 14:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پاسخ سوال بالا، قسمت پنجم
انتقال پیام پنهان ضعف
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/mohsentavoosiseo/836" target="_blank">📅 14:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پاسخ سوال بالا، قسمت چهارم
هم خدا هم خرما. در نظر گرفتن استاندارد تخفیفی.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/mohsentavoosiseo/835" target="_blank">📅 14:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/mohsentavoosiseo/834" target="_blank">📅 14:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/mohsentavoosiseo/833" target="_blank">📅 14:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/mohsentavoosiseo/831" target="_blank">📅 13:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJYkzWQbwqNkG9rcbyXsvom9M3tT6uKModquJ2vxbZh-ogg-QAD_CKHqa4y3jlyWOyLctEFWMVhqn-7tBPqQAwAzox1TzXOkmrpOaJ0E_6e_wohedktingUyaHZpNnW4GsWPcBiOJee7Vaa5k2pQosCK33jNFtkcF2lPlwsJiDo-3DJFaCttki8Mj3vhxn9EUSyY4xwcQpIGtpBYF3o-6UgLJvgvTRZCFnQ3a6IIAvRgQXZ_24fzdjOC439zRsXTE6DJx4n4eGZRrDE2Ez5N9kLNZK-NTt4L_IbGfueSMFLpspiNRCeB4LDNcszfCqgc30SrDenCIIHWgvKQHnFhEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/mohsentavoosiseo/830" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره ( مثلا تخفیف بگیره یا نگه داره فردا پس فردا نکنه) ؟
حس‌میکنم این بازاریا وقتی دادن پولتو یک روز هم بیشتر طول میدن احساس برنده بودن میکنن . اینو چطوری بهش غلبه میکنین
مثلا طرف قفل میکنه تخفیف بده
یا همشو نمیدم نصف میدم نصف یوقت دیگ
وقتی سفت میگیری کلا ناراحت میشن و کار نمیگیره وقتی هم که راه میای باید داستان داشته باشی
نه که ندن ولی پولو از ارزش میندازن یبار
جواب سوال بالا در ادامه.(یه پادکست ضبط کردم. طولانی شد ویس ها).
#پروژه
#پروژه_گرفتن
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/mohsentavoosiseo/829" target="_blank">📅 13:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه کلاس زبان عمومی باید برای کلمه "People" قرار بدیم. اینجوری فایده نداره. خوب نیست دیگه انقدر آدم بی سواد باشه در عصر هوش مصنوعی که مترجم در لحظه و رایگان در دسترس هست.</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/mohsentavoosiseo/828" target="_blank">📅 12:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پاسخ سوال بالا
https://t.me/mohsentavoosiseo/826
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/mohsentavoosiseo/827" target="_blank">📅 21:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-826">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سوال از پشتیبان دوره(سانسور شده):
من دسترسی کامل به دوره دارم و دارم رو سایتم کار می کنم.
کارفرما اومده بهم میگه که یه محصولی به نام x یا خرید x ما تقریبا از سه ماه پیش اومدیم روی رتبه یک و محصولی بوده که تقریبا فقط ما داشتیم.
الان رقیبمون هم این محصول رو موجود کرده. در صورتی که دو سه روزه محصول رو تو سایت گذاشته و اومده لینک دو. اما ما خیلی طول کشید تا بیایم لینک یک.
من جواب لحظه ای که به کارفرما دادم این بود که شما سرمایه گذاری درستی روی سایتت نکردی الان سایتت از نظر UX و پرفورمنس و اعتبار و off page  صفره و مسلمه که سایتی با این اعتبار سریع میاد لینک دو و بعد ما.
الان کارفرما میگه با من با عدد حرف بزن و منطقی بهم بگو که دقیق چیکا کنم که تا چند روز اینده این سایت نیاد جای من که رتبه یک هستم رو بگیره.
پاسخ در voice پیش رو:
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/mohsentavoosiseo/826" target="_blank">📅 21:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/mohsentavoosiseo/825" target="_blank">📅 22:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-824">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بخاطر احترام به حقوق تولید کننده تصویر لینک پستش رو میذارم. ولی حرفم خود تصویر نیست.  بعد از نظر سنجی پایین، چیز دیگه ای میخوام بگم.</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/mohsentavoosiseo/824" target="_blank">📅 22:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-823">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-poll">
<h4>📊 این تصاویر رو می بینید کامل؟</h4>
<ul>
<li>✓ نه فقط کلی نگاه میکنم ببینم راجع به چیه.</li>
<li>✓ کلا حوصله ندارم ببینم اینارو</li>
<li>✓ کامل میبینم. دونه دونه فرایند ها و تصاویر و عناوین و متن هاشو.</li>
</ul>
</div>
<div class="tg-text">بخاطر احترام به حقوق تولید کننده تصویر لینک پستش رو میذارم. ولی حرفم خود تصویر نیست.  بعد از نظر سنجی پایین، چیز دیگه ای میخوام بگم.</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/mohsentavoosiseo/823" target="_blank">📅 18:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5AKMJEL0T1Q6HaUrlj7zPGTdKFdkXFaaw8q1zIELGmFnG0UNZdHJL6Oqfb6R2d9nf3G0KgG76VvmNMhoVpRAvTI3QKjx_WDVjLmDWTukrOdlZTSuVKbAfJY7y77hpWoYzIm9T30YXU6jhzQSZi-R-_MuVzFbEyvGbi5t-1b7c1IYEpqSGG3RP5Go0sjLSTdt0tKnw19sdvyZGGDNdD5W4_RYYxkMI36KQHcFpttxV_x3iJ-UeapLT7RG-Tq0W_h9NaLFvW2WLOl67wLa0YwHzaSf8qMl638QAIuNHjyndRSuOfwGQWDfeLAgwnmHoNYxIGAkQs6y6OSx3KZrcuJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر احترام به حقوق تولید کننده تصویر
لینک پستش
رو میذارم. ولی حرفم خود تصویر نیست.
بعد از نظر سنجی پایین، چیز دیگه ای میخوام بگم.</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/mohsentavoosiseo/822" target="_blank">📅 18:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اگر از داخل ایران وصل میشید، کشور رو یک کشور در نظر بگیرید و هربار یه کشور نشه. جوری نشه که انگار طی الارض دارید صبح آلمانید یک ساعت بعد آمریکا یک ساعت بعد ترکیه. (بیاید فرض کنیم پیاده از مرز سوئیس نمیرید آلمان و بین مرزهای شنگن در حالی که کلاد رو باز می کنید).</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/mohsentavoosiseo/819" target="_blank">📅 18:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-818">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کاهش احتمال مسدود شدن اکانت Claude
بجز اکانت گوگلی که باهاش تو کلاد لاگین میشید و بجز کارتی که باهاش پرداخت میشه،
اگر از داخل ایران وصل میشید، کشور رو یک کشور در نظر بگیرید و هربار یه کشور نشه. جوری نشه که انگار طی الارض دارید صبح آلمانید یک ساعت بعد آمریکا یک ساعت بعد ترکیه. (بیاید فرض کنیم پیاده از مرز سوئیس نمیرید آلمان و بین مرزهای شنگن در حالی که کلاد رو باز می کنید).
و چک کنید وی پی ان رو با یک سایت تحریم(بدون شکن) مثل
https://developers.google.com/search/docs
که 403 نده. اگه سایت های فیلتر براتون باز میشه ولی 403 میده این ها، یعنی به راحتی وی پی انتون قابل تشخیص هست که از ایران وصل میشید.
همچنین توی  incognito یا private mode مرورگر، وارد سایت
https://whatismyipaddress.com/
بشید و ببینید کدوم کشور هست آی پیتون.
من چون ایران نیستم خودم دست به تست نشدم. ولی همونطور که قبلا گفته بودم، کشور وی پی ان، با کارت پرداخت کننده اون حساب، باید بخونه. معمولا خرید مستر کارت مجازی همون کشور، راه امن تری هست. ولی روی کلاد تجربه ندارم که با این کار هم باز میبنده یانه.
چون اغلب آدم ها حوصله ندارن وی پی ان و مسترکارت مجازی رو خودشون بخرن بزنن. میدن یکی پرداخت کنه. همین خودش باعث دردسر میشه.
به شرطی که سایت پرداخت کننده هم، اون کارت مجازی رو قبول کنه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/mohsentavoosiseo/818" target="_blank">📅 18:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-817">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تفاوت کلاد در چت بات(پایین ترین سطح استفاده از کلاد):  متأسفانه لینکی که دادی به خاطر AJAX فیلتر می‌شن و محتوای واقعی سوال‌ها رو نمی‌تونم ببینم سیستم فیلتر کردن با JavaScript کار می‌کنه که من بهش دسترسی ندارم.  اشاره به همون بحث همیشگی SSR در سئو(https://…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/mohsentavoosiseo/817" target="_blank">📅 14:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تفاوت کلاد در چت بات(پایین ترین سطح استفاده از کلاد):
متأسفانه لینکی که دادی به خاطر AJAX فیلتر می‌شن و محتوای واقعی سوال‌ها رو نمی‌تونم ببینم سیستم فیلتر کردن با JavaScript کار می‌کنه که من بهش دسترسی ندارم.
اشاره به همون بحث همیشگی SSR در سئو(
https://t.me/mohsentavoosiseo/267
) که گفتم فاز لبه تکنولوژی برداشتن بر ضد پول و به ضرر خودمون هست.
هوش مصنوعی های دیگه نمیفهمن به خاطر جاوااسکریپتی لود شدن با Query string نشون نمیده. این عین انسان میفهمه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/mohsentavoosiseo/816" target="_blank">📅 14:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-813">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مباحث امنیتی(امنیت ایالات متحده)</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/mohsentavoosiseo/813" target="_blank">📅 14:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">صحبت خارج از موضوع کلاد:
چون خیلی شکایت میشنوم میگم. وگرنه جالب نیست بگم. چون اون ها هم بهرحال از دوستان من هستند. میگم که شاید تغییری ایجاد شه.
از ل............ت برای احترام اول به اعصاب بعد به پولتون توصیه نمیکنم خریدی انجام بدید. آدم های خوبی هستند. اما چون همه چیز دست مدیران فنی هست و ذهنشون همه چیو فنی میبینه و با ذهن تکنیکال غیر تجاری میخوان مشکلات رو حل کنن و تصمیم گیری کنند،
در مدیریت فرایند سفارش ها به مشکلات زیادی میخورن و بعد میان موردی دونه دونه حل میکنن.
افتادند توی لوپ و حلقه بهینه سازی(بازم فنی) که دیگه یک بار برای همیشه درستش کنند. چند ساله. اما گاهی باید ورود کرد دستی کار رو جمع کرد. باید هزینه کرد. بیخیال سود بیشتر شد و به روش غیر فنی، فعلا شرایط رو درست کرد.
بماند که در تشخیص فنی اینکه مشکل کجاست هم اشتباه میکنند. چون فقط از یک زاویه دارن به مشکل نگاه می کنند.
همون چیزی که همیشه میگم مغز صرفا دولوپری و غیر تجاری،
1- یا ایده هاش شکست میخوره،
2- یا نمیتونه بفروشه اصلا و جمع میکنه
3- یا نارضایتی از محصول یا خدماتش ایجاد میشه که نمیتونه حلش کنه(این ها سومی هستند و حداقل تو یک و دو گیر نکردند).
این نکته برای خود اون کسب و کار و کسانی که دریچه دریافتشون بازه، میلیون دلاری ارزش داره. باید میلیارد ها تومن یا صد ها هزار دلار از دست بدن تا این بازخورد رو از زبون یه مشاور که ایراد کسب و کارشون رو میگه بشنون.</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/mohsentavoosiseo/812" target="_blank">📅 14:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⭕️
❗️
🟢
درباره معلق شدن اکانت های کلاد
موجی که راه افتاد ظاهرا همه کسانی که از سایت ا.........ت خریده بودند suspend شدند. اما از گزارش هایی از ساسپند شدن غیر از ا.......ت هم هست.
برای ما نشده. لاگین از ایران هم داریم با وی پی ان. و لاگین های ما از چند کشور هست. ولی هربار کشورش عوض نمیشه.
پرداخت هم از یکی از کشور های ثابت اتحادیه اروپاست با کارت شخصی. با کارت زراعت بانک، ایش بانک و وکیف بانک ترکیه و ورود از ترکیه هم مشکلی نداشته.
مکالمه ما هم فارسی هست اکثرا. ربطی به زبان شما نداره. حساسیت اصلیش روی پرداخت کننده هست و هویت پرداخت کننده.
چون بحث احراز هویت سنی و مباحث امنیتی(امنیت ایالات متحده) توش لحاظ میشه.
اکثر ادم ها هم استفاده های سنگین ندارند. حتی از skill و connector ها که پایه ترین و ابتدایی ترین قابلیت کلاد هست استفاده نمیکنن. فعالیتی که توسعه کد سنگین تو گیت هاب به صورت انلاین و مواردی که میتونه منجر به استفاده عمومی بشه رو بهش حساس تر هست.
اما خودشون میدونن دقیقا رو چی حساسن. تو متن خودش هم نوشته موارد خاص و این خاص رو تعریف نکرده.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/mohsentavoosiseo/811" target="_blank">📅 14:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-810">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کسانی که گزینه "خوشحال" رو زدند که از جایی با قیمت خیلی کمتر به صورت اختصاصی میخرند،
ممنون میشم دایرکت پیام بدید(آیکون یا کلید message همین کانال) و من رو هم از این نون سهیم کنید
😒
. زشته کارتون که مخفی نگهش داشتید
😏</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/mohsentavoosiseo/810" target="_blank">📅 15:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-809">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-poll">
<h4>📊 اگر من ابزار های اختصاصی(نه اشتراکی) هوش مصنوعی رو به قیمت دلاری اصلش ارائه بدم با حداکثر 10 درصد بالاتر، هر ماه حتما تهیه می کنید از من؟</h4>
<ul>
<li>✓ صد در صد بله</li>
<li>✓ 10 درصد بالاتر نه. معادل دقیق قیمت دلاریش باشه صد در صد</li>
<li>✓ نه. فقط اگه یک کم ارزون تر از معادل دلاریش در بیاد میگیرم. وگرنه نمی گیرم.</li>
<li>✓ من از بعضی AI ها رو از جایی میخرم که خیلی کمتر از قیمت دلاریش در میاد. اختصاصی هم هست و خوشحالم.</li>
</ul>
</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/mohsentavoosiseo/809" target="_blank">📅 15:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-808">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">درباره این ویس و اون سوال، اون سه راهکار (ادز و کانال های غیر کیوردی، کیورد ریسرچ عمیق تر و out of the box و تغییر استراتژی محتوایی)، اگه همچنان شکست بخوره، جواب نده یا نصرفه یا توان هزینه کردن نباشه،  دیگه باید بوسید گذاشت کنار دیگه. سود ما تسلیم شدن به موقع…</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/mohsentavoosiseo/808" target="_blank">📅 00:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-807">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/mohsentavoosiseo/807" target="_blank">📅 00:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-805">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/mohsentavoosiseo/805" target="_blank">📅 20:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-804">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">https://www.instagram.com/reel/DaNzmW8MtPF/</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/mohsentavoosiseo/804" target="_blank">📅 20:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-803">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">https://www.instagram.com/reel/DaNzmW8MtPF/</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/mohsentavoosiseo/803" target="_blank">📅 20:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-802">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">من احساس میکنم آموزشی که جناب طاووسی میدن برای این مدل بیزینس ها مثل سایت ما یه آپدیت نیاز داره که نیاز هست برای سایتایی که کم محصول هستن و محصولاتشون قابل تفکیک و توسعه به صفحات مختلف نیست چیکار باید بکنن؟</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/mohsentavoosiseo/802" target="_blank">📅 19:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-801">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سوال یکی از دانشجویان دوره از پشتیبان دوره:  من یک سایت در زمینه فروش پلاگین های وردپرسی دارم. کلا نزدیک 13-14 تا محصول بیشتر روی سایتم نیست مشکل من اینه که توی مثال ما یک لندینگ بیشتر نمیتونیم بسازیم اونم برای خود محصوله.سایر صفحات میشه ویژگی های محصولمون...که…</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/mohsentavoosiseo/801" target="_blank">📅 19:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-800">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سوال یکی از دانشجویان دوره از پشتیبان دوره:
من یک سایت در زمینه فروش پلاگین های وردپرسی دارم. کلا نزدیک 13-14 تا محصول بیشتر روی سایتم نیست
مشکل من اینه که توی مثال ما یک لندینگ بیشتر نمیتونیم بسازیم اونم برای خود محصوله.سایر صفحات میشه ویژگی های محصولمون...که نمیتونیم اینجا صفحه لیستینگ بسازیم و مجبوریم بلاگ ایجاد کنیم.
اگه بخوام مثال بزنم مثلا پلاگین woocommerce gift داریم که براش یه لندینگ ساختیم و یکی از ویژگی های این پلاگین BOGO deal هستش..خب ما اینجا نمیتونیم یه صفحه لیستینگ بسازیم که در مورد BOGO deal باشه و فقط یه پلاگین توش باشه..نمیتونیمم یه لندینگ جدا برای BOGO بزنیم که اونجا پلاگین رو معرفی کنیم. مجبوریم یه بلاگ بزنیم که در مورد BOGO حرف بزنیم و نتیجه این میشه که کسی که توی حوزه ما یه پلاگین مخصوص فقط برای BOGO deal زده باشه میاد بالاتر از پلاگین ما قرار میگیره و ما هم توی برنامه مون نیست که بیایم این ویژگی رو از دل پلاگینمون در بیاریم و یه پلاگین جداش بکنیم. در نتیجه توی نتایج در صفحات عقب تر دیده میشیم.
یا مثال دیگه یکی از ویژگی های پلاگین ما Buy X Get Y هست که این کلمه خیلی سرچ میشه. ما نمیتونیم اینو جدا کنیم از پلاگین و یه پلاگین یا محصول جدا بدیم ولی رقبا اومدن یه پلاگین نوشتن فقط buy x get y انجام میده و اون الان بالاتر از ماست توی نتایج در حالی که این یه ویژگی خیلی کوچیک از پلاگین بزرگ ماست.
وقتی هم بلاگ مینویسیم برای این ویژگی توی بلاگ مجبوریم اینفورمیشنال صحبت کنیم و از روش های مختلف غیر از پلاگین خودمون هم حرف بزنیم که بتونیم با رقبایی که فقط بلاگ وردپرسی هستن رقابت کنیم. در نتیجه نرخ تبدیلمون خیلی کم میشه.
من احساس میکنم آموزشی که جناب طاووسی میدن برای این مدل بیزینس ها مثل سایت ما یه آپدیت نیاز داره که نیاز هست برای سایتایی که کم محصول هستن و محصولاتشون قابل تفکیک و توسعه به صفحات مختلف نیست چیکار باید بکنن؟</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/mohsentavoosiseo/800" target="_blank">📅 19:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-799">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سوال زیر رو 99 درصد آدم ها متوجه نمیشن. ولی تو جواب، ساده توضیح دادم سوال، چی هست.
مخاطبشم اکثر آدم ها نیستند. اما نکته های توی جواب، از نظر باز شدن ذهن، به درد همه میخوره.</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/mohsentavoosiseo/799" target="_blank">📅 19:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-798">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انقدر که رو وایب کدینگ مانور میدن تعجب میکنم. البته درک میکنم. بازارگرمی خوبیه برای اینکه کسی که خبر نداره بگه wowwww برم ببینم چیه.
vibe coding - وایب کدینگ
یعنی به هوش مصنوعی بگی چی میخواد برات کدش رو بزنه. همین! یعنی هوش مصنوعی به عنوان نوکر کد زن تو باشه. یعنی nokar coding یا vibe nokaring
😏
حالا میتونی روی پرامپت خوب زدن مانور بدی که اون دیگه ربطی به وایب کدینگ نداره. برای کار با هر هوش مصنوعی هست به صورت کلی.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/mohsentavoosiseo/798" target="_blank">📅 17:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-797">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اگر فروش اکانت کلاد، جمینای و سایر هوش مصنوعی ها رو دارید، و همینطور ابزار های SEO،  من به عنوان Reseller شما و شما هم تامین کننده اصلی، میتونیم همکاری داشته باشیم.
فقط با کد تخفیف و این چیزا کار در نمیاد.
ممکنه کد تخفیف بزنن سری دوم نزنن. و ممکنه یک ابزار بخره کاربر از طریق من، ولی بعد سری دوم بیاد ابزار دیگه ای با همون اکانت بخره. لینک affiliate خالی هم فایده نداره. مگر اینکه کوکی خوبی براش تعریف بشه.
اگر یک ساز و کار عادلانه و قابل track خوبی وجود داشته باشه، میشه همکاری کرد. تقاضای زیادی سمت من میاد. به خاطر سود بسیار کم و تامین پردردسرش، من نمیخوام خودم ورود کنم به کسب و کارش کلا که کلا خودم بزنم. در حد ریسلر فقط میخوام درگیر شم.
کلا به خاطر track نامناسب یا عدم اعتماد کافی یا ثبات نداشتن آدم ها یا کسب و کار هاشون، تا حالا همکاری جدی reseller نداشتم.
اگر فکر می کنید میتونیم همکاری داشته باشیم به دایرکت همین کانال، پیام بدید.</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/mohsentavoosiseo/797" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-796">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سوال:
من 20 میلیون تومن پول توی بورس دارم. بفروشم سایت بزنم؟ سئو هم بلدم.
پاسخ:
سئو با 20 تومن در نمیاد. میشه 120 دلار! میشه 5200 لیر.
شما هیچ کسب و کاری رو با 100 دلار نمی تونید به سود برسونید. پول میخواد. با هر استراتژی ای حساب کنید(کیورد های کم رقابت)، باز هم با صد دلار به فکر راه اندازی کسب و کار نباشید.
در بدترین حالت، کم رقابت ترین حالت، حوزه خیلی خیلی خاص یا محدود شده به چند مورد خاص که سوداوری خوبی داره(بعد از تحقیق مفصل کلمات کلیدی)، مثلا در حد کیودری مثل "خرید فلان ماده اولیه" که اون مواد اولیه برای کارخونه های خاصه و شما هم مثلا آشناش رو برای تامینش دارید، رقابتش صفر یا نزدیک به صفره و خلوته ولی سرچ کننده ها مشتری هستند و پرداخت خوب دارند و نرخ تبدیلش بالاسات،(چون مثلا کم هست کلا)
در این صورت، با ماهی 200 دلار(نه یک بار 200 دلار)، میشه امیدوار بود بعد از 6 ماه شروع کنه به درامدزایی. در خیلی شرایط استثنایی، 3 ماه. شایدم اگه کیورد خاص پرسودی باشه مثل مثالی که زدم و هیچ کس هم کار نمیکنه و جنسشم جوریه که شما میتونید تامین کنید راحت، شاید خیلی استثنایی بشه با همون یک بار 200 دلار. بشرطی که از قبل بدونید. نه اینکه تازه بخواید شروع کنید تحقیق کردن.
روش دیگه ای بلدید؟ میگی نه! رفیق من فلان کرد و فلان؟ حله. من بلد نیستم. از رفیقتون بپرسید. نه بلدم نه آموزشش رو میدم.
شما اکانت 20 دلاری کلاد نیاز دارید حداقل. دستی هم انجام بدید موقع Off-Page نیاز دارید به هزینه کردن. خیلی چیز ها هم هزینه پنهان هست که به چشم نمیاد. مثل زمانتون که داره میره و از کار و زندگی مفتید. ماهی 40 میلیون تومن از دست میدید که سال دیگه تازه شروع کنه به درامدزایی.
سئو پول میخواد. رایگان نیست. ابزار هاش هم رایگان گیر بیارید، موقع Off-Page، پول میخواد.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/mohsentavoosiseo/796" target="_blank">📅 14:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-795">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مشکل ما با کسانی هست که سوال نمی پرسند از پشتیبانی و خجالت می کشند!
آپدیت مفصل سئو بین المللی بیاد که خیلی فشردست اون موقع هم میخواید سوال نکنید؟(دانشجویان دوره).
کی دیدید التماس کنه بیا از پشتیبانی استفاده کن! 60 هزار تا سوال بپرس! هرروز! هر ساعت! ما طبق زمان بندی خودمون جواب میدیم. ولی شما که میتونید بپرسید!
آگر تو دوره باشه و مشخصه که ندیدید، ارجاع میدیم به ویدیو دوره، بهر حال یه کمکی می کنیم در حد تعهدی که مکتوب دادیم(نوشته شده موقع خرید). ولی از سمت شما واقعا نباید مراعات و شرم وجود داشته باشه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/mohsentavoosiseo/795" target="_blank">📅 12:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-794">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چالش رایج دیگه ما!
آدم ها خجالت میشکن. فکر میکنن کنتور میندازه یا سهمیه ایه سوال پرسیدن! (پشتیبانی دوره رو میگم. نه دایرکت خودم).
مهارت سوال کردن، مهارت طرح سوال وقتی که جواب، دقیق به جواب ما نیست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/mohsentavoosiseo/794" target="_blank">📅 12:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-793">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سوال از پشتیبان دوره:(سوالات خیلی سطح حرفه ای هم داریم. ولی هدفم پاسخ دادن نیست الان).  مابقی دستورهایی که میخوام در فایل روبوت بزارم مثل قبل هست؟ مثلا disallow کردن سرچ ها صفحه چک اوت و ...   فقط ادرس لاگین رو دیگه قرار ندم  درسته؟</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/mohsentavoosiseo/793" target="_blank">📅 12:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-792">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سوال از پشتیبان دوره:(سوالات خیلی سطح حرفه ای هم داریم. ولی هدفم پاسخ دادن نیست الان).
مابقی دستورهایی که میخوام در فایل روبوت بزارم مثل قبل هست؟ مثلا disallow کردن سرچ ها صفحه چک اوت و ...
فقط ادرس لاگین رو دیگه قرار ندم
درسته؟</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/mohsentavoosiseo/792" target="_blank">📅 12:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-791">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خرید قسطی هرچیزی، intent کاملا متفاوتی از خرید اون چیز داره(بدون کلمه قسطی). اگر سرچ والیوم داره(جستجو میشه قسطیش) صفحه اش باید جدا باشه برای شانس بهتر رتبه گرفتن.
اگر صفحه یکی باشه و تو عنوان بنویسید نقد و اقساط، حوزه رقابتیش بزرگتر میشه. ولی این هم میشه. ولی روی کیورد خرید قسطی اون چیز، سخت تر رتبه می گیره.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/mohsentavoosiseo/791" target="_blank">📅 00:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-790">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سوال دانشجو:  و اینکه یکسری تعاریف هست برای سئو هست. این ها چی هستند؟  Topical Authority Internal Linking Strateg Site Architecture  Content Hub / Pillar & Cluster Information Architecture + Semantic SEO Link Equity Flow + Topic Authority Reinforcement</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/mohsentavoosiseo/790" target="_blank">📅 00:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-789">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سوال دانشجو:  و اینکه یکسری تعاریف هست برای سئو هست. این ها چی هستند؟  Topical Authority Internal Linking Strateg Site Architecture  Content Hub / Pillar & Cluster Information Architecture + Semantic SEO Link Equity Flow + Topic Authority Reinforcement</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/mohsentavoosiseo/789" target="_blank">📅 00:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-788">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سوال دانشجو:
و اینکه یکسری تعاریف هست برای سئو هست. این ها چی هستند؟
Topical Authority
Internal Linking Strateg
Site Architecture
Content Hub / Pillar & Cluster
Information Architecture + Semantic SEO
Link Equity Flow + Topic Authority Reinforcement</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/mohsentavoosiseo/788" target="_blank">📅 00:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-785">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کسانی که میگن چرا طرف رفت ارمنستان یا ترکیه؟ اونجا که ظرفیت نداره فضای دیجیتالشون. اونجا که اقتصادش فلانه!  باید بگم قرار نیست برن شرکت ترک یا ارمنی کار کنند. ظرفیت اونجا مهم نیست! از دیجیتال مارکتر ها بعیده این حرف!  اونجا فقط یه نقل مکان سکونت فیزیکی هست…</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/mohsentavoosiseo/785" target="_blank">📅 22:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-782">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آموزش سئو با محسن طاوسی
pinned «
هرچیزی که دوست دارید یاد بگیرید یا از من یاد بگیرید، حتی خارج از سئو، توی دایرکت کانال بفرستید.  میخونم همه رو قطعا. (صرفا دریافت. بدون پاسخ و تعامل خصوصی).  قصدم از باز کردن دایرکت، صرفا دریافت نظرات شما درباره اینکه علاقه مند به یادگیری چه چیزی حتی خارج…
»</div>
<div class="tg-footer"><a href="https://t.me/mohsentavoosiseo/782" target="_blank">📅 13:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-781">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هرچیزی که دوست دارید یاد بگیرید یا از من یاد بگیرید، حتی خارج از سئو، توی دایرکت کانال بفرستید.
میخونم همه رو قطعا.
قصدم از باز کردن دایرکت، صرفا دریافت نظرات شما درباره اینکه علاقه مند به یادگیری چه چیزی حتی خارج از سئو هستید.</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/mohsentavoosiseo/781" target="_blank">📅 13:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-780">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8PHnik5grlHQxaJT-DwCSY4WxU0l3L4h2br70UhOkcTRAClOm29XFWgei798Dn-9OaevBbyDlB1KySQhdgbl9qcDGmz9ou0vH7d3k_p82YmDkLX9FDHPNKPX3XcFXDvw5lOtTUqlDqf4ZSwCdGpejtyrhoZlxpJfYudtz9vpVNAk5ZCLG3KHqwcAC1PmKgzS9Gsxyp16hJsDW-b2mkbSKg9aDa2Uc2gtcltpo9OqX2-aOpPFu5NOUoTDG2PvwWIqdzPdI20_KM9JLIVn5s7k144JQ7vFbLAS0j0thbMfgbINGOSnDXxw3PocQChryWDfY0ZNl3Rx5wsn1uOKvZTow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسانی که نمیدونن دایرکت کجاست. پیام خصوصی ایکونش در اندروید اون پایینه. نیازی هم به ستاره و تلگرام پریمیوم نداره.
تو آیفون هم داخل خود کانال رو اسم کانال بزنید نوشته message.
تو وب و دکستاپ ندیدم هنوز خودم.
بدیهیه که تبلیغات، مال خود تلگرامه و در کنترل من نیست. خداروشکر این کانال، افرادش آی کیوشون تو این چیزا بالاست و میدونن که تبلیغات پایین کانال های تلگرام، دست اون کانال نیست.</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/mohsentavoosiseo/780" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-778">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هرچیزی که دوست دارید یاد بگیرید یا از من یاد بگیرید، حتی خارج از سئو، توی دایرکت کانال بفرستید.
میخونم همه رو قطعا. (صرفا دریافت. بدون پاسخ و تعامل خصوصی).
قصدم از باز کردن دایرکت، صرفا دریافت نظرات شما درباره اینکه علاقه مند به یادگیری چه چیزی حتی خارج از سئو هستید و شنیدن هر صحبتی.</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/mohsentavoosiseo/778" target="_blank">📅 11:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-776">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/mohsentavoosiseo/776" target="_blank">📅 17:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-775">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">توضیح در ویس پایین  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/mohsentavoosiseo/775" target="_blank">📅 17:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-774">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTIGQLNs9dytszNu1GO_CSM_cBx4AFIAcalR_QbdwfA53s00F7qRI7lXJNS9zCJJbdv1cXgXN3P3m2DdkSvlLcI_SS4dz0_IbuMncRuuKUdVWFt0dNyy_oPbW7BBiwa75EvY3HC5YhTn5I_oCJbSfUkDQDPUNCaW4qssft-fVsaapBplvwocLRTcAQbK7x_c3WoRHei6X1ecXoBxvI7EKRboiLbGmTWhUwIFIiYOHq2phCPqRj2-Z6pmyDTFqJcRgTzisqU4OWC0QIOHpg4zFFc1yVZzpFapO5a7tSIecNa0jutW4gpNzNbTMgn02KcN3LORKKYLJ-iOdjnsfKorOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره پستی که روش ریپلای زدم:   نظر یک نفر قبل از اون پست:  از این زاویه نگاه میکردم که آقا تفکر وقتی آزاد باشه کامنت هم باز میزاره که جامعه بتونه درموردش صحبت کنه  وقتی میبنده داره آزادی رو میگیره</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/mohsentavoosiseo/774" target="_blank">📅 17:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-773">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">درباره پستی که روش ریپلای زدم:   نظر یک نفر قبل از اون پست:  از این زاویه نگاه میکردم که آقا تفکر وقتی آزاد باشه کامنت هم باز میزاره که جامعه بتونه درموردش صحبت کنه  وقتی میبنده داره آزادی رو میگیره</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/mohsentavoosiseo/773" target="_blank">📅 18:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-771">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چرا کامنت ها و ری اکشن هارو من باز نمیکنم؟ بخاطر بحث اقتصاد توجه: https://t.me/mohsentavoosiseo/364  نمیخوام ذهنم درگیر این شه که اااا پستام کم لایک خورد. کم ری اکشن مثبت داشت. ااا منفی داشت. . خیلی لایک خورد روحیه بگیرم. و وقتی کم لایک خورد ناراحت بشم. یا…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/mohsentavoosiseo/771" target="_blank">📅 18:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-770">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/mohsentavoosiseo/770" target="_blank">📅 12:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-769">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سوال یک دنبال کننده که احتمالا شناخت قبلی هم به من نداره:  نکات سوال:  پارتی نداشتم کار خوب گیرم نیومد گفت ریاضیت قوی نیست پایتون نخون.  تحصیلات بدون فرصت خوب اشتغال.  نگرانی آینده.  هوش مصنوعی جای سئو رو میگیره؟  سئو رو برای کارمندی یاد بگیرم.  ۹ ماه کاراموزی…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/mohsentavoosiseo/769" target="_blank">📅 15:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-768">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntTYthj5dU5LaCPMczdAj5WW93TPJsU4WpOyjWe5Q1ESinHbYMV2SbVyCK8grtVP4aUggEk-FdITf17mSiDqWCW4PPmYY_jvT_RYO8ybcQX1KxWqOpsuJUUzr0nNSka-gs7PlscGR61Fy4euJU6r9T1-LcDCOipXkFp4FtW447M2My3R6YcnDqrYb_ITBtjhhrPag1irmlnIPvoGuP2cXKnA287yg5CC2yhzRS3RhxtggNjWdu1ausUC07ZW-GqHz_o1PRhcYvfxOcp2XEADZ4rT-vJiGJ38Hvg12paFs4efr0hH8BJiWyY0byb-2CQtT4ABvnZa_viyeGKo6HD7KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوال یک دنبال کننده که احتمالا شناخت قبلی هم به من نداره:
نکات سوال:
پارتی نداشتم کار خوب گیرم نیومد
گفت ریاضیت قوی نیست پایتون نخون.
تحصیلات بدون فرصت خوب اشتغال.
نگرانی آینده.
هوش مصنوعی جای سئو رو میگیره؟
سئو رو برای کارمندی یاد بگیرم.
۹ ماه کاراموزی رایگان
تو ویس بعدی فقط جواب نمیدم. تحلیل می کنم این  صحبت ها رو.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/mohsentavoosiseo/768" target="_blank">📅 14:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-767">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">چرا کامنت ها و ری اکشن هارو من باز نمیکنم؟ بخاطر بحث اقتصاد توجه: https://t.me/mohsentavoosiseo/364  نمیخوام ذهنم درگیر این شه که اااا پستام کم لایک خورد. کم ری اکشن مثبت داشت. ااا منفی داشت. . خیلی لایک خورد روحیه بگیرم. و وقتی کم لایک خورد ناراحت بشم. یا…</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/mohsentavoosiseo/767" target="_blank">📅 14:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-766">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">من دهان به دهان شنیده بودم از چند تا از دوستان که زمان مصاحبه برای مجموعه خودشون، کسانی که دوره رو دیده بودن خیلی از نظر فنی و مهارت نرم، متمایز بودند.   افتخار میکنم
❤️
❤️
اما الان دغدغم اینه که کسانی که دوره رو گرفتند، کامل ببینند. چون درصد کسانی که کامل میبینن…</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/mohsentavoosiseo/766" target="_blank">📅 14:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-765">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/mohsentavoosiseo/765" target="_blank">📅 14:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-762">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سوال دانشجو:  من ی مشتری دارم که سایت خدمات راپل و نماشویی ساختمان داره گیر داده که فقط مقاله میخواد و ماهی ۷ بیشتر نمیده و من باید بهش تضمین بدم تو قرارداد بیارم که رتبه میگیره صفحه اول. این حرفش منطقیه؟</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/mohsentavoosiseo/762" target="_blank">📅 13:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-761">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaTEiWsLNICzio1RY7IKb1uUmKJabOP9QW2FVdo4zVjDob484dEhCLOf87BXX310cnJhsAG3FiA6YKIIpQ_q-yuu26RB0ywNrCL8bMYFgxXiPhxUNgnGBpXCrP8AK3BwiXpyemz3ORaubQEM7cqgawPL-MSucN7xRE-V4KDp8Iu6IUzYdaFjwZf_8jqMBEWpXrrdNC-36kaskhrqd_TutwOnA6moSJZWWnkakDte1nVQZ02oT2dPa6nogXJwEOn_dmcXjMX22l-ppIcEQoBQCk_urTJwkKRSXPe56XcKt6gipTwzuFDkb3fokpBlWPo-M0mvIXwLgslTNilZ1qiajg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوال دانشجو:
من ی مشتری دارم که سایت خدمات راپل و نماشویی ساختمان داره
گیر داده که فقط مقاله میخواد و ماهی ۷ بیشتر نمیده
و من باید بهش تضمین بدم تو قرارداد بیارم که رتبه میگیره صفحه اول.
این حرفش منطقیه؟</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/mohsentavoosiseo/761" target="_blank">📅 13:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-760">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اگر کار دقیقا قابل برنامه ریزی میخوادی جای اشتباهی اومدید. SEO به دردتون نمیخوره</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/mohsentavoosiseo/760" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-759">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سئو برای این نیست که بهار شروع کنی تابستون بیای بالا محصولات تابستونی بفروشی یا برعکس برای زمستون و فصل.
نمیگم نمیشه. ولی نباید روش حساب کنید. اگر کار دقیقا قابل برنامه ریزی میخوادی جای اشتباهی اومدید. SEO به دردتون نمیخوره. هرچیزی هم میچینید فقط رو احتمال و تخمین با بیش از 50 درصد احتمال خطا هست.
کار با زمان بندی دقیق میخوای اورگانیک سرچ به درد نمیخوره. گوگل ادز و سایر روش های دیجیتال مارکتینگ ادز محور فقط. که میتونی در لحظه و در روز کمپین رو شروع کنی و تموم کنی.
گوگل خیلی تلاش کرد کنترل رو از ارگانیک سرچ باز ها(SEO) بگیره که گوگل ادز بیشتری بفروشه و برای گوگل ادز تقاضا بره بالا. و موفق هم شد.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/mohsentavoosiseo/759" target="_blank">📅 12:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-758">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/mohsentavoosiseo/758" target="_blank">📅 11:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-757">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سوال دانشجو:  من رو یه سایت دارم کار میکنم که تجهیزات آشپزخونه میفروشه.یه دسته بندی داره هود اخوان.و تقریبا ۵ ساله همین دسته بندی رو داره.زیر مجموعه میتونه هود مخفی،هود مورب،هود شومینه ای باشه با توضیحات و مدلاش.الان اوکیه من اضافه کنم؟یا چون همون صفحه هود…</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/mohsentavoosiseo/757" target="_blank">📅 11:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-756">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سوال دانشجو:
من رو یه سایت دارم کار میکنم که تجهیزات آشپزخونه میفروشه.یه دسته بندی داره هود اخوان.و تقریبا ۵ ساله همین دسته بندی رو داره.زیر مجموعه میتونه هود مخفی،هود مورب،هود شومینه ای باشه با توضیحات و مدلاش.الان اوکیه من اضافه کنم؟یا چون همون صفحه هود اخوان رتبه داره اینکار رو نکنم.</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/mohsentavoosiseo/756" target="_blank">📅 11:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-755">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/mohsentavoosiseo/755" target="_blank">📅 20:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-754">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سوال دانشجو:  من روی کیورد با مشتری کار میکردم و قیمت میدادم یعنی یک سری کلیدواژه میداد و میگفت اینا برای من مهمه و من کار میکردم میوردمشون صفحه اول  علاوه بر این براش مقاله هم مینوشتم و تو بقیه صفحه ها هم کار میکردم  و تضمین میدادم که میارمش صفحه اول اما…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/mohsentavoosiseo/754" target="_blank">📅 20:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-753">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سوال دانشجو:
من روی کیورد با مشتری کار میکردم و قیمت میدادم یعنی یک سری کلیدواژه میداد و میگفت اینا برای من مهمه و من کار میکردم میوردمشون صفحه اول
علاوه بر این براش مقاله هم مینوشتم و تو بقیه صفحه ها هم کار میکردم
و تضمین میدادم که میارمش صفحه اول اما این تضمین از دید دوره درست نیست
حالا میخوام بدونم مشتری روی یک سری از کلیدواژه ها میخواد بیاد بالا (از 98 تا 1401) روش کلمه ها کار کردم و صفحه اول بوده الان افت کرده و میگه کار کنید تا بیام صفحه اول.
سوالم اینه مشتری از من در برابر پولی که میده تضمین میخواد قبلا من تضمین رنک میدادم
الان چی بهش بگم برای تضمین؟</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/mohsentavoosiseo/753" target="_blank">📅 20:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-752">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سوال یکی از دانشجویان:  هدف از صفحه دسته بندی محصول اینه که خب محصول بفروشه قسمت توضیحات هم که شاخص ها کیفیت و قیمت گفته میشه  صفحه اصلی هم که معرفی برند هست هدف از اینکه برای بعضی کلمه ها لندینگ پیج داریم چیه ؟  با کلمه هایی که براشون دسته بندی داریم هم نوع…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/mohsentavoosiseo/752" target="_blank">📅 18:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-751">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ادامه جواب بالا
روش جادویی من تو مشاوره هام(توهم جادو)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/mohsentavoosiseo/751" target="_blank">📅 17:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-750">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/mohsentavoosiseo/750" target="_blank">📅 17:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-749">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/mohsentavoosiseo/749" target="_blank">📅 17:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-748">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سوال یکی از دانشجویان:  هدف از صفحه دسته بندی محصول اینه که خب محصول بفروشه قسمت توضیحات هم که شاخص ها کیفیت و قیمت گفته میشه  صفحه اصلی هم که معرفی برند هست هدف از اینکه برای بعضی کلمه ها لندینگ پیج داریم چیه ؟  با کلمه هایی که براشون دسته بندی داریم هم نوع…</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/mohsentavoosiseo/748" target="_blank">📅 17:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-747">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سوال یکی از دانشجویان:
هدف از صفحه دسته بندی محصول اینه که خب محصول بفروشه قسمت توضیحات هم که شاخص ها کیفیت و قیمت گفته میشه
صفحه اصلی هم که معرفی برند هست
هدف از اینکه برای بعضی کلمه ها لندینگ پیج داریم چیه ؟
با کلمه هایی که براشون دسته بندی داریم هم نوع نمیشن؟
مثلا الان یه دسته بندی داریم که دسته بندی تجهیزات هتلی هست که داخلش محصولات لیست شدن
و یه لندینگ پیج تجهیزات هتلی برای تماس بگیرید و هتل های تجهیز شده و …
اینا الان هم نوع میشن؟</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/mohsentavoosiseo/747" target="_blank">📅 17:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-746">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سوال بعضی از دانشجویانی که تازه شروع کردند:  داخل این دوره ی اموزشی طریقه ی این که چجوری کلمات کلیدی که پیدا کردیم رو تو صفحات بزاریم رو اموزش میده چون من نه از رودپرس سایت یا سئو هیچ پیش زمینه ای ندارم و داخل وردپرس اگه من بخوام کلمات کلیدی رو جایی بزارم…</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/mohsentavoosiseo/746" target="_blank">📅 17:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-745">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سوال بعضی از دانشجویانی که تازه شروع کردند:
داخل این دوره ی اموزشی طریقه ی این که چجوری کلمات کلیدی که پیدا کردیم رو تو صفحات بزاریم رو اموزش میده چون من نه از رودپرس سایت یا سئو هیچ پیش زمینه ای ندارم و داخل وردپرس اگه من بخوام کلمات کلیدی رو جایی بزارم باید کجا بزارم ؟</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/mohsentavoosiseo/745" target="_blank">📅 17:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-744">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdSTZmWoAQo-PnbpDQpU5hCLu6-41t-9AIXUFSaXIFOqf7KXBlCUXGCzvciVzjoz_oHL069nt0GC52MAPFZ6zJdKEnRc4x0CsbgCsdKmN6oNrgwIl5GHm8jllRT_-IHZ7k2zTmamPsF7_fd3POwmlbUdX2DgFD1-MjC0nSFtBnRJl6NIe_NBHfQoZwy-wPva2rvokjJO0AaqyEhSmVQl1RrKPPojRaZVvS3JCoIETOmunoIBJxsr9fZr-MONrUP9PYa9lLG2_I9lLulWLne5Sz1nyRNEujUIDgA9papHnb8caZe9vv4-jcLg3CqBsmb-Y4mgVXZqxGQ5gPNmQaxu8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما هم فکر می کنید این بنده خدا و این بندگان خدا، ساده اند؟ یا من تنهام؟</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/mohsentavoosiseo/744" target="_blank">📅 09:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-743">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">چطوری بعضی ها خوش شانسن یا مهره مار دارند و همه جا سریع کلی آشنا و رفیق پیدا میکنن؟
در ادامه دو ویس بالا
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/mohsentavoosiseo/743" target="_blank">📅 18:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-742">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/mohsentavoosiseo/742" target="_blank">📅 17:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-741">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">چرا اگهی میذارن استخدام نمیکنن؟
😏
چرا حقوقو زده انقدر کم با این همه وظیفه؟
😒
چرا همه تخصص ها رو باهم میخواد؟
😒
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/mohsentavoosiseo/741" target="_blank">📅 17:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-740">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هیچ اشکالی نداره مدام request index بدی تو سرچ کنسول. گوگلم مشکلی نداره.
ولی حرف من اینه که الکی داری خودتو خسته می کنی. دست و پا زدن الکیه و نهایتا نتیجه زحمتت ریست میشه.
مشکل جای دیگست:
https://t.me/mohsentavoosiseo/737
https://t.me/mohsentavoosiseo/739
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/mohsentavoosiseo/740" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-739">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/mohsentavoosiseo/739" target="_blank">📅 17:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-738">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سایت های ابزار تحقیق کلمات کلیدی خارجی مثل mangools و keywordtool و ایرانی ها، از کجا دارن search volume (تعداد جستجوی کلمات) در ماه رو میدن؟
چرا دیتاشون باهم گاها خیلی فرق داره؟ چرا نمیشه به فرمول رسید؟
پی نوشت:
میگم نمی تونی بفهمی منظورم عدد دقیق و حتی حدودی هست. وگرنه ابزار ها میدن همشون. سادست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/mohsentavoosiseo/738" target="_blank">📅 17:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-737">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">چرا التماس کردن برای ایندکس شدن درست نیست؟
سایت من لیاقت ایندکس شدن داره؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/mohsentavoosiseo/737" target="_blank">📅 17:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-736">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سوال یکی از شرکت کنندگان دوره از پشتیبان:  من نیاز به بررسی کلمه کلیدی باتری یو پی اس از سمت‌ پشتبان رو دارم. در واقع میخوام بدونم ویدئوهایی که دیدم درست ازشون یاد گرفتم یا نه  سرچ ولیوم این کلمه رو ۲۱۰ پیدا کردم و kd رو ۱۲٪ همچین lps برابر ۲۸ میباشد دقت کلمه…</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/mohsentavoosiseo/736" target="_blank">📅 16:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-735">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سوال یکی از شرکت کنندگان دوره از پشتیبان:
من نیاز به بررسی کلمه کلیدی باتری یو پی اس از سمت‌ پشتبان رو دارم. در واقع میخوام بدونم ویدئوهایی که دیدم درست ازشون یاد گرفتم یا نه
سرچ ولیوم این کلمه رو ۲۱۰ پیدا کردم و kd رو ۱۲٪ همچین lps برابر ۲۸ میباشد دقت کلمه کلیدی که بین عدد یک تا سه در گوگل خودمان باید شماره گذاری میکردیم من سه رو دادم. تحلیلم این است که در این کلمه بیشتر باید هزینه off page کرد اگر یک محتوای بی عیب و نقص و تمامی موارد تکنیکال رعایت شده باشد در بهترین حالت رتبه ۸ به بعد رو بگیریم .
ممنون میشم راهنمایی کنید که این داده ها و تحلیل تا چه حدودی درست هست
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/mohsentavoosiseo/735" target="_blank">📅 16:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-733">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/mohsentavoosiseo/733" target="_blank">📅 13:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-732">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یک دوستی دارم که همیشه فکر میکنه من یه تکنیکی بلدم که انجام میدم سایت ها رشد میکنن. هربار فکر میکنه دارم میپیچونمش و نمیخوام بهش یاد بدم!  همیشم این رو مثال میزنه. این برای سایتی هست که من فقط یک ساعت مشاوره و راهکار دادم. اوایل فوریه. حدودا یک ماه قبل از…</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/mohsentavoosiseo/732" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-731">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahP8-NJq4PJQhgaP2RxivkyP9cQBTm-VfJxi0sO_HP4I9RLkPhLU_eMDitKoVIwjTrz9YkIFdw5BbzU5s3BJO_uDnh4RDg4dv9JMiE_7XYJum59KOLQx-VYt4-T8VkosIkPwTX-HsIFvDJEcQcznzskXTFp7PC6DIeBFrcqekq24EtDHMddFc8N5IX1qmK9ld3YJYdMBmN-_bK6F9Xd6JP-FA-0SQiS4m6c--YCBmIQLn-_wgdTbvvhee6maFG612acFPVKlpn8SmN6ijv8TUvjPbaCpA802NO6qknTsbusALCv-nEirBd6_eQ4W5dskqpxrmOAHppTO-b2PnC7rwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک دوستی دارم که همیشه فکر میکنه من یه تکنیکی بلدم که انجام میدم سایت ها رشد میکنن. هربار فکر میکنه دارم میپیچونمش و نمیخوام بهش یاد بدم!
همیشم این رو مثال میزنه. این برای سایتی هست که من فقط یک ساعت مشاوره و راهکار دادم. اوایل فوریه. حدودا یک ماه قبل از جنگ دوم(اسفند).
بازار آمریکاست و زبان انگلیسی. و فعلا هم خدماتش در یک ایالت هست فقط.
محتوای صفحات تولید شده هم اتوماتیک به کمک AI و ابزار ها هستند.
من فقط گفتم طبق این اصول باید این تعداد صفحه بسازی. لندینگ نداشت! کیورد ریسرچ نداشت! یه صفحه نخست بود و پنج تا صفحه دلخواه به سلیقه مدیریت!
همین! من تکنیک نزدم! تو سئو کار مفت نداریم. برای همین رشد اتوماتیک هم کلی زحمت نیروی انسانی و تحلیل وبررسی مداوم کشیده شده.
صفحه بساز! (بعد از کیورد ریسرچ)
همین! صفحه با AI و اتوماتیک ولی آبرومند و خوب بسازی، بهتر از اینکه نسازی!
این سایت هم رشد کرد تا جایی که رقابت اجازه میداد. یه سقفی داره. بعد باید دست به دامن Off-Page بشی.
هم تو دوره مفصل یاد دادم. هم رایگان اینجا دو ساعت و نیم. ضبط 2018 هست. الان در نیمه دوم 2026 هم همینه:
mohsentavoosi.com/200
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/mohsentavoosiseo/731" target="_blank">📅 13:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-729">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">لینک رویداد چند روزه رایگان و آنلاین گوگل درباره AI Agent اینه. این رو گفتم میبینم برای محکم کاری، بعد ضبط رو شروع میکنم:
https://www.kaggle.com/competitions/5-day-ai-agents-intensive-vibecoding-course-with-google?registerForCourse=true
ولی معمولا پرت زیاد داره طبق معمول. یک ربع مفید یا یک دید و ابزار بهتر ازش دربیارم کافیه برام.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/mohsentavoosiseo/729" target="_blank">📅 12:25 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
