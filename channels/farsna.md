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
<img src="https://cdn4.telesco.pe/file/O_5R1VxoJwHHpPyHiBZWQwDdYeiB6LkgetkJemPDZNoPmJ06JefkeicR0BqDiBOHhPeOIXeeUSTA24k4FzPM5nd7i7UBuvh3b_G1U59QTl0HVMpXQ2_P5QCVM-7O-d9q4miWJ9qTMH0aYMbnXYuF5HkXOQIFqX0N_-_0M68x04WiC9ufbxnZXDk5GPUePC5sDbUyB2RlcNraWOvvIcG3h2wDdkBU41Ph0u6Ymj2UUAS5tONxBTUlojpJhrrda84V1JhKycXBnAQFkwG5gu9521uNOv2t02rycHZS0ARoV0IIoPcSXqBb6bxhPDxDMldsgbehpn0XbAhTizpj7avnnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 21:22:18</div>
<hr>

<div class="tg-post" id="msg-449463">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
منابع عراقی از شنیده‌شدن صدای انفجار در سلیمانیۀ عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/farsna/449463" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449462">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxY7OjJlxl3LBqkpwgGEJqelFS29hny8v70PhKU7LxaKx8nheb406luPHXssocJ3YPkkDFs5bMsT5J1gEFcO3Up9dXbYid4Y4CV_0PesL3c0PWrNYyZ9iQS6tXIoX_lcsp_GAFANIggycWTODS8DfebDmY-ayPd5h7H0RsADzWkCJevYufFI7oq0lZBWf9YnJfk6Fa-8ZXjZoy5diGcX7JPlFoF1dAjH_q7jjTTPoCxgjpvGs3HuVxUIKFUjdWQmdAM96rblAw24MTKbz20Ru3eoCvs6oE_SXES7VEteIzfOt4TknBZWS7REkpYLc8ErZyDuj4LTZ5KZV3reK82hOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فناوری به جانِ جام جهانی افتاد
🔹
گزارش رویترز نشان می‌دهد تصمیم‌های مبتنی بر VAR، آفساید نیمه‌خودکار و حسگرهای هوشمند، بیش از هر دوره دیگری اعتراض بازیکنان، مربیان و هواداران را برانگیخته است.
🔹
کارشناسان معتقدند استفاده گسترده از فناوری باعث شده روند طبیعی مسابقات بارها متوقف شود و بسیاری از تصمیم‌های حساس، به‌جای آنکه با قضاوت داور در زمین گرفته شوند، به اتاق VAR منتقل شوند. موضوعی که به باور منتقدان، از هیجان و جریان بازی کاسته است.
🔹
دامنه استفاده از فناوری نسبت به دوره‌های گذشته به شکل محسوسی افزایش‌یافته و همین مسئله، جام جهانی را به میدان جدال میان فوتبال سنتی و فوتبال مبتنی بر داده و تکنولوژی تبدیل کرده است. بسیاری از مربیان و بازیکنان نیز معتقدند فناوری باید در خدمت داور باشد، نه اینکه جایگزین تصمیم‌گیری او شود.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/449462" target="_blank">📅 21:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449461">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b397539a5e.mp4?token=kUVlxeDd5Z1LZcweJZ-4g5rhcSE8OL5cfFDYz55qPfKUsEwmG9MsAJfDh4KDd_YQI8COrwqIvDtzAVdFsVerOtrGF08AMP_XZOaNc0C_uronCoDfbWwSP0No-JFfJGSbXnLFtxfWM1nMvjWT-BtOaqAlrnjBWGG3XSDrRiNirswgtIj2yhqim_qP57UkYRGrps1bVbfPNHVi6GDzw1H3qhvTwiJLBVm6CaYqepovuxyvRE9TiNgTp1DzKpAsT5HOx8POgw9gTPV1NqM2n8oVs6p_ySYXnKBCTVPKy59iWP0Okw0mUeWrUWvYoPgAKvEU1nfL_nHYOjixP1DRdIeMb4jcc0bwznM6_Shimh3VAKGz0CKVRE0gcBmuzM5pAesh5n9VxWLPGj1snnlqy65Arl2UaJDv8Ln8KBcOz3mmJivoTSfHeoJMsXknJeu7DdSkmJoquCqkx0XFbmnPCGNhsMLg9vQDz0hgw0R8RMIgCWHUverpknD_ok6sExpmJJCEKmROwyyy_-6uSD1zl5dxUT2emnJ7q23fTkV7jYFSh29eVt_7lY-pSL046NH_22lzbaJ1WtnhYCe5rBux7PYowrS8xUWoWZt6S7xrW0rYG0oCkqoNL41LsgBR5Y7xY6TNP7Tvp8wgqekGsp1AV9mppkEtJ63zQTnG0kHN0siL2jM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b397539a5e.mp4?token=kUVlxeDd5Z1LZcweJZ-4g5rhcSE8OL5cfFDYz55qPfKUsEwmG9MsAJfDh4KDd_YQI8COrwqIvDtzAVdFsVerOtrGF08AMP_XZOaNc0C_uronCoDfbWwSP0No-JFfJGSbXnLFtxfWM1nMvjWT-BtOaqAlrnjBWGG3XSDrRiNirswgtIj2yhqim_qP57UkYRGrps1bVbfPNHVi6GDzw1H3qhvTwiJLBVm6CaYqepovuxyvRE9TiNgTp1DzKpAsT5HOx8POgw9gTPV1NqM2n8oVs6p_ySYXnKBCTVPKy59iWP0Okw0mUeWrUWvYoPgAKvEU1nfL_nHYOjixP1DRdIeMb4jcc0bwznM6_Shimh3VAKGz0CKVRE0gcBmuzM5pAesh5n9VxWLPGj1snnlqy65Arl2UaJDv8Ln8KBcOz3mmJivoTSfHeoJMsXknJeu7DdSkmJoquCqkx0XFbmnPCGNhsMLg9vQDz0hgw0R8RMIgCWHUverpknD_ok6sExpmJJCEKmROwyyy_-6uSD1zl5dxUT2emnJ7q23fTkV7jYFSh29eVt_7lY-pSL046NH_22lzbaJ1WtnhYCe5rBux7PYowrS8xUWoWZt6S7xrW0rYG0oCkqoNL41LsgBR5Y7xY6TNP7Tvp8wgqekGsp1AV9mppkEtJ63zQTnG0kHN0siL2jM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خواندن زیارت امین‌الله در سومین شب بزرگداشت رهبر شهید انقلاب و شهدای خانوادهٔ ایشان در حرم امام رضا(ع)  @Farsna</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/449461" target="_blank">📅 21:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449459">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‌ اذعان رسانه‌های صهیونیستی به تلفات نظامیان آمریکایی در کویت
🔹
المیادین: رسانه‌های اسرائیلی می‌گویند «به‌نظر می‌رسد در حملۀ موشکی ایران به پایگاه آمریکایی در کویت، تلفاتی در میان نظامیان آمریکایی وجود دارد». @Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/449459" target="_blank">📅 20:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449457">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a41578c32.mp4?token=Sfb2Pkbl1RmLeIqCRe7Q5Q9t4M0jU1L361s3PVBo6POUTsq0kVxd7Synox2wNeFg4Rmj_wD35tspyHrPcUorHfp74Do4WLhNq5ryrRVieRmz6339DwlME8-ZBSav2MhOi-aTnF0faIshI3YYvh-qbgboc5-XSiMoYXcXfj9qR7ctpZ8gLUFmUi_v5BVw-6Oae8IZWAE6bJdRFgadcsPJos8BzfNm5_bLw-MACrCoWDBkvbQDZ-lpVbGMhvIN1zq-Sesfkw6YNGnksRH55uUuVI_DLMCImeQXhHWDCgiHR_n0ImOFxs2yE4Gk3fUCWISi2KX4QasduOS5uRrrdzjXMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a41578c32.mp4?token=Sfb2Pkbl1RmLeIqCRe7Q5Q9t4M0jU1L361s3PVBo6POUTsq0kVxd7Synox2wNeFg4Rmj_wD35tspyHrPcUorHfp74Do4WLhNq5ryrRVieRmz6339DwlME8-ZBSav2MhOi-aTnF0faIshI3YYvh-qbgboc5-XSiMoYXcXfj9qR7ctpZ8gLUFmUi_v5BVw-6Oae8IZWAE6bJdRFgadcsPJos8BzfNm5_bLw-MACrCoWDBkvbQDZ-lpVbGMhvIN1zq-Sesfkw6YNGnksRH55uUuVI_DLMCImeQXhHWDCgiHR_n0ImOFxs2yE4Gk3fUCWISi2KX4QasduOS5uRrrdzjXMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۳ پیام عملیات امروز ایران علیه اهداف آمریکایی
🔸
سیمیاری، کارشناس مسائل سیاسی: نخستین پیام عملیات امروز ایران، اشراف کامل نیروهای ایرانی بر تحرکات دریایی و نظامی آمریکا در خلیج فارس و رصد دقیق تمامی تحرکات دشمن است.
🔸
دومین پیام را ناکارآمدی اقدامات و استقرارهای…</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/449457" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449455">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کاهش ۴۲۰۰ مگاواتی ظرفیت شبکه برق درپی خسارات جنگ
🔹
مدیرعامل توانیر: در جریان تجاوزهای اخیر، بیش از ۲ هزار نقطه از شبکه برق کشور آسیب دیده و ظرفیت تولید برق حدود ۴۲۰۰ مگاوات کاهش یافته است.
🔹
خسارت واردشده به شبکه و تجهیزات صنعت برق از ۶۰ هزار میلیارد تومان فراتر رفته است.
🔹
گرمای هوا باعث فشار بر شبکه برق شده. از مردم می‌خوهیم با مدیریت مصرف، استفاده بهینه از وسایل سرمایشی و کاهش مصارف غیرضروری، صنعت برق را در عبور از روزهای گرم تابستان همراهی کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/449455" target="_blank">📅 20:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449454">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMPJFdVm7f6MMXV7aG7FGCxu-t-QYkpd06AjN7ZAwZhQYQz0ZJ4UJ39xhPwZqNcCUmem2mhCHhgbaQgXE5Ts3W-iimO9_SiJafcvYjPeXsRasnhcCQQC5t-kdcKWpz5s55fFNpO29yzmSQGGscwrrlYvUClO2qN9DZCEF6hLkaXcoDRSLyt-tVP907ni1uY4CUDAPvD0c2A4imaKgC74eL_AGXlCbICBW4t3LA-1o5lsOYfzeBOCRY4MNVF4Th8Xk8gfPrAg4Ch0sRhp7gl9greOF3bjiJnXOO7ng1b5SfT76hI26VIg5jIKwNiFX-meSUSHvv41lswM48wSJvyk4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رهبر انقلاب: انتقام خواست ملّت ماست و به‌طور حتمی باید صورت بگیرد
🔹
به پیشوای شهیدمان عرض میکنم: ای قتیل مظلوم! ای مظلوم سرافراز! ای بنده‌ی صالح خدا! حال که با چشمان اشکبار و دلهای شکسته با پیکر شما وداع میکنیم، با شما عهد می‌بندیم که مکتب شما را پاس بداریم…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/449454" target="_blank">📅 20:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449453">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌  خبرهایی درباره هلاکت ۳ نظامی آمریکا در حملات موشکی به کویت
🔹
برخی منابع گزارش دادند علاوه بر این ۳نفر، چند نظامی آمریکایی دیگر هم در جریان این حملات زخمی شده‌اند.
🔸
هنوز منابع رسمی، این خبر را تأیید نکرده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/449453" target="_blank">📅 20:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449451">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌
🔴
وزارت دفاع کویت: ۳ پایگاه مرزی زمینی کویت هدف حمله قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449451" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449450">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌  خبرهایی درباره هلاکت ۳ نظامی آمریکا در حملات موشکی به کویت
🔹
برخی منابع گزارش دادند علاوه بر این ۳نفر، چند نظامی آمریکایی دیگر هم در جریان این حملات زخمی شده‌اند.
🔸
هنوز منابع رسمی، این خبر را تأیید نکرده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/449450" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449449">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRTuxOuoN7kZmNcgDMH9Kmxo_hZv3AmNXROPhfuBil8L6G4ByNMcATMUahWsgyAYK80OctPn0nmvsUYgPxJ7YSVVXhmag4WDHrVRX6vvtvl7uPCfSd4Z44qFEBJBtSmS9JCNtAOHWS49El0nJ5gN8HJh1CDkIIqqSCoassduNb13H_2kr_jPKw1a2wsXKA1I-4U5JwCPljK31YNixYjdyaqvMEWboB4tCRvwbCgi9_kmubp4OGGiULlIhmo5Sv8j7biEHVWgpJwUnFK4QYJxREkQ9dPipEZBDXaUpUuHJfC8gMXJooq45fPkB4BaahgkjbRvv7UleM32cm1jkhCAfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات ان‌بی‌سی نیوز از مرگ لیندسی گراهام
🔹
شبکه ان بی سی نیوز با انتشار جزئیاتی از مرگ سناتور لیندسی گراهام گزارش داد، نیروهای امدادی شامگاه شنبه پس از دریافت گزارشی مبنی بر «ایست قلبی» به منزل وی در منطقه کاپیتول‌هیل واشنگتن اعزام شدند. تصاویر منتشرشده نیز…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449449" target="_blank">📅 20:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449448">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e0923355.mp4?token=PLIxpj1PwgzAlplm0p230QTzmnC8h014Zvv4otF_hMCV4XTL_ZvS2Ch3iLsySGQsqmZRlqjjwMkPZ9vHM7Ko7iZT_E_xDBjqPJMuOUdgevvrghmeUg2tcIho_Wi6dvsAyfWFOb3G4KzPiYsKpkaDhxSm-G3CXBVyc7_kdkNRMTlBBwK3ke9SQEgkTJWNYO_av4ao2ftuCp1KmbiscbQ4tNTY4T9Fm4Md37loqLebP0eYQoXFh4U7LUakUN7TpoPI2na3GBfYe5J-IGzKNe5q4DWH5MZ6P__ehIBhuRadVNY13o98QfepWtjZYAKPpFBz4qkbUHY8r4zcOmb2a-inig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e0923355.mp4?token=PLIxpj1PwgzAlplm0p230QTzmnC8h014Zvv4otF_hMCV4XTL_ZvS2Ch3iLsySGQsqmZRlqjjwMkPZ9vHM7Ko7iZT_E_xDBjqPJMuOUdgevvrghmeUg2tcIho_Wi6dvsAyfWFOb3G4KzPiYsKpkaDhxSm-G3CXBVyc7_kdkNRMTlBBwK3ke9SQEgkTJWNYO_av4ao2ftuCp1KmbiscbQ4tNTY4T9Fm4Md37loqLebP0eYQoXFh4U7LUakUN7TpoPI2na3GBfYe5J-IGzKNe5q4DWH5MZ6P__ehIBhuRadVNY13o98QfepWtjZYAKPpFBz4qkbUHY8r4zcOmb2a-inig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خواندن زیارت امین‌الله در سومین شب بزرگداشت رهبر شهید انقلاب و شهدای خانوادهٔ ایشان در حرم امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/449448" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449446">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiMNQ9U7j002raJU7kdR_vlmdyKcSllA8NLTTZPmGplH-l0NLIZ2r80gMh5rIf6I9tIZpTHPXRuSe730MmtXYy0dkjIV8tAVf9xrZs2rfJHggJ30-igQNkagWk8hosxDuSc6xU_7D9WngoS5gTjHrjCA4hDPUihKd9Gv2lLbTCBh440nmfgo67yWSV9pldtgDrblAgzNOetEjH2EIgdf3na30R4U8ymQS_Q3ScD0QUpvGMAAOt5Z5WZFHWWw_I7IhIV7234zaHNq8fYFo-MB2Ju0GgXeoVESqrW9ti_VFsRzIs_QEBveidM5xEhxffaSWBCyFeVfx_bsG8urRkFCjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارز اربعین از بازار آزاد هم گران‌تر شد
🔹
در شرایطی که قیمت دینار در بازار آزاد تا ۱۱۰ هزار تومان کاهش یافته، زائران امروز ارز ویژه اربعین را نزدیک به ۱۲۹ هزار تومان دریافت کردند.
🔹
کارشناس اقتصادی محمدرضا صدری می‌گوید که «کاهش فاصله نرخ ارزهای دولتی با بازار…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/449446" target="_blank">📅 20:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449444">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">📷
منابع خبری از شلیک ۳ موشک بالستیک به‌سمت منطقه المینا در کویت و محل شلیک موشک‌های آمریکایی ATCAM گزارش می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/449444" target="_blank">📅 19:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449443">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abb9e83072.mp4?token=TUzP0Q_TgTw1cvvO3ilzwf_F9IQokoEguMCRvO_yVbs5tI7B1FHYXH7rT3kess7mv20NlVQX83JSkC5eROHzEvYlp5SHDE9ZbP-Xou2yBiC_B3Fqwcg8Fpll9to9cUNLwYScGz4KbsnY7eXdVC6l3DLnHIpwS2ePcP10OolOEZ5LnyIyMasGxKH5gtgg7WmwTHFUXGHhSrMEuuLekLc7iwfHfFrKDMRhxKCAs1_Rjsxf_D6qnMfyOugHh5UftJsOy03_9TwP01u8o-suG6NC9H7GjMm8EP3LfQsOVA0Idlgt-la6j3kFVFUvpypTiWE2Y6bzKNDX2hQ2yrO8VVeRlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abb9e83072.mp4?token=TUzP0Q_TgTw1cvvO3ilzwf_F9IQokoEguMCRvO_yVbs5tI7B1FHYXH7rT3kess7mv20NlVQX83JSkC5eROHzEvYlp5SHDE9ZbP-Xou2yBiC_B3Fqwcg8Fpll9to9cUNLwYScGz4KbsnY7eXdVC6l3DLnHIpwS2ePcP10OolOEZ5LnyIyMasGxKH5gtgg7WmwTHFUXGHhSrMEuuLekLc7iwfHfFrKDMRhxKCAs1_Rjsxf_D6qnMfyOugHh5UftJsOy03_9TwP01u8o-suG6NC9H7GjMm8EP3LfQsOVA0Idlgt-la6j3kFVFUvpypTiWE2Y6bzKNDX2hQ2yrO8VVeRlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژنرال بازنشسته فرانسوی: تلاش ایران برای هدف قرار دادن ترامپ کاملاً طبق قواعد بازی است؛ در واقع، این خود او بود که ترور مقامات را آغاز کرد؛ پس اقدام تهران رفتاری متقابل و در چارچوب منازعه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/449443" target="_blank">📅 19:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449442">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsxgfvMgBc-PQs9f1zBhfABeeeOfaZtRXlY0dTrDqyCB-ToML4-KNvV7TSQ-j5yNq6A1IgsGZAUgI2cqQDRDWXv0LHyIK_QXxjZ76-ad06Q8xWuiLZFa2R_oLjqbRlDTMuoHej9_HS81zWe2dX8TRGervlTb1KT2qd7wr3X_aoswlZEsjg6u5EzlR--6erAvC3-gZCdxXAY4r8HtM4X6fZW8NHO2XGnH4zd4tqpXboZmXaUMMMu1EE6gtI8NFafRbhb9BpXWq_ckHKoXj5be0M1D2uz0eOEceujQzRNDNG2w7ayNaHeYnP_rTIxLwhKTKyL4SFDjiQHE1DDwhZQEGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرود اضطراری هواپیمای اماراتی در پاکستان
🔹
یک فروند هواپیمای باری بوئینگ ۷۷۷ شرکت «امارات اسکای‌کارگو» که از اوساکا به دبی در حال پرواز بود، پس از اعلام بروز مشکل فنی در یکی از موتورهای هواپیما، مسیر خود را تغییر داد و در کراچی فرود آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/449442" target="_blank">📅 19:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449441">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bca0ef46b.mp4?token=XHGoI9wcI81igrcYfTUKkPyJGbAH97_vnY9qgt9jjcutEz65Y3aPkzIWDkzGByHdtGeFiSeXSVw3k3pIy0H9HaWqlzpJ8_qR__sJOvme31EbrNeU7qhHCtcdNKmVEiRWlEO84CEQb7H63cr7-Re-QeqoVzhtYVraMOlY5OacKv3MIYjaHf52u4bU0JMmBiXEBIl2KDP_xui9LX9K8buf1EgV-1aIXjn2Y3BMKMrXMfmnvvFYhJ2VEZCN5ruhCKGIRTeFlgMl5wPFcLO2ojsQAQDW90OFIsUsizT1lx_RMjIrV2YpYWa5KHOFNnACOuhZ0rLIX-VYqZq1t5iJHl7_xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bca0ef46b.mp4?token=XHGoI9wcI81igrcYfTUKkPyJGbAH97_vnY9qgt9jjcutEz65Y3aPkzIWDkzGByHdtGeFiSeXSVw3k3pIy0H9HaWqlzpJ8_qR__sJOvme31EbrNeU7qhHCtcdNKmVEiRWlEO84CEQb7H63cr7-Re-QeqoVzhtYVraMOlY5OacKv3MIYjaHf52u4bU0JMmBiXEBIl2KDP_xui9LX9K8buf1EgV-1aIXjn2Y3BMKMrXMfmnvvFYhJ2VEZCN5ruhCKGIRTeFlgMl5wPFcLO2ojsQAQDW90OFIsUsizT1lx_RMjIrV2YpYWa5KHOFNnACOuhZ0rLIX-VYqZq1t5iJHl7_xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان رامشیر در جادۀ عشق به سوی کربلا
🔸
کاروان عشاق‌الحسین(ع) شهرستان رامشیر در پنجمین روز از مشایه پیاده‌روی خود را در مسیر آبادان به کربلای معلی ادامه داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/449441" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449440">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در بندرعباس و قشم
🔹
دقایقی پیش صدای چند انفجار از سمت شرق بندرعباس و محدودهٔ دریایی قشم شنیده شد.
🔹
همچنین اهالی منطقهٔ مسن در جنوب جزیرهٔ قشم نیز صدای چند انفجار را شنیده‌اند.
🔹
ماهیت انفجارها هنوز مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/449440" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449439">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3af5e768c4.mp4?token=dvjPUDWkdouHu2ghbLqzK-eCfX3nZp5rVozAEGcby--wbYftwlIEHCulOiblV6Eg-gN14SnWLpYRgS5D2Nmwxn3DTXwy11NpuOsLmbgILpKUz60Tt6_9RkRO--ee-7AgyoESiRdx2m7GRJsO-WPM0WPKxvu2lsU8rh9aEHEvUpC6_elK6T2uciGfqFVtptIcM0L7EWNlf5iU6qU620xEylxa3Ho0ETqR66S9Ae2hw2jMYOCLWS33MkPgJ6K_r29fhB8E9TfOOZ5teoFF9OUrMlHONgDUT-AajgdJNG7wiej1Pxdg8myQwHUuKQhfQRmHKKyceCfE4dKZzf03CdsnlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3af5e768c4.mp4?token=dvjPUDWkdouHu2ghbLqzK-eCfX3nZp5rVozAEGcby--wbYftwlIEHCulOiblV6Eg-gN14SnWLpYRgS5D2Nmwxn3DTXwy11NpuOsLmbgILpKUz60Tt6_9RkRO--ee-7AgyoESiRdx2m7GRJsO-WPM0WPKxvu2lsU8rh9aEHEvUpC6_elK6T2uciGfqFVtptIcM0L7EWNlf5iU6qU620xEylxa3Ho0ETqR66S9Ae2hw2jMYOCLWS33MkPgJ6K_r29fhB8E9TfOOZ5teoFF9OUrMlHONgDUT-AajgdJNG7wiej1Pxdg8myQwHUuKQhfQRmHKKyceCfE4dKZzf03CdsnlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
️مدیرعامل تامین‌اجتماعی: از میان ۲۹۰ هزار متقاضی بیمۀ بیکاری، درخواست ۱۷۰ هزار نفر تأیید شده است
🔹
بیمۀ بیکاری ۱۰۰ هزار نفر پرداخت شده و باقی پرداخت‌ها در هفتۀ آینده انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/449439" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449438">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnomjObrcSSftYbiSQgeedYMPWGMDSf4tICa3IWuIRCY3W9lRNOpndZZGAaALxv4JSkFl4A9Hr2j-FB1vp3hiFq-aiscqNp0PojxpDula7LY-HK-KKtf3jvdzY8yyyv498KoqyJxu8ZKOcJzkLiVd2RrduaTiCCokP4FMNStwNSQ8EjAv09y-8OlYn8uVMef18Q_QZO-StOTYlvKBvKDbtHK0YGovIFFW8p5C1KdM-lY6OXFXrp6-CyLDL9KNer1sfcgVwSrFr6P3Md1HgdpUvimxnavRPQzIgjhOiguTnlPBJs2VEZOPP0NynGN8VJGFEEqwPCRdrfrL3H4h6-PoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات برنامه‌های وداع، تشییع و تدفین ۲
شهید بسیجی در مشهد
دوشنبه:
◾️
مراسم وداع: همزمان با نماز ظهر در رواق امام خمینی(ره) حرم رضوی
◾️
مراسم وداع: ساعت ۲۱:۰۰ در میدان سلمان فارسی
◾️
مراسم تشییع: ساعت ۲۲:۰۰ از چهارراه برق به سمت حرم رضوی
سه‌شنبه:
◾️
مراسم تدفین: ساعت ۸ صبح؛ پیکر شهید سیدسجاد علوی در آرامستان خواجه‌ربیع و پیکر شهید مهدی هنرمند در مزار شهدای بهشت رضا (ع) آرام خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/449438" target="_blank">📅 19:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449437">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZyZo_axVixB0QvZgxTcadAFkfTC-_rNp3nWUtLgXq9FSHUD9y_lfOMSiUSc4UG3U8imIP9AB9J-i5cJLwMd3UuqsIo7djMtKtCVPHuSiQ7d8ggV8EuiasjjukhP8vN3afpdWCF516rR-N_Ri45lazadMRPwoz3taD9RbqYrCKmS6_Fu7QG_gWay_C3Ng93crvZNIztblel-zAO5INAkg7VU8xZ6CpmXkI4dQX_5j7UAUr4pmKuKRll7ydwL70EzF3jhW4oi0-K50otl2Wt2O4AdlD1cLThfC_oj1y_KpFkBTXsTwgcuV4Hs-p_fuf17TSKnQZAr7APdsoZlyRtKdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع خبری از وقوع انفجار‌هایی در کویت خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/449437" target="_blank">📅 18:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449432">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yrd4r6xaS4ODt7TjqnAv0J2nlIRHjBHqxofhIda0Siz3NP_Hi-RGFqqQUb9TavEVZqXv7FpT3raa9JKh32KQF5yMVMG2o-3pJm1zZrGEqVS772dJ1nnXp58C9pS38eMoiOlOt4Fp-EV8eTJruq4QX1Fj9Ksh11dpetP0r8ZeM1EzQVwvz70NAFA5dMSK1DlxtuL_yv0wmNpUK7uO8vdO0HftYSm0CDhrhwx4vRXdXtx0CuCSwyFf2XSE3D8O_QjbDCvEtZ7I49fvRVYkbALGqTCSyKMqAKeNXGMwwn_gzAvfZF7XvYzwiQJSKMDJIkDcmFk1t2zoI21bfgLTe8NGRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kjM1HjF-aZV0xdDX84AND2W-c3ywkdBBHOEhTAVlkrgj8u_abQ702FYUuCxF1j7CRr-zbylIi-BkaCHXWDXKKNYRFPJY3TXnHx584KBXY1x158DppmjPVaAOqRveCG74rAEwi6sB_F1QAwXwso0NKarzk7H_iKKmqQsSspAAc2KhsJ9_zxVn11ECZ2dJx4o2GqAfMC9wQImybKERW3oZ9T0zcy9NcYRTvK5E4Tar6fHbazdgETOiOUhQkyNSfc6XP1W1ivw7iIRixrCsADVlMwHqEjGOKhaXE_TvkN0b69ajzhWJDOEl8YzfE3hHdMUGw9_ihziPOb5B3g_b4ocmqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmT1aP4GL4Zi0gzxw8e7qRqKXbXN2lqbSc8EQFusJWe39I4H6VMa4sOIfPwAoF1m_68zekKTNuNOzjbfasvXb9lbm7125keF36bvgcn7P5IYdrQWLfJT46ryAwL07PdaYkNpL7lVdVeWj7T9gLdZmePd32sdjy9k7ntJz79VFcdQEJ5uQvelKXOulrzEaBWkXcefkZu5_0abTDnX-h4gALG-2BrzKhz6hG6sTQgqwttUvVNCNbTB-u3CP2trt7_6njxWcJiI3zWW35ysE7l4e6L4fPG3_A9jxDPVCxp-bzwrKrKVxV9lwQy4sJosFraijWkSfNjjdv1ZmRpi_1OoEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UGgSXTkm87gx1_GCznQBpWcCfdfUtYajRsbW5CuqIg93P3f0uEYeks7rvoLvLLiwnyo86vCUyxhhPR88f7QZ__LQLwG1tYT4HcuPEFckAgqNIwnMYmZ0aEpMLcOps1KlyhSgBhI98MmfT7GFbotgCEFOjP2ddiX-FdCzVo-eq9YUi8LCY85EB0-qWSofz5UXcA3SKAv1WHKeKsYJGKTFyvqa7X-GiSr2j46IVFy5_IlcRhpDN5nBoy16Icr8JWWVL_ADvDfYYfJ_q8TuPrgWMCON2nzsWihOpJAiTGtDdolQiqA8eIwN4mqdYk9S_Fi3FqPT6V02leHGiJOB0h8WRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KRlTitGqq9UA8lFBQ1A0Kr-WBBwuCN-aCKHOwI8radaWhXp-3Xsc9fBGHfQhXb9zcwKN7E7RRysKigvVvC_IWMoAltdWZFgoxrPD2UXtKF9SNcNGkTQMb5sst5Gsa0JTvmcoIe-_rILuPXGj3MXEvvvJOcdX3RY7TBAodjb5e2Z36S2su-x_rNKifjtuztWM0R5_AnakyCZ3S98p1uTJkZk1SAFGW_RRnoQuQMuEKuKv3XH6t15TR-v1ZjP97594CtdNFAOcEmnRWGrCW6YCHmZvb-KnYPgMmS5OGKpBzQtQPrB0dB-Kn5VAktbjZhD846T73u9u5dMG7NNQI-vu4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
این عکس‌ها بهترین‌های سال ۲۰۲۶ شدند
🔹
برندگان دومین دورۀ مسابقه عکاسی هوایی بین‌الملی سال ۲۰۲۶ مشخص و عظیم خان رانی  از بنگلادش عکاس برتر این رویداد شد.
🔗
مجموعۀ کامل این عکس‌ها را از
اینجا
ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/449432" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449431">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
منابع خبری از وقوع انفجار‌هایی در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/449431" target="_blank">📅 18:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449430">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GV2cpxeMUVGJBh1x1QTDN-qxFFgg9LNt1nZpmrSwLb_EmhsTNPq9HeWCDj5pKC_WoPdrt3yWSPMOMD8PFv6jxmEMpkKN5cb-_BmpJ65yJhpf7mtkQ7kUVhHZspLRXZZNb1mwu7BFJfSQtFMZHkoDmizeFNHwS-LlSo59QVMrZqytP42sL9NCL0BFmTH-TXAeTarlbwAtTHRtEQNJpOoxuT5lm1xvCaVv6S5a9PCIXNYXxkSkjaEAV-xJQjsySKFKdyDeN3KN2XERbF5R4syzxUrSmhdi41qcOSw0ZG_DVflTUZVy5CYfFhgLACi4D3s6HDJ5CM3zB7Ggin8LOMEbCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت‌نام زائران اربعین از مرز نیم‌میلیون نفر گذشت
🔹
معاون سازمان حج و زیارت : در کمتر از ۲ هفته از آغاز نام‌نویسی، تاکنون بیش از ۵۰۰ هزار نفر در سامانهٔ سماح نام‌نویسی کرده‌اند.
🔸
استان‌های تهران، خوزستان و خراسان رضوی بیشترین تعداد متقاضیان را به خود اختصاص داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/449430" target="_blank">📅 18:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449429">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjvhVCQKSoYiozJ3NrSBh2EFmZgAnIR4By1b-lL2oaDEo3nE5B-NQE_h1SwSvXruaXiEwee5mxvsTbh35lZQIMV3-OxgMaJlfDCtF46MUqJYZHuhz8qfURJyuiD3R-HRlX7v4N3D5cJm0jWB1rk64r7HaKK1pZfo3n8v0EoRHSOSSQwKXOb2muYs4mccFEkO9xxHvuk819UfxpAHPXzgRkrWyqqAUg-TaronvyI4-206jRMbYjIewbmhtJZtMKDuDmsdVerDvQ7cBfBdG6uRKrQKY4tSh3cGFduUF9FURvJThkDefG2_-jNMsfRpx3UhXruQf938yBA0Y0qdGIdgsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف یک محراب تاریخی در پاسارگاد
🔹
اداره میراث فرهنگی شهرستان پاسارگاد: یک محراب تاریخی در جریان عملیات ساماندهی و مرمت کاروانسرای محوطه جهانی پاسارگاد کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/449429" target="_blank">📅 18:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449428">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27759874bd.mp4?token=ZGGJmVJNU6OzsQ0LxF9KAmjm8oWsvIQ2YNRxGOyuv8q2aBUlzKDdxEYdCHeZ_82AgRIiJrRWVLetG6BKMIfOhd-fEd2V5PZDXsWw6peKxfyE9HjAQGMx-QNh99jc57Fle95jHTJwnbCUqcR_1W_0NVNf6M2UMXj7aV2ALg09Oc1-5pVDZDDXuvjw0MadPNpZpAZzBhAG3m7lj1-iMLMo8mI_vrBaepkHmPMg2v2f4aSbTchPByEr5sseejqfDzhziBR2X_4gpQibLXX00I-c9eUI3q8QnMutZgnkmHZd3TgMOonSp0js4JmuH_H3qAraZdxNtS-bdCjjbsskkX-eZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27759874bd.mp4?token=ZGGJmVJNU6OzsQ0LxF9KAmjm8oWsvIQ2YNRxGOyuv8q2aBUlzKDdxEYdCHeZ_82AgRIiJrRWVLetG6BKMIfOhd-fEd2V5PZDXsWw6peKxfyE9HjAQGMx-QNh99jc57Fle95jHTJwnbCUqcR_1W_0NVNf6M2UMXj7aV2ALg09Oc1-5pVDZDDXuvjw0MadPNpZpAZzBhAG3m7lj1-iMLMo8mI_vrBaepkHmPMg2v2f4aSbTchPByEr5sseejqfDzhziBR2X_4gpQibLXX00I-c9eUI3q8QnMutZgnkmHZd3TgMOonSp0js4JmuH_H3qAraZdxNtS-bdCjjbsskkX-eZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حکم اعدام ترامپ و نتانیاهو باید صادر بشه
🔹
اگر میخواهید به جمع خون‌خواهان رهبر شهید اضافه شوید
اینجا
کلیک کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/449428" target="_blank">📅 18:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449427">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1bff11a8.mp4?token=Bq6skfv_Kzx09Vte6slJI0OyAHacD2t9zwj1jiMeOfUu-Gi_7DuFB9ndTolb974KqpceuAEiXK8IRgEeRwlHKLsc62skZkdtTSmknpowGXCLOQwNhWhHEcT5hnEgu836-QQ8KZdlFIeDiV0QZmlZm7tym5QWcp3MJbafMNdO7GWC6wONgo1ec_kq9NOgUlT9f0THqEVaZq0pJ3ietB8IUgrcdNGqeBa_q5HrmujY2iEi2QlG70A-TWQGvPGxKHaCs7Io5ICy_PfCRlkjw0AGD_mCzGbGjmuFwreyGig_1K_CNZIJEUXANashJi9QslOdJgwywij7sl17NopsP5rJkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1bff11a8.mp4?token=Bq6skfv_Kzx09Vte6slJI0OyAHacD2t9zwj1jiMeOfUu-Gi_7DuFB9ndTolb974KqpceuAEiXK8IRgEeRwlHKLsc62skZkdtTSmknpowGXCLOQwNhWhHEcT5hnEgu836-QQ8KZdlFIeDiV0QZmlZm7tym5QWcp3MJbafMNdO7GWC6wONgo1ec_kq9NOgUlT9f0THqEVaZq0pJ3ietB8IUgrcdNGqeBa_q5HrmujY2iEi2QlG70A-TWQGvPGxKHaCs7Io5ICy_PfCRlkjw0AGD_mCzGbGjmuFwreyGig_1K_CNZIJEUXANashJi9QslOdJgwywij7sl17NopsP5rJkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«عمو لیندسی» که امروز مُرد که بود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/449427" target="_blank">📅 17:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449426">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BC1njZ74pYCXI5ukckkBTdnsPSv-jLh1NmaZvvYu55IWeL2874Ip2pGq41Q2ljtzWH42zO8cYcJbK0pUOdjBghkkJkPiF6XTt8aR2HxQB8by6ME916CnZgDr6HWQ2mA3-00ZMPj81jj94eK4W-FK3EUwt460aLGdc8hodZr9Dk3ubBjEKVa3CFxtfpGwSSKbDPmKXtpWBBdK_o13-2oUN559EZj1Ti_H4f441giTbpkzCPc5FmFHDOlMdZ4w_-vzTG1TXkamMeoICZcXu4WKdOMWDjd1Tr9RCGSYUMRK17M7qi8-KXVS0v6Po5plBKp9w4JopdV4bmoLoJ-2ygM5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین چاپ بافت زنده در فضا با موفقیت انجام شد
🔹
شرکت زیست‌فناوری «آکسیلیوم بیوتکنولوژیز» برای نخستین‌بار موفق شد بافت‌های زنده کلیه و کبد را با چاپگر زیستی سه‌بعدی در ایستگاه فضایی بین‌المللی تولید کند؛ دستاوردی که می‌تواند مسیر ساخت بافت‌ها و اندام‌های پیوندی در آینده را هموار کند.
🔹
نمونه‌های چاپ‌شده اکنون به زمین بازگشته‌اند و در حال بررسی هستند. این فناوری هنوز تا چاپ اندام کامل فاصله دارد، اما می‌تواند در آینده برای ترمیم اندام‌های آسیب‌دیده و تولید بافت‌های پیوندی به کار گرفته شود.
@Fransa
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/449426" target="_blank">📅 17:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449425">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPeeQi5nZtB0pz1o7XC-Liy4hZ53kjQuAPVCUtwIbnN0sdUatHiNx_z2gBncyIlPX13oNOXQfn8zJUeGee4hU-HxTJJFJtF0rfwP4Zip5yUXZoHli-wrs9imU3p5Igi7PoHDKBd6N9m52qQDWQtJzD3HMX6070snhUmmMg7CqCx_fKvov0vrftxXch8zgwRJELmArcY0WayDmaXOO4TqgnXI093hP7p4iURaEZOaifZ4YNqwUQPDTHaMB32YQ3BAcPsIE_-jq5a4we4LCrOtKxx9T4YqgHHzE8KaIT9OXGETWpdcvXxgHv_wX6dlL87L_Wp3BlATYBM64yq-jg_b9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توهین مجدد ترامپ به ایران
🔹
رئیس‌جمهور آمریکا دونالد ترامپ در مصاحبه با ان‌بی‌سی گفت: ما دیشب آن‌ها را به شدت بمباران کردیم. آن‌ها آدم‌های شرور و بیماری هستند.
🔹
رئیس‌جمهور آمریکا ادعاهای خود درباره توافق را تکرار کرد و مدعی شد: ما دیدارهایی با آن‌ها داشتیم. آن‌ها دیروز یک توافق را پذیرفته بودند. یک توافق عالی برای ما، بدون هسته‌ای، بدون هیچی.
🔹
او مدعی شد که ایران «از همه چیز چشم پوشیده بود»، اما پس از جلسه، حملات را از سر گرفت.
🔹
ترامپ در حالی به عدم پایبندی ایران به توافقات اصرار دارد که آمریکا حتی به اولین بند یادداشت تفاهم عمل نکرده است.
🔸
نقض مکرر آتش‌بس از سوی آمریکا با واکنش قاطع ایران همراه شده و نیروهای مسلح ایران ضمن هدف قرار دادن پایگاه‌های آمریکا در منطقه، بسته شدن تنگه هرمز را اعلام کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/449425" target="_blank">📅 17:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449424">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wn714pM2xii0diKyjYlbdRIKtcC7Q6BLr6PWWFWXl79lVI0egUaP4uPsd_fHe2uU2pgXGTQ9rehSZOR6ASSe6guk4Dp_cOfS1uvFwb65a3EQUtRJvrx0bGPR6CfzzTJCjMWW92g3A7tCn4ZlMMuA4w6YgLzLCYB6BBVgBqAwjjTLHpuPt1dt4Skwh1RSuZzgUbmkMxsXh2oJcuCWuLQ-Dps8oG9eSHovL2t9RZ7TLJJrqu5c9bmc5h7cvU5VSNg0qGmSjS3rY3-bAC2oxXSg_pgQcieHC39cGc6E8VfWErIt7_ch5l32lOIkVwBqLxR0_CvTPRb7p_o_EJewY_KIDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوت امیر سابق قطر
🔹
دیوان امیری قطر، نهاد عالی دولتی این کشور، روز یکشنبه اعلام کرد که امیر سابق این کشور شیخ حمد بن خلیفه آل ثانی،  در سن ۷۴ سالگی درگذشت.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/449424" target="_blank">📅 17:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449423">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36d0e88047.mp4?token=SXRDFgdqxG7LzHpvnV5fBJ591B2Tb1lr4aZ6wwwHCGONQYx5pn0je1p7RlDU5PmErz1SXmPoSInnOsAn8L5uPUZdlPy_pCpYq_u_47hINSX8kaIkJFI2XIH2gbG2dd5NE1xOuxnIZUXGiyWd_6Ojo_K-AGGq_u001u9UdYYjFs3DmyObQTNOIkQ3JB_dpLiseTuvavpVfS7ge8Vy3tvrpjGK9x6sfCxTBCVB0M62pP2vrt32LXOe5KpWaBd1vveOdIAQsRkzXzMKAmw-k4Y0GqMAiKq0PQeI-trX_pAjZr3NG1nvSPZucubHcZzyU2r1qkug9XaDLPG0XGXy2bLtSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36d0e88047.mp4?token=SXRDFgdqxG7LzHpvnV5fBJ591B2Tb1lr4aZ6wwwHCGONQYx5pn0je1p7RlDU5PmErz1SXmPoSInnOsAn8L5uPUZdlPy_pCpYq_u_47hINSX8kaIkJFI2XIH2gbG2dd5NE1xOuxnIZUXGiyWd_6Ojo_K-AGGq_u001u9UdYYjFs3DmyObQTNOIkQ3JB_dpLiseTuvavpVfS7ge8Vy3tvrpjGK9x6sfCxTBCVB0M62pP2vrt32LXOe5KpWaBd1vveOdIAQsRkzXzMKAmw-k4Y0GqMAiKq0PQeI-trX_pAjZr3NG1nvSPZucubHcZzyU2r1qkug9XaDLPG0XGXy2bLtSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگنده‌های رژیم صهیونیستی، منطقه الصناع در غرب شهر غزه را بمباران کردند
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/449423" target="_blank">📅 17:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449422">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeGIpA6QrJ5gmq3ovCYfQTNDIJPI9K4U79rZazWsw3UnSbYVvj1p4g3XzTWSSqiTxKv270BjlvpwGkcVjlXxID7ACmugwZ18vsf4Bh4UGc4_WjEr0SnmZgaBNxOswZqc4nljga-OzEoQkDsfLyqgnVmHdYo8dRoKwMlMvRd_TNpFMsB83aN1dzFSErXR27NljPDXpEs4OKk6WR0D5YB_e46ckjpwYjtY3vLZ2rCifs0OpRIBLe13udwR9cQeUD_aF_GSEP3PuMavnDNowGxUy_SDVUoorBF5v6HPkuPSno0TXmfMqIRxUFneA5DGxDTYWjcX69oJLjoaIMbwyrrZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش محصولات ایران‌خودرو بدون قرعه‌کشی
🔹
ایران‌خودرو از روز سه‌شنبه ۲۳ تیر، فروش اینترنتی محصولات خود را بدون قرعه‌کشی و به‌صورت فروش قطعی آغاز می‌کند.
🔹
این طرح در دو قالب فروش فوری با موعد تحویل ۳۰ روزه و فروش فوق‌العاده با موعد تحویل ۹۰ روزه اجرا می‌شود.
🔹
پژو ۲۰۷، تارا، دناپلاس، راناپلاس و سورن XU۷P از جمله خودروهای عرضه‌شده در این مرحله هستند.
🔹
متقاضیان باید هنگام ثبت‌نام، وجه خودرو را در حساب بانکی خود موجود داشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/449422" target="_blank">📅 17:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449421">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be12894915.mp4?token=eFw6TrQSasC3r3mXju5LXgOSYe8XsTY_RSoLmnLPLb2Cp9EU0szuldYh4DJCVUJdnfHxWKbyTEywoE4XR0QqlHUbjE-3s3YdYMV_-hLzIvJMJ36kuC2Vy2U__Bkt8e7SV2yvDuPh8LkZheGt5VKPIWXma8ojr6XpQTiGskK8kFPRnkBnsryrjPjG3p-eD-DbqBkXds0s6JnHITsgcYpYvjljE9Yp6EkbeeH_Q5cTPM8H-K-K5ieLO_uf7Qk-lPOunvP9nYXFwuY_CUSeP5CVIUvDKTTpOfdUDEu48o5m1Xm9IX39lUa8fEYsafpRxzfaY7oILI7vdMk_NjVH55i-BrNfmP4SOuJ2h0Pr-Gb45ZeJoNBtDfsC_Jrssa6B8i8cwGmXq8gIaPIL-MR_pH7mdUkSEfSrLQ4v_eM6wL959fFThhKv0tDRMmCUrMR4CyZ8YqmCiM1oJ8irjDG0hyHVLAPSXIIfvcHZbcdKCWs9-ZKODpY9PvtuYN6r3f-5vrMBbKx_46ZnqwG7GZmi7zVWi9D0f__2oXdCZrMcEgkXaGXKaeEuDgM3v-y3g6pGWj6i7rgmNLf2Pt9D1VmiEOQBN-M_TRF0cFk5dniFvyhMejnXXdkRfFsmktWk2H7wpIQGgUIUvqzkUL_woIQG48nHIVWYIYw1kHlFezJrlNcA0Zc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be12894915.mp4?token=eFw6TrQSasC3r3mXju5LXgOSYe8XsTY_RSoLmnLPLb2Cp9EU0szuldYh4DJCVUJdnfHxWKbyTEywoE4XR0QqlHUbjE-3s3YdYMV_-hLzIvJMJ36kuC2Vy2U__Bkt8e7SV2yvDuPh8LkZheGt5VKPIWXma8ojr6XpQTiGskK8kFPRnkBnsryrjPjG3p-eD-DbqBkXds0s6JnHITsgcYpYvjljE9Yp6EkbeeH_Q5cTPM8H-K-K5ieLO_uf7Qk-lPOunvP9nYXFwuY_CUSeP5CVIUvDKTTpOfdUDEu48o5m1Xm9IX39lUa8fEYsafpRxzfaY7oILI7vdMk_NjVH55i-BrNfmP4SOuJ2h0Pr-Gb45ZeJoNBtDfsC_Jrssa6B8i8cwGmXq8gIaPIL-MR_pH7mdUkSEfSrLQ4v_eM6wL959fFThhKv0tDRMmCUrMR4CyZ8YqmCiM1oJ8irjDG0hyHVLAPSXIIfvcHZbcdKCWs9-ZKODpY9PvtuYN6r3f-5vrMBbKx_46ZnqwG7GZmi7zVWi9D0f__2oXdCZrMcEgkXaGXKaeEuDgM3v-y3g6pGWj6i7rgmNLf2Pt9D1VmiEOQBN-M_TRF0cFk5dniFvyhMejnXXdkRfFsmktWk2H7wpIQGgUIUvqzkUL_woIQG48nHIVWYIYw1kHlFezJrlNcA0Zc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۶ راهکار مردم برای اینکه امسال برق قطع نشود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/449421" target="_blank">📅 17:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449420">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8344cf58b.mp4?token=f7GlSXRaQIp4JdiK9nTNvxYFvKB7fudjJKyXV2WHrmI99QafLdQV2R6ZYhXzh2DEC_ciusQMp0ylIjtpDQt5Nf521gw_zRp-Fhl3GbnmgHlxae2dNvYM0O_YkGQgH9qjb7xTpIMFaMsyfdTvo3DEuTBukZPMHVxsAEihDk7AqSW4YL6C_i1zp0rjbE_Dv-9-tjHev1UpS8oeLfe9IZk1vprTKSW9HYHBZO3Wl6RpmyzdWHfIXDHdLB5zIoSHpoELlvaGkDkqUzlxW2mETdphJwmQHOJKM8puRPakobvBy9IoxQMzARVsASMzFlawcl9PkpG_I1N3ky4kAMGRn1z8GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8344cf58b.mp4?token=f7GlSXRaQIp4JdiK9nTNvxYFvKB7fudjJKyXV2WHrmI99QafLdQV2R6ZYhXzh2DEC_ciusQMp0ylIjtpDQt5Nf521gw_zRp-Fhl3GbnmgHlxae2dNvYM0O_YkGQgH9qjb7xTpIMFaMsyfdTvo3DEuTBukZPMHVxsAEihDk7AqSW4YL6C_i1zp0rjbE_Dv-9-tjHev1UpS8oeLfe9IZk1vprTKSW9HYHBZO3Wl6RpmyzdWHfIXDHdLB5zIoSHpoELlvaGkDkqUzlxW2mETdphJwmQHOJKM8puRPakobvBy9IoxQMzARVsASMzFlawcl9PkpG_I1N3ky4kAMGRn1z8GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هماهنگ‌کنندهٔ ویژهٔ سازمان ملل در امور لبنان با عراقچی دیدار کرد
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/449420" target="_blank">📅 17:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449413">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MW9JUnq-AuvfuBetPvoe_q8KFTmaobKTXH4bBSemsZeS4W6d94osT4_27Dhv_e6pA7DEbxeFy7WLsljJAaKI0oNYsMRvQNg7EyMoaSjR8UHq1SkrnQtCoGMDQIYtQ_p8IGXQ0drNw3mTWlyZ51e8UBKPCgB2rnJ4BeZtioW1NWnIjfBrRIXxd9zZtWNfj_IB16to76WCUtZRe-tFjcTT-nZ7j2fwbH_j1dM1qfWxW1kf63FGJyyCTEyu6AiRJ7XwDY_kSce9RZlQ8rs1WqU2ZjzbU3P1pYc7g4ND6wGETLoUKtd4jtlwsR5thkjoSweWWvFdfESc3aMGdHIeKf0SwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lxVGfAprzKUG1kqibTmFibEwW76sG1R8RoBewRjDMybnAXXDhdx3-KagALotuMON_Z2DcTkoCy2WBmE-GM0G8Rp7BmHKEz_krrKoJ56pYvDXPSlOJAd7jGC7pMOt2sqemmhG9uVvQZIjk1VLoXPZVdKwH6MlFaisoHfqjb2t9bXoVJIIVoxoYq_niZN-nN0qpwgrY_nWyPOid-f7Isr0Oo7WGyYpUtSIkemNaiv3sby-s-QqnoV-2k-59sj3TO2SbbaJDRJgQtekWA44iMWCkEj6ADqluz0KC_juqAVQ3xCXCsaBI--jVkhPIEOd7vP3GuTjsxA9GkOusuHeuU73-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tMzTJDMOd77-CfJA_oB30Vlqy6AT5Ai2MGgI7_C1pTbh2tNZE0mLmR6jIMlUyBfym2BgSllokjYdwQWSO9NKos5lj746RpmBY0efX4w2tc7eGnLzqve3FVz_GfnRJGvmPu0jz3lwd7Q9LTzdhcKIY2dQFCoOYNlWpmZB5ohdt4FHi1miCIzdp1XNOpjbjbNmZcgBPO8Kmnzcl7PkDTeOruGqG94XCMIsFgd7mYeRpYmLxGq2KTin07xCXbMeLxzz8dtjWb9IOe4mQlYedemlVDmcSft7PrBtutqEfLItzP9gFL2BeKDWiUKG7k9DiYiP20fb0hXYFe0B-r0VQ0Y_yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iNcRDLGYL6RJ8mf5_8Yqvx46c4128v_Y7ZwuRniSBtwLbz22gyw0mXC-03410VDk08N9hdzKYpQf68Ku4dQOOe0Fk1ftx3-mJ1_w49NZuprgPCc-He10qCIhcq03TUpbZUHmDG9plaQHK57ZKaiDcp06pVmv2fhXQB879dCdeYl4Wo0o4MRkKl5kW0tsXcR7JT-TrM_hfn95PuKOutS4jd9uyD1witkBkVj1stapTlKNSyDAJfaxYOO78IPAA-hp-V_GjQtGFi3KyKEeLmrQnPyYv46OHhBaVBTOyfLPLQ-hwvE48Bio2d2VipW_GPadQCRgCtupfgfg0V5Xs-2Itw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGRsHP3CNJKEXN4Te4wlXopk6ue9LrHutsqYEoy4dTv4Tm4yvoLLAGAjfD5JreVdAHoD1NVX3FzSjcCCMA7vKY3hEUriEa-rzmu8H9smdDL2zMc5kSmm-lXWkdeqAedRmKePZNRVnlUXBcQWMBBlplbd4kgsRmPE-TOCFSoQBodw9AyMXcPFnWY9G7VdkDJ8C0mI5emW741xx0EHnChmd9WsZATIUE4vZolozGA5-JE7_yMqo07FSJIklSboOar4XMSFTUhYf1kH0ypB0wKcaBawn42cnMPDu0u8jiD4d9UTj9hdihkdEhhnddops6zxDZxqSfRpPN5Tj0yyqmRniA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EiV8h3xvln9kb9WhHQdYPxueJQjr-I16qPoa8HnAHEkBldatJC3nWK4RwQ4HT7sTKnfZIs5CkDT9hu5Km-w9kcEuG3xy1f-kdQw5ez9SUe-bjp46b_rV2eiUX_TNSJqufBPD2ZWWrd2BIq8ddoQA8BtO5Ar8E9uhdGYR1OfiYVywTPnoWxL1PBW0N00dBVsZ1oJQ6gKhBzcbyqBTWjPFCYPi53_CkZditPuV2EYQAGJIQsbrNkGMwhkks0iAdr-Dsr8grVCPWqjAyMh7z6JHF9fbWOYDVrbgTQXEZYMtGtNfBejXfNTq5Z19lnP27Ew6mVYP8iQYSxI7OSmRfSZP2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q--91V95xSXwsrAx7JEzhyWTTaOvVA10OPBzZndoJY9IiSNMOKimFsqRCkYiXUqO5SBjgkzpq3jsEzlBKjz8CNNy0PSCZ-TcNC7_yfEuPfcE551PkrbkmSYb6FGWGRs5Wx3YmsEus4pB8I7es17svyggC-YjZaNe2mBGzc8e1bNbdVoL_q-Uk8rlwpGnBvPbp1l26KMFq9Ier9DwBYJCPJxjzD_sNkdQoN0vxKs13hozjyaH-A9TdpIWbLF-8TZ788xu-FjBs8XhlOw7GkaqBy9YfrnhBtZBO6s99witjFJG4W2riU9P_3qSj1e1MLutfQK5Hwfk-RO8U1KXpi-IbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقات پدل قهرمانی کشور
عکس:
زینب حمزه‌لویی
@farsimages</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/449413" target="_blank">📅 16:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449411">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7jeocFsJCK5vM8uHh9GsRd0t4Pgr4KVG-vdFpLsB0tIiNMydIRYEQBNfQpvDe7qLO0UZS1sNL5kJGi4vEnPyNggHjx564IE4CIrq1TW5d1YC62_d7uiqnokwz256bcQ4K-IFpCGC6ctmCV95r3tHgtSkP4Y904ad8YNLQ1ml_NGtKkCRq3fVMafyhWc7fNeUPltQca6FO8eCKFH9jgDrrkOEESXzFnXwqnKPNm_Whrlls30UxHJphzASQmV3iRXU7g_XyA3eLHLQoCd5TL4Wbut10kEZodNODRrtnR1En7xtXGW6Iug9VX2m7G25aju9dkf0-yiZs2nX-wvesbmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و شرط دریافت ارز اربعین اعلام شد
🔹
به‌گفتهٔ دبیر ستاد اربعین، توزیع ارز اربعین از امروز آغاز شده است و فقط زائرانی که در سامانهٔ سماح ثبت‌نام کنند می‌توانند تا ۲۰۰ هزار دینار عراق دریافت کنند؛ نرخ دولتی هر ۱۰۰۰ دینار برای زائران ۱۲۰ هزار تومان تعیین شده…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/449411" target="_blank">📅 16:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449404">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lwhVUgxyB8lDXLwy5yCkPSfTIboG7QvLrjYRJrpNf0BZG3sHv7OghaYVkXKHoJC0JI9CKqYiKC0YpX2sUdzTAYajLezus2LJruLZ2K5deAJgsU9MPUp_dXy6O4R45FChyi4QLGpQ1m4KwZ4XO36U8yi4eh_sKl81srqXrjwtVbj_LCoUBz7boEeFC1yPO5EjBscfvMeZIBQeY6EHorqQfmAZr-y9zNGULCIzxMXZgZB_TYFFhZPEkNKoKXBrQwl-sJkokxEO0_NtuFGv3UyJGEphVcixPdynQAUrZUW8T_PhNO4yQQ1oYjGlu74_8NJk20FK0raUaW0FqOj-vnu0og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m_hFjQAERNm-1_Tv8Uo-dMRxUVWeLp1k8ZKbSqXbl10O8KRDkARozVFtnRqB7c3akwO5Dg4-ow4ij0JQU-xGlc0JlRu7dwXhq-MwFO_znTYwVgEV-w5stCNanIMFgY1_vPn-jE3yDcZNaWv805Q9m9dIMYQHrL60ZU4qukvBU3ApwvC73oNuzq8OYUpyGHN0DFwJydTNcqGN3p4ZDUuCU_J4khkvhP7N_UF2MbcSk0Ke9C9isD2XPC7rkEu5JZKCvjaMpqSiWCvitIW0dXbsF66nThJ4-Y3FPHhXx6IbTdpq04efZ2FMzf2nCYVZ8Q_qhMForfpVfPxFLpIgz54CNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KiSlCd3o4zSmFS0xY2Qzs6DRc4s-zzYuXr2UqlVs1tMPrdpk6vMz9suiFq76LROKz40_PY_XiPFjNNVN1Qv-Io9RRLtPg08l9gRfvYgYs4_U2EceQqrSKwowFrv0Nu1PzV1_7_ny5ic87OtFbRb0SeQQFPFoNgy5ivopBm1sHGLT4hcoV9G4PSo9H4wm4HIejb3KKQ5DurSa64vMFEa-eCg-JE-SqTJ4N3CWpHpY3TTgClwdRmaat7XrfReZFNEqC-BoP1QqnwUaPK2juwPEUiYnjLKaiGES1oL7e39JJ6DcSYO8elmoepVowF6KKpLJegabOgJ_fLbzUij4kqe4uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SX6McHtvfqbvCRulJ3P6ZFDY5hav9PDMB2-YaqwOeuGperNJ40IMs51u53aJ3GAc1VOAktWof4ko7HVQOV3-JpBe67XCNCsI-1HwrhlT_C2y9_TnQZY3OkWSUZ4jL3uksYTG1FFS7gxzf2hVCyH6Pm7CLBTOXGlK9ysEj5u8DtQAeMFQ1y2QU_GQh79WgmvqHT_fd3LARio9pUJtQVj4pXHyPufVPPAuBD1OoAsj69TEFRFk-nSNxxO46NbRQxM3W_xaQ2bVpv0vdewunNx5Oal0st4tkB-rB-vM9yXAFqDjTtLQm9qBFLb8FLw6Tkhnla7AIzDw_tWzYxiNl0bTdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqjyyrbd08IMG4J_M1eubYm87oOIGi8D1mBnsZChtzNOLOkNXYNTxJNVCd0YSvqAqLgRBGfSIgNynNZ6GYfw7sImtqYuw4MBW4bpKHUBTsnm13zgu5s3AQt__84T_tZgz_aoCQboL8sTo247CAA86C8WLP289vbRKiaQ8Gr-MK8SjWbd15Dqh6PNN1fkGy0sbfHGy5NwotWsEz8n6VYgABWK0iBjRLt4DJeCJ95YG8d_b1t2tn1Bp1w1B-Hek3u01tM9jYuQIaKpXjcEZZuGLABMV_l3Gv32IHrSTs2w8DAtsK948tmuTXuczZYeTkpYH_yBM44Aw5iJruJW1ux9BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sD7sxfmP2sc_Jud3XrzD3dBMfgPiDD7ASEOXK-21OSRPD80xXcP6UoZ6RjmTXCXLBvRqr4o8BXxDks8kTA471vTlbJ8yuN1rozFWW87QswSNBqNoE18E6C_GdC13Vx_3dzN_ArGJpEVnp2VCvxTKAniDFFt2eKsYUUvfkhUsXqEitKPj2pmOoOw1ogRn5cLi96WQ6nQg5_MLHoIXNP_rKtlcwzVS2RbPz2zx3pR9tSzYWzFVVne4CZ0dhgqZE6Rb9gQuvz_Sait0CXDnhe24qXZsd9pZybErYxdT8gXn9kAnU2wtVTg4RMli7KpCXyAIA0qpobXwBgqrwQXEtvuhKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V8mBkhg2riSa8khzBRW_vIP9_VguLx61LbTuUDVcEf3d6ITm6jzdGCe7dIdP3n9SesKP2gDblSDK7OdnC4vLTMEOGIXzpk8hCVRqd_kntKXDd5UDw2EurdzH2gBTWza8A3wE0ytRRz090bgJuliq4XKER7LAAqUR7hnERUQF1thsyeg80mhE9oSZO3bI376Zvd2jWe35SlF0FttA5wibia4PN9MVctWMmaVYhKO2y9hz3wiOa1p3BxFJi_ItoKfr8q4R3zigKuD2_5objfSrUKsg30IrFUHXCxP-5DDNuhAM1vH-Kh3BTlA7TeekKPeFhzF0xpbm7scJZSQQYlp8GA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم بزرگداشت آقای شهید ایران در بجنورد
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/449404" target="_blank">📅 16:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449403">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsNHAaXoTFkhw58dydk3sJshotO00pFUh11E9Vz8mgNKFFtAAv6qJ6p9_IGDOZ14C0rs5tFHy8MdvIlhuY2Z7JacNP5axmp9UZ15_c--gFApYx8M4EYn9BOgj73k6KWMGJ4-aXUDntrJC5GQHfG5kxwyddtqt6Iv8IXfh05jKDInj2DUjcgwuSCcqkWwG3FhcHncCRohXWypYF5bHVcY2YCcr2Z3PVAFCI-I-r0Kq9rzLHpaAJLOkw3f44IfqrIEwKkfB3mQkkSkpetJVmgp1-IPEtRwFJXqfoRNT8DnbRI3CKt7tFcdS4DUAdkZ9VqHoCUvdqlmLgnQTdGcW5MFhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد مدیریت آبراه خلیج فارس: تردد از تنگهٔ هرمز درحال‌حاضر امکان‌پذیر نیست
🔹
به‌دلیل تحرکات غیرقانونی اخیر نیروهای نظامی ایالات متحده در منطقه، تردد از تنگهٔ هرمز درحال‌حاضر امکان‌پذیر نیست. به‌محض برقراری ثبات و آرامش، کلیهٔ درخواست‌ها براساس زمان‌بندی بررسی و مجوزهای لازم صادر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/449403" target="_blank">📅 16:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449402">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpPuqPerJTuHr1OAKouVlTa8jmVqfx-r6eYj7d04RooSzeSIt2F6v16AJHM6vfbQcCJN8qR89cpoqvRVvZA9ESFH_DsqC1fekEDAv_tL6wbuEADPlpfGjKCkMK1LEZmHGYGYcqhkufkHhzrIBmrKro_p3HvzW9JnGACZb5_LoG2R2orHlOVFGCkzjLOnNXf9RF3AmDyWhozTs3SHpVsu43x1ZcQUdQwwx5hRbo43amNI8skD8oJmzjm9a2-7HpYqCo4eLBJlVlpmtIYQTASoWRaVf2E-6ttrjz8Gy0tSagvfzm2Gj-2YMYdD70OyzLKPK-BFNMgSxso_7L2tFS34Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حراج شمش طلا سه‌شنبه برگزار می‌شود
🔹
مرکز مبادلۀ ایران اعلام کرد صدوپنجاهمین حراج شمش طلا سه‌شنبه ۲۶ خرداد از ساعت ۱۴ تا ۱۷ برگزار خواهد شد.
🔹
قیمت پایه شمش‌ها در روز حراج اعلام می‌شود و معاملات به‌صورت حضوری و نقدی انجام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449402" target="_blank">📅 16:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449400">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGF6wlogNhtgzKfvIuuO2zezZJ5El5BPL8fMkGjgxn50iUoMlhFStU4gH3lNdAzwDp5s6JmB4HwtsQY_Eo-RPov28baFuS0wPt1ObhPumy3VcriWSFyewBgphj8F8TyIdTvmKWzsszjeBsKnjhvmlEVCByA0W_feUmcyx504gfcda0ianZtBkrIi5TK8V2xaLBnaT4ylQUIigCehueckWCcERgvHU-9G3LhbR7ihG87HyDVfVLJdj-23Y-SpggZT-SkEeGpx_vL0sLdewG3fe5E5oK-Y7lFEEuSTEx0ib6cKvJMAx2OoW7RA9G2dtmmJ7_KmC0nhpvfbLiSeyncSuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپاه: مرکز فرماندهی و کنترل و آشیانه‌های پهپادهای MQ9 در پایگاه آمریکایی پرنس‌حسن اردن منهدم شد
🔹
اطلاعیۀ سپاه: رژیم جنایتکار آمریکا با تحمیل ارادۀ خود به حکومت پادشاهی عمان، شب گذشته تلاش کرد بار دیگر آزموده را بی‌آزماید و با تحریک چند شناور، مسیر غیرقانونی…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/449400" target="_blank">📅 15:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449399">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3IBlo0Mcx6GGPrQ-11egryqKTWEUKA_6gZhoPkIKCDosIRJ9mEUa1MyyM1RhdTQ9OYt8_LVEE9jpFP23ZamN0WyKVGgec0xBubWqCDFqvblTUdovEvwIq0Z03r06gN0wtvoA0s0v7tDajd0Ab5rTiWWljRzGQMpzZlntSFZw_exscTcmMuz_oOHEpx8VeOj1R_G006tcOUZthEKZwfqoeoGuvfV4DTjsPA8YewIqbWp_KJTi7tM2Z3n5wDlIYU-EO7bv2oRuh7WMCecUTWwJaKV-4QGy0qrC4IutVWwfa_ioqKZ2Cji2lL8jxBRu-c2q-sxV8EKiO3h6iSLMB01tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیلی جانشین پیروانی شد
🔹
با تصمیم مدیرعامل پرسپولیس، محسن خلیلی، به‌عنوان سرپرست این تیم انتخاب و جایگزین افشین پیروانی شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449399" target="_blank">📅 15:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449398">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuU7CH3in-FUJIZXohFUHe7LtH77axyyiGpkCgjZyKB_2bWnTSHh5SqkjXHix7V90RCpzVL84dpBGMCyEBGAEioH56M9HczDdwj1Q1ATmohQBCDn4sHxNZk4okJGFoN6R1vO_ETD49RljKEzRYaWO4CHwNtcL3hz2TZQw1B467kPC-DxX1Clugz_kSiWzr9CCQK77sjlB7UZNc-eV2qwMO7EqL5JzqQDlABsifUnURxkcXE678Fjm9gff3dvgv5yFjtsIh9XpeTWHj_kXFZ56HiUTc1LdEEHPHsOAgFNVQ3Z9nCldRIBMZYhQHHOiNn0BU_dCmMEkRO08ioN7Yd2QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
بیش از ۶۰۰۰ عملیات فنی ایرانسل برای پایداری ارتباطات در تشییع رهبر شهید
🔸
ایرانسل، با تمرکز بر مأموریت اصلی خود در ارائه شبکه ارتباطی پایدار، در برگزاری مراسم تشییع پیکر پاک رهبر شهید انقلاب اسلامی، مشارکت و بر ایجاد، توسعه، بهینه‌سازی و پایش گسترده زیرساخت‌های ارتباطی در مسیرهای برگزاری مراسم تمرکز کرد.
🔸
ایرانسل در مجموع، بیش از ۶۰۰۰ عملیات توسعه‌ای و نگهداری اجرا کرد که شامل افزایش ظرفیت مکالمه و پوشش رادیویی، افزودن باندهای فرکانسی، توسعه فناوری‌های UMST و LTE و 5G، بهینه‌سازی شبکه، رفع تداخلات فرکانسی، ارتقای زیرساخت انتقال و تقویت شبکه رومینگ در ایران و عراق بود.
🔸
افزایش لایه‌های جدید LTE، توسعه سایت‌های موجود در مراسم تشییع و راه‌اندازی تعدادی سایت سیار و سایت ثابت جدید، از دیگر اقدامات زیرساختی ایرانسل به شمار می‌رود.
🔸
با وجود استقبال بی‌نظیر عزاداران، شاخص‌های کیفی شبکه، با پایش ۲۴ ساعته، در سطح بسیار بالا باقی ماند و متوسط موفقیت تماس و شاخص دسترسی‌پذیری حدود ۹۹ درصد و متوسط میزان قطع تماس حدود یک درصد ثبت شد و کیفیت و سرعت دیتا، حتی در اوج جمعیت، حفظ شد.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/449398" target="_blank">📅 15:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449397">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarmaye Bank | بانک سرمایه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae1-b5uNC4tqDnfotmwg4u5P60gcUponZv890B9yaG2S2DuorInL8nTB-UgkvfqvcnKQ_vZcr0rZS3u09-tpUYla-UfpOr8O76x8gi1vu7t-IMd-_BUwhotHIHV7CeEXa80YD2VtP5fSGVFoo-XGnf-ybzXrutDAUfMaJCrCqya01VaCyQZcHbkKLQqkuTnWjjzUBOF27g64fZeGmWSPJXH8E6WH55v6pJq5OWAj4lEk4TmkyYwZSha7Hubn_QuF3gAXXfGeD-VTRCxvji1UzH4W4U6iJBNuK4ihA3UNkCgI2ySe5yU8HgDZ-lksh8zP7cUup598H9v7JlXKaxUDlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚗
کمک هزینه تسهیلاتی ویژه در بانک سرمایه جهت ثبت نام در طرح خرید خودروهای وارداتی جدید
(اتونوین)
💰
جهت بهره مندی از تسهیلات به اپلیکیشن سرمایه به لینک:
https://my.sbank.ir
و یا به شعب بانک مراجعه نمایید.
📅
زمان تعریف حساب وکالتی: تا پایان روز جمعه ۲۶ تیر ماه
🔗
لینک وکالتی کردن حساب
🔵
جزئیات بیشتر
📞
صدای سرمایه به شماره ۴۳۷۳-۰۲۱ آماده پاسخگویی به سوالات شما هموطنان گرامی می‌باشد.
‌
#بانک_خوب_سرمایه_است
🔽
بانک سرمایه را در شبکه های اجتماعی دنبال کنید:
📲
اینستاگرام
📱
تلگرام
👨‍💻
وبسایت
📲
بله
📲
ایتا
📲
روبیکا
💖
آپارات
📲
سروش</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/449397" target="_blank">📅 15:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449396">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/449396" target="_blank">📅 15:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449395">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7UDH8j855aqRChRH8LVA4BHgaRKSMtndizkPS5jn2tcbwgUjoK4K3dJQdTBHq1DUoI3Tw4bpq4FztIDsLyv3xjBQD6psTV-ZjJU0bLEq5j-yAgCYgdZSiQsmnbbGja2fPDusDcLCfrn4b8NMhVjI0RhLf6chV_XOVxjnsO4bj1PL23jGm5e9HxMbaby0Pfa8-L0jfhARZtzh7JIdjsBd3j3-kdNAS9D85daO59aSpf0jrt8tOdoF10CX5BlMJQ3SsabJA-5p_WJOyqVxqWjUaJXEXRHqo8I7Sj5fKZ58gYrPd_gZ2l5-gwjQVCnttLVQHWXliwlSJX-MiLTkgIBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر رضایی: اهمیت تنگهٔ هرمز از ده‌ها بمب اتم بیشتر است
🔹
اگر دشمنان بتوانند فرهنگ رهبرکشی را در منطقه نهادینه کنند، امنیت هیچ کشوری تضمین نخواهد بود و به همین دلیل باید در برابر این اقدام ایستاد.
🔹
ترامپ و نتانیاهو از مهم‌ترین خطوط قرمز جمهوری اسلامی عبور کرده‌اند و باید پاسخ متناسب با این اقدام را دریافت کنند.
🔹
پس‌از این همه دشمنی و جنایت، سخن گفتن از دوستی با آمریکا معنایی ندارد و ملت ایران باید با قدرت از حقوق و عزت خود دفاع کند.
🔹
تنگهٔ هرمز همانند یک عامل بازدارندهٔ راهبردی عمل می‌کند؛ این گذرگاه راهبردی از ده‌ها بمب اتم نیز اهمیت بیشتری دارد و ایران از آن حفاظت خواهد کرد.
عکس: خدابخش مالمیر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/449395" target="_blank">📅 15:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449394">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌
🔴
عمان از حمله پهپادی به چندین هدف در استان مسندم خبر داد
🔹
خبرگزاری رسمی عمان به نقل از یک منبع امنیتی اعلام کرد: چندین نقطه در استان مسندم هدف حملات پهپادی قرار گرفته است.
🔸
استان مسندم، یک منطقه کوهستانی عمان است که بر تنگه هرمز اشراف دارد و با امارات…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449394" target="_blank">📅 15:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449393">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKvaFiRRZM1ZF4eJcYPXHGtk2oUEokq1sCReoR7yk2x6Uep2imTVZCn88SbBZt8JCxcQ-kFYTBg9Rp1DFs0E5QHs_HCdofDcEJFH0OA_2cVyQFpQONGJaABZrClhPhdhcvV8guL5KYbl-7ayMXVu1GDgBc6coaE4l9t8uCJNDJpeqAaJ6ikwT4s7Y12fVDIZHl4gABQUCR2kOFSSVrGV0i5WmNg8_07zMOmfhJBt7SyfByYsMlurJBEGkn9ybhl7ecEJs7O_rS5sFrOfOak3edNhLlsTFr7G2xgd0A6cj_thefogxYpVqSAYY4tFEDjvWSocpFfGEuywK2yJP69Nlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تروریست‌ها با هوش مصنوعی بمب ساختند!
🔹
پژوهشی از دانشگاه کمبریج نشان می‌دهد اعضای گروه تروریستی بوکوحرام از چت‌بات‌های هوش مصنوعی برای برنامه‌ریزی عملیات، عیب‌یابی سلاح‌ها و حتی دریافت دستورالعمل‌های ساخت بمب استفاده کرده‌اند.
🔹
براساس این پژوهش، مدل‌هایی مانند ChatGPT، Gemini، Claude، Grok، Meta AI و DeepSeek برای دریافت اطلاعات فنی و طراحی حملات مورد استفاده قرار گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/449393" target="_blank">📅 15:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449392">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltipGyBkmbmleQsm2Dg86aWEiMe7TSq4UjNjfltX1dB5lz9UNiy8MmNiQd43Qk2dEVPGQy-Lkg_DaTMMJnt7xUs0-f-3FoIoaROYY8VM7TQapXzmCe6Jhdk9H7nlAJWXcqjrp5XyB5cjayUWGK0r9WYwvEGbzgqA6qfn1s2jxi-C_O05sRUJWOnDk2s1jvfwCRXd8Ijw9IdPvZOPk8H2TkAHbpBC_-2DjLqxqZ3qL6sW5WY1MVZ4u35iKP6wcje3zEQpYqZbSto6W1J9FgdO8L8rBGb_2LdfhQRXSj4UZzT0MyhdLnTtk0xFex7f_-ICVOUe73KKJwHi1w_poORnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تنگۀ هرمز همچنان بسته است
🔹
شناورها باید با نیروی دریایی سپاه هماهنگ باشند تا از تنگۀ هرمز عبور کنند.
🔹
از دیشب تاکنون صدای ۲۵ انفجار ناشی از حملات دشمن متخاصم در استان هرمزگان شنیده شده است.  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/449392" target="_blank">📅 15:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449391">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522a1a11b3.mp4?token=VfCTx-5IQ_kebr0teZCWRIJiim0w7kBVBEiolaWcVP4C7O6VkJuspNtY4BuZ6ICMGriLQHx3PpConZSdqm3CCuLkDbrNmjZG4q20E7DHpB7DbNX2HjVw_IsSDFoMX2UuspJOn-7Nyu0PWvr0qw_jXqvs_tBPOIRrhwLfYJ0jTKEfFsGkTfk6v9ZbZVobyDma1kf7qVH9CjpjHC97GwMZMDTOas3d_BSCXnp5CvXf3zQzh10Cc36t_ODrN0K81EuuW48tkaxHlXQ88nbwe62chDd6bjhWbggUcvAIsoN4bVkzRCjpcNI2Mc-ghkMmRt6rBWGNOgtMep7812Hu0pfR5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522a1a11b3.mp4?token=VfCTx-5IQ_kebr0teZCWRIJiim0w7kBVBEiolaWcVP4C7O6VkJuspNtY4BuZ6ICMGriLQHx3PpConZSdqm3CCuLkDbrNmjZG4q20E7DHpB7DbNX2HjVw_IsSDFoMX2UuspJOn-7Nyu0PWvr0qw_jXqvs_tBPOIRrhwLfYJ0jTKEfFsGkTfk6v9ZbZVobyDma1kf7qVH9CjpjHC97GwMZMDTOas3d_BSCXnp5CvXf3zQzh10Cc36t_ODrN0K81EuuW48tkaxHlXQ88nbwe62chDd6bjhWbggUcvAIsoN4bVkzRCjpcNI2Mc-ghkMmRt6rBWGNOgtMep7812Hu0pfR5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
صف طولانی زائران حرم رضوی برای حضور بر مزار مطهر «آقای شهید ایران» در رواق دارالذکر  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/449391" target="_blank">📅 15:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449390">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8qjlWTJUDfH9X0XYsYZ2sv33w6YpaX0LNGzuGNEn5FEgOs3iBRSDSC7nCHP3Jf0Y04J77Uusd7eMdl9UD6l2tGtoPfAhbbPmAkNwZFnMEVsWTm2dKokEYfGuCNhFbVMstpOr9Nb9ooeUVqBBdktdBw272IyQe_RGOyjM0GWRHat-_GRi5x68GzIbkf-tR8vQ0rsN046098-wC2x_E0ZDA84TDFU6T3G2uYOpQFYsdahQKQPRT8OnhcnrqHRqqsCm8-WM2LO1hPghZqJsFpJ7svkdHWdT-pWH6qFrI6qaFoEi4hKblWH0_krAI62-glgX2Xo6PYhrlyQNiP5sFxkaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپاه: دومین شناور متخلف در تنگه هرمز مورد اصابت قرارگرفت/ مرکز فرماندهی نگهداری جنگنده‌ها در هم کوبیده شد
🔹
در پاسخ به ادامۀ تجاوزات ارتش کودک‌کش آمریکا به پایگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی ایران، علاوه بر اصابت و متوقف‌سازی دومین شناور متخلف در…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/449390" target="_blank">📅 15:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449389">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2cdb876f3.mp4?token=gVdKMG21xh_3h6bSy-kx0xaKI-RjKLlpRCVTLVZem0ZYGHL9HRqTmSUcQ6CHXkt5uVtfzIumud4ogBbRySCrhNi-TWQZfZRKUBxoWXkZUpZp3Lb2ZUXiEo45C5ok78qBbnpvLCecQpnIMzoj4goZTjWk2HojHvSdUp2ZMqRgglydCJNaFg56GbEwQAubJ0AiGPfHgRjhDCNiSWdo7SbAQDtzhEB6d1yeDlkJv9pHaXjUlgBJnQuw2QvrW_FjNEXSn-QgpMPAWRQcA0LwlJcoVxvBEa6tdEoYlD9ByAsAuSwryepxhEGorEzKV3ka5kmt9JB0aub3FsaI0Ws1h5XbxjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2cdb876f3.mp4?token=gVdKMG21xh_3h6bSy-kx0xaKI-RjKLlpRCVTLVZem0ZYGHL9HRqTmSUcQ6CHXkt5uVtfzIumud4ogBbRySCrhNi-TWQZfZRKUBxoWXkZUpZp3Lb2ZUXiEo45C5ok78qBbnpvLCecQpnIMzoj4goZTjWk2HojHvSdUp2ZMqRgglydCJNaFg56GbEwQAubJ0AiGPfHgRjhDCNiSWdo7SbAQDtzhEB6d1yeDlkJv9pHaXjUlgBJnQuw2QvrW_FjNEXSn-QgpMPAWRQcA0LwlJcoVxvBEa6tdEoYlD9ByAsAuSwryepxhEGorEzKV3ka5kmt9JB0aub3FsaI0Ws1h5XbxjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نقش رهبر شهید در جایگاه ایران و ایرانی در جهان از نگاه مردم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/449389" target="_blank">📅 15:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449388">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIANFFpIDeEklaDDwnagYR7KD9TKTtv6Am9BSJZptkyTYMCy_1TGC4f0kya7yDHZ90B6jKKutuJkA3yXvt1xUN_sXSXK95IRHXouXkWWbc4BCyTdV3nV603tOCdHOlZg8wpbFpQsLNyyxHxAjWe0se5yyd2HEvFgBS3mYXWdE_zVzAyzO9nhUxKsSwEpHAk5nkPKTuvctBrPxCmupl2GsbC0AcabY2_qgtXQ-vsvZmSdqP3pDt85E0TXGuUZDZFZSYphMA_1zmipM6ZStsfWPmdGCOtXw5Z0XEr_4YDtIuNmdmkDweNNRhbVl9-jDFPMr9Q5YtibBmttGUVb9ymesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارت بانکی جای پول نقد را گرفت
🔹
براساس گزارش جدید شاپرک، در خرداد امسال حدود ۹۸.۸۲ درصد از تعداد تراکنش‌های شبکهٔ پرداخت و ۹۰.۳۳ درصد از ارزش آن‌ها به خرید کالا و خدمات اختصاص داشته که نشان‌دهندهٔ تبدیل‌شدن کارت‌های بانکی به ابزار اصلی خریدهای روزمره است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/449388" target="_blank">📅 15:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449387">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5c1155f2.mp4?token=XqXJxMEjKuaOHvRdvrJUy6kDR8-OC7nnfUBZTnuRN1n1auFDdVHCxHTA_Q2GoGj8M7tI7PV47Z38H7yc6hP_9DtJF0kol5Xylr88Haidm13SBkmXgVvkO5wcEixGatn2p3Hf9laHLzTiJ03uPlfE-BelqWyZ2yV-6jiptUTF7WVpHLOdRYZYHOZkg7Iu9p8Dajih1VfYFMaurBWa_zLh3Aetaliruwgapwln_KptJeU77iUCFya6IEKeE3kmi7FqkkxtrIQT-4F257mwF2viur8Uv5Yv5AP2a7ai15b7C4L9sW95tiYZGvceT4Vh-_D-WxHsjdni9Ked8HE07L1fAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5c1155f2.mp4?token=XqXJxMEjKuaOHvRdvrJUy6kDR8-OC7nnfUBZTnuRN1n1auFDdVHCxHTA_Q2GoGj8M7tI7PV47Z38H7yc6hP_9DtJF0kol5Xylr88Haidm13SBkmXgVvkO5wcEixGatn2p3Hf9laHLzTiJ03uPlfE-BelqWyZ2yV-6jiptUTF7WVpHLOdRYZYHOZkg7Iu9p8Dajih1VfYFMaurBWa_zLh3Aetaliruwgapwln_KptJeU77iUCFya6IEKeE3kmi7FqkkxtrIQT-4F257mwF2viur8Uv5Yv5AP2a7ai15b7C4L9sW95tiYZGvceT4Vh-_D-WxHsjdni9Ked8HE07L1fAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنگۀ هرمز همچنان بسته است
🔹
شناورها باید با نیروی دریایی سپاه هماهنگ باشند تا از تنگۀ هرمز عبور کنند.
🔹
از دیشب تاکنون صدای ۲۵ انفجار ناشی از حملات دشمن متخاصم در استان هرمزگان شنیده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/449387" target="_blank">📅 14:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449386">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8604121fb0.mp4?token=BqGqvm85UfeJYp0HvBiCC7bKNvEw2O91xnsFtZrFuX6xcfQxHAsn5L2D9rbpxSsw2_5CAQsvpqquXlF7Xt2YhwNwHV9J7_fxXV4s-C1npTDCIMOwuAFXRIVm7DQLw2dwtJhuL4xKPKVzklpabP5FnRseeOtlNAPTfU4nKpigdUVRzgFL3XdZ-ft5RtONFU7tmKtE8c1X-_4UO4CuG1SBAqXOfiVZzqc8s1OYHybTs3zk0LYNke4s5unqQirCIAEXA6k5W429pv9GddRnd9Pz296xyWJivXa94VPpWP_E4NzVi3YqJhV-LxqALf0vvsFr6Fc9G5eY9pmTJccBJwiPnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8604121fb0.mp4?token=BqGqvm85UfeJYp0HvBiCC7bKNvEw2O91xnsFtZrFuX6xcfQxHAsn5L2D9rbpxSsw2_5CAQsvpqquXlF7Xt2YhwNwHV9J7_fxXV4s-C1npTDCIMOwuAFXRIVm7DQLw2dwtJhuL4xKPKVzklpabP5FnRseeOtlNAPTfU4nKpigdUVRzgFL3XdZ-ft5RtONFU7tmKtE8c1X-_4UO4CuG1SBAqXOfiVZzqc8s1OYHybTs3zk0LYNke4s5unqQirCIAEXA6k5W429pv9GddRnd9Pz296xyWJivXa94VPpWP_E4NzVi3YqJhV-LxqALf0vvsFr6Fc9G5eY9pmTJccBJwiPnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هرکجا که گره فراوان شد؛ ذکر یا مرتضی علی گفتیم
🔸
لحظاتی از شعرخوانی محمد رسولی‌ در کنار پیکر مطهر رهبر شهید انقلاب در پرواز تهران به نجف اشرف.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/449386" target="_blank">📅 14:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449385">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCLBksB7049-fsL5TYGsvADtjfAdrIS5Y59LUy_sTrp1TReR2Q5upz4VB5ddy50armWmx3WgUle358fm2hCr0m6-h119l2yZJ4LuC7c7fOx88RniXekwSCiUr59GouxYSvzq6JOX265eSg5pphYx0fasTvMjuNnzD0XskeohV-JXiWa0RD1Sfc6eJ0OWzO1P4dMBfPBOm70NZJx3KUXk2O6Av47RKLeH1f3klZ8Vu3bflf626821AJxr0aMnqrv-a2mhzlC1wieVgjLqxQx1YXR7sFBlCSSv5XK0q39_6xUCmoN5Zt0LzjxByilAE3I3YlKlyeAcFYsjoYuwS07Eog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ پیام عملیات امروز ایران علیه اهداف آمریکایی
🔸
سیمیاری، کارشناس مسائل سیاسی: نخستین پیام عملیات امروز ایران، اشراف کامل نیروهای ایرانی بر تحرکات دریایی و نظامی آمریکا در خلیج فارس و رصد دقیق تمامی تحرکات دشمن است.
🔸
دومین پیام را ناکارآمدی اقدامات و استقرارهای آمریکا در برخی پایگاه‌های منطقه‌ای از جمله رأس‌الخیمه و کویت عنوان کرد.
🔸
سومین پیام این است که هرچه آمریکا سطح تنش را افزایش دهد، جمهوری اسلامی ایران نیز با دامنه‌ای گسترده‌تر و پاسخ‌هایی متنوع‌تر به آن واکنش نشان خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/449385" target="_blank">📅 14:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449384">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ibkv8bG2ZVabn7PnTqveFpg_XXTL49RLMk0YLe8mDeEv8XVZcdcNjGEjMO3SF9y6LbLlVWoePk7IRwDSfB3zlUxhOBG6TIlRVcM7mEyvcTYmmCUrPwLZy4UdUprBh50oImBVI7WqyajJMo5WrOVn45S_P1ovYIzbYv1P9GEfUbdDGNKbnAmC2v9NhvAffLYsI-1Hqd-i3Kf3dPb1NQrTAgGRdq3Deq9uFurL5tOhaPyqo9t0DiRkYHqk0uwwbjkKk0IRTJzbKoKKAdsUAN1aU3vheQINw3ZjME9qQY1QIupUxJ8bDtxWzvlQ5_Kvz6_wmWvwVb_BluDCctV5s_meYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توصیۀ خطرناک انگلیس به دریانوردان در تنگۀ هرمز
🔹
سازمان تجارت دریایی انگلیس به کشتی‌ها توصیه کرده با وجود اعلام بسته‌بودن تنگۀ هرمز از سوی نیروی دریایی سپاه، از مسیر جنوبی تنگه تردد کنند.
🔹
این توصیه درحالی مطرح شده که نیروی دریایی سپاه اعلام کرده «تا اطلاع ثانوی تنگۀ هرمز بسته است» و شب گذشته نیز دو کشتی که به اخطارها توجه نکردند هدف قرار گرفتند.
🔹
به‌گفتۀ منابع ردیابی دریایی، یکی از این کشتی‌ها در معرض غرق‌شدن قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/449384" target="_blank">📅 14:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449383">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OadQkPRgh1qHA0jNTS2b69AtD2xvo8evMKmX7VEIek-CydQAvQMO2Ns6ohya1J5XY04vg9c2ynU2r8__Chv_7PHf6kvW7uJZqCSQyU0WZgZUFR2NSiMP7tjrU9ho-_8K8JrCg8ntObJkYTmW3Mdrm_xIVKdbojJB6tkA62YZJcg3hU1KsOKDnm1AbKl09k9n9mcvSWCuHvW1uKDVGKOgI-PDsyJx0tpJUqQaTxFV_KlTFRuqik4vszzRbGcUi2h68kAZNTykAilmLjyXqJkwHuKKq5TV-nPUUaacMAoUxJdZ1UBkzftlMSGscWqLTtaIM4HxaiDR1oM_dJgszFJ0Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشت‌پردهٔ تأخیر در اتصال کارت سوخت به کارت بانکی
🔹
کسب اطلاع خبرنگار فارس نشان می‌دهد مرحلهٔ آزمایشی اتصال کارت‌های سوخت به کارت‌های بانکی درحال انجام است و سوخت‌گیری با کارت بانکی به‌صورت محدود و ایزوله انجام می‌شود، اما زمان اجرای کامل طرح هنوز مشخص نیست.
🔹
افشین، معاون علمی رئیس‌جمهور، می‌گوید برخی مقاومت‌های مدیریتی ناشی از نگرانی دربارهٔ تبعات امنیتی احتمالی اجرای طرح است.
🔹
او می‌گوید که مدیران تصور می‌کنند اگر «تغییری در سیستم فعلی ایجاد کنند و حادثه‌ای رخ دهد»، مسئولیت آن متوجه آن‌ها خواهد بود.
🔸
اتصال کارت سوخت به‌کارت بانکی قرار بود اسفند ۱۴۰۴ آغاز شود، اما با شروع جنگ و احتمال حملات سایبری به‌تعویق افتاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/449383" target="_blank">📅 14:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449382">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnBi7eHolJtcsaHn15pShALMm-0tCmOK5RVPIpghhhcZdDv2n2AGUbqtnrW00wXvVWTlYGkegMRmbOyGI6KG0OAQVMtzIuiyQqJqw6Kj17MunyTrbtolCKSzUqbMWag2W-_4xJtvE09kEfwAiFKlPNVv5VrNm0tict-HRLL2waeBrtbFeL5oZR-TnYkXpXiPkN0vBYNtbS8i6ZB49qoKAQgacnquRQzNBquRXhRHLxX5D1-i26h7aLg-7E1HR8_RlRahIZXmuyyrv12scnEJLXnXkpjS5IQpUm8t6OphOeBS-hGAP79zmSoITE9haXgFXRSKVpNFhAhBgCroO5Xc7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنگونی یک موشک کروز توسط هوافضای سپاه
🔹
صبح امروز در جریان تجاوز ارتش تروریستی آمریکا یک موشک کروز توسط سامانهٔ نوین پدافند پیشرفتهٔ هوافضای سپاه در حومهٔ خرم‌آباد سرنگون شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/449382" target="_blank">📅 14:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449381">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDLhxOzw7IHy0wfUwa0gVB4cTxKhRxWx9gPQgbShzFu71I4AJSnYvGTK42aHq-RT96Y5NZnB6K9tHEHmSJ3URhduMNhZpP51Bh4PifzTd32lSJzpeyVYSubjpZZxVYbwY2I8HWE3I-8J4q70Zobl9uk-v83YKUwgbUWH42O5CYCFuBv1c5eA1O_s0jPrQZ5rCLP4-R_9JS3zsdqWZSmZFPacHPJxurou-OBr6Tu0SV2xO-ETD6sutRMcUzMyWJLMTUyJ2HlKdLOB1z8TD8i607d8XDloKyzwoESlGXPH9AspZUaevCB3mx05e64r-WJpJxHjoS2wNx2mqz227xrdkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویر حملات سحرگاه امروز نیروهای دریایی و هوافضای سپاه در پاسخ به تجاوز ارتش تروریستی آمریکا  @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/449381" target="_blank">📅 14:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449380">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f78a41745.mp4?token=FgLNg2ao4a_6GdPE_Q3NpWA0_29suqBu7THK7Q0tMrGiHFHRq1YL5NoXQm56t1tkqS_bsMDdmsKwaK-7uEANKHJHUhQLYQfwVAeaN4MpNwvLy66GQfZXN48XCqTx6HNpvVEHHjteua-pFurYT5PcpGk0I76gQSzBve0BAu6FE7K2eGyseZi_UpP_Pu4aVfGPBj8Ba0qyCo2Jkn6PDaJ0lHXWFsJwAaL9WEt4u73tlITAnNh_cz6Bnfhw1W2AhbdpfGkFGweXYE32Czy8AVfXLwSTBG8eChKeedO6I00cQeJ9UjcggTcdnDgDlQp1AC-5L4swJa5weGqMXEpaexQr-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f78a41745.mp4?token=FgLNg2ao4a_6GdPE_Q3NpWA0_29suqBu7THK7Q0tMrGiHFHRq1YL5NoXQm56t1tkqS_bsMDdmsKwaK-7uEANKHJHUhQLYQfwVAeaN4MpNwvLy66GQfZXN48XCqTx6HNpvVEHHjteua-pFurYT5PcpGk0I76gQSzBve0BAu6FE7K2eGyseZi_UpP_Pu4aVfGPBj8Ba0qyCo2Jkn6PDaJ0lHXWFsJwAaL9WEt4u73tlITAnNh_cz6Bnfhw1W2AhbdpfGkFGweXYE32Czy8AVfXLwSTBG8eChKeedO6I00cQeJ9UjcggTcdnDgDlQp1AC-5L4swJa5weGqMXEpaexQr-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ اوکراین به یک پالایشگاه روسیه
🔹
رسانه‌های اوکراینی اعلام کردند پالایشگاه نفت سیزران در روسیه هدف حمله پهپادی شبانه قرار گرفته و دچار آتش‌سوزی شده است.
🔹
این پالایشگاه در فاصله حدود ۸۰۰ کیلومتری مرز اوکراین قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/449380" target="_blank">📅 14:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449379">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dtj4fbuwrQjyjoChsWBJqgtDqtjMlUsVXhBRv7z3IAPK3KL-KDgJAPqupxsdvJBRQUj3jqMAGpTD8A6RYNzwbo4V6z_MympsH5BZAyxfI18wczl6qLiPRNie9CHuDiq6Ht3ZUrhSfedwRQerbzCkrXOX3YoW0UtYQkcTzb2kp_zCpUEkFvfl0EtgQlXKgjlf5PR5X9NZ_UCjBFGrRm8cXiimw1gfjPRTnwF9kaRxHOoVJft3O09RYBxIaKfb4BpMlzW62dd0WzvBqJoxMzxThO1-h5-3fBK4KJMwmAv035SsQsejaXFOFB6c_fm_-uZzplNA2RNSTcTvGvoAXAE-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل تأمین اجتماعی: پیشنهاد دادیم مبنای حقوق بازنشستگی تغییر کند
🔹
سالاری: در حال حاضر مبنای محاسبهٔ مستمری، ۲ سال پایانی خدمت است؛ درحالی‌که ممکن است یک بیمه‌شده ۳۵ سال حق بیمه پرداخت کرده باشد اما تنها ۲ سال پایانی خدمت او در تعیین مستمری اثرگذار باشد.
🔹
این روش باعث شده که ۲۷ درصد افراد در ۲ سال پایانی خدمت با افزایش قابل‌توجه حقوق مواجه شوند و مستمری آن‌ها بر همان اساس محاسبه شود.
🔹
پیشنهاد سازمان تأمین اجتماعی این است که برای بیمه‌شدگان جدید، مبنای محاسبهٔ حقوق بازنشستگی براساس یک دورهٔ بلندمدت‌تر تعیین شود؛ به‌شکلی که حقوق هر فرد در هر سال نسبت به حداقل دستمزد همان سال سنجیده و میانگین این نسبت‌ها در زمان بازنشستگی مبنای محاسبهٔ مستمری قرار بگیرد.
🔹
اگر مبنای محاسبهٔ مستمری براساس کل سنوات بیمه‌پردازی تعیین شود، هم بیمه‌شده و هم کارفرما انگیزهٔ بیشتری خواهند داشت تا حق بیمه براساس دستمزد واقعی پرداخت شود. برآورد سازمان این است که اجرای این اصلاح می‌تواند حدود ۳۰ درصد از فرار بیمه‌ای را از نظر مبلغ کاهش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/449379" target="_blank">📅 13:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449378">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5ZCeHVw7P_DoUajulHA8kWtE3b4Ww8-T0_Dja4BpbDQ4TFUfa7MmG-1rCyap4LSGLqozR12Wkdu1gNJtXtMbj89peJTwmnj6jreJ0i3bmilyqwqO5aYDLlLXLtiGKzPwa2NkJgG4fe4jYpahuepxUrMkgGujLX5joUxQtZ1CVwSRdrSVilYHhxeGzSeT-NMPQbNibCNiIermT3aKw7Me-ylJF5axKVWUdzqP2bToXT0URtbhQBRmu0X6Wb2DIHV48tZzGRZGgJQXYsaThnB5I6n8EKARoUlIC3psc9PpUUjNvf8-QYbL5hrg03nCH9QmTDvm7v3gnUgv5DpygLqPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
انگلیس با برتری ۲ بر ۱ برابر نروژ، به نیمه‌نهایی جام‌جهانی صعود کرد. @Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/449378" target="_blank">📅 13:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449377">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رایگان بودن مترو همچنان در هاله‌ای از ابهام
🔹
در حالی که قرار بود از امروز طرح رایگان بودن مترو و اتوبوس‌های بی‌آرتی به پایان برسد، مشاهدات میدانی از برخی ایستگاه‌های مترو نشان می‌دهد که همچنان هزینه‌ای از مسافران دریافت نمی‌شود.
🔹
درنتیجه به‌نظر می‌رسد وضعیت…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/449377" target="_blank">📅 12:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449376">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/im1eTW6ZymUtCA-Csg6kKNkqIGg0gz3SMmjJWZgiFx0QY0WBTavJM5UiRPBJ6eMuecjqObHPNrgb8Q5fhg254jlQI13r8a_Vo9RAJ5wPvNpHj0lyvhDVVknlyApl_Nj1FzepgBk1AUfp9U50_7BseTyfZE86T-xfA-Ksnf0AAyJTAo0FmwWH3cRGxq8_WQYbQFphFfffWHUSUGmb_dUUW6eBMw7ViBPTubu7opwFv9gJQKjktZKGuxQfHyemoywI6Vy4z2vRKfZpm-uENoWvBFu6Ceep2w6mICwaxshBpi1cFKX56dK-Sl24NF2PfwcX4AdnE7s_Ujy3BGJzgX8rIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با ریزش ۱۲۷ هزار واحدی به ۵ میلیون و ۵۶ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/449376" target="_blank">📅 12:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449375">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اولویت ثبت‌نام حج با چه کسانی است؟  براساس اعلام سازمان حج، از فردا دارندگان قبض‌های ودیعه‌گذاری به‌ترتیب اولویت‌های تعیین‌شده می‌توانند برای ثبت‌نام اقدام کنند.
🔹
کسانی که در کاروان‌های حج سال ۱۴۰۵ نام‌نویسی کردند اما موفق به تشرف نشده‌اند از ساعت ۱۰ صبح…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/449375" target="_blank">📅 12:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449374">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUK3HmgWdnPxFHku_V79Z14EMZAVzlFeAB5yExrFSDr0lkgaDmNzGECbB83WpVFansFZl2qWZ2awPbaesnpciD-N6SyMOcbV5CFH-ZW2XG5bc_oVv5ySGbMKbAfquba5Hgo-tGiJYqnEHiryjVkLYsyobh_bz7WUADSw3fCSg1fo7hAkggn-IE64Z8PZAghJeECmtnl2I0h5R63OMaHzLtudfuJcM4km78UiN8G0hB4AdavO4FCUxm6jG5ok8nS7HkNxfQzzC8FTEkP2-uhGLWjbu-EcHw8ZT3j6EHDUK68X30_ixrIlVlCR4GPBA0QE4njw5q_-rcAzj_QRDRTClg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا پهلوی برای مرگ سناتور ضدایرانی هم عزادار شد!
🔹
فرزند شاه مخلوع از مرگ سناتور آمریکایی که یکی از حامیان اصلی تجاوز نظامی به ایران بود ابراز تأسف کرد.
🔸
رضا پهلوی پیش‌تر هم پس‌از حملهٔ آمریکا به میناب و لامرد و شهادت صدها کودک و نوجوان ایرانی، مرگ چند سرباز آمریکایی در حملات ایران را تسلیت گفته بود!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/449374" target="_blank">📅 12:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449373">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a676d04f3.mp4?token=v-UBVlXklRB14sYbHwADza2GXr1lAJow8-ItqwgppdtRceSvvhML0PXaglKNTxM-YLQiD9373XLXuUdNCzVdPDWtOhnfnFlVIY8hHOsvw1zClBtjs5xqXd6uC5BoJScdZzVFPSIftzvYh9ctgzng6Frcw5Ry0wK0tOuz6WjYzO8CqBNZyaJCYOoBH3z6B0ZkvjS1qk2bmZt0hJ_M5Nw3_1XjnD3WBk2eniea_ND7lkyC6MqS32gN4XXwEw6az93e59X7yUotz4pawgR6r0kQFmcbeDhASUPbpnottuJ5h55LJpz5_9rksdOOOVp7Y72bB1awfbcO7AZ2OaHEeSQaMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a676d04f3.mp4?token=v-UBVlXklRB14sYbHwADza2GXr1lAJow8-ItqwgppdtRceSvvhML0PXaglKNTxM-YLQiD9373XLXuUdNCzVdPDWtOhnfnFlVIY8hHOsvw1zClBtjs5xqXd6uC5BoJScdZzVFPSIftzvYh9ctgzng6Frcw5Ry0wK0tOuz6WjYzO8CqBNZyaJCYOoBH3z6B0ZkvjS1qk2bmZt0hJ_M5Nw3_1XjnD3WBk2eniea_ND7lkyC6MqS32gN4XXwEw6az93e59X7yUotz4pawgR6r0kQFmcbeDhASUPbpnottuJ5h55LJpz5_9rksdOOOVp7Y72bB1awfbcO7AZ2OaHEeSQaMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصاحبهٔ لیندسی گراهام در روز آغاز حملهٔ تجاوزکارانهٔ آمریکا و رژیم صهیونیستی به ایران: «رژیم ایران» ۲ هفته دیگر به زانو درخواهد آمد و سقوط خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/449373" target="_blank">📅 11:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449372">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XubkKTv-VNG6gcEJMm3SVe_ZbRjgPuzoeqbM9CACmdTYsjekrrY9rykRKWmsAPtK0i9mgS2rvXovKTPc_m3Y1nX0Vns_hwkz5cJqEftTIKyi--uG-wdCS_t9gvq0wFrVFgCD_rfEQb5uME3-QQM2ZTc7XELQ6GXUgB8z6Sst-LFw187zzF94q74CBMtf1hzxEgsx_H2LSf6puVmQs__NQQaoeHJWzxckdKU1iT5mZx7DaXlkT2t4PsxQkHi3_0vJV9el4jR86RYakO71skanvEVuDQcxmK4Fn2RGd3rT0yDoWF50Ru2yH2amW05zPKIfZ3TJ-QmLN2a8W5y07sCf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش کنایه‌آمیز مرندی به مرگ گراهام: حیف شد؛ کاش قبل‌از رفتن به جهنم قیمت فردای نفت را می‌دید!
@Farsna</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/449372" target="_blank">📅 11:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449371">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4FRwHFJhf5uMRUWOQsLmybjF0EvrIltgqHvS8NOrESiq-TsoyFk_M5ofZFcJK17abHP2vI-pZVai6WdZ2zqY8eNE6YLOxCTBc-AgKzEbhSBQ2ZIuyScISUPV8JLgD19_fgovZbgQzYPx3vl5NsDhFm9BtmPz2b19kTmEtFOxM9j6HydCryg27R-g4VEexpxByHfMSEsdMbeSPsIt33o9VcUYTXBeh8_7ZZ83KqQufR830SOF93fFIBQAHUzYaLz6OIDwjKhHIauKf97ky9Vy6R2_-aNwW4h38b0DvBO4sY_1mBdAMIv1uO9aRd4xX1qdYKk-m45jLjHxOus8BZTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: فقدان لیندسی خیلی غم‌انگیز است
🔹
سناتور لیندسی گراهام، یکی از بزرگترین افراد و سناتورهایی که تا به حال شناخته‌ام، درگذشت! او همیشه پرکار و یک میهن‌پرست واقعی آمریکایی بود.
🔹
جای خالی لیندسی بسیار احساس خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/449371" target="_blank">📅 11:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449370">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIEzsydbf-4TNd5C6BxLQ5nuTbD1uy--6glVpU6LiS8qBtJk5PC7vXjsxQ-0tCDRyT_1X41fUDom1YkuwsIhfp6hOYVU_HRoJpbkKCtvVHMaW3-U24TxbKPjkcC-MOtPO3fpeHf7fUdSl_IHUySKNUDmzbEYKcs3pH3dlmyTpK1Aurtfs1FY7SYosCnCJHxXeAsFwy6Jo4cyvk9aICyQ3pVBoit07sGzCk3aJ-8JwjP4FpDKNzzYJAMwwYzLtJdMEmpezkdNZCmIr5taDlIHoaRWRmr5SItYKC9K-Zw-OZwR0962YlG7g-nT6HqEXZ2Ej7L5DBGszZnUP2j48X7S-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: فقدان لیندسی خیلی غم‌انگیز است
🔹
سناتور لیندسی گراهام، یکی از بزرگترین افراد و سناتورهایی که تا به حال شناخته‌ام، درگذشت! او همیشه پرکار و یک میهن‌پرست واقعی آمریکایی بود.
🔹
جای خالی لیندسی بسیار احساس خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/449370" target="_blank">📅 11:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449367">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
سپاه: مراکز پشتیبانی لجستیکی ناوها و سکوهای سوخت‌گیری ناوهای هواپیمابر آمریکا در بندر دُقم عمان، با یک حملۀ سنگین و غافلگیرانه درهم کوبیده شد. @Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/449367" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449366">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌
🔴
وزارت کشور بحرین از فعال‌شدن مجدد آژیرهای هشدار خبر داد.
🔹
برخی منابع هم شنیده‌شدن صدای چند انفجار در بحرین را گزارش کردند. @Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/449366" target="_blank">📅 10:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449365">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o83mtPLzoJ_LHo8TIBHULAldPZYNfvIEH6BTxOkDeJaVU5G5m6zYo8b909L4wEXHITM8Agg9yqDp0oxkflLCA_SWEZZJx3Bo61FWlMLRt3qYglZRq-GY3kokfuG7Rviiz1xjCdx-2dt8M23di0NeNgsXXZ6aCgfBDT6U-TjWKu0NC-eoCl9K_3prj83hHRihP-sEktm9dH3kV6-hwMcGb29knxcueUTjgn1FAIvbdNNZ0ddzdAE17H1uiz05vnX2Tv00RvxEdE-MOZ2wLFc77v9b2HtR40nlSXkEkI7gSRzpquxz1ffCduq9HqEbSNdSVbGKYj3nCQZp0ofdOsEj0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات ان‌بی‌سی نیوز از مرگ لیندسی گراهام
🔹
شبکه ان بی سی نیوز با انتشار جزئیاتی از مرگ سناتور لیندسی گراهام گزارش داد، نیروهای امدادی شامگاه شنبه پس از دریافت گزارشی مبنی بر «ایست قلبی» به منزل وی در منطقه کاپیتول‌هیل واشنگتن اعزام شدند. تصاویر منتشرشده نیز انتقال او با برانکارد به آمبولانس را در حالی نشان می‌دهد که خودروهای پلیس و آتش‌نشانی در محل حضور داشتند.
🔹
در همین حال، این خبر در شرایطی منتشر می‌شود که میچ مک‌کانل، دیگر سناتور جمهوری‌خواه و رهبر پیشین اکثریت سنا، همچنان پس از انتقال به بیمارستان به دلیل ایست قلبی تحت درمان قرار دارد. سخنگوی مک‌کانل اعلام کرده است که روند بهبودی وی ادامه دارد، اما جزئیات بیشتری از وضعیت جسمانی او ارائه نشده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/449365" target="_blank">📅 10:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449364">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1408d2321a.mp4?token=KiGK8o5OXs5aWnxkhWXVKyQW-_ao87QbT4K2T6fCNxbVB3WS0r6T778e1Qgqqbhtzy8TWlnAPF85FewMCNGT_xkpl7N8oTxallFyCs5EtwIkmH5asx4qQLEke8mpnDIcqlbeC9kxDkC7Gjk68jC9ErTJWK9stzWhrtHhQ8Ls0G8jCc_QUhv8HrusIRYGPkaNyyF9FwDMWJATYjewU89BU9CRt1Awodp51ZInwf0UugJLgiVyKGknXc4OigOI3qKPYxoyir9tPPNnBPpxc8OdR9pVVEo3bx5yf39Iyuch-WwfLkrkVBxOOYehOyHURo17KpFujCJui8aw-zUIHSlGew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1408d2321a.mp4?token=KiGK8o5OXs5aWnxkhWXVKyQW-_ao87QbT4K2T6fCNxbVB3WS0r6T778e1Qgqqbhtzy8TWlnAPF85FewMCNGT_xkpl7N8oTxallFyCs5EtwIkmH5asx4qQLEke8mpnDIcqlbeC9kxDkC7Gjk68jC9ErTJWK9stzWhrtHhQ8Ls0G8jCc_QUhv8HrusIRYGPkaNyyF9FwDMWJATYjewU89BU9CRt1Awodp51ZInwf0UugJLgiVyKGknXc4OigOI3qKPYxoyir9tPPNnBPpxc8OdR9pVVEo3bx5yf39Iyuch-WwfLkrkVBxOOYehOyHURo17KpFujCJui8aw-zUIHSlGew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: مراکز پشتیبانی لجستیکی ناوها و سکوهای سوخت‌گیری ناوهای هواپیمابر آمریکا در بندر دُقم عمان، با یک حملۀ سنگین و غافلگیرانه درهم کوبیده شد. @Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/449364" target="_blank">📅 10:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449363">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyJnFlbitho-rYZUIIrjHra5ynG8PCr57F5H9vkS75sLszQYTOVgYuaGz_V8D-4z2_exD5Ez5TrIG7MEsZPn1CWxpQhNUjxOHhEqzfdRGYZjm8eUZi-jlspycBZoyNTl6ox09D3HXdxuYZM93PYNB3q4CHfc0qjDpunSaaJt47BC7aBo3Zj0CGLoV2EM7mU2sJr4e7j8OXVaOKEWPBFmwr1uX9gc0bjr4R8OJgUsKw1c5NLopI2l1KU-GsHJdEvV1sgPiFJuVljK2pE57Hr-m2EyLoQjTeAv-Bd85vGpfjwSWqxWAAqPtNrb65kUG0s9lwA7Mdx_Qn035m9ruVPgGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوهن، وزیر صهیونیست: سناتور گراهام یکی از بزرگترین دوستان اسرائیل در واشنگتن بود. او مواضع قاطعی علیه محور ایران و نقش مهمی در تقویت پیوند اسرائیل و آمریکا داشت.  @Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/449363" target="_blank">📅 10:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449362">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJ9a_Y_lSMEitz1XAswqveqzPOGwQab0s7-GSQ3KP-zduyZjM8rZlRrt4EhZ4ta3G9FZSI9v6z6lxteWkHWlKkZktP3MzgRccbwlKQQNwP0VeDQkZqb1M16x7UrXesnHJvrzVTSV3OWc-UdpUsHU4mbj1iCTfeUemBOuwXNMNMShQwjcdHP9zqCniZIrK8XP_uJo3R3hsiAhkC_pEkgk9p47JJKTqaLGNZDNoNxapSdhd1WE3M7NmaTprcfdnsYEEExq77jbLzPxyLY9GU9QxD2_pi7oAfEiGWryc8yp-bivjQx1OhH_lAP4pjDNhPdldYmgzxbfCp4M8gPs6Ik_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ رژیم صهیونیستی: دوست صمیمی اسرائیل و یکی از قوی‌ترین و پایدارترین حامیان آن را از دست دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/449362" target="_blank">📅 10:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449361">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzXvogkkdFqfZoQ-C9dHnP1kmHf6b5j21fyWEyY8fcEuFnsoYVlfZBxgK7_7VvHfFbMhWGGpcngb-hEcapgPesFN76wjU8qVSLB1DKp1WKvQEA59-OiK1-t-oEG8DSCLxsWLnL-nVMtDuMQvY3paNQ5fNfCg3pF5-4B3bMdB9zpBbXp1tTuTtXg46UGKVVeqo03HDkdklUjUR8Tok5VYpQLGGaVmhvr1HdT_tADWME5bnRrex-eOWoris8WO4Eh3k4H5koTKWybG3AgRTqIv584Gsm8yOncpVnpe9cZ7kylnLd_LfD2KoXD5ScKShMjKmpXottsSjy0cLo6v5-2iVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بنت، نخست‌وزیر اسبق رژیم صهیونیستی: قلبم از شنیدن خبر مرگ دوستم شکست؛ اسرائیل یکی از بزرگترین دوستانش را از دست داده است.  @Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/449361" target="_blank">📅 10:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449360">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TK3SSpv8Z9d0JMKK50x-PRoMAEwUBeUFy9KnQKxABUE83_BUS2lUa3Z-AE9MHLSrldhoQHV68o6Hh4hvJQ1DQE2sY9E0eqAfLS_ipcV7pS_9QnpN6rQb8DTLjix6_dcJy_RJ1x--Nc3iEun4GNMGLwYOqhMwXO-mcmzxPhopLsPdOdLFwpq2Y29Oi9ZjWXsuQ2pqSaTrHegkzEkXpKH0OHqo5zuaKo6wHu15Qsfr45rWc2_0NotzWDTxbNwyRox0hJ5if3tH2DjGiZ8CCc3zFulGP_db5Vy5urhSgOnP95wAExr5N65Vs-XESg4SrhYlRSKJg5MaVtUJhQJuS-ojTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بن‌گویر، وزیر تندروی صهیونیست: اسرائیل یکی از بزرگترین دوستانش را از دست داد.  @Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/449360" target="_blank">📅 10:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449359">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">احتمال شنیدن صدای انفجارهای کنترل‌شده در تبریز
🔹
استانداری آذربایجان‌شرقی: امروز تا ساعت ۱۲ به‌دلیل پاکسازی منطقه از مواد منفجرهٔ باقی‌مانده از تهاجم دشمن، احتمال شنیدن صدای انفجار ناشی از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/449359" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449358">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCXsWuHLK9_pnKYQs8bG5oaRJ7xx3neJKRsAGIcGWJk_-8uf-AjZhcCTR2MzYO2aygzXZXJNQT1EaiSygH4XEJF3Nq9dJr3e7vBb0RbrgLXkpixaXPN1-soWMuySNzaqt7Hve5JThgp4eBU-PLxPgzKE7WgagMGBVfr0fMcOhP1qGM_gC1cQgUmeoff6OGHU7Rc4d_-PStfa7xlDqQtR35wLayZ1OLWpMQ7K38wlwo2DOadDKL7aWryA_HhR0WrdYkskum2Q-D8N3svcIwNzMQl_HE8sCgl3SnGHEXPV7lVxxagQcwDZwMFc5lfjh6i-Q6aE52_n54EHdX_eD6lBDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
ارائه ارز اربعین از سوی شعب منتخب بانک شهر
🔹
فروش ارز اربعین در شعب منتخب بانک شهر آغاز شد و تا هفته اول مردادماه ادامه خواهد داشت.
🔹
به گزارش روابط عمومی بانک شهر، فروش ارز اربعین امسال نیز همانند سال گذشته به صورت دینار عراق انجام می‌شود و نرخ آن بر اساس نرخ اعلامی از سوی بانک شهر خواهد بود. بر این اساس، به هر زائر واجد شرایط، تا سقف۲۰۰ هزار دینار اختصاص می‌یابد.
🔹
در راستای ارائه خدمات هرچه مطلوب‌تر به زائران اربعین حسینی(ع)، بیش از ۱۱۰ شعبه منتخب بانک شهر در سراسر کشور مسئولیت عرضه ارز اربعین را بر عهده دارند.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/449358" target="_blank">📅 10:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449357">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmEBAXSyCkhDUZWLbtCd0tcUznWrdwowuUPBfaw8ybrT8YdU5_F1qPGQLwuJ5dGIp4ZrM5v2Gv_jEOdLI38nD3cP6kTeEmKbF4wEymF7a2NTYbMe3Fu-FIP8OzzICXT5XKoJy9-gtR6buM_kB1OA0TvVZMLGKppqac8abfFliKT5Q9V03B-cUd7DkIbxr29pjC9KDdAgt25Rfo80e_eA-aW4-riapR_BExVI3dfMV-RmBTGDsVOoR8qIpIwNgZxswRQPhnMpplZOGLF07sg4umfOSULGMkOabKFvFC_4Jm5Pz4A41kINJ4eJ9h1Ty0S_SWtsPa1sOOuL3OyuUf_0pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/449357" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449356">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/449356" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449353">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QaEq5BUeqBbPmsEFm6CZiNIpMjfUsGjKrzXdJEvS7OtR_xarMIuOYb5tsJGam1n-1G1yB5_ro79ZJGL_MMdsgrNNWPSW4034c6NpnxJgjwt_Y2SlHy_6OoSiTKijglRZEZRNex1_7GvjN5O2lMgxBIGF7K6JVN-_zkpzl2qu3NP2ni0rW-kF9zQ1YSCUrNhev46kUfsu86Z8Qiaaz63LB3NG7hcvGu_XfGledqvoQj0PPuqVv5kTgj3EttG_JXUNNZ4u1OHz3l7O1Xm9cZQ2Ir6rEjkA_8wGoD-IomM4_WiTeLvFG09iEPxDgI7og1TeSOc8n3IUJwpNtMr0dAmz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JE5rUd4qBd8w2YfCWjVo00ATU8Er_7wi3V9N-HcTWv2CfM9pEgyPOA8iYcZ_7M9nH5kAY-Cz7TNgQNapPCnYpRa8mcy51BuYPIxpXWvP8t3xAonfKJlwXJvdudarcYRfHeznBlP2mf71Rtg5WVxUxswUELBLufRQ8UHf274CifgLVncu5bRS7U5d1Pe0ZIGM02tXN66w_F4rOiA-I7CvwBU_OqXacPFC7Kn_3Lk-WL9PaR-VclJOb-0BE4srSHnk6gmDbpRimffUxvYMSimrivwvlxxgfXrwdPheeFCcUqo9dai07FvCpvWxv-pGIU2ANldqQzB0zTau9ImaRJniqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjtvofmuxNvqYE1wo08MRuetgWznp8jzeTfhUpIU9Uf2gCWuwYrOThjASGgcnL13MbPrEmiY49GBsCxOt-dFVyfcN32qFxqwoVZTuB2oIA6qUUJ25mS___qH2_C_jtuH_3Jpi9cdzIsmwCutzCOZ5-IsompFJdvOepj5tLeYjF4QV1pB-JlKy-KjN3GOqQwoosEVp4YmJAblcLgdx8ClrNumLfnloCDVf9_QzWNapEDxzbiC_axL99neh2pO5-Xe6jczGsc9fs2PNwhFvLdhODx-tdwL2wYBEa2mVOdzRgr9rHlcHq3K_BRwNnDInR2UOct_P__x57zx8eMYx5CmvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آخرین اقدامات علنی گراهام قبل از مرگ: دیدار روز جمعه با ولودیمیر زلنسکی و بازدید از تاسیسات پهپادی اوکراین
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/449353" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449352">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iehb-917iqEgb6WBajOTh4MFErQTdeLq2-MMToTxKaDruS_Z2TR93irWcMLjPrjPgHC_8z3lxuvo2gdJY1FNzi_Vx5Ns0Tc8qC9eNzGOtVRut0UROJgoa4JnsjGSwMmwfgO6MqX031qGoLanvLYufyEPLfwq-DGHk9rHTlKtn-UNPPx5bgLYPgsm4qtc-TLGPOyXIbqXEl87U5Z_6aR5sF7nxVvVlKrLIaNDsr-fq1nkmIeWgEt0p310G4IyXEe1jmFomhxihzOBwH4bx_cdP9zjv6LC9hXqqD_jZKij06S7In7r-vsuLqVNgEiR_t6YCZPoUnVcbCBDThOIdpcJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرگ ناگهانی سناتور ایران‌ستیز و اسرائیل‌دوست آمریکایی
🔹
دفتر لیندسی گراهام، سناتور جمهوری‌خواه و جنگ‌طلب آمریکایی اعلام کرد که او بر اثر یک «بیماری ناگهانی» مُرده. @Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/449352" target="_blank">📅 10:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449351">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌
🔴
منابع خبری از شنیده‌شدن انفجارهای شدید در کویت و بحرین خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/449351" target="_blank">📅 10:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449350">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5KL7727YVFxVVXSgVNeWIuQ69fpTrs5v24bMdbeXaQH4smICMpiQ75M8m3W5HtzhWQMxcvS31IOHj0HyLOUvkT8_N4rLVuqEzsvZh_SY4QnvCC30z3v7ErSP6hYaVoXI0US2GQezPjKUF8fCeKU9bMJ5Igfn5XJPY15v26Nt61eL1CkpAeYESOVxagQB1vuf0tfLl29aiimcY7AR8ZwN896Fq-DDXovQEyx2FHdAeyVmmTCRoAsa-_Hzml0xyOVBpUjg6n06LcLLsWF2HRduk3GpdWw69Py6UxyEzAbkSXc0tHmadi5dEYLiuusi0hOQQ_RZQmAGAgBpVEiWiG42A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شلیک‌ِ اخطار نیروی دریایی سپاه به کشتی متخلف
🔹
نیروی دریایی سپاه: در اطلاعیۀ قبلی گفته بودیم مداخلات بیگانگان و تعیین مسیر غیرقانونی حرکت کشتی‌ها در تنگۀ هرمز، برخورد قاطع ما را به‌دنبال خواهد داشت و روند افزایش ترددها در تنگه را با اخلال مواجه خواهد کرد.…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farsna/449350" target="_blank">📅 09:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449348">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2DYP48onq11QaN8ClRVmkuCXZ9ZLhwOeSXnkN9_9QlY2QpkPFFdm09cTDUgwAkpbijBIu48OM8JA8S236gpHVjbNTgvR8c0_8f53PCzqLCWjRjDnC9yPFBOUFEqbr7RimylnZS5NGr5Pe1d_V4Jyh6juR9f8PcVHDbnzdntX9XrzwQH5f7G1NzTYOF5qWYFEiJ3zHY6fmNqZINhW1fR_i_EK43rcaLdwJTcfkj3zngMV3cLQ98xb86m5YE6nm2c4p0e6qJPp0f08Ks0yv7tAEJqGeCpFyp-BArzkHNJ7OEsmxJOtlw2CfcmllINM09rr8E3B7G3PM-YBEJDZmZbMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرگ ناگهانی سناتور ایران‌ستیز و اسرائیل‌دوست آمریکایی
🔹
دفتر لیندسی گراهام، سناتور جمهوری‌خواه و جنگ‌طلب آمریکایی اعلام کرد که او بر اثر یک «بیماری ناگهانی» مُرده.
@Farsna</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farsna/449348" target="_blank">📅 09:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449347">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyRM3BxGk0gp4b0XE_RwdWu6fTiGS-n2-jvqmPL6zvX2cJIY54ZXZoukBuhOEepUrl-T9ev7lmbiab3IHVChCFtUDQQttSf949ubGxfc_OFuVAsUCgHseRureUS40-HcbF4wCJ0d-EHff9p8biTpDUoSoeevlUfD3uqdWihB1-von-r7SK7J8MQ55ED8-mgA_DbxDAQXvjy3xx-dTjDaO5banbLSPpxrRv7Naic4gRJLHEQ6DBipRbKTaWyvdEk_xZ37KJbaM5JTfyKfCrNg0SDyOzE609iS3j3bVqdi-y8Zuf1YzVcEVl_r09GEmGRcVO41a75dITIMIloxMXNVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی با استقبال مقامات عمانی وارد مسقط شد.  @Farsna</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farsna/449347" target="_blank">📅 09:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449346">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یک نقطه در خنداب هدف حملهٔ دشمن قرار گرفت
🔹
معاون امنیتی استانداری مرکزی: صبح امروز یک منطقه در خنداب، مورد اصابت پرتابه‌های دشمن قرار گرفته است.
🔹
برآورد دقیق خسارت‌های جانی و مالی در دست بررسی کارشناسان مربوطه است؛ جزئیات تکمیلی متعاقباً اطلاع‌رسانی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/449346" target="_blank">📅 09:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449345">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مراسم بزرگداشت امام مجاهد شهید در مصلای تهران از سوی رهبر معظم انقلاب سه‌شنبه برگزار می‌شود
🔹
دفتر مقام معظم رهبری در اطلاعیه‌ای اعلام کرد: به‌مناسبت شهادت قائد عظیم‌الشأن انقلاب اسلامی و اعضای خانوادهٔ عزیز ایشان و همچنین با خضوع و خشوع در برابر عظمت و شکوه تاریخی ملت مبعوث‌شده در بدرقهٔ آقای شهید ایران، مراسم بزرگداشتی از جانب رهبر معظم انقلاب اسلامی، حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای(مُدَّ ظلُّهُ العالی) سه‌شنبه ۲۳ تیر ۱۴۰۵ از ساعت ۱۷ تا ۱۹ در شبستان مصلای امام خمینی(ره) تهران برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/449345" target="_blank">📅 09:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449344">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCnYBQtlkaFw1G11qV4J5E-qBKLZF_UxqwSsNRLQ5vilce5pTT5TaeiaX-NS0oNcMQJZtqmUKQQhZVvNBCFRPACn6ZRYj8enjBEAYcXHi12DcfwFqli-_0AmMChzcqMdfH9Gm8rCFIn_I6qhnmCbfHI9lN8lTB8opBJ37niYsX9I_6Zt3kDckQuO5wuy4ep8ud1Z14w0XZOXMEsHGXrM044Vt4ghsApNZAQwTbRoKCXQaHJ8WF98mTN_llniyYubwopu7-SX5M8jvMs4qep29gTTDTnYVOSJa9q0LN-yXGUwbAYr0PeNyTh_T7hWwnFIFTpwZi72PXEj9B8OMAJOJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوت امیر سابق قطر
🔹
دیوان امیری قطر، نهاد عالی دولتی این کشور، روز یکشنبه اعلام کرد که امیر سابق این کشور شیخ حمد بن خلیفه آل ثانی،  در سن ۷۴ سالگی درگذشت.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/449344" target="_blank">📅 09:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449343">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c425861fa.mp4?token=BQl_6BWGc7ynaMBXRhB_lgRIaMgi4pHJXnAHQzChyXldXhnA3jqxCG76SS5Rr2PmXb_UikIe-2lRPiEaCIVVEFS-KQN5I6SRb6EqEeyZQjoUfv1O5dsdXvV6VhnFvNvJuQykjSE4rYPzTo2rISmd5dzXYaULIQH3jJc76nagbowIR1P9hH-_HphqlBlq2_rbjo_1DQXz6edXFFtlMZ8UjU5Bp5yQjsVbEQStk7brLbq7DKhGCgiv2IPOlsJ0BQNmr0sHe-oisr2Qcg8zBiYFNc5p6BscZ4Y6FnWj7lLwBIMamG-LXIR4M8o8xegbdBeLuy8YTyx4Rm07FiGsb54lyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c425861fa.mp4?token=BQl_6BWGc7ynaMBXRhB_lgRIaMgi4pHJXnAHQzChyXldXhnA3jqxCG76SS5Rr2PmXb_UikIe-2lRPiEaCIVVEFS-KQN5I6SRb6EqEeyZQjoUfv1O5dsdXvV6VhnFvNvJuQykjSE4rYPzTo2rISmd5dzXYaULIQH3jJc76nagbowIR1P9hH-_HphqlBlq2_rbjo_1DQXz6edXFFtlMZ8UjU5Bp5yQjsVbEQStk7brLbq7DKhGCgiv2IPOlsJ0BQNmr0sHe-oisr2Qcg8zBiYFNc5p6BscZ4Y6FnWj7lLwBIMamG-LXIR4M8o8xegbdBeLuy8YTyx4Rm07FiGsb54lyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: مرکز فرماندهی و کنترل و آشیانه‌های پهپادهای MQ9 در پایگاه آمریکایی پرنس‌حسن اردن منهدم شد
🔹
اطلاعیۀ سپاه: رژیم جنایتکار آمریکا با تحمیل ارادۀ خود به حکومت پادشاهی عمان، شب گذشته تلاش کرد بار دیگر آزموده را بی‌آزماید و با تحریک چند شناور، مسیر غیرقانونی…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/449343" target="_blank">📅 09:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449342">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌
🔴
وزارت کشور بحرین: آژیرهای خطر به‌صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/449342" target="_blank">📅 08:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449341">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اصابت پرتابهٔ دشمن به ویسیان در لرستان
🔹
استانداری لرستان از حملهٔ هوایی صبح امروز دشمن آمریکایی-صهیونی به ویسیان، از توابع شهرستان چگنی خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/449341" target="_blank">📅 08:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449340">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20121c07f8.mp4?token=uim--37sPE1aV-C_Gbhm2C810RX4YY8jvyBX8eb1V5J7JgeusBmXGaDC4C5gNIgjcrHf78vmm6sS-iArMHMXz49y-d1A_-A74Be-T80p-HjETx4RRXbZkXEfULXrpLZExAQbUvTk2iSh50_8KGjkjb6FcvmrfHHwl3vgaN5rFTSVOnz8CChpWIzoxTCMi8Y1afzp0WUt3n6Y3ncm1fBtWND8I5-DVg7chN7MAgjDlI-5yyYFTzk5TFJ64X78N9uhBsOPRv62YMvyasEKZewx-3JhskkCc-LNVflUZMZ5De3a25QV3goOCw1n1Qj8coTdfiFvgGFG6u2zY3XSB6QIbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20121c07f8.mp4?token=uim--37sPE1aV-C_Gbhm2C810RX4YY8jvyBX8eb1V5J7JgeusBmXGaDC4C5gNIgjcrHf78vmm6sS-iArMHMXz49y-d1A_-A74Be-T80p-HjETx4RRXbZkXEfULXrpLZExAQbUvTk2iSh50_8KGjkjb6FcvmrfHHwl3vgaN5rFTSVOnz8CChpWIzoxTCMi8Y1afzp0WUt3n6Y3ncm1fBtWND8I5-DVg7chN7MAgjDlI-5yyYFTzk5TFJ64X78N9uhBsOPRv62YMvyasEKZewx-3JhskkCc-LNVflUZMZ5De3a25QV3goOCw1n1Qj8coTdfiFvgGFG6u2zY3XSB6QIbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
وزارت کشور بحرین: آژیرهای خطر به‌صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farsna/449340" target="_blank">📅 08:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449339">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
منابع خبری از حملات جدید علیه بحرین گزارش می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/449339" target="_blank">📅 08:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449337">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
سخنگوی ارتش: آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
🔹
امیر سرتیپ اکرمی‌نیا: مداخلات آمریکا برای ایجاد مسیر غیرقانونی در جنوب تنگۀ هرمز باعث ناامنی شده است.
🔹
ما موظفیم برای تأمین امنیت منطقه و تأمین امنیت عبورومرور کشتی‌ها تلاش کنیم.
🔹
نیروهای مسلح مقتدرانه از حقوق مردم ایران در تنگۀ هرمز دفاع می‌کنند.
🔹
بانک اهداف نیروهای مسلح دائما درحال بروزرسانی است.
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/449337" target="_blank">📅 08:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449336">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
منابع خبری از حملات جدید علیه بحرین گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/449336" target="_blank">📅 08:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449335">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8QN1oWo8S8mmXso3uYRXbE6GZHKVucuabI04t7-0sByKpVca9ctTUm8jWscLMtrQA2p7mABn0TYa70NPx4dBRGLLE1RXUh2g_xZ2LQhn6fRK4rxW72hn33SiD2HzO26VgfPdi8RxZuFa2lSH3p3QXxW8Ljd3b1ewtA93qJ3dCoIsiY-Y-pFYt54iuUJeoyOSNPcmHu5TAMfOKlR27ATVaiwPi8y6Sv14GWbtINintHDjlkhgIX2sKR-BkIY6iSxF67UmgcFrnuPUefHMrSCiAz375Kwmy90WHn2x8uK3dd4tfWxe_gulItJOo0p7cjxZs2fVK9dLvD-P35UMM_UZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بلند شدن دود از پایگاه دریایی آمریکا در بحرین، در پی حملات ایران  @Farsna - Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/449335" target="_blank">📅 08:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449334">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‌
🔴
وزارت کشور قطر از ادامه‌دار بودن حملات موشکی خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/449334" target="_blank">📅 08:03 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
