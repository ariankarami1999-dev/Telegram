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
<img src="https://cdn4.telesco.pe/file/rJD7z0XlXXPABfUIVAiVPexi7Z--2yuzZYrKNh38r-mG_YcikvbgKYYS8hS3ESp0CM5Q3ZVLRmV3iWCKI1lxt1NhKUx_cGQq8QuGOJhmk78eh8QAblExvpFPI2OTBQEmFrpr4dpLrNjbd9w3wbdLfFNTQMcudRPwyZaCH9MyzEdHxNeBVst6cYNbaK27U53zEqy2wI41YWsc4zvhMT-eaXvNUlaPJqCIUNNZ1kwG2U8vtteuyzflKyRoiQ6DUOEnv_apjThdvm-orvoCQgVMn9JxS2P3L-DY5gWJS6yuZ8j0ULyQjBZk3MYrkRuJWvsC9KjAdX1-XnjEArMvjfxsTA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.27M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 19:02:49</div>
<hr>

<div class="tg-post" id="msg-688775">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a112479587.mp4?token=CzxrTL6-ze8FevrMDguWV8-LZ7DSDEiqcZ6GhfltidXugLX6DdktPulH8RAyOV245tL5FuHNItILXKlSvobXdwTISdQ_5WbTBq1y3ngXqZqNjaBQb1WkLCqMA_tMpARNHjf4FQDONojVwRsQPrdygi69k0xsphAwac_FoouPmBQW3cg6Y6v7S7y2Nw0tKiDjmnUaGWogVc4IMxvgtVum4NDpxSxKIvGiP95umx4U_w5B-nDa5Zejq8dDKMjpKRKTf-3vcUyCklGLIfBZqJ_C08q-IXjAmw6mPFwN-11g5z-Ev1PWQCXLrzW-ndTYrQyNM5stLDrcR5GTYVVJlZub0URMeP48jnBP13i2zoo2qiCgbxLpEd43wFSCJDgi1Ud9kXzG1YfH9pmJUlfG3XU2cPGYM-3-hisIN1FSIss47g42KPBF0uUjHXHQxriMkcbIqcsS-aNfbZJV_iXnMI-Fmg_kTg2TreJm4SvYZkyuUHExoIcs2V0PGdkRlNBIj4tAu2iTKVCXcLKNhfpZ5N3aMzGiWlpaZAVBLpfv6UoSRK0ZmbSkTkpTcC6na7KRJfO9jLy2DCvb_6OM5COgsncotMKzW66wYhqJ8A6B9jH7eDnXuxf3Zydiy7MEhLXPvHCZqFyhLRp8OjehPml9pP5iL8V7S4rGoJL7KDyWDo9eVzc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a112479587.mp4?token=CzxrTL6-ze8FevrMDguWV8-LZ7DSDEiqcZ6GhfltidXugLX6DdktPulH8RAyOV245tL5FuHNItILXKlSvobXdwTISdQ_5WbTBq1y3ngXqZqNjaBQb1WkLCqMA_tMpARNHjf4FQDONojVwRsQPrdygi69k0xsphAwac_FoouPmBQW3cg6Y6v7S7y2Nw0tKiDjmnUaGWogVc4IMxvgtVum4NDpxSxKIvGiP95umx4U_w5B-nDa5Zejq8dDKMjpKRKTf-3vcUyCklGLIfBZqJ_C08q-IXjAmw6mPFwN-11g5z-Ev1PWQCXLrzW-ndTYrQyNM5stLDrcR5GTYVVJlZub0URMeP48jnBP13i2zoo2qiCgbxLpEd43wFSCJDgi1Ud9kXzG1YfH9pmJUlfG3XU2cPGYM-3-hisIN1FSIss47g42KPBF0uUjHXHQxriMkcbIqcsS-aNfbZJV_iXnMI-Fmg_kTg2TreJm4SvYZkyuUHExoIcs2V0PGdkRlNBIj4tAu2iTKVCXcLKNhfpZ5N3aMzGiWlpaZAVBLpfv6UoSRK0ZmbSkTkpTcC6na7KRJfO9jLy2DCvb_6OM5COgsncotMKzW66wYhqJ8A6B9jH7eDnXuxf3Zydiy7MEhLXPvHCZqFyhLRp8OjehPml9pP5iL8V7S4rGoJL7KDyWDo9eVzc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دوربین موبایل‌ها روز به روز عجیب‌تر میشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13 · <a href="https://t.me/akhbarefori/688775" target="_blank">📅 19:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688774">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
روسیه در شورای امنیت: اجازه بازگشت تحریم‌ها علیه ایران را نخواهیم داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/akhbarefori/688774" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688773">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
نماینده پاکستان: دیپلماسی و گفت‌وگو باید اصول راهنما برای حل موضوع هسته‌ای ایران باقی بماند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/688773" target="_blank">📅 18:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688772">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
گزافه گویی های نماینده دانمارک در شورای امنیت: ما از ایران می‌خواهیم از حمله به کشورهای منطقه خودداری کند
🔹
ایران باید به‌طور کامل از قطعنامه‌های شورای امنیت تبعیت کند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/akhbarefori/688772" target="_blank">📅 18:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688771">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097198224.mp4?token=AVnIz22RucUHIAM0QNJjFhW6kUm7pWJsytfZIPwHZYNJBL3kg7P5HNKp4H0Q07UAPz9AzqFtQg3ysUxj_6VoH3NcQ7FYvtvXpKNXDxf6THP_LYH4RPVD5ifDGruQ3McLFXqY6mNRy8nMiO87AaHeOLwjLB1Tf61p2Z0B6W0-2n2Ya3ccxhENzuaxr7nff0OoPjAjnSJjt3_kL6Bd1muIqV1iBYYoB22RHmq00qUY934o-mMb6Nn_IEyq1AdXKtFtW3uDKIYhy_5L86cg96oAKwrd2PfgBMjgE16RSWDGmZEoFTfazRife-ot5oEc_-LnXuszI-IxJqVjt5GSAFu1cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097198224.mp4?token=AVnIz22RucUHIAM0QNJjFhW6kUm7pWJsytfZIPwHZYNJBL3kg7P5HNKp4H0Q07UAPz9AzqFtQg3ysUxj_6VoH3NcQ7FYvtvXpKNXDxf6THP_LYH4RPVD5ifDGruQ3McLFXqY6mNRy8nMiO87AaHeOLwjLB1Tf61p2Z0B6W0-2n2Ya3ccxhENzuaxr7nff0OoPjAjnSJjt3_kL6Bd1muIqV1iBYYoB22RHmq00qUY934o-mMb6Nn_IEyq1AdXKtFtW3uDKIYhy_5L86cg96oAKwrd2PfgBMjgE16RSWDGmZEoFTfazRife-ot5oEc_-LnXuszI-IxJqVjt5GSAFu1cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحریف واقعیت توسط نماینده آمریکا برای پوشش شکست تحریم‌ها و تقابل با اراده جهانی  نماینده آمریکا در شورای امنیت:
🔹
امروز باید گزارش ۹۰ روزه از وضعیت هسته‌ای ایران ارائه شود، اما دولت ایران متأسفانه دسترسی‌ها به مناطق هسته‌ای را مسدود کرده است
🔹
روسیه و چین…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/akhbarefori/688771" target="_blank">📅 18:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688770">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خبر بد برای آقایان؛ خانم‌ها در رانندگی با موتور و ماشین قانون‌مندتر هستند
مهدی قمصریان، مدیر عامل صندوق تامین خسارت‌های بدنی در
#گفتگو
با خبرفوری:
🔹
با توجه به شرایط اقتصادی و اجتماعی، ضریب استفاده از موتورسیکلت توسط خانم‌ها در جامعه افزایش پیدا کرده است.
🔹
باید در نظر گرفت در صورت رانندگی بدون گواهینامه، هیچ حمایتی از راننده مقصر آسیب‌دیده صورت نمی‌گیرد و این موضوع می‌تواند به رشد چشمگیر آمارها منجر شود و رانندگی بدون گواهینامه، خانم‌ها را از برخی حقوق شهروندی از جمله برخورداری از پوشش‌های بیمه‌ای محروم می‌کند.
🔹
به دلیل تعداد بیشتر آقایان، ممکن است تعداد حوادث و خسارت‌های مربوط به رانندگی آن‌ها بیشتر باشد اما بر اساس مشاهدات، خانم‌ها در استفاده از خودرو و موتورسیکلت، قانون‌مندتر رانندگی می‌کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/akhbarefori/688770" target="_blank">📅 18:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688769">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
دبیرکل ناتو: مین‌روبی در تنگۀ هرمز به ما مربوط نمی‌شود
🔹
موضوع مین‌روبی در تنگه به قلمروی ناتو مربوط نمی‌شود. البته ما آنچه درحال وقوع است را زیر نظر داریم و کشورهای عضو ناتو از نزدیک با یکدیگر هماهنگ هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/688769" target="_blank">📅 18:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688767">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
بشارت به مردم یمن و غزه؛ باب المندب آزاد شد
🔹
خبرهای اولیه از ورود مجاهدان یمنی به جزیره فوق استراتژیک میون در باب‌المندب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/688767" target="_blank">📅 18:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688766">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A__2GQ-_XjtsPwTqWpzqBOjHbMxB4F_rHKvRzjtvAHmORkT-m9TDS1cajxZ3C7iVbt04uKuDfa8X2I7kKuUb7tVrCRItT7HyBd_0SfwsekLmGPPMKYi74C0LUbOGMkLVD1mQKv3LjQngCIcptMCOD8U36lQVx6JVtThVu0DvDVBbV_FXbrKkXKvYFAP3-2Rqrj1DLgaEKBFmnjaL1X0vlAegtekZqmpfgUY_GHudjBq8ajh84FH96fURt2DA7YdFFGP_lIclkKUF7ceFIARO7wLCL_RJ-AV-USaZs0ERaW6mxQSntesc5hEa5hys5zYfcqVXbmbuhA3-_leuxDh0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدیدترین تصویر از آیت‌الله جنتی که امروز منتشر شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/688766" target="_blank">📅 18:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688765">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
برخی منابع رسانه‌ای از حادثه امنیتی جدید در‌ تنگه هرمز و وقوع انفجار خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/688765" target="_blank">📅 18:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688763">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
سکوی تجاوز آمریکا به ایران در جایگاه شاکی / نماینده بحرین: حملات اخیر ایران نشان‌دهنده عدم پایبندی به قوانین بین‌الملل است!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/688763" target="_blank">📅 18:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688762">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
طرح دوباره ادعاهای واهی علیه برنامه صلح‌آمیز هسته‌ای ایران توسط نماینده انگلیس!   نماینده انگلیس در نشست شورای امنیت نماینده انگلستان در شورای امنیت:
🔹
ایران به فعالیت‌های هسته‌ای خود ادامه می‌دهد و از تعهداتش فاصله گرفته
🔹
ایران تنها کشوری است که بدون داشتن…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/688762" target="_blank">📅 18:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688761">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
تایید برنامه جلسه امروز شورای امنیت برای بررسی برنامه هسته ای ایران با وجود مخالفت چین و روسیه
🔹
11 تایید
🔹
2 مخالف (روسیه و چین)
🔹
2 ممتنع
🔹
این رای گیری صرفا برای تعیین برنامه امروز شورای امنیت و تایید بررسی برنامه هسته ای ایران صورت گرفت و رای به پیش نویس…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/688761" target="_blank">📅 18:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688760">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f3228749.mp4?token=F0L6ccX6Brnehh_dYr4tlLaoIQbZ5fulnprySqZ7-pQxiY8g-rteVSfb5Qw92-elFzZJVYNurA7fr24paed_1Iw5tlzllPKqXT3P4CKKcXSQRX9CamSUqIfsPtqEm9-xzOKtm0iNBAxX4cOMuyUqRVLwq_oD-ytdJioifUsb4aoCa_fKvGSJiXD-CzNnvhCwdkz054T0yj0A1XBNF4kQM0BZmAllfH5DxLy9Yb6zQVupIqummEeap3i7N3n0s-TBrsaGQ37F62hP16CMNDziaRkyU4ku2KlLYYD_132ZlLAX3nhpW23Uu-ENB0Oywyp_-BTGcn7th0LMjksDGDHWRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f3228749.mp4?token=F0L6ccX6Brnehh_dYr4tlLaoIQbZ5fulnprySqZ7-pQxiY8g-rteVSfb5Qw92-elFzZJVYNurA7fr24paed_1Iw5tlzllPKqXT3P4CKKcXSQRX9CamSUqIfsPtqEm9-xzOKtm0iNBAxX4cOMuyUqRVLwq_oD-ytdJioifUsb4aoCa_fKvGSJiXD-CzNnvhCwdkz054T0yj0A1XBNF4kQM0BZmAllfH5DxLy9Yb6zQVupIqummEeap3i7N3n0s-TBrsaGQ37F62hP16CMNDziaRkyU4ku2KlLYYD_132ZlLAX3nhpW23Uu-ENB0Oywyp_-BTGcn7th0LMjksDGDHWRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترتیب ماه‌های میلادی را یاد بگیر #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/688760" target="_blank">📅 18:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688759">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
تحریف واقعیت توسط نماینده آمریکا برای پوشش شکست تحریم‌ها و تقابل با اراده جهانی  نماینده آمریکا در شورای امنیت:
🔹
امروز باید گزارش ۹۰ روزه از وضعیت هسته‌ای ایران ارائه شود، اما دولت ایران متأسفانه دسترسی‌ها به مناطق هسته‌ای را مسدود کرده است
🔹
روسیه و چین…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/688759" target="_blank">📅 18:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688758">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8d4cd9b0a.mp4?token=cG14hY6lcm3cgFdxEuJVX3ERIbnVM9J7N3AJ0Jawp5Tca_fE8k9HaX8xmbpaOAROs_4obEKk2c49Z-AbcvXGxxaQQ7EKzRMwboLqUaYZWkfQZa2k3uv3m0JaYXBOoByrnl6PvfWKqhPIqukxGA5ISLRGEPW6Da5-clU3KuinJBKRviIBTznlqCQb8zwCb2YbdsF5vgw-OWw6kUCrTlZ3DUFtUDKKBxBnMyA-O5bpWx71c96aKiOQKjrRbO99Zp-f2PH6yYymJwgUcbV5uRSXhhfxXffOcWw61c9jaFSgavpOcNp66FSthpUYL0xo3OOM3QhdIl9arSjZqydABShVFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8d4cd9b0a.mp4?token=cG14hY6lcm3cgFdxEuJVX3ERIbnVM9J7N3AJ0Jawp5Tca_fE8k9HaX8xmbpaOAROs_4obEKk2c49Z-AbcvXGxxaQQ7EKzRMwboLqUaYZWkfQZa2k3uv3m0JaYXBOoByrnl6PvfWKqhPIqukxGA5ISLRGEPW6Da5-clU3KuinJBKRviIBTznlqCQb8zwCb2YbdsF5vgw-OWw6kUCrTlZ3DUFtUDKKBxBnMyA-O5bpWx71c96aKiOQKjrRbO99Zp-f2PH6yYymJwgUcbV5uRSXhhfxXffOcWw61c9jaFSgavpOcNp66FSthpUYL0xo3OOM3QhdIl9arSjZqydABShVFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر دفاع یمن ترور شد
🔹
منابع یمنی می‌گویند محمد العاطفی، وزیر دفاع دولت نجات ملی، همراه با شماری از فرماندهان انصارالله در حمله هوایی به غرب تعز ترور شد.
🔹
انصارالله هنوز این خبر را تأیید یا تکذیب نکرده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/688758" target="_blank">📅 18:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688757">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22e2097cb2.mp4?token=SutpOgL8Q-P83efMsI4OLRlQ-MrH0DXbJbDHjuzDW_4gjnuMr_TfM2E2b18ZBmBED3rZAM0Bp9G7fDTB2QRRZjnk9e94eahOjUkXPcYp6EH_CwphmzHP24vvZTu6HVHRIzH65pXUke7ce9avTIx1r7uMV4RuW5jkm88mqIB4Flr-M1I56r5vah0lV1tYIUmT64ZI08ybo28RXLm0vYf6cjqBpyEv_AQFg-rBob12H9ZuBFAtMi0uC-SHAXCwoYZJEDGaSYeEyccKDb5YJb7IUoNeA6sxos_W08hCQEEFoE4KtKV9FCOdBLNL3vHxEGFYmpyiKl8lz7PYi39vqeftVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22e2097cb2.mp4?token=SutpOgL8Q-P83efMsI4OLRlQ-MrH0DXbJbDHjuzDW_4gjnuMr_TfM2E2b18ZBmBED3rZAM0Bp9G7fDTB2QRRZjnk9e94eahOjUkXPcYp6EH_CwphmzHP24vvZTu6HVHRIzH65pXUke7ce9avTIx1r7uMV4RuW5jkm88mqIB4Flr-M1I56r5vah0lV1tYIUmT64ZI08ybo28RXLm0vYf6cjqBpyEv_AQFg-rBob12H9ZuBFAtMi0uC-SHAXCwoYZJEDGaSYeEyccKDb5YJb7IUoNeA6sxos_W08hCQEEFoE4KtKV9FCOdBLNL3vHxEGFYmpyiKl8lz7PYi39vqeftVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحریف واقعیت توسط نماینده آمریکا برای پوشش شکست تحریم‌ها و تقابل با اراده جهانی
نماینده آمریکا در شورای امنیت:
🔹
امروز باید گزارش ۹۰ روزه از وضعیت هسته‌ای ایران ارائه شود، اما دولت ایران متأسفانه دسترسی‌ها به مناطق هسته‌ای را مسدود کرده است
🔹
روسیه و چین می‌خواهند قطعنامه‌ها را نادیده بگیرند و با وتو کردن آنها از ایران دفاع کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/688757" target="_blank">📅 17:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688756">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
مخالفت قاطع روسیه و چین با تشکیل جلسه شورای امنیت درباره تحریم‌های ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/688756" target="_blank">📅 17:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688755">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
کرملین: اوضاع در منطقه خلیج فارس در حال حاضر مطلوب نیست/ طرفین خویشتن داری کنند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/688755" target="_blank">📅 17:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688754">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4fd80c3cf.mp4?token=rK4fta92g78xKlqRo9f_mUNCOCbhgIT8Nz8E6HiIZ2dxi8vAzy8kj0ab2VSqLwr6Uf-ShWlF1vgiVPfiPCE5rwuT3haNuh5USpmtznZ8FvtOR3IaneDav5Uqg-fzlkmoUg-5KFOYRwgXlqFp5gYjWDiO9A5uHah81vk-gEqtKnaEQ1PQvpNqyK_bvN3rqWTq8NipfbYDcq-TNRxJzSEMOGVtCGL5aFZRGmDW3qX760SY9xdSKeZzDTxr9kVGy9wwB8Jq3LbqqW2Hqpr4lYV6jFuQ1VrNR5FClSVE0YvpDocLTcpOguDOhKUvOcTRvMj1t5lD-JfHyLnCa8fq-ZCSCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4fd80c3cf.mp4?token=rK4fta92g78xKlqRo9f_mUNCOCbhgIT8Nz8E6HiIZ2dxi8vAzy8kj0ab2VSqLwr6Uf-ShWlF1vgiVPfiPCE5rwuT3haNuh5USpmtznZ8FvtOR3IaneDav5Uqg-fzlkmoUg-5KFOYRwgXlqFp5gYjWDiO9A5uHah81vk-gEqtKnaEQ1PQvpNqyK_bvN3rqWTq8NipfbYDcq-TNRxJzSEMOGVtCGL5aFZRGmDW3qX760SY9xdSKeZzDTxr9kVGy9wwB8Jq3LbqqW2Hqpr4lYV6jFuQ1VrNR5FClSVE0YvpDocLTcpOguDOhKUvOcTRvMj1t5lD-JfHyLnCa8fq-ZCSCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضربۀ‌ کاری انصارالله جهت افزایش تسلط بر دریای سرخ، جزیرۀ زقر هم آزاد شد  خبرگزاری‌فرانسه به‌نقل از منابع یمنی:
🔹
نیروهای مسلح یمن پس از تسلط بر المخا، جزیره راهبردی زُقر را نیز تحت کنترل گرفتند و در مسیر گسترش نفوذ در سواحل دریای سرخ هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/688754" target="_blank">📅 17:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688753">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c6fae3b6a.mp4?token=aR1ApDvjTx56nsIOyPiubjQxKuqL49mKUqWgdj_8e4Pru6nv0-EWNLN0o2zD4WUrBJq8w4xq3120aBF4QLtXHwyckCO9rvOgok3aiDM6_a5nSJYeAiD4n06aGGTE0mSapCSdgxzAqzcM-O_k85qWZw30MAhACGt6CZJx-XAXYeP-5-6MaSwzEWvKLsT3V0mGFkVDJpouCVe59PPGFeN_2ErGC2rXwTqHDXiZN3vcYmCPX1OlJUZ4mrKEEIco6XlPMfnf1DY4lkwvsT_iPLUkr00bEfUneeVIpJrJ7lfSLhSdP7FmZFgvVS276kbfXQJlqdgDwJTN8QWTZ7352GNthw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c6fae3b6a.mp4?token=aR1ApDvjTx56nsIOyPiubjQxKuqL49mKUqWgdj_8e4Pru6nv0-EWNLN0o2zD4WUrBJq8w4xq3120aBF4QLtXHwyckCO9rvOgok3aiDM6_a5nSJYeAiD4n06aGGTE0mSapCSdgxzAqzcM-O_k85qWZw30MAhACGt6CZJx-XAXYeP-5-6MaSwzEWvKLsT3V0mGFkVDJpouCVe59PPGFeN_2ErGC2rXwTqHDXiZN3vcYmCPX1OlJUZ4mrKEEIco6XlPMfnf1DY4lkwvsT_iPLUkr00bEfUneeVIpJrJ7lfSLhSdP7FmZFgvVS276kbfXQJlqdgDwJTN8QWTZ7352GNthw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیلاری کلینتون: ترامپ قهرمـان المپیک دروغ‌گویی است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/688753" target="_blank">📅 17:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688751">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R87IaCAv3x-rRTOP3F579zyiDMCEbe_E7nkGMUnbBuuimbsvcfjN7A41QZfRz2pIqDg28_wtpCEo5FwsVuimar6drmf5vWXecSDexI0DAg2lKpxC6KZrOK32vi8t33pMVHjWcWxRAZXeODlBgjkw3FbjUCxHfaiKw4jNEXXjNs_E2znQj1yeWRpngm1lmCZcF1jFIntwy5BH7glJYk-3LtA0w46PqsbFLGfXtnhj3O7kpV54EMNViSl_TO8MhXIOLRD1o-430Uq54K0ZQ1bfdX3Zs2IBegRK_zDVMGVSDSocKr2H-c-7mcusFFR232qBMPaN5HjqbskwaQ9J-xP0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فروپاشی ناگهانی در جبهه جنوب غربی یمن | نفت عربستان در تیررس تحولات ساحلی | چرا عربستان وارد عمل نشد؟
🔹
خطوط نیروهای مورد حمایت عربستان سعودی در جنوب غربی یمن طی شب گذشته و صبح امروز با سرعتی قابل توجه دچار فروپاشی شد؛ رخدادی که معادلات میدانی در امتداد ساحل دریای سرخ را وارد مرحله‌ای تازه کرده است.
گزارش تحلیلی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3244244</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/688751" target="_blank">📅 17:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688750">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
رزمندگان یمنی دو جزیره دیگر را آزاد کردند
🔹
خبرگزاری رویترز به نقل از منابعی دولت وابسته به ریاض نوشت که ارتش و انصارالله یمن بر دو جزیره «حنیش الکبری» و «حنیش الصغری» در نزدیکی باب‌المندب مسلط شده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/688750" target="_blank">📅 17:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688749">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
نفت برنت برای پنجمین‌بار امروز تغییر کرد و به ۱۰۵ دلار رسید!
🔹
بعد از خبر کاهش تولید نفت عربستان در پی حملات یمن، قیمت نفت در کمتر از یکساعت دو درصد افزایش پیدا کرد و هم‌چنان درحال افزایش قیمت است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/688749" target="_blank">📅 17:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688748">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
با دستور عارف، معاونت حقوقی و علمی رئیس‌جمهور مأمور بررسی طرح نفوذ شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/688748" target="_blank">📅 16:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688747">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2367c9e480.mp4?token=E9NuJySRHqo9EDTFR5vl5sHM9nW2PtKdONA8a6-O9ciTDjShOpNek8FU4WI_jMnmC3_wJsFONwi9MTrXfhenSRWwiEy4DWa-LlVRDxS1toKlfV5YFgMeFbpRz5XBSSBn-_sVvDebCATA3UaNE2iAfkif8BUVuaatayGUqhjmpk1KCQhWl61AEicCrrYB4wzaKS00ObUzqjpX-Nvzcz-0oxmdbtHFdGj1tadYWqGESQAvRZ-8IqG8LBmjGa4WIytuJZrIEVHrqYX-qgldSRCHgVDNz22w8aqw1uQRKtFvTe3-7U2Khv0OFexX15mDWRmaXbR_Okp0mNnbVp-aL87LAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2367c9e480.mp4?token=E9NuJySRHqo9EDTFR5vl5sHM9nW2PtKdONA8a6-O9ciTDjShOpNek8FU4WI_jMnmC3_wJsFONwi9MTrXfhenSRWwiEy4DWa-LlVRDxS1toKlfV5YFgMeFbpRz5XBSSBn-_sVvDebCATA3UaNE2iAfkif8BUVuaatayGUqhjmpk1KCQhWl61AEicCrrYB4wzaKS00ObUzqjpX-Nvzcz-0oxmdbtHFdGj1tadYWqGESQAvRZ-8IqG8LBmjGa4WIytuJZrIEVHrqYX-qgldSRCHgVDNz22w8aqw1uQRKtFvTe3-7U2Khv0OFexX15mDWRmaXbR_Okp0mNnbVp-aL87LAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غمگین‌ترین راننده قطار؛ مردی که در متروی بدون راننده چین فقط نظاره‌گر است
🔹
این خط کاملاً خودکار است، اما حضور یک کارمند در کابین توجه کاربران را جلب کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/688747" target="_blank">📅 16:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688745">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73fe73d6bf.mp4?token=INv1mQqkAAsDvsXIoxZZS6PHs1CURF2Hx7oimP2jJdtut2M86TxhYWYvoM9cPXh80Qvav1hB_mYVixv6_XNwyWmj4ustrBq-NjJYWcxvkenHt2QFj8oBzgmGADhG911-yzRpR7EBLb7DqJYlpL42_4gyNgmNwoe41_CeeeAk97Fdp9pFYw5orQIe5WQh3C78eP0MvRz2D4UsO7uCynKjuK_CrP6vh0jpVTXjOV_3V49PrsNZgIOpwvirfRhObFAdUFcjyMF0bOFUBrhGVjfHjccKKqBHGVqOBpr4jIi7tTKvi2Mii1Rk6QNNKSZ4AJNwBU9e6R4IcAs2SqIoA1lZTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73fe73d6bf.mp4?token=INv1mQqkAAsDvsXIoxZZS6PHs1CURF2Hx7oimP2jJdtut2M86TxhYWYvoM9cPXh80Qvav1hB_mYVixv6_XNwyWmj4ustrBq-NjJYWcxvkenHt2QFj8oBzgmGADhG911-yzRpR7EBLb7DqJYlpL42_4gyNgmNwoe41_CeeeAk97Fdp9pFYw5orQIe5WQh3C78eP0MvRz2D4UsO7uCynKjuK_CrP6vh0jpVTXjOV_3V49PrsNZgIOpwvirfRhObFAdUFcjyMF0bOFUBrhGVjfHjccKKqBHGVqOBpr4jIi7tTKvi2Mii1Rk6QNNKSZ4AJNwBU9e6R4IcAs2SqIoA1lZTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضربۀ‌ کاری انصارالله جهت افزایش تسلط بر دریای سرخ، جزیرۀ زقر هم آزاد شد  خبرگزاری‌فرانسه به‌نقل از منابع یمنی:
🔹
نیروهای مسلح یمن پس از تسلط بر المخا، جزیره راهبردی زُقر را نیز تحت کنترل گرفتند و در مسیر گسترش نفوذ در سواحل دریای سرخ هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/688745" target="_blank">📅 16:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688744">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ورود گردشگران خارجی به کشور، 90 درصد کاهش یافت
محمدعلی فرخ‌مهر، رئیس اتحادیه هتل‌داران تهران در
#گفتگو
با خبرفوری:
🔹
ضریب اشغال هتل‌های تهران در شرایط فعلی به‌طور میانگین حدود ۳۵ تا ۴۰ درصد است در حالی که در شرایط عادی می‌توانست به حدود ۶۵ تا ۷۰ درصد یا حتی فراتر برسد.
🔹
ورود گردشگران خارجی نسبت به گذشته کاهش قابل توجهی داشته و بدون احتساب کشورهایی مانند عراق و افغانستان، کاهش گردشگران خارجی حدود ۹۰ درصد است.
🔹
با احتساب گردشگران عراقی و افغانستانی، میزان کاهش ورود مهمانان خارجی حدود ۸۰ تا ۸۵ درصد برآورد می‌شود.
🔹
کاهش پروازهای تجاری، محدودیت رفت‌وآمد و شرایط ناشی از جنگ از عوامل اصلی کاهش حضور گردشگران خارجی و افت ضریب اشغال هتل‌ها است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/688744" target="_blank">📅 16:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688743">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfHvheihOxEGoGnuCbdviF4Rj8kQ8X2qnuDNOpRRXeS9U6tF6blHUTDGuXSEt36ck_LzD_QNyW5ayibhNt1vGoq9ePy3tLCwseC7JQtuvJFRvxKLApidqMoYy5v_v3dC0f97JaUKp1llALcICYrMnoPPKSBnIjLHC6W-ueBXltB8Nlt7SYEmbbJ5hB9o5aqpBpBrgGQNn5sz2oT3GGEr5pFfHokFtPvqzGOEaEDoJw_d5ThPNHmuEgvGM0k9kRErxQLAkKqsj_ln1e8lxZ8Ac9C24aiXYV2xNbtVypVuKftftwIxu0Bfd-jShWxwLMXUSXOwPWP2i6d-I9c8FuOR-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بشارت به مردم یمن و غزه؛ باب المندب آزاد شد
🔹
خبرهای اولیه از ورود مجاهدان یمنی به جزیره فوق استراتژیک میون در باب‌المندب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/688743" target="_blank">📅 16:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688742">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a22254fe.mp4?token=KvgX2wkLJBckhq-JgC28ZxBXHyjWGGZx8ZyY4E8rRK8MWRvdLfn-AASrVI7slbbmtzp-f_bycfSShoZIW_oba0jVSU3l79jZqtbO3D_piur0G3FPHmEg1LUgakbdyknkgR_7jPwlZVNSiqfNBzRGeOamKo0lmPoeYoj4j9zGNjy4VH74z5OVfIZIqmHOlKYzw2wv3KagVjESnKJMU8EemZswh_gU3fXJmkPxDh21BM5E7GxqFxEX5RfnglTu2BRRk3dcn3mmjlNGJKBjD0XLgRtpkGT93qG3YDVSIe-9v1WIOpVOd4kIfFlxN7B54w1N1m7VMG3M-adsY6P3t9SR9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a22254fe.mp4?token=KvgX2wkLJBckhq-JgC28ZxBXHyjWGGZx8ZyY4E8rRK8MWRvdLfn-AASrVI7slbbmtzp-f_bycfSShoZIW_oba0jVSU3l79jZqtbO3D_piur0G3FPHmEg1LUgakbdyknkgR_7jPwlZVNSiqfNBzRGeOamKo0lmPoeYoj4j9zGNjy4VH74z5OVfIZIqmHOlKYzw2wv3KagVjESnKJMU8EemZswh_gU3fXJmkPxDh21BM5E7GxqFxEX5RfnglTu2BRRk3dcn3mmjlNGJKBjD0XLgRtpkGT93qG3YDVSIe-9v1WIOpVOd4kIfFlxN7B54w1N1m7VMG3M-adsY6P3t9SR9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: به واسطه نیروی فضایی از فضا می‌توانیم نام مسئولین ایران روی اتیکت کت‌شان را بخوانیم از هزاران مایل دورتر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/688742" target="_blank">📅 16:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688741">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34fa144beb.mp4?token=nyDUqeiF9acfLqxZMBYKpfp5EtLZKT_-SlJITwHDdeUKIVppMjVByonlDmWdbU1u2HiRYphpasasRDHTN8vsW0rfph4e2Edq027IGTMZENbWQqgUjKA5ReQIqsjuaSk4biz-dsPHaKoZ4PMMSig-iDDn7pQKu2lPx3xACkVQUAlOeRZJfw9TK01Fzejqy_WDwWdHmV6HfthSFRckpIbRo6-yN-7xfBUA-Aa_TEaBB_0X-o0ROVXbboSC2oFSQL7n1hbM9yVJUYF_5iaotBfmkege4_xvNHzlEQSrH9H-T5L2tA_lKL0LgtxAEFkCR1KBT8O6rn6sOILuvPdXlzdmVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34fa144beb.mp4?token=nyDUqeiF9acfLqxZMBYKpfp5EtLZKT_-SlJITwHDdeUKIVppMjVByonlDmWdbU1u2HiRYphpasasRDHTN8vsW0rfph4e2Edq027IGTMZENbWQqgUjKA5ReQIqsjuaSk4biz-dsPHaKoZ4PMMSig-iDDn7pQKu2lPx3xACkVQUAlOeRZJfw9TK01Fzejqy_WDwWdHmV6HfthSFRckpIbRo6-yN-7xfBUA-Aa_TEaBB_0X-o0ROVXbboSC2oFSQL7n1hbM9yVJUYF_5iaotBfmkege4_xvNHzlEQSrH9H-T5L2tA_lKL0LgtxAEFkCR1KBT8O6rn6sOILuvPdXlzdmVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چشم شما تنها جایی در بدن شماست که می‌توانید خون خود را در حال جریان ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/688741" target="_blank">📅 16:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688740">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15c3a10b0.mp4?token=V_44MkOVj-Gziv1cIQknjAxHtVM3kdcq7s7kv5GzAOeaY0Yw2qrFyLkbaL4niaqkJ3ukcZSYlLYAmpXAyigMs4IKF2zmaoiXRFJmGogoNokMLNvX15TG1gSzLHdVZr2v3r8IQr-ACwlVY9JLxb9_2V62WXGNtQWO7LvzVWR5GXz8LNqj23fLcAqzH5H97tLlusOcWJR6D4cnlszJLp_VJO1w20ZRj9yVXjYQHgljK5Fu_m_aapgge7F0zQWlxxBWikZV7BllOZbXHpAsvWGg1jhK_WurWgcXvHIWoB2LW2L-3NfwnfVUMArQxtjm69eO8BUxL1icxM1HRjC-WxVPI0yNqt6VNEn26N1Y7FVbiNZKfECSeetWMZraYYLjTeA5_JOcbWb6F8nshijltGA57JpBBMs5UnwlY9bd7G_z_k5u8AnZnoMce9RHWrEmiLzTjcbe5dy85JS1P5NJMk63J-JRBboArPsAE_SujdlP40doMts16C2BhbdOMW1ZHlBnsUJAI0ze7TQqkPnp_Jd2cjcCK4CtLMDbtwANwCYWPTZVzRySAk431ZNcwYi2UNzU-WzaflzeC3Nh0KxuJPthevQLz-92GxSET9lApt-6_yuaQFUL-0UXW_CODB3J0ZWUmSLa9iXhpm2E10n7JWar5V6HWRuF4JosI0_-L_2fS6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15c3a10b0.mp4?token=V_44MkOVj-Gziv1cIQknjAxHtVM3kdcq7s7kv5GzAOeaY0Yw2qrFyLkbaL4niaqkJ3ukcZSYlLYAmpXAyigMs4IKF2zmaoiXRFJmGogoNokMLNvX15TG1gSzLHdVZr2v3r8IQr-ACwlVY9JLxb9_2V62WXGNtQWO7LvzVWR5GXz8LNqj23fLcAqzH5H97tLlusOcWJR6D4cnlszJLp_VJO1w20ZRj9yVXjYQHgljK5Fu_m_aapgge7F0zQWlxxBWikZV7BllOZbXHpAsvWGg1jhK_WurWgcXvHIWoB2LW2L-3NfwnfVUMArQxtjm69eO8BUxL1icxM1HRjC-WxVPI0yNqt6VNEn26N1Y7FVbiNZKfECSeetWMZraYYLjTeA5_JOcbWb6F8nshijltGA57JpBBMs5UnwlY9bd7G_z_k5u8AnZnoMce9RHWrEmiLzTjcbe5dy85JS1P5NJMk63J-JRBboArPsAE_SujdlP40doMts16C2BhbdOMW1ZHlBnsUJAI0ze7TQqkPnp_Jd2cjcCK4CtLMDbtwANwCYWPTZVzRySAk431ZNcwYi2UNzU-WzaflzeC3Nh0KxuJPthevQLz-92GxSET9lApt-6_yuaQFUL-0UXW_CODB3J0ZWUmSLa9iXhpm2E10n7JWar5V6HWRuF4JosI0_-L_2fS6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واقعا چه کسی جهان را اداره می‌کند؟
🔹
واقعیت این است که جهان یک دولت واحد ندارد و هیچ رییس جمهوری وجود ندارد که فرمانده همه کشورهای دنیا باشد؛ پس چه کسی دنیا را اداره می‌کند؟
🔹
در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/688740" target="_blank">📅 16:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688738">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
قیمت نفت برنت با رشد ۳.۵ درصدی، از ۱۰۴ دلار عبور کرد!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/688738" target="_blank">📅 16:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688737">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a67ef8c4.mp4?token=jeSRnYTixvCcg6jvu8hOY5m5UGdvtvctqhe2SmUbzpevNdl5TOldB_R8zpPSDE3joEEhV24ejwsOxvqT1XaoZywEXh5tlsUbdwWkQUWiwpVDFxnf3waIfcetUhExlJ2thdnrU4vgLOt2hdIuy-LQJmUcwz3nH_9cZIaeMHNSHupsxRgB--3Td9SphQjxE7xxrEmf5ceEx8WhIuGmQM4fCLtHpp8gahmdFSYziggDX4PfdPwhqh6QjOFmfsI_N4Pquuy4C5N8FilbtykK5hKVBzG6GZgSr2zvU6raG9ZeFI9XKw8m1sMoxElwTg9G7bcr14I6VzyCrw0dYdbl2VZceQ4tJmy8DBOUwJyLvWYm7sCCrZU82aI8_povYexIiFbtLMAph2W_8rynDw8g5-rrjIcqDRkkDzMJrz5og2mxgPj-0l1vZUJDp2yuD8X_EOEWy5SqqImztgV49V5x9C74nj0Fo0qkGQ_3rAwu4T_dEwyTlrjBmkWijF00NhzLgJOTQtLpIJVUIUah1f-DgdpWQmylDlG19b7oiaP8WvbY1ucKQ0aas7CvxmSwhSryAbm9q3VVugYIgiPPAijxC85W3nfOD8u8ayiVEMW34J4q7IkmWnpM1vs_t_Zgfa8gkaxTLYOcoAEBDNVQKXwjDxIX2sp5NX7vNdBIdPmNmByryxI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a67ef8c4.mp4?token=jeSRnYTixvCcg6jvu8hOY5m5UGdvtvctqhe2SmUbzpevNdl5TOldB_R8zpPSDE3joEEhV24ejwsOxvqT1XaoZywEXh5tlsUbdwWkQUWiwpVDFxnf3waIfcetUhExlJ2thdnrU4vgLOt2hdIuy-LQJmUcwz3nH_9cZIaeMHNSHupsxRgB--3Td9SphQjxE7xxrEmf5ceEx8WhIuGmQM4fCLtHpp8gahmdFSYziggDX4PfdPwhqh6QjOFmfsI_N4Pquuy4C5N8FilbtykK5hKVBzG6GZgSr2zvU6raG9ZeFI9XKw8m1sMoxElwTg9G7bcr14I6VzyCrw0dYdbl2VZceQ4tJmy8DBOUwJyLvWYm7sCCrZU82aI8_povYexIiFbtLMAph2W_8rynDw8g5-rrjIcqDRkkDzMJrz5og2mxgPj-0l1vZUJDp2yuD8X_EOEWy5SqqImztgV49V5x9C74nj0Fo0qkGQ_3rAwu4T_dEwyTlrjBmkWijF00NhzLgJOTQtLpIJVUIUah1f-DgdpWQmylDlG19b7oiaP8WvbY1ucKQ0aas7CvxmSwhSryAbm9q3VVugYIgiPPAijxC85W3nfOD8u8ayiVEMW34J4q7IkmWnpM1vs_t_Zgfa8gkaxTLYOcoAEBDNVQKXwjDxIX2sp5NX7vNdBIdPmNmByryxI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضربۀ‌ کاری انصارالله جهت افزایش تسلط بر دریای سرخ، جزیرۀ زقر هم آزاد شد  خبرگزاری‌فرانسه به‌نقل از منابع یمنی:
🔹
نیروهای مسلح یمن پس از تسلط بر المخا، جزیره راهبردی زُقر را نیز تحت کنترل گرفتند و در مسیر گسترش نفوذ در سواحل دریای سرخ هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/688737" target="_blank">📅 16:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688736">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f9275b09d.mp4?token=Kbh1l_b8aeXCbgjmy1LzhchlUSc2EUor4fl5LO2tvkHwh7zon8pSDTe-YmwXJOcfAW0Ru5CxGeUaN7PwvZ2n1V7vvFCPPgkO3E9z31HZNkqQb8ZQsj0BryCEl-mF-NWcWmz9o4Ku2Tyjk2mD-QRmOjgEgiiaglWaLV24Bm6dR5otGxqiAyrdKUZOfLzrA-hw9epv9Nv3g7WFU0Yfz6bJH8RuUz1qHw67wWnCkD2BBCRR3HST61kqU_Mg9IYdLSQrZSsTwGvOVe16oUbwF_LtJ3k14rgd5NTjJKlbzot1RFt7glw0uQ_7jByc2PxwM5CfCUrclWom2nRJ9pbfaRYY3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f9275b09d.mp4?token=Kbh1l_b8aeXCbgjmy1LzhchlUSc2EUor4fl5LO2tvkHwh7zon8pSDTe-YmwXJOcfAW0Ru5CxGeUaN7PwvZ2n1V7vvFCPPgkO3E9z31HZNkqQb8ZQsj0BryCEl-mF-NWcWmz9o4Ku2Tyjk2mD-QRmOjgEgiiaglWaLV24Bm6dR5otGxqiAyrdKUZOfLzrA-hw9epv9Nv3g7WFU0Yfz6bJH8RuUz1qHw67wWnCkD2BBCRR3HST61kqU_Mg9IYdLSQrZSsTwGvOVe16oUbwF_LtJ3k14rgd5NTjJKlbzot1RFt7glw0uQ_7jByc2PxwM5CfCUrclWom2nRJ9pbfaRYY3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر به خرید طلا علاقه داری، این چهار اشتباه رو‌ انجام نده #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/688736" target="_blank">📅 16:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688735">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
حماقت‌های ترامپ نفت برنت را در آستانه ۱۰۴ دلاری شدن رساند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/688735" target="_blank">📅 15:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688734">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIavTouox46ofe0pUwle7h22cpgKqWgWjXBrjuJY_tastwmNpl0JFeNAxgdnDeH6LOpB9wUp8YP0aJHM-vOonif49HnYwkZk_Smsc0ngRdUOjYlAxz7OSY_eip3QSCxzE_g3hLGZzzG97_KSn5kj-g46MBWm7D3naHsEvlLOOasz_5-GKrj0E7st4hB2iZBtqIw6mqtIWZxlI8Bc-qrIeuI6PFZLH_sHGQHzdp-HlJ7DO433MLt-CzL0KgjpbXOG9T6QtvUcv91MQPYIQtPRSxkJL-5kBze3n303z9tc0W10LJNhEFmuv81tjBi29TJrPSOaHwiE85S3pw2mZZuNcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خشکی‌های زمین بیشتر در اختیار کدام نوع پوشش‌ها است؟
🔹
بررسی داده‌های سازمان فائو (FAO) از توزیع پوشش سطح خشکی‌های زمین نشان می‌دهد بیابان‌ها و مناطق بایر با ۳۳ درصد و جنگل‌ها با ۳۱ درصد، بیشترین سهم را از مساحت خشکی‌های سیاره زمین به خود اختصاص داده‌اند.
🔹
همچنین مراتع و علفزارها ۲۲ درصد و اراضی کشاورزی ۱۲ درصد از این مساحت را تشکیل می‌دهند؛ در حالی که سهم شهرها و زیرساخت‌ها و همچنین پهنه‌های آبی و تالاب‌ها هرکدام تنها ۱ درصد است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/688734" target="_blank">📅 15:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688733">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ایران به ۹ جنگنده آمریکایی در اردن آسیب وارد کرد/«سی‌بی‌اس» گزارش داد در پی حمله به پایگاه موفق‌السلطی، ۹ هواپیمای نظامی آمریکا هدف قرار گرفته و آسیب دیده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/688733" target="_blank">📅 15:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688732">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEzRi_m6OqoR9KW39IsXAZTM-kkbIfZ4JVcHRfVtxBp5hfiLZF4QpniZFXPX8fNgPY1sy29_R_k0Xb7X0OlgCiKzaaYqm4wSjnNUgCa9ZZ4LGUuYtdoPq16payin2QWyKWCtG1JHckZ3cBy-3mloQmuapdvCID02rOgS7wVFMe_21Ha4ALKfccPC_hD_qtuqpEKDEVUsxCFZLj3hxtE1DGCUSJ8U_65kWku7VQwl38qkKpTYvHH7zlBemffEpHgmMeUKz2toehGXvqEBLl49XJTg2vXlcigq8bZflupBw957ruHBdm0VzMhwHX3lZfZunO19Vr740VB3-rb4-jsDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت خام برنت به ۱۰۲ دلار برای هر بشکه افزایش یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/688732" target="_blank">📅 15:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688731">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
بازار ۱۰۵ هزار میلیارد تومانی فیلترشکن در ایران
🔹
بازار فیلترشکن در ایران به بازاری بزرگ و پرهزینه تبدیل شده است. از هر چهار کاربر ایرانی، یک نفر از فیلترشکن استفاده می‌کند و از هر سه کاربر فیلترشکن، یک نفر برای آن هزینه می‌پردازد.
🔹
در طولانی‌ترین دوره قطعی اینترنت، متوسط هزینه هر گیگابایت فیلترشکن به ۳۹۰ هزار تومان رسید؛ رقمی که در اوج تقاضا حتی تا ۲ میلیون تومان برای هر گیگابایت افزایش یافت.
🔹
دیتاک، اندازه سالانه بازار فیلترشکن در ایران را حدود ۱۰۵ هزار میلیارد تومان برآورد کرده است.
🔹
رقمی که نشان می‌دهد محدودیت دسترسی به اینترنت، علاوه بر تبعات ارتباطی، به یک بازار اقتصادی قابل‌توجه نیز منجر شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/688731" target="_blank">📅 15:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688730">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26efa8e122.mp4?token=aRAqRJvlX_-gQaCZRVIKS1iYzedTyP_rkXO-i_r8l6J2flroh_x2foEtmaEGkKula-j5ZPU0jdh_6uJpfL8AKrEJ2a6EibeQl_VlNrjqjzQg5j84Y9HXAv9hQ4eMliMhCMdgME22-YwFZx7cA2uci9Z7BVZhK8bH7ZUAU6-22gkm1FYO4l5XzijyJRfOSPrX-wrZ_Il8U-ddSMP9zFUtgqMyQab3oWilmiv280w147-M1A1ubc_kAjUZpJRXANDlBwa99HSTBAJQJl5BRd_6AAzXtI7vZiBNbkXzRpOa0oYBHhuU4nkQYA948ZUuqf-72Em-5EgnPyNdwEi7qCHw0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26efa8e122.mp4?token=aRAqRJvlX_-gQaCZRVIKS1iYzedTyP_rkXO-i_r8l6J2flroh_x2foEtmaEGkKula-j5ZPU0jdh_6uJpfL8AKrEJ2a6EibeQl_VlNrjqjzQg5j84Y9HXAv9hQ4eMliMhCMdgME22-YwFZx7cA2uci9Z7BVZhK8bH7ZUAU6-22gkm1FYO4l5XzijyJRfOSPrX-wrZ_Il8U-ddSMP9zFUtgqMyQab3oWilmiv280w147-M1A1ubc_kAjUZpJRXANDlBwa99HSTBAJQJl5BRd_6AAzXtI7vZiBNbkXzRpOa0oYBHhuU4nkQYA948ZUuqf-72Em-5EgnPyNdwEi7qCHw0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتقا آیفون ۱۷ به آیفون ۱۸ پرو همین حالا در هند شروع شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/688730" target="_blank">📅 15:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688728">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
تعرفۀ مکالمه تلفن ثابت به همراه ۴۵ درصد افزایش یافت؛ از ۲۰ شهریور، سقف تعرفۀ مکالمه تلفن ثابت به همراه از ۶۲۵ به ۹۰۶ ریال افزایش می‌یابد./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/688728" target="_blank">📅 15:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688727">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd29b2165.mp4?token=SeS96P-VQcorTkacrWKTlzsGRXbGmFEJWGtXKIjP34DrJ9i2ZnYc3I49Gz1RIi0alMTLqQ0LRajEYP80A36AdzJbjVpy4M_Ti-KUWPO1U53N-sjDcL8cYjq4mxF2wIQOCyQUFT2smRM9ZPBoA35iR3H-ew8EIM7qbjFDYcpk7JhZhuTkgBUWQlyN-Csd_Y_9ef9gUjB7z5z49DN_K8lTK_KFuhri5AiS99-j1h4TYMtKOSK8oJK3srDplMD1_5TQE50NTC1WC4LlGCYFoRB08Fqo78SKOrTK3YbBiAabPXGjvkKoMpJCqPmNB_c-V5bOqRUWb6DeC97H60iOvXoRqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd29b2165.mp4?token=SeS96P-VQcorTkacrWKTlzsGRXbGmFEJWGtXKIjP34DrJ9i2ZnYc3I49Gz1RIi0alMTLqQ0LRajEYP80A36AdzJbjVpy4M_Ti-KUWPO1U53N-sjDcL8cYjq4mxF2wIQOCyQUFT2smRM9ZPBoA35iR3H-ew8EIM7qbjFDYcpk7JhZhuTkgBUWQlyN-Csd_Y_9ef9gUjB7z5z49DN_K8lTK_KFuhri5AiS99-j1h4TYMtKOSK8oJK3srDplMD1_5TQE50NTC1WC4LlGCYFoRB08Fqo78SKOrTK3YbBiAabPXGjvkKoMpJCqPmNB_c-V5bOqRUWb6DeC97H60iOvXoRqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مطمئنم نمی‌دونستی هر رنگ درب بطری آب، معنی متفاوتی داره  #حواست_هست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/688727" target="_blank">📅 15:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688726">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e0d0778d.mp4?token=SjZhhVU4PXgqRtn49BUCeDaq0tO61MCGLVNTVLP46MvIdoW2he1Zxe61d93LtO2r2BC4Eb1F5Jc1c_Py44LAKRRTEcoGPlac8MwHp9_oh9EnRezdwrbWLa6E-EMhKEmEyqylgdUsg5KDvklap7ZvQj4PJnK7GpGiMNSbGTz2v1tNVv0tUHee1IRm_LB3kRYRr9eJsU3ptnLqWb4nr4GjOvf9Drg7HXT82b_hcAqDkshHFeNZbb79vV8nsA2L2-9w54O35TBSZG6pcQKfeDZzNI09_ydQRAOm8k_LGknaqgHW-n6f_P4HgidIS1mdKiDIqxzu65WdB-OjMIZzR7365g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e0d0778d.mp4?token=SjZhhVU4PXgqRtn49BUCeDaq0tO61MCGLVNTVLP46MvIdoW2he1Zxe61d93LtO2r2BC4Eb1F5Jc1c_Py44LAKRRTEcoGPlac8MwHp9_oh9EnRezdwrbWLa6E-EMhKEmEyqylgdUsg5KDvklap7ZvQj4PJnK7GpGiMNSbGTz2v1tNVv0tUHee1IRm_LB3kRYRr9eJsU3ptnLqWb4nr4GjOvf9Drg7HXT82b_hcAqDkshHFeNZbb79vV8nsA2L2-9w54O35TBSZG6pcQKfeDZzNI09_ydQRAOm8k_LGknaqgHW-n6f_P4HgidIS1mdKiDIqxzu65WdB-OjMIZzR7365g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشای لغو عملیات ویژۀ آمریکا، در نتیجۀ حملات ایران به پایگاه مهمش در اردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/688726" target="_blank">📅 14:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688725">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7EyKpn1VV3YHyHbP2bNH04_-Y3RpPIs-Xm3D1f6lBD8zU3CUirCo3-5TGtLuwNSwNmWmKj4huftWHZ66DL-DycGLj7ULO3mg9kdA6bIxC4ZSyW2MeuCgUBVP0nZ6UYK0DYLUWIrQHURdW7i6xPvRmqyROSUq_B8qPOl3vwU_PAmo4HjViefVCM9Dm7aZ-u6JcwDclTT_QE2OVoAik-aim_3lUNH00mYlqWX_NOxRQM4nG6u3MabZdZFXMO_pNJ5Ez7rJ2o7CYobhUoX1Z2Pq_kxbE_p0xy6eOCmRgIrCgCZxKLCJkBsEWpyK3Rg5R0UbXOJH4PuBCP1MF1-Ahz6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکار یک فروند زیرسطحی هوشمند دشمن آمریکایی در تنگه هرمز   نیروی دریایی سپاه :
🔹
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/688725" target="_blank">📅 14:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688724">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
جزیره زقر بدست انصارالله یمن فتح شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/688724" target="_blank">📅 14:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688723">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb8a25e666.mp4?token=HTI2Y-2qsSUPXjIk3EuGxfIU9lDhXlmH5ABuipIoDwMXNgxinaAXAG1Sn4q39ay_hU57UeNptM7_KhbbIAwCnD83UXV18B-GchwF5j5lxlLcVPixXnNq3TJExdBejLiq3LSpTJrCW4n24Qi52ar1dq8IEdEuUpGOL0SE1scUiZ5tn6uKliEgsfwt3CEinIhbE3kfHMqzo5LHcDxbtAiVw1rdB5DXpmA3JPtBZt2j_VyKOsgWgVtVBixR03MP8w0XN_bFhuc8ZlTbu_RanYmb7xwbHuObwA8-HzT7PZiJou_iWgHC3HNPlnz3puOjek2mR9k3ZJwXVTFh8vGr8ERTGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb8a25e666.mp4?token=HTI2Y-2qsSUPXjIk3EuGxfIU9lDhXlmH5ABuipIoDwMXNgxinaAXAG1Sn4q39ay_hU57UeNptM7_KhbbIAwCnD83UXV18B-GchwF5j5lxlLcVPixXnNq3TJExdBejLiq3LSpTJrCW4n24Qi52ar1dq8IEdEuUpGOL0SE1scUiZ5tn6uKliEgsfwt3CEinIhbE3kfHMqzo5LHcDxbtAiVw1rdB5DXpmA3JPtBZt2j_VyKOsgWgVtVBixR03MP8w0XN_bFhuc8ZlTbu_RanYmb7xwbHuObwA8-HzT7PZiJou_iWgHC3HNPlnz3puOjek2mR9k3ZJwXVTFh8vGr8ERTGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حادثۀ مرگبار برای کشتی خارجی در چین
خبرگزاری شینهوا:
🔹
یک کشتی باری خارجی در حین تعمیر و نگهداری در کارخانه کشتی‌سازی در شهر چینگدائو آتش گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/688723" target="_blank">📅 14:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688722">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
جزییات تازه از موشک جدید ایران که برای حمله به ناوهای جنگی آمریکا مورد استفاده قرار گرفت
نیویورک‌پست به‌نقل از روزنامه تلگراف:
🔹
ایران برای نخستین‌بار در حمله به ناوهای آمریکا از موشک‌های مجهز به جست‌وجوگر الکترواپتیکی استفاده کرده است؛ موشک‌هایی که با دوربین و حسگر نوری هدف را ردیابی می‌کنند. سنتکام حملات را تأیید، اما اصابت به ناوهای آمریکایی را رد کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/688722" target="_blank">📅 14:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688721">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
الجزایر روابط با امارات را قطع کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/688721" target="_blank">📅 14:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688720">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsSJgtZsH2aygpdswbUWtuITIz_8PKKC9-1HFr6zB3we6kVYdYFt99vR3wl8E_-4lRzSH64qEYY5DC5MlFJPVFgrqBcFwc3ANIyg24aZ1ULTnmJdmpvpxYRe-t881Q_vT0mPabSoaIB7C7iJreIpOw4yUnZoVriYLFVoktY4DEI-IDkBYL9btt8pElNLHmQAfHNRiCU1XS70grfTxHU8Up1hJevZLN8AS8sMb7B9CsU2VQOQz3rb1PmgXxWpmYqMZ6cyJnC8yZ9VdxmYZc-ZNJPtV3jzXox0BOldOTNDl4Csta0oiOKsrfYpc24n2393nHUkptV96LgjGrEfgVypIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال استریت ژورنال، بلوف ترامپ را رسوا کرد: «کاخ سفید نگران مقاومت ایران و طولانی شدن جنگ است»
ترامپ روان‌پریش، ساعاتی پیش گفته‌بود:
🔹
«فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام خواهد شد. چون آن‌ها (ایران) دیگر نمی‌توانند دوام بیاورند».
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/688720" target="_blank">📅 14:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688719">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45cc121a87.mp4?token=rIpZVNsGP9Cc-t0rXSa8vrNeouVuQ3HyvHcqsLZnx3N4hzA0cdjpofezky74PTqxj7gQTrGYWOe1M-pf9p8PwcaBEpk7WwY-XNYeVu9Z1K1PvR8ba0ixtqJb01zpZy-7giB4iYIPhL-n_3oxZ0dYmiduChwI_8yhJD5v7lh3e_65wswbHJodZ-WqR2vAXiqabWit5ltdbX4G9nw8gndfG9Wvylwvjvyek9b3fo7Qjy4UwMLibfOSpe_qg_R_7QOhvyly4NyfU3CZGsBDr7iOATCKDHGl18Ai4lMeqeJopXuTMKVyqvGnl0j9QZeIgLaseqKpXvvb1dAhW-27_k4hTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45cc121a87.mp4?token=rIpZVNsGP9Cc-t0rXSa8vrNeouVuQ3HyvHcqsLZnx3N4hzA0cdjpofezky74PTqxj7gQTrGYWOe1M-pf9p8PwcaBEpk7WwY-XNYeVu9Z1K1PvR8ba0ixtqJb01zpZy-7giB4iYIPhL-n_3oxZ0dYmiduChwI_8yhJD5v7lh3e_65wswbHJodZ-WqR2vAXiqabWit5ltdbX4G9nw8gndfG9Wvylwvjvyek9b3fo7Qjy4UwMLibfOSpe_qg_R_7QOhvyly4NyfU3CZGsBDr7iOATCKDHGl18Ai4lMeqeJopXuTMKVyqvGnl0j9QZeIgLaseqKpXvvb1dAhW-27_k4hTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر انسان‌ها به‌جای زمین، روی سیاره‌ای دیگر زندگی می‌کردند، بدنشان چه شکلی می‌شد؟
🪐
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/688719" target="_blank">📅 14:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688718">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
فرمانده‌‌ای که با فراموشی جنگید...
🔹
همزمان با نزدیک شدن به آغاز اکران فیلم سینمایی جانشین آنونس رسمی این اثر به کارگردانی مهدی شامحمدی و تهیه‌کنندگی روح‌الله سهرابی منتشر شد.
🔹
آرمان درویش، شکیب شجره، پیام احمدی نیا، هاشمی، سارا توکلی، هادی شیخ الاسلامی، پیمان نوری ، میلاد رفاقتی ، حسین اثباتی، محمد صدیقی مهر، حسین اسماعیلی، عرفان آصفی ، رضا نوری و با حضور امیر آقایی از بازیگران این اثر هستند.
🔹
«جانشین» محصول بنیاد فرهنگی روایت فتح و تهیه‌شده در انجمن سینمای انقلاب و دفاع مقدس است و با پخش بهمن سبز روی پرده می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/688718" target="_blank">📅 14:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688717">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dATsLi6FJY7R0_8g5RHaQn8CWZdkUPk8J9Q1870Rq4TFmuMP14ax6qyrclyZ4pEnzhCXYhime2Tqr4flCejKPf5NDENxPKeI8T-JJMuLiLJ7RYr99Qrd_8NVGKcFYrF3UvH5YGuUDQqhAOCBmraRaWjDfzENmZnJPN30z_9tAnuKFcK0gb-RRouPG3UHG7Tj3QcvsV0EDNLk6giamwykBo46UHsU9zYq0RSGD7CBty02jo5FlbCevuwR6TuNfJDsgNnV2Zv4FcUX9iiXG9MCLZA7DvI_T0z1Ef1h8uCb0MOh_r2geqOEgVmSMv7QSLTeAESpYMn2MkDDABXxw0QYGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ پولپاشی کرد: اگر در انتخابات پیروزی شویم به هر بزرگسال آمریکایی ۵ هزار دلار می‌دهم
🔹
مجری فاکس نیوز: ۵۰۰۰ دلار برای هر شهروند برای هر رای؟ یعنی ۱.۳ تریلیون دلار. رئیس‌جمهور در حال رشوه دادن به رأی‌دهندگان است و کشور را ورشکسته می‌کند.
🔹
ونس: رئیس جمهور…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/688717" target="_blank">📅 14:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688715">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e68e197b46.mp4?token=g64OW-IsLL5rg88r_z0Ks_ec0uhbqWoKX7-pjSz9YXN3pkA5lwD8dj2pvUNU0_h_OC1-vWNtVVX_THlrTHXH8giufGE5HS0bLqi7c3gm_M0cAgLfAfx3LxU4hz-M8mYXVXp6wpTh3tClLe4HO6A-7DIefysFAOkfqeDBOOpvV3xraAjwcs8TePDCJOl0i9B-3U8sVcxHcwy4wFIGlsUdidiGstl0E1RMa-Ia3dP190QW36SDDYCqhjJmQgUifIZmvlbUdWu3mZmpvht1ahgQMUOF5t-i7CnNd68nHfJ6NWkW6x3S6lVRyVxoBDJ5lO89U4C6GUFonWPbstgTR9Kddw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e68e197b46.mp4?token=g64OW-IsLL5rg88r_z0Ks_ec0uhbqWoKX7-pjSz9YXN3pkA5lwD8dj2pvUNU0_h_OC1-vWNtVVX_THlrTHXH8giufGE5HS0bLqi7c3gm_M0cAgLfAfx3LxU4hz-M8mYXVXp6wpTh3tClLe4HO6A-7DIefysFAOkfqeDBOOpvV3xraAjwcs8TePDCJOl0i9B-3U8sVcxHcwy4wFIGlsUdidiGstl0E1RMa-Ia3dP190QW36SDDYCqhjJmQgUifIZmvlbUdWu3mZmpvht1ahgQMUOF5t-i7CnNd68nHfJ6NWkW6x3S6lVRyVxoBDJ5lO89U4C6GUFonWPbstgTR9Kddw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر منتشرشده از ورود نیروهای انصار الله یمن به بندر راهبردی المخا، در استان تعز و مشرف به تنگه باب المندب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/688715" target="_blank">📅 14:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688712">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vg8Vbo2RRrYlTEyNEWJYvzer2yUh28nQlKwT8Wq77Wg77w3R7JX1AnfbhP4arrQ082Uq7avgC_rkyacp-7ZZCp2RDD_T6yV0GH5jGIkgBNJNi8Al-QEtpMTrkzpFm7CfBX9_sKQn1Y7bFq-TgfEjBWWF_DBQsm_UtkCbEWUfo3tnKVxeOlvRvptd-dZCgotSowIL8b6L_jn5682MA4z3LetUPcEoDZNtA9Y9jPZQqpIEBl9TSa1DpWwcW9Yc3HRTzWqR70Dzi8ZwiNZt8AzpZsCDoP8S12slbvM4FeI4f9gTQXDD_2z7wZ_vSZi9J9vqppCyZa_accLMQyUHMrrQ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NyaOyLkdy6xoJif-XQkzw39Iz8dO0DmvvHBdu2-LrmhekkrQ7h9MvTOUfxlzWfX58sGyFCsANVPnWrdWB9P82dhvYth-42y0A-hkLPbVZha2eDWOY04kA0kzjh54o8Kco2m4qrICnLE2AhqNbPPx9RpwfDMLQqdfRvTfxhTsMZVeH-ZqgSDxJSpNmkWyZWOouG_Z-NHQhv3-7bnFzGAEUULT7AgKj0m4NzRphdowHXmzMmdlShuHIvxepF35IA3ySLF5kqcYT1xnRmkFd5wFmd_7mKVZH_aPzEl6ZGvzYyBdHWXwkCq7g_H8gRg2PF1xYOjjyFinGvJeD268qXTW0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RDX3ROJERHxeRTUahkhd7WKow8eG-J5lhCFmg4bhO86Mch9Se23-_uRPZU-UUTeCDcpB_hcqiu9d75aCMtUd0ropf2PneN8LmpvmTwwnZ9CoS8PADYH6P2MQVx6kJCLNuYP0kHQdTAv7_SEpgMS_52IQS6hlIHexKyWlE6_E8_irAjto4gaqrUmfNmSfteIdEai_7ztkMCc41m46itdeln_YKn5Z3LL5b_jHPN_c3kNd3rNSBhPKFjlQ74OQRQ1NC9_rYDts2cm1xSf5yOHCXXnWpDR7FFG98OoDw156o_OYOBE3IYtSfy8Bdid4gLfpsMXK6I6DuZclOO1fyUTQeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هزینه های میلیاردی آبدارخانه شرکت های بورس
🔹
در حالی که چند روز پیش هزینه ۱۱.۵ میلیارد تومانی آبدارخانه بورس انرژی خبرساز شد، بررسی ها نشان می دهد شرکت بورس کالا با هزینه ۹۸ میلیارد تومان رکورددار هزینه آبدارخانه برای یک سال است.
🔹
بورس تهران با هزینه ۷۸ میلیاردی و فرابورس با ۱۷ میلیارد تومان در رتبه های بعدی هستند./ تیترتجات
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/688712" target="_blank">📅 14:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688711">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
پزشکیان: ممکن است در برخی جا‌ها با کاهش سوخت‌رسانی مواجه شویم، لذا باید سوخت و تجهیزات گرمایشی جایگزین به آن مناطق برسند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/688711" target="_blank">📅 14:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688710">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c562b5ca.mp4?token=bEvsrBk-CaLeDqGabCCM4o36bJz39cKw0DBBaam1NEUfL3_xBwdpsMo6GYtlxK-W2SnfpGAI6F6VVtYuou3Fa8FcPhT7VulvPoq2fxIOMvK6k5qCQ25bimSth8f9n5fXuPpPF1GPagnhi_VemxZzQ1vEJoLHrUC82w2z7r1cHdmgvKAk-UAAx5foS6_5acB_kGpSiU-7tXDb8AOyBDZd8PzNKmxD-LR9oqw8DGloVmhU9shUzx2dpRFAwwRHsU4_vxC70cS1jtR_nEBT5T4r6TFDTOTDlv2WhpQDc-ap8Bfo80luqxZC0BbJfgOtGNLZxOdymbN7wYB3D-hXqHDGGq-XMBcPHVqJrf4yFWFEjhk8LwM1c-ANlspja8TWha9TOtokcwNsQMEOnmvt4lfCCfL-m2-Lei-nW_aKe3ec2kHPC7Er4uyZmBh34AnZ9Q1uSFcJcTmNBH_kOYYiHi4SG-K7ZYGZnFqIueNP-Yiyse4n15XI7NATXqDL8nOK7YUns1GdHIoRmtCqpVtM62tCh8EsarLvupz7z1o6QW5d6UGkVxGyGki5dbwReYNtDn82tkoEXYrCRRAfIpboALu_wn9ALFWdLaB8WtZHp1BOhW5SMD5NzY7ncoAORtoScQbM4o7aol9AxdHtQQgREr4ovMb8i1Rbn7g5lSPnptAa_QU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c562b5ca.mp4?token=bEvsrBk-CaLeDqGabCCM4o36bJz39cKw0DBBaam1NEUfL3_xBwdpsMo6GYtlxK-W2SnfpGAI6F6VVtYuou3Fa8FcPhT7VulvPoq2fxIOMvK6k5qCQ25bimSth8f9n5fXuPpPF1GPagnhi_VemxZzQ1vEJoLHrUC82w2z7r1cHdmgvKAk-UAAx5foS6_5acB_kGpSiU-7tXDb8AOyBDZd8PzNKmxD-LR9oqw8DGloVmhU9shUzx2dpRFAwwRHsU4_vxC70cS1jtR_nEBT5T4r6TFDTOTDlv2WhpQDc-ap8Bfo80luqxZC0BbJfgOtGNLZxOdymbN7wYB3D-hXqHDGGq-XMBcPHVqJrf4yFWFEjhk8LwM1c-ANlspja8TWha9TOtokcwNsQMEOnmvt4lfCCfL-m2-Lei-nW_aKe3ec2kHPC7Er4uyZmBh34AnZ9Q1uSFcJcTmNBH_kOYYiHi4SG-K7ZYGZnFqIueNP-Yiyse4n15XI7NATXqDL8nOK7YUns1GdHIoRmtCqpVtM62tCh8EsarLvupz7z1o6QW5d6UGkVxGyGki5dbwReYNtDn82tkoEXYrCRRAfIpboALu_wn9ALFWdLaB8WtZHp1BOhW5SMD5NzY7ncoAORtoScQbM4o7aol9AxdHtQQgREr4ovMb8i1Rbn7g5lSPnptAa_QU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با گلدوزی می‌تونی خیلی راحت لباسای لکه‌دارت رو کاور کنی
🪷
#فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/688710" target="_blank">📅 14:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688709">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvZXf7HxPNKjV_1tSt37ESEZJE6pMhUJmVhSFH59riGjahwkQ-L2gs6x7q2d4xtzfxRWxHp2e91jJKtYkZOTiiz5RjU3ybNmOd5HFq5ZG9rRlnRwyWt7sUljfacv9BFw0MbqQbo0msF2dB4dQH1zLJ5GK7iOgYda9BqmqFeUiieGlEf_GUNHtn3tz5xp8pXuCmOtSKtK4Bisd5hR4wr-SJxjVc940cFNAkjH9gMu0li9pCdMx62ss3QmViQ_Io5T2n8PWm1eV6LfvSkVzYiGi-gimdyQ7-xJR_x_CwhB7Hl1pcpoYU0OBuRqaY88mB2tpVM2B2Sp4rCNlN8EAPPRqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ پولپاشی کرد: اگر در انتخابات پیروزی شویم به هر بزرگسال آمریکایی ۵ هزار دلار می‌دهم
🔹
مجری فاکس نیوز: ۵۰۰۰ دلار برای هر شهروند برای هر رای؟ یعنی ۱.۳ تریلیون دلار. رئیس‌جمهور در حال رشوه دادن به رأی‌دهندگان است و کشور را ورشکسته می‌کند.
🔹
ونس: رئیس جمهور…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/688709" target="_blank">📅 14:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688708">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2db4c9cdf7.mp4?token=lwIO8N7waEfOP0rveSvzUlChQXOzziftSjCd68BXyimRIEYE2myymZ1_xYda98SfkfCsGlDSSBqMBh7oYXkPYkIGt-BdbkkToeVsdF70JGwuC96Xh-aqhAgnIcH5ZXlRWNMs7gTc1Ip2gUvLkL0eIn7VxOdLVhJnqwzR231nQRjEZWsYZbExY50p771dkyy4o0Ci4The2D0vwsxvZBcPQ8IdrApNW0XM4evMDefLkLOBtefr4leXckR8tdjk1tQj8bgIFcJ6JnpbupkwHI2rpoozqwUeOcmxkgrFq5ZLJg4MOv94zqnZzNPk6hF_o8tfi1rqRux90Fpj2aKJ5LeePA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2db4c9cdf7.mp4?token=lwIO8N7waEfOP0rveSvzUlChQXOzziftSjCd68BXyimRIEYE2myymZ1_xYda98SfkfCsGlDSSBqMBh7oYXkPYkIGt-BdbkkToeVsdF70JGwuC96Xh-aqhAgnIcH5ZXlRWNMs7gTc1Ip2gUvLkL0eIn7VxOdLVhJnqwzR231nQRjEZWsYZbExY50p771dkyy4o0Ci4The2D0vwsxvZBcPQ8IdrApNW0XM4evMDefLkLOBtefr4leXckR8tdjk1tQj8bgIFcJ6JnpbupkwHI2rpoozqwUeOcmxkgrFq5ZLJg4MOv94zqnZzNPk6hF_o8tfi1rqRux90Fpj2aKJ5LeePA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای خرید رادار پدافندی انگلیسی توسط حسن روحانی
علیزاده طباطبایی، عضو شورای‌مرکزی حزب کارگزاران:
🔹
این قرارداد را میرحسین موسوی لغو کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/688708" target="_blank">📅 13:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688707">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
وزارت‌دفاع روسیه از تصرف شهرک زاروبینکا در منطقه خارکف خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/688707" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688706">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ترس اسرائیل از پاسخ ایران؛ کاتز دوباره تهدید کرد
یسرائیل کاتز:
🔹
هرگونه حمله علیه اسرائیل، صرف‌نظر از دلیل و محل آن، با یک واکنش قوی مواجه خواهد شد که خسارات جدی به ایران وارد خواهد کرد، خساراتی که ایران تا به حال آن را تجربه نکرده است، از جمله حملات به تاسیسات انرژی حیاتی.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/688706" target="_blank">📅 13:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688705">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yrp9uyydgAxqXlSKaeBlhNXpOl6AZde8RDCVkiBVC9SO3ovDGJRNTw-bHOXAzmC2MVZd8GcV7rldLQEafeFqy-I__kUM4pYVkx_nm0B4kBPYyTUcDUqjtC5FtinAEp7f2uyZx38u-lXv29GfX402pl5VctXNSg8OUnNDC5IRdfJ1E--KOjcwwKbYaMpkdkDl_i563pQXWp7vy92UL88HLGsVH1w11iGsdFX7VMEOL7_Vz-rV9De7chpfgiKbxtXuu7pZRnsSsCbvLkValAa3YDO4C9FYZxVp-t-ofN2uPOs8IEIr83vJt4oaH79QAjVEVT6ju3UcYn7xt2zZnOMIWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزیره زقر بدست انصارالله یمن فتح شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/688705" target="_blank">📅 13:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688704">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7ff24cc3.mp4?token=ZfM1RYDLMPu3db1k_MbGZg5EHfrccQs8NhRT82Q7tLqzTSNsDZ6uBoNPAAGDGzBoUjLrh20G_0g7JS0wOfq_vPbJepNCNUuXMG011XshcqUPpsdmqxHxVnpYr7Ai2M8utOFw4Mx7cYfxXJ1pWiVyLXVcBiMAmmjxuwkpomanfPktgH5WSUm705PRDcT4BcWUdgBp8L-symBF9KPI3Mr3RloPEvl-kf-85tAmIXLT8TlziK9RwogUGa2p_O0s2Iq3I3VV5d2Zppsoop3yY2yukAZm0ktCfphlLkwDc1-cHm3MdZTOD5VGxKw35oY54kQcDC1HGMR_nEQ_P91YZuspcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7ff24cc3.mp4?token=ZfM1RYDLMPu3db1k_MbGZg5EHfrccQs8NhRT82Q7tLqzTSNsDZ6uBoNPAAGDGzBoUjLrh20G_0g7JS0wOfq_vPbJepNCNUuXMG011XshcqUPpsdmqxHxVnpYr7Ai2M8utOFw4Mx7cYfxXJ1pWiVyLXVcBiMAmmjxuwkpomanfPktgH5WSUm705PRDcT4BcWUdgBp8L-symBF9KPI3Mr3RloPEvl-kf-85tAmIXLT8TlziK9RwogUGa2p_O0s2Iq3I3VV5d2Zppsoop3yY2yukAZm0ktCfphlLkwDc1-cHm3MdZTOD5VGxKw35oY54kQcDC1HGMR_nEQ_P91YZuspcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ریما رامین‌فر و پسرش روی فرش قرمز جشنواره فیلم ونیز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/688704" target="_blank">📅 13:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688703">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGgYxjTDqLsxQn9nyl_Js_5vJzCorjBFVSWFC3_CQA_oHwAc3qY-3aEOxsAJqVo9pd9pvuJjIKGSBmXfIJHduB0N7mf6flLEgunuUgSDymwSp-5BXw3er3RKk6y67AMwP-XICFameurvgLEGZPBqeInndzrZy-g-EXuSfvY11_Pdhq71-tOWK1rkVY8Z0gB1tQ5lySd1IGuOtmbaKW1bt0IfKqCYESV5HRN0V_r-EO07MDLV5-vweualOWpNunekk8McynQW0-479dZCjbMoowAp60vMsl0vLlEIt7RHIMmX98KrGB9C46pOahLHlq6QtjHJfLex6YnFx5Uk9pynFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت خام برنت به ۱۰۲ دلار برای هر بشکه افزایش یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/688703" target="_blank">📅 13:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688702">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ارتش لبنان: نیروهای اشغالگر اسرائیلی به توافق چارچوب پایبند نبوده‌اند و از زمان امضای آن تقریبا ۷۷۰۰ بار این توافق را نقض کرده‌اند و همزمان حملات، تخریب‌ها و بمب‌گذاری‌ها ادامه داشته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/688702" target="_blank">📅 13:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688701">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkpQ1qtW_BnyBLiOU9jdtJoPxtcPfOywjfvCh1lbsXsvsf00s_QfCzhIDaeLSNnIL01oWmykzebLeUOHmoKe6hX687mCryXkofdEB3f5pZAlhb-OyDVZhSqdKAlZUG74-dd6h6sF77MgH2tbHGv4igHztbaRhn-nXqKkQX9Batc-YX1KhyrxLo2a7MuzV5w-eFYLcROrxNrpW4mhWFMgRRJ3qlsr1oFMKko1lhsHyiGqMvgJIF6c1MbDnq4XrorqhBMIK10mI4AyFJ68aVAaj5BhKCFrtXcxXfnG7eARk2bQEoWIM0MK9u2uHPdWdI-GvXqv8KdAvsrZD5boUybi9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دادستان سابق‌فدرال در واکنش به خسارات وارد شده به پایگاه‌های آمریکا در منطقه:
ترامپ و هگست شش‌ماه است به ما می‌گویند که ارتش ایران کاملاً نابود شده و همه نیروهایش در غارها پنهان شده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/688701" target="_blank">📅 13:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688700">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
به گزارش رسانه‌‌های نروژ، نخست‌ وزیر نروژ فاش کرد که هواپیمای حامل زلنسکی، رئیس‌‌جمهور اوکراین، هنگام خروج از مولداوی به مقصد اسلو، پایتخت نروژ، تقریباً مورد اصابت یک موشک قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/688700" target="_blank">📅 13:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688699">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26d845f0b3.mp4?token=pVrNQm1XTX8CyWqfeo5KbFyPH61mlI9Ouq5UlyB16TpsfDY8e48Iedb3OMfn5nRZIbyyZZLqasnIjHwazdVXsMB5vYv94WpQSWroHplyismkLn_ACB3G3TFYQTIYht-EFLYeO6k9SIC4SRiCF473bX8yoTpAOCALnOl98Gzw__GJMhpPWFlN3cbvkjyYRKoNKpNSgP7H8HsvYPOwl8xXUQIWOv2k2lT4_s7QMBPowDc_FaqLLzCUELGyVAY_ci3cFerTf6QXcMmHDNAfitVspBWFrKx_vPrUlLYtter4BzBp77YX6PH9_4h_jRtwKOV1FhmRrRfQPCPULkyhCCYc3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26d845f0b3.mp4?token=pVrNQm1XTX8CyWqfeo5KbFyPH61mlI9Ouq5UlyB16TpsfDY8e48Iedb3OMfn5nRZIbyyZZLqasnIjHwazdVXsMB5vYv94WpQSWroHplyismkLn_ACB3G3TFYQTIYht-EFLYeO6k9SIC4SRiCF473bX8yoTpAOCALnOl98Gzw__GJMhpPWFlN3cbvkjyYRKoNKpNSgP7H8HsvYPOwl8xXUQIWOv2k2lT4_s7QMBPowDc_FaqLLzCUELGyVAY_ci3cFerTf6QXcMmHDNAfitVspBWFrKx_vPrUlLYtter4BzBp77YX6PH9_4h_jRtwKOV1FhmRrRfQPCPULkyhCCYc3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوشحالی نیروهای انصارالله پس از پیروزی در شهر حیس در جبهه الحدیده
🔹
نیروهای مسلح یمن در ادامه پیشروی‌های خود در جبهه ساحل غربی، موفق شدند کنترل کامل سواحل شهر راهبردی «المخا» را به دست بگیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/688699" target="_blank">📅 13:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688697">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUr7BmjCSJKgQhM_lIN7XxTK3fPxI37WzI0VWlcnfHU5xfuW30uzuwpAgio_EtGZUcogerhW_Mar5EwMif-a9m8tI3JtGEojtPO4CgM8evbOxxJlI3kYK_y8FVdxWUR0tdVpBTSgAR-VGNyKYhpMUTPInCHpKgVqgMSqvu5F1cKxX8E_wzzOkz0cDT1j139IiVMZqz0y7YygUP3gYE0JMS4ZLj3wfmRU6WfooKioPGSCoC15i6C1uoNrTt0iiXGCoyk_hgW4-grt5SJkbR3sDyo0Q7o_KXZD3deHqzcYmeLgDGY-4DqdNMXv-fILD6sHcrhSqQH9KmqPt8L0IVXZQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۹ شهریور ۱۴۰۵؛ ساعت ۱۳:۱۰
🔹
بازار طلا و سکه امروز پنجشنبه ۱۹ شهریور در مدار صعودی قرار گرفت.
🔹
تشدید تنش‌های سیاسی و پیشروی نرخ دلار نیروی محرکه اصلی بازار داخلی بودند، اما افت بهای اونس جهانی مانع از جهش شدید شد و شیب رشد قیمت‌ها را کند کرد.
🔹
این واگرایی میان دلار و اونس، طلا و سکه را وادار کرد تا با احتیاط بیشتری به روند افزایشی خود ادامه دهند./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/688697" target="_blank">📅 13:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688696">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
اعتراف رسانه نظامی آمریکا: ایران به هواپیماهای آمریکایی A-۱۰ و F-۱۵ در اردن آسیب رساند
/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/688696" target="_blank">📅 13:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688695">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b0fcb209.mp4?token=bu6T0LLD4COmxK5rcNE9cW9SfDeiinIw1uUTshUY7SzteOtO-Jk_wlrqimHEa7SCVn7kqdDa7BOXM4nwH0poyYTPytwWcMnEQ6xbWzxAKkrSF9-gtqLtM3UmFmAoVaoHl0RO1y7X7McBHmfDYYfPynu3MmkdC2U914z8uLWE6hTaRAmLS4ZqWOP6QDZ7SDQXLAF6Vp66HAcxPSGJRrI5idRJM1mcQGma3LKfmkN-7jPQy5-ZTwqtMNCNorTmWzlgbEk83PgCIuFNALR6GcPFBmD_XkqqSsCibOBGNiW_-2iABG5NyFTpETUOa_90gSJQiFxAsC-dL6ZdAV7jyTNQAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b0fcb209.mp4?token=bu6T0LLD4COmxK5rcNE9cW9SfDeiinIw1uUTshUY7SzteOtO-Jk_wlrqimHEa7SCVn7kqdDa7BOXM4nwH0poyYTPytwWcMnEQ6xbWzxAKkrSF9-gtqLtM3UmFmAoVaoHl0RO1y7X7McBHmfDYYfPynu3MmkdC2U914z8uLWE6hTaRAmLS4ZqWOP6QDZ7SDQXLAF6Vp66HAcxPSGJRrI5idRJM1mcQGma3LKfmkN-7jPQy5-ZTwqtMNCNorTmWzlgbEk83PgCIuFNALR6GcPFBmD_XkqqSsCibOBGNiW_-2iABG5NyFTpETUOa_90gSJQiFxAsC-dL6ZdAV7jyTNQAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مامان‌ باباها درک همین چهارنکته باعث میشه فرزندانتون ازدواج‌های سالم‌تری داشته باشن #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/688695" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688692">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FjgDo_TZzfxtXn47gMatO3nnpDteB2PD-4SJsEBOW0GdbsYsEh1dmNu5UhjbppY2PVwZsa97hcziHxgSbLynNiKiTNB3xLupPDUI6AJp-qyckdXz2el6sq4SP0e5_RiQH0_tQBhLuDWeyvzg534V_duO54rg9aPu3woHZofSNYq3p_CHIPoIFrn5DmVIdYw1kJVEJM6VwB1gAG4M29lZ8folDTnheER38RctwGtypOvNj_lQuU9IrHHbUL7GOQ5J8YOa9ho8bC3AY9kPvJDv1scYb0FiMo9r-Cr7AdaPQvY20a4njIz1KxDU-tMqUHvDqF-jJ8xsrf1kXFJu9DN2kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQKqG9ESbakBSwFciUktfawZ2RwDGCIlf7qYSAvRWNezwl6LwZx2nZc2Ew_FULAluyNid45uhgIfsQ0aZqr880yuU-FwbTbqIIKgyeq4CBZwJXIF2xSd29crMTaa7SXstTnKNWRSY0kRzHfwLJWdqbXAUsjAzV3hiGcslY6vk66rCy17IJXP193qk82unsh-c9JvMt2dM49btPi36DavqEUhMnk7RWZOrEfwopXfEBVMPvf_smzUvSwbgGZ-b7ZQFfhXzATDTJqJMf5AVj3LIDH0hEHlK2yCc8RDPCtAnrFOJwG8gy244Mr849qlVxq0NoTfgbv49PTmfbaftVs2iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4NB-q6-CNCsYqAJebsssEZoFneLjR9Dm_jybK6Y1NslMiuWcHqj7G5J6WV6H31RDJCF0occzB4aS_lQNFBp1F4OtM7QJ53XriW8His5E-dzFIuUMMrnRQT7WdD-2tIKvv3qK2mzwEhuot84Gu0N5kVfq4U-thxJSWAU9UaV4ZOgIMXUW7_xj_Y1qYewJ_7DANMTTrZaA-_WWZ6ZxPmwsM2g8JSe2bBiBSpCpVBxm-rVR0HIr6noDHPamWdXCnA3A5m0B1mSOeJr83T2asRSSOQlhRuErPDMIdgBJ7V7r6j9IPlW6rertIY2bFpVIf-1qP1ESeRwa5z0iKHKP0J6dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قالیچه‌های زیبای ایرانی زینت‌بخش خانه‌ها حتی خانه‌های دوره ویکتوریای انگلستان؛ خانه موزه سامبورن، لندن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/688692" target="_blank">📅 13:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688691">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
رویترز: پاکستان و ترکیه تصمیم گرفتند نیروهای خود را به یمن نفرستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/688691" target="_blank">📅 13:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688690">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cep6vS0nwghiF3mLdrYwM-41da1I0SJJDVLkNOxQnqmvD17GARc8t_urjcaAvjBTxVIfgmOLLiHPr8PqCuBMeM0mJNKVl3QtZkq5h4Ru9sZl_woD3SXx6ohf8dpQgn2Ec8KCR29lYuQVR3xt833rF402UMR_mpOzn9Rbl16oSUsnx9olq6PuFRB861RHqJFaynea7BcWMZvPfYAUA8M0cX8mQwuALfN2in67kZFLxgcU8FmzV0m1TB_7SFlc2IICRaKAST-8jWRYURx7ffj4e46bocsERE_PlHjKrVAZBKi_hU0db9Hfhc-zwYlVs6-QDirVhwGrc5OUPiZO_t3e2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
قاب ماندگار ۷ دهه اعتماد مشتریان/ رونمایی از تمبر یادبود ۷۵ سالگی بانک صادرات ایران
🔵
بانک صادرات ایران به پاس ۷۵ سال حضور متمادی در عرصه‌های اقتصادی و روایت نمادین اعتماد تاریخی و ماندگار اقشار مختلف جامعه، از تمبر آغاز ۷۵ اُمین سال فعالیت خود رونمایی کرد
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#اخبار_سایت
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/688690" target="_blank">📅 13:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688689">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
هشدار تب کریمه کنگو/ رئیس مرکز بهداشت یزد : با شناسایی ۷ مورد قطعی ابتلا به تب کریمه کنگو و فوت یک بیمار بر اثر این بیماری، شهروندان گوشت مورد نیاز خود را از مراکز مجاز تهیه کنند و از کشتار خارج از کشتارگاه خودداری کنند.
🇮🇷
✊
@
AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/688689" target="_blank">📅 12:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688688">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
بلومبرگ به‌نقل از منبع ایرانی: ایران تا زمانی که اطمینان پیدا نکنند آمریکا در آینده برای حمله مجدد بیش از حد محتاط خواهد بود، جنگ را ادامه می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/688688" target="_blank">📅 12:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cc7TzW0yitL34XI9WR3HKgWzit1JGY5yB1N7njdPtJL0FavGUAjQLeb4Gwgz_rtAv9UDOM5qh9bNu8LStHVNAX8Tpjkc_-If2jOsFeU7wgeQ1o6emcCLBWLJxNqiTIcEmU8kGJtYmDc887Vibn4N2mfrgZhwqT-n1HOQfZTedb2u2vw5TbheWlQOBtnDescfApfLds_DaQx_-FE5sKtgmorxunO3Oo9LeH2CfsymWlSrY0PGzHs-k1z_kaZoDbyBM1JlazoRsuBlmkDnrYMBAjdQE534oPcfSOlDJ8pRxbA-mqp5sKw-kWFqAxjuDE_oj6T66nQoT9YNVlSY1CH3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDeovFYpjnwTFearAWUz5de8a3JgqU6UNZ8_U8YQEX92bKk93qjdtv2Dsxtg_jttJV0WS708fnkOyLS9ngqGYG8MBtJLAYhsuROLDbiROGpWeeQXHDdc9SKGNX4w6kuC2xEIWmjdIiEPl6vAJDX6U5zo_CnBSIKmPb5Zme5CFHF9rGlGvBI69xkTvHI-Khm20eJs5UsPwIG-W6Neq7E2cVggyglXTqOTLes-4WIErfoSj8F66FJuCi8hfcLLCZDoCIKU_IgDE5rvAHuLMqeiH3Ed6BBZ6bI_fKUJSKoup-WGfDRG-g5G68XS8BqvC-nO0yNEXmM69oQpcsxYSXDKwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ادامه اعلام قطره‌چکانی تلفات آمریکا
🔹
آمار رسمی پنتاگون شمار نظامیان مجروح آمریکایی در جنگ با ایران را از ۷۵۸ به ۸۲۱ نفر افزایش داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/688686" target="_blank">📅 12:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688685">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
افزایش هزینه وام مسکن همزمان با رشد بورس
🔹
قیمت اوراق «تسه ۱۴۰۵» ۱۲٪ رشد کرد و هزینه دریافت وام ۲.۴ میلیاردی به حدود ۴۷۰ میلیون تومان رسید.
🔹
«تسه» مخفف اوراق تسهیلات مسکن است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/688685" target="_blank">📅 12:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688684">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cygX1DAQ56bhWvX0DmHgFW2Pq9CFUAwITWfWm6u59nkIdzyXP5ecwqBRcx5zQeUXDOOj9Nl_DwFnnGM4aalKIruKno6AkLTNLVlL3rj7GhqKUTrS1_GsC7GAY-bkZeB5QxoQ7eD1jlVntRsu1QIiyMZYo6lgDXFvAOxS-SqD11wDjVrJeAYw_HUrSCiMOa666tFpQ3Gi-AXoKy8HQ6FIX84DekJaHso-fQaMuB8YDB-HADXE1QE6inNfG4jpbDnN2rT5_UhWYSwPl4mAF_n0J1Es55U1pEUjYuHFtyhvvj2qVTWm3G5Pc-s5i9o9B70UfxAHRuCkxHMkd-9nSo8Wxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دکتر شایان: بنگاه‌سازی رویکرد اصلی بانک صنعت و معدن در حمایت از تولید است
دکتر محمود شایان، مدیرعامل بانک صنعت و معدن:
🔹
مأموریت بانک صرفاً تأمین مالی نیست و بنگاه‌سازی رویکرد اصلی بانک در حمایت از تولید است.
🔹
از سال ۱۳۹۱ تا پایان ۱۴۰۴، یک‌هزار و ۶۶۶ طرح تأمین مالی‌شده توسط بانک صنعت و معدن به بهره‌برداری رسیده است.
🔹
برای اجرای این طرح‌ها ۸ هزار و ۵۳۸ میلیون یورو منابع ارزی و ۱۶۲ هزار و ۷۴۵ میلیارد ریال منابع ریالی پرداخت شده است.
🔹
این طرح‌ها با ایجاد ۸۲ هزار و ۳۵۳ فرصت شغلی، به شکل‌گیری ظرفیت‌های جدید تولیدی، توسعه خطوط تولید و ایجاد فعالیت‌های اقتصادی جدید منجر شده‌اند.
🔹
همچنین تا پایان اسفند ۱۴۰۴، ۱۶۷ طرح با مشارکت و تأمین مالی بانک در حال احداث بوده که ظرفیت ایجاد ۱۸ هزار و ۸۰۱ فرصت شغلی را دارند.
🔹
در مجموع، یک‌هزار و ۸۳۳ طرح بهره‌برداری‌شده و در حال احداث با تأمین مالی بیش از ۱۳.۲ میلیارد یورو منابع ارزی و ۲۹۴ هزار و ۹۱۸ میلیارد ریال منابع ریالی، ظرفیت ایجاد بیش از ۱۰۱ هزار فرصت شغلی را فراهم کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/688684" target="_blank">📅 12:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688682">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار کرمان(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68c0c8a3ff.mp4?token=aZVeCPZdAliGg9UieftgRCULfn10TT2LvObyz1DSAqvJ01db72r-OwvqIg6TLoJG74NQ745Z9doVEmoEgZ4-IHmCkGQIZZ6-4Q-lh6P62WHfpN6-BUrCpvfGOfo2Xmpx37gjBh7D28bgWzXOrrm8H0-eKBZyPC2uLrlAcc7dxOh49TgRxboOaLBmei0EUwgOFDGXLmmWvsB7pf8cZagjS7w1Y2sCBVzXRUJ3u2Klm06wjvg8XXZK-hEUbSZFxvAHMKXLLXJZDRVHyhaie76prggihdexjbacBTLplNd9eLNX-N-Cd8eijxaXyZ3EuVFJ95h7vZUh1fHeh28PZaUTHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68c0c8a3ff.mp4?token=aZVeCPZdAliGg9UieftgRCULfn10TT2LvObyz1DSAqvJ01db72r-OwvqIg6TLoJG74NQ745Z9doVEmoEgZ4-IHmCkGQIZZ6-4Q-lh6P62WHfpN6-BUrCpvfGOfo2Xmpx37gjBh7D28bgWzXOrrm8H0-eKBZyPC2uLrlAcc7dxOh49TgRxboOaLBmei0EUwgOFDGXLmmWvsB7pf8cZagjS7w1Y2sCBVzXRUJ3u2Klm06wjvg8XXZK-hEUbSZFxvAHMKXLLXJZDRVHyhaie76prggihdexjbacBTLplNd9eLNX-N-Cd8eijxaXyZ3EuVFJ95h7vZUh1fHeh28PZaUTHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«از عجایب کرمون؛ ممکنه وسط تابستون شاهد بارش برف و تگرگ باشی!
❄️
🌨️
»
🔹
بارش تگرگ جیرفت سربیژن
@kerman_news</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/688682" target="_blank">📅 12:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688681">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f166173e8c.mp4?token=muyAvbv7tZsc6q9EQHXXJNrQdD-6Gi56igoIPOa7gGn9XvVv3QxARgDnF7xKevfD29sWJl3aQCTz3lm71NamkY8e53HATnKAgF6829jzfsUsuHEsgrMFtvR0LdnuYfR0mCtAC0wgFPcjE0NyxPDinJ0MpB_V35r7Z2TCFj87xA5vdu6cQvH0gqY0bOe6W3EAEn6Ne9_hrWOHbeTMpYf-D5vJKFK8tB4WS_KxGsNAOekhObtXx7qJ_liOQC-y0bnKvDUzfHUfvssbID-YaOPohGMz1j1xvecVvpFszQKoVPmmn04Sziopq95ji21G_PgA5NUo0EEJBx10asrKtQe3yqXlDgHrSJBTJHcB9ns4o78l1dbUkA5td-1cl6XUIu_3XXEwtK8ElN-_PgKDm8n9bLdYr8oJpxf4WnhryMge9g53YCjVu2rgLXNoKdA8LmkEobKJYNOjbP5jIGXff5wKGX1C74_sEsa7ngI6VOzQicxlY3sUNRY3a_M8RLWGCF9JUuB7Rw55CZEwSZAXD39oDLRElMXwEhD0b6aIvtD6a2wEqghC42pbRa4XwtPRc60moynrzEk0o_QqjEhneUT8Rufb-PavUQueO-KLVhJZn5d0OqZ9WKpkkShtvenD1uv4hAmEmank187D8wcHXq2ITvoUgxZjKEIcnKtKExTmy8E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f166173e8c.mp4?token=muyAvbv7tZsc6q9EQHXXJNrQdD-6Gi56igoIPOa7gGn9XvVv3QxARgDnF7xKevfD29sWJl3aQCTz3lm71NamkY8e53HATnKAgF6829jzfsUsuHEsgrMFtvR0LdnuYfR0mCtAC0wgFPcjE0NyxPDinJ0MpB_V35r7Z2TCFj87xA5vdu6cQvH0gqY0bOe6W3EAEn6Ne9_hrWOHbeTMpYf-D5vJKFK8tB4WS_KxGsNAOekhObtXx7qJ_liOQC-y0bnKvDUzfHUfvssbID-YaOPohGMz1j1xvecVvpFszQKoVPmmn04Sziopq95ji21G_PgA5NUo0EEJBx10asrKtQe3yqXlDgHrSJBTJHcB9ns4o78l1dbUkA5td-1cl6XUIu_3XXEwtK8ElN-_PgKDm8n9bLdYr8oJpxf4WnhryMge9g53YCjVu2rgLXNoKdA8LmkEobKJYNOjbP5jIGXff5wKGX1C74_sEsa7ngI6VOzQicxlY3sUNRY3a_M8RLWGCF9JUuB7Rw55CZEwSZAXD39oDLRElMXwEhD0b6aIvtD6a2wEqghC42pbRa4XwtPRc60moynrzEk0o_QqjEhneUT8Rufb-PavUQueO-KLVhJZn5d0OqZ9WKpkkShtvenD1uv4hAmEmank187D8wcHXq2ITvoUgxZjKEIcnKtKExTmy8E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از امتحان کردن این ذرت مکزیکی دیگه از بیرون نمی‌خری
🌽
مواد لازم:
🔹
بلال
🔹
کره ۵۰ گرم
🔹
پنیر گودا ۳ ورق
🔹
پنیر پارمسان
🔹
نمک، فلفل، آویشن
🔹
شیر یک استکان
🔹
سیر ۳ حبه #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/688681" target="_blank">📅 12:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688680">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
هشدار پلیس فتا درباره VPN ها؛ اطلاعات کاربران در معرض دسترسی است
معاون فرهنگی و اجتماعی پلیس‌فتا فراجا:
🔹
نمی‌توان هیچ فیلترشکنی را به‌طور مطلق امن دانست و اطلاعات و داده‌های کاربران در زمان استفاده از این ابزارها می‌تواند در معرض دسترسی قرار گیرد؛ از این رو کاربران باید از VPNهای ناشناخته و غیرضروری پرهیز کنند./ سیتنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/688680" target="_blank">📅 12:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688679">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
رئیس قوه قضائیه: دو وزیر محکوم در دولت سیزدهم ترک فعل نکرده بودند، بلکه مرتکب جرم شده بودند/ وزیر کشاورزی دولت مذکور در دو پرونده متفاوت، مجرم شناخته شده بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/688679" target="_blank">📅 12:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688678">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqs8QNYf06bCYaTCVojzllia16Weg223EFv4gFVbwXu_7Bb_NBvAE9-QIzczDhINNlhbGZN6HAw0nrgRGQijFycRu4rGAy7WL6UDtBnz7u0tnK6FNBQk4ElFylVzt4Wz3KU2L0UPnVlzjhH8jfCnOIfTK4uK3ERaZxCnrKaPe0ww3bRlIvuG4Mweder-h1ao0XOHlInviBXum8jK5Shj4jQnW8Q4-MYAhTHYPqibY3RWiYzf3yxr0EHf7S62kx92e0NRkBkj7Jwy4rfE5sfv30Zw168soa-W_SgOQwrqUNC2dvPE3Dy8muEPxiXooj-98Pz5SmXTdpODCzPAOPlUCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصلاح تعرفه‌های ارتباطی شرکت مخابرات ایران از ۲۰ شهریور
🔹
شرکت مخابرات ایران در اطلاعیه‌ای در سامانه کدال از افزایش ۴۵ درصدی تعرفه برخی خدمات ارتباطی از ۲۰ شهریور ۱۴۰۵ خبر داد.
🔹
بر اساس ابلاغ وزارت صنعت، معدن و تجارت، تعرفه مکالمه تلفن ثابت با تلفن همراه، تماس‌های همراه با همراه و پیامک تلفن همراه تعدیل می‌شود. در همین راستا، سقف تعرفه تماس تلفن ثابت با اپراتورهای همراه از ۶۲۵ ریال به ۹۰۶ ریال افزایش خواهد یافت.
🔹
مخابرات اعلام کرده آثار مالی و درآمدی این افزایش تعرفه هنوز مشخص نیست و متناسب با میزان تحقق، در گزارش‌های مالی دوره‌ای شرکت منتشر خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/688678" target="_blank">📅 12:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688677">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6de943b0e.mp4?token=h7iRKB62_ZonXTxGCQ6nj30gbFjeLUjM7Zw6B7CFnBwaR5YLzumuhUP52vuKIu9qiN-rtcC4RiC2HfxFKLMZb63NDA4v1w5jm7iV9q3DZuUyg1H_900t6_sbPVDAIZrKqrCuFG1woHhsbvlF6s4kz12KvPqO_WN4ah903hCEIXOM19fjumoLhAIXj-byej07fEwdJLBFqFftIhpnD3cn6tVNW5w4nWAe03j2AanSvecXeivNnBWawOIKUWOF3XhHyA6TAzyfFp0woJV0v90jAD6hYuQFw6swONWFfdzIxd6bMvK5AyRtR1_YBGd_idGnpQUBIeJtrRlDgebXXFhLHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6de943b0e.mp4?token=h7iRKB62_ZonXTxGCQ6nj30gbFjeLUjM7Zw6B7CFnBwaR5YLzumuhUP52vuKIu9qiN-rtcC4RiC2HfxFKLMZb63NDA4v1w5jm7iV9q3DZuUyg1H_900t6_sbPVDAIZrKqrCuFG1woHhsbvlF6s4kz12KvPqO_WN4ah903hCEIXOM19fjumoLhAIXj-byej07fEwdJLBFqFftIhpnD3cn6tVNW5w4nWAe03j2AanSvecXeivNnBWawOIKUWOF3XhHyA6TAzyfFp0woJV0v90jAD6hYuQFw6swONWFfdzIxd6bMvK5AyRtR1_YBGd_idGnpQUBIeJtrRlDgebXXFhLHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غول ۲۵ متری خیابان‌های زوریخ؛ نسل تازه اتوبوس‌های برقی در راه است
5️⃣
4️⃣
3️⃣
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/688677" target="_blank">📅 12:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688676">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
وزیر دفاع یمن ترور شد
🔹
منابع یمنی می‌گویند محمد العاطفی، وزیر دفاع دولت نجات ملی، همراه با شماری از فرماندهان انصارالله در حمله هوایی به غرب تعز ترور شد.
🔹
انصارالله هنوز این خبر را تأیید یا تکذیب نکرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/688676" target="_blank">📅 12:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688675">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3nw-BlOoeAn27U24kN1qCNELAMQNxPPk2Q4LuilCWHrGLzxg37ZRazA9MWgTOoXBxjoa8v40eJL-rgeeQuBI9bT2SpSxMwK2NUAnFOraO4X7bzr5iVg5BpSnnKRB8UlkthV14DwA__l6DlfcqYexmvAYpS_zBc1Kir2vj1b6rDLLcd0BAbqhzFowf1gC12qokbJTx-g9dVuuQl5yKqxaV5Jw-3fWOfyK307DXEhcOxllcNqvTd-2ri1I_dbcqPanHWuJpCuowacNa_daCf6e0Oz6_bIow35j1FeFLCqlY6qDqOEyvTHo1xR5HM71rR3-9iKAwo2_ZGLTiTGzeT09w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
همیـن الان یه قدم به سمت رویاهات بردار
🏡
ویلا |
🌳
زمین |
🏠
ملک
📍
چمستان | آمل | نور | نوشهر
فایل‌های منتخب برای خرید، سکونت و سرمایه‌گذاری در مازندران
👌
اگر دنبال یک ملک مناسب در این مناطق هستی، حتماً کانال رو ببین
👇
🔔
https://t.me/parsia_villa
⛪
کارشناس فروش المیـرامرادی
09196674154
09196674154</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/688675" target="_blank">📅 12:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688674">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نگو که نمیدونستی
😮
😮
جشنواره پایان فصل امرداد از این هفته شروع میشه
😍
💫
۲ هفته کلاس زبان آنلاین رایگان از هر کجا که هستی
😇
امتحانش که ضرر نداره؛ کیفیت کلاس رو ببین و بعد تصمیم بگیر
🎯
🫵
ظرفیت فقط ۱۰۰ نفر
🌸
برای رزو این دو هفته کلیک کن
👇
👇
https://amordadflc.com/home/sitepage/4860
☎️
02128429272
🌐
amordadflc.com
🆔
@amordadflc_admin</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/688674" target="_blank">📅 12:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688673">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
آیا پاییز و زمستان قطعی برق خواهیم داشت؟  وزیر نیرو:
🔹
از الان نمی‌شود پیش‌بینی کرد اما تلاش ما این است که پاییز و زمستان آسان‌تری داشته باشیم./ باشگاه‌خبرنگاران‌جوان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/688673" target="_blank">📅 11:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688672">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkgZnWfO0G8kzdea_jBI3xNAhnjUHC5NzcMXUWW_vcMW27oQLo4bj2QPtrp6fJhZrlKJhhk73i0m3bU0TQXt2uwqyzHLgMh8LWO9c6oSZLscxiCpLsQw9139G-ioJWs5rxk1pX7L9BQvIhROZd7usDyeaaW9tzzm93YPiy-nRVdDN5bEg150-bngKfiY1rhe7MIhH7mVnSYBuPMbGh0yJivScgh00uEWjFzejL8VwLSgqtk8U4xcU_cgzWH_YlQL5n9ZZXym854ejWmO7862x9OqgAWGWY7Gz8FeeV4pNdRVNPVmJZy5VJbqWiYM-Snqlt5IZeaCRjqKClF8eWxKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز به نقل از منابع مدعی شد: ایران از یک سازوکار شبیه به تهاتر برای فروش نفت خود به چین استفاده کرده است
🔹
پکن پول نفت تهران را به صورت اعتبار، جهت خرید کالا‌های چینی مانند دارو، خودرو و تجهیزات نظامی پرداخت می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/688672" target="_blank">📅 11:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688671">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52d9a4bf3.mp4?token=ZC_PvyiXO0LwJn0EHQaqRCdcoyfC7KjYgM0LDMykWWLIbsnWs2ilzyP0_zGkc4aaZz_Hf5OgDOST_K-NYvjqwHhn6rqzZcYfwM4Ip19vemxYBha2ssOfHyrRJou6IvK0cbS3v-iLt-xxe-cXX2Whd07_byv04MxlILEQkxyMCUB77uZ31kqCJnDDd9v8MSqXKeh5fgg7IOadCTF0quU9urD3dtaVlv5WQX84U7cV3cJNdSKEZcxRv3b9cPTcgSxrDG9tPfBe-fRLPMfLuHiPbIQuYg5gDmPFHHFocN6IElKupqVrzukErdoNNj1Bos83WOI4cOm1FXiRYFQI88lzUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52d9a4bf3.mp4?token=ZC_PvyiXO0LwJn0EHQaqRCdcoyfC7KjYgM0LDMykWWLIbsnWs2ilzyP0_zGkc4aaZz_Hf5OgDOST_K-NYvjqwHhn6rqzZcYfwM4Ip19vemxYBha2ssOfHyrRJou6IvK0cbS3v-iLt-xxe-cXX2Whd07_byv04MxlILEQkxyMCUB77uZ31kqCJnDDd9v8MSqXKeh5fgg7IOadCTF0quU9urD3dtaVlv5WQX84U7cV3cJNdSKEZcxRv3b9cPTcgSxrDG9tPfBe-fRLPMfLuHiPbIQuYg5gDmPFHHFocN6IElKupqVrzukErdoNNj1Bos83WOI4cOm1FXiRYFQI88lzUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژل دانه‌ کتان، ارزان‌ترین کلاژن دنیاست
🔹
دانه‌ها را بجوشانید، لعاب طبیعی‌ آنها آزاد شده و ژل غلیظ به دست می‌آید که پوست را سفت کرده و موهای آسیب‌دیده را ترمیم می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/688671" target="_blank">📅 11:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688670">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXy4nVds-kdq6VnU7NKeT5sfIDKbtz6JXKdninstEyCqcAC329nn2TtE-7Wg-2tE7BkGGr6zxFbOrZ0x75B0tL6K-nAP5Gk6NKvBGuXUH_bDNhk3HuEPUAZOBLK9WESiVLBb5cpC8QExEHMfH_wc4wzN4WzCny7jSSPbHYHb08q1htYj3Ea4w7Vy-gN9F9-F73iyFpmzzDSTg7GA-3G_C31CuaQkmwxJ3jRGzCErPzWIzw-jGxVSjtmjZO8jJ5DEiS8g0-uecpDJGkXW0IQ-p5ZHQsvDmnhD1-cjlydigqNGXTh21tvsiMXcoVX-JeyfbYhCHgButAmbCrs3w2rEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قرعه‌کشی جام ملت‌های آسیا ۲۰۲۶؛ تیم ملی فوتبال ساحلی ایران پس از انجام قرعه‌کشی مسابقات جام ملت‌های آسیا با لبنان، ویتنام و افغانستان هم‌گروه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/688670" target="_blank">📅 11:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688669">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
آیا پاییز و زمستان قطعی برق خواهیم داشت؟
وزیر نیرو:
🔹
از الان نمی‌شود پیش‌بینی کرد اما تلاش ما این است که پاییز و زمستان آسان‌تری داشته باشیم./ باشگاه‌خبرنگاران‌جوان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/688669" target="_blank">📅 11:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688668">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
میانگین قیمت خودروهای وارداتی چه قدر است؟
🔹
میانگین قیمت خودروهای وارداتی در سال ۱۴۰۴ حدود ۲۳ هزار دلار است که نسبت به سال‌های قبل افزایش یافته. در سال ۱۴۰۲ این رقم ۱۹ هزار دلار بود، چون بیشتر خودروهای اقتصادی وارد می‌شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/688668" target="_blank">📅 11:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688667">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc4549ab4.mp4?token=HVunTeB8vLPT7pkMY51kmEagnyUqF1x-NpgM5Hw1a_3hpp0MXwnAqnX8bMkqHtvLU4h7GS1ldNK4wPhv5MDC-gd-pfBQwSDIU2UIlf-QsC55qE0xfi-rx1x1r0XKHTSezCeCNNqHSf36UIlYfxWeHreEkVXQESob5j7_u-Vc65NvTSN9XyH9OP5A858L6vmxLNWwkGdE86f9vHxUiNZspNsRb_NZlL74B2pQ_WcwOz48FiZ2mu1FmIJqt_Z-1hTpgQOsFzTxQCnH2Un9X2YqAgCm-XJ_bNzwA_zImR7mH5SrF-FfDaBem9qlZDsOUeisEJMqJBgsUrfYpWL7HJDv1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc4549ab4.mp4?token=HVunTeB8vLPT7pkMY51kmEagnyUqF1x-NpgM5Hw1a_3hpp0MXwnAqnX8bMkqHtvLU4h7GS1ldNK4wPhv5MDC-gd-pfBQwSDIU2UIlf-QsC55qE0xfi-rx1x1r0XKHTSezCeCNNqHSf36UIlYfxWeHreEkVXQESob5j7_u-Vc65NvTSN9XyH9OP5A858L6vmxLNWwkGdE86f9vHxUiNZspNsRb_NZlL74B2pQ_WcwOz48FiZ2mu1FmIJqt_Z-1hTpgQOsFzTxQCnH2Un9X2YqAgCm-XJ_bNzwA_zImR7mH5SrF-FfDaBem9qlZDsOUeisEJMqJBgsUrfYpWL7HJDv1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی ترامپ متوهم: ما دقیقا می‌دانیم در «کوه کلنگ» چه می‌گذرد و فعالیت‌هایی را در این سایت رصد کرده‌ایم/ ممکن است ناچار به هدف قرار دادن این مکان شویم ‎
🔹
ایران در حال فروپاشی است و برای دهه‌ها قلدر خاورمیانه بود اما اکنون دیگر این‌طور نیست. #Devil…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/688667" target="_blank">📅 11:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688666">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803268b4e6.mp4?token=UiJjQD-58wNWG6hHuE3ibECzX8ntSA_ksozRsWpHOGcYXA6wI4zXKh09MqG4wKD-1dNHP21Z_dL0MeUfsFRUi2xisS6JGUbi8XVVNXFqAzTiCc3VdzO9FYyXegI1jAVI7WW6O_ds2QO8pHJG0E-sIKNsVhNd0QLWmWhASdH0rHVbJvfsvtZSYMpcLpN5AKHHIpoiCp3AOs3Ulx53goyjY68_0Tfzw8HeveDKMt8aQtygJtsvywU3yhz6KaKTP0HSWWjQukkTHiPestXlIIFw4tXkuSpQ3oefddoAuotgYO3ysSFhLruRyKfDXIchJwOLK4Ubo_3r_hby51ZOQSOTVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803268b4e6.mp4?token=UiJjQD-58wNWG6hHuE3ibECzX8ntSA_ksozRsWpHOGcYXA6wI4zXKh09MqG4wKD-1dNHP21Z_dL0MeUfsFRUi2xisS6JGUbi8XVVNXFqAzTiCc3VdzO9FYyXegI1jAVI7WW6O_ds2QO8pHJG0E-sIKNsVhNd0QLWmWhASdH0rHVbJvfsvtZSYMpcLpN5AKHHIpoiCp3AOs3Ulx53goyjY68_0Tfzw8HeveDKMt8aQtygJtsvywU3yhz6KaKTP0HSWWjQukkTHiPestXlIIFw4tXkuSpQ3oefddoAuotgYO3ysSFhLruRyKfDXIchJwOLK4Ubo_3r_hby51ZOQSOTVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخریب عجیب یک کاروان‌سرای تاریخی در سبزوار
رئیس میراث فرهنگی سبزوار:
🔹
کاروان‌سرای تاریخی «روس‌ها» در سبزوار تخریب شده است. این بنا در دوران پهلوی ژاندارمری بود، سردر باشکوهی داشت و برای ثبت ملی اقدام شده بود. تخریب توسط شهرداری تأیید شده و مجوز آن احتمالاً با جمع‌آوری استشهاد محلی صادر شده است.
#اخبار_خراسان_رضوی
در فضای مجازی
👇
@SedayeKhorasaniha</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/688666" target="_blank">📅 11:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688665">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPFS79oUC6svuvOWP0qgFJINgv5l8bCge_pIQ9Y_U0QhBbFmVS6XdwuoMk8dLICUBlz9XyAG25VejtdauImqsF_0zpn-tdslZvlvmEt9ovvnuYoNnLIr3JLJpN3JT3gS7Ol1_1AbCMETQ488mJaQS089qxgBUgKABIQJrmPTRxsfKq6tkmz1WOmZ36IcI9o9yrTGe3xOZxlhUFhlVD0eIrDHZoOiw39CNQj5ZeqKqxEoBEGvjALUuuOZVjQALlw4H0_ywH94i8cn3BIFSztLVcrPSe1mg8jyfViG1fbTgdlhuv-OuQn1i2OPpWmAah9BP4YjRdbolyW4Swbaoz67jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع سهمیه‌ای اقلام مصرفی خودرو
قطعات وارداتی شامل:
کیت‌کلاچ، لنت‌ترمز‌،شمع،وایرشمع،تسمه تایم،تسمه دینام و...
مختص خودروهای داخلی
شروع طرح: پنجشنبه ۱۹ شهریورماه
ثبت سفارش با محدودیت کد‌ملی
تحویل رایگان از ۱ تا ۳ روز کاری از طریق پست
🌐
متقاضیان گرامی جهت کسب اطلاعات بیشتر و درخواست اقلام می‌توانند به وب‌سایت ایرانکو مراجعه نمایند:
www.iranko.ir
.</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/688665" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688664">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ed56d9b64.mp4?token=kNAcISSJkDIHsA3-Jrn4sNJp1-vjlRYf0WSLspqQ4-CQce8v71YE3vcwPUki8gprsmqjL82RhXHKzj4f1e7atL4HgBVRjv4DA1uMUEfGE8TDR0CnjvXf-MZwHMfBE8DeWcQgn55zLRG4EAOLs6_089Mm2csIywjpHXh77mZ2J0HFTEhDFxzacr14bbtnSs2RR48LCz31J57HjOdd6nYgh6xfHwtNv4xgWlhJzOIIMW84QPe2SIJdt2V2US7bZ7H64yScm7ZgRkGEU3xXKQT_8uR-YV0NS3-8eRa33JvUlduD1baDjhpPyeRbr1ZN_1aV0z9mC4HEe0okLexPsxPvTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ed56d9b64.mp4?token=kNAcISSJkDIHsA3-Jrn4sNJp1-vjlRYf0WSLspqQ4-CQce8v71YE3vcwPUki8gprsmqjL82RhXHKzj4f1e7atL4HgBVRjv4DA1uMUEfGE8TDR0CnjvXf-MZwHMfBE8DeWcQgn55zLRG4EAOLs6_089Mm2csIywjpHXh77mZ2J0HFTEhDFxzacr14bbtnSs2RR48LCz31J57HjOdd6nYgh6xfHwtNv4xgWlhJzOIIMW84QPe2SIJdt2V2US7bZ7H64yScm7ZgRkGEU3xXKQT_8uR-YV0NS3-8eRa33JvUlduD1baDjhpPyeRbr1ZN_1aV0z9mC4HEe0okLexPsxPvTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی از اولین بنز میباخ ۲۰۲۶ دنیا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/688664" target="_blank">📅 10:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688663">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/397d00b91d.mp4?token=vagz7dSs1W9ruc3q2Ilcj7-7LczooaDs38sa3vd7V51MAyCrZxd0p4EikNmIO88biOskaCLHnjAVZWc7V-JymTMXjGighNLTjW5ejUGLitQQ_8MSI4C1JYj6wj_GtwByvyvjYyn4o8Oxboxz5gIkfn1QluzxoniRSbKcINoelkjxNC4oHBCexwNO3-hbsb4NCMft-7xhPoyNPr1DljZjjj64UKjtzruZ5HdEVBWEmJCtPOM0y9DewXWA4F7fPAZlD29bhXWhUCC6NkirFwQ-8EPDtIXeVqCsTL0WAGkHb8emVyfxHsi2ysDfYGptvqhKoiRAgGVUBqzYkKsfRGgPpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/397d00b91d.mp4?token=vagz7dSs1W9ruc3q2Ilcj7-7LczooaDs38sa3vd7V51MAyCrZxd0p4EikNmIO88biOskaCLHnjAVZWc7V-JymTMXjGighNLTjW5ejUGLitQQ_8MSI4C1JYj6wj_GtwByvyvjYyn4o8Oxboxz5gIkfn1QluzxoniRSbKcINoelkjxNC4oHBCexwNO3-hbsb4NCMft-7xhPoyNPr1DljZjjj64UKjtzruZ5HdEVBWEmJCtPOM0y9DewXWA4F7fPAZlD29bhXWhUCC6NkirFwQ-8EPDtIXeVqCsTL0WAGkHb8emVyfxHsi2ysDfYGptvqhKoiRAgGVUBqzYkKsfRGgPpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر روزتان را با ۱۹ بسم‌الله شروع کنید
روایت داماد شهید رهبر شهید انقلاب:
🔹
رهبر شهید، هر روز یک کاری را به نیت حضرت امام زمان(عج) انجام میدادند و ثواب آن را تقدیم ایشان می‌کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/688663" target="_blank">📅 10:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688662">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd13c4a34e.mp4?token=NGRp3UW2AnXz8lertEoKRM4ryU0Gk8BWly1rKm5BArcTKHz1TlRnqzZNDgAexK3eaI7ge_Mkgrtzi8nkZwCvmESYk8irkF4RxyfoYBFTKp94bfXhp1eU-oLNOANRLK_N20LMr2qsiOxUdfx03JUvtSELMLzgl1jhUW4hmysCjPPYcBpL9hvpQAUOjoMVlLqyIKn38AoXzXHV4-ZQn3L5Yyj_KqphWCRVr7Ep7-55A6NTrbRCcRBJuKF_YiUFHYXsFOjEOqjHshQNy15JbAk5f-qIK48TNxEOSxHMQuZtXa5oFl6SHQGSndRL0PMI3YWjoCzPHZHOM8m7fZW6ATVI86EtVWZc1J_pKNKxVdkxWhd1N4-Y1ShTawI_70qTrakZ7HYr3jAea5dNyWsh9OY-TSWz_dXPwMaAWPXRU-4UcICHWNt2tJZYC2t5KBZ8fXSSqs0F4noSEV2GTb-By8rlnu-X_fvJn90kNkhhKH3S3Fewey6cDQUr-kF2P94q3u9OqnMQNoJ6vWbegEWUVpWja9wZCnaHmj0Wh5KcTecMCkyFjF7JFIBBsirAhZNUpTeTiVPo0WcdpLsKiiy9WEsvhK8S9G9nXznoWBgw8h9Kk7EkjkQNUeAVql1UyGUOE3Pp7GOIbCn9R3uBfyrEAIuXZBF_V45f8S5ED20QfnmrLkY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd13c4a34e.mp4?token=NGRp3UW2AnXz8lertEoKRM4ryU0Gk8BWly1rKm5BArcTKHz1TlRnqzZNDgAexK3eaI7ge_Mkgrtzi8nkZwCvmESYk8irkF4RxyfoYBFTKp94bfXhp1eU-oLNOANRLK_N20LMr2qsiOxUdfx03JUvtSELMLzgl1jhUW4hmysCjPPYcBpL9hvpQAUOjoMVlLqyIKn38AoXzXHV4-ZQn3L5Yyj_KqphWCRVr7Ep7-55A6NTrbRCcRBJuKF_YiUFHYXsFOjEOqjHshQNy15JbAk5f-qIK48TNxEOSxHMQuZtXa5oFl6SHQGSndRL0PMI3YWjoCzPHZHOM8m7fZW6ATVI86EtVWZc1J_pKNKxVdkxWhd1N4-Y1ShTawI_70qTrakZ7HYr3jAea5dNyWsh9OY-TSWz_dXPwMaAWPXRU-4UcICHWNt2tJZYC2t5KBZ8fXSSqs0F4noSEV2GTb-By8rlnu-X_fvJn90kNkhhKH3S3Fewey6cDQUr-kF2P94q3u9OqnMQNoJ6vWbegEWUVpWja9wZCnaHmj0Wh5KcTecMCkyFjF7JFIBBsirAhZNUpTeTiVPo0WcdpLsKiiy9WEsvhK8S9G9nXznoWBgw8h9Kk7EkjkQNUeAVql1UyGUOE3Pp7GOIbCn9R3uBfyrEAIuXZBF_V45f8S5ED20QfnmrLkY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی اپل از آیفون‌های جدید تا اپل واچ و ایرپادز
🔹
اپل شب گذشته از آیفون دوئو، آیفون ۱۸ پرو و پرو مکس، اپل واچ سری ۱۲ و اولترا ۴ و ایرپادز ۵ رونمایی کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/688662" target="_blank">📅 10:45 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
