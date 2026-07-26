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
<img src="https://cdn4.telesco.pe/file/gGqzAfwT_q-OmEUkRMRaUVE7hAV667MKtdi4Z_LS0S4J-0J-gmPaKcgHIVEbI2mmtcJa1KjHQ2W9JH6gwvCuARQt1UN0kBclRMU3u6fRZ-SyT6_XV3N-ojir149mFMr9BWPaQITHvI8b0NZfUT0GJO6Jd3Cd2omQdh9aeq_jTDvQfNySwCy2zaVbWqVe4Pz01Kr_9MxECGJp88YJibIeux4FTF0F3RvNieljWeQorObpFmbTsvzFz6L39rrUWqakfYdSk6l1eFdRbzP9wWmfVlYV55T1dzgA7_5iSJeScCETehwJpRh0NzFpWiiCpiEsX7NiErNIvOTP78kSKctPiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.27M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 13:21:19</div>
<hr>

<div class="tg-post" id="msg-675398">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
سرلشکر رحیم صفوی: نیروهای مسلح ایران معادلات دشمن را بهم ریختند
دستیار و مشاور عالی فرمانده معظم کل قوا:
🔹
نیرو‌های مسلح ایران با بهره‌گیری از ابتکارات جدید و تغییر صحنه نبرد، معادلات دشمنان را تغییر دادند.
🔹
مقاومت ملت ایران و جبهه مقاومت، نقشی تعیین‌کننده در تحولات آینده منطقه خواهد داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/akhbarefori/675398" target="_blank">📅 13:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675397">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIW8xvwI756Y9sPfEwRL6hpmIyDMQw8-e9JFPlVygLoX5h-y-gy1QMm7C5Gg39EBd4iLY-gQ0U1g60stGMyzQUw9FfaXR1k-xq1XvyZf3pDEmbe6yfasHUW8g1Mrb2ny8BInpl4wYK7Vuf_LcW8HuruNoHrie2p3u5_xV0hEvz0aDrHkO9VDOgNOmukHpwtSLPANvW7aGf1zvUbWaorFKAFChSXxpmPHgyF7rDxYVV6-raPKHW9awjgsGcvIMOz-8OY284XBN3K1EUq4s-NKa6GQXTsj1DbhCM8ofTC8rTe0m2w_1szOui5VGhYoy8cfll9JovlI0kNWQiKBE9EX3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع حادثه دریایی در دریای سرخ
🔹
سازمان عملیات تجارت دریایی بریتانیا اعلام کرد که یک کشتی در جنوب دریای سیاه مورد اصابت یک پرتابه ناشناس قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/675397" target="_blank">📅 13:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675392">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arOjLfw3vwJ_glCxMly-w05KiYyY2gvs60SCz5HMd9kiEnlfsZz0vHs5HtgftmeN1iLRFA6uwUG8agIg5ZECYEXdsPqw21DnIkC1xBtKaQcR8eFt2NsI_UP7ftk1kIAFYr9LCL8mqgN_y-AzChkj-gs5kmCXM6WpgxkwZk76ZPGfp-WFRkcluENKigBk-qvv5z5e70JCq1j1fdo-e4afh3vRgJewSYq0zRB7OCQpMIMGUXnaQzsnNVYhZQhaQLkh_ZkN8wvj0WQ3OvKtGwLnwxUgTVAgCBxgzEthNKk9UOW8u63QDX94X16w1HabrqP9fsXMjhwx3WqNgK1usd_EoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_zhSyezgA6_PsZJ2atGRMLg6ckAAljhanShjw_wWTAHIxbc0UxuNMXHxAEHcPLF_9kFZHHbyrPt321T7y3kqi9tetsK7kW0_YN0Pw8eaLoY_qph5LlL-vamWaKuwGqxx0tNslc2UK3364N9OXIkX98lSt_p8seYpnYCnDrFq_JOnuidYz1cAD1QQBV5reTrXQkb416-SkZJnasBqWcxA2FYTJ7KHh_1eTtIk-EyQSGRqObFftltgTlKFK3f2M6xUL2jYmVPdU9_2K9g7J_eyWb2_giyPLMaO9dTq7g3FuxERpYBgid7FH2lSHqYctlkjveQsmcEXDfEH0NEVT55XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xp0QqgC0y2iH_u-aw5WYyB3Pb8RsgaJRTR32B9p6NgAXE-knKzfLqyhEIDB0GTAgigArbGjn9cH2DFe-zF6LtFaEDR1ufpCKfXUS-7scEs8xiD0ozgZk2fYAfAnCmQK-dm6IGezNLyzr6VK83-eSeprVF2pp8YMjC67K-Pn5kN0fXEhqGM34pzYO4Dev_oQ9sUolhBnqpacyp6dMxvCH5YWTCMDZzBT3xRYIJA_WARYe2bQpERX-ZR0CFPIYqQTkjeODd83VYJITDEv2et8AJbQHFO6wU8nKKmbbLpCXuJjFKH8sR2oglccGRiwIpyiU8L89Z1tkjHhTJ0C624oCjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ubIDtp4K71Rh2DnEIYAQPveCPjfA1eQzfRyQEh8L1e0vXR5RTWc1PUw1PqwY99JKJgIq3Kf1t7XEsVuc5xLs7EA5UoqmoITY1kYOTG_hyzYWTTnK-y01FMkcEU0pW5RrJMrbtCh-u_OT6g8dWb4__OTEC4uOZr2UhM5oTkRLSqxK-WdZCcrFdZJm1ZF5NaSi5kpdIBuGpIujC-05zRCf5laLpXG5nKZpgiE7twZGQvfuoh-Z96NX3G1yHnOsTz35rQBuizBnwKKEmjhb4BFwqujUjwH2h0tgKGF5jGT_TK48ZPEEn6DqyKCSz6js7iogJ97wuvsRpTVVuQ_bpzdbZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ve5ydn9n6ky3zEv6yMD2r4HOBfZpVa4n0VPXkohUYWyqzhT_iRG5C254VlCW0QF9BKNMrLR4E9L3PYi1gmG_JG06pxAImAtRfwXhnEBFE52hKvTb8-VlHtOZX9so5h0MU4Tt1SdJzMz2hWCtiWNdEFMUFJBWnmNsQWnTPhjSiF4Xa9ByaaaKYTlccZ4zQsmr27_Wp6fqkw667zzLw6N79QUF3lHs0jWOCXfY8RnWVk0G2T9FluJOtVsEUtQ6QjD8LOBGuFKxIABEV7X491G79_fJ-cvg9KDBXWS29lRuHBHxwgGeyxe6ThgEDyh7xvyMYX3KlZTY7iFwOiCj2wQZqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مقدار دقیق مواد برای ۵ تا ۱۰۰ نفر؛ دیگه نه کم میاری نه اضافه می‌مونه
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/675392" target="_blank">📅 13:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675391">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
آشنایی با خدمات مرکز داوری اتاق بازرگانی تهران
🔺
حل اختلاف قراردادهای تجاری از طریق مرکز داوری اتاق بازرگانی تهران نسبت به دادگاه و محاکم قضایی، مزیت‌هایی از قبیل کم‌هزینه بودن، یک‌مرحله‌ای و رسیدگی سریع‌تر و کاملاً تخصصی را دارد، ضمن اینکه محرمانگی پرونده اختلاف نیز کاملاً حفظ می‌شود.
👈
سایت اتاق بازرگانی تهران:
https://news.tccim.ir/
👈
صفحه اینستاگرام:
https://www.instagram.com/tccima/</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/675391" target="_blank">📅 13:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675390">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
چالش تفاوت قیمت‌ها در بازار لاستیک
🔸
تفاوت قیمت لاستیک در بازار، یکی از دغدغه‌های مصرف‌کنندگان هنگام خرید این کالای ضروری است. بررسی قیمت‌ها در برخی فروشگاه‌های سطح شهر و تعدادی از فروشگاه‌های اینترنتی نشان می‌دهد که بعضی محصولات با قیمتی بالاتر از نرخ مصوب (۳۰ تا ۵۰ درصد) عرضه می‌شوند؛ موضوعی که دسترسی به قیمت شفاف و فروشنده معتبر را برای خریداران مهم‌تر می‌کند.
🔸
برای نمونه، در یکی از محصولات بررسی‌شده، قیمت مصوب یک جفت لاستیک سایز  ۱۸۵/۶۵/R۱۴ از یک برند پرفروش حدود ۷.۵ میلیون تومان است؛ درحالی‌که قیمت همان محصول با مشخصات یکسان، در برخی فروشگاه‌های عرضه لاستیک و فروشگاه‌های اینترنتی تا حدود ۱۱ میلیون تومان نیز مشاهده شده است.
🔸
تپسی‌گاراژ با هدف ایجاد تجربه‌ای شفاف‌تر و مطمئن‌تر در خرید لاستیک، امکان مشاهده قیمت محصولات و خرید لاستیک‌های موجود با نرخ مصوب را فراهم کرده است. کاربران همچنین می‌توانند لاستیک موردنظر خود را به‌صورت اقساطی تهیه کرده و برای دریافت خدمات تعویض به اتوسرویس‌های منتخب مراجعه کنند.
🔸
برای مشاهده قیمت‌ها و خرید لاستیک با قیمت مصوب و اقساطی به
لینک
زیر مراجعه کنید.
https://tapsi.link/rh2g6</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/675390" target="_blank">📅 13:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675389">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPxoS2oeOD8E7i9G_3oForWXJo5Z89wjWAFZxy2v7TuCmtjaOTvY5VC6oESYnD9DcFZUr3FaRTS8MqvZIEN-co_NgpSHrgVyCP46QK-pt_e6w4-AaVqxSvD2GiwS7Foe6uDvLevJ3Drifl4KzycfIGGfo8qASDeCfENYnhOAOzPKzt8FMLNKrcpJybngMw70cDTh97-N9f1z2jxVKKY5AXQUnV8LqhJYak3x9ncKkI9lZLmmDoiPOG6ag9Mv3ORLXtbfWJczxLQklgHz3GJBz4XxJBp9hkgwqkTCUM4kkRO5raYiceWKNI89G3aGZo5nvrPqQV_Y_pGnKES6Ye5Kyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۴ مرداد ۱۴۰۵؛ ساعت ۱۲:۴۵
🔹
امروز قیمت دلار در بازار آزاد با کاهش نرخ به ۱۸۷ هزار تومان رسید.
🔹
همزمان بازار سکه نیز نزولی بود؛ به‌طوری‌که سکه بهار آزادی با افت حدود ۴ میلیون تومانی به ۱۷۵ میلیون و ۸۳۵ هزار تومان رسید.
🔹
بازار طلا هم در مسیر نزولی باقی ماند و هر گرم طلای ۱۸ عیار، روی رقم ۱۷ میلیون و ۹۷۲ هزار تومان ایستاد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/675389" target="_blank">📅 12:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675388">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879cc5a64a.mp4?token=WUcjVoyVmcH747nUJdu_We4wPzNcIf7Sp6l_bRYH6c7tAsN0MFcbUjUeCNPLvsTvHd2qKjtVcQQ9K2Bo2FLKAplfMKYbDthxPg4VSk8SdODaBaHZKEsDR4cj1Vwv_Rj03qAu8i5TEWNgHo7LR78w_GZ5JrmOwt2d4FrIldq7ikPeBKdFRAmRJ83i8qHWKyq92kDL6Bc8Ypt4MP7iA5tuWluonaYSFeKrWz2VG9G7kM7_JuibQSRQMrwGFEXsdMbdhpnFZhAcTCsVu_f8P6SZrzoPLOH7t_RoPHkULx9-mznkSGW49C3sSAzUB4h0FAqGzJiu257hynmCPW2OTnyjfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879cc5a64a.mp4?token=WUcjVoyVmcH747nUJdu_We4wPzNcIf7Sp6l_bRYH6c7tAsN0MFcbUjUeCNPLvsTvHd2qKjtVcQQ9K2Bo2FLKAplfMKYbDthxPg4VSk8SdODaBaHZKEsDR4cj1Vwv_Rj03qAu8i5TEWNgHo7LR78w_GZ5JrmOwt2d4FrIldq7ikPeBKdFRAmRJ83i8qHWKyq92kDL6Bc8Ypt4MP7iA5tuWluonaYSFeKrWz2VG9G7kM7_JuibQSRQMrwGFEXsdMbdhpnFZhAcTCsVu_f8P6SZrzoPLOH7t_RoPHkULx9-mznkSGW49C3sSAzUB4h0FAqGzJiu257hynmCPW2OTnyjfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور امریکایی: هیچ تهدید هسته‌ای قریب‌الوقوعی از سوی ایران وجود نداشت؛ ترامپ آمریکا را ناامن‌تر کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/675388" target="_blank">📅 12:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675386">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aad00d00c.mp4?token=b1XTqxbo6JCHqDNFVxfiX6Z7O6qM188386UECGMcY4J8XvnPrZ6qG3u72OFflbp-sVBbgIoNpFO4LkPOqJpded2AokupqYK-Q4sNAB2DerAlcWPyQs485X8E1F-62xPeIBki_OGlG9U3yuV6HIznvyj3924NQt7pMl1z9d9B2Izh_PUvjBJWMS0Vw0Fk1j3iiuWaRFGEyhAWppomXsrLzFXtMSQHWkZa3oomgJCcmrKS5Dx3GeMpkCQVo0rV0xEL9TWy1qyhRTxcDz09Y0dU2Xb97B-Ymnjurz1MG0uRinoj6_u31jdAC68iId-STmd8OUHJ86XBzgafzR-T7i67ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aad00d00c.mp4?token=b1XTqxbo6JCHqDNFVxfiX6Z7O6qM188386UECGMcY4J8XvnPrZ6qG3u72OFflbp-sVBbgIoNpFO4LkPOqJpded2AokupqYK-Q4sNAB2DerAlcWPyQs485X8E1F-62xPeIBki_OGlG9U3yuV6HIznvyj3924NQt7pMl1z9d9B2Izh_PUvjBJWMS0Vw0Fk1j3iiuWaRFGEyhAWppomXsrLzFXtMSQHWkZa3oomgJCcmrKS5Dx3GeMpkCQVo0rV0xEL9TWy1qyhRTxcDz09Y0dU2Xb97B-Ymnjurz1MG0uRinoj6_u31jdAC68iId-STmd8OUHJ86XBzgafzR-T7i67ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکبر عبدی، هنرمند تکرار نشدنی سینما ایران
🔹
گفتگوی خبرفوری با مسعود ده‌نمکی و احمد مهران‌فر در مراسم تشییع اکبر عبدی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/675386" target="_blank">📅 12:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675385">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQePExA5AiG6Yd35d4b9lmtOu_4tOAUfqEWUIs62Toe_oAf0uBRD_dW6e1fbthMydg9iCdvjYRM1mYV--wFX3FyOLqHWb6MI6PIJdls5vJ_JyIpCaUCIwXj9pHxRoCUu6Ka2TrC4y5l4OWziW00SpefB95f2z3giZ1R6530vLk4TvOwXMxN1tPGLdVRdZ6XqCnL2ITCO6NegzDr0XvD2xANod_iepOGRIMll_PEfBMaSgoCU_RuNZ-a6GBh-myike4qCS9KIuehJItsCFQyI0UDpOM7yJ1ZG_hWjzpOqwQ13qzRFCrm35TsAFCK9ljQ9UZs4XnHcvklc-_YhCWLvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهش ۱۰۷ هزار واحدی شاخص بورس و بازگشت به کانال ۵ میلیون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/675385" target="_blank">📅 12:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675384">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
آمریکا انتشار تصاویر ماهواره‌ای خلیج فارس را محدود می‌کند
🔹
آمریکا با فعال‌سازی «کنترل شاتر»، شرکت‌های تصویربرداری فضایی را به تأخیر یا بایکوت انتشار تصاویر خلیج فارس وادار می‌کند تا مستندسازی خسارت‌های حملات ایران محدود شود./ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/675384" target="_blank">📅 12:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675382">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76665a24b.mp4?token=flGmvvVIV1sEB4yfOm_C3eP05bbpuciz4J_ovon-lq5PrCYfWM0PENdfVUlt1ej2BHTEgpeq2eWXh_WfRoLn6OOal42_Of-wQgZqqu9m8BJKWVSbzFhIchu0cZBggYspFYD_FAE0Y8QNIz8EWkqsUadX38IEm_ci1wy6m4NDVB2R3QUY_Kv2dNKeRo4l0s9tNgHLFR5kJLOysr76Qo0uaPRqeu7yh602sUqeyZ_ru6CR030YN7x2IlNxqPYzaUah7SakPOHINI3duJYGrLYXru_o-XW0yFw7IVm7oD6NV8f8dw3ai-lgSVHCS0sX8KZp6t62yl54bd--M0e_gGu4Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76665a24b.mp4?token=flGmvvVIV1sEB4yfOm_C3eP05bbpuciz4J_ovon-lq5PrCYfWM0PENdfVUlt1ej2BHTEgpeq2eWXh_WfRoLn6OOal42_Of-wQgZqqu9m8BJKWVSbzFhIchu0cZBggYspFYD_FAE0Y8QNIz8EWkqsUadX38IEm_ci1wy6m4NDVB2R3QUY_Kv2dNKeRo4l0s9tNgHLFR5kJLOysr76Qo0uaPRqeu7yh602sUqeyZ_ru6CR030YN7x2IlNxqPYzaUah7SakPOHINI3duJYGrLYXru_o-XW0yFw7IVm7oD6NV8f8dw3ai-lgSVHCS0sX8KZp6t62yl54bd--M0e_gGu4Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر عجیب از سرعت آتش‌سوزی در جنگل‌های اسپانیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/675382" target="_blank">📅 12:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675381">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ایرانی‌‌ها روزی ۷ هزار تن مرغ می‌خورند
مهدی یوسف‌خانی، دبیر انجمن کشتارگاه صنعتی و صادرکنندگان طیور ایران در
#گفتگو
با خبرفوری:
🔹
به دلیل بالا بودن عرضه و پایین بودن تقاضا، حدود یک ماه است که مرغ زیر قیمت به فروش می‌رسد. پس از گذراندن دوره ۵۰ روزه، حدودا از ۱۵ تا ۲۰ مرداد مرغ با قیمت تمام‌ شده کمتری به بازار عرضه می‌شود.
🔹
میانگین سرانه مصرف روزانه مرغ در کشور حدود ۷ هزار تن است. فعلا صادرات مرغ نداریم و به واردات بی‌نیاز هستیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/675381" target="_blank">📅 12:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675380">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e170f357.mp4?token=HSDOm40i_J3IspmZKsu2cDpajt6uKwc-BxokhfpHNnz9Ro8Q4Vr3qDKZJhzu_l1jYUCrYvhgemjktNzdF3xb-qk6Pqa8YShmGS2StyfAzT-ap7sWj5pldpJjk0UJJWsLWGoVXMEjwQ-c9nVbL-k9NUi346sRJ-pUb7R3YiYToazZ2Tf5ne1G0dmb2iVx2MR2_ga_UQeQIJk585X_s6kkUPEhSg509k6qCmYNTI9opbx5GHH_wBRyFEBmCo9thW4EzGGN1rly9_Z4lz5bc6sy5yOQ9vBKY_rRwuTtvw-QFWEmqLxJLLyHQ9h0wwcYHlbsIHIZAJwIJc7Wb5EhsFIdN41YvEhUiQ3Un3L4B617FmrLEOhwdJxqvCPksx3OEuzMHfhpSVtF7vEx4tJthmCWircZH9XriUAKQl2HH-LIG7FZ6Q3YG9HkgLSybPXIm95N9f7v3GBAfjti1NVFY6N7XvOkDB1TeB8b833VFnbTrJAgNAHbInnR6sT4MgTzof92olGwLkmRj7PzZhlT8U5rXbNG3IChGoXI_zayzktVpQCeiOeoPxtsxJl4rYWfb0EF9HjrzXxc10IOT2wBA7sFc3Cr6V9f2CgzxMTEeETHUVQHw7AAzDu33hyEXq8ocDe9AQFsO21bt4bMM09wEzMp7_FWHTG4lOdfsfLlmo3xcv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e170f357.mp4?token=HSDOm40i_J3IspmZKsu2cDpajt6uKwc-BxokhfpHNnz9Ro8Q4Vr3qDKZJhzu_l1jYUCrYvhgemjktNzdF3xb-qk6Pqa8YShmGS2StyfAzT-ap7sWj5pldpJjk0UJJWsLWGoVXMEjwQ-c9nVbL-k9NUi346sRJ-pUb7R3YiYToazZ2Tf5ne1G0dmb2iVx2MR2_ga_UQeQIJk585X_s6kkUPEhSg509k6qCmYNTI9opbx5GHH_wBRyFEBmCo9thW4EzGGN1rly9_Z4lz5bc6sy5yOQ9vBKY_rRwuTtvw-QFWEmqLxJLLyHQ9h0wwcYHlbsIHIZAJwIJc7Wb5EhsFIdN41YvEhUiQ3Un3L4B617FmrLEOhwdJxqvCPksx3OEuzMHfhpSVtF7vEx4tJthmCWircZH9XriUAKQl2HH-LIG7FZ6Q3YG9HkgLSybPXIm95N9f7v3GBAfjti1NVFY6N7XvOkDB1TeB8b833VFnbTrJAgNAHbInnR6sT4MgTzof92olGwLkmRj7PzZhlT8U5rXbNG3IChGoXI_zayzktVpQCeiOeoPxtsxJl4rYWfb0EF9HjrzXxc10IOT2wBA7sFc3Cr6V9f2CgzxMTEeETHUVQHw7AAzDu33hyEXq8ocDe9AQFsO21bt4bMM09wEzMp7_FWHTG4lOdfsfLlmo3xcv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از وقوع طوفان شدید در منطقه روستوف روسیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/675380" target="_blank">📅 12:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675379">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d154d7226.mp4?token=TceW2Wdx0J0tro-LiVYAxUEAy57UlbCATmsCdD3k7Sxci8uZ5A6dU95xcpk9aimkHe60Wy25t8f0M0ARwWwUerJ-sMglkSi0ItVE8yj2jmOhTXjl0ozfnRa7hAYwCx5O_S2ysnlGhYiSNmNMR9MMzm5UsuCm0RQX7Bp2-av6oHi-0By2MVCZ0xsNpE9e3f_vjfnY3cbblnQIh0qWLkSjeZVXTakwLHbVj3H1E2VU3v0BTNN4Rrobggw2Aj7DesixZPKhG1ZoA85U01rQT1yIqWFcnazOpWxU9PYY4WWPc8GVzNy9Jzxzy1DGCyEvS87d1boeWZW_gn2sXMeY3wz8gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d154d7226.mp4?token=TceW2Wdx0J0tro-LiVYAxUEAy57UlbCATmsCdD3k7Sxci8uZ5A6dU95xcpk9aimkHe60Wy25t8f0M0ARwWwUerJ-sMglkSi0ItVE8yj2jmOhTXjl0ozfnRa7hAYwCx5O_S2ysnlGhYiSNmNMR9MMzm5UsuCm0RQX7Bp2-av6oHi-0By2MVCZ0xsNpE9e3f_vjfnY3cbblnQIh0qWLkSjeZVXTakwLHbVj3H1E2VU3v0BTNN4Rrobggw2Aj7DesixZPKhG1ZoA85U01rQT1yIqWFcnazOpWxU9PYY4WWPc8GVzNy9Jzxzy1DGCyEvS87d1boeWZW_gn2sXMeY3wz8gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داروهای روانپزشکی رو باید تا آخر عمر مصرف کرد؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/675379" target="_blank">📅 12:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675378">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxSuvKGTOc5r94WRhMvkTYMGoiowcSevYH63pE-uztyoRiJ1--BKWkYlE0ReUOYNaVd7rtTBwQzdvo7HxWgxpOQh7DyEu860lt6o5ZQwoEom5oUqRa2tuIusAMZPrvCKtghtrYrdftdfvaW6Yb3Zc7MdTKU5U-z0wzEEvUgF4byzQLOCWmHc-gMtUgoL4wvPWklwFLi9s0vjrziSIMyeh2rbxe5UwNwmRbEZDMIoHydLwpZaXUOHvn89GIFFE1SogJG3JGdUpdlbxq8DJoPvlg8k1ox5asGKj8c_pO2bqt5Nle0XyZuTdcM2wXr0hRYy-rMW2gUE843BqwK7W5Wt4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
برسد به دست زائران اربعین
تمام خدمات مورد نیاز شما در یک اپلیکیشن جمع شده است:
🔹
بسته‌های ویژه و پرتخفیف رومینگ (اینترنت و مکالمه)
🔹
بیمه رایگان تلفن همراه
🔹
تامین ارز زیارتی
🔹
استعلام گذرنامه
🔹
خدمات سلامت آنلاین و...
📱
همه در نسخه جدید اپلیکیشن «همراه من»
برای مشاهده تمامی خدمات دیجیتال و خرید مستقیم کلیک کنید:
https://www.mci.ir/-4I2DXIW
https://www.mci.ir/-4I2DXIW</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/675378" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675377">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQh6qzmqWhBo2r3Kx0yxc6uaRd7nZym62orCTLev54Mi-auQccAk7JJipXO9qlE0kN6_O3quObNFAC_Eqb2XgPJw5oPiyRWdvvJ5WFidxqRGMFWAe4Bt3YcRiIvi4JElDn_PLwltsZfsRXgaCnKuRNyvgGaBEhkTtFEULvH3wU9BOCswYrZLlFEEeXjCEdl36i46vR6HshGCLGbZ93F3p_usKyAnRjDOgkI7l175_AKVokN_DH9c2P8FsI35mogSFTzWjHlP4VT9PDlft65EFVgOTqxZCNgVezVYWciPr2i_9v6vqLnmDo_eOZYxLKY6jo2oxoZE_gdK2MT8xkIbDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هاکی ایران بعد از ۵۰ سال مدال گرفت
🔹
تیم ملی هاکی ۵ نفره پسران زیر ۱۸ سال ایران در دیدار رده‌بندی قهرمانی آسیا با شکست بنگلادش، نخستین مدال تاریخ هاکی ایران در ۵۴ سال فعالیت فدراسیون را کسب کرد.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/675377" target="_blank">📅 11:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675376">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
وزیر آموزش و پرورش: سال تحصیلی جدید حضوری آغاز می‌شود
🔹
وزیر آموزش و پرورش شایعه مجازی شدن سال تحصیلی آینده را تکذیب کرد و گفت برنامه دولت و آموزش و پرورش، آغاز حضوری مدارس در سال تحصیلی جدید است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/675376" target="_blank">📅 11:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675375">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
اولین جلسه مجازی مجلس برگزار شد
.
🔹
سخنگوی پلیس: بیش از یک میلیون و ۲۰۰ هزار زائر اربعین از مرزهای زمینی تردد داشتند.
🔹
استانداری هرمزگان:احتمال شنیده شدن صدای انفجار‌های کنترل شده در جزیره قشم وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/675375" target="_blank">📅 11:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675374">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
توصیه‌های وزارت بهداشت به زائران اربعین
فرهادی، رییس مرکز سلامت محیط و کار وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
باتوجه به تابش شدید آفتاب که حاوی اشعه ماورای‌بنفش است، به زائرین اربعین توصیه می‌شود دو ساعت قبل و بعدازظهر حدالامکان زیر نور آفتاب نباشند و ساعات استراحت خود را در این زمان تنظیم کنند.
🔹
در ساعات اوج آفتاب حتما هر دو ساعت یکبار از ضدآفتاب با SPF بالای ۳۰، لباس حفاظتی و ترجیحا روشن که تمام قسمت‌های بدن را بپوشاند، کلاه لبه‌دار و عینک آفتابی استفاده کنند. همچنین خوردن مایعات، به‌خصوص آب و یخ، از گرمازدگی و اثرات سوء اشعه ماورای‌بنفش جلوگیری می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/675374" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675373">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uk0r8Jm1ghtwnotSMB2nU7FxSlcYW06SFUaGdn-oSc595Ci9iewlHuR4Votcu7ONxecNg5eiesaUPAE3axBknd7tlBXnc0sg-C-l4CE_6l09giRp_8pCjMIFHBWAxEZ_d5v20jCJDYnGwbOB08pfAv0yGhWD2YzvfZ-ru-LYZ52RMYopsek0lWEOZSDkfE4JJAlwOJKLnwxbESHtwtMAF_v2wjhknlX7QbGCb70lMeAVNfosw-6U1xuFk8Mv6U6Jz2gYq_5fKGkI3ixYIfSAc5ek2HyS4wxqNNHDehbl2_0iCE7yDQgglQgdqXKWx5wfCoRRp55lJdfAKwq7pf-Gog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده پیشین کنگره آمریکا: جنگ با ایران از احمقانه‌ترین تصمیم‌های سیاست خارجی آمریکا خواهد بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/675373" target="_blank">📅 11:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675372">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
فهرست خسارات بسیار سنگین آمریکا در پی حملات ایران منتشر شد  سردار محبی سخنگوی سپاه پاسداران:  طی ۱۵ روز (از ۱۷ تیر تا ۳۱ تیر) آمار خسارات وارده به شرح زیر است
🔹
در حوزه راداری و پدافندی:  ۷ مرکز فرماندهی و کنترل  ۳ سامانه ارتباط ماهواره‌ای  ۶ رادار پدافندی…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/675372" target="_blank">📅 11:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675371">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
آخرین وضعیت آزمون‌های نهایی در شرایط کنونی کشور
وزیر آموزش و پرورش:
🔹
یک میلیون و ۷۹۰ هزار دانش‌آموز پایه‌های یازدهم و دوازدهم در امتحانات نهایی شرکت می‌کنند.
🔹
برای پایه یازدهم ۶ آزمون و برای پایه دوازدهم ۱۱ آزمون در نظر گرفته شده و این امتحانات در ۵۶۰۰ حوزه سراسر کشور برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/675371" target="_blank">📅 11:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675370">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
تیزر/ مروری بر مجمع سالیانه «وتجارت»
🔹
تیزر اختصاصی شهر بورس از مجمع سالیانه
#وتجارت
.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/675370" target="_blank">📅 11:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675367">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5a04d09fa.mp4?token=pQ0bcbD-ZAm8wZtVhGZZBovSs8vNFg7r1lOds78NOoLQWkJRWu1QCn9KX-k_5yPHF58fGG-Gu3jjTkirncOig3OnXtEeHLkKEYjWS8QT_w001xxvUVV368zkqkRXfwDSxTjBPb6Of_c8Rvg33mnABJrpbf1TmWhXtcCfH0bxRVRJNteqqpH5Vr_dQRCds4pfaOMNCic2S9CmY2xWJzmHfP0Pnai4o7-W3hckg_S-t9_tsEibGE7ViZAxlu4-c23-BS4wcNZ5GtVnam4e5mfEJAcPU9cSIqpedQRTXeu82MbqNXtHkuhsiCH6K1f9o7FaqGSfBD_f8vxe8HoCtbd2Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5a04d09fa.mp4?token=pQ0bcbD-ZAm8wZtVhGZZBovSs8vNFg7r1lOds78NOoLQWkJRWu1QCn9KX-k_5yPHF58fGG-Gu3jjTkirncOig3OnXtEeHLkKEYjWS8QT_w001xxvUVV368zkqkRXfwDSxTjBPb6Of_c8Rvg33mnABJrpbf1TmWhXtcCfH0bxRVRJNteqqpH5Vr_dQRCds4pfaOMNCic2S9CmY2xWJzmHfP0Pnai4o7-W3hckg_S-t9_tsEibGE7ViZAxlu4-c23-BS4wcNZ5GtVnam4e5mfEJAcPU9cSIqpedQRTXeu82MbqNXtHkuhsiCH6K1f9o7FaqGSfBD_f8vxe8HoCtbd2Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های هنرمندان در مورد اکبر عبدی
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/675367" target="_blank">📅 11:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675365">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4a1a32e2.mp4?token=HeygKgpq_aMInyNlPPJB9LoHGnHHhrjy_QlOnpgjqVYMFVMRmOgnkGsSs8CMr4_J_czN6nHvHdHB5ZfDtdzyk1DcRo0EKnjgNDWuj9c897M9LefCcFFCPNEO8IQY_GccbTYi13ss_Lrmy3kaiS0utNmq94tnkDDjEHOwVcCLxj8h87npffmCF5Rvy2l-yUNDkW95hIbVmMxJ1iVZ5XgAm8wnsean19YOg-0UqZ9B0ND44oQWv01PiSB8ng6cJUwIKZdGdUGhlDqRRBU393jYYNASGG2xKzd5EEXOJtvacJxxcS4klDwuvar-a-WhTQ50kCP3ltA18viqbIJhdsLvNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4a1a32e2.mp4?token=HeygKgpq_aMInyNlPPJB9LoHGnHHhrjy_QlOnpgjqVYMFVMRmOgnkGsSs8CMr4_J_czN6nHvHdHB5ZfDtdzyk1DcRo0EKnjgNDWuj9c897M9LefCcFFCPNEO8IQY_GccbTYi13ss_Lrmy3kaiS0utNmq94tnkDDjEHOwVcCLxj8h87npffmCF5Rvy2l-yUNDkW95hIbVmMxJ1iVZ5XgAm8wnsean19YOg-0UqZ9B0ND44oQWv01PiSB8ng6cJUwIKZdGdUGhlDqRRBU393jYYNASGG2xKzd5EEXOJtvacJxxcS4klDwuvar-a-WhTQ50kCP3ltA18viqbIJhdsLvNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های علیرضا خمسه در مراسم وداع با پیکر اکبر عبدی  علیرضا خمسه:
🔹
دیشب در منزل اکبر عبدی، انگار سکانسی از یک فیلم تازه بود؛ باوری که سخت در ذهن یک بازیگر می‌گنجد. بدرود مرد شریف، بدرود رفیق./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/675365" target="_blank">📅 10:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675363">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
صحبت‌های علیرضا خمسه در مراسم وداع با پیکر اکبر عبدی
علیرضا خمسه:
🔹
دیشب در منزل اکبر عبدی، انگار سکانسی از یک فیلم تازه بود؛ باوری که سخت در ذهن یک بازیگر می‌گنجد. بدرود مرد شریف، بدرود رفیق./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/675363" target="_blank">📅 10:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675362">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مدیرکل فرودگاه کرمانشاه از برقراری ۱۰ پرواز فوق‌العاده از طریق این فرودگاه در اربعین خبر داد.
🔹
ادارات مازندران فردا دوشنبه ۵ مرداد تعطیل شد.
🔹
انهدام کنترل‌شده مهمات عمل‌نکرده امروز صبح در پاکدشت انجام می‌شود و صدای انفجار احتمالی طبیعی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/675362" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675361">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
اظهارات عجیب طلبه‌ رزم‌پوش: برخی برای معافیت سربازی وارد حوزه می‌شوند و بعضی هم فکر می‌کنند آنجا بخوربخور است! اما...
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/675361" target="_blank">📅 10:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675360">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
جلسهٔ کابینهٔ نتانیاهو به زیرزمین منتقل شد
🔹
رسانه‌های صهیونیستی گزارش کردند نشست کابینهٔ این رژیم که قرار است امروز برگزار شود، به دستور مقام‌های امنیتی به یک محل امن زیرزمینی منتقل شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/675360" target="_blank">📅 10:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675358">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f95c1cd2ef.mp4?token=ghOuUZFDCr_HUGecYgqf2sHUuJWNWC0f5tw3taXiTNHs4Bv7TCcROStdRhtz4S_rFcWiZmsmJ6FTaGIvdv004A7ytsvClfYPHySTNHU2n3dY2MF04zinx5Y2xG601gd6xx6EbBiqtvepzpG4OM6AKtkquIZARUXG7s3SQ6D2sSMrVKH6oElac-6oB9Ho_qRl86ImCcOjitIdp-NyGSx55KdcefszuXWfagRpi_42r7z_8hH_FKQKhjxqnvQdERtvfd9nqzPjooKF_smsIW8KnjsX6aO8we7H2SFdc4aQQWC-mNIDM0iSvQ-mR1AGZNxXB_nnp9MNzro8sVK4LPaGTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f95c1cd2ef.mp4?token=ghOuUZFDCr_HUGecYgqf2sHUuJWNWC0f5tw3taXiTNHs4Bv7TCcROStdRhtz4S_rFcWiZmsmJ6FTaGIvdv004A7ytsvClfYPHySTNHU2n3dY2MF04zinx5Y2xG601gd6xx6EbBiqtvepzpG4OM6AKtkquIZARUXG7s3SQ6D2sSMrVKH6oElac-6oB9Ho_qRl86ImCcOjitIdp-NyGSx55KdcefszuXWfagRpi_42r7z_8hH_FKQKhjxqnvQdERtvfd9nqzPjooKF_smsIW8KnjsX6aO8we7H2SFdc4aQQWC-mNIDM0iSvQ-mR1AGZNxXB_nnp9MNzro8sVK4LPaGTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همسر مرحوم اکبر عبدی: از این‌ به بعد هم راه او را ادامه دهید؛ ما کمدین‌های خوبی داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/675358" target="_blank">📅 10:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675356">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C66TEd_azc0VENVHGyOMwxXHdqdqQouqWo08njYvfL0z3DVZJmUXH2qKxKpibh8ERUNOguNYgbR3ChA6EFWL3n6ySxvL6lEL_mxnHzzkfx7sjeXtYkMgfDb_1rAvs46H1nwCVZx3P9q2C1Eeasf_fHahgSuyMxQkCXdoZetN3HXvnQF7r3EaNOZdx-vO8SKMvXBfHt1ZP_0Okwj4Ei8WOgHOZby_YzELXQ_OCKafJ9l4L89jbQcTB_opWt5Y1A4gcFvLJAUdoRMUfsJGg1FiJYSNYnj21vGZIiBBG1NMw67IIw2b12Dp_8TTVor3IZQhml_aa4ZJTg8Uwyml00wFNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EESgiFctGeHNmw_QAYnj3BlbM7W7ONabZNN8LTNxtTfSW5s56XazVVBVshB3oh0dtbATIvczUqXOuVu917c-lJvWbLTHjMdS4b65R-xldXkiX84_S3QiZK-7gSVfIRuuPB1s2s04HLso7ZC9NM-Z2FO7avap5jIoSiYJUzu-TWspcbLUeAP1nXfoTuU3ywG33DTjslApNqHHj3DJkW72fGswiHqtCljk31hMWLnR7iowPYk_soop5LUB87jHr4gqp0odnHyjvn2qnajobvtXadag-HUi78IcvNC8iDXPvahgCuPFMfFfP8TRnUxTSoEZRgLYROhZ3v6s02j0im7jXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
برند معروف گوچی از پوشک جدیدش برای بچه ها با قیمت ۸۸ میلیون رونمایی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/675356" target="_blank">📅 10:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675347">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLz_c1MCUrmXBxwCvoVgh0_rnwvXeyX0LuiCy1zIAgQHSm1MsbDNjXlk3r3D8OJRDw4gyC_yCVUbdbH3xTT7EZkgyP6YR8PEcUnRmCl2d8VBQI9m8i0JzzhIjAcuqwDIx_NPH5r70k2XDQgCIhIWGsZ57pciBsE1R3DkRTqDme3TM7iwDfr8QCOAHxNwzg9CeeYkdA-25SfqC2RnzAlxgnVUEfL8QHQQ4SfgEBn4ox2K0sxXQ1HDpLKcbP4Ixu3V2ObuA-9CCMR_TENRSl8i8te15t2QJlYqd_GMi-04SM2E7zAkyKvtVEPjzHt44fo5tjSAK6p8JhHOjKcuEhXKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWkrD0eMUBGdDsnHd6leWSBVLMAm9Dx7c9Ubag7DWFkFpm8tcSg1rab0bmZOM_bxt0hDw69KoRZc4ArfTxEeM1Fa3X-bsEUp7MEs7fS24IXYTXnbiXDZUJyq8url-WHbextwC0Gtmsja7uMfu1fwGGFs3l4vFZbDfzfgiQpViD91RmgDFpy8FswzbFh5WUkzyNAO_Gz2U7VoGV8SkstDD9jVrf9D4k3icQthR0iHJmhsO9E3FDT-ny8trekhMUnNeEWGJUSdDbJMpVyXFP9YmtAtwnfb_K5EapiKmEkLmjh6Yl5hq4epvTmy5Enog6CW6jA7f0LwADLnR0-gdFmj9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_TEuoNMHNjVK4fjyEJy9Zlc6GtGmkCLeQLFfIrZx6lpzbh_gubmW5GVDBscH0QZ7a4yEmx59jacTtWLbRc-121ByKd01114R5u2eB8Y_Ae9zjHMqlx98RjsyVIrUbS9hitSDfbDNMTGGLHvn1NeBlZG9pZDd5--NAbGegBY3ciYwbi2ihu76KlcalILY04TGFl-N-I0ce4W4aVIv71LRIOUpAJBXiWyxOsJdsjTbfVogDawp9OM2gvZEAY_WO0lPTZWkEV35jZm_80hFeXiMZ4MMBYdQQKVCSweBp1iYufXZXlGlmKfcVE-xVAhG0k8stHosR2sQANxFEYVrd6B0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXNqD5tvtP53WjlgY0gGWKjc50V5kwwA98LJ_w47LJnBrT9ZlvSaegJViUlvLldHnsjvHmhh-teQ9qY0DiqxRgJDnovFIQ1sB7GFeRs6YDE6opiOYl2dCBthEY8UBmLQ7C1KrSpsVnj6kn2HSVShDFplN7znX-9gUcwScwUBd0bnkXi4u8ljW8-xEnXQQbSP2jOZMKUzF_tRgB-5iuRdt41MP-xsX30jCtxc9fCN68of-86hTzsnwCa7_aeV43QXrEQIs-WkZuOSlmjHk31e4xTiTxyFdVFMF7zElcy6b64OT970CYXgVa04vZK81NvUXGjNCRuQwOk7-nRMCyvIBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0clBrscCnJObmicLc1ZbmGtHm-MSlRQiK3MxhuOr2XVlBbUmgQ12M1bkM__3piOa9t07eWP28b8J18Ip4kpnfDqceK_0FEh4i4L-wti7GM5FjSVwr2ZXW1GEZdl6WzB_ehwW_3c1agqJCdkP_Uf6eFRGVam3vSg5TIjY4e6wyFy-B8TkQZpH9voKInKN8O6z6hZmzpKk2l-08lznH-BtUTWegEpyLtWwYeX6DbtgxdUE0GKOjso7xxBxqLNsGYXBIG_OWk3-ljL0DDwEKONAVgZkepPxexbkBp6-q6FKv3X8NpqIEYip3hToj8NPS7MaFfA3a68wcGvT-dRHK0QQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkeG3RDYQmOvK1NaCA650PreTf000O0P2EWme_KW-Un3wnHMbjlwhzJHINj0cQ5SDVeMTte-4HCOwp0QkjpmWhvyoK_7XoI0s0TbhfsIEd9WpN5qIFN-SjkhvpGxptGmmWIRy64iiwTu-b9kIzhePtu0XGneUaOFHL8ZfyygjhEVPkdvZEh05nbdAJd2jMP9Rso9JZZ1YYFWge0p6cbPpCYVsi_T4rrwhTAOsIxG9Fo5nacOGGNxINOKcq63Gd52nQ7PVpvfx3TWFhh27oE1oZIg5btDTdWe5CsAhfSU9uwPcCrde8LYvHqoLrEByyN1REWIeREwUpH0yXfBeu4SgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4DcwIlFCz1Tw3_EhdRRqGjbS_GpBc7k3gmntIZk6XDcGqCtSKXjpYKdl7ej--Skv66yiGXEm7wPglCMEEC1EEtY_apwUNjSGgmrB5b6sR2iAgKwlOtqqdcgTi6fD_b2oicYlqE9L7rIlv8jc_JRGgEknaK8_h4mN7E03jYD0mIaywo9Lpenj5w6HAmTXOTKkOh_Y__aiNSfKrxKW3cmNdB9rT11oQOypaMJXHHZdAri8h99RY7eMjowzOiyoYOMOngzg0K2PrtlLI3vB4dr5_YiaDMYMGZd2UxwbyWC0vWBcVXnPDezg9fllEdzwP53TD5Ip_jC1RMO512u4ahvaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qSWqU-CF8eHQ7Ptb-VucU6ERzKDUcmxnb4NDViQyP9031KyZdEMu1Iy6q2cb16bwp2soUwQ7Mh4rwPqQSKSY93dM8mP33yArG25Hk9bWis3neU6JgTX3XzbLDVoDunOJMFSetdoT-W47A9ru5RjMjnUcrv8e5i_dTYPjJuDG6Sjn8MlC61Vdw5TxiQKysOeyGi6vWaA77VstbkY2HXzudGOA4aHubS-Ia4yAAABPAdRIUAHIKMGvryHpjfNda8Dj8wjWcnMR1WwRviiP8vP9dlHPlZsFa0lI5QlVwRipk4EGIQpAmk3hCEr4trOGYvjXmPcVGZKR0v3EvosfrzPgDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jLuQvUC_g0iv187-Z5Nys69R4nE_CQU36UXKZpNXwGuVQFuhFF6IRp3ZyH-RZ5PxToq4CR9hJHMQgyCyggXRrS4MdSS9x1POyII9b5NE8G__BJBSMRB9aLZhDNjDvzj5j9at_Y5RSS7Lg2XrXaHSVwkPUjifQjxU1LuWYkQgoW8Q79ZSRimWkVsutdG7AHAuMUnSQ7yawoq4pfMzFFeYH_KQtW-i6D4hZ126ORtH66Yo128AgRiZ9BnViz13aVWCshMxqaQCydSnB2BiGvutT9CTCerHmx1VFrp5hT2w_mTzvyyl-9ymPyCh93M7J0ksuX3k6PI18nKYCTsXieQ69Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گزارش تصویری محفل شعر شاعران و نویسندگان ایرانی در اربعین به نیابت از رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/675347" target="_blank">📅 10:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675345">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQBmdeHwDXWi0HUnnSljxgSpkXV22UWI3KEW9VjWsBGr0oibedIym1Hok3W18Dd0SSH-Aj-rIHBifgYP3_NDFaDHL8kDDNaBcdnZxs6hsOxCX-HVxj9-_tO-Lwwdptnd9TfutND5_ZtrJ6GFuN1CwzcOhE0soRSv-XwOd9C8FGd1bNcjqAqbG5yabyxujh0EHpXWFaDj8xwhsdhYWJCybeZD_QairNfth27FzKhsUOA8UCMTND9NUfWboQ6-Hk2LZlPp-Y8U4k_sfx8Yjpf-1t3DeJM_cZToERrFIQu2qNYeNfW4btLsxtu2J4Q4aynlVoJvOU9iN6k5RswzV5qi3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fd934ca97.mp4?token=p3z2N7UkpvcBZGpRkhkUsxHsSBlnyOR2R-DF2b9vZoDl4cFsXSH_e2o0taaWW9sCh_SrcHYX47hd3y5d3zvYnH69_cwfJly_cRWVtfUdnIg8V0FmvQCUug2CMIksh4PDgZ4J6tnKlwXTebtdxR6y5-uXQ3xA_awM9YgzR1kxq1RfDZF8zfaMTMdWgEmL1pZKcxK9mDtPZQNTdphFdPzJcZhHobGI7QpZ8Xn-zAl2IXK_wnCppctiu8WKvgeJ6vhhHj5aAd3xA42jlsdhpsi2h1-NHvaildIDYoPZ0Uzphz8bzMta1fb4nweCzW-itDH4HldE4nDxgLMboB-AiW8WpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fd934ca97.mp4?token=p3z2N7UkpvcBZGpRkhkUsxHsSBlnyOR2R-DF2b9vZoDl4cFsXSH_e2o0taaWW9sCh_SrcHYX47hd3y5d3zvYnH69_cwfJly_cRWVtfUdnIg8V0FmvQCUug2CMIksh4PDgZ4J6tnKlwXTebtdxR6y5-uXQ3xA_awM9YgzR1kxq1RfDZF8zfaMTMdWgEmL1pZKcxK9mDtPZQNTdphFdPzJcZhHobGI7QpZ8Xn-zAl2IXK_wnCppctiu8WKvgeJ6vhhHj5aAd3xA42jlsdhpsi2h1-NHvaildIDYoPZ0Uzphz8bzMta1fb4nweCzW-itDH4HldE4nDxgLMboB-AiW8WpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از هنرمندان حاضر در مراسم تشییع پیکر اکبر عبدی بازیگر سینما و تلویزیون
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/675345" target="_blank">📅 10:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675342">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uLqiHp2iNd1ZQpUXJ4xod9tDCw8K1ITNsxfLXXf4CpBa0c7CtlU0s_lvT-AnwMl2X-AtWWi4kkcU5597vqTKXzaWuz4JygF_Bo3RO90-DIKwxfisE_ndkP6RFqPGDrfUgTuCviDx8nqZhUXtTgapqWrzLbMo3xXPHCNS-FpXVlkadlQ0Ok0rZUvffMgos3MdmlghmQ2QwLgekODMgg4SvMdF76bcxo_45844fQsIZG-331B2o7No14G6NN1DuWzuryfpxguz7Nt7qFUH5GS5H9M32TWiXCn4-ycafnzdmCYU02Wb4tjmz71OT_jICa5ubkX35gmhbwuy_FOdZ_2_fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/omtoQrIcjiWx3WNP1Q5_HLSdqpk-CCvhgkAPCpjaookp4OtrqQYRBQHejfE-efQdPWiFt8xIRonfN7FUohrzcaSNDhd7XVmwkY1BRJg784paxsygzTH0qimlDPKzZ5TyCwQtCsoW90mFAH-waY2d0SvoxlYdT74upHiw0xlCGu5QHFPQOHehL4_h_DqNOuk0xFu15yLnxC4ocDU2kBwT76MPEsKNqVnUqqOp5ym9-iYdHFq5RDKHyc9HtRxlosH-CsCTdLjNeLZ3VnuM3_UITLXniRXIp-y61vVMX3hOHK-i6Igpprhl_Db9BO7Uz0HF_QgPwheEBkhV67HAwJbFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVAEMfzFT1WwoK7gT0O1wE7EuUVGVaqfdUPnUqpmu4OqyhXE1jgfsgOTMYrqBREJJ1TZpNFnFQURkKjGV7UnRSHOt4kgnU2n7Ux-SY8VrO2L04EsrvXJ7TSI9sTZVGCYHh28hKBJ4Nxomg2cDnCw3xGPy5FDv7YLVheABIczdjQ0lN24aIbxl7ZnYeEUCxhrYkSpOY4QHtXhBcVJi80A3C7SW5wID0l2RP6ydDiRRWx84s9-h9mLbFCyaEfyW_0nyAMgIm-dzCaZMtxCZWCEuLOcIaT31y2HkWmN-U-zzOLyoW1Htjwm2DM5Oc1CjvI3y50jLtYcCOpPUBh6GEI3Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بنادر کویت و عربستان خالی شدند
🔹
تصاویر ماهواره‌ای نشان می‌دهد بنادر کویت و عربستان کاملاً خالی شده‌اند. یمن تأسیسات نفتی عربستان را بمباران کرد و نفتکش‌ها گریختند. مقرهای آمریکا در کویت نیز هدف حملات ایران بوده است. از زمان لغو تفاهم‌نامه، کشتی‌ها به‌تدریج کاهش یافته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/675342" target="_blank">📅 10:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675341">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
دبیرخانه شورای عالی فضای مجازی، خبر مصوبه جدید برای برخورد با بلاگرها را کاملاً تکذیب کرد و اعلام کرد که جلسه این شورا بیش از یک سال است تشکیل نشده و چنین موضوعی در دستور کار نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/675341" target="_blank">📅 10:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675340">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
در ۲۴ ساعت گذشته نیز ۶ کشتی پس از دریافت اخطار قاطع سپاه، مجبور به لنگر انداختن و پذیرش دستورالعمل‌های ایران شدند
./صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/675340" target="_blank">📅 10:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675339">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd39b62ba.mp4?token=iUm3cB0TbobsMSkhj_Kg3TTVFvdTbJM7MpET9Rzu_NW3vAPZe5ESbRFsYdRFVbg3J8DfS3J5RN5iE1msZZF43bSMVNRI0HJblrf6e-oZH_BhnVtNA3VEhPXvat_r37Lv1yB-NSFnNer904cIDrdTu9hoM1aSAt27eOssyGkMQb9UVdEMFDy0rXMIqrnRbC8A2ZoCcIO6nTOgI7qRfhxgk3yF-DRFF8-FImEZ-scRIS_i4rYtVi0pRRTnnz2kpeCdb-YshNpoD6Dx7YY8fIIRs5SI-qdl-gCpBO-25TMiaWh0IYyhp_Ptx5IKpQwzghHtMoEvFaUOrisd3fo8TpIdKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd39b62ba.mp4?token=iUm3cB0TbobsMSkhj_Kg3TTVFvdTbJM7MpET9Rzu_NW3vAPZe5ESbRFsYdRFVbg3J8DfS3J5RN5iE1msZZF43bSMVNRI0HJblrf6e-oZH_BhnVtNA3VEhPXvat_r37Lv1yB-NSFnNer904cIDrdTu9hoM1aSAt27eOssyGkMQb9UVdEMFDy0rXMIqrnRbC8A2ZoCcIO6nTOgI7qRfhxgk3yF-DRFF8-FImEZ-scRIS_i4rYtVi0pRRTnnz2kpeCdb-YshNpoD6Dx7YY8fIIRs5SI-qdl-gCpBO-25TMiaWh0IYyhp_Ptx5IKpQwzghHtMoEvFaUOrisd3fo8TpIdKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کوکوسبزی رو به سبک تبریزی‌ها درست کن و از طعمش لذت ببر
😍
موادلازم:
🔹
تره ۲۵۰ گرم
🔹
تخم مرغ ۳ عدد درشت
🔹
آرد ۲ قاشق‌غذاخوری
🔹
نمک، فلفل، زردچوبه، پودرسیر و پودر پیاز
🔹
گردو و زرشک
🔹
روغن باید داغ‌ِداغ باشد #اشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/675339" target="_blank">📅 10:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675338">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb7c984de.mp4?token=S8MQ5N6Vi_-IH41F5yVngOkDTFSZiEUT4orp6Iz9s96KnFGvvLWEImPAhy27tokdygIg1N-dKBQ7BtuFWpRCHubWamNVP8dYn_v2Ws9ud4dhzCUUoSBxonobJxT7fe7NcuC4C_A5FHTQvSuJpwJcMuEXL6nt4CvVliM3XvHQSkEsAvFDZN5_JyfojVGJsUjxogA3qfmXOnVbPOeOPDcqrwp_NfiV5oBfr55BG41C0S2uYELtdQ--Ea8U8NYwpK7ZMBREFVj18f7qerVd25txzFMUBSBdJqwScdUoAMTsoYtV4DxowkQ6GQqDi2TbtQabDVSoIVTh47-yMtwAir6COg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb7c984de.mp4?token=S8MQ5N6Vi_-IH41F5yVngOkDTFSZiEUT4orp6Iz9s96KnFGvvLWEImPAhy27tokdygIg1N-dKBQ7BtuFWpRCHubWamNVP8dYn_v2Ws9ud4dhzCUUoSBxonobJxT7fe7NcuC4C_A5FHTQvSuJpwJcMuEXL6nt4CvVliM3XvHQSkEsAvFDZN5_JyfojVGJsUjxogA3qfmXOnVbPOeOPDcqrwp_NfiV5oBfr55BG41C0S2uYELtdQ--Ea8U8NYwpK7ZMBREFVj18f7qerVd25txzFMUBSBdJqwScdUoAMTsoYtV4DxowkQ6GQqDi2TbtQabDVSoIVTh47-yMtwAir6COg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت شاعر «میدان با تو، خیابان با ما» از خلق این اثر حماسی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/675338" target="_blank">📅 10:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675337">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74fc712a0b.mp4?token=dUAzisFAVqM523oCd2KbvqmNxZvjPTGIahYkHFV6eDfjcjsNOSFdOyIfFGL3yZlR_Bba5QS8sDM3LfEcbveEThHDfMp6uTh2dYFmT8ZxogB30UWOaYnOlsAw6z4B3dNJsC_QzpuGUGkZ6CnBfIC9iLAYfY6L0DdzvsyTMEPo7SGVCZn2Ve9T4VPqJw53BIBKsLh1yb-eUXxP5GFWlmH32Q9CIXAmgFshNiO6W7bHb-0GP5f98WksNGVyBsBmB7W83OUmjVc4iRQquXFsP0O0AOrHo68yTCRzcLECIP0l2HVSUNuGvw1pzBEpbAwxPlEyYQ-LSpLbJroo1m9BLsO2NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74fc712a0b.mp4?token=dUAzisFAVqM523oCd2KbvqmNxZvjPTGIahYkHFV6eDfjcjsNOSFdOyIfFGL3yZlR_Bba5QS8sDM3LfEcbveEThHDfMp6uTh2dYFmT8ZxogB30UWOaYnOlsAw6z4B3dNJsC_QzpuGUGkZ6CnBfIC9iLAYfY6L0DdzvsyTMEPo7SGVCZn2Ve9T4VPqJw53BIBKsLh1yb-eUXxP5GFWlmH32Q9CIXAmgFshNiO6W7bHb-0GP5f98WksNGVyBsBmB7W83OUmjVc4iRQquXFsP0O0AOrHo68yTCRzcLECIP0l2HVSUNuGvw1pzBEpbAwxPlEyYQ-LSpLbJroo1m9BLsO2NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصاویر از تشییع پیکر اکبر عبدی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/675337" target="_blank">📅 10:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675336">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
فینال جام یوفا، ۱۹۸۹| گرم‌کردن افسانه‌ای مارادونا؛ شاید زیباترین قاب تاریخ فوتبال
🔹
هنوز بازی شروع نشده بود، اما مارادونا با چند لمس توپ و با آهنگ Life is Life، خاطره‌ای ساخت که از نتیجه مسابقه هم ماندگارتر شد.
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/675336" target="_blank">📅 09:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675335">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
شیطان زرد مدعی شد: توقف موقت حملات به معنای عقب‌نشینی نیست و در صورت شکست مذاکرات حملات به ایران خیلی سریع آغاز می شود
/ ایلنا
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/675335" target="_blank">📅 09:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675333">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/719dbea7f0.mp4?token=eOFjWImiccV0p0SDnIbN4TkHP0wbLObUzUqLNvth8IJp4-jGgjIfSt19bEDzTow8xfkLGUmXsGmZqC17R93sQU5qB5MkY2jTD6MU9GlJkoZSlk_qss3nsC0IDOyBuHRH42-xp-EDmpxh-1d1Bcfhu2jSr_WPq7SUBgFvDVQ3qqRmeZ5vg1SWmGBuSOx4KY6olu8A2s-eMM-2de01Yf-nyWpG3341V9gE0t3lrzPQ6Wqepat1X9UIIZ1qMjqb3NpT3ZgtkooTW5uKZqimCbeZpVlKttzyo836SKTYAXeelwcetBH0BUeL0jeNuPhjzgGo_V7gB87j27QRFsy2h81ftw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/719dbea7f0.mp4?token=eOFjWImiccV0p0SDnIbN4TkHP0wbLObUzUqLNvth8IJp4-jGgjIfSt19bEDzTow8xfkLGUmXsGmZqC17R93sQU5qB5MkY2jTD6MU9GlJkoZSlk_qss3nsC0IDOyBuHRH42-xp-EDmpxh-1d1Bcfhu2jSr_WPq7SUBgFvDVQ3qqRmeZ5vg1SWmGBuSOx4KY6olu8A2s-eMM-2de01Yf-nyWpG3341V9gE0t3lrzPQ6Wqepat1X9UIIZ1qMjqb3NpT3ZgtkooTW5uKZqimCbeZpVlKttzyo836SKTYAXeelwcetBH0BUeL0jeNuPhjzgGo_V7gB87j27QRFsy2h81ftw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر اکبر عبدی ساعت ۹:۳۰ صبح روز یکشنبه، چهارم مرداد از مقابل تالار وحدت تشییع و در قطعه هنرمندان به خاک سپرده خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/675333" target="_blank">📅 09:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675332">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b220fadc5.mp4?token=hrRkQCfbZdaf4GLEWBUp7U5YdyA6-ch1bL5hHR23j7x9dCYhql51uoxMTq_a7W7AI-QCv5iOfyEbvaE8-ohqsk8qEkFMZtOCLbDz1RzofxExKSPoZGMKKPA3at-rwKynJ3765wvbJ67USIDB9JBU_LHOkQgn3vI9Xg9SfRTYn9ThBIH7_VB8eLY3DJpJmTPpBWcVA5eGFAnQxwesy7KP7M101c6nAPRQu1AiE1qyY9oh4EVwC7SUyHUdxeQYvOtdA63Fyh42AsFV6fPScb8mFXD5hNl6jgPerOEwPY0n7akdgUKva2JzvxKwF8PIMqF_Hmqoz_GwqwsWo5j0d6cdX1cGuyiwG4j2u3fKq0fcpARPMfLsmw6qSGku3R81p2d6pKkPMW16E2TFlbqKvPeONPr9XOUO4WhRs5pgT6otvEc7bgodk5QX7KFWeKiwX9h-KFNpheFXmtrEx2R5u2dtiffIAL0bafN5d8tovQb7n15My-IJmKhtCd8nnU1EY6H0766_xaVQ1iJgY7ST3UfClRbkmC_dWM61sx6qdZnJNoQOD58f0gzSO8C_eaSDsx1zdxIq3oUt-LSreSPwgCbV4Chtp4t-DlxFKUdPVM1g4oBvqYpqU4xlpKtw9hcJgvmJIv8Zfq6HEIpPkgCMSFZifHIC4zQW3l4KKmzYPk6_J68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b220fadc5.mp4?token=hrRkQCfbZdaf4GLEWBUp7U5YdyA6-ch1bL5hHR23j7x9dCYhql51uoxMTq_a7W7AI-QCv5iOfyEbvaE8-ohqsk8qEkFMZtOCLbDz1RzofxExKSPoZGMKKPA3at-rwKynJ3765wvbJ67USIDB9JBU_LHOkQgn3vI9Xg9SfRTYn9ThBIH7_VB8eLY3DJpJmTPpBWcVA5eGFAnQxwesy7KP7M101c6nAPRQu1AiE1qyY9oh4EVwC7SUyHUdxeQYvOtdA63Fyh42AsFV6fPScb8mFXD5hNl6jgPerOEwPY0n7akdgUKva2JzvxKwF8PIMqF_Hmqoz_GwqwsWo5j0d6cdX1cGuyiwG4j2u3fKq0fcpARPMfLsmw6qSGku3R81p2d6pKkPMW16E2TFlbqKvPeONPr9XOUO4WhRs5pgT6otvEc7bgodk5QX7KFWeKiwX9h-KFNpheFXmtrEx2R5u2dtiffIAL0bafN5d8tovQb7n15My-IJmKhtCd8nnU1EY6H0766_xaVQ1iJgY7ST3UfClRbkmC_dWM61sx6qdZnJNoQOD58f0gzSO8C_eaSDsx1zdxIq3oUt-LSreSPwgCbV4Chtp4t-DlxFKUdPVM1g4oBvqYpqU4xlpKtw9hcJgvmJIv8Zfq6HEIpPkgCMSFZifHIC4zQW3l4KKmzYPk6_J68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناریوهای احتمالیِ آمریکا در مقابل ایران!
اکرمی‌نیا: ما برای هرکدام از این سناریوهای محتمل آمادگی لازم داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/675332" target="_blank">📅 09:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675331">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
امیر اکرمی‌نیا: زیرساخت‌های آمریکا در اربیل تقریباً به‌طور کامل نابود شده است
سخنگوی ارتش:
🔹
پس از نقض تعهدات توسط آمریکا و تلاش برای ایجاد مسیر جعلی در تنگه هرمز، ایران در چارچوب تفاهمات پاسخ داد و پایگاه‌های آمریکا در اردن، کویت و بحرین را هدف قرار داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/675331" target="_blank">📅 09:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675330">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWoyK7jkDpDsMlRc64GB-hrzafvffuQIFWgZj6jg81m86HrAerUlZusBTuTvhAi_5WyrX_-Ctz_h0UCpiyMXK7a8mE3gwfOuVuXAXG_qGn8NQ-l7PBzFo5zqc9d8plhIGLLe3HZ3zFvG63CXsDsSvBkaWUSEI6QChP9Yjd4E5aVf_CbrccSO-qMErqV_ShW3aQMH7DD45TVb_8AVkh0ldBrOJP57F-kv73FJh1wk9o6gaMqvEAQeyrHH67B44u_A3Jtmc8ZdTJmdJlVWHY2LVAqzuvTfIRUEhbiZdSffgJ4YYh5W2HUU2STJcgwiJXBZ31ts1a3jBI6eWT4AC6LygQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ۸۱ هزار واحدی شاخص بورس
🔹
شاخص کل بورس در دقایق ابتدایی معاملات امروز ۸۱ هزار واحد مثبت شد و به سقف کانال ۴.۹ میلیون واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/675330" target="_blank">📅 09:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675328">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1756a5af24.mp4?token=jke1B6H41ExBK460zKtxgZEm8VE1hrzgU7VRWksChUAOJkVL66l0CqXqP0cv_MjpJvHsC0RuzTmFAqJnZLQgnP9yw5Er31yx7N3RQgDyfFTeM1JDzITbsQAwERowt-8CFYODPEfbdhBR8MMQWfcdxeqA2Y4yDbvrjyDiuc9VSzUnmst3w_WJYlwEyNJLx6_0FXw48U52rhNkE_6-JCirb01OoLAE0gnxXD3qY-dzUR23MlF8gGfyck7u2gGu2m_kYW1pR63ojz1s0YFSUUi39YuWJFFNWAckKVuQLInbxk9ylL1GYipaNS6YZPAMDqiDXkIHmbOGJsKXt1dExKcUboc29bu0jNEIIPTqG3RzFD0J4VMOmbtFbDyY3wf4E2cgUCt6klBoZJZG-km4_ZO49cJlHuAM1ipV3Jy-7TK6hv7CuO3RxYUZcm5pI2jgzH9aIrvMX8kPgxgnR5Fm-8HiGadDjihB9MF0IjsP-dldmADwkdg5DNeq7c52TUvL0_24A3uCZwCKM7NDSxIVmhuYGFp_UxCZpiMXjtgUcTMX5HW9gi1SNytOEmjDaLx9bIsIpy-zbEHWuWSbZbYrsfjO8g3EnBkT0u1LtKjKDMJlFuhtarHBbXavHhEg_xLdxGeM_DF__jaGdxsO5rRbdT7Kmf1P_eTrltgmdXNlGkgzUKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1756a5af24.mp4?token=jke1B6H41ExBK460zKtxgZEm8VE1hrzgU7VRWksChUAOJkVL66l0CqXqP0cv_MjpJvHsC0RuzTmFAqJnZLQgnP9yw5Er31yx7N3RQgDyfFTeM1JDzITbsQAwERowt-8CFYODPEfbdhBR8MMQWfcdxeqA2Y4yDbvrjyDiuc9VSzUnmst3w_WJYlwEyNJLx6_0FXw48U52rhNkE_6-JCirb01OoLAE0gnxXD3qY-dzUR23MlF8gGfyck7u2gGu2m_kYW1pR63ojz1s0YFSUUi39YuWJFFNWAckKVuQLInbxk9ylL1GYipaNS6YZPAMDqiDXkIHmbOGJsKXt1dExKcUboc29bu0jNEIIPTqG3RzFD0J4VMOmbtFbDyY3wf4E2cgUCt6klBoZJZG-km4_ZO49cJlHuAM1ipV3Jy-7TK6hv7CuO3RxYUZcm5pI2jgzH9aIrvMX8kPgxgnR5Fm-8HiGadDjihB9MF0IjsP-dldmADwkdg5DNeq7c52TUvL0_24A3uCZwCKM7NDSxIVmhuYGFp_UxCZpiMXjtgUcTMX5HW9gi1SNytOEmjDaLx9bIsIpy-zbEHWuWSbZbYrsfjO8g3EnBkT0u1LtKjKDMJlFuhtarHBbXavHhEg_xLdxGeM_DF__jaGdxsO5rRbdT7Kmf1P_eTrltgmdXNlGkgzUKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سازمان ضدجاسوسی آمریکا در خدمت کدام رژیم است؟
افشاگری جان کریاکو، افسر سابق سازمان CIA و تحلیگر سیاسی:
🔹
سازمان سیا کاملا برای اسرائیل کار می‌کند و افرادی مثل مایک پمپئو در رأس آن است که از صهیونیست‌های سرسخت به‌شمار می‌رود!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/675328" target="_blank">📅 09:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675326">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_JIJWvj7UMgL2JuQmSFF_ez5RDLtX4pCTGcOSrwuhSLnIg-jJRSQ3ZyWrY6FRqS5Japj7ABuIFeHNtup9OFTeCb8_eFkaQkXUsVhF2sa63TS_wsydIj5_GkYUdxornQojbZG9hHgSNCLdcPurr2JzVKHAtnCggbu76BQPyK_29W7uEYOR0zLZidezxotac0Gmq6UpbWbeamgVKevJDU-Ze79luVNx0j_bMllpBvVqDGbV8sasn27uov20F_6IGqzX1bKpdXmO89847_WCVhtOjRXc-IXKp7iq1Dyf0hNs6eadPj02sSVhQ0VaCaGD4k5CBdk3JmntCx9GXqy7faHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دارندگان سند تک‌برگ زرد بخوانند؛ آیا باید سند خود را تعویض کنند؟
سخنگوی سازمان ثبت اسناد و املاک کشور:
🔹
اسناد تک‌برگ زرد نیازی به تعویض ندارند و معتبر هستند.
🔹
تنها اسناد سبزرنگ صادرشده پس از ۳ تیر ۱۴۰۳ مشمول قانون الزام به ثبت رسمی معاملات اموال غیرمنقول هستند./ میزان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/675326" target="_blank">📅 09:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675325">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84fcb8b82c.mp4?token=QZtTrzTXxVqIZ9Tv1PxqXMQjR7LdxEWSoYIO_sJImZh8QpHDQ2-5kNSCIdejAhCFlxJvlNmZkGHioi4E0gs-uWHxk_W3sOCxdDFbjntMjHmXj5Wu-ZMCeXHSqyE7tHwKaJ_mJ-lk9aIaC20qWd5SCkpN66mobRXT7Ybb3t413sgtp50LZfEIubiBqAW_zDis7rT6lLlnlXq9LfIKJ1gBsFud1zzNKw-rXZnLb9qvF2DZoDMzUmj1u0CA8de-r7MO2wV9ShTOpO_1Fy4C6p9BxWUQXc5E5SsJH5n4kMukJtuKsJcl2LwRkCIRkvR1ooTZAiRd1KZfpHcgllQaHenttg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84fcb8b82c.mp4?token=QZtTrzTXxVqIZ9Tv1PxqXMQjR7LdxEWSoYIO_sJImZh8QpHDQ2-5kNSCIdejAhCFlxJvlNmZkGHioi4E0gs-uWHxk_W3sOCxdDFbjntMjHmXj5Wu-ZMCeXHSqyE7tHwKaJ_mJ-lk9aIaC20qWd5SCkpN66mobRXT7Ybb3t413sgtp50LZfEIubiBqAW_zDis7rT6lLlnlXq9LfIKJ1gBsFud1zzNKw-rXZnLb9qvF2DZoDMzUmj1u0CA8de-r7MO2wV9ShTOpO_1Fy4C6p9BxWUQXc5E5SsJH5n4kMukJtuKsJcl2LwRkCIRkvR1ooTZAiRd1KZfpHcgllQaHenttg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگ‌ترین اشتباه والدین با یک گوشی شروع می‌شود!
🔹
گوشی همیشه مشکل نیست؛ مشکل وقتی شروع می‌شود که برای هر گریه، بی‌حوصلگی یا ناراحتی، اولین راه‌حل باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/675325" target="_blank">📅 08:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675323">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLTSGm8D0Rns3d98PkW149UMeImvefR7Xn1ObKl6wIwuqVddD_DQ0f6AodjpWJCdnidvFmuJz4tdFxBPNfcQCyQoirlkGSjBf0v7dOwImZVQb3dMBPcoSIZhOxDtlFQFlJItR-6EIhzAmflwolebN84fPmTIIN98L9N-k3Nc1MmpbybAlrP7-AkkHVLJhQQI3qV4cofQKwpXM0l3MrRT7als1bXKEx0xUnXOBb3XclAdOZ5_a-NEdsLMlNY3f-OdU8xDdE-eWBrOH2UumM2vsf9rKmRrzAyNfb9sXnYjVfUW6d7fLEY_rZtfDdOBL8mAlrGLJMyCzpOOu3dTI2BpQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخستین عکس ثبت‌شده از سطح مریخ ۵۰ ساله شد
🔹
پنجاه سال پیش در چنین هفته‌ای، کاوشگر وایکینگ ۱ ناسا با فرود موفق روی مریخ، اولین عکس تاریخ از سطح این سیاره را ثبت کرد. این تصویر که چند دقیقه پس از فرود گرفته شد، نخستین نمای مستقیم بشریت از سطح یک سیاره دیگر بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/675323" target="_blank">📅 08:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675320">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZaWSaIcFzBujhvZQc3bjsd22mOw8aCylLYoMtB8Axw7pU5POyUGrBAn3dxPajIbABmqQN_2bdmBjod9CwrRmQUl6k_AjOfP9CPoj2CJ6k4k5me_12ttCKW3qjlcFCGy4hp5_VkhrmEKHg1ISRm1a7iScKeIgqGbv9mHtdRBNVV8_zzJ8AZhVWaxH19CpxRNXJ40ikFR9_VL2-JazoyyBkC4cxbKRzWWhecsuQYZj4rLfYSi8xAYJFnPRUl7rttbp7unaLzQBhM9rrZRsD-aLWUwOUkO0ytAGSl7-fdtW9NcPT2BBGXWi8e68waXpGvdWW4Y2KU0ijnLCIf_ENnvvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محاصره دریایی ایران همچنان ادامه دارد
🔹
محاصره دریایی و مزاحمت برای نفتکش‌های ایران ادامه دارد و شب گذشته یک نفتکش دیگر در مسیر خروج از آب‌های ایران متوقف شد.
🔹
همزمان، یمن به آرامکو و پایانه نفتی ینبع حمله کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/675320" target="_blank">📅 08:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675319">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ec9d1cd3.mp4?token=l3078TwGMhwnw_M23z1TwkGbItDJl7OZKmEUEnAclH-ryeYNquq0cjfKCeIkEvBpyW9mpW4ESNdQbx3cwAV465KB7GtpSlGkESqekGExLuIdndg_6WbpgcsxJLD9N7F0M1HeNeHgMhSC7717LBSJaR2OUj_poI73WGstLGhdBCcK2K2L0wGNg8HbK3CNLBXQQL1S5szLRsk0bPKtNdnuKWbI5aHWbOJXrCElf8gatoiiwXH7ExLji0kl6Mxgfuuo98QWcXYfBFhfRqsgmiQE-oxsLWKVo97lmnDDw2Op6sfQ7vX5VA5CrPXVZoz0gpD_7rfc6VQLAtpoFqozcveKAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ec9d1cd3.mp4?token=l3078TwGMhwnw_M23z1TwkGbItDJl7OZKmEUEnAclH-ryeYNquq0cjfKCeIkEvBpyW9mpW4ESNdQbx3cwAV465KB7GtpSlGkESqekGExLuIdndg_6WbpgcsxJLD9N7F0M1HeNeHgMhSC7717LBSJaR2OUj_poI73WGstLGhdBCcK2K2L0wGNg8HbK3CNLBXQQL1S5szLRsk0bPKtNdnuKWbI5aHWbOJXrCElf8gatoiiwXH7ExLji0kl6Mxgfuuo98QWcXYfBFhfRqsgmiQE-oxsLWKVo97lmnDDw2Op6sfQ7vX5VA5CrPXVZoz0gpD_7rfc6VQLAtpoFqozcveKAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه فرم زانوهات طبیعی نیست، فقط با ۵ دقیقه تمرین در روز اصلاحش کن! #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/675319" target="_blank">📅 08:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675312">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWQbpuj7qZhEkZU4wUaQunzG_XqWeaC05RNMNkOkJvU-v8hYVg06FNVlso0ngea9d0rcLz6wujcja3BLNuwcjrTqIkxkbsgVbyS6HT6rjlQ1w_a2QH8dT8ZuFkTVgZ8MWs81d66NGhZruVlVpYy-OB8qoJaad-Iwm19ZvPqxF_oaSOYQB7IxPGBsjhiLfghkDyJ-YInLgfm69nvRMQuT-blAw2HxzA2f9W6q91TR4riGq6b51YfKiByIru8Iq7BVum5n2KVYTuaRvOJSXMBrRtYeGey9SO1iAT67-rTZE8vyEMD-36804_vkWmG-arTRQmKNvtoTg6Z9gr3QW-bKbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۴ مرداد ماه
۱۱ صفر ۱۴۴۸
۲۶ جولای ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/675312" target="_blank">📅 07:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675311">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شرکت آب و فاضلاب: جیره‌بندی آب در دستور کار نیست
🔹
ادعای سی‌بی‌اس: گفت‌وگوهای ایران و عمان درباره تنگه هرمز پیشرفت داشته است
🔹
جابجایی رایگان زائران اربعین حسینی از پارکینگ‌ها تا مرز شلمچه به وسیله ۲۲ رام قطار
🔹
زلزله‌ای به بزرگی ۴.۶ ریشتر بردسیر در استان کرمان را لرزاند
🔹
سفیر کویت در آمریکا: «ادعای مشارکت‌ ما در عملیات علیه ایران دروغ است»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/akhbarefori/675311" target="_blank">📅 05:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675309">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNmM9grNEEu1uY2pppF4yljxoyCE6U50BBhd3pWrpmJVGoRlyJnm57h8pw51bPsoIB6kGNMDYIaWoFzbASujrJyWbk-Fmp-pIj-YOdYFmxWErQ0wkAvNISsTSJHwKIDMOw4rs_XyQXMeDhS_d577sANXcsCUR435Hn5vhcx9FquPTOHEqX7Rgr7PAsK7K3s05iYsQJDLGyDtLW8HafOazl4vhrBdJw3kb_IzbKeEqYskgxkOR5cEPo8prkU9w9oPgT_K5s1BoPzWkGM_tW37pGv-hkxG5icsVcVSN7IVRvoCgJsVjyB5hRir1UPHDKPaIdDFOizdTRVw1idkjb8saA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر فروشگاه آنلاین داری، این پست می‌تواند هزینه تولید محتوایت را نصف کند.
قبلاً برای هر محصول باید:
❌
عکاس می‌گرفتی
❌
لوکیشن پیدا می‌کردی
❌
ساعت‌ها زمان صرف می‌کردی
حالا کافی است یک عکس ساده با موبایل بگیری…
رقبایت دیر یا زود از این ابزارها استفاده می‌کنند؛ سؤال این است که تو زودتر شروع می‌کنی یا دیرتر؟
@digitall_cast
ارتباط با پشتیبان :
@Digital_cast_support</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/akhbarefori/675309" target="_blank">📅 04:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675308">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
نیویورک تایمز دلایل اصلی توقف حملات آمریکا را فاش کرد
🔹
روزنامه نیویورک‌تایمز به نقل از مقام‌های دولت آمریکا گزارش داد که ترامپ، دست‌کم در مقطع کنونی برنامه‌های خود برای گسترش عملیات نظامی علیه ایران را کنار گذاشته است؛ زیرا تشدید جنگ می‌تواند ذخایر موشک‌های رهگیر پاتریوت و دیگر مهمات پدافند هوایی آمریکا را در غرب آسیا به سطحی نگران‌کننده کاهش دهد.
🔹
موضوع کاهش ذخایر تسلیحات دفاع هوایی تنها یکی از عواملی است که بازگشت آمریکا به عملیات گسترده نظامی علیه ایران را به اقدامی بسیار پرریسک تبدیل کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/akhbarefori/675308" target="_blank">📅 03:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675303">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d261d61d47.mp4?token=qZhC2M702THPAUcI3YiSaocPgj5b6YRtELJ-vQ53XuBo1FLzmV-DHlQg9egM5-JERXF9SlsW7M0QmL9AlmRKqDXjMLjjOzPNz-Wu8V_F_XM2ShzYA4S-Qol1JyBSc7rJcI-SdrglfknJWH7P8A9Ho4afQIHxz7Rpy3uPGwJiEZwC3GuMOz1C2Z4ZV5s-dIlUNTtXGVXpfk6eZbaIHyX9uj9AqSDuGwDCaeUuEGosJ1EloWLZoZNxNVigko7UgVIETY3x_W1wmht85mZAJcEYG8oKjAKCWqGxJl-Jl98S4CrnBRzKQmQPfm2o2K9X15RI9Oj0vK003lhtJVY639pkeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d261d61d47.mp4?token=qZhC2M702THPAUcI3YiSaocPgj5b6YRtELJ-vQ53XuBo1FLzmV-DHlQg9egM5-JERXF9SlsW7M0QmL9AlmRKqDXjMLjjOzPNz-Wu8V_F_XM2ShzYA4S-Qol1JyBSc7rJcI-SdrglfknJWH7P8A9Ho4afQIHxz7Rpy3uPGwJiEZwC3GuMOz1C2Z4ZV5s-dIlUNTtXGVXpfk6eZbaIHyX9uj9AqSDuGwDCaeUuEGosJ1EloWLZoZNxNVigko7UgVIETY3x_W1wmht85mZAJcEYG8oKjAKCWqGxJl-Jl98S4CrnBRzKQmQPfm2o2K9X15RI9Oj0vK003lhtJVY639pkeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک سرباز کویتی که از شاهدان عینی حملات موشکی ایران است، می‌گوید: موشک‌های ایرانی بدون هیچ تلاشی از جانب پدافند آمریکایی، به هدف خود اصابت می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/akhbarefori/675303" target="_blank">📅 01:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675298">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515003979a.mp4?token=I0GessnClZlXLWwaLGj_3pSsdU9PcniJaHPwSFPKQHWoV5ZH2V6LkBDTWY9goVYKaABkwGhpmcELHEX9XWmlRBLv_wSMjDqClYuNytMuTk1sh3xvmGBdV0ZWS0gCr29W1Q-RWjzc3ouqi4KQgyIRgk-9_h2Qy1yXUV1zkp6nPTzB-f1j0PUrGjqeoMbP1zoZEP67OKzWoutEe3o9e-cEQRhVTrjFaW8Q4A-jie4mWZnQQPA3eiZ9XHbd9v6W5T6N2ai3FmpfbTWRvm_rLfQIwZUModSgfpixZ0LZurcvVJTEj2TPOkuHXaIjqg8lkWFMj_1OBBc0lBkA2e_BHyPNTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515003979a.mp4?token=I0GessnClZlXLWwaLGj_3pSsdU9PcniJaHPwSFPKQHWoV5ZH2V6LkBDTWY9goVYKaABkwGhpmcELHEX9XWmlRBLv_wSMjDqClYuNytMuTk1sh3xvmGBdV0ZWS0gCr29W1Q-RWjzc3ouqi4KQgyIRgk-9_h2Qy1yXUV1zkp6nPTzB-f1j0PUrGjqeoMbP1zoZEP67OKzWoutEe3o9e-cEQRhVTrjFaW8Q4A-jie4mWZnQQPA3eiZ9XHbd9v6W5T6N2ai3FmpfbTWRvm_rLfQIwZUModSgfpixZ0LZurcvVJTEj2TPOkuHXaIjqg8lkWFMj_1OBBc0lBkA2e_BHyPNTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری‌هایی بین نیروهای یمنی و گروه‌های وابسته به عربستان سعودی در استان الجوف در یمن رخ داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/akhbarefori/675298" target="_blank">📅 01:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675297">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ادعای سنتکام: محاصره دریایی آمریکا علیه ایران همچنان به‌طور کامل برقرار است
تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی آمریکا (سنتکام):
🔹
۱۲ کشتی تجاری را که تلاش کرده‌اند محاصره را دور بزنند، تغییر مسیر داده است.
🔹
۲ کشتی را که از دستورها تبعیت نکرده‌اند، از کار انداخته است.
🔹
۲ کشتی دیگر را برای اطمینان از رعایت کامل مقررات، مورد بازرسی و توقیف موقت قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/akhbarefori/675297" target="_blank">📅 01:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675295">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533ce86674.mp4?token=fpxJJ5zoTixTPeHo_coSumC7RA7BMRsQ1oQ1bRN55DglUozDBBqtlwhuEykl825OF-66iEA54XUvx1axNccEGsK1x65EDFgZwZnvkDjwGiJO9j9PmLwa0VwDyh3urWLZ8-MZ75b16l6ZI6-4ktwmhlYeFWGSNmWqVLMFM8QCjP2lRND7IpXAOHMyQ_6nTdHk90DPqVRInfpAMRf9xhWzte7YSgUjoSGT8jolzzgHYKcRVh-IQPDPgTcJ0KLkMc0rD8Kq62PKnVbh2Uy1i2vy3inZYe6x2PWkwB6JqBrwp_PFSEXP-LgluvMix5ELj6jzMk9et7s5z6xLkE1FZ54L3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533ce86674.mp4?token=fpxJJ5zoTixTPeHo_coSumC7RA7BMRsQ1oQ1bRN55DglUozDBBqtlwhuEykl825OF-66iEA54XUvx1axNccEGsK1x65EDFgZwZnvkDjwGiJO9j9PmLwa0VwDyh3urWLZ8-MZ75b16l6ZI6-4ktwmhlYeFWGSNmWqVLMFM8QCjP2lRND7IpXAOHMyQ_6nTdHk90DPqVRInfpAMRf9xhWzte7YSgUjoSGT8jolzzgHYKcRVh-IQPDPgTcJ0KLkMc0rD8Kq62PKnVbh2Uy1i2vy3inZYe6x2PWkwB6JqBrwp_PFSEXP-LgluvMix5ELj6jzMk9et7s5z6xLkE1FZ54L3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ۴ سرباز به هلاکت رسیده جدید آمریکا در جنگ با ایران  سی‌بی‌اس:
🔹
یک سرباز ۳۰ ساله آمریکایی آخر هفته در عراق در جریان آنچه آمریکا انفجار کنترل‌ شده برای انهدام یک پهپاد تهاجمی اعلام کرد، به درک واصل شد.
🔹
پنتاگون اعلام کرد گروهبان مایکل امانوئل سوینتون…</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/akhbarefori/675295" target="_blank">📅 00:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675294">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1059e02fca.mp4?token=Yx4hdrY8N0irTNQTRmImdUCUw_dmT5WVKIx7GjQ-_gmpWpUS7jDyvSokP4g4s6T2kvev1LmFLYPoLmNMJKaTvWf4MeuGssufReJg7RCYBlUK20x09ej7c8EE7DTxo8UOzLzfnYX174iQXtmBODcXF3RRGkydgG2n9O65WNlt3zH5vpdCqMNWuS5xeBCX-g7kwQVXXUeTwSJC-1XXDfi69FBe-OwC8ycIDhL0z9Bh27MIsPmT3mdtMFxMngHVRbToXHCeDrK_sGvXTZpbdnufC4H_k4tiaPhMeqAPY9XACFgl4gBlOLw7vLclkRdnqnDYW-6yPVBOFF5e6dl8NB_PQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1059e02fca.mp4?token=Yx4hdrY8N0irTNQTRmImdUCUw_dmT5WVKIx7GjQ-_gmpWpUS7jDyvSokP4g4s6T2kvev1LmFLYPoLmNMJKaTvWf4MeuGssufReJg7RCYBlUK20x09ej7c8EE7DTxo8UOzLzfnYX174iQXtmBODcXF3RRGkydgG2n9O65WNlt3zH5vpdCqMNWuS5xeBCX-g7kwQVXXUeTwSJC-1XXDfi69FBe-OwC8ycIDhL0z9Bh27MIsPmT3mdtMFxMngHVRbToXHCeDrK_sGvXTZpbdnufC4H_k4tiaPhMeqAPY9XACFgl4gBlOLw7vLclkRdnqnDYW-6yPVBOFF5e6dl8NB_PQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعلام وضعیت اضطراری در برلین در پی حمله با خودرو
🔹
در پی زیر گرفتن مردم با خودرو در برلین، وضعیت اضطراری در این شهر اعلام شد؛ گزارش‌های اولیه از مجروح شدن ده‌ها تن حکایت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/akhbarefori/675294" target="_blank">📅 00:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675292">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40532c012e.mp4?token=Bdw3BlebjSDQCPZ5jYCGgcwoKJVWA7ygQ7JWtdw2FEhQK_GGCWVehwrsaNK7jRZac8MWLsluFgZqrv9gwricrZ72_3KBZRnn_chC5VABAFQx_ZsAighSSIEsGpKLm1O9zsIXKXOuneAICZUYpQk6TN5jCsW84Kn_pnejuQw7yEcjwL4gII9t_MTrhrp1MNL7uQQG7GObL9S0KQ9eHsKA2XDUpg1Z9XmaQ7b4z40PmuV4zDAEBqwEd-mxFdSfpXtd90yII4eGj16Z_cz0azVYzZNvwVsDUS7OYiL7gZIsIHfupPzN3rE9YxW4XO7aGVa8yGkviILsNYzqyWFvOTbScg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40532c012e.mp4?token=Bdw3BlebjSDQCPZ5jYCGgcwoKJVWA7ygQ7JWtdw2FEhQK_GGCWVehwrsaNK7jRZac8MWLsluFgZqrv9gwricrZ72_3KBZRnn_chC5VABAFQx_ZsAighSSIEsGpKLm1O9zsIXKXOuneAICZUYpQk6TN5jCsW84Kn_pnejuQw7yEcjwL4gII9t_MTrhrp1MNL7uQQG7GObL9S0KQ9eHsKA2XDUpg1Z9XmaQ7b4z40PmuV4zDAEBqwEd-mxFdSfpXtd90yII4eGj16Z_cz0azVYzZNvwVsDUS7OYiL7gZIsIHfupPzN3rE9YxW4XO7aGVa8yGkviILsNYzqyWFvOTbScg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از انفجار کرکوک در شمال عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/akhbarefori/675292" target="_blank">📅 00:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675291">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6552d0ad6.mp4?token=htQeoAunFp27tD3yDo4-HG1Jj624WuWxPsKVkUbM-OsLwBkqJALq78_lPvGzwTNtpepJ6cdPdl6Fn8Z4ZoFbzpn9_JEN-eMuL9JjAq4qaJSJOXX60_MbhaWX56Fln4O0yg7E9f4yCpKtWahk26ZV4gm2D7l1QEiMOIs9w_fWuygaP9lOFTXzr-tC8VPc7_ZsdhzvvltDaCElrMvi9VU4255BjWue-xFVrYJT2LIbnhyX7Cux5-fGG4sIISpGMNIH9bZLUN2c_RGaUSyWkAZ3KUg1e6gRgG_ToS4JdhrompxxQH0-uHMB7p8AkGshtm2JwlhEnz6-RZMp1f5MuFjbtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6552d0ad6.mp4?token=htQeoAunFp27tD3yDo4-HG1Jj624WuWxPsKVkUbM-OsLwBkqJALq78_lPvGzwTNtpepJ6cdPdl6Fn8Z4ZoFbzpn9_JEN-eMuL9JjAq4qaJSJOXX60_MbhaWX56Fln4O0yg7E9f4yCpKtWahk26ZV4gm2D7l1QEiMOIs9w_fWuygaP9lOFTXzr-tC8VPc7_ZsdhzvvltDaCElrMvi9VU4255BjWue-xFVrYJT2LIbnhyX7Cux5-fGG4sIISpGMNIH9bZLUN2c_RGaUSyWkAZ3KUg1e6gRgG_ToS4JdhrompxxQH0-uHMB7p8AkGshtm2JwlhEnz6-RZMp1f5MuFjbtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت پدیده نادر «شبح بروکن» در روسیه
🔹
در کوه‌های اوستیای شمالی، سایه یک انسان همراه با هاله‌ای رنگین‌کمانی روی ابرها ثبت شد.
🔹
این پدیده نوری که «شبح بروکن» نام دارد، زمانی رخ می‌دهد که ناظر از بالای کوه به پایین نگاه کند و سایه‌اش روی مه یا ابر بیفتد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/akhbarefori/675291" target="_blank">📅 00:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675289">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
احضار کاردار موقت اوکراین به وزارت خارجه ایران
🔹
به دنبال اقدام مجرمانه ارتش اوکراین در حمله به شناور تجاری ایرانی، کاردار موقت این کشور در تهران از سوی دستیار وزیر خارجه احضار شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/akhbarefori/675289" target="_blank">📅 00:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675288">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd_Wqjt4JRhRxFc_nDMXsTDcq9uHGDNHywbl88cA0eJpHtshyyRC91mGyyK2Mkfoni0QtEnNnzi5Ov6Hm10BFpMUEHbxlhuddqHAzUqD2iWM9EgZdTGzqPvl-I_DsKxW8z1nhCB4kCqER2ogdnAG57D0p1SrQ2HN0N1Zk5WGGqxgmCZeZMcqvNxwG8s4DjtEdCbFLjF-lFQDQ6JJCYyVXsEkw0cSuaS_SdAxtjxbeH9UAsIpET6SKYvoDOPUG6m3nYA7PVsM_tdTp5LtjxnfFK92pSe5jLHuP-jlvAotBV8CNMry24cIN0dSWM1TF5h2TxdLIAUE_Rw92Kv-XxikJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زلنسکی مدعی شد: روسیه به ایران در تصاویر و دیتای ماهواره‌ای کمک می‌کند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/akhbarefori/675288" target="_blank">📅 00:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675286">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdBDB1_EgPKt4kiYp28Paio8_A2Uhho5QBYSY5V1eG2nReVf6YzvW7M6KfVoyjZKpuEmTkdhur_VArdCTfMJHwJKA3xsZrnDGpBinLjdfy3b_oV8Yl9J-s33YKn45heNGgqjjRjm-n5qWdEVjNpwOivPD1WWBZn_C1ksApPk4fvGP0EpTTcxYcVlZUlk7CT2fesbuvniR0deJVNPir9Y1OG9HscCqtZpPlwdq-lRLOE4OZJqKFlHsP_CdHPze-FwAPwR7J8lrMdeHn5oUso0tHMvaYRPZjXxkCb9Yox7c45P-WRgwciOvGZ9ETsf_1zUHLOJ4bFqNkCBYtjZestxEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عروسی قرن در راه است!
🔹
رونالدو و جورجینا در ۱ آگوست رسماً ازدواج می‌کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/akhbarefori/675286" target="_blank">📅 00:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675285">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDVnCfD0InQQrhP3jBclQHHF6eu--1216-W_b66ch-90O4npe994Y4QKN3q_o5QGILN7g_XMPyvOoPQL3bhpveP0rhnQ1lfpPEf_fWYwwPsNgkiwto7oLiNLwbljRcoRwM8tYcNEwCv1PFCq45kYFKg75l-HQJQg_6r6TNUtXULgU2xDeReiQZ9pKuaJEozjeX-Hd6RVbGCeddP7YwrGlUK24ZeCeRHgYqXiPPn7SnxfBaaGqiX9KckjI8Sk1geOY7bSTZLrb4QAlmGTzrV5Jmigfb6l8tmKpK8FF1EdPRnHra3MTjgt0YatsB-IKlrIkfHOBSAebuHgbxT6W3l2Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/675285" target="_blank">📅 00:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675284">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=dMJvlN17xpPxMD0ruzIOMU_QU7TEohf9ZWc1uPLhOR1EuXiMBkENGviY8EP-oZHqEZm8LajrniDppPGNgBmroIhFv1k8YiL8qbHYL-Flq9qMS2U4_WHXTe8vpt7Qhjo0uaL84sNuVCABlaIs15UKoEP8BA4n1DqFI08P-UfXNCmwuJfvUoXIv4gb4my-mAgpSxdyN1hqQnU9eJWI4HVi_L0MTLyynSyYhcgXuXJf00t0KyBP_O6yUeNCjpEgw-BkZCbAlf8cd0XnsQ7S5YMDCGo8ACZynRZ1OZP2MKcYlqOgnAACxkjMx_qVoiNs47bevUGzyOCgdeUzQOZ-QfYcYGbwA5vbUA2ybqNawhyx5wxC9qhGdXhxsdge2pDdzJTfXN7niQeMuk4xBF_bg0VskCbsI8WLgw8Sa2ptFycIyQA_wK1hNg-IqTM56zXMq41EZwqsekgb_BTuSPf7s_FSWNtXNEYT3dQAOlPHzcnYTCgU5aGyPeMxMVo4395ZtNFCcY6ayyzwvw8aA1WZuHfIGm7S8EBpiZyWtNYgpe7JfOV_IsCVvzpLNKDjKsDoUYfcyangSg6yGBTGe4h5uI2H1z7Gc49Auh5CEzTzryeYQQObmUzYEGRKDx8YoG48cDJ12-bQcSLtEkT8E5JbBhVCfA0tSgJGOzz9taTB1yEcb7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=dMJvlN17xpPxMD0ruzIOMU_QU7TEohf9ZWc1uPLhOR1EuXiMBkENGviY8EP-oZHqEZm8LajrniDppPGNgBmroIhFv1k8YiL8qbHYL-Flq9qMS2U4_WHXTe8vpt7Qhjo0uaL84sNuVCABlaIs15UKoEP8BA4n1DqFI08P-UfXNCmwuJfvUoXIv4gb4my-mAgpSxdyN1hqQnU9eJWI4HVi_L0MTLyynSyYhcgXuXJf00t0KyBP_O6yUeNCjpEgw-BkZCbAlf8cd0XnsQ7S5YMDCGo8ACZynRZ1OZP2MKcYlqOgnAACxkjMx_qVoiNs47bevUGzyOCgdeUzQOZ-QfYcYGbwA5vbUA2ybqNawhyx5wxC9qhGdXhxsdge2pDdzJTfXN7niQeMuk4xBF_bg0VskCbsI8WLgw8Sa2ptFycIyQA_wK1hNg-IqTM56zXMq41EZwqsekgb_BTuSPf7s_FSWNtXNEYT3dQAOlPHzcnYTCgU5aGyPeMxMVo4395ZtNFCcY6ayyzwvw8aA1WZuHfIGm7S8EBpiZyWtNYgpe7JfOV_IsCVvzpLNKDjKsDoUYfcyangSg6yGBTGe4h5uI2H1z7Gc49Auh5CEzTzryeYQQObmUzYEGRKDx8YoG48cDJ12-bQcSLtEkT8E5JbBhVCfA0tSgJGOzz9taTB1yEcb7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگر قصد دارید سفر اربعین را با اتوبوس راهی مرز شوید، پیدا کردن بلیت را به سپاس بسپارید
🔹
سامانه پایش آنلاین سفر (سپاس) با اتصال به همه درگاه‌های رسمی فروش اینترنتی بلیت اتوبوس امکان مشاهده و مقایسه ظرفیت‌ها را در یک سامانه فراهم کرده است تا سریع‌تر و آسان‌تر بلیت مناسب سفر خود را پیدا کنید.
🔹
از ۲۷ تیر پیش‌فروش بلیت سفرهای اربعین آغاز شده است. برای برنامه‌ریزی آسان‌تر سفر به سامانه سپاس مراجعه کنید:
🔗
sepas.rmto.ir
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/akhbarefori/675284" target="_blank">📅 23:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675283">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
خبرنگار الجزیره در تهران: هیات عمانی تهران را ترک کرد، اما دیپلماسی متوقف نشده؛ این بار در سطحی بالا که ممکن است به افزایش امید‌ها برای یک راه‌حل مسالمت‌آمیز و دیپلماتیک و کاهش احتمال گزینه نظامی منجر شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/akhbarefori/675283" target="_blank">📅 23:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675281">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
ترامپ دستور توقف تمام حملات به ایران را صادر کرد
👇
khabarfoori.com/fa/tiny/news-3233105
🔹
حمله اوکراین به شناور ایرانی
👇
khabarfoori.com/fa/tiny/news-3233113
🔹
بامداد مرموز؛ چرا آمریکا دیشب حمله نکرد؟
👇
khabarfoori.com/fa/tiny/news-3233081
🔹
تصویر گوگوش در آغوش اکبر عبدی
👇
khabarfoori.com/fa/tiny/news-3233085
🔹
تاخیر در گزارش سم‌شناسی لیندسی گراهام | آمریکایی‌ها روی مرگ گراهام مشکوک‌تر شدند
👇
khabarfoori.com/fa/tiny/news-3232948
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/akhbarefori/675281" target="_blank">📅 23:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675280">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcddb9a3f7.mp4?token=Q-Z1nH1PgWL-lwG_zmOe-_NO5ppaxphLsYx-MH0HWE9Azc_xNnX0KKw57CsJJ7oiZAWwAO7GbWJI7v0ErXp0vk9Hy4LhD5kKQtq9FF0il_T__w36F4rOHLg1k38GfvXKduLUDFXs41ECrdRK5s3Jn4SdSVhReDGfEGMGFxmaprKaoSJdIZeBAwOo8RXM6BcVzva4WYpSDizT3Zjf460fu2h6zVgHr4uYhAnJHxpaj_nLMMKw4JppqGXW_C_xkIizfor2Ar436sElDlAxl65F-BcrOMb1Y_JirwnIMNrzZFpOB-v2EFw4spAL_MK7xbO_E6kLhZ5Pl7MIwoPC-XfTPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcddb9a3f7.mp4?token=Q-Z1nH1PgWL-lwG_zmOe-_NO5ppaxphLsYx-MH0HWE9Azc_xNnX0KKw57CsJJ7oiZAWwAO7GbWJI7v0ErXp0vk9Hy4LhD5kKQtq9FF0il_T__w36F4rOHLg1k38GfvXKduLUDFXs41ECrdRK5s3Jn4SdSVhReDGfEGMGFxmaprKaoSJdIZeBAwOo8RXM6BcVzva4WYpSDizT3Zjf460fu2h6zVgHr4uYhAnJHxpaj_nLMMKw4JppqGXW_C_xkIizfor2Ar436sElDlAxl65F-BcrOMb1Y_JirwnIMNrzZFpOB-v2EFw4spAL_MK7xbO_E6kLhZ5Pl7MIwoPC-XfTPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسیر ما ادامه آرمان آوینی‌هاست: اگر ما را با خليج فارس تهدید کنند، آن‌را گورستان شان خواهیم کرد #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/akhbarefori/675280" target="_blank">📅 23:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675278">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
سخنگوی سپاه: انگلیس درصورت همراهی با آمریکا هدف مشروع ما خواهد بود
🔹
هر کشوری، چه انگلیس، چه کشورهای حاشیه خلیج فارس و چه دیگران، اگر در جنگ از آمریکا پشتیبانی کنند، هدف مشروع ما خواهند بود.
🔹
اخیراً هواپیماهایB1 آمریکا از فرودگاه‌های انگلیس استفاده کردند،…</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/akhbarefori/675278" target="_blank">📅 23:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675277">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای کانال ۱۴ اسرائیل: ترامپ دستور توقف همه حملات علیه ایران را صادر کرد
./انتخاب
اخبار لحظه‌ای دور تازه میانجی‌گری‌ها
👇
khabarfoori.com/fa/tiny/news-3233105</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/akhbarefori/675277" target="_blank">📅 23:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675276">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سخنگوی سپاه: انگلیس درصورت همراهی با آمریکا هدف مشروع ما خواهد بود
🔹
هر کشوری، چه انگلیس، چه کشورهای حاشیه خلیج فارس و چه دیگران، اگر در جنگ از آمریکا پشتیبانی کنند، هدف مشروع ما خواهند بود.
🔹
اخیراً هواپیماهایB1 آمریکا از فرودگاه‌های انگلیس استفاده کردند، اگر همراهی کنند، هدف قطعی و مشروع ما خواهند بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/akhbarefori/675276" target="_blank">📅 23:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675274">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmqZSoJ0B39ODgALJzLqJTe7lxMe81MKtnWgoQ8kK30gzSYM4o7a-hF9xhVQHYmT9VNrMeQGVmQ1Hsv8T-d_g6sw32L7A3-fCvKVgBop3bjMfRE21Tilqi75_AHRU5s63rDcaazxGEiM0Wp39Acb0H2KDCzZMGb8ViRMaLgU2nkxFL2mMPh-J917BqE8FFkGKn7KV_FMHBgznhP9a-w5PmHQBH-KkI89q1YQKeHp5ezy4vtyrBlSSansULdys3LfjAnvvpOtj8cuJX2mButgeaJ2Qk2IPnlbwuv-Jq7pQAscBFxOjfZLGbiiJfBYXH9sX_5E4qBmCeWhNDHH8GdUWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2j3vdW-E2sne5gptyPjPMxL4iI-hCLRJXa5KPKa2Bh7muVPwRXY3OJ_4Svh7gsCApGAwRcB1I-53xSXeycHk4pkLwfC1pXpqJJeJ9YobpaNcEyJxyaSRvfATMHdgXWfHKZw2mYUftcen_go5LO4UZVKMQuQbK2d0eYJmVtR1zcCwP4VRwHDUFXlOjm0-JFM2jho4YhHMaxGN5K3-0AB58ZahktUnzBCe19DkHLlVobl3KVjs76dUr6oOuLRb-mya4syhtavms5c37UgJqOvavSz1QNxg4CZQmtk3ED1qblfBi59vORHAosrhIraewaeRTyntf_P6Vb2nCIowziBEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/akhbarefori/675274" target="_blank">📅 23:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675273">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11c8107cff.mp4?token=YNNeak773NEhmSsGKGkpEiVjR1s6Y99-0O-do-yx06gUkBQOi_7Z1TnbkPLFCxpIGs_U7RlCdN0IhhxmlXJ0fDowjS-o6ZfOR08xf9FkCUFZZ5YcmQggHskUgjSva-qd3m6037lg6x6pGBIm9iyHGg5hqkhPou8BiEHC-KIkiUNtJi66VgiPZU2SQQNQpdlE7Co7xmAsgL1rmCejSxwOUFVdnrAbh-TLLID39Ap5j5gsC7PeVmTSEJ9VvH4HRKxejeeVa_pLwdgz3owvwj79kFQnqu_u67E7fdrF5QCLYeD-yhFvrooGzggOu32MACRsC0dgjuSOA26uTcMyI4m5Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11c8107cff.mp4?token=YNNeak773NEhmSsGKGkpEiVjR1s6Y99-0O-do-yx06gUkBQOi_7Z1TnbkPLFCxpIGs_U7RlCdN0IhhxmlXJ0fDowjS-o6ZfOR08xf9FkCUFZZ5YcmQggHskUgjSva-qd3m6037lg6x6pGBIm9iyHGg5hqkhPou8BiEHC-KIkiUNtJi66VgiPZU2SQQNQpdlE7Co7xmAsgL1rmCejSxwOUFVdnrAbh-TLLID39Ap5j5gsC7PeVmTSEJ9VvH4HRKxejeeVa_pLwdgz3owvwj79kFQnqu_u67E7fdrF5QCLYeD-yhFvrooGzggOu32MACRsC0dgjuSOA26uTcMyI4m5Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس: بحث اصلی میان ایران و آمریکا، تنگۀ هرمز است/ هرگز تنگۀ هرمز به شرایط پیش از جنگ باز نخواهد گشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/akhbarefori/675273" target="_blank">📅 23:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675272">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6x2ZtrFSbQW0Cb6xbHW2LJ7q9eUQUd2dMmnkCkDdMNgboiS19Gd3a8EGBKG5nKSJfZRkiT_W0BD-6trtIZRgyZpwGbordO3tk3-QsrDpu529fr34HZocg1WLpSY_HBVXR6TkJl7ckTZaKqIkZoInIMepahnNHuu_sEF8_wa7qxSx7ztIowCKpb37l2zAh1FuOmoPmiHTyH0R47aK0KhCAQi_gIidNkYryWRahq4fMsPvsXu2MHqjCHrfpiD8ZCimBLz4Lpk03xmKOcxOwFfDLR4osHaW5FRz18lfcG_TmHsh1S7wRbXmM6i18sD5Zua-pAbad8kk1ztgm_r6Ob5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منزل «بن گویر» هدف حمله پهپادی قرار گرفت
🔹
رسانه‌های اسرائیلی گزارش دادند که یک پهپاد در نزدیکی خانه ایتمار بن گویر، وزیر امنیت داخلی رژیم صهیونیستی، اصابت کرده است.
🔹
جزییاتی از حادثه منتشر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/akhbarefori/675272" target="_blank">📅 23:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675271">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EquFggwSrzdAu7YZ2a_JKzIf2kD-h7-xTzgxTjY_wKVDVvgnc4s9YooUXJcUxrbDc5I5V_XBIXB3-bSCVIPyNzBfymHY4-_pu4Hq8FTHaUjn_dT8r093ZMfJ3b_LReLYauWxrlPn8mLteMcE973YjnobDnq_rq6nhA5zxjZODzl80VbJo7LQFyV0XpVnjwz-syFR9zrCxnpoGzxhUkJZ00FcfiLlAgaMRLM726dddL2lAgdqCHWlLUu8ZJe8VxPSY8PbdTIx5KLCkyUMbM7nlccnncqMpPXmf6gbZO7Yp7X-6ivFGTAN61G_JUXhTJPxAp4uFPvcuMNRDzUwS64Uew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چیزی که دیروز محل تردید بود، امروز به مرحله اجرا رسید/عرضه شمش طلا به دلخواه متقاضیان! چند وقت قبل، ماجرای شمش‌های طلایی که در فرودگاه خبرساز شد، واکنش‌های زیادی به دنبال داشت.در همان روزها، برخی با تردید درباره اصل ماجرا صحبت کردند و آن را صرفاً یک حرکت تبلیغاتی یا نمایشی دانستند.
اما حالا با گذشت زمان، موضوع وارد مرحله متفاوتی شده است؛ عرضه رسمی شمش‌های طلا آغاز شده و این محصول به شکل عملی در اختیار متقاضیان قرار گرفته است. شمش‌هایی که قرار است در وزن‌های مختلف عرضه شوند و امکان خرید، دریافت و حتی بازخرید آن‌ها فراهم شده است.فارغ از تمام بحث‌ها و قضاوت‌هایی که در روزهای اول مطرح شد، حالا چیزی که اهمیت دارد این است که یک ایده از مرحله حرف و ادعا عبور کرده و وارد مرحله اجرا شده است.در نهایت، بازار و مردم هستند که درباره موفقیت یا عدم موفقیت هر طرح اقتصادی قضاوت خواهند کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/akhbarefori/675271" target="_blank">📅 23:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675270">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgurLKmyvGijpxeJ4HDoOwqgQNytV3Q3Z7mGMytKzBH1wicbmazj_c3Gmsi_ntrVL4pGr8X50fsmm1pPqOzk4ulkeq8YZb-obpcMxrnLTWRp6XtWgDO8Dh_g5_Z_PuHeiGTZN-5z_ozWhIN-uG9SWxekVcjPNqIcywRIfTyw9Ex5DYvLspyZOnDSKWqPq692mqmHylqqHBnJrVjSKyKhz2s0ClMeoUzOwQgm2rr9Sywhd1iHs44xUxzV0yHDo9zxdZ0sATguQ_51x7bdWBZD7dOKjK7vYNF82u1-7N6IwbKAtTtZ6qQX7nEef-KV9oFF3tVaRIRxIXEJODuCOVo-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
اطلاعیه ویژه زائرین اربعین امسال
🕋
زائر گرامی، برای پیشگیری از مشکلات خروج از کشور و تأمین امنیت سفر، انجام ۳ اقدام زیر، قبل از حرکت به سمت مرز الزامی است:
🛂
۱. دریافت گذرنامه معتبر با اعتبار حداقل ۶ ماه
📝
۲. ثبت‌نام در سامانه سماح
📱
۳. ثبت شناسه تلفن همراه زائر در سامانه همیاب
جهت ثبت شناسه، فقط از طریق لینک زیر اقدام نمایید
⤵️
https://hamyab24.ir/l/qlx
https://hamyab24.ir/l/qlx</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/akhbarefori/675270" target="_blank">📅 23:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675269">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
دونالدِ قلدر کانادا را به بهانه «سوءمدیریت جنگل‌ها» و آلودگی ناشی از دود آتش‌سوزی‌های فرامرزی، تهدید کرد
🔹
سگ‌زرد هشدار داد که هزینه‌ی این آلودگی را به تعرفه‌های واردات از این کشور اضافه خواهد کرد. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/akhbarefori/675269" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675265">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
سخنگوی ارتش: تمام پایگاه‌های آمریکا و ضدانقلاب در اربیل عراق نابود شده است
🔹
دیگر توان عملیات نظامی از پایگاه‌های اربیل وجود ندارد.
🔹
در جنگ جدید از پهپادهای نسل جدید علیه مواضع آمریکا استفاده می‌کنیم.
🔹
پهپادهای نسل جدید از آرش ۲ قدرتمندتر و مخرب تر است.…</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/akhbarefori/675265" target="_blank">📅 22:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675264">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2134834fc.mp4?token=PsxOwJFGPmw91lvBWKTcvd1bSnfV-Caet-ThJBACfrextSUJdzAQYviuCRwZfxQOroYz2hnShgay7c4zsB2o2dgqwwkqz1SFWQQ7AzzVSl0TOYUNyLbUeoQByoX_vs8alJbEfjg0EgqL_773e_NcoR49YWQ7lmNo4dnOhNznY4ogK9nmW0biRE2xKYcTbn7A7DBP0Q5WM84ouk9GwB_7I_5FWmFVtClz_BtLG7cF2j-uSg11bDTwGTXCxrpFFsrYHMnSyrVIk0ERgdvozsE5TvgwziFAnqXvZm_x6pemFsPXzQceEDZqjBcIWAD-8N5xhACmhnFbHeL8Dk0wjW9BLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2134834fc.mp4?token=PsxOwJFGPmw91lvBWKTcvd1bSnfV-Caet-ThJBACfrextSUJdzAQYviuCRwZfxQOroYz2hnShgay7c4zsB2o2dgqwwkqz1SFWQQ7AzzVSl0TOYUNyLbUeoQByoX_vs8alJbEfjg0EgqL_773e_NcoR49YWQ7lmNo4dnOhNznY4ogK9nmW0biRE2xKYcTbn7A7DBP0Q5WM84ouk9GwB_7I_5FWmFVtClz_BtLG7cF2j-uSg11bDTwGTXCxrpFFsrYHMnSyrVIk0ERgdvozsE5TvgwziFAnqXvZm_x6pemFsPXzQceEDZqjBcIWAD-8N5xhACmhnFbHeL8Dk0wjW9BLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از گریم‌های مختلف اکبر عبدی، مرد هزار چهره‌ی سینمای ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/akhbarefori/675264" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675263">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
رئیس سازمان اداری و استخدامی: تا زمانی‌که قانون فعلی تغییر نکرده براساس اختیارات‌مان حقوق نیروهای شرکتی را به صورت مستقیم و بدون تاخیر به حساب‌شان واریز خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/akhbarefori/675263" target="_blank">📅 22:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675262">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sr4GS9tuXHeNAwPujheXBn28Kn-fU-wE2zSVu7gAyHbUVYJYDHueGBtXff01JHeMWWgCOT8YmV5oOarqZRGV-GNTBTy4-iwf9HQKhohJceBRxxnrzIOL2Xr7wLbr-z1XypgXTnWEIltND7ecWnEFsgZoDEKoJhRsod8V05uF3jurYj2DG3uSKVHX53p1DstVYqTEFxq-OXd0uHwWmpfkJqfAKasV9vYR2T6UyfzoJmQmEvl_Mv_Y0f2Lt5fbk7GXZL-W1D84IyUH5T1_YjmykWKjOybmcDpNzZ9Px759BG9Y-O2ZJlz4AkDL05b0KtUKNfF1yWVHdCPc5Ha40BVbhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چه کارهایی مصداق کفر هستند؟
🔹
امام علی (ع) کفر را بر چهار پایه استوار می‌داند: عمیق شدن در وهم (کندوکاو در اوهام)، تنازع (ستیزه‌جویی)، زیغ (انحراف از حق) و شقاق (دشمنی و لجاجت). این عوامل، حجاب‌هایی هستند که خرد را از حقیقت بازداشته و انسان را به گمراهی…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/akhbarefori/675262" target="_blank">📅 22:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675261">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbc947bc56.mp4?token=fX_3eZGgoAkb7gDRQfJp-J6NcXXP3LvRUexSYFeW8ZAjTHxZT5J-NWL66SZSXpwvhSmf_Hvt41IKRr5VqtFin7U_NCSslTbDcjkPC6YVHi6sS-B5I1JwzCt8oglYfYdMC9Ki60Xyp0nZKBCfq4XFO04gXNRqf6emdGLhJjgD_LllLozQAu6D7qwgi4MzvgII_97Yom74_D9s0_l-em2-ivdG-zY3bTdwoJTua8rjnObGm8kiC9phoR8TmpNCUHcsOd0Qlpfji3eTAKNaS8SnqrUqyN_CtxJfdjxIj8KGgOWgZTvCVsGzidAAq3jHo_69cXZcecyB4veX1Ms7VD6tuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbc947bc56.mp4?token=fX_3eZGgoAkb7gDRQfJp-J6NcXXP3LvRUexSYFeW8ZAjTHxZT5J-NWL66SZSXpwvhSmf_Hvt41IKRr5VqtFin7U_NCSslTbDcjkPC6YVHi6sS-B5I1JwzCt8oglYfYdMC9Ki60Xyp0nZKBCfq4XFO04gXNRqf6emdGLhJjgD_LllLozQAu6D7qwgi4MzvgII_97Yom74_D9s0_l-em2-ivdG-zY3bTdwoJTua8rjnObGm8kiC9phoR8TmpNCUHcsOd0Qlpfji3eTAKNaS8SnqrUqyN_CtxJfdjxIj8KGgOWgZTvCVsGzidAAq3jHo_69cXZcecyB4veX1Ms7VD6tuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین وضعیت تنگه هرمز از ساحل بندرعباس/نورهایی که خلیج فارس را روشن کردند!
🔹
گزارش خبرنگار خبرفوری از قلب تحولات جنوب ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/akhbarefori/675261" target="_blank">📅 22:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675260">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmOs67eMvQTt1PBJAhKFwdmTH7eGSziikttlBFpAZfnQywlvLOrv5-mvTrr7yvDGSUATi8qIu2HSMJzPeaXgjPQ0L742ftE31cMxbKKqbw9Twlcxmz0cQW4GGxeJMeamQYCB7KUoMH1wGZpzDfoGMR79NjUS5xIHwPzQVsZlaGiazODPQi59zxPd8aOPfuFQRoC6TFZfRUe8MKWxW6TU-o4SjoTeyzrw1MfvJMIvmETX6I3ivUIOp4dJ-fqnp6D6088MpLTXe-PTg5ENCxBd9QzCVurCFkoOuuHvGppd0aL9LZZjbjJ-mylcjGhun472gMte0VNBquOjmIY6ENqFqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای زلنسکی: شناورهای مرتبط با ایران را هدف قرار دادیم
🔹
رئیس‌جمهور اوکراین امروز در پیامی ادعا کرد «در حملات دوربرد خود در دریای خزر به نتایج بسیار مهمی دست یافتیم؛ از جمله شناورهایی که برای انتقال محموله‌های نظامی مرتبط با ایران مورد استفاده قرار می‌گرفتند.…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/akhbarefori/675260" target="_blank">📅 22:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675259">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b0e668086.mp4?token=oR_dsxTT8abKGatN5EsnlNumWeCZqfLXGqgYUPKn4rSW7RcjMO4ajp9GT5w1RR0-O_ai-wNJWsRRWxY6Utq-3EuIOK_xijVI-pazAGnPgMkUjo9161Iid9EQA0ymOD_eMDcQEuynfZ0AS6PFPrORmqZw1QUVhncYB1Pqex2cgngpJBEwUeS1Wxro_HzYPiAamLbqw5c8tHcWaQXnNDsF4lrTnjF6ieZqW70OTNenf-Lz3Hwsh76AliV0Pnpg8BXAbgpF2OBOivbZBNgVYrgB1ap2NxSpNx7KDzPFAB4CvPJnX7mF2oLltx7FZJHsmMdQl0tHl9UKwoldxhsfQ-KyDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b0e668086.mp4?token=oR_dsxTT8abKGatN5EsnlNumWeCZqfLXGqgYUPKn4rSW7RcjMO4ajp9GT5w1RR0-O_ai-wNJWsRRWxY6Utq-3EuIOK_xijVI-pazAGnPgMkUjo9161Iid9EQA0ymOD_eMDcQEuynfZ0AS6PFPrORmqZw1QUVhncYB1Pqex2cgngpJBEwUeS1Wxro_HzYPiAamLbqw5c8tHcWaQXnNDsF4lrTnjF6ieZqW70OTNenf-Lz3Hwsh76AliV0Pnpg8BXAbgpF2OBOivbZBNgVYrgB1ap2NxSpNx7KDzPFAB4CvPJnX7mF2oLltx7FZJHsmMdQl0tHl9UKwoldxhsfQ-KyDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نگاهی به مریخ از فاصله ۵۵ میلیون کیلومتری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/akhbarefori/675259" target="_blank">📅 22:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675256">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cn-2RKxEVW2uQmsCxOdRyIQ2V1gt2cIDMPBo_Mm8CyF2P0G2m8IsGOkOcW5kZNcZbdTW4mKLRerUEW16HeXWc6-miMYy92e0UQ4yu3tAZussKFVkULezlKkCVBjCO21CdymIyT18wt1Zp7owG7CrH8L0wyAs-6lDIEbaHuppykOq_dJFBkd1NrsrMjFYCpA6OaHGLE2RKj1a1QMSnckd9tIrAe_BGwJEIbcBkDGGK5t1LsJG2AQKiO-W7ZLIx_e2Q1Y5-E8yWYDvTv5qWRrVIV41XG8BmxGU0r_wi4k3ANxhW8As4c7Kkg-B1f7k-7FHhTOYG0WAlOlu_zeymSIh8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKsEu-fnruufu9i9T0jg-NXad0K4YhJPotFt7u1iLp7xbijBtaYok8IleIixYsToROYf8f3K2W368wl759PNQSxXTQb4fvJ-SRO_sT046fIqFQ42v3aEpXkA5sawQ2VYcb0eBLlNRnHXshSyWJ29_Yny2JgxKxlfUhWA59CyGzoaAhCjMO1Qgvy1ffxmiOmMcShTUVoHIilq0qS--KbiiU48Ju29PexwbOkXL_62rCxZZh7knfVxSnfdsfbVX5f5ydvpKSSXxFwz1ag1ubbEJbgI6rK0twCUyCdb0DPD95ECLbpvGaXZpqB4aLjXT0OHFyzdAAxGfnS28okKH0_6tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">میزان وابستگی کشورهای حاشیه خلیج فارس به آب‌شیرین‌کن
🔸
کشورهای حاشیه خلیج فارس بخش عمده آب آشامیدنی خود را از طریق آب‌شیرین‌کن‌ها تأمین می‌کنند.
🔹
در قطر، حدود ۹۹٪ آب آشامیدنی از طریق آب‌شیرین‌کن‌ها تولید می‌شود که بالاترین میزان وابستگی در میان کشورهای منطقه است.
🔸
در مجموع حدود ۴۰۰ واحد آب‌شیرین‌کن در کشورهای حاشیه خلیج فارس فعال است، اما تعداد تاسیسات بزرگ و اصلی در هر کشور محدود بوده و بخش عمده ظرفیت تولید آب شیرین را همین مجموعه‌ها بر عهده دارند.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/akhbarefori/675256" target="_blank">📅 22:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675255">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
وزیر آموزش‌وپرورش: امسال استخدام گسترده‌ای نخواهیم داشت
🔹
در استان‌هایی مانند تهران، شهرستان‌های تهران، اصفهان، مشهد و شیراز کمبود نیرو وجود دارد اما امسال برخلاف سال گذشته، جذب گستردۀ نیرو انجام نخواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/akhbarefori/675255" target="_blank">📅 22:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675253">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
سخنگوی ارتش: تمام پایگاه‌های آمریکا و ضدانقلاب در اربیل عراق نابود شده است
🔹
دیگر توان عملیات نظامی از پایگاه‌های اربیل وجود ندارد.
🔹
در جنگ جدید از پهپادهای نسل جدید علیه مواضع آمریکا استفاده می‌کنیم.
🔹
پهپادهای نسل جدید از آرش ۲ قدرتمندتر و مخرب تر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/akhbarefori/675253" target="_blank">📅 22:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675252">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
«اشک میناب» منتشر شد / تازه‌ترین تولید موسیقایی در سوگ فرشتگان دانش‌آموز
🔹
همزمان با تداوم آیین‌های تشییع و خاکسپاری شماری از پیکرهای مطهر دانش‌آموزان شهید میناب، بنیاد رودکی قطعه موسیقایی «اشک میناب» را به همراه نماهنگ این اثر منتشر کرد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/akhbarefori/675252" target="_blank">📅 22:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675250">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ادعای سگ زرد: اگر به ۱۰۰٪ خواسته‌هایمان نرسیم، به جنگ باز می‌گردیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/akhbarefori/675250" target="_blank">📅 22:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675249">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
تظاهرات گسترده در انگلیس در اعتراض به همکاری با آمریکا در جنگ با ایران
رسانه ITV:
🔹
معترضان خواستار توقف استفاده از پایگاه‌های نظامی انگلیس در جنگ آمریکا و ایران شدند.
🔹
معترضان ضدجنگ در مقابل دروازه‌های اصلی پایگاه هوایی نیروی هوایی سلطنتی در «رف فیرفورد» (RAF Fairford) تجمع کردند و از نخست‌وزیر، اندی برنهام، خواستند تا استفاده از پایگاه‌های نظامی انگلیس را در جنگ آمریکا با ایران متوقف کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/akhbarefori/675249" target="_blank">📅 22:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675248">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW64CMA86goNged9MPIascjrbukF8aFaAD0Zu2YjRtPEKHZrt_w24DbVGS2epwFNUyex4e9he-ap4KiUaeHqIye0c-BQMALCwIY-qABOdxwohCvG9vfMFHQ535v7h-whNTX3Ub83i4El6doXM10uynd9DOct0dQnNKuDMcRLPK1QlQUC7tM-tQTDjfqIfnp3lxbQ5Fe-4Fw_x5ULp-BqTirVU0bhXyehsh28NUL8VY7R7rlVpgOdhfZk6lSkAIO2a5HAfl4uoUrMFFvJOxFuwUivx8jo-UsH8hggDvOUWzu9iFa6KCBGXOFZdHXTKkxquV9tB-C5OzT07vbjBggN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مام اسپری سورملینا
💥
هم خوش‌بو، هم ماندگار، هم راحت!
⭕️
داخل هر بسته ۲ تا مام اسپری هست و از نظر قیمت خیلی به‌صرفه‌ست.
✅
کامل بوی بد عرق رو از بین می‌بره
✅
بدون حساسیت و بدون لک روی لباس
✅
مناسب خانم‌ها و آقایان
✅
ماندگاری زیاد؛ فقط یک‌بار بعد از حمام استفاده کن
🟡
🔵
رایحه اسپرت و دلپذیر
🟢
ارسال رایگان + پرداخت درب منزل
🔥
سفارش با تخفیف ویژه از لینک زیر
👇🏻
https://yeklinks.ir/mamtele?utm_source=@Akhbarefori
https://yeklinks.ir/mamtele?utm_source=@Akhbarefori</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/akhbarefori/675248" target="_blank">📅 22:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675247">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA3RDes5ia53W0PmXt45IrsLoClsd7YcCIsldWX8ZQm7UImaIa8VyiSIT27j6I_V885knu8eihsSYhjASkCgRVgXi8eQL_pCaQMgEgBY2S_wl8iR5d-iJacEeoWqM1DE85dprYaZStcc4wRsI943mwrGK2KeGKOJaP3aQnxtAN_gPbJ5KgdFQiOPBk-E4a3mcijBKQz1fAmHJR_8ysBZURKfw6FReVnxBn_it9dS0DhNnnZqDU0iJIVE0jUoY3hDghOqv5FFOz03erHJRPBPDrlf3M0THZ_26OJFwfa6h6T_PRfm05QXh1gFhmsh3hHRTFy3acubw0-R4v2_1mBrvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پل لَتیدان؛ شاهکار مهندسی دوره صفوی و طولانی‌ترین پل تاریخی ایران در ۸۰ کیلومتری بندرعباس
🔹
این پل با ٢٣٣ دهانه و بيش از ١٠٠٠ متر طول، ۳ برابر سی‌وسه پل اصفهان است.
🔹
لاتیدان روی رودخانه سیلابی کر و با سرمايه يک بازرگان هرمزگانى مقيم هند ساخته شده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/akhbarefori/675247" target="_blank">📅 21:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675246">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOxhafBbJG0U1BrAxWa1lj2Lea43WJn4BcZeAkmXc5J4eseAXS9Ys3qKctNBpyv5bhg8fVMjZeTtxr3lO6reEjIWgGZK_K-faCwbGc1FHGMRt-yOKoHbfR_ij4UHrkRcjoysFJ7Q5TljtaRJMwYlbVzvS7t-XGan_HQgg99g4Wbe4X9hDY6Gfcjo3sU0YYB6y23c80FyeJT-7qOFzpd0o07R70CQ316DGjTMB9TM6IH1NgdeVa7IMivQ1tJUHRte_wUPwj8ProJg5UVduNbUCeQ_dtYJNINqrKUniRuaGn2R-NIFgjdAQaNPLrlQandy_xVcMZgL8gGxdSZYVMGxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
زیارت به نیابت رهبر شهید
◾️
همین حالا با ارسال عدد ۲ به ۳۰۰۰۱۱۵۲، شانس خود را برای ۱۰۰۱ سفر کربلا امتحان کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/675246" target="_blank">📅 21:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675245">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76eb5d57cc.mp4?token=pT9I02H9dGvmpiMDXbaPUzB4USRRVcpMFrmx7Rqe291H6a9QFa4qgBhTQ1BraO5IFKrF9sXRtsUP5YRpJlG_m__eFGTvYg65AJUGXK3PvPaeyX9oGi1KGOdxM3efxvCqgfgiV5i0VUanGGjo143JARuKWhgyQqKYOh9g7ub4XanGDly08Ohkf-7fmFLVjmvo6Vg6w-DJWFa7D0ZuNtaOSTPCkGrWtlqU5deLKTnCXzqqfwO7k2QxG7o2CFW7CN6nveeBwmgIIpCf-tZ24thAYXuxIsWS9F2Eh-ayhWCW31txKzNPkcwAM9xejwD08HflsB5_WYUf-ethPCMEINPXFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76eb5d57cc.mp4?token=pT9I02H9dGvmpiMDXbaPUzB4USRRVcpMFrmx7Rqe291H6a9QFa4qgBhTQ1BraO5IFKrF9sXRtsUP5YRpJlG_m__eFGTvYg65AJUGXK3PvPaeyX9oGi1KGOdxM3efxvCqgfgiV5i0VUanGGjo143JARuKWhgyQqKYOh9g7ub4XanGDly08Ohkf-7fmFLVjmvo6Vg6w-DJWFa7D0ZuNtaOSTPCkGrWtlqU5deLKTnCXzqqfwO7k2QxG7o2CFW7CN6nveeBwmgIIpCf-tZ24thAYXuxIsWS9F2Eh-ayhWCW31txKzNPkcwAM9xejwD08HflsB5_WYUf-ethPCMEINPXFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش عضو هئیت رئیسه فدراسیون فوتبال به پاداش ۱۴۰ میلیاردی قلعه‌نویی:
این پاداش‌‌ها نسبت به گذشته خیلی ناچیز است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/675245" target="_blank">📅 21:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675244">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsDtwx47MK03kSgm4UIJTrLkTLCH386yArQSYEbspyZinUsOukTrpod5IPW6SUjPfM9qI1gRoCH5MF3MO7E7bHeRPvSpzYUJ46HKe0c9me_eVoU5zwS-uoRG7SGoH9u1UPRqTmSdskZ7ujtfba3IVd0sxU9YxEmaJoXrrYMzsZ0BS3e4UcDhPRioIqNsx7HBqcacWzDsr3pxArk453x5eX6J_cGpDm8Aid04HNES13V1krYOvKh0jxTFIwHH-WvR0L9jKOs8WgJ5OWVkt0COBhifDYqqADnOGAnNAtOCL8WtI1vMQZ-HgG-_O5RriREoP7KlBmOfYzJCNDCtNYotlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زرشک سیاه؛ یک میوه، هزار خاصیت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/675244" target="_blank">📅 21:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675243">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادعای وای‌نت: قطر و عمان تهران را تحت فشار گذاشتند تا سازش کند
ادعای رسانه اسرائیلی وای‌نت:
🔹
قطر و عمان فشار قابل توجهی بر ایران وارد کردند تا موضع خود را نرم کرده و از آنچه به نظر می‌رسید یک عملیات تقریباً حتمی و بزرگ آمریکایی بود، جلوگیری کنند.
🔹
اسرائیل ارزیابی کرده بود که یک حمله بزرگ بین شب جمعه تا شنبه آغاز شود که این امر باعث آماده‌سازی‌های چشمگیری در اسرائیل شد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/akhbarefori/675243" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675242">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxOyZHAfvsssSZ-QN_2FjU0OSqZa330KZYWKUgeTihinN2GXS9OL0Hukz1Z0m6i9eUFDJdcoI8hqJmWigOnL1P5PV0KigUGNlpT5eaPDGhFT5gqNWZE1R9kWQIC-2MyV08ljX3dDnUJj0aiPz0VtPOrbU3kAQvGc4HArNJsyyCAhlrmKbQRzxeyu2zx9v5B_3f1A6TUQm9uEzRMf1ftvb2j07NGy16cklqJqqlV1DUuU55ZeWSuOAovFhPSqnESBS_1wUlK8jJIUUIsUETnZPbt3cagq2F4qmC5Tlqb63nYqniiubgee5bH7i67n2qgljCJzZ4OZZLbNRjovzfGTug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتقاد کتی پری از کاخ سفید بخاطر استفاده از آهنگش در ویدئویی از حمله به ایران
🔹
کیتی پری، خواننده پاپ، کاخ سفید را به خاطر استفاده بدون اجازه از آهنگ «Firework» در ویدئویی از حمله نظامی به ایران محکوم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/akhbarefori/675242" target="_blank">📅 21:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675241">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02181638c.mp4?token=kZ4MqM7Q_3o8T2LCvqxx--BRNdu-OQmAwLp6r-OZF_xmoAEqZ72FZlWgBqrbwbNjBE0ELA40qcuivs4T1Jr6eWqw1N7ISKfQMsyKqMqC5K4O2zb8TOAwVXud2KynAAbIQ1dSZpD1qUQh67WZaNrOK8eAzt6_gn6GnBnKU5_Lf_ni-URNzj_jX21TKSABhArNYp4KQ5-iuYV9a5_VK4AiYIbWdy4Bokb8SnecyNHvZvLlF_p1ZM1zuV-16U4uRDnH_BXrDWc8yzvbH01ySS7pA-P3TRXE5AGA0303kJVLmwEfLMEpstgV-t-yOfxQJacu8ALckjZnToXplAvgYWTBsSRjUvAw2ufoyDX-0Y5bM0yKtpYIyjzmv03undz5vChcF_jP_Ty3GOVxNjHxx_0XPKkX5a5A1j_qCxXzPTYOqDofp12FQO1Sl6YmKR4Nb0tvJ9mbvYmIu4HF2nliM5Ntu5kzAPsMaC6r7I9r5R0A2JGDp-tp5sDPhDk1AkbBjAZ3C7P1WFZJ533ddEHleu5wC6mdK0LtL_z1hmhLiC9AwYSZnIGqS_mjnKLLc2JqkSpYOLi8WALFIy6Nwr3Gp2yKINcNV31rLbqI560i1cAffupy4izA3WBmxV9QlkDrlWwWFld8IyQTnq321UA2aTsPrJw3cmJK4cYTLGil_tQXLd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02181638c.mp4?token=kZ4MqM7Q_3o8T2LCvqxx--BRNdu-OQmAwLp6r-OZF_xmoAEqZ72FZlWgBqrbwbNjBE0ELA40qcuivs4T1Jr6eWqw1N7ISKfQMsyKqMqC5K4O2zb8TOAwVXud2KynAAbIQ1dSZpD1qUQh67WZaNrOK8eAzt6_gn6GnBnKU5_Lf_ni-URNzj_jX21TKSABhArNYp4KQ5-iuYV9a5_VK4AiYIbWdy4Bokb8SnecyNHvZvLlF_p1ZM1zuV-16U4uRDnH_BXrDWc8yzvbH01ySS7pA-P3TRXE5AGA0303kJVLmwEfLMEpstgV-t-yOfxQJacu8ALckjZnToXplAvgYWTBsSRjUvAw2ufoyDX-0Y5bM0yKtpYIyjzmv03undz5vChcF_jP_Ty3GOVxNjHxx_0XPKkX5a5A1j_qCxXzPTYOqDofp12FQO1Sl6YmKR4Nb0tvJ9mbvYmIu4HF2nliM5Ntu5kzAPsMaC6r7I9r5R0A2JGDp-tp5sDPhDk1AkbBjAZ3C7P1WFZJ533ddEHleu5wC6mdK0LtL_z1hmhLiC9AwYSZnIGqS_mjnKLLc2JqkSpYOLi8WALFIy6Nwr3Gp2yKINcNV31rLbqI560i1cAffupy4izA3WBmxV9QlkDrlWwWFld8IyQTnq321UA2aTsPrJw3cmJK4cYTLGil_tQXLd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا سپاه شرکت آمازون را در بحرین هدف قرار داد؟
🔹
سپاه پاسداران انقلاب اسلامی شرکت آمازون را در بحرین مورد هدف قرار داد. این شرکت چه اهمیت نظامی دارد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/akhbarefori/675241" target="_blank">📅 21:42 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
