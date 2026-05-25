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
<img src="https://cdn4.telesco.pe/file/KnTFg2ZFnQ4Ir25b0dyBVvYDai0oY_91N94pbqHkaJgp5Qd2QerA5nflYq94NYsdPPeNIjHyM-o69EUL0bpWpwx02iX-xioMMrUcc3EEloq2kznU9uAqvjQz7uA5bS2_crLWmo2vlPtxCKjVYLmi94cWZS_1tWtP7uNIihLBQyMbuAX6Elf3Wxg4Pb-PoSuXGq9LE5KlgnaP_nGEfm_MfqKogEEEgOincI6Hwjjpn0iVrKc9I14MrJPTyFzI4UIvVIkuWcbgwBa6IIBHv8XwAss70ZsfyRmKsEGolHAjPKkxWeKS_mRNcUHUiX-smxn1cigeWjYZGHXqxdF-DdGsUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 20:30:38</div>
<hr>

<div class="tg-post" id="msg-437972">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قسمت آخر سریال ۷ میلیارد دلار پول بلوکه شدۀ ایران
🔹
همزمان با طرح آزاد شدن اخبار آزادسازی پول‌های بلوکه شده ایران در قطر، بی‌اعتمادی ایران به آمریکا سبب شده تا دوحه مسئولیت تحویل پول را این‌بار خود بر عهده بگیرد.
🔸
ماجرا به سال‌های اجرای برجام باز می‌گردد، زمانی‌که فروش نفت ایران به کره‌جنوبی ادامه داشت اما هم‌زمان با روی کار آمدن ترامپ و خروج یک طرفه آمریکا از برجام، ۷ میلیارد دلار از دارایی ایران در کره‌جنوبی مسدود شد.
🔹
اصل مسئله پرچالش پول‌های بلوکه شده کره‌جنوبی و قطر به ساختاری با نام حساب امانی باز می‌گردد، سازوکاری که دست وزارت خزانه‌داری آمریکا برای تحریم ایران را باز کرده و امکان نقل و انتقال پول بدون اجازه واشنگتن را منتفی می‌کند.
🔹
کارشناس اقتصادی علی زارع معتقد است که ایران باید به عنوان پیش‌شرط نه پول قطر بلکه مبلغ پول‌های بلوکه شده در سایر کشورهای جهان را نیز مطالبه کند؛ اما یک کارشناس اقتصادی دیگر، محمد اصغری می‌گوید آنچه اهمیت بیشتری دارد، سازوکار دسترسی ایران به این پول است، بارها دیده‌ایم که گفته‌اند پول را آزاد کردند اما ایران به پولی نرسیده است.
🔹
کارشناسان می‌گویند، ساخت مصارف دقیق هزینه‌کرد برای پول‌های بلوکه شده و پیگیری کانال‌های مالی امن مسئله اولیه برنامه‌ای است که ایران باید روی میز بگذارد و آزادسازی پول‌های بلوکه شده را مطالبه کند.
🔗
شرح کامل این گزارش را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/farsna/437972" target="_blank">📅 20:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437971">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ed3iFlVFen_QHJrPl5gMQxhV2dfXSPN8aTolZowYqXW354J1XW8C76Ejxys4As4ZEIwY-YB-k1kaiZV6HhW6pkLKYHh-c6jMeyqCGVm3SIgLiZyHohi6DWhQ_dOxOkJPBKfsEMxOE1Zc15Srwn4oam4j0B5EqgIqUQrNJd0fl-eBOUvFFY5ukdznOMKyPMFF8Hh-j15UkjWgjDBzQ5zVUsoXJ3aBysfHFeIdDH7Ivpq8FyPLDUYWNxKWLKSLpywT7zarIJEvGuxECDg91gakL2xSdOWCBeR_6mvqcsC64VvXzmF51M4TDwbzUaM5FKZiqL-_EEEd34lOuJO4WABMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورکر: هر توافق ممکن با ایران برای ترامپ تحقیرآمیز است
🔹
رسانه آمریکایی نیویورکر نوشته: هر توافقی که دونالد ترامپ برای پایان جنگ با ایران به دست آورد، به دلیل شرایطی که خودش ایجاد کرده، تحقیرآمیز خواهد بود.
🔹
جنگ ایران یک «شکست استراتژیک» برای آمریکا بوده و حکومت ایران اکنون در موقعیتی قدرتمندتر از قبل قرار دارد.
🔹
ایران در چارچوب توافق پیشنهادی، هم پول نقد دریافت می‌کند و هم از تحریم‌ها معاف خواهد شد.
🔹
به‌نظر می‌رسد جنگی که با هدف سرنگونی حکومت ایران آغاز شد، در عمل به تقویت این حکومت منجر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/farsna/437971" target="_blank">📅 20:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437970">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7Xi6Sbsp5n4lmxDwRMgtahSLVgIfgNqt768aRS3xhGesDQd6_NA_bnI-tXj2UumfeIrnmlGZRaK7aouuCv9wPn77f7zTgl87Md79pincgDpYuzhlCR95zioL3ifRrfZ5PTltIlxMOGNH8w-TO4g2my9lLnHumSLinBe-T_G0d7Sv-1lroWVhZjoqNLBA6SQIh-ymCk_X6fQAxy1AEXTCejc_VRtVlWUCpVRFVQcWHYk7z6leBaEyNqkvLcz4p0AIFtCENZLasrweYRWuFNB4-m3mIrqo-_tp-oncDLZoAMUQJooFQ_H_0Vh9e2zqu0BsI-sFtWeSu3AE_lfp5329A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام شبکۀ سرقت سوخت از خط لولۀ اصلی انتقال سوخت در هرمزگان
🔹
رئیس کل دادگستری هرمزگان: ۳ نفر از سارقان فرآورده‌های نفتی را در حین برداشت غیرقانونی سوخت دستگیر شدند؛ در بازرسی محل وقوع جرم، یک لوله متصل به خط اصلی انتقال سوخت کشف و دستور مسدود سازی آن صادر شد.
@Farsna</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/farsna/437970" target="_blank">📅 20:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437969">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxBEhI9d7fgDekoFeLUzPBtPLX2CXtr-ZXAhK-aoiLb36gstu8ZvN4_e0MP6KWdgJXCSurGv-AeSw7BhQsgzyQ5t6nUxy58TBznMSH1HWia4R-fBEDVkSkr34rcRDiYm-GEhlE9hsQhzaMTJ-B_nKDzo1hA4-X4tCIQEQv9Gvw7sSThj8xDfo-jjEDlSrgYKq0UXrpJEsJ15bFoMUKK4W28PA1n5lYRW11qvcRPl5v-dIXRp0CnBno1ToF9m761ijyY-1BRwNdAcpi-QNTBWx4i3gdBGtwGYxXPUf0YGS8YjfSngGNFNiR2yaVQSYXhf35oBnGyFO76G7_SMfc2oaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های تبریک عراقچی به رئیس مجلس لبنان و دبیرکل حزب‌الله
🔹
وزیر امور خارجه ایران امروز در پیام‌هایی به رئیس مجلس لبنان و دبیرکل حزب‌الله عید مقاومت و آزادسازی لبنان را تبریک گفت.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/farsna/437969" target="_blank">📅 20:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437968">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02341b84fe.mp4?token=QyjOdGpelz0V6SskJ4bWqi-4zSpTBybltWFEc5RUoTQDyURiGseuUkvUxhWtjBIZMRDUHjem6FEt2smnYswHcpPRjV03n1US2Txc47w2qlxT1LFuYdiIVzl1EAlJHBhf_NKP0Vzzo2CkJwIhVKyGdpTrHSOxPyvmiJT4dYunQ0pNxng29kSx4QWODeKQEns4VH1gnTuNbd37d80CYL9VejDF4wmzZjC0dQRWGHmM1dPwl4gBELSK-fd9PMgqYab4UqK3WfnfNEwDmXXQUeJJtYgi9GcemS0EBjdDSzYIDDZr5wMaLADhDYFj9TINJvpII07_GL6ME20vPvj5Av14tmawSe7UBWLJeC_N-T-o-_h3oJEj1eWFGiGbfJg2eut5aqzsPKKDkgB4hKbXD-ZxAPJCHBYmG6PKb_g7IbgznGaleyTklsveLBjiAQ4rEDRKrxDWtFzNCAmhXKpJnBZJc5jo7AJent4AZbgQGaUO0bpHx4uskF0gu-rVF-Hl3GtaX8G5cJ4OZg5VVm291B8d5VcAFFVMhRs27qCbzwIty1OSw1VWpQRC2bQJvgRhGkpyktQgCMxOb8A2Tcu6yDoB2XSk3Jsmw4xzUSOwDNoWHOM2JSH-JENJKUBY_4pP0W13THucVj3Io6sUizYBU8YGdA7j2LKfYyuM-vzy-OIHbX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02341b84fe.mp4?token=QyjOdGpelz0V6SskJ4bWqi-4zSpTBybltWFEc5RUoTQDyURiGseuUkvUxhWtjBIZMRDUHjem6FEt2smnYswHcpPRjV03n1US2Txc47w2qlxT1LFuYdiIVzl1EAlJHBhf_NKP0Vzzo2CkJwIhVKyGdpTrHSOxPyvmiJT4dYunQ0pNxng29kSx4QWODeKQEns4VH1gnTuNbd37d80CYL9VejDF4wmzZjC0dQRWGHmM1dPwl4gBELSK-fd9PMgqYab4UqK3WfnfNEwDmXXQUeJJtYgi9GcemS0EBjdDSzYIDDZr5wMaLADhDYFj9TINJvpII07_GL6ME20vPvj5Av14tmawSe7UBWLJeC_N-T-o-_h3oJEj1eWFGiGbfJg2eut5aqzsPKKDkgB4hKbXD-ZxAPJCHBYmG6PKb_g7IbgznGaleyTklsveLBjiAQ4rEDRKrxDWtFzNCAmhXKpJnBZJc5jo7AJent4AZbgQGaUO0bpHx4uskF0gu-rVF-Hl3GtaX8G5cJ4OZg5VVm291B8d5VcAFFVMhRs27qCbzwIty1OSw1VWpQRC2bQJvgRhGkpyktQgCMxOb8A2Tcu6yDoB2XSk3Jsmw4xzUSOwDNoWHOM2JSH-JENJKUBY_4pP0W13THucVj3Io6sUizYBU8YGdA7j2LKfYyuM-vzy-OIHbX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توقیف ۲ همت چوب احتکارشده در مازندران
🔹
سازمان اطلاعات سپاه مازندران: یک محموله بزرگ چوب احتکارشده به ارزش ۲ هزار میلیارد تومان در سوادکوه توقیف شد.
@Farsna</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/farsna/437968" target="_blank">📅 19:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437967">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180a3e98bc.mp4?token=EPtlOBFAd4z8qMwKyxgR0tl4LqLYnOpr5mWeoruQWGWIk2kMrqyI2brzCDXJ-_w4fV4kwu0p6M8SXGdFLyXLrNUe0j__kYrjnzUi3ZP6O06PNmXqjx4DkqakXwSmzNldXRsCQtKu9VDPYzx8ONuB-1BuLXIWtk2Ds0qzJV-2AbU-GhcS0KuvSonf3hzaWX7B4JIGQP8VaD7i3Rw3i6EoVnEsuyMGjg5951WpBnl7o1F_G-52_TIGXSJMIAiIAKj5MR2MC1oCaRzFTgfIPPLsbRruTW5QcxmFQq3ISIJ_OJgiQVA6bbS2PUYFUcP0EbXDnBbWffb-H-1iK5MSeKLrzWbFfW_31e4knLt2Xy6yFX0LDBvgTGw0zYotuxtX_rNZGVrxPFze0EZfI8ABKZ5wM2oxsh2ypea7Ol8u3CjWzNvwpqpvhzIH_OLWXoFRqV_WcmHJVgLVPgIu72RG7-T02Ed2OW-xFT3I8wnuI1gMG_gy2YSLB5zS-xJsECMZGLcDg5Li3suPMnvXszSPYCPJfYmMkjmJv1Tc28xyizpfEJcQcI7vXvegSdBRYVcyv8clVaIYe8WESnQ4GGWVEzps6xlQP90BHNg0jUAbZh3sRDcItjtCMVbIynZnTbhEUyEk-iDqkVN8cPTzrx7T_J6iwRrXOBsmL7PbHtzCwGKNfuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180a3e98bc.mp4?token=EPtlOBFAd4z8qMwKyxgR0tl4LqLYnOpr5mWeoruQWGWIk2kMrqyI2brzCDXJ-_w4fV4kwu0p6M8SXGdFLyXLrNUe0j__kYrjnzUi3ZP6O06PNmXqjx4DkqakXwSmzNldXRsCQtKu9VDPYzx8ONuB-1BuLXIWtk2Ds0qzJV-2AbU-GhcS0KuvSonf3hzaWX7B4JIGQP8VaD7i3Rw3i6EoVnEsuyMGjg5951WpBnl7o1F_G-52_TIGXSJMIAiIAKj5MR2MC1oCaRzFTgfIPPLsbRruTW5QcxmFQq3ISIJ_OJgiQVA6bbS2PUYFUcP0EbXDnBbWffb-H-1iK5MSeKLrzWbFfW_31e4knLt2Xy6yFX0LDBvgTGw0zYotuxtX_rNZGVrxPFze0EZfI8ABKZ5wM2oxsh2ypea7Ol8u3CjWzNvwpqpvhzIH_OLWXoFRqV_WcmHJVgLVPgIu72RG7-T02Ed2OW-xFT3I8wnuI1gMG_gy2YSLB5zS-xJsECMZGLcDg5Li3suPMnvXszSPYCPJfYmMkjmJv1Tc28xyizpfEJcQcI7vXvegSdBRYVcyv8clVaIYe8WESnQ4GGWVEzps6xlQP90BHNg0jUAbZh3sRDcItjtCMVbIynZnTbhEUyEk-iDqkVN8cPTzrx7T_J6iwRrXOBsmL7PbHtzCwGKNfuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کدام گروه عراقی در ایام جنگ تحمیلی سوم به مواضع آمریکا حمله کرد؟
@farspolitics
-
link</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/farsna/437967" target="_blank">📅 19:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437966">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">سه نمایندهٔ ایران در آسیا مشخص شدند
🔹
استقلال، تراکتور و سپاهان ۳ نماینده فوتبال ایران در آسیا خواهند بود. این تصمیم را هیئت‌رئیسه فدراسیون با توجه به جدول کنونی لیگ برتر اتخاذ کرده.
🔹
اگر سپاهان موفق به اخذ مجوز حرفه‌ای نشود در آن‌صورت تیم‌های رتبه‌های بعدی جدول به آسیا معرفی خواهند شد.
@Sportfars</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farsna/437966" target="_blank">📅 19:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437959">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKCYSU5v6O2PGRqkGv3YK3T0NehJEmsoQpwZC8AlxDnUa-5FiUNL99eoqt2Pym94Md1LrwqHnwOUxRw2g9sJVh7rcvQdL-3CVTpadQ_VwSIiS-0vLdNz0y1RWBU3-of_s6Hg7JDXSsiLF-h8ET7Ya-ONnosF60eHy53FtoAMr4Hz3n8aLlHuwf_bCF8xAwy07vSbCCYliO3PV-b8wEXiYsUo_tkF0KXZU1Dy4TIRIOApEToJItpPvJi92-PI6VVOWLnOz-ouwz6Hn4IGTs2EWZdDmpzeiCmmAxJhr2gTv-IwwcmfTf0URdilan8PzWRioYeQ6p60idF9af9gVx0r8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6TEDXNy8Pp07Ax6GKMwm04qsFsTu4HAIfVDtr9jWRaEEb-Tgs95X8p-ub4N9PgzURj23tFKT9wSBHXZauHd0K87x4OSHwgaChWRkuoypsUpTpkmYrWdcv30I580MUpvbVM8UpaExTHy9X_FMnIkaPORyWRDq_olbXYHV6lhHXKPXiiGZGJfy9oqvq_BUXpvGjhjwr0q5hZcHxHnNP8wtQHzgiJMcVKRVymdMC_VzycnOvXt1ayJrSTpbFdO6G_s8k9_rfn-Gwe-JjZR1KvEHKY4zqyWacyFQPGkkj6Hj0ogmzKbzkMPYBhidrQTlS3p4ET4jTXCFwIjenVeTwOPGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XlLYq2QHb2P43c4s5OoBQeIwUJOGcla-8HUk4SjYqUja_EBwmcbqP7yu96aAo8BPCoq77iGJdEXfkG3B5iYbg_Ccv3ob75JsDyqxLrJB_ARxwr7hKEI8QcnoVnB6cnTWfevctnP43FrEWFvU4z-Ovg42ZaLyRYjO74XRPcvswQqCDbfG84LolmgkkgWAkp1A1ArbUrgXFmbUlJbhsgnVNxpkI-lOtNhAtkVDLrDfjV3KyMZiMs7fXcse8KV1M8G3H8BIUEaAYHUq-i7EtyCJq5KlflLQM56HD4ze74qlbaGXvgezkGVC0P6CXYVIjzVoJo1F1MSzh7_dVqxvY2mVSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5Z2f7yEwf-QzujWokRZmiTPx7DwhqupVvdBjW93PgWIlYfrKxMb-hTGBhJJXBp-Pc9oM9FMk1j3_SV7xe7WDeIO6AQxdOj1NgED6MSu65L8w3eU94YRaFsJ2vtANZlSxlHebiNSxfymHYqFufHfbROFWLKtOu5grMiHik33zzsIkARfQQMbFEX6AeaTve2LHTfnlyXAM4mbKl7fydliudgn3kKBCKz4Gt8fo-QFG6PVGf1zkcMjnM2qQFBFdqKlaJMCo-yBC-57oO1U6xWpRyq5n1R69rO6bRQtanaEMlM9dY76SREofPp7kW0WY6zghvJASvzw5zmBHQCoaGNTJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q81SB-S-fHz5eyvymg3dIzB_hlBLE-l-Ozb2I9aL1FEZATJAhEI13ZVji1ox0hhvBVhFCkEbWANg-zjhJi7w2BpijyauBi_IfIod7i-AI1btNe6raW7dGoGV8jR9Y38O70-7-BJwbUE7II3qPU5C7qtr1Rq4Jw84P4oUz23jNmKga3v11jAnTsnYEDX941dcQciYVe0lqFsOnX-LVf9zA8kFBQXavXdBQ4Sl8aTumqiJ8dn38L6U-a2SRywRZFjmjazPuL-XBChfYj3R_h8eVQjAUYGeIOnFvtmQS3RYaMXJj_ZNf7wvAM8oUCwxg-8L3jI5_Zz6VgFvK4jB1SwTBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c1IihmZFF4xczvSK5FJQL0bwwAMr98qsrelgDXmZrl3w09IscCK0J_PjnTb325WvJxn21o3lemedFT8LogkoRuqlDLTfytMJykYukWEqz0QjuMXemejNXal5Fpgz7WKagx3-d6mpZxTfrAFlPjNScP2qNGYgHxHbohUFBsDpnG2Au42RFJzJDZ3JALjmGc-BfWpPb7q9oI_OlUp9GgUBDYVBxrPHCEs2o5Kf_75EjYLvSgvBg_JA-Cetp1dR0mTA_SLPOfU0IR1hrD3yc5cGTxvAx0BsMTWbzKJcYly1xuHk_ioRFCbh8I9LY8cgvbxfU0Nt1iJffFERR1CTXVXl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kvkF2IpPa5XNmpdKPQUAgMYfyuztgSIsQdbFBuo2RWfz3VVJc7YUzdzMjagjKacXuqHOjkMTRPzT-vfKsdwqirS8TD4CcdeY4IWNf5g7n140eBPn1CpKhi9BnR7ao-vJwQFQhvxOnkq9DzsUD1Am_9li7gn4nuse-mWHq1Cusfn-q4qg8Ral4eUOZTh0lJKQVAig9Sqxlm-mHckuW_kdDu7ilRzzxp-5Q4JuK5XLY3PinEJ11QZRb1-s7WgHzplYnlKPUDfITaOowUGb0kSzLu_LxQO3wJa9X60D7rae0rzIIxW2dO3loeqlYSZRyaMw2VqJuz47Ayt9DS5S1U4c_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گذر زائران عرفه از مرزشلمچه
عکس:
فریدحمودی
@Farsna</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/farsna/437959" target="_blank">📅 19:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437958">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWOkkEdvK8ALXcfflKaXHJ6dxLXc5gacZCtIYeuNVSJrU55KQHTJj3ZdGaTDv6xhEAERHBkdyRlUJM6UiT3054bGAPDYBQ2rT8-SNW0xEuCVVQ62W2U4WfY2oNpUYrspyI4ek_A1a84ezHj4HGQerag7zyt0OF3KSpYDjwYWPYsXORCfrQokvTJzSR-cB5FRZtRImgbdCWgaCPKofV_6-BQcOotNHkjDwhPcR5VSg2eVHaRVoVlv8LHpVdPrr5cHyAYs9SHMyMFuA22ezZQLS38jW4VWHm11VRM9XDQn_k3qGYRXvj52TINd5UEC4fvpIcpYwCXJiga7gu53XVFHoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: عقب‌نشینی در‌ کار نخواهد بود
🔹
این را میدان نظامی، میدان دیپلماسی و مردم مبعوث شده حاضر در خیابان با مقاومت جانانه خود نشان دادند و دشمن را زمین گیر کردند.
🔹
حالا بیش از هر زمان دیگر کشور نیاز به وحدت و انسجام دارد تا آمریکایی‌ها و صهیونیست‌ها در این زمینه هم مأیوس شوند.
🔹
میدان وحدت و انسجام هم یک میدان دیگر در مبارزه است. تلاش همگانی برای جلوگیری از هر سخن و اقدام وحدت‌شکن، ایرانِ عزیز را به پیروزی نهایی خواهد رساند؛ ان‌شاءالله.
@Farsna</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/farsna/437958" target="_blank">📅 19:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437957">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccnCwxetMJ-3-pvvmQnu94hQjfvZWh2EVkIXpirmlInnDxKW_y0wIuqFabMni0eY1xyqzgnwxPP5jm0JE7TqoWD-GNJIpGEIBx6Awdz9i4MqEAQ-1PnaeumrPD2tkjClbLVZ4BzolxFLPyRUldtGzztfaykgEPnhGfK0Eyu1DmzZuCPTXiyXU0eaiEUs5Cy-wsGdrFm2RcIwNQbXTQdQdWQXFR8Nl-uA7hVDYhltXju5Gt90_iCf_jGpHSZcWg0278IXLMPVd5Oru0fkEq25f8BNdGr45al0UqeEuqFJeGQlSQvXA3-fQtLtSfPPKhxDlCPWT3X4qIEVwaXLR_9R5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ۶ کشور باید به پیمان ابراهیم بپیوندند
🔹
در رایزنی با رهبران عربستان، امارات، قطر، پاکستان، ترکیه، مصر، اردن و بحرین، صراحتاً تأکید کردم که همزمان با توافق ایران، الحاق تمام این ۸ کشور به «پیمان ابراهیم» باید الزامی شود. البته امارات و بحرین از قبل در…</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/farsna/437957" target="_blank">📅 18:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437956">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7c1487f04.mp4?token=K7GMxDS_jtdo6JlYFLtNndeYy0CyTG3eiNpEPno0nwTyZco4gHtMt0Rkp9xYzMI7Bo4_vkOkNiNRuKu-O4CMknd4rF0qCO9Gz6VqSh6oKVp3gwwULikiEKkm6aQbG_7DsJv0afhqeB7uiRM7t2-QFdG5-Xe6aoueSF86ISIDSnRZVF4RtL1M_cp_N54PYb_EXoJbX7J556_xJNSprv3J0yDQBnMkwVcGCKF6dydFipdgp0CJXezsRB0bLqnsHBJiqUoQJpYc0PHt7R7IRPu4JIRI6ODyGGOZzJAgpo51xfHexCNWT9df8IB-XbRKdPmxeq357Ewr_0cwTFVKdcasPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7c1487f04.mp4?token=K7GMxDS_jtdo6JlYFLtNndeYy0CyTG3eiNpEPno0nwTyZco4gHtMt0Rkp9xYzMI7Bo4_vkOkNiNRuKu-O4CMknd4rF0qCO9Gz6VqSh6oKVp3gwwULikiEKkm6aQbG_7DsJv0afhqeB7uiRM7t2-QFdG5-Xe6aoueSF86ISIDSnRZVF4RtL1M_cp_N54PYb_EXoJbX7J556_xJNSprv3J0yDQBnMkwVcGCKF6dydFipdgp0CJXezsRB0bLqnsHBJiqUoQJpYc0PHt7R7IRPu4JIRI6ODyGGOZzJAgpo51xfHexCNWT9df8IB-XbRKdPmxeq357Ewr_0cwTFVKdcasPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکار نظامی صهیونیست توسط پهپاد حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/farsna/437956" target="_blank">📅 18:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437955">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1200615a.mp4?token=rgF0i_Q0oNGunpS616iDbUR0o91R8j1aVw0x9J7dFS2Fgs7IRnYSne8ZD-3LwiZ3UN_Wu_LKE6nqBMNJq5Ib1FOVwRCNShJnrcr-vC4UFDiE89hZPzKz4D025lIl11PLiKPpvmH7hR6Db7XfRsWL7pSZcymfYBy2XA2MOYZk1GP6rytk8mGBneJosfr7DfspleidcFLQ0Op3dcmL7gCCywfu0sTUSlSBdSPSirhocS80o6M5LkFV-oBTtkXUb7Wm52B1MIUxqc16V4eusD9ShWDzmlSJBygSd0Xz7Y-gueqMVswMhLCAAXlm4ERMWxMQPaTioy20TgUnNuzbqX29Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1200615a.mp4?token=rgF0i_Q0oNGunpS616iDbUR0o91R8j1aVw0x9J7dFS2Fgs7IRnYSne8ZD-3LwiZ3UN_Wu_LKE6nqBMNJq5Ib1FOVwRCNShJnrcr-vC4UFDiE89hZPzKz4D025lIl11PLiKPpvmH7hR6Db7XfRsWL7pSZcymfYBy2XA2MOYZk1GP6rytk8mGBneJosfr7DfspleidcFLQ0Op3dcmL7gCCywfu0sTUSlSBdSPSirhocS80o6M5LkFV-oBTtkXUb7Wm52B1MIUxqc16V4eusD9ShWDzmlSJBygSd0Xz7Y-gueqMVswMhLCAAXlm4ERMWxMQPaTioy20TgUnNuzbqX29Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودزنی به سبک منوتو
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/farsna/437955" target="_blank">📅 18:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437953">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKdtW2fyEoZBiCLoA5mrVFJu-jw3kSJhBhmDHNquXXAKQ_ctU24Eq5dktX5Ezh5YWuiJpmVjPOWMjFjW-xBq8SrGamNj5iLvGcg0adzrC96o-bczZEgei-em7HIw5VEpwl0Ti2YBTcKY0kFEEzsiTc9fGsaAmd1t3c7DL9oVs1ITs7-YnN5HjppYkKUIOiIC8wUnfRgsSwzyYX_Bp6ze9TrzAjEiPSEccHjz9CAtTC3Nvy-znZZ9o29H3OFGoAFWzrc2BfxtLN4cGvbwRHVsRqQGeZA9VIwCQRmVBYi9Rn8Td9JmHq54nuFDWpjIyLppgDJ8ABwwwZQLFkTHDQrsAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تبریک اژه‌ای بابت انتخاب مجدد قالیباف به ریاست مجلس: دکتر قالیباف حقاً و انصافاً در جنگ‌های ۱۲ روزه و رمضان در عرصه‌های میدان و دیپلماسی جهاد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/437953" target="_blank">📅 18:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437946">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIA1RQA45q8NOj8xVQp0O47kuF5VkBIAqqLxs4WPTYwxJZcXXYFMijQ0Ye2bz54mo_Nx7XGH0E7FgaRTt-UCWTCDmvz-GvTVcfbh87iTMX3_zLADJZuVln9Z3fXbAjPHlh52R0c9U49L_c36AnLljy1FXUo4h4-ioLIUu4WxzK-grmuK6dv7zNgqYgSMN-cpsFP_xuv85xCm_O5ABj9q4GQir5fIqacb6yal9-Roc-elR0G2vsnVEiwBrsK9heojXbjQxQBqlXk-6nwC7UA38_RzfxXsvAOiRqnGedNERv5kkZ2QajFn1kr6QTGnXKHmhXssj-k1jYtklqV-mMIcJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kVDahFNvlwHLrugV399RVUWWDYrEsty82BkTA71Ev9clzfnYVFSRPtDvQN_GjOOnC4RkRv1pwDd2thmVfHks7DI0RHsqyE6uRJyTmxUjvWbfEWNDGqyng1n2v3suIDJN62sDOF5JdLsgmiJJSNXEKPP8ULCpMtxtOkEJlQug0dSwG2EM8Vf-45CeYaCD2SDrK3Ky9CTSuxJ44ELz0_djyy08qKa8K95GvZ7P8yv1Vmy1_xk7cZtOWi8jXXQqdcm_7YYQ3O36j5xMXX3drVN1WcevWCcNvLqwkYVrgVGvnFETW7D7fYziBODSA4ylztTVoGXd3aRnHaLvwp_UOfO10g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7GHsLaOZHSI59C1uXcj2in2AcKJPgUhfUSs9Ntdc8v8__5DQdc5a2iIGZ72fNaW2pB2wyJGx5pcBlV0EEybijr0Mgaah__o8h8qW43ydzy6HlbKwX79O4IBSq_-4hoULoV3T2J-_29Z1sB3FTlEQTXbp40Qwe48Hw19COSg2RkzeqaLXowh7S5NK4rbFd3FAsVVeSNuDMG3pd71vwsriuR6XKknvG1eMEP-5PY2YLRFufFpc_AQWCxJ6udvjhv0Qt57oILp5BAoPuFMV2Z4fhUIxi-tVyhLtEnOqBVewTMLXOqJjPV5NCjve6y05IDKNO6y1LMcZp0uT5qU-Kz6IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A7cABHRpABuLAgJzwJI_QyqWe-YnBTdw_hVmntegLw-ouZ8AjM7mRcKjVvR-cbBqmW0kLmMFWBGPKZCmjjL3jKGfvTfXAOBZXWkCnR0IVMdUquGCmg_vvWB5YPTD9pic18htfMIKBoCg-BtnpzXQVVW59dOnrptVd6z0Fz2JRMme46HKZfvbEZAwFFzkn8qH4EWlULcZYhBK7SQ5vJdulGm1wl3VMKuQrWLw-bHfHA47iQpWux1XnX3FbI3mYdxNNPSGe7_-UmfiYWi5W-ieyCYFGJ4FGm3f5vB45j63hVTCIzkVTkk6JeQdouzl61lIyOg2o9VvPQ0T6pFlOeoWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ez_OzutT6TGe6fX-7lj6v2sFCzBmhG_o9g2qaDCLOrPe0EG6XIi2Z9vO6ox4FQXFO-FZV2YX2DiZspMoStOP_NumGgKcYytEylO6NHcpcYCP_zWO3468ZqoQK0YoP2y9yXMUegEUeUPWlK1mtPwDoLtIvh9hwVUsdpxlBX9rmJS-AxmEC6m0JgME0Wi7Dpk4KC6PyJWCe2PMJrVmAX0ftcc_5YpZsIiS-c-AOkoCDnl8FXRSNCSIqk0pJT3fcMzuJ8X-NVRdkjctCpbjE2LFjXAPa7qMPBR5Nup9wQ0VDOtyyXAteUeRF_K84GRkawsn1dS49qyPVlOCJ7QFfsiQcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FK1jAXZrIYPvCdXmc0jN4btMT0JGc8OLNMpwzQXob-4i0odMYqSpEJuRNtQE35Us_3CzPHWodxMGar-PRdHO7zN_BTbE6ebR45VT8Zw2KvctqmDDdJPWTvy873eoJHz-om-zfLLGHO-QfPU3rENA2P7RuUtH6i-vudL76MDzoAJjQCNLAzsZenCPPVUDt3pxI4xrZ8oAV_BGMKhFk2_9unDAVV2I-P00FLR0Abq14Xy6DlLLsmbAPHTM2L1s-rKRVKelBn2ZTz2sZougHg8b6xeOYZ__Q7EkaXPnUioRHSv9cF6YO7W6gCpoga4Jr1cyXHLZnlFJ2twWLMTBfABOYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RBVPWJ3XWvBeqCME3X2PNGy3tZwFFG_bNI74ETZ9s1vaT_2D3jkOD9U7P5ymWWSByVanXEi7O7ejcydFa59p7frTCDKrSvSDD3Dmo8N2EIZoPRiXK4GFVAtreBXwAthWfL_Ns4GnfKkFbavAeTifXJwv_Cg-X0YnNWnkQFLF2xbkD7p6egflXWLh0x5sWWvMimrkz99OfIWe595XW4xabLjWSUs-3a90_29WeAyBBCaEgtiGpa-HPNNdyBjWKsyKEquNsbdh-hTd7xBDPRLtrqK-TI5SmkmOfL-n13L_ZD9vxfOZxwqlPcxlnIjvmdyCc56eitJKMSog786fuWrAQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آموزش سلاح در میدان انقلاب زنجان
عکس:
عرفان تقی‌بیگ‌لو
@Farsna</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/farsna/437946" target="_blank">📅 18:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437945">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyrAIYI_mW_5Gm9_rgllb-uzwVkobm1WOv8DK4jKDhVXHOzwu9KOf_KMKOJyWgD94Jew3tOmjsSdVgOuw-o7VloDuqyU0fH_etEnfX_WFVPHVcCI9bfcrZnJlV2MT94EK2St5PxTwxdfsTRfUL2_fkK9xbBmManTwj9uqMBiOX79JoeZr0VXo8v7BXFgP2HkKevR56z4Pfoo2JfUqTiLuLyJEeNVPQcT9tZ80maJ6GwtaQGHYtTYPRh33WK-gFirw2CcZkGB02pr7yqejvbEjOkhQHICiaDiP8lJhaulu420Q3nC8PnnVRg-vj2cWBBuUVstLJR0ZgIVfCPcyrMVfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل: اختلاف نتانیاهو با ترامپ عملیات فریب است
🔹
طبق گفته یک تحلیلگر ارشد امنیتی اسرائیل، گزارش‌های درز کرده درباره تماس‌های تلفنی پرتنش میان ترامپ و نتانیاهو بر سر ایران واقعی نبودند، بلکه بخشی از یک راهبرد حساب‌شده برای گمراه‌کردن تهران بودند.
🔹
بر اساس گزارش کانال ۱۴ اسرائیل، این جنجال با گزارشی از پایگاه خبری آکسیوس آغاز شد که مدعی بود یک تماس تلفنی به‌ ویژه دشوار میان ترامپ و نتانیاهو درباره یک پیشنهاد جدید آمریکایی که از طریق پاکستان برای ایران ارسال شده، صورت گرفته است.
🔹
کوبی مایکل، پژوهشگر ارشد در مؤسسه مطالعات امنیت داخلی (INSS) و مؤسسه میسگاو، توضیح می‌دهد که این یک فریب تاکتیکی درخشان بوده است: «نه رئیس‌جمهور ترامپ و نه نخست‌وزیر نتانیاهو هیچ علاقه‌ای به یک بحران واقعی ندارند. با درز داستان درباره یک بحران جدی ادعایی میان آن‌ها، ایرانی‌ها ممکن است از زمان‌بندی حمله نظامی بعدی کاملاً غافلگیر شوند.»
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/farsna/437945" target="_blank">📅 18:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437936">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gloRDUOILAehJkrrIna39LbfXikViK72AGlvaT49rbsXkFh02v7u5HXtu0W72Z-0oEhJkgAGF9BynTP1nWY-IKJi6xPe50QitAUl-SeBiCbCy0RMSbbed9XQXh1b8R--JxVCWnqNAHNc9g9uxIkmQR6A36PYL6QX7p2bYdTXVejUBeqKG7H_Fj16vd9C3o2y8aGf2zlxPcTD7krCqW-J8GZ8V4zPilUawUBVAOtEG3W_ALuMcKRQf2OXKkUCHwA51mUfIwmPNHZnDS21cAEg65NzpIkkrObO44LvGFrY-AJKeFfSowREmvFP3JA4J1Lm1HCQlC1bc-DX653hKttZog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جلسهٔ ستاد ویژهٔ ساماندهی فضای مجازی به ریاست معاون اول رئیس‌جمهور، موضوعات مهمی در خصوص برقراری اینترنت بین‌الملل مصوب شد که پس از تایید نهایی رئیس‌جمهور، برای اجرا به وزارت ارتباطات ابلاغ می‌شود
🔸
یک منبع به خبرنگاه سیاسی فارس گفت: در این جلسه برقراری…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/farsna/437936" target="_blank">📅 18:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437935">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sumhSwu5JZlIIHZiFDQvAFm8ZaYDHVI6LuH2f1ih529Sstvn2gq3Mzz1JLzR1LBb6_yXDLfDWFcyDzFeuZj-ry6a3KVTgW39mzI00swQkDatB9zbT-BCIXbLSQuUZuTLmogSjaXnR26a0NwqyErjR6jLPxtozXK9b_zu4UuHhGTpn0XeP26stFCgEnz9KG4befKvxzDiMF4TujsXHI4UG0b460IiB2xpX6E5_24ynOlPjl43ZjJpgyaaGi8bHHbZ31B2f1EYNDx71xyTBXaTgc47En3-n0rmLyFwXdLkhG9MUWfc-kB6_aSmGdoDUu2jBCyc54viyW_DE5l7u8KT8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت‌های جدید لبنیات اعلام شد
دبیر انجمن صنایع لبنی از افزایش قیمت ۴ قلم پرمصرف لبنی خبر داد:
🔸
شیر نایلونی: ۸۴ هزار تومان
🔸
شیر بطری: ۹۸ هزار تومان
🔸
پنیر یواف ۴۰۰ گرمی: ۲۰۳ هزار تومان
🔸
ماست دبه‌ای ۲ کیلویی: ۲۲۸ هزار و ۷۰۰ تومان
🔹
هفتهٔ گذشته نیز قیمت شیر خام با افزایش ۲۹ درصدی به کیلویی ۶۰.۵۰۰ تومان رسید.
🔹
گفته‌شده انجمن صنایع لبنی و سازمان حمایت برای افزایش قیمت‌ها به‌صورت لفظی توافق کرده‌اند و هنوز ابلاغ رسمی صورت نگرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/437935" target="_blank">📅 18:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437934">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-46.pdf</div>
  <div class="tg-doc-extra">2.7 MB</div>
