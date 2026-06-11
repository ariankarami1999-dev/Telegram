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
<img src="https://cdn4.telesco.pe/file/cVsREW4kUwULfeEZb0xr32Qwvgo4xHnszBEv4ik2MO42oPwf3Qz3Gj1w_wVepVvMAf2tWuugZYPLsmY-LkVrgovPFgfgoxArFS-1--CICKYHiAF7yx5dXqNGzC3u1EJuunYdTJXr4FCluFeoW40ro9aDgsrnHfb9jpYsAko972e4zlDnY9XDXnWgyez1_ZCcpyNyW99VduBlY9Wy-lI_Y9pprgqNcEyOyOtg2RMZlE9ATd6Cdb0OvpexnHmJPORMkwpr7HzVrY0PvyTF--7Bz8LZQVZx3414iMTG7HJevsx8IYnDnZoCnPSpdYL-3hFtXg5ysVYbGMFm-SjK-D5Nlw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 323K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 00:43:33</div>
<hr>

<div class="tg-post" id="msg-14587">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/withyashar/14587" target="_blank">📅 00:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14586">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer"><a href="https://t.me/withyashar/14586" target="_blank">📅 00:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14585">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انفجار در سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/withyashar/14585" target="_blank">📅 00:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14584">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اکسیوس، به نقل از یک منبع: نتانیاهو هیچ اطلاع قبلی نداشت و وقتی ترامپ بیانیه اولیه خود را در مورد توافق با ایران منتشر کرد، غافلگیر شد.
@withyashar</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/withyashar/14584" target="_blank">📅 00:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14583">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">https://t.me/boost/withyashar
بوست داره میریزه…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/withyashar/14583" target="_blank">📅 00:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14582">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خبرنگار: دیروز گفتید که ایران ممکن است در حال همکاری با ایالات متحده باشد. آیا شما معتقدید که این بار در خواست خود برای پیگیری دیپلماسی صادق هستند؟
ترامپ: این به سطح هیجان آغاز شده در آن بستگی دارد. ما در سه روز گذشته به شدت به آن‌ها فشار آوردیم. امشب حتی سخت‌تر به آن‌ها ضربه خواهیم زد. آن‌ها این را می‌دانستند.
ما دقیقاً به آن‌ها گفتیم که قصد داریم چه کاری انجام دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/withyashar/14582" target="_blank">📅 00:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14581">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">️واشنگتن پست: توافق بزودی در رم یا ژنو امضا میشه
@withyashar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/14581" target="_blank">📅 00:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14580">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ درباره رهبری ایران:
من این افراد را بسیار منطقی‌تر از کسانی که دیگر در میان ما نیستند می‌یابم.
این گروه متفاوتی است و فکر می‌کنم گروهی باهوش‌تر و دارای دلیل و منطق است.
همه آنها این توافق را تأیید کرده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/withyashar/14580" target="_blank">📅 00:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14579">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad8668d6f.mp4?token=vmYqw2NM49RmlsvG6GKkMusI80bhsLGH6BuitaPMNBuYXnsWSqyJ-fOAEbwpAtyDbAPdqMPEkZFpPKaKcQf2u3WgsBW8kEwp8vHIrfkH4IXjFHgex_oCUj-Xc7ao2Go_7mEUJTpmThbo2LsPxAQDsMPwQgYWiEN6lOe5FIKIceuADrOA74CdwWHxNpJ2Ztf_wIVTT0S0sqUVpNX4IO8FGG6AjxowZOT-xkg5zRLxekjaMkQT3TRblqk-SME-QbcBH5bhrVbmN36dk3VjTxIH1exiDKK46TYahPsG55mM4YglC_pAGMIrOJEKBsy5BS3siSu5sPi5kUMKV7cHtnaSFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad8668d6f.mp4?token=vmYqw2NM49RmlsvG6GKkMusI80bhsLGH6BuitaPMNBuYXnsWSqyJ-fOAEbwpAtyDbAPdqMPEkZFpPKaKcQf2u3WgsBW8kEwp8vHIrfkH4IXjFHgex_oCUj-Xc7ao2Go_7mEUJTpmThbo2LsPxAQDsMPwQgYWiEN6lOe5FIKIceuADrOA74CdwWHxNpJ2Ztf_wIVTT0S0sqUVpNX4IO8FGG6AjxowZOT-xkg5zRLxekjaMkQT3TRblqk-SME-QbcBH5bhrVbmN36dk3VjTxIH1exiDKK46TYahPsG55mM4YglC_pAGMIrOJEKBsy5BS3siSu5sPi5kUMKV7cHtnaSFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا رهبر ایران این توافق را تأیید کرده است؟
ترامپ:  تا جایی که می‌دانم پاسخ بله است.
@withyashar</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/14579" target="_blank">📅 00:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14578">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/14578" target="_blank">📅 00:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14577">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ :  ما این جنگ رو از نظر نظامی خیلی زود بردیم، تنها چیزی که نبردیم، رسانه‌های فیک‌نیوزه
تنگه بازه؛ ولی این تنگه‌ها از چند ماه پیش هم باز بودن، فقط شما خبر نداشتید
@withyashar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/14577" target="_blank">📅 00:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14576">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دفتر نتانیاهو: رئیس جمهور ترامپ با نخست وزیر نتانیاهو در مورد نهایی شدن یادداشت تفاهم با ایران برای ورود به مذاکرات صحبت کرد.اگرچه اسرائیل طرف این یادداشت تفاهم نیست،نخست وزیر از تعهد رئیس جمهور ترامپ برای اطمینان از اینکه توافق نهایی که در پایان مذاکرات شامل…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/withyashar/14576" target="_blank">📅 00:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14575">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad4cd3bf3.webm?token=LJCK8bM12PhwwNP1lsgwwRpXg33-n8n_atBTJlyWwlzf3xVMWDMuOoxcXFdEeFf42cKMlxqPoRlWGBm5PAfUDWWIEPR5tGdh0SGSd3stMRTyQ29R6YFZ0j5iG4vtjwAaI6aImhlHV9azxdBCfXT-72hBuGNokpMKNrp8vm8jeEl-mcgPL-ZjCHfhPfAK-iu8__5SFZ-NPr5W_8qi373KY6gxy0ZNqIVJDvEkConxipeT06a0ZDbHoIwSIMetPPDVzth0RWSuWtt6aIO_xdJu_Gfl0NE_a-7azgQcOHzcjy2sW058eWVSPw1p-2PxeBdqtsF1jJ9muR5wQBmFyKUu-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad4cd3bf3.webm?token=LJCK8bM12PhwwNP1lsgwwRpXg33-n8n_atBTJlyWwlzf3xVMWDMuOoxcXFdEeFf42cKMlxqPoRlWGBm5PAfUDWWIEPR5tGdh0SGSd3stMRTyQ29R6YFZ0j5iG4vtjwAaI6aImhlHV9azxdBCfXT-72hBuGNokpMKNrp8vm8jeEl-mcgPL-ZjCHfhPfAK-iu8__5SFZ-NPr5W_8qi373KY6gxy0ZNqIVJDvEkConxipeT06a0ZDbHoIwSIMetPPDVzth0RWSuWtt6aIO_xdJu_Gfl0NE_a-7azgQcOHzcjy2sW058eWVSPw1p-2PxeBdqtsF1jJ9muR5wQBmFyKUu-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: عملیات جزیره خارک دیگر روی میز نیست.  می‌خواهید آشوب ببینید؟ می‌خواهید مرگ و ویرانی ببینید بگذارید ایران سلاح هسته‌ای داشته باشد  نمی‌خواهم برای دستیابی به توافق با ایران ضرب‌الاجل تعیین کنم. @withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/14575" target="_blank">📅 23:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14574">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ: عملیات جزیره خارک دیگر روی میز نیست.
می‌خواهید آشوب ببینید؟ می‌خواهید مرگ و ویرانی ببینید بگذارید ایران سلاح هسته‌ای داشته باشد
نمی‌خواهم برای دستیابی به توافق با ایران ضرب‌الاجل تعیین کنم.
@withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/14574" target="_blank">📅 23:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14573">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وزارت امور خارجه ایران:
ما قبلاً گفتیم که بیشتر مفاد توافق‌نامه حل و فصل شده است، اما طرف آمریکایی می‌خواست خواسته‌های جدیدی را اضافه کند.
@withyashar</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/14573" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14572">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دفتر نتانیاهو: رئیس جمهور ترامپ با نخست وزیر نتانیاهو در مورد نهایی شدن یادداشت تفاهم با ایران برای ورود به مذاکرات صحبت کرد.اگرچه اسرائیل طرف این یادداشت تفاهم نیست،نخست وزیر از تعهد رئیس جمهور ترامپ برای اطمینان از اینکه توافق نهایی که در پایان مذاکرات شامل حذف مواد غنی شده،برچیدن زیرساخت‌های غنی سازی،محدودیت تولید و برد موشک و توقف حمایت ایران از گروه‌های تروریستی وابسته به آن در منطقه باشد، ابراز قدردانی کرد.
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/14572" target="_blank">📅 23:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14571">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ادعای نورالدین الدغیر خبرنگار الجزیره در تهران:
دیگر همه چیز قطعی و تمام شده
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/14571" target="_blank">📅 23:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14570">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
دو فروند هواپیمای آواکس E-3B Sentry  یکی بر فراز عربستان سعودی  دیگری بر فراز خلیج فارس رادار خود را خاموش کرد ﻿
@withyashar</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/14570" target="_blank">📅 23:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14569">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ در برنامه زنده: همین الان مطلع شدم که مجتبی خامنه‌ای، رهبر ایران با توافق موافقت کرده است. ایران حالا منطقی‌تر عمل می‌کند.
از نظر نظامی در این جنگ پیروز شدیم
ایرانی‌ها فرصتی دارند تا کشورشان را که تا حد زیادی ویران شده است، بازسازی کنند.
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/14569" target="_blank">📅 23:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14568">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تسنیم: منابع ایرانی می گویند هیچ توافقی نهایی نشده است و هر ادعایی در این زمینه تا قبل از تصویب در ایران فاقد اعتبار است.
@withyashar</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/14568" target="_blank">📅 23:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14567">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/14567" target="_blank">📅 23:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14566">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کامنتم هم زیر پست ترامپ، کارهای اداریش را انجام بدهد فقط همین رو لایک کنید  https://www.instagram.com/p/DZdJ2LZvAza/?carousel_share_child_media_id=3917330556395457754_347696668&comment_id=18055196378739071</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/14566" target="_blank">📅 23:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14565">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer"><a href="https://t.me/withyashar/14565" target="_blank">📅 23:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14564">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">العربیه: آمریکا قبول کرده تحریم‌های ایران رو کاهش بده و محاصره دریایی رو برداره.
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/14564" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14563">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">۳پا: اگر امریکا تمام خواسته‌های ما را در سندی که ارائه دادیم بپذیرد، به احتمال زیاد ما این توافق را تایید خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/14563" target="_blank">📅 23:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14562">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ از عاصم منیر پاکستان تمجید می‌کند:
من او را ژنرال می‌نامم. او یک ژنرال است. او یک ژنرال بزرگ است—آنقدر بزرگ که در واقع یک مارشال میدانی است، یک درجه بالاتر.
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/14562" target="_blank">📅 23:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14561">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ: ما به‌زودی توافق را امضا خواهیم کرد و اسناد در وضعیت تقریباً نهایی هستند. باید خیلی سریع انجام شود.
همه بسیار خوشحال هستند. کل خاورمیانه خوشحال است. و فراتر از خاورمیانه نیز همین‌طور.
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/14561" target="_blank">📅 23:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14560">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ:  من نمی توانم در مراسم امضای قرارداد شرکت کنم و ونس در امضای توافقنامه ایران حضور خواهد داشت.
امضای توافقنامه با ایران ممکن است به زودی و شاید در آخر هفته انجام شود.
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/14560" target="_blank">📅 23:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14559">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ: توافق به دستیابی به توافق در روزهای آینده بستگی دارد و ممکن است امضای توافق ایران در اروپا انجام شود.
تنگه بلافاصله پس از امضای توافق باز می شود.
@withyashar</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/14559" target="_blank">📅 23:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14558">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ:  ما به توافقی دست یافتیم که ایران را از داشتن سلاح هسته ای باز می دارد.
من همین الان با نتانیاهو صحبت کردم.
اسناد ایران تقریباً در مرحله نهایی است.
من فقط با رهبران قطر، امارات و عربستان سعودی صحبت کردم.
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/14558" target="_blank">📅 23:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14557">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دفتر امیر قطر:
ترامپ تأیید کرد که تفاهمات ایالات متحده آمریکا و ایران مورد تأیید همه طرف‌ها است
@withyashar</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/14557" target="_blank">📅 23:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14556">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83be481908.mp4?token=glr75D7mbgGhFY2D76h_KNHj31NzOPQl33szEFQIF7XfRPRshouuwoQ_lwE5NxO2isXzLBY1Jz7hwJ96O7cumTP7iB7oYKMaL-jLp2OBHDbM1WzCnQ_XL6-YnZiUTOxrrl4WlwkNWrEKNJ_Yt7bFd8to7Fw5wbFP7xjpsgYiJdVqfG8LEsyOrE84KlmVT0UWxq2pv-DA-qL5DNtgobKOx7qrmAUJdRCaSlDMxg-nQ_tv0VbLrdH3xdzUWqAoNnxpDT9z7lMCwNTqjT-xpLxvyky4UAgLgtCCgGEFAb2sBM0aE6DT4qR_5vqi82E5TXD3xiJmt2hPzPqtgf3dokRx-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83be481908.mp4?token=glr75D7mbgGhFY2D76h_KNHj31NzOPQl33szEFQIF7XfRPRshouuwoQ_lwE5NxO2isXzLBY1Jz7hwJ96O7cumTP7iB7oYKMaL-jLp2OBHDbM1WzCnQ_XL6-YnZiUTOxrrl4WlwkNWrEKNJ_Yt7bFd8to7Fw5wbFP7xjpsgYiJdVqfG8LEsyOrE84KlmVT0UWxq2pv-DA-qL5DNtgobKOx7qrmAUJdRCaSlDMxg-nQ_tv0VbLrdH3xdzUWqAoNnxpDT9z7lMCwNTqjT-xpLxvyky4UAgLgtCCgGEFAb2sBM0aE6DT4qR_5vqi82E5TXD3xiJmt2hPzPqtgf3dokRx-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/14556" target="_blank">📅 22:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14555">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/14555" target="_blank">📅 22:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14554">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer"><a href="https://t.me/withyashar/14554" target="_blank">📅 22:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14553">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">زاکانی: مراسم تشییع جنازه علی خامنه‌ای در دهه دوم محرم برگزار خواهد شد.
@withyashar
😂</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/14553" target="_blank">📅 22:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14552">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ادعای الحدث:
هیئت قطری در بازگشت از تهران، موافقت ایران با پیش‌نویس نهایی را منتقل کرد
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/14552" target="_blank">📅 22:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14551">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبرنگار نیویورک‌پست: ترامپ همین الان به من گفت که توافقی با ایران کاملاً نهایی شده
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/14551" target="_blank">📅 22:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14550">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کامنتم هم زیر پست ترامپ، کارهای اداریش را انجام بدهد فقط همین رو لایک کنید
https://www.instagram.com/p/DZdJ2LZvAza/?carousel_share_child_media_id=3917330556395457754_347696668&comment_id=18055196378739071</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/14550" target="_blank">📅 22:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14548">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آکسیوس:  منابع ایرانی امروز به کشورهای منطقه اطلاع دادند که توافق «اصولی» در مورد یادداشت تفاهم حاصل شده است، اما تأیید رهبری همچنان لازم است
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/14548" target="_blank">📅 22:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14547">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شبکه 13 اسرائیل :مقامات اسرائیل توافق با ایران را به رسمیت نمی‌شناسند
.
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/14547" target="_blank">📅 22:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14546">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فارس به نقل از یک منبع آگاه نزدیک به تیم مذاکره‌کننده اعلام کرد که جمهوری اسلامی هنوز هیچ متنی را برای توافق با آمریکا تایید نکرده است.
این منبع اظهارات دونالد ترامپ درباره نهایی شدن قریب‌الوقوع توافق را رد کرده و گفته تاکنون هیچ یادداشت تفاهمی میان دو طرف مورد تایید قرار نگرفته است..
@withyashar</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/14546" target="_blank">📅 22:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14545">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/14545" target="_blank">📅 21:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14544">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شبکه آی۲۴: مقامات اسرائیلی از پست ترامپ غافلگیر شدن و فعلا برای ارزیابی وضعیت به اظهارات علنی رئیس‌جمهور آمریکا تکیه دارن.
به گفته یک مقام اسرائیلی، تل‌آویو پیش از قضاوت درباره صحت ارزیابی ترامپ، منتظر موضع رسمی جمهوری اسلامیه و تجربه‌های گذشته نشون داده که صحبتهای ترامپ همیشه دقیق نبودن.
@withyashar</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/14544" target="_blank">📅 21:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14543">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سه منبع آگاه از مذاکرات به اکسیوس ادعا کردند که اختلافات کلیدی در جریان گفتگوهای روز چهارشنبه بین مقامات ایرانی و میانجی‌های قطری حل شده است.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14543" target="_blank">📅 21:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14542">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرنگار نیویورک پست: ترامپ همین الان به من گفت که توافقی با ایران "تقریباً کاملاً نهایی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14542" target="_blank">📅 21:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14541">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">LIVE ON INSTAGRAM جام جهانی ۲۰۲۶
INSTAGRAM.com/YASHAR</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14541" target="_blank">📅 21:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14540">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56c98e45a.mp4?token=UtGbJgHP5hwBW91dbB5ZbmSEyjPM11E4LLfd61VC_OJ-bkSkMnQ1f8dkGX8_RN_04xzQcqxeZ_Xg6goUaC1JNChWBB2SL-G4sqNVxVTqC4-X5gCR-2I6g_UP9UCNDXvFTIofLbF_XdI8ZyWOPikgFx1AhdZOrzc9bf6uGjnMm15VqTembGgVquDiD83xldV9tOq9RkQU6neJCF9KPufVbPOw3xN5yyl0Y5Uug2adhCK1NpQOeVhFp5XhNjGGENgVRLs-o01GS0r5unIY0EooFbDJH7q597bSd2pJl2yQiIcMccnCKBhkpu-sOHU6pZACpSgI-wCcRnnShvXbusvWPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56c98e45a.mp4?token=UtGbJgHP5hwBW91dbB5ZbmSEyjPM11E4LLfd61VC_OJ-bkSkMnQ1f8dkGX8_RN_04xzQcqxeZ_Xg6goUaC1JNChWBB2SL-G4sqNVxVTqC4-X5gCR-2I6g_UP9UCNDXvFTIofLbF_XdI8ZyWOPikgFx1AhdZOrzc9bf6uGjnMm15VqTembGgVquDiD83xldV9tOq9RkQU6neJCF9KPufVbPOw3xN5yyl0Y5Uug2adhCK1NpQOeVhFp5XhNjGGENgVRLs-o01GS0r5unIY0EooFbDJH7q597bSd2pJl2yQiIcMccnCKBhkpu-sOHU6pZACpSgI-wCcRnnShvXbusvWPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14540" target="_blank">📅 21:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14538">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0No7XnzQqfQVoThPykHNLYKIOCVSWHojA6FEFBXTgWViyBvjIZNijoWz0l2JT0O6ss8PNE_lS76cUnkThv7LXph8IJHzSRjf1tEAOK25k255fbit2s1g4lkz1HrJ1t5WfNtsbvanaH-WNNrP17tp7IB1BRXz7B81KlC_ogoendTm4w25o4cKlUxq_byh7gLUXAVgGKC1c8rpEckUjv_e0C81DPUA_-y7sEhLzSppAbUH7KQ3nwY3kFZZtWQ13YOSxLCRM5D6KJ1E8oIywqW7CAmqjYBXrx3UELxAA8S81WCt9Rpxgw2Uy_T8Bcdaa9DsGOWloYz0WieuGetoqcXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایرانیان برده شده و تایید شده است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی شده علیه ایران امشب را لغو کردم. مذاکرات و نکات نهایی، هم از نظر مفهوم و هم با جزئیات فراوان، توسط تمام طرف‌های درگیر، از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات متحده عربی، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران، تایید شده است. محاصره دریایی تا زمان نهایی شدن این معامله به طور کامل و با اثر باقی خواهد ماند زمان و مکان امضا به زودی اعلام خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14538" target="_blank">📅 21:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14537">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ: بمباران امشب را لغو کردم
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14537" target="_blank">📅 21:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14536">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">صدا و سیما: ویدیو انیمیشن انفجار اتمی که نیمه‌شب از صدا و سیما پخش شده بود، بابت خطا در تدوین بوده
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14536" target="_blank">📅 20:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14535">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شبکه ۱۳ اسرائیل : نتانیاهو یه جلسه امنیتی فوری با مقاماتش برگزار می‌کنه
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14535" target="_blank">📅 20:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14534">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKjMHUY6A3gDsr52_7y-JYCypz85oaOx2GCr3HEy-jTnxhAxgCBi45YD0v5zaijsaT7h3xnpOKIJA1ugEp7SlBTpia3fPDB7eHsis1GAisndIqIAQ8_zRg7E_XmkJ08qSMf5cDSpDOY8ZTTWzWjLMO6BqFR5OBXtAeiT0HB6yHBrdrxqKdsKeFiGZcFQtDip-JhQYpoBZpZpofnfNxqweW8bdwg0gwz-5wyEFL5A8IQk9c4aD4MdnjyEdmqL8fY5V0z3eJZjQPp4oIhxUHugF87xTzeDRBOCDkp21Syj0HJwAvWC2o-eCpglWdz9jLL87NWLXMFm9pMNuoz8u6bIYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوخترسانها از اسرائیل بلند شدند و کم کم صحنه برای اپرای امشب در حال شلوغ شدن است.
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14534" target="_blank">📅 19:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14533">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d83e2c9514.mp4?token=A4st7lS7r5VlmRVX_nfwBl0-6chg8Dgvd5jedaFG88e3Nw589Mcb9o1ndPb55mch6WuRLYn5Mwr5FmTnjo-CtbFEIZVsl8wMY838NfNWOeGKg1V3L_6vhl4n5hcID9bYqwqoLssaCYPELWGjMqTziXP60DJTBw_payNmWaQjd1RiNa6Yu-yGM0-7bcJypB-Q1xPnaBEzvrkSw7EXV5TyZ-KRHIkwfmcKgWXpZrjnAnsk8R_-lRYsIygHu02yg0IWPv7QA0NSFOaY0qCqdbwIyqRAoe37X9m1HjpxLbZmaZlPxzj4msmqLZc9q3ewwwAnpvwlSd1XNBbCiEubrbt8jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d83e2c9514.mp4?token=A4st7lS7r5VlmRVX_nfwBl0-6chg8Dgvd5jedaFG88e3Nw589Mcb9o1ndPb55mch6WuRLYn5Mwr5FmTnjo-CtbFEIZVsl8wMY838NfNWOeGKg1V3L_6vhl4n5hcID9bYqwqoLssaCYPELWGjMqTziXP60DJTBw_payNmWaQjd1RiNa6Yu-yGM0-7bcJypB-Q1xPnaBEzvrkSw7EXV5TyZ-KRHIkwfmcKgWXpZrjnAnsk8R_-lRYsIygHu02yg0IWPv7QA0NSFOaY0qCqdbwIyqRAoe37X9m1HjpxLbZmaZlPxzj4msmqLZc9q3ewwwAnpvwlSd1XNBbCiEubrbt8jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای امروز نشان می‌دهد که تأسیسات غنی‌سازی هسته‌ای نطنز ایران که در جریان بمباران امروز نیروهای آمریکایی مورد اصابت قرار گرفت، خسارات زیادی دیده است.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14533" target="_blank">📅 19:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14532">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خالیباف: استراتژی‌های اشتباه و تصمیمات بدون فکر، صحنه بازی را به شکلی فاجعه‌بار به نقطه صفر برمی‌گرداند؛ زیرساخت‌های انرژی و بازارها را به انفجار می‌کشاند و مردابی بی‌پایان پدید می‌آورد که سال‌ها در آن گرفتار خواهید شد.
ایرانی متفاوت خواهید دید!
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14532" target="_blank">📅 19:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14531">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش CNN: کابینه ترامپ تصرف جزیره خارک را به‌عنوان آخرین گزینهٔ بازی درنظر گرفته
پنتاگون در وضعیت قرنطینه امنیتی قرار گرفته
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14531" target="_blank">📅 18:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14530">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14530" target="_blank">📅 18:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14529">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8825907b11.mp4?token=sDlAkCbFcdTaOxUocZjvne5lboBJQLST5MPy0eOqO6dUHuXknbETNEfOLnvNS0eN5l59ThY_k9sy8JvcT7xbiEmy7j73_4xrs6l0yB4C5OVb3l2JgRESmgZxS_IcKEwz1rVQBiCsnsTa_P6xYKcWBJuzwSUyLcXVsbEdfpTcQ5B8ShkGmUfiqxgHjECVpRFAElMnud26xhhNq_llRt9o3rkCOXoocxI7itaNIKy0e0yEGJ3WAN4uWa_9L-cJMbwF-SW1u5eI1qbxmYCv0c4tP5H2s2WqmFAAycRBCuwX1zvYsakju2CLwU_MQH89a4DHBoaqDhkImdviGGrybb70IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8825907b11.mp4?token=sDlAkCbFcdTaOxUocZjvne5lboBJQLST5MPy0eOqO6dUHuXknbETNEfOLnvNS0eN5l59ThY_k9sy8JvcT7xbiEmy7j73_4xrs6l0yB4C5OVb3l2JgRESmgZxS_IcKEwz1rVQBiCsnsTa_P6xYKcWBJuzwSUyLcXVsbEdfpTcQ5B8ShkGmUfiqxgHjECVpRFAElMnud26xhhNq_llRt9o3rkCOXoocxI7itaNIKy0e0yEGJ3WAN4uWa_9L-cJMbwF-SW1u5eI1qbxmYCv0c4tP5H2s2WqmFAAycRBCuwX1zvYsakju2CLwU_MQH89a4DHBoaqDhkImdviGGrybb70IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کپشن با شما
🥴
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14529" target="_blank">📅 18:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14528">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سی‌ان‌ان: برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی میشد، به تعویق افتاده. این خبر رو یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتن.
مقامات به دونالد ترامپ گفتن که چنین عملیاتی احتمالاً به تعداد قابل توجهی نیروی زمینی نیاز داره و به طور بالقوه میتونه منجر به تلفات سنگین آمریکایی‌ها بشه.
پنتاگون و کاخ سفید هرگونه اقدام برای تصرف جزیره خارک رو به عنوان یک گزینه «پایان‌بازی» در نظر گرفتن، آخرین راه حلی که میتونه موازنه جنگ رو تغییر بده، اما با هزینه‌ای بالا.
نظامیان آمریکایی پیش از این حملات هوایی زیادی بر تأسیسات نظامی جزیره خارک انجام دادن، اما در این حملات عمداً از ضربه به زیرساخت انرژی این جزیره خودداری کردن.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14528" target="_blank">📅 18:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14527">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14527" target="_blank">📅 18:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14526">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14526" target="_blank">📅 18:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14525">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گزارش CNN: ایران در حالی که ارتش این کشور در حال انتقال محموله‌های موشکی است، سامانه‌های پدافند هوایی خود را در جزیره خارک نوسازی کرده است.
ایران همچنین در امتداد خط ساحلی جزیره خارک مین‌گذاری انجام داده است
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14525" target="_blank">📅 17:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14524">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">همکنون ایران با پهپادهای کامیکازه شروع به حمله به گروه‌های مخالف کرد ایرانی در در شمال عراق کرده است
🚨
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14524" target="_blank">📅 17:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14523">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی مجلس ایران در پاسخ به تهدیدات ترامپ: «او پاسخی حتی قوی‌تر و دردناک‌تر دریافت خواهد کرد»
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14523" target="_blank">📅 17:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14522">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0215ee2f80.mp4?token=lIDXn3_gGHsNfiOHqgaj85kZY4O0TQBUDGRaYUQVTCTnGTfr9RpX0pk-4bBahmGJ3CGbkv27T66i9rEQuSYolBTY2HzArZQXTHRT29CXq-CB5GtLMuqy85P3uosr--9OAnrA3e-5dypejgyVSgDh6FG-NAU_Z4vw9Hhr42pM9IBQIhNPdr421NJpOEBuqc3XcW-vuhtuxFVrLTUhtCX_ty9ktvRF_uMIcstwQ4Vr7oukSTBfvxn49rjuHipT5R09WL7Z8d1ZXNRmzoE5bVlwbPUHLnZTaSKpNCtE_jIoi5K2p00DWkO4uxK_TuozwgbEY8lz-0pvieWpprdeH25Sow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0215ee2f80.mp4?token=lIDXn3_gGHsNfiOHqgaj85kZY4O0TQBUDGRaYUQVTCTnGTfr9RpX0pk-4bBahmGJ3CGbkv27T66i9rEQuSYolBTY2HzArZQXTHRT29CXq-CB5GtLMuqy85P3uosr--9OAnrA3e-5dypejgyVSgDh6FG-NAU_Z4vw9Hhr42pM9IBQIhNPdr421NJpOEBuqc3XcW-vuhtuxFVrLTUhtCX_ty9ktvRF_uMIcstwQ4Vr7oukSTBfvxn49rjuHipT5R09WL7Z8d1ZXNRmzoE5bVlwbPUHLnZTaSKpNCtE_jIoi5K2p00DWkO4uxK_TuozwgbEY8lz-0pvieWpprdeH25Sow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ارسال سلاح به معترضان ایرانی از طریق کردها:
ما در واقع به آن‌ها سلاح فرستادیم و صادقانه بگویم از کردها بسیار ناامید شدیم. کردها ما را ناامید کردند.
من با این تصمیم مخالف بودم. می‌دانید، من می‌گفتم، «نه، باور ندارم که آن‌ها سلاح‌ها را تحویل دهند.
فکر می‌کنم آن‌ها سلاح‌ها را برای خود نگه داشتند. فکر می‌کنم این یک ننگ است. اما من این را به یاد خواهم سپرد، کردها. من این را به یاد خواهم سپرد.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14522" target="_blank">📅 17:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14521">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">لشکر ۸۲ هوابرد ملقب به تمام آمریکایی
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14521" target="_blank">📅 17:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14520">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ خطاب به مجری:
مثلاً شنیدم که به (زدن زیرساخت) آب اشاره کردی؛ قطع کردن آب واقعاً یک ضربه ویران‌کننده برای اوناست. من میتونم این کار رو تو یک دقیقه انجام بدم و سیستم آب اونارو قطع کنم اما مشکل اینجاس که مردم دیگه نمیتونن آب بنوشن. منظورم اینه که پس اونا باید چیکار کنن؟»
مجری:
«پیام شما به مردم ایران چیه؟ اونا الان به اینترنت دسترسی دارند.»
دونالد ترامپ:
«خب، پیام من به مردم ایران اینه که اونا ترسیدن. چون هیچ اسلحه‌ای ندارن و طرف مقابل اسلحه داره. اونا تجمع (تظاهرات) برگزار میکنن و به اونا شلیک میشه. اونا اون کشتی‌گیر و دو نفر از دوستانش رو دار زدن؛ باور کنید یا نه، اونارو با جرثقیل دار زدن؛ با خشونت تمام. اون یک کشتی‌گیر بسیار مطرح بود و اونا اونو اعدام کردن.»
«اونا حداقل ۴۰ تا ۵۰ هزار نفر رو کشتن و مردم ترسیدن. میدونی، وقتی یک مسلسل به سمت صورتت نشانه رفته باشه، یا وقتی چهار تک‌تیرانداز روی چهار ساختمان مختلف مستقر باشن و به سر مردم شلیک کنن، سخته که تجمع برگزار کنی؛ متوجهی؟»
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14520" target="_blank">📅 16:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14519">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/14519" target="_blank">📅 16:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14518">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14518" target="_blank">📅 16:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14517">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer"><a href="https://t.me/withyashar/14517" target="_blank">📅 16:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14516">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ: ایران بزودی به پایان می‌رسد، امشب هم بشدت بمباران خواهند شد!
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14516" target="_blank">📅 16:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14515">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ: مسئله ایران تمام شده است و ما می‌توانیم فردا نیروهایمان را بیاوریم، اما نمی‌خواهم نیروی زمینی اعزام کنم مطمئن نیستم
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14515" target="_blank">📅 16:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14514">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ: دیشب ۲۵۰ میلیون دلار بمب روی سرشان ریختیم
امشب وحشتناک حمله خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14514" target="_blank">📅 16:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14513">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ: ما برای معترضان ایرانی سلاح فرستادیم، اما از کردها بسیار ناامید شدیم زیرا آنها سلاح ها را به معترضان تحویل ندادند
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14513" target="_blank">📅 16:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14512">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ: ایرانی‌ها بسیار مغرور هستن حتی در مذاکرات، اما من دوست دارم همین الان با هم توافق کنیم.
اگر ایرانی ها توافق رو امضا نکنند، بشدت بمباران خواهند شد؛ عجله کنید، هنوز می‌توانیم به بزرگترین توافق تاریخ برسیم!
ما هواپیماهایمان را بر فراز قلب تهران به پرواز در می‌آوریم
تاکنون به اندازه کافی به ایران حمله نکرده‌ایم.
پل‌ها هدف بعدی حملات ما هستند! اما من نمی‌خواهم این کار را انجام دهم زیرا وقتی این کار را می‌کنم، مردم رنج می‌برند.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14512" target="_blank">📅 16:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14511">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رویترز: لشکر 82 هوابرد آمریکا ملقب به لشکر شیطان به‌زودی جزایر نفتی ایران رو تصرف خواهند کرد.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14511" target="_blank">📅 16:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14510">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ به فاکس نیوز:
ما در حال مذاکره با ایران هستیم
ترجیح می‌دهم جزیره خارک را در اختیار داشته باشم
ما هنوز به اندازه کافی به ایران ضربه نزده‌ایم
من از ایران ناامید نیستم، این توافق خوب است و ممکن است بزرگترین توافق تاریخ باشد
هواپیماهای ما بر فراز قلب تهران پرواز می‌کنند
ایران در تبلیغات خوب است اما در جنگیدن خوب نیست
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14510" target="_blank">📅 16:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14509">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا، اسکات بسنت:
«رژیم ایران در بازی با حاصل جمع صفر که واردش شده، بازنده خواهد بود.
هر خسارتی که ایران به متحدان ما در خلیج فارس وارد کند، از محل دارایی‌های ایران جبران خواهد شد.
هرگونه عوارض یا هزینه‌ای که برای عبور از تنگه خلیج فارس دریافت شود، با برداشت از حساب‌های ایران خنثی خواهد شد.
هر حمله‌ای که ایران انجام دهد، فقط پیامدهای اقتصادی و مالی سنگین‌تری برای این کشور به همراه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/14509" target="_blank">📅 16:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14508">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/14508" target="_blank">📅 16:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14507">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlirweza</strong></div>
<div class="tg-text">یاشار چرا شبا میزنه</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/14507" target="_blank">📅 16:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14506">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
اعلام جنگ دوباره ترامپ: امشب بدجور میزنیم و به زودی خارک را هم میگیریم.
@withyashar
اتاق جنگ با یاشار : امشب شامپاین هم میزارم رو میز‌ آماده
😁
🍾
🥂</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14506" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14505">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLIQSWSl-nbCpQ67qZrrN3lxGmbbky1Yt9cfNGTcbvp5bRIOwL2Hyk_SmqwJ6qSeE-dbNltZVVVM7wGHpv3RhyHGGsuSWA3xjCzziC-ytKLgoJsj4JNCOoX8lf-hwIRb5FL43_EhRRghQGoywMz4IpM7jz9WM-pgBrrM8envVMfgdHmZwepzVTBWKpizsv3T83Ui-eqbXcq-oRl6y5CbtRmkp39dQ7xqvHH6hv0UOJAJ2vmylXYSfX_O1Mc_-3a80yfeIY40qq3s7WE8Z2qZGP0ZAkK0Y_uRUna-7m9vZqLWGDQvIaBEi4q0lm_XN18xdXISWiuNN7c4w17TODHOaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :«ایالات متحده امشب ضربه‌ای بسیار سخت و سنگین به ایران وارد خواهد کرد؛ ایرانی که نیروی دریایی، نیروی هوایی، سامانه‌های راداری، پدافند هوایی و دیگر بخش‌های دفاعی آن، به همراه بخش عمده توان تهاجمی‌اش، از میان رفته‌اند!
در آینده‌ای نه‌چندان دور، ما جزیره خارک و دیگر مراکز زیرساختی نفتی را در اختیار خواهیم گرفت
و کنترل کامل بازارهای نفت و گاز آن‌ها را به دست خواهیم آورد؛ همان‌گونه که این کار را در ونزوئلا انجام داده‌ایم؛ اقدامی که برای هر دو کشور، یعنی ونزوئلا و ایالات متحده آمریکا، نتایج بسیار خوبی به همراه داشته است.
از توجه شما به این موضوع سپاسگزارم!
دونالد جی. ترامپ
رئیس‌جمهور ایالات متحده آمریکا»
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14505" target="_blank">📅 15:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14504">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb9c61bed.mp4?token=R3M2Y2csEYPV18NDP10If5co_7d4I5zpMsjp2_dOtxc4v_sFIHKUn6J38mwtuF9akrTg3knh7rT5iSXbmRmI3-OGZtaUan8lDRmsxv-AmYowS1bVSRQTR1rwWiT39Gb6W27H8r84gxoi0A7b54nsIEeWOIoYFBQQ485BvrwQkywAzOvm-ldPN4V5tF42DzaTzSJsBW9PggfjOEiRTYzkezdkQ7OvBLZHKAUoQeRVzG3aDKMUEq7UUHWwIIU0NdXOFV59_YeiE3zNzbGkIObzz9a36WhABKQKi4_4M1VDqCATUZMWH1Fdd3vlyKOcVb-ZyFFLSRamHPDabaNOcS5hfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb9c61bed.mp4?token=R3M2Y2csEYPV18NDP10If5co_7d4I5zpMsjp2_dOtxc4v_sFIHKUn6J38mwtuF9akrTg3knh7rT5iSXbmRmI3-OGZtaUan8lDRmsxv-AmYowS1bVSRQTR1rwWiT39Gb6W27H8r84gxoi0A7b54nsIEeWOIoYFBQQ485BvrwQkywAzOvm-ldPN4V5tF42DzaTzSJsBW9PggfjOEiRTYzkezdkQ7OvBLZHKAUoQeRVzG3aDKMUEq7UUHWwIIU0NdXOFV59_YeiE3zNzbGkIObzz9a36WhABKQKi4_4M1VDqCATUZMWH1Fdd3vlyKOcVb-ZyFFLSRamHPDabaNOcS5hfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیلگر ارشد جمهوری اسلامی آمریکا
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14504" target="_blank">📅 15:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14503">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سنتکام:نیروهای آمریکایی یک نفتکش را در خلیج عمان در ساعت ۱۱:۲۰ شب به وقت شرقی در ۱۰ ژوئن غیرفعال کردند، پس از آنکه این کشتی با تلاش برای حمل نفت ایران، تحریم علیه ایران را نقض کرد و این سومین کشتی تجاری است که این هفته توسط نیروهای آمریکایی غیرفعال شده است.
فرماندهی مرکزی ایالات متحده (centcom) علیه نفتکش m/t jalveer که پرچم گینه بیسائو را داشت و تلاش می‌کرد نفت را از ایران از طریق خلیج عمان حمل کند، اقدام کرد.
یک هواپیمای آمریکایی دو موشک هلفایر به اتاق موتور کشتی شلیک کرد پس از آنکه خدمه بارها از اطاعت دستورات نیروهای آمریکایی خودداری کردند.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14503" target="_blank">📅 15:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14502">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یک منبع دیپلماتیک ارشد به «الحدث» گفت:
پاکستان و قطر در ساعات گذشته تلاش‌های خود را برای پیشبرد توافق افزایش داده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14502" target="_blank">📅 15:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14501">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شنیده شدن چهار صدای انفجار از تنگه هرمز در قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14501" target="_blank">📅 14:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14500">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزیر دفاع بریتانیا، جان هیلی، استعفا داد و اعلام کرد که نخست‌وزیر کی‌یر استارمر و وزارت خزانه‌داری منابع لازم برای دفاع را در برابر تهدیدهای فزاینده تأمین نکرده‌اند.
او در نامه استعفای خود گفته است که «طرح سرمایه‌گذاری دفاعی» پیشنهادی «به‌طور قابل توجهی ناکافی است» و هشدار داده که این موضوع می‌تواند آمادگی نیروهای مسلح بریتانیا را کاهش داده و این کشور را «کمتر امن» کند.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14500" target="_blank">📅 14:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14499">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">صداوسیما: انفجار در سیریک گزارش شده
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14499" target="_blank">📅 14:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14498">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مسکو
:
آمریکا پیش از آنکه درخواست دسترسی بازرسان آژانس به تأسیسات هسته‌ای ایران را دنبال کند، باید تضمین دهد که به تهران هیچ حمله جدیدی نمی کند.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14498" target="_blank">📅 14:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14497">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وزارت خارجه کویت: حملات مکرر ایران نشان دهنده رویکردی سیستماتیک و تهاجمی است که کویت نه آن را می‌پذیرد و نه تحمل می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14497" target="_blank">📅 14:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14496">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تسنیم: ادعای رسیدن به متن نهایی برای تفاهم بین ایران و آمریکا خبرسازی است
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14496" target="_blank">📅 14:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14495">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ادعای رسانه بریتانیایی امواج:
پیش‌نویس توافق نهایی تهیه شده است.
متن آماده است. دیشب نهایی شد
اگر تا امروز به صورت نهایی تایید شود، به صورت رسمی اعلام می شود
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/14495" target="_blank">📅 12:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14494">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EH6VDqkVVjkH4ejHLQGuRbrc5Y1n_TOW8DCpbeOnzJSr7Fpl1-IjGrrbZh2mDuREhxhskZ1PpQXxKPjAQLbwLt9mVtFpfWx6soFujceSINoSsd0O4dxfzQ_fzrDEws9JnqCC_1MMjdHeokay7al2DZQuTT5MGtqgDUSH80wDeagOBiIxzsKBpxlw_DbnCDi6dU2Byc2uGTkBZMTh1iWCbsyAXPut94xNlqTBZMjmXmzkmW0U2206aVnckA4pkHkc8uU1EJZRBsO52XCa8mUH2egE58iNyGRw0RyX7810pEBbNqRtU3d3mA0JAebCVTAYygZfSsjFZF5P0AsITRy3_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران کوه ولنجک الان
@withyashar</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/14494" target="_blank">📅 12:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14493">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مهر: یک حملهٔ آمریکایی به یک کشتی باربری 150 تنی ایران، در خلیج عمان در اوایل امروز انجام شد، این کشتی حامل کالاهای ضروری را از خصب، عمان، به ایران حمل می‌کرد
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/14493" target="_blank">📅 12:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14492">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7YNnNGGh-3Xc345WbX465tMAgkBdxhKFyr6PjkkU-VUv40RlbfVNMZDDoKE-vtLcmuNW3jWFF0Sy7BKEPXlKQhwz7mW-VAsac8qX9ILY4LABRxI9tjNB9YxzQ7amee6ILBriAkGfEZIxpMCVIgUWtFrETSLjeO1HFcKfZnQB9ebPAn4j_mEFPfoE89qUwSuI62RAQXZ4y8tgY9hO4KmxGY_kjE4d7m8aYmU6fbJOOrkOhdVqEJCspp3SzHzU8QkIAfx19LEzSe-1Vi0SeHhf_Ev3oP1vmjTaEZK_iO3mbumg4zkkZ8LaC4tAuxq7rDgV3KWrNgcDRipQFIEvHE_Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه در خصوص نقض آتش‌بس توسط آمریکا
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/14492" target="_blank">📅 11:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14491">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ادعای سی‌ان‌ان: یک منبع دیپلماتیک می‌گوید مذاکرات آمریکا و ایران همچنان در مسیر خود ادامه دارد
یک منبع دیپلماتیک آگاه از موضوع گفت که مذاکرات برای دستیابی به توافق میان ایالات متحده و ایران، پس از گفت‌وگوهای شبانه، همچنان در مسیر خود قرار دارد.
این مذاکرات با وجود تبادل حملات میان آمریکا و ایران در طول شب ادامه یافت؛ حملاتی که تهدید می‌کردند تلاش‌های دیپلماتیک را با پیچیدگی و دشواری مواجه کنند.
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14491" target="_blank">📅 11:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14490">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ارتش اردن: سامانه‌های دفاع هوایی دیشب 20 موشک شلیک شده از ایران به منطقه ال-ازرق را رهگیری کردن
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14490" target="_blank">📅 11:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14489">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/217e03e668.mp4?token=Yt-hQTBX39-HkphqPYDZiCsetnpTYG6gDjljQqbClplLhyqXVq8F2GLz9M7J-WePmgCuzgM4-NY7UQL12ViYckbA-3YlGQv-wq2lfZDJ1SUhbSC8-Mb8L1_YW0dOfjihlWhuE8NY32jTdT9I8FFCXGbWF8G1x5Hf-TUVpY8_sjPfP3ynAI0Zs-VwRLaon2mR7Jk2HnN3jj-0FKiya9W8HEe5fMVeruKLxriyoq2CUyAv7UcOim6ueOiLMvo9e4-dyXUURywRXMU-FFyN9y8VzQJO5z-rNUOyrl8QJfMzLECrKkpyhgbQ3JGPZiClvqlDjyFc7jAflI7vI-uHwlBePA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/217e03e668.mp4?token=Yt-hQTBX39-HkphqPYDZiCsetnpTYG6gDjljQqbClplLhyqXVq8F2GLz9M7J-WePmgCuzgM4-NY7UQL12ViYckbA-3YlGQv-wq2lfZDJ1SUhbSC8-Mb8L1_YW0dOfjihlWhuE8NY32jTdT9I8FFCXGbWF8G1x5Hf-TUVpY8_sjPfP3ynAI0Zs-VwRLaon2mR7Jk2HnN3jj-0FKiya9W8HEe5fMVeruKLxriyoq2CUyAv7UcOim6ueOiLMvo9e4-dyXUURywRXMU-FFyN9y8VzQJO5z-rNUOyrl8QJfMzLECrKkpyhgbQ3JGPZiClvqlDjyFc7jAflI7vI-uHwlBePA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیندسی گراهام،درباره ایران:
اگه همین الان توافق نکنن، باید دست اسرائیل رو کاملاً باز بذاریم و خودمون هم از نیروی نظامی استفاده کنیم.
امیدوارم اتفاقات امشب باعث تغییر رفتار بشه.
اگه این فشارها باعث نشه که بیان پای میز مذاکره، باید استراتژی رو عوض کرد. باید با تمام قدرت وارد شد. کار رو یکسره کرد.
بعد از اینکه تکلیف ایران مشخص شد، به مرور زمان مردم ایران می‌تونن کشورشون رو پس بگیرن و مسیر صلح بین عربستان و اسرائیل هموار بشه.
همون افرادی که میگن زدن زیرساخت‌های ایران اشتباهه، باید بدونن که این‌ها اهداف نظامی مشروع محسوب میشن.
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/14489" target="_blank">📅 11:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14488">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وزیر دریانوردی هند: سه ملوان هندی دیروز در حمله ارتش آمریکا به یک نفتکش در‌ نزدیک تنگه هرمز کشته شدن
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/14488" target="_blank">📅 10:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14487">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دولت لبنان ممنوعیت کامل فعالیت‌های سپاه جمهوری اسلامی (IRGC) در داخل خاک لبنان را اعمال کرده است. به نیروهای امنیتی دستور داده شده است که هر عضو سپاه را که در آنجا فعالیت می‌کند، تعقیب، دستگیر و اخراج کنن
@withyashar</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/14487" target="_blank">📅 10:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14486">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا:
«اگر ایران توافقی که ما می‌خواهیم را امضا نکند،امشب نیز اهداف نظامی آنها را بمباران می‌کنیم»
@withyashar</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/14486" target="_blank">📅 10:53 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
