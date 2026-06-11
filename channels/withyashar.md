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
<p>@withyashar • 👥 320K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 15:23:01</div>
<hr>

<div class="tg-post" id="msg-14503">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سنتکام:نیروهای آمریکایی یک نفتکش را در خلیج عمان در ساعت ۱۱:۲۰ شب به وقت شرقی در ۱۰ ژوئن غیرفعال کردند، پس از آنکه این کشتی با تلاش برای حمل نفت ایران، تحریم علیه ایران را نقض کرد و این سومین کشتی تجاری است که این هفته توسط نیروهای آمریکایی غیرفعال شده است.
فرماندهی مرکزی ایالات متحده (centcom) علیه نفتکش m/t jalveer که پرچم گینه بیسائو را داشت و تلاش می‌کرد نفت را از ایران از طریق خلیج عمان حمل کند، اقدام کرد.
یک هواپیمای آمریکایی دو موشک هلفایر به اتاق موتور کشتی شلیک کرد پس از آنکه خدمه بارها از اطاعت دستورات نیروهای آمریکایی خودداری کردند.
@withyashar</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/withyashar/14503" target="_blank">📅 15:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14502">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یک منبع دیپلماتیک ارشد به «الحدث» گفت:
پاکستان و قطر در ساعات گذشته تلاش‌های خود را برای پیشبرد توافق افزایش داده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/withyashar/14502" target="_blank">📅 15:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14501">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شنیده شدن چهار صدای انفجار از تنگه هرمز در قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/withyashar/14501" target="_blank">📅 14:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14500">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وزیر دفاع بریتانیا، جان هیلی، استعفا داد و اعلام کرد که نخست‌وزیر کی‌یر استارمر و وزارت خزانه‌داری منابع لازم برای دفاع را در برابر تهدیدهای فزاینده تأمین نکرده‌اند.
او در نامه استعفای خود گفته است که «طرح سرمایه‌گذاری دفاعی» پیشنهادی «به‌طور قابل توجهی ناکافی است» و هشدار داده که این موضوع می‌تواند آمادگی نیروهای مسلح بریتانیا را کاهش داده و این کشور را «کمتر امن» کند.
@withyashar</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/withyashar/14500" target="_blank">📅 14:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14499">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">صداوسیما: انفجار در سیریک گزارش شده
@withyashar</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/14499" target="_blank">📅 14:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14498">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مسکو
:
آمریکا پیش از آنکه درخواست دسترسی بازرسان آژانس به تأسیسات هسته‌ای ایران را دنبال کند، باید تضمین دهد که به تهران هیچ حمله جدیدی نمی کند.
@withyashar</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/withyashar/14498" target="_blank">📅 14:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14497">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزارت خارجه کویت: حملات مکرر ایران نشان دهنده رویکردی سیستماتیک و تهاجمی است که کویت نه آن را می‌پذیرد و نه تحمل می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/14497" target="_blank">📅 14:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14496">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تسنیم: ادعای رسیدن به متن نهایی برای تفاهم بین ایران و آمریکا خبرسازی است
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/14496" target="_blank">📅 14:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14495">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ادعای رسانه بریتانیایی امواج:
پیش‌نویس توافق نهایی تهیه شده است.
متن آماده است. دیشب نهایی شد
اگر تا امروز به صورت نهایی تایید شود، به صورت رسمی اعلام می شود
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/14495" target="_blank">📅 12:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14494">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZR_fl7jpDIVXJSRj2KYtirQBNNVhpaT7j9WrR1dUrjqk3pN7aEbeG5S-XoBAcIPGF-q8GsH4EJskDkj66iXGCGN7DyrCUH2SjnVV6EEKblQDDAyR66uvk10bh-2C5n2ZKCHtNW5jrFhPs4-y6H5OFHuBCZJGQf1UM0YxbcGRtlcwQwJVDZBODjEYmRqaJIJJOH7iRcF8FmTouCbRTxpFxv4DSAXhCysGSjMtfJP9Kqup5JNHDuHdo1KPjDjykQPBaAUCWR2Q0xCFpBPBxaDTxlxd_TL1IKi9BSkl-KV0UQfSteQ50ZdEbiII-JSz_cqGhlbWhx73IZa0_zd84_wvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران کوه ولنجک الان
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14494" target="_blank">📅 12:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14493">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مهر: یک حملهٔ آمریکایی به یک کشتی باربری 150 تنی ایران، در خلیج عمان در اوایل امروز انجام شد، این کشتی حامل کالاهای ضروری را از خصب، عمان، به ایران حمل می‌کرد
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/14493" target="_blank">📅 12:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14492">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcTkB4CuYs-LnJ_fKfXZIBPF_Vx9QBhMUFfSBK30Tgf6Am0VgfDLCl1Nk-NcNZpKUQwIhIPCdfPw0hWcC4wsvzpmU7Lr-0xGnBpZ26JFvVFmci6LRLJ23oQN1KugG_Ho3NCL1HfY8x7vBKQBKWE8xv3F0PRQf5kPuvlwNRCzF1XzFuhXVNEbedX3je8ZHl1Mt6U7Ou0H0WcHhG4U5qH3PBIzXxLEI-08m7BCTID_7o9gyF2O2JrZqJ1g9tsGIQezT3B1fqOf6jBkd-dPIwRzBpPicUmMnO48tbP_L2SXMQBqQUFT8luclI8NGGkQdp0pPJXWILowv--ztQUIWM_slA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه در خصوص نقض آتش‌بس توسط آمریکا
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14492" target="_blank">📅 11:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14491">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ادعای سی‌ان‌ان: یک منبع دیپلماتیک می‌گوید مذاکرات آمریکا و ایران همچنان در مسیر خود ادامه دارد
یک منبع دیپلماتیک آگاه از موضوع گفت که مذاکرات برای دستیابی به توافق میان ایالات متحده و ایران، پس از گفت‌وگوهای شبانه، همچنان در مسیر خود قرار دارد.
این مذاکرات با وجود تبادل حملات میان آمریکا و ایران در طول شب ادامه یافت؛ حملاتی که تهدید می‌کردند تلاش‌های دیپلماتیک را با پیچیدگی و دشواری مواجه کنند.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14491" target="_blank">📅 11:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14490">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ارتش اردن: سامانه‌های دفاع هوایی دیشب 20 موشک شلیک شده از ایران به منطقه ال-ازرق را رهگیری کردن
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14490" target="_blank">📅 11:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14489">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/217e03e668.mp4?token=CTPpm9X-GH7OBAaGxsjPBLjyJXK1UNR3KqJQKRsAqcYTM0ULGFI7HlnAWJ-WfjMdUUpZgdcPMaZCUyDwGpA5QTdibGMXqph2nOpfze8EBd7fuBivug-WJ22Du0lAnCUscz_Ka-4R_NfiNaZFxLxYSrPShNPxzd_alAWb5PODLPdXCpNeW2xmJW0GkrCx18wPTZituFAvQFySS3VMi6WFPM_hsjVIHY6odXmvXv8AZsK153SnRa4yjs1YJEBQpLYgMn5ozeEfeCkej49N-u8ojIBj7dDUw15Abr5gtmiafEgRYhtM6mJKbcmWh7-Ygz4VogQPdzGcAihsbT2zZRPlPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/217e03e668.mp4?token=CTPpm9X-GH7OBAaGxsjPBLjyJXK1UNR3KqJQKRsAqcYTM0ULGFI7HlnAWJ-WfjMdUUpZgdcPMaZCUyDwGpA5QTdibGMXqph2nOpfze8EBd7fuBivug-WJ22Du0lAnCUscz_Ka-4R_NfiNaZFxLxYSrPShNPxzd_alAWb5PODLPdXCpNeW2xmJW0GkrCx18wPTZituFAvQFySS3VMi6WFPM_hsjVIHY6odXmvXv8AZsK153SnRa4yjs1YJEBQpLYgMn5ozeEfeCkej49N-u8ojIBj7dDUw15Abr5gtmiafEgRYhtM6mJKbcmWh7-Ygz4VogQPdzGcAihsbT2zZRPlPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیندسی گراهام،درباره ایران:
اگه همین الان توافق نکنن، باید دست اسرائیل رو کاملاً باز بذاریم و خودمون هم از نیروی نظامی استفاده کنیم.
امیدوارم اتفاقات امشب باعث تغییر رفتار بشه.
اگه این فشارها باعث نشه که بیان پای میز مذاکره، باید استراتژی رو عوض کرد. باید با تمام قدرت وارد شد. کار رو یکسره کرد.
بعد از اینکه تکلیف ایران مشخص شد، به مرور زمان مردم ایران می‌تونن کشورشون رو پس بگیرن و مسیر صلح بین عربستان و اسرائیل هموار بشه.
همون افرادی که میگن زدن زیرساخت‌های ایران اشتباهه، باید بدونن که این‌ها اهداف نظامی مشروع محسوب میشن.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14489" target="_blank">📅 11:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14488">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزیر دریانوردی هند: سه ملوان هندی دیروز در حمله ارتش آمریکا به یک نفتکش در‌ نزدیک تنگه هرمز کشته شدن
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14488" target="_blank">📅 10:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14487">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دولت لبنان ممنوعیت کامل فعالیت‌های سپاه جمهوری اسلامی (IRGC) در داخل خاک لبنان را اعمال کرده است. به نیروهای امنیتی دستور داده شده است که هر عضو سپاه را که در آنجا فعالیت می‌کند، تعقیب، دستگیر و اخراج کنن
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14487" target="_blank">📅 10:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14486">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا:
«اگر ایران توافقی که ما می‌خواهیم را امضا نکند،امشب نیز اهداف نظامی آنها را بمباران می‌کنیم»
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14486" target="_blank">📅 10:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14485">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گاردین: ترامپ از کنگره درخواست کرده هرچه زودتر با اختصاص 350 میلیارد دلار بودجه جدید برای تقویت ارتش آمریکا موافقت کنن.
ترامپ گفته با توجه به شرایط فعلی، آمریکا باید سریع‌تر توان نظامی خودشو افزایش بده و این بودجه بدون درنگ تصویب بشه. کارشناسا معقتدن ممکنه این بودجه رو برای حمله زمینی به ایران بخواد که انقدر عجله داره.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14485" target="_blank">📅 10:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14484">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سنتکام: نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) حملات دفاع شخصی بیشتری را علیه اهداف متعدد در ایران در 10 ژوئن به دستور فرمانده کل انجام دادند.
نیروهای سنتکام حملاتی را به قابلیت‌های نظارتی نظامی، سیستم‌های ارتباطی و سایت‌های دفاع هوایی ایران در سراسر ایران انجام دادند. نیروهای تفنگداران دریایی، نیروی هوایی و نیروی دریایی ایالات متحده، مهمات دقیقی را به سمت اهداف ایرانی شلیک کردند که تهدیدی برای نیروهای آمریکایی و کشتی های تجاری بین المللی در حال عبور از آب های منطقه بود.
این حملات در پاسخ به تجاوزات بی مورد و ادامه دار ایران است. نیروهای آمریکایی هوشیار، کشنده و آماده هستند.
@withyashar</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/14484" target="_blank">📅 04:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14483">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer"><a href="https://t.me/withyashar/14483" target="_blank">📅 04:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14482">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">صداوسیما: انفجارهای مهیب در اطراف استان البرز، هشتگرد و نظرآباد در کرج.
@withyashar</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/14482" target="_blank">📅 04:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14481">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoW4zZi0TCOvBtIpEKGBPS0web6sj76x3llfFaM4ia-zmqvq0zJDmDTI1WSibvxefpgXL0v80HfXB87sIeU3dzntCuTzs4cfT-sxFqMC1404zksgGFEsFduYLi0xioVScSobyxq0lfN7pAT2uMiIvVwFzB7Zm0TAFIOW-ZEIarqQQ-lCbbEF_DTRzOfgixgNvRICmkz6lX0Cp2jYi5HX59JvndMojafk18KBu8ANKP2l957VRy90_bhma_o8Vsf6SJJO904QsIa6E7wwZmwHrxfYr58eQbAdJEchrPgWO6EMG_hlxl7V91I5IaPPsXS2w8pRoOYqI8218WxKVTF5Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرج
@withyashar</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/14481" target="_blank">📅 04:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14480">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/14480" target="_blank">📅 04:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14477">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llDQyiLPvF4UEsXYUKzUWc7AXonimWsRwadg9clNz1YOGD2zFYrWeicmOyCOzrGUqPaXLJe8MFfsceUzshuCER2cN985irT5OrQz77k4KShCR5tjG3KSfY9DG6i6-XCRPC__TmzNFONtyjqA-EBOh8-HfmbTZMRGj30ynLxVgkk07tYtqKmdBf1OnEBvHKSx4p_jNmLiJgRMTdoXCvlEXFDIZjUH7iNjUqGFnqWmu8W8R-L9zjKyjgTeC5ziZYbspUCLifIvxl3Yx08oTq4Td7IQwAWbld2JYHQWEBvYzCgw3qlmR6SK0FjYqtQ_G_H_1Rl4wTYPK9UYJqUCy3gouA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fglfRbyCcoGHwtGch0o8gKMJ_wuVqhv0VtxJH39twf1QldAiTnqP5u8p7RphF-TTYBz20xOSPdTUDt9w98JaEOEno996IniRdsyXRsxYypLUoj830af7g35w0Uld-xXsuwmhiOmM3RPEwPTL2y54Drv_l1-bmZ5yitCE91uLnKfPPIetu2fOZqp_UaelwoTpMWJcmQKBpxGxEAe3eDWrx5bHnBxlErrjvr9Tgqfpi1ECrKjNyNHYv7TqEkpIGezbv4cCC3acqPvYFtKZHeszuTciR1V3C10r6vlYX786Ik-GNuKiFbQRPwEiAMisCSz_bzbGkwbWDIBya7UHfHDwPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jwSp36vrY6DvZpYfyQxZYtqQMcJWdM1Ls7LNxZfq8OPzlEpvVe-PV9vSihQyyuqQijdO5EYlb7IwEfCy24uqeO5XsNfF2z9jxJY_DlTwRdqodKEGPaGSavIuFUBnptO0W-c125Ahevh-vKpDUB6mAQkPka0DdzhAXz_m9XFrndHQX4I-foO0NfgR_ULCbGQ-otFtKMWuYdy-rgvrIIYNdAOqmHnl19dPRh97SfqZPcrI_7xdfryWaiVOGXTgKpWnjSvysme1yrAJD2DgEjAsdMDV1YWXQ9inSJR7thPLFBxMDOkmY8Q9slYdu8kqP0lfED7jMRwses_R4uTT1YKjDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کرج
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/14477" target="_blank">📅 04:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14476">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBLHzcMiz4Lvu9wlRyQ_HAYwFV0CVkBDcuo4h8xjihLy-3sMUIVGeJjtleXLqrGjRMwLTyF8GF7N1ikV8wPPLJo1EWCe7TaYyaOswLK8lnGFdiWx9vKHdFcljeMeBM9023YNlIIzdOxhreV0um-SjWUEKT42enJJ106xk4y0NvWwP82JjglZ5Ad1dtE08GO6C2Aym03zeA3d8ZEVxlpe2iHhuvNtj2y5P83JmqnahxCrdhA4Kf7_gSNCOX-lbBmE6o9VMI1r__z0TTjn20Brd2PN0gIASdoURsV1H0bjKNhZrKMkbHrCLec6yBC5kbzLonQ77S0i7osrlxpQQFZ9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان کرج
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/14476" target="_blank">📅 04:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14475">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کرج انفجار پشت انفجار
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14475" target="_blank">📅 04:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14474">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شنیده‌شدن آژیر هشدار و انفجار در بحرین
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/14474" target="_blank">📅 04:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14473">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هم اکنون موج حملات ۳پا به بحرین
🚨
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14473" target="_blank">📅 04:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14472">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">امیدوارم کرج هدفمند باشه
🥹
✌🏾
💥
همه انرژی بدیدددددد</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14472" target="_blank">📅 04:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14471">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مهر: انفجار در اشتهارد و آبیک
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14471" target="_blank">📅 03:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14470">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">صدای انفجار در فردیس و کمالشهر کرج
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14470" target="_blank">📅 03:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14469">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14469" target="_blank">📅 03:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14468">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">چندین انفجار شدید در کرج
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14468" target="_blank">📅 03:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14467">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا:
توقف حملات آمریکا به مناطقی تو جنوب ایران بنا بر اعلام ترامپ، به دلیل پاسخ قدرتمند و کوبنده نیروهای مسلح جمهوری اسلامی ایرانه که تو این رابطه شکست دیگری بر ارتش آن کشور تحمیل گردید. پاسخ نیروهای مسلح به تجاوز و شرارت های آمریکا ادامه داره.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14467" target="_blank">📅 03:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14466">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">روابط عمومی ۳پا بعد از مصرف:
رزمندگان شجاع نیروی هوافضا و قهرمانان نیروی دریایی سپاه سحرگاه امروز در تنبیه متجاوز و پاسخ به تعرض ارتش کودک کش آمریکا به بعضی از واحدهای خدماتی و پاسگاه های ساحلی سپاه و فرماندهی انتظامی و محوط فرودگاه بندرعباس طی دو موج عملیاتی هجده هدف مهم متعلق به ارتش شرور امریکا در پایگاه های هوایی علی السالم و احمدالجابر و همچنین پایگاه های هوایی شیخ عیسی را مورد اصابت قرار داده و منهدم کردند
@withyashar
🥴</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14466" target="_blank">📅 03:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14465">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087dd6e032.mp4?token=ukEq-LD6se5ICcYr3qWugACeSMZ0L-IoAIvaIy9z6XQa4Q87LWs6HuYGlB4zeiGpoWO0B0vpCycM-0isRx_nJFuMIlDyp3VV1N49MoTKJAimpM8oEVeVeh2fPbSfANP3fOo2amABK8UXoQBTDVXup1Dvqn6C4mXQIuHQzt4WZl7cks2pbF3_O_CydKEUY9gWihRDEaL3sX4neeerNBkeOg6oklDvF9pEA-jZV-J0uGF-oYLj1EEZOFYEjdmTViTAiDCI6i53FDTJgmQd9hUvEdgYDzP2f37i_LPuThz2x5tL8IQ4gtihRZWWF2G4M8g0A3Sbsc1C0A8fNG54Mws0Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087dd6e032.mp4?token=ukEq-LD6se5ICcYr3qWugACeSMZ0L-IoAIvaIy9z6XQa4Q87LWs6HuYGlB4zeiGpoWO0B0vpCycM-0isRx_nJFuMIlDyp3VV1N49MoTKJAimpM8oEVeVeh2fPbSfANP3fOo2amABK8UXoQBTDVXup1Dvqn6C4mXQIuHQzt4WZl7cks2pbF3_O_CydKEUY9gWihRDEaL3sX4neeerNBkeOg6oklDvF9pEA-jZV-J0uGF-oYLj1EEZOFYEjdmTViTAiDCI6i53FDTJgmQd9hUvEdgYDzP2f37i_LPuThz2x5tL8IQ4gtihRZWWF2G4M8g0A3Sbsc1C0A8fNG54Mws0Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دست پخت بی بی قالینیاهو
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14465" target="_blank">📅 03:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14464">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ : این آتش بس، بیشترین آتش‌بسِ نقض‌شده تو تاریخ جهان بود. @withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14464" target="_blank">📅 03:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14463">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ :
این آتش بس، بیشترین آتش‌بسِ نقض‌شده تو تاریخ جهان بود.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14463" target="_blank">📅 03:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14462">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سنتکام : رسانه ی جمهوری اسلامی درباره هدف قرار دادن کشی آمریکایی هم کذبه و هیچ کشتی هدف قرار نگرفته.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14462" target="_blank">📅 03:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14461">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سنتکام:  ادعای سپاه پاسداران مبنی بر بستن تنگه هرمز کذب است!
حقیقت: کشتی‌های تجاری امشب به عبور و مرور در تنگه هرمز ادامه می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14461" target="_blank">📅 03:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14460">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ: حملات امشب به پایان رسیده.
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14460" target="_blank">📅 03:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14459">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ: نیروهای آمریکایی ۴۹ موشک تاماهاوک به سمت ایران شلیک کردند
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14459" target="_blank">📅 02:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14458">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ: اگر ایران توافقنامه رو امضا نکنه، فرداشب به بمباران آنها برمیگردیم.
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14458" target="_blank">📅 02:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14457">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e874ef24.mp4?token=TO017t1_sdyIYiXSjX5w_pwYltmrmB6cd-b0_0rEht-HeUtWDIkUBU6uugxc40QNw8U3FlUyg4TzDC4OxxNM7ljDyjrIyX7zK7YbB_qsdDmyBD5jyKca5ar1kiWv8hnCRCcGNhc1Hew8JuA0gmqzfrvgIZfDvd-rTs60OGhcOaV4RBxKfyDPE0rj1SLmNlRPfOvSfHcVdE1JlPdU57tz9vyTh21h2e6daN4g7fjz9DpSkuiYYJ1sWTrgicG3VsYSF0bg-Kv5eVaGWJIALq6yyca60RgeCcZPYe3FG_p8uqC1jM431fVFFeAr6WY3xJpYBoLHxYTeg7EAPOrGbdzbLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e874ef24.mp4?token=TO017t1_sdyIYiXSjX5w_pwYltmrmB6cd-b0_0rEht-HeUtWDIkUBU6uugxc40QNw8U3FlUyg4TzDC4OxxNM7ljDyjrIyX7zK7YbB_qsdDmyBD5jyKca5ar1kiWv8hnCRCcGNhc1Hew8JuA0gmqzfrvgIZfDvd-rTs60OGhcOaV4RBxKfyDPE0rj1SLmNlRPfOvSfHcVdE1JlPdU57tz9vyTh21h2e6daN4g7fjz9DpSkuiYYJ1sWTrgicG3VsYSF0bg-Kv5eVaGWJIALq6yyca60RgeCcZPYe3FG_p8uqC1jM431fVFFeAr6WY3xJpYBoLHxYTeg7EAPOrGbdzbLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14457" target="_blank">📅 02:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14456">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ به فاکس : ایرانی‌ها ازم خواستن بمباران رو متوقف کنم
مستقیم با مقام‌های ایرانی صحبت کردم
جنگنده‌های آمریکا در حال پرواز روی آسمون ایران هستن
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14456" target="_blank">📅 02:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14455">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ: بمباران به زودی تموم میشه!
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14455" target="_blank">📅 02:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14454">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پاکستان:  به آمریکا اعلام کردیم که دیگر دست از تلاش برای میانجیگری برمی‌داریم
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/14454" target="_blank">📅 02:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14453">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/14453" target="_blank">📅 02:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14452">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">هوافضای ۳پا: پاسداران برای یک عملیات تاریخی آماده شده اند!
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14452" target="_blank">📅 02:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14451">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14451" target="_blank">📅 02:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14450">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14450" target="_blank">📅 02:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14449">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارشات اولیه از حملات هواپیمای جنگی A-10 آمریکا به قایق های تندرو سپاه در جزیره لارک
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14449" target="_blank">📅 02:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14448">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Remix Az Asemoon Dare Miad Ye Daste Hoori ~ Otaghe jang</div>
  <div class="tg-doc-extra">Yashar</div>
