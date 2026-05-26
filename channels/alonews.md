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
<img src="https://cdn4.telesco.pe/file/Vcl_DXfJZACJRC5jQ6xLhznzx1jK7veoIfzVbTYvnpOze2Ha_x0NulLIftYAaZRgK0BVOMAjuaoKd_TQWPek1usBELzMhqt7QsU3xcFPRTv4rIeiRw6AcUQWmRiftMrA6gPMCwV_B7s-21gM5z7tc6yvhWd8AYk1s8yxSekhYdKxW-2f1oP1nNDx1WwaofvCs71dZWbO4SIxFaX4pO7Oi-sXadCGaTpo3r-gO9Nd_t2L1P97r6L5Sa4-QpsEGyCfeDxGpr73N7uCshRstMgkC981RMl4fdQ8szJp9ZM3c3kXZzJsHbl0FY1UkLAlvItK8pbwflfBWx8gu1kB1XF0Qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 936K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 07:01:12</div>
<hr>

<div class="tg-post" id="msg-122701">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
رویترز به نقل از وزیر امور خارجه آمریکا: تدوین مفاد توافق با ایران ممکن است چند روز طول بکشد/ فکر می‌کنم در مورد عبارات خاص در سند اولیه، بحث‌های زیادی وجود دارد
روبیو، در مورد حملات اخیر آمریکا اظهار داشت:
🔴
تنگه‌ها باید باز بمانند و به هر حال باز خواهند ماند.
🔴
دیروز برخی مذاکرات در قطر انجام شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/alonews/122701" target="_blank">📅 06:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122700">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
آمریکا حملات جدیدش در جنوب ایران را تایید کرد  فاکس نیوز به نقل از سخنگوی فرماندهی مرکزی ایالات متحده مدعی شد:
🔴
ما روز دوشنبه حملاتی را در جنوب ایران برای دفاع از خود انجام دادیم.
🔴
این حملات، سکوهای پرتاب موشک و قایق‌هایی را که سعی در مین‌گذاری داشتند، هدف…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/alonews/122700" target="_blank">📅 06:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122699">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
آمریکا حملات جدیدش در جنوب ایران را تایید کرد
فاکس نیوز به نقل از سخنگوی فرماندهی مرکزی ایالات متحده مدعی شد:
🔴
ما روز دوشنبه حملاتی را در جنوب ایران برای دفاع از خود انجام دادیم.
🔴
این حملات، سکوهای پرتاب موشک و قایق‌هایی را که سعی در مین‌گذاری داشتند، هدف قرار داد.
🔴
ما در طول آتش‌بس با خویشتن‌داری به دفاع از نیروهای خود ادامه می‌دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/alonews/122699" target="_blank">📅 06:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122698">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفرامرز | اینترنت بدون مرز🚀</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O97ET3oPdukYj3_vDV9LDltWS6DeW-S_dHJRrE6InKpz_-Hz4ex_djjmkxxR9uIWQRxswgV3ZKliJ4vnHAPYmHy6k4YyC3cZqjNT438E_WNsvC61HIlfw5hWj6Il94iAme3pOT0iH-BOhPcW9TPw9l7DUZZGOHlcDVS2ZQOjvw_zlsc3lMFfvoaSmtQk4GBst5Y_xwqA0QIUHgXKaN2QI_XucGQAX7YoA8fipzcKPeU2E5puXyJDbC3HVbyt2guGtXKHyKqgOlcUnZ4kNovOn4JSEFdEJnX0O3ishO_154AAZFwWZu1Z2ZEK1TpELWMNy5gQtBcfuT41neVBUF4Pbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش فرامرز کف قیمت ایران وصلت می‌کنه حاجی
🤙
فی ۱ گیگ = ۱۵۰ت
فی ۲ گیگ = ۳۰۰ت
فی ۳ گیگ = ۴۵۰ت
🧡
فی ۵ گیگ = ۷۵۰ت
🧡
فی ۱۰ گیگ = قابلتونو نداره ۱٫۵۰۰
ایکی‌ثانیه تو جیباته جون داداش
👇
@VPNFaraMarzBot
@VPNFaraMarzBot
@VPNFaraMarzBot
@VPNFaraMarzBot</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/122698" target="_blank">📅 01:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122697">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
پدافند هوایی ایران سه پهپاد آمریکایی را در آسمان بندرعباس سرنگون کرد، از جمله یک پهپاد ام‌ویو-۹ای "ریپر".
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/alonews/122697" target="_blank">📅 01:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122696">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CC4OeejwS-vTvCpxBO4v6wNtTlFtBdScgFjgHpXn8nb1TgUhW9EaSQNGqdjmpK3a2sGmOdwjJ5O2L5XhLx6M8F1wvtnKUK8o5DNMZDlYkiHHjjJXKB9xQS_R02jqEhQccMEVhaDPoj2SxfL7aVPboKsga_Eo-vL0vCdeDZSfzQcfbbcNmPkuYBJZoOM7P-Oa9I_qHSOMLz9ub9GOPqmAs61ia5iwBnxDJyrnAPrSJ0XgEmzRfCNIkFzElhSPsfhd_d21Urg2ZrqKF7e1nC_pswJuXbtYSKNenXQSxC8LfX7jlivGnTJ0XexXgKZFrLAWyfdO1ku37l6pfniFwRI9ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ هم اکنون: اورانیوم غنی‌شده (گرد هسته‌ای!) یا بلافاصله به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود یا ترجیحاً، با همکاری و هماهنگی جمهوری اسلامی ایران، در محل یا در مکان دیگری که مورد قبول باشد، با حضور کمیسیون انرژی اتمی…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/alonews/122696" target="_blank">📅 01:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122694">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZfIyg7dUtjtvuQDRTHD7Yp_FYMgmf0EIpyFDVH0vgAJXtd_kZYkhdCq1u2aDyw8Fgb1ypPw4JELE5JbKZkzUYnEzlC79PkroYozGLVpqXwnzIosMFOSJB6MRig6h9BpNz4xTOuXME8aYxnFQCSATtXG2rCj5S_otPz1cPR_iRrWxRmMm6Mu5-zmd1CkGK-aU4qQO7OPlDCIoNG_YHlCajN2ZAWKhwdXnDEBV8KGYUHbOsrIpwsLVb_I5uy1Q8BrRt23B3XNzMYjlaBc8fa5HAt3GSg2ikc5ipuRE3LaOo6FzHwrLkPhX0FuRuQV8De3N0En89mnHn87IlzTqADEviA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lNzZpGZRK4B9LrSSR8lZo7o-A_AQRU_tnVY9_bms6EE0nlMIx0DcV9bI6v_kFJsjI3xWQv53-dSto8F41rsOw2xWeqiMz3gN7_LXet0a7CMQzkrxhltRfhR_WPYpTB74g5QFr4eXMvSqGwsoXPmUIWigFdjYsvf_PFpQZj7PdAJ4M17OFmbtGTnEw0C6fmwVSYvHY-yhoolkCl5QyDqbYOX2IOgYT1D8P1ubTQwHfqFtbKHrxWOFFMOENqmABnFUzzBu87Fv507-pO7uvi8ltLGX01iy_0YCwHkM_ckyCGlrsFXWdj_uHhzzLcfWRYlVWKzOhR91chXZ5ffV8bwuHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
در شرایطی که همه فکر میکنیم به فنا رفتیم امروز در ایران، تمام ظرفیت فروش لکسوس LX600 با قیمت 110 میلیارد تومن توی کمتر از 10 دقیقه به پایان رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/122694" target="_blank">📅 01:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122693">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
بلوبانک قطع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/122693" target="_blank">📅 01:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122692">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
رسانه نزدیک به محور مقاومت: ایران احتمالا با انتقال اورانیوم به خارج مخالفت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/122692" target="_blank">📅 01:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122691">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qmp0q1QHvUtf8M1XVY0xZgAk2rJ38oRAP_lGxGQ8aQmIwQIXgkiTPhmTQINQW1e3599D6IEGdTW74EWvfQeiKQAXmyb6wjtmmS4e797yWQn--pKTlZWuxiVrkTPXst2lqa-U7GhNL_MlF9osyEax14WN6ZkevuBMrNeAGpPgTTN_uUuxLcF5RGJRhw8scCt8xa8K3ikZodeQkyebB3wBxfrFUmwFX4Y6OJIbuHct1mE_-9PdVq0dIP3wyyJN-0zl1y4hZvBZQyMlfYJZixX-UBK8OOwVySwy9_Sl6Rj1BCd_-9qBr3YgPkZALYLDDtDhUUdusenQevDPMXtN6STkww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ هم اکنون:
اورانیوم غنی‌شده (گرد هسته‌ای!) یا بلافاصله به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود یا ترجیحاً، با همکاری و هماهنگی جمهوری اسلامی ایران، در محل یا در مکان دیگری که مورد قبول باشد، با حضور کمیسیون انرژی اتمی یا معادل آن، این فرآیند و رویداد انجام و نابود گردد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/122691" target="_blank">📅 01:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122690">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
وضعیت فعلی
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/alonews/122690" target="_blank">📅 01:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122689">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
جنگنده‌های آمریکایی یا مشترک آمریکا و اسرائیل دو قایق تندرو نیروی دریایی سپاه پاسداران را در نزدیکی جزیره لارک در تنگه هرمز هدف قرار دادند که منجر به کشته شدن حداقل ۴ پرسنل ایرانی شد.
🔴
این حمله تقریباً ۴۸ ساعت قبل از افشای گزارش رخ داده است.
🔴
رسانه‌های ایرانی تحت فشار بودند تا از انتشار این خبر خودداری کنند تا مبادا مذاکرات جاری آتش‌بس مختل شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/122689" target="_blank">📅 01:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122688">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فووووووووووری/گزارش‌های اولیه از پرتاب موشک‌های ضد کشتی توسط نیروی دریایی سپاه پاسداران به سمت ناوهای جنگی آمریکایی در خلیج عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/alonews/122688" target="_blank">📅 01:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122687">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
نام سه تن از کشته شدگان نیروی دریایی سپاه
🔴
عباس اسلامی
🔴
قدرت زرنگاری
🔴
عبدالرضا گلزاری
تاکنون باقی تلفات اعلام نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/alonews/122687" target="_blank">📅 01:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122686">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گروهک تروریستی «الجیش الکانفیگ‌» مسئولیت حمله به بندرعباس رو گردن گرفت.  [@AloTweet]</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/alonews/122686" target="_blank">📅 01:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122685">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
کانال ۱۴اسرائیل: چهار نیروی سپاه در حملات آمریکا به قایق‌ها کشته شدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/alonews/122685" target="_blank">📅 01:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122684">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
طبق برخی گزارشات دو قایق تندرو سپاه هدف حمله جنگنده آمریکایی قرار گرفتن
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/122684" target="_blank">📅 01:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122683">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
هم اکنون پرواز دو فروند هواپیما سوخترسان آمریکایی در آسمان خلیج فارس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/122683" target="_blank">📅 01:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122682">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/122682" target="_blank">📅 00:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122681">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/122681" target="_blank">📅 00:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122680">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">💢
فوری/پرواز جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/122680" target="_blank">📅 00:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122679">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
طبق برخی گزارشات دو قایق تندرو سپاه هدف حمله جنگنده آمریکایی قرار گرفتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/122679" target="_blank">📅 00:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122678">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">با پولایی که کانفیگ فروشا این مدت در آوردن بعید نیست موشک خریده باشن کار خودشون باشه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/alonews/122678" target="_blank">📅 00:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122675">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706144e3cb.mp4?token=QpRon5KxJnF7HQoujXZ4s0Onf11p64bOrdirMomBXht8SPbFKAvZ-q7EVriPPJaU3ZeBmja1iNI9XlybLZ5ws4zRPdBNwxGB2-_fo3Nr-Ez9AfTy8vAFHkJ7dLfgS_KhT9OhWl-NFAdeCWrXD2SUQo4Rc2QhmbT28vcFFbLrT2wMKulQZtasjm7exjmQr6rCT8hd7c41CcZ7UPtbWvoGHVEvm_PjQ3_WlNitV9Oez7nZqhtrbwF8WFlOBmvk1oy-BlqMs7wpdcT0WZLJ0Ic0J_rvbiiE9vieLV_jnCB9Av0tKxc6rmxeeUKmnuKgVSAD4hO2qu-0m5Wu975HeVsh7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706144e3cb.mp4?token=QpRon5KxJnF7HQoujXZ4s0Onf11p64bOrdirMomBXht8SPbFKAvZ-q7EVriPPJaU3ZeBmja1iNI9XlybLZ5ws4zRPdBNwxGB2-_fo3Nr-Ez9AfTy8vAFHkJ7dLfgS_KhT9OhWl-NFAdeCWrXD2SUQo4Rc2QhmbT28vcFFbLrT2wMKulQZtasjm7exjmQr6rCT8hd7c41CcZ7UPtbWvoGHVEvm_PjQ3_WlNitV9Oez7nZqhtrbwF8WFlOBmvk1oy-BlqMs7wpdcT0WZLJ0Ic0J_rvbiiE9vieLV_jnCB9Av0tKxc6rmxeeUKmnuKgVSAD4hO2qu-0m5Wu975HeVsh7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اولین فیلم های تایید نشده از پهباد در قشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/122675" target="_blank">📅 00:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122674">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WJLknxNTRn_mT_K9DFfwX4layUQQj2LFGM_FhtNmBbqo-yGnv8QKhvERZRlXn9C-AL5_qRx3VtZ9T1VGgdCCJ_H-V4gkYqNa2ZNNTSQlF3JFkk1FLrf3tqgBS_Zjbn5YycPjUKagO1qZfzbYy3ARZQzRQ21LfTLgIlD1BZRV6BOXxTFoIXvQGn6WIznJbLp6mopTIl3LwKXVgWYQkvA1ikCSK-aFho4SpsORERC_NhZvK6m6EF52-Spk220rHFgdp5uzCQ63Y3xcXNCRqTb7FV41dQPWt5WujzZCkrZW9QHv-_QA7ezrTC8MOTdzdeZ99GupryeVPdaEdcoyoKaQuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در حال حاضر یک فروند هواپیمای سوخت‌رسان KC-46A پگاسوس نیروی هوایی ایالات متحده بر فراز خلیج عمان در حال پرواز است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/alonews/122674" target="_blank">📅 00:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122672">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
تابناک:
فرودگاه بندرعباس مورد اصابت موشک قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/alonews/122672" target="_blank">📅 00:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122671">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyjIVKWgm7bLjwIzmvkEyUIrhAoj6acmVv7X_c7u-PbZVfVToRlUJE8YlAa-S51cI4D1UIOgLaXNMYzHjMuGdilXOCYkqbJBo89eLlEbPS2AomEN_wJi7ZZqebaRKh17JPAtnN2mKTl7gQB4bqkspuF3AVO8on_9OOIx1zswZ7EBYLYvtQlopQ-dEfgl2Ny-iZY181HAmDzYsWQldormoCWQVtnZd4JvsmWq05lq76y19TE5w699LSDjaruFGi7ypUXFVOIpmGo_0Sjn5ieknHPBJ68P9fp6qmXHVBqXZoTT7wOsJ_1GU-2N0hsSfKXOP88jUo4RSGZkAfFGmG4Z9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دودی که گفته میشه از سمت پایگاه هواییِ بندرعباس بلند شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/alonews/122671" target="_blank">📅 00:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122670">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
مهر: دلیل  انفجار های بندرعباس مشخص نیست
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/122670" target="_blank">📅 00:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122669">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
فارس: همزمان در خلیج فارس حوالی سیریک و جاسک نیز صداهای مشابه شنیده شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/122669" target="_blank">📅 00:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122668">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
طبق گزارش آکسیوس، ویتکاف و کوشنر در روزهای آینده به اسرائیل سفر خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/alonews/122668" target="_blank">📅 00:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122667">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
فوری / صدای ۴ انفجار در بندرعباس شنیده شده!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/122667" target="_blank">📅 00:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122666">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری / صدای ۴ انفجار در بندرعباس شنیده شده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/alonews/122666" target="_blank">📅 23:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122665">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j71qTFwbZ56wZhL0EnAKyioCb1RsYQKLu7McfrdKg4NgO7WN3zIKNlSfG_Pt9vwPFNgdNxrifGwVgy4B2OvMqxELZpqnpeMsejHk9j0-DR9PymlOWi9LB7qecdt8Jc9C118fJ5IxxjEJERoeP0Qqikk2SjnuSUffEZK7w15ghvWkRVpwkfF-V-DgHDDFxm5NzhTiUQNIJ9irNFQJOmAKiDtcFcApOqMKNsfL6ezlinpt8fvqRY8y5KmoE42iKzTsj1YDh9CJ5YZq_UnF5S7PPvIZrO8TQGvLQZCFqkQKRmv3ea3yuY6zw0NZcBHe-kvMa3yRDPYk_q_gXwTqTxcqDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره به نقل از یه منبع :  با میانجی‌گری قطر، آمریکا و ایران روی آزادسازی پول‌های بلوکه‌شده تهران به توافق رسیدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/alonews/122665" target="_blank">📅 23:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122664">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86a0a0247b.mp4?token=QxPgVAMU-PLOx3snECvzYjBqWfMkn3OYEv6G7VQFZmpvTPMJDWE99iXbCuuBqS71Lj1IkAB-peOnUzc8EfBh8RbJz8FXzmdYBLaZur6b7ODq8x7L7MV3w8UnlBIHnToEzBk0XZXkTfYJVaxJqeJW0A2rQ4oCLy6eWiZWZ-LcxzAZU4-pw99rZrHjZ9T-3ZrASi1xcobNcgcclvYRVWzRSfLTfNe-mPStlNlP0hQogN7OuveySomOAal0HgI3swC6plyVT4AuGhAbxfyUyHU7Pb5e7B9j8ZabdlVEoPE11zdBwBG7806yg_BCvvaZ_SnrqQh7f0Q3yjjsQpn7BFXqAb-WN2Rz9iWdwRwJdDFCm8XKtzl15t_k20nJh0Vl8Kj1n6P4XJL6Bxa03zmbfRY78gJ5yqoBRf_WLc0SPRElyu9oez8NKVqL19cdg8cJR2Uck8nIG_xZUnliW3tp0H8MT_dznslc8ipb8ePUVBvtZbnAnmcmvOp-KzVsx3FvtAP8EUNuFo6BxtbeJH9vJEuMubS3MOsBtldC93Lkx30YCmGGJVxjQz_t4uW_KhmFrs31Zv5PyxPIQ1gZPyBHdVcC6tLUIql_LoDFlrteJYY4zKltA_r2OVdiw8OypiP22lctcsaYCV_1igH9oN3PrdK30Yn3RqdytQ9tWgvi5pczmc8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86a0a0247b.mp4?token=QxPgVAMU-PLOx3snECvzYjBqWfMkn3OYEv6G7VQFZmpvTPMJDWE99iXbCuuBqS71Lj1IkAB-peOnUzc8EfBh8RbJz8FXzmdYBLaZur6b7ODq8x7L7MV3w8UnlBIHnToEzBk0XZXkTfYJVaxJqeJW0A2rQ4oCLy6eWiZWZ-LcxzAZU4-pw99rZrHjZ9T-3ZrASi1xcobNcgcclvYRVWzRSfLTfNe-mPStlNlP0hQogN7OuveySomOAal0HgI3swC6plyVT4AuGhAbxfyUyHU7Pb5e7B9j8ZabdlVEoPE11zdBwBG7806yg_BCvvaZ_SnrqQh7f0Q3yjjsQpn7BFXqAb-WN2Rz9iWdwRwJdDFCm8XKtzl15t_k20nJh0Vl8Kj1n6P4XJL6Bxa03zmbfRY78gJ5yqoBRf_WLc0SPRElyu9oez8NKVqL19cdg8cJR2Uck8nIG_xZUnliW3tp0H8MT_dznslc8ipb8ePUVBvtZbnAnmcmvOp-KzVsx3FvtAP8EUNuFo6BxtbeJH9vJEuMubS3MOsBtldC93Lkx30YCmGGJVxjQz_t4uW_KhmFrs31Zv5PyxPIQ1gZPyBHdVcC6tLUIql_LoDFlrteJYY4zKltA_r2OVdiw8OypiP22lctcsaYCV_1igH9oN3PrdK30Yn3RqdytQ9tWgvi5pczmc8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: این خانم‌هایی که قبلا می‌گفتند بگیرید همین الان تصاویرشان هستند که پرچم ایران و تصویر آقا را برداشتند و می‌گویند حاضرم جان بدهم و در مقابل دشمن بایستم در صورتی که یه روزی می‌گفتند این‌ها را بگیرید و جریمه کنید!
🔴
در برخی مساجد اگر خانمی با مانتو برود، خانم‌های چادری وی را از مسجد بیرون می‌کنند!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/alonews/122664" target="_blank">📅 23:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122663">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
شبکه الحدث گزارش داد تل‌آویو دست‌کم دو بار به تازگی تلاش کرده شیخ نعیم قاسم، رهبر حزب‌الله لبنان را هدف قرار دهد اما موفق نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/alonews/122663" target="_blank">📅 23:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122662">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
منبع نظامی به تسنیم:
اسرائیل هفته های پیش حمله پهبادی به امارات کرده بندازه گردن ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/alonews/122662" target="_blank">📅 23:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122661">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/183f047406.mp4?token=Y-OPxmTP-eCeBoT_myQ1Dr3GpWuavcfI4nNcYPKRsxS4DsNTrSxU0ipJ2nCBD723MNGhdPkQvnvREJaoDO-4GBPTSii3Hs9oEZ2v6vnRhwkLunCs3FaYxgz4JbszCN3K6PAARQ4AyEbqc11lRTc_vhF1WgN-WfBcovE4lnkuvkgpHWwAQkyzOEzp0GdadYEmbQuqVcCTfWo1LDZbg2AlLnN2ZaPyC1sI7OF36W8DFW6e1dUACN73fJvYsuzSucN4s2DF012Rgf1HE_RbVlfiBeUgP_slg4fWGI66iGAJuS71OZ_GaXcz0mElLfiZvZz6WdPMRk_MBDG4MWE9fqJTkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/183f047406.mp4?token=Y-OPxmTP-eCeBoT_myQ1Dr3GpWuavcfI4nNcYPKRsxS4DsNTrSxU0ipJ2nCBD723MNGhdPkQvnvREJaoDO-4GBPTSii3Hs9oEZ2v6vnRhwkLunCs3FaYxgz4JbszCN3K6PAARQ4AyEbqc11lRTc_vhF1WgN-WfBcovE4lnkuvkgpHWwAQkyzOEzp0GdadYEmbQuqVcCTfWo1LDZbg2AlLnN2ZaPyC1sI7OF36W8DFW6e1dUACN73fJvYsuzSucN4s2DF012Rgf1HE_RbVlfiBeUgP_slg4fWGI66iGAJuS71OZ_GaXcz0mElLfiZvZz6WdPMRk_MBDG4MWE9fqJTkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل اعلام کرد موج گسترده‌ای از حملات هوایی در قالب عملیات “تیرهای آتش” را در بیروت انجام خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/122661" target="_blank">📅 23:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122660">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA7orzFtE24JCnegh3pmfrQH0I27NT_JjP1qhhFvapuJx1wbvtw3_LG5EMjF568Tm2Vg9-U5dWQ2u8a4IE891ItiRpw3ZquVqGUJlwye7_VfNvr5te4ijTuIzVD0BxhqGVdYEVCKImCeQbJ6JnigH3ZoK1870YTJ8uv_PULZoqpKFZvSp3Heg95sO4YrFy_e0_dIZkBauZR-_XOHj3Juk9-jC5wwWcNmMh_FSMuDfZVKpeazj3bCfFU9nAIfVUPTqEDi_aTW_Zc1gRB6ppgR4Rudk-sy2e0c4ihX4i3Bp9tVdtRbKyH7MqFVOd1KqgSFc00K8PosArp7y2raraZ3vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حزب دموکرات
:
امروز از قهرمانان آمریکایی که در جنگ ترامپ با ایران فداکاری نهایی کردند، تجلیل می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/alonews/122660" target="_blank">📅 23:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122657">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1tl3cPToXFpCnxSX76o3TfAsYja8CMzNvcQWovO4hoLAhgmrNlqIBQFiP6mZrCwEdUl_-vpNOuL3ERDXQ7bs2D98j0XGG3TBdvgyYZkM_AVQD3joW4R21LZScvhfly3ucQlZZZBHjzlxmcpGNw6uFfdc7fXMCmvpMR-YY5ef52NZvTfGu6Fh2z17HpIrWkEmgiwdcqJMpmKjtfaBermd68-BMeqf5vy3_VFuZD3w78_tB7W4Cvoxg2pr5CCeV2yyt6WEWcF14XxdzBJGc8GFWGnpPfFgwtUZNH_OfWTdOKJFdhaBCADDSiuYcslxVjd6SnO3jMzKQ2au6iDeKOhvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mxhKeVXsRZwvPMGbgJ7NnILuABatQRrs6V-1EvdX5q6YSQa8CUq9Bk1DQwB4nudk-Oc7NQJJDoosbyPxUeFZ1RBFSTnaptHwYSklYOFlRurySb1zNNTFeN65B3GDjHxGX3dPpD0I-lY4h66sZhjPDos4yP3efTFzARd8NOSiEscv5FjirDZVyduuucqe9NLbK3M3WaE1kOmqNUxHFNGKG5FZ6WQumil8DzPPqXzLF8ZxxsVwBKssj4uPmdN_yQ53dtp7TeFnkqJfsqwPdc4N2dGo1jRrGnSw3mxOiQsSAE1q-rMPI8LuvR87i-R42Ho8K85CC-dMG2tgm-UwGg3MAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43136f33c2.mp4?token=txPzJTgQQL4b9DCChIPubpIwJ8IeSLOX-hBbBkT_S5mgPqEc_v_M4ztEn5YZjBAbXsWJXNOHFSH1z2jUEO05uQsTv6-Vn8kwlm_f0lRw3j2opu-wgtayGeilinOgpRIGmlmP3jWVQ3nJPTM3uzjuZSTC8XY2XiwUqOxEqsbVv5Rl2h7vLCqa8EbVDYdKMY4b5zaBy2VidFbcf_IsJsjNpXNUv1_tapM-lTdzAkRAZ9ngxqv-2iMhYX7GsrGdTWulPo22oqLVaykX-Xu3V78w1kghpG0kcktjoqvSMf1EkPe-ZX370aj78Aj9wXSxQbxMAe5a9DNiFp3Z3Y1xcMclDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43136f33c2.mp4?token=txPzJTgQQL4b9DCChIPubpIwJ8IeSLOX-hBbBkT_S5mgPqEc_v_M4ztEn5YZjBAbXsWJXNOHFSH1z2jUEO05uQsTv6-Vn8kwlm_f0lRw3j2opu-wgtayGeilinOgpRIGmlmP3jWVQ3nJPTM3uzjuZSTC8XY2XiwUqOxEqsbVv5Rl2h7vLCqa8EbVDYdKMY4b5zaBy2VidFbcf_IsJsjNpXNUv1_tapM-lTdzAkRAZ9ngxqv-2iMhYX7GsrGdTWulPo22oqLVaykX-Xu3V78w1kghpG0kcktjoqvSMf1EkPe-ZX370aj78Aj9wXSxQbxMAe5a9DNiFp3Z3Y1xcMclDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک حمله هوایی اسرائیل به اردوگاه پناهندگان نوسیرات در مرکز نوار غزه چند لحظه پیش انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/122657" target="_blank">📅 23:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122656">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
پاکستان دعوت ترامپ برای عادی‌سازی روابط با اسرائیل را رد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/alonews/122656" target="_blank">📅 23:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122655">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
۵ پیش شرطی که ابتدا آمریکا باید انجام دهد
🔴
رئیس کمیسیون امنیت ملی خبر داد:
🔴
۱. خاتمه جنگ در همه جبهه‌ها؛ مخصوصا در لبنان؛
🔴
۲.محاصره دریایی آمریکا علیه ایران باید برچیده شود؛
🔴
۳. پذیرش حاکمیت ایران بر تنگه هرمز؛
اگر محاصره ایران برچیده شود، تردد کشتی‌های غیر نظامی برقرار خواهد شد؛
🔴
۴.تعلیق تحریم های ایران طی ۳۰ روز؛ از جمله تحریم نفت
🔴
۵. آزادسازی منابع بلوکه شده ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/alonews/122655" target="_blank">📅 23:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122654">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5ZOdjzodVz9zQo-fvCaWqWbafpoRWJCb_TTSHaWwWW9C-rWQnB3BP2QdpHeKzSdm1VUiEk7Y2pNCEd5WmTrQIkXfWWgtbrr94f2mGJTJye8uX2MWku0CrKmD_TcQ5zSA_YcyYwVNuu45cQXoM-h8k0tCiu95yFYfVw81aF3uscef9ajwr03pOdWF1K7eikBFPmBIIBh7_aqUowzVUqejlz-3R52Ef9Nr31GFwwPhpUEm9DOoOiGQW9SndfZioSBG-YXe2QQO9AzGwUk7c9EMXRAFLV7Xzhk9-4HYVGKtYWbvv177XXqBRus8QSQnJJGWzvjMRFTSBebEWej97-AFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی
:
«قالیباف» به عنوان مسئولِ تیم مذاکره کننده ایران، «قرارِ دوم در پاکستان» را شرکت نکرد، ولی امروز بدون اطلاع رسانیِ قبلی همراه با «عراقچی» و «همتی» به قطر رفت!
🔴
حتما «موضوعات مهمی!» در قطر مورد بحث قرار گرفته که میزبانِ سران ایران بوده است؛ آنهم کشوری که در دو جنگ اخیر خاکش بارها مورد اصابت قرار گرفته!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/122654" target="_blank">📅 23:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122651">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_0AAUnSr1vIC-IPZDNW0HIp4HJcSiy5HAaLkflIq0LNOzhZApZ5KwNcAWOHUeYB35Cb5zZerHuDXR552OA-Wm2s5WXeLkWM3gpSQfJZ2Czp1Qjt5eYfVaR0gXIjtAGLdcyklWLnqpI1i_4DFuWR_M2nSXNb8ynToAFEyZii5qFFzgmfGgHUMUIkZtBByhSZEKbuGu_bV9COB3fXoeR_0sDiLVccwb6uhR5rWVuBAl8E4OsfyO3AkUWd3ok5v0D-WE6Ka2iTLL78PtnyBruS8G090qiwOoFLSgLBXMNM3SXnUkshe4ZmeqpoCr33xkbRTs9GRNgrJP4qGyQeRqPYCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKpZiOnkbcYtksfGftdR-vTvtIboYXVXMxx_WgCbh5RNdNG6fQ3dyaxaqTeNgvp4JyCblnySwqKz9K3kqI9T60KAMSPDPWPUYeyKWQp9KnC1zGCZFzpN5bG1A_1NJPnTGTndQl_fbgWb7RPB4fH6sN0K8-OrL1I35F1eGvofTWlm4ejK4EHVXwXvdU_t8DzjhVBDwZ1KIOb4ajj_I_EPoTl1Lr2f66dBG3Yj0N6MK8PkswEB6nI4Fo5jIqGrjk3QFY1DLE5u95T4TF0sJCGs3FRcWxGPoFZKBpWNaFkvuxY6TS-MBxFgzPwZapz-TutTSLbLIxnJPP3CRNsBeSjr7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUDjZM5fIEYNMrPLCzIl-kZPNgjhHWOX0ICsvQXEMZB-fuDBxDIWyIlp6nOr8h-O-4uEb78QLi9DpzlzlPOQcMOcUi42zQMSFahktD1iWSQBN-B0_OzWoSAVPgXqDkvH2t52Ii0nm3wPueDzoWeugpS5EQkrHBYJ1sh5M0bJFQT3wL1DEqor5PR2jpbqh2H2cMiGpTOY0bnuMMtfIk6xpvP03vTKSBHV1ZlcEpGOo2zGsDbrcoLELqd6vyOBjPaOtPKafZD9-8rWx6yH9LLkQPDOWc-LPkqLvrxLftT6fZ0QnxETdAo0tPgXcwPIjN8XdL54kpSaj4FJwshHOAtBNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله‌های جدید ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/122651" target="_blank">📅 23:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122650">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
یدیعوت آحارونوت: کاخ سفید نتوانست درک کند که جنگ بدون استراتژی به چیزی بین شکست و تحقیر منجر می‌شود؛ ترامپ حتی نتوانست افکار عمومی آمریکا را قانع کند.
🔴
اگر آتش‌بس شامل برداشتن محاصره دریایی باشد، ترامپ خود را به مسخره خواهد گرفت.
🔴
با شکست آمریکا، اسرائیل اکنون با بدترین وضعیت استراتژیک تاریخ خود روبرو است: سه جبهه فعال — ایران، حزب‌الله و حماس — و هیچ فضای مانور.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/122650" target="_blank">📅 23:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122649">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی: آمریکا هفته دوم جنگ از طریق عاصم منیر اولین پیشنهادش را ارائه داد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/122649" target="_blank">📅 22:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122648">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIXslgrCtjcOryK8WnhpcJPfsV6vV_zrxPWi8APHF2CBerce--b3DQzKmSzeX8j45_u-F4LIHOUgIomY3hxdb_whkGmtN1lGl_2iS0RWIOz5IdcK651XtDWeXEFVDIrHhA7biwkHpTrf9DftmB9FZOHK8iBEfylsoNtspSPVwoVL_QiBXjGPkIPHmiRymdje_F3UH40QZQgRK67Vctf2tVaGC4N9SmXrGxNwKmGkcNoXLS2fnXrU6Oq4S-LAy-c7NaPcZQqa9C42pJW6aemaBjma9sl_i8-pw5qWOHgtpDxShY1eikA-hX0E36b3xpVzYgTa3mWPJHfoMthfMrzxPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / لاوروف از روبیو خواست کارکنان سفارت آمریکا در کی‌یف را تخلیه کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/alonews/122648" target="_blank">📅 22:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122647">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
‏ظرفیت فروش لکسوس ال‌ایکس ۶۰۰ با قیمت ۱۱۰ میلیارد تومان، زیر ۱۰ دقیقه تکمیل شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/alonews/122647" target="_blank">📅 22:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122646">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
کلش ریپورت: وزیر امور خارجه روسیه به وزیر امور خارجه آمریکا گفت که مسکو برنامه‌ریزی‌ای برای «حملات سیستماتیک» به کی‌یف دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/122646" target="_blank">📅 22:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122645">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lhys3HAKyd9Gm0ntbqCzq9GNdbBvOKAvC3FdiAo4o4o25cypqa88YtowgpiRFfpTpQVmoDssO4ufjXJ0hZHBd_LETF1Mt3GJKFqWhVemnvtnh4xYRsmlbaoRXhXy5aNIsH__EuK7uGqURe2P0dBq1FK_zdEQ7Tg65o_petaL4L-MFRppTOU5nnzeb6El7ko826C24MzQp4CBzbmJ1r-X_vAyBw1ipCO7C0x941NZ0zU2lZTeO5_Jfzz-_QHHPWJEt75HB4H917lFKceJJuIQfdoUKmgho6n8_7DU8YBIJKMtJNGWVLMfiuKCmE3N84t5td9iqhK2mmJx8AmnWejUSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت رسایی درباره وصل شدن اینترنت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/alonews/122645" target="_blank">📅 22:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122644">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxLTW73JMXUu0xHgyaR4i49q4z11zg2K4Ivgfxf6LK1yXjup9aqeLsws9HMaRcTh9doIZMbCqxcjGuMzZ42wDPpKYJP3uvvP3SOhUtxdZ0N7o1KHR960CD1TtNGPLKGDhD9NZRI2FjzCC7nS-uCfoVvAxtbvD4i5oeRm0g7rm4Y-soS_eP3_fzOihTdVFXUxX02FQbgz7mvWz7EYrYbnLM8zT7__R4yXfGDVUTvC2S_ACeY1OC8zsGf8VvB-UcNp4zVwrfSTgPM4UsNBE0HCUiwcc6C5f0U3DiBRctIUDIGHP_KS4ygx9vl0jUj9QIYl7pxKgBD9YC0ggtMy9mB9Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/122644" target="_blank">📅 22:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122643">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزیر امور خارجه روسیه، سرگئی لاوروف، در تماس تلفنی با مارکو روبیو، وزیر امور خارجه آمریکا، اعلام کرد که نیروهای روسی حملات سیستماتیکی به اهداف نظامی در کی‌یف انجام خواهند داد.
🔴
لاوروف همچنین از آمریکا خواست تا کارکنان دیپلماتیک آمریکایی را از پایتخت اوکراین تخلیه کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122643" target="_blank">📅 22:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122642">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری /  نتانیاهو: دستور دادم حزب‌الله نابود شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/122642" target="_blank">📅 22:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122641">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ارتش اسرائیل شروع حملات به چند شهر لبنان را تایید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/alonews/122641" target="_blank">📅 22:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122640">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره: احتمال دارد اسرائیل پیش از هر توافق ایران و آمریکا، دست به یک عملیات نظامی بزرگ در لبنان بزند
🔴
با هدف استفاده از فرصت زمانی باقی‌مانده تا توافق ایران و آمریکا.
🔴
یا برای به شکست کشاندن توافقی که بر توقف جنگ در جبهه لبنان نیز تأکید دارد. و احتمالاً ممکن است شاهد بازگشت جنگ به منطقه باشیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/alonews/122640" target="_blank">📅 22:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122639">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
آمریکا هیچ تصویری از پیروزی ندارد و هیچ یک از اهداف اعلام‌شده‌اش را محقق نکرده است، در حالی که ایران بقای خود را تضمین کرده و با بستن تنگه هرمز قدرت خود را نشان داده است، به نوشته اسرائیل هیوم.
🔴
تنها نتیجه ملموس تاکنون بازگشایی متقابل تنگه است؛ همه مسائل دیگر — از جمله برنامه هسته‌ای ایران، موشک‌ها و نیابتی‌ها — به مذاکراتی با تاریخ مشخص موکول شده‌اند.
🔴
این توافق حتی حزب‌الله را به آتش‌بس ملزم می‌کند و عملاً ایران را به عنوان یک بازیگر نظامی و سیاسی در لبنان به رسمیت می‌شناسد، که کاملاً در تضاد با اهداف اولیه جنگ است.
🔴
تمام مسائلی که برای اسرائیل حیاتی هستند به مذاکرات آینده موکول شده‌اند و هیچ‌کس نمی‌داند آیا این مذاکرات اصلاً برگزار خواهند شد یا خیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/122639" target="_blank">📅 22:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122638">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
نبویان، نماینده مجلس: رها کردن مدیریت و حاکمیت بر تنگه هرمز در هر توافقی با دشمن، خسارت بزرگ و شکست برای ملت ایران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/122638" target="_blank">📅 21:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122637">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VegbmYz-TWZQdfRvKO6zDV01nyxZjsolbtoAGxZu0G98rXPa4gYZ03Se7nPcI6xwo07M0XLeYy7NWhC8WYU0rBwnfP9h_C1UNrphRTHg-1sA-PxCeflW2BjTz5SQpouwC1sWrmftAVAsCVbdNN5OoahTYLjyZ0xsUAr8HbmhKEbHZiH0ot5eFGCEKdxS7tdGPb_3I-xy3tg502uNuW5IZ2uOkZ2wdpXOcz_D2m_Hla8VJ9RWokfwV9FTw6_xOrLJetlffnbwJ3e1E4gHGm5GTSVZ3UsiOdZjlKJHEts7S5xD0mU__yk6ymvBS_PP-wiso8p5B_qQ7NJlSTfzf3zaFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکونومیست: نزدیکی ایران و آمریکا به توافق؛ توافقی موقت برای خرید زمان، نه پایان قطعی درگیری‌ها
🔴
ایران و ایالات متحده به یک توافق نزدیک‌تر شده‌اند، اما این تفاهم از جنس توافق‌های پایان‌دهنده به جنگ—آن‌طور که دونالد ترامپ ادعا می‌کند—نخواهد بود. این توافق در بهترین حالت، صرفاً زمان بیشتری را برای پیشبرد مذاکرات بعدی و به مراتب پیچیده‌تر خریداری می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/alonews/122637" target="_blank">📅 21:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122636">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
بنیامین نتانیاهو: «ما در جنگ با حزب‌الله هستیم و حملات علیه آن را تشدید و قوی‌تر خواهیم کرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/122636" target="_blank">📅 21:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122635">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWlPpYVhrUvV8Og7dKf7alJ_v10658EpbqtD9GcZ0OzGbZ-XI_z6VwBrkjI4tWI98aVfGTXJVfwKt9aaaJ9s04S7HPEigM-iF-wf5xaqk4jeMz17h56YzI7KvNk58xWUAeurLJfI5U9Ahbl8KPc0CoFdj_Fc2gs_8KSfuDsaZIthqI3ZSdoQ28XOAiiqVGkllQ8M0jG1fcaodwLZ4c3GXke_OIJ0BRnqQIJlG_D8PrQa2mY0tozKa26rKdYApgzmTkj1DjIi56LHkdxJp3MBY6flsx-7YVXQlGT6lhSVyzpZfKaljRDg7_eSwLortCIEj2HF5pDqu3aSgs_niFMfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روایت آمیت سگال، خبرنگار شبکه 12 اسرائیل از اختلافات ایران و آمریکا در مذاکرات:
🔴
ایران در حال حاضر فقط حاضر است به عدم توسعه سلاح‌های هسته‌ای متعهد شود، در حالی که ایالات متحده چندین گزینه برای ذخایر اورانیوم غنی‌شده ایران پیشنهاد می‌دهد، از جمله فروش آن به ایالات متحده، انتقال آن به یک کشور ثالث یا رقیق‌سازی مواد.
🔴
اختلافات همچنین بر سر تنگه هرمز باقی مانده است، ایران بر مدیریت بر این آبراه اصرار دارد در حالی که ایالات متحده خواستار کشتیرانی آزاد و بدون محدودیت است.
🔴
هنوز هیچ توافقی در مورد دارایی‌های مسدود شده ایران حاصل نشده است، اگرچه قطر پیشنهاد داده است که ۱۲ میلیارد دلار وام بشردوستانه به ایران بدهد.
🔴
لبنان نیز به عنوان بخشی از چارچوب توافق گسترده‌تر مورد بحث گنجانده شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/alonews/122635" target="_blank">📅 21:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122634">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RggUmjE27uTwYzu9Y5YAfJ8qQWEH27rrs7RLPbeUimxIOGCiNXiptxdZ4yoLP3F4Iffw8v7RyVdO2RSAVNIgTixhCjsXrKN5AeHx-ECkMfh4EdoeESPoo-Skk8y_36u82VaUhBDfou9w-peh_xieGZxxXt5KpklliPbHcodrwXT_dkRNTVQRK7n0L-eju8Ff9mQcaHPoqZpqI9zAprVDhcfSdZ8s23JOUSd_pMoRaNRIFAyS4HRpoor6YfR4TtCXgDwN6jH3aoXJHX7JoKhe5yqDVUPSNS1aAa9diycMj0ZJZd_jd8ZC5wDoGsGt7aTOws5_o6VB13rMNJktHFjW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی، از رهبران بولشویک‌ها:
پزشکیان خودشم میدونه نمیتونه اینترنت رو وصل کنه. این خبرای جدید بازی رسانه‌ایه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/122634" target="_blank">📅 21:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122633">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/122633" target="_blank">📅 21:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122632">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-uOsa1z8bYvoSKoSG2h9SNwEcwsxYeYdRx3qOwoxCKyf5lcYEtWBBk_L-MnzJvULCPsw23JJ7-fILXYngfF9rkHnTK8GUTE7WutBxA9wQGafIxuUqQPpWKP-WFAnXhw5mDYrh4YqQFf4ksG3uZSn7RJ9Oc5dKvyKiBstsoXV4PyO8A7YPdU1D2jPJB5txpPwy0n7zxMHj4wCSjsvOjsO5h6C3ioJjerXOjYG-_CVtpMMbMjIAz6mNio4sCxDX14CWz5E9dE71SbRENM-n4LDg3vLA2W8vmH9WTpRxA-Na1IteYLU9ooO5dcqkoRRtsWmp05OjxqYEcGss9A53GMHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام آمریکایی به اکسیوس گفت: دولت ترامپ از تشدید اقدام نظامی اسرائیل در لبنان حمایت خواهد کرد
.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/alonews/122632" target="_blank">📅 21:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122631">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
اسرائیل آماده حمله گسترده به لبنان است
🔴
کانال ۱۴ اسرائیل: نتانیاهو و کاتز (وزیر جنگ) درباره گسترش چشمگیر عملیات در لبنان و تصویب هدف قرار دادن ساختمان‌ها گفت‌وگو کردند.
🔴
کانال ۱۳ تلویزیون اسرائیل: اسرائیل در حال مذاکره با ایالات متحده در مورد گسترش عملیات نظامی در لبنان است.
🔴
خبرگزاری رسمی اسرائیل هم گزارش داد که ارتش طرح حمله آتشین قدرتمندی را علیه لبنان آماده کرده و منتظر تایید سیاسی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/122631" target="_blank">📅 21:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122630">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caYBfFJHH4TVBJU2dWKtlOVAM-v6KIwboCpX1OHfkfF4h9WxFioVmGHpkz4f6IfEaElbWEbwMsHhRSnlnnpLvHTGUlo1xx2c2BNyK-YtdBYCG12TnSVNpiKvo0ur-lc28i8oGGrDU4OJGt4DY5JV5FsIOtVLyyV5TxnYrE3jHPKBoWKwkvJbWMzl-cLlD3m9miKyzyIPlgde1TF4s1zfjhqIqS9r45MOvZW55Mg3JSStSCfw59RM4sLP0GtdiUQm_H3nDnIxcyioiHJ_NIViMFa9ukhgRAoxjiXYguk4hBBzo0j0GC3PU4DVv8_MvFsimydhfjsjFRVn3KCuoiJGtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اشتراک v2ray
🗯
گیگی
120,000
تومان
🔗
لینک ساب برا چک کردن مصرف و حجمتون
🔥
سرعت و کیفیت بالا
✅
پشتیبانی دائم
📱
جهت خرید :
@v2safeBot</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/alonews/122630" target="_blank">📅 21:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122628">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
قیمت نفت امریکا برای اولین بار از ۷ می به زیر ۹۰ دلار در هر بشکه سقوط کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/122628" target="_blank">📅 20:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122627">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فووووووووووری/فارس: اینترنت باید با دستور شعام باز بشه و فعلا خبری نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122627" target="_blank">📅 20:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122626">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
مدیر روابط‌عمومی وزارت قطع ارتباطات خبر داد: رئیس‌جمهور دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/122626" target="_blank">📅 20:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122625">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb1084d3e.mp4?token=jAXE9ViHV5neLZCcjHFtAZICKjJ_UHwRRENTFzpZPzgPfcUafMR9KDYrUpZVf0hZgh2WNLaJu3OLc9fGs0I1qd39XszUoeoztpfeU08HvmrNHguyeVWW6dQq_WedeM9FX4Dr3ktdyp130kCCfFICkqhks8xKpYQQTwdb1WTCxm0VuQt1v2ETtSuaci6pwM5E9Dbsnjp7HyQXz6b5gqrLHFI4T0CKOtG-gwIjXv6Bn-WUVkDzVYP-3O0DH1Oi5d45LDDD6Vf6bcP6iT0pM8WL7NQ-J4x5RPNwuPSoWNWK-eMTR6Q4NWnPXOwwU8bk6raeguPdHL_kIq9TbfcmJONFzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb1084d3e.mp4?token=jAXE9ViHV5neLZCcjHFtAZICKjJ_UHwRRENTFzpZPzgPfcUafMR9KDYrUpZVf0hZgh2WNLaJu3OLc9fGs0I1qd39XszUoeoztpfeU08HvmrNHguyeVWW6dQq_WedeM9FX4Dr3ktdyp130kCCfFICkqhks8xKpYQQTwdb1WTCxm0VuQt1v2ETtSuaci6pwM5E9Dbsnjp7HyQXz6b5gqrLHFI4T0CKOtG-gwIjXv6Bn-WUVkDzVYP-3O0DH1Oi5d45LDDD6Vf6bcP6iT0pM8WL7NQ-J4x5RPNwuPSoWNWK-eMTR6Q4NWnPXOwwU8bk6raeguPdHL_kIq9TbfcmJONFzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ایران هرگز نباید سلاح هسته ای داشته باشه
تو دو درگیری اخیر مجموعاً ۱۳ نفر از نیروهای مسلح رو از دست دادیم
- تو ونزوئلا که یه پیروزی کامل بود هیچ تلفاتی نداشتیم و اونجا رو در یک روز گرفتیم
- اما تو عملیات خشم حماسی ۱۳ نفر جانشون رو از دست دادن
- این افراد فوق‌العاده برای جلوگیری از دسترسی بزرگ‌ترین حامی تروریسم دولتی به سلاح هسته‌ای جان خودشون رو فدا کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/122625" target="_blank">📅 20:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122624">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری/روزنامه هم‌میهن: رئیس‌جمهور دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/122624" target="_blank">📅 20:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122623">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری/روزنامه هم‌میهن: رئیس‌جمهور دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/122623" target="_blank">📅 20:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122622">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
رئیس شورای هماهنگی تبلیغات اسلامی: فعلا تصمیم نگرفتیم چه زمانی رهبر سابق رو تشییع کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/122622" target="_blank">📅 20:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122621">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
کانال ۱۲ عبری:
برخلاف ارزیابی‌های قبلی، ایران تولید موشک‌های بالستیک را به سرعت از سر گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122621" target="_blank">📅 20:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122620">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ادعای العربیه:
پیش‌نویس توافق تأکید می‌کند که کاهش تحریم‌های نفت ایران مشروط به اجرای تعهدات آن است.
🔴
پیش‌نویس توافق آمریکا و ایران بر دوره ۳۰ روزه برای بازگشت کشتیرانی در تنگه هرمز تأکید دارد.
🔴
پیش‌نویس توافق آمریکا و ایران بر دوره ۶۰ روزه برای مذاکرات هسته‌ای تأکید دارد.
🔴
توافق بر آزادسازی بخشی از دارایی‌های مسدود شده ایران طبق سازوکاری مشخص تأکید دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/122620" target="_blank">📅 20:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122619">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری/فارس: باز شدن اینترنت دست شورای عالی امنیت ملی هست و فعلا تصمیمی گرفته نشده و گمانه زنی‌ها الکیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/122619" target="_blank">📅 20:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122618">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JL1ePzXO0ZTSPPILYeqIHubMqF5E_xX-2cTrWFV3iIhLmDEl_XTdIyEKF3xL8XqqUWPgKAj1hyhj-2B-oM9ouzh9m8cjOtaU54IOU2Z4LdR24NhJHutPpD2ueCcKOn01XYzNnSusb7kuaroMDBUOwW07H9xUEesrIhscqkIEUeoDKLkoHqm5cSXu-oPLXwQ98yZWeQecrm06Jl0k_6hAafqLnkozCqpIbfCc3eDyXy2kif5O4AI7G1EU0Uoo8ihWim6OEc_IiA37IBvv1qSCOw7NIOlXCyHwU60SRcg4huOpmR6ZnlrfhUmM2_Gx_usovV7N8lCFvNVV7xDhLgTCFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه: پیش‌نویس توافق میان آمریکا و ایران، برقراری آتش‌بس جامع در تمامی جبهه‌ها، از جمله لبنان را تضمین می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/122618" target="_blank">📅 20:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122617">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
منابع خبری الحدث:
پیش‌نویس توافق آمریکا و ایران بر گشایش تنگه هرمز بدون عوارض و خنثی‌سازی مین‌ها تأکید دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/122617" target="_blank">📅 20:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122616">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/797c664227.mp4?token=GEcxwRFkTpWXNRRinpv-jmV8as0uI2BDvYROtWsapyq6UUJTZHMOMj1oXctPYvrh4WEhp1uwyLBekQ3Tt2zyGo5LHn72EBanL2lMz7N940YbrRNyJ0mqSwD_VgtOr0PcMZ9g9qd0qd4RpCaKwHJnaLxZwPXyNYCBdEcGSNdUwCP8L4gxAkqXK6CWDLBcbwTICpv4y31fiSVafvCuE1DFlgg1hFJ2gpMGoJFA0fJjYDQXu2lXGLfIdKjAmGmi94YhUZNRgjL7dpzMXMaj7RLaq5_BjfV8uZ6aVLx8U2Ead0NmdiX41JT1gFXWo8Meoc3Vq7LRoFSfSxyfWu-tIKUo1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/797c664227.mp4?token=GEcxwRFkTpWXNRRinpv-jmV8as0uI2BDvYROtWsapyq6UUJTZHMOMj1oXctPYvrh4WEhp1uwyLBekQ3Tt2zyGo5LHn72EBanL2lMz7N940YbrRNyJ0mqSwD_VgtOr0PcMZ9g9qd0qd4RpCaKwHJnaLxZwPXyNYCBdEcGSNdUwCP8L4gxAkqXK6CWDLBcbwTICpv4y31fiSVafvCuE1DFlgg1hFJ2gpMGoJFA0fJjYDQXu2lXGLfIdKjAmGmi94YhUZNRgjL7dpzMXMaj7RLaq5_BjfV8uZ6aVLx8U2Ead0NmdiX41JT1gFXWo8Meoc3Vq7LRoFSfSxyfWu-tIKUo1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ به احترام روز یادبود تاج گلی بر سر مقبره سرباز گمنام در گورستان ملی آرلینگتون می گذارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/122616" target="_blank">📅 20:14 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122615">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سی ان ان:
مذاکرات به خوبی درحال پیش رفتن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/122615" target="_blank">📅 20:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122614">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olRvZrJP_QdV_j2yXwjIh9de1mUwca4dRZNkCuDo_qmjGJhkOwOkxIs78s7t6-lWOALvtmPf0LV0CBdtsBy0WiKnNUP8DNqGwhDYEBsQD5EFtQZpEj-8PkCBSliz8910_mlUpw9Cf_y_Jq_SfHTjJm10bEZY1XHj4j60VZKiyNJiTumASomCOV59S0aDmxtyzYemNdWZXTf9CLreJY3UpQ2pL4bP7HKci8GoiJkXkL-9LS1kbznrfNJQPhacLgwkexa_iU7tOGfVcbKEN99mFZMP7izp9sYOXXx_QfMCzB_j1VrkuJht_3KA4r6xrMloWVK5sbyON-roRnO5FYo_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از واسطه‌ها
:
واشنگتن و تهران به مواضع خود در مورد مسائل هسته‌ای و دارایی‌های مسدود شده پایبند هستند..
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/122614" target="_blank">📅 19:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122613">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
‏سی‌ان‌ان از مسئولان آمریکایی:
اختلافاتی درباره نگارش مربوط به برنامه هسته‌ای ایران و رفع تحریم‌ها مانع از نهایی شدن توافق شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/122613" target="_blank">📅 19:50 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122612">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
کانال ۱۵ اسرائیل به نقل از یک منبع:
اسرائیل در پی تشدید حملات پهپادی حزب‌الله، در حال بررسی تغییر رویکرد نظامی خود در لبنان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122612" target="_blank">📅 19:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122611">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
یک منبع مطلع به i24NEWS: مذاکرات بین ایران و آمریکا پیشرفت دارد اما مشکلاتی وجود دارد، تغییرات و "ارتقاءهایی" که هر طرف در زبان یادداشت درخواست می‌کند.
🔴
هیئت ایرانی که به قطر آمده است، تلاشی برای پر کردن شکاف‌های جدی است - مانند مسئله آزادسازی وجوهی که ایرانی‌ها درخواست می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/122611" target="_blank">📅 19:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122610">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی: هیچ عقب‌نشینی وجود نخواهد داشت. این موضوع در میدان نظامی، میدان دیپلماتیک و مردم حاضر در خیابان‌ها با مقاومت شجاعانه‌شان که دشمن را ناتوان کرده است، به اثبات رسیده است.
🔴
اکنون بیش از هر زمان دیگری، کشور به وحدت و انسجام نیاز دارد تا آمریکایی‌ها و اسرائیلی ها نیز در این زمینه ناامید شوند. میدان وحدت و انسجام، عرصه‌ای دیگر در مبارزه است.
🔴
تلاش جمعی برای جلوگیری از هرگونه سخنان و اقدامات تفرقه‌انگیز، ایران عزیز را به پیروزی نهایی خواهد رساند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/122610" target="_blank">📅 19:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122609">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: به نظر می‌رسد گره مذاکرات ایران و آمریکا در مسیر حل شدن قرار دارد و ابتکار قطر برای حل اختلاف میان تهران و واشنگتن نقش اساسی در این روند ایفا کرده است؛ به‌طوری که دوحه عملاً یک میانجی بوده، نه صرفاً کمک‌کننده به روند میانجی‌گری.
‌
🔴
تنها چند ساعت باقی مانده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/alonews/122609" target="_blank">📅 19:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122608">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
فایننشال تایمز: دو نفتکش حامل گاز طبیعی مایع (LNG) از تنگه هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/122608" target="_blank">📅 19:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122607">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
شبکه CNN: توافق احتمالی ترامپ با ایران می‌تواند تقریباً به اندازه تصمیم او برای آغاز جنگ اختلاف‌برانگیز شود
🔴
طرح کلی توافق پیشنهادی، بسیار کمتر از «تسلیم بی‌قید و شرط» است که ترامپ در مارس از ایران مطالبه می‌کرد. برخی از جمهوری‌خواهان می‌ترسند که بالعکس این ترامپ باشد که تسلیم ایران می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/122607" target="_blank">📅 19:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122605">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVHQ2Fywg1qUbxtHsgpgZh5H89PKpNY69rDEM9mS2QdL6uYc-aagSdt8TOipuwJv5MIpkaO3axDc4guf1SjFx5bDt4GrgnAD5nUp1vPUPY_7GC5qjQYNlbO5coHycKwitw_azdNdwR5K-L2C0db1JX_0SaCLYkvC_SA80WoJdThTNE8Gg3H8xdLhv0PMXBj1wH9t99jfUiQMgsSiJM5QxDaX2Hw76MN_qzQutaHC5Kj1TK_9xhz7l6FAMdqV7oUp2n1CZpHbtYXshYvWTWS8HWHbbtzlYzA-2jTUmDp6A1qpgCPeEbWIh9w7X4N3g3F-eN_iX9ryZqgnhHtz9zzS4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/guhP6vwNPSA7ZVaz2p8l7WAwq-Zl2euYjn5JN5zkMsL6kV569tsE_Q7i9DtMaghS5rz9gd_GgUppxGagO0yYN564iFadwDw36gZ6HAjAYkkJN-5j0TLla8RjX9xA5dySCSEpKdM-bRSl0UMvq0meE2GF1h7XLlFRFQcsAYXqEL4H_YqwlsHEiIAELV4PAQd_bZhj8wwMf-MbNQWmVov-QmkrSO5eBkKQ3KJjTfWj4rW0Ls5LO7k5Vd7G5bSPhr7FBxVqCtBLVWXpXq4SP_Ozx9gxvM72_BgKbiWHX6z9gFzWLX7ZnHIVELtkpHoFG7DsGo6pVXf9gqAbG2TTbJg-KA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ عکس‌هایی را که به جو بایدن و باراک اوباما درباره ایران تمسخر می‌کند، دوباره منتشر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/122605" target="_blank">📅 19:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122604">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5540723a.mp4?token=Oy8L7OfUWfZT2TYreP6nvt2t3WvI6r9_dJkfB3-Uhlq87452Hl2B-9q8NZUsnDv91oRi_TNHb1z8obiYh1Vnga5cBt4DDSMpNHN-UwnrqAgmcvjKhOYf5rtIZ_MYykxH8UnoXGEyt3RmKV1rkbS5ixtvL_fPfGaE8AAtTgtMdLKEgdllbqw__binOY33JQW8bByAI02u4riqPksZRcUBrRl3CG97zwSkO_UaUyUFmxQNt3Ryr27W1plwywKIDHhpsTBioNFc5Ir4RMwnLCQTwuZkQpqcw_tnj29N_cKR1J5Sbc5qe6hXP-o-0zvT8BVKWZu5bwwFp-M7L0bCdWkoCzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5540723a.mp4?token=Oy8L7OfUWfZT2TYreP6nvt2t3WvI6r9_dJkfB3-Uhlq87452Hl2B-9q8NZUsnDv91oRi_TNHb1z8obiYh1Vnga5cBt4DDSMpNHN-UwnrqAgmcvjKhOYf5rtIZ_MYykxH8UnoXGEyt3RmKV1rkbS5ixtvL_fPfGaE8AAtTgtMdLKEgdllbqw__binOY33JQW8bByAI02u4riqPksZRcUBrRl3CG97zwSkO_UaUyUFmxQNt3Ryr27W1plwywKIDHhpsTBioNFc5Ir4RMwnLCQTwuZkQpqcw_tnj29N_cKR1J5Sbc5qe6hXP-o-0zvT8BVKWZu5bwwFp-M7L0bCdWkoCzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاپ لئو چهاردهم : هوش مصنوعی باید خلع سلاح شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/122604" target="_blank">📅 19:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122603">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5ZOkqJP8d1QzAULq5uMTZ5Cm5eYCCkyj6cD_QzfflMR0lHtUCQmN0han2ASJ7_Qgnnpc-r2vAI9NDjpeoBiiHo0OEe0s1c3SAuq8xsYWA0ZeCajpFq4kcTvmvVAm3nWFqJYDZxFCSnkVwTSdrqKE09v9nbi4iKfa7WQdCWfVaq7N-N91o7GXkoqAe3RvF3ZHBX1KSMNUqttiALJaov-Jc2syOmRGokrd3qieDLTAa--hjV1XJ2ppEn1ctJWjfavE8wxeK1paSfVhBW4jUf4lAN8nfPRzoV09m7GwxAxOV9mO8Tk8JwczdiVd5Z0icoggrlMadBr3OhLkpIYXex03w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / الحدث : منابع نزدیک میگن ایران آماده‌ست اورانیوم با غنای بالا رو از کشور خارج کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/122603" target="_blank">📅 19:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122602">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
الحدث به نقل از منابع عالی‌رتبه:
به احتمال زیاد فرمانده ارتش پاکستان به دوحه سفر خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/122602" target="_blank">📅 19:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122601">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی در آسمان جنوب لبنان دیوار صوتی را شکستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/122601" target="_blank">📅 18:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122600">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF): نیروهای دفاعی اسرائیل آغاز به حمله به سایت‌های زیرساختی حزب‌الله در منطقه صور و مناطق اضافی در جنوب لبنان کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/122600" target="_blank">📅 18:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122597">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JM4bzzdlS4m12f0IMJvsAxV7oPQ2Mbj-Uq1n0GMt506yH40bUzu_RmwzbZghLB2f3W2_KYGXf91xW5fb3sN3RW02kTmFffyH4XyQ_Lvx1A_Y3OwOXXGRQL16B6mlE-RjEaNTbyjQXM1H_vgLeNBiMVpK7iTHknNvzZuPp335TbwXi0ujmgbZTsgYsSmP5unvh6Jl1-NfY1kBjCT4gIyp0AEm1Wz-Gr9PoW1-Qk8xRrjIbQsQT-_cqDxJcSlaHiT547aQFnoR73pPhT-kOqJ0aKv9jhLb1reNE1UAHHK7zOYn7u5diMafEGCfGeF0bH2y013KqJMpe9b-UzsuyranIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0f9ce0e5.mp4?token=ORMEQEG8pykIGGi05teDaZ_SHxsKFFdVJXW8rlh4gwyb13SCCdsMzhGd_nEKKO9HnYppRxQMhBThtxAWTBUfiX-h9XXEQm5Sq2e9rl6xOeKCp7614lAIMbBrwYY5lxTEk9gzfasQcsg8Q-VMvidjs6K38h0Gvs2bCfzOSZJpIhSDCFJQi47tlnDm6BV3PYPRb8GQaosB0Oi_DL9kDa2wk2oJji0xRQKQrwXkjh_qpTTh9ZqXSdaihfFpYt2hqV5-pxeNvpHRmGyKPdoz0SPM6bRbeucs7B7alr_5_1e75xllKgLZRw8zZscm7cBHzfc7GRLTAxN3525DYDTMRTMy-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0f9ce0e5.mp4?token=ORMEQEG8pykIGGi05teDaZ_SHxsKFFdVJXW8rlh4gwyb13SCCdsMzhGd_nEKKO9HnYppRxQMhBThtxAWTBUfiX-h9XXEQm5Sq2e9rl6xOeKCp7614lAIMbBrwYY5lxTEk9gzfasQcsg8Q-VMvidjs6K38h0Gvs2bCfzOSZJpIhSDCFJQi47tlnDm6BV3PYPRb8GQaosB0Oi_DL9kDa2wk2oJji0xRQKQrwXkjh_qpTTh9ZqXSdaihfFpYt2hqV5-pxeNvpHRmGyKPdoz0SPM6bRbeucs7B7alr_5_1e75xllKgLZRw8zZscm7cBHzfc7GRLTAxN3525DYDTMRTMy-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌هایی از حملات اسرائیل به صور در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/122597" target="_blank">📅 18:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122596">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSfA5MBVxIoKI4FHtJHmXsny6bez-TBZVPoQ20hZfeb4QGSX_05gL1DxmZophtvs5RXCqItl6jYkE16bBfO6yh4xjx7mWgqzcqu91CZT2qiy8c1rKYuRw4_aYR8dMc7j4nDuiq1dQuLehXKV2VaRbwS6NXCn03A3yHrKjzHWG7mofEzSFShumEIqTEpl2Bvl06D6x59jM25x5zCSn8RjHJ7uTKWWV6MN5Kvs4GxQI29Zsk4yC6YDAdenl3PKuLbmGWezK_-cAnvBEwcLU84A7zZKqA8VgBHR0At1piDlbF4KlyWZucmATbW_OTFDiwJO6fNJBZkFjh7uQ_9pp_x2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال تلگرامی Fighterbomber که وابسته به نیروهای هوافضای روسیه است، قول می‌دهد که روسیه «کی‌یف را تمام خواهد کرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/122596" target="_blank">📅 18:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122595">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
یک منبع سعودی به سی‌ان‌ان گفت که عربستان سعودی تنها زمانی روابط خود را با اسرائیل عادی خواهد کرد که «مسیر غیرقابل بازگشتی» به سوی تشکیل دولت فلسطین وجود داشته باشد و تأکید کرد که موضع ریاض «همانند همیشه» باقی می‌ماند، با وجود پیشنهاد ترامپ درباره به رسمیت شناختن منطقه‌ای اسرائیل پس از احتمال توافق با ایران.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/122595" target="_blank">📅 18:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122594">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
الجزیره: هیئت ایرانی در قطر برای گفتگو درباره «حساس‌ترین مسائل حل نشده»
🔴
مذاکره‌کنندگان ارشد ایران در حال سفر به قطر هستند؛ کشوری که نقشی محوری‌تر در گفتگوهای ایران و آمریکا ایفا می‌کند.
🔴
عباس عراقچی، وزیر امور خارجه و محمدباقر قالیباف، رئیس مجلس، در حال گفتگو درباره حساس‌ترین مسائل حل‌نشده برای دستیابی به یک تفاهمنامه هستند.
🔴
رئیس کل بانک مرکزی نیز در این هیئت حضور دارد که نشان می‌دهد تحرکی در جریان است و بحث‌هایی درباره رفع انسداد دارایی‌ها (که یکی از خواسته‌های اصلی ایران است) صورت می‌گیرد.
🔴
منابعی به الجزیره گفته‌اند که بحث درباره سایر موضوعات از جمله ذخایر اورانیوم با غنای بالا باید به زمان دیگری موکول شود و تمرکز فعلی بر گام‌های اعتمادساز است.
🔴
نقطه اختلاف دیگر، تنگه هرمز است. اسماعیل بقائی، سخنگوی وزارت امور خارجه ایران، پیشتر گفته بود که این موضوع بین ایران و عمان است و تهران خدمات امنیتی برای کشتیهای عبوری از این تنگه را ارائه میدهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/122594" target="_blank">📅 18:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122593">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) : پس از به صدا درآمدن آژیرهای خطر در ساعت ۱۶:۰۳ مبنی بر نفوذ هواپیمای متخاصم به چندین منطقه در شمال اسرائیل، یک پهپاد انفجاری که توسط حزب‌الله شلیک شده بود، در خاک اسرائیل، نزدیک مرز اسرائیل و لبنان سقوط کرد. هیچ تلفاتی گزارش نشده است.
🔴
علاوه بر این، اندکی پیش، نیروی هوایی اسرائیل یک موشک شلیک شده توسط حزب‌الله به سمت خاک اسرائیل را رهگیری کرد.
🔴
در حادثه‌ای دیگر، اندکی پیش، یک پهپاد انفجاری در خاک اسرائیل، نزدیک مرز اسرائیل و لبنان سقوط کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/122593" target="_blank">📅 18:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122592">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2ONgmIpeCDLiC7RPig-KXQKCuCfUIKEAhAt9lHz1gHVsASlDK5v6AulD9OoLEn1ihULzK8DJOuxgzOAB9n3naYJ-Rn-5FkNmG82ldT0N1vs6jDd63Vk3X4z-eTwpzr18JAtwagbiIEcqB8DUbKezpb_sB7_Mi8lkGfQ780YBLOUFXZRS41Bj0HrrNP51edK0rKgYIYkqa6a-eAMb3PVlljGj3qaznAHX0zKEarf7RHOjuQznPDC0DtFhN2O_jxjJul-gjpIkgVAh6CJNEp_YuIzZeiCq0HXPuMWaY6vBTc2R3ua-9ofwzCosnNIm57C4-D5G23qePsGpzDwL7ShXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور جمهوری‌خواه لیندسی گراهام:
پیشنهاد اخیر رئیس‌جمهور ترامپ که گسترش توافقنامه‌های ابراهیم را به عنوان بخشی از یک توافق مذاکره‌شده در مورد مناقشه ایران الزامی می‌کند، به سادگی درخشان است و منجر به مهم‌ترین تغییر در خاورمیانه در هزاران سال خواهد شد.
🔴
با صلح عربستان سعودی و دیگر کشورهایی مانند پاکستان با اسرائیل، منطقه شاهد سطحی از ثبات خواهد بود که پیش از رئیس‌جمهور ترامپ هرگز تصور نمی‌شد و در نهایت به یکپارچگی منطقه‌ای منجر خواهد شد که خاورمیانه را به یک قدرت اقتصادی و منبع فرصت‌های خوب تبدیل می‌کند، به جای اینکه یک انبار باروت باشد.
🔴
انتظار دارم متحدان عرب ما این را بپذیرند، همچنین دوستان ما در اسرائیل، با تمرکز بر این وظیفه، زیرا شکست گزینه‌ای نیست - که تحلیلی درست خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/122592" target="_blank">📅 18:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122591">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqy_PCL8Uo8P9eIpflUqzMaHX-0_7lv5-1UFnKiQageARX5wnuL-pazsqy_0B2ho81RhQX1pqewE-c7doKRggzOeqFMJxfrblwkf8DGj5wqBFXmZaQALGS9lSwX3BDNnOaIMlwxa_yGFe5In-ZGKzGTOHdTwsBC0MBW14AGuBHgHMzoKOLX7e-9GPE0q9CsWp7VVz3BSh5CVDVJr8X1igXF5XXkzW35ZMtHkQXTtcF4kGC9eHfnFEFVgQFmb6OXRcDzT9L8-UWkZO1XUSNE0uC9BT-2ubzvyH2MnGNLRFQcvxs1fS5xMFD22k97Qh0fDkNa0K8F8MGttBy75H_iFMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش مکو اسرائیل، ایران در طول آتش‌بس، بازسازی بخش‌هایی از صنعت موشکی و پهپادی خود را سریع‌تر از حد انتظار از سر گرفته است.
🔴
بر اساس برآوردهای اسرائیل، ایران در حال بازسازی موشک‌ها، پرتابگرها، پهپادها و سامانه‌های دفاع هوایی در تأسیسات زیرزمینی موقت با استفاده از قطعات باقی‌مانده، حمایت روسیه و قطعات قاچاق شده چینی است.
🔴
مقامات دفاعی اسرائیل معتقدند ایران می‌تواند تولید پهپاد را ظرف چند ماه از سر بگیرد و تولید موشک را ظرف یک سال به طور قابل توجهی گسترش دهد.
🔴
فرمانده سنتکام، دریاسالار برد کوپر، شهادت داد که ۹۰٪ از پایه صنعتی دفاعی ایران نابود شده است، اما اطلاعات به‌روزشده نشان می‌دهد حدود دو سوم پرتابگرهای موشکی ایران سالم مانده و از تونل‌های زیرزمینی مجدداً مستقر شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/122591" target="_blank">📅 18:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122590">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
قیمت جدید لبنیات:
🔴
شیر نایلونی: ۸۴ هزار تومان
🔴
شیر بطری: ۹۸ هزار تومان
🔴
پنیر یواف ۴۰۰ گرمی: ۲۰۳ هزار تومان
🔴
ماست دبه‌ای ۲ کیلویی: ۲۲۸ هزار و ۷۰۰ تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122590" target="_blank">📅 18:05 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
