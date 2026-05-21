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
<img src="https://cdn4.telesco.pe/file/kKReu-6fyG43823cOSG1LFmMQu1WqE6uhWVdCuL8pdBt5hMQr_CAABJFaYak_OMt1gOw5yyTaevRWbDz9oun0YV8Xt7RPqU5mx16ijjN_gwBYW9sB8VZPePANvBZEUuqUQEKuSxd5ya8ilMbxxXvunjarm5jelwEZo1trjdg5s0GsD-j4S57hYKVrTGrkZD9azz4NiTkwiv4VHkaJUn3Lg79WkGfASoujw06dwbquidT-PUNS0GrVHASUtY8vLC_IXockYAw3NxoG88UAnznz2RecnvhDjtRY2YHKOz3l5RxNGhyPBZGYgKz9MNVCfrBSkc_Nd_0kX40OvfxB06Nnw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 141K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 17:27:22</div>
<hr>

<div class="tg-post" id="msg-64990">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyXOcgMDloepFRV4LkQhkXXLW6Lznj_FTM06lpWkKnEk3UC4Ekhd_j1rhryJntUzhOfBsd0Krmw938kqJCslo5rHdBT1NBfM2FzItDikPfOqI6pAU_5MM2YQ43DoWeQbKhe04fjzruZLjsEWFIh34vZ8P2mlcbiFTwanI_GZDhLktadmbYl4W7VcO1TGOvP5mb6Klbc2xKeafPb2WlW8FiVRZbJkFmkAbH2ZY-EwNpgHwiE3vags65M7x99JRJdpdm7dwsp8Wm7CceLyXvKk4Z2M30Laktaw9b9Pap4LCJiQiizWwjeMxsUEKDcgZ8ojMxWKp9fHvsVddHqS0nSHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ یه پست از نشریه نیویورک پست بازنشر کرد که تیتر خبری‌ش هست؛«چطور میشه تهرانو تو سه حرکت نابود کرد»
@News_Hut</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/news_hut/64990" target="_blank">📅 16:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64989">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAOoxdRcARPFRjZ9ziZ9OmBiUgigH4N8ZqZo4TbrHRW5w4DVDh9Msb2ByS1CFw615V4aGcyFu0EF7vgBsZFj-Ubvn_cE9y_YYyMILXVlU8zGcgO5twIiwi5GdZ463Ea7D-jDFi0kUCRGReXJ7VgS7CGL8lUK4SVzwoFf1rqp9gPRa3t85MWBJJoa-O5BROS-qETFOFY0JrREbJcGUtHh0hJ-1PJrc--HaMMY7gNmXwolzvAQisZlsrqBnVvr8Ig6oGmcBavH1A5hmNh0f-BjKLkVwItuIgRkImuQJHMBD2LCuJv_Hs7wfnJYiZy7M-2NWvahVgHUcdi2jk2xmA8QBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ جدید هزینه‌ ریجستری گوشی‌های آیفون
ریجستری آیفون ۱۷پرومکس، ۱۰۴ میلیون تومان!!!
@News_Hut</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/news_hut/64989" target="_blank">📅 15:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64988">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eppa0wiVSCzuY078ThxqJoExD6kfWme_QUWBZolYoqp2R_Tki5YlrRUcEXpYGyrKuLK49IGAeU2_wV99yHm0N5-TOYr6jEVlcRMzgcL7DD0sDbPsVYnAwaDWPBPaEMyair9Va_E4AM-nshDvtdIaRIULGraXiF4QxHdHkjjY4BeCyxCgCxawZsvx3JICwJJXI1RCHGJFZGxyrioSiT5JP8DTtI89l5m2NWZDoB0I4CDv6oQiVbx1syNRcCjjWAXXQuRkoRBPSJ34SUq2a-02pb9FBuN72B_QHQ5aX7B-SVaVtg86yvbSmvE2V3czSpHSOsoLdWHDvVan81DgarlM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فهرست کاخ سفید از مهم‌ترین دشمنان امریکا که در دوره فعلی ترامپ حذف یا دستگیر شدند:
رئیس‌جمهور ونزوئلا - مادورو
رهبر رژیم جمهوری اسلامی- خامنه‌ای
معاون رهبر داعش - ابو بلال المنوکی
و برای رائول کاسترو رئیس‌جمهور سابق کوبا (و برادر فیدل کاسترو) کیفرخواست صادر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/news_hut/64988" target="_blank">📅 15:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64987">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
📰
رویترز: منابع ایرانی می‌گویند رهبر معظم(مجتبی)اعلام کرده است که اورانیوم غنی‌شده باید در ایران بماند.  آمریکا می‌خواهد اورانیوم بسیار غنی‌شده ایران به خارج فرستاده شود مقامات اسرائیلی می‌گویند ترامپ به اسرائیل گفته است که این اتفاق خواهد افتاد دستور رهبر…</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/news_hut/64987" target="_blank">📅 14:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64986">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
بندرعباس ۴.۶ ریشتر زلزله شد
@News_Hut</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/news_hut/64986" target="_blank">📅 13:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64985">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Te5-zBbsnpOEieuUCJqxZ3eNM0tnBoEs4pcge4PBrRd1HpvaO-iDz2m4f5lzNmK30hyFxi-vv4wJRysS1PGgOhq1C9fU8h0TOT-W41qow0r3L6u-I3w3tlp_J3FZ7dWAumoWdPZH7aVkfqZ2ItuoviLXDnF3FwL5kONv-gsavliOPl_Ss6nRrTytRNCVvsSD4E5ek7-n7suHrJwAUuTpB8QxALTl-LlJacZKTfuJv8O4sT1jsWYFsUUu7BHC4kYEulzKongEKzFIGt6sTyydg-MVgVK14Q28WkNRCMbRlJ8wa5JRQ7inO8V1bv8tovFDefylnoH41jlktNuD6YIQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شریعتمداری: تا زمان شکست امریکا و کشتن ترامپ تنگه رو باید ببندیم
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/64985" target="_blank">📅 11:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64984">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: اگر فرمانده ارتش پاکستان به ایران سفر نکند، توافق نهایی ممکن است ظرف چند ساعت اعلام شود  @News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/64984" target="_blank">📅 10:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64983">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خبرنگار: آقای رئیس جمهور خیلی از خانواده ها در آمریکا نگران گسترش هوش مصنوعی هستند، نظرتون چیه؟
ترامپ: هوش مصنوعی عالیه، ایران نباید سلاح هسته‌ای داشته باشه :)))))
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/64983" target="_blank">📅 04:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64982">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: کار برای نهایی کردن متن توافق میان واشینگتن و تهران به طور جدی در حال انجام است و دور بعدی مذاکرات پس از حج در اسلام‌آباد برگزار می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64982" target="_blank">📅 18:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64981">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: کار برای نهایی کردن متن توافق میان واشینگتن و تهران به طور جدی در حال انجام است و دور بعدی مذاکرات پس از حج در اسلام‌آباد برگزار می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64981" target="_blank">📅 18:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64980">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SPRG3FYs-6aB33qN7O-jQmVBX4rR96RUPYukjTBnimWXzFGXq92rjtg-Uxf78zhI0HQmlPQZBsMEQqktESS07f5HKjkeO_h4_8tozT5zzJZwgQCJwKmBgGQUh9-07fInPceut6tvbhPbFMnfjY45vzLdprHqCwUST8agTkrmAnxs8tp6oHyfZUqzwz_pU2ru9Yxor05Swg6988tLnDHba2qdcv5nuWOAvVqrq0aLbHZKOrUx83TI5JPWMUDB5G6cNSHT2TT4uEc8ee2hXwY-0LH5fpqEWdDeMKC-gekq6tCUxnXa1xYS7pcrRuUFNN-HQqnYml784revR72ywFUlyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای مرضیه حسینی خبرنگار ایرانی کنگره: یک منبع مطلع اینجا در کنگره به من گفت که ترامپ روزهای چهارشنبه یا پنج شنبه پیش رو، به ایران حمله خواهد کرد.
به گفته این فرد، این حملات برای یک عملیات “دو تا سه روز” متمرکز خواهد بود و به مراکزی با هدف بازگشایی تنگه هرمز انجام خواهد شد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64980" target="_blank">📅 13:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64978">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dl1e29SdQg-COcKZUwo5S5Mx0FhJhvgNtdr3wVp2dOF1hO4owCp5Un9gkn3FbEBmSZhNNDR_tD5fi89ZNtuZMi4_2NL0ozQzx-nLWrHiyVCOF9I7VJdLJjFqGpVs9G3Z_cI6qfqgGN6ON067bbSfYcnxKkJtF3r0e0ejdgJJYPa7dOHjpw2maxB_h0Akjo1SvuPD9aWy8PkxCKPCP1MNRFkROfzAkDsYSdKDxQF9BAkWRJJ4LQXJTnpSJYFB_JJydbm3oSsDCRnSVo7Opd9bR04YJdLeI5ZT9pleH5QjaHMy_lki9hopbJ98KyV4smt4BxMM7hrdUTm6gBkNOw_ZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWpJdVlUHveD48giNN8ySyngZCZHG3sQGcFafl1FBhUaul_nE8i_z7oG_m9DGNsZxFYRX6I4n67CyPskQShXKb_EUDM8gg6inPSctQKZ9PSuVWOQWdVS7M5Tzp10KOaj0xpAGtVf8eyK84SKwo_XgioBWC1sgP13IxegSwPhXu_dYvmBc1D5iw90-eJT0IwOOt-mzSvfozBlSdWP5CGMwlWtkRp2Uy0fOghdNK5_drhmuoog11DWRIeqBgxhSMGE1Rb5o1FioLGu482rIj6QHEYArJSg2qHK6uquR_dLTqowUkNI1QJj6szCyWBWW9g5Zq9qyW2fyc9eP5-mNjJZgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
گزارش NBC از موبایل جدید ترامپ  به نام «Trump mobile»:
مدل T1 با قیمت «تشویقی» ۴۹۹ دلار به فروش می‌رسد و به صفحه‌نمایش ۶.۷۸ اینچی، دوربین اصلی ۵۰ مگاپیکسلی و حافظه ۵۱۲ گیگابایتی مجهز است.
گوشی ترامپ موبایل در چهار نقطه از بدنه و نرم‌افزار، لوگوی «ترامپ» حک شده، پرچمی آمریکایی با ۱۱ راه‌راه به جای ۱۳ راه‌راه روی آن حک شده و از پیش، شبکهٔ «تروث سوشال» روی آن نصب است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64978" target="_blank">📅 13:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64977">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358ed734a6.mp4?token=dFrAZxwfSyzkpSZEJ2FzA2eG58Q-GeWEWfFNFtP1Zcrz70MGTV99R8RdseUvteGOBYD2SLQWHJU2Meez9VdeyTUo_9gyN2Qc0KPPA7Lu5_jlkE2gapT1RhEaUaprTBASC18qs26Qvzhm3kr1MMk1ikPoTC6JKix0STTZrL_sEtlVNPdkLtzBIBkSPA47ubpNQ1TQ1DpI9Xi6_BxLZ1m_UOzczRE_erwmkR-FPFM_YmgVbcj53_N6ORYpxrB82gfsdTZsPCPgCOT3fxP53l6AM3EiC7oosGjkv8qNSkBJymp9vF00bb3hkneZGOQVLB7c86LISztx53F9uC7wFQFo9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358ed734a6.mp4?token=dFrAZxwfSyzkpSZEJ2FzA2eG58Q-GeWEWfFNFtP1Zcrz70MGTV99R8RdseUvteGOBYD2SLQWHJU2Meez9VdeyTUo_9gyN2Qc0KPPA7Lu5_jlkE2gapT1RhEaUaprTBASC18qs26Qvzhm3kr1MMk1ikPoTC6JKix0STTZrL_sEtlVNPdkLtzBIBkSPA47ubpNQ1TQ1DpI9Xi6_BxLZ1m_UOzczRE_erwmkR-FPFM_YmgVbcj53_N6ORYpxrB82gfsdTZsPCPgCOT3fxP53l6AM3EiC7oosGjkv8qNSkBJymp9vF00bb3hkneZGOQVLB7c86LISztx53F9uC7wFQFo9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان،عضو کمیسیون امنیت ملی مجلس:
امیدوارم خبر سفر عراقچی به نیویورک برای مذاکره در خصوص تنگه هرمز دروغ باشد!
چرا ما در خصوص موضوع تنگه هرمز باید در خاک اسرائیل و آمریکا مذاکره کنیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64977" target="_blank">📅 10:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64976">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
📰
نیویورک تایمز:  ایالات متحده و اسرائیل پیش از جنگ با ایران، طرحی را برای نصب محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، به عنوان رهبر جدید کشور مورد بحث قرار دادند. احمدی‌نژاد گزارشا در مورد این طرح مشورت شده بود، اما پس از اینکه در حمله‌ای اسرائیلی به خانه‌اش…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64976" target="_blank">📅 09:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64975">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دموکرات های احمق برای بار nام خواستن جنگ رو متوقف کنن که بازهم رای نیاوردن  @News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64975" target="_blank">📅 08:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64974">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y84fs079zHmHkk077wHgQqTxoztbl8NpjRuqlMCbXcdK5PGYThW3mDtGLLGBjmH5OcZGy217ZqvsKUN4BuuDw8T6kKu5n1UothFaWXAt6lyNJ3eek6NhH0SpP1tOTm5G1pSYdIoxDGpta9Iwuzh1kgYOGlMSsOYFzfhMYuWAl-MagiZSRr1eu6-Sovnak1cceSPe1xyCK4LofZ9gXtOXHZ6vSkL5zVnYygvRnyP7JPbgCzx02pk0B3e3De5L7xZkWZ_LC7vg5qWK7F1rUySTFwYObXmRLNClI2TJpozuJEkv4guMvLA5KQXHNUrfA_M9thHn0j3XaVPRXvSNvehiyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور لیندسی گراهام:
امیدوارم و انتظار هم دارم بعد از این چند ماه مذاکره با ایرانی‌ها، دولت ترامپ هر تلاشی رو که برای دوباره کش دادن مذاکراته رد کنه.
این رژیم ماه‌ها وقت داشت به توافق برسه، ولی به نظرم واضحه دارن بازی درمیارن
من ترجیح خودم راه‌حل دیپلماتیک هست، ولی قدیمی‌ترین ترفند ایران همیشه این بوده؛ امروز و فردا کردن، کش دادن، کش دادن، کش دادن
در مورد هر توافقی هم، منتظرم بره سنا و اونجا بررسیش کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64974" target="_blank">📅 07:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64973">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xppes16jBr6icjVEyfw_RVuywgbv9JAynjxL4z_DDKmTexdGrFDLJ71mMZFPGy4LMtnZYppTEvrCBhSoATslT-ADoHBDX1QPfO8kWdVn6JR3EiCNVDeKT4Y6-K_36_NTAg2filUeQctNQeJ-hCP1_2iOQSIuWQOugDVbMiGXYPoZK7SbT5_SibaBx2Gq6DEuE8F82FvZz8yVTRel-aX_-xd9CY90_f3baw2fJSYK2XMjSYPxenZOqZv4O6oHttWfUplvfg7Z7cHpO5juiq-2s8g4tf94LDCOfWNiEIXSQ0da-DnT5Wquu0ACPntE1ZMkg0a-S1CJuQ-Gua-xk2_S2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غریب‌آبادی، معاون وزیر امورخارجه:
امریکا میگه دستور حمله رو به طور موقت لغو کرده و در سایه تهدید می‌خواد مذاکره کنه
اونا باید اینو بدونن برای ما، تسلیم معنایی ندارد؛ یا پیروز می‌شویم یا شهید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64973" target="_blank">📅 00:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64972">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🇺🇸
اولین اظهار نظر متفاوت امریکا نسبت به حمله انجام شده به مدرسه میناب و جان باختن کودکان این مدرسه:  برد کوپر، فرمانده سنتکام: ایالات متحده عمدا به غیرنظامیان حمله نمی‌کند. مردم ایران دشمن ما نیستند. سپاه پاسداران انقلاب اسلامی در این مورد دشمن است. تحقیقات…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64972" target="_blank">📅 23:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64971">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b854a8a43b.mp4?token=mqEkkMbFOSglUgy255C635OESdE7XyevqKazRpNMpRV8t2Vd5e17E2qcZKCsuhAukCzRl3StQWXD9_B-dzwkrFwoXAXxCBT9VXXJarVbOVAd8gFfcSzhiSzE7rHbJ-x79Qwr3NHb22cFBf6wsWp0p4VgE096fIeFHgDWKEbMk6RluG4sNjuArqD2TpwThCBml3JN49MwoxKaf-VmfmCtu4-2BZvKEeSKnQjiEygYAbb0CWQkQkW0_6sIm-PVfF2Gy0NaKdF4YCruBvScAJvSxry2wOIIoszzlIkCuRCy9IQkdc1e4nhHYWLWl9GwmfPcR0VVPOgD6t3LBIfqzoJTSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b854a8a43b.mp4?token=mqEkkMbFOSglUgy255C635OESdE7XyevqKazRpNMpRV8t2Vd5e17E2qcZKCsuhAukCzRl3StQWXD9_B-dzwkrFwoXAXxCBT9VXXJarVbOVAd8gFfcSzhiSzE7rHbJ-x79Qwr3NHb22cFBf6wsWp0p4VgE096fIeFHgDWKEbMk6RluG4sNjuArqD2TpwThCBml3JN49MwoxKaf-VmfmCtu4-2BZvKEeSKnQjiEygYAbb0CWQkQkW0_6sIm-PVfF2Gy0NaKdF4YCruBvScAJvSxry2wOIIoszzlIkCuRCy9IQkdc1e4nhHYWLWl9GwmfPcR0VVPOgD6t3LBIfqzoJTSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جی‌دی ونس، معاون رئیس جمهوری ترامپ:
گاهی اوقات کاملاً مشخص نیست که موضع مذاکره‌ای تیم ایرانی چیست.
گاهی اوقات سخت است دقیقاً بفهمیم ایرانی‌ها می‌خواهند از مذاکرات چه چیزی به دست آورند.
در حال حاضر برنامه‌ای برای تصاحب اورانیوم غنی‌شده ایران توسط روسیه نداریم. این هرگز برنامه ما نبوده است.
نمی‌دانم گزارش‌ها درباره این موضوع از کجا آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64971" target="_blank">📅 23:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64970">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/64970" target="_blank">📅 23:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64969">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=sGpN4ynIbFZRkTtzEMBvcHC9zyoQZxREaSG2h7_hq9fV4yY1bKVu4BxJWMekab6wTYIrT4hFl33VO6u-4n-BlEC05Z6IWwzyaRtLMxkd-Kbcjkj-wjaiYeCiPZv-XnJKzizWQuQEXrYg1tttcbD7_nZCx3X3SQ93HoSV6XyqvRs0oEIRsX-0TzYO-vzfbFTQdgG0OzANO_XVXbIpLVpW5ztUSjZnYXHBLxHby2vaF-q5Sl9hGNmfxHIXdPjuFqjYNsE8-MnHLDfXHpgf_fmZXuh3sHXye1WCGxB7a9o_b7Al6V9W3o89bzOkoEqhDwcMBpOzi-OMJtAbTEQPkezOew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=sGpN4ynIbFZRkTtzEMBvcHC9zyoQZxREaSG2h7_hq9fV4yY1bKVu4BxJWMekab6wTYIrT4hFl33VO6u-4n-BlEC05Z6IWwzyaRtLMxkd-Kbcjkj-wjaiYeCiPZv-XnJKzizWQuQEXrYg1tttcbD7_nZCx3X3SQ93HoSV6XyqvRs0oEIRsX-0TzYO-vzfbFTQdgG0OzANO_XVXbIpLVpW5ztUSjZnYXHBLxHby2vaF-q5Sl9hGNmfxHIXdPjuFqjYNsE8-MnHLDfXHpgf_fmZXuh3sHXye1WCGxB7a9o_b7Al6V9W3o89bzOkoEqhDwcMBpOzi-OMJtAbTEQPkezOew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره اینکه ایران چقدر وقت داره تا توافق کنه:
دو یا سه روز. شاید جمعه، شنبه، یکشنبه. شاید اوایل هفته آینده. یک بازه زمانی محدود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64969" target="_blank">📅 18:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64968">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2efb45471e.mp4?token=QbCVFI9JRaS-Txhja1-RDhxy3iPHmWWGWRJoXSZnygaHmSp2zntkTNKiIoteyIwkNNEPxi2QRBmC0prG4gVB-MolqhtKjm78q0_vrOC9eroNTh7DIC1CPFuCjSeOSwQqDweGxWLJ96qiR0wO2AlcMBhjvdKcT5fsjDMpOuCrGh3XJhKmgo5k24r3NUoeoVllTCH1aRQrg-TXiSXaeZgGXON4bmBTQdrgogdurmz3r9v1j9kQxbFnhYuNAkDZ7AVko2G4gAfvWq9xVwzM2a-lxK-74vL_Rf2-zpBTDBvCJ5qgEgCbUMY5IuFlPozAuzXZ4n9AdSIHp2mooc8OOTofjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2efb45471e.mp4?token=QbCVFI9JRaS-Txhja1-RDhxy3iPHmWWGWRJoXSZnygaHmSp2zntkTNKiIoteyIwkNNEPxi2QRBmC0prG4gVB-MolqhtKjm78q0_vrOC9eroNTh7DIC1CPFuCjSeOSwQqDweGxWLJ96qiR0wO2AlcMBhjvdKcT5fsjDMpOuCrGh3XJhKmgo5k24r3NUoeoVllTCH1aRQrg-TXiSXaeZgGXON4bmBTQdrgogdurmz3r9v1j9kQxbFnhYuNAkDZ7AVko2G4gAfvWq9xVwzM2a-lxK-74vL_Rf2-zpBTDBvCJ5qgEgCbUMY5IuFlPozAuzXZ4n9AdSIHp2mooc8OOTofjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: دیروز چقدر به حمله به ایران نزدیک بودید؟
🇺🇸
ترامپ: یک ساعت فاصله داشتم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64968" target="_blank">📅 18:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64967">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:  ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم. خیلی زود خواهید فهمید.  @News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64967" target="_blank">📅 18:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64966">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9954bd7931.mp4?token=kuTiYy0k__U8YO91Inq1rxPMGveKlyL0CzwTOfkVGhzZxzBn62MSPFlyhSRdpYyQrtquEDOLqF75XjyanqD_Fw3Bst449QLO4_3VWapvfZ6MgajeolkXa1mhijLUnSJVDKNT-G7uvF1kYEheqdZ5W8MyJ7QmTtyNjBLEOblnkAmnWws6pvJnRxOBt_OTpkpZBnAnxpVjRMbelsziycRSFPXzLvt3lPOJU8LKWUE_ePLk4eAtS4KNJttVHSX6nF39XjZu6H79KA2MlD_FdbTixlWK-yNiK1Qmj0a74YraIuDX6cxnTyRcQkQqQfpEuMY-5ecIOId6Asz6Y2PPL74vhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9954bd7931.mp4?token=kuTiYy0k__U8YO91Inq1rxPMGveKlyL0CzwTOfkVGhzZxzBn62MSPFlyhSRdpYyQrtquEDOLqF75XjyanqD_Fw3Bst449QLO4_3VWapvfZ6MgajeolkXa1mhijLUnSJVDKNT-G7uvF1kYEheqdZ5W8MyJ7QmTtyNjBLEOblnkAmnWws6pvJnRxOBt_OTpkpZBnAnxpVjRMbelsziycRSFPXzLvt3lPOJU8LKWUE_ePLk4eAtS4KNJttVHSX6nF39XjZu6H79KA2MlD_FdbTixlWK-yNiK1Qmj0a74YraIuDX6cxnTyRcQkQqQfpEuMY-5ecIOId6Asz6Y2PPL74vhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم.
خیلی زود خواهید فهمید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64966" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64965">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=IHKnSAAvTPlOVeLttHeX67cvRhFmmmA9XQ9cGxixTu1E1C4RzG7OZs4_WEXXhKRsmPZf9QIYwRjEf3GGfPnwe8g4EVK4ff5An9CXi_r4Nbp5NaxcoDfufNrZGUN9MAwUYJZEvj9xLdYmR0_d5kmMgbOWY0hUdW6pUi8HsobVaMCY8FwT5HGuIhcJyfrj1BGvmC68ANZm-_vGAQ_KATFRnBdk53bfVUSNrRGi6yvyFikbb36DGxLbGN6WXQFzLstNaWLjrmfkEkD7DT8mIyDhd7S60rqP5lmaH0ZphSsFBTaDf2dURBsAH0KaPGTlj5sngHNiMvs1lZ1PC3XoE2YBsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=IHKnSAAvTPlOVeLttHeX67cvRhFmmmA9XQ9cGxixTu1E1C4RzG7OZs4_WEXXhKRsmPZf9QIYwRjEf3GGfPnwe8g4EVK4ff5An9CXi_r4Nbp5NaxcoDfufNrZGUN9MAwUYJZEvj9xLdYmR0_d5kmMgbOWY0hUdW6pUi8HsobVaMCY8FwT5HGuIhcJyfrj1BGvmC68ANZm-_vGAQ_KATFRnBdk53bfVUSNrRGi6yvyFikbb36DGxLbGN6WXQFzLstNaWLjrmfkEkD7DT8mIyDhd7S60rqP5lmaH0ZphSsFBTaDf2dURBsAH0KaPGTlj5sngHNiMvs1lZ1PC3XoE2YBsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار طرفدران حکومت تو تجمعات شبانه: مرگ بر امارات!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64965" target="_blank">📅 15:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64964">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
خبرگزاری مهر: صدای انفجار ناشناخته در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64964" target="_blank">📅 14:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64963">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7zpEIANVhfEsB3xTMYLBWhhyAosIVc6I98O9CMuouDjHI5icizgyANZmPk9MyEKOUP4ka2UIiBHVSSiVGmSi9bMPGwAJUGGH32yqeVVhCfl5BYFcOlhquIo5kcPrnPx1HMSwpYgpTA238HzK8CBe6BOwucEUZAEufKB96_7L5IDnYFVuvJxxAFsuaTsqsxasAPp3lPCU60k92potWUqalZzyyVe3FqiPyEO0kwGCU61-BCtC_76vgR6wrCSbl94wX3-SY8BNMJMNLMdgp-MBRCOvhhtTeLW5c4k2_1gK8XdvqnEGbCkGb9m-UdjAgCTtU-RuYerH42hLWXwl4vrBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:   من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64963" target="_blank">📅 01:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64962">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4qfr4NxQJTwQf8_a4RL7POdjOGpwubK0hBT-8aDGpNBVnFPqgmFyfWmOTRM8pSHtBtZYT5y2RcAzLMBv4UXOtWNPxQu6td48QXenZV8q6Ln0TTAz1GijhCcOGz7AW791TV8HVOo_6dE93hdEUjHhME4_ITxdSht7Dm6o8tbS4VTt8ZA-PQpeX7_RZKAMVUCKkrY8I7P4A55d2oL8HxXa9Kmq79XCyPNewlrFAitXoz6Kmsz4Uc1ZqE5DNfSB_QI1bpXoBS4qmYlZnyY0Etc4TiEDzlyEehUzEvGsaVEJn0Oyat_puwIAI6RS2ZPyPmAjvongaXZNcFFLCFsd9bVzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به سلاح هسته‌ای دست پیدا نکنه.
با توجه به احترامم به این رهبران، به ارتش آمریکا دستور دادم فعلاً حمله انجام نشه، اما همزمان آماده‌باش کامل هستیم که اگه توافقی به نتیجه نرسه، در هر لحظه یه حمله گسترده رو شروع کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64962" target="_blank">📅 22:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64961">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inoxP4RgNn0PRkO5b0Cuy53MVFM5VnFWHByqo-9RNKTXgy4pOGpF_iv_7EJ902LfRwsvN-R2eBweabMjf41jyt7n97RxWZ5d-pw3zx1XgN6PQOQS_d-5apgAFyeTlcwKVp1-b8MtaSTLg4mBHel_S0_Va1IsmuWEn8eDF8zGbLcDKBH-oWeaBNrITyWZJbro-7v6r0ROmp1CtuhnZsq3ziUotpyZmDUmsCNwy3gl5vegZGf9lPUxHci7ppdCukd-Dd4afwIBsSkx8uR1LqThYN7NYonkMYHOfUG3NwbGY4YgUvrFHNY8WVNI75ibp112SiDZ1tx7Bb24tS1NUXvpkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
«اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» در حالی که پرچم سفید نماینده را به شدت تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌شان همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی بزرگ و باشکوه ایالات متحده آمریکا بپذیرند، روزنامه‌های در حال سقوط نیویورک تایمز، وال استریت ژورنال چین (WSJ!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و همه اعضای دیگر رسانه‌های خبری جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است، حتی نزدیک هم نبود. دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آنها کاملاً دیوانه شده‌اند!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64961" target="_blank">📅 18:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64959">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4NjP2rNwzAl7qbhlGTSFKX_d-eNQPr5VPwa1IhoAbMLiyOX1-LBpZP7yKMV1r_9JMpwnNNoQYgehZsu-VSJgotYAYpQNX85GF5OKGC2dm-FodYceh0ONnXSbtWVVcekXAEMmltfbZ1ktlRiMYivHmxRfOXWfoaUUklw_GCt3Rmx4mJbf7Djz1Txdz1ZMZVF32pFQWwz9Jei7GRBjBIzIJypRAQvu93OfnQ_jdE5dyb3PKw9g1aPao9ycMnUglkDtRKrU2KL7eALv7RQRZLCsSa8lhJf_gH-ZREo1Cu4nmYiSf3HOeJzOSPj3e6dmOdmxOWqMKwYOwKNqXI4Lk0QEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2H6Iyfx4H8AoxTndzR0qT9lUwZQsXq-q69Ns6NIVb7ZfTPM6fCmqocKjXIvtGCPUnPGzo5OoprT3mzWb2S0e314dyUww_E2VB5f_dv50vxdjA2keT3d-6bHMnWZo6hOslNV25CPU-V2Zwyss3pmrOJLaBbdF8Qvpp4ydtaeMnv4vWE8DdstrDZeL1kgbzcpnt5_9-gl2Pu8V0SP03hGVS23UjfqWF7T21Kc206JUAizBp_wS8CGlSoWW1RCNIl3izf31j-DQndtPZbdS8nj37_6Upf-r2lBcKYdXcXVcBFWe2Rl922pgGCLg-9ZgugkRsHiNhvzTnajDJemuSeUng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت خودرو ، ۲۸ اردیبهشت‌ماه ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64959" target="_blank">📅 14:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64952">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C0TNMJHget_j5xbAl215C3_HJv4SUDO1Q1KkOr-yDTAISKK-jFWTtv7vKZvZPd34Rs5PHbJHMn-Bb-IgRlTxzOSaDS09QZTLNl5yjtPiTAC_5ykV4laFxdn9ofpw6xjRM_iMBW8RXtlv0kziLRMHI0R0NNe1ml-2ck4FQ3CIjSwEzAuBj0KumXyZR0fGRq2ZHZop580WpIbszhd4F2PxXSdxQVtAZhmJyOmm68T8jZyWUNnwBDvWkzIyzdQqz9y34h24Ue0vrqZhA2C6iALZSpxoxa5XQvG-BhtRW5ofkFEDzlvNjhQC_Qfpx2Z9ZFt5EkBQveW23RBdpbpBhLmMvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qrsTEGNu1gz547mcnzBVU3uNSiRJbOIKhT_-U2oSSkyFU1XjRnouQwvJ5_0mqehFLGUx24wf5S1RzSA2hgnBnU14a8Oell_h2jHtty2juaMsy2P8i_wFP6Xao5lKVxj-MR8da6uI5Bijbeb_8qB7Ei0NLepoU73Cr1rAToeWkaDpyUNEndAvpqIDgBIdoyGqOS6pa66FeIypAHaSbLyg-vqNZIDtHEjYmNT1sG8IelZcXlK3ybdMs83KgsVxt72UMEG2sFxv0kUNtRv3EXf1mVxAX6poyLa-B3vPBvSvxVO5PA7P0RC_9aJjckP9LYgumnw7QOaXiwtql5QTY3qJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iiCnMC3jQVl-UqV6CSCoVG7G_Gh3N1sbv9PpXx6FFZDlBnSOGowiBvacCv84CwY-FYkb1fI9v8tIIgTsxNUOLTF59qRtYjAe7xQ7rWoQcBh_gQNHJA7YlxfsLMfMZI1i3XXY7YJR07eEpj7XNUnPlFyQ1cC5gVIi0mGCIiW2ZTV93nNkwydd86LjO5kGHNHgV28AxXNDkwsIRCNsrJs3__kXhUpVKfOuU8Dus_yb6CKCxeZ05InUfFAEWa84ku6MssfuNTw9BbZ59jg1zf3_qor3BVb2-2P0I-23bw7GBCmhP7s7DefiKj7x3zbJYv77xst0UE76KNZpGBzDPQVahA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rCiN_mZ-G4FOXgY-aOuJvkzeXJKtwAu66sLEWyWWzp_Ym7aftR3gsAX19Ad2chqoWZjGxziaSDCnSLtJYHwTROKNUBCF02T-KpfoF9PJ1Z83HzfoTqqtqqByZQ3RG81vc53VrV82-1dhBLEJQjvZkJmStLlOafpvkgPfwdx_ziwNpcikFZq2NnVH1e4A-w_TtOYJZVFyTHwAQYiODxl0E1t_vfW_nrI8jGdTtgiD3Li_brP-Hrw-A_hbbDxLBQKQa7P5Pl6U3HshB1WcuCBPMNzycwBEjfyKH6i6sWeMDmtHljjvt-DIs0WKZqYAegsToLPqmvfsNBQToM41s2MV_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gj2Bg9BbdDTs7EEuTVenm0kyVkkmHHsBMEz7wMtSyfTmBbPouUN9YB-mg6mvyB-rLc10dZ_8La6GmJglU3qT2gAVbJSZgbXcewDopSOYP69mATU6W2DJHZHcCQh_RjqajhEIIE293ijSyjcVcL48z4mEdpmc_0F9VPXy-0_4_a3Rq3abVaUZL_QI8awq3c4QItLvp5H-O756NbAcXnw-iqpeiJ4NSNI-2yxMqKFq1aRI-s8Q2-1oAWvARdpk1nzc-LqJ_Sr575abN6EkFQXjNWk2xV00tGBB_92dwj-hSlQywosTZgJcDsJYtBkmc3GgUBa3iLFxOYa1ORbxdd9Oyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XAYuzS5XVxrL9psN-j_vedvajbCxXAKR1jYcmnguKHdcYex3xFy79LdW01DnGiaavx9l_1UyYcNpqYLRQM0ha9p1IPf1FRsqlLGX1n9A6YnMW3bKGonvGmoMPmNzeKVQmYVnWtfN3Qs5UbJY208W1cM079DXp5ZIsqAZP-jfpHk2LArAcYP5iJeRkLfJcs_VR6phsDIqGdTEOrXN50sLAjS-UeEFOd1eI3t2RCYnnIRk6zgC35ng7uxTpVcYJXshi-d1Z-LpmDiuQoQgfG8OESXP8wXdgKj4lmwT3F2IoLyW3YtkFBlWj46sZUOooPkKuAK-7LUJN4pkazCQW_oJ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H2H2YeQJlbKAteC8_h2-OxRJU7zbOCLCcb5xiH0ZblnvQC67-Sp6Gj8WDwEVIC_gh13iqpExgKu96XVlml6QkH4VNlLbdsSrSb4BsommdLuTnSKxgbGZdZ_uzwjVC9tMPNekLDkbODj2zahRTeUHqofa08QRtrYl9Xm_cohMGrzkw0emZyvJk6fWoQdKI2U4dH-2sB1IV5vQhnA6szfgFd4XRT0AkkDmueHj9YnPMuwE7G6NslIzdww0YrNARcO5ip6FR83g0_YRe25yZ_VZIXX1j0ONDzvhNibmgdMS8vbe5Kk2giPLVMvSFcBi0aXJsw1_mWB7vLKxDUN1ojmK6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
پست های دیشب ترامپ دلقک که با هوش مصنوعی ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64952" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64951">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaVLBUfi9uVQzO2yxAUhueq6hLTQuHGdqPRY0Vi0sQTO9hSlUwO7ESnMC6fvQwpOjtm0LEFkh4JwH9KM5-_KgOgYL8EQQun_Qo88TGCYizG5ZMdJ22aAym7dfvkczJhqHdsak9CWj0AGfMqnesdgsp2Ss9bLyCj9VW4tdl2qV9wblsSkFzQRqTIyZxdI1VMrwOnBZ3dYv-XJ9J8lVtwTpjt684XpcaP8YuJKueZhIkgZ3R4pb7_FH5VPxzwtq4xRGUAPr1BHKcmf2g44ZcfKUZdvg2j4InPQAQAbVxxyYxndXel1FaWlUOQpb0e-A1yOOgShpUYIiDQPCXsBZjA4MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست عجیب حسین دهباشی سازنده ویدئو تبلیغاتی حسن روحانی تو انتخابات ۱۳۹۶:
حملات و ترورهای دشمن تا رهبری حسن روحانی ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64951" target="_blank">📅 10:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64950">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cskaSZ8rp6NGpVuGqb_cGen7zCfomlWvhQjkTyzeb9oeN-MdnqHWmE1Rs-XdM_xigJctf-SUOY95HVFffEnZsBbqBhgimXs6jzH8dop0K5Nnl0pxwAnWrEhbs7EqdlFIGJyDAaDxHCfv57yMFyuKixOBZNJ6oUVe7yAXwJXedVqDshsmojqkjqzoKdFTHlwQrCXDz6THY7jvqd_2tKm3qHbCLEkMdOeJYlnMQfychpH7Ew6BTHRWY-T92HD8o2WAkyXL6tpM_LDoXne8Q9Ad5idQ9d1ZjWxECrYXQ-J4IUN1TmQDHItENXmD6hgrzSOe4lk7jVly5ucSOxqrqm2aqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در شبکه اجتماعی که فیلتر شده
روز ارتباطاتی که قطع شده رو تبریک گفت
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64950" target="_blank">📅 21:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64949">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClVZFPj4a_P2_14k8yFX1x-4aVwHiWnyg_MP0g64RxdIjj6MtHqbkojVnJoP55_vBmBRsfhu065KBVCAFXboRX9SrgQqa8GEgbA8v_bjvOHMb0DVufKTQSYzOzDqJfvU1Vyz43UIxUmoE0MwsZkjRTPVniWzq98xZWuIvLeIrANhv25SOWwIBbYHxpIKZBvs7XA5faaDocPRn5YuDKavPLBR8i6-2m1RHx_uSPQYuqhK4Es5g4uSwKrUTsXK79WkiJBtBFA6G6SPm6flPYI-JMkI9sxSMHrNw2Lt2sQKiHjlEsTslZo6md0-ET44prCaXmh2NySFV_IFx6S79ajYQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64949" target="_blank">📅 21:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64948">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=AesqHsd8bbmcRUHpc0dd_B9bdMrAjByRVwNGAeXtmzZY38hrYElI0H0ECTACQO9OEEShtBfMs549JXbcFd6EV8kXlGAc2ZgnOa9pNCAIpC4FQh_t0lhaI4jBpZF5GY-HnQNO-bzYHvJxifo7epvTgf3axyNDZ9cz64YH4oAJob8b6jSOY27rQYw9WGiWkOgF84fRuXAFpf1Awg3ZhwdQ-sTpQqY3L4VZ3odFrOh5N43VKfoskcuw-3fuDjrXHItMRUz3E203K7g2o3Ihpj-7nv4yNrRq7tLQP4lB9JztMJ_fAhb-Z-ugn8OpEn57AjiZm8xsQaWT_f31GHRRmQsz_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=AesqHsd8bbmcRUHpc0dd_B9bdMrAjByRVwNGAeXtmzZY38hrYElI0H0ECTACQO9OEEShtBfMs549JXbcFd6EV8kXlGAc2ZgnOa9pNCAIpC4FQh_t0lhaI4jBpZF5GY-HnQNO-bzYHvJxifo7epvTgf3axyNDZ9cz64YH4oAJob8b6jSOY27rQYw9WGiWkOgF84fRuXAFpf1Awg3ZhwdQ-sTpQqY3L4VZ3odFrOh5N43VKfoskcuw-3fuDjrXHItMRUz3E203K7g2o3Ihpj-7nv4yNrRq7tLQP4lB9JztMJ_fAhb-Z-ugn8OpEn57AjiZm8xsQaWT_f31GHRRmQsz_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
بر اساس تحلیل من، هیچ چیزی نشان نمی‌دهد که افرادی که اکنون در قدرت هستند با قبل متفاوت باشند
آنها هنوز هم می‌خواهند جهان را ترور کنند، اسرائیل را نابود کنند و به ما حمله کنند.
هر قیمتی که لازم باشد بپردازیم، خواهیم پرداخت.
چرچیل چه گفت؟ «هر قیمتی که لازم باشد برای شکست هیتلر بپردازیم، خواهیم پرداخت.»
همین موضوع درباره ایران هم صدق می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64948" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64947">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یک سری کانفیگ فروش طی یک حرکت بی‌شرفانه برا سرور هاشون ضریب گذاشتن، یعنی شما ۱۰۰ مگابیت مصرف می‌کنید ولی حجم مصرفی ضربدر یک عدد می‌شه، حالا ۲ یا ۳ یا هر عدد دیگه‌ای  اگه این حرکت کصشرتونو جمع نکنید تک تک اسم می‌برم تا نه آبرویی بمونه نه مشتری‌ای @News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64947" target="_blank">📅 19:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64946">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تسنیم: ممباقر گذاشتیم نماینده ویژه جمهوری اسلامی تو امور چین
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64946" target="_blank">📅 12:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64945">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=rMlqn9pxC7SzuC0if3AptwZQIgwHVsRsqJGgBln1_yPjpSIYeC7noVDYVy0uoEmZVnInozfR0043HyePi1i0eOY-lXWju1fy8fFq8KQlAQmfi5tJRy6-JXcoLP6uYsZzDhHLMXUsdyrLzaTWdWKArhGfEPaXKF7wtp0VwCKD4SNLkG6kMHc9NounnFDes0adNFjQPIl5t28RTp84czlYYcI8tnYeuSuBIwJl_GWE1JiPogUBy9mh84i9ohFWrav7hQeBKawkPP8TgRG4pweiA-zjyThF8hjZt8Uy8hp3LXksUAUumYkSIAoeil_4uLO3wqhyxdG6xrBXbCegHZ1NhA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=rMlqn9pxC7SzuC0if3AptwZQIgwHVsRsqJGgBln1_yPjpSIYeC7noVDYVy0uoEmZVnInozfR0043HyePi1i0eOY-lXWju1fy8fFq8KQlAQmfi5tJRy6-JXcoLP6uYsZzDhHLMXUsdyrLzaTWdWKArhGfEPaXKF7wtp0VwCKD4SNLkG6kMHc9NounnFDes0adNFjQPIl5t28RTp84czlYYcI8tnYeuSuBIwJl_GWE1JiPogUBy9mh84i9ohFWrav7hQeBKawkPP8TgRG4pweiA-zjyThF8hjZt8Uy8hp3LXksUAUumYkSIAoeil_4uLO3wqhyxdG6xrBXbCegHZ1NhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
‏
حدادعادل: والا من خودم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/64945" target="_blank">📅 10:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64944">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VtaFArDUEiy8e5GZeQO3I1fFy8p2g-H-ibp2veQkqdQGEcKT9SQMWDAZSBgknY3Gv-8px1Iw6XHzlLJ9RrTdFJ29f64xLNNIdgF7r7yDzBfO0pHrW1hBKEVnr3llXlKheJ8INHJVSYVZxEbGUYkvKFPRfXOMkyQmnBNTW9UTJTMMIckkxQYZrd1SxJHiP7LpE2No6izIiBaHiapmKliFAeyf4h_7atBtYSnct2dVELly63muLkU3Jc1H0lv4m-1eX-cquVHGeuE7AjhDSkTa57vyU_QBatl5pzetpBcAbUYWdc1EPBOgSbCVX_SMamZepTDr7WvhuFQwIBuBdDXhSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیلی‌میل: کیر میخواد از نخست‌وزیری انگلیس استعفا بده
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64944" target="_blank">📅 07:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64943">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWrGZb_RWKqjfDDGVVvNxZzG-6sdOd3SCY8YeDLvmAOeI73ZdO9LvNem1toje7W3tb_PQuwh7aQllUY3cId2UrZD-o18zvYGSgNwh0GctpxzzirhK3HDit0Ot1xqWopHqmGhxyFSsxFW-gSSZTMYeHRi2Kx74bdd1WMYkChBJWbOWhOPtvGzx0ZHhX6KpkR2K5gKzLeNZqFWvmGXyw6Eyps4nyieLInaxTR5fnjmjDBUwFzQm6ML5LM5ppzXsuv4cHxIjczv2BfdHZRH5XDeGPdDf6nslDXdELUx5ZcN4UhRpP67qNfOK8u4Jd-3J4ojlgSDT2U1JC-hse-mSZExKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در سوشال تروث: «این آرامشِ پیش از طوفان بود»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/64943" target="_blank">📅 00:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64942">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مثل اینکه شمال کشور زلزله‌ی نسبتاً شدیدی اومده، مراقب پس‌لرزه هاش باشید
❤️
‌
#hjAly</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64942" target="_blank">📅 20:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64940">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bps8L33wRLmtb0qNzzTdJwGLWBuMpEAQF5p6C-pxHyp9NGA0EAe9ElfkayO04eSNPMofDzP2vVCxsjEkJDltwnGGwf1QpwMqyWwxUdoX2X574UZp8-yHLqtp8Cnsn-a8t3h4U9Io6vTwl7PEPhYGJQkI4yBkKvghaJUioxfBH4I2SifLf2lwIBk7eURkSDJCXydpnawHWoYxQBZ3ghkDFJFRYYnlhAOSjhECjFO07aQtagBxXcOlwRt0oviZQ-nNWKflZmvVyx1-VvYgl02c7frfKxuvVLy_VRd-zZJ5ZBz-6DnI17ijnQPOz-Qw5R-9rXuGjYCXK90QJVQfmdPtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=JyoU3hKzD7ukxkNrAGYIOtqpWZpz9SnCBjIX7aWpKGjH9TvIdOVrFqKE1H79ATY4tvuXfFpjI0JnjnBRM10ZEFlcRNdqTl1Zzajm2AXesZxRvaOUuUt9uwfsJm8Z58XUHcTmuQDS2oN5XyL0IrNcuokHgOBWl0p3msPYx3OkwleSJH0gYNsf24XjBcGmy5cXzwX6c_OXmevHoqjPp7tSyj0j2qGtby6ZPSZoljaK-cXuM6gDT7CviOr5PQrwpFKRB5Seuy58gbe82DkSr9_YLU9xukZAIqnCemA2NdSwesA5fCCEmgNCgw9Hoo9LnKwVygG5oQPqYNkisT48DEd6wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=JyoU3hKzD7ukxkNrAGYIOtqpWZpz9SnCBjIX7aWpKGjH9TvIdOVrFqKE1H79ATY4tvuXfFpjI0JnjnBRM10ZEFlcRNdqTl1Zzajm2AXesZxRvaOUuUt9uwfsJm8Z58XUHcTmuQDS2oN5XyL0IrNcuokHgOBWl0p3msPYx3OkwleSJH0gYNsf24XjBcGmy5cXzwX6c_OXmevHoqjPp7tSyj0j2qGtby6ZPSZoljaK-cXuM6gDT7CviOr5PQrwpFKRB5Seuy58gbe82DkSr9_YLU9xukZAIqnCemA2NdSwesA5fCCEmgNCgw9Hoo9LnKwVygG5oQPqYNkisT48DEd6wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند طرفدار فلسطین از برج ایفل بالا رفتند و پرچم فلسطین را از طبقه اول آن آویزان کردند
شش نفر از این افراد توسط پلیس دستگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64940" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64939">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sU1ZA2o7r9_4j4p12P7SJ9ZA9wheT8eMmD28EBwsne-_9HNpyw-WpfUkEBk--XDd36wj1IdBwuMqp00ukPnciV9hspC6xBzcBY5YHo5bIyHMCH0rsSto8bGnbqBi3blcJgsa_7VIEmuUZykPyOl2LXy0y9dhbuaDRcagnOFlNRb-crKNDEykJMN8UFhblzYE0pLRXksEI_0fcie9r-G2usoR7AQnppc6c7BDhHqugVx6Xo1bXVqQQDv8F9-ehvZ9mDJCHY21LS9T1hCaVefs6DRogwCpWDhFcdcCmaCb8-zqnUfIdIi-3rwD2_sz-mLkaWdxF1TKSIRaCM_pNNxXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست ترامپ در تروث‌سوشال:
بازی نداریم! تماشا کن قراره بعدش تو موضع مورد علاقت چه اتفاقی رخ میده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64939" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64938">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64938" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64936">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7zpScNHPja2imIuwB8aKn4HOeqdQl3Yucv9g0UJiEtutFjoJ0NA5-QlA7j4g7HTnBBJXCXl_hizxeaJ4I9d7yk8C9BQsGSOO0UTlkD1DhxzROoE8AEXEEco4-LI-NtlUUzMP88HacS0rxCJxAoKAVjc5DmMUmr_LGewgNM-RFDuCaD0iqOE2VjgbwwnSYAcn0oZht7YQftpKjD5iEokGx7oh7SmeNpT6bq0Q7KO1MI0cAPO6SNc4dOt1ytjtcxVpxuXF7E2SGREdT6ebKoY_B9IPXhhm_8whhsizDj85pTah1HB5A757KHU-tstJab9CQGfQqc6_OFIWwkOZmLsDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3-JwibJjdd41vanRf_Z49ObcwzqGD3y_-D1Z1s_mboERqe-vRRHkrxB2PG4o5w2V694ubBOI_bgt6CQlGCVpA_3onSHdCQCIewBij1VBKGaVbaLoykCO9jVFjRJADZdo-9OcPJrY6pWblIoFrXCK-he3JfVp4MX1P8oILR52Cz1rPZgfrg-tP9UhbX_YmTUm5lQsJFqpQLHDfHAq9ilmxHiw_6JR7PO4bwXsMj0dyaqHGIdeWZSdIDcgau-nfYTprxMtOj-VUuIsNcwPDjxuy8w3sV_O0wivPpQu9Uwptcs6qV8NIKXIayIG-lifnE6rnQPm75rCw6AFbbHRoTM0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیکتاتور‌ها مثل هم رفتار می‌کنند
دیکتاتور ها مثل هم سقوط می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/64936" target="_blank">📅 10:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64935">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل گزارش داد که در اسرائیل برآورد می‌شود دونالد ترامپ در ۲۴ ساعت آینده درباره اقدام نظامی علیه جمهوری اسلامی تصمیم بگیرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64935" target="_blank">📅 10:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64934">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">عه امروز واقعاً روز پسره؟ روزمون مبارک
🕺
#hjAly
‌</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64934" target="_blank">📅 10:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64933">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4x3un4rrd-rVsYB58JO3EInDi0hWNHZDGKNfVAW0DGe5c53V_jd_ubR-YzOjSQ6oiwk7N_bUvBSyVRjRGl-5KhW2ygzACVJ0nNTmSAAbQl7Df8ckZKNdtNNZlDJF3khuV-Jz91KMQZzK2F7ammiJ5Sh9ceCNlG0EyUoV1wDR1406nB6-jPJpiHypTgBDA7JMp-g0P9shoAkPkLPrrf0VT5U3GhwccLWX3Af_ubvw0TyTrnHFeGCSlFdIKTtVjRZFyPu2UIC-Yyz_EdGvH1OWoB996UMIg6BnL5PHWld3QmqPegbYxdZvMbNuT9u9q0k0fSbRHZj9t6XGSPsaNLX-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزالدین حداد، رئیس شاخه نظامی حماس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/64933" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64932">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=Eq9adYPpWhMNo-lw55r1-mqg--AKnPRkSnDwdA7t0tu5k9ksif5AEP3Nq9q-OKqcWdG_yddBqVuulTsbCmTmiJmjErPh7E3hrDzHEiIEGorkp9DcpqC2TeAkRiZg9pMWpWxtbrav4yNa1J63Lj05gqAx25ZRk7APxOeQ9TacroDHt4u-yC38jloy7-OW_kARIDjv1AemSVU31aoWqeD_1xhQ6aujMD-eb79j3IzPKSVlvZA10XfYHSQsVHe_X7dLjh3A5Cc_gkg_8hs57STVwWb4QAojO-vb5YB2XFFFN7DVa17a-PmgtGrOR-UybQwv-ppAth0xT3Wuohrf0YZ8ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=Eq9adYPpWhMNo-lw55r1-mqg--AKnPRkSnDwdA7t0tu5k9ksif5AEP3Nq9q-OKqcWdG_yddBqVuulTsbCmTmiJmjErPh7E3hrDzHEiIEGorkp9DcpqC2TeAkRiZg9pMWpWxtbrav4yNa1J63Lj05gqAx25ZRk7APxOeQ9TacroDHt4u-yC38jloy7-OW_kARIDjv1AemSVU31aoWqeD_1xhQ6aujMD-eb79j3IzPKSVlvZA10XfYHSQsVHe_X7dLjh3A5Cc_gkg_8hs57STVwWb4QAojO-vb5YB2XFFFN7DVa17a-PmgtGrOR-UybQwv-ppAth0xT3Wuohrf0YZ8ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64932" target="_blank">📅 20:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64931">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
📱
👑
آی‌پی های جدید برای فیلترشکن شیر و خورشید
🛜
‌ ‌ ‌ همراه اول
2.22.250.149
23.58.193.140</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64931" target="_blank">📅 19:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64929">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">همه‌ی اعضاء هیأت آمریکایی قبل از اینکه سوار «ایر فورس وان» بشن و پکن رو ترک کنن، هر چی که از میزبان‌های چینی گرفته بودن [هدیه و یادگاری]، همش رو همون‌جا انداختن تو سطل زباله.
دلیل این کار احتمال جاسوسی بوده
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/64929" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64928">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXrQSBtw2plliKxiaN0rNkH9OCzuHcolo7NeEfOvHEHNKBFWxgmTm_5XdcPFkL-5gWk3fwriWzH7nqEjFlgrBYU9nRcXW_amp9O9jXRLgrpWIDDU34klXqof9t6jeJutIWiFoP3of4jcS2IHTlTyeGUv-cJ25wn7ZLeblLDGvDjdKfJeVvPByHhgTZTmtIkKQzSSIBBx3r2gR---heIQ0HHufzI8eJULjUu4jq51AGrKbR6gxCnd_VmXyG0GxcmlV61mUggj2l4n5zd7xyAi5UplXdvAkQbSdpP0KumrwikIHoOZCqFm2yG2fuCzA_1ypphw6RrvPuARIWanNaAKJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/64928" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64927">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: تعلیق ۲۰ ساله‌ی غنی‌سازی باید یک تعهد واقعی باشد  @News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64927" target="_blank">📅 14:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64926">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم  @News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64926" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64925">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم
؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64925" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64924">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تنها هدف حاکمیت فعلی، رسیدن به اولین شرط هست و بقیه شرط بیشتر نمایشی هستند برای بستن دهان طرفداران، چون به خوبی ‌می‌دونند که ترامپ، اوباما نیست و تا زمان انجام توافق، قرار نیست تحریمی لغو شه یا اموال بلوک شده آزاد شه!  منتها ترامپ به خوبی برنامه‌ی جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64924" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64923">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
ایران از چند روز پیش منتظر پاسخ آمریکا به این پیشنهاد پنج‌بندی بوده، طراحان این پنج‌بند فرماندهان سپاه از جمله جعفر عزیزی با مدیریت احمد وحیدی و تایید مجتبی خامنه‌ای بودند، طبق گزارش خبرنگار ارشد الجزیره، تمامی این پنج بند توسط آمریکا رد شده!  جزئیات پیشنهاد…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64923" target="_blank">📅 13:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64921">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IdnoId0e2sBAYyzwqez82uHVCZ2MjXBARJE131TL5JziXfQ31BSB3rWbO6HCWDaU0WRxdqtydpX5M5WTzxISRSFUgyWX8oGPC3kUCogas5H9doLoNi4qpLGYfd-1xM5vqVSXms49bhfTiC1lj15wM-t8qlINNpp570wCUptA-flAElFS1DdSsb8B1U4YBYZikMktQILIYGnkxwhGkOIVIwN1BEjuGcOFGKJZDFDV2icANTqwdbcmCv2UtySHzgeYg-bqLeIJaRUUKJ6e08nlcx--LKohZlyRemD9jJHv_q05JQRrEAYgXbE0tnJBqOnQVtNyTM8g4J4umdsBFC2LGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CNvToyjQcBQbIyTlMShHjeTcBp__Whe5wCNf3m3AsxcRPlucOLpxkXpt0w5OISHEaX0T2aeyhM3l3J4vbAy8KU_kXAxughP4OanawKAkg27l7T3ZPUmLYMp6IcHK2r6B6XlzAKCSVsikYRfXawx2KK35Ucsc75NlLbqaiANS5RwSMhgpuNK8tUj83lDCIp6xOAnREu2q1ARVP9rfD9L74ev7HcI3qq4aloZyEjY6NpQF6IdatP_GFWM17eRfKxXg_H2SyCjX8Ss3aCcYYigGcOkwZ3IMvfkkhO51RvpZurR5608B6lLLRpyqsw4P2gNohX219iE405QFXw5jyl8rGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ الجزیره: پنج بند ایرانی ها توسط ترامپ بطور کامل رد شده‌اند، مجتبی خامنه‌ای دستور داده بود در صورت رد این پنج بند، دیگر وارد مذاکرات نشوند  @News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64921" target="_blank">📅 13:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64920">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uG1MVRBYSpahZ-5ZFh06kJ9vGFQs7kgn8lyG1NLznB1a4wciTwKRpc8ce54IpTJPIOBCHEVjr7fv5Hl8_Rn9ByJNCMEI6JBcE6BDVl-1R-wdPJNhj5nyvt3CmC9FDg12KRvAH3FME4wiQAGBvIXDD7hDy_QotyNDqPT-K9dL3NXcnWhwmSODDPEP4Z5YRXDjWrYjaK1CTXLCKQV5o_b4B4FIJxhZv20sShNBrmqLYRdn8BRzCd1WKM73r82pau9gVW9DVrTRs1mh_zfV9-tLtUgHRkmjHrvf1xEoh8Q2LQrhCtGwBQE2lUlQzABe9zw3esXVP0VmvUjwKr77ayhhIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#فوری؛ علی‌هاشم خبرنگار ارشد الجزیره: یک منبع آگاه ایرانی به من گفت که تهران رسماً پاسخ آمریکا به پیشنهاد ایران را دریافت کرده است و واشنگتن شرایط ایران را به طور کامل رد کرده است  تیم مذاکره‌کننده ایران پنج شرط را که باید قبل از ورود به مذاکرات در مورد…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64920" target="_blank">📅 13:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64919">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇺🇸
ترامپ:  امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند. می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت. هر کاری…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/64919" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64918">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🇮🇷
عراقچی: پیام‌های متناقض آمریکایی‌ها مهم‌ترین مشکل است، هیچ راه‌حل نظامی‌ای وجود ندارد و فکر می‌کنم ایالات متحده باید این واقعیت را درک کند. آن‌ها دست‌کم دو بار ما را آزموده‌اند و اکنون به این نتیجه رسیده‌اند که راه‌حل نظامی وجود ندارد!
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64918" target="_blank">📅 12:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64917">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.14@HotVpnPlus.apk</div>
  <div class="tg-doc-extra">23.9 MB</div>
</div>
<a href="https://t.me/news_hut/64917" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
👑
یکی از فیلترشکن هایی که گزارش اتصال خیلی بالایی از اون میاد، فیلترشکن غیررسمی سایفون بنام شیر و خورشید هست، دقت کنید این یک ورژن غیررسمی هست که تعداد زیادی از کاربران تونستند با این روش به اینترنت بین‌الملل درستی پیدا کنند! در آخر پست لینک دانلود این اپلیکیشن قرار می‌گیره</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/64917" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64916">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lB8hMsgZ4oIHtEiCbSIZOj_RJYWq53uR2lK2flNtscFabcjyqVl-cwNAIHsihI9fY7ER0GSTDTrag_dfKpafCOySomPRn1gFVxSsMz9iS3ii5fZ5SKAffSQCJz6yofdYkJVRBqd5fw5ed04pNVzvYm4ESix2WWHbdxll03WcliwS7oOPnxAX7b1HhXXwcjnL83mBg4ll5nhCOS8d16VBudpXBAXIZ3DuuCgBkmDvpV0YTyLhr8YWAayM1wtsnh3ARGq-Huy4x69CgJNI-usBY0ZPHX185I3wWODNCQX9zyPWkhyb6nSAj83HBEMjtWNBK3jroX0qtkdIKIMjFWSKpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
👑
یکی از فیلترشکن هایی که گزارش اتصال خیلی بالایی از اون میاد، فیلترشکن غیررسمی سایفون بنام شیر و خورشید هست، دقت کنید این یک ورژن غیررسمی هست که تعداد زیادی از کاربران تونستند با این روش به اینترنت بین‌الملل درستی پیدا کنند! در آخر پست لینک دانلود این اپلیکیشن قرار می‌گیره
👑
‌ ‌ ‌ وارد فیلترشکن شیر و خورشید شوید
[دانلود فایل در پایین همین پست]
1️⃣
‌ ‌ ‌ بعد از اینکه نصبش کردین و وارد شدین، از نوار بالا برید تو قسمت OPTIONS
2️⃣
‌ ‌ ‌ تو مرحله دوم وارد قسمت آخر یعنی More Options بشین
3️⃣
‌ ‌ ‌ تو این مرحله برید پایین تا گزیه Connection Protocol رو پیدا کنید یبار بزنید روش تا با صفحه جدید روبرو شید
4️⃣
‌ ‌ ‌ تو منوی باز شده گزینه CDN Fronting رو بزنید و برگردین عقب، دقت کنید برا بعضیا تا همینجای کار رو انجام دادن و برگشتن به صفحه یک استارت رو زدن وصل شده و برا عده باید باید آی‌پی هم وارد کنه که در ادامه می‌گیم
5️⃣
‌ ‌ ‌ تو مرحله بعد باید یه قسمت برگردین عقب و وارد بخش CDN edge IPs بشید
6️⃣
‌ ‌ ‌ تو صفحه‌ی باز شده باید آی‌پی های زیر رو وارد کنید، دقت کنید آی‌پی ها مدام آپدیت می‌شن و آپدیت های جدید در داخل کانال قرار داده می‌شه، تو این بخش کافیه یه آی‌پی وارد کنید و OK رو بزنید، حالا برگردین به قسمت تصویر شماره
1️⃣
‌ ‌ ‌  و روی استارت کلیک کنید تا وصل شین، دقت کنید بعضی از آی‌پی‌ها hostname دارن که بدون هیچ مشکلی تو شکل شماره پنجم، host رو تو قسمت دوم (پایین فلش) وارد می‌کنید
🌟
آی‌پی هایی که فعلا موجود هستند
:
CDN SNI Hostname:
python.org
151.101.64.223
151.101.0.223
151.101.128.223
151.101.192.223
92.122.123.128
2.16.186.20
2.16.186.31
2.16.186.44
2.16.186.58
2.16.186.69
2.16.186.81
2.19.204.19
2.19.204.87
2.19.204.137
2.19.204.144
2.19.204.145
2.19.204.170
2.19.204.184
2.19.204.185
2.19.204.202
2.19.204.210
2.19.204.211
2.19.204.217
2.19.204.218
2.19.204.225
2.19.204.232
2.19.204.234
2.19.204.240
2.19.204.249
2.19.204.250
2.19.204.251
2.19.205.8
2.19.205.9
2.19.205.11
2.19.205.27
2.19.205.33
2.19.205.34
2.19.205.40
2.19.205.41
2.19.205.42
2.19.205.49
2.19.205.50
2.19.205.58
2.19.205.59
2.19.205.64
2.19.205.65
2.19.205.82
2.19.205.83
2.19.205.88
2.19.205.97
2.19.205.98
2.19.205.105
2.22.151.4
2.22.151.9
2.22.151.12
2.22.151.13
2.22.151.15
2.22.151.17
2.22.151.20
2.22.151.22
2.22.151.23
2.22.151.32
2.22.151.36
2.22.151.37
2.22.151.39
2.22.151.47
2.22.151.51
2.22.151.53
2.22.151.54
2.22.151.58
2.22.151.60
2.22.151.62
2.22.151.135
2.22.151.138
2.22.151.139
2.22.151.141
2.22.151.142
2.22.151.143
2.22.151.144
2.22.151.146
2.22.151.149
2.22.151.150
2.22.151.151
2.22.151.152
2.22.151.153
2.22.151.154
2.22.151.155
2.22.151.156
2.22.151.157
2.22.151.158
2.22.151.159
2.22.151.161
2.22.151.162
2.22.151.163
2.22.151.164
2.22.151.168
2.22.151.169
2.22.151.170
2.22.151.171
2.22.151.173
2.22.151.175
2.22.151.179
2.22.151.181
2.22.151.182
2.22.151.183
2.22.151.184
2.22.151.185
2.22.151.186
2.22.151.188
2.22.151.189
2.22.151.190
2.22.151.191
2.22.151.193
2.22.151.194
2.22.151.195
23.32.5.18
23.32.5.44
23.32.5.71
23.32.5.96
23.32.5.118
23.32.5.141
23.32.5.167
23.32.5.193
23.32.5.214
23.32.5.236
23.53.35.146
23.53.35.158
23.53.35.171
23.53.35.182
23.53.35.194
23.53.35.207
23.67.253.24
23.67.253.55
23.67.253.77
23.67.253.101
23.67.253.120
23.195.81.72
23.195.81.84
23.195.81.96
23.195.81.108
50.7.5.83
63.141.252.203
65.109.34.234
92.122.123.128
94.130.13.19
94.130.33.41
94.130.50.12
94.130.70.160
95.216.69.37
96.16.97.82
96.16.97.104
96.16.97.126
96.16.97.148
96.16.97.169
96.16.97.191
104.124.148.191
104.124.148.203
138.201.54.122
142.54.178.211
144.76.1.88
184.26.163.12
184.26.163.24
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
23.48.23.186
⚠️
‌ ‌‌ ‌ دقت کنید با یکبار لمس همه کپی می‌شن فقط اول ip هارو رو از حالت خلاصه به حالت گسترده تبدیل کنید تا همه قابل نمایش باشن، و داخل فیلترشکن باید تک‌تک بزنید
👑
‌ ‌ ‌
لینک دانلود جدیدترین فایل فیلترشکن شیر و خورشید
https://t.me/hotVPNplus/9
@HotVpnPlus
|
@HutNewsPlus</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/64916" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64915">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=jsiomvuaHaHjUVwsr5pIUlGX5zB5qTmXPaUArIgBZetooin-causUZZTzVPjM-MC3p2vJ_CYANd0LSQKDWq7whRR91xF5p_8GoES7o4CaFLWKyH1X1rnbaD_-M0hGj8mMPuBqSzlAQmaAtKDur3eaqbVWKKgFN6hV9GJVm-nLbBFFZEk0vJXX0NvNW0NcaM9XyTqLO3QsbU_6miqjulr0cL2eZd8eZjAY6EokXOzfcLXQKSMKhq3lVWE2in9EBxxLYfI_Kwn9SZQEjpchHka3w1x_GywSK1cD65XKxQ0sA6lSmMhLH3BjbOc0_CbdqfMSTLEr7MthDHz153gcYhQpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=jsiomvuaHaHjUVwsr5pIUlGX5zB5qTmXPaUArIgBZetooin-causUZZTzVPjM-MC3p2vJ_CYANd0LSQKDWq7whRR91xF5p_8GoES7o4CaFLWKyH1X1rnbaD_-M0hGj8mMPuBqSzlAQmaAtKDur3eaqbVWKKgFN6hV9GJVm-nLbBFFZEk0vJXX0NvNW0NcaM9XyTqLO3QsbU_6miqjulr0cL2eZd8eZjAY6EokXOzfcLXQKSMKhq3lVWE2in9EBxxLYfI_Kwn9SZQEjpchHka3w1x_GywSK1cD65XKxQ0sA6lSmMhLH3BjbOc0_CbdqfMSTLEr7MthDHz153gcYhQpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند.
می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت.
هر کاری که در چهار هفته گذشته انجام داده‌اند، در یک روز از بین خواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64915" target="_blank">📅 10:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64914">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
📰
کان نیوز:اسرائیل معتقد است که ترامپ پس از بازگشت از سفر چین برای از سرگیری عملیات نظامی علیه ایران تصمیم خواهد گرفت.  مقامات ارشد ارتش اسرائیل و فرماندهی مرکزی آمریکا (CENTCOM) در هفته گذشته درباره احتمال از سرگیری عملیات علیه ایران گفتگو کرده‌اند. بحث‌ها…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64914" target="_blank">📅 10:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64913">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/A9sx7WkZZ4gIJ1eZZFAw2IHenZRK00LbMl2j0t6cC1cVShs3aVleNRlJpy6JG_MpQtNoozrEh5vQ6dMwXhwc3P8Hlwd5mXUyZSmgClEB4RID-ZrVGJtUSSuhQJ1FMEDn42bpNbrhTEEyazdxwSHXPC0KHuPp8MhmzkNWezlAtkeP5PIUdwAN6l-5pN8cCU-G16y17cHhnmGa0xxgOdo5-DSkLmia7kcrrPba5Y3HROK9a1g_eemHluiDZhZH8zMz0z_BJ2nYRS8S4Zk65rpw-jz2ABbtczHQ5H-ramCUiHkfoTAff66QL8DAm0nwmoYBX-BaxXNEErTVxn5gCzTfcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/news_hut/64913" target="_blank">📅 03:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64912">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qM2xfeBA2fTh9xc-QhWehC405pDM4aAnoAuZJfhNy4xCeWaUoFNN24ovePao7fRDSvlI4YYBWRY5_F4zBaJPvFihCMoR45Vo6S2J0BUB15IpIF1wBqLfcRIOqXmYRLebcQRMjTF7Y0CTUYG-TkzcDO94ag9-h3qHpTaOmvxSZImqijBtJtyNKDiUkkQAnWD9E7hVH6QJoBrkdxzEsm6MI881NX6ve7kNHnc5stiAOdrGbiZVG3_iD7SZgkzO19ZMKD2YO6DJy7_PxmLnpazzQQjPLWxIRg9XwACt3rU_yKlHuUAM3nHmqxZdXy5U_inJloa2yBVBJZZWh0a5a88B2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی؛ نماینده‌ی مجلس:
دولت قصد داره میزان سهمیه ماهانه بنزین ۱۵۰۰ تومنی و ۳۰۰۰ تومنی رو کاهش بده و قیمت بنزین ۵۰۰۰ تومنی رو هم به ۲۰۰۰۰ تومن برسونه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64912" target="_blank">📅 19:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64911">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=FeyPgYPqihVWNx-GfFAcc-V9Y7YF8Yvw8r4-cJVWolk03G9_fUgY8-Gqnl7WZLR-AKsGkNuSj05Bu9b-Uld5hfnzDGz8Amyk6nxpuaw1yVhDxnCfey_y_kCYeiPnSH1RnyM89T77uLt2_-GlgERAj1tSSw3ie9RVJNw14ta_LAGTQxKjxr9BeKuxIVDWq9MV5dilltVWvdc5WTPJsIna-CEBWnly_1sB06VEukzhwlQn4hieGzW3bPKuWRvuNTO7KraipTSr8aoFAm5BlyMywHxVmZmLKfM9sb-Stt7K5a4B6HOVogGsebL3WzenbdEXNdhxMFVp779EdXu0fBdglg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=FeyPgYPqihVWNx-GfFAcc-V9Y7YF8Yvw8r4-cJVWolk03G9_fUgY8-Gqnl7WZLR-AKsGkNuSj05Bu9b-Uld5hfnzDGz8Amyk6nxpuaw1yVhDxnCfey_y_kCYeiPnSH1RnyM89T77uLt2_-GlgERAj1tSSw3ie9RVJNw14ta_LAGTQxKjxr9BeKuxIVDWq9MV5dilltVWvdc5WTPJsIna-CEBWnly_1sB06VEukzhwlQn4hieGzW3bPKuWRvuNTO7KraipTSr8aoFAm5BlyMywHxVmZmLKfM9sb-Stt7K5a4B6HOVogGsebL3WzenbdEXNdhxMFVp779EdXu0fBdglg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ی دست دادن ترامپ و شی
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64911" target="_blank">📅 13:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64910">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWixm3L3HZ27QlvixkBBMXxrq-U-nrf90kumMoSa9CKVv7aFKK4cxBcsU8qcTWn99d7yk50uikQoZB8ElyKBbMQg3jnpIXI0rFpZpogZjJEIjo_4GVe72ureSC5Qr_-Y6RGQ5m_pg2NAOcdHWfcqMrK9esSWW0sQEaVr4HuvMvKoNkIpdgKf6FPlQW7J4IQzvScWlmzrf6gD2vQTed6rt4-bRyi3ysq_yEsnwC4mrHIQ_VIXpG0aEX5MLT6-fA9On4z2nTDs78z_wuXjRqi8y12EZiMeHU1XfItit1K9eqUjMTeXILp2i5LqGBXuVNC0ci9fW3WSJ8ClC_vgtieEyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64910" target="_blank">📅 02:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64909">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64909" target="_blank">📅 02:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64908">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇺🇸
#مهم
؛ برای اولین بار،  اینجا در کنگره امریکا، سه نفر از جمهوری خواهان از صف حامیان جنگ ایران خارج شدند و به قطع نامه پایان جنگ با ایران رای موافق دادند.
با اینحال این قطع نامه رای نیاورد و تنها با اختلاف “یک رای” رد شد.
در‌صورت تصویب این قطع نامه ترامپ به عنوان فرمانده کل قوا حق قانونی حملات مجدد به ایران را نخواهد داشت.
اگرچه در نهایت ترامپ حق وتوی این قطع نامه را خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/64908" target="_blank">📅 23:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64904">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRJ9gdUsLx_vxMnUbUNt5JvVcmEiih6gziw31O1GPe1eJRu6dBnunYt01_A2l7cKpMMiCJyEYwzIFkNaP6nf_ToedhdfVBCikYm01gfw_pctiewKQvwVGnQr8J-q-1WO4CTi0Fa160ffMeMLPBZ3pcPVJC8-JfDtfPrf3ZSMyZFs76Yx321SvQLfEXe3FR10B5SLrCpbrBxCjOw4oCM5Oq5aCLGMOjvOuw9nzPCVrZu0URwtNUaQAxlu0TfyyWXVQy5DzxjGp-nuZ0Dkuj8qkIn38Zu0rcaPDLPFDRjN-EnvTDC1TCGM21ea-YtPYuf8asB3WrOg0k-ORF_ehH0rxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uTCI1Eh1Twp3HgPQ-6jc0bbe9TQVwuCs0QQiFGxIbS-kyfqiUJMLPX3Mw_WARzWQw2DL410OkiuN8-oLblVcJUDkVOAWw4uY0tdCYaL6zmyfR9sVcl00q4zBXQk9JtuIkl59xru6PXkVqK2FsIaHSkurx5w3pIE14VJZzkegkrKt4e-eqmlx8_ecmqXPE0MAwH6XaxAMvSVhQhBS2zS0cNLnob7AJmu2L_RbNZ9ZPb1TLlMJOabS-45OER65W6tiqKVBgd4kYpGglERarOTxUb0aZO0xaA4jG5qF5RLuk_rhzVvhGFc0fXA9TAG8sthAcZVZBLVY7kfctsHHgUYZ1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=AH3OWbsrYP22sg4fYwRMmVDtk_jCVqri2wPVp5GwUzCkIS1DnW6qogs186E12qRITpH9i4ZJe0779aQd806NotFK8euujo18LCLoDOdlAoE20gTZ9QTl12Ao5_nr7Gc7QA48op9KbSigoUvtAoaGRZYkhec7mpc7C2aMOmcV4TEbdF4AwrEnLBLS9TVRYWa9-GxCll0PPhtoZycvnBrCqFEBPDX1z6wcDJXYtjL8Cd81n_HnMrm5shNwX8wu0ISgCTRoibjc-ekiEAgFVjMqKrD9cng0LG4fmFAHqmNFUuMtG7KnJZ4FWt52cGL9Q6gdnJpANb8Q_1H7bl8GwUarBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=AH3OWbsrYP22sg4fYwRMmVDtk_jCVqri2wPVp5GwUzCkIS1DnW6qogs186E12qRITpH9i4ZJe0779aQd806NotFK8euujo18LCLoDOdlAoE20gTZ9QTl12Ao5_nr7Gc7QA48op9KbSigoUvtAoaGRZYkhec7mpc7C2aMOmcV4TEbdF4AwrEnLBLS9TVRYWa9-GxCll0PPhtoZycvnBrCqFEBPDX1z6wcDJXYtjL8Cd81n_HnMrm5shNwX8wu0ISgCTRoibjc-ekiEAgFVjMqKrD9cng0LG4fmFAHqmNFUuMtG7KnJZ4FWt52cGL9Q6gdnJpANb8Q_1H7bl8GwUarBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم تو خیابو‌نا و پارک‌های اطراف پردیس بعد از زلزله و پس‌لرزه‌های دیشب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NzYt3vzGf67UAJb1z-owGliNsgl_g_uzFf-LEt4ULEjMU4_cnXVJiSffHzAvM9deCzS_ba4aDaShOJwdsLWcY7yUY74oYiY7gXScv6X6KGYtzeas0ZXsFrpPh98SnF9Hv2c6LoLlanfIK8ns_R6rKwHOpx8IllGLb-9394XHZd8VzKwZb1FYkMHF8g-NBCZ8M0t51vpiFWeEonSqFj-DxhI3kDILee6cGE09qTqIxuXt7YkWe3rViOCiKPHtlm9YNteWuze1uWijSIDSeqbPICGVJwep7dkFIt3z8xQeScSQeye5lsoMYJ5yTdeL-aH2hSza2xbp1pPC18nP3ZkxjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KZxpnbUux2_ng7d9uc2bEoNiXZENmUQvXTKCtr48oXTegXmV6geLlbRZjOFkhn3WVLgJrHk_NRUsK9033GI6rhWUowe5LX29eK3WxrGMjgmV-JYoRNEvB1slCF5TGLdby4Z8DwE1tyFyKMz4T9p5KbnOQryNL9aK8euNe9mAVnN-MSq1S4JREUDykzvAkptxPM0N9IwxttngbF823m_MhglCvTaxsWSXTyeaDg52vxObZIgrd15PnybtcH9E1qrdwJJoVVMnqoTh3DcF09sztu8Rd8MxCHXysRMJtcU0YNUbujdVtzW2hP8_w_NHspsHV7TGVepFnov8f90wAkh_1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64899">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pcDupIcYFojFIzjglSlyci7tjRKoFDs_jOy2-w_lqSWnFaTs17Z9qTBq8u014QK1ZsxLSe8TkPcspMZemkq2PBAoyvdC81E681vSS4CttvXZLeFKHzrEzVPwO7TC-1nwLyW490fQNOKA0xwb5fQ73pF17iIXltlB4paYzcVUrEnxKmHNpfYkes5iH9aU2TgEH1ghiT_xPE0tnBxkqhynq-gz3UF9O6N2ertYcFKwlMXIL9v-ZmomfrF24QVKodVU187CPFs82XmRmAZYZTusJbTrUQEJ3k4J1HurlY7rXdWcz2rlG5j8oJhksCT3ds7xNzJZ9LuKns3sV00pWBQp6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QwzRqQcZjDe16WonEhKcHANGhYnsHlKB-tbAuxcs25R7488p7C0WpEWvcUYJ7KOeoSGYClauhwkflmnDz2Gv7xPoU3iweifNyzycqLhFyj6O6n4o5KCOQ6AvWY9EQJf2kojNiZO6DERsHa-oN-1P6N4abbx3uum1G2mgUOL4fRclnRLoaaEqTfD1CHra67Jbr0yQ07pQjrJOPxMO4XlJ-iIx_KXtSdTyfw4fbscvRPq7xL3i_g1mVeYv-v3ERbjHMrux4rqpGwtIF3OjoLC5LEEZH8hn2IcvRovzXbUWsUDIcMsTeqhMIej4ZjVeMo5wI5-vEJZiUoj1vy2UED5Fmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکوروبیو داخل «ایر فورس وان» دقیقا لباسی رو پوشیده که مادورو پوشیده بود
هنوز نرسیده ترول رو شروع کردن :)
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s46UTl1C-Gf30uGzoz2bysHb4FZSdo7RpCAABhVpo6__rarG-lCo7g-mZCjJ9MJFDHZMdUs7F37ONzG4Fj3qf3R31R_Ou2nG0HlfkgQhhOvIiNTuPWaQUYzT8aWxC6TiLuNCQLQZ8-m8-Zvr-fOfHSpR5-M-LZeh9Z3zXq7BYb3yg0PtApcSK1_Wnh-qH92khxXhbZFJxwySe-tcjMllNVxugyUhvkMl4ZA0Bg4xhb--S1HlmPG0UItX963RlTYkjqizmn_lJ1cUPsiKp0rrbXgGaSKLregKhzOLse_j9thCIpApWH_vMKd8DZLiAiqvtm_5Ce2EKnM-9qPfrgs4PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mvyD4JOLYoUojgdUzsDMpghT5p7On-_rHJMGD880MD0rh-QAUbxb6e_SamTx7OEuRDbXt4sL6BdeqhamhzDkM2UPMncyoEIL9eClmLCpZE_bF5ERBE_CotvVujsg8JGJcCB0P8KgIoLRmNS7sVaS9VcEgfSn7CFjc7wIiKCPFmQx3_MW6WoiTb-ndliM0VftBh4CyqwiaJeiL7N35MwgLhgcpX73PGdqGcO6VyGHlv6Fyg7IVJhgUDfZA7goqEVkE1oI9RRB_dSOxS1GkJLpWXtu8zJ4sul8Vy_08qQ_ghJaRvW8sDTFrjugP3z9p43iV4rDW2mZG4azpb0KytxRdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=lg0Yh0Qfq_jHq_qhfkBgvF2K3WCeusvx7DXB_Pp1svGIccEd_HberyIJSAGIZL-4KTxkAauF174y-7uOQBAXcI4zX_f0O0IyMnAcGVny8d1R6AbauLK8bk7qeUDkohs9T_zuuRjfh91J_sYF5SZY30Gct-dIFtRw-9DUcADyAiJ8sETYyhsH8jmDwMVk0W24FBb6u_8LgHQwMWKWopQZ8u0Z92v86eOb7RyTysWiUnLYZYvBXZE0pkkGDkkms_q65zRmqnLPueGgl_zkrYfAEP5UgNbAhY8KRdtpCrAI2XHAc3mmmMUCPMnjdAjQzCrvrg6W_D7-rl4miZCYcGZUYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=lg0Yh0Qfq_jHq_qhfkBgvF2K3WCeusvx7DXB_Pp1svGIccEd_HberyIJSAGIZL-4KTxkAauF174y-7uOQBAXcI4zX_f0O0IyMnAcGVny8d1R6AbauLK8bk7qeUDkohs9T_zuuRjfh91J_sYF5SZY30Gct-dIFtRw-9DUcADyAiJ8sETYyhsH8jmDwMVk0W24FBb6u_8LgHQwMWKWopQZ8u0Z92v86eOb7RyTysWiUnLYZYvBXZE0pkkGDkkms_q65zRmqnLPueGgl_zkrYfAEP5UgNbAhY8KRdtpCrAI2XHAc3mmmMUCPMnjdAjQzCrvrg6W_D7-rl4miZCYcGZUYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پیت هگست درباره ایران:
ما در صورت لزوم  برنامه ای برای تشدید درگیری داریم. ما برنامه ای داریم که در صورت لزوم به عقب برگردیم.
مطمئناً در این شرایط، با توجه به سنگینی مأموریتی که پرزیدنت ترامپ برای اطمینان از اینکه ایران هرگز بمب هسته‌ای نخواهد داشت، گام بعدی رو فاش نمی‌کنیم.
ما داریم یه ارتش رو دوباره می‌سازیم که مردم آمریکا بهش افتخار کنن
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64895" target="_blank">📅 19:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64893">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CVaT09gbgz0eb4gZnLzD5vyvXvjERSbeVi_DWerrhDkVUcD1hubw3t7hmNDj4XEVywwwN08uFn_mBNN5dvq69sdmfWTdKdNdi9moSBrW7hw1q1swCEmf6CHZZCioEjc89BQ9EGRWjr80z7eBKlaSUj74AM6xEkmzjmAdhQUE56Md3NKbr31bYh0H0NGzzqQkLvIQWZzNRQJ2ODgFgMHlfUtozGvPboCpLTaiI-G0D65-iOnB985P7GhzX0SP8zPKXCqVIj2LnoUJxm-VC_FlUJ-hHy901ncUHsq_-GPb8tjT5OCai3y3SDN305Tkj7CECStw4Tjict3Cw7ynXe0QtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g40qNxQO24i1YEHNdaCNNZmpfjEeDl93USoDskK5clH6Rmw_Rc_y0yyDcIUyO1Ns057e2bNasSvYet2XzM7nIy00YJEPBMFd5X0JvIYgdGzuHWJqZa3WIV9lr2jllCSifMOu96PEPuAWOIfjyBvEFIyA5ZOIFmBtkHTpkiibzt5gQ-IMPEp5BzlE_AsYsocz0dmZbh6Jmb1HsJkdK_KqnZGGp29R-YAx0YxYYeFNTA9fq1NiKt9ax_lO6AX8HVYaxD_u4oX8GNReu2akahSi6AbLRP12u8OJLAMU6eUZ266A94kwKOHSx-60_bGvUzYm4OLJEPpuk8nQfZ0o3e2J5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4g5ExMHZsZegIttjIQn7kB-aUeqb6cywLkIoLvxVVIZx_PjgyI23yLq-NvkheJ717ZSfSKPKjab3li81FSY33L4S0JcdP5P0pCEitERvx94UMw_sJwT9IpFLAgN0z8vQb-h83chEw_3aJCkmgUGxfXwMg9wyIOkza_jfStHn3lQR_Jjqajf3v3-ezBwF63bE_ggduhk2DZQ7kSqY8nMq6pgAvg8VcHUXCrWWeaoTTyEgEM76mXwONubhJt1JTvForz8aWufqBhLm9rro_dLbMKXsk-9rOBwlHLYTo6k8HdEKHhUwxcaQZ6_-rg8qbwJso03mMomN3J2CovLASlNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64891">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=FQFBFUpcuc0hlSVZgMslSlkpYTpw50EMH_PagzCvKiQ5JIzoQmnxiv8ODjy8BETxyuqE4zSQu1zTwxzhaCvRPt8O7EOiPgKCjKT1cWK5q1C4LGDAzSVTtiezhD4aZ_EQZwYQD-2XbkdOdM6vECNK6pUw2EHUf-STcH7XzVhdhlf6lFCJRzMSVu6jEmyahI3SbtYq4jWZEpdwGSq0U_oXCTyU0pfS6_7EEx1ZHlQgZCsQc4cYfSXXYQiUmInWTkuI8QRuOWtFOtHNAv7O5dbHnv8ubqHi-phb-ynUr-o5ta66AnovlXby-uxVZg1txTueQLFsJaa7Gk4shuryaKcxpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=FQFBFUpcuc0hlSVZgMslSlkpYTpw50EMH_PagzCvKiQ5JIzoQmnxiv8ODjy8BETxyuqE4zSQu1zTwxzhaCvRPt8O7EOiPgKCjKT1cWK5q1C4LGDAzSVTtiezhD4aZ_EQZwYQD-2XbkdOdM6vECNK6pUw2EHUf-STcH7XzVhdhlf6lFCJRzMSVu6jEmyahI3SbtYq4jWZEpdwGSq0U_oXCTyU0pfS6_7EEx1ZHlQgZCsQc4cYfSXXYQiUmInWTkuI8QRuOWtFOtHNAv7O5dbHnv8ubqHi-phb-ynUr-o5ta66AnovlXby-uxVZg1txTueQLFsJaa7Gk4shuryaKcxpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ملانیا بهم  گفته باید رفتارت رو درست کنی تو دیگه رئیس جمهوری پس از کلمات رکیک و فوش استفاده نکن. من هم همین کار رو می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64890">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=U1w_tz34uyDPXTfbrqKcF2-3LrjcsbMCIAHzlfqAhurTCOLUpF5aE-eTpMmFvQnRHOpJr6VUASj_kcomiVHKnrv5nvoUVeG15dLlf5Bc8Kzwg6Bn9643-8spaZEHmeZXDqEuTgIfDZJtYUthjneztpsL7cv3zGFGcQ7F7k1Yr7hd-Jpci8PqQzuTC_pAMM9oOox5iNdXeaD3gPd-E9zF6K5jkyk_Z0Iqh2vwXjIKj_80aljk94uHCIrstXU1Bvb5lWVzrfzmhGi7AG850kbdq68PPq0Tc9yU1mNiuNyDFn5sCnON4aCmr5LKfM9-KqJJUgd_7tVWbWZG0SxDDjpg2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=U1w_tz34uyDPXTfbrqKcF2-3LrjcsbMCIAHzlfqAhurTCOLUpF5aE-eTpMmFvQnRHOpJr6VUASj_kcomiVHKnrv5nvoUVeG15dLlf5Bc8Kzwg6Bn9643-8spaZEHmeZXDqEuTgIfDZJtYUthjneztpsL7cv3zGFGcQ7F7k1Yr7hd-Jpci8PqQzuTC_pAMM9oOox5iNdXeaD3gPd-E9zF6K5jkyk_Z0Iqh2vwXjIKj_80aljk94uHCIrstXU1Bvb5lWVzrfzmhGi7AG850kbdq68PPq0Tc9yU1mNiuNyDFn5sCnON4aCmr5LKfM9-KqJJUgd_7tVWbWZG0SxDDjpg2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره نماینده حزب جمهوری خواهان تو انتخابات ریاست جمهوری آینده امریکا:
کیا جی‌دی ونس رو دوست دارن؟ کیا مارکو روبیو رو؟
به نظر ترکیب خوبی میان، من معتقدم که این یه تیم رویاییه. فکر می‌کنم کاندیدای ریاست جمهوری و کاندیدای معاونت ریاست جمهوری آینده باشند
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfFTZjW65zCGkkw-yBZsQPGNS7C4q3r8A0N-dKnxJO2A1IZiIB1W-AjS3JQfJzvCyiswZlbDfip_mIvyP7AuuSj3UoCaprTm15Vz2rquIefBZ0SuVuFpnXLA5n6zdxwMAIFum_577eStVkaHUhRvpwh4yqmMKSTqdXchFyl9na_DL4enCeWsx11yU1fYhvTo5JeFC1vGIG3hFrqajelOg2RjPpOHvVJK2HwegwmmgqHstwiiInyPqwBuWoY-IWWceJj7tNh1TZSNg2JKbUprtyPNXDskTu-BavptLQW3EX6yl0F0TIfZDfThzIttcgdW6voRmP1K3vztl5pfMwwr0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tkbOCIDU9arKG952fHNbN1CIQbb6LYI09wdRMtfFpRdqPySgbYc0rY0g5Xk62cfpg2DC04S2RDGIY1TvZVeizP9ULH-UUlIpxRiEgmjgX4YFV3SNJZMQl9oklRtRyayREJWrB7eSx3Mp6k-jbKV_DUGx1wwdeoZzfhC2GZspGmUwH9qQNrzUIk_YhSUsntRUBUCwKdeloesRklHa4sAgYcmnrEZhol1XBAXVzsun28bAIR2yTsjZkh3q7jd9y_Mrza0-KwptgFLoYeimlj5umTZigF9np27eXgzW9blklRs3qMxX1820rSmLKWpNgk4UAjl-4ou7rFbKRdWp58W3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/news_hut/64885" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64884">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ به انجام عملیات نظامی فکر میکند اما ازسرگیری حملات آمریکا به ایران پیش از سفر ترامپ به چین بعید به‌نظر می‌رسد
+باراک جان
اینو که ما خیلی‌وقت پیش گفتیم
😎
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64884" target="_blank">📅 20:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64883">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64882">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64882" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64881">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_yxgzxYfpFjvvDis-HmTRvd6fZ63PJOu95SRTP0k2uc3BKen70hG_rVptoajPhrW7rCGCD8Bx9VAD0RafwYNvpaPAp4QzgZjYo40Z929EFHlsKqec17yNXBEZYQauQhOaEXPWFnO0g0oHGa8anuyHVfbir8fK4BCKNrY8Q1VNIjc7vwr5mebsv1yNI4zoPFRzZYJOHUO_Pl5VnnA5DlJ6Da5Ym3OfismZrXT4oTceJHf6F9Hv_bTT11pvZctSX8pMzD331RFAlMlWSW8kJVpOpHi6wcqCZj14S3A0NlpLCR9wTYGd9VSycvFf8btm8V5An_euc7InoTuwLabc9doQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvwLw0LrT7vtY9Bm5bSpHRGEF5cM7XFNaeVK5qs16F0OKKzm_xn1JoT6ENO3_jmsslAjIi17YNfQ9pPNldlFzWyXIVQblsV39Q3ycjX_kJs7HAuf3HSy1X2sXV5Birq84DzBfiO6s04onTpFmt0NW-ilTHdOVyc83gJuPjQgSHe9W6Wl0O3002gYOqfeMy9NVfJrTV7veaXMb2_WQtXMdRKFtR1xawRKJ7wxu21uHU-xpYJhMjoXYYtyDnwoh5Yk7xOBVTfOXrVBCQzoyBS7PwqX-bOU4O0WqiedS-bcmfwFZdRxWJnwezOUekbmQEhyDR9bmwhQxJKMbpNy3qfGIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
لیندسی گراهام:
من از تلاش‌های جدی دونالد ترامپ برای پیدا کردن یک راه‌حل دیپلماتیک جهت تغییر رفتار رژیم ایران قدردانی می‌کنم.
ولی با توجه به حمله‌های مداوم آنها به کشتی‌رانی بین‌المللی، حمله‌های ادامه‌دار به متحدان آمریکا در خاورمیانه و حالا هم این پاسخ کاملا غیرقابل‌قبول به پیشنهاد دیپلماتیک آمریکا، به‌نظر من وقتشه مسیر عوض بشه.
در این زمان “پروژه ازادی پلاس” خیلی ایده خوبی به‌نظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64873" target="_blank">📅 09:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64872">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
📰
المیادین: منابع المیادین جزئیات پاسخ ایران به پیشنهاد آمریکا را فاش کردند:  لغو تحریم‌های آمریکا علیه ایران آزادسازی دارایی‌های مسدود شده ایران آزادی صادرات نفت و لغومحدودیت‌ هایOFAC مدیریت تنگه هرمز توسط ایران  گنجاندن بندی مربوط به آتش‌بس در لبنان با تاکید…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
