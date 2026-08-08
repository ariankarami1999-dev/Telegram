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
<img src="https://cdn4.telesco.pe/file/N1ksmM6v4ExDRe4-5KDQv2cmX_3UwduZK601kx-mACInKHXSs_teYpIo6VKQ5JlF0kxSyuk0Qfr7DXdXSohCgxaolsoIRpPSIsSrco8L--Xk3V8G-2DSc-FyJTuFec6u5CN7DDHNM1eZnga0mGlQ1Nnupi9_GLHDEBOaMMaG25aJmKHMio-UGGvLwjqJe3c_l_en1n8MD0DWN3XJkgGJqmaAgs38Zg5FHYfxKhEEWgrLQcIT59wDDgs7XEdNSnfWobuwMXvbRtWtnOyFe11UbVd_7002cRwZuF8qqR-ANKOecY3c-qvSItV-4p9HdrwPD9D5uNcWwyvhetyjmQB2_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 130K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 19:23:35</div>
<hr>

<div class="tg-post" id="msg-69747">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5pMvcpPXZ6xc3Vtecdc8qmzFIkBsN7n0w4Wp2iaIk7j0h8KWUFn-FC-9a4WRF4pFEmujlzfZkuN5KKrxinac_7ETv9v8Yu4WWaVcvf-V60gbQQS0fIK4puJGh2CHfuKQ5ij3L-qaJeKpQEXh5jr87X43Jb78TWb-B4Xa5vzXM5tM18yhXzBBA7gEL4b0Y4-z_ZXjjbe1Pw9Wf-pru-Z1j8qLsLQsXKaUgp3Qesj7DNaw91UpYuTe-gAU0EVjWUaFSZA6jzfnmQK-Kx-90miwlp3wb1nbZF05i0k3w47juvKSwTC-IBQWg9xRjhy07tjXznCWk3WQeAXFJDBRJz0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
بیانیه دبیرخانه شورای عالی امنیت ملی:
🔴
اگر ایالات متحده رفتار خود را اصلاح نکند، تنگه هرمز باز نخواهد شد.
اصلاح رفتار به معنای موارد زیر است:
عدم تهدید ایران به هیچ شکلی و به هیچ زبانی، و عدم توهین به مقدسات مردم ایران.
پایان دادن به جنگ و تجاوز علیه ایران و متحدان آن در لبنان، فلسطین، یمن و عراق، برای همیشه.
رفع محاصره دریایی و عقب‌نشینی نیروهای نظامی دریایی و هوایی از اطراف ایران.
پرداخت کامل غرامت خسارات وارده از دو جنگ تجاوزکارانه علیه ایران.
رفع تحریم‌های ظالمانه و غیرقانونی اعمال شده بر مردم ایران.
آزادسازی بدون قید و شرط وجوه مسدود شده و ضبط شده متعلق به مردم ایران.
🔴
اینها مطالبات مردم ایران هستند که در طول ۱۶۰ روز حضور مستمر در میدان‌های جنگ و خیابان‌ها، فریاد زده‌اند.
شورای عالی امنیت ملی هرگز عقب‌نشینی نخواهد کرد، نه در جنگ و نه در مذاکرات.
@News_Hut</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/news_hut/69747" target="_blank">📅 19:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69746">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTDCOUmTlYFGvp1XTMewZes1vRwLvKPzoMI3__aF-32ecigpXBgUWAoZbSJ7HJ9_yjl7oBfUBIUm71SB_6nK6yuQVrzHBppSqiPRm6ZpapFWDhFj3fAgcH1PiNMCjJGauQ5EH9cmPwB0uG4Ref5UZt4ZslOQb1LHSJvUTanrEdGS-7XAydbqVSDT11xcusZRhlPEZVevv2qqZzixDfMm3pxozt3j4iqB-7-RnKKdqs6MSJuktAFrpecBHOeo0MQTHYn8xHAa2RCd3A_4A8nPG-Zrd9HQjSOeocYvu_TH8sF7i3A6iAkwWIGuR2ATFd_p232v0-CK-TD2RBvtrHmDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/news_hut/69746" target="_blank">📅 19:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69744">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJeV5X0CvFOPBYTy9WC5IAP4lPm2j3aA9FMjt19a8m295_1HrfY_CsCOXNBLyC-qmu67V71MglZD-KeKfekd8VjO9e3xxNnRdUAOGP-dcx3ey7tM1WYLaxauioZDCVgHrLOJl2eIhT7rFO9_rca3k9BrceYKQnC128K3hZYCXHCsvSwgmLHjdzn2VME7VHLFluOo00c6TJR8EnZfskpoFJ4YB_U-bP2ZcW_CO-a4z0sObm6Z_-8y1fGvdo9ITjw9dVWl7dwLX6RWu7GWPDyi6kd6m98t6-QYOy3VPilsjRFkAwcNVYYaov3wdH1sUrfzz4cAKV_yYs8NRNQZf6hCFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک تایمز:
ایران فهرستی از خواسته‌ها را ارائه کرد که این موضوع، امیدها را برای بازگشایی تنگه هرمز کمرنگ‌تر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/news_hut/69744" target="_blank">📅 18:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69743">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uT2GkZBXk6oFZyiqllCOEMBoH-8ekMIO4MgO-Y0iMvF7Vww3pMkUGjrMgVir2I_WuLXFGY5TG1dM8lTOs5n20L7kOtO5-NONcbmtMa8QSVDWr8vUyXDqf5DfgWhijr5Xr2ws27IEcpXZaLxBxU2KV5lcsgikolLYgpfgkEOxgoRKmjX1GreBpIfTgDbZNkTrM_YsMowbSgmWudDyxRW3LozzuDNpD-X3Ym3FzWI-BPa6C_30d11lPB3ArXFBRROexQWk38e_ZgogYlRLEI7S-pl9O2Hg7wm3CM6lUJyCdV5fWhjLxV1e5896DiX7nWdqCpiVBo65wfHb_lqPMlnHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان حمل و نقل دریایی بریتانیا (UKMTO):
گزارشی از حادثه‌ای در ۱۸ مایل دریایی شرق خصب، عمان دریافت کرده است.
یک منبع موثق گزارش داده است که یک کشتی مورد اصابت یک پرتابه ناشناخته قرار گرفته که باعث آتش‌سوزی شده و آتش  خاموش شده است.
هیچ گونه آسیب زیست‌محیطی گزارش نشده است. کشتی و خدمه در سلامت گزارش شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/news_hut/69743" target="_blank">📅 18:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69742">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43af7e53e1.mp4?token=OAPg-TlbuyJzaV6vlgfcsNFRH5xvQdq3qYVoc_TpcNQyzdAFIjNixVOCBB-17ncixFbXAke6gC398cRev3H7cQJGtKfzTKIZmqwfMvJQ3OxGVJmrPBK6UZA1tVYoYPSSSJUTltb2fUSpQ5_UBb536E02NwdoaKImEOGkQmpAtBXC227a7H2zZjzK53yJLRE0WLg1xL-5bs1eS1NsoN9Pa69ugRlik2o9vrrrOlsiEX1j4O-zKdRdAyLu1QA9Ztut3xqPu0glPHVJoyE_RZp4N690UxBxbrXbC7MHajWX-v7ZaJtVGMNg34Tk8FEUEbMXB_EOSCzZ5PjZK6wDYHTxJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43af7e53e1.mp4?token=OAPg-TlbuyJzaV6vlgfcsNFRH5xvQdq3qYVoc_TpcNQyzdAFIjNixVOCBB-17ncixFbXAke6gC398cRev3H7cQJGtKfzTKIZmqwfMvJQ3OxGVJmrPBK6UZA1tVYoYPSSSJUTltb2fUSpQ5_UBb536E02NwdoaKImEOGkQmpAtBXC227a7H2zZjzK53yJLRE0WLg1xL-5bs1eS1NsoN9Pa69ugRlik2o9vrrrOlsiEX1j4O-zKdRdAyLu1QA9Ztut3xqPu0glPHVJoyE_RZp4N690UxBxbrXbC7MHajWX-v7ZaJtVGMNg34Tk8FEUEbMXB_EOSCzZ5PjZK6wDYHTxJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبتای یه وکیل مرد:
توی تمام این سال‌ها به این نتیجه رسیدم که نود، برای پسرا معجزه می‌کنه.
پسرا عاشق اینن پارتنرشون بهشون نود بده، اصلا هم براشون مهم نیست کجان، سرکار، خونه و...
من خودم یه بار وسط دادگاه بودم و دوس دخترم برام نود فرستاد، منم گفتم این واقعا محشره، مرسی.
@News_Hut</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/news_hut/69742" target="_blank">📅 18:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69740">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v2uldnpHb595ZAU8PRadbHABeShpnmkKc78I7EBTSfxHpaEGt_IQZE_85xYe_BgfkZUKT1t-_iYGe6OnZVw0FapLYLV6PJ7tWMf8OSmbxks6anjPmUywIkUDga3p0B9kCFblRY3qjPZNdccBIxqM95O9sZEAXfomp9A1B-Zej8VxsNNh4GqFCVoVNPpUSi9cPV6NHJXGbu_QOPg0hIPEqKQOYUgyln-si-gXXnYHzpjfTs7zLIzRwFlWl__hjSKpAvPHTHHY22Lc7q6ELqSN5OYZuxrM1nZhz8nnaEVPc5VyjBnBI6kC_39cCBpBDYoV72cFsEZXtMlNCPgEv2DZoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c7e1449f7f.mp4?token=nMFEg5H2vERTLSDeWXMnKhpV9RzaJMmI8yAMqf3cbc4x1ZHnudUWIKL9724Qrpuviu-7qCpQG2TFMW2cVTObbZNQp8zsp_l0jg-fRP30mNVtaJ0Kmj65pIsTYLyaXXyFzcl08OpueIJIy5pI_KKHqgXoQBQhhycjd0j1DNZWjQ-6nMDAfaI7FGxO1FgtYEy-qffy7zxKZVrSI_pK1MrII22ETVCgYeDn1oMiH5EOkgRFk9EPWeBDpdF6iECuCCVUst1zK68tDumJOlkwtqwqEfrfRjCrRwNvi9VJJYiZjQTf11gepElF_eHS3mU9-NDzGZDKj6Xs2YhAz9X7_BfxhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c7e1449f7f.mp4?token=nMFEg5H2vERTLSDeWXMnKhpV9RzaJMmI8yAMqf3cbc4x1ZHnudUWIKL9724Qrpuviu-7qCpQG2TFMW2cVTObbZNQp8zsp_l0jg-fRP30mNVtaJ0Kmj65pIsTYLyaXXyFzcl08OpueIJIy5pI_KKHqgXoQBQhhycjd0j1DNZWjQ-6nMDAfaI7FGxO1FgtYEy-qffy7zxKZVrSI_pK1MrII22ETVCgYeDn1oMiH5EOkgRFk9EPWeBDpdF6iECuCCVUst1zK68tDumJOlkwtqwqEfrfRjCrRwNvi9VJJYiZjQTf11gepElF_eHS3mU9-NDzGZDKj6Xs2YhAz9X7_BfxhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی اوکراین به دو پالایشگاه نفت در روسیه
پهپادهای اوکراینی بار دیگر پالایشگاه نفت سیزران در استان سامارا را هدف قرار دادند که در پی آن، آتش‌سوزی گسترده‌ای در این پالایشگاه رخ داد.
در حمله‌ای جداگانه نیز پهپادهای اوکراینی به پالایشگاه نفت ایلسکی در منطقه کراسنودار حمله کردند که باعث وقوع آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/news_hut/69740" target="_blank">📅 17:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69739">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6b8444e04.mp4?token=KufL6PitJ2_Cnq6CsGzi7LAvv0neueaQKB0YnM7ZfhDPg5x3jo_XWzyZTn-pdY3fl9vE9XTMEupeuZAglyh7K8hppYb52XpXU0y2HPQuKDbWO2W8RRwVZwnQdMN8GzImh9rzVgIsQqnwTW3IsNGkMzJYzH_nqYxosakzT2APqozBjjTXAkijjdGnVfMs93GJokLtvfwsZP9QeFqb3f5dyuyqSRsj9kWlOgyxkVIY24Ze_VJT6dwoUovdTj2quWupsQGPVIGaIHo7W3GqeW8mBY9GB9IzmKbQmM2u9C6kpv5saZVrVZBLM1mEs9UHUrPz0r_b7TivZS7jB5iI2tOdc4QL-AR89WuqCHziONdAHgMCzsJqiYB17LZaGsghOiRBVlYd8nMPP8Fs9uIaalpgXvQivwN6vcZEkA6QFIv1zLxfzlW2VvaXAPvm6ggxLAQ87kHE9G2_EGJeTRZzNPfyEkMnWXxSAxneZgep27S1XLaPX7G-qZc7V4PR9rjL-29o7exq8gNPEi7ymDAYWgV4nxiewsdVRiSodg0ch7opR6-BC_70llcl4P2OKhqgmu87e9Yq8UGzZimQZknrL8RP7MhX86gzteiYb0brZAd1p-lsnGuehp7iTvmcpirbUpeHB-a0EWpDM0wQe5tLsloMSmOI-wRJb4HLJ5QQSAMipuk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6b8444e04.mp4?token=KufL6PitJ2_Cnq6CsGzi7LAvv0neueaQKB0YnM7ZfhDPg5x3jo_XWzyZTn-pdY3fl9vE9XTMEupeuZAglyh7K8hppYb52XpXU0y2HPQuKDbWO2W8RRwVZwnQdMN8GzImh9rzVgIsQqnwTW3IsNGkMzJYzH_nqYxosakzT2APqozBjjTXAkijjdGnVfMs93GJokLtvfwsZP9QeFqb3f5dyuyqSRsj9kWlOgyxkVIY24Ze_VJT6dwoUovdTj2quWupsQGPVIGaIHo7W3GqeW8mBY9GB9IzmKbQmM2u9C6kpv5saZVrVZBLM1mEs9UHUrPz0r_b7TivZS7jB5iI2tOdc4QL-AR89WuqCHziONdAHgMCzsJqiYB17LZaGsghOiRBVlYd8nMPP8Fs9uIaalpgXvQivwN6vcZEkA6QFIv1zLxfzlW2VvaXAPvm6ggxLAQ87kHE9G2_EGJeTRZzNPfyEkMnWXxSAxneZgep27S1XLaPX7G-qZc7V4PR9rjL-29o7exq8gNPEi7ymDAYWgV4nxiewsdVRiSodg0ch7opR6-BC_70llcl4P2OKhqgmu87e9Yq8UGzZimQZknrL8RP7MhX86gzteiYb0brZAd1p-lsnGuehp7iTvmcpirbUpeHB-a0EWpDM0wQe5tLsloMSmOI-wRJb4HLJ5QQSAMipuk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
تریلر اولین فیلم ساخته شده با هوش مصنوعی
!
فیلم Hell Grind
اولین فیلم بلند سینمایی است که تماماً و بدون دخالت ابزارهای دیگر توسط هوش مصنوعی ساخته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/69739" target="_blank">📅 17:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69738">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9UI60CK1kcB5ihWJlqovHbgu8JciVtZIUUZkxlcL-gB7H5Ox_JWX2Puy1TlaP6kL2fJBSXBDZJxZg2PTpHRPtVTdgn0xPY-bubTBlZgApmyWYh5av8H0s4TyEk8CvNvc5WAsFO7N4k_bGy4_MBlBjnnMgs1W_-lvpbcxUqui4nRoVfLXJ7kjTwyRtYIGblcLyJMj-r8FvXHQxWe2HqPJIDki5EbEy9QkyaidWrDa8uvC8wbXTn3ZmpyudPKFe3eIxak4gn-p4iEAqagNisXGNf9E9xBvZq_tgzB3AIXOS1qEbTYdnuTwFU4Xnt-t4PtBijQi6cHMobr62m6YHUHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇦🇪
طبق گزارش الجزیره، ایران امروز صبح به یک تانکر نفتی دیگر متعلق به امارات متحده عربی حمله کرد.
این چهارمین تانکری است که متعلق به شرکت ملی نفت ابوظبی (ADNOC) است و تنها در این هفته مورد هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/69738" target="_blank">📅 16:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69737">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a24c34d2da.mp4?token=Ly5f1DtoYIJynpFY0NMdTSTEawI2mqj-pVWtRP_lrlv18iH9FAwFVFrP1XOA40TOuqtvXyOTV5xosD8ZfQQPD2eRJ4mgIkFOopGqRssuWqr9sWSRyc53X9VMyFOcH_PAHsCcvci99S7tGVzDB1YzQijJEv3hVfqXWlnYpzaLEPwk5xtq1XjpRgBfiqWFGMK2zF56yHCltzsf0WfI5CZTIb7kS96wsvzSeX8imrTogxBKdmzvnEyukPfoXuWGtId2-rhi_69WIbp_5C27zPp3MnXkvx14dT9Dnthglyh3Sd1hj4fc5XT6mLKj6pewLLCNxkZ6oFaOuicmVmgjGeSXKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a24c34d2da.mp4?token=Ly5f1DtoYIJynpFY0NMdTSTEawI2mqj-pVWtRP_lrlv18iH9FAwFVFrP1XOA40TOuqtvXyOTV5xosD8ZfQQPD2eRJ4mgIkFOopGqRssuWqr9sWSRyc53X9VMyFOcH_PAHsCcvci99S7tGVzDB1YzQijJEv3hVfqXWlnYpzaLEPwk5xtq1XjpRgBfiqWFGMK2zF56yHCltzsf0WfI5CZTIb7kS96wsvzSeX8imrTogxBKdmzvnEyukPfoXuWGtId2-rhi_69WIbp_5C27zPp3MnXkvx14dT9Dnthglyh3Sd1hj4fc5XT6mLKj6pewLLCNxkZ6oFaOuicmVmgjGeSXKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های ظریف درباره سهم ایران از دریای خزر:
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/69737" target="_blank">📅 16:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69736">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a9432f087c.mp4?token=i61hkNvTx9nym-SHioO0D9NxmsAyn-CCEa5iILxqkVdIXspmBZ4QZNcqOzMpneZ1yMi0L9w9-sFX1MTx-3i1cpkCeQJBn9nzBWmGgxKr6I4EhmEjC-ZNZfwYt3URNlIJkMX_6IwBm2mA2TXo8BLBE99Ul5f5hcjesG7qPYCQtWgIU0fELkTB2iaLTrllFuDcP1jKD2rdqJCJG3Fx1fYunbR6Ecuc_iFpH5Z5uOOs3lNMleuAXF1mrxheItWV-8FZug--ZsUQ9zP9Iz7hMfyAuyZuFmraMtqsEOd6UwvSzFot633IUTIvmdDnWcxfmhYJZu7KuByznxM0pGWSVVepoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a9432f087c.mp4?token=i61hkNvTx9nym-SHioO0D9NxmsAyn-CCEa5iILxqkVdIXspmBZ4QZNcqOzMpneZ1yMi0L9w9-sFX1MTx-3i1cpkCeQJBn9nzBWmGgxKr6I4EhmEjC-ZNZfwYt3URNlIJkMX_6IwBm2mA2TXo8BLBE99Ul5f5hcjesG7qPYCQtWgIU0fELkTB2iaLTrllFuDcP1jKD2rdqJCJG3Fx1fYunbR6Ecuc_iFpH5Z5uOOs3lNMleuAXF1mrxheItWV-8FZug--ZsUQ9zP9Iz7hMfyAuyZuFmraMtqsEOd6UwvSzFot633IUTIvmdDnWcxfmhYJZu7KuByznxM0pGWSVVepoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه سکانس از فیلمای قبل انقلاب و داستانِ شب جمعه
😂
اسم فیلم: لج و لجبازی
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/69736" target="_blank">📅 15:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69735">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇷
🔴
⏺
‌وزارت خارجه جمهوری اسلامی : کنوانسیون خزر منافع ایران را از بین نمی‌برد
🇮🇷
معاون وزیر خارجه:
در پی تصمیم برخی کشورهای ساحلی، پای بیگانگان در حال باز شدن به منطقه خزر است.
تصویب کنوانسیون رژیم حقوقی دریای خزر به معنای از دست رفتن منافع ایران نیست.
این کنوانسیون حضور نیروهای مسلح کشورهای غیرساحلی در خزر را ممنوع می‌کند.
تعیین خط مبدأ و حدود بستر و زیر‌بستر ایران موضوعی جداگانه است و در این کنوانسیون تعیین تکلیف نشده است.
به گفته غریب‌آبادی، اجرایی شدن کنوانسیون می‌تواند چارچوب حقوقی و امنیتی خزر را تقویت کند
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/69735" target="_blank">📅 14:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69734">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی سپاه پاسداران:
بازگشایی تنگه هرمز تابع سازوکارها و شرایط تعیین‌شده توسط جمهوری اسلامی ایران است و ارتباطی با مذاکرات ایران و عمان ندارد.
بازگشایی آن منوط به پذیرش کامل شرایط ما از سوی ایالات متحده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/69734" target="_blank">📅 14:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69733">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
قوه قضاییه:
آیت‌الله خرازی به دلیل حرف های کذب و دروغش تحت تعقیب قرار گرفت و براش تشکیل پرونده دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69733" target="_blank">📅 13:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69732">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e778f30e9c.mp4?token=GAglA8eq-bbn1U_DGJL44eV3cICoDvivji29jRBvh-6t2AcvLpPsxNTTjwH4XIw8sGDYO2rKaOfGsPozMfgIq8AmsOFY4j7bUsoCjFDVjl1Bin48gnNfoTlWHpwYSd0gSNdxbc9Bp_RRwtHLJCk_XW4j_FHmoR-d7A0EM4oQO1HsrEsWEKo-hgGHD8i50SspXtKXg71UjNPRRmGZN8bfrPSYp-a_IQBasCZw6EiX0PU-MNT5oP2hnzmPMrr70_888eoIySsrtlJsQ76R47JenCF3x4XdpIgdpwr-kskEi3bpLWhnaOcOPPK3gtcY4xEa2NfL5LfXWJ4Eweu7mybBEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e778f30e9c.mp4?token=GAglA8eq-bbn1U_DGJL44eV3cICoDvivji29jRBvh-6t2AcvLpPsxNTTjwH4XIw8sGDYO2rKaOfGsPozMfgIq8AmsOFY4j7bUsoCjFDVjl1Bin48gnNfoTlWHpwYSd0gSNdxbc9Bp_RRwtHLJCk_XW4j_FHmoR-d7A0EM4oQO1HsrEsWEKo-hgGHD8i50SspXtKXg71UjNPRRmGZN8bfrPSYp-a_IQBasCZw6EiX0PU-MNT5oP2hnzmPMrr70_888eoIySsrtlJsQ76R47JenCF3x4XdpIgdpwr-kskEi3bpLWhnaOcOPPK3gtcY4xEa2NfL5LfXWJ4Eweu7mybBEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مقایسهٔ قیمت های سال 1400 با 1405:
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69732" target="_blank">📅 13:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69731">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhAz8yEww0GaDEqRJrIgULpmGd8AWhvL1vng35faDk0Gayrf17y8kLwxMXBoEDs68_j1-6C_KNwNuD_stBD_On39iZffFTrLetG0vng2t_RGkZeHHhc3wbOJijW0GKQIB7CSY-pDwixjCJLgwWh1YjmvmrUGFa6N-UhoOAAhgh2571tVw-wouf8snU6vlTmcOSwBS9w-MTjXXidL-0-sZUgSmoVmjJbbHfGNWk7RL0dPITAR-zYrSlRtAeYDZGuc9LIg5lJ4iTQx5sGe56ZrJg4q4XkM-39qjKCUfYHw5LZnzEgsX_LUm8_XYf2JyjzlE-bVQWktjmAJnd2YpOqMDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
تعداد زیادی از سوخت‌رسان های آمریکا از ایالات متحده و اروپا در حال حرکت به سمت خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69731" target="_blank">📅 13:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69730">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb80381b74.mp4?token=uPSPLmQUjHHSkt95NdZX5-gCYUXTPH8o-CkgL6rdzPJy5qHkLFwv39sQzBlfiCV5RWf_l5ktcXZaZ9B_UeyDOVr7AsLxJvnSgHLY-ROgcWUEx35ompS8L38s2jscpLc7OlVVMiCZf6IZ7JHtkKpUAlaNtQ_GLpq3akFbC7zqBns9K7wfIdkHSMR_S1kEyeCq76yVhJXgpAs48BfsSqPehqttaK86yzQR-ofzMR-tA2UCCYNiuod0YSp1T26JHtRtkb73SxCXJDmY50SPJfC4kB_7GzDfkMOTfrSVF8lz0Ek9PQGUCJfJip7mvAZymmXGYabs3JCImGrB4DS3II3-Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb80381b74.mp4?token=uPSPLmQUjHHSkt95NdZX5-gCYUXTPH8o-CkgL6rdzPJy5qHkLFwv39sQzBlfiCV5RWf_l5ktcXZaZ9B_UeyDOVr7AsLxJvnSgHLY-ROgcWUEx35ompS8L38s2jscpLc7OlVVMiCZf6IZ7JHtkKpUAlaNtQ_GLpq3akFbC7zqBns9K7wfIdkHSMR_S1kEyeCq76yVhJXgpAs48BfsSqPehqttaK86yzQR-ofzMR-tA2UCCYNiuod0YSp1T26JHtRtkb73SxCXJDmY50SPJfC4kB_7GzDfkMOTfrSVF8lz0Ek9PQGUCJfJip7mvAZymmXGYabs3JCImGrB4DS3II3-Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آخوند
:
قبل از انقلاب باید شب و روز میدویدی تا خودتو خانوادت از گشنگی نمیرید،الان وضع مردم خوبه.
وسط جنگ با ابرقدرت ها واسه خودشون میرن تفریح و در آسایش و آرامش و کاملا شاد هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69730" target="_blank">📅 12:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69729">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce1bb2a9c.mp4?token=Jdpt9Fsm3-KLgXG0CQIzi9hbkbseSRDCKzBZEO0jj_KlXUV0CqtpospkElPMycW5QB5pTJtwcTbSf_3KDrYbWRvrFblSN5YGiPJAlg9BgzwfT9JudiNbxpVkhcbKGP-dNf9vhnItsaV2KaF95uhSkuleEQsuPetSvF-kP4WdM-KSvwepEwckrzq5Le5_BJoMGPUr9uikNnMYYRalWHQH0gqUr7ZY706mLizv4y9PKFJO0sm5N05NB0UKCBEPp08JCvEqaoF8s6RSWWNj_gJBXlkGu6803VeWzcQ40poThWlYEsejnTBJ7BUNO4bInQRIBhe3qTNjUwJt3f5iKI_3CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce1bb2a9c.mp4?token=Jdpt9Fsm3-KLgXG0CQIzi9hbkbseSRDCKzBZEO0jj_KlXUV0CqtpospkElPMycW5QB5pTJtwcTbSf_3KDrYbWRvrFblSN5YGiPJAlg9BgzwfT9JudiNbxpVkhcbKGP-dNf9vhnItsaV2KaF95uhSkuleEQsuPetSvF-kP4WdM-KSvwepEwckrzq5Le5_BJoMGPUr9uikNnMYYRalWHQH0gqUr7ZY706mLizv4y9PKFJO0sm5N05NB0UKCBEPp08JCvEqaoF8s6RSWWNj_gJBXlkGu6803VeWzcQ40poThWlYEsejnTBJ7BUNO4bInQRIBhe3qTNjUwJt3f5iKI_3CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📰
مراد ویسی تحلیلگر ارشداینترنشنال: جنگ جهانی سوم در راهه!
هر چقدر اتفاقات و شرایط رو بررسی میکنم، دقیقا مثلِ قبل از جنگ جهانی اول و دومه.
توافق و تفاهم نامه همش کشکه، هیچکس تو خاورمیانه حاضر نیست سلاحش رو تحویل بده، یه جنگ عظیم و جنگ جهانی سوم در راهه!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69729" target="_blank">📅 11:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69728">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41f0d554f1.mp4?token=e9zCkXpGiMwPvFNkp3Di3uDhP-uzelP2Hc8H_Zmp3QDQ9LyPgOhfhqYQ1-WU-748tYcvDGhfe-cipa6MR-HLWiqIHgnf9N9klTF0isZK1ufgB4C-h_LJNmMCO3YsWrKcX8syukKBxFp0_idpeGTmAOZyibo9arVnO9urFbmVo4xHVi4N2cEvSAYGc18EovwYylifzJSPQueLCyyHGDchaztSXDL5oGvbmkV8pVVKCpRII1X629mC3dqxCYtQFC74Y6ODl5D9-iUoZc1SYE6mEtrf9p83eIyIwegl1kTnmwxqJXE1IL8Fuw8BcHtY3GkPkmzc_QD3-OhqN2E4Qg0GeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41f0d554f1.mp4?token=e9zCkXpGiMwPvFNkp3Di3uDhP-uzelP2Hc8H_Zmp3QDQ9LyPgOhfhqYQ1-WU-748tYcvDGhfe-cipa6MR-HLWiqIHgnf9N9klTF0isZK1ufgB4C-h_LJNmMCO3YsWrKcX8syukKBxFp0_idpeGTmAOZyibo9arVnO9urFbmVo4xHVi4N2cEvSAYGc18EovwYylifzJSPQueLCyyHGDchaztSXDL5oGvbmkV8pVVKCpRII1X629mC3dqxCYtQFC74Y6ODl5D9-iUoZc1SYE6mEtrf9p83eIyIwegl1kTnmwxqJXE1IL8Fuw8BcHtY3GkPkmzc_QD3-OhqN2E4Qg0GeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
نویسنده امریکایی
:
ایران مهم ترین مهره روی صفحه شطرنجه
!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69728" target="_blank">📅 11:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69727">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
نیروهای ویژه دریایی اوکراین از تاریخ ۶ جولای تاکنون، به ۲۱۸ شناور در دریای سیاه و دریای آزوف حمله کرده‌اند. همچنین، بین ۱ تا ۸ آگوست، ۱۲ شناور دیگر از ناوگان سایه مورد هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69727" target="_blank">📅 11:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69726">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69726" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/69726" target="_blank">📅 11:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69725">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7f1c8ee4.mp4?token=uFRb7h44daNApt0qaMuc4mSrDj7TsSUDGMirBsnlAfHSmo6oxPasdxePqezgdJ68VKRpc9sjsDhT_-cEGJSQsFxoKjonM0Cs73bmdXzZ3iXUY5s0rJ2VnVCBNlNRcuTDRIJwWud4UyAUHv0IspIS7AGcvOx1wfGJRQFywidjMxTkd8v967FTKPS8DPrK70pPw1NU-2hFLvnuYPecMjv5BucfRvlwo2vxBv2V053Xl_pnC1-H3Cmkibg6-hjVU7aP1z3SVUBLBF6WDmry_HY-7ZT0qpXj1-XdNFm0xS42AOcT3n9HayzT2zRzmWLw-ZPraypb3uycSM2uOzEYlH80hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7f1c8ee4.mp4?token=uFRb7h44daNApt0qaMuc4mSrDj7TsSUDGMirBsnlAfHSmo6oxPasdxePqezgdJ68VKRpc9sjsDhT_-cEGJSQsFxoKjonM0Cs73bmdXzZ3iXUY5s0rJ2VnVCBNlNRcuTDRIJwWud4UyAUHv0IspIS7AGcvOx1wfGJRQFywidjMxTkd8v967FTKPS8DPrK70pPw1NU-2hFLvnuYPecMjv5BucfRvlwo2vxBv2V053Xl_pnC1-H3Cmkibg6-hjVU7aP1z3SVUBLBF6WDmry_HY-7ZT0qpXj1-XdNFm0xS42AOcT3n9HayzT2zRzmWLw-ZPraypb3uycSM2uOzEYlH80hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
اگر
#تندو
تیز هستی اینو ببین
💵
💰
✊
این بازی فقط سرعت عمل بالا میخواد
😍
🟢
ویدیو
#آموزش
بازی AVI رو براتون گذاشتم خیلی راحت با سرعت عمل بالا بدون ریسک کلی پول دراورد به همراه
🤩
🤩
% شارژ اضافی
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r17
@betinjabet</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/69725" target="_blank">📅 11:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69721">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dab2dda1d.mp4?token=vwF_Xor32mH2OHLQ4ybPM3FAqdnJdBzDw5DapfZT3x3FIkieOMfPX7N9D-5ISI6OmkM7yeYLWicqo1exEUTXwZocM3osNxd8hPHAnBOVzgw1eiiqJ7YZA3kxYHuhPbjgR9bTFAkjHx7FwkfRYvYG83hG-SXFQ4r8CjGy-OjX3ukepRQzKFRsFisrj6NG1-WNSTkng8kKHvGe-6a35Jv-EoV2qiptmXqDk47crUHN2TTFHMrWI1u6AjMxwCZl70q7E9R3Dold1l5iFaG-Q_F9NFCGmYbD3B9NJfJzg1JQzdqX1sbAfAxPEphnaHQL0GcA9AoEiy2Cz_eiQQkSEc1E5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dab2dda1d.mp4?token=vwF_Xor32mH2OHLQ4ybPM3FAqdnJdBzDw5DapfZT3x3FIkieOMfPX7N9D-5ISI6OmkM7yeYLWicqo1exEUTXwZocM3osNxd8hPHAnBOVzgw1eiiqJ7YZA3kxYHuhPbjgR9bTFAkjHx7FwkfRYvYG83hG-SXFQ4r8CjGy-OjX3ukepRQzKFRsFisrj6NG1-WNSTkng8kKHvGe-6a35Jv-EoV2qiptmXqDk47crUHN2TTFHMrWI1u6AjMxwCZl70q7E9R3Dold1l5iFaG-Q_F9NFCGmYbD3B9NJfJzg1JQzdqX1sbAfAxPEphnaHQL0GcA9AoEiy2Cz_eiQQkSEc1E5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این روزها قبل از ورود به هر بالا پشت بومی، سعی کنید در بزنيد؛
چون قطعا یکی اونجا هست که داره سعی میکنه سیاه بشه
😔
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69721" target="_blank">📅 11:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69720">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aa229942a.mp4?token=drK5-vGhqO7Cfb675wGFjhf4h8cetMRUOxqA1X_CLJPrkOfruWd4abaGwy86OtJQMp6vc1xdrtZ0QDhhN8mLGtZCHryuJlNGByG92ZKfRZ2Fi5rWI6IzAVXQgYVcW4trysR2EBlk60t2XIJUKw7VwHe3jHJdp6b20S4Jz0-lVXGuYr_HYC2ZZnD7M0i2tPebERysLGFjmaCwcmqlGVJzQpo_7GWoMeuFqdsab2NPgzZRQhYkMWn7FqlxGzJXXZs2JreHsfh2etdQjUg6-0LNjoxSm5lA9aIW1d04WYCNNisMFvwvSKlBYaw0lrE3sqxXESK_BSnhNfmnrfEp1cIB0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aa229942a.mp4?token=drK5-vGhqO7Cfb675wGFjhf4h8cetMRUOxqA1X_CLJPrkOfruWd4abaGwy86OtJQMp6vc1xdrtZ0QDhhN8mLGtZCHryuJlNGByG92ZKfRZ2Fi5rWI6IzAVXQgYVcW4trysR2EBlk60t2XIJUKw7VwHe3jHJdp6b20S4Jz0-lVXGuYr_HYC2ZZnD7M0i2tPebERysLGFjmaCwcmqlGVJzQpo_7GWoMeuFqdsab2NPgzZRQhYkMWn7FqlxGzJXXZs2JreHsfh2etdQjUg6-0LNjoxSm5lA9aIW1d04WYCNNisMFvwvSKlBYaw0lrE3sqxXESK_BSnhNfmnrfEp1cIB0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، (مرداد1397):
همه ما انتظار داشتیم ایران درخواست پنجاه درصد بکند. قانونی هم بود.
اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین پنج کشور، یعنی کمتر از بیست درصد.
برای ما عجیب‌ و غریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69720" target="_blank">📅 10:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69719">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrL6m8V-CaNsOJrtZFpNG6QcxFsFG3_z0-N72O8OWgwfwOVHftex0wU4YuIP-B7l0HynAELmfu2-u-j1SJrXN1hE88FjSJzKRjGYH8EmDs4Q86gwpR6TFSz5arcDzOS1LFO6iQ063-BI_-R3_mFif__JrmiBEzVpFMPG1eRyRPRZGglBPRj-GSHs3PzhDMtBzxjA-F4vFClGRgmwbMbb8IGwQb8C3Q_r7hkZyILxdZhw12ovcGDbUEBsCS7ZWLh0637d4n0-IeSUQYvj-wdHAcugPgWyJY7LULV4e947d0mYx6I2yoK2-0xxRgTZM-n-cWsrxjAvQx1IQveBRtBrrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه ساعاتی قبل یک کشتی دیگه رو توی تنگه هرمز هدف قرار داده؛
گزارش‌ها حاکی از آن است که ایران به کشتی‌ای در تنگه هرمز و نزدیکی سواحل عمان که قصد عبور بدون مجوز را داشت، حمله کرد
ه
است.
یک شناور تخصصی که برای مقابله با نشت نفت و اطفای حریق طراحی شده، در منطقه‌ای که نفتکش هدف قرار گرفته، در حال فعالیت است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69719" target="_blank">📅 10:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69718">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9bc484b9d.mp4?token=HaNcBq4n2XvlYiW7Pf6cqadCziCMKKnD-H3mBiikyJbzlliRhFG_Tf8Mwoy-F9rEV1ZwlrmryBtXGqmhHFPpKbmCyWS9CjxKIHbHpNHn0uDf55o_mISqPwaKa_4tq6rtGK8yHUdNwY2vE6CWwkMTjBceJSrcbGrESlbVrkcXHp5UjHtYAVqsqWnZR5vl7YcB5Sxbbz3gW_04QBPo7blI3ZHnDIqEi7-xqGKZTHKx1Gav4xzXhoVmY6TYIMW7nJ-vuMYLxNpNp-u_JpdFugo_mcWIiK2JWeQMgqZXITV3bdQkPvj06khw5h4xHy06h-fI99gBFYUwFSh9iGwrEEqm0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9bc484b9d.mp4?token=HaNcBq4n2XvlYiW7Pf6cqadCziCMKKnD-H3mBiikyJbzlliRhFG_Tf8Mwoy-F9rEV1ZwlrmryBtXGqmhHFPpKbmCyWS9CjxKIHbHpNHn0uDf55o_mISqPwaKa_4tq6rtGK8yHUdNwY2vE6CWwkMTjBceJSrcbGrESlbVrkcXHp5UjHtYAVqsqWnZR5vl7YcB5Sxbbz3gW_04QBPo7blI3ZHnDIqEi7-xqGKZTHKx1Gav4xzXhoVmY6TYIMW7nJ-vuMYLxNpNp-u_JpdFugo_mcWIiK2JWeQMgqZXITV3bdQkPvj06khw5h4xHy06h-fI99gBFYUwFSh9iGwrEEqm0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادمهر عقیلی، قطعه‌ی گل یاس از البوم مسافر رو که سال 1377 منتشر کرده بود، بعد از 28 سال دوباره بازخوانی کرد و تو اینستاگرام منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69718" target="_blank">📅 09:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69717">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0959732695.mp4?token=Qnb1W-fuwYEZX7U4VKrj4BvOJC1TsKnp3EfbYI0K4E-Dd2mqCJiJ9gUIRGCE_I1gSdwXMDiUDmMAV3iKH80Sg1YxIqWZV8INzX9I9TafTMx3SPodtuApZHQ5MKQdHriBx2BqYgIc_vukqZPN0AnUTpDBGzJ-qSyjMW0B64qxJ5oDU-9kGOTgOPNAghIUqodUmHP9CoNWLig525RjwT2Vqd-D3mcFM-X3NnHtPVdQpkH-7UGqhFtw7Ah9TyiV8dk8uC-b4K2rjc4gAIM7oIy4NWoV_K09GL9KShExc2GIn0njlItVZKeZszzl768cT-tHPRuNB2fwKbLWDTREJrA_SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0959732695.mp4?token=Qnb1W-fuwYEZX7U4VKrj4BvOJC1TsKnp3EfbYI0K4E-Dd2mqCJiJ9gUIRGCE_I1gSdwXMDiUDmMAV3iKH80Sg1YxIqWZV8INzX9I9TafTMx3SPodtuApZHQ5MKQdHriBx2BqYgIc_vukqZPN0AnUTpDBGzJ-qSyjMW0B64qxJ5oDU-9kGOTgOPNAghIUqodUmHP9CoNWLig525RjwT2Vqd-D3mcFM-X3NnHtPVdQpkH-7UGqhFtw7Ah9TyiV8dk8uC-b4K2rjc4gAIM7oIy4NWoV_K09GL9KShExc2GIn0njlItVZKeZszzl768cT-tHPRuNB2fwKbLWDTREJrA_SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مسعود پزشکیان:
تا وقتی میشه حرف زد چرا جنگ؟
ما با همین گفت و گو تونستیم جلوی جنگ لبنان رو بگیریم. (اسرائیل از همون موقع تا الان تقریبا هر روز داره لبنان رو میزنه).
تونستیم محاصره رو برداریم. (ایران درحال حاضر تحت محاصره دریاییه)
تونستیم پول‌هامون رو برگردونیم. (هیچ پولی از پول‌های بلوکه شده به کشور برنگشت)
تونستیم قسمتی از تحریم‌ها رو حذف کنیم! (درحال حاضر تحریم ها بیشتر از قبل جنگ شده)
بعضی‌ها تو داخل کشور فقط میخوان که ما بجنگیم
،
اتفاقا اسرائیل هم همین رو میخواد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69717" target="_blank">📅 09:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69716">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👑
آخرین مصاحبه شاهنشاه آریامهر محمدرضا پهلوی با دیوید فراست (پاناما1980) زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69716" target="_blank">📅 09:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69715">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69715" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#گل_با_پوچ
راحترین بازی پولساز
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید راحتو سریع برنده شو
👌🏼
💖
مرجع
بازی های روز دنیا در ‌پلتفرم جهانی بت اینجا
⭐</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69715" target="_blank">📅 02:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69714">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15f45ab1f.mp4?token=DSM86AO-M3rmbnMIX7zQ7YBeEyeQNZMgmRwsarxqU2MCAp7wyFjkOAbH7NeF9mBJlVQx8xrnt-QheagQsTK_ORfNoynXbcmMyUC70S_QW9aYAPvgJ3ItMCuiqXrssLWYvkZzdfqEx8koHl8T5mxJbjwlBdLMpo1eC8Y2T6KcEppc8WQgsYQ6aoCDNwAr7G9M28K0PK8yAW68MDwH1gTYzD7DMcztJrSLvvcenv_WF8IXsUm4pvPsKxUzSXNSmpemH3fXZqExDxx42GFCNAcB00msl5SexlbCavlEhb5hFnMam36m34UFmA9z1whM_DLz01tnhFckL7fP_RZb2iRDSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15f45ab1f.mp4?token=DSM86AO-M3rmbnMIX7zQ7YBeEyeQNZMgmRwsarxqU2MCAp7wyFjkOAbH7NeF9mBJlVQx8xrnt-QheagQsTK_ORfNoynXbcmMyUC70S_QW9aYAPvgJ3ItMCuiqXrssLWYvkZzdfqEx8koHl8T5mxJbjwlBdLMpo1eC8Y2T6KcEppc8WQgsYQ6aoCDNwAr7G9M28K0PK8yAW68MDwH1gTYzD7DMcztJrSLvvcenv_WF8IXsUm4pvPsKxUzSXNSmpemH3fXZqExDxx42GFCNAcB00msl5SexlbCavlEhb5hFnMam36m34UFmA9z1whM_DLz01tnhFckL7fP_RZb2iRDSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
#آموزش
گل یا پوچ آنلاین با افراد واقعی
🟢
حتما وبدیو آموزشی رو‌تا انتها ببنید راحتتربن بازی پولساز بدون ریسک و بدون پول گل یا پوچ بازی کن
با هر شارژ
2️⃣
1️⃣
🔣
موجودی خالص میگیری و با موجودی اضافیت میتونی کلی پول دربیاری
🔥
💻
آدرس سایت مورد
#‌اعتماد
ما:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a16
@betinjabet</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69714" target="_blank">📅 02:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69713">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuzVkoDWEfDilmB4Pj6zAuDQk8s5TU-5K4HbLhdfXA8EI1FIRC2l5fsn3sVZfsfaWhWhLcZVXe9viT2A3M2WL2G9aptUoZDCmQJDNwiDCB-YiISbx1IckdOdB4sRiUAbjDOLkwrD4iE1LPVAfAY1c2jpl7a8CcXHQBfkxJ2vCWioVDEotKY34iGlH-eJmKSaUzU0B2tI8AbM_V3ktsaLMEH0Mhm1ay7mQiwvy7yStLFof_fJlwVAKXxCXrT82CgBG5AqPA5Dlo19pf6n79LG94Tl4XYjIo7FjYQ4vHRlvpxHiFdhlkT0uRpdVC9CwfaTTUw6Jqg-rzZz-lTL1tKSiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت لارا لومر در جواب قالیباف:
"جمهوری اسلامی رئیس جمهور ترامپ را مسخره می‌کند!"
یادآوری روزانه شما مبنی بر اینکه مسلمانان بازیگران بدذات هستند و نمیشود با آنها مذاکره کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69713" target="_blank">📅 01:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69712">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66931f1c30.mp4?token=EsexIXqcAgjg0wI1wh-JIStYU2cxmBt0yukWhMsxHjSmp9zkAM6lUT8U9Z9wlRw6qfQTHsH-g_8ARYLLwgF-lvFP4AM-RUVjUdtFZlhuqreOmwR6hJbzrUdIN5ew_nKEwn3essA151lzSeyMr2D2gpBCgJZvweYpPrXXZfJtLoSX_-96QIzLrEbVV2Q0cZ8E4ZNR8aeQvOGO5gYJ7Hb5Mcq9GR08jmLNpBOk0RY-lhX273fNLP4NFOyvt9iWEN4RZ3JWSIooLY7aJtzQp0dPgRACMaS0I0CT86QpYfk9pS6uciSiUQA8kWVuoBNfXaUlSoum0RSAo7cOngssz5GBwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66931f1c30.mp4?token=EsexIXqcAgjg0wI1wh-JIStYU2cxmBt0yukWhMsxHjSmp9zkAM6lUT8U9Z9wlRw6qfQTHsH-g_8ARYLLwgF-lvFP4AM-RUVjUdtFZlhuqreOmwR6hJbzrUdIN5ew_nKEwn3essA151lzSeyMr2D2gpBCgJZvweYpPrXXZfJtLoSX_-96QIzLrEbVV2Q0cZ8E4ZNR8aeQvOGO5gYJ7Hb5Mcq9GR08jmLNpBOk0RY-lhX273fNLP4NFOyvt9iWEN4RZ3JWSIooLY7aJtzQp0dPgRACMaS0I0CT86QpYfk9pS6uciSiUQA8kWVuoBNfXaUlSoum0RSAo7cOngssz5GBwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مسعود پزشکیان:
ما هیچ امتیازی به آمریکا ندادیم!
آمریکا به تعهداتش عمل نمی‌کنه؟ خب اون موقع ما هم نمی‌کنیم.
تو جلسه شورای امنیت، 12 نفر از 13 نفر از این توافق دفاع کردن و رای دادن، چرا؟ چون منطق و عقل اینو حکم می‌کنه.
کسی که نمی‌فهمه همینجوری میگه بزن! خب این تبعات داره...
من از شهادت نمی‌ترسم که هیچ، واسم افتخارم هست ولی اینکه نتونم مشکل مردم رو حل کنم، واسم قابل قبول نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69712" target="_blank">📅 00:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69711">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372d7e9f3e.mp4?token=E_kPmRbU8mhyNUMPdm3AvMAjOoJwmSsIyMyM_kl3AgsoIkeqiMvNt_ZPo9BCegncEBof0BkhzwlUMHGuu1prQN_grNq3w84ZsqsyQSveUDRhOaFt_Tatt4GcKzwO40VJZIwG0Ediy5SSY9t8C_NNpLubWO6mFbyP7ZngfRXWyIIeqWSOUVgHPLhNTozuKPkCF_aU2qMM36C6Xq1qp6K5MNG7SE3zyF79ewtigPfBhPxFTe2_erw8miG_qZNY5IReJ4hPcmTgaLILNxl6uVUkCswrMeI-KHnzoTwMwfmsgoO6Kx8FygtgT81i6rQTDNIjgvVlejyrcJi1KlkAcBp4SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372d7e9f3e.mp4?token=E_kPmRbU8mhyNUMPdm3AvMAjOoJwmSsIyMyM_kl3AgsoIkeqiMvNt_ZPo9BCegncEBof0BkhzwlUMHGuu1prQN_grNq3w84ZsqsyQSveUDRhOaFt_Tatt4GcKzwO40VJZIwG0Ediy5SSY9t8C_NNpLubWO6mFbyP7ZngfRXWyIIeqWSOUVgHPLhNTozuKPkCF_aU2qMM36C6Xq1qp6K5MNG7SE3zyF79ewtigPfBhPxFTe2_erw8miG_qZNY5IReJ4hPcmTgaLILNxl6uVUkCswrMeI-KHnzoTwMwfmsgoO6Kx8FygtgT81i6rQTDNIjgvVlejyrcJi1KlkAcBp4SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ارژنگ امیرفضلی
:
بالا برید پایین بیاید، برید چپ برید راست، مذاکره کنید جنگ کنید نکنید:
🔻
هیچ چیزی به قبل از ۱۸ و ۱۹ دی برنمیگرده
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69711" target="_blank">📅 00:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69710">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇺🇸
ترامپ در گفتگو با خبرنگاران:
ما افراد بسیار زیادی داریم، اگر بخواهم درباره همه صحبت کنم، تمام روز طول می‌کشد.
اگر بتوانید به سرعت سوالات خود را مطرح کنید، از شما سپاسگزار خواهم بود، زیرا ما یک جنگ را پیش می‌بریم، متوجه هستید؟
این عذری است که من برای ترک این جلسه کمی زودتر ارائه می‌دهم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69710" target="_blank">📅 00:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69708">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4300472.mp4?token=QE4QTXHqbFX0Zkw5dqgT58gCvKU9tsR0l0HhoosmJQIFmkzs8lve4_MD_-i3qkenvMa2GrTG6zErwoJpg1vzAcn8L96yGEmmANd6AO892rTiX1O58j9z3zfhjS5N0QEm04_d4vYlOSXgHDKeQGp-RO0mTTRERcKpzh0ffMcrXT3xYAh2rps6k_KaCYc3OSZwYqkos9Kz2ARCjs3WYxys3PhJh9KZfI9czZCU_HNUwZm_-QfpUXpSL8iMQlcqYIczcw-RLz6LkuPtglgisOM5zFYPqFUCjSh85BxCR_dMtQsjVr_eW3bAbAp68AkYUO2h74-Yy8Kmnz1bgrYQKsc60g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4300472.mp4?token=QE4QTXHqbFX0Zkw5dqgT58gCvKU9tsR0l0HhoosmJQIFmkzs8lve4_MD_-i3qkenvMa2GrTG6zErwoJpg1vzAcn8L96yGEmmANd6AO892rTiX1O58j9z3zfhjS5N0QEm04_d4vYlOSXgHDKeQGp-RO0mTTRERcKpzh0ffMcrXT3xYAh2rps6k_KaCYc3OSZwYqkos9Kz2ARCjs3WYxys3PhJh9KZfI9czZCU_HNUwZm_-QfpUXpSL8iMQlcqYIczcw-RLz6LkuPtglgisOM5zFYPqFUCjSh85BxCR_dMtQsjVr_eW3bAbAp68AkYUO2h74-Yy8Kmnz1bgrYQKsc60g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خرازی(برادر زن مسعود خامنه‌ای):
فتوا میدم بی حجاب هارو بکشید اصلا رحمی نکنید
.
هرکی خواست مقابله بکنه اونارم بکشید
.
این دولت شیطانیه اینارو هم جلو اومدن بکشید
.
این دولت شیطانی شده زیر نظر آمریکا ما باید به حکومت اسلامی سابق برگردیم
.
اسلام همینه باید ضربه بزنیم و ضربه رو دریافت کنیم
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69708" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69707">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a717b4bbc3.mp4?token=uaqSaqfwvoB0ywwUUYF1ZkFAIHs9YhGahY4aCOw6q2z95IjKLRamzwS5ucwGY1aVaZ7Izs8eRRXSyof8YYu7kVsMoaBKOFYVDHyxRWw6WKjUJkTYlrj4bha30_G6XXwlgLarhOpn--lnFhprl2FbMvlK0aoPwRwbJ7qvZTeB4lY4esV_IxHckd03xgcpjCaXETWnW7JmOwKoJlVEVWpCOC2D12FearfqLljQ3_ONhu-tpgV_qyKSLOdKBurnkEqWd9mssIZya5AI93FdkpoBxemmBsbKXspOBskrn06oGTL-dre-DYN_6UnTnXA-00iVmtKahIMPle73--EUH9_UEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a717b4bbc3.mp4?token=uaqSaqfwvoB0ywwUUYF1ZkFAIHs9YhGahY4aCOw6q2z95IjKLRamzwS5ucwGY1aVaZ7Izs8eRRXSyof8YYu7kVsMoaBKOFYVDHyxRWw6WKjUJkTYlrj4bha30_G6XXwlgLarhOpn--lnFhprl2FbMvlK0aoPwRwbJ7qvZTeB4lY4esV_IxHckd03xgcpjCaXETWnW7JmOwKoJlVEVWpCOC2D12FearfqLljQ3_ONhu-tpgV_qyKSLOdKBurnkEqWd9mssIZya5AI93FdkpoBxemmBsbKXspOBskrn06oGTL-dre-DYN_6UnTnXA-00iVmtKahIMPle73--EUH9_UEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تحلیل جدید محمد باقر خرازی از حمله مسلمانان به هند و چین در آینده:
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69707" target="_blank">📅 23:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69706">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6ea65bf65c.mp4?token=dZbdWULbMCbiZM-4FQCjoxGOTUVUW4-fQFdhpUEgv4n6Bkng197O3pQ3GxWPerqYUhTd8khRVS55cN594CH4nz4DTjtX1GCJ7bNX-LGaSesB_zyU1V1PY30s_LIAgS1Z085DLa4aF1UKiUYV7E9wRXkM5IOQ1O3U_RsLh9McZdA_dTKdjXY6xZx7G-YWnkfN2AINWo8afdlKLEPy4pgz7O595X1EkPoCDMUbSnmgggkcA2ljQr10BbWbGjFifiQEPAu2PYLUtcGlzETRFcWH90moj5riww7VHJ26W2Er6dFmCSNPavDFmuTa_Nr7Pcr3O6lotwAAJtkRNfDT0l21QA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6ea65bf65c.mp4?token=dZbdWULbMCbiZM-4FQCjoxGOTUVUW4-fQFdhpUEgv4n6Bkng197O3pQ3GxWPerqYUhTd8khRVS55cN594CH4nz4DTjtX1GCJ7bNX-LGaSesB_zyU1V1PY30s_LIAgS1Z085DLa4aF1UKiUYV7E9wRXkM5IOQ1O3U_RsLh9McZdA_dTKdjXY6xZx7G-YWnkfN2AINWo8afdlKLEPy4pgz7O595X1EkPoCDMUbSnmgggkcA2ljQr10BbWbGjFifiQEPAu2PYLUtcGlzETRFcWH90moj5riww7VHJ26W2Er6dFmCSNPavDFmuTa_Nr7Pcr3O6lotwAAJtkRNfDT0l21QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
یکی از قشنگ‌ترین ویدیوهایی که درباره توصیف وضعیت جامعه در حال وایرال شدنه:
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69706" target="_blank">📅 22:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69705">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rjgx9s1bkMnwU20q-Rwqx0maOzR4P8PHAfIMCxQgrjCnvWj7X5XvkrCK6PqInVel-mY0O5scuZEliT4CB0wBuFdIUsEksebTxhwEbqTcpD11WP4UsxCccrR5uUFzrULe2AKehaB9zkls7fdy9yWhjtEfFstfywQ-cOcp-PF4ZRa4Yl7EF5bOftj_7PNWkb8qFuEStAxvswDiWTJ8a6lK8xAzUX53QQhBM84wbVRTq_9tuo4_T3Iu_daCNCAWwiG1_s9PgEcZZEh5l9GAKUn8RyZfU76gX4-Rkf8KIr3eWqhdor1g-QX8Ug4UZTW9H8oJYZUngz6wLXKdIHDDtwPUHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عباس عراقچی:
نیروهای مسلح قدرتمند ایران امادگی و اقتدار خودشونو درباره بهترین ارتش جهان نشون دادن
هنگامی ک مسلمون ها کنار هم متحد باشن میتونن درباره هرچالشی از بیگانه با قدرت و قاطعیت ایستادگی بکنن
زمانش فرا رسیده که تنها بخودمون متکی باشیم و برادری واقعی رو در پیش بگیریم
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69705" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69704">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">6 شب و 6 برد پشت هم
✅
من به پول هیچکدومتون نیاز ندارم و قرار نیست چیزی بهتون بفروشم  آماری رو رقم زدم که حتی تازه وارد هم میفهمه این آمار کار هرکس نیست
🚀
g16 https://t.me/+5fvta-uF4QA3ZDY0 https://t.me/+5fvta-uF4QA3ZDY0</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69704" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69703">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NK62Cm5m_Ocxc9PXwDCR_C82eomyO5QBCc7ebWXsFDQQwIiApm2IbdhXq-5Y-r8rub_Dosbi_8QW_UwLpUJeJwAKIeQCEjCFn0EgypQ8z8ChsxIE7GX2MJ4J39jf5Xgs-F6FRwU95TcXaQrK12sOyWsieslzDownuug7gcLmnXqqS9Isg5HT4mbJLRcQiZANUqV--8_NpDI9-v0Kd6rdHALRhJAcQVEpo_kUWbF8No04gX_689QpbTIbLCSmeK90af0FoxORh_ggNagemzfb_8nYlr66_KmKXBtXEytZyrd4N_xEC9qMhDuE3thVzHJNy0aDiTMsQX6TltAYYIhUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6 شب و 6 برد پشت هم
✅
من به پول هیچکدومتون نیاز ندارم و قرار نیست چیزی بهتون بفروشم
آماری رو رقم زدم که حتی تازه وارد هم میفهمه این آمار کار هرکس نیست
🚀
g16
https://t.me/+5fvta-uF4QA3ZDY0
https://t.me/+5fvta-uF4QA3ZDY0</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69703" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69702">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfaWTedRqFC4MCIzyqjpstJL_Z492mn3iGPMCZ4tKYSD-iMwPCpHqp1rmbMtAlhbScERvrC13XU1DU8AF0CzIdJGzR25NvuY1bqfr6xp1UaDSnWcnuBx0Utxd7ovoHEiKU9lnxbX0GG_AMzDPXc4YUQ67SocqQ0iAq_PBk29jh1vF2GK-6ec_NFb5rkgKJYxSaEjTOqkO0geQ2PXTPC4XYP43wKWjFnGN0XaCuSUzIEP-qgutCpmBnKxVqV6Xs7fnhUg9Dj0Ge-LrmSxktT9pxzEHZnCalwj-A2fX9fj4tXlZSle30sE6Nn5PXEeQYY4KmC8ZqoMnrVbgg-cICD2aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
مذاکره‌کنندگان ایرانی منتظر تایید نهایی از سوی شورای عالی امنیت ملی ایران در مورد توافق آتی با عمان و ایالات متحده هستند. این دیپلمات ادعا می‌کند که انتظار می‌رود شورای عالی امنیت ملی این توافق را تصویب کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69702" target="_blank">📅 21:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69699">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWFgJP2z6UNW8K7fiekLcc7CdRiumMC5NkiHK_R2w54SLpMJyLsq6N9Cd2T8BCBIa8gFIitmyvF9PWit1vg2hvrPk1rqaZR2ljcjU9FGBtEeYqfpshQ5ryHeZ_pVOKwR6_ivUvmIhw_bSa7JYWxfALOzjjB-drISU4jQMNdx_ExpzVPQ7fwEp3An_zzZWZhKcm-ofchzEF9JhKWSeQbdAbfgNoZr4KekNytgPvyHqBGaC5R9QyVHMImHGq9nzjZgjGqXB0D_bZeCeSlODkgLvUTrikBhFFEFish_wdxRtYTBq2ZPf1VLpfGnBoQ2f7XOt-0qtVy5wbajScoyvOQ1Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UVBRQgJErq413TKuX6mlBK705S-mQPxatYEXtTgI70bRg6aBW-LtTy-hJ2DPyzD-SVnUZMI0wd64_FrWtTfq6nrq190MeJxv4dA-yBL--jQajcdP6eWGI2LGw3lUatTYrKD_RLC4LAKWwNj2kpw9l3UztFSfV16jgvN2II31szzIdVwv6LGudMoic9EO3LWLNsCpDLgCGXlxEIe1zpNYK3bIA2AXAWS_FFjhzav_8d3ykkL-kBTxctjAfOBYyFCLiZqw8VHCQgarMle6CZ8NYTktxPFprfIqg9NPncrCFcs2TFEgKxDkrBzeLlA8Vkjr0ur5gBv4kIVd2ZdxiMBXgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ab8e5c4f.mp4?token=kHS1kMgBVwP7PXjtZA3RlEBWVp-YHMQuv5pOY9mijYufajhwNNTk5GkxU4kI853ghUSvHb6iTGuBJMMmpivHzJYbHZIZc_O0DbqS1OOp4GTtyEAG_OAYJOOlsznxoh08-CwIwvgq-FKNs7etynMBvR13OrK2D_JwjdUd5tw43pBPgiun2qnpMcaNLwl5iJGJ6Y5sZisj2ImqxSksuB2c-Ykd_3WnJibrcnpmDAYxyNz2dT0xXe3841IFOAU_6H4xPlj75M50ryBvYeZKTJcUu2kejy6P3PcZgqL2b9A8F11HwmSaMAMkZDymE6-zrQzeIav1zURIHU-EM1F7iUlIlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ab8e5c4f.mp4?token=kHS1kMgBVwP7PXjtZA3RlEBWVp-YHMQuv5pOY9mijYufajhwNNTk5GkxU4kI853ghUSvHb6iTGuBJMMmpivHzJYbHZIZc_O0DbqS1OOp4GTtyEAG_OAYJOOlsznxoh08-CwIwvgq-FKNs7etynMBvR13OrK2D_JwjdUd5tw43pBPgiun2qnpMcaNLwl5iJGJ6Y5sZisj2ImqxSksuB2c-Ykd_3WnJibrcnpmDAYxyNz2dT0xXe3841IFOAU_6H4xPlj75M50ryBvYeZKTJcUu2kejy6P3PcZgqL2b9A8F11HwmSaMAMkZDymE6-zrQzeIav1zURIHU-EM1F7iUlIlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیویی از محل اصابت بمب‌های GBU-39 آمریکایی به سایت پدافندی رژیم در جزیره خارک:
ویدیوی منتشرشده محل اصابت بمب‌های هدایت‌شونده GBU-39 ساخت آمریکا به یکی از سایت‌های پدافندی رژیم جمهوری اسلامی در جزیره خارک و محل استقرار توپ ضد هوایی قدیمی ZU-23 در جریان جنگ را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69699" target="_blank">📅 21:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69696">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P6g-lFnlG4kZd81l2EyDOY-YTMkSHHGwUW_MwFXvU8vPl2LRMwlagJE-NdI2BBASkEwEcvkQr4L2qXbIN44mGPRcE2l5PNODbRQSdHoVJ-Joo3V2XSqHbtMK6R1iaeEGoGjcwUMYfB7Pwi9jepyU-Y0DkG7YiXuqfHql2FSUzE8LBnHqPF01TfNrtz3dTKf2d67SYRbfAcCFHYPfRPbNd14NlzuRcxiwHsMKldv7plwUuKDFBbhze0GHB5agbfN1cwfB-TxF7Rw-7uR_qQ8AjJEAomIYbtI_6bFI-qw0OVePdCudt2vub1n9jR7TO7kFsemWORqF3ThkL0Y7HQudZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7ed553c5ba.mp4?token=BDTXMDq0G5_9bJAqohPXhLkzqX2GGj2nttljt_wagPyhm-PULbvwFW6n9zWdmV7x0YS1-E7BKKgn_0ILEgNutMxI4yF3bv7ppG96jnzwizXjUnP1gQrXmdxl1BK3hT5O8eSkgojjKtlMGVaU-w99dGpF5iZWPv4RYUuIWTHO7_1HliAFiDu49gAWBpW4G4N3rNiLp7fBbb25DXEC2vkbTqmridN9u069aoxNPRm8YX2wK2mfrOuss6Dg9WsK8y-LcN4N1JP2EEunR_o3ECe6FKoCI5oMQCsALleLH8GLEMmGhs82iKCioFMvooh3wXSFJLlKJy1wX9P4PkkHReAD9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7ed553c5ba.mp4?token=BDTXMDq0G5_9bJAqohPXhLkzqX2GGj2nttljt_wagPyhm-PULbvwFW6n9zWdmV7x0YS1-E7BKKgn_0ILEgNutMxI4yF3bv7ppG96jnzwizXjUnP1gQrXmdxl1BK3hT5O8eSkgojjKtlMGVaU-w99dGpF5iZWPv4RYUuIWTHO7_1HliAFiDu49gAWBpW4G4N3rNiLp7fBbb25DXEC2vkbTqmridN9u069aoxNPRm8YX2wK2mfrOuss6Dg9WsK8y-LcN4N1JP2EEunR_o3ECe6FKoCI5oMQCsALleLH8GLEMmGhs82iKCioFMvooh3wXSFJLlKJy1wX9P4PkkHReAD9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز ۱۶ ام مرداد، سالروز درگذشت فریدون فرخزاد هست.
مجری، خواننده، بازیگر و سیاستمدار ایرانی، متفکر، میهن پرست و آینده نگر.
به قدری کلامش پرنفوذ بود، که جمهوری اسلامی احساس خطر کرد و در نهایت ترورش کردن.
اون همیشه دغدغه‌اش، آگاهی و آزادی مردم بود و همیشه مردم رو به مطالعه و مقابله با خرافات تشویق میکرد.
از جملات معروفش میشه اشاره کرد به:
«یک روزی ملت ما آزاد میشود و این روز زیاد دور نیست. فرهنگ همیشه بر زور، ستم و قلدری پیروز می‌شود.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69696" target="_blank">📅 20:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69695">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH_5mTneZtX7Ngcxk8ZxiYsvWZPD3hpAEcMWK29KTXrpumVpTB76JgQByajukCeVvtdZxiZJ6jTgTtJst-yEOpWCIcImEdwx70SzRvsml3G6wQLXnzGWNdCET3PxcHfIP4xh7B_1O41C4IJXZX0Xxf59AeY1Bi9dux6Z-wtjhGfDsSLoBv_iivoK1DmeIgq9hWhK9_yWRwU3cznw0EHW9I0H89I2LLAoY1QLxOZ_xPE06JQ_uu10dBSjbtIWszNM1-mcUsT94AfPfk90Ouj1BLUFy-iU5tAALc_j0azeYVqhAXgixNNAswWh9jFmx_77QRRZ_AZy5S5RQlcFdKma_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
تسنیم تصویری از لاشه جنگنده آمریکایی F-15E Strike Eagle (با شماره ثبت 00-3000) منتشر کردند که متعلق به «بال ۴۸ جنگنده» (48th Fighter Wing) بود.
این جنگنده F-15E در ماه آوریل سرنگون شد و منجر به آغاز یک عملیات نجات گسترده از سوی ایالات متحده گردید که طی آن هر دو خلبان با موفقیت نجات یافتند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69695" target="_blank">📅 19:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69694">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bedb477ce.mp4?token=OiBXcCsHsv0Kx6Ry9YL5Fq4EJayVbty8FIeAZPS8WH-nJWGzDrAzdF1RyNk9LdtfAoVMXxMY2ELZA8mYZaH1rFUONa3sr8sk7twlQJZMEAas_3mLUlVJM2Z6LsbDLIOpLDl3aCb5aI7KeQhCCdp7hP5TWsm5GwNKQmm27XEVfTE9p4LtWDt8QrfkZ1qtkLAkvo1SZAkSSJpIi3U8gLoDN05K1PBv3_A3kwUA60NBg99LR6Z9T0ZN-VB7ypLcNz1HXTMOWPHW-haU3zVnHC9zbO3OgYfz36xl0fT-BH45Lttod6B_0Wo_8-ewfQvXF7LAe6FV8lWQ7oNJhmNoNcmjFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bedb477ce.mp4?token=OiBXcCsHsv0Kx6Ry9YL5Fq4EJayVbty8FIeAZPS8WH-nJWGzDrAzdF1RyNk9LdtfAoVMXxMY2ELZA8mYZaH1rFUONa3sr8sk7twlQJZMEAas_3mLUlVJM2Z6LsbDLIOpLDl3aCb5aI7KeQhCCdp7hP5TWsm5GwNKQmm27XEVfTE9p4LtWDt8QrfkZ1qtkLAkvo1SZAkSSJpIi3U8gLoDN05K1PBv3_A3kwUA60NBg99LR6Z9T0ZN-VB7ypLcNz1HXTMOWPHW-haU3zVnHC9zbO3OgYfz36xl0fT-BH45Lttod6B_0Wo_8-ewfQvXF7LAe6FV8lWQ7oNJhmNoNcmjFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⌛
چند روز پیش یه خانوم معلم به برنامه شهبازی وصل شد و این حرفا رو نثار شهبازی کرد :
من معلم دانش آموزان ایرانی هستم و خیلی رندوم مجری حال بهم زنی مثل شما دیدم
اسمتو از گوگل سرچ کردم دیدم حالم از ادبیاتت بهم میخوره از لفظ و گفتارش و از عدم اگاهیش حالم بهم میخوره
همه میدونه این مسخره بازیو که ایران گذشته چطور بود و الان چطوره حالم از دروغ هاتون بهم میخوره
واقعا صداوسیما انقد بیچارس افرادی مثل تورو بزارن مجری و وقت مردم رو بگیرن؟؟
البته دیگه افرادی براشون نمونده باید دست به دامان چنین افراد مزخرفی بشن
🇮🇷
حالا واکنش شهبازی: اینایی ک از سلمونی و کوچه خیابون گذرا مارو می‌بینید بهتره یه چند قسمت ببینید بعد مارو قضاوت بکنید
👍
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69694" target="_blank">📅 19:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69693">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Anw9SV-BY3xLkWNarlIJr4QqPjXywWnM6mQuVqhLUSYu7bwIVvwzV71NZW9LEOEqAlFUdoCDT0tKX4muctXyYX8ohCfr40VPshTiblls4DORJVUmgi7WoJ1KsxcO9O4BAmZrpCh17XNKsq5NO9QGNEBSpSJgFN9Yr71rFZA594zBcn1AAdVpBY_r2t3nsSEhpTmPzW4v_Pw4dExsN3k0MIv4LaUOyAwyFQhR9k8VpEENqkJfaZNwsC0iBk4B1GUPQeruc4t1NbFJJXRhx5CLNBXhqP_MPZr8NuCzIHXBFifdqUajo7Epa_wav8MEmgYD7oj_n5P8a5kNKJ0fxkMB_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
به نظر می‌رسد که محاصره دریایی ایالات متحده، صادرات نفت خام ایران را متوقف کرده است.
تقریباً یک هفته است که هیچ تانکری در جزیره خارک، اصلی‌ترین پایانه صادرات نفت ایران، بارگیری نشده است. این طولانی‌ترین دوره اختلال از زمان آغاز جنگ است.
اطلاعات ماهواره‌ای و کشتیرانی نشان می‌دهد که اسکله‌های بارگیری خالی هستند و ترافیک کشتی‌ها به طور کلی متوقف شده است.
ایران همچنان درآمدی از نفت‌هایی که قبل از محاصره ارسال شده‌اند، کسب می‌کند، اما این محموله‌ها رو به اتمام هستند.
به جای پر کردن مخازن ذخیره، به نظر می‌رسد که ایران تولید نفت را کاهش داده است تا از تجاوز به ظرفیت ذخیره‌سازی جلوگیری کند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69693" target="_blank">📅 19:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69692">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af32e5c900.mp4?token=qtB4UqhGeYM15C1dcxtGKGA8aWwr8ke8yGn8hhWJZzUSsD40Q_4AN6YAs0FlyRrL18ti4xlPzXVmi9DF6aVronH1tZCuMKpIFDJxAqjP1cmoz-h8qDukrcZ58YtI9mX8eiCWHurjnelh3MZ6xACI1e6MBO9POClWEtgkRGrrSP67kWbGTaYSrTOyTmDf9Xk0faz09CAfmC5lJmudsQv8PuyiZkHOwANmJgwG9YtixeCdbz25oWvNL8DXG0WFE3B22LrpluDzLNYiuKH_BS0TIyhdZaPx5BC2XV3qypzLkvRZ7_otGo9htec4J5P7-Onpf4lwxiTVOcYr-IlcFg0-wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af32e5c900.mp4?token=qtB4UqhGeYM15C1dcxtGKGA8aWwr8ke8yGn8hhWJZzUSsD40Q_4AN6YAs0FlyRrL18ti4xlPzXVmi9DF6aVronH1tZCuMKpIFDJxAqjP1cmoz-h8qDukrcZ58YtI9mX8eiCWHurjnelh3MZ6xACI1e6MBO9POClWEtgkRGrrSP67kWbGTaYSrTOyTmDf9Xk0faz09CAfmC5lJmudsQv8PuyiZkHOwANmJgwG9YtixeCdbz25oWvNL8DXG0WFE3B22LrpluDzLNYiuKH_BS0TIyhdZaPx5BC2XV3qypzLkvRZ7_otGo9htec4J5P7-Onpf4lwxiTVOcYr-IlcFg0-wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت، وزیر خزانه‌داری آمریکا:
«ما آن‌ها را کاملاً تحت فشار قرار داده‌ایم و آن‌ها با تورم ۱۵۰ تا ۱۸۰ درصدی مواد غذایی روبه‌رو هستند و حتی توان پرداخت حقوق نیروهای نظامی خود را ندارند.
فکر می‌کنم به‌زودی، شاید حتی امروز یا فردا، شاهد دستیابی به یک توافق و برقراری آتش‌بس ۳۰ تا ۶۰ روزه باشیم و تنگه هرمز نیز بازگشایی شود.
در این صورت، قیمت انرژی باید کاهش پیدا کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69692" target="_blank">📅 18:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69691">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac71f40e4.mp4?token=vHGB1GCwA7sQCFDyNPqu8-eEew60T-nhv6IIhFh-Xu-PkuI_dbJgNkI8w0tLsjwM9m4R09T24cImPV8Br8DbyeiRnNPIchXrJQYVmIivFncRIhxl4jHSGam21nnTA8tfjAkF4-ArvagSweG9RCdTqK9-FkeDFuUEJctbMOgACsRUl-IUcw6IekAXQum35yz3c1Bde6YuN2-BisSv-ojy3_nvpavwMZ346VOh2zooRatet6antPfwSrx7KWgzI40Niw0Y7wC4uvYH1XU8honxsZYt-re2iuvIP5NQqv1AYzBbvf21Vs-Kv7UsHd6YVE35pIXCVUFEBRfQrO7V4EyKRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac71f40e4.mp4?token=vHGB1GCwA7sQCFDyNPqu8-eEew60T-nhv6IIhFh-Xu-PkuI_dbJgNkI8w0tLsjwM9m4R09T24cImPV8Br8DbyeiRnNPIchXrJQYVmIivFncRIhxl4jHSGam21nnTA8tfjAkF4-ArvagSweG9RCdTqK9-FkeDFuUEJctbMOgACsRUl-IUcw6IekAXQum35yz3c1Bde6YuN2-BisSv-ojy3_nvpavwMZ346VOh2zooRatet6antPfwSrx7KWgzI40Niw0Y7wC4uvYH1XU8honxsZYt-re2iuvIP5NQqv1AYzBbvf21Vs-Kv7UsHd6YVE35pIXCVUFEBRfQrO7V4EyKRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبت های یک حامی حکومت:
دیدید واسه اربعین چجوری از پول شما مردم خرج کردیم و کباب آهو دادیم به زائرا؟
براندازا بسوزید، بسوزید که هرچقد پول دارید و ندارید باید خرج امام حسین کنید، تا ابد خرج امام حسین و دینمون میکنیم یا الله!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69691" target="_blank">📅 17:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69688">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266f0707c9.mp4?token=fcrcxwg0l42o3qOR7FODmU61zvt1EUSzoVIIyZS35H04bCKWVKFOWaiQB0xTuhqWvX03dsT23GaEKLNBFSbJFsLQ_ToaVWo2uCTFzRn3pQ-sU9aCFbIB1tXwPjSK10PFTzSr1koT_0m6-aKwHdjqBxi6y-lh0JYw2RBbOJHYRcpa5iLJVaB5bIyHaYLrxO37AF6Ffe3N4HZibr7wJvwvYa7ZeuDOwiBpP_nhfTyqloJPUiX3b--Qa0XbF8HkyQkspQfbcRL6pia7T6FGYk-Srjkd03jinlE7WFeRH6EebrNDS-tT84OegIIUDPgwlIR5TBr7RN1Z0jjUeY9qulUpDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266f0707c9.mp4?token=fcrcxwg0l42o3qOR7FODmU61zvt1EUSzoVIIyZS35H04bCKWVKFOWaiQB0xTuhqWvX03dsT23GaEKLNBFSbJFsLQ_ToaVWo2uCTFzRn3pQ-sU9aCFbIB1tXwPjSK10PFTzSr1koT_0m6-aKwHdjqBxi6y-lh0JYw2RBbOJHYRcpa5iLJVaB5bIyHaYLrxO37AF6Ffe3N4HZibr7wJvwvYa7ZeuDOwiBpP_nhfTyqloJPUiX3b--Qa0XbF8HkyQkspQfbcRL6pia7T6FGYk-Srjkd03jinlE7WFeRH6EebrNDS-tT84OegIIUDPgwlIR5TBr7RN1Z0jjUeY9qulUpDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‼️
🛸
وزارت جنگ ایالات متحده، پنجمین مجموعه از اسناد مربوط به پدیده‌های هوایی ناشناخته را منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69688" target="_blank">📅 17:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69686">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727c872e40.mp4?token=DeHTJd7KGJ_9TPGKQN5Hh1TFtLwyD-NM8A4zvpI8FLU_Bzwz_v9sEzDWxyBl1HcmaHcLmcokbkTc9ukoFwUf59RPPnjPI5_wwMwMru277SW0GRswdb10k7JdUq_q1e1ixx-vwQ6_LQprhRhg37M_zKwex30Pk1s8CZJooojTRm1uG6T3qOV3TqNEpZDTVaPGLRr977XI1FRzN6lMYHUpDmhoH7HS29p-xYJzoYvYfgvM2n-nQUHp9-WTsiV-iNNTKLKHT2QIOpmMeY0E7-Kd1oryTGEkz9ru799r63EBQQNdnIg9tdZpN9oPm5meT2paX69c9-OpgxJIMacDHZ2Bdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727c872e40.mp4?token=DeHTJd7KGJ_9TPGKQN5Hh1TFtLwyD-NM8A4zvpI8FLU_Bzwz_v9sEzDWxyBl1HcmaHcLmcokbkTc9ukoFwUf59RPPnjPI5_wwMwMru277SW0GRswdb10k7JdUq_q1e1ixx-vwQ6_LQprhRhg37M_zKwex30Pk1s8CZJooojTRm1uG6T3qOV3TqNEpZDTVaPGLRr977XI1FRzN6lMYHUpDmhoH7HS29p-xYJzoYvYfgvM2n-nQUHp9-WTsiV-iNNTKLKHT2QIOpmMeY0E7-Kd1oryTGEkz9ru799r63EBQQNdnIg9tdZpN9oPm5meT2paX69c9-OpgxJIMacDHZ2Bdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از یک مصاحبه قدیمی با روح الله زم :
من با بالایی ها ارتباط دارم و بهم امار میدن کاملا
اینا پشت بیسیم هرچی میگن من میفهمم
هیچکس نمیتونه بفهمه منابع من کیه
همه مکالمه های بی سیم، سیستم ایران شنود میکنم
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69686" target="_blank">📅 16:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69685">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b41beaa653.mp4?token=faFcZbCaSKBHCmnugk2232AEfAd3cSjA2qV0ciqwh7UKCT0bF0HUDeD8udV9c22JkIJhu78-rdl0mPQtfmptcuZcCN391szTNI4n_ZaB1GAoqcoLxJ8bUhMEx_8NRd-Y2-IF5Dim2nSjopiYbWEGhODo_NwI2Mxr5NpDK8W0i8h6bwt1Tm1EbRRG3p4Kqtkp5oSAb7U6uRfUP8pmEeNrCtBmxSYExUvmdfq5_biX_093YPYjpCa91rgN7JsQtHaLihlP66giGlF51w8l3DQBv5APRulX9FAUE9FDZOLIbFDhvg0g8uDcftmc9e2ctBY5kL2QtS_I0-n5_TXU8S-JoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b41beaa653.mp4?token=faFcZbCaSKBHCmnugk2232AEfAd3cSjA2qV0ciqwh7UKCT0bF0HUDeD8udV9c22JkIJhu78-rdl0mPQtfmptcuZcCN391szTNI4n_ZaB1GAoqcoLxJ8bUhMEx_8NRd-Y2-IF5Dim2nSjopiYbWEGhODo_NwI2Mxr5NpDK8W0i8h6bwt1Tm1EbRRG3p4Kqtkp5oSAb7U6uRfUP8pmEeNrCtBmxSYExUvmdfq5_biX_093YPYjpCa91rgN7JsQtHaLihlP66giGlF51w8l3DQBv5APRulX9FAUE9FDZOLIbFDhvg0g8uDcftmc9e2ctBY5kL2QtS_I0-n5_TXU8S-JoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم وایرال شده از مرکز ترک اعتیاد توی بالاشهر تهران؛
اینجا ترک کردن کمپ، سخت‌تر از ترک مواده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69685" target="_blank">📅 15:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69682">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rv8ldM4Loh-2ug2oP79f0wWFQXg-nxbh_tT4nHBsHDis1Ys_u3b_HRSposrmG2-KfgfrsEMlrhuNnfP3xl91pGuiMIYbES-wS7v0y5ZWZ14iowApXSYNpuN_mSt-jYXujL8es6TgtvZUyHzGgddZTBFllkV3fTqr5JZw02uDLeUuP_d3tXgkWnitizHRX7gfh6VszUQ5-TFPaL6iypd7EMym9knbxnVmDJ0ShtcyQhInhxy9rJf29k8HFpAl7XBU7NqlPk3WfhD9qGgCnJq-5YQKdgnThrAYX2WzDKO9vhYOoepWp3LC4N6eWYewV25I-ENrDwdWrfjourh677NvGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/taX2U4Lng5p3Pi29EeWQkNjA7qMfc9LP2SgGnMbTCkLrK7C8m6x-91pOg278hoVSjHV3dP-8zw_vvdYJ-fB-VqIyrcgVnKgxMY6USvPD6L8j5EGKlKKmztmWuViCND3K3m022d4i9lVjo4jliF1TeMU_FKsDZMOMAFt9TqM2gVzkIXR014p9Cjks8ScCKnnZP9sDgMYjT7ItU_B0lIbZtyIEjw64-JFQRvyj_6xv_KFDtsS7sCcfqywHm0TeVNihaNG1zgt3NYtuyZqCWu0jNqHR363-nlMnkyfZKt6WQS0mVzYjOTQSZAA7pe-Gi9NaQ2OGgpZLKfqSK7FE450Tyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qaFiTdabI_U_DjIK80J3P3qyAilUF92sBaeRG-d03nP1oKtr-sx9XVqm2DuykpdrYyYobgMCYakUiL0TYfiF2ozIjP5f_DLdi6xCZ0N9YBZe18cSfVnSdeauuq_yf9_f-VvgasrtxgtE8m0fLojJNG55TjR77M5AsJq-nvn6AAXopjnO8DNV84PUdbmnFQAQxxt8g_rwQPe2O4QLz-RW7rCgAtphmkbgMv64MCbF943VxLuecL3KzkS-WDysdwiz9LOJEpmBcwWzv7t22IXRGFq3_p-emInm6dIkQgmawA7DcjVewMZKAzKOeAw99dPlGPoSD-iHIYMe_xll0jieJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇮🇷
خبرگزاری تسنیم وابسته به سپاه پاسداران تصاویری از یک «انبار» هواگردها منتشر کرده و مدعی شده این تجهیزات متعلق به هواگردهای اسرائیلی و آمریکایی هستند که در جریان جنگ سرنگون شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69682" target="_blank">📅 15:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69681">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5020dac98e.mp4?token=i-TbTYPreZefw494cA91zBC7ZO-v46prArizrp3L-bIpXkGuoYisme8aXXTfStNG6IK4sRmM0qEmmFO1iIlkswYvT6TiqzU_Lwg9QR12dWYp4v7OMsrV4_viematM1KD-xNw7e0ktDJ-S2lTTT4B1GCNA-OyJRmD-UFjHoGqWAx4Yki6IDXiPuZnjbcQnJIegjhiPgfg-TvKW8bNNg9bWnEY9FUbbVpJCDPP_TpxBLq9wg8FJbkGd3bgubwlt0nOe-hS3gxHYWyx_zcOp3bRzqsmkQF81z3NHASO5zKmM9Tg_OdYadAlddyfZ0RGWg1RrnS7tkcULoCgS-QOP4kh7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5020dac98e.mp4?token=i-TbTYPreZefw494cA91zBC7ZO-v46prArizrp3L-bIpXkGuoYisme8aXXTfStNG6IK4sRmM0qEmmFO1iIlkswYvT6TiqzU_Lwg9QR12dWYp4v7OMsrV4_viematM1KD-xNw7e0ktDJ-S2lTTT4B1GCNA-OyJRmD-UFjHoGqWAx4Yki6IDXiPuZnjbcQnJIegjhiPgfg-TvKW8bNNg9bWnEY9FUbbVpJCDPP_TpxBLq9wg8FJbkGd3bgubwlt0nOe-hS3gxHYWyx_zcOp3bRzqsmkQF81z3NHASO5zKmM9Tg_OdYadAlddyfZ0RGWg1RrnS7tkcULoCgS-QOP4kh7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سردار کوثری، عضو کمیسیون امنیت ملی مجلس:
ما هنوز که هنوزه موندیم چرا شمخانی با اون همه سابقه نظامی، اصرار داشت اون روزِ حمله جلسه بذاره!
رادان گفت نمیام و رضائیان، رئیس سازمان اطلاعات فراجا رو فرستاد.
پاکپور، فرمانده سپاه گفت من نمیام دارم میرم اهواز، ولی به اصرار شمخانی اومد.
وزیر دفاع رو هم با معاون‌هاش دعوت کرده بود.
الانم چون کسی از اون جلسه زنده نمونده، نمی‌تونیم بفهمیم چرا شمخانی انقدر اصرار به برگزاری جلسه سران داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69681" target="_blank">📅 15:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69679">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lYbp6PO4gKxwTgvNFBHfTM6Ktl2ssuA0HGV1eZaBBhmmS8Ws2zQr7xO3wKa3-dCBcsW5I-7GWRq_VgilhtnqIP3NFEHj1xUyrfoWbt8f6M4FKzc5k2x0xipNytcjRGI7g7mtOzqNlkImm6eVEwSKS4sNIrl7SLlIeWjQBKQJu7oiQcOUUaJxa8W39dWP0hT1itnR_ataf1Uu01GPm35uA7RIr4qkM4bJmVKfh1P9vRhfhjmRyT6viaG-rlgwxDhEf-XPwKc7iSkXP86LAZwTPI4d_a8YD5S_2qGImk5DNLsjie0Oj5GBmdwF0appCAIRxWMwKFoqGU632KMkZR85dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AiJYwl7BbOaGXgzKt5L774qO2KfYNJYdNf-g7uo74ThOHyef0xGF70qhxGwAvfxGJQNELe41_Ykf4hJsFOfNWvMu0uTphXAcjLBfuRzkG0VlS9f2W0MP3-8SLhu5FL0TaXkjwYuCv2mIh-lvhFyxYxL9EFeGHQq9zmEgQf760Q9g7h92VG8ODsMGZFFvgrsGrrXvJhq5aU45rKulGW8KBMJ3YxOX1e7i3DDQOmqXYMBlp1d9C7M8j3cP76WL-mg3QQg0v8onjlgG44YOR6QK68YMFMfptmCPQJqYJkd-A9MHbsap9M-JJN1rMRBvQh0CV1rWp25P1EoP_i9-zhRVIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⭕️
🇸🇦
🇹🇷
🇵🇰
ترکیه، عربستان سعودی و پاکستان پیمان دفاعی «توافق‌نامه مکه» را امضا کردند: «هرگونه حمله نظامی علیه هر یک از این سه کشور، به منزله حمله به هر سه آن‌ها تلقی خواهد شد.»
این توافق که مذاکرات آن از سال گذشته در جریان بود، چارچوب نظامی سه‌جانبه و مهمی را در بحبوحه بحران منطقه‌ایِ رو به تشدید — که پس از حملات اسرائیل و آمریکا به ایران پدید آمده است — ایجاد می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69679" target="_blank">📅 14:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69677">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b215003af2.mp4?token=BYGL7217kOxGsbYW-Swhu3EO3jTnvxrxmfTCL1XOvQuBB1RfCAQK7Oq2SCnKprwhbiYn9XhmTQiyt9Tlmr0SwxtCAKgUI8h4uPPpgonhlA5q3sdaxXtCXavwrozsGrbtH_kpqWGfsdAyG4WJqoWnQMyt7t3P5RolBdo4nA55LuprsrY5X14DxIVDwXPDCOFzEAweenQutFrmmPjO8xX3lnd3purBvHQKRC4fqfmJKRidvj8SiXNuy7FmrNTnARE4J8zOJbYGi0ECnhc0-DJ3jGAWOYj-eMi87dq6Rg05hj55g6pLKN9ySOYwZ2r9ZFcV6OPxLISLjiFJBv_LAFG7zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b215003af2.mp4?token=BYGL7217kOxGsbYW-Swhu3EO3jTnvxrxmfTCL1XOvQuBB1RfCAQK7Oq2SCnKprwhbiYn9XhmTQiyt9Tlmr0SwxtCAKgUI8h4uPPpgonhlA5q3sdaxXtCXavwrozsGrbtH_kpqWGfsdAyG4WJqoWnQMyt7t3P5RolBdo4nA55LuprsrY5X14DxIVDwXPDCOFzEAweenQutFrmmPjO8xX3lnd3purBvHQKRC4fqfmJKRidvj8SiXNuy7FmrNTnARE4J8zOJbYGi0ECnhc0-DJ3jGAWOYj-eMi87dq6Rg05hj55g6pLKN9ySOYwZ2r9ZFcV6OPxLISLjiFJBv_LAFG7zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇹🇷
🇵🇰
رجب طیب اردوغان، رئیس‌جمهور ترکیه، و شهباز شریف، نخست‌وزیر پاکستان، به همراه مارشال عاصم منیر، فرمانده ارتش پاکستان، امروز وارد مکه در عربستان سعودی شدند تا در مراسم امضای توافق‌نامه دفاعی سه‌جانبه شرکت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69677" target="_blank">📅 14:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69676">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/637fe07403.mp4?token=n5AKl7uAe7vX2e4SNrl6WZyTDs7B8od1Ab3oN9_nuU0aXVpBlGiwXw-MpejgnxlbfrUjHVpY8aNe0MD4L0G2fHhrVuhWyl_1T6JOh2TBYWPNGLskBNBzwzhbFT2oDXJXR-_T8p0ZkZk_7Dbe3-Il2AA9vKv6ZP44wapH-YnG2FdX-wAlcWCiIUsjnQlkiSYtMX4Y5C3inXldOQrMqQaOQKSxY3n0tEJ45j28WxsfI3ueeKlopKYLz5IxRpm0PoaKN7YYtyz0dE89PlXTbb1Sm-6BG3PrbkTl9U_ErEXqpYkdhr3FYmPr2dftxtMiczFa-nFo4grckN0j0QbPbaOqyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/637fe07403.mp4?token=n5AKl7uAe7vX2e4SNrl6WZyTDs7B8od1Ab3oN9_nuU0aXVpBlGiwXw-MpejgnxlbfrUjHVpY8aNe0MD4L0G2fHhrVuhWyl_1T6JOh2TBYWPNGLskBNBzwzhbFT2oDXJXR-_T8p0ZkZk_7Dbe3-Il2AA9vKv6ZP44wapH-YnG2FdX-wAlcWCiIUsjnQlkiSYtMX4Y5C3inXldOQrMqQaOQKSxY3n0tEJ45j28WxsfI3ueeKlopKYLz5IxRpm0PoaKN7YYtyz0dE89PlXTbb1Sm-6BG3PrbkTl9U_ErEXqpYkdhr3FYmPr2dftxtMiczFa-nFo4grckN0j0QbPbaOqyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از صحبت های ترامپ درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69676" target="_blank">📅 13:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69675">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a5084b0f.mp4?token=Xtf5Nok75lcrRIsuTDNxLGJdJYGI2xrIUWnJ-RAcih67eJjyN2jOTlqDaL0Xb-far71x3N1SIsSO124HyP-jZy7flEhFE7s5Yh1dy54jEYKL40gBiJMA-ZOa5ADcg-BIpYqZF4NbGv7EEAE2aAEh5GGpnVMiLCDzlIqWFNoPoA4E5xjbax-Xehpc2kIqRZ1B9nNqUv58Zg9xC7qLCPojyJ1_QMeKxetyzsJ-ifp5nliIKS12O2xAMXZAJdKP6SBVzGLCeYU2NDjK0benoQVeWPq6PVgDNMVGZIN4_X_Es7C9mSN7b3Qcauyr765W2VeHvRXcm399POJALI8umrstzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a5084b0f.mp4?token=Xtf5Nok75lcrRIsuTDNxLGJdJYGI2xrIUWnJ-RAcih67eJjyN2jOTlqDaL0Xb-far71x3N1SIsSO124HyP-jZy7flEhFE7s5Yh1dy54jEYKL40gBiJMA-ZOa5ADcg-BIpYqZF4NbGv7EEAE2aAEh5GGpnVMiLCDzlIqWFNoPoA4E5xjbax-Xehpc2kIqRZ1B9nNqUv58Zg9xC7qLCPojyJ1_QMeKxetyzsJ-ifp5nliIKS12O2xAMXZAJdKP6SBVzGLCeYU2NDjK0benoQVeWPq6PVgDNMVGZIN4_X_Es7C9mSN7b3Qcauyr765W2VeHvRXcm399POJALI8umrstzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
روایت کوثری نماینده مجلس از عملیات اطلاعاتی موساد؛ «رد لاریجانی از طریق گوشی زده شد»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69675" target="_blank">📅 13:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69674">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
r16
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69674" target="_blank">📅 13:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69673">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajlUKGTzs1mU8yDkk5C9OXB5H6uwDsNTXGDsgpl1DR-OY0vXSYScveg2z__5_EbIdI4qP13JER8nrfi5c6zzH1UrsjEsJ3ucGnfL2gBkCx68-g2anuQvd_jvDdlmKvFxNM3JiB1VPpzeec8AqIv0bz82wKk9QKaRSfGJX0lkxshvAw_c3b776FBdfRDC-wcGt0tqTRfQVPhEdKoBMfYhYAY9oqv16T3yRKHVo0MteLCwj7mkVotjMlLEkCi5hCWteM1Crh_zSnY4PCXXlZofe8TYXYdkTvZzxasjdLxIaN7R8IKEy5UZ7OCMa747ognMNT0ultOEHV-Blxi7rxru7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r16
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/69673" target="_blank">📅 13:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69671">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0c63da7c.mp4?token=gG-h0ZSAgbIM4oBhMQWvL6_0kmjVq4FhllGG355-ZLToMgtnkCYQnEp0dD3r6IRanmKxHlUXsJANq8JC2Bx1D5TDpD9T9G-_Y4QSJUAnndMErDes_q8OmFcI8Aa4Xqac-uRjumjavvIJkqyE2KsIwyZqbccGAZU3CDy-9RiyQurLaDQIatsxQYAv_G3JVvYQzAYrrE2yy8yOdNJSJD8npJRxTangbs-7eVFVkIwZ-tRtoEgru_SeM8xDyg3hi_1_EWjijZoEXI75DaXTH1mi2FkVoGIdOnN-OZpniOtjADKDUqnuAhh08A_VY_yIMrcZMZX6imE3EMBXAkXVu_MuqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0c63da7c.mp4?token=gG-h0ZSAgbIM4oBhMQWvL6_0kmjVq4FhllGG355-ZLToMgtnkCYQnEp0dD3r6IRanmKxHlUXsJANq8JC2Bx1D5TDpD9T9G-_Y4QSJUAnndMErDes_q8OmFcI8Aa4Xqac-uRjumjavvIJkqyE2KsIwyZqbccGAZU3CDy-9RiyQurLaDQIatsxQYAv_G3JVvYQzAYrrE2yy8yOdNJSJD8npJRxTangbs-7eVFVkIwZ-tRtoEgru_SeM8xDyg3hi_1_EWjijZoEXI75DaXTH1mi2FkVoGIdOnN-OZpniOtjADKDUqnuAhh08A_VY_yIMrcZMZX6imE3EMBXAkXVu_MuqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تا حالا نوک قله دماوند و کاسه قله دماوند رو دیده بودین؟
۸ مرداد ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69671" target="_blank">📅 12:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69668">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10354b943b.mp4?token=QWISHLlA-heN5rhKFbIXL-VVUGPjk7VDWsOu7jBV7lzq5Zca2cV7N0QCkBwAqq075PpWIlpOwiP9d5VsHtY0oJ8HA37SSY8WjUI2qYcGdoPPT3qlYC7ZmwchB6TvpRL2jC2C3nyb8PQ1t0QDJRaRQCRKWzxkLlATNG0UZz3Yz63_PayxOj-v4tvAr-LZLLnJMX99qqxPh7mWezGkVuEJCI8vJZoBw00oXKPI89ABsbwrQLWl1GZrSmOUmllD2VUu4s-XFgkN7VTzUKnp26PVRj_4LHf9c2_ILr8iDfrSq24izbaEgmoXyAQvY0y6gc_kD93JXVjNiogoePMEVhE0qA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10354b943b.mp4?token=QWISHLlA-heN5rhKFbIXL-VVUGPjk7VDWsOu7jBV7lzq5Zca2cV7N0QCkBwAqq075PpWIlpOwiP9d5VsHtY0oJ8HA37SSY8WjUI2qYcGdoPPT3qlYC7ZmwchB6TvpRL2jC2C3nyb8PQ1t0QDJRaRQCRKWzxkLlATNG0UZz3Yz63_PayxOj-v4tvAr-LZLLnJMX99qqxPh7mWezGkVuEJCI8vJZoBw00oXKPI89ABsbwrQLWl1GZrSmOUmllD2VUu4s-XFgkN7VTzUKnp26PVRj_4LHf9c2_ILr8iDfrSq24izbaEgmoXyAQvY0y6gc_kD93JXVjNiogoePMEVhE0qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🚀
🇷🇺
پهپادهای دوربرد اوکراینی در حال حمله به انبار شرکت روسی "وایلدبریز" در شهر یکاترینبورگ، واقع در منطقه سوردلوفسک، هستند. این انبار حدود ۱۷۰۰ کیلومتر از مرز اوکراین فاصله دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69668" target="_blank">📅 12:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69667">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff4cea8c93.mp4?token=X7BP2CsbRuuKMGoLyXvTENOGGc-TQjCi93IF-CsxMDsZIycVBUT2vwKUZNJjB6KikK3Mzlx00c6uJVD1Y12nNYuxcJgNvNkvtgqdQoGmjsDc-WA7cvyLitHAA2c2wF3PIONEzARw6hImXwNtuc4jn__YSZiaUZ1XYxYLGG8DX6jZW3Sez9XR_egCWwfF7bXvURyXMurS6f1BV_NV60CVMdggc3godRNkx4smNnz-ft5dejCnkch2v8cH1KgifCRHrMjR12hnMdFZMQDZl0vfK_2pPtqTaaJBToGvoHdvgEEdl0-qYzKYuQY6CF-EtvxWtp1ivg1t9lsksRWjJvEp1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff4cea8c93.mp4?token=X7BP2CsbRuuKMGoLyXvTENOGGc-TQjCi93IF-CsxMDsZIycVBUT2vwKUZNJjB6KikK3Mzlx00c6uJVD1Y12nNYuxcJgNvNkvtgqdQoGmjsDc-WA7cvyLitHAA2c2wF3PIONEzARw6hImXwNtuc4jn__YSZiaUZ1XYxYLGG8DX6jZW3Sez9XR_egCWwfF7bXvURyXMurS6f1BV_NV60CVMdggc3godRNkx4smNnz-ft5dejCnkch2v8cH1KgifCRHrMjR12hnMdFZMQDZl0vfK_2pPtqTaaJBToGvoHdvgEEdl0-qYzKYuQY6CF-EtvxWtp1ivg1t9lsksRWjJvEp1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسره رفته خواستگاری، بهش گفتن 114 تا سکه باید مهریه بدی؛
🗣️
اینم قبول نکرده و گفته کمه و من اینارو میدم؛
369 تا سکه
1382 تا گل رز سفید
کل طلافروشی رو می‌زنم به نام دخترتون
یه سهام کوچیک هم تو یه کافه دارم که اونم میدم
امیدوارم راضی بوده باشین.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69667" target="_blank">📅 12:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69666">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
🇺🇸
🇨🇭
آمریکا حتی به سوییس هم اجازه ساخت بمب اتم رو نداد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69666" target="_blank">📅 11:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69665">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ca70a3a5.mp4?token=cOzCdE8O8DzN6-4gSK5ix2Mb-WymcUsTKhAS-U1o9m8gSrT0b23nsz4-bKDOPIMBa-b8Fx6IiWyeKiBh6rO67oCKBhi1o6Z3etioGW6p0TNb4zuVs4n1C7euYhXjDjFLx149hA31QGRrvk_vLsxDmYPI401I7eWx00QitWdNDCGY67Mr90v2u1KprB9_0trS0DzFcVXHNqhPYqwnxYW5TUW4WVKNQguvsERl-sBzDkbetVhdlvKbKdehM9WC_bwiK1RSffgp8bBIo9l4YDZF2RGc1GN03HtMTPYnDARG5RcvPhQnOzfRXyvKvceAAGuG4voM1V1iIllsKOOh7gDSYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ca70a3a5.mp4?token=cOzCdE8O8DzN6-4gSK5ix2Mb-WymcUsTKhAS-U1o9m8gSrT0b23nsz4-bKDOPIMBa-b8Fx6IiWyeKiBh6rO67oCKBhi1o6Z3etioGW6p0TNb4zuVs4n1C7euYhXjDjFLx149hA31QGRrvk_vLsxDmYPI401I7eWx00QitWdNDCGY67Mr90v2u1KprB9_0trS0DzFcVXHNqhPYqwnxYW5TUW4WVKNQguvsERl-sBzDkbetVhdlvKbKdehM9WC_bwiK1RSffgp8bBIo9l4YDZF2RGc1GN03HtMTPYnDARG5RcvPhQnOzfRXyvKvceAAGuG4voM1V1iIllsKOOh7gDSYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از شعبه بازی این پیرمرد، قراره هر لحظه بیشتر سورپرایزت کنه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69665" target="_blank">📅 10:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69664">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMk2K2oBZDnESO8l2jsUPV_38KL8mPfBDdnSxMUhKmr8Y-BlvxOala_PAeqvamg9uwfKspiOnIVHiIXRXS2m9rq8GsoJGaRc92VIbceMNI5xjiSYaL_3vX1riFTibxMeJCS5h2tE0bjWxKCenJ2eH9XDL6EWZ_4--MQ8YqXT1evDFhEPfVm9Yn5aFvn9KFCLYoKRSqOQKwX2aO8ucsh60U6Nnb8kT1IIk4WlBd4zxd-dDm45AC7lPH2BhiM4Fl9lLzzBUH-5E_5VKMBHPWtVfkpVI9pMG3t4zXjRrn7ULz6oTXiwXbkKXp16TnNwBWKT4prM7aN-EnJ5ill7BQOB2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
عنوان مقاله ای که ترامپ در تروث سوشال منتشر کرده؛ دونالد ترامپ در جنگ با ایران پیروز شد!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69664" target="_blank">📅 10:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69663">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c98f66ca27.mp4?token=lHIA86AxIIOZnOZWpaIXHiRhpEILe93ybPahgDHHRUJXFR-KeVtXCZA_-ZomEqfHBUGqnTyMP6Xz0flqnw5Cd5C3OT4e60i5SbTXLAJqaHcO8G-RLSk2U51cOs170YmbmKjkZq5nqKPlUuH3L7uoOU8rsqy3obm6V8Zw-1L7aRv2XeTW9dLrQHco0m-xgLrBMsndxECk-uIaB-A8Oz0RL4OYdZRVsofn64_zV7rXvd8EAsFLsoDhwDz88WGeCRA96geiaqaabdt9xilbP7Ia0_drQeOd9gcL_Mlt7Jw1B99w8TkRcUsJ1JTo17vHv1gdvSv2s3YfYUcm_FEe-Vu-_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c98f66ca27.mp4?token=lHIA86AxIIOZnOZWpaIXHiRhpEILe93ybPahgDHHRUJXFR-KeVtXCZA_-ZomEqfHBUGqnTyMP6Xz0flqnw5Cd5C3OT4e60i5SbTXLAJqaHcO8G-RLSk2U51cOs170YmbmKjkZq5nqKPlUuH3L7uoOU8rsqy3obm6V8Zw-1L7aRv2XeTW9dLrQHco0m-xgLrBMsndxECk-uIaB-A8Oz0RL4OYdZRVsofn64_zV7rXvd8EAsFLsoDhwDz88WGeCRA96geiaqaabdt9xilbP7Ia0_drQeOd9gcL_Mlt7Jw1B99w8TkRcUsJ1JTo17vHv1gdvSv2s3YfYUcm_FEe-Vu-_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
این شما و این مجهزترین اتوبوس های مسافرتی چینی!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69663" target="_blank">📅 10:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69662">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d6484080b.mp4?token=PvXP8ohFdLskmhMMHPVPLh72Tj_hlvaDq7f3WV7zh_4l2akvjkU9RaO9SYPqSayoGqW9Sn0LF--_jhK5Vb379lh0gVjsiXAj-T4flX_VDYQEfxGNZx_d1kk4_uyiB-0JY8CdOOO7FTPS7EElCClPALFgtFQhgf_SClTlY-2QJ0BZM1ey9kz4No9YsvNUti0LHaDN9aUmKx2ZCPk5jIYXil7wb4mDVtAkw7EYN1W7ckpXabyFI_zj5CpeRRxR8RZoLhCyQk7n1l3PJTkPomttk3rtacTbXA6CLxnqn2KXu1V8-EH9uvSqjmOYi5pjMpj8sMGUOoI0SvpNxJseS9n7zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d6484080b.mp4?token=PvXP8ohFdLskmhMMHPVPLh72Tj_hlvaDq7f3WV7zh_4l2akvjkU9RaO9SYPqSayoGqW9Sn0LF--_jhK5Vb379lh0gVjsiXAj-T4flX_VDYQEfxGNZx_d1kk4_uyiB-0JY8CdOOO7FTPS7EElCClPALFgtFQhgf_SClTlY-2QJ0BZM1ey9kz4No9YsvNUti0LHaDN9aUmKx2ZCPk5jIYXil7wb4mDVtAkw7EYN1W7ckpXabyFI_zj5CpeRRxR8RZoLhCyQk7n1l3PJTkPomttk3rtacTbXA6CLxnqn2KXu1V8-EH9uvSqjmOYi5pjMpj8sMGUOoI0SvpNxJseS9n7zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو دیده نشده از لحظه حمله به بیت رهبری و ترور خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69662" target="_blank">📅 09:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69661">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-release.apk</div>
  <div class="tg-doc-extra">4.5 MB</div>
