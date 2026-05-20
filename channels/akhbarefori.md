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
<img src="https://cdn4.telesco.pe/file/OFE5oDEnUDY7AjKDgSgdiI62nAypcSxnUGYpltYJsH8f_4zpEte5PSMxJ42R1cS1sHLjaiT9mEb7_Q-SES6WtrOwkif63jmAmw7xpvcdZ4QO39r5S3GJtPo_qerBfbjaRnMu25o-AEolm56o2g69DwVy0uphkwQogBQfTEMrNbWbRsMdVCTF7mVessPMSjB1cl-BM7IfbW4F--3-KRQlTj7eZMp1Q9xR00nsZvd-zXL8jVbTg1YGuh-3M0gy9cgZsOLQfwx-uQRoyk9hdDHr7hkUsK0eDq9tJYC6LVxvNLG2hd4dRS8NszTqzrq89VMlSvH76l6M9zjjOBHOog1ufw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.97M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 14:55:14</div>
<hr>

<div class="tg-post" id="msg-653196">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZX85jwDtqsSXvKjnwD1IoySvbIUTodDwHEy4fC4GPtgvwpYWObnLm2nd8qowQzsTOig9DXoEBH5WFU7c-TvWdr1s08-TFjwM7l3yinTZV64ySojIiI3pxjIFrvQ4RvuCToyxIRjgYcA-StKMAbX0QDXPJtSl_KifBGKUM4HUcW-hB6QmEb-NO1-OjokUOa1U0FRWoMejqoerbwzY_OPInjcK_S7bmew_14uIVYMRCTa9PG5hG5lJORko6gH9YaC72dAb-Ngkk6XFXBKN6BnIUHyJOE3uMqhLrZK11Wt-P8FtkHgNnTbjetUUjsGQGdsacrTk4jrYUIe_s7RS9woZ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستورالعمل اجرایی تسهیلات ۵۰۰ میلیون تومانی مسکن روستایی به بانک‌های عامل ابلاغ شد
🔹
تسهیلات بهسازی و نوسازی مسکن روستایی با نرخ سود ۵ درصد به متقاضیان پرداخت می‌شود.
🔹
بانک مرکزی: مابه‌التفاوت سود تسهیلات مسکن روستایی از محل صندوق ملی مسکن تأمین می‌شود.
🔹
تسهیلات مسکن روستایی با تضمین سفته زنجیره‌ای و در قالب قانون جهش تولید مسکن پرداخت خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/akhbarefori/653196" target="_blank">📅 14:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653195">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTMAGIJyON2PKnSUeECm6DOR3GZByl105XpUh9xggvagsVgFfHPdsmr52IvJ4j5k_T4d6WrPZ76ZAqlkK4KlURLe6Dn5Q-HlrxFA3uvMoKxuzCeIc7gUp8WxpzVShIpNrMekCwA3wbZpQT4_R3L-vtDeZxsfCKFH9fBG904CMgi60t8d7XT84hI8dEgKHXIjYFj4o-IIOkkrXjHoPzzDL8bHd18qJtxDvknyPsaEZL3Vculrek6_WB5FvztfNbCSmwK0EKGG5Q2dsqMnrSKG3OLfqcc721LCsSjygl_vcaj2hJ3P5-X8HQOTGhzqtD2bhQmh8KrGRmivDOYKmj_4hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«جان ایران» به شهر آمد؛
همزمان با هفته جمعیت، بیلبوردهای این پویش ملی با پیامی متفاوت رونمایی شد؛ روایتی از تولد، امید و آینده‌ای که با نفس هر کودک برای ایران ساخته می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/akhbarefori/653195" target="_blank">📅 14:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653194">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
پزشکیان: مردم باید بدانند که کشور در حوزه تأمین بنزین و برخی حامل‌های انرژی، با محدودیت‌هایی مواجه است
🔹
در شرایطی با فشار‌های خارجی و آسیب به بخشی از زیرساخت‌های انرژی روبه‌رو هستیم، استمرار مصرف غیر ضروری، اتلاف منابع ملی است.
🔹
دولت نمی‌تواند منابع را صرف واردات سوخت برای مصارف این چنینی کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/akhbarefori/653194" target="_blank">📅 14:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653193">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
واریز یارانه نقدی به حساب سرپرستان دهک چهارم تا نهم
🔹
یارانه نقدی اردیبهشت ماه ۱۴۰۵ به حساب سرپرستان خانوارهای دهک های چهارم تا نهم واریز شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/akhbarefori/653193" target="_blank">📅 14:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653192">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3876f012bc.mp4?token=B2ZnYBXGZJalX2MBOJrO1oRL4VDJgWoaNnwWrzUuAqpf2vNrPYR22Xo8qhaCLUyiyCNFlHIkxpLRHRQI2xtVXmh8d6YJNigXIYGa1FXBKyebsOUuozfBhF1IOwMbgVy9Ux17-jQtnvu5L6cQoMEjOYGz9KdB8lXzlbNtaD21imk2qtuZk5dNDPEGwrdQEh80S8F6mT2U5EWrFkiVcQO9YgWc-AOauWEppdMgwkSukqxGLnSL8y2eRtKTVSIgptU7nrXIZ-loYlmiGp51xLdxEiIxf2NPzj0lxLEIAt8sIn6OjfdB90omaBywvLiPtdcMOkDblVES6e9woka4kFTfQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3876f012bc.mp4?token=B2ZnYBXGZJalX2MBOJrO1oRL4VDJgWoaNnwWrzUuAqpf2vNrPYR22Xo8qhaCLUyiyCNFlHIkxpLRHRQI2xtVXmh8d6YJNigXIYGa1FXBKyebsOUuozfBhF1IOwMbgVy9Ux17-jQtnvu5L6cQoMEjOYGz9KdB8lXzlbNtaD21imk2qtuZk5dNDPEGwrdQEh80S8F6mT2U5EWrFkiVcQO9YgWc-AOauWEppdMgwkSukqxGLnSL8y2eRtKTVSIgptU7nrXIZ-loYlmiGp51xLdxEiIxf2NPzj0lxLEIAt8sIn6OjfdB90omaBywvLiPtdcMOkDblVES6e9woka4kFTfQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تسهیلات ازدواج و فرزندآوری افزایش جدی یافت و برنامه های حمایتی پس از این ادامه دارد
🔹
وحید دستجردی، دبیر ستاد ملی جمعیت : طرح یسنا و طرح حمایتی سوء تغذیه کودکان به قوت خود باقیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/653192" target="_blank">📅 14:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653191">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رشیدی کوچی: ۹۰ درصد مهمانان صداوسیما وابسته به یک جریان خاصند!
جلال رشیدی‌کوچی، نماینده سابق مجلس در
#گفتگو
با خبرفوری:
🔹
فعالین سیاسی، بین‌المللی و نمایندگان مجلسی که به صداوسیما دعوت می‌شوند، بالای ۹۰ درصد وابسته به یک جریان خاصی سیاسی هستند که در صدا و سیما حضور دارند.
🔹
چند شب صدا و سیما را نگاه کردم و اکثر کسانی که در آن حضور پیدا می‌کنند، وابسته به جریان پایداری هستند و این یک نوع تک صدایی به نظر می‌رسد.
🔹
واقعیت صدا و سیما نتوانست به حفظ اتحاد کمک کند و موفق نشد و حتی در یک جاهایی که حتما ناخواسته‌ بوده، از طرف مجموعه صدا و سیما به این وحدت خدشه وارد شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/akhbarefori/653191" target="_blank">📅 14:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653190">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
کنست به انحلال خود و برگزاری زودهنگام انتخابات رای داد
🔹
کنست در جلسه مقدماتی خود با اکثریت ۱۱۰ عضو و بدون هیچ مخالفتی، به لایحه انحلال خود و جلو انداختن تاریخ انتخابات رأی داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/akhbarefori/653190" target="_blank">📅 14:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653189">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
عراقچی برای شرکت در نشست ویژه وزرای خارجه شورای امنیت به نیویورک دعوت شده است. سخنگوی وزارت خارجه اعلام کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/akhbarefori/653189" target="_blank">📅 14:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653188">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N17N17yUn0pzbxD1iTXeuBe0CjVFKrGZBZqzPB0ZQoxbA9TtHDFiC53FCuBKaX-6Lu_dA8dGeo_exDc0BUTcN84Ri7h2M9EHBLzblk7bs4j3J8OWdSkd-7kTG1UBQGXkD4ONVNgNkAvFc8qVqS_meA1XqhD_YBV-JleJwK1GlnSRMDSHK_wmYNlbL2kOl5AHzY8bxNaLvxWYbz94GeNpeI7AuPQFk1pyjxO7pbvckwhdRJ5fiZwq5eM4ea4TxU7tVDrLRDbrwupWU2hS4H2jIBbSjsB0tPPL50N3PfGuolfL9jfG382MwdN1n48FxGbYMNr6-SJ2R70SlXxuEvsZgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✉️
پیام رهبر انقلاب اسلامی به‌مناسبت دومین سالگرد شهادت شهید رئیسی و بزرگداشت شهدای خدمت
✏️
بسم‌الله الرّحمن الرّحیم
🌷
گرامیداشت شهدای پرواز اردیبهشت و در رأس آنان رئیس‌جمهور شهید حجت‌الاسلام والمسلمین رئیسی، یادآور شهادت خیل شهیدان خدمتگزار در جمهوری اسلامی ایران است؛ از مطهری و بهشتی و رجائی و باهنر، تا رئیسی و آل‌هاشم و امیرعبداللهیان و لاریجانی، صدها شخصیت برجسته و تربیت‌یافته‌ی مکتب خمینی کبیر و خامنه‌ای عزیز اعلی‌الله مقامهماالشریف که دفتر خدمت خالصانه و مجاهدانه‌ی مسئولان جمهوری اسلامی را با امضاء خونین خود مزیّن کردند.
🔸
از زمره‌ی ویژگیهای بارز شهید رئیسی، مسئولیت‌پذیری، جوانگرائی، توجه به عدالت، دیپلماسی فعال و نافع، و بخصوص مردمی بودن را می‌توان برشمرد. این خصوصیات موجب دلگرم شدن دوستان ایران از جمله مجاهدان جبهه‌ی قدرتمند مقاومت و بسیاری از دلسوزان نظام می‌شد. این همه البته با معنویتی که ریشه در عمق جان او داشت، آمیخته بود. در رابطه‌ی بین مسئولین و مردم، خصوصیات مثبت تأثیرگذار، موجب قدردانی متقابل می‌شود. اینگونه بود که بدرقه‌ی او تا جوار مولا و مخدومش حضرت ابِی‌الحسنِ‌الرّضا صلوات‌الله و سلامه ‌علیه با شکوه کم نظیری صورت گرفت. دوران ناتمام ریاست جمهوری آن شهید، مقیاسی از تلاش و دلسوزی برای ملت و کشور در عین حفظ استقلال آن را فراهم ساخت.
🇮🇷
اینک ما در برابر حماسه‌آفرینی‌های ملت ایران در مقاومت منحصر به فرد تاریخی مقابل دو ارتش تروریست جهانی هستیم. این امر، بار تکلیف مسئولان جمهوری اسلامی ـ از رهبری و رؤسای قوا تا همه‌ی سطوح مدیران ـ را سنگین‌تر از گذشته می‌کند. امروز شکر نعمت انسجام ملت و دولت و تمامی دستگاه‌های جمهوری اسلامی، در تقویت انگیزه و خدمت مضاعف و مجاهدانه‌ی مسئولان، گره‌گشایی از مسائل و دغدغه‌های مردم خصوصاً در عرصه اقتصادی و معیشتی، حضورهای میدانی و مستقیم، و تعریف نقش جدّی برای مردم بعثت‌یافته در مسیر پیشرفت کشور و حرکت امیدوارانه به‌سوی آینده‌ی روشن است.
🤲
رحمت و رضوان الهی بر شهیدان راه خدمت و نصرت الهی و دعای سرورمان عجل‌الله تعالی فرجه‌ الشریف پشتوانه‌ی خدمتگزاران به مردم مسلمان ایران باد.
✍
سیدمجتبی حسینی خامنه‌ای
🗓
۳۰/اردیبهشت/۱۴۰۵
📲
@rahbar_enghelab_ir</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/akhbarefori/653188" target="_blank">📅 14:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653187">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TW5iJXP_FkT5JfBq_GD0Msjxha1tM1c8qcyYFURvRWN1bqpa9yge2tt4Ts75k42lNO4typF8xiWXVubbkgu6t5_jCOW_tlCklhiXQR2L3zbmXew5IlzPzy7j0c1EwWfx12ACsrbrbYkNvvPS-C2s8kFMIAMxXWxqTcIS7_ACYrAMjS0Vs93-ITARPpSrpZMg037CeV6g5qBbPNYSJXAsymWW0hTPLDIcSpGyXpPgiSkY05hANGHbsYgQbELvsGIGP17TD2UQX9JFyj_0JMt6Mm6ISBjkv13iGJPYNDb8GuLlJr7PBOeqBckZs2QKelyYZBNIMCsG9GxWcCifeX5VJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خارجه انگلیس: بحران ایران جهان را به‌سوی گرسنگی گسترده می‌برد
ایوت کوپر، وزیر خارجه انگلیس:
🔹
بر اساس برآورد برنامه جهانی غذا، اگر جنگ با ایران تا اواسط سال پایان نیابد، حدود ۴۵ میلیون نفر ممکن است با ناامنی غذایی حاد و خطر گرسنگی روبه‌رو شوند.
🔹
ادامه انسداد تنگه هرمز، انتقال جهانی کودهای شیمیایی را تقریباً متوقف کرده و امنیت غذایی میلیون‌ها نفر را تهدید می‌کند.
🔹
جهان در حال «خواب‌گردی به‌سوی یک بحران جهانی غذا» است. /خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/akhbarefori/653187" target="_blank">📅 14:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653186">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isFkKEfDrOmWtdEzFNNoXTa4tEK1lA6Tn4pbVlDajitXM8lyNh6lcjdmOarpgw7X9TUmlpzpziG9YR1r-scJmXnfvWJYdpnKsuboUldGcxrnN5SQpEJIrm-Q8yQf0lGruMuccmgb-63dobHCO8ABZz9dgikL189co49THRJw2mo86ntBXHodsTgFDU9mAptTIcamZMIVt0nQ---0h3m45R4ya9ZFXDsweIJ0JVDtqr5wdScTZaKk8Lhi34OX0PIAOBdpFheDIyrZBMSO204E6ZsQzWl2jnZ3MeHbBSREgvu5Hz36wv4DsmE3a9ou2mgJQNgXhw7raw2L6_o_javksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صنعت نفت اجازه نداد در شرایط جنگی چرخه تولید و تأمین سوخت کشور دچار وقفه شود
🔹
رئیس‌جمهور ضمن قدردانی از تلاش‌های شبانه‌روزی مدیران، مهندسان و کارکنان صنعت نفت در حفظ پایداری تولید و تأمین انرژی کشور در شرایط حساس اخیر، دو مأموریت راهبردی را برای مدیریت بهینه منابع انرژی و ساماندهی نظام تخصیص گاز به وزارت نفت ابلاغ کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/akhbarefori/653186" target="_blank">📅 13:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653185">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
انحلال کنست در رأی گیری مرحله اول
🔹
کنست اسرائیل در رای گیری مقدماتی به طرح انحلال خود و برگزاری انتخابات زودهنگام با اکثریت ۱۱۰ عضو و بدون هیچ رأی مخالفی رأی داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/akhbarefori/653185" target="_blank">📅 13:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653184">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
سومین فایل صوتی قالیباف منتشر می‌شود
🔹
تا لحظاتی دیگر سومین فایل صوتی قالیباف خطاب به مردم با موضوع تبیین تحرکات دشمن برای آغاز دور جدید جنگ، ارتقای آمادگی دفاعی ایران و تشریح مسائل اقتصادی کشور منتشر می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/akhbarefori/653184" target="_blank">📅 13:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653182">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svH5QUHa2ZVJ68mIggUIjDf9oDeyDX0_HVBVLO4TKmbkzU9WJNPlwWip19rbuXTbHbyZ3O8mRLEZMX8jPkXhhfwacVe2V8dtLt2WfM_ZSbpGvqus78ojRaOqn81XtFjjHVkt1zFU0uV64S8GHxwjwiVQu7BPbBYfsm4Ngs4aZzaAabfczQeGkweJeMCor-iJoCXKzj6DawUQ-E4fhaEN8gbjaEYbe5xq0MfRIwV1N8PNEhUH8_wY-gI8XyC3lF0IRYKCC9SHDODTFrR4_YY4OjGs4y73A02VNXHuk3s5MRnGe9WCHeI8ASmjAq_Fx2NOZpxkqL7o267Nz58fLlRC9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تا ساعتی دیگر پیام رهبر انقلاب اسلامی به‌مناسبت دومین سالگرد شهادت شهید رئیسی و بزرگداشت شهدای خدمت منتشر خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/akhbarefori/653182" target="_blank">📅 13:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653181">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef77528fd9.mp4?token=Bm2B41Ya9lSRU-o5YNrx7WP-8LvqwbwlAxQkmKkdQl82Ieu7HimHqt6ZKxiCfKwiQ1VNsOLsKMkjMDOq33ZkaJemxX1c1x-1HKGaxw3DFSZb6ZqYm_qo_00pwBsLvMmT9-rf-LYnqxkhLf53qPSib5LmSVhXR1xxWoGYAgXug2q_YNm5GIYM48jNWBqTJVd9pw630B-tCgk-UQb4HCn5d7Tlad750RoaL9imfXuAz4M7HXAnnYH-SrOBxE4cbxhIzEphUqVg-DWdEye87dodmq17mPkj2ynL0Bdo0fkT47EU2sAXMJQ88kAmopuL6UOkz531fmdTQhhE8eKHEojlCo5YLEUAAQR-zP5Cx2d5uYboZGWrg72389-Bnvi_5WC_AxfzzEm-gvPotbdSVE1Vv2cQUJHzyhXuN94UxCYEE2uNzCtRd056rPEDxFb-Z84A_FOjZ2j8rvXzeZ84lweCabRsT656jnM_ssmRhlYOFnprSYZ2_ZVOm3AkWsEyMAgsqjoxXAVDvBnqrAp1q7taf_IK4U1IIAGJWKJP_PnwVW8ZY8YcW7XSykAuj81AzZm11HqwOt4RoFyECTM70TiSsG0DiXw3LF6_IfFxBn9WhmZk0buB5XAWnD-p1NxYSyvP5vO0-B4iAEW71q90ILlChrXt8-u-_5GCUJktmHoFTj4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef77528fd9.mp4?token=Bm2B41Ya9lSRU-o5YNrx7WP-8LvqwbwlAxQkmKkdQl82Ieu7HimHqt6ZKxiCfKwiQ1VNsOLsKMkjMDOq33ZkaJemxX1c1x-1HKGaxw3DFSZb6ZqYm_qo_00pwBsLvMmT9-rf-LYnqxkhLf53qPSib5LmSVhXR1xxWoGYAgXug2q_YNm5GIYM48jNWBqTJVd9pw630B-tCgk-UQb4HCn5d7Tlad750RoaL9imfXuAz4M7HXAnnYH-SrOBxE4cbxhIzEphUqVg-DWdEye87dodmq17mPkj2ynL0Bdo0fkT47EU2sAXMJQ88kAmopuL6UOkz531fmdTQhhE8eKHEojlCo5YLEUAAQR-zP5Cx2d5uYboZGWrg72389-Bnvi_5WC_AxfzzEm-gvPotbdSVE1Vv2cQUJHzyhXuN94UxCYEE2uNzCtRd056rPEDxFb-Z84A_FOjZ2j8rvXzeZ84lweCabRsT656jnM_ssmRhlYOFnprSYZ2_ZVOm3AkWsEyMAgsqjoxXAVDvBnqrAp1q7taf_IK4U1IIAGJWKJP_PnwVW8ZY8YcW7XSykAuj81AzZm11HqwOt4RoFyECTM70TiSsG0DiXw3LF6_IfFxBn9WhmZk0buB5XAWnD-p1NxYSyvP5vO0-B4iAEW71q90ILlChrXt8-u-_5GCUJktmHoFTj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنایت آمریکایی‌ها در رابطه با حمله به قایق‌های ماهیگیری از زبان صیادان لارک
🔹
اینجا وطن ماست؛ به خاطر مشکلات و ناامنی نمی‌توانیم مثل قبل کار کنیم اما پای وطن ایستاده‌ایم.
🔹
برشی از قسمت چهارم مستند «ماجرای تنگه»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/akhbarefori/653181" target="_blank">📅 12:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653180">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ca1668589.mp4?token=Ked0BZA81nLV1Wr2ke_0JY2XL4L5-Rld8qA_J_shL13uUrwov5-DAN3c87Z-4-oYGCrwr4b9YuFGuWB1iXZcVf3ZPAgnt47vAQ2UcFIu5k5EzzIlwnOLqsKFAHCtchPejm4MRbJAUeV3vQZrbwFxR7m_Bp5IyK-fpwg97whzKYk6UBzJUy5cFz9XzSrzngo4XwOfQ6YjPnw1BNJrGDnX4DESlOyHYVQjEqMeCNqMYq-BDTrhvgIMtuv7hdguxE25K-mdayGunQPvckbEwbnGhMru79w2W2n5JZeg0vKyVAaKoLKW-Xn4NGZ2g-RCbbKaemmfI_m1IVU0cHcRYGan3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ca1668589.mp4?token=Ked0BZA81nLV1Wr2ke_0JY2XL4L5-Rld8qA_J_shL13uUrwov5-DAN3c87Z-4-oYGCrwr4b9YuFGuWB1iXZcVf3ZPAgnt47vAQ2UcFIu5k5EzzIlwnOLqsKFAHCtchPejm4MRbJAUeV3vQZrbwFxR7m_Bp5IyK-fpwg97whzKYk6UBzJUy5cFz9XzSrzngo4XwOfQ6YjPnw1BNJrGDnX4DESlOyHYVQjEqMeCNqMYq-BDTrhvgIMtuv7hdguxE25K-mdayGunQPvckbEwbnGhMru79w2W2n5JZeg0vKyVAaKoLKW-Xn4NGZ2g-RCbbKaemmfI_m1IVU0cHcRYGan3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکر کارلسون در کانال ۱۳ اسرائیل:
🔹
فکر نمی‌کنم ایالات متحده به اسرائیل بدهکار باشد. فکر نمی‌کنم ایالات متحده باید چیزی به اسرائیل بدهد.
🔹
فکر می‌کنم باید تمام کمک‌ها به اسرائیل و تمام توافق‌های ویژه برای اسرائیل را از فردا متوقف کنیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/akhbarefori/653180" target="_blank">📅 12:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653179">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
غربالگری آسیب دیدگان دبستان شجره طیبه میناب
🔹
رئیس مرکز بهداشت میناب: معلمان، اولیا و آسیب دیدگان روحی بازمانده از حمله به مدرسه شجره طیبه، امدادگران و مردم شاهد حادثه، از نظر سلامت روان غربالگری می‌شوند.
🔹
این غربالگری از هفته آینده برای بررسی سلامت روان بیش از ۱۴ هزار نفر اجرا می‌شود.
🔹
معلمان، اولیا و آسیب دیدگان روحی بازمانده از حمله به مدرسه شجره طیبه، امدادگران و مردم شاهد حادثه، نیز از نظر سلامت روان غربالگری می‌شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/akhbarefori/653179" target="_blank">📅 12:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653178">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLDuzI3MTIk49R7Jje_kpgmRjYS8k1hT_J8_5jEZYUNllBmZqjtAqcmEoNGO8fnUFu8JEQXoaed2vaH-GZC33KJD5KCJ8z8Z1SM5ewybXMacKBtfqmPiWLgvpi49GCLJJ0KoKrA2RD2EwI6PHs3cNBQZ9D2zTa73Z_gASCf4y4wZXLpHYxQuJ4E9a7yvalr_2VN2VXIsyqqwqKGYZg6O1HZm_iq8sBI2jxevfpfUIYnTsazGgZVl6If4KH5UNhY19L5rQhgWXxigbfBklzoDTA3ut--sw9aHGP0WR79xv7063li9RlMFfivH0MbvTXY5i9ERIJLeqwxzGxDQrdXHew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دومین گفت‌وگوی تلفنی ترامپ و نتانیاهو در چند روز اخیر
🔹
رئیس‌جمهور آمریکا و نخست‌وزیر اسرائیل دیشب تماس تلفنی طولانی داشتند که بسیار مهم توصیف شده است.
🔹
آن‌ها یکشنبه با هم درباره ایران گفت‌وگو کرده بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/akhbarefori/653178" target="_blank">📅 12:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653177">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ih2Y8ZQjLCxbaWxdBLLVTTs8RmAuXyvG-gdRCJfp6A3EnCMvPlpkBHtFWZjV1nBDEp2MbS1j6UFnkRldzveBnfpJU4KQx5p19IHA_m0YZFsS8VDudSbpTUz4vhDMjrmxcOVCA0JeAJRyPg-z1RiZ8aHBI59ZNvKWvzXbk2x5HaYXISXIoFJdgLKKHgtfisJ6N8ChVpEpB-zUELdQQ5tw8eV6KWNswfzel38Q6kh32Tn31S_yxU3QPdqnfDRVIvK8tk3LrdzqSmJzJLILa4dGUXycbD3jWipnNpNrql1TRP-e1t4Vc3ucFZ_m9hdYKSDO8mv2ZN7pnyAfiIL3tT2A_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی فضای مجازی: باید نسبت به پاکسازی زیرساخت‌های کشور از سخت‌افزارهای آمریکا سریعا اقدام شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/akhbarefori/653177" target="_blank">📅 12:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653176">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
نشنال اینترست: فرمانده سنتکام در جلسه سنا به حقیقت و واقعیت توهین کرد
🔹
نشریه آمریکایی با اشاره به دروغگویی فرمانده سنتکام درباره کشتار غیرنظامیان ایرانی در حملات آمریکا، بی‌توجهی وزارت جنگ این کشور به تلفات غیرنظامیان در جنگ علیه ایران را نشان‌دهنده سیاسی‌کاری گستاخانه رئیس‌جمهور ایالات متحده دانسته که در حال گسترش در میان صفوف ارتش آمریکاست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/akhbarefori/653176" target="_blank">📅 12:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653175">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a53595853.mp4?token=h4hUM-CWjhNLrvWwiZLa6fjUKG7JbO8x_WvO3HxXpOXx4zhlkJPtpgXaD6GzGAeQhoy7xCIsTBY1OxAlZFItzvP11P901UMgw2Q-F51REtghwNQAzxRzqy1sAarLiXpdQn5gMz5H26qTKGrh_C6ZnwLHLPsLf2hgdAnTMLYtN0q4eo8lO-__6QLIB7mDOLgWFEvLwE7epdOFNsCSXd3BYfdY4RtQcKEoEdrLpZ_KG_-NDDYR6ll8CkfehpPn7IOHQgT2C0-KQuQYUIbxNfgpdvIBaXSyvl9y6hNyvR_9NJoS0iAcC61BSEQSJDB9JFXjUSew884DwQdHUA71jtZf_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a53595853.mp4?token=h4hUM-CWjhNLrvWwiZLa6fjUKG7JbO8x_WvO3HxXpOXx4zhlkJPtpgXaD6GzGAeQhoy7xCIsTBY1OxAlZFItzvP11P901UMgw2Q-F51REtghwNQAzxRzqy1sAarLiXpdQn5gMz5H26qTKGrh_C6ZnwLHLPsLf2hgdAnTMLYtN0q4eo8lO-__6QLIB7mDOLgWFEvLwE7epdOFNsCSXd3BYfdY4RtQcKEoEdrLpZ_KG_-NDDYR6ll8CkfehpPn7IOHQgT2C0-KQuQYUIbxNfgpdvIBaXSyvl9y6hNyvR_9NJoS0iAcC61BSEQSJDB9JFXjUSew884DwQdHUA71jtZf_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار فرمانده سنتکام از پاسخگویی درباره جنایت مدرسه میناب
🔹
فرمانده سنتکام را درباره جنایت مدرسه میناب به چالش کشید و از او پرسید، تا کی می‌خواهید «پشت این ادعا که تحقیقات ادامه دارد پنهان شوید؟»
🔹
مارک استون خطاب به کوپر افزود، تیمی از شبکه اسکای نیوز همین الان در میناب هستند. آنچه آنجا رخ داد را دیده‌اند. هیچ مدرکی دال بر وجود پایگاه موشکی در آنجا وجود ندارد.
🔹
درحالیکه کوپر در حال فرار از پاسخگویی بود مارک استون دوباره وی را سوال پیچ کرد و گفت، تا کی میخواهید پشت این ادعا که تحقیقات در جریان است قایم شوید؟ «حداقل بگویید تحقیقات چه زمانی پایان خواهد یافت؟»
🔹
فرمانده سنتکام به جای پاسخگویی مسیر حرکت خود را تغییر داد و تلاش کرد با کمک محافظانش از دست خبرنگار اسکای نیوز فرار کند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/akhbarefori/653175" target="_blank">📅 12:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653174">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdoWrdVs4gMzAPvAf8qprN43deK-2bBtPgsYugOi2k7ZAEBiIWxMVWwpdgA6HbjQhe98aTqrwU_XjMlnLRiVP97DKB6KybDpIcMFztioAFXcZf5os4qbNo78pMZWvJzIldc0HpVsYVYLYituCaZap0hZIQ_Fou78N8qdoHL4Sk7H1SuDTf-csUBPudSaEoZYItAXuyp2ksUrQ5dX18mDvaCqiMwAvUS8BFWVFgkW0KVC8Iz4PjgeQICPBa7T0pRgoy78l-I5CsL3TCTP3XG0kIJLqr3XAoIURyrLiOcF7UlZCdGoBJXn2huKEbamv9N3el2m14EnPLQahtQrIctVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاثیر جهانی فناوری پهپاد شاهد ۱۳۶
🔹
کشورهایی که نسخه‌های خود را با الهام از این پهپاد ایرانی توسعه می‌دهند:
🔹
آمریکا
🔹
روسیه
🔹
چین
🔹
اوکراین
🔹
لهستان
🔹
ترکیه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/akhbarefori/653174" target="_blank">📅 12:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653173">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
تکذیب ادعاهای بی‌اساس خبرگزاری مهر درباره حقوق کارکنان بانک مرکزی
🔹
در پاسخ به گزارش منتشرشده توسط خبرگزاری مهر تحت عنوان «پرسش‌هایی درباره افزایش مزایای کارکنان بانک مرکزی در شرایط فشار تورمی»، ضمن ردّ اتهامات و ادعاهای بی‌اساس مطرح‌شده، به منظور تنویر افکار عمومی تأکید می‌شود که هرگونه افزایش حقوق و مزایای کارکنان بانک مرکزی کاملاً بر مبنای قانون بودجه سنواتی و مصوبات دولت  بوده و هیچ افزایش خارج از ضوابط یا رقم بی‌سند «۲۰ میلیون تومانی» در کار نیست.
🔹
تمام حقوق و مزایا بر اساس سقف‌های مصوب قانونی کشور پرداخت می‌شود و هیچ نوع مزایا یا تسهیلات ویژه‌ای خارج از ضوابط سازمانی و قانونی به هیچ یک از کارکنان پرداخت نشده است؛ از این رو ادعای مطروحه در خصوص تسهیلات کذب محض بوده و صحت ندارد.
🔹
آن خبرگزاری بدون استعلام و کسب اطلاع قبلی از صحت و سقم مطالب مطرح شده، اتهامات بزرگی را به سیاستگذار پولی کشور وارد کرده است. در شرایطی که کشور درگیر جنگ تمام‌عیار اقتصادی و تحریم‌های ظالمانه است و بانک مرکزی در خط مقدم مدیریت نقدینگی، کنترل تورم و ثبات‌بخشی به بازار ارز قرار دارد، اتهام‌زنی بی‌اساس به سیاستگذار پولی نه تنها غیرحرفه‌ای، بلکه در تضاد با نیاز مبرم کشور به اعتمادسازی نسبت به سیاست‌های پولی برای دستیابی به اهداف اقتصادی است.
🔹
شایسته است خبرگزاری مهر توجه داشته باشد که در دوران جنگ رمضان، با وجود ابلاغ حضور ۲۰ درصدی کارکنان دستگاه‌های اجرایی، بیش از ۶۲ درصد از کارکنان بانک مرکزی در محل کار خود حاضر شدند و اجازه ندادند حتی یک لحظه چرخه نظام پولی و ارزی کشور متوقف شود؛ این فداکاری و مسئولیت‌پذیری سزاوار چنین اتهام‌زنی‌هایی نیست.
🔹
بی‌تردید در شرایط حساس کنونی که دشمنان نظام از هیچ تلاشی برای ضربه زدن به اقتصاد ایران فروگذار نمی‌کنند، باید منشأ چنین اظهاراتی بررسی شود تا مشخص گردد کدام جریان به دنبال تخریب سیاستگذار پولی کشور و ایجاد بدبینی عمومی نسبت به بانک مرکزی است. از خبرگزاری مهر انتظار می‌رود به جای دامن زدن به شایعات، امانت در انتشار اخبار را رعایت کرده و در مسیر حمایت از ثبات اقتصادی کشور گام بردارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/akhbarefori/653173" target="_blank">📅 11:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653172">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnTWQZwsr-dDF47hlNtzcZhymcIV3xDsWODlEg7tLThbfzeDCF-rds3d7FmSCeTvHI8GJww62YwWhz3fZIhQvPf30kOWFTb1uH_YwY5_AsY19l--LiAdFJry46BAGQ2jBhGmtxjM1IaN9-rL5D32_-LPLfMmBYGXri72siRrKVN9nXEnZJoArm-LZjXKUXH31PXi_cnrPFsxduE7HBdp2QMZr6vX1ivHEBnPiJaW-i9yhl22uGsLtWgkJLoEgkQXOUTMKQq4jHFFcmwlc5QtXmRASWfLRmCnkMbOY9gjreJ6hpwuRvuVDldaM0dM0peNslj7vuND1KWb4ml1-hvlfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصوبهٔ جدید قیمت چای اعلام شد
🔹
براساس مصوبهٔ جدید کارگروه تنظیم بازار کالاهای کشاورزی، تشکل‌های مرتبط موظف شدند با هماهنگی سازمان حمایت، قیمت انواع چای را به‌صورت دوره‌ای تعیین و اعلام کنند؛ دولت همچنین بانک مرکزی و وزارتخانه‌های صمت و راه را مکلف به کنترل بازار چای کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/akhbarefori/653172" target="_blank">📅 11:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653171">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
شی و پوتین حملات آمریکا و اسرائیل به ایران را محکوم کردند
🔹
رئیس‌جمهور روسیه و چین امروز در بیانیه‌ای مشترک حملات نظامی آمریکا و اسرائیل به ایران را محکوم کردند.
🔹
در این بیانیه آمده است «طرفین اتفاق نظر دارند که حملات نظامی آمریکا و اسرائیل به ایران، ناقض حقوق بین‌الملل و اصول اساسی روابط بین‌الملل است و به‌طور جدی ثبات در خاورمیانه را تضعیف می‌کنند».
🔹
دو طرف در بیانیه مذکور، بر ضرورت بازگشت هرچه سریع‌تر طرف‌های درگیر به گفت‌وگو و مذاکرات با هدف جلوگیری از گسترش دامنه درگیری، تأکید کردند.
🔹
آنها همچنین از جامعه بین‌المللی خواستند موضعی عینی و بی‌طرفانه اتخاذ کند، به کاهش تنش‌ها در منطقه غرب آسیا کمک کند و به‌طور مشترک از اصول بنیادی روابط بین‌الملل حفاظت کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/akhbarefori/653171" target="_blank">📅 11:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653170">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGHkrR0JauLnTrQnNNCy2NzOhUcolCXhYCRmglumGDRQ8vMEBKAoLSlKuKkGEYfZexli9e7sOqv7Feg3fr5cyYwJ-arqbKd69tSSqT05kjCH0nmX-0qYsdH6rPr8yZwqjFp4ou859YNQ2VOIuAkhx6fkpfdhlUInl623khtdffTDrldk0jOyXb6sZy04BZ0YztCExG63xVzCvIA6LjbAP-7Fzz4P2FYWKnYzXdPcyzMVQNfCJyHWN4GC6gS-I1P0CiCudLMwtEK-j6AkKB_n8kNIem1B_gZIro1TbfTJ_8RgniySKFXcv4hDK9RKaxROx6afvci3ncw3OvV-cQbnYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشت خشخاش ممنوع است
🔹
قوه‌قضائیه: براساس قانون کشت گیاهان مخدر از جمله خشخاش «مطلقاً ممنوع» بوده و مرتکبان با توجه به اهمیت و تکرار جرم، به مجازات‌های قانونی محکوم خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/653170" target="_blank">📅 11:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653169">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
یک سوم جمعیت کشور تا ۳۰ سال آینده سالمند می‌شود
🔹
وزیر فرهنگ و ارشاد اسلامی در همایش روز ملی جمعیت: اکنون جمعیت سالمند بالای ۶۰ سال ما حدود ۱۲ میلیون است، اما در سه دهه آینده مطابق نرخ باروری ۱.۳۵ که داریم، جمعیت سالمند کشورمان معادل یک سوم جمعیت کل کشور می‌شود.
🔹
ناترازی جمعیت کمتر از ناترازی آب و برق نیست؛ اما چون بحران آب و برق روزمره دیده می‌شود، ما را درگیر می‌کند، در حالی که بحران جمعیت پنهان است و زمانی متوجه عمق فاجعه می‌شویم که شاید برای جبران خیلی دیر شده باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/akhbarefori/653169" target="_blank">📅 11:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653168">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68cacafa4c.mp4?token=VFQppqUB461EEZOmMiLXeopWIUpdHlvJtcLxQjLnph8jL1QoMmFAqIWAn5lzoHXb2gfuqGZjirg6HgNoNyNXBmHRewO_wOqf_9j4sLNPmaPRNXbOY6ubQFvZLTIx_yB3yVn1fr_3MR6F_eR7v-KySNFGznB_Vz3ehmSo7W-Yih_c4VlgrwzYBsFM8uTz3wjqxU9khUK8Xn8J-1htx2p8tH59eNDCBLx4Bq32g-09BtD0xIBNqrxbzw_8e5rEQ3riIAzzqigoYdPqVapmgCscWNCx7gubzRolKw3xpk6x3v1lZbkDyn-q-uJKOqaAKgwEax9lnr9toWdWPE5w88jO_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68cacafa4c.mp4?token=VFQppqUB461EEZOmMiLXeopWIUpdHlvJtcLxQjLnph8jL1QoMmFAqIWAn5lzoHXb2gfuqGZjirg6HgNoNyNXBmHRewO_wOqf_9j4sLNPmaPRNXbOY6ubQFvZLTIx_yB3yVn1fr_3MR6F_eR7v-KySNFGznB_Vz3ehmSo7W-Yih_c4VlgrwzYBsFM8uTz3wjqxU9khUK8Xn8J-1htx2p8tH59eNDCBLx4Bq32g-09BtD0xIBNqrxbzw_8e5rEQ3riIAzzqigoYdPqVapmgCscWNCx7gubzRolKw3xpk6x3v1lZbkDyn-q-uJKOqaAKgwEax9lnr9toWdWPE5w88jO_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قائم پناه معاون اجرایی رئیس جمهور: جمهوری اسلامی آماده است در مقابل حوادث طبیعی و  جنگ و یا حمله از تک تک آحاد ملت دفاع کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/akhbarefori/653168" target="_blank">📅 11:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653166">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
جنگ منطقه‌ای که وعده داده شده بود با تکرار تجاوز، به فراتر از منطقه کشیده خواهد شد
🔹
بیانیه سپاه پاسداران انقلاب اسلامی: دشمن آمریکایی صهیونی که از شکست‌های بزرگ و راهبردی مکرر از انقلاب اسلامی درس نگرفته و بار دیگر زبان به تهدید گشوده بداند، اگرچه آنها با تمام توانایی‌های دو ارتش که پر هزینه ترین ارتش های جهان هستند به ما حمله کردند اما ما همه ظرفیت های انقلاب اسلامی را علیه آنان وارد عمل نکردیم.
🔹
اما اینک اگر تجاوز به ایران تکرار شود جنگ منطقه‌ای که وعده داده شده بود، اینبار به فراتر از منطقه کشیده خواهد شد و ضربات کوبنده ما در جاهایی که تصور آن را ندارید شما را به خاک سیاه خواهد نشاند.
🔹
ما مرد جنگیم و قدرت ما را در میدان نبرد خواهید دید و نه در بیانیه های توخالی و صفحات مجازی.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/akhbarefori/653166" target="_blank">📅 11:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653165">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
‌ابلاغ سهمیۀ بانک‌ها برای وام ازدواج و فرزندآوری
🔹
براساس ابلاغیۀ بانک مرکزی به شبکۀ بانکی، در سال جاری ۴۳۵ همت تسهیلات قرض‌الحسنۀ ازدواج و فرزندآوری پرداخت می‌شود که از این میزان ۳۵۰ همت برای ازدواج و ۸۵ همت فرزندآوری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/akhbarefori/653165" target="_blank">📅 10:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653164">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0686366cf9.mp4?token=lqPfNfSCzV5MHS1DWIYAW60XeG6CPyT8hEq4iLFZWEsciioYsliu40lT8iOZQWHMze96FweP7VSuuEZcjgTd1m211jJSdtDi2mV6WPIy9O2nzrv-7EPKBsfUpy2nxs4n9iRJJ_CGEEcLZdPMx4FQCcgSzFe037Iymcr1UW5Ub_Wr31-I1HNkMz4pJkqZF18WFQqgCsB_OYBRhul0h0_GRGgYNfMwfYyDJny74FZv1SQWL8bjZruoPHGxwb2WSP_ik8fEjBp59fQuTMyYZs3Kofr50M_PMcYsdr2LMebp7IBrmRGMikclrnCxyMp87NDE45cDfnIvAvYt_uBpEJVbQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0686366cf9.mp4?token=lqPfNfSCzV5MHS1DWIYAW60XeG6CPyT8hEq4iLFZWEsciioYsliu40lT8iOZQWHMze96FweP7VSuuEZcjgTd1m211jJSdtDi2mV6WPIy9O2nzrv-7EPKBsfUpy2nxs4n9iRJJ_CGEEcLZdPMx4FQCcgSzFe037Iymcr1UW5Ub_Wr31-I1HNkMz4pJkqZF18WFQqgCsB_OYBRhul0h0_GRGgYNfMwfYyDJny74FZv1SQWL8bjZruoPHGxwb2WSP_ik8fEjBp59fQuTMyYZs3Kofr50M_PMcYsdr2LMebp7IBrmRGMikclrnCxyMp87NDE45cDfnIvAvYt_uBpEJVbQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا سرشار: جنگ فعلی ۸ سال طول نمی‌کشد و حداکثر در همین یکی دو ماه جمع می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/653164" target="_blank">📅 10:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653163">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b013a6c4.mp4?token=pO1W8cYPkZcWSUlD55r_Qr79H2xR33QtB9omTt-WH4GmbwlT0PZM7S2KSP_ox43m_szHBcC3_UalvrwNl6E62stGgdLQqobeMGmdEQlakikIKV_e4bYFinscAXyW_AAAe8ZqK-ki76C4LazdTBShv7o4Oy9horK-Eg5gJkeSnTyP1GSeoP8S7sC4KjXIWor5KLS2_9uaZYbbxdjOuJweWwiyxOHHKw2XylUuD7gYX9ziyWEtKb6MdPWytBJlC9MVKaQvuewANqQ3UHYLu3BdNtHkWH02SFHJe0C15pmxmHc1cyNGPD7gHXDzRqGTEqV-uRsbsB-8dwBqdr-n_iSevQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b013a6c4.mp4?token=pO1W8cYPkZcWSUlD55r_Qr79H2xR33QtB9omTt-WH4GmbwlT0PZM7S2KSP_ox43m_szHBcC3_UalvrwNl6E62stGgdLQqobeMGmdEQlakikIKV_e4bYFinscAXyW_AAAe8ZqK-ki76C4LazdTBShv7o4Oy9horK-Eg5gJkeSnTyP1GSeoP8S7sC4KjXIWor5KLS2_9uaZYbbxdjOuJweWwiyxOHHKw2XylUuD7gYX9ziyWEtKb6MdPWytBJlC9MVKaQvuewANqQ3UHYLu3BdNtHkWH02SFHJe0C15pmxmHc1cyNGPD7gHXDzRqGTEqV-uRsbsB-8dwBqdr-n_iSevQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرود بالگرد نظامی رژیم اشغالگر در بیمارستان رمبام که تعدادی از مجروحان ارتش رژیم صهیونیستی را انتقال داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/akhbarefori/653163" target="_blank">📅 10:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653162">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60095701d8.mp4?token=qtlDREG4xgZedk-IIIj46jO1zXf1RaYV3TiJPB-KSbwH1gMOzVo_TPXIL2GHgma99utQc1MVUnAReKJJJ70YCbYbH1URG39k9gxXS3Gg5I6L5Z-BAMQ1lAOpZN0whItTWU6ReIYDeqXFmHkTUCOxLbvy7HSmsCHu3qPhfmnpRnAOx2oE7hFxzv3Q4OGor1CNQW6zNQWvGNEib1W183t_gii5oZKqk8JNayUhRvXB23betsWSe_YGCYByNh7I-t0xWSJL1zcp8KKgH7_jFJtdI5vyk5qUS9_TNQ8b8PSUHP0obTDJEZNNgY3aZxAIDwa3SRxLG-XsU5-VdGYMa0U_5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60095701d8.mp4?token=qtlDREG4xgZedk-IIIj46jO1zXf1RaYV3TiJPB-KSbwH1gMOzVo_TPXIL2GHgma99utQc1MVUnAReKJJJ70YCbYbH1URG39k9gxXS3Gg5I6L5Z-BAMQ1lAOpZN0whItTWU6ReIYDeqXFmHkTUCOxLbvy7HSmsCHu3qPhfmnpRnAOx2oE7hFxzv3Q4OGor1CNQW6zNQWvGNEib1W183t_gii5oZKqk8JNayUhRvXB23betsWSe_YGCYByNh7I-t0xWSJL1zcp8KKgH7_jFJtdI5vyk5qUS9_TNQ8b8PSUHP0obTDJEZNNgY3aZxAIDwa3SRxLG-XsU5-VdGYMa0U_5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوتین و شی بیانیه مشترک تعمیق روابط دو کشور را امضا کردند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/akhbarefori/653162" target="_blank">📅 10:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653161">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAl8cIZtb0jsGO4AYbFFf10h366xGuo4iKuLsSQdSMXcJDcepVzH6QSL8vcK2BSXMBPui2rR0PxRr8yshIPfvkO0YODuIMZxsrflxqPPsd4mYB4yDXePJSs6r0NaFlOwqZv_FA-EQ_DNmddvCy0uqK8IVAzgA4zDjF9G4WDwDgheDMP5tYjiBl9oV-EgAv5y1aijVQxHIDydgXbZiZoPXxUUhZmruNrH84s-nzL-Mh9wf0MYnZM7C5w4GFFNcrYpsk9ShBNsTvZ6VouBpsP3CEGTUH48cteT1MNG-nxc7KdB_cwXe-JWkKfycnNza86GXuxkeyDs4YMiYp3_8mzTew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس‌جمهور: اگر برای مدیریت مصرف برنامه‌ریزی دقیق نداشته باشیم، در ادامه با مشکلات مواجه خواهیم شد
🔹
پزشکیان در نشست سراسری استانداران کشور: روش‌هایی که تاکنون برای اداره کشور مورد استفاده قرار گرفته، در شرایط فعلی به‌تنهایی پاسخگوی همه مسایل نیست.
🔹
ضروری است با نگاهی نو، روش‌های جدید و راهکارهای خلاقانه برای عبور از مشکلات طراحی شود.
🔹
یا راهی پیدا خواهیم کرد یا راهی تازه خواهیم ساخت؛ اما لازمه این مسیر، رها شدن از قالب‌های ذهنی محدودکننده و نگاه‌های محدود در تصمیم‌گیری است.
🔹
اگر روش‌های پیشین به‌تنهایی قادر به حل مسایل بود، بسیاری از مشکلات تاکنون برطرف شده بود.
🔹
اگر برای مدیریت مصرف آب، برق، گاز و بنزین برنامه‌ریزی دقیق نداشته باشیم، در ادامه با مشکلات مواجه خواهیم شد.
🔹
باید مردم را برای صرفه‌جویی و مدیریت مصرف به همکاری دعوت کنیم تا بتوانیم کشور را با عزت و اقتدار از شرایط فعلی عبور دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/akhbarefori/653161" target="_blank">📅 10:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653160">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp0ZXp0-K1OwL4fLMJm4P5ClwFeT_L2aRsY1eThxc0tnOOlAy5LYjPjPwvlpLn0yUUetOKQr0TKaxm7EMTyVpfHSBhlKMnzXvPPOUoAqDtunEef-bdHVY0hVdFmkwCDxxu-yWs5FvKjeUG9SXKj3_8T7cql3UqEFG6QTh_g_4dMrQhu_TyGLCZGYiTYd6bc1M7saYyzXNo68Pd-gdLWU5C-Q9UxPqPUwr-XcmyhFZTj6P53YwdeEeJCeLV1xof5llhDm7IPyM5J2d1kTtyGJdAo46vVUlK8KFi4lDxA7-sDHPacYzLkCrvskcTMo94emmPs1whcdD5IFCc3cWuswWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران: در صورت از سرگیری جنگ هیچ آتش‌بسی را نمی‌پذیریم
🔹
سفارت جمهوری اسلامی ایران در وین امروز و در پی ادعاها و تهدیدات دونالد ترامپ رئیس‌جمهور آمریکا درباره حمله به ایران عنوان کرد: چرا رئیس‌جمهور آمریکا (دونالد ترامپ) معتقد است که انجام یک حمله‌ به اصطلاح «کوتاه» به ایران، تهران را به مذاکره بیشتر متمایل می‌کند؟
🔹
در این پیام که در صفحه ایکس این سفارتخانه منتشر شد، آمده است: بر اساس همین فرض اشتباه، که ناشی از برداشت عمیق نادرست از واقعیت ایران است، پیش‌بینی کرد که جنگ کمتر از یک هفته طول خواهد کشید، اما این جنگ ۴۰ روز به طول انجامید.
🔹
سفارت جمهوری اسلامی ایران در اتریش در این پیام خاطرنشان کرده است: اشتباه نکنید: اگر ایران مجدداً مورد حمله قرار بگیرد، این بار تا زمانی که همه اهدافش به طور کامل محقق نشود، با هیچ آتش‌بس یا مذاکره‌ای موافقت نخواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/akhbarefori/653160" target="_blank">📅 10:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653159">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a4b6ad821.mp4?token=ert23TTPfhIThKcFzLPa4TZVTWFxDvMHRXt78SAP9mzXj0NyhaUbE-HL4CT66Q4l4PNxn6s2HS9Jo4dv57fm0tG888uRNf3sQFUIycPbyRFZS1wUE1JDObqskJOEDT7pZQI0HQ8mLkO6FAqhc1ldPq7DL9Esiz7kidKp-6l3C68RCupFcREA5_4Y79Bf4o5anYjOiMjajhYZliCGKl1gEvOs0USujd8i2AAv4IK_jAa2Hs434CSMs4a6JYIJcqxMChBB9HPB6pj7DF2GxqzdttWihXcK76c1vPKuVHdIbsbl6ViLEG8fJShhstfXGHuEdNjJVf9uE1FozEh4A9g8KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a4b6ad821.mp4?token=ert23TTPfhIThKcFzLPa4TZVTWFxDvMHRXt78SAP9mzXj0NyhaUbE-HL4CT66Q4l4PNxn6s2HS9Jo4dv57fm0tG888uRNf3sQFUIycPbyRFZS1wUE1JDObqskJOEDT7pZQI0HQ8mLkO6FAqhc1ldPq7DL9Esiz7kidKp-6l3C68RCupFcREA5_4Y79Bf4o5anYjOiMjajhYZliCGKl1gEvOs0USujd8i2AAv4IK_jAa2Hs434CSMs4a6JYIJcqxMChBB9HPB6pj7DF2GxqzdttWihXcK76c1vPKuVHdIbsbl6ViLEG8fJShhstfXGHuEdNjJVf9uE1FozEh4A9g8KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قائم پناه معاون اجرایی رئیس جمهور: دشمن رهبر انقلاب را شهید کرد اما ما تسلیم نشدیم و بلافاصله ایستادیم و به ابرقدرت دنیا پاسخ دادیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/akhbarefori/653159" target="_blank">📅 10:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653158">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
رئیس‌جمهور کره جنوبی: اسرائیل شهروند ما را ربوده است
🔹
لی جائه میونگ رئیس جمهور کره جنوبی در پی بازداشت یک فعال شهروند کره‌ای توسط نیروهای اسرائیلی در کاروان کمک‌رسانی به غزه (ناوگان صمود)، بیانیه‌ای تند علیه اسرائیل صادر کرد.
🔹
او در این بیانیه اعلام کرد: اسرائیل یکی از شهروندان ما را در شرایطی ناعادلانه و برخلاف قوانین بین‌المللی ربوده است.
🔹
لی همچنین با اشاره به واکنش کشورهای اروپایی افزود: بیشتر کشورهای اروپایی می‌گویند ناچارند بنیامین نتانیاهو را بازداشت کنند؛ ما نیز باید تصمیم خودمان را بگیریم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/akhbarefori/653158" target="_blank">📅 09:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653157">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBlUfddUUE5n8p_6xxUmyRsPMdIDa3mqpn9dTd9LHSEFtb1gYJpMrSwn1pQdi0UrwRB_HZ3WZDxAMSjBX38QKtJQU-nULIx_vwdqfP0ysPsK4B3Iiu98Tk54RpFHHKEJFg08aunLf0TYeEe_cNjUT2xacYjHHz2IqSeCRFWmwNtK_H6l3w9zwfquT50_c73OH4v62XQyMfFQLkUx_yG3m5zGl9r-WUpN3gGsIkrjbGYA1U7JeVqsgTKV6YOYN88XBzLSH8Pp5IZqeLBs710yBNB8jTvYhlTO2gDn4Rb8ZuIESKkYsawClxxFqfPEqU_4X8RlOlebgX5dg9XJT3BT3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روند تخلیه و انتقال کالاهای اساسی با جدیت پیگیری شود/ لزوم ساماندهی فوری بازار اجاره مسکن
🔹
رئیس سازمان بازرسی کل کشور در دیدار با وزیر راه و شهرسازی با تأکید بر ضرورت آمادگی مستمر دستگاه‌ها در شرایط جنگی و پساجنگ، خواستار فعال‌سازی ظرفیت بنادر شمالی و تقویت مسیرهای ریلی و زمینی شد و گفت: روند تخلیه و انتقال کالاهای اساسی با جدیت پیگیری شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/akhbarefori/653157" target="_blank">📅 09:49 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653156">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
انفجار پهپاد حزب‌الله در ساختمان محل حضور نظامیان صهیونیست در جنوب لبنان
🔹
یک پهپاد انتحاری متعلق به حزب‌الله که با فناوری فیبر نوری عمل می‌کند، در داخل ساختمانی در جنوب لبنان که نیروهای ارتش اشغالگر اسرائیل در آن سنگر گرفته بودند، منفجر شد.
🔹
این انفجار منجر به زخمی شدن فرمانده لشکر ۴۰۱ و تعدادی از نظامیان شد که با هلیکوپتر به بیمارستان‌ها منتقل می‌شوند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/akhbarefori/653156" target="_blank">📅 09:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653155">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
زخمی شدن فرمانده تیپ زرهی ارتش اسرائیل در جنوب لبنان
🔹
پایگاه خبری صهیونیستی واللا گزارش داد که فرمانده تیپ زرهی ۴۰۱ و چند نظامی این رژیم در حمله پهپادی حزب‌الله زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/akhbarefori/653155" target="_blank">📅 09:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653154">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
دبیر ستاد ملی جمعیت: با این فرمان جلو برویم در سال ۲۱۰۰ میلادی ۳۱ میلیون جمعیت خواهیم داشت!
🔹
دستجردی، دبیر ستاد ملی جمعیت: اگر ما با این فرمانی که داریم جلو می‌رویم که نرخ باروری ما پایین ‌ترین حد هست، پیش برویم در ۷۵ سال آینده در سال ۲۱۰۰ میلادی ما ۳۱ میلیون جمعیت خواهیم داشت و دیگر نیازی به جنگ نخواهیم داشت، خود جمعیت آنقدر کم خواهد شد که در حقیقت ما از صحنه جغرافیای دنیا حذف می‌شویم.
🔹
اگر بتوانیم وضعیت خودمان را ارتقا بدهیم نرخ باروری را به ۱.۹ برسانیم ۶۲ میلیون نفر در ۷۵ سال آینده جمعیت خواهیم داشت و اگر بتوانیم بیشتر موفق باشیم و نرخ باروری افزایش بدهیم، بالای ۱۰۰ میلیون جمعیت خواهیم داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/akhbarefori/653154" target="_blank">📅 09:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653153">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed19b408e4.mp4?token=AU088WmLNnNa_JDpHMHJEnKMkQGtGLK9HPVIBfU-eEQHc9VVirvVaTTsRYB_zpnsi31-96bZOZjJA2i_L9oNSX0yVf7ml3hatQrIbCFEaLwkuOkigXbJMbD-FNqN1m_O3z0_yohCwX485jjBUSrbZn3GfJM83bu-AhbVwdvK0vDNwWXUvecNyRY4HjaUoRqf-ziiAgy-uqsQrAYEvGRdA0jEC8W42CEjtDM4dIY0QKXBj52mxo-NG3hDG5eRHuScqvH8b2lTwteafwq-5iDh1O4RB3tQEfcwsXBkW_GkjV2JuokOwzhP9PtKSL-mnelX2OB7QoURPz2v9tuzEoNyVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed19b408e4.mp4?token=AU088WmLNnNa_JDpHMHJEnKMkQGtGLK9HPVIBfU-eEQHc9VVirvVaTTsRYB_zpnsi31-96bZOZjJA2i_L9oNSX0yVf7ml3hatQrIbCFEaLwkuOkigXbJMbD-FNqN1m_O3z0_yohCwX485jjBUSrbZn3GfJM83bu-AhbVwdvK0vDNwWXUvecNyRY4HjaUoRqf-ziiAgy-uqsQrAYEvGRdA0jEC8W42CEjtDM4dIY0QKXBj52mxo-NG3hDG5eRHuScqvH8b2lTwteafwq-5iDh1O4RB3tQEfcwsXBkW_GkjV2JuokOwzhP9PtKSL-mnelX2OB7QoURPz2v9tuzEoNyVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم نباید خسارت‌های وارد شده به آمریکا و رژیم صهیونیستی را فراموش کنند
🔹
داوودی، کارشناس مسائل بین‌الملل: طبق منابع خودشان، کشته‌های آمریکا در جنگی که ورود زمینی نداشتند: ۸۰۰ تا ۹۰۰ نفر / کشته‌های اسرائیل: بیش از ۱۶۰۰ نفر
🔹
زخمی‌های آمریکا: بالای ۱۰۰۰ نفر / زخمی‌های اسرائیل: بیش از ۸ هزار نفر – در حالی که هر دو طرف آمار را خیلی پایین‌تر اعلام می‌کنند.
🔹
خسارت انسانی فراتر از تصورشان است. حتی منابع آمریکایی می‌پرسند: این همه تلفات برای سربازانی که وارد جنگ نشدند، یعنی چه؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/akhbarefori/653153" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653152">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH6rRfYdLk1v__rCwP1asl8jofLVAUjnt7ykZtx8I0LtqKwyZmO2Y0b0c56IllJZHRK7fkKVvm3F_lp8mfzQ0ArRCriwe5uqZsa1-HQQz0955ZgG8QK_zazcql2W3iRA9iH8z8McRC65unNrZIWp29WLqcWqUZ4jB6j8SkkfskKSd00376YUSOXLUHhn7JRstLS7GJcswwOv_HrJq5pQ0rvc7yUb1Fx6zktMAHml070KsVphJec-e_XDNX6iEPfxyhzD6-9_4h0MJ8Aw8Kqz83hXAWp9SDr4rOf8taxsvjp37DLDfju1FLnvoREI2sm2PI90CogmdMYHYjid2iGHjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای نیویورک تایمز: هدف اولیه جنگ، انتصاب محمود احمدی نژاد به عنوان رهبر ایران بود
🔹
بنا بر ادعای نیویورک تایمز، درباره این طرح با احمدی نژاد مشورت شده بود اما پس از مجروح شدن وی در حمله اسرائیل به خانه اش در تهران در روز آغازین جنگ، این موضوع آشکار شد. مقامات آمریکایی گفته اند که هدف از این اعتصاب رهایی او از حبس خانگی بوده است.
🔹
نیویوک تایمز مدعی شد: احمدی نژاد جان سالم به در برد اما پس از آن از تلاش برای تغییر، سرخورده شد و از آن زمان تاکنون در انظار عمومی دیده نشده است و محل نگهداری او مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/653152" target="_blank">📅 09:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653151">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
کرمان امروز تعطیل شد
🔹
استانداری کرمان: به‌دلیل هجوم ریزگردها و آلودگی هوا، اداره‌ها و دستگاه‌های دولتی استان به استثنای مراکز امدای و خدماتی امروز تعطیل است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/akhbarefori/653151" target="_blank">📅 08:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653150">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
شی: جنگ علیه ایران باید متوقف شود
🔹
رئیس جمهور چین در دیدار خود با پوتین گفت مذاکرات بسیار مهم هستند و جنگ علیه ایران باید متوقف شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653150" target="_blank">📅 07:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653149">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-QHMAm_5efdK_hw8Dl-4QkIx483jgOM8_V4ujABcy3RxKAv4rsQysAa4LnN1zbVOoQXXWFqIR2lTOGFkeAPDUnl71TzHXauHZ3ioCKdYrtJRF7f5XabrqLd-Aw0OdyKWwph1tTI8NT0e6Xs1aH1j7SSdtzQbulw-BZhV4xyreL-ZzUh2C-yMT_1OCoLbxhCBAYWYCk_3Uw33JoBlTQhUr9iUu0iascob5w-5i9-uxou_pVQ6enXjnyfkUFscyjRDZmzp4WFQOSDE3jlUp3omZVH-vMIdgjIXVppSwzxTwdwElbV3cJlELbLlKpT2K3gqHP4B_eQPoBJT2EEnuSeQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۳۰ اردیبهشت ماه
۳ ذی‌الحجه ۱۴۴۷
۲۰ می ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/653149" target="_blank">📅 07:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653148">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
حکم قصاص قاتل الهه حسین‌نژاد اجرا شد
🔹
حکم قصاص قاتل الهه حسین‌نژاد، با درخواست اولیای دم و پس از طی تمامی مراحل قانونی و قضایی اجرا شد.
🔹
حکم قصاص قاتل الهه حسین‌نژاد با درخواست اولیای دم و پس از تایید حکم در دیوان عالی کشور به اجرا درآمد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/akhbarefori/653148" target="_blank">📅 06:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653147">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzAgaJgmJ2iQHGAwGYAOi6bPFkUInjV8DsgKW8I4v6DFLfP5iq1ssRBdQiwHWPURSi3m7KJZc7IVcgCt9qy8VLmpKC_Vq42lb0UenIK4ALalt4o0-9-4VTiJ8-Rvsl-PQo6ZZhhJdUuaz8dPKs9VFSupr2TeEmygPR_IhWpDP8CnJom906cFbJyDuQBFuFfL2IaK8v1u46C2GIJPcZAitSGRR74vp2UvwCg9DZcVxC5xowgX-g7CZm74ImSIKL6RkvEuEICC6kQXExf5QXZube617FO3ODpdBN-9_hgM2OPYf2iyP4IwDSwUFywI-fMoVFlZxcdkRIZxt1dF37s6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار روسیه درباره انجام آزمایش هسته‌ای توسط دیگر کشورها
🔹
«سرگئی ریابکوف» معاون وزیر خارجه روسیه بامداد چهارشنبه گفت که روسیه به‌طور متناسب به انجام آزمایشات هسته‌ای توسط هر کشوری، واکنش نشان خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653147" target="_blank">📅 06:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653146">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWhpSqjgXYXHUXXGZrWVqpNJswpZfctwAIAGRF8gcF9U4zC9ZhGbvA_kJpqWHCe60_JHv5fkVyMeXAR7udD4sTFpJTVZnIi1yjAGCl-YVaEeV_dWWT_WgGA2KLbZtZ15bORaaRoiABQOWGL4mz_BlX55TBu5-smwPmNIfjHQ_bR5VHCmnfv3_gaKQYCi4-lP1-0q80N4VcMSuBvZnlTrhSH2a_d2L3orU4kMC1zaHW63Z5x6IWWouTypuzNAeS28SvnlKUiLtE1fGbt5NFfrAzjGuEkxc240AMi2fxCVMQlfKIW89f5JRQ_HpL9SB6Be32eTdppn0ruMHmC3bCjfSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایرباس هزینه‌های جانبی خود را به دلیل جنگ آمریکا علیه ایران کاهش می‌دهد
🔹
شرکت بزرگ هواپیمایی ایرباس به دلیل آشفتگی ناشی از جنگ آمریکا و اسرائیل علیه ایران، از نمایندگی های خود خواسته است که «هزینه‌های غیرضروری» را ۱۰ درصد کاهش دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/653146" target="_blank">📅 04:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653145">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpIrxMgD0il5syVhivwdYE5OjonlusfZ_Dd_5mCCgLQU6y1XgdCUBzuUH009Xye4VqvZsJitIbUNXz50WJ6mBJc8YIrrgH8L1Xvr7amsS4su46Ak9wi3RYDUeGl7V0RlVqMCCeAMR1SLsRq1WMM4cljiO136XlY4Vt-XY3ptlhh7W48h5zLmfP_4lmp7ucIYFmfiPP0u4_s787Zo5da2D7gNZ8zKZVRfvjhKFGWqK9BwOYJUeQQo58KaYctS21k9A9yetObA8ZqRu6HQ_DtKqTircjEuqaW_wrI44kG2cYjKqwbdgnD8mw60Uk5DyFXLmdfnCmvHiTf6xUbdkP9yNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقام حماس: اسرائیل از ورود دارو به غزه جلوگیری می‌کند
🔹
مرداوی، عضو ارشد حماس: رژیم‌صهیونیستی به مفاد آتش‌بس در غزه پایبند نیست و اجازۀ بازسازی بیمارستان‌ها را نمی‌دهد.
🔹
بیشتر کسانی که توسط اشغالگران در غزه کشته شده‌اند، غیرنظامی هستند. اسرائیل به مفاد توافق پایبند نیست.
🔹
اشغالگران اجازۀ بازسازی بیمارستان‌ها یا ورود دارو و اسکان موقت به نوار غزه را نداده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/akhbarefori/653145" target="_blank">📅 03:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653144">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua5SeezokOZngeo_xFfBTcjLwe3LdDkT5H12IywxfBwz7UnpJDr0Ig6mQqfFZ5d8YbR0H-gp9mHX7UU2GfXk_caIlG58abdfq4eq57zXBuIUDp1zLHlI8p0qC8sQ-oQ8R2kEggfUu_FTwC3jfvHtGNiTZNtl9qHTmTH80MRnCGSYoPJ_D7YY4TgHVfDgi41-JtUGxfLalUbbNyBG_hox4dm_6maBBMdO8WP92Gy7QeSl58tbzZDt1neklaiqbUwn-nE2ZxdTDc7quRfl3QPcgyaAq3EytAQ4U-jfK-qJQb0t6twvhwE3B74tw3kcDDvY8zTy60TnePIAttt5j1FRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تأکید بقائی بر محاکمه و پاسخگویی آمران و عاملان جنایت میناب
🔹
سخنگوی وزارت امور خارجه بامداد امروز با بیان اینکه تقلای شرم‌آور آمریکا برای توجیه جنایت میناب نمی‌تواند ماهیت این جنایت را مخفی کند، گفت: فرماندهان نظامی و مقامات آمریکایی که مسئول صدور دستور و اجرای این حمله فاجعه‌بار بوده‌اند، باید طبق قوانین بین‌المللی کاملاً پاسخگو و محاکمه شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/akhbarefori/653144" target="_blank">📅 02:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653143">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu1yHQqYSoTG114XP_gCYYEVz1wtQte7-twwElrFHwswa3COo-mbRTm_qOVtKlFTp9OCvSFgXyxjW44obpjSBFB7LCAX8U9_I97c2O9FyjlzydtQGPzpGIJjFqesuB9dGA0oIKO5t7hF0xWEsYUcJE6DtlKHNsE0DJ4v7Nhk58dbilJNCvbMGOCsIPocrJKtM391cscxlLISWk1zDGQNY1ub8Av49v8n-i_iHZKLVKDKOGk5WMtA97dyiQ5M_hBsJ-B79JBEXIuuiMP3HzOCByYV0UB0FmNd9rgPbS4ells9dfYgoRy7zzGIG1xaKDQ-toBiWmmhmYCbhK26B9yYJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایندگی جمهوری اسلامی ایران در سازمان ملل متحد: ایالات متحده آمریکا از شورای امنیت سازمان ملل برای انتشار دروغ و اتهامات نادرست علیه جمهوری اسلامی ایران و برنامه هسته ای آن سوءاستفاده می کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/akhbarefori/653143" target="_blank">📅 02:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653142">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
دستگیری مزدور موساد در شهر ری
🔹
دادستان شهرستان ری: یکی از عناصر مرتبط با سرویس جاسوسی رژیم صهیونیستی (موساد) در جنوب شهرستان ری، شناسایی و بازداشت شد.
🔹
هم‌اکنون روند رسیدگی به پرونده وی در حال انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/akhbarefori/653142" target="_blank">📅 02:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653141">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQaCo8Cs-qqLIvzSPiPY1w8eEk9R6Ll6GNmCcwTZLUM7NstyjrmqaKzekTuqG093tk2XqHlDafC2JTs9-A87Jy6G2gKZCL6gCsWGLezARguZrzwZqpfg6HLrEPp5R0k_fdi-WMajWZwsVqNfxOuB8Dt7yZEciZ2fZh3S79Qyp9RWDXb28qgWm0RcVs-vuJ_xT7sYbJ0oazPrkhBqWKJnNA0H8MAhql1bPPqpxQ3TeV977khU2BDmi6xHm_UQcJqhYyGHwg2CXpBWMO2omKAOT8l_sG4k_Brc13J6ogxTrz3K2E-zTAt1LQo4ImwnM7biHn2vJ4Qp-3hf4jL2LRwtEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویب طرح پایان جنگ ایران در سنای آمریکا
🔹
سناتورهای آمریکایی بامداد سه‌شنبه طرح محدود کردن اختیارات جنگی رئیس جمهور این کشور علیه ایران را، بعد از ۷ بار رد شدن، تصویب کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/653141" target="_blank">📅 01:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653140">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKc9azQ3jRncEG1rFT-_T_yq9WyTqF4j1Ry75509hU3aJo3UdgN8BUXWncCadNNdLzkfJ3HaJEyrn1nISyILhn5X5l05cuUtpNoE5xaGs5HToIsOyPAjykvIetYsSrqn4QuYrpPpLMfv-BBH2KJG5pvOT7qY9nOr5nGltxLRAwo-iFUmZ5kTAz_1dCFxco4cumNsa9y5FAYulA2gp8rpYLX1Hv3HWf-Pv19ATyr3KFA7_t1_tAPSJmWtbtmE724OWL5cl5QwufDRHi7jIuYo_slLI53S-YXLXJ5KzHlWkOTDL1DNbB0q5tUK_c_Y6sbS1-tzUJOYArEuOKUr6IIBOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز از تصمیم ترامپ برای توقف حمایت نظامی آمریکا از اروپا خبر داد
🔹
ترامپ قصد دارد سهم توانمندی‌های نظامی خود را که برای کمک به متحدان اروپایی در زمان بحران‌های بزرگ در نظر گرفته شده، به شدت کاهش دهد.
🔹
پنتاگون تصمیم گرفته است تعهدات خود را در این زمینه به طور قابل توجهی کم کند و انتظار می‌رود این تصمیم روز جمعه طی نشست مقامات ارشد دفاعی ناتو در بروکسل اعلام رسمی شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/653140" target="_blank">📅 01:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653139">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGkrLq4IgDMlQwdH2ZjbTEwTfG6la0K1vCDTZ_R_EI2GfJ-PjidyVxkixgzNitoqy4XnTOtGEYKy3J85gZuUgsuHN5DLwEtCMcWdtTpF110EoWMf8fepf-Uz6GP5tGpB8ZWbBjDiQHFcb7QtqTayjVBkHZD43kXUYCGx3aWlRFj4y3L0jk78-Sxv85ZFalp4-5clstZtsZrKSr2pjUWi-i8Su7tBCSiJKuml1uuaK-2qReqbXIlrnvBtddvRByGJXI3UnVMEk5kgWJ-1VErATrSHLDyapfuHfajdAg188FxfPBXUvFnb9LnsLzGKbXexcvpIsxQ0_XE8WVjoVe_YXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: تقلای شرم‌آور آمریکا برای توجیه جنایت میناب، ماهیت این جنایت را مخفی نمی‌کند
🔹
سخنگوی وزارت امور خارجه، در واکنش به ادعای فرماندهی مرکزی ایالات متحده آمریکا درباره دلیل هدف قرار دادن مدرسه شجره طیبه میناب و کشتار بیش از ۱۷۰ دانش‌آموز و معلم، نوشت:
🔹
ادعای فرماندهی مرکزی ایالات متحده آمریکا (سنتکام) مبنی بر اینکه مدرسه ابتدایی شجره طیبه میناب در محدوده یک مرکز موشکی بوده است، کاملاً بی‌اساس و انحرافی است. این تحریف آشکار، تلاشی واضح برای پنهان کردن ماهیت واقعی حملات موشکی ۲۸ فوریه است که موجب قتل عام بیش از ۱۷۰ دانش‌آموز و معلمانشان شد.
🔹
هدف قرار دادن یک مرکز آموزشی فعال در ساعات مدرسه، نقض فاحش حقوق بشردوستانه بین‌المللی و مصداق بارز جنایت جنگی به شمار می‌رود.
🔹
ماهیت غیرنظامی این مکان را نمی‌توان با توجیهات فنی و بازی با کلمات پوشاند. فرماندهان نظامی و مقامات آمریکایی که مسئول صدور دستور و اجرای این حمله فاجعه‌بار بوده‌اند، باید طبق قوانین بین‌المللی کاملاً پاسخگو و محاکمه شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653139" target="_blank">📅 00:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653138">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzNKcjve1o5a6vksl3122v-SU_S0fJeSjNyCl_eyWP7u5f6dC0Kh7lRzioyyvQkTaPtOv9Nf-X9lHCYSjO5pXC8_LfCFulDAirUXjwIaCs_Qc3cje0tWfax8-4ckZLDeAsC9CRdDQtLM5CWsMj9h28vK1VjZTRFMyLncw2BaJt1OYPhYKhiw5Il7fD23DJ_x1DeKC0iRzCVtkBU8_flewUDfMm9EYyjeO-P8RwvujTvSmrZmkAy15PrhFzwzKcwXp1CsHTNKxdP_R-_2t3C_qO27YYPFYaFX7hePqVxk8__YE8WQpFuah28gli6Kxn1RkrWx6EF7WcVs2aGEB7t2pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: مطمئن باشید بازگشت به میدان جنگ با شگفتی‌های زیادی همراه خواهد بود
🔹
ماه‌ها پس از آغاز جنگ علیه ایران، کنگره آمریکا به نابودی ده‌ها فروند هواپیما به ارزش میلیاردها دلار اذعان کرد.
🔹
اکنون به‌طور رسمی تأیید شده است که نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه F-۳۵ را سرنگون کردند.
🔹
با درس‌هایی که آموخته‌ایم و دانشی که به دست آورده‌ایم، مطمئن باشید بازگشت به میدان جنگ با شگفتی‌های بسیار بیشتری همراه خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/akhbarefori/653138" target="_blank">📅 00:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653137">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df5fd590b.mp4?token=bAxdDFHC4eMKE9-tCvfpb_c7rYaODmBXYpfVs2pysbHZm-26p2hfQDIvrd-Wl_7uiTZYdtt3l7GlHA5-2i1e5HBLaUCB2Evwc7OSkUrLu6zJQHD1R9DtGeDp4QKxeo-F8pwXJi9IIt88D6fkn9iu2bGuv5VrLALKGKFozJ7Hdm-rtXyjDdXEBPttvyLCtEzBu25NUf3C9IL0YzQOMZVkXJNm9apgGQztL0ZC3TeXMX6e9DRyYLLo1TFqxjoO9yex00ze0_td-TrGYE_IhqaHmf-cKCF5QaXdPBB_1HgdzpweExlBkee3I_lRkmiOk6Cwhg_qq08SLprjJa9oPSFqwD9MnfMQlO8DB7X6AgWJgyopOCKwCeSn35ePI8ayPk5JnASMaYVou3YIpiGQMKyLctVGDJL8b8Wf4xSmTo8Cg6anlu5EBXZvgnsu5mR3Il22Amt-9H8azvICkt_xaNdfNcyT6froYIxTEyr-rKP0lqemGrgInxeakruX6Ez6YyBOLRn4YF81CM5ztG5yd3lE1Qv6fqUU8giEM_P312W1KuAkbhrlwMMqFZ0hEzGpZwwbKTieZXm6NCq8ZUGfwYt9fENfY3GJ6LOhiQyMHZYWBPyOOGQJah8Y1wDitLiBtNUFhz2WKsGj4p7GQhssyAtG_LRsXtcb4Y5cEkL6ikvov1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df5fd590b.mp4?token=bAxdDFHC4eMKE9-tCvfpb_c7rYaODmBXYpfVs2pysbHZm-26p2hfQDIvrd-Wl_7uiTZYdtt3l7GlHA5-2i1e5HBLaUCB2Evwc7OSkUrLu6zJQHD1R9DtGeDp4QKxeo-F8pwXJi9IIt88D6fkn9iu2bGuv5VrLALKGKFozJ7Hdm-rtXyjDdXEBPttvyLCtEzBu25NUf3C9IL0YzQOMZVkXJNm9apgGQztL0ZC3TeXMX6e9DRyYLLo1TFqxjoO9yex00ze0_td-TrGYE_IhqaHmf-cKCF5QaXdPBB_1HgdzpweExlBkee3I_lRkmiOk6Cwhg_qq08SLprjJa9oPSFqwD9MnfMQlO8DB7X6AgWJgyopOCKwCeSn35ePI8ayPk5JnASMaYVou3YIpiGQMKyLctVGDJL8b8Wf4xSmTo8Cg6anlu5EBXZvgnsu5mR3Il22Amt-9H8azvICkt_xaNdfNcyT6froYIxTEyr-rKP0lqemGrgInxeakruX6Ez6YyBOLRn4YF81CM5ztG5yd3lE1Qv6fqUU8giEM_P312W1KuAkbhrlwMMqFZ0hEzGpZwwbKTieZXm6NCq8ZUGfwYt9fENfY3GJ6LOhiQyMHZYWBPyOOGQJah8Y1wDitLiBtNUFhz2WKsGj4p7GQhssyAtG_LRsXtcb4Y5cEkL6ikvov1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده مجلس: تثبیت تنگه هرمز به همت شهید تنگسیری و رزمندگان عزیز ما، با تدابیر مقام معظم رهبری، در جنگ اتفاق افتاده
🔹
روح‌الله متفکرآزاد، عضو هیات‌ رئیسه مجلس: تنگه هرمز آب‌های استراتژیک ملی ماست. به همت شهید تنگسیری و رزمندگان عزیز ما، با تدابیر مقام معظم رهبری، تثبیت این تنگه در جنگ اتفاق افتاده.
🔹
ما تنگه را بسته نگه نخواهیم داشت. موضوع، موضوع حکمرانی ماست که باید تثبیت بشود.
🔹
هرکجا نیاز شد برویم به سمت سیاست‌گذاری اجرایی آن هم شعام، هم مجلس با تمام قوا انجام خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/akhbarefori/653137" target="_blank">📅 00:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653136">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
۱۰ شهید در تجاوز صهیونیست‌ها به شهر صور لبنان
🔹
وزارت بهداشت لبنان: در حمله هوایی رژیم صهیونیستی به دیر قانون النهر در شهرستان صور در جنوب لبنان بر اساس امار اولیه و غیرنهایی، دست کم ۱۰ نفر از جمله سه کودک و سه زن شهید و سه نفر از جمله یک کودک نیز زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/653136" target="_blank">📅 00:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653135">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGsX-udoAuOG5IiDVhxgU69OM68b7vEKhoPwMZZu0YLff2kZkhEL9CWFgWEGCBrQiTNCurm7QKivnSDlk4k14p3G84xtbMP1bIeo4yLkCfxPJP9kUU-NWMLT0Z1_xu8Gr1TRMI_NnKPVE4iBpMcQdRiqqwpA9NooXg-D-13bVMyCZ1SQwde1uSuptIc4IJSrc8DRt8usRpAp0XpmDmbEyHfDy9ly06anK1-Hv2rRw545fjYmodYjtAPEC6MYfb3Yg5SkqiC1TxYjem1pYO3Jzuy1EJPFlpWdkuemtW4orZZ-MjZqEDLmdnhboxAWFYDDCZjrP6rtXCZI4FWvkECrgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرسنال بعد از ۲۲ سال قهرمان لیگ برتر انگلیس شد
بیشتر بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3216390</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/akhbarefori/653135" target="_blank">📅 00:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653134">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccca31dbb4.mp4?token=vlRy4XOPOuZAtsGU3Kvdja12gz1l7-HOBMnNmN_nnZ9lfy1UEyaoXQ8hDmTQ4ek-IvCqMWQPrmsbLA3uw7a1KE2doMnZeNjkiGh8D1PWUp6lAPtXVt21wY52so3yRv1gGf3zKxU0pwfB8Crz242LJmzFSvhgoYzQ9X740TZeSVd1GCMItglA-dV-2emj14zYugycbI3JXmTQdcvtxYZgSGuWvcUna6qOzFby8Rx7CfzD0jjFdfQyBoSXLu8_-HEfz7u-WyyJelljTf7cX4r8izWwxQV8PsNpgEkJ1OKAN7Wn3BdXuCRu1GJelSSygn6Fbd0NpcrIE2cCtlhs7UjToA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccca31dbb4.mp4?token=vlRy4XOPOuZAtsGU3Kvdja12gz1l7-HOBMnNmN_nnZ9lfy1UEyaoXQ8hDmTQ4ek-IvCqMWQPrmsbLA3uw7a1KE2doMnZeNjkiGh8D1PWUp6lAPtXVt21wY52so3yRv1gGf3zKxU0pwfB8Crz242LJmzFSvhgoYzQ9X740TZeSVd1GCMItglA-dV-2emj14zYugycbI3JXmTQdcvtxYZgSGuWvcUna6qOzFby8Rx7CfzD0jjFdfQyBoSXLu8_-HEfz7u-WyyJelljTf7cX4r8izWwxQV8PsNpgEkJ1OKAN7Wn3BdXuCRu1GJelSSygn6Fbd0NpcrIE2cCtlhs7UjToA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسویه‌حساب پادشاه جوان ایرانی با امپراتوری عثمانی !
برای ادامه ویدئو
👇
https://youtu.be/rCuQWD1D_es?si=Cxi0mh-CjPIi0Nmk
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/akhbarefori/653134" target="_blank">📅 00:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653133">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
از کنار داغ‌ترین خبرها و گزارش‌های امروز ساده عبور نکنید
🔹
گزارش لحظه به لحظه از تحولات روابط ایران و آمریکا | شبکه ۱۲ اسرائیل: ترامپ تصمیم گرفته حمله کند!
👇
khabarfoori.com/fa/tiny/news-3216088
🔹
حقه کثیف ترامپ در اعلام تعلیق حمله به ایران | این عدد همه چیز را لو می دهد!
👇
khabarfoori.com/fa/tiny/news-3216090
🔹
نقشه پنهان اعراب برای ایران | پیشنهاد محرمانه عرب‌ها به چین | یک اتفاق غیرمنتظره در دو سه روز آتی!
👇
khabarfoori.com/fa/tiny/news-3216309
🔹
خبر محرمانه یک اسرائیلی برای حمله به تاسیسات هسته ای ایران | جنجال لو رفتن یک نقشه شوم | ماجرای حمله به اصفهان برای استخراج اورانیوم چیست؟
👇
khabarfoori.com/fa/tiny/news-3216091
🔹
جنجال رقص منشوری در خاکسپاری | هیاهوی دختر خواننده مشهور در مراسم عزاداری + فیلم
👇
khabarfoori.com/fa/tiny/news-3216016
🔻
ویدئوهای جذاب را در آپارات خبرفوری ببینید
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/akhbarefori/653133" target="_blank">📅 23:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653132">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bfcf97015.mp4?token=rfiGRb7rG63uXFT1QjFr6rZ72OFoHNuQzLM7g81rnX1AwNb7ulL1qRizg-Pp7qdFn2tooGmmW3v8ZvVZUKngRMz2iFmvR68QiVw3dzfPfdfBtWnYfoRktcCOdApJoyy3IxOGQ-kHnKIlhyg3WXXKW1X4AAzRRWAu_l_4MNSSv56FCcW4i6dVS2cSk9W2KQkCLyAiBuCMawvaV7WKC4XwQ55HgDbnSfM7azpX5O5S_tAJFYeC3aKzPb0jz31C9lWUqtCIdRPDc3ZbdwHwpBrcs6utRGMngRqTH7YCdGgBNinZKor-pEaevRuHuKqZs0OdI_r1TOEQJNCvX1Scc2Kmcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bfcf97015.mp4?token=rfiGRb7rG63uXFT1QjFr6rZ72OFoHNuQzLM7g81rnX1AwNb7ulL1qRizg-Pp7qdFn2tooGmmW3v8ZvVZUKngRMz2iFmvR68QiVw3dzfPfdfBtWnYfoRktcCOdApJoyy3IxOGQ-kHnKIlhyg3WXXKW1X4AAzRRWAu_l_4MNSSv56FCcW4i6dVS2cSk9W2KQkCLyAiBuCMawvaV7WKC4XwQ55HgDbnSfM7azpX5O5S_tAJFYeC3aKzPb0jz31C9lWUqtCIdRPDc3ZbdwHwpBrcs6utRGMngRqTH7YCdGgBNinZKor-pEaevRuHuKqZs0OdI_r1TOEQJNCvX1Scc2Kmcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: وزیر امور خارجه ترکیه حد و حدود خود را بشناسد و بداند اجازه ندارد درباره جمهوری اسلامی ایران از کلمه باید استفاده کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/akhbarefori/653132" target="_blank">📅 23:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653131">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
وزیر راه و شهرسازی از ارائه پیشنهاد تعیین سقف افزایش اجاره‌بها در هر استان و تمدید خودکار قرارداد‌ها به سران قوا خبر داد
🔹
رئیس دانشگاه تهران: ۷۰ سهمیه جذب هیأت علمی برای رشته‌های پیشران علم و فناوری مانند حوزه‌های هوش مصنوعی، کوانتوم و فوتونیک اختصاص یافت.
🔹
فرمانده انتظامی استان هرمزگان: هزار و ۸۲۰ تن برنج پاکستانی که در انبار اطراف اسکله شهید رجایی بندرعباس احتکار شده بود شناسایی شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/akhbarefori/653131" target="_blank">📅 23:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653130">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
معاون توسعه روستایی رئیس‌جمهور: اینترنت به وضعیت گذشته بازخواهد گشت، زیرا دستور رئیس‌جمهور است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/akhbarefori/653130" target="_blank">📅 23:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653129">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ow7M4TVahOYGxpn8nuaa0yo3FmOYQJGklYUul66hymhXh4TKko8ii9p20I5Xjxb5SYSseJjdhHqKNaWetiVAX-uDl25Qf2jJpY-38oVAPHD9Cn9_ziMqwYwQh7ENIE91UFS2si_jsH1xbH3bWDJ_WOAwfBH3YfVH7iqWFyegm1KaSBhqvC_Gp_w1ivmN8e16T03iIgF40nqF5n_uk8ixiz-wSRVMLz4a63kGqQ5FszvCS63lSzLrxDUItT4gfq8pdkxXT2S1HmLAO4VJoYkO1AzeSc-69m1wQ_kHvoKieiQhLpsJzegPjalwhDykRmUmULKtX0XJhAz-YwjWViMbwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون بازرسی قرارگاه خاتم الانبیا (ص): در آستانه تحول تاریخی بزرگی هستیم
🔹
سردار اسدی: با تاکید بر اینکه امروز در انتهای یک پیچ بسیار مهم تاریخی قرار داریم، گفت: آنچه از همه چیز واجب‌تر و لازم‌تر است، حفظ وحدت مسلمین است، زیرا دشمن تمام توان خود را به کار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/akhbarefori/653129" target="_blank">📅 23:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653128">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
انسولین در بازار کم است؟
محمد هاشمی، سخنگوی سازمان غذا و دارو در
#گفتگو
با خبرفوری:
🔹
تحریم‌های آمریکا با ایجاد محدودیت در حمل‌ونقل، تراکنش‌های بانکی و افزایش هزینه مبادلات، به‌طور غیرمستقیم بر واردات و قیمت دارو از جمله انسولین اثر گذاشته است.
🔹
افزایش قیمت انسولین‌های وارداتی بیشتر به دلیل حذف ارز ترجیحی برای اقلام دارای مشابه داخلی و نوسانات نرخ ارز است.
🔹
بخش زیادی از نیاز کشور به انسولین از طریق تولید داخلی و مطابق استانداردهای بین‌المللی تأمین می‌شود و سازمان غذا و دارو با پایش موجودی و تقویت زنجیره تأمین، تلاش می‌کند دسترسی بیماران به این دارو پایدار بماند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/akhbarefori/653128" target="_blank">📅 23:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653127">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/103f07f218.mp4?token=eXx7RS2PWTNC3rOE-YcC0YlGsGdg6c0yw9Sny7VXzHvT33DpvAZkOFiH-W6HS4PjNHSvk4nqJq0UJ_tUwrkm98N_f0oYxU5gexQz0T_gUesK5uKIjOeLKybOZtrVnztS8o94ZK33NYvNx5B7rhqwU4Hdp664l8e-DpfaB47ntSzCMrmE2iUCARC_-mUL4vHafXghULb-fHCKu38fX-H4uo8Vq5MoMKNpodrjPpR0BZqAXXvv50szD9cjbnUPnQaCVgS06It6rfb41dh9CjKkAcyi1ebJfIWn0RggJjTPP8uwzhTthF7So4b99uSsKZQVMd3xnpl0VNYDVBgC9fXo1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/103f07f218.mp4?token=eXx7RS2PWTNC3rOE-YcC0YlGsGdg6c0yw9Sny7VXzHvT33DpvAZkOFiH-W6HS4PjNHSvk4nqJq0UJ_tUwrkm98N_f0oYxU5gexQz0T_gUesK5uKIjOeLKybOZtrVnztS8o94ZK33NYvNx5B7rhqwU4Hdp664l8e-DpfaB47ntSzCMrmE2iUCARC_-mUL4vHafXghULb-fHCKu38fX-H4uo8Vq5MoMKNpodrjPpR0BZqAXXvv50szD9cjbnUPnQaCVgS06It6rfb41dh9CjKkAcyi1ebJfIWn0RggJjTPP8uwzhTthF7So4b99uSsKZQVMd3xnpl0VNYDVBgC9fXo1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر صمت: قیمت خودرو متناسب با افزایش قیمت ارز تغییر می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/akhbarefori/653127" target="_blank">📅 23:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653126">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e15dd1d8c.mp4?token=DcXwuacBC2PF2XpdMlvGgtCb9DTh2tWEhvgwP3g1yPa3AnX25nofUaiXB_98YqBQFtY4Xfr49ZFKM9C0oTLNDy9WAl1MA08a-IT8qPJG9H6w_ZoQgLgX3hIaC--8qKAJL2XIZX3jRaxh-6-MI-zCUbXrbuHChsJS52j5La1pc-uheUVHI117SUNJp988-T0Q-G7cag-oUMnBtR2lHy1el1XrLyIgMy8JKWBjfiN9Qb6kx27iaFBQ-nacPMZ2fzVC0wffFQo6QwLgfF2P_8klc_YxsvB9UBWFj43rpIS5VW8xBfuWJIbRSQGjeaVRpsbSgJtLW3x5_P_mPptyP0INrTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e15dd1d8c.mp4?token=DcXwuacBC2PF2XpdMlvGgtCb9DTh2tWEhvgwP3g1yPa3AnX25nofUaiXB_98YqBQFtY4Xfr49ZFKM9C0oTLNDy9WAl1MA08a-IT8qPJG9H6w_ZoQgLgX3hIaC--8qKAJL2XIZX3jRaxh-6-MI-zCUbXrbuHChsJS52j5La1pc-uheUVHI117SUNJp988-T0Q-G7cag-oUMnBtR2lHy1el1XrLyIgMy8JKWBjfiN9Qb6kx27iaFBQ-nacPMZ2fzVC0wffFQo6QwLgfF2P_8klc_YxsvB9UBWFj43rpIS5VW8xBfuWJIbRSQGjeaVRpsbSgJtLW3x5_P_mPptyP0INrTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: امیدوارم خبر سفر عراقچی به نیویورک برای مذاکره در خصوص تنگه هرمز دروغ باشد/ چرا ما در خصوص موضوع تنگه هرمز باید در خاک دشمن مذاکره کنیم؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/akhbarefori/653126" target="_blank">📅 23:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653125">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0090d76668.mp4?token=jrTA93hcUr41ypTw4gMrmzCenWXSf9d-iAVml4efxtD-pxbJu2yHuJhHZwC5oZIKpRfWF6iu0jdMWFwu0tIVw1dSStTK5QBbT5vWv6QDtPdTo5CrJPl137ebtIkj_K6Clqn_WmIwWJYq07cr5u2RXIsr816XgvAAKwDyZ-u_kb9cZMGgTyuO4OdLf8p21SnZ5VRg3m35Rcj3Mj-xaHh1joqsT8l5asZSaKxIyg0jVfaYNNHLv0VAGTSxrhMCvbNinX9yPkr15XrDL68S8C9NR9lwFgk_c-nxJ1cZHylgnwwyqGweOMJQfe4lV4RUn5j7nVnICfdKucUQkz9dn0TXBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0090d76668.mp4?token=jrTA93hcUr41ypTw4gMrmzCenWXSf9d-iAVml4efxtD-pxbJu2yHuJhHZwC5oZIKpRfWF6iu0jdMWFwu0tIVw1dSStTK5QBbT5vWv6QDtPdTo5CrJPl137ebtIkj_K6Clqn_WmIwWJYq07cr5u2RXIsr816XgvAAKwDyZ-u_kb9cZMGgTyuO4OdLf8p21SnZ5VRg3m35Rcj3Mj-xaHh1joqsT8l5asZSaKxIyg0jVfaYNNHLv0VAGTSxrhMCvbNinX9yPkr15XrDL68S8C9NR9lwFgk_c-nxJ1cZHylgnwwyqGweOMJQfe4lV4RUn5j7nVnICfdKucUQkz9dn0TXBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده کنکره آمریکا فرمانده سنتکام را سوال‌پیچ کرد
🔹
ست مولتن: دریاسالار کوپر، شما در مورد ایران مدام از عبارت «به‌شدت تضعیف‌شده» استفاده می‌کنید؛ تابستان گذشته به ما گفته شد که برنامه تسلیحات هسته‌ای ایران «نابود و محو» شده است. آیا می‌توانید تفاوت میان «نابودشده» و «به شدت تضعیف‌شده» را شفاف‌سازی کنید؟
🔹
فرمانده سنتکام: جناب نماینده، هرچیزی که به برنامه هسته‌ای مربوط شود...
🔹
ست مولتن: نه، نه! من از شما نمی‌خواهم درباره برنامه هسته‌ای ایران صحبت کنید. من از شما می‌خواهم درباره زبان انگلیسی صحبت کنید! تفاوت میان «نابودشده» و «به‌شدت تضعیف‌شده» چیست؟ آیا این دو یکی هستند؟
🔹
ست مولتن: ۵ ماه پیش ترامپ در استراتژی امنیت ملی خود دقیقاً از همین عبارت «به‌شدت تضعیف‌شده» استفاده کرده بود. اگر این ادعا ۵ ماه پیش صحت داشت، پس چرا ما این جنگ را شروع کردیم؟ آیا او آن زمان به ما دروغ می‌گفت؟
🔹
فرمانده سنتکام هیچ پاسخی نداشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/653125" target="_blank">📅 23:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653124">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
اسرائیل همه کشتی‌های ناوگان جهانی صمود را توقیف کرد
🔹
ناوگان جهانی صمود: همه کشتی‌های شرکت‌کننده در این ناوگان که به سمت نوار غزه در حرکت بودند، از سوی نیروی دریایی رژیم صهیونیستی توقیف شده‌اند.
🔹
بنابر گزارش‌‌های عبری، نیروهای رژیم اشغالگر تاکنون ۴۱ قایق و کشتی از میان ده‌ها شناور شرکت‌کننده در این ناوگان را تصرف کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/akhbarefori/653124" target="_blank">📅 23:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653123">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38bbc55be7.mp4?token=FStT2mzY3VLJo_S3wkvzZqXXpDYrjV8dIA1wZOwcNpFtjQSJkycePmat7pid9mrb04hwpm0Kf_EG-2pxndAB3nXRO9cnn3kFyv_hZ0HdbN5qoCK2YY_y5e5MyYBiNtT9DtSs2ZLlm4meb2Dj4BmD9t_yThsTDdGMri4Z-iq_ER1FWuR6NfOOeAXjabif3pwT-FaD8cc8Mu4esnzVHCngH9pre46qVrxsOZYuxnWxrjwjRit6fAv4oS_ekkE3zpVExDNYap898ZdjU_TYDKXoBSOyCdCOw-0mP1bQKo2jO3uWpm5FA3p8UerigkRBxtl5L80R_IHcaCyaOcBQ-iRinA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38bbc55be7.mp4?token=FStT2mzY3VLJo_S3wkvzZqXXpDYrjV8dIA1wZOwcNpFtjQSJkycePmat7pid9mrb04hwpm0Kf_EG-2pxndAB3nXRO9cnn3kFyv_hZ0HdbN5qoCK2YY_y5e5MyYBiNtT9DtSs2ZLlm4meb2Dj4BmD9t_yThsTDdGMri4Z-iq_ER1FWuR6NfOOeAXjabif3pwT-FaD8cc8Mu4esnzVHCngH9pre46qVrxsOZYuxnWxrjwjRit6fAv4oS_ekkE3zpVExDNYap898ZdjU_TYDKXoBSOyCdCOw-0mP1bQKo2jO3uWpm5FA3p8UerigkRBxtl5L80R_IHcaCyaOcBQ-iRinA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: ایران باید پاسخ نظامی به نمایش محاصره دریایی بدهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/akhbarefori/653123" target="_blank">📅 23:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653113">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5eWTaSsLdnjzdoYtWiBPj-zMAzgBNljYJ7Zg42bl5Nz6Mknj2m1gA83VCSClNQ_hvOP86hpmaLcS2lh_TwCMivQfvLd_S2uZ1mo7jILvsGKkqp_shAy7wOyMQ2UtHuMgn7S9VyqgorLhDalXCGDRmDm4EE23Wmrzze0jwzW_yQTv7cciaKGgtRH7wH9_szs8WVW8b6CJALCkSst7vktThmpWTK3tnI6sMvEBkvSRxnFzLSudwTRJ_7zqrt04LjclvY6yMgC7_lPb1j_1t8uj0POwAEuSEhJkiLVMAKYc7ks2kb04os6zFBanEy3N0dQTHAX0YyWB5xi5FGFmL2OFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/miqeUcqrekvBB8VVln0AjH28cwP5qGYL6o-EbXT1WjE27xdlZ79fK-aF6qlK7RDmpq3F4-iywpOwwX8H4rKmflRX1b4b8cvjSS6BpxveCM1B0DdPsl8O1SlH_LgDoCh_yqz5JL1z2zvAR53x75h_vZ6OXTUMt9SiIqyS1tG3LrQ9lZRxPNN4fzMrALGOMfYlQkz0NKT7wtk9C_1k7Xcr0_bjg0OQz_pmLSQvYy9Hy_-iWimhi4rxL3utKwEDUY0ylbA545a8DBU3DA7Rwv1pRUScdUAMjMwD4ihjPw7l0rIEz5_SiPLdKcQNd52UawFuukoAdn4TpJMoqOKJD8MWtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcWgiroCgcZAU6QlpA6Akm304E5aR03evOtFIl9xb6blfnkEHScLF48IZ-OVaRnijRZjILzFW4NmzXt-9EZiEjsSuRAG0M7r4q8yJakCuMtWaeDgH85lc341KmhSL7aoy_KV21hM1OGthLe5lkeClIPsoQ1S90iQ73M3FlXlBfLVmOJ_euKOU9teZehMVgO80oyN3VuDMnNB8QsYFcQaWZFwBM1GHeJWGZKuryvbtQaqfNzNgemq02fOnS1MBcYZ-9BnQ28LnWws4Vsf0f8YFdN4MjUMcwhxKpfTxrvYRqXMXUEno7dHto_GLLTEhmWUtqxU3BVCBdtON8fhXs57oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0xEvXG3tTkgjtqPBEcJqJjBKQdu4eXPhR3BIPtmv_TSrblAECBOK5FABE6__F5-rTFLUkgVYYubvbwnpkEJlFGXn6HZ0_t2W72PaU6WErPkkrxJxrA9lj6SjkdWsJCscecKQj0A5HZq-8Q0gOxQIE5lvSAsBbz_cWDaPTuDzyzuNZTnNYz18XX5vioGxcAXnSU2Yj85sjiU4VJUN8Yd7KNQBE1OvlACFYIzCJiQJUhyj5pTZGX4L0oxD832Oj_CW1QgAL5RtP6Jn-1gKFI69c24k--F_Ig8Dm5wcU-rI-YHPYthCgGbWY7kJ3Mm2NwNOuB182e9gjoDxKO2h7n-KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehIhTgoJla8nQpFyNDQmsHtUgSNdgxFdXfs6ihKn1d_s370liGEiGIWmlGgQSXb4dv6uPeKNUjDXLnjmxp27icmJC4exTCbdJsBMzVN5ImiNLGJsxQSuV1zG8usl1PzJIaEMKOWsy9y9ZeAvXLVNNl4u_GJ5VJZE3_qIFLeS3rKi9rtW24Qc31gAff7jFJ5a6PAL-YF_VHHIkR792-_xmeCcND7dU4q_NLe-X1Qq_x1_s1fRmrNmR_FsWl-O3-9didrxQLK4Z64PiteURG1vKyxfH67Amu-xd8OS0XVjcpe5HenGQ260sF3eZF_qvqhaeGF1hnhm6dyw1X5KnWkvjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XTJf6qJglgwEwURbroB2fyIX7d9z5oKhb1TA7jT9Q4zUsDZRZxBr4zA7TVTtRAQpY36DM0qTqBWE0qU8QQJgLfhuLeLIOaLnjG0xzJpZbKdHtH0_rQUfgcgyxErAcRayFu5IAd_OMOrPRzairbJ03cxsukIT0jDrJyxuYOAbr-cDQ7aA3-JuN-YjyiyP2cRYP3RitEsn6Sg3Cb-EkihbEa4PKzWo3u80J73pOdYGPFO1Xt8KFwwu02nG3gG3Zun6dL3RjhRgx19yIm4emlGF7s-8UshDMsb0MA-XCeJaFfgC3-_OM1XhOXZp5mNEGN4pEiOephNNCCGBe9dVrjQasg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6MWQeWEQOsW9pBu2MhF-VWZa3Iw1WLgswHmtPAUHRH-OwRoc3ZBpFc2DeMDRIyOZk30LCmpIoLMDJnhyMowlS3jWpeUNYsV-75Oj4bxW8NOAOBIwLnf2OnS_gCIULnVA-RlryZ_EtTq6vu7Cp1yaAtvV391qSsnXjNlDE5rDI2z41P5BgoJNKQWm9ER3Lg8L3LJ0Orm4VArHWjU1099YPoIjEzG24HnaRT3qpH3qtf7zKUCF58rl2d4urOuPuLyrGp0sU8Sa8tmFLTmFiNnY3jCmGU1JeCCA8B1JFheddS_O2KLwu54SMtfTJKKgRyFzHowP4fgp35rFFIk5bjH8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzShiXPK83a0ZAvoEaocLzTWZfE19L8jhEqqAUtB0pdQ7rs0k2QDFNffnNtAKI7mBHMZGs6KCboO-HXVyw4pKNkvCpLhJyA3MSRUvRIWZANdOPpcMzK2B16APzvCvWFbV_Jvw4gDZrn1i7NWNoTbmjvEVmT7HdGNoBz8d45DD_Dzus3d_atUTJCHTKN1Di7b9r0vkXMCF4jxTEeuOR1GNOXhoZvjgvMJ7vbVNVxcFuxOqgWpdR47VnMVCzPDaYEVLpJtXRBcBb03c4FZcOdURVtGw5dgvM1lLarX9sRVxLqSbojDja_MSi6HCK_jrFoll8UDTTh6HixYu5zTFDWGDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgPpzCoV0sxR0J5GBtWG0JwukIKe3dyGYdHf7z-aKIoG81gvOPXSzGe34lmff1AiYeBQiHvdhqyWBnLLOvHXiAGTzm5UmbhaD5WIGbkh5bJzpS8Nv2ZHq2dvh4tlGuCRr6YPWEImvpvobOS9_Jv7OTerMDP5FJ65IHgkswjQyf_H0proXKlXaU83TMBaKLlJJQkePBLQ-R-s37LIbRB5nGjIHPZLZbzqDVWhcEInAMfC73iOQY8ythXIWWXF4PUN_u76QR7ZQBfW9zSLoxagjtiazaCPlsAjmUHIU67tb05KJAWG9OfKvcP85sE-n6BYbyr5-zDph3ZUSs4ky_zX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XWMewIL-z0lbs9dgsPkvvGIiR36Nn7s-Ww8j4sFnB-XI3EzmEwz8v4tYt_j6w2hGi91_U_M2CAgoY5BudyhU8E7Wow4ElWGSEEu9FcFC31-wRBQNtamexShCcVbwWhgg-qiiLxL-H_hS1WLu_55iKm86Lnr39pM1VGJyPUCqzTQHvry5WlPoVo8PV78o4zuJZh-6cYxUDIcUMzPXAQsOOJhISr_AhDNtzmpCz2CTLkVCqjDityAIDwC1txxG_f2k9Nxhk6RVTUjUKiBchU9A1UNUe-AKWGt-6HJBj5mFF1IEq65ej6js4_Ln0czGZDIymMIWzQGaSv4m-q7ocSwTaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت برکتِ همدلی
💫
هر روز، به پشتوانه
#همدلی
و همراهی شما مردم عزیز،
#هیات_قرار
با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی میان خانواده‌های حائز صلاحیت، گامی در مسیر حمایت از خانواده‌های ایرانی برمی‌دارد.
ادامه این مسیر خیر، حاصل اعتماد و حضور ارزشمند شماست
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/653113" target="_blank">📅 23:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653112">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41f0e41066.mp4?token=FPmEWsJTUEE7IhpenJXX78u-d-WGzqy6mY9UeySB964KoMLK8rmAo23FifUXdGGu2pvdwfLpuPYv6e5HDBmbau2ovX5u4iWG1mqsWvHYNd2qdhRlllzRI1-pLjrr2PsafTwfUbdd0roeCT6ef23466Xg0AbE1NvsZv_Iog0so8E9P97-RAkq6d6pXfoTDILWXPC-tei-0JKTtP5TOe7wxCwtRV-vP6s03dNTycuVVBFzW6desXUXc96ChfjbBpmgMkYqtlTEhAVJokjxbrn9RLOEU5kNH4OQV9nuKPiWBp4QHp-g2VI-63h716QzBA1pk5YY-VdItPT-kQqCGusGLHFT_dvnWkHyqntPvnUhNRUp3jEvsY1yGFpl4RBJ7bIlWSmgLNvXWyJnXiMEBS95-Tih-Wb1DygOIO__n5pFbzZya6-xcRCQU__Au6SjnBlcTvZ4P-2KyPXxy4vw2gQz0G9jyE6Ld5nz-000iXEy4ziZob4cVxObQseY736KYBEfMZPfOJfBMfX9BPRUP1QJ59fVp5Of3M5CYxNmAq0rziaj9nVPM6iPJB87cSgbPRTOQX7ccKR1ApsczWI3R9NOq9-omb-dGMsxBlLFpDkg7Yqg0qV4xpR0Mx1Ta4s2v-peBPrpxm249RpJiACY5xKe4kuGJwmdnCiddkZo-9s4IpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41f0e41066.mp4?token=FPmEWsJTUEE7IhpenJXX78u-d-WGzqy6mY9UeySB964KoMLK8rmAo23FifUXdGGu2pvdwfLpuPYv6e5HDBmbau2ovX5u4iWG1mqsWvHYNd2qdhRlllzRI1-pLjrr2PsafTwfUbdd0roeCT6ef23466Xg0AbE1NvsZv_Iog0so8E9P97-RAkq6d6pXfoTDILWXPC-tei-0JKTtP5TOe7wxCwtRV-vP6s03dNTycuVVBFzW6desXUXc96ChfjbBpmgMkYqtlTEhAVJokjxbrn9RLOEU5kNH4OQV9nuKPiWBp4QHp-g2VI-63h716QzBA1pk5YY-VdItPT-kQqCGusGLHFT_dvnWkHyqntPvnUhNRUp3jEvsY1yGFpl4RBJ7bIlWSmgLNvXWyJnXiMEBS95-Tih-Wb1DygOIO__n5pFbzZya6-xcRCQU__Au6SjnBlcTvZ4P-2KyPXxy4vw2gQz0G9jyE6Ld5nz-000iXEy4ziZob4cVxObQseY736KYBEfMZPfOJfBMfX9BPRUP1QJ59fVp5Of3M5CYxNmAq0rziaj9nVPM6iPJB87cSgbPRTOQX7ccKR1ApsczWI3R9NOq9-omb-dGMsxBlLFpDkg7Yqg0qV4xpR0Mx1Ta4s2v-peBPrpxm249RpJiACY5xKe4kuGJwmdnCiddkZo-9s4IpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حزب‌الله پرچم رژیم صهیونیستی را به زیر کشید
🔹
حزب‌الله ویدیویی از پایین کشیدن پرچم رژیم صهیونیستی از مقر ارتش در شهرکی واقع در جنوب لبنان منتشر کرد.
🔹
حزب‌الله در این ویدیو که متعلق به دو روز پیش یعنی یکشنبه گذشته است، ابتدا تصاویری از حملات متعدد خود به مقر تیپ ۲۲۶ ارتش رژیم صهیونیستی در شهرک البیاضه را به نمایش گذاشت.
🔹
بر اساس این ویدیو، پس از حملات متعدد حزب‌الله که غالبا با کوادکوپترهای انفجاری انجام می‌شود، نظامیان صهیونیست ناگزیر به ترک و تخلیه مقر خود در البیاضه شدند اما پرچم این رژیم را در این مقر باقی گذشته بودند.
🔹
در انتهای این ویدیو، کوادکوپتر انفجاری مقاومت با اصابت به میله، موجب پایین افتادن پرچم رژیم صهیونیستی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/akhbarefori/653112" target="_blank">📅 23:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653111">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بحران پشت مشهد و تهران؛ آب شرب مسئله شد
عیسی بزرگ‌زاده، سخنگوی صنعت آب در
#گفتگو
با خبرفوری:
🔹
با وجود بهبود وضعیت بارندگی نسبت به سال گذشته، هنوز یک‌سوم کشور با کم‌ بارشی و تنش در تأمین آب شرب مواجه است. استان‌های تهران و البرز و به‌ویژه شهر مشهد در صدر مناطق دارای تنش آبی قرار دارند.
🔹
در حالی که میانگین پرشدگی سدهای کشور حدود ۶۶ درصد است، این رقم برای سدهای تهران تنها حدود ۲۳ درصد و برای سد دوستی حدود ۵ درصد است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/akhbarefori/653111" target="_blank">📅 23:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653110">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW-YwWO5txR7TtTC71IHdreS1-9z7hHucfgWswJ4SP1ILzwr7cf1xvZGaO43DQ3U_Ar7wGS7ennFrA-bZ4ttyQDfjx6rEhpD6JveUQ-8cTeMJnhSbPSeC7Vq-kausp14P8a09mVqh7RzEjbmoGgbXH0tLsD3kNXVdzYm2YC2DZlfj7QVLnBDSQ-fV5bvk7iObV_16rffQ8yWxs_VknU0xXiNUiPE2gJv1m5XWNjKCdSh_JoDG-RjAj_yi5n7_lhS5g52XVLjUdAGJa-KKQ24sgzgZ3qlHzKltV23QV5eipBTKg3ebonGxIiDAQ_kcR6ooY7BMQ1qF8vwLDrWiF_f8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولیانوف منطق گراهام را زیر سوال برد
🔹
نماینده روسیه در سازمان‌های بین‌المللی مستقر در وین اتریش امروز به اظهارات سناتور جنگ‌طلب آمریکایی و حامی ترامپ لیندسی گراهام درباره ایران واکنش نشان داد.
🔹
گراهام در پاسخ به این سوال که درخواست شما حمله به زیرساخت‌های انرژی ایران است، گفته بود: بله خواستار آسیب زدن به این رژیم هستم. شاید اگر به اندازه کافی به آن‌ها آسیب بزنید، حاضر به توافق شوند.
🔹
میخائیل اولیانوف در واکنش به این اظهارات گفت «این آقا ذهنیت و طرز فکر بسیار خاصی دارد، اگر بخواهیم مودبانه بگوییم».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/akhbarefori/653110" target="_blank">📅 22:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653109">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
نیویورک‌تایمز: در صورت ازسرگیری جنگ، ایرانی‌ها تاکتیک‌های جدیدی به‌کار می‌گیرند
🔹
«ایرانی‌ها خود را برای ازسرگیری احتمالی حملات آماده کرده‌اند و سیگنال‌هایی فرستاده‌اند دال بر اینکه در صورت حملهٔ دوبارهٔ آمریکا، درگرفتن انتقام و تحمیل هزینه‌ای سنگین بر منافع آمریکا در همسایگی‌شان و اقتصاد جهانی تردیدی به خود راه نخواهند داد.
🔹
در هرگونه دور جدید از درگیری‌ها، ایران ممکن است روزانه ده‌ها یا صدها موشک شلیک کند تا «به‌طور مؤثر با دشمن مقابله کند و محاسبات طرف مقابل را تغییر دهد.»
🔹
کشورهای عرب حوزهٔ خلیج فارس باید خود را برای حملات شدیدتر به زیرساخت‌های انرژی‌شان آماده کنند.
🔹
هدف‌قراردادن میادین نفتی، پالایشگاه‌ها و بنادر کشورهای خلیج فارس، یکی از کارآمدترین راه‌های ایران برای آسیب رساندن به اقتصاد جهانی و اعمال فشار بر ترامپ است.
🔹
اگر آمریکا به زیرساخت‌های اقتصادی ایران حمله کند، ایران با بستن تردد در باب‌المندب به آن پاسخ خواهد داد. یک‌دهم تجارت جهانی از تنگهٔ باب‌المندب می‌گذرد.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/akhbarefori/653109" target="_blank">📅 22:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653108">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/akhbarefori/653108" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاه‌ویکم
رائفی‌پور:
🔹
0:03:30 مرگ جاهلیت به چه معناست؟
🔹
0:07:40 دعای پیامبر در مورد محبین حضرت علی (ع)
🔹
0:21:30 بازخواست چند برابری علما در آخرت نسبت به سایرین
🔹
0:34:00 مرگ مقدمه بیداری از خواب غفلت دنیا
🔹
0:41:10 حجت تمام کردن امام زمان برای تک به تک مسلمانان
🔹
0:51:20 عدم وجود عصبانیت در مؤمن واقعی
🔹
1:01:40 تفاوت هدایت عمومی و هدایت باطنی
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/akhbarefori/653108" target="_blank">📅 22:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653107">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3870ff30.mp4?token=VYuqzzOyFX1ZU0emicbMjCTt7tO-Z9Y2sIiCjw5l0ZKywpd59uptF3L5bDgLMOFlnDdkACy4fyS3NVJcnSWcxfVy8BGU0DPjnrF4bkvyYgRk9P2RK0-QN5c6bVE3Sm4cvJOadfEqYBQreWymbV7eRGsXGZ8zJvx4WhQYdXGUhwI40IRaibDVlLA-VVGfnz6Uh01qOzBVnp2AxW5qZCAskI6neHsCNbowwfiLMM1B79ArsXyGeh7JlKVFlBVCUBudWQB7fg7ghXtElQcXXeK0jfqhJTH_ryfITvQdMoi8RFHJv1rBKrTZ1PmXEzDGvI3fflMNNZaBexcWT_uFVFodwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3870ff30.mp4?token=VYuqzzOyFX1ZU0emicbMjCTt7tO-Z9Y2sIiCjw5l0ZKywpd59uptF3L5bDgLMOFlnDdkACy4fyS3NVJcnSWcxfVy8BGU0DPjnrF4bkvyYgRk9P2RK0-QN5c6bVE3Sm4cvJOadfEqYBQreWymbV7eRGsXGZ8zJvx4WhQYdXGUhwI40IRaibDVlLA-VVGfnz6Uh01qOzBVnp2AxW5qZCAskI6neHsCNbowwfiLMM1B79ArsXyGeh7JlKVFlBVCUBudWQB7fg7ghXtElQcXXeK0jfqhJTH_ryfITvQdMoi8RFHJv1rBKrTZ1PmXEzDGvI3fflMNNZaBexcWT_uFVFodwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدهی بیمه‌ها به داروخانه‌ها کی پرداخت می‌شود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/akhbarefori/653107" target="_blank">📅 22:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653106">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6579b980bf.mp4?token=CEEVGEyPuIEUqwDXZ0klXjulFWJ3qlJ8zBKFIVcM0hbAIde6SANCfc5TBWPiKUfHmE8Ye3AKZXOpWW-tEUbxNKI9eTTPE5tS2ORRhPLhEnFQ-yvFrJZxL4waCYm8ntZzz4VrfEYWM2pEY28IDyGKikJgmj8n-iZKYayUWn7xArZIHdntkZW2GjHIEh1rAdeXHigEGmEXBA41_Nai9vNliHWtZOHOa-NgaQQM3pGVe8M5QnQz2BRQo1OYYzbtgCBjzxQCOwUPg7zMLK0y5sxUI_fR5dxMbLAj8md9446lZzJ2y1lS25s8GoiCPF23lDskhWwbnrznSzEbCBezZ7NdPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6579b980bf.mp4?token=CEEVGEyPuIEUqwDXZ0klXjulFWJ3qlJ8zBKFIVcM0hbAIde6SANCfc5TBWPiKUfHmE8Ye3AKZXOpWW-tEUbxNKI9eTTPE5tS2ORRhPLhEnFQ-yvFrJZxL4waCYm8ntZzz4VrfEYWM2pEY28IDyGKikJgmj8n-iZKYayUWn7xArZIHdntkZW2GjHIEh1rAdeXHigEGmEXBA41_Nai9vNliHWtZOHOa-NgaQQM3pGVe8M5QnQz2BRQo1OYYzbtgCBjzxQCOwUPg7zMLK0y5sxUI_fR5dxMbLAj8md9446lZzJ2y1lS25s8GoiCPF23lDskhWwbnrznSzEbCBezZ7NdPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک سیگنال مهم اقتصادی برای تصمیمات ترامپ درباره ایران
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/akhbarefori/653106" target="_blank">📅 22:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653105">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6c4c745d.mp4?token=gNj0teAt0dn--R9rDAfgbz6Z1Lee_HbgG15IBkBX3oKtsa4o0uo8jKVXuGRlpDLpvXhauVmToPVaDcFINMSqVPqTnwOTugZHsmZuDnXNarndsz3amyz0-89qVdEUofozJTd822TXL7cC-_uaPtjryyeiK2t7janjJrKZu4XHLjlXhXCW7YoMpyi-NMudmLWHHFEN97fBNfekzKquWpaqJCqI1GCSdZgsQU1KA8fetjh58u2h41PxiEy5w1ZMJb5qZGlrXHoqDWMcEAwm0LWSCj1iQs_yivwBy6R02-yKTwLXqT559kBWUTve1N01rXnIhD74CNP5NwTRuz1irHctbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6c4c745d.mp4?token=gNj0teAt0dn--R9rDAfgbz6Z1Lee_HbgG15IBkBX3oKtsa4o0uo8jKVXuGRlpDLpvXhauVmToPVaDcFINMSqVPqTnwOTugZHsmZuDnXNarndsz3amyz0-89qVdEUofozJTd822TXL7cC-_uaPtjryyeiK2t7janjJrKZu4XHLjlXhXCW7YoMpyi-NMudmLWHHFEN97fBNfekzKquWpaqJCqI1GCSdZgsQU1KA8fetjh58u2h41PxiEy5w1ZMJb5qZGlrXHoqDWMcEAwm0LWSCj1iQs_yivwBy6R02-yKTwLXqT559kBWUTve1N01rXnIhD74CNP5NwTRuz1irHctbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توجیه بی‌شرمانه جنایات آمریکا و اسرائیل توسط ونس : طبيعیه که غیرنظامیان در حملات نظامی آسیب ببیند
🔹
معاون اول ترامپ: هر زمان که حملات پهپادی یا موشکی به کسی، به ویژه جمعیت غیرنظامی، آسیب می‌رساند، این چیزی نیست که ما اصلاً دوست داشته باشیم ببینیم و این یکی از چیزهایی است که گاهی اوقات اتفاق می‌افتد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/akhbarefori/653105" target="_blank">📅 22:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653104">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEzpbcUfOdXgthYhXLvR0GiEN42QL67LTCp4gIAlYVlAFc4sbCoVoWm9IVtnH6HWyZ9jhGT4Zr2C8rTJwa0ipCD57feFzHgQ3rBMK4HiogDQzxuqWu0xKXilQfgTaX59sHzsg6w6_8s1uCk1bGL8oH7cIvU9FxAzjVZQF2QEdqDf-aY7g6GSSkiw9gspnEnDEABXvFrMRE1hwT6o2DokYwmgaldfZM9cadtJi0tsCZdXFAChEnP3s_Ng46Ks2OisHNi6Dtj3AGdhZM4eNA-EDDw9IW7jQVoX3NL3y0y7j8s8Q4IjWnY6gcciPKfbLcyZ2jn5rE8-lO14rfoZg2mzOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیروزی غافلگیرکننده ایران در «جنگ وایب»
مجله فارن پالسی:
🔹
ایران در جنگ جستجوی اینترنتی (جنگ وایب) برنده شده است. ایران اکنون با تولید انبوه ویدیوهای رپ لگویی، پست‌های طنز سفارت‌ها و محتوای خلاقانه هوش مصنوعی، روایت جنگ را به نفع خود تغییر داده و به شخصیت اصلی فضای مجازی تبدیل شده است.
🔹
در مقابل، کمپین‌های دولت ترامپ با میم‌های تهاجمی و محتوای AI بی‌اثر بوده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/653104" target="_blank">📅 21:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653103">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c29eff5b.mp4?token=uSAzFRFgNXj-az-c50Geawp3py002-mdSHSs-aJlgRcAW8xvoUe62Y6pEQHVbHbClf56f17dU6FoNO7WrJ2VpI45wNXOAeMBw-sp359sAgVOa-DPakl0z1e9rU0jfB4b56vJ_yzixfnuZsNf1s8EkBGLm_a6yjep-yf5ayfzY-MxrgE2wBe8qZAe5uq4N7ReM6YLJmPuio4vWHFXg1ia5yplRdlNY0OS3AR4VDHXZSuXXd3aLYkBFgsUZPboXYZMdDVbRXDusBemZxyFLRp8EgVA7vP6TJ_qwpvFJg_rRnVU86qhVxNOoRszEruvjokZaq4VJG8JBDY4DvYJXnxz6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c29eff5b.mp4?token=uSAzFRFgNXj-az-c50Geawp3py002-mdSHSs-aJlgRcAW8xvoUe62Y6pEQHVbHbClf56f17dU6FoNO7WrJ2VpI45wNXOAeMBw-sp359sAgVOa-DPakl0z1e9rU0jfB4b56vJ_yzixfnuZsNf1s8EkBGLm_a6yjep-yf5ayfzY-MxrgE2wBe8qZAe5uq4N7ReM6YLJmPuio4vWHFXg1ia5yplRdlNY0OS3AR4VDHXZSuXXd3aLYkBFgsUZPboXYZMdDVbRXDusBemZxyFLRp8EgVA7vP6TJ_qwpvFJg_rRnVU86qhVxNOoRszEruvjokZaq4VJG8JBDY4DvYJXnxz6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میزان حمایت از جنگ ایران در غرب چقدر است؟
🔹
نتایج مهم‌ترین مراکز افکارسنجی دنیا داده‌هایی را به شما نشان می‌‌دهد که حیرت‌زده خواهید شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/akhbarefori/653103" target="_blank">📅 21:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653102">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
رئیس سازمان بهینه سازی انرژی در مورد شایعه گران کردن بزنین: دولت فعلا قصد گران کردن بزنین را ندارد
🔹
سقاب اصفهانی: برخی تاسیسات ما آسیب دیده و نیاز به صرفه جویی داریم.
🔹
درصورت اینکه با کمبود مواجه نشویم گرانی بنزین در دستور کار نیست
🔹
اما اگر این موضوع رفع نشود ممکن است به نرخ سوم بنزین فکر کنیم تا بتوانیم بخشی از یارانه دولت را به بخش‌های ضروری مثل دارو اختصاص دهیم.
🔹
من هم می‌‌توانم مثل خیلی از مسئولین بگویم مشکلی وجود ندارد اما اینگونه نیست و ماهم دچار کمبود‌هایی شده‌ایم.
🔹
پ.ن: نرخ سوم بنزین ربطی به نرخ‌های ۱۵۰۰ تومانی و ۳۰۰۰ تومانی نداشته و معاون رئیس جمهور از طرح موضوع نرخ سوم این است که مصرف بیش از سهیمه با نرخ سوم محاسبه می‌شود که این موضوع نیز در صورت صرفه جویی مردم ممکن است در دستور کار دولت قرار نگیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/akhbarefori/653102" target="_blank">📅 21:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653101">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
توزیع مرغ منجمد با قیمت کیلویی ۲۶۰ هزار تومان آغاز شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/akhbarefori/653101" target="_blank">📅 21:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653100">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOt4kySUnBM1WkWE0F7dJjJdkxEvCUgzH2fyZ9WNnWl52dqPb44nEdLuCuPx1xKFuGM_sr5szJ5c-C1fLaMR_3EuyG3FIeuz4TEmPJOTtyo3Bi1KcyPgN1QNS-Veoy_6W91KJiPdcAHth-LEt0BdXUq2JWdVEj2DVFuEp7x5cFhao8pmluubbj3fBjvlcQDxyghNR80KlzAEjLIbQrfBAejgzgmDtzZgKSvNoRmKMIcvBL2AwZ91Syn9DeSya-sAlNktR0p2DWQ2Dl-A4l7_UReNxLdxFgpZ8x2qONGDoAjW-K3uuq9XSY5jVnwNlpEKbT60SR0mXCQB0UN6efoCKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارن پالیسی: ایران می‌تواند بزرگ‌ترین شکست ترامپ باشد
🔹
ترامپ امیدوار بود که بتواند رئیس‌جمهور چین را متقاعد کند تا میانجی‌گری یک توافق صلح بین واشینگتن و تهران را بر عهده بگیرد. اما این اتفاق نیز مثل خیلی از اتفاقات دیگر برای ترامپ رخ نداد.
🔹
ایران هنوز ۷۰ درصد از ذخایر موشکی پیش از جنگ و دسترسی عملیاتی به بیش از ۹۰ درصد از سایت‌های موشکی خود در امتداد تنگه هرمز را دارد. اینها یعنی ایران می‌تواند تا هر زمان که بخواهد به اخلال در حیاتی‌ترین گلوگاه انرژی جهان ادامه دهد.
🔹
یک بحران غذا در جهان و کمبود نیمه‌هادی‌ها که به هلیوم متکی هستند، از هم‌اکنون در پیش‌بینی‌های اقتصاددانان برای سال آینده گنجانده شده است. هرچه این بحران بیشتر طول بکشد، هزینه‌ها بالاتر خواهد رفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/akhbarefori/653100" target="_blank">📅 21:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653099">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M90bn2kVQ2ya0AIj2JpbHhUcRQzq7Vxx4V7KR3PFbH4aAJcoHiTw36-Zrd1lPPmhCr5Oc8d3Wr7jLXWxzFvvXrE_hOh_H3Bt0xBqrmvXi4kMoUnzAaD35IlCWEGYt0joGocmTOeI-BPbZ54ts3_SCBFTDm9hsN-6fSqlYnJSyoMbZcElkRwt5NW1xCfrLBh0LLiRWqB2e6hXxXgjzWkSFY9Niqv-IwAYnuOlVXt5HSOfwlvJT4qeayLTKxjRD6iT6TDXkerFJm01f5TWvacomKXSIyRAPwceO6HNi2nrOeTEqsLOuBaw2eq_sCZAHr8EcTnhIbTybI753P5r68a_wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بوس به بورس
🔹
برخلاف القای رسانه های معاند و کانالهای فارسی زبان برای ایجاد صف فروش بورس تهران امروز عملکردی امیدوار کننده داشت. شاخص کل با رشد ۲,۵۰۰ واحدی به سطح ۳ میلیون و ۷۱۶ هزار واحد رسید. شاخص هم وزن نیز بیش از ۲,۶۰۰ واحد افزایش یافت. جریان سازی های منفی نتوانست روند صعودی بازار را متوقف کند و بورس خلاف جهت نمایی ها ظاهر شد.
🔹
هفتصدوپنجاه‌وچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/akhbarefori/653099" target="_blank">📅 21:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653098">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6ae8ec25.mp4?token=Afno2qNTswTx_IminBbuo099GF5d1V_QhsrRS4F1XuVEjvaXLkriB8O6kUrJTVPbo09EbsWyhkYIddrrkQXJLT2h6FRZPqeLjVqWZOGtrUrES5x7P76H6T6BJk8eI82IQmVQOj35eD6bDO_C2L5K8CXCnd4KdSfzTztHiUNxEeMUS2aLw13ooea2cFT2a4zkQ2AcBwR96RsfJyN5yjGU8zMkMJW88hSIz-0il-d4HX8zgb6dwmrWB2o2zDQSpKw4b5-0wxvJbMqTFcCIPBCkR8Q328XLdI3IMbOw70kMqWTVJNsNVHRpzvu9HlzV8QunfRgqWFdFrOTqkDx1vZtNZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6ae8ec25.mp4?token=Afno2qNTswTx_IminBbuo099GF5d1V_QhsrRS4F1XuVEjvaXLkriB8O6kUrJTVPbo09EbsWyhkYIddrrkQXJLT2h6FRZPqeLjVqWZOGtrUrES5x7P76H6T6BJk8eI82IQmVQOj35eD6bDO_C2L5K8CXCnd4KdSfzTztHiUNxEeMUS2aLw13ooea2cFT2a4zkQ2AcBwR96RsfJyN5yjGU8zMkMJW88hSIz-0il-d4HX8zgb6dwmrWB2o2zDQSpKw4b5-0wxvJbMqTFcCIPBCkR8Q328XLdI3IMbOw70kMqWTVJNsNVHRpzvu9HlzV8QunfRgqWFdFrOTqkDx1vZtNZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت بازار مرغ در میادین تهران
🔹
توزیع مرغ منجمد با قیمت کیلویی ۲۶۰ هزار تومان آغاز شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/akhbarefori/653098" target="_blank">📅 21:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653097">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ونس، معاون ترامپ: اگر ایران به سلاح هسته‌ای دست یابد، بسیاری از کشورهای دیگر نیز خواهان داشتن سلاح هسته‌ای خود خواهند شد
🔹
ایران اولین دومینو در یک مسابقه تسلیحاتی هسته‌ای جدید خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/akhbarefori/653097" target="_blank">📅 21:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653096">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
صورت‌ حساب ۵۸ میلیارد دلاری بازسازی در خلیج فارس!
🔹
مؤسسه «ریستاد انرژی» برآورد کرد که هزینه تعمیر و احیای زیرساخت‌های مرتبط با انرژی که در جریان جنگ خاورمیانه آسیب دیده‌اند، ممکن است به ۵۸ میلیارد دلار برسد.
🔹
رقمی که سهم تأسیسات نفت و گاز از آن می‌تواند تا ۵۰ میلیارد دلار باشد. این رقم به‌ طور متوسط حدود ۵ میلیارد دلار خسارت در بخش‌های صنعتی، نیروگاهی و تأسیسات آب‌شیرین‌کن را نیز در بر می‌گیرد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/akhbarefori/653096" target="_blank">📅 21:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653095">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEJzdvnQSvIIJltnOH05QSsnHirFtVswb_Z00c0N5q7RDTZFomQLAjJ7BV2GbRFBnrscLxck5pHfDYqRuReSTMuh1SxSox6m-4QkAI60J_e8ZLZwEus-mldHzyHDxNRJ6jC7Tvzji5oFeOL7EZH44IlD7owd_r6B3kHyHk4gtDoztbXW4HEIeD-dg7OkVuNFOtWDQ9bUNca4UabhsFb-LRtvALQHmY6SlpnKOL0E0KYz4CaAEsZOiU-4RWr-UG_CPvoNYVJy0brY1QALqm8mHcVEgDVkYmxUQ0qYywVYF5YD8HQFqPTRIptMRW7hzXDptih6Oh4Q0F_ErV-_SfTEMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد متولدین هر سال در ۱۲ سال اخیر
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/akhbarefori/653095" target="_blank">📅 21:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653094">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojZ9MslwyyE-s7cqImmtsGVTpZtxCehn0IvJ1yfAr7rTJY5giFElTowySRz1xkLaeg0zl6xvNiyzx93Ld7ZAoE-BE3FzAMkR_M2DufonHPXDt0EEzBGMMaAS1S82ru8Fbs3_a-WkBjHgOz64L2QGH0Tef7ZDEW9UUCOT2EWLoKW-_AJEkk55nT9X8U7W91aml3d5xPyrqJVCERrFC4eh3sTSGGrbddvKN3T7A0zUhXxwgkST9YrFtHBo67qhXv5cnO5yEUqVeyxS7QT2m46LpyWbclV6VKNhqaOSnaV_TQjVERQMWSCiCLHDCuE9n8jiv9MhAIx7QgG6HEqm6YVV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقامات اسرائیلی: حمله به ایران فقط مسئله زمان است
🔹
شبکه ۱۲ اسرائیل روز سه‌شنبه گزارش داد که مقامات اسرائیلی ارزیابی می‌کنند که حمله به ایران بیشتر مسئله زمان است تا احتمال آن و حمله به ایران را قطعی می‌دانند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/akhbarefori/653094" target="_blank">📅 21:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653093">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3b3e60533.mp4?token=joqukIKQuDCihzlbcxEHtr_tVuXqPUChPRz5MWDakezcpRCRpI14DL8v7jIFZkWchAgXdulT9jBZvP-g9GXl__sLts3wcgd-BMyp0OeyknyScOgxoIdbYFvwExXHAc2SYLQp4tUecCJLbJieBodWLlLgIeYtHRm21x5K9v8G6Uc3rYRNVJgnwA1aCZvwxHrTDkS1S_zE2duQ0uwQYpdNtkX10Dm1hMVAg-z1o4tGrvZ_LuX98Oq5RKf_rWSyD8OpE57OSTTwXFoUfvIsk1R98zsVHM7k71M3WHvILkBRe4vDrcFEampr1z8k-maohK6A4sByPJwRq8zbIys91Cjmu4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3b3e60533.mp4?token=joqukIKQuDCihzlbcxEHtr_tVuXqPUChPRz5MWDakezcpRCRpI14DL8v7jIFZkWchAgXdulT9jBZvP-g9GXl__sLts3wcgd-BMyp0OeyknyScOgxoIdbYFvwExXHAc2SYLQp4tUecCJLbJieBodWLlLgIeYtHRm21x5K9v8G6Uc3rYRNVJgnwA1aCZvwxHrTDkS1S_zE2duQ0uwQYpdNtkX10Dm1hMVAg-z1o4tGrvZ_LuX98Oq5RKf_rWSyD8OpE57OSTTwXFoUfvIsk1R98zsVHM7k71M3WHvILkBRe4vDrcFEampr1z8k-maohK6A4sByPJwRq8zbIys91Cjmu4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مادر عسل دانش‌آموز مجروح مينابی از رنج‌هاى فرزندش مي‌گويد...
▪️
مستند تلویزیونی
#من_زنده_ام
به روايت مژده لواسانى
روزهای زوج و جمعه‌ها حوالی ساعت ۱۸:۳۰
📺
شبکه نسیم
▪️
محصول مرکز سیمرغ
قسمت‌های گذشته این برنامه را در تلوبیون ببینید ...</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/653093" target="_blank">📅 20:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653092">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svXmkwn6ajcwMLog2zZWnwQWjv0SgrvQvI2IsRIOctNLYQsncQjp7RCH2V6nCi5Sj1azXIP5Ta-_1b0Yst-vz2Ob8kt5PJr6FLQuCpJxHiYOYruXOKyu4oCt1Gts0v7vsnzJVDnOJfd2DT7rUei-9sNgn_pVo06G-iSbdZVbsbcWFMWpMtmrICa5IuB7iBIQttxT7LceNAV5mWNycawd9Do5Yia5dT9vqou-bKl3THjnKu5cR3XazFZEYUXC3R0MNvmGLX7nUaHahngcWs8K5EGG0Q4ulGS79Cvq1j8gYNb-XKJjnWW5Qx1XO37qBffWKKIRqDFuQgXwnaZqjJq3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هلاکت یک نظامی صهیونیست در جنوب لبنان
🔹
رسانه‌های عبری از هلاکت «ایتامار سبیر» از عناصر یگان ماگلان با درجه سرگردی در نبردهای امروز جنوب لبنان خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/653092" target="_blank">📅 20:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653091">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-Sx92NSEmCDsqqDu59-7geTpsB1fKE_XwfL6Roi5kRvEO_a-7UOQ4ObwSjRTLt9Oc0oneLO_HWncFRzAJsaV83ykcm-lbiLQB2CpQIF8ZxJ_gDH_icHC-ZeZhM5yi1LKj7y_TwSvYjw2SoKhUkOFVe5ccnG4LFH8QE9-BrQ7bsPx8a3tp8MQq6O3LzvLHYCxJyRof1csfa1XJ3bAFTg2nTa8IZ14W7ii1070Mw338HdVST3w2n5y7mfyammUOurZcsuTpoKIhQ2X585P4maBPWTey-oWH9g50uVY_cBkpHmmXFHg0wW0oEWferqinPvPILz8iETUKVwZ6WYTjvw7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار عباسعلی فرزندی به یاران شهیدش پیوست
🔹
سردار عباسعلی فرزندی، رئیس پیشین دانشگاه عالی دفاع ملی امروز به‌علت بیماری و جراحات ناشی از ۸ سال دفاع مقدس دعوت حق را لبیک گفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/akhbarefori/653091" target="_blank">📅 20:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653090">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3da56e431.mp4?token=XGqsYupM6avIFYqHb5UW6I3HiLouOlu0-MLvXVzCflRWx1U9yTwWo_UkFmMLGIbr2aps3asgfIaWksdRf6OD4UCDv2igDO08invh_n0EFoPg5h4VbAt3girWPVxzvRNX6DGYF_pdh8rLYTys1OFHiEGlAGhr1rxukObh0-qr4UTKDiCjX7L9BPV7jpij6J3Xw0gSLIBJrw7l6qrC094Lc0ZCzXmMrYqR6gX4-6VWtOgVz1kB8LAXyp9bV7Av-YCGZ7qXPpfY0zwUSXCpm1kbXveqeJ-l5bIiYhSOA2Iv0N_CZDqFGDI82VIPQnZiPFOhtPq8nAQlqEUWi2IyhBqPgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3da56e431.mp4?token=XGqsYupM6avIFYqHb5UW6I3HiLouOlu0-MLvXVzCflRWx1U9yTwWo_UkFmMLGIbr2aps3asgfIaWksdRf6OD4UCDv2igDO08invh_n0EFoPg5h4VbAt3girWPVxzvRNX6DGYF_pdh8rLYTys1OFHiEGlAGhr1rxukObh0-qr4UTKDiCjX7L9BPV7jpij6J3Xw0gSLIBJrw7l6qrC094Lc0ZCzXmMrYqR6gX4-6VWtOgVz1kB8LAXyp9bV7Av-YCGZ7qXPpfY0zwUSXCpm1kbXveqeJ-l5bIiYhSOA2Iv0N_CZDqFGDI82VIPQnZiPFOhtPq8nAQlqEUWi2IyhBqPgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنگه هرمز چه زمانی بسته شد و چگونه باز می‌شود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/653090" target="_blank">📅 20:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653089">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a17997558.mp4?token=q3tlAnobxvAe0F21mMDNyX5oTSc-xMxnfhnUyaY9QFrh1Q3SZ638fqFF9opPgV4bvfXlHRB20KVwJrw1OGZsXFRpwBeVqjegWD1F7TUUr2jf0saodwqlKZ-HD6i3soAZd75CwcHJllA6-JXO_IvdU8dyaOoJKN8HhPVi_wcZl8Eyp6Zufpg9uLCHbj5De33Nr_fHBRQh7S8kts4rH78k_UMgjxfQ_kXxbInxjIURK11qV4nQ9KK5EiMsJ0jdRIHYytvZyAomKnC9yy65WooVsgT32Ei8y5okVdW2WrMR3T5DceQlIabQeX3hnq-Ed7x-NUnigjv8290-vGAUek8dxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a17997558.mp4?token=q3tlAnobxvAe0F21mMDNyX5oTSc-xMxnfhnUyaY9QFrh1Q3SZ638fqFF9opPgV4bvfXlHRB20KVwJrw1OGZsXFRpwBeVqjegWD1F7TUUr2jf0saodwqlKZ-HD6i3soAZd75CwcHJllA6-JXO_IvdU8dyaOoJKN8HhPVi_wcZl8Eyp6Zufpg9uLCHbj5De33Nr_fHBRQh7S8kts4rH78k_UMgjxfQ_kXxbInxjIURK11qV4nQ9KK5EiMsJ0jdRIHYytvZyAomKnC9yy65WooVsgT32Ei8y5okVdW2WrMR3T5DceQlIabQeX3hnq-Ed7x-NUnigjv8290-vGAUek8dxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشاره رهبر انقلاب به دغدغه رهبر شهید درباره افزایش جمعیت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/akhbarefori/653089" target="_blank">📅 19:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653088">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lV9oOyHZmS3CIY-4El2GlYu-5sIbEetnQJXfk4jnfwb2UoM95rTdHG1NTa33GZDxthq8uWla5GJ03h4kmZp6zVdLZea1mHLiP0YS7w30zSSZVC4rUEIS8yxP9Wh2n5lD-PoKpTPEAm-jZx5x5zJf732AC6F21KsCF2PG9tzZelY9UmlHKGdDJzAxvfZBmDUvldRjEuYSUCy-hsZ_5GVKrbmV3PHJ-9b5llOQkO-LunYscvmYv4B003Eguembi_m8DnbekEPK5Wd9C-ZqcXVeC4afaxkZCIbFCtH_d86FFSy_F-JXHWcw9k7eGS8AySL7CX-JSJ8jtk8RqE2fjMuzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر صهیونیست، ترکیه را تهدید کرد
🔹
«میکی زوهار» وزیر کابینه نتانیاهو در سخنانی با بیان اینکه ترکیه باید به عنوان کشوری متخاصم برای این رژیم تلقی شود، تهدید کرد در صورتی که جنگی دربگیرد، آنکارا تاوان سنگینی خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/653088" target="_blank">📅 19:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653087">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
تکمیلی/
🔹
آمریکا ۱۲ فرد، ۲۹ نهاد و ۱۹ شناور را به فهرست تحریمی خود افزود.
🔹
اکثر این تحریم‌ها با ادعای ارتباط با ایران وضع شده و تعدادی از آن‌ها نیز مرتبط با جنبش حسم مصر، فلسطین و حماس هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/akhbarefori/653087" target="_blank">📅 19:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653086">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73c56a8557.mp4?token=cUfX0NRFY6oipns733Dbujvd43EPYKY7aPdm9zY6ChAlrhoVE8qIqM6722Xbx5pFfnAZ1J7q7cEU2w1ZXFCKsYsvbo8v7nCT1RfYBSVlnsc7nzNNoXNGxNiIXoBaaIuBTx4vT4bsi8i8XXkw263mcKpnVADDN4AM0iv1ZxQs3A5rvSowz64D-oI7w1YVi6GNCm4ahFQbJLNycJYYwbsTd39JB_qZDcysrSJHuTVr71lXlBCx9GU5GYquWdDfIDpusu_p80k2gJPWTFWPnx-J0rz6SxaMKuYnUbYrmHrjt9wqcXQVF8Xb6_2Wo_puALZ-FR5RuG0xRcxc1gqGDkRFriVRmv8SMruRbs080Pq0MgK3P9beZm7LUJlyDT9x-T7CfGvM5DfRBLtqsPYPhvPUN71lEY_u6T8e9N34Y9NgNAOSEvuK2u0r70K2yllsWAGOnpII10a2zAkS-YU0L8Knhosu9CfBqQ0aG_tse6PXz2gLox_a-tnGyatZLX8fDwSUwBCR8UTqBggYPw4nB09rDmsG81Gis2bzsaC5XLmZrsD4tHG5GvZ34HpMzLAs02tsdIrepUPrf8zOWkrXQ6sQwIVUjAvJCTK895X_LVi6K_TF0PrORJ4MBQavY77fZ_zvP2omqFCTiI-7dVTHYil1ccknP2BimLoA7DKDDr2SJCI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73c56a8557.mp4?token=cUfX0NRFY6oipns733Dbujvd43EPYKY7aPdm9zY6ChAlrhoVE8qIqM6722Xbx5pFfnAZ1J7q7cEU2w1ZXFCKsYsvbo8v7nCT1RfYBSVlnsc7nzNNoXNGxNiIXoBaaIuBTx4vT4bsi8i8XXkw263mcKpnVADDN4AM0iv1ZxQs3A5rvSowz64D-oI7w1YVi6GNCm4ahFQbJLNycJYYwbsTd39JB_qZDcysrSJHuTVr71lXlBCx9GU5GYquWdDfIDpusu_p80k2gJPWTFWPnx-J0rz6SxaMKuYnUbYrmHrjt9wqcXQVF8Xb6_2Wo_puALZ-FR5RuG0xRcxc1gqGDkRFriVRmv8SMruRbs080Pq0MgK3P9beZm7LUJlyDT9x-T7CfGvM5DfRBLtqsPYPhvPUN71lEY_u6T8e9N34Y9NgNAOSEvuK2u0r70K2yllsWAGOnpII10a2zAkS-YU0L8Knhosu9CfBqQ0aG_tse6PXz2gLox_a-tnGyatZLX8fDwSUwBCR8UTqBggYPw4nB09rDmsG81Gis2bzsaC5XLmZrsD4tHG5GvZ34HpMzLAs02tsdIrepUPrf8zOWkrXQ6sQwIVUjAvJCTK895X_LVi6K_TF0PrORJ4MBQavY77fZ_zvP2omqFCTiI-7dVTHYil1ccknP2BimLoA7DKDDr2SJCI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: مدل حکمرانی امام خمینی و رهبر شهید ما را به جایی رساند که ابرقدرت انحصاری جهان در مقابل ما زانو می‌زند و التماس مذاکره می‌کند
🔹
مشاور و دستیار مقام معظم رهبری  در بزرگداشت رئیس جمهور شهید و شهدای خدمت:
🔹
در جنگ جهانی اول با اینکه اعلام بی طرفی شد بین ۸ تا ۱۰ میلیون نفر انسان کشته شد. در جنگ جهانی دوم هم ظرف چند ساعت تمام ارتش رضا شاهی از هم پاشیده شد و قسمت بزرگی دیگر از کشور رفت.
🔹
مدل حکمرانی امام خمینی و رهبر شهید چه بود که از این کشور چیزی درست کرده که امروز با ابرقدرت انتحاری دنیا که بر همه جهان تسلط دارد درگیر می‌شویم و او به زانو در آمده و التماس مذاکرات می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/akhbarefori/653086" target="_blank">📅 19:46 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