</div>
<a href="https://t.me/farsna/437934" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
دستِ پُر به میدان بروید
🔸
اگر برای اجتماعات انقلابی به‌دنبال شعر، شعار یا تک‌بیت‌های روز هستید، ویژه‌نامهٔ «خط» پاسخگوی نیاز شماست.
@Farsna</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/farsna/437934" target="_blank">📅 18:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437933">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سردار حسن‌زاده: امروز از روز نخست جنگ قدرتمندتریم
🔹
فرماندهٔ سپاه محمد رسول‌الله(ص) تهران بزرگ:  هرچه دشمنان جمهوری اسلامی، به‌ویژه آمریکا، شکست بیشتری متحمل می‌شوند، هیاهو و فضاسازی رسانه‌ای آن‌ها نیز بیشتر می‌شود.
🔹
خصلت استکبار این است که هر زمان در میدان دچار شکست می‌شود، با اظهارات گزاف و جنگ روانی تلاش می‌کند واقعیت‌ها را وارونه جلوه دهد.
🔹
خود آمریکایی‌ها نیز به‌خوبی می‌دانند که ایران امروز از روز نخست جنگ قدرتمندتر است و اگر بر مسیر تهدید و فشار اصرار کنند، بار دیگر طعم شکست و ضربات سنگین، مهلک و پشیمان‌کننده را خواهند چشید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farsna/437933" target="_blank">📅 17:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437932">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3fd2d26d4.mp4?token=TiFD4he56eL2CwqUHDyTatvTUnEk9kX1efXdv1-ngKbTbCK20CchUApxmvK8YFG_JbQVnyOCtccvgmTQ1pzbpZq-9CaaFSJOt-9D05sJip2i64J6r8F9wf64eaxxfPAUiQgmHR-Z8t0pjwaLeGicZHycfNneSq1nmFIUZ9H_B2rIX5M7oUEBimH7Y55CCwoOnaxkumR7fLLowftQnhLhKDE2Da5D8F9hY3GmW_kL2viq6zco9MF8gOz_KXAw71kDWSGrQqUVpY7b8mjbEoq27fz9_0epFdARp3sF58MR-VJhK7_JqXxhLipcFUjPApwTV0K7Z0F92_NXj-KMjKTGgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3fd2d26d4.mp4?token=TiFD4he56eL2CwqUHDyTatvTUnEk9kX1efXdv1-ngKbTbCK20CchUApxmvK8YFG_JbQVnyOCtccvgmTQ1pzbpZq-9CaaFSJOt-9D05sJip2i64J6r8F9wf64eaxxfPAUiQgmHR-Z8t0pjwaLeGicZHycfNneSq1nmFIUZ9H_B2rIX5M7oUEBimH7Y55CCwoOnaxkumR7fLLowftQnhLhKDE2Da5D8F9hY3GmW_kL2viq6zco9MF8gOz_KXAw71kDWSGrQqUVpY7b8mjbEoq27fz9_0epFdARp3sF58MR-VJhK7_JqXxhLipcFUjPApwTV0K7Z0F92_NXj-KMjKTGgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«مسلمیه» چگونه دروازۀ ورود به عزای سیدالشهدا شد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farsna/437932" target="_blank">📅 17:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437925">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oo2YlML50Q5ukUtczjrREvqBJV9-klyOGUXu9NUOyVT5-MuKiseyhRBjKyQbizNknbK7w9wCiHCY_W3mbAr_ZQitfiYK4MPpQnXiQlWfI26OJ_PzMvV2yUcQr9jl2rbar_G_0rAZZOAKav4jbI29-47JHTBxrlRCgvPGR5fN-FVr5xvS9trHLmjHJLmRpNEFpKslLJTmWITZgZe3WayyMkWy-UdberK6IQ3prhgRzAkYjyfS14Drogk-nfX9nWlQdYITMLsnAFBvskTUntUjetZFW0mDp7W7FkFz7MvqP4jkyK04AyixFRd3N8gG54N_K_tYD8dLGJkeUrIKa6-kIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HHxjUxNj_OMy6QBLjsOirtiyDrb_9EDA8PS4m_WqN8Jove6gAAA8T11hKAN2Qw_BQF8hfTLopRB1I1ZQcMHB-2pYXzCQ7qkK651J11dCoE_gT_qZsCLZ5n9vsUU4IduowKo8Ga2k7FBUzfIf8bNZvHCaO41vxxpFdNmg1_LYaybx22IM-ZywZhOOwsCrdFOMQTR5yFt8tqkLMEm5YOvwbV7uBtREzhyoKdVnAc845OTHXBx6BMYCpGM6SEnRwQq9a9UiGWNOTCn7Tz4x8NsJV3x_5UsP0V_snL_REAvtomnRzXdtZVU1zW3qtLo65Vg-0_uWKw_TH7wHAu76pG4Daw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehdOsc1zy7Obkt4b8OsSBpsYV9wpuqvx9FRT9eEAIGjShy0xt2Du7Hes9LLS2VUVzgRiAGHpevuQh6V9hU7tAiOe0gYnV5Isg3Q4yalDf_E6lVm0vvQDvJ8g87DWg9sHw3yQopJ8mGxZpzYhWiMbTPgUkGn2Blhja8PGBnz-qayFHvlJGPfCaIs1KLtEHu29yTWZ1OouZCFAY-v1qQtpOvGagxknK2Gif8EtWduCRYRP32iu91oumgZTfQrWQJN0X3iRXW3zILw011w5riuXoYYYnRaB2CUweVFb9RZZDau_VQeg0IQBE78ZYpnkI4U-K7dqkAOJup6BU1bh3ogq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oryAGoI51iLbbZWC-8kjnn0vXgBDZ7MtDvgfLViMZuqejtjtZFDER9njQEV-GIrP4TFNOAPSjaj8oKRliQZmgtF6v_GoKb6Ts6TohYWnx_piwurEHiEANvRMYXmaDFqacZaNetdXaD_L1yVitwdrMqQYgKkKQNAMlJFH45NyDST-OPNnw0DfEz-gfbieySckFWxz3Di6rJKR0ywAtqt-hjm6Si5OnStSFSmN4kEi6Mcta7gkPfwmmmGONDeDsugSgUvSG0Mu4vufhPbsqz7BPcRVYhQcTNKUqogjDABpxNjCCCZLeanTHsPDVvYVBBAkIoVrOGIWE-4CXRhzdUCq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vg9UIn_drPuobpW4PjynWDXVG78_I1digJ4k8WsyHaz7gzUtxV1VBIDU_spH9uCeHqfw4NBhz6ns6Diz7yisNEgzue6SPi4U0aOI-GQXkhYsBVtwTafRyDbVWofM8xvBOKIt42I_L1p2eRfqFyVVbNEKVLP0Dp9FalEaJV_15XRCHk2YVbVwC_VNL1mVi2fElo2eavcklx5FNWc_1none20XsuIFTGx0mVNizVeWRlwbmeRaXy9lT1hOAGQfFshaIbkgcLoywPb8tCU7D1bMAkHYd73V8h86-H79O_3fnEm8zhCVUSutXo3_xWwz4g-K9PGAngXsLk-ifb9NA3je7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aG-ZzH2tX29Q-lEbSs9OJJqd1V5a4JB0forH76fdDblK3z2PzSV5uhWRztURjb3LTuReGEi868P05N9sm8jPcyJh-4cQPQxe0zhhF7mRRu8ooEd4JKK9HDfmFuP8cIHKZFGrf1cHQfMNrlqnnGEwiGPPzIS4EJ8HF_3ydK2O6W-tPR_J8y-nYbPzeJWfzGEEgg2yaDsNRSqkGflLkupd1NUuEBDilW7RFxjLJC4W9qsX5B0FtmqAg744MLlI_KeDodftKJmmhZ2AWbg3HuuyFutT3mBW4qNlnFIci0yLvZZ6pPCkGr-s3bSDDbnuYvS959TQb3yOXBcgiYiVv-EzHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TrMiIqyWnq7FIt9BYrkXtVd4TKvZkfWb7vNQH1--uGsPKtBEOCplBgRrCpFZ2_W9ycZq0u4OOkaW59OZuvIIV-GqOhgjs41ICDhGj3D_yc0NkpQSNWk_IWoyuAai3euaycpIRD35W4086PDmeU80EV-fOOrqs9Npgfw75tZa77C-6QBkhiDMbR0Qe15vwqhQou2O7-LwMKp8yo6i9edyMWHUHfZDq1pEfFTdtR0dqm4Korirx0E1CPp8d0Q9OOYsT9BDx3cvHhONNhGbn_s7OHWbFU-vZn5pSwFF4VkO6Z9SXedMEOe1l9-Ji4zaFoy8tg-W0k-HyRWaQSqGQV5Q9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دریاچۀ شورابیل، قلب تپندۀ اردبیل
عکاس:
حسین حسین‌زاده
@Farsna</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/437925" target="_blank">📅 17:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437924">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تجمعات و تانک‌های رژیم صهیونی هدف حملات حزب‌الله شد
🔹
حزب‌الله: یک توپخانه و تجمع نظامیان صهیونیست در شهر العدیسه و ۲ تانک مرکاوا در شهر دبل را هدف قرار دادیم.
🔹
همچنین تجمعی از خودروها و سربازان ارتش دشمن اسرائیلی در شهر القوزح با حملهٔ موشکی هدف قرار گرفته شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/437924" target="_blank">📅 17:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437923">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c22b517759.mp4?token=Mw0ksSCqvrHCw5WdRuD-sTvAu8suPyXLrhPDTq24Hl4ipw_X4F606vmgzKoOWxpHAhw4k0vwsfVqK328C-rIZI1hsnIceJm0qWeQdDNzP9n8rEATRQPxzA3yr_rwBR8pa9nw5RR-i4CXXc3tY2bqseEDCjMIZWpHmZbNjgkJOZGF6gg7x50KXAGmO9JoD0F2HdaibtZySlN03yS2N4joEZCNWjkaW866Xzhvv7ge4QAW3x7QIaDykW_2_MLM3IVliibxr77eaDkLfI370AsD_Y2Rqkqtt8ptvn99MB2usxfLWwqcl6cgGIDVlPyMDsvcrvRapHRBv9w8mcYx66S7MJHL2vIdDC3Av7Khky2E3qZfJVP5LRWaTkb0RH_BpqZDsR2-cq4W5-uLMXZQgRxZcX5JS1Nps8a3EXyi7qc8aNAhBJZLHwo88Ts65DPuC_9R01PBcXxQRkFqio-dutVVRNZ92da1dAeByT-_LQRSn64_mad-cYA-LbH6D6JdrMme69mvhe77nxVA1xB_MqQr8EKPOPJeVhXb0ooLdrnuxPdaL-Y7GfrxbUZ_gX94JFOLla9-aaHc8np46LjCGTu4v1puQrBlPItss1VQ1UBrABEEpdNF12uAJqGHMzST9BP8qc1pIypGaKC0KeOD89kfMybx0rChyyD5eg9Dz_p_80g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c22b517759.mp4?token=Mw0ksSCqvrHCw5WdRuD-sTvAu8suPyXLrhPDTq24Hl4ipw_X4F606vmgzKoOWxpHAhw4k0vwsfVqK328C-rIZI1hsnIceJm0qWeQdDNzP9n8rEATRQPxzA3yr_rwBR8pa9nw5RR-i4CXXc3tY2bqseEDCjMIZWpHmZbNjgkJOZGF6gg7x50KXAGmO9JoD0F2HdaibtZySlN03yS2N4joEZCNWjkaW866Xzhvv7ge4QAW3x7QIaDykW_2_MLM3IVliibxr77eaDkLfI370AsD_Y2Rqkqtt8ptvn99MB2usxfLWwqcl6cgGIDVlPyMDsvcrvRapHRBv9w8mcYx66S7MJHL2vIdDC3Av7Khky2E3qZfJVP5LRWaTkb0RH_BpqZDsR2-cq4W5-uLMXZQgRxZcX5JS1Nps8a3EXyi7qc8aNAhBJZLHwo88Ts65DPuC_9R01PBcXxQRkFqio-dutVVRNZ92da1dAeByT-_LQRSn64_mad-cYA-LbH6D6JdrMme69mvhe77nxVA1xB_MqQr8EKPOPJeVhXb0ooLdrnuxPdaL-Y7GfrxbUZ_gX94JFOLla9-aaHc8np46LjCGTu4v1puQrBlPItss1VQ1UBrABEEpdNF12uAJqGHMzST9BP8qc1pIypGaKC0KeOD89kfMybx0rChyyD5eg9Dz_p_80g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرهٔ علیرضا پناهیان از هدیه‌ای که باعث ناراحتی رهبر شهید شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/437923" target="_blank">📅 17:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437922">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrqHSj3uNSvGljCMouKjIT9Mx7LSa_RM8JHV7760gx4QequWZzwsUyZ_iAUULibo61WmN4v6bKn7qKH5zRwCPkYn0hxkSHdI8KDA7cxCGl1VCzT_54F2fbdcmnrOEEAI7iW2R_rzeL3pEF91_HktybUICBg1A4A7yLGju8WwWDOikrny3jepTZlM4GU61LS2sTOBQFSLgu1xlH-_VJE47lVyKS6P30YVWD9LTrpTORvnCyx9FbW_xgu8lNaKehmovM0_W0MflOOc2SMa7Rm0yU8TU2X7iKLu77nCZnYxQv0GX_ycywMOH3zSwaQfyIVBh_Zq2KHh469TnGvmBe7-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
قیمت مرغ درحال کاهش است
🔹
براساس گزارش میدانی خبرنگار فارس، امروز قیمت مرغ در مناطق مختلف تهران از کیلویی ۳۹۰ هزار تا ۴۴۰ هزار تومان فروخته می‌شود.
🔹
پیش از این، قیمت مرغ در بازار به دلیل کاهش جوجه ریزی به ۴۸۰ هزار تومان رسیده بود.
🔹
یک مرغ‌فروش منطقهٔ بریانک تهران به خبرنگار فارس گفت: قیمت‌ها در چند روز گذشته هر روز حدود ۱۰ هزار تومان پایین آمده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/437922" target="_blank">📅 17:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437921">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAS2syj_Pz_dSkGcvu8TNp6HJmsJLB1irgC_OniCOGbVWndDvnU-N1bdtPmsGHnKCQqO3Z73cG-l2_STfbpI73A1mpwC3VWUeIkU0Xmn9hJEn6aiasmqV5_hz5aWHMIyQvo5DbfgQXbGyMQh6bJLq4-e3lB41KwTLUIkKLkWQdSJ0ZTqtlHKorP0WmPsZnY0k6AVefYwhsKeVgrwJMTBGTYbhhkKd1-BdOHPW8FoBKJnkO0BmqgmjOeSDMpB_aEjFHnVN1jThKnjQWWsE0nLQp1USlg_zbA7xTTakWyEKrXfbH2TMQJOUdao613E0pRQtsCKBkKmylIAnRlMiGcHag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: یا با ایران یک توافق عالی می‌کنیم یا توافق نمی‌کنیم
🔹
من به همهٔ احمق‌هایی که هنوز چیزی دربارهٔ توافق بالقوه‌ام با ایران نمی‌دانند و از آن انتقاد می‌کنند، می‌خندم.
🔹
این توافق دقیقاً نقطهٔ مقابل توافق فاجعه‌بار برجام است که توسط دولت شکست‌خوردهٔ اوباما…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/437921" target="_blank">📅 16:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437914">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nR6YIYWSpCt9b4gVMX5SEZr4TUOoNV3_f4feJprWWDfiAv775kUgXg-fh4SPx1epn2N-0QeIu6L2Qr3wYmT1NjldP8172V5DoICAbX_lZKdI-NEpBdmynHqUI5mqwgHyUsHmXBeY7fn32Wgoh-4KATXEhnxzWIp2BMwg4uK5jOmzow5xcDHjveueJYtVpkZ74IJZ4lbrt6432Cud-rHtv9aM_gqYkDAsef_vBBDS-XikbwSfF2mH91nvnP2u73W6Fz8V1324njFNghpB2bjiz9cWX6kagm1qk2nWOBLecY4aqGo64TA2wSHqP6E0FMID7m1WSrOjLVRVR8o7gTbkRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bqKDrUgztdwxEVwJaYfKXRIsyQ-PUmHhl-W-Mt06yfLdaRisLX6JYHI4NipuWPxCr04-yvyKLhfXhdzvzt8shC_YWnyYtAPdArOVtuTLb5Yeftlx-OC3a-eSBNXVofNv8I-1GTSTE1N5tUPjEHbv9nUajrjTMFGt28oK2s5cc2xj8zqzbLCLZw6UwaNUNlon8t_Y_jIxtRu5YpFiToEI9WPtmLFYFQAYmxd6O-VwhbG3Dx1GyXqGztG8aLUQDqgjHAt1gwKIUnDFnUMikEV3vDgFmxMzcJCmZFrqm8P1oDWCxkiGnbN6sALbs1hGAfqWXJ6BPwwffdHkWvFvwnXZfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rK-KzlTEsVlbtxjpBMz144xfR50K0Rg7ikF_olpSLrz1T385c551Ml0oHINaqCPS_apOGBdBEtVRl-ZTcfd268lOgWZV8j3hyn2gE2hAFU_h-t6o0mHWPgHWPGoO83JhlTgbAcVT8Z6TRGhWo2GQ972ScdJz5rkHbc6PnNBhCumpISdFZSzDnTDhr2UPaw-6Ts__2ySzusdKkEjTZ5u0dXL9kJJVaGGeDPjYzW5KrK9CoeVqTrItjo_7f4Hzuk9OnWX5YSCZA-1QY64TRvN05z2iC8C9yS1NTCO7rc4ZuD6DCAcIf-IFQxLf3pDdduHjhtrs9umSFX2QCxRI0jEfFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jc1IAUWUzo-flc6SgaU1lWZ872KJhBvEWPCQINJtsjJRF8-VebLgyVzku0hJ5RfXJQ7VM0U68r2RrzQSwhwc3XsWzT4urbez09cFydZMDdIg3_nrbeJzozKDVlop086BgQ3NcBspXI3I1DCpEnXMJi9mjjXDkTVn9JINGPY8lRfWPRdUm2k5PnN3j_P1uK2iXmMzpdC_-OYBOBOksij9vzI-_hO8Wu1ktw55syVuUg6h3mwzBYbaZDgipIi-a0b9EFoM8KcgRH1qiYLMr35NfSuF2qcWv7z4504VkrWit317TGc4avzDeoF0RRLXjpDsVecBkxWP7L7VXwJj3Vxd0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WlbH0offhMuf4UclsoXZeLbOy7MIm2p9acLCmYmpaxTasO6lVMg_1hK1pyy0-Lze2hW4je1n3w0xgB6itqEunnQ4PiEN1W77vD7XwJPvxWCWCGd7fmazcKQdgmoM81bz_UI4TkP0Bj33C3Gu0PoNQHIpmX0DI6yQ4R56TVN9lmAx7cs-q2x69I_82VEjrA3N2CMG0Rn51whCaHnaU6xVAcsBAAL_GNox5nv7GApVDksxEVFIFc8i8bCTOne8QuosOMee4qZXgJ_5HWKf-653zxMphfkROyenswDVbPt7hGS7UC5rZBw_lHr8OIyF-0OuzmZyg8CqQad0bnz6Ez_a-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVl_qRJw2M14sZrhuoOPW5aNVbi1B7mazB1CqMGE46Y2u22kBlJPDmNzLalr5UgL_5XFofbP-r9oB8MDmdHKZb-pnGwFMTpr-rEF9DNDbvHPcVWWBuqNyxPqwMBqYOKoxsqyB6VcIxEGDtAj9mkBUmN5l2GuYbQU_ZypUbgNMO5TBbChE4jhb9jJB2MiTH1LuryHwU1FcHyVnAVa0-0KenC3z9EEdzBlZSbwwkpNSSUyls01r8uaZBzEg-yn5yJXSEU4jOH-jgNMVcPZ6Ybsmqzjv2QsxNWmALTLBhs-iNvAHoTW-kBAqZi_UKg4jk_EqKSiyEQ_-7dzQppDuMqUuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ با آغاز انتخابات هیئت‌رئیسۀ مجلس، قالیباف در محل رای‌گیری حاضر شد و اولین نماینده‌ای بود که رای داد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/437914" target="_blank">📅 16:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437913">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4egP_wNOawQ67BSos_ieiwncFZ2TgIkLN9DScq-_Jg-1BuFmdsg6xsTVCFhLLCEhIQ0SFVk8XDRRywI_FAGAtCL-JwaFO1IqUX3zTxw_VVS_ukDZzAlPCnka28IMpR--U9WEMX4okbkY76K83CyRAPSA6anjQSQil6iMArEvwdy81VsLkxYSn5OTis8C0PYAUVrkhoUkRdD5a8dZtpCaSv7kifZNzIWCvLP79YOB7LNi1opUYioYrE6NdV9ngp4jqj-MUG_XfwzrXa4xSBYEGwFBeyYINbnFq6qXLbXE6XPBEL_GsxHEr6u-0AkFzUbyup25U751OgZl3bNZzL3aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تابستان داغ در جایگاه‌های سوخت آمریکا
🔹
گزبادی، تارنمای آنلاین قیمت سوخت در آمریکا پیش‌بینی کرده امسال آمریکایی‌ها گران‌ترین قیمت تابستانه بنزین در سال‌های اخیر را تجربه خواهند کرد.
🔹
رئیس این تارنما می‌گوید به‌خاطر بسته‌ماندن تنگه هرمز، میانگین قیمت بنزین…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/437913" target="_blank">📅 16:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437912">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پهپاد متخاصم با «آرش‌های کمانگیر» شکار شد
🔹
در ساعات گذشته، فضای خلیج فارس شاهد نمایش اقتدار دفاعی جمهوری اسلامی ایران بود؛ جایی که رزمندگان ایرانی با رونمایی از آرش‌های کمانگیر با سامانه‌های جدید، یک پهپاد متخاصم را بر فراز آب‌های استراتژیک خلیج فارس با موفقیت سرنگون کردند.
🔹
این عملیات که با به‌کارگیری سامانه‌ای با قابلیت‌های پنهان انجام شد، پیامی روشن و قاطع از سوی ایران به شمار می‌رود. مقامات مربوطه تصریح کرده‌اند که «این نشانه از طرف ماست تا دیگر هیچ پهپاد رادارگریزی نتواند بر آسمان خلیج فارس نفوذ کند.»
🔹
این اقدام، تأکید دوباره‌ای بر حاکمیت و امنیت کامل ایران بر حریم هوایی خلیج فارس و آمادگی نیروهای دفاعی برای مقابله با هرگونه تجاوز است؛جزئیات فنی و عملیاتی این سامانه جدید تاکنون محرمانه باقی مانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/437912" target="_blank">📅 16:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437911">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a8f1d68e.mp4?token=sr-eQkrcgGe7fMpoqXLnANnNP0llFe-I3yNkn4aTnz6ern3JXDxsJxTuFyWFNDRbzm7CwZu_GpoR6ujNFWvHFuBUtWs05sNIMkA-E8TiygFdf5M9RSDJdGU1egDOvKlUXnmosIUKwOz0kMRKWtQSGYLLX0OZ6W1-LmKsTxF4rH9do7FnC1DUFuo__W92Ex8FPHCHmm0kF46AI3-J3nYQAVOHS0dOVh-EMUTi1YfQUMQ09S2eDbYCDYZc34JXG-5k0wZkLuhGrdU9oNh0xAh3VyFbZTpV5Zt8QJWIoZxfsBxKnllahJlH7NSJGGEX9wPenwIuwYcEqN1ukaV-GDsaaQd7hvhkf4NZdc5hTDZ46BoOYGhOHZCo43ThxvAY9oJfQoy96CS6ESbePT_uwxtEh8iy_eqChAIW3Jdhv8zd7iypxNx3ZAyq7sPj8MAdqRotijCSqjIPBj4POgO_JDWw_DLEkF3_RE8cOgj9i3CiJnT-3vcxGfIzDVXe3qAOtaI3CGUkQ9QjsIFldZwjPRAygQy2iHA7-xmJfPcMUc1ciOrai6O6_tEBrIyaHsE9fDNcLnXRe7Gcrd6AJMVKmbdgeyYBQUaU4Oh8Bnrn7zLUVMIBtQtOHsBdhMy0JdT-RxvNWw8-UyN-PPgCuTrgyFltJ-3kHha4cXnQaATK5GqImb8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a8f1d68e.mp4?token=sr-eQkrcgGe7fMpoqXLnANnNP0llFe-I3yNkn4aTnz6ern3JXDxsJxTuFyWFNDRbzm7CwZu_GpoR6ujNFWvHFuBUtWs05sNIMkA-E8TiygFdf5M9RSDJdGU1egDOvKlUXnmosIUKwOz0kMRKWtQSGYLLX0OZ6W1-LmKsTxF4rH9do7FnC1DUFuo__W92Ex8FPHCHmm0kF46AI3-J3nYQAVOHS0dOVh-EMUTi1YfQUMQ09S2eDbYCDYZc34JXG-5k0wZkLuhGrdU9oNh0xAh3VyFbZTpV5Zt8QJWIoZxfsBxKnllahJlH7NSJGGEX9wPenwIuwYcEqN1ukaV-GDsaaQd7hvhkf4NZdc5hTDZ46BoOYGhOHZCo43ThxvAY9oJfQoy96CS6ESbePT_uwxtEh8iy_eqChAIW3Jdhv8zd7iypxNx3ZAyq7sPj8MAdqRotijCSqjIPBj4POgO_JDWw_DLEkF3_RE8cOgj9i3CiJnT-3vcxGfIzDVXe3qAOtaI3CGUkQ9QjsIFldZwjPRAygQy2iHA7-xmJfPcMUc1ciOrai6O6_tEBrIyaHsE9fDNcLnXRe7Gcrd6AJMVKmbdgeyYBQUaU4Oh8Bnrn7zLUVMIBtQtOHsBdhMy0JdT-RxvNWw8-UyN-PPgCuTrgyFltJ-3kHha4cXnQaATK5GqImb8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باقری، دبیرکل حزب عهد ایران: قطعا نمی‌شود به آمریکا اعتماد کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/437911" target="_blank">📅 16:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437910">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p81TYYaCSaiaah1fAjBhnj3XcFeYUuoiCIAdplweNrCgeDORZ7ONTcm3-Ohd4eemHk7aJFflqcN9khp_eFk4EAFwTA3y3lLWSmUsQp1MtmFtXQkNzCDkDn-dgA6F4sx_qiOHZyWE4vRjA1q9uweZ6mHHTwJ787BHI_CwRlmX-v50adXz-ZtSXAcMSG1I4kapcvyU8ZJnwoa_qtTCdrUBvRU3B0j_QxA7ca2laJlAf88NBbkJ6_pG2BRHaKozmYI7I3bWZVE4B-6G_aSHfh5EGG9Mv4u-zR2RknmeDOAFxVSBx4S-sY5IcmJzV09Egq05EPTetwYnUV-42GOQtGKqBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی‌برداری مصر از پهپاد ایرانی شاهد-۱۳۶
🔹
ارتش مصر از پهپاد انتحاری «جبار ۱۵۰» رونمایی کرده؛ پهپادی که به‌گفته منابع نظامی، به‌شدت از طراحی شاهد-۱۳۶ الهام گرفته است.
🔹
مصر تنها کشور کپی‌بردار نیست. تا اواخر ۲۰۲۵ دست‌کم ۶ کشور نسخه‌های مشابه ساخته‌اند یا درحال…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/437910" target="_blank">📅 16:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437909">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVRbVH7xiUQHY1FiddmHA821ukyzyWtDF9IR4OrAuN5kHEHtXSDHRObkGK09OSpgJ1RA6DzKsiMKWN11hSJYKB35UYDX-JcBXBjmiufG0upMurk-xcikZ9g-teEqHTmdQ9BPIvZi2b32HGdLsrTyr-ayWPAePaxVg9jpfVnwfl3C0QnFK_SBs8ja1EscohYUPMSuTXooovVqosY20CydNHSLKC5ggB-UQCk-7f4-sOOxrJizBJf4Tkxvc3kZq6nVjzzlQyWvlu2ocZ08fxa_1nYcZVHqVaVflHeYv_K4D4D9HWa0tP8B05A2oBStB5D8Uvbs69cGH_VW6eugi3__Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسب اجازۀ مجلس از رهبر انقلاب برای رأی‌گیری وبیناری
🔹
سلیمی، عضو هیئت‌رئیسۀ مجلس: با توجه به شرایط جدید، از رهبری اجازه خواستیم تا جلسات مجلس را وبیناری با امکان رأی‌گیری برگزار کنیم؛ زیرا در قوانین فعلی محدودیت‌هایی برای تشکیل جلسات وجود دارد.
🔹
به محض دریافت پاسخ درخواست، هیئت‌رئیسه تصمیمات لازم را برای آغاز جدی فعالیت‌های عادی مجلس خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/437909" target="_blank">📅 16:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437908">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfbde40c65.mp4?token=mBcES5its2mWtBvJiqvlB-DrWeWNVedfxNrCIoAIEBOGimf2L6YD7e6kvj_PBPVpGC8xKCp9IvfdRKQUWr7z4J_rKwpPt-Bhb-N6bblkvz7XymwlS0O5Mz5sBzCf8ZM8nYagrjgyvu-EbdxQYhMs-FLhRfReolsGKj8_WKwmE5wQLl-AONa9YolLaoZ4F_VdTxOvEI3Xp7sC_qd7kGZwcqqfhyoeZEcxi04wYobod022AKFHbznd8r94UsZYUdfPYk0LZ3TFmC2hw5ws3XpmJgzDz_e1m-9Sf2QwOa3bSFwQtxfKSk1ElqZ69wNoNQaw5wGJuOJ30WKtJx9J0eTCu7ZttCph4GeXD2RCd0R4eCHZM-YhoxgqZP0lOTYekFcQk9rdmHjqw4WXwpcaFnqxlLM7Jzx1ip81mjXcpXpcZTfkbej18j7mMcVuOxyyX1lSkXcU0lJow3IrBbCvXJduvLDe1efKODSrQq8GUQx5LrNes4c1sxtIYA7KZSQWcWri9k2aLaFuSxmhayOWtLp9LC-PF-jv-dXA2luz6G2BtJpxacSuPPatyH5WF6hwlqy4z00iG56_HS-KtMYt81vmnv2QTA9_4KCbjlWlRheovWZl-QjND6WCfyVEAWP_sXfxf4rAviMiuHmTpIeQz0pMwcNgsLmdLIwq_-F-n0Sg_P0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfbde40c65.mp4?token=mBcES5its2mWtBvJiqvlB-DrWeWNVedfxNrCIoAIEBOGimf2L6YD7e6kvj_PBPVpGC8xKCp9IvfdRKQUWr7z4J_rKwpPt-Bhb-N6bblkvz7XymwlS0O5Mz5sBzCf8ZM8nYagrjgyvu-EbdxQYhMs-FLhRfReolsGKj8_WKwmE5wQLl-AONa9YolLaoZ4F_VdTxOvEI3Xp7sC_qd7kGZwcqqfhyoeZEcxi04wYobod022AKFHbznd8r94UsZYUdfPYk0LZ3TFmC2hw5ws3XpmJgzDz_e1m-9Sf2QwOa3bSFwQtxfKSk1ElqZ69wNoNQaw5wGJuOJ30WKtJx9J0eTCu7ZttCph4GeXD2RCd0R4eCHZM-YhoxgqZP0lOTYekFcQk9rdmHjqw4WXwpcaFnqxlLM7Jzx1ip81mjXcpXpcZTfkbej18j7mMcVuOxyyX1lSkXcU0lJow3IrBbCvXJduvLDe1efKODSrQq8GUQx5LrNes4c1sxtIYA7KZSQWcWri9k2aLaFuSxmhayOWtLp9LC-PF-jv-dXA2luz6G2BtJpxacSuPPatyH5WF6hwlqy4z00iG56_HS-KtMYt81vmnv2QTA9_4KCbjlWlRheovWZl-QjND6WCfyVEAWP_sXfxf4rAviMiuHmTpIeQz0pMwcNgsLmdLIwq_-F-n0Sg_P0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگو با رانندۀ نیسان معروف جنگ رمضان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/437908" target="_blank">📅 15:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437907">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2f6c61094.mp4?token=pZ2duBBDHXTRa5_hZLG0OlOwAMyS61Awzu_fhbH4gBTnXvd0xPOGgYfGvX2ZGXrn3JpDOKfDhT4uOMhD0VCnodyCnBNK6FavNWrbJhJdDmKqQkoydv-teolRXcf2cpjIbg0elP-m178apFZo74bG091G3Cs-xHPi0WhyC0mSJpNniPVRbMsVEvW7_GHaGgmAj-9FzOCCXLlMQ_i0M6je-ezflkbQ3iHRQ2UVwsy6JyHEwpvD57YP9mne8IRSbCCdjjDz3dGpQuT1bBTaj1q0TwG4xihJAdNlka4fFCrODRGzekLjC0XXb1rNzR_S4y442uNTqdzlPryZpcGIbjx0Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2f6c61094.mp4?token=pZ2duBBDHXTRa5_hZLG0OlOwAMyS61Awzu_fhbH4gBTnXvd0xPOGgYfGvX2ZGXrn3JpDOKfDhT4uOMhD0VCnodyCnBNK6FavNWrbJhJdDmKqQkoydv-teolRXcf2cpjIbg0elP-m178apFZo74bG091G3Cs-xHPi0WhyC0mSJpNniPVRbMsVEvW7_GHaGgmAj-9FzOCCXLlMQ_i0M6je-ezflkbQ3iHRQ2UVwsy6JyHEwpvD57YP9mne8IRSbCCdjjDz3dGpQuT1bBTaj1q0TwG4xihJAdNlka4fFCrODRGzekLjC0XXb1rNzR_S4y442uNTqdzlPryZpcGIbjx0Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شمس‌الواعظین: طبق اطلاعات من در مورد آزادی اموال بلوکه‌شدۀ ایران اختلاف وجود دارد
🔹
عضو شورای اطلاع‌رسانی دولت: اختلاف در مورد رقم و زمان آزادی اموال بلوکه‌شده است. اگر این اختلاف حل شود یا امشب یا فردا شب شاهد یک تحول امیدوارکننده خواهیم بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/437907" target="_blank">📅 15:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437905">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‌ رویترز: قالیباف و عراقچی در دوحه هستند
🔹
خبرگزاری رویترز به‌نقل از یک مقام رسمی ناشناس مدعی شده که محمدباقر قالیباف و عباس عراقچی برای دیدار با نخست‌وزیر قطر دربارۀ توافق احتمالی ایران و آمریکا به دوحه سفر کرده‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/437905" target="_blank">📅 15:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437903">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رئیس بانک مرکزی به قطر رفت
🔹
عبدالناصر همتی پیرامون بررسی آزادسازی اموال بلوکه‌شده و در راستای کمیسیون اقتصادی مذاکرات به قطر سفر کرد.
🔸
هیئت قطری هفتۀ گذشته دربارۀ میانجی‌گری مذاکرات ایران و آمریکا به ایران سفر کرده بود. @Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/437903" target="_blank">📅 15:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437902">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwSf4CBBo0G3GPrBkvFUu2OIKBzv7mFFfdpzaw4T2X40lKj0GESK9kwPaV8-8Y1AtDHDfsJVNjt3X9bfKXCI5ZbDvXwm6xEO-ZwvuAimV7Kp9NeirHDXjPo4d_FPBXoa7si4k9xEJzGOLqipcKi0qNh8TytRAOlLOn8dMcywcrgG8oipd7WqxR6WxbtX29BR6ODNxCbvfumbDRTzMHoobGB_O-ekMvvmVbGhBRwBaV5QlM88KRnVyvlF95XwU7AukGc2mxumlVtq7eh5Ttya9MAcyBbV_6kDnD5HA7smKkQD-1wrxU7ERjbaaB2CI3XjPGQxFFWEUkw1iqOxMSJV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حنظله: هویت افرادی که به ناوگان صمود حمله کردند را فاش می‌کنیم
🔹
گروه هکری حنظله: فردا هویت افرادی که به ناوگان جهانی صمود حمله کرده و علیه آن اقداماتی را انجام داده‌اند، افشا خواهد شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/437902" target="_blank">📅 15:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437901">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JW0tRyDJDDTFS7q5aeAHlBvXi1cspd8MirtOG8-XH3isO-6ljD_gEM2cfs9AR5h_pM08We0YeQW3JbyCX5xwz86SxljQ2oJds7okb9hfP-FNy8KYds39oFNkLRhyZzujITsP8qw8MofHteF_X1WE026fSaDqFKMZ0mok-FjHQBdll1kskpZIQ1CKerKLsZ1lRsiMJvGWSZfXT2XDxb_2N3NKRRV22jZWqqngbXHd547cS__DxV2u8QJvJXD2cYMzsKRUwf-hyFSQuwOgGF-6iei0uHiJ_87gEch11z6QBmpkM66AoJPoU0sxS3Bkk4Hca2AX-KSKH1HB7QSMerx9Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واردات انبه ممنوع شد
🔹
سازمان توسعۀ تجارت ایران ثبت سفارش واردات انبه را تا اطلاع ثانوی ممنوع کرد.
🔹
استان‌های هرمزگان، سیستان‌وبلوچستان از مناطق مهم کشت انبه در کشور به شمار می‌روند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/437901" target="_blank">📅 15:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437900">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgnru3JVRnOosWN_pFl3BIrWptX6pVkIHDfZ2zU_p-9E6uoXoyaikdfj6Yl1z6T0j9J1au9a_kn63uR2-TRrNOgL1iDwxZX1tH-rZblsFiEaj7aZNAc-e-wdK4BjfRXtLUAB1sjznpUnJHABwsV8spZBkIVjbV4OyvzXKn9v2c84EObjrp4uANcEwnCvomL-1Od9LGWwClYy5QyvDOdWkwrDgQZX9auIlD4aQiz_m38IfKwu-2pXqFQQvHBZXfnd33RJlq4822sbP-GE7jkAs35EMpdp5Wy14_0yjyyyGOOgWKr4VM61pSSO9UjPvBJEv-axoVpbGTrdlZcewrZ_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جلسهٔ ستاد ویژهٔ ساماندهی فضای مجازی به ریاست معاون اول رئیس‌جمهور، موضوعات مهمی در خصوص برقراری اینترنت بین‌الملل مصوب شد که پس از تایید نهایی رئیس‌جمهور، برای اجرا به وزارت ارتباطات ابلاغ می‌شود
🔸
یک منبع به خبرنگاه سیاسی فارس گفت: در این جلسه برقراری…</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/437900" target="_blank">📅 15:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437899">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d53ff24aa.mp4?token=agxPmjC6VmGlPVh_CBDkvN0QUXyP47QKhVcxeTwTV8Ur5NXaRIg-qr7WyNdcVfXrPc_plndMIwBsZUqhNlCTdEtjWAZRUiKy4jCJeY-qfY9i-LLGpNziRb2nW20FZVfxB5lARuGFGm8-ox6l20QOzK6u8XJWLHb8OiS7cZ8IkRhMb4VfJGw3grX6kVRovgbWm23HlRmHqY864wRboXCOvEgyS1LCzipVfcFGzNiM8hQv1Yu7ZKUHXJ9UziDm8t04LiaR6cHX-rXVugHJBEPwA9rETm5A77WH9Oyahyt1SGhI_aLHGDEqzvedjED-ECQMJkqP6keAujzYRqIJt1zWlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d53ff24aa.mp4?token=agxPmjC6VmGlPVh_CBDkvN0QUXyP47QKhVcxeTwTV8Ur5NXaRIg-qr7WyNdcVfXrPc_plndMIwBsZUqhNlCTdEtjWAZRUiKy4jCJeY-qfY9i-LLGpNziRb2nW20FZVfxB5lARuGFGm8-ox6l20QOzK6u8XJWLHb8OiS7cZ8IkRhMb4VfJGw3grX6kVRovgbWm23HlRmHqY864wRboXCOvEgyS1LCzipVfcFGzNiM8hQv1Yu7ZKUHXJ9UziDm8t04LiaR6cHX-rXVugHJBEPwA9rETm5A77WH9Oyahyt1SGhI_aLHGDEqzvedjED-ECQMJkqP6keAujzYRqIJt1zWlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ عبور ۳۳ کشتی در شبانه‌روز گذشته با مجوز سپاه
🔹
نیروی دریایی سپاه: در شبانه‌روز گذشته ۳۳ کشتی اعم از نفتکش، کانتینربر و سایر کشتی‌های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند. @Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/437899" target="_blank">📅 14:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437898">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e120ca66a3.mp4?token=U8I5tzDVX29AnCbiwVtBZEj6rmru55Qhzakpy8wXup5BvApkKHgiFLEk7NuJMwhPfbLlXoi1VzwRm9i_ucp7ZXuMQTFrt-pZiE9zZwGKEIieONZUYU724EdpAX5BLG3RKIji4YgnPY28g8tAkFB0uALmc7-Mdtz5aPy024Vjzqbl3wh5s0rZd404SL-mtZD6Gp9d2o667z0WVM9e3J9P39bQ9nxB-XZ2a2_2XhQ8jNaVyisL8JE-YAQm27sz1zcLcQKLiwnst9XNQRHe27uyEBIJiUr3KhxvvDq8RobsiWl4K7VvcUs-IaTYyi8FisOq0SVPF-mmAVtlwe9pI-x-5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e120ca66a3.mp4?token=U8I5tzDVX29AnCbiwVtBZEj6rmru55Qhzakpy8wXup5BvApkKHgiFLEk7NuJMwhPfbLlXoi1VzwRm9i_ucp7ZXuMQTFrt-pZiE9zZwGKEIieONZUYU724EdpAX5BLG3RKIji4YgnPY28g8tAkFB0uALmc7-Mdtz5aPy024Vjzqbl3wh5s0rZd404SL-mtZD6Gp9d2o667z0WVM9e3J9P39bQ9nxB-XZ2a2_2XhQ8jNaVyisL8JE-YAQm27sz1zcLcQKLiwnst9XNQRHe27uyEBIJiUr3KhxvvDq8RobsiWl4K7VvcUs-IaTYyi8FisOq0SVPF-mmAVtlwe9pI-x-5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس بانک مرکزی به قطر رفت
🔹
عبدالناصر همتی پیرامون بررسی آزادسازی اموال بلوکه‌شده و در راستای کمیسیون اقتصادی مذاکرات به قطر سفر کرد.
🔸
هیئت قطری هفتۀ گذشته دربارۀ میانجی‌گری مذاکرات ایران و آمریکا به ایران سفر کرده بود. @Farsna</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/437898" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437897">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyP7HqvNAHJ_o42mOf0TFYK2ANCttrgtYg1YtmmlkhAUp_EAiVOlBPrS4zq1EG2ZIDTc8h2h55Y0aiaGT5usK98hnwvEtPYHeAPpInm2s_9zxgpxTizCZuEPFxNlWU0cDFvlImIx8XS4PpxaLLyFO3tkzF6JsD2MEkXG5E_xKhjArqympLwT-rTyk1Ku-ZBIdW0RVPGuQYOca6xkAKVFatcafc1JQHWTI84CB3QnD0YAAMqGIWE_ZZL_dbyWKfnps9hshcElxdp3HMrp7w6cQMmoZPTHh_lx-nVeUQ3KBKCBIJGiSI-ptz40JvaGUr74roMIfOzSd0cT2hUS6kwimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: یا با ایران یک توافق عالی می‌کنیم یا توافق نمی‌کنیم
🔹
من به همهٔ احمق‌هایی که هنوز چیزی دربارهٔ توافق بالقوه‌ام با ایران نمی‌دانند و از آن انتقاد می‌کنند، می‌خندم.
🔹
این توافق دقیقاً نقطهٔ مقابل توافق فاجعه‌بار برجام است که توسط دولت شکست‌خوردهٔ اوباما انجام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/437897" target="_blank">📅 14:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437896">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRP-NRzeCXNFQRDcTdwnNaaIoVv2S7VRcLMZI2L5fGNZ5i-ZsQyaw2jCPoyvFDAbg7H9R371GLNPBiChcB08SzWVqzj__ZNRP9cfClsCsdEB5ikIMp9vSx2fZVY2d8EaieflxJHpYFPWiR4YNZVFNEqE493RPNbrJq0gv2kAfkdUybjsthKLlE8PE16mbbVwera1X5TGFVbz1nKqAtWaKPdjBs3A6WChBU_E9NkGr05VKwE49lqjWPWUD3AkG8WeGK4lDAGvakC0Zf9EQzqqrjB-pfdQB7ZB84b332dLoeFWruAjdSzgp04k7jRP5BO8yig4X5DSAoLkxsw3LmJExA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بانک مرکزی به قطر رفت
🔹
عبدالناصر همتی پیرامون بررسی آزادسازی اموال بلوکه‌شده و در راستای کمیسیون اقتصادی مذاکرات به قطر سفر کرد.
🔸
هیئت قطری هفتۀ گذشته دربارۀ میانجی‌گری مذاکرات ایران و آمریکا به ایران سفر کرده بود.
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/437896" target="_blank">📅 14:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437895">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868d082d3a.mp4?token=AZnukhuWA_5E2EVsnBm29V8LG3XPGOskl7o-RCJfsDxGISC8SA-sKoSzY5EGKUGUDpPFuSB1XmsV3ijIi-mt91CCCy3yDsb0UiNQQpYV3uCpbrG__Ae1UjX6XOuDvBbVOwgA0I3Y7jYW5kxkkayFhVI9KNiG6ePKnuHuuYRCPQolVnrhNcIulBu6HHn_enFQNKg0viO7ezhHVmIqPRTRa_oxe1KhTGhs21V-wNcZoLbbT3BgH94l9ixkAa42_dj4Jg6SjQWBZDrZXM9XpbeLsuKywtDD0a6HqqgMcryKM1pDfWhzmMQC2QSxF3L8Nt0SFpSRVZq_SEWGIqumq9eFSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868d082d3a.mp4?token=AZnukhuWA_5E2EVsnBm29V8LG3XPGOskl7o-RCJfsDxGISC8SA-sKoSzY5EGKUGUDpPFuSB1XmsV3ijIi-mt91CCCy3yDsb0UiNQQpYV3uCpbrG__Ae1UjX6XOuDvBbVOwgA0I3Y7jYW5kxkkayFhVI9KNiG6ePKnuHuuYRCPQolVnrhNcIulBu6HHn_enFQNKg0viO7ezhHVmIqPRTRa_oxe1KhTGhs21V-wNcZoLbbT3BgH94l9ixkAa42_dj4Jg6SjQWBZDrZXM9XpbeLsuKywtDD0a6HqqgMcryKM1pDfWhzmMQC2QSxF3L8Nt0SFpSRVZq_SEWGIqumq9eFSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ دبیران هیئت‌رئیسۀ مجلس مشخص شدند
🔹
محمد رشیدی: ۱۶۹ رای
🔹
روح‌الله متفکرآزاد: ۱۳۸ رای
🔹
فرشاد ابراهیم‌پور:  ۱۱۳ رأی
🔹
مجتبی بخشی‌پور: با ۱۱۰ رای
🔹
احمد نادری: ۱۰۹ رای
🔹
سمیه رفیعی: ۱۰۵ رای @Farsna - Link</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/437895" target="_blank">📅 14:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437888">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oa0hbMoPqcxf4GwReI3Ov9rkq8jCQbABppEhUGnjH3TtvbH-o4-CzPtMhmlG2-ENIEaCzSFuAPI0i5vEPJZAgjFUa1tiELOvdAqEKnm_g6gGF4x5RQZgt2O11q8u2k3qVHoMI14G93fAghbnBsfD9wRgksk-_ept5IMazAB2z4JWkrKTIHGj1jb6qj2xX6NiSVxHvY0HM2v57CFvdWdwP27iE6uQBcj7iYHAjnamoLEYa6WISC_6ksdkCgHgc3EwOj-s0OL6Qc05wVmP6BWgmctS302OXlskjdBXUHDwfHN2gNOal1mZr9V6HUaBCcvYIVu8OR1kcmhP5dsgq8Yi7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkWAKa0VdArZS0neHaNCtwHtuaro6OcDd2ErP7KVzomqLP-TvF_d8xScRWg5Cjmoq6xqUZV1i2p32LCYKI5D8nRSV1lBgxFZ6c9a-0O7Sh04FnqYxLRTqWGEFFqh4Ejarp1ndeSlMzL_UtzkHf9RsFt99lVJuITViCXyIIVCyQ48u4A4gOV28UlQfKlnPkVW7Or-gTAXTSn9qKotmR0jdHgL-vyFeD5w567CO2v0_Cgc7cqqOjLh4y-Ny839v-uBGoOYAJUdaMtNuYxeTqOcaORbvd9r-IYPI0KpkxCKfJw3afQ1NCf0NQw2_7YsxDl1dpM6GSrqYRqREgQh1N4JNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vTdMYsNJ4vIozsPbj2Ul8ICEWfl7DMyhECxpDFWIHTejeZHvSGkhEYV4eh9gRcRlgec0SznuUx6tbbHXHUVdjlRsKpeM4nqiNUathRmSJRp-nwtRBJuKsKbYpFl1orq4vADnbTOzXbKvx26jKb2lbm6hWukXWsDZiNFr30Gq5Tj-tQsKeIryiLl-RyzFrBfRCVryFoG5Ora8IMWjX_aQQgi-05JEJJsWJiT5-WpuTaGtWuF8kd7ZBQZYZ3Q0p9fc-Kcgz4NgNM3-Caha7sIq2fWBtu3KKCdg-dncQhpu6Yf2H7xg1-vbiehMsBQpmu7D0nEFPMewOaP0nGn6OJ7AiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VwUaTDd0MKKRRmegIISd9ihEXMKdKS_xAnwi4B2wIIu9B1i30rKhTH25Av8S3VfyDUwbNXm0I6id0FaguwtF1YYE2PyDVFuSFXzQoDhL7fo6TA_0x2LLohoMJZVuikyaJkQHXuUn5cuVPh-LcfSraKzwaJa8RY_uiplgZl9KHkyZ7_DWcVn3SBkvGd2aeLERzVAG4vcF_47MQpur-P2EUXNFRzfcFfs3Kk5pc_wbaBCski16OBdIYMBIvJT0KUu8vxIARbYlg0kpsVTFglyIt_NhqKk7unpZztF34tYLbXuXITxhqf8sO5KMYpKBg5chj4YbgwMSAZpsEdQ8kZkfww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FcuE8pUr6GzModzwC3EUQG7kKt-IYwMg63OhQn3EByZoege10yrOsVpnyNJVkpVx9C4NLFXKFVayh1aB5xx97q2U_SX7wTPrVUhD-uQhxQbn1BljbKhMbV31myX-VgAtRXFWs2aZO5wzrnMmPBMlHcz5CU9otlrSIGuP80eyHHXaeAQIwSm7neMJOgVCb2t_VTfgL8PTPLp1fZUVmGts2aWlAfMHso0lV7k-bac3nG1kiXM1v-26mRE8CkbT8g9ojbh_7Wz_NsRJ5XX3UjQzAEV7yo0vFXO_yCWS0WY4ZKeph0dvX4f-ACIg0x46a5Yi6U9u9bQthR1uIwknOeubUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L33N3jPm19Pgmg3arDZX5MAoCCGSXzt5yHscMiT5UvjAfsUJQ3mHSvTjCX0yaw0v8R_2C8ndyW4tFGn3iJLTxU_S1Kto_kY02VcoUdnKP18wgSokeYV48w6tQuxDZeax8a-6iNmI8vxgSpHrTMU1YJ1dn2Bl1iII4eMg9nLdJkeYOy8d2gKPSTR1fZDsvgh8J1Z9oV6SioYMuAWg0RE-D8CjINOYUBWvzJKsSvYkn7RdOheE51UB1eekD039bMhdhn2Q9UhEhAYcdyr_6ARChjj436YsZd5RwZelb99hSJ5EEPCdOpgv1ud_v3rijnhj40dA-cfNggk86jBshepDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wy21MCWN5_-TAKLUVo43dC8qzyY2CcNzKurGFeno12iPUGvCkFtLL0jizyqQdvQgOD4mtCPITdEnJeORD1L4Qm0y9WDz4bPL366UYHpIZKdMTpKTOGHtQU6bUfKYI1R64OQ3X-KadslF7-MXeqbZsP-VexZJenzuq1OjZGZGC4CmrDASGPw_dKRptpCXKJIk5dljOlw73ChZ2bK-TzGe_i0Vwe9wBAv_AYII5_wkcRPiAXczmT5N08zliUAY_7r3NquRjjCNFuEnlQ7BN4sTTIVc4Wh7KSAidDJZMHH94228M9DT_BiW8az8vjHsyy-HJGiwKF_ACXX841o5TJhWOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: حتی سنگ‌های میناب هم از وقاحت مسئولان آمریکایی کهیر می‌زند!
🔹
مسئولان آمریکایی بعداز حدود ۷۳ سال اقدام علیه مردم و علیه توسعهٔ ایران دم از دل‌سوزی برای مردم ایران می‌زنند.
🔹
همین آمریکایی‌ها در جنگ تحمیلی سوم به‌جز مردم بی‌گناه ایران،…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/437888" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437887">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76c52eca46.mp4?token=duaCVTl63OwPR2JGKo6qonH4FbLgSXfPemPCY3ogN15o-LtFuiIAnvmidfUtQwhY8dQRTqDsQkCyvQP1x8p-n7n7VdF4y-6enaD-gF1H4Hcm36b1EF5WbeUVNkj3cHgud7Lxu-NAOETQG8FnQusa1uh4GNBmt2JX9DF3PVO39p9rhjYlK5QLnkfPn7zn0PdB-Nb_5nkmxKM95F9qQ-HsPHdFnIAuJe8MZTIK1PURsli4mny8UrAR3DS19cHk9fH2jB5pjccNvPQWAsw09szUxQuSrmN13Vb9NWzyhwRzXuLxpJ8Wb9kFXhtvoj1d4Sgr-gINz2XAuRA25hZPXuyNAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76c52eca46.mp4?token=duaCVTl63OwPR2JGKo6qonH4FbLgSXfPemPCY3ogN15o-LtFuiIAnvmidfUtQwhY8dQRTqDsQkCyvQP1x8p-n7n7VdF4y-6enaD-gF1H4Hcm36b1EF5WbeUVNkj3cHgud7Lxu-NAOETQG8FnQusa1uh4GNBmt2JX9DF3PVO39p9rhjYlK5QLnkfPn7zn0PdB-Nb_5nkmxKM95F9qQ-HsPHdFnIAuJe8MZTIK1PURsli4mny8UrAR3DS19cHk9fH2jB5pjccNvPQWAsw09szUxQuSrmN13Vb9NWzyhwRzXuLxpJ8Wb9kFXhtvoj1d4Sgr-gINz2XAuRA25hZPXuyNAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت محسن منصوری از نصیحت شهید رئیسی به الهام علی‌اف  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/437887" target="_blank">📅 14:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437886">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPMcn4-_692zEEDclwJjLj8o1CquVHvRWnFiTZPrCp4rZGshBH5cMujlGQxr5c_8QOF679JZfjX24P9wihuJLS2vDyrnbhVHqeLOkRDK14Or2awEAtQIkIvF9d8oVcJLCDIosx9BADUwGSSFRC0Z5mZjhUXwiWxvwc2hYOyxDQ0rBdGw5fIsMUnwCQ-URXGRpGn-X51C7voX8qYqF7wrcZfNfA-Ecq48rNDUn1vMH5IgNBSGAQSOIkMMn1sRnp7_1YAgNCvqGTGWVXp_1m208wr4aRnrvyF_fX0B9WWIQ_84pI0apK-0o9G8GY4e6tMapK68BJC7I0KSFw2UGZx4Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم جهش بورس در چهارمین روز بازگشایی
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۸۳ هزار واحدی به ۳ میلیون و ۹۹۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/437886" target="_blank">📅 14:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437885">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dce6905834.mp4?token=I3DvqH2jF2PPd_SSRVy9-gZ-z0hv1UWX6gS3coN9iwUDDGtymQTRRCAuViB4gqzc9HpOoiLZLGULq4WjEe3xaNifeL1iChckcgv8QXMIm8W4yI8PLFNfA_EWHffaT8n70iT7eTeuUNcaEzlXvc9V8uS6HiJ__oGKgrnqPQ4huqbokgUfIvI2WJrJHu8EWWbdggt5zP6ssj6-WU_sZzm0rB2p_mhuGAE58Kf-AYtv8QlDTOEdNqvckoZd5WYclQcsBzW-WAYbdmt7Q9F3VxHqJtnWzHeOVYraD6u3sE_GOhNwgHOFXmrZQsiDaT35Ug9aMbxT5CxyHdYap_fvl2I0Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dce6905834.mp4?token=I3DvqH2jF2PPd_SSRVy9-gZ-z0hv1UWX6gS3coN9iwUDDGtymQTRRCAuViB4gqzc9HpOoiLZLGULq4WjEe3xaNifeL1iChckcgv8QXMIm8W4yI8PLFNfA_EWHffaT8n70iT7eTeuUNcaEzlXvc9V8uS6HiJ__oGKgrnqPQ4huqbokgUfIvI2WJrJHu8EWWbdggt5zP6ssj6-WU_sZzm0rB2p_mhuGAE58Kf-AYtv8QlDTOEdNqvckoZd5WYclQcsBzW-WAYbdmt7Q9F3VxHqJtnWzHeOVYraD6u3sE_GOhNwgHOFXmrZQsiDaT35Ug9aMbxT5CxyHdYap_fvl2I0Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تانکر سوخت مخفی‌شدهٔ ارتش صهیونیستی هم از پهپاد حزب‌الله در امان نماند
@Farsna</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/437885" target="_blank">📅 14:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437884">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONlLY93_zdQwrXnhQOpnRXpp-SDrrySNu2zzMQAOpHTWv9Qvi6fTXKeWFNz0KUU0NT4yoajqdVRTBsQzJzak11mELI4R8kbvEE9wxLaLClukkmHZFoNvkAVvTx9bzQLYVIW0wxWptPnWIgPdkTBUsdURz9WtGRZ4S8BZklmkdVtdRhHWxS_cL5_RoxZigGTf-4OwC1Bl6kk5pszPdyVUTZnk7FFfwQiB6chsGN48fnHJXQQvlEEYlaxKTyIeDecyqPoh-Hqd5qmr0QyUrvZE7f0Wy_qVVT3sMGI43SmdlrqWELnBMmWz_Y_CqEOAcjAScK2UB_swblII2SBA87vaMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رحیمی بر سکوی نایب‌قهرمانی آسیا ایستاد
🔹
در ادامهٔ رقابت‌های پاراتکواندوی قهرمانی آسیا در مغولستان، زهرا رحیمی، ملی‌پوش کشورمان در وزن ۵۷- کیلوگرم موفق به کسب مدال نقره شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/437884" target="_blank">📅 13:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437883">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/No-qW6KyRpkZqldPzbfVwvIsAASE8Rq0e0A3aMFiWwNHQNHKFBHYKrpueGUsGDN9WyBEYJeDa0_Yx3WXR0eUi9pQO-cU3Re4WIR2D6vdOtveZUoJ0RiFsPTTVpx2Ba7gRbuy01D71kTq_1VR0fxAZ7OhX88TAdxb9i7ZqKDKVqjw7NBjutDzoF9yuuQGwHDc7223x6t3U04SzSzkczMpk0g3pC5Mq0-gAnsN5gOSzAtFwwFtTNHCyijClF2WzofpvHy-yNw-qAI0jfPgFFWtgekb_V5bIXF_qT9kTPu-nfAMa6_YoSUwAd2Xm5VMBcJkfU9kBF_O6F5pjvDqViDQMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رحیمی بر سکوی نایب‌قهرمانی آسیا ایستاد
🔹
در ادامهٔ رقابت‌های پاراتکواندوی قهرمانی آسیا در مغولستان، زهرا رحیمی، ملی‌پوش کشورمان در وزن ۵۷- کیلوگرم موفق به کسب مدال نقره شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/437883" target="_blank">📅 13:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437882">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxMJZFwCpRSYMpek9GrPfop3LLo_U_RCbjxYToYKJnmbz5-fVfZhpB2Fhg4IHLKhoFiVZpVY3NLwPiYyE4dCbuaCVtnwXtgLMafnTeue5YnbkCd26T9i_JKYQOvVxtAQoVnc3-L-khFyz_Sl2CXjZXaxHO02hnv8mxS19AXGuurT13heDLu9qEfEwxp0e10JED-yBvAAgqIfAyNOshC6OEKqmd0NEPZt-F0mUjqne52L6QtASg3IgM2Kno-p_4xgU63GbAsBf7Mqh1fBcZFghEfWSecWmbMS-JlsL9mmiyZr2AwsUrV6sYwSCnUmOpACf7bg4m1HkGV8k43_W7lufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جلسهٔ ستاد ویژهٔ ساماندهی فضای مجازی به ریاست معاون اول رئیس‌جمهور، موضوعات مهمی در خصوص برقراری اینترنت بین‌الملل مصوب شد که پس از تایید نهایی رئیس‌جمهور، برای اجرا به وزارت ارتباطات ابلاغ می‌شود
🔸
یک منبع به خبرنگاه سیاسی فارس گفت: در این جلسه برقراری اتصال اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف تصویب و برای تأیید به دفتر رئیس‌جمهور ارسال شد.
📝
جزئیات مصوبه اطلاع‌رسانی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/437882" target="_blank">📅 13:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437881">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c577a69b.mp4?token=BSERYyoCf_NaAVEB77aARqbq81iX7uh6kMOhntKkRPlW-WgQ1kSRwNjh2NgMMAqMvG-UjSfrcMLovVOtak1e2Np8Ld_7iy1iF8Zz5Wdf9Qi82D9uAwo3hv3PunL81ud6luwtyFPe2uhDz_nE7iscRncHqRO1YNpuc34NM0QTTpLsSCMy11HDsn90BFXFf2bLeGkC8ANjNPIj4n6grJeiH2ERNK1pN0r6RRFSYSNIDvY8mAv_cQQOKNIGWfon8ZwY_Mb9NCoCjGXCh11lIfDh_4yrHeeqXo3dcz-EB80E0XdUE2MzVSOYJgYK9ePbubFGaQTFyvKXaqqeTlDv6Cj2UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c577a69b.mp4?token=BSERYyoCf_NaAVEB77aARqbq81iX7uh6kMOhntKkRPlW-WgQ1kSRwNjh2NgMMAqMvG-UjSfrcMLovVOtak1e2Np8Ld_7iy1iF8Zz5Wdf9Qi82D9uAwo3hv3PunL81ud6luwtyFPe2uhDz_nE7iscRncHqRO1YNpuc34NM0QTTpLsSCMy11HDsn90BFXFf2bLeGkC8ANjNPIj4n6grJeiH2ERNK1pN0r6RRFSYSNIDvY8mAv_cQQOKNIGWfon8ZwY_Mb9NCoCjGXCh11lIfDh_4yrHeeqXo3dcz-EB80E0XdUE2MzVSOYJgYK9ePbubFGaQTFyvKXaqqeTlDv6Cj2UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت اعضای ناوگان صمود از ۴ روز جهنمی در اسرائیل
🔹
پس از اینکه دهها نفر از سرنشینان ناوگان صمود از کشورهای آلمان، ایتالیا و فرانسه از شکنجه و آزار جنسی خود توسط نظامیان اسرائیلی پرده برداشتند، اکنون سرنشینان استرالیایی این ناوگان نیز روایت‌های مشابهی بیان کرده‌اند.
🔹
به گزارش رویترز، برگزارکنندگان «ناوگان جهانی صمود» اعلام کردند برخی از بازداشت‌شدگان پس از آزادی به دلیل شدت آسیب‌ها و جراحات به بیمارستان منتقل شده‌اند.
🔹
«جولیت لامونت» فعال استرالیایی و مستندساز، در گفت‌وگو با رویترز گفت: «این فقط آغاز چهار روز جهنم مطلق بود. من به چشمان بی‌رحم‌ترین انسان‌های دنیا نگاه کردم و هیچ چیزی در چشمانشان ندیدم. باید جلوی این افراد گرفته شود.»
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/437881" target="_blank">📅 13:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437880">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📹
جمعیت، خط مقدم یک جنگ پنهان
@Farsna</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/437880" target="_blank">📅 13:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437879">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMF-rTA6kgXbhMiJMqkCncwxtqCdb3k_b06QDtFD_3Kx3laCw7AMIuQUN1-eXOziPaDAllByNtP4HNYt0IItKEUFHspuTfPA48Wj23NmmSB1TRXrPC4mCBH7TvTmxo-O56w_YYAVhlBoMx_DaecA4HxOdLYBGt1ELLnWlzlYt89rvb24-8aPw1H8a97yRFIKlchCcURDkzZkstbrvXntVC3e14qt3UlluPMmKjjObDFI0hI65KdLY9CL60bKBLGI2pY7BfMxzMRiuy8XkyMKtFiVoNSYcVwp5W7Z3Xjni61eGId9zqhXRqUWFU4l0Xy-ahmkabEIGZrEVPHa4hyYaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
جهش ۵۰ درصدی تقاضای مس تا ۲۰۴۰؛
🔰
هوش مصنوعی بازار فلز سرخ را متحول می‌کند
🔻
براساس گزارش مؤسسه معتبر S&P Global، رشد شتابان هوش مصنوعی در کنار انقلاب رباتیک و هزینه‌های دفاعی، ساختار تقاضای جهانی مس را متحول کرده است. پیش‌بینی می‌شود تقاضای سالانه این فلز راهبردی تا سال ۲۰۴۰ به ۴۲میلیون تن برسد؛ جهشی ۵۰درصدی نسبت به سطح فعلی.
🔸
این گزارش تأکید می‌کند بازار جهانی مس در حالی وارد دوره‌ای تازه از رشد تقاضا می‌شود که ظرفیت عرضه، هم‌پای این جهش در حال توسعه نیست؛ موضوعی که می‌تواند بازار را با کسری سالانه بیش از ۱۰میلیون تن مواجه کند.
🔸
مؤسسه S&P Global تأکید کرده است که تنها سه‌سال پیش، نقش هوش مصنوعی و مراکز داده در برآوردهای تقاضای مس تقریباً نادیده گرفته می‌شد، اما اکنون این فناوری در کنار صنایع دفاعی و رباتیک، به یکی از مهم‌ترین موتورهای رشد مصرف مس در جهان تبدیل شده است.
ادامه خبر در مس‌پرس
👇
https://mespress.ir/x6QQ
@mespress_ir</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/437879" target="_blank">📅 13:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437878">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/437878" target="_blank">📅 13:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437877">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7GwdThKvljjLnEBV-hRsH9IBVTngCL-C_2FzagbX28CnvDItGnxTsXYG1geud678GpYNiSQjLpF1NVmpzxQppKVYGj3TOqBerDayqrpKBKRa1u68mmWUcm4Tc0NvWIBsBRc83X5sRtZQuFSOFR-4NHE_dwcGY-LFRrvu4BXnW8a8ex3VZZOTOGkbblI7rSwsUYlljEArhNXd3w4rGQJrhYlXXbEuw8nAm4skLUYqmyWco4205QmgmYcr7T_JcvAZpN1Afyit_kRpLcKPBbbM5YpMoheW3uWAJWTv36PTOdsZQ4KgPwkottuRPyhuQgyWwGzSkwVHkwrjpnhpDAZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رای قاطع مجلس به ریاست قالیباف
🔸
محمدباقر قالیباف: ۲۳۵ رای
🔸
محمدتقی نقدعلی: ۲۹
🔸
عثمان سالاری: ۷
🔹
رای سفید: ۵  @Farsna</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/437877" target="_blank">📅 12:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437876">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbi5X_xyi5c3Bz4IYN0ouzCLomEU54IPdBo33t_QVyXooF5sYJglh2McNNgCQeLgfU9rgVjoRAfc6okeqBp_4eTZ1dxyjS2CrjqM7bSsoZlR0XCu0gWadsPOfjiOqLs2FhlKRXwueRMRWLU6LbDm1l8EfMGXq7jHIpeu5LHw7A6ffJRssM2blAlDr0AdtKoFbIH9xeqJndEhFTQhUsKg8ZwGyWtJEGD8GHGCQprbsRnXuGRrliKZHXcCjaBvjQQMAtVp8gtEyudCZ_Fw90zkQxt_AwRcUZ5x6TXoVg_b9fPfayz3e29JkK9cDUpOGoKc8cnUdorkoVTShedEaG3_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقابله با رانت و قاچاق مطالبۀ رئیس‌جمهور از اتاق بازرگانی
🔹
پزشکیان در نشست با اعضای اتاق بازرگانی، مسائل و موانع موجود در حوزه‌های ارزی، انرژی، تولید و تجارت را مورد ارزیابی قرار داد و دستورات فوری و لازم را برای تسهیل فعالیت‌های اقتصادی و رفع مشکلات موجود به دستگاه‌های ذی‌ربط ابلاغ کرد.
🔹
رئیس‌جمهور: دولت خود را موظف به پشتیبانی از تولیدکنندگان، صادرکنندگان و کارآفرینان می‌داند و در مقابل، انتظار دارد تمامی فرآیندها با شفافیت کامل انجام شود و زمینه‌های رانت، فساد و سوءاستفاده از بین برود.
@Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/437876" target="_blank">📅 12:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IWrjufL2-2oqGXUdeNM6SZ-ONAuGGY9toltVUzNpH8TdyHAD5f7NfaMGTRLADlo6QqvdG4HBW13fMn-vfmgnn0uPJK5lQCc6z5C_O0IaybwtrMkfmigNZQNJZ3URn8oTA3KNzQ4rT9EWDwHU3EHST6quF8QPiMlKg-27pQbQmhNo1My5DBhUz_pYRjFU-731CjqWBwGOB-gUryXAvJXZWiP1bWaHw5Hi7LO1p1Kiz_GTKQySA1vdLULvBLjPiaLGi6Lte2PAxl_g38JD7PXUiZ9eg88gBqkmAZcZ7Yu29_ZqxtERB-C8e9VKWy7zMF5rMEU_dw3Oja4RG305uZjzig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIAQI1-L0_-_ZTV8mntwaACuq1uMw7q3A98xLBsDDHZHY6gMp71kJq8tGOd99pv93M46XqAozMxp9ySiUruzuGwJpHP3JEOEeRWgEHL2xa2aS0iqVMpuoxmQCEiwLREGbMP8YNo3z6yyDzFvtqhxLJ0F7_ydwqMOnR4K22kpeMuNLwIArFQ6K3nGG8vHpIQ8JMaX9cy1YlsPVy1yVwm1amB0NNeUDMKwDBycW85izZCupPsWVrg1PNbWeTKDwZf1Qzne_EGN02TjngYoGQ46vbnutr0binF0nGjFpiM6BhPfJG_JYwhVm-nC-mQQ-I7KoiNF3DTHRxj2VVJPwyV48A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kw_xRg1ddH_vMSvDgw-pYSqWT5H34laFUP2fZupzGqO8xCweWqy-UHR14I1PqX6VuXYDdyYuM5XussJrqHCT8rl6hsifzqE31uNooALn3yA4r4rRQPPgxCzRbLA2SDj0ZQMlIhRXJVSvVeN1xoQlgQophLe6N6t2G94nGZrO34L24Pwk7bDxpnfVS4EUqufXLhMvPfTlJ7hlnPQk49F-GPJMRxX3nuHiNoBUteoCX68EEd6nQa5xM80iYRGnAu9Xq4wQZXTJDXksQRnEIRMic96tbJjx5CRWaLTtU5G3vq4Vspi8fQLpzytTzWwhQZw9eI59RDiSFWAnUwIIBFWmSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ldQt_K7yabTbAsKf8sXY9XONlFE2ByJqe9410Y7Cg7VuUV2HOIFFGQZ3K7AKpyDm5Q69mNu0UzQWpx1YmMMbXPZGkY_teUBaVKksFwh9CAVZJHAFWSQWDNEz-ovma8bLoeGpP_r3PSkF8YW1ugCc2FatWSJpn-F0dT6rgFFPGr7lG8QUOfeaFhMwRwAfSZpYDCBLHu90WuOsyVOwBjR197Yk06G4ApL7P7ddXExe_NCbxjHCt8gvTXy4qKlw0PS428Qj9czPQjIiB9SXUVC5A5Q2s0t4CDOun9uiInzXVgs1zuYqykCk2XBPKhkuRKuL2f25MA6DCU8eWaN5DMPZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MawKCcAYoArMjJAY964vJCEWgU7rsAbeU6vrsicrV-ABS08J2OdRY9nR7IotJhlvNR5QkkdzqZYnF9CobfU59JHW12qGtiq0awWKBlnrumj4kFGEokBHIKDbJkL1vZq_QeESVIxspu88kGLt4QCf00G958tjLGwQQZslM3GaQzacKqL7XwvwnDsayLvGV-gBYKws9OWM2jN67EGBB7LTyCv-YyVxSWY4-h3VevsMNyDpv7g4Ve4g0yoKPYyPO3oeBHwegd6DdlNEruwMYHPaJoHFHXVNOZIzBsL-KCOb2gs-_kDhvxLXTjYc3d_O5xS0CLm6MQCzqv2zNB5PR4SfzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dxf9KKUZNOID4rMJyj-EWTotHmwNxhDJtih58vjz1YbxTK0Cx_OOH9iUoyt_6xevRe3JNZLnKNR96x4tlcV0zV1CJz_wOgkV-pQq_9XLy0X03w98fgJLGAwTUnmCdFcZXaYqO-GIZBR7pcBvp62EgB9wIEkW8tqVWoMlokDhdp0pdvq2O5pMHWQk19uDKibwMIVRwpd6T2DKywGQyN3QG5Gv8V3687Jg3FuvcArsecWEKwrOyZg4nKfWlb3KmEJgAZTuH4wT41IlHAV2dL-3i3E-nRnoPrOK7U2mtnO6x9bwADIjxthUg9CvQQM2XKND8vjy1LZsLH_741sEZ74i6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mK9nraLKBXgiFlMG35Q7LIIks84OFdMGx8tx7EKCb-kKKBAR5V4tNiZp7GlXvSMDxXIhMqV5KyEaxKGv2zRS16dReJPOvJyxrVNK6sGbj8TuXTiFM5102zc4kfejgwWVkOdxDVstsZa154VZAga7dhnkpD_bWh087V9A5MK-5kRkXONOtKUa8mt4_l0dViEZ6UaDM0beKeIpa5rfcXtMBhgaF4j1HXiCUPMRfh9yCDmqhuA-MYzbrCUxBr9DMdc1h_YZdyu4XoS8V3-5VCp4ChL9hTR7ieoOqIJkwDhAlb64B7GAP7-ufNc-RvK0DvMn_4MNxffT8mCNtelJMiod4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
باغ‌موزه‌ای از جنس مقاومت در دزفول
عکس:
علی صاحب محمدی‌نژاد
@Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/437869" target="_blank">📅 12:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437868">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quEnwknzkfyibzsZcaOZ2a3G0iP_q6q6rL1co6utVaWZARysYCXvhjLcgqdnjBmaXt-P-UA5LwUAGIjmppSfWGzZQF0n0f5qHCIQsffO8bS_hE1inILLMikJjVH7vXREB99sDajQhxzlLxTcyiyoKUUsm2S1NtsBGmLssa6C_WUi5Aa0XCXbt8z00Y5_etjSjjL3cUys7-ZYYk78p-MmWkKVHFwA6YNx05iLbx2co3W4I_ZBOHiXeMx6LgcVsaLiNMXd8isqbg3KqeyaqGh286QdPKDJyG8nGr7OxZwCBTncsampleYaw6ddmsqPkdJ8O09sTw3pAf3jMhbmUA6EIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا غندی‌پور</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/437868" target="_blank">📅 12:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سمیه رفیعی: ۱۰۵ رای</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/437867" target="_blank">📅 11:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437866">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a25ac8b2.mp4?token=HQ4IpKQXarY4GgSjdXhaHQWSLX0PQH_Z0GNdkI29mrCcOJDeeNftUJkSYES50H5rhDCmOGL0YrMX7b-MG8bdEEVZORouPgpQtZY5LlJVNjlUfIELTNAXpsi03ZwThkNES78QLSJCTewrD_yYS3JtWxL9bn77y_8soh8kiIB_jAaPm4L1FEjwzgLqWAKQklXAF5JQ5oDnwJ62VDxWJn3FiudI60NvNvf9JHax_MQqzS_Is7YAQOjEoE1fvsbQ6NfHw19GTRCfNlSLrCLy3iCzLwUq62tiJI4Os-J2w3vuE05vgYgWUySAmRFWve5S7T3i48BUpIC9xr1LZ7PaU5zyYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a25ac8b2.mp4?token=HQ4IpKQXarY4GgSjdXhaHQWSLX0PQH_Z0GNdkI29mrCcOJDeeNftUJkSYES50H5rhDCmOGL0YrMX7b-MG8bdEEVZORouPgpQtZY5LlJVNjlUfIELTNAXpsi03ZwThkNES78QLSJCTewrD_yYS3JtWxL9bn77y_8soh8kiIB_jAaPm4L1FEjwzgLqWAKQklXAF5JQ5oDnwJ62VDxWJn3FiudI60NvNvf9JHax_MQqzS_Is7YAQOjEoE1fvsbQ6NfHw19GTRCfNlSLrCLy3iCzLwUq62tiJI4Os-J2w3vuE05vgYgWUySAmRFWve5S7T3i48BUpIC9xr1LZ7PaU5zyYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
👍
سینا خلیلی قهرمان کشتی کشورمان، با سر و ابروی تراشیده به دیدار کودکان سرطانی رفت
@Sportfars</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/437866" target="_blank">📅 11:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437865">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌ دبیران هیئت‌رئیسۀ مجلس مشخص شدند
🔹
محمد رشیدی: ۱۶۹ رای
🔹
روح‌الله متفکرآزاد: ۱۳۸ رای
🔹
فرشاد ابراهیم‌پور:  ۱۱۳ رأی
🔹
مجتبی بخشی‌پور: با ۱۱۰ رای
🔹
احمد نادری: ۱۰۹ رای
🔹
سمیه رفیعی: ۱۰۵ رای @Farsna - Link</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/437865" target="_blank">📅 11:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437864">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e61bf8d50.mp4?token=FXzuLcLZ09JCqdadKBwpJDmlGggwlQvJT_5O_0HDoowT-6pnQrerdZ_6ABYHee7A2fjnYbkiCn8dhlARsfLV22PHHMrPXMyUQDrks84Wg4NFmykcID7ETEfP15LgOeh9eCyjZbyntW5a0jn8iWYRLk4UZSTA5kw2UJnHFBuzrqaHa1-ZTDHlKz7ZziAt25wVmev6I4p20gZL0EV0V_1XVoNuej9Wc5eGSbFMWkaTMdHiRLV8uNqzCVyrUwFvYy51-YtNwYQR3CX_N-Gz9togBYA-6UEKQQHGrX3h3_sxVxZG27T8fkkZ_QfPKAjU0NYaD1vjZRh5snKgF6ZadEaKX5W6MMz1TU8phXRHgZF2I6bTU9_WjVlutkTg7Y7rszFlDry9ALsZjMlOY-9KFCSAAXT7gcaeyKhntwglL-npkmcpjFC9sHzbWkK7mlZBF0pclxCSvV9YULchJ_ms9zDB0VDLvb1_kH3uCZ5N60M0sZlegV1WVCOBzXsSkClvlLtNh6vfdStPaqGJeA65ZB8ERHEr-MS976bvoq29omuxMs2WJf0ZXQmFEkTNpw96mIR5EGgf7NKzw4lbYG8zyaOGwWtpsPomYsenLVK1tGq4Nyd7srGerMoHSUXbPNCAFWrR3HS3k3oZiAnPuPwtOv54uWY1eHIGuaHplb59ykIT0YI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e61bf8d50.mp4?token=FXzuLcLZ09JCqdadKBwpJDmlGggwlQvJT_5O_0HDoowT-6pnQrerdZ_6ABYHee7A2fjnYbkiCn8dhlARsfLV22PHHMrPXMyUQDrks84Wg4NFmykcID7ETEfP15LgOeh9eCyjZbyntW5a0jn8iWYRLk4UZSTA5kw2UJnHFBuzrqaHa1-ZTDHlKz7ZziAt25wVmev6I4p20gZL0EV0V_1XVoNuej9Wc5eGSbFMWkaTMdHiRLV8uNqzCVyrUwFvYy51-YtNwYQR3CX_N-Gz9togBYA-6UEKQQHGrX3h3_sxVxZG27T8fkkZ_QfPKAjU0NYaD1vjZRh5snKgF6ZadEaKX5W6MMz1TU8phXRHgZF2I6bTU9_WjVlutkTg7Y7rszFlDry9ALsZjMlOY-9KFCSAAXT7gcaeyKhntwglL-npkmcpjFC9sHzbWkK7mlZBF0pclxCSvV9YULchJ_ms9zDB0VDLvb1_kH3uCZ5N60M0sZlegV1WVCOBzXsSkClvlLtNh6vfdStPaqGJeA65ZB8ERHEr-MS976bvoq29omuxMs2WJf0ZXQmFEkTNpw96mIR5EGgf7NKzw4lbYG8zyaOGwWtpsPomYsenLVK1tGq4Nyd7srGerMoHSUXbPNCAFWrR3HS3k3oZiAnPuPwtOv54uWY1eHIGuaHplb59ykIT0YI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله فاضل لنکرانی: در اجتماعات شبانه تفکیک باحجاب و بی‌حجاب را مطرح نکنیم
🔹
هرکه در اجتماعات شرکت کرده برای دفاع از اسلام آمده. بزرگان ما در برابر عظمت مردم اشک ریختند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/437864" target="_blank">📅 11:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437863">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‌ علی نیکزاد با ۱۴۳ رای و حمیدرضا حاجی‌بابایی با ۱۰۰ رای نواب رئیس ‌مجلس شدند.   @Farsna - Link</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/437863" target="_blank">📅 11:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437862">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50542a4d12.mp4?token=MA2oIyA446wDPaRMQV6_w3jNGYPILde6vySfAaSvulrCqEbXDcCYFnuTzMlQiKozfpmc2xjhp3o1tpJbkl9RPNWqHNCLpjOzDKSsKtsO3BiIj4wJSDVDhUyu2ZmoS9PVv-0vHiuxoCsyB9OPMAx5zxqSZQlp0d_LIcyw2T5kmDKkCpU3kvx1pMjUPb0c16ZKJZS66W1vyw2BDKe8t-gNJVFVk8oJrRKNuQy0EorKoJ3jaC8y34USVSvMzLrj6iGepxF_IT3fmn3dpGNf48c8fUcZtWI1TatViK6JXfdXguVchG4cHEDJSq0bhEP0Gq7fN4X9FvxYuxMhwH4j38RUBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50542a4d12.mp4?token=MA2oIyA446wDPaRMQV6_w3jNGYPILde6vySfAaSvulrCqEbXDcCYFnuTzMlQiKozfpmc2xjhp3o1tpJbkl9RPNWqHNCLpjOzDKSsKtsO3BiIj4wJSDVDhUyu2ZmoS9PVv-0vHiuxoCsyB9OPMAx5zxqSZQlp0d_LIcyw2T5kmDKkCpU3kvx1pMjUPb0c16ZKJZS66W1vyw2BDKe8t-gNJVFVk8oJrRKNuQy0EorKoJ3jaC8y34USVSvMzLrj6iGepxF_IT3fmn3dpGNf48c8fUcZtWI1TatViK6JXfdXguVchG4cHEDJSq0bhEP0Gq7fN4X9FvxYuxMhwH4j38RUBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت خارجه: هزینهٔ ترددی که در تنگهٔ هرمز دریافت می‌شود بابت اطمینان از تردد ایمن کشتی‌هاست
🔹
خدمات ناوبری و اقدامات لازم برای صیانت از محیط زیست طبیعتاً هزینه‌هایی دارد و نام این هزینه عوارض نیست. @Farsna</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/437862" target="_blank">📅 11:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437860">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XER6Eqp37-kZuM-5VpiWVI4Gb11ni-BucRKCFd3y_kTwaLinn15rfdhORGCalaEJ1T6UFq8W3kiFtLPqXLt-R_JXWN_gtFSDIbb2DOT-0-QxCPeUOI3Hv_JxlHsVeNL-OEg6p933m5jHTjZ4qdnDwoN9YV99IaWVlQJ4lQS7EnWBv4BpA3jxTa1CptxONTZeWQvU-qtHzelLHzVJv6VSoBTcMmXX5keQyUEOZqbo0nv2kdErYxgC3K0e6vtMFllnfGIk4lWm5mBqHc3-YXfBDzpQgH9LYfv-yREG4j_TC6Vn7vjl12zYCwwq8Ne_G_tkhvz_EHzP2SqgtWbY9-gsqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا دبه کرد؟ روبیو: اسرائیل حق دفاع دارد
🔹
در حالی که به گفته مقامات ایرانی، آتش‌بس در تمامی جبهه‌های جنگ به ویژه لبنان در تفاهم‌نامه بین ایران و آمریکا مطرح شده است، وزیر خارجه آمریکا در جدیدترین اظهارات خود گفت که اسرائیل حق دارد از هرگونه حمله توسط حزب‌الله جلوگیری کند.
🔹
مارکو روبیو در پاسخ به این سؤال که آیا اسرائیل طبق توافق، به لبنان حمله نخواهد کرد، گفت: «اسرائیل همیشه حق دارد از خود دفاع کند. هر کشوری (رژیم) در جهان این حق را دارد.»
🔹
وی ادامه داد که «اگر حزب‌الله قصد داشته باشد به سمت آنها موشک پرتاب کند، اسرائیل کاملاً حق دارد که به آن حمله پاسخ دهد یا از وقوع آن جلوگیری کند.» به نظر می‌رسد که روبیو با این اظهارات، این موقعیت را برای اسرائیلی‌ها فراهم کرد تا به بهانه حمله پیشگیرانه، حتی در صورت امضای توافق آمریکا و ایران، همچنان حملات خود به حزب‌الله و مردم لبنان را ادامه دهند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/437860" target="_blank">📅 11:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437859">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فرمانده قرارگاه خاتم: سامانه‌های جدید پدافندی را به‌کار می‌گیریم
🔹
دشمن بار‌ها مدعی شد که بخش نظامی ما را در حوزه‌های دریایی، هوایی و موشکی نابود کرده ‌است؛ ولی همواره ما در صحنهٔ جنگ نشان دادیم که همهٔ ظرفیت‌های ما باقی مانده است. ما تا آخر با دشمنان مبارزه و شکست را بر آن‌ها تحمیل خواهیم کرد.
🔹
روند ارتقاء تجهیزات ما به لحاظ تطبیق با شرایط روز، مرتباً درحال پیشرفت بوده و این موضوع در میدان مشهود است.
🔹
پدافند هوایی ایران در جنگ تحمیلی سوم به‌مراتب بهتر از گذشته عمل کرد؛ ان‌شاءالله سامانه‌های جدیدی را به‌کار خواهیم گرفت تا بیش از پیش با حملات هوایی دشمن مقابله کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/437859" target="_blank">📅 11:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437858">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rimbriYjoaARnazHJswHp9b6F_Rhs4wNHbneArorfOPPFUIFy5XqWIzrVQs8XmWNOPNDzjS8bu9Ete5XAAbJSRTy_McSSuqluRqvs233AH1Y5FcDxzQoHgumbLDaxE_9fjNk2dG18pHyWojAA0RaKmzEJetKxthpuKkhspXnCVkmkL7t-10qA7iosCao3XrxdD2ExDDfM3BRmOspwkJTrvkenNfL4dzLLmbQDvd8ISUWUsRKP_gVK7QWlMMRpcaameGCfIFHCalpVOPrYCvLxiswnIbly05cCfXVFa15s10JigXyrpgI_n9jWyMLK5m05Cbbfj9g0Rps3U9Levz7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارندگی‌های کشور ۶۳ درصد بیشتر شد
🔹
میزان بارندگی تجمعی کشور از ابتدای سال آبی جاری تا اول خرداد به ۲۲۹.۴ میلی‌متر رسید؛ آماری که نسبت به مدت مشابه پارسال ۶۳ درصد افزایش داشته.
🔹
براساس آمارها، ۱۵ استان امسال بارش‌های مطلوب‌تری را تجربه کرده‌اند و در برخی استان‌ها میزان بارندگی حتی بیش از ۲ برابر سال گذشته ثبت شده.
🔸
گفتنی‌ست به‌دلیل ۶ سال خشکسالی متوالی در کشور و انباشت کسری مخزن در سال آبی جاری، همچنان صرفه‌جویی در مصرف آب ضروری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/437858" target="_blank">📅 11:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437857">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rt1mlnwJlqi0TZjY9Q5W4z8on3EDqcECT3LcpLxZZ5yMPLu1E_2_5LXF-YY7yhB6sdacIRz4BPHGSyqQYbHZ5TgUzzZAYUTGl4cfaefIh0M4Bzprur7rg0S2lClrCR6Ta8sjUIhvDFpGLJpjYbkb_yyfIdRo7XThU70rB4tJnAOYHxFVLitep1gFQ_0Nm62yjzzKvc7RhyvafbswM1c4WDrprFx_pBrHTAkL-HvY6kgLasvrLSLio_z73FmXCu3kXyotIswWHlHPtJmI9iNEVuprUjphTDdASgIqc4oeS_frCFlr17qk4BTuS70Hc93k2vaXiz9veEz6asa70SR80Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: امیر قطر به تهران سفر نکرده است
🔹
هیئت قطری به‌سرپرستیِ معاون دبیر شورای امنیت ملی قطر برای کمک به پیشبرد تفاهمی که به میانجی‌گری پاکستان در حال انجام است به تهران آمده بود. @Farsna</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/437857" target="_blank">📅 11:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437856">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌ علی نیکزاد با ۱۴۳ رای و حمیدرضا حاجی‌بابایی با ۱۰۰ رای نواب رئیس ‌مجلس شدند.   @Farsna - Link</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/437856" target="_blank">📅 11:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437855">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رای قاطع مجلس به ریاست قالیباف
🔸
محمدباقر قالیباف: ۲۳۵ رای
🔸
محمدتقی نقدعلی: ۲۹
🔸
عثمان سالاری: ۷
🔹
رای سفید: ۵  @Farsna</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/437855" target="_blank">📅 11:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437854">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">چرا ایران بر آزادسازی پول‌های بلوکه‌شده پافشاری می‌کند؟
🔹
تهران در مذاکرات با آمریکا، آزادسازی فوری دارایی‌های بلوکه‌شده را به یکی از مطالبات اصلی خود تبدیل کرده؛ مطالبه‌ای که ریشه در تجربه‌های گذشته و بی‌اعتمادی به تعهدات واشنگتن دارد.
🔹
مقام‌های ایرانی معتقدند تجربۀ خروج آمریکا از برجام و بازگشت تحریم‌ها نشان داد توافق بدون تضمین عملی، نمی‌تواند منافع ایران را حفظ کند؛ به‌همین دلیل تهران این‌بار بر دریافت امتیاز نقدی و فوری تأکید دارد.
🔹
برآوردها نشان می‌دهد حجم دارایی‌های بلوکه‌شده بین ۲۰ تا ۳۰ میلیارد دلار است؛ منابعی که به گفتۀ کارشناسان می‌تواند نقش مهمی در تقویت اقتصاد کشور و آغاز پروژه‌های توسعه‌ای داشته باشد.
🔹
در مقابل، برخی کارشناسان اقتصادی معتقدند نباید توافق بزرگ‌تر میان ایران و آمریکا را صرفاً به موضوع پول‌های بلوکه‌شده محدود کرد؛ اما گروهی دیگر تأکید دارند آمریکا باید هزینۀ بدعهدی‌های گذشتۀ خود را بپردازد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/437854" target="_blank">📅 11:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437853">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83aa6ec124.mp4?token=QNdLTmDmmbBRcxcA_UjkqA0A_hCwAwJUA0YqSrnKmxhfo89UAnuINiUsESXB7M9q7WAnf3xw9gQGVgRahDQlkVQOqdNV17O8og6gPEYxiIIhxqPavQ-7vK_lMLr7vADCUcpKB1ggNCI5rQGCCRvb5MnvMxn_En2SXvOVWV7VtpyXHVG0rmNmXWI9rTIzCXaXceX9I9VwLR2_lvfQ69wBaF8lRgM1FSPj9feX6zVzIgvPbbC3Ck2Ygx1CL3qEk_-awek85eVEhdLPSxv6t9cn7Zk_hIGZll1Gp-ztiam2FxsTXxym9THkHnmijCBnvtPMyt9JItlKi4fezdqmlmKd8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83aa6ec124.mp4?token=QNdLTmDmmbBRcxcA_UjkqA0A_hCwAwJUA0YqSrnKmxhfo89UAnuINiUsESXB7M9q7WAnf3xw9gQGVgRahDQlkVQOqdNV17O8og6gPEYxiIIhxqPavQ-7vK_lMLr7vADCUcpKB1ggNCI5rQGCCRvb5MnvMxn_En2SXvOVWV7VtpyXHVG0rmNmXWI9rTIzCXaXceX9I9VwLR2_lvfQ69wBaF8lRgM1FSPj9feX6zVzIgvPbbC3Ck2Ygx1CL3qEk_-awek85eVEhdLPSxv6t9cn7Zk_hIGZll1Gp-ztiam2FxsTXxym9THkHnmijCBnvtPMyt9JItlKi4fezdqmlmKd8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: در مورد بخش زیادی از موضوعات مورد گفت‌وگو به جمع‌بندی رسیده‌ایم اما معنی‌اش این نیست که به امضای توافق نزدیکیم
🔹
آمریکایی‌ها در چند ساعت دیدگاه‌های متفاوت و ضدونقیضی از خود نشان می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/437853" target="_blank">📅 10:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437852">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxWnRh4k63UZFup6UqKdDaqwN2isnYlt_wFjbBYfq_5JYOdxZrtiH8Nw5xO0pwd7WKpEAmU9_rnKDuDb2F0EkZGylKeVfVFq02laMPmSNaL7nJLYvd1RmnlsReMDBmyrxL69N3VLDeq0yqRgMBRrFsjem8Pn73X08tN45sMRH86ZrLvDZtq0xNhLjQp9oBGx2EZ9fnQ5IEOZEU_eToD-Xu_V3N9ahL6QLNpDQjN40DK4EdMaPjMU1Wj-Tv4l8vNxZbip90kRJnFoBEZE_PASIaUeC9asJtQEbQIL1kjx12ndqPHa_ofAivHHSJ_jB68mCO51kh_OegktoCzPHwLX-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ با آغاز انتخابات هیئت‌رئیسۀ مجلس، قالیباف در محل رای‌گیری حاضر شد و اولین نماینده‌ای بود که رای داد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/437852" target="_blank">📅 10:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437851">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5997c07b1b.mp4?token=KHNabKg5buS23d-aELr9jnT2KJCTt0IgWgchnlEC1yXXywW6XhxH-lrhhPh_6qaaCYp3kjn--_74X03rO-TdMPMHsQ6PLu3Z6rlVd99JvO_H-g7owdoQCt-I0kYQbTcNiHVJfKIiPEQM2bNmDUN0JLkdO86S7_CxRAorLCn8uSRl-N0H1AWoCr-idPsGwp25AUISgp4J7gs4abVFCve3JfdyLZ0lxlEHLeIgJrwYhNmg_zDSqZ5J4j00olj3uGLmTg0rs5x9WfSKOg8U9y559Wee_T3709bP9SPnOzdM7tQL2AfNLF92UdA83nuN-tj9CVqBydR4a4IF7cMXNltWOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5997c07b1b.mp4?token=KHNabKg5buS23d-aELr9jnT2KJCTt0IgWgchnlEC1yXXywW6XhxH-lrhhPh_6qaaCYp3kjn--_74X03rO-TdMPMHsQ6PLu3Z6rlVd99JvO_H-g7owdoQCt-I0kYQbTcNiHVJfKIiPEQM2bNmDUN0JLkdO86S7_CxRAorLCn8uSRl-N0H1AWoCr-idPsGwp25AUISgp4J7gs4abVFCve3JfdyLZ0lxlEHLeIgJrwYhNmg_zDSqZ5J4j00olj3uGLmTg0rs5x9WfSKOg8U9y559Wee_T3709bP9SPnOzdM7tQL2AfNLF92UdA83nuN-tj9CVqBydR4a4IF7cMXNltWOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: در مورد بخش زیادی از موضوعات مورد گفت‌وگو به جمع‌بندی رسیده‌ایم اما معنی‌اش این نیست که به امضای توافق نزدیکیم
🔹
آمریکایی‌ها در چند ساعت دیدگاه‌های متفاوت و ضدونقیضی از خود نشان می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/437851" target="_blank">📅 10:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437850">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oP15lGG4HSaDeopx2xjUqW7fl7ZwTPgmsNF2fbi8ttB9uzxOc0b8QsWmSwRWSDFREep-2Z_tS8PQpTdDyWc96l2GBzapguTJrd8oRB5l8ixSrjak9g3XSjKaNmKmb_5BTinXiLjA8gAz9QpJqARVkRLPEDif6Luk90NBjDmQwibo5a-EXii2Qpyu5ueJmOMOZqDLnJi2aJqi9PqLSvgG7FrVGSuW5QxcmZv6SxuAi9AMtMp64yFIexJKPU_E4nBUYw6F0j0pEmy42SzJcs7T4XKWDgTQm79O4uoOuZDF2jKsGTe-xyL2mgTSR5cd5qESfv7rxUd--3YojCUvV_dnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی کمیسیون امنیت ملی مجلس: آمریکا منتظر بنزین ۶ دلاری باشد.
@Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/437850" target="_blank">📅 10:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437849">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c1e7403c.mp4?token=DGjFHtU3cuypFYO92MUqZ_JqsipBKHCyG21SYxvdEr8uNtwDprGVeTTEkG976HptX2ODtAVt_jxBhUQQ8lP-etYiogfZ-GGV608LYZ3JpNH8WqdwcEo_my7jNaU5pVri_qefu3FzCkXZNl46kx17-aGWuvTVSbuSURdBQ03JbHSuckgtuxxlws3bl1ey1fIdObvIKzcZQb8b6ZZB9s4-DvnmX1SqEowWC0VnwqJMkl5r1A8XxQ6niaLcRygpyIz8O8onCc5BDYqxevFSBh3NdO9D6d6cytktrPaM5-zop2815z4t-JCuJKs4NNGCN5TRWb3XLOEuGJPXAmVQquAXyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c1e7403c.mp4?token=DGjFHtU3cuypFYO92MUqZ_JqsipBKHCyG21SYxvdEr8uNtwDprGVeTTEkG976HptX2ODtAVt_jxBhUQQ8lP-etYiogfZ-GGV608LYZ3JpNH8WqdwcEo_my7jNaU5pVri_qefu3FzCkXZNl46kx17-aGWuvTVSbuSURdBQ03JbHSuckgtuxxlws3bl1ey1fIdObvIKzcZQb8b6ZZB9s4-DvnmX1SqEowWC0VnwqJMkl5r1A8XxQ6niaLcRygpyIz8O8onCc5BDYqxevFSBh3NdO9D6d6cytktrPaM5-zop2815z4t-JCuJKs4NNGCN5TRWb3XLOEuGJPXAmVQquAXyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ازدحام زائران کربلا در مرز مهران
🔹
مدیر پایانه شهید سلیمانی مرز مهران: روز گذشته بیش از ۱۹ هزار تردد در مرز مهران ثبت شد؛ همچنین امروز تاکنون بیش از ۱۷ هزار تردد در این مرز به ثبت رسیده که این آمار همچنان درحال افزایش است.
🔹
ازدحام ایجادشده در مرز به‌دلیل تراکم جمعیت در پایانهٔ زرباطیهٔ عراق موقتی بوده و روند تردد زائران درحال بازگشت به شرایط عادی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/437849" target="_blank">📅 10:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437848">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌ بیش از ۲۷۰ نماینده در انتخابات هیئت‌رئیسۀ مجلس شرکت کردند
🔸
مجلس در حال حاضر ۲۸۵ نماینده دارد.  @Farsna</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/437848" target="_blank">📅 10:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437847">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قالیباف رئیس‌مجلس ماند
🔹
محمدباقر قالیباف با رأی بالای نمایندگان، برای هفتمین سال متوالی بر صندلی پارلمان تکیه زد و رئیس‌مجلس ماند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/437847" target="_blank">📅 10:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437846">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeeSlvm9D-oiDH5ror8zW4pbaau7I8ASDsn3bwUepgw2b0k-oGl_mDth-Z-E8ksHVQOdChDcctS-ifkOq9spcuLgs4iWvvwD1gPcHCOt3lTFhdy7RQuE3wRy9uPff_j-8UakHcqDotEdGkb1ciaV23N9GJGk6yWyy86rRCyxaKUQC0bkgLMjncnCjPrppcTzdg5YZkGdNdwsOysdcoCrTnxMTdjzTGMyTzThE1VgiojWfAlzWYYwo48vKAgxJg7ncKBPjE18l_HPpOLadQYpAZtZl8ber_QtQTL4MNypIGRIvDCXA1g9aIG07Jql92PSXqZosSF8n_7du6cSljwQPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ انتخابات هیئت‌رئیسه مجلس برگزار شد
🔹
انتخابات هیئت‌رئیسه مجلس که از ساعت ۷:۳۰ صبح امروز آغاز شده بود، دقایقی پیش پایان یافت.
🔹
این انتخابات به‌صورت حضوری و با رای مستقیم نمایندگان برای انتخاب ۱۲ عضو هیئت‌رئیسه شامل یک رئیس، ۲ نایب رئیس، ۶ دبیر و ۳ ناظر برگزار…</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/437846" target="_blank">📅 10:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437845">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ho8Jq-oGy9IxSFS5rkdgMfn_joI4dx5LvGli8sTNZmofGo5cegDrZ1Qbnucf7itVYWx6X_Ha3XOPkWvsCeYYyDRMJYGg4KVDJv7Iy4385_pIt1_p74YCOQ5bfeUQRzKJUL3ItmtjSoMVi4otOLnpCymz77ctweDPAhEDJyiC7PI3_aE3lcKLFPUdjEVeaxVvVluVXfBykU1eSVrLm8O9GdidpdsW8xntrav2IA67dqNqg1QYPth3tIscG9qbA_4Eou9j-xJ5AS2YDFXUA40qDNHukVRVxZzM1IROZ7f4z8oZgnkwXWwgG2mHW-FxFnZOrW6iBjYabyJ2MsfP0SvjdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
احیای بخش جنوبی دریاچۀ ارومیه پس از ۲۰ سال  @Farsna</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/437845" target="_blank">📅 10:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437844">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgWbsDx3T-ipORmRcRaWp8_eWsKcuRRzSmF5RNAQo-DSHiCevrst7EDdDUEic78FgWVk1zic8lzQeIuYQ5iviqz_I3JMqvoDUOkmtuYeIYboaDAnFdWkHzvlrbBNNM8ncbACFvQ5j-g_Tcsf22jiWKp7MMZFEQYq7vFJ8DbL1JXlHjOB3lpQB5J8pdao01cdcvVIhTwfjUDFsNNQTRjyIMQfVy4XakTIBhnY5aSg4Z0m5qEln3h5q3R02bRbIHfUPhJeYXY20hS7mGgD0wGsbuyqqjAZ-jwJ2Xmuy-x-q6lTbyY4gJiEzTFfuoKl2C99vxYECs7NGiwPR6R9EMPsug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناسک حج آغاز شد
🔹
همزمان با فرارسیدن یوم‌الترویه (روز آماده شدن برای آغاز مناسک حج)، فرآیند انتقال زائران حج به عرفات از ساعاتی قبل کلید خورد و مناسک حج تمتع امسال وارد فاز عملیاتی شد.
🔹
۷ هزار زائر اهل سنت کشورمان با اتوبوس‌ها از هتل‌های محل اسکان خود خارج شدند و حدود ۲۳ هزار زائر دیگر هم امروز به مشاعر مقدسه منتقل می‌شوند تا از فردا خود را برای دعای عرفه در صحرای عرفات آماده کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/437844" target="_blank">📅 09:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437843">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpU5X9nqatUDjrgVJyzYVjxf2ocqdCDDN7t2lhRPTDdv20zAn_c2Qwv99O03JaUFauDBnWZMqnw72kG70VrOPcwI9ATDboqm43X76eN_ljAIP2qz7QxUTCqDS3kJRphIigJlxlUmCyG43mBtaDIZZxAZQFKh-taltiCFLXffiuQYFtTgMtHG-AVph-TxngENQZc-v6C_M8D22dLuw4b8kGHlcChDBhWZ015GyxJwuPQhRSyoFvz9R0z_tGJqhFP2j2ws9Tm91NQypdF6G69EnVyfeLc-AtsTZOjw4hnOnDRbxiPu1FJQ7kyarLo1hgOwz6A5VQeZWwnrwn_JB3STvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: در مورد مباحث هسته‌ای تکلیف خیلی روشن است؛ ما عضو NPT هستیم و حق داریم از انرژی هسته‌ای برای مقاصد صلح‌آمیز استفاده کنیم. @Farsna</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/437843" target="_blank">📅 09:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437842">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCzdWE1_0TeoT9wkEi0ErpnC19YCAxXt7iSVkpfuadKL3NE6BllYFtVXLyY0IMnBDDHbKpMArKlnhhRP8bjK1-yLuM-HdVqswW4IlF5PRg4FGBC3ji6l8DgSOiTI_utH01lmHjtjz1tIjDkcZmq6YJD3i3MM-tZVUYOKZekCkjLYKAHs_H1gUYpxHugVQ3pdU_hzhD3XMYKr0dgPhkZK5z13vKcP2C-xdITBnULn_gVmAMY42yWm8dbRL6-hE1rb6kpisKsnbcOboFClkYtaBu4Bfa5JGBoUMCCzvBGi0TYyJoj71Jy9MrqZyhazCppmJ-I5aV8yL9Y_YMPXQodMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرودگاه‌های فعال کشور به عدد ۲۰ رسید
🔹
سخنگوی سازمان هواپیمایی: تاکنون ۲۰ فرودگاه کشور پس از جنگ تحمیلی سوم بازگشایی شده‌اند.
🔹
فرودگاه تبریز نیز تا یک هفتۀ آینده فعالیت خود را از سر می‌گیرد؛ فرودگاهی که به ۹ مقصد خارجی از جمله استانبول، بغداد، دبی، باکو و هامبورگ پرواز دارد.
🔹
فرودگاه‌های مهرآباد، امام خمینی، مشهد، شیراز، اصفهان، اهواز، کرمانشاه، ارومیه و رشت از جمله فرودگاه‌هایی هستند که تاکنون بازگشایی شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/437842" target="_blank">📅 09:50 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437841">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kw4O8JHUKFAibR_TRwWgBgd4y7AYnh1-zUrxgsGbIY-Nf9AdhBoQ1RjJ3iBJIbniseHRVYA4aC5eOGolF-94__9uEtopEeOV3IcmC_SFs11aDV8_ynHwJesC58GOGpuxTRn9a4nfm7Wjhd6iRVUwXNl2bmviMGpWsrnnccXhqCHy9medBEy5tYPP9XoULfx9JO87J7kcbg7ASX2rWRA7BhBbad3xuKppuEs8Uz1bLlx5_oU7l-YezhFVJ-RxGuwymPvWl2ETX_bJSSHxsMQESDXLtcXLs8N40HQjktzlXMP9GK597TXe0EAsltomwSlXlEkAdj02ioCTEo72sTlI8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار قاآنی: مقاومت امروز همچون خرداد سال ۶۱ و ۷۹ زمینه‌ساز آزادی قدس شریف است
.
@Farsna</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/437841" target="_blank">📅 09:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437840">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌ پاپی‌زاده: جلسۀ انتخابات هیئت‌رئیسۀ مجلس فردا حضوری برگزار خواهد شد
🔹
نماینده دزفول در مجلس: نحوۀ رأی‌گیری انتخابات هیئت‌رئیسه به وسیلۀ صندوق‌های رأی‌گیری الکترونیک خواهد بود. نمایندگان احراز هویت می‌شوند و سپس رأی می‌دهند. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/437840" target="_blank">📅 09:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437839">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdjGnyCtVnM1gTnZTwBJ8tshM2s8mzxiCXKymo1-bA9Is15pzwehyupVxkU0YATma7SLydaZSQX3dGmp-HeQUxDyAFZuIAQ1O4xVyn_1GJacJXL0ieS6EbMRM44uv3OK7v_3I1eXFZXWJcjfSwKYNQbWKc76gMTTzMppjvHJ2LXSkHDPVj2X815F7Fzka8WdPRLbsU_6CbhWGXS0NpZ-V4SUN6W1_kf1Gfd3yJHEHhSLkjBHd8_Fdxrb_a2z1J6Q3J1X1gGVk8p7DErY2PFAXUIDf5ChMslE1IQwohBw9SWQcflCgROeY_NK6HKadx4QhGdESLpVSU9YXu3HQcCHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای نامهٔ شبانهٔ وزیر کار دربارهٔ تأمین اجتماعی چه بود؟
🔹
انتشار نامه‌ای از وزیر کار به وزارت اقتصاد از لایحهٔ «ایجاد نظام جدید تأمین اجتماعی» پرده برداشت که ابعاد آن، نگرانی‌های عمیقی را در جامعهٔ کارگری و بازنشستگان ایجاد کرده؛ به‌ویژه آنکه این لایحه بدون اطلاع قبلی و مشارکت نمایندگان کارگران و کارفرمایان در حال پیگیری است.
🔹
براساس این طرح، ساختار مالی تأمین اجتماعی به‌طور بنیادین تغییر می‌کند. بر این اساس، حق بیمهٔ سهم کارفرما از ۲۳ درصد به ۷ درصد کاهش می‌یابد و مجموع سهم پرداختی بیمه‌شده و کارفرما به ۱۴ درصد می‌رسد.
🔹
۱۶ درصد کسری حاصل از این کاهش، قرار است از محل درآمدهای مالیاتی عمومی کشور تأمین شود. همچنین، تجمیع تمام منابع در خزانه‌داری کل کشور و انتقال دارایی‌ها و تعهدات صندوق‌های تابعه از وزارت کار به دولت، محورهای اصلی این لایحه را تشکیل می‌دهد.
🔹
رئیس کانون عالی شوراهای اسلامی کار با انتقاد از فرایند غیرشفافِ تدوین این نامه گفت: هر موضوع مرتبط با حوزهٔ کار و تأمین اجتماعی باید براساس سه‌جانبه‌گرایی و با مشارکت کارگران، کارفرمایان و دولت بررسی شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/437839" target="_blank">📅 08:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437838">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4sI6eYGMEzL2hDUTtc7Tc8gc3qNS46xRGkk6dx3YP0ZUPFa0oHZSkJt3Et-K6C8KAzlTIUEnAavlBYFYGZ_glmHENZwZaBjOMQV5OokhRluP1RLmkgcnlo8MKkqnhS3_7F5KVwZN7DjdzA_xI2GBuORqk9XUsEIqdVk-BimbNp70FxW7mxn1dcELs1VmV3GmfIJOy867bDYAiEmGEj6BpYqd7PBC9fhrBvRrmKf_3AnH-2e47FBiv9QLacIka3dDlXE3N8i9S2kh5B-PJ8djll8PyZus0p0f7vVXeebo_928CZQbmaMdDvsnXZEiSEEeB-GN79-lMtZ4UqAgPYvPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشکنی امارات در تجارت با ایران
🔹
براساس کسب اطلاع خبرنگار فارس از اتاق بازرگانی ایران و پاکستان، این اتاق ضمن تأکید نسبت به‌کندی پروژۀ سی‌پک، از کارشکنی امارات برای جلوگیری از تبدیل بندر گوادر به رقیب دبی خبر داد.
🔹
کریدور سی‌پک که به‌صورت رسمی در سال ۲۰۱۵ و هم‌زمان با سفر شی جین‌پینگ به پاکستان استارت خورده بود با اتصال مناطق مختلف پاکستان به بندر گوادر، یکی از مهم‌ترین پروژه‌های ترانزیتی منطقه محسوب می‌شود؛ پروژه‌ای که می‌تواند ایران را به منطقۀ راهبردی تجارت هند، آسیای میانه و قفقاز تبدیل کند.
🔗
شرح کامل گزارش را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/437838" target="_blank">📅 08:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437837">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0LnUrPyQVspmdhi-PCjKwsLuMVfBTdLP3m5QVAK7YiRu2A9Ll9uNqgcvMctuG3OyI1UUy1uKbUMtmV8STvjnuW9tY_LDmcl2qQ3oaYHgbNwphGudvx8EYQXnV0GG6HQ5RJ-xfAvI6Y3j47Qv8FMlNNI-X7ecijs8Xqp4c6L8WW1A0F8cazkdcQPO5xTC5IXSE-ScFfTSlGtstcsUWXIUKtC26nMQIEALi3btns6tYtGBvj7rP3OwdjhL1NWf2B6rfNfW-zQg9nomT2VYKZrN9_i-kwh_ETgz8Fc8WhvoffnqfAx9SYhouVZSlzlHSigGu4EQrVG5G62kP3kwSmLDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلفات جدید اسرائیل از حمله پهپادی حزب‌الله
🔹
ارتش رژیم صهیونیستی از هلاکت گروهبان ۱۹ ساله «ناهورای لازر» و جراحت شدید یک نظامی دیگر اسرائیلی در نتیجه حمله پهپادی حزب‌الله لبنان به شمال فلسطین اشغالی خبر داد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/437837" target="_blank">📅 07:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437835">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a4c4f1642.mp4?token=R6baeh4OK7nBdf4eAdnl9Gw1nokpjDQYbNixTV9wE6himAP1ygcEinohI9WtTVeT65W7BEfjZlwiC-J-Ttzcu3pA1FtuzByNWne8kz1rHZEOkibcZStx2h0pJFNqH0YHteOuFwT74Ii0VVrs5AuREmyiR6dzFkkqjkSkyRKIsr2qaWb-pkzAYNuhbaa3cNadkvrvkJ2_CF1nn4tWMeBKqnHEIQzZrXVmhXNz0sULGb7hz1VLq5dC56nUxCaXFbIH4maBrUG_ui-ldjx4EkhEChleYAfaijB1ygsHDZc-Nh6ee4Yjkzuj6rv60Z_6TibWOuWQ4yC5vU-ucduFHBfQxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a4c4f1642.mp4?token=R6baeh4OK7nBdf4eAdnl9Gw1nokpjDQYbNixTV9wE6himAP1ygcEinohI9WtTVeT65W7BEfjZlwiC-J-Ttzcu3pA1FtuzByNWne8kz1rHZEOkibcZStx2h0pJFNqH0YHteOuFwT74Ii0VVrs5AuREmyiR6dzFkkqjkSkyRKIsr2qaWb-pkzAYNuhbaa3cNadkvrvkJ2_CF1nn4tWMeBKqnHEIQzZrXVmhXNz0sULGb7hz1VLq5dC56nUxCaXFbIH4maBrUG_ui-ldjx4EkhEChleYAfaijB1ygsHDZc-Nh6ee4Yjkzuj6rv60Z_6TibWOuWQ4yC5vU-ucduFHBfQxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس اکبری، از لیدرهای مسلح کودتای دی‌۱۴۰۴ به سزای اعمالش رسید
🔹
عباس اکبری فیض‌آبادی یکی از لیدرهای مسلح اغتشاشات نائین اصفهان بود که نقش مهمی در حمله به فرمانداری، مراکز تأمین امنیت و مراکز خدماتی این شهرستان داشت.
🔹
او با استفاده از سلاح کلت کمری به‌همراه…</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/437835" target="_blank">📅 07:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437834">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">عباس اکبری، از لیدرهای مسلح کودتای دی‌۱۴۰۴ به سزای اعمالش رسید
🔹
عباس اکبری فیض‌آبادی یکی از لیدرهای مسلح اغتشاشات نائین اصفهان بود که نقش مهمی در حمله به فرمانداری، مراکز تأمین امنیت و مراکز خدماتی این شهرستان داشت.
🔹
او با استفاده از سلاح کلت کمری به‌همراه عدۀ دیگری از اغتشاشگران به فرمانداری نائین حمله و اقدام به شلیک به‌سمت مأموران حافظ امنیت کرده است.
🔹
علاوه برآن براساس اسناد و تصاویر موجود، نامبرده به‌صورت مسلح در خیابان نیز حضور یافته و به‌سمت ماموران تیراندازی کرده است.
🔸
عباس اکبری به اتهام محاربه، تخریب عمدی اموال‌ عمومی به‌قصد مقابله با نظام مقدس جمهوری‌اسلامی ایران و اخلال در نظم و امنیت جامعه، اجتماع و تبانی برای ارتکاب جرم علیه امنیت داخلی کشور محاکمه شد.
🔹
پس از برگزاری جلسات دادگاه و اخذ دفاعیات، با توجه به اعترافات متهم و همچنین فیلم موجود از لحظۀ تیراندازی و گزارش مرجع انتظامی از کشف اسلحه از منزل متهم، بزهکاری عباس اکبری محرز و به اعدام محکوم شد.
🔹
پس از تأیید حکم از سوی دیوان عالی کشور، عباس اکبری فیض‌آبادی فرزند علی صبح امروز به دار مجازات آویخته شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/437834" target="_blank">📅 07:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437833">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تغییر ساعت رسمی کشور دوباره اجرایی می‌شود؟
🔹
اخبار رسیده به فارس حاکی آن است، دولت به‌صورت جدی در حال پیگیری بازگشت تغییر ساعت رسمی کشور برای مدیریت مصرف برق است.
🔹
اگرچه درحال حاضر دولت ساعت کاری ادارات را جلو کشیده، اما وزارت نیرو می‌گوید این اقدام به‌تنهایی کافی نیست و در صورت بازگشت تغییر ساعت رسمی، صرفه‌جویی برق می‌تواند به حدود ۲۰۰۰ مگاوات برسد.
🔸
این در حالی است که مجلس در سال ۱۴۰۱ قانون تغییر ساعت رسمی را لغو کرده بود.
🔗
اما کارشناسان دربارۀ مزایا و معایب این طرح چه می‌گویند؟
اینجا بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/437833" target="_blank">📅 07:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437832">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
مداحی جدید حسین طاهری در میدان انقلاب
🔸
همه‌جا کربلاست، کربلای حسین
🔸
همه ایران شده، جان‌فدای حسین
🔹
ایران کربلاست، ایران کوفه نیست
@Farsna</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/437832" target="_blank">📅 06:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437831">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b3c44c8c.mp4?token=Y1TlXcwscg0HFLpu3Ef-3x3yRq13Dv-XCSnsdtcSLdfIE1e8Lt6VeU1y6agHYHEjUx7obtvAFO145g0p_AYOkjmJF9hS6RkLD1RLQdVio9mJ5vWj0BI8M96k418gQMEaWT_A7lr70U7dJnnDqxWQNOQwWRoD_KGBgpaxDTFodefgZim5xeyuX8KACXHx_OguOImh_xEr6GKSVVosNkSOX_kEwvqVZnDd7vmo1SLS0425XCmswsnAbqzIWxB2RYq9CCN75hfLGZjLt8ZjOdNfMkEG5q_ZFv5HyhG_DoTvWjuROw6gugELC2bS4oNq9HJJWh1W5sajqpRF1jd1XiRLnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b3c44c8c.mp4?token=Y1TlXcwscg0HFLpu3Ef-3x3yRq13Dv-XCSnsdtcSLdfIE1e8Lt6VeU1y6agHYHEjUx7obtvAFO145g0p_AYOkjmJF9hS6RkLD1RLQdVio9mJ5vWj0BI8M96k418gQMEaWT_A7lr70U7dJnnDqxWQNOQwWRoD_KGBgpaxDTFodefgZim5xeyuX8KACXHx_OguOImh_xEr6GKSVVosNkSOX_kEwvqVZnDd7vmo1SLS0425XCmswsnAbqzIWxB2RYq9CCN75hfLGZjLt8ZjOdNfMkEG5q_ZFv5HyhG_DoTvWjuROw6gugELC2bS4oNq9HJJWh1W5sajqpRF1jd1XiRLnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریای مازندران تا فردا مواج، و تعطیل است
🔹
ادارۀ هواشناسی دریایی مازندران: باتوجه به مواج‌شدن دریا، فعالیت‌های قایقرانی، صیادی و گردشگری دریایی تا اواخر فردا سه‌شنبه پنجم خردادماه در دریای مازندران ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/437831" target="_blank">📅 06:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437830">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vuz9Dt82VZ0MsgQ_t0WiGXuWL7TVB5JQJe71-rbVPEemW0p3YMxgjp3C72btVPGMOwIQReMHhZpZW8CeuUKDYgpkw1KA__AnyD8y0JszCFXEOFSYfHWO3SW6n0BjpfsTLBDyFnhA50dVq1Mn6n2AfKN4mRWs_CGSM7GmRNkKi-AeCClIeFWtk8621mxKJHDB55m0VpkBUh8khbUG_z6BAsgQOT55uB4JIsBGKldcwzaJun0DLikgqVn6hURwtbGtxc-2w_paPlVMKbJqGxID7ZgrQP8M-mH4IuksyUQHfv8Hdfw-1kCFhwF4zkTAqWDJ7w_zmK9a-R5QIjrda-xNEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان ثبت‌نام‌های مشکوک در قرعه‌کشی خودرو، با ورود دادستانی
🔹
پس از تکرار گلایه‌های مردمی مبنی بر اختلال‌های مکرر و تکمیل‌ظرفیت برق‌آسای سامانۀ ثبت‌نام خودرو، دادستانی تهران ضمن صدور دستور قضایی برای رفع این مشکلات، خودروسازان را مکلف به برقراری عدالت در عرضه و بازگشت به سازوکار قرعه‌کشی در صورت تداوم شرایط نابرابر کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/437830" target="_blank">📅 06:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437828">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJu8J_nAwdyrwJQg2zwQsc1ICrGrFswU6LWmmpCTcov7mhJ80fhPfVupgb7g2W72MhT4gQQjI-6dA_P0lrWG5qRBDJnSSbjl3aUQeuaZjWyG-DaNKABQ3tzpmrtn-cekU07ratTZ1YDwoqh2vYGOIPK8cClWPktrGRJpKESdTPi2pGjFpeMamRlwhtEmSOMhrOH7V3nSssI6OSpkLd5neMMBMBOWXpWFyhd0SbYvWkwumXKQmgkuHp0PJZx2D9kYvDUgPHEvgBZCMs94kfXDPluESyd2tdkphhJ4n3DeBjvHwmmhiht1CAGT2vVSKhYI2LNaNpJpneyWuNeZY4CX6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو پست مهم استقلال در حالت انتظار
🔹
قرارداد بیژن طاهری، سرپرست استقلال در پایان لیگ امسال به اتمام می‌رسد. اگرچه مدیران این باشگاه نظر مثبتی روی عملکرد طاهری دارند، اما تصمیم‌گیری دربارۀ ادامۀ همکاری با او به بعد از تعیین‌تکلیف سرنوشت لیگ‌برتر موکول شده است.
🔹
تصمیم دربارۀ آیندۀ نیمکت استقلال نیز در زمان مذکور گرفته می‌شود و باید دید مدیران باشگاه در صورت نیمه‌کاره ماندن مسابقات، با سهراب بختیاری‌زاده به کار خود ادامه می‌دهند یا اینکه شخص دیگری را جایگزین خواهند کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/437828" target="_blank">📅 04:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437827">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a6e0f39e1.mp4?token=F9YpAC0xMUp1Ntf-nTlHXU3dltn-1fNnx0YvL1mTKlyV-e-gNTH5RvbwSHp7_nU3vwWywBfOSn1_BYzxIWxxZcH4y5Y4fn1ZepqAFHZ1DSc2SYXJor-d0TXQ00_qg9_1fSvPhFuW-xOGrGePGXXFwXRGHfmLrL2MgygqgHxr-LsNfInT4NPreVjWCGXmG-1791RtIC1Q3omHDT7UDWJKVc7imIAWpmEWOVEYeMF7vQb8LnKnUXnJcDiL9wOq3P8_APh5jrAaPt_05ExupVXyaCXu5Qxh5ueUZ0HDp06vKKt_pMyGMlg7sP2X66-qnTq826PWa_JE4Dhfu2hQ99fjpo9zik5NHe8Utio3FxsMfyl6NOPbLV2UmHr32StfZ_Le-HiTYP2XKVF9EFkK3IBpGYpcwke18BoNUBMjGbfv-8e8VFdr-P6trfDMS4gHVKpp6Gt66y9idbpFmOqPzBHEdUOzKOnLOvwULrJsGToPL2NKUrEGrbRjYls6HE0J-HeWq_qeHHDE4BfJjf7Xjpiuk3tJ7VOaH3WxirCAhBtLXgIVmKquRlAD3mHAwNY9Mzv-tYEJYUH9EujDItwYatOEpw6wf_-jOsrCewKQpRDAdDSRtj1Dcnout_zpj321QDrEB7wEhjS7VLdxnYm9NUjrwwRCdCcbNf7-krNh3qqFBak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a6e0f39e1.mp4?token=F9YpAC0xMUp1Ntf-nTlHXU3dltn-1fNnx0YvL1mTKlyV-e-gNTH5RvbwSHp7_nU3vwWywBfOSn1_BYzxIWxxZcH4y5Y4fn1ZepqAFHZ1DSc2SYXJor-d0TXQ00_qg9_1fSvPhFuW-xOGrGePGXXFwXRGHfmLrL2MgygqgHxr-LsNfInT4NPreVjWCGXmG-1791RtIC1Q3omHDT7UDWJKVc7imIAWpmEWOVEYeMF7vQb8LnKnUXnJcDiL9wOq3P8_APh5jrAaPt_05ExupVXyaCXu5Qxh5ueUZ0HDp06vKKt_pMyGMlg7sP2X66-qnTq826PWa_JE4Dhfu2hQ99fjpo9zik5NHe8Utio3FxsMfyl6NOPbLV2UmHr32StfZ_Le-HiTYP2XKVF9EFkK3IBpGYpcwke18BoNUBMjGbfv-8e8VFdr-P6trfDMS4gHVKpp6Gt66y9idbpFmOqPzBHEdUOzKOnLOvwULrJsGToPL2NKUrEGrbRjYls6HE0J-HeWq_qeHHDE4BfJjf7Xjpiuk3tJ7VOaH3WxirCAhBtLXgIVmKquRlAD3mHAwNY9Mzv-tYEJYUH9EujDItwYatOEpw6wf_-jOsrCewKQpRDAdDSRtj1Dcnout_zpj321QDrEB7wEhjS7VLdxnYm9NUjrwwRCdCcbNf7-krNh3qqFBak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراف مجری‌های «منوتو» به وضعیت فلاکت‌‌بارشان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/437827" target="_blank">📅 04:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437826">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a5c636c7.mp4?token=i_35jKVzmZaMjbBoz8Ge5Y8KzLYQkgDthI5QD_PxHoS9cnneMXhn4A71T9W0Z0WdwxcMT7Jy8r0IOI6rOKja9ftQDWpPBoHDlp7i8o1DnWP13g6yVg_Hecj2Wh_rRafV-DV57a35Lg29hnkkWWCgDG5ZvDih_m999NdW7SHPYk51CJ8-PLiCRg8sRXMkMhOvymy8njdtQ7f9CVJB0dogw0U8b1Uu-XCrn6X-YZ-aA1_yMGjXAvVcJ3AOhD8HGMSFU5BBfo_NWqkvCbe2uqIqk5iT5yi51epJB2yqezpaGXDdXiNSIvZgGlaNQPkIEfxY9dE8bqfVlNg8FQr82146jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a5c636c7.mp4?token=i_35jKVzmZaMjbBoz8Ge5Y8KzLYQkgDthI5QD_PxHoS9cnneMXhn4A71T9W0Z0WdwxcMT7Jy8r0IOI6rOKja9ftQDWpPBoHDlp7i8o1DnWP13g6yVg_Hecj2Wh_rRafV-DV57a35Lg29hnkkWWCgDG5ZvDih_m999NdW7SHPYk51CJ8-PLiCRg8sRXMkMhOvymy8njdtQ7f9CVJB0dogw0U8b1Uu-XCrn6X-YZ-aA1_yMGjXAvVcJ3AOhD8HGMSFU5BBfo_NWqkvCbe2uqIqk5iT5yi51epJB2yqezpaGXDdXiNSIvZgGlaNQPkIEfxY9dE8bqfVlNg8FQr82146jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی مهیب در یک کارخانۀ صنعتی در کالیفرنیا
🔹
رسانه‌های آمریکایی از وقوع یک آتش‌سوزی مهیب در مرکز صنعتی بازیافت لاستیک در شهر لس‌آنجلس خبر داده‌اند.
🔹
دستور «در پناه بمانید» برای ساکنان اطراف صادر شده؛ پلیس خیابان‌های اطراف را مسدود و از رانندگان خواسته از مسیرهای جایگزین تردد کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/437826" target="_blank">📅 04:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437825">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c069109f3d.mp4?token=M8RMz9XBA6B7_ZmNnHL9fGAwb87egReTPK68rQzkfTiW0IxGD5I8RHhsQeJFPMunX3s8cPDtMTzr38JROFiQxoOvO-nm4LjhK-8IjDoz9R9prBp3Ljgl0MaaXRoMRxgkEyWs5-P0QdQPgGDfhksy4OAlhM4tf-Sl0Mvp541saVmEEMV6O_uBvALjkLwnwdi8lrk7lDsHrf66JR0NHvf_orPgEvZAnvB_ezc_kbB1wY2ueto-b4fIcR7gQud_iO2tx-16qNqffw7d2RmeXax48V-6l-F2ze0qmTLFyFLpfUuu-UtW5yja-LR8T0jQ_Woe24ebN_Mlce0erDK4i5WiLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c069109f3d.mp4?token=M8RMz9XBA6B7_ZmNnHL9fGAwb87egReTPK68rQzkfTiW0IxGD5I8RHhsQeJFPMunX3s8cPDtMTzr38JROFiQxoOvO-nm4LjhK-8IjDoz9R9prBp3Ljgl0MaaXRoMRxgkEyWs5-P0QdQPgGDfhksy4OAlhM4tf-Sl0Mvp541saVmEEMV6O_uBvALjkLwnwdi8lrk7lDsHrf66JR0NHvf_orPgEvZAnvB_ezc_kbB1wY2ueto-b4fIcR7gQud_iO2tx-16qNqffw7d2RmeXax48V-6l-F2ze0qmTLFyFLpfUuu-UtW5yja-LR8T0jQ_Woe24ebN_Mlce0erDK4i5WiLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینترنت کدام کشورها به تنگۀ هرمز وابسته است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/437825" target="_blank">📅 03:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437823">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8nJ-YtmGNojH0sASv2sGrTSw6HEm9tpDEItuOkzI5alTYCEIz6cNgp_LbcXsSMSMeveIE_PmUG2PqxP3AZQEwCrH_h0ODhpps54TpMYUktudqCGS-N9KMQS5T8WwMXrMpH6Z5aBLW294sJHUjxinsLTyUdRo6auwKal-LIMBsyVIedyR3OBBGKwwRyS__ltUuc5jIhGc_LU91f2p47bj_8m81OF-HT0mwgPNjEq5xIUOTpAxmZpsZnq_MriEEcTAbnOhNon8p0nvjpvBBG_LRfqFzfuczJs1Jks9khiW33th5Pqad0xmkITmjgj2f1h1XzsMmisEY6dZ3HyaalH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخواست ترامپ برای پیوستن کشورهای عربی به توافق ابراهیم
🔹
آکسیوس گزارش داد، ترامپ در تماس تلفنی اخیر خود با سران منطقه، از آن‌ها خواست به توافق عادی‌سازی با اسرائیل بپیوندند؛ درخواستی که تعجب رهبران عربی حاضر در این تماس‌تلفنی را به دنبال داشته است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/437823" target="_blank">📅 03:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437822">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a91471a6.mp4?token=j5Qua-uNCl5BFarHXAQKsXW6q-qVsor1HhV4a4Odrx25XH8MPC9ej5b-go1s-g6yl5l305NkSvh5k2bnAacXuCtkrBi4_q29mebOTx6Cs0GD6MqWrvVkMQeSIVsPZQQm7h6VoYjzCTHC2Y3wd90CUB2BgOAc0q1w7cRkxzf639lKnh16eCu78tNCBAX255hedzkxVE4o-WVQtIaKOCLCT_VVnK6Xk8Zjfbl_jDBkS8UEUTDlZumqgxcNuatcZONS9jC-8TQ00zARjgB-dBgY_qGsTKgoCMItUBNpn9VXLvgfXc8XjEZDi9sRXPPhoyXj7LxTXAhNHER_hmtQwbFXW3aT_bDggmjJfGyjG9C4GoLV5c2jBpIPveRaMPDUlOb-NIvGExElWGxgnN2gvoxYAExlVlH8fTBfzMeVYJD10br025oWNC8lpE8rArPm9FoBseiviwnVfUvwQVxRfhYL1Co-y82OdFVTtrZBozIE6a1Zmgv-QknbL3V6NeD6QcapLAQZGJaG7qyl0IhNdsCkn5s6KETUiUAAjFFCJn4BPWp1IsLY6akjjUqfdBVJ-IwepJm-HJQ8aLmV6-Gvzf8TqpPw3eoPmaT9vWMLsLeOkonEXzDurnODHOgmS3uzNfH5oqNSwyC5MQBpbaVEd0bJa__TVJx_YUjVjeH6brU5qoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a91471a6.mp4?token=j5Qua-uNCl5BFarHXAQKsXW6q-qVsor1HhV4a4Odrx25XH8MPC9ej5b-go1s-g6yl5l305NkSvh5k2bnAacXuCtkrBi4_q29mebOTx6Cs0GD6MqWrvVkMQeSIVsPZQQm7h6VoYjzCTHC2Y3wd90CUB2BgOAc0q1w7cRkxzf639lKnh16eCu78tNCBAX255hedzkxVE4o-WVQtIaKOCLCT_VVnK6Xk8Zjfbl_jDBkS8UEUTDlZumqgxcNuatcZONS9jC-8TQ00zARjgB-dBgY_qGsTKgoCMItUBNpn9VXLvgfXc8XjEZDi9sRXPPhoyXj7LxTXAhNHER_hmtQwbFXW3aT_bDggmjJfGyjG9C4GoLV5c2jBpIPveRaMPDUlOb-NIvGExElWGxgnN2gvoxYAExlVlH8fTBfzMeVYJD10br025oWNC8lpE8rArPm9FoBseiviwnVfUvwQVxRfhYL1Co-y82OdFVTtrZBozIE6a1Zmgv-QknbL3V6NeD6QcapLAQZGJaG7qyl0IhNdsCkn5s6KETUiUAAjFFCJn4BPWp1IsLY6akjjUqfdBVJ-IwepJm-HJQ8aLmV6-Gvzf8TqpPw3eoPmaT9vWMLsLeOkonEXzDurnODHOgmS3uzNfH5oqNSwyC5MQBpbaVEd0bJa__TVJx_YUjVjeH6brU5qoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جهرمی‌ها همچنان ایستاده در قلب میدان
@Farsna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/437822" target="_blank">📅 02:39 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