</div>
<a href="https://t.me/news_hut/69661" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎲
همین امشب با اولین شارژ
🤩
🤩
🤩
درصد شارژ بیشتر بگیر
همین الان شانست رو با موجودی اضافی امتحان کن حتما بزنده میشی
👌
👇🏻
👇🏻
🌐
Telegram
🎲
🌐
winro.io
🎲</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69661" target="_blank">📅 02:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69660">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7Ht43pRfFjtW3f1oQy4NzfcTpEjv10kMA9GXo7gU1mUdm8UCYVptbgS9D50czAqOv2QMrwyirQmUWUMfFH2hvbbmYIrHP_fzxz0uPacTg0BNfC8y9uhS_bmPnkSS15WnO9X74vPvKu4UUyVBas8q_s_osQo9Msx_c2vflW-EPc5bfaAwLAoEEFk9O9SoFauhOKBXDZOHsA8MpNnyG-0FWAlKygDGnOtJ4qXI_4HplQScN7yWBUVLm8OWNKcvtdsRkjP9bjBKS-XANIx9vmuco5J7txFGqF5ZfO2lVFHq9Y3KwpziUhERQJC2GcMuc266iMgg1zwkdbhljqJoRk5aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
۲/۵ میلیون شارژ کن ۱۰ میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای هر واریز در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
.
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا a15
🌟
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69660" target="_blank">📅 02:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69659">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HylS152CDAUXnYg9tCwNU2nwanWubWw8s4DvH1EPeyw_Q00x6XyxsHkzDzQLTilydVyZN47j4lLXm6kPZsxqspFAsPrAeNMXrM42RE9gO9Pov8pJO-s7Elz8drTAeu49WWJT0VLA6KHrAMe29wqOgYFe83JcaG8icaMIZwHOvwrfDJhuaN3AejNObCskE0KFft0QmmVZw6lFZUHlb8LSYcjnmiMcOP7C11tTiNION8zUYUZF3tF9gXDi6VeQKmcl2csOMOt15X-rpJ6ukSKc3SJKMFaICbcz-yOTYA0e8ARLqmNLC_sis6A_wUDaG5GGhlS51XLfgrUcNmVKXYYNnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇹🇷
🇵🇰
رویترز:
ترکیه، عربستان سعودی و پاکستان قرار است روز جمعه یک توافق‌نامه دفاعی مشترک امضا کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69659" target="_blank">📅 01:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69658">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVACA7B_-ZFZMRBXczKgLy8YgMVso3P9ijLYBBhesIugwT-ZmtImm_HEgJn0aatzOy3WzEXn4OBACeQJQiVZAYsZvR-PP-Ed7s3glX6NZwz0y2WC3n-lGZvYIhypAacFqaZW_-4kYzoO0HETKJLjAKC-3iVynI-6OKg3x-w8tEtDIH5riddvQn-2mfMnwSjMlo4HUWauPvN4Kw16CZty33xHJSGm1kZTRWI_3qA7jnmbPxVv9G9pHKhBjEJ5kXB-nYhvOR1xTrdDU17khe3sCPccXuNBriRyVkLxQDpARpnLNsonJL_NTaMWcte5EgU9tbUkcbkf6y52huRaW97b5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سی‌ان‌ان:
🔴
یک مقام ارشد سعودی؛
اطلاعات موجود نشان می‌دهد سپاه پاسداران ایران در حال هماهنگی با شبه‌نظامیان مورد حمایت ایران در عراق و حوثی‌ها (انصارالله) در یمن برای تدارک حملاتی علیه عربستان سعودی است.
این مقام اظهار داشت که این گزارش‌ها به‌ویژه نگران‌کننده هستند، زیرا در شرایطی منتشر می‌شوند که ریاض در پی کاهش تنش و انجام مذاکرات صلح‌آمیز است؛
روندی که به گفته او، پیشرفتی مثبت داشته است. وی افزود که پادشاهی سعودی «برای اتخاذ تمامی تدابیر لازم جهت مقابله با هرگونه تجاوزی، درنگ نخواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69658" target="_blank">📅 01:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69657">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2I4yu2buQPHxHHSu-epW1hL4dfc5UOJ3SejxHZWr82EyPK-LNfRYoQlC9OAXrv2YbaJUty6UXWgxcW7acNrpN4w6KA5la4wShOebU-ooO6FEl7fErXa6OurHsgDEe1l7G9k1VU0XilyS0Nin0NdQ__PiavC6B20Gx4oSkZgFjIxo0s4Ut7USj9VLdd-77aQrWPkoqql-V93nkTXFOXMplJYWbUCNxegMNzC87sv4Se4XvpBWu_-iTqxWFO4MywrF_OsCFLP9MUuBEpU5SgxUUuMbbOY9HEot54OU4TBTePNWKUaiycP9j1RdP45dXVbkzoHzk2NZQ2dVkWAPGB_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
کانال 14 اسرائیل:
محسن رضایی میتواند خودکشی کند، ما برای او مهمات مصرف نخواهیم کرد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69657" target="_blank">📅 01:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69656">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac1c12b672.mp4?token=Xd0CYW8xDBByD4vA73YdulrPq9oqRT9Zp7SNNQWfpxtkpmHocl8llmrxwhpxaWbhTAHEM0oeHXxJ-r9D_WU1R2SfXkFH_2qaL-jTSfhprxalAgXEKST-sXQcLNl1tc-qzzDqYtopU2pq-YvX5hoBtqUBWnkn63Laea6OSb44UwVs5QIFokAtH9qu7jpKmKtWMIsWbFaUVNofXdyhcCF13a3mJbwwSe8Zb0aV6WY-zi_sQdFubbNhJdQYwkSO-Rtk7iT1pE8-MV_VASZ1ualOZdCw9__yoA0vCGXxhOyhetAAGTUs0U4CfC2nWFQ3Gfz4zomdaLcfpljqQ1cRBQmLKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac1c12b672.mp4?token=Xd0CYW8xDBByD4vA73YdulrPq9oqRT9Zp7SNNQWfpxtkpmHocl8llmrxwhpxaWbhTAHEM0oeHXxJ-r9D_WU1R2SfXkFH_2qaL-jTSfhprxalAgXEKST-sXQcLNl1tc-qzzDqYtopU2pq-YvX5hoBtqUBWnkn63Laea6OSb44UwVs5QIFokAtH9qu7jpKmKtWMIsWbFaUVNofXdyhcCF13a3mJbwwSe8Zb0aV6WY-zi_sQdFubbNhJdQYwkSO-Rtk7iT1pE8-MV_VASZ1ualOZdCw9__yoA0vCGXxhOyhetAAGTUs0U4CfC2nWFQ3Gfz4zomdaLcfpljqQ1cRBQmLKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
تفاوت اعلام مرگ دشمن از طرف ترامپ و اوباما:
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69656" target="_blank">📅 01:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69655">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7820062e8b.mp4?token=ojIi3AahdpDd7KIm6j_-UTUgrEsYsh7HN0N8NSnQ8A5BF_0gI4MYQCZbfuFBzfwFy-dQAHxgFbuIPn3ou3AY8S_L2o3D4ARdmLqb-J7JjNDVJVQa4-7cCkN1GaivEet7w8BtYhoOdwpKxjwHUGuW3AkFlayN38PSoDOOsI3javX7cmeaD-9iPsC5yPzHieLLH_rbh9VkahLBvTtBMZ_N48HlLEjdOEtq_XTbiiQYe4KKomE6ZlE0mdJJ9fNA6o2InMoq6iOX1ovQo7dndYUIpocRWplCuSgOenArqDCkKejkzV4-mjcFgQnITCqCFAH3MQe9RTdvZ4muW0-f8NBNyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7820062e8b.mp4?token=ojIi3AahdpDd7KIm6j_-UTUgrEsYsh7HN0N8NSnQ8A5BF_0gI4MYQCZbfuFBzfwFy-dQAHxgFbuIPn3ou3AY8S_L2o3D4ARdmLqb-J7JjNDVJVQa4-7cCkN1GaivEet7w8BtYhoOdwpKxjwHUGuW3AkFlayN38PSoDOOsI3javX7cmeaD-9iPsC5yPzHieLLH_rbh9VkahLBvTtBMZ_N48HlLEjdOEtq_XTbiiQYe4KKomE6ZlE0mdJJ9fNA6o2InMoq6iOX1ovQo7dndYUIpocRWplCuSgOenArqDCkKejkzV4-mjcFgQnITCqCFAH3MQe9RTdvZ4muW0-f8NBNyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آیا توافقی برای بازگشایی تنگه هرمز حاصل شده است؟
🇺🇸
ترامپ:
نمی‌خواهم بگویم [توافقی] حاصل شده، اما در حال حاضر کم‌وبیش باز است.
ما کنترل تنگه را در دست داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69655" target="_blank">📅 01:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69652">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6e63add2.mp4?token=rsNoACFizcS44IIz7EzPLesI8DUFh60y2KjF-fFSlCE-AEz6EDgMSSeMkpU-FPcImeRZonM4veLqIGAE0jjReMtPeIajEhIjJUSMX16Rni_WRSkPv0eVXuoQKYrI_nRr4xLFpIE55UMv7OVBSl-CZWfZOaSdZKyXd-j1eaPum7hfcKYrn6Fwj08ko3wDqjddqSxgGhAqpntT83-IIbtnxQFHgnx5YedSTSrUJM4p-tYCAHWqF1AE0EjaMf23CD6HtSI-Q5_NyzLVMnDfUEG6C0ycc1ros6u9NtJoh0oXdHEKLa4JOJZuNlf-8MkBiJVVr3lq6ovOMcPDKhb79Mr2qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6e63add2.mp4?token=rsNoACFizcS44IIz7EzPLesI8DUFh60y2KjF-fFSlCE-AEz6EDgMSSeMkpU-FPcImeRZonM4veLqIGAE0jjReMtPeIajEhIjJUSMX16Rni_WRSkPv0eVXuoQKYrI_nRr4xLFpIE55UMv7OVBSl-CZWfZOaSdZKyXd-j1eaPum7hfcKYrn6Fwj08ko3wDqjddqSxgGhAqpntT83-IIbtnxQFHgnx5YedSTSrUJM4p-tYCAHWqF1AE0EjaMf23CD6HtSI-Q5_NyzLVMnDfUEG6C0ycc1ros6u9NtJoh0oXdHEKLa4JOJZuNlf-8MkBiJVVr3lq6ovOMcPDKhb79Mr2qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
به نظر من، جنگ به زودی به پایان خواهد رسید.
فکر نمی‌کنم آن‌ها بتوانند این وضعیت را برای مدت طولانی‌تری ادامه دهند.
من درگیر مذاکرات با ایران هستم. اوضاع خوب پیش می‌رود.
ممکن است به‌زودی توافقی حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69652" target="_blank">📅 00:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69651">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed7984246.mp4?token=ZCIftbU3AQ30omoYnC-BzJLs6vxI2OYkN5r5zA2FPwXQwTqYjtLdLWdYUMlr9CMgvKJalRZzFZWO6_v1dNIJgxldL-d816AuS8cpW6LC64b68J-DttJG51MV19A7oFi2ya5sdujFfPRkTkziQFAIQ7GSRo8o0OTOSmgm5Pp0vvW919q7gSgiRBq2r38MwQpQ1oDh7r550WmYlZ4HQWhclAY5nhLkN8cM3tmO6SWohVEDvjSoy87Yvesx-A7keCdpyrTHLFZdNO1h3r839mEYkXouE0fn5ZUKbS-SNlXH-bM_5iU0z8NPTn_ANFVYPENJcptAxozeVMMv8KPCChFaYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed7984246.mp4?token=ZCIftbU3AQ30omoYnC-BzJLs6vxI2OYkN5r5zA2FPwXQwTqYjtLdLWdYUMlr9CMgvKJalRZzFZWO6_v1dNIJgxldL-d816AuS8cpW6LC64b68J-DttJG51MV19A7oFi2ya5sdujFfPRkTkziQFAIQ7GSRo8o0OTOSmgm5Pp0vvW919q7gSgiRBq2r38MwQpQ1oDh7r550WmYlZ4HQWhclAY5nhLkN8cM3tmO6SWohVEDvjSoy87Yvesx-A7keCdpyrTHLFZdNO1h3r839mEYkXouE0fn5ZUKbS-SNlXH-bM_5iU0z8NPTn_ANFVYPENJcptAxozeVMMv8KPCChFaYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حامله شدن دختر 20 و 18 ساله توسط همسر 50 سالشون!
🎙
خانوم دکتر:
یه آقای 50 ساله به همراه دوتا همسرشون که یکیشون متولد 85 و یکیشون متولد 87 بود، بهم مراجعه کردن.
خیلی جالب بود که دوتاشون با هم حامله شدن و میخواستن تاریخ سزارین‌شون تو یک روز باشه و این برای من خیلی عجیب‌تر بود
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69651" target="_blank">📅 23:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69650">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5609274449.mp4?token=sPodSI4EMZ0v85VhJOwPW7YgScnn_Y3kAciOwS5KdhNOiYW2m8ry3NBbUkEzdFJtkiSaYKnGnkpiTBIzupQafjqfyk26lVwhatbiQoCZt-3F1lDWheRguI4ca8WljlKy4pTFok1SQ9R6K5zFN6EPKYBV1W8QN-nGxMumzNQB9qXVs32PNLZf4PHqqVOYRHhMUQ3IT8aeSe5FD-lADmyZwgGneJkLkp01VYwF14x7G-dkr0eaaSkB1B_fDgmiXrg1zH1br0M1dLZ39K9k32TzjYHs-qmrutSM7J4b9rKRHDAbyndkUO-43qSimAsw8pQGtBEiHCkJWd1ctqVIroiKsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5609274449.mp4?token=sPodSI4EMZ0v85VhJOwPW7YgScnn_Y3kAciOwS5KdhNOiYW2m8ry3NBbUkEzdFJtkiSaYKnGnkpiTBIzupQafjqfyk26lVwhatbiQoCZt-3F1lDWheRguI4ca8WljlKy4pTFok1SQ9R6K5zFN6EPKYBV1W8QN-nGxMumzNQB9qXVs32PNLZf4PHqqVOYRHhMUQ3IT8aeSe5FD-lADmyZwgGneJkLkp01VYwF14x7G-dkr0eaaSkB1B_fDgmiXrg1zH1br0M1dLZ39K9k32TzjYHs-qmrutSM7J4b9rKRHDAbyndkUO-43qSimAsw8pQGtBEiHCkJWd1ctqVIroiKsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
انتقاد رونالد ریگان چهلمین رئیس جمهور ایالات متحده از جیمی کارتر در قبال رفتارش نسبت به ایران و شاهنشاه آریامهر:
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69650" target="_blank">📅 23:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69649">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kJpqaDoHjXLi0h1mMChPvwuhzzJJARbVRjB7_9tG_iSN3dLfOof7_X9N62zW5vk64hVAW_VVZ4C8u6ObgTEo0YD1oxBoMmcsbfzaxaM3NO-Qjzqc3HRIixBGL_dhcqIaBRek6k6aoisH1PxfzT4cctdOfwAAvsyS6zY_QuYJ1W1WzHnh9_52y6A4p3EP5RdhzwGNP7opcHDkQ-8FCdD6RAXztN0u832TgE7Noi3QM05Rff42LT5rxwiGT-DQJ0GEN-62vlBGEk_lxMqdByhBFGPDyEoGRFVEGGeRIOrUy0Jlh5SEq5mnJPjqQx_if5S27OMCQiA9xkUZWNagwK1kcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
«حمله‌ای عظیم در راه است... صبر کنید، بی‌خیال؛ آنها می‌خواهند مذاکره کنند.»
این همان نمایش دیپلماسی است که مدام تکرار می‌شود.
استفاده از زورگویی، وعده‌های نقض‌شده و اخبار جعلی به‌عنوان اهرم فشار، راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید. ما به نمایش‌های بیشتری نیاز نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69649" target="_blank">📅 22:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69648">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/164214744c.mp4?token=YSGrL1BWmmKuPGbEtujFwkqOWhCwkWwpU_lBxUeweAomNKbXTmt6_kqgc16EPRhWC9sjAp5Yd2BIaVl_NoGNYTLBR8xGUr2UyHlPLI3U5nsZYjnM5zldCyw-3qqHQ36dORiUV9O-OicNMMvBnb4TiaKmP6X9X2xvxaqTI8lOdk2tkFPOXe4ICKb3RVJrgD_kh16ZtDHkhDC6RkCJ3BhTmF9SKFPIR1WpG7NwzCjvomkc6ZBjg6alGSGqLZeFeifNg1JbJv9835rV7xawi9paAKDY7jrW5YpU4p5SpJveVptYC2fkIJKyqQrTKnxYjzqO46efzr7and00NS7lYLevRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/164214744c.mp4?token=YSGrL1BWmmKuPGbEtujFwkqOWhCwkWwpU_lBxUeweAomNKbXTmt6_kqgc16EPRhWC9sjAp5Yd2BIaVl_NoGNYTLBR8xGUr2UyHlPLI3U5nsZYjnM5zldCyw-3qqHQ36dORiUV9O-OicNMMvBnb4TiaKmP6X9X2xvxaqTI8lOdk2tkFPOXe4ICKb3RVJrgD_kh16ZtDHkhDC6RkCJ3BhTmF9SKFPIR1WpG7NwzCjvomkc6ZBjg6alGSGqLZeFeifNg1JbJv9835rV7xawi9paAKDY7jrW5YpU4p5SpJveVptYC2fkIJKyqQrTKnxYjzqO46efzr7and00NS7lYLevRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان:
پزشکیان: ما بچه که بودیم پنکه نداشتیم
مجری: آخه آذربایجان خنکه
پزشکیان: من تو زابل خدمت میکردم
مجری: آخه شما میگی وقتی بچه بودم
پزشکیان: من تو زابل خدمت میکردم و پنکه‌ام نداشتم، حالا چی میگی؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69648" target="_blank">📅 22:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69646">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
گزارش غیررسمی از شنیده شدن ۲ صدای انفجار در قشم  @News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69646" target="_blank">📅 21:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69645">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
گزارش غیررسمی از شنیده شدن ۲ صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69645" target="_blank">📅 21:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69644">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c949993e0a.mp4?token=r-KYJiQp4FwyQsq23bsTS-ArnYu7VimEZXdlAN1uICGWkI8sARr-yX0qPaE43H2CVTtFHHOy1GBNuPP5GeJhuy_XOs7Tn58LpfiUOzKhq74-rl0LSnLXW5SVjls1i4IPBfmJiYAru0Mmvv4qqwcV-mWfPNSQzRBOIJ3lHUKJj7IR1OpKdZaC4voHWANyP1F0Z-r48besmJt8ptgrlV9pC3U1LzAv5EsD94boEyRiGJnMY4eYPwp_RFRzHH48kJMoZGs7Qr8hweaP63EciR-QXjFjZYIeHRQ9u3TE17p8A6eK9htiaqP4L4aeNJAtrAK3Ya83xhq05aPy0HW7LgmX-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c949993e0a.mp4?token=r-KYJiQp4FwyQsq23bsTS-ArnYu7VimEZXdlAN1uICGWkI8sARr-yX0qPaE43H2CVTtFHHOy1GBNuPP5GeJhuy_XOs7Tn58LpfiUOzKhq74-rl0LSnLXW5SVjls1i4IPBfmJiYAru0Mmvv4qqwcV-mWfPNSQzRBOIJ3lHUKJj7IR1OpKdZaC4voHWANyP1F0Z-r48besmJt8ptgrlV9pC3U1LzAv5EsD94boEyRiGJnMY4eYPwp_RFRzHH48kJMoZGs7Qr8hweaP63EciR-QXjFjZYIeHRQ9u3TE17p8A6eK9htiaqP4L4aeNJAtrAK3Ya83xhq05aPy0HW7LgmX-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
تصاویر اولیه از تاکسی پرنده‌ای در چین که قراره به زودی شروع به فعالیت کنه...
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69644" target="_blank">📅 21:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69643">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slIzB-M1TYVpr0xLTieDEvIFs9X516Vg1DihzzphWTHbGpJ1LKhINtHoUcliLqRJQg4ggA5Togo6bOlbKfFVZZL6CJLw5kMyRgCj2Rmxhsv9wsKbpRz3I6wZnk_OXU_i0igg7qQfeSGRPaAvuSwH-4GdqePq8FgbBCNk3yorscWKCya20k825m6jhcrg6-wLrAPYmpeqaOCWc2m4fgsGRpZHb0SuLJ1a9HSeIuqkEh5a0kQ2AhLMNGZOLpuL6dVQPHcokS26ugEPp4k3cm5q62mhsU8JkbUEYLbJK57J3tyBbeFNWcsOWxRWadodWCJ6NcYCfIRpCatgVGdLuQEocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
خبرنگار الجزیره :
تنگه هرمز: به نظر می‌رسد توپ از زمین ایران و عمان خارج شده و به زمین آمریکا افتاده است و اکنون چشم‌ها به رئیس‌جمهور ترامپ است تا در مورد جزئیات باقی‌مانده و تعهدات آمریکا تصمیم بگیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69643" target="_blank">📅 20:49 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69642">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaVObziZG6nWo1a9iXKcKty1I-xd-6sujkl3omTRWni6U-sma4hiqYhLcDIPrbAVgv4ktAswXPctCMDXL1t4kC8OkgvGYQpOajeCXxdMA5TSucy6GGyx5y74gjpoBv6DIuleq9E1aZUKYpShcm5GMgdQGn3xLakYhK0egLqpUd9AdEyey9j77mPrpY_t2EQI9szbVGTqnexxvc3ljF-ieTE1jrg3a05pw8iwJmtr-vV7OzOfuKJTGEGROT1cB2wgAMtdcGXjjR_AOvDqrQNcEBFC8lx-NWw-Kt4_VQLo8bn5qL2BuA3EE3YTHfG1hZCTfSUhYIGJ3_YRkGrtoaXRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
رسانه‌های «اخبار جعلی» طبق معمول در حال پخش شایعاتی نادرست و کاملاً بی‌اساس هستند.
من از عملکرد «پیت هگسث» بسیار راضی هستم.
همه چیز فوق‌العاده پیش رفته است، از جمله عملیات ما علیه ونزوئلا که نتیجه آن در کمتر از یک روز حاصل شد و به ما امکان داد تا یکی از بدترین جنایتکاران جهان، یعنی نیکلاس مادورو، را به دست عدالت بسپاریم!
در مورد ایران نیز وضعیت بسیار خوب پیش می‌رود؛ کشوری که با هدفِ «جلوگیری از دستیابی‌اش به سلاح هسته‌ای» در هم کوبیده شد!
پیت در میان نیروهای نظامی از احترام بالایی برخوردار است و پیشرفت‌های چشمگیری ایجاد کرده است؛ از جمله حذف سیاست‌های DEI (تنوع، برابری و شمول) و افزایش آمار جذب نیرو به سطحی بی‌سابقه.
این شایعه توسط «واشنگتن کام‌پوست» (Washington ComPost) — که یکی از بدترین رسانه‌های این حوزه است — به راه افتاد؛ آن هم با وجود اینکه ما به آن‌ها گفته بودیم گزارششان کاملاً دروغ است.
در واقع، من عمیقاً معتقدم که «گزارش‌دهی» جعلی آن‌ها مصداق خیانت است!
رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69642" target="_blank">📅 20:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69641">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d50525385c.mp4?token=QFCcM_6M9SWgLgvi8lk6WdGyR4HtKZbOH6KAjvoNnabxHxCqslp-0Awx8dH8pz7OjfFQM2mk5q-hlS8JzmPrVsnOa6sFGGZp0IcGFtXYP2X91u3Cv03p6d3Wr4IjDq3ErBFVh0ZUeViT0MPbuA0-5KjKnEaqUEQjWryqeFQqo9667TrGFRSyMLjUTa7zZFYFTU2acfRx0Hl-g6vmBIagGWhNDOoscmaXTSyH72Rf2OdEtC0RDp1sgy3u8IqSBSutPaYYvEqBqLMO1T4PIbH2D_XHAOxLeFr2Jv4DFKOihh-68UgdsfZHWKfU_jKfd0mnVUY4YmiAsy-iIN_wiHqRIYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d50525385c.mp4?token=QFCcM_6M9SWgLgvi8lk6WdGyR4HtKZbOH6KAjvoNnabxHxCqslp-0Awx8dH8pz7OjfFQM2mk5q-hlS8JzmPrVsnOa6sFGGZp0IcGFtXYP2X91u3Cv03p6d3Wr4IjDq3ErBFVh0ZUeViT0MPbuA0-5KjKnEaqUEQjWryqeFQqo9667TrGFRSyMLjUTa7zZFYFTU2acfRx0Hl-g6vmBIagGWhNDOoscmaXTSyH72Rf2OdEtC0RDp1sgy3u8IqSBSutPaYYvEqBqLMO1T4PIbH2D_XHAOxLeFr2Jv4DFKOihh-68UgdsfZHWKfU_jKfd0mnVUY4YmiAsy-iIN_wiHqRIYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
دیشب روسیه هم یکی از سنگین‌ترین حملات خودش رو علیه اوکراین انجام داد و اينجوری کی‌‌یف رو ترکوند!
4 فروند موشک مافوق‌صوت زیرکن/اونیکس (3M22 Zircon/Oniks)
24 فروند موشک اسکندر-M و موشک‌های شلیک‌شده از سامانه S-400
115 پهپاد تهاجمی، از جمله پهپادهای شاهد (که بیشترشون از نوع جت‌دار بودن)، پهپادهای Gerbera و Italmas، و همچنین پهپادهای فریب‌دهنده Parodiya
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69641" target="_blank">📅 20:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69640">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am-E0sY4es1Dx_9ideTA5If-NB4JpYTOAwKHV6HReZuLQRmSUkVOyj4LioBffot19OhJkA--7v7T8eZn9tlulcKGjeICOxT6ueCfApFBgpE_T0TS_YFOea7MdlkDIHqyf-XYV8f_h-j9Zob-xiFlvDeDhYli_skvQ4vlJLA-6sj82nbMknTo7scYtOcc3UO_jEFq1PNHQglVVHItaXlBvkvpbo4shfsRT5e6zTgN4DgJ6sCcEw2ftA8LSQ8luStG6ugvuy6CsI-OhzQ7tFou95xrAVyJeITuTsHoh0ZmYIde8gz6VKzWWthowWFIsgDqFyV7MaD3pNJSFLfGqLRvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
پس از استعفای محمدباقر ذوالقدر، فیلد مارشال محسن رضایی به‌عنوان نماینده رهبری و دبیر شورای عالی امنیت ملی منصوب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69640" target="_blank">📅 20:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69639">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇴🇲
سلیمی، عضو هیئت‌رئیسه مجلس: متن اولیۀ طرح «اقدام راهبردی تأمین امنیت و پیشرفت پایدار تنگۀ هرمز و خلیج‌فارس» در کمیسیون امنیت ملی در دست بررسی است.
🔴
براساس این طرح: عبور شناورهای متعلق به آمریکا، رژیم صهیونیستی و سایر کشورهای متخاصم از تنگه هرمز ممنوع…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69639" target="_blank">📅 19:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69638">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇴🇲
سلیمی، عضو هیئت‌رئیسه مجلس: متن اولیۀ طرح «اقدام راهبردی تأمین امنیت و پیشرفت پایدار تنگۀ هرمز و خلیج‌فارس» در کمیسیون امنیت ملی در دست بررسی است.
🔴
براساس این طرح:
عبور شناورهای متعلق به آمریکا، رژیم صهیونیستی و سایر کشورهای متخاصم از تنگه هرمز ممنوع می‌شود.
محموله‌های مرتبط با رژیم صهیونیستی، اعم از نظامی و غیرنظامی، حق تردد از این منطقه را نخواهند داشت.
شناورها یا محموله‌هایی که در اقدامات علیه جبهه مقاومت نقش داشته باشند نیز مشمول ممنوعیت خواهند بود.
کشورها و اشخاصی که به ایران خسارت وارد کرده‌اند، تا زمان جبران خسارت، مجوز عبور از تنگه هرمز و خلیج فارس را دریافت نخواهند کرد.
برای قانون‌شکنان، جریمه‌های سنگین از جمله تا ۲۰ درصد ارزش محموله، پیش‌بینی شده است.
دولت موظف خواهد شد با همکاری نیروهای مسلح، مسئولیت‌هایی مانند هدایت ناوبری، نظارت بر تردد شناورها و حفاظت از امنیت و محیط زیست خلیج فارس را برعهده بگیرد.
این طرح همچنان در مرحله بررسی کارشناسی قرار دارد و مجلس از صاحب‌نظران خواسته پیشنهادهای خود را برای تکمیل آن ارائه کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69638" target="_blank">📅 19:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69636">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a34485680.mp4?token=JRI9HbfH2fnHQVefqDnG5ILqmIO4vmiOAYEjHoH_TJ4Te1tvhBBDzdjfWlD4a1U7ONfnVF-aiQ9rAaIZNritmLWyxq0rbkf80NIxhTYoukAKoa1sqoUAUTfE0_Nk-sG6VhINXDNcWNuhR4IlOjUoPW9vk3LTD_Y5yaWTvA2SFW4T9hwv8xDlCTtJfcJgbu3WbBEss-zqBFb-kaktnm1jwpXYV-hxAVSYx2nraOpMVMhgGfjU2iXwvSuBVCXlPSwSzuDyB4F8YkFlNAZpgC6wCPScYlI8YmG9TYaaSLMrhTgc5Y205Mx39UzMSfyWu4byJL7rcShME8N6zoYZmUN9RK6NmGe_G73-DeWwcCOrOb9ah5ZMyL1g7QiUdicN0TowDmQrQ2zDFLLDWSfXJaPMrwuCJZpYvCZasxAbBc50Dgv_PJmTi_lqABe4Wj_PPk1rRFgPSdljqxNNCR0yYU7VQx3_B-XvlbMzdL25obsDqUhBpnflit2MkskT2sPKobaBuHaxjwQH2EutneCZV7k_e_Fbdt1bI98-Dq9IKVofn2IwhXIMWsK3xA_jK1GNiu1bSz26JKAyIQueZ3HGaHSBs3fH9aU1OPZZGB9Zybx1UCJNHK1lAKFdBezgDWTgQ4WJ6rjZrAinIjhbW-XVyPeLpBtzMdkUElZyxbvwfbts9uI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a34485680.mp4?token=JRI9HbfH2fnHQVefqDnG5ILqmIO4vmiOAYEjHoH_TJ4Te1tvhBBDzdjfWlD4a1U7ONfnVF-aiQ9rAaIZNritmLWyxq0rbkf80NIxhTYoukAKoa1sqoUAUTfE0_Nk-sG6VhINXDNcWNuhR4IlOjUoPW9vk3LTD_Y5yaWTvA2SFW4T9hwv8xDlCTtJfcJgbu3WbBEss-zqBFb-kaktnm1jwpXYV-hxAVSYx2nraOpMVMhgGfjU2iXwvSuBVCXlPSwSzuDyB4F8YkFlNAZpgC6wCPScYlI8YmG9TYaaSLMrhTgc5Y205Mx39UzMSfyWu4byJL7rcShME8N6zoYZmUN9RK6NmGe_G73-DeWwcCOrOb9ah5ZMyL1g7QiUdicN0TowDmQrQ2zDFLLDWSfXJaPMrwuCJZpYvCZasxAbBc50Dgv_PJmTi_lqABe4Wj_PPk1rRFgPSdljqxNNCR0yYU7VQx3_B-XvlbMzdL25obsDqUhBpnflit2MkskT2sPKobaBuHaxjwQH2EutneCZV7k_e_Fbdt1bI98-Dq9IKVofn2IwhXIMWsK3xA_jK1GNiu1bSz26JKAyIQueZ3HGaHSBs3fH9aU1OPZZGB9Zybx1UCJNHK1lAKFdBezgDWTgQ4WJ6rjZrAinIjhbW-XVyPeLpBtzMdkUElZyxbvwfbts9uI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی تهران برای افراد بالای 30 سال هم مهد کودک زدن !
یعنی شما صبح که از خیابون داری رد میشی ممکنه یه مرد 40 ساله با کوله پشتی عروسکی ببینی
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69636" target="_blank">📅 19:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69633">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSnW1ORTTc50gKeOPVjHHB-hBZmzrFZg492ukynvKZAQDwIuhkTT1LQAMd76oaQhnIzRQh3dB79HA2DrlX4w89ejNueFZW-L_htFOFy0hwSfyqEBVZvlrxDti4qPMfiKZ9_9Yv0mL4eGsBay4IAKun95TZJD8ePf19DrLBgoOVwVKt9hpNljqgtnCXjRBhrQvDC_2ztmu-yuzE08pGt4yMa-WeJ0v6u08NetLx_kMSYq7aPKjFGLoai4CIkO-gQNNRo5mcV0k4meGOY-VDSW9X2Y8v1kqGGVrD4aTN0Gn7sLGA9d9SMYTQhXMGEXbij4e3-CwxT92q0UP7FqCIX0Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a607d311.mp4?token=moRHrxVUnIxUMKeGbxA_tkxu9zKkTE2E1B26FobNBxwwjDFaoR0wGpyE6kTJGbFE7Ff8xcGYJB8sU0x20GXyUwVTwjsO4ag9_DN4uxmx3dLBhCTDvbtPKV1hcu8xbtCLQEzuJJDS7LKQ8Q2t5tDn8wp7GpyOFVlahT47rhn_FRQIONRcjiaY1_gX-ZCr0ZW9Oa_T1IOPCiGSrxKHJ54XoZruFZqMYpM94Ncv_W6phoeJ4fyZ5xOyvLmwboN4OQByC-VgxhQDZTCgNob7-sD1vX2fmuJ35g2Ta98H9qPHrpc4GlPPfUzPH0WjpjYhXELy66lSCs6fwrN90z_kueeNyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a607d311.mp4?token=moRHrxVUnIxUMKeGbxA_tkxu9zKkTE2E1B26FobNBxwwjDFaoR0wGpyE6kTJGbFE7Ff8xcGYJB8sU0x20GXyUwVTwjsO4ag9_DN4uxmx3dLBhCTDvbtPKV1hcu8xbtCLQEzuJJDS7LKQ8Q2t5tDn8wp7GpyOFVlahT47rhn_FRQIONRcjiaY1_gX-ZCr0ZW9Oa_T1IOPCiGSrxKHJ54XoZruFZqMYpM94Ncv_W6phoeJ4fyZ5xOyvLmwboN4OQByC-VgxhQDZTCgNob7-sD1vX2fmuJ35g2Ta98H9qPHrpc4GlPPfUzPH0WjpjYhXELy66lSCs6fwrN90z_kueeNyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69633" target="_blank">📅 19:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69630">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47221b6a95.mp4?token=qO8gxhP222Zv_2FXO0s28MsfpZJdkxqDM4v3vWSmi1E_gJlFqdoGJkhkl1Rb0_15u8GOgaxLja75S6h2bX2tX0wDpx3MLRtqw81nLQcCVepzEW0NNKjfh687TX9t6Tylo90-M0J6B0rMpONUKtMhgHO1P_bw-RJMMFp0itdm97-zOXyb4y4A7YqEYdFvGzkvqSbsNCLaEb80Dx2-7qaebYXPy2GThhpbQuJ75SIidTS7FJnbAnQGm4KPM7sHzGST3l6RhM2VqVWdaEinlHWrqmdWgfKMqCnqd4BU0BoGa284TMlfACf56ciUYnduWxrfdimNJRQS_X8K0NNfut7L_BgQ_NGYk-mD5RZlBGLfpr3JvRFlJioQIqOukRUc707AlgntsyNaRMqYjiXM34MYYumwkObHuNYQNPRKrGO9WPG1nc47W4BZJL8YjEjBUbg0ZvCtc2JWIZFqg8QPeiRWIEShhUUVEg3nUKB_qSR1Pm0pxGQgs4HVCxmn00zyyGqZqBS4YUK50eUoINj2NT0ymEfrEskeJGxcrcooOUG7FDJltP10b2OLsAwH1Xo00jZxZzi-ZH2OKRYqJmZe35o5qDz4nHZ-d3VYn5A3hEdF33qW0qpV8-unlbVGlIw-wxQhxkOIz4GJVZspjnGYa7-G2ZLY5W_B5cdFi8HgG5LtW50" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47221b6a95.mp4?token=qO8gxhP222Zv_2FXO0s28MsfpZJdkxqDM4v3vWSmi1E_gJlFqdoGJkhkl1Rb0_15u8GOgaxLja75S6h2bX2tX0wDpx3MLRtqw81nLQcCVepzEW0NNKjfh687TX9t6Tylo90-M0J6B0rMpONUKtMhgHO1P_bw-RJMMFp0itdm97-zOXyb4y4A7YqEYdFvGzkvqSbsNCLaEb80Dx2-7qaebYXPy2GThhpbQuJ75SIidTS7FJnbAnQGm4KPM7sHzGST3l6RhM2VqVWdaEinlHWrqmdWgfKMqCnqd4BU0BoGa284TMlfACf56ciUYnduWxrfdimNJRQS_X8K0NNfut7L_BgQ_NGYk-mD5RZlBGLfpr3JvRFlJioQIqOukRUc707AlgntsyNaRMqYjiXM34MYYumwkObHuNYQNPRKrGO9WPG1nc47W4BZJL8YjEjBUbg0ZvCtc2JWIZFqg8QPeiRWIEShhUUVEg3nUKB_qSR1Pm0pxGQgs4HVCxmn00zyyGqZqBS4YUK50eUoINj2NT0ymEfrEskeJGxcrcooOUG7FDJltP10b2OLsAwH1Xo00jZxZzi-ZH2OKRYqJmZe35o5qDz4nHZ-d3VYn5A3hEdF33qW0qpV8-unlbVGlIw-wxQhxkOIz4GJVZspjnGYa7-G2ZLY5W_B5cdFi8HgG5LtW50" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
🇱🇧
ارتش اسرائیل (IDF) اعلام کرد که در ۲۴ ساعت گذشته، مجموعه‌ای از حملات را علیه "اهداف حزب‌الله" در مناطق جنوبی لبنان انجام داده است. این اقدام در پاسخ به انفجار بمب در منطقه مجدال زون انجام شد که در آن دو سرباز ذخیره اسرائیلی کشته و چهار نفر دیگر به شدت مجروح شدند.
ارتش اعلام کرد که این حملات، انبارهای سلاح، مراکز فرماندهی و سایر زیرساخت‌های حزب‌الله را هدف قرار داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69630" target="_blank">📅 18:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69627">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gD5iTx_rmw3zhCSNGMutGEPmTAlovysmdFJMpMgYscGGbVBH8OUYAhF7xybSlIGnTOSAsRqT1IxaOxJb4lUTsn3EMZ7R9z7w0s2S-_sY353Xg3_xWNM5cvQlEcV82aAd6e7sdRDrEOlTQFaJZTDYcPR6r3fKm11dqOjgxqbWRtrwzHLvlHtMhZ4wvvhLab9BvuHae3WacZMh-T851Tp0X2UjrvjmsUIM32vlPK3CEILA9hbXrDPsR7LOqCDsXWsyf5LCD7oPtm89LXru89p8Gg4bCD4vXKWz8qjpaC3AMh7noPyztfhwVN_hclYBMr8QX8PI499Re5XLDvvXsszezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb7351e85c.mp4?token=i2Sceas6KsPCRkhfjuMHRQf0MgiMXEBFR1C5AMOPTbozRL_0t4ABf-V46GCfocUonh4Gg9lpqNmEoVgt8YRcNHea6W9BiSquQT2WX_9CdADyAZiiD5Cwzms0kfKphZ0Ir6h2FEpUK5i_1rXhPgAe7CpzHUoy2VxiUv6qVgLrqLSOaGApltdWZxjjoHec5eA5RHJqu5-3hV93IYHjuPDBtVKrwqfpUzL43m7CHDfD90NzuE2cq98ubImCXgPyERICejINj8gVOkJDgsQnFSaiERj3sjDB8TEnhYGPcQFEbN2jV-gQyAACc-C67zSrKIUgVZPhdW7jWnRouVEf8rXu4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb7351e85c.mp4?token=i2Sceas6KsPCRkhfjuMHRQf0MgiMXEBFR1C5AMOPTbozRL_0t4ABf-V46GCfocUonh4Gg9lpqNmEoVgt8YRcNHea6W9BiSquQT2WX_9CdADyAZiiD5Cwzms0kfKphZ0Ir6h2FEpUK5i_1rXhPgAe7CpzHUoy2VxiUv6qVgLrqLSOaGApltdWZxjjoHec5eA5RHJqu5-3hV93IYHjuPDBtVKrwqfpUzL43m7CHDfD90NzuE2cq98ubImCXgPyERICejINj8gVOkJDgsQnFSaiERj3sjDB8TEnhYGPcQFEbN2jV-gQyAACc-C67zSrKIUgVZPhdW7jWnRouVEf8rXu4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
زلنسکی:
امروز صبح دو پالایشگاه‌ مهم روسیه رو هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69627" target="_blank">📅 17:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69626">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67d7912f58.mp4?token=dBpKGXKPX3Gt6hIB5gOlaluHs4wNZL6v0iZdf3vBjEcPOCjU0epcsj-jBx8-u6zZ3A11pdVK88yn3yfgSE9nJcDR4rZnM_J7C58JnO-vK7ZeyqDsgsx2LcKp6mQzxBgscwwxkSt35frON7l-6eBT3TOKjmju7HfhUjsUqtu6_QW9axPkhBqqWytR9AwcFETZomLKCc5I7ZcpONXXHuT-5diCY94MyTeH0aeBA7d1zqVhioLlVxH5DitAoUJtH9UhxpgYb-T9eorN9pLOGWv0KjG4mwGfPjW4I1RF4IbCjtyFEN1BeJwjzyCOZKcACpDdqCNAdc0vjv_Nm4_znvtQspy2QTVbjHu-1k-GQAPb3OPGOQaSDCF--q4BpM_7OMDcyh91b-BOJF_0oXedUzi8gWeBSWofmkWER-pzLIozRFwbkwXFS9GejO-t8ks5Uva4R4tsv0PFiBCPAMSnMJQPA5r833X4L44HBdWjqjXE_OOQM7zQ9PFBA4oKt9GVcKyNbImlbN9DdI0BqQXCsY26v0EtJ7DJU9A0qigQM6POcyQsOjBm3y-n9CAsu6BxSMRHO9q0SJdmRbxKv26sVqhvhltZUxzG5Fo4UzM-lOfrA24RLnO1A7oxJRBCcpQu2KZiluSAxXRB5teFH7cdysscWsk3w4dQvssronmme9NR-CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67d7912f58.mp4?token=dBpKGXKPX3Gt6hIB5gOlaluHs4wNZL6v0iZdf3vBjEcPOCjU0epcsj-jBx8-u6zZ3A11pdVK88yn3yfgSE9nJcDR4rZnM_J7C58JnO-vK7ZeyqDsgsx2LcKp6mQzxBgscwwxkSt35frON7l-6eBT3TOKjmju7HfhUjsUqtu6_QW9axPkhBqqWytR9AwcFETZomLKCc5I7ZcpONXXHuT-5diCY94MyTeH0aeBA7d1zqVhioLlVxH5DitAoUJtH9UhxpgYb-T9eorN9pLOGWv0KjG4mwGfPjW4I1RF4IbCjtyFEN1BeJwjzyCOZKcACpDdqCNAdc0vjv_Nm4_znvtQspy2QTVbjHu-1k-GQAPb3OPGOQaSDCF--q4BpM_7OMDcyh91b-BOJF_0oXedUzi8gWeBSWofmkWER-pzLIozRFwbkwXFS9GejO-t8ks5Uva4R4tsv0PFiBCPAMSnMJQPA5r833X4L44HBdWjqjXE_OOQM7zQ9PFBA4oKt9GVcKyNbImlbN9DdI0BqQXCsY26v0EtJ7DJU9A0qigQM6POcyQsOjBm3y-n9CAsu6BxSMRHO9q0SJdmRbxKv26sVqhvhltZUxzG5Fo4UzM-lOfrA24RLnO1A7oxJRBCcpQu2KZiluSAxXRB5teFH7cdysscWsk3w4dQvssronmme9NR-CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇰🇵
🇺🇦
روسیه در حال آموزش نیروهای جدید از کره شمالی است احتمالاً به منظور آماده‌سازی برای عملیات آتی در اوکراین.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69626" target="_blank">📅 17:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69625">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d7f55ab9.mp4?token=LuM3IGPSQL3sGBDF6BJuoof05buw6JizETNM5FELna3FvY9rW0tuXkWuagk8oORq7h7q2J-1wReHa7Knjr3TSVlhSvTV-hcrcIbq8L01iOo1W3uePqCnSIec5GNImhHbhfyE9B0y3Wc-Um_oLWgtYFtzSv6XzkTjWyWt5ppLq7NEYZm79D9320qI0RG9nBtNFfk7cPYehYQpt2BG_wB13b1yn2sehOlb07FhNfRBgzg1Lz1oUZ0SNT3JB8gAjoeqEHFFUONMPHL1hq6NLLtBD9FTm3eBnAhIqZ03wsR9YlkX0-_wVSVDf_3rfX56W5gqH-ivClqBoQT0zQUPdzK1Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d7f55ab9.mp4?token=LuM3IGPSQL3sGBDF6BJuoof05buw6JizETNM5FELna3FvY9rW0tuXkWuagk8oORq7h7q2J-1wReHa7Knjr3TSVlhSvTV-hcrcIbq8L01iOo1W3uePqCnSIec5GNImhHbhfyE9B0y3Wc-Um_oLWgtYFtzSv6XzkTjWyWt5ppLq7NEYZm79D9320qI0RG9nBtNFfk7cPYehYQpt2BG_wB13b1yn2sehOlb07FhNfRBgzg1Lz1oUZ0SNT3JB8gAjoeqEHFFUONMPHL1hq6NLLtBD9FTm3eBnAhIqZ03wsR9YlkX0-_wVSVDf_3rfX56W5gqH-ivClqBoQT0zQUPdzK1Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
خرازی(برادر زن مسعود خامنه‌ای):
«آیت الله مجتبی خامنه ای سه سال از دفتر رهبری طرد شده بود.
برادر وحید حقانیان(از اعضای بیت رهبر شهید) عضو سیا بود.
پزشکیان الدنگ و پرت است.
قالیباف هیچ چیز از دین اسلام نمیفهمد.
خدا لعنت کنه دکتر مرندی(پزشک علی خامنه‌ای) ملعون.
دفتر آقا فاسد است، حتی دکترش هم فاسد است».
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69625" target="_blank">📅 16:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69623">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/761165b2c7.mp4?token=FHqL4e9_hrOhUsozUVH-bMG7KbrkZYB6FMiyyS0DcE4xOweHzF5Z7qOZWhp2vc3gq-X09q5bFATz5VW3iHlS2lv6--nEgcQo-pGEPgaTE_o_hUj5MiRvuwYMZ5oTvIKhLZsuHrgzWa9sfDAckMfCP9gFojjzIJl9eOaMHz5xKP1P8duV8hbKKicviO3VABtK5h2f-s_14ZAXRcP_Kdg3TjWQu03_X4n1Tk603KbtmlE5wBAskiNG7SZLAnvxYXVXKYFIT4T3bj4gAtpre-cjgEnPIBhQ072JqPjKphnhuPhX0s0CjkIJxnQWE7PZO6DsQj-hGFHKMvEgSy3J3YTryg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/761165b2c7.mp4?token=FHqL4e9_hrOhUsozUVH-bMG7KbrkZYB6FMiyyS0DcE4xOweHzF5Z7qOZWhp2vc3gq-X09q5bFATz5VW3iHlS2lv6--nEgcQo-pGEPgaTE_o_hUj5MiRvuwYMZ5oTvIKhLZsuHrgzWa9sfDAckMfCP9gFojjzIJl9eOaMHz5xKP1P8duV8hbKKicviO3VABtK5h2f-s_14ZAXRcP_Kdg3TjWQu03_X4n1Tk603KbtmlE5wBAskiNG7SZLAnvxYXVXKYFIT4T3bj4gAtpre-cjgEnPIBhQ072JqPjKphnhuPhX0s0CjkIJxnQWE7PZO6DsQj-hGFHKMvEgSy3J3YTryg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
❌
🇸🇦
در حملات موشکی یمن به مواضع نظامی عربستان تاکنون بیش از 30 کشته شناسایی شده و انتظار میره تعداد تلفات بیشتر بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69623" target="_blank">📅 15:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69622">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🇮🇷
🇴🇲
الحدث:
توافقی میان ایران و عمان در خصوص بازگشایی تنگه هرمز در ازای احتمال لغو محاصره آمریکا، قریب‌الوقوع است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69622" target="_blank">📅 15:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69621">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuAf-M0tdpiBkIhVqUwvxRCjJTJjuKMl7r0jvVyZMR7BBavGQUq9vsFZhLXSdxoLsjzdKfKmBfcGngNyaZ2NzMMaI2VjpIjLheH7TbnSfQgUyowidX0v7Wd6O-5CPsmDuMr3wCiXfaCFJOd2kCHEp3PzzxcMC6_UN6OTgI8fSJxDv56vbf9I8T0bRNrFIMga3-_XLQTLC9Q8Fn4w6-Pc9PGYnxaxPhKEcbm9ik2Wt07DPU-pEfPTOpmd9o0vnt9a1Lg1GxsmujFDZRQXlmWrCMTzzHtKqFlVOBVr4De4aEiWRG_QuPI439puQ_ob9tTsnOzw0esCg8wlvVSXS_B7Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
🇺🇸
واشنگتن پست:
🗣️
ترامپ به طور خصوصی به حامیان مالی جمهوری‌خواه خود گفته است که می‌خواهد جی‌دی ونس در سال ۲۰۲۸ پیروز شود
و از عباراتی مانند «ما باید جی‌دی را انتخاب کنیم» استفاده کرده است.
مشاوران تأکید می‌کنند که او هنوز به طور کامل در مورد جانشین خود به توافق نرسیده است و هنوز رقابت بین ونس و مارکو روبیو، وزیر امور خارجه، را حفظ کرده است.
🔴
یک منبع این موضوع را اینگونه خلاصه کرد:
«جی‌دی دارد به موفقیت می‌رسد و ترامپ آن را می‌بیند.» و خاطرنشان کرد که ترامپ دیگر به طور معمول نمی‌پرسد «جی‌دی یا مارکو؟»
البته او با مشاورانش همچنان برای این انتخاب در حال مشورت است
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69621" target="_blank">📅 15:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69620">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoXNjBlQE2FxQM0jWgoft4xaThbpzXdQ2G2N8Zz1YpnGVMWvv6pEEJ8tGV3DLpa-MmpJwIY_OFl2ov7pjTXmyh7h9Apm3nf_HoEHx8BKtAJa8G2ZdV2UCAxg9JYFzBP3V0aNX-txUDyezRfTjLRlhhF6dmL489xbWos8zJb-Icr9qD4iZK6nYhcl63BpmQOuNJ6DUrwWLOyMUG5w0WPnUVcqY5A1Ofd60M1z3xbeYJhTEF3RtUd0-q6vRwAu28nO2PdpBpG5Qjl-r1jxPRPZgwBjgIFlGzqORhbbbcm5vDx5-0XGWHPSVxdWJkeHVgY7GBXU0Hq5ZsEa3FyD_rk9gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
آمریکا از ناوشکن جدید کلاس Arleigh Burke Flight III؛ USS William Charette رونمایی کرد
نیروی دریایی ایالات متحده مراسم به آب‌اندازی و نام‌گذاری ناوشکن جدید
USS William Charette (DDG-130)
را برگزار کرد. این شناور از نوع
Arleigh Burke-class Flight III
بوده و بخشی از برنامه نوسازی ناوگان ناوشکن‌های موشک‌انداز آمریکا محسوب می‌شود.
◀️
نام‌گذاری به افتخار «ویلیام چارت» از نیروهای نیروی دریایی آمریکا که نشان افتخار Medal of Honor دریافت کرده بود.
🔼
ارتقای سامانه‌های رزمی
نسخه Flight III نسبت به نمونه‌های قبلی Arleigh Burke دارای بهبودهایی در بخش سامانه‌های دفاع هوایی و موشکی است.
مهم‌ترین بخش این ارتقا، استفاده از:
◀️
رادار AN/SPY-6(V)1
این رادار آرایه فازی فعال (AESA) بخش اصلی ارتقای ناوشکن‌های Arleigh Burke Flight III است. این سامانه برای کشف، رهگیری و مقابله با تهدیدات هوایی و موشکی طراحی شده و نسبت به رادارهای نسل قبلی توانایی بالاتری در شناسایی اهداف دارد.
◀️
سامانه رزمی Aegis
سامانه Aegis یک سامانه یکپارچه فرماندهی، کنترل و مدیریت تسلیحات است که داده‌های حسگرها را دریافت کرده و امکان کشف، رهگیری و درگیری با تهدیدات مختلف را فراهم می‌کند. این سامانه هسته اصلی توان رزمی ناوشکن‌های Arleigh Burke محسوب می‌شود و در نسخه Flight III با رادار AN/SPY-6(V)1 یکپارچه شده است.
❓
نقش عملیاتی
ناوشکن‌های Flight III برای مأموریت‌هایی مانند:
⬇️
دفاع هوایی ناوگان
⬇️
مقابله با تهدیدات موشکی
⬇️
اسکورت گروه‌های رزمی دریایی
⬇️
عملیات چندمنظوره سطحی به کار گرفته خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69620" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69619">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b6e5f9de.mp4?token=sORjR2Nw7fwPHbrTkLQg_5F1bhWw8Eh36sapS0LWXJg8e0s4SuhM8xo_IqoKccF10RIjwLHspupCb78od7XK293pGImd9t-ncBZWXjQiEXTa4K7ZnT6ID26_EtioaoIrZoAhTyGOjrGGoutNd5KS2FEb6MY993MOH3wloDI3ID30yob0clhe5619l1FsuB2oVTzuhNNA-dPJv0tGnsKcH0tL2azijl8d-2myk7yfGaxHQ8JZSWU_MjUgOffyLmDfvGVW_hJ4jQNXwbEHbTiYhWqVZEPwvKM1iAvVzT8GyujqjMtxGPOMSzTpQ2lZY6NZAgVuyzAHgYysPEJeNl2GBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b6e5f9de.mp4?token=sORjR2Nw7fwPHbrTkLQg_5F1bhWw8Eh36sapS0LWXJg8e0s4SuhM8xo_IqoKccF10RIjwLHspupCb78od7XK293pGImd9t-ncBZWXjQiEXTa4K7ZnT6ID26_EtioaoIrZoAhTyGOjrGGoutNd5KS2FEb6MY993MOH3wloDI3ID30yob0clhe5619l1FsuB2oVTzuhNNA-dPJv0tGnsKcH0tL2azijl8d-2myk7yfGaxHQ8JZSWU_MjUgOffyLmDfvGVW_hJ4jQNXwbEHbTiYhWqVZEPwvKM1iAvVzT8GyujqjMtxGPOMSzTpQ2lZY6NZAgVuyzAHgYysPEJeNl2GBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
مراد ویسی تحلیلگر ارشد اینترنشنال:
قاجاریه در عهدنامه‌های ننگین گلستان، ترکمانچای و آخال، سرزمین‌های ایرانی در شرق و غرب دریای خزر رو به روسیه واگذار کرد.
حالا جمهوری اسلامی، از سهم ایران در دریای خزر به دلیل نوچگی روسیه می‌گذره.
مردم ایران، این روزها رو برای تاریخ به خاطر بسپارید؛ جمهوری اسلامی در حال رقم زدن خیانتی بزرگ به ایرانه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69619" target="_blank">📅 14:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69618">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de4ded641.mp4?token=o14m7DBeo2UMUAoj3pLDrHLa4_7pLLm21eod7oT1mBYeqf-eiFSYEFo5t3SvMso0pQXMWs7PfRp-rg-4oLIAoBmUO55gQAE1ZcoL-KWCpqQYpD6sxFlg7iQ7EKRy4H_KIrGj906VTc_3yx73IYVtz6T9Pqe4j-3y-WSr69_FRHUQ4ZtO4oJoFTnm0k0n4VoMgOGARCd4RcebSwN8IfhdaqGTfJBvMtVhxqucBiVq-yeKDAVMFNVd4ZRupBNxBlAcTQmeMz9SvwWMB26alEpgPwyskCtI8J-NrYFnj04oKUzQb3qBJXPH8-6EhY3tXj7d74Rg9FrHwbQjywLfp6REKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de4ded641.mp4?token=o14m7DBeo2UMUAoj3pLDrHLa4_7pLLm21eod7oT1mBYeqf-eiFSYEFo5t3SvMso0pQXMWs7PfRp-rg-4oLIAoBmUO55gQAE1ZcoL-KWCpqQYpD6sxFlg7iQ7EKRy4H_KIrGj906VTc_3yx73IYVtz6T9Pqe4j-3y-WSr69_FRHUQ4ZtO4oJoFTnm0k0n4VoMgOGARCd4RcebSwN8IfhdaqGTfJBvMtVhxqucBiVq-yeKDAVMFNVd4ZRupBNxBlAcTQmeMz9SvwWMB26alEpgPwyskCtI8J-NrYFnj04oKUzQb3qBJXPH8-6EhY3tXj7d74Rg9FrHwbQjywLfp6REKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از صحبت های یک دختر درباره مادرش:
❓
کی گفته هر مادری قابل احترامه؟
از میزان اشغال بودن مامانم اینو بگم که تو سن 13 سالگی پریود شدم و وقتی بهش گفتم منو تو خونه 3 روز زندونی کرد و گوشیم گرفت و کلی کتکم زد
بهم گفت تو چه گوهی خوردی تو هنوز بچه ای چرا باید پریود بشی؟ و این خون یه چیز دیگس!
از 12 سالگی هم منو میفرستاد سرکار میگفت باید خرج مدرسه و خونه رو کمک کنی بدی!
همینطور که اینارو میگفت تا اول دبیرستان بیشتر نذاشت درس بخونم و 15 سالگی ترک تحصیل کردم
مامانم گفت لازم نیست درس بخونی باید بیشتر کار کنی چون خرج ها رفته بالا اجاره خونه بیشتر شده باید بری کار کنی
به محض اینکه هم 18 سالم شد از خونه زدم بیرون و الان 6 ساله نه میدونم کجاست نه شمارش چیه نه باهاش حرف زدم
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69618" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69617">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79de90eb9.mp4?token=eyTWZ6RjCmWFOpmjvDG8WF0H_nmh3HxModtEFufa_uHkSOkUWgwGpaca05dhJFBwVChKXXF9jFwDwjdbONmRXIuhzGwBVR1kLER3mV__8JlDtEzlr6ihUHxh0EiTvGE6ZJGs3SAb1NMioUD_NHJU2SsxO_voXlCLzrdhNXWvV_8gJ7MzAPyWQYvGafeSWq7L5VxyvRxS59FwtlE5fTh3dtnJzTgZVB-CnanM0KcJAyCIK0KLppYB0gE-b9GWBCrRk7FKkS8M3q8z_8sJC76-FnFJjLFI15yHIMZULM2RCuokOGaaMR7ZIHIb4Dy4cDHyMCs7Wtp-9van65ipuBWkOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79de90eb9.mp4?token=eyTWZ6RjCmWFOpmjvDG8WF0H_nmh3HxModtEFufa_uHkSOkUWgwGpaca05dhJFBwVChKXXF9jFwDwjdbONmRXIuhzGwBVR1kLER3mV__8JlDtEzlr6ihUHxh0EiTvGE6ZJGs3SAb1NMioUD_NHJU2SsxO_voXlCLzrdhNXWvV_8gJ7MzAPyWQYvGafeSWq7L5VxyvRxS59FwtlE5fTh3dtnJzTgZVB-CnanM0KcJAyCIK0KLppYB0gE-b9GWBCrRk7FKkS8M3q8z_8sJC76-FnFJjLFI15yHIMZULM2RCuokOGaaMR7ZIHIb4Dy4cDHyMCs7Wtp-9van65ipuBWkOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی که یه خانم حامله ایرانی از میزان تکون خوردن بچه‌اش توی شکمش منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69617" target="_blank">📅 12:51 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
