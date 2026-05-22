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
<img src="https://cdn4.telesco.pe/file/YLSE5Y95NH6XxkigtQvDFxJBJd247jKZLVfMYj2FVthv96uKL4MdQN2OPZVCyn5sPT758YPYq91fYqI8thXLYmjTvS4rCaopVrbdkBlJOJZ-5HlL6uV3C_CVoVLcPY2G93gKHkrez17BtgbwDTTD9O2QjQnHIwuaYgHaIs8vvkGzDt0DbdGWsza_OJDiVjUe9LlkhVSD_ACh54HICKCp6RmpZIZ758vEzcEI0M-E2w608yIJtneLFGCZWCnpSDDwM0uhcqBdbF4TSF3C1cUummDpeDH4n0enwrmZq8STzs9MHsTFgDslwFQoeO1pbH2UV42guH2cNywnc9Z5HO7YVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 141K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 13:48:30</div>
<hr>

<div class="tg-post" id="msg-64993">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
سفرِ «عاصم منیر»، فرمانده ارتش پاکستان به تعویق افتاد، این یعنی هنوز اختلافات ایران و آمریکا حل نشده
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/64993" target="_blank">📅 23:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64992">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3890f54566.mp4?token=nN6fJF7ND7qTdjik55bqAM3hyR14uyCSeJC_aoK-qcqpgkCqNLxA-K30DvxA1DDuwRVP8SkCftdkj68Q1NC8_Ff3s80zCvWMH7NHj9SmyDDz0Wrpwwl9SGFB7tcLfiTVds0PcMZUPb8bIu73guv4-oxy08V-VUI8zD6PmP864IrOFSFNsaeGpC_xdByuYazOYBIlX7nepaarKm4In6uxOyIil5wU5oc2lSDMMFtTC0fXgKVcp-B9DPt9ZtRTvT0168aKxFu7V9xfo3xnuqpCWc37GPWkgzLrsgq8Ka8Uy8NTnRuN2PRl2wEP81qMhEaDUBl4Sw5rZgDWgY7hXLfumQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3890f54566.mp4?token=nN6fJF7ND7qTdjik55bqAM3hyR14uyCSeJC_aoK-qcqpgkCqNLxA-K30DvxA1DDuwRVP8SkCftdkj68Q1NC8_Ff3s80zCvWMH7NHj9SmyDDz0Wrpwwl9SGFB7tcLfiTVds0PcMZUPb8bIu73guv4-oxy08V-VUI8zD6PmP864IrOFSFNsaeGpC_xdByuYazOYBIlX7nepaarKm4In6uxOyIil5wU5oc2lSDMMFtTC0fXgKVcp-B9DPt9ZtRTvT0168aKxFu7V9xfo3xnuqpCWc37GPWkgzLrsgq8Ka8Uy8NTnRuN2PRl2wEP81qMhEaDUBl4Sw5rZgDWgY7hXLfumQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آیا در عروسی پسرتان شرکت می‌کنید؟
🇺🇸
ترامپ: او دوست دارد من بروم. من سعی خواهم کرد. گفتم این زمان مناسبی برای من نیست. من یک مسئله به نام ایران و مسائل دیگر دارم. او شخصی است که مدت‌هاست می‌شناسمش.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/64992" target="_blank">📅 22:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64991">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/64991" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64990">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyXOcgMDloepFRV4LkQhkXXLW6Lznj_FTM06lpWkKnEk3UC4Ekhd_j1rhryJntUzhOfBsd0Krmw938kqJCslo5rHdBT1NBfM2FzItDikPfOqI6pAU_5MM2YQ43DoWeQbKhe04fjzruZLjsEWFIh34vZ8P2mlcbiFTwanI_GZDhLktadmbYl4W7VcO1TGOvP5mb6Klbc2xKeafPb2WlW8FiVRZbJkFmkAbH2ZY-EwNpgHwiE3vags65M7x99JRJdpdm7dwsp8Wm7CceLyXvKk4Z2M30Laktaw9b9Pap4LCJiQiizWwjeMxsUEKDcgZ8ojMxWKp9fHvsVddHqS0nSHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ یه پست از نشریه نیویورک پست بازنشر کرد که تیتر خبری‌ش هست؛«چطور میشه تهرانو تو سه حرکت نابود کرد»
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64990" target="_blank">📅 16:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64989">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAOoxdRcARPFRjZ9ziZ9OmBiUgigH4N8ZqZo4TbrHRW5w4DVDh9Msb2ByS1CFw615V4aGcyFu0EF7vgBsZFj-Ubvn_cE9y_YYyMILXVlU8zGcgO5twIiwi5GdZ463Ea7D-jDFi0kUCRGReXJ7VgS7CGL8lUK4SVzwoFf1rqp9gPRa3t85MWBJJoa-O5BROS-qETFOFY0JrREbJcGUtHh0hJ-1PJrc--HaMMY7gNmXwolzvAQisZlsrqBnVvr8Ig6oGmcBavH1A5hmNh0f-BjKLkVwItuIgRkImuQJHMBD2LCuJv_Hs7wfnJYiZy7M-2NWvahVgHUcdi2jk2xmA8QBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ جدید هزینه‌ ریجستری گوشی‌های آیفون
ریجستری آیفون ۱۷پرومکس، ۱۰۴ میلیون تومان!!!
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64989" target="_blank">📅 15:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64988">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eppa0wiVSCzuY078ThxqJoExD6kfWme_QUWBZolYoqp2R_Tki5YlrRUcEXpYGyrKuLK49IGAeU2_wV99yHm0N5-TOYr6jEVlcRMzgcL7DD0sDbPsVYnAwaDWPBPaEMyair9Va_E4AM-nshDvtdIaRIULGraXiF4QxHdHkjjY4BeCyxCgCxawZsvx3JICwJJXI1RCHGJFZGxyrioSiT5JP8DTtI89l5m2NWZDoB0I4CDv6oQiVbx1syNRcCjjWAXXQuRkoRBPSJ34SUq2a-02pb9FBuN72B_QHQ5aX7B-SVaVtg86yvbSmvE2V3czSpHSOsoLdWHDvVan81DgarlM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فهرست کاخ سفید از مهم‌ترین دشمنان امریکا که در دوره فعلی ترامپ حذف یا دستگیر شدند:
رئیس‌جمهور ونزوئلا - مادورو
رهبر رژیم جمهوری اسلامی- خامنه‌ای
معاون رهبر داعش - ابو بلال المنوکی
و برای رائول کاسترو رئیس‌جمهور سابق کوبا (و برادر فیدل کاسترو) کیفرخواست صادر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64988" target="_blank">📅 15:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64987">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
📰
رویترز: منابع ایرانی می‌گویند رهبر معظم(مجتبی)اعلام کرده است که اورانیوم غنی‌شده باید در ایران بماند.  آمریکا می‌خواهد اورانیوم بسیار غنی‌شده ایران به خارج فرستاده شود مقامات اسرائیلی می‌گویند ترامپ به اسرائیل گفته است که این اتفاق خواهد افتاد دستور رهبر…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64987" target="_blank">📅 14:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64986">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
بندرعباس ۴.۶ ریشتر زلزله شد
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64986" target="_blank">📅 13:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64985">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OcrQK2OOG24xnlzE_J3lH49DHo8Gc4tmz-yPMfSGeH3kIzxljTVVSnJcr7ELq1RE1gfsFeqaXnkQCcObgXL60deTiav0gHIuK2eKNado14gWp-myLoFvbO08rGiLqDD0TRCAqX7Q2frY8CUMqYIQqev-u5JvyTGtI8Yt5PlbAv--wT8tDEpc_3dvKQ842A4y0Axarx3x_UpuV3sVBc5i_usm6lfyWNdOpSx2IOMkcOAsYQrTLMCOXY5XWiYL16J1zDs-1UaqwYPUdQB_-ZCS1-cClU7vwM_QL6EuheF6p8JCDB8IONRdaJNaIpfEZBUPAWRzgZl0zcJ7GhkzLVcU4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شریعتمداری: تا زمان شکست امریکا و کشتن ترامپ تنگه رو باید ببندیم
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64985" target="_blank">📅 11:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64984">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: اگر فرمانده ارتش پاکستان به ایران سفر نکند، توافق نهایی ممکن است ظرف چند ساعت اعلام شود  @News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64984" target="_blank">📅 10:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64983">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خبرنگار: آقای رئیس جمهور خیلی از خانواده ها در آمریکا نگران گسترش هوش مصنوعی هستند، نظرتون چیه؟
ترامپ: هوش مصنوعی عالیه، ایران نباید سلاح هسته‌ای داشته باشه :)))))
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64983" target="_blank">📅 04:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64982">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: کار برای نهایی کردن متن توافق میان واشینگتن و تهران به طور جدی در حال انجام است و دور بعدی مذاکرات پس از حج در اسلام‌آباد برگزار می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64982" target="_blank">📅 18:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64981">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: کار برای نهایی کردن متن توافق میان واشینگتن و تهران به طور جدی در حال انجام است و دور بعدی مذاکرات پس از حج در اسلام‌آباد برگزار می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64981" target="_blank">📅 18:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64980">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dv1DfwI_UOgAuRNLdPIUEJBLcrV6X9AfwJ3FtAfs4rBdEGnykjvfFGSKGLwdZKMQg6HM6FDOK6mH3PSkf0N2D4aT3C3cATDD8SmjAvxw8LAE_IA9ClfxV26T26_o1klwTmTnJeuK313KnA4G7ZuBfbgww7j-DxlmvDbFIuZSs36dAh_DBdcBCapucPVRd0HuthjCylcLDq2EHV1_QrDN_BLhjpWKFdvJTLfvxryzVCsZLG-bu5qdomI_dtBkVXnvldPYOmYSWx47SELaSU7vABtDOrjDXUVq19xH1FNDMopJzh4b3gCIIBu4BeLlSR8Zi3E2QkEdAO6n5q1mAMt7jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای مرضیه حسینی خبرنگار ایرانی کنگره: یک منبع مطلع اینجا در کنگره به من گفت که ترامپ روزهای چهارشنبه یا پنج شنبه پیش رو، به ایران حمله خواهد کرد.
به گفته این فرد، این حملات برای یک عملیات “دو تا سه روز” متمرکز خواهد بود و به مراکزی با هدف بازگشایی تنگه هرمز انجام خواهد شد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64980" target="_blank">📅 13:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64978">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HYNn7Vn7Se-JImgQEmZLmu4URXDA3nFwDh65akGArZTBx3nwg0pPlGOzHj0WmbIjk7SBaP_sLNAOSw0br_ukYTWsSC-Jy4YwNPEnw4bGZx15MhNeXqdseevcvZEbEty3pFvNDV_RO5yCJcz8Tmb8bPtZ8Xs7ayE0SavAY_sKPPRbff1DMsdqyy4r8bftycrXRrYnGz0adogKIUmBl372Wae98BvmFdQkZ2BBESApGjOj-wQIgrp5FfCUxnG8aXzsi7rBECGeA2Y9AILSPpg5TslwdpveoYlOqZyx9gmI5CLXHKLeLHK_i4Np3AfCuGdeO4Vfs3BHIeS4nKLSGMWzTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHQHE5C2TG3JdUxaS6SI4kCOPo1-O_fBPP-L6nUrLWcO7vGi54YIU511lkvI33XhCDy_hl8V2BTmes2kY33t9NKuFlCF-R401HhdrO4czVQZiYNLGCg_eh3ffXeaAoJxWt8UV8xVDubcOdFapYRVmMj5gtcrD3QjmF-E5w1l7sa2uhbIfrq7aDGZK2wpHZYuq334TTUw09llt12f8pEZT6xcPmGiWXnxkq6Vf84bRXrPysldQyGb4iswGQrUUYQ2osBbPi-m3TSQJCbiPGdkizu_f3J9_L3QmdH7omRK5aNLZTsbhYS_V8clEfKi_VkVGB2FfW6xHOZgs1JVY2Qi_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
گزارش NBC از موبایل جدید ترامپ  به نام «Trump mobile»:
مدل T1 با قیمت «تشویقی» ۴۹۹ دلار به فروش می‌رسد و به صفحه‌نمایش ۶.۷۸ اینچی، دوربین اصلی ۵۰ مگاپیکسلی و حافظه ۵۱۲ گیگابایتی مجهز است.
گوشی ترامپ موبایل در چهار نقطه از بدنه و نرم‌افزار، لوگوی «ترامپ» حک شده، پرچمی آمریکایی با ۱۱ راه‌راه به جای ۱۳ راه‌راه روی آن حک شده و از پیش، شبکهٔ «تروث سوشال» روی آن نصب است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64978" target="_blank">📅 13:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64977">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358ed734a6.mp4?token=jL6VJ22uO6BFeqFydzV1hw_k1uxOWQY34VZFIEIzDkThDd6hYHtmATaKnlIA-J6C2upYpERtU4eXmtlhy8UaPKI1NT-RS7Jf2x-eFAq52c-JoDVTzDYBtArzoG4li51YGaRzNhoAxqB970TbNPvR1ucib3OhSpDIoRBg3ee6wShxaQZ-1vthPBUsJKr2vo2hpPK4_HpdYO8lZplpy6_eFfkxcw6zk1a7z4k23UrxYNRghi9Hrwfg0nc7DpCH8G5hZEN_Fs-IVY1T-Th-gL1rxhXJaeKqtFbQ1UrS5MVI1hx0P5qozdPqW80IYv6AOZqbXzW1XHfBaA2HXhQCaYW79Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358ed734a6.mp4?token=jL6VJ22uO6BFeqFydzV1hw_k1uxOWQY34VZFIEIzDkThDd6hYHtmATaKnlIA-J6C2upYpERtU4eXmtlhy8UaPKI1NT-RS7Jf2x-eFAq52c-JoDVTzDYBtArzoG4li51YGaRzNhoAxqB970TbNPvR1ucib3OhSpDIoRBg3ee6wShxaQZ-1vthPBUsJKr2vo2hpPK4_HpdYO8lZplpy6_eFfkxcw6zk1a7z4k23UrxYNRghi9Hrwfg0nc7DpCH8G5hZEN_Fs-IVY1T-Th-gL1rxhXJaeKqtFbQ1UrS5MVI1hx0P5qozdPqW80IYv6AOZqbXzW1XHfBaA2HXhQCaYW79Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان،عضو کمیسیون امنیت ملی مجلس:
امیدوارم خبر سفر عراقچی به نیویورک برای مذاکره در خصوص تنگه هرمز دروغ باشد!
چرا ما در خصوص موضوع تنگه هرمز باید در خاک اسرائیل و آمریکا مذاکره کنیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64977" target="_blank">📅 10:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64976">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
📰
نیویورک تایمز:  ایالات متحده و اسرائیل پیش از جنگ با ایران، طرحی را برای نصب محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، به عنوان رهبر جدید کشور مورد بحث قرار دادند. احمدی‌نژاد گزارشا در مورد این طرح مشورت شده بود، اما پس از اینکه در حمله‌ای اسرائیلی به خانه‌اش…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64976" target="_blank">📅 09:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64975">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دموکرات های احمق برای بار nام خواستن جنگ رو متوقف کنن که بازهم رای نیاوردن  @News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64975" target="_blank">📅 08:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64974">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjE3UyV0u02pIUG5t97ijjGp7320h-LTwtQzTNbxhtGwF0GFf2e72qzVg2-WnPifVRJlvZU003xH8jfhpF346wy68MsGe3UBd2wGJ5Yqgl5gHA9Oa1UHSBxKHlYjegCbSh4bcbIsBvWOtjJE7_jwrg7ro0REBiHAdyWF48m8VV_KBSlJP9tpVAzmdrILM1YIuTU3qa4hPVzSlsfG0f1HGI-f0vQtm3koY9emlxMn_OOjm64NcOH7e48UNfum3OLZKQzl1dZSEAQVPOzO30f6rM9z8FjsRg1tZkqWmUZw2AtiIZrUQBSYjVRe0u-mrcYOEpZIS7iPULKPkvf1PacH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور لیندسی گراهام:
امیدوارم و انتظار هم دارم بعد از این چند ماه مذاکره با ایرانی‌ها، دولت ترامپ هر تلاشی رو که برای دوباره کش دادن مذاکراته رد کنه.
این رژیم ماه‌ها وقت داشت به توافق برسه، ولی به نظرم واضحه دارن بازی درمیارن
من ترجیح خودم راه‌حل دیپلماتیک هست، ولی قدیمی‌ترین ترفند ایران همیشه این بوده؛ امروز و فردا کردن، کش دادن، کش دادن، کش دادن
در مورد هر توافقی هم، منتظرم بره سنا و اونجا بررسیش کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64974" target="_blank">📅 07:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64973">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmnLMrFUgcMr9bh5NG9Ux_VG0h5NAuYh3OQ07xSuYnkqrV9OiAgIVTawNgaKCyGiTdFgUCV7zF2mFS1jNUKpbIYjj6Xfw6417NKFUWmedIP-1qHkpAJox9v_CxXkyWGALraCCmOmjMpz1kLBzWEPsz-4trnCXZGw0dRUeXIBZ7ez80NfPYmz3Blxsfe0bt_ZwLyNJtLi1ST4QkuIui-DJYRWBCDXv-cInNkdkhfDXmLSqJ6jhKqA1PJOnJ7BkzijqKcdOJ9DmtXILBl-TrAQ7foziQJbbXk_oMX7RKBh2puKKNQvIJKsYtmPhGtaPXTQyiIkrg8nEEP74yvPbD3Nig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غریب‌آبادی، معاون وزیر امورخارجه:
امریکا میگه دستور حمله رو به طور موقت لغو کرده و در سایه تهدید می‌خواد مذاکره کنه
اونا باید اینو بدونن برای ما، تسلیم معنایی ندارد؛ یا پیروز می‌شویم یا شهید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64973" target="_blank">📅 00:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64972">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🇺🇸
اولین اظهار نظر متفاوت امریکا نسبت به حمله انجام شده به مدرسه میناب و جان باختن کودکان این مدرسه:  برد کوپر، فرمانده سنتکام: ایالات متحده عمدا به غیرنظامیان حمله نمی‌کند. مردم ایران دشمن ما نیستند. سپاه پاسداران انقلاب اسلامی در این مورد دشمن است. تحقیقات…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64972" target="_blank">📅 23:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64971">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b854a8a43b.mp4?token=DS8SaWHU6q1O1u9YVw6pshH5OkYBl13iAuzOv7B7OR2JZDXoPaGdai_1U3eapbw2S3R-_C3leZab_j2pyYxfu4H4YdBCwUObX9kxkFhz8tV7m9DZnElqJQOIPuUFUS1jIDsBzpBB-wXpCJdaqsK5NTPhtai3EGqd8UPvMyV9ICODx8vPWIkYwRo2iPd7fS9aUEYUsk1nz1s1S7CrpUOFa2rYa1JxddA4LYA4AwYanQWeI6glvrwV1d7zmh8rw5lUX737nvC6qgbEMuWhXuAvffDa3VAvA9MgLbOV9TCfJxQZA5d9DWVafmuKZd1yym5Fb2rGb6pUEcnYCG-v2kstWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b854a8a43b.mp4?token=DS8SaWHU6q1O1u9YVw6pshH5OkYBl13iAuzOv7B7OR2JZDXoPaGdai_1U3eapbw2S3R-_C3leZab_j2pyYxfu4H4YdBCwUObX9kxkFhz8tV7m9DZnElqJQOIPuUFUS1jIDsBzpBB-wXpCJdaqsK5NTPhtai3EGqd8UPvMyV9ICODx8vPWIkYwRo2iPd7fS9aUEYUsk1nz1s1S7CrpUOFa2rYa1JxddA4LYA4AwYanQWeI6glvrwV1d7zmh8rw5lUX737nvC6qgbEMuWhXuAvffDa3VAvA9MgLbOV9TCfJxQZA5d9DWVafmuKZd1yym5Fb2rGb6pUEcnYCG-v2kstWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جی‌دی ونس، معاون رئیس جمهوری ترامپ:
گاهی اوقات کاملاً مشخص نیست که موضع مذاکره‌ای تیم ایرانی چیست.
گاهی اوقات سخت است دقیقاً بفهمیم ایرانی‌ها می‌خواهند از مذاکرات چه چیزی به دست آورند.
در حال حاضر برنامه‌ای برای تصاحب اورانیوم غنی‌شده ایران توسط روسیه نداریم. این هرگز برنامه ما نبوده است.
نمی‌دانم گزارش‌ها درباره این موضوع از کجا آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64971" target="_blank">📅 23:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64970">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/64970" target="_blank">📅 23:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64969">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=YJu_zZNW0Tn8xZUK7rBC1SH22xSynRJNBxTN8idqHAElAkV4tyPo2aPXcWttDesSscc9NY1kTBrMJyy3MfyXhHz8cyZN4Rr7xP-8Lmgf4owHDWaD5N8Wr0ga_V7sXzoFKC2paUkDDflmYXEZWfX-llp03RrYetZV3K1FF66e65pbnDQeDpZCgb3KC-OumyHu_ohLC1yoH2ek2lilcErHIyco3OzGI_TWhQj0eyIhWWY33asFBHQd8M6VIrQZo17plllzyW9EothrJAfQllo6-lncnxTO9UdcZDhPOyxFB3am5luTGfhmWnMuMk2_IxCrjSKClLmP3xz7sosuZ6urWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=YJu_zZNW0Tn8xZUK7rBC1SH22xSynRJNBxTN8idqHAElAkV4tyPo2aPXcWttDesSscc9NY1kTBrMJyy3MfyXhHz8cyZN4Rr7xP-8Lmgf4owHDWaD5N8Wr0ga_V7sXzoFKC2paUkDDflmYXEZWfX-llp03RrYetZV3K1FF66e65pbnDQeDpZCgb3KC-OumyHu_ohLC1yoH2ek2lilcErHIyco3OzGI_TWhQj0eyIhWWY33asFBHQd8M6VIrQZo17plllzyW9EothrJAfQllo6-lncnxTO9UdcZDhPOyxFB3am5luTGfhmWnMuMk2_IxCrjSKClLmP3xz7sosuZ6urWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره اینکه ایران چقدر وقت داره تا توافق کنه:
دو یا سه روز. شاید جمعه، شنبه، یکشنبه. شاید اوایل هفته آینده. یک بازه زمانی محدود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64969" target="_blank">📅 18:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64968">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2efb45471e.mp4?token=hmAWTWDyutSWHQTaliGwYylri93gw-nA0wHX5cBZtENiZ1JdElj1iH_ChlNIK7bkj_56aGmuen9-quSVXI-b9j_F3eHatd2DCkgpfYU8KNN-2hC2aJTZOPXqseK4xa6GlR23UB_v_9nGukfONUSKT4udWbjdZdoSvtgGEUaCWfR_38PmRKcGuTyfm8CndzEEYMLSWVZKYro9jWL7Wpk-JgrTnGLLakMQ-Fp0AcEpRJ1Kaeh-6DDqXosy_sdRY11tug3hNaqeAhMWmv2SORB3Bstd4-uRderjiP7liGH55yQr3MPiB2-9ni-ampR4LmH-71AWa0Mdqyi9-VILc3NLtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2efb45471e.mp4?token=hmAWTWDyutSWHQTaliGwYylri93gw-nA0wHX5cBZtENiZ1JdElj1iH_ChlNIK7bkj_56aGmuen9-quSVXI-b9j_F3eHatd2DCkgpfYU8KNN-2hC2aJTZOPXqseK4xa6GlR23UB_v_9nGukfONUSKT4udWbjdZdoSvtgGEUaCWfR_38PmRKcGuTyfm8CndzEEYMLSWVZKYro9jWL7Wpk-JgrTnGLLakMQ-Fp0AcEpRJ1Kaeh-6DDqXosy_sdRY11tug3hNaqeAhMWmv2SORB3Bstd4-uRderjiP7liGH55yQr3MPiB2-9ni-ampR4LmH-71AWa0Mdqyi9-VILc3NLtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: دیروز چقدر به حمله به ایران نزدیک بودید؟
🇺🇸
ترامپ: یک ساعت فاصله داشتم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64968" target="_blank">📅 18:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64967">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:  ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم. خیلی زود خواهید فهمید.  @News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64967" target="_blank">📅 18:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64966">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9954bd7931.mp4?token=jyQLgzjCPnHtnc852295aO_SR1sJpastTwIVmap7dSh9O4KA6oTKIsLMcvP6xROrOmCQNVC22ki4SYgf2OcPSN327zDeWGJZKlFfU6B5GZOR5GgRsNAZfhM3ZGAam8oofE5Wx1GAnKvJxrv8XlwGzYs4SiZUSvQJMOHaCH5KPbVG3tF0rRazJ97T-XRYah8Qmk2gIGp7SVDgvOBfJ_1KFgKZuyyRzsAtb2iJF-OXoJD9qzzEO5xdvV3WaO1tp0F3_oBEuA_YNOQPp-eNhRXWBggvB6Y4xkrPnGmRXzTZ-4tvVOXhziBFWZ33ZFVU_8UJaNRpCClgYod0AN3WZAKDTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9954bd7931.mp4?token=jyQLgzjCPnHtnc852295aO_SR1sJpastTwIVmap7dSh9O4KA6oTKIsLMcvP6xROrOmCQNVC22ki4SYgf2OcPSN327zDeWGJZKlFfU6B5GZOR5GgRsNAZfhM3ZGAam8oofE5Wx1GAnKvJxrv8XlwGzYs4SiZUSvQJMOHaCH5KPbVG3tF0rRazJ97T-XRYah8Qmk2gIGp7SVDgvOBfJ_1KFgKZuyyRzsAtb2iJF-OXoJD9qzzEO5xdvV3WaO1tp0F3_oBEuA_YNOQPp-eNhRXWBggvB6Y4xkrPnGmRXzTZ-4tvVOXhziBFWZ33ZFVU_8UJaNRpCClgYod0AN3WZAKDTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم.
خیلی زود خواهید فهمید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64966" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64965">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=IHKnSAAvTPlOVeLttHeX67cvRhFmmmA9XQ9cGxixTu1E1C4RzG7OZs4_WEXXhKRsmPZf9QIYwRjEf3GGfPnwe8g4EVK4ff5An9CXi_r4Nbp5NaxcoDfufNrZGUN9MAwUYJZEvj9xLdYmR0_d5kmMgbOWY0hUdW6pUi8HsobVaMCY8FwT5HGuIhcJyfrj1BGvmC68ANZm-_vGAQ_KATFRnBdk53bfVUSNrRGi6yvyFikbb36DGxLbGN6WXQFzLstNaWLjrmfkEkD7DT8mIyDhd7S60rqP5lmaH0ZphSsFBTaDf2dURBsAH0KaPGTlj5sngHNiMvs1lZ1PC3XoE2YBsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=IHKnSAAvTPlOVeLttHeX67cvRhFmmmA9XQ9cGxixTu1E1C4RzG7OZs4_WEXXhKRsmPZf9QIYwRjEf3GGfPnwe8g4EVK4ff5An9CXi_r4Nbp5NaxcoDfufNrZGUN9MAwUYJZEvj9xLdYmR0_d5kmMgbOWY0hUdW6pUi8HsobVaMCY8FwT5HGuIhcJyfrj1BGvmC68ANZm-_vGAQ_KATFRnBdk53bfVUSNrRGi6yvyFikbb36DGxLbGN6WXQFzLstNaWLjrmfkEkD7DT8mIyDhd7S60rqP5lmaH0ZphSsFBTaDf2dURBsAH0KaPGTlj5sngHNiMvs1lZ1PC3XoE2YBsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار طرفدران حکومت تو تجمعات شبانه: مرگ بر امارات!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64965" target="_blank">📅 15:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64964">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
خبرگزاری مهر: صدای انفجار ناشناخته در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64964" target="_blank">📅 14:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64963">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugRg45oWuINhpyOx49sQlpq5fKeD_tRUQOBmV4SU3RkGMkD0DJKOcr3ecXJmwvjvlRKU8rWSvNwBkw3FwIB5MUaHE76Ygz_jRI8WKzAwGqKEuO5lLhBskG18Xxv493Nh60b3PslfVOsVzWgjGkPM9SWukq52_onl0Y3Dot1682Fq4iahlwRVh6qswtKK0IvmWr5NCKsPeOZr8ieSyooiT3dxkyqRUXCUEMB54C2vPAZJqTIG5rhPpqntCZKkI04ak3g_nz_ZBXNTvr_vYcb3N1jfQiCmrP2ULE4aSIWxK0Z76B220Ttnuy6mJV6CjL_dJSNVeu_e-uKJ1IwVDc3NhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:   من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/64963" target="_blank">📅 01:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64962">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZyUVy0Kz4NFqWKbH-1ws0n-q2VTBmJgLNdKMSOhZaiIPQMnIFyyzAVwdmyM5jh8xkG6ew0_cHeP6JMeNXowXOSOugidmV1XAsr1b5iURs6N442hYbh4rva-LfT4pOpmwsZ3Ql0v84LJxmFbQ2yVvtehixNy4ogX2CVq-0UIuEz61_vzzEenwj7sJouZU6SlKUiOpJnb7hp4SV3aqSZ-ywTv9buAoOJck8MLC9YMSMgquzK6vz5xLmndjOCODUYqWO1jGrJuMtt49V7QoLkuo9Md337lSyiOJbi9EV_iMSt-jdMShBcqMmARVDjFck2tiYNoLCHTS_6EapsrId8ivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به سلاح هسته‌ای دست پیدا نکنه.
با توجه به احترامم به این رهبران، به ارتش آمریکا دستور دادم فعلاً حمله انجام نشه، اما همزمان آماده‌باش کامل هستیم که اگه توافقی به نتیجه نرسه، در هر لحظه یه حمله گسترده رو شروع کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/64962" target="_blank">📅 22:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64961">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3pKbqLNUobRFJhYDuB3VSZwawRRXVCJdfeMJwej0ckAt1Ginz2T78iD-mzbg__5yFsCHygG3mLDZj-XCR2dV4x62NFtwTlNTVzPUw-LrexPBSZGwz39J7CB-VwY0BJBbdl3H7IzjnNj_IQZwZU64v-ed3CVHbmQ8RabQ-wQMztWJCxu3eBk2hkxZipG1fnqeDP9hyfPbaWhm1Ul9xt7z4dx8GFXw28WkhpSsLCFSWmVT26i_583LpvqLMaB-m7R4VrL6e0D2wwGPI07130sJH4Iz4s5dKLmKVdi6zOZwMzBmMJyqili3aOLmlX3-gV-gi1Kyv5KdDt5B72R4trV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
«اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» در حالی که پرچم سفید نماینده را به شدت تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌شان همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی بزرگ و باشکوه ایالات متحده آمریکا بپذیرند، روزنامه‌های در حال سقوط نیویورک تایمز، وال استریت ژورنال چین (WSJ!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و همه اعضای دیگر رسانه‌های خبری جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است، حتی نزدیک هم نبود. دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آنها کاملاً دیوانه شده‌اند!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64961" target="_blank">📅 18:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64959">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MuwYIrm7n8EOfDVHge4L1uQfOIMOmOpd3g3jRBYZAaB8D-z0tXgx6sSSHGwCczr4THq49v7TNSGYe5VwpWRtGSo4pib6Pw3tTnRE1uzmj361MmNepCX7Wcmd6tc9c-llQTFF37pEZ8jufLDgt8rXAcDMT1C_1R8KseWjXf4eVEcIuTuz930ULDwaqrtp524DAvZaQjLglPsVlDEkDMsJ3SHGs6xAHSTx2opm_Hlry42yDU76w-WJqJ7OE77Xr4g3T_PiI9vL8fuJiW7q8F8Ws27CKfU8Ev1trw4evUnkt7dVui-71gsjSyFaEusYnnx2zqpjeCEK8FtM_TQOyk28RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PziOAdPXvHenksVzD1XgGn5jQ7uyx29lOfd9gChn2xFjFYtsB8aI0TBv4-SbjQ9VZwzq6mRRDDmSNuy36fWHll1r_mJoHBAbspqgF-La62_uRZYSCPvDlLhIUFAhRWZQv8SaDD28Xl3OgOGZhsx3pMYTwc3xTIW83xgGdTRcm3VMmLbxkvk39s8Qs8akuj_mFfCCbr-T9DGasKsXcWjYDqSNkReLoocUJYhzzxwIwUWTCzMjNNc5Ev-6Oo1stgxrnK4Hx_dLzynBsH-N2cZWGl7aGdqXoIvVH2cGKkyhXfKLf8GAJIljvBgzL5YxPCk24MGjA2YzamOcMQ34BgqTUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت خودرو ، ۲۸ اردیبهشت‌ماه ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64959" target="_blank">📅 14:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64952">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BKPMJbIBIav8qu3hd3sZ_VpxAx-QlMEoJN7Okg0hcTzq2ZqLrNEHAZdpSJ_hr7LwuWLedz4M9HCKxIJpZ_vptXnvAYyM23EHzCOLln65T6n2eRo0UI4vIN__VXQUtia50_anVm_DFtNV9HMotPErqQCAyFCPh3oKu4M5edkpqdrW-Ue6p5jWzR36nJ-eJBv683WzVzZViRvlLNBakGwqZk5juVyE-yO1vA2lK2nQdtO_o4lKbFz2XKWeEhSQL9ajykWYOVeZBPVv_5U2fnGkQ9GG4yw0X18U49tGVP6lT9bzogFuvjb6Hzc1RrxtV7U6z2UekXrlS_t_t8QPYjJB0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TlG3fkv-c0vBsHK4kdcBLdZPldUrXprpvdQEGdOed2iHI_iqS2-RNDu0qXrh_9A_Hnssat4N-kGN1JHgo4EjQGRw_msBVAMlSlV4l2len9bc-sEghKL_HonL60FhH7qZumCTytUzlBd13mgGH21fxA49jx-momXveveo28CFUM7hzxByA0iKVQyCs7LYGLAf_EL905QHYYsj65xdetN_hBu1zcZec_9XeQdr4tL2Mh78uIGBfTvPRgNRjSX5QH-jQG0KLx3-3j3GJGjttYvOcvQj_ZTVI0ZY75pSjKDngxoVbrwjkaH2_RLbOmfUPwT3m6Z-2WQ4Hlol_vDiyEUXiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/danH8DpAyLcMzWw6GX6V1i7d9AHfnWg8D8BE1asbqfGtFB-FaLZMPl57ESqv5ROgxlMgzmTsPehxVSC4yXoidO8_61Htg3BMkWiGChhQLcTSljoSscSbms5MSk9yrfEc9mOKLSZHKlTBh0mCQPZVR3MjoeGXpjuHtOQ6OlWqDU21xic7SC1yf4Su56ni2wwwG2ioIePB3FWu163IuGpEYg-60FrmiueLcCwPlFG4sdi79GKVreGoSRJbA0Vi08Hb4jln0Rm5TuCj5W3vPuryy6TfKzGq09giVlDvtQ7LhMPtEQFq9veZBak2HCpDOulFlIwB7KvB2OVI0GjKFMbSbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Am0ZhHfPXJywYgDMHvETOJQlnoNI4D6B6xEwjkig_rPEUsvrobu0vr0QWauo8_6sXK_hgpxPwgs0lcwU6Cr2ZEhgyKcaYNa4Z68YeM1Lz2TMHdHiTYmxHwpMkiIDesxOACWAPHJaHtAHL28SsHLcSzCRdkmHkvasaEAV8MQN_J2LDO294zxnOsezR2DOOqCKevwrdwKF7MUnNk0c_MDut9VSiN1y5dKQd2Q4x5u2Aq4j7e4IEijQJynHPyJhG8J1IJYBB_uEMRUAmd-Hgb0C--AqcBzUVWa-Z9BBX_6lyaa1dH5nMOFrjnEmjHqZPgOP1pTK5bIPe1RViBuXettZDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TATQTQ2iVaKaL8BVdKXGINMhYEJKCVYa1jGEzADR88LSOy9cX9ECf9s7Ni4rYR4cKcV5PXi5EYvYR15dXA1rUjr9T57AG-XEXOatlXELgdUXOHyE-XROaEtw6fL9n8WzUqhsTgvOxo6myDxFVI0gMzwpzhkfR55z6IrGqhvGzra6pDqlimqFyWhfTriRNuqZIdQp9h7z_oJHlYcQ4Nj6e_47iIH6uClXgHFhGOR2wJ7wXUz7TJFqG-xzm6duZ331opfWwAtPdZEViTuClI02ISAZ_9ECROO6I9_Hkjb5VNWSR_uD9WmhZKG2YK0Xx1PREnC8yrI361Ew_Nd95dW0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ar7IvM4cqiKwrGljGO-TebPLs2AwRKQILJBn077B7pIwg7IBU-QPj6_p7seEozRevilIhrweh-TUZJtSe8pwDs8Bz0SLFyM8OWYdqKpxzMcbN9S59CmEvGxweFk5zys6eP3UKVDcUjfMh7D1mXREvRczq7Ot8CkOVT8RFnMXG1w36lp2OW9-i_s-1oTR7XXHvWMqGY3aW-sV-ZkokTngZdWNHwJiTGYoh_6zoQYs3nUdNUhLr3ercC_ZJL_ZH4SmOg85lVPE8NOq_wPoiMtqJTDW95KboWPN1p2xCnMQi4lHbvf3hlxh6dXUVLm0GxaLrTG6KxHMeg3_eACr-m96ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a4qjyFjQfadd04Ptjrd1zXEI11A_9CAgrWyv65C_zLVfdaG9ksicfMlXGrPB48tv8FcXWCrey-MhzTh6oiTUqPbcFQZrK4RsDpUCy3Ep1WsQgs-Zf2D6IGguyZkcod5qgVn0dIG6ONKlVD7LaFoHFTjkxZESsCGwnr2ADPbXQ6FWhnW_T-o1SFymQ2NwTn_tpn0oeVw8dvFrpDhTClyRontbP5rA25HXMv5toeQz35JUedQyOEFdCllpBL3FffrwQwfWnhLpASMjBorfqsQIHZI8wDNL_9e28NFHG1L19LsK0B6t9rERGI4SiOxZq0PBbwt0-ynhT5KnukS0if_i3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
پست های دیشب ترامپ دلقک که با هوش مصنوعی ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64952" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64951">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7sN-OVjEnZi5JyAqiiYHyXITpSpUNEGoyF2C60y0Tqgf3iX3Vnxe3XWCTB5OAVtqtLL95uHraukPJUSE-vC9uDqvpI-2IIwKf5sgNYke3bY-Lo7lDHWgFr4-oxkZWdX6jHGVfz2R19jHyJgj9ztEm1nY7fjVqHa7vbL2GFqJJQSd7JOVy9GANlZv35XZvecIz-wvs6X73JsmXRoh0SF12IgotNWmZ03cMOkMsbetIAFmDsZH992Z5QVid-tTXXwhkRdfEgyb2rWrOq33tknUj686Z83G0lNhKIkec3R_ziZJo7ESSfuTsPiXXu2sMBLIhZpyqJZWSWDIB-d9BqLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست عجیب حسین دهباشی سازنده ویدئو تبلیغاتی حسن روحانی تو انتخابات ۱۳۹۶:
حملات و ترورهای دشمن تا رهبری حسن روحانی ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64951" target="_blank">📅 10:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64950">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gxrPstrH9IpR1k1O66c7STMz7iYiFHFN8X_MRvddoQbyxlAfTag88wWN1voLl1F36SekFDOneMX9u-b8UFCuPGt2VXXoFJaHA1Uf5Rhpzp1GpStK1F2_uJzrjGRoKX1mgJmnOnWJFCP6_yAZqWBStRFOqzARQ93uvoiyjJ3t8ouNgx0CQFTuIWV3ydjaXcloN9N1xGP3Dm1AjiVSNogzqhwlIaGUwMgz1KFlugV8w0JEdkQIuTGComEq9hp9U8tr-4N4pzemOvf2c4RA_vbYtdEy_NKROii8Mti7OerYjASR_8IFerLwziWBHOlQFrEYJLl45HCHEetEQsIi2PLV6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در شبکه اجتماعی که فیلتر شده
روز ارتباطاتی که قطع شده رو تبریک گفت
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64950" target="_blank">📅 21:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64949">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64949" target="_blank">📅 21:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64948">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=B1qWXBIJOvHhyX70e322KW0bTXeNP-Yvd4JOLX1Jt3bgmEpA9BslHomYmu4wKhuPL-HWcjaXWaazpQnHcyUnsZMR2u75AiW7TgZTlJETI41HmiftoYCrAEwyG5Q8NPwI_kuYt-DMy6S_Tlv6w3Zl4yCLsDMiDhm-x-OoeoZ7CDdnqhNpYWxWtoPbcCTRuCuDVlqdUS3CiHv7kGES_c29C91vyoQCM6ZH5QZ0BDdpUZ29yoN038SDQzX7P6DbG9K0ptgsa8Jor5by3o6y-aQd3El_pzO0kgWY9C1kPt1XFy0yChE6nBGvKuDudPXcC4Y__tznlzQplVmdDfvYRoZtVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=B1qWXBIJOvHhyX70e322KW0bTXeNP-Yvd4JOLX1Jt3bgmEpA9BslHomYmu4wKhuPL-HWcjaXWaazpQnHcyUnsZMR2u75AiW7TgZTlJETI41HmiftoYCrAEwyG5Q8NPwI_kuYt-DMy6S_Tlv6w3Zl4yCLsDMiDhm-x-OoeoZ7CDdnqhNpYWxWtoPbcCTRuCuDVlqdUS3CiHv7kGES_c29C91vyoQCM6ZH5QZ0BDdpUZ29yoN038SDQzX7P6DbG9K0ptgsa8Jor5by3o6y-aQd3El_pzO0kgWY9C1kPt1XFy0yChE6nBGvKuDudPXcC4Y__tznlzQplVmdDfvYRoZtVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
بر اساس تحلیل من، هیچ چیزی نشان نمی‌دهد که افرادی که اکنون در قدرت هستند با قبل متفاوت باشند
آنها هنوز هم می‌خواهند جهان را ترور کنند، اسرائیل را نابود کنند و به ما حمله کنند.
هر قیمتی که لازم باشد بپردازیم، خواهیم پرداخت.
چرچیل چه گفت؟ «هر قیمتی که لازم باشد برای شکست هیتلر بپردازیم، خواهیم پرداخت.»
همین موضوع درباره ایران هم صدق می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64948" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64947">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یک سری کانفیگ فروش طی یک حرکت بی‌شرفانه برا سرور هاشون ضریب گذاشتن، یعنی شما ۱۰۰ مگابیت مصرف می‌کنید ولی حجم مصرفی ضربدر یک عدد می‌شه، حالا ۲ یا ۳ یا هر عدد دیگه‌ای  اگه این حرکت کصشرتونو جمع نکنید تک تک اسم می‌برم تا نه آبرویی بمونه نه مشتری‌ای @News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64947" target="_blank">📅 19:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64946">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تسنیم: ممباقر گذاشتیم نماینده ویژه جمهوری اسلامی تو امور چین
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64946" target="_blank">📅 12:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64945">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=LK_7mXIiKtkRJaqnk2rZrJXTpQ1_J2ep9_SikANf78d9K558wpO2RYOSwkmeWgOuoXEZhOOEPFAsKXpDCA5PSVKs5b6M6kIqIQQWSIvL8nMxm9Cy54wul3SJhSSVpaF8xaTlkhD2kyq0jMq9lTpesOqIzcNtJ1bKbH7RG4XVz96027HKUIom3lsvdqwoeDM_AaSw9ORgAAGe0hRqpvbg9S-eJeey-qq-zQoGeLYF1Q1OYVz5bujnfmmKBAbTStupvO6pphqvyr_AWUU3RMgGB-PyCNKxru2Es0h6gxIVECPZplYa4va-QFP4JlD42wnVZnANBbPCADHeObHbMvIa5A" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=LK_7mXIiKtkRJaqnk2rZrJXTpQ1_J2ep9_SikANf78d9K558wpO2RYOSwkmeWgOuoXEZhOOEPFAsKXpDCA5PSVKs5b6M6kIqIQQWSIvL8nMxm9Cy54wul3SJhSSVpaF8xaTlkhD2kyq0jMq9lTpesOqIzcNtJ1bKbH7RG4XVz96027HKUIom3lsvdqwoeDM_AaSw9ORgAAGe0hRqpvbg9S-eJeey-qq-zQoGeLYF1Q1OYVz5bujnfmmKBAbTStupvO6pphqvyr_AWUU3RMgGB-PyCNKxru2Es0h6gxIVECPZplYa4va-QFP4JlD42wnVZnANBbPCADHeObHbMvIa5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
‏
حدادعادل: والا من خودم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64945" target="_blank">📅 10:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64944">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/eYFJBMT4-uVcCj-HR_kzI0YlzscEBXoyYJxVCEyswM_icTtDRLHs1TAepx-kooITJVaV47PAYczHaUsSrfmVqP8zcZIA4QLigllECR8d4sZqcPMMjSbBPNthWPsh19nZRKIQQNXwAglc2e74tWCw_BKH2tZsTYOIaHKytHSLamvhlouYQe2Obr0L2XsobBb9dmUiY2LXxgv4UxUYhznmxOfj6mvgLviuMbJ9-5c1LAYrTJ_oB9smiRQt4e8EJaQytS60aOQsLCQVJgb9gqQTcIGCe6WgihvTdyI_zY46Nk_WBxYCT298W47fkENga19bF8jE1nmXtXvs1LGo-DjQMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیلی‌میل: کیر میخواد از نخست‌وزیری انگلیس استعفا بده
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/64944" target="_blank">📅 07:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64943">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0s5erLIloHUHfolBKnfhY_mlKQIY3rBg_hLUr5hQs4hlQd_4E3vhc02o-F-kTCHQ-8KmZvlmx9UZwY4RPNoizRzoA6lExz7_Jz9CI5ybPnrV1Yd2LzaIJ5KNxIqEMdZGg0k3pmv-Z-5QEArfW3PGaNka056ZrLC0nJGJj1nej7yjB4AVwk1NS6KlFaLerhBDpqadIieNc1SbK4FcRzcaaUzfq3TZSOoQt3IaaG7lmmJZuSzL5chokvyd490vB5KIzmV_kXsvv8VbMHk10WX5gnyAzmhI7s9Lx_X4aAxYjxhLG4o5dur7JK6LDIyvdqRIl7eFs8le3F1An2k5XNnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در سوشال تروث: «این آرامشِ پیش از طوفان بود»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64943" target="_blank">📅 00:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64942">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مثل اینکه شمال کشور زلزله‌ی نسبتاً شدیدی اومده، مراقب پس‌لرزه هاش باشید
❤️
‌
#hjAly</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/64942" target="_blank">📅 20:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64940">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JerYi-Cldl_H4IxXyg_IY-dPimfEVV4MDZONFHSbrXuq8BDLMINIbd0Uk_ZIsJ97t5WMbwgEDkTLtEf9NmriMYRZ7BnnNh5al4vylQ2OLEBv1VHtoQf7e2ydnRzl_WZATm5cRjbWLzgALvk5pfb60SGptWUXve5cxwV1KeTkIQuIX-Nf9kShTYS84BqmhREwp9Fohhzbqh8tU09Cyl7Su5f1k9G9MDaOtReALTomhYBPfvXu3YVYPfKFC4pgx-LdCzRFWtsyJiCFKMwwyBhT8k2w-TM9x7EEimINa-LSu2duSIuwSSrOdWLWUggZ6s-mK-_HaClrgvivuQUsJuLsUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست ترامپ در تروث‌سوشال:
بازی نداریم! تماشا کن قراره بعدش تو موضع مورد علاقت چه اتفاقی رخ میده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/64939" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64938">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64938" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64936">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XZ7y-7f_lQpDX7SlRwz6JkpmMk5fu1XdxrGQKSFrNm6YeBKNsMO--POkSpyHEhRtrs_2LPC1NurbmnLrhbUUIkg16RpjiITwxS0sSoOd7Z9MJywOWoLLT9Nr-L0rVG_sroZ1Wg6WMf5eEmW5_nCpN7aq5eRgA01-rcN0FskRr-58R8-JoeywrUCRjNICL0AeT8SkEP3Go6RgGZZ9vMwWnFzSFV41okMZlEL2IKQ--DOuAhonA_NySE4xGeSisva8zVgSxV1JJQQFE_Uab2VPl-_-3YXTOurrw3Swi9joZCX6sFMJxOpbjaKGMNJuFyct5tJYNuENvq2zRvMIHc7sjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bq4yfpcV-35kOA0dMROMJ-HxTq-shGqFbvnsnT3YGl9Q-hrD2dZD_7f9eT75hokn9JN-wmCglwjmFS-oo4Ah1Q7NfQXNNlQT2_AeFd-5UfI-CWZyh-Cm6AnPYI9mOfF6AfgC30Z51LQyogPEVVUMbzXasO-HzELiyDSn-oiBFi5H0Tdm5w8f45jARPbh5ORPoOsrm6dFAdF9EUh8XxhGstC7VORPYfKHV56Z1U08wSIrvXTBMSQbldZIV7kYY2IFkuzD_EFdi1Et8FZl4LhLtgjPcP8ALNtSvWSxZnEv4yL_FdPMu5cpWjJRC_SjXT3ob78cE4rg9yz66NI5FlLSJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیکتاتور‌ها مثل هم رفتار می‌کنند
دیکتاتور ها مثل هم سقوط می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64936" target="_blank">📅 10:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64935">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل گزارش داد که در اسرائیل برآورد می‌شود دونالد ترامپ در ۲۴ ساعت آینده درباره اقدام نظامی علیه جمهوری اسلامی تصمیم بگیرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64935" target="_blank">📅 10:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64934">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">عه امروز واقعاً روز پسره؟ روزمون مبارک
🕺
#hjAly
‌</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64934" target="_blank">📅 10:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64933">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbEjmQkCNSDTpQL9pyzuAWJ3AO7k_khD1VqoO_ugqjdUWbgTaeV2BJzO9lGWyHVwDvRf8JeRQAlEi5FBz-BSA0nAIJuODcNEJC0UYaAIvTd7xKXDAmUh_bV0VL1xjNlEWGSdTtuFXla4-4zA68i4vt3waDKed0bCYHehVh2GZt_7p91EB1R2aDhskC41BdUvez2A9y9K_naQiUNkPnfgCOvy52mBBwz7FLLvKGp9sc8gYRQmgjENImTPE9EcSZSinPt0TrltxSwOziLEvOMlP5dLfkT464rYCqxfPCJOvqgn5qLcTkM4HUI-Oe75LHcKUR3gx-oCW1JB5HL5Sn3kTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزالدین حداد، رئیس شاخه نظامی حماس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/64933" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64932">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=Zf4RdtiwVHNvuj_0cYs5KlRpFz3i1SU67IhhGW2nPp3NL23sEaxuQ_NWp5srxoB6RP_7tWI6--4raaw4S885KQMwR24t_GUq7enyOWQ7Ty61YPnRocPB2o6puNFA8sNlsq-847QK8fo7ikzlrkYiPnJufP3ZStoG276wGpNPSvmZFb22Qqgk6HgpSbg6sbzM7h7bVZnEmyZ68N4bjv6sWfvu4Yiyf1nEu4x7apUdppCI6x4y2xFdj42WOOQoq1mfkTOjU9L0g_l6bz5nO8mmIaR7cZZmK3EK0drcE-9owJNdE9pNy9A2fzzMsgY0QXDwxbqc4I0nHhucZ7PoIR6SGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=Zf4RdtiwVHNvuj_0cYs5KlRpFz3i1SU67IhhGW2nPp3NL23sEaxuQ_NWp5srxoB6RP_7tWI6--4raaw4S885KQMwR24t_GUq7enyOWQ7Ty61YPnRocPB2o6puNFA8sNlsq-847QK8fo7ikzlrkYiPnJufP3ZStoG276wGpNPSvmZFb22Qqgk6HgpSbg6sbzM7h7bVZnEmyZ68N4bjv6sWfvu4Yiyf1nEu4x7apUdppCI6x4y2xFdj42WOOQoq1mfkTOjU9L0g_l6bz5nO8mmIaR7cZZmK3EK0drcE-9owJNdE9pNy9A2fzzMsgY0QXDwxbqc4I0nHhucZ7PoIR6SGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/64932" target="_blank">📅 20:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64931">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
📱
👑
آی‌پی های جدید برای فیلترشکن شیر و خورشید
🛜
‌ ‌ ‌ همراه اول
2.22.250.149
23.58.193.140</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/64931" target="_blank">📅 19:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64929">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">همه‌ی اعضاء هیأت آمریکایی قبل از اینکه سوار «ایر فورس وان» بشن و پکن رو ترک کنن، هر چی که از میزبان‌های چینی گرفته بودن [هدیه و یادگاری]، همش رو همون‌جا انداختن تو سطل زباله.
دلیل این کار احتمال جاسوسی بوده
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/64929" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64928">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8NwD2_1Jhmdny3E6dxTOF-eL4o45ERicoMhelpY34OR9RpIx60ZKsZQd49-qD8Lx_iNR2eoCpmNESOypjAR7qvHCqEZ61cooWdYj2ZQifcWFCiw8GYB8ue2tm3Lbe3O5byqFSDtH2nSUZ6TP_JT3wR4uXVg9NDGx-pnWwuz2hr-GSWGhwfecHMh_LOHlGjZTlgEPHIU1IYQsIFAcL6JyQsyCYkRp5dGU2CvRZfnbIz29xUoaoNnotUyeHwIeOaKfdHGMET77ywM9UI5nEXGHXtjwc50l9_fK2csWuljpaTRxT6i1_Ras8fYHNUbToUm5VcP_A8-ICLXG4SBOV2Mzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/64928" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64927">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: تعلیق ۲۰ ساله‌ی غنی‌سازی باید یک تعهد واقعی باشد  @News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64927" target="_blank">📅 14:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64926">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم  @News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64926" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64925">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم
؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64925" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64924">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تنها هدف حاکمیت فعلی، رسیدن به اولین شرط هست و بقیه شرط بیشتر نمایشی هستند برای بستن دهان طرفداران، چون به خوبی ‌می‌دونند که ترامپ، اوباما نیست و تا زمان انجام توافق، قرار نیست تحریمی لغو شه یا اموال بلوک شده آزاد شه!  منتها ترامپ به خوبی برنامه‌ی جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64924" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64923">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
ایران از چند روز پیش منتظر پاسخ آمریکا به این پیشنهاد پنج‌بندی بوده، طراحان این پنج‌بند فرماندهان سپاه از جمله جعفر عزیزی با مدیریت احمد وحیدی و تایید مجتبی خامنه‌ای بودند، طبق گزارش خبرنگار ارشد الجزیره، تمامی این پنج بند توسط آمریکا رد شده!  جزئیات پیشنهاد…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64923" target="_blank">📅 13:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64921">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ogPLDVegPwDWOIXiYrYAD_EfOoT23Yh8CzDgTms1uHemTr85scoIQwLxDny1MFpX8Ua7Ae7_Odt12Jl_wiJHO_jWwKWJOGvtInPBsr-FGkPzSXtdXKc1-MKnINvGCLmkyU0HzNf8Gu2pKODH1gbGmhMLDmy07WoEIWs0RhHBzyHVLXqEPDUPPuMNq3gP4ECBx0CbeJYNWis0SPlb_sz2v1PQjWtGR20fmVCAgF9E4lzUTJiWnE_6CB6iMf7QiljQuDVgvgEnvggiD2QG_F27h1VoQxNTFAluCGEQnU48L8wVckpV07BhI7o6RHSDGyw1FyTiyWhCzLN3y9EF8gFmpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AsPEckekfNGGpq1XC-26FqXX8RLGmlzFT8_vUbGfnUYTIc7TsGGotJUlO4s3F3pRYfLZ7ipZEgU9UCzvvhp8e7fQiO67iDS9sBd4DUMcoCEZqwxi7cJRySxECJqr36NipSEiQh3OVI4iFRMGRh-PGqXWQ6Gw7twxg6YMlvglp0k-NOB-MJRDKSagJAQD72jhNI2b5nsw4kMXF_B_EFNz-m5v_kFVfVJx6h1cYa5It7oyj5AbhhtIDf6AfWyWl6ViXtweF0EenIJvtyDjvaD9qleDJN0oITWEoa666Iu8oYpVsLSY_Jcukn51-JnKCQ0k92UIZCbLK5oB4Fvk1jvO_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ الجزیره: پنج بند ایرانی ها توسط ترامپ بطور کامل رد شده‌اند، مجتبی خامنه‌ای دستور داده بود در صورت رد این پنج بند، دیگر وارد مذاکرات نشوند  @News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64921" target="_blank">📅 13:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64920">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUt5SeJPR3JCW_2i3b2UCKhfdqbQmGuH3q5OC-bJQ_g06grQEVm47sViZQwbjfRiwWLoTx20PxMMZl1aqoU426pFRqVrBMkQ_DoRLm3N1rnw2Ce2WptDiGdqRe67HDYFEBqoyjp7Csz84WEDYyYtB_Phf5QF8Jsq6vAiSooKzhlsbNb4yUVr6_4Ok9kh4Ju_SZsTDpm7zBXjc3eCLRhlTsBpFK_8v0rfaD5G0bKU3GscGuuglKbcPYFt5q9CQKm680SXJlS6DpIdhXGvMFblElSexYN2XABn4J85Im8mP6jwE_KOvpb9rQVHyzfxtXxfD4IDooW0FTstDUm6hhfHxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#فوری؛ علی‌هاشم خبرنگار ارشد الجزیره: یک منبع آگاه ایرانی به من گفت که تهران رسماً پاسخ آمریکا به پیشنهاد ایران را دریافت کرده است و واشنگتن شرایط ایران را به طور کامل رد کرده است  تیم مذاکره‌کننده ایران پنج شرط را که باید قبل از ورود به مذاکرات در مورد…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64920" target="_blank">📅 13:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64919">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇺🇸
ترامپ:  امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند. می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت. هر کاری…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/64919" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64918">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🇮🇷
عراقچی: پیام‌های متناقض آمریکایی‌ها مهم‌ترین مشکل است، هیچ راه‌حل نظامی‌ای وجود ندارد و فکر می‌کنم ایالات متحده باید این واقعیت را درک کند. آن‌ها دست‌کم دو بار ما را آزموده‌اند و اکنون به این نتیجه رسیده‌اند که راه‌حل نظامی وجود ندارد!
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64918" target="_blank">📅 12:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64917">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/64917" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64916">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICPT-r90ow7asfYl_-NwZXpsOdwJlgtf1kHsyRHjrAvmLdxVcCGCwQflVx_hlaPoMpmPkFxUbdG6krMTXGOQQYCjPuc_VjrPo_wU5xai9niqGZlvKTJkxCYLO8YVGSgrFKLX2kpxpUmtXasT3OhaBcWLncSUJnIkmOd00WekTuHPWIXSmdPw9WqlmY6sjQp4Kcz5dGJF78w_m37YpjWfP283dKnHaRxv08KolCr9zi-P2KEpTE6zl6K8UQzFvg8xocQ0ar6Gb_JUe-rS7R8oVYwNprZQOkfz8sroGBP3NuSOauGcw4bBUBDyx_y_QHZ1v0YPiyBmzY2uhzEH8jnNiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/64916" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64915">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=GuDjhdDztRtfbw6wNJ6dv4ND1jxyjSfyYYqzRTHXneGUiyq0UkaTTc8Ghy4_Iws83XzwcJiF0aQAlvzImscG-TM-bQWrfdq9CHvhWbXSXE9O3z-W3ohWlSnn6A6sqbSz7ynBy58G1g7G_mfJrk-0FRfpVBQaWnbcT1IWGVDyyZyEUkiD7x9kCP2SLJHS98mx3jEJL8sd60itbdK3iHrHD1uic6-wNrvVqaWlZKVK8RWnfkYxVzDVgXf8e_pGAVMrHJds6wgN-tc37zZh1gEc8UlXa1gfAJ4wsFty0bdrkhmT5ssW8UDDD4K-lMjwTnFVVVmEctln0lIg7c_4gKpB8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=GuDjhdDztRtfbw6wNJ6dv4ND1jxyjSfyYYqzRTHXneGUiyq0UkaTTc8Ghy4_Iws83XzwcJiF0aQAlvzImscG-TM-bQWrfdq9CHvhWbXSXE9O3z-W3ohWlSnn6A6sqbSz7ynBy58G1g7G_mfJrk-0FRfpVBQaWnbcT1IWGVDyyZyEUkiD7x9kCP2SLJHS98mx3jEJL8sd60itbdK3iHrHD1uic6-wNrvVqaWlZKVK8RWnfkYxVzDVgXf8e_pGAVMrHJds6wgN-tc37zZh1gEc8UlXa1gfAJ4wsFty0bdrkhmT5ssW8UDDD4K-lMjwTnFVVVmEctln0lIg7c_4gKpB8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
📰
کان نیوز:اسرائیل معتقد است که ترامپ پس از بازگشت از سفر چین برای از سرگیری عملیات نظامی علیه ایران تصمیم خواهد گرفت.  مقامات ارشد ارتش اسرائیل و فرماندهی مرکزی آمریکا (CENTCOM) در هفته گذشته درباره احتمال از سرگیری عملیات علیه ایران گفتگو کرده‌اند. بحث‌ها…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64914" target="_blank">📅 10:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64913">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/mk3J_afxBSj0VoidDtAadEfMkKaljWewjOxNiskBPYRrzKlrq2eBnUej98UwgLboOQRUdU_SlpXgiYJt_0-ouOhyWJmzvWgZ8_jQ0Bbnp5QbYnQV-OZUHjhqlnD_Z3nYrWld7gHfkFBe5kj1Se1mG2fOj8Jo3DJEOASEBvJ_UuM__ZZWxZzINzSh0yIW-UM8u_88WSPCaH2wbeoFkMSIsK_HLYidn5VtjSpTO5fb-XBQvazu2ydil7GkljR1oA12QgTKkqMCdAHQsCyQkhPVyzqX2EoGvdWUYY4ZaVDj5Q4rRF5MAzIenEoEmkfdVAhepHVYiY-TE60SBJDkN4UIuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5l4tkCHIPrlx5VOJ_29FR0iGUSodWlpM0tX4ol-laJSDJqIviLROqSma9JvbLtHShiWyRdOTXUmGrHZ87GVTByYvAMd3k4LkYP1JmuATYMaGYayv1wFbeqvm3QM_cEp0eKag1WAoZCken2-bwhhx2Q3jXod0LTDV6a4TkA5Wj9T-O1aItPfXuZdqk5kx62EM8mE_2SqbVLPYQynSDPKkul40CcKx8Oe_fqQDPNKabuOhbH34_fitophGY5lRdvVW6dDwGIkz7Lt-UlGAo0-CmRSqsAbw3VtKAv0-xD3GeMUBH7__jKy_ZJgS6XwdggMUNvJESWfd3iXC8lq23e_0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی؛ نماینده‌ی مجلس:
دولت قصد داره میزان سهمیه ماهانه بنزین ۱۵۰۰ تومنی و ۳۰۰۰ تومنی رو کاهش بده و قیمت بنزین ۵۰۰۰ تومنی رو هم به ۲۰۰۰۰ تومن برسونه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64912" target="_blank">📅 19:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64911">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=UWP0FoZsw2PM30LT10wvqTmikGC57coMKcxaxFiNWnVhQpNPNhO-vIyM-4F0Y02vQXIf3CMMqWZDrI8ME3evJVI5vIG_30uyy7s54XIy5xSrWXvxFWPCZ7wBDeCL1JpHOUEz2luO7tm5Gh82x0aWhhTV6kh6N3BIqLdTrtUJWzu_LKY92bxenWz81ry6nUfxmRgTut25gkmc2LPzs5YabUXNPLVutbSsEKGy1fOC2Z1bd_cw-6s8uaPXQhECibQzFQt80GOcqkGBmTAlbo4DSLLvWl1D5xc9sruClMm0Hp5O2OT1y6SHtjbTUAxCAgXfZg42_yoSJdZQJHLhvzhy6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=UWP0FoZsw2PM30LT10wvqTmikGC57coMKcxaxFiNWnVhQpNPNhO-vIyM-4F0Y02vQXIf3CMMqWZDrI8ME3evJVI5vIG_30uyy7s54XIy5xSrWXvxFWPCZ7wBDeCL1JpHOUEz2luO7tm5Gh82x0aWhhTV6kh6N3BIqLdTrtUJWzu_LKY92bxenWz81ry6nUfxmRgTut25gkmc2LPzs5YabUXNPLVutbSsEKGy1fOC2Z1bd_cw-6s8uaPXQhECibQzFQt80GOcqkGBmTAlbo4DSLLvWl1D5xc9sruClMm0Hp5O2OT1y6SHtjbTUAxCAgXfZg42_yoSJdZQJHLhvzhy6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ی دست دادن ترامپ و شی
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64911" target="_blank">📅 13:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64910">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZArirYkaPxx1cJlqq7ilAbDL-gTHuwcyJTSfs2IhIhhFYle9a8SKhTwfFeldb7RtGoWtBf0W1ZnvcM08Fmt2kJWz4X5LTbPlRbZrBD6SliCTmEqTpCDgKkyG3t__n4j6CtKXyBisFu2etPGJqneJ_Oer4Qd1glA7r4CJM7AJSmBPGIpS2mjB3gf2-OZ8mOSdfFkal0LIVgcKMcqQ6a0QpOZjqEH0BhXm9bb3M61gU_APUDqYYGqIgZgJeOfcR3BSKdz3wrlVWmY3XhV7S04KwFyRflnvvgsJZ826i9v3mbrBAQI0-c_Ze5hYmgh4zrUV63_up_qMrxJTq59qYW5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64910" target="_blank">📅 02:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64909">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64909" target="_blank">📅 02:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64908">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGmO-VOFJ8x0ik59Qgjv9n2W6sPsducjxNDtSgq364TNpKxmIM8s21w_Pz0XAs3EWjFOBWyHsSV8qKGrhvZfwv-3n4gmsxv-DYlEniwGFHJ7lcxU3zmbZoIkUQ-j4P_3Ec-fUtG2hMOEoqMozgOLw5eflgnQ30Em3RRwmunOj7O34gUZC5wT9sXYIunEUlUsG1CU4KzsscEt9ji8AGn6-k0ByxzEGWe0dmcalbKl1MkQKozK3VDtfRpYmpc1LP30RL2jnxs7KFKz_Ifb_AsyN5liw_izsg8msXbu9nXXTluER3scElDQL3ZDDWOqIGnAIW8iigE9ZooRd_MkDbK7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ixTm9sB6B4ZkxA6DkL4DMPOTJmYyJ9Gyrgw8BiFpTb0zE2pxXTZhTipUU1eKXEKRW-UFgxY0POHIYLcmbwAAVUqVOhCoddxIncM1zRhAuIebW2Fp8utg1tqLXz8CNYyyCwRKquugEyNn7IvynhSsWHivnHbqxLUVHT_sjL2vS0C6rueg9_OAo5hBg1gZeHWiVUgqFHaZfPKFYqI-DsRMUn_Om-x4q0o5rMiP3RQUj4UtXg6pjPTKJik2qt3uzeFtg3FGHAlYRJbVBE64nR8xNX0Ddgzecyc2U0oPmHdW03abtMbDiaXstI2BafwcyBq9al0FMi0decyu-5BgXpDjXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=Evbi1w6dtgCdhYrz77eUqxcSZx1SAlvOig6IWqvXkxGhCsJhbar5pYqnKOJtKmq62RIVUKccWBHazJzhIbzKSroXHGdL__zi61lZS8U8-iWJH0eddEp_pv-2GAO7XfvnPhPCDRAnYgapGE2Laj1GT1uncsyGs9ij52oFJd_bbCARRknr6HL3CUVBJJlbqK7XEqXv5Xkw-LrCQi2fXn3tkz4GcHz0r5Z7qqbo8gUKqD00jUL5P9bqBaObienPJdupPbNi6R-9u3LPIJAydnd0pDrk1pC4yWF098TXuewOzrbQ7lH0iooYbMPSdhGUUuKA_7q6jYUTBMVqUoxHplph-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=Evbi1w6dtgCdhYrz77eUqxcSZx1SAlvOig6IWqvXkxGhCsJhbar5pYqnKOJtKmq62RIVUKccWBHazJzhIbzKSroXHGdL__zi61lZS8U8-iWJH0eddEp_pv-2GAO7XfvnPhPCDRAnYgapGE2Laj1GT1uncsyGs9ij52oFJd_bbCARRknr6HL3CUVBJJlbqK7XEqXv5Xkw-LrCQi2fXn3tkz4GcHz0r5Z7qqbo8gUKqD00jUL5P9bqBaObienPJdupPbNi6R-9u3LPIJAydnd0pDrk1pC4yWF098TXuewOzrbQ7lH0iooYbMPSdhGUUuKA_7q6jYUTBMVqUoxHplph-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم تو خیابو‌نا و پارک‌های اطراف پردیس بعد از زلزله و پس‌لرزه‌های دیشب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PUp22P6iB-k_9KQfELsTzfo5qKndo-8l2BIPdvL4CdavJcMMW4MZY2PLxseG29dN7oJSmvc6V1D5TWuV3ZfKaAmMzglC3OVZUJMWsVlPfsT_cgavzxHPjFdSnlpl4LTwnPGeE4uAH--B2053I0KIPPRILXrvCGFZJVvV6BT4jvl08E4yppl_e11EHDwQyOvcq0C0QMIDbXyHwOKBR6nVZUt_0jHwQqIlgUflMA08g2Q8Sw9T8ciLxjDT8eB2jH8RjXDFv9_wZxbZKeASoiLF3grSTL7Rt0NjX-dTUVxOqaRowU6YST6z3KdSyxU5lYig1Az0AlgcwuNXSJ0GYDQAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NrJD96lhV_6PBFwGHc-JDF9vGOmdGkMML69D9PIGqdNoU0varOH7jOJiaj041PqdeiRsPcXo_PSGGJFNv_WSUxlai7AT9toacPttv3TEQm_yl4VgCGbHtHVR1x04tbeZj5RcgcS9kSdy2AhIiMd9SNTc8O-PaGuUgFnBH_lmUbosIojH2tHJzsbUpkWQ_gKHrx9Fb5bebPNBfsPrdq5dtAki13DM2XnnI2ZJmtPE3mug4Wzg68pZTNiX7xMpomcjYYtd3BtCsFgykYVF2yUE6VFukpoz2WS7udz9IwBmRiSClrxFtVrFE4WC3fP5Qu8xoDi31a_uVFhALK1stDZBow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64899">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QxEGGeIEAsOFieRkadCtT4o3URP8L-AycUWsp7E5dx64H2wgLyRpSG5pqkr9uNIaTiWkwa6FusMR32Azv0s-LFiuc0ooe1vRsZLMusqnZckYUKjvt4RTCzATO9Ot8qMOzjMW-odasJzilxy_hqcV38k0Di1PRbntsBOigifyqwM6xPuQ72hIOluSHt9RbHPyiaqGQEx-atva9r8sv_uSC8OvrgonJM254GW_NasCtvSiR5grqO9RbS_fV04862SPmCEa7rYtQ-2u9Hhl8gQp6wb_xJU81WdQQShPtGucH_J8hw0V4ccZVRwFm3_mAvb6UrpsHHxO9RbSH9_NgILZag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vGNgOXPJQwKO43EX1ai8aPBrOkbhLqypX5QuCsZgRczzgUlbIsiAGECq0bseskZt5vhG2wIPonMDbLylzBsRICxQfVZ_6giPoFdGGkXHwnsiP4qm5k6cWzSsraI70accYEq1mA14QUmvtXUR9P39tu1mdH_WeLPEIxDaMp9HucVNYT_SQl8JNwbrty57arbJRfYUwX_2pLRYd5gVAw9XdaZsGLNidErqI9NYS4uReQt6A9uX0D3bHNyZuJAmwn-vhBxkYgpe1TwnqxEYGVjeBeBXA2jwZWkZnWyTLxvo2JlkskKsJfuzC7eRgGBWOKvtguZwWQUFDYLqxNQc6l45DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکوروبیو داخل «ایر فورس وان» دقیقا لباسی رو پوشیده که مادورو پوشیده بود
هنوز نرسیده ترول رو شروع کردن :)
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vR2Azm1gj7yrKULnLTV-eBtgrkdzLPmUWolNk6M_jbXeGm8xykojjxS5vQao3ebkuoTHo2kf4brJN43NSeGPGwlNOhDnn5AVaYRQzAKxIPtzCaRca_C2d0E34ALwNhJ0s1-JU2SYs9Mv4lMbHcOJ7EZjlyfbNs_jl2Lfm6jTin0HVA-hJlUZTxwJ4tljiCU0dcAVw7yQoagfwTHLzYW9eWbFEoJa-PwJfh9-z_9o7IXMXT-a2uGWlCdA0s-m9a1wPNe5rQPlNz92889g8K5GWLCx0JGKc37uZUpI7RZCrEscGoO55C_tD89Cs6IZ1-woTIfrEm2546CV_psKV4rsgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JFGax6-NgU1ZI8htT9skgnb8MToIozUy4AqxcfprkRq5hpiWv3uAXeNK7GD51jXO0JQ_JzPPDOG-Avb_LPktENY8iVlOueyEQk4KKfvRR1VhRV45QHp7NB_GKtG9TWPnvMekm7y1Ff1KInPrFoAPKbiojuqNAdJm3Sg0uwTauilmPZyQ_Fz3M9G4EBk6D0JggJYTCgwao_oBA4jtGZsQ8_ZH8688J8SQRw3gwcgAvFJwYmfFtqUjjP7yhu5kB6gdVMar3FtWKQuTbIG1uLZT97uSsBF6yfhpJDaZAUaHOHWijnlhvZpjymAoWs-oBkfN8pJ6g4BaXp-oqlPOgSYADQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=ZrZFKTd3wXktGDcSjWRuu6r1EXoUUDGcnpBMb0K4XRMqSrv3nibmI9sLiBDfaPe69l0iMwBiFMvyKDUwKQd5T2TUqBh6mYPFSFkaO1b_5OTMuTBpbNOqvao2THDlrZA2_qRvWyRr163VT6DrCwYy6LWB6rb2xzBkovq5TikoygAIdYH0nUVYLPguej4JG-FRXROybIGY1FlMOcjCupPd7eUj_hY2agCPiWVIAzL9wgHzeQc9C_Yeqk5bTvApXc9KbFRR0Btq9ipYkb_o-Adjhng9J15HhySAQlaXXCdNPiW4MDy-bY3s2ux3bipPWyElR1Um9BKFXeWv3BJ2v7saqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=ZrZFKTd3wXktGDcSjWRuu6r1EXoUUDGcnpBMb0K4XRMqSrv3nibmI9sLiBDfaPe69l0iMwBiFMvyKDUwKQd5T2TUqBh6mYPFSFkaO1b_5OTMuTBpbNOqvao2THDlrZA2_qRvWyRr163VT6DrCwYy6LWB6rb2xzBkovq5TikoygAIdYH0nUVYLPguej4JG-FRXROybIGY1FlMOcjCupPd7eUj_hY2agCPiWVIAzL9wgHzeQc9C_Yeqk5bTvApXc9KbFRR0Btq9ipYkb_o-Adjhng9J15HhySAQlaXXCdNPiW4MDy-bY3s2ux3bipPWyElR1Um9BKFXeWv3BJ2v7saqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFU5iLnWSPeHeXj7-Or8nuqty6l_lOaDg9W3Wp0awXo-1CjMZhnQmVUsK729AKJFruCNuUe82kyxdaoegbjN0Voq-tYIuNVB57PS6yJQEHRqv1NNCwTHVgb4vo0ddf0GRjTuZsgHI6iu4c7ZjemGVMOSpg6mRPo_F1v9ziK8la5iRnVI5ZFrN_1FM1FckzHFHIgsgx6HckexVkWqVrKx1nY9lHtgGffCOQiaC9DMKW1ChLAgDDwyO04Ih_Ux0aii65qSUc8BCOl67nuwwD-3ouL1izgqrtVtCiNcuw_ZbMNWEMyVG3y4YZTF5cJGN5ZLXGpafTG4PT68_Ibd3IZOiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EAUkhMvWJuVlpnLhgheeyH-WA_VecbyYPs__a8ZzqZAopySHkFoZmbDVomZP05WzyK1ox8kiOrUhHTax9IWoV9e3UdKTnc8i_W85xsWsBhGkzyiYKpi4srgADThNd6gxZ6H4ekAJl8YsRSAzJFgbVzm7011vlkdXZlPO4AJDrozIb-ZlbAGERDGmLdLlWqUhd1AlBH5KFJx9CvuEx4kOsQ86k8HALGEjcOGLbf-v8y-AH5CVaxpY36sq8kkqkU2KiCK4WrzZtFWvQCbrSxGHOixol0UlOYtOAANZNRzn3zDWVEIo8rtYHKDDO1uvOP_TrXrQnT0VPNoBRLKdIPmRWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-TVhBwPT584jmYksNLQ1P4boPhvtIbsXv2YhZjf5OGXvwyyrD1rMfIWxZXVTIjdsISHzy7HvhwkG0_4I88LTAJtyn5R7gFkqW3BKnEsnE2jUgxNalkgp-FjMMP0BC7ZJUUwfcoeaR7XhjtRPuL6ApzdDmRDJHspGQ3hko_ikmcq2FUFuUwYVNP0VbfoVGaI69Oz_PLMUk7vItX1mpDyMzHNQ_d6t8ekjkVeG-ruje1bpi4xSDLiPZuhGiidh7oJm2bjvZyNXdGi_bNzXN41P397mI1TOUTjHmgsf2HqmxBpnk7EhIDcNlAf5rr6EfEbBCIMRDgv4AK2YrreEE8NYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64891">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=XgaDvHXe-V2C5udXMNyh8bpbOrArV6bmqzvcReWRoqiX2mmE-Vik7X1c9KG9ghlA9qXyf9lzzfsqZI2SJ8_lAUdc7gtrs2Me_tOlA-1zgXYJcntAwJzL-WmwH7hv8TjCoUUb3wjaJuaAiciqO4VOqvsQRYCGUl_rH0jUuo6oRhiYikpD2X3teXn3z8ywQZzWCw33EkTIiwIhwHzGX8bidZmBUPso5-g4yvjJRi1P3_UVlmOKw_JcbOADcjVFGlTKmsoRlAEIWJFqEDZCA6JHI3EOUwojSmYx8FmYyV6IShW6SSxM08l5bhFuAytwlkJIQx7FyVChRDIYbBIijdZlQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=XgaDvHXe-V2C5udXMNyh8bpbOrArV6bmqzvcReWRoqiX2mmE-Vik7X1c9KG9ghlA9qXyf9lzzfsqZI2SJ8_lAUdc7gtrs2Me_tOlA-1zgXYJcntAwJzL-WmwH7hv8TjCoUUb3wjaJuaAiciqO4VOqvsQRYCGUl_rH0jUuo6oRhiYikpD2X3teXn3z8ywQZzWCw33EkTIiwIhwHzGX8bidZmBUPso5-g4yvjJRi1P3_UVlmOKw_JcbOADcjVFGlTKmsoRlAEIWJFqEDZCA6JHI3EOUwojSmYx8FmYyV6IShW6SSxM08l5bhFuAytwlkJIQx7FyVChRDIYbBIijdZlQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ملانیا بهم  گفته باید رفتارت رو درست کنی تو دیگه رئیس جمهوری پس از کلمات رکیک و فوش استفاده نکن. من هم همین کار رو می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64890">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=ZF1twdz0KTE6CTDnh2cI6lWAQ4hyB0iyEJrOeRCrgs421FyJA2lUeG1yyGG6PpPtfm-vEy5tLCw8wVxXu3CX-J6BaHEh15Qt2fZptZ2I6qo8eZUviV8MKQQUsfl7snnys3e5mQnBMFsdYgOaaLIgD19XfLKCCPTOBJs8Io3uuzEnEUYrUWHmRzUB69uFDQAYWVfjNgHuzt6Mn6suqWnymKr1W-HZHtmoWvtkZMt0TYKBIpSPu14Dw25QqZeXASwcd_Xisni6sGzYroGMsJz09s2-gOz4WTKnYBnSgujsFCvj4dyGxqZK36rv0ynFNEtWKZ6g_wJTs1-a7mn4cgKcww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=ZF1twdz0KTE6CTDnh2cI6lWAQ4hyB0iyEJrOeRCrgs421FyJA2lUeG1yyGG6PpPtfm-vEy5tLCw8wVxXu3CX-J6BaHEh15Qt2fZptZ2I6qo8eZUviV8MKQQUsfl7snnys3e5mQnBMFsdYgOaaLIgD19XfLKCCPTOBJs8Io3uuzEnEUYrUWHmRzUB69uFDQAYWVfjNgHuzt6Mn6suqWnymKr1W-HZHtmoWvtkZMt0TYKBIpSPu14Dw25QqZeXASwcd_Xisni6sGzYroGMsJz09s2-gOz4WTKnYBnSgujsFCvj4dyGxqZK36rv0ynFNEtWKZ6g_wJTs1-a7mn4cgKcww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره نماینده حزب جمهوری خواهان تو انتخابات ریاست جمهوری آینده امریکا:
کیا جی‌دی ونس رو دوست دارن؟ کیا مارکو روبیو رو؟
به نظر ترکیب خوبی میان، من معتقدم که این یه تیم رویاییه. فکر می‌کنم کاندیدای ریاست جمهوری و کاندیدای معاونت ریاست جمهوری آینده باشند
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVjffJCkNAmMfAtJwTM4ZzDE6K3eR6VX2Vr5ZP6b0257JSNl56lUyOGnwoCIYXnHoPjnvSyS6zKBJ19lWk1E-VbzHJEUUh57Bxn20Bb5XHdGcwnYhtVLMSeJKN7eu8f1uSF187pCfhFbKJhZG1GN7vZZgvgsF2gRAwdc_8WFBtZz-XK9rXeI5seb7FbhpsSl9cvXeynaSNlAyjFFBffzM7UkECpQEzWLDX4g4BppBCxQM73DvWRlcvBo2NCkRz9PB6nRyAfzKr5JtkNKuI0BlR93yaXkK08z_C5pz43d95KaBhwNJorh9CChEEbuoW-rSLxlHL-RrfxJUBkA8KO-2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/vwjnyHYl_iLq9AjUX95N2PvpkKwVZniyAtpjYyUvsWmxJIrrLT_t6O954IXdH5GHOOx4w0WAKMVhTlgw2ROeMoeKcoLtBGnNYD5L9XghASlruL4mhYy0edUHn-h00_yHWsOjLwkNj925deO3zo5TiSTcBmjwtQvoSIQX9E9S7z43l0a4MK-WcMhAm2IUL2BDQ7eCN-Sr9bV0j1EK6GoRYd69BymUNVgcYywSIltGIWhThKwskc3h-3fw2uyeWm1s4sdIteiCns-0eQSwqbV-5jIjux-8PD7Xmj99qUjb5YiQlon5cWeIiVUR0iEoWggNgwsN1l9OvyE1g-WxWL2KvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/news_hut/64885" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64884">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64882">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
