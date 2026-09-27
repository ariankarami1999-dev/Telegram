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
<img src="https://cdn4.telesco.pe/file/YvpQwkNQREldzQAtgSwaqaxZ0gsUzOaPoWmu8aVjFhNAhG6jP1scntY2wqig8F7UwjOfkCYu4CWvT_ImlWIy4P0wBIyBEEPSJ7aaTLL4XeWpEkypondiyRLSad2zLp4Ybhab23pmJRNZLf_s17lF7O5xKLepyiBthM-4yI0FqDNNwqVYGR5tdcs1whQNnJiqgdV2PKpxYbJ6oPf02PvGzosiv7RzHoOCJ0Lhjhry5Fu0qBCDXWOm0wX2CyL6SyAY23bK9imliDliotoDSo00Kq1awxipRiTfpGM2xyVqBjUcpPsHK-R2Qj5ILeh4KReqmpm01_7htFFE0bVrFcPJUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 10:52:38</div>
<hr>

<div class="tg-post" id="msg-149648">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lczCjFqzOiiHYLlxCTwbjgfOhvjQQJWRreTl6uz4UXm9UChRn3m3rjTJshYA-C2P6rAaITfMbXI2L3vLJ1HrHka9EBoMAOD-MrS345pTlaqJtgCwOEgv4yrBIzWuM3VmNsAZTjVldncybBHcN2MMY3TZfTKMgQjJKqiLxvwwVKpXippAkIphjP0XgrKN2Vfv5kwr5ew9u-ChVRiFjzt5emvXfdaiC_OVj2cvPbpTWJmhRb9yqGzC2RcgZG1by6eU09OXnNBMReDjuhKfIwkmOCupFTNBzDs6jcbs8OTxvsHg8rKjKPB0L5HWbtNqiPttgZf-f1vSwQ0rRgXVsaeMyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای اسرائیلی مناطقی در جنوب لبنان را هدف حملات هوایی، توپخانه‌ای و تیراندازی با مسلسل قرار دادند.
🔴
حملات هوایی: نبطیه الفوقا، میفدون و کفر تبنیت
🔴
گلوله‌باران توپخانه‌ای: وادی زبقین، منصوری، وادی السلوقی و حداثه
🔴
تیراندازی با مسلسل: بیت یاحون، صری‌بین و وادی زبقین
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/alonews/149648" target="_blank">📅 10:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149647">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/rSlVi7BNyRSvmt5F9Og5Dsd5kSJSnTwJ94dHiVlHqjYKlE_G6z7h8W9ngLrbKrwuKoccDTrNi7jevwUxV4w5k2pNRd1uMSRUL_oByq_jxtkr5jPUuqKCC7KPcLJwn25hutgY2KFqaLfGIOrQ3t2aJwC64ZOo20pz2iOdQRLN7kNzaopsgVI7YlN9TfMJAI73k7-BTRgfTelYUVgG0kkQZXMTVMZvP_8_TRuRrB0ArWvI-Rho8_9_quoEcZ5moK-oyQNlwCSiERKiAtBJ3oET4IV_dCWCJLFvFLPyNmwzOCYwNunwhLSndl_KpzxR_P6ImpKGoTVlOvzc-s0AVNDNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لهستان و لیتوانی در حال تدوین طرح‌های مشترک برای تخلیه گسترده غیرنظامیان از منطقه بالتیک در صورت وقوع حمله احتمالی روسیه هستند.
🔴
این طرح‌ها شامل رویه‌های اجرایی، لجستیک، زیرساخت‌ها و مسیرهای تخلیه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/149647" target="_blank">📅 10:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149646">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
تورم نقطه‌ای شهریور به ۸۳.۸ درصد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/149646" target="_blank">📅 10:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149645">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
توافق بغداد - واشنگتن با ازسرگیری ارسال محموله‌های دلاری به عراق
🔴
سخنگوی دولت عراق: بغداد با آمریکا به توافقی برای ازسرگیری ارسال محموله‌های نقدی دلار به عراق پس از چند ماه تعلیق دست یافته است که به تامین تقاضای داخلی این کشور برای ارز خارجی کمک می‌کند.
🔴
یک محموله جدید در روزهای آینده خواهد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/149645" target="_blank">📅 10:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149644">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
رویترز: با ورود طوفان شدید از سمت سواحل شمال شرقی به آمریکا که سبب بروز سیلاب و وزش بادهای سهمگین شده است، برق بیش از ۱۰۰ هزار واحد مسکونی و تجاری قطع گردید و بیش از ۴۰۰ پرواز فرودگاه‌های ایالات متحده لغو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/149644" target="_blank">📅 10:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149643">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fhOseeQ50tEmhV_E0pcVlmaz6i7qQLGUPKHIFRl0yfa-KERZaruWJSfEs2-a54chXy8prsM1AQ6FWDLoN9BfelATwNweDFtjjhGGNmxvrG8iIV-1qgn2wkoWElPb5CEZMQ7YoZDxYBeTkagNCquCchGIEs74QA3WLLK9QdJ4QgeFi6UgbQx-ouVQWvomyEz7jj2TMw8dKqP_wEMR0zQSyV1BzB0TUrOprWjc0k4KdMMWjKbqxnVTlBKfktc-bW6ydAboah6K7CVnGh7ta8iTUPVDgZ8y_OStNjtqyZQVVFXCB06bRDb4JE6V0ZLlsP2eHEnVKgJ0R1_ovIAgfU-TNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین محکومیت اقدامات این کشور از سوی آمریکا در نزدیکی آبسنگ دوم توماس در ۲۴ سپتامبر را محکوم کرد
🔴
سفارت چین در مانیل، آمریکا را به حمایت از «اقدامات تحریک‌آمیز و غیرقانونی» فیلیپین متهم کرد و گفت گارد ساحلی چین کشتی تدارکاتی فیلیپین را تحت نظر گرفته، تعقیب کرده و به آن هشدار شفاهی داده است
🔴
پکن از واشنگتن خواست از «شعله‌ور کردن تنش‌ها» خودداری کند و اقداماتی را که به گفته چین صلح و ثبات منطقه‌ای را تضعیف می‌کند، متوقف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/149643" target="_blank">📅 10:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149642">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKC8KTolNg8xSr_VZHJxPdM5QHAHrNXE8ogWlMRl9TOljDAJKUKt3m9dCOivKKQDkjHNyE1jHae7UwOAy-1QQx1lPV67nCC993ve49WUcrmuoWE7fQNKhqVgzA63PMbulkzdi4nbATz18wLv0u9D27Gr8AG8dz1SprbVwJSyXCgcfpiKHhsbb20nqV9FuYkaanYKd2x87kyvyVthTnK9aSWTDYjsrz-07ryQZhSFOmsmLr60kKkuzOGe7KAg7kXn6BTDQQYfCiFGtWVDlJ5M2du-1P7PsNa189_bihnR6KnwAedZba7pW47J64vor5eyu2Ysrzn9rD6f1XPTkC58oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی با معاون دبیرکل سازمان ملل در امور بشر دوستانه در حاشیه هشتاد و یکمین نشست مجمع عمومی سازمان ملل
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/149642" target="_blank">📅 10:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149641">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سازمان هواشناسی امروز برای شمال کشور رگبار و رعد و برق و برای استان گلستان و شمال شرق سمنان هشدار نارنجی صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/149641" target="_blank">📅 10:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149640">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
هاآرتص به نقل از مقامات اسرائیلی : ابراز نگرانی نسبت به توافق هسته‌ای غیر نظامی دولت ترامپ با عربستان
🔴
این توافق به ریاض اجازه می‌دهد اورانیوم را در خاک خود غنی‌سازی و دیگر کشور‌های خاورمیانه را به دنبال کردن قابلیت‌های مشابه ترغیب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/149640" target="_blank">📅 10:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149639">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کارشناس صداوسیما: ایران می‌تواند روزانه ۲۵۰۰ پرواز را مختل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/149639" target="_blank">📅 09:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149638">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
فایننشال تایمز: ارزش ابرنفتکش‌های قدیمی برای نخستین بار از کشتی‌های تازه ساخت فراتر رفته، زیرا مالکان کشتی برای بهره‌برداری از نرخ‌های بالای حمل و نقل در خلیج فارس هجوم آورده‌اند
🔴
بازار کشتی‌های بزرگ حمل نفت خام، به وضعیتی «دیوانه‌وار» رسیده
🔴
قیمت نفتکش‌های ۵ و ۱۰ ساله به شدت افزایش یافته
🔴
چندین کشتی که پیش از سال ۲۰۱۶ ساخته شده‌اند، با قیمت ۱۵۰ میلیون دلار یا بیشتر فروخته شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/149638" target="_blank">📅 09:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149637">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
فرانس پرس: عربستان مدارس ریاض را به مدت یک هفته غیر حضوری کرد
🔴
هنوز هیچ توضیح رسمی و فوری‌ درباره علت این تصمیم ارائه نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/149637" target="_blank">📅 09:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149636">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
آنیتا آناند، وزیر خارجه کانادا: «اینجا در سازمان ملل متحد، کانادا در همین سالن مجمع عمومی سازمان ملل، قطعنامه‌ای درباره حقوق بشر در ایران را رهبری خواهد کرد؛ زیرا ما قاطعانه در کنار مردم ایران در برابر سرکوب و در حمایت از حقوق بشر، کرامت انسانی و خواسته‌های آنان برای زندگی بهتر ایستاده‌ایم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/149636" target="_blank">📅 09:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149634">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
کارولین لیویت، سخنگوی کاخ سفید:
«ما در بریتانیا بودیم و من در یک ناهار با
دونالد ترامپ و کی‌یر استارمر
حضور داشتم. دور میز نشسته بودیم و همه مشغول ناهار بودیم که رئیس‌جمهور ترامپ ناگهان شروع کرد به انتقاد شدید از سیاست‌های استارمر
🔴
ترامپ گفت: «سیاست‌های شما اینجا خیلی احمقانه است. باید مرزهایتان را ببندید. باید افرادی را که در کشورتان هستند اخراج کنید. من کشور شما و مردم شما را می‌شناسم. آنها از کاری که انجام می‌دهید متنفرند.»
🔴
استارمر فقط آنجا نشسته بود. این اتفاق در خانه خود استارمر و در کشور خودش رخ می‌داد؛ ما حتی در کاخ سفید یا در خاک آمریکا نبودیم.
🔴
البته من از این صحنه
لذت بردم و برایم سرگرم‌کننده بود
.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/149634" target="_blank">📅 09:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149633">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
انفجار مهمات کنترل‌شده در دزفول خوزستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/149633" target="_blank">📅 09:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149632">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daf9976c70.mp4?token=feTzfQWroVvVBlkvDD9WdOmQ9_wrds4UoYmpHzOjF4zoZ_uoU_UpeAaYeIw6BUyyZgsZj8GUJUOL1tWw1tl_SJ6u_QIjj3a-2A1_AbW3hoQEplm-iwDwYHx6yoRMD9qh8Ja7AZQKMTWNAU8vbVGAA1j_glsKJb6GF1EcYYnk0AjcGY2W7MV0Vl2K5AYUyPljzlLcKmnt3fz5846u_IJJOBYD6yNsKZu1OKWBK4ufRDneI4zCKqYkdgAskk08A1Wn_yxsDlP9KVyOB9YMQkeH_0rnuXheN-q_XQ72tCMMz_D1W1PgSM-quiZtEI-gs8Z0Kj1uw02pAicNjWbtMdObHmGmXGArTl7YDGeALypbZfiyXpo52nbE8S9vsW_O6Wca-6ZYOMal6alQ74DLouh0l0UScjfmHKU85pmD0_o_4OKZ_Hluik9IsftiptnSgWdrPv0sZaI7LRKVK1mXk87Qu5yEVdlE3uEoKKH3t1opEKxwSBFWm_BI44gp0H6nu56M-BGqv-jSXgra59XTmlvPfA3heFjm-bZ03XQN6xztbd3TPJ1Udebnlu4EJveiahU1G93utzdfU_CglJgrTShasKyZEztQB25FqdyQ9sZaitfaMiU5i2fJ2PqDkLS4CcvkpeQ64mfI4_TndDsGN93g5HVBfAauFt8XbjgX_b12mfU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daf9976c70.mp4?token=feTzfQWroVvVBlkvDD9WdOmQ9_wrds4UoYmpHzOjF4zoZ_uoU_UpeAaYeIw6BUyyZgsZj8GUJUOL1tWw1tl_SJ6u_QIjj3a-2A1_AbW3hoQEplm-iwDwYHx6yoRMD9qh8Ja7AZQKMTWNAU8vbVGAA1j_glsKJb6GF1EcYYnk0AjcGY2W7MV0Vl2K5AYUyPljzlLcKmnt3fz5846u_IJJOBYD6yNsKZu1OKWBK4ufRDneI4zCKqYkdgAskk08A1Wn_yxsDlP9KVyOB9YMQkeH_0rnuXheN-q_XQ72tCMMz_D1W1PgSM-quiZtEI-gs8Z0Kj1uw02pAicNjWbtMdObHmGmXGArTl7YDGeALypbZfiyXpo52nbE8S9vsW_O6Wca-6ZYOMal6alQ74DLouh0l0UScjfmHKU85pmD0_o_4OKZ_Hluik9IsftiptnSgWdrPv0sZaI7LRKVK1mXk87Qu5yEVdlE3uEoKKH3t1opEKxwSBFWm_BI44gp0H6nu56M-BGqv-jSXgra59XTmlvPfA3heFjm-bZ03XQN6xztbd3TPJ1Udebnlu4EJveiahU1G93utzdfU_CglJgrTShasKyZEztQB25FqdyQ9sZaitfaMiU5i2fJ2PqDkLS4CcvkpeQ64mfI4_TndDsGN93g5HVBfAauFt8XbjgX_b12mfU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی آمریکا: «در هفته گذشته، یک روز داشتیم که بیش از ۲۰ میلیون بشکه نفت از تنگه عبور کرد؛ رقمی که حتی از سطح پیش از درگیری نیز بیشتر بود.
🔴
میانگین روزانه در حال حاضر حدود ۱۳ میلیون بشکه است. بنابراین نفت و گاز همچنان از تنگه هرمز خارج می‌شوند.
🔴
مشکل قیمت‌گذاری امروز، بیشتر به ظرفیت پالایش نفت مربوط می‌شود تا میزان جریان نفت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/149632" target="_blank">📅 09:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149631">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b927aa45da.mp4?token=dXsxJvxEJo5TNDABlHrxyfu9Qjkh2s9LxLT3rEVYnZ3lWHfzv9u7CdFO_o1pBTQkjsDXCgf5wgGJf24nMxFVElFALrgtXtx6IJkaE4GNiy0TkWSsxq1G-laxHj1bMlAwnTj_zSjrZeOad5O54puinnfPVI33lU8C8Ivbtwqu2ORLh_Jm-uFMtrHqxqSHVbUzT2OZukMDV5K_S1QwHMnn3jH6tdkABwO5Sc-DH54Vw2Jdzir1gOg10mFe7bdNdkNt0nC0qypV12ldjzJ_a6hMHCTqWEKT7ENo5kI0OZoVN8AgqeN3YayG9cZ5bHtoFsuD-3aE0MqGY7b05R9rjlPPVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b927aa45da.mp4?token=dXsxJvxEJo5TNDABlHrxyfu9Qjkh2s9LxLT3rEVYnZ3lWHfzv9u7CdFO_o1pBTQkjsDXCgf5wgGJf24nMxFVElFALrgtXtx6IJkaE4GNiy0TkWSsxq1G-laxHj1bMlAwnTj_zSjrZeOad5O54puinnfPVI33lU8C8Ivbtwqu2ORLh_Jm-uFMtrHqxqSHVbUzT2OZukMDV5K_S1QwHMnn3jH6tdkABwO5Sc-DH54Vw2Jdzir1gOg10mFe7bdNdkNt0nC0qypV12ldjzJ_a6hMHCTqWEKT7ENo5kI0OZoVN8AgqeN3YayG9cZ5bHtoFsuD-3aE0MqGY7b05R9rjlPPVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی آمریکا: «تنها راه برای ساختن آمریکایی بهتر، انرژی بیشتر است؛ یعنی افزایش ظرفیت تولید انرژی.
🔴
آیا می‌خواهیم در زمینه هوش مصنوعی از چین پیشی بگیریم و از مزایای آن در کشف دارو و کاهش هزینه‌های مراقبت‌های بهداشتی بهره‌مند شویم؟ قطعاً.
🔴
اما این هدف به ده‌ها و شاید صدها گیگاوات ظرفیت جدید تولید برق نیاز خواهد داشت
🔴
این دولت تمام‌قد پای این هدف ایستاده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/149631" target="_blank">📅 09:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149630">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: تمام بانک‌های تجاری بزرگ در امارات متحده عربی و ترکیه انجام تراکنش مالی با ایران را متوقف کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/149630" target="_blank">📅 09:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149629">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b9049d7e.mp4?token=knCj1xenBDibX6FSpBGM6KM_y7TeFq8BWELempnsTi28h46mkYyaXAeqMrCAyiLlWuEnPLL31Z7l4N9XCnjgJQrpk0XgdRzD430SIu4iPLVT6J_hzTgjywmnLT3vjoUHfhcUleYAzRwffJz1tqH0YXb0nr2Jt2MFW75mQYPoZv7sWVDI2XmqMVlFmH0o15I5eZj0FaF4whRzngC-ajbK6wIIB5sQ1_jHbSsgPYUuemjUeXOmwx6eyXnxgekhloChmzrrlonPjdnS6p4Ks7FmtIfvMfCh2TuOPhE4k2Je1TpH4ETbtUtC7k9rz_UIu3IkWZgLdVS4irsQ9al2ogcFIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b9049d7e.mp4?token=knCj1xenBDibX6FSpBGM6KM_y7TeFq8BWELempnsTi28h46mkYyaXAeqMrCAyiLlWuEnPLL31Z7l4N9XCnjgJQrpk0XgdRzD430SIu4iPLVT6J_hzTgjywmnLT3vjoUHfhcUleYAzRwffJz1tqH0YXb0nr2Jt2MFW75mQYPoZv7sWVDI2XmqMVlFmH0o15I5eZj0FaF4whRzngC-ajbK6wIIB5sQ1_jHbSsgPYUuemjUeXOmwx6eyXnxgekhloChmzrrlonPjdnS6p4Ks7FmtIfvMfCh2TuOPhE4k2Je1TpH4ETbtUtC7k9rz_UIu3IkWZgLdVS4irsQ9al2ogcFIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی آمریکا: «ما هنوز قیمت‌های انرژی بالاتری از حد مطلوب داریم و هیچ‌کس بیشتر از رئیس‌جمهور ترامپ از این وضعیت ناراضی نیست.
🔴
او رئیس‌جمهورِ انرژی است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/149629" target="_blank">📅 09:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149628">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBeq3zaNuRpcWokRBPRE3PDBGgBO202ELbbXKKHnFlOXS7o38Yc8H_6RUIOOuPW7EWmDP7bCm5r-N_In6aotDDrNPF8vmPbs-BfLEYAFRbJBizu8h0Ad7UlpzbSNpCS2BIFSwe3hxKPpq1hstOk2jZ8WSISQsrQGEEgFpTK2PWC_OxpvsxoxKXkfAL0OBwZ6gs6jjOUw5RWKlPTMG1cUpBGht_9wkpA3EJJm3pwvq0F-DlLzN5jnnx6jNX6DnSAsxFVK3kaZrjhEwLmc0fnsjDCFXjPX1ODg_Ah2yqxnxj6FfYL35kCcdqWzmiZuaHIlYlBYX9Guyv2ODUe3AZaWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : «ما بهترین شاخص‌های مالی در تاریخ را داریم، اما رسانه‌های خبری جعلی حاضر نیستند آنها را گزارش کنند!!!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/149628" target="_blank">📅 09:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149626">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_RoAJKDISQ2LMjCe1eylrTdVXkFM_16jCAs_8yKnGVLkXZGIHsETQjyAsXHArAgqtNgOcQ3fzcCcYDfRNDShOFFn-5AIg53NKca8mCdbXEcSCX1NR-lup0lns3aPoMZT8kUJEKU_tGzHf78Hv6tSdQhsE3MhmMWsoT0RLS1dlS-Bv1Hk1cdC3HVamSj1vgZKtHzHGMFdObq27zq_Waheb824QF4lwUWh09SKYanSl8qDdLkbcKZJTtcNDFtQxpTw8G7KbR_Ac8nnjdyJNyR87opNsJuyk2O7VtLmwBIwwKv3-0BLf4t28cZyhShv_qzJSZZALezQaYTnxJydwf-qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن‌پست
:
جنگ با ایران مصرف نفت و گاز در جهان را به شدت کاهش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/149626" target="_blank">📅 08:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149625">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/B-IMmVElbE9yg_otjt4bpHixQRoUpkTQoEUdkIfXFyAggf5EZ6vQdnMsq8_ytlsKMjqfm_pCwZswcX_iOV_KC4Kv5yXeRKJZBQKyexG-rOJ93_V6ZSU_K7qZrw2sdYF4yZS7O3CDKR2OIYugZ7FwJru9H2tNs1a7El4Mooz8v03SWcGd6oujoKpF6C78dAnwiSQeW6_3U_h6bYrOaLtoH-6iNvVt8By3vkfXA_g_MclzyVjzX9AJkxGYyyTudvZHjdWLmZ6I0n6Q7UScHGA-WdegrqFO65yzhV2otX76GAzdy2Iq66XiuDjkJ-6W-QIKrPg4i5SFII3E7910ii4f4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیش از ۱۰ فروند موشک کروز ضدکشتی به سمت تنگه هرمز شلیک شده است.
🔴
گزارش‌ها حاکی از آن است که دست‌کم برخی از این موشک‌ها حامل مین‌های دریایی بوده‌اند؛ مین‌هایی که هدف از آن‌ها تغییر مسیر کشتیرانی در مسیر دریایی عمان عنوان شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/149625" target="_blank">📅 08:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149624">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
عراقچی: شروط ایران برای باز شدن تنگه هرمز تغییر نمی‌کند
🔴
هنوز پاسخ قطعی میانجی‌ها به ایران منتقل نشده و تهران پس از دریافت آن تصمیم خواهد گرفت
🔴
شروط ما مشخص است و هرگونه حرکت رو به جلو برای باز شدن تنگه هرمز منوط به محقق شدن این شروط است و از آن‌ها هم کوتاه نخواهیم آمد.
🔴
ایران هیچ‌گاه مسیر دیپلماسی و مذاکره را نبسته، اما از حقوق خود نیز کوتاه نیامده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/149624" target="_blank">📅 08:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149623">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا : تیم‌هایی به نقاط مختلف جهان اعزام شده‌اند تا از کشورها بخواهند علیه ایران اقدام کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/149623" target="_blank">📅 08:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149622">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-qH3c3HyEDuY_rShltkr68VeOHdUys1MzhEmU4l1H5EWM62JiUL-D10LnF-lRfxmsLRD0LXCb6RDs7PacEeNP3IAiYIK8lvQxuI8fZ9iLfB4bYoh4FFZGqq75S5CMC7BjbbFAn_rzeBsoZffWrX1K-9rRmruSFwok6gS_oqcXJX0hL3v17oMBlsTOi2pCR-UAl1wCfSfGKhLZfg98coZAsQCeoAjFkAXKmHNrgO3nJBNGZ3mGBxYDm7RUG-NwW7yrFZkfe99uLHXhK7nrJFRc9NBrtD_b2OG0bgu4YY1WCPPxx_5jc7GRK0y1JxCLEiQY2UPHI2np7hYS3CwdRRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: در انتخابات میان‌دوره‌ای به نامزدهای جمهوری‌خواه و نامزد های مورد حمایت «ترامپ» رأی دهید
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/alonews/149622" target="_blank">📅 08:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149621">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgI2-c44AyGQJAP5LAprHXarZPeu6jqg09Gd29bTPXVD-Kr34Ltpd6-Ri6fC5FOvo4l4-SHLg3o9Jo4rIe_1f1qj-rFAOgHCy68-BPY-iiC95S9cVZfa9ul6exNyNP0jimnjihHd7AXrBaFpjUxVviwBx-rmlmsZd6RxJfQqPigd_zp4iFYsAew_WitunNBDVQOUmo2ewCz3IagpL2S9_S0cEzz2B_kjKXtX8FW-GAw79XG_XUkCltGXplAtH40yowOtrTdb6Yr3D9aw0nHnQenfcvcJHkQEnYoUfuoXd2UOh3mndik5bxkD85NBvkdvGBHRxD7PzX5LnEaNj7JjAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تام کاتن، سناتور جمهوری خواه: یک درگیری جدید با ایران در پیش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/149621" target="_blank">📅 08:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149620">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJPeTjIoODZM6oYiI74PUjowOB-wt4id46bS9qv-U0pRUaTeDsoJLTX6hFFOrQwwlFUuLB0jv_z3cZ7LB7H4TkdutCMebeVXeltLmUsqkdfQgePwFlZrSekpMLJxTzoHR0Sp8SQtnWGlz0NhNmrWbGHBVdHPLmORNzuZDuSunGuq7cl7iVAOFJqxPyqtfXmKwB-nYpSTybAkr5TOG8RvsJBV2YjtM6UdAHiXae2TZd7MCF488XOZe6Ji4Axs2UjZyjoB4xpfiVfTKAMjKqkQv3Cwi2GIySA3-kcMCRtuQAHgs60Pm-NoonLDwX5Jwb9ArX0OuUrQNJ0SiwrryqmHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
بسیجیای دانشگاه تهران قرار گذاشتن از امروز تا زمانی که دانشگاه باز هست نذارن این پرچم زمین بیفته و هر بار یه دانشجو میاد نگهش میداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/149620" target="_blank">📅 07:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149619">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
خبرگزاری اورشلیم پست:
عباس عراقچی، روز جمعه در پاسخ به سؤال خبرنگار فاکس‌نیوز درباره اعدام بیش از ۹۰۰ شهروند ایرانی در سال جاری و همچنین شکنجه و زندانی کردن هزاران نفر دیگر، لبخند زد و سؤال را رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/149619" target="_blank">📅 07:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149618">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea1ac8cce.mp4?token=UEgh3cqbO0SO39J4ctG7ORektAxGGPE-I0Pw55Z74XRhC2g60oPDwV-hCacqDpTrTEmkbdydzfGezb_OmQBZd77_KNcXvfcFpXrjqpfCErP7CytsybkBYmLjxEDoJ9Fbrdj303bTF3hEZa-sg3M1spsAclI8ABMvQ9yB99e36F9NonXiLWcTBKvTlR-hv2RQMXomXjZCORMXXHiQoNpEhDMp106f_GrQw5Ovvk5tA92WhkTCxk9wlVdvtJ42z6KMAIfhBt2VUqXndFHfOQcQ_-EDEUk_tfX2zNBwgmoXGzTMxAJZy5s78XpSw17pSB8rQwGlL52nINsBPliZsARkz7IiAr-6btNZTsGIr6hyImAOCy6vFNcMJssWWi9egoWg1ZFOa65QXTyorWym84ds97wYWwkiArFY3-4m6rJppfe9Msq422DJhPsNdNiP4z6DzCuzFocHDzC3uATP7ulFQE7iYBi5oSRi2D1B40J4XjQaiNy-1bE7HmkXquVINsXXrDHoBxfEy6YF-uuYPOpC6EHeXeHsTV_xm42ZPHWh9S4tTgoMwq2o5qgoafBcSNga98AMx15PzqVZ2eIzefu7Nry3WICukzOaC0y3cjPA8Q3jMCU0u3l5DoV8AloiAAdt3u1Fbet9sfiZlkgidCPd_BYbBU6Cq_9q8BU42hqvA6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea1ac8cce.mp4?token=UEgh3cqbO0SO39J4ctG7ORektAxGGPE-I0Pw55Z74XRhC2g60oPDwV-hCacqDpTrTEmkbdydzfGezb_OmQBZd77_KNcXvfcFpXrjqpfCErP7CytsybkBYmLjxEDoJ9Fbrdj303bTF3hEZa-sg3M1spsAclI8ABMvQ9yB99e36F9NonXiLWcTBKvTlR-hv2RQMXomXjZCORMXXHiQoNpEhDMp106f_GrQw5Ovvk5tA92WhkTCxk9wlVdvtJ42z6KMAIfhBt2VUqXndFHfOQcQ_-EDEUk_tfX2zNBwgmoXGzTMxAJZy5s78XpSw17pSB8rQwGlL52nINsBPliZsARkz7IiAr-6btNZTsGIr6hyImAOCy6vFNcMJssWWi9egoWg1ZFOa65QXTyorWym84ds97wYWwkiArFY3-4m6rJppfe9Msq422DJhPsNdNiP4z6DzCuzFocHDzC3uATP7ulFQE7iYBi5oSRi2D1B40J4XjQaiNy-1bE7HmkXquVINsXXrDHoBxfEy6YF-uuYPOpC6EHeXeHsTV_xm42ZPHWh9S4tTgoMwq2o5qgoafBcSNga98AMx15PzqVZ2eIzefu7Nry3WICukzOaC0y3cjPA8Q3jMCU0u3l5DoV8AloiAAdt3u1Fbet9sfiZlkgidCPd_BYbBU6Cq_9q8BU42hqvA6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
وزیر امور خارجه کانادا:
موضع کانادا در قبال جمهوري اسلامي ایران کاملاً روشن  است. تهران تهدید اصلی صلح و امنیت در منطقه خود محسوب می‌شود. این کشور هرگز نباید به سلاح هسته‌ای دست یابد.
🔴
تهدیدهای آن به حقوق کشتیرانی در تنگه هرمز، یک توهین مستقیم به حقوق بین‌الملل است.
🔴
کانادا از تمام ابزارهای در دسترس، از جمله تحریم‌های هدفمند که این هفته اعلام کردم، برای مقابله با رفتارهای نفرت‌انگیز رژیم ایران استفاده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/149618" target="_blank">📅 07:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149617">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPAYONET | VPN |</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ59hp4dbvkBOwS4NT_mriuISRaLX55CyqaWzY846CJmoQZ_PkolPMD6W5iHLrR9rHCJtrIT_zzxLj55TuL6vNiR5FzH6NhT-tDAK_7Cn4I5M5KhvfJ3cTA9llMJ2lyTYnEA1M5-EZv0Mb4wreJ38N1_eDmUEs3yzdXFVjLO6miXVCZrgDPp49C3Ev9WPX7P6NDe8VYU2ILQVZs1oHfB5xi1W__sxXXMzOUGASUH01-cseWi-KFhf2VYCybwsstQqY-QlFOPpokfo89ni3XUxdIggQjrJORtMvnXXeF2PDIQ1NKcS525D_ApsUN5ZHK04E9nHTWiNZw8MAgdwJsOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
کانفیگ v2ray نامحدود | چند کاربره
🦋
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
📍
نامحدود _ PLUS
⚡
:
🇩🇪
🇫🇷
🇮🇹
🇸🇪
🇦🇹
🇦🇿
🇵🇱
🇹🇷
🇺🇦
🇦🇱
🇦🇩
🇫🇮
🇳🇱
🇺🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇲
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
برای اولین بار در ایران
👑
کانفیگ ها بدون تبلیغات هستن
🚫
تمامی لوکیشن ها قابل استفاده در جمنای
✅
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
☄️
مناسب شرایط جنگی و اختلالات
💬
پشتیبانی تا آخرین لحظه اشتراک
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
👾
نامحدود تک کاربره  | 79 تومان
💵
👾
نامحدود دو کاربره  | 99 تومان
💵
👾
نامحدود سه کاربره  | 119 تومان
💵
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
خرید و تست رایگان از ربات
⬇️
BOT
🤖
@Payonetvpn_bot
ID
✅
@payonet_supp
❤️
CHANNEL
🫡
@payonetvpn
🔺</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/149617" target="_blank">📅 01:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149616">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
خبرنگار اسرائیلی:
حملات امشب سپاه پاسداران به کشتی‌ها در تنگه هرمز گسترده و کم‌سابقه بوده است.
🔴
گزارش‌های دریایی از افزایش حملات و کاهش شدید تردد کشتی‌های تجاری در تنگه هرمز خبر می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/149616" target="_blank">📅 01:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149615">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHrAcdI3UL53YL8ddcCtt04nXdz_x37D6Ed0sUlYttD2-2o5CrCkB8Coo-qwpKqCFpEGEXFNoQE4Tm6DET-BPXF2nnI8C2C017WhRlE8j6Tg3exlma1Rq5uxuePmTGQHqs-bgV0WIwgQoBsqTwfaH2J1thS_5iirKuQIy-H2wTM-6ZgW-crXzLTAMWR0nfyHF1CXzAaeYBLMUJ1mtv8Ds3AZ2bYFtSflicECV1D2lkw0iL1-FhQ7Lf3Ekn_xZlb-uUQ9l8mjzb5jjR-J8jP_LoAEUD4wsCk5yf85jZHS25s3Ev_ZAHRK0aAi472L9KKNvD50alKFyueVDAH-fepyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توهین عجیب به پزشکیان در ایتا
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/149615" target="_blank">📅 01:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149614">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
نیروی دریایی سپاه: در جنگ جدید، شناورهای دشمن در اقیانوس هند هم امنیت نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/149614" target="_blank">📅 01:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149613">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vixZ0CqyOjkK_ePtIosjNgncDr-PyzbhtICLXzNxtMrzkLsjYjlOKUagn_FI8y_T32ZrUAYaoEfICn3Ao0TLYWkwcOMFE8h9Ega2jh_yxQPzq4qIKxJouznPowoPwA2pcXLDafiPhjeBSvz6yve_9QdJwoTqeRLu-FPpu9YhHQF-cKKsWYPdlJIKj-GDDJhtX1ZNMot_d67zcrTGGj568Ev6tQHwsCFdLpPtl-bBX-4aBaGSwKplqPwk1aDNX4sReWBzOOhwE89y2knedbf1A6552pP0lx8W-vH_rd3lm-fYgXqR2Jk-YQ--hp-JGcdLn_TWokIgeW0xlRUhVAraoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی:
از شروط خود کوتاه نمی‌آییم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/149613" target="_blank">📅 00:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149612">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b0c9e9f6d.mp4?token=BXgitTZjZTCwQJ5UXerVTipn38p1Ho1kPpP6U8z9fw--iRXFbKwiQiZGoZFLfvTo9a0pKMGJ5SJvETRDxhFHN4tkmAYifoQxEs0hY287uZi3hfs9Gt0lXkHwl0IoY8sJuB9kc8jJjOHnurXh8rjDTOB55SjPW1hVNDGA0fnWQjBaUexz_xrGs2kMoS-eIFUHB1gg9wsAcPPpuhIXrU_Qt21wWklJhu9aQfR9bwg00wUEcX4C0b8q6yfG7OwMlmlEOzHoCrwUE1dG9R4_IFhne38kGjZC-9fTB_m0uekeT0kjZAs_fXtnYmjnrecfViTYq0ZDKdmQEo4l0rm2-qZsKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b0c9e9f6d.mp4?token=BXgitTZjZTCwQJ5UXerVTipn38p1Ho1kPpP6U8z9fw--iRXFbKwiQiZGoZFLfvTo9a0pKMGJ5SJvETRDxhFHN4tkmAYifoQxEs0hY287uZi3hfs9Gt0lXkHwl0IoY8sJuB9kc8jJjOHnurXh8rjDTOB55SjPW1hVNDGA0fnWQjBaUexz_xrGs2kMoS-eIFUHB1gg9wsAcPPpuhIXrU_Qt21wWklJhu9aQfR9bwg00wUEcX4C0b8q6yfG7OwMlmlEOzHoCrwUE1dG9R4_IFhne38kGjZC-9fTB_m0uekeT0kjZAs_fXtnYmjnrecfViTYq0ZDKdmQEo4l0rm2-qZsKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی معناداری که ترامپ ری پست کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/149612" target="_blank">📅 00:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149609">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/149609" target="_blank">📅 00:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149608">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سخنگوی ارشد نیروهای مسلح: قدرتمندترین ارتش جهان مقابل نیروهای مسلح ایران زانو زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/149608" target="_blank">📅 23:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149607">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
البوسعیدی وزیر خارجه عمان : امنیت کشتیرانی در تنگه هرمز نیازمند همکاری همه طرف‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/149607" target="_blank">📅 23:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149606">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کارشناس صداوسیما: ایران اصلا به نفت‌کش‌های امارات شلیک نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/149606" target="_blank">📅 23:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149605">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
اردوغان: جای نتانیاهو پشت تریبون سازمان ملل نیست، بلکه در دادگاهه
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/149605" target="_blank">📅 23:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149604">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
پزشکیان: ما می‌میریم ولی سر خم نمی‌کنیم. آمریکا و اسرائیل فکر می‌کنند با این فشارها می‌توانند ما را ساقط کنند اما ما با قدرت بر همه مشکلات غلبه می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/alonews/149604" target="_blank">📅 23:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149603">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
بیل گیتس مالک مایکروسافت: بزودی ممکنه هوش مصنوعی اونقدر قوی و خطرناک بشه که حتی باعث کشته شدن ۱ میلیارد آدم بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/149603" target="_blank">📅 23:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149602">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MD37q8aJrJxvJVT6R3fvMDKvTI6vCUr-dj2muPUI53R2LaOXWn2CrNmBcGdkArLd-NaPFnyMVpufKxMbtTc-bYG_b1XO7s2iv77JDp7lSrYXBmrMuGRD76EC-z-NL5MJ4m7_dkjo4Rdp8EG8Hra2N3_SlyFL0Cyz5E4Dav5Hn6eeZIbhOGacOf6sIzQp6wi6Dx_G5qFP6pUQxvo4ptNLFx6a7jVveXSQE5920ftqBK0qIkYLV7oD5zehEanlztT51BM9oB8fbb2rKODtU4IpSuwHF93vLMFTv_t6s5u_nD3kolbNkxQw6C8oYwNGC6uOJbWCo-hEUMKwyS8ipsDTMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: امروز روز بزرگی برای کارگران صنعت خودروسازی آمریکا و خریداران خودرو است! من به تازگی استانداردهای جدید بهره‌وری سوخت را تصویب کرده‌ام که دستورالعمل احمقانه مربوط به خودروهای برقی که توسط جو بایدن و پیټ بوتجج مطرح شده بود، را لغو می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/149602" target="_blank">📅 23:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149601">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHsK_aQwcs3IaaCTPFllUXksGUlBm_mvtDKQBINIx1W1AdXcUYQsGjZGU3SyM4m8Gd0dAKldMqnxlLaR5AlLVGNr3Xt---AAEXJQ3NgbmP47ExhriQWmzn1Daq6zpj8RstaanfHqL0YSLVN97bViThawPd-p2tKzGK3nmuTBe-Wd7Zrz2h_treh9b2LJVmO0DYZ_yrXFpfP4VBOkjn3UkDLT9aGJNmZF-XbLYR7OF4oIBnM-eGMJFBhTL0Aw2Op4dh67sKLxqsLJR0JPa1Smu-LOvyY6xIdBPZHh2F9aKLIehTS54bfighHFoALpH1ewqHZZ-NBjlIMiEDA1yhTcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت اینترنت کشور
🔴
در حال حاضر اینترنت کشور به‌طور کامل قطع نیست، اما اختلال و افت کیفیت در برخی مسیرهای داخلی و بین‌المللی مشاهده می‌شود.
🔴
وضعیت: ناپایدار / همراه با اختلال
🔴
اینترنت بین‌الملل: دارای اختلال در برخی مسیرها
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/149601" target="_blank">📅 23:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149600">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
پزشکیان: ما و یمن در حمله به خط‌لولۀ عربستان دخالت نداشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/149600" target="_blank">📅 22:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149599">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
پزشکیان: بی‌هیچ واهمه‌ای آنچه را که اعتقاد داشتم در سازمان ملل مطرح کردم، شاید اگر رئیس جمهور آمریکا آن حرف‌ها را نمی‌زد ما هم این حرف‌ها را نمی‌زدیم
🔴
برای این در تریبون‌های بین‌المللی صحبت می‌کنیم که دنیا فکر نکند که از گفتگو می‌ترسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/149599" target="_blank">📅 22:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149598">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
پزشکیان: زمانی که به نیویورک رسیدیم سخنرانی ترامپ را به ما گزارش دادند، که حرف‌هایی زده بود که شایسته خودشان بود و در نتیجه نوع فکر و پاسخ ما را تاحدودی تغییر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/149598" target="_blank">📅 22:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149597">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
پزشکیان در گفت‌وگو با شبکه الجزیره: از توافق عربستان، ترکیه و پاکستان استقبال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/149597" target="_blank">📅 22:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149596">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
پزشکیان: نتانیاهو نتوانسته غزه را وادار به تسلیم کند، حالا می‌خواهد حکومت ایران را تغییر دهد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/149596" target="_blank">📅 22:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149595">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a56a2e5a7.mp4?token=N6EIEqsopKN8sM3ps_ZehSITrbvkZGzIMhfgC5IHhxdQaQKansQr0MqEE3uXxnRfGND7X0oy-ielzjYz7IZIdjvflYEUUj4khSg_6JtDeeDj9lfjhwu7tJ4BMb0u4vq90gRa5LGnUBgnmnIXyz2sFAkq3Yy_Yj-JZKlJ_H69Fqd-UjVxiwBiJMKv2M36PSu8C8gyyZCL8ge40kNyCzq3cx0gEopvfFKpdTmx0onKuR9VQmkFQH3Lf1IVRA6Qrcg540QGhJCcovhAHRAbW7RwTl4JTkCD1HMt-GSHVT5F8H_ITyFo53biOwqBD9Y6wGSWhVq5L8HjAeAUGkQkduJHOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a56a2e5a7.mp4?token=N6EIEqsopKN8sM3ps_ZehSITrbvkZGzIMhfgC5IHhxdQaQKansQr0MqEE3uXxnRfGND7X0oy-ielzjYz7IZIdjvflYEUUj4khSg_6JtDeeDj9lfjhwu7tJ4BMb0u4vq90gRa5LGnUBgnmnIXyz2sFAkq3Yy_Yj-JZKlJ_H69Fqd-UjVxiwBiJMKv2M36PSu8C8gyyZCL8ge40kNyCzq3cx0gEopvfFKpdTmx0onKuR9VQmkFQH3Lf1IVRA6Qrcg540QGhJCcovhAHRAbW7RwTl4JTkCD1HMt-GSHVT5F8H_ITyFo53biOwqBD9Y6wGSWhVq5L8HjAeAUGkQkduJHOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکت پربازدید از ترامپ
🔴
ترامپ پس‌ از دست دادن با زلنسکی حرکتی انجام می‌دهد که برخی رسانه‌های خارجی نوشتند اسمش «دست شاخدار» است.
🔴
می‌گویند افراد خرافاتی معتقدند وقتی با آدم نحس دست میدهی باید فورا این حرکت را بزنی تا نحسی طرف به تو منتقل نشود!
🔴
برخی دیگر نیز حرکت دست ترامپ را عادی و اتفاقی می‌دانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/149595" target="_blank">📅 22:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149594">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OR8wR11Vs3zFTy1Q8ixMk9ei_47-y4vnCNbSIcKrUoEW1apwBg8I00E3BZTAWz4aqapwNOD5gpKoR43Rh10o6cPUyMdFmeQmr4nJYggcE3d_21uGyZDyZsHjDO1aM-Ot1JO3I7woxHu1ag3UuwRIpEu-Y_PYsvN8hD-6OELaY_sS7xczCKPsHM448ndMw4Qfzxm4hfTgics-znitK4fifqhGzT376N4YekKYjTfaJmhOTQ0CC5wGwPbOx2P7hHYUm_JOWvpsjhKSRRBt4hzpbnNXNTb58YXPfhJ5PVhoIsBvtraHSG62Fp1Dk0TezJp6E5wU9QHR1PH-8LT3vj5yVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شش فروند هواپیمای تانکر آمریکایی در نزدیکی تنگه هرمز در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/149594" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149593">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
پزشکیان: می‌خواهند ما با ذلت با آنان مذاکره کنیم؛ ما می‌میریم اما زیربار ذلت نمی‌رویم؛ ما اعتمادی به مذاکره با آمریکا نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/149593" target="_blank">📅 22:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149592">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
پزشکیان به تهران رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/149592" target="_blank">📅 22:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149591">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/get-_44SOqB1g5tc0XidqpyFvyWW_jpAFK6yANarQ4VEBh8m6KicERHIUdWlBajjmIOx9l-qFrkyPh3B8B5sW2XhRM-K00w-xgtqgpwMevcFbg-TxT2N7hkm8HIWppNbzIpdLHckqFqjbzmu9mCkMrxMo45F8d-_jEcOCcGu8ukDyVPWTQRK9XdG0gczewIcjLCRK5FLTRCnZ3Ap8vCcFrT-5hwHd0Ve3RRfPRRBgvUVP11EsTPkMyGJgcKn1gnmp-UepB3m2gDTW3UbdOMwNgO3SWydt71ZYstg0Wkfc66vd8-LwSMjNbcUWiNK60p6cxgwubOFtGMBecY5CyeYvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسام الدین آشنا: تجمع غیرقانونی در برابر خانه‌ها و فرودگاه‌ها نه مشکل « ناترازی»ها را حل می‌کند و نه رسوایی «ناتراستی»ها  را پوشش می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/149591" target="_blank">📅 21:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149590">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس:
به زودی ایالات متحده بر هدر دادن فرصت پاسخگویی به شرایط ایران برای بازگشایی تنگه هرمز و انجام ندادن توافق پشیمان خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/149590" target="_blank">📅 21:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149589">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
هواپیمای حامل رئیس‌جمهور تا دقایقی دیگر در فرودگاه مهرآباد به زمین خواهد نشست
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/149589" target="_blank">📅 21:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149588">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ترامپ: ایران دیگر پولی برایش نمانده؛ برای همین دنبال توافق است
🔴
اگر تهران به توافق نیاز نداشت، دلیلی نداشت که پیشنهاد مذاکره ارائه کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/149588" target="_blank">📅 21:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149587">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری /فاکس نیوز:؛عملیات نظامی علیه ایران اجتناب ناپذیر است.
🔴
ژنرال ارشد آمریکایی به فاکس نیوز: با شکست مذاکرات جاری میان ایران و آمریکا، مسیری که در پیش داریم شامل ادامه محاصره دریایی و هوایی و عملیات های نظامی گسترده از سوی اسرائیل و آمریکا علیه ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/149587" target="_blank">📅 21:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149586">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سخنگوی حوثی ها: با ضربات موشکی و پهپادی به تجاوزات سعودی پاسخ داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/149586" target="_blank">📅 21:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149585">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZ0ZNqkVltmAXfNdfQe_vhc7InWPRKcTbn4thjfT00d3C7ydqKJJroM-UIdnn_5Mp0zo7oqtHWyhYt8hkQL0T4EtuZHFc7UfFRza_9KJwT_cqI_BI2dMLS9SqJRH-4YsMIvmJhkpZtrkztFXa8xidRK_PSOhTgTmSIKHZbUeExjpmQT-kL_cfaOzE3c54kgcwVo4eNplLinAXsBcBs_VyrFRRk73wkm3gozWPEZ1p2P_KiPeOXLHqxBgwj9_yKrp_nAanjJUiZtIgBHGJViy8w9z5QZ71wODeXi0iF6DA9JfhNS9Gs4zzt0nitCbDUC_sFs_d_FwZW46yNy1U7CM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد میرشکرایی درگذشت
🔴
محمد میرشکرایی، پژوهشگر، مردم‌شناس و چهره ماندگار میراث‌ فرهنگی امروز  درگذشت.
🔴
ثبت جهانی نوروز یکی از اقدامات درخشان او بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/alonews/149585" target="_blank">📅 21:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149584">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TX8M7PLzwaRy6CWF8_78yjqEycTvqzOvjxXCSsy6ZY8_I-zvwcmdjIpR6PZid-NhGNyMAWQ8uJ-USjK9IuUS4Z7OgFsU_foU1hT7nwdkkVT8kGscmcoeh-YDRDzLfGuVOZgmv0gFI4Lq13p2z2XVn-4n8bqpmZYMfm9VDZmZAfUxfLJXVyURSb_A4yrEfLghbbK5KUGRR0BG_TzYleu_QcQfwXfcxqFVpBD3eFhLEmfPRbxEd6rVleqGY0VbFZuu-ukEXEFiC81ROqJJCq0G1we7vCPnewO4-vua1h4waXTPuVJRCrS97Hj4GPIPyBAFPdp0eSnlmCPP2rL_vz8qpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت پروازهای ایران در مقایسه با سایر کشورهای منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/149584" target="_blank">📅 21:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149583">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
محمد جعفر قائم‌پناه: حضور آمریکا در منطقه سازنده نیست و سرنوشت این منطقه باید به دست کشورهای منطقه ساخته و بالنده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/149583" target="_blank">📅 20:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149582">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
العربیه: ترامپ به تیم مذاکره‌کننده خود اعلام کرده است که تیم مذاکره‌کننده ایران تصمیم گیرنده نیستند و با آنها نمیتوان به توافقی رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/149582" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149581">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزیر خارجه عربستان سعودی: تنگه هرمز باید به شرایط پیش از جنگ بازگردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/149581" target="_blank">📅 20:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149580">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtdx53AunjU1_NSCu0gvGSsI-3_lPVyvPb1bKH7r8_uU_7zoUtimffL4ojxDvnAUfyhydagGrYyVZzMR58qeQqIf78RfY18Hfshjd_80nwR5-7DYpL3k8IYJ1m1eLlQ2p-5pWdJ0oW9oCdmpy12b232cowoOetPut8ovSWIBVe8OCBT-sSbeEGu8SnrBItOUY9bJ6xTwzxSqQxeCWfGmQnQINt00ZAn1zCjXTXfmVXVghgCmzsI6omBTUWgnGPdadGSYtUDe6_n4oTUc4TK7PJNqyHTlrJ9J1-Ttz7Cp8oaQCq-EkGtvzDFqGJR86BM7SulOvIIaPWWOYOPhxLZwDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واردات برند های لوازم خانگی از مبدأ کره جنوبی آزاد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/149580" target="_blank">📅 20:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149579">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
لاوروف: روسیه معتقد است زمان آن رسیده که به دولت فلسطین رسمیت داده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/149579" target="_blank">📅 20:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149578">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
لاوروف: حمله به تأسیسات هسته‌ای ایران، اعتبار آژانس را خدشه‌دار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/149578" target="_blank">📅 20:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149577">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
روسیه: ابتکاری را برای برقراری صلح در منطقه خلیج‌فارس و حل‌وفصل بحران تنگه هرمز آغاز کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/149577" target="_blank">📅 20:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149576">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
هیأت آمریکایی همزمان با آغاز سخنرانی «برونو رودریگز پاریا»، وزیر امور خارجه کوبا، صحن مجمع عمومی سازمان ملل را ترک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/149576" target="_blank">📅 19:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149575">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وزیر امور خارجه عمان: در نیویورک با همتای ایرانی خود درباره تلاش‌های کاهش تنش و تضمین امنیت کشتیرانی در تنگه هرمز گفت‌وگو کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/149575" target="_blank">📅 19:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149574">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60465d9694.mp4?token=WgACr7PncgqpfvZV4wDGHxURcbQ6Fh4Z0dat7LSwIYuRgxbgfSIanc-CvfbR-IY6ZtOPL-AMk9iGgfqz3xheN2O2Wprm5RH8LbTJKO-jaD-9P_9qbiIqro_KuobcdHMwoy15KelWx6ONS8HIvGB_tmF2eWGZudUpjUBCe_qZpxn0AO03aiPrfh2yDLbe1QqKw7S1RxfBaOzO34l1hltADRDG9BFdcxjgqB76VznRdOtqSuTvwxZwM7LAEbw0UO3yE0NAt9s_wY41bqBQa_XanPrvLGoom6CX7zQsa1hUhrYtHsACcwtHfxjQuWqQshzAY5F69eyA2OLajZNilRm77w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60465d9694.mp4?token=WgACr7PncgqpfvZV4wDGHxURcbQ6Fh4Z0dat7LSwIYuRgxbgfSIanc-CvfbR-IY6ZtOPL-AMk9iGgfqz3xheN2O2Wprm5RH8LbTJKO-jaD-9P_9qbiIqro_KuobcdHMwoy15KelWx6ONS8HIvGB_tmF2eWGZudUpjUBCe_qZpxn0AO03aiPrfh2yDLbe1QqKw7S1RxfBaOzO34l1hltADRDG9BFdcxjgqB76VznRdOtqSuTvwxZwM7LAEbw0UO3yE0NAt9s_wY41bqBQa_XanPrvLGoom6CX7zQsa1hUhrYtHsACcwtHfxjQuWqQshzAY5F69eyA2OLajZNilRm77w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من از الزیدی حمایت کرده‌ام او فوق‌العاده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/149574" target="_blank">📅 19:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149572">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
چین: از بازگشت آمریکا و ایران به توافق اسلام آباد استقبال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/149572" target="_blank">📅 19:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149571">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/819769b9dc.mp4?token=u1hzYhkybgEV-r2G0LJPdSV9UgchDTUSf6Kmcj2gMmGNcEfvwAowNsh4ukQeB6ZyNYPsmQTIXTvWIXM8zLTpoDKdFvZzRQl287ADVmsw9vJ6LoQfZNfcfYER-dZjUH2Ie3RGJnHM0Z7tRdVYIEBwAej-6-uUL6_CBGmQV7vvfm5rNOAcaIA-Z8lPurs7vU3yOfUfKX_k6jYB2frgiyi9EArGV1qriheL8dFBAgUU5JDK6pFWYGm6lpQp6hH4NEc5SXTDGrFgdd8Bw7IntOHKlYj0pal0Y1hRXSYiDSZJBiWHZKCKggWKHV8uPHdO1vv9KTkIgNvH1wRTw6bO3AemOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/819769b9dc.mp4?token=u1hzYhkybgEV-r2G0LJPdSV9UgchDTUSf6Kmcj2gMmGNcEfvwAowNsh4ukQeB6ZyNYPsmQTIXTvWIXM8zLTpoDKdFvZzRQl287ADVmsw9vJ6LoQfZNfcfYER-dZjUH2Ie3RGJnHM0Z7tRdVYIEBwAej-6-uUL6_CBGmQV7vvfm5rNOAcaIA-Z8lPurs7vU3yOfUfKX_k6jYB2frgiyi9EArGV1qriheL8dFBAgUU5JDK6pFWYGm6lpQp6hH4NEc5SXTDGrFgdd8Bw7IntOHKlYj0pal0Y1hRXSYiDSZJBiWHZKCKggWKHV8uPHdO1vv9KTkIgNvH1wRTw6bO3AemOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خارجه روسیه، لاوروف:
ما بر آزادی فوری مادورو و همسرش تأکید داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/149571" target="_blank">📅 19:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149570">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29448d7b81.mp4?token=NwQzfNVGz3T-AwvKMTmZF5eO8oGLH8PtFjcxovdwu2qwzLnJP4xwIXsoItXmGlLc4z9RE7dob2Nkg8vS_zwFFN8aVYzzX_kxp6NvHpsAm7GrVxCC41V63J1p8PFpDEy8AuApDK8gVLnPgHzqej0VVD4wB2VXcR0nH6NJacgyRVIGdwyngAdBiDB3dKiv-1VemVgUL_LdC9sWOHBSGOxEOR0_f-CNx7IlGABMUxxaDnahEVJ7hFeiLoIMQaZlA6YV3UsKSKXYrpmJ5CEngXn9S864mqv3oY8q99E_vJo6282uOm8iV7On00tvG6Npz2NFnAmssp-I1ROUkSMJSl0qaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29448d7b81.mp4?token=NwQzfNVGz3T-AwvKMTmZF5eO8oGLH8PtFjcxovdwu2qwzLnJP4xwIXsoItXmGlLc4z9RE7dob2Nkg8vS_zwFFN8aVYzzX_kxp6NvHpsAm7GrVxCC41V63J1p8PFpDEy8AuApDK8gVLnPgHzqej0VVD4wB2VXcR0nH6NJacgyRVIGdwyngAdBiDB3dKiv-1VemVgUL_LdC9sWOHBSGOxEOR0_f-CNx7IlGABMUxxaDnahEVJ7hFeiLoIMQaZlA6YV3UsKSKXYrpmJ5CEngXn9S864mqv3oY8q99E_vJo6282uOm8iV7On00tvG6Npz2NFnAmssp-I1ROUkSMJSl0qaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عملیات‌ نظامی گسترده‌ای علیه ایران در راه است
؟
جک کین، ژنرال بازنشسته ارتش آمریکا:
"عملیات نظامی اجتناب‌ناپذیر است ... حماس در حال بازسازی خود است. هزاران نیروی جدید جذب کرده‌اند و در مواضعشان ذره‌ای تغییر ایجاد نشده است ... حزب‌الله نیز با وجود ضربات سنگینی که متحمل شده، همچنان به اهداف خود پایبند است. ایران در اینجا مرکز ثقل ماجراست. اگر این مرکز ثقل را از میان برداریم، نیروهای نیابتی نیز در پی آن به تدریج تضعیف خواهند شد.
عملیات نظامی اجتناب‌ناپذیر است. این روند شامل
محاصره، فشار اقتصادی و همچنین عملیات نظامی گسترده
اسرائیل و آمریکا برای پایان دادن به این وضعیت خواهد بود؛ عملیاتی که قرار است زمینه لازم را برای فروپاشی رژیم فراهم کند.
عملیات‌های مخفیانه موساد و سیا
نیز برای تشدید شکاف‌های درون رژیم و همچنین تقویت مردم ایران برای مقاومت و، بله، دست بردن به سلاح علیه این رژیم انجام خواهد شد. فکر می‌کنم مسیر احتمالی ما همین است."
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/149570" target="_blank">📅 19:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149569">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBhf8AOnXDrqYp0gzYWllbzpbf52aE8nKgW9mragY3YQTdLechoV0fhLR_IM4-m8T-rAVWn5kO-P7f2WiVzCD4p8s2WMnutbBMxyflsiWizJ-couR2pp3t5Yggz6PL6NSuk3lfgYj5t5o_7gy27dVAo7tQ-vR2-Lx_3oNMHyPWxx2jC5TTispcrhZ1hfbUFlDb0s1PhYnCVqSIwpYMaOr5LnjsFIAyPPNQtKbv382jINuKmRtXsmFNHz5NKWsh-zgVu9oKFzjmUhKNqtFwxNPXiboLjetmxwl0G0hI8Siw4ylwwBYWsn-3u0TdMZ2SCoaF-N_6pgbQfdnO5hwNZCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکوتراست، دنبال بهترین کارشناس‌های فروش ایرانه
🚀
✅
اگه
ساکن تهرانی
،
پورسانت بدون سقف
برات مهمه و
شرایط زیر رو داری
:
فن بیان و مهارت ارتباطی قوی
🗣️
توانایی مذاکره و متقاعدسازی
🤝
پیگیری بالا و نتیجه‌گرایی
📈
توانایی برقراری تعداد تماس‌های روزانه در محیط Call Center
☎️
روحیه کار تیمی و مسئولیت‌پذیری
👥
علاقه‌مندی به حوزه فروش و ارتباط با مشتری
❤️
💫
همین الان رزومه‌ت رو به این آیدی بفرست:
@EcoTrustHR
@EcoTrustHR
@EcoTrustHR
@EcoTrustHR</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/149569" target="_blank">📅 19:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149568">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRGPccY_AMSjhjVMk9m7JvZgC3rHEdipsYcOYpVkaqZqRb2Ko2_NipcgjHjjiLZKZWhtVpATEmArO-iWuqARaVD_zLa1MfJDIkgS53LCoe7Rfygj_9XFQFpFutGbNrt4W3n0F6yEIUAUwK7jJ01QYZrfZG95tungPRbcP039EfxHGTKA53hRLq9IZakysWTa8up8yzPk7XBcRIWlgjSxvV1y0aGsAr77HiZMBjCiQgCMRBrwSBaHMq_3nIvtlfy-mHgKivdfN-IwvGKDmdgD2GSMv15g8H1bFZVAzxcjHsFK0u8sK9SPXpgPZ1evxQyu0ZvkXrZbrvzQzBAvLF0JlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فووووووووووووووووری</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/149568" target="_blank">📅 19:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149567">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فووووووووووووووووری</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149567" target="_blank">📅 19:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149566">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
محمد مهاجری: کمتر کسی از میزان علاقه من به سرلشکر محسن رضایی و لطف متقابل او خبر دارد.
🔴
با این حال خدمت این عزیز عرض می‌کنم حتما از مشاوران رسانه‌ای و سیاسی فهیم و دوراندیش کمک بگیرد.
🔴
نه فقط برای آنکه حرفهایش در خارج درست بازتاب داده شود بلکه برای اینکه مردم خودمان هم بفهمند منظورش چیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/149566" target="_blank">📅 19:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149565">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7a35fd24d.mp4?token=bjZpezGbv_0oJteORXlvapIX0zyYphH1YaH4NfKJVhLHVrW4JljUVDapVZckPOZPQFfGl8c-QlmznT2mmX-wt-dFC4ZVD5xtYai_5BbaJMP6SYAA227qOTiYokmm8WizrGKgwYGF0Wc76qVp8wZzY8NBXxD3ULWXdvuVVOs2c46XpgULxInIAiTB9Eh5hHO8F_ZabILSJ_PLtnfMU6mZ4sz5hqyq6Ga4awLpJYKOD7j3tZ7qHS84AcQL6pL2ggaGjhDmYRS48UQJt6a5a8PpTd10gQoerVR1Qwpj_EFxH8zI7VY-7HSS3z2IxaTxgMXMHrfaUcfwm3CVxBk_X8EfRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7a35fd24d.mp4?token=bjZpezGbv_0oJteORXlvapIX0zyYphH1YaH4NfKJVhLHVrW4JljUVDapVZckPOZPQFfGl8c-QlmznT2mmX-wt-dFC4ZVD5xtYai_5BbaJMP6SYAA227qOTiYokmm8WizrGKgwYGF0Wc76qVp8wZzY8NBXxD3ULWXdvuVVOs2c46XpgULxInIAiTB9Eh5hHO8F_ZabILSJ_PLtnfMU6mZ4sz5hqyq6Ga4awLpJYKOD7j3tZ7qHS84AcQL6pL2ggaGjhDmYRS48UQJt6a5a8PpTd10gQoerVR1Qwpj_EFxH8zI7VY-7HSS3z2IxaTxgMXMHrfaUcfwm3CVxBk_X8EfRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الونیوز خطاب به کانال‌ دارهای مخبر
😂
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/149565" target="_blank">📅 19:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149564">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYUNHn45PNkmxkLTGwCJIQY8Ts82jx8ajG92ZSlYPh_T1pK9QBrjqm_g7TKnJUm_QM1P3hBIppAHQk0dRELt7kRqQIt-64xJ9zVrwIOuPmp5fHeniLcf-yiJh1e4nP9H-JjaVJV_9s5YArGWQt7kk7EluupF4FKqkVoP7TvXFdhUjJEW7yMuMMKyv7xkHpd7glIczNrjgSmOpDzy31ZjUQSgtUt4Gwe8iKNxbPsFm_wMt5BwuL5yQ6FXaW0zmVAVRnNpL4ooAIAoWRCcPNDRcOvmUaGT99ZE6LMGwJsMXiiZrQRdvCRBYVXWIvqhXTJn2WRAY1BkYTLoQ7bM-QXeGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی:
به نظر می‌رسد ترامپ تحت فشارنتانیاهو و متحدانش برای تشدید تنش، پیشنهاد ایران را که مبتنی بر تفاهم‌نامه اسلام‌آبادبود، رد کرده است.
🔴
اگر نتانیاهو تصور کند که درانتخابات شکست خواهد خورد، ممکن است برای به تعویق انداختن رأی‌گیری یا ایجاد فضای«همبستگی ملی در شرایط بحرانی» (پدیده «حمایت از پرچم» یعنی همون کاری که خودمون میکنیم)، به دنبال جنگ باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/149564" target="_blank">📅 19:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149563">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad8b3ef10.mp4?token=DSLrlI8kJWEw0FqD0lMA4heJ2EbCIPGCAPP3a-QdF6wKg2_z8rYjZIAOcjKdxFQRPAxCxJBhMyf-xQbVOH7WJZPnma5B3EKrorQqKiNvcu0W5hT8HwNvvOJsbiUwVMpo0LBnaYriFxzBOmOFMO-ZT12ieqi5xYA4TwEv_TIrDPMrr9euQoPDXyc5btHGtFoahZXl4MIjQ1LNTH72Gr9Xb-42feQluqeyiZGnFM8qAjkQioo3j45xBATjk-x-a0dO27uMPnRJ0lp3ej2MR-CRzoTWY7EOorGZOJzSo7FMpnDpDUA4ZTD8ngJQKGrNZ8oL8fQ4ilNh_42B8BwaRnlTRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad8b3ef10.mp4?token=DSLrlI8kJWEw0FqD0lMA4heJ2EbCIPGCAPP3a-QdF6wKg2_z8rYjZIAOcjKdxFQRPAxCxJBhMyf-xQbVOH7WJZPnma5B3EKrorQqKiNvcu0W5hT8HwNvvOJsbiUwVMpo0LBnaYriFxzBOmOFMO-ZT12ieqi5xYA4TwEv_TIrDPMrr9euQoPDXyc5btHGtFoahZXl4MIjQ1LNTH72Gr9Xb-42feQluqeyiZGnFM8qAjkQioo3j45xBATjk-x-a0dO27uMPnRJ0lp3ej2MR-CRzoTWY7EOorGZOJzSo7FMpnDpDUA4ZTD8ngJQKGrNZ8oL8fQ4ilNh_42B8BwaRnlTRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست
اکانت ریاست‌جمهوری ایالات متحده آمریکا در فضاهای مجازی که فیلم‌هایی از انهدام تجهیزات نظامی سپاه و منهدم کردن بیت رهبری گذاشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/149563" target="_blank">📅 19:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149562">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fn2D9BdMEEyT1mttbYYG-5cBDJBEYn_af9S-4DFJKKDdNeYeOXyICegN7ryIzt_pbbcRbXOU87rOCp4kR8mqI6qe3XWt72vbmshwgbhPj5mERoNMagJ7nIYoQ7Eukr2j3KCYYBnad2oVfpbfGUO5iyDatRDbTToU3i5E5ypl048sBJQZjTgGNpgH4YN3kGGhaUmpYKYpL6wB63hyt-EtOus5kzCUz0ipwP5hj2L0ZbAgCaYGny7Kh48Md5xxtf3HBzXkI_0VpM_c2olZ53ocycHtAE8p4SIsXElMTioTFoKocg7ps-uqOm0jTeJ1vVE64oc450wjUeuS-8NFJ0SOlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
واردات سامسونگ و ال‌جی آزاد شد اما محاصره‌ایم
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/149562" target="_blank">📅 18:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149561">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihH6mU-BvJad3DzuFzljpstas8Z3zfZeKhDMKpclPqrcANEtdpQ_L0ExoKkzLRBI800F64cmNykpxBZxa4eS-MtV0qMI1zAskjmgYnM3dH78xgZjOzXrXQwCOrYb22sKKy6uBxf5_1zKXm7C2GkOsfGtimW79xVM3TFjirUJaaNIGYkuEnasbCbM4TZRx3w0CJxTHJKdVX4zqbhyhfZBzDALaROG6pKhCTdHSuMul8S76aAAFg5Eyrky7kOoRZQKHWFB37K59IUVB6ySAEbh8jlD8dH-D95RCBtbSubdpstAC8Z4PMYus_8guEgQ_hI0WMqS5_Zd8gtOPEKvutnbeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: من یه پزشکم خب؟ آقا مجتبی تونست ۷ساعت رو زمین بشینه و بامن حرف بزنه پس سالمه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/149561" target="_blank">📅 18:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149560">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رسانه‌های آمریکایی ادعا کردن، نتانیاهو داره آماده یک حمله تنهایی به ایران می‌شه و اگه حس کنه وضعیت انتخاباتی خوبی نداره، جنگ رو شروع می‌کنه   @shahab_gold_trading</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/149560" target="_blank">📅 18:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149559">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e294531f.mp4?token=g9_fOFEaLKXXgDcHGMzJeeYX5XWCLRQ2IzyJwQ2fPFoWPCovkd1jBgG8NgV0vTJKaUr4iR4pfKjHsAsU_3eHLuN4AJyi3rmTaYq7sn-TIjiyZWkcfD8eBoRN7KgL6luwOgZgwBiMrm0EVBtEccaFOLTmweCvDnEsjL1xbmP9gEVgtxo_TS_kWeUihlaO_NxcIggWBW0C60cRms-6ABGyr5FFIlLoVblh5JkE-kIioZEF6JtIv9dsYzNQmIk10i-A_3qWsKx_BGmvvSDro0KPpFDbBQKFPJQ70U4g4325IwM4dU1bgH2BZX04ufFxql6xz0I3ZzOUJIpy3psHi_l7YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e294531f.mp4?token=g9_fOFEaLKXXgDcHGMzJeeYX5XWCLRQ2IzyJwQ2fPFoWPCovkd1jBgG8NgV0vTJKaUr4iR4pfKjHsAsU_3eHLuN4AJyi3rmTaYq7sn-TIjiyZWkcfD8eBoRN7KgL6luwOgZgwBiMrm0EVBtEccaFOLTmweCvDnEsjL1xbmP9gEVgtxo_TS_kWeUihlaO_NxcIggWBW0C60cRms-6ABGyr5FFIlLoVblh5JkE-kIioZEF6JtIv9dsYzNQmIk10i-A_3qWsKx_BGmvvSDro0KPpFDbBQKFPJQ70U4g4325IwM4dU1bgH2BZX04ufFxql6xz0I3ZzOUJIpy3psHi_l7YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع بیکارها و الاف‌ها در فرودگاه مهرآباد و شعار علیه پزشکیان و عراقچی
🔴
این‌ جماعت معلوم نیست درآمدشون از کجا هست که هر روز ول هستن از اینور به اونور
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/149559" target="_blank">📅 18:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149558">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) : در پی شناسایی تسلیحات که نیروهای ما را تهدید می‌کردند: ارتش اسرائیل یک انبار تسلیحات متعلق به سازمان تروریستی حزب‌الله را در منطقه سجد در جنوب لبنان هدف قرار داد
🔴
ارتش اسرائیل امروز (شنبه) یک انبار تسلیحات متعلق به سازمان تروریستی حزب‌الله را در منطقه سجد در جنوب لبنان هدف قرار داد.
🔴
این حمله با هدف رفع تهدید انجام شد. در این انبار تسلیحاتی نگهداری می‌شد که برای آسیب‌رساندن به نیروهای ما که در منطقه امنیتی فعالیت می‌کنند و مختل کردن فعالیت‌های آنها مورد استفاده قرار می‌گرفت.
🔴
ارتش اسرائیل به اقدامات خود برای رفع تهدیدهای فوری ادامه خواهد داد.
هرگونه استفاده از خاک لبنان با هدف آسیب‌رساندن به شهروندان اسرائیل یا نیروهای ارتش اسرائیل، با قدرت پاسخ داده خواهد شد.
🔴
ارتش اسرائیل همچنان به توافق میان اسرائیل و لبنان متعهد است.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149558" target="_blank">📅 18:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149557">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الان عراقچی میاد میگه شروع خوبی بود</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/149557" target="_blank">📅 18:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149556">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
آکسیوس: مذاکرات همچنان سازنده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/149556" target="_blank">📅 18:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149555">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
اکسیوس:
در حالی که ایران می‌خواهد هرگونه مذاکرات را بر موضوع تنگه هرمز و محاصره دریایی آمریکا متمرکز کند، دولت ترامپ خواستار آن است که ایرانی‌ها با امتیازدهی در موضوع هسته‌ای موافقت کنند.
🔴
مذاکره‌کنندگان آمریکایی در جریان مذاکرات روز سه‌شنبه به ایرانی‌ها اعلام کردند که ایران کنترل تنگه هرمز را در اختیار ندارد و بنابراین نمی‌تواند درباره آن مطالبه‌ای مطرح کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/149555" target="_blank">📅 18:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149554">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d83c735408.mp4?token=fy21mQoK-WsejSd09pimvidWPHY3pd2h76JKKFWz-CpXTn5s-rAa_tigBqq_aEgbILKWKEg2z-YOzknntcOag6YMoH0azvq4U2_lQKuyUfgBtdjUO972EA-kyFe9TY-Ed498aNXa8DB8f4dGpAQvjpKN9Z6YS6qG32IzXmt3tlZ3SzAzdlxqR8KrcQKHjQCVp1jBeO-pATFt4nH378K-mt9OwniUikvHqPzqbkYdlioOIz2oO9maxx6NRokVrPmbcyk_TiaFJu47S19jUvjmkKIBLcq3ufLrPsYG7IiBJdzPaw46pbakaQMKiaUd8pX_-pE6sKGL5Zqn_FMZXKJ8PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d83c735408.mp4?token=fy21mQoK-WsejSd09pimvidWPHY3pd2h76JKKFWz-CpXTn5s-rAa_tigBqq_aEgbILKWKEg2z-YOzknntcOag6YMoH0azvq4U2_lQKuyUfgBtdjUO972EA-kyFe9TY-Ed498aNXa8DB8f4dGpAQvjpKN9Z6YS6qG32IzXmt3tlZ3SzAzdlxqR8KrcQKHjQCVp1jBeO-pATFt4nH378K-mt9OwniUikvHqPzqbkYdlioOIz2oO9maxx6NRokVrPmbcyk_TiaFJu47S19jUvjmkKIBLcq3ufLrPsYG7IiBJdzPaw46pbakaQMKiaUd8pX_-pE6sKGL5Zqn_FMZXKJ8PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: باراک اوباما اخیراً گفته است: «اگر برای دو سال زنان را مسئول همه دولت‌ها قرار دهید، اوضاع بهتر خواهد شد.»
🔴
دونالد ترامپ، رئیس‌جمهور آمریکا:
«من زنان را دوست دارم و فکر می‌کنم فوق‌العاده هستند. اما این واقعاً چه حرف مضحکی است، درست است؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/149554" target="_blank">📅 18:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149553">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ایرنا: عراقچی فعلاً در نیویورک می‌ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/149553" target="_blank">📅 18:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149551">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
تیرخلاص ترامپ به تفاهم‌نامه با ایران
🔴
العربیه: ترامپ اعلام کرده که امکان بازگشت به تفاهم‌نامه با ایران وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/149551" target="_blank">📅 17:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149550">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=AzcBE3bPkwii_qJMvLlkHByDbW16ycZrk6mA4PvlHxAYZXq5tdS_zMSQi7CGZxGZlhAR5JLHBmslT2-LqHvVXrNm-IjeY9gJnwreYTssonXnBoN__8t9H1AnBzZgPrenpoyzWMcGLWXscGuyRn85JCcdzT9jfSI7j905oKpkADU77ALP7BeU1bQujGwUgcKn0grEEszb2f2AimGzk4jYWqu0awy7ENds-nWT5oCMfDvpnlKhf5n7Ts6S0FH94ThqfJK3FGfObzcmguQg0MT97Z9vZBwFHKcWkZmWcbqay9qrGlyuIdWFOvYTnsonYxAGMOCt1GSXj-v5Pw8hE5q55g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=AzcBE3bPkwii_qJMvLlkHByDbW16ycZrk6mA4PvlHxAYZXq5tdS_zMSQi7CGZxGZlhAR5JLHBmslT2-LqHvVXrNm-IjeY9gJnwreYTssonXnBoN__8t9H1AnBzZgPrenpoyzWMcGLWXscGuyRn85JCcdzT9jfSI7j905oKpkADU77ALP7BeU1bQujGwUgcKn0grEEszb2f2AimGzk4jYWqu0awy7ENds-nWT5oCMfDvpnlKhf5n7Ts6S0FH94ThqfJK3FGfObzcmguQg0MT97Z9vZBwFHKcWkZmWcbqay9qrGlyuIdWFOvYTnsonYxAGMOCt1GSXj-v5Pw8hE5q55g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدا و سیما:
اول ما پیشنهاد آمریکا رو رد کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/149550" target="_blank">📅 17:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149549">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlbJZ33wMiZwWu6srV4V0n2kNoIbEX-nxWu5mWRfdEg4Ks8y79PwTTw4AX4lsN7zUOoI8ugtx9-pHtT_U33A6O3JQL3oy52emHhTk-s5m_bw3IOHmu9sC0oBvo6lTDHIXiJ4PH0M8ZUDyMMZo5Q3xBlVuCQXS0Vp5DbvilXJ1qewDv-pkd4nDdlmRUenkhO-N-RRcw2a8_F0_aO3Nzeu5YKvfyHtJWr8phvnkf-PsHHY0l0aYycNDChEzRAUN7op1tGY9sSg7BhOH9EZw89Y8Seh8gYhp4HP3L1VLnisf2U4MNOwz2pidUHk2yHGrpSfJdIqn35hgCPw-yeQOqQPtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۴۰میلیون بشکه نفت طی روزهای اخیر از تنگه هرمز رد شده و عملا تنگه برای همه گشاده جز ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/149549" target="_blank">📅 17:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149548">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/753abf70cb.mp4?token=gk1X0w7y7kqcZI408hk7ZBUWmhKwFp83-ecqhx1nKi_OuO9qQ0oZPUwyyg1mBVfq91YD5Tsy2Iptn7lGewSUfUyVnQw1Auu6zEMtNwvwk81xegDcJMTFeMu-n9eoYUUXnRMsR9f0xosEsXcG58KkrElDNGAMQBjgCYBM6Gm1MH-aXzpdxnpKEKlIeHWANXG9SiFU8wvBUyUsJhxv90sldRSPHKx6eCVN8jDnfUlj0A6wrIcQjnoNvI_VHnJh620AiBZ4tKqaOfEgWdwZ5H5gtIKHzqQS4HQk6-PtVUvzO5H55D0RDYyryjUeWO7dFv2lz2t2ZYBpVjoPHqABJ7KwzqKsaww6RciKfbc_ftS0_6MG5iBwt7tsfXem9K2xcZFeAFz2W9fFXjjS80nscPzVfDy3VuPmqZ2WraN6N6PLTZRKblUV_9QBmUgsMse-amzl42z9kqAZTp4pYgRjsOPk7MU9G_ReZFz-NQQ5iohdd8Ds3Ey9eQlOpuu7rP0akWukrMJt1KcnKC4UfV9C7nyREMvOqcz6DIkhhAG-y4b7I_gMwNV9sFtkZRllzG9ku0lHjs4XDFBZzMTvb6pf_RmS3sGK1OPqs1ZvS8E6vEsAEIWFA_vHlG6VbB9GxsJ0P3FBAGsRhzWHiX_azdudwQz65Me1gtu_Hj1hfTk0Nbf4KGc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/753abf70cb.mp4?token=gk1X0w7y7kqcZI408hk7ZBUWmhKwFp83-ecqhx1nKi_OuO9qQ0oZPUwyyg1mBVfq91YD5Tsy2Iptn7lGewSUfUyVnQw1Auu6zEMtNwvwk81xegDcJMTFeMu-n9eoYUUXnRMsR9f0xosEsXcG58KkrElDNGAMQBjgCYBM6Gm1MH-aXzpdxnpKEKlIeHWANXG9SiFU8wvBUyUsJhxv90sldRSPHKx6eCVN8jDnfUlj0A6wrIcQjnoNvI_VHnJh620AiBZ4tKqaOfEgWdwZ5H5gtIKHzqQS4HQk6-PtVUvzO5H55D0RDYyryjUeWO7dFv2lz2t2ZYBpVjoPHqABJ7KwzqKsaww6RciKfbc_ftS0_6MG5iBwt7tsfXem9K2xcZFeAFz2W9fFXjjS80nscPzVfDy3VuPmqZ2WraN6N6PLTZRKblUV_9QBmUgsMse-amzl42z9kqAZTp4pYgRjsOPk7MU9G_ReZFz-NQQ5iohdd8Ds3Ey9eQlOpuu7rP0akWukrMJt1KcnKC4UfV9C7nyREMvOqcz6DIkhhAG-y4b7I_gMwNV9sFtkZRllzG9ku0lHjs4XDFBZzMTvb6pf_RmS3sGK1OPqs1ZvS8E6vEsAEIWFA_vHlG6VbB9GxsJ0P3FBAGsRhzWHiX_azdudwQz65Me1gtu_Hj1hfTk0Nbf4KGc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا:
«من اخبار واقعی می‌خواهم و عاشق رسانه‌های آزاد و مطبوعات آزاد مثل الونیوز هستم.
🔴
چیزی که دوست ندارم، رسانه‌های جعلی هستند؛ مثل شبکه‌هایی مانند CNN که بینندگان کمی دارند، یا MSDNC که فکر می‌کنم حالا نامش را به MS NOW تغییر داده‌اند. می‌دانید چرا تغییرش دادند؟ چون میزان بینندگانشان بسیار پایین بود.
🔴
چیزی که من دوست ندارم، اخبار جعلی است و آنها ۱۰۰ درصد اخبار جعلی هستند. در دو سال گذشته، بعید می‌دانم حتی یک گزارش خوب درباره من منتشر کرده باشند؛ در حالی که من در انتخابات با اختلاف زیادی پیروز شدم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/149548" target="_blank">📅 17:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149547">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: آنچه آنها می‌خواهند انجام دهند، این است که تنگه هرمز را فوراً باز کنند. می‌دانید چرا؟ چون دارند از پا درمی‌آیند.
🔴
آنها پولشان را از تنگه هرمز به دست می‌آورند. بنابراین، خودشان خودشان را گول زدند.
🔴
آنها گفتند: «بیایید تنگه را ببندیم و برای جهان مشکل ایجاد کنیم.» بعد من وارد ماجرا شدم و ما بزرگ‌ترین محاصره تاریخ نظامی را ایجاد کردیم. این یک دیوار فولادی است.
🔴
حدس بزنید چه اتفاقی افتاد؟ آنها حالا دیگر پولی ندارند، چون می‌خواستند تنگه را ببندند.
🔴
و من گفتم: «بسیار خب، ما هم آن را برای خود شما می‌بندیم. اما بقیه می‌توانند از آن استفاده کنند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/149547" target="_blank">📅 17:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149546">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ: ایران خواهان توافق است و من هم از توافق خوشم می‌آید، اما این پیشنهاد غیرقابل قبول است.
🔴
ایران با بستن تنگه هرمز خود را در مخمصه انداخت و ما بزرگترین محاصره تاریخ نظامی را بر آن اعمال کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/149546" target="_blank">📅 17:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149545">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏
🔴
فوری/ترامپ: پیشنهاد ۷ شرطی ایران را رد کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/149545" target="_blank">📅 17:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149544">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏
🔴
فوری/ترامپ: پیشنهاد ۷ شرطی ایران را رد کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149544" target="_blank">📅 17:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149543">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
العربیه به نقل از یک منبع آمریکایی:
ترامپ به تیم مذاکره‌کننده ابلاغ کرده است که بدون اقدام اولیه از سوی ایران، هیچ توافقی در کار نخواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/149543" target="_blank">📅 17:17 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
