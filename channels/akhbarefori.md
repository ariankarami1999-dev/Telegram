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
<img src="https://cdn4.telesco.pe/file/fFAGFRpolZR1WQSVV6IGYMwwxEaRKNgBS_lFnekThVtFj_Gbzrcl1seWFVQ4jvUu9IIyFnfpFmHVCEvUCVaIG7bk1_GpdEDkXhejmfUYGQMAJYbuncPHYDpZDFSok-35VQuDfC5yIqOwiJd82WvllL8w891hOv-n3-IymlAY9C3qDiVzQwQOJGDrsf2RGzjSkom5j6uKMDOcpgfQOQ6GIRPmPdCc99tXbmAOhV4UiUox_E8cJT6XGRdAejG0FU2ECDaI3NwGv1zeRwBcfYfru5JAg2txRzcaprPlMRRRumWOOoqJPQGP36LTvlxqOQ7uBnMdNebh1AS9qb5_9st_Tg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.15M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 11:47:58</div>
<hr>

<div class="tg-post" id="msg-681627">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1278d5aaa1.mp4?token=Zw73ruFppjQ3cFbjgdkIRe1DsaMrbqeaJKKrOeEGMNkkbxO5cd7ASJGIT_8eN2E7zWeJJ7gzQUpmrO0r2oBBmdI1sIQoTRkepIA9BfkthaGcnzfHhmL6KfQ7MDTfgVC3LYE2JMbNED9brQOGzPQ83oP6ODVQBLX2xThMxvn1pmG77Kiim5aU6mLybm9ZWr1u6jEWfiKJLgHvVB0850IM7EZ3ZNzlobS8F_CUgL4DrtmvO0TjafqgPwjtAnQEm2jX-WLcWCiSZw3xvo0rBCMbey2XV7lncTZ2vz4NCJgJ5gRM3REGzeWhvde-ZxXkkxh5U3bW6ZqSlKm1dwC2RYI6ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1278d5aaa1.mp4?token=Zw73ruFppjQ3cFbjgdkIRe1DsaMrbqeaJKKrOeEGMNkkbxO5cd7ASJGIT_8eN2E7zWeJJ7gzQUpmrO0r2oBBmdI1sIQoTRkepIA9BfkthaGcnzfHhmL6KfQ7MDTfgVC3LYE2JMbNED9brQOGzPQ83oP6ODVQBLX2xThMxvn1pmG77Kiim5aU6mLybm9ZWr1u6jEWfiKJLgHvVB0850IM7EZ3ZNzlobS8F_CUgL4DrtmvO0TjafqgPwjtAnQEm2jX-WLcWCiSZw3xvo0rBCMbey2XV7lncTZ2vz4NCJgJ5gRM3REGzeWhvde-ZxXkkxh5U3bW6ZqSlKm1dwC2RYI6ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من تاریخ سرزمینی هستم که بسیار کوشیده‌اند راز پایداری‌اش را دریابند #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/akhbarefori/681627" target="_blank">📅 11:36 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681626">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWeImGOewfM4I4nXEMlRQJs7YXN_9oBTUvSoixxzKzQiHt2tiTa2lzRZGEvXzhe4tMgGpKkmPZp5a2PCL5TMokJ33vK_Aja3U5hh90iLyt-jrC3Tp3N1fp4hbRiODhiWN97dOgPu3R2lpoR2s4MSE104stYniMDXMGjIojVEA6b-87u5esyhyycfhrNBvCINiUo0w5uP2HZlWqvvQ2YszERLX5O4lUyFLVGr_pt-heLWPyEp_gvsZhr2DgryHpNCLPEex6QmjtVZGGqlcZMNmLPIBhzHDMJS04WVb_b41qp6YTSXlDJJnapW02uwdc1N52w2Zp2sy_42KWsJVqkMqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۴میلیون نفر در سنین فعال ازدواج مجرد هستند
🔹
همراهان گرامی خبرفوری؛ برای شرکت در این پویش کافی‌ست یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کرده و از دلیل تجرد خود برایمان بگویید.
🔹
برای حفظ حریم خصوصی، صدای شما تغییر داده می‌شود و هویت‌تان به‌صورت ناشناس باقی می‌ماند.
🔸
روایت کوتاه شما می‌تواند بازتابی از تجربه‌های متفاوت مخاطبان در این زمینه باشد
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/akhbarefori/681626" target="_blank">📅 11:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681625">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
جلسات علنی مجلس قرار است به‌صورت
تلفیقی حضوری و مجازی
برگزار شود.
🔹
مرزبانی فراجا از کشف ۴۹ قبضه سلاح و دستگیری ۵ قاچاقچی در مرزهای کشور خبر داد.
🔹
احتمال شنیده شدن صداهای نامتعارف در مناطق سردرود، اسفهلان، لاهیجان و اطراف نیروگاه تبریز؛ هموطنان نگران نباشند.
🔹
شمار قربانیان زلزله ۷.۷ ریشتری اندونزی به ۵۱ کشته و ۱۱۳ زخمی رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/681625" target="_blank">📅 11:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681624">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
کارمزد ساتنا و پایا هم با دلار بالا رفت
🔹
کارمزد پایا ۳۳ تا ۶۰ درصد افزایش یافته و به ۴۰۰ تا ۱۲ هزار تومان رسیده؛ سقف کارمزد ساتنا نیز ۵۰ هزار تومان شده است.
🔹
کارمزد کارت‌به‌کارت تا یک میلیون تومان ۱۱۰۰ تومان و برای هر میلیون اضافه، ۳۵۰ تومان بیشتر محاسبه می‌شود.
🔹
پیشتر رئیس‌مجلس گفته بود که افزایش نرخ ارز نباید بر بسیاری از کالاها و خدمات اثرگذار باشد؛ چرا که اساساً ارتباطی با ارز ندارند./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/681624" target="_blank">📅 11:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681623">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868650bed6.mp4?token=AoRXhxZFkw2-aq16Ea5SUdeVuhIv2D2mAOB3WZyyW6MxqGQ3qkU2luKuBTTkrxP5IPBegsn3JVwSfvEbQVzZOdoQwvEf4Fbf8z5Cu3yOOIWvHf1RphnKaz344ONmHPh06k4mB98VeO827G2equeLsZVfgzDvu-x2OL69PejqU-nxACQ9at5PIL4epsvQNSrqF7kZyy3QWFG6plEuDEZfnJp08CzxkUjuIN0Oh2zC_D_K2KP3KKuiGJWdEJCo4DctNFA-F7jvk0dPcVCEqiYHhHEH6yV3nmDjAkk-megXSyI2co8YP03qcJbYgJlPreq-wny2NZHnHclYBmf8V5fHbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868650bed6.mp4?token=AoRXhxZFkw2-aq16Ea5SUdeVuhIv2D2mAOB3WZyyW6MxqGQ3qkU2luKuBTTkrxP5IPBegsn3JVwSfvEbQVzZOdoQwvEf4Fbf8z5Cu3yOOIWvHf1RphnKaz344ONmHPh06k4mB98VeO827G2equeLsZVfgzDvu-x2OL69PejqU-nxACQ9at5PIL4epsvQNSrqF7kZyy3QWFG6plEuDEZfnJp08CzxkUjuIN0Oh2zC_D_K2KP3KKuiGJWdEJCo4DctNFA-F7jvk0dPcVCEqiYHhHEH6yV3nmDjAkk-megXSyI2co8YP03qcJbYgJlPreq-wny2NZHnHclYBmf8V5fHbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزایر دریاچهٔ ارومیه میزبان پرندگان شدند
#اخبار_اذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/akhbarefori/681623" target="_blank">📅 11:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681622">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
سخنگوی هیئت‌رئیسۀ مجلس: طرح مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در صحن علنی مجلس تصویب شد/ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/akhbarefori/681622" target="_blank">📅 11:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681621">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی: تصمیم نهایی درخصوص بنزین طی هفته‌های آتی اتخاذ خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/681621" target="_blank">📅 11:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681620">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4ti4o1szYVrgNiWHn6KLVyPkufnRfXIHKf9VzrH8Muap1FyK7rxfVp8sNZob_oYS_wo3UwiuQOLcdwtlaLWtOht_NXHGxcKDtUQJpPZ0bj8An4bMLv9ywKc5-igcRkGghA8rm7m9zDNJIcGGu6-ChkeQA4GxkXMqzM-q4YYPQi--5OH-pHKEkJv2rJo1w_rxfkREuPuvY3W8sOG4m3XFwkeQWVF2oIDDw1_2oA5br7kFFd5AIOw5I0ACdW9DbQGRm0kDZth1rX4tU_JlF9Td-KSOl0FClP-7CNGPZEbdAxgnVyVauQoU4lL-csJvTpm-FRhAmw8MRqZx0MUkqQxpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا بیشتر از غرامت متفقین از آلمان، از ثروت ونزوئلا اخذ می‌کند!
فرانسیسکو رودریگز، اقتصاددان سرشناس ونزوئلایی-آمریکایی:
🔹
به گفته یکی از اعضای کمیسیون دولتی ونزوئلا، آمریکا تاکنون در سال جاری، ۴.۷ میلیارد دلار از ونزوئلا بابت هزینه حمله به این کشور دریافت کرده!
🔹
که معادل ۳۲٪ از صادرات نفتی ونزوئلا در همین مدت است؛ برای مقایسه، آلمان بین سال‌های ۱۹۲۴ تا ۱۹۳۱، ۱۳٪ از صادرات خود را به‌عنوان غرامت به متفقین پرداخت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/681620" target="_blank">📅 11:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681619">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e99e81e0.mp4?token=HN97xzxZCf85gD2dxVYqvcxCELV8DGM2raN9kvv47kagqsxd_kOGnPyb_TlTVqmog2EUI74MfQez_MNU5swsIBIfzVZ-rKJZY0NEqdspxpJq3Dr9UGKBhgjaIbXLRbVMSKvv40aMq-azNrzzRmxRKjLh2SPUhrBCDmNcdT59ZgAnCKE2Gp-YrTNOFqFesRu_VmDIfo2C5sY4vDxvJSULBn4YjCBchNq1TSUR7lB4znts8QOuhMdj39L4S2GHFYwQG-UfqTDIvhAMBKQXBbmZlfAT6_tdRqP913ZQbM8VkaR5LYQD4KGJUq3rvH4LA7uNr3aoCYZtlgi0OwjIGn_MB4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e99e81e0.mp4?token=HN97xzxZCf85gD2dxVYqvcxCELV8DGM2raN9kvv47kagqsxd_kOGnPyb_TlTVqmog2EUI74MfQez_MNU5swsIBIfzVZ-rKJZY0NEqdspxpJq3Dr9UGKBhgjaIbXLRbVMSKvv40aMq-azNrzzRmxRKjLh2SPUhrBCDmNcdT59ZgAnCKE2Gp-YrTNOFqFesRu_VmDIfo2C5sY4vDxvJSULBn4YjCBchNq1TSUR7lB4znts8QOuhMdj39L4S2GHFYwQG-UfqTDIvhAMBKQXBbmZlfAT6_tdRqP913ZQbM8VkaR5LYQD4KGJUq3rvH4LA7uNr3aoCYZtlgi0OwjIGn_MB4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی جدید Honor با دوربین رباتیک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/681619" target="_blank">📅 10:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681618">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UW1-dD9v9zlz-jWnAzUIYvNsEds2DGR_qXMAZitiLOBvd6xNC-B7yPvMlK15MLfMWBvkzYkzU8btynY9LC63ECKtDUKLS5tRcmZlSFVd38mWH_qOTrtSNKiiZUBPtP_bEIpbrRSiusjQzIDDTOShAWHQpFE8InUwnTYUno5yKy8gWM5t4FtMU1l1lDdo0fSePKSvRFL5FvETQzz0-tqX8MX95EXkXtODWUiN4DEouazOmF_LC6gYsiEzJd7L_t3mKiOIfNK_dp2FDIPTH0p1jvdeCgQdK4fqARodrwymRg0soQ_A9CeYf5G3fyX5hPrRQnS6AZoxxJ0b6thOCjC2Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری متفاوت از کودکی رهبر معظم انقلاب اسلامی در آغوش رهبر شهید ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/681618" target="_blank">📅 10:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681617">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ستادکل نیروهای مسلح: تا شکست کامل دشمن آمریکایی و احقاق حقوق ملت ایران کوتاه نخواهیم آمد
.
🔹
براساس تازه‌ترین رتبه‌بندی شانگهای در سال ۲۰۲۶، ۶ دانشگاه ایرانی در جمع یک‌هزار دانشگاه برتر جهان حضور دارند.
🔹
کارت شرکت در کنکور سراسری و آزمون اختصاصی پذیرش دانشجو-معلم ۱۴۰۵ از فردا در سایت سازمان سنجش منتشر می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/681617" target="_blank">📅 10:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681616">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
هشدار روند کاهشی نرخ باروری در کشور
معاون بهداشت وزارت بهداشت:
🔹
جمعیت سالمندان کشور طی ۲۵ سال آینده به ۲۸ میلیون نفر می‌رسد؛ میزان باروری کشور ۱.۳۴ است و کشور در این زمینه از میانگین اروپا پایین‌تر است.
🔹
شرایط نباید به نحوی باشد که زنان میان اشتغال و فرزندآوری فقط یک انتخاب داشته باشند؛ باید با امید و اطمینان، شرایط ازدواج را برای جوانان فراهم کنیم.
🔹
موضوع جوانی جمعیت با «امید»، «علم» و «سیاستگذاری درست» اصلاح می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/681616" target="_blank">📅 10:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681615">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6702fd240b.mp4?token=i88V5ZHyfXEiTvUGmBKoRha3hySTCmUYONZGqb6optyiw-tLtNaERXEYlk7IqorYRDjfp7ibh20uaaN77nTrg0Us9z1SJbPFmZ79EqmfTHJQmMF_zKWj3jhlQxGHy_n0zWxnz_ZfePugQkVteoYNTWUpzJgD7GFFSC1Dm8k2Mqo4koH-o8t5xPcjHdmurs5zoqBpxy0NuBREVDZBvIDqjgs3j_IkPp2zssOwrL6wVKejrJ7v5CBcZFOF5KuNMSvNr6t1hMeAajPybgyqaH_ZN7-s3TgTjIiB9LEe14j2ud8_aXuY5FawIXtfgXH1U-QyZ4dAiFD3NKM_vqupYpu26Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6702fd240b.mp4?token=i88V5ZHyfXEiTvUGmBKoRha3hySTCmUYONZGqb6optyiw-tLtNaERXEYlk7IqorYRDjfp7ibh20uaaN77nTrg0Us9z1SJbPFmZ79EqmfTHJQmMF_zKWj3jhlQxGHy_n0zWxnz_ZfePugQkVteoYNTWUpzJgD7GFFSC1Dm8k2Mqo4koH-o8t5xPcjHdmurs5zoqBpxy0NuBREVDZBvIDqjgs3j_IkPp2zssOwrL6wVKejrJ7v5CBcZFOF5KuNMSvNr6t1hMeAajPybgyqaH_ZN7-s3TgTjIiB9LEe14j2ud8_aXuY5FawIXtfgXH1U-QyZ4dAiFD3NKM_vqupYpu26Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوشمزه‌تر از این لقمه پیتزایی برای  دورهمی و‌ مهمونی‌ها نداریم
🤌🏻
😋
مواد لازم برای ۱۰عدد لقمه:
🔹
هات‌داگ ۳ عدد
🔹
قارچ ۸ عدد
🔹
نصف یک عدد فلفل دلمه ای
🔹
پنیر پیتزا به مقدار لازم
🔹
نون لواش دو تا سه عدد
🔹
نمک/زردچوبه/پاپریکا/فلفل‌سیاه/آویشن به مقدار لازم #آشپزی
🇮🇷
…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/681615" target="_blank">📅 10:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681614">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCCd995w6KfBL8GR8sHKl1guUZ6mcMjURfDnwxWhGLYCalKk-i8kiEm8l5dBjYKEhBcDNCgLYExBTLyvAzrPk4D6KwlAKrfjbVxp18yUHR8gsunv6GDwuevlYh6f7thfv5IzlngysvmVCS16FLyzD58wB5xscYYLLfog3SAXy49ysRVWP_UmXVJspuqR4zx978cW5Y3JOy44Yo5xfOEhpw8uXdqJnir6DPv-IchsHDH7kWwQ989drX2etrXmj71s2SquzmmgERBsHv6gX9msOA_uQHSqBh_lICKYRpSlvzr9DG4zqnL67SasgYX-wBFXNFr395gToVB2qWprI-NKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طراحی زیست‌بوم جدید تأمین مالی برای اقتصاد فرهنگ و هنر
🔹
صندوق پژوهش و فناوری توسعه فرهنگ و هنر با دریافت مجوز از صندوق نوآوری و شکوفایی، با هدف تأمین مالی، سرمایه‌گذاری و تجاری‌سازی کسب‌وکارهای فرهنگ، هنر، رسانه دیجیتال و صنایع خلاق راه‌اندازی شد.
🔹
این صندوق با سرمایه پایه ۱۰۰ میلیارد تومان و مشارکت نهادهای دولتی و بخش خصوصی، قرار است حلقه اتصال میان ایده، سرمایه و بازار باشد و کسب‌وکارهای خلاق را از مرحله شکل‌گیری ایده تا توسعه و ورود به بازار همراهی کند.
🔹
تولید محتوای دیجیتال، بازی‌های رایانه‌ای، انیمیشن و توسعه پلتفرم‌های نوآورانه و فناورانه مرتبط با فرهنگ، هنر و رسانه دیجیتال از جمله حوزه‌های مورد توجه این صندوق هستند. همچنین کاربرد فناوری‌های نوین، از جمله هوش مصنوعی، در توسعه کسب‌وکارها و محصولات فرهنگی، هنری و رسانه دیجیتال  مورد توجه قرار دارد.
🔹
این اقدام با هدف حرکت از حمایت‌های بلاعوض به سمت تأمین مالی مولد و پایدار و تقویت نگاه اقتصادی به ظرفیت‌های فرهنگ و هنر شکل گرفته است.
#صنایع_خلاق
#اقتصاد_فرهنگ
#فرهنگ_و_هنر
#اقتصاد_خلاق
#سرمایه_گذاری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/681614" target="_blank">📅 10:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681613">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkuJk-WeqJUbw42txPIxL3NXMO-MtfgTxaS9c-ruVnYbKLDHYlHgkwy990CCaBnmBPQ3DGhGmYhY1Ocp0NbShjFBdQQz4UytQ-DoIoEJFZD-8zArr63pF_a10CF3Vw7QF6WcgE8PjulOx-enpi487upiPs1GDM77PoCjIyx-aiYiSRzxkA-jxmY7-h1iBxbyOOVKXPkrCuSBLZ6dpslHl3HRSglXteCycsGMlLxsgwtvK0IbDF0zwDQzF3NYwhXzO5FYOAW6k5GasUqibV4-dhtpgUHsimZjE2GHXQB6Qb3Dol51Ee_o8g5SmUuVxzb-Bco3rdegv9xFpHemcXELTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمونه‌ای از غذای در حال سرو در آبراهام لینکلن
🔹
یک ملوان حاضر در ناو جنگی آبراهام لینکلن، تصویری از غذاهای سرو شده در این ناو را برای یکی از اعضای خانواده‌اش ارسال کرد و گفت که این غذا شامل مقدار کمی از همه چیز موجود بود، نه غذاهایی که به طور شخصی انتخاب…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/681613" target="_blank">📅 10:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681612">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf8073203.mp4?token=CrwRbhm2anwqWNyJmD7Y51zZ2m-X7pW5gE-mnVIWlBkNxjgMWKqkXVVVbJ2ZjWwta0YxXcjwrgioDNFaitFcPUNBwTLyYVNIZR1xuo-vl0tYVGoCw6S_Ou5YshYz7ipNl0pylWjAOEkL34fGVkA6aGB8ZBf3vFvEzeFtskFLXMhQHIWD825m_OLAcbEd1H9nb70Qz3W11IXqXhh76Vi3dsxAdUJ5UTowLNnBP7Y0DTry7x6KjZzI79wz4K1lXQUW05oWPycjYY4aGXYvkrleyPPyAzdU_iXdNiYmX0vjypwYcaRFRF9OTKkk7ujp2wwsFzKwMAMO_0uvVY5vP08mVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf8073203.mp4?token=CrwRbhm2anwqWNyJmD7Y51zZ2m-X7pW5gE-mnVIWlBkNxjgMWKqkXVVVbJ2ZjWwta0YxXcjwrgioDNFaitFcPUNBwTLyYVNIZR1xuo-vl0tYVGoCw6S_Ou5YshYz7ipNl0pylWjAOEkL34fGVkA6aGB8ZBf3vFvEzeFtskFLXMhQHIWD825m_OLAcbEd1H9nb70Qz3W11IXqXhh76Vi3dsxAdUJ5UTowLNnBP7Y0DTry7x6KjZzI79wz4K1lXQUW05oWPycjYY4aGXYvkrleyPPyAzdU_iXdNiYmX0vjypwYcaRFRF9OTKkk7ujp2wwsFzKwMAMO_0uvVY5vP08mVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هزینه جنگ‌افروزی آمریکا برای جهان؛ نابودی ۲.۶ میلیارد بشکه نفت
رویترز:
🔹
پیش از جنگ، تقاضای جهانی نفت روزانه ۱۰۳ میلیون بشکه بود. این یعنی جنگ تقریباً معادل ۲۵ روز از مصرف جهانی نفت را از بین برده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/681612" target="_blank">📅 10:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681611">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efd2fb41c.mp4?token=o2uoYI3ZsA4RdudLb1odCvjciOEXYCGKp7QPfhQKPEHMcuW_wKXo6wywm9pT6oQlIcrGdeoI75PDrh6QlM2Mp7smXWXSfFYBmk-Z29VOHFkFrUzMhzB8OVeBivWFXYNC2zMh9pvvX5_7c5tm3u-cveeeC1axy32CWW39e-ItqBl10sGC-2qJ2ClL3u-osgi7r6IuMxPNxxf8P902p8o9YccIvsjZwqyPKBO2p4uOXRWShXFuukfmxgP3jkYe5oInv8x2fwWl8do4ZcN1x9iNNFKQ1ytyWOQr8OON9_r_yb0ZvcIPVvzDssQmIqfMtE6O11PtK-_awebRu5ZqCJzhpXVb_Ap2eXVG-gY4i8AUtvgbIcdXIaRErdAdqJMs8pxWamcPutltmNq7feE_hY2jrYWqZwKi5rB9xsyYzbnBBbGX8EqAD9gGZR3oL4UuErz7iufM0Tqjs0Nf2RoWD5GkIkecnUfesr5wEgNJ6vgHO2eTsg6IZvy1HdZfcTs_ZGN5dRjTrd0ghvG1D4suLG6MJe5vWEDsVmRJ0JJbx0LtW4YjxPB0BCpTmjUts2ZMI4UC8KHjShVNDi8SIzCh21GGkaoDdVuM9s1GwvMlGMuEMSx0fLDp-Kz6xthkKSiwr78DKvINXgTnH_-hEVJRyrBCrja5-OnVzBojXYp4L-LAQkY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efd2fb41c.mp4?token=o2uoYI3ZsA4RdudLb1odCvjciOEXYCGKp7QPfhQKPEHMcuW_wKXo6wywm9pT6oQlIcrGdeoI75PDrh6QlM2Mp7smXWXSfFYBmk-Z29VOHFkFrUzMhzB8OVeBivWFXYNC2zMh9pvvX5_7c5tm3u-cveeeC1axy32CWW39e-ItqBl10sGC-2qJ2ClL3u-osgi7r6IuMxPNxxf8P902p8o9YccIvsjZwqyPKBO2p4uOXRWShXFuukfmxgP3jkYe5oInv8x2fwWl8do4ZcN1x9iNNFKQ1ytyWOQr8OON9_r_yb0ZvcIPVvzDssQmIqfMtE6O11PtK-_awebRu5ZqCJzhpXVb_Ap2eXVG-gY4i8AUtvgbIcdXIaRErdAdqJMs8pxWamcPutltmNq7feE_hY2jrYWqZwKi5rB9xsyYzbnBBbGX8EqAD9gGZR3oL4UuErz7iufM0Tqjs0Nf2RoWD5GkIkecnUfesr5wEgNJ6vgHO2eTsg6IZvy1HdZfcTs_ZGN5dRjTrd0ghvG1D4suLG6MJe5vWEDsVmRJ0JJbx0LtW4YjxPB0BCpTmjUts2ZMI4UC8KHjShVNDi8SIzCh21GGkaoDdVuM9s1GwvMlGMuEMSx0fLDp-Kz6xthkKSiwr78DKvINXgTnH_-hEVJRyrBCrja5-OnVzBojXYp4L-LAQkY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت خداداد عزیزی از روزهای سخت زندگی‌اش!
🔹
ساندویچ نان و رب خالی می‌خوردم؛ به‌همراه پدرم دم حرم دستفروشی و گچکاری کردم..
🔹
برنج و مرغ تنها یک بار در سال و دم عید می‌خوردیم!
🔹
چلوکباب نخورده بودم و نمی‌دونستم چیه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/681611" target="_blank">📅 10:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681610">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-text">از سوی رهبر معظم انقلاب برگزار می‌شود
📢
مراسم بزرگداشت چهلم «آقای شهید ایران» در تهران، قم و مشهد
🗒
دفتر رهبر انقلاب اسلامی به مناسبت چهلمین روز تشییع و تدفین پیکر آقای شهید ایران، با صدور اطلاعیه‌ای از برگزاری مراسم بزرگداشت رهبر شهید حضرت آیت‌الله‌العظمی سیّدعلی حسینی خامنه‌ای در تهران، قم و مشهد خبر داد.
متن کامل اطلاعیه دفتر رهبر انقلاب اسلامی:
🏴
بسمه‌تعالی
▪️
هم‌زمان با ایام چهلمین روز تشییع تاریخی و تدفین پیکر مطهر آقای شهید ایران، مراسم بزرگداشت آن رهبر عظیم‌الشأن و خانواده ایشان از سوی حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، رهبر معظم انقلاب اسلامی، در تهران، قم و مشهد برگزار می‌شود.
▪️
مراسم‌های بزرگداشت قائد شهید حضرت آیت‌الله‌العظمی سیّدعلی حسینی خامنه‌ای به این شرح برگزار خواهد شد:
📍
تهران؛
🗓
سه‌شنبه ۲۷ مرداد، از ساعت ۱۷ تا ۱۹، در شبستان مصلای امام خمینی(ره).
📍
قم؛
🗓
چهارشنبه ۲۸ مرداد، پس از نماز مغرب و عشاء، در حرم حضرت فاطمه معصومه سلام‌الله‌علیها.
📍
مشهد مقدس؛
🗓
پنجشنبه ۲۹ مرداد، همزمان با شب شهادت امام حسن عسکری(ع)، بعد از نماز مغرب و عشاء، در حرم مطهر رضوی.
👤
از مردم قدرشناس ایران برای حضور در مراسم بزرگداشت رهبر شهید دعوت به‌عمل می‌آید.
🔻
حضور پرشور و گسترده عموم ایرانیان و دلدادگان امامَین انقلاب در مراسم بزرگداشت چهلم قائد شهید، بیعتی دوباره با رهبری معظم انقلاب اسلامی و تأکیدی مجدد بر ادامه راه آقای شهید ایران خواهد بود.
🇮🇷
دفتر رهبر انقلاب اسلامی
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/681610" target="_blank">📅 10:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681609">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
سردار باقرزاده: قطر اجازه ورود تیم حقیقت‌یاب ایران را بدهد
فرمانده کمیته جستجوی مفقودین ستاد کل نیروهای مسلح در پاسخ به تکذیبیه قطری‌ها مبنی بر عدم اسارت خلبانان ایرانی:
🔹
تیم کارشناسی نیروی هوایی ایران ماه‌هاست در انتظار ورود به قطر و بررسی میدانی درباره خلبانان ایرانی است، اما مسئولان قطری کارشکنی می‌کنند.
🔹
وی خواستار مجوز ورود تیم حقیقت‌یاب ایران و پیگیری فوری موضوع از سوی صلیب سرخ شد و درباره سرنوشت چهار ایرانی اسیرشده در کویت نیز هشدار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/681609" target="_blank">📅 10:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681608">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شاخص بورس تهران با افت ۳۴ هزار واحدی در سطح ۵ میلیون و ۷۰۲ هزار واحد قرار دارد.
🔹
استانداری خوزستان: فعالیت ادارات خوزستان روز دوشنبه ۲۶ مردادماه به دلیل افزایش دما، دورکاری است.
🔹
سپاه استان اصفهان: امروز صدای انفجار در محدوده جنوب اصفهان شنیده می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/681608" target="_blank">📅 09:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681607">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
هاآرتص: ترامپ پس از ناکامی در جنگ ایران به‌دنبال دستاورد سیاسی است
روزنامه عبری هاآرتص:
🔹
ترامپ در واکنش به ناکامی‌ها و «شکست مستمر» در جنگ علیه ایران، اکنون به‌دنبال کسب دستاوردهای سیاسی در غرب آسیاست.
🔹
آمریکا توجیهات طرف اسرائیلی درباره حملات اخیر در لبنان را پذیرفته و پیش‌بینی می‌شود واشنگتن در ادامه، خواستار خویشتن‌داری در سایر جبهه‌ها شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/681607" target="_blank">📅 09:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681606">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82e403547.mp4?token=q86v07cfONIWkbHUB43PK4hXPsN6ly3upUHgNKYJjZuI5Kh34K2vG59skejMqWDDMFGRNKbzCT6PfrBS4BVro5l9fkZVUvDaMbb4ooxA9v4cA9E9XUKISyixzMxSqalY0oOg1QAAnD6cXc38oBzQwL08SGtg606gyr_u7bNT136pJdD_ktg6w1VsN-BbT756y3UqIUUpQjU2PYHb86OXh1191dWnfCGM1E2TfeWm4I6kSb4OjagaeAwTx40ChDuTmQFdk48jIcWgh1XGOgp3fJBno8MXb6zdg4VPotWJwuCmFfTNkwX-LbWk75As1AhVd8k88bwsfVdwmrkvI5M-cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82e403547.mp4?token=q86v07cfONIWkbHUB43PK4hXPsN6ly3upUHgNKYJjZuI5Kh34K2vG59skejMqWDDMFGRNKbzCT6PfrBS4BVro5l9fkZVUvDaMbb4ooxA9v4cA9E9XUKISyixzMxSqalY0oOg1QAAnD6cXc38oBzQwL08SGtg606gyr_u7bNT136pJdD_ktg6w1VsN-BbT756y3UqIUUpQjU2PYHb86OXh1191dWnfCGM1E2TfeWm4I6kSb4OjagaeAwTx40ChDuTmQFdk48jIcWgh1XGOgp3fJBno8MXb6zdg4VPotWJwuCmFfTNkwX-LbWk75As1AhVd8k88bwsfVdwmrkvI5M-cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راننده خودروی مرگ چهارراه گلزار کرج اعدام شد
🔹
«شهرام صادقی» که در جریان کودتای آمریکایی-صهیونی دی‌ماه پارسال با خودروی پراید ۷ مأمور فراجا را زیر گرفته بود، پس از شناسایی، دستگیری و محاکمه، سحرگاه امروز اعدام شد.  #اخبار_البرز در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/681606" target="_blank">📅 09:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681605">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
فرصت یک‌ونیم‌ماهه دولت برای معرفی وزرای اطلاعات و دفاع
سخنگوی هیئت رئیسه مجلس:
🔹
طبق اجازه رهبر معظم انقلاب، دولت از ۲۹ مرداد به مدت یک‌ونیم ماه فرصت دارد وزرای پیشنهادی اطلاعات و دفاع را به مجلس معرفی کند.
🔹
همزمان ایده حذف شرط اجتهاد برای وزیر اطلاعات مطرح شده که به‌دلیل مغایرت قانونی، نیازمند اصلاح قانون و ارائه لایحه از سوی دولت است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/681605" target="_blank">📅 09:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681604">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b569333b1b.mp4?token=JZyg-u5B2IF3FgLwm1SMY2Tsd-56uZl3MPH_o7IbNPwkRkz4vt86KrZwYDhUsl5w_t-7X4XAL2y2e0_FTAKzdp3V-kCb7PaDYwQ4m2F657qDxss6Ctp8W4wC5eIhpwxn322rj0pJ_5Di4HTFx4EQfhDR5Wu3niFMotwMYHitxqoOeHYfwtk3LaOQDiEvmIspIruP6bsiLV_LOHVstcL1DHyj0rpg5rniwgveOtZ2ULSssOjLvIYz-f6tt6W4dedEn2KL49EuX-PLn8H7Y4XdXl2TE6djI-s9580SO5YydUZ_yBvwMENgUHhnBMZ-ZduFEbYEdlAKme2U446iBgVBrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b569333b1b.mp4?token=JZyg-u5B2IF3FgLwm1SMY2Tsd-56uZl3MPH_o7IbNPwkRkz4vt86KrZwYDhUsl5w_t-7X4XAL2y2e0_FTAKzdp3V-kCb7PaDYwQ4m2F657qDxss6Ctp8W4wC5eIhpwxn322rj0pJ_5Di4HTFx4EQfhDR5Wu3niFMotwMYHitxqoOeHYfwtk3LaOQDiEvmIspIruP6bsiLV_LOHVstcL1DHyj0rpg5rniwgveOtZ2ULSssOjLvIYz-f6tt6W4dedEn2KL49EuX-PLn8H7Y4XdXl2TE6djI-s9580SO5YydUZ_yBvwMENgUHhnBMZ-ZduFEbYEdlAKme2U446iBgVBrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت تصویر گربه پالاس؛ یکی از کمیاب‌ترین گربه‌سانان ایران
🔹
تصویر گربه پالاس، یکی از کمیاب‌ترین و ناشناخته‌ترین گربه‌سانان ایران ثبت شد؛ گونه‌ای که هنوز اطلاعات دقیقی از پراکنش و وضعیت جمعیت آن در کشور وجود ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/681604" target="_blank">📅 09:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681603">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58bf5cf360.mp4?token=gi-Cv-1iESSmkzvdSi09DvJFbI5Hxo4Zh41vXIi7LuRt-x4oJ0pskVVZFNIBzvd66hhEl5oyV-pHtVL1vbL6A-Vhw4vHEdtHeWTKUrHVKdETVi64CjYfh7DR7DzZU7ELdPBVjf2vfoTt81qJ2TVBX3hGSohgZqQeNgyz53Uw1xw5rHRd4qEdXI_2sztzyVjtXcFftfHDyU7tuw2RkfzO24mX0cMfiGTf7lEPYuhnkzOCdUPM8VQr-y2YgGvgL0b_NZR9qIcNJIs5V__Xs979o61SxJ4Scv6zBTVR2t_5ctlcAle0WHjxVP4gNWbeXPZMaPKR0VpRV82JBcVTSIwS-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58bf5cf360.mp4?token=gi-Cv-1iESSmkzvdSi09DvJFbI5Hxo4Zh41vXIi7LuRt-x4oJ0pskVVZFNIBzvd66hhEl5oyV-pHtVL1vbL6A-Vhw4vHEdtHeWTKUrHVKdETVi64CjYfh7DR7DzZU7ELdPBVjf2vfoTt81qJ2TVBX3hGSohgZqQeNgyz53Uw1xw5rHRd4qEdXI_2sztzyVjtXcFftfHDyU7tuw2RkfzO24mX0cMfiGTf7lEPYuhnkzOCdUPM8VQr-y2YgGvgL0b_NZR9qIcNJIs5V__Xs979o61SxJ4Scv6zBTVR2t_5ctlcAle0WHjxVP4gNWbeXPZMaPKR0VpRV82JBcVTSIwS-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شبکه عبری کان: ده‌ها هزار شهرک‌نشین صهیونیست آیین‌های تلمودی را در محوطه دیوار براق در مسجدالاقصی به‌جای آوردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/681603" target="_blank">📅 09:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681602">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
امتحانات دروس تابستانی دانشگاه‌ها حضوری شد
وزارت علوم:
🔹
امتحانات دروس ارائه‌شده در تابستان ۱۴۰۵ دانشگاه‌ها و مراکز آموزش عالی باید به صورت حضوری برگزار شود و برگزاری این امتحانات به شکل مجازی ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/681602" target="_blank">📅 09:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681601">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
قائم‌پناه: پول فروش فیلترشکن به جیب وزارت ارتباطات و اپراتورها نمی‌رود
معاون اجرایی رئیس‌جمهور:
🔹
گزارش مقامات امنیتی نشان می‌دهد استفاده از فیلترشکن‌ها راه نفوذ دشمن و جاسوسی را آسان‌تر کرده است.
🔹
فروش فیلترشکن بین ۷ تا ۱۲ هزار میلیاردتومان عواید دارد که نمی‌دانیم به جیب چه کسانی می‌رود اما می‌دانیم به جیب وزارت ارتباطات یا اپراتورها نمی‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/681601" target="_blank">📅 09:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681600">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e926fa28dc.mp4?token=LO2ckdyfKOJ-PtrBYuDAl6bN1GBiulp8dhLLdEI037-jFOPxqHolYmeKsELYbOd9l9gbONrTZnkHCU-gmb_zuPjkZzGQJSgzkGI-YXka6E6T3S3VIrontzu4ePxX8XM8im33vJn8rJbfzWHuxMfPwS50mVTyyT97-1AB4ZRG_wit8_2iVPgU-83FT76V-76yaqzowPrblFu6nawrtzRN1Z6gkY8r5P4tH2CQGi6GwiTftPNFKLkQzwL5nmpexK4_bGcUmV0b1YWJ6YEWWkZdU8uQEiEl_uFE1CzyCug7r6tnA9ZF1l-s2X7KPh723OXJ9_dcImJE6CX_LElkyj_LJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e926fa28dc.mp4?token=LO2ckdyfKOJ-PtrBYuDAl6bN1GBiulp8dhLLdEI037-jFOPxqHolYmeKsELYbOd9l9gbONrTZnkHCU-gmb_zuPjkZzGQJSgzkGI-YXka6E6T3S3VIrontzu4ePxX8XM8im33vJn8rJbfzWHuxMfPwS50mVTyyT97-1AB4ZRG_wit8_2iVPgU-83FT76V-76yaqzowPrblFu6nawrtzRN1Z6gkY8r5P4tH2CQGi6GwiTftPNFKLkQzwL5nmpexK4_bGcUmV0b1YWJ6YEWWkZdU8uQEiEl_uFE1CzyCug7r6tnA9ZF1l-s2X7KPh723OXJ9_dcImJE6CX_LElkyj_LJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در بلژیک
🔹
بزرگ‌ترین آتش‌سوزی ثبت‌شده در تاریخ بلژیک در منطقه «های فنز» در شرق این کشور گسترش یافته و تاکنون حدود ۲۷۰۰ هکتار از اراضی را سوزانده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/681600" target="_blank">📅 09:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681599">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca8d3f6f8.mp4?token=mFxj0UGShogxWA5NOXcYRhzBEu8Ll0hgN5fWebOgv_w4Ppd0f65uc-omRjrUaZmCxvE7M_fwPVQpkPZLd3oWDSnyLy2b79pJl0mUw2JpbEn8hlKYH8Qj_YZd-aYK8WY-SGb5jqeWPstcS4ESCCxp-9RvH0mkAnuC6GI7kbnr77OyYhuOwsVlpb1mgwHwhuPMuoC9wbzWDlyFvEQDXwlZJ5ZPHCIJZvo263c9bojUQ3FM67I3uyUm9Ye6vLwLV3u5tDGrEhosMZ_s7ofLSc6jGMyS9ki3e-SpHPpxt2Uw-eI6OpqQEO3Au2EQRjzHdeasz_cw41uqRHLfE4pcPVPflg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca8d3f6f8.mp4?token=mFxj0UGShogxWA5NOXcYRhzBEu8Ll0hgN5fWebOgv_w4Ppd0f65uc-omRjrUaZmCxvE7M_fwPVQpkPZLd3oWDSnyLy2b79pJl0mUw2JpbEn8hlKYH8Qj_YZd-aYK8WY-SGb5jqeWPstcS4ESCCxp-9RvH0mkAnuC6GI7kbnr77OyYhuOwsVlpb1mgwHwhuPMuoC9wbzWDlyFvEQDXwlZJ5ZPHCIJZvo263c9bojUQ3FM67I3uyUm9Ye6vLwLV3u5tDGrEhosMZ_s7ofLSc6jGMyS9ki3e-SpHPpxt2Uw-eI6OpqQEO3Au2EQRjzHdeasz_cw41uqRHLfE4pcPVPflg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعویض پرچم گنبد حرم امام رضا(ع) بعد از ۶٣ روز
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/681599" target="_blank">📅 09:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681598">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ورود دیوان محاسبات به نقل‌ و انتقال درآمدهای نفتی از طریق شبکه تراستی
🔹
آغاز ثبت‌نام آزمون دکتری وزارت بهداشت از امروز
🔹
روسیه: اوکراین به دلیل توقف فعالیت بنادر ۱.۷۵ میلیارد درلار درآمد صادراتی را از دست داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/681598" target="_blank">📅 09:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681597">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfDLM_uM38dKv9RdY7nzHhwfdcIwl12umEkwbDjZfGuOhQ01Ebr8U-x-LXpnBpP1sX4RRatgd245EKRXjNF4vAfqaRpXi1fiIi03teQlhC9zxBkSVJLDCvQL5MMhpWEHxvDYAfknIJeY5TB_sLAb0Z7g0hpFWYaoW55nv7PgxDsEZIJzua2QVVgFBOJCDXG6RFCoqxY04yuLgoheBhV3Iyuab1_rawSbAojzRHLA41eKdUFUlUFycq0eqSNj8udVFThtTJQfT61G5f6vFotFr_akXoz74JaAzVN2SUdU8yPPQopC_qgvmKDSZLoG1XM2Amww3_ZLHb2THFmZj4ScoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربردهای سرکه برای تمیز کردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/681597" target="_blank">📅 09:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681596">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c06bc234b5.mp4?token=lrgUd0CMitDy8OZv93Ria_6GGxukb-OWX5FDXZcNN5wnKcxxmLlDDx-yKXoBR9e6nImFvJ06TlNUZf0eOBXsYmOT-73biHQD6czd9gSe8tk2gR4xyq9bpw38q779UukRfM3qw2BHQpmMN2onroowpvnbbMm88Vvi1WZ1axx6cZZa_hnwRwYOexVjKa_6hoORpW5uEw9YueLzY2WvfSnhPSiWpH7K8wbhlbiTJ8nDoq2D59ZcAwq_VQls7X_2WkAkmp6tXq9-HGpYIYixBKNwhL1jzWGj6GWWNueF5OFnl5uEgyJXN64NoLd7lrqElIKd3tFEtvUu5JaoEp8nFzcVDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c06bc234b5.mp4?token=lrgUd0CMitDy8OZv93Ria_6GGxukb-OWX5FDXZcNN5wnKcxxmLlDDx-yKXoBR9e6nImFvJ06TlNUZf0eOBXsYmOT-73biHQD6czd9gSe8tk2gR4xyq9bpw38q779UukRfM3qw2BHQpmMN2onroowpvnbbMm88Vvi1WZ1axx6cZZa_hnwRwYOexVjKa_6hoORpW5uEw9YueLzY2WvfSnhPSiWpH7K8wbhlbiTJ8nDoq2D59ZcAwq_VQls7X_2WkAkmp6tXq9-HGpYIYixBKNwhL1jzWGj6GWWNueF5OFnl5uEgyJXN64NoLd7lrqElIKd3tFEtvUu5JaoEp8nFzcVDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرداخت وام ۴۰۰ میلیونی برای اسقاط خودروهای فرسوده
🔹
رئیس هیئت عامل سازمان گسترش و نوسازی صنایع ایران با اعلام آغاز اجرای آیین نامه جدید نوسازی خودروهای فرسوده از هفته آینده، از پیش‌بینی وام ۴۰۰ میلیون تومانی برای دارندگان این خودروها خبر داد.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/681596" target="_blank">📅 09:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681594">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
فرمانده سنتکام سفر خود به خاورمیانه را پس از بازدید از ۶ کشور و یک ناو هواپیمابر، به پایان رساند
🔹
فرماندهی مرکزی آمریکا، سنتکام، اعلام کرد براد کوپر، فرمانده این نیرو، سفر ۱۰ روزه خود به خاورمیانه را به پایان رسانده است.
🔹
این سفر شامل بازدید از ۶ کشور و یک ناو هواپیمابر نیروی دریایی آمریکا در دریای عرب بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/681594" target="_blank">📅 08:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681593">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d327e215b7.mp4?token=sZKkmaA4qLQR18IVSv2EHNMDr_pmTp1QaDfoWNPqxisGRIxkIdU2OnU3x-9raEoFZ9MdoV8mgPTKlBPNojigZrfNLL5sXnPshGZouwbZBSjaBrpTPqxXn9f-CBJCTRdlNDTEtHMYmjMP6zIkdOgua4zPwG66iDEzrUjrtDGrqAKnn633q5Uvd4WFOkjtJuqFvdFU8Q6H_Czp9G95rK6KqBkb87-k-yZAkPjhLXmiOx_VHl7le_PbX_Z5yhtG3VK9msUA7S7ZktCB3GIZdvNGKrF5a5n_vmESiwvCrp45PQUeldsjXx-ztlocR88B7vnGk9n674V69IjjBcoLSVt8hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d327e215b7.mp4?token=sZKkmaA4qLQR18IVSv2EHNMDr_pmTp1QaDfoWNPqxisGRIxkIdU2OnU3x-9raEoFZ9MdoV8mgPTKlBPNojigZrfNLL5sXnPshGZouwbZBSjaBrpTPqxXn9f-CBJCTRdlNDTEtHMYmjMP6zIkdOgua4zPwG66iDEzrUjrtDGrqAKnn633q5Uvd4WFOkjtJuqFvdFU8Q6H_Czp9G95rK6KqBkb87-k-yZAkPjhLXmiOx_VHl7le_PbX_Z5yhtG3VK9msUA7S7ZktCB3GIZdvNGKrF5a5n_vmESiwvCrp45PQUeldsjXx-ztlocR88B7vnGk9n674V69IjjBcoLSVt8hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روسیه: به نقطه سوخت‌گیری اوکراین در منطقه خارکف حمله کردیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/681593" target="_blank">📅 08:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681592">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad21162ec0.mp4?token=KzRTCy67dW5tPpkhqOlvHG1ehTSiqqAMUSab7O19l9-Xj1eraZPmI7ox5BE3qwK_DSy0m1r0_pDQwCs1Z74jTkLneujQLqXeHQXFYc__i9hLj6MlFRF2hOtO2Nk9QC_cKPdzhWJzfmFqK1zIbFAv6Z5uocapiuDWrcK_tqpxmo3fB0bGn9vIehGF6FWH_Ndnfexmmm9NSmJB1i9FReLSfeE0SWkw7rxFQOl6Gewkb4jQpYl091fhD3G8PCVH_Jff42ZVrUY0pGUV947vX3hfAQqSzzAGdV5JNPVvoDQJWifXV52FFevdMx4cvv0z_WO0M1JTzQd6k4GST3gn2FW2Fg5bWCdLwG1qPHzv_F-6uobb1vX3yZpGnV_finxswdWo6XS4WkxwJ5y5P7x4ZMsJK2km9doRvn8lIB1q-cnuvhqTsf0DAViBNs95wZ5WiWVHZqSDinu3pXyqxp7EIEuOT-UK3GNh2uPfFBDedmcFqSyUVJkmTfpAFxDABLHSWk-27_Nq4AyHTakFIHdgi6DfGUBimcuC42ETn47MhjKYiPhC2NjxXcZSlvZ_yt8Ewn9wxfOzd2VqlrihY06zI3Gz2SozcLZGesngSyRm98S7wyNMcCAVrEuTAnJ5NjAaZVccHOnM3yqYqtBiyoam0JczLCZCDU_xYuhqK_JAXRCy3os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad21162ec0.mp4?token=KzRTCy67dW5tPpkhqOlvHG1ehTSiqqAMUSab7O19l9-Xj1eraZPmI7ox5BE3qwK_DSy0m1r0_pDQwCs1Z74jTkLneujQLqXeHQXFYc__i9hLj6MlFRF2hOtO2Nk9QC_cKPdzhWJzfmFqK1zIbFAv6Z5uocapiuDWrcK_tqpxmo3fB0bGn9vIehGF6FWH_Ndnfexmmm9NSmJB1i9FReLSfeE0SWkw7rxFQOl6Gewkb4jQpYl091fhD3G8PCVH_Jff42ZVrUY0pGUV947vX3hfAQqSzzAGdV5JNPVvoDQJWifXV52FFevdMx4cvv0z_WO0M1JTzQd6k4GST3gn2FW2Fg5bWCdLwG1qPHzv_F-6uobb1vX3yZpGnV_finxswdWo6XS4WkxwJ5y5P7x4ZMsJK2km9doRvn8lIB1q-cnuvhqTsf0DAViBNs95wZ5WiWVHZqSDinu3pXyqxp7EIEuOT-UK3GNh2uPfFBDedmcFqSyUVJkmTfpAFxDABLHSWk-27_Nq4AyHTakFIHdgi6DfGUBimcuC42ETn47MhjKYiPhC2NjxXcZSlvZ_yt8Ewn9wxfOzd2VqlrihY06zI3Gz2SozcLZGesngSyRm98S7wyNMcCAVrEuTAnJ5NjAaZVccHOnM3yqYqtBiyoam0JczLCZCDU_xYuhqK_JAXRCy3os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گربه‌ای که ۳ بار زنده موند و نجات پیدا کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/681592" target="_blank">📅 08:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681591">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
غریب‌آبادی: یکبار برای همیشه واقعیت را بپذیرید: تا اینجا، شکست های راهبردی و سنگینی خوردید؛ تنگه هرمز ایرانی بوده، هست و خواهد بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/681591" target="_blank">📅 08:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681590">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
نمونه‌ای از غذای در حال سرو در آبراهام لینکلن
🔹
یک ملوان حاضر در ناو جنگی آبراهام لینکلن، تصویری از غذاهای سرو شده در این ناو را برای یکی از اعضای خانواده‌اش ارسال کرد و گفت که این غذا شامل مقدار کمی از همه چیز موجود بود، نه غذاهایی که به طور شخصی انتخاب…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/681590" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681588">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc6914b5cb.mp4?token=Oop2orBl7nMJmTto4KNXTo80WKPol1v6Gf_deH1iMRcs9c6d_aLirO_enC5FDYqiOP33mQpPEZr-hREabgxmkIgLvQdV5v09k1fcUienOmwTr4VI0nk00V6QDXUFK7yuOSM8tE9f619Lra8IUw5c98Hf1-3POpoEVuIbOS9EDHcLYTmBim5BIjD5AhQTnggwfMxf2pEDWv7QXKNMBb1zwEZCoQ8l9ZZygR1dz1gN_NyUWKDiPq6KeBdmlEwXGYk6Fd3usHVGq2YQ6p6bQa2XvgJmPHfZdl5Z1ODtxiw_P4gsJG_kL5RZcivti6CFrVazhIulaW_MCewmUCVFa7qQCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc6914b5cb.mp4?token=Oop2orBl7nMJmTto4KNXTo80WKPol1v6Gf_deH1iMRcs9c6d_aLirO_enC5FDYqiOP33mQpPEZr-hREabgxmkIgLvQdV5v09k1fcUienOmwTr4VI0nk00V6QDXUFK7yuOSM8tE9f619Lra8IUw5c98Hf1-3POpoEVuIbOS9EDHcLYTmBim5BIjD5AhQTnggwfMxf2pEDWv7QXKNMBb1zwEZCoQ8l9ZZygR1dz1gN_NyUWKDiPq6KeBdmlEwXGYk6Fd3usHVGq2YQ6p6bQa2XvgJmPHfZdl5Z1ODtxiw_P4gsJG_kL5RZcivti6CFrVazhIulaW_MCewmUCVFa7qQCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: چند ماده‌ی باقی‌مانده از لایحه جرم‌انگاری جنایات جنگی امروز تعیین‌تکلیف می‌شود
🔹
هدف محکومیت مرتکبان جنایت علیه ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/681588" target="_blank">📅 08:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681587">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0567e2a2ee.mp4?token=lwu0XCPFq8qUHvRBQhXlKV6il59W4_5yoWX4sJUMFS5udcUZveKNW8Os7RuJMvUJvhTcCY1Dbyti7RvBviYDtjTk0OL141sWHvK2hRaUaPTgOb0okgFXWJd41HfIV5dDKi-1H9QTyZr4qAHLuhC_AI78KOjToK9ZppJVxH7a-lBGrIjeu6gRkxb5O3lxBt92ig1D2FaVaGux8OaM62PiOMN6v17PAv1r39pDeZYj3k5iOpm1USUgxCdJsz--thuDJVSB0mCZ3ZfEFK5YYY-Rfc6Dn3q6ukDCLrJUMxMVKFRbyg-dmc4acAFDklOSGgLQdP1oNb91m_obYjyJ5brY5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0567e2a2ee.mp4?token=lwu0XCPFq8qUHvRBQhXlKV6il59W4_5yoWX4sJUMFS5udcUZveKNW8Os7RuJMvUJvhTcCY1Dbyti7RvBviYDtjTk0OL141sWHvK2hRaUaPTgOb0okgFXWJd41HfIV5dDKi-1H9QTyZr4qAHLuhC_AI78KOjToK9ZppJVxH7a-lBGrIjeu6gRkxb5O3lxBt92ig1D2FaVaGux8OaM62PiOMN6v17PAv1r39pDeZYj3k5iOpm1USUgxCdJsz--thuDJVSB0mCZ3ZfEFK5YYY-Rfc6Dn3q6ukDCLrJUMxMVKFRbyg-dmc4acAFDklOSGgLQdP1oNb91m_obYjyJ5brY5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیراندازی کور در آمریکا؛ کودکان ۴ و ۱۴ ساله در میان قربانیان
🔹
در تیراندازی عصر شنبه در پارکی در شهر لکسینگتون ایالت کنتاکی، پنج نفر هدف گلوله قرار گرفتند.
🔹
پلیس اعلام کرد چهار نفر از مجروحان از جمله دو فرد بزرگسال، یک نوجوان ۱۴ ساله و یک کودک ۴ ساله دچار جراحت شدید شده‌اند و حال آن‌ها وخیم اعلام شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/681587" target="_blank">📅 08:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681586">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0297adfe5.mp4?token=lu9cvvBbqI0If1_dZJm1v97dDeMRpqfM_lQ9x1IHpO2jbZpmSSDf79o2GKjheu56j8r9BzPEbxLpgK4tASquXEw72y81zH8Fa-Edaw2sS6ktIw6tt6Z6bb1ahmQ65sRmWc_IOnBMPQFIcaUjYatkzaD9l85F28gkK9qE16zGmjNg64ZKEshPuJ6UwgnUQVAvWWSAwuls02VBAq8WdDixAnA7awoSEUNCjkh9m23gkdy60alfo_u-eKJl8sWIVWS8u1FPXSgJQZxEytZCRsXrtfSAXFYlZOFzCEzyQ-6qstAG2aKH70kefQzVdus8Gtjc35XDS8u-GUBOadFJKCN0nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0297adfe5.mp4?token=lu9cvvBbqI0If1_dZJm1v97dDeMRpqfM_lQ9x1IHpO2jbZpmSSDf79o2GKjheu56j8r9BzPEbxLpgK4tASquXEw72y81zH8Fa-Edaw2sS6ktIw6tt6Z6bb1ahmQ65sRmWc_IOnBMPQFIcaUjYatkzaD9l85F28gkK9qE16zGmjNg64ZKEshPuJ6UwgnUQVAvWWSAwuls02VBAq8WdDixAnA7awoSEUNCjkh9m23gkdy60alfo_u-eKJl8sWIVWS8u1FPXSgJQZxEytZCRsXrtfSAXFYlZOFzCEzyQ-6qstAG2aKH70kefQzVdus8Gtjc35XDS8u-GUBOadFJKCN0nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرین کامل عضلات شکم بدون زمان استراحت/ بدون نیاز به تجهیزات در خانه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/681586" target="_blank">📅 08:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681584">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSbk6Lvtto7IX180-r34H6xyBgeoMreW06y30kwjILwxlS6Yl7TuKefwr0hcGrwfMuREmTmofrs2v0BZJflTe-XDMJSa4OklPBs6_TrkvWiM0KnZH8FjqmVKOIbr3O5pkvk54mUyI-_O6p8v7zmVlh2w8e7e8mD7D5-heRchuB6xKdUCM1-hwnJsB3i5Ay-WBSML4TmnzuxMLcQhMvfp3v4FDHNeakQsqJxtdAbqPxw33B14iHF9GQAp9TeJS6XXqoP1vHRleIwG8glp9y_fRy5BXrZmZ4paaZyRS36CkgOrz8G6PrOdaFJI17K0snBbxkYIrFwjBwK5e02GgX2YvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دانشمندان با تلسکوپ جیمز وب نوع جدیدی از اجرام کیهانی با نام «ستاره سیاه‌چاله» کشف کردند
🔹
اخترشناسان MIT نوع جدیدی از اجرام کیهانی را شناسایی کردند که ظاهری شبیه ستاره‌ای غول‌پیکر به اندازه منظومه شمسی دارد، اما رفتار آن شبیه سیاه‌چاله‌هاست. این جرم ۱۰۰ میلیارد برابر بیشتر از ستاره‌های معمولی انرژی ساطع می‌کند که علت آن وجود یک سیاه‌چاله فعال با جرم ۱۰۰ هزار برابر خورشید در مرکز آن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/681584" target="_blank">📅 07:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681579">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کالابرگ سرپرستان خانوار دارای رقم انتهایی کدملی ۳، ۴، ۵ و ۶ شارژ شد
.
🔹
فردا؛ آغاز توزیع کارت ورود به جلسه آزمون های سراسری و دانشجو -معلم
🔹
هیات حماس برای بررسی تثبیت توافق غزه وارد قاهره شد.
🔹
آغاز پروازهای مسافربری میان روسیه و سوریه پس از ۱۸ ماه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/681579" target="_blank">📅 07:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681578">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSn1NHVnyWVukU6CCGgDCLtGQNRgBSvMPEj9WOPDkTMYwT_yg2ZzKY3X8ULFuIFg3S-yvk58l5zZNm-4dfcS4lXiCAVN6FErdjXnzdUBMjsoaJOo0sqV-KDTuyzQs5Fr2zIwcgF1h6_UsFqK5Wyb2h97-HoweeDirSvTqc1gV9A7tPqVOskV7OHEP-kgL5ly6wW1BOTezU9iMrnPn1XJDUU2pNQnzrpTaSDGAHo5CX8hboy8Ayq_TD1iFAj23AC98Svvo1aEUcvrpC_MqQ6NvtBuXenCHklDaUcAIFXfX8Gj2a9gGg-pg464nyrh0ox4W0iqHWx-6ggz_ladRp1tGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راننده خودروی مرگ چهارراه گلزار کرج اعدام شد
🔹
«شهرام صادقی» که در جریان کودتای آمریکایی-صهیونی دی‌ماه پارسال با خودروی پراید ۷ مأمور فراجا را زیر گرفته بود، پس از شناسایی، دستگیری و محاکمه، سحرگاه امروز اعدام شد.
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/681578" target="_blank">📅 07:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681577">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-CxuO33JGdSNX7og1PqbawKVF2wX-TOsxBfQ52N06Z1gE0O84CqjJ1HJHFntOEzeSTQZfBqQ0aQ8ZH81wr32JU0HIV49-_3OYme9uQn7zN7wc6USDM11XEvXiUvx6xGC_zqfjWMxn88dtrZTbbaRSyDYEaMavDgAKJykUTs63kUrD8Y8YmsmnLjD3r5eEzJlGDadCVBZ-8I0Z1YuQ2OfMTPsdRp6-HXO2pl09OHfY5Uie7s0ZlJ00xwbqL8HxylWAEpW03OS2y66Ez54N18AoZwdclMnGgd3e8tIVTB73RTC-PhgW7QUn9vpXEinItOBkGCmrvRbs2b2ajgs7baTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۲۵ مرداد ماه
۳ ربیع‌الأول ۱۴۴۸
۱۶ آگوست ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/681577" target="_blank">📅 07:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681575">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hx_sRBI3zx1qj7FtU4nvNHS47pSzs2NdCKTFou6sHPxnyEa8kDxWrqkdnu5LgXrL3gU29uYizJpaUvR3MQv3m4EsbNk-eacWGWgVCf97PcFVBDCerwlJzfH0tIN2qBtBZN-cXtzTQcBnYzvJT4LqcbpxJwIbWG7T8gWQBNeLvoi95v50VFeUqEH5SG_ezZu-kmBpoOgnex01OGiiYCGWB5MYo7o48KX3ewvsJ_xoF8p0PfZX4B3-4wW8KvFdOyaQv_sqjvIenHsvfcrNaI-vfGXTEiIICjDXceQbkgntT6qAwsj35jLXIXTUfsGPIAFhqiB7b6Uw6-BGdxX-u1tngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
اگر دانشجو هستید یا در ۶ سال گذشته از دانشگاه فارغ‌التحصیل شده‌اید، از شما دعوت می‌کنیم در این نظرسنجی علمی درباره کنکور و قبولی دانشگاه شرکت کنید.
⏱️
زمان پاسخ‌گویی: حدود ۱۰ دقیقه
🔒
پاسخ‌ها کاملاً ناشناس و محرمانه است.
پاسخ‌های شما به شناخت بهتر تجربه‌ها و دیدگاه‌های افراد درباره آموزش عالی کشور کمک می‌کند.
برای مشارکت در نظرسنجی، لطفاً وی پی ان خود را روشن کنید.
🔗
لینک نظرسنجی:
https://harvard.az1.qualtrics.com/jfe/form/SV_6MsiAUIGfXgJZQy</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/681575" target="_blank">📅 02:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681574">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM1iI2fxmr39AhFDbugaofArTnM3tlBVTBIYoNVwgC0sXbZ-POqyaIwqhIo6UWHow0g69afxCnwGKuwsXp7xjzT6F5TUwOxsFJ7lxXLjYSlJK-VUsrKduX6rwJzfzLqQ9fWtfc6tAu1P3ViNW0VF60ds4h7eTbG9SXXWEUroeI5U-Be88hNuypx-8mgoh5Zdd1h5vMOlUzBoxwJuo4CMcRcjxHRe3n69sXumfg3RlkSH36k-w9pCddw6OHiSZ18VmAP23G8iBezI9bfYWrP-WfIQ3Y6m5H1d0AyYGRBouNjrufa8B_CUBqjrWr-Wz_4SyxvejFteLUhrms3eceyuJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان تروریستی سنتکام نقشه‌ای را منتشر کرد که در آن، نوار غزه و کرانه باختری اشغالی به‌عنوان بخشی از اسرائیل [اراضی اشغالی] نشان داده شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/681574" target="_blank">📅 02:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681571">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSt2o1H-ZtKNxamatR3HZKr3bJgcIiZn-bmAYPHGRrSoZWv-gMq3sLQ9Ax3pQrLWnjoek5Jb4Vquo40LzO-8TbsoUdMIOYDrVJcd8fUc483nsRAkMwTRnng3Mk1zt-xtG_OpImsy3Frqcf4HyQgdV9ou7CFp1qm-FHvxkseAFBhAp_uw2BoPxpWrySsjUxXkJ_KMZ-LNNjOy3lQtLapfwzu3mY3WMHfALCaE2ZejcOK1-7qGJy_d_JSeXm1xChBg919EH68XRzIsMaFG7nl50tmEQxS2lSeaAEH0Fmq8nMKak9rcZ59KkDwbAhNRcAgw7917uNSdsH53YVmSNXgGNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمسخر ترامپ بعد از فرار با کانتینر حمل آشغال مواد غذایی از ترس تهدید ایران همچنان ادامه دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/681571" target="_blank">📅 01:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681570">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fI8p9x_INacqvzcbLTzbGGgww11k7rEdTqfQi7A2qGq4q6-9llXj4huGkqFvzwgkeJDWDkvCE4_46nmfpTD4FeWi3YytqwpZ03NSwEt_Z05ca2ayBD8IEp1nbljz-Z3eRzMetmb8vqb772TobCRohFV4hmrOBPSSVhM30dGw1DxAOt1VgYD_1U-vqMdX8bBFtBksJUOJTsU1Cq_L4cZmudMzPgjjoDsOcXVrEkMSdEmWaflSEdFxSn7VXEsEMXvndokGNN_gF6SQAZGGMZ6uWn-LwucOTfqzTA1aWt25WD4VJKDm6OnARPixHvgBk3Sw1U1O35XLA4p4AQiKCM7caA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراهیم عزیزی: رئیس‌جمهور آمریکا باید نگران امنیت خودش باشد
رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس شورای اسلامی:
🔹
رئیس‌جمهور ایالات متحده به‌جای ادامه تهدیدهای بی‌پایان درباره تنگه هرمز، باید نگران امنیت خود باشد.
🔹
ممکن است شرایطی پیش بیاید که خودش مجبور شود برای حفظ امنیت، در یک کامیون حمل مواد غذایی پناه بگیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/681570" target="_blank">📅 01:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681569">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2a870060.mp4?token=AtsmykZ0ehqvkFBRA88pWAlw5H-HlyBP8-e_dA7jqOdpkTUGsPw3CbxYtJFkSX9lL2ETD5QZIRr_E_2yv28ByFXrTAywxGPt8XvOUmkKt64asE9gWV5M9jjJdFxfWgWQgzc7W3YdBOgB9-Le-mEUmpe8xhgTCepTat_aDdl_3VTHUC3rlv7ZiFEE8Vmhk1ZP_Fj_-WivcsNmpix_9qlXnu54Dd_37wNs4_wkv0TFMdAAqVNuL8EUJMxqakvmNucMMwG_c0XLan02Pmw1ufl_3H2gIq2lzG0XBKzzvWS8_nEeB4AO8r5EVfrpi1cUjs8jdNtxkUuY1Gy9MenBEbyb-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2a870060.mp4?token=AtsmykZ0ehqvkFBRA88pWAlw5H-HlyBP8-e_dA7jqOdpkTUGsPw3CbxYtJFkSX9lL2ETD5QZIRr_E_2yv28ByFXrTAywxGPt8XvOUmkKt64asE9gWV5M9jjJdFxfWgWQgzc7W3YdBOgB9-Le-mEUmpe8xhgTCepTat_aDdl_3VTHUC3rlv7ZiFEE8Vmhk1ZP_Fj_-WivcsNmpix_9qlXnu54Dd_37wNs4_wkv0TFMdAAqVNuL8EUJMxqakvmNucMMwG_c0XLan02Pmw1ufl_3H2gIq2lzG0XBKzzvWS8_nEeB4AO8r5EVfrpi1cUjs8jdNtxkUuY1Gy9MenBEbyb-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فارس: روز گذشته ویدیوهایی از برخورد تعدادی از عزاداران در مشهد مقدس منتشر شد که در آن چوب‌هایی به سمت هم پرتاب می‌شد
🔹
این فیلم‌ها بلافاصله با آب و تاب فراوان در رسانه‌های ضد انقلاب دست به دست شد و به نادرست القا کردند که این درگیری در صحن حرم مطهر امام…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/681569" target="_blank">📅 01:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681567">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a538aeadb9.mp4?token=X9T8xy4i8yeyAa-7VmBexS4HPDZv9-3NXgF5sg3Lgdp2TJw4BLyO611eMJgJGwRoqWe0b4PlZL13E7kzjegUYrJDxzRbQY94qktOV9Irk-FLBjmiwyaud4lpN_HHAn1wt5xuoZD0BUNcI_756rbqMPnQQRIanZ4ribp9esJAAPbnVoTReflmPACQ79OEDSmayvj3oBhq_ZRJD072aRWUUgvRnDW1vgoEl-8ssfOKAsxOAcvc_PB52l1-3VHiWxPXWtynVDPAOGtlzFNuDgJYGScmlqNmcWz7Wnq1QhmoZXu9nG20MipG08aDmnGSlDG-i4NyDV0wUrnAIqnXJNZkbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a538aeadb9.mp4?token=X9T8xy4i8yeyAa-7VmBexS4HPDZv9-3NXgF5sg3Lgdp2TJw4BLyO611eMJgJGwRoqWe0b4PlZL13E7kzjegUYrJDxzRbQY94qktOV9Irk-FLBjmiwyaud4lpN_HHAn1wt5xuoZD0BUNcI_756rbqMPnQQRIanZ4ribp9esJAAPbnVoTReflmPACQ79OEDSmayvj3oBhq_ZRJD072aRWUUgvRnDW1vgoEl-8ssfOKAsxOAcvc_PB52l1-3VHiWxPXWtynVDPAOGtlzFNuDgJYGScmlqNmcWz7Wnq1QhmoZXu9nG20MipG08aDmnGSlDG-i4NyDV0wUrnAIqnXJNZkbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه سبز شدن چراغ‌های قرمز حرم امام حسین(ع)بعد از دو ماه عزاداری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/681567" target="_blank">📅 01:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681566">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-poll">
<h4>📊 کدام طرح بنزینی دولت را بیشتر می‌پسندید؟</h4>
<ul>
<li>✓ طرح اول: قیمت فعلی؛ توزیع بنزین تا سقف ۱۲۱ میلیون لیتر، سپس توقف عرضه</li>
<li>✓ طرح دوم: سهمیه‌بندی بنزین بین خودروها؛ مصرف بیشتر با نرخ آزاد</li>
<li>✓ طرح سوم: سهمیه بنزین برای همه مردم، با امکان انتقال و خریدوفروش</li>
</ul>
</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/681566" target="_blank">📅 01:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681565">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
سومین طرح پیشنهادی دولت برای بنزین چیست؟
🔹
سقاب اصفهانی، معاون رئیس‌جمهور و رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی: در این روش سهمیۀ بنزین به‌جای خودروها به مردم اختصاص داده می‌شود؛ چه خودرو داشته باشند چه نداشته باشند.
🔹
روزانه حدود ۳۰ میلیون لیتر به حمل‌ونقل عمومی و تاکسی‌های آنلاین و غیرآنلاین اختصاص داشته می‌شود تا قیمت آن‌ها تغییر نکند.
🔹
تقریبا ماهی ۳۰ لیتر به هر فرد می‌رسد و امکان انتقال و خرید و فروش آن وجود دارد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/681565" target="_blank">📅 01:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681564">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
دومین طرح پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
🔹
سقاب اصفهانی، معاون رئیس‌جمهور و رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی: در این روش ۱۲۱ میلیون لیتر تولیدی روز بین خودروهای موجود تقسیم شود و هرکس بیش از سهمیه بخواهد باید بنزینش را با نرخ آزاد بخرد؛ تقریبا مشابه روشی که قرار بود در کرمان اجرا شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/681564" target="_blank">📅 01:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681563">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d76db735.mp4?token=h11cBVkYhz2fridAWe8ZGLarGeTV9147KsJlO_bWNlNrzqJMcKn3fQge0k1gbpjjUv7AeoubII6MpvBLhO418Iekhq9Nptq8QiYRXdXK2_ES2duVtLE09VW1-sEOSEHvf34eNVOrEo-vL5FmVWRfl5tzkBG_qpPHBgqkc4bv0mFi0svA2cJs8fj9_swwBTIKjoydrZ4BtPvPCVBNhACCEgLASZGjtkk_s2fB3k_rVAlQuk3L7Ght7X3sJqUtFbCdx8UtT-5PTNsJXiFpA9kw2W3eKctLUYW9A8NZS4roL-5gAQPRYMTaq-ZSfr6Lpvqz3T0fdgx2rFHtSVOusR1yjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d76db735.mp4?token=h11cBVkYhz2fridAWe8ZGLarGeTV9147KsJlO_bWNlNrzqJMcKn3fQge0k1gbpjjUv7AeoubII6MpvBLhO418Iekhq9Nptq8QiYRXdXK2_ES2duVtLE09VW1-sEOSEHvf34eNVOrEo-vL5FmVWRfl5tzkBG_qpPHBgqkc4bv0mFi0svA2cJs8fj9_swwBTIKjoydrZ4BtPvPCVBNhACCEgLASZGjtkk_s2fB3k_rVAlQuk3L7Ght7X3sJqUtFbCdx8UtT-5PTNsJXiFpA9kw2W3eKctLUYW9A8NZS4roL-5gAQPRYMTaq-ZSfr6Lpvqz3T0fdgx2rFHtSVOusR1yjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طرح اول پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
🔹
سقاب اصفهانی، معاون رئیس‌جمهور و رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی: در این روش قیمت بنزین تغییر نمی‌کند اما بنزین تا میزان تولید ۱۲۱ میلیون لیتری در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش می‌شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/681563" target="_blank">📅 01:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681561">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTJZ40_d0pLzdRqcuv4GJ-cRX022sy2s4BoOFkoFLQV_wHIGq63sfd56AIQCW41fji9aL2XqdCZiDPt6mkw7syBFaAUbGiEYINmjVBNFxwcHUP0E8QRhxKvLbRInudyOuSWtUOzCIryxQJ1icR_SfRor3oHXbgDmV88ixO41fw-F3BmdL-ZR8O8EZi8GjOJWG-SStfR1ARPZF40oOkg1NgoJX5HZWMc4tG30Iyqwqxs-6Bg7nkjcMUQjnJy6QlpT3eYi-J0X047KnlGI-othi6CQgv1jqEOtJagaU6-2M98RbC-ct1TM_1tNvXWBVg2TSp9yl6VnvOU3naSexbIvdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌بی‌سی: کاهش ذخایر استراتژیک نفت آمریکا به حدی رسیده که نگرانی‌هایی را درباره آسیب‌دیدن مخازن و توان عملیاتی آنها ایجاد کرده است
🔹
ذخایر دارای یک کف در حدود ۱۷۰ میلیون بشکه است که پایین‌تر از آن، «محدودیت‌های سلامت ساختاری حفره‌ها و زیرساخت‌های پمپاژ، مانع از برداشت‌های بیشتر می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/681561" target="_blank">📅 00:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681558">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUf7SUnzKmx53O0jib3OJdvOL5Dw-lJBeKQAts2cDRE1TQAm3M_gau18wNu8w427rjUY5qet5ZtaZXjRxFJeXTPq_uR2sPNgNLdRhkoe_joCgeE206EvtC29r7MJVWXALgYt1YO0N8Bmo2uoMinrySAsQyYryJoUCSCAnpJSbHH9RniXKgv5C_YnFMuGfWD8kVXHua0VYWkf-D14of051eO8CKaU5Ap9GpkGyNjf6hh40N071Pz4KfjCcPV141Yz7wepc_bS1a4qizgSF3BrG4mIV3CDHluwcnW3u8VhZVEzfZaeILIjcwZDzEwTabe0HIERf2pSY2OQK_RTWx9DXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ کلاهی با شعار «ترامپ ۲۰۲۸» بر سر گذاشت و نوشت: پیروز خواهیم شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/681558" target="_blank">📅 00:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681557">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe93a20077.mp4?token=jSoaG4WBy_3DjosVzLtvBS-mTeM-oycyZQ1NOVIuPcbPNQoCEehF0ZmbQL_1wB5GpimnKukrDbW0NWLRK05TsRy1ZVOcJJ-rZZg05G5Vt8jilkBbiCc0Uv4q1cFHSWA-CUIuBk-DOGWFnkERGGOjoo3NZErwmI_kkmzJCbkx2TsbQc5LQDQ2hgKIFJbRKTN1Z-WUGMM1by-GHehLF6hX0MeiA9SnnMYsJOoCu8dVey7VXEdNmqWDHYI5FmJCrqkzjAjVENP9gPFpK3Njc0o31sUDtMlAuuRZt4dnSeKhPITletA8GdzFTfU56hidS_Gf8Ro8LIb4WeMjUXw4HSPdtZBzDiCSlEsXPC5VQnIeJt_DggmjgF5zwx6RfTLXSXMOIY2GrY8bnGa9_U75-PYXcRZyi-TqAZ0GRvIrQdNRCXZ_xmf0dVndS9ppKm2W_ujp1x9PMUFnycz9ArfsrPb9bv_D9oIbzhvmgpUxbxU_MTBIawaiQ68GD6toB0NhsUi0pSvqTftoqUcWXBVH9YJ8EU5R6WPSwwTKHIt_EYaxB6jhg4jqfbGndfwxZKSyi7L8KS2AYr_YNcMTI9y_oIf2_Ut0EQgl2Ukm2fBaWsmI6s8A6Q_33GPMW_Y8EIAd0fP8amNrQfDhBKyvxRET3XmNXWClKxkK6AZRXNzR_2f0GSk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe93a20077.mp4?token=jSoaG4WBy_3DjosVzLtvBS-mTeM-oycyZQ1NOVIuPcbPNQoCEehF0ZmbQL_1wB5GpimnKukrDbW0NWLRK05TsRy1ZVOcJJ-rZZg05G5Vt8jilkBbiCc0Uv4q1cFHSWA-CUIuBk-DOGWFnkERGGOjoo3NZErwmI_kkmzJCbkx2TsbQc5LQDQ2hgKIFJbRKTN1Z-WUGMM1by-GHehLF6hX0MeiA9SnnMYsJOoCu8dVey7VXEdNmqWDHYI5FmJCrqkzjAjVENP9gPFpK3Njc0o31sUDtMlAuuRZt4dnSeKhPITletA8GdzFTfU56hidS_Gf8Ro8LIb4WeMjUXw4HSPdtZBzDiCSlEsXPC5VQnIeJt_DggmjgF5zwx6RfTLXSXMOIY2GrY8bnGa9_U75-PYXcRZyi-TqAZ0GRvIrQdNRCXZ_xmf0dVndS9ppKm2W_ujp1x9PMUFnycz9ArfsrPb9bv_D9oIbzhvmgpUxbxU_MTBIawaiQ68GD6toB0NhsUi0pSvqTftoqUcWXBVH9YJ8EU5R6WPSwwTKHIt_EYaxB6jhg4jqfbGndfwxZKSyi7L8KS2AYr_YNcMTI9y_oIf2_Ut0EQgl2Ukm2fBaWsmI6s8A6Q_33GPMW_Y8EIAd0fP8amNrQfDhBKyvxRET3XmNXWClKxkK6AZRXNzR_2f0GSk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قبل و بعد از لوکیشن‌های فیلم Terminator2/ فیلمی که هنوز بعد از ۳۰ سال کم نمیاره
🔹
جان کانر قراره آینده بشر رو نجات بده، اما یک ماشین از آینده برای کشتنش برگشته. خوشبختانه یک ترمیناتور دیگه هم هست که این بار مأموریتش محافظت از جان شده!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/681557" target="_blank">📅 00:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681555">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPv8a1ac_TS2RtZ2zlqmh10PlOaA39yNO_TiN7Z2jm1ZpxiZG-mrkKB6W8_SXwbJLcFXOlV9T6mWtZtM9TZh3XrhI2yrNqf2U55wMgVlPavhUNXAAdhm6myj2ceW1ImRXBsF7CtL8QuQEQOxkfdtZLNsiDfKBaaxSSUSxCBOzO45c90LuflgDJtO78Vr9WO5sHN9duCnPVqP_dysaXtE9E-JXYaOCQz-Gz6__t69lvVvYdbfgp4qjJXQ-remZP9WMJMp-VwQbll9wFPnmQ9psloyDXZQcS6rX9EowJT-lOG8VxY4s-Hn1svMeRrZzMNzXjhvBKyNE_oc0Ebecs5b6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/681555" target="_blank">📅 00:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681554">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
اسارت ۳ خلبان ایرانی پس از سقوط جنگنده‌ها توسط نیروهای قطری
👇
khabarfoori.com/fa/tiny/news-3237866
🔹
سه طرح جدید در پمپ‌بنزین‌ها؛ بهترین روش سهمیه‌بندی بنزین کدام است؟
👇
khabarfoori.com/fa/tiny/news-3237983
🔹
کارمند اخراجیِ اینترنشنال: هدف اسرائیل تجزیه ایران است؛ چه جمهوری اسلامی باشد چه حکومت شاهنشاهی
👇
khabarfoori.com/fa/tiny/news-3237989
🔹
طلاق مخفیانه بازیگر مشهور فاش شد | پایان بی‌سروصدای یک رابطه طولانی
👇
khabarfoori.com/fa/tiny/news-3237659
🔹
شغل این مداح مشهور طرفدارانش را شوکه کرد
👇
khabarfoori.com/fa/tiny/news-3237906
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/681554" target="_blank">📅 23:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681553">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9f8143e5.mp4?token=G8HFU-R7vAVSTiLf3FWjz-ASawl_xJGzAJlHJQsMwpKInvX0Fcn3m94RbYUo9AuAL-4qX7lwjU1FvHgJA94GokeS8Yoj9zAbD1CWHAuY0AZka8a3KF5bxLkzNP1EMQTnSJ2ifAQKkbxGRXYmGDkzAwocw2nPtpsbz8zfdjcn66CB3UfT1MnOOJXqwfzReOOcGla1StQJzNJ7wghA3J77B3lIxVnQjd78MPMZq7_1oO4Gpw3HfKWoS9VKwLIbH30x0V5W9yDEptNQaR4qf4xKFe8UxP_fTj5e74y5zeL-gAHDieN1tM2rcUU2llJA-pHsiZzAjnDPwm_9hC2zubf_Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9f8143e5.mp4?token=G8HFU-R7vAVSTiLf3FWjz-ASawl_xJGzAJlHJQsMwpKInvX0Fcn3m94RbYUo9AuAL-4qX7lwjU1FvHgJA94GokeS8Yoj9zAbD1CWHAuY0AZka8a3KF5bxLkzNP1EMQTnSJ2ifAQKkbxGRXYmGDkzAwocw2nPtpsbz8zfdjcn66CB3UfT1MnOOJXqwfzReOOcGla1StQJzNJ7wghA3J77B3lIxVnQjd78MPMZq7_1oO4Gpw3HfKWoS9VKwLIbH30x0V5W9yDEptNQaR4qf4xKFe8UxP_fTj5e74y5zeL-gAHDieN1tM2rcUU2llJA-pHsiZzAjnDPwm_9hC2zubf_Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمایت از تولید داخلی مسئولیتِ ماست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/681553" target="_blank">📅 23:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681552">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
طلای جهانی دوباره خیز برداشت
🔹
طلای جهانی پس از یک موج اصلاحی، خط روند نزولی را شکسته و دوباره نشانه‌های قدرت خریداران را به نمایش گذاشته است. این فلز گران‌بها پیش از رسیدن به محدوده ۳۶۰۰ دلار مسیر خود را تغییر داد.
🔹
اکنون ۴۱۴۷ دلار مهم‌ترین حمایت طلاست؛ حفظ این سطح می‌تواند پایان اصلاح و آغاز یک موج صعودی بلندمدت را رقم بزند. امروز طلا در محدوده ۴۳۷۵ دلار بود که ۱.۱۸ درصد نسبت به روز گذشته رشد داشت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/681552" target="_blank">📅 23:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681549">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dddeac06e.mp4?token=lshtcS4dS5zCVpgsu1xQRkpgXCOKM_zmzLYyExTl5AH13zj9M1mDzDQ6WhqJR-9qitQHOXJarMuk9nJL7-zNR37XmoI1q1EXn5YHDYuy34iYwhHzuRkPdxzh-NZ3tpyBVpk_ROksDlHpRDn-f5VbKjbhAqNNtGmigfFsKDFOvT16JUbq9WsIKcj1WiWC4jObWX5yh9ERnsWAT_Qv6XCM0fIJY0ZRLhfWsBVcjjZKRYFF4qfJCDikmyH-2HvPJ-I9d5BVS8GXyKIDVXKFm9_Agqt0VwMSOU653JeMSzHo_fAZOPAR0M5l-kfZqlc4MR39HKzHZ6wLC1qViO757z5STA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dddeac06e.mp4?token=lshtcS4dS5zCVpgsu1xQRkpgXCOKM_zmzLYyExTl5AH13zj9M1mDzDQ6WhqJR-9qitQHOXJarMuk9nJL7-zNR37XmoI1q1EXn5YHDYuy34iYwhHzuRkPdxzh-NZ3tpyBVpk_ROksDlHpRDn-f5VbKjbhAqNNtGmigfFsKDFOvT16JUbq9WsIKcj1WiWC4jObWX5yh9ERnsWAT_Qv6XCM0fIJY0ZRLhfWsBVcjjZKRYFF4qfJCDikmyH-2HvPJ-I9d5BVS8GXyKIDVXKFm9_Agqt0VwMSOU653JeMSzHo_fAZOPAR0M5l-kfZqlc4MR39HKzHZ6wLC1qViO757z5STA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیوه خاص مدارس ژاپن برای تربیت نسل آینده؛ تربیت کودکانی با مهارت‌های واقعی زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/681549" target="_blank">📅 23:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681548">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xx_XLi2tgD1sBRXUvicM738ditdRnv4spvUvqnKh8RK7yYhXAdz0cZSeTfX-7uv9UlVICatSAOeY5pgl3Hg06Ilpddk3wwAi6NspQL-8ho8v8CXMWQ3rTLyNCJniGhOndV6gkg2QBaE9w9ZXmF2QicSNHX8fk3T6dAa-WgFKCoJdt-b8Fb5kEcZe0kTwqfoZotJTCC7DHo5Of5vbwLlthpULfCunTwS7On4nAOZYQK5-nWFopPUk3Vwa8i_36dIDXBXKxvrqa-7iC7Inu9e3oOmaeneGCF6o3xL54d07W2xMaSoWKAzFxFsGUxg1SLEaiTfF4LxLifQ4L2QWcgQhLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارین پالسی: بله، جنگ ایران واقعا شبیه ویتنام است
فارین پالیسی:
🔹
ترامپ، دوست دارد اشاره کند که جنگ کنونی و درگیری ویتنام شباهت کمی دارند زیرا با وجود لاف اولیه‌اش مبنی بر اینکه کارزار ایران در عرض چند هفته به پایان می‌رسد، به طور غیرقابل مقایسه‌ای کوتاه‌تر از جنگ دوم است.
🔹
با این حال، برای هر کسی که امروز آن را مرور می‌کند، سخت است که تحت تأثیر این نکته قرار نگیرد که این دو جنگ چقدر با یکدیگر اشتراک دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/681548" target="_blank">📅 23:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681546">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb1b618029.mp4?token=HvCRN7-zeKRHR9R01wnyZBvMX9peuzpgDx-VM3RxZrYfblWubErRqWfQNkpR3JYVtrqGWh4aJk3UXixny5z_dLJVRdGEw6bCetHhIE4ZZGpKJEm6Q2t-72PFsCYYyRyfpX07gvIBoD7jUrkjZ-PCQe8B3cvLbaNy8bGVfIyHV3IjTOcqIoef9rOVpH2KBoh9uvkM6GWlYA6aYaYyLCNWnz706XYEc_iQAylVqhA8vSfPrzh7yDLeAzvpg2IHwiRHXttitsxcLx5s7h9D3Me209wEIqxq5ntOIhZvzPCRytW4fKaWo1PodTpT4FT93ZzWb6AQNwQ_Qp7gRZ1uhhq1fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb1b618029.mp4?token=HvCRN7-zeKRHR9R01wnyZBvMX9peuzpgDx-VM3RxZrYfblWubErRqWfQNkpR3JYVtrqGWh4aJk3UXixny5z_dLJVRdGEw6bCetHhIE4ZZGpKJEm6Q2t-72PFsCYYyRyfpX07gvIBoD7jUrkjZ-PCQe8B3cvLbaNy8bGVfIyHV3IjTOcqIoef9rOVpH2KBoh9uvkM6GWlYA6aYaYyLCNWnz706XYEc_iQAylVqhA8vSfPrzh7yDLeAzvpg2IHwiRHXttitsxcLx5s7h9D3Me209wEIqxq5ntOIhZvzPCRytW4fKaWo1PodTpT4FT93ZzWb6AQNwQ_Qp7gRZ1uhhq1fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غول روس در راند اول علی اکبری را ناک اوت کرد
🔹
در مبارزه اصلی برای کسب کمربند قهرمانی سنگین وزن ACA علیخان واخایف غول ۲ متری روس و شاگرد سابق بوایسار سایتی‌یف در همان راند نخست توانست امیر علی اکبری را ناک اوت کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/681546" target="_blank">📅 23:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681545">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ورود هندوانه و خربزه ایران به عراق ممنوع شد
سید رضا نورانی، رئیس اتحادیه ملی محصولات کشاورزی ایران در
#گفتگو
با خبرفوری:
🔹
عراق هر ساله به بهانه افزایش تولید داخلی برای ۲ تا ۳ ماه واردات محصولات جالیزی ایران را ممنوع می‌کند.
🔹
امسال نیز از ۲۰ مرداد ورود هندوانه، خربزه، خیار، گوجه‌فرنگی و بادمجان ایرانی به عراق ممنوع شده است.
🔹
باتوجه به مخاطرات جنگی در حوزه خلیج فارس، کشورهای کویت، بحرین و عربستان واردات میوه و تره‌بار ایران را ممنوع کردند که این امر منجر به خسارت به صادرات ما گردیده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/681545" target="_blank">📅 23:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681544">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
معاون رئیس‌جمهور: گفته می‌شود صنعت خودروی ما نوزاد است اما این نوزاد ۶۰ سال از عمرش گذشته است به نظر نمی‌رسد مشکل از شیر باشد و این داستان باید تمام شود ‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/681544" target="_blank">📅 23:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681543">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ادعای جروزالم‌پست: آمریکا دارایی‌های مسدود شده ایران را در ازای عبور آزاد از هرمز، آزاد می‌کند
ادعای جروزالم‌پست:
🔹
واشنگتن در نظر دارد به‌تدریج دارایی‌های مسدود شده ایران را آزاد کرده و تخفیف‌هایی جزئی در تحریم‌ها را در ازای اجازه ایران برای عبور تجاری بدون مانع و بدون عوارض از هرمز، اعمال کند. ترامپ می‌خواست ایران را فلج کند اما حالا به تهران یک پیروزی تقدیم می‌کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/681543" target="_blank">📅 23:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681542">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okZGllZa_zTubz5n84dbt6St-wCmRZd2qzf8dCU8fzxajdeeUU1Hz8j7XaHON8mN6xMJ-5g4n7ZjYl2ZSM-Xch2EhRHkIG5mv3vM2eCNSL22k1ZownJbJCT3N-eCDQV-N0VexbFzv8vck4oTcqCn2sWM4qKLGb06vSrRRpC18NHDBgCwPfEafrmkxkvXLpK6-n8XUdFPInCekwMngGckSExW9fM2-A-H9gtG6mX0kR8U1X7uTJa2b_5IbUoXp-UkFs6baShMQ1K_XHUDMmmWXj537we4anqBbnv5-mhsjggeY51zvDlSNn3XLHicJ5RfcOerugGtJWFhu-qEP1mpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمونه‌ای از غذای در حال سرو در آبراهام لینکلن
🔹
یک ملوان حاضر در ناو جنگی آبراهام لینکلن، تصویری از غذاهای سرو شده در این ناو را برای یکی از اعضای خانواده‌اش ارسال کرد و گفت که این غذا شامل مقدار کمی از همه چیز موجود بود، نه غذاهایی که به طور شخصی انتخاب شده بودند.
🔹
این ملوان گفت که به خدمه اطلاع داده شده بود که غذاها با هم مخلوط شده‌اند و افزود که لوبیاها از جمله بدترین غذاهایی بودند که تا به حال چشیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/681542" target="_blank">📅 23:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681541">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی: حدودا به هر عضو خانوار ماهی ۳۰ لیتر تعلق می‌گیرد حتی اگر صاحب خودرو نباشد
🔹
قابلیت انتقال آن به هر فردی که بخواهید وجود دارد. دولت مدیریت سهمیه را به افراد می‌سپارد.
🔹
قیمت دوم و سوم در این طرح وجود ندارد و سهمیه در کارت بانکی افراد شارژ می شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/681541" target="_blank">📅 23:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681538">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
معاون وزیر اقتصاد: وزارت اقتصاد صرفاً مسئول انتقال سهمیه سوخت به کارت بانکی است
مرتضی زمانیان، معاون‌ وزیر اقتصاد:
🔹
تصمیمات مربوط به سهمیه و نرخ در مورد بنزین در کارگروهی اتخاذ شده و هیچ دستگاهی به تنهایی رکن تصمیم‌گیر نیست. در این کارگروه دستگاه‌های مختلف سیاستگذار، اجرایی، امنیتی و رسانه‌ای حضور دارند/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/681538" target="_blank">📅 23:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681537">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b849fac5b.mp4?token=fvDpqauzVmw3iVy2ygdIESnGyNlA2ntnn5uACXkRZDu8crTKoGNVHJL8QIrLjPV0H10emkW_QRPMCkiKTb88iqyAFJNX9jjhtSMiO_vib5Nm9U6ZaLiRYogDBS08yHztWgrKyGU5iHcjxXes54v4JIdc7gffC8ZbZkUUxsJ_tD8KfKHGeWi0l35uEcxge9IKo6OZAFCxArx8PAxOjrmPGITx0fsnyLeaF-znGibbpICs1yhmjCFO7llRgDBum8_2gahBXsl5dsCG5rCoF0s3HFLGEgPrcgfsrs6OCVslV64RVzLguSi4mMJ4v58Zcjqs2ICA-pS7BteTH03rFcaR7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b849fac5b.mp4?token=fvDpqauzVmw3iVy2ygdIESnGyNlA2ntnn5uACXkRZDu8crTKoGNVHJL8QIrLjPV0H10emkW_QRPMCkiKTb88iqyAFJNX9jjhtSMiO_vib5Nm9U6ZaLiRYogDBS08yHztWgrKyGU5iHcjxXes54v4JIdc7gffC8ZbZkUUxsJ_tD8KfKHGeWi0l35uEcxge9IKo6OZAFCxArx8PAxOjrmPGITx0fsnyLeaF-znGibbpICs1yhmjCFO7llRgDBum8_2gahBXsl5dsCG5rCoF0s3HFLGEgPrcgfsrs6OCVslV64RVzLguSi4mMJ4v58Zcjqs2ICA-pS7BteTH03rFcaR7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‏
کارمند اخراجیِ اینترنشنال: هدف اسرائیل تجزیه ایران است؛ چه جمهوری اسلامی باشد چه حکومت شاهنشاهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/681537" target="_blank">📅 23:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681536">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqnmtGu5plCf8nk1_fsYthbGIrnsuXj_QdWlRt3wSv6vyp1U5ZfHUFkF7UpcyrkrzKjhhZEJy-VNF4O0CDAxf0VCBQivqc9hc1O2K5mRT-bdRDDFmVaYkAhei8App03QkEZuWSiPAfxYpvF8TdCQskwR3NocFD-0tUINC8jEJI5zywZZp_XJWCv5Aj4M6yc2KZY-iF7wxP0g1NPWu_P32lwQjMPVx1mlwXrM-XZsUFtLFBIvvU-sEzp1AJ2Vl1-KVOVRCKe73RcuD5TuMs2kCK8YK30_CLVjmoPNrWq1iP8Rr819wxqMwjUR0JcmxQLTfdJJtdBAS4JP_XJVHs6dbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهیه و بازسازی ۲۰ خانه زنان سرپرست خانوار آسیب‌دیده از جنگ با حمایت اسنپ
🔹
اسنپ از آغاز طرح «این راه به خونه می‌رسه» برای تهیه یا بازسازی ۲۰ واحد مسکونی آسیب‌دیده در جنگ ۳۹ روزه در استان هرمزگان خبر داد.
🔹
این طرح با همکاری مؤسسه خیریه «نفس آفتاب» اجرا می‌شود و برای آن ۳ میلیارد تومان بودجه اختصاص یافته است.
🔹
بر اساس اعلام این مجموعه، خانه‌های هدف در شهرهای بندرعباس، خمیر، میناب، سیریک، جاسک، بندرلنگه و رودان قرار دارند.
🔹
در این طرح بیش از ۱۰۰ خانوار آسیب‌دیده شناسایی شده‌اند که ۲۰ خانوار از آن‌ها زنان سرپرست خانوار هستند و بازسازی خانه، مقدمه بازگشت پایدار خانواده‌هاست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/681536" target="_blank">📅 23:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681535">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh32AvUSTNk9jFfdM3LKkvQfmVRrJeFqxqAtPcAMFvp_pYaqI0Z6yvgjpHXa7l9TzekFh_nIGR0pwaFaDQ75cmTz9KCqknHDtA7war-ysuloU3tLTEumc90DHJn5ogg0xfHQH8lJcMpBxjNZOjFOLBuf0HS9T70U_aI56k5meCVek3N3kGIiN_Gv6I-wxXNxMZnTv3SKMHhmFcCHKtDdGdmQErvPT73TEbk15BzeaxkhZ2ys8PHCiDZD_cjFf2-Da30tx7jaQoP2CUgDGPmYeC37I4pSeMvKNN9_CQIsfnG4N3mSIwKz3XH_rUlaM5ocR_vmnRd3nhrctzq5t9p04w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: ما نماینده کل جهان هستیم، هیچ چیز مثل ایالات متحده نیست
🔹
واقعیت جالب: وقتی دونالد ترامپ از جهان خواست تا به یک ائتلاف دریایی چندملیتی برای باز نگه داشتن تنگه هرمز بپیوندند.
🇬🇧
بریتانیا: رد شد
🇮🇹
ایتالیا: رد شد
🇪🇸
اسپانیا: رد شد
🇯🇵
ژاپن: رد شد
🇫🇷
فرانسه: مردد
🇳🇴
نروژ: رد شد
🇨🇦
کانادا: رد شد
🇦🇺
استرالیا: رد شد
🇩🇪
آلمان: رد شد
🇨🇳
چین: بدون پاسخ
🇳🇱
هلند: بدون پاسخ
🇰🇷
کره جنوبی: بدون تایید
🔹
واقعیت این است که آمریکا در دوران ترامپ به طور فزاینده‌ای منزوی به نظر می‌رسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/681535" target="_blank">📅 23:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681534">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
اعتراض عباس خورشیدوند به خبر بازداشتش
🔹
خورشیدوند با انتشار پستی توسط پسرش به انتشار خبر دروغین بازداشت وی توسط اینترنشنال اعتراض کرد
🔹
روزانه به تعداد افرادی که به انتشار خبر دروغ اینترنشنال اعتراض می‌کنند افزوده می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/681534" target="_blank">📅 23:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681533">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM3dfAoP8rOFr7JFGiclRvL7NYhLVtOa6BeVCeyUjfszGontXXm804VuP1gvf21Ed7heOMjeMGmoW_gBrxSZ-9Y6I7vOYPLVxNgua9bwTFvH4Vcph6t6LV-uENv_Efm8yVEZmkffHbTKrnWrWhbb6sy_vil2kEAjknbWNTfEF0gVXVuEWLvYqNYOG8kI4o8uRB_-OkPjr5Uu4xTZd59qJJP5gSoY8KhPOzDlnnlEVwHuSPVKemDlKTBJjMIJcPOJt_y9v4zMjnmcR6ZG_W-ubRtUHK76O7LhnQ15f53b_c7RunLUNsQcQU-IW5q1d4rhPk7WheIVmtypHCAr8O6W6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ردیابی دو لکه نفتی بزرگ در آب‌های ایران و عمان با ماهواره
🔹
محققان موسسه آب، محیط زیست و سلامت دانشگاه سازمان ملل متحد تصاویر ماهواره‌ای گرفته شده را تجزیه و تحلیل کردند.
🔹
تصاویر ماهواره‌ای نشان می‌دهد که در آب‌های نزدیک جزایر حلانیات عمان، لکه‌ای نفتی با وسعت حدود ۳۰۰ کیلومتر مربع شناسایی شده است.
🔹
همزمان در نزدیکی قشم و هنگام نیز آلودگی نفتی در حدود ۱۰۰ کیلومتر مربع از آب‌های جنوب ایران را نشان می‌دهد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/681533" target="_blank">📅 23:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681528">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyzGLR1mOl4tkCxTT_FFxtvPwhlfS7r1KHFsXwAVzvLoc42k3qik8oSSHb297mHQCzq2XV5X7eo1A-IDTktIRRBuAHKfc9UMHlHn9W0McQB-_a-BotjQOJh8TfJlDjDQpm1avcLaf8YX37w4y36ZTXNcJx0cpXlquRdeAfhOhOM8lGrMpfsQHhInAfabpxJnX16JuoX0cEXmtOww4v8kJushxo9H2AJFl7om_eRYRCXLDcJDXfnKelD8sbEeL10KL39ezDACklCN-nwUFdfPsmLePcjwDVVa9Bjs2hSENd4rgiI9SlNNICf9-ICOM5Jr9MoHf0tDDBej727PqeZLEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZO74JXJNSdlZfhctcmDFCwFagZ-qZgk4qDxgOh-_52UcllW-w9upvRXop7S0B493CkxDghpAy5OrSZKEwW0c62cMkYrvR6ktU3Om0Jpyl7uOC6nnGZ6FaWsYVq8yom5heq3bMPnlz5voILUs_QGbvcOF87y0SZmXElswGdAFB0KkbFyZTlthbOtRvFckMEo4bVAmKY_QSY3vM6zxo0aA86SEoOvnU6MxH3c1ultrnqeF4a9N9Oa19memi0kASiNgiSJsCZvGKPVXTksS3JJsz0WBdRwmjitR0mn1fwFmmtiqvrM2IKQuyKPJJUMlZ5Le23PMJJLslSHz5jh0oxENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHIfxbtA0gnLQLsXOZw5CUA0FBYKyxTNpJ0UWH5y93v29Bnkkzj2LLvmZFZ_yrbQkSM_tNKO6H_dKTO0byqQfoLvuCXPBNwj6a7i2ly1V7JL1Ab-46C8UoEgDijyIzi8wXVMP14tIdumQgLk9_4k7vdNutfvvfDQCGpS36ud9mwJlfRQIiUsJNidArRk5-i8RXnwM54vL8Qg-60jcibB6DfLPlW5-CvSNzGwR6sMe6Clga51gLod-jGwZ0Ya1ji27Uza6yRKjVA1B0l55WNQKmK42bsO4n73z0bLAnTG_AqNKKvoL1FHuOkDKgOiIbn0CSMFb4Fd3zZgbg65AKAAMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FzDTvWmvs6XZw2YjTa8t1vCzzTreFzJt0n0U-kExA-x2p9Q2r4W7jggFDO6GOj6kP-buaeVJ8OyTv7Uqq9XNklpeaTb0Z9Rx4KrmRIVszSlzidCmDE_RwR0CXILe429daZ_Z62OUeOp1U8wOFnZSjTH8dbVtBm7W-Lmi03QiNBiJgd4L2K2j3XqyoHHIqXRBQaTKBnFpuRq0uOEo3ylyZBT4lWY8z9URgdCepmZJxUqRvQ9CwbMRAy2-xaYhPyRFsRHOsa1Qo-1EX8UPSgaqs1z5INq3M4X9xQb3Qbk_X1Ae3knbHJJ2NM3nt8KRhHOR_rpC4BDQpmPyVupWbA0rBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵۰ ماده غذایی که با فریز کردن، عمر دوباره می‌گیرند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/681528" target="_blank">📅 22:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681527">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e9baec4ba.mp4?token=WgcehSSo76coRMKbUvY7vwYfzNaE4QoWTOXBYuv4Ebv7a4Z9aRpI7GOXmAh5Af5dd3R_Z-7tVPGhLTY6Vxex3aGgn1CbMPyvaJch8InDEeEPCQPKpQkX3YqzrSRtzTAyGWEzN8vgitwZQkMgQZNd_88mG7TXbO2DY7WdTS3BXayjT4QaUswCMb3YXfBF6QA-hJ4rBQrDz92DJLJcK4WVCkApPCu6tLBEAICla9oYMYU2zxIgm5UrnBbEvmHvOhS_OXquw_SvZHtut3eynsMClbqUpTEbkQKQg0VTlHlCctsFg65DfcJiVONtxlyIzRF24JGKGgwIEMnOP1brHGlVIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e9baec4ba.mp4?token=WgcehSSo76coRMKbUvY7vwYfzNaE4QoWTOXBYuv4Ebv7a4Z9aRpI7GOXmAh5Af5dd3R_Z-7tVPGhLTY6Vxex3aGgn1CbMPyvaJch8InDEeEPCQPKpQkX3YqzrSRtzTAyGWEzN8vgitwZQkMgQZNd_88mG7TXbO2DY7WdTS3BXayjT4QaUswCMb3YXfBF6QA-hJ4rBQrDz92DJLJcK4WVCkApPCu6tLBEAICla9oYMYU2zxIgm5UrnBbEvmHvOhS_OXquw_SvZHtut3eynsMClbqUpTEbkQKQg0VTlHlCctsFg65DfcJiVONtxlyIzRF24JGKGgwIEMnOP1brHGlVIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طرح اول پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
🔹
در این روش قیمت بنزین تغییر نمی‌کند اما بنزین تا میزان تولید ۱۲۱ میلیون لیتری در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/681527" target="_blank">📅 22:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681526">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
جنگ ایران برای این غول‌ها پول‌ساز شد
🔹
برخی بازیگران اقتصادی از جنگ ایران سودهای چشمگیری به جیب زدند. فاصله قیمت بنزین و گازوئیل با نفت خام، باعث شد بسیاری از پالایشگاه‌های آمریکا در فصل دوم ۲۰۲۶ یکی از سودآورترین دوره‌های تاریخ خود را تجربه کنند.
🔹
همچنین درآمد تریدینگ بانک‌هایی مانند جی‌پی‌مورگان، مورگان استنلی، گلدمن ساکس، سیتی‌گروپ و بانک آمریکا را در سه‌ ماهه دوم ۲۰۲۶ نسبت به سال قبل ۷۱ درصد افزایش داد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/681526" target="_blank">📅 22:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681524">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b9fc2e1d62.mp4?token=k-7a5_UPreR_-ORzV-bGaLEDpC7hj7ZfYz5ozV4-2rVMB8BtEiiZURTDwwPDVDQpnmVX_SNf7wGhnuuGWr1TGAYy7NgqeFowMgxQ602eUOgMUj33oYFtpWxlBkOiU5c_DVVg_cpdOEevZNm_Lt6XA_EkHw2Mg0FgeTKVABC2al0Ht5PHi1LrJxSWo_d6LpuXUyZgXWMx-73iSsStDLvzLkCoxxetMLfpcq7daGHV4xa3QcUfa651Tmbdkicx0n0cma9WzBddCqG4sx2xGMZhmjXSpfn4D_lIwuUTxrkUOv7De3ePmRKjygoEfynTFgKw-ztqwLcgXG-sdoq50a7Wtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b9fc2e1d62.mp4?token=k-7a5_UPreR_-ORzV-bGaLEDpC7hj7ZfYz5ozV4-2rVMB8BtEiiZURTDwwPDVDQpnmVX_SNf7wGhnuuGWr1TGAYy7NgqeFowMgxQ602eUOgMUj33oYFtpWxlBkOiU5c_DVVg_cpdOEevZNm_Lt6XA_EkHw2Mg0FgeTKVABC2al0Ht5PHi1LrJxSWo_d6LpuXUyZgXWMx-73iSsStDLvzLkCoxxetMLfpcq7daGHV4xa3QcUfa651Tmbdkicx0n0cma9WzBddCqG4sx2xGMZhmjXSpfn4D_lIwuUTxrkUOv7De3ePmRKjygoEfynTFgKw-ztqwLcgXG-sdoq50a7Wtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل‌پیش‌بینی‌ترین شیء در علم فیزیک، درست از همان لحظه‌ای که یک مفصل دوم به آن اضافه می‌کنید، به‌طور کامل غیرقابل‌پیش‌بینی می‌شود.
به آن «آونگ دوگانه» (یا پاندول دوگانه) می‌گویند.
به همین دلیل است که دانشمندان هنوز نمی‌توانند رفتار آونگ دوگانه را دقیقاً پیش‌بینی کنند.
آونگ دوگانه‌ای که شرایط اولیه آن حتی تا یک‌تریلیونُمِ درجه اندازه‌گیری شده باشد، باز هم ظرف مدت ده ثانیه کاملاً غیرقابل‌پیش‌بینی خواهد شد.
کمی درباره معنای واقعی این جمله فکر کنید.
ما معادلات کامل آن را در اختیار داریم.
نیوتون آن‌ها را نوشت.
لاگرانژ آن‌ها را به‌روز و دقیق‌تر کرد.
هر دانشجوی کارشناسی فیزیک می‌تواند آن‌ها را روی یک دستمال‌سفره اثبات و استخراج کند.
هیچ بخش ناگفته یا گمشده‌ای در فیزیکِ آن وجود ندارد، هیچ متغیر پنهانی در کار نیست، و هیچ عجیب‌وغریبیِ کوانتومی هم مطرح نیست.
فقط دو میله، دو مفصل، و گرانش. همین و بس.
و با این حال، این سیستم پیش‌بینی را به تمسخر می‌گیرد.
دلیل این اتفاق در چیزی به نام «نمای لیاپونوف» نهفته است؛ عددی که سرعت واگرایی و فاصله گرفتنِ دو موقعیت شروعِ تقریباً یکسان را در طول زمان اندازه‌گیری می‌کند.
برای یک آونگ دوگانه، این نما در حدود ۳ تا ۵ در ثانیه است و در برخی آزمایش‌ها حتی به ۷٫۹ هم می‌رسد.
به زبان ساده: «هرگونه عدم‌قطعیت ناچیز در زاویه اولیه شما، تقریباً هر یک‌پنجمِ ثانیه دو برابر می‌شود.
پس از یک ثانیه، خطای شما هزاران برابر شده است. پس از پنج ثانیه، میلیاردها برابر؛ و پس از ده ثانیه، دو آونگ هیچ وجه مشترکی جز قوانینی که از آن پیروی می‌کنند، نخواهند داشت.»
دامِ عمیق‌تر، ماهیتی فلسفی دارد.
مکانیک کلاسیک قرار بود معبد «جبرگرایی» (Determinism) باشد.
لاپلاس به زیبایی مدعی شده بود که یک هوش به اندازه کافی قدرتمند که موقعیت و سرعت تمام ذرات را بداند، می‌تواند کل آینده جهان را پیش‌بینی کند.
آونگ دوگانه تنها با استفاده از دو چوب و یک لولا، این رؤیا را بی‌صدا نابود می‌کند.
جبرگرایی در تئوری برقرار است، اما پیش‌بینی‌پذیری شکست می‌خورد، چرا که اندازه‌گیری‌ها هرگز دقیقِ مطلق نیستند.
شما نمی‌توانید یک زاویه را تا بی‌نهایت رقم اعشار بدانید؛ جهان این ارقام را در اختیار شما قرار نمی‌دهد.
بنابراین، حتی در یک سیستم کاملاً جبرگرا، درست از لحظه‌ای که حساسیت به شرایط اولیه از دقتِ اندازه‌گیری شما پیشی می‌گیرد، آینده عملاً غیرقابل‌شناخت می‌شود.
به همین دلیل است که پیش‌بینی‌های هواشناسی برای بیش از دو هفته با شکست مواجه می‌شوند؛ به همین دلیل است که آریتمی‌های قلبی در برابر پیش‌بینی مقاومت می‌کنند؛ و به همین دلیل است که مدل‌های مالیِ بناشده بر منحنی‌های هموار، توسط واقعیت تکه‌تکه می‌شوند.
آونگ دوگانه، چهره صادقانه بیشتر سیستم‌های پیچیده در طبیعت است.
پیش‌بینی‌پذیریِ هموار، یک استثناست.
آشوب (Chaos)، تنظیمات پیش‌فرضِ هر چیزی است که از اجزای غیرخطیِ کوپل‌شده (به‌هم‌پیوسته) تشکیل شده باشد.</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/681524" target="_blank">📅 22:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681522">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تبعات گرانی تعمیرات؛ تعداد زیادی از خودروهای در حال تردد معیوب‌اند
علیرضا نیک‌آیین، رئیس اتحادیه تعمیرکاران خودرو در
#گفتگو
با خبرفوری:
🔹
افزایش هزینه تعمیرات خودرو، بسیاری از مالکان را به تعویق انداختن تعمیر واداشته است؛ به‌طوری که تنها در صورت بروز خرابی جدی به تعمیرگاه مراجعه می‌کنند. شمار قابل‌توجهی از خودروهای در حال تردد از نظر فنی معیوب هستند که علاوه بر افزایش خطرات ایمنی، با نزدیک شدن به فصل سرما می‌تواند آلودگی هوا را نیز تشدید کند.
🔹
بخش عمده این گرانی ناشی از افزایش قیمت قطعات است و اجرت تعمیرکاران تنها حدود ۱۰ تا ۱۵ درصد هزینه تعمیر را تشکیل می‌دهد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/681522" target="_blank">📅 22:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681521">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4U1wSR1ICLHUr81sLz_W578kkjd6XEARbSGrmxA2em6sPXZpQY0He603KGI1k3Q6fvtFDT6ct2mnm7DrEata7xLAvkRiM3WNNeJSyVAbNiVD_TJs00zxWi2swNDSgvA_j-4LEYEls9JBs-2YR9Mc1JoSuTbiffhiBL2OL9JjGQfuCy42DG0njGudSd9CptGeCQAhq7yihoW4c4o-UEVxQsI6nSrXwdjG2oYuGBrWeFORF3AlP6SvaHmJe9C1UScLt3FFmD_dECvH_Z3v7oLyUJVGsiipJivLtTrZ6aAmZESVE-7YVLe-29R_xCJqdbb1mD8l3DP-CEjCVOIH2N57w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا در جنگ شناختی از کجا تغذیه می‌کند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/681521" target="_blank">📅 22:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681520">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
سردار باقرزاده: ۳ خلبان ایرانی توسط قطر به اسارت درآمده‌اند  فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح:
🔹
۳ خلبان ایرانی پس از سقوط جنگنده‌های سوخو-۲۴ در جریان حملات اسفندماه، زنده توسط نیروهای قطری اسیر شده‌اند.
🔹
«جواد صالحی»، «عبدالمجید دشتیان»…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/681520" target="_blank">📅 22:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681518">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18db338ef0.mp4?token=gUYdNvnJdKvModOEwFqUbwO6WRZkqHM3RgFGJw-mgRSuEnkD_g8qbsx5YTNMhq8Kok5nx0IulLqtjDBJSwh7gWuWBt0G8rSUkHNmooITXVogWJNBLMoA33YtXyYV_wdLrwghKaBbwR6DvZ9mVElAevtNhbf4LlZq5QRhfnBs-HTP6ycFj8rXXDyA03SXf-c7OgjaMu-_D1FGmbwC6ReZSxLhtefROGYA3Rxm6tX1VqzFVhBOk9f0Rola5gGpyFQqgKO3LL5Dj35Uvk12-7tQK9r0iKNQNl4BS4SfT27at6D0WKn94x7wSop92VWT-qMdlEpHSzsdOgZ0Nt-oJ09JZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18db338ef0.mp4?token=gUYdNvnJdKvModOEwFqUbwO6WRZkqHM3RgFGJw-mgRSuEnkD_g8qbsx5YTNMhq8Kok5nx0IulLqtjDBJSwh7gWuWBt0G8rSUkHNmooITXVogWJNBLMoA33YtXyYV_wdLrwghKaBbwR6DvZ9mVElAevtNhbf4LlZq5QRhfnBs-HTP6ycFj8rXXDyA03SXf-c7OgjaMu-_D1FGmbwC6ReZSxLhtefROGYA3Rxm6tX1VqzFVhBOk9f0Rola5gGpyFQqgKO3LL5Dj35Uvk12-7tQK9r0iKNQNl4BS4SfT27at6D0WKn94x7wSop92VWT-qMdlEpHSzsdOgZ0Nt-oJ09JZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا بعضی میوه‌های خشک مثل نمونه‌های بازار نمی‌شوند؟
🔹
یکی از چالش‌های تولیدکنندگان تازه‌کار میوه خشک، رسیدن به محصولی با رنگ، طعم و کیفیت مناسب است. برای داشتن یک خروجی خوب، چند عامل مهم تأثیرگذارند:
🔹
انتخاب میوه تازه و باکیفیت
🔹
دقت در فرآیند شست‌وشو و…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/681518" target="_blank">📅 22:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681517">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
تنگه هرمز یا برنامه هسته ای؛ آمریکا از کدام سلاح ایران بیشتر می ترسد؟
🔹
ایران از طریق مساله هسته ای بیشتر می تواند از غرب امتیاز بگیرد و قدرت منطقه ای خود را بیشتر کند یا مساله هسته ای؟ کدام یک از این دو می توانند عنصر اصلی بازدارندگی در استراتژی جنگ نامتقارن ایران و آمریکا باشند؟
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3237925</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/681517" target="_blank">📅 22:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681512">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
یک پسر ۱۱ ساله پس‌انداز ۲ هزار دلاری خانواده‌اش را خرج بازی کرد
!
🔹
یک خانواده در کانادا پس از ناپدیدشدن پس‌اندازشان متوجه شدند پسر ۱۱ ساله‌شان بدون اطلاع آنها، بخشی از پول را برداشته و ۲ هزار دلار آن را صرف خرید گیفت‌کارت برای بازی کرده است.
🔹
این کودک هنگام رفتن به خانۀ مادربزرگش، پاکت پول نقد خانواده را با خود برده و در دو خرید جداگانه، هر بار هزار دلار هزینه کرده بود.
🔹
خانواده برای بازگرداندن پول اقدام کردند، اما با توجه به نهایی‌شدن خرید، موفق به پس‌گرفتن وجه نشدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/681512" target="_blank">📅 22:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681511">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WE0IlQGeeN5WUneEa-JqTsfzQw80D1sn9iwoG5zvDyx2ollkf-I7BvtVfYnlZvh2bgLXI7REKuRzBVgFKr45y8mIBWlqfs8KU8SzQHsR9BAbyhPXbSZUE38yy_NZ9aIPaSGoIc2Yp_iMlybKnF9H9a_PfX_leoeKDuO9rBTTk7gMVMfefXU2tEpL2U8a9EvR2Iid60taayEwxzpp_DkeOHqZFbwjBnTzJW4naRhhK0l7pGsH8BCYDbEI70_qfCn19wuMb5xFkqsNyJmDmVeGUOW_-glC3eFi8AlFdlOi-s2nNwdljC2g3WCdpc4HB7O8simqmxUDd5EE96rQ8SsKog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر حرفی ارزش گفتن ندارد؛ گاهی سکوت عاقلانه‌تر است
🔹
امام علی(ع) در نهج‌البلاغه هشدار می‌دهد که زیاد سخن گفتن، احتمال خطا و پشیمانی را بیشتر می‌کند. ارزش کلام به تعداد جمله‌ها نیست؛ به سنجیده‌بودن آن‌هاست. گاهی یک جمله به‌جا می‌تواند احترام بسازد و یک حرف…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/681511" target="_blank">📅 22:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681510">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/916213bf74.mp4?token=MnVisPy1dXMJeIvuG6bLlfnutR2Cqt9wyUuBYp-im_Cas8kzAbH3KaR4iKFH-8r8KdtQ2gm2JjpPHynWns355Ay2csv3idf1CArvfVRyHE0Q5bM2kzlv5DBIvlfyw1qRpkHrMzu8OXKQ1TyHRgLLqdtUQONnMmgOq73iYuXFeluA_L0A27gCAIXzy67G_mZ3HxLmqsF39RyGY1dJNE5okmUoP6FKtWf6zOXYD8ampx1z-ghxRCRMUeLz1qxMcNZIebYUBKuzUTgdxkAkkAc3REIOYVD5tve_noiplGCI1RiSKOkgdPHCrSLXBEbYjWnYk1gaobXmhfuvkuOdMvf_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/916213bf74.mp4?token=MnVisPy1dXMJeIvuG6bLlfnutR2Cqt9wyUuBYp-im_Cas8kzAbH3KaR4iKFH-8r8KdtQ2gm2JjpPHynWns355Ay2csv3idf1CArvfVRyHE0Q5bM2kzlv5DBIvlfyw1qRpkHrMzu8OXKQ1TyHRgLLqdtUQONnMmgOq73iYuXFeluA_L0A27gCAIXzy67G_mZ3HxLmqsF39RyGY1dJNE5okmUoP6FKtWf6zOXYD8ampx1z-ghxRCRMUeLz1qxMcNZIebYUBKuzUTgdxkAkkAc3REIOYVD5tve_noiplGCI1RiSKOkgdPHCrSLXBEbYjWnYk1gaobXmhfuvkuOdMvf_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی نگاه از مرزِ دیدن عبور می‌کند؛ خلاقیت متولد می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/681510" target="_blank">📅 21:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681508">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf7fe58a0.mp4?token=u9OXgU3tE7sRhGYRZ6xlzTMbpPsp7YKelp3Nsrdb0dsEjAHl9mJJvxTUOmwwp7w59QcPHaSkrG7Ot-gEwCdk7UTJ604Ba5vYt7s1ydOOvp47VQfRBrcuuuYbexNjmhwr8PQMkc8dZvphvaSAhjMMbp1BK5Ein6hjd4DBdp6xSdPyNyYhIQwY2NhgmoUMEBMBxEZpdu-S9qQtSLboBRqCgYflTSIaTYPZp2eXZcPuNhyXilidftV1Yd4tLFpwo6WngFWMVl-85-Je55Rp_MpcOt3CKyG4u4r9DYDkmb_edfwV_o1h-2fzZS2yJ6DUA-BUXEWbz9hhuHJfb5iMLdPr3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf7fe58a0.mp4?token=u9OXgU3tE7sRhGYRZ6xlzTMbpPsp7YKelp3Nsrdb0dsEjAHl9mJJvxTUOmwwp7w59QcPHaSkrG7Ot-gEwCdk7UTJ604Ba5vYt7s1ydOOvp47VQfRBrcuuuYbexNjmhwr8PQMkc8dZvphvaSAhjMMbp1BK5Ein6hjd4DBdp6xSdPyNyYhIQwY2NhgmoUMEBMBxEZpdu-S9qQtSLboBRqCgYflTSIaTYPZp2eXZcPuNhyXilidftV1Yd4tLFpwo6WngFWMVl-85-Je55Rp_MpcOt3CKyG4u4r9DYDkmb_edfwV_o1h-2fzZS2yJ6DUA-BUXEWbz9hhuHJfb5iMLdPr3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ‌وقت نمی‌توان مستقیم پول به کشور وارد کرد، تراستی‌ها به خاطر تحریم جریان ارزی ایران را مدیریت می‌کنند
!/ تلویزیون اینترنتی مدار
گفتگوی کامل را اینجا ببینید
👇
https://youtu.be/BNd_H49d3ic
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/681508" target="_blank">📅 21:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681507">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hC2OBL3hkZWUX_jJBYEVmFGSPq72hugLczuPc2q_knYKC90Crje2iakG-2hLgp2RlktXPjxpjrWlEltkPL89dWF8cqsPtDwL98VMPiREtwYKzvxiRrJVISF66hZN-Va2hU5UzGVM1RNo73f51NtUzCaiWtajUeM0mXkEtQ5DbZsbR1Gq9uAhNUgFLYsxR9aMupzbtvAsqJYE8rRkJaoAx5e8EvtPxcur-wMS_fA17WmnnmGaC7R2FInair1PPLyW0Cak0cRq-YSwwahnNHLEA13M6hEWaYn0ixll04tMeNS7CjlNRYZ4kNJypS3eQ0hmeQBVpcu7Lm1c-2RK7IiUHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت شاخص توسعه انسانی در جهان
🔹
شاخص توسعه انسانی بر اساس ارزیابی سه معیار اصلی «زندگی طولانی و سالم»، «آموزش» و «رفاه اقتصادی» محاسبه می‌شود.
🔹
ایسلند با امتیاز ۰.۹۷ در رتبه اول شاخص توسعه انسانی قرار دارد و کشورهایی نظیر آلمان، بریتانیا و امارات نیز در رتبه‌های برتر جای گرفته‌اند.
🔹
ایران با امتیاز ۰.۸۰ و کسب رتبه ۷۵ جهان، بالاتر از میانگین جهانی ۰.۷۶ قرار دارد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/681507" target="_blank">📅 21:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681505">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aa0fd153b.mp4?token=j2O5sZz3fccw_Di4fYmyhUPjnAHfhYy6tmxokLsiYvPHWw17o-qBASN679WeTVix39nS-TKCiMzzEINNMA6lHwIpro_qCn5g1Kv2GP73qnxxU9dP3yMfAWFaOBFYzWZEyAddtZnL65qYRcApC_4mCKVqJFiN7j3KSsNIu0MvTVDKbdICp3OM1MVRaYwO2B7b1br_oIBSS2Mu9WxAY6H9vDxjOt9vPPwB-ZB-jJ77W_6ALBlbo0SqqxHWvLBTIfg0MA6_whO0J_C3VFbZeTdspZe13k9-A2DzKuPsrJu3E5rm-nZ5Im6WCQtBTsT2-WXmyUvcfOknRwdtffzucDc0mzP6PsIeX6ZTdBvTAQNRnVdta1RXSRKxgrUhYT1wpV7KLuKHILw7nAoZJpOy3rKXBXNGETTM0SuS0jV8dt8KWn7LU2ZIE_AG-dGdq_pOp2wmoPekoHIsHeQmbjMnGFJx5Bo8kEx3aHbHIBfpRyEmarGxoSzqYzw3S6wjy55-W-XtUTYSTZjRvShbFXHSt3YM0xhKXVD7tmWi1iMkt_40Dpc-Z78rtQU0EE8h2_sstL1DJK5_Dlm8O8_9wQlZl_C7dTixbiKTK-UeembuqdX9y-Q9h42mRliqw1Ro82rPFiYK6YCKPFJ3buWywOslEKbIR3-7_c_Px9ZMHEn1OZD0Ynw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aa0fd153b.mp4?token=j2O5sZz3fccw_Di4fYmyhUPjnAHfhYy6tmxokLsiYvPHWw17o-qBASN679WeTVix39nS-TKCiMzzEINNMA6lHwIpro_qCn5g1Kv2GP73qnxxU9dP3yMfAWFaOBFYzWZEyAddtZnL65qYRcApC_4mCKVqJFiN7j3KSsNIu0MvTVDKbdICp3OM1MVRaYwO2B7b1br_oIBSS2Mu9WxAY6H9vDxjOt9vPPwB-ZB-jJ77W_6ALBlbo0SqqxHWvLBTIfg0MA6_whO0J_C3VFbZeTdspZe13k9-A2DzKuPsrJu3E5rm-nZ5Im6WCQtBTsT2-WXmyUvcfOknRwdtffzucDc0mzP6PsIeX6ZTdBvTAQNRnVdta1RXSRKxgrUhYT1wpV7KLuKHILw7nAoZJpOy3rKXBXNGETTM0SuS0jV8dt8KWn7LU2ZIE_AG-dGdq_pOp2wmoPekoHIsHeQmbjMnGFJx5Bo8kEx3aHbHIBfpRyEmarGxoSzqYzw3S6wjy55-W-XtUTYSTZjRvShbFXHSt3YM0xhKXVD7tmWi1iMkt_40Dpc-Z78rtQU0EE8h2_sstL1DJK5_Dlm8O8_9wQlZl_C7dTixbiKTK-UeembuqdX9y-Q9h42mRliqw1Ro82rPFiYK6YCKPFJ3buWywOslEKbIR3-7_c_Px9ZMHEn1OZD0Ynw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باز کردن یک بسته اورژانسی قایق نجات تاریخ ۱۹۴۴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/681505" target="_blank">📅 21:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681503">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
تایمز اسرائیل: آخرین ناو آمریکا از اقیانوس آرام خارج و به سمت خاورمیانه رفت
ادعای تایمز اسرائیل:
🔹
جنگ طولانی‌مدت ترامپ علیه ایران، خروج آخرین ناو هواپیمابر آمریکا از اقیانوس آرام را اجباری کرده و منطقه را موقتاً بی‌دفاع گذاشته است. چین از این حواس‌پرتی برای تقویت نفوذ منطقه‌ای خود بهره‌برداری می‌کند.
🔹
تحلیلگران هشدار می‌دهند که برنامه‌ریزی ضعیف و استقرارهای طولانی، خدمه را خسته و منابع دریایی را محدود کرده است و نشان‌دهنده تغییر استراتژیک از آسیا به سمت خاورمیانه و نیمکره غربی است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/681503" target="_blank">📅 21:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681500">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423009927c.mp4?token=KaAxe_kuukLHzhDoMbsJDHiQRuOzpvr-GfygFEnFxuTXQ7C_qitwgqadl7aD7no6My02tlq_dkR9_N9tk-3sIljBwXVFjLKNCdNC9B_Em8u3fjuZcstXb80YoFDjaURPukfaD_LsreaGFkFVMAa54wg1fSvGzuGcJSpiMTcJwDcJGYPUbXnTijyr4HAxJYwX3WobqHlbEjKq1GbZECu2RDboaZ1vemCwnOfLBEIvSR-vctlPY6-ZZC6Am5i13cl49c8ONRMc-PFuYfq_yYz-Xfr6zlvqkJZBJSG2-bAETuh68Tcq8r8HuVPhY9ntdZ3eCVNNv4r5KpH3ep3YSnaKpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423009927c.mp4?token=KaAxe_kuukLHzhDoMbsJDHiQRuOzpvr-GfygFEnFxuTXQ7C_qitwgqadl7aD7no6My02tlq_dkR9_N9tk-3sIljBwXVFjLKNCdNC9B_Em8u3fjuZcstXb80YoFDjaURPukfaD_LsreaGFkFVMAa54wg1fSvGzuGcJSpiMTcJwDcJGYPUbXnTijyr4HAxJYwX3WobqHlbEjKq1GbZECu2RDboaZ1vemCwnOfLBEIvSR-vctlPY6-ZZC6Am5i13cl49c8ONRMc-PFuYfq_yYz-Xfr6zlvqkJZBJSG2-bAETuh68Tcq8r8HuVPhY9ntdZ3eCVNNv4r5KpH3ep3YSnaKpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقابله نیروهای امنیتی مراکش با هجوم مهاجران غیرقانونی به سئوتا
🔹
موج جدیدی از مهاجرت غیرقانونی در مرز منطقه تحت حاکمیت اسپانیا، سئوتا، ثبت شده است؛ جایی که گروه‌هایی از مهاجران از جنگل‌های اطراف تلاش کردند وارد آن شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/681500" target="_blank">📅 21:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681497">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYm28UWFG0maBgCPU2eEkRZoC_Mv1tVJ5qsPdaidR-4T5OXLR4zSfkACsuGnsgKDG6hesLFX_ah3jBJG2BeEUtz6D-iQVLG3hSHA8AJ6gyR8Kl1F9SqXRJjXlTn5lB9j4DjMa-SPAYPf4GFA87W075fD1rwZtkEP83LefGn4vykfC4LX4WZRwSqqePy0b5_MXG_uEVFxZXl5fq7CYioEd4zF58wkqPa5NsLoNnCGL3Ds-Ka5oVGffuKP4WCgwCtEJsWZ5KCstcWgb5Bw9tX7mtTQb_gOtpBPnNBDcsatioeukdbb3ggCjfjBpNzIZIusjuizXKJdVx9Yn4SX9lmTVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نگران تمدید بیمه نباش؛ ۱۱ ماهه پرداخت کن!
با امکان
پرداخت ۱۱ ماهه
، می‌تونی هزینه بیمه رو راحت‌تر مدیریت کنی و همچنان از
پوشش کامل
بهره‌مند بشی.
این طوری :
بیمه‌ت به‌موقع تمدید می‌شه
هزینه‌هات بهتر مدیریت می‌شه
نیازی به چک و ‌ضامن نداری
✅
بیمه‌بازار
کنار شماست تا بیمه‌تون رو متناسب با نیازتون و به‌صورت
قسطی
تهیه کنید.
👈
تمدید قسطی بیمه
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/681497" target="_blank">📅 21:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681496">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7w4Lki2DH0IMlz_n4WxxFZXfeAPatg8I4pb7YOGFaujJs26SDEChzm8VcCgtfC-HPXtj_7Eiq1wlcde8p-qa4rueUiQrfbcLCzZwHwgf8pdKjoFiHnQXFXMoW7X8dzgnf6HwNzZB2__CbbDlmZ5laQ2WK87xx3sR6qhvNUTK6dztg3SM6QWJS4l_s3vVamQcHl04ZMFImdEw0ZCuvKjZUp4uKALr8DuF2QRpDyrS-CKpEJOd-EdCYOoF9aC0ImNH-lrKL0s1xoHZqPwI9vS8PvwCSRxqCXfz4BflehpB5mGZgXAVai_UZtdZSRqeZfJFu-_5psXC954bTHhqus7SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد رسول‌الله (ص)
🔹
کارگردان: مجید مجیدی
🔹
ژانر: تاریخی، مذهبی، درام
🔹
بازیگران: مهدی پاکدل، علیرضا شجاع‌نوری، محسن تنابنده، ساره بیات، مینا ساداتی، رعنا آزادی‌ور و…
🔹
خلاصه داستان: داستان از سال‌های کودکی پیامبر اسلام (ص) آغاز می‌شود؛ دورانی پرآشوب که مکه…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/681496" target="_blank">📅 21:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681489">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
وزارت علوم: امتحانات ترم تابستانی حضوری است، اما در محل سکونت
سرپرست دفتر برنامه‌ریزی آموزش عالی:
🔹
امتحانات مربوط به دروس ارائه شده در بازه تابستان بایستی به صورت حضوری برگزار شود و برگزاری امتحانات به صورت مجازی ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/681489" target="_blank">📅 20:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681487">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgKtx4I2zb8jMNHlmDaUURRnQYxvDtNUV-G9dm6iIn6nulXaYz5cRHg1L-kP9Cl7kl8wC5szvMhYNy4_1ac0r9_z91CJbf6WTTqIYnUZ2YTAo5ch_2i6LsYVSivx87fzn4DOYKus1ZPhDNMVbSyzD9OVruR3uIndotdEpxPX4kPm2gpAg0XVP0diQ0tJM4wXJv9Q6aSL1yTEKWPg-Atnu7OMoPkT97FAhl29CWA3-9yDHLMzC1jR3xMWM_3uhg4Tyi4dF47xdMmQLuVh1_NjqDdFjDt6CJWDpLZyjHbZQH67eM5wnuTK-isj8zJErozMOEzxqYMf4KKTJ2BDpBRcDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای مضحک رسانه اوکراینی: ایران از زلنسکی می‌ترسد
ادعای کیف‌پست:
🔹
حاکمان ایران، زلنسکی را «دلقک» و عروسک خیمه‌شب‌بازی غرب می‌نامند اما شدت واکنش آنها چیز دیگری را نشان می‌دهد.
🔹
راهبردی که بر ادغام تولید اوکراین، فناوری اسرائیل، توان آمریکا و سرمایه کشورهای خلیج فارس استوار است و می‌تواند هزینه دفاع از متحدان آمریکا را کاهش دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/681487" target="_blank">📅 20:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681486">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
روزانه ۱۵۰۰ دلار درآمد ارزی ایران در مرز افغانستان از بین می‌رود
رسول نصیری، رئیس انجمن صنفی کامیون‌داران تایباد در
#گفتگو
با خبرفوری:
🔹
با وجود اعلام حذف عوارض متقابل، کامیون‌های ایرانی برای تردد به افغانستان همچنان باید ۳۰ تا ۴۰ میلیون تومان هزینه پرداخت کنند، در حالی که ناوگان افغانستانی با هزینه بسیار کمتر در ایران فعالیت می‌کند.
🔹
در شرایط فعلی، ناوگان ایرانی در بهترین حالت تنها دو سرویس در سه ماه انجام می‌دهد و بخش زیادی از بار در مرزهایی مانند دوغارون و ماهیرود به کامیون‌های افغانستانی واگذار می‌شود. گسترش ترانشیپ در مرزها نیز باعث شده روزانه حدود ۱۰۰۰ تا ۱۵۰۰ دلار از درآمد ارزی ناوگان ایرانی از بین برود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/681486" target="_blank">📅 20:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681485">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
وقتی شیطان در لحظه مرگ وسوسه می‌کند؛ روایت عجیب یک تجربه نزدیک به مرگ
🔹
00:08:00 تلاش شیطان برای انکار خداوند هنگام جدایی روح از جسم
🔹
00:38:30 نفرین شدن توسط فرشته‌ها هنگام دروغ گفتن به مادر
🔹
00:52:40 خوردن سه سیلی برای سه دسته از گناهان
🔹
00:56:45 دعا کردن و قول بازگشت به دنیا توسط روح جنین خانم باردار در بیمارستان
🔹
01:07:00 علت نارضایتی انسان‌هایی که در صف‌های طولانی، نان و شیر و خرما می‌گرفتند
🔹
01:10:00 تأکید دختر بچه سه ساله به خواندن نماز
🔹
01:16:10 نمایان شدن خورشیدی بزرگ با بردن نام علی در اذان
🔹
01:18:15 توبه قبل از تصادف در شب سوم محرم
🔹
قسمت سی‌ویکم (این چرخ گردون)، فصل پنجم
🔹
#تجربه‌گر
: سیدهادی سجادی بلالمی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/681485" target="_blank">📅 20:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681484">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2689297ea.mp4?token=qTAnjWUCMrQptz33-smhWmqYzznjQk4WdiaZWpWtUw4Sb_elQXQ-DcP4tFCiy-5BABK9SeTQ8zDroY9RhLHAHmca2S7ZI8Z-h_Vsyc0g73O0ZE2JOtRreNAiX7p-qHQtGAAQqludBBWOaCeeW5QMd6cwfmsVQp87nW1SbXkSWmhV_IHoVbpX9mZhfO4FLdnakIW74O9mMcXBk0WB6JGkySTGo2E27y_kw8B8ZB1eLvxZk1Cvm3BbHLMMvs3Y8pjBNy7_7_Z9P0MluvojO9Oh-GWNbBKsgee7jxbreCoevAMGCzrbGrMK7QEplc9HKKARfWWIq6MtYt2bZaxOvmHbXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2689297ea.mp4?token=qTAnjWUCMrQptz33-smhWmqYzznjQk4WdiaZWpWtUw4Sb_elQXQ-DcP4tFCiy-5BABK9SeTQ8zDroY9RhLHAHmca2S7ZI8Z-h_Vsyc0g73O0ZE2JOtRreNAiX7p-qHQtGAAQqludBBWOaCeeW5QMd6cwfmsVQp87nW1SbXkSWmhV_IHoVbpX9mZhfO4FLdnakIW74O9mMcXBk0WB6JGkySTGo2E27y_kw8B8ZB1eLvxZk1Cvm3BbHLMMvs3Y8pjBNy7_7_Z9P0MluvojO9Oh-GWNbBKsgee7jxbreCoevAMGCzrbGrMK7QEplc9HKKARfWWIq6MtYt2bZaxOvmHbXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با دیدن این ویدئو می‌توان تاثیر پیشرفت علم در سلامتی و کمک به انسان در بقا را درک کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/681484" target="_blank">📅 20:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681483">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gj7mbPkaCpIUYpki-WkcMQx4NByD2dSZL1NjA_GPGz8uTrCaN_Yrzyhc9MeTuXsGFcSAMeUDm1AfjWIVcWj0ii8dVnXwcJm9KqfmNtf_q-2bddR8cNbgXBSY33tGp8IDDiMcU5gXDkVDuWqy8uwR2nGXvPPkiVY1QHu1wV8m63R2JgnJ3TUeFa-Uy9GfajnE3FVz3pLFT9aTBnhpP0VCH_fHjj5DMq-SInlfn2ySNcpqhAmODXdwwCyG1VnRqhOUmTC70NTxi1hcevNCQmZI7Jw93wRvGDm28NepFHpKf-aFUq5TojDbzhMMlmbXNoSkOzVUMzz5-BqP-wrUjYSC1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهم مراکز داده از میزان مصرف برق جهان
🔸
مصرف برق دیتاسنترها در سال ۲۰۲۵ به ۴۸۵ تراوات‌ساعت رسید که معادل ۱.۵ درصد از کل برق جهان است.
🔸
پیش‌بینی می‌شود این میزان در سال ۲۰۳۰ به ۹۴۵ تراوات‌ساعت افزایش یابد و سهمی معدل ۳ درصدی از مصرف برق جهان را به خود اختصاص دهد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/681483" target="_blank">📅 20:28 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
