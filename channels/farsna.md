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
<img src="https://cdn4.telesco.pe/file/fldyJwPOM5x17hiZWuEO6bH7Wq8f60iZcvc01qljUUbhex_jc_galL05S73ryRqoHxT7bGScSDtOYwttEXmiWO_-Kb82fZB1thcxRkn3Q904gzMShbMrpP_WgOVBJT-828PH716NZ9YZgDLdF2dqPaHFPjn9ffMyE4RuCaf8QY4FxOOYGRPjpyfpwuBJCbepgO4VC4RyMI4_o0XCpcx43ukyLPA36uFJHyqvH1Q8hyjFylwZ3BQn2piKf0-lGYrW4JBtrYlWD4uUEVI0KStxKv-zDJbdEV_OsOU7Xlw-4Jn9ob8u_GrU8Ci4tB1R260yF4-XfaQAf1qNMQU7hwKVxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 03:19:12</div>
<hr>

<div class="tg-post" id="msg-451786">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
حملۀ موشکی آمریکا به بهبهان و امیدیه
🔹
معاون استاندار خوزستان: نقاطی در اطراف شهر بهبهان و امیدیه توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 679 · <a href="https://t.me/farsna/451786" target="_blank">📅 03:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451785">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIiEMut_G6_Movwk8iVqUiUUryjXmgOjYpXGvAo96rPRbTHjYgzYD1JMG-DSxTFH2fT0B1u2OkZdOYNh-P7Soh_-MfbzZ14MeBOZ08bBdHgaGNcPehWsKb-_ykzi9S6B48bRadfp-X1LmrP6eSJsZnaKcU4iotvq4wOpqptQPtIwQMJHArOa-SmiPGnxUHttnmDorUxLXNWzoUAzzYYoc1_Sjh3AQDEV3ksz39quQ8waPTb3ZPhx7IENqh4qicMZnaI_gOkYU1ok8aOo47JmC7J68zP9GinJcQbTTU9jQ514UiEj7JKZjxLXj6pBGmILmRYZOo-OkCage3Pb4XGnrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: با هدف تضعیف توانایی‌های نظامی ایران در تنگۀ هرمز، دور جدید حملات را‌ آغاز کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/farsna/451785" target="_blank">📅 03:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451784">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فعالیت پدافند هوایی در شمال شرق تهران
🔹
دقایقی پیش مردم تهران از شنیده‌شدن فعالیت پدافند هوایی در شمال شرق تهران خبر دادند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/451784" target="_blank">📅 03:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451783">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در چابهار
🔹
خبرنگار صداوسیما: دقایقی پیش صدای ۴ انفجار، و برای لحظاتی صدای پرواز جنگندۀ‌ دشمن در چابهار شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/451783" target="_blank">📅 03:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451782">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجارهایی در سیریک
🔹
دقایقی پیش صدای چند انفجار در حوالی سیریک در شرق هرمزگان شنیده شده است‌.
🔹
مردم سیریک حدود ساعت ۲:۳۰ دقیقه هم از سمت دریا صدای انفجارهایی شنیده بودند.
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/451782" target="_blank">📅 03:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451781">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در تبریز
🔹
دقایقی پیش صدای چند انفجار از حوالی تبریز و از سمت جنوب شهر شنیده شد.
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/farsna/451781" target="_blank">📅 02:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451780">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در ماهشهر
🔹
دقایقی پیش مردم ماهشهر صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/451780" target="_blank">📅 02:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451779">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجار گاز در یک واحد مسکونی در نارمک بدون خسارت جانی
🔹
جلال ملکی، سخنگوی سازمان آتش‌نشانی و خدمات ایمنی شهرداری تهران: ساعت ۲:۰۴ بامداد امروز حادثۀ انفجار در یک واحد مسکونی واقع در محدودۀ میدان ۹۵ نارمک به سامانۀ ۱۲۵ اعلام شد که بلافاصله دو ایستگاه آتش‌نشانی به محل حادثه اعزام شدند و آتش‌نشانان در کمتر از چهار دقیقه به محل رسیدند.
🔹
محل حادثه یک منزل قدیمی دو طبقه بود که سقف حیاط آن با ورق‌های ایرانیت پوشانده شده بود. رگولاتور گاز در فضای زیر این سقف قرار داشت و به دلیل تجمع گاز در این بخش، انفجاری بدون حریق رخ داد؛ حادثه‌ای که در اصطلاح آتش‌نشانی از آن به عنوان «کپ» یاد می‌شود.
🔹
بر اثر این انفجار، شیشه‌های همان منزل و ورق‌های ایرانیت و شیروانی دچار شکستگی شدند، اما خوشبختانه این حادثه بدون هیچ‌گونه تخریب بوده و خسارت جانی یا مصدومی در پی نداشته است.
@Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/451779" target="_blank">📅 02:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451778">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b4c8267b6.mp4?token=e_RhUKQsHs41PfR_RY7gK5ZnvlYxtAgNCdH28cfElCaSrncEQkQAG4myWrbFxuMxNdgSiEQluQBpC7TyThkuLLEQU-g3kr-HnTlFFUiTt6Lm-JlG9IQtDGUuw7d1QOxXFG1eHUgwlbR8Eo1KpWhoQLT5GgZSAVMv0nYQ1nKHnSbwze3S7CNzE46TuJB5xHTi3FODuP5W-vtw4C9DVApb-bREaHVe5p9SIINxff8G1SFiACv_hbtcmRsE8IeEtHuwJSi14jZk8HXgfbg8dRAoVej2A_Y2OXrADy_bQxpnAXNrNcewQMQtFNlBo0XMmrU7RrQHWe8sRKZvdHLALEBTFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b4c8267b6.mp4?token=e_RhUKQsHs41PfR_RY7gK5ZnvlYxtAgNCdH28cfElCaSrncEQkQAG4myWrbFxuMxNdgSiEQluQBpC7TyThkuLLEQU-g3kr-HnTlFFUiTt6Lm-JlG9IQtDGUuw7d1QOxXFG1eHUgwlbR8Eo1KpWhoQLT5GgZSAVMv0nYQ1nKHnSbwze3S7CNzE46TuJB5xHTi3FODuP5W-vtw4C9DVApb-bREaHVe5p9SIINxff8G1SFiACv_hbtcmRsE8IeEtHuwJSi14jZk8HXgfbg8dRAoVej2A_Y2OXrADy_bQxpnAXNrNcewQMQtFNlBo0XMmrU7RrQHWe8sRKZvdHLALEBTFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان حمایت: در ۹۰۰ هزار بازرسی انجام شده طی امسال، ۷۰ هزار میلیارد تومان گران‌فروشی و ۷۰ هزار میلیارد تومان قاچاق و احتکار کشف شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/451778" target="_blank">📅 02:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451777">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9171ddf436.mp4?token=AyWPUZffwiuZrIAJUp1NR4eCQG7SlFb649vXeMvA6ZyGSd5IN_PG2aEKorwCkQD4LU0vdyg7hSg8ZiYvV5NAcaRRluA6Tmp-KV8b-xaFjPEFUt2o6g-a2Xr8rApjZG6tCqFizdIOHqdqodGmsWYdwVbUoEo2-88rGgEqLJnIW1Z2TWgtJ9aPDIn_tlZqRMVwo5cxAKDCTWC2xD0mWvrxJhCR_Uhfqd8gfKq3IOlKYClZ07Zz2LbU3vxP8eYhmG9Ckxyu3KaxGEVCtZCZrj7ISVqJNjgN2yKxN_VH9hXrl06g-za-dIjaCgFDDnqEfbc3Tlv1VeOHyhR_PydTikppqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9171ddf436.mp4?token=AyWPUZffwiuZrIAJUp1NR4eCQG7SlFb649vXeMvA6ZyGSd5IN_PG2aEKorwCkQD4LU0vdyg7hSg8ZiYvV5NAcaRRluA6Tmp-KV8b-xaFjPEFUt2o6g-a2Xr8rApjZG6tCqFizdIOHqdqodGmsWYdwVbUoEo2-88rGgEqLJnIW1Z2TWgtJ9aPDIn_tlZqRMVwo5cxAKDCTWC2xD0mWvrxJhCR_Uhfqd8gfKq3IOlKYClZ07Zz2LbU3vxP8eYhmG9Ckxyu3KaxGEVCtZCZrj7ISVqJNjgN2yKxN_VH9hXrl06g-za-dIjaCgFDDnqEfbc3Tlv1VeOHyhR_PydTikppqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ قطعی برق گسترده در منطقۀ کردستان عراق
🔹
منابع عراقی از قطع برق بخش‌هایی از استان‌های سلیمانیه، اربیل و دهوک خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/451777" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451776">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b0a0cb6e0.mp4?token=b3ZEn3fc-Es1OZVBqZmG2g2waf3NoaubbqkIcyBbGB1nPpKv4_dOM4VBB_wWqEdU-7jhhV7k2oxXkPuH52HBPPKQ90Z6GnDpVFcxx2g9tGS13nDBlz9oSMb8ML9b_Mcy9uutKY80ov5a5lkTS8r6rq98AzDyXUpewZIYFBIH961_S7MXWN-WVzGpR9C32xDPEuWlNXp7vvl02F22t3T8JyTPlL-5O5-TvzYjJe9WdCeEhPGvSbJDsToOkFvFCX_tifXBH5JKB2KiKfFRTSSlVlxXV2Cw-5ceY74ZPCFW1fnzSz_BRUy4U6f-mx0ZP6DUhhSDLrQsGok3NfpDtIwNiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b0a0cb6e0.mp4?token=b3ZEn3fc-Es1OZVBqZmG2g2waf3NoaubbqkIcyBbGB1nPpKv4_dOM4VBB_wWqEdU-7jhhV7k2oxXkPuH52HBPPKQ90Z6GnDpVFcxx2g9tGS13nDBlz9oSMb8ML9b_Mcy9uutKY80ov5a5lkTS8r6rq98AzDyXUpewZIYFBIH961_S7MXWN-WVzGpR9C32xDPEuWlNXp7vvl02F22t3T8JyTPlL-5O5-TvzYjJe9WdCeEhPGvSbJDsToOkFvFCX_tifXBH5JKB2KiKfFRTSSlVlxXV2Cw-5ceY74ZPCFW1fnzSz_BRUy4U6f-mx0ZP6DUhhSDLrQsGok3NfpDtIwNiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قطع صحبت‌های هگزث توسط مترضان ضد جنگ
🔹
در میانه جلسه استماع سنای آمریکا، معترضان ضد جنگ با قطع کردن ادعاهای هگزث، فریاد زدند: «بمباران کودکان در ایران و فلسطین را متوقف کنید!»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/451776" target="_blank">📅 01:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451775">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ad125befb.mp4?token=I2eZ9FCAch1imqIYEvANPdaV8OzN0c_jpIhN10JPNZ9xX2y5XcHoy2BbEHxm6J6qMtBptEMf756yWDxHH4l5bbL4iVfQlK9wUqBorDIkrYf4mHhmfVEBVS7equYSamvuOjwnh2bHeZxthGeUtjxJ6DDOD6ODqDPnY9u8-SdHja3cPEyjJi0yxSVDKzdi93goNjK0axOWFr1ll65U57xhGsSRPzvDpRd3loGFoyBT5tECZmFof1lWtdIixTrj3vFjbQ1S1jDTgcGl2M-eznqMt0-xxKvUdv1V_LzxCq3duVFmcW-FAbBAIxg18PMGBsUXHnGa7vQul2Qts-gmRPDbQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ad125befb.mp4?token=I2eZ9FCAch1imqIYEvANPdaV8OzN0c_jpIhN10JPNZ9xX2y5XcHoy2BbEHxm6J6qMtBptEMf756yWDxHH4l5bbL4iVfQlK9wUqBorDIkrYf4mHhmfVEBVS7equYSamvuOjwnh2bHeZxthGeUtjxJ6DDOD6ODqDPnY9u8-SdHja3cPEyjJi0yxSVDKzdi93goNjK0axOWFr1ll65U57xhGsSRPzvDpRd3loGFoyBT5tECZmFof1lWtdIixTrj3vFjbQ1S1jDTgcGl2M-eznqMt0-xxKvUdv1V_LzxCq3duVFmcW-FAbBAIxg18PMGBsUXHnGa7vQul2Qts-gmRPDbQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم تشییع اعضای پیکر شهدای مدرسۀ میناب
◾️
چهارشنبه ۳۱ تیرماه - ساعت ۷:۳۰
🔹
هویت این شهدا از طریق آزمایش‌های DNA احراز شده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/451775" target="_blank">📅 01:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451774">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLytiPTqOe7LH-NQhS7c38_N2QbKuojCINRlMZ5Hf6-TMmg9GVftWp0u-YPdfPXGr93pph1OLTiLt5DYghyzRpqakZJWKTaKtFX4_kU4ncxn4yxbgcq47aDgC2wiMMuiCKjriV61pI8TTN9C0JORc-AAxIJGJncRSALHisKXQNxWK5B-LVbPHvGEmyxF6AJZiuVxsvb58mNJXWV2IJdeKY-rA-GwVT0KHnN7o7_bf7gVBV7Zpbs31xr6GRHiLznn0-ReyRskFGUk0cAe4UiW8YOTrmRfNwvm3ZtSWtmih1HOhXPNdCi3eN0-BS0OEXwh0WF_-CvKOBfum7lxyeTQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سودای رئیس‌جمهور لبنان برای پایان دشمنی با اسرائیل
🔹
جوزف عون در دیدار با ترامپ در کاخ سفید تأکید کرد که هدف نهایی، پایان دادن همیشگی دشمنی بین لبنان و اسرائیل است.
🔹
عون، همتای آمریکایی خود را به ادامۀ حمایت از ارتش لبنان در آغاز اجرای توافق اولیه با اسرائیل ترغیب کرد.
🔹
وی در این خصوص گفت: ما باید از نیروهای مسلح لبنان حمایت کنیم. بدون نیروهای مسلح لبنان، همه چیز از بین خواهد رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/451774" target="_blank">📅 01:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451769">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/odpPtarsLtV5vvzXYuNZTlQwm-tembeh2155S6JWEIPoE-_b00ASL6YrN5vUFAf_7DtR-K_ETxM4B8hzPUuWckOOLBnoEpIljobQqHGbeqWw7py2Twh6jn5ItsbJ3ZK6UitTVl-IIV6bhfXiG5bJ7pV9dpag7sB9fSSNOStFrgekZT-3pb-1OgApKBBUOOUAoLp4BGojbSxcwgppPMxb5FKwD6uPtZhPvaQD2u6bEvzbXh60VwEkEu83ZW7PNkq81N5ih4WJEXOmodGFgF7s27M6jYjdqCtNUleQOzWEPggaMJHpukHRdY3A9iIkoO50LpuG-6CIgZZHGinBVjpYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2SCladuotH3TIXIPr9HWyC1Q5Ug_hDzdjmej_ycLXopci3ihcrudoMbb3EolPTJkGrt8UHy92UXpzG-g9YBkou9ba7_ytc1gfI1D8vbe5RaRwO_vJJQLAmoMdiVQGt3GWc1AcOLJJLsah5yLfIAoA5xxyz9lGBgMTq76U6JZUgGaLN5Akp57j1vL19fPCU54hRYHpybBeC8zLL5PS4m8Dc-FSZzaHXoOB7yAoe3X0YlArHK3hYpvjvV-1F566enWnJuKjiipAqB10dUt_uHhN-VPFz5ASDq06ValdhIrdIxFEWSSDYO0XgCs_tXIvurszFgyTAYXSHV3L-HKDS7lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5WM6PECjQjd7AKKzqmsrfoM-Fl_UXmpt1hjmKh7tvq6yzkx8XpPoDF7KoGmwbHzVRhEohj2NW2U9GplIL6kaAVzcmSzkjx-xHYlamgfPDnBDSQMBHHS8hLXtfEUw4MEQvtK6ekHC2Vo-OVuZLEWPpLHU8mDNYtk2tetRaJk0qb35hFv-cfRSkJomC3skZk5bRtPvEcRIRPmpw4o6FmdJWiYyFer5pEOQKlzrDtfWpLuOtb6ui0X6Uc8Bs6dhzf36Gq3p8a_A7d85TeoR6UuWeAu-1fywl1xBZ3QU_sZwdly7mPnS_62zb4OK29uMNXzu_utnmltDENdfmjoT1aS_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNXUDU4EJHHF9-TrSkh1kKz6-HtVJXbDwkdZ3EiHuE7pFXvFVmupl9TfkzOBpNJMWFHLuPY2y7Y4wizTDBqIem15vGYJ155WdEmVtut5fuazcMKCNuza6nK1H0F1I6R5WAFna_May6DA51fAMiBFMS_sdad49_VUpKTtJ5bV85djEvCh4GraqqLz6unK6tHPeq8DxgjYDTTvlOmrJJAOl-sIy7qkgTx1-4cCLOQvTQGqe4L0RuNgLGHR9WUdDbzZjQqHRCLLzCnQF_goFyIDrvFKtYijkcrE0fAu37OHQecNFsTXNEB8W1a72JgJIKH-A8KrVLPpc8Mj6cQD6-nZzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/StZrB8U9cEc77YseyUoYc6JlY_3F_4-Ot5DYCh1Ia8rrhKoInu05ywYH7o0ua17UV0IiS2iq57iWKBElvQTcl02NR43I7jogPLYY8HuonzEQmd9wHb0gL-jX8wxgjgFx2sQZqFVTHAjLDeEuFuUqt8u-asYgVzw0jrqHiKLbw5wgNmVwLBgOhaXRFqFc7WPg59_l9G9IC9ITEx5_f0xJ_RRnNy-WLNTuFzer39yPPNXEua9iCDgnlacT-yd3Py0KfAMhJTMafdsKSpOVp-LOCbJGLqQHwVNsaMbRBOAR5oYK-KuM81imu-ULIXwsOKI7sBYq2iCm1xksN1NiNOqE9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۳۱ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/451769" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451759">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RMHW9-HM-wo2Ti6N0z3nU45GkN9kKIgenDuC0u1Nyzn_YGHy8GLOmEIa_GPteYhpILjQdY_ZsFmJXCr5WKkiR3q5wdNpBWgEYJm1n6VrJZ_nInuRIpQanWPW7MXTdwLsbBfxjPzKe4y7XcnC7pAqvSh-3Ifjz01160yhJf_Vlznb6OhniaAJlKDa23Txv2g9__ncjMX7nS0gnf2F7BokG3ZHTuPo0_tnxBmLG-DMP7sXQWkjAZxJMP8PTL4pJj4AbTDIu9IeqL3kaHdJHnh4bWb0uIlggj2gVXGWFZud5BkVEe7HuMNuH-iFm6vEeoYJCebkzXRAw-gSdhG9X056fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9IJIg9ldf2GdlWff_GLwPHVirAvSHgKzrNuv836UPcKhuBeIWLvApOUfYTgDnCO5RgJQG_q0fbm1rbbrnsDU8VyPedBweYjMqHHdvtV2x4mRnXEzeVLq_XvT_ILFXz5Fsz48Hmh1jDT8gFdbkQNc5Io64-Zy4Bzqwp-5IY2i5ORm5E9TZkcFq6hEVYW7SEgXeiXRksKYGb_67FFqtb9pPWMV8cZpjFuNDYmV0RiW-Ym9JkuIfQumZgZbgyd_fJyvsL3xXFud2MTcbGnNeqKTZ4nxNY39Xji_4vqCE6DHdQutAvn2TSSuK3sHznM-fli4OWGFfMQPKBntE61h0uS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NmDQfNC2ICdHHHTPEbeZ5Lf5MHAKgGadcMCGtJULBRrtFEY_NQBHROjU6QbILSreoF7dJEldUe9ScCLH8r852O2X0zi1pOj6IdiXEm_rmwUpa0AGIU9c4pvPUugHiAXWKz-LorZI1Xizzh6XofcZfz7QUhdREeoUNFXAmryRnSgtMDdUxIg144PMuCb-dHQS2Ck6fjJ4P0R7G7kQduULM1KONMZtIPiI7o6ysGF33p-60utrd-CfCqP45nERiupgfcIANSy9ETSW8Too-1tLyGmDcIl23mCe80DvIh1hipO7Qt-UH13n3IYCHG0OtWsCihKVMpZZIw1K-FII7hnHww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGaikiqePBmsxfhSzZ_QZPf4D4szwuY8TdMtLDBT6uqGGS2t80kVqoly10-PTHbrNFXvKWz9CopBdEnBua2L19VHa05_yg5xOjNj1ikG7OCBBSVQ60I-AJR35jyVc6CtDeN-4sWFqemfaZMje4s1YlW37GJ8ezVVp5io3mhiuYfWAHKxGAOWK7aq1karbcxPws9iHbhdQz6DI9_-2ZQeJ_5WDuiS62EX_1yZCIEk7A3Mh6WcJirLq3B0VlwIWdi5V9kIj1fHl3VJEKxiLW0vQHHLumEI1_np740l4EdXnulXmv3BEDQ-YCO7sQTUP5UGdLFhzVBmXTXSGJMxkAsQJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HbXwUfFegpHLzZdWoWRvsM7-DuMLoVpnXlUSoc6wcBY6UceHwIFtyikV4F9b3tndTHSdDQKtdBFxsGcoJXw-UIexHiJGlzRIyQU9B4wBiMmaGEMDI1zevScj2FO80W41oUu7ZtmJhvYCpvDBC0ocQfQBKUQ9kiBu10yTMXwhVgKAYQnvMnugtdOC6zRnCPrD48-3kispTT6LgaoYTo0fskvU4T6ErJEgh0dTOlm3_T61kAnPLqlZ5Jkv2JeNRlQD9y9V_DHEasypmG6BJM6Az8mU2ecbo2maWbHOgDAYJRHiYW9B-KKEArzz_W5XOKVh24k18QgtE7cF_hjRF_34CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aKqIwe5Co57VcaXUTtyMMjcSJUPNqhUEyM2Su6WRAQZ9r_Jyo396ecbCqjyiHoZVqA5UYFTyPR8c1Uy_WD2l1Xq0y7V4Q0PsUaB8qKHmD-LNurZesAaJATRUo8Wx-B9UUW3AZu5WIWwYcXdr3r2ipQE5bRy63GeOJT-7y1GS6AV9wZeuMmy7hqatBfchAbY0tBHa4zG_YFM089TLYJTzWrUNat5_dJH0VOMMmoVknPMFtsoNxeCnD01Ld1mqHT7HBYZKdLjvBa_gDkjojshDry04BIEYlptOKQqTgeFFmbBFU6_-NwnSmVroOBYaqhQzklUgQGayiEhUpaOfDyNa-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fEs2lDb9wKu5Sa-SW2tdtawNS-6ux2B4AQEsF3CdWPe46kW5QFy5bt2b8qUSde-R-nGqrszjwLnTEM_lWEjnWARJh05Qlgzvqcg5peU7m5waNI-hwgZh0hP8lEqSwU4sU2PXtFBqWGBR_8p0Z1swxqXKO0WApDrGeuij6apG_JITtMCEjnLqkIelajtMWr9t_IQft3AjlUFVxf3TI7EopXC2tfkdPdLZWbfLWMSMKF6PGnCHRabH1tcma4usFyySP_LOP_7H_H9UrzHm69jUDfgIdRHA2_gLgGAZ80er2ZoMIQm3blsv9YKdSe0Fh4pVtRmjG4TI48Y1iCgizXMPig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LagNz-Tggq2ZXmHIQ0-tAf9Dols7U77j_itVeAqfBtywXb97bQHLcligWnzVtJWoOGL_oobjjKg5cx8ghvbf_rtcFXkxo5kmLupfrLJT374gdrlofoxtkqSQljga0z332kZvxgo61ILx7w9PEOGdR3Bpfo-nZHoEKRxynpFII3egylpu2WoSUKkqrGJI_BRflcKa1CK9neQEwJBUkectU3GaRcx03qbWfzSUi2OTrAC4rNQwK9feYoQnS1xnoKI-6YdWuwA-26vn8xrSZgs-bVcruDMFrGZjgyOKuiFqwdgLEIeWfIOn1W5XCi6vG3Z5xQ59JSdONe5EE7EWjTCwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qeudu0e1CzfEoIf0j-k1nTSaqlw91RgxsEDCNT0WaykqxrTJw9T3W8tbRmnWBhtK54hp72d2XTQiQjUSaIZyC6wDLjn8jD7TU3kCTrk_i8Qc-zShuTz82svyOHdKdcThF0hEGXEnARM0OW7ieF3uRdWtnFBNJk_Bl0iOjkfFVdPV7qipXHa1UMJXiQl90r9tJw5hkqntQeNQo2v8EeEZtMgiLairg5L9I6F645Ju9REJqY_adIBVq7vq_AZxVmW_cDLVu7hP4wEYCiXXs4ud38gkQDdGpcnaEPqqpWjPdlAIE1LbgIXeh8esGNu1qu3yDLi1a6hifqhxzOCkaJc3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ATL_a7N7SbXgMy4kAtGA1pQu-vhXiW0PwFkTZ5nVRrkiG817J5ct3xJEo8tnBCIO0EgSya5w7KsqUzM2y3DQCM88ZOtiRZJYa94bsF-XtBmwNNLgEA7zXwCZRgJ3YajMVWt0kbTuF42NHWBNCZ7LM3oaA_5QtyL6S1zAN9MQhnzwzfjb0oTll_KZkgE4J72l_gmR3Ny_NmKOU6LJPdg9uSm52_6YGLPJexT8ktoG_i-auawQpTSfGtnxAu_NJy0o_5ETPcJb2CRCSAos_LdRFzLwfB7UMBXcbSeZZGXDI3dzYPfqQ1BPOz2j_4S6nsUyzFgl67nyiNRZbKUDjIVVUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/451759" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451758">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
آژیر هشدار و انفجارهای متعدد در کویت
🔹
منابع محلی گزارش دادند که منافع و تأسیسات آمریکایی در کویت، هدف موج جدیدی از حملات موشکی و پهپادی قرار گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/451758" target="_blank">📅 01:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451757">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
آژیر هشدار و انفجارهای متعدد در کویت
🔹
منابع محلی گزارش دادند که منافع و تأسیسات آمریکایی در کویت، هدف موج جدیدی از حملات موشکی و پهپادی قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/451757" target="_blank">📅 01:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451756">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
منابع عراقی از هدف قرارگرفتن مواضع گروهک‌های تجزیه‌طلب در سلیمانیۀ عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/451756" target="_blank">📅 01:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451755">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmAxh8dL-Jkqv04RmiYCORn0are9X2x-ANFkARhkE2T5R0uIJ5ac5EptN25ZyLMwvbNY-zEmH1NbP1hpId9SzHjNaFAELmD0BjiEeN22988-0z3DVundMP7UYHdbGwLjVv5Mg5icj7VaScwfq7V3E3xL7Q2Mq_LvXIlgydJaziGdgoJ4_dqeXwiPxnbUzKo-GJWIkZQIjX93cPvD9losaddyh8RnN5SXZpZX-4o1KkWd3gEeQxF7CZcoezzLq3mApCo5x-K__q9hp5zVgT56X2Vc2VbCmpFKACQKXpapDphLlF2Yfn9WIp0-FriYYLkzfERMeUyGAAVH3qksWQnzhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چشم دیجیتال سنتکام در بحرین کور شد
🔹
نیروی مسلح ایران در واکنش به تجاوز آمریکا، زیرساخت مرکزی داده آمازون در بحرین که یکی از گره‌های کلیدی تبادل اطلاعات ارتش آمریکا است را هدف قرار دادند.
🔹
منطقه ابری آمازون در بحرین که با شناسه انحصاری me-south-1 شناخته می‌شود، نخستین پایگاه متمرکز پردازش داده شرکت آمازون در خاورمیانه است که در سال ۲۰۱۹ راه‌اندازی شد.
🔹
تاسیسات آمازون در بحرین هرگز یک پروژه صرفاً تجاری نبود؛ بلکه در عمل به شریان اصلی و مغز متفکر پردازش اطلاعاتی واشنگتن و متحدانش در خلیج فارس تبدیل شده بود.
🔹
مهندسان آمریکایی این زیرساخت را بر پایه سه «منطقه دسترس‌پذیری» مجزا و ایزوله در نقاط مختلف بحرین مهندسی کرده بودند.
🔹
آمازون یکی از چهار پیمانکار اصلی وزارت جنگ آمریکا در قرارداد «قابلیت ابری نبرد مشترک»(JWCC) به ارزش ۹ میلیارد دلار است. این قرارداد به پنتاگون اجازه می‌دهد پردازش ابری، تحلیل داده و ابزارهای هوش مصنوعی را در لبه‌های عملیاتی و پایگاه‌های منطقه‌ای مستقر کند.
🔹
جزئیات را از
اینجا
بخوانید.
@FarsnaTech</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451755" target="_blank">📅 00:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451752">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdy2fClS_inf1VKxS80kq4jPFWzbYItBzUmqjcWReT6PmR84ngx2zPRjyGRUEg3FAn8gOV1q5_aNQGpM1xHt-YlqsP5RDDF9O9elm7ofi0nePidDHeL40LqinKdyOa1NmpdUUONk3PmTdOaCgtetiXmHJ3aAdDOdeR6gVMjwqSI9FHCo3xWPmWjSD24XAg9o4MC_Vt8ReASu6vxmb-yF3NMKruac8zxJ__SuO0044usybl-WWfyhBYtWOtNsembpPd7TQo6uJGBAzLoPKH9a-aU5Hs6VsONYZzMC3Y6dbwzfsqq0zhsCitCsFNc_4HmQMFk2r7k-1VFYNrB6u014Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e6c3b61f.mp4?token=GtoGdGd53CbOTXhLG_J-HRSyuHSHbuB28tMXYZ3JVKQz0Q0S9VD7ivSgfgq-oIyii0CaoaC_wlWxPoWTGRNHO986llhGkOyQ_ACmQHvZgrMA8Wq3qTb1Lq83Lg2JfOZAgipM5Hfpz_ei-iMrPP02KbLz1UfrW-uIqQwJ68M8ZExrqxvLmHB9EP0b7Wiq19IeuofI66Qxx8JLRCKSzQ7riI0iGDnKlGpljx7qnBBfH-R2K2xNGs95J5fgUf4T-fMdAqNTpwbTMpn_npQxsnwBsbkbfrS65djbJWWMfHzW0nS1S4s6Y-l3VP5TKK8h1H4MxDLV7GvxI1LAhSLjlU9r0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e6c3b61f.mp4?token=GtoGdGd53CbOTXhLG_J-HRSyuHSHbuB28tMXYZ3JVKQz0Q0S9VD7ivSgfgq-oIyii0CaoaC_wlWxPoWTGRNHO986llhGkOyQ_ACmQHvZgrMA8Wq3qTb1Lq83Lg2JfOZAgipM5Hfpz_ei-iMrPP02KbLz1UfrW-uIqQwJ68M8ZExrqxvLmHB9EP0b7Wiq19IeuofI66Qxx8JLRCKSzQ7riI0iGDnKlGpljx7qnBBfH-R2K2xNGs95J5fgUf4T-fMdAqNTpwbTMpn_npQxsnwBsbkbfrS65djbJWWMfHzW0nS1S4s6Y-l3VP5TKK8h1H4MxDLV7GvxI1LAhSLjlU9r0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از هدف قرارگرفتن مواضع گروهک‌های تجزیه‌طلب در سلیمانیۀ عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451752" target="_blank">📅 00:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451751">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🎥
ترامپ تهدیدهایش را دوباره تکرار کرد
🔹
رئیس‌جمهور آمریکا: ما ۱۰۰ درصد به سایت هسته‌ای جدید ایران حمله خواهیم کرد.
🔹
آن‌ها دارند تلاش می‌کنند یک سایت دیگر را بازسازی کنند. ما به همان سایت ضربه خواهیم زد.
🔹
هر سایتی که حتی فکر برنامه‌های هسته‌ای در آن به سرشان…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/451751" target="_blank">📅 00:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451750">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c48ca5530.mp4?token=P0esqZm26lgoQtXUBLhndWyXitDh1IBa2tDZSxtxG0lcp_ilRH-qVaaI-wtlCoSj70nJwCFpcAs9GGCTHXZS9QCAM4r6NFv-o1ZAF-58_hy_xRcY-hjrOBcFi3xxhn-0329K29S0bnpkOms4k_Lgp23GnSnC88fY6D8SdRdCY4LIB7YqzH_FC2Wov7grI153RF6wkUEu47N6PXKv9_gkJpdLV5iQceukkxlrGdHEyuomv0MGwuixdHlK-3wsdsK8tpagPktbVqTd__Qf1QsU3a6snuEqlgPYOpH48TcX4ZfPGTQMZ_Pjfenp-L9Wn3-SuCTCdrfF925HQKqvAGCZRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c48ca5530.mp4?token=P0esqZm26lgoQtXUBLhndWyXitDh1IBa2tDZSxtxG0lcp_ilRH-qVaaI-wtlCoSj70nJwCFpcAs9GGCTHXZS9QCAM4r6NFv-o1ZAF-58_hy_xRcY-hjrOBcFi3xxhn-0329K29S0bnpkOms4k_Lgp23GnSnC88fY6D8SdRdCY4LIB7YqzH_FC2Wov7grI153RF6wkUEu47N6PXKv9_gkJpdLV5iQceukkxlrGdHEyuomv0MGwuixdHlK-3wsdsK8tpagPktbVqTd__Qf1QsU3a6snuEqlgPYOpH48TcX4ZfPGTQMZ_Pjfenp-L9Wn3-SuCTCdrfF925HQKqvAGCZRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادعای وزیر جنگ آمریکا: جنگ با ایران تاکنون ۳۷.۵ میلیارد دلار برای ما هزینه داشته است.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/451750" target="_blank">📅 00:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451749">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a4272552a.mp4?token=oJgf2Ybfr8-3T6CqrFzxmdOrDuDe4EwJD3fQf8EffUUcnVFAgoCZbBWaGHSBaQcaWgMSAFbDH5lL7Vl8gqH7XkV7j1t1d_Arp9L-j4Qrud-qhM_8VgsC_tWo57TT-1qhkUNkeTfVwetlCNDsNzKNtaxJyXsk5yAvNJ47D_ZtmI2pAs8XLq6axbxVnpubpa2ZBxiQu4PG72YnzuoY3HGmSziRPEfqJqVUpJ2N-EzAJ9jyUMXRzMPeO81cF2RdKwEzK95buean50wjoTdFLKWjVXxC-7hIFmiepGL3HLhjYaJO8zxEPEwsZItYks67h4-EKOU0kbulboKpRh7EoIz0Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a4272552a.mp4?token=oJgf2Ybfr8-3T6CqrFzxmdOrDuDe4EwJD3fQf8EffUUcnVFAgoCZbBWaGHSBaQcaWgMSAFbDH5lL7Vl8gqH7XkV7j1t1d_Arp9L-j4Qrud-qhM_8VgsC_tWo57TT-1qhkUNkeTfVwetlCNDsNzKNtaxJyXsk5yAvNJ47D_ZtmI2pAs8XLq6axbxVnpubpa2ZBxiQu4PG72YnzuoY3HGmSziRPEfqJqVUpJ2N-EzAJ9jyUMXRzMPeO81cF2RdKwEzK95buean50wjoTdFLKWjVXxC-7hIFmiepGL3HLhjYaJO8zxEPEwsZItYks67h4-EKOU0kbulboKpRh7EoIz0Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی وزیر جنگ ترامپ را به چالش کشید
🔸
پتی موری: شما ۳ ماه پیش گفتید برنامهٔ موشکی ایرانی‌ها به معنای واقعی کلمه نابود شده، پرتابگرها، تأسیسات تولیدی و ذخایر موجود منهدم و تضعیف شده و تقریباً کاملاً بی‌اثر شده‌اند. آقای وزیر، ایران طی یک هفته گذشته…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/451749" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451748">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde16fff97.mp4?token=FVserwFM_INzC0_LLUCiXIdTIUtdoHY-oe4xLBqhsUw-GaHhdulLE_wRjk0mT9DTSaO-2HdXw6qekNmjwLN_kEJ1rQvT5W5j9gnp_U2Ag7hsop4dZaMKhJQIhGoipHlEEJUUiIpbi2i23mSWLnLhO-BPp6QE5W-XPi4cSvCUOGShdcgxPDbJQphVlX8EBGNwW8vKOHCvZ2XpJ0W10NnMhEFFVCSzzgs43nbctzCBdqTevPbdPKuZwUreLqV_kSyQe3RRKlT4Ch_zv2neEpXPkofELsZBjMklf_TWdIoWdEc1RO9Ak4K0uCB2K5EBt_J3kG0XCCFBIx9E8PDP1_SIUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde16fff97.mp4?token=FVserwFM_INzC0_LLUCiXIdTIUtdoHY-oe4xLBqhsUw-GaHhdulLE_wRjk0mT9DTSaO-2HdXw6qekNmjwLN_kEJ1rQvT5W5j9gnp_U2Ag7hsop4dZaMKhJQIhGoipHlEEJUUiIpbi2i23mSWLnLhO-BPp6QE5W-XPi4cSvCUOGShdcgxPDbJQphVlX8EBGNwW8vKOHCvZ2XpJ0W10NnMhEFFVCSzzgs43nbctzCBdqTevPbdPKuZwUreLqV_kSyQe3RRKlT4Ch_zv2neEpXPkofELsZBjMklf_TWdIoWdEc1RO9Ak4K0uCB2K5EBt_J3kG0XCCFBIx9E8PDP1_SIUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی: آیا توانایی نابودکردن آنچه را که زیر «کوه کلنگ» ایران قرار دارد داریم؟
🔹
وزیر جنگ ترامپ: بخش زیادی از توانمندی‌های ارتش آمریکا طبقه‌بندی‌شده و محرمانه است.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/451748" target="_blank">📅 00:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451747">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVNDI8d-NvaD70Zex7YA-9XBL9Qo0TzrLjj5-Df6RLlDhNSu7y4lTs8DOi1iNFKpH-YQEryfkBPdV3240MlHODeIREUnaBd6IYAHSIuRGa799_708-j77XCHAPfGPmNMzuEaBmo_s2lVKSZ-pZTgA8alyJVuQ9fmsWYk_Z9ewfwEnwPSwtRkoxg--ogZLYOaSSEO-yp_aHeSDD4t3HgfKEB1X7VRsDJPh4hDYN7zJ6LvEXT9n9uv1vtclxYu0XzP5TVz_H8jggZKHrlphvrdSX7czt0WoGpJ-aj1nb4JI3jl2LMLUy6Fn4GZs1T9IvpDOEnU0HbK2JFCnPnuzeL3hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلاش جدید ترامپ برای توجیه تلفات آمریکا در جنگ علیه ایران
🔹
رئیس‌جمهور آمریکا دونالد ترامپ با انتشار پیامی در شبکه اجتماعی تروث سوشال، تلفات آمریکا و مدت زمان جنگ علیه ایران را با جنگ‌های قبلی این کشور مقایسه کرد.
🔹
وی در این باره نوشت:
جنگ افغانستان: ۲۰ سال، ۲۰۰۰ کشته.
جنگ عراق: ۹ سال، ۴۶۰۰ کشته.
جنگ ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
جنگ کره: ۳ سال و ۱ ماه، ۳۶۵۷۴ کشته.
جنگ ونزوئلا: ۱ روز، ۰ کشته.
درگیری نظامی ایران: ۴ ماه، ۱۸ کشته
🔸
ترامپ در حالی این آمار را مطرح کرده که در روزهای اول تجاوز نظامی مدعی بود که جنگ با ایران در عرض چند هفته پایان می‌یابد، اما اکنون بیش از چهار ماه از درگیری‌ها گذشته است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451747" target="_blank">📅 23:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451746">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5683a4e5b1.mp4?token=A_fPw-JrK8xkFyhPtT5cIvoPjcCKXeO6WW-dSHRuVuQOMfMJBiXuDUqeq4vkGjzm0aewLy0_B9hAJUrU3B93LaSTB6jf-knzJwZ0WfdudBTdqFftuIEeeYRA3f7EPdPOUWJjaJ-y-sbGuUtTorRLaQUX425x0T0SbaPNQakDV5HqNnNTQVTn1QwdPwuJjh7Dw6b-L_Wqc1n9WQeNK0iLfakiVPZD8Or1_tux9ZVTOLtPy6ESniQWG0WAKI8S7Nv9ZDNRz-Ehw5BDKlpRAxt7PTINr-96TEiusd55MyI44YlUVA5WOd_D5NM7qXMC3UIjUPURy8H_FNoP5hWmM6GT_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5683a4e5b1.mp4?token=A_fPw-JrK8xkFyhPtT5cIvoPjcCKXeO6WW-dSHRuVuQOMfMJBiXuDUqeq4vkGjzm0aewLy0_B9hAJUrU3B93LaSTB6jf-knzJwZ0WfdudBTdqFftuIEeeYRA3f7EPdPOUWJjaJ-y-sbGuUtTorRLaQUX425x0T0SbaPNQakDV5HqNnNTQVTn1QwdPwuJjh7Dw6b-L_Wqc1n9WQeNK0iLfakiVPZD8Or1_tux9ZVTOLtPy6ESniQWG0WAKI8S7Nv9ZDNRz-Ehw5BDKlpRAxt7PTINr-96TEiusd55MyI44YlUVA5WOd_D5NM7qXMC3UIjUPURy8H_FNoP5hWmM6GT_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معترضان ضدجنگ در جریان جلسهٔ استماع سنا، سخنان وزیر جنگ آمریکا را قطع کردند و فریاد زدند: بمباران کودکان در ایران و فلسطین را متوقف کنید.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451746" target="_blank">📅 23:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451744">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9ab2fe524.mp4?token=bPAtt8cz3TelyALYwX1yEgMLrkZxbvLsuJGZhCThGS2pZz41M50KXZcF48v_x3TplcpElf5YqqkK4pF8Vg49PmjJkwD5aCw7BzcJ4MIC5wFokPKoTa2U54ihS5e6k1SzeWYf72TBlDZv_uZrpyx32SA-cq0TJEBbjdtFLd-Fhw7OqqbxyFSgSTcajW_ehJ-P-mLv1KDf062YiJI3-JBTT5Eh7qz-Eur6-nZfl4jR4f3MBF-1QmUSKiZJ1sJYJGQpnBYrJ7jfOu4MGNjpuJOF_MeMGu_eQR_Df0NRkuMXh6H3QK0r1etpMLetWVMlvWZ0q0l0oZuSXkwRKQtp9x6_Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9ab2fe524.mp4?token=bPAtt8cz3TelyALYwX1yEgMLrkZxbvLsuJGZhCThGS2pZz41M50KXZcF48v_x3TplcpElf5YqqkK4pF8Vg49PmjJkwD5aCw7BzcJ4MIC5wFokPKoTa2U54ihS5e6k1SzeWYf72TBlDZv_uZrpyx32SA-cq0TJEBbjdtFLd-Fhw7OqqbxyFSgSTcajW_ehJ-P-mLv1KDf062YiJI3-JBTT5Eh7qz-Eur6-nZfl4jR4f3MBF-1QmUSKiZJ1sJYJGQpnBYrJ7jfOu4MGNjpuJOF_MeMGu_eQR_Df0NRkuMXh6H3QK0r1etpMLetWVMlvWZ0q0l0oZuSXkwRKQtp9x6_Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معترضان ضدجنگ در جریان جلسهٔ استماع سنا، سخنان وزیر جنگ آمریکا را قطع کردند و فریاد زدند: بمباران کودکان در ایران و فلسطین را متوقف کنید
.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/451744" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451743">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dF-A1awx63txHLN5S06GOKkxOIH541rtYUwyuldIvXKI_vj6YX7WXmP5IYnDPNrPxtT_w5nDLG4nSARSw0aWQQDD73eNGir-lEzUztpfk3CTTGjd52a-ea42BuJ73iETcV3-HKUqRrg7J1xpbaRe3OUNvO_SSiXs2-HOtPBH6WP1EkI-gOrDmQ-XOfqokvQNHMqHW02G4Tl675trpw88zi6HY_lGoJi7ajmdJ_CczMbeqNmUkb53kVgyu3YlE6YsNvAMhJOXSDAgTGP0Ne-x___wZ85M3aUfvd9c4BUMKMUZPnJvKfV4iIh0NTWyZdlujmZ3kS1_tmHV7TRPplfXbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو کمیسیون امنیت ملی مجلس: محاسبات غلط، دشمن را به بیراهه برد
🔹
اسماعیل کوثری : مبنای اطلاعاتی دشمنان غلط بود، آن‌ها تصور می‌کردند که می‌توانند در عرض چند روز کار نظام را تمام کنند اما همین اطلاعات نادرست باعث شده است که آن‌ها اکنون در گردابی گرفتار شوند که حقیقتاً راه برون‌رفتی برای آن نمی‌یابند.
🔹
اکنون کارشناسان نظامی و سیاسی آمریکا به‌طور مستمر و علنی اذعان می‌کنند که ترامپ، با آغاز این جنگ مرتکب بزرگ‌ترین اشتباه خود شده است. بی‌تردید اطلاعات غلط، چه در حوزه نظامی و چه در سایر موضوعات، همگان را به بیراهه می‌کشاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/451743" target="_blank">📅 23:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451742">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f6f3ba24d.mp4?token=s-Bd39YYNctyjFc6uIlbpV9s2FwjSv59RgvGqfdOslk-BPtuEqM4vjaNJE_yujdb9ao3yPC24MrvSRt8Z7EaBuwTPSlNWeRP-Jp5-4VjNl6czIpHJBqkvHE6KTgpZq01usq7Ubt-hAGC74g4M4AYWuTd3mFVsSnbqxC-S-GNg-7TEzz2PraJ4nse_6Wc05AJG-q_PWV1MAPdmXbASqB1pRi1ww_FIKKls28Um_BFmvu_CHsJuHnTHEnDLuX1gEFQFRdQeTcHVcuAuM-OEdSypmOENOMQAZptWsCXjcvmXcTqrNSKJxrQOdH6rq3Kj7ZQizQls1vSOKlQigUxIL-SkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f6f3ba24d.mp4?token=s-Bd39YYNctyjFc6uIlbpV9s2FwjSv59RgvGqfdOslk-BPtuEqM4vjaNJE_yujdb9ao3yPC24MrvSRt8Z7EaBuwTPSlNWeRP-Jp5-4VjNl6czIpHJBqkvHE6KTgpZq01usq7Ubt-hAGC74g4M4AYWuTd3mFVsSnbqxC-S-GNg-7TEzz2PraJ4nse_6Wc05AJG-q_PWV1MAPdmXbASqB1pRi1ww_FIKKls28Um_BFmvu_CHsJuHnTHEnDLuX1gEFQFRdQeTcHVcuAuM-OEdSypmOENOMQAZptWsCXjcvmXcTqrNSKJxrQOdH6rq3Kj7ZQizQls1vSOKlQigUxIL-SkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع پرشور بروجردی‌ها در حماسهٔ ۱۴۳ خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/451742" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451741">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323a6a4a89.mp4?token=IgZiSa9l6hSMMtp9oUIcu6UWbVyprcgWcJPbWsER_2ZttaXCjIWTNAtBlBRSRDT4xbf6dd6ow49KYNK3RORdG4EikeAAxXT_G4FPHdv2gJsgL3FqjKdn0MK5T1cU5m7YDrheOLM6Ie1kR3h05QUQfKaJR2ngzmRnnX5TeBUAXjnUGjehiPJLBqte55yogbxj4Os_J-bCVQWuviH3jF0PVR6Msjzye_WON5Jt-nW8wshXeXHxmwFZEhLiLh4ufhOgDVrkoYeT2sU5oBr0MwU23BFsllxI5XD6-GHOVOKXr4AYpOE_Oej7SNUo54tfN2-SSNNYhd417joDZPRzDXObQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323a6a4a89.mp4?token=IgZiSa9l6hSMMtp9oUIcu6UWbVyprcgWcJPbWsER_2ZttaXCjIWTNAtBlBRSRDT4xbf6dd6ow49KYNK3RORdG4EikeAAxXT_G4FPHdv2gJsgL3FqjKdn0MK5T1cU5m7YDrheOLM6Ie1kR3h05QUQfKaJR2ngzmRnnX5TeBUAXjnUGjehiPJLBqte55yogbxj4Os_J-bCVQWuviH3jF0PVR6Msjzye_WON5Jt-nW8wshXeXHxmwFZEhLiLh4ufhOgDVrkoYeT2sU5oBr0MwU23BFsllxI5XD6-GHOVOKXr4AYpOE_Oej7SNUo54tfN2-SSNNYhd417joDZPRzDXObQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نجات بانوی ۴۰ ساله از عمق ۱۵ متری چاه فاضلاب در کاشان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451741" target="_blank">📅 23:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451740">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c74d42d8a.mp4?token=K-AFidC5RsxDsZ4TF2YC_p9c1DrPIgNUJp2EtGAlc1tFmWRxZF-mtQw46G93HcrOd0UAAesflkuf9u5MJA0fsaOrAnOFPOElT9zlCYzF-aoOtoC5tW3uLpBdcB1FB5abCeuKQ47tISUoLNHi6KuWYnoV3rI2zkrOACGHQTMVHfI_DNknp8Q4rsedmVYYoevNxurftogMZdwmQGT5MWv7floNmKhtxE1FytLroQehDyh-d6AO9Rn5ZUuJj1QMZW5ardQb3czqaxnqlQk7rhauULDdfLwID9Jzr2sMpm4QSLThtpX1gyD0iSBw8nCvRrDQgK-oo4uja35NuhOC4YeQHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c74d42d8a.mp4?token=K-AFidC5RsxDsZ4TF2YC_p9c1DrPIgNUJp2EtGAlc1tFmWRxZF-mtQw46G93HcrOd0UAAesflkuf9u5MJA0fsaOrAnOFPOElT9zlCYzF-aoOtoC5tW3uLpBdcB1FB5abCeuKQ47tISUoLNHi6KuWYnoV3rI2zkrOACGHQTMVHfI_DNknp8Q4rsedmVYYoevNxurftogMZdwmQGT5MWv7floNmKhtxE1FytLroQehDyh-d6AO9Rn5ZUuJj1QMZW5ardQb3czqaxnqlQk7rhauULDdfLwID9Jzr2sMpm4QSLThtpX1gyD0iSBw8nCvRrDQgK-oo4uja35NuhOC4YeQHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرۀ ایمان تاجیک، سخنگوی عملیات وعده صادق از دیدار با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/451740" target="_blank">📅 23:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451739">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b146be1c.mp4?token=uhn2OmO-Oimm7xpkhCJI7VHpEqwnsyW4Tgrh1dmoc67AKHnK3d5yVEy5gUUQRmiORLj-dFNlmu43IgsA1zP0cB2fJ6sup4Mqa-c7SaFrjXZYgV8G_OKdFoNRduuxQCF_xoV_s60H3XXDh8VSZcRbBoLgkZDVLp4p8sNdWfnFN6HcTCKoZ24lEKtqogml5tcjprfc8uCBo5RQ-Yi4T8MGns_GzCTmZmGJT8ZnMuMbt8Z2lLzAGOevtJVWzgUpIUoWmtaQRf2tKp3PSdOUVvXsZ2pDCB1yNrbQDygQZD5Qb-Za274KvDb07VOR4mTLzPqBbDbiJpWKWX_yHlGUsQFkRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b146be1c.mp4?token=uhn2OmO-Oimm7xpkhCJI7VHpEqwnsyW4Tgrh1dmoc67AKHnK3d5yVEy5gUUQRmiORLj-dFNlmu43IgsA1zP0cB2fJ6sup4Mqa-c7SaFrjXZYgV8G_OKdFoNRduuxQCF_xoV_s60H3XXDh8VSZcRbBoLgkZDVLp4p8sNdWfnFN6HcTCKoZ24lEKtqogml5tcjprfc8uCBo5RQ-Yi4T8MGns_GzCTmZmGJT8ZnMuMbt8Z2lLzAGOevtJVWzgUpIUoWmtaQRf2tKp3PSdOUVvXsZ2pDCB1yNrbQDygQZD5Qb-Za274KvDb07VOR4mTLzPqBbDbiJpWKWX_yHlGUsQFkRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از انهدام ایستگاه پشتیبانی زمینی و مرکز نگهداری یک بالن جاسوسی آمریکایی در فرودگاه اربیل
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/451739" target="_blank">📅 23:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451738">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b385fa4aee.mp4?token=lgXwPCfiTf0u4jjTSZ7Gwxp8ubQtWvC7v1CxMBSaPXslLa4exbfPWrmxn4FOj-ee6y9snv4xG0O4hNPk9iG2RyraUtjcP5wUbmw7dXlvd6iiG-twK_nZoZ6Mlpm3S6ljzxXsX46aYSC2wS2a2HpES9lQq96HJhXkctwX-4ZJz7TF5VlWKr16-q2Gkk8GePXYBjD0q2aaZAxlneIo_2Xuhp8aOiPOMhZ6WwgBxWnylE8Se4Hek7K1KvH5IjU10IpVMWCB1nJDuvThdRORXzL0qv7iY8gwxZBekFr5XYuk6mQ7g2ggGMkKf6GVW4q3lth_XdLedKTvvPVsKP_3TJc8yWeFanpXojdqL6gLhMzp8hD7bokfDZMaNs9R_ez6b6e4W2dx5UcezDm1t7K8XXUVdxswqBnIH2O9Be5jry6zux59vhzw3mSgSZtso5nUUFuNVhll2rjroZ1xRTTKdfS-RQiJi7LFcKl7wd93seI5R_FnA8XNb7SSemKIhIrWPKSDkyy0-t-BrT2T8DAQeVAhnzBdd8Cr91u8hIrXIVAEyJd4p2t61Gw4R_T5eKIeHVoMeLxx48mRk1OBTXJi3xKat6Nv0yN2yVtdIhOvvKAogBUbYf5d-XyhhephvsUh-YuVqOva5DmFZW1bXc0pcecHK1I5lXIjgPcZAgMvmhRI_7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b385fa4aee.mp4?token=lgXwPCfiTf0u4jjTSZ7Gwxp8ubQtWvC7v1CxMBSaPXslLa4exbfPWrmxn4FOj-ee6y9snv4xG0O4hNPk9iG2RyraUtjcP5wUbmw7dXlvd6iiG-twK_nZoZ6Mlpm3S6ljzxXsX46aYSC2wS2a2HpES9lQq96HJhXkctwX-4ZJz7TF5VlWKr16-q2Gkk8GePXYBjD0q2aaZAxlneIo_2Xuhp8aOiPOMhZ6WwgBxWnylE8Se4Hek7K1KvH5IjU10IpVMWCB1nJDuvThdRORXzL0qv7iY8gwxZBekFr5XYuk6mQ7g2ggGMkKf6GVW4q3lth_XdLedKTvvPVsKP_3TJc8yWeFanpXojdqL6gLhMzp8hD7bokfDZMaNs9R_ez6b6e4W2dx5UcezDm1t7K8XXUVdxswqBnIH2O9Be5jry6zux59vhzw3mSgSZtso5nUUFuNVhll2rjroZ1xRTTKdfS-RQiJi7LFcKl7wd93seI5R_FnA8XNb7SSemKIhIrWPKSDkyy0-t-BrT2T8DAQeVAhnzBdd8Cr91u8hIrXIVAEyJd4p2t61Gw4R_T5eKIeHVoMeLxx48mRk1OBTXJi3xKat6Nv0yN2yVtdIhOvvKAogBUbYf5d-XyhhephvsUh-YuVqOva5DmFZW1bXc0pcecHK1I5lXIjgPcZAgMvmhRI_7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موشکی که در عملیات اخیر سپاه رونمایی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451738" target="_blank">📅 23:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451737">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">موافقت نخست‌وزیر جدید انگلیس با تداوم همکاری‌های نظامی با آمریکا در جنگ علیه ایران
🔹
بلومبرگ: نخست‌وزیر جدید انگلیس، استفاده از پایگاه‌های نظامی این کشور توسط آمریکا برای آن‌چه لندن «حملات دفاعی» علیه ایران می‌نامد را تأیید کرده است.
🔹
این اقدام ادامهٔ سیاست نخست‌وزیر پیشین انگلیس کی‌یر استارمر محسوب می‌شود، کسی که بارها به خاطر عدم حمایت کافی از حملات به ایران مورد انتقاد ترامپ قرار گرفته بود.
🔹
برنهام احتمالاً با انتقاداتی از سوی حزب سبز  و لیبرال دموکرات‌ها روبرو خواهد شد.
🔹
این احزاب با استفاده از این پایگاه‌ها مخالف‌اند، چرا که به نظر آن‌ها این اقدام، انگلیس را در یک جنایات جنگی شریک می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451737" target="_blank">📅 23:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451736">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8060ff907.mp4?token=gM8oWfpGSQmrNbkq7F-aHD3aNQ3OPxftiK_tnzHhiNHRkrxiQF2MX5YN6dq3RnoPWEdbLI8yvxfDyfkdoXGmJuoeyqZ3TQdn6KR-bmzHSv2rrPBsJmqj0OyA_xECcFRlu4wxlR_xttORnJ16LIXegdCFqw3V_SCxKIfe8hQnmesjYANaYNQsVCXXVX1-wZJ0lY6akA4TQdOr-eQ1u7KteFiH_FE8ZE1lQX0RZ2t7J0Cz88vI3zh9aBothpoTFzhHWNdTJdIAzHU9MIDTyTl_D83cjzy5ZasylQP7XbIAuXGxccdlIqFBoDOBeAXpRCr7t9J23riXq-LzpZTYMmDytw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8060ff907.mp4?token=gM8oWfpGSQmrNbkq7F-aHD3aNQ3OPxftiK_tnzHhiNHRkrxiQF2MX5YN6dq3RnoPWEdbLI8yvxfDyfkdoXGmJuoeyqZ3TQdn6KR-bmzHSv2rrPBsJmqj0OyA_xECcFRlu4wxlR_xttORnJ16LIXegdCFqw3V_SCxKIfe8hQnmesjYANaYNQsVCXXVX1-wZJ0lY6akA4TQdOr-eQ1u7KteFiH_FE8ZE1lQX0RZ2t7J0Cz88vI3zh9aBothpoTFzhHWNdTJdIAzHU9MIDTyTl_D83cjzy5ZasylQP7XbIAuXGxccdlIqFBoDOBeAXpRCr7t9J23riXq-LzpZTYMmDytw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۴۳ قرار شبانهٔ تربتی ها
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451736" target="_blank">📅 23:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451735">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a70c08ba.mp4?token=DFcR-XQJPaFD7bW5NVuCgJODOY6U67PlhFbl7GV-09Gf9vsh7ERN7mDTeyaPW6xb-NcroSd3P9h1oGlBQoE6DqY9hMjN7DsOnqgjYhSH4iYjqMW5lbSiUCJ_Dk_gtJ0FD1mFG4MR0lomBK1ASKbg3NpyKNpuL1rdSP3tNRUo-UmKKlPBTFce9JPigVgZGdp0SGNHDe4ixxRzkFKyTTqntNOoFOD3M1ph5oea6_pR8AsQMHDmPHlC8yVoOnx1AdgCOW-LLTTbAv_KlAnBa5r5Wkc1f8BqiP8pTATyC-RqSiVAB-RrBi6qmpd_SrWm0aHsLac9e9MQ2ErV4JqFSQ_t9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a70c08ba.mp4?token=DFcR-XQJPaFD7bW5NVuCgJODOY6U67PlhFbl7GV-09Gf9vsh7ERN7mDTeyaPW6xb-NcroSd3P9h1oGlBQoE6DqY9hMjN7DsOnqgjYhSH4iYjqMW5lbSiUCJ_Dk_gtJ0FD1mFG4MR0lomBK1ASKbg3NpyKNpuL1rdSP3tNRUo-UmKKlPBTFce9JPigVgZGdp0SGNHDe4ixxRzkFKyTTqntNOoFOD3M1ph5oea6_pR8AsQMHDmPHlC8yVoOnx1AdgCOW-LLTTbAv_KlAnBa5r5Wkc1f8BqiP8pTATyC-RqSiVAB-RrBi6qmpd_SrWm0aHsLac9e9MQ2ErV4JqFSQ_t9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع ۶۲ قطعه از پیکر تازه تفحص‌شده شهدای دانش‌آموز میناب در بندرعباس  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451735" target="_blank">📅 23:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451734">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c339993d87.mp4?token=gS0PVIbKXknxJ5DY-R-6ZIgFQVkQIIopQMPfbjvU8SHaU8729aWlPQaPo1nQQ9SvnEYFCJKwbf9zQ8AAiHjAj4je1KnZcj17s2FvjMwFLJiUMvoJn58V6VVdeYJASNw7wjbJ4WD1_hcZ4QzJpOUipLoCrIkD66or8yFhaL1sZTmEzy5TV5b5yTonaqiuLkwkIT8LwykrCj14y_CgC1spWwlSz_Mpx6EcBQPwN6PuTnvfB_bGRHLFGCMM-xp2kYSeVAQWlb_IlfTQ0YddcWrxxeU_QbWx29kzH_w3lzceFD1AneuI4WycL-LWZB3umCzCHGV9FfvfCewVfiziO81nEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c339993d87.mp4?token=gS0PVIbKXknxJ5DY-R-6ZIgFQVkQIIopQMPfbjvU8SHaU8729aWlPQaPo1nQQ9SvnEYFCJKwbf9zQ8AAiHjAj4je1KnZcj17s2FvjMwFLJiUMvoJn58V6VVdeYJASNw7wjbJ4WD1_hcZ4QzJpOUipLoCrIkD66or8yFhaL1sZTmEzy5TV5b5yTonaqiuLkwkIT8LwykrCj14y_CgC1spWwlSz_Mpx6EcBQPwN6PuTnvfB_bGRHLFGCMM-xp2kYSeVAQWlb_IlfTQ0YddcWrxxeU_QbWx29kzH_w3lzceFD1AneuI4WycL-LWZB3umCzCHGV9FfvfCewVfiziO81nEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از فرمانده‎ای که از سال ۶۳ به‌دنبال اقتدار موشکی ایران بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/451734" target="_blank">📅 22:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451733">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سپاه: مجموعۀ تاکتیکی رادارها در پایگاه علی السالم و جزیرۀ بوبیان از رده عملیاتی خارج شدند
🔹
سپاه پاسداران: ملت قهرمان و ستم ستیز ایران اسلامی با عنایت خداوند متعال و دعای خیر شما مردم ایستاده در میدان، رزمندگان غیور سپاه در ادامه موج ۲۴ عملیات نصر۲ و در ادامه پاک‌سازی منطقه از رادارها، با تهاجم به یک رادار هشدار اولیه ، یک مجموعه رادار تاکتیکی در اطراف پایگاه علی السالم و یک سامانه راداری دیگر در جزيره بوبیان کویت، این رادارها را منهدم کرده و از رده عملیات خارج کردند.
🔹
عملیات تنبیه متجاوز ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451733" target="_blank">📅 22:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451732">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc98b2e8d.mp4?token=nuFgd5Oxf-Vqa9f-zqaV1TUYXg5zrNarInqlNv2Lc3WnjqaUETEUr-LRh7f24SJPYv_TRO5RzJN4p0Fp63Dl1Clu1JfLIfprV-zsHD6GrTWF-li9Icuf7EPcbLPgyWTnEgOjfiG5zF76VUKAxcJ_PqchldT5L388nOtK9bWcNH2xfUmB4PkxgtIWgA1MAi6hH28_3_2INMw5f0ScKS82uEszFfo8ModYpo1HgaWEOT9gRrQvsPqwuOqjTynP-AxHrPY_69YOqIDW8VrScxgSJhuQj78O7zvyqlcaI0WfXbuXz3lbfgDK7dE2AS144T3D9vYFeEkOcxEqVDQ8wz2E7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc98b2e8d.mp4?token=nuFgd5Oxf-Vqa9f-zqaV1TUYXg5zrNarInqlNv2Lc3WnjqaUETEUr-LRh7f24SJPYv_TRO5RzJN4p0Fp63Dl1Clu1JfLIfprV-zsHD6GrTWF-li9Icuf7EPcbLPgyWTnEgOjfiG5zF76VUKAxcJ_PqchldT5L388nOtK9bWcNH2xfUmB4PkxgtIWgA1MAi6hH28_3_2INMw5f0ScKS82uEszFfo8ModYpo1HgaWEOT9gRrQvsPqwuOqjTynP-AxHrPY_69YOqIDW8VrScxgSJhuQj78O7zvyqlcaI0WfXbuXz3lbfgDK7dE2AS144T3D9vYFeEkOcxEqVDQ8wz2E7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراغه در شب ۱۴۳  فریاد حمایت از وطن و نیرو‌های مسلح
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451732" target="_blank">📅 22:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451731">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9wF89djpRAKQDUvoJDvHTJDrm0-RWxzf4QNCgZ9YzRAQ5Nlhdw3hi8-gWqT92Ju8R8m6inOfITVUhpPpKYGGeKdeu_-m22iLZA6xu5QXHQ4Aeax-lMwB89UZESEjxBsr7saIiWZoLLyTEZCJ4hQzryFuUhIyz9GYIJo0-1OLF02TcP6gSgYNAVtiaUgsisQhbvhhtzwFdr3S7MvT8JlRmdqEG3gDsISASx1GbmvQzgFULbSlLghsZw4HzVFQDokxs59bJVEvqCTvvNhhesS830OyGSz4vAzdT_0zGM318NnhldKh_SKTI2TDo2z9PichrayQiB84_V6c9BGD2EOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم بزرگداشت شهید مصباح‌الهدی باقری‌کنی به میزبانی خانواده شهید
◾️
فردا؛ از ساعت ۱۷؛ مجتمع امام صادق(ع)؛ شهرک غرب، بلوار دریا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/451731" target="_blank">📅 22:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451730">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPXI5YahjY34lHaYT0RvKtIitCnj-51vqAhLL3INUhdXzfFbm-_kFoeyB5aM0tcXKKujB6c6Car0q1tnxidgYNezsomfVio6bixDxVM7vJ6eHLhKf_c4DPRHeJDGiI9Tpz6RIhzPjLAuU4nb2Afw0SZd4E_Pm-nJge4nJU-Ztk_9EKVM2CNDgAkD1opDB8buH2Wu2_BeztG2gbSaojw5abxc7qzpLdTeiLU61tKnIu_vcXasQsbXT8aDqcCOM1N8NZzfUS-jWgP6rOAjLeK5IoeZhdbQkANpT8DuF60xB6mo0eS1T8AYme5EUEvFMJmW8fktZPo3-tWsFaCTkIlYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتشار اسناد اعلان قرمز اینترپل علیه سران گروه‌های تروریستی کُردی
🔹
برای نخستین‌بار اسناد مربوط به اعلان‌های قرمز اینترپل، احکام قضایی و درخواست‌های استرداد شماری از سران و اعضای گروه‌های تروریستی کُردی منتشر شد.
🔹
براساس این اسناد، درخواست‌های ایران در پلیس بین‌الملل پذیرفته شده و برای تعدادی از متهمان اعلان قرمز صادر شده است.
🔹
این پرونده‌ها در چارچوب همکاری‌های قضایی و پلیسی بین‌المللی درحال پیگیری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/451730" target="_blank">📅 22:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451729">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
لطفاً در خصوص پرداخت معوقات بازنشستگان تأمین اجتماعی پیگیری لازم را انجام دهید. با توجه به وعده‌های پرداخت معوقات در ماه‌های گذشته و عدم تحقق آن، سطح نارضایتی بین این قشر زحمت‌کش به حد اعلا رسیده است. امید است با پیگیری از مسئولین مربوطه، مرهمی بر درد این عزیزان باشد.
🔹
نیروهای شرکتی ظفر کویر دامغان و کومش کار از تأخیرهای مکرر در پرداخت حقوق، بلاتکلیفی معوقات و نبود قراردادهای شفاف و قانونی گلایه‌مند هستند. این کارکنان با وجود نقش مهم خود در حفظ و پایداری شبکه مخابراتی، انتظار دارند حقوق قانونی‌شان به‌موقع پرداخت شود و امنیت شغلی آنان مورد احترام قرار گیرد.
🔸
لطفاً قیمت فیش‌های حج را پیگیری کنید. حدود یک ماه است که پیگیر هستم. حتی با یکی از فروشندگان به نظر می‌رسید به توافق رسیده بودیم اما قیمت‌ها هر روز به شکل عجیبی افزایش می‌یابد و آن شخص هم از فروش با قیمت توافق‌شده منصرف شد. قیمت‌ها از حدود دو ماه پیش حدود ۱۷۵ میلیون تومان بوده که حالا به ۳۰۰ میلیون تومان رسیده است.
🔹
بهمن‌ماه سال گذشته برای پیش‌خرید کامیون ثبت‌نام کردیم. قیمت ثبت‌نام ۴.۸ میلیارد تومان بود اما در زمان تحویل، قیمت را به ۸.۱ میلیون تومان افزایش دادند. وقتی برای اعتراض به افزایش قیمت مراجعه کردیم با ما برخورد نامناسبی شدیم.
🔸
اینجانب ۱۴ سال است متقاضی مسکن مهر شهر پردیس، فاز ۸ پروژه شمس راه ماهان، بلوک ۳۷۰.۱.۱ هستم. پروژه توسط شرکت مادرتخصصی عمران پردیس اجرا می‌شود. پس از ۱۴ سال، تمام وجه را کامل پرداخت کرده‌ام، سند ۵ برگی و سند خرید عرصه را هم در دست دارم، اما هنوز هیچ خانه‌ای تحویل نگرفته‌ام و هیچ مقام مسئولی پاسخگو نیست.
🔹
بنده ساکن منطقه ۱۰ شهرداری تهران، خیابان گلستانی، کوچه صباغ‌زاده هستم. مدت چندین ماه است از تلفن ثابت محرومم. بارها با شرکت مخابرات منطقه تماس گرفته‌ام اما متأسفانه هیچ اقدامی انجام نشده است. با این حال، ماهانه هزینه آبونمان از حسابم کسر می‌شود. لطفاً در این مورد اقدام لازم را انجام دهید.
🔸
لطفا عدم واریز وجه کالابرگ برای کسبه را پیگیری کنید. خیلی از فروشگاه‌ها کالابرگ را غیرفعال کردند، ما هم به زور ادامه می‌دهیم.
🔹
هیچ کدام از سهمیه‌های سوخت اسنپ و تپسی اصلا نه پرداخت شده نه محاسبه نشده است.
🔸
علی‌رغم درست شدن بیشتر موارد سامانه بانک ملی (بام)، ولی سامانه درخواست تسهیلات غیرفعال است. این درحالی است که مردم سرمایه خود را چندین ماه است در این حساب‌ها گذاشتند تا معدل حساب خورده و وام دریافت کنند. لطفاً صدای ما را به گوش مسئولین بانک ملی و بانک مرکزی برسانید.
🔹
خواهشمندیم درباره موضوع خاموشی‌های طولانی‌مدت برق در گلستان صالحیه، بخش بهارستان شهرستان رباط کریم خبررسانی کنید. مشکل بزرگ این است که آب شهرستان بدون پمپ برق تأمین نمی‌شود. هر روز در این گرما زجر می‌کشیم.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/451729" target="_blank">📅 22:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451728">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4iJHQnpNYpUQUq7Myvco7QIeuFlWUXCJHge6HKhkfsGdF11diTmFV7isf8JdeQU_hblm_QKedT8a_hy3Mvc2TQDu0urTzGEF54QTJid34XNYbxVAe3avACE2C33Je7VIKFD9Zuq_99Nwz0HerAztlzjvf9_JYY4Oo0bUNNjxcdOqF27BKIrIqsZgqWVzMsxXuEjeVyzXQWdziRqbCpM9uJcN8C33CezfMkSm-vwyCGvhRYiUmdphx4tZ7B7gZyu-luy5DYD69IzzvWFZ4xgH3IHeZQpqjsWcdol2GSwrBAznTX3IbKDTBVCWfbENT72sf6MxObE1qrdbM7Te8mrCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: جولانی مایل است با حزب‌الله مقابله کند
🔹
او مدت‌هاست دارد با حزب‌الله می‌جنگد. فکر می‌کنم کار بسیار مؤثری باشد، بنابراین موضوعی است که من دارم به آن فکر می‌کنم. @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451728" target="_blank">📅 22:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451727">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSoO2F8nDwDG5yKFiJHxWuhmTbIY9YyCe6wjr_stIqOMol9cjz4bpXcwyHLyD0t88vFmxO3LgDv4F1crP5UZQZGHy4PX6IzH8XeXNSWOi7CmjOHdhYPHvnsw61dsLFwx0Hs47LGhSshjaSmEt-4NZLVI3lB8LxFTznAp3QGCnPCet2nbyA3R3XX7HM52JYa_6qQO9tRHb6Jd3v3Xiae4h7kNSbydCX7MxEHpY7CCikQqBXH24SYvPRXfJNcOYlx6zBWERzywskdejStmAkkUcVmN0ag48tvdAhl1RZHKRiD6nU3S_DAIlsR1M_Oc9BNRYXI_tYpQQSv8ROYaxNx4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ این بود پاسخ مهمان‌نوازی ایران از کویتی‌ها؟
🔹
سال ۱۹۹۰ و پس از حمله صدام حسین به کویت، شماری از مردم این کشور به ایران پناه آوردند. ایران که تازه از جنگ تحمیلی خارج شده بود، با وجود همه سختی‌ها، از آوارگان کویتی در شهرهای مختلف میزبانی کرد.
🔹
ایران همان…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/451727" target="_blank">📅 22:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451726">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgWlU7KVBx1WB4Zpvg86HoqIzGrLp2-_XxwuJgvRmdUl7Yseiyp__iqpY9-ddE9PCYs9ZIsXhNfdW91BjqrNk-WBgg-OqTG5CQTSkhEzps-ow-YDyBOPXjHZJR7sbwRcFJFeJrfhHGFDjd6Ic3zQFs9NovlhsqtXDIkBkCPDrQwGaPngSq0NfPOEkUUopNsWDcCqSJUWezy7h5uQnNmvf1wQm9ulYygS2kPIS78r5GVbp2VR8ND_fL8EZzhkVlxFW2LadY_Xe3uFyQcTTb7PulMW-4rx5CDaY6DYGU3X4AKVDjXXXwIj-R3bbX6pM0iLfuNcgJgdTeS0hLlmGQOXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صید ۹ مدال توسط شناگران ایران از آب‌های تایلند
🔹
تیم ملی شنای ایران در دوازدهمین دوره مسابقات قهرمانی رده‌های سنی آسیا به میزبانی بانکوک تایلند موفق به کسب ۹ مدال شد.
🔹
۲ مدال طلای ایران توسط محمدمهدی غلامی در ماده ۱۰۰ متر پروانه و علیرضا عرب در ماده ۵۰ متر قورباغه به دست آمد.
🔹
تیم ۱۰۰×۴ متر آزاد با ترکیب کیارام کیانی، امیرعلی ثابتی، محمدمهدی غلامی و دانیال جهانگیری و تیم ۱۰۰×۴ متر مختلط تیمی با ترکیب پارسا شهشهانی، علیرضا عرب، محمدمهدی غلامی و دانیال جهانگیری، هر ۲ به مدال نقره دست یافتند.
🔹
۵ مدال برنز شنا نیز توسط دانیال جهانگیری در مواد ۲۰۰ متر آزاد و ۱۰۰ متر آزاد، پارسا شهشهانی در ۲۰۰ متر کرال پشت، امیرعلی ثابتی در ۵۰ متر آزاد و ماده ۱۰۰×۴ متر آزاد تیمی با ترکیب کیارام کیانی، محمدمهدی غلامی، امیرعلی ثابتی و دانیال جهانگیری کسب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451726" target="_blank">📅 22:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451725">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ff5728bb.mp4?token=fcHvY3y9G_vv0Q_Bz1yoBqjokxphF2NCD9o7Fkxak7VBR03IqPiBMQTUmzRZcL-MhFVBbXTynnmyFHTGVk0zWjx6AjTumIkDOyX9i3w_YXeAUBQgj41K3PThepd85agxNUoB7a5cVEMKeqCDWXtJ7A2RZrSmV3GkdMEfFAJiEr-8Xo-Q47fuXfUf-rZRLeD5t9U34czzuh355ILwc1lMPl-QQiWkjTY0J0omYvChRhrOvspLPrrUZQuN3eE7fgI0X7WRkVxtNCbceEb4bUwYFdis9SrLU2rlfFk3-4bKjf9l4ng7fcZmnOeYXCxrPjbVLclg_unqOYjWfzraeJHb2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ff5728bb.mp4?token=fcHvY3y9G_vv0Q_Bz1yoBqjokxphF2NCD9o7Fkxak7VBR03IqPiBMQTUmzRZcL-MhFVBbXTynnmyFHTGVk0zWjx6AjTumIkDOyX9i3w_YXeAUBQgj41K3PThepd85agxNUoB7a5cVEMKeqCDWXtJ7A2RZrSmV3GkdMEfFAJiEr-8Xo-Q47fuXfUf-rZRLeD5t9U34czzuh355ILwc1lMPl-QQiWkjTY0J0omYvChRhrOvspLPrrUZQuN3eE7fgI0X7WRkVxtNCbceEb4bUwYFdis9SrLU2rlfFk3-4bKjf9l4ng7fcZmnOeYXCxrPjbVLclg_unqOYjWfzraeJHb2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشت‌پرده فراخوان جعلی «محاکمه رئیس‌جمهور و اعضای شعام»
🔹
در روزهای اخیر، فراخوانی با عنوان «فراخوان ملت مبعوث برای محاکمه رئیس‌جمهور و اعضای شعام» در فضای مجازی در حال انتشار است.
🔹
تحلیل دقیق روندها و شواهد متقن نشان می‌دهد که این جریان، یک سناریوی هدایت‌شده…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451725" target="_blank">📅 22:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451724">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e86268f86.mp4?token=V-NmYIolbHUdlPWUG_NKyTpuhvLbDl2PMRJCWCOuYvGjf_wuvlsCQM9UNvLO_ff_-3eRt0HAI1SCVGjcBcRRmv-J4z7m9bDWqzLWKtEcconaG_vlooIc54S6l-LFPWhU8ZPrQWaI73GkfDMw61DqbGyu-5h8rSTodmm4_edGWtmAh7rtPO1m15cG8Hun-THqMeeh1T8xvT1VORwP90_en2a_j9siLYHTqk7lEcp7qjKTgMAcBMClFUzhYZIWazB00AHgo95P1FS2lk9tKF0eVCozI4Fx1yoihaFaBfzRUHUwQo7nUgWJ_eL0kOlcOQibMBzhLQuwJkEB4J_tZnJdXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e86268f86.mp4?token=V-NmYIolbHUdlPWUG_NKyTpuhvLbDl2PMRJCWCOuYvGjf_wuvlsCQM9UNvLO_ff_-3eRt0HAI1SCVGjcBcRRmv-J4z7m9bDWqzLWKtEcconaG_vlooIc54S6l-LFPWhU8ZPrQWaI73GkfDMw61DqbGyu-5h8rSTodmm4_edGWtmAh7rtPO1m15cG8Hun-THqMeeh1T8xvT1VORwP90_en2a_j9siLYHTqk7lEcp7qjKTgMAcBMClFUzhYZIWazB00AHgo95P1FS2lk9tKF0eVCozI4Fx1yoihaFaBfzRUHUwQo7nUgWJ_eL0kOlcOQibMBzhLQuwJkEB4J_tZnJdXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های لبریز از جمعیت، پشتیبان قدرت نظامی ایران
🔹
صحنه‌هایی از حضور پرشور مردم در ایستگاه ۱۴۲ تجمعات  مردمی.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451724" target="_blank">📅 22:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451723">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">شبکه ۱۴ اسرائیل از اصابت به سفارت این رژیم در منامه خبر داد و مدعی شد که این خبر قطعی نیست و «این حادثه در دست بررسی است».
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/451723" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451722">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
🔴
منابع عراقی: درپی حملات پهپادی و موشکی امشب، آمبولانس‌ها و خودروهای امدادی وارد کنسولگری آمریکا و فرودگاه اربیل شدند. @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/451722" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451721">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4c8036bc3.mp4?token=DAvknYKpoz581IBadAvZeDDHDrYJM_fFHkmQpXtIg8vwKt8IvcrJtDrZXpeylPTZU6LsXbUy_PMWDztxd47BBMlWLSErY00_CfHp2VpuWc9jQhPCq_TOSynnlU6bhEhVppt6IBEzKXZ12ncWBLcgM134IJRPpBm9JCY6y6VOKy08B9eR2_NbN5-HX48cfmkqzud2Sp_Yh4bKLoA90P2fpCZI6Z8kGWmMeGxBLbVIKZJtWO25Ijn_8KFvkVVFzlzsyHR5h2ErT11w2CWkyxQOfEJFniRJYRV6QOgUwb0LgE8dwJyytTU63aBwXrox4ldx1hzT13MoQrzOa4lUZD2ALQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4c8036bc3.mp4?token=DAvknYKpoz581IBadAvZeDDHDrYJM_fFHkmQpXtIg8vwKt8IvcrJtDrZXpeylPTZU6LsXbUy_PMWDztxd47BBMlWLSErY00_CfHp2VpuWc9jQhPCq_TOSynnlU6bhEhVppt6IBEzKXZ12ncWBLcgM134IJRPpBm9JCY6y6VOKy08B9eR2_NbN5-HX48cfmkqzud2Sp_Yh4bKLoA90P2fpCZI6Z8kGWmMeGxBLbVIKZJtWO25Ijn_8KFvkVVFzlzsyHR5h2ErT11w2CWkyxQOfEJFniRJYRV6QOgUwb0LgE8dwJyytTU63aBwXrox4ldx1hzT13MoQrzOa4lUZD2ALQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفحص ۶۲ قطعهٔ دیگر از پیکر شهدای مدرسهٔ میناب؛ ماکان هنوز مفقود‌الاثر است
🔹
فرماندار میناب: درپی عملیات تفحص در مدرسهٔ میناب در چند هفتهٔ گذشته، ۶۲ قطعه از پیکر شهدای دانش‌آموز کشف شد که پس‌از آزمایش‌های ژنتیکی مشخص شد که این قطعات متعلق به ۳۲ دانش‌آموز است.…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451721" target="_blank">📅 21:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451720">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
🔴
منابع عربی: صدای انفجارها از نیم ساعت پیش در اربیل قطع نشده و چند موج موشکی مقر تروریست‌های ضد ایران را مورد هدف قرار داده است. @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451720" target="_blank">📅 21:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451719">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-zyoUi6O_eh0d78riL4NTT7ck4J0V4_yvmtu-chbCyqw06m4r8NOdstfHNCQ2UUmfyEPnR75oTfXFN7T4IknQlm5iAuYwmoQzNHBgPxXK6p7T1z48Z9X5AExiHofHdfhJ_dcO8dSjCuuhbGw1atlhSg3eVoriyG1jwk9QLYq_YW5KOZm1Y6sTdtJBWYrA57HXJkkWajdYiAW1uAb2YPgvS9euy9z5PlJ3Q_iorFl8PfMl3pmp_9mdyFPhIoPts96sCcdApWfvIN3925jQvGrVwvyJCkHgs8-G_5bm5UJup5FwTPxFKc2DoMbbF2J0Ni5yFwlomcKkMSObLkOOnqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بذرپاش: برنت را می‌شود با بلوف تکان داد اما هرمز را نه
🔹
واشنگتن در بازار کاغذی قمار می‌کند ولی تهران «ریسک عبور» را در بازار واقعی قیمت‌گذاری می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451719" target="_blank">📅 21:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451718">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0add65574.mp4?token=bePzL6WD1Eo54GiULFBvMj5kc40APiRuXzbxbX9ojgNq9drDRjoHF8MSpoaVjzn5hV5prx-Ifl03dtuwt7aAacqISSVUjRJQhQbLU6jF9haRUspvdiGxPmWTpaD3mBXPaaqTyTOLipjzI5LMiYZILpMC_6nXRJec4k8C2XNm9IaKiyEYlYa4ZViOJbaSY3wzQ30HcSiJaRE7lZMT-kLdNn1t8IV-bjoFhySzwr0IyjyPXt_Me_lxQJ8-JRoN4T3DqU3b5YMvTxHUeC-qXVVDpoAFq9A7Cej8teFEf7AfUsiwZYhdRYAsFk65yS6OIebyD-cSN3kBK1oU4ZcvYFl_sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0add65574.mp4?token=bePzL6WD1Eo54GiULFBvMj5kc40APiRuXzbxbX9ojgNq9drDRjoHF8MSpoaVjzn5hV5prx-Ifl03dtuwt7aAacqISSVUjRJQhQbLU6jF9haRUspvdiGxPmWTpaD3mBXPaaqTyTOLipjzI5LMiYZILpMC_6nXRJec4k8C2XNm9IaKiyEYlYa4ZViOJbaSY3wzQ30HcSiJaRE7lZMT-kLdNn1t8IV-bjoFhySzwr0IyjyPXt_Me_lxQJ8-JRoN4T3DqU3b5YMvTxHUeC-qXVVDpoAFq9A7Cej8teFEf7AfUsiwZYhdRYAsFk65yS6OIebyD-cSN3kBK1oU4ZcvYFl_sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوش‌چشم، کارشناس مسائل استراتژیک: نقد‌هایمان را «مشفقانه» بگوییم؛ باید از شخصیت «عراقچی» و «قالیباف» حفاظت کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451718" target="_blank">📅 21:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451717">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/154a846214.mp4?token=I8KKsQyFqXWrSN_6bnwNffeI_w8EOuHaM9DmFb3KI4JTPO4OXvp-Jtz3ASBEYtrX_gxv_uAnfPTeRr4PzgUvgPB69lM9DpPKszL1KC6ImzuvIPtu23ROBNIt-JR0sI-qZuAjG2AiOacbbaRLHJuywB1_U77VttMACANXSpLFb7d7o3--I-V1ZNDSAufSoUlyeuCvH2xCdwj2gJCoeVgXPSHzyJC1Emjlmn6cHR76iLobwMvAtGZJg-bSmsvVDXk5lbwYtJIhL7L5-wjTolRzaas7t5pd7jZ6ZbfmkK2muuAvAY2GSFregQXpWfNq0skSfpCp2mg5R3qtBgCpPCJiIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/154a846214.mp4?token=I8KKsQyFqXWrSN_6bnwNffeI_w8EOuHaM9DmFb3KI4JTPO4OXvp-Jtz3ASBEYtrX_gxv_uAnfPTeRr4PzgUvgPB69lM9DpPKszL1KC6ImzuvIPtu23ROBNIt-JR0sI-qZuAjG2AiOacbbaRLHJuywB1_U77VttMACANXSpLFb7d7o3--I-V1ZNDSAufSoUlyeuCvH2xCdwj2gJCoeVgXPSHzyJC1Emjlmn6cHR76iLobwMvAtGZJg-bSmsvVDXk5lbwYtJIhL7L5-wjTolRzaas7t5pd7jZ6ZbfmkK2muuAvAY2GSFregQXpWfNq0skSfpCp2mg5R3qtBgCpPCJiIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسئول ستاد مرکزی اربعین: تا به امروز نزدیک یک میلیون و ۲۵۰ هزار نفر برای زیارت اربعین در سامانۀ سماح ثبت‌نام کرده‌اند
🔹
برخی مردم به‌دلیل حضور در اجتماعات خیابان برای حضور در اربعین تردید داشتند که با پیام رهبر انقلاب مشخص شد حضور در اربعین هم بخشی از میدان است.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451717" target="_blank">📅 21:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451716">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e655d9a666.mp4?token=eVa71qGQCD4nYUaXbw9IkQ-FJToLY024efGx-5-zw_jpX1xRN7EsTv68OMKDlB8CDR1hwBna8iOI5mChAFUeLUsK3ZD4kVzeGUhWVwZ7hwhvbxUM-SqsgWJvYnByeLaEHbCrR4TIbaSAyy2s60UOi4QdGtrhcfUK0WzxJnUn7DNz8EdlU40fTt4OwGJjCDsivyV-YcZNjre5eywVMG0Oz4KgXR8zCUZw3FNS5Q3VNIJwqJkRajOOw_2k7YVmFfOlHPBe-MibedfJ41KNKcLQ_j0vZXaaxw9L0rTGkJkhqy1cXJH-ER8387Y3_amZwep-tK_bzrz0ZOvZimjLwjUOdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e655d9a666.mp4?token=eVa71qGQCD4nYUaXbw9IkQ-FJToLY024efGx-5-zw_jpX1xRN7EsTv68OMKDlB8CDR1hwBna8iOI5mChAFUeLUsK3ZD4kVzeGUhWVwZ7hwhvbxUM-SqsgWJvYnByeLaEHbCrR4TIbaSAyy2s60UOi4QdGtrhcfUK0WzxJnUn7DNz8EdlU40fTt4OwGJjCDsivyV-YcZNjre5eywVMG0Oz4KgXR8zCUZw3FNS5Q3VNIJwqJkRajOOw_2k7YVmFfOlHPBe-MibedfJ41KNKcLQ_j0vZXaaxw9L0rTGkJkhqy1cXJH-ER8387Y3_amZwep-tK_bzrz0ZOvZimjLwjUOdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انتقام قطعی است
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/451716" target="_blank">📅 21:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451715">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🎥
لحظۀ اصابت موشک به مقر ترویست‌ها در اربیل  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451715" target="_blank">📅 21:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451714">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc36988cef.mp4?token=ZqVXsEUi8qtAeoI0FivW3xyvNtoWE6lAVMsh4_RtbY4AD0k3yoKqJALX9C6U4NXxkYJms8CvLq-odyjIQPYZGWxN91FszwbgkEhUrmgwTvazj6bmt0gSZ51TnpKyzNq9gewnaCEZ_LCUmwZKGNe4IbxBKYGB-nLCQsdFfQmsLAFCb1G1c2bx_v0ITYvGnQSeOrKu76QH7MoRfTwOfXzSZWo3y3hg4mblK223RAjII1JV0VouoQs3K4eWkOUh508kRGIyM572Ud51vq2reL5uW1WaInq9uyFNwof2iIW44ws8E6gY00qRJj6WqLBFUFUctKrE25rqSHZh2kTbDC6GRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc36988cef.mp4?token=ZqVXsEUi8qtAeoI0FivW3xyvNtoWE6lAVMsh4_RtbY4AD0k3yoKqJALX9C6U4NXxkYJms8CvLq-odyjIQPYZGWxN91FszwbgkEhUrmgwTvazj6bmt0gSZ51TnpKyzNq9gewnaCEZ_LCUmwZKGNe4IbxBKYGB-nLCQsdFfQmsLAFCb1G1c2bx_v0ITYvGnQSeOrKu76QH7MoRfTwOfXzSZWo3y3hg4mblK223RAjII1JV0VouoQs3K4eWkOUh508kRGIyM572Ud51vq2reL5uW1WaInq9uyFNwof2iIW44ws8E6gY00qRJj6WqLBFUFUctKrE25rqSHZh2kTbDC6GRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
منابع خبری از شنیده‌شدن صدای انفجار در نزدیکی کنسولگری آمریکا در اربیل خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/451714" target="_blank">📅 21:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451713">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0fpa_rLA1ggZvBl0Y4xNdykVxaBnc4Lwed6hoSOg-1BJgVPFjVz0WKlV1_qMIgcV_YR9taAPlXK6NyMi6CU3tVpCY1pjl1qGXrs1YxRbDA1Go9sXH7an3KYYAjPRnCDIXQ2Zco4LXNa0ekKOpXo2XUlPCZtNaVr8FlDKK8KBZlc3KiJf59Mh6pM4F05xA6MmLSJlvIvJ56xKe93A_ye8sZiwXWmFYjz7IQ-VFESrMFiGdHHTR2UGa6g5qznpktK0jZ4i5YMX2DwddBtecCTUUYwBdy35Vx1rFHaxiSsiJ51719HPf5a3cjs9FEgXONPk_5Ykm8OZYArvPIdbD3teA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
۱.۵ میلیارد دلار سوخت‌رسان آمریکایی در تیررس ایران
🔹
حملات هوایی ایران به پایگاه‌های آمریکا در منطقه باعث کوچ زیرساخت نظامی این کشور به اسرائیل شد.
🔹
تصاویر ماهواره‌ای نشان می‌دهد، حداقل ۲۴ هواپیمای سوخت‌رسان آمریکایی در فرودگاه رامون ایلات اسرائیل پارک شده‌است.
🔸
ایران در طول جنگ ۱۲ روزه و ۴۰ روزه بارها منطقه ایلات را هدف حمله قرار داده است.
🔹
هر سوخت‌رسان آمریکایی ۶۵ میلیون دلار ارزش دارد و تنها یک باند فرودگاه رامون ۱.۵ میلیارد دلار تجهیزات در خود جای داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451713" target="_blank">📅 21:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451712">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دلیل پلمب چند کافه‌ در تهران چیست؟
🔹
درپی انتشار تصاویر و خبر پلمب چند کافه در مرکز شهر تهران شایعاتی با موضوع برخورد مرتبط با امنیت اخلاقی در مورد این کافه‌ها منتشر شد.
🔹
کافه‌های مورد اشاره هم با عدم اظهارنظر در مورد علت پلمب خود به شایعات پیرامون این موضوع دامن زدند.
🔹
باتوجه به اخبار موثق دریافتی تمام کافه‌های مورد اشاره به‌دلیل مشکلات صنفی پلمب شده‌اند و پلمب آن‌ها هیچ ارتباطی با مسائل مربوط به امنیت اخلاقی ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451712" target="_blank">📅 21:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451711">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3319cb340.mp4?token=mOrN7LEUUBKFAWwGtgv2nrZ013fbYcZV0zS7AUDf5MnDYcP7IGHRt99CiFeVNwsDDm5Hp5MGYKW4Z3ortiox5VZIQ7KIGy0RKCAyzdtknpk9rMi2Z9xSadOffCkPmJWxA2dFzrPB1uMkhQIEjcTYa6PHuAebRctsg1A2tc4SM1Vyj57k63TbEgCBasa8Cc-nw_pL8qxom0o3NmjWAvKfnBX-NFdTqJH2Oq6Be7o2XUeHG6eHHX9-uyEN2T4GEb7uRbwg0XvHrIDV82xM3aSqdfM9InCEiXDiL6vrj_LABq2fLslXLDoUYmUEMxcqLJJ-P_odeWiwn47tYKWmL8Cviw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3319cb340.mp4?token=mOrN7LEUUBKFAWwGtgv2nrZ013fbYcZV0zS7AUDf5MnDYcP7IGHRt99CiFeVNwsDDm5Hp5MGYKW4Z3ortiox5VZIQ7KIGy0RKCAyzdtknpk9rMi2Z9xSadOffCkPmJWxA2dFzrPB1uMkhQIEjcTYa6PHuAebRctsg1A2tc4SM1Vyj57k63TbEgCBasa8Cc-nw_pL8qxom0o3NmjWAvKfnBX-NFdTqJH2Oq6Be7o2XUeHG6eHHX9-uyEN2T4GEb7uRbwg0XvHrIDV82xM3aSqdfM9InCEiXDiL6vrj_LABq2fLslXLDoUYmUEMxcqLJJ-P_odeWiwn47tYKWmL8Cviw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی کل کشور: اگر براساس گزارش مردم، فسادی کشف شود، به افرادی که گزارش را ارائه داده‌اند پاداش پرداخت می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451711" target="_blank">📅 21:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451710">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌
🔴
منابع عربی: لحظاتی پس‌از به‌صدا درآمدن آژیرها، یک موشک‌ به نقطه‌ای در پایتخت بحرین اصابت کرد.  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/451710" target="_blank">📅 21:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451709">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64f3a480fb.mp4?token=HE3Tkl3vADmZPEbRSTGpQR8rCGJ39GLMVef-_0dK2sALyhENvtArKe8_mXCddFPIlQ1TygWChWtBapC2KjLZHYQmOMh0CodwkTz2jshSDT_fen3VG3NOKutFlldbs-uOXWCGJXNlu-ouWZ2_8h8xh7txXT-3o2JCnUk49wQ6MrP3vsCbtR93MjpbU6Qg2dHrRPI4CU90EKhNx41uwbmv29Vdxvuj1wxeTQNv7WovUv_KopVA3jLkY_Wu57-0vC705f5RL6zfx5PqEywPB-hqxJtfT127BQ0NudAfBibfimIti3HQxQ4gdsFDVwcHNDRe5QK59Rhi6dqcXvzjJqwl9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64f3a480fb.mp4?token=HE3Tkl3vADmZPEbRSTGpQR8rCGJ39GLMVef-_0dK2sALyhENvtArKe8_mXCddFPIlQ1TygWChWtBapC2KjLZHYQmOMh0CodwkTz2jshSDT_fen3VG3NOKutFlldbs-uOXWCGJXNlu-ouWZ2_8h8xh7txXT-3o2JCnUk49wQ6MrP3vsCbtR93MjpbU6Qg2dHrRPI4CU90EKhNx41uwbmv29Vdxvuj1wxeTQNv7WovUv_KopVA3jLkY_Wu57-0vC705f5RL6zfx5PqEywPB-hqxJtfT127BQ0NudAfBibfimIti3HQxQ4gdsFDVwcHNDRe5QK59Rhi6dqcXvzjJqwl9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چشم دنیا باز است
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451709" target="_blank">📅 21:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451708">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eeb7e452a.mp4?token=TlvoX0NBvOla2ci4ozXWDg2hfqwayMU_-QnUp4JVYH0aTEZSL-MIjr6gClO1IS6roVB9eYdaeZzbYVmrJQP66Bal-giiQv9zgfrUoUzfeEhkOqqB2rB56XcPTynOkqayYv0rZtp6WF2uebn8JrHj0fJpW6aeV_mwRHbus4rlwm6cWkTScRPTIJofImDOvAqeJbD0l4IuG4jz5r4Fv0_Vh_6UXKKHN29NTy7G9IWMhc7Grp_F_Z-ILwCWSgutHtWV-qQmePKQNJ6prURcQpJlTYTO96pb9PMR2q_dksfFy1wlGbMd8xysCLAr2K8db2LGvjfDxOSnmqCpqunhkFqP8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eeb7e452a.mp4?token=TlvoX0NBvOla2ci4ozXWDg2hfqwayMU_-QnUp4JVYH0aTEZSL-MIjr6gClO1IS6roVB9eYdaeZzbYVmrJQP66Bal-giiQv9zgfrUoUzfeEhkOqqB2rB56XcPTynOkqayYv0rZtp6WF2uebn8JrHj0fJpW6aeV_mwRHbus4rlwm6cWkTScRPTIJofImDOvAqeJbD0l4IuG4jz5r4Fv0_Vh_6UXKKHN29NTy7G9IWMhc7Grp_F_Z-ILwCWSgutHtWV-qQmePKQNJ6prURcQpJlTYTO96pb9PMR2q_dksfFy1wlGbMd8xysCLAr2K8db2LGvjfDxOSnmqCpqunhkFqP8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس کمیتهٔ حمایت از جمعیت: برای ۵۰ درصد خانواده‌هایی که فرزند سوم آن‌ها متولد شده، زمین تخصیص یافته و می‌توانند ساخت‌وساز را آغاز کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451708" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451707">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cb3c27fad.mp4?token=f4XpojBIVhlE8ZWUlA0GNRcmiODGUm80WvGWplIX5Ce1M95zuNptrvvy44twZPxVVVRsFDzqiyaiOhKuE_VGxCwVvkw-cXvesAFsW5dECCkh1zpglQzoqcE1pBun3dI4qrt4oNIHr_2gsdE5Y9vR-zRxUL8s8weH23GNFrVD7V4dWpAzqaU0UBbzxesZ90t-VFwMSxfSzR9RxrO1qxgfJOTY0UdZ_nHyDPdJKL73bhRoQLxZwYD-KG8PU1bD_MuWpdELEBoW_jmYotaXLYsBFX5NuS5kaijaQNLLZmnv_3P9o6PRNDkfRxvkChlYfHBNa9O9XUfdo7Mi5eP4WlzJSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cb3c27fad.mp4?token=f4XpojBIVhlE8ZWUlA0GNRcmiODGUm80WvGWplIX5Ce1M95zuNptrvvy44twZPxVVVRsFDzqiyaiOhKuE_VGxCwVvkw-cXvesAFsW5dECCkh1zpglQzoqcE1pBun3dI4qrt4oNIHr_2gsdE5Y9vR-zRxUL8s8weH23GNFrVD7V4dWpAzqaU0UBbzxesZ90t-VFwMSxfSzR9RxrO1qxgfJOTY0UdZ_nHyDPdJKL73bhRoQLxZwYD-KG8PU1bD_MuWpdELEBoW_jmYotaXLYsBFX5NuS5kaijaQNLLZmnv_3P9o6PRNDkfRxvkChlYfHBNa9O9XUfdo7Mi5eP4WlzJSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع خبری عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451707" target="_blank">📅 21:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451706">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/451706" target="_blank">📅 21:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451705">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uufVX5YTurHK0-_XiZpaYKHLd9zWjc_peUNEmN-ngDBKIn9W7arG6AxX_Ftkoq8UJaAkJs-JDm4cjuVrJGwmR0jJVC-J8thuTyWFaA6tN3K5ZZzOdMe5i0X7tYd4bh0vqDmkNroc91NMbEOYaBTnTqfpfqFt8c8VD6H4RQkvM_75tevATBteATHsBvAK9OuiRs5W3G84SP3wCNUpABUKwY6KNYuTIj4dmpsuR3F_rXNwDK4bCfBmYAsKDU8RRJxKWYaIG568TaQAKwbwV8hMnr93P0rM6AOxYjlnxzFm26BdXT7mtC-zv_f9k54aohG8OiTvadCNMS93VfWg_JMnYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش: اجازۀ نزدیک‌شدن دشمن به مرزهای کشور را نمی‌دهیم
🔹
از زمان جنگ ۱۲ روزه برای احتمال حملۀ زمینی دشمن همواره آمادگی داشته‌ایم.
🔹
اگر جنگ به روی زمین کشیده شود، نبرد چشم در چشم خواهد شد و به دلیل ناآشنایی دشمن با جغرافیای منطقه آسیب‌پذیری آن‌ها به شدت افزایش خواهد یافت.
🔹
اقدامات نیروهای مسلح به شکلی است که نیروهای مهاجم زمینی حتی توان نزدیک‌شدن به مرزهای کشور را پیدا نخواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451705" target="_blank">📅 21:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451704">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
منابع خبری عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/451704" target="_blank">📅 21:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451703">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3033cae9c.mp4?token=GJjKng2LbqTwJkxxZbCno1Pf9idmV0hKjUQND9UookbFOnqKG_7W6J0-iioirnnweofMQlxPP0lljrJ7HnIw11Dy8LcMhDDcO1lPAhIjwTE_dCZZdgV6cgxsENChvq9bI-JUa4Zyfk7_CuHC9H216lI7BT5Lzpln84Upse1HGdQz73a9iu_RzbMbf-JHgURYJsSJBRckGRElnLD5LeFv4FN-I7APINVUFPORvzEklpZWVJCLVMRLJqDtbiK_GkDlU3UtIuY_N3DCN0lR5GNqoLdvoa47JtGUrmOUUw4y35eEczUHq7rR9pePfxi5hK2SeI8Yp7rmmeB7QFTx3shayw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3033cae9c.mp4?token=GJjKng2LbqTwJkxxZbCno1Pf9idmV0hKjUQND9UookbFOnqKG_7W6J0-iioirnnweofMQlxPP0lljrJ7HnIw11Dy8LcMhDDcO1lPAhIjwTE_dCZZdgV6cgxsENChvq9bI-JUa4Zyfk7_CuHC9H216lI7BT5Lzpln84Upse1HGdQz73a9iu_RzbMbf-JHgURYJsSJBRckGRElnLD5LeFv4FN-I7APINVUFPORvzEklpZWVJCLVMRLJqDtbiK_GkDlU3UtIuY_N3DCN0lR5GNqoLdvoa47JtGUrmOUUw4y35eEczUHq7rR9pePfxi5hK2SeI8Yp7rmmeB7QFTx3shayw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به عشق مردم جنوب؛ شما چند درجه دمای کولرتان را بالا می‌برید؟
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/451703" target="_blank">📅 21:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451702">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451702" target="_blank">📅 20:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451701">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89fca517c3.mp4?token=p4GtVEQZ3MLTUZDAOq8RST0GcUxrGIeSMKHZn7I10maQ0NI9NkeDkGKG2zrH3wUeTdG5LuKgPpiUCQ_3IdKuWZPCq-0ofW46A1Gog-jJIWYraiPhZHXORzWjSUGYbSidLZVAPX-_zCU7cuFXfaLJtuFlimLxgRvpqDI9lolhciGOmot3gqHMS-BOwTM4rf_ujxLn6OZ6iKDaxTkDI7tOXWZMas14Xekd1l-nkvCCwIM_DIA-M-pwQVaWtfQ0ff70E4jwHmetV3c1NBY3RHcPnQvU_KHZGJaOR96WF2NkGyFWWMR34Gp9PEznLth-yGv25kxkl5h3O6TWifysJ7Z72g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89fca517c3.mp4?token=p4GtVEQZ3MLTUZDAOq8RST0GcUxrGIeSMKHZn7I10maQ0NI9NkeDkGKG2zrH3wUeTdG5LuKgPpiUCQ_3IdKuWZPCq-0ofW46A1Gog-jJIWYraiPhZHXORzWjSUGYbSidLZVAPX-_zCU7cuFXfaLJtuFlimLxgRvpqDI9lolhciGOmot3gqHMS-BOwTM4rf_ujxLn6OZ6iKDaxTkDI7tOXWZMas14Xekd1l-nkvCCwIM_DIA-M-pwQVaWtfQ0ff70E4jwHmetV3c1NBY3RHcPnQvU_KHZGJaOR96WF2NkGyFWWMR34Gp9PEznLth-yGv25kxkl5h3O6TWifysJ7Z72g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایرانی به هیچ‌کس باج نمی‌دهد
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/451701" target="_blank">📅 20:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451700">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/791ad163fa.mp4?token=KKROFz8Bq49gOd65kF8Tm-xVMTZdrpbQ1WMrRKQT-M6hREj0uAG_OQuVWg19SNKf68mvzJm1Y2k-Qmp4zNXMy7X7M_MqXjUrDTfLKhtDFAXf0UeOTjCkbslUsLRmsZN0Rdnrqy13NZquEH0BYKhOZyf6L8zCQ_7CaBxK5VJiNUUL-ZsJwpG9Dt3F92XvhGJgGPc69vD7O-ytoLQWi2yC0QG-Ii25VBq_pa3vUwV0qfKH_adhhY6xyOz7pdL2bAzoP4_vP6tlmF4M3c2JL1gqCjOVniiX6qOYrJOLvmvLTapwsiO5LURN7boGqAR6Lvdpd_HOHXwedWbOrY5csXoXug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/791ad163fa.mp4?token=KKROFz8Bq49gOd65kF8Tm-xVMTZdrpbQ1WMrRKQT-M6hREj0uAG_OQuVWg19SNKf68mvzJm1Y2k-Qmp4zNXMy7X7M_MqXjUrDTfLKhtDFAXf0UeOTjCkbslUsLRmsZN0Rdnrqy13NZquEH0BYKhOZyf6L8zCQ_7CaBxK5VJiNUUL-ZsJwpG9Dt3F92XvhGJgGPc69vD7O-ytoLQWi2yC0QG-Ii25VBq_pa3vUwV0qfKH_adhhY6xyOz7pdL2bAzoP4_vP6tlmF4M3c2JL1gqCjOVniiX6qOYrJOLvmvLTapwsiO5LURN7boGqAR6Lvdpd_HOHXwedWbOrY5csXoXug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افشای جزئیات جنایت آمریکا در میناب توسط اسکای‌نیوز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/451700" target="_blank">📅 20:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451695">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kwlgf8IR3UaVRY4wtjAgBLTx6oLp3XSuRNxz4qAhjG8kydsYwtxnWS1VLeLoqQ71LDnCdSST4hvE_fiKSmZgcFL6ZRelDtdqOtKeKiwrYlaODnXlBL3B5e68q4kWBmGgnzWx7QtMvQz9NQv_f9GBXPTa4Dhy1XsgW45arAe2I40ChweAnUsp1b-lH0ZhWo2WvJbONADe6e2-5q7LFynY_aKlF-4uEcRed2iH_48dUxM-ePcVi9io94EzqygdXt0VzDvqaeHo5k0HDHUxXy0H0YPJ-kqlwNgvMQf2GD6uJ4Obr0qRQ20c2TdpKDk08K-ImMjJD_MNuOKams2U-mgVJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kiA3wecLYuo400qb3ePeotlgWG3uHwayLnkQhj8Qt-7LcJXl3LJC3tXQGzA14k33KouvRP01pbrOBkND9Pi504Wupa7ynTCl4IppMel3aq_tCS_nb_-FWkbMLA7nGjS10N7oVO4RcN2UHVoeGBC-xHg3x8vzTwwku-gqPyzrNStyZL83Whb0s0nHfg3yBe7ZNuSK2ANX-TxJzeV10pJqx8Q6UJ4RL6LUQtEOYouKGMr89xWKVroLv6TYdZ7RmvbZWCPq4qvKjELGBCAeJS2onBUl8tqV2GSnAUIsCfecy1CM8dIZzWtzpkDrwe7vWQO2u3mXJUPZf37GZeehQjnnVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tkS4Hl9ArEB24VG3fL32HVtTD1f--LSV63W8-v0k8eqFQtKN7bVQOjJ3doDW6C6Be5JAR-pSjcExuRssOj3phzp7qOERrR1fziDacXMhUxEt21EjO2D_gcostwNJaOlgABRNrOKssOiNuzgkC89HrEJqGMsPXGjOmdaGyW6g-zevgv7gcziwAzGYjfp5YdK9eRYpaF178qOIFUnc9e2Y3LZ6P6mYUswaGBreq7rAWrb3JKQnzYXatF6LPm_5JmPM_fmvHKGmo_vm346GiEFalzp3pGGInSQTjXJ84tgjqo_eZiTbM3-0dZCSA83382jnB5XjiFm160lf3b9qMW5TdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4euraWf0amNQtadapspaa8FutralY7qxJGUKaTzSlhF3lDv1q2np-dRCZZrxS4JjiPDUH9Wvx_KywDLX3xs_P8uHzNlJs0KuYU6Y4wFdLRuiOe7SsnGk_G-XvACqvAAf0elUwFMTW964REconNsxRDzMaRPfqM-oqF2xS4NQs2JMCxG7jTsTrFkQeJsXuzPM1Svf9zAY7Pw_Lzc1pftFhzLVJCozp-8u1OfVaECYPxW8IaiEvV5U9SrrDU7nl54cMsWI4AV6rhFRsiAstss3LJ1ZQiA2e6vgYH48qiauuJtxk6H-OzLb_JhYn9wtZjTGaiNNTN5jApNjSvjvee2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o3I4bJ_KiBXSH1NJifT6nF42DprYPHbklOuVc2a9OpGQ4nNaVK_5W7vvcL6DQqqhmDDKSMU2LM7sS7c9SaeOInIptSQmHyDEPMCEkgqcELs_zXInd8bESPxer9g_6J_sS1uzg62gqkFfsaFexa4mUX1bq4YpXPt5GV9qhZVGdKbT45_lRIVYLt_TmsEyI07Xpx4jMKSyv8vIi9n796dInbxKbNpmXXiWPuno1UVw7wBHn2RoDdds4YrIwyPNV92LUr6rvt19P5nZKhOf3Qi1RG_KAlD20PcLsoDg4if1uAk93Eu3e1KjhI5B7n4DQSMXB4s1yJ42nlybZxrsUzL7zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید خبرنگاران از سازمان فناوری اطلاعات ایران
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451695" target="_blank">📅 20:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451694">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">زمین‌لرزه ۳.۳ ریشتری تازه‌آباد کرمانشاه را لرزاند
🔹
زمین‌لرزه‌ای به بزرگی ۳.۳ ریشتر شامگاه سه‌شنبه ۳۰ تیرماه، حوالی تازه‌آباد در استان کرمانشاه را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/451694" target="_blank">📅 20:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451693">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">همسویی وزیر خارجه جدید انگلیس با آمریکا علیه ایران
🔹
اد میلیباند که به تازگی از سوی نخست‌وزیر جدید انگلیس به عنوان وزیر خارجه معرفی شده گفته که لندن بایستی در بازگشایی تنگه هرمز سهم خودش را ایفا کند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/451693" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451692">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d4308a98f.mp4?token=c05Nm-rwlwJyrkby82uvWO3z_NFlloq1KIhz0CI-TSdK2Atuxso-4Jm9pI7kMeC96-n-WobAvNK-pAaGfbu6C6gSGAVLLCVTN4G2kDbsbH1pP283xHBdqlMllUzCzkJVcx5lG-XnwECoBLx3Cke2S8jbS9gjOH4_6Xg0kBaigCQLN4mQI06XF97JpYISl6_aRF6ty4cKUIGKo1jfY8fJmQ1d4faMDBXx2aTy9vaJFMQ56290Wb09NF1UVnGtoaDew8HfDNjQqypjgjJae3pZKNHaijBvXcZRDSNqmakq9sULuLKYHUSl4C8boNGBDpA2k-_WxHx4aAZnDZHsM7HIUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d4308a98f.mp4?token=c05Nm-rwlwJyrkby82uvWO3z_NFlloq1KIhz0CI-TSdK2Atuxso-4Jm9pI7kMeC96-n-WobAvNK-pAaGfbu6C6gSGAVLLCVTN4G2kDbsbH1pP283xHBdqlMllUzCzkJVcx5lG-XnwECoBLx3Cke2S8jbS9gjOH4_6Xg0kBaigCQLN4mQI06XF97JpYISl6_aRF6ty4cKUIGKo1jfY8fJmQ1d4faMDBXx2aTy9vaJFMQ56290Wb09NF1UVnGtoaDew8HfDNjQqypjgjJae3pZKNHaijBvXcZRDSNqmakq9sULuLKYHUSl4C8boNGBDpA2k-_WxHx4aAZnDZHsM7HIUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رگبار موشک‌های سپاه و ارتش، پایگاه‌های دشمن را فلج کرد
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/451692" target="_blank">📅 20:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451691">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51426b3189.mp4?token=ebwNoS5uyKlu2ebugpiwc8-OFXe0vIFz-lehicIG94RlGObDCOK84FIoZMzIAYm6rHS7GewFgb9HZrNMRucOzkpx1L9XWphy1WPQzB5MEs5TthzYfV1MW5rjjeXIqXKgYLgZWF9t2VPYigV5gpDSmEEox6Hwx6Qwu1JyqNu49AMoYCG3Z40B1NbK0VckidAyVpr6mQU5EzmIdufSBrDDtKcCpChmb8O3u979rx3dALLxTiF8J4ZVxwzo9MsdCoutbDbotpylnvefaAPkuyw90NskitFTHKpcaBluKCf-2H7YuOsvLFAfuc16sea8lAYFUFmMkfV9q-evF9qP3TimVUuqOfsjuDbN89idFumRMIL19uUbfhNl3fAhshgOFrWTHW9YFFCV0OvANS7eEP-fd3kTaw_vc49fxb47UeBJRhHmWuBdtc23_ftIt4eKYQZJcGyh6EdIzq6ySjmn2kW_oPqX--_erW_1vBKkDF1gaTLxbGCLyzKUtXz1W6Xl4rLFVacFXR_RR3-FRXkuaT2qKnNkeEQNJRrhCaDiVBMr-DVj_xaKq-1gEql3ROTCRJwWQxXplMsHZvQtHJWWA5SZ6UK2UwhaTBTMgeByMxhwvTOcnFYfcxxiBZm0Q46GiqonwvE9xWrWMd8sxsCsVm29eU5046b3YEyeoxr8TSW60MY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51426b3189.mp4?token=ebwNoS5uyKlu2ebugpiwc8-OFXe0vIFz-lehicIG94RlGObDCOK84FIoZMzIAYm6rHS7GewFgb9HZrNMRucOzkpx1L9XWphy1WPQzB5MEs5TthzYfV1MW5rjjeXIqXKgYLgZWF9t2VPYigV5gpDSmEEox6Hwx6Qwu1JyqNu49AMoYCG3Z40B1NbK0VckidAyVpr6mQU5EzmIdufSBrDDtKcCpChmb8O3u979rx3dALLxTiF8J4ZVxwzo9MsdCoutbDbotpylnvefaAPkuyw90NskitFTHKpcaBluKCf-2H7YuOsvLFAfuc16sea8lAYFUFmMkfV9q-evF9qP3TimVUuqOfsjuDbN89idFumRMIL19uUbfhNl3fAhshgOFrWTHW9YFFCV0OvANS7eEP-fd3kTaw_vc49fxb47UeBJRhHmWuBdtc23_ftIt4eKYQZJcGyh6EdIzq6ySjmn2kW_oPqX--_erW_1vBKkDF1gaTLxbGCLyzKUtXz1W6Xl4rLFVacFXR_RR3-FRXkuaT2qKnNkeEQNJRrhCaDiVBMr-DVj_xaKq-1gEql3ROTCRJwWQxXplMsHZvQtHJWWA5SZ6UK2UwhaTBTMgeByMxhwvTOcnFYfcxxiBZm0Q46GiqonwvE9xWrWMd8sxsCsVm29eU5046b3YEyeoxr8TSW60MY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک سلام جایمان بده آقاجان
@Farspolitics</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/451691" target="_blank">📅 20:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451690">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEubNunfsvE0y6tZCCLzrBztdG6M6atHw1QkNtq6JZlRbSLsCq6cd8zYV3SqqeYKEO4EdaPXChodVdlZRHyJjcFZWCHmeA8RRCamDtsIl-DDq4e0AhtDEH2F8JSsFk2caXI4XUu4YuWTzxbRoPxxJIWj6jQB_eOrOoiEmYul6kXyf3aCxNrGUDiQKiZv6wm0KQc-HcTxfl3K9q4TteRu0vCQc-kFS9Z0ro09V6wFw6qwRptgs_C2oCny99N4XJyFBxqlWtnnuMmjhq2-MId6Ja7p1v60oK-oryBsbqAl_iKk-dktwlXPQ8nivGG6eSkfbtKA4gF6NeuDpdTukO3trQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام یک پهپاد انتحاری متجاوز در آذربایجان‌شرقی توسط ارتش
🔹
روابط عمومی ارتش: ساعت ۱۸:۳۰ امروز یک پهپاد انتحاری دشمن متجاوز با رهگیری و شلیک موفق سامانه‌های پدافند ارتش، در آسمان استان آذربایجان‌شرقی مورد اصابت قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/451690" target="_blank">📅 20:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451689">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اعمال محدودیت مقطعی در مسیر هراز
🔹
پلیس‌راه مازندران: به‌دلیل عملیات احداث روشنایی، تونل‌های ۲، ۴ و ۵ و تونل سپاسد در محور هراز از ۱ تا ۲۰ مرداد، در روزهای یک‌شنبه، دوشنبه و سه‌شنبه هر هفته از ساعت ۲۱ تا ساعت ۵ صبح روز بعد با محدودیت تردد مواجه خواهند بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/451689" target="_blank">📅 20:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451688">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRtgG9Xtte6zEKBynfvYO3sbEuwO2XrYYAFpX-R4lME5nJyifxWXwI4oaKDyG7qwhkYvZwlBNQ7f7EO2uFvyR6dv7OsAgajkFXggHEEAKFe4I1t42aIb5_UpR4xYJkj2usDXlEevLqtCtcnH7H2WAO5HE5wJPQiaeuDlAitbkBYm8LkL-NQWeoYvK2PmHSaIrAO5PnG85fZfyHK0LnwLzCQL_-wjfToMfz56Ce4qmu_Kq-evfMTm6V_nuO-DppQijUtLbpVm4nQVf-u4Lez2wLiSU3n__rI9PdB5DQuM7njOH_7OVDI4oggu_RhVHcIJW8YMxcZgzQtUffFQX1qdrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برق ۴۸۳ ادارۀ پرمصرف در مشهد قطع شد
🔹
شرکت توزیع نیروی برق مشهد: درپی عدم رعایت الگوی مصرف، برق ۴۸۳ اداره در سطح شهر مشهد را قطع کردیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/451688" target="_blank">📅 20:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451687">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdK8DvdUmbNTVlL4YQXb4UNzoLDZJy7FltkGaU_veqCoZdNrhlbdthZn00Xf7zLnC0QZkPvuk7mm_nDUiffWobXitmpxTaD2FTGcoW6WkDhA5MzR8LRtBE7vNYl-faRV0H6wGBa-v2MF1WB3rAGo0qErQOrygkwMTzFfiaBSQMjKwu7aQDQzENAt7ZYiqCTdRCanADDNSnxP0SXH22xxtuvrXVl7X7f1GswjOIQEaWUx_qWbVknMSpW8Jv6J1mTOn5wPoj1bk4VUNg0v98nglmNg9kOYwicWwVefIu4DeRXntzuD9eDHhEOPl829GgE92jvfbO6kCQRGRLWJ3o7A6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراض عراقچی به همتای فرانسوی
🔹
وزیر خارجه امروز در گفت‌وگوی تلفنی با همتای فرانسوی ضمن اعتراض به اقدامات نامتعارف و مغایر با موازین دیپلماتیک ۲ دیپلمات‌ فرانسوی در تهران، این رفتارها را غیرقابل قبول خواند و گفت: رعایت قوانین و مقررات کشور پذیرنده و پایبندی به اصول و هنجارهای شناخته‌ شده دیپلماتیک، لازمۀ تداوم فعالیت نمایندگی‌های خارجی است.
🔹
عراقچی خواستار جلوگیری از تکرار چنین اقداماتی و انجام تدابیر لازم از سوی دولت فرانسه شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/451687" target="_blank">📅 20:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451681">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mf_PFDHDRLiyFb57UozQHCvXcMf0Yy3zNKtsFaI47rCpf8L4llJsZ7uG16VAyBBaIojJHJ5Ob_TjIDOsHt-qKi0eh7EdqVc8YOcLSdHKL5NpOgMYSuZJRCX72g1EACSlR6WaqeGpCf_82nJDUYUEv52yzhw3qBpA8RcZ6gO7scSTFuQq-JgzG5dNvgcmgHCgU-jmkhEBddZkR0FGTBgsi5XM4zcjxSkNcstkCcuH6Q62vpSdABXzpazQsyLKDMnH59pOVWe6EH5isv8WG1AZsCwy6C-ewoLtzmaeCR4gZ2IuCVXAw4Hl0Jc9nec8jbc7ekRe4P8VpS1wWsdfFq1YfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvdF_KH-Mz26IiKgfsXfgYWOFTWuPEaid20Fy0YInGiuYol9wub_BQ8Um97-5UR4dhT53i95Ve2nCrloBUjRvvugdgqtqfMh2yfwkPKLI5E0dkXobCWrEjjPLclIdxWOv9anAbRl3iLmZGNnbiXSaKX03m9ocvp2j_1g4F1ePoOLx_pnmZMGDJ4zZCOMhGV7ybD3S7GPnV54oP-0Yx1w5gl6f9QEL-CyOF1se-hBGxkDKJ1tSNBRQ786BreGkKyXc4c2u2qB3LX7nZFkxie_ZuYYoyTh_3fE1IykUttGoXYvq25Q3iQeTsxmoBEwFk7OfV8klo8RoX5QhTxpTjePEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FC0N-k0EkvqHMSfnYLHbsd_4KeFcj6djt-3kkMrGHsAs6piITN1Vvn0Yd7CWXNO2vPLfiNXCO0s_-NYNMPnwoegJdpo0xAFTAKGXEFOxzxhGt4ZLy0FEM4n3V2ccV_lwlKnu080MNwuH-5KHRZVZRvMbhkQ-fv57mP3w2VQhDYVxPzpDSkmtbYDAaVgRI1oKZ_0OrfwWzrfXKVr7FdD1g1oejTfPAWHUjtF5x5xiS1VEy-FtYSWvJNAfg-DitK6miuLsxybtl7UrpmDpryCiRA2UyqnHGzGD7_LFAVf5c2BDYbF02SpgaLl0ZltRq16F1-zqDEI5ll38GRowG4EGQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l6sdLpHrMdBrbt6EwpgVFalpHXFePiJdYX-w6Hg7D97iZ4AIKvpVHUZxw8qOZ8ww_NxNaxs-4hjHp26bBkVdWCyeFZWtwo2Vv3NxUXRh_xlekcQLcGZQ247tjTiCIkwl557gdFauRpyjykArxb8WRMUZM9Rp-ghlMAfZ1k-bfNvduLdGyRI0Pv_MsJtaKkpdp9Yg_xCNVUGjw8zZQnHEZCzb5yI6IEO8pvHUbBnBIXO98OzS2vcwn8cqKLaZ0RSURnFYQCFPFITUhs7Rd2C_wqvASAkRY3wHeTZFsKgAmx6-Dvp8yU8mwEwjuxdth_lnA-4YhI383yJgY2B7U2i3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQhQVW-8g5uzBqwn4XAebJ0px_6GFzr6Ev1xieXE_oaDanco0VpVNgyBq4ZPGC6LSvzbCUrW1M89P7uZm1v89q8aBhPVPh4oT6J9AXycnnr0w1XQi7s4Qgz8TnS2LRKqr3a5YLojf_IY7wivdgvy7JCe3CAaWAXxcz4-aM3Bk_Pw3p_kfDpSHHC8DvnMTR0TagtZhCHJL6hqi-NirDF5JPCOVqCY524XLy8ae9DhvsROEFlK9l4qzdZArEAFt-sAqJd5LWionVkw1citSTPxfk1fNrBBSaiOB_UhpGZiESdtJoyRLHeSWi9rOTO9nAbF6kmwlUJTMVMK3RbR_SiCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kC15FuczJ9IFvD7EHaddKT40Zc3O4jfkN3MgpMJBLUJpzV9X-Lw9KRwa64Gh1F-BCTSZGGPwGChYQtXUxj1P9nUqrQXqRK88UQ2shDFufOYikzW6ZpzRz5CVUK_516rIBCZqePhpmMZBIe8rEXio58f-D7zvgQQDrXr3y6ce9XSMEpv3RIwWRn14-7wkIDPld9GuEcSSUOHppn09wMGkWg61JuKhPGKmNWwg0SpOQNULxDaNbyZ3pc-Qwiv04n4kRbxVkubvR1zFRBBQ3AcCJwVU2s7dvigYPe3jRIlaUpYW8yd7C41h7tOuLG6rmGarbfD1up9yoAbvcxc5Utzs2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
محرم‌شهر در میدان آزادی تهران
عکس:
عرفان باقری
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/451681" target="_blank">📅 20:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451679">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31f09280e.mp4?token=LHHeGJAlmRDCYn9Gy7IyH5NseU7ywTxSbzOSDSNJHXe2G0CdWIfCU1zVfib2UaQau9LydkRjmppfUXE5GY1RpyX1uBWMANioOtHnQln40esJ07RNdKl_GiYtW2hCaCKiYLfDXKTydWtYhro5L2KBpVk3IPWWyJT4rXu5RcccsCHPjrZlTVc5Po5lVCuOpT35H1AfYLaivlD13LpFdXyQeDSI3k5ApwpeI9Vrq3r_RIXueH2yQy_pBbFuEDIYkEZWL9oHeAhv0E9tSXXdU93j44LAR1lrT_iQWs9q6DBBpq1buzhLmmaxVWIt6YEDosUFK5XaTGSTlPsRMVaG0PiXVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31f09280e.mp4?token=LHHeGJAlmRDCYn9Gy7IyH5NseU7ywTxSbzOSDSNJHXe2G0CdWIfCU1zVfib2UaQau9LydkRjmppfUXE5GY1RpyX1uBWMANioOtHnQln40esJ07RNdKl_GiYtW2hCaCKiYLfDXKTydWtYhro5L2KBpVk3IPWWyJT4rXu5RcccsCHPjrZlTVc5Po5lVCuOpT35H1AfYLaivlD13LpFdXyQeDSI3k5ApwpeI9Vrq3r_RIXueH2yQy_pBbFuEDIYkEZWL9oHeAhv0E9tSXXdU93j44LAR1lrT_iQWs9q6DBBpq1buzhLmmaxVWIt6YEDosUFK5XaTGSTlPsRMVaG0PiXVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز راهپیمایی اربعین عاشقان حضرت اباعبدالله الحسین(ع) در منطقهٔ عین‌دو اهواز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/451679" target="_blank">📅 20:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451678">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc84283f2.mp4?token=gBriNh56UgaraP-6OpUGNtDrx-AT_g0A1HfpJWjMpIKBdwgUGjVaM-9ETvs-43YC5vtF5sbwWaEtodGQrmcMR9BzQ85m9IEbSANpndVF33FzPm10ZAWnnsidahIlRPfuUKJAlRLfID5ZvZCaLRCNIDJ-ryDGk08mlfVll9UYbvvk5kGwOhFKjGafkDFKThXpirNgj5-pQahA5ClnqIdfqO397xN1nDOfQQk7tY7QFUWNYLkBSBFOGmjJifbKtMsFtrI4dPtFqGya6SDISdtVIzORiapwY19gWB-frBq7v6O9AxaUM0JRqqrzFH0ve89a7AopQAbL8iCJEJNABtadiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc84283f2.mp4?token=gBriNh56UgaraP-6OpUGNtDrx-AT_g0A1HfpJWjMpIKBdwgUGjVaM-9ETvs-43YC5vtF5sbwWaEtodGQrmcMR9BzQ85m9IEbSANpndVF33FzPm10ZAWnnsidahIlRPfuUKJAlRLfID5ZvZCaLRCNIDJ-ryDGk08mlfVll9UYbvvk5kGwOhFKjGafkDFKThXpirNgj5-pQahA5ClnqIdfqO397xN1nDOfQQk7tY7QFUWNYLkBSBFOGmjJifbKtMsFtrI4dPtFqGya6SDISdtVIzORiapwY19gWB-frBq7v6O9AxaUM0JRqqrzFH0ve89a7AopQAbL8iCJEJNABtadiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بنیاد مسکن: ۴۰۷ شهر و روستا در جنگ صدمه دیدند
🔹
۲۳ همت خسارت در بخش ساختمان و ۱۱ همت خسارت هم در بخش کالا و خدمات داشته‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/451678" target="_blank">📅 20:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451677">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oc-kFj4OFC4zw7edjS4m-U6HdLNkTcktBY2Gkxdv6mdRhSt1Vosx7RXUEHSNIr1DJpQPCPI4z67JxrnNh0LQCI0NMrYzJgB3yAqZX8AYo5bOfEYaGqpUBPqR17CRD8D6u5TPy9NrJJ4JDowRRK6d3Ecd0pgRmBuWwbgia2NZQ96VauqnQX9RkLgGniqZvTnh__XRGjogo7cbTFwndfh8QEuijoGE8u7DtTJJHbEcnSnfAM6CXqusr8U4kg3E4tYUzBrRUZFBapGmfeFozfMWW8Zlg2RVmn7pRkqNdWTStmbMBiuNKaglqq27tP6bCxxKtlJAIJIsAFst-KjKUP_FYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به بلغارستان هشدار داد
🔹
سخنگوی وزارت خارجه در واکنش به گزارش‌ها دربارۀ بررسی درخواست آمریکا برای استقرار هواپیماهای نظامی این کشور در پایگاه هوایی «بزمر» بلغارستان گفت: «هرگونه همکاری در حملات علیه ایران، از منظر حقوق بین‌الملل به‌منزلۀ همدستی در تجاوز و جنایت جنگی خواهد بود.
🔹
در اختیار قرار دادن قلمرو یک کشور برای انجام اقدام نظامی علیه کشور ثالث، طبق قطعنامۀ ۳۳۱۴ مجمع عمومی سازمان ملل، از مصادیق عمل تجاوز محسوب می‌شود.
🔹
ایران در دفاع از منافع و امنیت ملی خود در برابر هر شرارت و تعرضی تردید نمی‌کند و قطعا هر طرفی که به هر نحوی در ارتکاب تجاوز نظامی علیه ایران مشارکت کند، باید مسئولیت تبعات آن را پذیرا باشد.»
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451677" target="_blank">📅 19:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451676">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
منابع پزشکی در غزه: از بامداد امروز ۱۳ نفر در اثر حملات دشمن صهیونی به شهادت رسیده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/451676" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451675">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbe7077341.mp4?token=KGxS_0aMBzud39ISBUY1dQi_-73nj1NpNPibfuDqpnlKwcTrm4C0eJw0YK0TSO_146REqZT1_j67b6bJLPdHcsgqsTQakkW1ns1cNYmATdgxauWnPrLAutXB-pInC5Fd5H6eYIa2EQFW4jMkQ3cf_FaK51yIuHcX0LbUEKJX-mKUILPbfcT6nE7I1xw2nr4aVkh8OQ-AMrzu8K1sxmrRs_nksf1Dtco72i2ofLdhJjR4Qbii7KLHPXJBHKpiKmgYLajPkByLgRzEyv-W_nYaIJpXBWZdpqAdrl_BaD7wvi0fi_0uh_xRDrjIu5cBvZVzkAFmL5jU5N_a6DJW5JzBCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbe7077341.mp4?token=KGxS_0aMBzud39ISBUY1dQi_-73nj1NpNPibfuDqpnlKwcTrm4C0eJw0YK0TSO_146REqZT1_j67b6bJLPdHcsgqsTQakkW1ns1cNYmATdgxauWnPrLAutXB-pInC5Fd5H6eYIa2EQFW4jMkQ3cf_FaK51yIuHcX0LbUEKJX-mKUILPbfcT6nE7I1xw2nr4aVkh8OQ-AMrzu8K1sxmrRs_nksf1Dtco72i2ofLdhJjR4Qbii7KLHPXJBHKpiKmgYLajPkByLgRzEyv-W_nYaIJpXBWZdpqAdrl_BaD7wvi0fi_0uh_xRDrjIu5cBvZVzkAFmL5jU5N_a6DJW5JzBCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ارتباط ما با رهبر عزیز روزبه‌روز درحال افزایش است تا بتوانیم با رهنمودهای ایشان مشکلاتمان را حل کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451675" target="_blank">📅 19:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451674">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c33d92d4d.mp4?token=p5GufM9pGbnhoWME8FyppZZEwh7nIozpsU3Exxp4bV_39P86cQMnofySOismCvnfW2aPj3DlzsvXh9LwUIu-xPBbXSKjODHMGqPB_JrFba4UfKuLo9LNtZAHOcVvCi2HIhMGb-oFF1nh_mzCQnJrYhuIrqLRWijdj66LOVd8NZs8QAbBV2PMackbQzjB3S0Rr7oRsHe5L3z_1aju0lAFHrN1pW_B213ubxxxwheeQjRNYebBJm8lIJf1oBFIFk1bLxRCVYqnBxDt5_PXXzhV0ytqk6q8PayhBKGyu1qGJ3wBzK04QX2Cmb4FOQgVX-cuCiU-pb6Un55Rgt2rGQcLUHGHZlHgs4BO8fZVKV850R_nd1m1ejrnHtC_3HRkx1EVoubRcil3gV7XqmSVG_aGF27RPUFytk1bA9futL5B-jHPKrTb_9GClqeoSZSzBq1d8Gy7Tz8j9LBJCg5AKigBraCY8GkPKHmyCFGaJnmjkmLSkM3OsnK5qzszljxmZ31p1KMIn27Obh3RsAyU1-5N2uOrDUQqIL9KaUN1vHLlK_16xTELVvk0xYSMIs-8VCvQkKVknZ07BfRz9lLR3qAV3k8MLUbBRJXjMGmJhpW65CUS0PkIolwaeHQ-q9Jl3ACua3LpG-cAEpUv5jtTw5df3oLkYKb_yQ5auDQAqQK7b2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c33d92d4d.mp4?token=p5GufM9pGbnhoWME8FyppZZEwh7nIozpsU3Exxp4bV_39P86cQMnofySOismCvnfW2aPj3DlzsvXh9LwUIu-xPBbXSKjODHMGqPB_JrFba4UfKuLo9LNtZAHOcVvCi2HIhMGb-oFF1nh_mzCQnJrYhuIrqLRWijdj66LOVd8NZs8QAbBV2PMackbQzjB3S0Rr7oRsHe5L3z_1aju0lAFHrN1pW_B213ubxxxwheeQjRNYebBJm8lIJf1oBFIFk1bLxRCVYqnBxDt5_PXXzhV0ytqk6q8PayhBKGyu1qGJ3wBzK04QX2Cmb4FOQgVX-cuCiU-pb6Un55Rgt2rGQcLUHGHZlHgs4BO8fZVKV850R_nd1m1ejrnHtC_3HRkx1EVoubRcil3gV7XqmSVG_aGF27RPUFytk1bA9futL5B-jHPKrTb_9GClqeoSZSzBq1d8Gy7Tz8j9LBJCg5AKigBraCY8GkPKHmyCFGaJnmjkmLSkM3OsnK5qzszljxmZ31p1KMIn27Obh3RsAyU1-5N2uOrDUQqIL9KaUN1vHLlK_16xTELVvk0xYSMIs-8VCvQkKVknZ07BfRz9lLR3qAV3k8MLUbBRJXjMGmJhpW65CUS0PkIolwaeHQ-q9Jl3ACua3LpG-cAEpUv5jtTw5df3oLkYKb_yQ5auDQAqQK7b2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اربعین امسال با یاد رهبر شهید پرشورتر خواهد بود
@Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/451674" target="_blank">📅 19:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451673">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1THMtTAgYXq-mN36Mzu_qsyqtikGWzt14vi_UExtxq0ZpyAf6thGQ4aUYjZ_ivrljoL1TsPUzHWQ7m2HXT11l5KB8mY18afMmaspFgE8Ytgt9iW4BS4AwJEb3lksbvz6j0r-5iqMV8Vdd2tW2W7yFeDUDg1aUZwBunr8F9yQUuRqLxA07wnmsqm54d49NduOAp2TkNZw4P8SHfhQf2Whh_XzmGEeKZGFFwBM8vQqwEMx-B7rgPp8Kexfx6l1xmoB77AMX7tyQE_oDC1imMihncISmsCNsWo3L-Uj5jpCbK1VXgUyS6uAoQE-CENU0LUjKVbz97MYrwB7dNr3mCAsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چگونه یک کارخانه می‌تواند روح هویت یک ملت را در کوره هایش بازتعریف کند؟
🟥
کیمیای آگاهی در کوره های فولاد مبارکه
🔘
در چند فرسنگی اصفهان، جایی که افق با غبار درخشان صنعت گره می‌خورد، سازه‌ای عظیم نه تنها به تولید فولاد، که به بازتولید معنا مشغول است. در نگاه نخست، مجتمع فولاد مبارکه شاید تنها مجموعه‌ای از سوله‌های غول‌آسا و خطوطِ بی ‌پایانِ تولید به نظر برسد؛ اما در پس این کالبد خشن، پرسشی بنیادین در جریان است؛ آیا مرز میان ماده و معنا در کوره‌های ذوب از میان رفته است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/451673" target="_blank">📅 19:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451672">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRnAnJdo37io9BVf8Kvq59qLF54fnxqPO6MUUpxcM0hAFcILciPga4_Ud5ZKym5hi--_8pJiuxySXGu9D7ibQhEHhRyLX9MEyUyYKp9RJOoXzgIKwaJiIO2Kk-emv1zkFd5kQLKqfiIrglqrYy-GlBJxHuSsvW_E6-bVHFocNk_x_j7t0XPXsWnpJGOXZX4c6qiq9ZhlIYGi25oiG5A2XJmML18GBdA7w9R-SQAo4_4ab4uePs24iZV0cnCjvOMhieLpmWIlS5NEVylJtydgBSX2fOlhwXAVPzx3oGLTzMUtTp4wWmb8kJJ2Dyoc7xSZMfrdzP5UxsnD-Ypr0z5DLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
ضرورت ترویج فرهنگ ایثار و شهادت
🔹️
دکتر اسماعیل للـه‎گانی، مدیرعامل بانک رفاه کارگران در راستای تکریم مقام شامخ شهدا، با حضور در منزل یکی از شهدای والامقام جنگ رمضان، از خانواده این شهید گران‌قدر تجلیل به‌عمل آورد.
🔹️
دکتر للـه‎گانی طی سخنانی در این دیدار اظهار داشت: همواره خود را مدیون ایثارگری شهدا می‌دانیم و تلاش ما در بانک رفاه این است که در مسیر خدمت به خلق، با تکیه بر آرمان‌های بلند نظام مقدس جمهوری اسلامی و فرهنگ ایثار، گام‌های موثری برداریم.
🔹️
مدیرعامل بانک رفاه کارگران تصریح کرد: دیدار با خانواده شهدا برای ما توفیقی الهی است تا با بازخوانی رشادت‌های این عزیزان، در مسیر خدمت‌رسانی به مردم و میهن اسلامی با روحیه‌ای مضاعف گام برداریم.
🔹️
در پایان این دیدار، دکتر للـه‎گانی با اهدای لوح تقدیر، از صبر و استقامت خانواده این شهید گران‌قدر تجلیل به عمل آورد.
🔹️
مدیرعامل بانک رفاه کارگران و هیئت همراه در ادامه با حضور بر مزار این شهید والامقام در گلزار شهدای شهرستان پردیس، با قرائت فاتحه و نثار شاخه گل بار دیگر با آرمان‌های شهدا تجدید بیعت کردند.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/451672" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451671">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/451671" target="_blank">📅 19:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451670">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc1730f80.mp4?token=iUMRb6FQ3kQiJ1kkxFvivVi9TyRt8WGxa8r-_XFOOG9o4lyHytUvOqKHJ_SqOvGeWtnmQZrnZ9-qoUWRllvYij3n2Y5WAD-WEVyCRHbB_4_x3YntTOjWvfos7syLkgGA6Ga7Ur9I9FlrKOlV5t1Dc4k1QYM280d8JAFdYsK1DFkVmd1vBuWwjOqZkZyCR-7E-EcfzUA_8A565jMyup5eOhMjAH5rHkaHxerJTEGKm47SZi10vY-xg9S21VPsldQY5-FBu3ikscXG0Lpem_mEvYi7F3qsVKnY0Cv3rEfG4A1F5BrpQ1yrd3aZuQ2B3DrgIrRdWtrBc0NcmLSkcYBKKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc1730f80.mp4?token=iUMRb6FQ3kQiJ1kkxFvivVi9TyRt8WGxa8r-_XFOOG9o4lyHytUvOqKHJ_SqOvGeWtnmQZrnZ9-qoUWRllvYij3n2Y5WAD-WEVyCRHbB_4_x3YntTOjWvfos7syLkgGA6Ga7Ur9I9FlrKOlV5t1Dc4k1QYM280d8JAFdYsK1DFkVmd1vBuWwjOqZkZyCR-7E-EcfzUA_8A565jMyup5eOhMjAH5rHkaHxerJTEGKm47SZi10vY-xg9S21VPsldQY5-FBu3ikscXG0Lpem_mEvYi7F3qsVKnY0Cv3rEfG4A1F5BrpQ1yrd3aZuQ2B3DrgIrRdWtrBc0NcmLSkcYBKKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر جهاد: هیج مشکلی در حوزهٔ تامین امنیت غذایی و کالاهای اساسی نداریم
@Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/451670" target="_blank">📅 19:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451669">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfdd5935a9.mp4?token=QPk9GT8gUi2vPpPU7qibbmdPKTLXg4yfjpast8-J2d63FzcBMNh35BTNw8DVZvOPKXfbMQ7OglhKeoAJUG428Hglfq2dPsjOrWoru6NeE4shLDXA1yzHXM2nXFQHy9EvoOCGYyPK2kwciSv80d24Ti9uPPSUlKHOw_x3A0iJxGgIpn_-leMFC61CH5T5M6EytyQ2kmSAuG15Koz4phigztEhps41HQOvTYgzhasW8FlZh8-t4ICFRaKGnbkL_ypjJ4rzXDoclT8WCZJxD-06xGIlQRKyQOntp9L6xJc8_EAy3mt3YmOgFhH_hYWarqwxxRJT3oW9UWj8vrfE1nYJuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfdd5935a9.mp4?token=QPk9GT8gUi2vPpPU7qibbmdPKTLXg4yfjpast8-J2d63FzcBMNh35BTNw8DVZvOPKXfbMQ7OglhKeoAJUG428Hglfq2dPsjOrWoru6NeE4shLDXA1yzHXM2nXFQHy9EvoOCGYyPK2kwciSv80d24Ti9uPPSUlKHOw_x3A0iJxGgIpn_-leMFC61CH5T5M6EytyQ2kmSAuG15Koz4phigztEhps41HQOvTYgzhasW8FlZh8-t4ICFRaKGnbkL_ypjJ4rzXDoclT8WCZJxD-06xGIlQRKyQOntp9L6xJc8_EAy3mt3YmOgFhH_hYWarqwxxRJT3oW9UWj8vrfE1nYJuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از خسارت به پایگاه آمریکایی Tower ۲۲
🔸
پایگاه نظامی Tower ۲۲ متعلق به ارتش آمریکا در شمال‌شرق اردن، در نزدیکی مرز سوریه که اخیرا زیر ضرب موشک‌های ایران قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/451669" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451664">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/epYrcpdv4Wb6_u5Earlno1AGglMySQLFw0c_vr5mmab95rlRVag4VUJLIjSBoflNV3oBmVEoaYLbctTf2bn48uRplBkrSEt2VJajsP5qDMIelBY2BuTPg5Rjw4WOevV04iIJyhuZOrCRZlBqbDBDojK3rTNTpOuJciku2sL2qL4PYegc0IXpDmIeq6bQ99-UWPAHITmevG5E-aBarId2H_b9LQJ1ZDHkpXq_OjnK1uGN0EoahoAZCVzh70UuYEFu15P-5VXGx9hwJ1vu7v2ldTeRzFK6WPspFTAA4heMdHQBqywNUwnHFiKO0_kAIBUlEZJ3H3mPHrq_viSkqsk8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eabAdHgIert0njTucxQGJ1xUpv2WtovO4TuABtWmJ0R_GqV5JlptU_f4bm3UEaJtzZ01jqggNrHK2H-IereBAp1mZOXWvsh5aKAHpe4lysKta_7UbuRZTniRpJNZ3p0z4w8xSt48PBDAAELmOdElwcT55eoMBNrqGk2JhlWyS_SYgoF-UB9BDlvuX5kJ5W4CidCYvpnIibeyBD4UeqcqxqGn8gsKUxTX8AbAkTWgM3FHRYPIzkH_ckzHhVz-RjrVSjK5Sf8Sdl3UB1pmFIeZqsK3UkTNE0TzWzS8rYYMlT13qXVDGcgl_8LNTE0w7LxC0I4robbu-i4An6OoCLAXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNVLXTdQMxIUF1eXP9MZSSBNyEl0qy_VB3hCEa02adwCcFFeH3b4Bdr8AqE_WMKXYY-2Ph90PVqabhspxGDpNS26cY1ytaL__PEhNA_qc06cPIX3GmdWFoEmryi5mG1JYYyG_34ZoCq0aIknS3BF7GLJ3J42hcorK-hrZI_Dm1DEoj3PX4UvpCOZTWgvVpfZkfekVZLqi1RIqqEcz8po4SnPCLxCIbJIvjCjuHdlTNIYjjxq-YxfQp_iLVFZUGURBLkYJQxb1EIcBuexkpMR_UOxbMbvDyByXKMCifGke_g_WSYVlXMWScn6WSaLDQvh-7W4m1VO_ILm9bBkptNN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rv5V-um5xN0FJqHi2VBoqi1QJrUVTrGs2Jkr1wU1yk5pegljv9K10KBI4tneWj5CawPh9rEMcRwZtV9y4sASrdoFvfKsY0fhhRGWC4104w0rQ-D6d8lTNBqChkD9hvv-wnRw5SC4EIblP91kUSizN0Xc389EMiHIUXfF-22RT6twn01W-jIcnH943h8v1e2mxwwxt_Pv7KYzfyQM_pzqZCsYRQNu1X1vClOBDezdyz_RJkRFsWHZwAfFcleaWdEKMLQJWGLKT1vhM3wg3XX0HWTmiRmDLROVH7BrQCVweW2tflh-3zddwmi0vdWegzpmF6iBtCZhkx7pxFa1zswgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xg4gonE-YDEd-iebWs1oCu6pOXE606BB2kqkp6rNw7Oc89Z6srPPjNdndRD2LwPMKP9W0s9Xsa_pAU_qLyhLhlDmiPsPRAMO-vwwY7SZ5opvIynYi1n_hGS6tJ_wnZblPOZuEK452MWV4783CemFQXAA8pw836l54z9wlzv5sw6azTdT6VTpLx46KrOSn7DghuelVDepvRDgFnK6U1c6ByaGwuaLoTmLpSmi4owXqrHHe_2gR1xaqOI-npKtQGVGVDMkZ4qqSRIvl1KUJhH_6KcOGul2_dBdVG3hjqVN3IbWMPx-zmMj4k-rcY3Tm25FQ5BmpgwRsgYiAY6CUNC14A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گرامیداشت روز ملی صنعت و معدن
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/451664" target="_blank">📅 19:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451663">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f2d573af0.mp4?token=SGQB1sGLzVZYpSda19IZFkcptggoiakUQarCvKrulLbpTDpKQM0s-UZddcaq7013MYCqBafcGhWbvNMeZCGf6oMF1RaKm46ar_0expDqPocRv436QPOhaUMbeUE6dzWfp86Nm45eXIBjz9eGzf_Vfn3F9iEgry0MvtkbCftN8iWDLM8AiWHscEjL6voC9SSQprkhOb-efXFXSPpaXiStQ_T-wbt4i4OBGQeCyZAz62Ka1uWgdY6QrsQiIzmm9QVhvAja0Ybfm9agDiO67srjm_lu4phuaDPe3AVdcJIf-aHjqVlCUbdVsbXra98z2wJWD_6lj9YEMZJ6Quypb_G59Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f2d573af0.mp4?token=SGQB1sGLzVZYpSda19IZFkcptggoiakUQarCvKrulLbpTDpKQM0s-UZddcaq7013MYCqBafcGhWbvNMeZCGf6oMF1RaKm46ar_0expDqPocRv436QPOhaUMbeUE6dzWfp86Nm45eXIBjz9eGzf_Vfn3F9iEgry0MvtkbCftN8iWDLM8AiWHscEjL6voC9SSQprkhOb-efXFXSPpaXiStQ_T-wbt4i4OBGQeCyZAz62Ka1uWgdY6QrsQiIzmm9QVhvAja0Ybfm9agDiO67srjm_lu4phuaDPe3AVdcJIf-aHjqVlCUbdVsbXra98z2wJWD_6lj9YEMZJ6Quypb_G59Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ تهدیدهایش را دوباره تکرار کرد
🔹
رئیس‌جمهور آمریکا: ما ۱۰۰ درصد به سایت هسته‌ای جدید ایران حمله خواهیم کرد.
🔹
آن‌ها دارند تلاش می‌کنند یک سایت دیگر را بازسازی کنند. ما به همان سایت ضربه خواهیم زد.
🔹
هر سایتی که حتی فکر برنامه‌های هسته‌ای در آن به سرشان…</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/451663" target="_blank">📅 19:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451662">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/913265ae74.mp4?token=eq2pL_aMDfnJUCaD5JJnZcY97nz7uq8Lf809OgQp2SqhwhRQVS4iLR11zzDpLf_0vUVD1sqQw3ENObez5KErCf6RAin3IrFza1fpzjBEtxLON1EOoNItej9pN12JWukmc_6Fq4GIHFbHV1m34S1WqRcli2LlMw7QvowAFmsqiA78N5AAU6NF8ihR4V6QSL-eDeqzcubUKjkhRZedIw6YAiZfi6Qk-OqcYQEnkbpehP0LJx54UVyQu87ciXK3_Fu4mcfzTX9CWzqspNZHAfOtQOcIg9Iy16uPaLKYIK9bneUDbjskKE59ObFh01rF5E_CQsRXS00J1L4NIJyC55cRtkpSSkHGJadjMU5Cih7n9TcZ_00oaxhJbyXMygfyjEH59c8222n5ZLw46vR-V2ZR0KlDTKaXxkms8sp8368KwEYqX4XcyUNOfcBnjb0G-LurzHPhgoIoUIrjcO0WnIHWLsFysP5f8zBk8DNnzW57GIXv84ewt8euzz7_pgSSJVZBXURM0Se9t9QEx8UYApfgNkwr2DynAVcvP5cWf88UlpeCUBCbYn5eY5905sow2LUt_Y2S__IHRar0OvwaASZy2gbW8G4ySd2xSctqF6C3zeqajU8Ut-aWmOkj8Qjcx5HIt11zBH6g-TiDDP3gH7GpR4UxGrtUh2mAPd9LSQ-TeLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/913265ae74.mp4?token=eq2pL_aMDfnJUCaD5JJnZcY97nz7uq8Lf809OgQp2SqhwhRQVS4iLR11zzDpLf_0vUVD1sqQw3ENObez5KErCf6RAin3IrFza1fpzjBEtxLON1EOoNItej9pN12JWukmc_6Fq4GIHFbHV1m34S1WqRcli2LlMw7QvowAFmsqiA78N5AAU6NF8ihR4V6QSL-eDeqzcubUKjkhRZedIw6YAiZfi6Qk-OqcYQEnkbpehP0LJx54UVyQu87ciXK3_Fu4mcfzTX9CWzqspNZHAfOtQOcIg9Iy16uPaLKYIK9bneUDbjskKE59ObFh01rF5E_CQsRXS00J1L4NIJyC55cRtkpSSkHGJadjMU5Cih7n9TcZ_00oaxhJbyXMygfyjEH59c8222n5ZLw46vR-V2ZR0KlDTKaXxkms8sp8368KwEYqX4XcyUNOfcBnjb0G-LurzHPhgoIoUIrjcO0WnIHWLsFysP5f8zBk8DNnzW57GIXv84ewt8euzz7_pgSSJVZBXURM0Se9t9QEx8UYApfgNkwr2DynAVcvP5cWf88UlpeCUBCbYn5eY5905sow2LUt_Y2S__IHRar0OvwaASZy2gbW8G4ySd2xSctqF6C3zeqajU8Ut-aWmOkj8Qjcx5HIt11zBH6g-TiDDP3gH7GpR4UxGrtUh2mAPd9LSQ-TeLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
تصاویر ماهواره‌ای از انهدام مرکز اسکان نیروهای ارتش تروریستی آمریکا در پایگاه ملک فیصل اردن در اثر عملیات موشکی ایران  @Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/451662" target="_blank">📅 19:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451661">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnOH_HXPDTXsfkKi6Ue8oTIWEhPrBh2yNP1XvbuoglZw-C7IdUk0YGXfGYSL0qpgvEQ97fLmUtnFN3Ds9srcyQVzRXzGEhhxF_90MsL2CvL-g7T0a5V5NP9GvA31kgFbWYLdraX1fr97hHnW5yP4hIzoSITV16rJczt8NN_Qydz_AN9evG_owhvJ1I_5TM_jV8exFItCBJI6RY90SRIuh_8s6o7Y44F2uqfumsxtL4Rjt2uIqHMVLviVGhUNR1x0U3HqjlPU2O2Ehsstyk-IGqBEjbVUd6wF8kUmG3ASyyNQBpv7S6V4FgXPVD7pbbY0yy3681EKpzaZ_9x_mfW0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیلی: دوگانه «جنگ‌طلب و صلح‌طلب» تله تضعیف امنیت ملی است
🔹
وزیر ارشاد دولت سیزدهم: هرگونه تلاش برای تقلیل فضای سیاسی به دوگانه «جنگ‌طلب» و «صلح‌طلب» نه با واقعیت‌های امنیتی جمهوری اسلامی ایران سازگار است و نه با مبانی علوم راهبردی.
🔹
به اعتقاد من، القای این گزاره که هرگونه ایستادگی در برابر زیاده‌خواهی دشمن به معنای جنگ‌طلبی است، نوعی عملیات شناختی برای حذف گزینه مقاومت عزتمندانه از محاسبات افکار عمومی محسوب می‌شود.
🔹
جمهوری اسلامی ایران هرگز آغازگر جنگ نبوده است، اما دفاع از منافع و امنیت ملی را وظیفه خود می‌داند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/451661" target="_blank">📅 19:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451660">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4b70551d5.mp4?token=PuazLs307bHVjUKsSysKhgHiwhTM1qVW0R0xxOpghR23F6YY7fdGXxeh8MOW6NIG6iScIHrWfQCN8KSf50GHNCPhGFmnD5vlO20-sin6IcBW9_TUz-0EqmuAC8EecPXHPKIIx9MsMnj8jjoI5KHQIZDBdeYvXFAD2T0qdrBNxZuEao7yFKsKk9199P9H44tzTjrpRzgGbFfMt8Zsoz6t9g5Nl1Tkk2QxcvelW0BH0Jz8KW8g1sj0-n5t_CajmOvKLEyY-OJCwZmjqFWkX89duEwIsGZydaj5I3YUYZoQsVgEy4NH8kleWQNPR3eBA3qA7xTbLDPvIQqOyWitA3iOLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4b70551d5.mp4?token=PuazLs307bHVjUKsSysKhgHiwhTM1qVW0R0xxOpghR23F6YY7fdGXxeh8MOW6NIG6iScIHrWfQCN8KSf50GHNCPhGFmnD5vlO20-sin6IcBW9_TUz-0EqmuAC8EecPXHPKIIx9MsMnj8jjoI5KHQIZDBdeYvXFAD2T0qdrBNxZuEao7yFKsKk9199P9H44tzTjrpRzgGbFfMt8Zsoz6t9g5Nl1Tkk2QxcvelW0BH0Jz8KW8g1sj0-n5t_CajmOvKLEyY-OJCwZmjqFWkX89duEwIsGZydaj5I3YUYZoQsVgEy4NH8kleWQNPR3eBA3qA7xTbLDPvIQqOyWitA3iOLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای اسرائیل درباره انتقال هزاران سانتریفیوژ ایران به اعماق کوه کلنگ
🔹
روزنامه وال‌استریت ژورنال گزارش داد که دستگاه اطلاعاتی اسرائیل ارزیابی کرده که ایران هزاران سانتریفیوژ غنی‌سازی اورانیوم را به کوه کلنگ منتقل کرده که هدف قرار دادن این تجهیزات در حملات…</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/451660" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451658">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/133652fe64.mp4?token=tPmvIeqQzZMXbbZ2IbdSVSI__BxhJfAksRoaK-dGXsNv3UHOnhPmvYIByveHcRu8_mLKdxtjJ8zbTnvIawsG_r0f0z-CklTJmXbqv_pgXSgrEKs8kDKkS3ZtahwnR9sOgqtTfaZIkhWM-t-eZ-Cruv4pE_SOF5mNKHDPeW1LTbKYEJoa_9S5jChdNT2vZslW-DA8X85Zg3MUus1_0wiQVfnZTjVU7b-Sl3LuFv_b6UwCEja6AYSJ9MNWf4v8rF_3UQbmVW2ltbp_XykSejWCNTzAJn-M9AIerDmobEgtOu7z3QwHIbpYfduOfze98b-qmlGtPHBmeN5QftN8GkZ1ujbiQFSRgnODXaAN3H-OI0m0r73LRuZ_tpggDgPPHzzmE-y8nRY3thrDU9MTyWLgGEQfaSZju5dCIjpJJadMxnzQu2EIo089InF_UcZpfO8JMV6pAKLFSRWGFuUOcJ7dQvOpjHx2YNskYwm4RTMu8cOSIMK4X-SKuragJD0i2St9_ZyzcJZ4c35HSlAIrsaPiS5uokwCo_Dx8PvVWZe1OBIvlymG-HxZfSVINEqIHlF977CP7yKy5euOS4yfAGX6PvY4bPmOPHj9zoobTctL4PIgQpym6LNrqYV_gN8m3l2vtnwDap4PX2VUjPQHB5SZCm3kBQhETy0C4RDjosjOpsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/133652fe64.mp4?token=tPmvIeqQzZMXbbZ2IbdSVSI__BxhJfAksRoaK-dGXsNv3UHOnhPmvYIByveHcRu8_mLKdxtjJ8zbTnvIawsG_r0f0z-CklTJmXbqv_pgXSgrEKs8kDKkS3ZtahwnR9sOgqtTfaZIkhWM-t-eZ-Cruv4pE_SOF5mNKHDPeW1LTbKYEJoa_9S5jChdNT2vZslW-DA8X85Zg3MUus1_0wiQVfnZTjVU7b-Sl3LuFv_b6UwCEja6AYSJ9MNWf4v8rF_3UQbmVW2ltbp_XykSejWCNTzAJn-M9AIerDmobEgtOu7z3QwHIbpYfduOfze98b-qmlGtPHBmeN5QftN8GkZ1ujbiQFSRgnODXaAN3H-OI0m0r73LRuZ_tpggDgPPHzzmE-y8nRY3thrDU9MTyWLgGEQfaSZju5dCIjpJJadMxnzQu2EIo089InF_UcZpfO8JMV6pAKLFSRWGFuUOcJ7dQvOpjHx2YNskYwm4RTMu8cOSIMK4X-SKuragJD0i2St9_ZyzcJZ4c35HSlAIrsaPiS5uokwCo_Dx8PvVWZe1OBIvlymG-HxZfSVINEqIHlF977CP7yKy5euOS4yfAGX6PvY4bPmOPHj9zoobTctL4PIgQpym6LNrqYV_gN8m3l2vtnwDap4PX2VUjPQHB5SZCm3kBQhETy0C4RDjosjOpsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نیویورک‌تایمز: در حملات چندبارهٔ ایران به پایگاه هوایی موفق اردن دست‌کم ۲۴ نیروی نظامی آمریکایی مجروح‌ شده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/451658" target="_blank">📅 19:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451657">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAE5Uq69NflospUrDyDneFNr-IKtau32MPpwhznpYkZUoYcuCpazdCr9S_xeGNzX1GDfWfkxUyorO37z30B87j-CoKkq9hu3DHQ2dxVylMTzcftEZqcfsvkKPGcK7df01MkKUboPdgyLvN5l1H036naG5LFj3ljs3_SV80OqumcjPv0kmAZfjUyqi6rXsH4ifkICNQD4LHIG7erbeYMJxaXvehViq1UdNTmsqKpAneYyJRdi4PPM7jmC9i5bsD10-vphCfHZSnKgBcmJupR1B-lkt18uPjzhCZtJZXr2TamQWPU9ZEo-Rx27ZmY85yUR3dK4obRGIw14rle3Ku7mzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نیرو: ۴ استان جنوبی درگیر جنگ از قطعی برق معاف می‌شوند
🔹
استان‌های سیستان‌وبلوچستان، هرمزگان، بوشهر و خوزستان اخیراً درگیر جنگ با دشمنان صهیونیستی و آمریکایی شده‌اند؛ مردم سایر نقاط ایران با صرفه‌جویی در مصرف برق، این هدیه را به هم‌وطنان خود در این مناطق می‌دهند تا این ۴استان از اعمال خاموشی معاف شوند.
🔹
بساط خاموشی‌ها تا نیمۀ شهریور برای همیشه جمع می‌شود؛ این وعده تنها مختص به مقطع کنونی نیست، بلکه برنامه‌ریزی‌ها به‌نحوی انجام شده که با اقدامات کلان مجلس و پیگیری تعهدات در وزارت نیرو، اقتصاد برق اصلاح شده و صنعت برق بتواند روی پای خود بایستد، بدون آنکه فشاری به مردم وارد شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451657" target="_blank">📅 19:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451652">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iu66idIitPNiEOl9J2zSTUPccTWGQUmhpxckUs35xxiH-lS3FV69W81bgyO5nn5ua05ZWXjoODuDVBAQcmVG6XZhp6nUv2Od2riJDkEf42Ervwqfu7hVj-aqp3iMoFg4pI9dpM0skYRaWt0aQFAS7ZssY5ilMMa_yP9y52idzxBaSkOpzpm_ni4ym6X3-tGabTwYlcrFjImijzkzu1m_5QOdUEmioAId1sAjmuY2YT3QRIt4Xaygezmqus9adL8Bes1ZKR9oPMm7Sd1JDKDNMaSSdIEUK_6WBnpXGKKTCO60jpmwAl00MN_VLHoLF7L_i4KJ2G8Mcd0CjIKit973ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NgCOTThkhWjeR3wOaChMOYp6XYf5QSoJoa871wKob9HzDuzO7Pw7nEAMmcfDO_Y60MulT7tEglZqkSnqFPZit6AtsQCRDys2KC7_vxFj_4H-v1y0cmfz0jwXJ6HAsspE6AOTeiLzR7hbg2mxRuYXRUYTh3kTO62LLOKocfCuKZ92l-0IUBgftg-yVBYCgrubD1sHdCyfvbGl9xDvSSNmfErRYmycqtvdoddnANv4xFc0Wn2GbMEwz7GQLJOxsqv89LGmdHdhX9fjs73KbvNpNEQr5_7qMapwY3CRFEuElSWnfqfAE1SQ74hvLGWK4JV8_bM3pQTsXvbC_Cul0G8aPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwWR58PG7QVetXSSFopLp2lDMdjOPCJcn-CvUffWUVeZF1aYwBXFwNj0VpHknkQsWzEeigDCHGDb7bX1Mo79fghmJ9c7VssqwNpgHzveUP2YL5vHd4b69Ud2Ald5GBA7IaMqhes2cbice-kbBYj7pz1e2u1GNCqnOu2I46-YuFOwyaAMpl6lWiNw98kOzRsZzzRDsgIWn65g1dGfe1xbJOdqe09j9dae-9T3NMj62q1iThGbT0H4hBTevr8wC_whCtAKGjm9lPSXbyCkR5-jBHoQbCqk31gHsANrB0s9O-DsGWDaX0XPWSVpJttfk9UjgbjVo421-KjurghJ_-0CYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SLodbSZ_mUbc-jwePqhWIWlRoFgaE5EQqLeCGf1KdgzHsvHUXhudacyVo26xfvQa1Zj0YXJoA7AzP5NfK95u15Ofivb1RafLvL_EUwPES4pjmChqEyPo02iE-THkIHpS8bP0NV9jCbG7AfvmuZboSSzczBke5nq1XMtubg4UugCfRkG7nk_9yd0LRxlmBVsULGstawEP_mv7fWorqSdd6Ox133FRQeKPGoYHbSWejNVesLnuT1KqASio52fA5EOGTV57IRDnqmX4M5-56O3c0m-h9yGB-VrGXDyQW0RwoqoBAu-K79MxgZKZB7XN2-SJRvIcT-KhNmzbpxuCWEyJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kaPMU_fMwy17aNsOUfyQup4xo9IbYQ1xkQpaxPruDsGAqqscMc_5QWaIoAHjUpo7DWSzb3SWrR9KnlRfZH5CURP6W-lpwXIaYFGKHYtNyVqxQiCRZtGFijoNGt76ccLvZ4Hfb7GTgNJKEdXu_MpajrrjiohNezu3piXFTqENuIuHlVvxQCDe_r-1029Rdto1cFdSLNVYTcAtT3kz0GkYv3_XYnnSZk2-32o0TkOfNUBtthxFw4YJXAoD62B0pGEjACKIPSd6ujnZs2q6jlp2hXDiLyzs8PubzKDMT_LUyk6bHdLykiFHCQymZKxeirfZ6AERn-jR_bzPxsiWA-k2xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
با کوله‌ای از خاطرات جنگ راهی کربلا شد
🔸
سفر اربعینی سیدرضا مفاخری، جانباز ۲۵ درصد دفاع مقدس، از کرج با دوچرخه آغاز شد.
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/451652" target="_blank">📅 18:58 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
