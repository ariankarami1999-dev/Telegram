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
<img src="https://cdn4.telesco.pe/file/HmsxHDhPuocH5cLFOPCvFIc55pEw_CRRkdzsNxfnSnEqjy7OpHOSuwlEsUBkh67PqGqU5hDTkl4rB5Q9vxXvKMKLv6LqdcxscMulP84h2KNLgXkBhII4fIHBEoz1bHjLxN3jKjFok8KYAgJ6DswJpwAQGuE3X456q8qNPTr0fEp0qPuZfRDvp5K1fvhL7yCj8ht_EGzmLjZWHAXstADl1wzS8KH97mDIk2QsXWZsT0CW8vECZLYrFntijYp8NVViu7BZlklop2DsL_fMfifldgiuXCH8VacErZ9jHEUREpL9LIwK6Ynzkau5UXtsHtGw8p86lEidJ4WEpuw6G_WKZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.61M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 03:23:56</div>
<hr>

<div class="tg-post" id="msg-658279">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
صداوسیما: در حمله خصمانه تروریست‌های آمریکایی، دو تن از اهالی کرگان شهرستان میناب بر اثر ترکش پرتابه‌ها زخمی و به بیمارستان میناب منتقل شدند
🔹
هم اکنون آرامش در شهرستان های بندر عباس حاکم است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/658279" target="_blank">📅 03:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658278">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
صداوسیما: تعدادی از شهروندان در حملات آمریکا به منطقه کرگان شهرستان میناب به شهادت رسیدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/akhbarefori/658278" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658276">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
وال استریت ژورنال اولین کد عقب نشینی آمریکا را صادر کرد
وال استریت ژورنال به نقل از مقامات آمریکایی:
🔹
ترامپ به دستیارانش دستور داد از طریق میانجی های قطری این پیام را به تهران منتقل کنند که این حملات واکنشی به حادثه پهپادی بود که نزدیک بود خدمه بالگرد آپاچی را بکشد، نه شروع یک جنگ تمام عیار./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/akhbarefori/658276" target="_blank">📅 03:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658275">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
مرحله اول عملیات‌های تهاجمی موشکی و پهپادی هوافضای سپاه انجام شد
🔹
پراکندگی مبدا شلیک‌ها و فراگیری بانک اهداف، جزو مهمترین ابداعات عملیاتی سپاه پاسداران در مرحله اول عملیات امشب است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/akhbarefori/658275" target="_blank">📅 03:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658274">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
تسنیم: ایران به تجاوزها پاسخ نظامی می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/akhbarefori/658274" target="_blank">📅 03:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658273">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای ترامپ: آتش‌بس با ایران، نقض‌شده‌ترین و ناقض‌ترین آتش‌بس در تاریخ جهان بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/akhbarefori/658273" target="_blank">📅 03:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658272">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
عقب نشینی دوباره ترامپ پس از مقاومت قدرتمند نیروهای نظامی ایران  ادعای ترامپ در گفتگو با شبکه فاکس‌نیوز:
🔹
ایرانی‌ها از من درخواست کرده‌اند که بمباران را متوقف کنم. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/akhbarefori/658272" target="_blank">📅 03:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658271">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
عقب نشینی دوباره ترامپ پس از مقاومت قدرتمند نیروهای نظامی ایران  ادعای ترامپ در گفتگو با شبکه فاکس‌نیوز:
🔹
ایرانی‌ها از من درخواست کرده‌اند که بمباران را متوقف کنم. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/658271" target="_blank">📅 03:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658270">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ترکیب تیم ملی والیبال ایران مقابل برزیل
🔹
ساعت ۰۲:۳۰
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/658270" target="_blank">📅 03:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658269">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای ترامپ به فاکس نیوز: حملات شامل ۴۹ موشک تاماهاوک بود و از شب گذشته شدیدتر است #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/658269" target="_blank">📅 03:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658268">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: اسرائیلی‌ها در این حملات به ایران نقشی نداشته‌اند/انتخاب #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/658268" target="_blank">📅 02:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658267">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ترامپ به فاکس نیوز: بمباران ایران به زودی متوقف خواهد شد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/658267" target="_blank">📅 02:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658266">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
عقب نشینی دوباره ترامپ پس از مقاومت قدرتمند نیروهای نظامی ایران  ادعای ترامپ در گفتگو با شبکه فاکس‌نیوز:
🔹
ایرانی‌ها از من درخواست کرده‌اند که بمباران را متوقف کنم. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/658266" target="_blank">📅 02:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658265">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
عقب نشینی دوباره ترامپ پس از مقاومت قدرتمند نیروهای نظامی ایران
ادعای ترامپ در گفتگو با شبکه فاکس‌نیوز:
🔹
ایرانی‌ها از من درخواست کرده‌اند که بمباران را متوقف کنم.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/658265" target="_blank">📅 02:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658264">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
معاون سیاسی و امنیتی استانداری بوشهر:  یک منطقه در ارتفاعات در شهرستان دشتی مورد هدف قرار گرفته که بدلیل سخت گذر بودن منطقه هنوز منشا آن مشخص نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/658264" target="_blank">📅 02:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658263">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
تنگه هرمز تا اطلاع ثانوی بسته می‌شود  نیروی دریایی سپاه پاسداران انقلاب اسلامی:
🔹
در پی نقض مکرر شرایط آتش‌بس توسط دشمن آمریکایی، تنگه هرمز تا اطلاع ثانوی مسدود می‌شود.
🔹
هشدار می‌دهیم هیچ شناوری از لنگرگاه خود در خلیج فارس و دریای عمان حرکت نداشته باشد. نزدیک…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/658263" target="_blank">📅 02:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658262">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
موج دوم حملات تجاوزکارانه آمریکا به جنوب ایران
🔹
یک مقام آمریکایی بامداد پنجشنبه به شبکه «فاکس نیوز»: «حملات نظامی آمریکا علیه ایران ادامه دارد».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/658262" target="_blank">📅 02:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658261">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
هشدار آمریکا به اتباعش در عراق
🔹
وزارت خارجه آمریکا بامداد پنجشنبه به شهروندان این کشور در عراق توصیه کرد که آماده باشند و شیوه‌نامه‌های امنیتی را به دلیل خطرات احتمالی رعایت کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/658261" target="_blank">📅 02:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658260">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64da998bb1.mp4?token=CAEp8VkrH3KqQgtniJx3-2AN6xLNL_yeEhR90c1j1zgxmRz7ftboCRIFxKLJpnPY9KHdMKJl76b8Uq-7fgSJwuw2YEH-65eLNAeDekUJDUqbY-3L8ybAgl8WOa9_PcaxQEK2NoA8-8PuUW638ZZyxxJ-k7p5OTvAl4SNKYmdDx_bYAgTw-8Kjiy-vPnP8W7n2jKLckin5e7V2WgU08OlVAnDm2lDX8DYlRUBGFiqCrl1bZKhP-cS47yFHf2bD3iVQNWlbEkyMNHqL50ruo_UKUIiJGiIQuKlLRK_GZEV0Yb7fyZx5u1NQ1DVmRrGgWxzAEAmee8_uq5arUM-Y7-nyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64da998bb1.mp4?token=CAEp8VkrH3KqQgtniJx3-2AN6xLNL_yeEhR90c1j1zgxmRz7ftboCRIFxKLJpnPY9KHdMKJl76b8Uq-7fgSJwuw2YEH-65eLNAeDekUJDUqbY-3L8ybAgl8WOa9_PcaxQEK2NoA8-8PuUW638ZZyxxJ-k7p5OTvAl4SNKYmdDx_bYAgTw-8Kjiy-vPnP8W7n2jKLckin5e7V2WgU08OlVAnDm2lDX8DYlRUBGFiqCrl1bZKhP-cS47yFHf2bD3iVQNWlbEkyMNHqL50ruo_UKUIiJGiIQuKlLRK_GZEV0Yb7fyZx5u1NQ1DVmRrGgWxzAEAmee8_uq5arUM-Y7-nyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار شهید طهرانی مقدم، پدر صنعت موشکی ایران: جمهوری اسلامی تسلیم هیچ گردن‌ کلفت و هیچ آدم قلدر بی‌فرهنگی مثل آمریکایی‌ها نخواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/658260" target="_blank">📅 02:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658259">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
گروه هکری حنظله: بخش بزرگی از موج اول و دوم حملات ارتش تروریست آمریکا تا این لحظه به‌خاطر عملیات واحدهای جنگ الکترونیک مختل شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/658259" target="_blank">📅 02:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658258">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
نخستین مرحله تجاوز آمریکا به ساحل جنوبی ایران بدون دستاورد در حال پایان است
🔹
برخی منابع مطلع از امکان توسعه حملات کور ارتش آمریکا برای عبور از مخمصه کنونی خبر داده‌اند./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/658258" target="_blank">📅 02:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658257">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
تردد هر نوع شناور در تنگه هرمز ممنوع و متوقف شد  قرارگاه مرکزی حضرت خاتم‌الانبیا(ص):
🔹
از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت
🔹
در ادامه شرارت های…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/658257" target="_blank">📅 02:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658255">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
پاکستان: به آمریکا اعلام کردیم که دیگر دست از تلاش برای میانجیگری برمی‌داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/658255" target="_blank">📅 02:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658254">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxPpXi8BL2uLeLUBIsVwyzWdhr1XMiKBz2AEPIYdrfGX88eYyaUsFHyIMw0LVbmrXJNLP2xeAsOHSIdwaqOsP54PDrLiDFDqgFOyk6kZ3e4LAxIfwTrCba4G-mvdl-tkSYNb1-3dwPrTxpLoF5X5UiQwcjzjIYwly_kciO23DpEpVZUYCycGlLRXDqUQNf7Wh9zxITYAyho04NlEXHlkyqaXtTsdWI7GIypMd4CKsenK1JDPlmHiA2GxRw_rEPhhUjtj3WRTnx4e9UAVH4LWv1A89EnWTvNNZZaBoGluSuN1q2atireEqt8rPUfg2ICtf0PdPeuY_JYjNFk9ZrdI3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیب تیم ملی والیبال ایران مقابل برزیل
🔹
ساعت ۰۲:۳۰
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/658254" target="_blank">📅 02:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658253">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
صداوسیما: صداهای شنیده شده در رباط کریم مربوط به صدای پدافند است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/658253" target="_blank">📅 02:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658252">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
دو فروند کشتی متخلف که قصد عبور غیر قانونی از تنگه هرمز را داشتند، مورد اصابت قرار گرفتند
/ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/658252" target="_blank">📅 02:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658251">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0722735183.mp4?token=Rl44npVJUJ9NLJ0AqPAZszqJx5lhfriVKHr81cW9RPZK-9WjX521qhtP3j0i-HxjWRrWGuPAeYVHkcJ28QUfEYPyOomGkARCj1nVh82zJIzzDrRSRIdk5tVEG1nPbDfSgtuCOvD6jYfiynArO9cYoPDOdM1GF2L82Cu7yWL93bt8tph6b_TPN22kIQk9KM2Tou-71UYjxvHXKOqic4CS7wtTEWmnKgomZ8QpXyKzbAApfTFurNh8_FKKkhyZQC2dbqblzTfEuXU16XtpBxIPXN8vnDgeqHY30-51TODWv5VIBX3zaEpgIoAmflJGgsvj8-OFJHQeLLjBj38v_FFoQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0722735183.mp4?token=Rl44npVJUJ9NLJ0AqPAZszqJx5lhfriVKHr81cW9RPZK-9WjX521qhtP3j0i-HxjWRrWGuPAeYVHkcJ28QUfEYPyOomGkARCj1nVh82zJIzzDrRSRIdk5tVEG1nPbDfSgtuCOvD6jYfiynArO9cYoPDOdM1GF2L82Cu7yWL93bt8tph6b_TPN22kIQk9KM2Tou-71UYjxvHXKOqic4CS7wtTEWmnKgomZ8QpXyKzbAApfTFurNh8_FKKkhyZQC2dbqblzTfEuXU16XtpBxIPXN8vnDgeqHY30-51TODWv5VIBX3zaEpgIoAmflJGgsvj8-OFJHQeLLjBj38v_FFoQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرماندار عسلویه: هرگونه اصابت به مجتمع‌های پتروشیمی را تکذیب می‌کنم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/658251" target="_blank">📅 02:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658250">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: میانجیگران قطری همچنان در ایران هستند
🔹
شبکه سی‌ان‌ان بامداد پنجشنبه به نقل از «یک منبع دیپلماتیک» گزارش داد، در حالی که آمریکا دور جدیدی از حملات به ایران را آغاز کرده است، هیات قطری که چهارشنبه برای ملاقات با مذاکره‌کننده‌گان ایرانی به تهران سفر کرده بود، همچنان در این کشور است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/658250" target="_blank">📅 02:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658249">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
تردد هر نوع شناور در تنگه هرمز ممنوع و متوقف شد
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص):
🔹
از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت
🔹
در ادامه شرارت های آمریکای جنایتکار و با توجه به آغاز حملات ارتش متجاوز آن کشور به برخی از مناطق جنوب در استان هرمزگان، از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت.
🔹
ادعای آمریکا مبنی بر عبور کشتی از تنگه یاد شده تکذیب می شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/658249" target="_blank">📅 02:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658248">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای ترامپ:‌ ما به توافق نزدیک بودیم اما همه چیز کاملاً تغییر کرد. ایران باید انتظار حملات سنگین‌تر و شدیدتری نسبت به سه ماه گذشته داشته باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/658248" target="_blank">📅 02:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658247">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
مشاهدات مردمی در بندرعباس: چند موشک پدافندی به سوی جنگنده آمریکایی شلیک شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/658247" target="_blank">📅 02:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658246">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
رئیس سابق هیات مذاکره کننده آمریکا: فشار نظامی موضع ایران را تغییر نخواهد داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/658246" target="_blank">📅 02:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658245">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
جزئیاتی از سطح درگیری ها در تنگه هرمز
🔹
ایستادگی و آتش گسترده یگان‌های نیروی دریایی سپاه، نیروهای متجاوز آمریکایی را دچار شوک کرده است. آمریکایی‌ها تاکنون بر ۷ نقطه ساحلی تهاجم داشته اند./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/658245" target="_blank">📅 02:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658244">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
گزارش‌های اولیه از حمله به کشتی‌های آمریکایی در تنگه هرمز
🔹
کشتی‌های آمریکایی در نزدیکی تنگه هرمز هدف حملات موشکی و پهپادی نیروهای مسلح ایران قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/658244" target="_blank">📅 02:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658243">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌
♦️
گروه هکری حنظله: واحدهای جنگ الکترونیک و اختلال سیگنال «حنظله» هم‌اکنون درحال مختل‌کردن فعالانه سیستم‌ها و سیگنال‌های دشمن هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/658243" target="_blank">📅 02:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658242">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
روابط عمومی سپاه: درپی تجاوز جنگنده f16 به حریم هوایی خلیج فارس و شلیک موشک سامانه پدافند هوایی سپاه به سمت آن، جنگنده متجاوز متواری گشت
/ صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/658242" target="_blank">📅 02:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658241">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB1kskml4B8DnmRlaCF77MKv1g94UfxnKB5t0dnQqXnCLYX1Gloyu4r-lJ9lfaWGRN0bQZsHWLlFwCc3mCp1RJt0i17g1Mep50IXVmU7DG_psykqtG1K9u_uikN50xiZNks-1nGerZKZxrfjWSksofbeG_d0WsyiNh3ubmAZgdgOVMQjqTz50U0ftLhXiGSG-QfzF6u4u9elZ-fof14SQRBsIt09PLvV3LtzSFFvJ0hDajOelidgNnKJgPT5_5B8Azu5AvchVnw7nbyOXgemnk38nsiHKaQZOILSMZi8Bq-1lRE8iMHgn1Yqek1zhjiF8cROud0RBrRD8pLVKtonoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هاآرتص: اسرائیل در انتظار حمله موشکی ایران پس از حملات جدید آمریکا به اهدافی در ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/658241" target="_blank">📅 02:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658240">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOGABKRKRwpYxtc4UkFiVAa3t0ud7_LF3QYhCS6L1oL17qFXFOf4ftbNRsm8adM1NsIexTo1K2jkoD-Ud0_-FTPaigon4Ho7vmmfoqWkrIM8FQY8c3ZTHEa94v3DI81Uirlaxu81c2J7FqYJpfCl7uK7P3L3Ye6NfvDyOd3MZ8Z9-BKlQDZqsz-v65KnoV5cyBkSo32jaY0u5-cwvA3OHAbGJILq8d_P9dS1gD_RgbsU49RA_vXcYLMpWm_68xCGzuyC7_1ZG15dKbQFp3PG00PRWBlkX-ZUTcor0_Wc1XvUFyc-KjLNYX7mYZhPkS0z1QupvItPAF3xdd0QZkvhag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلا با ریزش ۲۲۲ دلاری به قیمت ۴۰۳۹ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/658240" target="_blank">📅 02:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658239">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
رسانه‌های اسرائیلی: واشنگتن پیش از آغاز حملات به ایران، به تل‌آویو اطلاع داده بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/658239" target="_blank">📅 01:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658238">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
وزیر خارجه یمن: نسبت به ادامه تجاوز آمریکا به ایران هشدار می‌دهیم
وزیر خارجه دولت یمن (مستقر در صنعاء):
🔹
نسبت به ادامه تجاوز آمریکا علیه جمهوری اسلامی ایران و پیامدهای آن که تهدیدی برای امنیت و صلح بین‌المللی به شمار می‌رود، هشدار می‌دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/658238" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658237">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
شبکه ۱۲ رژیم صهیونیستی: به نظر می‌رسد موج اول حملات به آمریکا پایان یافته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/658237" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658236">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
صدای انفجار در بندرعباس
🔹
دقایقی پیش صدای انفجارهایی مجدد در محدوده شهر  بندرعباس از سوی منابع محلی و ساکنان شهر  گزارش شده است. این حمله مربوط به نیمه شرقی شهر بندرعباس بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/658236" target="_blank">📅 01:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658235">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ادعای کانال کان: به گفته منابع امنیتی، اسرائیل در این مرحله در حملات مشارکت ندارد/انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/658235" target="_blank">📅 01:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658234">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای نیویورک تایمز: چشم‌انداز پیشرفت دیپلماتیک در مذاکرات آمریکا و ایران زمانی تیره‌تر شد که یک هیئت میانجی‌گر قطری عصر چهارشنبه بدون هیچ پیشرفتی در مذاکرات، تهران را ترک کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/658234" target="_blank">📅 01:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658233">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
گزارش‌های اولیه از حمله به کشتی‌های آمریکایی در تنگه هرمز
🔹
کشتی‌های آمریکایی در نزدیکی تنگه هرمز هدف حملات موشکی و پهپادی نیروهای مسلح ایران قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/658233" target="_blank">📅 01:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658232">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
خبرنگار المیادین: منطقه تنگه هرمز شاهد درگیری و تبادل آتش است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/658232" target="_blank">📅 01:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658230">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
وضعیت اینترنت ایران پایدار است؛ نشانه‌ای از اختلال سراسری جدید مشاهده نمی‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/658230" target="_blank">📅 01:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658229">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ادعای فاکس نیوز به نقل از یک مقام ارشد آمریکایی: امشب چندین موج حمله دیگر نیز وجود دارد/انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/658229" target="_blank">📅 01:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658228">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
هم اکنون؛ چند انفجار در قشم شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/658228" target="_blank">📅 01:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658227">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
فرماندار عسلویه هر گونه انفجاری در این منطقه را تکذیب کرد/
ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/658227" target="_blank">📅 01:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658226">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
گزارش‌های اولیه از حمله به کشتی‌های آمریکایی در تنگه هرمز
🔹
کشتی‌های آمریکایی در نزدیکی تنگه هرمز هدف حملات موشکی و پهپادی نیروهای مسلح ایران قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/658226" target="_blank">📅 01:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658225">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
تسنیم: تاکنون خبر هدف قرار گرفتن منطقه پالایشگاهی عسلویه صحت ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/658225" target="_blank">📅 01:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658224">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
فرماندار کنگان حمله به بندر کنگان را تکذیب کرد و گفت صدا شنیده شده اما هنوز مشخص نیست منشا ان کجا هست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/658224" target="_blank">📅 01:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658223">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
گروه هکری حنظله: ما هر حرکت و هر جلسه مخفی دشمن را دیده و شنیده‌ایم. به‌زودی دشمن خواهد فهمید یک سال جمع‌آوری حساس‌ترین اطلاعات چه معنایی دارد
🔹
ما منتظر حماقت شما هستیم، زمانی که نتایج یک سال جمع‌آوری اطلاعات فاش خواهد شد. به جهنم خوش آمدید!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/658223" target="_blank">📅 01:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658222">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
هدف قرار گرفتن رادار آمریکا در اربیل توسط سپاه پاسداران
خبرنگار اسپوتنیک:
🔹
سپاه پاسداران ایران یک رادار امریکایی را در اربیل هدف حملات توپخانه‌ای یا موشکی قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/658222" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658221">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ایرنا: صدای چند انفجار از شهر بندرعباس در حوالی فرودگاه و پایگاه هوایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/658221" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658220">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mus9hIA_VyssZxxrRDbrCh2Y0rpzbWHeIBPhK951Tb3u28L7tC-tqChRKHTaaZ8ztd3KkRxfg4KvparJ239TdM26PTJcSud7qJTvHV5m4vVySyVnyoTuKsq1gNtc8r4fodeh21TxX7vCXv3WjPKlC7v22bxqd1d2SZUQk73udOg9E4Cong6B4mR6HIgNfWEnpM7FaBiKA3AWWxRAiEhdmk6FwXCtf60vBsKXf8tgHrC-lCHS2mOWr2FBP9J_QvCwnHh-BZEaK-0aNpP8ldAttYtaiyQNiBOyoBXfK_iCLKptgEmwdLVaS0aQh-OYVLMUest0_ojYLMizPd2uTr7IDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صداوسیما: برخی منابع از رهگیری یک پرتابه کروز دشمن در عسلویه خبر می دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/658220" target="_blank">📅 01:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658219">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
تا دقایقی دیگر پیام سخنگوی قرارگاه مرکزی خاتم الانبیاء(ص) در پی جنایت آمریکا و نقص آتش‌بس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/658219" target="_blank">📅 01:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658218">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
حمله به اهدافی آمریکایی در شمال عراق
منابع عراقی:
🔹
پایگاه آمریکایی الحریر در اربیل (شمال عراق) هدف موشکی از ایران قرار گرفت
🔹
وبگاه المعلومه عراق نیز خبر داد، ایران یک رادار آمریکایی در اربیل (مرکز کردستان عراق) را منهدم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/658218" target="_blank">📅 01:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658217">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال، به نقل از پنتاگون: این حملات اقدامی از دیپلماسی قهری با هدف وادارکردن ایران به دادن امتیاز در میز مذاکره است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/658217" target="_blank">📅 01:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658216">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
دقایقی پیش نقاطی در عسلویه هدف حمله دشمن قرار گرفت/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/658216" target="_blank">📅 01:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658215">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ رژیم: یک مقام ارشد آمریکایی گفت که تمام اهداف مورد حمله در جنوب ایران قرار دارند
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/658215" target="_blank">📅 01:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658214">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
تسنیم: هم اکنون یک کارخانه پتروشیمی متعلق به مجتمع گاز پارس جنوبی در عسلویه بمباران شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/658214" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658213">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
خبر فعالیت پدافند در شیراز مورد تایید نیست
🔹
دقایقی قبل برخی رسانه‌ها و خبرنگاران اعلام کردند؛ پدافند شیراز فعال شده است. در شیراز این خبر تاکنون از سوی مسئولان مربوطه تایید نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/658213" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658212">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
کانال ۱۲ رژیم به نقل از مقامات آمریکایی: منتظر واکنش ایران هستیم که احتمالاً پایگاه‌های آمریکایی را هدف قرار دهد، همانطور که در شب سه‌شنبه رخ داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/658212" target="_blank">📅 01:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658211">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
بیانیه سنتکام درباره نقض آتش‌بس با ایران
🔹
نیروهای فرماندهی مرکزی آمریکا امروز ساعت ۵:۱۵ بعد از ظهر به وقت شرق آمریکا، به دستور فرمانده کل قوا، حملات دفاعی بیشتری را علیه چندین هدف در ایران آغاز کردند. این حملات در پاسخ به تجاوز بی‌اساس و مداوم ایران انجام…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/658211" target="_blank">📅 01:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658210">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
سنتکام اعلام کرد حملات خود علیه ایران را آغاز کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/658210" target="_blank">📅 01:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658209">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
یک منبع موثق در استانداری هرمزگان: انفجارهایی ناشی از اصابت پرتابه در قشم و هنگام اتفاق افتاده که همگی ماهیت نظامی دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/658209" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658208">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ea7833987.mp4?token=GLRQwSB21s4nc_0UeR25Jsj-dwhFacaHa8wvwtsfpC8wAKOntsheuweVXehiX3xlgPX0f4ilybkx8XxbB8XajegPCbYVvzZKSWj4GBzujjmGc_W2_K-T1pLKMPCcNUF-mrwjoTNBrh3-G-AtBETIZKVCl3fpols6djspHkrdmfCijgH-yLyBKoQwped04X_tW3zE4lAdfUgT5prweyeoYrfBNxhEYKdkiLNll9cE2YwVJjnsJ9K7vLAwA9o-Zkwj0-pipNpGXulyy-91nWsvBGcioIJvJD9T9r-Yr5Rw5TyA6qzsOJ7Ix-dr-_BIvmNMFMoXgNtFbNd_xbxDjGlUDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ea7833987.mp4?token=GLRQwSB21s4nc_0UeR25Jsj-dwhFacaHa8wvwtsfpC8wAKOntsheuweVXehiX3xlgPX0f4ilybkx8XxbB8XajegPCbYVvzZKSWj4GBzujjmGc_W2_K-T1pLKMPCcNUF-mrwjoTNBrh3-G-AtBETIZKVCl3fpols6djspHkrdmfCijgH-yLyBKoQwped04X_tW3zE4lAdfUgT5prweyeoYrfBNxhEYKdkiLNll9cE2YwVJjnsJ9K7vLAwA9o-Zkwj0-pipNpGXulyy-91nWsvBGcioIJvJD9T9r-Yr5Rw5TyA6qzsOJ7Ix-dr-_BIvmNMFMoXgNtFbNd_xbxDjGlUDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون ـ پرواز جنگنده ارتش جمهوری اسلامی ایران بر آسمان تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/658208" target="_blank">📅 01:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658207">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
صدای چند انفجار در بندر کرگان نیز شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/658207" target="_blank">📅 01:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658206">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
یک منبع موثق در استانداری هرمزگان: انفجارهایی ناشی از اصابت پرتابه در قشم و هنگام اتفاق افتاده که همگی ماهیت نظامی دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/658206" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658205">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
‌
کانال ۱۲ اسرائیل: ارتش اسرائیل آماده پیوستن به ایالات متحده در کارزار جدید علیه ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/658205" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658204">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
صداوسیما: شنیده شدن صدای انفجار در بندرعباس هم اکنون
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/658204" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658203">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
خبرگزاری صدا و سیمای مرکز فارس: سپاه شهرستان مهر: بر خلاف برخی اخبار منتشره، حمله دشمن به این شهرستان یا اطراف آن تایید نمی‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/658203" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658202">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
صداوسیما: شنیده شدن صدای انفجار در بندرعباس هم اکنون
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/658202" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658201">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
افزایش قیمت نفت به سمت ۹۵ دلار
🔹
همزمان با آغاز دور جدیدی از جنگ افروزی آمریکا علیه ایران، قیمت نفت آمریکا از مرز ۹۰ دلار گذشت.
🔹
قیمت نفت برنت هم به سمت ۹۵ دلار در حال افزایش است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/658201" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658200">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZZL3cmo-NxNtjhSXx-0PkwyxOoBlIH2EkbHKvGswOSw8_SgnIcR-ntngcNMCI7OLuWejqBjPAI5RF6XJRN5Qa5QLHmH3tHTlG2mWOoR0qZoK_39tWIsev74VtGr_hKlAO6MQt8d5orWTDJhzFYW0kry6IO8P4D11K6MIlxvP-Upw7TTih-Pu59ntYzFxEfXSph5LFCCJ-Uhb4Ir9UXDk0z5ll-o8NbOD3gzZqZPfyA6DKx9B_yjUsD0NkYw1ARIqlAmv982Co_TMfUr1YzbokEbcZ_5hIpsEnzxV_X7kzsekGMTBAT_umtSyG-zLDdhdlO4fITGdjw6U5i5tnzqZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
או שנשלח לכם את המוות
או שתמותו מפחד המוות
یا مرگ را به سراغتان می‌فرستیم
یا از ترس مرگ، خواهید مرد
#WillPayThePrice
‎
#هزینه_خواهید_داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/658200" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658199">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
آمریکا نقض دوباره آتش‌بس و حمله به ایران را تایید کرد
🔹
یک مقام ارشد آمریکایی بامداد پنجشنبه به رسانه‌های صهیونیستی گفت که حملات تجاوزکارانه‌ای به چند نقطه در ایران در حال انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/658199" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658198">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7mLe4L4XuaNmfrqyNofcr2QX4Q7--OsdVFSjNtCoRcQA5w7Wn95UrrNP5SeQIR7mR9ZTOudrO73kwXLpxpEqHy8fpZZSPYsuKTu3A9z4HBDS6FeTSlNNsbwNjBD5OSGdhizGLCc6L09j5gyCJOUgJgZItgZ4_aNvO3tMMOkY9c7z5wdtvbg796DJRMoNMQ63bEQkLAapmDqUfa54yUH38S5Ta_FrLyNvIlIYUschPERb9dXWXzaW9JfZzXqEicQfw09Dl13pje-It1wcjjqJ4MuMUjfabXXrUNG9c9CkLEdTUys5uRuGm-NXe2cnAfdzkjhgThp4SfKcn69DvBzhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سنتکام اعلام کرد حملات خود علیه ایران را آغاز کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/658198" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658197">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
تسنیم: تاکنون صدای ۴ انفجار در سیریک شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/658197" target="_blank">📅 01:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658196">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
گروه هکری حنظله: ما هر حرکت و هر جلسه مخفی دشمن را دیده و شنیده‌ایم. به‌زودی دشمن خواهد فهمید یک سال جمع‌آوری حساس‌ترین اطلاعات چه معنایی دارد
🔹
ما منتظر حماقت شما هستیم، زمانی که نتایج یک سال جمع‌آوری اطلاعات فاش خواهد شد. به جهنم خوش آمدید!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/658196" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658195">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
صداوسیما: پدافند عسلویه فعال شده است
🔹
در جنوب استان فارس تا الان حمله دشمن صورت نگرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/658195" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658194">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
تکذیب انفجار در جزیره کیش و قشم؛ صدای انفجار در میناب و سیریک
🔹
بررسی‌ها نشان می‌دهد که تا این لحظه اخبار مربوط به صدای انفجار در جزایر کیش و قشم صحت نداشته و صداهای شنیده شده مرتبط با درگیری در خلیج‌فارس است.
🔹
براساس گزارش منابع محلی، دقایقی پیش صدای انفجار در اطراف میناب و سیریک شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/658194" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658193">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
هشدار مقام سیاسی امنیتی ایرانی به کشورهای عربی
🔹
یک منبع بلندپایه امنیتی-سیاسی ایرانی به شبکه المیادین: «همان‌طور که پیش‌تر هشدار داده شده بود، هرگونه اقدام نظامی علیه ایران توسط هر کشوری، چه در خاک خود آن کشور و چه در حریم هوایی آن، به منزله مشروعیت‌بخشی برای تبدیل شدن به هدفی برای جمهوری اسلامی ایران تلقی خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/658193" target="_blank">📅 01:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658192">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در محدوده شهر میناب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/658192" target="_blank">📅 00:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658191">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در سیریک /مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/658191" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658190">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
گزارش منابع عراقی: از فعالیت شدید جنگنده های آمریکایی در شمال عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/658190" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658189">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
شنیده شدن صدای پدافند در غرب تهران/مهر
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/658189" target="_blank">📅 00:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658188">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6976eb7c.mp4?token=NoDA_WbTd6PMlvTXDZA3S6enqe6767Fo-CuR-47B1T88Dv7P036oDrGrJY-7VgMBNNU4RfEeCZZjLIim4VgR1VsiWOe67n8qKSZOwCRxOX9gpiTsCmiqKtgtwT4fq4zJ1VqMstkWDW_qwEIMF9PI702yL0BP-CXRNnnAPyqaqMZcephDmfRG_a_ILGONSYDEypdeQ3BfO6cyg9T3xCAMXttK5a-IgnvsrZE7lIOpq7eMVOlvdBsEFlEZbtHluAjeYuPLTBSSFpo0h-4kUaG7jx3NkWWINYkIFMFHHlGN0daOuTQfjQXPF7WnkAcZdRnnTB99g8JiGYy-joIMK6DbPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6976eb7c.mp4?token=NoDA_WbTd6PMlvTXDZA3S6enqe6767Fo-CuR-47B1T88Dv7P036oDrGrJY-7VgMBNNU4RfEeCZZjLIim4VgR1VsiWOe67n8qKSZOwCRxOX9gpiTsCmiqKtgtwT4fq4zJ1VqMstkWDW_qwEIMF9PI702yL0BP-CXRNnnAPyqaqMZcephDmfRG_a_ILGONSYDEypdeQ3BfO6cyg9T3xCAMXttK5a-IgnvsrZE7lIOpq7eMVOlvdBsEFlEZbtHluAjeYuPLTBSSFpo0h-4kUaG7jx3NkWWINYkIFMFHHlGN0daOuTQfjQXPF7WnkAcZdRnnTB99g8JiGYy-joIMK6DbPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر جنگ آمریکا: لازم باشد با بمباران مذاکره می‌کنیم
«پیت هگزث» حین بازدید از مقر فرماندهی مرکزی ارتش آمریکا (سازمان تروریستی سنتکام) مدعی شد:
🔹
اگر لازم باشد با بمب مذاکره می‌کنیم... ما در این کار خیلی خوب هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/658188" target="_blank">📅 00:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658187">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4897c1e3a.mp4?token=OwaEQka_3hTly2RjghbWFqwRoS6iWaHvVKC6DpHB5okv8mlcCqeJiUSJDAjzWQRmD8EjWrkgINesPo8TtdxAoycz18PG71ch_1ZZK0XsBZ893HBxl1a1abMQOls_fuNf1j14Oh1oOGyXJmR6J2m5E3pfUeFNOXtfsvgxP0FTUY0fc7XchKmkSXxDo98VRYfoaI6OzqUehulVpRH_V0UeVtIKAo0lzlmjdJlc2Tsoi6FePRXJ3hMcyvQC3n1JiLkware50aWNYNVB-qCg0RnbV8jIq3imtjPHUxbVQm7n7P6i5lEp3jiKLQBJCRV1kmV8zGLnOIha-gK6gk4EJRQJWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4897c1e3a.mp4?token=OwaEQka_3hTly2RjghbWFqwRoS6iWaHvVKC6DpHB5okv8mlcCqeJiUSJDAjzWQRmD8EjWrkgINesPo8TtdxAoycz18PG71ch_1ZZK0XsBZ893HBxl1a1abMQOls_fuNf1j14Oh1oOGyXJmR6J2m5E3pfUeFNOXtfsvgxP0FTUY0fc7XchKmkSXxDo98VRYfoaI6OzqUehulVpRH_V0UeVtIKAo0lzlmjdJlc2Tsoi6FePRXJ3hMcyvQC3n1JiLkware50aWNYNVB-qCg0RnbV8jIq3imtjPHUxbVQm7n7P6i5lEp3jiKLQBJCRV1kmV8zGLnOIha-gK6gk4EJRQJWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بروجردی، عضو کمسیون امنیت ملی مجلس: به کشورهای منطقه گفته‌ایم اگر آمریکا دست از پا خطا کند، اهدافش در منطقه مورد حمله قرار خواهد گرفت/ زدیم، می‌زنیم، دست از پا خطا بکنند باز هم خواهیم زد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/658187" target="_blank">📅 00:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658186">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
صدای جنگنده‌ در برخی نقاط لرستان مربوط به پروازهای خودی است/ایرنا
گزارش لحظه‌ای تحولات امشب به روز می‌شود
👇
khabarfoori.com/fa/tiny/news-3222172</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/658186" target="_blank">📅 00:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658185">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
هم اینک صداهایی از دور در کیش شنیده می شود که منشا آن مشخص نیست
🔹
به نظر می رسد تحرکاتی با فاصله زیاد از کیش صورت گرفته است./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/658185" target="_blank">📅 00:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658184">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
ادعای وزیر جنگ آمریکا: سنتکام امشب کار زیادی خواهد داشت، چون ترامپ گفته است ما به ایران حمله سنگینی خواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/658184" target="_blank">📅 00:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658183">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
اسرائیل هیوم: شرکت هواپیمایی ایر کانادا تمدید لغو پروازها به اسرائیل را تا ۲۴ اکتبر اعلام کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/658183" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658182">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3669cf2f0.mp4?token=gMZ4QoifOg_elDF06cFsr04rGpZMKdSFiorpx2KPHQSrShwdv_bR7pSs9DXEibaDuSILoKp91Pc3qXi6elUp1YiA4uSpcMQeUwo8x5jHzkPkYN-kXOdTXTZIsHJqQvb40jdJyhhc3oz1_DZ8_FU5X5E2LCbYb_L3WKuXevXe66WSMh3zcpyaVyfgn4e_cwvE72RKRuQARLnwYdRcK_gp87HCxLdSkJjLnLjjnDSH5a2po9xePxoZkjLQYVir6RvA-9KfFpdGkn4AeArZ7yTz865aiUtlDYPokYQDs5ICli30ftgj7vXPYGDGgWDpAg_YCYdt1BLtVsDLlZOjsD_Xjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3669cf2f0.mp4?token=gMZ4QoifOg_elDF06cFsr04rGpZMKdSFiorpx2KPHQSrShwdv_bR7pSs9DXEibaDuSILoKp91Pc3qXi6elUp1YiA4uSpcMQeUwo8x5jHzkPkYN-kXOdTXTZIsHJqQvb40jdJyhhc3oz1_DZ8_FU5X5E2LCbYb_L3WKuXevXe66WSMh3zcpyaVyfgn4e_cwvE72RKRuQARLnwYdRcK_gp87HCxLdSkJjLnLjjnDSH5a2po9xePxoZkjLQYVir6RvA-9KfFpdGkn4AeArZ7yTz865aiUtlDYPokYQDs5ICli30ftgj7vXPYGDGgWDpAg_YCYdt1BLtVsDLlZOjsD_Xjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بروجردی، عضو کمسیون امنیت ملی مجلس: برای آمریکا قبول این حقیقت سخت است که امروز در دنیا چهار قدرت وجود دارد؛ ایران، آمریکا، چین و روسیه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/658182" target="_blank">📅 00:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658181">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ادعای وزیر جنگ آمریکا: ما از آتش‌بس برای توسعه اطلاعات و به‌روزرسانی بانک اهداف خود در ایران استفاده کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/658181" target="_blank">📅 00:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658180">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
فعالیت پدافند هوایی در شهر مُهر استان فارس
🔹
دقایقی پیش مردم در شهر مُهر استان فارس صدایی شبیه انفجار شنیدند.
🔹
پیگیری‌ها حاکی است صدای شنیده شده مربوط به فعالیت سامانه پدافندی در بیرون از شهر است و تا این لحظه هیچ انفجاری در محدوده شهرستان مهر رخ نداده است/ مهر
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/658180" target="_blank">📅 00:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658179">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3618b4bb8e.mp4?token=MqRTDdYtJlh5KgXtuGjDmLT4MUxBoPDKqlBFL5WqWFUcgIIrow1VywZ8rLAJJColYPQjWJDTFOlsfDqau9ktHNQ81_lxjMPMUvaBiTxYpGEUWwUahJUoW98prU4TXu7q1XhKHJb6A_oNM0B2jBWZyT9PmWi02GKk44iGXRPnXPAW3fl5Y3xlE6je53Z7UDvXvZlqlOp-55JoMy6J3jN1tNnmNlpYIyeI-zQo-LxNcL_AVpDcfBwHhEuO85tCp2D_vUTXK2HJ5G0JuGXgWLaTLWBCb886oUEHfYGKEVhgzRefv5mbDKPxHG5sS3N1mn4MRBR0aeOsROaF18yvPYixnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3618b4bb8e.mp4?token=MqRTDdYtJlh5KgXtuGjDmLT4MUxBoPDKqlBFL5WqWFUcgIIrow1VywZ8rLAJJColYPQjWJDTFOlsfDqau9ktHNQ81_lxjMPMUvaBiTxYpGEUWwUahJUoW98prU4TXu7q1XhKHJb6A_oNM0B2jBWZyT9PmWi02GKk44iGXRPnXPAW3fl5Y3xlE6je53Z7UDvXvZlqlOp-55JoMy6J3jN1tNnmNlpYIyeI-zQo-LxNcL_AVpDcfBwHhEuO85tCp2D_vUTXK2HJ5G0JuGXgWLaTLWBCb886oUEHfYGKEVhgzRefv5mbDKPxHG5sS3N1mn4MRBR0aeOsROaF18yvPYixnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بروجردی، عضو کمسیون امنیت ملی مجلس: اگر آمریکا در یک تفاهم محاصره دریایی را برندارد، ما باید محاصره را به جهت حفظ منافع ملی بشکنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/658179" target="_blank">📅 00:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658178">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
سفارت آمریکا در عراق برای اتباع خود اطلاعیه هشدار صادر کرد
‌
سفارت آمریکا در عراق با صدور هشداری برای اتباع این کشور اعلام کرد:
🔹
با توجه به تحولات اخیر منطقه، به شهروندان آمریکایی در عراق توصیه می‌شود که بالاترین سطح هوشیاری و دقت را حفظ کرده و به‌طور مستمر منابع خبری محلی را دنبال کنند.
‌
🔹
احتمال وقوع اختلال در سفرها یا بسته شدن حریم هوایی به‌صورت ناگهانی و بدون اطلاع قبلی وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/658178" target="_blank">📅 00:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658177">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
نماینده مجلس: افزایش هزینه‌های درمان علت عدم پرداخت بیمه‌های تکمیلی است
جعفری‌آذر، عضو کمیسیون اجتماعی مجلس:
🔹
مشکل اصلی بیمه‌های تکمیلی بازنشستگان و شاغلین، توقف خدمات یا عدم پرداخت نیست، بلکه افزایش شدید هزینه‌های درمان و محدود بودن سقف تعهدات بیمه‌هاست.
🔹
در حال حاضر بخش قابل توجهی از هزینه‌های درمان همچنان بر عهده بازنشستگان و شاغلین است و این مسئله در دوران سالمندی به یکی از دغدغه‌های اصلی خانواده‌ها تبدیل شده است./ جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/658177" target="_blank">📅 00:26 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