</div>
<a href="https://t.me/withyashar/14448" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
@withyashar
📱
https://instagram.com/yashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14448" target="_blank">📅 02:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14447">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مقامات آمریکایی به وال استریت ژورنال گفتند که ترامپ دیپلماسی با ایران را رها نکرده است، اگرچه صبر او به طور فزاینده‌ای کاهش یافته است.
حتی پس از تأیید حملات جدید در اوایل این هفته، ترامپ به دستیارانش دستور داد پیامی را از طریق واسطه‌های قطری به تهران منتقل کنند که این حملات پاسخی به حادثه پهپاد است که تقریباً خدمه آپاچی را کشت، نه آغاز جنگ تمام‌عیار.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14447" target="_blank">📅 02:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14446">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قرارگاه خاتم الانبیا: تنگه هرمز از این لحظه برای تمام شناور ها بسته اعلام میشه و هیچ شناوری حق عبور نداره
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14446" target="_blank">📅 02:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14445">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وزیر خارجه یمن: نسبت به ادامه تجاوز آمریکا به ایران هشدار می‌دهیم
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14445" target="_blank">📅 02:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14444">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نیروی هوافضای ۳پا: آغاز مرحله پاسخ قاطع و بازدارنده مستقیم به دشمن را اعلام می‌کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14444" target="_blank">📅 02:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14443">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شبکه ۱۵ اسرائیل : موج اول حملات به ایران؛ به پایان رسیده
@withyashar
یاشار : درگیری همچنان در تنگه هرمز ادامه دارد.</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14443" target="_blank">📅 02:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14442">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">روابط عمومی ۳پا: درپی تجاوز جنگنده f16 به حریم هوایی خلیج فارس و شلیک موشک سامانه پدافند هوایی سپاه به سمت آن، جنگنده متجاوز متواری گشت
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14442" target="_blank">📅 02:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14441">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هاآرتص: اسرائیل در انتظار حمله موشکی ایران پس از حملات جدید آمریکا به اهدافی در ایران
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14441" target="_blank">📅 02:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14440">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ : به توافق نزدیک بودیم اما ورق کاملا برگشت و ایران منتظر حملات سنگین و شدیدتر از دو سه ماه اخیر باشد
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14440" target="_blank">📅 02:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14439">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فاکس نیوز : اهداف بعدی ترامپ پل‌ها و نیروگاه‌ها هستن!
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/14439" target="_blank">📅 01:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14438">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رسانه عراقی «صابرین‌نیوز» گزارش داد که کشتی‌های آمریکایی در نزدیکی تنگه هرمز هدف حملات موشکی و پهپادی نیروهای مسلح ایران قرار گرفته‌اند. @withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14438" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14437">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رسانه عراقی «صابرین‌نیوز» گزارش داد که کشتی‌های آمریکایی در نزدیکی تنگه هرمز هدف حملات موشکی و پهپادی نیروهای مسلح ایران قرار گرفته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14437" target="_blank">📅 01:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14436">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خبرنگار I24News  :  عوامل آمریکایی: مراکز فرماندهی و کنترل، انبارهای مهمات، رادارها و واحدهای پهپادی مورد حمله قرار گرفتند
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14436" target="_blank">📅 01:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14435">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">المیادین: منطقه تنگه هرمز شاهد درگیری شدیده.
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14435" target="_blank">📅 01:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14434">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کان عبری: اسرائیل نقشی در حملات امشب نداشته است
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14434" target="_blank">📅 01:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14433">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پیشروی ناو های آمریکایی اکنون در فاصله 150 تا 250 کیلومتری از ساحل چابهار هستند.
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/14433" target="_blank">📅 01:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14432">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پرواز سوخت رسان های بیشتر از بن گوریون رصد شد. سوخت رسان اسرائیل به پرواز در آمد.
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14432" target="_blank">📅 01:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14431">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آکسیوس:مذاکرات ایران و آمریکا فروپاشید
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14431" target="_blank">📅 01:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14430">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجار ‌جدید قشم
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14430" target="_blank">📅 01:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14429">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فاکس نیوز به‌نقل از یک مقام: امشب چند مرحله حمله انجام میدیم.
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14429" target="_blank">📅 01:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14428">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش از برخورد موشک به فرودگاه بندرعباس
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14428" target="_blank">📅 01:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14427">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مهر: یه موشک کروز در عسلویه رهگیری کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14427" target="_blank">📅 01:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14426">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اتاق جنگ با یاشار : مشخصه که هدف امریکا متمرکز در‌ باز کردن تنگه هرمز است در مرحله اول !
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14426" target="_blank">📅 01:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14425">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">منابع عراقی: پایگاه آمریکایی الحریر در اربیل (شمال عراق) هدف موشکی از ایران قرار گرفت.
وبگاه المعلومه عراق نیز خبر داد، ایران یک رادار آمریکایی در اربیل (مرکز کردستان عراق) را منهدم کرد
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14425" target="_blank">📅 01:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14424">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مهر : همین الان سپاه با نیرودریایی امریکا درگیر شده تو تنگه
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14424" target="_blank">📅 01:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14423">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e48872fd.mp4?token=YNaiBHhbhfzdYj2AniNCnZ9O80Fpwr9Kz2eykszIn4kluuf_3ikxuFiKGwBkd6VhA2joM6M4kk8rHzG4Z5K1BfFWERMvsRTl95zEtxQYYtQJnh9_9iwh8Xo7ZfgmlkhBmNJRdeBIdJuT5aPhcZgPF9JjJaRdxBpXKVPAJzRHlExbW4P-aOFjyMrbGrBymcXZB2Mb8ODH-q43ACne_INoY_vBQoXZmy0FQWM4MDRaRhAUF22mjF2JM6RWSOKYBIEJfdHuPau5N_gg-a_OzV-TbYHtbOP0ggH1W0XdNzFDAtjlwH1DTsS1utmYQm3KZMIoLMGyzLiSZ4f_SzFe1QeOYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e48872fd.mp4?token=YNaiBHhbhfzdYj2AniNCnZ9O80Fpwr9Kz2eykszIn4kluuf_3ikxuFiKGwBkd6VhA2joM6M4kk8rHzG4Z5K1BfFWERMvsRTl95zEtxQYYtQJnh9_9iwh8Xo7ZfgmlkhBmNJRdeBIdJuT5aPhcZgPF9JjJaRdxBpXKVPAJzRHlExbW4P-aOFjyMrbGrBymcXZB2Mb8ODH-q43ACne_INoY_vBQoXZmy0FQWM4MDRaRhAUF22mjF2JM6RWSOKYBIEJfdHuPau5N_gg-a_OzV-TbYHtbOP0ggH1W0XdNzFDAtjlwH1DTsS1utmYQm3KZMIoLMGyzLiSZ4f_SzFe1QeOYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14423" target="_blank">📅 01:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14422">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تا دقایقی دیگر پیام سخنگوی قرارگاه مرکزی خاتم الانبیا(میلاد مدرسه ای)
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14422" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14421">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یک مقام آمریکایی به Axios گفت: تمام اهدافی که مورد حمله قرار گرفتند در جنوب ایران هستند و شامل سامانه‌های پدافند هوایی، رادارها و واحدهای فرماندهی و کنترل پهپادها می‌شوند.
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14421" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14420">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پدافند سیرجان فعال
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14420" target="_blank">📅 01:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14419">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">صدای انفجار در کنگان
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14419" target="_blank">📅 01:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14418">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الجزیره: اسرائیل هم امشب به ایران حمله کرده و تو عملیات حضور داره
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/14418" target="_blank">📅 01:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14417">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14417" target="_blank">📅 01:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14416">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114223d040.mp4?token=B2xfENx33_nPbwiykrbbAknMHFAvHl29zEVO7sNrnF9Sit_fFH6W1kmkJB4u0GGG7VPf0Nl1pZDDlAKPmWUOODAtCfrxBM2AekIz03yabZ61m7T9ruPjewHTDhIupgn5RqxJtwZmeb_L06UiLL-jCx2qLyqMGZGMClNQkJ1xUlWXihGXHnmuja27E2fbkkaJP-uKMXJiPs56StW3wVYT-qSAI_rp2SSaoqMP4fbMFDb7Tvt3PGMBTeMjX106mdF6KN81IQMFzBY2iDgGHZixZozOtbJkKqVZOSXV0r9o7bXpBmb1MWyElieBgAhWq52SZ3jtfr-6_CqBkV5AFGISCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114223d040.mp4?token=B2xfENx33_nPbwiykrbbAknMHFAvHl29zEVO7sNrnF9Sit_fFH6W1kmkJB4u0GGG7VPf0Nl1pZDDlAKPmWUOODAtCfrxBM2AekIz03yabZ61m7T9ruPjewHTDhIupgn5RqxJtwZmeb_L06UiLL-jCx2qLyqMGZGMClNQkJ1xUlWXihGXHnmuja27E2fbkkaJP-uKMXJiPs56StW3wVYT-qSAI_rp2SSaoqMP4fbMFDb7Tvt3PGMBTeMjX106mdF6KN81IQMFzBY2iDgGHZixZozOtbJkKqVZOSXV0r9o7bXpBmb1MWyElieBgAhWq52SZ3jtfr-6_CqBkV5AFGISCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/14416" target="_blank">📅 01:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14415">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a8425054.mp4?token=cNyI7yLMAZ00izFEAzvQRbfytKJmUR3ukBT5qhbV_Cel_zgIaVa5hr3601C06E9JpuVBwWfROuZX5bqv4JOLSY05sC-S3RZhiPor2-kVsQou3w1FATq0hre7YsSMRgD0GIlXQW_WJb-sCNWt5sgXH25bxHVEILqbHlXZ4sMCqv-UNWTVOLwMQpHiVshR_09qxHcU7x7-68BZ8k3GkR0XEN0TR2EYCOCLHBVHqYnu4yeT46GCWLWYnaSbsAR_3wUysZ4ljDJFSL8uQfSXfUCbrUos4AeSiIkYUA-xzBu24A9y0Rr-WNhgfKr_nmLO-SgW2q4cgO5LkhC-OZfKGTC_zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a8425054.mp4?token=cNyI7yLMAZ00izFEAzvQRbfytKJmUR3ukBT5qhbV_Cel_zgIaVa5hr3601C06E9JpuVBwWfROuZX5bqv4JOLSY05sC-S3RZhiPor2-kVsQou3w1FATq0hre7YsSMRgD0GIlXQW_WJb-sCNWt5sgXH25bxHVEILqbHlXZ4sMCqv-UNWTVOLwMQpHiVshR_09qxHcU7x7-68BZ8k3GkR0XEN0TR2EYCOCLHBVHqYnu4yeT46GCWLWYnaSbsAR_3wUysZ4ljDJFSL8uQfSXfUCbrUos4AeSiIkYUA-xzBu24A9y0Rr-WNhgfKr_nmLO-SgW2q4cgO5LkhC-OZfKGTC_zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده های ارتش بر فراز تهران
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14415" target="_blank">📅 01:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14414">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer"><a href="https://t.me/withyashar/14414" target="_blank">📅 01:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14413">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">منابع آمریکایی:حملات برای آماده سازی برای ورود زمینی انجام میشود
@withyashar</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/14413" target="_blank">📅 01:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14412">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">طبق گزارش‌ها، پایگاه نیروی دریایی کنگان برای چندمین بار هدف قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14412" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14411">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کانال ۱۲ اسرائیل: آماده پیوستن به حملات علیه ایران هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/14411" target="_blank">📅 01:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14410">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">منابع خبری آمریکا: عملیات امشب سنتکام در تمامی نقاط حیاتی ایران خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/14410" target="_blank">📅 01:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14409">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزیر جنگ آمریکا : حملات امشب مقدمه حملاتی بزرگتر است
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/14409" target="_blank">📅 01:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14408">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پدافند کرمان فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/14408" target="_blank">📅 01:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14407">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انفجار در کارخانه پتروشیمی در عسلویه
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/14407" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14406">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سنتکام: نیروهای فرماندهی مرکزی ایالات متحده امروز ساعت ۵:۱۵ بعدازظهر به وقت شرقی، به دستور فرمانده کل قوا، حملات دفاعی اضافی را علیه چندین هدف در ایران آغاز کردند. این حملات در پاسخ به تجاوزات بی‌دلیل و مداوم ایران انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/14406" target="_blank">📅 01:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14405">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">العربیه: پدافند هوایی در «عسلویه» در استان بوشهر فعال شد.
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14405" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14404">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بندرعباس زیر زارتان زورتان شدید
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14404" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14403">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فارس تایید کرد : شنیده شدن صدای انفجار در سیریک و قشم
دقایقی پیش صدای انفجارهایی در قشم و سیریک به گوش رسید؛ همزمان پدافند هوایی در قشم شروع به فعالیت کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14403" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14402">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ادعای اکسیوس: حمله آمریکا به ایران آغاز شده
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/14402" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
