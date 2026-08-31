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
<img src="https://cdn4.telesco.pe/file/Fv7iQavDcNvU0RmIPt-F3YV2Zx4l5uPQJUIdSmbWyV_c-kRj6IE440VsN3Cea-w4PKxjH2cM7y-XzXFO6HxA6zJTxkPlWhgdE2N4lnbz3d41Dbg2hYP90GRMWAAlaKWR_cy7HCzXPrsgZyzqDBfIdrih6EP2J3g1urrXelakB8UaUFhFGzPtsZMi508SyQ7w_Cjh221zZYJw5Fs2Lv0rwNcunVOjV20vZu5rWNRJ2IzFYITYGTKbv6wgzkG6OtvcEa0kj1QVFPGoTQj8MnulNH0FBKkqnuosNE9lspUyHqEOB78sTs83ZiMDZI_qZhF3HoUIILJWtVYvkK-4Is7Rjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 442K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 01:27:09</div>
<hr>

<div class="tg-post" id="msg-21883">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گزارش انفجار/پرتاب ‌جدید از سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/withyashar/21883" target="_blank">📅 01:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21882">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خیلی گزارش اومده صدای انفجار سیریک ، فک نکنم اینبار شلیک باشه فک کنم زدن…
@WarRoom</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/withyashar/21882" target="_blank">📅 01:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21881">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تنگه دعوا شده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/21881" target="_blank">📅 00:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21880">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مایک جانسون، رئیس مجلس نمایندگان آمریکا، درباره ایران: نمی‌توانیم بدون اینکه این موضوع به طور کامل حل شود، آنجا را ترک کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/21880" target="_blank">📅 00:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21879">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رسانه‌های اسرائیلی: قالیباف و عراقچی با ایالات متحده تماس گرفتند تا سطح تنش‌ها کاهش یابد
@WarRoom</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/21879" target="_blank">📅 00:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21878">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ادعای خبرگزاری نیوزویک : ایالات متحده قصد دارد یک کارزار رزمی ۱۰روزه محدود علیه ایران در جهت استهلاک هرچه بیشتر اقتصاد این کشور انجام دهد
@WarRoom</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/21878" target="_blank">📅 00:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21877">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">العربیه: شبه‌نظامیان حوثی با دو موشک بالستیک به شمال بندر المخا حمله کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/21877" target="_blank">📅 00:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21876">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اتاق جنگ با یاشار : کاوری که با عنوان «اکونومیست ۲۰۲۷» در شبکه‌های اجتماعی منتشر شده، فیک است. این تصویر تاکنون به‌عنوان جلد رسمی از سوی اکونومیست منتشر نشده است. مراسم معرفی
The World Ahead 2027
قرار است پنج‌شنبه ۳ دسامبر ۲۰۲۶، برابر با ۱۲ آذر ۱۴۰۵، با حضور تام استندج، ویراستار این مجموعه، برگزار شود. بنابراین تصویر منتشرشده پیش از رونمایی رسمی، اعتبار ندارد
@WarRoom</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/21876" target="_blank">📅 00:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21874">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تنگه دعوا شده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/21874" target="_blank">📅 00:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21873">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کل یزد دایرکت دادن که از یزد موشک زدن الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/21873" target="_blank">📅 00:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21872">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گزارش تایید نشده صدای انفجار شرق بندر عباس
@WarRoom</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/21872" target="_blank">📅 00:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21871">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4261e93c.mp4?token=sES4dFdlDlWELR7X6BRRZG8vNn9OendF4pfw5Ls26u7noCjklR3ArJnbwD-k-zzOxTjC-Nqd5fOiLjd4OtzU7vrPDSHuoMdVrZy99jEBr6cgGyn9NXJp1WHiS1qxJBBqMyh2ewJgNeGCRzd8bywg_Z5fS1KCHs3Mqr7tNto5UZG74wK1Kfh9qoGnenuUmSvamUzVQe-GiF-4v4KMQQ-qNGU9VbV7aXfJbfXCuc-0NybZMhXI3NB9OEe0elw949wey7yAibphrbEgfplL85yvckD5hpVmAaWA3Ou6oFVBADk4nsXWpiNMP-l6n3GWL-3Z308_e_rgeqPVuenlMv9k4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4261e93c.mp4?token=sES4dFdlDlWELR7X6BRRZG8vNn9OendF4pfw5Ls26u7noCjklR3ArJnbwD-k-zzOxTjC-Nqd5fOiLjd4OtzU7vrPDSHuoMdVrZy99jEBr6cgGyn9NXJp1WHiS1qxJBBqMyh2ewJgNeGCRzd8bywg_Z5fS1KCHs3Mqr7tNto5UZG74wK1Kfh9qoGnenuUmSvamUzVQe-GiF-4v4KMQQ-qNGU9VbV7aXfJbfXCuc-0NybZMhXI3NB9OEe0elw949wey7yAibphrbEgfplL85yvckD5hpVmAaWA3Ou6oFVBADk4nsXWpiNMP-l6n3GWL-3Z308_e_rgeqPVuenlMv9k4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: گزارش شده است که چندین فرمانده ارشد نظامی به وزیر دفاع، هگست، گفته‌اند ادامه یک عملیات گسترده و طولانی‌مدت در ایران، توانایی ما برای مقابله با تهدیدها در نقاط دیگر، از جمله در داخل خاک آمریکا، را تضعیف می‌کند…
ترامپ: ما هیچ هدف دیگری در ذهن نداریم. هیچ‌کس دیگری آن‌قدر دیوانه نیست که چنین کاری انجام دهد. ما در سراسر جهان مهمات بسیار زیادی داریم و اگر بخواهیم، همیشه می‌توانیم از آنها استفاده کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/21871" target="_blank">📅 23:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21870">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ : همه گفتن نهههه ولی من کردممم
@WarRoom
😂</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/21870" target="_blank">📅 23:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21869">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9uzJNdmTIll8e9ylqE46WrcLu2j6zZFHeOrBJfg37Z-GvMLiB94X4XDcFVGyrwE90My-U1Rf7bTtdWJSX8dNB5sTUcvOIbqN1UQ4Hf9kywj1FKAB1mIMMYO7uROjqCYGgN7C7SusDMR-twznofUC7GODZ3KX0Q7JguH7FNaSTfxXGlKZs0a9xaKg24fEmFuVDMBFKccGd3nmsnpXXUZfX1GUuzZBeBkkmfdFNsoqJTg5amDVpNOKnhF2ud7gDXdJBMQXFSSvLp9zWHZ-QCLKrm-ybFFbuLBU7aRklfoHRheThahC1G-Aoc7ZoFVFG36nI6jQD4GIwTjr2zBzKqJcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا : اعلام می‌کند که گزارشی از «حادثه‌ای شامل یک نفتکش و نیروهای نظامی» در اقیانوس هند، شرق عمان دریافت کرده است.
یاشار : اطلاعات و مکان بیشتر با ورود نیروی دریایی ایالات متحده به یک کشتی مطابقت دارد
@WarRoom</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/21869" target="_blank">📅 23:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21868">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253924d72.mp4?token=asRbvfw8DkAyAlz6c5VRzPTUKkb1_XwbXV7MHQ06zaeMiQAibMjEOlKoovOOmH3fH_eaJMKS1r7AHe7gakIF-W8iWp5VBll3itrB2p8ydAKy8Yf1I6lrLCtJYyPrj3EsqFmlcUQvLB9CUyi9q-m36rzQbK1TBXINYiBW54tcoce_j2NT8ev0LiJn-7KQmK_RfCg4ICWsTAN5GhYtZ2CoKUdIvuhfo4jbLE6W5k3tE3DlF8ilGqZ2SAFDx5owpeObHKdu9u6EiixzE09W8whrvZNtP2GkkD5FMYopuid7oF0pGYzYpnh17U11n9_YOOt7s33oybaNNVpi7au4xDOILw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253924d72.mp4?token=asRbvfw8DkAyAlz6c5VRzPTUKkb1_XwbXV7MHQ06zaeMiQAibMjEOlKoovOOmH3fH_eaJMKS1r7AHe7gakIF-W8iWp5VBll3itrB2p8ydAKy8Yf1I6lrLCtJYyPrj3EsqFmlcUQvLB9CUyi9q-m36rzQbK1TBXINYiBW54tcoce_j2NT8ev0LiJn-7KQmK_RfCg4ICWsTAN5GhYtZ2CoKUdIvuhfo4jbLE6W5k3tE3DlF8ilGqZ2SAFDx5owpeObHKdu9u6EiixzE09W8whrvZNtP2GkkD5FMYopuid7oF0pGYzYpnh17U11n9_YOOt7s33oybaNNVpi7au4xDOILw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا استفاده از سلاح هسته‌ای علیه ایران را منتفی کرده‌اید؟
ترامپ: من هیچ‌وقت چنین چیزی را نمی‌گویم، اما پاسخ بله است.
دلیلی برای این کار وجود ندارد. چه سؤال احمقانه‌ای. آنها کاملاً شکست خورده‌اند.
من آنها را شکست داده‌ام، بعد باید علاوه بر آن از سلاح هسته‌ای هم استفاده کنم؟ چه سؤال احمقانه‌ای.
@WarRoom</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/21868" target="_blank">📅 23:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21867">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2ae0a3f9f.mp4?token=fQgDhRtl_CtSeWxrf1IQLi-QG6zPbJ_h09gpFsA2sVvu9sc3d1os7PMeaQqevH8PfdE1Bz_SViuWwoxX3rcnceYBjVzf50J-qwnnQMUGtLWlX6mDPGaXPnog4Re5m8A7MQ4ZFvrK2Rc1Y-4zvPRi5zCQ-48GCWH2JTO-prrMM7e9hYXovKRLMb2w7ln1ReSvC3SminwfYI36vU1uAhI4NAwPmnM2NNiJfzvPchYCHtuYrYdZKyhdH-H2CNxHfT2qwYCeHgUw4LJ50dSDysg7icSQjoCmEXq_I3GcDmgkMwZ2yTfyJYfqyGQgx4K4xluReVc1qnJBvvp3bYFrDhFSxjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2ae0a3f9f.mp4?token=fQgDhRtl_CtSeWxrf1IQLi-QG6zPbJ_h09gpFsA2sVvu9sc3d1os7PMeaQqevH8PfdE1Bz_SViuWwoxX3rcnceYBjVzf50J-qwnnQMUGtLWlX6mDPGaXPnog4Re5m8A7MQ4ZFvrK2Rc1Y-4zvPRi5zCQ-48GCWH2JTO-prrMM7e9hYXovKRLMb2w7ln1ReSvC3SminwfYI36vU1uAhI4NAwPmnM2NNiJfzvPchYCHtuYrYdZKyhdH-H2CNxHfT2qwYCeHgUw4LJ50dSDysg7icSQjoCmEXq_I3GcDmgkMwZ2yTfyJYfqyGQgx4K4xluReVc1qnJBvvp3bYFrDhFSxjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار
:
ازسرگیری حملات به ایران، یک عملیات محدود است یا یک جنگ تمام‌عیار؟
ترامپ
:
آن‌ها یک کشور شکست‌خورده‌اند... این به آن معنا نیست که به آن‌ها ضربه نخواهیم زد. خواهیم دید چه اتفاقی می‌افتد.
@WarRoom</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/21867" target="_blank">📅 23:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21866">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e3f0dc763.mp4?token=BPnLFvvJ_-sTckxsCUKTqWZSh2XC46F9-IC6u5M-0-XKYydq7UbdnlPdKACbOG1Hb6_pS-Qfz3HvtSSR2E78q18V5GKn6exIMS9N1fBMS851dBxnqTQipDaqmS202rNahSoOnpp8DMR70FOvrypfNYG-cjX5MrBIrwF3CUvgT_Q4BHXTTg_LKdPZQIprBZv3hZSntN8Cynf8CZU-fBBafjXUXLPI1C-OJFBOFycNiC8GGEoej_wnptYaaCClp9v6-qAMrwUjGJl1NLh5pmxt6cXzwvDNqXkzhLax2OEO1sBUoPx_fNvd0OMuVuRxS1RDah9MvRA01ZKbLB9MPWnTCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e3f0dc763.mp4?token=BPnLFvvJ_-sTckxsCUKTqWZSh2XC46F9-IC6u5M-0-XKYydq7UbdnlPdKACbOG1Hb6_pS-Qfz3HvtSSR2E78q18V5GKn6exIMS9N1fBMS851dBxnqTQipDaqmS202rNahSoOnpp8DMR70FOvrypfNYG-cjX5MrBIrwF3CUvgT_Q4BHXTTg_LKdPZQIprBZv3hZSntN8Cynf8CZU-fBBafjXUXLPI1C-OJFBOFycNiC8GGEoej_wnptYaaCClp9v6-qAMrwUjGJl1NLh5pmxt6cXzwvDNqXkzhLax2OEO1sBUoPx_fNvd0OMuVuRxS1RDah9MvRA01ZKbLB9MPWnTCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما وارد ایران شدیم و داریم حسابی آنها را درهم می‌کوبیم.
@WarRoom</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/21866" target="_blank">📅 23:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21865">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4906f15f1.mp4?token=XTiuZDaYT_XNH7s2JQw0MT0f8Hu8AUPBJW1w9Eb0hKXa4p_VTwz5EInXgVdBwKwoNcsWC9uX696hJZtUe492AOP__CqHhC84mJGqm3dR5Hb4HRo48prxuPtGnIVYFm4H-wBOszASUvYScnLFOKT3zqRUSsQjvFRreZZ5eL2Kh8Vple3Q2pk0avL4m_sywCVNaiqn-voRMldc35O0s2bez6VvrVoiZa9HRD7uD_teONm0X6xLZ3Ms4XsFtV66pmKtZ0qShaXuitfEhqErTbCKBt3iwY29ozCtaq-wId6MmrVheBbYS0PWC3CZJPtEsJA-g1Ub7S1J2LewDwvG0go63w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4906f15f1.mp4?token=XTiuZDaYT_XNH7s2JQw0MT0f8Hu8AUPBJW1w9Eb0hKXa4p_VTwz5EInXgVdBwKwoNcsWC9uX696hJZtUe492AOP__CqHhC84mJGqm3dR5Hb4HRo48prxuPtGnIVYFm4H-wBOszASUvYScnLFOKT3zqRUSsQjvFRreZZ5eL2Kh8Vple3Q2pk0avL4m_sywCVNaiqn-voRMldc35O0s2bez6VvrVoiZa9HRD7uD_teONm0X6xLZ3Ms4XsFtV66pmKtZ0qShaXuitfEhqErTbCKBt3iwY29ozCtaq-wId6MmrVheBbYS0PWC3CZJPtEsJA-g1Ub7S1J2LewDwvG0go63w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: آنها واقعاً نمی‌دانند رهبرشان کیست.
@WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/21865" target="_blank">📅 23:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21864">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad4bfc4cdc.mp4?token=K3HiHkynWuh5H9Ua1zVx2ADt8NuWCrQgWsu03wr0Z-F1mL9JTmQT9Ow9ct3wWC1ty_LdCdfFewozNAJu0IXKawAAo1PIkY95Vvtgf5ilFUaX10IJbdwG90CJUXNmHo29ocr71jxdud8W47BtyqAVhpRCEUDujGcP7OVTzDZut0SOXYAyQj7zR6DffdTBXcTrMXsDITKSrDSTW5pj5nK4HAVgIG5uOIS4tHKrVBwcdQbY8dKmr7zdT3nk0y92EYvUNbOxMXqVoQtqYh5o73LZpEkMSFUcEFEg_Uu14vZW-8zV5OiGZSqC0A_AFxTpcZ45-OcMYEOsvCxwOngbQLaPK4WkVwAez8QQeN2m6QmTthK7h1j5l0A_lTg6JXBQiMab2WiqSzYmzbqN-1DDM8OcckX30BlcLzJj_TdM80ik_7ShosL4WbHsg5zWIk6cboKAfWH_awyDW3b4cn0LViJ796yYcZ3HUlnSu8ezZq7jbb08KGSspqpeabZXe9e0e1W8OVigNJLp4je4Bj_ShKemDIsJK5cq97phMkMK8JGx3Zc2A9zpjtuHYuPVSQ1_e8N-RtrbWaJdQ5gwy3Y8x4mkSzXYzfCzstZ5AYNCaBcOhSDc2GibID0pHVrbmrV006Y9o5QUQ4JJeZhMah81DowUuB73pg8Adk5Zb1lY_31vFqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad4bfc4cdc.mp4?token=K3HiHkynWuh5H9Ua1zVx2ADt8NuWCrQgWsu03wr0Z-F1mL9JTmQT9Ow9ct3wWC1ty_LdCdfFewozNAJu0IXKawAAo1PIkY95Vvtgf5ilFUaX10IJbdwG90CJUXNmHo29ocr71jxdud8W47BtyqAVhpRCEUDujGcP7OVTzDZut0SOXYAyQj7zR6DffdTBXcTrMXsDITKSrDSTW5pj5nK4HAVgIG5uOIS4tHKrVBwcdQbY8dKmr7zdT3nk0y92EYvUNbOxMXqVoQtqYh5o73LZpEkMSFUcEFEg_Uu14vZW-8zV5OiGZSqC0A_AFxTpcZ45-OcMYEOsvCxwOngbQLaPK4WkVwAez8QQeN2m6QmTthK7h1j5l0A_lTg6JXBQiMab2WiqSzYmzbqN-1DDM8OcckX30BlcLzJj_TdM80ik_7ShosL4WbHsg5zWIk6cboKAfWH_awyDW3b4cn0LViJ796yYcZ3HUlnSu8ezZq7jbb08KGSspqpeabZXe9e0e1W8OVigNJLp4je4Bj_ShKemDIsJK5cq97phMkMK8JGx3Zc2A9zpjtuHYuPVSQ1_e8N-RtrbWaJdQ5gwy3Y8x4mkSzXYzfCzstZ5AYNCaBcOhSDc2GibID0pHVrbmrV006Y9o5QUQ4JJeZhMah81DowUuB73pg8Adk5Zb1lY_31vFqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: آنها یک کشور شکست‌خورده هستند. نرخ تورم آنها به 350 درصد رسیده است. آنها هیچ ارز معتبری ندارند. به سربازان خود حقوق نمی‌دهند. بیشتر رهبرانشان فوت کرده‌اند.
نیروی دریایی آنها نابود شده است. نیروی هوایی آنها از بین رفته است. تجهیزات نظارتی آنها تقریباً به طور کامل از بین رفته است.
این به این معنی نیست که ما به آنها حمله نخواهیم کرد. ببینید چه اتفاقی می‌افتد.
@WarRoom</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/21864" target="_blank">📅 23:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21863">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18b0e8cad.mp4?token=v4YpHyGc4AU0dDyQC4CUVwrULWCygPKm--a9ZtcO5FGzIftmTE5eJPKLx5yZph5wlX2n1yaKFmIh4AmxRETLelTYzKnNetldLWSvoJBBA4qEIvECkEO_OQZX6rpbDiJ429Fb4ml5doog4oCj7k9AQXNYDVVJ2_OD6JWBiBC36PmNxYsWTAjykLL9kayzPiZLocJgYld8XSVa9KH0cy19pbtuYsbztRe6uKpB9IF5EF0LGEwPrHprGVGYpjJht7iFSMSRsU7FELpr0xKiSLz4C67lFS8twzd5Z33PeREJv5fwB0xTSHL5gg5NSeT-YG_GQtULn5sCECqTr5TnhhtAPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18b0e8cad.mp4?token=v4YpHyGc4AU0dDyQC4CUVwrULWCygPKm--a9ZtcO5FGzIftmTE5eJPKLx5yZph5wlX2n1yaKFmIh4AmxRETLelTYzKnNetldLWSvoJBBA4qEIvECkEO_OQZX6rpbDiJ429Fb4ml5doog4oCj7k9AQXNYDVVJ2_OD6JWBiBC36PmNxYsWTAjykLL9kayzPiZLocJgYld8XSVa9KH0cy19pbtuYsbztRe6uKpB9IF5EF0LGEwPrHprGVGYpjJht7iFSMSRsU7FELpr0xKiSLz4C67lFS8twzd5Z33PeREJv5fwB0xTSHL5gg5NSeT-YG_GQtULn5sCECqTr5TnhhtAPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : در صورت بروز وضعیت اضطراری یا جنگ، ما کاملاً آماده‌ایم تا با آن مقابله کنیم
هیچ‌کس به ما حمله نخواهد کرد. می‌دانید دلیلش چیست؟
چون آن‌ها عاقل هستند
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/21863" target="_blank">📅 23:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21862">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کانال ۱۲ اسرائیل: چند مقام ایرانی امشب به‌صورت مستقیم و همچنین از طریق واسطه‌های منطقه‌ای با دولت ترامپ تماس گرفته‌اند تا از حملات تلافی‌جویانه گسترده آمریکا که گفته می‌شود برای امشب برنامه‌ریزی شده، جلوگیری کنند. این گزارش پس از ۲۴ ساعت پرتنش و در پی تبادل اقدامات نظامی میان ایران و آمریکا منتشر شده و تاکنون از سوی تهران یا واشنگتن تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21862" target="_blank">📅 22:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21861">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">همکنون یک F-35 از سمت خلیج فارس به سمت عربستان سعودی سیگنال 7700 روشن کرده ودر حال فرود اضطراری است @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21861" target="_blank">📅 21:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21860">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اکسیوس : به گفته سه مقام آمریکایی، رئیس جمهور ترامپ در حال بررسی طرحی از سوی سنتکام برای انجام حملات محدود در تنگه هرمز بوده است تا از بازسازی قابلیت‌های راداری و موشکی ایران برای حمله به کشتی‌ها جلوگیری کند
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21860" target="_blank">📅 21:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21859">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خوب رسیدیم به ساعات ملکوتی صدای انفجار به وقت سیریک لطفا گوش هاتونو تیز کنید
😁
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21859" target="_blank">📅 21:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21858">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آکسیوس:شرکت‌های رمزارزی به‌دنبال ورود مستقیم به نظام بانکی آمریکا
اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرد تعداد درخواست‌ها برای تأسیس بانک‌های جدید در دوره دوم ریاست‌جمهوری ترامپ افزایش یافته و بخش قابل‌توجهی از این درخواست‌ها از سوی شرکت‌های فین‌تک و رمزارزی مانند
Coinbase و Ripple
است. این شرکت‌ها می‌خواهند با گرفتن مجوز بانکی، خودشان مستقیماً خدمات مالی و بانکی ارائه کنند و کمتر به بانک‌های سنتی به‌عنوان واسطه وابسته باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21858" target="_blank">📅 21:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21857">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پنتاگون قراردادهای هفت‌ساله‌ای با لاکهید مارتین و سیستم‌های مهمات و تاکتیکی جنرال داینامیکس امضا کرده است تا تولید موشک‌ها را گسترش دهد.
این توافق‌ها با هدف افزایش تولید و تسریع در تحویل اجزای حیاتی برای برنامه‌های موشک‌های ضد موشک تهاد (THAAD) و پاتریوت PAC-3 MSE انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21857" target="_blank">📅 20:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21856">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">امروز
کنگره آمریکا بعد از تعطیلات تابستانی دوباره شروع به کار کرده، تمرکز اصلی مجلس نمایندگان روی
لایحه تأمین مالی موقت دولت
برای جلوگیری از تعطیلی دولت است
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21856" target="_blank">📅 20:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21855">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTarazi</strong></div>
<div class="tg-text">به تمامی دوستانم معروفیت کردم حتی به راننده های اسنپ گفتم بهشون صریح ترین و سریع ترین و درست ترین اخبار رو فقط از یاشار دنبال کنید خودم گوشی رو میگیرم براشون میزنم پیجت رو</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21855" target="_blank">📅 20:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21854">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8089942cc.mp4?token=JrzyO0lxRElrB13_YzfDjctlKXTPy57uxkCTAPhOicYzl2B2g1toaQsYvlP0xS0NBfKFlo1SjtYSztluEn9TD9sYRcY3YuC2PThbUawaaEwvvVg4qtJ_ZMbf4eXEWk5vcNEkiAtPHEtG4bdxx8C0kTR4S558wmj-eQMAKLlj8voSiRH6y2jXXs1iYZi9WvLumOpoFim5MIOsvg77-RaYFxehm9Roo6XyQtR5K2bD5QOu4OWrwKkmXpZ3qE5MxFNp9CZ0f_jm48k6ncxPxGtURAcJl90chCjH2LqzBAVhQbQugwEvNb7YVtQpw2-TujWvHosgOx0AgJsudfeLc52GnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8089942cc.mp4?token=JrzyO0lxRElrB13_YzfDjctlKXTPy57uxkCTAPhOicYzl2B2g1toaQsYvlP0xS0NBfKFlo1SjtYSztluEn9TD9sYRcY3YuC2PThbUawaaEwvvVg4qtJ_ZMbf4eXEWk5vcNEkiAtPHEtG4bdxx8C0kTR4S558wmj-eQMAKLlj8voSiRH6y2jXXs1iYZi9WvLumOpoFim5MIOsvg77-RaYFxehm9Roo6XyQtR5K2bD5QOu4OWrwKkmXpZ3qE5MxFNp9CZ0f_jm48k6ncxPxGtURAcJl90chCjH2LqzBAVhQbQugwEvNb7YVtQpw2-TujWvHosgOx0AgJsudfeLc52GnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
تنها چیزی که برای رهبران ایران مهمه اینه که سرشون به گردنشون وصل باشه ( نکشیمشون )
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21854" target="_blank">📅 20:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21853">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سه پا : سامانه‌های پدافند هوایی ما یک پهپاد از نوع MQ-9 را در شرق تنگه هرمز سرنگون کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21853" target="_blank">📅 20:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21852">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الجزیره
:
پوتین اعلام کرد روسیه در مسیر پایان دادن به مناقشه اوکراین است
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21852" target="_blank">📅 19:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21851">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6a8c19c57.mp4?token=rrCsxoqs_h0-0-_pyG_Rqawdrt6BvyZwvRq1Cfo2bepwZ_GnHd15duqKLECFNXJJFgWtoRspX7vdsIxuSFm3W0W2MZkUFWhTtxizOGavxrV09oj4hI1LV7sJP4xpcv5329D5X726LKRkwAfFQ2ii1QM4Mc4tjmJZ2Sn-65t7Tth84DbRHRMtwH6M8Op5ZaYKHqtJARTtA_uAOVIfsTrlG-rbOhZaOBJp1Ct5HzEPSsEwjqRsnspmgBkCcPoMzXSOdlG5CHBEkmA7wWmYTKcuEvSMJ72qCxU4n-tOCPl8m9-eI8qaWQZ43_oYYBJoZB1uL98SJUB9uHIHJJ9_Y2iyxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6a8c19c57.mp4?token=rrCsxoqs_h0-0-_pyG_Rqawdrt6BvyZwvRq1Cfo2bepwZ_GnHd15duqKLECFNXJJFgWtoRspX7vdsIxuSFm3W0W2MZkUFWhTtxizOGavxrV09oj4hI1LV7sJP4xpcv5329D5X726LKRkwAfFQ2ii1QM4Mc4tjmJZ2Sn-65t7Tth84DbRHRMtwH6M8Op5ZaYKHqtJARTtA_uAOVIfsTrlG-rbOhZaOBJp1Ct5HzEPSsEwjqRsnspmgBkCcPoMzXSOdlG5CHBEkmA7wWmYTKcuEvSMJ72qCxU4n-tOCPl8m9-eI8qaWQZ43_oYYBJoZB1uL98SJUB9uHIHJJ9_Y2iyxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور آمریکا، ونس : اینگونه فکر کنید که ترامپ با پست جزیره خارک به ایران پیام خودش را داد @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21851" target="_blank">📅 19:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21850">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTySX7V8iBOnvBcUByzoEvBjBuDtQBKZlbNah-PSzBfmYCEr12Q9aVSMtEczuDN0HkCdPsCcIwRdtYu4yShId0aYYTIecFgbCb4oypsbY592MKKX47WUMRIf_nn3vGP0Zlqu03vWiNNm8rUIJf--PXoRjbmk7WQxWXomXxQNBxNBtcjkO1hL7Pnq8b05FkkFvvchbqm2ZmvJ0RGTmJmFNdNXWp2y8cTGjingajDAP32vOCJF77fZbUTFfVddd351dENaqdSHLqwm9ZsMaJCdLwbKYHj6qH4dJmWbY-K-C8YLAy94tBIKBbnq5ME_8WVOsA64TMqKcanWU7vw_InEaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث ، بازنشر خبر بلومبرگ :
ایران با توقف تجارت با امارات، در معرض خطر از دست دادن شریان حیاتی اقتصادی خود قرار دارد…
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21850" target="_blank">📅 19:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21849">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ در تروث  : جزیره خارک دارد به‌طور کامل به تکه‌پاره تبدیل (با خاک یکسان) می‌شود!!! @WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21849" target="_blank">📅 18:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21848">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فرماندار قشم : دو کشته و تعدادی مجروح در حمله آمریکایی به جزیره لارک در شب گذشته. @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21848" target="_blank">📅 18:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21847">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">منبع اسرائیلی: پس از تشدید اوضاع در خاورمیانه که شب گذشته رخ داد، فرماندهی جبهه داخلی آماده است تا این بار شاهد تشدید اوضاع در
نیز اسرائیل باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21847" target="_blank">📅 18:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21846">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نرخ دلار ۲۱۲،۰۰۰ تومان(سقف تاریخی)
دلار کف بازار ۲۱۴-۲۱۷ هزار تومان(سقف تاریخی)
تتر ۲۰۹،۵۰۰ تومان(سقف تاریخی)
بیتکوین ۷۷،۹۰۸ $
انس جهانی طلا ۴،۴۲۴ $
نفت برنت ۹۰،۷۹$
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨
۶ عصر تهران</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21846" target="_blank">📅 18:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21845">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awFooGqy-HfBqz7S875tFWOJBYAGHU6Qpj0i9TvZwB1OU9sw7OYwO5gk7hAgzM9osgwt2ZhutmKAITrIEXm7XALQSAY8lOWEmDIieI6TImEYt8E4-wCsuwAbvsE2XBm68CmWWQd7NvK0NMufYx7iEAuBQb2YsmG2Y9usN4EnXBJwHMTgERusFJRT_7Rm_gn-MMyA3AXd8iDmFK8zI3NpqHrCk8G8OfxB7a_V6HM-xC_6s0N-VsyXf0ICdLMFX3kibwz827cih0t0qpvmImsHfCldvot8HjvcHIrQNk9QKKVj1RK0ZQ-1L1HfeHZHK0dhvkaRfJi3_7TO8nMqean3IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ سوخترسان و جنگنده های پنهانکار در حال عملیات در تنگه هرمز - خلیج فارس
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21845" target="_blank">📅 18:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21844">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کانال ۱۳ اسرائیل گزارش داد موساد پیش از آغاز جنگ، طرحی مخفی برای سرنگونی جمهوری اسلامی با استفاده از نیروهای کرد آماده کرده بود. بر اساس این طرح، هزاران نیروی کرد برای آموزش به اسرائیل منتقل شده بودند تا پس از آغاز جنگ از مسیر عراق وارد مناطق کردنشین ایران شوند. قرار بود نیروی هوایی اسرائیل با حملات گسترده، مسیر ورود نیروهای کرد را باز کند. طراحان امیدوار بودند یک شکست نظامی اولیه برای جمهوری اسلامی، اعتراضات میلیونی در ایران را به دنبال داشته باشد و به فروپاشی رژیم منجر شود. اما سه روز پس از آغاز جنگ، این بخش از عملیات متوقف شد. یک مقام اسرائیلی به کانال ۱۳ گفت: «سه روز پس از آغاز عملیات، دستور رسید: انجام ندهید.» طبق این گزارش، مخالفت رجب طیب اردوغان و فشارهای جی‌دی ونس، معاون رئیس‌جمهور آمریکا، در توقف این طرح نقش داشت و دستور نهایی از سوی کاخ سفید صادر شد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21844" target="_blank">📅 17:39 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21843">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خبرگزاری CBS : ترامپ به شدت عصبانی است و می خواهد امشب به ایران حمله کند!
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21843" target="_blank">📅 17:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21842">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ea412ab5.mp4?token=GFBkVi6ZCLWrAZWfdavkLhxtD4nCwMAknGWn2BVZGcCMaQFjnxEYuWLDXtI6PhqIB9xMXpDVtgAqValD9ESeKbmOL1ZjMA30jtDyo8ip3KVFQaHPg44t-JZSrp40eoN9Sdf5oM6LfEi6buR3UCwbO0ZKL7UFRAY1qgrr7GYZXGCawpGdy-62e1QkWpCcJqeC0x7Hg0Meqg7lBA71yzRriOfugavSY_JJ7F2OMfbkxQCIM_txf-Kw7dpGi9bdgqxMp_E-7Xu40iHnSJyur9oBIpRFdQoDHcOj7CsXyvwDDgPxUbtHaW_DqUBc0nvM_xdAvjpfHu8rNphUHxSlJTbszA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ea412ab5.mp4?token=GFBkVi6ZCLWrAZWfdavkLhxtD4nCwMAknGWn2BVZGcCMaQFjnxEYuWLDXtI6PhqIB9xMXpDVtgAqValD9ESeKbmOL1ZjMA30jtDyo8ip3KVFQaHPg44t-JZSrp40eoN9Sdf5oM6LfEi6buR3UCwbO0ZKL7UFRAY1qgrr7GYZXGCawpGdy-62e1QkWpCcJqeC0x7Hg0Meqg7lBA71yzRriOfugavSY_JJ7F2OMfbkxQCIM_txf-Kw7dpGi9bdgqxMp_E-7Xu40iHnSJyur9oBIpRFdQoDHcOj7CsXyvwDDgPxUbtHaW_DqUBc0nvM_xdAvjpfHu8rNphUHxSlJTbszA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت: می‌خواهم از اتحادیه اروپا و بانک مرکزی اروپا بابت بیانیه قوی حمایت از عملیات‌های اقتصادی ما علیه رژیم ایران تشکر کنم.
با همدیگر
در این گروه حکومت وحشتناک ۴۷ ساله آن‌ها را به پایان خواهیم رساند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21842" target="_blank">📅 17:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21841">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGy0TsfJ41WScI2XXq7cTNPIpnLQT48KxKs3rXLbe4yJV4FFARaoCf-Yf7KLf8i9tesBU8GNKylvs0zkoAKcEbjtGFGJSVj4HX2a49dbafrWaN09BO73eZtwk_CLkpzAJFO_MNtC7WqftqwPujgQMQIlpS1EWmiY7_9KFcWamikEGKyNPhB0kRiQ2TZypUj8eIaqSCP3LaTp3fLCdz2eEfuL8n1Yw-L7IkndIQ3tksmFB0yCZ72KBz19JkVt4fde4aLGUSxFZxtLhkx7QDt47xCpUCrL-tXm8sWOPPj1t2Mw72pKdZr3s1NxIN1LI36MrT15gJMIbcByANMAOEGoqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت یاب سنتکام در پاسخبه خبر فیک پرس تی وی : هیچ کشتی در تنگه هرمز به مین برخورد نکرده است. این یکی دیگر از تلاش‌های سپاه پاسداران برای ارعاب کشتیرانی تجاری منطقه‌ای از طریق انتشار اطلاعات نادرست است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21841" target="_blank">📅 17:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21840">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ به شبکه فاکس نیوز: ما به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد.ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد. @WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21840" target="_blank">📅 17:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21839">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">@WarRoom
roo be jolo</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21839" target="_blank">📅 16:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21838">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21838" target="_blank">📅 16:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21837">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21837" target="_blank">📅 16:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21836">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7129ba04fe.mp4?token=ucklD6sXsKKNno7c3tmieUOjUwxorz5xqqPunw_TQPxEakGEo8j9V8gDWUv0vyBACIZQPDduV8fttRJyaF1rEb_B4p5dwQMUHA1ILY3WY-cHS8L8nFiKbVX_epva9Dmuzj2Zaj6naI5FYMNm5nu5CANkh4C_NXrB6Cd_vDjdtpQyUPuChHXQJ6x7DZnfhvs471OYA5W-CYlb3i75McqJf_PKeTtO14OooKq0-Wc8p0CoDyW0HCJWyQUJBHez7WAoXdrWc9vZHvH6p7pWvvdasRjf_wNDxgZ8_-0Suz0wty5D7KmoH6z6EKczOPXBf9nJe6Rr2YatROVktO2xlTRONQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7129ba04fe.mp4?token=ucklD6sXsKKNno7c3tmieUOjUwxorz5xqqPunw_TQPxEakGEo8j9V8gDWUv0vyBACIZQPDduV8fttRJyaF1rEb_B4p5dwQMUHA1ILY3WY-cHS8L8nFiKbVX_epva9Dmuzj2Zaj6naI5FYMNm5nu5CANkh4C_NXrB6Cd_vDjdtpQyUPuChHXQJ6x7DZnfhvs471OYA5W-CYlb3i75McqJf_PKeTtO14OooKq0-Wc8p0CoDyW0HCJWyQUJBHez7WAoXdrWc9vZHvH6p7pWvvdasRjf_wNDxgZ8_-0Suz0wty5D7KmoH6z6EKczOPXBf9nJe6Rr2YatROVktO2xlTRONQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسنت : «ایران تحریم‌ها را بسیار جدی گرفته است. رهبران ایران از وضعیت اقتصادی کشورشان شوکه شده‌اند.
ما شاهد صف‌های بنزین ۳ تا ۴ ساعته در ایران هستیم.»
ایران به دلیل اینکه از نظر اقتصادی در حال از دست دادن توان خود است، به اقدامات نظامی و خشونت‌آمیز روی آورده است
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21836" target="_blank">📅 16:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21835">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
فروپاشی کامل اقتصاد ایران ممکن است نهایت چند ماه طول بکشد
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21835" target="_blank">📅 16:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21834">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ به شبکه فاکس نیوز: ما به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد.ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد. @WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21834" target="_blank">📅 16:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21833">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ به شبکه فاکس نیوز: ما به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد.ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد. @WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21833" target="_blank">📅 16:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21832">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بیانیه جدید EASA : هشدار پروازی اروپا برای آسمان خلیج فارس؛
آژانس ایمنی هوانوردی اتحادیه اروپا (EASA) با انتشار یک بولتن امنیتی جدید، توصیه پرهیز از پرواز در حریم هوایی کشورهای امارات، قطر، بحرین، کویت و بخش‌هایی از دریای عمان را تمدید کرد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21832" target="_blank">📅 16:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21831">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45560d441c.mp4?token=gnFS2w_tAgmPse2drEUEFrSqUermVoNRtxym6h6BNlQNZQ3bImnOhjVH5Ae6ragpL2gzhUfzNiL-jLaYiCj6ZFrCANcBl0ydWTCJ7vNZ88Xs9VOtJu_sZ0HUImsECupilgQGUm7CN9d0q0z1sZEtJxmgDZdgeYfmqyAzmargJ0zAuJkUvs5weBycBEKITCHFDGpHMpHJ6eTgvQv3ypgc6tg2qLzjqS75qMZLWnrJnPCwj75bhiDtkn-8Poj8j1afC2xeyOrYFP0JiO_gQL9GZ9tLbO7doiA5MPcJNuSKc_BHphoPgo8LhAUCgF5extaP12y0MkLr1A-8z6yqE4P3Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45560d441c.mp4?token=gnFS2w_tAgmPse2drEUEFrSqUermVoNRtxym6h6BNlQNZQ3bImnOhjVH5Ae6ragpL2gzhUfzNiL-jLaYiCj6ZFrCANcBl0ydWTCJ7vNZ88Xs9VOtJu_sZ0HUImsECupilgQGUm7CN9d0q0z1sZEtJxmgDZdgeYfmqyAzmargJ0zAuJkUvs5weBycBEKITCHFDGpHMpHJ6eTgvQv3ypgc6tg2qLzjqS75qMZLWnrJnPCwj75bhiDtkn-8Poj8j1afC2xeyOrYFP0JiO_gQL9GZ9tLbO7doiA5MPcJNuSKc_BHphoPgo8LhAUCgF5extaP12y0MkLr1A-8z6yqE4P3Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به شبکه فاکس نیوز: ما به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد.ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21831" target="_blank">📅 16:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21830">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21830" target="_blank">📅 16:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21829">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ompMv8TKQNJ8Pi4sr7urD-IwdEoQGwHJLpNVvggiqOQH7w2TfMrjbpygW7YHWw817V8LMPgYms5RUN2R3fL-uX6I2MVsacixkrhgRjumS3PAncAihNpZKKo-fuJT7I2LoBQjjrnwWLr2opl9OZZpT8EUeZ9ss5-P5Xle2lTLP7_7b4n4TsJyCz5OGGqOGHknq8ecBAEtx9wpEW2QQ89cE-zr8GVrqm2UJjmgbGaq8cmV90GAcBRkHyebGhYHbawf2IOKNMsXm4ekdAZ45U263IeOmp3nRV5TTnfdmJXs-OURMjVLe6rE-eMIRAoJgMlYOOriC7zHZIVk1eqzyNLlYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «ایران رسماً یک
کشور شکست‌خورده
است.
ایران مُرده است!
آنها نیروی دریایی ندارند، نیروی هوایی ندارند، پول و ارز ندارند، حقوق سربازان و نیروهای پلیس خود را پرداخت نمی‌کنند، تورم به
۳۰۰ درصد
رسیده است و رهبری کشور کاملاً دچار آشفتگی و سردرگمی است و توانایی نمایندگی درست و شایسته کشور را ندارد.
تنها چیزی که دارند،
اخبار جعلی از آمریکا
، آمادگی برای کشتن معترضان خودشان است (اکنون بیش از
۱۰۰ هزار نفر کشته شده‌اند
. آنها باید به دلیل
جنایات جنگی و جنایت علیه بشریت
محاکمه شوند!) و البته یک خط خوب از
«چرندیات»
است
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21829" target="_blank">📅 15:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21828">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فرماندار قشم : دو کشته و تعدادی مجروح در حمله آمریکایی به جزیره لارک در شب گذشته.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21828" target="_blank">📅 15:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21827">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ در تروث  : جزیره خارک دارد به‌طور کامل به تکه‌پاره تبدیل (با خاک یکسان) می‌شود!!! @WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21827" target="_blank">📅 15:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21826">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCL8-pmfA-2T-5oNhlSqRBF3EH8KasXMOjle1_qqz-z8yaqP9Nwd8p6ALEFNp8AQ-i94Gobs-6wk9MHQaYFM0Cpi_mpbinzAeL_ephg7msypCJdsxqU9Nck-QtTYt-Zxw565n_u8ZmZhNy5ugY45vlK-XWHtQNjZlbEl1cwBK72Na5OwQihxN7jpqxXIW-YlT2mK7W6-PM3Us0JuBfG4J39c38jZMierNfjVlV-BCLA74N2B-7Bjc8RiNT-WHk5HF-YFrjJtH8Z8YUjpDPNmTFFCUwBEzcKGe43D4QjX6WdE2tZtFqil7hdkMpgUzKjDZZentrUsY1gZy6QA_jTnwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک جت جنگنده رادارگریز F-35A نیروی هوایی ایالات متحده هنگام گشت‌زنی در آسمان خاورمیانه، بر فراز آب‌های خلیج فارس پرواز می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21826" target="_blank">📅 15:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21825">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ادعای تانکر ترکرز : تنها کسی که انتقال محموله‌های STS (کشتی به کشتی) را در تنگه هرمز انجام می‌دهند، خود ایرانی‌ها هستند
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21825" target="_blank">📅 13:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21824">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نرخ دلار ۲۰۹،۶۰۰ تومان(سقف تاریخی) دلار کف بازار ۲۱۲-۲۱۵ هزار تومان(سقف تاریخی) تتر ۲۰۸،۴۰۰ تومان(سقف تاریخی) بیتکوین ۷۸،۶۳۴ $ انس جهانی طلا ۴،۴۴۱ $ نفت برنت ۹۱،۰۷$ @WarRoom
🚨
🚨
🚨
🚨
🚨
۱ ظهر تهران</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21824" target="_blank">📅 13:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21823">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Izt5SWWLtcL8NI-BZ3tfcvS8vmTTtz2tXTKBTx01zdTMqHigxNKSqcM2CF6rdILYtf-NLIpqIaKWPA7qNleQgXQFywW6epb_a6l9VoC6mQEjEMkeMpUQjT26BuYIZOY83BkAdoo9V8eILlROGQRrejJcknNIoJ3onPXCegnzmwUL51Ui3td91DfcRx01MtAmXfub_oD6OWU-WBh8GzePg8ZIzQQ_c5x3xloEyvYQv1LZAO_ipO2wFmAy1-BeRFMgYmQA7C3Uwk47KZayR3yn7VWlljpmcKPmK93hh-_bgaw7NMQTUH6PYXMu9no5_HjXgUPFVsH7aamrW0-Y6NkJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار ۲۰۹،۶۰۰ تومان(سقف تاریخی)
دلار کف بازار ۲۱۲-۲۱۵ هزار تومان(سقف تاریخی)
تتر ۲۰۸،۴۰۰ تومان(سقف تاریخی)
بیتکوین ۷۸،۶۳۴ $
انس جهانی طلا ۴،۴۴۱ $
نفت برنت ۹۱،۰۷$
@WarRoom
🚨
🚨
🚨
🚨
🚨
۱ ظهر تهران</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21823" target="_blank">📅 13:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21822">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ درباره ایران: «ما کمک بسیار کمی از کشورهای دیگر دریافت می‌کنیم، در حالی که خودمان به کشورهای دیگر کمک می‌کنیم. ما
میلیاردها و میلیاردها دلار
برای کمک به ناتو و کشورهای دیگر، از جمله کره جنوبی، هزینه می‌کنیم. ما به آنها کمک می‌کنیم، اما وقتی نوبت به کمک به ما رسید، من زیاد اصرار نکردم؛ فقط پرسیدم: «آیا مایل هستید مشارکت کنید؟» و همه آنها گفتند: «نه، متشکریم.»
و من با خودم گفتم:
این موضوع را به خاطر خواهم سپرد
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21822" target="_blank">📅 12:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21821">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اسرائیل و یونان قراردادی دفاعی به ارزش تقریبی 3 میلیارد یورو امضا کردند تا یک سیستم دفاع هوایی چند لایه برای اسرائیل در یونان ایجاد کنند. این سیستم برای مقابله با موشک‌ها، پهپادها و سایر تهدیدات هوایی احتمالی از ایران و ترکیه طراحی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21821" target="_blank">📅 12:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21820">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taa-9yq-W-sVheBxbnQMkScQXcTl9xZoFfgQ0zJ7T_w29gXjSETn8sC4rs9ipiNYx_uwvBDimYB98eGwjZwT2mxBtvjUMnZGlDaVE9evtNkfUhmcQc54CCwubM_sbVCPFFA-4t8AHSpng7BergVLDIzw-Dd9xJOs0ibkA8Zr7pc8B8-h5jQJ9XQk7ddGjNbmusVFV-vflK9BlX6AvLJZ30EYd1ws4gNX61GhFi2PevQ4O4Mx_eCU72xD2lh9OYmr__beafBYFiF3Z_bWMVBJJjMnkHOzxAsPlx82GZuPJi36692mAz3JKaFq6IvwjWnJ5cigc7HILsT_kEOlRdYFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه , عراقچی:
نتانیاهو با افتخار می‌گوید که موفق شده است دولت آمریکا را متقاعد کند تا به جای اسرائیل، علیه ایران جنگی را آغاز کند
. او در حالی که می‌خندد، درباره "تاثیر" خود بر ایالات متحده صحبت می‌کند، تاثیر ناشی از بیش از 1000 ساعت حضور در شبکه‌های تلویزیونی آن کشور. در عین حال، او با زبان انگلیسی، از رهبری ترامپ تمجید می‌کند.
او یک مار است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21820" target="_blank">📅 12:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21819">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سخنگوی وزارت امور خارجه، کاظم دست کج غریب‌آبادی:
این اقدامات تهاجمی، پاسخ مناسبی را دریافت خواهند کرد.
باید حضور بیگانگان در این منطقه از بین برود، و آنها باید درس‌های جدی بگیرند تا از تکرار اقدامات تهاجمی خود علیه کشور ما خودداری کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21819" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21818">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نیویورک تایمز به نقل از مقامات آمریکایی:
نیروهای ما تنگه هرمز را تحت نظارت دارند و آماده‌اند تا به نیروهای ایرانی که امنیت کشتیرانی را تهدید می‌کنند، حمله کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21818" target="_blank">📅 11:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21817">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اتاق جنگ با یاشار : رسانه‌ها به طرز عجیبی جدیداً قسمت صحبت‌های ترامپ که در مورد کشتار معترضان هست را حذف سیستماتیک می‌کنند. در صورت مشاهده رگباری گازعنبری برخورد کنید. @WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21817" target="_blank">📅 10:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21816">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">امروز اگه بازار بودین از صف های صرافی‌ها و پمپ بنزین ها ویدیو درست و تمیز بگیرید ، همچنین محکم کاری کنید و حرفی در ویدیو نزنید دقت کنید تصویر خودتون در رفلکس شیشه یا آینه نیفته و ماشینتونن هم معلوم نباشه و دایرکت چنل ارسال کنید
@WaRroom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21816" target="_blank">📅 10:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21815">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11404cd66.mp4?token=f80cBWzQaqoXYr_6XIKRsK5iz1S5O9FZZQH4BmE87Vt7qjU6BgaWuy0_OAiPWeIc_Zh6_NAox_SqaTSKBkSFybxdMXEKJg6sNt1s09HjfKIXtFRkJ4zRPsDuwsgUANZyQu7yCEmpbbYg3Wi3mG63DJW-Bv8ejIvcJ30xGafPKgyoBQgqNRIPUIX4Hz48JJ4YdRvsILSTr-nq084MfjqcA-M2Ix-mRyDk708zvjE1fkdcYT_iOJW9faACo2I9fLFZNim73B4UI7Zxicr0OszN9CahdtO1huJh5x_xF6RdCpLnbf-Bf7GDnb3xbI5RgEmkDQy3RwA5PTP9X-w1-tg9Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11404cd66.mp4?token=f80cBWzQaqoXYr_6XIKRsK5iz1S5O9FZZQH4BmE87Vt7qjU6BgaWuy0_OAiPWeIc_Zh6_NAox_SqaTSKBkSFybxdMXEKJg6sNt1s09HjfKIXtFRkJ4zRPsDuwsgUANZyQu7yCEmpbbYg3Wi3mG63DJW-Bv8ejIvcJ30xGafPKgyoBQgqNRIPUIX4Hz48JJ4YdRvsILSTr-nq084MfjqcA-M2Ix-mRyDk708zvjE1fkdcYT_iOJW9faACo2I9fLFZNim73B4UI7Zxicr0OszN9CahdtO1huJh5x_xF6RdCpLnbf-Bf7GDnb3xbI5RgEmkDQy3RwA5PTP9X-w1-tg9Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
به‌محض اینکه در جنگ با ایران پیروز شویم، قیمت نفت مثل یک موشک به‌شدت پایین خواهد آمد.
ما همین حالا تقریباً کنترل کامل بر تنگه هرمز را در اختیار داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21815" target="_blank">📅 10:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21814">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزارت دفاع امارات ادعا کرد که نیروی هوایی این کشور، یک پهپاد را در بدو ورود به آب‌های سرزمینی خود مورد هدف قرار داده
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21814" target="_blank">📅 10:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21813">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ به فاکس نیوز: آنها رژیمی سرسخت و باهوش هستند، اما بسیار شرورند. آنها ۵۲،۰۰۰ معترض را در چند ماه کشتند  اینها رژیمی بسیار خشن و شرور هستند و اگر سلاح هسته‌ای داشتند، اسرائیل دیگر وجود نداشت. اگر من رئیس‌جمهور نبودم، اسرائیل از بین رفته بود. دیگر اسرائیلی…</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21813" target="_blank">📅 09:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21812">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7948962027.mp4?token=SrWjRPHuR7vmT6rZBwld0GZhOOVtDtq6DS2jFYJH0WTVU6zTkhaB0z-TYCSXvZ4PghN4p4GZz0kvtbZGQ62st9SUM218W6ivh7drHRYOfdRR5T_kFwZCuUGbRWPXXnwGAw4mvDsixed-0We7PJ-XhMdGpA6d1dveb9oVdFKj7BpCHIqaRdd4jwdB7zWewS47EaHFCUMHz5pLKTuG0dTYXczhYzew8gTVScfAn32ef3O34devRpBiZPleresexFx7wIKxYRbPt6VtCfn-LcWJ3nfryf-ozr5UTzMAtJ5gdD7Pyxg0VmyQRVuhKpZq-YqAhjo7BuDQhCUv_626RWi2hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7948962027.mp4?token=SrWjRPHuR7vmT6rZBwld0GZhOOVtDtq6DS2jFYJH0WTVU6zTkhaB0z-TYCSXvZ4PghN4p4GZz0kvtbZGQ62st9SUM218W6ivh7drHRYOfdRR5T_kFwZCuUGbRWPXXnwGAw4mvDsixed-0We7PJ-XhMdGpA6d1dveb9oVdFKj7BpCHIqaRdd4jwdB7zWewS47EaHFCUMHz5pLKTuG0dTYXczhYzew8gTVScfAn32ef3O34devRpBiZPleresexFx7wIKxYRbPt6VtCfn-LcWJ3nfryf-ozr5UTzMAtJ5gdD7Pyxg0VmyQRVuhKpZq-YqAhjo7BuDQhCUv_626RWi2hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمونه‌ای از شیوه استقرار مین‌های دریایی توسط سپاه در خلیج فارس؛ راکت فجر-۵ با کالیبر ۳۳۳ میلی‌متر که به‌جای سرجنگی استاندارد، حامل محموله‌ای از مین‌های دریایی است. شب گذشته نیز احتمالا سامانه‌ای مشابه در جزیره لارک هدف قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21812" target="_blank">📅 09:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21811">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78dd13214.mp4?token=AMw_40Hx-Uglso52ERVXmClGmH6K6nUVIO6JtjKt3tHbP9-mPY7WRmL-TlOyYDxzUOnJILwpmzR4c8zqYMev_HqRvhNQPDXKi185NvuWoG8gNwcttXBSICivP_TGUg78Pjs5oBPbmuzAdpIxuuISAztyDJnTgffYAkE_gZQfTIABToRGX0phFWAJ-UmrorF2emyLGk12Lb2awoC3plR7l1toj6CsALQuRQoZorSSZz8FrjLsxEyCxzSrdIVvLrenB9gAb1PG1G3JSVd5O7vtc_aClrpQKPSnvBvNwWLH1rNvObP89PcF8i--Jp_YvKp_FOvS6Dmw_Gprs9BRK03esTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78dd13214.mp4?token=AMw_40Hx-Uglso52ERVXmClGmH6K6nUVIO6JtjKt3tHbP9-mPY7WRmL-TlOyYDxzUOnJILwpmzR4c8zqYMev_HqRvhNQPDXKi185NvuWoG8gNwcttXBSICivP_TGUg78Pjs5oBPbmuzAdpIxuuISAztyDJnTgffYAkE_gZQfTIABToRGX0phFWAJ-UmrorF2emyLGk12Lb2awoC3plR7l1toj6CsALQuRQoZorSSZz8FrjLsxEyCxzSrdIVvLrenB9gAb1PG1G3JSVd5O7vtc_aClrpQKPSnvBvNwWLH1rNvObP89PcF8i--Jp_YvKp_FOvS6Dmw_Gprs9BRK03esTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
دموکرات‌ها می‌خواهند کشور ما در جنگ با ایران شکست بخورد؛ اما این اتفاق نخواهد افتاد، چون ما به‌طور مطلق و به‌راحتی در حال پیروز شدن هستیم.
تحریم های اقتصادی کمرشان را شکسته آنها محکوم به شکستند و در زمان مناسب، یا ما پیروز خواهیم شد، یا آنها دست به اقدامی خواهند زد.
من با پیروز شدن مشکلی ندارم. نیازی ندارم که امضای آنها پای یک تکه کاغذ باشد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21811" target="_blank">📅 09:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21810">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa60f768ab.mp4?token=SPuNCkaHfbmI2lrKQfZBx_M-Rz3AgG5TIYvwA_2g8Fo5K05EFj5Cp3ewapVL0BiPRraPs6xNjAWRW_Wk4vcs6OGKs91ZMaVxB7iOhekSZ2pH9OtGv-rgu1XabWKbAuR6p_rEBlOiJj0Bx4yEXC9Nvsfy62RQUXL01p5XEV_Nx36bU2FFcwXeYVHgyFMs2joZ9BIqGVOuZlUXZC_C3s04JTkiOAw0_FJrBceIS3HPpgnURzurn1FuZA4OJRWYj-NgfemVAD7gvxsIJ8Map1ndlrXH3sLUaqbwzprwdyftl6Z9xNzjvtLyr7HSx5iHItlR1TkrAPAqMGiWrgQ1Esa5zpDOB0GPjwy2YrTaZNnWJ33k6mf0AtJrZsYFcWakEXqHfL1zFHQbOst0xEcjT3XaQaNhA0wJ7UxUZzfUxcSGJA7R_PJq6p0N9ymShqE1ZnhmMTLG6kl7rEKTPEbBnjWK2b0UBZJAY6-ZSpwte9b9nddQ45VMVsZVj6fvlPIxAPdGkb3D0vm_37LV_IzWClXPwUibU-HKsmBfxYYpdwpAfZ0Dt0gFs3AHTaI6tMzfHG2boqJr0f6JPghc3onrB7Lj-d34sCAVv5OgK6fPUKfDWPCVZrkaI4-YOiw-C2wRBs3XXIXt2Xwrr92VSfeGqV9E-r3QBNWeY8hkw59pTmPgyVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa60f768ab.mp4?token=SPuNCkaHfbmI2lrKQfZBx_M-Rz3AgG5TIYvwA_2g8Fo5K05EFj5Cp3ewapVL0BiPRraPs6xNjAWRW_Wk4vcs6OGKs91ZMaVxB7iOhekSZ2pH9OtGv-rgu1XabWKbAuR6p_rEBlOiJj0Bx4yEXC9Nvsfy62RQUXL01p5XEV_Nx36bU2FFcwXeYVHgyFMs2joZ9BIqGVOuZlUXZC_C3s04JTkiOAw0_FJrBceIS3HPpgnURzurn1FuZA4OJRWYj-NgfemVAD7gvxsIJ8Map1ndlrXH3sLUaqbwzprwdyftl6Z9xNzjvtLyr7HSx5iHItlR1TkrAPAqMGiWrgQ1Esa5zpDOB0GPjwy2YrTaZNnWJ33k6mf0AtJrZsYFcWakEXqHfL1zFHQbOst0xEcjT3XaQaNhA0wJ7UxUZzfUxcSGJA7R_PJq6p0N9ymShqE1ZnhmMTLG6kl7rEKTPEbBnjWK2b0UBZJAY6-ZSpwte9b9nddQ45VMVsZVj6fvlPIxAPdGkb3D0vm_37LV_IzWClXPwUibU-HKsmBfxYYpdwpAfZ0Dt0gFs3AHTaI6tMzfHG2boqJr0f6JPghc3onrB7Lj-d34sCAVv5OgK6fPUKfDWPCVZrkaI4-YOiw-C2wRBs3XXIXt2Xwrr92VSfeGqV9E-r3QBNWeY8hkw59pTmPgyVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
به فاکس نیوز
:
ایران در ابتدا جنگ به کشورهایی حمله کرد که به‌نوعی بی‌طرف بودند؛ عربستان سعودی، قطر، امارات متحده عربی، بحرین و کویت.
همه شوکه شدند. من هم تعجب کردم. فکر کردم این اتفاق از یک جهت خیلی خوب بود، چون آنها تمام حمایتی را که داشتند از دست دادند. آنها تا پیش از آن، تا حدی از حمایت برخوردار بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21810" target="_blank">📅 09:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21809">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4845fda47.mp4?token=W124V48z7ZRT5obS2bLdGmgIVKzrOq6CS_BIxs15p4s00fZ-Ob32aGxR4XPrF4vC0H89D6n9RkjRyaD5ryNpG8YfIFiDSL7I-5ZrWh221xcieI2MkD4Ex18briNVner7KWULrsJyTR8hyLkk6q1n4-gDdxoPYbI6d4PywuTwXm3A-n-UTMYmbvWs_VHR9Ppz9Vq_aNIOXQbHlv-UwQUQdYbiFcTaPsO17n6tgTIJAmiFwZje8S3O2fKDrT7vlC5Tne8sPMZ2UovnYGu__HHpeKJ1rN_Z9-eflzvdUXQqy-6ZuBEyYWrKVhXggCtOOwI4mgbJCSScAGFtRukBFgDa_6mX3kUBnVNcNLAzOoDY-xqP7b6m8YMgVcxRR_Qx6p6xb70tXVAg2E_VQs0hRFTUGMGgZcXdnE31KSzuaetMr8jaTkJagDayC5bOUnIhBCQpvAaIhKKI_Cz-nc0PdCyQ_DcrlqFzouEpNvGuaWMo6P3BhzL4iRCJjWMiyMQGiT_tDcWY4u0ouY0DXnJ4orAwi9Zmsf-n84mLzHGyrFOe4PKLgP_XpeJAN9Umz15Y_jmrrSAlQ2deusSOGYFwB2B36u4wJ-hh2PcWdol9BhRnzM6EgKqQ-ZbfdLluL073E-mk8E5gy_e7E8qfkH9703sSLmSa0SUZyVpmtgFbdI71a94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4845fda47.mp4?token=W124V48z7ZRT5obS2bLdGmgIVKzrOq6CS_BIxs15p4s00fZ-Ob32aGxR4XPrF4vC0H89D6n9RkjRyaD5ryNpG8YfIFiDSL7I-5ZrWh221xcieI2MkD4Ex18briNVner7KWULrsJyTR8hyLkk6q1n4-gDdxoPYbI6d4PywuTwXm3A-n-UTMYmbvWs_VHR9Ppz9Vq_aNIOXQbHlv-UwQUQdYbiFcTaPsO17n6tgTIJAmiFwZje8S3O2fKDrT7vlC5Tne8sPMZ2UovnYGu__HHpeKJ1rN_Z9-eflzvdUXQqy-6ZuBEyYWrKVhXggCtOOwI4mgbJCSScAGFtRukBFgDa_6mX3kUBnVNcNLAzOoDY-xqP7b6m8YMgVcxRR_Qx6p6xb70tXVAg2E_VQs0hRFTUGMGgZcXdnE31KSzuaetMr8jaTkJagDayC5bOUnIhBCQpvAaIhKKI_Cz-nc0PdCyQ_DcrlqFzouEpNvGuaWMo6P3BhzL4iRCJjWMiyMQGiT_tDcWY4u0ouY0DXnJ4orAwi9Zmsf-n84mLzHGyrFOe4PKLgP_XpeJAN9Umz15Y_jmrrSAlQ2deusSOGYFwB2B36u4wJ-hh2PcWdol9BhRnzM6EgKqQ-ZbfdLluL073E-mk8E5gy_e7E8qfkH9703sSLmSa0SUZyVpmtgFbdI71a94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
به فاکس نیوز
:
آنها رژیمی سرسخت و باهوش هستند، اما بسیار شرورند.
آنها ۵۲،۰۰۰ معترض را در چند ماه کشتند
اینها رژیمی بسیار خشن و شرور هستند و اگر سلاح هسته‌ای داشتند، اسرائیل دیگر وجود نداشت.
اگر من رئیس‌جمهور نبودم، اسرائیل از بین رفته بود. دیگر اسرائیلی وجود نداشت
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21809" target="_blank">📅 09:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21808">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d72b70a62.mp4?token=BcSLj6n-1sF0MymQvtGSEnPmpOfGGjbgv_iHKJuGN5cjBIP6OX-WyE8DT0ERloURwCUS9GS8W9P40SlTRncMQ9tBz7dByxmyJtwPcyYhywO5UnG5WfSBYaH_ZBP1sjD_5T0hi60WldKyiiaaTVHIrnnVfBvJkNLl_BXE6XuM0lhwHdoa_51r0WzUTooW0AFBYrPo4p2nVzRAesWG8t93z-8Ue99GXNM8vOAsglDBeSBFkd1yhB0GAqQxu3H1gTi6ZiPA5Ph2n6vaGNAvwebNfT7ZhBFUW0BmfuZsJrG8ya_tqx2SNSM9LFqLBFGuQSuutRsGVfRkcy0Go19HORkhdTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d72b70a62.mp4?token=BcSLj6n-1sF0MymQvtGSEnPmpOfGGjbgv_iHKJuGN5cjBIP6OX-WyE8DT0ERloURwCUS9GS8W9P40SlTRncMQ9tBz7dByxmyJtwPcyYhywO5UnG5WfSBYaH_ZBP1sjD_5T0hi60WldKyiiaaTVHIrnnVfBvJkNLl_BXE6XuM0lhwHdoa_51r0WzUTooW0AFBYrPo4p2nVzRAesWG8t93z-8Ue99GXNM8vOAsglDBeSBFkd1yhB0GAqQxu3H1gTi6ZiPA5Ph2n6vaGNAvwebNfT7ZhBFUW0BmfuZsJrG8ya_tqx2SNSM9LFqLBFGuQSuutRsGVfRkcy0Go19HORkhdTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به فاکس نیوز
:
تماشای واکنش سریع نیروهای آمریکایی و موفقیت آنها در رهگیری آتش ورودی «در لحظه و به‌صورت زنده، شگفت‌انگیز» بوده برایم!
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21808" target="_blank">📅 09:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21807">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6da7ebc4e.mp4?token=qD1ZJci1Zvf5FR5wGnYEJDqdgKckxLzhNnL6iTyRNxTxWEn1RbNuBQhUGUVy9Arkf2Rn2FF2kl0_u0V6kvS2HQUMXu6qeL9OT07thJPFkMCvhsWFR_NaxhMJYx037sd5Mu31bDb62i6s-RDe_TaRnnXCJK9TYU5vbvak9zBfDJQfb4MWm9n8qikemppgvFUROvJadJwLyAd9pJtwPzVmDVV6S_jBOB1EJL3Unpa8m1lzrpoOamXEV282m_nDfQyBrKTgp0he0bRgREYjP3jfwhqLGHtXwXLXY6EdYAjN15HhR0yPiXaIrieQCspVbAtCuz1HgIEIeZzn_nGNFjM8Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6da7ebc4e.mp4?token=qD1ZJci1Zvf5FR5wGnYEJDqdgKckxLzhNnL6iTyRNxTxWEn1RbNuBQhUGUVy9Arkf2Rn2FF2kl0_u0V6kvS2HQUMXu6qeL9OT07thJPFkMCvhsWFR_NaxhMJYx037sd5Mu31bDb62i6s-RDe_TaRnnXCJK9TYU5vbvak9zBfDJQfb4MWm9n8qikemppgvFUROvJadJwLyAd9pJtwPzVmDVV6S_jBOB1EJL3Unpa8m1lzrpoOamXEV282m_nDfQyBrKTgp0he0bRgREYjP3jfwhqLGHtXwXLXY6EdYAjN15HhR0yPiXaIrieQCspVbAtCuz1HgIEIeZzn_nGNFjM8Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در تروث  : جزیره خارک دارد به‌طور کامل به تکه‌پاره تبدیل (با خاک یکسان) می‌شود!!!
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21807" target="_blank">📅 09:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21806">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حقیقت یاب سنتکام : نیروهای آمریکایی اقدامات محدود و دقیقی را علیه نیروهای سپاه پاسداران که در حال نصب مین در تنگه هرمز بودند و تهدیدی فوری ایجاد می‌کردند، انجام دادند. به عبارت دیگر، ایران این تهدید را ایجاد کرد و ارتش ایالات متحده آن را از بین برد تا از دریانوردان غیرنظامی، کشتی‌های تجاری و جریان آزاد تجارت جهانی محافظت کند
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21806" target="_blank">📅 08:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21805">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عراقچی همراه پزشکیان
به منظور شرکت در نشست سران سازمان همکاری شانگهای عازم قرقیزستان شدند
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/21805" target="_blank">📅 08:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21804">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بیانیه سپاه : «یک نفتکش غول‌پیکر ناسازگار که می‌کوشید از مسیر جنوبی غیرقانونی تنگه هرمز بگذرد، با دو مین دریایی برخورد کرد، آتش‌سوزی گسترده‌ای رخ داد و کاملاً متوقف شد.»
سپاه پاسداران هشدار داد دیگر شناورهایی که قواعد امنیتی آن را نقض کنند با همین سرنوشت روبه‌رو می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21804" target="_blank">📅 08:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21803">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNWMKyyFXBiI9ehewt6GD2i9iJGExxZzM67B-oChq-oQmKePtgltwD_l8ZMs9SW_YLiijIr8JTtlfq6apJusy0fwS-VF1ZF0351vm6LDFRWOIbvBQBbXUN9-uFYfXhwK05FVHBcSq82LG18lmAdHNA1BhkdnT6Jh4pRIbPqwCJbN46WbCVuuYyIfIKzGHWvtuWx6A_xZJdOeMGN29e0jvR1Wdi8FEOtEb5v31e9Nch9CgvKcbGA6JSEdz2uShQuHZnAv8tQ84jFew2YqBouyW3V-ikqN0Xpj3TuaVQVxFkn2bRxLHdlI8Oi88FI1MzRj9-q6c4ac_JyrqPmzePPl4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حال حاظر بر خلاف رسانههای رژیم که گفتمد هواپیما های امریکایی از منطقه فرار کردند،  ۴ سوخترسان که همه آنها از قطر بلند شده‌اند، مشغول عملیات بر روی تنگه هرمز هستند و یک سوخترسان هم از اسرائیل به سمت خلیج فارس در حرکت است.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/21803" target="_blank">📅 03:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21802">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/21802" target="_blank">📅 03:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21801">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCU-RgBbEMzMkLWhue82Y7279009mClgfFrW6nQXMWC5fN69JgSzRx5ESjNpzaf7TGZp2VuH8aZONSNB0h8bGtcMSdZRo3J6sp12A8t_sXKaq6nY1_fFYNX1gG3PKqzpLotbhsIu_vKXvcFWPy-BQgTK2q4RaAdQ2xZGZ-cS_33aEsWQYbwh4yNb5am3FrAoYutBJrMe-TB7A6uSdlDQDA91Tv3yhDqfXX8oRjU3sfs5YBn2wjlmEzguJ2r2bIHQ3QtOJfv-GAunpN_Retg4uqUVD5wRwqlIrM-x5Fb4DgRAMlTnREe0zWoyHFgVK2XCC27P71j0bNf1lPqdoJmZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز فلای‌کیش‌که از مهراباد داره میاد امام ! آیا دارن تخلیه میکنند مهرآبادو ؟!
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/21801" target="_blank">📅 03:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21800">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گزارش صدای‌انفجار از تنگه
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/21800" target="_blank">📅 03:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21799">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ارتش اردن در بیانیه‌ای ادعا کرد که ۸ موشک را پس از نفوذ به حریم هوایی این کشور رهگیری کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/21799" target="_blank">📅 03:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21798">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کانال 14 اسرائیل : تو حمله هوایی آمریکا به لارک ایران ده‌ها نفر از پرسنل سپاه پاسداران کشته و حدود ۱۰۰ نفر دیگه هم زخمی شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/21798" target="_blank">📅 02:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21797">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/21797" target="_blank">📅 02:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21796">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLS0q2pOO_gFzkiGP9mRj4VV-gmxHgpAAMAl_lLza40K8rCR6ZfCwC_1n0iWgY1nfTI9BJ80SlzBGGp1J9xfpfsxga-KGzkbjx0vIgKc928bD6ZJQmrWOFrI0Y2Dp5aZnPmewnyTakqV7FKK3k0RRjvF4AEPv3fg6HyvP7_y9uGWCUquUJnGm8N2bUJ-pHXVAb2oasUaloyxrfHn0ycyWE2WbQlg89PhhsI3-ITCqHkn-vq1JLGEx8HV8vpOJr4UDxzi7D9zqpoOBgeRMbKuVqW2yaGDKV-QKqAJiMivKbayKzUxVX_jMzXe_v6zWbBRdvNazjSfUOKBMaiOVNcUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/21796" target="_blank">📅 02:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21795">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فردا ملت همیشه در صف ، در پمپ بنزین و صرافی ها ! قیامت می کنند
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/21795" target="_blank">📅 02:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21793">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89022fc40e.mp4?token=VYtBSf7-sW-JUfvFHSTb6AtwRxwI6xSVbYpPRmzatZ34iJX2IbLtpVEnTbOMpfuJXLoPw7wduyLj5qhvvL0Ywta75TfeFqC_WJK2l6EdXNLsdI9sMwbqYW8wQb6l0uSpcB_syD5L9Phq3qEO0JckGjMWdB3WwArjY_L8zrIq8viHPkRFnKtgyC1ZDh9KngUISVJWU8FeodE47looI6pwUctJsQyS8nUMeLX4bP3lixnzhiL-RHdLTaGoXLA_5of18VWG_UMFeKZkG8fKXEE8n_z5looBaX5G7TId3eLNegxS0hbl5mzV6xQpxx6Zk1fLX1mEhd6ykPIV00O9Bik-AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89022fc40e.mp4?token=VYtBSf7-sW-JUfvFHSTb6AtwRxwI6xSVbYpPRmzatZ34iJX2IbLtpVEnTbOMpfuJXLoPw7wduyLj5qhvvL0Ywta75TfeFqC_WJK2l6EdXNLsdI9sMwbqYW8wQb6l0uSpcB_syD5L9Phq3qEO0JckGjMWdB3WwArjY_L8zrIq8viHPkRFnKtgyC1ZDh9KngUISVJWU8FeodE47looI6pwUctJsQyS8nUMeLX4bP3lixnzhiL-RHdLTaGoXLA_5of18VWG_UMFeKZkG8fKXEE8n_z5looBaX5G7TId3eLNegxS0hbl5mzV6xQpxx6Zk1fLX1mEhd6ykPIV00O9Bik-AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی سپاه با این ویدیو تایید کرد فقط اردن رو زده و نام عملیات امشب تنبیه متجاوز بوده
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/21793" target="_blank">📅 02:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21792">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">چنل‌تلگرام رو پین کنید بالا حتما و نتفیکیشن های اینستاگرام رو هم روشن کنید کاملا ، چنل یوتبوب رو ساب کنید این هفته هر جور شده استارت میزنم   https://youtube.com/yasharrapfa</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/21792" target="_blank">📅 02:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21791">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یک منبع آمریکایی به فاکس نیوز گفت:
تاکنون تأثیرات جدی‌ای مشاهده نشده است. تقریباً تمام موشک‌های شلیک‌شده تا این لحظه مورد هدف قرار گرفته و منهدم شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/21791" target="_blank">📅 02:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21790">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/21790" target="_blank">📅 02:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21789">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/21789" target="_blank">📅 02:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21788">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/21788" target="_blank">📅 02:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21787">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خسته باشم ویس میدم تو دایرکت نده تو مخی</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/21787" target="_blank">📅 02:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21786">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/21786" target="_blank">📅 02:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21785">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/21785" target="_blank">📅 02:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21784">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/21784" target="_blank">📅 02:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21783">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/21783" target="_blank">📅 02:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21782">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">امارات هیچ خیری نیست
😃</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/21782" target="_blank">📅 02:16 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
