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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 22:24:13</div>
<hr>

<div class="tg-post" id="msg-64991">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43db173db6.mp4?token=UYJX74dHEB-etqzit5h9pS7ofD69wWJ-D0pr0hidYjAXu4DSPcgzv0Lh_ClhfMvQcT0YCKEodkpS38Q-vLARS-ABfgYCQVfWgbHRjDlgX7l1a3wQnda_tDGLEfWO9fQUuTpLzdhP4RQXapsF8XIFrM2Yz4nF2IVWahm5cCa5eH0BJa4R-0oIUMgjAzT9jILv6PrfRrabqRAsRXRbsArAVsStA6BMF2mNfEYa40uqthdPVRIhIUexfd-_X-R65CNRL7MMYbhybuIFghrPA7WcaKGWZEG6vp_XeqjCM8s62P9ezhJKyZ-M3PgKtppOQ0ALRQ9S0QtdT42K8xXWoRBJjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43db173db6.mp4?token=UYJX74dHEB-etqzit5h9pS7ofD69wWJ-D0pr0hidYjAXu4DSPcgzv0Lh_ClhfMvQcT0YCKEodkpS38Q-vLARS-ABfgYCQVfWgbHRjDlgX7l1a3wQnda_tDGLEfWO9fQUuTpLzdhP4RQXapsF8XIFrM2Yz4nF2IVWahm5cCa5eH0BJa4R-0oIUMgjAzT9jILv6PrfRrabqRAsRXRbsArAVsStA6BMF2mNfEYa40uqthdPVRIhIUexfd-_X-R65CNRL7MMYbhybuIFghrPA7WcaKGWZEG6vp_XeqjCM8s62P9ezhJKyZ-M3PgKtppOQ0ALRQ9S0QtdT42K8xXWoRBJjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🚨
ترامپ:
ایران نمی‌تواند اورانیوم غنی‌شده خود را نگه دارد. به محض اینکه آن را به دست آوریم، احتمالاً آن را نابود خواهیم کرد. ما آن را نمی‌خواهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/news_hut/64991" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64990">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyXOcgMDloepFRV4LkQhkXXLW6Lznj_FTM06lpWkKnEk3UC4Ekhd_j1rhryJntUzhOfBsd0Krmw938kqJCslo5rHdBT1NBfM2FzItDikPfOqI6pAU_5MM2YQ43DoWeQbKhe04fjzruZLjsEWFIh34vZ8P2mlcbiFTwanI_GZDhLktadmbYl4W7VcO1TGOvP5mb6Klbc2xKeafPb2WlW8FiVRZbJkFmkAbH2ZY-EwNpgHwiE3vags65M7x99JRJdpdm7dwsp8Wm7CceLyXvKk4Z2M30Laktaw9b9Pap4LCJiQiizWwjeMxsUEKDcgZ8ojMxWKp9fHvsVddHqS0nSHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ یه پست از نشریه نیویورک پست بازنشر کرد که تیتر خبری‌ش هست؛«چطور میشه تهرانو تو سه حرکت نابود کرد»
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/64990" target="_blank">📅 16:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64989">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAOoxdRcARPFRjZ9ziZ9OmBiUgigH4N8ZqZo4TbrHRW5w4DVDh9Msb2ByS1CFw615V4aGcyFu0EF7vgBsZFj-Ubvn_cE9y_YYyMILXVlU8zGcgO5twIiwi5GdZ463Ea7D-jDFi0kUCRGReXJ7VgS7CGL8lUK4SVzwoFf1rqp9gPRa3t85MWBJJoa-O5BROS-qETFOFY0JrREbJcGUtHh0hJ-1PJrc--HaMMY7gNmXwolzvAQisZlsrqBnVvr8Ig6oGmcBavH1A5hmNh0f-BjKLkVwItuIgRkImuQJHMBD2LCuJv_Hs7wfnJYiZy7M-2NWvahVgHUcdi2jk2xmA8QBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ جدید هزینه‌ ریجستری گوشی‌های آیفون
ریجستری آیفون ۱۷پرومکس، ۱۰۴ میلیون تومان!!!
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/64989" target="_blank">📅 15:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64988">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eppa0wiVSCzuY078ThxqJoExD6kfWme_QUWBZolYoqp2R_Tki5YlrRUcEXpYGyrKuLK49IGAeU2_wV99yHm0N5-TOYr6jEVlcRMzgcL7DD0sDbPsVYnAwaDWPBPaEMyair9Va_E4AM-nshDvtdIaRIULGraXiF4QxHdHkjjY4BeCyxCgCxawZsvx3JICwJJXI1RCHGJFZGxyrioSiT5JP8DTtI89l5m2NWZDoB0I4CDv6oQiVbx1syNRcCjjWAXXQuRkoRBPSJ34SUq2a-02pb9FBuN72B_QHQ5aX7B-SVaVtg86yvbSmvE2V3czSpHSOsoLdWHDvVan81DgarlM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فهرست کاخ سفید از مهم‌ترین دشمنان امریکا که در دوره فعلی ترامپ حذف یا دستگیر شدند:
رئیس‌جمهور ونزوئلا - مادورو
رهبر رژیم جمهوری اسلامی- خامنه‌ای
معاون رهبر داعش - ابو بلال المنوکی
و برای رائول کاسترو رئیس‌جمهور سابق کوبا (و برادر فیدل کاسترو) کیفرخواست صادر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/64988" target="_blank">📅 15:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64987">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
📰
رویترز: منابع ایرانی می‌گویند رهبر معظم(مجتبی)اعلام کرده است که اورانیوم غنی‌شده باید در ایران بماند.  آمریکا می‌خواهد اورانیوم بسیار غنی‌شده ایران به خارج فرستاده شود مقامات اسرائیلی می‌گویند ترامپ به اسرائیل گفته است که این اتفاق خواهد افتاد دستور رهبر…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/64987" target="_blank">📅 14:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64986">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
بندرعباس ۴.۶ ریشتر زلزله شد
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/64986" target="_blank">📅 13:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64985">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Te5-zBbsnpOEieuUCJqxZ3eNM0tnBoEs4pcge4PBrRd1HpvaO-iDz2m4f5lzNmK30hyFxi-vv4wJRysS1PGgOhq1C9fU8h0TOT-W41qow0r3L6u-I3w3tlp_J3FZ7dWAumoWdPZH7aVkfqZ2ItuoviLXDnF3FwL5kONv-gsavliOPl_Ss6nRrTytRNCVvsSD4E5ek7-n7suHrJwAUuTpB8QxALTl-LlJacZKTfuJv8O4sT1jsWYFsUUu7BHC4kYEulzKongEKzFIGt6sTyydg-MVgVK14Q28WkNRCMbRlJ8wa5JRQ7inO8V1bv8tovFDefylnoH41jlktNuD6YIQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شریعتمداری: تا زمان شکست امریکا و کشتن ترامپ تنگه رو باید ببندیم
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/64985" target="_blank">📅 11:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64984">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: اگر فرمانده ارتش پاکستان به ایران سفر نکند، توافق نهایی ممکن است ظرف چند ساعت اعلام شود  @News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/64984" target="_blank">📅 10:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64983">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خبرنگار: آقای رئیس جمهور خیلی از خانواده ها در آمریکا نگران گسترش هوش مصنوعی هستند، نظرتون چیه؟
ترامپ: هوش مصنوعی عالیه، ایران نباید سلاح هسته‌ای داشته باشه :)))))
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64983" target="_blank">📅 04:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64982">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: کار برای نهایی کردن متن توافق میان واشینگتن و تهران به طور جدی در حال انجام است و دور بعدی مذاکرات پس از حج در اسلام‌آباد برگزار می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64982" target="_blank">📅 18:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64981">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: کار برای نهایی کردن متن توافق میان واشینگتن و تهران به طور جدی در حال انجام است و دور بعدی مذاکرات پس از حج در اسلام‌آباد برگزار می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64981" target="_blank">📅 18:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64980">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SPRG3FYs-6aB33qN7O-jQmVBX4rR96RUPYukjTBnimWXzFGXq92rjtg-Uxf78zhI0HQmlPQZBsMEQqktESS07f5HKjkeO_h4_8tozT5zzJZwgQCJwKmBgGQUh9-07fInPceut6tvbhPbFMnfjY45vzLdprHqCwUST8agTkrmAnxs8tp6oHyfZUqzwz_pU2ru9Yxor05Swg6988tLnDHba2qdcv5nuWOAvVqrq0aLbHZKOrUx83TI5JPWMUDB5G6cNSHT2TT4uEc8ee2hXwY-0LH5fpqEWdDeMKC-gekq6tCUxnXa1xYS7pcrRuUFNN-HQqnYml784revR72ywFUlyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای مرضیه حسینی خبرنگار ایرانی کنگره: یک منبع مطلع اینجا در کنگره به من گفت که ترامپ روزهای چهارشنبه یا پنج شنبه پیش رو، به ایران حمله خواهد کرد.
به گفته این فرد، این حملات برای یک عملیات “دو تا سه روز” متمرکز خواهد بود و به مراکزی با هدف بازگشایی تنگه هرمز انجام خواهد شد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64980" target="_blank">📅 13:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64978">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dl1e29SdQg-COcKZUwo5S5Mx0FhJhvgNtdr3wVp2dOF1hO4owCp5Un9gkn3FbEBmSZhNNDR_tD5fi89ZNtuZMi4_2NL0ozQzx-nLWrHiyVCOF9I7VJdLJjFqGpVs9G3Z_cI6qfqgGN6ON067bbSfYcnxKkJtF3r0e0ejdgJJYPa7dOHjpw2maxB_h0Akjo1SvuPD9aWy8PkxCKPCP1MNRFkROfzAkDsYSdKDxQF9BAkWRJJ4LQXJTnpSJYFB_JJydbm3oSsDCRnSVo7Opd9bR04YJdLeI5ZT9pleH5QjaHMy_lki9hopbJ98KyV4smt4BxMM7hrdUTm6gBkNOw_ZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWpJdVlUHveD48giNN8ySyngZCZHG3sQGcFafl1FBhUaul_nE8i_z7oG_m9DGNsZxFYRX6I4n67CyPskQShXKb_EUDM8gg6inPSctQKZ9PSuVWOQWdVS7M5Tzp10KOaj0xpAGtVf8eyK84SKwo_XgioBWC1sgP13IxegSwPhXu_dYvmBc1D5iw90-eJT0IwOOt-mzSvfozBlSdWP5CGMwlWtkRp2Uy0fOghdNK5_drhmuoog11DWRIeqBgxhSMGE1Rb5o1FioLGu482rIj6QHEYArJSg2qHK6uquR_dLTqowUkNI1QJj6szCyWBWW9g5Zq9qyW2fyc9eP5-mNjJZgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
گزارش NBC از موبایل جدید ترامپ  به نام «Trump mobile»:
مدل T1 با قیمت «تشویقی» ۴۹۹ دلار به فروش می‌رسد و به صفحه‌نمایش ۶.۷۸ اینچی، دوربین اصلی ۵۰ مگاپیکسلی و حافظه ۵۱۲ گیگابایتی مجهز است.
گوشی ترامپ موبایل در چهار نقطه از بدنه و نرم‌افزار، لوگوی «ترامپ» حک شده، پرچمی آمریکایی با ۱۱ راه‌راه به جای ۱۳ راه‌راه روی آن حک شده و از پیش، شبکهٔ «تروث سوشال» روی آن نصب است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64978" target="_blank">📅 13:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64977">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64977" target="_blank">📅 10:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64976">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
📰
نیویورک تایمز:  ایالات متحده و اسرائیل پیش از جنگ با ایران، طرحی را برای نصب محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، به عنوان رهبر جدید کشور مورد بحث قرار دادند. احمدی‌نژاد گزارشا در مورد این طرح مشورت شده بود، اما پس از اینکه در حمله‌ای اسرائیلی به خانه‌اش…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64976" target="_blank">📅 09:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64975">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دموکرات های احمق برای بار nام خواستن جنگ رو متوقف کنن که بازهم رای نیاوردن  @News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64975" target="_blank">📅 08:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64974">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y84fs079zHmHkk077wHgQqTxoztbl8NpjRuqlMCbXcdK5PGYThW3mDtGLLGBjmH5OcZGy217ZqvsKUN4BuuDw8T6kKu5n1UothFaWXAt6lyNJ3eek6NhH0SpP1tOTm5G1pSYdIoxDGpta9Iwuzh1kgYOGlMSsOYFzfhMYuWAl-MagiZSRr1eu6-Sovnak1cceSPe1xyCK4LofZ9gXtOXHZ6vSkL5zVnYygvRnyP7JPbgCzx02pk0B3e3De5L7xZkWZ_LC7vg5qWK7F1rUySTFwYObXmRLNClI2TJpozuJEkv4guMvLA5KQXHNUrfA_M9thHn0j3XaVPRXvSNvehiyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور لیندسی گراهام:
امیدوارم و انتظار هم دارم بعد از این چند ماه مذاکره با ایرانی‌ها، دولت ترامپ هر تلاشی رو که برای دوباره کش دادن مذاکراته رد کنه.
این رژیم ماه‌ها وقت داشت به توافق برسه، ولی به نظرم واضحه دارن بازی درمیارن
من ترجیح خودم راه‌حل دیپلماتیک هست، ولی قدیمی‌ترین ترفند ایران همیشه این بوده؛ امروز و فردا کردن، کش دادن، کش دادن، کش دادن
در مورد هر توافقی هم، منتظرم بره سنا و اونجا بررسیش کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64974" target="_blank">📅 07:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64973">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xppes16jBr6icjVEyfw_RVuywgbv9JAynjxL4z_DDKmTexdGrFDLJ71mMZFPGy4LMtnZYppTEvrCBhSoATslT-ADoHBDX1QPfO8kWdVn6JR3EiCNVDeKT4Y6-K_36_NTAg2filUeQctNQeJ-hCP1_2iOQSIuWQOugDVbMiGXYPoZK7SbT5_SibaBx2Gq6DEuE8F82FvZz8yVTRel-aX_-xd9CY90_f3baw2fJSYK2XMjSYPxenZOqZv4O6oHttWfUplvfg7Z7cHpO5juiq-2s8g4tf94LDCOfWNiEIXSQ0da-DnT5Wquu0ACPntE1ZMkg0a-S1CJuQ-Gua-xk2_S2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غریب‌آبادی، معاون وزیر امورخارجه:
امریکا میگه دستور حمله رو به طور موقت لغو کرده و در سایه تهدید می‌خواد مذاکره کنه
اونا باید اینو بدونن برای ما، تسلیم معنایی ندارد؛ یا پیروز می‌شویم یا شهید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64973" target="_blank">📅 00:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64972">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🇺🇸
اولین اظهار نظر متفاوت امریکا نسبت به حمله انجام شده به مدرسه میناب و جان باختن کودکان این مدرسه:  برد کوپر، فرمانده سنتکام: ایالات متحده عمدا به غیرنظامیان حمله نمی‌کند. مردم ایران دشمن ما نیستند. سپاه پاسداران انقلاب اسلامی در این مورد دشمن است. تحقیقات…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64972" target="_blank">📅 23:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64971">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64971" target="_blank">📅 23:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64970">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/64970" target="_blank">📅 23:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64969">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=Vja8pFwMfmWtpnjP0YZnwy-J0S6EOsZD93TuEh3xg3NBCbqDBpY_7E4e_ADJTU7m55htS8dOL46o8b6a3ZD77tM_JLEjdZDGzEoU72HXM38amiOktWgwexg8eSZjiZauvek4xt6BfRW_aaNXwe7CZTpIyyF5WvqDJ7EfqkUp-UWwdokQSViwLgTQzfxz9Dwyxj62_2rzY-B7kL1Kv8RuZN5weR13GV6s8yd0ZDORp1NRzMtoBB5iSYIEUdbpXyiwioo0iirQsM95IyNs6X2hYQEEI8cO0K-rQkjk5wZ9b4ReQNCFmWV5soomkbOV6Oh26TtIdtf321ZJTUT4RI8okw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=Vja8pFwMfmWtpnjP0YZnwy-J0S6EOsZD93TuEh3xg3NBCbqDBpY_7E4e_ADJTU7m55htS8dOL46o8b6a3ZD77tM_JLEjdZDGzEoU72HXM38amiOktWgwexg8eSZjiZauvek4xt6BfRW_aaNXwe7CZTpIyyF5WvqDJ7EfqkUp-UWwdokQSViwLgTQzfxz9Dwyxj62_2rzY-B7kL1Kv8RuZN5weR13GV6s8yd0ZDORp1NRzMtoBB5iSYIEUdbpXyiwioo0iirQsM95IyNs6X2hYQEEI8cO0K-rQkjk5wZ9b4ReQNCFmWV5soomkbOV6Oh26TtIdtf321ZJTUT4RI8okw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره اینکه ایران چقدر وقت داره تا توافق کنه:
دو یا سه روز. شاید جمعه، شنبه، یکشنبه. شاید اوایل هفته آینده. یک بازه زمانی محدود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64969" target="_blank">📅 18:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64968">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2efb45471e.mp4?token=FdkVZODwxe2moOBrIG6RkxmWbROGI8BL1LZqKE_pYdeB2OaPzOw5JKLuo9qNPhxCmzI1NMEeIFgIP77BbUe4iLPdITK9KE-TdUfB951EvHBk2P_39V9PEO6YsY9qbgomOtVt_eyPsti575riVUyVHN652A1IDW_307349w8zwrGnVjKisUz9WHTkZYYrmC2mnfhcVOMu52IhHqrSyXqCopuoJQqZET8PuFMNhYvm-Aj8fOdJRmhKC9Bo6v1_1Kd2CwETEDbdKIoPM5LkEfb8oMg-D5CNjEAppn5upxHA1hdcypMX0E-0c3OWgrKQq1M2Y0K9IZKqS6Q8-hgCkyYzvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2efb45471e.mp4?token=FdkVZODwxe2moOBrIG6RkxmWbROGI8BL1LZqKE_pYdeB2OaPzOw5JKLuo9qNPhxCmzI1NMEeIFgIP77BbUe4iLPdITK9KE-TdUfB951EvHBk2P_39V9PEO6YsY9qbgomOtVt_eyPsti575riVUyVHN652A1IDW_307349w8zwrGnVjKisUz9WHTkZYYrmC2mnfhcVOMu52IhHqrSyXqCopuoJQqZET8PuFMNhYvm-Aj8fOdJRmhKC9Bo6v1_1Kd2CwETEDbdKIoPM5LkEfb8oMg-D5CNjEAppn5upxHA1hdcypMX0E-0c3OWgrKQq1M2Y0K9IZKqS6Q8-hgCkyYzvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: دیروز چقدر به حمله به ایران نزدیک بودید؟
🇺🇸
ترامپ: یک ساعت فاصله داشتم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64968" target="_blank">📅 18:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64967">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:  ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم. خیلی زود خواهید فهمید.  @News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64967" target="_blank">📅 18:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64966">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9954bd7931.mp4?token=I8CnyWKk5UsJNybJSaeOTQHJDlt85cZ6EY74Z89XGVp_fRyZ-GTpLaRSJrpp2buXajQeXFSpiE_u7dmPMC-6l4QcVHOzG2y_hkZpQ9q7EJfoJaPk4f5ABKo5SNiejTxRjfmuEOACmn4amqIWqjdIPFGQAVghvbOtHbGNN_VriD1ScsFAfiTCAtaGBsxJyVpK0OF6pGYBhIYOSYnJwP6hp2vUJt15_NEy5SMWiUgh-rVpFDhZSpvGDip82Hz03SZelBg_GYOmGTY73VvO-8h6smtTOCc3qy3_l63Zm9fLl5FARX4wLyoHPbXgqvzWIqeEn5OfIv4jLbkU7m7_YqDDPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9954bd7931.mp4?token=I8CnyWKk5UsJNybJSaeOTQHJDlt85cZ6EY74Z89XGVp_fRyZ-GTpLaRSJrpp2buXajQeXFSpiE_u7dmPMC-6l4QcVHOzG2y_hkZpQ9q7EJfoJaPk4f5ABKo5SNiejTxRjfmuEOACmn4amqIWqjdIPFGQAVghvbOtHbGNN_VriD1ScsFAfiTCAtaGBsxJyVpK0OF6pGYBhIYOSYnJwP6hp2vUJt15_NEy5SMWiUgh-rVpFDhZSpvGDip82Hz03SZelBg_GYOmGTY73VvO-8h6smtTOCc3qy3_l63Zm9fLl5FARX4wLyoHPbXgqvzWIqeEn5OfIv4jLbkU7m7_YqDDPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم.
خیلی زود خواهید فهمید.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64966" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64965">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=IHKnSAAvTPlOVeLttHeX67cvRhFmmmA9XQ9cGxixTu1E1C4RzG7OZs4_WEXXhKRsmPZf9QIYwRjEf3GGfPnwe8g4EVK4ff5An9CXi_r4Nbp5NaxcoDfufNrZGUN9MAwUYJZEvj9xLdYmR0_d5kmMgbOWY0hUdW6pUi8HsobVaMCY8FwT5HGuIhcJyfrj1BGvmC68ANZm-_vGAQ_KATFRnBdk53bfVUSNrRGi6yvyFikbb36DGxLbGN6WXQFzLstNaWLjrmfkEkD7DT8mIyDhd7S60rqP5lmaH0ZphSsFBTaDf2dURBsAH0KaPGTlj5sngHNiMvs1lZ1PC3XoE2YBsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=IHKnSAAvTPlOVeLttHeX67cvRhFmmmA9XQ9cGxixTu1E1C4RzG7OZs4_WEXXhKRsmPZf9QIYwRjEf3GGfPnwe8g4EVK4ff5An9CXi_r4Nbp5NaxcoDfufNrZGUN9MAwUYJZEvj9xLdYmR0_d5kmMgbOWY0hUdW6pUi8HsobVaMCY8FwT5HGuIhcJyfrj1BGvmC68ANZm-_vGAQ_KATFRnBdk53bfVUSNrRGi6yvyFikbb36DGxLbGN6WXQFzLstNaWLjrmfkEkD7DT8mIyDhd7S60rqP5lmaH0ZphSsFBTaDf2dURBsAH0KaPGTlj5sngHNiMvs1lZ1PC3XoE2YBsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار طرفدران حکومت تو تجمعات شبانه: مرگ بر امارات!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64965" target="_blank">📅 15:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64964">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
خبرگزاری مهر: صدای انفجار ناشناخته در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64964" target="_blank">📅 14:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64963">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHU-RCOBcXJl9Z_P-SwZIMoWO7a0k7Yte88SWiGep6xZ4p5kjR2L0PEL6_slSuuM9fL1B_UILHLYxV5HGH-VRNDSwoMeq2Yw1D0kwNg2uyhgRZExu3OdWMhiEXpLaiDXu0eI6G-cbE0vbq40Wu0NJlVoRtwm-yCsyA8xvhi9Zs8teY7qJ7XHvaGdcun8w6pztnDSSZObWgtP7pezaGzXIetQjozabq1ACspBqA5m3wtgh78kjMGa2Y_xJq4-CiBnP9g3vQ5DltAG6hrBQwn8GcTAKq_9e3Kny-S94GcxVMWEdJ70tbBDTg7wzEagLj7QmI17mrsPcWYiPZIIySvhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:   من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64963" target="_blank">📅 01:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64962">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4qfr4NxQJTwQf8_a4RL7POdjOGpwubK0hBT-8aDGpNBVnFPqgmFyfWmOTRM8pSHtBtZYT5y2RcAzLMBv4UXOtWNPxQu6td48QXenZV8q6Ln0TTAz1GijhCcOGz7AW791TV8HVOo_6dE93hdEUjHhME4_ITxdSht7Dm6o8tbS4VTt8ZA-PQpeX7_RZKAMVUCKkrY8I7P4A55d2oL8HxXa9Kmq79XCyPNewlrFAitXoz6Kmsz4Uc1ZqE5DNfSB_QI1bpXoBS4qmYlZnyY0Etc4TiEDzlyEehUzEvGsaVEJn0Oyat_puwIAI6RS2ZPyPmAjvongaXZNcFFLCFsd9bVzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به سلاح هسته‌ای دست پیدا نکنه.
با توجه به احترامم به این رهبران، به ارتش آمریکا دستور دادم فعلاً حمله انجام نشه، اما همزمان آماده‌باش کامل هستیم که اگه توافقی به نتیجه نرسه، در هر لحظه یه حمله گسترده رو شروع کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64962" target="_blank">📅 22:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64961">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inoxP4RgNn0PRkO5b0Cuy53MVFM5VnFWHByqo-9RNKTXgy4pOGpF_iv_7EJ902LfRwsvN-R2eBweabMjf41jyt7n97RxWZ5d-pw3zx1XgN6PQOQS_d-5apgAFyeTlcwKVp1-b8MtaSTLg4mBHel_S0_Va1IsmuWEn8eDF8zGbLcDKBH-oWeaBNrITyWZJbro-7v6r0ROmp1CtuhnZsq3ziUotpyZmDUmsCNwy3gl5vegZGf9lPUxHci7ppdCukd-Dd4afwIBsSkx8uR1LqThYN7NYonkMYHOfUG3NwbGY4YgUvrFHNY8WVNI75ibp112SiDZ1tx7Bb24tS1NUXvpkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
«اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» در حالی که پرچم سفید نماینده را به شدت تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌شان همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی بزرگ و باشکوه ایالات متحده آمریکا بپذیرند، روزنامه‌های در حال سقوط نیویورک تایمز، وال استریت ژورنال چین (WSJ!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و همه اعضای دیگر رسانه‌های خبری جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است، حتی نزدیک هم نبود. دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آنها کاملاً دیوانه شده‌اند!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64961" target="_blank">📅 18:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64959">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ggBYPu_g5TMg2xvYIvVg9y_1RhMgo8kJqIawKNEIFGsxqBBzyymoLM8Y_4oPv9B25fXqO516u0_d69URCwFZIhw33EyrlC7oTgge-AR-ZRHTF0X-bVaivFm8W4mKnlrDefu4lQ9pWdBeogrPxv9MnJcXVzOfRhPjKnjBroxND0xqn_m7NM2QpiVFEEjyj1kS1blrpWbs1gherFWwf4pZFJDwjS2moHn_kLwEExvNjNIRLX3fgowpq8sGlhOpI6eq4m7AwbPbCfjWBpeKxe1i_Den2Dw3PaHmzrMTYYj6WyrKC357d5rL7mCTcwspYfyazzbLgeZMVTVySJLzFCXHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jo3mmQ01D9tm7NLGyQVBGb0Ch9H2kktgBsyG2jy70Gr2XcVi4JpN544FpmepbulFWa-ZGCJ-fRzOmxlJZCSUbi1wF6kg8CnkJQ_Qc0mig6iqFWis2hc0kweZyT7N2dP47NEdX5FYiaW1SFU4UKrnC6HZm5tPcgY_F51draiAjnsdzRkFIT0pO-rtv_6-EqnqZ4dO7RMg4AcyeX5HguEXw6yzznS8oNiGGmTkGqTvwWsEGd20wfDXuhHoUG9Db_B_FwJQRHzCGrkRyoDD6lRapc6fPdqOkSr_nMLkUkmQGnhcMRpyD5OrxKcVajQftXadjt5jDQVJZPCMbA4z3a8XcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت خودرو ، ۲۸ اردیبهشت‌ماه ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64959" target="_blank">📅 14:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64952">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C0TNMJHget_j5xbAl215C3_HJv4SUDO1Q1KkOr-yDTAISKK-jFWTtv7vKZvZPd34Rs5PHbJHMn-Bb-IgRlTxzOSaDS09QZTLNl5yjtPiTAC_5ykV4laFxdn9ofpw6xjRM_iMBW8RXtlv0kziLRMHI0R0NNe1ml-2ck4FQ3CIjSwEzAuBj0KumXyZR0fGRq2ZHZop580WpIbszhd4F2PxXSdxQVtAZhmJyOmm68T8jZyWUNnwBDvWkzIyzdQqz9y34h24Ue0vrqZhA2C6iALZSpxoxa5XQvG-BhtRW5ofkFEDzlvNjhQC_Qfpx2Z9ZFt5EkBQveW23RBdpbpBhLmMvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qrsTEGNu1gz547mcnzBVU3uNSiRJbOIKhT_-U2oSSkyFU1XjRnouQwvJ5_0mqehFLGUx24wf5S1RzSA2hgnBnU14a8Oell_h2jHtty2juaMsy2P8i_wFP6Xao5lKVxj-MR8da6uI5Bijbeb_8qB7Ei0NLepoU73Cr1rAToeWkaDpyUNEndAvpqIDgBIdoyGqOS6pa66FeIypAHaSbLyg-vqNZIDtHEjYmNT1sG8IelZcXlK3ybdMs83KgsVxt72UMEG2sFxv0kUNtRv3EXf1mVxAX6poyLa-B3vPBvSvxVO5PA7P0RC_9aJjckP9LYgumnw7QOaXiwtql5QTY3qJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iiCnMC3jQVl-UqV6CSCoVG7G_Gh3N1sbv9PpXx6FFZDlBnSOGowiBvacCv84CwY-FYkb1fI9v8tIIgTsxNUOLTF59qRtYjAe7xQ7rWoQcBh_gQNHJA7YlxfsLMfMZI1i3XXY7YJR07eEpj7XNUnPlFyQ1cC5gVIi0mGCIiW2ZTV93nNkwydd86LjO5kGHNHgV28AxXNDkwsIRCNsrJs3__kXhUpVKfOuU8Dus_yb6CKCxeZ05InUfFAEWa84ku6MssfuNTw9BbZ59jg1zf3_qor3BVb2-2P0I-23bw7GBCmhP7s7DefiKj7x3zbJYv77xst0UE76KNZpGBzDPQVahA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rCiN_mZ-G4FOXgY-aOuJvkzeXJKtwAu66sLEWyWWzp_Ym7aftR3gsAX19Ad2chqoWZjGxziaSDCnSLtJYHwTROKNUBCF02T-KpfoF9PJ1Z83HzfoTqqtqqByZQ3RG81vc53VrV82-1dhBLEJQjvZkJmStLlOafpvkgPfwdx_ziwNpcikFZq2NnVH1e4A-w_TtOYJZVFyTHwAQYiODxl0E1t_vfW_nrI8jGdTtgiD3Li_brP-Hrw-A_hbbDxLBQKQa7P5Pl6U3HshB1WcuCBPMNzycwBEjfyKH6i6sWeMDmtHljjvt-DIs0WKZqYAegsToLPqmvfsNBQToM41s2MV_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gj2Bg9BbdDTs7EEuTVenm0kyVkkmHHsBMEz7wMtSyfTmBbPouUN9YB-mg6mvyB-rLc10dZ_8La6GmJglU3qT2gAVbJSZgbXcewDopSOYP69mATU6W2DJHZHcCQh_RjqajhEIIE293ijSyjcVcL48z4mEdpmc_0F9VPXy-0_4_a3Rq3abVaUZL_QI8awq3c4QItLvp5H-O756NbAcXnw-iqpeiJ4NSNI-2yxMqKFq1aRI-s8Q2-1oAWvARdpk1nzc-LqJ_Sr575abN6EkFQXjNWk2xV00tGBB_92dwj-hSlQywosTZgJcDsJYtBkmc3GgUBa3iLFxOYa1ORbxdd9Oyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XAYuzS5XVxrL9psN-j_vedvajbCxXAKR1jYcmnguKHdcYex3xFy79LdW01DnGiaavx9l_1UyYcNpqYLRQM0ha9p1IPf1FRsqlLGX1n9A6YnMW3bKGonvGmoMPmNzeKVQmYVnWtfN3Qs5UbJY208W1cM079DXp5ZIsqAZP-jfpHk2LArAcYP5iJeRkLfJcs_VR6phsDIqGdTEOrXN50sLAjS-UeEFOd1eI3t2RCYnnIRk6zgC35ng7uxTpVcYJXshi-d1Z-LpmDiuQoQgfG8OESXP8wXdgKj4lmwT3F2IoLyW3YtkFBlWj46sZUOooPkKuAK-7LUJN4pkazCQW_oJ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kqblbK4xn7GN-eqpDHnSkI61U2KyDNL7id8MMbldmJmgXPeSrB2iLnMHFHC4AmtRnDXPU_QUc7uaXO57OH6u5U2xtQrIVLDnxSdbb7qu1UoTaxMIWDtQJtDMgjVEzzrcX01RzJscsyKxf0BZgYVKZqBDuCHsjGoa441ZWC0xSQXA3GAmgZdktJoAqAQyQB1sqnQ7K5OtFhd3ClxerF7uEbuy6val7TxyAcaKjPNBCmk7d1SRs05NnhlZvSvj-yAyJScUwduFmNXUTxdNIZdNB7bqmblRRjMRqSsHmkU-Q9KarsIlg4GwtoTcRHW9IpwmMriMQsduzUidfJBgJFFbPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
پست های دیشب ترامپ دلقک که با هوش مصنوعی ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64952" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64951">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdjlGEAjjgeLcPv9b79H6N_xYxWu8DB20P2Tc8ByBEBhCmvZhDNSYVGgrmyk_uG_qCViwBIP2axKkmtvCLXXlunO5XFYU4_a3vWYmVym6wygrj3h4NF0kIe1An2YKHeqBh6_osxp3_skr_IeDxZqSG_mmRPKVlJTEAciEKrhwihVwh8b41yaXAeKAayUzxftTi9K10pc8fVhGCVUvGPj5lDnQhtDuxHiEMmtZr-GHJyaRqWimlgZAoze7omE2PVBlrcPvQ2ywosv0z2x0uSqX_LVrAj3290SNrpzomaF5KHgsPcYrgK1agbCLw08Y5wTnMuNqRu7L-GFyxYKG6YoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست عجیب حسین دهباشی سازنده ویدئو تبلیغاتی حسن روحانی تو انتخابات ۱۳۹۶:
حملات و ترورهای دشمن تا رهبری حسن روحانی ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64951" target="_blank">📅 10:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64950">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/A-v36wOfFkYoV_NXZg6V_-X-DB38Ak1n02xWH5CBbkL3MH9b7t3fUYyfAv2pww-woF4LmQ7njx2BX331wgYx_OZfy_rlFacj2s-uqGBpNISuyo8oCsT9z-h_NUh5B9JF0uzOfv9DvlU1yxUcUxOGEC-MonXqNcSt8p_2WtMYAwl_eGoFbm8n8wUsU8LgYGIvBKU4UidjJJBI6LKd6L_NoFhCjOdh7PYr8pIZW7n2VqfMO43PJnW9LtxX5CCOAN9O0Lm4MNLNoDWrl2j1mOTUe_FYshnfKXkK9rLTWCDednL9m0E9fG6ikY-AgIneMyYHUg7Uib_d6-ZgOmuxhlu6tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در شبکه اجتماعی که فیلتر شده
روز ارتباطاتی که قطع شده رو تبریک گفت
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64950" target="_blank">📅 21:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64949">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O83f7Y4Mcab0BOAC3YylpZf1TbBrhXu8e9MSfjEfaZGuFB1hZvfCr43YbAi7lCJwThFojC7WXrz2FAO_ZjHTgITp3AZi-1j2vbFaqvSfXaPi-4nvpIaNBFivtzuElioJMa-XKXuFrlt7g1dzbyIEYq1mpZ_Z7zcmLi1u90ickawRWpm1d_Po4p7e5EIRoQPlocqepk5b8pbnxsh16Ia0QYUq77iaI8GsweqYBWfmhKYDbVZHZVu5COF5iKURm8pfrMfvAwHbROBRVX80aRaXDR12IkcY-A_UJi88jrLDI6b7r5N2Ws905CL9FnJLUvSUnV7-uqTbh6s2uxO4a2wNVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64949" target="_blank">📅 21:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64948">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=dIfVlPMtgpgrwFO5ClVe3F6tiuGPL57hpiQVPhbDTuzNHywDASI8mw3rmzBmvZrKFVhTGq75H3jh1gQ_I-KVC_uVzEwKZy54SXlP0O8Odf_U15j03aV1c5U5ODYQ2jVz-QcL36pWRZPaa5hPPHf7EUWlkFfRJT8x6ywMEBp8LfaHdMLPzKHNGluPk4U4Rdp1z_Eg-CJvob14R1hc2rAndFqJgwRp6XWaczYCZENq2ZYp7pYsYHIWR79LiFdks8qh4L5L8mOhSQ88ke5jW34ADrmen54lZe7eE8FZmepU_UKR0K63TXdP9wVE5nq3xMXuasfLh_bsBvdu5-aSkGv1nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=dIfVlPMtgpgrwFO5ClVe3F6tiuGPL57hpiQVPhbDTuzNHywDASI8mw3rmzBmvZrKFVhTGq75H3jh1gQ_I-KVC_uVzEwKZy54SXlP0O8Odf_U15j03aV1c5U5ODYQ2jVz-QcL36pWRZPaa5hPPHf7EUWlkFfRJT8x6ywMEBp8LfaHdMLPzKHNGluPk4U4Rdp1z_Eg-CJvob14R1hc2rAndFqJgwRp6XWaczYCZENq2ZYp7pYsYHIWR79LiFdks8qh4L5L8mOhSQ88ke5jW34ADrmen54lZe7eE8FZmepU_UKR0K63TXdP9wVE5nq3xMXuasfLh_bsBvdu5-aSkGv1nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
بر اساس تحلیل من، هیچ چیزی نشان نمی‌دهد که افرادی که اکنون در قدرت هستند با قبل متفاوت باشند
آنها هنوز هم می‌خواهند جهان را ترور کنند، اسرائیل را نابود کنند و به ما حمله کنند.
هر قیمتی که لازم باشد بپردازیم، خواهیم پرداخت.
چرچیل چه گفت؟ «هر قیمتی که لازم باشد برای شکست هیتلر بپردازیم، خواهیم پرداخت.»
همین موضوع درباره ایران هم صدق می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64948" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64947">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یک سری کانفیگ فروش طی یک حرکت بی‌شرفانه برا سرور هاشون ضریب گذاشتن، یعنی شما ۱۰۰ مگابیت مصرف می‌کنید ولی حجم مصرفی ضربدر یک عدد می‌شه، حالا ۲ یا ۳ یا هر عدد دیگه‌ای  اگه این حرکت کصشرتونو جمع نکنید تک تک اسم می‌برم تا نه آبرویی بمونه نه مشتری‌ای @News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64947" target="_blank">📅 19:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64946">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تسنیم: ممباقر گذاشتیم نماینده ویژه جمهوری اسلامی تو امور چین
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64946" target="_blank">📅 12:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64945">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=IyVomOxjdSuVzJ4eisuRh9tEzwRdPdg-gxqNcn8NAa7renFjWS5iDRNuhrzqGx1vWF7MAR_28HHkDLu4A7ijeNyqPRE2ltOkRtP6SVK75TqIFWHo95SDOxfvWUK36jUcNS_d5VccIY-AEPJcshAm6Rsm5Td_cEwAEMFGX5Celll06ay2jta_trMW664Ep7zRkmTdHAZ7sytW1QzuQRfGcZDClgc7vhsPS5gGzrMMYu8VVfobWObAgpa6CNxMXupsA_FRkcfJQcXPGBmKUC96LhN5DbGLG-3c5aNb5MtzlsX5amjWv9nHaAa-k5iEZ2KzfpOS3p2JbPyI6I_eOzARdg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=IyVomOxjdSuVzJ4eisuRh9tEzwRdPdg-gxqNcn8NAa7renFjWS5iDRNuhrzqGx1vWF7MAR_28HHkDLu4A7ijeNyqPRE2ltOkRtP6SVK75TqIFWHo95SDOxfvWUK36jUcNS_d5VccIY-AEPJcshAm6Rsm5Td_cEwAEMFGX5Celll06ay2jta_trMW664Ep7zRkmTdHAZ7sytW1QzuQRfGcZDClgc7vhsPS5gGzrMMYu8VVfobWObAgpa6CNxMXupsA_FRkcfJQcXPGBmKUC96LhN5DbGLG-3c5aNb5MtzlsX5amjWv9nHaAa-k5iEZ2KzfpOS3p2JbPyI6I_eOzARdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
‏
حدادعادل: والا من خودم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/64945" target="_blank">📅 10:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64944">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jEtq_SgqQhkJNv7xXUFUIzp0R1kDgTr5lkhrMrQA_kMpE4pflNCo6TrwnxSfK1AgwWoCshtmgDtNKFivTi7ChHw3B0A6DZR7EXMq-36F2kTEPwKQU2de9K5O4Y7THB9Bcam3HzDHLDXlOlMOSlqxkQWRGyLtSDwHHQB5g2eZHcsZQcX6r6DCw68LZuQqQ4mEzX_qYeW0ElgdLsKBeRYLOqzUulsZrq4VL7k9boXnW7hUe5KvkW95e9HCdsCMnjpYRKE0a-J0sxA7TsxCC0oZjSMj-d0ANVJ8ELuu3uYdwDpPQJ3Kd8REaLZMMvA2PF1zP_lv5vKMJCc1WhvLyn8WuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیلی‌میل: کیر میخواد از نخست‌وزیری انگلیس استعفا بده
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/64944" target="_blank">📅 07:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64943">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0eV5CEAwg08K-8ZTobYYC3IoEhlfgKRx6pV7o8Gz4VCi6dvhVmUKyprh1QgJMpDTIbAqGS8QqzA_h233IqiSKI83u4r1cRe5Xcwk4NBel7ELDQlBb8jcCaF8LtSAg73GXiARSkpzJFi4aQ1xe0DvHi9zQlzHVClRfhLKHy8Jcm0WE9fllgediyBnF6oBHHIbLoVeNFJJAKQBGbfGvcPb-F2MQmDgG2vtNCFoRTFoLuHFo7IgGyT7YCEBPu0sgLnsy8z6VWmK5M3RVETtZuydtLHFQCKvdBwWWIuES25pHjbI4XqrbeA1uP37J6HA46hyk3GiHIJdPDYVp9Hn2C2dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در سوشال تروث: «این آرامشِ پیش از طوفان بود»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/64943" target="_blank">📅 00:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64942">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مثل اینکه شمال کشور زلزله‌ی نسبتاً شدیدی اومده، مراقب پس‌لرزه هاش باشید
❤️
‌
#hjAly</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64942" target="_blank">📅 20:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64940">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IPbfZH7tYqyMhBJC1exycxU9j-zmkMxn9F6m3d6cKy7UW1QCF6rOGiPbZUtO3imPsiYYYxI6lV-z9PO_1y_mjb2S7T3Ot9BsS0PWjimUkVnZ2xurlKqaacmaWJJnYyp8bDoHwTeUNkGEAnRHY-L8J5t2SRMVNDso6dcwhFERXwXanWKXcyfAsmVbpRqv2BTJIr7q2sxIEm1RetQ76Sl4tEGtnT7U1JQIbom69tp4bsXRwbWvXHwqXijZDpDJ1E5_pftDeYxtCKIVrpIy3EosAqnglfhaW5yc61kPrFRraH8FbTyG_IeOA9bD1QjO7rC77KjERMHJKEzzYpnRaf-HJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=Q2tQF2zqmq3p2bHxnzw8mOdKX1tPClAIOL61x1HMYMreQRYKMxqauwzI0C7Lx0L094jB-2YQ8iUR12zEWm4PXoVCrMwtnnNPBof_HjoaL5zo2YCONs5nTnEOKOsBoDhaUHvk1Kaq5Ctb4tXALeK4ELqjMLUJ9CSkMH4NBKG_px2mJhiqV6j2L50rSHh_-NxI0MjUhi4Dge9S1FHLvX71yTk3a1E7mPhhe3_uaFzI8Zdqkkd8t93Gq70ZQ_ihcckhKsw5WUlhjbu-kdeSNL96aFRKQEcVt2GuzCYtZcadOnWqxJ2zMQih1g30TUp8A7wI5nJQB8Nt4r_cY28utzdfLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=Q2tQF2zqmq3p2bHxnzw8mOdKX1tPClAIOL61x1HMYMreQRYKMxqauwzI0C7Lx0L094jB-2YQ8iUR12zEWm4PXoVCrMwtnnNPBof_HjoaL5zo2YCONs5nTnEOKOsBoDhaUHvk1Kaq5Ctb4tXALeK4ELqjMLUJ9CSkMH4NBKG_px2mJhiqV6j2L50rSHh_-NxI0MjUhi4Dge9S1FHLvX71yTk3a1E7mPhhe3_uaFzI8Zdqkkd8t93Gq70ZQ_ihcckhKsw5WUlhjbu-kdeSNL96aFRKQEcVt2GuzCYtZcadOnWqxJ2zMQih1g30TUp8A7wI5nJQB8Nt4r_cY28utzdfLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند طرفدار فلسطین از برج ایفل بالا رفتند و پرچم فلسطین را از طبقه اول آن آویزان کردند
شش نفر از این افراد توسط پلیس دستگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/64940" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64939">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBLKBDz_LfAzbZcanJGEHX5YgmblrpbtWUfPC6C2dRBZzZjHB4raau6uL7ofizxZyQ58mrFYd121iZ-Qbpz0kjLo2bEF6tWKVlXWBsteNN8cP9MOX--XHi8li2oY8J5IEO0k0eBojIUSv09o2zwv7Tfgam11AqDz68ZdGFtyI0i4XlH3FmKcRuY5RffSncCTbB9UxnL9DcQfZ6X_l13fxN7jzDBHMySA6bwODJNTpnUvjy79exp399yPDZGwrfvu_3UexJ7kpLQI9a7xBFYOQ6bUwdwr2zFI9vB0Pchlga_DWipPwn-WUzpbZA0QyUvTsYJXDwf0nS7_p23ddnS8aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست ترامپ در تروث‌سوشال:
بازی نداریم! تماشا کن قراره بعدش تو موضع مورد علاقت چه اتفاقی رخ میده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64939" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64938">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVojg4fPWU4kc-RDm1OACLhyfJsIcewYIVXnUorG1W04wzsfmklOVPoxHuePrbR1oSfyuI4p1stueL28oxRkgtw_orw7BswbkpuOJ-d0xqxv7n_Uu0hJuq6_szRS98Kyc7ac8fALf9IO2501SRtNROXqLmV7dv7AOKJ5XUO6kuWRy3TdFrM68nSiVPBBgpyVhPuyv_mtY4KMxFNj2FsL2dZAyPbdNOEgqC5DaHFzp9xjQc_kgifjnAC54aJGj7D897BTNh_wBZ-jLQurxdrfXw1VhLmHre3dfYi5qQk0Kh76lMIG4Gjv-f_ZWKkQRvA2H2cq671xcC4g68qq0mPXUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W2CfhREndYBzqHiIXQvGneRg88-nLg4yXD6UMX1ewsAtszY8JVU4GAVd7ihVky_dnqF_gWzJg48cF2Sm3Wc5ka1W99rbtcFHRjLHKAMCGNi-nQgwjI9-w8GySfxMrYHr42WE6scDnGETwVs2-ZTnq36ChZp2_ymVUZRhvDio5zSG9KwpZxunccZD-irFqjamxeD0YTUBHSxdLZxtH1VUVKYgODFPZoHlSlidiwTrkA303ah1jOnuqw58bcbJ1RWFvX2ZTzKGUHrYLDf6p2lpcW-Gg4sdSkEv9aAbBOZEHnvpJu5o76qWHIpP-Qg5Momts0NjhhgXj98xqNfqugXITA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیکتاتور‌ها مثل هم رفتار می‌کنند
دیکتاتور ها مثل هم سقوط می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/64936" target="_blank">📅 10:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64935">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل گزارش داد که در اسرائیل برآورد می‌شود دونالد ترامپ در ۲۴ ساعت آینده درباره اقدام نظامی علیه جمهوری اسلامی تصمیم بگیرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64935" target="_blank">📅 10:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64934">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عه امروز واقعاً روز پسره؟ روزمون مبارک
🕺
#hjAly
‌</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64934" target="_blank">📅 10:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64933">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nl0I1k0T5IG16P08CBqJ8472CRxrdxU45lP3l3vI9B81EXqH4pbgwIb8LWTvD4_1P__8TVRz4t6OxlUXcUqsRuIheqTUhNoLB6aLK5O7ufPr-VMwS4Q32UpNGLvNiJFn1VOb1yvKXozWVc_McqgcNHKWnqrY2IhhCeLjh7WjIrV2a00aRQ6HUymU7kZD-WJwY4XgLC0LUVJXAYBMTZWkiW_MdR43SDtNt71-C2FvXsZw4PGO5G0M0KQbPOzjacREgv86xnfmaKdKXK1JoOZOZtLr5lW_fprBlsIPQPffkp7bJnOo4UKtP-80IlbeDQcSOrJ8ttSeLRLbGNRk670BsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزالدین حداد، رئیس شاخه نظامی حماس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/64933" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64932">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=J0bEqfZuYXCEU5jop1bDoEAtaNDJKCDhxlCp1BudqCyKoWjcAMHNK-dACd3xYN5UM6Jlfx_sjuE-oQLt-2tHF6a3A7XWgTWCEiAmo5cj6IXhi5yv90rrGJMhrbr8Wf4jPZZbuJOZeN7XjnK-nenyyVIRQFPNGjg2Abf-RV3w_1S6h4-fr8EXhMhDOcX6YCBLq93wvpI5v6DQW3bXH1K0nSbvY6-XMLBhatzUVJX84kEh0b8-s4hn6hxLUNmNDb2-52VLEuJS2qexUOuWbWjMP91l8NnXUNRieBXeFkq0y45egSBP73meI0vOEOhVY0HhtUMbNseQLZmtQEhFlwYoWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=J0bEqfZuYXCEU5jop1bDoEAtaNDJKCDhxlCp1BudqCyKoWjcAMHNK-dACd3xYN5UM6Jlfx_sjuE-oQLt-2tHF6a3A7XWgTWCEiAmo5cj6IXhi5yv90rrGJMhrbr8Wf4jPZZbuJOZeN7XjnK-nenyyVIRQFPNGjg2Abf-RV3w_1S6h4-fr8EXhMhDOcX6YCBLq93wvpI5v6DQW3bXH1K0nSbvY6-XMLBhatzUVJX84kEh0b8-s4hn6hxLUNmNDb2-52VLEuJS2qexUOuWbWjMP91l8NnXUNRieBXeFkq0y45egSBP73meI0vOEOhVY0HhtUMbNseQLZmtQEhFlwYoWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
📱
👑
آی‌پی های جدید برای فیلترشکن شیر و خورشید
🛜
‌ ‌ ‌ همراه اول
2.22.250.149
23.58.193.140</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64931" target="_blank">📅 19:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64929">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">همه‌ی اعضاء هیأت آمریکایی قبل از اینکه سوار «ایر فورس وان» بشن و پکن رو ترک کنن، هر چی که از میزبان‌های چینی گرفته بودن [هدیه و یادگاری]، همش رو همون‌جا انداختن تو سطل زباله.
دلیل این کار احتمال جاسوسی بوده
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/64929" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64928">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrcTwl39BhFGFEsQUcUL0AVH08OZf65EHnMdaRt7k-ksmGNcQhAr4LK0N7k8VB7FmAbMkzoXacIRYL3U_8oBlK_GYRXTECc1FtTqXpHIBTL9ixh-S0_N3baTUIHpVDPKTDe9UZolkD2UEyX4AtWG0RZ0KazZKX-rVgE-VX0wCnU7Vq1c5PTlkm4rXbAM_8umGD4OgpCE80HYpqAeULmXm_QfsBrBsx8RxMf0iriZLvvV07jPkWu6LWgsznV48hRcKCcS2rzWvDhOdVRw46viKl9ck1g_dDSR_-9Ou7lb1vH1iL1eLAGND7PzQaVbB6WLteI5OMVBHATOsREnfl3Hvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/64928" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64927">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: تعلیق ۲۰ ساله‌ی غنی‌سازی باید یک تعهد واقعی باشد  @News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64927" target="_blank">📅 14:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64926">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم  @News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64926" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64925">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم
؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64925" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64924">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تنها هدف حاکمیت فعلی، رسیدن به اولین شرط هست و بقیه شرط بیشتر نمایشی هستند برای بستن دهان طرفداران، چون به خوبی ‌می‌دونند که ترامپ، اوباما نیست و تا زمان انجام توافق، قرار نیست تحریمی لغو شه یا اموال بلوک شده آزاد شه!  منتها ترامپ به خوبی برنامه‌ی جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64924" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64923">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
ایران از چند روز پیش منتظر پاسخ آمریکا به این پیشنهاد پنج‌بندی بوده، طراحان این پنج‌بند فرماندهان سپاه از جمله جعفر عزیزی با مدیریت احمد وحیدی و تایید مجتبی خامنه‌ای بودند، طبق گزارش خبرنگار ارشد الجزیره، تمامی این پنج بند توسط آمریکا رد شده!  جزئیات پیشنهاد…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64923" target="_blank">📅 13:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64921">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQHEas87saHHhh4LMlwYwNmGyf8sZ9Du0Ea-4STCIsuwyT10vkg98R98GMRuIJlAFo-Zdh4a7rKI_6Rf7clj_YhsvSc-raTUV97IcKEaRjOKs2G-9ljcCQAwhMr5MEvcwjbXveLAFdNrwMc5o1CHFEh2Nf1gDEdUZ7co2WMCm0s_AtolhMAg7evMwnYk_JcXstvpGom-Oyev8TpB7Is7A5AfoViynQbABGToX4z-ZtoJftbHoYclsZMwoZvEPlJUSdBOf6QgnMxwpvS3d1vHgxHS3NU1N4yjLAzzSJhVOSSOAFM0ljKiQH25-RFK87N1-P-IPf4w3WkH3ZLs4Z19Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RzjQ0Trhh3eQSiCp36qt356a0P0aDcTPsKZf0Cyt2d_qMmWwJpHbCT4cFfpq_g6cb0-szbWVOgBB-E7AIBEeufkfPoudJ4LJg0eaEdDv7L-Uqo76R87ZMNIk5Bnj7AWSIKAABzfcsvUbUgP2ZTb-bvw7ja1oQHW3E37klNHPaikKcBmsj8fL3RZOBCP--yNJIqghq06rVY2As_Xq4n-2vm1YxV8vAEZWz6lI25WLRhv3n0q76V5puzSimPC1s50jXZ21FOkU07-rgS_f-Fy3jlD0ApEDJ8Rxdywu-K-gu8CPWLwdBFTysT7io4EbEB_A1OQCk67mSAHp2gtJ_vPALg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ الجزیره: پنج بند ایرانی ها توسط ترامپ بطور کامل رد شده‌اند، مجتبی خامنه‌ای دستور داده بود در صورت رد این پنج بند، دیگر وارد مذاکرات نشوند  @News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64921" target="_blank">📅 13:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64920">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LD2_vyaUMRSAXhrYUF2IKU6Rc7sLudF7XFAx4Y-bfmb5DTzRVtz3sc06vJ4GWefpR95zkIdOCz0bgmAC-NuDl86s9V9-5HnOkVGlB8LkCdpIA1SZVa5ft6Zi_bRWYdtDtTtKozTgsMr8Vz7QMIpjbEzjrGOMJpZr0IRoUJBP8UGqs9Ulz6H9lvmDB3UDK4-nPDovJBXrMFcL3ddPawtQT498HKwIaSXCcLQAP-321m5aETNU9KszGxbRhH118PaSUSee_T-eQ3hBXr5s5tD3AEhF4jDphFc0nTcyucXfXucWhWk06ZZRv6dB9UCAbftUk3E-SWiZh9JQEkblE7BS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#فوری؛ علی‌هاشم خبرنگار ارشد الجزیره: یک منبع آگاه ایرانی به من گفت که تهران رسماً پاسخ آمریکا به پیشنهاد ایران را دریافت کرده است و واشنگتن شرایط ایران را به طور کامل رد کرده است  تیم مذاکره‌کننده ایران پنج شرط را که باید قبل از ورود به مذاکرات در مورد…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64920" target="_blank">📅 13:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64919">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇺🇸
ترامپ:  امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند. می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت. هر کاری…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/64919" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64918">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🇮🇷
عراقچی: پیام‌های متناقض آمریکایی‌ها مهم‌ترین مشکل است، هیچ راه‌حل نظامی‌ای وجود ندارد و فکر می‌کنم ایالات متحده باید این واقعیت را درک کند. آن‌ها دست‌کم دو بار ما را آزموده‌اند و اکنون به این نتیجه رسیده‌اند که راه‌حل نظامی وجود ندارد!
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64918" target="_blank">📅 12:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64917">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1BcESwkgxxntjV5ehdzmpCsabVlqS8gfVv9LyqQsQGgwpNevLpwJVz9NTYvjH0Lb6PKjryW8vL_7T7z1KqXSfy2CjTqwxT82QL-V3-IlxUu7MqixQRZWw0JDiO0C6v4IpjQe3kWRJ8vFK8tnbBxBqbFts7RwiHPaNL_lYKJ4yEDG0A5XXv9RN8oR38e0yaukJ2Wre67IlcLM4_mgpiH6nocDgCJ2sqsW0Ma2mNtLbgqHvf1mAIvTOmC0a-T9vUHcYdKeGChPxWa9VqcW9-WyPkbm1V3iW4npp24TcXOdionoa-vYzuBX4A8KfHoOk-V3Hk7i1HQ7RhaDidDbWDa1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=DrROHvdQ6UrFCOgv5akvlNcRNRd9WVqwuBUP3qFxmbOSiFMdlmE0DWPOWWiwc28bx9sYSw4YjykybasM3vEn8SigiIgA_65vww-s1vZJNmhM0c6t0PFDDWoImyAGwR45wXu3Qstf6fUvhgGYWvyKYyoSncnps1qAdQXADwaxE7EgxKQqX2YnhR0WH-5dWA-xvHmIJ2-4erqBCrlEhzmxZ0BLaa1czEenjQGSs5M1xpOeZcp-hnoyjhexcJGFebsUpNLSwY6U8g4T73_5BEGOgGHUmxeu_A6PmR6hipP3NIvXzqkkn9DLOZ-LvPMCRXoZZCEkULO9CWd7CGVhu9ejoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=DrROHvdQ6UrFCOgv5akvlNcRNRd9WVqwuBUP3qFxmbOSiFMdlmE0DWPOWWiwc28bx9sYSw4YjykybasM3vEn8SigiIgA_65vww-s1vZJNmhM0c6t0PFDDWoImyAGwR45wXu3Qstf6fUvhgGYWvyKYyoSncnps1qAdQXADwaxE7EgxKQqX2YnhR0WH-5dWA-xvHmIJ2-4erqBCrlEhzmxZ0BLaa1czEenjQGSs5M1xpOeZcp-hnoyjhexcJGFebsUpNLSwY6U8g4T73_5BEGOgGHUmxeu_A6PmR6hipP3NIvXzqkkn9DLOZ-LvPMCRXoZZCEkULO9CWd7CGVhu9ejoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند.
می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت.
هر کاری که در چهار هفته گذشته انجام داده‌اند، در یک روز از بین خواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64915" target="_blank">📅 10:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64914">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
📰
کان نیوز:اسرائیل معتقد است که ترامپ پس از بازگشت از سفر چین برای از سرگیری عملیات نظامی علیه ایران تصمیم خواهد گرفت.  مقامات ارشد ارتش اسرائیل و فرماندهی مرکزی آمریکا (CENTCOM) در هفته گذشته درباره احتمال از سرگیری عملیات علیه ایران گفتگو کرده‌اند. بحث‌ها…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64914" target="_blank">📅 10:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64913">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/p3sxZ3VLZEHUJYiPNAZaYFM3gHbHWQNjbcQGzYobU34P1_brO12RbcvRPTH31GPgZf9X66LQBrCQmmlMAFnJZD7MYBwL29Ej5EdBMnW99tEwTz9lBA37CAyoJK0PULfhR0EHg13n8RIfuAsVtymKyab7Dmg0npFijLdVPw86m_eoSglE7TqUb4cpVLRtwUS4r_DL3yesXlyijG7UR37HBEjALsLCpZ78_9Ala0fT7ueXfpyAZXlnuK4ciFRkXrSi89UOIxGrcjWAPZL-qxCMnmPtKtVQwGuktuTHOfUBnnmPfxhjjE2H0A2uPSWLXVyAFaXjhC3WMBlGt73-Tnk_hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/news_hut/64913" target="_blank">📅 03:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64912">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3CkkhHzdd31bg9JEu9jVTQdFaiHonLa-PUmo-y08XSnqhjzKR3qk8tKWpxKXhxwCrXiLcBdutQWY_OEc1kgzCqIYRRtFUZoZUK2oSzMTq5cth035KnXp-TZU9z_eTqbJESvnzwtIWOu3OzRuYrOks14UbbmXMk9oyRqTrjVUwGsl3vt6guoal0F376uZO8QCLJeaQ5ORZeZ75ZVCLREvFeltO4BsiJkirWjVllgBdpM8HeGmBNFXeAGN-RJ3IebWZEltcL5RGcFNUl8Flz0BLY4ehCco-iW_zYP6p9-Tj3PlYHwsu2_YFPEg9SPlt5mqYKfNGSa8OhQgtf5rSjX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی؛ نماینده‌ی مجلس:
دولت قصد داره میزان سهمیه ماهانه بنزین ۱۵۰۰ تومنی و ۳۰۰۰ تومنی رو کاهش بده و قیمت بنزین ۵۰۰۰ تومنی رو هم به ۲۰۰۰۰ تومن برسونه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64912" target="_blank">📅 19:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64911">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=Zyx36SCt0vH8FbGAh7tas9VxVnoPnsJcBUvNRJOcshqqv2fvHSiyJLM2CFT9WOqafKeVvX9gOUBtesaGnAQnBSeDRRJlnXdC-Y_KlspLI3X_EKnJ7JZa2MghPXYrGrRrRI6gv_1kEKpX5PL5ILhVFxy8WK6cHeGxmcX6mU-rPxWedjhlyhFfCr-G-YBPVMIxStm34B9GwkSJu4rtVx9riMoHlNZUDiUHAISYM1BnJu3qs1MIoF0oQfWThdzIjjstNDViTISqmicevmwpd2agdHPdx0i1BnUDvZdmKUjyI5Fuk228Hkm__KeUKUW2M6Gh4Ke26Bev6sGkRhQMx_oUCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=Zyx36SCt0vH8FbGAh7tas9VxVnoPnsJcBUvNRJOcshqqv2fvHSiyJLM2CFT9WOqafKeVvX9gOUBtesaGnAQnBSeDRRJlnXdC-Y_KlspLI3X_EKnJ7JZa2MghPXYrGrRrRI6gv_1kEKpX5PL5ILhVFxy8WK6cHeGxmcX6mU-rPxWedjhlyhFfCr-G-YBPVMIxStm34B9GwkSJu4rtVx9riMoHlNZUDiUHAISYM1BnJu3qs1MIoF0oQfWThdzIjjstNDViTISqmicevmwpd2agdHPdx0i1BnUDvZdmKUjyI5Fuk228Hkm__KeUKUW2M6Gh4Ke26Bev6sGkRhQMx_oUCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ی دست دادن ترامپ و شی
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64911" target="_blank">📅 13:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64910">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQz1GNdYKvYEqw9GPYwfRpTRHizJZaQN1apH3fjQgbiTkL-9RSyCmZ2MFKsKKo76O6snHwP37OoCvJDFx9_m78CmGAcNNyn2TYI9NYvwKBeMVN1LeS41n1lhdByD02UTPnmF6CmPD6sO6AVXerVBF1F_OFqMoTA6qiO8EVyfGAnjIdIwO28xcblBD1vE4190Fh0QTjZGWJc8ML-aSoVz7dH7tVk9JbKRv6Kssnn1YrERJlAD59IA0U6yUOQ2Hu-KKwg0c2nQyQM6UqJFLHsG2z2MV5JdrvWybtyZVtHY7EE6KLN7vOt4TQbX4lNz5o6RAYCFFBgyRj9inp_au11hqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64910" target="_blank">📅 02:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64909">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64909" target="_blank">📅 02:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64908">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MRSV6GEuBiVhwJG5m0HeTXSxfUWnqXbY20qmYI_VhG0YpuhNwYikxre_10xsj0h9-X2kOu9Tn1TtOPeTnwytxvyP5MD1AdX1ZIWDqfFz8BA03JoJCYiTha7m0C4BwXyHz2v88tGE8u-5_9OCTkD9TLJwXYWuWJdXTICOnFcplcQFfjddEm2Q7zL59Z2uIbsSrBHvMbDNi-aWzDmDJZS6aDsB_bmxvLhK9JTZKAp9S2R010JIWeE_xcG332mPkxQdfCRGRkXJK8H5TCrGzv6JBmxMI2RCNfnEQnszshwJaGFLYxMMSuAPmptRiW502NtymT3vw8XFJtsx8YiuKgwBow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SwyJ9ReNAnzF3sIK3dh9iTRRyQEoGRz7GLfVUSV8xd5uV-pSdGiByRu3ult2azJLN-098s2Vi_mjCCoAsK3kdqgkV7Z8_4t8wj_x4F53SuJ9fV7ZtAUHgK8FZLA8kqoYdO73XxD0TmvuuOPfTRt1jAOa7P5hPhijOQGQk1q-YbpJN_kfO0-AZe_WloV9lmXCITA7OBGuXZbJ0qUXlT-0oNe3kl4yPKgubIlxy_7JYQBpHGfsqmdkS9knJurcmrGUXok7_wW8oL-DdBKMktgK40erecE2un8JfQmCBfvHQmc1FP38ssv3ejU4BConOFiSdoci27rOAjcOFT2qNyh5jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=igkc6KcVbk6B2VruEAQR_RnkVG7N6cToQaEE0Swaa7gOypKsQFW0k9ziwPpqQ0Jb_oT2WPUIVS2g4KbS7gxiJI1jgPzra2firvAaPG5jD8s2JKDTl9n3DyofTLWSuSlVcQ0nI1JxFgUYaIfi9x5YPDmFpZUrhgVCxGBd1Q3l4psUg24fwevksuRyFzzSS6e1-b5OqkG-lQE0fQumcNOaaBpYp8YTCov5LRmOxCM2q4DDypYq0Z6KWm2_RBTIOYXkgmZnGY_njD1IppLE4LUIZ5_aZKzUx651DT6lmd9ibPDad91r9GkjbZ9b2atl01QGthud9sTREFKgjQb-_n6cww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=igkc6KcVbk6B2VruEAQR_RnkVG7N6cToQaEE0Swaa7gOypKsQFW0k9ziwPpqQ0Jb_oT2WPUIVS2g4KbS7gxiJI1jgPzra2firvAaPG5jD8s2JKDTl9n3DyofTLWSuSlVcQ0nI1JxFgUYaIfi9x5YPDmFpZUrhgVCxGBd1Q3l4psUg24fwevksuRyFzzSS6e1-b5OqkG-lQE0fQumcNOaaBpYp8YTCov5LRmOxCM2q4DDypYq0Z6KWm2_RBTIOYXkgmZnGY_njD1IppLE4LUIZ5_aZKzUx651DT6lmd9ibPDad91r9GkjbZ9b2atl01QGthud9sTREFKgjQb-_n6cww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم تو خیابو‌نا و پارک‌های اطراف پردیس بعد از زلزله و پس‌لرزه‌های دیشب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dl9rzZMQmr0H0hFRTLlezNsGLtQDtP4Opxv4ntjMsgBwBOsKYvPd-t4G3zUCHBa0XORR10elrTMKg2JeFEn73yjLBJT__ZhKxmJqncmg7FbEx_cIk6c9rwDMNp-yi-AwFFvZWeV4XPJsztB5_2VbR0lyuDp68CKcIcwVabe-H62aHj4_kt8uCoQysR3V9T_Q9Tyk6MzV4QH-SRiAg8ATF7t0jWU8PTHtbiYKvy6drzIzdogeA0hugnbzORePQI1wrrqXdWDK-H92E8pxoEC_StNortnR3ifCK7n2V1vL9S9mTWmrA7-okK5CB7FaTfXvTCxsHzeM3MijZ3q4skKYLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b4jixrucnrhF_zis8dgBbUAuzxZK-ipdishMvrGKTxTqbsz2WzqqKoR8kVrL4lOlSAD44kWjPDmCd8Hpv0xv9WT9LgpiwO72h6hoj5J-doXg6_CYSRmDIRuCKRVS-yaP8h9eIw5CMQbq_b3Hko-VUU5K4DKZfex3tQiO_jzCGjw2bJ10rxT8qHQkHqlOn31oWacstaPeVz0jCiqjdenn31NqGPMWgJMQyZvDTLxTjs9vjespcNWl2z_qXdECnoWQa6l1mAfjPl1WcH7UTKiSSU3z4VlrGCEBxVzfcCLfq_4Rk7Dev4kITmHRbq3yg_U-6iDgoZysz5BsvO4VNlFNcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64899">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W69uZ4ylRcZ9v-q02q-_x4LyttX_Kbz1KpnkOOjVYgjC-ilHodemM_OxjwfraGsw-fEDMGiM6EsByFBSjas_Dv_Ub4ySkBURKf11FcHxcwBH6WF_Yu14CnxbgwakhuBP4vu87hx1DcovNKBL8JaGFgu3K_o_Mo3O2N8JsN4iCu-g7-UvXnX4id3udDQCT-H1EKXAuOZMPX6VllsY24pf02tCGv4rq5jLWHfGHxdVlhiAv9bKO03f5S2xKQsfp-OLwkSsjlNDte403NLyio1fPNq5EDgKqp8UFtHao7LJXibxIFaXI5yV721fqbWWMBTOUc4VyRKpdlJfL36FMrt5EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yugqmxue2TcCGXPDRqGzuCI-eNBAY6w7H-lir8LZIDYa3Ki9R7Tls4gNHMDl9F_CJwZFJ38CgkX5wGxYKigfcBfNKaaF7e6kxicfyrf3qAikwiTaLcHDoOu3YX_bdcEjS6_xMtWyg_yeY2cGRfmReN5sQXA4IcO7cg1ME1lHgCDCD9KP89EOExoqjJNifOobtnK0md0iRhA_QtPkKGITSx_Kmy2GIpb0nFFyXEZjmCvychK2juVgAjo_bOETBtJoMbhu4J83G9ML-Sq1q57RAHY_Oriqd_Ma2LvkJbYvEOmt6VieyOoY940HeXoY28rwt-E9G_hv9D6H_rzROvTb6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکوروبیو داخل «ایر فورس وان» دقیقا لباسی رو پوشیده که مادورو پوشیده بود
هنوز نرسیده ترول رو شروع کردن :)
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WybeSvAHzWFIiINp3LPA_88HjCzAH9A8xklTbcYlW6G4yDXWjOlUYn6i8p0-24EI4su4CPh6rj_M5I9hzt6J4jG92qQS5s3iX9WZjzOm9iIJE0-WeKixiGBOLUhE4JwLEB7jr-FkN8a-WVAelUqFI0qRNXRuRaJR5bp7KBM43vpHFToxJdqPSP7o_nhQJlv9pkuWHALIEBPpqyjoqrVlRZu4h81lN_vDttJI7v7n1n7e-0MKpIxdLiar1rwu2GmhsNgoV4ct9Cki88yYAJMbaCzUeS8OYV7cuNtA4JPgdCuwDW6nOfs9vs1tWdlMGfCLxO7nero74ZtaJd9zG16yCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k3OvyfxZOzhEEOKENiosKfjYTydcIOmT4kOB24-aErNPbDk4eCdq_o0YyaFbX39N5AN8vP0R6U99qyfqTGsQK1996qlXP235GBECtS7mRQ3eG9QjOVoosC-YliOLIL2gXf5E4OBSFt4_Hi5NdfFr176ByBmq47763r1pqMUkRNKOQu-LE_ulObWTb9L_u08WO43giiNaA5r972t_hwpLIQw3dEn7UWEz12IzczrY6pubab_8toverdUMtOLb6b7pktQZohgAi3xH4YhD50-LqrfNMtp2i4OZ2enAoZK_25m9OTOX7Xtg3mbzyy0qbbMR3enaZeVKVE16wTkljBkSdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=pYVbSgtlgkOLGZzUKe8FaZRrxOOZ7ZouQF7qE3MjVAJm1JLInLBSmb9R1Sq_u4iHqCyD2Ob6DG59k3ZhsEktVYvwl23ywlU9nPhtdQUrhFYlZNoyTpN6eW8wkWaRp39EOZybQANQd6avFdkTL3QBPQoKvy32BfbxD8FasBBj6z8tSyXYhlTY4yQR7Gfyz5K2Zcp1algP4RwOjJFPXAf23CBe2pm5eSbfgsHMTHBuQQa2Q2d1z1By2ykPcLlHsGnorPIesXqhfAEJc2HGgiVmauXO411rn9ib30rP0wSYMiyB3iDOKNzLHxNEZrygx1aFM_vZr8-CRHlRV6_epTy8PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=pYVbSgtlgkOLGZzUKe8FaZRrxOOZ7ZouQF7qE3MjVAJm1JLInLBSmb9R1Sq_u4iHqCyD2Ob6DG59k3ZhsEktVYvwl23ywlU9nPhtdQUrhFYlZNoyTpN6eW8wkWaRp39EOZybQANQd6avFdkTL3QBPQoKvy32BfbxD8FasBBj6z8tSyXYhlTY4yQR7Gfyz5K2Zcp1algP4RwOjJFPXAf23CBe2pm5eSbfgsHMTHBuQQa2Q2d1z1By2ykPcLlHsGnorPIesXqhfAEJc2HGgiVmauXO411rn9ib30rP0wSYMiyB3iDOKNzLHxNEZrygx1aFM_vZr8-CRHlRV6_epTy8PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پیت هگست درباره ایران:
ما در صورت لزوم  برنامه ای برای تشدید درگیری داریم. ما برنامه ای داریم که در صورت لزوم به عقب برگردیم.
مطمئناً در این شرایط، با توجه به سنگینی مأموریتی که پرزیدنت ترامپ برای اطمینان از اینکه ایران هرگز بمب هسته‌ای نخواهد داشت، گام بعدی رو فاش نمی‌کنیم.
ما داریم یه ارتش رو دوباره می‌سازیم که مردم آمریکا بهش افتخار کنن
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/64895" target="_blank">📅 19:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64893">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y07h4iGJqxc9pheBgEGV5HON44M1pHePxpZh_uSckADGgzDcEuLMr3wxUOhkw3AL3NkXjpp9ieryV9rgnP3FwvA1ojdoccvUe3gkpUG2fOZAvjjX7g_FmXKVmWR67VsWECu89x8WpPiLwuPbD73MdncBCiFIBxtf3ZGzrsVmwfz_1X26WXMPUFqLQEmb9nSLwQvtVnDnC5QWKlMpwWrclj-4pnXnbf-30dUAc-qYNXSRHCcXGFdgYOR2DXpRHD79k0qaRkY_MQh-K3PmV3l2MWsCaw2fNGh2mlKAfQMMUG4tss3MAPl5uGVQJR4KOi8cWA2fhrGd6c_QX0mo17MEpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E71GG_GifPotl_jW8jDMzh3LY4cnSDjlIs6fELR1fKKD3HbBjahtJYEmeFtzG6Ma116RgrkuUtKbdr7LRzlOxOsl05LxvKUEOPwondCrc7rJu1MWQwevTB9Hus0emk1E5YrVbCHrU6GqhI-H2Y2W_91qM2lYwPhuckbL8dMZxDuQj06M_IpJrOI856v0m7ICU6cMFqzfqD7Ihl2FawzaxcFU6PNa_YH_fNiud6B--vqFtyxRJmEv0JuhwI7-UMoindgogMf5gKoLartb7PUNS61f1hZFXll9r03XKVsZ62DswnEb0Qj-D5hSUWOws3IQIEUkf0WAx9eRiPpR2BbTiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXw5Vbejd7sX26Qjgq0ZFdRToUZwbUXo0Wcs4QNExdr5a90sNNfIRzlJbkHuPZy00DSvcxhOfDNPT3nFI2zvJs3V2w9kYF1b_-JBXpqRv_iHeuAFNHeqARw9vYNNtNomLylmRYBdn-BesaU2VWZltCMKjkxzwsKIouvjLCjLYIl83n3mbNhSFLK6us74tsiNQ-4k2Ug9zkriWOuVfFIhxTH9Gx26X31Y7CG52ODMoHsVMbvYiUhRZ5ZW5HIZgQVgnCiEBIw4-lCg7_Tb4k0Lhzbt4gT1XRGoATMGw1Fp3y3ISh4aB5yBks74TtAJY8-zvMxoMgV7EVNDqNPGNG6CEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64891">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=V3ielI3NUr5xuKkQZoeN4TcmJi0SuvLZtld1C0dVNziK7Ht_T9oE0PFUdxLqcID573PzF9tBnA-sanfFTpUgkm55DLHUBA-KKPFDxEzoPs3baPepxxzqjKCQQq83sU_CW5ylGNXEKYW1oZ3XHhrNpmsNZj4QJFu359pSyD0TA6NOAP6roAaNE_TH59XJJJehdunnM_pqEY0GvMK7f9JgYzaOHfsBifBJY4qXbog1CI7AboQyTooei8KNyZ0MUpnkkgfSniu4ES7On1vqx_0H_QMwHUWp9zE56nvj0xey3Bm_Q-VxXyNBHSCEMKAO4hEykh2xIPSiB5ulFhEOMHQJuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=V3ielI3NUr5xuKkQZoeN4TcmJi0SuvLZtld1C0dVNziK7Ht_T9oE0PFUdxLqcID573PzF9tBnA-sanfFTpUgkm55DLHUBA-KKPFDxEzoPs3baPepxxzqjKCQQq83sU_CW5ylGNXEKYW1oZ3XHhrNpmsNZj4QJFu359pSyD0TA6NOAP6roAaNE_TH59XJJJehdunnM_pqEY0GvMK7f9JgYzaOHfsBifBJY4qXbog1CI7AboQyTooei8KNyZ0MUpnkkgfSniu4ES7On1vqx_0H_QMwHUWp9zE56nvj0xey3Bm_Q-VxXyNBHSCEMKAO4hEykh2xIPSiB5ulFhEOMHQJuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ملانیا بهم  گفته باید رفتارت رو درست کنی تو دیگه رئیس جمهوری پس از کلمات رکیک و فوش استفاده نکن. من هم همین کار رو می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64890">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=WlDngnaTcxancDLdHCVkTXEZaJdSn0q_b9v9F7G8y0RZJnYsG1Zwd05ssNgK-lZ2WLqCSC32VqMGQbHHm6ejR6xUOy-OVUMZ_Ocng5LtLHERQ157ncbm3iKi7EF92gbnLruQi3iEgtPbfCUxTzaXYtoGEfEsGYQJ43wdR3Kvoxyxbv-e2mV93YJFjF98Ed1vqCXxnYnmGLDWXnvP_T7LKyyfxM_rXjS-AolRBqPe2rnc7VccB5pm6YPLx0S30UWhvHwlF_aq6pkj86FZMKxJto62E-8YL-JWlacO_xTKAQMG8mUCQvZQkGxZBS7TF44renvGqh4ejpH1vhtAvpzqFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=WlDngnaTcxancDLdHCVkTXEZaJdSn0q_b9v9F7G8y0RZJnYsG1Zwd05ssNgK-lZ2WLqCSC32VqMGQbHHm6ejR6xUOy-OVUMZ_Ocng5LtLHERQ157ncbm3iKi7EF92gbnLruQi3iEgtPbfCUxTzaXYtoGEfEsGYQJ43wdR3Kvoxyxbv-e2mV93YJFjF98Ed1vqCXxnYnmGLDWXnvP_T7LKyyfxM_rXjS-AolRBqPe2rnc7VccB5pm6YPLx0S30UWhvHwlF_aq6pkj86FZMKxJto62E-8YL-JWlacO_xTKAQMG8mUCQvZQkGxZBS7TF44renvGqh4ejpH1vhtAvpzqFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره نماینده حزب جمهوری خواهان تو انتخابات ریاست جمهوری آینده امریکا:
کیا جی‌دی ونس رو دوست دارن؟ کیا مارکو روبیو رو؟
به نظر ترکیب خوبی میان، من معتقدم که این یه تیم رویاییه. فکر می‌کنم کاندیدای ریاست جمهوری و کاندیدای معاونت ریاست جمهوری آینده باشند
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOUnU6VNJOzgAKbI9axDSx__-ve34ApoLsjY8KbDzJwh7jEFYEXL0Hxhj7y0gR6ZpDymY07gF2u5XtmIjggFLuaAcFPbxUfxraMwnez5QbHQJ6IvGu6yLORnTFWB3Tgpz1h1PZsUf_byv1B0O2ZmjuPG8cA1xdM7oR5RON9aGS2eyzpEgPd8-Te6PGMj7GnM8OAs5dd5z3mnWeJD-mHKL531FC5Go2nMC40mty5WZONE8mTXgetkTL9YWZSSVAPQvpc95R2gnhjiQgbYJBhXSv_P96BO-nv_gAIkGBkVKDfJRGxbUI3i_fJImxLuO4bhf3AAsFCHGowbe-xSv3gBEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qfED9NxrwommtqAP6aGEN3C3J9adWmSvrONNeWJAfS6zvtMi02qQnvEKC4C2aVN5bn3kyaV7KWTbKkA_kTo-I_2uQULJ1UjQqD6Tmd-r0XxdoBcNNYW-yBKXGxmzKoHpE3TTd5vaPJDu6-FcW_8Wxv1oCNv_BY3OC1jld2S7scrk91mlQETpLtilfxS2qusvuPFNtb4Do8PO4T_yv85heOR8Ii98arWroG22SFWhe2tg5NOGNuKCenp7yMraClwPkvOjtWmAAP1CYi49ptuEiaHnI2dFlSoGgEGvJXKxqgItUam0Lm5G5_M_uLtKQRqRKfmfNimqX8KeIJquHwnBCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64882">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APZnHYsZ_Ix-1E43r1opCPF66EXz56OQrhbEh44hP_cDpH_vpp57CxdHYYlTPw48xFQIAh0WVtzBeDCFoHdQvOK6OBl_7-mlc9Eb-FlgxHrooRRsvtN8iU-43RQkGS8-2yF3WGQg4s6xIG52bndzsYlUsYYlFe2hcD6HRV95l2ygLY5QGB6ccc-0Ik63G45ye2uJ2e8xbkcq32cDNGDEUHadJju-3I14VbEh_2JrWRAUIucNx-I8bW9alaR4GohHOb2vRCuuztLcx-oFhMvJVb5KRBFCMIOjeLl3-ad6bfbleEvRIA9b9_6cIZ7bBkTGsaagEh4Jd1yrTR8bW6ZdAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkHSLdEJHplCwIRAOQ6TjuxKJps07dwfpJr_bPJYF-0t_30z-SHXgCb8aA76Uuxe3cPLukO2UomX06AbcGnUcgaYOAatfvC7eJQUW2k8P4exBRLlpBKrGGgfyqhq4USF2iA3ED86_BNQIE88WhkQZtDPRTE9cxEV2e4w8V-vvnJGdkIhaJfFXTcDptUlmIbzABD8dTvw94xZVxeeiiUNsivpS61s0e1VfkmPmYEN4VvrxJ5Ts6mn3r651ESF1VFbJXc4e-nfFtYu6LpK6SiqVyoqjJAXhwE4dvHkJsKnjThmV6orEZl8vgJ3Rq5uT0cM6VHeZ6N1iD37KOJp-P8q5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
لیندسی گراهام:
من از تلاش‌های جدی دونالد ترامپ برای پیدا کردن یک راه‌حل دیپلماتیک جهت تغییر رفتار رژیم ایران قدردانی می‌کنم.
ولی با توجه به حمله‌های مداوم آنها به کشتی‌رانی بین‌المللی، حمله‌های ادامه‌دار به متحدان آمریکا در خاورمیانه و حالا هم این پاسخ کاملا غیرقابل‌قبول به پیشنهاد دیپلماتیک آمریکا، به‌نظر من وقتشه مسیر عوض بشه.
در این زمان “پروژه ازادی پلاس” خیلی ایده خوبی به‌نظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64873" target="_blank">📅 09:17 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
