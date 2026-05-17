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
<img src="https://cdn1.telesco.pe/file/jXiKmFb2doTHQXSd_QZ-CrBB9EyEgXlhQRtToEmJFj8iO126Gl74Dyw2A5JDava0ZPbG1gDttWsDPOU6PtH1pzR6Fi1q9Z-z2WXxmHaB274FvfeZuj3z49zcGUpmpB7XvG8k5BMLfIzSSLIDa2lQJaQdCnGgvrKOJP7tu0EfuzvyvF0LozKtUsAWVl1bhtRPr8l_EVP3Lc6ppy8c8Zxwm0vWk_J1pJV12iDQRf9zNRuFJbYrig-x8lwGPCsBbWV6e5lF4vaXxyUbJC1vYMBjpZAVN3xHPEGlppG4E6_zNyRdbYn1iJgbEvchSjGQb7K82aB2U1h5Sr3J6zgkK4PgjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 20:17:40</div>
<hr>

<div class="tg-post" id="msg-75516">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/khg7pfEaW-RFmpELYKeepRIvbtM0UnqB5uyFmLGxoOurmunHtTIqJsuRYCcvbJTG46WjAJdg3hais6YuiH_VJXKX2Rs4VrbsyV9aM8MTJcOTaskBwtcoq3ZAkwCK4fUy25iEkz5UTxVBZd5N1XcsuXLyBLN9uI5FQJE2kvZGugBz8l28pF1-TwBz7GkJ9BSirAVrakFEVg5Pz3ShRO-L2KEKveoW9kGlGhrQY1amhIodvDb43a3srDAFhfDOVWOCLW5SaJ18u45ese9C1FsU9WoU1_zuALxptuzFhVsYO1a3hDCx9KKqHTCBkUhc_25pr_MH__yOy0-FYhnAICMuiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FMFFZD27Q-7L0w8egtbhTXwv76DUHymnLUaNFQrQrPxDWdYLvdkB45qDxGGOFdMAQ8SUa-RfVHQAzyWQcHbQCs5H8ux7FsyNeNGwxNd-rLG20QUDX7pWWMLyU78UncG6NTAmNs2S7ULr2TrZrNYrQEDz6TnIGx6upJk31ISOpWJNAAHBolu-ox3exeS-3ieO-jr0jaj4JcDFaYRKcHtuQ17FRv_xaJCYoGDr5Xv3BO3CwK2GbFi_y26LwG22FXWjLZoSEIIxtBaKPSjFulgnaWwSeIwJk8hzeLJshmyWB-DwPAdA185XPAfkKFo7p5GJwWlvoKu2_gQ7lMAprgHBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OaqTOrdp4Lzjs3evotRloAuf-nsqzt7ZDyvebPEa2rb-7wvnCbVWyvXJOWH2qF47CzpLW1TMSxa6hKKEt2jRO0SlyShQUh1UREJpJ7cRNc7GmkKCEI1XzwirR-QHGSwpZyOx0Jql5TVu8XdNn2TaOHF123PHSSlovVpMpXgeDaG1x7DYahBhM8Cir_PU4R7uUfFBNiNMfMvxdXTboZ2kg4K4iMRBGf_ICz228p_RtnF9okb3g_a369WmySOFNRsepWtrP9yQ3sEfCKVO6OeYIBvLghiwCqTYTJACS3SEtPLUyGfxXhZFdB5_dKWW2NIT2lOCJFgpYTlPWVF4C9sByQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N7emVCcr1jRQaxwmw5St7QQCAzPVk4WEGZKciT5-sNrom-vFmtprf4o85Ux4bO_TvYYmZXzQvyoCcd5-OaOskfzyCWgZvpz4-XNWYUQelSCBKrwcP7O1JUgKrW9uQo1RD2LdbFkaRthjwdX9qWU7x4BnRgzSembIQSxSa3nV0EkUftGI3fNQUbQJoUTmYIzTp_Ns_qw4a0mfp6JXq-LMwXN5k2mdqyov6NjRYGSAYV_-ky1ht98rtdGHuuKoNp75AAPeXk8o7kMrz6Ta4v9Vlectxaghg9RSgTBSHdtiqZ-QqYDgrsPKw1lRU5uzyFVLEc3YwTe6b1uckM53SYyx2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">drpezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/VahidOnline/75516" target="_blank">📅 18:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75514">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dvRzYGBHCpi-GIVfM0DBrZokQ1q6vVLF1ItciF2vQ7mt6bysyuq52V85sOY4zTuW_S_6Y37pSMDjVxgoIha843zh1Nl7AMgjbzW4w7yiQLbsauoPOGGXhpFTnQp_livqMDeq6XRiqzbE4wbsQoS3dEVYoiAy3umZ262iYNDfhH6j4U6m1Ifv09kDmmV_VCP2F1wAZ4ZERPgETjIzsZ7Amp3pdH1mFQ4sxztD-Me_LzKIO8PAFzcR1nbuhp2rDdXbvqwLs14dMvlux8w5awP-7vp5b8haBZ3kKMqFAm10636VevjuaB75xvLqxSFNFAixp-t848wfP5lOXXTX5cbkEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K6_WDXf27utP8c6Se9vA-l32EeABBo2Cn2EOEb1bYBplY6leMCO-KEzgwY4CvxJT4cBPChA0JNCbttAWGRGmAujmSSzWRsSvFQ2EBkbDmJAHjAy6Fvp7lLHKXPgtjskm1a2X3zESZnipgFRVZXELpgCdnRWv5eflbSFWJ9G951VxSULmFn7_2txpxEaUeUNfxNB4KX3VdI6fVj7taqiZlGkt3Ex7NfRdiVAdl3EQ9cpAZHSc8ktmMMHJojywoykHqtZFS7KxQc9juFP_zlIEf1j4iZG6KeBTnIfxpAy9MBxr2SCm7ww7SV40kKap0jFJhuQTSULHsNUjc2xHCkj_oA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن نقوی، وزیر کشور پاکستان، عصر امروز با محمدباقر قالیباف، رئیس مجلس ایران در تهران دیدار و گفت‌وگو کرد.
رسانه‌های ایرانی و پاکستانی گزارش داده‌‌اند که آقای نقوی برای از سرگیری مذاکرات به ایران سفر کرده است.
گفته شده او حامل پیام‌ آمریکاست و پاسخ ایران را هم دریافت خواهد کرد.
به گفته سفارت پاکستان در تهران، آقای نقوی دیروز پس از ورود به تهران «نزدیک به سه ساعت در نهاد ریاست جمهوری حضور داشت» و اسکندر مومنی، وزیر کشور، و عباس عراقچی، وزیر امور خارجه نیز «در جریان این دیدار در نهاد ریاست جمهوری حضور داشتند.»
علاوه بر این، محسن نقوی «دیداری خصوصی» با مسعود پزشکیان داشت که «حدود ۹۰ دقیقه به طول انجامید و با حضور وزیر کشور ایران همراه بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/VahidOnline/75514" target="_blank">📅 17:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75513">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZUAXwSH-9IIoQgpch2bE0P6HxmuxBRJWfOpgNkj-IM6DXETiuPtCz7JehQMUQ-pHsGRVVuCQWx-qEyR0Cd2GEoSwIlLqD3w8mZsPSDLaK_NqpPVCjd3OJq2nRy8RVjxdRIONERnDHHJOUQbye0JFBUDKqDx74IuW-hzIKl-5QhGvkCSP6qLAYq8-eUP-UgBYZXH3z-GCXmwRNaJwEWR8O58PI9PPMKvU0wi3_5TJwiax8Dm4O-ZML5mHz2eXWcFKRrjfa5vXyKUO4ioXY3gH1L5EXzsK07cx9XuoKMyrAbFzPKDeGMrUdzlrApY1ZZU1JcKweL5smRHwEyskroymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس با انتشار متنی مدعی شد جزئیاتی از پاسخ آمریکا به پیشنهادهای ایران در جریان مذاکرات به دست آورده است؛ گزارشی که در آن از پنج شرط اصلی واشنگتن برای توافق با تهران سخن گفته شده است.
براساس شنیده‌های فارس، شروط اعلام‌شده از سوی آمریکا شامل موارد زیر است:
۱- عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
۲- خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا
۳- فعال ماندن تنها یک مجموعه از تاسیسات هسته‌ای ایران
۴- عدم پرداخت حتی ۲۵ درصد از دارایی‌های بلوکه‌شده ایران
۵- منوط‌شدن توقف جنگ در همه ساحتها به انجام مذاکره
به گفته فارس، در مقابل، ایران انجام هرگونه مذاکره را منوط به تحقق پنج پیش‌شرط اعتمادساز دانسته است: «پایان جنگ در همه جبهه‌ها به‌ویژه لبنان»، «رفع تحریم‌های ضدایرانی»، «آزادسازی پول‌های بلوکه‌شده ایران»، «جبران خسارات ناشی از جنگ» و «پذیرش حق حاکمیت ایران بر تنگه هرمز».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/VahidOnline/75513" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75512">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mv3aj6Kx5KeplKB5UmdGchuaJezI2odBxObQGygyLIPJCTAUtzQpJLMjFbItlXy0Xt0bHN5K_bV5PyVu1erUetGFGDwBMIES6_rMbt9eivZizJ55epbRGWRPYuDR62dqMh5f9KKF45ufKa4y27GBMWtvVWIcFz6tc2Vf3IczQQxtsfIr_6hQnkr1RJM7xV3KvU9cVRxmtlkcRBD2VBwtRNNTTaP5Mo35NepXrUHFIq7Ropk1chMYs87JPJv0yy-LjykRiJb8HgDSoN6LCbJ_WfW-bi1qIKfk33XZZa5nCFar4t-VU7L7N27TGHh0-qIhSdh-LR_gPhRS1vh4vWoTtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، در کانال تلگرامی خود اعلام کرد که کتاب «قدرت مذاکره» او به چاپ پنجم رسیده و در چاپ جدید این کتاب، بخش جدیدی با عنوان «دیپلماسی زیر آتش» درباره روند «مذاکرات غیرمستقیم با آمریکا در جنگ ۱۲ روزه» به آن افزوده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/VahidOnline/75512" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75511">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPDR4UY_D5GBm9oO0tnLL9ADBJVMG5JO2tRJtRdVzVgDcBFtvW5Rgdncqv5GINRGGcyyJeO696VQtITLz39j-m-vOaV2FVRZ6x-adKQ26uBSV0kZKDJS5UAEEQ3fp86CvVfra3r4kKX6ynNawj-tVgcrHuBhb7ur9pgMHzzVqXUEDVbv6nOw3OQ_mMI0LqmQKaxnhRTzPfn6q-nF2RbiuqqaE3CA1ZZ9sAfRDRV5JFFRFj6CIsg-rFBXl6aCKVXz-xGgXolSPKUrrMMhCVvYQerqaxTnfXyGbfc9131POUR9FVUm7H8VC9oF7s-Do_uT-iKP-yQNDBp_bpHBIzacCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره رسانه‌ای ابوظبی روز یک‌شنبه ۲۷ اردیبهشت در شبکه‌های اجتماعی از وقوع آتش‌سوزی در نیروگاه اتمی براکه در امارات متحده عربی خبر داد.
این آتش‌سوزی پس از حمله پهپادی به نیروگاه اتمی برکه در منطقه الظَفرَه آغاز شده، اما کشته و مجروح بر جا نگذاشته است.
بر اساس توضیح اداره رسانه‌ای ابوظبی، این حریق در ژنراتور برق خارج از محدوده پیرامون نیروگاه به راه افتاده و بر ایمنی سایت اثر منفی نداشته است.
در پی آغاز حمله مشترک آمریکا و اسرائیل به خاک ایران، امارات متحده عربی به بزرگ‌ترین هدف حملات تلافی‌جویانه سپاه پاسداران تبدیل شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/VahidOnline/75511" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75510">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3yqFzbm77ekMQe2hDokVvGYlwPfZpsEgfI1hy9SqjoSWTO8EYVgEL51P32HkIPOWnu-d1ks9tR_BGrIluGGiPNjuUZdsdSPVLD15qNrXlONr3EFT2pzmCU4tmW4VOKrqkDw_AbctHne4Jb9Et0bu649DhCEyjGJg4LtzcPLXzdwkCdmXGniU8wwYf3ZBiLCiS0k_qZd-wPCNmJHy7zdRM6HCvEAr0lGlPLtTwb5CmoLaOMY8kPYRfgpRTdWHJYG4snltilZA8YIfD5KgHSqa8bqgdDihILUXOoGbME2X5r3GaZ1YOcZZDh1h-rVR-0WgPtTpKkqzScFaB75vzZXCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، نزدیک به سپاه پاسداران، روز یک‌شنبه ۲۷ اردیبهشت نوشت که محمدباقر قالیباف، رئیس مجلس شورای اسلامی و عضو سابق سپاه، به عنوان نماینده ویژه ایران در امور چین تعیین شده است.
این خبرگزاری امنیتی بدون هیچ توضیح دیگری تنها نوشته است:‌ «پیشتر علی لاریجانی و عبدالرضا رحمانی‌ فضلی چنین مسئولیتی را برعهده داشتند.»
🔸
در این خبر نه توضیح داده شده که چه کسی یا چه نهادی قالیباف را به این سمت منصوب کرده است و نه برهه کنونی چه اهمیتی دارد که حکومت تصور کرده است به این نماینده ویژه نیاز دارد.
اعلام تعیین قالیباف به عنوان نماینده ویژه در امور چین دو روز پس از دیدار رسمی رئیس جمهور آمریکا از کشور چین رخ می‌دهد که در آن یکی از موضوعات گفت‌وگو ایران و تنگه هرمز بود.
کاخ سفید روز پنجشنبه ۲۴ اردیبهشت اعلام کرد دونالد ترامپ، رئیس‌جمهور آمریکا، و شی جین‌پینگ، رئیس‌جمهور چین، در دیدار خود درباره گسترش همکاری‌های اقتصادی، باز ماندن تنگه هرمز و جلوگیری از دستیابی ایران به سلاح هسته‌ای گفت‌وگو و توافق کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/VahidOnline/75510" target="_blank">📅 17:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75509">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZSdILLGoIRnBJKi_L0H-ZUoqhDRSKa1s_jY-V9nEpx5KowmE7TsAGCGn8BHKCXPfN1HWDb0lwTbyR56B9wB7RpTrsol6H6z5p1fd720mlCMz3eNhIKR_gQOsw2vmJgz0EvavkXV2kyAZr4041sc9tnKz9Sk5J-yAm4_SHS5MlObK9rknGgHx5eG86rkC1Rle67t_Uo0-d0g0WSJiVEWTxhnGpGQfrY26wQGMFWWy4W2DS-99XcvWdhbY7J15JjYWiUty5GAmoNcNh5zs5H-fhTN11L0QGEJO_i-AlcaxYFstqZUbvyP5u0S1CG_H8Cjuxreh_CdBydjPO2cU_be9Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه دادگاه صادق ساعدی‌نیا، مدیر کافه‌های زنجیره‌ای ساعدی‌نیا که در اعتراضات سراسری دی ماه گذشته به همراه پدرش، محمدعلی ساعدی‌نیا، بازداشت شده بود در دادگاه انقلاب قم برگزار شد.
کافه‌های ساعدی‌نیا از جمله کسب‌وکارهایی بود که در اعتراضات دی ماه پارسال که با اعتراض بازار به نابسامانی اقتصادی آغاز شد، مغازه‌هایشان را تعطیل کردند.
نماینده دادستان قم در این جلسه آقای ساعدی‌نیا را به «فعالیت تبلیغی یا رسانه‌ای برخلاف امنیت کشور»، «اقدام عملیاتی برای گروه‌های معاند نظام از طریق انتشار استوری و فعالیت مجازی و حضور در تجمعات غیرقانونی و تعطیل کردن کافه‌ها و مغازه‌های خود در کل کشور و تشویق تعدادی از کارکنانش در ارتکاب جرایم علیه امنیت کشور» متهم کرد.
به گفته نماینده دادستان و قاضی، موارد اتهامی بر مبنای اطلاعاتی است که از محتوای لوازم الکترونیکی ضبط شده از آقای ساعدی‌نیا و از جمله تصاویر و چت‌های او در واتساپ استخراج شده است.
نماینده دادستان گفت که آقای ساعدی‌نیا در واتساپ خود «برنامه‌ریزی برای تعطیلی کافه‌ها را همزمان با صدور فراخوان دشمن به مشورت گذاشته بود.»
قاضی به او گفت: «شما با فراخوانی که داده‌اید با اقداماتی که انجام داده‌اید، این تعداد جوان را به این مهلکه وارد کرده‌اید و نظام متحمل صدمات زیادی شده است. چطور می‌توانید جبران کنید؟»
@
VahidHeadline
نماینده دادستان، مواردی از جمله فعالیت‌های ساعدی‌نیا در فضای مجازی، تهیه کلیپی از یکی از کارکنانش با نوشته «جاوید شاه» روی دست، ایجاد و مدیریت گروه واتساپی کارکنان کافه‌ها، انتشار پیام صوتی درباره خاموش کردن گوشی برای جلوگیری از ردیابی، حضور برخی کارکنان در اعتراضات و برنامه‌ریزی برای تعطیلی کافه‌ها و کارخانه‌ها همزمان با فراخوان‌های اعتراضی را از مصادیق اتهامات مطرح‌شده علیه او عنوان کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/VahidOnline/75509" target="_blank">📅 17:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75507">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ks47G7a5a-HH12ME9vgMHPeyW7yBa4nTJL4V-S6nnUS9KI6S3vaoyxGsfq45wlICPamitAsZudVXbJo-88_N83T0TQgTMxVACfOTN83M4FK4R5VV0ttB4NVF33OcFbY1qyO4uTOofpqxaaktMqUqavZQ4OaJSLTaEg20SxbaEBHT6EN-O03lBPCSN1fpTt9rXOh0eVp9F9GRHnE3sY0M-kn9Tu625ycE5zgnwJhxmUfHlkMM2OPPTDgoYzi0nErQFVRhvWDt-ciIJt4KFBTgIpqMG8Ec4gGk9tfDWWR-xMHX-4VUgBYJ39Xx7L_PRUerNOJl-GpbxQ925Hki3eVFbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز شنبه تصویری گرافیکی از خود در کنار یک فرمانده نظامی بر عرشه یک ناو جنگی، در فضایی طوفانی و در میان شناورهایی با پرچم جمهوری اسلامی، در شبکه اجتماعی تروث‌سوشال
منتشر کرد
که روی آن نوشته است: «این آرامش پیش از طوفان بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75507" target="_blank">📅 23:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75506">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2db463b161.mp4?token=n1or4xyUSWmpFJuYpDnm9DxtheGiPbDrz8vAXgTJBn2Npd99DmUN-tZ_jl_T7K4qCwOfVOk1sOpxDwuX_qTZDmagIcMU_etjLiJ2xUk_xS6zdVNmzry9CNDILbxda92UG_DG0tD4dGRGHOHr3RI3w6cp6aKqXt-TW8v7d0mJgMWyBBFPD26ZjVcEgZVNSB4VTAITx_c-T1bb0MEmIF8jg2cdHcuG4XlfplnuMR9HrK_AsjK6UQRcsz3A-eV19yBBrN-QpynX23dlJuOoIE7YhA5X4NuPKzKxxa7Bys4EDkMVKOkZyVwMQ-RCZqUHO9URRzhg0wunT_uZ03M-W7G78g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2db463b161.mp4?token=n1or4xyUSWmpFJuYpDnm9DxtheGiPbDrz8vAXgTJBn2Npd99DmUN-tZ_jl_T7K4qCwOfVOk1sOpxDwuX_qTZDmagIcMU_etjLiJ2xUk_xS6zdVNmzry9CNDILbxda92UG_DG0tD4dGRGHOHr3RI3w6cp6aKqXt-TW8v7d0mJgMWyBBFPD26ZjVcEgZVNSB4VTAITx_c-T1bb0MEmIF8jg2cdHcuG4XlfplnuMR9HrK_AsjK6UQRcsz3A-eV19yBBrN-QpynX23dlJuOoIE7YhA5X4NuPKzKxxa7Bys4EDkMVKOkZyVwMQ-RCZqUHO9URRzhg0wunT_uZ03M-W7G78g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، انیمیشنی در تروث سوشال
منتشر کرد
که در آن به ناو آمریکایی دستور شلیک به هدفی با پرچم جمهوری اسلامی را داده و می‌گوید: «در فهرست اهداف‌مان قرار دارد، آتش!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/75506" target="_blank">📅 21:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75501">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aCqWK-cadKW2igF4rg_Vp76SS8O3UuQYx10WtxOZUqBYDQ-tfSrtnraPNEa3LU4CopcwnI652pQ9Wq6uE9Frk_0efd1-x0FDcx0KqifuCLz5dPl56We7TJsZSSeFmrjju6oBW7A3vrAhWyEVVtw6yCFmRqcc3zvS1tZUY7XRf3ACJ3OXEKdvZ0JoTf6SLnP54_4oQVsBSqG591iKE2GiJLzhxS8eXJ9oqPDTh0cbL77JFuEBf7PHtv-gExuKtgSjdrn1F3D3d3ZEiEhdSqBCNqANWy397SFv4-gy-kzrmexA1fdL0CWjqeoPLNxnJCcxMOmKgtNR08Q-cuDmPk3SJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sHlVrIuw2CHE3J2GSlLtxQ0pq4xA5eooeze9ButkShV053t9YNvgnND2c1m_DT5_SUFFlka7ArhOmIwEH_tRopH_boCb4scMEgusK60cs84pAlrPh0f07Mwmv1mC9rcq0HCj0rbQ8gYjAu_VYGVCULW-cIy0BduIkHFPFWS-9wYBsOVE7b2_1QZqgbic-EbH-JY2dmLsHbFWiSVtIZyp1x04gLOUjZd8QZeCycqiLrxwbCH8Jrp3Vn-ARmGWPsxSCW0S-WMYWI31XCCpNSQeOiNNgY8T6jtQgHPS7ZT7P3-O1bk4dMCPwl147V3EacM1Rn66bMMAN0uWnFBgGuvzVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dCavKFRMsqU2AAVjJkQngMXmM-jSD3WhFP11azmDzQE2A2kcTYlKdZrJm28Ysht3Z16Slj497PGvoBgUwkwBuLivt-6JJDg8lDlBgsyabwaH-Enl5IHKDznpsurAzXP8gYii9EeZ1MCp6Gr8v3g41-cmd2l8pfNXG6Wunahjx1st35R36HUdswxpKl0bxnhAyodh0pQI9fV5UESL0J3XCR371jD79LVjg39vekS0fyVqbcUzo1SScIWMgmqAvhJEL54d0IGEh7-25SWomA5S_08aOUfdxikPDPTZ8dWxUNbPWQRoQCQlfoIJrZdPg87U_M6dLodCmiom1EpNbBubjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qF2-5EnNvNkBUm3Pssc16ZrO_6klM4w28dNEwNVaJUYQqexMGgB7PssOVsLMK9GdQuY2NWUSOwrch3YCA1_62SwaddkZcfkElll12arYFyq0BIuzi2snbEI7Ci9MVM1j8vG9UTPoA-3qve8Ctecx81DVj6TGl8GsuVgzndxjeLic6UJpobfEjWCbjZq0QAXwxQBNxBD05Dv60x7vKOfNw91uWxiYVgiFVsHl7eHFWbiAiQWB74MNnWUg14MpUtNRIX_SElS5mH-G_LBwRT-ytg0V4VvYgl35XfRHjePsuAFtVZwVSMnXrw-llRKuU8HaoQ41wVZtddGnkpIsqNJgFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fcb834d170.mp4?token=BsnNmziVLtTu3mnnpGL4h3WgqUetGallKcP2uABDMfbOjjspAhK1BemPW_QYrkzsG0usX1--PH4hM6zAYnRxG6v1G9VK2-aTbUOVgKZdDlLcvGOdZwpNrdeklplGeyIbjpfZT1UEC5WmC3rntFaPFmgZKHo-5guTs4GB-8qW9E07fUDynixg3DSDNUuf7HoX817ZXH69T43b8Ai0UheMratvudC6HZzR6R1oXGp2ZbRliBS2XFI-VzlW9rtxrOb4n9AkGuPPy0a0bxE6anMwhxZ7qpJgKZRLEiFgahHJerc9B5hJsJBrn7lfMB8XY30Cd7ziucl38hM9zPWF_ky8Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fcb834d170.mp4?token=BsnNmziVLtTu3mnnpGL4h3WgqUetGallKcP2uABDMfbOjjspAhK1BemPW_QYrkzsG0usX1--PH4hM6zAYnRxG6v1G9VK2-aTbUOVgKZdDlLcvGOdZwpNrdeklplGeyIbjpfZT1UEC5WmC3rntFaPFmgZKHo-5guTs4GB-8qW9E07fUDynixg3DSDNUuf7HoX817ZXH69T43b8Ai0UheMratvudC6HZzR6R1oXGp2ZbRliBS2XFI-VzlW9rtxrOb4n9AkGuPPy0a0bxE6anMwhxZ7qpJgKZRLEiFgahHJerc9B5hJsJBrn7lfMB8XY30Cd7ziucl38hM9zPWF_ky8Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر جمیله شفیعی:
JamilehShafiei
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/75501" target="_blank">📅 17:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75500">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffe0351e23.mp4?token=kEiMjdawLQM1g-uFe7mwKHmbF2mJPFJv_BVVeqqUmB3sOl_7sGJnvvqUBSkPQz6wfKS9YNVzxzelAwfhEHltLekt4Jw6co3NnvzipCDDXBmhD5ytfYrb4TEjEL-7VaXNaNn2COYu8xb1T4ImQ6jzRVWduFRtJgsQH4ZvCrcG2aQAKIQ1b6b6eDpdXbJg4APCT_Rc8frBOT8e4Es68jCTjq246ms9IQ70LF1SgI7SgZmny9tIlJjG4VasLkttasAJbhCFvwlKSqMyCbasV-zECkZ5KHLBO6UAa1_QdkmIUtOtzzZr-21cs_R1A2xGFz4QqXqZwhmWkrrv2mc2Wlz_Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffe0351e23.mp4?token=kEiMjdawLQM1g-uFe7mwKHmbF2mJPFJv_BVVeqqUmB3sOl_7sGJnvvqUBSkPQz6wfKS9YNVzxzelAwfhEHltLekt4Jw6co3NnvzipCDDXBmhD5ytfYrb4TEjEL-7VaXNaNn2COYu8xb1T4ImQ6jzRVWduFRtJgsQH4ZvCrcG2aQAKIQ1b6b6eDpdXbJg4APCT_Rc8frBOT8e4Es68jCTjq246ms9IQ70LF1SgI7SgZmny9tIlJjG4VasLkttasAJbhCFvwlKSqMyCbasV-zECkZ5KHLBO6UAa1_QdkmIUtOtzzZr-21cs_R1A2xGFz4QqXqZwhmWkrrv2mc2Wlz_Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"مجری شبکه سه تلویزیون: یک راکت ۲۰۰ دلاری می‌تواند کل ارتش آمریکا را در منطقه به زانو درآورد"  ویدیو با تیتر بالا در منابع جمهوری اسلامی منتشر شده و خانعلی‌زاده متوهم رو نشون میده که مطابق معمول چرندیاتی در سطح خودش میگه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/75500" target="_blank">📅 17:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75499">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46bd8e2257.mp4?token=BY3pyp4z1G_VBaRwF30l-NNvxCfWCpXPob5oCaVDtfTqDwsobdhCABU2p0dad5Z8rTuq9y7hZDG2MDH6hyjtGiUuRw39FQxL7PeZzO-Mk1i-VL9gzwQupfm7GeO5dOkfxHXb1oLCBRhv515EA-I7pQlbXEeei10NAOjAhkzO6P6FmwvivTZXo9IV3Cqb5C2-j-SzhJeUPQ3kmkKsXEtCrvoaCchpWWhkQl52Daunyj4MyR-qFWJ1cN47mFDkdWJcch1Xq8vNpw9aBU3LpVCuy8-kUG1DYkQR6Gkt3PK-Oq-wgAPS_FpTSLHh6fXwiJD0uRv5OAfYoudDADmY60VVOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46bd8e2257.mp4?token=BY3pyp4z1G_VBaRwF30l-NNvxCfWCpXPob5oCaVDtfTqDwsobdhCABU2p0dad5Z8rTuq9y7hZDG2MDH6hyjtGiUuRw39FQxL7PeZzO-Mk1i-VL9gzwQupfm7GeO5dOkfxHXb1oLCBRhv515EA-I7pQlbXEeei10NAOjAhkzO6P6FmwvivTZXo9IV3Cqb5C2-j-SzhJeUPQ3kmkKsXEtCrvoaCchpWWhkQl52Daunyj4MyR-qFWJ1cN47mFDkdWJcch1Xq8vNpw9aBU3LpVCuy8-kUG1DYkQR6Gkt3PK-Oq-wgAPS_FpTSLHh6fXwiJD0uRv5OAfYoudDADmY60VVOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در یک برنامه زنده تلویزیونی که از شبکه افق صداوسیما پخش شده است، مجری برنامه با اسلحه واقعی به پرچم امارات متحده عربی شلیک می‌کند.
در این برنامه که موضوع آن درباره آموزش شلیک با اسلحه کلاشنیکف است، فردی که لباس نظامی به تن دارد و صورت خود را با ماسک پوشانده است مراحل آماده‌سازی اسلحه و شلیک گلوله را به مجری آموزش می‌دهد.
مجری برنامه هم در مرحله شلیک تصمیم می‌گیرد به پرچم امارات که در بنر مربوط به دکور استودیو، شلیک کند.
@
VahidHeadline
صدا و سیمای جمهوری اسلامی جمعه چند برنامه پخش کرد که در آنها مجریان در بخش‌های استودیویی با در دست داشتن تفنگ ظاهر شدند و کار با سلاح‌های سبک آموزش داده شد. مجریان در این برنامه‌ها اعلام کردند که در صورت لزوم به جنگ خواهند پیوست.
این برنامه‌ها که دست‌کم در سه بخش پخش شد، در رسانه‌های داخلی بازنشر و در شبکه‌های اجتماعی با واکنش‌هایی همراه شد. برخی کاربران شبکه‌های اجتماعی این بخش‌ها را نشانه‌ای از بسیج در شرایط جنگی توصیف کردند.
جکسون هینکل، مفسر سیاسی آمریکایی، در شبکه اجتماعی ایکس نوشت تلویزیون دولتی ایران نحوه استفاده و شلیک با کلاشینکف را به‌عنوان «آمادگی برای تهاجم زمینی آمریکا» نشان می‌دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75499" target="_blank">📅 17:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75498">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3SEaMk5QvtALKY7styW-lngOBBf-UHM8HPX38whil4Vv5CQa034JXCCy3MruqIijc3D0HqzEgDbKIBLhZ9SmAgnGnY9QytzxIfd9YDaxSkIISxbO6mJBJ2gJy4lTfS1h5H47KykjhbgNXlo5jtdFFz0w_zxcBJbxyaaFi-d1PmuTsl3ipkQpItqVcIg4EjZjZLQqGZaGiJzeF58yCVl6H_EE2ifGjbdMJUkcWX0Sxuf5aD1S1jw2b7khby6l7EenjP_FlGTbxkm7SMClBZRcTknMsuJp9McbXU7jbQATg0mjjkGmz657DkU_IVAkImSEC8nDKDLM2DFHPQwcI8FIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه وابسته به قوه قضائیه جمهوری اسلامی اعلام کرد اموال ۵۱ نفر در استان یزد، با دستور قضایی و به اتهام آنچه «خیانت به وطن» و «همکاری با دشمن» خوانده شده، توقیف شده است.
بر اساس این گزارش، پرونده این افراد در ارتباط با قانون موسوم به «تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی علیه امنیت و منافع ملی» در حال رسیدگی است و مقام‌های قضایی مدعی شده‌اند دارایی‌های توقیف‌شده قرار است برای «حفظ حقوق عامه» و بازسازی اماکن آسیب‌دیده از جنگ هزینه شود.
اموال توقیف‌شده شامل حساب‌های بانکی، دارایی‌های منقول و غیرمنقول، سهام شرکت‌ها و حتی اموال وکالتی عنوان شده است.
طبق گزارش میزان، از میان این ۵۱ نفر، ۲۰ نفر در داخل کشور حضور دارند و ۳۱ نفر دیگر در خارج از کشور به سر می‌برند.
این اقدام در ادامه موج تازه‌ای از مصادره و توقیف اموال شهروندان و مخالفان سیاسی صورت می‌گیرد؛ روندی که در عمل به ابزاری برای فشار، ارعاب و مصادره دارایی افراد تحت عنوان‌های سنگینی مانند «خیانت» و «همکاری با دشمن» تبدیل شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/75498" target="_blank">📅 17:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75494">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ta1OUmGdgBFoK6e_iMlJD85jafRE_bvnMGrUYTznISFbiQ5KH0gqRnRUqEDJo855uu-uk24scb5m-nQrR_r0cF1Bai9NvFgho4jZrp-qVmW1sFnEFg8-3mbSDXVt3UgJZu1GYZT_FoMpkIckdbuoJClMtxqphu_HA5DlPRWJXixuDHSP_hHKmYlAdUYiQZYU5qNcvxEheV0YdnBhqm-Cv0JghT5QRZE0REUES-D4d2h0ZKNIlx1862GN0F_fN1r65aCVFEKKc43T4i_PPtxJMvO3Vv7lmLs1Zm031GHREwes-e1H2MZmVDBtjh3nWh27yxuSQiE3ndEnfdb4pfHC5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sTYrm7OOBhXTxv3SD3NhJoCRINsgjlRA-ASV5lS3FY3at8gDqi_AbTP1a-wOTyUssk7OFNd4u7HyPYXv8ISXyn3GLLsaAMQ7h_eeFLlduVAS6lBKnSzCmmIqTKebuOhesjqoJHb9IYfx7HwtaNyWhJPpOVxVVo0eQuEeW9V_6COPiJh94n8hNdXqedcCkirxtGn2jKXG6RyAW_dp5zR8ygSxNDx8ERWvmGsKSITT_ivbHT4VHloTYQBDhptZQYHLp65JfRbJ_rvGvUbP2EDAu2CN3DdwMH4xx3ABDkdUPcIpK_xZiXjy_sPVAAN8R7CX2QAa8fkYywneMOEjD8_6Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CN_hKEzLmmiZ0rOwzzVaG5XblUDp0_zY2SCTtX7e2HxnQyd3oykl_L2njq9dP1SxHr4zlYQ5G2eRum7mGjnOyBdIxZtVgRvuvyQjjvKt7CpHKS-Scq0_j9wKsff0HlR6RhqkMct5tDrOHxApWU2mJCvZ3korUUDtYaWK9PDZD-hriRZnmEP4OfTy3b6gcM0X1qzvw34z49PpEit7GmXh9O-iGISdfRJjHqdDcuwgoC3mN9RY9rqFJrB_EEOhJoTPuYfpcEW2y3_HG-mal_KzBHEP-np0xLK5XziSJZQETrV9JRUZgSmK0z9pXriCFNKto0QDumcK7bRyYmWdSzg7yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d-6FH3hi6KZZacpqDCPlcVicM8AJFD4BsjCsTHQTHSWLtbUtKyiBY64xBFZXydRfxkP5hskXgMtZixfec11za5usZPft9DoYedIdD21gt3KRx0abxk41IjvimXBNxi8zBs1DbkZ6taGacBHAQbnED8TjqkI-FKxw_EkT_BQK5NSzdWtlm06TOOkKtnOtZS3MczhNNZ6UdEF2dXMpOa1Bl_U_ipK9fwCP9CapN9aKdzYzu5LDhsTxzgNVxndf5Tminw70EbT6qhe1qPuiu8DhGg54wzpu8XTyHRp5if2YJ1KYOuI1LK-Uf9IMQeBw3cFCjyYpB5CA4HDaGZ4cR_ye5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او تاکید کرد: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا در بخش دیگری از این مصاحبه گفت حکومت ایران از نظر نظامی به‌شدت آسیب دیده و بار دیگر تاکید کرد: «آن‌ها دیگر نیروی دریایی ندارند. نیروی هوایی ندارند. همه‌چیز نابود شده است. نیروی هوایی‌شان از بین رفته است.»
او تاکید کرد: «تنگه باز خواهد شد. آن‌ها سلاح هسته‌ای نخواهند داشت و دنیا ادامه خواهد یافت.»
رییس‌جمهوری آمریکا گفت به درخواست مقام‌هایی از پاکستان، مرحله نهایی عملیات علیه ایران را متوقف کرده است. او گفت: «آن‌ها گفتند: می‌توانید متوقف شوید؟ ما قرار است به توافق برسیم. و واقعاً چارچوب یک توافق را داشتیم؛ بدون برنامه هسته‌ای.»
ترامپ در ادامه تاکید کرد تهران پذیرفته بود مواد باقی‌مانده از برنامه هسته‌ای خود را تحویل دهد، اما بعد از هر توافق عقب‌نشینی کرده است. او گفت: «هر بار توافق می‌کنند، روز بعد انگار می‌گویند چنین گفت‌وگویی نداشته‌ایم. این حدود پنج بار اتفاق افتاده است. مشکلی در آن‌ها وجود دارد. واقعاً دیوانه‌اند. و به همین دلیل نمی‌توانند سلاح هسته‌ای داشته باشند.»
رییس‌جمهوری آمریکا در بخش دیگری از مصاحبه، در پاسخ به این پرسش که آیا توان و مقاومت حکومت ایران را دست‌کم گرفته، گفت: «هیچ‌چیز را دست‌کم نگرفتم. ما به‌شدت به آن‌ها ضربه زدیم.»
ترامپ تاکید کرد آمریکا عمداً بخشی از زیرساخت‌های ایران را هدف قرار نداده است و افزود: «پل‌هایشان را باقی گذاشتیم. زیرساخت برق‌شان را باقی گذاشتیم. می‌توانیم همه آن را در دو روز نابود کنیم؛ همه‌چیز.» او گفت به تاسیسات نفتی و برخی زیرساخت‌ها در خارک حمله نشده، زیرا آسیب به آن‌ها می‌توانست موجب از بین رفتن نفت شود.
رییس‌جمهوری آمریکا درباره وضعیت مذاکرات با جمهوری اسلامی گفت افرادی که آمریکا با آن‌ها در حال گفت‌وگو است، به گفته او «منطقی» به نظر می‌رسند، اما توان یا آمادگی لازم برای تصمیم‌گیری ندارند.
ترامپ در پاسخ به این پرسش که آمریکا در حال حاضر با چه کسانی در ایران طرف است، گفت: «با افرادی طرف هستیم که فکر می‌کنم منطقی هستند، اما از توافق می‌ترسند. نمی‌دانند چطور توافق کنند. قبلاً در چنین موقعیتی نبوده‌اند.»
او در پاسخ به این سوال که آیا تا زمان دستیابی به توافق صبر خواهد کرد، تاکید کرد: «من کاری را انجام می‌دهم که درست باشد. باید کار درست را انجام دهم.»
او همچنین گفت مقام‌های ایرانی به او گفته‌اند محل نگهداری مواد هسته‌ای به‌شدت هدف قرار گرفته و «کوه گرانیتی» روی آن فرو ریخته است. ترامپ افزود: «آن‌ها گفتند فقط دو کشور می‌توانند به آن دسترسی پیدا کنند؛ ما و چین. گفتند خودشان توانایی دسترسی ندارند چون کاملاً نابود شده است.»
ترامپ گفت: «نمی‌توان اجازه داد ایران سلاح هسته‌ای داشته باشد. آن‌ها از آن علیه ما استفاده خواهند کرد. اول اسرائیل را نابود می‌کنند، بعد خاورمیانه را، بعد اروپا را.»
او درباره افزایش قیمت سوخت در آمریکا گفت فشار اقتصادی ناشی از بحران کوتاه‌مدت خواهد بود و افزود: «وقتی مردم توضیح کامل را می‌شنوند، همه موافق می‌شوند. این یک درد کوتاه‌مدت خواهد بود.» ترامپ گفت پس از پایان بحران، قیمت انرژی «مثل سنگ سقوط خواهد کرد.»
رییس‌جمهوری آمریکا در پاسخ به نگرانی‌ها درباره افزایش فشار اقتصادی بر خانواده‌های آمریکایی در پی جنگ با ایران و رشد هزینه‌ها، گفت شهروندان باید این فشارها را تحمل کنند زیرا به گفته او هدف، مقابله با تهدیدی بزرگ‌تر است.
ترامپ در واکنش به این موضوع که برخی آمریکایی‌ها افزایش هزینه‌ها و بدبینی اقتصادی را احساس می‌کنند، گفت: «باید تحمل کنند و باور داشته باشند که ما آن‌ها را به نقطه بهتری می‌رسانیم. اما من باید کار درست را انجام دهم.»
ترامپ در ادامه، فشارهای اقتصادی ناشی از بحران را با ضرورت مقابله با جمهوری اسلامی مرتبط دانست و گفت: «به مردم گفتم متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا همچنین گفت کشتی‌های حامل نفت ایران که چین در روزهای اخیر خارج کرده، با اجازه واشینگتن حرکت کرده‌اند. او گفت: «ما اجازه دادیم این اتفاق بیفتد.»
ترامپ در پایان در پاسخ به این پرسش که آیا حکومت ایران در نهایت عقب‌نشینی خواهد کرد گفت: «بله، قطعاً. هیچ شکی ندارم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75494" target="_blank">📅 07:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75493">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otXJD3HKUFpgIWWi37jaduEKGDad3u0kR8LIAmXojPAa40sseW0VXVgKfWd3vS900BM-mVip2-o0kHoRPm8n3ICCXdvOiLQ0e2TicR1x-XvgDV_WzJkRar3zxTTZDwuaYUkjL0jcfRPjdLDoylk7DjG8HovtKHGtybh-rrz3cDQ-sS9pgUKq1z_IlOyOStBTcqqjBwwVI9Fn4LjhxWe4h07wywIaYbBxcd2uGNcdAACbMDrSmh5o6xYaq2sBqyFwpnvEmrUD3MqQiSaNJXqBApG7voCWv0ABFFWVgsGmG7MHxU8wVWEX0GhjuA63qRHK0HwFbQqR4f_yDV5RZ7vR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر خارجه جمهوری اسلامی، در واکنش به بالا رفتن قیمت انرژی در آمریکا، در ایکس نوشت: «در حال حاضر، افزایش قیمت بنزین و حباب بازار سهام را کنار بگذارید. درد واقعی زمانی آغاز می‌شود که بدهی آمریکا و نرخ وام‌های مسکن شروع به جهش کنند.»
او نوشت همین حالا هم میزان ناتوانی در بازپرداخت وام خودرو به بالاترین سطح خود در بیش از ۳۰ سال گذشته رسیده است، اما تمام این‌ها قابل اجتناب بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75493" target="_blank">📅 07:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75492">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTA1fU3EWb_frn0ZJDxYU9gfF48EFVEI4op76PAtKQnYqOZlr2SDosabJobJ-q_bXxUu9lApuDq8k7uUwj5LBGpMTdQi3iI2tkWew3Fb5Ru-TNzZDqb5cbrPrHEDQjVBY_FhiVYfGCaY3XF7GnL4hpeJfTAP9-_sSOdST3TbN1thP_EzkkCY93snKNtp087DaWI-_QGZw94sKQg832jqUBo_fA_c9ExmHpSN-7GhH7NAeDeSILCxnalItHm6kbMmTcbyTAVLxwqqKO2RdBse1DhX1XevIRyKasxgwdXhQ1VlT1q2DKzKh9_5NT8lcsCiv8yWxACuDr2-H08W-0ZqXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نماینده چین در سازمان ملل و و رئیس دوره‌ای شورای امنیت، از پیش‌نویس قطعنامه پیشنهادی آمریکا و بحرین درباره تنگه هرمز انتقاد کرد و گفت که «محتوا و زمان‌بندی آن مناسب نیست و تصویبش کمکی نخواهد کرد.»
به گزارش رویترز، این پیش‌نویس قطعنامه از ایران می‌خواهد که حملات و مین‌گذاری در تنگه هرمز را متوقف کند. اما دیپلمات‌ها گفتند که اگر این قطعنامه به رای گذاشته شود، احتمالا با وتوی روسیه و چین روبه‌رو خواهد شد.
دو کشور ماه گذشته نیز قطعنامه مشابه مورد حمایت آمریکا را وتو کرده بودند و متن آن را علیه ایران «جانبدارانه» خواندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/75492" target="_blank">📅 07:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75491">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PO3T0xnh7IgzdakJ0fPZTLxlv2e5Z5JgDspBeQOHYwuFTYemUAzhUaL6ot3Zdjb7BpWu9ypBcBXf-SdKJNqKyN7V-7ymkLL-dOdz5OINq6rSjb7159h-dTmdeFahDW8CotvRE-bCZtyi0zjHejOqANOuZNPDUE20GbO8FoCcA-I2Oj-WZAV0ePLFgBbYf22Q0I6XwLZdHX8JFDABYiResKN1vIJXi9UFiCRckEkVkEpvoG_lHu-pIF7qURR6L3HvCkC7VME--PrdCAiCkVH8-LM-vmSrmrMsPHqzJDx8dvSd4ezPpTlsDIrb0ibRbL_r0d3gU5QB1r49oB_cJ4TmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرزند عبدالرحیم موسوی، رییس ستاد کل نیروهای مسلح جمهوری اسلامی، گفت که جنازه پدرش که در نخستین روز حملات اسرائیل و آمریکا به دفتر خامنه‌ای کشته شد، نزدیک به ۳۰ روز زیر آوار مانده بود.
موسوی پس از کشته شدن محمد باقری در جنگ ۱۲ روزه، به‌عنوان رییس ستاد کل نیروهای مسلح منصوب شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/75491" target="_blank">📅 23:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75488">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m8N1TuUdk-gGAJh2O0PmIkgafevDJQUUqhqDRRv8mx-WYeYZgJENjkbVVAbHrjMDbUBqdKC7Z1_r4mIWuTvJ4pjE41AlVNXEMf1wCV02SKsCGE9uIaWrxfSpqXlqx-I-QGQpC97ZwEfrN320fyXAumSqCzr8uqsjy9y31ZGl0IP-pv1UgvfGDZcA1pEOJg1xrrUl0fmMm8bItcuXTv0FloahbpPsO6nQjxvyZIbpk8a4V-nfX2xLYvCkiklNKvOEGDZCdJqquXTc1aU_iND-Pnv6a2TqjL4lL2dCZYHndBv1xE-pPN-_HgoU3pt5Zu14raiBiBQrnJzHkz4NuWMK5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db61779f21.mp4?token=SpKdUyMBw9H9Ck9LqxuXKCZCKOMcO6hlXWzdThUHTDDEHl5z4f5lXxNF33kmlC0YHRBF0-DOCVW5o-PIgIlEg3OcZQ2uAczA2um5_BkquOWS5IJuNA53xhY-3Mr3V-zfwAC5WaPF541LhiCzhG5RDwQdmDBSmCwhH8hJ6bj4n-Jd6Wk8tM-ZaPC4rglNPtNF13WnDpDm-ShBu0IoVK_6rLv47WzeUf04uga2Zgobboz2Yl7qOu6YGtQscPEu9N2yModEjF4ci-PJooym3FDC1Vklp_Zu4487EZj8UN88_Clc-QapmP1VDLDPLsjScDkrz-THptGwix5feqMQnst6Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db61779f21.mp4?token=SpKdUyMBw9H9Ck9LqxuXKCZCKOMcO6hlXWzdThUHTDDEHl5z4f5lXxNF33kmlC0YHRBF0-DOCVW5o-PIgIlEg3OcZQ2uAczA2um5_BkquOWS5IJuNA53xhY-3Mr3V-zfwAC5WaPF541LhiCzhG5RDwQdmDBSmCwhH8hJ6bj4n-Jd6Wk8tM-ZaPC4rglNPtNF13WnDpDm-ShBu0IoVK_6rLv47WzeUf04uga2Zgobboz2Yl7qOu6YGtQscPEu9N2yModEjF4ci-PJooym3FDC1Vklp_Zu4487EZj8UN88_Clc-QapmP1VDLDPLsjScDkrz-THptGwix5feqMQnst6Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر و یسرائیل کاتز، وزیر دفاع اسرائیل در بیانیه‌ای اعلام کردند ارتش این کشور، عزالدین حداد، فرمانده شاخه نظامی حماس، را در یک حمله هوایی هدف قرار داده است.
عزالدین حداد، از فرماندهان ارشد گردان‌های عزالدین قسام، شاخه نظامی حماس است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75488" target="_blank">📅 22:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75487">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZb17GCqkN5-aKSSqf8sy5n1oXqjLFgErzDNN7m2MWiTUSErieGQd7nZnqTyvpROtbPAJXgRfQzh3u3q7liqQVCvOzh5bRLQtKFTX0AFnCwAsLQIIows7WgAfFaDHKb0lGfaDLghlSV7_Rgb5DJarPwXBhyHTdmoqc9gfQtreuB48Boy6gjbGQHxT_PD9Z_pzaAYUApZW_4xADAE0r7xO7b84Od1BVpdtHjxEL9yo94Drxm1phtr50LV6mZjpblne-W5HpPk0bcehxIt7HXV1rGZV7EvxIWzrLS5s2w6DaaaKPzpuA8pq8TP_Eo0rgqawnZGNg_AOh9sfS61QMQT4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا سپهوند، عضو کمیسیون انرژی مجلس شورای اسلامی از کمبود روزانه دست‌کم «۲۰ میلیون لیتر بنزین» در ایران خبر داد.
به نوشته خبرگزاری تسنیم، این نماینده گفته که تولید روزانه بنزین در ایران بین « ۱۱۰ تا ۱۱۵ میلیون لیتر» و مصرف روزانه بین «۱۳۰ تا ۱۳۵ میلیون لیتر» است.
سپهوند با بیان اینکه «در کوتاه‌مدت امکان افزایش تولید وجود ندارد»، خواستار جدی‌گرفتن «مدیریت مصرف سوخت» شد.
پیش از این وزیر خزانه‌داری ایالات متحده گفته بود ایران به‌زودی با «کمبود بنزین» مواجه خواهد شد.
اسکات بسنت با انتشار مطلبی کوتاه در شبکۀ ایکس، نوشته بود: «در حالی‌که باقی‌ماندۀ سران سپاه پاسداران، مثل موش‌هایی که در لوله‌های فاضلاب غرق می‌شوند، گیر افتاده‌اند، به لطف محاصرۀ دریایی ایالات متحده، صنایع نفتی آسیب‌دیدۀ ایران، در حال از کار افتادن و توقف تولید است. پمپاژ نفت به زودی متوقف خواهد شد».
او سپس پیامش را به سبک دونالد ترامپ، با جمله‌ای که به‌طور کامل با حروف بزرگ نوشته شده، به پایان برده بود؛ جمله‌ای با این مضمون هشدار آمیز: «مرحلۀ بعد،‌ کمبود بنزین در ایران!»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/75487" target="_blank">📅 21:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75486">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/575f6be6da.mp4?token=m_CeWPbuYoPVm_5kgs-PTuxyrW8_uKXeMFJZ0vCb1tA-CrpOKrniaDokVG6IqWbGnkRIQmw46_pbJrycWWJqR1ixGM3uMtGTyc-n-Fcskdt--Vta4xJU1EcYT5qnbgXq5U4MmDv8LhNS3-FrWpYyUqVN3-qhmVJrU717e3X0Smf7Bwi4_J7NUcOsToEvJsXsxZ2H-Np6biq3qvWiyq_wq0NkvtvcA3V26X42uhkA9DlJhQ5o0HOwkRyip1o9E4oWX6D54Jsu-gfr92OlYu7zNp8Kk2ySYsjol7gVi24tWEsUY8mjDm1ZO1o7E_HdSLu7Gka8UoalgBlxPVJU-IL-pA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/575f6be6da.mp4?token=m_CeWPbuYoPVm_5kgs-PTuxyrW8_uKXeMFJZ0vCb1tA-CrpOKrniaDokVG6IqWbGnkRIQmw46_pbJrycWWJqR1ixGM3uMtGTyc-n-Fcskdt--Vta4xJU1EcYT5qnbgXq5U4MmDv8LhNS3-FrWpYyUqVN3-qhmVJrU717e3X0Smf7Bwi4_J7NUcOsToEvJsXsxZ2H-Np6biq3qvWiyq_wq0NkvtvcA3V26X42uhkA9DlJhQ5o0HOwkRyip1o9E4oWX6D54Jsu-gfr92OlYu7zNp8Kk2ySYsjol7gVi24tWEsUY8mjDm1ZO1o7E_HdSLu7Gka8UoalgBlxPVJU-IL-pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاوه مدنی: وضعیت دردآور جزیره مارو (شیدور) ملقب به «مالدیو ایران»
نشت نفت به
#خلیج_فارس
پس از حمله به تأسیسات نفتی جزیره لاوان در فروردین ماه عامل این فاجعه بود.
#جزیره_مارو
[با کیفیت بیشتر:
۶۰ مگابایت
]
KavehMadani
برشی از سی‌ثانیه سوم ویدیوی بالا درباره وضعیت ساحل بیشتر مورد توجه قرار گرفته:
AzamBahrami
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/75486" target="_blank">📅 20:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75485">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYa7NRxh8xeQZCy_GzXv1nsZtSTDhXwplAjKCgF9XN2gXmXYUvtSFxQ5SYERG1utRrijD8He2xn66818uutI84yMYHWzQO2-lSd67AYmrM7Uj-ooHTzh6PajEAAdTNmvdhpWOjwItY2XITjpf1Yjvw65AIwVTorAszM7729GIOEuMdruSWnXYUpwJy0Vy6c5nbl8c5ETesV0jBIcqO8RO15ew57KT_utuK_8OdMv9pLqS-QxiQhXVDm-ljaXpnqFLdr2iCVbXcUOfyLPiklBwaM70JK8mOeEUmIO994ItkalcyJapzeq2A3rS5WpdDe6T9i1yII7bueJi86MoLjVQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه پاکستان اعلام کرد که یازده شهروند پاکستانی و ۲۰ شهروند ایرانی که در کشتی‌های توقیف‌شده توسط آمریکا در آب‌های آزاد گرفتار شده بودند، به اسلام‌آباد منتقل می‌شوند.
اسحاق دار افزوده که «تمامی این افراد از سنگاپور به بانکوک رسیده‌اند و اکنون سوار پروازی شده‌اند که قرار است اواخر امشب به اسلام‌آباد برسد. سپس بازگشت برادران ایرانی به وطن خود تسهیل خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/75485" target="_blank">📅 19:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75484">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZQa9Bw-W2CeG3kEUQpqQC27WvJehFSYhHqUZRhb7Ia8ETwF-Jrk5yykr6UAq2LKZ-BqxUNzLVVS3QYVbsLoM-WGEQFI8DUOSRWnlMdCOQSmGro001MPOHBsFAF3xmpZzKWqb0s2pe909AKZeNfOon9Jy0QAD5EwxR__8yZN6Tehg4xzBC5gW4mJiIKANenLPapQN890ICkweVHsPPy07b4C9XdvjyzYQwiAYyUA1QwP6-6rbmrIJm8eI3biqxzQu-YuFdP5XDK7ZAEeznfYR69kYLbSTUbFfzmkv_635ujvNc0rmhtlIpjmvtqV_G4KBckCkgRGZGqAGMStrNjpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدراعظم آلمان می‌گوید در جریان گفت‌و‌گوی تلفنی با دونالد ترامپ، رئیس‌جمهور آمریکا، هر دو بر سر ضرورت باز کردن تنگهٔ هرمز توسط ایران و ممانعت از دسترسی تهران به سلاح هسته‌ای، توافق داشته‌اند.
فریدریش مرتس روز جمعه ۲۵ اردیبهشت در شبکهٔ ایکس نوشت که در مسیر بازگشت رئیس‌جمهور آمریکا از چین، «تماس تلفنی خوبی» با او داشته است.
او افزود که آن‌ها توافق دارند که «ایران باید همین حالا پای میز مذاکره بیاید. باید تنگهٔ هرمز را باز کند. نباید اجازه داده شود تهران به سلاح هسته‌ای دست پیدا کند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/75484" target="_blank">📅 18:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75479">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rOJfd_ZUt1xymYlXOkDUY8ALxVM4e2yWgH_b3XbPuBh0JrsqcqaGV_tYMMhJN8xHDQ_0EXSC9HRuZpLiEAn_RDvF-_yYE5JbacivWMatBASNCYLBTGSzsEQT0hcqIM-a4SCpWUTVohpimDhG8RPB7wncr0NE0vS0H2DRJ46eXW7Xhtv-pjDipy0ub42PHbO58koURYZR-2nOswiq88S5DdnpSewoKu0pdmpKGA6KNcfWuGoM6YeYnQEEm6vq9t9DZNSVzNfDOlhlkVrF3KFoAQNSL2CA50lfKKMF59G376gqJMnXusZToIgoVJz7Iwbw58nCSU-C09Pz_jhsTskbhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fjzPoO0GAPlViHPjSFTJUM8Hq86sdKQs_OiVOLeHiCTNzZdIRDUWJ9D5i7JrSKB8riBT_S5env3w3dxcWGrLwwxUsMeNl0LU2SGs2yetpj4XCjRT2qgI_rp42YObyGBae5f4I1GjO1yKHHupCBnyCYKBKOHLuF4LH7qj7FGJPrlCP1BgtSy--0w43VQxsJunmqegALXrru-O1KKeeAUwFEOqnRmHsXi0HJDIfGhYpdGQHFDapqRRoioyq8bqKCWTRKB-93ZW78BWpxd9mQo0uB8Bg9vDECWMWTmTXkL5bDBQVc930kIp6rEHUpaza3WlMbHbhH1my-CELx5mRBmISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZAA4oCkeF68XzMNr3Vc3x6My-6OeHnUnAZ-SjLby56UcTsA0sNZnLptBBABDpLKn3yTVtWM58KKRyl1I7TY2wIvc63utKoAhCtx29JspVUdGGQrm7v1m7RGECkITnrB9ji_INnv_i5FozoHfOQU9NnA49bqltUX-0DZ1P3mTGmNzm5NyRONH00kYidZuecLM47QLx-07wgmkmE8HMJu6_jE4zPqDSKJHjx_dPK3HWdFTMya0cpwSnuI_FpWL3mWi3y3QyNhmXMiPqzkBhVYubQfZV8syGYLuuM-F3bui13d7uiRxbbRErbjjC5haP5ocWCSh1FYFpYcH_1WNvFAzHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1948a10693.mp4?token=QL6lh8M_2xbHJLJXG9c6okkJS1nNWR-_APN4JgT7F7jp6z7CYvOF2lUhR0dk-_Zem-5j6Uqvo6gxSrB7YmksXJVf-ODyt69k-MqAq_JnQTNjBvdUq5ZbnUNWQ2MKXf32vbTkovllK2lGcYFgchkJSQMTdvUIEO5VD6tGkRCEblDHvmEu21MFCdB9CG4AYe2_GPT1N-swHbgCLSZOw9TmvAlFJwhajw7cUQQi-OvK6Jf7TJwzIy8MLQVQR0yJJdFoxxcGUnd1EyvbvAGviwZgEAbzDEq0nJ4n-Yw-16Y1-XSK-qmMwRldFfoNjMDC1KK_3QlS8bJTFAedU4oItyOuMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1948a10693.mp4?token=QL6lh8M_2xbHJLJXG9c6okkJS1nNWR-_APN4JgT7F7jp6z7CYvOF2lUhR0dk-_Zem-5j6Uqvo6gxSrB7YmksXJVf-ODyt69k-MqAq_JnQTNjBvdUq5ZbnUNWQ2MKXf32vbTkovllK2lGcYFgchkJSQMTdvUIEO5VD6tGkRCEblDHvmEu21MFCdB9CG4AYe2_GPT1N-swHbgCLSZOw9TmvAlFJwhajw7cUQQi-OvK6Jf7TJwzIy8MLQVQR0yJJdFoxxcGUnd1EyvbvAGviwZgEAbzDEq0nJ4n-Yw-16Y1-XSK-qmMwRldFfoNjMDC1KK_3QlS8bJTFAedU4oItyOuMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز جمعه ۲۵ اردیبهشت در مسیر بازگشت از چین در پاسخ به خبرنگاران، درباره آخرین پیشنهاد ایران در مذاکرات هسته‌ای گفت که آن را «از همان جمله اول» رد کرده است.
او با بیان اینکه محتوای ابتدایی این پیشنهاد «غیرقابل قبول» بوده، افزود: «حتی ادامه آن را هم نخواندم.» ترامپ تأکید کرد که صرف تعیین بازه زمانی مانند ۲۰ سال کافی نیست و آنچه اهمیت دارد، ارائه تضمین‌های واقعی و قابل اجرا از سوی ایران است.
رئیس‌جمهوری آمریکا همچنین تصریح کرد که، هرگونه توافق باید شامل انتقال کامل مواد و سوخت هسته‌ای از ایران باشد و افزود که توافقی مبتنی بر «حرف‌های توخالی» قابل پذیرش نخواهد بود.
@
VahidOOnLine
دونالد ترامپ در پاسخ به پرسشی درباره پیشنهاد اخیر جمهوری اسلامی گفت این پیشنهاد را بررسی کرده، اما به گفته او، اگر از جمله نخست یک متن خوشش نیاید، بقیه آن را کنار می‌گذارد.
ترامپ در پاسخ به این پرسش که جمله نخست چه بوده است، آن را «غیرقابل قبول» توصیف کرد و گفت مسئله اصلی از نگاه او این است که ایران نباید «هیچ شکل» از برنامه هسته‌ای داشته باشد.
در ادامه، خبرنگار از ترامپ پرسید آیا دوره ۲۰ ساله برای او کافی نیست. ترامپ پاسخ داد که «۲۰ سال کافی است»، اما به گفته او، سطح تضمین‌هایی که جمهوری اسلامی ارائه می‌دهد اهمیت دارد.
ترامپ گفت که اگر قرار است توافقی ۲۰ ساله مطرح باشد، باید «۲۰ سال واقعی» باشد و نباید به گفته او، توافقی مبهم یا ظاهری باشد.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا روز جمعه ۲۵ اردیبهشت و در زمان بازگشت از چین به آمریکا در هواپیمای ایرفورس وان به خبرنگاران گفت با وجود آنکه نیروهای مسلح ایران در جنگ نابود شده‌اند، ممکن است نیاز به «یک پاکسازی کوچک» وجود داشته باشد.
ترامپ ساعاتی پیش در گفتگویی با فاکس‌نیوز هم گفته بود که نیروهای مسلح جمهوری اسلامی در چهار هفته گذشته، تلاش کرده‌اند تا تعدادی از پرتابگرهای موشکی را از زیر خاک بیرون بکشند و جای بعضی تجهیزات را عوض کنند، با این حال «آمریکا قادر است در دو روز همه این‌ها را نابود کند.»
@
VahidOOnLine
دونالد ترامپ در پاسخ به پرسشی درباره اینکه آیا شی جین‌پینگ، رئیس‌جمهوری چین، تعهدی قاطع برای فشار بر جمهوری اسلامی به منظور بازگشایی تنگه هرمز داده است، گفت از کسی «درخواست لطف» نمی‌کند.
ترامپ گفت: «من درخواست هیچ لطفی نمی‌کنم، چون وقتی درخواست لطف می‌کنید، باید در مقابل لطفی انجام دهید.» او افزود که آمریکا به چنین کمکی نیاز ندارد.
رئیس‌جمهوری آمریکا در ادامه گفت نیروهای مسلح طرف مقابل «اساسا از بین رفته‌اند» و ممکن است به گفته او «کمی کار پاکسازی» لازم باشد. او همچنین به آتش‌بس اشاره کرد و گفت این آتش‌بس به درخواست کشورهای دیگر انجام شد.
ترامپ گفت شخصا چندان موافق آتش‌بس نبوده، اما آن را به عنوان لطفی به پاکستان پذیرفته است. او از مقام‌های پاکستانی، از جمله نخست‌وزیر و فیلدمارشال این کشور، با تعبیر «افرادی فوق‌العاده» یاد کرد.
@
VahidOOnLine
دونالد ترامپ گفت آمریکا ممکن است در مقطعی برای حذف آنچه «گرد و غبار هسته‌ای» نامید وارد ایران شود. ترامپ در مسیر بازگشت به آمریکا و در هواپیمای ریاست‌جمهوری، ایر فورس وان، به خبرنگاران گفت: «در زمان مناسب، یا وارد می‌شویم یا آن را به دست می‌آوریم. فکر می‌کنم احتمالا آن را به دست می‌آوریم، اما اگر به دست نیاوریم، وارد خواهیم شد.»
او افزود: «فکر می‌کنم آنها کاملا شکست خواهند خورد و ما هیچ خطری نخواهیم داشت. ما تجهیزات لازم برای خارج کردن آن را داریم، هیچ‌کس دیگر ندارد؛ شاید چین چنین تجهیزاتی داشته باشد.»
ترامپ پیش‌تر نیز در ماه مارس در کاخ سفید درباره ذخایر اورانیوم غنی‌شده جمهوری اسلامی هشدار مشابهی داده و گفته بود: «یا آن را از آنها پس می‌گیریم یا آن را برمی‌داریم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/75479" target="_blank">📅 17:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75478">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cii-zFgClF34ChEbRRnWIB0KlvToNboMZhNcvNdJSnFPBUKkiUShAiVKqfbhKV2FyLoCpE2LAVJqmcEGxzt0yDt-QYsY7BWzp2C-FR-mRb560vyJUvo1hdnVwWejQFlGHTCh2sUMiAieo1L0doybnVXgMm_PhBXyOMbppsX_L2o28aGDyuTkEyqNwOIkBay3zELo0S4VqlXHJPhj4PCLVYO3KcWZHJ7merd6pxOpzMvlvN19jAj2Ux71wJPnl2M4lelpz3mZBAt8qotSeIBs-39GBCL4MLho895xS55sjUKnHhWEw_OKHRnUw1j_l7IiNmxLRaRQ35qARElfioJgxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست وزیران خارجهٔ کشورهای عضو بریکس در دهلی‌نو، پایتخت هند، به‌دلیل اختلاف‌نظر میان اعضا به‌خصوص بین ایران و امارات متحدهٔ عربی بر سر جنگ ایران، بدون صدور بیانیهٔ مشترک پایان یافت.
به‌گزارش رویترز، هند روز جمعه ۲۵ اردیبهشت اعلام کرد به‌جای بیانیهٔ مشترک، «بیانیهٔ رئیس» منتشر شده است، زیرا برخی اعضا دربارهٔ تحولات خاورمیانه دیدگاه‌های متفاوتی داشتند.
گروه بریکس شامل برزیل، روسیه، هند، چین، آفریقای جنوبی، اتیوپی، مصر، ایران، امارات متحدهٔ عربی و اندونزی است.
روز پنجشنبه رسانه‌های ایران از تنش لفظی در این نشست خبر دادند و نوشتند عباس عراقچی، وزیر خارجه ایران، امارات را به مشارکت مستقیم در جنگ آمریکا و اسرائیل علیه ایران متهم کرد و گفت میزبانی پایگاه‌های نظامی آمریکا از سوی ابوظبی و همکاری امنیتی این کشور با اسرائیل، آن را به بخشی از جنگ تبدیل کرده است.
روزنامهٔ لبنانی الاخبار نوشت که در مقابل، هیئت اماراتی خواهان آن بود که هر بیانیهٔ نهایی، حملات موشکی جمهوری اسلامی ایران به این کشور و توقیف کشتی‌ها را محکوم کند، در حالی که تهران بر درج محکومیت صریح حملات آمریکا و اسرائیل اصرار داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/75478" target="_blank">📅 17:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75477">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdQbdzdCT_ZLPOX8UEHFPRQaathn88bCkrxYdrXZo_lsbgLSaX_ER7bBzjUQAssTBPWbDL4x-OAwm8cDnevuv6dkGXGasuY88kl-MzqLG6axyLSx45UM16zW7mrOa-F3SJeePyUkIzR86tNHt4Lhp_ffM6yBQ-0Tt4iElxetz2_9ACR2OFrxmA89-X0I4rt-JfZlZrgnPTTOpygWKhj5hmZmyZ8m4mRaX1EassoNQLm22vQeQqWORJHRl-noGh_Y5gtSittUOfHs2KtJQpJ4RM4W5h6ikArrRAkk3mo59YP8ojTzYec7LM3ZQLsktLFvazegumpqInJ1nts3iQEVuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی اعلام کرد این کشور ساخت یک خط لوله جدید نفتی را برای دو برابر کردن ظرفیت صادرات نفت از طریق بندر فجیره تا سال ۲۰۲۷ تسریع خواهد کرد. این اقدام توانایی ابوظبی برای دور زدن تنگه هرمز را به‌طور چشمگیری افزایش خواهد داد.
دفتر رسانه‌ای دولت ابوظبی روز جمعه ۲۵ اردیبهشت اعلام کرد شیخ خالد بن محمد بن زاید، ولیعهد ابوظبی، به شرکت ملی نفت ابوظبی، ادنوک، دستور داده است اجرای پروژه خط لوله «غرب به شرق» را سرعت ببخشد. به‌گفتهٔ این نهاد، این خط لوله اکنون در حال ساخت است و انتظار می‌رود در سال ۲۰۲۷ به بهره‌برداری برسد.
در بیانیهٔ دولت امارات اشاره‌ای به زمان‌بندی اولیه این پروژه نشده است.
خط لولهٔ کنونی نفت خام ابوظبی، موسوم به «حبشان ـ فجیره»، ظرفیت انتقال روزانه تا یک میلیون و ۸۰۰ هزار بشکه نفت را دارد و نقش مهمی در افزایش صادرات مستقیم نفت امارات از سواحل دریای عمان ایفا کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/75477" target="_blank">📅 17:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75471">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GJ7hvijjC_7CE2Ha0BvWlAaNl9WSOyOlGzbBRoWs7CzmVMuWMxmn4OSYg4ePJ2J3xQlxiOeBxxyVHHNc7a1Ez9HFtbc-Z1odru_RfcbblFX7wjZwn-XqV9v4mDilo8Sc-wkQeWH3x4Gn6trhN4PHpKFNhaAW5chX67ktPdcDHjQeBojp3-cbgvhuECvYurIzxRBiGMlOqx7jHnHcAbdbNZh0z-M244uE2Ym4SfOevEcdyhL-drKedWvK1T2YEcMCOuMiZFUqfN0oWdGfHK94FBZr7oK7U4R0hJD6B3ebFcchhLbMEdFN7CihfPDZ4EQbk-hXGqrQFW61z6ZYbhw3Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OIY8Q4K2UV8ZpsAyr2UX2P68eSMTp7a4ggghhNkAC36YnsH2VqE9pPPxJyU7mevYButwTjuwAAJYTVqm606VChyyH_FakOPQNxJCudIgAb683HeHbdgAM1AXxX0ybm5cuCB8jEsAahMwzfyKWbkzaR-FfQ55ATzz-Xs5jfM2BdcplrMd1aiY88mOFtfifHGiV-jlX6ay8PQk0XXvWmL8Evb5zYLFWtIsXCWwyErPIoYz2t2o-1tqf_0I4ftdfjylKr-jipFli4o6r36yMSEDNaxgN8SHNU84V3bHriXUDIolYzrnB8_wz1UX2Ll96JvZSEP6GkAgb8HUYv3eYhZKkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oJDZgBkdvOP0zRx83vBJukAOt1Ah0TaDwPOYCDeeRUJJ_fnYITnFz_c61BbfbvQAhuD8OzxkW0Z0kC2V9Kmct3tzapSk4dP1U2JI-yqDzAYh_epwhrnCFGGs1jG3GyP7sopr4GkshZfqYtWKFqz4WLcSGQKyENytzF67iKih6mmxAbfbBkEoe8m6OtBRUuvGTXAy7CVKAk9YuDLaMb_ItOjduqPkVbQdZGhc0GKAFk6vQz18MhX2sgdLtve2yLy5wtXZKTsmJ_OXuLF2mN7Qr3r6TcVf_EAyGFLZIar-lWIIrDdPWioDj4MfZrit6nkffrlW_REO3AWfGWnbZe9g9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v7TmlgdP9kpT1zAfkWWyAf17rEZC9TtbgLk58wqk3MwG68Mb2K9t1oV00Oo-De8qv5RM64UcKCPQkhg_52g-Xov8hnlYMAutX5dOogAPWxLN1HT9cHimNpd6aCTN-Kb3CvmFKbYsA1enJLbFE2_B9jfQ1vxZSya5fTx4uGaH33C4m0qGCFgdh5Qy8-baEtBC_suWzFxMfydTlEvkDGswlSVnacQ3pWcJMBoS02vfJAmyIc_eJ2DojCgv7Zy2NUfXgK1zE6F1znoUDFQ0UMOZTJZheGPILTVlugDToqkAnSA8ZaRPraFMr2SM5XEDnF5vOkdAnd-h9ZQtgTSZ_NLaPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UpM4wlOLkgYENn8HIAw8JaQxVpS3Ej-aVN6xn7gEU51mbHM8O8d0AOJQ5QPxMGMYm21L9zx99lZeiZ9kej2GhJFi23H_QkI7q5KjmkFJnr8wITYICNHy-V5DzF01SK-W1Dr4q67XfJi7Mny3fpkM-Y0mfqzYXqqBWrnZudDPO-JDyn7Gv6A9fAuFhOBVqmHbqABRWUK_qXJp5OpeLDuDrQuLsRcs4NaPhZGwh7SObEWSr_UxXWkXoMHFut8oYIZjmAckBq3527zZFubpzwykQ7iFP2J5mJQDnVDJQBjU5ec7AsXupsj6Pb5GKP8w4gGYUT4vSRePViF-k2AfCNMeZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A3Leqt71DYu4HLOXqnQPfGyqy-tz56ErJIN8v2SLtQjs-_psB3ZnZPx5_15qKM1KBG77jf4k9FSWk50n61rzhTBN93oCLAqxnx8BFpoVVRRG-uTS3631rl9EdpKS34TSwtPbP7D7x3QBq4XvxbdnKagMQtEnBPm6EP1T9acQdEpzPG2hQj-s2AMF4d8XY2nkA8U8ikdQX-9q8-dGPoi_nagztX2Je4VesKV0qtpAmbTu-I17D410aDy3HPluWaRBMzcxm-PoFoHKZnYcL8OxdAZS-N6a-Ppob_1svzpjsM4kAd0MSlvfyw60znlpgHe5rSoWQPLXp500sSG6758cJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا در مصاحبه‌ای که با فاکس نیوز انجام داد گفت او درباره ایران با چین صحبت کرده است.
ترامپ افزود فکر نمی‌کند که چین هم خواهان این باشد که جمهوری اسلامی به سلاح هسته‌ای دست پیدا کند.
او گفت جمهوری اسلامی می‌تواند یا «توافق کند و یا «نابود» شود. رئیس جمهوری آمریکا گفت نمی‌خواهد چنین کاری کند اما آمریکا قوی‌ترین ارتش جهان را دارد.
ترامپ گفت ما در جمهوری اسلامی با «رده سوم» رهبرانش طرف هستیم. او گفت رده اول و دوم رهبری نابود شدند و فکر می‌کند رده سوم از رده اول و دوم «که دیگر با ما نیستند» «منطقی‌تر» و از لحاظی «باهوش‌تر» هستند.
او این تغییر را به‌نوعی با یک «تغییر رژیم» مقایسه کرد.
ترامپ با اشاره به اینکه جمهوری اسلامی «پنج روز» زمان صرف کرد تا به پیشنهاد آمریکا که «یک ساعت» هم زمان نمی‌برد پاسخ دهد، افزود جمهوری اسلامی در داخل خود «آشوب فراوان» دارد و «چیزی به جز آشوب» ندارند.
ترامپ در مورد حمایت چین از جمهوری اسلامی گفت که رئيس جمهوری چین، شی جین‌پینگ قویا گفت که به جمهوری اسلامی سلاح نخواهد داد.
...
او افزود «امیدوارم» جمهوری اسلامی این مصاحبه را ببیند چرا که آمریکا می‌تواند به سرعت همه تسلیحاتی که آن‌ها در طول آتش‌بس ممکن است به آن‌ها دست یافته باشند به سرعت نابود ‌کند. ترامپ گفت «ما دقیقا می‌دانیم چه کاری می‌کنند...و هر کاری که در چهار هفته گذشته انجام داده‌اند ما آن‌ها را در یک روز از بین می‌بریم.»
رئیس جمهوری آمریکا گفت جنگ را می‌توانست «چند هفته بیشتر» ادامه دهد و ماجرا تمام می‌شد اما به درخواست چند کشور آن را متوقف کرد. ترامپ گفت جمهوری اسلامی دو گزینه دارد: «یا توافق کند و یا نابود شود.»
ترامپ همچنین درباره خارج کردن اورانیوم غنی‌شده از ایران گفت این کار را بیشتر برای «روابط عمومی» انجام خواهد داد و او احساس بهتری خواهد داشت که آن مواد از ایران خارج شود.
رئیس جمهوری آمریکا افزود «به‌دست آوردنش پروژه بزرگی است، واقعاً پروژه بزرگی است.»
او گفت: «اوایل به انجام این کار فکر می‌کردیم، اما زمان می‌برد؛ حدود یک هفته و نیم طول می‌کشید، و این مدت زیادی است که در قلمرو دشمن باشید.»
دونالد ترامپ توضیح داد که «باید این حجم عظیم گرانیت را جابه‌جا کنید. می‌دانید، آنجا گرانیت است. گرانیت سخت‌ترین سنگ است. واقعاً شگفت‌انگیز است، چون بمب‌هایی که استفاده کردیم فوق‌العاده قدرتمند بودند. و یادتان نرود که علاوه بر آن، با موشک‌های تاماهاوک هم آنجا را زدیم.»
او گفت فکر نمی‌کند خارج کردن آن مواد از ایران «لازم باشد، مگر از نظر روابط عمومی. به نظرم برای رسانه‌های جعلی مهم است که ما آن را به‌دست بیاوریم. من همان کسی بودم که گفتم آن را به‌دست خواهیم آورد، و به‌دستش هم می‌آوریم. حواسمان به آن هست.»
ترامپ اشاره کرد که با «نیروی فضایی» آمریکا که ابتکار او بود همه تحرکات در اطراف سایت‌های هسته‌ای در ایران زیر نظر آمریکا است.
او گفت «من ترجیح می‌دهم آن را به‌دست بیاوریم، اما مراقبش هستیم. دقیقاً می‌دانیم آنجا چه اتفاقی می‌افتد. چند روز پیش مردی تلاش کرد وارد آن گذرگاه شود. دیدیم دری کاملاً متلاشی شده بود. و ما از همه‌چیز خبر داریم. اگر هرگز حرکتی انجام دهند، و این را هم به آن‌ها گفته‌ام، اگر نیرویی بفرستند و ببینم کسی تلاش می‌کند، تنها کاری که می‌کنیم این است که با چند بمب دیگر آنجا را می‌زنیم و کار تمام می‌شود. آن‌ها چنین کاری نخواهند کرد.»
ترامپ گفت: «به آن‌ها گفتم ما در آن محل، در آن سه سایت، ۲۴ ساعته ۹ دوربین داریم. دقیقاً می‌دانیم چه می‌گذرد. هیچ‌کس حتی به آن نزدیک هم نشده است. در ابتدا بررسی کردند و گفتند هیچ راهی وجود ندارد که کسی بتواند به آن غبار هسته‌ای برسد. اما با این حال، من ترجیح می‌دهم آن را داشته باشیم. ترجیح می‌دهم به‌دستش بیاوریم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75471" target="_blank">📅 07:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75470">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rTW2ygwJnPndnyqUAiKwieFIB5kNvH_ealReKxd62vOyYMBPBNUyGbbSHbfhPCs9QmXDaXSdluHtRXVHgGabj-HKu2k0ETfMJyQR97oyTpE9hDHpSI3IPAoo-efdAJ3B6JTWkckYDbsuxloTWY-YCL7PmHsITeQvm2PeOXQkPPXWLrlTRqDAYSZV7H8W7-CLJceMIv3rUAYbM6aiQTYoRCtu6OxxiOdWTi1YFx3YiMBFjG2O_opEX0TfBgBR98hWwhUC5q3mKgXJX1oneFX6yTqhgTqPm7Z9Ouk09d6G7F9SPg928l7C5wEPTnt5Ck3rloTnlym7WoGB7hzO6fRHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: منظور رئیس‌جمهور چین از آمریکای در حال افول، دوران بایدن بود
ترجمه ماشین:  وقتی رئیس‌جمهور شی با ظرافت بسیار از ایالات متحده به‌عنوان کشوری که شاید در حال افول باشد یاد کرد، منظور او خسارت عظیمی بود که ما در چهار سال دوران جو بایدن خواب‌آلود و دولت بایدن متحمل شدیم؛ و از این نظر، او ۱۰۰ درصد درست می‌گفت. کشور ما با مرزهای باز، مالیات‌های بالا، تراجنسیتی‌سازی برای همه، حضور مردان در ورزش زنان، DEI، توافق‌های تجاری وحشتناک، جرم و جنایت گسترده و بسیاری چیزهای دیگر، به‌شدت آسیب دید!
رئیس‌جمهور شی به خیزش شگفت‌انگیزی اشاره نمی‌کرد که ایالات متحده در ۱۶ ماه تماشایی دولت ترامپ به جهان نشان داده است؛ از جمله رکوردهای تاریخی در بازار سهام و حساب‌های بازنشستگی 401K، پیروزی نظامی و روابط شکوفا در ونزوئلا، نابودی نظامی ایران — که ادامه خواهد داشت! — قدرتمندترین ارتش روی زمین با فاصله‌ای بسیار زیاد، تبدیل دوباره آمریکا به یک ابرقدرت اقتصادی، با سرمایه‌گذاری بی‌سابقه ۱۸ تریلیون دلاری دیگران در ایالات متحده، بهترین بازار کار تاریخ آمریکا، با شمار افرادی که اکنون در ایالات متحده کار می‌کنند بیش از هر زمان دیگری، پایان دادن به DEI ویرانگر کشور، و آن‌قدر دستاوردهای دیگر که فهرست کردن فوری آن‌ها ناممکن است. در واقع، رئیس‌جمهور شی به‌خاطر موفقیت‌های عظیم بسیار در چنین مدت کوتاهی به من تبریک گفت.
دو سال پیش، ما در واقع ملتی در حال افول بودیم. در این مورد، من کاملاً با رئیس‌جمهور شی موافقم! اما اکنون، ایالات متحده داغ‌ترین کشور در هر جای جهان است، و امیدوارم رابطه ما با چین از همیشه قوی‌تر و بهتر شود!
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/75470" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75469">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8EIzLd6FT8kyToDaWJ7tm6L2W4pCN9tjJ7t3wiPHuM1jTrAzYDpGKNJr7k4IUiVXCe6BOcvOVu7kOqRIjNdnShrY3SvGt3FvGjr-jozg-uJMzKv8ub9MF3UM-gk-TON93Qj3Z5AI4uqRoPVKypxeH7ZbZrOcmpiG5yY1E6bOr9qxwJ2_k1CWj6s78MxmMB1D7Ai9VERz1qmlLAxDPFxiBMVhLmwGWGOYS9mbW1jOx2moHJHRywbhcOKa1sOHQ6jyxV_UI2fyg0spQ902ZJM_gX77zP3WzxXgZYQQp_LCXit4FxKw0JwqXvAoBHE9Cw-NBsWKVH355PjowpNcfyB0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با سفر «دونالد ترامپ» رییس‌جمهور آمریکا به چین، رهبران ۲۶کشور دیگر نیز روز پنجشنبه ۲۴اردیبهشت۱۴۰۵ در بیانیه‌ای مشترک خواهان بازگشت وضعیت عادی دریانوردی در تنگه هرمز شدند.
این بیانیه که توسط کشورهایی مانند بریتانیا، فرانسه، بحرین، کانادا، آلمان، ژاپن، قطر و کره جنوبی امضا شده است بر «تعهد خود به استفاده از ظرفیت‌های جمعی دیپلماتیک، اقتصادی و نظامی برای حمایت از آزادی ناوبری در تنگه هرمز» تأکید کردند.
در این بیانیه آمده است: «کشتیرانی باید آزاد باشد، مطابق با مفاد کنوانسیون سازمان ملل متحد درباره حقوق دریاهاو حقوق بین‌الملل.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75469" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75468">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/On3iQDI2m8TdBYxADGZOHUut1QryLqUXtm6Vx6OCWPmrY60lnUuOuhKzEzdO-jaJ1IidTJZMaoAb1xc02mKrehsro15UdfcsGkNW3ARYOD_u4xoHUpRH9U-oWW50FOz8ib2Jzisq7RmZl6SfkfSngaQcVEwpLa8xYofRF7aJQuY6k6drBEbvfHeGerhthDuo9oIiiLv2YhqJa-CAxANvYm7kTtUCiXnpcN8rOpKnQJzSLIom3HjGFiibMjX4ZIx6qYS3nMM7icdfQeFDhK5om9Z3Rj0IWmE9_sLvQdvc6jsbp4T6lXj2hQm0150CZJInn8om55wcVtIllYs60NMcjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، اعلام کرد که صنایع موشکی، پهپادی و دریایی ایران «۹۰ درصد تضعیف شده‌اند.»
او در یک جلسه استماع در سنای آمریکا گفت: «تهدید ایران به‌طور قابل‌توجهی تضعیف شده و این کشور دیگر مانند گذشته، در هیچ حوزه‌ای، قادر به تهدید شرکای منطقه‌ای یا ایالات متحده نیست. آنها به‌شدت تضعیف شده‌اند.»
کوپر اشاره کرد که نیروهای نیابتی مسلح ایران در ۳۰ ماه پیش از جنگ اخیر، بیش از ۳۵۰ حمله علیه نیروها و دیپلمات‌های آمریکایی انجام داده بودند؛ به‌طور میانگین هر سه روز یک حمله، که در نتیجه آن چهار سرباز آمریکایی کشته شدند.
برد کوپر با دفاع از جنگ اخیر  تأکید کرد: «امروز حماس، حزب‌الله و حوثی‌ها همگی از تأمین تسلیحات و حمایت ایران قطع شده‌اند. این نتیجه از پیش تضمین‌شده نبود.»
او همچنین گفت نیروهای آمریکایی دیگر برای سرنگون کردن پهپادهای ایرانی از مهمات پیشرفته و گران‌قیمت استفاده نمی‌کنند.
ذخایر سامانه‌های دفاعی پرهزینه برای مقابله با پهپادهای ایرانی در طول جنگ خبرساز شده بود، اما فرمانده سنتکام اعلام کرد ارتش آمریکا اکنون از مهمات ارزان‌تر استفاده می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/75468" target="_blank">📅 19:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75467">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1vPZr9AWjCtgbUpbhd56cmDMwyJyjGBfh3wcFjtvOEQmFiTs-J423qXE9k-XR11-hNmqp4LqzwU0nb3RFBmvDCMjuzP6aM4bpLVj3tOXyKGxMcbH6XGMvOlgi0-sm9w6Em4N90FWlU_GvPXZu1saR29Gg5i2hMIdVj_IIn8LOyoTh3zKEwhjvvZPvmEAHSrAFYsPBr14HKAo_0vksgbD4pTfnqo6ff1NICzMUdEKTVx6viXB870kS5HJntMJIDpI5Z7X5VCaBo_C9zftMuhdt27eSdPgaUAcA9loPUUxnaxbuQxFClxiPyFhUX1nkr4gJwpg4P4irrRUHh_aZoDdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی، نماینده تهران در مجلس، نوشت جریانی «شناخته‌شده» در دولت چهاردهم که راه‌حل را «آزاد کردن و گران کردن» می‌داند، قصد دارد سهمیه بنزین هزار و ۵۰۰ تومانی و سه هزار تومانی را کاهش دهد و قیمت بنزین پنج هزار تومانی را به ۱۵ تا ۲۰ هزار تومان افزایش دهد.
او افزود همان جریان در دولت چهاردهم پیش‌تر با حذف ارز ترجیحی ۲۸ هزار و ۵۰۰ تومانی و گران کردن ارز، به گفته او، «بالاترین تورم پس از انقلاب ۵۷» را به مردم تحمیل کرده بود.
رسایی نوشت محمدباقر قالیباف با «پلمپ کردن بدون توجیه و دلیل مجلس»، راه نظارت نمایندگان بر تصمیمات دولت را بسته است. او افزود انجام تکلیف نمایندگی سخت شده، اما تلاش می‌کند مجلس را از این «مرگ تعمدی» بیرون بیاورد و جلوی این تصمیمات «عجیب» را در موقعیت «سخت و جنگی» فعلی بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/75467" target="_blank">📅 19:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75466">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOAeWzutykgTATHnppRUKi9ASaV-WI920VZuIHGQvCm7H1k-C8eMquz6rWfuMmx3wP7YuAwHOTaVE_C6nKRayAezpqMBs9pJ4SSOR6y_qIBdXB-gW6-zfXnLH-ELALum9jDXLxhHV0ip27yf5gfEDs2vMwBbSBuGzHaEMI4rMIyCrSd3m17q2VZ3_UJYtzvrLy2rV_Nlem40YXTGnnj5nrGQdZiOOis0qncJZNfw_wKxqNDLIvrO69zO_-bS7QuONVHjwCTDXAVGUCJmffWWj6rIj3QTpGWgF_zB2cYTSWjqB2S98ChYrSKZygv4DjZK7hQjEyu_LeF7m-Th7Yqa6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی پوردهقان، دبیر دوم کمیسیون صنایع و معادن مجلس گفته است که مصوبه شورای عالی امنیت ملی در مورد اینترنت پرو در اجرا به «قلکی برای همراه اول، ایرانسل و رایتل» تبدیل شده است.
او در مورد انتخاب محمدرضا عارف، به عنوان رئیس ستاد ویژه ساماندهی فضای مجازی گفت که «مجلس در این مورد چیزی نمی‌داند» و این حکم مسعود پزشکیان، رئیس‌جمهور را «تزئینی» خوانده است.
به گفته این نماینده مجلس این قبیل اقدامات بیشتر جنبه «روانی » دارد و قرار نیست که «اتفاق خاصی» در این مورد بیفتد.
آقای پوردهقان همچنین گفته است که بدتر از قطعی اینترنت، تعطیلی مجلس است و اکنون مجلس با بسیاری از وزرای دولت به لحاظ نظارتی هیچ ارتباط خاصی درمورد عملکردشان ندارد که یکی از همین موارد موضوع اینترنت است و هنوز یک جلسه ویژه نداریم که فردی بیاید و شرایط را توضیح دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/75466" target="_blank">📅 19:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75465">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIM0SFwS6UM2wjbe2Ll7Wv0H6lgTLphcAh3C0I_M9kJgOIOFiwgoR87htnptYEutevpIbQzMJ_-zdQfJnroeKqor4WeCl_HODHGcTqZaqdwRAlndE6SAjcSQKOtcf3hPurlCFfsbGXGdkPiiXCQSbw97QehOyTC8OuzGuHATpPsLVzLSYkpaku2b4jImM_Tvlo-d811IcGKCKg4rkO7wYr1Z_IT-3MJtQSnqg6-Dhlu5Tv0b2I7gFTdnhNVp_n7ZYKvERHmjQyuxBmofkpHCRoEE_xzTchJex1gBo7Ymbzck26yZeA7z-eMVZtSsGUl7UtSZJ5DfXk6Fh4pMkAX5AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل در یک سخنرانی گفت که ماموریت ارتش این کشور درباره ایران کامل نشده و برای این احتمال آماده است که شاید دوباره ناچار به اقدام شود.
یسرائیل کاتز تاکید کرد: «اگر اهداف‌مان تامین نشود، دوباره اقدام خواهیم کرد.»
پیش از این نیز ایال زمیر، رییس ستاد کل ارتش اسرائیل، گفته بود که «نبرد به پایان نرسیده و ارتش برای ازسرگیری جنگ در صورت نیاز آماده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/75465" target="_blank">📅 18:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75464">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8nisi0BQSlPOG5bRnMLW5xqHS1_EdEt4fZ-qaoMFIxQhZDzGmKkbtfPA378xImFumpkxL_QwGG4jnZYbui88jodNQukzBwOn_VIjZYIhH5cEu-aXt3pxdu9_nqW6OulAb7JHWJ7TYgXOdSVgpjaGr8y38Xm8Z751Foh60wOkuuoS2_Rz4uG69bKBAf_ulxn1opeVDW4ogfS09xHkDrGrxfwOJMJDyDC6O-7nV5hCxgsqR8shTuH0gP6E9jFzPOneDbiTEZZtm4eYZAEkXJCHwXiNncrcE15QFgjZrPFHNvCHGF7HMDcKVB-iR5wx22XAeUY_KyNxOMQh2rmAu_n0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر دارایی آمریکا، در گفت‌وگویی با شبکه سی‌ان‌بی‌سی در حاشیه سفر رئیس‌جمهور آمریکا، در یک مصاحبه از پیش ضبط‌شده گفت که معتقد است چین از نفوذش بر تهران برای بازگشایی تنگه هرمز استفاده خواهد کرد.
او گفت: «فکر می‌کنم آن‌ها (چینی‌ها) هر کاری از دستشان بربیاید انجام خواهند داد.»
آقای بسنت افزود: « بازگشایی تنگه هرمز بسیار به نفع چین است. فکر می‌کنم آن‌ها پشت پرده تلاش خواهند کرد، البته اگر اصلا کسی بتواند بر تصمیم‌های رهبری ایران تاثیر بگذارد.»
به اعتقاد وزیر دارایی آمریکا، چین به‌زودی سفارش بزرگی از هواپیماهای بوئینگ را اعلام خواهد کرد و افزود دو طرف در حال گفت‌وگو درباره بهبود روابط تجاری از جمله صادرات انرژی هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/75464" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75463">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYbQGhvAHh8FIhcQ2f7aTpPCrObCVz8EdnBJ3n7u9FKpXnLvUS9-zgZkKx2RAZRmcPcsu3bkH7zoz4c6V1KlMH2M3tboukFWN7ypprJAI73BUS0ZREDEdkwJ0r71bwfAcJPhAoLBF4aar2yM8-w_CBHDqVNehGzCfrXl0-rqJ2iagYjrVz6XJCJnB9Yur3Qv8UCKisdpLL_rLXCX8li_cX8HEDswLf76zpBy7RvKlPVDU6eiteOFg28-15utlzMFX7hmaJ5TrF25xckV-Dv1ZdncsgkFfyhPyI3wpWAS4F5nebhgmWORDOuIdHNQnB4bVsegS_jglCHq1dZB8mnJoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران می‌گویند وزیر خارجه جمهوری اسلامی در نشست بریکس در دهلی‌نو، امارات متحده عربی را به «دخالت مستقیم» در عملیات نظامی علیه کشورش متهم کرد.
این تنش یک روز پس از آن رخ داد که امارات ادعای بنیامین نتانیاهو، نخست‌وزیر اسرائیل، مبنی بر سفر به این کشور حاشیه خلیج فارس در جریان جنگ ایران را رد کرد.
خبرگزاری مهر به نقل از عراقچی نوشت: «من به خاطر حفظ وحدت، در سخنرانی‌ام در بریکس نامی از امارات نبردم. اما حقیقت این است که امارات مستقیماً در تجاوز علیه کشور من دخیل بود. وقتی حملات آغاز شد، آن‌ها حتی آن را محکوم هم نکردند.»
رسانه‌های ایرانی مشخص نکردند که نماینده امارات چه اظهاراتی در این نشست مطرح کرده بود.
بر اساس این گزارش‌ها، عراقچی همچنین گفت که «نه پایگاه‌های آمریکا و نه اتحاد با اسرائیل برای امارات امنیت به همراه نیاورده و این کشور باید در سیاست خود نسبت به ایران تجدیدنظر کند».
عراقچی پیش‌ از این نیز گفته بود: «کسانی که با اسرائیل برای ایجاد تفرقه همکاری می‌کنند، پاسخگو خواهند شد.»
رسانه‌های ایرانی همچنین درباره اینکه آیا شرکت‌کنندگان نشست وزیران خارجه بریکس در هند خواهند توانست بیانیه نهایی مشترکی صادر کنند یا نه، ابراز تردید کرده‌اند؛ زیرا اختلافات میان ایران و امارات ادامه دارد.
در همین رابطه از کاظم غریب‌آبادی، معاون وزیر خارجه ایران، نقل شده که به دلیل حضور امارات در این نشست، «مشکلات و رایزنی‌هایی» وجود داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/75463" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75462">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DB7qNx10gFZMNDJIlOH25B1qpn1LWHY18kP00tfkNvh8bLUovmVScYvUHGthM28R1l7wfX49VnzO5l60TLQ8lXSAsw_14b85iuVpia8cR89LCcfwrzUj0X3Gd7xjw3Ak0fHzK9ucvnIAkd2cr5y4rhxhDTeZxDfllEiIWRCFjIac---pdKfJBy3tDoU8DvlLTuX7kKxbh40_rENwDXgaO2sEr2gT3VU7LT3PSgr_WSyZmCDUdnzZNXBVl5ZfkTCxnnT202mQw5OAFOeAPkodIkqA8h4o4yAG8x3M-w6g4jbsxg6VqHfg6lOwlNTKPwfvFv_C0a1OB-pkNk8OsvVXOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یونهاپ، خبرگزاری دولتی کره جنوبی، روز چهارشنبه ۲۴ اردیبهشت به نقل از یکی از مقام‌های امنیتی این کشور گزارش کرد که بررسی‌های سئول نشان می‌دهد که به احتمال بسیار زیاد جمهوری اسلامی ایران مسئول حمله به کشتی باری این کشور در تنگه هرمز بوده است.
سفارت جمهوری اسلامی در سئول هفته گذشته هرگونه حمله جمهوری اسلامی به کشتی باری کره جنوبی در تنگه هرمز را رد کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/VahidOnline/75462" target="_blank">📅 18:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75461">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSMKC3WxgB5rj3gCZF60cgr-4l7GNgC4ODC8p_G60ZQbstg4B96adMhl2G4ao8VVnGJy-YdeiBLw3Bd2B71Ac35XR7vWMfAyr6iP8jkwja9bfDV34obNYw8OBDYzzfeyrsJqQSfPygHvYy5yuHr_l-61C7234zKbkXqALyDJrfT08n-SuRO8a1MTIcI21YC86fR03QGbbNE6hHo4cEylWZERQjPpJcO6t74JYHtrW-qcJbSnNYotkiisBHG2Mv3v0lpWIzN7S6upNZIMkqQ8h0gb4XYOqQXFg4eoNy0ME6gQgqST25NhKadvt9Esg2cmZX0oSBUkMvbT0k0fecSp0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا روز پنجشنبه ۲۴ اردیبهشت اعلام کرد پس از وقوع حادثه‌ای دریایی در شمال شرقی امارات متحده عربی، «افراد غیرمجاز» کنترل یک کشتی در لنگرگاه را به دست گرفته‌اند و این کشتی اکنون به سوی آب‌های سرزمینی ایران در حرکت است.
این نهاد گفت گزارشی دربارهٔ حادثه دریایی در ۳۸ مایل دریایی (حدود ۷۰ کیلومتری) شمال شرقی بندر فجیره امارات متحده عربی دریافت کرده و پس از آن، کشتی به تصرف درآمده و مسیر آن به سوی آب‌های سرزمینی ایران تغییر داده شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/75461" target="_blank">📅 18:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75460">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgZa847v-bldSfRFnqpKHHzlpgqaTJNhUSH5Vm_JiZgwHL5jzIE7pdPLqbo8O8Z5SoUS30mpTKH5ZxvwMLDYIbk8bApBpPh_6ilFP54_8aCjSeHhJkrCS1sS4LA0Kct8hXbqyNrMs_tOh_Eu8xl4f_Qrx5dxblC2J2Cmn4WshWM1wqyBPb7Ue0qmF_uzUC9rrZhj1IN-pgJfVJ-u9H_pYC5lI8s5hqyz6iTLYPSGCgdrvM29EbZ16PVRUYmNn75FDD9lIyahCNNNqtu4E-OgFU6ep8LgeO0d3epetRKoxRx5q8Jz6TRWQpfBCD-MV_W0YRW3kcNSsI9ouXCyomWQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید اعلام کرد که دونالد ترامپ و شی جین‌پینگ، در پکن توافق کردند که ایران هرگز نباید به سلاح هسته‌ای دست پیدا کند و تنگه هرمز باید باز بماند.
آمریکا این گفت‌وگوی دو ساعته را «خوب» توصیف کرده و می‌گوید که دو رهبر در حال تلاش برای تقویت همکاری‌های اقتصادی هستند.
در بیانیه کاخ سفید، رئیس‌جمهور شی همچنین «علاقه‌مندی خود را» برای خرید بیشتر نفت آمریکا ابراز کرد تا وابستگی چین به تنگه هرمز را کاهش دهد.
همچنین گفته شد که مدیران برخی از بزرگ‌ترین شرکت‌های آمریکایی هم در بخشی از این دیدار حضور داشتند.
آن‌ها همچنین درباره اهمیت پایان دادن به ورود مواد اولیه برای ساخت ماده مخدر فنتانیل به آمریکا هم صحبت کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/75460" target="_blank">📅 18:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75459">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgxUoJ_666xKQJHN-O8iY1p3_tcWkUp6pcEBKI_t0BVJFy8HqWe9IHGY3VLipK9UY5wDarkCMbDqIG8nvwlNnsWO3KjAOhCDi0ovjSRanH4t5hmxED1Ed9BpUOyLZufNc9EkLtKknjaMJofjm8Rzoh18rraX0HbcZvwOGKZsqB8Z2C0imVV5xfC0ZiZ054kuBvDdl8Vj8h6g6SBbEmcchN577VEg2ADvsO2futXOS0urkTjoRfBvYJw-0WbQAHSTAOgUIho5LoOX4KWZW-uNQWyMpSlipot0mbhnT9ux1LHKQb4_iOva1abQrr881c7ZLZobI3Rd89wwpTvc_o0MfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، می‌گوید به نفع چین است که حکومت ایران را برای باز کردن تنگه هرمز تحت فشار بگذارد.
براساس گزارشی که فاکس‌نیوز از اظهارات روبیو در راه سفر به چین پخش کرد، او گفت: «ما این استدلال را با چینی‌ها مطرح کرده‌ایم و امیدوارم قانع‌کننده باشد. آن‌ها اواخر این هفته در سازمان ملل فرصت خواهند داشت دربارهٔ این موضوع اقدامی انجام دهند؛ زمانی که قطعنامه‌ای برای محکوم کردن اقدامات ایران در ارتباط با تنگه‌ها مطرح می‌شود.»
روبیو گفت حکومت ایران در حال ایجاد ظرفیتی بوده که بتواند با «انبوهی از موشک‌ها و پهپادها» سامانه‌های دفاعی کشورهای منطقه را از کار بیندازد و هرگونه حملهٔ احتمالی به برنامه هسته‌ای خود را با تهدید به وارد کردن خسارت گسترده به کشورهای خلیج فارس پاسخ دهد.
مارکو روبیو همچنین با اشاره به بحران تنگه هرمز، گفت این وضعیت بیش از هر کشور دیگری به زیان چین است و پکن باید ایران را برای عقب‌نشینی از اقداماتش تحت فشار بگذارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/VahidOnline/75459" target="_blank">📅 18:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75457">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oqSDo6ZQv55X-9RimFJmbk_BesbmsBhRC5Bqyz25WqSsOu7XbSlU9B_WMzhjTpcrS2529A-m89oZxVUtE8fNDxsekfwHhSHEoEWWuWSvBIAg8BHmXW1eSJXCGJ3VX3UHkDST7Aydpoe1Zm7TGE6DcW4NXh7Gj3WSggZrRkaUaA3oPHswCRd1RV_1z6CCtvhDOILCUQ4i9P8OXg0IYat_979Y9iVWJiricPi6e9zd4vTukGT3x_UPM8ThuyZcFOESKlGWyGJ6KVglmy3vFtlZXLCw7GekFR7JRrhb8pOr3aTQjMEE_ejzhrrPWrLyQE0AcT9kaDRQKvPr-Pfyy97NXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ks1mc6lfx653Dd4Srfpc1o0Wdap9qadebMkXOo5RFF1PZzy8nWoPSqwpzH3-zymj2moPprMKdjrr3RtTFbcNVwUqmMlalgYPwWbPlUltIOu5yi749xunBGruXIYRTt3JQqhojXA554XY_0YmXwv3PIF0QgtPQfg4Fxk0IJp80rcN_UsIzFB92tzDydAd0WnyocHyN-CG43DAPZENuf_8lvBgB3znnUiR3_BEwIbbyh6atRyw8WolOFnUP8REAzh2PTRBb65tuG69W6bndeICx9cNi2Qh0Iw7R3xFrt7Xdle8ee3HZgsJqVC5uFqS-Am9JQa9gsZxnm6kH50JUW2_sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نت‌بلاکس، نهاد بین‌المللی پایش اینترنت، نوشت که پس از بیش از ۱۸۰۰ ساعت قطعی اینترنت در ایران، نظامی طبقاتی توسط جمهوری اسلامی برای دسترسی ایجاد شده است.
😋
💩
همزمان مهدی طباطبایی، معاون ارتباطات و اطلاع‌رسانی دفتر مسعود پزشکیان، ادعا کرده است که اگر همه‌پرسی برگزار شود، مردم در شرایط جنگی، امنیت را به سهولت دسترسی به اینترنت ترجیح خواهند داد.
@
VahidHeadline
روزنامه اعتماد گزارش داد که نخستین نشست «ستاد ویژه ساماندهی و راهبری فضای مجازی» هفته آینده به ریاست محمدرضا عارف برگزار خواهد شد.
هدف اصلی این ستاد، فراهم کردن زمینه‌های لازم برای رفع محدودیت‌های فضای مجازی است تا حداکثر تا میانه خردادماه، امکان اتصال مجدد شهروندان به اینترنت بین‌المللی فراهم شود.
عارف در این مسیر قصد دارد از ظرفیت نخبگان و اساتید برجسته ارتباطات نظیر هادی خانیکی و علی ربیعی [
🤨
] استفاده کرده و میان نهادهای حاکمیتی برای بازگشت سرویس‌دهی هم‌افزایی ایجاد کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/VahidOnline/75457" target="_blank">📅 18:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75456">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsUS1uyIcGVzcvMxDU7uz4Gcy4OumAEomrYhmgMy4PZES4eWA4P4nOEss4oLJtBq9kQ_w9qv4ikBrr2gG9qG8bIDu9e4qsm2FnRlFCJzJzyo4a2gImjL6i3f7XQD3VVY_-hKudu7-4X_LXatJgJ5haO-_GGqublVrd6lT9lLLcxFni565toR_MFTz1_q_ME0an2m44ALfv3mNCrlBE3I4coDc5Ka6odJxG-VZsJs05PpZW29mqSBosKxeSVeNT2oFt4BzI-8ZszILNdki_jmJRvPlD0fcKD0Qd-9PZQjJ3565uwZnd175MpCL9riERUO8cVud01qqdfPhT6x5rF6Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی شفاخواه، فعال حوزه آموزش و حمایت از کودکان کار و ساکنان مناطق محروم، توسط نیروهای وزارت اطلاعات جمهوری اسلامی بازداشت شد.
این فعال حوزه کودکان عصر سه‌شنبه ۲۲ اردیبهشت ۱۴۰۵، ماموران وزارت اطلاعات بازداشت و به مکان نامعلومی منتقل شد. همچنین تمامی وسایل الکترونیکی و ارتباطی او و همسرش نیز توقیف شده است.
@
VahidHeadline
هنوز از دلایل بازداشت، اتهامات انتسابی و محل دقیق نگهداری شفاخواه هیچ اطلاع دقیقی در دسترس نیست و پیگیری‌های خانواده او برای کسب اطلاع از وضعیت سلامت او بی‌نتیجه مانده است.
مهدی شفاخواه طی سال‌های اخیر به صورت داوطلبانه در مناطق محروم و حاشیه‌نشین فعالیت داشته و از طریق آموزش ورزش و مهارت‌های اجتماعی به کودکان کار و نوجوانان آسیب‌پذیر، در راستای کاهش آسیب‌های اجتماعی از جمله اعتیاد و بزهکاری تلاش می‌کرد.
او برادر رضا شفاخواه، وکیل دادگستری و فعال حقوق کودکان و زندانیان سیاسی، است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75456" target="_blank">📅 18:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75455">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6ed3795eb9.mp4?token=N4dlms4wKdjda_Nm9iyC-WtVK7YWFCHcFxGDU7xlJDjGoDJiCUIcVuKqQK63AUo2Gh_JzdLTqHFA88l8mJ2BCX2JjGDkb0jT4_8y66wWLhnieif39I7h0OGwJTxRQsBQlFKi53mIPKjIkOsRopFix4jBULeeDiWQ227knsmu1s8JI83bBBbq1r-TimnYhbS0XrKa1eGL45zYAAiBPyly6wu21fbti26FFcmdt_d5UfFYX7VoprJPSqW3wAMCvdTemtU8ETQZ4qMKBVQWOl_-jRMxp43YN95MJYRkqBhOfXXM0P_axGZgCHfm7kSOUyXJKL8KzGGfLZzoQ9ZQn-0-Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6ed3795eb9.mp4?token=N4dlms4wKdjda_Nm9iyC-WtVK7YWFCHcFxGDU7xlJDjGoDJiCUIcVuKqQK63AUo2Gh_JzdLTqHFA88l8mJ2BCX2JjGDkb0jT4_8y66wWLhnieif39I7h0OGwJTxRQsBQlFKi53mIPKjIkOsRopFix4jBULeeDiWQ227knsmu1s8JI83bBBbq1r-TimnYhbS0XrKa1eGL45zYAAiBPyly6wu21fbti26FFcmdt_d5UfFYX7VoprJPSqW3wAMCvdTemtU8ETQZ4qMKBVQWOl_-jRMxp43YN95MJYRkqBhOfXXM0P_axGZgCHfm7kSOUyXJKL8KzGGfLZzoQ9ZQn-0-Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر پرچم حزب‌الله را در ویدیوی مربوط به بدرقه فوتبالیست‌ها سانسور کرد.
FattahiFarzad
دیده شدن پرچم حزب‌الله تو اینستاگرام مساوی با پاک شدن ویدئوست و ممکنه حتی اکانتشون هم بن بشه.
Sam1Kia
اعضای تیم فوتبال چهارشنبه‌شب ۲۳ اردیبهشت‌ماه در میدان انقلاب تهران برای حضور در جام جهانی ۲۰۲۶ بدرقه شدند؛ رقابت‌هایی که خرداد و تیر ۱۴۰۵ به میزبانی مشترک آمریکا، مکزیک و کانادا برگزار خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75455" target="_blank">📅 07:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75454">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LexdyrBRppK9I2VPeDSWdDTXvmZ99U3vpqYj02-zXrmzygL5lm9YWZogHLaD6twowBFVpZQATwFsCNYFCZHQJJdgoccOMNQKnetykZh6oZWBArtsGhz7AbY79Pn3w0oiRkCX7tHlx9lCJfSbsbofgCbN4tFPVFcHAaYMuwm5MCHai_QoUwcrbthj-TzCvjtdpjAx4Dnu2-SoE_N75-inQRDhZIVKdhspoxg_R7kkGhc2XQjb6uxf8WNrIxb0BmacqPeEuykzelhq6-KGHWpkiEksunuEEHU_Vd0m9YWD1Gn43FtvSSWJda8JufpBQWcoWHEgSj3W-sVxG57yI7G73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه امارات متحده عربی اعلام کرد گزارش‌های منتشرشده درباره سفر بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به این کشور صحت ندارد.
پیش‌تر دفتر نخست‌وزیری اسرائیل اعلام کرد بنیامین نتانیاهو در جریان جنگ آمریکا و اسرائیل با جمهوری اسلامی، به‌طور مخفیانه به امارات متحده عربی سفر کرده و در این سفر با محمد بن زاید آل نهیان، رییس امارات متحده عربی، دیدار کرد.
وزارت خارجه امارات متحده عربی اعلام کرد روابط این کشور با اسرائیل علنی است و در چارچوب توافق‌نامه‌های ابراهیم که به‌طور عمومی اعلام شده‌اند، برقرار شده است.
وزارت خارجه امارات متحده عربی افزود این روابط مبتنی بر محرمانگی نیست و هرگونه ادعا درباره سفرها یا ترتیبات اعلام‌نشده «بی‌اساس» است، مگر آن‌که به‌صورت رسمی از سوی امارات متحده عربی اعلام شود.
عباس عراقچی در واکنش به سفر نتانیاهو به امارات متحده عربی در زمان جنگ، نوشت: همکاری با اسرائیل در این مسیر غیرقابل بخشش است. افرادی که برای ایجاد اختلاف با اسرائیل همکاری می‌کنند، پاسخگو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75454" target="_blank">📅 00:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75453">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B90i4LhMWkV8cIF_o2ehlheJS-lij5T7OWLj15wU_--jrVmmapZM8ryxqyDnckn_JjWOCyC3dqFYOWqkBhidlt2F0R6EpPzX2JhvFL1qIkAcV7bI46ayJR5ozWyhAlLwweZVserJ6vIdNT4Z0nBX1nFLxSZhnv_BhgPYTUBxK2vJO8VCRQPru1lW_ic3RCa5LN-z5Pb70PZVuUfPJf2RNaR4Rn_BsCAdkANticK6qUt5nKxQOZE0bDWTMfT6V--daTMc6hw1j0l_RIrXkf4uxxP1elMPWxhZ0WJDLWOwy8PHaYIiH0YCdqpqfhgqTVhHFJcCnHQfsQ8iDTkDwu12aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، اعلام کرد که واشینگتن معتقد است در مذاکرات با ایران «پیشرفت» حاصل شده، اما هنوز مشخص نیست این پیشرفت برای عبور از خط قرمز دونالد ترامپ کافی باشد یا نه.
آقای ونس روز چهارشنبه در کاخ سفید به خبرنگاران گفت صبح همان روز با جرد کوشنر و استیو ویتکاف درباره ایران گفت‌وگو کرده و همچنین با مقام‌های عرب در تماس بوده است. او افزود: «سوال اصلی این است که آیا این پیشرفت به اندازه‌ای هست که خط قرمز رئیس‌جمهور را تأمین کند یا نه.»
به گفته معاون رئیس‌جمهور آمریکا، خط قرمز ترامپ این است که ایالات متحده مطمئن شود «سازوکارهای کافی» ایجاد شده تا ایران هرگز به سلاح هسته‌ای دست پیدا نکند.
اظهارات ونس در حالی مطرح می‌شود که ترامپ پیش‌تر پیشنهاد تازه ایران در مذاکرات را «غیرقابل قبول» توصیف کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/75453" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75452">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KWWB_-GltQCclt2htFPhBwtPmE9unscaUxTAHpTPWVW0UmjfLLc7ZujBWC0X41C4ettba0CvzV2u21WeuWA_76pJTwhJ9gYDfY60PGhKkzCQeBRwpNftxaOklA6857aksMAAwf033y7mWfmGgzzO2au4F_AaR-05StWfDh-lD4qnNlHSH0jzUO04KPkOrEdmxdRHMQZbLYj5MKXyLrSoJUXEJNP2O5H0bSYFPbbznhRrpKB_ZiUthZVCx2E4jhGTiiIppbV_qW-kbsjTtrvjyK03WqgYuvIt9gHx0XwLCk2W2d7E81L1emwNCxB6wN2ez9l8AADHRpsmObrJAIulOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی شامگاه چهارشنبه ۲۳ اردیبهشت اعلام کرد که محمد عباسی، یکی از بازداشت‌شدگان اعتراضات دی‌ماه سال گذشته به اتهام قتل یک مأمور امنیتی اعدام شده است.
خبرگزاری میزان، وابسته به این قوه، گفته است که او بعد از تأیید حکم توسط دیوان‌عالی کشور و با توجه به «تقاضای اولیا‌ء دم»، «قصاص» شد.
ساعتی پیش‌تر، پایگاه خبری هرانا به نقل از یک منبع نزدیک به خانواده این زندانی نوشت که مسئولان زندان قزلحصار از خانواده محمد عباسی خواستند که برای ملاقات با او به زندان مراجعه کنند، «اما پس از حضور خانواده در زندان، این امکان از نزدیکان او سلب شد. پس از خروج خانواده عباسی از زندان، آنها در تماسی تلفنی از اجرای حکم اعدام محمد عباسی مطلع شدند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/75452" target="_blank">📅 22:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75451">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WUh67MDH2U2_hytgvsvBKhORtr199Ti726C7TTFS5K109PoCGrsMMy4UbgtjTWvdzxzsdtNfAOUXSm1f3xKEHkwdKkjpgVmaKcRuFkKGmRaKII0yjWk0VGQqO1Et0WCNebH3LwBJe01XbR7nOl9mDNMiuP_v5rmpJcbsUxAt8blxMnX7Rt8pgtjj7e43x1PYmKp_LJkGwJ78A6IIQ9oUM6igsWBOC1uDAyXfIPPdMLdewwsmTcSMF3RquYpUcRfCeCVvkzjog9lb9TiMy2fEXToTOCWY89I9rD_w1085kBDU9H4Ltqd4EA9v3tXp1Wxv47ARBkJvZmEnOql4lBox3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر نخست‌وزیر اسرائیل روز چهارشنبه اعلام کرد که بنیامین نتانیاهو در جریان جنگ آمریکا و اسرائیل با ایران، به‌طور «محرمانه» به امارات متحده عربی سفر کرده بود.
در این بیانیه آمده که نتانیاهو با شیخ محمد بن زاید، رئیس امارات متحده عربی، دیدار کرد.
دفتر نخست‌وزیر اسرائیل گفت: «این سفر به یک پیشرفت تاریخی در روابط میان اسرائیل و امارات متحده عربی منجر شد.»
پیش‌تر مقام‌های ارشد آمریکایی تأیید کردند که اسرائیل در جریان جنگ با ایران، یک سامانه پدافندی «گنبد آهنین» به همراه نیروهایی برای بهره‌برداری از آن به امارات اعزام کرده است.
همچنین به گفته مقام‌های عرب و یک منبع آگاه که با روزنامه وال‌استریت جورنال گفت‌وگو کردند، دیوید بارنئا، رئیس موساد، دست‌کم دو بار در طول جنگ با ایران به امارات سفر کرد تا دربارهٔ هماهنگی‌های مربوط به این درگیری رایزنی کند.
@
VahidHeadline
آپدیت:
امارات تکذیب کرد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/75451" target="_blank">📅 21:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75449">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPii8W3rF6Ej5UjVK0l0AGmli4-RB-b_Vmk24ttqao62LKGh6xvZp4k54dCO70Hg8oX1P1DCtoq_zPJb_7us1ax4jrh3P3SMqxnoke2IzjMFM_o4fn9qVRt3QG2LZOsd9I6qum0i89UXJg6nkS8MHwu56Qz7cTGbPoKgVsdgUEp4se4kAGiiYLd8dVmKXdO0ecgWGo9d4OHnuDXaQ8cgIQlYuMmY8JrRPh3gCX0mJa3P35GoCWu5oucv85yZjjeL3MtDbNHu9t0iYTiWyrMBjHumKsZQ5ZiWjoYvmFqPYW7tEjff3f4jfo0ogjyEGRDW1BlaigrfuVO1UHaMmMZJnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی ایالات متحده روز چهارشنبه ۲۳ اردیبهشت با تاکید بر ادامه محاصره دریایی بنادر ایران اعلام کرد که از زمان آغاز این عملیات، به ۱۵ کشتی حامل کمک‌های بشردوستانه اجازه عبور داده شده است.
سنتکام در پیامی در شبکه ایکس نوشت که نیروهای آمریکایی طی چهار هفته گذشته ۶۷ کشتی تجاری را وادار به تغییر مسیر کرده و چهار شناور را نیز برای اجرای محاصره «از کار انداخته‌اند».
این فرماندهی همچنین اعلام کرد اوایل هفته جاری، دو کشتی تجاری دیگر پس از تماس رادیویی و شلیک تیر هشدار از سوی نیروهای آمریکایی مسیر خود را تغییر داده و از ادامه حرکت به سمت بنادر ایران منصرف شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/75449" target="_blank">📅 19:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75448">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/928f9dddaa.mp4?token=uEdQNPeiVDIbK_4u480sIgFTLyarwKZsab5T4wA2d_tInNtXQWIPQCeidf1TvDv0PJjwx49hCKNjsSeGy295vqzesDTZoUS8lPQ6Zg5379lbMIeFqqgKzi5boyspBPdtn70_dMy0B8Vfo4zU4gd1RlI0vxiF9yeIijhq32Jl06pgxlwshhq4ECdA-2rAJ2Y9mIF7QrgfB4hyFt8LrUvbj4do1hpBVGRCEZb0BTwzbu2ox6_naji0YCfKpg8sML8tm4ElVv9q4P-We9AV82jyepKT2adXeP_TVTc7BRvD9ETY6enlBqBU81415B8Qs-Qu16j9olBDTJCLZqQUyc3Gow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/928f9dddaa.mp4?token=uEdQNPeiVDIbK_4u480sIgFTLyarwKZsab5T4wA2d_tInNtXQWIPQCeidf1TvDv0PJjwx49hCKNjsSeGy295vqzesDTZoUS8lPQ6Zg5379lbMIeFqqgKzi5boyspBPdtn70_dMy0B8Vfo4zU4gd1RlI0vxiF9yeIijhq32Jl06pgxlwshhq4ECdA-2rAJ2Y9mIF7QrgfB4hyFt8LrUvbj4do1hpBVGRCEZb0BTwzbu2ox6_naji0YCfKpg8sML8tm4ElVv9q4P-We9AV82jyepKT2adXeP_TVTc7BRvD9ETY6enlBqBU81415B8Qs-Qu16j9olBDTJCLZqQUyc3Gow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ‌های ملی‌پوشان فوتبال در صداوسیما درباره میزان تحصیلات دانشگاهی‌شان جنجالی شد.
در این گفتگو، یکی از ملی‌پوشان در پاسخ به سوال مجری که پرسیده بود «در کدام دانشگاه درس می‌خوانی؟» گفت: «نمی‌دانم، الان حضور ذهن ندارم».
در دوره قبلی جام جهانی نیز انتشار ویدیویی از دروازه‌بان تیم ملی فوتبال ایران که گفته بود «من دکترا دارم»، بحث‌برانگیز شده بود؛ دکترایی که بعدها مشخص شد به‌صورت غیرحضوری در رشته تربیت بدنی دانشگاه پیام نور اخذ شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75448" target="_blank">📅 18:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75447">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVwSJN88NzknL9m2qVHoy9qsYoeV7LptqSepf0cL6-SjncD_s19s3ZnN4VzXiuGaLxMhMDBoQZQPR_QVgCM3n7lAP9Ip8PoAm2ujzpaMOUYEkkFa_wOGQveBklsSXtU0JBV4VMGnAooaAgSXNkGCaINT9VfTAb70SSa6SGrWBsqEAeZ4VT2du1-auNo9VpVuVqb_G55qOdlMb4crVmDAS9AoT1lHNSpSaD63z97O_eAZ3beV8dFqaMUe9sx2kOrKyaeVEyguFlGMEY8ZRz2-cITj3P8pm5ZaIA0xVMehTTmFJPES5VoSe6w7duSOScy7YAGHo15OQr5LW5s_sl7a7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز به نقل از دو مقام غربی و دو مقام ایرانی گزارش داد عربستان سعودی در جریان جنگ خاورمیانه، در پاسخ به حملاتی که در خاک این کشور انجام شده بود، چندین حمله اعلام‌نشده در ایران انجام داده است.
به گفته دو مقام غربی، این حملات توسط نیروی هوایی عربستان سعودی و در اواخر ماه مارس انجام شده‌اند. یکی از این مقامات گفت این حملات «اقداماتی تلافی‌جویانه در پاسخ به حملاتی بود که عربستان سعودی هدف آن قرار گرفته بود»
رویترز با اشاره به گزارش‌های پیشین درباره حملات امارات متحده عربی به ایران نوشت اقدامات عربستان سعودی و امارات متحده نشان می‌دهد کشورهای عربی خلیج فارس که هدف حملات جمهوری اسلامی قرار گرفته‌اند، به‌تدریج وارد فاز پاسخ‌گویی مستقیم شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/75447" target="_blank">📅 18:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75446">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqmyRApwyqkb2xUrDrN2Cq66NcKBBdVT4JiAxgOllmVaD9hiYfBdnbgLw0Mhu3IBQDHVLWMm2cA427PBOpCVdS7rKrdvDkTJMtIUnhkN6ucHK-crJCrO_1yBICPd-SuLaZKQSRF7vsDL7BHcWs3LbNcskJ6uXJCmtDIvw2dHMn3hCIRLUcpNVKqLCBF4BbOIOsuFIDUMWMALvBGzIF3UjKsy5xAUAnIhn31HGVHkdQGEQ1hQpLYU2WwwXra-ff9UmZeUiMkhyjqYHtmunN5LKdh_zD8-XWgpX0CeLfsbYfZHTj1pcPctMs5VGzYm72Bag_kqBliO2zWWeNo9g4VAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کمیسیون مستقل اسرائیلی جزئیات تکان‌دهنده‌ای از خشونت جنسی «سیستماتیک و گسترده» توسط حماس و سایر گروه‌های مسلح فلسطینی در جریان حملات ۷ اکتبر ۲۰۲۳ و علیه گروگان‌ها منتشر کرده است.
گزارش ۳۰۰ صفحه‌ای این کمیسیون نتیجه‌گیری می‌کند که تجاوز و شکنجه جنسی «با هدف به حداکثر رساندن درد و رنج» انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/75446" target="_blank">📅 17:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75445">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gq9Titl9rwPKR2hY4OkrG5I8X0lE2DLAcvJJQG3yUqdEIG3rXCVtjLXwt4D7Z_C-adJ1JmKiFGImY6ls5NXjzTrZnJBviU7eNyhZpzArb37WAMoI12FjUh7je22Qi5nNnUK353f5xsR8XAhf_1K3aW3nV-1hrj6cB56qLgkTHTPNiNwLWHBBMcXqCdPidBZ8HaJGpRXGZVFzCfWpc_TfJI89sevh1XbcywrpSCGe7YSUwfqL3uLkqoM7EddBWofEqQ09eN_DW6d1sasjpSv8DstRSydhPF3lBGLgu6oXApuH9qjDN7_6pXQpKS7_ZJA4q6DVK9QzdFd3zWqQPKvLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، محمدرضا عارف، معاون اول خود، را به ریاست «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» منصوب کرد.
در حکم آقای پزشکیان بر «حکمرانی یکپارچه» در فضای مجازی، پایان دادن به «چندصدایی» و جلوگیری از «موازی‌کاری» میان نهادهای مسئول تأکید شده است.
این انتصاب در حالی انجام می‌شود که امروز هفتاد و پنجمین روز اختلال و محدودیت گسترده اینترنت در ایران است.
حکومت ایران از ۹ اسفند (۲۸ فوریه) و همزمان با حملات اسرائیل و آمریکا، دسترسی به اینترنت بین‌الملل را قطع کرد و تماس‌ تلفنی با خارج از ایران هم با اختلال جدی رو‌به‌رو است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75445" target="_blank">📅 17:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75444">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dWkF5WPC0UzQ5sN0VjxLGjE-WAj9Vwe5vLEKOTUPiV_Efye0YWoDgL_gYXCmRPvEzy6bW2nbjqPUt2FId5IwCCXlU93lwBCIGr1ymNZCahKgN3kPkmiI-RQbff2PnlyzpLSSc2Iihxo_1Cqq2cwSj1LL1MUWGQqZ8U1n_1UkZwIXVLI_bcyDS272MQZSBiKjFeRK08N6irIxIZnQFyZ0LXk0zUZ1mSxs2Px43Um7Fg9dwIeYD6pJ8blQfdQRwhVrh_cqtBZ3H1xKf7td734Yl8nG2NCIkYNlQv3SqTbfcSZxXLHmIaY1-s8g3eycXaKGQSuIQpoFiRU8Hqg9IXQsEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، مهدی زارع، زلزله‌شناس و استاد پژوهشگاه بین‌المللی زلزله‌شناسی و مهندسی زلزله با اشاره به زمین‌لرزه به بزرگی ۷.۱ در قرن نوزدهم در گسل شرق تهران گفت: «وقوع زلزله‌های ۴ ریشتری اخیر در ۲۸ فروردین و ۲۲ اردیبهشت در پردیس نشان از تخلیه انرژی دارد. وقوع زمین‌لرزه‌های کوچک به صورت مستمر، بخشی از انرژی گسل را تخلیه می‌کند، ولی این لرزه‌ها می‌توانند نشانه‌ای از ناپایداری در پهنه‌ای وسیع‌تر باشند که مقدمه رویداد بزرگتری است.
به عبارت دیگر، لرزه‌های خرد و متوسط، هرچند تا حدی تنش را کاهش می‌دهند، اما نمی‌توانند به طور قطع احتمال وقوع یک زلزله بزرگ را منتفی کنند. در برخی موارد، چنین توالی‌هایی می‌توانند پیش‌لرزه (foreshock) باشند.»
@
VahidOOnLine
امروز پیام‌هایی از پس‌لرزه یا پیش‌لرزه ساعت ۱۲:۳۳ دریافت کرده بودم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/75444" target="_blank">📅 17:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75443">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utkVHNklmu6M-G6KjtAVQn93pnqCmjBGY2o7YKAbmKtjm8Z0KZ8IG-D3hj8y8dlud3N4FutT_MUqNHEN58oylD7-Sq8tcqufHIRj6LMOkqXPB-Hrwgbo_bA7rN8edCmIddDlCoa1gMHptOFYXbjVAPeJ6OIOtoMAnQN-jlDUczapescacRDnP5sR8tlOz3AI9k4Fppun6Qf-F3YGvE17mW17P5VnovRNpHMOUm99IoEBYppVXa4xxwv8ISZHof4UPzQgwa0EMX_lGEB_A778rW6yYx5MdEb9laJab3XNLjxiOt6LVXJ40uBLrZCTt8OcieSEmlO75Szg2kvZ9DhTMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احسان شیرخانی، شهروند ۳۵ ساله اهل شهرستان ملکان در استان آذربایجان شرقی، بامداد روز سه‌شنبه ۲۲ اردیبهشت ۱۴۰۵، با شلیک مستقیم نیروهای بسیج در ایست بازرسی شهرستان بناب جان خود را از دست داد.
بر اساس گزارش رسیده به ایران‌وایر، نیروهای مستقر در ایست بازرسی بسیج شهرستان بناب، خودروی این شهروند را به بهانه «عدم توجه به دستور ایست» هدف تیراندازی مستقیم قرار داده‌اند.
یک منبع مطلع در این‌باره به ایران‌وایر گفت که نیروهای بسیج بدون رعایت قانون به‌کارگیری سلاح و بدون شلیک تیر هوایی، مستقیما به سمت اتاق خودرو تیراندازی کرده‌اند. به گفته این منبع، چهار گلوله به احسان شیرخانی اصابت کرده و او در دم جان باخته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75443" target="_blank">📅 17:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75439">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gr6BG-HTNZD6wwQyE7fuayrDJFdENBVFkP_Goc3zsgrLcKb5n4o0_eEM3KbmJgK2SIoRo_mdRbPBpTIGmMzVGMWvvhgHbliMFWjOhUJEkrF6OK1T5FWj08-aD-wZhYmeZ3u31LuTrDcr-w8Pzv2taDlHTGpYYYLk7DiEYQhfjLPPCsZKed803wGqDOC4d7bas5oDdH56Xf-b-smaCZdqw58uvZly-3CUoul4V8xz9WCzUR0KbMUmwU4SF1EnTr1wdFJSO9kn3HXayv1OgggVvZswYnETaUZP-O8WEvkGfV3YoleACmjI4a4yZNPT9ex1BNjq7Orw5vdxBCrPhXI-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YQjYYQmHaEz8v6jN2jFbnoFOvPK74C5x8dxl9zOMzGUkXBSpi9sxNkilqhC1oKbmfpd563VoEntIilCw3-0RFCcOzbO1OjQX_0uOX59JoBKZKl4ffinUTtiXxtn9tsCqrA6Yg_I3Z8MX2iOTbVosNtqG4rIr0Z9yWFHnLydRsJJC6smurXi1TCCcBT6r6F8TWhb1F7_i5emvAlMIOnjJT4cPRm4-zvYOHgwoKzu0rhzlfRH49-c9PtiJ68D0gimKQg7qups3sFu17JRHNRWyGdg8QP2JiK60xma253EQrOmUzOMvVawXzq8KkN6xQnxfmzzE5JI3C4ntrOZBtJh75w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O0Y3SPDF9K-uNIyzXu0teBy_sfFmJL125Pmrb46TWmVWOxKJ3avejE1QNjWKb9zCDt6Y77Yw2QNdyhJhDwd0Mbj79j8jh80K1pnEijFQRAHRo74lB3QJXMGHaJbPJzyl2JWlBg6Qk4iPJpQk-EQWFwH0V2nsAjKLYBJ8qMUnc45DB1xLsQYWB6Vq2VJa8pHkXfEj4Ebs3eodkZUmJEKJcgJzo3TnbwDhjnOfEaw4l_It_f20BmU6cCUS8exPb_AIUpq6XN-6qQuUO_zAHMfojyBnUvmnhkzpaXdZ7e5-laVhxGw_rRJ41HnxBkDWuzDNwN0RuOdNjzvVe_tHXXZJeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O6WidkAvkXmSSFpyHmFhOJSYZpVVDzgsVr_wDV_1h_0PoQCLdtHa9Fs6JppkxLb3uNyemgiM8CZfb4c9NP-EPhaWJYjIEXpvSTpWynklNo9fC32aHLa6kMt8uahMTiWvPcwhx_bh1BHD_AETAk-intgRm75nJGpUmyu_AGLraK60zT-rzaKCjXXZwPldPCDNMa4TzHaQVE72H5a9svv-KEw6N1k6tJe7zUVA-2Qo80OAF4TDJnivu315MhIOiW_g2L71_xbCr8vjNraEpQhMB4ME4cEGbthkeDub03WXk2wiYD_MqxXzl768-LAodflVWoEsW9GE9lyo4wkrH7fo3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قوه قضائیه ایران یک زندانی دیگر به نام احسان افرشته را به اتهام «جاسوسی» برای اسرائیل اعدام کرد.
میزان‌نیوز نوشته که افراشته که «در نپال توسط موساد آموزش دیده بود و اطلاعات حساس کشور را به اسرائیل می‌فروخت»، بامداد چهارشنبه ۲۳ اردیبهشت اعدام شد.
در بخشی از گزارش بدون اشاره به جزئیات آمده که او «به عنوان کارشناس سایبری در یک شرکت وابسته نهاد نظامی مشغول به فعالیت» بود.
با این حال در گزارش مفصلی که ارگان رسمی دستگاه قضایی ایران درباره این زندانی منتشر کرده، مشخص نیست که او چه زمانی بازداشت و دادگاهی شده و از جزئیات روند محاکمهٔ او نیز اطلاعاتی منتشر نکرده است.
شماری از وب‌سایت‌ها و نهادهای حقوق بشری نوشته‌اند که احسان افرشته، متولد سال ۱۳۷۲ و فارغ‌التحصیل کارشناسی ارشد مهندسی عمران و متخصص شبکه، اوایل سال ۱۴۰۳ پس از بازگشت از ترکیه بازداشت شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/75439" target="_blank">📅 08:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75438">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I9t21Cx781KoltaZ6FAhrUpRbfLfPnSkCwT9IsYjdWU6QpSZfCW4b-qaD0xZX7lLfxaGaLcR27012UsA7nuYOlja36QNlGrxO4lQYLKmKoeg-3wX-5g1Nc8X36H7yIEjli_CF4q-A4czyz1sMtQ9M7TBA7WFfv6F9xOehAePfbJqgvfOePx53DiK1_KFtTvaUpt_fUn3_dlDsHhgTVhtrOWHzZeeEd0P24BRNHt9VpBEx27x5ZbwaEcaCJebfl-eUNq3blLH8wSydX2ZxlpLiXqSXR6N7yFIwWrIgUBbzxXY3HpuzmMt-PDl5C_YIgoAd04U3OwgPPIe1mBWTQ9GSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه چهارم۰۰:۳۳
پیام‌های دریافتی:
دوباره لرزید  شرق همین الان 12:33
بازم اومد ولی ریزتر از قبلی
همین الان دوباره لرزید (نارمک ) ۰۰:۳۳
من الان دوباره لرزیدم
وحیددد نزدیک چهاربار تو پردیس
#زلزله
اومد نمیدونی تختم چجوری میلرزید
آپدیت: تصویر دریافتی بالا و متن رسانه‌های داخلی به نقل از مرکز لرزه‌نگاری:
بزرگی: ۳.۴
🔹
محل وقوع: حوالی پرديس
🔹
زمان وقوع: ۳۲ دقیقه بامداد
🔹
عمق زمین‌لرزه: ۱۰ کیلومتر
🔹
نزدیک‌ترین شهرها:
۱۰ کیلومتری پرديس (تهران)
۱۱ کیلومتری بومهن (تهران)
۱۲ کیلومتری رودهن (تهران)
🔹
نزدیکترین مراکز استان:
۴۱ کیلومتری تهران
۷۶ کیلومتری كرج
🔄
آپدیت ۳:۳۰
پیام‌های دریافتی درباره لرزش پنجم
زلزله دوباره
ساعت ۳:۳۳ شرق تهران باز زلزله اومد
پردیس،۵ دقیقه پیش برای پنجمین بار زلزله اومد وحید جان سابقه نداشته تا حالا خیلی مشکوکه
ساعت ۳:۳۵
پردیس دوباره لرزید سه و نیم
سلام وحید جان
ساعت ۳.۵ باز زمین لرزه اومد پردیس، با صدایی شبیه به ترکیدن
🔄
آپدیت: لرزش ششم ساعت ۵:۵۷
یه کوچولو دیگه زلزله سمت پردیس حس شد الان
و الان هم دوباره لرزید
٥:٥٧ دوباره پس لرزه اما خفيف تر
آقا وحید ساعت ۵:۵۵ دقیقه صبح، پردیس برای ششمین بار لرزش احساس شد
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/75438" target="_blank">📅 00:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75437">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">زمین‌لرزه دیگری به بزرگی ۴
این میشه سومین بار ظرف چند ساعت گذشته! اولین باردر شرق استان احساس شد و پیام‌ها از پردیس و بومهن و دماوند بود و یکی هم از لواسان]
پیام‌های دریافتی لرزش سوم:
تهران مجددا لرزید
دوباره لرزید کمی خفیف‌تر
وحید جان دوباره لرزیدیم  شرق تهران .. ۲۷
دوباره! پس لرزه بود.
دوباره هم اومد ولی ضعیف بود خوشبختانه
وحید جان شاید باورت نشه اما سومیش هم همین الان اومد، منتها خیلی کوتاه و کم بود...
ان، زلزله، ۰۰:۲۷
باز اومد، کوتاه، شاید پس لرزه باشه
دوباره اومد
یعنی اون رفت این برگشت
دوباره زلزله اومد
باز هم لرزش ۱۲:۲۷
سلام بازم لرزید حدود دو سه دقیقه پیش طوفانم هست خدا رحم کنه تو این شرایط فقط بلایای طبیعی کم داریم
اینجا ازگل، ۱۲:۲۷دقیقه، دوباره لرزید
🔄
رسانه‌های داخلی به نقل از مرکز لرزه‌نگاری:
🔹
بزرگی: ۴
🔹
محل وقوع: حوالی پرديس
🔹
زمان: ۲۶ دقیقه بامداد
🔹
عمق زمین‌لرزه: ۸ کیلومتر
🔹
نزدیک‌ترین شهرها:
۹ کیلومتری پرديس (تهران)
۱۱ کیلومتری بومهن (تهران)
۱۲ کیلومتری رودهن (تهران)
🔹
نزدیکترین مراکز استان:
۴۰ کیلومتری تهران
۷۶ کیلومتری كرج
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/75437" target="_blank">📅 00:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75436">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GxFc1fKTcVczT3E0nq8Asow6uOZgY9sOxjt8R-NRKnwFS6pKAngSb5_4kfhAmTSeVlCkHM-SuEFWbahB9cRP4vtqsdNyN5nTw2FBLZUGeNHD8LR1baXbzPMFhQ5lgsaHGoKfqvs6HpvFyhmSmzrMZyBeczv0b-N-IuIVrt1t14NBwsdG16T3PNsemksjTykwj8RzSS9ABEPNNJU6Oi4vkv63ckaF2ciMF2ri2wtiTaUCUqx-OwRwaxBR6O5LHc2PWIxkCCYJK8jcQC5tZwXuYF9qmrT_BD6AJ5YAR1xjOqXd_LM5GZVshb7Ay-wRQ_qgzpWYBw4p6iZIDFOXV6griA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
وقتی «رسانه‌های جعلی» می‌گویند دشمن ایرانی از نظر نظامی در برابر ما عملکرد خوبی دارد، این عملاً خیانت است؛ چون چنین ادعایی کاملاً دروغ و حتی مضحک است. آن‌ها به دشمن کمک و از او حمایت می‌کنند! تنها نتیجه‌اش این است که به ایران امیدی واهی می‌دهد؛ در حالی که اصلاً نباید چنین امیدی وجود داشته باشد. این‌ها بزدل‌های آمریکایی هستند که علیه کشور خودمان طرف می‌گیرند.
ایران ۱۵۹ کشتی در نیروی دریایی خود داشت؛ تک‌تک آن کشتی‌ها اکنون در کف دریا آرمیده‌اند. آن‌ها دیگر نیروی دریایی ندارند، نیروی هوایی‌شان از بین رفته، تمام فناوری‌شان نابود شده، «رهبران»شان دیگر در میان ما نیستند، و کشورشان یک فاجعه اقتصادی است.
فقط بازنده‌ها، ناسپاس‌ها و احمق‌ها می‌توانند علیه آمریکا استدلالی مطرح کنند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/75436" target="_blank">📅 23:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75435">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">"وحید تهران لرزید"
+ ده‌ها پیام دریافتی مشابه درباره احساس لرزش زمین در مناطق مختلف تهران
به نظر می‌رسه بیشتر پیام‌ها از سمت شرق و شمال شرق تهران هستند گرچه در غرب شهر هم کاملا حس شده.
حدود سه ساعت پیش هم در شرق استان تهران حوالی پردیس و بومهن و دماوند زمین‌‌لرزه خفیف‌تری حس شده بود و غیر از اون مناطق فقط یک پیام از لواسان داشتم و پیامی از خود تهران نداشتم.
🔄
رسانه‌های داخلی:
زمین‌لرزه‌ای به بزرگی ۴.۶  ساعت ۲۳:۴۶ امشب مرز استان‌های تهران و مازندران را لرزاند.
این زلزله در حوالی شهر پردیس و در عمق ۱۰ کیلومتری زمین به وقوع پیوسته و در بخش‌هایی از پایتخت نیز احساس شده است.
بزرگی: 4.6
محل وقوع: مرز استانهای تهران و مازندران  - حوالی پرديس
تاریخ و زمان وقوع به وقت محلی: 1405/02/22 23:46:07
طول جغرافیایی: 51.83
عرض جغرافیایی: 35.82
عمق زمین‌لرزه: 10 کیلومتر
نزدیک‌ترین شهرها:
8 کیلومتری پرديس (تهران)
10 کیلومتری بومهن (تهران)
11 کیلومتری رودهن (تهران)
نزدیکترین مراکز استان:
41 کیلومتری تهران
77 کیلومتری كرج
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/75435" target="_blank">📅 23:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75433">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SljJAONGT00CYZYP4Pt9XsMGhza_6MzeMiTKTXbFFElS2PMCEzslHH0X4k7TzGlPF_ysS_exyVBsh_6-QX--txB-m6m1pw5dqSfvXQYOUg3UDKYkGj_8mWvUBj1wZLJXbTDEytc4_gREfNQtQscBmLx7JtuP7KLZ6EdmJ8QHs5CLIsEfNKRJ2iAv7wFfTFH1WCWEkHZ4PFWoCH7505Wq-vpKD9jzDk-nZowyEWvOiYHtBsiknyfYPuZOjufLovBnPSR2VKKIwxQq5nWcvK8HNRLVahehlnfDakt21VimQCGbqEHWYaBVxQJXWuoQK1FWIE8uC1GnDc6GnJ2Kbl2LbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/93a0dfa6c7.mp4?token=DEQ85UL8XghEn9fOqFPa3AiyTN0jvL68qh3YUdFUUXNx4-iUrG6fc-eow2SbTZwI-ZbcprQjIe0-z6zKm8Z46UBKwAOF34wC41Mr4bblp6D9tze3Df2N8XuL006aMuUSDkhlyx7AETT0MOs-c5VuqmvtoNlBkNxJ912lVb4JLCO2lb1s_Rdi-Ukj7YhF62N0zrEknEBmKIVkKiu4zxBXb2Dty9jqboW7SQnaKOAempse-atWCjE9T6QlsNawoIzEsxrm5ofj3f5lBNgHbnQCNlmTVyXkfaI_lvyV1LmSy_DYuuE0jq-l4xNagaWym16mVI7Tpr2_KDPJsCXB8Sf7rg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/93a0dfa6c7.mp4?token=DEQ85UL8XghEn9fOqFPa3AiyTN0jvL68qh3YUdFUUXNx4-iUrG6fc-eow2SbTZwI-ZbcprQjIe0-z6zKm8Z46UBKwAOF34wC41Mr4bblp6D9tze3Df2N8XuL006aMuUSDkhlyx7AETT0MOs-c5VuqmvtoNlBkNxJ912lVb4JLCO2lb1s_Rdi-Ukj7YhF62N0zrEknEBmKIVkKiu4zxBXb2Dty9jqboW7SQnaKOAempse-atWCjE9T6QlsNawoIzEsxrm5ofj3f5lBNgHbnQCNlmTVyXkfaI_lvyV1LmSy_DYuuE0jq-l4xNagaWym16mVI7Tpr2_KDPJsCXB8Sf7rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: خواهیم دید چه خواهد شد
دونالد ترامپ، رئیس‌جمهور آمریکا، پیش از سفر به پکن گفت که رئیس‌جمهور چین درباره جنگ ایران «نسبتاً خوب» عمل کرده است، اما واشینگتن به کمک او نیازی ندارد.
او روز سه شنبه در جمع خبرنگاران افزود که قرار است با شی جین‌پینگ «گفت‌وگویی طولانی» درباره ایران داشته باشد.
ترامپ تصریح کرد: «فکر نمی‌کنم ما به هیچ کمکی درباره ایران نیاز داشته باشیم. ما به هر شکلی که باشد پیروز خواهیم شد. یا به‌صورت مسالمت‌آمیز پیروز می‌شویم یا به شکل دیگری.»
رئیس‌جمهور آمریکا با اشاره به این که توان نظامی ایران در جنگ اخیر از بین رفته است، هشدار داد: ««ایران یا کار درست را انجام خواهد داد یا ما کار را تمام خواهیم کرد.»
او به جزئیات بیشتری درباره این هشدار اشاره نکرد، اما این اظهارات در حالی است که ترامپ پیشنهاد آخر ایران برای توافق پایان جنگ را در روزهای اخیر رد کرده و آن را «کاملا غیر قابل قبول» و «فوق‌العاده ضعیف» خوانده است.
رئیس‌جمهور آمریکا قرار است چهارشنبه برای دیداری رسمی وارد پایتخت چین شود. این سفر که قرار بود در ماه مارس انجام شود، به دلیل درگیری نظامی آمریکا و اسرائیل با ایران چند هفته به تأخیر افتاد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/75433" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75432">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hgDdlHi4aA88lF6YInQFNrs5ddjAHo8SvqAKuvADy9toYjbopY-_8x6-TJMjsSW4nRfEZdqIKXj3wi-76-DvmLTDSgIPE36CF60X2bycex0tQg79e4gKtCoGNBdDtkXJ_II7pRznWIpNn1hV6GB6zTi1bySwul8giAcFi7aukQ58c1PSXi7glu3Ft8woKtHVo6zUlpiGE6Tkc9pQwZiCBZvoYnLnoajGmE5Xf3tZcYxGuwaxS_1ngnHE4F9DPCu6d5F-Eng9Q8JsSobq33fijRHxaU5LQUxqpxGBQLyGRQ5SsimWh8SbJJ9BgX2DdDTcJ9H5IBCGMZ_odi1GtlqUFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در گفت‌وگو با برنامه رادیویی «سید رازبرگ» گفت: انتظار داریم اقتصاد ایران زیر فشارهای ناشی از محاصره بنادرش فرو بپاشد.
او افزود این درگیری بدون نیاز به شتاب‌زدگی حل‌وفصل خواهد شد و جمهوری اسلامی با انزوایی روبه‌رو است که آن را از منابع درآمدی محروم می‌کند.
ترامپ گفت ایالات متحده در حال انجام ارتباطات مستقیم با مقام‌های تهران است و برای رسیدن به توافق عجله‌ای ندارد و او اطمینان دارد که تهران غنی‌سازی اورانیوم را به‌طور کامل متوقف خواهد کرد.
@
VahidOOnLine
دونالد ترامپ گفت حکومت ایران با انزاویی روبه‌روست که آن را از منابع درآمدش محروم می‌کند و انتظار می‌رود اقتصاد ایران زیر فشارهای ناشی از محاصره بندرها دچار فروپاشی شود.
او افزود: «این درگیری بدون نیاز به شتاب‌زدگی حل‌وفصل خواهد شد و جمهوری اسلامی با انزوایی روبه‌رو است که آن را از منابع درآمدی محروم می‌کند.»
دونالد ترامپ درباره اورانیوم غنی‌شده در ایران گفت مقام‌های جمهوری اسلامی به او گفته‌اند قرار است آنچه او «گردوغبار هسته‌ای» می‌نامد در اختیار آمریکا قرار گیرد، اما بعدا نظرشان را تغییر داده‌اند. او تاکید کرد در نهایت این مواد را به دست خواهند آورد و موضوع را جمع‌وجور می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/75432" target="_blank">📅 17:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75431">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx7HL19fOYXDJ8bpkJiyYD1KDfwbSGYOgjmjzhtxpBIR1LPWnwgBOav_olb6pjlzQe6A2mlUP8gRliWbtHaximhIbh-2DY9y4xm2kvc6B7bZPFLqE99aHYjXatQFhrgTqW-0YNxR7Y98GLMVW-y2YdR94_uPnc7NZ6PBBS_T4MSOYPsNX2EFUYODKGlbXWoB4ch00PZGNicGAU2Uryd0oYid9GOzEYb10MsTkW-1oz7CX22BtVqnm_LXO6SacZjDl_vk36HLjvt_xLSRGI0iVxlZEH1news6P_HWUD1CCZ3EoUF-6l0CRX_-b9dOhYeU6KLhjdQKpGNUQ-BVydRskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد پنتاگون روز سه‌شنبه ۲۲ اردیبهشت اعلام کرد که جنگ ایالات متحده با ایران تاکنون ۲۹ میلیارد دلار هزینه داشته است، رقمی که نسبت به برآورد ارائه‌شده در اواخر ماه گذشته، چهار میلیارد دلار افزایش نشان می‌دهد.
به گزارش خبرگزاری رویترز، در حالی که تنها شش ماه تا انتخابات میان‌دوره‌ای کنگره آمریکا باقی مانده است، دموکرات‌ها در نظرسنجی‌های عمومی موقعیت بهتری پیدا کرده‌اند و تلاش می‌کنند این جنگ را به مسائل مربوط به هزینه‌های زندگی پیوند بزنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/75431" target="_blank">📅 17:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75430">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s-uPQ0j8m1roKtkwXPIekubyUdSHER8Ywt7aH12SWDVKdaSQhzzsjxEpBbrLpUP5zaoJ8HwSb3tzzyyeD0AD5pot_JavBHttL3mJlSR7rdM__kg8f5Htc5ImeQpHjAk7Njiyo47hsyTGRNVI_FZ9ceNJELtWBbMzP3_K7nfpkRgX-T4ZYqxtOc4TcfVo28Q_vQG0Tt6bBUY9TJt7S3JkEDtABZ4WtSa9b5TKq9mqDpUa-dwiCjMkIH9i36vhvLKyf_4e-1cqpoMfALVbRS9_aaVe6UWWGpfhRoiSaCGWOENAwRQHF_Dk9T2gKzYqx2QkdW7lbo44R0lZi5xPCX-Cqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه در تروث سوشال دو تصویر گرافیکی منتشر کرد که صحنه‌هایی از حمله به پهپادها و قایق‌های جمهوری اسلامی را نشان می‌دهد.
در یکی از این تصاویر، یک ناو آمریکایی با استفاده از سلاح لیزری یک پهپاد جمهوری اسلامی را هدف قرار داده و نابود می‌کند. در تصویر دیگر، یک پهپاد آمریکایی دو قایق جمهوری اسلامی را هدف قرار داده و منهدم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/75430" target="_blank">📅 16:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75429">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4234e573f2.mp4?token=iHhv_qP2PpgUoaO2Nf8eX6-GSVC70dxBcnqgBnh3tLy0wZ0BmvxgWAVawbUQWQM6CGpZRbeHNDM_4qSc8orsxPagj4sU5w__J9zJ4AZZg_5O3xllibVOVhm5_CDRy9IRRqxl6MFzedFva2FGX0DfIoP3NmrX5mxNYzocjt-iwnAGyYH99TZTreihj3fZC3DY1Rd8tZmd-5mOpdGExpJ6d2Jj9b3iQ4NVw1JQsBoy1PyTElb6j5LuHpc58XzgxMoG74GN5Qz1U_YY3gbHx5QONlJkHnuE1NN-dvImuR6I1JJdl3WE3A8yAJ85rj6gmDenHRoWnN4Pl9kkyObzodNZpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4234e573f2.mp4?token=iHhv_qP2PpgUoaO2Nf8eX6-GSVC70dxBcnqgBnh3tLy0wZ0BmvxgWAVawbUQWQM6CGpZRbeHNDM_4qSc8orsxPagj4sU5w__J9zJ4AZZg_5O3xllibVOVhm5_CDRy9IRRqxl6MFzedFva2FGX0DfIoP3NmrX5mxNYzocjt-iwnAGyYH99TZTreihj3fZC3DY1Rd8tZmd-5mOpdGExpJ6d2Jj9b3iQ4NVw1JQsBoy1PyTElb6j5LuHpc58XzgxMoG74GN5Qz1U_YY3gbHx5QONlJkHnuE1NN-dvImuR6I1JJdl3WE3A8yAJ85rj6gmDenHRoWnN4Pl9kkyObzodNZpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری سخنگوی دولت مسعود پزشکیان روز سه‌شنبه ۲۲ اردیبهشت به دلیل وضعیت اینترنت به بگومگوی خبرنگاران با فاطمه مهاجرانی منجر شد.
سخنگوی دولت تاکید کرد که «اینترنت پرو» با مصوبه شورای عالی امنیت ملی که ریاست آن را مسعود پزشکیان بر عهده دارد،‌ مورد استفاده قرار می‌گیرد.
او در عین حال تاکید کرد که این اینترنت ویژه کسب و کارها است. [در حالیکه خیلی از مردم بدون کسب و کار هم پیامک گرفتند بیاید پرو بخرید]
@
VahidHeadline
فاطمه مهاجرانی گفت با توجه به وضعیت جنگی، فعلا اینترنت عمومی وصل نخواهد شد.
مهاجرانی در پاسخ به پرسش‌های متعدد خبرنگاران درباره وضعیت اینترنت و به‌ویژه «اینترنت پرو» گفت ما در وضعیت جنگی هستیم. رئیس جمهوری به‌عنوان رئیس شورای عالی امنیت ملی پیگیر حقوق مردم است اما وضعیت جنگی است و بعد از پایان شرایط ویژه، اینترنت به‌حالت قبل بازخواهد گشت.»
پس از این سخنان، چند خبرنگار تلاش کردند تا با یادآوری تعهدات دولت پیگیر وضعیت وصل اینترنت شوند. مهاجرانی خطاب به آن‌ها گفت: «وقتی رئیس جمهوری آمریکا می‌گوید آتش‌بس به تنفس مصنوعی وصل است، انتظار شما چیست؟»
@
VahidOOnLine
فاطمه مهاجرانی، سخنگوی دولت جمهوری اسلامی، با اشاره به قطعی طولانی‌مدت اینترنت در ایران گفت اینترنت حق مردم است و عصبانیت مردم کاملا درست است. اما در ادامه تاکید کرد: «عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود.»
او افزود: «رسانه‌ها کمک کنند که این ادبیات را جا بیندازند. دولت طرفدار دسترسی آزاد است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/75429" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75428">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/To1ezTm3vLawxPjr4A6XdqxMcN4WFyCaLHgpZd4Ab25YpLg5BobiT1aGZcP2uUA2n9XWzX1sx4EXwLSsUWtawYfVAoZw6Q52ToMHgsCmv0kKiApKcPRxEmnK02wTVIErCBtm-5ppSCmTjEayINRrrviGlUqmqWnahm20eg3EhLAigy4rWG95XDKI6j1U66uDH0MgoLql9iM1RubUf31_VCMD93cC_NNLqho1wFh15FAvUbYdFE7GFZr6yjzKGkpHkGsVUpbf0ltablR9jSk2L1wbdhV5Oyj8RkVuNOfDPzTgtt9v7I1Vzf_w36JRFITpEwAEUwvDL0o_CUYXY8Flvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه از اجرای حکم اعدام یک زندانی دیگر به نام عبدالجلیل شه‌بخش در بامداد سه‌شنبه ۲۲ اردیبهشت خبر داد.
ارگان رسمی نهاد قضایی ایران، شه‌بخش را «تروریست آموزش‌دیده» گروه «انصارالفرقان» معرفی کرده است.
از زمان حملات آمریکا و اسرائیل به ایران، جمهوری اسلامی اجرای احکام اعدام را افزایش داده است و در برخی روزها چند نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/75428" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75427">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSQaGJmw9igEi6nh2eX1OJxQQS3v2ewqjaLG0_RaIPniOxNA9ZnyQk987uMsf1R7R0cfhHQVixu5OjabOs4FDkLRTN1f_rif2W7a3QWBmfsPYgd4YlUAYyGKuif8JcyKJMPCwWbhYmsJ9vEZ_akvN6YfhbJMRFyxwH5rz1KWHEi-R99ZrJTYs0SVtvqxY7lH2DSvdzSpH4pyHDb6Hn4jGNS50HsOGRgflPAFlsPmAWuLApeUcSFy41ok9Krlofea_REClMvPlj8GUnZz9IP-WsT_C2r68SRR1EIQXHG2Ndh41h63NsOBMfflmN7H20cQMXjNnwAF02XVOfo-3wts9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نشریه آمریکایی وال استریت ژورنال، امارات متحده عربی به‌طور مخفیانه حملات نظامی علیه ایران انجام داده است؛ موضوعی که به گفته منابع آگاه به این نشریه، می تواند امارات را به یکی از طرف‌های فعال مخاصمه با ایران مطرح کند.
منابع آگاه به وال استریت ژورنال گفته‌اند حملاتی که امارات تاکنون به‌صورت علنی تایید نکرده، شامل حمله به یک پالایشگاه در جزیره لاوان در خلیج فارس بوده است.
در اوایل آوریل گذشته و هم‌زمان با اعلام آتش‌بس از سوی دونالد ترامپ چند حمله هوایی به تاسیسات نفتی ایران در جزایر این کشور و اصطلاحا مناطق فلات قاره شرکت ملی نفت ایران صورت گرفت که باعث آتش‌سوزی گسترده و خروج بخش بزرگی از ظرفیت پالایشگاه لاوان از مدار برای چندین ماه شد.
ایران در آن زمان اعلام کرده بود این پالایشگاه در یک «حمله دشمن» هدف قرار گرفته و در پاسخ، موجی از حملات موشکی و پهپادی علیه امارات و کویت انجام داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/75427" target="_blank">📅 03:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75426">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejNDN03_tV0O5F74R5QbWKl2XIArJ6R36KkPyOTNMgxsbso33MKtx2mgVDxt0GBrGsEajIPCWMiZ5dGuo4CiBRL-_AnkMP0WaK-2U19fy-3GhmgU2lDNB61A36QXnlQhtQIi2vRxjUXHVjGs4stqIu6J0769p8sHPVkD2JzMyOn2Zhko7PDIMfsnBwk5b2ugw9KkYTXMuz_kSMJAFILhulO4A70Lh-M0ZOfLXWVwtT9bkt9mIYohJrLqLzfy6CNEXv8GwnG1yL6FXjRfBV1dQ0wucnRBf09e1r-Skoxrk6RfLpOhDBkWpnirW4lSPyeQL6-Vv3pyDz4rQfWozdQ9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده، روز دوشنبه، ۲۱ اردیبهشت‌ماه، در بیانیه‌ای رسمی اعلام کرد که پاسخ اخیر تهران به پیشنهاد دیپلماتیک واشنگتن، نه‌تنها از نظر سیاسی غیرقابل‌قبول است، بلکه با استانداردهای لازم برای لغو تحریم‌های مالی و اقتصادی نیز همخوانی ندارد.
این وزارتخانه تاکید کرد که رویکرد فعلی ایران مانع از هرگونه گشایش در مسیر مبادلات بین‌المللی و آزادسازی دارایی‌های بلوکه شده می‌شود و تا زمانی که تعهدات شفافی در حوزه برنامه هسته‌ای ارائه نشود، فشارها بر شبکه مالی این کشور ادامه خواهد یافت.
در همین راستا، اسکات بسنت، وزیر خزانه‌داری دولت دونالد ترامپ، در اکس با بازنشر این بیانیه، موضعی قاطعانه اتخاذ کرد.
او با اشاره به اینکه پاسخ تهران نشان‌دهنده عدم تمایل این کشور به همکاری واقعی است، نوشت: «در حالی که دولت ترامپ با حسن نیت مسیری برای دیپلماسی باز کرد، تهران با پاسخی کاملا غیرقابل‌قبول به میز مذاکره بازگشته است.» بسنت تاکید کرد که وزارت خزانه‌داری، سیاست‌های مالی را به گونه‌ای تنظیم خواهد کرد که جمهوری اسلامی متوجه شود عدم پذیرش توافق، هزینه‌های اقتصادی سنگین و غیرقابل‌جبرانی برای نظام پولی و بانکی این کشور به همراه خواهد داشت. او نوشت: «زمان آن رسیده که تهران متوجه شود هزینه لجاجت، فروپاشی کامل اقتصادی است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75426" target="_blank">📅 23:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75425">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FHSegrB9AtcJoLLhOarX-7FlQKqL4pC_Rag797exHPPHkdYoYojoxiG-Ai-uytckFaxPWTofTVrpyrwUw_kPeuQH4hW6qlSuLGDAO9B_Fme0jtXKgAhWudMGM9VRsTRNxzxWCM-mWEd1P1N5M4eoGDEe2h5A-vBeLcO16pw-ENeDreDQJeOadSg5FjY88IiPEy2ypkI_hLO6ipfU6fUetQmNxCWvZ4ADd-WYkZAAlzfjrVdn5_DIwaDDHe7GL5m778dNwB995spxFUfDkS8TKp2IwnySgB5W4--GjJ7nZahn9NVJVABmeUH5HDlJdU7B3iiqcdzd88Qi_g0-SXcukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی و رئیس هیات جمهوری اسلامی در مذاکرات با آمریکا، دوشنبه ۲۱ اردیبهشت‌ماه در شبکه اجتماعی اکس نوشت نیروهای مسلح جمهوری اسلامی آماده «پاسخگویی درس‌آموز» به هر تجاوزی هستند.
قالیباف نوشت: «استراتژی اشتباه و تصمیم‌های اشتباه همیشه نتیجه اشتباه خواهد داشت. همه دنیا قبلا این را فهمیده‌اند.»
او افزود: «ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/75425" target="_blank">📅 22:19 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75424">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rM26y7M-AMs2PZnSw9lpd0VqCdepzfo-iNkh_x4jTPjh2LG2oWGFk4KcossmMDybauvWpjj6rOEy2gFBzRAeHAWFSIIjJaHzBh0p_3eyocyle586NKFV07iOGjkHAlbb7nKvdyVWfpl9U_cGBnj0iL7StvSPJysBKa52PBQwxaz0wC-B0uvMED080PPMLVXGMtzH9mKpiwGlZB6P3qQ3fLITsXQFQ_4LPTKEQ3TiEtc7zi2irOYme0jrv6soAjVddq6xErVu0uvFOpDMwJZDgT6ZpKprPQmQoTokppwRrZJM0VwEpATnuOlukNb2MRnKXUkQ8t3XBYML7vh4XTy1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس گزارش داد دونالد ترامپ روز دوشنبه روز دوشنبه ۲۱ اردیبهشت ۱۴۰۵ با اعضای تیم امنیت ملی خود درباره ادامه جنگ با ایران و احتمال ازسرگیری اقدام نظامی علیه جمهوری اسلامی جلسه برگزار می‌کند.
بر اساس این گزارش، سه مقام آمریکایی گفته‌اند مذاکرات میان تهران و واشنگتن روز یکشنبه به بن‌بست رسیده و همین موضوع گزینه نظامی را دوباره روی میز قرار داده است.
اکسیوس به نقل از مقام‌های آمریکایی نوشت ترامپ همچنان خواهان توافق برای پایان جنگ است، اما رد بسیاری از خواسته‌های آمریکا از سوی ایران و خودداری تهران از دادن امتیاز جدی درباره برنامه هسته‌ای، احتمال اقدام نظامی را افزایش داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/75424" target="_blank">📅 22:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75420">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YcxdVr6K20SeHf-p8392Cwfc2ts-IkqZD3RsCUKJo1ya-pSPDOeKHeHtsqpI6ZFUVlEqu-gqsDESLTccBWLBrstADVI39w-aDOzzKAHmRqM9H4vqAdRKqSrfFA33dQfHQmui3-7WgBoL4sd1OOB3X4zd_DEoocB00G-FpBqGkEkZ3hkZX7IEQqpKz1cPNauhIgqB33H8b9Zg8dXYt1kCOt0C5WS6xiYztebxIp7C6IHdljdQ6CMcs-LgtC7quINBucAcMfS6IZqp_Suaw3apk8FYALLXz63S4VQbb_AgwndUQ82DW383tPfGxcBWUTqTltelyhnE6jG3X61TgclmSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GnxLiqjKd4kvEzcZgGi545qpyDMw65ok9ZApylgL7OPSdyfoMmVAI6WglPBwQ20DklzQAlsqlA-h-HgkhYChWNBwcjx3vQmbW9twT9S31g_1LCSQ5TZ-6CpVCFFwfHFMir7Rajh4z3OnHW9e7HVltIB61yLwHnc7ghcIuJQ9VelybAHUAkoEmlffzVcq87s0lCrjVW1WDRUaPmUIZy8FXgdUrO3mzRmlL_btFIHPMnZLEQFg8ttz7T5uYM8Sjl8n4tZWS1POacor4-G-0yt3KtlCzyG62Cc0ifZ2STYRWMEzdiVnC-AAxP6pPN6aC4fwuIvNENya9mmYUoyThqdidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P5wmB11_f_g7-UQez_K-CNRJmDo8-AdVcKPzbPhgrH7vOXlp4jub4zMm4sRsdY-OSGztylR4ZIEcW6QfPtuY9wJAkcfOuVQZObNn7SjfD4Ai_RKjM2f_IUUtxI_UDTQ-5WMW1Vs1nF8WixBICe0RlHGTgbFxWpaw3NGv1Vuf3HtACMBN9wGz5xwVEeb9qHpehjAQB4iLKieCcP1TJbX8kC0-yW0DPzlzYyZB6t2O5HJCB5kRYnm8AS2anmW_TSAFT2QrJ20wWOoLD-cyQPdFnw-VumBm6OWgkSj-KQ_qHRrF2Pc-KstO0KLWdCS6ftX3KocB6XGOfML_iNKj5bRsOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mZY88rVbAg0XTg0jg4cYTzOAnzOQmXM_iRZUBI4WgCa-GfF-LAKZfmWUGBFpmXO0IMl4LT2X7eZtZCrpm-ZeJTYavrSK9xalHa0suQHeqFYAFTYc4iWo3fqKsRBK8YRNesdr6kj89FafPWia40oZ3oSZ2szeiByp4YZZ4lZuUiAYEvzn8ZxveKLIsD-FcQg3VKoo3ZQ3diu2gOuHf7GK_GvJQIVog-bpLTqYx-ZUaNgdW-UZPIOIhLIXk3QhgdGA1LL_9pc_Ju8Rpk716k5C2dAZcXa_2xLeV_pvUMKXmz6v35P06keOr06CIDhDCCyid0m4A0VVkjp2PjOdAbVhtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی حدود ساعت ۱۹:۳۰ به همراه تصاویر بالا:
▪️
وحید الان برام پیغام اومده که من جان فدا هستم و ثبت نام کردم ولی خودم در جریان نیستم
😂
▪️
آقا یه اتفاق جالب افتاده. ظاهرا بعد از هک شدن دیتابیس جانفدا دوستان یه فکر بکر به سرشون زده.
من هیچ وقت در این کمپین ثبت نام نکردم ولی پیام زیر رو برام فرستادن. فکر کنم خودشون به صورت پیش فرض همه رو تو این کمپین عضو کردند، حالا هرکی جرات داره انصراف بده… البته نمیدونم انصراف داره یا نه.
▪️
امروز این پیام برای من اومده در شرایطی که من اصلا ثبت‌نام نکردم.
حتی برای پدر خانمم که فوت شده هم اومده.
▪️
امروز عصر واسه من این پیام اومده
در صورتی که من حتی تا حالا سایتشو هم باز نکردم
حالا یا خودشون دارن روی شماره هایی که از یک سایتی یا صنفی داشتن ثبت نام میکنن، یا اینکه یک ادم [...] واسه من فرم پر کرده یا اینکه مسیج الکی فرستادن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/75420" target="_blank">📅 20:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75408">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bHcA2XCsjTIKAYRUa4EniEDY36l9oZODiJe0BTYAchV2Gb-K3qkQYwzmgYjm1Hxwb8l6hM0IWzdLjzjFww-9kGmm-hz49aP2fse1KmpctRT_LnnfQPeYrqU3BYNWXvNw9C_lBqQHGnN_Fl1a2qzYGm_2nc1y3AKdwfblA96d4XMeMq_iRj70nRAe13G1y-aVeT_s5X4Lj8vVMHyjoleebZbvz2ximEWqEQnP5eyw8iiTZ_qbFyHsl_ZwNM0HCwmGOHtiEpayP7-vPOokY1fwS4YYtD3zDIp3PiarOBB30VIIh6WS93Vr1E5UuB0szxzAknlANI3xhRPxxSFD8MNxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d0QjdNh6Hp-hDwO7dXK-kMgEUStvF3bkje27wLmAOZvs9bjxXHni5ITSxtJW1gyHeNejgfMTxHH902Ikx9l-h6kMFtE1MhIDX0TRtjYpxS5HqVYjlS8ohy63fh4SH5lsnoGZ-SM-rCM3rGEAD02Wnm-2LXof_Xo9iZevl-nwp7FkVKDSvm1AG1Y0-XWd54IpBwQ86jR3Dip8gGv0uuuZiQdVdj2zGc76Gt0lj-eGb-6rJ15wuIO4sMphfCdqgCmZ2awotWDq2M8C6MKkJHjwA4A7-_YxlbfQc9TJzAq1FWnZm3jvi9YRqPyC9dd_SRKeCPhDlBl5nh78VHLZplo1WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VhZG75ViDEuygMh1V6KAFsQ5rCpC5wbt2vSTBAu_GjdmUa95vFZLsKu9okGb8WO8eJmZwFZe9DTrq5uNGD2-yzZHqxbNq62zznoaEOS70LOIPQXD_rlegLtQquuuydqMyYBCARVMId2YRqpYcxshppJtT-GKZBt1Qe6nVmBE4nPXOrDt4gE_dHa44QIkFhEfktztgEKmQsAZLq1E5wiAgYfedzdyaXzbTQF_gj0xTxHvPOaPpWL7rnTwC5--FlibVavxiatFA9smy9A1FuPnkUcQFmXLHDvxK3yXLzSwJEScw15cx3K-5BJaIa38tS8F8bthOa8u0UZU5nFVwHh6Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YgA_0cfGX5xHAgoc4e84EcNpYOpPmITV_G0baWyjLr8880OjBBxETUh_nzC8kLDIFlkaUTXby65oTUSGN5aQIcIPj-0GnUx3dJTM90Fq7gIdi7gk3aOWCF8DQfGfAWPadXXY2FlUW4Nt2lLZBH4sSpEA3C1hENSvpZKutIlgQnx3PpL_zyDmPNwdmT7invIuhR_H0fEnPt2IdgvsLSwC7inAeILkzbBodkQyuW8U0Na7x6q1qxxXbi90Nu1LJMMfZig-EBRlOyewcz3yMqhBZI9aVvTW80k3EpWQ4LDMbm1a9li80XmxbBowsZsrEt3JkFXZImlgJXF6Iqhyz3JpuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a88e38f89c.mp4?token=QJQeaxaoRkQ7NQcbSQWjNJzgiReZPpgu7EshZogoBiRapuwecz4lez2jicP_sQsouLkxkZPinWITA5dSmrmhhscBGHvCS2HbTTBzGzy8OD7OFKwXQE5u4M5QyxPes5WU98xKSI-kWmNjPYj_Tg9Y7k94WcJVkkrBuZ73CWUR0IVGmjy3JesihgD7t_YBwqxwR2kVQzEv8WlVqdAN6UC7b2LiZlnIEN7ck52hAtLnM5cCk1l4ET27stIi0k8JCv7_zAsdJDYFkQyoED6K9l4fYlTXFQ-QV7eRYkAgmunL5DetgenTJgbZAzKj6pMiG3QTmcmaUWCM-pWTIK0HeQZfiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a88e38f89c.mp4?token=QJQeaxaoRkQ7NQcbSQWjNJzgiReZPpgu7EshZogoBiRapuwecz4lez2jicP_sQsouLkxkZPinWITA5dSmrmhhscBGHvCS2HbTTBzGzy8OD7OFKwXQE5u4M5QyxPes5WU98xKSI-kWmNjPYj_Tg9Y7k94WcJVkkrBuZ73CWUR0IVGmjy3JesihgD7t_YBwqxwR2kVQzEv8WlVqdAN6UC7b2LiZlnIEN7ck52hAtLnM5cCk1l4ET27stIi0k8JCv7_zAsdJDYFkQyoED6K9l4fYlTXFQ-QV7eRYkAgmunL5DetgenTJgbZAzKj6pMiG3QTmcmaUWCM-pWTIK0HeQZfiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا روز دوشنبه ۲۱ اردیبهشت گفت پاسخ تهران به طرح پیشنهادی صلح آمریکا احمقانه بوده است و او از ادامه جنگ و فشار بر ایران خسته نمی‌شود.
ترامپ در یک برنامه عمومی در کاخ سفید و در پاسخ به پرسش‌های خبرنگاران درباره طولانی شدن مسدودیت تنگه هرمز گفت: «احمق‌ها نمی‌خواستند قبول کنند. فکر می‌کردند من خسته می‌شوم یا حوصله‌ام سر می‌رود یا تحت فشار قرار می‌گیرم اما هیچ فشاری وجود ندارد.  ما به یک پیروزی کامل خواهیم رسید.»
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا روز دوشنبه ۲۱ اردیبهشت، در پاسخ به پرسش خبرنگاران درباره آنچه او تغییر رژیم در ایران خوانده بود گفت: «در ایران میانه‌رو و دیوانه‌ها را دارید. دیوانه‌ها می‌خواهند تا آخر بجنگند.»
رئیس جمهوری آمریکا گفت جنگ خیلی کوتاهی در پیش خواهد بود. ترامپ تاکید کرد که میانه‌روها در جمهوری اسلامی از دیوانه‌ها می‌ترسند.
دونالد ترامپ از پایان هفته سوم جنگ می‌گوید با توجه به کشته شدن دو صف اول رهبران جمهوری اسلامی، تغییر رژیم در ایران پیشاپیش روی داده است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، اعلام کرد که در حال بررسی دوباره «پروژه آزادی» در تنگه هرمز است، اما هنوز تصمیم نهایی درباره اجرای آن نگرفته است. او گفت هدایت کشتی‌ها توسط آمریکا در تنگه هرمز تنها بخش کوچکی از یک عملیات نظامی بزرگ‌تر خواهد بود.
ترامپ همچنین درباره مذاکرات با جمهوری اسلامی گفت: «حکومت تسلیم خواهد شد.»
او روز یکشنبه نیز اعلام کرده بود از پاسخ تهران به پیشنهاد آمریکا رضایت ندارد و آن را «کاملا غیرقابل قبول» توصیف کرده بود. همزمان صداوسیمای جمهوری اسلامی اعلام کرد پیشنهاد آمریکا رد شده، زیرا به گفته این رسانه، به معنی «تسلیم کامل رژیم ایران» بوده است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، به فاکس‌نیوز گفت واشینگتن در حال بررسی ازسرگیری عملیاتی برای بازگشایی تنگه هرمز است.
او افزود واشینگتن فشار بر جمهوری اسلامی را تا زمان دستیابی به توافق ادامه خواهد داد.
ترامپ همچنین گفت هنوز تصمیم نهایی درباره ازسرگیری «پروژه آزادی» را نگرفته است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه ۲۱ اردیبهشت‌ماه در گفتگو با سی‌بی‌اس نیوز درباره پاسخ اخیر تهران به پیشنهاد صلح آمریکا گفت جمهوری اسلامی در برنامه هسته‌ای خود امتیازاتی داده، اما این امتیازها «کافی نبوده» و پیشنهاد تهران همچنان «بسیار ضعیف و غیرقابل قبول» است.
@
VahidOOnLine
دونالد ترامپ در واکنش به اظهارات بنیامین نتانیاهو که گفته بود «هیچ‌کس پیش‌بینی کامل و دقیقی» درباره تنگه هرمز نداشت، گفت: «من داشتم. من می‌دانستم آن‌ها تنگه هرمز را بسته‌اند. این تنها سلاحی است که دارند.»
ترامپ افزود آمریکا می‌توانست در چارچوب «پروژه آزادی» این گذرگاه را باز کند و گفت این عملیات می‌تواند از سر گرفته شود و در آن صورت «بسیار شدیدتر» خواهد بود.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری ایالات متحده یک روز پس از مخالفت با پاسخ پیشنهادی جمهوری اسلامی به طرح آمریکا برای پایان جنگ، به فاکس نیوز گفت که ایران فنآوری لازم برای بیرون کشیدن ذخایر اورانیوم غنی‌شده مدفون زیر خاک را ندارد.
ترامپ در این گفتگو تاکید کرد که اورانیوم غنی شده ایران آنچنان در اعماق خاک تاسیسات هسته‌ای دفن شده که آمریکا باید آن را خارج کند.
براساس آخرین گزارش‌های آژانس بین‌المللی انرژی اتمی، ایران دست‌کم ۴۶۰ کیلوگرم اورانیوم با غنای ۶۰ درصد دارد که گمان می‌رود در تاسیسات هسته‌ای اصفهان مدفون شده‌اند. این تاسیسات در جنگ ۱۲ روزه و جنگ اخیر اسرائیل و آمریکا بارها بمباران شدند.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری ایالات متحده در اظهاراتی گفت: «مردم در [ایران] می‌خواهند به خیابان‌ها بروند. آن‌ها هیچ سلاحی ندارند، هیچ تفنگی ندارند.»
او ادامه داد: «فکر می‌کردیم کردها قرار است سلاح بدهند، اما آن‌ها ما را ناامید کردند. کردها فقط می‌گیرند، می‌گیرند، می‌گیرند. در کنگره هم درباره آن‌ها شهرت خوبی دارند و می‌گویند خیلی سخت می‌جنگند، اما نه، وقتی می‌جنگند که پول بگیرند.»
ترامپ گفت: «من از کردها خیلی ناامید شدم، اما ما برخی سلاح‌ها را با مهمات فرستادیم که قرار بود تحویل داده شود، اما آن‌ها آن را نگه داشتند. من گفتم آن‌ها آن را نگه می‌دارند، اما چه می‌دانم؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75408" target="_blank">📅 20:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75406">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RX1GeUjBJqEusrdGkCL5av-MEufZVrXTFR4a2rElINv3TfQquyPaCVNbA9EUwJEnt8AbaNUetnrMXnOXma2Gv0LWpU9rdhmWEtQiU0WeuitMDJNywtig5Jc5QjDvAgJ4gjKLhQjb8K2vprWbQc-nW50qte_W7-VnLp0D3L4_FrpFXABxqMYCdiKEf56-kbV_6jUFHuyzqQeXJyDS9dXi8tZg-Y0m9h150ohqB9SaALqig_Zbc_XFNOK2z8K6QqKx6ZLa_O_xLCGB-uuGio20TFJSTXqdUmoW9ylA8ZT6zBgrfBBDiLnuWjSSuLLN8ZN0FjObQ0m5tIVUvNc2lqRAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G1ZgwHEO0tp0hVoyN-Hxd5MkZJI6rxpG2mSGCTUUun6Csg1ZvKrxRD6fKlhCRFJgxkD0bZJjukX6-gtwHn4PvWGyoZCWqOc45YsoI_Jlm99QGdYwdKc1xBjkblsjdG4ERuNiNoZd2zZ9w1O6bsiJbEBxWWCtGwmoDfHce1WoFjlY-qBD83xH6EDUmeGfk8ZTmvf9Bo9o2R7hT8neLiH1Xh78e2Er1UocBlSQtEA5EmisiNCmXaAfsXnOreQkac8WduHGklHTdpnCOkbcEoid2LgKB6bNfUkOwgsq5wp9EX2vPJ6mMrl1TjpnwdUOfocdUjFbhtft5hY1kNegKzv3Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">AmirKh1982
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/75406" target="_blank">📅 18:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75405">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">قطع اینترنت نه تنها ربطی به تأمین امنیت زیرساخت‌ها ندارد، که «اقدام علیه امنیت ملی» است.
در ۷۲ روز گذشته میلیون‌ها گوشی، کامپیوتر و سرور ایرانی از صدها پچ امنیتی حیاتی محروم ماندند و در معرض انواع نفوذ و هک قرار گرفته‌اند.
در این
#رشتو
بخشی از این آپدیتها را مرور می‌کنم: @
hamedbd_channel
hamedbd
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/75405" target="_blank">📅 18:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75404">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR0PDpgQYl5jBEdscTaST28gCJjWvV6A_7jyMeQYo5JP8cmsknT9wTib8HWWEdr9LNU2r4y8rlo0r3RWcw5aL7pKijyzgp-Y8NfIdt9VPHO_sjb1qxmo4VrDIC-sgVBWcYCfEjY2y9h9UJyDdYZyqorBrf2RraSuy0TZwGYKjM2xgDHVEzv57DmxTjtCHiQgauDa6Bnn53VxMAFAWO5tSTZywAgo7mK_XgNYJjEs9lg0EKvjOmnbW5UlsU1OCiRhfYPRrIDdg-QMLxwnKfpZWRYmp_xqCMGr1Ug3Bgn_aXyExGt3JHZsorkgMWCFqTiuuyCc8iFhcdosMziRAfckeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار روز دوشنبه ۲۱ اردیبهشت‌ماه در بازار آزاد تهران به ۱۸۲ هزار تومان افزایش یافت.
این جهش قیمت کم‌تر از یک روز پس از مخالفت شدید دونالد ترامپ، رئیس جمهوری آمریکا با پاسخ جمهوری اسلامی به طرح پیشنهادی آمریکا برای پایان جنگ روی می‌دهد.
علاوه بر پاسخ منفی ترامپ، بنیامین نتانیاهو هم اعلام کرد که کار اسرائیل با ایران هنوز تمام نشده و ذخایر اورانیوم باید از خاک ایران خارج شود. این اظهار نظرها احتمال برخورد نظامی دوباره را تشدید کرده است.
قیمت هر سکه طلا هم روز دوشنبه در بازار آزاد تهران به ۲۰۰ میلیون تومان رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/75404" target="_blank">📅 18:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75402">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/og3NpYrc4UIDOInEYrNnSgTh45xmNuwl9CiqVGcZGPNiK9KXTDpwIWXcijvlNgN14F0DMnC7XPZCem8i-hkgsU8iXuc8Y7Mtc6vvLOf6WgEEZmzDAiD_sGCayNbParmn07mOyX8Hx81sSLym-RkZZQwGAwyZwDGQFOg6XZRQUUF35C9_AG5N5wviV6e8u3hAo3sKHlOWepZ9Q_H2pNtl65OELtSNdTMvbl4Khog5_SmbzL_829ZHqjhViltPHAnFlmR8_-7du2k87kc6DVvVl7uo9znTeMAt9BNGLdPr6ZingPDD4PYCrUZhWGJ9KSeRaA3i5KZFeGIlPtNGmvqJzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qq2kDK5uM8pizcDEWUly37ezHt1o9rBxRlmp8k34VKDxjQ_3M8Ft7qtWUrBAx_YF-cVhyy3iOQFhqCk2QbNameVVbBUIqTo9Cq2WC4BRw7CfHl12CQr6eTt5w3GtprMEzs-ydPv8StIIzfIiAk0I5ziSWFnz_4sPTmGdf-co0J0wcK0xY23T7A514OoBDiKW8yMDB8v_9fW5JLQI8TQczrHzb8hYQNG7uqcxTaa8ENun1uj_F3OkLukSAdG2Syl7li0KX5BwL9zxX23dCb-J58dYOvlRGJqDiWWp-_X2aSOstBiBZy6Uxi5rRDpxM8P7ecfqn86AJlDloBSwZmRwtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😋
💩
«محسن محمدی عراقی» معروف به «محسن اراکی»، عضو مجلس خبرگان رهبری، انتخاب «سید مجتبی خامنه‌ای» به عنوان رهبر سوم جمهوری اسلامی را «کاری الهی» توصیف کرد و مدعی شد در روند این انتخاب «دست هدایت امام زمان» را دیده است.
@
VahidHeadline
«ابوالفضل ظهره‌وند»، عضو کمیسیون امنیت ملی مجلس جمهوری اسلامی، مدعی شد حکومت ایران به ظرفیت‌ها و سلاح‌هایی دست پیدا کرده که «بمب اتم» در مقایسه با آن‌ها «ترقه» محسوب می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/75402" target="_blank">📅 18:07 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75400">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hbs4K4Jtaz3fwk55NW8v0OX1x6w4T4lbQIOn1FTKr6yvEH05niB8ErA_vPiA3RhURF-iFXan1dI9lTHDbU3KvNbKMGVvSpLsfhLV_flQyRjfypmm_Cm8EBR7YzsHXU00muCoYFzjRxgApY1ZX5fx1u7yr2JMdUmfZ0sGsauWcH2kmAdmEyEzHIJ4-7G0-yvve-HiJCtm11dkUaRa7vP8nYudUw4cnL0c4Ys8qyzVVDWHydyrLng8K0bNACMeAaw243-_3KAuSbwIJ0WheE31jBFI6w9pLYmnkPaNp3hXr6ejYA_U3cexEWSHc71YTdQELYo-4xoW6TX5xZ2p9e1qLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JrDdOP-klWHSar__4DaK-8H60DfAVMOwkwa516nuvcX42K7AaVuI45a-tIFPlNKIsdpItMwXRZOn6pT1uikFwYsO_PN5L2iGrmFPxyJrlExgBQiBP2Y9GYLTcH-g8sPAvo21UBWHbkyaXZQNtzEnce4EQKUKXvLyyx2otJynlkVxVY3yteX-g5lX4KlD1kR-ItlGItlyJpS2GYnwL79KkCcMgidXwh2MwElHI8bL-GUgDWCyA_8MkYVRoSZfRsiH0vCRNa4OXnnKYoeri_XNIJPlo-8Edxp0fvnDN5nDPNwwDqxKCmZMrOsHsy7hiK93lzn7jt_pqDDJHlkZywqktQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نخست‌وزیر بریتانیا تاکید کرد که از جنگ ایران حمایت نمی‌کند و افزود که شهروندان این کشور نگران افزایش قیمت بنزین و تاثیرات اقتصادی آن هستند.
کی‌یر استارمر تاکید کرد کشورهای دیگر می خواستند بریتانیا را جنگ ایران بکشانند اما او هرگز این کار را نخواهد کرد.
@
VahidOOnLine
دولت بریتانیا روز دوشنبه، ۲۱ اردیبهشت، ۱۲ فرد حقیقی و حقوقی مرتبط با حکومت ایران را تحریم کرد.
به گزارش خبرگزاری رویترز، این افراد به «مشارکت در اعمال خصمانه» علیه بریتانیا و چند کشور دیگر متهم شده‌اند.
در بیانیه رسمی دولت بریتانیا، از جمله این اعمال خصمانه به «طراحی حمله و ارائه خدمات مالی به گروه‌هایی که در پی بی‌ثبات کردن بریتانیا و دیگر کشورها هستند» اشاره شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/75400" target="_blank">📅 18:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75399">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bK4YvNPIbRx91D98dzAireXC1yGkqCNZzhX0PSmmyYi_MXdKc3ZcwPDdas0XKz7e0B4gR1WJ9xk3mTMNmrB4eqG4BUjydewna6ieqELwQyOkCTNPrQ5-SpZkO0VOzq6LsdDXKmQJGKbIHDRT-WQUXsvn2UqhyZWjcc6tZxb7Db9ATORR5hk__kLJd9BJ_vk8rI6TGA6URVgfW1tCnDJ0zPX0FUcxKp1enIC_Kiie_NPnxDrKGRRL4ReHAqDBIcBxp-yoGLFI3gFMnqyAM48wTQSYii2WSG8v9tpC8_x--7x7JUFFpHdkjOjbyszJeoplCx2kj2pe_WBz_1mLCrdxwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدعلی جعفری، فرمانده قرارگاه «بقیه‌الله» سپاه پاسداران، گفت: «تا زمانی که جنگ در همه جبهه‌ها پایان نیابد، تحریم‌ها برداشته نشود، پول‌های بلوکه‌شده آزاد نشود، خسارت‌های ناشی از جنگ جبران نشود و حق حاکمیت جمهوری اسلامی بر تنگه هرمز به رسمیت شناخته نشود، هیچ مذاکره دیگری در کار نیست.»
او افزود که با این سطح از بی‌اعتمادی به آمریکا، طبیعی است تیم مذاکره‌کننده با هدایت کلیت نظام، شروطی را مشخص کند که همه حقوق مسلم جمهوری اسلامی را تامین کند و این شروط «حداقل انتظارات» ما است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/VahidOnline/75399" target="_blank">📅 18:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75396">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MD0DELxNyJjIo6UG9fhZnOAqC1lGDcuwk126PDJ5K4wtOQdKCZG0tRSO2CvEWHFCMVNXcW8-AFMUMCqZWeNpmOSVDjL9mYOMkrpxZUHxPJKrQFKtlqYRzErQM2LRl3qrvFfcy_NlfkKU9gOI-SngZCH0pjCEI5yUZQW_TjKO7jfL_iyjoJL_7L6zPRLrBZZ9f1KbEhBwWLdVaeEvXVo3w8VEJs8w2U8b8dIDGYawGEY6NTFBJW39u4-a2QGMAyo7ArF4wr8dYq80HBGJfzOpGGm1wb9E9d-4ExeAdZyg-wi1kJXtgQm-OFL_N-oqPcYC6LrlPKcdKlyh4S0rlcOCiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VAGAwFAJDno8nlGPPApSHxCTeUYW4l7YulX4U6bKSts8WVPwT2vtIXUYc1njc3k6Y3TLZx_gd5hoZY87_xihzEKCiUs16LNos3KEUSgLM_IgCY_RcH4hbXIx1vjCQ3Pf5YctdabffyvabvZtRhBEnCJ9yM0lq7VZSaJjHMOxfKgKGNVOLHksCo3wtZeZSpLDdjYnYAsyTYmQohdblirffpG3LZCaDebuzm7tkhAkbDx2JMzT_PMjYGy1Ipiy9T5S-K3VE-cWq4lV34hwTafuJqzXkofSsjGXhClH3YTnJVWNOH0q6EacVXI72TdctcBoDjln6qPMjBApt0so5nSk1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b8603029cf.mp4?token=vCjcVFasnVNL3lwwc4PbtrjlyhWZliRe4D0B3v-tF7VHmTUTOD9U8ASl3LSN0GHOJsO_nvcTUYHIRmF5x_YI6PUQKGL57VKJB2S92NxGhmrX0Op3s286oz9q-RBfnivtAnGnP-Z0QUFyWgMA4dRs0QltB7awsWn7i_njCfnAMAKN73dkjwc-ehtiRnbDpvl6fMzV0a99nL4eGe3b55GT5urepgwTBz0IRatfgMyhrK5vlzLxb8QvIIRwBCkMPIHrll3CKgVTB-I1diLDOYh3QE6FvZqTaMqCLJcHV7E3IMQT6bpTwjIRdcnU_DMGxN-4d3qIsQhsk0o4zemaY5i3gA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b8603029cf.mp4?token=vCjcVFasnVNL3lwwc4PbtrjlyhWZliRe4D0B3v-tF7VHmTUTOD9U8ASl3LSN0GHOJsO_nvcTUYHIRmF5x_YI6PUQKGL57VKJB2S92NxGhmrX0Op3s286oz9q-RBfnivtAnGnP-Z0QUFyWgMA4dRs0QltB7awsWn7i_njCfnAMAKN73dkjwc-ehtiRnbDpvl6fMzV0a99nL4eGe3b55GT5urepgwTBz0IRatfgMyhrK5vlzLxb8QvIIRwBCkMPIHrll3CKgVTB-I1diLDOYh3QE6FvZqTaMqCLJcHV7E3IMQT6bpTwjIRdcnU_DMGxN-4d3qIsQhsk0o4zemaY5i3gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«اسماعیل بقایی»، سخنگوی وزارت امور خارجه جمهوری اسلامی، در نشست خبری روز دوشنبه ۲۱اردیبهشت۱۴۰۵ گفت در شرایط کنونی اولویت تهران «پایان جنگ» است و نه تصمیم‌گیری درباره آینده برنامه هسته‌ای یا ذخایر اورانیوم ایران.
او در بخشی از صحبت‌هایش بدون نام بردن از دولت یا فرد خاصی نیز گفت: «هنوز با کسانی که علیه ما تجاوز مرتکب شدند تسویه حساب نکرده‌ایم.»
بقایی در واکنش به اظهارات «ولادیمیر پوتین» درباره آمادگی روسیه برای انتقال ذخایر اورانیوم ایران گفت: «در مرحله کنونی تمرکز ما بر پایان جنگ است. این که بعدا در مورد موضوع هسته‌ای، مواد غنی شده ایران و مباحث مرتبط با غنی‌سازی چه تصمیمی گرفته شود و چه گزینه‌هایی را مد نظر قرار دهیم، موضوعاتی هستند که وقتی زمانش برسد حتما در موردش صحبت خواهیم کرد.»
او همچنین درباره روابط تهران و پکن گفت جمهوری اسلامی با چین «ارتباط مستمر» دارد و گفت: «چینی‌ها به خوبی از مواضع ما آگاه هستند.» بقایی مدعی شد چین نیز مانند جمهوری اسلامی، اقدامات آمریکا را بخشی از روند «تشدید یک‌جانبه‌گرایی» می‌داند.
سخنگوی وزارت خارجه جمهوری اسلامی در بخش دیگری از سخنانش، آمریکا را «بزرگترین تهدید کننده صلح و امنیت بین‌المللی» توصیف کرد و گفت: «جمهوری اسلامی ایران ثابت کرده قدرت مسوولیت‌پذیری در منطقه است. ما قلدر نیستیم، بلکه قلدر ستیز هستیم.»
اسماعیل بقایی با اشاره به حملات آمریکا و اسراییل علیه جمهوری اسلامی گفت: «حمله به یک کشور، از بین بردن زیرساخت‌های آن، ترور رهبر و شهروندان یک کشور، مصداق عمل مسئولانه نیست؟»
او همچنین در واکنش به انتقادهای «دونالد ترامپ» از طرح پیشنهادی جمهوری اسلامی، از مواضع تهران دفاع کرد و گفت: «ما امتیازی نخواستیم. تنها چیزی که مطالبه کردیم حقوق مشروع ایران است.»
بقایی در واکنش به صحبت‌های رییس جمهوری آمریکا گفت: «قضاوت را به مردم واگذار می‌کنم که آیا مطالبه ایران برای خاتمه جنگ در منطقه، توقف راهزنی دریایی علیه کشتی‌های ایران، آزاد شدن دارایی‌های متعلق به مردم ایران که سال‌هاست به ناحق محبوس شده، زیاده‌خواهانه است؟»
او همچنین گفت: «هر آنچه که ما در طرح پیشنهاد کردیم معقول و سخاوتمندانه بود و برای خیر منطقه و جهان است.»
سخنگوی وزارت خارجه همچنین مدعی شد که این وزارتخانه، از هر تصمیمی که از سوی نهادهای نظامی مانند سپاه پاسداران برای «تنگه هرمز» گرفته شود اطاعت می‌کند.
@
VahidHeadline
گزارش ایسنا:
isna.ir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/VahidOnline/75396" target="_blank">📅 18:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75395">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6ajNSIStIVP0hCKQTNjKWWGXG03ksCPu_UVjnPpoqHaeV5XGoKDiwDm4AAY3CO-fdO8R_cdhXo8fLPzgHrJV7nFYUqyjzwzmPBVEMquaveUma2CcJeKfr9Kx0tqUSBEth4VB_VNznN7NDfOoT2GSqxdLUmhdNEj-OVHoSAq3qu8mPy_gZTtFCMnX4j_NGLCCyU7AEW7qkFkvSVX5DiIZ-LsaRY0ndomsNDA1RIxJR5qrKOO0YZct0UkGJPBTT8IyPRhZjiTIANUegiTqjXjMffPO0I55MlBsfSaYXHWnsb03FXEp-xxsTwdq9_3145W6koW6uK3TwwlaNzglu97Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار تصاویر ماهواره‌ای که نشان‌دهنده نشت احتمالی نفت در محدوده‌ای در نزدیکی جزیره خارگ است، سازمان حفاظت محیط زیست ایران می‌گوید: «منشا آلودگی مشاهده‌ شده در اطراف جزیره خارگ ناشی از تخلیه آب توازن آلوده یک نفتکش آسیب‌دیده بوده است.»
این نهاد گفت: «هیچ‌گونه نشت نفت از خطوط لوله، تاسیسات پایانه‌های نفتی و یا سکوهای متعلق به شرکت نفت فلات قاره ایران در جزیره خارگ مشاهده یا گزارش نشده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/VahidOnline/75395" target="_blank">📅 18:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75394">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FnCPvZVQzTABHiXPztMpIk9Gn4wSku3YRTF7_Y294wE97R6Bc71hR455sjT0aJ0tJLiBMo2IICeJwCScJesTiU5ETYnG73IYHGrJ8WklJltPN9dD4KcK79o8wnePiLDrFEBruejsOtPHnwWdgj8ogsxlFvE8fadl-ILFE2dDRD9YpViHOuzEQBLTTiitavLnT0jucudwcochbikm7tfFW2w-3XX_lNPAJKBkpOlyQpoogvxSbYruub4TWrhcnJXpsVGMVIR1eoqPFXhswFJwD7bu5FY-JR7UvSwPa1AbOVANLpDHFZpJ4DXSIOkFDooQc9c1BWvbiA142eVqoS3Z7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
گزارش سی‌ان‌ان از اینترنت طبقاتی؛ «فکر کن با بدبختی وارد اینترنت می‌شوی و می‌بینی کسانی که دسترسی بدون محدودیت دارند طوری رفتار می‌کنند که انگار همه‌چیز عادی است»
♦️
سی‌ان‌ان در گزارشی میدانی با اشاره قطع اینترنت و رواج اینترنت طبقاتی در ایران می‌نویسد، قطع اینترنت در ایران اکنون بیش از دو ماه ادامه داشته و طولانی‌ترین اختلال ثبت‌شده تاکنون به‌شمار می‌رود.
برای میلیون‌ها نفری که زندگی و درآمدشان به اینترنت وابسته است، این وضعیت ویرانگر بوده است. فراز، ساکن ۳۸ ساله تهران، به سی‌ان‌ان گفت: «تصور کنید با بیکاری و تورم دیوانه‌کننده دست‌وپنجه نرم می‌کنید و به ترتیبی موفق می‌شوید ۵۰۰ هزار تا یک میلیون تومان جور کنید، فقط برای خرید چند گیگابایت وی‌پی‌ان تا بتوانید وارد اکس یا پلتفرم‌های دیگر شوید، خبرها را ببینید و صدایی داشته باشید.»
او افزود: «بعد وسط همه این استرس و خشم، وقتی بالاخره موفق می‌شوی اکس یا تلگرام را باز کنی، می‌بینی کسانی که دسترسی بدون محدودیت دارند طوری رفتار می‌کنند که انگار همه‌چیز عادی است؛ واقعا مثل مشت به سینه آدم می‌ماند.»
متوسط حقوق ماهانه در ایران بین ۲۰ تا ۳۵ میلیون تومان برآورد می‌شود. سی‌ان‌ان می‌نویسد، اینترنت پرو، شکاف عظیم میان فقیر و غنی را عمیق‌تر کرده است.
وب‌سایت «خبرآنلاین» نوشت این طرح «جامعه ایران را به دو طبقه متمایز تقسیم کرده است: نخبگان دیجیتال که از اینترنت سریع و بدون فیلتر برای تجارت، آموزش و ارتباطات بهره‌مندند، و رعایای دیجیتال که در محدودیت شدید، سرعت پایین و هزینه‌های سنگین بازار سیاه وی‌پی‌ان گرفتار شده‌اند.»
قیمت وی‌پی‌ان‌های بازار سیاه به‌شدت افزایش یافته و بر اساس اعلام سازمان «فعالان حقوق بشر در ایران» مستقر در خارج از کشور، قطع اینترنت طی دو ماه گذشته حدود ۱.۸ میلیارد دلار به ایرانیان خسارت زده است؛ رقمی که با برآورد اتاق بازرگانی ایران نیز همخوانی دارد.
روزنامه اطلاعات نوشت: «قطع اینترنت ــ که خود منبع درآمد شمار بسیار زیادی از کسب‌وکارهای مجازی بود ــ وضعیت بحرانی و پیچیده‌ای ایجاد کرده است.»گزارش‌های داخل ایران نشان می‌دهد «اینترنت پرو» از طریق «فهرست سفید» در سطح اپراتورهای مخابراتی و بر پایه «سیم‌کارت‌های سفید» عمل می‌کند؛ یعنی برخی سیم‌کارت‌ها، حساب‌های موبایل یا نهادها از سیستم فیلترینگ کشور مستثنا می‌شوند.
برخلاف وی‌پی‌ان که با رمزگذاری ترافیک اینترنت سانسور را دور می‌زند، «اینترنت پرو» ظاهرا کاربران تاییدشده را از مسیرهایی با محدودیت کمتر عبور می‌دهد. گفته می‌شود دارندگان سیم‌کارت سفید همچنان به اینترنت جهانی کامل دسترسی دارند.
بر اساس گزارش‌ها، هزینه اینترنت پرو برای بسته سالانه ۵۰ گیگابایتی حدود دو میلیون تومان است، علاوه بر هزینه فعال‌سازی ۲.۸ میلیون تومانی و حدود ۴۰ هزار تومان برای هر گیگابایت اضافی. در مقابل، اینترنت عادی ــ که اکنون به‌شدت محدود شده ــ هر گیگابایت حدود ۸ هزار تومان هزینه دارد و همین باعث شده بسیاری ناچار به استفاده از وی‌پی‌ان شوند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/75394" target="_blank">📅 18:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75393">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xqn4xYi6F-aYceOFkGRx6HMVe5zEF4dbyMeNeSgGicBpAKqMJzDcAxpEFQkoI0qWB0k9SKPhuLMNWqqOgtkNSsBXtLyX0A2aWghLOTwMyzwNaOZHqY9DzkSWW9pEjszXdlfafyQ3CD7HAhzBQhZq0cfYTjXLNS7bIyeRnXuHlBHak9CD6W0tdlK2Gx9p42wVCmpwHhNHb7RukmjjZAtzIwn9J4pwnNPISH83I3O_nFKi1va_An3tYxrYWZXr8hYUptkDhU1b0sUT082GIzqFLuryr1ccgY-jMJ1TejqDDc0NErbUQRAgDQcrKuwRMcwZD3G9Gf8L-vllMVGkzvPDcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی، صبح دوشنبه، ۲۱ اردیبهشت از اجرای حکم اعدام عرفان شکورزاده، زندانی سیاسی، با اتهام «همکاری با سرویس‌های اطلاعاتی آمریکا و اسرائیل» خبر داد.
شکورزاده بهمن‌ماه ۱۴۰۳ از سوی اطلاعات سپاه با اتهام «جاسوسی و همکاری با کشورهای متخاصم» بازداشت و به اعدام محکوم شد و حکم صادر شده علیه او به‌تازگی در دیوان عالی کشور تایید شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/75393" target="_blank">📅 09:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75391">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rq59BiAXX57r_XqU34xClhcOVLBUDPIMVmfV5jLftKwFU1ij9qKcsp6Kg1qVNY7g4DNK1jCQctheYozSx5P3617H5zJ8s4q0VovLPz9FRCgM9JG3kkq3Y_KbQKbeKU24KcvjJWHhfG8nQLY-KK4N81Ioj3g_WttnG2Z76VVhAUNQM7Uis4krUmF0Kp7sChdghEwBE43JxL0ofAzehiAUFByvPYXFT4Ju3CT-krTFRBZW4OteZ3yGcpv1HfJVoRhpk_B3uWVPgFbiFIg4_JfAFs_JHwYRI-NX89aLkjFEsCu_ijXoafJ31si8H7PCUQ-r7rQDuPnZaBRbl1vpZzfGxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IHrjQ6j23nu1B5KiThqPDiL4owXDrsBfGKF9sHdYuSIm1MrviIUrpiWVsTrUwLOZj0iZsQ3zdzrQQ5lwHhTgXR39FrSXDlYHC8HRZVt-3LRzSO3YUh4SlyU_E85holCTOI9W_dYxxXxk1xJdEAbr93J4Gt7U_z8-RdZ7Aw_C13WJcrwIumO1tmpR8D4NSjFj0O3Jrq3x2gcYvdy_F9Mxm-Y8beez4SboDMsIsJaqLRz8A-Z8v-8USWmL1ns1AUefRLXBo0TZjJBjggNdqmA9Lbawrq6UFDLcXVmyO4cCkyFYjA_Z-vj6EH12Oyz2ddZ8KBp-9kPXZxA2nVsWaXKaAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آکسیوس
: پرزیدنت ترامپ روز یکشنبه در یک تماس تلفنی کوتاه به آکسیوس گفت که پاسخ ایران به تازه‌ترین پیش‌نویس توافق برای پایان دادن به جنگ را رد خواهد کرد.
ترامپ اندکی پس از این تماس، در پستی در تروث سوشال، پاسخ ایران را «کاملاً غیرقابل قبول!» خواند.
ترامپ به آکسیوس گفت روز یکشنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، صحبت کرده و در میان مسائل دیگر، درباره پاسخ ایران نیز گفت‌وگو داشته است.
او درباره نتانیاهو گفت: «تماس بسیار خوبی بود. رابطه خوبی داریم.» اما افزود که مذاکرات ایران «مسئله من است، نه مسئله دیگران.»
ترامپ در این مصاحبه کوتاه روشن نکرد که آیا قصد دارد مذاکرات را ادامه دهد یا احتمالاً گزینه اقدام نظامی را در پیش بگیرد.
سناتور لیندسی گراهام، جمهوری‌خواه از کارولینای جنوبی، در ایکس نوشت که ترامپ اکنون باید اقدام نظامی را در نظر بگیرد؛ موضعی که گراهام در سراسر آتش‌بس یک‌ماهه بارها تکرار کرده است.
او نوشت: «با توجه به حملات مداوم آن‌ها به کشتیرانی بین‌المللی، حملات پیوسته به متحدان ما در خاورمیانه، و اکنون پاسخ کاملاً غیرقابل قبول به پیشنهاد دیپلماتیک آمریکا، به نظر من زمان آن رسیده که تغییر مسیر را در نظر بگیریم.»
گراهام نوشت: «پروژه آزادی پلاس همین حالا خیلی خوب به نظر می‌رسد»؛ اشاره‌ای به عملیات دریایی برای هدایت کشتی‌ها از تنگه هرمز که ترامپ پس از کمتر از ۴۸ ساعت به‌طور ناگهانی آن را متوقف کرد.
@VahidOOnLine
خبرگزاری تسنیم، رسانه وابسته به سپاه پاسداران، روز یکشنبه، ۲۰ اردیبهشت‌ماه، به نقل از «یک منبع مطلع» در واکنش به پیام ترامپ مبنی بر «کاملا غیرقابل قبول» بودن پاسخ تهران به پیشنهاد واشنگتن، نوشت: «همین الان واکنش به اصطلاح رئیس‌جمهور آمریکا را به پاسخ ایران دیدیم. هیچ اهمیتی ندارد؛ کسی در ایران برای خوشایند ترامپ طرح نمی‌نویسد. تیم مذاکره‌کننده فقط برای حق ملت ایران باید طرح بنویسد و وقتی ترامپ از آن راضی نباشد، قاعدتا بهتر است». تسنیم نوشت: «ترامپ کلا واقعیت را دوست ندارد؛ به همین دلیل مدام از ایران شکست می‌خورد».
@VahidOOnLine
خبرگزاری صداوسیما گزارش داد طرح تهران که ترامپ آن را «غیرقابل قبول» خواند، بر ضرورت پرداخت خسارت‌های جنگ توسط آمریکا و حاکمیت جمهوری اسلامی بر تنگه هرمز تاکید دارد
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75391" target="_blank">📅 00:44 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75390">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OSKt_IDCXi2njsUqIjBYewNmoilVn0IoJg51Laj-egBSpOozDTNH9LIaXrletyk90_iaQWW9kMsQ6IzINNgAoVLb6JQu-MjCCTxuECTemh4JHI6z6KryMhWWvvcVzsqRIZyStfDAOxjgKNMi2tsn2ZpqTyi5C7NgBxJ8TxfCo-goDpX7pc_3GKqK2yAYWk-1oN4_ucRYsDzew0ufyfTcNMthV6y4dqphkeReOvuA6x1sXStDxPfOOhvPBEwiMJ5-cRsnX0zewxIBcmIPagp7F9qfgWUmeJQx8OToyFQWc8sd26RdV-9iJ_BiYwvd9bTUzhFpPXrs7aKRTn8SkHGJDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ پاسخ جمهوری اسلامی را رد کرد
پست ترامپ، ترجمه ماشین:
همین حالا پاسخ به‌اصطلاح «نمایندگان» ایران را خواندم. از آن خوشم نیامد — کاملاً غیرقابل‌قبول است! از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/75390" target="_blank">📅 23:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75389">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eeB4GhGz_uUG1UHCHwL80FFI5_8TP0XrR2ERwowykdT18pTXBcR5UqeJ0eSFLTx-T4PnRxxG6HV8m2a8lhNwn-FecvhXR6YcxLiD2-PhJ86rNpO4p4wEJskrKAxQR77QiF3tGF7a4WIwBRe0g9EsRwwDt-CEfSQyzzay1Vspa-cZU11RUdCqvRIk-q2RVd-63TiHVxtswbqb9t6JUxkEODmouUqtUBdCEDFITP94xMX0tqNbJCVclfTL2C5PxqEbOWm_B6zXlK-zawSI61yNjabQjg_fWNpQgAhFk41GaiQLN2G9Ike4n16HzOXf6nKDTHZ4YqfPRHOEQBESqymHUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال، شامگاه یکشنبه ۲۰ اردیبهشت ماه، به نقل از منابعی آگاه، جزئیاتی از پاسخ ایران به پیشنهاد صلح آمریکا را منتشر کرد.
به گزارش این روزنامه، پاسخ ایران که از طریق پاکستان به‌عنوان میانجی به واشنگتن منتقل شده، همچنان اختلاف‌های مهمی میان دو طرف باقی گذاشته است.
به گفته منابع وال‌استریت ژورنال، تهران حاضر نشده از پیش درباره سرنوشت برنامه هسته‌ای خود و ذخایر اورانیوم با غنای بالا تعهد بدهد.
ایران پیشنهاد کرده مسائل هسته‌ای طی ۳۰ روز آینده مورد مذاکره قرار گیرد.
مقامام‌های ایران همچنین برای رقیق‌سازی بخشی از اورانیوم غنی‌شده و انتقال بخش دیگری از آن به یک کشور ثالث اعلام آمادگی کرده‌اند.
وال‌استریت ژورنال گزارش داد تهران با برچیدن تاسیسات هسته‌ای خود مخالفت کرده، اما در عین حال آمادگی‌اش را برای تعلیق غنی‌سازی اورانیوم اعلام کرده است؛ تعلیقی که به گفته این روزنامه، مدت آن کوتاه‌تر از توقف ۲۰ ساله پیشنهادی آمریکا خواهد بود.
بر اساس این گزارش، ایران در پاسخی چندصفحه‌ای به تازه‌ترین پیشنهاد آمریکا برای پایان دادن به جنگ، خواستار پایان درگیری‌ها و لغو محاصره کشتی‌ها و بنادر ایرانی شده و پیشنهاد داده است تنگه هرمز به‌تدریج به روی رفت‌وآمد تجاری باز شود.
وال‌استریت ژورنال نوشت ایران در مقابل، خواستار تضمین‌هایی شده است که اگر مذاکرات شکست بخورد یا آمریکا در آینده از توافق خارج شود، اورانیوم منتقل‌شده دوباره به ایران بازگردانده شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75389" target="_blank">📅 23:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75388">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q76RBGc8OtZbOniSNVe21KXAMlETpynm3J4OzHDWOOX6yy0ICCYiiHpSOsmt7y1bxGa1086_CPs2ru58EGwjcjrpMdIP6R7GfqBr5R3IZcZUu8LV3RdRIhPVfZXUAoA58Rr6IX_tnE__eguKeR8f1z2Fe2YC-SfcN-R9FrMF2PNIRDsCpe__97fal3C-Pj54QpphEfS1AqsNQguLlQMpYJ3kGY83UEFAdv2MbvJdT1RsJkZ6EcAyYWhbHMSr2dSbJyjAznB_3gDVBuNZFaILLhnaVxikNueSICs1S2KqHd-n_GS7NfdWUHrW3MxUUHpfd-lbXVoYjQ2A9a4BcqlZYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران شامگاه یک‌شنبه با اشاره به شنیده شدن فعالیت پدافند هوایی در اندیمشک و شمال دزفول از سرنگونی «پرنده متخاصم دشمن» در اندیمشک خبر دادند.
شهروندان نیز یک‌شنبه ساعت حدود ۱۰ شب از شنیده‌شدن صدای پدافند در این شهر خبر دادند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/75388" target="_blank">📅 23:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75387">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">#دزفول
#اندیمشک
پیام‌های دریافتی از شنیده شدن صدای پدافند:
پیام ساعت ۲۲: دزفول حدود 20 دقیقه صدای پدافند میومد
دزفول وحشتناک صدای پدافند اومد.جدود ساعت نه ونیم
سلام پایگاه چهارم شکاری دزفول از ساعت ۲۱:۳۰ تقریبا یه ریز پدافند فعاله
پدافند پایگاه وحدتی دزفول فعال شده از ساعت ۲۱.۵۰ تا الان ۲۲.۱۷
فعالیت  شدید پدافند در اندیمشک ساعت 22.15
اندیمشک
ساعت 22:19 امشب پدافند فعال شد در حد 30 ثانیه.
یه صدایی میاد انگار پهپاده
سلام، اندیمشک ۲۲:۲۲ دقیقه چند دقیقه ست پدافند ها فعال شدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/75387" target="_blank">📅 22:32 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75386">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vL2g7xyWWPohmwHKCnQEEpvQ3Mhjf74S6_qjWmgOLdoQge_1-em9WGtRXB2eNZoQ0QS3_59HB2h67RB7ZAm01BgYRL1bE6P7xtF2R-Kwl0a2vsUh3cuk_C4wAyJFr7MQ_8FoHHiThU4tPOjlniZg9QSwdYd4e2GsIidcHXeXj-kMkJOICxJAHGT1AEgbDQaySqRay5Cvu3hrcsFbeut7UYvXiiXRg7NezKW7sy3EwOsQtexBFwI1cBhp2tN5PuF1VPlYFCc0LfNePBgtqGBxRbMcMrAOG2vmSL_boiNGgv0P_GqosTYxmr-uuaH_cTZFmi-d1o2fA9-SwJR6m8ldUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: آن‌ها دیگر نخواهند خندید
پست تازه ترامپ پس از آن که جمهوری اسلامی گفت پاسخش را از طریق پاکستان ارسال کرده. ترجمه ماشین:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است؛ «تعویق، تعویق، تعویق!» و سرانجام وقتی باراک حسین اوباما رئیس‌جمهور شد، به گنج رسید. او نه‌تنها با آن‌ها خوب بود، بلکه عالی بود؛ عملاً به طرف آن‌ها رفت، اسرائیل و همه متحدان دیگر را کنار گذاشت و به ایران یک فرصت تازه، بزرگ و بسیار قدرتمند برای ادامه حیات داد.
صدها میلیارد دلار، و ۱.۷ میلیارد دلار پول نقد سبز، که با هواپیما به تهران منتقل شد، مثل هدیه‌ای روی سینی نقره به آن‌ها داده شد. همه بانک‌ها در واشنگتن دی‌سی، ویرجینیا و مریلند خالی شدند. آن‌قدر پول بود که وقتی رسید، اراذل ایرانی نمی‌دانستند با آن چه کار کنند. آن‌ها هرگز چنین پولی ندیده بودند و دیگر هم هرگز نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما پایین آورده شد و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آن‌ها بالاخره بزرگ‌ترین ساده‌لوحِ همه تاریخ را در قالب یک رئیس‌جمهور ضعیف و احمق آمریکایی پیدا کردند. او به‌عنوان «رهبر» ما یک فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
ایرانی‌ها ۴۷ سال ما را سر دوانده‌اند، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای خود کشته‌اند، اعتراضات را نابود کرده‌اند، و اخیراً ۴۲ هزار معترض بی‌گناه و غیرمسلح را از بین برده‌اند و به کشور ما که اکنون دوباره بزرگ شده است، خندیده‌اند. دیگر نخواهند خندید!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75386" target="_blank">📅 21:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75385">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T52uw7iS1ccG_OJiXEbtRNOtE1keQMEMJU0Au9wvRJQ4765qN4SbKIDjDw-lL3F1WrDVqh9N4py2ZSZ8ZoUQilnoQHH-87TwxllRv_kv3opdIoSRQWsj5pqZ55kJEW6nVZf8fawhD0w6WQxVYRu8e-32O7xQleVn-6tktVH0u33_nOSHwsZWctcOoAq80Fs8b_VlAg--hv2EVuPDgdKv1KUyevz_8uUmxFEYnnv2iWlmOSSoRm69_FK4lPQVbQPqwm1vBAqwXggk30AO8I-lOJ8LEBctqYJ_0YckEasuQdaLyRwiwTwYmfirgkkJItuqyyQtLbgyUkIFXsiZepcO1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در بخشی از یک مصاحبه که قرار است ساعاتی دیگر مشروح آن پخش شود، گفت که ذخایر اورانیوم غنی‌شده ایران باید از بین برود تا بتوان گفت جنگ آمریکا و اسرائیل با ایران به پایان رسیده است.
او در بخشی از گفت‌وگو با برنامه «۶۰ دقیقه» شبکه سی‌بی‌اس گفت: «این [جنگ] هنوز تمام نشده است، چون مواد هسته‌ای، اورانیوم غنی‌شده، باید از ایران خارج شود. تاسیسات غنی‌سازی هم که وجود دارد باید برچیده شوند.»
او همچنین گفت: «ایران هنوز از نیروهای نیابتی حمایت و موشک‌ بالستیک تولید می‌کند. بخش عمده‌ای از اینها نابود شده‌اند اما کارهایی باقی است.»
آقای نتانیاهو در پاسخ به این پرسش که این اورانیوم چگونه باید خارج شود، گفت: «وارد می‌شوید و آن را خارج می‌کنید.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/75385" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75384">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iccqqFlMNLqyfFhlbGQzLCBpFjcBjdkF5RZNbC4k9rl3nMlf2Zc3Xi97XxbA8LZs_KFqGMd4szS6r8iqbJp_ucfrO1vFGCkjoGtAigQ4cYRhSTwloqZuzokAAlek9TQpmjw_H0W9bYpmpeS4qOKfzLbiOcG-sZ7HGaNkFI1hByajq01J_3Ro2SeWvM7WVPPJs58UjUYue7J4tLuqrRrwuqd6EpWVyGlGa-IngJyUiiqPwWEU0vTAFn0zeTDAlf_Y8hOqon8vO74frgBXwPveEccu42pSV8eofcJVMF6VdzZZwKxHiqsdZFNtl1wT4nAM3N8kR5FQTsOkXmJj1qFiPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Afkham_minus
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75384" target="_blank">📅 19:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75383">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6jAxjEck4NB59RxNvzi7kqvEBrfjw3ln5xgJMtbW24VznPI5AGd4dpGYXG6LvtiuM0HdMOgDXxrQyfdChDynUAf8TAgt58QZoXNbPph2pb8YlxKov6pARmbqUi1itLkjqLifSG_Rse3iF5bKvxYnelZuF2kCVf84-NFI2p4u3rLlOGTsTz8grWXnIVo1WQukWvTxHvnf1w8XsbT6eVus-2O9VKucBA8uFJGPeWIXkCwWdYIxpGlx-xQNvN8X4ItbReiR5WCDXZMCFBXSgD7h0yGXeNlWRGXcre3TBGSmukXoFFSBKMfp7PVPXWh2pFy3EhPwzzXVX4uv2HIGk86oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رحیم نادعلی، معاون فرهنگی سپاه «محمد رسول‌الله» تهران گفت: «در جشن بزرگ پیوند آسمانی زوج‌های جان‌فدا، خودروهای جیپ جنگی برای جابه‌جایی عروس و دامادها در نظر گرفته شده که با گل‌آرایی، پرچم جمهوری اسلامی و تصاویر رهبری تزئین شده و زوج‌ها در این خودروها در مراسم حضور خواهند یافت.»
او افزود زوج‌های شرکت‌کننده قرار است با «ماشین‌های عروسی به شکل جیپ نظامی» و «خودروهای نظامی گل‌کاری‌شده» در سطح شهر حضور پیدا کنند تا «فضای شهر را به یک شکل هنری و نظامی» درآورند.
به گفته او، هدف این است که نشان داده شود این «زوج‌های جانفدا» جان خود را «زیر پرچم جمهوری اسلامی تقدیم این نظام خواهند کرد» و «از هیچ چیز نمی‌ترسند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75383" target="_blank">📅 19:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75378">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HJfaIrs1MCNtE6Gbl7RquCPoSvyhPK3mWUV-HSBHcs4-0Exy4q9kaqDp-yWzXVvD9eDagpUQfql4y-UVqW9Qee8lnKiefYSu-5md0Mxz0yRwvz1p5uxhhoZkoaLSLJRkl9ZQw2ogv020yqUreNT_CWSrBe1PFqHXrGFU6lpV5rwVAI1NYUC1miO6XXK6cXvXYri71lc36LvdJLIkLVvLBSknbbkZPIQaH8XTykt3ULnroyVJkAVH6hS4pKUeIEztKGrOUduR5i9BeROzZVQc6uASLeJaxcJLekaIC5sLSWQ2qb-jUcXfH46Q5Xc5jAxSHiYk26llkc0BRUHto6408g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sLi93bwkqxwKFd2YYo6Q4lguJJ5TkV41pev_7GR3PKGN376ZM7LT8OzGfPk94-s-vnPLMprsrMTIPGXi3Z2y9oaejaEYoTvpO-nzF-0pGDfMW2Lcn50xRjcw0JIs00AbBx1p3IC_PDDdZgwXMntd_2f56HBMlv7i3aMUMjaJjgDev9Q3nfYPOGEj32mViJfhfMMjAGlUsIecuCuKDbkrHeKZ0QM7dlHtmObNyZuPLKKePzwWwaikX72_l7Okqi0p7qjNJhAugKQawRutnkQTEZBikGmp9z9NBKZk369pQLaJuLOOH9McGgpiLoUoQbrweIhuk_WruZpPrjRb_dUksA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kHtj10EgT9xYL4MMK16HdGmlRdGYgkUxLj4H4YMcVZb6FpIL7S06MRW3p1kbLIE5iDYi_Ut5MDFhuqn9asKWQmAmOF5DbLtaDJYLoJNUMHodS75GAzUO4ToyGqS8l-ZtXBHETJsmHeCZKmBV-NFpNa6_1EgmlGi-w67P8ifn8RNpfXf54vCYpYYFOhSKO5Z58Hm0JNhrtqio2F2CVZJeJ4OW4PUmODFh-AWjfmo_pr5m5PDvsvRco15wSEfxbRRQ_UpUgXtoJxALIbXHy1YlBKsaDCscBMn0dFb9rPsCJxAHSLSCrSnLv_64-a7UFC5cLHFH7J4WCuGd_QmtZ-sXuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/chEgV4NSxSyCVKwlODz4malSud_UE6rjKKPC6Q3-YSi8mrKV4zs2Yt_MeVzsXshb5VhBN10diokxhUcJBl0qsLN8i_cid_o_7PBL36pQjHTzQiEJDu0soz9qGpZzm-Be_0Ixg9Ssjte3ebc7Mdey_6PUx4lcQe9d8T2NMwscFq5tP8w3XROhNk0PrTkxAcgi11g3AiEXO43Mz0IH40NByqpR8Yf39NxJtchh-amK4MrkO8TBeTZyBmnjxy915wl1bYkLqPGy_BbYybIwntMcR_U34UxrYX3kZkQ0D6XFTsiz7UPuTbiwP4hE7OVcOCr-hcAoYTv7GzP5Bvc5OXk3iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mGCmt3g_VplhPaH7E3kGp0n_f0N-NhQwCn_tO53f-AT_6RtNV04fufeGRfYGUo2QAtlSpm9i30P3paEMNNK4sIYr-_UsWNIpY0rtXaOiTHr6-5OCAWOGTE64M2oAEFfGeYYgaL9aQ1Cj6ZXm6NwV3AyrC6j_--qVu82hG93CPQ_bAgyzfAxvASZnKpwukQjOKhIOV9-IrIpUs_unMm6eoCe0Z_FQDh4VkF_npBcafNLqjSLfizUbj_wVjrV_K4DT7IuHmGfKJbtoFJSnCocfe86DVorUcybd7mQ18221GkZ--nAwB1wes5ltBiC-l4PvIJNQeTWDrSn_cpB4GdzysQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا می‌گوید عملیات نظامی در ایران تمام نشده و ارتش ایالات متحده می‌تواند اهداف دیگری را نیز هدف قرار دهد.
دونالد ترامپ در گفت‌وگویی با شریل اتکیسون، مجری آمریکایی، که هفته گذشته ضبط و روز یکشنبه ۲۰ اردیبهشت پخش شده است، در پاسخ به این سوال که آیا عملیات رزمی در ایران تمام شده است، گفت: «نه، من چنین چیزی نگفتم. من گفتم آن‌ها شکست خورده‌اند، اما این به آن معنا نیست که کارشان تمام شده است. ما می‌توانیم به مدت دو هفته بیشتر هم وارد عمل شویم و تک‌تک اهداف را هدف قرار دهیم.»
او با اشاره به این که در حملات آمریکا و اسرائیل طی جنگ اخیر «احتمالا ۷۰ درصد» اهداف مورد اصابت قرار گرفتند، افزود: «ما اهداف دیگری هم داریم که احتمالاً می‌توانیم به آن‌ها حمله کنیم. اما حتی اگر این کار را نکنیم، سال‌ها طول می‌کشد تا آن‌ها دوباره بازسازی شوند.»
به نظر می‌رسد اظهارات آقای ترامپ پیش از ارسال پاسخ ایران به آخرین پیشنهاد آمریکا برای این توافق انجام شده است. هرچند که او پیشنهادات قبلی ایران را رد کرده بود.
رئیس‌جمهور آمریکا در مصاحبه با شریل اتکیسون همچنین دربارهٔ اورانیوم غنی‌شده ایران که در عمق زمین و در تأسیسات هدف قرار گرفته در جنگ ۱۲ روزه سال گذشته مدفون شده‌اند، گفت: «ما در مقطعی آن را به دست خواهیم آورد… ما آنجا را تحت نظارت داریم.»
ترامپ اضافه کرد: «من چیزی به نام نیروی فضایی ایجاد کردم و آن‌ها آنجا را زیر نظر دارند… اگر کسی به آن محل نزدیک شود، ما مطلع خواهیم شد و آن‌ها را نابود خواهیم کرد.»
او بارها اشاره کرده است که توافق با ایران باید شامل تحویل ذخایر اورانیوم غنی‌شده ایران به آمریکا باشد. تهران چنین درخواستی را رد کرده است.
@
VahidHeadline
رئیس‌جمهور آمریکا گفت: «ما نمی‌توانیم اجازه بدهیم ایران سلاح هسته‌ای داشته باشد، چون آنها دیوانه‌اند. نمی‌توانیم اجازه دسترسی هسته‌ای به آنها بدهیم. اوباما این کار را کرد. اگر من توافق هسته‌ای ایران را لغو نکرده بودم، الان سلاح هسته‌ای را داشتند و الان علیه اسرائیل و خاورمیانه و شاید حتی فراتر از آن استفاده می‌کردند. می‌دانید، آنها در واقع موشک‌هایی دارند که دیدید می‌توانند به اروپا برسند.»
از آقای ترامپ سوال شد آیا این درست که عملیات رزمی علیه ایران تمام شده است.
رئیس‌جمهور آمریکا پاسخ داد:«من این را نگفتم. من گفتم آنها شکست خورده‌اند اما این به این معنا نیست که کارشان تمام شده است. ما می‌توانیم دو هفته دیگر هم وارد عمل شویم و هر هدفی را بزنیم. ما اهداف مشخصی داریم که احتمالاً ۷۰ درصد آن‌ها را زده‌ایم اما اهداف دیگری هم هستند که می‌توانیم بزنیم.»
آقای ترامپ گفت حتی اگر هم این کار را نکنیم، بازسازی سال‌های زیادی برای ایران طول می‌کشد.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در گفت‌وگو با سی‌بی‌اس نیوز درباره اورانیوم غنی‌شده در ایران و جنگ علیه جمهوری اسلامی گفت دونالد ترامپ به او گفته می‌خواهد وارد آنجا شود و به نظر او این اقدام از نظر عملی امکان‌پذیر است. او افزود اگر توافقی حاصل شود و بتوان وارد شد و این برنامه را برچید، این بهترین راه خواهد بود.
نتانیاهو از پاسخ به این پرسش که در صورت عدم توافق چه رخ خواهد داد خودداری کرد و گفت برای این موضوع جدول زمانی تعیین نمی‌کند، اما این ماموریت را بسیار مهم دانست.
IranIntl
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/75378" target="_blank">📅 19:20 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75377">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGMPR0j64vfjDo2TV4XUJYcbwW0aGeSTk5ZC0E4jkGQdllnh8X3Ea_1hfHcJ9hYUjPhTNjr9XX7Xmws-Ojfcbq8wnLwEkb4hhc__Xli2jAIkSvr0DYHO58C7CcjHc2N_67nNhadjQJk151IMCHbbnbnBIu_DEf2g5-9ieMK5L74xrkKy_qU48RiYz-s6pFGBj6AMunsveqiUsAxLhT71kni7FBekoFnocSXYc8XyvephgxH4kgmBF8KIjMPFPcrCexR1o411eP4cFmf4k7H6esjmg1SajvPfJzHaJSBWDkwqI1a4ktJWwaSuU8d5roPmsfSn3DWJvc6UFF5N_42dgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایرنا، روز یکشنبه ۲۰ اردیبهشت ۱۴۰۵گزارش داد پاسخ تهران به آخرین طرح پیشنهادی ایالات متحده برای رسیدن به توافق بر سر پایان جنگ، برای پاکستان به عنوان میانجی مذاکرات ارسال شده است.
ایرنا بدون اشاره به جزئیات بیشتر نوشت: «بر اساس طرح پیشنهادی، در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود.»
وب‌سایت اکسیوس و خبرگزاری رویترز، چهارشنبه هفته گذشته گزارش دادند که واشنگتن و تهران به یک «یادداشت تفاهم یک‌صفحه‌ای» برای پایان دادن به جنگ نزدیک شده‌اند.
رویترز نوشته بود در این تفاهم‌نامه حتی به تعلیق فعالیت هسته‌ای ایران یا بازگشایی تنگه هرمز که از سوی سپاه پاسداران بسته شده، اشاره‌ای نشده است.
در مقابل، روزنامه وال‌استریت ژورنال گزارش داده بود که در طرح پیشنهادی آمریکا، تهران باید ثابت کند که به‌دنبال سلاح اتمی نیست، تاسیسات فردو، نطنز و اصفهان را برچیند، فعالیت زیرزمینی هسته‌ای را متوقف کند و همچنین بپذیرد غنی‌سازی را تا ۲۰ سال متوقف کند.
رییس‌جمهور و وزیر خارجه آمریکا روز جمعه گفته بودند جمهوری اسلامی تا پایان همان روز قرار است به پیشنهاد ایالات متحده پاسخ دهد.
@
VahidHeadline
ولی جمهوری اسلامی به جای جمعه، روز بسته شدن بازارها، صبر کرد یکشنبه پاسخ داد که ساعت ۸ شبش به وقت شرق آمریکا بازارهای مالی هفته کاری رو آغاز می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/75377" target="_blank">📅 17:51 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75376">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLRciSX22IupC8xpoPe1w1E8wSP0YsR4fuMP8j7DlGh-jVWirlEouyGrI47zLBjCD_GgiMYGy3GwjHHpZNVvLbCU2XUSEWKcGJ4PAyk4pWM06uD21jWxZP5Tjf7QOecg19uoE1_rWWWj65uFIjceiCvoxJ7EwHSYYwekl7gax2lxtTRo8tWIHyNS0goedpyZaqN8MsjBnpf6IB-R0631E5nem2Vy-TYfhjKEpPXR2KhxfV_wwteXFz6b9W0FosUXH0qOG0Yt1VeyiyESTHkn2KZVOe2YIsn8VAQuix0fUDIhzwawzSeM5u5DK85Bw-fnY6Kbkn1B9zdUPGfFkWbDbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع امارات متحده عربی روز یکشنبه ۲۰ اردیبهشت اعلام کرد که سامانه‌های پدافند هوایی این کشور با موفقیت دو پهپاد پرتاب شده از «ایران» را منهدم کردند.
این وزارتخانه تاکید کرده است که از زمان ««شروع حملات آشکار ایران، پدافند هوایی امارات متحده عربی در مجموع ۵۵۱ موشک بالستیک، ۲۹ موشک کروز و ۲۲۶۵ پهپاد را منهدم کرده است.»
وزارت دفاع امارات همچنین گزارش داده است که از زمان شروع حملات آشکار ایران، تعداد کل جانباختگان نظامی به ۳ نفر رسیده و تلفات غیرنظامی هم ۱۰ نفر از ملیت‌های پاکستانی، نپالی، بنگلادشی، فلسطینی، هندی و مصری است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/75376" target="_blank">📅 17:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75375">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYsfNi5sae107yCQ7ROWBz_FRZopXMuZv4TIcHRPCNGdRyHVQDH14KbCEKherf_B5BnkDQ61j0l-JA1b7s3JNlHITLAVDlQqYPAxBXCRO-zkoZt8OAlOl8je-v5OFXQMQDNOXRti5Kax9Cwpxq3M38ygnXWnjHP2aiy1R3HUzX7_ZWn5MZf2ZriFBMKVDheYf5FxJYNkqjrwBPNKdU4PvXZ-pv0yc5Yp0qqbtqq92O7073IChNIjSb5-mTk7doJhXuLHDFqs5zMyNjWtpWVBQfpJFjHMa3uwkvRssEb9FW9juealf0aKyxWDom3ZX8MT4ySuAb_NiVguvHeQw9Szqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جمهوری اسلامی گفته‌اند علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، با مجتبی خامنه‌ای دیدار کرده و گزارشی از آمادگی نیروهای مسلح، از جمله ارتش، سپاه، نیروی انتظامی، نهادهای امنیتی، مرزبانی، وزارت دفاع و بسیج ارائه داده است.
بر اساس این گزارش‌ها، عبداللهی گفته نیروهای مسلح از نظر روحیه رزمی، آمادگی دفاعی و هجومی، طرح‌های راهبردی و تجهیزات لازم برای مقابله با «دشمنان» در سطح بالایی از آمادگی قرار دارند.
این رسانه‌ها همچنین نوشتند مجتبی خامنه‌ای در این دیدار تدابیر تازه‌ای برای ادامه اقدامات و مقابله با دشمنان ابلاغ کرده است. با وجود انتشار متن این خبر، رسانه‌های جمهوری اسلامی تصویری از این دیدار منتشر نکردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/75375" target="_blank">📅 17:46 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75374">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnDIiUu6__CZLjPJCuHhIExBaSZGuqu7T1yoHovq4wrkyrwRVOKgECaPEBSUQ0GCH6SHjb_WxSbBtB0cWBOZEUIIsgzkGDUhNa85Q4rMqMsZTNXyo92rYstapyEY6UKj4QOeQouuIBCzQ8SdDCtWX2i1n7y7E-dA_6r8hM8rcVQoXKD2SbUtnEDb0Iwy1AgTQKERnLWR2wyAHM7Otf6Wx9RZWQmfwrQDCzPp8isFN0t69VTkU77MSSkB2Qgn9y0Jf1VlhO3fnqjSOOyol8CqCRdDGCPImJBh7NOfRwbbUU2BVi-XKMBa7NzVNnzBV4osG74SRZhxdKrcoQavikifRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران درباره کشتی باری هدف ‌قرارگرفته شده در نزدیکی سواحل قطر، به نقل از منبعی که نامش را فاش نکرد، گزارش داد این کشتی با پرچم آمریکا تردد می‌کرده و متعلق به ایالات متحده بوده است.
سازمان «عملیات تجارت دریایی بریتانیا» (UKMTO) صبح یکشنبه گزارش داد که یک پرتابه به سمت یک کشتی باری  در ۲۳ مایل دریایی (۳۷ کیلومتری) شمال شرقی دوحه شلیک شده است.
بنا بر این گزارش یک آتش‌سوزی کوچک در این کشتی رخ داده که خاموش شده است و تلفات جانی نیز نداشته است.
این خبر در حالی اعلام شده است که مارکو روبیو، وزیر امور خارجه آمریکا روز شنبه با محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر امور خارجه قطر، در میامی دیدار و گفتگو کرد و شراکت دو کشور را برای بازدارندگی در برابر تهدیدات و تقویت ثبات در خاورمیانه حائز اهمیت خواند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/75374" target="_blank">📅 17:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75373">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQZUdsDtjrPs6tZMz71Y1DU6BYR7XZWCawGuZxkmVB_PymrG7Ywi417gBkpgcXAW4whBNE4lgv_JmtIFqG8PSmtpvFhSv0fKcqNC1joi9PvMv-3JQmLYpnpfo05ZmsXK-Tc1dDMuAGs9MRysmPRUKlh91Nekw76AhboZ-ake1Peo9rZrmz5GtSCP9q8qjSYd_WNULgoKR1qVdbp2ffEQqhRYgn-Ijxu--i7n_tKOgddUi6ZfOIcMJ1wYdH3_EXTBnUR8j2HM-o_Z-ZGbT1ZEVSzk0yoZF9xrdQ2hSAgAcwQuTj49BULaPyHFzCTuX22YzoX8z0_RgcUrii7kX9MNKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ‌ ‌ ‌
خبرگزاری فارس می‌گوید «یک نفتکش حمل‌کننده گاز طبیعی مایع متعلق به قطر به نام الخریطیات» با «اجازه ایران» از تنگه هرمز عبور کرده است.
بنابر این گزارش، این نفتکش «روز گذشته در دهانهٔ تنگهٔ هرمز دیده شده بود و پس از آن سامانه موقعیت‌یاب خودکار خود را خاموش کرد.»
به گفته فارس، «این نفتکش که مقصدش پاکستان است، نخستین نفتکش غیرمرتبط با ایران است که از نیروی دریایی سپاه اجازه عبور از تنگه هرمز دریافت کرده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/75373" target="_blank">📅 17:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75372">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQFyilHtnzndsKgNzcqai5pfSrbeHypg8sEz594ZXIOxwCDwe34bX720e-WFGOzotu1wqjaLntIHgaRUiQkFt-xUsgURcGX67URczutYs7ltopoYKit4Y_0D2rhB_jbQhKuJDU8o3Yd8n8tocI_f2GGr4ss0ZeprxP7Kk6JkwU7eQ1tplbL1HvhGjMo1sIO69nukTTAVpY4Rxp3tptauqT-6bfchUjSpvBkSzoWGT-0BpE0a9Vq9XiskdKPm5P6XpvVoXHNREXTxK-Gqmone4ulqOvL7KjJoC-DNkMNC02mIh66cSnujMyQ8DSXVSD-5afcF2CQ04WcFVmSlnVF7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های داخل ایران روز یک‌شنبه به نقل از مدیرعامل شرکت پایانه‌های نفتی ایران هر گونه آلودگی نفتی ناشی از تأسیسات جزیره خارک را تکذیب کردند.
او گفت: «به محض انتشار این اخبار، گروه‌های متخصص اچ‌اس‌ئی و اداره شیمیایی و آزمایشگاه، همه منطقه را پایش کردند اما حتی کوچک‌ترین موردی یافت نشد.»
خبرگزاری رویترز گزارش داده بود که تصاویر ماهواره‌ای ثبت‌شده در روزهای ۱۶ تا ۱۸ اردیبهشت، لکه‌ای بزرگ را در آب‌های اطراف جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، نشان می‌دهد که به گفته کارشناسان با «نشت نفت» سازگار است.
بر اساس این گزارش، لکه‌ای خاکستری و سفیدرنگ در غرب جزیره خارک دیده شده که به گفته یک پژوهشگر «رصدخانه منازعه و محیط زیست»، مساحتی حدود ۴۵ کیلومتر مربع را پوشش می‌دهد.
به گفته عباس اسدروز، «طبق اعلام مرکز بین‌المللی «میمک» به نمایندگی از سازمان بین‌المللی دریانوردی هیچ‌گونه نشتی در زیرساخت‌ها، مخازن ذخیره‌سازی، سیستم‌های اندازه‌گیری، اسکله‌ها، خطوط لوله این منطقه و کشتی‌های در حال بارگیری وجود ندارد.»
اسدروز توضیح نداده است که لکه موجود در تصاویر نشان‌دهنده چه چیزی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/75372" target="_blank">📅 17:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75371">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ab_qWbPVbYEpZ2Z45QwcXDIn1u0GTDUMeIloR9ssF_MX7kmCI1CHjtuF2zTyEvzBlk2307tJZsneyryW0mpQA65LM4KPleOI7q-S0qtrhGQYAdlGSuKWKU0xfvYQ4bR7YFn_C9BD1gtZR9xk4r0TJRrWfbGMwKNgigUSR3sghCrmp89jk02in9BvXFIL1zIq4kkp9qzIN_Fq8fbVxleVvTXnmUK1wPZWjhWzadHVfKwS_GVN8fVVLcN8HKvYblxekuDylkl8LLNfAz-NUVehAWWF3wyrVb9JA-FXanystHDT0ptlzKxxyQpYD1gCYKV_X9ZLQj1wJWnzTAQxVeEnjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «وال‌استریت ژورنال»، اسرائیل در اقدامی بی‌سابقه یک پایگاه نظامی مخفی در بیابان‌های عراق ایجاد کرده است تا از این طریق عملیات هوایی گسترده خود علیه ایران را پشتیبانی کند.
این پایگاه که پیش از آغاز درگیری‌ها و با آگاهی ایالات متحده احداث شده، میزبان نیروهای ویژه اسرائیل و یگان‌های امداد و نجات برای خلبانانی بود که ممکن بود در جریان حملات سرنگون شوند.
طبق گفته مقام‌های آگاه، استقرار این مرکز لجستیک در فاصله ۱۶۰۰ کیلومتری از اسرائیل، نقش کلیدی در مدیریت هزاران حمله هوایی تل‌آویو علیه اهداف نظامی رژیم جمهوری اسلامی در خاک ایران طی هفته‌های اخیر ایفا کرده است.
این گزارش فاش می‌کند که مخفیگاه مذکور در اوایل ماه مارس و پس از گزارش یک چوپان محلی درباره تحرکات مشکوک هلیکوپترها، تا آستانه لو رفتن پیش رفت. در پی این گزارش، ارتش عراق نیروهایی را برای بازرسی به منطقه اعزام کرد، اما نیروهای اسرائیلی با اجرای حملات هوایی سنگین علیه سربازان عراقی، مانع از دسترسی آن‌ها به این سایت سری شدند که در نتیجه آن یک سرباز عراقی کشته و دو نفر مجروح شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/75371" target="_blank">📅 01:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75369">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/laDXz3AKPdUiq9W3aKU3J5vStnDMZSL1lIjNUZdwoxRrgXh5OnNLcyO3X-jsHRYglFG99HH-Lb_4ccn5AJixbptaKGpv2Kw3MoDoWrayK2x7XMreAvyuOcLhXsfvp5TxAW4ezTgqTkWygTshsi5A1ArybrCs8EbV4DuxGbMJ8iOiTO9uMwYChDzaMDgwHKzpUmV1H56LmSg0NStZe2h6AEqKMA-LWqY7ac9PWpPNKLeESrA-GZN38V6s7yOEL5rRYtJRsl0EBBw2IcBfylj50-9VqGu-dbHHH6gEUcK1TC_nVayOfFlNbCOPe5eZc7HpalGIHNX_j3oyVo-4xP1Tdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HkxUcDBqnkydJvQ6cFj6fDPQ4tZJnxuHgz2b2fhHbnNMa3liTBeuXPFJiiUclbZCDcbscpHO9c9OytbBvZcBLRz4e_V-EHJ4Oj3d9ASq9w368BbIyalv164boOH3AzCRvziw5cP4M5Kzp1XlNmUUdFn_zChL9SISjZboYBbGTS5U1TiPmR_veWTMtGonb398byL6jV7DSincRWexlhCMnlxflWbvOvtVzqqT-7sLATIJWz8cjtTXPAl-lqw0Y6aYpdP63FoN06KSrivbRpJG6hczJ2zEt4lbw92Yi8Vj9Tkj4aDMuickDKHarY3Odcwiw2CESGG8eBbQCBmgfL7zzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر ساختگی دیگری که ترامپ در صفحه‌اش منتشر کرده
:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/75369" target="_blank">📅 01:15 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75368">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m2stEpE8gUhUvXG8-nvtH8vjQWYIK3WoljfFwT0Iom0qgNynXEfUC9thIxNRNs8GXM0kmKXUFyi0FByjgehZTScRScMDK3s1NSiiPWRRGSdOVD3YjTtXjA8W2WkALtHllIT9J_QUy17v_rJc5l6ZBJCvWB_eA9WEjJt1rp1JXWZQ8yhrn2wXWlHewN3vIShv1kNOyM44mdupITcfbFsMLE5MB42v8v0CtFpRWBgTbjsu4Vx7csaYR3Rni2lyYOufYgnwrN1qAgRcCcSEYrBxthfIaJoSxO_dRGdM34bBXQ_wxdFKZ19M9jtxDigybjePwunDA-vHaC-z0diUu2TC8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/75368" target="_blank">📅 23:39 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75367">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7nMKbjkbhFnmLoxuEtT8vr8imI9sPUx6v3Oom1eVtND_9Sb7CgPh2B1mKw5J1TWjOQ29DBcu7y9GMLEQghUayusQc0HXp-UVmcN4FubW0PflYHfog8UuPkM2jyMDuyvpT7HZqm2OR3JC1Rw1plKqLjUDmtoT_93Xl5bJknyNq0XDyxYY7okfNHmNgngfKe0VtR9MLVIY1DoJcfeVPyWNabxnCR5R5eF2sCM4TIqKqM0QVROmzAk7FAVJJ9wantPmYSpgj2bOMl7XlYHSjKdcQrvI77tX_1IYql2p6ip1974HwP26i0jC-necPttLAb80H3ou1yHs2DHk5ZTx_XjtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، با اشاره به کابل‌های فیبر نوری عبوری از تنگه هرمز و تهدید به اختلال در اقتصاد دیجیتال جهان در صورت آسیب به این کابل‌ها، خواهان اخذ هزینه از شرکت‌های خارجی و الزام غول‌های فناوری نظیر متا، آمازون و مایکروسافت به فعالیت تحت قوانین جمهوری اسلامی شد.
تسنیم نوشت: «کابل‌های تار نوری زیردریایی عبوری از تنگه هرمز روزانه حامل بیش از ۱۰ تریلیون دلار آمریکا تراکنش مالی (شامل پیام‌های سوئیفت، معاملات بورس و تبادلات ارزی) هستند.»
رسانه وابسته به سپاه در ادامه خواستار «اخذ هزینه مجوز اولیه و تمدید سالانه از شرکت‌های خارجی، الزام غول‌های فناوری (متا، آمازون، مایکروسافت) به فعالیت تحت قوانین جمهوری اسلامی و انحصار تعمیر و نگهداری کابل‌ها از سوی شرکت‌های ایرانی شد.»
فارس، دیگر وابسته به سپاه، نیز در گزارشی نوشت که ده‌ها کابل فیبر نوری زیردریایی که آسیا، اروپا و خاورمیانه را به هم متصل می‌کنند، از گذرگاه تنگه هرمز عبور می‌کنند و تهدید کرد که «هرگونه آسیب به این کابل‌ها می‌تواند اختلالات گسترده‌ای در اینترنت و اقتصاد دیجیتال کشورهای مختلف ایجاد کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/75367" target="_blank">📅 23:38 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75366">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vn-J7_ugnVgqZXwxUlKb-Zcfpt5uBNvc-IjwlolfOeaE6ZSVNqU9k8JvZ7QtMJiLKGkY_OOCr3-zX0PrIQbZap0pZeWWgWKPL3wU4cmywt_WqFb7BPosfHaXXBaP0Tk3NLPNhLwJS7ijXNTUoomJCRwnBHf82NFfCu0It4oiCGiNRqIw4WfY-vXiGA8UocvopKKHHtp3N0BDJuU4Zs81QYhSf27pXw-Rmoqw_wPp0frT8Gdqk9hkDlYE7om9YWAPZ7RM7SZuF0iEr2yuuAO0_PyxXp-6mr8UEomjxtoa4abHq92x6bAdT3-wrZjI48ejsdfAG7x1W0g8GS0D-EjMDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولادیمیر پوتین، رئیس‌جمهور روسیه، روز شنبه ۱۹ اردیبهشت، ساعتی بعد از برپایی رژهٔ «روز پیروزی» در مسکو، گفت که معتقد است جنگ اوکراین در حال اتمام است.
او بدون اشاره به جزئیات بیشتر دربارهٔ این جنگ به خبرنگاران گفت: «فکر می‌کنم این موضوع در حال پایان یافتن است.»
روزنامه فایننشال تایمز روز پنجشنبه گزارش داده بود که رهبران اتحادیه اروپا در حال آماده‌سازی برای مذاکرات احتمالی هستند. وقتی از پوتین پرسیده شد آیا حاضر است با اروپایی‌ها وارد گفت‌وگو شود، او گفت که گزینه ترجیحی‌اش گرهارد شرودر، صدراعظم پیشین آلمان، است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75366" target="_blank">📅 23:37 · 19 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
