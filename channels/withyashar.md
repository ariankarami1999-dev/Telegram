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
<img src="https://cdn4.telesco.pe/file/SX3EEjUqyRk0XgPufYLRM0eIJ7yH0Jn2SVJiQkGetc7ixWVP1_DdnyoMoxP4Ctk9apbB1F-fbCqefpHDA80371W-9NKi_zLXXQuiaPgBQhBMQtbjA8z_30Bao8ifhoM1Dc7JwjvBlV-20BL_VZbjeY54JvvrEECnqApiql1eKYtGBiLZfvN8UBZr6OT1GqjHqLuN6RsZB56XESAAMx5UPKnJHY_QD0n4mispqbDvJ7yup2Z_ZIze5l2VrgEVgNDrXvNoxXIA7XBOYh73Zc1p-AoxQvNxFQDUbpFY7x7NKmPLGgee9A0OCmFlhzsEhwol4VmJEKUP1qREjzMSN4wFGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 436K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 01:04:36</div>
<hr>

<div class="tg-post" id="msg-20194">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خبرنگار شبکه i24 news: همزمان با انتشار گزارش‌هایی درباره آماده‌سازی برای حمله به اهداف مرتبط با بخش انرژی در ایران، یک منبع آگاه از این گفت‌وگوها به من گفته است: «رئیس‌جمهور دیگر صبرش را از دست داده است. این حمله می‌تواند رژیم را در آسیب‌پذیرترین نقطه‌اش هدف قرار دهد. تصمیم نهایی در آخرین لحظه گرفته خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/withyashar/20194" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20193">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اتاق جنگ با یاشار : تیک تاک ، تیک تاک ، تیک تاک
بینگ ، بینگ ، بینگ ، بینگ
@WarRoom</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/withyashar/20193" target="_blank">📅 01:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20192">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وال استریت ژورنال:ترامپ در جلسه امروز تیم امنیت ملی خود در کمپ دیوید ، دستور حمله نظامی جدید آمریکا به ایران را صادر کرده است @WarRoom</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/withyashar/20192" target="_blank">📅 00:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20190">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سی بی اس :  آمریکا و اسرائیل در حال آماده‌سازی برای سخت‌ترین حملات بمبارانی علیه زیرساخت‌های انرژی ایران هستند ، حملات ممکن است از همین الان (آخر هفته) شروع شود اهداف شامل نیروگاه‌ها و پالایشگاه‌هاست اما ترامپ هنوز دستور نهایی صادر نکرده ، اسرائیل با آمریکا…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/withyashar/20190" target="_blank">📅 00:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20189">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سی بی اس :  آمریکا و اسرائیل در حال آماده‌سازی برای سخت‌ترین حملات بمبارانی علیه زیرساخت‌های انرژی ایران هستند ، حملات ممکن است از همین الان (آخر هفته) شروع شود اهداف شامل نیروگاه‌ها و پالایشگاه‌هاست اما ترامپ هنوز دستور نهایی صادر نکرده ، اسرائیل با آمریکا هماهنگ است اما مقام اسرائیلی می‌گوید از تصمیم قطعی مطلع نیست همچنین بحث‌هایی درباره پایان قبل از باز شدن بازار دوشنبه وجود دارد،این طرح در جلسه کابینه کمپ دیوید مطرح شد و برخی دستیاران کاخ سفید مخالفند اما پنتاگون اعلام آمادگی کامل کرده همچنین بحث قطع برق تهران هم مطرح شد!
@WarRoom</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/withyashar/20189" target="_blank">📅 00:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20188">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گزارش تایید نشده صدای انفجار اطراف اهواز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/withyashar/20188" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20187">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اسپانیا: مهاجرین غیرقانونی به مال ها حمله کردن و در حال غارت کردن فروشگا های لوکس هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/20187" target="_blank">📅 00:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20186">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سنتکام : از زمان ازسرگیری محاصره بنادر ایران، مسیر ۳۰ کشتی را تغییر داده و مانع حرکت دو کشتی شده‌ایم
@WarRoom</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/20186" target="_blank">📅 00:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20185">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مجری : در مورد ایران، آیا ایده‌ای دارید - یک ماه، یک سال؟ چقدر طول می‌کشد تا آنچه اتفاق می‌افتد حل شود؟  ترامپ: همیشه سخت است. ما ونزوئلا را در کمتر از یک روز حل کردیم. @WarRoom</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/20185" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20184">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXqA1Rx1upO7aFgQJaNGIvhfAzasWdubC45-H7qn0RaA4F-beEcMF32Eezy-LLM5WnUtJYyAsPEsj5OY79eFPlXTqkSneXd2Oos0aYIaV45_C7yNOPm9T6vV5SKq5no64B38mlDyrSsrWRWT_GoKe2ytfubLukfCiLexUCj45EYq2ux2xpF-em99JCTMS29R6BYgAT7wf3QE0asKRWQLl9YUGasxYpIPQcECde6J4mUwc_r6GsFC-03nOFMSmmigA_O61x4lwHiTDo0BDEicOC5g3WpX954eumC3KDD-aiK2owaDyDfeoD_wA45NOzoxhlXgxt3hll9y2te7BcJHfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان اسکله پل بندرعباس
ارسال مهمات و تجهیزات به قشم
@WarRoom</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/20184" target="_blank">📅 00:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20183">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گزارش صدای انفجار غرب بندر عباس @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/20183" target="_blank">📅 00:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20182">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb09e50276.mp4?token=liXCuo-Rp0OxV-jo2QrecG6IdKP8f757qheW68B4hhP0a-MlF-b9mEY7lkUdd21GQpmYcgmQ6OsRH2_nImyczQ1sc_SkPK2haaQRoFrkW1i1nMnG7xe4pqreRHoC2xizmjZXSp5-n5H-rLfHs5yY2z_1RLIbm183kRsS9mETaEjoJzQUI2P9YossMVJtlbgkTCf-BMKGriJQ6TcrVaTD7xMRMYD_NhopRR5BUMh1Gwn5MpfCW377783mHc4uFO10bSCxEX6iB3CZEYGUWUaLL1GZjys8nfFq1CFpyGWqcwqNAjTtE8rJoRNJAUXGc1RQYU7ygSj99a9vvvEDRlAxDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb09e50276.mp4?token=liXCuo-Rp0OxV-jo2QrecG6IdKP8f757qheW68B4hhP0a-MlF-b9mEY7lkUdd21GQpmYcgmQ6OsRH2_nImyczQ1sc_SkPK2haaQRoFrkW1i1nMnG7xe4pqreRHoC2xizmjZXSp5-n5H-rLfHs5yY2z_1RLIbm183kRsS9mETaEjoJzQUI2P9YossMVJtlbgkTCf-BMKGriJQ6TcrVaTD7xMRMYD_NhopRR5BUMh1Gwn5MpfCW377783mHc4uFO10bSCxEX6iB3CZEYGUWUaLL1GZjys8nfFq1CFpyGWqcwqNAjTtE8rJoRNJAUXGc1RQYU7ygSj99a9vvvEDRlAxDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری
: در مورد ایران، آیا ایده‌ای دارید - یک ماه، یک سال؟ چقدر طول می‌کشد تا آنچه اتفاق می‌افتد حل شود؟
ترامپ: همیشه سخت است. ما ونزوئلا را در کمتر از یک روز حل کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/20182" target="_blank">📅 00:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20181">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گزارش تایید نشده صدای انفجار از دور در قشم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/20181" target="_blank">📅 00:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20180">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گزارش تایید نشده صدای انفجار سکنج کرمان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/20180" target="_blank">📅 00:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20179">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حوثی های یمن
: ۸ نفتکش سعودی مجبور به تغییر مسیر شدند
@WarRoom</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/20179" target="_blank">📅 00:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20178">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ در مورد ایران:
می‌خواهید همه چیز سریع تمام شود؟
به دیوانه‌ها سلاح هسته‌ای بدهید.
خیلی سریع تمام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/20178" target="_blank">📅 00:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20177">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارش صدای انفجار غرب بندر عباس
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/20177" target="_blank">📅 00:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20176">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8900ed7e3.mp4?token=HRzpO23w-t-2C8IgRuRB6IjWOun9zEROPaw_h7NKKgxfz2T-cx2GtYTYqcyNV_iTpSxgXj2TtLp29kA_VO99pti62MVwYuqWaDnGQMnyV3wq0ttBigeegMZu1-qPJtSU-qCb0qZekr4oUPYdl1Hae3y5RwV3F-UQcq2eTJn0eYz_zbXyX_ryljzd0xMTb0q3BCupEsHOr-TgDOWDDb8mjuvpfnmCh4cBJrJeJKQtUOsRs17w8JtbrwQ3YRYvzEl2eF_4bSpaMpjC-o9u-VdHi03b6kgmRTeLhJDq9Npx9nQZHM4RB2NmX1R6X0p0JV34ftL3FQoAE7Ij4FRkFN_hjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8900ed7e3.mp4?token=HRzpO23w-t-2C8IgRuRB6IjWOun9zEROPaw_h7NKKgxfz2T-cx2GtYTYqcyNV_iTpSxgXj2TtLp29kA_VO99pti62MVwYuqWaDnGQMnyV3wq0ttBigeegMZu1-qPJtSU-qCb0qZekr4oUPYdl1Hae3y5RwV3F-UQcq2eTJn0eYz_zbXyX_ryljzd0xMTb0q3BCupEsHOr-TgDOWDDb8mjuvpfnmCh4cBJrJeJKQtUOsRs17w8JtbrwQ3YRYvzEl2eF_4bSpaMpjC-o9u-VdHi03b6kgmRTeLhJDq9Npx9nQZHM4RB2NmX1R6X0p0JV34ftL3FQoAE7Ij4FRkFN_hjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران
:
من در حال انجام کاری بسیار بزرگ‌تر از چیزی هستم که گفته بودم انجام خواهم داد.قرار بود وارد شویم، توان نظامی آن‌ها را از بین ببریم و بعد خارج شویم.
اما بعد متوجه شدم اگر این کار را انجام دهیم، باید نوعی حضور و نظارت مستمر وجود داشته باشد؛ وگرنه آن‌ها دوباره همه‌چیز را بازسازی خواهند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/20176" target="_blank">📅 00:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20175">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHvjeI_K5O3oM9wat6EC0SkBGLgEnFVvq6r4PykZ2GpfzJeS5dsUhnZB-vvlgc6Tc8tyfxrPmW52qJrSztfM8z8GtYwu_QT05-czKgIsbOqENfhMJq_WR9XfJaDP_cumzsw-4bKu8y_tTysg6eaeidLo3c7xAg8YdRpzTUSEPla003EUD6RyPBEO7nqY0F33uLiy1qeV4KASC_Cazh9wWt57-Hv17Aihg_BPQcYDj8Zkx_PpoRlMn4TVdtvXFnUm6wtG17CZUOd9eAvmryKP9FHHFmomX5mv-yZt2MiQEX2eIYNnxSe7Bpb7Sje0GXP5xf4VJPOSESY8E-keobf-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس تحلیل داده‌های پروازی، دو فروند جنگنده F-35A Lightning II نیروی هوایی ایالات متحده آمریکا با کد دم LN و معرف پروازی TABOR71 و TABOR72 صبح امروز از پایگاه هوایی لیکنهیث (Lakenheath) بریتانیا به سمت خاورمیانه اعزام شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/20175" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20174">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZDV9z0_INlaI2ApQorVCHalnW0jaWis_VkWYqSt3wt88Aalf-64mMSfhkutaHCwRaV5_anRr8ulvd1HBzfAF0oTuBEU6g3f__tTPj8Hu5rXexB40OE3ULudDhHBgo4eL5hYOx6ncyHhKbB4ahwlofocO50vtSR_2NhPRFMMHfb1T5nC0EECb6MjvfGCZeP4YAoU8e6buEce5iNG5s2ZrMtJ428hsnXtFLjUCmMEYXV5z1Fpd0ozunKBWoqLwDTpJl6pM0LIsilyZ9gCbwWfhFv8h1-cnDdLuXkzOysmL1Gx0eaoE5nBpA3OJbQT1Aliv2euwf_Ai5xPdgPl7ydxHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش فعالیت سوخت‌رسانی هوایی آمریکا در خاورمیانه همچنان ادامه دارد؛ طی ۷۲ ساعت گذشته دست‌کم ۱۲۲ سورتی پرواز توسط KC-135 و KC-46 ثبت شده (میانگین روزانه حدود ۴۱ مأموریت) که حداقل ۲۱ مورد آن در خلیج فارس و دریای عمان انجام شده است. این سطح از فعالیت نشان‌دهنده حفظ ریتم عملیاتی بالا و توانایی و آمادگی کامل آمریکا برای اجرای حملات دوربرد، گشت‌های رزمی و عملیات شناسایی بدون اتکای کامل به پایگاه‌های منطقه‌ای است.
@WarRoom</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/20174" target="_blank">📅 23:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20173">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b1ce5038.mp4?token=P6yzLhQxmrPFhVxB5NS9JIPK0q3xJjFIpla7S-K5nfR7JT6dNIGbfKpk_HkoUk8IEy7-SeLZKiBGPjRqmB4YlkAy76SIVvGP_1hAclFPiEi7VeVxHuryoeGdQO_eGhYEubDsDfFBmNvMnaWSSyTJr4g6d0Y3syuq8rdq8LF-RRCuWp-xQvxHH8weCiKvD6niE_KSLFhbfyHx8fRp0TSrtqev3P-NE3gtMMsLS-HY9GoNbluuCTJjp9RwGuCxuW8SVbmjUROc28OTbq_9UmUP5muqtr8cZ4hhy8uHndaEYab2Lcpajz-2PQTjtYXjwUPrEGFf0UYgO5C6_GVWc7tu1nlZ7pbAJMYzKW9kkm9ID44MAZx3ixvXb9IUhF985p1AAdrJHchL4cI4rGlmhNvYQ5f-pZNbEwOFe4cmCjJXXOrNifa6JDfZkynGbP7L8ihHn1lOya-w9fXlk3ZkJR8kiZieLQtDZXIlVzq7SXxRVQ5DLp2d6cTs6ptbPdnC515tU5liZcEaL3SsfQX2fdMxlPeH_mUpBQ0GLm6chk9e4nDdxnR1H0u19nD7dxDPkQ-s4AgDxeB8XCPrmZp7qd0IlRzeNTy1D9X_YLODHQLFbwgkNXfrJBZcX0tl0-NfsCyGW6_IK2PoUCq70PIlAekkoB4eB-vSA2twBy3ViRCupWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b1ce5038.mp4?token=P6yzLhQxmrPFhVxB5NS9JIPK0q3xJjFIpla7S-K5nfR7JT6dNIGbfKpk_HkoUk8IEy7-SeLZKiBGPjRqmB4YlkAy76SIVvGP_1hAclFPiEi7VeVxHuryoeGdQO_eGhYEubDsDfFBmNvMnaWSSyTJr4g6d0Y3syuq8rdq8LF-RRCuWp-xQvxHH8weCiKvD6niE_KSLFhbfyHx8fRp0TSrtqev3P-NE3gtMMsLS-HY9GoNbluuCTJjp9RwGuCxuW8SVbmjUROc28OTbq_9UmUP5muqtr8cZ4hhy8uHndaEYab2Lcpajz-2PQTjtYXjwUPrEGFf0UYgO5C6_GVWc7tu1nlZ7pbAJMYzKW9kkm9ID44MAZx3ixvXb9IUhF985p1AAdrJHchL4cI4rGlmhNvYQ5f-pZNbEwOFe4cmCjJXXOrNifa6JDfZkynGbP7L8ihHn1lOya-w9fXlk3ZkJR8kiZieLQtDZXIlVzq7SXxRVQ5DLp2d6cTs6ptbPdnC515tU5liZcEaL3SsfQX2fdMxlPeH_mUpBQ0GLm6chk9e4nDdxnR1H0u19nD7dxDPkQ-s4AgDxeB8XCPrmZp7qd0IlRzeNTy1D9X_YLODHQLFbwgkNXfrJBZcX0tl0-NfsCyGW6_IK2PoUCq70PIlAekkoB4eB-vSA2twBy3ViRCupWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فروند جنگنده اف-۳۵ با یک حادثه در پایگاه هوایی میرامار نیروی دریایی در سن دیگو، ساعاتی پیش آتش گرفت. تیم‌های امدادی حوالی ساعت ۱۰ صبح به وقت محلی به دلیل دود غلیظ به محل اعزام شدند. علت حادثه در دست بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/20173" target="_blank">📅 23:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20172">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">روزنامه نیویورک پست، به نقل از دو منبع، از جزئیات بیشتر طرح دو هفته ای ژنرال براد کوپر فرمانده سنتکام گزارش داد عملیات بمباران گسترده و طولانی‌مدت علیه ایران تدوین شده است.
این عملیات، یک بمباران مداوم خواهد بود، برخلاف حملات محدود و شبانه‌ای که در دور قبلی درگیری مشاهده می‌شد، و از مهم‌ترین عملیات‌های نظامی از زمان آتش‌بس هشتم آوریل خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/20172" target="_blank">📅 23:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20171">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/20171" target="_blank">📅 22:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20170">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/20170" target="_blank">📅 22:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20169">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20169" target="_blank">📅 22:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20168">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نظرسنجی شبکه 13 اسرائیلی:
62 درصد از شهروندان اسرائیل به توانایی ترامپ در جلوگیری از پیشرفت برنامه هسته‌ای ایران اعتماد ندارند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/20168" target="_blank">📅 22:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20167">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">واشینگتن‌پست: ترامپ نباید به توصیه‌های جی‌دی ونس درباره جمهوری اسلامی عمل کنه.
به نوشته این روزنامه، تهران از مذاکرات برای خرید زمان استفاده میکنه و آمریکا باید فشار نظامی و اقتصادی بر جمهوری اسلامی رو ادامه بده و از ازسرگیری عملیات علیه ایران عقب‌نشینی نکنه.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20167" target="_blank">📅 22:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20166">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_XB_NcTOdwdgN4hCrPxAwmEa4VpmaMrby6HnxY1Z1q-E82zYFdmPJeuccIzsTwnmJoOCPSGOyN6E9aVkP_j2wUmxEV4px4L51Pk7ejjfSFCxaSY8OBELXde30E-7veB9Tft2SrcM2tf_0Ln-a2rBs5LdZqgVt5R-OFa9YoNSd5vlzpNUKFkn7CNWrhl0wf2B5CoD_vCmxHEIuPTb2mL9LTkseeVry0iIUmoI3jiDy4lHv20oCWUIDDJM4b6cSjHENvRVZ82BrAOoRDbaYHxvTSZN9MzxzIS6iIfq6wubF0XpqxZgRadVjaBIieq6VSNITPfs5oP4pbMMeFEnK-s4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس گزارش تحقیقی رویترز منتشر کرده، یک صرافی ارز دیجیتال، به مرکزی برای جابه‌جایی پول‌های غیرقانونی ایران تبدیل شده است.
این صرافی یک شبکه گسترده قمار را که توسط دو اینفلوئنسر سرشناس و بین‌المللی در شبکه‌های اجتماعی اداره می‌شود، به صرافی بایننس و فعالیت‌های استخراج بیت‌کوین و بانک مرکزی ایران مرتبط می‌کند.این شبکه قمار فارسی‌زبان که متشکل از بیش از ۲ هزار وب‌سایت است از جمله توسط
ساشا سبحانی و پویان مختاری
، دو اینفلوئنسر ایرانی تبلیغ و اداره می‌شود که ارتباطاتی در سطوح بالای حکومت ایران دارند. تحقیقات رویترز همچنین نشان داده است که سپاه پاسداران سال‌ها پیش کنترل بزرگ‌ترین وب‌سایت‌های قمار قابل دسترس در ایران را به دست گرفته و از آن زمان تاکنون از این وب‌سایت‌ها برای انتقال حدود چهار میلیارد دلار به خارج از کشور استفاده کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20166" target="_blank">📅 21:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20165">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d306e1b0.mp4?token=XBxMZQjYnz72NllRF2RB-88cCB_GuXyANlMhNd2bNSSBl0OfdORsGQX7V-5TKVfk8iT2vsDp5GRac3pkhv-oTFG_Uu9puEGgjM1PwTM_GNSoPBCfE2ShlIaw-q0HgdUBSuca7V7WR8APH7QQRrv0l_L93SoVww6DESQV9Owe07q13TgJBPZBd5fT26PnsClEZbSuryrwP8g_ECw5GKF6zp-buLfGwe5tw0gLHydktIctqsqAXR4Tc0Zt08v2htlHj70UbFeMzc-MlVGgE4YHAy_MS4foP0II_6vy3VomRNNufUecIcSR04fZ_ClWD8zR_-YS0GCZgI896v-lG_1hrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d306e1b0.mp4?token=XBxMZQjYnz72NllRF2RB-88cCB_GuXyANlMhNd2bNSSBl0OfdORsGQX7V-5TKVfk8iT2vsDp5GRac3pkhv-oTFG_Uu9puEGgjM1PwTM_GNSoPBCfE2ShlIaw-q0HgdUBSuca7V7WR8APH7QQRrv0l_L93SoVww6DESQV9Owe07q13TgJBPZBd5fT26PnsClEZbSuryrwP8g_ECw5GKF6zp-buLfGwe5tw0gLHydktIctqsqAXR4Tc0Zt08v2htlHj70UbFeMzc-MlVGgE4YHAy_MS4foP0II_6vy3VomRNNufUecIcSR04fZ_ClWD8zR_-YS0GCZgI896v-lG_1hrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: میدونید موشک هایی که ایران به سمتمون میندازه رو چطوری رهگیری میکنیم؟! اینطوری: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20165" target="_blank">📅 21:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20164">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1ss9FBARvmx8Yb6WSL04CIwgezlqX4O5HqrhLtDCxksUSIK7n6QSz7vCvDcCOiqpyrOhiWzynCXBPhx525JIzGLB1anLb7LD60gIpBhcnIdyIxtoy6zsU4Rin8QZRLx2DQ1bO309QRH2uZKTv6QeRojhO92Fp2yZIu3GsYa8FGNz9Vf6HnXm6l_Ca9wnDgo5f92UHYHAEVsWXDbcDEUC1x3fYXOQVU6_V3ACrY7KwwtUG8b5xiSUZw5_4pFjejdeQKpSFi3hFoSt8Qy84cgbuPd_Qyu_6N0RxsipU8fGt5kdixkPDcF-XNjopgwf1U0Pmw2L7QeiP2MevRL260IbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای، روز گذشته یک ناو هواپیمابر آمریکایی(بوش یا لینکلن) در ۳۴۰ کیلومتری بندر چابهار ایران مشاهده شده است
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20164" target="_blank">📅 20:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20163">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c77f1bbbfa.mp4?token=mhuvISeL9qOfwc95f_GsOul8YLxo5cdCSBQkxHSSC0ANzwrwBFpUfM4XNPm-zL7c6cIEIogxldpChPIFiaWAUYQdQN5sEX-Su-6t-yt9Dpz21BMKgv8CwmxmSInE7dTbRZN8pxaRP5Y5l6LfRSCmej8rbNDxzbtdtU43Px28vDHJufHVX-bBOqyqRIE5bPVdu1hDuRRRB9hkjsagWqYaqbZzD-R2vbYS2aGHHg6H3Hqsw5FPuCK4hqmcd2e2lD6COGmh6p48M-Orxg1Wj9mqSnGS7NAG5IblL7D7FZXM3Wms5_mNqSWPQfzsvjPcvBkj-_IN2qwcs93F-ss5RaBKXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c77f1bbbfa.mp4?token=mhuvISeL9qOfwc95f_GsOul8YLxo5cdCSBQkxHSSC0ANzwrwBFpUfM4XNPm-zL7c6cIEIogxldpChPIFiaWAUYQdQN5sEX-Su-6t-yt9Dpz21BMKgv8CwmxmSInE7dTbRZN8pxaRP5Y5l6LfRSCmej8rbNDxzbtdtU43Px28vDHJufHVX-bBOqyqRIE5bPVdu1hDuRRRB9hkjsagWqYaqbZzD-R2vbYS2aGHHg6H3Hqsw5FPuCK4hqmcd2e2lD6COGmh6p48M-Orxg1Wj9mqSnGS7NAG5IblL7D7FZXM3Wms5_mNqSWPQfzsvjPcvBkj-_IN2qwcs93F-ss5RaBKXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفتید ایران هنوز برخی از توانایی‌های خود را حفظ کرده است. آیا آمریکایی‌ها باید برای این حملات پی در پی آماده باشند تا زمانی که ایران به سادگی قادر به حمله متقابل نباشد؟
ترامپ: آنها کمی قوی‌تر خواهند شد، شاید الان، اما ضعیف‌تر خواهند شد.بله، مطمئناً. شما همیشه باید هوشیار باشید.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20163" target="_blank">📅 20:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20162">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f7a15aa5.mp4?token=Qd4mey8CSg2Ua2ZxlosbflR0b0LlkqdUlbxWUgHqO3kM3GQ46Il-HHQnCDbO-R4AdopSOtiHgc-QtDlSuWYrN1rhoG-1MaAmah8D9JYb5FLZ-zmt6H-zXQflqHVsNN-0RoYl4b3VuEUSWw7ZRRixAq6sZeo4hxCDT_kUV_TewYuhwROYzMsbfJrqnyxXmlDqOW3GJ5VDS1_ZmoWhv6Mnyanre4iAWzA7G3GzhCvqZEfnZYXTolL6B0MhmUEuCL1eA5UrLfWb9VXFbm_0ZdDJfjfV6Mxs_fDcYyI_9uVInmBgNTEyUFbFfHL5UZXOGs3IWJHNuIQz3xeCHMbtiU1SBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f7a15aa5.mp4?token=Qd4mey8CSg2Ua2ZxlosbflR0b0LlkqdUlbxWUgHqO3kM3GQ46Il-HHQnCDbO-R4AdopSOtiHgc-QtDlSuWYrN1rhoG-1MaAmah8D9JYb5FLZ-zmt6H-zXQflqHVsNN-0RoYl4b3VuEUSWw7ZRRixAq6sZeo4hxCDT_kUV_TewYuhwROYzMsbfJrqnyxXmlDqOW3GJ5VDS1_ZmoWhv6Mnyanre4iAWzA7G3GzhCvqZEfnZYXTolL6B0MhmUEuCL1eA5UrLfWb9VXFbm_0ZdDJfjfV6Mxs_fDcYyI_9uVInmBgNTEyUFbFfHL5UZXOGs3IWJHNuIQz3xeCHMbtiU1SBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره ایران:
رادار؟ «رفته.» رهبرانشون؟ «رفته‌اند.»
و بعد جمع‌بندی نهایی: «همه‌چیز رفته.»
همه‌چیز... رفته. همه‌اش... رفته. رفته که رفته!
آخر هم با یک بالا انداختن شانه گفت: «البته، باز هم به جنگیدن ادامه می‌دهند.»
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20162" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20161">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f38497106.mp4?token=hBc04Z_0tCTobK_VUsv_IH9OQLMemjKKmWt6bOEUZqHgdOhEgCpJG291iAR1ndvbCvemWw7W-mArt_8nAk5HEfLt7fjSM08rn6hmjIOSrliKxjALVm0XsJIo1VQC2yo0Ab3uwXaC0g7QnYx9EeJh1DzI2fYcxkLkpAlzYcnVDP3athw7LkUmFi2JUwuM9xj7ZRsYpLTFPr5w19GIxnlqyCuBOvtzzUBYDM-WXz__Q4Hr9deQLke1Fd2h2eS3A1ll1WZtA6qQ15Ha4jBkEDKzhF0UCYyugbWwLnmllMHjBa7U_qaJXlLeHmAWxic_cDUwEo8Wvl3qMG6VEJggsPif4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f38497106.mp4?token=hBc04Z_0tCTobK_VUsv_IH9OQLMemjKKmWt6bOEUZqHgdOhEgCpJG291iAR1ndvbCvemWw7W-mArt_8nAk5HEfLt7fjSM08rn6hmjIOSrliKxjALVm0XsJIo1VQC2yo0Ab3uwXaC0g7QnYx9EeJh1DzI2fYcxkLkpAlzYcnVDP3athw7LkUmFi2JUwuM9xj7ZRsYpLTFPr5w19GIxnlqyCuBOvtzzUBYDM-WXz__Q4Hr9deQLke1Fd2h2eS3A1ll1WZtA6qQ15Ha4jBkEDKzhF0UCYyugbWwLnmllMHjBa7U_qaJXlLeHmAWxic_cDUwEo8Wvl3qMG6VEJggsPif4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: سنتکام گفته حملات اخیر برای کم کردن توان ایران در مختل کردن تردد کشتی‌ها در تنگه هرمز بوده. به نظرتون چند حمله دیگه لازمه تا به این هدف برسید؟
ترامپ: «هیچ‌وقت نمی‌شه دقیق گفت.
بیشتر کشورها تا الان تسلیم شده بودن.
ایران هنوز تسلیم نشده و بابت همین باید بهشون اعتبار داد.
اونا همیشه به سرسخت بودن معروف بودن؛ واقعاً هم سرسختن.»
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/20161" target="_blank">📅 20:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20160">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ: موشک تاماهاک باورنکردنی‌ترین است - می‌توانید از یک درگاه عبور کنید، آن را از پنجره یک خانه عبور دهید.
هیچ‌کس چیزی شبیه به آن ندیده است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/20160" target="_blank">📅 20:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20159">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ
: اگرچه نیروی دریایی، نیروی هوایی و پدافند هوایی ایران تا حد زیادی از کار افتاده و تنها توانمندی‌های ناچیزی برای آن‌ها باقی مانده، اما تلاش‌ها برای تضعیف بیشتر این توان باقی‌مانده همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/20159" target="_blank">📅 20:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20158">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حقیقت یاب سنتکام : سپاه دروغ میگه !تنگه هرمز همچنان برای عبور کشتی‌های تجاری باز است. ایران آن را کنترل نمی‌کند. هزاران کشتی طی چهار ماه گذشته از این آبراه بین‌المللی عبور کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/20158" target="_blank">📅 20:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20157">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8367cad8.mp4?token=rYqLIbwe126Yl-2dHMsDTntDzmW_RLxPnPgO3jv_AvoyZkSV5Csa5g0JZ9X88veafRZfVGGVUxOQgM7UEkcAf5ft7ckjMj5P7E7TTGDFUiMpiehcFfHoFld8377ak90iNfphiBcUGA0Beh9nCR14V2MJMPRR8MrGH6mC4Vy1k5Iub7dzVmznOvZfQtqTPboSLWoOkgGB7UtZoXfpUgByoZVWiVGTgHKUUdr5Hd511jGu5NORNUhNQ2ys1MIflpqZ60YYROqZ-cji0RWUWUJZSMjrAaxZKB1QTQSEsUEN-wIhonzcbu6l6dvgtkY3DiiCigS0HHSLcoV5VxwLl_xTupHfS5LoSvrzAUz5UfukGDcFdI9BNUp1JP8l5LsKX_bIpI8OYywU7TG1cG5fqM757UwraamTLOWuMeCfTcPZSBhBRKO8JwMfdxUa8dSUYG-SvwADGwzMgVDg7ZH9Uk_zylwrF6PT6vZPARK3LftAfQDOe99M4G6d0QmQNjo94E13jit4rClu20IxIs4zHBj02QCbDmV4HJE2zemkLL6rhyluUBbxuwvv3X0OfhkKtSclXeHR-_GDry2GiTaNFV9vG_fq43WDznBT6vd23V9bq86iC_qQtmM-goWS4LL0HJhzd2dUuEk9EDVSmzVRTlZs82IHZDAynXsnv8RGEGRMlAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8367cad8.mp4?token=rYqLIbwe126Yl-2dHMsDTntDzmW_RLxPnPgO3jv_AvoyZkSV5Csa5g0JZ9X88veafRZfVGGVUxOQgM7UEkcAf5ft7ckjMj5P7E7TTGDFUiMpiehcFfHoFld8377ak90iNfphiBcUGA0Beh9nCR14V2MJMPRR8MrGH6mC4Vy1k5Iub7dzVmznOvZfQtqTPboSLWoOkgGB7UtZoXfpUgByoZVWiVGTgHKUUdr5Hd511jGu5NORNUhNQ2ys1MIflpqZ60YYROqZ-cji0RWUWUJZSMjrAaxZKB1QTQSEsUEN-wIhonzcbu6l6dvgtkY3DiiCigS0HHSLcoV5VxwLl_xTupHfS5LoSvrzAUz5UfukGDcFdI9BNUp1JP8l5LsKX_bIpI8OYywU7TG1cG5fqM757UwraamTLOWuMeCfTcPZSBhBRKO8JwMfdxUa8dSUYG-SvwADGwzMgVDg7ZH9Uk_zylwrF6PT6vZPARK3LftAfQDOe99M4G6d0QmQNjo94E13jit4rClu20IxIs4zHBj02QCbDmV4HJE2zemkLL6rhyluUBbxuwvv3X0OfhkKtSclXeHR-_GDry2GiTaNFV9vG_fq43WDznBT6vd23V9bq86iC_qQtmM-goWS4LL0HJhzd2dUuEk9EDVSmzVRTlZs82IHZDAynXsnv8RGEGRMlAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: چه کسی از دولت با ایران صحبت می‌کند؟
ترامپ: آن‌ها همیشه می‌خواهند صحبت کنند... استیو، جرد، جی‌دی و مارکو درگیر هستند.
گزارشگر: ایران می‌گوید مذاکراتی در حال انجام نیست
ترامپ: ممکن است مدت طولانی درباره هسته‌ای صحبت کنیم و سپس آن‌ها بیرون بروند و بگویند: «ما هرگز درباره هسته‌ای صحبت نکردیم...» آن‌ها فقط کاری می‌کنند که عصبانی شوم
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20157" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20156">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ درباره ایران : آنها هفت ساعت درباره موضوع هسته‌ای صحبت می‌کنند. من می‌گویم: چرا هفت ساعت؟ این کار را می‌شود در پنج تا ده دقیقه انجام داد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20156" target="_blank">📅 20:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20155">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ درباره ایران:ما می‌توانیم به توافقی با ایران برسیم، اما من به تدریج اعتمادم را به آن‌ها از دست می‌دهم، زیرا آن‌ها دروغ می‌گویند
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20155" target="_blank">📅 20:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20154">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اتاق جنگ با یاشار : طبق روال تمامی جمعه‌ها از هشت ماه پیش تا کنون، امشب بیداریم و نوشیدنیهای الکلی و غیرالکلی را نوش جان خواهیم کرد.
امروز بیشتر خاص است چون ورود ششمین ماه میلادی شروع جنگ هم است
@WarRoom
💥</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20154" target="_blank">📅 17:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20153">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وزیر خزانۀ آمریکا به فاکس نیوز: محاصره‌ی نظامی و اقتصادی ایران متوقف نخواهد شد و ما در سراسر جهان به دنبال اموال ایران خواهیم رفت.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20153" target="_blank">📅 17:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20152">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ به فاکس نیوز: ایران در نهایت چاره ای جز تسلیم نخواهد داشت‌‌  اتفاقی راجع به ایران قرار است بیوفتد @WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20152" target="_blank">📅 17:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20151">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ به فاکس نیوز: ایران در نهایت چاره ای جز تسلیم نخواهد داشت‌‌
اتفاقی راجع به ایران قرار است بیوفتد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20151" target="_blank">📅 17:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20150">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ در مورد اتفاقات اسپانیا:
واقعاً افتضاحه، ببینید وقتی آدم نادرستی به قدرت برسه چجوری یه کشور رو نابود میکنه. این تصاویر رو بخاطر بسپارید، اگر دموکرات‌ها دوباره به قدرت برسن همین بلا سر آمریکا هم میاد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20150" target="_blank">📅 16:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20149">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ امروز در بحبوحه تشدید تنش‌ها و ادامه جنگ با ایران، جلسه کابینه خود را در کمپ دیوید برگزار میکند. به گزارش رویترز، در این جلسه علاوه بر مسائل سیاست خارجی و جنگ با ایران، پیامدهای اقتصادی درگیری‌ها، به‌ویژه افزایش قیمت بنزین و نگرانی‌های سیاسی جمهوری‌خواهان…</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20149" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20148">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حماس در بیانیه‌ای اعلام کرد با مرحله دوم چارچوب آتش‌بس موافق است، اما تأکید کرد که فقط سلاح‌های سنگین (مانند راکت‌ها و موشک‌های ضدتانک) را تحویل خواهد داد؛ آن هم مشروط به خروج کامل اسرائیل از غزه، تشکیل کشور مستقل فلسطین، بازسازی غزه و پایان همه اشکال تجاوز.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20148" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20147">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDsMhJ3IezPubE3mVigpn-hgYS4mem9oODdRIxEAS187b3tqCOCmlpkopCqq3ZvIQS0fJnd4Q64ecO6NSkLWVAy7CGCBKgGMkJLdCNgpoVizT4wuoM98HhYogswre2UG-6ALnNekjXbi6uTEcdNGDLR88tjyfO2BI-t3R9jG7rRLn9s3x7lul9t6KFZvoMplpqPieVjhKEm7VunlDBNCH6g3-GiYpm8b3oQZBaPNb0wFk52VFjjr_-NzsnVK0yGzRz4NUGlME8SodQAGXavfSoaaCGUi7BY0FwmaRc28zM6SydlqToh1xPWCjwJOqjOtReb0wZ_8n4w-l85tq_-rMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر سند محرمانه افشا شده از تعداد واقعی ثبت نام کنندگان در پویش جانفدا  که 8,311,811 نفر بوده و حدود 2 میلیون نفرشون نظامی و حدود 6 میلیون نفرشون بالای ۵۰ سال و ۸۸۵هزار نفر زیر ۱۲ سال دارند !
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20147" target="_blank">📅 15:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20146">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ امروز در بحبوحه تشدید تنش‌ها و ادامه جنگ با ایران، جلسه کابینه خود را در کمپ دیوید برگزار میکند.
به گزارش رویترز، در این جلسه علاوه بر مسائل سیاست خارجی و جنگ با ایران، پیامدهای اقتصادی درگیری‌ها، به‌ویژه افزایش قیمت بنزین و نگرانی‌های سیاسی جمهوری‌خواهان پیش از انتخابات میان‌دوره‌ای آمریکا، مورد توجه قرار گرفته است. این سیزدهمین جلسه کابینه ترامپ در دوره دوم ریاست‌جمهوری اوست.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20146" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20145">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وزیر دفاع اسرائیل ، یسرائیل کاتس برای بار هزارم : اگر ترامپ از ما بخواهد، به حمله به ايران ملحق خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20145" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20144">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کويت: از بامداد امروز هدف حملات پهپادی ایران قرار گرفته‌ایم , خسارات فقط مادی بوده
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20144" target="_blank">📅 14:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20143">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwcYkq3Ro-NwtwFW_AT6Tolc-DwT70Jw8wXvSc3IrDf0lci4IywiVPI-TzafX50ZUGBWfIa6fctAMJDBJMbxXhC_QI_2J0vYSb-k7SD6jW8qAizyU7i1u1xoNBFw8SpBahKFpNqk5rOn7Ffk4q1X2JN1SkR3dZ2E3-gg6HbssMwbKvm_0wVOA6_Q9ZH-LHtEZ_yxRZ0kYZtZQAzXD-UJjtpiG1YiQPwu0rCxrCAXMclzr1fsUA_P0u0KH2jnLT3AhQcKZ_depmmv4qoDTUiTG7IwirGgac_sXIsM6aBKfeZmxVISW17J_4CI1qE3lf4qZceJzn7qwh4HB9g4F8nRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون تنگه‌هرمز یکی از کشتی های هدف قرار گرفته توسط سپاه
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20143" target="_blank">📅 14:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20142">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd52784122.mp4?token=nlqOmACVsxq3-ZDI9GYS3aMMUP4-YPqx6PSGOYcGe5o8BWEmVGnHx2EDBojepPYiBj7XavgnFruGG3uF50vXWpb03dtjZ6Ps6gUj3CQeRzEMmUSJJi-lacbw1Pqi_MMkcGRdJO5z-ONN78hAOPdKhkfVmkvm_x6VhkRr8-aFqKkXLTzyPaEwg5741wUannT4UajkMXfnLEF1iqw-TwmqJCFoebVVY9bwx-tIZEySOzN-H5sLt4k54eEYNVh7Oni9diWU1EpJsOaeMAB0V4xFgLUvbjPrtNswT6cVALangkf0Sy7Ng0iIuTy10ObHA4paU5f2sLMmv_hLSSUzeoZpqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd52784122.mp4?token=nlqOmACVsxq3-ZDI9GYS3aMMUP4-YPqx6PSGOYcGe5o8BWEmVGnHx2EDBojepPYiBj7XavgnFruGG3uF50vXWpb03dtjZ6Ps6gUj3CQeRzEMmUSJJi-lacbw1Pqi_MMkcGRdJO5z-ONN78hAOPdKhkfVmkvm_x6VhkRr8-aFqKkXLTzyPaEwg5741wUannT4UajkMXfnLEF1iqw-TwmqJCFoebVVY9bwx-tIZEySOzN-H5sLt4k54eEYNVh7Oni9diWU1EpJsOaeMAB0V4xFgLUvbjPrtNswT6cVALangkf0Sy7Ng0iIuTy10ObHA4paU5f2sLMmv_hLSSUzeoZpqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی آتش‌نشانی تهران: دود مشاهده شده در آسمان شرق تهران، مربوط به حریق ضایعات و فضای سبز در محدوده جاجرود است
حریق در دره است و آتش‌نشانان در حال اطفای آن هستند.
@WarRoom
یاشار : چیزی نیست بی بی داره آشغالارو آنیش میزنه تو دره دید نداشته باشه</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20142" target="_blank">📅 13:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20141">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085ee0b373.mp4?token=SSJ-AZ-JtkwAUudEHRwVr9yriI0A1VbueKI7WU0LrdVk5LCQEnaux84wbTOjnazdLH3q2mODTLBrEM3fRo5606jBGOOaaFFT_KZvLzaR6JImhAb7wYeL0ZWygIQVFnVXYXvoEsBUFl0irvOXJ-50qUfRujh3tK1kYVdPYNmgNYWCF7ZIIXqlCBLDMUMlWlhOvYRxgI3K-urMCn4t5mIthjBxX8BF3LLPEjFCeBMCmoqMkdqQVJUa94M2pRuia0jF8ren7vKRxj4fH-9IjZv_ugZSCWpM4pdgMOylVxiUOFPTg35j9YYozOrvumQhlpDRrfV9BKExJR1J2da0LlbqiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085ee0b373.mp4?token=SSJ-AZ-JtkwAUudEHRwVr9yriI0A1VbueKI7WU0LrdVk5LCQEnaux84wbTOjnazdLH3q2mODTLBrEM3fRo5606jBGOOaaFFT_KZvLzaR6JImhAb7wYeL0ZWygIQVFnVXYXvoEsBUFl0irvOXJ-50qUfRujh3tK1kYVdPYNmgNYWCF7ZIIXqlCBLDMUMlWlhOvYRxgI3K-urMCn4t5mIthjBxX8BF3LLPEjFCeBMCmoqMkdqQVJUa94M2pRuia0jF8ren7vKRxj4fH-9IjZv_ugZSCWpM4pdgMOylVxiUOFPTg35j9YYozOrvumQhlpDRrfV9BKExJR1J2da0LlbqiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون تهران ستون دود بزرگ سیاه و غلیظ در پشت سد لتیان
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20141" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20140">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">به گزارش تلگراف،
آمریکا و اسرائیل در حال بررسی گزینه‌ای جدید برای افزایش فشار بر ایران هستند که شامل «محاصره زمینی»
پس از ماه‌ها حملات و محاصره دریایی در تضعیف تهران است؛ این طرح بر اعمال فشار به همسایگان ایران از جمله عراق، پاکستان، ترکیه و افغانستان برای بستن یا محدودسازی گذرگاه‌های مرزی و قطع جریان واردات و صادرات تمرکز دارد، به‌طوری‌که به گفته یک مقام اسرائیلی هدف آن است که ایران عملاً از تبادل کالا محروم شود، با این حال ژنرال بازنشسته آمریکایی شان مک‌فارلند این سناریو را «تقریباً غیرممکن» توصیف کرده هرچند معتقد است در صورت اجرا می‌تواند فشار اقتصادی شدیدی وارد کند، ضمن اینکه احتمال دارد طرح مذکور بیشتر جنبه انحرافی داشته باشد تا توجه ایران را از اقدامات واقعی بعدی منحرف کند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20140" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20139">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1VxMN45SsEPaa_ttIO1xzxsBgDVVvIVtWDNlqXBrMhKnCVVC3wGY5Pm__mA5CrIDXGS392BSSyINfFG2Qgn3hFJCcBHl8s8Rdo6HHXo_I4sjHp5W8L9wkc3_BzUQGlX3aUWHaT1w47Muu0EyfeHvtc7Cbhp4ffdeoPjzOXQMshzffeJkLaEsQeidG-toTGz651iUZvWKpo9eX6FlACAQsTbLN5ZbtxlAGCnJhTbXxs6D7ldY34VDAKTMTdj6M2MuuQzE1XS51JLo13zTpfz2wnQpzWlMqEwz8qUgInlhZjfX5JMdtZTWZE-R8M_oThQM6KOkyLtjYkWZYbGH95B_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانکر سوخت‌رسان KC-135R نیروی هوایی آمریکا با شماره 8017-63 پس از ماه‌ها سکوت، دوباره فعال شد. این هواپیما در پی برخورد مرگبار مارس ۲۰۲۶ بر فراز مرز عراق با تانکر 0347-60 با شناسه «ZEUS70» آسیب دیده بود.8017-63 که با کال‌ساین «RCH169» وارد منطقه شده و پس از فرود اضطراری در تل‌آویو (LLBG) زمین‌گیر شده بود، اکنون با شناسه جدید «RCH564» سیگنال داده و در فرودگاه بن‌گوریون فعال شده
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20139" target="_blank">📅 13:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20138">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeetJjc3wTMXNaBH9kuTyWZo6d_1PXntZQX3OUoUc1sJdCFydiB68yCDawCdV-9dcfxBa6vWrBs77cD7Pijg7y5f0OHA4q8G3b3AYHwFPpyAfZjUcbCrL4qBap-gDfEVIC812QejKx_ky41y8W5pteycfMgAG5eKMTawbxAxI9KCTzeuf5UaXmaOU4MKLobeN9z7k9Qho0_TFkhMePPGPQgMTvjM5cDfVzAjIl4eovptui94NLGvi_2lqAAm36MCH0w7H0BfDRW_BWKYxztSm6IdstQp3X3sAf-U9JDF9T826qkGoZfZGvAQsJ8A_NGd8FxukTPo8EaYDUyp9O5c9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اعلیحضرت شاهنشاه محمدرضا پهلوی و انور سادات، رئیس جمهور وقت مصر، هنگام تماشای یک  مانور نظامی در تاریخ 28 تیر 1355 در منطقه علی آباد قم.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20138" target="_blank">📅 13:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20137">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارش صدای انفجار در تنگه هرمز @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20137" target="_blank">📅 12:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20136">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حماس بیانیه گروه بین‌المللی صلح غزه رو تأیید و اعلام کرد اسلحه‌ش رو تحویل می‌ده.
این یک شکست بزرگ دیگه برای رژیم در آستانه‌ی دور بعدی حملات تمام‌عیار آمریکا و اسرائیل علیه ج.ا در خاک ایران محسوب می‌شه.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20136" target="_blank">📅 12:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20135">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/054d20c537.mp4?token=ZNv3wqEzfk1Bk0tTr5hQ1xHU3EJFDaEN47gDdyR77yqPWwNoos9DHpp4_VGohhv4fA2aNCwoQUmqyIGh5Z7d97yDHAYUlzhZ1Bp8BrEhuuCWsVwXJsIA0dUAy9eJRhG0lat0SSTr74BjCwBH2eQ_oIIvSgot3-6XEgOIAyE2nlMcQLGjxcKluWTuZWBg-bidrEOdbfE6bhjKRhz5NS2s29NGJIgx6NgSsYHu5z-2Pbt-rbk8h7oRYIaojoADPazzpJYphOUi_jWF5niJ6ob3Hs0CJdHHijl4dF9ygYKasNufSEgrwoTrzrfIK89-1IEzK9D6sFSXqrTFOGiIlpXgADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/054d20c537.mp4?token=ZNv3wqEzfk1Bk0tTr5hQ1xHU3EJFDaEN47gDdyR77yqPWwNoos9DHpp4_VGohhv4fA2aNCwoQUmqyIGh5Z7d97yDHAYUlzhZ1Bp8BrEhuuCWsVwXJsIA0dUAy9eJRhG0lat0SSTr74BjCwBH2eQ_oIIvSgot3-6XEgOIAyE2nlMcQLGjxcKluWTuZWBg-bidrEOdbfE6bhjKRhz5NS2s29NGJIgx6NgSsYHu5z-2Pbt-rbk8h7oRYIaojoADPazzpJYphOUi_jWF5niJ6ob3Hs0CJdHHijl4dF9ygYKasNufSEgrwoTrzrfIK89-1IEzK9D6sFSXqrTFOGiIlpXgADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال بدل خامنه‌ای از زائران مراسم تشییع جنازه خامنه‌ای (فکر کنم بیکار شده اومده آبدارچی شده)
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20135" target="_blank">📅 12:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20134">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9xEzYpsmP2VzIBctLDVxavEdLe6CgD928_3zKV-iabbocCseV-Ubnmz9OqXEk-aQd_Igun7CzZI1U5vG4wQ5OBX9zB69E7BIbhIgMWxbGsqWvvQ7dIiKALu4zgoIrMMMm0GlNqZ3xAavluQLMvIAfd1JWtvCQRx5Ol0uLq4bZOiERHEGxAOe1-CPsSNySsfo1ik-0C1v6VMw5aMJlOtPtuQUTfVEF_pItreGSan9vajhSbE69rIHo6E-FnVXViNkQX80nl9STcMEdm0MI3YJL7c9WM4AgXSR9MjmVSH0CSwcCB4j3NdnRmcQEuRGda8tNzXDCKU4qc4wW9PEUmhsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزه ۱۵ میلیون دلاری جدید وزارت خارجه آمریکا برای اطلاعات درباره شبکه مالی سپاه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20134" target="_blank">📅 12:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20132">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گزارش صدای انفجار در تنگه هرمز
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20132" target="_blank">📅 12:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20131">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کانال ۱۴ اسرائیل: رسانه‌های دولتی ایران به‌نقل از یک مقام ارشد گزارش داده‌اند که «با اطمینان صددرصد» حملهٔ قریب‌الوقوع آمریکا به منطقهٔ کوه پیک‌اکس در راه است.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20131" target="_blank">📅 12:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20130">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">باراک راوید، آکسیوس: به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم تشییع جنازه علی خامنه‌ای، رهبر سابق ایران، به این کشور سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکند و وقت‌کشی کند
یک مقام ارشد آمریکایی ادعا کرد که ایران سعی کرده حماس را متقاعد کند که توافق‌نامه را امضا نکند، اما این گروه ترجیح داده به حرف آنها گوش ندهد
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20130" target="_blank">📅 11:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20129">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce43f3e25d.mp4?token=kivogwuKX4VhWFbAAS8YBCR1blTr51Jbo8u3x5QX8G3skTqO44CJKz82k6ce--kzNa59KIset1eNDt022UwQtkLS7vCoUTNyRekXx12GUwvysM3PLRLon5icuD6vcpIs5HFPcLmgPZX87SmUmoyegy2jGBDgpdUvv0r4nior52b4s0b-sLQx5vGS8UntFgEtRbLx_JTNNJpS7gax8eR4cEMYU4g4ADuvRKwG6tVZnWxviPIm3Uf7rEQ0Ba22BLIArXqQykY5H63jqm9vQUgC-fu7WTPY3g-xgVBsOZFD4i9qgnH5ebm1dGBLWAGn2ofBKzqrtPFTojAN3kIqauI29g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce43f3e25d.mp4?token=kivogwuKX4VhWFbAAS8YBCR1blTr51Jbo8u3x5QX8G3skTqO44CJKz82k6ce--kzNa59KIset1eNDt022UwQtkLS7vCoUTNyRekXx12GUwvysM3PLRLon5icuD6vcpIs5HFPcLmgPZX87SmUmoyegy2jGBDgpdUvv0r4nior52b4s0b-sLQx5vGS8UntFgEtRbLx_JTNNJpS7gax8eR4cEMYU4g4ADuvRKwG6tVZnWxviPIm3Uf7rEQ0Ba22BLIArXqQykY5H63jqm9vQUgC-fu7WTPY3g-xgVBsOZFD4i9qgnH5ebm1dGBLWAGn2ofBKzqrtPFTojAN3kIqauI29g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون پرتاب موشک از یزد !
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20129" target="_blank">📅 10:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20128">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d722b8754d.mp4?token=i5qQ-FffD0w40rx5fRv9JMwYYBviBF-KgXSW8G762qPE-b2F5KrV5OFpc4URxHmN80sBcmDZUC7yfVJFfQeuW3orb48Na55Ifq7CRTxDp0XpASHuAVZU3Eoj5J92-SQ_BvyHU5Ys3c8GuP-bc12cqa6J6XuTxl8qO8gK3f9lRz2UE4CRNBo20BsjglqBDWJXEV_GkoLhaQDjoHjSrVaU6Q_dDN1Bf1UWz5aZZ_b-o3YjpuXMfzVnyorxrSn_3nclSai3fHJnacEY-tudqTT6rw1_gN6ZY8VJ-1gfwcs9YBY08nc8R6P_Ff3j--uSEenimUNGe3I3bRmrThcQNMWI8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d722b8754d.mp4?token=i5qQ-FffD0w40rx5fRv9JMwYYBviBF-KgXSW8G762qPE-b2F5KrV5OFpc4URxHmN80sBcmDZUC7yfVJFfQeuW3orb48Na55Ifq7CRTxDp0XpASHuAVZU3Eoj5J92-SQ_BvyHU5Ys3c8GuP-bc12cqa6J6XuTxl8qO8gK3f9lRz2UE4CRNBo20BsjglqBDWJXEV_GkoLhaQDjoHjSrVaU6Q_dDN1Bf1UWz5aZZ_b-o3YjpuXMfzVnyorxrSn_3nclSai3fHJnacEY-tudqTT6rw1_gN6ZY8VJ-1gfwcs9YBY08nc8R6P_Ff3j--uSEenimUNGe3I3bRmrThcQNMWI8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس نیور : آیا می‌دانید چند روس در این جنگ کشته شده‌اند؟ آیا تخمینی دارید؟
زلنسکی: کل تلفات روسیه ۱،۶۰۰،۰۰۰ نفر است و حدود ۷۰۰،۰۰۰ نفر کشته شده‌اند. تقریباً.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20128" target="_blank">📅 10:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20126">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78bd5b2c6.mp4?token=GhJaZi7XP2f5gOPQ7aNc7lGr7opNPpmh_aDUqvmgMw7EGi5kMT_VcBT1vZTH_A9rK4K3Kr556OSK4cct5U6WhpR65qwu9tI-oQVsv8OTfAhR7sVku0T78VanymLfznbJmp3cWridjR_GhbkMM6C_KsH8VJyqIlUY_0DfpT38zXgtV4CQ8wssOFXhwZ3OeYz08VKtxjbXLQeuKKJh5VRAh6EkiPTK2tYizsXPIY0ZTUWuQt_q1mRhFvSH3gAph5YFb5gcTVxYn2FnZ21l3-GYTl8dMYJcVUQX2CUSvN8gqyYbMUC98qeILACgD_tPq3GrsmRcJsWA8hxweKR9uin3MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78bd5b2c6.mp4?token=GhJaZi7XP2f5gOPQ7aNc7lGr7opNPpmh_aDUqvmgMw7EGi5kMT_VcBT1vZTH_A9rK4K3Kr556OSK4cct5U6WhpR65qwu9tI-oQVsv8OTfAhR7sVku0T78VanymLfznbJmp3cWridjR_GhbkMM6C_KsH8VJyqIlUY_0DfpT38zXgtV4CQ8wssOFXhwZ3OeYz08VKtxjbXLQeuKKJh5VRAh6EkiPTK2tYizsXPIY0ZTUWuQt_q1mRhFvSH3gAph5YFb5gcTVxYn2FnZ21l3-GYTl8dMYJcVUQX2CUSvN8gqyYbMUC98qeILACgD_tPq3GrsmRcJsWA8hxweKR9uin3MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور گرفتار وی آر شد !
عادل : من دست بوسی نمیکنم. آخه چرا باید دست یه مسئولی رو توی‌ جمع ببوسم؟! من اگه دست بوس بودم الان داشتم برنامه 90 رو اجرا میکردم.
ما این فیلم رو آهسته کردیم که ببینیم واقعا دست رو بوسیده یا نه. دیگه قضاوت با خود شما که دستشو بوسیده یا اون لحظه به هر دلیل دیگه ای یه لحظه سرشو آورده پایین که شبیه به دست بوسی شده.
نظر شما چیه؟!
دستشو بوسیده؟! یا اتفاقی سرشو‌ اون لحظه آورده پایین!؟
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20126" target="_blank">📅 10:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20125">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بی‌بی‌سی: یک شهروند بریتانیایی به اتهام جاسوسی برای سپاه IRGC، دستگیر شد. او به جمع‌آوری اطلاعات درباره یک پایگاه نظامی بریتانیایی در قبرس متهم است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20125" target="_blank">📅 10:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20124">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یک مقام آمریکایی به رویترز گفت که تهران تلاش کرد حماس را از پذیرش توافق خلع سلاح منصرف کند، اما ایالات متحده ادعا می‌کند که بر فشار ایران غلبه کرده است. این مقام آمریکایی افزود که سمت دیگر اگر اسرائیل هم این توافق را رد کند، رئیس جمهور ترامپ ناامید خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20124" target="_blank">📅 09:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20123">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e9526a12.mp4?token=XoXwzPB1Z2XoL7dt2U5B8fD6O0TWG6VnGbf2kfb8w0inToDQeaEB3lJ6wxgs7oI_3tzzKnEhyzf0f1txto0aBq8U1gfAaeFB39fgFcSG9rwoTvS6U3wO-axgUNpt_i0jEVl0a6vkA2-Xs1KhDA91PDRlBOSAeiqxW7zCDxr1jo4cupgX7aemoi_gySzpH9FUnf3X_CA4g4YkO7yz6YD0lE_P7FZMHXzGposX45q5doLaG0M-FYoRT0jOBydIpMZm5p_QUteOesTo8csIRhOMO0WY_EhPJ2IJet2NL8WhH7j0HwDL9SJl99TsMMa3DvASMG1WXavOIlpO3zeLlLu1pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e9526a12.mp4?token=XoXwzPB1Z2XoL7dt2U5B8fD6O0TWG6VnGbf2kfb8w0inToDQeaEB3lJ6wxgs7oI_3tzzKnEhyzf0f1txto0aBq8U1gfAaeFB39fgFcSG9rwoTvS6U3wO-axgUNpt_i0jEVl0a6vkA2-Xs1KhDA91PDRlBOSAeiqxW7zCDxr1jo4cupgX7aemoi_gySzpH9FUnf3X_CA4g4YkO7yz6YD0lE_P7FZMHXzGposX45q5doLaG0M-FYoRT0jOBydIpMZm5p_QUteOesTo8csIRhOMO0WY_EhPJ2IJet2NL8WhH7j0HwDL9SJl99TsMMa3DvASMG1WXavOIlpO3zeLlLu1pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روزهای اخیر، چند شهر اسپانیا شاهد ناآرامی‌های مرتبط با مهاجرت بوده‌اند.  مهم‌ترین درگیری‌ها در شهر توره پاچکو در منطقه مورسیا، واقع در جنوب‌شرق اسپانیا، رخ داد. این ناآرامی‌ها پس از حمله به یک مرد سالمند و انتشار ادعاهایی درباره مهاجر بودن عاملان آغاز شد…</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20123" target="_blank">📅 09:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20122">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مقامات اسرائیلی و آمریکایی به اکسیوس : ونس و نتانیاهو عصر سه‌شنبه در یک دیدار دوجانبه در واشنگتن، گفت‌وگوی «مستقیمی» درباره اختلافات خود داشتند
تانیاهو با ونس درباره انتقادات اخیر او از دولت اسرائیل گفت‌وگو کرد
با وجود تنش‌ها، طرفین سعی کرده‌اند روی «همکاری در حوزه‌های مشترک» تأکید کنند تا تصویر هماهنگی استراتژیک بین واشنگتن و تل‌آویو حفظ شود
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20122" target="_blank">📅 09:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20121">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">در روزهای اخیر، چند شهر اسپانیا شاهد ناآرامی‌های مرتبط با مهاجرت بوده‌اند.  مهم‌ترین درگیری‌ها در شهر توره پاچکو در منطقه مورسیا، واقع در جنوب‌شرق اسپانیا، رخ داد. این ناآرامی‌ها پس از حمله به یک مرد سالمند و انتشار ادعاهایی درباره مهاجر بودن عاملان آغاز شد…</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20121" target="_blank">📅 08:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20120">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ: مطمئن نیستم به اوکراین اجازه تولید موشک‌های پاتریوت را بدهم
این یک سلاح فوق‌العاده است و باید کمی درباره اینکه به چه کسانی مجوز تولید می‌دهیم، احتیاط کنیم
تمرکز اصلی من پایان دادن به جنگ روسیه و اوکراین است؛ کوشنر و ویتکاف، برای نخستین بار طی روز‌های آینده به اوکراین سفر خواهند کرد
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20120" target="_blank">📅 08:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20119">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFqsjB4NojGVkoLnS8oUV5gwmIDqrwVV5w-ot7Td5FWxgURnV35CD9fZyogXvIRcgIrLMA4eTrXBQiQrcQ8tRCu8xRLDSlI44KT7lCrE7iVaKna9sRJ4aXej-ijPLw0XJHGqGidJx6O2M3MIGvB_n2m7uFMaTn2x0dC-Mai-RjYgkZT8TmmpetoJqKP3ZHdVOucCF-S6h7ubZKadpgLs5A3O2DV4knaXZEifIVhtgm5RAGmgi7I316fw5MZmPGdYpvlLm4FNOAMKEhFnuFNhyncbzVl72ob_5ykDhc9_zdLZDZQUK9Xz9e1RTxtRuIt6Pgnni4oHnQLht9WlcMkzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری i24news : ارتش اسرائیل با ۷۰۰ تن مواد منفجره ، شبکه تونل‌های حزب‌الله را در زیر کوه بوفور نابود کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20119" target="_blank">📅 08:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20118">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">روزنامه تایمز : سیا و موساد دنبال پیدا کردن مجتبی خامنه‌ای هستن.
گفته میشه رهبر جدید زخمی شده و بالایِ 150 روزه که از هیچ وسیله الکترونیکی استفاده نکرده و احتمالاً تو یه پناهگاه زیرزمینی تو تهران یا اطراف قم مخفی شده. چون ردیابی از طریق شنود و ابزارهای الکترونیکی نتیجه نداده، سرویس‌های اطلاعاتی تمرکزشون ر‌ روی جاسوسیِ انسانی گذاشتن.
طبق ادعای مقام‌های سابق موساد، مجتبی خامنه‌ای پیام‌هاش رو از طریق چندین واسطه و نامه‌های دست‌نویس منتقل می‌کنه؛ پس تنها راه پیدا کردنش، نفوذ به حلقه نزدیکانشه. بعضی منابع اطلاعاتی احتمال میدن سپاه مرگِ مجتبی خامنه‌ای رو مخفی کرده باشه و بعضی دیگه میگن، ممکنه حکومت واسه گمراه کردن بقیه، از بدل استفاده کنه!
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20118" target="_blank">📅 04:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20117">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a76d99f52.mp4?token=iFZwO6JdeDPqewVWWX9qN82UxtSkwV4IQ98f1mPHDgOCwGNgE_k3S-VfyWaFow_xF-MWB7wyZ64TXqvzvuPAfzXmh7X8sy8si5mKJFQbIAtD334jllrvvMZsQydl_1nbMOGKtqZvpF7Vle_NBtCTlBsiSnVnFFohiWNtGF9LLBA3xFSJLqbi04J0OU7M1tn7Vog7lZXbYUtsoefUsE-N7XiP1uscqB6qpR-ra_tDxRrl2bwY2mK8DKAUjWChfoa_geTSvn5xToY5UO73IQSnerBAIvD9y8crwcpIYRlasYI25OBh6xXEhPq1ocCT8OCQNcYmj9bbRyeTb9kGm1EJfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a76d99f52.mp4?token=iFZwO6JdeDPqewVWWX9qN82UxtSkwV4IQ98f1mPHDgOCwGNgE_k3S-VfyWaFow_xF-MWB7wyZ64TXqvzvuPAfzXmh7X8sy8si5mKJFQbIAtD334jllrvvMZsQydl_1nbMOGKtqZvpF7Vle_NBtCTlBsiSnVnFFohiWNtGF9LLBA3xFSJLqbi04J0OU7M1tn7Vog7lZXbYUtsoefUsE-N7XiP1uscqB6qpR-ra_tDxRrl2bwY2mK8DKAUjWChfoa_geTSvn5xToY5UO73IQSnerBAIvD9y8crwcpIYRlasYI25OBh6xXEhPq1ocCT8OCQNcYmj9bbRyeTb9kGm1EJfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روزهای اخیر، چند شهر اسپانیا شاهد ناآرامی‌های مرتبط با مهاجرت بوده‌اند.
مهم‌ترین درگیری‌ها در شهر
توره پاچکو
در منطقه مورسیا، واقع در جنوب‌شرق اسپانیا، رخ داد. این ناآرامی‌ها پس از حمله به یک مرد سالمند و انتشار ادعاهایی درباره مهاجر بودن عاملان آغاز شد و به درگیری میان گروه‌های راست افراطی، مهاجران عمدتاً مراکشی و نیروهای پلیس انجامید. در این حوادث چندین نفر بازداشت و تعدادی نیز زخمی شدند.
هم‌زمان، در شهرهای مرزی
سئوتا
و
ملیلیا
در شمال آفریقا، که تحت حاکمیت اسپانیا هستند، تلاش هزاران مهاجر برای ورود به خاک اسپانیا باعث افزایش تدابیر امنیتی و تشدید تنش‌ها شده است
بخش قابل توجهی از مهاجرانی که تلاش می‌کنند وارد
سئوتا
و
ملیلیا
شونداز
مراکش
و برخی کشورهای مسلمان شمال و غرب آفریقا هستند
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20117" target="_blank">📅 04:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20116">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1e208199.mp4?token=QGIBttnzNKJ62Ygbc4hUlsl0NMRTpr7-ULSfCu3RvFWRn_1pkWg1bnzbfNordafK25zuqQjOBZZkjL2eYzBJNvTa9qdkuR-SgfBxZoxI3jabLGTlGL10TYX2_OLUHMPAc8naC6X_e1Hrw2De5VpzSJ4ybrifkeZE1xExDCtokpo_4swA2EdG2pB18xEDW1MauRQaDAAYbKUuwoxgGSwUEuZ8stN9eCFIKIMeNGg_oCESF0phbTISUX4X1OK6VQpePapsIncmEgPQsCJNi8gNoZI3TO79s0MBeK6cbP2b9DdNadLo7PAZmUOXaHAXVJqqPSgHCCWJ-0N5u_3ExihG-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1e208199.mp4?token=QGIBttnzNKJ62Ygbc4hUlsl0NMRTpr7-ULSfCu3RvFWRn_1pkWg1bnzbfNordafK25zuqQjOBZZkjL2eYzBJNvTa9qdkuR-SgfBxZoxI3jabLGTlGL10TYX2_OLUHMPAc8naC6X_e1Hrw2De5VpzSJ4ybrifkeZE1xExDCtokpo_4swA2EdG2pB18xEDW1MauRQaDAAYbKUuwoxgGSwUEuZ8stN9eCFIKIMeNGg_oCESF0phbTISUX4X1OK6VQpePapsIncmEgPQsCJNi8gNoZI3TO79s0MBeK6cbP2b9DdNadLo7PAZmUOXaHAXVJqqPSgHCCWJ-0N5u_3ExihG-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون حملات پهپادی مستمر به پایگاه‌های گروه‌های کورد مخالف رژیم ایران در اربیل
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20116" target="_blank">📅 03:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20115">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4qdcchwWBHKeT544cq80HIJc8h_TVAAH1M1Y2qim_xKjwr9PSnxgMb67f3MUdVBOjBXDDQ8NIefquc9GpcflEMTVXU3Egs33fN_xDfoxIwreuWthhUQcsxFcVTrEpVzizifITU7jyKhuoSWaOoRciHJjJIAL1nb72yCcxPPULYKTm4fM1gDnw-6hzWcj4-s5LuNeX9NEyH-Kw_-hF5Ixh9hkmAnohVFbIMwj1AmntlcM4xPkMEBO5CQ9uA58gG8R7yv7KlAGB03eiDoQKpUfiJFwqZQKm4eHauiGInGor8U_e_Z7FZs0LckvvOPug6l5z20uZ4ijNUF6QxfUhk7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مدعی شد توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه حاصل شده است. به گفته او، این توافق به‌صورت مرحله‌ای اجرا خواهد شد و پس از تکمیل خلع سلاح، نیروهای اسرائیلی از غزه خارج شده و اداره این منطقه به یک دولت جدید فلسطینی با حمایت یک نیروی بین‌المللی و پلیس جدید فلسطینی واگذار می‌شود. ترامپ همچنین از مصر، قطر و ترکیه به‌عنوان میانجی‌های این توافق قدردانی کرد و آن را گامی مهم در جهت صلح و امنیت پایدار دانست.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20115" target="_blank">📅 03:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20114">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ممباقر : حمله تروریستی به منازل مسکونی غیرنظامیان در جزیره قشم، ادامه جنایت در میناب و لامرد است.
امریکایی‌ها عادت کردن که سیلی‌هایی که در میدان نبرد می‌خورن رو با ریختن خون بی‌گناهان جبران کنند؛ تاوان خواهند داد.
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20114" target="_blank">📅 00:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20113">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dr1DB665x9jjLL6QTiStrziEYGx_FiO2n80ti2XXylmnVuwTCk_vzYsMDAqMxTwsvClgnSvuYZuFazsU6GO4jave71eeLM6ns1CeYw2cvAVSRUhOEoBpqMg2HrU7xVZ8Vi281afkLZ4YqASVBgMEkBceKnTz5GJKMTUemNrFWqWwML3LfM-aA7MpCuQsOrpaKt1rejQlLizxCCj2ezx2KXP7hCTu5kKK0tiw1uN0b4Qn-Ksswyuk01HGy44cGIZ3-OEIpk_xXPUrRoHmN79c2Zm4TmG3G7I2PMhEjAGFLZgg8-Xr-nOyl-hMA2crvwn2LjcrxgXUKcvRC8gxSGQe5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : حوادث ۲۴ ساعت گذشته:
حملات آمریکا به ایران: آبادان، اهواز، شادگان و اروندکنار: شلیک موشک‌های HIMARS؛ کازرون و پراش‌بند در فارس: حمله هوایی بدون گزارش تلفات؛ بوشهر و کیش: گزارش انفجار؛ قشم: حمله به یک خانه و کشته شدن دو ۳ نفر
حملات ایران به پایگاه‌های آمریکایی: پایگاه موافق‌السلتی در اردن: طبق ادعای ایران که آکریکا تکذیب کرده، ۳ فروند F-35 نابود و ۳ فروند دیگر آسیب دیدند و تعدادی از نیروهای آمریکایی کشته شدند؛ پایگاه علی‌السلام در کویت: دو انبار پهپاد و مخازن سوخت هواپیما و هلیکوپترها آسیب دیدند.
در عرصه دریایی: در تنگه هرمز، دو کشتی هنگام عبور با حادثه روبه‌رو شدند؛ در یکی آتش‌سوزی بزرگی رخ داد و هر دو بازگشتند. همچنین یک تانکر LNG قطری برای نخستین بار در سه هفته گذشته از مسیر تأییدشده ایران عبور کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/20113" target="_blank">📅 23:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20112">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">جمهوری اسلامی یک موج جدید از حملات موشک/پهپاد را به بحرین آغاز کرد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20112" target="_blank">📅 22:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20111">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا نام یک فرد و ۵ شرکت مرتبط با شرکت هواپیمایی ماهان را در فهرست تحریم‌ها قرار داده است.
بسنت، وزیر خزانه‌داری آمریکا :
هر کسی به سپاه یا ماهان‌ایر خدمات مالی، لجستیکی یا تجاری بده، به حفظ یک سازمان تروریستی کمک کرده
ما این افراد و شرکت‌ها رو شناسایی می‌کنیم، معرفی می‌کنیم و دسترسی‌شان رو به سیستم مالی آمریکا قطع می‌کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/20111" target="_blank">📅 21:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20110">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ارتش رژیم جمهوری اسلامی :
پایگاه شیخ عیسی در بحرین را با پهپاد هدف قرار دادیم
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20110" target="_blank">📅 21:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20109">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">لیست کشورهایی که اعلام کرده‌اند از ائتلاف دریایی عربستان برای حفاظت از کشتیرانی در دریای سرخ حمایت می‌کنند، به گفته عربستان  آن‌ها به این ائتلاف پیوسته‌اند :
کویت، بحرین، قطر، اردن، مصر، یمن، ترکیه، پاکستان، بنگلادش، سودان، جیبوتی، سومالی و نیجریه.
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/20109" target="_blank">📅 21:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20108">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">روند خلع سلاح حماس : ایالات متحده تمایل دارد پیشنهاد حماس مبنی بر تفکیک سلاح‌های سنگین و سبک در فرآیند "غیر مسلح کردن" این سازمان تروریستی را بپذیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20108" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20107">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شبکه i24 پیام اسرائیل به آمریکا:
بدون یک اقدام نظامی "معنادار" در ایران، تغییری حاصل نخواهد شد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20107" target="_blank">📅 21:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20106">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8772ccba1.mp4?token=rHQCTcfKpUpNPqoX0aTbrBdipv86GO93er2CopKWrix6ac_atnOYMua9SlSf6s8pCPSB-ejsIM3kU3bWI23F5c2_-1XNWrjT3bfslXeGavvyFn6HFgCWk1acUV9zmlJbGuxtO4Rbs2gXb0LRyPDMzCuTKW7QKfY3gKZ3BEM25rmRgTFnInqgxoW60tMbwNPNdCMHkTAsY50XUSOf0gtEjy3wvDz1ZFUVspM8b9VeT2Ygrq7Q3-a4zVBC9cHftDUWkTvV7DMFXm0YQBqAXn48Hrvp4opfbNDGTdDQIx5ISGVKSxxgOMCyTMRqaBkVnb7jQU1GFpL3VgqTKeGFmSeGZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8772ccba1.mp4?token=rHQCTcfKpUpNPqoX0aTbrBdipv86GO93er2CopKWrix6ac_atnOYMua9SlSf6s8pCPSB-ejsIM3kU3bWI23F5c2_-1XNWrjT3bfslXeGavvyFn6HFgCWk1acUV9zmlJbGuxtO4Rbs2gXb0LRyPDMzCuTKW7QKfY3gKZ3BEM25rmRgTFnInqgxoW60tMbwNPNdCMHkTAsY50XUSOf0gtEjy3wvDz1ZFUVspM8b9VeT2Ygrq7Q3-a4zVBC9cHftDUWkTvV7DMFXm0YQBqAXn48Hrvp4opfbNDGTdDQIx5ISGVKSxxgOMCyTMRqaBkVnb7jQU1GFpL3VgqTKeGFmSeGZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنای آمریکا با
۵۰ رأی مخالف
در برابر ۴۹ رأی موافق
طرح محدود کردن اختیارات ترامپ برای اقدام نظامی علیه ایران رو رد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20106" target="_blank">📅 20:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20105">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رویترز به نقل از مقام‌های فدرال و ایالتی آمریکا گزارش داد که بازرسان در حال حاضر احتمال می‌دهند هکرهای مرتبط با ایران مسئول حمله سایبری هماهنگ به سامانه‌های آب شهری در ایالت مینه‌سوتا باشند، اما تأکید کرده‌اند که هنوز به نتیجه‌گیری قطعی نرسیده‌اند و تحقیقات ادامه دارد. به گفته این مقام‌ها، این احتمال نیز وجود دارد که مهاجمان برای افزایش تنش‌ها، خود را به جای هکرهای ایرانی معرفی کرده باشند. در این حمله بیش از ۳۰ سامانه آب شهری هدف قرار گرفت، دست‌کم یک چاه و یک تأسیسات تصفیه آب به‌طور موقت از مدار خارج شد و چندین سامانه نیز به کنترل دستی منتقل شدند، اما مقام‌ها اعلام کردند که کیفیت آب آشامیدنی تحت تأثیر قرار نگرفته و هیچ موردی از آلودگی آب گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20105" target="_blank">📅 20:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20104">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نتانیاهو : ممدانی، شهردار نیویورک، ایران و حزب الله و حماس رو حمایت می کنه!
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20104" target="_blank">📅 19:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20103">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رویترز، با استناد به دو مقام در غرب آسیا، گزارش داد که انصارالله این هفته از خاک عراق و با هماهنگی گروه‌های مسلح عراقی و نظارت از سوی سپاه ، به عربستان سعودی حمله کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20103" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20102">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سنتکام ادعای ایران مبنی بر انهدام سه فروند جنگنده رادارگریز اف-۳۵ لایتنینگ ۲ در پایگاه هوایی موفق سالتی، اردن را تکذیب کرد؛ و ادعای رسانه‌های ایرانی مبنی بر اینکه نفتکش ام/تی نورا محاصره آمریکا را شکسته است را نیز رد کرد.
سنتکام همچنین بار دیگر ادعا کرده است که تهدید اصلی برای کشتیرانی تجاری در تنگه هرمز، رژیم ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20102" target="_blank">📅 19:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20101">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گزارش وقوع چندین انفجار در صنعا ، یمن
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20101" target="_blank">📅 18:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20100">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">«فاکس نیوز»: همکنون دولت آمریکا گزینه‌های انجام عملیات نظامی گسترده علیه ایران را به ترامپ ارائه داد.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20100" target="_blank">📅 17:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20099">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">Bitcoin : 65000$
Tether : 193000T
Brent oil :91.5$
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20099" target="_blank">📅 17:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20098">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اواخر شب گذشته، دو فروند بمب‌افکن B-1B Lancer با شناسه‌های LANE90/91 از پایگاه RAF Fairford برای یک مأموریت آموزشی کوتاه بر فراز سواحل جنوب‌غربی بریتانیا به پرواز درآمدند و با پشتیبانی هواپیمای سوخت‌رسان CLEAN71 عملیات را آغاز کردند. این بمب‌افکن‌ها سپس برای تعویض خدمه به فرفورد بازگشتند و حدود ساعت ۰۱:۴۵ بامداد با شناسه‌های HARPO40/41 دوباره به پرواز درآمدند تا با سه فروند هواپیمای سوخت‌رسان CLEAN91، CLEAN92 و CLEAN93 از پایگاه Lajes تمرین سوخت‌گیری هوایی انجام دهند. به نظر می‌رسد این تمرین، شبیه‌سازی سناریوی عدم دسترسی به حریم هوایی فرانسه و پرواز به سمت ایران از مسیر جبل‌الطارق بوده؛ مسیری که پیش‌تر در عملیات Operation Epic Fury نیز استفاده شده بود. این مأموریت حدود ساعت ۰۴:۱۵ بامداد با بازگشت بمب‌افکن‌ها به RAF Fairford و هواپیماهای سوخت‌رسان به Lajes پایان یافت
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20098" target="_blank">📅 16:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20097">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJZSuZWtooO_gsjWb2Ann8dAx0nYcatZKIfrrX4mZ6yikWGdOs4_EOvr2JOGzuqgaAy_QWh6PiJpBxQquAeTuH7seTfuDZn9GOGve5dUNCtGx40MWWxH-bTX4BJc9L1xrN5cPhCe6Hd7JViUADNAKCbm9tV9lTV-7TOsjKb__4-OI82VOM-h2gPPkp9IhHAXgVqeUOTCbuSHHH68ueWbI9Ps40LEL_D5CKYstIa4Atec7Vi3oDtjlK5_qe4PQqp-dQImpJlQHDQAbOUWDKisIZEN_NM-EltqLMGOjFkTWOoR_TQQpYP0oeQiQ-wYm8QTdw1IIzgH-7u1p45YI_DXMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏۳ تا از کثافتهای رسما گی حشدالشعبی که در حمله عربستان کشته شدند (عکس رسمی) همین افراد دی ماه در ایران قتلعام کردند. @WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20097" target="_blank">📅 16:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20096">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گزارش کانال ۱۴ : درون کوه کلنگ گزلا - مستحکم‌ترین سایت هسته‌ای ایران.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20096" target="_blank">📅 16:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20095">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اکسیوس : چین با ۴۰ درصد کاهش خرید نفت موجب
جلوگیری از جهش شدید قیمت‌ها در پی جنگ و بسته شدن تنگه هرمز شد
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20095" target="_blank">📅 15:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20094">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سپاه زنجان: در حمله موشکی دیشب آمریکا، 3 پاسدار کشته شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20094" target="_blank">📅 15:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20093">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وزیر دارایی اسرائیل، بزالئل اسموتریچ:
«غزه بزرگترین زندان جهان است. مردم به زور و برخلاف میلشان در آنجا نگهداری می‌شوند و اجازه خروج ندارند. این یک چیز وحشتناک است. فقط دروازه‌ها را باز کنید و بگذارید غزه‌ای‌ها بروند.»
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20093" target="_blank">📅 15:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20092">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خانه ای که در محله مينابي در قشم موشک خورد گزارشات بومی میگن که محله مينابي ها همشون جز بسيج و سپاهن و عادی نیستند ، ویدیو خبرنگار رژیم این گزارش رو تایید میکنه و نشون میده عکس قاسم کتلت هم بر دیوار بوده @WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20092" target="_blank">📅 14:51 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
