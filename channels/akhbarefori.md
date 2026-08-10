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
<img src="https://cdn4.telesco.pe/file/AISTfjBj_wPqBOHU0SBZqdOVDami_CwZ3xI_njsOFyyzxr_Y1SmbENZ8jRcnadOBhR_PN4SHZLb2oVdOlEAs1oqlos-FkDk94Ilx1oOG2g7HnhpbRIfyuhSDUVWTkxm-p8Oz9BwP5oSG14NlDWRiEwMwCWAoBFfiwJJ4ByNHhmRJDZWRMNgDsDKpiw7jV0TigOVapRJYPAXds6nUQ_5iEiLyUDnetGQRT3ZnkxmmenOe0whvL37POgd2QiWJYBmezwoaqLanmG1SoG4LeWlfhnoBxMYPsrA4_0NMXW1jHD4DnOk2PS4Xe8yN8V3pjBZOrSctAl3Os2-x2KWKCq_0eg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.24M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 20:52:02</div>
<hr>

<div class="tg-post" id="msg-680081">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMB_q0ZmYINo5V9kv7hs5Kmp41HChaKi6FN_U0CDkNxs18RrFx62PgpGIsL5PvAcSY-_tu94E6bKqqwLYWT65EKeF2rXEnjTpp6T1YVRbF-JUu4e3ZTUP86tI1mbq-lpnEm4CGOtHt6SH7rxPZpwh1GfebrTQck6oVime1MNpDi_Q1PcuDb5919puRwZYrDW00UuUNNUaqi5RTDuRoua2rHSxbD28qnRZAzh4-W6gFjSv1-2chG1qbEDq8VAJNuV-LF2jcMbu5Oz5r7R7D5vn2y_lhG6gfkMAj4yfVT5xPnnRowBq_pZ7o4n0JnlPkE9mNOYwdTE3ps64G1rUQa6HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینفانتینو به رابطه غیراخلاقی با یکی از کارکنان یوفا متهم شد    نشریه انگلیسی «تلگراف»:
🔹
جانی اینفانتینو متهم شده که در زمان تصدی پست دبیرکلی اتحادیه فوتبال اروپا (یوفا) با یکی از کارمندان رده‌پایین فیفا رابطه غیراخلاقی داشته است.
🔹
گفته می‌شود این خانم در…</div>
<div class="tg-footer">👁️ 24 · <a href="https://t.me/akhbarefori/680081" target="_blank">📅 20:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680080">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سهمیه سوخت سالانه تراکتورها به ۲ میلیارد و ۶۸۰ میلیون لیتر افزایش یافت
🔹
توانیر: قطع برق پتروشیمی دماوند برای حفاظت از شبکه بود
🔹
مارین ترافیک: تردد در تنگه هرمز به شکل قابل توجهی کاهش یافته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/akhbarefori/680080" target="_blank">📅 20:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680079">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f2fb02188.mp4?token=gTGJMPJLA5_M2zJ_tvRIe0fbd_evVScPhXZQwcJIWiL65dQInS6xz5vVwplE4I9eRgYSFe2TCyCWqm1TxBReJll2bjtRmwmJ9YP5P3f7qi3mmqGvkLo9CYObFbWuIxnAItc1NbwRXn06jRh8wxUMuLli81I6D0uyGV0W1zcnlkOdl5z6QsuRNrnHChZZeFknXw3tagaonYQz8hi_4g4rDuKp6aDRav6ssVe9wk68dUAHDBxOQXel2GYEpN-JneKyoYF-58J7HfaaSSg_tD_lbSUpWDz5_NZJq-rMFggWTmicItu1yfXqAfxpsNmMCDQbYKmn8UBi9pddT6p7j41E4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f2fb02188.mp4?token=gTGJMPJLA5_M2zJ_tvRIe0fbd_evVScPhXZQwcJIWiL65dQInS6xz5vVwplE4I9eRgYSFe2TCyCWqm1TxBReJll2bjtRmwmJ9YP5P3f7qi3mmqGvkLo9CYObFbWuIxnAItc1NbwRXn06jRh8wxUMuLli81I6D0uyGV0W1zcnlkOdl5z6QsuRNrnHChZZeFknXw3tagaonYQz8hi_4g4rDuKp6aDRav6ssVe9wk68dUAHDBxOQXel2GYEpN-JneKyoYF-58J7HfaaSSg_tD_lbSUpWDz5_NZJq-rMFggWTmicItu1yfXqAfxpsNmMCDQbYKmn8UBi9pddT6p7j41E4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب حجت‌الاسلام ‌والمسلمین حسین طائب به سِمت رئیس سازمان بسیج مستضعفین سپاه پاسداران
💬
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی حجت‌الاسلام ‌والمسلمین حسین طائب را به سِمت…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/akhbarefori/680079" target="_blank">📅 20:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680078">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319955d4cd.mp4?token=U2jEAQPSelnBCu7BhGau719pAqk3yAsXs2hlgYtMXGEiAhFgnSaQstUVAJdr8cgHLm27zX_C9SY3ZjtsePbjSNK7ChPBnaj1ViTM8IyFeyUJWlWVICWVNb4nlvP77yc9Tu7f3z5YQvSUP0bUuSd2mN-Lzl5xdbHFmvT2mp_ppEjz9CnfHUhqPnDGSECYc_Be25dj9ZWtqyMc238-BpAao5A0uQtY2Ox9xionYzWWwCE2YEQWY-FFRiAZpNkmdj_zWHxmmvhrC4Y4tC5PKtYF-oTobcBrVjnLY7oN7iEPaR6nP6s2ratqBiuv4xkG2HNixQN6rL3TUjkqmGpSflhnrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319955d4cd.mp4?token=U2jEAQPSelnBCu7BhGau719pAqk3yAsXs2hlgYtMXGEiAhFgnSaQstUVAJdr8cgHLm27zX_C9SY3ZjtsePbjSNK7ChPBnaj1ViTM8IyFeyUJWlWVICWVNb4nlvP77yc9Tu7f3z5YQvSUP0bUuSd2mN-Lzl5xdbHFmvT2mp_ppEjz9CnfHUhqPnDGSECYc_Be25dj9ZWtqyMc238-BpAao5A0uQtY2Ox9xionYzWWwCE2YEQWY-FFRiAZpNkmdj_zWHxmmvhrC4Y4tC5PKtYF-oTobcBrVjnLY7oN7iEPaR6nP6s2ratqBiuv4xkG2HNixQN6rL3TUjkqmGpSflhnrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب سردار دریادار علی عظمایی به سِمت فرمانده نیروی دریایی سپاه پاسداران
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی سردار دریادار علی عظمایی را به سِمت فرمانده نیروی دریایی…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/680078" target="_blank">📅 20:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680077">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فعلا خبری از تسهیلات کسب‌وکارهای اینترنتی نیست
رضا الفت‌نسب، رئیس اتحادیه کشوری کسب و کارهای مجازی در
#گفتگو
با خبرفوری:
🔹
کسب‌وکارهای اینترنتی نسبت به فعالیت‌های سنتی، هزینه راه‌اندازی پایین‌تر و امکان بازگشت سریع‌تری دارند و برخلاف مغازه‌ها، نیازمند هزینه‌های سنگین اجاره و راه‌اندازی نیستند.
🔹
با وجود پیگیری‌ها از نهادهای دولتی و حاکمیتی برای پرداخت تسهیلات به کسب‌وکارهای مجازی، فعلا برنامه جدیدی اعلام نشده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/680077" target="_blank">📅 20:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680076">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a82ea307d.mp4?token=uDFuCcP7kvSNC6VIwBBSo2IMNSmam9PVpBIIpuSoAq5N0mCHmzZYLM3QZSpRf7nxknhfXotuEtpSxOpgjh_j2EoP7iLBC8Hof2drx9rDGWlC96OCzuFxJVusOOWoTDNQzs46N5amqrgJAfOcqWkRePMUIOVDzf5bWmZm1ML90udVeWbuSBKaDkqvjqS7zImlQJYayZfkeTOGcO9MwQ_muDbQy29yrVd1daNQtCnVCvRCqEvg5bo2eR0QvCdt3FBeMYS8hG_jkU4mYTvpVM23kGdyk3_A-V79UB1YYBA_TOqu8BKR4GBfuZUmYjj_H-WY_rSHULnmyFABBaRr0nBEbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a82ea307d.mp4?token=uDFuCcP7kvSNC6VIwBBSo2IMNSmam9PVpBIIpuSoAq5N0mCHmzZYLM3QZSpRf7nxknhfXotuEtpSxOpgjh_j2EoP7iLBC8Hof2drx9rDGWlC96OCzuFxJVusOOWoTDNQzs46N5amqrgJAfOcqWkRePMUIOVDzf5bWmZm1ML90udVeWbuSBKaDkqvjqS7zImlQJYayZfkeTOGcO9MwQ_muDbQy29yrVd1daNQtCnVCvRCqEvg5bo2eR0QvCdt3FBeMYS8hG_jkU4mYTvpVM23kGdyk3_A-V79UB1YYBA_TOqu8BKR4GBfuZUmYjj_H-WY_rSHULnmyFABBaRr0nBEbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب امیر سرتیپ کیومرث حیدری به سِمت جانشین رئیس ستاد کل نیروهای مسلح
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی امیر سرتیپ کیومرث حیدری را به سِمت جانشین رئیس ستاد کل نیروهای…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/680076" target="_blank">📅 20:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680075">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb31addbe.mp4?token=h7IZgaiIH_GloYCpuoSJ35MYQ9ttOyps66XG3OLBawlQk9XuwnBG0JQSAr7V6nfrsnLm-q3XmweU9PbYw4-elZghcylRHrNqFgsfbcreS7UNJMiGdE5cdCKm3-uymcX5yt4Yy5YsSUJOzYZKoffF2S4eQhW4uHnXQVWYOEyqnd8CYa4o0_h23gdPi3PmR8UIC-6gk3HQX8x0DAfy1mMpEFXXES_3bQn9rQGaVUOqahdFpsxWy_OIAfxhD0VW0FnJWx2A-Q_GcVX9Oz45fhcChu_xnu5dI8DehVz00154oPo5naBvj-6hzTp97njkWHp-gLmROLc5t-zKqf50q7dhsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb31addbe.mp4?token=h7IZgaiIH_GloYCpuoSJ35MYQ9ttOyps66XG3OLBawlQk9XuwnBG0JQSAr7V6nfrsnLm-q3XmweU9PbYw4-elZghcylRHrNqFgsfbcreS7UNJMiGdE5cdCKm3-uymcX5yt4Yy5YsSUJOzYZKoffF2S4eQhW4uHnXQVWYOEyqnd8CYa4o0_h23gdPi3PmR8UIC-6gk3HQX8x0DAfy1mMpEFXXES_3bQn9rQGaVUOqahdFpsxWy_OIAfxhD0VW0FnJWx2A-Q_GcVX9Oz45fhcChu_xnu5dI8DehVz00154oPo5naBvj-6hzTp97njkWHp-gLmROLc5t-zKqf50q7dhsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب سرلشکر علی عبداللهی به سِمت رئیس ستاد کل نیروهای مسلح
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده معظّم کل قوا در حکمی سردار سرلشکر پاسدار علی عبداللهی را به سِمت رئیس ستاد کل نیروهای مسلح…</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/680075" target="_blank">📅 20:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680074">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwYx96E6CCzhnFP0DqKaRjsDQ1EOWeB6crGr2LvlZVIqul3M3NeOtAc7ilFDu6Z8ngPAhKtAoslvVVQklNpQCIXAI9vun-0gTkZi87_-KdMHl68A8fK-w3uFVxvi6Oa4XFiHK-BpSCE134qxOyD7UPOxW0hIoCnijiAqFL2LuqMLn-wrKIr-fZKQ5cS2FHDaTZZF_AFbiV3JRxAwG7zteLI69aKVYMF9mBxWOCvjkL1wLqk0gKNS9RVDXlSzWvV_4qMSEibgOlbv9y3FehlSmFMgaqEUN7IFBda6i-BtjI3DncTNx2Cie-ETm1DAZLk5Nz3QbA5bks2mjiWipmg_Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با صدور احکامی جداگانه از سوی فرمانده کل قوا صورت گرفت؛
📝
انتصاب شش فرمانده عالی‌رتبه در ستاد کل نیروهای مسلح، سپاه پاسداران و بسیج مستضعفین
💬
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده معظم کل قوا، با صدور احکام جداگانه‌ای مسئولیت‌ها و مأموریت‌های شش…</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/680074" target="_blank">📅 20:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680073">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvPt4c7Y4LLoUhvFAeMcrolfkySdBxXH-TzUbkpI_GSisN40YPOMRcRWA34CmVMY1gpMzTiJFbOjlATc1FVQNQLXQ6jtHcyI6t7IlZHEy3_VTXZtrwmImp3uBt3C_JB8agGpRFhrFa2Xf1e1ASljglKx3_LDwdaG1vlEvKSQG2HwKl6L7EN3yjVX48cagQWQrH1GznNFUdggfltFypZTySY8UZQ-Kca_wRztYnhZRxzQpecGWWe7vdxNUvxtRg30Pw6ydUiVQ3koEo-ymHvr8dFXgNlDueAQqI25mw8rUTof6RCSeZQsoCviEyw-epTPlnvxyQbfPSVY1WGlnV8S3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: ایران قوانین را در هرمز تغییر داد/ عربستان، ترکیه و پاکستان به فکر افتادند
الجزیره:
🔹
خلیج فارس در حال تغییر قوانین برای ایران است.
🔹
ایران از جنگ به عنوان اهرم فشاری برای کسب برتری بر تنگهٔ هرمز استفاده کرده است.
اکنون عربستان، ترکیه و پاکستان در حال تشکیل یک ترتیبات امنیتی جدید هستند که می‌تواند تا حد زیادی مانع از پیش‌برد مزیت‌های کسب‌شدهٔ تهران شود. /خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/akhbarefori/680073" target="_blank">📅 20:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680072">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
وقتی از کما بازگشت؛ روایتی عجیب از شفا و یک سفارش مهم
🔹
00:12:45 صحت خواب مادربزرگ از حادثه تصادف
🔹
00:23:40 هم صحبتی با روح فردی که در زمان کما بودنم، فوت کرد
🔹
00:31:00 حضور فرد نورانی و دست کشیدن به شکستگی داخلی بدن که بیمارستان متوجه آن نشده بود
🔹
00:35:10 سفارش حضرت موسی‌بن‌جعفر برای حق‌الناس و طلب حلالیت
🔹
00:49:50 کارهای خیری که نجات‌دهنده شد
🔹
00:57:30 رؤیت سقوط افراد عریان در دره‌ای خوف‌ناک
🔹
01:03:05 اهمیت دادن به خواندن نماز اول وقت بعد از تجربه
🔹
01:12:00 نیکی کنید و بازتاب آن را ببینید
🔹
قسمت بیست‌وهفتم (حلالیت)، فصل پنجم
🔹
#تجربه‌گر
: سید‌ امید متقی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/akhbarefori/680072" target="_blank">📅 20:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680069">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URZBPHxwuH9LDpfNEOIUd1ZEuK01VGH7CLW-mVxHKVlTD2PURG9LDbRV8MCTgnLNzRZT4TKpMdHXuf81w6MKMJAEBprTF0kBSpCUwx6kW5cKTchCHmVkQFe6ZAkgbtdpNN0BCF1N3C8lfHm6R4qLiHWPhaAtnwowCprPn0aAciENg7CF90SGcVboak4CDVkP7TIeMx2D71AVGx5lJhLX1KqF19uRWF0_hXvFBANWgQzWUefCtMKZmqjunGlt8ummwfMntOg92bnT_XzcCl8RkMU9jG-PRPHLG3-97n4dw-h7IcEA1VQUQNBjmcn6MruFZh2J5KkYYYxXuDa_8KaD-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمرکز؛ قربانی اول استفاده افراطی از شبکه‌های اجتماعی
🔸
در این نظرسنجی بیش از ۲۶ هزار نفر شرکت کردند که سهم روبیکا حدود ۵۴، بله ۲۸ و تلگرام ۱۸ درصد بوده است.
🔸
شرکت‌کنندگان به ترتیب: افت تمرکز، آسیب به ارتباطات حضوری و اخبار زرد و شایعات را به عنوان بزرگترین آسیب‌های استفاده بیش از حد از شبکه‌های اجتماعی معرفی کرده‌اند.
🔸
استفاده افراطی از شبکه‌های اجتماعی می‌تواند با پراکنده‌کردن توجه و کاهش تعاملات حضوری، زمینه را برای مواجهه و انتشار بیشتر اطلاعات نادرست و شایعات فراهم کند.
@amarfact</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/680069" target="_blank">📅 20:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680068">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJXFhi3cX2CgqPNPJOgy00s0sHENr_xYjmGZDOOS75LitGmwU-cl6pCH3k-SILqy5AfMWGig9_f7wDoyq-n_D1kAipILhZNjXrFO-zc76Yu93pniQS8ECZyMtQ4JdzDKS9we5wZbX566Ud7dTZhU1kEHFn7L6bytlxyj_vWo5o6JLYAAC4--RvoBSXvgeB0P5OJgYImG9gt-2IyHSNLInhEH9wg-fSmaguvtkS4QE6oVsCMEFfdBlgSmym4wJ5G-ztwiMAfYe_M-f-TyqFhTKWyasoGYjiIv2eV5VX-kGJgpweWyT4LuzPdAyADK3ZTqTrnltGqsKRaHtgFWN_CJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد: من هم از ایران می‌خواهم خسارات ما را جبران کند
رئیس جمهور تروریست امریکا مدعی شد:
🔹
ایران خواستار جبران خسارات ناشی از درگیری‌های نظامی پنج ماهه است و من نیز از آن کشور خواهان جبران خسارت هستم.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/680068" target="_blank">📅 20:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680067">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg3P0RKaesqaYjrnrAlR_LYiqZ6GozErv3Rb5J2HEFz38p-AHY-umgGQys8pLMuxtI2C5RvPUMgjFAo6MjatYrfBoPN1X_PpdunYkWBDoThB2YKnyV7m2-irKVpA3MTwivtGmHMLdEv6GRZ2NveAfbDwzpehVk_bwJ9iZSIcYKdMRAsCEOV1S0LPKFz99xG0tiYSbj-eZlAWv1Utch-202LYxeuEEINsnBwlQMbu67-XYoSorI6VMaz7B8oy4zwmmBr8N6AreP3XB9exDTTKTtF8yumt3pdU8zUPCRGlpASkAuDpX8s3_J1zxB4L7TBR-Vu8RWkPyR9V6Jm5devF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/680067" target="_blank">📅 20:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680065">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcZ7eU_wILpQijxXTSafgl4JJvDOpOQUfVcKRGU2kavCX4HPwa__Ie6uq1I1GJj922d5lyZWEW0zeC2E4HkHZAtzpKi5ws86j3_-XozKvcBwbaBeP2T-VeKCWh6ZmGsgFJTXC8r-pNMUM6WuHfr89d-n0UUmnpfoB6GPSOJzFnoepjMd8BT0rETRhMXPQZjHin6SVLbK-3cWa0t6NF5sJd7DglLt5oUl_MAAsnjQ_K1xyyeVwYmvikUVNsGs7xAdVHTENl8y6YAJ_0UF797cdUzzui_Bf-l2BuliAI34g3FV_vIGtlADlq8unP-CdTUIVf6AQsHGYgw7PVNilFpYEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد مرندی: ایران آگاه است که نیروهای رژیم ترامپ در کویت، امارات متحده عربی، قطر، عربستان سعودی، بحرین و اردن در حال بسیج برای یک حمله برق‌آسای بالقوه احتمالاً در کنار نیروهای اسرائیلی علیه مردم ایران هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/680065" target="_blank">📅 20:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680064">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed2fc31183.mp4?token=CJlJZni7DOF_d4AB-puEhx3pk8Q7V4jLJjtFZZxB5IvTJT9YpFRHfQLsH1w4qjvJaEJ-Y3-2o9WS4Z5FH0jHf1JyadBg_fKBL_Pykl8dcI_ZGwzrYHhx3gpXU1nu3HGaLtUwhASAYmh8bOK_OOTPEE7iraAYKqALDtZju6YJDgSu-ShlseeXQURwx7_E6cMzFXr2ZZQbM263V4CQjI-4sNpDeLRL51FfzOUwmMKvzbcrQFt7u1jptzJkJiCrGNB1IzfnN82FpZAQuhR8aU-9QXmbbaSehb_CwqNSm7nsdcWykkOu18pe-aHihKwe5e3OCb1CzH2AkJ0c6NDyxZMmkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed2fc31183.mp4?token=CJlJZni7DOF_d4AB-puEhx3pk8Q7V4jLJjtFZZxB5IvTJT9YpFRHfQLsH1w4qjvJaEJ-Y3-2o9WS4Z5FH0jHf1JyadBg_fKBL_Pykl8dcI_ZGwzrYHhx3gpXU1nu3HGaLtUwhASAYmh8bOK_OOTPEE7iraAYKqALDtZju6YJDgSu-ShlseeXQURwx7_E6cMzFXr2ZZQbM263V4CQjI-4sNpDeLRL51FfzOUwmMKvzbcrQFt7u1jptzJkJiCrGNB1IzfnN82FpZAQuhR8aU-9QXmbbaSehb_CwqNSm7nsdcWykkOu18pe-aHihKwe5e3OCb1CzH2AkJ0c6NDyxZMmkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افسر بازنشستۀ آمریکا: ایران معادلات را از هسته‌ای به تنگۀ هرمز تغییر داد
ویلیام پاتنم:
🔹
هدف آمریکا همیشه این بود که ایران به سلاح هسته‌ای دست پیدا نکند اما امروز تمام تمرکز آمریکا روی بازکردن تنگۀ هرمز است.
🔹
اقدامات نظامی آمریکا تاکنون نتوانسته به اهداف تعیین‌شده علیه ایران منتهی شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/680064" target="_blank">📅 19:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680063">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-0EfHWFBC7uWxkUEONlSn_aWaHXrKQEKXFF6vNVQtrie-aQ5OSISkMj9B4iQGXt79L8QczZop773D4zQNT6FFld57tnigVJdIAqB0r3pQlxHNJeKIW_mRYtawDWQtcKaAc3oHz5XTRQ3W_KNjv7I2I_8EPtRxvZ0Zdt1_kNxb5m2Cvc1R-1fpbGfO45NQjAhoQAStQ-OaM9qtbZ-nqNMvPmmymgXrwrJaAhP7osKSpiFe3lBQCwkNJAvsmxWzWSSWlxOYWFQ1DBMd-E1qwoVdSBk8EmFHaERLqf6BDQbjm5UrvSCunZivmtqhS0SSZOh7_s-EYVVm1sOHOELVenMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ خطر برای نوشابه‌خورها؛
نوشابه چگونه می‌تواند به گسترش سرطان کمک کند؟
🥤
🔹
پژوهش‌ها نشان می‌دهد فروکتوز می‌تواند در برخی شرایط به رفتار تهاجمی‌تر سلول‌های سرطانی کمک کند؛ اما این به معنای اثبات مستقیم نقش نوشابه در ایجاد یا گسترش سرطان نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/680063" target="_blank">📅 19:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680061">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
کاهش سوخت‌رسان‌های آمریکا در فرودگاه بن‌گوریون
شبکه ۱۲ عبری:
🔹
ارتش آمریکا روند خروج و کاهش تعداد هواپیماهای سوخت‌رسان خود از فرودگاه بن‌گوریون را با شتاب بیشتری ادامه می‌دهد.
🔹
گزارش‌ها نشان می‌دهد شمار هواپیماهای سوخت‌رسان آمریکایی مستقر در این فرودگاه، به عدد دوران آتش‌بس (حدود ۲۰ فروند) نزدیک شده است.
📲
‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/680061" target="_blank">📅 19:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680060">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQTtCoojAAyXBaZp5wGDDd05NIzoIkJ4z8a-azBRM8VoMXvH4y5p3zLYGbWq03mCQSdbvMroapm0jNBMeR9Gtx3yFKn9-i3VF8P5afZXHWf0XbIAMYo1zDLBqwDDIVdHcxCF_eh4w5NnPWdB8ml9XmyhVwPJdPD-nHkr8N7aOizCGswbCcjt9K6YuoVTDeMRlFUHBSsn_4wPxVRoq0EAcmm6GjDrhOfRERpk7pWi_l4uQERjCQn4D2KjXVka-uis1lFxFPtcV04bs4yyd81CJYTQMCCpwZiObSW-u7mWjnbRl1JiT7GqiK3U3fELEL5VZD5Jn2TwwRqwBwxWNNSQoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب سرلشکر علی عبداللهی به سِمت رئیس ستاد کل نیروهای مسلح
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده معظّم کل قوا در حکمی سردار سرلشکر پاسدار علی عبداللهی را به سِمت رئیس ستاد کل نیروهای مسلح…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/680060" target="_blank">📅 19:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680059">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcsVTrBpQ1F_LYi55wcPVT4ODdJT4WghlJsvWqlCpw_NtDw4yvxtsVabcWZNH14RfAOkiDcOnWjJyiLlrHGKCJAyWLcj2qEDMYplznbxITCVm17RqGAkv82BKhNCJ-9GB-gQa3H_yv9TlA9RgQsvrqVsq5pXMwNswUMe4jcL9SuyetbaDrQklxnAgLLQ6kVHFVT4uwpfv5vhKoNnzpmr_JU94tKBr8ohb2ca3m4HGsL_s_rFj6eAVKzO45sfI0FQ3fsiIbjZSLrGuTOt6Eore7VidngMc9Hi6zE01t0nZ9iApm8naB1JD2oIbeoBzPM-_QXn6l5nWwUJQvpdj3dTjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هوش مصنوعی به Word اضافه شد؛
چگونه آن را فعال کنیم؟
🔹
افزونهٔ Autopilot را نصب کن، درخواستت را بنویس، نامهٔ رسمیات را آماده بگیر.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/680059" target="_blank">📅 19:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680058">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJLi4guRrQml5Umhc5AFT2NDYkD0_YFR_-_5MlGRrYAmf2ev_gGpc7cWdt180GRQkh8KMSmBZWyHHDwuQZxtlG3-jPQaQJrk8GmfbtQj5WcRmKWkvlKYCxrA8j2ijYyIVLHk1d8Z2Br1tkBSN5yeT_bNHdIfjJi6ZIji2C2UES4Z3c6vKdi6Dv2_jXPLQIAH-zKSQoSbyaWk2Ji-S1HaEFcT2Lkp42E-UY7mqxjHiPozJ5EKSrKqyTwiXiQnQ-dwxfAjgPUW2Ww8SLjMOwMISazUrzJTZnTxRj0ZNIhOqa7sQIIkItgpiVOav9UUicvQ6R1wKwyyz1pec41BFlS2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنگه هرمز؛ اهرم فشار ایران برای بازگرداندن ترامپ به توافق
🔹
ایران بازگشایی تنگه هرمز را منوط به اجرای کامل تعهدات آمریکا در توافق ۱۷ ژوئن (رفع محاصره، لغو تحریمها، آزادسازی داراییها و عقبنشینی نظامی) کرده است.
🔹
مذاکرات با عمان نهایی شده، اما بازگشایی فوری نیست و به تحقق شروط ابلاغشده به آمریکا بستگی دارد. کارشناسان میگویند تهران تا حصول اطمینان، این اهرم فشار را حفظ میکند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/680058" target="_blank">📅 19:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680057">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36a60f89dd.mp4?token=ormAawlbf2IzJxRQuFCsXTZdbIdIxCJ9PVdP7QN4g1LBXiSK5Xcp4_Heap1Ev4r-63tUcI6n0sygUSIaAQYN7ZJGwzzSwqiOKE_UBsd3XaWVEu3BHogeQdtO_WvNRBdU9DfeNAVKM7cnqbbv1LNdTSoQzoW1SURlxXCDcsYihG2xRYe2JhjO8szU8pnnDFoVtwaP9n-lugXK_m6HappfaTT_TpgpICZXAz7aLfs7479HENQELSGTjtmkgYy2zivyrRb3-Ijf8cQmudSwcqWro0ggcKIZ9-R7FK9sHtFwXi7ayjQI009fQt_qFgHxKfFyATDohLe1yhwmN9Xg46SopQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36a60f89dd.mp4?token=ormAawlbf2IzJxRQuFCsXTZdbIdIxCJ9PVdP7QN4g1LBXiSK5Xcp4_Heap1Ev4r-63tUcI6n0sygUSIaAQYN7ZJGwzzSwqiOKE_UBsd3XaWVEu3BHogeQdtO_WvNRBdU9DfeNAVKM7cnqbbv1LNdTSoQzoW1SURlxXCDcsYihG2xRYe2JhjO8szU8pnnDFoVtwaP9n-lugXK_m6HappfaTT_TpgpICZXAz7aLfs7479HENQELSGTjtmkgYy2zivyrRb3-Ijf8cQmudSwcqWro0ggcKIZ9-R7FK9sHtFwXi7ayjQI009fQt_qFgHxKfFyATDohLe1yhwmN9Xg46SopQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجموعه‌های تابعه شرکت توسعه نیشکر راهی بازار سرمایه می‌شوند
🔹
دکتر علیرضا کاظمی در حاشیه برگزاری مجمع عمومی «شرکت توسعه نیشکر و صنایع جانبی آن» راهبرد جدید این شرکت را ورود مجموعه‌های تابعه به بازار سرمایه دانست و افزایش NAV را از نتایج این استراتژی برشمرد.
🔹
مدیرعامل «شرکت توسعه نیشکر و صنایع جانبی آن» افزود: در همین راستا خبرهای خوبی را بزودی از طریق اطلاعیه‌های مندرج در کدال به استحضار سهامداران حقیقی می‌رسانیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/680057" target="_blank">📅 19:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680056">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6888c6d752.mp4?token=LFGIYXptTPrRU2r9qbPiMVvEEsLdE7-_YYrft7MhVhZ7ORNxqiJsJq8g6ruc8xtYLDuWM3FpiNg8vxIA6C02B7a-ZP-jqRwFnUN13gJAK8rTcNvHXHHjSPUQKiYetg0jeNdPlB-E4w1EwH0GLWdbrU8O4jf4ETuPaqUXiB3uFdMDsRu2kshT7BnXenUsoRoX_VRx1A0wtSfpAZM_rfl5f_un-NPuK_Wc67ZyKg1Opqd3OZS086BYj_TcCfpZWWIoLNHJvuERrn3W79iCpdOWtOZE7Yge8wVLTnYG8e1NABAPPtmjZX9OrgpHEEz4iYM3yH6datFIcOM3G6GHEz9BTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6888c6d752.mp4?token=LFGIYXptTPrRU2r9qbPiMVvEEsLdE7-_YYrft7MhVhZ7ORNxqiJsJq8g6ruc8xtYLDuWM3FpiNg8vxIA6C02B7a-ZP-jqRwFnUN13gJAK8rTcNvHXHHjSPUQKiYetg0jeNdPlB-E4w1EwH0GLWdbrU8O4jf4ETuPaqUXiB3uFdMDsRu2kshT7BnXenUsoRoX_VRx1A0wtSfpAZM_rfl5f_un-NPuK_Wc67ZyKg1Opqd3OZS086BYj_TcCfpZWWIoLNHJvuERrn3W79iCpdOWtOZE7Yge8wVLTnYG8e1NABAPPtmjZX9OrgpHEEz4iYM3yH6datFIcOM3G6GHEz9BTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران؛ قدرتی نوظهور در باشگاه قدرت‌های جهان
!
شبکه آی۲۴ اسرائیل؛ دکتر محمود افندی، کارشناس و استاد آکادمی روسیه:
🔹
آمریکا نه در یک باتلاق، بلکه در یک فاجعه گرفتار شد؛ زیرا نتوانست به هدف راهبردی خود در برابر ایران دست یابد و حتی نتوانست توان موشکی و پهپادی ایران را از بین ببرد. کمبود مهمات مورد نیاز این جنگ و فرسودگی توان پدافندی آمریکا، واشنگتن را به سمت راه‌حل سیاسی سوق داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/680056" target="_blank">📅 19:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680055">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8e0GhYr3c1TlLDhALBL7qreNlfoelq8m1PDuU9iXfSGINihLuTXldjHLv4jEo8w1OjII-_UHnTAN2Hj9W9-n65eADM_Ry9PccQfqimLS_jwBI6_fCbZ_w4LMb1Tp8zcpxVF_K9d6VYdQ7JWaQLMgR1Q_A0T06DoFJkN_ilQX0MDyO1KhXqSPGftQtqiUmTnajN8yx0xopR4q4JmkcsbgBS3EncH3xkNlspKwHqN0B6_80gDU6cISEYV7CGW-1dSd_JJHuVO5fkreNr29Pxrvv65HQ3K7cBgzcgWQx207RmY3Y_P59cF7BdEhTrCr0fjFvvwSM8bsIuoAHtibWzQLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از یک بشکه نفت خام چه فرآورده‌هایی تولید می‌شود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/680055" target="_blank">📅 19:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680053">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب حجت‌الاسلام ‌والمسلمین حسین طائب به سِمت رئیس سازمان بسیج مستضعفین سپاه پاسداران
💬
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی حجت‌الاسلام ‌والمسلمین حسین طائب را به سِمت
رئیس سازمان بسیج مستضعفین سپاه پاسداران انقلاب اسلامی
منصوب کردند.
🔻
متن حکم فرمانده‌ی معظّم کل قوا بدین شرح است:
✏️
بسم الله الرحمن الرحیم
حجت‌الاسلام والمسلمین حسین طائب
نظر به شهادت پرافتخار و سرافرازانه سردار سرلشکر غلامرضا سلیمانی به دست دشمن صهیونی-آمریکایی، و با عنایت به تعهد، شایستگی، و تجارب ارزنده‌تان، و بنا به پیشنهاد فرمانده کل سپاه، جناب‌عالی را به سِمت
رئیس سازمان بسیج مستضعفین سپاه پاسداران انقلاب اسلامی
منصوب می‌کنم.
با توجه به اقتضائات و شرایط جدید کشور، تحقق مطالبات زیر با لحاظ تدابیر فرمانده کل سپاه، مورد انتظار است:
1️⃣
تعمیق و گسترش فرهنگ بسیج و مقاومت به منظور تحقق شعار «هر ایرانی، یک بسیجی» با استفاده از ظرفیت آحاد مردم مبعوث شده و اقشار میلیونی جانفدا در راستای ایران قوی و متحد و حفاظت از انقلاب اسلامی
2️⃣
تقویت شبکه‌ی اطلاعات مردمی، افزایش مهارت‌ها و آموزش‌های لازم توأم با بصیرت‌افزایی و بهره‌گیری از فناوری‌های نوین برای مقابله‌ی مردم‌پایه با تهدیدات دشمن
3️⃣
تعامل سازنده و مؤثر با دیگر نهادها و سازمان‌های حاکمیتی، دولتی و عمومی و گسترش گروه‌های جهادی، بسیج اقشار و محلات به منظور توسعه‌ی خدمات اجتماعی اثربخش با محوریت مسجد
4️⃣
ترویج فرهنگ بسیجی به عنوان الگوی مقاومت و پایداری مردمی در سراسر جهان در برابر استکبار صهیونی-آمریکایی
امید است توجهات و ادعیه سرورمان (عجل الله تعالی فرجه الشریف)، موجب توفیقات روزافزون شما و همه‌ی بسیجیان عزیز گردد.
✍
سیّدمجتبی حسینی خامنه‌ای
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/680053" target="_blank">📅 19:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680052">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب سردار دریادار علی عظمایی به سِمت فرمانده نیروی دریایی سپاه پاسداران
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی سردار دریادار علی عظمایی را به سِمت
فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی
منصوب کردند.
🔻
متن حکم فرمانده‌ی معظّم کل قوا بدین شرح است:
✏️
بسم الله الرحمن الرحیم
سردار دریادار پاسدار علی عظمایی
نظر به شهادت پرافتخار و سرافرازانه‌ی سردار دریابان پاسدار علیرضا تنگسیری به دست دشمن صهیونی-آمریکایی، و با عنایت به تعهد، شایستگی و تجارب ارزنده‌تان، بنا به پیشنهاد فرمانده کل سپاه، شما را به سِمت
فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی
منصوب می‌کنم.
ارتقاء آموزش و مهارت‌ها، تجهیزات و امکانات دریایی، اشراف اطلاعاتی توأم با رشد توان و آمادگی‌های رزمی، تعالی معنوی و بصیرتی، و توجه به نیازهای معیشتی برای تحقق نیروی دریایی تراز انقلاب اسلامی و همچنین تعامل اثربخش و هم‌افزا با سایر اجزای سپاه، بسیج و نیروی دریایی ارتش جمهوری اسلامی ایران و دیگر بخش‌های ذی‌ربط لشکری و کشوری، مورد انتظار است.
امید است توجهات و ادعیه‌ی سرورمان (عجل الله تعالی فرجه الشریف) موجب توفیقات روزافزون شما و همه‌ی رزمندگان آن نیرو گردد.
✍
سیّدمجتبی حسینی خامنه‌ای
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/680052" target="_blank">📅 19:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680051">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب سردار لشکر مصطفی ایزدی به سِمت جانشین فرمانده کل سپاه پاسداران
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی سردار لشکر پاسدار مصطفی ایزدی را به سِمت
جانشین فرمانده کل سپاه پاسداران انقلاب اسلامی
منصوب کردند.
🔻
متن حکم فرمانده‌ی معظّم کل قوا بدین شرح است:
✏️
بسم الله الرحمن الرحیم
سردار سرلشکر پاسدار مصطفی ایزدی
نظر به تعهد، شایستگی و تجارب ارزنده‌تان، و به پیشنهاد فرمانده کل سپاه، شما را به سِمت
جانشین فرمانده کل سپاه پاسداران انقلاب اسلامی
منصوب می‌کنم.
ایفای نقش جهادی در ارتقاء سطح آمادگی‌های سازمانی، با تقسیم نقش و مأموریت در راستای تدابیر فرمانده کل سپاه، مورد انتظار است.
امید است با عنایات الهی و در ظلّ ادعیه‌ی پر خیر و برکت سرورمان (عجل الله تعالی فرجه الشریف) مزید توفیقات و انواع فتح و ظفر برای همه‌ی نیروهای مسلح نظام اسلامی حاصل گردد.
✍
سیّدمجتبی حسینی خامنه‌ای
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/680051" target="_blank">📅 19:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680050">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب سردارسرتیپ احمد وحیدی به سِمت فرمانده کل سپاه پاسداران
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده‌ی کل قوا در حکمی سردار سرتیپ پاسدار احمد وحیدی را به سِمت
فرمانده کل سپاه پاسداران انقلاب اسلامی
منصوب کردند.
🔻
متن حکم فرمانده‌ی معظّم کل قوا بدین شرح است:
✏️
بسم الله الرحمن الرحیم
سردار سرتیپ پاسدار احمد وحیدی
نظر به شهادت پرافتخار و سرافرازانه‌ی سردار سپهبد پاسدار محمّد پاکپور به دست دشمن صهیونی-آمریکایی، و با عنایت به خدمات شایسته و تجارب ارزنده‌تان، جناب‌عالی را با اعطای درجه‌ی سرلشکری به سِمت
فرمانده کل سپاه پاسداران انقلاب اسلامی
منصوب می‌کنم.
در شرایطی که نظام مقدس جمهوری اسلامی ایران در مواجهه‌ی راهبردی و سرنوشت‌ساز با استکبار جهانی قرار دارد، تحقق مطالبات زیر مورد انتظار است:
1️⃣
ارتقاء مستمر و همه‌جانبه‌ی توانمندی‌ها به منظور بازدارنگی حداکثری، و آمادگی هوشمندانه برای اجرای عملیات تهاجمی پرقدرت علیه دشمن
2️⃣
اعتلای فرهنگی در سازمان سپاه و تقویت تقوا، بصیرت و روحیه‌ی انقلابی به عنوان گوهر درونی آحاد پاسداران و فرماندهان
3️⃣
گسترش مدیریت و فرماندهی برخوردار از بنیه‌ی معنوی و علمی و مهارت‌های نوین در سلسله مراتب سازمانی
امید است در ظلّ ادعیه و شفاعات سرورمان (عجل الله تعالی فرجه الشریف) توفیقات مضاعف و فتوحات پی‌‌درپی نصیب همه‌ی نیروهای مسلح نظام مقدس جمهوری اسلامی ایران گردد.
✍
سیّدمجتبی حسینی خامنه‌ای
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/680050" target="_blank">📅 19:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680049">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب امیر سرتیپ کیومرث حیدری به سِمت جانشین رئیس ستاد کل نیروهای مسلح
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی امیر سرتیپ کیومرث حیدری را به سِمت
جانشین رئیس ستاد کل نیروهای مسلح
منصوب کردند.
🔻
متن حکم فرمانده‌ی معظّم کل قوا بدین شرح است:
✏️
بسم الله الرحمن الرحیم
امیر سرتیپ کیومرث حیدری
نظر به تعهد، شایستگی و تجارب ارزنده‌تان، و به پیشنهاد رئیس ستاد کل، شما را به سِمت
جانشین رئیس ستاد کل نیروهای مسلح
منصوب می‌کنم.
کمک به ارتقای توانمندی‌های دفاعی و امنیتی، تقویت بنیه‌ی معنوی و روحیه‌ی جهادی نیروهای مسلح جمهوری اسلامی ایران، و توجه به نیازهای معیشتی نیروها، با لحاظ نظر رئیس ستاد کل نیروهای مسلح، مورد انتظار است.
امید است توجهات و ادعیه سرورمان (عجل الله تعالی فرجه الشریف) موجب توفیقات روزافزون شما و آحاد نیروهای مسلح گردد.
✍
سیّدمجتبی حسینی خامنه‌ای
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/680049" target="_blank">📅 19:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680048">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب سرلشکر علی عبداللهی به
سِمت رئیس ستاد کل نیروهای مسلح
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده معظّم کل قوا در حکمی سردار سرلشکر پاسدار علی عبداللهی را به سِمت رئیس ستاد کل نیروهای مسلح منصوب کردند.
🔻
متن حکم فرمانده‌ی معظّم کل قوا بدین شرح است:
✏️
بسم الله الرحمن الرحیم
سردار سرلشکر خلبان پاسدار علی عبداللهی
نظر به شهادت پرافتخار و سرافرازانه‌ی امیر سپهبد شهید سیدعبدالرحیم موسوی به دست دشمن صهیونی-آمریکایی، و با عنایت به خدمات شایسته و تجارب ارزنده‌تان، جناب‌عالی را به سمت
رئیس ستاد کل نیروهای مسلح
منصوب می‌کنم.
تحقق حداکثری مطالبات زیر مورد انتظار است:
1️⃣
ارتقاء توانمندی و آمادگی‌های همه‌جانبه و روزآمد دفاعی-امنیتی نیروهای مسلح و بسیج مردمی
2️⃣
فراهم‌سازی امکان پاسخگویی به‌موقع، انقلابی و مؤثر به هر سطح و نوع از تهدیدات متعارف و نوین نظامی، شناختی، و ترکیبی علیه نظام مقدس جمهوری اسلامی ایران
3️⃣
تکمیل روند ادغام ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم الانبیاء(ص) مبتنی بر تدبیر امام شهید (رضوان الله تعالی علیه)
امید است با عنایات الهی و در ظلّ ادعیه‌ی پر خیر و برکت سرورمان (عجل الله تعالی فرجه الشریف) مزید توفیقات و انواع فتح و ظفر برای همه‌ی نیروهای مسلح نظام اسلامی حاصل گردد.
✍
سیّدمجتبی حسینی خامنه‌ای
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/680048" target="_blank">📅 19:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680047">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-text">با صدور احکامی جداگانه از سوی فرمانده کل قوا صورت گرفت؛
📝
انتصاب شش فرمانده عالی‌رتبه در ستاد کل نیروهای مسلح، سپاه پاسداران و بسیج مستضعفین
💬
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده معظم کل قوا، با صدور احکام جداگانه‌ای مسئولیت‌ها و مأموریت‌های شش تن از فرماندهان و مدیران عالی‌رتبه نیروهای مسلح را ابلاغ کردند.
▪️
بر اساس این احکام، سردار سرلشکر خلبان پاسدار علی عبداللهی به عنوان رئیس ستاد کل نیروهای مسلح و امیر سرتیپ کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح تعیین شدند.
▪️
همچنین سردار سرتیپ پاسدار احمد وحیدی با اعطای درجه سرلشکری عهده‌دار فرماندهی کل سپاه پاسداران انقلاب اسلامی شد و سردار سرلشکر پاسدار مصطفی ایزدی مسئولیت جانشینی فرماندهی کل سپاه را بر عهده گرفت.
▪️
در ادامه این احکام، مسئولیت فرماندهی نیروی دریایی سپاه به سردار دریادار پاسدار علی عظمایی و ریاست سازمان بسیج مستضعفین به حجت‌الاسلام والمسلمین حسین طائب محول شد.
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/680047" target="_blank">📅 19:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680046">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18ec1b8e9.mp4?token=MOTEx1YD4n1BrNrFC6J7IKGCREa_QmRpp5MH5PjEjy87PJuTYRmQK3oTyUc7BFOMKAtTlHe60Yd191EE3HxDnb0BrzmGsGI0m4w4AKJUePIQLgO2tqOwu6l5C66x8e9dOXlN4xGkyLCv--MGlYQGjT7srjWPUI-EJUnpOsvwozw3q8CyZzVpWekbltPbYKGD0GaI96fvmmpVu8fw4yviApSN_JLyEiFcrM4u9TDpeYVnFDl-uLv6plpH2pUIVv_x-k0fObu0qRWHJq6eh4YSPhGoF4MtdGylLaNcpURjz9I8BZ2kGQ-f7oH-WgjOI6CgEFmQuW4A7fc6n6j-aJa7Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18ec1b8e9.mp4?token=MOTEx1YD4n1BrNrFC6J7IKGCREa_QmRpp5MH5PjEjy87PJuTYRmQK3oTyUc7BFOMKAtTlHe60Yd191EE3HxDnb0BrzmGsGI0m4w4AKJUePIQLgO2tqOwu6l5C66x8e9dOXlN4xGkyLCv--MGlYQGjT7srjWPUI-EJUnpOsvwozw3q8CyZzVpWekbltPbYKGD0GaI96fvmmpVu8fw4yviApSN_JLyEiFcrM4u9TDpeYVnFDl-uLv6plpH2pUIVv_x-k0fObu0qRWHJq6eh4YSPhGoF4MtdGylLaNcpURjz9I8BZ2kGQ-f7oH-WgjOI6CgEFmQuW4A7fc6n6j-aJa7Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات مشق‌نویس؛ از نسخه اول تا نسخه چهارم
🔹
رباتی که متن را با دستخط شبیه‌سازی‌شده روی دفتر می‌نویسد و صفحه را ورق می‌زند، حالا به نسخه چهارم رسیده است.
🔹
هدف سازنده، ساخت دستگاهی است که با کمک ابزارهایی مانند ChatGPT پاسخ تکالیف را تولید و با دستخط کاربر بنویسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/680046" target="_blank">📅 19:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680045">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp9LF_mgDM6YnaZ3CrE5Zfr7BkRHLBKP7_cB_Sn9EpWkvnUpN-Sw4aOk8hEOLqYHuPuXH-Hti7CoDGgSnlKTuzXeUqSSHOrQ1T4cUMBxUjbcU0CmqAfaJd_KPP1uT5YSZpWGK25tsjRr-bEVFiwKfujKOLvVELGmaW1z56JBz3BQ1U5MDSqABWqgHtVyHe9UXLGW4K4j63JDMlN0Z8uXA_juWuGKdpcE95AlY3VT55aLkXRoFFJ5LM5Xmf600DMqAZtQW_0w26iIFpwsV7vgN3Xgc2VpINU6r1nPx7o9FHYgbx1-v8uunQqZAse5sXOOKBbMMkNbmcL0fdNG2zmdLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون قرعه کشی، 50 دلار برنده شو
🎉
۵۰ تتر سرمایه معاملاتی، برای کاربران جدید ورسلند که باهاش می‌تونی  ترید کنی و سودش رو برداشت کنی
💸
🔻
فقط کافیه ثبت نامت رو تکمیل کنی و به صورت آنی، 50 تتر رو دریافت کنی
🔸
بدون قرعه‌کشی
🔸
بدون واریز اولیه
همین الان ثبت نام کن و از 50 دلارت استفاده کن
👇
🔗
ثبت نام در 5 دقیقه
🆔
https://t.me/versland_io
🆔
https://t.me/versland_io</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/680045" target="_blank">📅 19:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680044">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJNQC_4UpD_s0UJYKzXHIVy-PzLBqcgCOHDDGdajdJfd4HgHY5vkBWeZfiPAcHrKhnoqtYph_-cFUcoWC8g-7GO4-hCZeTQvyTcpxpZv5qIS5QeTnNlE47cpiSGePTNaVZ19W1avohzlaq7gknEcPYWN6hGJPWwQ481MOV5HtbADGTkDOkibpnBpfBAzs0myHLM-knXp8D0loDtocWGvi-P3V2fUAIa-dTCQzNZyrpn5zmacw1uBukOGApY1SeHiQGGTAFbG_iu02YmWLQP0afVPxkRFqf6rF4p6xxGinKloF6bmMrpA2YLq4_Vfl25mVFoVjUccCTj8vj2v7Zd5jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
انواع ست ورزشی مردانه با قیمت تولیدی رسید
🔥
اگه دنبال یه ست شیک، راحت و باکیفیت هستی، این مدل‌ها رو از دست نده
👕
✅
کیفیت بالا و دوخت حرفه‌ای
✅
قیمت مناسب بدون واسطه
✅
پرداخت درب منزل
🚚
برای مشاهده مدل‌ها و ثبت سفارش کلیک کنید
👇
https://khabarfouritel.affdn.com/productsList/default_affdn_set_men_off
انتخاب‌های بیشتر با پرداخت درب منزل رو ببین
👇
https://khabarfouritel.affdn.com</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/680044" target="_blank">📅 19:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680043">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
زمین‌لرزه‌ای به بزرگی ۴.۷ ریشتر در مرز استان‌های خوزستان، ایلام و لرستان و حوالی حسینیه به وقوع پیوست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/680043" target="_blank">📅 18:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680042">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72e3762d0b.mp4?token=FdYR6H_3Jxb3sHnive6AG3Sk8ImiU0RA7KbsyY3CaOTngbFFiq8Im5gZB8boqh-sWzYT8k8csCBnZWcEii2qClg4iafAoxBOSIzW9a6o0CWV61Y3RRbUfrYja1T7GjPG4m1IgbxuQ5ucIrbrgw_AsP4_PA8NRNre4FQ7kdSfr09fR0crnjkdDswzx-_9PuAFZ1HRCfgkp3bxbjv9IvhSR1d7GThc2bfWKzDrSktDmjz2zXd9BHD-2ymYNZqkI5oeGfM3PSKVTOFUXrS6jBltEimPnkt9S0qLBF86mHdyrXPBlLvdb7LyXNH2JUJnLwxhcpBnh2ta8KRS74ZKbHuj9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72e3762d0b.mp4?token=FdYR6H_3Jxb3sHnive6AG3Sk8ImiU0RA7KbsyY3CaOTngbFFiq8Im5gZB8boqh-sWzYT8k8csCBnZWcEii2qClg4iafAoxBOSIzW9a6o0CWV61Y3RRbUfrYja1T7GjPG4m1IgbxuQ5ucIrbrgw_AsP4_PA8NRNre4FQ7kdSfr09fR0crnjkdDswzx-_9PuAFZ1HRCfgkp3bxbjv9IvhSR1d7GThc2bfWKzDrSktDmjz2zXd9BHD-2ymYNZqkI5oeGfM3PSKVTOFUXrS6jBltEimPnkt9S0qLBF86mHdyrXPBlLvdb7LyXNH2JUJnLwxhcpBnh2ta8KRS74ZKbHuj9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افعی شاخدار دم‌عنکبوتی، یکی از عجیب‌ترین نمونه‌های فرگشت
🔹
انتهای دمش شبیه عنکبوته و با حرکت دادنش پرنده‌ها رو به دام می‌اندازه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/680042" target="_blank">📅 18:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680041">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/958354fbb3.mp4?token=Wjt8TUST1wjvH4ka25GLuzgf_RJMIvTK_LjrZejwAN-MpMxr7wMbj1_2OfnpuQ2LEuzGx3RyaNXDn6lZS5BGnWXDEAbKqQEPHve8PNfCzcYKPyWlNmS-PqeVT4KJdYrC7Kd9o9FntLMEZNJHXzqrJWrLZN-l-BG8EmLsRAz-HDPyKulLtTSIlz6g3YyXxwOU0GK4SeFtPVz-v1ax3Z5XSPlM4c1cYK9mcaNxL_fk4TBpppwl-dfurnyf8t31BNwW4hKA7etZqk7la7NYtneMZkSpD8V2oPCQ58MmhnqXsqfu1ugmTPzqEzg5-Uwmd0ZNp0m-xnVKNOzR7Skvi8-Th5bBANWfe7evN7urMp1H6VFZJdIw7QZnVlClNWgNfSR0HYsS49hl8izDJ2ukVV5X8DLx5-75Y6Hg-_e9HDmZRMOY-oYTE_QKoh8ue0f_bPVEnb5MRMdY-1dpJdP9_6pKltUJNPPPWsLv-U4djnISGPPsLw9CWcPvr4YLVJku-0jv5qWwsVOpoUp0Euig1LGZgsOCKETWp-qR3YWJKOEYF54fgO-Y6RzGtf_qGOkenNfRy3wu7u39DLTduHHAFY8YVeonRX8HgxXocFeTuvj-I-flJBMEVN-uWMhUcCc-BuXBN695mUao047Y-K6z9-qfuu-ESVA0b-pWS9fT2qP0ibo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/958354fbb3.mp4?token=Wjt8TUST1wjvH4ka25GLuzgf_RJMIvTK_LjrZejwAN-MpMxr7wMbj1_2OfnpuQ2LEuzGx3RyaNXDn6lZS5BGnWXDEAbKqQEPHve8PNfCzcYKPyWlNmS-PqeVT4KJdYrC7Kd9o9FntLMEZNJHXzqrJWrLZN-l-BG8EmLsRAz-HDPyKulLtTSIlz6g3YyXxwOU0GK4SeFtPVz-v1ax3Z5XSPlM4c1cYK9mcaNxL_fk4TBpppwl-dfurnyf8t31BNwW4hKA7etZqk7la7NYtneMZkSpD8V2oPCQ58MmhnqXsqfu1ugmTPzqEzg5-Uwmd0ZNp0m-xnVKNOzR7Skvi8-Th5bBANWfe7evN7urMp1H6VFZJdIw7QZnVlClNWgNfSR0HYsS49hl8izDJ2ukVV5X8DLx5-75Y6Hg-_e9HDmZRMOY-oYTE_QKoh8ue0f_bPVEnb5MRMdY-1dpJdP9_6pKltUJNPPPWsLv-U4djnISGPPsLw9CWcPvr4YLVJku-0jv5qWwsVOpoUp0Euig1LGZgsOCKETWp-qR3YWJKOEYF54fgO-Y6RzGtf_qGOkenNfRy3wu7u39DLTduHHAFY8YVeonRX8HgxXocFeTuvj-I-flJBMEVN-uWMhUcCc-BuXBN695mUao047Y-K6z9-qfuu-ESVA0b-pWS9fT2qP0ibo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوخی علی مطهری با شایعات استعفای رئیس‌جمهور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/680041" target="_blank">📅 18:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680040">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
روایت نیویورک‌تایمز از بمباران زیرساخت‌های غیرنظامی جنوب ایران
نیویورک‌تایمز:
🔹
حملات آمریکا در جنوب ایران تونل‌ها، بنادر، راه‌آهن، اسکله‌های ماهیگیری، کارخانه‌ها و تأسیسات آب‌شیرین‌کن را هدف قرار داده است.
🔹
این حملات فعالیت ماهیگیری را تقریباً متوقف کرده و یک بمب ۲ هزار پوندی آمریکا نیز در منطقه‌ای مسکونی در روستای چه‌تنگو فرود آمده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/680040" target="_blank">📅 18:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680038">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPytvPOpQEB4Tuga766wkochsCaXLH0C4epzjd0ooNMlZFPjgtTz-IpygA0Ah2MLqdJQwx3T_geniH1M825I_NnDExxQRBD0cff7FPY3KytN3uW9F1FiwL3J2y-TgeG58g9C2ZHP6Zk3T_52jTc5oQebLAiHvN2iC6BVx8PTlXHQ7P3PGKtByc1xqZ-UP3Mecu-K4o-jzHIEPUCTLH7PRr0-CmmEhBwPdoIhJXqIDUZwo1lmiao4iIsstQyroeT8M4N7mMjTdnJ_RDLBCcKHX_0xv-I0P4N0gst6L0TK78M-3n_rgmsPunDYcfIbZiCSP4wbXubV53smSWXv8MG55g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تا ساعتی دیگر منتشر خواهد شد؛
احکام انتصاب تنی چند از فرماندهان بلندپایه نظامی جمهوری اسلامی ایران توسط فرمانده معظم کل قوا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/680038" target="_blank">📅 18:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680037">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae89fdc1e.mp4?token=Oo7GOcKkhRTXbVzsSFM516Uq_wEyPeoDzq-ovmTxzIIpVO8aBsDJoyLSfVo8sFNJTU9QwQta5xAArwY3ozT00Y6BMWq7AhLCGP68jYWEQk7nSif8Ve-lJta8GQjUV5c7cJJRq-dxnRLsSBCF-FxafrWypApGaK86T6r496D0VOH_y0YnFwk79YwseE1BoppvAgrfQhjPiPSMkc1C9hB8J0ibhjqHA3S5YO-P22_cgADVb7YB2Gi-aRy4kHS2MIz_lnZxFTZBKxEyU-sfadPIzrIPpjBiGMDankrpc_fcOLj_utX7S7e3QrT2GFFrpLajwnrWgDgY5dofZ7UyYzzgtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae89fdc1e.mp4?token=Oo7GOcKkhRTXbVzsSFM516Uq_wEyPeoDzq-ovmTxzIIpVO8aBsDJoyLSfVo8sFNJTU9QwQta5xAArwY3ozT00Y6BMWq7AhLCGP68jYWEQk7nSif8Ve-lJta8GQjUV5c7cJJRq-dxnRLsSBCF-FxafrWypApGaK86T6r496D0VOH_y0YnFwk79YwseE1BoppvAgrfQhjPiPSMkc1C9hB8J0ibhjqHA3S5YO-P22_cgADVb7YB2Gi-aRy4kHS2MIz_lnZxFTZBKxEyU-sfadPIzrIPpjBiGMDankrpc_fcOLj_utX7S7e3QrT2GFFrpLajwnrWgDgY5dofZ7UyYzzgtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین تصاویر ماهواره‌ای از تنگه هرمز
🔹
با وجود ادعای ترامپ درباره باز بودن و کنترل تنگه هرمز، پایش‌های دریایی از کاهش محسوس تردد کشتی‌ها خبر می‌دهند؛ روز یکشنبه ۹ کشتی کمتر از جمعه از تنگه عبور کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/680037" target="_blank">📅 18:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680036">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52c4a7ad6a.mp4?token=udP38rW7efuf950_Qb0kXA1GXRxoZ9Xka78wDAhwceTyknMBo0XrprdUIQn4C9sI2HbmB7EpWEWCgQ2EDYogwZX0ZOg7b4lFgG7PCZrFrEIm53WW9V5Lq1pGxbnO8YvBr3qm-rkbZnJdLUJGK7zoSfIs1ppE4ne3G_1aH2Tg6YW3agK5PVHZBuyuOwY0ioa9E6bGu2epKubxIdh0ONetTX8JfZ5nEUMMdfetiTKlL6mkcwzx0GxdgiI2vU2K7uWHtJkUOUcMM0n4SaunNDX4Z4iBsQmOa23WSfIOS0j0Ccw_SUqfRNsFsWwaANvv1v6NePzSCZEGDn_iFfsL3f2Q4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52c4a7ad6a.mp4?token=udP38rW7efuf950_Qb0kXA1GXRxoZ9Xka78wDAhwceTyknMBo0XrprdUIQn4C9sI2HbmB7EpWEWCgQ2EDYogwZX0ZOg7b4lFgG7PCZrFrEIm53WW9V5Lq1pGxbnO8YvBr3qm-rkbZnJdLUJGK7zoSfIs1ppE4ne3G_1aH2Tg6YW3agK5PVHZBuyuOwY0ioa9E6bGu2epKubxIdh0ONetTX8JfZ5nEUMMdfetiTKlL6mkcwzx0GxdgiI2vU2K7uWHtJkUOUcMM0n4SaunNDX4Z4iBsQmOa23WSfIOS0j0Ccw_SUqfRNsFsWwaANvv1v6NePzSCZEGDn_iFfsL3f2Q4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکورد ماهی صید شده با دو متر و ۱۲ سانتی‌متر شکسته شد
🔹
ماهیگیران روسیه یک ماهی تن به طول ۲ متر و ۱۲ سانتی‌متر در خلیج پتر کبیر صید کردند که رکورد رسمی این منطقه محسوب می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/680036" target="_blank">📅 18:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680035">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: قرار است در تنگه هرمز خدماتی به کشتی‌ها دهیم و به ریال هم عوارض دریافت کنیم
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
با وجود اینکه قسمت عمده‌ای از تنگه هرمز سرزمین ماست، اما محل تامین تجهیزات نظامی بر علیه کشور ما بوده است.
اگر دنیا و کشورهای همسایه بخواهند علیه کشور ما اقدامی انجام بدهند، باید جایی باشد که آنها را مدیریت کنیم و آنجا هم تنگه هرمز است.
🔹
یک طرح ده ماده‌ای برای اعمال حاکمیت ایران بر تنگه هرمز در مجلس بررسی شد و اعلام وصول هم شده است.
🔹
به هیچ عنوان امکان برگشت تنگه هرمز به شرایط قبل وجود ندارد. هزینه انتقال کالا از مسیرهایی غیر از تنگه هرمز زیاد است.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/680035" target="_blank">📅 18:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680034">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YT0U7eVjbEjnptcWRtsBj32sNvdWyqiHb4MaNze_cKuP29hmlbWCwfEIeEAw61Y-zFYl88gia1aEu_85DMkKFRwEga2huhKEO1CUsU2qFFcQqibN1VTYkeAklCVbXiw9rdNi64NdvvkO3vBhxbxgdsj3htweunT_m3Vrx-I1jfS_v-WK-I6XrJwTk9ODWmU3pFDQmwxFhS2W2MknIjN78gge1bauI-qVd2Si7wzjN7OLFE1YnhIX-VuVdqUTAjdJp6CZeSagR1H2Ttgx84WpjVE0r9ECLvnVa8_O6UjHytfuDuvrITiII4D-7XSsrC7hvKfsOjOlrMsHMcEnzGBmUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاعری که عشق را به زبان جان ترجمه کرد؛ مولوی
🔹
جلال‌الدین محمد بلخی، معروف به مولوی، از بزرگ‌ترین شاعران و عارفان جهان است. آثار او، به‌ویژه «مثنوی معنوی» و «دیوان شمس»، قرن‌هاست انسان‌ها را به عشق، خودشناسی، رهایی از ظاهر و رسیدن به حقیقت دعوت می‌کند. ویژگی‌های…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/680034" target="_blank">📅 18:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680033">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxaPKdEE6sLlNJC99oZt2l1YgpUYxZCQowUE3dRrDisykM83zQ91ykxHG1CktqO3n4_3FK96A04TsHGhVDpIDpjQyCAKLLdOFcxy2g42-7nztfk-s_kj7L01WKsbMOEFaXw9XApwNVo8K0eFQXjQuzVtuYbQktNrlUdnutRy9hgfVuMZAvXYspcNEZfDqsKYbyWMMytsFhfXEVFXoZjCGN2gcwRh_Etjx5VbUF6GkEiVcn5pmnL4CG2OOYGOr3TOapfsTXAXCezRh2AGrwavqmjmhHXhmjcGGyLntWVFZ0ufvP2v-9XPNgb16gHqVJViqXwpZeHwO6h6GBWNdSvZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون نیاز به چک‌وضامن و در عرض یک دقیقه
ملّی‌گلد امکان خرید اقساطی طلا تا سقف یک میلیارد تومان را فراهم کرد
ملّی‌گلد در راستای توسعه خدمات خود، امکان خرید اقساطی طلا تا سقف یک میلیارد تومان را برای کاربران خود فراهم کرد. این مجموعه همچنین سقف وام آنی نقدی با پشتوانه طلا را از ۵۰ میلیون تومان به ۱۵۰ میلیون تومان افزایش داده است.
در سرویس خرید اقساطی ملّی‌گلد، کاربران می‌توانند در یک بازه زمانی بسیار کوتاه،‌ تا سقف یک میلیارد تومان، به صورت اقساطی طلا بخرند؛ این سرویس بدون نیاز به چک و ضامن ارائه می‌شود و کاربران می‌توانند با انتخاب بازه‌های زمانی ۱۲ یا ۱۸ ماهه، برنامه بازپرداخت خود را انتخاب کنند.
در این مدل، طلای خریداری‌شده با قیمت زمان خرید محاسبه شده و تا زمان تسویه کامل اقساط نزد ملّی‌گلد نگهداری می‌شود. پس از پایان دوره بازپرداخت، طلای خریداری شده با نرخ روز به کیف‌پول منتقل می‌شود و کاربران می‌توانند آن را به صورت آنلاین نگه دارند یا به صورت فیزیکی تحویل بگیرند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/680033" target="_blank">📅 18:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680032">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای جدید از آتش‌سوزی در پالایشگاه نفت جیزان شرکت آرامکوی عربستان سعودی پس از حمله انصارالله یمن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/680032" target="_blank">📅 18:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680031">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/680031" target="_blank">📅 17:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680030">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bce5f4670.mp4?token=aKuaKqrPywgwAgFtj0rgl8zi4KWU6rhhy5k0QQTXhgK7jsp567fWqRZa8l8-hz373_psLUjQjpOCsEd8j1nYzdm_t9apTqj3_TmvMKNnFyRe9TLN9xCUX1R5khGEBIH38DlpWT4PFugU4-2oE8BjNhM3l-BlmkRgpv4-R4vtqiifGgUo8GJo7fP7UUJjuD8_hsRn3PszvfT_fosvkeKg0Hm1i4LrBvhASmNsaU2CbPazInNB3XYm36MvXmSOj0Q1NfCnhrEmfBr-q3hngEC3HLRvXW3gngushW-PEUlcvTRPLHQGqy-s6yIyA2IkCMKMkpgILvc4jUowQ1p3y92-vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bce5f4670.mp4?token=aKuaKqrPywgwAgFtj0rgl8zi4KWU6rhhy5k0QQTXhgK7jsp567fWqRZa8l8-hz373_psLUjQjpOCsEd8j1nYzdm_t9apTqj3_TmvMKNnFyRe9TLN9xCUX1R5khGEBIH38DlpWT4PFugU4-2oE8BjNhM3l-BlmkRgpv4-R4vtqiifGgUo8GJo7fP7UUJjuD8_hsRn3PszvfT_fosvkeKg0Hm1i4LrBvhASmNsaU2CbPazInNB3XYm36MvXmSOj0Q1NfCnhrEmfBr-q3hngEC3HLRvXW3gngushW-PEUlcvTRPLHQGqy-s6yIyA2IkCMKMkpgILvc4jUowQ1p3y92-vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از لحظه کشف خیانت تا تصمیم نهایی، چه باید کرد؟/
تلویزیون اینترنتی مدار
برنامه کامل مُدارا را تماشا کنید
👇
https://youtu.be/4127WFofp-M?si=05Z3uS5Mhr--u9Vb
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/680030" target="_blank">📅 17:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680029">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
جهش ۸ درصدی قیمت گاز در اروپا
🔹
قیمت گاز در بازارهای اروپایی با افزایشی ۸ درصدی روبرو شد که ناشی از ابهام در سرنوشت مذاکرات پیرامون بازگشایی و امنیت تردد در تنگه هرمز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/680029" target="_blank">📅 17:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680026">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28de48ce92.mp4?token=J4KaeBzxRTOdBrtxnkWdGpX0bE3c51FewYR2mmJKu59X0ST0xTNgSNY2COIrSXE7MmJcvIqlo31Gy7ANV31cjKhrhLu7p4IO5bFuqAtzrwRI8thDH7bwe5QnEfl59eTJSQXM0geuKwegIJBnF0tNLDlOoq5df94G6TPKQK7hU4uhGh9dcdFO6UnkHWUTRYpH3ZNLA8qdoYrl5VZw8-lVs_7cB4NjnDY-hxMnsSY3IHLQzhLCd5lwMupolAPB6h5B4xRU_mfl7kQK2dJb66-ixmFtLsNw9R3IY8FZ7FHwhm22hufjuDm70KwWWbYkyr1yAgmlWdMUKL6OLBF4FdK7hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28de48ce92.mp4?token=J4KaeBzxRTOdBrtxnkWdGpX0bE3c51FewYR2mmJKu59X0ST0xTNgSNY2COIrSXE7MmJcvIqlo31Gy7ANV31cjKhrhLu7p4IO5bFuqAtzrwRI8thDH7bwe5QnEfl59eTJSQXM0geuKwegIJBnF0tNLDlOoq5df94G6TPKQK7hU4uhGh9dcdFO6UnkHWUTRYpH3ZNLA8qdoYrl5VZw8-lVs_7cB4NjnDY-hxMnsSY3IHLQzhLCd5lwMupolAPB6h5B4xRU_mfl7kQK2dJb66-ixmFtLsNw9R3IY8FZ7FHwhm22hufjuDm70KwWWbYkyr1yAgmlWdMUKL6OLBF4FdK7hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات اولیه زلزله ۷.۴ ریشتری کلمبیا
🔹
سازمان زمین‌شناسی آمریکا از وقوع زمین‌لرزه‌ای به بزرگی ۷.۴ ریشتر در کلمبیا خبر داد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/680026" target="_blank">📅 17:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680025">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
حمید رسایی: مگر منصوب رئیس جمهور می‌تواند مجلس را تعطیل کند؟! جایگاه حقوقی دبیر شورای عالی امنیت ملی در جایگاهی نیست که بتواند مجلس را تعطیل کند
نایب رئیس مجلس:
🔹
مصوبات شعام پیش از ابلاغ به استحضار رهبر انقلاب می‌رسد اما در نهایت با امضای دبیر شعام ابلاغ می‌شود
🔹
ما سر هر موضوع و مصوبه‌ای نمی‌پرسیم آیا به استحضار رهبر انقلاب رسیده است یا خیر؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/680025" target="_blank">📅 17:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680024">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904a9af188.mp4?token=cU3Z3wDWl9rGL477vlQzM_NEbJpe1xi_KRqa99NLFLHlDeSjSf5yIeKKDg1IEHQgzMhCqic8hKFGuTiAB9Zn3EwOFaZf_e5R2OW08GaZh7LQ3YXc7iqCgl8Dg4axWrb5znzKB-gdMtr69qTcq2tc1TmA4MviMMrOQfTWb2pVCJ1o0xDNvE86rbPYdBnW7gWTUmGcVLrJe63MFR9NMQLof7q56VQBK2-bFfg3pnTV-vGIOFgcZfb10IvATU04wleNKv5gjeVm1Mo9vrbhs5zsDowZsZD-__Qs83nQJGMNQLIAajVrEaoK_31qGckIrdQfwgdxWLUdnEjCySXVy5h8GxKZxR2CMghLTHOvqWUU6fal3_XqwIrA3UrxCxW4N5ag1mHHfV3FBIa0YQu4ynECCgt4BUIobm0rklQOV9U_j6RsMsL5eKlctVCY3A1LkNmvqmD9Q4YMd3foCBjDzY_e8U6PQdo3YMpRzzMTBX7rBJqXBvJORYCTG5JaWHNHjle7VcurnmVsAHDXrJx5sZi5YleFNp4XLTIX4R4JvSYFi8CPR97prt45I4v4faj3LoO30kqV7t0enhAeT7r9rD1ipBAMEQs9dLFX4_jS1xyRAm8EKVc5ES6qAKnkUDwkhZp9C_Dejb2D0B_XJHnTA60qT-7x2cbiSKgmeVOgIDhpYto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904a9af188.mp4?token=cU3Z3wDWl9rGL477vlQzM_NEbJpe1xi_KRqa99NLFLHlDeSjSf5yIeKKDg1IEHQgzMhCqic8hKFGuTiAB9Zn3EwOFaZf_e5R2OW08GaZh7LQ3YXc7iqCgl8Dg4axWrb5znzKB-gdMtr69qTcq2tc1TmA4MviMMrOQfTWb2pVCJ1o0xDNvE86rbPYdBnW7gWTUmGcVLrJe63MFR9NMQLof7q56VQBK2-bFfg3pnTV-vGIOFgcZfb10IvATU04wleNKv5gjeVm1Mo9vrbhs5zsDowZsZD-__Qs83nQJGMNQLIAajVrEaoK_31qGckIrdQfwgdxWLUdnEjCySXVy5h8GxKZxR2CMghLTHOvqWUU6fal3_XqwIrA3UrxCxW4N5ag1mHHfV3FBIa0YQu4ynECCgt4BUIobm0rklQOV9U_j6RsMsL5eKlctVCY3A1LkNmvqmD9Q4YMd3foCBjDzY_e8U6PQdo3YMpRzzMTBX7rBJqXBvJORYCTG5JaWHNHjle7VcurnmVsAHDXrJx5sZi5YleFNp4XLTIX4R4JvSYFi8CPR97prt45I4v4faj3LoO30kqV7t0enhAeT7r9rD1ipBAMEQs9dLFX4_jS1xyRAm8EKVc5ES6qAKnkUDwkhZp9C_Dejb2D0B_XJHnTA60qT-7x2cbiSKgmeVOgIDhpYto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حمله آمریکا به اداره پست آذرشهر در ۱۹ اسفند
#اخبار_اذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/680024" target="_blank">📅 17:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680023">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/111e8c1034.mp4?token=L5Ky80QaJumaRXMM7Pg_4lex_tY1Fbz2U1p8mJmhQdOLh7v4DfE05H_cXFx974F-vigWyo-gTY-XAa570RIRwFvQeBmzzAUizdMejrIr-KqjrVVIyodZ-xlipJxZCTq2aQ1tG5kA50boI7dhzo1yS4b9dWpOp8ntUEIHsdCzUk87w3pO3WMeNfXUdyWOGm5tUQflbB3Y5tOpZJgoKm0Iu1EsHJvAOcBW7Y5vI5Y5nT36gwJ3C11oujUPZ3CnNYTedhUE72hc7LCdbTj4k_Try-lw_OfKafY-RVNTdPJvvpuKl0gsItYkfjc_6QdSzjdKBgqrYiWMfsChyKboToQC4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/111e8c1034.mp4?token=L5Ky80QaJumaRXMM7Pg_4lex_tY1Fbz2U1p8mJmhQdOLh7v4DfE05H_cXFx974F-vigWyo-gTY-XAa570RIRwFvQeBmzzAUizdMejrIr-KqjrVVIyodZ-xlipJxZCTq2aQ1tG5kA50boI7dhzo1yS4b9dWpOp8ntUEIHsdCzUk87w3pO3WMeNfXUdyWOGm5tUQflbB3Y5tOpZJgoKm0Iu1EsHJvAOcBW7Y5vI5Y5nT36gwJ3C11oujUPZ3CnNYTedhUE72hc7LCdbTj4k_Try-lw_OfKafY-RVNTdPJvvpuKl0gsItYkfjc_6QdSzjdKBgqrYiWMfsChyKboToQC4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حدادعادل: کسانی‌که هنوز در رویای دوران انتخابات هستند اشتباه می‌کنند؛ وقتی که کشور در معرض خطر است چه اصولگرا و چه اصلاح‌طلب باید به دولت کمک کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/680023" target="_blank">📅 17:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680022">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
رئیس پژوهشگاه رویان: اروپایی‌ها ایران را برای درمان ناباروری انتخاب می‌کنند
شاهوردی، رئیس پژوهشگاه رویان:
🔹
پیش از چالش‌های یک سال تا یک سال و نیم اخیر، سالانه بیش از ۵۰۰ زوج نابارور خارجی در پژوهشگاه رویان پذیرش می‌شدند.
🔹
بیماران مسلمان از کشورهای اروپایی، از جمله انگلیس، برای درمان ناباروری به ایران مراجعه کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/680022" target="_blank">📅 17:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680021">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
«توافق مکه»؛ نام پیمان سه‌جانبه نظامی ترکیه-عربستان-پاکستان
🔹
همزمان با برگزاری نشست سران ترکیه، عربستان سعودی و پاکستان در جده، گزارش‌ها حاکی است که پیمان دفاعی سه‌جانبه‌ای که قرار است امروز میان این سه کشور امضا شود، به طور رسمی «توافق مکه» (Mecca Agreement)…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/680021" target="_blank">📅 17:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680020">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cad9612af.mp4?token=Yt31narOd5Fu9sftic5W6gmJno7EoKfYSuSfI7H0BDYaHTdNw8qCbRJFOUZrct0oBp20RyV2lyTNQppgVvBVKbjM2LOQ6DDapmDdLNKSGJcgb1b0yNhvgOoVXHL31-zt5DWoYBHoTs_4ME5kPVGpuzSpFh6j9kLUwoT55xQQ6-ZifR2lXX4RhqOQQhtzFJideIpXDjAOfB3q6_JzOqULxuSWqiMLv60W-PRG3ooCYN5WbTrcijoumQLbfJ9fdNo4JdN4gF3rMqaJp5DT3RI6EeWv7ZbDvXxj2UpRv6BledUbIyzihorOBivr7TgXRYeH4sGFa6Cvd9HhKYNWG9RynjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cad9612af.mp4?token=Yt31narOd5Fu9sftic5W6gmJno7EoKfYSuSfI7H0BDYaHTdNw8qCbRJFOUZrct0oBp20RyV2lyTNQppgVvBVKbjM2LOQ6DDapmDdLNKSGJcgb1b0yNhvgOoVXHL31-zt5DWoYBHoTs_4ME5kPVGpuzSpFh6j9kLUwoT55xQQ6-ZifR2lXX4RhqOQQhtzFJideIpXDjAOfB3q6_JzOqULxuSWqiMLv60W-PRG3ooCYN5WbTrcijoumQLbfJ9fdNo4JdN4gF3rMqaJp5DT3RI6EeWv7ZbDvXxj2UpRv6BledUbIyzihorOBivr7TgXRYeH4sGFa6Cvd9HhKYNWG9RynjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: خدمت رهبر انقلاب رسیدیم و از هر دری گفتیم
🔹
ایشان از لحاظ جسمی  در صحت و سلامت کامل بودند؛ ایشان رهنمودهای خود را ارائه فرمودند و  دغدغه‌ها و مشکلات را گفتم و به راحتی سخنانم را گوش دادند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/680020" target="_blank">📅 17:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680019">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/680019" target="_blank">📅 17:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680018">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpSOiM6Ru61MPJX13MCxSeEO3ZtG8GL4UOaIG4k9JlXpub92QA14L3U9XsrTm2aFqW9JP4P29BBfp6nUYtKbAYwZAaDy65gBP9Poj9c0V8xQsbxEYNDhgDMnihgqlVGfr1Ke1QNO2zaYZJChWizXmIvqdejs04ySkJRkxi_1_IH5_bcpfcJA5pRl9yS9MWRu0KknWO1lnyfCn1skyw53iy2jReTZW5HZ4_4wpeaSRCaSMDl6Vo6NOagJs_OOJPTfCiAlWFYnYw65nDCiGOe6sDQW-0lZKQ_8aDZSu85CiiFyiRnO-3JHXny7Ks7TsyqjhGn_z_SCn9KL17xKuFzI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران» / ۴
🔹
عبور سهم از بازار بانک کشاورزی از مرز ۷ درصد پس از ۲۰ سال
🔻
سهم بانک کشاورزی از کل سپرده‌های شبکه بانکی برای نخستین بار طی ۲۰ سال گذشته، در تیرماه ۱۴۰۵ از مرز ۷ درصد عبور کرد.
🔻
سهم از بازار این بانک پس از یک دوره تثبیت در بازه زمانی ۱۴۰۰ تا ۱۴۰۲، روند صعودی به خود گرفته و از ۴.۳۶ درصد در ابتدای سال ۱۴۰۳ به ۴.۵۱ درصد در فروردین ۱۴۰۴ رسید و سپس با عبور از کانال ۶ درصد در پایان سال ۱۴۰۴، در تیرماه ۱۴۰۵ به ۷.۱۷ درصد رسید.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/680018" target="_blank">📅 17:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680017">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f2576f565.mp4?token=YPxQdIA5H7-2R2thSDfajxooIZcyF4_qiA6ZTRQ7TnmvVTduZL6dZ20I4kmaOqKGjDBRvApHbzEknaxdLWZ0Uhek6e2RJ67h0ye9FfrJsvsdHcwfK4cr3SB9NLIJVC99lToc3HgnHI_xhQt797ZcMKRdWOTbHFg-PXAFMYn4GDIDx4eCgXEo5L0FXSzz4y1jQDd3_kUISM3__FPMYLjd1eijaSvDb2OLo6e7HxDMrP4oGSQKeGBgCN7XCAM47f1XXH6i05QP0mIK7F34xQ__kJTdwooitQZccz7M0i5seeQ2gDjyEDdtLQ9-Dme8MnxUsWl58hnbxo8w0yUbSwCBrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f2576f565.mp4?token=YPxQdIA5H7-2R2thSDfajxooIZcyF4_qiA6ZTRQ7TnmvVTduZL6dZ20I4kmaOqKGjDBRvApHbzEknaxdLWZ0Uhek6e2RJ67h0ye9FfrJsvsdHcwfK4cr3SB9NLIJVC99lToc3HgnHI_xhQt797ZcMKRdWOTbHFg-PXAFMYn4GDIDx4eCgXEo5L0FXSzz4y1jQDd3_kUISM3__FPMYLjd1eijaSvDb2OLo6e7HxDMrP4oGSQKeGBgCN7XCAM47f1XXH6i05QP0mIK7F34xQ__kJTdwooitQZccz7M0i5seeQ2gDjyEDdtLQ9-Dme8MnxUsWl58hnbxo8w0yUbSwCBrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات اولیه زلزله ۷.۴ ریشتری کلمبیا
🔹
سازمان زمین‌شناسی آمریکا از وقوع زمین‌لرزه‌ای به بزرگی ۷.۴ ریشتر در کلمبیا خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/680017" target="_blank">📅 16:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680016">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15e2b081d.mp4?token=j6_nKPqtPAqPd4qWHygxFSSVzpCSoel66Az-qrCNxD8qp_scdsOYJS8OQifoS2-pqxHtcR5fZgm2V7xcmcOkTWTeN1p2oqj2lhdn5KDpAtaDtctlR1VWzjZGyTKcK5K8YT2GLlT79DrbxgVZNLk5WPwgV8f9s9gixh5F8g5p8pkQqbh4H9qznsC9FuyQ2ZNckJTjP71RIgXqCxH_HU0z_KD_F4clH_7AjA4JT-18aJ5yNIJRPCEG9Mj4FfK52XFu0LNGqau8t7m0WOjF5RrYhqf2fk6vYCSDMbzHDOWvDFrUJYzht6-siHt35qc8Nv40xy2UV_HQumSOXJ8XhIdLvQrmUoRZcLCR1m8Yu2Bvg_pPtomq-grRsDJNE5NCNvTXfbIzFiURofc9Is3yxRkXmG7K5_EnmiKvmfvs7rSucf9mIQDbJcGUC8pnddmnfjiI0eJ7rByYxDeOukQWmkZoum4lCip1gBYM71L4njyQfZSZBIcGNQPGt4usT6NkedtyTExzt7eE13k9iTBWFfAmLmJiqkaSqUy955oESBWQwgy8S8p3jBZZvn3yhOYaj7KmNP-U-j6PQj9E2CYPuWvNoNnktbF5iAaXoZUt-0fZCEhin-MQj6gF0mzgZBztbU5L_Lq4AuWK74sN18WnR5NdRiJaBiayFwjF07rrbj8Fus8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15e2b081d.mp4?token=j6_nKPqtPAqPd4qWHygxFSSVzpCSoel66Az-qrCNxD8qp_scdsOYJS8OQifoS2-pqxHtcR5fZgm2V7xcmcOkTWTeN1p2oqj2lhdn5KDpAtaDtctlR1VWzjZGyTKcK5K8YT2GLlT79DrbxgVZNLk5WPwgV8f9s9gixh5F8g5p8pkQqbh4H9qznsC9FuyQ2ZNckJTjP71RIgXqCxH_HU0z_KD_F4clH_7AjA4JT-18aJ5yNIJRPCEG9Mj4FfK52XFu0LNGqau8t7m0WOjF5RrYhqf2fk6vYCSDMbzHDOWvDFrUJYzht6-siHt35qc8Nv40xy2UV_HQumSOXJ8XhIdLvQrmUoRZcLCR1m8Yu2Bvg_pPtomq-grRsDJNE5NCNvTXfbIzFiURofc9Is3yxRkXmG7K5_EnmiKvmfvs7rSucf9mIQDbJcGUC8pnddmnfjiI0eJ7rByYxDeOukQWmkZoum4lCip1gBYM71L4njyQfZSZBIcGNQPGt4usT6NkedtyTExzt7eE13k9iTBWFfAmLmJiqkaSqUy955oESBWQwgy8S8p3jBZZvn3yhOYaj7KmNP-U-j6PQj9E2CYPuWvNoNnktbF5iAaXoZUt-0fZCEhin-MQj6gF0mzgZBztbU5L_Lq4AuWK74sN18WnR5NdRiJaBiayFwjF07rrbj8Fus8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت رئیس‌جمهور از دیدار ۷ ساعته خود با رهبر معظم انقلاب و تاکید ایشان بر حفظ وحدت و انسجام ملی و توجه به معیشت مردم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/680016" target="_blank">📅 16:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680015">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YO2WlF3RIFQbgLD2sw_mCxMIGSWKxMfPUeg4PIXwQYU46dWPHxrpDsDjv9bvof_8vzNW77gn9gr3l_7jQ3WliUplQQ3uvluv8tHHHYdFNXefz2Bsoj7M8hIon4QybeKoI00m-ZL7QYkUbpFmJnzlzIrJO3HccieREc8FkUTC7Q9ANMUyWR8tNxm0J-9zcP9bSyizvV_SWV-BqNoe8FKsFXqyIONVezCsKo1EkgGHA70AdJcXMsYkjAX2Bes5pkdxcUhA06C3U2mtWSbsIVzJqJWyXHZsAUQKMYzxp9QTQWMQ3J5tmqmIq5XNvgd25vpy1VLbzIpHp-tiBDBENILcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: ایران در چارچوب توافقی برای بازگشایی تنگه هرمز، متعهد شده مانع عبور ناوهای جنگی آمریکا از این آبراه شود؛ اقدامی با هدف محدود کردن حضور نظامی آمریکا در خلیج فارس/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/680015" target="_blank">📅 16:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680014">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxKJibBbD21UNk5G60ZPYse05Ru35Cbe9CZhPmL8IIS5yomfA1cYtYRDD0SNMHdXoGgchaRPDfTLFMnW_fOydCPKyO_1q0vEELxoLp-NFoxCJmYWu2WnQ9wDYxJkmSkQ9Zleu_6269T-K19HsNc6zsEJVh9KHzN0kKvLQe6ruu1nZ76YShF1-6a8V1mI7TMSkOVRznVRR_OYhuoj6XsiB1KmS9Mwk0gUfzRV7D8PpJ77pAAbP-wdAfFcFLN4I-SN-SsMoELMeY8u1WsDC_vaGWZm-hcAYi5RO7dypaVDXq-44qARTWRWkM1vmo7ZWexf6cf4rE4fRrEnp0eJS7vg-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت سالروز شهادت امام رضا (ع)؛ حاجت روا
🔹
همراهان گرامی خبرفوری؛ برای شرکت در این پویش کافی‌ست یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کرده و از حاجت شیرینی که با عنایت و لطف امام رضا (ع) برآورده شده است، برایمان بگویید.
🔹
در ابتدای ویس، نام و شهر خود را بگویید و روایتگر کرامت و نگاه ویژه ضامن آهو در زندگی‌تان باشید.
🔸
صدای شما می‌تواند امیدبخش دل‌های بی‌قراری باشد که این روزها به سوی خراسان پر کشیده‌اند
👇
#حاجت_روا
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/680014" target="_blank">📅 16:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680013">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74b1219c01.mp4?token=pd72VzqxZXAcP79Qk1_vv1KwvvVDWsXo83YqrAyGp5a6OtUhZw4DfUrbxgtmXGuM7zXWTkNSnvs7dP8yHbZlWlZDCWvXO7Hln3SGpPNB5-wbqbAUbc7Dbjqmxig6-dQP3YoZucEyMonVUHkQ3BAsa7KFF4vXKW4CoMTdhRNYJx0KozG4MArSp4wujo-FURqh8LJ_D-hgnQorVjfPzPlXQ59ADmXWPmWQiEEyuFrix9WRLhcUgD2G3VDP1cy8k5aa02bkAX0UnqoLBEaLwCNFyisGsMfr51cZL0o8PLWrX_bHHxzSVnIEaVgiqPiJoXX2wp2El0X6EQii93X6JdAV3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74b1219c01.mp4?token=pd72VzqxZXAcP79Qk1_vv1KwvvVDWsXo83YqrAyGp5a6OtUhZw4DfUrbxgtmXGuM7zXWTkNSnvs7dP8yHbZlWlZDCWvXO7Hln3SGpPNB5-wbqbAUbc7Dbjqmxig6-dQP3YoZucEyMonVUHkQ3BAsa7KFF4vXKW4CoMTdhRNYJx0KozG4MArSp4wujo-FURqh8LJ_D-hgnQorVjfPzPlXQ59ADmXWPmWQiEEyuFrix9WRLhcUgD2G3VDP1cy8k5aa02bkAX0UnqoLBEaLwCNFyisGsMfr51cZL0o8PLWrX_bHHxzSVnIEaVgiqPiJoXX2wp2El0X6EQii93X6JdAV3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی عجیب از خانومی که بخاطر عمل زیبایی ماشین خودش رو زیر قیمت بازار فروخته!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/680013" target="_blank">📅 16:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680012">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loe2sDMMo8JdHjMlZxZiMX_qfnNllP4UlpbupWgxiN1jnVak3y_OKGp-BwyNb0jAc2WhfI05VhFEaP-Nk6SEV0IheEmD0TuujZGwvzfCc-ER4lvt6a_zxDubsekIo9Ak5t0-lxL_IHXYv8Fo_icmvizWV6EyFzBH2Ah9Cd0tMGn2mdlnwcZQFlDVWc9GRVYzOzBg4Ck3c7reQPpcnxlvPu7l18HLf50GH83sm8oMqt2EDteYqnPPsNkNcj1uUTH5civ1nRnaFN1SyM-DGFkBQCR0ppk5YsD00D53jIirR_s6Sf6g5AM7NcZsUIcWvqSB_qjX7NkLL0PRVd2s6pZN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهانبخش به اکسلسیور هلند پیوست
🔹
علیرضا جهانبخش کاپیتان تیم ملی فوتبال ایران، با عقد قراردادی به اکسلسیور هلند پیوست و بار دیگر به فوتبال هلند بازگشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/680012" target="_blank">📅 16:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680011">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/156dbace98.mp4?token=txic4fgf0JGklJyq40DpDHlRuPVlN4Hw_paQ3p7744sKJpacPf5L5RWceQW03wWHn7dNo_x_LDlbU51t71CePEk78l3u1BpTDMrBwmlO0rtFb58zVV3nQYU1pIJXyCl3QMR83IZ3JMIrFe_6XXsu1pd5N2o-91M5X5QHRS8G4DPpHX1su2dRHQBMEkwTMCxdHdWgV_VoMcSxbEKAMSgyNuoKNqQJUOH2wTFqktXV3El7kYMekunXDKOvlbe_72dGMNrTsmv1hpgrOTDq8EAHUf9j6oS-fwhI3k7dZY5z-_gSuWBMNL-RC7sFUmYLeaHNf6wzz68kO8hDRceSiZZnJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/156dbace98.mp4?token=txic4fgf0JGklJyq40DpDHlRuPVlN4Hw_paQ3p7744sKJpacPf5L5RWceQW03wWHn7dNo_x_LDlbU51t71CePEk78l3u1BpTDMrBwmlO0rtFb58zVV3nQYU1pIJXyCl3QMR83IZ3JMIrFe_6XXsu1pd5N2o-91M5X5QHRS8G4DPpHX1su2dRHQBMEkwTMCxdHdWgV_VoMcSxbEKAMSgyNuoKNqQJUOH2wTFqktXV3El7kYMekunXDKOvlbe_72dGMNrTsmv1hpgrOTDq8EAHUf9j6oS-fwhI3k7dZY5z-_gSuWBMNL-RC7sFUmYLeaHNf6wzz68kO8hDRceSiZZnJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایده جالب برای بسته‌بندی محصولات کوچک
🎁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/680011" target="_blank">📅 16:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680008">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7557a5a45e.mp4?token=W6CsG-FlFumz2e9H8lPmfbq--1TnBe-JLp6BYr3qmoeMYLBWkfqrB8rDTFUL8hq4iuKZHrHtLOt9gXuzR54iwQog-SG1BJRr1I6ge487LU_Nww_Ja7uF1jbgVfkGSvXlUBGluIsFKMt_beqd5egKOAzwN1G1ASI3DPlUMSJ7NHTRaWd31fMhQU3rBoQBpSR0R9iiHMpJ0NHntryLdYoFZ2gYjzJagfSmHtGVd1UNoYVX8x5ggCgznVzxzq8rSeqKkTaCohVjoXOCTiP51r83TY0Dj1g_Rns998bE4a-iXGqgKWDmeJ1gdRniHBG_l0w2NfowrTc0OnIUzH8wjW5Kzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7557a5a45e.mp4?token=W6CsG-FlFumz2e9H8lPmfbq--1TnBe-JLp6BYr3qmoeMYLBWkfqrB8rDTFUL8hq4iuKZHrHtLOt9gXuzR54iwQog-SG1BJRr1I6ge487LU_Nww_Ja7uF1jbgVfkGSvXlUBGluIsFKMt_beqd5egKOAzwN1G1ASI3DPlUMSJ7NHTRaWd31fMhQU3rBoQBpSR0R9iiHMpJ0NHntryLdYoFZ2gYjzJagfSmHtGVd1UNoYVX8x5ggCgznVzxzq8rSeqKkTaCohVjoXOCTiP51r83TY0Dj1g_Rns998bE4a-iXGqgKWDmeJ1gdRniHBG_l0w2NfowrTc0OnIUzH8wjW5Kzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش عجیب از «مستراح سنتی» در تلویزیون ملی بریتانیا
🔹
در اقدامی که برای بسیاری از بینندگان غیرمنتظره بود، تلویزیون ملی بریتانیا در گزارشی به شیوه استفاده از مستراح سنتی پرداخت!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/680008" target="_blank">📅 16:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680007">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ibe1oxfyBXTy_rrOH6TI3roDs95GtxKHK5G3o3iFs9koBVlgLpEO66gDbgCvIMOcxijMa3AwPNyzAcej-z8XNHP-rnR_gCWIQ3HfiklwtgCUUya_PBm-uDTCFlyBOJ29sBr5tWdAfh6J3G-aKM4fmRkTJWtSf5M6hmKJvQ8PlY-N4ur9xAOFORKEWlhXQtuff3h1iRmvTadX29mr2gACccwmHyGk-FnZeVvCCWXD2QDuNXNxXS-A0IcLchQon4kIWCX_76OdUvIkbrqEwg4DQl7X_WpxnP_HUf5LXoyNkWm1bKqrMvnaWir7SwI8qMgoY-RZRM4Kqe-Et1LXh4XQJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
آیا می‌توان با ۱۰۰ هزار تومان طلا خرید؟
صندوق‌های طلا با پشتوانه فیزیکی سکه و شمش و امکان خرید از ۱۰۰ هزار تومان را دارد که امکان پس‌انداز تدریجی طلا را فراهم می‌کند.
رشد قیمت صندوق‌ها مانند طلا است، مثلا صندوق «رز ترنج» بازدهی ۱۲۶ درصدی داشته، اما چگونه می‌توان صندوق طلا خرید
👇
👇
👇
📌
آموزش نحوه خرید صندوق طلا را اینجا ببینید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/680007" target="_blank">📅 16:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680006">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/785faa238a.mp4?token=qBnzchO4JPMrp-QjYnDlGDSVZIHFet0QTvJzQBD2cZY0B4-D5AEiWpFJQv6lAk8_J1yYpAPGNl79trnbQp7RZG3s-TWYycBh3oNyvJxa8wTgeRb7xaRPjFEr8jNQ4Rrfx3D2VBe5sdjk8V1WdgYgqnDj_8ZbulPBfQ6paAhniH1tHW37iW8krYGCI0iAVp8YlcIrU7l2h946KD_4v4Jjlxdl6Xxcl6-gdHOnS59mI6Z38iZTRldbzErpusO4NuIPP-M_Dk4oZ8U97AI3iYJ3gMOwvAwaCaJi4C22NXYQ9bV0XmEGBUltVhgBrKjLOgtehL8FJd_QmmzToiJpjcX-jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/785faa238a.mp4?token=qBnzchO4JPMrp-QjYnDlGDSVZIHFet0QTvJzQBD2cZY0B4-D5AEiWpFJQv6lAk8_J1yYpAPGNl79trnbQp7RZG3s-TWYycBh3oNyvJxa8wTgeRb7xaRPjFEr8jNQ4Rrfx3D2VBe5sdjk8V1WdgYgqnDj_8ZbulPBfQ6paAhniH1tHW37iW8krYGCI0iAVp8YlcIrU7l2h946KD_4v4Jjlxdl6Xxcl6-gdHOnS59mI6Z38iZTRldbzErpusO4NuIPP-M_Dk4oZ8U97AI3iYJ3gMOwvAwaCaJi4C22NXYQ9bV0XmEGBUltVhgBrKjLOgtehL8FJd_QmmzToiJpjcX-jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور با سرمایه کم، یاد بگیریم دارایی‌مون رو زیاد کنیم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/680006" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680005">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر کار: پرداخت معوقات بازنشستگان احتمالا از دهم شهریور آغاز خواهد شد
🔹
نتایج آزمون ورودی پایه دهم مدارس نمونه دولتی و تکمیل ظرفیت سمپاد اعلام شد
🔹
سخنگوی دولت عراق: هیچ اطلاع قبلی از حمله سعودی آمریکایی به مواضع حشد الشعبی نداشتیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/680005" target="_blank">📅 16:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680003">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428feada65.mp4?token=GJ3v-Q5zTkmoLR7A2NJTKTuApTE8rte3hB3vj192bdTFEHRhYl1FSRRqVjJKOOPxxWG4paQuEZGeRrmM_a9AWON0wABeTMfC2PtBvXH_u1yKAOxAKJtYt_j_kmTVMLhbIODG5FjJCAAMR-EiJE84NRQcqAHjBMKagE4_DbOk2gf4pzSLZRGz7qEYDQLNYslHMGkQxjC2_dThCqv-p2zp8Jij7UXV8LO9bnTOhk1zA6DZn5WpoMMb-WlNyecPnbZjq67fVF-sM70qc8Sk6_HWQvHnUO0pdBMdqT0qa_3tWS0xodw1uJH0RwDYQ4WHME0ZHSowWcArgMnfIhZbgli6MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428feada65.mp4?token=GJ3v-Q5zTkmoLR7A2NJTKTuApTE8rte3hB3vj192bdTFEHRhYl1FSRRqVjJKOOPxxWG4paQuEZGeRrmM_a9AWON0wABeTMfC2PtBvXH_u1yKAOxAKJtYt_j_kmTVMLhbIODG5FjJCAAMR-EiJE84NRQcqAHjBMKagE4_DbOk2gf4pzSLZRGz7qEYDQLNYslHMGkQxjC2_dThCqv-p2zp8Jij7UXV8LO9bnTOhk1zA6DZn5WpoMMb-WlNyecPnbZjq67fVF-sM70qc8Sk6_HWQvHnUO0pdBMdqT0qa_3tWS0xodw1uJH0RwDYQ4WHME0ZHSowWcArgMnfIhZbgli6MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دارو چطور در بدن پخش می‌شود؟
🔹
این همان چیزی است که وقتی تزریق می کنید داخل بدن‌تون اتفاق می‌افتد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/680003" target="_blank">📅 15:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680001">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d8e98d63.mp4?token=THh5CgTCBvfTMBRgzCK7UgSVtB9OzwjTU457gaAOaE_VOzXhQvk9_eStj1KfvGBYE6uP7jkpmjSHaP3Ebdm93Vc9a-x40WziJRMaDaMSjkcL_TVMysADjb5Hkwby5jq8xWCq0YS6PDIJsBbtI2SOtdL0aNddgAMbeKSKzzWRpm68N1ugGBj3hyN9eS-_i9hJ9QnZ7T0z40BSLzOfeRnyGEq0Ai5y-YiXOxjveTl6q0mqgbuFgsly49tpKdzFjt4A1Ip3Y1iwV1Du6LHjubA5FbmmVtWVPX8ItUuuBlzm_fzLj4YKKLIg9vicNVni0Y8cbS-UKXnlkd6v1kYkELxHAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d8e98d63.mp4?token=THh5CgTCBvfTMBRgzCK7UgSVtB9OzwjTU457gaAOaE_VOzXhQvk9_eStj1KfvGBYE6uP7jkpmjSHaP3Ebdm93Vc9a-x40WziJRMaDaMSjkcL_TVMysADjb5Hkwby5jq8xWCq0YS6PDIJsBbtI2SOtdL0aNddgAMbeKSKzzWRpm68N1ugGBj3hyN9eS-_i9hJ9QnZ7T0z40BSLzOfeRnyGEq0Ai5y-YiXOxjveTl6q0mqgbuFgsly49tpKdzFjt4A1Ip3Y1iwV1Du6LHjubA5FbmmVtWVPX8ItUuuBlzm_fzLj4YKKLIg9vicNVni0Y8cbS-UKXnlkd6v1kYkELxHAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب‌ترین ترکیب طبیعت: پلاتیپوس؛ هم تخم‌گذار، هم شیرده، هم سمی!
🔹
این پستاندار آبزی استرالیایی هم تخم می‌گذارد، هم به بچه‌اش شیر می‌دهد، منقاری مانند اردک، پاهای پرده‌دار و دمی مثل سگ‌آبی دارد. جالب‌تر اینکه نرها روی پاهای عقبشان خار سمی دارند! انگار طبیعت چند حیوان را در یک قالب خلق کرده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/680001" target="_blank">📅 15:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679998">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
اتاق تهران، راهبری مسئولیت اجتماعی برای آینده پایدار اقتصاد
🔺
واحد مسئولیت اجتماعی اتاق تهران با ترویج پایداری و اجرای برنامه‌های اجتماعی، نقش بخش خصوصی را در توسعه پایدار اقتصاد تقویت می‌کند. برای کسب اطلاعات بیشتر اینجا
کلیک
کنید با شماره (داخلی۱۶۵۱)۰۲۱۸۸۷۱۹۰۱۱ تماس بگیرید.
https://t.me/TehranChamber</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/679998" target="_blank">📅 15:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679994">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YSQznovN28jPGzFqUJdUZMItTdWaNNliV18QGvlGDJ4tgf_RZJJMcSjSY5OoSRn7SD5BYp5eG5W4MN4wBQWMZ7APlwU8D5YI3nbDEzM5ObKuSmnXlXHzWS9tT79eDxTUb8LZN7hj31cEtf5sbesSWi5mGgwynrpWYpsWwLv3bXMZ6OllC7b9eYxLOhCVD6md75SwVd7JksoLxd4dh0Cil1r4llHXhogqnYSwJTQA6edb7XcAqrvVoZFGziRbQVQ4z2kELf7sFdn2ASRc8imyQnUuEO_3oVzcCQ2a4S8eniCFHQ7iQK0oIpVGy6_D37SXQjDAqDV4jtF7AKYn5GRXwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qq8Qq_SxPT3gUFk3N39Z-pd1SAPhcadOQyvsdKF_XH4aY53sXhllQRtip2dA21akspm_z-EW01SrPGm7WMxav6f9pT5yt-kSlVCV_C3xRC5Xx8Ni6PVWe1RmapnHbGVkM6pdt_BTwGmKNBKSyk47zq6rSW_60UiBcd0Ze-3VdWogRIiO2hopTDNXOQ-90UJV7E67uxoN4r8h80bkI_y9w1ATdrmRyzkJn2lJC8D00WXGAKZTKHtqddJzlrhi6mKmeyUzZSYSTgKIu12WOAJZXYdD8YVzwpQOoK2rYVLkKH5J5tocrnSu27ZgWryknr_PW8GdvNxbUYIWRg-62HRiJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fY7zukPvwrEuhIY2nGFtE0q_h2KHcbWkgaElAJXHlEpA-F8vyTuwoI2AqHgr0iDNkAs_Ug5uhTQDBNHNgeTqe-ggifc3bj3a96q794xZ7EXm-DeTYJd9_vN-uMxxdtKMiLFfvgBO9Ps2aUSIxcX3THnAwIpF0kjcmnStbp2Z_q1E_vWmb_pzaeegXl1l9SZiGqWIKrZWSe_9QLW34tVoOJfgyV9FWBNgxMrf9L-l639i1Hsbz9sIZMSNkB8iv4f2xEWP02uUz-o1lAKsRLkgdGER9exF7SAQCXgKSsVwPPajOuoEpu5K3r2H7aZZOJM4hSqIM3HFcH75m9pymVM99A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83cee229a5.mp4?token=HilZV0DvcRQMw_UdJZ-vd8LwjdpsyslWPJX_C43whIyO74IucomRKolD42v6mOeYzhOjCxhwGzuxYKDhi80RfZyp6_xAoBPxqugYXcuNA0epFcxkFGy6pwowDA0lQNwbhRskevL0r0aZQ-idYtS9OH5Y8J0fFBIhSp8sL23yps9PTU7BrP7Dm6q5D-D21n4FwIj5D389GDAAClqSEjr6aBU6uZu7e822iqKaI-erpuITPqX7-s7HnbE-49bBlCusxPIVONOUekn8OxDTcFdjrkWH9PQ45k52Q3Ex_DmhZowg4uKgEM5s0pY6-0x_B4vlR_vdhb9aaIZIBaxoohaTrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83cee229a5.mp4?token=HilZV0DvcRQMw_UdJZ-vd8LwjdpsyslWPJX_C43whIyO74IucomRKolD42v6mOeYzhOjCxhwGzuxYKDhi80RfZyp6_xAoBPxqugYXcuNA0epFcxkFGy6pwowDA0lQNwbhRskevL0r0aZQ-idYtS9OH5Y8J0fFBIhSp8sL23yps9PTU7BrP7Dm6q5D-D21n4FwIj5D389GDAAClqSEjr6aBU6uZu7e822iqKaI-erpuITPqX7-s7HnbE-49bBlCusxPIVONOUekn8OxDTcFdjrkWH9PQ45k52Q3Ex_DmhZowg4uKgEM5s0pY6-0x_B4vlR_vdhb9aaIZIBaxoohaTrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از انهدام ایستگاه پمپاژ شرکت STAR ENERGY زیر مجموعه شرکت ADVARIO در بندر جبل علی امارات متحده عربی در جریان جنگ رمضان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/679994" target="_blank">📅 15:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679993">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d332845585.mp4?token=fwei3MYjSJKXpdF7Ycs3UfBFKl1k1C61rj8j59XtykLhXEtvnaWyPd5k6nXUDpkOG7oGIy5vYMzkbF1TALRfZLyoBXIs4ecII2n5GDnAlPysaEZUZ0XzWht-eaXb11vVskYbozTErmU9rnmi2odlY66upkFd6tYilIFEbyFuZnkIapF6T2G0cRy3VQxRCctIP1MRs9Sa18XlGxTX3_Q6XwXkL0S_Q0G7PE6B8bR6UenT6PjKCv-P0eBkECeFp__yXzJZFh_pOkvKYirsiPy-Kn6MZLItJom8Po7DcYx_pJdNdWJXVsoIy8Oehi0oTk1U7npqQqWpt1BHxsxnihxG1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d332845585.mp4?token=fwei3MYjSJKXpdF7Ycs3UfBFKl1k1C61rj8j59XtykLhXEtvnaWyPd5k6nXUDpkOG7oGIy5vYMzkbF1TALRfZLyoBXIs4ecII2n5GDnAlPysaEZUZ0XzWht-eaXb11vVskYbozTErmU9rnmi2odlY66upkFd6tYilIFEbyFuZnkIapF6T2G0cRy3VQxRCctIP1MRs9Sa18XlGxTX3_Q6XwXkL0S_Q0G7PE6B8bR6UenT6PjKCv-P0eBkECeFp__yXzJZFh_pOkvKYirsiPy-Kn6MZLItJom8Po7DcYx_pJdNdWJXVsoIy8Oehi0oTk1U7npqQqWpt1BHxsxnihxG1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشای چهره وحشی آمریکایی‌ها؛ از ویتنام تا امروز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/679993" target="_blank">📅 15:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679992">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ba76786ce.mp4?token=hePW2MvCASeSWcXt-JLcvd4Z5QmftboDAkfhdQ8HH7Xxv1ibnovOar7T2OLLPgGlvl_nQqR-bST8P2liegIZrgGFAPZcXRlSEkF2kCGtBjYDsfrfYxOIHbyJ5BRJF7q8J2fA2jxhjN8wFj3sCdFD9uMl4Ajd-RR6xpHl1YNbn9A9yL-Ff5XGINzhXjnqqzrmLM_XDjw5gv6kJo-9jxR8zxgVl9UFKf-wlXr5ns-AEhtoksJ1C3XvO9YYlRV8Rv0xuIMvrnn1LIWkb7ULOu56jVG1vEPLjabZJm0_Lbi_K6J7b_FXcAt9dKdSwTYgWuyLKBYIOp0kXWKPY6Qb3cBoEBVQGBUIsbScqxQsFOshCjshzXILmENEFjL-LambBDDQYFBybkN1Pu5RQmbhU4jxL-tXS2FSHvQah0l_YWlxxvcppOaVY71Kzn9mospM8zScypH0o0bQ643aCOfZEZ6IPEcgzgPFyxGiFidaLUurZwC3nusSz5cH7PawM8urkaJ5HQkjQWJvxYQbBuiCdz9p2mxy1wS7-62RcWVSt1zy1RDjnBaMT6XPHnyr0dxiqA8WDWnJlXCXbbGYAfaav8nY29rINo3Tkc-eRQ5z-OKYDSQ3t-APcfiAv3hSmBmsV_46gECEjU-WWbSv8wqcl-oWJfrGRbhCk15IfsDvv6Zz4vo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ba76786ce.mp4?token=hePW2MvCASeSWcXt-JLcvd4Z5QmftboDAkfhdQ8HH7Xxv1ibnovOar7T2OLLPgGlvl_nQqR-bST8P2liegIZrgGFAPZcXRlSEkF2kCGtBjYDsfrfYxOIHbyJ5BRJF7q8J2fA2jxhjN8wFj3sCdFD9uMl4Ajd-RR6xpHl1YNbn9A9yL-Ff5XGINzhXjnqqzrmLM_XDjw5gv6kJo-9jxR8zxgVl9UFKf-wlXr5ns-AEhtoksJ1C3XvO9YYlRV8Rv0xuIMvrnn1LIWkb7ULOu56jVG1vEPLjabZJm0_Lbi_K6J7b_FXcAt9dKdSwTYgWuyLKBYIOp0kXWKPY6Qb3cBoEBVQGBUIsbScqxQsFOshCjshzXILmENEFjL-LambBDDQYFBybkN1Pu5RQmbhU4jxL-tXS2FSHvQah0l_YWlxxvcppOaVY71Kzn9mospM8zScypH0o0bQ643aCOfZEZ6IPEcgzgPFyxGiFidaLUurZwC3nusSz5cH7PawM8urkaJ5HQkjQWJvxYQbBuiCdz9p2mxy1wS7-62RcWVSt1zy1RDjnBaMT6XPHnyr0dxiqA8WDWnJlXCXbbGYAfaav8nY29rINo3Tkc-eRQ5z-OKYDSQ3t-APcfiAv3hSmBmsV_46gECEjU-WWbSv8wqcl-oWJfrGRbhCk15IfsDvv6Zz4vo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت رئیس‌جمهور از دیدار ۷ ساعته خود با رهبر معظم انقلاب و تاکید ایشان بر حفظ وحدت و انسجام ملی و توجه به معیشت مردم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/679992" target="_blank">📅 15:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679991">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TckD2PwykbqhqkoBttDMUKbb6pNGjRdjT_ydVN6wnfdoBpfbjQAn23wo3PapO_WFBDFnDG1HUrk7kjyO7rO-mCmPdSHce3yBVvtjEh5fpa39e4_1gKAPLNnKPFQVRcfOs9P8FTZlxZECdxSasrJe-GMidwrwzO5IGn7uBjqPfz-eydZo3Z_sr2OQnl9WjGr7ZtEzDaxdaySR0idy5sEV-Tgu4lX4KwkeGlgG7-BOCqKnaFBWO1wNhSvGfZF7LF-B7NeZ7Yy1wGEqvVrttQ5B12gl35_Xky-rOJ0Oer62Endy7RbchJZx3OwvfyYvcESxezqe70_pD6ggWcIvth1_rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ فایتر ایرانی در مسکو برای کمربند قهرمانی
🔹
امیر علی‌اکبری، قهرمان اسبق کشتی فرنگی جهان، شنبه ۲۴ مرداد ۱۴۰۵ در مسکو برای کمربند سنگین‌وزن سازمان ACA با علیخان واخائف (قهرمان فعلی) مبارزه می‌کند. این دیدار اصلی رویداد ACA 206 خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/679991" target="_blank">📅 15:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679990">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
دادسرای جنایی: جنازه حمیدرضا رجب‌زاده اطراف تهران کشف شد
🔹
ساعتی پیش جنازه حمیدرضا رجب‌زاده در اطراف تهران کشف و به پزشکی قانونی منتقل شد.
🔹
در پی قتل فجیع حمیدرضا رجب‌زاده و در دسترس نبودن پیکر وی، سرانجام با دستور قضایی و اقدامات جنایی پیکر وی ساعتی پیش…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/679990" target="_blank">📅 15:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679988">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
سخنگوی سپاه: موشک‌های ایران قابلیت‌ تغییر مسیر دارند
🔹
موشک‌های ما قابلیت هدایت دارند و حتی برخی موشک‌ها می‌توانند در برابر سامانه‌های پدافندی دشمن تغییر مسیر دهند
🔹
حتی اگر برای موشکی یک هدف مشخص شده باشد، می‌توانیم آن هدف را در میانۀ مسیر تغییر دهیم و هدف ثانویه‌ای برای آن تعیین کنیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/679988" target="_blank">📅 15:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679987">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c92dd8ed3.mp4?token=Trr084xFkgaLrtwmSH7Ki-52Hn6VDfpMWOJSX3hsFOrGDwxW1iBu93-6REIwg5ewerEL7i1sGoXnxM_yE98ohbwtcA557K3fJe5sM6t0FmL-SDcbZHioC2Z7fY_FoFUGKlZ8gdPziMKXGNVR_NfuIkgq6PvpwZQeRfI1nTYteJEbx5iPFghXB4KmGHQhebIQJrqCER-S216WfSZCixVDhODi5LgNyV015E0dqLfomyl4s1Ls8mUTCqkNxPf74gVQMaF9W6CL6YM81GaJPIX6U8PS5-VkMnYu_XmjxRSSP2vsf0UCAOiK87_Oq-GBI1CpzSoHzaNK2Nvo898fVAb7_VwZnBGG2I7HWasCcgUcV6ybqis0ZEnmhOHXz9QLvJZ5_00Bn2bQjsaxxX0ze_TOREo5ANadhNKrh0e5dYlGsF8GcgvfGqgRl0GjHyjNQr145P4P1Q8ljprhZjTOMk2VkGZYNPWq4Hob5DmOm262dJ9XadR1lvc7Vxa18yxaXX_zxl6Qzjn1CsXe1C9_qF2LJlFE3OSJqjrEDnfb4KsIpPzJ9atBqDu9MsaWJ8LqGF3ohw_iK1ZHjWhoexItoQnmvek37Brpbmg8IlDZCyuDPUzIiuWxNiESh8haqjjGSPwTupOSoPf_T6WvbV1NwrQi-di5xQrwlJsc-whr8t0q7CI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c92dd8ed3.mp4?token=Trr084xFkgaLrtwmSH7Ki-52Hn6VDfpMWOJSX3hsFOrGDwxW1iBu93-6REIwg5ewerEL7i1sGoXnxM_yE98ohbwtcA557K3fJe5sM6t0FmL-SDcbZHioC2Z7fY_FoFUGKlZ8gdPziMKXGNVR_NfuIkgq6PvpwZQeRfI1nTYteJEbx5iPFghXB4KmGHQhebIQJrqCER-S216WfSZCixVDhODi5LgNyV015E0dqLfomyl4s1Ls8mUTCqkNxPf74gVQMaF9W6CL6YM81GaJPIX6U8PS5-VkMnYu_XmjxRSSP2vsf0UCAOiK87_Oq-GBI1CpzSoHzaNK2Nvo898fVAb7_VwZnBGG2I7HWasCcgUcV6ybqis0ZEnmhOHXz9QLvJZ5_00Bn2bQjsaxxX0ze_TOREo5ANadhNKrh0e5dYlGsF8GcgvfGqgRl0GjHyjNQr145P4P1Q8ljprhZjTOMk2VkGZYNPWq4Hob5DmOm262dJ9XadR1lvc7Vxa18yxaXX_zxl6Qzjn1CsXe1C9_qF2LJlFE3OSJqjrEDnfb4KsIpPzJ9atBqDu9MsaWJ8LqGF3ohw_iK1ZHjWhoexItoQnmvek37Brpbmg8IlDZCyuDPUzIiuWxNiESh8haqjjGSPwTupOSoPf_T6WvbV1NwrQi-di5xQrwlJsc-whr8t0q7CI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری رییس کمیسیون عمران مجلس
:
خیلی از پروژه‌ها را در کشور که اولویت نداشتند، به دلیل فشار و لابی شروع شده است
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
خیلی از پروژه ها در کشور در اولویت نبودند یا نیاز کشور نبودند، اما با فشار افراد مختلف این پروژه ها را در کشور داریم؛ از جمله فرودگاه‌ها ، سدها و غیره.
🔹
از سال گذشته دولت سختگیری می‌کند که پروژه جدیدی شروع نشود مگر اینکه پروژه قبل تمام شود‌.
🔹
دولت هم نباید از زیر بار نیاز یک منطقه به یک پروژه عمرانی به این بهانه فرار کند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/679987" target="_blank">📅 15:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679984">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
وال استریت ژورنال فاش کرد: ۴۲ هواپیمای آمریکایی در حملات ایران منهدم شدند یا آسیب دیدند
وال‌استریت ژورنال:
🔹
حملات ایران (بیش از ۲۰۰۰ حمله در منطقه) به ۲۰ سایت آمریکایی در ۸ کشور آسیب زده، ۴۲ هواپیمای نظامی آمریکا را منهدم یا آسیب‌رسانده و ۱۳ میلیارد دلار خسارت تجهیزاتی و تأسیساتی به آمریکا تحمیل کرده؛ درحالی‌که پنتاگون برای دفاع از پایگاه‌هایش آمادگی کافی ندارد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/679984" target="_blank">📅 15:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679982">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_9VXOTJSbpQpE_G8n5hWWdd2nAwsozJOC7TM1QQ-6R12rafDzTAOtqRp_34qYAs2RnYnivjriNpuXNlviPZboIMTFfcYchgAwtfUgJmlZVbjmb-vYz9DqBG-cQ9c2FxeaW04nMDwL9hVMeQMNlIK0PjNzlbX_EEplMXeMxhPrabvpwTuEYYqQ8UcNj9DPj_ARx35CMkoezSkn44ToRoGDXtNspEH7Jcy_lo6k5cmL8M6Ex-ZcYzdqaS-2In315Km5rEmx8OHjwe7pMxAZXycnrat5i09-onwxSu5tH-FBRfkCeILbQCjnIEDR2fAOWQApY0_9_3W_zJszRUOSr7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ۱،۰۰۰،۰۰۰ تومان تخفیف، خودروتان را برای سفر آماده کنید
💯
🔸
تعویض انواع لاستیک دولتی
🔸
تعویض روغن موتور با قیمت مصوب
🔸
خرید و تعویض لنت و سایر لوازم خودرو
تمام این خدمات با تضمین کمترین قیمت و یک تومان تخفیف در اختیار شما قرار دارد.
کد تخفیف: RWELXT
مهلت استفاده: ۲۳ مرداد
حداقل خرید: ۳ میلیون تومان
همین حالا وارد سایت تپسی‌گاراژ شوید، نزدیک‌ترین مرکز خدماتی را انتخاب کنید و سفارش خود را نهایی کنید.
👇
https://tapsi.link/mrip0</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/679982" target="_blank">📅 15:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679980">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec49f80d3b.mp4?token=qzV-7a6_d8LgCnWfsU8nTFw7uqgP5ICjPQT5gzp5zDtfmM1QRjgEb54AeTD2NPYUJV06wjtuTVyKvABjgpOgZou8TTp1eLQboea8_rfgu5hCAQ-2Dp8zFJFfuYdaWOWQ67kg7N1UQFaJr2TCgXlox4ZsYePam9jy7CRQ28U_MWPFwyshwOTuOaPFs56uLbRXH79OY592P7Jqroqjqj8ZxQ55VMkJo4BYNtEKWnVJ9hL8V1u3rRhM9qE9dRRyLCpIXxxtuUczHX1bgu_jwkss43bYfYMe7Vi_gTOUP5cWieMLz0wrmrzTVGy_WqLDRWkvL6yKI9OyIFHeSbrzVvZZ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec49f80d3b.mp4?token=qzV-7a6_d8LgCnWfsU8nTFw7uqgP5ICjPQT5gzp5zDtfmM1QRjgEb54AeTD2NPYUJV06wjtuTVyKvABjgpOgZou8TTp1eLQboea8_rfgu5hCAQ-2Dp8zFJFfuYdaWOWQ67kg7N1UQFaJr2TCgXlox4ZsYePam9jy7CRQ28U_MWPFwyshwOTuOaPFs56uLbRXH79OY592P7Jqroqjqj8ZxQ55VMkJo4BYNtEKWnVJ9hL8V1u3rRhM9qE9dRRyLCpIXxxtuUczHX1bgu_jwkss43bYfYMe7Vi_gTOUP5cWieMLz0wrmrzTVGy_WqLDRWkvL6yKI9OyIFHeSbrzVvZZ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگیری پزشک قلابی عمل‌های زیبایی در شهریار تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/679980" target="_blank">📅 14:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679979">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688432cc6d.mp4?token=J0-jVCoYPPhpAOPg2Njpe3nnaMlj3n2FvSt9qdUB-PlbNsBK2sJzS8jaV028P_-Slp5XIQm6fw2CdPP1zafrqARUqrvwWWoYqyEKTfil1639pw_3WLS1hdAbHBrTUrzsi2h3PiKgFw6G3nGKEzPyxVSmslpWjkuGLK-6fdvxRePy-uUWmmDJQeyDUhlf-8UqsJuGivFNjQin8KPQQ4OAdCrEbIW6u5swmZK3Idc9WqQhmCHX0GFNwzS1PQGaJ3JpdU3RkBYuH1gcZTPAX14O2BwvHSBTirE4L-2ORHeOfEP6YuA84BdF8YmXiwq_Dm14DM09QTII2QxqSFuW3LagCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688432cc6d.mp4?token=J0-jVCoYPPhpAOPg2Njpe3nnaMlj3n2FvSt9qdUB-PlbNsBK2sJzS8jaV028P_-Slp5XIQm6fw2CdPP1zafrqARUqrvwWWoYqyEKTfil1639pw_3WLS1hdAbHBrTUrzsi2h3PiKgFw6G3nGKEzPyxVSmslpWjkuGLK-6fdvxRePy-uUWmmDJQeyDUhlf-8UqsJuGivFNjQin8KPQQ4OAdCrEbIW6u5swmZK3Idc9WqQhmCHX0GFNwzS1PQGaJ3JpdU3RkBYuH1gcZTPAX14O2BwvHSBTirE4L-2ORHeOfEP6YuA84BdF8YmXiwq_Dm14DM09QTII2QxqSFuW3LagCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهید سپهبد موسوی: هرچی تنبیهی من خوردم، بخاطر خنده‌هام بود
🔹
۱۹ مرداد ماه، سالروز ولادت فرمانده شهید نیروهای مسلح
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/679979" target="_blank">📅 14:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679978">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrJz9kaDJZ7on2Dle_OGbwV6HufVwVnExr-0j5kneIHxaNvNByQVYqb3G9nBtzw5N-dpIA7BLlpraxJyiefHokHRHbJdHQr5tZx6d3siBbYDaicA6tFhMk6G5uaotkKpno2HbGFBkUks3cldkBacVz5JU19h6ABP-o2md7RVptD8J6HLbps_R6tjgzCiAb6EygOWgpgfFJIwHd9QPNKQXvt6F4NjAuOs7oBuP1iY__HCjDbwMUiGAE6MmAZ9aaBmRGZY1vuNv5jIxjvHwXruwxl7WRH-feOqmOGiIwMofqLtpNSogoYNNKzmZ0NEqpITok6WSi2lfyehHXw4s8dOwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات سایبری؛ عامل بیش از ۶ درصد ترافیک اینترنت کشور
🔹️
بیش از ۶ درصد ترافیک در سطح کشور بدلیل "دیداس" و حملات سایبری است که عدد بسیار بزرگی است.
🔹
حملهٔ دیداس نوعی حملهٔ سایبری است که در آن، مهاجم با ارسال حجم زیادی از درخواست‌ها به یک وب‌سایت یا سرور، باعث ازدسترس خارج شدن آن سرویس می‌شود.
@amarfact</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/679978" target="_blank">📅 14:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679975">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7607a3ad.mp4?token=g2_-BUEH5wvHpIaNWHI12HnGpunQ4d0d8YgvXc0xnZFORaZtF45IIgQLYGtfJlCkLfnKawz0M26lKGkW1NqpUHhL2ABSqSSgvXwgmfm6iK-ZXEOC93Ex-57Udwg39R6Zpuum5guYrB4-oq3d78bZ2Glk9GRO0L-OdHI1bUKVWiVESf-m8k1Hd7y19eWSOMjSPv0PzK7A6QaUG6sWvTzQAmP7X6bH8VMloq0NcHBn2BIRafvGe2joGDtHTNJpoSJPfmnkcYpLpf-IhWXTpywL5-wU6zcAavJeIzFLVR8LcdVUr4iYrBpv4b84uDTore3qGQCXzMYw8tiYhtigO_OR-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7607a3ad.mp4?token=g2_-BUEH5wvHpIaNWHI12HnGpunQ4d0d8YgvXc0xnZFORaZtF45IIgQLYGtfJlCkLfnKawz0M26lKGkW1NqpUHhL2ABSqSSgvXwgmfm6iK-ZXEOC93Ex-57Udwg39R6Zpuum5guYrB4-oq3d78bZ2Glk9GRO0L-OdHI1bUKVWiVESf-m8k1Hd7y19eWSOMjSPv0PzK7A6QaUG6sWvTzQAmP7X6bH8VMloq0NcHBn2BIRafvGe2joGDtHTNJpoSJPfmnkcYpLpf-IhWXTpywL5-wU6zcAavJeIzFLVR8LcdVUr4iYrBpv4b84uDTore3qGQCXzMYw8tiYhtigO_OR-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی کمتر دیده شده از سینه زنی رهبر انقلاب در مراسم تشییع فرزند مرحوم آیت‌الله استادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/679975" target="_blank">📅 14:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679974">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45066d47b4.mp4?token=HGF-NR9UCAu2fVnSWKEHvEr2ndmArRO3CoP7mZTG7hdky6dNFX4Vt1vi_9_jiAW1jyoFBwr2uz_GUn3GUz3uraGrSzNQ02k5xoRMB4CtY6C7OHlNz-C7bh8zD5ZQjLcT57Cxi-tJP86MwNMIP4YiCweVPZKv34LwwGmch9GkV0ZE80zd6WYWKpWMiSFqs1qKHkCCMX3zWMoAzkYPWyom4x8AvNmPfC9pFsfAhtii4uDRuyJ3GmSKw1VRI9SH2iZa5Pd8uJ-iIKJ8Y9VMzwa0O4A56qibi05es7NXlUmReMuIqCC5wDwmK_7hN3TcdYabnJIn5coBtEMIve9nVigifg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45066d47b4.mp4?token=HGF-NR9UCAu2fVnSWKEHvEr2ndmArRO3CoP7mZTG7hdky6dNFX4Vt1vi_9_jiAW1jyoFBwr2uz_GUn3GUz3uraGrSzNQ02k5xoRMB4CtY6C7OHlNz-C7bh8zD5ZQjLcT57Cxi-tJP86MwNMIP4YiCweVPZKv34LwwGmch9GkV0ZE80zd6WYWKpWMiSFqs1qKHkCCMX3zWMoAzkYPWyom4x8AvNmPfC9pFsfAhtii4uDRuyJ3GmSKw1VRI9SH2iZa5Pd8uJ-iIKJ8Y9VMzwa0O4A56qibi05es7NXlUmReMuIqCC5wDwmK_7hN3TcdYabnJIn5coBtEMIve9nVigifg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه رشد لاله مردابی
🔹
یکی از اشتباهات رایج، یکی دانستن لاله مردابی با نیلوفر آبی مصری است؛ با توجه به مرکز گل می‌توان تفاوت این دو گیاه را تشخیص داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/679974" target="_blank">📅 14:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679973">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffa2d0a474.mp4?token=PnNWIRituQlHOGWforseksjVOCgOmrcFhXrc-zi1R1xkt-VGh9CJJBBGIb3BwTFRUJE1cCFGQ_za5lZprdBpM7hILIwuypXg4NjhNQgmqoMt0NYGJP3DX7gXGETGVt5Jfb6uJ_A0zkwhEyLWwViC8tPyc1vjMRp2p68ryPthnXvEbTiLowIpV1tB1_mrPlviswPLzL8fGKtVtzrPOhEX3fbcgsyQDXsUXRrDMoc-jsExbaH_JmWrW6UI0CC08WBF9A9GWZPRQGXVJZ1O8nwHmMoBAE7rAvJzDQH9C5wEKkdEAflTYS3w4DFhq4C9RxG3V5PBA7gxrGEfdvR_acuPCJxk2zh8ypU0EJ7O9Q7IKuCx6nU3GJ63X2Ihn_t_lRQk8FJOYJ3tYVGMpqUs1WvO6uTUF4HEetd8OkU6RY3GM5N54ZGhKI756fPa2N_E8UAAkA9lc3PWzZ94fv3Niuqki7SXHGm1cTIiGTzlQx_XNFfN92ZesrM_q1bqLQncqqaOAS_eNubF2B4nxlR8XhTBV0dI-rP6sPoEefHpUTZkdcYRLPaOT777NcAfKREbHH2qASGoKvjXs1pw_4DWUbwZM0mEKS6sjRLrVtvZdUKRoLnuUKEFL5rhjmexU1_cjyuoOpUb74apEAAfeNkKb87aLBj2DSefPMWdtew7ItuGnIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffa2d0a474.mp4?token=PnNWIRituQlHOGWforseksjVOCgOmrcFhXrc-zi1R1xkt-VGh9CJJBBGIb3BwTFRUJE1cCFGQ_za5lZprdBpM7hILIwuypXg4NjhNQgmqoMt0NYGJP3DX7gXGETGVt5Jfb6uJ_A0zkwhEyLWwViC8tPyc1vjMRp2p68ryPthnXvEbTiLowIpV1tB1_mrPlviswPLzL8fGKtVtzrPOhEX3fbcgsyQDXsUXRrDMoc-jsExbaH_JmWrW6UI0CC08WBF9A9GWZPRQGXVJZ1O8nwHmMoBAE7rAvJzDQH9C5wEKkdEAflTYS3w4DFhq4C9RxG3V5PBA7gxrGEfdvR_acuPCJxk2zh8ypU0EJ7O9Q7IKuCx6nU3GJ63X2Ihn_t_lRQk8FJOYJ3tYVGMpqUs1WvO6uTUF4HEetd8OkU6RY3GM5N54ZGhKI756fPa2N_E8UAAkA9lc3PWzZ94fv3Niuqki7SXHGm1cTIiGTzlQx_XNFfN92ZesrM_q1bqLQncqqaOAS_eNubF2B4nxlR8XhTBV0dI-rP6sPoEefHpUTZkdcYRLPaOT777NcAfKREbHH2qASGoKvjXs1pw_4DWUbwZM0mEKS6sjRLrVtvZdUKRoLnuUKEFL5rhjmexU1_cjyuoOpUb74apEAAfeNkKb87aLBj2DSefPMWdtew7ItuGnIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین‌پاک، کارشناس جبهه مقاومت: رژیم صهیونیستی ۷۰ درصد غزه را اشغال کرده است/ اگر دوباره خطای حمله به ایران را تکرار کند، با ضربات متفاوت و تسلیحات پیشرفته‌تر ایران روبه‌رو خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/679973" target="_blank">📅 14:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679972">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
فیلتر پلتفرم‌ها بدون تایید رییس جمهور ممنوع شد
؛
دولت اختیار محدودسازی کسب‌وکارهای دیجیتال را مشروط به تأیید رئیس‌جمهور کرد
🔹
بر اساس این مصوبه، دستگاه‌های اجرایی دیگر نمی‌توانند به‌صورت مستقل درباره محدودکردن فعالیت پلتفرم‌ها تصمیم بگیرند و هرگونه اقدام در این زمینه باید ابتدا در «ستاد راهبری و ساماندهی فضای مجازی» بررسی و در نهایت به تأیید رئیس‌جمهور برسد.
🔹
اهمیت این مصوبه فقط به تعیین یک مسیر اداری جدید محدود نمی‌شود؛ دولت برای تصمیم‌هایی که خارج از این چارچوب اتخاذ شوند نیز اعتبار قانونی قائل نشده است. بر اساس ابلاغیه هیئت دولت، هر تصمیم یا اقدامی که بدون طی این فرایند برای انسداد، تعلیق، تحدید یا ممنوعیت فعالیت سکوها و کسب‌وکارهای فضای مجازی انجام شود، «فاقد اعتبار» خواهد بود.
🔹
فرد ذی‌ربط در صورت واردشدن خسارت، مطابق قوانین و مقررات مسئول جبران آن خواهد بود./ شرق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/679972" target="_blank">📅 14:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679971">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f43b18398.mp4?token=qFFGxLOl4ctt-HNgVLJv_FgB4tw8Ph4a1i_JMeYWhtwoEOuVcmcGzqDv86fOvE5V4JdeEcSSLz8mDmiou4_dB0Nk38cldwhtTmAP5QGADW8TBeDH4mjtkNuRhtk4XjDZPf84h2V0O5crYk214NVDW-G66I6zfef71SqMoZfD2M7PaQaL6srTwklReWnbfnseQ1tpN98MYR7tGUYKfd6fXXVdVFQ2YP0xKRvqh1FaG9cXFdtx4KhAXdE8NMgJhxfdwtB8b0-RjIaJz6gPrk1-ocadHBPh2ngNi-PRqhw2YpaedmDEVArdmY6x0Ccmp55qfUo8T_n_B0s3uOR1wgE5HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f43b18398.mp4?token=qFFGxLOl4ctt-HNgVLJv_FgB4tw8Ph4a1i_JMeYWhtwoEOuVcmcGzqDv86fOvE5V4JdeEcSSLz8mDmiou4_dB0Nk38cldwhtTmAP5QGADW8TBeDH4mjtkNuRhtk4XjDZPf84h2V0O5crYk214NVDW-G66I6zfef71SqMoZfD2M7PaQaL6srTwklReWnbfnseQ1tpN98MYR7tGUYKfd6fXXVdVFQ2YP0xKRvqh1FaG9cXFdtx4KhAXdE8NMgJhxfdwtB8b0-RjIaJz6gPrk1-ocadHBPh2ngNi-PRqhw2YpaedmDEVArdmY6x0Ccmp55qfUo8T_n_B0s3uOR1wgE5HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: هیچ قدرتی نمی‌تواند مردم ما را وادار به تسلیم کند
🔹
مردم با حضور در میدان، تهدیدها را به فرصت تبدیل کردند و همۀ معادلات دشمن را با وحدت و همدلی شکست دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/679971" target="_blank">📅 14:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679970">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وهفتم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای سید امید متقی که بخاطر خواب آلودگی در حین رانندگی دچار سانحه تصادف و ضربه مغزی شده و یک‌ ماه در کما به سر می‌برد و با رؤیت جد بزرگوارشان امام موسی‌بن‌جعفر، شکستگی‌های داخلی در بدن که بیمارستان متوجه آن نشده بود، شفا می‌یابد و به او سفارش رعایت حق‌الناس و طلب حلالیت از انسان.ها در دنیا می‌شود، را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سید امید متقی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/679970" target="_blank">📅 14:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679969">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3Vy33Wz8HUQLG08nKaGUQ9O960dqmxQNyAifja3yMQrnOiu0EHFTc_2Djs5Dw2-FdcsJXPvtuIPZg06MYzyk7ZcoS-TnHNVcMVzuA0FsNlxL05tV6VjfAJxS95ata-cI5nechwxzhwU2fD5Ipa5DtMhxzyytquSSqdzTCfNRNTVx1dkQhKSB77rrgPUcjEMFZv1wBqCud0WKMSFdJf40FyoTmkJuX7-ZHD4yrwdacG_zrUF5eMVKbmaeOu3KfmdeX2B_WzeiuNZTONA6cdqXTNkQMc_g9-l7d0aJg9yYiFdXFZtJB6XDT0Uq6iVaYa6GEQUPYDkrBQHLdGX5HnMTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر کتونی مناسب چه مدل شلواریه؟
#فوری_استایل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/679969" target="_blank">📅 14:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679968">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
افزایش شهدای حشدالشعبی به ۲۰ نفر
🔹
حشد الشعبی در بیانیه‌ای اعلام کرد که در پی حملات آمریکا و عربستان تاکنون ۲۰ نفر شهید و ۳۲ نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/679968" target="_blank">📅 14:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679967">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e7d6feab.mp4?token=ko4kCBwsVYLiNSS6HL4EiGJi10ZArdaLAagwz0sNvqb5kDy3_A07DvKbRa5kv8evwOpc-osBOGSJx0FWWu332XjaO0U4AgqIEX1XBdIcprJ_BYOGn5q0U9x9wN26_UDdQPWZ2i_vm7w2Q8f-bv0UoYwFAg4B1HswVV6cJu09xBEt2ZRQMKlyw5-S3-WkaaMkg6egjh_WTfQMYNVDOj2UEiLDfaHrrKScvIo-p1gf_yyCfRH0kWtYdACC0v77CEDSWWcGTVn8Wel6hiX-ZKxVn2c3AJkq4By4sDMDig9YmCxEc0zgNajmMMSMslZwiIiQwxXXk4WOuJ9WNqGQrDsc6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e7d6feab.mp4?token=ko4kCBwsVYLiNSS6HL4EiGJi10ZArdaLAagwz0sNvqb5kDy3_A07DvKbRa5kv8evwOpc-osBOGSJx0FWWu332XjaO0U4AgqIEX1XBdIcprJ_BYOGn5q0U9x9wN26_UDdQPWZ2i_vm7w2Q8f-bv0UoYwFAg4B1HswVV6cJu09xBEt2ZRQMKlyw5-S3-WkaaMkg6egjh_WTfQMYNVDOj2UEiLDfaHrrKScvIo-p1gf_yyCfRH0kWtYdACC0v77CEDSWWcGTVn8Wel6hiX-ZKxVn2c3AJkq4By4sDMDig9YmCxEc0zgNajmMMSMslZwiIiQwxXXk4WOuJ9WNqGQrDsc6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باید برخاست؛ برای ایران، با هم و کنار هم
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/679967" target="_blank">📅 14:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679966">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d4c320e7.mp4?token=mCOY_lMdF9HfBE58zscZGtXDQ4hoZ7u-UMsDgJkSC7jibZAk7u7dsXJtQAv-JVWdPn9QpsIOcIGL0lkRHbwM4lUbo_xw8YmNfdE75fEyl03VH_2IVLgBXkkKUtCHvyVo1DbtZ3aFDFBBqouwp3S_AV0vsmRBGRhkD1qqXJxk7oMJ496omNP0GHEOR9zptaF-SBcme2K4ZE8sBodFdA7XIqsr5KSNv2PYTHlXuRx7kALj91PL--krXjSxrYxR5amsxi3ir0rHik7cd9cQQiSDmGwqUhjDSse0aJ1OHPwrLr3XkMhlKMFgPZ7eTMotozwKpY7CSZqf0ea6LrqVI2yjf10YB9hCYGIbxuSH7O-vVMOdt370Y00f_1dA-FL_9DAZ9Kk0v6z1rzY0cbSx842fp1JPGdCO1QOOVp1lpyfwhsBK59hWMRGpQnNC62DJaajUHhmdyH3-EFS7c_Q5cKqqyyJRFfj6nB5-tQJB90hVZHGGAHUiQHtEvDgg6fqgypztdNXFoXFMtVbLCBVwiPzmNHC4JtUGiSQI9fuQy-1xweTC6vOxvRhEJwY3AS_CxUE2TZ-0MlpG8mYbU-pchzjMmDXiD2F052RIHbU0lB0qe_4zoalJCzoKlkunoR_7c9pHFdNvf6gFW5d-PlRwciogWWzIexr1xHsAG-q8SQ0ie5U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d4c320e7.mp4?token=mCOY_lMdF9HfBE58zscZGtXDQ4hoZ7u-UMsDgJkSC7jibZAk7u7dsXJtQAv-JVWdPn9QpsIOcIGL0lkRHbwM4lUbo_xw8YmNfdE75fEyl03VH_2IVLgBXkkKUtCHvyVo1DbtZ3aFDFBBqouwp3S_AV0vsmRBGRhkD1qqXJxk7oMJ496omNP0GHEOR9zptaF-SBcme2K4ZE8sBodFdA7XIqsr5KSNv2PYTHlXuRx7kALj91PL--krXjSxrYxR5amsxi3ir0rHik7cd9cQQiSDmGwqUhjDSse0aJ1OHPwrLr3XkMhlKMFgPZ7eTMotozwKpY7CSZqf0ea6LrqVI2yjf10YB9hCYGIbxuSH7O-vVMOdt370Y00f_1dA-FL_9DAZ9Kk0v6z1rzY0cbSx842fp1JPGdCO1QOOVp1lpyfwhsBK59hWMRGpQnNC62DJaajUHhmdyH3-EFS7c_Q5cKqqyyJRFfj6nB5-tQJB90hVZHGGAHUiQHtEvDgg6fqgypztdNXFoXFMtVbLCBVwiPzmNHC4JtUGiSQI9fuQy-1xweTC6vOxvRhEJwY3AS_CxUE2TZ-0MlpG8mYbU-pchzjMmDXiD2F052RIHbU0lB0qe_4zoalJCzoKlkunoR_7c9pHFdNvf6gFW5d-PlRwciogWWzIexr1xHsAG-q8SQ0ie5U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: هیچ دولتی در حوزه مسکن خوب عمل نکرده است
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
متاسفانه در کشور برای حوزه عمرانی جایی برای بخش خصوصی پیش بینی نکردیم.
منابعی که در بودجه سالانه برای حوزه عمرانی پیش بینی می کنیم یک پنجاهم چیزی است که نیاز داریم.
🔹
باید قبول کنیم خیلی از پروژه های عمرانی را در کشور کلنگ زدیم؛ حتی درصدی پیشرفت فیزیکی دارد، اما نیاز کشور نیست.
🔹
در حوزه عمرانی کشور را گران اداره می کنیم.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/679966" target="_blank">📅 13:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679963">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
کشف جسد «دنیل سیاد» از مرتبطان پرونده اپستین در پاریس
🔹
جسد دنیل سیاد، از چهره‌های کلیدی در پرونده جفری اپستین که متهم به تأمین دختران جوان برای او بود و قرار بود بازجویی شود، در پاریس پیدا شد.
🔹
وی دومین فرد مرتبط با این پرونده است که در فرانسه جان باخته…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/679963" target="_blank">📅 13:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679958">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdXl3g_1M0wd-2ImhkTUk14b3sf-ZkeyEODaoJELJkEP7RWpFeQY5A9_nWCGxTlAaH_0nYODDLaUTepx46DPbBuqDicwxOTAb9AJjL4n6qw7w5Nttoih9WBL_ahtuH9tDwaDwU2WaVGs5nD5YS54wRHk3j-gbJ9bpW5T3yM-3MeNCyRE8G8onqWmTPgxcTzvEiIc5f3NX-zvLNHb54K7ZC1Xiru2XcLbUztdDg_mKRIFdrsG3J_McyVlXLJEwxKUbWZFiBEDWyvTCs3q5hFA-U3tyHzqcEO4tmnUtXEeZ4odyZjEsZqLRPXvU3krAegkdAAAmSkVa5banOtlUbkkmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYEaIj56K5X8Axmi7TB5ivsNFzVrLTyu37YwbwK_vX5qEILMoQ2yluxeagizZjqZDpRKA4YEX7ro7VEEzbtQB8YlSHbv63xXg0yuQUgcKGARubKmtjIkso47-A5AiM3DeJm_S0DolIdwrnpWisF_ajCoIE5BmehXUE06pC-bx0STk7jf2QDh1UHdOLMfavSh98hx42khQCSSdSOd-WlFUtNYFPLjjHqx_Gl1oJZtrObnJWN5NCEuGD-ySElJaBfa-Q7ouz8jKob8-Pbe7mjcUr4olVwLCpC_pOB_mki-diWwGxCzbeMZyJxhY-OdzG2vo3c5m2qTD0F75RoKVp0JXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TQGvrwost6tTf2ahK0_xtKD4ik2k71TL3dpmuw5tGCA58NP485tLzMRYwWhpcc1yHN1SCc7CkNNjgRFNXPcVzvXkT_FUYnPea09NH1n5269Bs8NtIEhA63MCXXPZ52_COaE01oTyZhFl6HMNs3r7_unw_34pNPm8Mem6NqTbFb8Ku4EZsSl7492kUVjwWKdS3DgfGmNFM_m6AmqAcpuLkedz5pspghNHY6n2mNIngNtlZ-xEZ652_4uiiyc7KJSfvv2Eg3Jzsc2MAZtBWMU8tQKe4ncudBsyDsYxyK_fB4mT3grc7IYysuYUMFWXAugeQd_-RjUO6E32W23B1e4TIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شمشیر کوتاه هخامنشی
🗡
🔹
اکینکه‌ی زرین یا شمشیر کوتاه هخامنشی، متعلق به سده‌های پنجم تا چهارم پیش از میلاد است که در اکباتان (همدان امروزی) کشف شده و اکنون در موزه ملی ایران نگهداری می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/679958" target="_blank">📅 13:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679956">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdd3a47ed.mp4?token=LirSty3wpxhEcTI8aD5wmn-jqDusLStM_wFxAJJotIfnUMSByQWdttuI3um5yPwbCprcYRNpyGkmFzahTOMqLaLhx5J-CwgwJn1UO2txV6G802f2fQRQTBpd_frw2C0f8Z11aGSsAo-KJJnZrqeIBeaYOQdzPxhbeMkMyCEnuNM7RCG_xeLQ5pRiL8fUibpE7CtlpGNXjhLLDHEWWgGaQyvfPl5-ESWapxNn6-4ewi2ldII0kWgdprirW_B0i3zYlCXhchgjSL_ZwhyNMmJDV4EDn48lW_E0EbF-8_BFesshmGkkKZs79v8G0Y7obN_Uk_WlW5Xn3dLbjFKwAv-Q0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdd3a47ed.mp4?token=LirSty3wpxhEcTI8aD5wmn-jqDusLStM_wFxAJJotIfnUMSByQWdttuI3um5yPwbCprcYRNpyGkmFzahTOMqLaLhx5J-CwgwJn1UO2txV6G802f2fQRQTBpd_frw2C0f8Z11aGSsAo-KJJnZrqeIBeaYOQdzPxhbeMkMyCEnuNM7RCG_xeLQ5pRiL8fUibpE7CtlpGNXjhLLDHEWWgGaQyvfPl5-ESWapxNn6-4ewi2ldII0kWgdprirW_B0i3zYlCXhchgjSL_ZwhyNMmJDV4EDn48lW_E0EbF-8_BFesshmGkkKZs79v8G0Y7obN_Uk_WlW5Xn3dLbjFKwAv-Q0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تبلیغ متفاوت نتفلیکس برای فیلم «آخرین خانه»
🔹
نتفلیکس برای تبلیغ فیلم «آخرین خانه»، مردی را سه روز داخل اتاقی ساخته‌شده درون یک بیلبورد در لس‌آنجلس مستقر کرده است؛ اتاق به کتابخانه، کارت بازی، دوربین دوچشمی و تخته سفید برای ارتباط با رهگذران مجهز شده و با فضای داستان فیلم هماهنگ است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/679956" target="_blank">📅 13:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679955">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWwVh9A33FG-OcqAAdjgXmzNPQRSL2NwhhiY0BW9GIzuCmSLDRQQr9cegwB4RVn7PU8t_jFqz4793Ec0Xt-N9QRtvEqFYy6OZQ7uGQ1fUSBZToqucSpgT0OrkF_7uIXo_UESR_vWeGbTMMaRqTa2TEcuQOlhKfSHM5YDc5D14xVmOYIeMaKY7mduI3VpZ7EeiOPmv6RTusOkTebsRB4xjsmw4ui7iO6-pqzbIvE2u37VJq3zGbWAmRIAEY0v1IA2-_gWXTH7XDuqWBZd4U9NjO4B2AxfsJnjcj1XFE15gj1WYC8dOU6RsSlcrg3xOqQ3UK3UgLZ1yfGikXXR3skaSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۹ مرداد ۱۴۰۵؛ ساعت ۱۳:۰۰
🔹
دلار در معاملات امروز با افت هزار تومانی نسبت به نرخ پایانی دیروز، به کانال ۱۸۵ هزار تومان عقب‌نشینی کرد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/679955" target="_blank">📅 13:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679954">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efnoHij_6gXvG4AhievbY0utBDmNqWWchqcIyCuhRdCxjKXs1yaJH-cEqC5JrA5-5pcMC4lzMhwWE8iq09XLnDh1oOywCo7ck8i2iCddc3TfkGHGGHWDQsgJ75_-liN0Hj3MsjvH4-VZFg1MATTQh6MRfHDRq17ZP5A7_V6DW4AaGicxLWFV0UIdE1SBlaHq28eI21zl4E0_uhdMBifqREfBXx9dGEJHq3HnAXtRYQBh8t9IHG5aPhMoIZj0pGei5rtfXGSLXjNB6Z3sRvqL1XkjXZWBcm45TJQ9rSiMB8KZ9lRQNyVdAv5Y3So6AGuUmfIsdJtvkBzTwbsuwsDtEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصمیم‌های بزرگ نوری برای آینده سهامداران؛ از افزایش سرمایه و تقسیم سود تا تثبیت سرمایه‌گذاری‌های راهبردی شرکت
🔹
تصویب افزایش سرمایه به ۹۶ هزار میلیارد ریال و تقسیم ۳۸۵۰ ریال سود به ازای هر سهم
🔹
مجامع عمومی فوق‌العاده و مجمع عمومی عادی به‌طور فوق‌العاده شرکت پتروشیمی نوری، امروز یکشنبه ۱۸ مردادماه با حضور سهامداران در سالن همایش ضرغام تهران برگزار شد و تصمیم‌های مهمی درباره آینده مالی، سرمایه‌گذاری و توسعه‌ای شرکت اتخاذ شد.
در این مجامع، افزایش سرمایه پتروشیمی نوری از ۶۰ هزار میلیارد ریال به ۹۶ هزار میلیارد ریال به تصویب رسید و در مجمع عمومی عادی به‌طور فوق‌العاده نیز با تصویب سهامداران، ۳۸۵۰ ریال سود به ازای هر سهم تقسیم شد.
بررسی و تصویب صورت‌های مالی سال ۱۴۰۴، گزارش عملکرد سالانه، اصلاح اساسنامه و انتخاب حسابرسان از دیگر محورهای این مجامع بود.
*سودآوری در کنار سرمایه‌گذاری؛ تصویری از منابع و تعهدات نوری*
در جریان ارائه گزارش عملکرد مجمع، دکتر غلامرضا جمشیدی، مدیرعامل موفق پتروشیمی نوری، با تشریح وضعیت مالی شرکت تأکید کرد: ارزیابی عملکرد نوری تنها با تمرکز بر سودآوری و توجه به جنبه های تک بعدی امکان‌پذیر نیست، بلکه باید همزمان میزان به مقولات متعددی همچون سرمایه‌گذاری‌های کارشناسی شده سودآور ، تعریف پروژه های نوین، مدیریت هدفمند هزینه ها،  تخفیفات خوراک، بدهی‌ها و نیازهای نقدینگی شرکت مورد توجه قرار گیرد.
*«هنگام» از سرمایه‌گذاری تا تولید؛ حفظ دارایی‌های ارزشمند برای سهامداران*
یکی از مهم‌ترین محورهای گزارش مدیرعامل بزرگترین شرکت آروماتیکی ایران، به ثمر رسیدن سرمایه‌گذاری در پتروشیمی هنگام بود؛ پروژه‌ای که در شرایط فشار نقدینگی و وجود بدهی خوراک، با تأمین منابع مورد نیاز به مرحله تولید رسید.
دکتر جمشیدی با اشاره به اهمیت این سرمایه‌گذاری اعلام کرد: آثار سودآوری پتروشیمی هنگام می‌تواند از سال ۱۴۰۵ در پرتفوی نوری نمایان شود و در بودجه سال جاری نیز حدود ۶.۸ همت سود برای این شرکت پیش‌بینی شده است.
مدیرعامل نوری همچنین تأکید کرد مدیریت برای تأمین نقدینگی می‌توانست نسبت به واگذاری بخشی از سهام هنگام یا سایر دارایی‌های شرکت اقدام کند، اما با استفاده از ابزارهای تأمین مالی، اعتبار و ال‌سی، از فروش این دارایی‌ها جلوگیری شد تا سرمایه‌گذاری‌های سودآور و بلندمدت برای سهامداران حفظ شود.
*از یورو ۶ تا عبور از بحران؛ بازگشت مقتدرانه نوری به مدار تولید*
پروژه تولید محصول با استاندارد یورو ۶  به عنوان محصولی ارزشمند و راهبردی نیز از دیگر طرح‌های مهم مورد اشاره مدیرعامل نوری در مجمع بود.
این پروژه مهم که به مراحل پایانی رسیده، اکنون کاتالیست آن بارگذاری شده و آماده افتتاح رسمی است.
دکتر جمشیدی خاطرنشان کرد : این پروژه با ظرفیت فعلی حدود ۱۳۰ هزار تن، از منظر توسعه بازارهای صادراتی و ایجاد فرصت‌های جدید در حوزه بانکرینگ دارای اهمیت ویژه‌ای است که ظرفیت افزایش تولید نیز برای آن وجود دارد.
مدیرعامل نوری در بخش دیگری از گزارش خود به آسیب‌های عملیاتی ناشی از جنگ اشاره کرد و گفت کارکنان پتروشیمی نوری طی ۶۷ روز تلاش شبانه‌روزی، بازسازی ۱۸ خط و حدود ۵ کیلومتر خطوط انتقال را انجام دادند و در مجموع حدود ۹۶ هزار نفرساعت برای بازگرداندن واحدهای آسیب‌دیده به مدار تولید صرف شد؛ تلاشی که در نهایت به بازگشت شرکت به چرخه تولید انجامید.
در کنار این اقدامات، نوری در سال ۱۴۰۴ موفق به ثبت رشد حدود ۵۰ درصدی فروش داخلی و ۵۱ درصدی صادرات شده است  که توانسته جایگاه این شرکت را در بازارهای داخلی و جهانی به طور ویژه تقویت کرده و ارتقا دهد.
*خلق ارزش ؛ از رشد عملکرد تا رضایت بینظیر سهامداران*
گفتنی است پس از ارائه گزارش عملکرد شرکت توسط دکتر غلامرضا جمشیدی، مدیرعامل پتروشیمی نوری، این گزارش با استقبال بینظیر و تشویق پرشور سهامداران حاضر در مجمع مواجه شد؛ واکنشی که با توجه به عملکرد درخشان نوری، رضایت صد درصدی سهامداران و تشویق های مکرر آنها در حین ارائه عملکرد شرکت، نشان دهنده این بود که مجموعه پتروشیمی نوری در سال ۱۴۰۴ توانسته است رضایت سهامداران خود را به بهترین شکل ممکن فراهم کند که می توان آن را دستاوردی بینظیر در صنعت پتروشیمی کشور دانست .
این استقبال به‌ویژه در زمان تشریح رکورد تولید ۱۱۲ درصدی، عملکرد فروش و صادرات، حفظ دارایی‌های ارزشمند و اقدامات انجام‌شده برای عبور از چالش‌های نقدینگی و تأمین خوراک، جلوه بیشتری یافت.
مجموعه تصمیم‌های اتخاذشده در این مجامع، از افزایش سرمایه و تقسیم سود تا حفظ و به ثمر رساندن سرمایه‌گذاری‌های راهبردی، توسعه پروژه‌های جدید، تصویری روشن از رویکرد پتروشیمی نوری برای تقویت بنیان‌های مالی، حفظ ارزش دارایی‌ها، توسعه پایدار و خلق ارزش بلندمدت برای سهامداران ارائه کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/679954" target="_blank">📅 13:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679943">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ad7XoWYT3WvXEEA0fO1Kg8S_Fa9GuLrAuq56leOcBjXuTW75g8PZubX20IHfWwsa1e3ev3ZgAn7Um0z-HSlgwP119BJIOvImIoopydMv25ag6toGAhFO4HMfS8HpOnqkAzzoA13ZXmy6RoGpellyxhRcbVBFp9K-C5f7k835SbnlGirVT5Naj4qU_tHoZCQ1BGHug32jQuFJBgFpvlbBHSyCZvJrACZ4gny4Ghi_YnMIhbvnWpAL_5p8k9edm6sECjsVbNrqTi3VHLHTavjJtiDLttwv_wP83lgIxD6E4hJbc7ic7UMzK9OTIBrFwIudhTdSoTJZ0qbtXKqSr8R7EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCjofCTTj4PF8szqiFkdUy5VUqOi7BrUP2xrdWBbrm1XNEcjhU1OtevdzsiYwQz7zho0NnVrrKKoOcSJ8yTGeXEyEcy9z_sEvUwmaKC0CQDPqiSNlyncgKzzODjJyMSMkXzI8_q7dWF4kbOcgfneV3ngmT2SNKEqh8nVXk3HC1uaM721KNQB8WockWe-frpDX08uuYHtT3AdeZ6w3_PGVpTiDY8id042QGU4qHTXwG4B317ESu3AikUM0ezfEn1dcYQOXZbm8EdqG-kxl3G2w7lOO5eQ126WNJbHqoO_C4Nk0_0_a7cDcuLgfehVLcE3q74da-1Mf1HeLLhuKEXwsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WMqaJV4gTNq-ywEDOMhZl-Iu3yDF3ojciEml9etrhnI95BW_ea40RXKIAgnFXm3Zx9CBglLzMg0_FXfMWRWbqtb_LZWeNeGwi5PKT9JlWrox7nGiatPo5wMFhBjyax7f_8ikCGxcxBQR6TuD9R3F853QgYztP96q7G9Kap22mkwZAEGyzBKRn-zhzxWwpx-PJb6ggll90zACOPluCFB5IdbEsnzw6YnD9RJtctbqHYSCnq7DYBMi0ENxdvYpjUnJYbOYWehUFcSmV2YSNbh0CObxsSlEWtsPGSWsx-TZZY0IXG-XyWh_0dsUni3iPK8MbE4PHGlzXHKoPmVvcS3C8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wu2CJceHM3fs_5IAGgbXkjqCe9jfegsrRDljmryUIM-bTYdBptTr9b7Wuo_BiGDWYSyzmMiDq3ij5jCxnmEfNAmxf_6Oba9RGbx7usevpmaPckcumV2HMl2KdGl8sMHm9YFQoyw3UqyocN12eRl4M5zFPIK4vm0KfvGZmUQ4BoFV-qpHY9kdalifmCSqDPiMWkf4lDPM1v4DcTLUqPYvdhuanRPtMQ3F4JQ_qG6OB5TBkHxjN18Zww_icPjEGdbaPQ-HVa26x4LZuP4VvA5BR_zhwTqRWr1dqBcakqhZHVFaZ1_Tty_ELdPQJCfR46SPfMkv9u6vdy2wBvFsFmGSNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qi7wNIIdjVgFELQDVYoBUfo7OTbqwrrUgc9vXFwGqn6RxzZoHhpT-0qoMRJlQ16tfasWFPm21AfdoQS4MPpFBuX-7XWTVQsFfCFt3qpFa-M8keCsNiwoBMzFZE-AlLGCeV59xmFQ-RvPOXKgR1uVZ1Y64z0kGJGvUX_ATkKipw6xVK4EFtUZT2H83oDkMgepNBizE4J7tMoilFnLZ32J8LMN1ooxtjScWsqYcaUb43K33kbHAuHJEjNfo-eJOU1iTBtxmscJnRUr3SxmZi9mC83kAlUCADdPbNhVDWWj0_Vv34uUIfyc239y60mRd0EG-IpYBhFq_7tbz2IxqcCuTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZNloHJ5WtFUrUZR38cybRTgNpytyVgAdyTubQv3_5As22IOUGt4zTw5sEw-r_Gz6TOuEGz3k5X_s0rnUMr0hhsyizJKl261drbPyq2wP9r9G8Efg8j_Beq3KFYTJKPfyMo2MHUPNb628N5po1tOWhWFGmyLrskE4OWe-9qINjCb2aRfR2FcQPSvOpfq_4bc8yXPuLy8SKJlmScjKqxv_dd_TdYh2VZW0cuvJNkP6hKfEExtsnaO-bCDVcQ_FY6pXv2ABjocWnpJ0RP0LBNucj_uVm2M1LtQ2ouA7LciEmum0FO2S5dds9WdVXHd01wuaCi2Dq8yBiXZ3jLGk-aJgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlQoEZDenYKmshT-QQ-DJVyGdEAu-mWWTBSgPSOBV_2ZmS6Xq14vsDfI27utCEWmcysEa7dKpB0u3o3Do1xKKC2l8upBZgZN34pv7dMmgbghzgFYr7x5JKUbVT6IFCUDr1wc_Nw-RunOJbt5XEFxt2jGZnqnEJz8nNVBApesNyDoC6SWae1ui-6OqS2ui3KumzHX9LbSRgEewyRL8ykS0nZFOgisTZpqOnzB0Zo1cbSE_NdHktZZhCp3vrc3XDPvdjUOo7b5IDe2yJiEkotulQpaBzVwJklPSGa8E70Aw9Gl5yzPjU4FGfZ1ZOCDAkN6wH9vx7SqVICJUL6xhPEUbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/faxtueQRpBaVsIKeDC2nPp0yutN7CLFjAgXyihI0_wnrHO9P9qgn8kvc1hM9iZ6wRqRyfvk5R6QyFcTNExSIj_4t5kQ5m10VkGyZqXqKUkpqlSRjOXV6_CLw8TdMY8SlQbDceuHDc4v4gO-bA1Cmn7ECwTaOBdKTO_fUCz-wN0s7hGo49Zrkl2dlQfwmh87gA7gyUIIh7Rpdl60W5HjRB-BLrRAr8YsM674A7LQhiOOyiCD963s5UgKd9Mj2VgW_hGhy3-Ig1_UrvPiRvccXgdtnsqi-TgDm04R7HXBHpLwmKucxHr4btWZ3TTdl5HW0iybYHS6u8anpNo2ZSjQopw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsz2YUc0qpnN5CPBJ2h_Q7KPY4t3YQkqdonO9uEEKDVDnSL4C1Wpw7D5zN10Wz5G9nPUjraclUXAx8aHfSu-pUdUWQeV8QCEL7HVd3MELVwsSojA9uwEcbEzMD7vbYPius0mPW2NySGuSrOmQAe4e96PQXPcedfalvz9s9YXnYwc-SmtA4I_8FhF55qQnkzzqIF4tlC3tfET6B-JabODBBCu7R7KpUW87Ca4vCAsixlgwnvI8aH0Q44MYdCQZ3DolkXx5qgAsrBM2MEEGHhvEmZo6gx7W3XoTJwv9pbZah4qn3fws0a_Jb1jVxpTUlGQDZcWWpYgK4Gd2Q1SFsFpHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حال و هوای موکب هیئت قرار در مسیر عاشقی
🔹
موکب هیئت قرار در محل تپه سلام مسیر ورودی به مشهد مقدس درحال خدمات به زائران پیاده امام مهربانی است، چندین هزار زائر پیاده از روزهای گذشته به سمت مشهد در حال حرکت هستند
🔹
هیئت قرار با همت کارکنان هلدینگ تبلیغاتی و رسانه‌ای خبرفوری راه‌اندازی شده است
@Heyate_gharar</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/679943" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679942">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXwjBIlfysuwK0JWYup7OiaFazlaY_AtvQCS2zstFHtAMPxMwJVLRKHnYmjaqGwTlPCbYsvuMg9eWkaVQ__aXOm1ftrTXv0daAShSEakFoIBLWX5ZavKxlEbNsPi2BRg6YjM5dfP5jlcGDKJb00elgckVjRqHRX3mPPkGiozKpVG2vAsAd0i3cwiV6f4mQ92N2kX9F9xDVMSqys648D9nzKi0hK6Qp_rOSisI8tKubVzgk92tdkVIboD_FMERQw97j-eeR2WR8_O-iw-SGi_KvasIwhAYgzwHSr9kvN-rnozbVi47h6IS08bgF_jZJ-t_gAwhiwg69Pmo2TvedOL4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات و اطلاع‌رسانی دفتر رئیس جمهور: با حکم ریاست جمهوری اسلامی ایران دکتر مسعود پزشکیان، محسن رضایی به عنوان دبیر شورای عالی امنیت ملی منصوب شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/679942" target="_blank">📅 12:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679938">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3ROz5xpb5mf4mhojeuzFZ9Fgjy4gDBLzSrdY0ida8pSt9Sg3Ly6jzLjZOGnhVtRKIgYudATjuzNtkD84NzE86qTFvNJ86J-a6ByCtnv200Va_N2W40ocIpfgi7EOJwBNL2GaRAMeTuYB7361cD4mk0vL5cqde66Rphd9R1GZSzTgyLuWiCEqtuxqiImHBzR36zgAOoNT6JFVf7rPB7AgP2Qpmv2T4kn81Oskvl5wgkLgSs4Zj2TmTSDzKeTJYxmf5ViCPproSed9cq6Kncuq58Hadkg_RKCzQ1mjSpweG4oU4_VEE5K2KqVqD5bdeKat97l_-pek_i5HSd2rSUe8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/679938" target="_blank">📅 12:42 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
