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
<img src="https://cdn4.telesco.pe/file/NYP6B4bi5hMTRgjG_WkP27OgAloKLtd3j4c83ZjRPNINZq_ufVNy6RWWhTVrLDZ_9nPc-N5oWj-wJRDrj2LZgWQl4igpnDqFfRdWTbtO3w4jvY5CH3jwRWRSDSpDXbqNJzjBGnNWnPeV-2nWNx0Ziyrt5KvaIVsI_OLFqUN85jgcqSjI9BtU-65afWjY2I9MNYKaJb4JmW3x5C3sAyFrZQbcDNJ0Va5RN6G13tUpXpUPCo9_AkJLFhxmco2oyh0JQUdc4HGaSpHOZBvxYwfDBtm-PpE7amdGlghmCuipzVr79enZUEEZmNARgXZ5A-BKkXIVjvl4BewoK_aMQKNsXg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 139K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 01:42:52</div>
<hr>

<div class="tg-post" id="msg-65031">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
آکسیوس: توافق بین دو طرف امضا شد.
👎
این خبر فیکه و آکسیوس و خبرنگاراش همچین خبری نزدن.
@News_Hut</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/news_hut/65031" target="_blank">📅 01:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65030">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=Q3QKam1ZuetRednLenOyo-FZUTE4crRKfv7OiojytJYJcm-Se3mkB_SViWuYJMvs8327YGemYU40C7GYL1zmXZKjO1ru2CU9BbvE2ybI5AxSQnjfEqdnuv0OIlkvCASjKUj4jRfhRrlFXU62zLpqehuVcnnSMD-7fY-OWZPZt0ADrq8oXdhaTHtbXuB1xsONxiaEKI9O5jPs6BHtbh3y5U9s46Ke1CspZoR1Tiad1p3NhpHMQMvaKSr4xN4nJcFW573a_lluWtI1S1kFtZBK1NK6BgDwQnKiwGOCFgKPLf0YKQUf9Zo1JOiD1NiegzpeuKBiL6Chl7H78x0ZxrrZOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=Q3QKam1ZuetRednLenOyo-FZUTE4crRKfv7OiojytJYJcm-Se3mkB_SViWuYJMvs8327YGemYU40C7GYL1zmXZKjO1ru2CU9BbvE2ybI5AxSQnjfEqdnuv0OIlkvCASjKUj4jRfhRrlFXU62zLpqehuVcnnSMD-7fY-OWZPZt0ADrq8oXdhaTHtbXuB1xsONxiaEKI9O5jPs6BHtbh3y5U9s46Ke1CspZoR1Tiad1p3NhpHMQMvaKSr4xN4nJcFW573a_lluWtI1S1kFtZBK1NK6BgDwQnKiwGOCFgKPLf0YKQUf9Zo1JOiD1NiegzpeuKBiL6Chl7H78x0ZxrrZOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/news_hut/65030" target="_blank">📅 00:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65029">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=H7gkaVAQCe8OZ8dUrmii9WI0Eo37up1O-8r3aPwToZ3SgpJRM0uztSexo5S1QCZB3Q_l98yTuOVE9FXmoHITIXAemEKHvZ-_VryMTWV13_P5FDG4mQD0o8z5sUY5tt6cyLyRe--u-vX3X-RcO6NUyltJcmt59HDXppIsYyue-r2EnYZURu8Zqbnh6kGC-kV3aIRKk8oG2ZIzrtW0cW0ymCSB2o382R8nR83cfbOLsa_GW4YS-VGR896zrzmIjjYbXg4CRjfT4ZuA0f-3W7PA5eETaR_UCy6hnT3BmuKv54pZKprtRfw337gg11Rlj0MKb4MO37TWScABKX1Kws_k2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=H7gkaVAQCe8OZ8dUrmii9WI0Eo37up1O-8r3aPwToZ3SgpJRM0uztSexo5S1QCZB3Q_l98yTuOVE9FXmoHITIXAemEKHvZ-_VryMTWV13_P5FDG4mQD0o8z5sUY5tt6cyLyRe--u-vX3X-RcO6NUyltJcmt59HDXppIsYyue-r2EnYZURu8Zqbnh6kGC-kV3aIRKk8oG2ZIzrtW0cW0ymCSB2o382R8nR83cfbOLsa_GW4YS-VGR896zrzmIjjYbXg4CRjfT4ZuA0f-3W7PA5eETaR_UCy6hnT3BmuKv54pZKprtRfw337gg11Rlj0MKb4MO37TWScABKX1Kws_k2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/news_hut/65029" target="_blank">📅 00:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65028">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/news_hut/65028" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65027">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l2TzFSGKSAvzIWbb8UWmPbzskQ-nypc5ed83BqI8rlUSBNwiKRqchHGiUcauQLT5ic98w6aKR5Fi0VzijKGhXNpI8CCqWHOikKoHv-v1XBjffdktz0MXVW7JnrCXCH4M5ip2BTlHgw2bb7umaQFlxiTDpv0LI8xsnqFDLUs8sTKEXqS4JlB8Tb4RGlejZ5d_ZaJEFdbND_M3vvTpLbuX7EOQ7w2afL8EyyKItrK-kIDkzjifM7me2EBzMyBKObT5oO1ZYmDogEkmLzYBchcGWufFPy-BEYdWJeEcsmCWhhJb20vxaq9sPoEgbBCejUgEQphtxUJWag9cuu_7w4dnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ:
من در اتاق بیضی کاخ سفید هستم، جایی که همین حالا تماس بسیار خوبی با پادشاه محمد بن سلمان آل سعود، عربستان سعودی، محمد بن زاید آل نهیان، امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی، و وزیر علی الثعادی، قطر، مارشال فیلد سید عاصم منیر احمد شاه، پاکستان، رئیس‌جمهور رجب طیب اردوغان، ترکیه، رئیس‌جمهور عبدالفتاح السیسی، مصر، پادشاه عبدالله دوم، اردن، و پادشاه حمد بن عیسی آل خلیفه، بحرین، در مورد جمهوری اسلامی ایران و تمام موارد مرتبط با یک تفاهم‌نامه مربوط به صلح، برقرار شد. توافق‌نامه‌ای به طور کلی مذاکره شده است، مشروط به نهایی‌سازی بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر، همان‌طور که در بالا ذکر شد. جداگانه، من با نخست‌وزیر بیبنتانی، اسرائیل، تماسی داشتم که به همان ترتیب بسیار خوب پیش رفت. جنبه‌های نهایی و جزئیات توافق‌نامه در حال حاضر در حال بحث هستند و به زودی اعلام خواهند شد. علاوه بر بسیاری از عناصر دیگر توافق‌نامه، تنگه هرمز باز خواهد شد. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/news_hut/65027" target="_blank">📅 00:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65026">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahshid</strong></div>
<div class="tg-text">بله  مگه چیه ما با ۹۰ هزار ... گواهینامه مون گرفتیم</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/news_hut/65026" target="_blank">📅 23:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65025">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گواهینامه شده ۱۵ میلیون تومن!!!!
الان یکی میاد می‌گه حاجی ما با ۵۰ تومن گواهینامه گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/65025" target="_blank">📅 23:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65024">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بستن تنگه‌ی هرمز در جنگی که ۹ اسفند آغاز شد، تمامِ معادلات آمریکایی هارو بهم ریخت، اون‌ها حتی چند روز قبل مین‌روب های خودشون رو هم از منطقه خارج کرده بودند! دومین مسئله‌ی شوکه کننده برای اون‌ها حملات وحشیانه به کشور های عربی بود  هر زمان آمریکا_اسرائیل به…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/65024" target="_blank">📅 22:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65023">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">باز تو این دقایق فیک‌نیوز و نویز‌ها بشدت افزایش پیدا کردن، اخبار ضد و نقیض زیادی به گوش می‌رسه، اما کلیت ماجرا اینه که تهران آخرین پیام خودش رو به عاصم‌مونیر داده تا به آمریکایی ها برسونه، ترامپ نهایتا تا دو روز دیگه بعد از دیدارش با ویتکاف و کوشنر، تصمیم…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/65023" target="_blank">📅 22:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65022">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">باز تو این دقایق فیک‌نیوز و نویز‌ها بشدت افزایش پیدا کردن، اخبار ضد و نقیض زیادی به گوش می‌رسه، اما کلیت ماجرا اینه که تهران آخرین پیام خودش رو به عاصم‌مونیر داده تا به آمریکایی ها برسونه، ترامپ نهایتا تا دو روز دیگه بعد از دیدارش با ویتکاف و کوشنر، تصمیم می‌گیره، یا از خواسته هاش عقب نشینی می‌کنه و یا اینکه دوباره جنگی برای اعلام پیروزی شکل می‌گیره، تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/65022" target="_blank">📅 22:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65021">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ شنبه با ویتکاف و کوشنر دیدار می‌کند و یکشنبه تصمیم نهایی برای توافق یا جنگ دوباره گرفته می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/65021" target="_blank">📅 19:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65020">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ شنبه با ویتکاف و کوشنر دیدار می‌کند و یکشنبه تصمیم نهایی برای توافق یا جنگ دوباره گرفته می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/65020" target="_blank">📅 19:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65019">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
📰
ترامپ در گفت‌وگو با آکسیوس:  در حال حاضر احتمال کاملا 50 / 50 است که یا با ایران به توافق برسیم یا دوباره جنگ از سر گرفته شود. یا چنان محکم‌تر از همیشه به آنها حمله نظامی می کنم که تا حالا مثل آن را ندیده‌اند، یا توافقی خوب را امضا می‌کنیم + ترامپ شنبه با…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/65019" target="_blank">📅 19:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65018">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
فایننشال تایمز: ایران و امریکا به یک توافق آتش‌بس ۶۰ روزه نزدیک شدند!!  @News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/65018" target="_blank">📅 19:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65017">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
📰
#مهم؛ فایننشال تایمز: میانجی‌ها معتقدند که به توافقی برای تمدید آتش‌بس به مدت ۶۰ روز نزدیک شده‌اند.  این پیشنهاد شامل: بازگشایی تدریجی تنگه هرمز گفتگو درباره رقیق‌سازی یا انتقال ذخایر اورانیوم غنی‌شده بسیار ایران کاهش محاصره آمریکا بر بنادر ایران رفع تحریم‌ها…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/65017" target="_blank">📅 19:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65016">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0xOhwt87enRVtxV5Tvw62HCq6E8QBzx592MO_mVokfvrse5GzylfR42m2CoL5N0bUNRglVYvnX53ffjUmAqe6dWaf75eQUdJc49fd3x1r6UcXAXe_7MTEOPHW2ykc4kAcr5bvGecHnZw6BeDMr70zy5Wtwt1g_w52HOF5qBwidJq3oyV2NPsUmSZzkGufEP3f39ln63zwJPlTaSGqI9lDsjbHp4a9PTBvFlVJGfdUyZPbRZCL8XbgSlWOnYz-kybzRsQf51BmYgjcs6Vix16PendMApzz-mgsucptnjsVOnUTaLTTGZ-qefPnPDVspSvqa3j8gSwzTFxVjrkXrvuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید ترامپ تو تروث‌سوشال: ایالات متحده خاورمیانه!! با پرچم امریکا روی نقشه ایران
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/65016" target="_blank">📅 18:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65015">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ مارکو روبیو: ممکنه امریکا به زودی خبری در مورد ایران منتشر کنه شاید هم نکنه امیدوارم این اتفاق بیفته
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/65015" target="_blank">📅 17:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65014">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b75d0f1f7.mp4?token=LKY4YlSUyKduwXkUI4b3xI629DMPnwzcy6wkxIvtqkWi7wIVqYY8dqqkU2g4_sbBIUWF3ijC2Drw7RGvUZkC8LHHrT7P_FbnCl5WSthM5NIXQORWm1IT8X-qqQp8Tqsiy2T618Fblx3IwFK-n5_wjFofZ822G973gNjj7LAaS74NekcXqU7SLBPBHlnUWTc_OukgjS8V27CLjt8BFVzsjL8scDf0tIMUM6qmpCkHSXuXUPZnl5u_raQhVFCtGGE_agtVWqz1PMzEBzmEFr07o0HbsEb5K09adIj2YwTaa4MoGWLdFPWjw7z5FC4MSg4KsdTfeHc1JN4g8DJmzXzBKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b75d0f1f7.mp4?token=LKY4YlSUyKduwXkUI4b3xI629DMPnwzcy6wkxIvtqkWi7wIVqYY8dqqkU2g4_sbBIUWF3ijC2Drw7RGvUZkC8LHHrT7P_FbnCl5WSthM5NIXQORWm1IT8X-qqQp8Tqsiy2T618Fblx3IwFK-n5_wjFofZ822G973gNjj7LAaS74NekcXqU7SLBPBHlnUWTc_OukgjS8V27CLjt8BFVzsjL8scDf0tIMUM6qmpCkHSXuXUPZnl5u_raQhVFCtGGE_agtVWqz1PMzEBzmEFr07o0HbsEb5K09adIj2YwTaa4MoGWLdFPWjw7z5FC4MSg4KsdTfeHc1JN4g8DJmzXzBKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقائی، سخنگو وزارت خارجه:
ما هم بسیار دور و هم بسیار نزدیک به یک توافق هستیم.
دیدگاه‌ها به هم نزدیک‌تر شده‌اند، اما نه به حد یک توافق — بلکه به حدی که ممکن است بتوانیم به راه‌حلی برسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/65014" target="_blank">📅 17:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65013">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73653df566.mp4?token=q3WawO1uHWs9-a0WXoKzZRcvLUxc7PZkAvx1imIEUywbLiR9hWOHJzew73cMFa466Xpz6N_F6_eghrVBlMhmA2OYAWtD7leO7rKo3Td6xh6hrSEwgfpe3xBx7TFQUoSNioRNP-_-I1vg8v8CINVnVj_b-cUPoCd8a4tDdU5ztO_8tFfl8NVxu6gADwMJdkJ75FURQnrTDcZHIllRDan1g-660WeIyoIbJVGUvKuuuGsfW7ppc--Hu1fbNt6_MSfu3CvK6njkaJsnxZWXuxZ0f3mVr-kvpLtxcKdEZUEmBcWfEBgPCVGlvctvUsLGI0SiXAmR1m4oHV5dDMh3qumkfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73653df566.mp4?token=q3WawO1uHWs9-a0WXoKzZRcvLUxc7PZkAvx1imIEUywbLiR9hWOHJzew73cMFa466Xpz6N_F6_eghrVBlMhmA2OYAWtD7leO7rKo3Td6xh6hrSEwgfpe3xBx7TFQUoSNioRNP-_-I1vg8v8CINVnVj_b-cUPoCd8a4tDdU5ztO_8tFfl8NVxu6gADwMJdkJ75FURQnrTDcZHIllRDan1g-660WeIyoIbJVGUvKuuuGsfW7ppc--Hu1fbNt6_MSfu3CvK6njkaJsnxZWXuxZ0f3mVr-kvpLtxcKdEZUEmBcWfEBgPCVGlvctvUsLGI0SiXAmR1m4oHV5dDMh3qumkfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توئیتر اکانت ترامپ که با هوش مصنوعی به ویدئو درست کرده از مجری سی‌بی‌اس که مخالف خودشه و ترامپ میندازدش تو سطل زباله :/
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/65013" target="_blank">📅 15:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65012">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RJQ7UQQaeeVyme0Cy3RksoCBJUl7m0BQKV4IParg7FNEH9zVdjNnG7UfIIKVFIi5cfjCjA9RRsMNDW-0TE8cnxq3bdPSf8d_0C5magzDiVRUDyjYgrzuYnCMh4M2MfLUbCioWfgV1GvOZoy6OQ1BvpDSJCtn-WZ2XH_k9jxH-_DvXwhQRiJdA9EWjxS0XoU8WNn4apPXFjImKVhBP_AEm8QcedfhBMUFBgsQ-Pc4vx-Eo-IiU4edt1_0NoJ9RRCsxOKYsQAGkFK_gvLkvzVaxMBQL-Qe73WWjm3CGfQMxyrBxvPjG9iuvPKPLI_kN9Ef1L1mb1VrtPcE5pGCSGOlRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ عروسی پسرش بود نرفته، آخر هفته برنامه گلف داشت که کنسل کرده و تو کاخ سفید مونده حالا خبرگزاری‌ها شدن دو دسته یه دسته میگن توافق نزدیکه حتی متن توافق منتشر میکنن یه دسته متن توافق بقیه رو تکذیب می‌کنن و میگن کلا حتی نزدیک توافق هم نیستن دو طرف.  این وضعیت…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/65012" target="_blank">📅 14:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65010">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GCd74cIsIynOS2fDwK3JN38l8vJ9CZ_oihmWpjcaGeQ9Wl5_A7-GpyHodGfEc3iZkE8u77EMpq3eBOHoO7uIyaGi_H0yXRi5fKtpFlO5z3GYg_aF1ZUaI-1_Amw10fQt96TIHv82zGxy7cCFX84I6nbli_FQYakJYC7aaUYL4WQOXvNv1U2R_voqum_W7nAFAkDVBR-qYfCVmeg3jje7CSYRn76gt1haZ1-rbauFCqEM1_x5z41MGDjL2UPCcigTAHOitdAEw6C2cYX95xLBcDPGPEHb-2gjgNjbui_UIIjPjd4gj7waDfzf2_QR9H2h4y2Qaq57CVM_iUGlbLmDdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6eddfffea5.mp4?token=tAJAVradaiADfOb3vvmDOzCZbzuQFH_LmI7Gyk8LfMYIgY7A3wX72K0y5QouRCoKC9IvkQkuZ9BS2WDUFRNK57EvColnTOxjdCalYaiuUoN3l2U2jmlSDakjIpXD57FQyS6W8DbEHqJIvqpgo_uhNTxmLM9ixCSg590VT2aMcSq5hZwqAqJfE4QTnb6DFxcQ9HW2nYvaiVc3PcI1vogI4TjN4cXPYnMXFwriE3ys3gn9c0APs5BbKIHYh06FFOm2khLdwEqipWXo4w7FO_7vg_F5K3-Bx2v9Cb3dBQFjQrJIMDxNxhVvpzkWtoUg-dnaAHmsp67X8O4rjOaopCP_1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6eddfffea5.mp4?token=tAJAVradaiADfOb3vvmDOzCZbzuQFH_LmI7Gyk8LfMYIgY7A3wX72K0y5QouRCoKC9IvkQkuZ9BS2WDUFRNK57EvColnTOxjdCalYaiuUoN3l2U2jmlSDakjIpXD57FQyS6W8DbEHqJIvqpgo_uhNTxmLM9ixCSg590VT2aMcSq5hZwqAqJfE4QTnb6DFxcQ9HW2nYvaiVc3PcI1vogI4TjN4cXPYnMXFwriE3ys3gn9c0APs5BbKIHYh06FFOm2khLdwEqipWXo4w7FO_7vg_F5K3-Bx2v9Cb3dBQFjQrJIMDxNxhVvpzkWtoUg-dnaAHmsp67X8O4rjOaopCP_1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابک زنجانی از برنامه جدیدش به نام مای دات رو نمایی کرد و برای تبلیغات نوشت:
اینستاگرام پولی میشه ولی برنامه ما رایگانه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/65010" target="_blank">📅 13:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65009">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
⭕️
ایران با صدور اطلاعیه‌ای، پرواز در بخش غربی حریم هوایی خود را تا صبح دوشنبه ممنوع اعلام کرد.  @News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65009" target="_blank">📅 03:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65008">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
⭕️
ایران با صدور اطلاعیه‌ای، پرواز در بخش غربی حریم هوایی خود را تا صبح دوشنبه ممنوع اعلام کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65008" target="_blank">📅 01:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65007">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">واقعاً خوشبحال جمهوری اسلامی که با چنین اپوزیسیون احمقی طرفه، نه تنها پادشاهی خواهان با [به اصطلاح] دموکراسی خواهان دائما درگیر هستند، حالا خبر رسیده که علی کریمی و شاهین نجفی از داخل گروه پادشاهی‌خواهان هم باهم بشدت درگیر شدند
!
شما با این وضعین می‌خواین در مقابل آخوند بجنگید؟ جای تاسف داره واقعاً، حیف مردمی که گوش به پست و توییت های شما بودند و هستند!
#hjAly</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65007" target="_blank">📅 22:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65006">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec1cebe91.mp4?token=iK3UK5tD1kAJtieg5Pg5UBpkRtnlJZnDC2PXZF5yFGb4cLZ6pLEm7i4IgJW7NL7SdS2zcz9rpx8r85UUpwJK9Tel71_42_NuY4UXynkAFuk0FepACKSLBbsZHijXymiWwCzLoMHsXb_xRgzKEx4LobGuDaXnqcH83gZbkntYK7M0Kn9SV93D4UadHbfZ0WCQ4Cl0FExbYYe5ItOlYoq280QI4rqTDyGcdNgRN7OydCWtfGdGTiLVEgEyltg5DkTheU9i_989oy0_rh8j3GxNNC6SfkhBhv21BrYH_9ef5Ioj8bgu3i_4CS1L4dBpPlu2Zun9syINod-m2-9tuL-SRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec1cebe91.mp4?token=iK3UK5tD1kAJtieg5Pg5UBpkRtnlJZnDC2PXZF5yFGb4cLZ6pLEm7i4IgJW7NL7SdS2zcz9rpx8r85UUpwJK9Tel71_42_NuY4UXynkAFuk0FepACKSLBbsZHijXymiWwCzLoMHsXb_xRgzKEx4LobGuDaXnqcH83gZbkntYK7M0Kn9SV93D4UadHbfZ0WCQ4Cl0FExbYYe5ItOlYoq280QI4rqTDyGcdNgRN7OydCWtfGdGTiLVEgEyltg5DkTheU9i_989oy0_rh8j3GxNNC6SfkhBhv21BrYH_9ef5Ioj8bgu3i_4CS1L4dBpPlu2Zun9syINod-m2-9tuL-SRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امتحانات نهایی پایه یازدهم و دوازدهم تو بازه ۱۵ تا ۲۰ تیر به‌صورت حضوری برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65006" target="_blank">📅 22:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65005">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🎙
خبرنگار: آیا در عروسی پسرتان شرکت می‌کنید؟
🇺🇸
ترامپ: او دوست دارد من بروم. من سعی خواهم کرد. گفتم این زمان مناسبی برای من نیست. من یک مسئله به نام ایران و مسائل دیگر دارم. او شخصی است که مدت‌هاست می‌شناسمش.  @News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65005" target="_blank">📅 21:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65004">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
العربی‌الجدید: سفر عاصم منیر به تهران دلیلی بر توافق نیست و پیام جدیدی منتقل نکرده است، گزارش‌ها درمورد مفاد توافق گمانه‌زنی است و اختلاف بین طرفین هنوز زیاد است.  @News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65004" target="_blank">📅 21:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65003">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
📰
العربی‌الجدید به نقل از یک منبع نزدیک به مذاکرات:  سفر فرمانده ارتش پاکستان، عاصم منیر، به تهران به معنای این نیست که توافق در دسترس است. گزارش‌ها درباره وجود پیش‌نویس احتمالی توافق صحت ندارد و صرفاً گمانه‌زنی‌های رسانه‌ای است. وزیر کشور پاکستان پیام جدیدی…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65003" target="_blank">📅 21:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65002">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
📰
العربیه: طبق منابع العربیه، انتظار می‌رود پیش‌نویس نهایی یک توافق احتمالی میان ایالات متحده و ایران که توسط پاکستان میانجی‌گری شده است. که ممکن است ظرف چند ساعت اعلام شود.  شرایط کلیدی آن عبارتند از: آتش‌بس فوری، جامع و بدون قید و شرط در تمام جبهه‌ها، از…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/65002" target="_blank">📅 21:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65001">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرگزاری های حکومتی: عاصم منیر وارد تهران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65001" target="_blank">📅 19:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65000">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2227480c5d.mp4?token=On2Uc16Qx8N0ZtlttPQrbTizlNDHee9VCnv4Usoe6-uiCbT7F2GVyU6W_rh889Dmj0YGGY3yy4XZZm-gozVNcbv_QG61ruWN1DuYZHd2tKZpEJ7lynmoprQReAL2_nAemmER3wozacU_E6IZFRljURWsofVk3EcKe-EueCTBQXMEgBH3WPmJ6FFGscuNNiSxXfnXPy8TneiisuvHbHPD6IhWgj5SQzpScglpCmvSnafNBQecD3iqoyFUQRV3AP3DNLwVrp51aLmR-2M_ExPH_AQmQkiE5k7Z5hS2xfiCTjprImxE-arTxb6yZTW_HonxUk7DPRG15W3oLcO1hdQonw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2227480c5d.mp4?token=On2Uc16Qx8N0ZtlttPQrbTizlNDHee9VCnv4Usoe6-uiCbT7F2GVyU6W_rh889Dmj0YGGY3yy4XZZm-gozVNcbv_QG61ruWN1DuYZHd2tKZpEJ7lynmoprQReAL2_nAemmER3wozacU_E6IZFRljURWsofVk3EcKe-EueCTBQXMEgBH3WPmJ6FFGscuNNiSxXfnXPy8TneiisuvHbHPD6IhWgj5SQzpScglpCmvSnafNBQecD3iqoyFUQRV3AP3DNLwVrp51aLmR-2M_ExPH_AQmQkiE5k7Z5hS2xfiCTjprImxE-arTxb6yZTW_HonxUk7DPRG15W3oLcO1hdQonw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو:
ما باید شروع کنیم به فکر کردن درباره کاری که اگر چند هفته دیگر ایران تصمیم بگیرد، «ما اهمیتی نمی‌دهیم؛ ما تنگه‌ها را بسته نگه می‌داریم؛ هر کشتی که به ما گوش ندهد یا به ما پول ندهد را غرق می‌کنیم» چه باید بکنیم — آن وقت کسی باید کاری در این باره انجام دهد.
امروز این نکته را مطرح کردم؛ خیلی‌ها سر تکان دادند؛ خیلی‌ها بعد از آن نزد من آمدند و آن را تأیید کردند، اما امروز خبری برای شما نداریم که چیزی در حال وقوع باشد.
باید پلن B داشته باشیم برای اینکه اگر کسی شروع به تیراندازی کرد و چطور تنگه‌ها را باز کنیم، و من امروز این نکته را مطرح کردم. نمی‌دانم که آیا این لزوماً مأموریت ناتو خواهد بود، اما قطعاً کشورهایی از ناتو می‌توانند در آن مشارکت کنند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/65000" target="_blank">📅 18:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64999">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/news_hut/64999" target="_blank">📅 18:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64998">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwoo8guTUV65lq3oG8wH-BfdM6swDijvSIWvXtvyYjSMDHoi37lJ_VoJazNJGlVTE3CDDxPyl4fNy5KMUfGk8FHFXMhKjqm2MmAzRp8NKa-XWZgHeGRJBce4eZTALjj8-F8muYH5sTdkrMi-E4tGmLbGk_WKt_uWrjGhnm29Wdi7O0mQKXtwgWM1ocMg1JyoCjFz87YaIdiSU4PNLEI-66at9eHUpmCDAOg6EpbsPJv7vEvFzDKJJ4z03Fd3Z0ITkOwMQMfNtJN0gOa6tsqH794LVohBDXRA8a_WHgrY7rnkb8hBJUIToc7u43p2XOIFeRPNZ11uwO4kFd3jQ-LGSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
لارنس نورمن، خبرنگار وال استریت ژورنال: یه منبع میگه هر چیزی درباره پیش‌نویس توافقی که داره می‌چرخه، دروغه و صحت نداره!
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64998" target="_blank">📅 18:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64997">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
📰
رویترز: یک تیم مذاکره‌کننده قطری امروز به تهران آمده است با هماهنگی ایالات متحده برای کمک به پیشبرد تلاش‌ها به سوی توافقی برای پایان دادن به جنگ با ایران و حل مسائل باقی‌مانده.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64997" target="_blank">📅 17:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64996">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHfEAI2uzP49zZj-2eIWuh8sKGWDputmFROvzWUBBerZbUAb5TPGmW1C_pLcBxBzWMB53_AqxNk9RmX4M9d_WkNCcqOKpl021O_0ULzodaZG3L8jENeZiuhi-BmBbyogS3AdBHdSUJhMyhud3ZspzI1KFIuHyutQGUekFjm9-G98OLYCpQVeOl2o62lAAlC_dnjFYITFIhn3CT1wDUacsIYRjE_YVXRa90LPsj7WopE38QqxQAPOplNg1U2whUPAqWzWVjJX4_rYlNHjKFRfg4r5l3EE_QLDUnVYsWtUwOG0OFUHoMNA9a7IKg95-A63f1zJoEyK1T9lvgZ5uKqODg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو هواپیما دولتی پاکستان راهی ایران شدند؛
احتمالا عاصم منیر در راه تهرانه
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64996" target="_blank">📅 16:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64995">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OV1FkoN86TpuoM0ffGkjuuLPJz4kBj8UC80yPWLx3CgDaxxb2YZKiTCVurrF1tdgfZVfWfE0VM6URqz7jZaIlqz6AiSxHoyDisXhLsOkmC3YVGBJj9DQ2TWnPSh0X9mjMwtD62IXkDKG5MxhVvc5qhlNmnSwwyClWF4wz3-AMMLoQt1cI6tFYE2E6fBHleyGP4WpZA5i3Oe_cd7sH5ijRrRk5cJ_U9V_kTIXwK8JBq9OzBt2UFyOakZxfpOKY7VWjrY7-9U9OQx9rlGGkL76lPq2tgOsr7WgKfcDyPUeVSOqg1k3yfR95i_Mxb7u37XOGvfRxmM35IQClvAiu8FQHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یزدی‌خواه، نایب‌رئیس کمیسیون فرهنگی مجلس: نهادهای بالادستی به این نتیجه رسیدن که بازگشایی اینترنت به صلاح همه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64995" target="_blank">📅 14:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64994">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سپاه: تو ۲۴ ساعت گذشته به ۳۵ کشتی اجازه ورود و خروج از تنگه هرمز رو دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64994" target="_blank">📅 14:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64993">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
سفرِ «عاصم منیر»، فرمانده ارتش پاکستان به تعویق افتاد، این یعنی هنوز اختلافات ایران و آمریکا حل نشده
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64993" target="_blank">📅 23:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64992">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3890f54566.mp4?token=H2Do92CDS_M52ZbY1g9w-rz1frqjNbUTZ6sqYlPI-wfy4tlDOFHtqcZQ4un6g5bic7wN9oimBpO3r-Uo0Gbyh9X4c2OBglS3SGze8z3WyFdW5o_TVOJGo3KVlhXPt7Tspah37vgzv0OswbR_nwp56HPWY7dfLbtbPgApDHC_9exZICWo6Lovt7HnT1-2Fbf_RjA9VjpRejixS_JjKg0v_ByllUSZ9gtsnxdG6vbq27_0IRQXUbDG3hz1GLA87YTWJ8No-MC92QIxsUPDMK6TzPinObi-BUXW4R3xxvM-JSKVSQGgo_LsvmbsHqGwXm1iB3r_oINt6FvNpQUzlgxH2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3890f54566.mp4?token=H2Do92CDS_M52ZbY1g9w-rz1frqjNbUTZ6sqYlPI-wfy4tlDOFHtqcZQ4un6g5bic7wN9oimBpO3r-Uo0Gbyh9X4c2OBglS3SGze8z3WyFdW5o_TVOJGo3KVlhXPt7Tspah37vgzv0OswbR_nwp56HPWY7dfLbtbPgApDHC_9exZICWo6Lovt7HnT1-2Fbf_RjA9VjpRejixS_JjKg0v_ByllUSZ9gtsnxdG6vbq27_0IRQXUbDG3hz1GLA87YTWJ8No-MC92QIxsUPDMK6TzPinObi-BUXW4R3xxvM-JSKVSQGgo_LsvmbsHqGwXm1iB3r_oINt6FvNpQUzlgxH2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آیا در عروسی پسرتان شرکت می‌کنید؟
🇺🇸
ترامپ: او دوست دارد من بروم. من سعی خواهم کرد. گفتم این زمان مناسبی برای من نیست. من یک مسئله به نام ایران و مسائل دیگر دارم. او شخصی است که مدت‌هاست می‌شناسمش.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64992" target="_blank">📅 22:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64991">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43db173db6.mp4?token=iN-IhaYYVikEwl0J3yqHz9q5TcOuHQuHvcmhAM435psq-LP3hshvj3j5vy9POjy0XHQ9xaTLUFbRnEDtgpWRHfy6u530RG_lIgA9Nq7cVtLvfOTivuAGf-hKijvqKF267WA1NIrAKqgisV-d5T1Mkszf6pa3s_Uq9GtjyFvlBlwZXUaXuRR3j8uTS7nlJtYtBKkF4UAdElUJjjMVVjZwLm4ZI0bfZmtWX7C47ebVGpE0_FIN_gKUXhFZrEDMTRxjFlr2wBIIRXJtrcNjr3dhc-BKYZS9jWmf-jXogDjtGeEN7r17b_l7lrWqeSZoVXea-8xyBqTcy8uWkQTXvZ_CuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43db173db6.mp4?token=iN-IhaYYVikEwl0J3yqHz9q5TcOuHQuHvcmhAM435psq-LP3hshvj3j5vy9POjy0XHQ9xaTLUFbRnEDtgpWRHfy6u530RG_lIgA9Nq7cVtLvfOTivuAGf-hKijvqKF267WA1NIrAKqgisV-d5T1Mkszf6pa3s_Uq9GtjyFvlBlwZXUaXuRR3j8uTS7nlJtYtBKkF4UAdElUJjjMVVjZwLm4ZI0bfZmtWX7C47ebVGpE0_FIN_gKUXhFZrEDMTRxjFlr2wBIIRXJtrcNjr3dhc-BKYZS9jWmf-jXogDjtGeEN7r17b_l7lrWqeSZoVXea-8xyBqTcy8uWkQTXvZ_CuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🚨
ترامپ:
ایران نمی‌تواند اورانیوم غنی‌شده خود را نگه دارد. به محض اینکه آن را به دست آوریم، احتمالاً آن را نابود خواهیم کرد. ما آن را نمی‌خواهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64991" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64990">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIGDVzZKKpIwvDdr1VkonBhev7Q0sI2lp5qsOeEWbaviII3ZT-7CturhwUcZuPW7Cc66boiJ_4ESprp0L9qbQBRAN0Gb4H_24S3EFZTjmveXRJlvaGGyVqGvi0D9ouDZtK73tSQuNKPcFM72spElQ7p_vZ6_oh5fTjj2uTEJotIB1oH5eglffhV65TNGDnv2sLzXmozthOm2FX9WSqY7LMaPtgWsfZCPcwmNYv1EXmrjpRneGaTmTg-7pDQ8dFmyGoIY_135bz_dKV1kmaRyrollizAX3pnTjxfirJwcqj5dZXTpzJ7NQpC6Q3L_g7psFUnN_U4Zs0-PVxkvExxLpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ یه پست از نشریه نیویورک پست بازنشر کرد که تیتر خبری‌ش هست؛«چطور میشه تهرانو تو سه حرکت نابود کرد»
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64990" target="_blank">📅 16:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64989">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvfM4l5OEzLYCP76Lgf5B9RHWpQOpLSEgMHzgebJG4Ld1WXrKOhm_WWonQL11ZLGHvOtLgPrLa9mXXUpq6w3TSSqStBhBDkk8jrWQfQxF9CSC6cZa_RKXOCnXeHL-ybgLb3-ScG33JwG-5m72ewpTmjgqg_-OyyOKolvbEk-wlKxVMMoBPWHhT1i8jL7GU-uxPeDBMg5n6W3osML2Sn_kafUfwX0Ykv--_Y584FUf_NfnWwKJU23uRHpIGBmeq2afORzTvesbjRS6DuHu-z1DpzgnKcdQwZwf8txruiYc2YGZmRMrvcTGBEIzOIyrgxpZbgLYjPCkXM1F3KRH_ZusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ جدید هزینه‌ ریجستری گوشی‌های آیفون
ریجستری آیفون ۱۷پرومکس، ۱۰۴ میلیون تومان!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64989" target="_blank">📅 15:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64988">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRkDZK_UvZE6L4ePGq6SsAx7RBRQcWh61AemOCOOkl-YxTM_RHDAKG7rgTa00zDLoq3vl53-eGqktkImAPCN-r4h9wAtBGr8vOzblX-tNNZyrv4eCmPp4MmDZX2jY-kL-hUxzOCtjOg_FVl-UJ6OUVlHROwWj1o53l05kg07bdUSTuNzgv1X5rVxIx9Sc6E9_1Pduw346h2Yq8d0JCr1ujFAFWS5Zpg7hYqAI_GyZx7WE48ruFkS1QPvSROWMDFYEHDhFEnpWTU7VNndd2DoxCC17xHoYyRB53UykUjv8J5pkmRi5vUNwjzCTUn1KKaHllL1YwNy5S7Dp9sxFqQqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فهرست کاخ سفید از مهم‌ترین دشمنان امریکا که در دوره فعلی ترامپ حذف یا دستگیر شدند:
رئیس‌جمهور ونزوئلا - مادورو
رهبر رژیم جمهوری اسلامی- خامنه‌ای
معاون رهبر داعش - ابو بلال المنوکی
و برای رائول کاسترو رئیس‌جمهور سابق کوبا (و برادر فیدل کاسترو) کیفرخواست صادر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64988" target="_blank">📅 15:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64987">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
📰
رویترز: منابع ایرانی می‌گویند رهبر معظم(مجتبی)اعلام کرده است که اورانیوم غنی‌شده باید در ایران بماند.  آمریکا می‌خواهد اورانیوم بسیار غنی‌شده ایران به خارج فرستاده شود مقامات اسرائیلی می‌گویند ترامپ به اسرائیل گفته است که این اتفاق خواهد افتاد دستور رهبر…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64987" target="_blank">📅 14:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64986">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
بندرعباس ۴.۶ ریشتر زلزله شد
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64986" target="_blank">📅 13:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64985">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QAODG7vKq8BqJUpys5Y_n7-yOKAa0ss0gaagj7zVCuo6vAh7MyGxzDjMLFhuYC6IuXMbTVXGRcHDhbcpH_Yd4mjEoBPyh85EFxlDSR1VszcWC5TXpnWQ6QY-cQogtyipO_reHWgRkYcEBRtc5F9raFx0Lug5iCEKbWsBduaRveUaDvtiiHusPCbNV6Hir_RRxKZ9cSDc55BgkAsLZk8rEFsZIx1vjzOUV65MeEbB3Sv5K963EjOd7jXa4i746d5I6YLVt-sgn7Ln9QzQ3f0JfPrTmTazNCAQMuzU0gp33j4BN28_rtSsuTMH5RBdRLJ6HEBbfNEgjHBYtolrp3KQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شریعتمداری: تا زمان شکست امریکا و کشتن ترامپ تنگه رو باید ببندیم
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64985" target="_blank">📅 11:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64984">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: اگر فرمانده ارتش پاکستان به ایران سفر نکند، توافق نهایی ممکن است ظرف چند ساعت اعلام شود  @News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64984" target="_blank">📅 10:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64983">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرنگار: آقای رئیس جمهور خیلی از خانواده ها در آمریکا نگران گسترش هوش مصنوعی هستند، نظرتون چیه؟
ترامپ: هوش مصنوعی عالیه، ایران نباید سلاح هسته‌ای داشته باشه :)))))
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64983" target="_blank">📅 04:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64982">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: کار برای نهایی کردن متن توافق میان واشینگتن و تهران به طور جدی در حال انجام است و دور بعدی مذاکرات پس از حج در اسلام‌آباد برگزار می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/64982" target="_blank">📅 18:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64981">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: کار برای نهایی کردن متن توافق میان واشینگتن و تهران به طور جدی در حال انجام است و دور بعدی مذاکرات پس از حج در اسلام‌آباد برگزار می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/64981" target="_blank">📅 18:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64980">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q6kv53ZSC2oAqhL5CRDtMtQGLbfJc9sfHfURgLu5Ip2ebwU1THrEyo7HWjW6JaWxdOpjyXLYJo3DpZdJ-td52TGuMqj9v5_TUEEczB8ED8iXBxURen9ut0aAgrcE6uqzVyIl7YW9tNQmlQ7k0C7vsi273MkAmiRxM-PJ7zjU76SOpTbphraE6fxxe_gl_aEMG519A6pSfEDEZPwfl6hBN8Tk7lDrAFV171VSiIw6C9Nf6GHRHcgLQXjdxCLmv33UIzWREkhKGtkbhgxiY0ubbZit7cLs5GvNNGN7KHWT8_qQb31lhE8HJ9PaMFat28ulZPhskR8stINvTrWyAYvb7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای مرضیه حسینی خبرنگار ایرانی کنگره: یک منبع مطلع اینجا در کنگره به من گفت که ترامپ روزهای چهارشنبه یا پنج شنبه پیش رو، به ایران حمله خواهد کرد.
به گفته این فرد، این حملات برای یک عملیات “دو تا سه روز” متمرکز خواهد بود و به مراکزی با هدف بازگشایی تنگه هرمز انجام خواهد شد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/64980" target="_blank">📅 13:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64978">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MuuXMksBmKCBwXk_KOEQvN9jN3G5kM5DUEeJmvawoeZZH01BI1f_359n3_7lJA8x_ezOUAUGf8uUkKjyGOysHSeqrpnwCavIN4dsDp71OOob7qLlm4oTKdX6PCmPwKalGERXFvvS-5H1LMiBENnOwM3_XZ34tkhhl9CHpW2BNerrSoN8Y4hCu3xExMhIi5R8d8FVTBSREy8W_zL-qrrRgrV-QVYoK9rFdegvmlqSuJmCALBgsnozkpFyVhpyQnFlUbse5xkXrsF89zNi__plOH_7xluE85GwBqYl1UBYTIssy44kAH13v2VbRFFonAsvXYK0U7wClktUFFKTlgPvGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XByz6GLI4U9Z6rO5f-HxJqHne9qLo4URM2O_N5pDSsKWgeFIhMXi0EYMeIlCKzzY75gTbt0b1fwZkxRJFrTomu2vNpKX_XYBqXMHg5Xvt_5RiUtxShI7g2Pg6o_NrmzV99NPaxQWGjwY5BbhCEBOb5B8D2EJLY8dS49ePJWGFoHEXpHGBIUsuZpMrcimVoiAoH_ThpH5vPahK8DadtXuy1FF7yLuwgsvAZuW6vSjYxf8Rs-UCQ-xGwER1jiPLpQzTll5bfd8MEGLsOU3rpJukqv0bLrK5bzR1PuppaGO5rH1GcTl3kmZMLjEuvyiWZD5DfHWEVKul4-LPxQMSuoHDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
گزارش NBC از موبایل جدید ترامپ  به نام «Trump mobile»:
مدل T1 با قیمت «تشویقی» ۴۹۹ دلار به فروش می‌رسد و به صفحه‌نمایش ۶.۷۸ اینچی، دوربین اصلی ۵۰ مگاپیکسلی و حافظه ۵۱۲ گیگابایتی مجهز است.
گوشی ترامپ موبایل در چهار نقطه از بدنه و نرم‌افزار، لوگوی «ترامپ» حک شده، پرچمی آمریکایی با ۱۱ راه‌راه به جای ۱۳ راه‌راه روی آن حک شده و از پیش، شبکهٔ «تروث سوشال» روی آن نصب است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64978" target="_blank">📅 13:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64977">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358ed734a6.mp4?token=R7tgp0dd-73lHs-ilKgNbskKyfSmBNmW5Ww7EQnEeRRc4EdwwOWhQkGgiXT1FLP2hqMC4tkLI-PtAUA3Ld0aE7bOC7zAo2qaQ8jnPJ4aww2AjKc9vHyYGyF6KAyueha7-l026JqbVm3MWhKO834RWd8DR7RvH-Vfbs_mVySYq4y8-6yEdnkfMkhdxXiw1dXsTym1q0KTLK5i74eL8QUbuHyHR-Vz-NLqdP_UzeeuMuIwZm62b7jv8PNoF15zDYV_GdA7arj_gJcs_RjR2w1LPd9jO7Xxtf6h9Ko6r4vQjsfsOXOsGFHUYLY9Vl1WVCIG00ot9RI_FZEub7TC--zt6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358ed734a6.mp4?token=R7tgp0dd-73lHs-ilKgNbskKyfSmBNmW5Ww7EQnEeRRc4EdwwOWhQkGgiXT1FLP2hqMC4tkLI-PtAUA3Ld0aE7bOC7zAo2qaQ8jnPJ4aww2AjKc9vHyYGyF6KAyueha7-l026JqbVm3MWhKO834RWd8DR7RvH-Vfbs_mVySYq4y8-6yEdnkfMkhdxXiw1dXsTym1q0KTLK5i74eL8QUbuHyHR-Vz-NLqdP_UzeeuMuIwZm62b7jv8PNoF15zDYV_GdA7arj_gJcs_RjR2w1LPd9jO7Xxtf6h9Ko6r4vQjsfsOXOsGFHUYLY9Vl1WVCIG00ot9RI_FZEub7TC--zt6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان،عضو کمیسیون امنیت ملی مجلس:
امیدوارم خبر سفر عراقچی به نیویورک برای مذاکره در خصوص تنگه هرمز دروغ باشد!
چرا ما در خصوص موضوع تنگه هرمز باید در خاک اسرائیل و آمریکا مذاکره کنیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64977" target="_blank">📅 10:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64976">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
📰
نیویورک تایمز:  ایالات متحده و اسرائیل پیش از جنگ با ایران، طرحی را برای نصب محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، به عنوان رهبر جدید کشور مورد بحث قرار دادند. احمدی‌نژاد گزارشا در مورد این طرح مشورت شده بود، اما پس از اینکه در حمله‌ای اسرائیلی به خانه‌اش…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64976" target="_blank">📅 09:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64975">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دموکرات های احمق برای بار nام خواستن جنگ رو متوقف کنن که بازهم رای نیاوردن  @News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64975" target="_blank">📅 08:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64974">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkl2blFf040waMHPNRax8DfwLroFj6NTiYbR_jKrnHrafDJ-t11Fix5lp84BQtsnrAipzOSE9Qx9Qj4_TSrJjHzsfW-KZ4jKsDXIm1waxEX4vyG7W3pAAvlBnANMBGFx1d7TEnjANpS3L9CCipHwLOM1TF3Bq0rgwL5ZrNWcG6iiOYTLOMNbFBgebhd2OcioV2UatZT907HdqBNRnW-MMfSg-t3s8KzjnsEv6rs0QM8sANhhMGd-uIPzOpByhKOEfRzBfk9F2cGmJmAbfxPq9lQVJuswTXs1Ftee7NhRPexQcgxQtJuSHfuoepngI_vt_2h8dVWodNaKOU193R3KtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور لیندسی گراهام:
امیدوارم و انتظار هم دارم بعد از این چند ماه مذاکره با ایرانی‌ها، دولت ترامپ هر تلاشی رو که برای دوباره کش دادن مذاکراته رد کنه.
این رژیم ماه‌ها وقت داشت به توافق برسه، ولی به نظرم واضحه دارن بازی درمیارن
من ترجیح خودم راه‌حل دیپلماتیک هست، ولی قدیمی‌ترین ترفند ایران همیشه این بوده؛ امروز و فردا کردن، کش دادن، کش دادن، کش دادن
در مورد هر توافقی هم، منتظرم بره سنا و اونجا بررسیش کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64974" target="_blank">📅 07:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64973">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5Oo0VfsIswHlg2zrbO4J0dxXl9lnrRI3ULw46brsYmmwnKPQq3MQH4U5g3h-nHaz3zey9GucN4bdUaCknMZkabp0GEz7wDefYA8sGYI-yTH0G7513qRe8KXYWEVL4MXjyjCTDHNxUj54pHS5kwo2_LraPL77m1i-2x4uBwnEpuVjms7byvQoQhT3qcy7O7il1aez3r-ccV4CjS7GIu19ZeZyOCWfgkOsIvbrK8EYMe-frFB6_ywjOUCc309D6RDqiIE-poQQsDOvEYKvpYRudANuq69rmNNV_pxzTBjlFqOwMzvznlMWPYGFrMiRrce4m32vYU7T38pWwMYrJXUKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غریب‌آبادی، معاون وزیر امورخارجه:
امریکا میگه دستور حمله رو به طور موقت لغو کرده و در سایه تهدید می‌خواد مذاکره کنه
اونا باید اینو بدونن برای ما، تسلیم معنایی ندارد؛ یا پیروز می‌شویم یا شهید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64973" target="_blank">📅 00:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64972">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🇺🇸
اولین اظهار نظر متفاوت امریکا نسبت به حمله انجام شده به مدرسه میناب و جان باختن کودکان این مدرسه:  برد کوپر، فرمانده سنتکام: ایالات متحده عمدا به غیرنظامیان حمله نمی‌کند. مردم ایران دشمن ما نیستند. سپاه پاسداران انقلاب اسلامی در این مورد دشمن است. تحقیقات…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64972" target="_blank">📅 23:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64971">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b854a8a43b.mp4?token=h1YBOO8huo9xbCH0eJu0xIo4_X8D4oQ5AfajrRx05b6ydXKugfL4bkFnsxxsyref42Lpnv-pukM1VEzUhmq_rEC2-3cIWoGZm5W-0iuVOJdtUIpPb47hp1zag-Zqs-cAzx7fyBlLqmxhXIyT4PP-X4pE52G1qJzSQBFKCapXoo0Rw-tEE0Ktrw4bfoxftLiEJWzJEco_iD1GO-RCPRWYrDCDW_j_8MRhTx6OdVihEV8srZ8T6pH-rYiwL1bwsXQv0kslf__M5xPBrNu1ibjRY7IeHMdhnTsHkJP5nNWfJj7uWNOvDXMlgIAr8nktJs8UJmWjE5TOVLi58Dn3rdT_Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b854a8a43b.mp4?token=h1YBOO8huo9xbCH0eJu0xIo4_X8D4oQ5AfajrRx05b6ydXKugfL4bkFnsxxsyref42Lpnv-pukM1VEzUhmq_rEC2-3cIWoGZm5W-0iuVOJdtUIpPb47hp1zag-Zqs-cAzx7fyBlLqmxhXIyT4PP-X4pE52G1qJzSQBFKCapXoo0Rw-tEE0Ktrw4bfoxftLiEJWzJEco_iD1GO-RCPRWYrDCDW_j_8MRhTx6OdVihEV8srZ8T6pH-rYiwL1bwsXQv0kslf__M5xPBrNu1ibjRY7IeHMdhnTsHkJP5nNWfJj7uWNOvDXMlgIAr8nktJs8UJmWjE5TOVLi58Dn3rdT_Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جی‌دی ونس، معاون رئیس جمهوری ترامپ:
گاهی اوقات کاملاً مشخص نیست که موضع مذاکره‌ای تیم ایرانی چیست.
گاهی اوقات سخت است دقیقاً بفهمیم ایرانی‌ها می‌خواهند از مذاکرات چه چیزی به دست آورند.
در حال حاضر برنامه‌ای برای تصاحب اورانیوم غنی‌شده ایران توسط روسیه نداریم. این هرگز برنامه ما نبوده است.
نمی‌دانم گزارش‌ها درباره این موضوع از کجا آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64971" target="_blank">📅 23:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64970">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64970" target="_blank">📅 23:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64969">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=XqwxTQf9jLOmcxGdAjCFnrBsTCnjRW5VeF7gEAjvX-BE1N2Ty1pme4sFQAORmI_VRX-20BnZCi0HklCAgXgAOUohMEbEy2r1ciePxhO8L29hIDXDTadM1LvXMfW_TE-GelD95fRe_y06GZ8ZRBZQiwpzOQWekw4zaMrjeU5Fn84pP2XYEN8K98OaGbXaQ3kghD1--wiLRU0SRGS-qEpYyWaeD9i2QJCUCSjQTKjn3Cwl6K-ej5QNkpvldOh7DNsIEuMfWlvAFuipCS7ZM_RzjEjFZ1efruaZw2pwzu9iWwmdM1ozA_FPLGLGDYe98Ao8nRMd1HoZRSHRwPTeY-D8sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=XqwxTQf9jLOmcxGdAjCFnrBsTCnjRW5VeF7gEAjvX-BE1N2Ty1pme4sFQAORmI_VRX-20BnZCi0HklCAgXgAOUohMEbEy2r1ciePxhO8L29hIDXDTadM1LvXMfW_TE-GelD95fRe_y06GZ8ZRBZQiwpzOQWekw4zaMrjeU5Fn84pP2XYEN8K98OaGbXaQ3kghD1--wiLRU0SRGS-qEpYyWaeD9i2QJCUCSjQTKjn3Cwl6K-ej5QNkpvldOh7DNsIEuMfWlvAFuipCS7ZM_RzjEjFZ1efruaZw2pwzu9iWwmdM1ozA_FPLGLGDYe98Ao8nRMd1HoZRSHRwPTeY-D8sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره اینکه ایران چقدر وقت داره تا توافق کنه:
دو یا سه روز. شاید جمعه، شنبه، یکشنبه. شاید اوایل هفته آینده. یک بازه زمانی محدود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64969" target="_blank">📅 18:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64968">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2efb45471e.mp4?token=sTMG4UubWL4slbiWGUq39tcRczLbniSpmkwgNQrAp0JPrdWgL74qdAWM2Zy8vRa92t-2B4oElysYYysrpI__2EDMBpXM_AJgt-ii9TtrJl_8ntvlbZQlcFmzQUtOjmkzKcNE6m03WAPPdrOpqJoASdEjbw_Ws2P886qU4X1AG4UIapoipR4EZqDyRasCH_A5Hn5wHH2mhRTs0LD1eSetw9G_Q_csjoSKo7c2ndTGVO-cLA1jzP3_Rp-SBusPHLwyRwCuAmZOZ94yFU_ijyWV7FpObmV9Ypybt6S_6Vr22TlQJ23W70I_zNi_KAqTz4EmQwk3Z7lz9LWXIBlorKGfaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2efb45471e.mp4?token=sTMG4UubWL4slbiWGUq39tcRczLbniSpmkwgNQrAp0JPrdWgL74qdAWM2Zy8vRa92t-2B4oElysYYysrpI__2EDMBpXM_AJgt-ii9TtrJl_8ntvlbZQlcFmzQUtOjmkzKcNE6m03WAPPdrOpqJoASdEjbw_Ws2P886qU4X1AG4UIapoipR4EZqDyRasCH_A5Hn5wHH2mhRTs0LD1eSetw9G_Q_csjoSKo7c2ndTGVO-cLA1jzP3_Rp-SBusPHLwyRwCuAmZOZ94yFU_ijyWV7FpObmV9Ypybt6S_6Vr22TlQJ23W70I_zNi_KAqTz4EmQwk3Z7lz9LWXIBlorKGfaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: دیروز چقدر به حمله به ایران نزدیک بودید؟
🇺🇸
ترامپ: یک ساعت فاصله داشتم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64968" target="_blank">📅 18:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64967">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:  ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم. خیلی زود خواهید فهمید.  @News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64967" target="_blank">📅 18:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64966">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9954bd7931.mp4?token=tWgn_LpbhZvqjw57yac-XxrGqtITkoOeXjqw1z6N5I_qoeb2lR0cWr1nb9I5TPq39bl6yCmYdaKghHEVRX723IyyvCZTMBKdWX-g60nf-IB3kj94ZbpiZWLMz0gLj_LU-CzqyGJPDyYycIIQQWhQlvf8DkUc87yAigBYuSwiSAECOvNgvIug9GsufuOC6fnH8lLLYZwZsuvITY2u263DJLsQTAhw4HYEbbtlQesKPlhDnSOZlYyfIlfPAhiIJaSFzhhF5iXxHpLmuo3molxZMyOQEoQEN37RJ_pb1AV8MFdcGWmBzMq92N2WMh8FLPjWIe8DNdDIPxgaSFlQcQgZ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9954bd7931.mp4?token=tWgn_LpbhZvqjw57yac-XxrGqtITkoOeXjqw1z6N5I_qoeb2lR0cWr1nb9I5TPq39bl6yCmYdaKghHEVRX723IyyvCZTMBKdWX-g60nf-IB3kj94ZbpiZWLMz0gLj_LU-CzqyGJPDyYycIIQQWhQlvf8DkUc87yAigBYuSwiSAECOvNgvIug9GsufuOC6fnH8lLLYZwZsuvITY2u263DJLsQTAhw4HYEbbtlQesKPlhDnSOZlYyfIlfPAhiIJaSFzhhF5iXxHpLmuo3molxZMyOQEoQEN37RJ_pb1AV8MFdcGWmBzMq92N2WMh8FLPjWIe8DNdDIPxgaSFlQcQgZ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم.
خیلی زود خواهید فهمید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64966" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64965">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=FPG04h_FT0AeAJcE9aNQanoqGDIyioiSw3Vx_KWvJqKws5fCMh6Myn01AutDB-PHCK2kwPYgEHu8C88hdzxyFuZjurH0yCiiPV4QacHZYHujKPqkY_wazJFRU8EnYLx55G6Hnew5xt4rqaSfprCrBsVtQXBwK90Rfc0W10nocmDk3Tr6Kiwtot1_tJ88eVhUqqweO_j4sYpEVASwMCFafQXK2kwVhKcPg_4Wd9MkrAsxHZs41P-y70hBc2_vE_SodiS-d-6O1gNKmySkRCQD_rzkt9xTKJnS5tLoz_m5ktyL0VZ_W3tHwZ5QPxPs4ANmB18ctTNpY2d8RSjAzduC5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=FPG04h_FT0AeAJcE9aNQanoqGDIyioiSw3Vx_KWvJqKws5fCMh6Myn01AutDB-PHCK2kwPYgEHu8C88hdzxyFuZjurH0yCiiPV4QacHZYHujKPqkY_wazJFRU8EnYLx55G6Hnew5xt4rqaSfprCrBsVtQXBwK90Rfc0W10nocmDk3Tr6Kiwtot1_tJ88eVhUqqweO_j4sYpEVASwMCFafQXK2kwVhKcPg_4Wd9MkrAsxHZs41P-y70hBc2_vE_SodiS-d-6O1gNKmySkRCQD_rzkt9xTKJnS5tLoz_m5ktyL0VZ_W3tHwZ5QPxPs4ANmB18ctTNpY2d8RSjAzduC5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار طرفدران حکومت تو تجمعات شبانه: مرگ بر امارات!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64965" target="_blank">📅 15:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64964">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
خبرگزاری مهر: صدای انفجار ناشناخته در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64964" target="_blank">📅 14:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64963">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sy5SAhOxhheRyN3UstfwFZ6V6hnIGSexW8o3-oA0tQOH3h8oYi60zzSNL2eiesYLSNElHQgmzGD7yvHB5AQoyWk4z6LlFQt_sURD9_dmMLrktegb17EcrSIvBuvGO-a4BaEttkjfXe-aEKSgJlE_ySnhg51dM8N0_4BzSw5IlFEt5nf2F8M7JcRimUd4AuztJIuAb1H4LtR9eay52zerhyGFk-FzViz0kuTLINIP5JCWjDkPGWDul84-J3cM-eIcOO0Fw_M_bBLbZBTqGuhdsKqkDb1hOZHAmeysAgpfzeoqC9aMTgrd6iLrCC-7SKiSYggAtcUtr3YaIOWSNvSDpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:   من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/64963" target="_blank">📅 01:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64962">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuUhdOOVcemSxNX59xvEVdgaPzEGGjiUnSx2TwT-AFEGVyoX0zY_-HmWeokim9WJ7ttPnEhomEIapCX7xqwKAMxUm6gXeLpzuePQ956nIHDEz4NZLu0mVYKhtTykgYktsKdyUXgnN9NWlZa6KkwnJpsohqe_-pj3kS92uTaS_pnotozlllZYP1_znZDgnhqzeI4gPWka2mxSUVaV-_2eGtksUDlrDM1K-KIlLGIy_7PtV5l_IlmD-dbKWrpIlZouumH2je3zXR5z-8Uk251p3IhIyXHHMUmXwAJSwkzRP6-HKOAUNy4Dx8kYnC8ILpwgNsW-IXiJOvJFgntkPAO47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به سلاح هسته‌ای دست پیدا نکنه.
با توجه به احترامم به این رهبران، به ارتش آمریکا دستور دادم فعلاً حمله انجام نشه، اما همزمان آماده‌باش کامل هستیم که اگه توافقی به نتیجه نرسه، در هر لحظه یه حمله گسترده رو شروع کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64962" target="_blank">📅 22:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64961">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S35OlibETQkMvUtQ8Kd8dzyJPKxubn0Jhxs_VaZ2xf1tscSqoEWAvhADXmzScwXauSMNcxX7v9lIiAWPWfqL3Zzxaq2K-IZt5AnGKESpyCTYh5-Ye89GSvneR2uv9TotYHO7m7gIyjN28iVGA0sBjNGpr4baqoxmMsYhLDs1Hn4Sr3mWTOALGJgKr1CdcSj3i_tufIjc5XvMs_2s3r3yHbF2rlmIrfK7BxDl9rou-6ZuRHmNwfSXF4TBqAPljjrTM45Fk0o1DweuZsMiN2ArMKlYNSOmSgE1vzK2SVCWdNQlK-EhLDNo_vW0oZGTHf9YbGHw6iwMtjPW4m2f9DpQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
«اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» در حالی که پرچم سفید نماینده را به شدت تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌شان همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی بزرگ و باشکوه ایالات متحده آمریکا بپذیرند، روزنامه‌های در حال سقوط نیویورک تایمز، وال استریت ژورنال چین (WSJ!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و همه اعضای دیگر رسانه‌های خبری جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است، حتی نزدیک هم نبود. دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آنها کاملاً دیوانه شده‌اند!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/64961" target="_blank">📅 18:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64959">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h83WFuBXtwOzReL5ttnUCRHIp1AxUyTpdEzlM650FGOH0BqPeGi8qNmeE5EH2Xxkza5QfEoKrbby7ag7Ac575hQusJtiJA4EWzxrgnINVwtHn7mh9Vjr-X7UH4RDy7qe1rjbFwBLo6Ns_iPjykaur3sQXj2MT_jBTzc2cW5GWKSgmI1BFytWW5ztEiI8R0QvU7T_Gnstn_0Cqi5s8go9KHBRh487pZBVJNNOO1LjfKEYJNxxiS4owoSN4TioZl0JeieiexAqDzXEXty-fm_CEHh-2mDafrHWgeOEVSXj5UInHXTQz9VgwZRTsWBSwAcVd6WG19lh6EOnHpRjTpHeGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F_OiyJAKbQKbtOS3LBRswLpEMUiqEmNMaWXf3fHFukIeG7_HopCJEFKsJ-eZ5s_m4e1dbmgMPjFRnqCOkNBoOiJXHBTAT4oJP5_7o9cb04P5zn8b67yvv1rnywfU5XP7nU2o0RZmjctpiFExIPck7TGhVNmMbLuJcmtqJCc7-9pzCoCESt2jA5mFT6_ls15GnIRCTdHczcFd1UZYBg8wQt5fscrY5bAydVlrWBVgZIOUpTk-EeFUVQvUiR5R3RGhsWfoaL2KrE-6J7fF7e2oPfrnRf83Hn6f4R7AeX8hPAa3Pvp3YAsYM5nhjS_tJXiifxc-LAaWAsveK7QNKauGbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت خودرو ، ۲۸ اردیبهشت‌ماه ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64959" target="_blank">📅 14:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64952">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/euCGL67xgnCVU_fc0RqaBZpq-7x19akgqz4ccu98PJOMfdPhioIsTLEyUuD9ihp-BAUwYUnzZ9NrVaS1glasj3If9EWZlK_Gol0kznhZFAV8r-e8e_oDTe3X_ht63QaR5nXFPUQPvoQi03uyAA7MMx7tE0IWHHXhNLaeLDYFlLkvivpp_fICM9B8xQvq6oS7NmozNXcdkVQ2qVnGtFyjPPj8_QfuNUlwEiLdiua8-3MczOpR3fwskybbvlJ8yIe_4InNxZhRtmC-2zXA0zlmk63HutAzQeV0dfENtBwd1yBEsJzpJ2zPpE3SqhmMpw3gniTEOKBC5-5UslFsz1SCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EFhVS_AYZsbhIA1wUGY7bwT7UUJGkvg43drGJcEn5phUAHwkQUlnGTngj3-iz-hXJDvTLWRNVjPLtGDUD6dqjeSerLYFN_23AWcmlVO8Lxug8zZVLiNGXRBixynxYSGsRNYuA3MVqFQMKcN_E63dyRKmsd6WOR48hWMPwGUrxVlIvdJVh59zZobCxuVowdupyx323cQiEeackJUBlPoHTYWUeZ2F-VC1ufSMO1HZBkCUV_-jxLoqwOtMPcBFRLOkx4uNHwQ025XJXbGd9Gywo_IVvBRgmFf8UtpUajWhTCsjfaXzGAteCYlbni74Qcl-fQrAKtjtqnKBBZe_MLfBGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SWsk5MF6QljZWP7n3PrtutD96XJ9L8uggicPThCC-DR26Bq8uQLQ13DELquxrodlRvqamk-f8vi75qRHyA0eCJ1C0owD1qNzdxuJsCirXPYATewil-vJssVQofxb_uzYg-MEft6fuHsZYjymxX1mueBYJO6WDUIYG2BsQSju4xkKJzad1QpmQSqTt0Pcfb0o_rNK7DvznyM_se2YkKbBIN8wwVr_Vwz3qk7fh7bc-qdV67wrnhNIJjrMteRKZm298szhDmxoqsjsWMSfy1UQgugbzEvAz_MzFHWmApV6Rioo_UzkiiliocCdfXrRHCDwajKJ4IS21v06vp_YAggQbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AYrunp9cvsPLLvQ8RC7f7Rt-sMWoMn-J0gM9bh4-WzS0VJd3xkRAgy4zyqfl8gDtMi347SAccyY9uogX6HJesEk6dSDTYObFsx_1klWaT5DM_wimj7uQjLxRoYSVe847m-n9aB-MZmcv7DOrfoo_0NVWKpYKN_fmqpxE5QikvBOXxbtiZMrv7Fp5ULgGuL3T_fFMgu8g65z6sCczCeQ7wxJ8qoFZUHUXfi8rqT8v2FejEIRMVwh5sMptpkeEzfAtKRW0tym5iTTWBzi2o-6PkKhHfiunSobqlXTkbEsEzdY_7bH_BiMgsZdpMMx2GhVLwOkZl86jZ3BDGWuL5fDcuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cYxCEZ8awR3UMUjx1if1ojS2Bxh8dQgCFE5Yh3-XeQjvB3Brhi105OOeyH021uz8eRjT33T_zoV9GhD-v--yRgBTPdnqik77ZpUc--D-cR_iJyrS6F_c0zh5au2ugYjh8czDvdeP6lYwOaJeDHLXSSor_7KxBYVWrV9LtYPDfJQtuD5K76a6Ye0qZMDCPkHsxcosxLDZ6otns3O_QVzrhA8CEfxZRMeaFf7nELpJ1qZ4qbpj06O2lFvdYa_g__kSPC8gTQf_VsQCfVJYu9_UpmiqjsnGncyd7Mv5_iEVQYqVvgpVwfg0q8yN6c1hffAUDAKOjHovaiwTK8vclGSaaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g5CZGuUs4CeOCEbldJPoArCnYo1EdVQ5ASFP8T6D595RLnaCaHEt0y8SHeT86nFOb0tjI7xu-1O-cuZ2J8iDQehHZdHnS3MRSu3PoqGZFW80fnvrnQYSR4Zav6ul6IpE2WbDRpIa3uGSiE1kKwE1Q64-twtwycT2F1idsRriLoJmFXTDwtvmVbhrQqDZKKu1meHn4Lj0t6I30OQXJYabVfdVoZ6AfXePmyCqn-cSy6osvn-JzqpwJ8Dm4UM39fdcV_nqvtHEOJ9MSoLlTk6kMKNK0o9O1saQoCqLuZ7kRGm5iEFtCyJdgOfEWvjvBS0izsVMDr2zFYseQis1HCfgFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V6vt2yWbjwVKef1cqHplm4tuv3tonX9Ze_DmiK8lyz4xxzrTKSyrywpoF-eYeWr9XSxjcKQAJ7dmS7s74ucJcFh1qGpwv61VAF-P-8pYMbKYuu4W1VcEjU3fwm0S9X3zcFpDKDTmvH_NVCSPerrmLm_BUSg-7Uu_ukZ5KNArdZABewRHPGFov6H7xlVniLewt7x5fFsINN3yJC7Dw_2MbDBXw_vPyk6Inn9B-4LamGZVWWX8rWOGYCJA3aB5WGMqzYscGc5IvJ2HuxMUYvlnyrAWoydqhu_LpYz-CaOk09zV6brIJHxLqcQIQI14V9STNPAHEWCyj6VPqUzFCuJyhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
پست های دیشب ترامپ دلقک که با هوش مصنوعی ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64952" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64951">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r--VwQCdosOUofvng6-r2ubtzH31KVIDcqsTALI8y0YUysKdxe10ga7yTdbtwZFktFq7FVWeJZeIsbFIAkOxMH0zHiqolfvGPf_hRn__jKb05r9_rL4P8UiIJFPw8LezdXPYGmy6mQb_ie1fNwbeJfzXz9UwYIe2hpovNCwq8F2Jq6HAwZUbToRprLEUeK5O2TZPGD-lDCDrr7V2U6f8vjEv6Egi41BFnIziPkrFUUCYM1YJMjGxNFkGDIjv6F4S9L2IaIpvNzqs9zCe85edWuDidc2hATq475LTAjh3ZHXuQDS_h-RxlZLxTDPQeeQIABI9BHPapKer52ynL1vbSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست عجیب حسین دهباشی سازنده ویدئو تبلیغاتی حسن روحانی تو انتخابات ۱۳۹۶:
حملات و ترورهای دشمن تا رهبری حسن روحانی ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64951" target="_blank">📅 10:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64950">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fDSXFSuJfjG8ACDKulCtDj6VD2sNKIjwXSgGQwe-GLwIUR3uwcCagCDAV_8ttBLMyt6R8JX-FtEBHkUKx4R0o-bIKraXAywoHOXFFURAu1XlshjkoeXzeEcVkijyMcoieZvx8MenW04a91uubXyXkyueJeTXYhWsrY5p6DiSDs6K4pik7X9d9aq1zQtK0lp_3ltdmxqe5lL9GwxpbKDU4iNpUMjCF8FgcAkQlSm2fYmP0Naix2Sn02dXeTKLvzZQpyupWUJCyV78VI6M0x0qV3usm5VP01VSpmvQzb_VeFVft7nVJmN60mHnOkdyFZShhtCoFipVSBzaRaYbwNQI2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در شبکه اجتماعی که فیلتر شده
روز ارتباطاتی که قطع شده رو تبریک گفت
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64950" target="_blank">📅 21:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64949">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNPG6QBwIAjQBiFldVa75OgS6B43ALBVy-Jf9qcg5Vfjc9-yOb6VKEQ2MhalTZOTO6X8ITOwNr29HKZmqnsAkWdEG84KfKpcxoePMLkW_Ev-wqV6Z8I9wJr79Ie8rEaFx1uns3mpVhMwEs01joDM1PH1cGZpmSr-EK97CU_TcOgOOk22ZmygT-Ojl_w7qvzhtYLlKfCAJGi7CEfhEisf_M7qG_-Cczf5SNoQnuoVbmJHnMFUU-iju7BJ03NOomwgnx7UCEr-4ZJq0SV-9GMLWHOqUANv3WbtLRk1NwAEAdcZjUJsyb9s37uKc2uULQsZRtyaQE6C69nPr6IxqgilQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64949" target="_blank">📅 21:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64948">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=J_x8xEi_caXjL12yZQGUpWBCeUWHLhX3QZCkGKIP9rziQFNYWgMPrEmF_miTmf4McfjkfbHVyVe7Q-ngIi-lkshoQ4XIBuPsbMu2VSazIGdXTlFyXa0sQE9fEY2x2URBPcjceDVUnpXqVJzDz43sLFcdJEZ4WlFo9521Ro4PLi6hSGkQf-6nDR48IHKWlX0FrStLAKbzKvfbC02JL9kn08PFSvnMLsRP-_TXWadmUQAmMLTq3AEJuUdl3JN8SrXIG5MNYSSWw-MHhmz5MMks8s0nRguJZmFdY8TDuzZz48Oq182FMWyVoeW5YoGMxq8yWv2EuC_9MaNdW6Z3wO4mfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=J_x8xEi_caXjL12yZQGUpWBCeUWHLhX3QZCkGKIP9rziQFNYWgMPrEmF_miTmf4McfjkfbHVyVe7Q-ngIi-lkshoQ4XIBuPsbMu2VSazIGdXTlFyXa0sQE9fEY2x2URBPcjceDVUnpXqVJzDz43sLFcdJEZ4WlFo9521Ro4PLi6hSGkQf-6nDR48IHKWlX0FrStLAKbzKvfbC02JL9kn08PFSvnMLsRP-_TXWadmUQAmMLTq3AEJuUdl3JN8SrXIG5MNYSSWw-MHhmz5MMks8s0nRguJZmFdY8TDuzZz48Oq182FMWyVoeW5YoGMxq8yWv2EuC_9MaNdW6Z3wO4mfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
بر اساس تحلیل من، هیچ چیزی نشان نمی‌دهد که افرادی که اکنون در قدرت هستند با قبل متفاوت باشند
آنها هنوز هم می‌خواهند جهان را ترور کنند، اسرائیل را نابود کنند و به ما حمله کنند.
هر قیمتی که لازم باشد بپردازیم، خواهیم پرداخت.
چرچیل چه گفت؟ «هر قیمتی که لازم باشد برای شکست هیتلر بپردازیم، خواهیم پرداخت.»
همین موضوع درباره ایران هم صدق می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64948" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64947">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یک سری کانفیگ فروش طی یک حرکت بی‌شرفانه برا سرور هاشون ضریب گذاشتن، یعنی شما ۱۰۰ مگابیت مصرف می‌کنید ولی حجم مصرفی ضربدر یک عدد می‌شه، حالا ۲ یا ۳ یا هر عدد دیگه‌ای  اگه این حرکت کصشرتونو جمع نکنید تک تک اسم می‌برم تا نه آبرویی بمونه نه مشتری‌ای @News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64947" target="_blank">📅 19:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64946">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تسنیم: ممباقر گذاشتیم نماینده ویژه جمهوری اسلامی تو امور چین
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64946" target="_blank">📅 12:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64945">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=POEgWcqU8n56JIS8AkEMm1AtTtRsiDIVrK9P5UN5l5r1KEatZDh-ncnOJ4MGsOq_Z2Zko9AkAQVxDguiwo15mo0OqMgiY1TOPE9LesfBpmS-J5NyaX_taQhqNiBmpy_cuImkivUdtgG_msQaC4qGQoLY173BYacaLF73YsEIKbWRiJ-vdQPRWIO_L7ZJOQ-6sNDLOLJdTl1mm0LFXoLIlVfZY6KcxzfXF3ebfSI_vr8s18b_8ZuBxZrXxy6HYsJFZ8V1VG__-eD8wSH1zcvSjYdr62A5LY3ODC50R2hLhT0QfNQPRU9VHn8_ad0eQZb6YtahAodMxkI7S_Yhp6HHvw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=POEgWcqU8n56JIS8AkEMm1AtTtRsiDIVrK9P5UN5l5r1KEatZDh-ncnOJ4MGsOq_Z2Zko9AkAQVxDguiwo15mo0OqMgiY1TOPE9LesfBpmS-J5NyaX_taQhqNiBmpy_cuImkivUdtgG_msQaC4qGQoLY173BYacaLF73YsEIKbWRiJ-vdQPRWIO_L7ZJOQ-6sNDLOLJdTl1mm0LFXoLIlVfZY6KcxzfXF3ebfSI_vr8s18b_8ZuBxZrXxy6HYsJFZ8V1VG__-eD8wSH1zcvSjYdr62A5LY3ODC50R2hLhT0QfNQPRU9VHn8_ad0eQZb6YtahAodMxkI7S_Yhp6HHvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
‏
حدادعادل: والا من خودم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/64945" target="_blank">📅 10:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64944">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/IFldfXkwSFsU1HIjUF7Jq5noKStkd3ZeGA4qVwcVUTTNGvij5Q8BkRQB-7BiWFhl5pW-BXtTF4APnM3UHFmFCTi1iM2un7_aB-MzYLDyEE0YMYvho3ojXhQ8tte0x8uWaE8Kcntd6tZGvLtsN6vk_72Qzgd2TFBVN_Z8XRi0CZ6LwFdlqAYLHMEAuT4OCj3PkumRo6y1XjIFBmPsnurFLLDQWVRsUTZIwCVpOmZCC2CaSZQWKu7pYbhDeH75GQLL378pqGpg6jEhmAABhwOPCCbBP-I5AhCf2zB4kwICaiG5zh-0_mbCtWAO8iiLNBeg4HhXi7upcPrh0lMrf3QxnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیلی‌میل: کیر میخواد از نخست‌وزیری انگلیس استعفا بده
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/64944" target="_blank">📅 07:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64943">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqYWqE6Nnub0bDWPrzHOFyUZlWEAld-POaLse1cKWD7mVRZbOVfMgVfWtc2j5bOwBU8N0ASHs2k3MsyCVfl3zk1t53OeO9A2ZDj4ZvSW2yAMbJ3K7jzBl7zYXR3UQFAKdt61IZjfci0-SLQaF_8_REAqfnWr_bBeqCCgNCIsTyVyiG-ZCPTEmmUdL_u5DNYZG-vBwmxLrKCco2OE8gs4DK-2hmg_ydZ222q4dcBc9Tq6vIkb4MG_XLsANOvdRNzoyhUtPerW42JxmIaaqeHypeJ40ue8oNasR-l10FLRNgUMGdt1lJYeo0jLY2IvoENQgaKuip2lDtGHmRODYAdlvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در سوشال تروث: «این آرامشِ پیش از طوفان بود»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64943" target="_blank">📅 00:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64942">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مثل اینکه شمال کشور زلزله‌ی نسبتاً شدیدی اومده، مراقب پس‌لرزه هاش باشید
❤️
‌
#hjAly</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/64942" target="_blank">📅 20:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64940">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ahTvj1TBQrIyjRjX2aCo2Fk2iTPUeoUO5CLNgAxC2EjhIoiNQZ0fFx0y13-9t182jTz6gY_XfQ7h-l06LbaCNS2DFthjWejZ4-CrUwXqNg9XpKzR6qCvwFBH_pTOijAm0Ca0qGCo7933ZRo2KvKXQGrpjRoklkQ9vnTuTn-h_VKey22KeTkcYedUgL1h4sCt9NPE2PZusyrjKG4NHohqWyAiPxRRQlgj-cK5PB_G2IQKRqKZfNAzkBbkt94BQs6hLtDEV_xDKJQ6x1IywRhBzwLsiQP0H8vIxNmqx4G1iqybPG-FWTiMQmNu40ZEmM4Vi43maS6Wzdx_JzTLtcNWVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=CSTKY90B754I9Sh1D4y3UBIggNzZbeESJFJN-x7nJLDQtBLYQaxPMpqbfal0R9cpOJJVoUO2_wxiQUKT88mMye7k843yPgofuQHPPOthpA0BL5r-bwT7pRydjDre-c-y-c9stkLhzYrnkMJa-pqx1sOXZtPLHzzDJDVbTHkehRUsFxwFLWM0eMEGYI1WDAwBV4Df0jN9-vsQriTLzXymQiMwDuPYzsVIGkt_V1CxgPZkN09kqoJ1QM31_D7wxUwexhrdR-a_ylXCdqTijO6UPJQ7hSgU1FTNJ1zeqSyvmzHfJb_3PJAvAaUYcsAefnak1c1YTcyt9YPgfuniLfxqNg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=CSTKY90B754I9Sh1D4y3UBIggNzZbeESJFJN-x7nJLDQtBLYQaxPMpqbfal0R9cpOJJVoUO2_wxiQUKT88mMye7k843yPgofuQHPPOthpA0BL5r-bwT7pRydjDre-c-y-c9stkLhzYrnkMJa-pqx1sOXZtPLHzzDJDVbTHkehRUsFxwFLWM0eMEGYI1WDAwBV4Df0jN9-vsQriTLzXymQiMwDuPYzsVIGkt_V1CxgPZkN09kqoJ1QM31_D7wxUwexhrdR-a_ylXCdqTijO6UPJQ7hSgU1FTNJ1zeqSyvmzHfJb_3PJAvAaUYcsAefnak1c1YTcyt9YPgfuniLfxqNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند طرفدار فلسطین از برج ایفل بالا رفتند و پرچم فلسطین را از طبقه اول آن آویزان کردند
شش نفر از این افراد توسط پلیس دستگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/64940" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64939">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZmI8JQB4SSkZx53r6gc3CGzuFa-hGCcXZPZvHPngMJ5SLrUHCBThp80VmACrZ_Tw3hXwDzGIv9mqtLZWsTxPH775PSl2adL92ac8o-ZnAe5BdJRKz_KH4bcUCewBBDF9MS7SeftLBUloi4jNmWHR6R3NMLzK9xnt0d8udISqvE5TQ9oFiwltM-tlqdc0dSZZwLTTdZrtflsG33mAoVLtwYvo0PZsE5HMq4TxCmza3X8X6JjJ2BPMIhsymGaiEv9kOf8U4MyK-MHUMpUsn9URoFjuUKjw61hogxQ_50gp4ED4Ll5Go321KdbO1XtriRe9tSCpKLF4_Z3W_pqQ9Nc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست ترامپ در تروث‌سوشال:
بازی نداریم! تماشا کن قراره بعدش تو موضع مورد علاقت چه اتفاقی رخ میده!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/64939" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64938">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔥
🔥
آفر انفجاری امن‌نت
🔥
🔥
💥
گیگی ۱۷۵ تومن
🎁
۳۰٪ تخفیف خرید اول
کد:
AmnNet30
⏳
فقط تا پایان امشب
❗️
ظرفیت محدود
⚡️
اتصال پایدار | تحویل فوری
👇
برای خرید سریع کلیک کن
🤖
@Amnnet_admin_bot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/64938" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64936">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XexlXmfOF6HjGBxJFpZQpccIAdndTqrNgvHZbjdnbtp_EA4j7zuzlLYMaMG_DO29Thrm5yaAG5WteTX44e0lxfo3J0pLE3YTU9bnveg-XJkHQ9zQ9VzYyVtoCtwah6pUJzP_UiHhkv0sn_MaeMUXzSBJ-NoKPHHwpOQRwfAhRPs008hr4kQ7sB0kctzTaNlC5U4p8KzDJXBYyZ-Vbu-2JIHX0BGRpX4cIXchFxPP-fQJV21vo5y_yTatxOFmlVnMx-nJ2Xa-FTrIhpqAQg7jvxVOfRSDsTPTTIyphfFOhp8yI6dyI7-Z02uf_JaVmGRTGHIwD60a6S2covEGOuePnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/orQT_3w_nknhabFfsWfvo49DZCTyrjtlmrNc7tWSwin6QTQUjqfeBJKom_4VSGhrVBRknCyzqvP5vxpd7AOUMuNnLZVTWQhC8xHEFrGwG2m6rZkOyaCYEIx3dKLfpAo5m-t9IhZ-nbsdsRODoXCBWA_Z1ReIgx_sSgfPmcMG62ln4Ju06OdzDgHOeMcyI6v7Do-WbyD6TOfVeEWJwGJJHClNyTlOz9ei1GAih3yqJCCn96kkZeTuJLzaoreWDWpUv7_I9NITMIrlT14gWoWEmS_5moX7EWbd2Yz_0W3j9QGVEes33MgEw4aUbbpqvp4hdfo8e-YMLtYAReBH41oM1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیکتاتور‌ها مثل هم رفتار می‌کنند
دیکتاتور ها مثل هم سقوط می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/64936" target="_blank">📅 10:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64935">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل گزارش داد که در اسرائیل برآورد می‌شود دونالد ترامپ در ۲۴ ساعت آینده درباره اقدام نظامی علیه جمهوری اسلامی تصمیم بگیرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64935" target="_blank">📅 10:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64934">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عه امروز واقعاً روز پسره؟ روزمون مبارک
🕺
#hjAly
‌</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64934" target="_blank">📅 10:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64933">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUCjs9peVatGdUFWlX3gFwvldRfKdmKo0J_tTJUSX7eWDIlnpCHiW9je9MAHJyaEdVDKyZE-Ft4nyKU8oP7LewshcsKUkT5Uu1sdEAtaKesGhaEfSu-wZ2NlyXGCHvq0mQjIg7C4SR7MxhiPexleRX-OCzJfjq7dqFDhfVrCvCBx8TgE1HkZ0KfdkhbxZRmKjlFkG4zfwt996WtAcnJv8XE8BYL8faWOOOKMUIIA1c_7i8s6uDqVV92FMoMq68u_Xftne4wy_1qZ5kiLeMAnvE-e2Rauzk3gSrUhvYjumf7-SgYLI0BbiFDgpA4x_5EwQeNV2Q1CNWqY3hW4fnc7LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزالدین حداد، رئیس شاخه نظامی حماس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/64933" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64932">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=GxNqBbouNzKhoE55EUU1Ri13jU7mZCavA1qkKal3Jtg3zrjPLCiqwrDf6kgA_C18F0wceU2yeapMm50ocHMKfprZxVRMK68LeHnyzuBAU7hr6XLApUS_imat_nB9qGMQDDq0PBpj4UOoaOrxVsIoVxYphjmG4ZDEOi8G9MAD_sOAgPyiAdiO-U8TQ-5PIR9jrn7E7mJPV_y9gkiD0wAhFUzrtrsbZM_4Uagm69cvy01Xx3KagecebcE9OWDfsLzRJOej0ShpR8qkBgH9URm1S1zfPjv-lJAF3eLnmZAhXtvN1z4kOPLJPkm8uOY-IEhF8BSgZxiuYy0uc4Gw4B5AJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=GxNqBbouNzKhoE55EUU1Ri13jU7mZCavA1qkKal3Jtg3zrjPLCiqwrDf6kgA_C18F0wceU2yeapMm50ocHMKfprZxVRMK68LeHnyzuBAU7hr6XLApUS_imat_nB9qGMQDDq0PBpj4UOoaOrxVsIoVxYphjmG4ZDEOi8G9MAD_sOAgPyiAdiO-U8TQ-5PIR9jrn7E7mJPV_y9gkiD0wAhFUzrtrsbZM_4Uagm69cvy01Xx3KagecebcE9OWDfsLzRJOej0ShpR8qkBgH9URm1S1zfPjv-lJAF3eLnmZAhXtvN1z4kOPLJPkm8uOY-IEhF8BSgZxiuYy0uc4Gw4B5AJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار
: آیا آخرین پیشنهاد ایران را رد کرده‌اید؟
🇺🇸
ترامپ:
نگاهش کردم، و اگر جمله اولش را دوست نداشته باشم، کلش را دور می‌اندازم.
🎙
خبرنگار
: جمله اول چه بود؟
🇺🇸
ترامپ:
یک جمله غیرقابل‌قبول. اگر آن‌ها بخواهند هر نوع برنامه هسته‌ای، به هر شکلی، داشته باشند، بقیه‌اش را اصلاً نمی‌خوانم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64932" target="_blank">📅 20:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64931">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
📱
👑
آی‌پی های جدید برای فیلترشکن شیر و خورشید
🛜
‌ ‌ ‌ همراه اول
2.22.250.149
23.58.193.140</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64931" target="_blank">📅 19:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64929">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">همه‌ی اعضاء هیأت آمریکایی قبل از اینکه سوار «ایر فورس وان» بشن و پکن رو ترک کنن، هر چی که از میزبان‌های چینی گرفته بودن [هدیه و یادگاری]، همش رو همون‌جا انداختن تو سطل زباله.
دلیل این کار احتمال جاسوسی بوده
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/64929" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64928">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnRju99jkwiED-Dsvb93LngmEt5ONLt4Xzi_3VGcagV1pMG_P3UeCW7GILA25Ygq0LQZAsZLIdQYpSxeU95-SOkKHnTgBwoL7FUIhL4xDn7-rBcxkLKOj9qbVmAYe_rRtfbKDzxRF9um-DyvuGE0SdBIAhfh3Ozxa8qnHjhor9_CMbqu3EZZ4V5uH_9oSYTwRNtY2W-YNu_UMmhyvkhnDgR2D8Vlb3UaEALP1ynJDXINke76da8IYmUfIUeSPz8WHeTACVUXpbpYATeFmXa6LK93iBG4PiXVc6a-DewKDxWIQ-EL6ocrCnJqXXFlDLJnoZNYmxTcjeJZPjwkIM2IaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/64928" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64927">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: تعلیق ۲۰ ساله‌ی غنی‌سازی باید یک تعهد واقعی باشد  @News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64927" target="_blank">📅 14:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64926">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم  @News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64926" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64925">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم
؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64925" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64924">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تنها هدف حاکمیت فعلی، رسیدن به اولین شرط هست و بقیه شرط بیشتر نمایشی هستند برای بستن دهان طرفداران، چون به خوبی ‌می‌دونند که ترامپ، اوباما نیست و تا زمان انجام توافق، قرار نیست تحریمی لغو شه یا اموال بلوک شده آزاد شه!  منتها ترامپ به خوبی برنامه‌ی جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64924" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64923">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
ایران از چند روز پیش منتظر پاسخ آمریکا به این پیشنهاد پنج‌بندی بوده، طراحان این پنج‌بند فرماندهان سپاه از جمله جعفر عزیزی با مدیریت احمد وحیدی و تایید مجتبی خامنه‌ای بودند، طبق گزارش خبرنگار ارشد الجزیره، تمامی این پنج بند توسط آمریکا رد شده!  جزئیات پیشنهاد…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64923" target="_blank">📅 13:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64921">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQZiGhSRwVXiHePYoEYYbftL5zTeGmobK-ayJkJV4xBmiXyeNltv7UsD-0T6q94aokUDTziymzvKjrwzAZ2bbzAezNPfjQbKtOSno8gJMDaQAekwuD7mA7v4sds9j45Kxm34_yJXLYPkMAXEQSe87_rSakMurxoD4l4RxWtK1XgU_Ae1eKh1Rg9SFBEgqPvTAeFQ957dFiBQBE6hPejs8pg-j0X3_TmAB8lJF8_tP0ne_ezPcixeBI-NUtENG_XP4X2vgRTupvYkn2xxhg-G8aY00cuEopmOlbcmLzUoj7Nos7JbEaQhaYmBWn2TSi7aheuzUy2sVzoPidoKY_EGKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mp8IVpw9QVAB8v8y2blUCvkvXWkKH-N1wLeFmuhn-poJo0rxtKXzbWpUa98_3tc3pIMQqkYgQRcnzge20Bozmo_NqZyLawzv06fgNb6dOAZmVLeT9zW3KLEGMH6SE9FCZ24BY_QLR0B8J3JA53NFLaQLN_KVxdM_mAln_xhbu1s5QplM8APR7Rjegq9uRYnV3zTXoE34W_TfZTGi4E_Jlvw-b23pTPjCRHYoo-T71HO-erIKEIhyd5cd7CDl65RnOAG61-7pdG6GqW-2d_GqbpKGOgo_lKTjBC-bdGWeP6zp41e6JtTyWT4oGptE5hLKjt1HsiUTyOpjLKUcvD1Mpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ الجزیره: پنج بند ایرانی ها توسط ترامپ بطور کامل رد شده‌اند، مجتبی خامنه‌ای دستور داده بود در صورت رد این پنج بند، دیگر وارد مذاکرات نشوند  @News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64921" target="_blank">📅 13:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64920">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHeDaLv1hPH_47wzjznXvRvJdJOpgFoFfdrJxKW-_36xj3ke1jpgg5ay_5A-vlTooB4Ban2C6uUBNNaTh2-mcRDIM3edvVd-1JAQSv2gsnAw_abZVLTNk4GUR1qoDEsPlmI7123E37noWXBGGWyViulTcfPf0ZSmOsz5pcnYYMXoqktk-LiyJi4JhSii4Il9rxVlZLt6moF6MwvOE7aTYBNKtUTa1IL_81iasrl6Lb-4_Jp9meB4qR7CtsoSDHBN6j8GB0uYC_0MSnvomwhvFOVfPnX1URao-RyfPEFtLKJdJi2fqDtQcPwgD5dPk4Li6f8Xb05R4Yjs2pdCod-xkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#فوری؛ علی‌هاشم خبرنگار ارشد الجزیره: یک منبع آگاه ایرانی به من گفت که تهران رسماً پاسخ آمریکا به پیشنهاد ایران را دریافت کرده است و واشنگتن شرایط ایران را به طور کامل رد کرده است  تیم مذاکره‌کننده ایران پنج شرط را که باید قبل از ورود به مذاکرات در مورد…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64920" target="_blank">📅 13:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64919">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇺🇸
ترامپ:  امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند. می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت. هر کاری…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/64919" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
