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
<img src="https://cdn4.telesco.pe/file/D2MBelVTSvrvcdkQmlH1G2ecDqMFTw4hTw_YK09b2DIuid47tV_7AC242yoah_4XR7-EVVUtbkxSUMstu83Clnl7MqdTCBk-C6BkZ3GcihwsOjMA2tyJbXm77SE-jnEyFqFuC7KxLA9YwgbZPoS8UMv4l2FQ83lf220wq_LMegGqFoKRRqWospps-vCzjg-eBDNM0LUMEencf5fvTfyUBZ34DjWpO3viHvwk-k3IZhddsGZm76ga7xH7p2WVcDEoMN4Xm4BYOQx9BqqRHD1j3CXgFBn4F6T8vsOby3LQhjCMBflQYvgn2WNgp-QxwLXkJw_JNSJys-g-7L6NhlMa6g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 13:49:48</div>
<hr>

<div class="tg-post" id="msg-23587">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ikc5dVwB7CsUTIhRrDJh_itdn6_16Ry25A7hGNIl16H_mdalBdKbItFnM9Isi-JmkCVJmHPEYYHcFXNiYxJd3sXVp5_Qjt-mkHXWG5nDlg1vQVGFkHT89XMkpOCq2GZzHeTdRSso1sr0HOdcp6PHM59Fm2dq1nEIFeIfbYzPJIcYGGC-sanDYDF80A9Sx3HSwp_kHcLn0QSKnBEBTYZPc28tgSb5s-idfWW1Laud1PhuCi-Ul50DIRuTxz6VC-h29LlJmVxTDo1QukXPHUkZZG2Q6f1k-37EC5xYsHvUT2HlZNWsyZHoubSoKBNKsXlGYSSzCEqu4-S6E-_iHqAOpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : تصاویر ماهواره‌ای جدید نشان میدهد ایران در حال بازسازی سریع تأسیسات طالقان ۲ است: تصاویر ماهواره‌ای شرکت وانتور از ۱۳ سپتامبر ۲۰۲۶ نشان می‌دهد ایران بازسازی تأسیسات طالقان ۲ در مجموعه نظامی پارچین حدود ۳۰ کیلومتری جنوب‌شرق تهران را با سرعت…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/withyashar/23587" target="_blank">📅 13:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23586">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dih8RRZP-Vw36KxjRW5ATNEgVJ9KSKolXHlIcI4Ynm-ycQraV_vlwIVvL9kr70CEeUJQBy5eA2yHBb9c2qsjOFlVbHFxTzkVpubQC6umPewHOp6xG0bYZiOg0_xK4PmBLLWYaN5ESlE6ndcvJhcTKeLxUr9La6Hv4lJygNjiMZNNku3o8QfPJr9jsTwkf6uit9rn_i2LCq6GEag_FGwvSENWzJoPZ1M0ifRuOwu6nWJPVPh1FMzzvajBct0pntUWFUVmXoVlCswWDI49MUwwpc5n3dqembLXg7TUWqva24yz7Qw-UKY9AUu25YMGW-UO7CjRcAlx758OS6AXlI_Y8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فناوری جدید برای مقابله با طوفان‌ها :
پژوهشگران با بررسی حدود ۳۰ سال داده‌های هواپیماهای موسوم به
Hurricane Hunters
چهار نشانه را شناسایی کرده که می‌تواند به پیش‌بینی بهتر زمان تقویت سریع یک طوفان گرمسیری کمک کند. این موضوع می‌تواند برای هشدار زودهنگام در برابر طوفان‌های شدید اهمیت داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/withyashar/23586" target="_blank">📅 13:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23585">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پژوهشگران پس از
۵۰ سال
منشأ یک گروه خونی بسیار نادر را کشف کردند. این وضعیت که
AnWj منفی
نام دارد، از سال ۱۹۷۲ شناخته شده بود و حالا مشخص شده به ژن
MAL
مربوط است. بیش از
۹۹.۹ درصد مردم AnWj مثبت
هستند و انتقال خون نامتناسب به افراد AnWj منفی می‌تواند باعث واکنش خطرناک ایمنی شود. این کشف به شناسایی این افراد و پیدا کردن خون سازگار کمک می‌کند و
سیستم MAL به‌عنوان چهل‌وهفتمین سیستم گروه خونی انسان
به رسمیت شناخته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/withyashar/23585" target="_blank">📅 13:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23584">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اسپیس‌ایکس مجوز بین‌المللی Starlink Mobile را دریافت کرد
؛ کمیسیون ارتباطات فدرال آمریکا (FCC) در
۱۷ سپتامبر
مجوز فعالیت بین‌المللی سرویس موبایلی استارلینک را صادر کرد. این مجوز گام مهمی برای توسعه فناوری
اتصال مستقیم ماهواره به گوشی‌های معمولی
است؛ فناوری‌ای که استارلینک قصد دارد در نسل بعدی آن، تماس، پیام، اینترنت و خدمات ارتباطی را بدون نیاز به آنتن زمینی در مناطق فاقد پوشش موبایل ارائه کند. البته برای فعال شدن این سرویس در هر کشور، دریافت مجوزهای محلی همچنان ضروری است.
@WarRoom</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/withyashar/23584" target="_blank">📅 13:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23583">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رویترز:
یک پیشرفت مهم فناوری در چین اعلام شد.
شرکت چینی CXMT اعلام کرده نسل پنجم فناوری تولید تراشه‌های حافظه DRAM این شرکت وارد تولید انبوه شده است. این فناوری با فاصله ساختاری ۱۱.۹۵ نانومتری طراحی شده و چین می‌گوید می‌تواند تولید تراشه روی هر ویفر را دست‌کم ۵۰ درصد افزایش دهد. این تحول برای چین در رقابت با
سامسونگ، SK Hynix و Micron
اهمیت استراتژیک دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/withyashar/23583" target="_blank">📅 13:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23582">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جنوب لبنان صدای ناله های حسن خرسی میاد @WarRoom</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/withyashar/23582" target="_blank">📅 13:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23581">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تایمز اسرائیل:
اسرائیل در حال بررسی نقش احتمالی خود در دفاع از عربستان است.
این موضوع در پی گسترش حملات حوثی‌ها و فشار همزمان بر مسیرهای هرمز و باب‌المندب مطرح شده است
@WarRoom</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/withyashar/23581" target="_blank">📅 13:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23580">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رویترز:
آمریکا و چین امروز مذاکرات مهمی را در نیویورک آغاز می‌کنند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، و هه لیفنگ، معاون نخست‌وزیر چین ؛ این مذاکرات چند روز پیش از دیدار ترامپ و شی جین‌پینگ در واشنگتن انجام می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/withyashar/23580" target="_blank">📅 13:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23579">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یاهو نیوز :
ارتش تایوان برای نخستین‌بار رزمایش مشترک با چند نوع پهپاد تهاجمی برگزار کرد.
این رزمایش شامل موشک‌های ضدکشتی بومی و سامانه‌های HIMARS نیز بود و رئیس‌جمهور تایوان گفت ارتش در حال تطبیق خود با جنگ مدرن و افزایش تهدید چین است
@WarRoom</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/withyashar/23579" target="_blank">📅 13:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23578">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رویترز:
ایران اعلام کرده تنگه هرمز تا تحقق شروط تهران بازگشایی نخواهد شد.
محمدباقر قالیباف، رئیس مجلس ایران، گفته بازگشایی تنگه به اجرای تعهدات آمریکا و برآورده شدن شروط ایران بستگی دارد. همزمان محسن رضایی اعلام کرده تهران هفت شرط برای آغاز مذاکرات با واشنگتن از طریق میانجی‌ها مطرح کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/withyashar/23578" target="_blank">📅 13:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23577">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رویترز:
رهبران جهان این هفته برای نشست مجمع عمومی سازمان ملل به نیویورک می‌روند.
نزدیک به ۱۳۰ رئیس دولت و کشور در این نشست حضور خواهند داشت و جنگ ایران، بحران اوکراین، بحران انرژی و خطرات هوش مصنوعی از موضوعات اصلی هستند. ترامپ قرار است بار دیگر در مجمع عمومی سخنرانی کند و پزشکیان و نتانیاهو نیز در برنامه سخنرانی دارند.
شی جین‌پینگ به نیویورک نمی‌رود و به‌جای آن احتمالا مستقیماً در واشنگتن با ترامپ دیدار خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/withyashar/23577" target="_blank">📅 12:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23576">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فرمانداری دزفول اعلام کرد صدای انفجاری که دقایقی قبل در بعضی مناطق شهرستان شنیده شد، به دلیل منفجر کردن و از بین بردن مهمات بوده و مربوط به حادثه یا حمله جدیدی نبوده است
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/23576" target="_blank">📅 10:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23575">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/23575" target="_blank">📅 09:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23574">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/23574" target="_blank">📅 09:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23573">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/23573" target="_blank">📅 09:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23572">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f301cc57.mp4?token=cSRCdeT3Y00sXl9OPX9vRv1UPYvONDJmEfHoRR5Qw1ys6vdsFdDMCI8VHdr_8H8p2FUh9mBt5kcslvR9GbdPQeamdHwpWAPGiOYP8POhyvKO-NxkapQjTAip5c7olhQcA5AfodY_fJDiWzzOk_Yy-2qm0iysECULYk0KZaIJeQ8XdxsaK7072UmeqJKTt9wCD9eBDmRwvCpdnhzAv1GYuu1C7YaPVTmpNs1I1PKsWlaU_dWHBax3FqT0ITtgLdsTRgXn9HRRSTvR5Ojl7Ljhzxex_n6vqrOdwiNNjb4ztvjiYPOvFKXDZecyeJsPLYSbtsQWSmfApcgyLcRoSEXEqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f301cc57.mp4?token=cSRCdeT3Y00sXl9OPX9vRv1UPYvONDJmEfHoRR5Qw1ys6vdsFdDMCI8VHdr_8H8p2FUh9mBt5kcslvR9GbdPQeamdHwpWAPGiOYP8POhyvKO-NxkapQjTAip5c7olhQcA5AfodY_fJDiWzzOk_Yy-2qm0iysECULYk0KZaIJeQ8XdxsaK7072UmeqJKTt9wCD9eBDmRwvCpdnhzAv1GYuu1C7YaPVTmpNs1I1PKsWlaU_dWHBax3FqT0ITtgLdsTRgXn9HRRSTvR5Ojl7Ljhzxex_n6vqrOdwiNNjb4ztvjiYPOvFKXDZecyeJsPLYSbtsQWSmfApcgyLcRoSEXEqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب «محسن نامجو» یهو با صدای بلند تو خیابون شروع کرد به آواز خوندن که یه هموطن اینطوری رید بهش و با یه خفه شو کار رو بست تا مزاحم مردم نشه
@WarRoom</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/23572" target="_blank">📅 09:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23571">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6efb269a37.mp4?token=a5ZlesRgkiN_bp9SylyKr_5a6Lv7uHlEr5VqPubkHuz_94hiJZzAgTFW2bH6Q5GF7BKeS6XNLvQYYT-689y8qvrhvneMuSUuTHP3M7DOmU_MGgwLtwH6HLWFZQF9SCFoPCsTHebZKzZyODggvvCV7l6P1SHv7fNbFGtBP5h6wSB2lf4Y7K1b-qO4U8MV3liYiNQ6BNUv4RU3kbQW_MjUHYmY6PN88uqDlnRm8cjANZPAhMY-UPz21NKix3w9FJ_U77365kLj4m4LsEbmdfiCjoX00nnB90ttIB8NYHR0W2iYMarCg-AgAgMrXB1oNrn0VZUQWk-aj3sks7VJLrJrRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6efb269a37.mp4?token=a5ZlesRgkiN_bp9SylyKr_5a6Lv7uHlEr5VqPubkHuz_94hiJZzAgTFW2bH6Q5GF7BKeS6XNLvQYYT-689y8qvrhvneMuSUuTHP3M7DOmU_MGgwLtwH6HLWFZQF9SCFoPCsTHebZKzZyODggvvCV7l6P1SHv7fNbFGtBP5h6wSB2lf4Y7K1b-qO4U8MV3liYiNQ6BNUv4RU3kbQW_MjUHYmY6PN88uqDlnRm8cjANZPAhMY-UPz21NKix3w9FJ_U77365kLj4m4LsEbmdfiCjoX00nnB90ttIB8NYHR0W2iYMarCg-AgAgMrXB1oNrn0VZUQWk-aj3sks7VJLrJrRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاله سینا اشکبوسی جاویدنام ۱۶ ساله در مراسم کوروش کبیر دو از شدت تأثر از حال رفت
@WarRoom
💔</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/23571" target="_blank">📅 09:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23570">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e48ca2a7.mp4?token=tG-F3W7PaMYfhQY-CZZmLAKDm-tMJB2ogjOHC_mPBLA4pNMvfd9OuBnBtQLP9wQ9UyBe18dmm0vTNvJ8RyIUwQdusnmxwmUa2iUO6loVojkLRuM1RTMI3oe9_qPfldDEkZPg37TN40ekrm55pzS3R2eslLzzQG6ghQ4v25kL61RMn4uwHk-hXaflt6qa627jchgBu3GPtPr1vDvmZaIqD0cyKK0HF8EcvBfe7FTVFSqeVGKyfWnNR1RSqws_lNIrbCZqLS8j5ElixEuUbvJwQo0iZR1ffFg94qihYQ7N2w6_Gbcy898wHp97wfSYqIY_E4SZZfOuDX8Yu9IJmnOlGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e48ca2a7.mp4?token=tG-F3W7PaMYfhQY-CZZmLAKDm-tMJB2ogjOHC_mPBLA4pNMvfd9OuBnBtQLP9wQ9UyBe18dmm0vTNvJ8RyIUwQdusnmxwmUa2iUO6loVojkLRuM1RTMI3oe9_qPfldDEkZPg37TN40ekrm55pzS3R2eslLzzQG6ghQ4v25kL61RMn4uwHk-hXaflt6qa627jchgBu3GPtPr1vDvmZaIqD0cyKK0HF8EcvBfe7FTVFSqeVGKyfWnNR1RSqws_lNIrbCZqLS8j5ElixEuUbvJwQo0iZR1ffFg94qihYQ7N2w6_Gbcy898wHp97wfSYqIY_E4SZZfOuDX8Yu9IJmnOlGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هموطن با غیرت از مایک جانسون، رئیس مجلس نمایندگان آمریکا، می‌خواهد کار نیمه‌تمام را تمام کند و به این رژیم پایان دهد. مایک جانسون ماه پیش هم در سخنرانی خود در مورد حملات به ایران گفته بود که
ما سر مار را زدیم
و همچنین در ابتدای جنگ هم گفته بود مردم ایران دهه‌ها زیر یک رژیم تروریستی استبدادی زندگی کرده‌اند و اگر تغییر رژیم در حال رخ دادن باشد، این می‌تواند برای مردم ایران فرصتی برای چشیدن آزادی باشد.
مردم ایران باید برای به‌دست آوردن و حفظ آزادی قیام کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/23570" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23569">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a2f841f0.mp4?token=OkX3BX1N82vta4zuVJIxxB3XKyLdceXP3iKLZ84qxRpyx4nvaxBvgzwekjbkiGk4pYNBFypeKZVuwMoE8oDBBQi7QrFqR0Umfy4iuZ-mEyHWSOY5TFUdc-culFHNf0zjAUPX4ST9w85jh6JnEmeGKiJ-S_LDP6kHvGYFpg-SbOZom5lAgIdvQ46jxvtmr-YE-sbUWqRa88e8FDUC4LS8kofPPtLDq1cyhBsSb3H-lbseFCSU-tpACJFWvZtPksgIB8LC0Ds08-qZ-dOA_UETVgaPkdvxeT5h-qZ1u9L8vkBneXPZXHHClhtIcbNFB9ARvxGfsFlARR9BEOG4HnZQMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a2f841f0.mp4?token=OkX3BX1N82vta4zuVJIxxB3XKyLdceXP3iKLZ84qxRpyx4nvaxBvgzwekjbkiGk4pYNBFypeKZVuwMoE8oDBBQi7QrFqR0Umfy4iuZ-mEyHWSOY5TFUdc-culFHNf0zjAUPX4ST9w85jh6JnEmeGKiJ-S_LDP6kHvGYFpg-SbOZom5lAgIdvQ46jxvtmr-YE-sbUWqRa88e8FDUC4LS8kofPPtLDq1cyhBsSb3H-lbseFCSU-tpACJFWvZtPksgIB8LC0Ds08-qZ-dOA_UETVgaPkdvxeT5h-qZ1u9L8vkBneXPZXHHClhtIcbNFB9ARvxGfsFlARR9BEOG4HnZQMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏یه پیام اضطراری خیلی کوتاه ۱۷ کاراکتری (EAM) ساعاتی پیش روی شبکه HFGCS آمریکا پخش شد. آخرین بار بعد از شروع جنگ با ایران همچین چیز مشابهی شنیده شد..
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/23569" target="_blank">📅 09:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23568">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فیزیک
@WarRoom</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/23568" target="_blank">📅 08:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23567">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ویدیو اختصاصی زیبا از دیشب
@WarRoom</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/23567" target="_blank">📅 07:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23566">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دیدبان اتاق جنگ : ديشب چندتا موشك خورده ب قايق هاي سپاه داخل قشم  جزايره ناز سوزا ، شايدم قايق صياد های بسیجی بوده که میرن شهپاد های آمریکارو بدزدن بوده معلوم نيست ، ولي برخورد انجام شده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/23566" target="_blank">📅 07:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23565">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf28a7f1e.mp4?token=NUk7rBO6WUXbuc3nSXTME4LF5n7AN4cqXS7Am-9dab1tFXsf9PvmgboAI9tLS_lD8kOR6RJexEXF26S6ciVKm8AdifMgPAHQmkquBlbvsRgjKV7b08hWKocqFly1O6qjCwtz0UoI0C79K0aTCCgf1di8JR-iJMJNc82rwPEk9O4SGE9pC-3h-29RfGIo1BKkhpa6Dt8prHM4kkh8WFUBxFerAaf1zYvfh3P9RGV4dX6HRwq5pzqzS786GDYXaPC48VJN2hQgcAWPpZNLO3ysCwkS2FiXg6t9QPBO95OoPt7OpswCGoAYhGVxUtSiVPjSvHBK2VNQNCyWPIzTsFX-bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf28a7f1e.mp4?token=NUk7rBO6WUXbuc3nSXTME4LF5n7AN4cqXS7Am-9dab1tFXsf9PvmgboAI9tLS_lD8kOR6RJexEXF26S6ciVKm8AdifMgPAHQmkquBlbvsRgjKV7b08hWKocqFly1O6qjCwtz0UoI0C79K0aTCCgf1di8JR-iJMJNc82rwPEk9O4SGE9pC-3h-29RfGIo1BKkhpa6Dt8prHM4kkh8WFUBxFerAaf1zYvfh3P9RGV4dX6HRwq5pzqzS786GDYXaPC48VJN2hQgcAWPpZNLO3ysCwkS2FiXg6t9QPBO95OoPt7OpswCGoAYhGVxUtSiVPjSvHBK2VNQNCyWPIzTsFX-bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فروند بمب‌افکن
B-1B Lancer
آمریکا امشب با پس‌سوز کامل از پایگاه
RAF Fairford
در بریتانیا برخاست. برخاستن با پس‌سوز معمولاً نشان‌دهنده وزن بالای هواپیما و احتمال حمل محموله تسلیحاتی سنگین است، هرچند در پروازهای آموزشی هم استفاده می‌شود. حدود
۱۲ فروند B-1B
همچنان در فرفورد مستقر هستند و این پایگاه از ماه مارس یکی از مراکز اصلی عملیات
Epic Fury
علیه اهدافی در ایران بوده است.
در اطراف پایگاه نیز برخی خبرنگاران و عکاسان هوانوردی شبانه‌روز در مستقر می‌شوند
و با هر پرواز سریعاً عکس و فیلم تهیه می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23565" target="_blank">📅 06:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23564">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نوراد: یک جنگنده اف-۱۶ یک هواپیمای غیرنظامی را که وارد حریم هوایی ممنوعه کمپ دیوید در مریلند شده بود، رهگیری کرد. این حادثه ساعت ۱۵:۲۰ به وقت تهران (۷:۵۰ صبح به وقت محلی) رخ داد. جنگنده برای برقراری ارتباط با خلبان، شراره‌های هشدار شلیک کرد و سپس هواپیما را…</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/23564" target="_blank">📅 06:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23563">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وزارت امور خارجه ایالات متحده:
احتمال تشدید درگیری بین عربستان سعودی و حوثی‌های تحت حمایت ایران , آمریکایی‌های خارج از خاورمیانه باید سفر به این منطقه یا عبور از آن را به طور جدی مورد بازنگری قرار دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23563" target="_blank">📅 06:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23562">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b3db75582.mp4?token=iFIH5e2CGH5kM18oPYdVpxbPYGEbpUUMAChqHxWoEwp-Ro4lyRU1fTXqjUIaMxYzaGRGZZgO0DXD8ZZpATU5kjs4g5LfCLYpro3L6ZCXLbjyJAdkb1PubFwpOJjCU9GAdet0ZQYCNCR25PF9aqy7NU5PZwnp2BstjraWPR5jpNzL9D-mpU4FZ2OmJjlh9WS6WGJRMyb3xEs8Gmzun5J95-lnOedq0q86Bg14HCtfiWog2VsvqYUj8n4Qe-E8D8xI10P4G2C9gPe_axCl6tUs50fxiJedCybm7z-Cfb7n8bfh7OD6gORrXyGWBWMpnMZaIA4uctowOyfKiT6MYWel3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b3db75582.mp4?token=iFIH5e2CGH5kM18oPYdVpxbPYGEbpUUMAChqHxWoEwp-Ro4lyRU1fTXqjUIaMxYzaGRGZZgO0DXD8ZZpATU5kjs4g5LfCLYpro3L6ZCXLbjyJAdkb1PubFwpOJjCU9GAdet0ZQYCNCR25PF9aqy7NU5PZwnp2BstjraWPR5jpNzL9D-mpU4FZ2OmJjlh9WS6WGJRMyb3xEs8Gmzun5J95-lnOedq0q86Bg14HCtfiWog2VsvqYUj8n4Qe-E8D8xI10P4G2C9gPe_axCl6tUs50fxiJedCybm7z-Cfb7n8bfh7OD6gORrXyGWBWMpnMZaIA4uctowOyfKiT6MYWel3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در رویداد «کوروش کبیر ۲» در تورنتو : «حماسه دی» نتیجه یک هیجان زودگذر نبود؛ پشت آن یک مسیر طولانی و پرهزینه بود. جمهوری اسلامی که در روزهای ۱۸ و ۱۹ دی سقوط خودش را قطعی می‌دید، دست به یکی از بزرگ‌ترین جنایت‌های تاریخ زد. ما امروز از همیشه باتجربه‌تر و مصمم‌تریم. هدفمان مشخص است: سرنگونی جمهوری اسلامی و رسیدن به یک ایران آزاد و آباد. چهار اصل اصلی ما هم روشن است: حفظ تمامیت ارضی ایران، جدایی دین از حکومت، آزادی‌های فردی و برابری همه شهروندان در برابر قانون، و اینکه مردم خودشان با رأی آزاد و عادلانه شکل آینده حکومت ایران را تعیین کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23562" target="_blank">📅 01:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23561">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سفارت آمریکا در لبنان، بغداد، بحرین و اردن نیز هشدار مشابهی دادند. @WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23561" target="_blank">📅 01:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23560">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سفارت آمریکا در اورشلیم به شهروندان آمریکایی در اسرائیل و منطقه هشدار داده است که با توجه به افزایش تنش‌ها، احتمال بسته‌شدن فضای هوایی، لغو یا اختلال در پروازها و محدودیت‌های تردد وجود دارد و از مسافران خواسته وضعیت پروازها و فعالیت فرودگاه‌ها را مرتب بررسی…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23560" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23559">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7efc866236.mp4?token=PPgTe4XfFWdP4O2cjCO7rAIjIRZkkTAG98cB9vhBHE9stOApguDsNXoNbhm95W0iMsEQHpiHQ4__XQ9uAlk-4PIZL2aIpRCJouOGE66r1kcp96_7WYYjlok3LKqieUjkwk-_inpBnNwXPqQr5wnjKqcxRE8K8SzcJUdnRVCutmWAnqO-gFgEw9x2nmqJi9SfeXLXoxSE8GIM8v6vHMfgpl2ywqUfvRhdQus9Bss3zwfjjXNWEt3uE9P0fJfCqOvu9fZxddVZehkXytEAwwd2qdR_ia2TfQfOWAuvgVDbmcC52oIvVVrwU6pkfGBPZcNKBOAl9jLQu2RVre0ax85wog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7efc866236.mp4?token=PPgTe4XfFWdP4O2cjCO7rAIjIRZkkTAG98cB9vhBHE9stOApguDsNXoNbhm95W0iMsEQHpiHQ4__XQ9uAlk-4PIZL2aIpRCJouOGE66r1kcp96_7WYYjlok3LKqieUjkwk-_inpBnNwXPqQr5wnjKqcxRE8K8SzcJUdnRVCutmWAnqO-gFgEw9x2nmqJi9SfeXLXoxSE8GIM8v6vHMfgpl2ywqUfvRhdQus9Bss3zwfjjXNWEt3uE9P0fJfCqOvu9fZxddVZehkXytEAwwd2qdR_ia2TfQfOWAuvgVDbmcC52oIvVVrwU6pkfGBPZcNKBOAl9jLQu2RVre0ax85wog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23559" target="_blank">📅 01:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23558">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رضاتون کجاس حرومی?</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23558" target="_blank">📅 00:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23557">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a9813c09.mp4?token=k8EZCuBVAIX8Hwd3yLITiZZ6Dgk105ze0epI9JcsJSBKiqrEoZxa_8UN6gePtgN9p9qSe4GVuMLJXg0jC1TI-B-R0UHZZnGJiPoaRHLxvweTF9sTKPr8FRYmYWcy2awJ6O4b2l4Gl9yKGZh99ZMRAW9asBCI9Zmtl11yIrGz5BsKDIEDzFpI_71a5r6GOyODqdOQgfrj-b2_zZWem2qugEUrGvkN6vV4Shdg0K9U_jyo_hpTZIDxTWyy4QiYQalc3z1xr4M5qGHudnW6uKIAqUDjl98gzzPzuQTJ7ya-LLydh2UdGBncCVVvF1VMBSmNb6usxWsWMfPEZP3IR9E_CU5bCFypcy0l9IePHDNQ7f_Ozdf6ALKbY4zCq216cx69ONxSyRE_su25dprPSUW0N2lEH8wURs-yw-7L4GQrhfp6NGz7nvfTBQA4-xneJ_ljS0ZTjWJKeoJ-TyvPphmtEJeLprYpLmQioMOxA0PaqyZyZiZtU_d_iHNlJcxCFpLsof2D229OSHrtWdT9pZjg4MvPfy7X7XqQo9T3i9Wq7jE8IlLesHqw4-FKWIgOu9Cr-xu7XcRuLdbpHO_4mr4yAPHzX1p_or74DymQull4WtJ6781HVamMRdeqcLrCUTcsHBQMJ3etZfdr5DcduzmIhsa7m0D2G4L94toS1Pxol8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a9813c09.mp4?token=k8EZCuBVAIX8Hwd3yLITiZZ6Dgk105ze0epI9JcsJSBKiqrEoZxa_8UN6gePtgN9p9qSe4GVuMLJXg0jC1TI-B-R0UHZZnGJiPoaRHLxvweTF9sTKPr8FRYmYWcy2awJ6O4b2l4Gl9yKGZh99ZMRAW9asBCI9Zmtl11yIrGz5BsKDIEDzFpI_71a5r6GOyODqdOQgfrj-b2_zZWem2qugEUrGvkN6vV4Shdg0K9U_jyo_hpTZIDxTWyy4QiYQalc3z1xr4M5qGHudnW6uKIAqUDjl98gzzPzuQTJ7ya-LLydh2UdGBncCVVvF1VMBSmNb6usxWsWMfPEZP3IR9E_CU5bCFypcy0l9IePHDNQ7f_Ozdf6ALKbY4zCq216cx69ONxSyRE_su25dprPSUW0N2lEH8wURs-yw-7L4GQrhfp6NGz7nvfTBQA4-xneJ_ljS0ZTjWJKeoJ-TyvPphmtEJeLprYpLmQioMOxA0PaqyZyZiZtU_d_iHNlJcxCFpLsof2D229OSHrtWdT9pZjg4MvPfy7X7XqQo9T3i9Wq7jE8IlLesHqw4-FKWIgOu9Cr-xu7XcRuLdbpHO_4mr4yAPHzX1p_or74DymQull4WtJ6781HVamMRdeqcLrCUTcsHBQMJ3etZfdr5DcduzmIhsa7m0D2G4L94toS1Pxol8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون شاهزاده در همایش کوروش ۲ در کانادا، همچنین ۲ جنرال کانادایی هم در تصویر دیده میشوند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23557" target="_blank">📅 00:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23556">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmin</strong></div>
<div class="tg-text">رضاتون کجاس حرومی?</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23556" target="_blank">📅 00:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23555">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جنوب لبنان صدای ناله های حسن خرسی میاد
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23555" target="_blank">📅 00:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23554">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">چند گزارش از فعالیت کوتاه پدافند شیراز
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23554" target="_blank">📅 00:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23553">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سفارت آمریکا در اورشلیم به شهروندان آمریکایی در اسرائیل و منطقه هشدار داده است که با توجه به افزایش تنش‌ها، احتمال
بسته‌شدن فضای هوایی، لغو یا اختلال در پروازها و محدودیت‌های تردد
وجود دارد و از مسافران خواسته وضعیت پروازها و فعالیت فرودگاه‌ها را مرتب بررسی کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/23553" target="_blank">📅 00:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23552">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پدافند شرق تحرک ریزی انجام داد قطع شد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/23552" target="_blank">📅 23:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23551">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انتخابات پارلمانی روسیه در حالی ادامه دارد که مقام‌های روس از
حملات سایبری به سامانه رأی‌گیری و شبکه‌های ارتباطی
خبر داده‌اند. مسکو اوکراین را متهم کرده، اما برای این اتهام مدرکی ارائه نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/23551" target="_blank">📅 23:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23550">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نوراد: یک جنگنده
اف-۱۶
یک هواپیمای غیرنظامی را که وارد
حریم هوایی ممنوعه کمپ دیوید
در مریلند شده بود، رهگیری کرد. این حادثه ساعت
۱۵:۲۰ به وقت تهران
(۷:۵۰ صبح به وقت محلی) رخ داد. جنگنده برای برقراری ارتباط با خلبان،
شراره‌های هشدار
شلیک کرد و سپس هواپیما را به‌سلامت از منطقه خارج کرد.
دونالد ترامپ
هنگام این حادثه در کمپ دیوید حضور داشت
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/23550" target="_blank">📅 22:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23549">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رویترز: دونالد ترامپ اعلام کرد آمریکا یک «نیروی هوش مصنوعی» تشکیل خواهد داد؛ طرحی که به گفته او مشابه نیروی فضایی است که در دوره اول ریاست‌جمهوری‌اش ایجاد کرد. ترامپ همچنین گفت به‌زودی یک «تزار هوش مصنوعی» برای نظارت بر این طرح منصوب خواهد کرد. هنوز مشخص نیست این نیرو یک شاخه نظامی مستقل خواهد بود یا یک نهاد فدرال برای نظارت و توسعه هوش مصنوعی.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/23549" target="_blank">📅 22:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23548">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رویترز: کره‌جنوبی اینبار اعلام آمادگی کرد در بازگشایی هرمز مشارکت کند
؛ وزیر خارجه کره‌جنوبی در دیدار با مارکو روبیو اعلام کرده سئول آماده است «مشارکت اساسی» در بازگرداندن عبور آزاد کشتی‌ها از تنگه هرمز داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/23548" target="_blank">📅 21:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23547">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آسوشیتدپرس: زنان بدون حجاب در یک مسابقه دو در تهران شرکت کردند
؛ صدها زن بدون حجاب اجباری در یکی از بزرگ‌ترین نمایش‌های نافرمانی اجتماعی در سال‌های اخیر در یک مسابقه دو در بوستان ولایت تهران شرکت کردند. همزمان در همان روز تجمعی حکومتی در تهران برگزار شد و زنان محجبه در حمایت از حکومت و جنگ حضور داشتند.وزارت ورزش از یک ماه قبل مجوز داده بود ولی دادستانی تهران اعلام کرد علیه عوامل و دست‌اندرکاران برگزاری مسابقه دو در بوستان ولایت اعلام جرم کرده و پرونده قضایی تشکیل داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/23547" target="_blank">📅 21:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23546">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الجزیره: ۱۱ سرباز سوری در انفجار انبار مهمات کشته شدند
؛ انفجار در یک موضع نظامی در منطقه عیّاش در استان دیرالزور رخ داده و ۹ سرباز دیگر زخمی شده‌اند. علت انفجار هنوز مشخص نیست و تحقیقات ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/23546" target="_blank">📅 21:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23545">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94774fe4a2.mp4?token=k6s5or3w3pGBPnxjmAUwTingOo6fv6hgytcbHu8zpqTs3nc3X12aFx7heEMI2cCwYNPAiH3K16Z7ha33yI7vl51SFp6nQx_Gj35QZs_aZE5CoKchqyRquLE8wq6Xv4x50cWJKO6B7SkecCsRmgLYT4SS1HaM2DCq6-YSPtk9RJJvR2HhZ2FXVz0TGnfwpOiNyBHve7xIibAt2oF9uFk8T9XT7OTS33CGJWZYLwr5S_uka_ZshEu_4moGLNj5hQaeWzBxlFARmllPTSgHMh6ueR0A9r4zGzdgoV-M2vDT0VYoNpQTe5a4jwLUEG4wDnv3ZihJPeVe8pUfRkrrajuTk4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94774fe4a2.mp4?token=k6s5or3w3pGBPnxjmAUwTingOo6fv6hgytcbHu8zpqTs3nc3X12aFx7heEMI2cCwYNPAiH3K16Z7ha33yI7vl51SFp6nQx_Gj35QZs_aZE5CoKchqyRquLE8wq6Xv4x50cWJKO6B7SkecCsRmgLYT4SS1HaM2DCq6-YSPtk9RJJvR2HhZ2FXVz0TGnfwpOiNyBHve7xIibAt2oF9uFk8T9XT7OTS33CGJWZYLwr5S_uka_ZshEu_4moGLNj5hQaeWzBxlFARmllPTSgHMh6ueR0A9r4zGzdgoV-M2vDT0VYoNpQTe5a4jwLUEG4wDnv3ZihJPeVe8pUfRkrrajuTk4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق روایت و ویدیو منتشرشده، چند جوان در خیابان دانشگاه زاهدان با خودرو در حال تردد بودند که ناگهان گلوله‌ای به سمت خودرو شلیک شد؛ گلوله گردن سرنشین صندلی شاگرد را خراش داد و از کنار گوش سرنشین عقب عبور کرد. گفته شده حال افراد داخل خودرو خوب است. در مقابل،
خبرگزاری فارس
گزارش داده بامداد جمعه حدود ساعت ۱۲:۳۰، نیروهای امنیتی به یک خودروی پژو مشکوک شدند و پس از مشاهده سلاح در خودرو، درگیری رخ داد که در جریان آن
۳ نفر کشته شدند
. درباره ارتباط این دو روایت، اطلاعات مستقلی منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/23545" target="_blank">📅 21:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23544">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">واشینگتن پست: رئیس‌جمهور ترامپ در اظهارات علنی خود همواره تأکید کرده است که سیاست‌های انتخاباتی میان‌دوره‌ای بر تصمیمات او درباره ایران تأثیری ندارند.
اما ترامپ در محافل خصوصی نشان داده است که می‌داند تصمیماتش در شکل‌گیری فضای سیاسی نامساعدی که حزبش با آن مواجه است، نقش داشته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23544" target="_blank">📅 21:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23543">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: متأسفانه دیوان عالی آمریکا شجاعت لازم برای «دوباره بزرگ کردن آمریکا» را نداشته است. آنها در شش ماه گذشته با تصمیم‌های سیاسی، نادرست و مضحک خود درباره تعرفه‌ها و حق شهروندی از طریق تولد، تریلیون‌ها دلار به ایالات متحده خسارت زده‌اند و برای همیشه به نحوه شهروند شدن افراد در کشور بزرگ ما آسیب وارد کرده‌اند. این فصل غم‌انگیزی در تاریخ آمریکا بوده، اما ما پیروز خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23543" target="_blank">📅 21:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23542">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBvq1klMmSxPqPE73P7FDxrSEy-2PlIcFxEwBAkTtSiiNosom113tdLDkfZPJnkphSNXlUctRWj2y-efCsIG-TC5upr6iPGRxaRD8T_lF83YJ7bpGMB7J8eJV_u-i6va2eZ33JoAK6a4T61aw6L7djTTdMZtn1EL4dl02m_3ocFyG0I33-A0u6H4K6PNeYfFcnN0hYzv73M6P1Xg6JEYx1KsqoZF5zS4AMxsWi9jLwa24u0xrEmX11vt8nEBu1_kkT_XSPMrWWvUHYp6KFOQ7Et_6K9qgb3XcxeKX9P5uLCazyg4D9TC5_dlpUOAfDSF0YQLgAFTLpYPHGnErHuwSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رژه جن فدا ها ، اخطار اگه تصویرو زوم کنید ‌شب ادراری‌ میگیرن
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23542" target="_blank">📅 20:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23541">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کانال 13 اسرائیل:
قطر شروط تهران برای پایان جنگ را به آمریکا منتقل کرده و ایران اکنون منتظر واکنش دونالد ترامپ است
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23541" target="_blank">📅 20:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23540">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرگزاری i24news : بنیامین نتانیاهو سفر خود به آمریکا را کوتاه کرده و برخلاف برنامه قبلی، به تگزاس نمی‌رود و دیدار برنامه‌ریزی‌شده با ایلان ماسک نیز لغو شده است. نتانیاهو اکنون قرار است پنجشنبه مستقیماً به نیویورک برود، در مجمع عمومی سازمان ملل سخنرانی کند و بلافاصله پس از آن به اسرائیل بازگردد. در برنامه فعلی همچنین دیداری با دونالد ترامپ وجود ندارد؛ مقام‌های آمریکایی دلیل آن را محدودیت زمانی و تفاوت برنامه سفر دو رهبر اعلام کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23540" target="_blank">📅 20:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23539">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db86a12457.mp4?token=PbSUUtf8FVDiUpayrVkMWg6oeCqITFw0K66u8KCl39bctEp523X8GHUay_wDB-Fk_RetAnGIiPcIin5vUKUkD_MsOtiJ1rxTcvESnQU1eTHc3S0uNzbKJYhfriZPaAo98ameQA37mGpViSwHB9WuTkhAe6oTZxs9LcA_hTXiXDhwOk_mInCNxqhvewkEj_CLw2s9spWodv4sRs3w5jqTQWpFij_9akoq-TkNw5WE9_x1fXQkKClNIz5NbOHyAyg51zFJ1gxoMYxkqyNOzJGYFG60yh7b9DByBGzEpp04SESIIVGOZ37kzKzndXKnieMweDuJCMYuRgRpcRUK0sBB0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db86a12457.mp4?token=PbSUUtf8FVDiUpayrVkMWg6oeCqITFw0K66u8KCl39bctEp523X8GHUay_wDB-Fk_RetAnGIiPcIin5vUKUkD_MsOtiJ1rxTcvESnQU1eTHc3S0uNzbKJYhfriZPaAo98ameQA37mGpViSwHB9WuTkhAe6oTZxs9LcA_hTXiXDhwOk_mInCNxqhvewkEj_CLw2s9spWodv4sRs3w5jqTQWpFij_9akoq-TkNw5WE9_x1fXQkKClNIz5NbOHyAyg51zFJ1gxoMYxkqyNOzJGYFG60yh7b9DByBGzEpp04SESIIVGOZ37kzKzndXKnieMweDuJCMYuRgRpcRUK0sBB0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارک لوین بازنشر کرد
صحبتهای
، رندی فاین، نماینده کنگره آمریکا:
شبکه‌های اجتماعی، اینفلوئنسرها و اعتراضات، همگی برای
بی‌ثبات کردن آمریکا از داخل
طراحی شده‌اند. بخش زیادی از این اقدامات توسط
روسیه، چین، ایران، ترکیه و قطر
تأمین مالی می‌شود. ما باید همین حالا درباره این موضوع صحبت کنیم تا مردم
قبل از اینکه خیلی دیر شود، بیدار شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23539" target="_blank">📅 19:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23538">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">صدای انفجارهای کنترل شده در ملارد
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23538" target="_blank">📅 19:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23537">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آکسیوس: جنگ ایران باعث افزایش شدید قیمت بنزین و گازوئیل در سراسر جهان شده و فشار اقتصادی و تورمی را حتی به کشورهایی که مستقیماً در جنگ دخالت ندارند منتقل کرده است. دولت‌ها اکنون با افزایش هزینه سوخت و فشار عمومی مواجه‌اند و در صورت ادامه جنگ، احتمال تشدید این فشارها وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23537" target="_blank">📅 19:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23536">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">محسن رضایی به شبکه الجزیره گفت:
از نظر واشنگتن، پذیرش شرایط ما برای خروج از جنگ، کار درستی است. تهدیدات ترامپ هیچ نتیجه‌ای نخواهد داشت و ما برای یک جنگ قاطع آماده هستیم. ارزیابی‌ها و محاسبات رئیس جمهور آمریکا درباره ایران نادرست بود و جنگ با تحریک نتانیاهو آغاز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23536" target="_blank">📅 18:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23535">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd58a1e73c.mp4?token=h8pBcrYgnSbrTTcFOhQGkQOV5r1wfkis8twGfXlKFrNRZX8789Mv49EZGG0H7geKfxU_DsrCWaUN1_deg4PI2WieQiOQe5u-Gvr13G9AzZlvptytIIuc2bK_oaokZs8sJGghq29t_c9HV2kNh57VlInhUCHFYTrbDyDcIHbG_qUHIGdcDMd1r8h3-JoS60tETG-GeYmiRi4o7rXm5EdhX84UW-6jugKZjZ9DjxhmeCOvPNIHy550gjTXmRcBFxwFGal4LYjlhcy0iWOZCF_qey-eiIGk4I0KeQ43f_NBnoK80xe8_zPrKCkSZbugICEdlRvEAwSRlublp12HR0M60BGu90FoEk3aPelUEWN5MgPM5JCX6XJe26g9LbS9WqbQbl4lqXzFW8Wzytk8b4XmsJz7s4tk76hAxLOuQ4t7nbsER_iOGEAUU4kUa8NdO16BUgcGe5-IFVKhIT7IT_nQq5yAeFvs_NjFRL0QMJG7u835Rq4wvNFYVm7NiXddLK9dMo81Vh7LPMuFsMss7ncqqTwtC05RPVZpgL07hPi_Xrv6rUVoLMxTblRaQiH6WG7HiVwVr6si1BTRq5C3DhQa2Jk_hfIUCYPSO0vij8eH1v544f1pcFL7rpI0ofod4xqLt1lsMw3up1_YFVf-43D8cWSIsn2XbB72ApFjmBT2DjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd58a1e73c.mp4?token=h8pBcrYgnSbrTTcFOhQGkQOV5r1wfkis8twGfXlKFrNRZX8789Mv49EZGG0H7geKfxU_DsrCWaUN1_deg4PI2WieQiOQe5u-Gvr13G9AzZlvptytIIuc2bK_oaokZs8sJGghq29t_c9HV2kNh57VlInhUCHFYTrbDyDcIHbG_qUHIGdcDMd1r8h3-JoS60tETG-GeYmiRi4o7rXm5EdhX84UW-6jugKZjZ9DjxhmeCOvPNIHy550gjTXmRcBFxwFGal4LYjlhcy0iWOZCF_qey-eiIGk4I0KeQ43f_NBnoK80xe8_zPrKCkSZbugICEdlRvEAwSRlublp12HR0M60BGu90FoEk3aPelUEWN5MgPM5JCX6XJe26g9LbS9WqbQbl4lqXzFW8Wzytk8b4XmsJz7s4tk76hAxLOuQ4t7nbsER_iOGEAUU4kUa8NdO16BUgcGe5-IFVKhIT7IT_nQq5yAeFvs_NjFRL0QMJG7u835Rq4wvNFYVm7NiXddLK9dMo81Vh7LPMuFsMss7ncqqTwtC05RPVZpgL07hPi_Xrv6rUVoLMxTblRaQiH6WG7HiVwVr6si1BTRq5C3DhQa2Jk_hfIUCYPSO0vij8eH1v544f1pcFL7rpI0ofod4xqLt1lsMw3up1_YFVf-43D8cWSIsn2XbB72ApFjmBT2DjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
کنگره از چه زمانی باید وارد عمل شود و درباره جنگ ایران تصمیم‌گیری کند؟
مایک جانسون، رئیس مجلس نمایندگان آمریکا:
ببینید، دولت این را یک جنگ در حال انجام نمی‌داند. چنین چیزی نیست. آنها در تلاش هستند یک عملیات را به پایان برسانند؛
عملیات «خشم حماسی» که موفقیتی بزرگ بود.
من فکر نمی‌کنم در شرایط فعلی نیازی باشد
دموکرات‌های مارکسیست لیبرال در کنگره
به فرمانده کل نیروهای مسلح بگویند با ارتش چه کار کند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23535" target="_blank">📅 18:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23534">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75e72d7fb2.mp4?token=dYfq_qKCnhQftbX6bQE4wjHs6nHKfdJUwze3sBhP-8vFk69JbBcFbbS5VFxl8WDRaadcUe4wOhpZA92hshdYxDvyg1hWv6WG7-tHOJZMAF02i7rC_xRP7uuEEG4T6hs_obhOj1AZ5NZBRcKya1G90Vec8kMeGXIwnDOGzI-NiO6Q74G3wfZs6PX9Bgh0vMHYd68GPkCRw1bauB5DZ8bTHsQSt0M7h2SqmmFGJMwIVqWt3eICc00JErfbkXeOPn_-RrOjLeM4pkgzRsBN6Zz4a2EaBndZvYRAiRFqTMdOs8KkXTTkRinOYGRrBEV5Zxwg372wFWJ5IL-50GHEPge1-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75e72d7fb2.mp4?token=dYfq_qKCnhQftbX6bQE4wjHs6nHKfdJUwze3sBhP-8vFk69JbBcFbbS5VFxl8WDRaadcUe4wOhpZA92hshdYxDvyg1hWv6WG7-tHOJZMAF02i7rC_xRP7uuEEG4T6hs_obhOj1AZ5NZBRcKya1G90Vec8kMeGXIwnDOGzI-NiO6Q74G3wfZs6PX9Bgh0vMHYd68GPkCRw1bauB5DZ8bTHsQSt0M7h2SqmmFGJMwIVqWt3eICc00JErfbkXeOPn_-RrOjLeM4pkgzRsBN6Zz4a2EaBndZvYRAiRFqTMdOs8KkXTTkRinOYGRrBEV5Zxwg372wFWJ5IL-50GHEPge1-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلاغ پر بازی کردن ناتنیاهو در سخنرانی :
نتانیاهو: حسن نصرالله کجاست؟
جمعیت: حذف شد.(پرر)
نتانیاهو: یحیی سنوار کجاست؟
جمعیت: حذف شد.(پررر)
نتانیاهو: اسماعیل هنیه کجاست؟
جمعیت: حذف شد.(پرررر)
نتانیاهو: علی خامنه ای کجاست؟
جمعیت: حذف شد(پررررر)
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23534" target="_blank">📅 17:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23533">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رویترز(کل ماجرا): اروپا در پی تشدید حملات روسیه به اوکراین وارد مرحله تازه‌ای از آماده‌باش شده است. روسیه حملات موشکی و پهپادی را افزایش داده و کشورهای اروپایی نگران سرایت جنگ به خاک ناتو، حملات سایبری، خرابکاری و حملات پهپادی هستند. لهستان امروز برای احتیاط جنگنده‌ها و پدافند هوایی خود را به حالت آماده‌باش درآورد، در حالی که حریم هوایی این کشور نقض نشده بود. بریتانیا از مردم خواسته برای شرایط اضطراری آب، غذای ماندگار و وسایل ضروری در خانه داشته باشند؛ سوئیس نیز راهبرد امنیتی جدیدی تصویب کرده و ذخیره آب و غذا برای شرایط بحرانی را توصیه کرده است. فرانسه و دیگر کشورهای اروپایی نیز حفاظت از زیرساخت‌های حیاتی و توان دفاعی خود را افزایش داده‌اند. با وجود این اقدامات، اروپا رسماً وارد جنگ نشده است؛ اما سطح آمادگی نظامی و غیرنظامی در برابر احتمال گسترش جنگ روسیه و اوکراین و بحران‌های منطقه‌ای به شکل محسوسی افزایش یافته است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23533" target="_blank">📅 17:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23532">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b85e47807.mp4?token=X_6-0_9hLC_NHcwoSDO7wUiOF5ni5ArLqdb5IzLqOHXftntzfrOUnTaTKXGQ4sAbqcsiJiWmesB_AjoA7pVy4qcsO3990JZS-ViOCHO-Y9vJHiE6FSSU9akuwuN2a-bHFI5jhspHKUIjYYvWvfsSLR_KYtSue45YC4R-KZSGVILObedL4fW6GbUthu8ad61Qb0RI096cdeBKMwrs6Dv5Ri2TwRA4cezPsLjeQFKDj3zPDkQJ-RCdGQ_PslODHC12YMJUJDxfQ8OkzlUZd0VM-xt1oRFdKSpHRrQclHgst5rsZWmz_2r7-H-gEpdCnHlKzialVHxZVp4I5tCJ7q30jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b85e47807.mp4?token=X_6-0_9hLC_NHcwoSDO7wUiOF5ni5ArLqdb5IzLqOHXftntzfrOUnTaTKXGQ4sAbqcsiJiWmesB_AjoA7pVy4qcsO3990JZS-ViOCHO-Y9vJHiE6FSSU9akuwuN2a-bHFI5jhspHKUIjYYvWvfsSLR_KYtSue45YC4R-KZSGVILObedL4fW6GbUthu8ad61Qb0RI096cdeBKMwrs6Dv5Ri2TwRA4cezPsLjeQFKDj3zPDkQJ-RCdGQ_PslODHC12YMJUJDxfQ8OkzlUZd0VM-xt1oRFdKSpHRrQclHgst5rsZWmz_2r7-H-gEpdCnHlKzialVHxZVp4I5tCJ7q30jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریادار برد کوپر، فرمانده سنتکام:
ما با تمرکز کامل و جدیت به کار خود ادامه می‌دهیم و با نهادهای مختلف دولت آمریکا، کشورهای عضو شورای همکاری خلیج فارس و همچنین شرکت‌های بیمه و کشتیرانی همکاری می‌کنیم تا
حجم تردد کشتی‌ها از تنگه هرمز افزایش پیدا کند.
این تلاش‌ها نتیجه داده است؛
حجم عبور نفت خام، محموله‌های تجاری و گاز طبیعی مایع‌شده در دو هفته گذشته، از هر زمان دیگری در شش ماه اخیر بیشتر بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23532" target="_blank">📅 16:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23531">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b5c1e187f.mp4?token=hLpkSFyiztaFdKnK3-1rGvdARHBHYu-2DzfoNtQngQFCGZdrbkEhzUeYaPCQuX2ja8aVY-SQU-FqrTg_w8UUFUhxB4Z_F9Y2CeRtHwgOgqc1wzNPQgm6IbStfe-RjgMak6wKRAEjYtrpRB5acdnd8EifvrlWj09L8GqGcH3DwOyrzJhyQEZc1xewrMRAaEUUEMLB8LkZlURZsH21IkqIqCFKQIttmiGUZutchkOEldLpUNh5PMjxtUYiISFUsHwo4OM6ZVl5Bwo0pNaIRrIajYgCLP_drO6LMjN8jC2v1s7UAJEsetnQfHJ4XC_7xmYRp9FrlmWVklBQ60mpsPzyXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b5c1e187f.mp4?token=hLpkSFyiztaFdKnK3-1rGvdARHBHYu-2DzfoNtQngQFCGZdrbkEhzUeYaPCQuX2ja8aVY-SQU-FqrTg_w8UUFUhxB4Z_F9Y2CeRtHwgOgqc1wzNPQgm6IbStfe-RjgMak6wKRAEjYtrpRB5acdnd8EifvrlWj09L8GqGcH3DwOyrzJhyQEZc1xewrMRAaEUUEMLB8LkZlURZsH21IkqIqCFKQIttmiGUZutchkOEldLpUNh5PMjxtUYiISFUsHwo4OM6ZVl5Bwo0pNaIRrIajYgCLP_drO6LMjN8jC2v1s7UAJEsetnQfHJ4XC_7xmYRp9FrlmWVklBQ60mpsPzyXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریادار برد کوپر، فرمانده سنتکام:
نیروهای سنتکام طی دو ماه گذشته از خروج
بیش از یک میلیارد بشکه نفت خام
از خلیج فارس از طریق تنگه هرمز پشتیبانی کرده‌اند. سنتکام همچنین با تأمین حفاظت و هماهنگی، به عبور
بیش از ۲ هزار کشتی تجاری
از تنگه هرمز کمک کرده است.
مسیرهای اصلی عبور در تنگه هرمز عاری از مین هستند
و هزاران کشتی از این تنگه عبور کرده‌اند. بیش از
یک میلیارد بشکه نفت خام
از کشورهای شریک در خلیج فارس از طریق تنگه هرمز صادر شده، در حالی که
ایران به لطف محاصره کامل و مستحکم آمریکا، حتی یک بشکه نفت هم صادر نکرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23531" target="_blank">📅 16:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23530">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خبرگزاری i24NEWS: جزئیات بیشتری از پرونده مرحوم حسین پدران منتشر شده؛ طبق روایت مقام‌های ایرانی، او از طریق واتس‌اپ با فردی که خود را «بن» معرفی کرده بود ارتباط داشته و متهم به انتقال اطلاعات حساس نظامی به موساد شده است.  @WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23530" target="_blank">📅 16:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23529">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حکم اعدام حسین پدران، فرزند حمیدرضا اجرا شد؛ رسانه‌های ایران به نقل از مرکز رسانه قوه قضاییه اعلام کرده‌اند که او به اتهام همکاری اطلاعاتی با موساد و انتقال اطلاعات درباره سایت‌های موشکی و نظامی در اصفهان محکوم شده بود. @WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23529" target="_blank">📅 16:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23528">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رویترز: بانک ملت تنها تحول مالی امروز نیست؛ ترکیه در هفته‌های اخیر تحت فشار واشنگتن برای تشدید محدودیت‌های اقتصادی علیه ایران قرار گرفته و لغو مجوز بانک ملت در همین فضای فشار اقتصادی انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23528" target="_blank">📅 15:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23527">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23527" target="_blank">📅 14:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23526">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝘼𝙢𝙞𝙧 𝙎𝙩𝙧𝙞𝙠𝙚</strong></div>
<div class="tg-text">داداش دیدی شاهزاده یه چیزی میدونست از اعتصاب کردا حمایت نکرد</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23526" target="_blank">📅 14:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23525">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">استوری پدر ریاکار مهسا امینی با پرچم تجزیه‌طلبهای کردستان که خط قرمز ما محسوب میشه. این استوری هم‌اکنون پاک شده. توضیحات رو در وویس براتون میدم. پرچم ایران فقط شیر و خورشید است و این خط قرمز ماست. @WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23525" target="_blank">📅 14:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23524">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363a420621.mp4?token=RQil0y_A2Tkq3vdZMn-ULNGVzOxybAhqgnfPuUgFExINsysEyp1IwzMnR2XP8WJOXhNJy2rSAtEk1k1MowlDtu2RquC51zyjQ8qxOFjS7jMfXJtCnlV7Q3iB7JKkfbXUl9yJYUTmsnbpubAiUM0XeMwJF4LcV1CfhzPXXkmG6Z-wgH62KHyn5XMohYIH48r5xCRYcv0YDFqMmtmfLFf6L5Np3BunNfWxp5CHaRTiYaRoZR5r5mTNjBJD4CxSB3kbfyLEO2_zVFG3gYw5Y6PNVFC33dP62w_7pLKqYZX4-T8MwGZs_yxOxpZ8vQQD3KTRPMFW_fp9k8Um1A-ARGuNDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363a420621.mp4?token=RQil0y_A2Tkq3vdZMn-ULNGVzOxybAhqgnfPuUgFExINsysEyp1IwzMnR2XP8WJOXhNJy2rSAtEk1k1MowlDtu2RquC51zyjQ8qxOFjS7jMfXJtCnlV7Q3iB7JKkfbXUl9yJYUTmsnbpubAiUM0XeMwJF4LcV1CfhzPXXkmG6Z-wgH62KHyn5XMohYIH48r5xCRYcv0YDFqMmtmfLFf6L5Np3BunNfWxp5CHaRTiYaRoZR5r5mTNjBJD4CxSB3kbfyLEO2_zVFG3gYw5Y6PNVFC33dP62w_7pLKqYZX4-T8MwGZs_yxOxpZ8vQQD3KTRPMFW_fp9k8Um1A-ARGuNDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی دیشب رفت تجمعات
😂
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23524" target="_blank">📅 14:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23523">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بانک مرکزی واردات خودروهای لوکس را متوقف می‌کند
بانک مرکزی اعلام کرده است که برای واردات خودروهای لوکس مانند لکسوس LX700، مرسدس‌بنز کلاس S و بی‌ام‌و سری ۷، کد ساتا صادر نمی‌شود.کد ساتا مجوزی است که پس از تأیید منشأ ارز صادر می‌شود و برای ترخیص خودرو از گمرک ضروری است. بنابراین، خودروهای مشمول این تصمیم تا زمان دریافت مجوز امکان ترخیص نخواهند داشت.این تصمیم برای جلوگیری از سودجویی در واردات خودروهای گران‌قیمت و کاهش فشار بر بازار ارز گرفته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23523" target="_blank">📅 14:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23522">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ان‌بی‌سی: مارکو روبیو، وزیر خارجه آمریکا، برخلاف جی‌دی ونس، در طول جنگ از قرار گرفتن در کانون توجهات درباره جنگ نامحبوب ایران اجتناب کرده است؛ رویکردی که ممکن است از نظر سیاسی به سود او باشد. به گفته منابع نزدیک به روبیو، او در تمام مدت جنگ یک «دست پنهان» بوده و در تدوین راهبرد دولت ترامپ نقش داشته است. این منابع همچنین می‌گویند احتمال نامزدی روبیو برای ریاست‌جمهوری در آینده می‌تواند همچنان روی میز باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23522" target="_blank">📅 13:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23521">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حریق در انبار کباب‌سرای محمد در تهران، در خیابان دولت (کلاهدوز)، نرسیده به سه راه نشاط (پلاک ۳۳۵) @WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23521" target="_blank">📅 13:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23520">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23520" target="_blank">📅 13:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23519">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گزارش‌ها از کشته شدن ژنرال فراق العسّار از فرماندهان ارشد حوثی‌ها حکایت دارد. این گروه در بیانیه‌ای از او به‌عنوان فرمانده تیپ یکم کماندو یاد کرده است. العسّار در جریان حمله‌ای در جبهه کَهْبوب، در نزدیکی تنگه باب‌المندب، کشته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23519" target="_blank">📅 13:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23518">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79606f3b2f.mp4?token=EOrO3ySxhipizpEgYm8UliUIuh5MhNOXq2XYtZhI030UxJfxUkC41c3-x9GZcZ8SfXwWP0bB4xHe4qdrUNXrqb5tSXkbXwzWpJT3qNckndZVGS25xdRR9oWXqmGD2rjMzFBVGuePJ44UjaEdy9SV3X506gEhsjPZ3ovCOOHpGWiZSYwMed4GgWIOTttcnLNpKlgumMfQszpufOCI9ncmSPP4pbbPGDOiE55rxNR7BHzLLwIQ4RF5TkOphdGdynnCx3tyTHjlkLbI8ctQ9o25Zm2Dxh9725mtH-PgnOvme9C_SjNoHL9Wk7lIUpNYoQml1a50Ab7AUItP37Z56flBYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79606f3b2f.mp4?token=EOrO3ySxhipizpEgYm8UliUIuh5MhNOXq2XYtZhI030UxJfxUkC41c3-x9GZcZ8SfXwWP0bB4xHe4qdrUNXrqb5tSXkbXwzWpJT3qNckndZVGS25xdRR9oWXqmGD2rjMzFBVGuePJ44UjaEdy9SV3X506gEhsjPZ3ovCOOHpGWiZSYwMed4GgWIOTttcnLNpKlgumMfQszpufOCI9ncmSPP4pbbPGDOiE55rxNR7BHzLLwIQ4RF5TkOphdGdynnCx3tyTHjlkLbI8ctQ9o25Zm2Dxh9725mtH-PgnOvme9C_SjNoHL9Wk7lIUpNYoQml1a50Ab7AUItP37Z56flBYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر پزشکیان: من هم جان‌فدا هستم
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23518" target="_blank">📅 13:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23517">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23517" target="_blank">📅 13:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23516">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23516" target="_blank">📅 13:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23515">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23515" target="_blank">📅 13:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23514">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝘼𝙧𝙖𝙙</strong></div>
<div class="tg-text">داداش یعنی چی که میگی تجزیه طلب
تو حق مردم کردستان رو بده بهشون چرا بخوان جدا شن؟؟
وقتی رضا پهلوی دوم بتونه برابری ایجاد کنه و عدالت ، هیچ قومی خواستار جدایی نیست بلکه اونایی هم که هستن میشن طرفدارش و طرفدار کشور.....</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23514" target="_blank">📅 13:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23513">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromℛℯ𝒷𝒾𝓃 𝒟ℯ𝓁𝒶𝓋𝒾𝓏</strong></div>
<div class="tg-text">وقتی خاکمونو پس گرفتیم توهم تو همین کانال کونت میسوزه</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23513" target="_blank">📅 13:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23512">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23512" target="_blank">📅 12:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23511">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏بهمن کارگر، رییس ستاد مرکزی گرامیداشت «مناسبت‌های دفاع مقدس و مقاومت» گفت که امسال با توجه به شرایط جنگی، رژه نیروهای مسلح برگزار نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23511" target="_blank">📅 12:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23510">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">داداش نگو ریاکار عقیده خودش رو داره بچشو همشریا و هموطن خودمون کشتن</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23510" target="_blank">📅 11:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23509">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗬𝗮𝘀𝗶𝗻</strong></div>
<div class="tg-text">داداش نگو ریاکار عقیده خودش رو داره بچشو همشریا و هموطن خودمون کشتن</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23509" target="_blank">📅 11:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23508">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23508" target="_blank">📅 11:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23507">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الجزیره: قانون جدید تحریم‌های ترامپ، تمدید ۵ساله «قانون تحریم‌های ایران» را تصویب کرده و اختیارات کلیدی تحریمی آمریکا علیه بخش‌های انرژی و تسلیحاتی جمهوری اسلامی را تا پایان سال ۲۰۳۱ حفظ می‌کند. این قانون همچنین ابزارهای جدیدی برای اعمال تحریم و تعرفه علیه روسیه و خریداران انرژی روسیه در اختیار رئیس‌جمهور آمریکا قرار می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23507" target="_blank">📅 11:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23506">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">استوری پدر ریاکار مهسا امینی با پرچم تجزیه‌طلبهای کردستان که خط قرمز ما محسوب میشه. این استوری هم‌اکنون پاک شده. توضیحات رو در وویس براتون میدم. پرچم ایران فقط شیر و خورشید است و این خط قرمز ماست. @WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23506" target="_blank">📅 11:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23505">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c64jmDkTJhbro3pnG6ic0tMDSsLyG7o2hQVlNfCLd_cLRV-ng9nVgrd0b49Q3cdf7vZSierEmwOXXabOPDnYPGn9Mr3rYQpvQDg4n7Y6d9pg2TLyzewA9LS71ouNjLhgqZNDilCEqRpzryhH2MieUtA1rm1QYdZK4p3nqUKVfeXMK1_ikXLULOc7de6n2DTdhyEZeOBfkpz9Q09xEMvGYfKv0szE4WTOBNsxpn6yvHW0PAbOGuPNFgYut_BD7_6j-AM1WGRr34UiUpkpMy03cGpfxxNWyP1HyZUQi6K-yVYZCFU9_mcb_Dpko2d5a9Sx6qcSSa_JShD9CLZqdzK9nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پدر ریاکار مهسا امینی با پرچم تجزیه‌طلبهای کردستان که خط قرمز ما محسوب میشه. این استوری هم‌اکنون پاک شده. توضیحات رو در وویس براتون میدم. پرچم ایران فقط شیر و خورشید است و این خط قرمز ماست.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23505" target="_blank">📅 11:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23504">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هم اکنون تهران ، خیابان دولت ، چهار راه نشاط @WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23504" target="_blank">📅 11:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23503">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23503" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23502">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23502" target="_blank">📅 11:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23501">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc408f38d4.mp4?token=YzGbRYJD6f3eJMyIiXJEkNVAM_tPfESxTMi3WBxROKFsBnHhHbxVI4PK2dNjBiAKOebcykei50bIqDleaHTBiCFv6alQBS-xCh3cLdDp_0pVGc7JurYDtW75iXmq-mIFHaiwnQ7PKPzt3omt1notSmjGxWTWcMffR2FI0GZOBIQFXhkUtzvsP2OQvXAKCQ9hf20-Qm1IwG1PRfkN-kwtYpI9_jVFAmaiiTsq6cwHs06bdWW9Vj40o0dUZsCHHgV65C6EYrPlfhzIkWXoQBYOPNgNnr8EkMxeuYVJ0-6Xpos5hIfToGX22p5HwO2WQeStPFhOl6BCwJiZ_olH4KD96anyMG-obrY4Jeyxl4DnV5IXPNUYr-5yR7bkh04EkHTNxeI5DViO0hFrs8dbpvo9vOZWrVSLQM-Vx_MPty7-SE2BBX8IewRV58KVZoJsXeCyI_w8CLzLLtQMx7C-9tV8z1DXrTN8pFzph6Kvx30Uagi3XbiX5stjLzzeGNCev56ScI5B8KviIFB1XsW7b8tdnMCxi-ocrjQcaqcW4O8PVSbmD24DZ1rWpu6NggNi0van2IuLq7v5aL3dTiJdrs4Z40VQ28M0V6VnwmVmCmTxoMr3ViEU26DvBDpNqpIG9xpWMXbcbQ-8mrReWWPDbqBoU2BN6suinOwp84qV_uzHD2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc408f38d4.mp4?token=YzGbRYJD6f3eJMyIiXJEkNVAM_tPfESxTMi3WBxROKFsBnHhHbxVI4PK2dNjBiAKOebcykei50bIqDleaHTBiCFv6alQBS-xCh3cLdDp_0pVGc7JurYDtW75iXmq-mIFHaiwnQ7PKPzt3omt1notSmjGxWTWcMffR2FI0GZOBIQFXhkUtzvsP2OQvXAKCQ9hf20-Qm1IwG1PRfkN-kwtYpI9_jVFAmaiiTsq6cwHs06bdWW9Vj40o0dUZsCHHgV65C6EYrPlfhzIkWXoQBYOPNgNnr8EkMxeuYVJ0-6Xpos5hIfToGX22p5HwO2WQeStPFhOl6BCwJiZ_olH4KD96anyMG-obrY4Jeyxl4DnV5IXPNUYr-5yR7bkh04EkHTNxeI5DViO0hFrs8dbpvo9vOZWrVSLQM-Vx_MPty7-SE2BBX8IewRV58KVZoJsXeCyI_w8CLzLLtQMx7C-9tV8z1DXrTN8pFzph6Kvx30Uagi3XbiX5stjLzzeGNCev56ScI5B8KviIFB1XsW7b8tdnMCxi-ocrjQcaqcW4O8PVSbmD24DZ1rWpu6NggNi0van2IuLq7v5aL3dTiJdrs4Z40VQ28M0V6VnwmVmCmTxoMr3ViEU26DvBDpNqpIG9xpWMXbcbQ-8mrReWWPDbqBoU2BN6suinOwp84qV_uzHD2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون تهران ، خیابان دولت ، چهار راه نشاط
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23501" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23500">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc97b83ba.mp4?token=pyTkKmQ-jnV9n81D_ROcTSaOEWceji9zo_DvBiZ6aMTkx7wM9FjfXT1a4x3z3qsY_FdaGb68oVV0cWUzL5ZLk9V752tKE4-yb6T-m6wTtMGkBOAOuWXoupsog_lzsx0Pu6u2znfhSqV9t7p7P5U0eFY3blWPa_aEv68yMqUDX0kEIlSaQ-l2UK4tkg9plLqbrEBahLlI1zrlMA3EvQ67wFtiAMfZPT_zS585XJ6W2VfWayBveNYWHZTc5_VtvM1bxcPRpIlgknntVgKMdTAAOiKZh7-ObHo3laKbaNWgVnXrVdRwvBo6jBlp8lp_YgR5I3tfTEHH-embMk7fQ3QkUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc97b83ba.mp4?token=pyTkKmQ-jnV9n81D_ROcTSaOEWceji9zo_DvBiZ6aMTkx7wM9FjfXT1a4x3z3qsY_FdaGb68oVV0cWUzL5ZLk9V752tKE4-yb6T-m6wTtMGkBOAOuWXoupsog_lzsx0Pu6u2znfhSqV9t7p7P5U0eFY3blWPa_aEv68yMqUDX0kEIlSaQ-l2UK4tkg9plLqbrEBahLlI1zrlMA3EvQ67wFtiAMfZPT_zS585XJ6W2VfWayBveNYWHZTc5_VtvM1bxcPRpIlgknntVgKMdTAAOiKZh7-ObHo3laKbaNWgVnXrVdRwvBo6jBlp8lp_YgR5I3tfTEHH-embMk7fQ3QkUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان تهران شمال شرق ، محدوده شریعتی میرداماد ستون دود عظیم @WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23500" target="_blank">📅 10:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23499">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlCGqg2qIU7qOkcuMNzMEDNcQeknrdL4VqMmw7EOLC0KG2-y6oJro32Ob8kOn2C5ZhepIzIxQGHk3zl2C1f7MhBgSDQ63EJNQ_tEdC11rRiU-CXqH5GByi8UJkPHU5FYXhW9hHRjF5_5CEvufjXBiLWE7ACEnV4zQEaKm3zHrtv3qsh9ynyj3KZDOQDb6hB-MO-lvSya5JoGi0UDfsBd701H3Sh8-OkBCNOKAEqzHm1R1xfM-35KhSxx2DFY0hr81HAK9c88MTw1hcBZZtmYBQUH-M9_ZnF_BKSLOzWGoVj8dV-Vz0JHmdG78NjHJrsRB0z2x3WdbjK6Xx1-WRJTSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان تهران شمال شرق ، محدوده شریعتی میرداماد ستون دود عظیم
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23499" target="_blank">📅 10:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23498">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOiHyErfpoA4hBfNfMoegJ1q5BxkvDbb52Yh9bottZI-UdOP9Pv9k7YxgA5rEUWao7VgsuOl9Otf_42WwXgWEZEE2H9JRf7n1XYLA27vKa7yMnlnYxKn4cXKhij3H0fCm01Pc7fU6TGnXno89rpIii13UHbRg5Kcs2s7-0cv8oupuqMHUjqsestJHFJaFfc0JblPkdaYCrzQyLAD-pbJ-cv6s1T6n63y1MSSDTnFandoZEuKeneKSfKdPw3ArPDCAAo6yyY6cAD9d2FcAxUouW7Yvq2swLAFGtGX-MuT5czkpUX9pUwd1RMNzP9Ajy9aTVew5Y9tL8Us04UuPjxLOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن‌ کج بند رضایی: منتظر موشکای با سر‌جنگی ۱ تن به بالا باشید
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23498" target="_blank">📅 10:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23497">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57b8923ab5.mp4?token=s4pHh5mDmSYOmIbshjZcQO6H0rursJ4NAGgN0SXEFprBDzoYJNYkJHRLwR7SrdlB4cUgXo7fPsEHMwohUXwG4x249fxh6ZxEOJEURJYYokz1cjYj_UKiccHVTFGS_M6KSywwKiLVpsf_wDTaeIrb7c8ttHJ1-cYCP02wmXJXpYiBbLyvZbv17_SAjrun-oQf2sS5FkZqBduOzsJZQI03RnlfxgG_McjfyhaO5pNyVrQU_vDlzHkOK0ssRuSkYXRL_10bRWh4wvuUNx8vhHQJLa7n-FvpSg_CRDY1ceDlDqoPytwph7olfWt6UQfeT7_TlqWG2ay9DKbaa-eMCn5B-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57b8923ab5.mp4?token=s4pHh5mDmSYOmIbshjZcQO6H0rursJ4NAGgN0SXEFprBDzoYJNYkJHRLwR7SrdlB4cUgXo7fPsEHMwohUXwG4x249fxh6ZxEOJEURJYYokz1cjYj_UKiccHVTFGS_M6KSywwKiLVpsf_wDTaeIrb7c8ttHJ1-cYCP02wmXJXpYiBbLyvZbv17_SAjrun-oQf2sS5FkZqBduOzsJZQI03RnlfxgG_McjfyhaO5pNyVrQU_vDlzHkOK0ssRuSkYXRL_10bRWh4wvuUNx8vhHQJLa7n-FvpSg_CRDY1ceDlDqoPytwph7olfWt6UQfeT7_TlqWG2ay9DKbaa-eMCn5B-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست درباره ایران: ویرانگری حملات نظامی ما علیه ایران تاریخی و بی‌سابقه بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23497" target="_blank">📅 09:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23496">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ec58e117.mp4?token=q4ZXWNlS261GcIu_Azof2_1Zd7MavsIm9RbmJAMVW49YwvW0z9Fttt-Mesz6LCEE7qHJ3VFx2Z--qHT56cCCr23m1DAoyzY4fpoGPGZgPoBKjtXT_4MXWlz6nVrdOoq0zEN678G8rEK_etIpglumsjcS6nZa83pL89FwDWSuNHXK9_k8mr1Fc3Be0u5wFMoBVnQ3W7Q8tT5q5_ltfZjDqiSdqQm-BV_wjosJXVSjGVgG-YR1PnFf8gSQz2RgnMxk8lXyB-bP1RKyfPwp1hsd-jXoMiB9hXAuc2F4dSKZD5Lbs1xVsF24XotUxyY-bY-ixfG8RdiBYbyCifVkrlzNtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ec58e117.mp4?token=q4ZXWNlS261GcIu_Azof2_1Zd7MavsIm9RbmJAMVW49YwvW0z9Fttt-Mesz6LCEE7qHJ3VFx2Z--qHT56cCCr23m1DAoyzY4fpoGPGZgPoBKjtXT_4MXWlz6nVrdOoq0zEN678G8rEK_etIpglumsjcS6nZa83pL89FwDWSuNHXK9_k8mr1Fc3Be0u5wFMoBVnQ3W7Q8tT5q5_ltfZjDqiSdqQm-BV_wjosJXVSjGVgG-YR1PnFf8gSQz2RgnMxk8lXyB-bP1RKyfPwp1hsd-jXoMiB9hXAuc2F4dSKZD5Lbs1xVsF24XotUxyY-bY-ixfG8RdiBYbyCifVkrlzNtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما در جنگ با ایران با اختلاف زیادی در حال پیروزی هستیم.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23496" target="_blank">📅 09:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23495">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8ba38435.mp4?token=PB8Xe9MlczOmQdn-x5PhDzs9XZlANMvxXs9DOHfH1v9J5fqvLBbH_PhiGQkQB9DZfN3-YAn12eQz4lPrNyHtrO-LdXWYeGym4aTkyDHM7zhRyIRkgNfcFmOultdUeXseoHvqoFkXTfiope-0yoYse6RV1wyUX5VdTEuinlXnVkmNObYrOALpCXEOdkoOtHn3jULJCZOEucu85oYvGb4XzkjPZcL5LWOz9USsG1EuwyEd2YJH4ZCDfhqqrZJSVDnfpYtasRxEDF2ljA6r62ocWbMyoLiuMqno6sBTUIYx_lU_44_CCSu_Bwc2Rv0vKMb8Kpxq1W9CwtRLS2R006DJ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8ba38435.mp4?token=PB8Xe9MlczOmQdn-x5PhDzs9XZlANMvxXs9DOHfH1v9J5fqvLBbH_PhiGQkQB9DZfN3-YAn12eQz4lPrNyHtrO-LdXWYeGym4aTkyDHM7zhRyIRkgNfcFmOultdUeXseoHvqoFkXTfiope-0yoYse6RV1wyUX5VdTEuinlXnVkmNObYrOALpCXEOdkoOtHn3jULJCZOEucu85oYvGb4XzkjPZcL5LWOz9USsG1EuwyEd2YJH4ZCDfhqqrZJSVDnfpYtasRxEDF2ljA6r62ocWbMyoLiuMqno6sBTUIYx_lU_44_CCSu_Bwc2Rv0vKMb8Kpxq1W9CwtRLS2R006DJ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: هفته آینده در سازمان ملل سخنرانی می‌کنید. پیام شما چیست؟ ترامپ: سال گذشته، اپراتور تله‌پرامپتر من را از ورود به سالن منع کردند. بنابراین مجبور شدم بدون تله‌پرامپتر آنجا بایستم. جالب نیست؟ خبرنگار: پیام شما چیست؟ ترامپ: یادتان هست؟ آن‌ها پله‌برقی را خاموش کردند. خوشبختانه بانوی اولم خیلی محکم بود و توانستم پشت او یا بخش دیگری از بدنش را بگیرم. در واقع، دستم کمی پایین‌تر از پشت او قرار گرفت و محکم گرفتمش.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23495" target="_blank">📅 09:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23494">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f409e707.mp4?token=Dc2e71pYiKQ-nS4XyO9Es6QWC7hn9QxprQ6POHBRIog9rY-K34rD6M_Tn7zaXriKDJg1NS1r9LMFLwZiLifPPmmOMPPR7YHjwRD6s16CZA9KgLNFEUCay92hnpP1E7VbI2u9-j4A3jLAf1sm1_SVMmicR0EdG7eLG-IFHeE6iCMi3qX6_tq8YkbL4vHTcZR253KNMjKD--rHc7NAXxsFkuKZS30oN_kigCeG3-Zh4eSO97VYvJeLTFvBDkjWBaMzTGsAlIkJttaXjFeRzw0K2yARoNv_0OBVcJ0HLSiKu9PskNuwGsx21r_3Unx3i-hulZvBNBOgV8qA-3GkPO4FYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f409e707.mp4?token=Dc2e71pYiKQ-nS4XyO9Es6QWC7hn9QxprQ6POHBRIog9rY-K34rD6M_Tn7zaXriKDJg1NS1r9LMFLwZiLifPPmmOMPPR7YHjwRD6s16CZA9KgLNFEUCay92hnpP1E7VbI2u9-j4A3jLAf1sm1_SVMmicR0EdG7eLG-IFHeE6iCMi3qX6_tq8YkbL4vHTcZR253KNMjKD--rHc7NAXxsFkuKZS30oN_kigCeG3-Zh4eSO97VYvJeLTFvBDkjWBaMzTGsAlIkJttaXjFeRzw0K2yARoNv_0OBVcJ0HLSiKu9PskNuwGsx21r_3Unx3i-hulZvBNBOgV8qA-3GkPO4FYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: اگر از مردم بپرسند که کاهش قیمت بنزین را می‌خواهند یا اجازه بدهند ایران به سلاح هسته‌ای دست پیدا کند، نتیجه رأی‌گیری با اختلاف بسیار زیادی به نفع جلوگیری از دستیابی ایران به سلاح هسته‌ای خواهد بود. مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23494" target="_blank">📅 09:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23493">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgjilM4jcPmOXFfMSdNHclnkjDFcV3NwL6d2Zrk12NwnYzk41qXPi48VQzQ9tNEtiIYvgGPCMTLwhlevkaFXzrNMX1uZj2b94jjgrsnooJbER174qJ_VMt9mQTHIMvqq_rn_7na6qmbhaAtcM-d0rC5m9LnauIaRWnTy6ii3uCc52GBJT8_kYu3rHXMsN9CKaYRPQYVry1nJvfqdgeW9MBqfhp1Nzmvs50A3TVcaDX_6Ylh94iuu6xFH3iHvu-iT4lOjyE56ctHp8d4TI3UWuhWF2TNAwfdUc-gy8XCGfUiFIlNdJh2JXJaTaKWin6IuUcS_ZyO_4a_C-QovBF5L1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام
حسین پدران،
فرزند حمیدرضا اجرا شد؛ رسانه‌های ایران به نقل از مرکز رسانه قوه قضاییه اعلام کرده‌اند که او به اتهام همکاری اطلاعاتی با موساد و انتقال اطلاعات درباره سایت‌های موشکی و نظامی در اصفهان محکوم شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/23493" target="_blank">📅 09:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23491">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d34xtGUvCY5RboTsUbbLSnCo_nOFevnWPDU44K8pdEujTNXfDYVSAvS2aHkPKPL_1giSZujLF78EngfgZKXzpDJAXMcKvXgTHOA_f9S9yJcVrxBR5h2pT_MvGIt9mYHxuyXCtBav9SPZYlj242tPtwaBCKUiZrYCgjsUdsvN0xIu7Zaaz75AqVqc16pzIM43lGsfw_HczfKQmok8F2e_G_KnkKPigiGWsMnGeRrl6Eh7z4_GTvFL_UnN-DVb2rvDy3PsBIXcvoR7fftnrzHjJag-1l-wbOJmcbpN9Arx8wjgqdtXnyZMGOIUPJlBsO2xwmaOGx1_cyLyhTaHUCpwPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qu2RkRmN-KJyJrlzs1BmaaCcDBbrQD1yXB893prxcAlqh4phpP9YRUP0Xf9GHy3C8D4E73oZfxaMxel0KtZCYi8sVa2-K1Px9pyC9qokL5YUleTFohEk8d8m73nyLTuAsm46mXwqTuqMc0sFoPWW5vNGyH9-cBv1nRYDdOYTPw7qSyptCLlWlBiIHXCdHPE8OuU9Nhv7t37Fd_GJwR__pO-ru7bFxBUCuxEEsEa9q7WBx-RINZI4ZR-yslMH7wC5zDkryM0D-11VoHWXy31fkZom2kRKTtEY2yc_oyigwAjrnS4A6XKybSoKpoYdatfOq-Ka0dorfxMc_cJB8icyyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پستی در شبکه اجتماعی تروث سوشال، فهرستی با عنوان «۲۵ دستاورد برتر ترامپ در سال‌های ۲۰۲۵ و ۲۰۲۶» منتشر کرد و در آن، از سیاست‌های مهاجرتی، کاهش مالیات، اعمال تعرفه‌های تجاری، افزایش بودجه نظامی، گسترش حفاری نفت و گاز و لغو برخی سیاست‌های اقلیمی به‌عنوان دستاوردهای دولت خود نام برد. مورد مرتبط با ایران در این فهرست، بند ۱۱ است؛ جایی که ترامپ مدعی شد آمریکا در عملیات‌های «چکش نیمه‌شب» و «خشم حماسی»، ظرفیت غنی‌سازی هسته‌ای ایران را نابود کرده تا به گفته او، ایران «هرگز» به سلاح هسته‌ای دست نیابد.بند ۹ نیز به افزایش بودجه نیروهای مسلح آمریکا تا یک تریلیون دلار در سال جاری و برنامه برای رساندن آن به ۱.۵ تریلیون دلار در سال آینده اختصاص دارد
@WarRoom</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/23491" target="_blank">📅 09:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23490">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VL_U4nr3HgbGTShYyH-gOsPzvIr-RL1BO4E5shrbTWzyVwegjTCRLjnaS-nxya-kVrhLTEg7JnSdZgk8LXz9pdea1caPtaz9PSCQi3eeDucaIoQhj_YPQTCUxOLuNtwMMxRZ7hshL5sl0rL54gEidMf0t2I7c5jXkyc1XMvrBoOBXAPK7J9zRaYs7Z8fzc3oPAkGLyF4lmKX5SqTxltfZLGZ3l_1mDazNmGlcydFQ9jV8bElXTzCHDr54stKKqIIWDoS6vbB6NDZh6Ifi6AMGEJQrvFFw2C8MTxMHq2G9ArZ5gJV60FdhR9S8z6lOWVHLTh63wApIxM37n5LbnnLbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیم جونگ‌اون از خط تولید پهپادهای انتحاری یک‌طرفه بازدید می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/23490" target="_blank">📅 09:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23489">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qakvzLXTo5pP35RdB24w5_pA8uryBb1qgpwzxpEJSEAWEsY40g9CAynY35DLMk5rtsy42o9kFmFgI_OVQowt5accqF1Rpu-dvXAdG7qGpVjSF3hVXVb6fhnbwxBOfXkX2ZibCbKF_2MZ12CoCSJYN7Exfqz-Zn_CiEa0GgZCe6Z71ci05Zow2T-Bz2PpmwDzsAYd8ssCrxKmRyVl-8uOleuL5BvED7h0TAXUjPvL-O1U6Jj-XTgzWh6Ee-LG-N9J6HFSB2vWQ94JQA1r90vqHiLcssXsBW3o8xpe_JBML3tzuEN7l9LkuN4ECl5HUvw8mWHsy4_PtEK0T7Fw_cLIVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد ناظر بر امور بانکی ترکیه مجوز فعالیت شعبه استانبول «بانک ملت» را لغو کرد؛ بانکی که صددرصد متعلق به دولت ایران است و از سال ۱۹۸۲ در ترکیه فعالیت داشته است.سازمان تنظیم مقررات و نظارت بانکی ترکیه (BDDK) دلیل این اقدام را تهدید علیه ثبات نظام مالی عنوان کرده است.این بانک پیش‌تر و در پی تحریم‌های آمریکا تا حد زیادی از شبکه بانکی جدا شده بود (قطع دسترسی به سوئیفت و حذف از سامانه انتقال الکترونیکی وجوه یا EFT ترکیه)، اما این تصمیم به معنای پایان رسمی فعالیت‌های آن است.
@WarRoom</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/23489" target="_blank">📅 08:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23488">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08184bf9e6.mp4?token=WSglex7TzHbS_Ylzx8Y3C57_QC12YzQsvyATy5urY3_tHk6ly_wlRzsKB1HYNAIADbr4tnMOPrPRI59nHH9EIndBNO8Fq0b0kiGK2Ik1Fz8kP2TNZ_JEfcK-5tRDWW2UPXR1HP-FAvaU9D-kRrFzcu4mnjZk8Fol00Z5RbrolOdM9qJsNpG-zZONhemYioM6teY2jSnD3vFIT2U-TxT3yt21z89iJJP0ITb0KXEdVv_ayNOIPl0WKBWKxvaR4aMEu85_rTxYz0VMCpmrRg9BD2v-wOAkIhIgEjsdyAfCkvnFb7ZMDbQvREJij52WSbkrqqFuoKjGkC3pu-lSnkQOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08184bf9e6.mp4?token=WSglex7TzHbS_Ylzx8Y3C57_QC12YzQsvyATy5urY3_tHk6ly_wlRzsKB1HYNAIADbr4tnMOPrPRI59nHH9EIndBNO8Fq0b0kiGK2Ik1Fz8kP2TNZ_JEfcK-5tRDWW2UPXR1HP-FAvaU9D-kRrFzcu4mnjZk8Fol00Z5RbrolOdM9qJsNpG-zZONhemYioM6teY2jSnD3vFIT2U-TxT3yt21z89iJJP0ITb0KXEdVv_ayNOIPl0WKBWKxvaR4aMEu85_rTxYz0VMCpmrRg9BD2v-wOAkIhIgEjsdyAfCkvnFb7ZMDbQvREJij52WSbkrqqFuoKjGkC3pu-lSnkQOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست: در طول ۲۵۰ سال گذشته، ما همواره به آمریکایی‌هایی نیاز داشته‌ایم که برخیزند و بگویند: «مرا بفرستید.»
چه کسی با «قرمزپوشان» (نیروهای بریتانیایی) خواهد جنگید؟ چه کسی به نبرد با کمونیست‌ها خواهد رفت؟ چه کسی با اسلام‌گرایان خواهد جنگید؟ چه کسی مبارزه خواهد کرد؟همواره آمریکایی‌هایی بوده‌اند که گفته‌اند: «مرا بفرستید.»
@WarRoom</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/23488" target="_blank">📅 08:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23487">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aq30moLA_7IVa8UHVdwBxJrWKeZeun76uJuC0Go3pph_alC3ygKpxbDhjArvWjANGEIaK9szp-bat21Ud1boSE_jGBI_UoCynUXy0C8NI7U0bh6Hj1HDKV_BhY9Zjj_zsy_Hy2lV-xOei3oKFQGBuIcqJaC18PE2VrBuz-3vzinBFLZcD9YTyYREglaIbXn_7XRrLCQ-TXa0TsbRtTYkSuNPmApXwIE-D0pncEiuvKncOlsM2KV1SLpPLLq9tGfCmHdT_jFdCiBXAnHgngqLXrAZ5Bd0MXe23Nf820sTmPH63Pfr3v5BfngA9UQq81dltR3R4J323_yLN_uqK-mMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون پس از توقف موقت این طرح در اوایل ماه جاری، اکنون در حال پیشبرد برنامه غربالگری اجباری سطح تستوسترون برای نظامیان مرد ۳۰ سال و بالاترِ ارتش ایالات متحده است. بر اساس دستورالعمل‌های جدید، این آزمایش در معاینات دوره‌ای سلامت و ارزیابی‌های سالانه گنجانده خواهد شد و مسیرهای درمانی استانداردی نیز برای موارد کمبود تستوسترون در نظر گرفته شده است. نظامیان جوان‌تر نیز می‌توانند به‌صورت داوطلبانه درخواست انجام این آزمایش را بدهند.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23487" target="_blank">📅 08:42 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
