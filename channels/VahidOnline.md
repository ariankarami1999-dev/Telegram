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
<img src="https://cdn1.telesco.pe/file/gddkxtyudohLP7c6QKBzZDjoTmIjIADG3JBLnIq4UKzeqMncsqI48oiYtJvMOJYyZGm-oKBvk8Hj5EHi6Z4iP8LfoGX3f7RJIQEBPPS6TmZcEySpBFKk6jPO29x9WYzPxFW8YRu_7EDlJq1BU9TaSXJbdOinkgxqXnQxmlGwrPYmisiNL9zLr9o8-NEOhW2ibc6eQrRqSr-rUrkePJWRSjvWlreQznSPUSglQvsUDBJLiaxRwZuiY8_oOTZLdHCSBTofA-oa4JAUetJ9kAYawE-BoJgtbug2bnbVTisqK5eHd-tOD9S3XCO6vs_9bA-EgFE7hj4a9_EjzfHgvvXcBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 18:45:45</div>
<hr>

<div class="tg-post" id="msg-76653">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=HXALQdecsXl5JTmG5xaUiZ8io1xRFRPWMcRAVTGu8xzkrDXLdLeFNd5LRM1gQHCu_A3h_pyt5-OW9FgBQPTUPXG53HTaW3LdPew_2l0aR_EqP0LTys_1Kol9aC2few78EsPJU5Q4IB551rjyhN6mgpwfya7RxRv9S_63uDTVrjqvQtmcFIwOw-gjzAKyeMitvMs4nmmSNe1v9WCvshuMBElKCcuPYf3Md-5RR-SVRAnL59-aKwmc8Iaq2CHKOVI5968j-otHz81CU4KIzJWJjGtnAFz3__m0BKTVGZ2g00PqOjucWwanE4iadrorBWcbzBYr7HGpMJsKldiR0BB28w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=HXALQdecsXl5JTmG5xaUiZ8io1xRFRPWMcRAVTGu8xzkrDXLdLeFNd5LRM1gQHCu_A3h_pyt5-OW9FgBQPTUPXG53HTaW3LdPew_2l0aR_EqP0LTys_1Kol9aC2few78EsPJU5Q4IB551rjyhN6mgpwfya7RxRv9S_63uDTVrjqvQtmcFIwOw-gjzAKyeMitvMs4nmmSNe1v9WCvshuMBElKCcuPYf3Md-5RR-SVRAnL59-aKwmc8Iaq2CHKOVI5968j-otHz81CU4KIzJWJjGtnAFz3__m0BKTVGZ2g00PqOjucWwanE4iadrorBWcbzBYr7HGpMJsKldiR0BB28w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به  پزشکیان دوباره بیل دادند، اگه شهباز شریف جلوش رو نمی‌گرفت فکر کنم تمام اسلام‌آباد رو درخت می‌کاشت.
NR2OH
مسعود پزشکیان، رئیس‌جمهوری اسلامی ایران، در جریان سفر خود به اسلام‌آباد به همراه شهباز شریف، نخست‌وزیر پاکستان، در مراسم نمادین کاشت نهال دوستی ایران و پاکستان شرکت کرد.
ویدیوی منتشرشده از این مراسم نشان می‌دهد پزشکیان پس از قرار دادن نهال در محل کاشت، همچنان به بیل زدن و ریختن خاک اطراف آن ادامه می‌دهد؛ در حالی که شهباز شریف چندین بار با اشاره دست تلاش می‌کند پایان مراسم را اعلام کند.
در این میان، لبخندهای شهباز شریف و ادامه بیل زدن پزشکیان توجه کاربران شبکه‌های اجتماعی را جلب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/VahidOnline/76653" target="_blank">📅 16:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76652">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQfGnVA4wzod2qFLvT-OUdVPO3KDmxxTj7n5FS3reDZVmGf0pCyZvD4LnknLpleVO5qrC9JOOSzjuiUb5anjK61iM2YWANd1Q8aBo1TOfk4D6NhvALNJc4-SxAnTeFTmzn2Oxd98OxbQDDSJRvPlkdwMM2OpHlltSiQD9aDQtSU-TRCoAd0MWuBBJTN2nh3igVFFYA4Avs5wK9QsrJr7ex_hpraSdnXvmkSx30htM6YK7NhvParBIpXaIct-Rdg3ZvCEzqZ0pKfKaxTFbPJP0u1fxoguWsF8XDGKF5tB5bO8bPHpTSY5xbeGw1d70TJsG624m7ttyjQWwv7B7kf9cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده روز چهارشنبه گفت واشینگتن بر نحوه مصرف دارایی‌های آزاد شده ایران نظارت خواهد کرد و به همین منظور دفتری در دوحه، پایتخت قطر، برای نظارت بر این وجوه تشکیل خواهد شد.
اسکات بسنت در گفت‌وگویی با شبکه خبری سی‌ان‌بی‌سی، تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای خرید مواد غذایی و دارویی از آمریکا استفاده خواهد شد، حتی اگر ایران گفته باشد که نحوه مصرف این منابع را خودش تعیین خواهد کرد.
او بدون ارائه جزئیات درباره سازوکار نظارت بر مصرف این منابع گفت این وجوه توسط وزارت خزانه‌داری آمریکا در خاورمیانه نظارت خواهد شد.
مفام‌های جمهوری اسلامی در روزهای اخیر با رد اظهارات مسئولان آمریکایی گفته‌اند نحوه استفاده از منابع آزاد شده در اختیار تهران است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/VahidOnline/76652" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76651">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9yvLlSBxY1QRrq8p-fDWVJB5-rwtbWXBkVLgOK3sE2568NHkgZfp16K2cZ88dX7AtpIuDv4fROvTIzlYFYo8P_n0u8d2c28mRKQJxyPQj0y5LG3F0n9tOxMSzEbMxwG0ulZvitcmX1_3bbTPRRFcrxB34uhjNTJw0h-M6tejhOxkqvg6FuAbk34Dy-2Zx6v1lcOHtf2_rG3Q2BkpBQeuFm8azRge9OsyP6-_GEe41AiYrE9E5k035fmrp25Fc3WBLgAyZOzgLAHQNHgaxnW3foLJMuGYC1uUjy5KcGMNDpuQ99CTf7_28sZtFKYvZRfdvVKmrTAv3Q1cfdrrS6lPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی اعلام کرد که دسترسی به تاسیسات مورد حمله واقع شده و مواد هسته‌ای صرفا در چارچوب توافق نهایی با آمریکا ممکن خواهد بود.
کاظم غریب‌آبادی روز چهارشنبه در شبکه اجتماعی ایکس با اعلام این که در سوییس هیچ نشستی با رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی «علیرغم درخواست او»، برگزار نشد، نوشت: «هیچ برنامه‌ای نیز برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته‌ای وجود ندارد.»
او افزود: «این مباحث صرفا در چارچوب توافق نهایی و در نتیجه اقدام عملی طرف مقابل در خاتمه تمامی تحریم‌ها و... بررسی و تعیین تکلیف خواهند شد.»
پیشتر گروسی اعلام کرده بود که سایت‌های غنی‌سازی هسته‌ای جمهوری اسلامی توسط بازرسان آژانس مورد بازدید قرار خواهند گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/VahidOnline/76651" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76650">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeeFagyyGtTyB1ikNWlrwxA5AQ-tlTBiwzdBF5I3YjC9YzpEQIxoXWfFU48PdCyNYWzQ0J8DdkczIlLwm36uhws3uTPuX9xueQUZxG8-U9rwp2z3LaUIoMGiBNvyl2_r9rbY6__eJqLpl-RKCv9H8qEHZFxGjY0MHdsNG-bYVdWOUq_Drrsl77YwHoAlHxVTOrxQFfewua38BJOFY69y27NIWo-_qyGBIbI0i3ARuuYmdB4YAL5tf61eRaX6nkOF38VZBU_u6gSuB4HVvgiL6DVYwedb3KZEWo6zhQ109BCIHd8_Xe6SbFWcIL15VCTkbe6YHGGx90qnnVc1wUzaqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، روز چهارشنبه در دیدار با رئیس امارات متحده عربی در ابوظبی درباره تفاهم‌نامه ایالات متحده با ایران گفت‌وگو کرد.
در بیانیه سخنگوی وزات خارجه آمریکا آمده که روبیو در دیدار با محمد بن زاند آل نهیان و دیگر مقام‌های ارشد اماراتی «درباره یادداشت تفاهم رئیس‌جمهور ترامپ با ایران، تلاش‌ها برای تضمین عبور کامل و ایمن کشتی‌ها از ‌تنگه هرمز و اهمیت صلح و ثبات در منطقه» گفت‌وگو کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/VahidOnline/76650" target="_blank">📅 16:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76649">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccVZqv7TX7COrys4NqnvU8YbG7VB44NWJ7hb5KN5DxQLvIGEolrfkvwOlXVoEYFSX_2mqYUFYgyOShZbcaWm2WfzHKLcMcNe37rqW4_SIBZ3uX4GafF2-YM-omYEDDKLvdVP8OgTLpWvhJPRX3ml3_lI4aoXoi_gl_-podlQAqnkH2kylbcNl6bWXIVrblWav2r3RXa2FFUsGil8nNfp5G_TbGtlQZiTDCJ5WY3YMMnlX7xbMiyydAbDxS4Acv_HzFktY5sZ6mo5z_mWRCdfIk6PZaHpyGHlwipZZJgoaUjLvgmf5SPU8j0ehSbcq4QGm6WSyzz0PpBCvNhNB5ql2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامران غضنفری، نماینده تهران در مجلس، ضمن انتقاد از تداوم تعطیلی صحن علنی، به خبرگزاری ایلنا گفت که قالیباف طی چهار ماه گذشته بدون هیچ مبنای قانونی از برگزاری جلسات علنی جلوگیری کرده است.
این نماینده مجلس، وجود مصوبه شورای عالی امنیت ملی برای تعطیلی مجلس را «دروغ» خواند و گفت تعطیلی صحن با هدف جلوگیری از مخالفت نمایندگان با روند مذاکرات و پذیرش آتش‌بس صورت گرفته است.
او ادامه داد: «نمایندگان هم از یکی دو ماه پیش از قالیباف خواسته‌اند که اگر چنین مصوبه‌ای وجود دارد، آن را به ما نشان دهید، اما او هیچ چیزی نشان نداده است. بنابراین، این ادعا کاملا کذب و دروغ است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/VahidOnline/76649" target="_blank">📅 16:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76648">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tm4Kq6pTj8J4I-KhNSu_JDv6KhKMpq35Sxw0doNWXoxgrJeAkvjuoH6spe2CqZQ362YhaEkto_AlChXjHCCnO8O9AMC8VCtSRWusDiqG6_JPB611941hwBuItB9QFAyVWMqqy0fKFRUPrVoGaibWoXVO6oIiu6Tg4CwtELdr6XwwmIrNXOfLhjrfXcUbApCEyycE_vXBAgoY2BI3WM7UCrWdvtgoTqvAauh4ycRoyNJLWHJDfJi2w9Q2WgRc4WtZnb-jQPdelTZWKaIehaDbOCslmZPZcjTYVeTLI_xpLJCpcIEojWGuGlz_p8tzdmsGKPRzCnWZgwwpHMSnW9rHwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران به آمریکا اطلاع داده است که، برخلاف گزارش‌های دردسرساز فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای، و هیچ نوع هزینه دیگری از هیچ‌گونه‌ای از سوی ایران برای کشتی‌هایی که از تنگه هرمز عبور می‌کنند مطالبه یا دریافت نمی‌شود.
اگر این اطلاعات نادرست باشد، مذاکرات فوراً پایان خواهد یافت!
علاوه بر این، هیچ پولی از سوی آمریکا به ایران داده نشده، یا از پول‌های خودشان برایشان آزاد نشده است.
ما بخشی از پول آن‌ها را، که کاملاً تحت کنترل ماست، برای خرید ذرت، گندم، سویا، و چیزهای دیگر، در اختیار کشاورزان و دامداران خودمان قرار خواهیم داد.
غذا در ایران به‌شدت مورد نیاز است، و ما آن را منحصراً از ایالات متحده برایشان خریداری خواهیم کرد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/VahidOnline/76648" target="_blank">📅 16:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76638">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJxuK0lq1nNxLlR4DEjIBdKIF9Ijdidd8hTN3jYmLSJPR_38EIFWOAhBi2DI126q_z2D92B50vgCii7XNOuUUhgjXDVaXPG1MtWUmE-ypB4jNaoMAA3sXtF-a5TXGWKh6-n0px11PCh853s-M2tvRxuPBqd7nC3vdlqH7PxhIiymDuWDoHMvcLyJg_jmIQAcE8JJ51X1VwQvX6G-D3JkfmgRmKFFgY2xjPln6Z9kjfTJSPdHScAsYcNQjW4RlXtNiVPoLxtN6wyxTyGd5bMkLCkLCveiQC00x42hCNZF2kei63xL4GE_laUXPM8aFCHxVxkqX3ycL6TEEVCdca2nPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXVJ26c4flIBn1-NoRZpSmlg7lurQZLGhJRIx7s_xL5Ktph-BK4KM9oU1FD_rvhHJOi6uZsrNqVhz-Z8hFgXsgbcKwLqs3qMrOpGNzCs6s6noCTs-TYsCV-Wy4tVcZVVa-Oxbil-eMjO4xXhX68Swp7F-g2m0WrEa3tlvhqZnOpESLFcpWC0swPz6JiYDzp2PMNGE1QNI9lTf-qrDppQ0Hlg6tDAsk0dEpKAziA4Bto3K9w6j4uM_XIuUHZAjh0eiRg8SE6v55O9JB4Z4zPr2MrJIih2xqJV32h7i9xFNZJOSyyv9zb0WQNqvz2uSthAnR95ZjK9iM6PUkA9AicW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IjmKmR7LsKNlEte3CDbJBzuZldABpLg65fDncaNR8v0r_do0kgGHOXxyDUWl7Dh4xl8sVV8kcEASEWzt9zEoH8FP78Mfv5zUAgkB_UYr9eVSYP7B-9tzDcH7D94bHumb0PJrn18KVgJfab1EU8HKVQQ6vLQ9tYUH5LCjb5Ay5rk6k6anxcra22uTw_kgTNLM1A24rgNf_79sfj0poYE2bYaezMWT1Qv1wVy5lYHg-QLnJJYdbr9eGt9rIPqfXhwaZpLL1E3FizC3Xa6RrZbMx7s4S-7fOY7c08daDsL_2VKmPdOaq8wPyLroehFx9UR7sbjwA9wAYaTAyTPuoFr4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRfcfyDg6tz2vw43vR4umgUW1SXHMV1u5L1hWCVx3cyLpuIULstm9L4o6-3sO_1VMf03cT31iWR2Cv2orJMbPoyFiVNqcMcFX1qG1vvzu2HLAjGG9ZLWgKgvFGQUtpnqt5kNtUKf8a1klJhQnH6933Q9mvdCcbGfnhUqcxpi3oKHDueZwztk4c4fof-CtIxBlc3C0KQmEG6rLfM0J-5UhHDvMUdR7M-Qr00BXq45RuR7eWODK4wCU4cF5ww_Y1rS252mdk0dblXXwqg5Wu0_nKBJy6TB0NLIBUgL1UmlwsKQv6-kiI4970JfZw8g2Cf8Y22UHqsYqxrWF-lugjqh2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O79Npj03T27i8Hki_6RxsW4rjjlnVrkfmaE3zgNs7mAS__0qVbf8y4fu6VhQrCG-ymaCQb4Dzk1cuVJChcSAoKGjhDBxmUVJNHK66E7eLE1_XKBH9QOOcvwh8iNtE8Bb2piNLaMLSR3E_dCpaHv7bf4dd1ITQXd31zDTy4ztGZXh2-KE_w8PqPx5NBSfeerHxELKlrxt6BIlIWHZ_JZNUzGAFGc5gJyvWC8JQrOeqii4VG2VkFx_oUhpb1eVaB_x2mHdqC6dutSgOdgNu9qNlqyyFTeHOM2zHaGuBRcFgK9dJlRQhjUmEp4sQpessUMEwlAQd_q-u454s4357z16OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkgltZIpsJHLlAhl3cYjlIOacXsH69fu6ySCQ_tNrY4Xo4tnZ6OvY9uSTByRyukh2J7m2XFK_cxRNFY7sXVAtL3nvh6UBmCX9Iy3zWhAOHtzQB7BBC9QYN007kauH1OWsZ9a2i3GLqxlI34YywpmuPxZDvXJyXMHP4nuh1YapvboJ5kFw8q4Ebg3lxImKzTDgBhvoztDieAu3xzcEGZOk8PQB19aTlqVFDroj69J19hyS4o9jZYziWNqZGCPcvz-QjQ_k1ERe8hUed140DmlEnvryzQlssWNCxt7WoaH3Cpgvls9fAbDjXQhdTXoQInYXcYYI6HbGf9Tr3o5-noA2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOPrKyNNMHnwRJNdppChLOUrnF2p3Z_TPk3jkeypU5267wPDu7qaCuq2kcByn-QC0TeOuwmf-YASe3gEejsm5IUHQ7LnAHwofxWClVGcKK9XUcnFvyMWVeGVA5cSdk-nzKWD1kYx7aLQzUrGmX3ueoFzwRpY-lJcYSbCaaicmXQTwK696ixcYeKpV6KxlkmJ0ccKkccyw6CcjLre1mhUY0NszeX85EOhm4OaXcYsA78pXrmw0hxWXC7y4KQrb-hkQHWZ_WSfnChPoE7LdIWKUzQR4cY4EGnkYfbe_rB2KFNu0G0NfNck2-bLqa4j780TNO2iPZ61PtZBPe3OPZylFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMuQMHJCrMTx99S4gMcOHKOxrLXqk5VE3FMgJhQq87g-ErGvs7x9nyZv-lsDSjSqOZ2Tt5MNEJc6kNPCcjHIeQTdcK-DmByMDcX8hJJtEJKWefZrwm4m3xdkAhYe73t66yC5nLvsRR-Je4LvpyqR_DdY-dTQEnGcN4tonkhKKmuavmO36A6oc5KfE2Vefmnhx2D5T6FSBLP3G-OXppXsOuvWGbURAgRAxP4K1FroSs_mzWuiQwdzQnhwJKYL-qOl8fDXUDhfcQH8DK8XzvwFq6nA0exNs6FJPjm5q1VOWlpziNurWAIJ5Vg0rffRAVEpbVaiKGLQe0vGItv3LdSEvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fENjfgkP4-BnN3hGM6wr9-D0MFIg9soyehNB_6JlnP6DCzJOaTpP_jsimlOQNHj51DYIUG6uq_i9rneY-FelbAkgIkGDEH0SAWuQzX8RwHL2SzCAU1E30HHz8zTVR69yHgFhhlQRdGLO7sM43YLydrQrzA5POOCGSCo7SjA2Stoa6513a9h4Z6iqVy-OlBK2tkMFtfrRC98BX3fnJUUIKH_eOxvEywvVIGD4E9qIpuES-uA88nzGUjTpJLnvNcFP104qynLV3sigvLE7CDm6pVcpcKCPUmw_9Tp3Umgtzed-gi2-mZv3gqKMSjpw2rX6itUqS18UkMYtZ2yF2S6Y7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZrMqDaAeALyCASU4KL4afC7XhKicoNV52LGMP0-1OCygPPhTYHI3dF-kUzb6KAe8IT0Sp1gzExkzNzq-0560QY18bqmJbGxuW5JhqR8lxApOspqvA7wdPt2ZkFxJIpfqa96h6YIwC8TXuZgU2O5wYiY2fdqi66UXUV7wgkUIXq7Kb7zOE1hcwHdYE0BuPsG3RyPcH84cfL9tt5c91tl3qx087DDYhWjJwhy_JuYhKKUCKtboBKmfsVHcQBrq0o0EGq3MN9Id1OJaeUiha3H2fontxPvo6G-aS_MBjmEYDGNbINsQB2Vs1os9r0xTHReA3cbeyVxkIzKB3WoVeCvG2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔴
مرور قربانیان اعتراضات خرداد ۱۳۸۸
‏اعتراضات خرداد ۱۳۸۸ که در اعتراض به نتایج انتخابات ریاست جمهوری سال ۱۳۸۸ شکل گرفت، جانباختگان زیادی برجای گذاشت، بنیاد برومند تا کنون ۱۳۸ نفر از این افراد را که مرتبط با این اعتراضات کشته، ناپدید یا اعدام شدند را در نقشه اعتراضات خود ثبت کرده است. برای اطلاعات بیشتر در مورد این قربانیان به سایت بنیاد برومند مراجعه کنید.
اگر شما هم اطلاعاتی در مورد قربانیان اعتراضات دارید با ما در میان بگذارید.
‏لینک نقشه تعاملی اعتراضات:
https://www.iranrights.org/projects/protestmap/fa/
@IranRights</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/VahidOnline/76638" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76637">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=gSeh6k9Ksg98fJQXdAre3-yDH03YnbT0eIWbBoLNl0d5UOQDctFqBgSx5h1XLTDDHb4oh1_Fjl2lACIKXPvkh8tw25o4DJrqne7ScVPBlWb06iWm5SlV1LcZbYvkdzyS4W1OJtoW0AaZuN_z8B4vfwCNzUD1Xmfvr9vBsfzYa03xqvDmQtoicV4m3ZZiQMx2CJzPU6GXeOsFjJArMO2d4urbxIknVt8hHmRNAYzMvrw-Z6oqIoOsfPHPVhZfjpRRfSqTfwr4O53nG0PAiyLsJGGthW9ovi6-LuAsxz6c70aUVXLmtYg9X6hcageDHkBnveIhczekQKFLXXN9UaOO7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=gSeh6k9Ksg98fJQXdAre3-yDH03YnbT0eIWbBoLNl0d5UOQDctFqBgSx5h1XLTDDHb4oh1_Fjl2lACIKXPvkh8tw25o4DJrqne7ScVPBlWb06iWm5SlV1LcZbYvkdzyS4W1OJtoW0AaZuN_z8B4vfwCNzUD1Xmfvr9vBsfzYa03xqvDmQtoicV4m3ZZiQMx2CJzPU6GXeOsFjJArMO2d4urbxIknVt8hHmRNAYzMvrw-Z6oqIoOsfPHPVhZfjpRRfSqTfwr4O53nG0PAiyLsJGGthW9ovi6-LuAsxz6c70aUVXLmtYg9X6hcageDHkBnveIhczekQKFLXXN9UaOO7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ پست کرده
متن صدایی که ازش شنیده میشه به تشخیص ماشین:
از سال ۱۹۷۹، زمان می‌گذرد.
ایران در ۴۷ سال گذشته هر سال آمریکایی‌ها را کشته است.
۱۶۰ گروگان کشته شده‌اند.
۱۸۰ حمله از سوی ایران به آمریکایی‌ها.
رؤسای جمهور پیشین با سازش با ایران، ۱.۷ میلیارد دلار نقد به آن پرداخت کردند و در حالی که ایران به دنبال سلاح هسته‌ای بود، از اعمال تحریم‌ها خودداری کردند.
این می‌تواند ۱۱ بمب هسته‌ای یا موشکی بسازد که به زودی ممکن است به خاک آمریکا برسد.
تولید قریب‌الوقوع یک سلاح هسته‌ای آن‌قدر نزدیک است که آرامش‌بخش نیست.
ایران چه زمانی به سلاح هسته‌ای دست خواهد یافت؟
هرگز.
متشکریم، رئیس‌جمهور ترامپ.
realDonaldTrump
پست دیگری که در واکنش به تصویب طرح توقف جنگ در سنا نوشته:
ترجمه ماشین: بنابراین، من ایران را در گوشه رینگ گیر انداخته‌ام، آماده زمین خوردن، حاضر است عملاً هر چیزی به ما بدهد، و برای نخستین بار در دهه‌ها، حسابی برای ایالات متحده و رئیس‌جمهورش، یعنی من، احترام قائل شده؛ آن‌وقت سنای آمریکا تصمیم می‌گیرد رأی‌گیری بدزمان‌بندی‌شده و بی‌معنایی درباره قانون اختیارات جنگی برگزار کند و به حامی شماره یک تروریسم در جهان بگوید که ایالات متحده کاری را که من با آن‌ها می‌کنم دوست ندارد و من باید متوقف شوم، و با این کار به دشمن کمک و آسایش رسانده است.
چهار بازنده جمهوری‌خواه همراه با دموکرات‌های احمق رأی دادند، و ایران از افراد من پرسید: «همه این‌ها یعنی چه؟»
این سناتورها همین حالا کار مرا دشوارتر کرده‌اند، اما من آن را انجام خواهم داد، به هر طریق ممکن، چون من همیشه کار را انجام می‌دهم!
رئیس‌جمهور DJT
realDonaldTrump
در واکنش به:
سنای آمریکا که در اختیار جمهوری‌خواهان است، روز سه‌شنبه از طرحی قانونی برای توقف اقدام نظامی آمریکا علیه ایران حمایت کرد.
سنا با ۵۰ رای موافق در برابر ۴۸ رای مخالف به این قطعنامه مشترک رای داد.
این طرح پیشتر در اوایل ماه جاری در مجلس نمایندگان آمریکا نیز تصویب شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/76637" target="_blank">📅 06:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76636">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uy1PRZF35la-ISWsfmOcatoS2Rpf1ZbmlPtdPtOIMl485EFQV9UjVu4-ZvKTOkfECxwun5GPfKxRgfqNmh4T_pyga05TXrM9rZCHf9hzLNPyQw4fss4488oyA3zaGh2J_0KE4bp0rhzFaaYr7HubQqZQetOL_kvLY30kNlxd1B6jZtspXVXbr6jZywquDGgkZRPjcLaO1kInfE1-3W2IVaKkmmuVj9lv59EGjKf9lA9PWhTejmEXSsvdB5_eS8oSlft52yEwEI8vJkYJ5vXSqDh5uyBLNFeKhMJl7MJgW8U9STSe_hzpvmEpJvpCIMAvwU_IIpcHnT4Tegtysm_Bng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ProtesterCrow
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76636" target="_blank">📅 03:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76635">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cTCJIrF9wK7X5NS8ybHCv-JLTbBhJAdwayCjaXgRn5dxGSg3n19xWrDHOM5q-yc78AFTbA7a2BLFeJLdxoPRiIROdo9fdaFS2HCIWXN5sugbqW6ttOwikLQ6B34ow6xRWISqLG9tBqbyrhV-G3Xp8Q8qzf9BsHJXaKZ18C4uni9KVEWIrosHQjUfwNZV27abC-tORZrt2G5-pgIbRZ4uxeXTNz7FTh_bEIoSO783HBTAufu5IHCTGhFhL56EW38kGz99qcwyMWNlEKRmTCFp3IjDgjdfCC7JVVYoeZHUzuFn-kJEvJzSFWxepg8cTUwhrR4B87aPyEDXjn1eA76GGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنرانی ترامپ در پنسیلوانیا
جملات مرتبط با ایران به تشخیص ماشین:
ما به یک توافق صلح تاریخی با ایران دست پیدا کردیم تا درگیری در تنگه هرمز را پایان دهیم.
راستی، دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد. جای بسیار زیبایی است. این بیشترین مقدار نفت در تاریخ این تنگه است. هرگز چنین چیزی ندیده‌اید. به آن می‌گویند فوران نفت.
مهم‌تر از همه، داریم یک چیز بسیار مهم را تضمین می‌کنیم؛ چون دلیل انجام این کار همین بود. من به همین دلیل این کار را کردم. ۹۹ درصدش برای همین بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
اما یادتان باشد، این آسان نبود. ما ۴۷ سال رئیس‌جمهور و افراد دیگر داشتیم؛ کشورهای دیگر هم بودند. ما تنها کسانی نیستیم که هیچ کاری نکردند. آنها قلدر خاورمیانه بودند. حالا داریم ایران را بدون نیروی دریایی، بدون نیروی هوایی، بدون پدافند ضدهوایی، بدون توان موشکی، و بدون برنامه هسته‌ای باقی می‌گذاریم.
ما آنها را بدون هیچ ظرفیت هسته‌ای باقی می‌گذاریم، و آنها با این موافقت کرده‌اند. و رابطه‌مان هم خیلی خوب پیش می‌رود، هرچند اگر اخبار جعلی را بخوانید، هیچ‌وقت نمی‌فهمید. فکرش را بکنید، اخبار جعلی.
آنها ارتش ندارند، نیروی دریایی ندارند، نیروی هوایی ندارند، پدافند ضدهوایی ندارند. ما می‌توانیم هر وقت بخواهیم بر فراز تهران پرواز کنیم. هیچ‌کس کاری به ما نخواهد کرد. بعد اخبار جعلی را می‌خوانم که می‌گویند اوضاع آنها خیلی خوب است. اوضاعشان خیلی خوب نیست.
اما اقتصاد ایران خرد شده و پایه صنعتی دفاعی‌شان چنان به‌شدت آسیب دیده که بازسازی آن سال‌های زیادی طول خواهد کشید. سال‌های بسیار زیاد. حالا ما داریم تلاش می‌کنیم به توافقی برسیم که منصفانه باشد.
یادتان باشد، ما مجبور شدیم این مسیر انحرافی را برویم. مجبور شدیم سراغ ایران برویم. نمی‌شود اجازه داد آنها خاورمیانه و ما را منفجر کنند؛ اگر چنین چیزی ممکن باشد. ما زودتر به آنجا می‌رسیدیم، اما آنها اسرائیل را منفجر می‌کردند، کل خاورمیانه را منفجر می‌کردند. اگر می‌خواهید اقتصاد بد ببینید، آن اقتصاد بد است.
یادتان باشد، نفت ما، در میانه این درگیری، از دوران جو خواب‌آلود بایدن هم ارزان‌تر بود. و ما داریم یک آتش را خاموش می‌کنیم. بایدن، کلینتون، بوش، همه‌شان، باراک حسین اوباما ـ اسمش را شنیده‌اید؟ اسم باراک حسین اوباما را شنیده‌اید؟ ـ هیچ‌کدامشان کاری نکردند.
اوباما به آنها ۱.۷ میلیارد دلار پول نقد سبز داد، یادتان هست؟ با یک ۷۴۷. آنها انبوهی از پول نقد را با هواپیما بردند. ۱.۷ میلیارد دلار. صدها میلیارد دلار به آنها دادند و فکر کردند می‌توانند با رشوه آنها را به صلح بکشانند.
تنها چیزی که آنها می‌فهمند همان چیزی است که این آقایان ردیف جلو می‌فهمند: چکش. چون اگر نگاه کنید به کاری که آنها کردند ـ به کاری که ما با ظرفیت هسته‌ای‌شان با آن بمب‌افکن‌های B-2 کردیم ـ آن یک چکش بود. در واقع اسمش را هم گذاشتیم چکش. عملیات چکش.
دمبوکرات‌ها به نفع داشتن سلاح هسته‌ای توسط ایران رأی دادند. و علیه بودجه نظامی رأی دادند. اما من آن را دور زدم.
ایران، ما آنها را از پا درآوردیم. در یک هفته، اساساً از نظر نظامی تمام شده بود. کشوری بسیار بزرگ‌تر، و با ایدئولوژی‌ای بسیار متفاوت. ایدئولوژی مسلمانان کمی با ایدئولوژی کاتولیک‌ها فرق دارد. ما کاتولیک‌ها و مسلمانان را داریم؛ کمی متفاوت‌اند.
... ونزوئلا عالی بوده و ایران هم عالی بوده/خواهد بود، اگر عاقل باشند. وگرنه مجبور می‌شویم کار را تمام کنیم، که کمتر از یک هفته طول خواهد کشید. اما فکر می‌کنم آنها مشکلی نخواهند داشت. آنها کاری را که باید انجام دهند انجام خواهند داد، چون ما باید این کار را تمام‌شده ببینیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76635" target="_blank">📅 00:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76634">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=g6_Ek09s0Y_kxfu3YiL0zpYAhEMXBW-lxong_cPM_7CLCawtQgoHI8JId57lAbJNcftEFOxEomdbnSHNx8Mgu888DOAZhUJJ4B0sCNHTCP-TXgFWIMeecMNdBfMZBUtDGM68HVY_v0v7z-gJYUIppVOUWY4OgskXsjJcbO7uVetmFP8hwe3FpFuEUHe1lI45w458jNp7RZ1GWfQ4Q5TF2b0CwchIqy2NbrrYc1Xl05Cvji2ejyYd98WUtA4Bwk0imPSqaCJOxQ9OP4PGZjpPi6YlAgdCQrm9eQCEnBZUdK5Lzq8bnTQT18E9tU1-ceyxzKQjVgO4r9d4CxSkr9Zh1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=g6_Ek09s0Y_kxfu3YiL0zpYAhEMXBW-lxong_cPM_7CLCawtQgoHI8JId57lAbJNcftEFOxEomdbnSHNx8Mgu888DOAZhUJJ4B0sCNHTCP-TXgFWIMeecMNdBfMZBUtDGM68HVY_v0v7z-gJYUIppVOUWY4OgskXsjJcbO7uVetmFP8hwe3FpFuEUHe1lI45w458jNp7RZ1GWfQ4Q5TF2b0CwchIqy2NbrrYc1Xl05Cvji2ejyYd98WUtA4Bwk0imPSqaCJOxQ9OP4PGZjpPi6YlAgdCQrm9eQCEnBZUdK5Lzq8bnTQT18E9tU1-ceyxzKQjVgO4r9d4CxSkr9Zh1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آذر عظیما، خواننده پیشکسوت موسیقی ایران و از نخستین خوانندگان برنامه «گل‌ها»، در ۹۹ سالگی در اصفهان درگذشت.
آذرمیدخت عظیما سراج‌پور که بیشتر با نام آذر عظیما شناخته می‌شد، متولد ۱۳۰۶ در اصفهان بود و فعالیت هنری خود را از سال ۱۳۳۳ با رادیو ایران آغاز کرد.
نخستین اثر او ساخته‌ای از ابوالحسن صبا با شعری از ابوالحسن ورزی بود. او همچنین از نخستین هنرمندانی بود که در مجموعه برنامه‌های ماندگار «گل‌ها» حضور یافت و نخستین برنامه «یک شاخه گل» را با همراهی ویولن ابوالحسن صبا و سنتور فرامرز پایور اجرا کرد.
آذر عظیما در طول فعالیت هنری خود آثار متعددی را در برنامه‌های «گلهای صحرایی» و دیگر برنامه‌های رادیویی اجرا کرد. قطعه «راه شیراز» از شناخته‌شده‌ترین آثار اوست که با ارکستر فارابی به رهبری همسرش، زنده‌یاد مرتضی حنانه، آهنگساز و رهبر ارکستر، اجرا شد.
از آذر عظیما به عنوان نخستین بانوی آوازخوان اصفهان نیز یاد می‌شود. او روز دوم تیر ۱۴۰۵ در ۹۹ سالگی درگذشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76634" target="_blank">📅 23:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76633">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=ubatK5iQEQs4Xrm9bgtXZ_lCVjaoDwWUQGHx0mtmDw7NjGup56ZP7JzWWvyMCMU5cbbZZi0ZoAnPvVdBisdxQEB-e4LlqHOx7w9HOPpE-Jc4EZJZ8d2UghvST0Jl6hHBRkgC2bVtL30Nk-YXoBGc2HChBRzRhD5n-SjOM-c5MN16_yF9xKs9voZLZIhNl5Wh9UGnpMIxHgVKrzbUuT0G-j-HNXodRlFHOUw4OlonYLAzBnZgpIf2P0I3LkwgI_EVNgykeoq2LWPzWFaXWf8INJuYm3Lu_eKErLEdqkRDKePSHfrpMsRFV52DPTon24VdTqch4BYw-SJ5_MVULeeFGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=ubatK5iQEQs4Xrm9bgtXZ_lCVjaoDwWUQGHx0mtmDw7NjGup56ZP7JzWWvyMCMU5cbbZZi0ZoAnPvVdBisdxQEB-e4LlqHOx7w9HOPpE-Jc4EZJZ8d2UghvST0Jl6hHBRkgC2bVtL30Nk-YXoBGc2HChBRzRhD5n-SjOM-c5MN16_yF9xKs9voZLZIhNl5Wh9UGnpMIxHgVKrzbUuT0G-j-HNXodRlFHOUw4OlonYLAzBnZgpIf2P0I3LkwgI_EVNgykeoq2LWPzWFaXWf8INJuYm3Lu_eKErLEdqkRDKePSHfrpMsRFV52DPTon24VdTqch4BYw-SJ5_MVULeeFGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی بالا رو منابع دولتی با این شرح منتشر کردند:
"تشریح جزئیات اقتصادی تفاهم‌نامه ایران و آمریکا از زبان رئیس‌کل بانک مرکزی"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/76633" target="_blank">📅 23:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76632">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU6HGrxDmNFeRCzW6scH7xwt-g-L1wObB0TseqmFoXRP3rCQUUEgpSYfltEEoKHAR-HTrVfAr2g-3keJtkhu0pwCXFDYna5dmKBed8l_vlSr9yQxUpVlGsWY0QyKzY10CU5rN10pcnYs4T20svX0I_xtik1QxlOtTSmf_J4hThzGInQaErBHakLmMqFBP4KbZoSix726Y3tvRhw0LRMRItbONAXI3XYgdtfKWQgocva5U0LrTH41AhuX6S6Up8z0FO8cWExw6XYeuLCG4VOZzcOP28kd-ZoPeHuoAdFq_7bay1CT5WsZ0_bdd8l_pm6SE0FbAyQOioewc-8UmN-kaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده، در حضور خبرنگاران در ابوظبی گفت که جمهوری اسلامی ایران به دلایل سیاسی و داخلی خود، موافقت با بازرسی‌های هسته‌ای آژانس بین‌المللی انرژی اتمی در نشست سوئیس را تکذیب می‌کند.
روبیو گفت:
ما می‌دانیم آن‌ها با چه مواردی موافقت کرده‌اند. من نمی‌دانم چرا مجبورند این حرف‌ها را بزنند. سیاست داخلی یا مسائل درون‌مرزی آن‌ها هرچه که هست، خودشان باید با آن کنار بیایند. اما ما می‌دانیم متعهد به انجام چه کارهایی شده‌اند؛ حالا یا آن را انجام می‌دهند یا خیر.
وزیر خارجه آمریکا در پایان تاکید کرد: «اگر آن‌ها به تعهدات خود عمل کنند، فرآیند رو به جلو حرکت خواهد کرد، اما اگر از انجام آن سر باز زنند، رئیس‌جمهوری (ترامپ) باید تصمیمات جدیدی اتخاذ کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/76632" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76631">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=SDhNVBq-R1f8lTOYUXwN9OH3ObZEKADkwhwteUgC55bSHa0pElSvvdX9pMOhMQ2cXr-qfOkKUpdvqVlspHujCocHnj7Gg5GxYvzo9DXphuDMU5TJ7YGQ85Gsa3P5uLzmhhpxdxG3ktzclXoEFz5g19I2eSH_pijiiRqvxlaz8JS4mkUk8K8Qq4yj5K3WDD-8nKY3f4kBCmUkYRIruZZoXVCHGtjcpIydO5AFsp2LOPnnBaQMW5aIfXtJ8GZhDY0LwahqGI3xAX50qQkkRFVGBwshrT2qLD7N1wbNN0e_JrieZCaQXWa5OzQ8Oa9MSXelR1txPYr4bwEr3ViP4tGtCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=SDhNVBq-R1f8lTOYUXwN9OH3ObZEKADkwhwteUgC55bSHa0pElSvvdX9pMOhMQ2cXr-qfOkKUpdvqVlspHujCocHnj7Gg5GxYvzo9DXphuDMU5TJ7YGQ85Gsa3P5uLzmhhpxdxG3ktzclXoEFz5g19I2eSH_pijiiRqvxlaz8JS4mkUk8K8Qq4yj5K3WDD-8nKY3f4kBCmUkYRIruZZoXVCHGtjcpIydO5AFsp2LOPnnBaQMW5aIfXtJ8GZhDY0LwahqGI3xAX50qQkkRFVGBwshrT2qLD7N1wbNN0e_JrieZCaQXWa5OzQ8Oa9MSXelR1txPYr4bwEr3ViP4tGtCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
آقای رئیس‌جمهور، وزارت جنگ برای جنگ ایران ۸۰ میلیارد دلار درخواست کرده است. فکر می‌کنید آمریکایی‌ها در شرایطی که بسیاری از نظر مالی تحت فشارند، از این حمایت می‌کنند؟
...
آنها فقط از این حمایت نمی‌کنند، بلکه آن را مطالبه می‌کنند، چون اجازه نخواهند داد ایران سلاح هسته‌ای داشته باشد.
می‌خواهید دردسر ببینید؟ بگذارید آنها سلاح هسته‌ای داشته باشند.
ما در قبال ایران خیلی خوب پیش می‌رویم. آنها نابود شده‌اند و ما داریم با آنها توافق می‌کنیم. باید ببینیم همه‌چیز چطور پیش می‌رود.
همین حالا، همان‌طور که احتمالاً دیروز شنیدید، ۱۹ میلیون بشکه نفت عبور کرد. این بزرگ‌ترین رقم در تاریخ تنگه است؛ تنگه هرمز.
بازار سهام ما به‌شدت بالا رفته و قیمت نفت در حال سقوط است. امروز برای لحظه‌ای به ۷۰ دلار برای هر بشکه رسیدیم ــ در واقع فکر می‌کنم از آن هم پایین‌تر خواهد رفت. این پایین‌تر از زمانی است که شروع کردیم.
و واقعاً شگفت‌انگیز بوده است. نکته اصلی این است که ایران سلاح هسته‌ای نخواهد داشت.
خبرنگار:
ایران؛ ایرانی‌ها می‌گویند هیچ سفر برنامه‌ریزی‌شده‌ای برای بازرسان آژانس بین‌المللی انرژی اتمی وجود ندارد. آیا این بخشی از توافق شماست؟
ترامپ:
اشتباه می‌کنند. خودشان می‌دانند اشتباه می‌کنند. به ما در داخل گفتند که این را قطعی کرده‌ایم: بازرسی صددرصدی.
و اگر حق با آنها بود، همین حالا جلسات را لغو می‌کردم.
خبرنگار:
و ایران می‌گوید درباره آن توافقی وجود ندارد. از نگاه شما، آقای رئیس‌جمهور، آن بازرسان واقعاً چه زمانی روی زمین خواهند بود؟
ترامپ:
در زمان مناسب. عجله‌ای نیست، اما در زمان مناسب روی زمین خواهند بود.
خبرنگار:
آقای رئیس‌جمهور، به متحدان خودتان که از توافق با ایران انتقاد کرده‌اند چه می‌گویید؟
ترامپ:
خب، فکر می‌کنم هر کسی که از آن انتقاد کرده، در موضع بدی قرار دارد؛ حتی اگر از دوستان ما باشد.
چون ما ایران را در موقعیتی قرار داده‌ایم که هیچ‌کس تا حالا قرار نداده بود. رؤسای جمهور دیگر باید ۴۷ سال پیش این کار را می‌کردند.
ما ایران را در موقعیتی قرار داده‌ایم که ارتشش کاملاً از بین رفته، رهبری‌اش از بین رفته، رادارش از بین رفته؛ همه‌چیزش از بین رفته است.
آنها موقعیت مذاکره خوبی ندارند.
اما با وجود این، پولی که از ایران خارج می‌کنیم، قرار است به کشاورزان ما برسد تا ذرت، سویا و گندم بگیرند؛ باید پول زیادی باشد.
چون آنها مشکل گرسنگی دارند، مشکل غذا دارند، مشکل دارو دارند و مشکلات زیادی دارند. تورم هم دارند. تورمشان همین حالا به ۳۰۰ درصد رسیده است.
بنابراین مشکلات زیادی دارند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/76631" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76630">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AT2OlF8MVZmrcAuEzUGiBam3SLzpZId0e-2Gel7cxwnCPUrpDUFlH8tTVcvPrDSMh6-KwvFw2EtZsOyKNtdxhWAoUemLCwajmxFew73xUsiCsafYMXo64NpHNz4hL6DtkzvdmHIpnTxOFZnZQHJFJHKb1HEpcbHKZ2chZpQDNjXgoBkCyx67hB3raCPr2w_a1qIycblK5Uocl0x2X8VsZ6soERsC5zaGkAwgG0AEWXDWpaTdPgf7EkcbGZN5tfF0szTxgLRpT1br9ZjJT2uBYtkw3q0F7sbcuSK013GGwb7bmHx-VU6SngWZS7aui650SJIT_RX205dD3yteXr5PQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، سه‌شنبه به شبکه ان‌اچ‌کی ژاپن گفت بازرسی از تاسیسات هسته‌ای ایران انجام خواهد شد و هرچه زودتر آغاز شود بهتر است.
او افزود اولویت اصلی آژانس، شناسایی و تایید محل نگهداری اورانیوم با غنای بالا است.
گروسی گفت آژانس بین‌المللی انرژی اتمی به‌زودی با مقام‌های جمهوری اسلامی درباره زمان‌بندی و جزییات بازرسی‌ها گفت‌وگو خواهد کرد.
او تاکید کرد آژانس این بازرسی‌ها را به‌طور مستقل انجام می‌دهد و نیازی به نظارت یا کمک دیگران ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/76630" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76629">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q-HsdfJkXlJ-7-9bzLHjsaixdOdtUP8VxQBDjhZRKnDFNgvPJK3oxD0QLadUlLDT_9CEuxcYUEvYlZbsH43mQCJJIj7Z9dgm2V9kY9B9dFvBeF9Re196ioh7dkt1ikselsfzdJHni3wcy6br4wYDToVFX6RT6fmkiPj47gEu94AweHLwmqzV6ZIegMmVvAA3BMM9gEfwsnlKxYnJPvIy7pGAhij4VN4ZuLIDPZuOua1lD40ebNGqtrhnkn9HiMBUQwxEmNoUjlXJTwZ9UPETYdPk8vAC7B4gKY6VJ-YReEND6hNfJKOpCjkGfbKJvKx8SOqQbTDnKDBkuQ0LPGac7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه آمریکا می‌گوید تا زمانی که گروه‌های نیابتی مورد حمایت ایران به حملات موشکی ادامه دهند، دستیابی به صلح پایدار در منطقه غیرممکن است.
مارکو روبیو که به امارات متحده عربی سفر کرده است، روز سه‌شنبه دوم تیرماه افزود این موضوع «در زمان مناسب» مورد رسیدگی قرار خواهد گرفت.
او همچنین تأکید کرد هیچ کشوری حق ندارد بر تنگه هرمز عوارض یا هزینه‌ای تحمیل کند، چرا که این آبراه یک مسیر بین‌المللی است و بر اساس قوانین موجود بین‌المللی حفاظت می‌شود.
تنگهٔ هرمز از زمان آغاز حملات آمریکا و اسرائیل به ایران در ۹ اسفند پارسال، از سوی سپاه پاسداران مسدود شده بود و تنها هفته گذشته پس از توافق اولیه بین تهران و واشینگتن برای پایان دادن به جنگ تا حدودی بازگشایی شد.
وزیر خارجه آمریکا در مورد لبنان که برقراری آتش‌بس در این کشور بخشی از توافق بین تهران و واشینگتن است، گفت که ما قرار است مستقیماً با دولت لبنان به توافق برسیم.
روبیو تصریح کرد که «آینده لبنان را مردم لبنان تعیین می‌کنند و پرونده لبنان از هرگونه توافق با ایران جداست».
@
VahidHeadline
فرماندهی مرکزی ایالات متحده،
سنتکام
، با انتشار تصویری از ناو هواپیمابر «یواس‌اس جورج اچ. دبلیو. بوش»، در شبکه ایکس نوشت که این ناو در
دریای عرب
در حال فعالیت است.
سنتکام افزود دو ناو هواپیمابر آمریکا همچنان در خاورمیانه مستقر هستند و نیروهای آمریکایی حضور خود را حفظ کرده و در حالت آماده‌باش و مراقبت کامل قرار دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/76629" target="_blank">📅 19:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76628">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5986282857.mp4?token=rwlfrDZgBabz6nd_erg_M3vu7wh3jUdH7ywXPwToO78LBkGmBV3WNrJjU8-A2RBZvfAhfwQZVaIAS-yHAISDeOMUwWUO995fPzWpQdc-6cSIXJkEvHeITBbVV60viV-reYqkl8RP9qqu9btWk4GZYZIFTO15AuEKU5KpgwerRFSpLdh3VP7zAxUfisHBukFeVbB4YtxSwVHOQrlfmyCNjvOxOVxJXineaAQQWmyytJWCuFFcGKejd6BncrsFXp1zaYB_xmrtaJ2qPdU3T0ttsmuiF_1Z-8YQUJ_8hL-sk5OPi1YyQO586l4IMjVYL60lQ8H8GNyO1rM_fXQeAjCHBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5986282857.mp4?token=rwlfrDZgBabz6nd_erg_M3vu7wh3jUdH7ywXPwToO78LBkGmBV3WNrJjU8-A2RBZvfAhfwQZVaIAS-yHAISDeOMUwWUO995fPzWpQdc-6cSIXJkEvHeITBbVV60viV-reYqkl8RP9qqu9btWk4GZYZIFTO15AuEKU5KpgwerRFSpLdh3VP7zAxUfisHBukFeVbB4YtxSwVHOQrlfmyCNjvOxOVxJXineaAQQWmyytJWCuFFcGKejd6BncrsFXp1zaYB_xmrtaJ2qPdU3T0ttsmuiF_1Z-8YQUJ_8hL-sk5OPi1YyQO586l4IMjVYL60lQ8H8GNyO1rM_fXQeAjCHBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر پاکستان روز سه‌شنبه دوم تیرماه گفت که در مورد موشک‌های بالستیک نباید استاندارد دوگانه‌ای وجود داشته باشد و تأکید کرد ایران همان حقی را برای در اختیار داشتن آن‌ها دارد که سایر کشورها دارند.
شهباز شریف همچنین به خبرنگاران گفت که در تفاهم‌نامه مورد توافق میان ایران و ایالات متحده هیچ اشاره‌ای به موشک‌های بالستیک نشده، زیرا این موضوع اساساً در آن مذاکرات مطرح نبوده است.
پیشتر برخی رسانه‌ها از قول نخست‌وزیر پاکستان مدعی شده بودند که او گفته است موضوع موشک‌های بالستیک تهران از جمله محورهای مذاکره بین ایران و آمریکا است.
در واکنش به این ادعا، خبرگزاری فارس نزدیک به سپاه پاسداران نوشت که اظهارات نخست‌وزیر پاکستان، «کاملاً اشتباه و احتمالا ناشی از بی‌اطلاعی است».
به نوشته این خبرگزاری، پاکستان در حال حاضر نقش چندانی در میانجی‌گری این مذاکرات ندارد و اظهارات شهباز شریف بیشتر برای پررنگ‌نمایی نقش واسطه‌گری این کشور مطرح شده است.
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/76628" target="_blank">📅 18:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76627">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIRaNWZvyZBhuiuq7QjlRUUeQJDoSwu4WkwdYhW0YFuP4-nOY5ILJg7x_JPJmK0SFKEZyulXWdBoLhCw_p6KM9WRUvcPaqo16HBtDVZzn-RQKNxGlYjA847k76IOGJX-hn8RCcDyF-Cy_AS_OFNrrCsNYpUC3orAVOaX4mzidcbSm1wcyx0tHqmatQ6j8wbMGDU7ZWJD5KMlV9uxynbHAYowLpGOQTj1wgGj6PO11EI9tkUyhoI8FedP_6tLRLAWWMgY3O165E-KEVkBEMjuawX-m7WLScw0nxe-54DnraCMcfBlTCWe_XE7zHiqhyVDiOnJkY0ilG5cBA30X9Q5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثریا طالبی، مادر امیرحسین موسوی، فعال فضای مجازی مشهور به «جیمز بی‌دین» که از آذرماه ۱۴۰۳ در بازداشت به‌سر می‌برد، می‌گوید پس از پخش گزارش تلویزیونی از فرزندش در جریان جنگ ۱۲ روزه، اتهام «همکاری با دول متخاصم» به پرونده او افزوده شده است. مهر ۱۴۰۴ صداوسیما با پخش ویدئویی از اعترافات اجباری امیرحسین موسوی، او را به «جاسوسی و همکاری اطلاعاتی و امنیتی با اسرائیل» متهم کرد.
پس از آن امیرحسین موسوی که با نام کاربری «جیمز بی‌دین» در شبکه‌های اجتماعی فعالیت می‌کرد، با انتشار نامه‌ای سرگشاده از زندان اوین اعلام کرده که تمام اتهامات مطرح‌شده علیه او «نادرست و تحریف‌شده» است. آقای موسوی نوشته که پس از ۱۴۸ روز انفرادی، بازداشت همسرش و تهدید به تکرار شکنجه‌ها، وادار به انجام مصاحبه‌ای اجباری شده است.
ثریا طالبی، مادر امیرحسین موسوی، در گفت‌وگو با «امتداد» با اشاره به وضعیت پرونده فرزندش گفت که امیرحسین موسوی از ۲۸ آذر ۱۴۰۳ در بازداشت است و خانواده او همچنان در «بلاتکلیفی کامل» به سر می‌برند.
به گفته او، فرزندش هنگام سفر به کیش در فرودگاه مهرآباد بازداشت شد و خانواده تا مدت‌ها از محل نگهداری و نهاد بازداشت‌کننده او اطلاعی نداشتند.
مادر این فعال توییتری همچنین گفت امیرحسین موسوی حدود شش ماه در سلول انفرادی نگهداری شده و پس از انتقال به بند عمومی، از او مصاحبه تصویری گرفته شده است. او مدعی شد به فرزندش گفته بودند این ویدئو صرفاً برای آرشیو ضبط می‌شود و در صورت همکاری، طی چند روز با وثیقه آزاد خواهد شد.
به گفته طالبی، در زمان تشکیل پرونده، اتهام‌های «اجتماع و تبانی علیه امنیت کشور»، «فعالیت تبلیغی علیه نظام» و «توهین به مقدسات» علیه فرزندش مطرح شده بود.
او افزود پس از جنگ ۱۲ روزه و پخش بخشی از این مصاحبه در بخش خبری ۲۰:۳۰ صداوسیما، اتهام «همکاری با دولت متخاصم» نیز به پرونده اضافه شده است.
طالبی با انتقاد از نحوه انتشار این ویدئو گفت: «فیلم به‌صورت تقطیع‌شده پخش شد؛ به شکلی که این تصور ایجاد می‌شد که امیرحسین در زمان جنگ اطلاعاتی را در اختیار دشمن قرار داده است، در حالی که او در همان زمان در زندان بود.»
او همچنین از شکایت خانواده علیه برنامه ۲۰:۳۰ و رسانه‌هایی که این ویدئو را بازنشر کرده‌اند خبر داد و گفت این شکایت در حال رسیدگی است.
مادر امیرحسین موسوی با رد اتهام‌های مطرح‌شده علیه فرزندش تاکید کرد: «انگ وطن‌فروشی به امیرحسین نمی‌چسبد. او یک فعال توییتری بوده و اگر کسی با ادعای ارتباط با اسرائیل برایش پیام فرستاده، بلافاصله آن حساب را مسدود کرده است.»
بر اساس اعلام وکیل پرونده، جلسه رسیدگی به اتهامات امیرحسین موسوی روز ۱۳ تیرماه در شعبه ۱۵ دادگاه انقلاب به ریاست قاضی ابوالقاسم صلواتی برگزار خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/76627" target="_blank">📅 18:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76626">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E6ZcTlkUudKy4AwPhC47cBRHSnsJlT_T7iyqWXTgBUB1G1VRYYghF0i3FQeVVEovd_WA_pOQIhKEg7lBFjyS_hQPNqUCuiyOy9VqBnhTbFLlk8zaowvv0p95udhTM204WJ-b3_T2wYUJ8YQzXuWeNR9Nk8ShnvdbuO6igmR8ipbDgXB-6UGuGlfD2TjDPj7XvLPm6K_FjW1Q7mBQydVJgM1f0l6ER6co6VdAl90HGJhybGRAohWoa0mWfris8Sm7NqCuePUu_MmythfoioTM5OEyMKEXjWNNMYL_jbHttyg5J8QqJ-P135w5bFDaFKkw5TktfXpFTP2zzFHhU_zNhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/76626" target="_blank">📅 18:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76622">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AgXDWaTHFt87uxoh3EAari6-URQC3NfNV2I-hemRVTqRr1er8f0siiMfVELvRir7KFBxh82oScBdM1WT9bp7yU76FbCnkcB479EPl0TwuWDQE0skB3Hy4QMOYQSNQeWOkGX69x04xmvq_pcMqX9S1CA03KXfzueOqX68xWDzp8hPtyjajmBTYlnfaS946RWGDRfmQab0_0iEQyh7eHJwnmEDqySNFf3DDJocenn-guUR_4fsNqO08lEuxzPbv_T2MJinQRQ5-yAN70AuETToWksJWtCtNK6Ybo_KF3j0J2LzKAZYRHan8r81TlVqgLTrVYHPFq8lkCOKagyeCwqQmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X1PG-1lu4v2BZUj--_dzz5UZgefz3r2kJ2SEhmRUvkCCglx9wuGzkBn7kH6E_nqlShnq1vdrpBJB0pGsvCau1DqOS1FPUwhWaIxbTb0h2K7u7tFk2-YM1ygj1JieUHKjcDsJGWXQztRna2P0t49AdL6JaByZxEsKANaKtpJu59_fiSoZXleJOhlRpvwJ_cJbRwsRtrFZWtFsU96P6rTpht1e9_Sq8uMDXg5Nb3mrQotkp3OKJMIZS06_NcK_FUKYt5ZusfhzT2MX-ot1HQsu9YQoxmBSXsyhpOTerm-wE39oIdU38-vkEkeFGYHYw57yBpY0pBfQ-qm6Fuoij3xvvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hnzkc7hkStBVydHNPwclRxPxoTsvMHTeVivWzoOHrRke35FPFzFPLXlzMU709q7ArY3SGeFy0EmYzs_9XzZPDL8XcvnAecwNil9U5eQ_wb5_5F3E7kv2sU4f5ddqjocuoussJbbRyTxnnP5Am5JBwxgxr_LhdkLSZd82l3eqRMBfeO1W56Ihz7CHAIpsa8UOBlJbNZQdQaHaH9tX8CVBOG1fQyPkHWEUm3wG6ro9_Y5OXPBry8OwXbEcyOqERrMoPeUmipNgiNkeLfNhJmZZtyn4qZqPx2SJ1KA_-FoO-i3_MDQgsknOYZal9JrecIGZy4Qr0uYvSu2diiwckJ3wtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AThF-0j_gtzTWds_KbWRPlYR1n99Y8ViDbwukq4_wyLEj9fZ-j0_0nDYif86zjz5dNJ-oaAkD2mzVVJuLbUvTyBENeqKZDGLQzSS1AULhA3UA-GGpoM_NsrxkPVVph0nlm9QQExhyP5AzNkiwQ3m14FIuvRwyxfbC_Owbl3ylqy8QM9TfE5wVM68vzSwkSzrdJ_z9_lByDykuY9nWkb4SVs2m2y5G9y0sQfTZWAfZ3m7c0yztxeYu4DqUXcDbuXBZEynkLYedx2eewy-1-iF7CKw1YwBpuy8Rta4VpdljcOgEdSvbwaaKDqBgUgRdxQhyXT2YPqk19ikP14CrHij8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش‌های کاربران از بروز اختلال شدید و قطعی در سامانه‌های آنلاین و پایانه‌های فروشگاهی (POS) برخی بانک‌های کشور از جمله بلوبانک، بانک کشاورزی، بانک ملت و بانک رفاه حکایت دارد. این اختلال‌ها موجب شده مشتریان در انجام تراکنش‌های مالی، خریدهای روزمره و استفاده از خدمات غیرحضوری با مشکل جدی مواجه شوند.
@
VahidHeadline
گزارش‌های مختلف کاربران در شبکه‌های اجتماعی حاکی از اختلال گسترده در خدمات بانکی چند بانک بزرگ ایران در روز سه‌شنبه، دوم تیر است.
بر اساس این گزارش‌ها، پرداخت الکترونیک و انتقال وجوه در چند بانک بزرگ مانند ملی، تجارت، صادرات و ملت با اختلال همراه است.
خبرگزاری‌های فارس و تسنیم، نزدیک به سپاه پاسداران با تأیید این اختلال‌ها از احتمال حمله سایبری به مرکز خدمات پشتیبان خبر داده‌اند.
در همین رابطه شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، با تأیید انجام حملات سایبری، گفته است که «شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است.»
این برای دومین بار طی دو هفته گذشته است که خدمات بانکی در ایران دچار احتلال می‌شود.
چندین بانک ایران اواسط خردادماه هم با قطع ارتباط و خدمات روبرو شدند که به گفته مسئولان دولتی به دلیل حملات سایبری به زیر ساخت‌های خدماتی بانک‌ها بود.
تاکنون گزارشی از عامل این حملات سایبری منتشر نشده است.
@
VahidHeadline
آپدیت:
پیام‌های مختلفی دریافت می‌کنم با نظریه‌های توطئه که فکر می‌کنند بازار ارز و طلا و...  قراره نوسان داشته باشند و نمی‌خوان کسی بتونه خرید و فروش کنه و...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/76622" target="_blank">📅 17:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76621">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnUswE5SlCcM0sE3ihCaY2Mk9vRTX3vsPXWhyYPpfRnhFHzscnUE52D0wJ1yIF2qwzKeexMWQ7_CvjjvuOw18rQobzFx9Aq4SzES0f_h0bRySkGQM0QSPj7xlzlYqW8DYe4WzWaO4pkyi9zDmqIWnsSziX8IdvmFIfuCor7HBXrpLCtljPjDK2Npm4d4SNwq6-wVW31cNtyNB3e9a_WYeb3C0x0rxhL67p-P-U0z8-9GqIpTgzQsVO2_HZVzHHirZoTAEQdmZgydEYP_pDE9sA1iYfHflvP71pJwRnAJFUx6qr8ZI7cZ8z2GhdQFMsNG18btvGIWAFmaGfvvq7YMSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان و ایران روز سه‌شنبه دوم تیرماه توافق کردند گفت‌وگوها درباره نحوه اداره آینده کشتیرانی در تنگهٔ هرمز، از جمله خدمات دریایی در این آبراه راهبردی و هزینه‌های مرتبط با آن، را ادامه دهند.
به گزارش خبرگزاری رویترز، در بیانیه‌ مشترکی که پس از مذاکرات مسقط منتشر شد، دو کشور اعلام کردند یک کارگروه مشترک با مشارکت وزارتخانه‌های خارجه تشکیل خواهد شد تا این گفت‌وگوها را پیگیری کند و همچنین با دیگر کشورهای ساحلی و طرف‌های مرتبط رایزنی خواهند کرد.
این اقدام به نظر می‌رسد اجرای بندی از تفاهم‌نامه‌ای باشد که هفته گذشته بین ایران و آمریکا امضا شد و بر اساس آن، ایران موظف است با عمان و دیگر کشورهای ساحلی خلیج فارس درباره مدیریت آینده کشتیرانی و خدمات دریایی در این تنگه، که مسیر حیاتی برای انتقال نفت جهان است، گفت‌وگو کند.
این توافق پس از سفر محمدباقر قالیباف، رئیس مجلس شورای اسلامی، و عباس عراقچی، وزیر خارجه ایران، به عمان اعلام شد. این دو مقام ایرانی با سلطان هیثم بن طارق، پادشاه عمان، دیدار کردند و با وزیر خارجه این کشور، سید بدر البوسعیدی، نیز گفت‌وگو داشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 198K · <a href="https://t.me/VahidOnline/76621" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76619">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dcxSYBCueQmcTnVkSoVzZMq-oPPK82_SRILeguLLcLiUwomy4x8G6hujn0bVjkCsYkWzR15awlmkOzJewAb9uiGI0IGBMUl9Ri3hnqNTPhvVpR0KRKfXU-b169J5MhejO18N_dbTbrZxFXfw_3IynhkZwebWECJH3NfSPtF2KysldXQRf471KkAVdW7MoPAlO1FIKLe4aF8jPPdvnmIkjM5FGTQkIDzWVmlbVtpEW9DHfcP4SFX_Sovx5vg38JrXTpywmnk8C4DGMw8VIPSLQXPalwVCl8OILz3js29k4ZJVAa1smQNPRmQVW1rxu1kVFXxxlaS-aHuz6uxvlqgywQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=mEgQed5Gyw_5FvGk0fUdXMYS_MuRCs6Ro5S6QhzLhjG12wbysFJvWzo79y40tbtqSxBC68r4Y5MyM5CXZOGoikjP9ihBOAtYg22znRc4d1nxIJaaCVmW0dkE0mqKi3kswb0mlQHyyha8y7FK_G-sSKMYtE68uM4AiOKOswJhUpFxjuoSeHeSbnOdlxNpdjrUS9HsxVStV9gvpwKHYQRioHgN0y90jDzT_zHT2X4EERqjfE8I7n3Zg7HsyclxxO3A5zrk24tFjWHcOAf9L3q_V67FsmDxoRawSL6_LmJMALGHOLeMx9m97sfM9StK4iS3rbOfcX781D2wI75lzo4Whg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=mEgQed5Gyw_5FvGk0fUdXMYS_MuRCs6Ro5S6QhzLhjG12wbysFJvWzo79y40tbtqSxBC68r4Y5MyM5CXZOGoikjP9ihBOAtYg22znRc4d1nxIJaaCVmW0dkE0mqKi3kswb0mlQHyyha8y7FK_G-sSKMYtE68uM4AiOKOswJhUpFxjuoSeHeSbnOdlxNpdjrUS9HsxVStV9gvpwKHYQRioHgN0y90jDzT_zHT2X4EERqjfE8I7n3Zg7HsyclxxO3A5zrk24tFjWHcOAf9L3q_V67FsmDxoRawSL6_LmJMALGHOLeMx9m97sfM9StK4iS3rbOfcX781D2wI75lzo4Whg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامران غضنفری، نماینده مجلس شورای اسلامی، در شبکه اجتماعی ایکس از برنامه شماری از نمایندگان برای «تحصن» مقابل ساختمان این نهاد در اعتراض به ادامه تعطیلی آن خبر داد.
او نوشت که «چنان‌چه مجلس بسته باشد، تا باز شدن مجلس، در همان‌جا تحصن خواهیم کرد.»
شماری از نمایندگان مجلس به تعطیلی این نهاد طی ماه‌های بعد از حملات اسرائیل و آمریکا به ایران در نهم اسفند ۱۴۰۴، اعتراض دارند.
حمید رسایی، یکی دیگر از نمایندگان مجلس شورای اسلامی، یکشنبه ۳۱ خرداد با انتقاد از ادامه تعطیلی مجلس گفته بود در صورت ادامه تعطیلی، همراه برخی نمایندگان مقابل ساختمان مجلس جلسه برگزار خواهد کرد.
حسین صمصامی، دیگر نماینده مجلس شورای اسلامی، نیز در پیامی جداگانه در شبکه ایکس، نسبت به ادامه تعطیلی صحن علنی اعتراض کرده و نوشته است: «بیش از ۱۰۰ روز از تعطیلی صحن مجلس می‌گذرد و نکتۀ تاسف‌بار آن است که در سامانه قانونگذاری، امکان ثبت استیضاح وزیر و صدور بیانیه مسدود شده است.»
انتقادها در این زمینه به خصوص از سوی نمایندگان نزدیک به جبهه پایداری با پررنگ‌شدن نقش محمدباقر قالیباف در مذاکرات با آمریکا، افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/76619" target="_blank">📅 17:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76618">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oivr_xTrg7roYL1TT-a2awhlGTI7ZKIOPcODJPEkQu2kGiALCq_5tWfr9bALKk5LtE7F6nsH4mqyUyWnCZ0iQLsV2_e7T7-PAg5RhBvlHaCu04_jMMJSRaxRedm-N-ZeH2Yb-he3LZ-1IvsqZOreWGXimRNqovTlwUpnKqabZec7F6FzkqIXwoWPpK1bU_quyt8Dps-5IcmZpKYL8ph3FuzWuWy8S5RgG9EsklGIrSaY2Pmw7jxTfXOdkhRxM-8GOjnf_yjIWgfSl6EhxaO8bfW0i-McbfqB3g12yn6BoQssXj82iyJCCJfgptKG_RBhPLYnO1NIlY8xZi03vTu89A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانون فیلمسازان مستقل ایران، ایفما، در بیانیه‌ای نسبت به احتمال اعدام علی صفری، بازیگر تئاتر و دانشجوی دانشگاه فرهنگ و هنر هشدار داد.
این کانون با ابراز نگرانی از طرح اتهام «محاربه» علیه او، از مراکز سینمایی و نهادهای بین‌المللی خواست تا برای نجات این هنرمند و سایر هنرمندان در بند، «فشارها بر رژیم ایران و قوه قضائیه آن را بیشتر کنند».
به نوشته این نهاد، علی صفری، بازیگر جوان و ۲۳ ساله تئاتر و دانشجوی دانشگاه فرهنگ و هنر در جریان اعتراضات سراسری ایران در تاریخ ۱۸ دی ماه ۱۴۰۴در شهر کرج بازداشت شد و «تاکنون اطلاعات روشنی درباره‌ی روند پرونده‌ و وضعیت این بازیگر منتشر نشده است، اما اتهام «محاربه» در تاریخ ۹ بهمن ۱۴۰۴ به طور رسمی به او تفهیم شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/76618" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76616">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/op3QVGiKNb7VjaRWefk7lzUNftuVs8yTCuAKSzBest5e9tkDU-2VOUpHAICLB4plMZEJT4-CXlmvZRKFjmIuwWT1OVpyplMqRVVA1HWvvvO-bkgdTIxyxttpBADGallGx4nfYUEMyhbiGKK_KpihzgcRC7W0jAE-TpMNNdQtNZ9R8pu2_BGg8lZeJcEr24loVVxc6jGKjpiYDr7hDnXhMZI-uYRo8DPrqY5DAjdKfVKn5DwBBN0W6TLMoiYiBTbo6V58Em2_URcekNaCQByjMAhzf8QIDwXnjpxhiB44qvZUyqbK9k60u2HcP7iYt8kwhgKn_f2ThSF36TeoSOZn_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/11113460cd.mp4?token=MlyIBC-TY2Y15Jj58C5qSw6trOaEOgjb_SydgGIbdCHfdIXHbnFMy2OONhTcxpSZkVEd5dQteh3gi2WDHIfeJQ2E8xU2vie3wQMMQ8mMaL2IQP6ITuMJ3R1p1zCY2GGfckLcvCgYfzu2Dxp7uzHl3ctAdWGp6KHU6tx-nmi80p2HvRrb1OULwSrWlIPUHCMtO43eQ60j8IwWEilO3rD5YiYdxncUWCH4pW8DI92sN8h9420H2-lMCc1lFfuHFIdT1UV80jCYZyqjKSkGske9zSKlG_u6NZOWxYfqHePr-9BSX4RoH78afOsbYWP_QTvPXpWcdSQB5gCMmGMrBUm3Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/11113460cd.mp4?token=MlyIBC-TY2Y15Jj58C5qSw6trOaEOgjb_SydgGIbdCHfdIXHbnFMy2OONhTcxpSZkVEd5dQteh3gi2WDHIfeJQ2E8xU2vie3wQMMQ8mMaL2IQP6ITuMJ3R1p1zCY2GGfckLcvCgYfzu2Dxp7uzHl3ctAdWGp6KHU6tx-nmi80p2HvRrb1OULwSrWlIPUHCMtO43eQ60j8IwWEilO3rD5YiYdxncUWCH4pW8DI92sN8h9420H2-lMCc1lFfuHFIdT1UV80jCYZyqjKSkGske9zSKlG_u6NZOWxYfqHePr-9BSX4RoH78afOsbYWP_QTvPXpWcdSQB5gCMmGMrBUm3Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز سه‌شنبه دوم تیرماه بار دیگر تکرار کرد که ایران با بالاترین سطح بازرسی‌های هسته‌ای از تأسیسات خود موافقت کرده و این بازرسی‌ها «تا ابد» است.
دونالد ترامپ در پستی در شبکهٔ اجتماعی خود، تروث سوشال، نوشت که با وجود اعتراض‌ها و «ادعاهای نادرست» ایران، و «هم‌زمان با جار و جنجال رسانه‌های جعلی که هر کاری می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند»، ایران «به‌طور کامل و تمام‌عیار با بالاترین سطح بازرسی‌های هسته‌ای برای مدت طولانی در آینده (تا ابد!!!) موافقت کرده است».
به گفتهٔ او، این امر «صداقت هسته‌ای» را تضمین خواهد کرد. «اگر با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد!»
نخستین بار، جی‌دی ونس معاون رئیس‌جمهور آمریکا بود که روز اول تیرماه خبر داد ایران با بازرسی از تأسیسات هسته‌ایش موافقت کرده و این امر ممکن است در هفته جاری رخ دهد.
با این حال، مقام‌های جمهوری اسلامی بویژه سخنگوی وزارت خارجه ایران هرگونه بازرسی آژانس از تأسیسات هسته‌ای را رد کرده‌اند.
@
VahidHeadline
پست‌های ترامپ، ترجمه ماشین:
با وجود اعتراض‌ها و اظهارات دروغین آن‌ها در خلاف این موضوع، همراه با هیاهوی مداوم اخبار جعلی، که هر کاری می‌کند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهد، ایران به‌طور کامل و تمام‌وکمال با بالاترین سطح بازرسی‌های هسته‌ای برای مدت بسیار طولانی در آینده، یعنی تا ابد، موافقت کرده است!!!
این کار «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این موضوع موافقت نکرده بودند، هیچ مذاکره بیشتری در کار نبود!
بر اساس این موضوع و سایر امتیازهای بزرگی که ایران در حال دادن آن‌هاست، من موافقت کرده‌ام اجازه بدهم تنگه هرمز باز بماند، بدون هیچ محاصره دریاییِ دیگری. با این حال، همه کشتی‌ها در جای خود باقی می‌مانند تا اگر لازم شد، محاصره دوباره برقرار شود؛ چیزی که در حال حاضر بسیار بعید به نظر می‌رسد.
پول و/یا تحریم‌هایی که وزارت خزانه‌داری آمریکا آزاد می‌کند، به حساب امانی منتقل می‌شود که تحت کنترل ایالات متحده آمریکاست و صرفاً برای خرید غذا و تجهیزات پزشکی از ایالات متحده استفاده خواهد شد، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما.
این‌ها چیزهایی هستند که ایران به‌شدت به آن‌ها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است همین حالا، پیش از آنکه خیلی دیر شود، کمک کنیم.
گفت‌وگوها به‌خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد؛ رکوردی بی‌سابقه در تمام دوران. قیمت نفت به‌شدت در حال سقوط است و جهان جای بسیار امن‌تری شده است!!!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/VahidOnline/76616" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76615">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AtPDaVz7lVJPOysn2Z-9ztLIsWeH21raodsTiVO2dwUuTLMD7hrAuKXbP2mcdAsPNUxykbzSRk6IVXNHd9Vpu-TnwFmy8SzwXVN4VTc4QU8VO5APyrSzpt6F7z_UjAKqTrnLGWCNXDkq98c1NAK88udOsEiRHkfZfM-klHM4d8M2yEpPL87WwIp6OQr82iwNnbDqkJHDLID3hE0LqQp9B8LV3SnlpKQhSkqPqd9iWFAp0RxJtUf_83QUMN7hnP7Re56dBiFZ1irm3LgqyO-FHyr6RkOIsW61rdbz13MFO266-q3YL3ni2WRc36hHWU-G9r_5Xh8RnJAnWKTW2q1esQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر سه‌شنبه دوم تیرماه گزارش داد قیمت  [نان یارانه‌ای، نان یارانه‌دار] در تهران و ورامین افزایش یافته و در برخی موارد به حدود دو برابر نرخ‌های پیشین رسیده است.
بر اساس این گزارش، قیمت‌های جدید از سوی استانداری ابلاغ شده و از امروز روی دستگاه‌های نانینو در نانوایی‌ها اعمال شده است.
بر اساس نرخ‌های تازه، قیمت نان لواش به دو هزار و ۷۰۰ تومان، بربری به ۱۰ هزار تومان و سنگک به ۱۵ هزار و ۵۰۰ تومان رسیده است.
محمدجواد کرمی، رئیس کارگروه آرد و نان اتاق اصناف ایران، نیز افزایش قیمت نان را تایید کرده است.
در ورامین نیز رئیس اتحادیه نانوایان از افزایش ۹۰ تا ۱۰۰ درصدی قیمت نان خبر داد.
بر این اساس، قیمت نان لواش از هزار و ۴۰۰ تومان به دو هزار و ۷۰۰ تومان، تافتون از دو هزار و ۳۰۰ تومان به چهار هزار و ۵۰۰ تومان، بربری از پنج هزار و ۳۰۰ تومان به ۱۰ هزار تومان و سنگک از هفت هزار و ۴۰۰ تومان به ۱۵ هزار و ۵۰۰ تومان افزایش یافته است.
مسئولان صنفی افزایش هزینه‌های تولید، از جمله دستمزد کارگران، خمیرمایه، حمل‌ونقل و اجاره‌بها را دلیل این افزایش قیمت عنوان کرده‌اند.
رئیس اتحادیه نانوایان ورامین نیز گفته است اصلاح قیمت‌ها با هدف ادامه فعالیت نانوایی‌ها و حفظ روند تولید و عرضه نان انجام شده است.
این افزایش قیمت در حالی اعمال شده است که نان از مهم‌ترین کالاهای مصرفی خانوارهای ایرانی محسوب می‌شود و در برخی اقلام، نرخ‌های جدید نسبت به قیمت‌های قبلی نزدیک به دو برابر شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/76615" target="_blank">📅 17:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76611">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XbcOgusvJkivbRV5qTkYbjqd0LHd9SFngjM7miCdrQspA7UNlJyTo7T1fJDjdXgE4Cg1ix0rTKgc4NLgJrv-vGxX1tTFJaUdX5GY0rYkg7XYAqz-2hUZ_LSvPTABruZsLYdRCrlrQ_alSwCn05-kLe9p4a3-tgTrxpBmPu6GV_OQZRixXFSRRrtrCKR1q1qmsFlRjZ2v3S_EuVwmjXU0AHkF7EeJ1zBNyIysRWwH4K9meOujDQXdgZpLP81_tp-LgbZWbhivRQGwuxDYDiFOpp33NKH_1GEyBpl7VhI054t_K3Cyc7C7ABCg8f-UoVANSFtrAez9GxImFXOsfqsRKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TmMIhEVfiJ4YAmuxJl9L-2ezhAAy7HTtNvs98j6886g_pGpILg51O2gF7OU1Ei2wkJCoAMNIMtg2ZO3_0GsZD-WD-6r1CVxhAc-i6a_umpdY5XF_WFXiDLqRotVLujVAnWRugASeM8tXV8cpLs4680WzfkUlrPtvHQ9pPDZeFg6SxZCwGh5Fk27J36E5h84_flqmMdlJuNgBMdpkKy5ZBJOKvn1O-s78UpYT58eTljFV4UQbmpa5mI79UWegGrC2wHW5oI5uZj7j9WAwO5iYmusMVZgMqbdiLfcKcuwKT8g3sut9ZWgmxyaK1j0MPmVP3y2Bxzngpq6dpIbh6bHPug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/APs_BzI45M3YbHLOZjMrpPDPavW8YzZcCDdgOBq6LzI_lBZ716_w6FowLiZf7iOfhG6Itz4a1MhE-ql2ejfLX0kvM0dHzrJAGfqC4Al0Bhs4Sbox1PVE_J8PO3WBVtizqxVdgJZcolgTJS9W5GigfHRCumkkfNEX_XpJZ7BaOXIDo63ASc51hSRuudW4gFjORfSPIHPyLL_hmD3l_LekDLewCjFujshVP4YYTKX4j1zD2-kJDT-A4I0N3_YD5ltdd8y7IzhBBOz-wxfe0R1MFjX6M3Tj-BROGeokORmxNQd_wBoqEQkTGVkEAVDGjntfRq7JM8rZX29y6psw0Qfa1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=vOD5ce5L1aDtr2Q0QGVWagQXh1bcQXco3f5PMgfFQOFQDWI8_DwvFU_1JKii-MR_K5XtzS-bFDQj3sKTU9fqQFCb1rQCWQzCtQAPOQ-HBD37yDN63EMj8eHpuiuSms3yRGJ77nd8FJlKojGnYXPlTupYAi52jAVZzloR51ajPrgLATrIRihkwknI4rljv5vtzZrG3YLwK7SJvetZZ4ymjp1saBB88jHggoxztVf_4Q7Zenp7NcQirbTiXGicqN3MhPiGIqDopq4QpwUMw94-qbnZpg-oaD6GEqYuqQAJv0wrDuNF7CTR_CGlqL0hWjqELhEv_VtdvHuoeP5ax-3UGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=vOD5ce5L1aDtr2Q0QGVWagQXh1bcQXco3f5PMgfFQOFQDWI8_DwvFU_1JKii-MR_K5XtzS-bFDQj3sKTU9fqQFCb1rQCWQzCtQAPOQ-HBD37yDN63EMj8eHpuiuSms3yRGJ77nd8FJlKojGnYXPlTupYAi52jAVZzloR51ajPrgLATrIRihkwknI4rljv5vtzZrG3YLwK7SJvetZZ4ymjp1saBB88jHggoxztVf_4Q7Zenp7NcQirbTiXGicqN3MhPiGIqDopq4QpwUMw94-qbnZpg-oaD6GEqYuqQAJv0wrDuNF7CTR_CGlqL0hWjqELhEv_VtdvHuoeP5ax-3UGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«امیرمحمد هموله» ۲۴ ساله، ساکن شهرک صدف شهریار، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ بر اثر اصابت گلوله به ناحیه سر به شدت مجروح شد.
او پس از تیراندازی به بیمارستان نور شهریار منتقل شد و حدود ۵۰ روز در کما تحت درمان بود، اما سرانجام در روز هشتم اسفندماه ۱۴۰۴ بر اثر شدت جراحات جان خود را از دست داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/76611" target="_blank">📅 17:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76603">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O9uAS91epL6_oQ7tIYBurBZS4n5CmK3f-4guJMmWVZC-MQT3zj5Desp2lisFBxSc59A4M_BsHTxNEg_E0x2oIiKga48A-t6-e38CjjV2X3wHXN59-ctazTr7K6SbgRw7TWzfzHFbTBkceT2vSxFt0uy7QU1HmRO-69a6vGo76lqrCm3tAm_B16QyLTG4syjOxHASC4EdSJAngkI11fsKm6xO-AjYAsdFmUsUxS6Wzt4NoMXlt-Uj_tt9cASd6iZnfW8wWa1xH5eo2SD9KgUAr5xHOnEJkE4bqTH7i-HbBI11-CoL2P40IpDKB4BP16jr7pW823S6CMGCTUEuYdPCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fLcmTCt4MqHPDyexflRrcDqblSBevFycXyuPpJv1-TMkn-WPBkYoZCCxTaRUJOAJV6MdOC0m5WRtrYJhtbLBcphc1KBp01W03BMntRU9AjoI6l6B8uLH7wa27IoVJuijp-3Y39FjqcFByxzOjppf38UqbK8wmzOOYNzFUjvnDStcJfY_s_IC5KUQ2PX0UGHHrF8snSF3qNbtW9V4dzO-M3l6XLY4DjnE5sdcvpjdDAdbbXEQenDP1MVswJiYezRPcGNE-Zx5utGU-oVazchrWHQpMhuE8DIJQv7u2MF4xN-IhZ9OI4ZdW3p3tuMTZ3LQFyf-5ZdtSO3TawPqhFnVXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jwwF3ZxU63rOJfZ-gcW5kGuvDLuVCNBjzUGsq5hyNSTBoyIbsQA84ZbsM35jW5Ir6mcs7LSYAyZxWgO1WEvWGyFONBYGXQ7C1KtM6hFy2jBMpIS-e2pZaLxthx4t3YM-qopRONu08Pw3gyNgJiTk4wh2Tq6ER5sRFTM6b2yDJAOXP3im56SQ1Kk1FJ8XFlrstPi4nvHuATqw-7ZTxdx1FmnOTZQ0rhM-79l3YRnF-_VWhzX4TOsR5p4pCkItHbKwGXS6-_0meF6PgHQUS9dXVAUfU_Nn5oFlwJcf03oDgxXYA2qF07tNBT_bAF2gUGOekBbALLtAWi5BzKot457aVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RsqkTKdKpKNVkdFWZq0AhqRC2iI4pISaC5-XD2_DggeVEpIYGYT1-Ks663yC4-C331r1rA_uLvTfLLT7E-VBJCf5g0VFQRBA75nu95-x1UUvlcb9jAeJHPzCTzxZ4C6ANHRwI9WPGm4o-fFwdjSojtRmNBMXGxBH6cmwkfb8V29yuQz9tQ2z0esiEvVXOxZymh0NilOb0u9aiyy6GKlkb8XkidFa3WxxqkOJezK2W7eVrxo_XTm8ulm7oQsHYQ-s6kY_seO004q7GldB8dLF3UgLJM8s6RHdVMt43WouatJCsdkASNJCB8wr-N3UH656SwGsK-Pct0e2IHGIP6R2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/davWpWtRvtLk4zSP5Vts1KAl2YAQgm0NZYBpfUda_xryDAKwBiR7xlytmGUEh_vYhbVSPWwBU1shYSkNY2yNY3YKy_EhvKRSYagM0tzb8iMzumsIWnuKK25nUfUbe7Mf4tnHYJrt-wMjSGf-ZmZ7AaQmJKYsjNUsZ98EGOyTVaCcoEMAFLtlk3o8PLFeNtyIKzFEGcKPjKQUnW0J1tyFInCm8H1yCDhuR-Bp0IR2oONUegYafallk9x-7DsGL5PW2eEIgiN7IXywNbdxGzWKNoq3w7O2dl8PaSMmYlKlpXBngWMDsWa6VfDmjoFzkezYsNBLiKff5NGDOez8ndMQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XjUwbRmxopVkqtx2YkjfQwXgsBDQ02NEHGe_P5B2x3Jvc5d2hNjIBeG1MSQ_ktzhYZACUjjmFcJ-wkeLmdAx3Vs-GwME1XVeVZ0AnKp5LBOjsQH3IECoTVdCI8KAOUEolTiOSyf_cAr8mAXePsgg96N_Hk0j9BiaE-K4MP-0e4OhHpzzsqlh89xa9jAvCWTo6OKtBrUKc_TQmxN9Epzyb_Oltnrw6o3VgscpW-fUUDViPGtae1e-LkzoXMspeW9NJHiSuMJNSCQFez_0ULCkSVOqI2D_xMY3S-GP-qN1lD2FtJFGMfCQTtkj-wD0X3obUhNZ6qjSPEM1aj-MFk3iiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T_rDoSPM96hnqyKetFpAiEJ8qALIdHwVWRUF0HNi_nszR-CUHj3ytg9GXA06XjDmrvwaz8Iaztf4OlnsUzBavq0_qCTCICHaNSTbbjV1o4saOytzs1YINXC61dDO1RsUJU6jK_1bqD17zKO0hIzeYbAx9z9lxCYEQF35hfTDXHJ3ypTV1_cNO5Sz0bRk8nMr7IDqqQyiU8eh71VTYhFBfe-Zl0rL1NKngqMxo0j9On9rqV0B_Mj2gDsiKGjomfyY8swUBLrc4CDxbT8g7YJOeW8OghesDyeQo8m1jE84vNWbvUU-Tg1TVyn75LJkdnn0zknP-pWS05L4JEkjXd5YkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TV6oBnl-j3cxv9fNvelqZaLah6eouiPc8KbVek1F49Ux0PKNOaLmnM9jzO8Hu1-WcwpiKlvpuTXmr6mkpvcz8uu64lp9-mjZaq2Lb9rRjRs-RJ-e1ZLNv5FnQXUj2U1ZafOJQYAo6vr__hMnEqfEgHvtrXYOVpa7YogUrYe5rBkjKYA6mAdYhwlPNaEI-mXbG2JopK8f6x2xsZaJluWQ4rYlNckhCevkpru9Y8iWZYxsHAqGwbdEcN2xiT8EJPuknpUj9vBI9nnHy6PpHQamsvL-bV1cV5Xf9TFIixKxax2Z--9Hj5znH0sCamFKyEiG9zNt-C2ghJ5bAqpHojMmkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ پشت سر هم پست کرد + ترجمه ماشینی
دونالد ترامپ، رئیس جمهوری آمریکا، دوشنبه عصر نتایج چندین نظرسنجی مختلف درباره توافق با جمهوری اسلامی را منتشر کرد.
از جمله یک نظرسنجی مشترک «سی‌بی‌اس نیوز» و «شرکت یوگاو» می‌گوید که به عقیده ۸۰درصد جمهوری‌خواهان، این تفاهم‌نامه «بهتر» برای آمریکا، و یا «خوب» برای هر دو کشور، است.
در یک نظرسنجی دیگر، ۶۷ درصد می‌گویند از تفاهم‌نامه اخیر صلح میان دو دولت حمایت می‌کنند.
در نظرسنجی دیگری نیز ۴۷درصد گفته‌اند که این تفاهم‌نامه اثر مثبتی روی نرخ تورم و توانایی مالی خرید مردم آمریکا خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76603" target="_blank">📅 02:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76602">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSn3xYE1eXCFPFUMebEP5ZKu-FYqyRGtmLj-wJcbYV6fiedmSnM0uj8SEyAD2Arj8l_fDpWGkIQX0SUIufITgnN1mRshWsHfr3i1KQZ86V24ZN0VLVXxwi_P36_6AzJ5IAf2F_LQx_lUXbLJJd5l5PthPZ1Ic1hKZCElJKnUzhuAZMQTKTJg6vB9bmwWRSWKF97Gq5u4Mvqs0iM0QtHesbjvHLHfOFmco2bWLXemf9v0HNGxETx1IbF3H_0Qc-mNejOUihXNx0_1Pcc6kXffOHPqvvdn3HzYrpZi-PGSMISBHZ1_ndt7DawmsYDufD5SX7g42F12Wasqwb54uDnnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، سرپرست تیم مذاکره‌کننده جمهوری اسلامی ایران، در واکنش به صحبت یکی از مجری‌های صداوسیما با انتشار پیامی در اکس نوشت: «در یکی از برنامه‌های صداوسیما دیدم که گفتند کاش فرودگاه مهرآباد را می‌بستند تا تیم مذاکره‌کننده به سوئیس نرود. به آن عزیزان می‌گویم اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد.»
پیش از این، روز شنبه، یکی از مجری‌های صداوسیما گفته بود: «در کنار بستن تنگه هرمز باید فرودگاه مهرآباد را هم می‌بستیم تا مسئولان برای مذاکره نروند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/76602" target="_blank">📅 02:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76601">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ: اوضاع ما  ‏در مورد تنگه هرمز خیلی خوب است.
‏دیروز نفت بیشتری از هر زمان دیگری از تنگه عبور کرد؛ بیش از   ‏هر مقداری که تاکنون از تنگه عبور کرده است.
‏احتمالاً این را می‌بینید.  ‏ما با یک فوران نفت روبه‌رو هستیم.
‏تنگه کاملاً باز است.   ‏این را می‌دانید.
‏خواهیم دید همه این‌ها چطور پیش می‌رود.
‏اما ما دو چیز داریم.
‏ما یک تنگه باز داریم و کشوری داریم که   ‏هرگز سلاح هسته‌ای نخواهد داشت.
‏هیچ‌وقت، هرگز، سلاح هسته‌ای نخواهد داشت.
ویدیوی بالا:
به تشخیص ماشین، حدود ۱۱ دقیقه از نشست خبری ارتباط مستقیم با ایران داشت.
متن فارسی اون دقایق
ترامپ در پاسخ به سوالی در مورد تنش‌های احتمالی در تنگه هرمز گفت
تا زمانی که ایران به ما احترام بگذارد، نمی‌خواهم بگویم از ما بترسند، تا زمانی که احترام بگذارند اوضاع خوب خواهد بود. 8:15
@
VahidHeadline
دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه عصر گفت اگر جمهوری اسلامی «به توافق خود عمل نکند یا اگر رفتار مناسبی نداشته باشد، من کاری را که باید انجام دهم انجام خواهم داد.»
5:00
ترامپ: نیویورک تایمز جعلی گفت، اوه، وضعیت تقریباً همان چیزی است که چهار ماه پیش بود. نه، چهار ماه پیش، آنها یک نیروی دریایی داشتند، دقیقاً ۱۵۹ کشتی. آن از بین رفته است. کل نیروی دریایی از بین رفته است. آنها ۲۵۰ هواپیما داشتند، همه از بین رفته‌اند. ضدهوایی آن‌ها از بین رفته است. رادار آنها از بین رفته است... همه چیز از بین رفته است. رهبران آنها از بین رفته‌اند. کل کشورشان از بین رفته است...»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76601" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76600">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=dERTlAXlRS90YEAphh7N4QUhvoRJ9YMfzuRciEHMdWhVPlsYrxtabutYsHOyPTiuqY0riMKx9-_nR4PHGo18xWzr4QF96FxTDyEXJNap_62fy9qVhOln9tMPIK_GsfjbpfTcQm62wq9f8L7G2YmAGTXpMpgPKGcQc7o_NESzwk44AZK8g_rQbWQPjx0d46YxuoHZuNad6AIBC9BUBWlALFoa1SZpuz6esomdg6NIwO_20YLU6M62IyQR9vt_tiQDquZkb7v9iYK_mew0ZTLzzxLzPFA879PYSHcOZxUt087L8G1FqNoB4E4sLWGTLPpinDRlvFTjs6B3OUmgMqurhA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=dERTlAXlRS90YEAphh7N4QUhvoRJ9YMfzuRciEHMdWhVPlsYrxtabutYsHOyPTiuqY0riMKx9-_nR4PHGo18xWzr4QF96FxTDyEXJNap_62fy9qVhOln9tMPIK_GsfjbpfTcQm62wq9f8L7G2YmAGTXpMpgPKGcQc7o_NESzwk44AZK8g_rQbWQPjx0d46YxuoHZuNad6AIBC9BUBWlALFoa1SZpuz6esomdg6NIwO_20YLU6M62IyQR9vt_tiQDquZkb7v9iYK_mew0ZTLzzxLzPFA879PYSHcOZxUt087L8G1FqNoB4E4sLWGTLPpinDRlvFTjs6B3OUmgMqurhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس، ونس هنگام ترک سوئیس، ترجمه ماشین:
🔸
سازوکاری ایجاد کردیم تا مطمئن شویم نه‌تنها تنگه هرمز باز است، بلکه باز خواهد ماند.
🔸
قیمت بنزین همچنان کاهش خواهد یافت.
🔸
سازوکار درستی ایجاد کردیم تا آتش‌بس منطقه‌ای تضمین شود و درگیری‌های اجتناب‌ناپذیری که پیش می‌آید مدیریت شود.
🔸
ایرانی‌ها اجازه داده‌اند بازرسان تسلیحاتی، بازرسان هسته‌ای، پس از مدت‌ها وارد کشورشان شوند.روشن است که ما این رژیم بازرسی را تقویت خواهیم کرد تا مطمئن شویم آنها هرگز به سلاح هسته‌ای دست پیدا نمی‌کنند.
🔸
بخش زیادی از تیممان را آنجا گذاشتیم. ایرانی‌ها هم بخش زیادی از تیمشان را در آن اقامتگاه گذاشتند تا کار را ادامه دهند.
🔸
این دارد بنیانی می‌گذارد برای چیزی که می‌تواند خاورمیانه‌ای واقعاً دگرگون‌شده باشد.
...
خبرنگار: آقا، خیلی سریع؛ دیروز لحظه‌ای بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما دست ندادید و بعد او از اتاق خارج شد. آیا احساس کردید به شما بی‌اعتنایی شده؟ آیا فکر کردید این کار از طرف آنها عمدی بود؟ شما آن اتفاق را چطور تفسیر کردید؟
باور کنید، در چند ماه گذشته زمان زیادی را با ایرانی‌ها سروکار داشته‌ام. گاهی آنها را به‌عنوان مذاکره‌کننده‌هایی بسیار گیج‌کننده می‌بینم.
اما ببینید، ما یک نشست خبری کوچک داشتیم.
آنها آشکارا در ایران از همان حمایت‌های
متمم اول قانون اساسی
که ما در ایالات متحده آمریکا داریم برخوردار نیستند.
ما با شما صحبت کردیم و بعد چند جلسه واقعاً خوب داشتیم. چیزی که برایم کمی خنده‌دار بود این بود که بعد از آن جلسه اولیه، نوعی توفان در شبکه‌های اجتماعی شکل گرفت که همه می‌گفتند ایرانی‌ها می‌خواهند بروند. و بعد ما حدود ۹ ساعت دیگر با آنها صحبت کردیم.
بنابراین فقط به رسانه‌ها توصیه می‌کنم کمی به آنچه از شبکه‌های اجتماعی ایرانی می‌بینید بی‌اعتماد باشند.
آنها می‌توانند مذاکره‌کننده‌های گیج‌کننده‌ای باشند، اما احساس می‌کنیم در حال پیشرفت هستیم. ممنون از شما.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76600" target="_blank">📅 22:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76599">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W-pf-hYx6A1tYt4xuMe3aA2h1mscXpeK_Yf9W_G9nlLdk3UGNpc69h0pjfprBj6bVgl3Qmc9a6LQaRQWckWqIHV16NUxTNUCDI_PHB5sDStJoOiFO5otyxQ7UqdaC_t9HWJAm8UmTd8gYf-jJsYZ11Otieu2IvdVUo8IIrww25s02C6CFZbeobK6mrgLfAy-KGC571SjBkj7wosaNyUMgUivZIr4UIuvSMQHE7pHfwbuVlw6BsWPLMIAUcGWFwC8dScQFVyI_0LTIuTWF5HBYc7BVrAkR1v4UG2OwYha-taebMJ7Wz-qWGKU5kCyiWXNM-CETdCbuDNalPfoA1kUtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
همه کاملا آگاه‌اند که ایران موافقت خواهد کرد که برای تضمین «صداقت هسته‌ای» در بلندمدت، بازرسی‌های گسترده تسلیحاتی انجام شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76599" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76598">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqO49Xbvs8_s4vZvhFJ1--6-2thxXDx9OKUuUCAUEG1jlUmMj2se4NzjbglFkJHJUw3HSDxHSMdOOYnwsUR61YXoa8vCh7WX9CeRUkrf2U14ac6iC2Qaaj6vjV4CbJ3Nj3BILwWftMCZilcOA10FJIQDA0DlxfKYm3ByUxXdjltDc0kLVhxqJe5s9X6H3buV_qH7y-ROzLt2RLlPjtcXYLBGOqbj-SkRA9WTEMu0yPiqpW3EOsmSuTAvAwQydyOQIQoak5apCfNXKnomZTVx4T3tBDzF9kLL5BNyn0wJG1mwpffT7wKbTzBLyh83j4qI5Mc8AuK-9oCS5Qt57RFxhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز دوشنبه، رسانه‌ها خبر دادند که محمدباقر قالیباف، رئیس مجلس و رئیس هیئت مذاکره ایران، که تازه از سوئیس به تهران بازگشته بود بلافاصله برای دیداری دیگر به مسقط، پایتخت عمان، رفته است.
به نوشته روزنامه هم‌میهن، قالیباف در سفر به عمان به همراه عباس عراقچی،‌ وزیر خارجه، قرار است با هیثم بن طارق، سلطان عمان دیدار کرده و در زمینه ارتقای همکاری‌های دوجانبه و تشریک مساعی «برای تثبیت ترتیبات ایرانی»‌ برای اداره تنگه هرمز گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76598" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76597">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l4V87FsK1vXXAfzksFMEWts2uWYNfIHa9dkUxNbwfHNGqg35Ee3YEhpTwDItzPa54NTiLLIprJsT5jrlayrqH5R-PcOmRV9pAvKuPQ18xo1TpKUqW73ub1KXqmDRgSOyYVgAcsH5srThM3aAsyZGJfA4b16CqmLdc9YY1EqeFdlJFi5vZ98p041_RS-NcJosLlp1KvOFx2jpXFmFUgawx6S9Xf0285t-b9XvXzP4aIWPgV6Tvc7VpQc2hKfbHMHPMaaQ-unZKDUoGVuUPACAGc5QCaESuBQxPfqeD72EdP_TVkZ2h5whQi8IvcaJKUWNg5LwsYyurUBytgYH8JP2tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه نوشت اظهارات جی‌دی ونس، معاون رییس‌جمهوری آمریکا، درباره بازگشت بازرسان آژانس به ایران کذب است و در مذاکرات سوئیس هیچ صحبتی درباره حضور بازرسان در کشور نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76597" target="_blank">📅 20:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76596">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=FlykQUBRvA2I_ixhRchB0qs9fxYELAmIaHtpi_nzPD39RRWNZDupsw41KvXALqXYNXfhRuCl9DRw6zKtjIMdesrI-NcDi7LJjEAXMxUpp5lemQQak6dkaL0XPu0I4aiFILFNKPvX7G_qxQXLCYp1j0A9CQCjUGhjJclPly0j_VjNFkgFGpQ_cUcx3jKhK6bVf0qHws5Uy-5jtVdRAVewpveQH4zQLkXOklUd3Zvhq_Kz26QxlEUIy9KpfgVHTs436IVWGjebppgHvlTiKZXdoq91RklR6P4Dvbci3KodM8QkgTnz6oiGvnLRElppEXcFaKrbst-TP867Wvchwxspuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=FlykQUBRvA2I_ixhRchB0qs9fxYELAmIaHtpi_nzPD39RRWNZDupsw41KvXALqXYNXfhRuCl9DRw6zKtjIMdesrI-NcDi7LJjEAXMxUpp5lemQQak6dkaL0XPu0I4aiFILFNKPvX7G_qxQXLCYp1j0A9CQCjUGhjJclPly0j_VjNFkgFGpQ_cUcx3jKhK6bVf0qHws5Uy-5jtVdRAVewpveQH4zQLkXOklUd3Zvhq_Kz26QxlEUIy9KpfgVHTs436IVWGjebppgHvlTiKZXdoq91RklR6P4Dvbci3KodM8QkgTnz6oiGvnLRElppEXcFaKrbst-TP867Wvchwxspuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تا وقتی که لازم باشد در جنوب لبنان خواهیم ماند
بنیامین نتانیاهو اعلام کرد که موضع و دستورش به وزیر دفاع اسرائیل تغییر نکرده است.
نخست‌وزیر اسرائیل نوشت: «نیروهای ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم علیه خود یا ساکنان شمال را دارند.»
او تاکید کرد که ارتش اسرائیل «هیچ محدودیتی در این زمینه ندارد.»
نتانیاهو بار دیگر تکرار کرد که ارتش اسرائیل «تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهد ماند.»
در مذاکرات ایران و آمریکا در سوئیس، هر دو کشور تاکید کردند که حفظ آتش‌بس در لبنان از موضوعات محوری است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76596" target="_blank">📅 18:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76595">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lwKG5dyzOYmXilGUCKm-qyz4PhvYIl2eJDpK0NEZe4yDlfKAzj8XFnK_ZRhrVpY7L6Gxi_jcIpV_REG3esOlFuMOW86wIJ0n9uBh-NLM9oEVkJE41sJpp6nfSWaUybvmT1Flfjt1EkPd_qMzze2BsHsq5LICNcjyMwdII83j__4IaEjd49G7UEeGZ1qk4c16lDQtNh-4c5467eps7LuTTnFsK-uTK2lPMSIErnDOTtBN0tiylJMyi0uxNBYzMa8s0_m17QqHlc5uKLHeXm4eUr7hoVR2LH9Ki1k2PJ2f5tHKusr5jtFsiYPfyz9E3vXv8layzCvTl2TA9pOzMnuMkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا با صدور مجوز عمومی، تولید، فروش، حمل و تخلیه نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران را تا ۳۰ مرداد مجاز اعلام کرد.
بر اساس این مجوز، تمامی معاملات و خدماتی که برای تولید، فروش و انتقال این محصولات ضروری هستند، از جمله بیمه، مدیریت کشتی، تامین خدمه، سوخت‌رسانی، ثبت و پرچم‌گذاری کشتی‌ها و عملیات نجات دریایی، مجاز خواهند بود. این مجوز همچنین شامل کشتی‌هایی می‌شود که پیشتر تحت تحریم‌های مرتبط با جمهوری اسلامی قرار گرفته بودند.
در متن مجوز آمده است که واردات نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران به آمریکا نیز، در صورتی که بخشی از فرایند فروش، تحویل یا تخلیه مجاز باشد، امکان‌پذیر خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76595" target="_blank">📅 16:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76594">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PoawJ1Mtoa-FzMmiuuk0povbqGd99U7H0YZYnV5OdnABdVasVrYBWC-trSHhKDUDp2KYrk7nNRizlPznUcCK_sEt4veJ5yjJ-Opz0h1KRcJ1ZqP8Imadeky63RCps8Hs46PiMvGq_OpHZFaIbzmqeac5j2Quq-fa31e5azAcLuxsbh9NQTBIJwrY1zETcTDAJJkbamc7GAUAoV5DhdtQtripCQB1zdoN7ymy4CqCwcf3Sj2NZtkIBHLwCaunaEUIU-AezDq9WDB1OzmBgF_j2UgVUi_0HXyQXARsXWNWN-Cc6P0Ju_mRAZWBRAOlrsyNh-Z4qWmGhSaE_ZC8EDbxSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس گزارش هرانا  در خردادماه ۱۲۷ حکم اعدام اجرا شده، ۱۹ نفر به اعدام محکوم شده‌اند و حکم اعدام ۱۲ نفر نیز تایید شده است.
هرانا همچنین از ثبت ۸۰۹ مورد بازداشت در حوزه آزادی بیان و صدور مجموعا ۴۹۳۳ ماه حبس، ۷۶۶ ضربه شلاق و ۵۱ میلیون تومان جزای نقدی برای ۸۰ شهروند خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/76594" target="_blank">📅 16:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76588">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Enc1XHqggljXJxSC2pO8jwg6uYxXqDXdpf9CVGcPBEd9Ay6584u4ESuoXZNzENCHkcrDH9xegUy6MTY_XttOuegJCiSBl5WYDaulye8GwZaribUltrpTJdAw7dooviV4GobUGx8M1OSarmB82wKIYf_mFnUL1WQ0w8I9mpngPGX22-6q0DqAHaIgHWG4SvLJ0HBdQwF3ZKMq5ELYL7DpO5djcg7IYyDkmKNWfizkjIoh-KQuZPGKgk0m2Lm0ZnJIclXokZ4x56UeQ-C-Z06NT-tvLAk0o4etH9CASWwXjRXg_g9Ff3EP8e6D-2_PNn2-72HDHaUMBDM5iYgahwFhEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y760EsyL4atg5OR5Cc0xeDjROLTh0gnLybfOspDOdiApV1T-AMq7IsvW8vo11HPwomOppte6KJHW8FpGp2_EOCGGLUXWN6w2JBEi047GWrRflsrBiaapG8-GLYfMZR8jKl4_tiANgm41dmkbNUGPGv-s1Or-WEeTeK2LlqFDYtZeR6imFGAsXWBb0ktwr7Ud9oTdMlkcwjqraYDEr9URoBHl1NxiMs-YrXWZdaOAUca8hpKp75GDZS25FRul9UgpUGzz_v5iga1rzM_4HuEhPneE2vemC0O3hXnl1G81agXsK6d4fwr0Jakn4KD9WeKlRYZjSMmY41SVBFxuot2TUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i6rW0_K6tT3ZtRoVVq5ziCMfvz1qO5RkpVvM0EmEW9PLzwp8fk1hXgc9z58WsYoxVWBSKdV_hE7NH1rnod__NP4R1hlcq04DQqpKsa8atE32jzTalormfznMoxuVGB3nf3O8Q7a9XyvXawdIyUTupA094PYNONd0fN4jkBFP7rpmf8JvTfutLpqpwgn8kZj73aPsNVToxqEdTrSw7fuanyHFMfJNb24uQ9c0w7luzgS0mfMbm2vIak68zJhNvlM_CY6HD7Wo_-aTUP5m8Y07IjeP4MRj3CHDFNbmB7IiOALn4BxvqZxjmxbY93EUiG3VnhQGLbySBKwmVcjewzX7PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HNWr-D8PwR34-x_1-pNg1iW2j8eAuQ0Y6bk3baVJskhd8lEWkTrJ5HRpieGbSJg-G-5VqTaKq3liPM-eA6bz7RUFJUJAtcOSvVF6tNj-wpuNVivqai7nnONeXVJaVb720-Mwl5aFb54Q0IrwxL5vjcSR5c1cjEcgabXwW8Jd4plw3CA9U-AA_6SpYmxxqHIdNI_67drlNksFg9VKWvnkaOajdLANTA5_HFucTVUn5fr1U9yb7TpZUgA4iueKQyGvWMfpC0M6EoIJjOZFDVApuik6P6jnobFD7ZIcs3c-VqSNy8hgRRZh6Lfjfgck8xwqfV8jfP4Kv4T24wQRSSp5rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SDOy45Es3VfdK_jkKrWJ2HxNQQ3JiTP4NpmDZkAHmY7d2Mk7L6c_A5tYs6qZYOwdrhH0-yyFseUwtLmj_YnSmIbz1Qxi9qvrHCId6mWaLdbXYMPTXYf-o5IE0_nvU_ffWlIQJcZcyibleUXU0H5WP9RSGONoIaVmE3o7Le2KW5g7Nl02za7vrlIoGb-gkyg2VoFv5BNCn6p_Rpf3MDDwuDxX0Tv4CSZLavDgyneKa9Tovvnda3g_UI4KGn9erH0BhA14erDgZEeVhlSJAJfnYg_afYnxwe4_eTWAR2EikvORufAuBmNSl_oNxHqjLWfSQs_DeSZVYgAcTWhuwgJkDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=lrXAYrCyCXyLXuF2BbFvNM7lXJ9EBzRG3Z5-NU984XSh8mBY1SQSfB56Uc95mJ_mZL3cVmxpt7yb7-J5KDlvza5FQVnhI9vtwNEb-5cGKKFnyHUqYBXo69BqY0NPwBpKjMQM-pDAJ0LUMTmyg5V_lxIFAjGgvARW-Wggmp1nEChmO7jryCg69QC-k5lHtWKaQboug-kBv_G2zYR3hOL8zwRdqKxmQ8CXpLkyX0o712NBzZIjIdkMcjcXgBwbtiUTMM_DjTqJ10ACrBZCjatSRAWG93S2zv7Ixy1aBEW8oPcub0vlSDuzGXO3vCwI_8s8ERii5MudUms2GaE9YXnqzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=lrXAYrCyCXyLXuF2BbFvNM7lXJ9EBzRG3Z5-NU984XSh8mBY1SQSfB56Uc95mJ_mZL3cVmxpt7yb7-J5KDlvza5FQVnhI9vtwNEb-5cGKKFnyHUqYBXo69BqY0NPwBpKjMQM-pDAJ0LUMTmyg5V_lxIFAjGgvARW-Wggmp1nEChmO7jryCg69QC-k5lHtWKaQboug-kBv_G2zYR3hOL8zwRdqKxmQ8CXpLkyX0o712NBzZIjIdkMcjcXgBwbtiUTMM_DjTqJ10ACrBZCjatSRAWG93S2zv7Ixy1aBEW8oPcub0vlSDuzGXO3vCwI_8s8ERii5MudUms2GaE9YXnqzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجه جمهوری اسلامی گزارش داد «تحریم صادرات نفت و پتروشیمی تعلیق و محاصره دریایی برداشته شد.»
علاوه بر این، عباس عراقچی اعلام کرد برخی از دارایی‌های مسدود شده آزاد و طرح بزرگ بازسازی و پیشرفت اقتصادی ایران اجرایی شد.»
آقای عراقچی این موارد را در پستی در حساب کاربری خود در شبکه اجتماعی ایکس اعلام کرده است.
@
VahidHeadline
معاون رئیس‌جمهوری آمریکا اعلام کرد که در گفت‌وگوها با حکومت ایران پیشرفت حاصل شده و جمهوری اسلامی با ورود بازرسان هسته‌ای به این کشور موافقت کرده است.
جِی‌دی ونس، روز دوشنبه در سوئیس گفت که گفت‌وگوها درباره بازرسی‌ها ممکن است از همین هفته آغاز شود. ونس درباره زمان آغاز کار بازرسان هسته‌ای در ایران تأکید کرد: «احتمالاً همین هفته، شاید از امروز.»
معاون رئیس‌جمهوری آمریکا افزود: «ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم. گفت‌وگوهای فنی در هفته‌ها و روزهای آینده ادامه خواهد یافت».
@
VahidHeadline
معاون رییس‌جمهوری آمریکا، گفت یکی از اهداف واشینگتن در مذاکرات، ایجاد سازوکاری برای نحوه استفاده از دارایی‌های مسدودشده ایران در صورت آزادسازی آنها بوده است.
او گفت هدف این سازوکار آن است که اطمینان حاصل شود منابع مالی آزادشده به مردم ایران کمک می‌کند و صرف حمایت از فعالیت‌های «تروریستی» نمی‌شود.
ونس افزود جرد کوشنر با همکاری مقام‌های قطری طرحی را ارائه کرده است که بر اساس آن، در صورت آزادسازی دارایی‌های مسدودشده ایران، ایالات متحده و قطر بر نحوه مصرف این منابع نظارت خواهند داشت و باید آن را تایید کنند.
به گفته معاون رییس‌جمهوری آمریکا، این منابع مالی برای خرید محصولات کشاورزی آمریکایی از جمله سویا، ذرت و گندم اختصاص خواهد یافت تا در اختیار مردم ایران قرار گیرد.
@
VahidOOnLine
جی‌دی ونس، معاون رییس‌جمهوری ایالات متحده، در پاسخ به سوالی درباره تهدید تیم مذاکره‌کننده جمهوری اسلامی به ترک میز مذاکره، گفت: «آن‌ها تهدید کردند که مذاکرات را ترک خواهند کرد، یا دست‌کم در شبکه‌های اجتماعی چنین تهدیدهایی مطرح شد. اما ما دیروز تا مدت‌ها بعد از ساعت یک بامداد در حال مذاکره بودیم، بنابراین آن‌ها جلسه را ترک نکردند.»
@
VahidOOnLine
گزارش‌ها از سوئیس حاکی از ادامۀ مذاکرات فنی ایران و ایالات متحده، به ریاست کاظم غریب آبادی، معاون وزیر خارجه ایران، است.
رسانه‌های جمهوری اسلامی نوشته‌اند که قرار است دوطرف روز دوشنبه اول تیرماه در مورد سازوکارهای اجرای یادداشت تفاهم اسلام‌آباد و تشکیل گروه‌های فنی مربوطه با یکدیگر گفت‌و‌گو کنند.
با این حال تیم اصلی مذاکره‌کننده ایران به ریاست محمدباقر قالیباف، رئیس مجلس شورای اسلامی، سوئیس را به مقصد تهران ترک کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76588" target="_blank">📅 16:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76587">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MP3s8ZehjguUsLctmnc0uorL2xm0GbeFYDlWU0O1eT_EzIHqOYPWAjgO7K1xxkrHerizFLSKGvhyGU1IUJ4u7zQw5g1lCig8kVT7jg09c9tdqxwJ74m1IXzHc0mALv3c5jGEJp1BREefqbOkeqoySorRt8WjUEtZUEbaUkCTef5yFOtUcbn031vhNQgXaA4YXOjn7w5rHL08Eb2RtIVjWwy2VhMWXldfzvqxeTg403q42mlvNwZnEqSgf07JIedcoXruQNjluixas3m1Z7Tz7_jkXITfwqsuO53HbKalTlwyDCn3ziVOZT_l-FziVPQP7plsGDwmngo1DgkGrbRQ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میانجی‌ها اعلام کردند ایران و ایالات متحده روز دوشنبه اول تیرماه توافق کردند خطوط ارتباطی مستقیمی برای باز نگه داشتن تنگه راهبردی هرمز و پایان دادن به درگیری‌ها در لبنان ایجاد کنند.
بنا بر گزارش‌ها دو طرف از طریق تشکیل یک کمیته عالی مذاکرات، بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیدند  همچنین قرار شد گفت‌وگوهای فنی از همین هفته در بورگن‌اشتوک درباره همه موضوعات ادامه یابد.
در بیانیه مشترک دو کشور میانجی یعنی پاکستان و قطر آمده است که: «طرف‌ها با تشکیل یک کمیته عالی موافقت کردند که مسئول نظارت سیاسی بر روند میانجی‌گری خواهد بود. مذاکره‌کنندگان ارشد به‌طور منظم به این کمیته گزارش خواهند داد و گروه‌های کاری مسئول موضوعات هسته‌ای، تحریم‌ها و نیز گروه نظارت و حل‌وفصل اختلافات را هدایت خواهند کرد تا اجرای مؤثر تفاهم‌نامه و دیگر مسائل تضمین شود. کمیته عالی بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیده است؛ نقشه‌ای که زمینه را برای آغاز فوری گفت‌وگوهای فنی بیشتر فراهم می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76587" target="_blank">📅 05:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76586">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BMskqICMnZNWcnplyCFadXTC-7Sqmtrq2MmdteiY6me_u9-DgOZMSFf1RhwavGxT1ft9C9SHG8m5wh9jhUnYR5lwq_WBOVHaOJHuFh27mxfb5NCq0M95Ru9CPPqEsgADd9xURx_ylZcoZB1TaH0PJE70Idt2gXSMlg8QmlTxRRVrjWnBH6-MqJ2UIU6vU7fGERQomuRBy9TsuzMEpOpIdiExRi9hUxYc1i2CoQSQNbZtXxrawqlJux6L-F5DMLM3hjcY3OcsWPM8IltMkgaFAghhOtcpj_3MRRV_MTwEzNcyXBgCbH5c39KH_pEjV1CCAXRzlIX0TGhgEnd_bzC_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف با فوتبال، ترجمه ماشین: ما این‌طور از سرزمین‌مان محافظت می‌کنیم. mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76586" target="_blank">📅 05:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76584">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eMlTaIItTnmu7OqJELafdIc2vyMARb6G69CVGfIARbp25i1EZmBqP6Og7YbumoLweE7jmFGHNQLUwUkNVjryccsadmvwtd6s1dodeX02GAlNl80s28Ewei-8uOediAGe3X_U3a9ECkHKJoycuvkbpN87a5OCokMZ7ZpP89_4xaWc0dv0yv05M_XjQXpGfBo_fm3cZ4_vnAFOowhG_LvxRw3AArpPGEAfQS0iWz4kAKgoAx_7aKtSdL8lK5XsrJIhsleQrUcRneEwBIfDlcxIAS1MzEV12IJdeq9isi36MHCZWy2qK5FShwyORrJgplSGn3W1ADLfgykWNZ06bD2-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nmzrYkzWvG2wmZ_OhoO7P_-iwHBcdOy56LIVCRlSl9CSuFiRPe2o46V2BO91ScgXETphIotVJC2NyukL3bCfOzdAHjDGojrq4mKotjJfdPoI_LOdjOckNEy5LVinUSU9A6seP-X_0XPpBv_3hV95wWDGTgjSEoS-I5vFl2RxPpkY1ZtJTEbDx5PVaO2MbQdz1ay0KQwNxALpp2StDyS7deDn5C3lioRfTDqhD9H7gRIJXnLz_cwAAtGEhjIiLUxW83QH_zF6Rz0j-bWonsDcaSazS6kSndYq2gVRNwGjWbZPMDL-qD5fbA2SuKLYOsZr7cA9zr5fFTwqkJ-9inQLww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی، اعلام کرد مذاکرات سوئیس با «پیشرفت‌های خوبی» همراه بوده و گفت‌وگوهایی درباره پایان جنگ در همه جبهه‌ها از جمله لبنان، فروش نفت ایران، آزادسازی دارایی‌های مسدودشده و سازوکار عبور کشتی‌ها از تنگه هرمز انجام شده است.
او گفت درباره صدور مجوزهای لازم برای فروش نفت و آزادسازی دارایی‌ها پیشرفت حاصل شده و قرار است سازوکاری برای موضوع تنگه هرمز نیز تدوین شود.
بقایی همچنین تایید کرد هیات جمهوری اسلامی پس از انتشار آنچه «اظهارنظر تهدیدآمیز آمریکا» خواند، از ادامه نشست چهارجانبه خودداری کرد و مذاکرات از طریق میانجی‌های قطری و پاکستانی ادامه یافت.
به گفته او، تهران بر اجرای تعهدات طرف مقابل، به‌ویژه در زمینه آتش‌بس و تعهدات اقتصادی، تاکید کرده است.
بقایی افزود گروه‌های فنی دوشنبه مذاکرات خود را برای بررسی جزییات اجرای تفاهم‌نامه ادامه می‌دهند و قطر و پاکستان نیز متنی را به‌عنوان جمع‌بندی توافقات حاصل‌شده در جریان ۱۸ ساعت مذاکره منتشر خواهند کرد.
@
VahidOOnLine
تسنیم به نقل از بیانیه مشترک قطر و پاکستان گزارش داد که نخستین جلسه مذاکرات نمایندگان جمهوری اسلامی و آمریکا در بورگن اشتوک سوئیس و با میانجی‌گری پاکستان و قطر به پایان رسیده است.
در این بیانیه فضای مذاکرات «سازنده» و روند پیشرفت «دلگرم‌کننده» عنوان شده است.
به گزارش تسنیم، طرفین با ایجاد یک کمیته عالی رتبه موافقت کرده‌اند که نظارت سیاسی بر میانجیگری را بر عهده خواهد داشت.
براساس این گزارش، «مذاکره‌کنندگان ارشد به طور منظم به کمیته عالی رتبه گزارش می‌دهند و گروه‌های کاری متمرکز بر هسته‌ای، تحریم‌ها و یک گروه نظارت و حل اختلاف را برای اطمینان از اجرای مؤثر تفاهم‌نامه و سایر موارد رهبری می‌کنند.
کمیته عالی رتبه بر سر نقشه راهی برای دستیابی به توافق نهایی ظرف ۶۰ روز توافق کرده است که زمینه را برای آغاز فوری مذاکرات فنی بیشتر فراهم می‌کند.»
تسنیم می‌افزاید: علاوه بر این، یک خط ارتباطی بین طرفین برای مدت ذکر شده در بند ۵ تفاهم‌نامه ایجاد شده است تا از حوادث و سوءتفاهم‌ها با هدف عبور ایمن کشتی‌های تجاری از تنگه هرمز جلوگیری شود.
@
VahidOOnLine
عباس عراقچی بامداد دوشنبه، با انتشار پیامی در اکس از پیشرفت‌های حاصل‌شده برای پایان دادن به جنگ لبنان در پی میانجی‌گری خستگی‌ناپذیر پاکستان و قطر خبر داد. وزیر خارجه جمهوری اسلامی نوشت: «صادرات نفت و پتروشیمی معاف شده، محاصره برداشته شده، برخی از دارایی‌های مسدود شده آزاد شده و طرح بزرگ بازسازی و توسعه برای ایران آغاز شده است». عراقچی با این حال تاکید کرد که اولین آزمون واقعی و جدی این دستاوردها، عملکرد «سلول مدیریت منازعه لبنان» خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76584" target="_blank">📅 05:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76583">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5HfOekuIrsOn5S7NQWrKh38Zaz3frV9tB8kS_gb1xxzzB_GEhzPfh3-0fLK4qJFBvCXrtiVHoGEqWPgHBAaGpInhQpsYSJ7e33O1cvu6OvsRZDn27ieJjI-hpTj1BCCt49lvx6wdcPZ0D4Q1D2CLGxNcJuyNkiL4Lzx2V71l-gl16m5RiTB1psxngx7LJWFZ3PuTmeny7drQ6nSs0Hi4NM47VxIcOqD7rrug3o0Q67TMs4tXszS0cv6nhCrgHfyqdElzQC7GvqDNwWNv6ZB1rb6g1zv-b5X0RT-LVUF003oiTt7-0XKHGvhkG3SsMEZs3Pv0mOW_A1rlZyGSbSRgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اعلام کرد مارکو روبیو، وزیر خارجه این کشور، از دو روز دیگر، یعنی ۲۳ ژوئن (دوم تیر) در سفری دو روزه به خاورمیانه به امارات متحده عربی، کویت و بحرین سفر خواهد کرد.
در این سفر، آقای روبیو درباره مجموعه‌ای از اولویت‌های منطقه‌ای گفت‌وگو خواهد کرد؛ از جمله:
تفاهم‌نامه میان آمریکا و ایران
تلاش‌ها برای تضمین عبور کامل، آزاد و ایمن کشتی‌ها از تنگه هرمز
اهمیت حفظ صلح و ثبات در منطقه
وزیر خارجه آمریکا همچنین در بحرین با اعضای شورای همکاری خلیج فارس دیدار خواهد کرد تا درباره اولویت‌های مشترک کشورهای منطقه گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76583" target="_blank">📅 01:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76582">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d6dbgxWQZbLPmoDQeh0n8EosBx1pK8VkexEmjhMteiI1QpSIjUa8kfa057Gskd5qFkQkcg21FSHwfW3jFqj4KdKuIZSkzaMLKkkOgmsDSJj0Xn8aS4qzBPqlAp7vCs12vCMHNuIypKYdppGTvJqqEtDsvHQdH5IVanIqHtPoY4PVnxf2eD7IHH-2xsWlRlmZZCFgRr7Q9STD75Je48yMejSkxPain_HyM64QKDmi_YKXUu_b2MDzhzFxlpe_wkvS4Cntl3ydMaFCD-8NstJaI1yff0fSNl3SCef9D17u8rPApMG9w_5Cr5OjrrQdSWHHmh_n9eLGvdyV8gBH0GGxJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف با فوتبال، ترجمه ماشین:
ما این‌طور از سرزمین‌مان محافظت می‌کنیم.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76582" target="_blank">📅 01:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76581">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FSWO9pv43DxNnSwyfloUPDeiayWiSkO4_u6NSJxI5N0iDWbozY3m-j3Ge4QHOGP4iPsCVhh5Y6pLin7xEeiy2NeLxKk6GtSQ-ivAnPzimv3YTsazcVSztYxsS6hkNCBb0VGfXkmEe802QYnwJ3sxY8Qvh1YKIzvAJGlYc4eLqSTNS1RkUK2LSlaWZ7ZcsEQ7EsvMzT8uWM_uVGn_JwklEduZwIVxjch1z4vxuWrOkwfbQtBHXwSHu9ruM3HhgeUo-2S1xycrxdJha3xDcnIGLs_QTqS-daMFEJ0C3obyYcV7MyyqMQTZkf1ZHmifZrQfSVfbcwA1pOFbAE4ffLR3jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو پست ترامپ علیه نیویورک‌تایمز درباره اخبار جنگ:
تیتر نیویورک‌تایمزِ فاسد و رو به سقوط این است: «بعد از تقریباً چهار ماه جنگ چه چیزی تغییر کرده؟ تحلیلگران می‌گویند نه چندان زیاد.»
واقعاً؟ ارتش آن‌ها از کار افتاده، نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آن‌ها تقریباً نابود شده، دو رده بالای رهبرانشان از میان رفته‌اند، تورمشان به ۲۵۰ درصد رسیده، اقتصادشان درهم شکسته، به سربازانشان حقوق پرداخت نمی‌شود، تنگه هرمز باز است، نفت با شدت در جریان است، و بازار سهام و اشتغال در آمریکا به بالاترین رکوردهای خود رسیده‌اند. این‌هاست آنچه تغییر کرده، ای ترسوهای فاسد و بی‌اخلاق، و حتی بیشتر از این‌ها!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
نحوه پوشش خبرها درباره ایرانِ بسیار ضربه‌خورده و آسیب‌دیده از سوی نیویورک‌تایمزِ فاسد و رو به افول، از طریق «واقعیت‌های» جعلی و ساختگی، به نظر من «خیانت‌آمیز» است. من همه گزارش‌های دروغین و مضحک آن‌ها را به شکایت چندمیلیارددلاری‌ام علیهشان اضافه خواهم کرد. آن‌ها مجرم‌اند!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76581" target="_blank">📅 00:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76571">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jz-7DOT8Xmq10FJMC3UQc-2rO8vcBsNneQI9ptxfXB86RWPTyl8UauJex6rIFwqZLRxzZCJsPD6Xzhq9x4gifY5WCHmKSRT88kbMKqZQD2Kq0ZlpGETPCDrDVcVY8Ai6xaTImYUe-aBvz7i0SWY4My4KTkDRgWnuEYFHRZlUHHAjGFMWSR_b-IENK5uIbA8lwYgC9XUUje7GKkGH5lD8OPnPIXeCQFI-Eg6soy40lX_Cy4BAdSxrQ-LbtH6zTKlXbsv1I6z3mMfKY3MNeJlw_ZZ7xAFwFeLc4DmkXE0AAAERL_rv9jWpbmRRorf3zKP6q0GFMtg0xzti5QqsiAGKWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XO7T9F2oNA4EAISM6t7fiwdFjZUjqI79k3joyfX5BhSHQcxfXUX_RVoy-sffRj3Vqdq24mT8M3xWq1vA_cR35R3iluBBZrQ7cs-3fJWTJDXrMW0hmZX_9m74s8a3foGQpOtyNPSE5DTB6LS8fyfv1lsY5wUachKygKcqgd33cmZ4Ee2CERWVNWI8jaHC6I7dEifCrFlpktD_w40vdORx6-pVdrFLktB0iWzV3SQNPy06pQ4CGqa9DmpsMw0mW7OU-sJX43yM7WQENsmfv91PNRzR79u4WQBiGO-SIBMYkPlZNSS0czFFGRhpG8jHXJr_Cp_aDX3_x5ssJAe9zmPPag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qAvMXGAB-dQ6jyErMTwd8MPOPGhDo4T6FwjWnGE0-1rdJMblY5X5MsW59SmXUS68H44kHeuMj53Cfq52Hes47c1nfaJ8xl4ly4BDbN9QdlH5lnMsWSDPIgkcybhS1oszguIsU7fT_kFE3tOo8qi91rQ4BX4ZCA-KIn-E41DGFfO-PwlkOZ1x71cdlMETFP_CWLr_KssM1mKc9jZc6S2pcEkNncC4C7feEbF5KvtQeDokc6gsm__78Pv9THjy90uep3ESG4TZK_grwA1wJ-klJdf4JKEFrd0TRUeigUZSnuVfmACaUE3nJ4ci8aGmzkQ787b023jTBvl17znvkeA2Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M849XZMN5xJaxRA-bLp753hDuyqMszxhUQfFFei9kTZpMD8HfCHycAg7sxdJX-iJ5N5y70t2a8qhYlEMhlSzRsQ8jjxjOHf7UD5rOYp6M22WRIPdsZFTt_dCHWt6Q1euHXJuiO8_0cL8g87KETz0KevRSWLJgQGu6AbuexvyHq-Oja_1QetilUc3H-mv1ijXXQxLTOMV8A0JTqx1X7GtpGC_FxO6F3G6EC1D4dLFyDMguuR3jMJHcfTEuI-ats93JxotKFTA9_jisixXb0V133WmQoTg26O5Cgb879fJatrqDhL4sLtbKV9OlKAo4I_zhunumgtv23z_PqEPDlRUKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jroKbQUfaxm8YeoMB_wND3fXMq0SrybVTOEmx_9xJU0LtyDWpScCF65yN2oogsyd4Vf1eQHKHoUWL04If4oE77r_gTPfBmmd77qhtuTkgpKf3nC4Ob4boqDuKAZmzmYc5WphaA1FKZ2kKwRnu6tcFP_9oyFmILR-H_jlf6cuAVX6xTBOdY8sw_U_HDLChZu8Be1exzJtN7Nnbma2fArGb2gc9VhdhZZLfCQQP6NKLlmW2XWsEOry4WIWvJ5TfL1nWjxvLxiyGBxxshM-3-WKk2MHagwDjdxqrVxGd8onSLz_wO8tc1pFjoSh2ZYgzykPOcQLpCmiO79YKMUM3ihOFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AOb6PwwqoyTUG4kVWIauKZkU8YFkjwRUnTpT6tkb6qtUPguhrj5zAPm2oSnA02yIAC46F99VtW5FifTdgMtIQtRLsN6x-762edJsehJ7BdeyUbkVeS6-vYDBLXL5T2svd0KtxZAP02rg-T5a5L8ohQ2EN9t2AeEBcHQs2GmI2jjlZbxgpkQgRH7ghXK0hkPjoQ9Wbfd6cCQibkkhMqljXx23m2GszY1O8eM2Cr5LzeqIYG0UwP5nXG91cOE12LbwXqGRCDKY_vdLFszYMIOeiBpZFJ_cGw-NxEQ4jDgihR6Di6qUoBYTlfnLOwCCKz7VIUUUQwbVWumrA0k2NNGzhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nzxKjYTkOBH6EvR_NOP_NfhJulOQZ4sx9lh0ttxjA2QdYmny2nIKB8k7EQ058s055h6FJkn7-lDt6qIh4aNG0V4BRQ-SBOj_n_nxMUEMMD3-hc5XxmSSB4bJHeoKgPakz8NHQ7RNzbSAB02OWOBumqC50WzIQehRM9oL64gJUGOdr2hM37IQynGdhOnKIFde31s_-s3sBXD1vcdBfWUbhosmPsALHSkalY0RYSgh8eVrkBXOG2JcsumT8-wGC7UXHmtvUBSsIk8p1d76dGILua103T9h3SLBe1H5v4MEaScNk88ovksmOZFy2fKlU2fHguhdYWAk-uwDYkQ5etwC6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=fkwSKhZMkcXijkWnRUDZ8FKkTvYCOyWpXxP-q8CyG1DOM7B-1N9EfGip4o8r4maRL8nzASmhlBI4A8w8P8n1HYze__oyuI3kxuNKCyvpr82hCNMgtMkAdQaIbV7_tbdVqJI-SOxLdeR1GXcmGwzsBqEkQBSWfVdVefukONCbKMa3lv7kPdoe1Gc3RdOgES8KwF7_j6UNNgrDuSm1Wwp9YbTxve-7__UmWUarWh86DqjMkCauADv44M1horg-sXcU6ZKWXNGxYEO5kWiQ1qcMF-xrBz7cT46_fX_DfnJcolxSDBhq2uk6fCERMn8NiWWl5v1A49o-NZdhRnUluPd2PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=fkwSKhZMkcXijkWnRUDZ8FKkTvYCOyWpXxP-q8CyG1DOM7B-1N9EfGip4o8r4maRL8nzASmhlBI4A8w8P8n1HYze__oyuI3kxuNKCyvpr82hCNMgtMkAdQaIbV7_tbdVqJI-SOxLdeR1GXcmGwzsBqEkQBSWfVdVefukONCbKMa3lv7kPdoe1Gc3RdOgES8KwF7_j6UNNgrDuSm1Wwp9YbTxve-7__UmWUarWh86DqjMkCauADv44M1horg-sXcU6ZKWXNGxYEO5kWiQ1qcMF-xrBz7cT46_fX_DfnJcolxSDBhq2uk6fCERMn8NiWWl5v1A49o-NZdhRnUluPd2PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال ایران در دومین دیدار خود در مرحله گروهی جام جهانی ۲۰۲۶، با ارائه یک نمایش دفاعی، در ورزشگاه سوفای لس‌آنجلس مقابل بلژیک به تساوی بدون گل دست یافت.
مدافع بلژیک در دقیقه ۶۶ از زمین اخراج شد و این تیم ۱۰ نفره به بازی ادامه داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76571" target="_blank">📅 00:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76570">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e_ugLxn28ogwyC5r5Af6tUtDiGf8NJbkipDxW61BjaIIqa4oQiTVDp6tlPVsar7nYuit9An8XWCZFjeNSJUbX4v-5myBvwXGpPgQa07ya2BdpvVEfkx-oAQLIkh6v9QRh6MJBQtuPN1ijQxt6v2avp0RqczlBjWRFFkB-wXMEImjFBfKCVZyslneHfKzCtHthr2YtnBdsYys5GD1DGSJbVE9pVh11lCmWabtaKCg3eMqxKkVybS20VVigBHPKTaB3HCj_WJ3tuQ4U7y-t-YxUa5CYnjc-wbdRlmxxULq5riK1Lf0qzPffGWXsFiLEq_q2W97cENex2kIYlNn98idIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
بعد از آن‌که تریلیون‌ها دلار خرج ناتو کردیم، ایتالیا و نخست‌وزیرش حتی فکرِ درگیر شدن با جمهوری اسلامی ایران و تهدید هسته‌ای بسیار جدی آن را هم نمی‌کنند. دهه‌هاست که ما از آن‌ها دفاع می‌کنیم، اما وقتی پای آزمون به میان می‌آید، آن‌ها برای دفاع از ما و بقیه جهان حاضر نیستند. خوب نیست!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76570" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76569">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PDdBwJvmTup1BQgA23qnFNXladEvlCiyvw01QZe8JZMtEXtaKAvDLpf2CK9jtHlg8o0qv28rDah--n-nHLgqLQM0io4l0_5fiqoHauy5FXovfm3E-DfDeZ5eWPAV3FX26DOsdFcglM18cHMxXPzGUQuXBHU2NOSYxFOaW06Bbsby33VB9ShX54oEzoC8P4IvxqXeK28NZxYfv6iEM76p3VaSNVcw7J7S0XanTbm0BjguRTe_F3kkVkHRIDyI1SRzxTmy3F16vZI4R6JXQFidnQcRkBcz3GgNRIYUEZpSKF4om4PQsa-n6pJLvBx9qDNjiChTkVlM5SenMixmso7hGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ک مقام ایرانی یکشنبه شب ۳۱ خردادماه به خبرگزاری رویترز گفت مذاکرات میان ایران و آمریکا در بورگن‌اشتوک سوئیس متوقف شده، اما پایان نیافته است. این مقام جزئیات بیشتری درباره علت توقف گفت‌وگوها یا زمان از سرگیری آن ارائه نکرد.
این اظهارات در حالی مطرح می‌شود که گزارش‌های متناقضی درباره وضعیت مذاکرات منتشر شده است. پیش‌تر باراک داوید، خبرنگار آکسیوس و کانال ۱۲ اسرائیل، در شبکه اجتماعی اکس به نقل از یک دیپلمات حاضر در مذاکرات نوشت که هیئت ایرانی محل مذاکرات را ترک نکرده و گفت‌وگوها همچنان ادامه دارد. با این حال، خبرگزاری ایرنا دقایقی بعد به نقل از یک مقام هیئت مذاکره‌کننده جمهوری اسلامی گزارش داد که مقام‌های ایرانی پس از دومین دیدار با هیئت قطری، محل مذاکرات را ترک کرده‌اند.
@
VahidOOnLine
خبرگزاری ایرنا، رسانه دولت جمهوری اسلامی، گزارش داد هیات جمهوری اسلامی پس از دیدار با هیات قطری، ساختمان محل مذاکرات در سوئیس را ترک کرده است.
هم‌زمان، یک منبع نزدیک به هیات مذاکره‌کننده جمهوری اسلامی به شبکه سی‌ان‌ان گفت گفت‌وگوهای میان جمهوری اسلامی و آمریکا در سوئیس متوقف شده است، اما پایان نیافته است.
به گفته این منبع، گفت‌وگوهای غیرعلنی همچنان ادامه دارد تا طرف‌ها به میز گفت‌وگو بازگردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76569" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76568">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k7Gdyc9Qq_E-Mx1FBKMXrNzboVEtuPOexPHw4KftXWRVWBj8Fl39h0kxTK3ebqjyPB4xnd9IuG1qjnmGcxtNmKWPnTJq3CmYu9Ln3_HzOcUq1OdXnufrgXHbUP1iQVRn2NWYEh2OeKIuzyf3kLafk1DLEb5sbOvS8VKx5Dh2CZf2RVpsQuwC9QZExQKQPCHY6_Oy5xdFoyrOqnLcfA8a9VCDAy1s0THY76x3tPmCLcOQbn-gIgwh0Xf8vcbIBXkW63m3aYopX3UVsboKgl0RdN6-TxpxUb8cjWdZBX-a1XiH6S8m61z3mCuKhn4tSUEWIQ_q1bKncI9P54Fm36Nm-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد.
"
ادعای فارس و تسنیم به نقل از "یک منبع نزدیک به تیم مذاکره‌کننده"
پیش‌تر در
اکانت قالیباف
همچین توییتی منتشر شده بود:
با خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند، این ماییم که عمل می‌کنیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76568" target="_blank">📅 20:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76567">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dxY-8XGxDSq4qyNsJO_JOkXGjzZvK51iRd_0TMAbbNG7pS28qdX1uQ2zKP4J-VAwcCe9NKgcvgsyzZiDaO-eLPqJDO6rw3greY5nGa6ZHF1tfV3CFq5cYzgMUVBsnnSwcz1S7Z_IhXR_qC1BY9IyJcARIX5cFP9UR_f0m_XiC1k2sT3UWeNHDB_7Fe3VemEOme7Rg3EscyPJiWCwFJNbbZcwhMNuBrCboRs31TYdaGamhObbfqNKn4GoIi6EicUW0tqh7N6GPJU87zm_OfR7Knx3Gw8T70TtsT20wZSrULLrD-Lz1xMJXG1vLOn8uomL-L1U0HhZXzRHqSIy776Biw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در واکنش به اظهارات مسعود پزشکیان، رییس دولت جمهوری اسلامی، درباره ناچار شدن آمریکا به پذیرش تفاهم‌نامه میان دو کشور، هشدار داد که تهران باید در مواضع و رفتار خود تجدیدنظر کند.
ترامپ در گفت‌وگو با فاکس‌نیوز گفت: بهتر است مراقب حرف زدنش باشد. بهتر است رفتارش را اصلاح کند، وگرنه ما کنترل بقیه کشور را هم به دست خواهیم گرفت.
این اظهارات پس از آن مطرح شد که مسعود پزشکیان روز یکشنبه ۳۱ خرداد گفت: آنچه مسلم است از حق غنی‌سازی اورانیوم هرگز کوتاه نخواهیم آمد و طرف مقابل نیز ناچار است آن را بپذیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76567" target="_blank">📅 19:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76566">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TwYHnfyX-_ZLFyREw-EaJf2kfR_uwnmFLPX5E1otl2eW5fGh5ApYjy2JaGpwF56E9Hd18HQ83O2QEG9JZnSquZpdyyLVoidKsT1YtHDFijjEicpZVYfLGunUg1KQ7SkWz5traM80bthlxLQEV3q0Jou46RG0OSXHE6aJJAoD5Oj_1hLYWCmPNade4pRaOwvKCS3d4s3OH1yBSwu-jDNlbI3yOU6CbgynBw7Vylmsx436_Crbbq0Ua56MgQOk4DJk6JdwIjZH76ZauXntsu3iBns8ShKLB1Qdd0h1Z-NNBOQOJUVK__ZEvErKHCocZbCLAqLu0qIL3WLfClxifQbMZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، اعلام کرد همزمان با برگزاری مذاکرات در سوئیس، به مقام‌های جمهوری اسلامی درباره هرگونه اقدام برای بستن تنگه هرمز هشدار داده است.
او در گفتگو با شبکه فاکس‌نیوز گفت این هشدار شنبه شب به تهران منتقل شده و تاکید کرد در صورت چنین اقدامی، ایران با پیامدهای سنگینی مواجه خواهد شد.
ترامپ همچنین گفت به مقام‌های ایرانی گفته‌ام که اگر تنگه هرمز بسته شود، «دیگر کشوری نخواهند داشت و حتی امکان بازگشت به کشور خود را هم از دست خواهند داد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76566" target="_blank">📅 17:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76565">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KvVQvw-i-KrDeb0lyxquO8pttYPmrfjrVh0yBswrdU5_6MmbHgM1RqzqQI0-hYduCB92ewQyLnbrybHU48Fxl6SOXsI1PVY1q5M6ONikwID7qMFdQEMZqhrG0DMQIOiLXNVWi5q6BI3fxwCIwRcWl22eseFzrPUp5dJ184pO--iS4yqNAR4AGkcSupblNJi_tw46mqxSekWYkbokAItQxeOnZYWs4fViYMrNIrdIgS1xsSuW7dK70ggBdwokWS3ix3LFQ1iIO-rQIRRSw-mTvUFQfNMitNcwoKAMGQknaLFBykrwjQ0bOVsnJ80YKPsVmKnoA0xoecSl3uH8GY0BGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران باید فوراً جلوی نیروهای نیابتیِ بسیار پرهزینه‌اش در لبنان را بگیرد تا دیگر دردسر درست نکنند.
اگر این کار را نکنند، دوباره به ایران ضربه‌ای بسیار سنگین خواهیم زد؛ درست مثل هفته گذشته، اما این بار شدیدتر!!!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76565" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76564">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e1422ca156.mp4?token=JwUQJQStlWTQdA74Xu5otXe6WOvjQBC_UYzZC7cov8p8P2ZMaqY3yL1xtCSEE-_0xmxn8Uqbc54EbiDo1nZap2X7MUx9ofVeNN0XVU5xaopGe83GTaIrmthRNB_GBd41IDGMv42uT72yc7l5UdtNpJokAUg5NQCwBRw2iKHotYWWGChlzDts8ysexd3HDyz6e76Dp9QR7aW_ak9D_02qpa0o00gZySkpldid_x0lE0PJ_58MBInUug7m0RlXHJWyIJsj7X5-bZ5nHjA__sAVfsAPxVVSKd8r2h6BdmlqzwBhlLPa9tvuGR0y4etHmEXzZiplLIOXvVv2fHdJbRB9CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e1422ca156.mp4?token=JwUQJQStlWTQdA74Xu5otXe6WOvjQBC_UYzZC7cov8p8P2ZMaqY3yL1xtCSEE-_0xmxn8Uqbc54EbiDo1nZap2X7MUx9ofVeNN0XVU5xaopGe83GTaIrmthRNB_GBd41IDGMv42uT72yc7l5UdtNpJokAUg5NQCwBRw2iKHotYWWGChlzDts8ysexd3HDyz6e76Dp9QR7aW_ak9D_02qpa0o00gZySkpldid_x0lE0PJ_58MBInUug7m0RlXHJWyIJsj7X5-bZ5nHjA__sAVfsAPxVVSKd8r2h6BdmlqzwBhlLPa9tvuGR0y4etHmEXzZiplLIOXvVv2fHdJbRB9CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس و عراقچی در یک قاب
خبرگزاری تسنیم به نقل از یک منبع نزدیک به تیم مذاکره‌کننده جمهوری اسلامی گزارش داد که هیات آمریکایی و برگزارکنندگان نشست ژنو قصد داشتند پیش از آغاز مذاکرات چندجانبه، مراسم عکس مشترک و صحنه دست دادن میان هیات‌های جمهوری اسلامی و آمریکا برگزار شود اما محمدباقر قالیباف مخالف کرده است.
به گفته این منبع، محمدباقر قالیباف، رییس مجلس جمهوری اسلامی، با این تشریفات مخالفت کرد و اعلام کرد اعضای هیات جمهوری اسلامی در مراسم عکس مشترک با هیات آمریکایی حضور نخواهند داشت.
این منبع افزود در پی مخالفت هیات جمهوری اسلامی و خودداری آن از حضور در این مراسم، پخش مستقیم و برنامه عکس مشترک لغو شد و پس از آن هیات جمهوری اسلامی وارد محل برگزاری مذاکرات شد.
به گفته این منبع، هیات آمریکایی از هیات جمهوری اسلامی پنج دقیقه فرصت خواست تا خبرنگاران محل مذاکرات را ترک کنند. او افزود مراسم پیش از آغاز مذاکرات، بدون حضور هیات جمهوری اسلامی برگزار شد.
@
VahidOOnLine
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، روز یکشنبه در آغاز مذاکرات ایالات متحده و ایران در سوئیس، این گفت‌وگوها را «تاریخی» خواند و تأکید کرد ایالات متحده آماده است روابط خود با ایران را به شکل بنیادین متحول کند.
ونس در حالی که در کنار نخست‌وزیران پاکستان و قطر ایستاده بود، در اقامتگاه بورگن‌اشتوک در کنار دریاچه لوتسرن گفت: «این یک دیدار تاریخی است. پیش از این هیچوقت رهبران ایران و آمریکا در چنین سطح بالایی با یکدیگر دیدار نکرده‌اند.»
تصاویر و ویدئوهای منتشر شده از محل نشست نشان می‌دهد هنگام حضور معاون رئیس‌جمهور آمریکا در اتاق محل مذاکرات، عباس عراقچی، وزیر خارجه ایران، نیز حضور دارد.
معاون رئیس‌جمهور آمریکا درباره اهداف مذاکره با ایران گفت: «آنچه رئیس‌جمهور از ما خواسته این است که فصل تازه‌ای را آغاز کنیم تا روابط خود با مردم ایران را متحول کنیم و دست دوستی را به سوی آن‌ها دراز کنیم. پیامی که به مردم ایران می‌گوید اگر رهبران شما حاضر باشند از نقش‌آفرینی به عنوان عامل بی‌ثباتی منطقه دست بردارند، و اگر حاضر باشند در بلندمدت از جاه‌طلبی‌های هسته‌ای خود صرف‌نظر کنند، آنگاه ایالات متحده آماده است روابط خود با آن کشور را به شکل بنیادین دگرگون کند.»
او ادامه داد: «این بدون تردید هدف ماست.»
ونس همچنین گفت: «ما تنها در چند ساعت گذشته پیشرفت‌های بزرگی داشته‌ایم و انتظار دارم در ساعت‌های پیش رو نیز پیشرفت‌های بیشتری حاصل شود.»
او با اشاره به اراده ایالات متحده برای «متحول کردن» خاورمیانه، افزود: «ایران در گذشته یکی از عوامل بی‌ثباتی منطقه بوده است. اکنون آینده‌ای را می‌بینیم که در آن همه بتوانند برای پیشبرد صلح و رفاه برای همگان با یکدیگر همکاری کنند.»
@
VahidHeadline
جی‌دی ونس پیش از آغاز مذاکرات اعلام کرد واشینگتن طی ماه‌های اخیر بیش از هر کشور دیگری برای توقف درگیری‌ها در لبنان تلاش کرده و این روند را ادامه خواهد داد.
او با تأکید بر اینکه «صلح آسان نیست» گفت رسیدن به توافق نیازمند تلاش و «بده‌بستان» میان طرف‌هاست و افزود هدف آمریکا تنها صلح با ایران نیست، بلکه دستیابی به ثبات در کل منطقه دنبال می‌شود.
ونس همچنین مذاکرات جاری را «آغاز یک گفتگوی فنی» توصیف کرد که قرار نیست همه اختلافات را یک‌باره حل کند، اما فرصتی فراهم می‌کند تا طرف‌ها برای نخستین‌بار درباره مسائل اصلی به‌صورت مستقیم گفتگو کنند.
به گفته او، حضور رهبران سیاسی برای تعیین چارچوب مذاکرات و حمایت از تیم‌های فنی است و با وجود چالش‌های پیش‌رو، طرف‌ها با انگیزه برای ادامه مسیر آماده هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76564" target="_blank">📅 16:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76562">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/12a29862bf.mp4?token=aNU4Yh8x1ibcLWZIs4Hk0RglbQ0avBF73EXIL3EXrf2IPqNqZZph6XpVi7VZ7NKw4EJZGjbB_e_7wl5gZLMtsBAlTcHQBIyEOPAzvf9-icBsULdeSjbIyC8j4gi16RG-O4AkFQSwfHNXsXoCvaYK7WPWPlL926yyKVhSVOdNEsdcAhaedN-SzDw6ckDQpggSokykIOf3w29Tp9L8kw216aRLt2TrijGmNMZnl_D3zVrsVTATd8ErrqfSa-sgiQh_TcAx2LddpgeUkzf7mPPWqQDRlLwTMU_elFwowEMstingtBwoIXsI0Ex-CVRbVcQChkS3oepRh6i9uNTl2Wrqbw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/12a29862bf.mp4?token=aNU4Yh8x1ibcLWZIs4Hk0RglbQ0avBF73EXIL3EXrf2IPqNqZZph6XpVi7VZ7NKw4EJZGjbB_e_7wl5gZLMtsBAlTcHQBIyEOPAzvf9-icBsULdeSjbIyC8j4gi16RG-O4AkFQSwfHNXsXoCvaYK7WPWPlL926yyKVhSVOdNEsdcAhaedN-SzDw6ckDQpggSokykIOf3w29Tp9L8kw216aRLt2TrijGmNMZnl_D3zVrsVTATd8ErrqfSa-sgiQh_TcAx2LddpgeUkzf7mPPWqQDRlLwTMU_elFwowEMstingtBwoIXsI0Ex-CVRbVcQChkS3oepRh6i9uNTl2Wrqbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، همزمان با برگزاری مذاکرات مستقیم میان ایران و آمریکا در سوئیس، گفت همه نظامیان در شورای امنیت ملی موافق مذاکره بوده‌اند.
او در جلسه‌ای به مناسبت تشکیل بسیج اساتید در دانشگاه تهران، در میان صدای اعتراض عده‌ای از حاضران گفت: «همه امضا کرده‌اند که این راه را باید برویم. حالا هر کسی می‌خواهد تفرقه ایجاد کند، این گوی و این میدان.»
او با اشاره به نظر فرماندهان نظامی در شورای امنیت ملی گفت: «فرمانده قرارگاه [خاتم الانبیاء]، فرمانده ارتش و سپاه، و نهادهای امنیتی همه بودند و همه یک حرف زدند و همه متحد بودند و همه آن چیزی را که می‌خواستیم عمل کنیم را امضا کردند.»
این سخنان پزشکیان در پی افزایش انتقاد اصولگرایان تندرو از دولت در پی انتشار نامه منسوب به مجتبی خامنه‌ای صورت می‌گیرد.
آقای پزشکیان همچنین با تاکید بر نقش دولت در حمایت از نظامیان در دوران جنگ گفت: «۲۰ میلیون بشکه نفت که مال دولت بود را به هوافضای سپاه دادیم. ارزهایی که داشتیم را به این عزیزان دادیم.»
@
VahidHeadline
مسعود پزشکیان، رییس‌ دولت جمهوری اسلامی، گفت نگرانی اصلی او این است که دولت نتواند رضایت مردم را جلب کند و نارضایتی‌ها به اعتراض‌های خیابانی منجر شود.
پزشکیان گفت: «از آنچه می‌ترسم این است که نتوانیم به مردم به درستی خدمت بدهیم، ناراضی شوند و به خیابان بیایند و اعتراض کنند. آن وقت ابهت ما فرو می‌ریزد.»
او افزود مهم‌ترین قدرت جمهوری اسلامی، وحدت مردم است و مسئولان نباید اجازه دهند کمبودها، کسری‌ها و نواقص باعث نارضایتی مردم شود. به گفته پزشکیان، بروز چنین وضعیتی موجب «خوشحالی دشمنان» خواهد شد.
@
VahidOOnLine
بعضی از جملات پزشکیان به انتخاب خبرگزاری دانشجو، وابسته بسیج:
🔸
اظهارات عجیب پزشکیان: من از این میترسم که نتوانیم مردم راضی کنیم و به خیابان بیایند اعتراض کنند
🔸
تمام مفاد تفاهم‌نامه امضا شده بین ایران و آمریکا به نفع ماست و دستاوردهای این گفت‌وگو و مذاکره عیان خواهد بود.
🔸
ترامپی که ما را از انجام بسیاری از کارها منع ‌می‌کرد، در سخنرانی اخیر خود تمام آن‌ها را حق مردم و ملت دانست.
🔸
۶ میلیارد دلار پول ما در قطر برخواهد گشت.نتانیاهو اولین ناراضی از مذاکرات است.
🔸
تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم، این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.
🔸
شورای عالی امنیت ملی در وحدت و انسجام تصمیم گرفت؛ همه یک حرف زدند و متحد بودند
🔸
مواضع ترامپ ۱۸۰ درجه نسبت به گذشته عوض شده/ آنها پذیرفتند که حق ملت ایران را نمی‌توانند نادیده بگیرند/ قاعده عوض شده است
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/76562" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76561">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjJYhrw0XanjhyuM2b6RhPrNiNMFsQpgjCJdH2fXue4gThiiqV8AgnhSg0K7nSmlFyBdOKHcc6G4qWXR04rgDHy6M2Yh6BbxSgNkdCh2pwYM9-ibbIXMWA25QBrn_d8iGTvKsFmY9O9c-gaQ_UCdVjRcwR4KbwL2MBrOTy10vJ43KwWiDwkYhZTj-8HuP6cZUNU_G1XmJweg-fyttIcJFb42KkK3Bu_u0RHzIZqiSZZgeRl1WAWtB8yc9CXCpt83I2yqx8Pcrg0Q9x2RRbb0Bzk04Q92mRyaPJ3mteN6uB_uxs83eQwdRdWmVrIEHvOK2QXDWYqE5hVcPTRDlnRQRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو منبع منطقه‌ای آگاه گزارش داده است که آمریکا می‌خواهد نخستین دور گفت‌وگوها با ایران با دعوت تهران از بازرسان سازمان ملل برای بازدید از تاسیسات هسته‌ای ایران پایان یابد.
به گفته این منابع، این تاسیسات پیش‌تر هدف حملات آمریکا و اسرائیل قرار گرفته‌اند و آخرین بازدید بازرسان از آنها پیش از جنگ قبلی، در ژوئن ۲۰۲۵، انجام شده بود.
اکسیوس می‌گوید: «آمریکا در مقابل آماده است به ایران اجازه دهد به بخشی از دارایی‌های مسدودشده خود دسترسی پیدا کند؛ از جمله حسابی به ارزش شش میلیارد دلار در قطر.»
بر اساس این گزارش، ایران می‌تواند از این پول برای خرید کالاهای بشردوستانه استفاده کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/76561" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76560">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOUjZkRGeff55zEa1xIIha98oImIkF01FeD9O4DxMcIAVOJB-8NPYWjonfZhA_oI_C7l3_8ByPjQ0zJkEj8Dv6MWeFAIMTtcGrq0kEPBxCIkVy5xCUQ_I_jU3oLM60TLc1bMo665v-SSEs7z-hlB1fxskR_wTI2q_vKgFWPDIavtOaungzZf_PL-q2OngtVov94HVQn6GoFTR_AsfBcL0xeoZ-l_on0mYUMjbYuKIZq4bkKkwSAczKlhTwDUBjPtpgWpP-hjS4Q1s-B1k5_GECpiPJMbDJKvDOG2hrDhARa81HhB5UhTTq5Uno83gbWdaGFOuMLt1B7qbQCjNdzeaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام‌های بهداشتی در غزه می‌گویند که دست‌کم ۱۰ فلسطینی در حملات هوایی و تیراندازی نیروهای اسرائیلی در چند حمله جداگانه کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/76560" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76559">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4il-QuotNUz5z5cukuyIIj8PVdMvFygTX7ZhvINnUOBpRjxsR7jdPDVmQcuqiQEkMmmyk57Jt8vAIiaSHMdD-yyXyZUc5Vb1dce_McmyCfM5Ae8ku48n1clfZVqjzkkSevhBT5TsPRSKMzW6e6AZC6FpOesWq0a23Z5FAVTkljQwXUdFaKUtatE24UCNexudgIufQqze6A6lXWmD_7alSl9_D3oQsfDei3UeUoL0SJHMZTAnwJiapy-Nmb_F4l_UNbJZKmnSRMjiS2fSIC8IB8VoxkKf3dYx6dVfwSqgX_mRmeBr7vcdXchbc7HNBysF3CLt_PKJTS_RE5qiuPlVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از هزار دانشجو و فارغ‌التحصیل دانشگاه صنعتی شریف با امضای نامه‌ای سرگشاده خطاب به محمدرضا تجریشی، رییس این دانشگاه، نسبت به آنچه «تشدید فضای امنیتی» و گسترش برخوردهای انضباطی با دانشجویان خوانده‌اند اعتراض کردند و خواستار پاسخگویی مدیریت دانشگاه شدند.
انجمن اسلامی دانشجویان دانشگاه صنعتی شریف تاکید کرد که بیش از هزار نفر این نامه را امضا کرده‌اند. انتشار این نامه یک روز پس از رسانه‌ای شدن صدور احکام اخراج برای شماری از دانشجویان شریف صورت گرفت.
امضاکنندگان در این نامه نوشته‌اند که در ماه‌های اخیر دست‌کم ۳۰ پرونده در کمیته انضباطی دانشگاه تشکیل شده و ۱۳ دانشجو با احکام بدوی تعلیق یا اخراج مواجه شده‌اند. به گفته آنان، احکام سه دانشجو نیز در مرحله تجدیدنظر تایید شده است.
نویسندگان نامه تأکید کرده‌اند که آنچه در دانشگاه می‌گذرد، ادامه «روندی نگران‌کننده» است که به دلیل نبود واکنش مؤثر از سوی مدیریت دانشگاه، هر روز ابعاد گسترده‌تری پیدا می‌کند. آنها همچنین نسبت به افزایش سرخوردگی دانشجویان، گسترش بی‌اعتمادی در فضای دانشگاه و آسیب دیدن اعتبار علمی دانشگاه صنعتی شریف هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/76559" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76556">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSu1WPz3ES1F5-IZZU2U4hnQq500Zs8E-gRsodcxflR0jxz4deE1znnLi0svuUHjjOCO7aKASsuCxe4s3hN2IEei1sdc9lfAmJ-f0w3fPvIXuMMJfiA14Hvexrlhwsb7r7MnH-obn4jhy7fuRoNpSIMkto9nhjVyqNXZrRWoqPlbQ9gpG78B2NbTVt5okhXNLngG-InalhImsVu6ooWux9ECOkEMDdfDTDbHjjbKC4bzu4adTYawcfy-Bytsxlu-oeMFgF6Yw45TW-PdLodVoi0aCTD-SFD6H8nwGFyMexEhW_UyESb3ScHyo-FiZNGR1bBo50rB4yI48FCXlLtqaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_367yoLkIZsPXmyEmcgE5rD3_5J2ZjWb6REyY7Fmmjs12xejS56Mc2uUEeTxGFCSPdNJm4Jgb86uBBx1rFvPgSzTSmCEl2TuCLkZdI006AexvcLr6KWl2ZgGvaN1RN0cgMv6yMHgwzWXqCJ1hOEQzDzhs_2L_gjwFmwU03Rrz2EIyoBIsuXyFGmDKELKf2M_sKwoL9W_vCXleQTS9GM55ETHc_1S-tS3m2eciJw5KeEY7gB3UJsHLpLD_7HTVno1ntuIaDYd1Fz9OHC4q8tNBfKmszbASOun3pF28j9NsIoAYTbkCes83ejF5UFcHq_bDU2HXvhTsRkQbnkWZ8S9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
جواد علیکردی، وکیل دادگستری زندانی، توسط شعبه اول دادگاه انقلاب مشهد به ۱۸ سال حبس، انفصال دائم از حرفه وکالت، دو سال تبعید به سراوان و دو سال منع خروج از کشور محکوم شد. جلسه رسیدگی به اتهامات او در ۲۰ خرداد ۱۴۰۵ برگزار شده بود.
🔸
به گزارش خبرگزاری هرانا، آقای علیکردی از بابت اتهام «اجتماع و تبانی برای اقدام علیه امنیت ملی» به پنج سال حبس و از بابت اتهام «فعالیت تبلیغی برخلاف امنیت ملی» به ۱۳ سال حبس محکوم شده است. پرونده او پیش‌تر در شعبه ۹۰۲ دادسرای مشهد مورد رسیدگی قرار گرفته و پس از صدور کیفرخواست به دادگاه انقلاب ارجاع شده بود.
🔸
جواد علیکردی در ۲۱ آذر ۱۴۰۴ توسط نیروهای امنیتی در مشهد بازداشت شد. او ابتدا به یکی از بازداشتگاه‌های امنیتی منتقل و سپس به زندان وکیل‌آباد مشهد انتقال یافت.
🔸
آقای علیکردی برادر خسرو علیکردی، وکیل دادگستری و مدافع حقوق بشر است که در آذر ۱۴۰۴ به شکل مشکوکی درگذشت. وی پیش‌تر نیز در پرونده‌ای جداگانه با اتهامات سیاسی و امنیتی محکوم شده بود که اجرای بخشی از احکام صادره
علیه او به حالت تعلیق درآمده بود.
@IranRights</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76556" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76555">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gDHYMMg4fp_y4nJRVC6VS4EiGsjhJQefG3VB73OOl0QLf0jNKCmo_y5eWr6k5ZloUPXNT6S7BBV4URtUqM-05ftl_ro5GEZspSL82WDjQTacTBjq5GhYhkwjPE1rV_2XZ76bHMhyo1oM5HZWI-lhwrIw_XQnyvXsOb2BCeVhW6xoBmn41Q5KnV4u7t0n8LFQJr6_sp8EmmnVq8hFgBY0KWOzdKjkqzUffqi4r3EWEOZ4BjHMh3j83zZILm6z07p_XM1qh65tDnVgxZL_ggfKtHQbldObidCFFlE7aqLT94DCqELn-B7bHZoHt0AwZNyt4gQGvAVDDO9IPtsryxGyfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: هیچ‌گونه عوارضی در تنگه هرمز وجود نخواهد داشت مگر به نفع آمریکا
ترجمه ماشین:
در دوره ۶۰ روزه آتش‌بس، در تنگه هرمز
هیچ عوارضی در کار نخواهد بود
،
و پس از پایان دوره ۶۰ روزه نیز
هیچ عوارضی پرداخت نخواهد شد
؛
مگر آن‌که، در صورت تکمیل نشدن توافق، این عوارض
از سوی ایالات متحده و به نفع آمریکا
وضع شود؛
آن هم بابت خدماتی که این کشور به عنوان «فرشته نگهبان» کشورهای خاورمیانه ارائه داده، برای جبران هزینه‌های گذشته، حال و آینده.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76555" target="_blank">📅 22:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76554">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/35770a9ed5.mp4?token=brZ1TSvklYTiiP7f-7G9xLD-7HodOQJEZR3z7iqlIStGKPPg9iHpk5-Yg_Q-iPOzyHTahs0_DlZAK-U4gGAG-7wOdpaB0VPXftMIpldlOUMEKv8yNmO-a6dsyO8aU6qzT8XJBU21atkYVtGTSLwVDWY7O-GJ-gzhgCVeN1tV_vQRZ13CYGn_mD0WqdE8ZZ5gSPeut23hA_6A5sBEvFkeMx-Ss8DC7cIw_8wmoLStUE6ZWhvGzNnuQ_zGKcHINuyKxoswbx4lQITRPPkct2dYq4aChsOMOTk_-QgNfxi4UW0ihsmHNGseVMfFOa-6msVYbabxvE5p8Yc1T0gK5iPJLy37MwH3Vt4iHo8trqPYuc10KgSJBq0M0oFCrxpL6c5xxLykhN1juXmUbaGZBlGGAMEeQgtr1hFDwUU8pLk2HVMnGHMRTvDk-5paDCbLCJuJBwX8jFETqNTjEP6uzZexGWDDUfm5OW8zrRQuZOkeKAs74fXgTcwPK9Py6aBv5-07o-pSwYpDq8srbzGnQ6QFTYoodEpS_wqy0ZP_e94M6WiUGxulMpBSGZyc95xtFXdwe9YW0fs9lNHFT_qCcUPdna8N8IhPSP-gGs0GErVrYKmNcKoFyGkK9Ik-84OgC83ief2tqcxoQonGLbRa0pLhp2Y73frGbpUqRclfi3InA9I" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/35770a9ed5.mp4?token=brZ1TSvklYTiiP7f-7G9xLD-7HodOQJEZR3z7iqlIStGKPPg9iHpk5-Yg_Q-iPOzyHTahs0_DlZAK-U4gGAG-7wOdpaB0VPXftMIpldlOUMEKv8yNmO-a6dsyO8aU6qzT8XJBU21atkYVtGTSLwVDWY7O-GJ-gzhgCVeN1tV_vQRZ13CYGn_mD0WqdE8ZZ5gSPeut23hA_6A5sBEvFkeMx-Ss8DC7cIw_8wmoLStUE6ZWhvGzNnuQ_zGKcHINuyKxoswbx4lQITRPPkct2dYq4aChsOMOTk_-QgNfxi4UW0ihsmHNGseVMfFOa-6msVYbabxvE5p8Yc1T0gK5iPJLy37MwH3Vt4iHo8trqPYuc10KgSJBq0M0oFCrxpL6c5xxLykhN1juXmUbaGZBlGGAMEeQgtr1hFDwUU8pLk2HVMnGHMRTvDk-5paDCbLCJuJBwX8jFETqNTjEP6uzZexGWDDUfm5OW8zrRQuZOkeKAs74fXgTcwPK9Py6aBv5-07o-pSwYpDq8srbzGnQ6QFTYoodEpS_wqy0ZP_e94M6WiUGxulMpBSGZyc95xtFXdwe9YW0fs9lNHFT_qCcUPdna8N8IhPSP-gGs0GErVrYKmNcKoFyGkK9Ik-84OgC83ief2tqcxoQonGLbRa0pLhp2Y73frGbpUqRclfi3InA9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نبویان: مجتبی خامنه‌ای نامه داده بود که چرا شروط من رو در مذاکره رعایت نکردید؟
07:20
صدا و سیما: افشای مکاتبات مجتبی خامنه‌ای از سوی نبویان در شبکه خبر پیگرد قضایی دارد
صداوسیمای جمهوری اسلامی ایران اظهارات محمود نبویان، نایب‌رئیس کمیسیون امنیت ملی مجلس، در شبکه خبر پیرامون مذاکرات پیش رو بین ایران و آمریکا را «مصداق تخلف قانونی و مستوجب پیگرد قضایی» عنوان و اعلام کرد «مدیرکل مربوطهٔ این شبکه استعفا کرده است».
محمود نبویان، که به جناح تندرو موسوم به «پایداری» تعلق دارد، روز شنبه ۳۰ خرداد با خواندن بخش‌هایی از متن‌هایی که گفت مکاتبات مجتبی خامنه‌ای با هیئت مذاکره‌کننده است، مدعی شد رهبر جمهوری اسلامی در مراحل مختلف با روند مذاکرات و بندهای متن‌های گوناگون مرتبط با مذاکرات مخالف بوده است.
این گفت‌وگو پیش از آن‌که نبویان به متن نهایی تفاهم‌نامه برسد، قطع شد و موجی از واکنش‌ها را در میان دیگر چهره‌ها و فعالان رسانه‌ای جمهوری اسلامی در پی داشت.
صداوسیما در بیانیهٔ خود اعلام کرد نبویان در اظهاراتش «اشارهٔ ناقص و مخدوش به برخی اسناد دارای طبقه‌بندی» داشته و سعید آجورلو، عضو تیم رسانه‌ای هیئت مذاکره‌کننده و از چهره‌های نزدیک محمدباقر قالیباف، نیز او را به «تحریف عمدی متون» با هدف «فرار از پاسخگویی درباره ادعاهای نادرست قبلی» متهم کرد.
محمود نبویان، ۲۳ خرداد ماه، در آستانهٔ امضای تفاهم‌نامهٔ ایران و آمریکا، در یک برنامهٔ زنده در یک خبرگزاری نزدیک به سپاه، متنی را که مدعی بود تفاهم‌نامهٔ ایران و آمریکا است، روخوانی و از برخی بندهای آن به‌شدت انتقاد کرده بود.
نبویان یکی از اعضای گروهی بود که پس از اعلام آتش‌بس جنگ ۴۰ روزه، همراه هیئت مذاکره‌کنندهٔ با آمریکا به اسلام‌آباد رفته بود.
مجتبی خامنه‌ای، که پس از اعلام رهبری هنوز هیچ صدا و تصویری از او منتشر نشده، پس از امضای تفاهم‌نامه توسط رؤسای جمهور ایران و آمریکا در پیامی مکتوب اعلام کرد «نظر دیگری» داشته اما «با تعهدی» که پزشکیان به او داده، مسئولیت آن را بر عهده مسعود پزشکیان، رئیس شورای عالی امنیت ملی، و دیگر اعضای این شورا گذاشته است.
@
VahidHeadline
حمید رسایی با انتشار ویدیوی بالا نوشت:
نبویان در آنتن زنده شبکه خبر، در حال تشریح جزئیات نامه‌های رد و بدل‌شده میان رهبر معظم انقلاب و شورای عالی امنیت ملی بود که پخش برنامه به بهانه میان‌برنامه به صورت کامل متوقف شد!
ما که از یادداشت‌های آن امام شهید در این باره اطلاع پیدا نکردیم ولی گوشه‌ای از یادداشت‌های امام حاضر توسط آقای نبویان در حال پخش از سیما بود مانع آن شدند!
صدا و سیما:
🔹
روابط عمومی معاونت سیاسی صداوسیما: به استحضار مخاطبان محترم شبکه خبر می‌رساند اظهارات یک نماینده مجلس دعوت‌شده به برنامه امروز زنده این شبکه و اشاره ناقص و مخدوش وی به برخی اسناد دارای طبقه‌بندی و مکاتبات مسئولان عالی کشور، مصداق تخلف قانونی و مستوجب پیگرد قضایی است و سازمان صداوسیما پیگیری‌های لازم را در این خصوص در دستور کار قرار می‌دهد.
🔹
شبکه خبر ضمن ابراز تاسف بابت بی‌توجهی مهمان مذکور به قواعد اخلاقی و الزامات آنتن زنده، به اطلاع می‌رساند مدیریت این شبکه ضمن پذیرش استعفای مدیرکل مربوطه، برخوردهای انضباطی لازم را به دلیل بی‌توجهی به الزامات برنامه‌های زنده و سهل‌انگاری در مدیریت حرفه‌ای به عمل خواهد آورد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/76554" target="_blank">📅 21:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76552">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GElc-kclGr2R0vby6zuISAORI1OCfnA0a8C3TwsJgiDLpzbm63DNgMquy66SZN5g3ddti3VJliXdNL0IQIaH2yPLMZxPeLnF1JfnGY32UZHZB-7GVzOIWQbQcQ0RAj3lnTI8R2cIHyVe9ay_Jc5y-itV2H5sf4tHEqqkuUK1M5SW8QBltc7kECo8002fLVaCrKNr7inz1-eBz0DmHlP11B0n_QsINpsJsV7NlTz9tUA4K5PvgYM-X17PASSbTzrJRlfMpCwY5tBpvUG_R32CUsDyaoyMLW_bbSKZJxowQPqjLYH89fx-FF4XpIDDM8Q4JnCZBzHJimxjEC3AgXjTig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q0G03SdY3cjQnDPrVZU9fuN5cG9ybNXqiDBaCqJ3yKopXLgX8pCbMU1rcL2XRt2nibmh__ur7mgVFdJ0PyhB5kTfI9Vxgv-LZPifnr2r8u6-31N433ojMqqjc1ri4e-L-wE1Avdp4uV-DqOvdFxPAh64GFOot7AZzGvCeK4ZBYB2RcOCFakYadZPNUECCQO-ZfgxUh5VCMLqwJoorNn4HxKULwzVhLRmAV7WN5Nh9jDSFZHrCTz2wHegDgC0UUWG-rE4AWathce5FkLhD1Oy5xzcu6ZZkCYxsOz1eJ3Z7Fh5ToI9SvBVHU3BPW2B_ke_wl5cJLTkD9b1DtOukwVzVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ در تروث سوشال نوشت: محبوبیت ملونی در ایتالیا به شدت کاهش یافته، شاید به این دلیل که او و ناتو در جریان ماموریت جلوگیری از دستیابی ایران به سلاح هسته‌ای، به ایالات متحده پشت کردند.
ایتالیا حتی اجازه استفاده از باندهای پروازی خود را به ما نداد که یک مانع لوجستیکی بزرگ بود؛ آن هم در حالی که آمریکا سالانه صدها میلیارد دلار برای محافظت از ایتالیا و دیگر متحدان ناتو هزینه می‌کند.
رئیس‌جمهوری آمریکا در پایان با لحنی تحقیرآمیز تاکید کرد: اکنون که ایالات متحده ایران را از نظر نظامی شکست داده، او می‌خواهد برای بالا بردن آمار محبوبیتش دوباره با ما رفیق شود؛ اما نه، ممنون!
@
VahidOOnLine
جورجیا ملونی، نخست‌وزیر ایتالیا، با انتشار بیانیه‌ای تند در صفحه اینستاگرام خود، به هجمه‌های اخیر دونالد ترامپ پاسخ داد و حملات کلامی رئیس‌جمهوری آمریکا را «بی‌دلیل و بی‌معنی» خواند.
ملونی در این پیام خطاب به ترامپ نوشت: «محبوبیت من به هیچ‌وجه به رابطه با شما بستگی ندارد و دوستی با شما نیز کمکی به آن نکرده است. محبوبیت من حاصل توانایی‌ام در دفاع از منافع ملی ایتالیاست؛ یعنی همان کاری که همواره انجام داده‌ام.»
نخست‌وزیر ایتالیا همچنین با دفاع از تصمیم خود در جریان جنگ اخیر و عدم اجازه به آمریکا برای استفاده از پایگاه‌های نظامی این کشور، افزود: «نحوه استفاده از پایگاه‌های نظامی آمریکا در خاک ما، تابع توافق‌نامه‌های متقابلی است که ما همیشه به آن‌ها احترام گذاشته‌ایم. تا زمانی که من نخست‌وزیر هستم، این توافقات نباید نقض شوند؛ چرا که ایتالیا یک کشور مستقل و دارای حق حاکمیت باقی می‌ماند.»
ملونی در پایان نوشت: «در هر صورت، میزان محبوبیت من اصلا به شما مربوط نیست. پیشنهاد می‌کنم شما روی محبوبیت خودتان تمرکز کنید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/76552" target="_blank">📅 19:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76551">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/piIHQ4opcwG2h2lctuRBIeGh-FT5kmppwAdtu5a7IEYtZAjfKLDOZYSp9O227FMenqeaIATgSAUaxhV3aUslQCwroRy8apazwm8awwR5K6x8Vow0x5pBPRGCryiQxo3fI5e7_lX8KInFN00bkn35D0_sE3qG33fa-WHLQE3P708EHIewzrweaqnU8sDK3TlyKaA8eKbIiBgpyaM9vfShXgD0FnFkYUS07q4b0j92Yg6pnbcL4yGY-Wq8mjrMNMbnHLwffPQFyM1xlyQhYT0MZdzFe4oACTSE2iWqdYn2uOhcDRympuDU0jUcTEef0X8VejfCTtoQkvYvZoXIB7U0KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران گزارش دادند که هیات مذاکره‌کننده جمهوری اسلامی به ریاست محمدباقر قالیباف و با حضور عباس عراقچی، عازم سوئیس شده است.
بر اساس این گزارش، عبدالناصر همتی، رییس کل بانک مرکزی و علی باقری کنی، معاون بین‌الملل دبیرخانه شورای عالی امنیت ملی نیز در این سفر حضور خواهند داشت.
همچنین کاظم غریب‌آبادی، معاون و اسماعیل بقائی، سخنگوری وزارت خارجه و حمید بورد، معاون وزیر نفت نیز این افراد را همراهی می‌کنند.
پیش‌تر وزارت خارجه پاستان اعلام کرد که مذاکرات فنی میان جمهوری اسلامی و آمریکا، یکشنبه در سوئیس آغاز خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76551" target="_blank">📅 18:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76550">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iwBKBltsSAh-EafEKEeold_77suElDJSsvmKUMSPDn1zu1bP0b9ir9o4zsb0Ru0uXnVGVRBQBl81dbv1_SRQb-hXulpr44eGCvxYypi1IBWo6eDHUyq_xmaInGWakdLaVCADKOEUIRDUxnWUV3AAmG2CC061_fAEvYJ0Fh0Xc-5OHK3mQxkZU5zT9h3PZerg9DmBcd8IW7KX4O4LIsDEoOGVNeFKAPg6xkDnWoQHDe2pY6EPpaNYBpN3JcZXvOV3wPDY-f0K5CDahDU0PTLJNRbt1sAmFf0XWsXbzgSrDQWhwPHANygycplB_6MHXurH-PGAhvDgVr8JbXnRaiegCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: تنگه هرمز باز است
پست اکانت فرماندهی مرکزی ایالات متحده،
ترجمه ماشین:
عبور کشتی‌های تجاری از تنگه باز هرمز
تامپا، فلوریدا — تردد کشتی‌های تجاری در تنگه هرمز در ۲۰ ژوئن افزایش یافت؛ همزمان نیروهای آمریکایی به عملیات خود در منطقه کلی ادامه دادند تا از آزادی کشتیرانی حمایت کنند.
امروز عبور امن از این آبراه بین‌المللی همچنان برقرار بود و ۵۵ کشتی تجاری از آن عبور کردند؛ کشتی‌هایی که حجم زیادی بار و بیش از ۱۷ میلیون بشکه نفت را به بازارهای جهانی منتقل کردند.
مرکز مشترک اطلاعات دریایی این هفته اطلاعیه‌ای صادر کرد و در آن عبور امن همه کشتی‌ها را در یک مسیر تعیین‌شده تأیید کرد؛ مسیری که از ادعاهای خودسرانه درباره الزامات یا هرگونه مانع، آزاد است. جزئیات مربوط به عبور امن را می‌توان در اینجا دید:
ukmto.org
نیروهای آمریکایی همچنان در منطقه حضور دارند و هوشیارند تا اطمینان حاصل کنند که همه جنبه‌های توافق با ایران رعایت، اجرا و به‌طور کامل برقرار و لازم‌الاجرا باقی می‌ماند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76550" target="_blank">📅 18:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76548">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31b632aa9b.mp4?token=k54qZi93urmN2MD6ITxBhRVh-1R4MdgPy6gsCQUeqjOvF6noQYvqPscthpsCnvdHOtrREFQdfkf61QybXk4dSF5cZj50WCPGe8ljcOneB8sd9vLCZtGFfqOU3HF_Eiz6lqmLgtiH-ZwKKBzVffB3SDt9KzHQnjmhdmrGlK7uXBd2wVFGPeesfG86kmNr3RlHGFFJqMlU3A-4Qitmbsvr4FOoScd_rQN_SOlGBALLwzaccVzXq4C63EYwvHurQxR_0JHJme7VBSktA-vV97k3RngramUefIAJ2Vjaca2kEx3hZk81kidXUsi6cVPxjDCf1F7Q0CUYVOAuvS5LE2GXtg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31b632aa9b.mp4?token=k54qZi93urmN2MD6ITxBhRVh-1R4MdgPy6gsCQUeqjOvF6noQYvqPscthpsCnvdHOtrREFQdfkf61QybXk4dSF5cZj50WCPGe8ljcOneB8sd9vLCZtGFfqOU3HF_Eiz6lqmLgtiH-ZwKKBzVffB3SDt9KzHQnjmhdmrGlK7uXBd2wVFGPeesfG86kmNr3RlHGFFJqMlU3A-4Qitmbsvr4FOoScd_rQN_SOlGBALLwzaccVzXq4C63EYwvHurQxR_0JHJme7VBSktA-vV97k3RngramUefIAJ2Vjaca2kEx3hZk81kidXUsi6cVPxjDCf1F7Q0CUYVOAuvS5LE2GXtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی در شبکه‌های اجتماعی پربازدید شده که مادر مانی صفرپور، جوان کشته‌شده در اعتراضات دی‌ماه، را در حال سوگواری برای فرزندش در کنار یک دستۀ عزاداری نشان می‌دهد.
عکس پسرش را بالای دست گرفته و می‌گوید «پسرم، پسرم».
مانی صفر‌پور، جوان ۱۸ سالۀ لاهیجانی، ۱۸ دی‌ماه ۱۴۰۴ با شلیک نیروهای حکومتی در محلۀ سلسبیل تهران کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/76548" target="_blank">📅 18:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76547">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FGAgsroBMne00e1jShGAVYHgb3PLZllioWoG_bCL_9MHSOnJ2NoClIYY7K2wSTH-dS9agRhs2mu5drwyqjU_DPad0sb_Wn-IV4EcFxElbeJegymsfvOBtV1cX9WAUFAJDquPrFjquwHh6IYnUgakfP-xgrVrw3mfBcu7jXL2zttAXjg3TFFo6g8Iq2Syx4YDR8UMcX_XbjXNBcW0EonbJ_JUQGanAiOF-oiFXUgAg88nRAFCK33QdR0pfP2V39W3MAWlkvxZ-mXKWbgzh-8Xdhxs_3745TWPy1idO1e18HncwLLoBNFQq-z6fyrOJJcL-h3z5QbpWrn7geuyxWXscg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد تنگه هرمز در واکنش به «نقض تعهدات امریکا در اجرای آتش‌بس» و «حملات اسرائیل در لبنان»، به روی همه شناورها بسته شد.
نیروی دریایی سپاه همچنین از شناورها خواست به تنگه هرمز نزدیک نشوند و هشدار داد در غیر این صورت، امنیت آن‌ها به خطر خواهد افتاد.
قرارگاه مرکزی خاتم‌الانبیا، واحدی از سپاه پاسداران هم اعلام کرد تنگه هرمز به‌دلیل «بدعهدی و پیمان‌شکنی» امریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه، به روی تردد کشتی‌ها بسته شده است.
قرارگاه مرکزی خاتم‌الانبیا روز شنبه اضافه کرد این گام اول «پاسخ به عهدشکنی دشمن» است و در صورت ادامه این وضعیت، گام‌های بعدی برای «پایبند کردن دشمن به اجرای تعهدات»، برنامه‌ریزی و اقدام خواهد شد.
خبرگزاری فارس، وابسته به سپاه پاسداران به نقل از یک منبع نظامی در نیروی دریایی سپاه، عصر شنبه اعلام کرد که تنگه هرمز از دقایقی پیش به‌طور کامل بسته شده است.
حملات اسرائیل به جنوب لبنان در روز شنبه دست‌کم ۱۰ کشته بر جا گذاشته است. اسرائیل اعلام کرد این حملات در واکنش به پرتاب گلوله‌هایی از سوی حزب‌الله، گروه مورد حمایت جمهوری اسلامی، انجام شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/76547" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76546">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rjQ-TEy66AT-do1kuymNvOC_RkOhQFqOlfFtMqxw4yNC4BK418tgX5uWkIw-ynFD5unt-Yq85_Xeme1srKfdaPnIbpvEKj8dBiwUtTGpsHxBTTTufJvCVoI1qEsoFkfjd-ckrUDWrrYn5e4DaQPl1eLNXvaN84iDxRdPvcfpdL529h3X1YcsSf1vO87xz-Cbyme72jift1SY0b05ERRuiTRGCUtc7HzNoKhbqOx891Vy2Tgz52YTjq4eDGzaFASmcCe8he1-KQxx7DNn-KkrIS6K91glXgNM-PcJUVM0Z-b5XCnKTuX5E7sjsM6Z1UFgZ-7b3mkvaOaS-O7eGk0BUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهوری آمریکا، روز شنبه ۳۰ خرداد در گفتگو با فاکس‌نیوز اعلام کرد که استیو ویتکاف، فرستاده ویژه ترامپ و جرد کوشنر، داماد او، «چند ساعتی است» که در سوئیس حضور دارند و مشغول بررسی «برخی از ابعاد فنی این مذاکرات» با ایران هستند. به گفته ونس، کوشنر و ویتکاف در گزارش‌های خود تاکید کرده‌اند که «امور به خوبی پیش می‌رود.»
ونس همچنین از احتمال ورود میانجی‌های قطری و پاکستانی به سوئیس برای پیوستن به این گفتگوها خبر داد و افزود: «قطری‌ها و پاکستانی‌ها می‌خواهند مطمئن شوند که ما این کار را به شیوه درست انجام می‌دهیم، بنابراین من تلاش می‌کنم به این روند احترام بگذارم.»
معاون ترامپ که سفر خود به سوئیس را در اواخر پنج‌شنبه شب به تعویق انداخته بود، بار دیگر تاکید کرد که انتظار دارد طی دو روز آینده عازم این کشور شود. او با این حال خاطرنشان کرد که هماهنگی‌های این سفر «همواره یک رقص هماهنگی ظریف دیپلماتیک است.» این مذاکرات که پیش‌تر قرار بود روز جمعه برگزار شود، پس از وقفه‌ای کوتاه دوباره در آستانه ازسرگیری است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/76546" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76545">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIN1C2I0oOgbaczgfwd3PGT3fgxPtBQMmZUf5exoiOTOiGDOLx067FggT3T0dESLrDjVSC0z2ZRNgXmFcpsPdgs0wBrImNxHQz2e6Hslyks7pH5W2yF3ctUiTpQlwep72YkyWLkh1FBLBtOu2dIVZNxlocv4Nj4EP669MSct3ALYelZuUpWnOVEk2YJeWnDcceL1Q_fR2O4EBMlC5-KRqApSErzA4D_m4xfiB3lU3nzZ0O902UuY1IDuCobBbhe2gT3KtSnGdXiJwqwrOtAdBV-Cg03GHqCui14dfyATAZ_eKWOpXC6YMGXdYuZ_H7qpJqsuuu1odQgGYC8hmcjjYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«طاها نظری» معترض ۱۸ساله که پیشتر به‌دلیل حضور در اعتراضات ۱۸ و ۱۹دی۱۴۰۴ بازداشت شده بود، پس از  تشکیل جلسه رسیدگی به پرونده، به ۵سال حبس تعزیری محکوم شده است.
ماموران اطلاعات شاهرود، در فروردین ۱۴۰۵، طاها نظری را شناسایی و به صورت تلفنی احضار کردند. بعد از مراجعه به محل، این جوان ۱۸ساله به‌صورت موقت بازداشت و تحت فشار برای پذیرش اتهاماتی نظیر «ارتباط با تلویزیون‌های فارسی‌زبان و فیلم‌برداری از اعتراضات» به او نسبت داده شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/76545" target="_blank">📅 17:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76543">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pceLeAul5mYSGcwQ2iLCXP2ue9b-QexHkSCo2IbnttikpR7S8NAyNwUhmLNJ6HddrLlJUszHBJUu8C3qmGltK97jXoREqGiuhXWrO4DKDE0JrXKp6lT17zZbERPviP6oVMKo8mKDewtEFCeCRjLOXQhy_zZQC4wEr7ew2SpIh7MfLc3riE3iiYJXpA40nk4781tB0G6_wm7F1uagXVYnzRwk4nZOCP4dCWU4A1iBaxz6DxV-EdIs_BPPXebFUUpymya57Urzamegj1Xnp8wcm8ToIxyw-dDtwYhyN47k6mPJli-dGO_LjWcZEXKVFGlN_Bs10eYOX2pFkTBNpLOEyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YKdA-nTabanLzfHTCpINQZ4ozV18lhzPhUiCTJAYjStxuNHMrUakDET_fSJnBBdSSYQHw7mPF_8LaBk-gHg_d3rlVygpKfIW1Ij8Wn3M25iNQ3dE7w2FqNhJXVt2WYUIxawPx6b9NQm5dCVoboClj3D7fyQh1uWFWoYtk_etWzyRJ0l0tfVBrjqAiHhBZWknIwPQvRhh-CKbil0PEQhkaqONxA1SbnAdQQTnKm3l8AOFG0QxQbiuP333tZnhfgbjUYoI3tXab3ybf923Pa4-850veHYi6tQ09AFgUCSyLs6LR_iqQ7vPRnXiRAxwsLbgVw9VrQke6tXizydcJQJUYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت دلار و دیگر ارزهای خارجی که در پی نتیجه موقت مذاکرات ایران و آمریکا کاهش یافته بود بار دیگر افزایشی شد.
روز شنبه، ۳۰ خردادماه، قیمت دلار آمریکا در بازار به ۱۶۲ هزار و ۵۰۰ تومان رسید. قیمت یک یوروی اروپا نیز در این روز به ۱۸۶ هزار و ۴۰۰ تومان رسید.
این در حالی است که در طی روند کاهشی قیمت ارزهای خارجی در بازار آزاد ایران، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان رسیده و قیمت سکه طلا هم در محدوده ۱۶۰ میلیون تومان اعلام شده بود.
روزنامه هم‌میهن روز شنبه قیمت سکه امامی را در بازار طلای ایران ۱۶۹ میلیون تومان گزارش کرد.
از زمان اعلام تفاهم‌نامه ایران و آمریکا در تلاش برای پایان جنگ، قیمت ارزهای خارجی و سکه طلا در بازار آزاد ایران شاهد کاهش قابل توجهی بود.
@
VahidHeadline
حسین صمصامی، عضو کمیسیون اقتصادی مجلس شورای اسلامی، در گفت‌وگو با سایت خبری تابناک افشا کرد که در هفت سال گذشته بیش از ۱۳۰ میلیارد دلار ارز حاصل از صادرات به کشور بازنگشته است.
این در حالی است که حکومت برای بازگرداندن ۲۴ میلیارد دلار دارایی مسدودشده کشور وارد چانه‌زنی فراوان با دولت ایالات متحده شده است، امری که نشان می‌دهد تا چه حد به این پول نیاز دارد.
در این میان بیشترین میزان عدم بازگشت ارز صادرات مربوط به سال ۱۴۰۴ است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/76543" target="_blank">📅 17:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76541">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jQ1wVsdfcjxDWZyWsPq_oJYw229m1pWE_nxX2-e5vxBkinfRdgXE0B0ITMVYqrKYzTm6qzQFgbLd2umSE0oyoeyoUFXe2LPI6gQIl5uH--H3RDGWpX6KhPs459eQ4OGZKVQ-wuEFSes9Kmg9RLPjVgV5vbLvFSDaONM9wnqzGGzTBkTpYG2-TuFhXqZxoSb-70XdI1ObCNKbgF0RospcnkTiJKgM7Cc3I6shEbjWAWjl54sftsNnK1CQP2uY08379u8VlqL6BY53C86bf0ID4E3if_ENf1hXif1uMYfPoNl4Z2VFNktM7RfnJJiDiYMsJmAqFtvlUL96fV4tbIgQyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbc33926c.mp4?token=IPHfCKhSrBuxvGEQE5NqNLnAVsgiTSuqIwL7MgYIAr7-FjKzcDH58p_Zq5D8p2VhrLmVYuuDqYaJRkUiYt2fCvd3VplpQERNW55WfMEicOR609GOf-b1fv75uUGyPp4dU41-g3wtn3yxi9T_faBooTlKTvCmedFfNevT2RXjFijUI4Ewm43uNQbvrYDAAJc2DcM0ZI-gtABqKj46zG0oOxEWWQYRdVbrUiIt6f3TeOHAXhGcJC0t0Wpec2lly98NXaEwi-nVvqisTS6ofUZQVLhNnzBdmt2UVLNR3BSMlDQankmtardbQ7MyhzAeO-HpH37hsALAvmTs9qz6zMvw5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbc33926c.mp4?token=IPHfCKhSrBuxvGEQE5NqNLnAVsgiTSuqIwL7MgYIAr7-FjKzcDH58p_Zq5D8p2VhrLmVYuuDqYaJRkUiYt2fCvd3VplpQERNW55WfMEicOR609GOf-b1fv75uUGyPp4dU41-g3wtn3yxi9T_faBooTlKTvCmedFfNevT2RXjFijUI4Ewm43uNQbvrYDAAJc2DcM0ZI-gtABqKj46zG0oOxEWWQYRdVbrUiIt6f3TeOHAXhGcJC0t0Wpec2lly98NXaEwi-nVvqisTS6ofUZQVLhNnzBdmt2UVLNR3BSMlDQankmtardbQ7MyhzAeO-HpH37hsALAvmTs9qz6zMvw5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که هاجر نادری، مادر متین پرویزی، در صفحۀ شخصی خود منتشر کرده است او را در کنار آرامگاه پسرش نشان می‌دهد که می‌گوید «من به پسرم فقط یاحسین و تشنگی را یاد ندادم، به او یاد دادم که جلوی حرف زور بایستد»
خانم نادری در ادامه با شرح کشته شدن فرزندش در اعتراضات ۱۸ دی‌ماه می‌گوید امسال محرم برای فرزندان میهن که «ناجوانمردانه کشته شدند» عزاداری خواهد کرد و ادامه می‌دهد که «می‌دانم امام حسین هم برای این جوانان عزاداری خواهد کرد»
متین پرویزی ۱۸ دی‌ماه سال گذشته در سبزه‌میدان زنجان با شلیک گلوله جنگی نیروهای حکومتی به سرش کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/76541" target="_blank">📅 17:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76540">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNqleowcXyGW9aFfZIWOVrP8_OIhxRFvOxi-qqZVFkMC8P16TP3Ym1B1H7C5E_usWBtks3stNqp6lDUJhHPHkIPyNDDPckX_Qr51GviYi8_ISLkgIRjBU7Q7uwSYS51P3O-iGu0yOqyGAaCYHj77VFuB_Vlm8l5gnSYAM-k07nE1UkXzIRMuVmiq0-DtPlEuX5mxD5ln0LFwAhc4Hsp8B0YdHZ75i9U9Wu2w4x1R9KO3RGteJ2ChEA6as01Xd0DdFHtGPgmOP0BKObryL_YheZZRwO8c2qOuztGQPJ-5HY1GsdS7rKF2LgIyLE5CF3VWZChNjndRNn3Hpc5CWD7Frw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن نقوی، وزیر کشور پاکستان، صبح امروز وارد مشهد شد.
ایرنا به نقل از منابع خبری در استانداری خراسان رضوی گفته است که او سپس برای گفتگو با مقامات عازم تهران خواهد شد.
بر اساس گزارش‌ها وزیر کشور پاکستان قرار است در این سفر در مورد از سرگیری مذاکرات مستقیم بین آمریکا و ایران در سوئیس، با مقامات ایران گفتگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/76540" target="_blank">📅 17:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76539">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNmRxg4dG31SgtyVx7RzLTzg6ey28iiRqQlz8ETZuVEGZToWNqQQFdp4OBgN8oZmVVpbjdVFyQ10EvV5w4rTAetGuYQMUxno0NzpKHO_zSs62k2HSThF2Lu3EXEZ8m4NYTXatRzHbUSj5fJNzoKKGEc37KY8KuNASj9bafTFEj0NsZQ5E7xi7Ifb0qrM3RXDoJT410ylrnwNIMkUB2QsGUGbpbvTtjp7rs2fYjjwDrfALaLHZU_UYnFN_KrJGDTwigH47CzbAor_cIQaT7RG5dUMOXHG1U3n-f6NFNaEYHEgsxELCSCtCXfdLkiEVf6znB3bhBypO4RZ2OEXotUrmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز اطلاع‌رسانی پلیس استان لرستان از پلمب یک واحد صنفی و معرفی فرد متخلف به مرجع قضایی خبر داده و اعلام کرده است این اقدام پس از آن صورت گرفته که به گفته این نهاد، واحد مذکور «ضمن عدم رعایت قوانین و مقررات، اقدام به هنجارشکنی» کرده بود.
این در حالی است که تنها سه روز پیش نیز مرکز اطلاع‌رسانی پلیس لرستان از پلمپ پنج کافه‌رستوران و سفره‌خانه سنتی در سطح استان خبر داده بود. در آن گزارش، دلیل برخورد با این اماکن، اجرای طرح موسوم به «ارتقای امنیت اخلاقی و اجتماعی» و آنچه «هنجارشکنی» عنوان شده، اعلام شده بود.
در هفته‌های اخیر و هم‌زمان با فروکش کردن فضای امنیتی ناشی از تنش‌های بیرونی، گزارش‌هایی از افزایش تمرکز نهادهای انتظامی و قضایی بر حوزه‌های مرتبط با سبک زندگی شهروندان منتشر شده است؛ روندی که به نظر می‌رسد بار دیگر کسب‌وکارهایی مانند کافه‌ها، رستوران‌ها، فضاهای موسیقی، پوشش و نوع تعاملات اجتماعی را هدف قرار داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/76539" target="_blank">📅 17:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76537">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f49d58cd5c.mp4?token=BAKIom30wklLSq7gRGHS5FeIrBSsFs2UB2z-skTRKBaWifJIf4wqnher_MKeNG7J6p6M2mdeZA84pLnXTFbI1PoK07Ug5NNKxsIMbS-1tr0f5DUDlGo1rTWcLkdacSePj750DbUnlGZOpKNV-WbObEj_IxxDhB66vEp-G5tOudl4VaLHEELLPb4B2vEgsLYx-WEMLgiozdVsbrqlkkS2TKND6Npp9AZR1XSVbMoQ-Tic2-uNCxReXmwpE4JxhgQCIDmsM3bT74nsNTFfTMcZIugLbX1McoCecG-DLui9-MBYuNNUu7QVWe6fasv32qYrPbTNXYSryth4WoJufa22-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f49d58cd5c.mp4?token=BAKIom30wklLSq7gRGHS5FeIrBSsFs2UB2z-skTRKBaWifJIf4wqnher_MKeNG7J6p6M2mdeZA84pLnXTFbI1PoK07Ug5NNKxsIMbS-1tr0f5DUDlGo1rTWcLkdacSePj750DbUnlGZOpKNV-WbObEj_IxxDhB66vEp-G5tOudl4VaLHEELLPb4B2vEgsLYx-WEMLgiozdVsbrqlkkS2TKND6Npp9AZR1XSVbMoQ-Tic2-uNCxReXmwpE4JxhgQCIDmsM3bT74nsNTFfTMcZIugLbX1McoCecG-DLui9-MBYuNNUu7QVWe6fasv32qYrPbTNXYSryth4WoJufa22-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع‌های اعتراضی زنان به فعالیت‌های معدنی حوالی دو روستا در استان‌های کرمان و سیستان‌وبلوچستان با حضور نیروی انتظامی به خشونت کشیده شد.
بر اساس گزارش‌ها زنان روستای پشموکی از توابع فاریاب استان کرمان روز ۲۷ خرداد در ادامه اعتراضات مردمی نسبت به نحوه واگذاری و بهره‌برداری از معدن کرومیت پشموکی تجمع کرده بودند.
گفته شده که نیروی انتظامی علاوه بر ضرب‌وشتم معترضان، شماری از آن‌ها را بازداشت کرد.
هم‌چنین منابع بلوچ گزارش داده‌اند که زنان روستای سرسیاه از توابع تفتان استان سیستان‌وبلوچستان هم روز ۲۶ خرداد در اعتراض به گسترش فعالیت‌های معدن طلای تفتان و پیامدهای آن بر زندگی مردم منطقه تجمع کرده بودند.
در ویدئویی که منتشر شده شنیده می‌شود که مأموران نیروی انتظامی با خشونت، تهدید، توهین و واژه‌های تحقیرآمیز با این زنان برخورد کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76537" target="_blank">📅 17:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76535">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/egLF74GT2Etlxx2qX3nq8ws5t3G_ZMVHL3DUnZynT_VSbJQVkXLWl7ubD2BpAmV2w4-1F9fyDfvO4mOac4exki-NGXA18JrmEVQDaQI5h6gglNkmqFytWWdIW7tscytGdKA6O4hqHTYn90NcDU0QAXVQF4PeJBZwe103wVP9bJT7iUl_zEi49WFbYB4fMja87kgAWt45IEb10v3oH5Zp9FZ5qxAU1s58vrgKbX_m9L4rPE8yWt7wuS5kCRmOmmuSmLdyl7UCnjKqtxzyY4htpcZsIN9KPU34tb1QmUdA-qmTbJDyvmfIc5BMTusiGKrhcZoCeYjmpiC0xbHlM8RVLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vsbtoyfZTuY79YDvWlvia1G-RaZ8KCngcjGQpCbU-wxvYYFy0B21HG8sfQ0--UY3ykxRd0ozOeSONCh08txyeIdvD08T-MZw_TeSJA__mxQ5aMRJf99fsvTKqSnKLrxkYg9UuVrvSmf7rMawDKs0kTqQyiKpwRm3NLnxJs6p1s2Euo8xC9jjK8UTXhIDpL-MZ3MkxWtjVjX1e0StRZ03RyTNNJdvqyyt4AYkMhUEydfjnw038flX6VUE_fHk1QWaYEToEzoTbCRn_ebjkmkzAflKVx55OTUPORl3F66fxs7gRx2xwams3ypE4QdURTt9j0oUQIg2Jlg8g1ozZDK1-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس گفت: استیو ویتکاف، فرستاده کاخ سفید، در حال سفر به سوئیس است، جایی که انتظار می‌رود دور اول مذاکرات با ایران در مورد توافق هسته‌ای احتمالی برگزار شود.
به نوشته اکسیوس، قرار بود مذاکرات جمعه ۲۹ خرداد آغاز شود، اما به دلیل درگیری بین اسرائیل و حزب‌الله در لبنان به تعویق افتاد.
@
VahidOOnLine
خبرنگار اکسیوس به نقل از یک منبع آگاه، روز شنبه اعلام کرد: «عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، در حال برنامه‌ریزی برای سفر به سوئیس در روز شنبه است.هرچند این برنامه همچون گذشته ممکن است تغییر کند.»
این خبرنگار به نقل از منبعی در یکی از کشورهای میانجی فاش کرد که عراقچی روز جمعه به چند تن از همتایان خود گفته است: «موضوع آتش‌بس در لبنان برای ایران یک مسئله حیاتی است و حکم برد یا باخت (تعیین‌کننده سرنوشت) را برای مذاکرات ایران و آمریکا دارد.»
خبرنگار اکسیوس همچنین به نقل از یک منبع دوم از میان کشورهای واسط افزود: «ایرانی‌ها صراحتا تأکید کرده‌اند که می‌خواهند پیش از سفر به سوئیس، شاهد برقراری و تثبیت کامل آتش‌بس باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76535" target="_blank">📅 04:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76534">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e1550d193.mp4?token=U5UvkR2rENorgRUoPbsrxk3YCnjcnlhq8ppTaACiltvw-v77R-3RcvRSkR6RKsvAveIXZblNAiaSqJk5XOryxODyXhDDb03Mm2rOV16YScQwc2FnixZAVeibnhdi8ZrXXEf8wbsvFFsr1m6cx1BtqOupLfTCjxQIqqAgqmXQQsXNmAR7nHfLZ23B0VIGN_US5jL1SLB2WjzN5QYHPXjKNNjdl0yayg4jKA6ftFqlhW2cMHLDqNcQsG6f913C2aq7XuHPY_NA3kiDisokAQOSraTtf8YUYmxX64fPle3O6lO8gvoiMAu1DLGJVsonhKODiUGCRYOiBZFYbg9swlclOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e1550d193.mp4?token=U5UvkR2rENorgRUoPbsrxk3YCnjcnlhq8ppTaACiltvw-v77R-3RcvRSkR6RKsvAveIXZblNAiaSqJk5XOryxODyXhDDb03Mm2rOV16YScQwc2FnixZAVeibnhdi8ZrXXEf8wbsvFFsr1m6cx1BtqOupLfTCjxQIqqAgqmXQQsXNmAR7nHfLZ23B0VIGN_US5jL1SLB2WjzN5QYHPXjKNNjdl0yayg4jKA6ftFqlhW2cMHLDqNcQsG6f913C2aq7XuHPY_NA3kiDisokAQOSraTtf8YUYmxX64fPle3O6lO8gvoiMAu1DLGJVsonhKODiUGCRYOiBZFYbg9swlclOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو بخش مربوط به ایران از مصاحبه امروز ترامپ
متن کامل این بخش‌ها:
https://telegra.ph/trump-06-19
بعضی از جملات همان متن:
ترامپ: و من آیت‌الله را کشتم. یک مقام سپاه هم بود. و متأسفانه به آیت‌الله دیگر هم آسیب جدی زدم. به شما بگویم، من او را ملاقات نکردم، با او صحبت نکردم، اما دیگران درباره‌اش حرف می‌زدند. او شجاعت خاصی دارد، چون به‌شدت آسیب دیده است.
با وجود همه این‌ها، نمی‌توانید بگویید بی‌خیال. من ارتششان را نابود کردم. نمی‌خواهم این را نادیده بگیرند.
برای کسانی که می‌گویند شاید من به‌اندازه کافی سخت نگرفتم، باید بگویم من ارتششان را نابود کردم. بزرگ‌ترین پلشان را زدم، چون دیر در جلسه حاضر شدند. گفتند این کار خیلی قشنگی نبود. من گفتم پل جورج واشنگتن؟ سه دقیقه‌ای نابودش کردم. خارک را زدم، همه چیز را، جز یک چیز. گفتم به لوله‌ها دست نزنید، چون نمی‌خواهم به اقتصاد جهان آسیب بزنم.
بنابراین فکر می‌کنم خیلی سخت گرفتیم. به کسانی گوش ندهید که می‌گویند می‌توانست سخت‌تر باشد. کل ارتششان از بین رفته است.
پرسشگر: چطور تغییر رژیم است وقتی هنوز خامنه‌ای جوان‌تر و خیلی از مقام‌های سپاه آنجا هستند؟
چون افراد متفاوتی هستند. خامنه‌ای جوان‌تر با پدرش فرق دارد. افرادی هستند که بسیار کمتر از دو گروه قبلی رادیکال‌اند؛ و من هر دو گروه قبلی را می‌شناختم.
اما به این فکر کنید: همه آن‌ها رفته‌اند. بعد می‌گویند چرا سخت‌تر نگرفتی؟ تنها راهی که می‌توانم سخت‌تر بگیرم این است که دو یا سه هفته دیگر وارد شوم و آن‌ها را شدیداً بمباران کنم. اما این چه چیزی برای ما به دست می‌آورد؟ تنگه هرمز باز نخواهد ماند. فرض کنید این کار را می‌کردم. فرض کنید تصمیم می‌گرفتم این کار را بکنم. الآن بازار سهام ما فوق‌العاده بالاست. قیمت نفت در حال سقوط است. قیمت نفت تقریباً همان جایی است که قبل از شروع کار من بود. تفاوت بزرگ این است که ایران هرگز سلاح هسته‌ای نخواهد داشت. آن‌ها هرگز سلاح هسته‌ای نخواهند داشت، روشن است؟ خیلی واضح و ساده است.
آیا می‌دانید در دو ماه گذشته، من کشتی‌های زیادی را از آنجا خارج می‌کردم و کسی خبر نداشت؟ می‌دانید چرا خبر نداشتند؟ چون ما رادارشان را از کار انداختیم. همه تجهیزات دفاعی‌شان را زدیم. آن‌ها قادر به دیدن نبودند. هفته گذشته، یک شب ۲۵ کشتی داشتیم، یک شب ۲۲ کشتی، یک شب ۱۹ کشتی، یک شب ۲۱ کشتی. هر شب، همه این کشتی‌ها بیرون می‌رفتند.
ایرانی‌ها مردم بسیار باهوشی‌اند. نوعی نبوغ ابتدایی دارند، اما باهوش‌اند. منظورم این است که باید جلوی آن‌ها را می‌گرفتم، چون اگر سلاح هسته‌ای داشتند، از آن استفاده می‌کردند. می‌خواستید ببینید؟ بگذارید چند شهر را در جایی منفجر کنند؟ مثلاً اسرائیل را منفجر می‌کردند.
اگر من نبودم، اسرائیل امروز وجود نداشت. چون من توافق باراک حسین اوباما، یعنی برجام را لغو کردم؛ توافقی که مسیری به سوی سلاح هسته‌ای بود. آن‌ها پنج سال پیش به آن رسیده بودند. به نظر من، در همان هفته اول از آن استفاده می‌کردند. اسرائیل دیگر با ما نبود. اگر من آن کار را نکرده بودم، اسرائیل سال‌ها پیش از بین رفته بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76534" target="_blank">📅 01:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76533">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfBOIjBq5sRm5gnEjQruoB2eiX-WW1HJYHEPcYNH3syyDdLdEWNqToUtWzpbHRLny_CKlFlK9UiqOgR6QOc0tIM9gllGAxJYdl9eZNn3Pn6tc76pVKOw6DxFF1bKwlJ54yRKqoAOQMuKPVBowZhbPxzi2UrFX_ABzF-D3qXM2AMK-QUQ6FfpskEXlFq01cD8jQlwYuWuJ6XkYG_fKy3onIjgJSA6Llt7C85SibLfYIj1V0GueA07mKyIPBZ2sBbuyEfoQDedfYJuzur2H-5PV1ggDU0k0v2GaCaMc9PyIH2c_cSaFLi1xyy5TXGITrccyKipNc4ftnDQQWKbgCwtlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس‌جمهوری آمریکا، در مصاحبه‌ای با برنامه «آکسیوس شو» با دفاع از تصمیم خود برای شروع عملیات نظامی در ایران، مقام‌های جمهوری اسلامی را «بسیار باهوش» و «نابغه‌های بدوی» توصیف کرد و هشدار داد که آن‌ها در عین حال بسیار غیرقابل‌پیش‌بینی هستند.
ترامپ با اشاره به مداخله نظامی اخیر ایالات متحده گفت: «من مجبور به اقدام شدم تا جلوی آن‌ها را بگیرم؛ چون اگر سلاح هسته‌ای داشتند، حتما از آن استفاده می‌کردند و با منفجر کردن چند شهر، از جمله در اسرائیل، هرج‌ومرجی واقعی به راه می‌انداختند.»
او با تاکید بر اینکه اگر اقدام او در لغو برجام نبود، اسرائیل سال‌ها پیش نابود شده بود، توافق دوران اوباما را مسیری هموار برای دستیابی جمهوری اسلامی ایران به بمب اتم دانست. ترامپ همچنین با ابراز شگفتی از زمان‌بندی تقابل با ایران افزود: «چیزی که مرا غافلگیر کرد این بود که آن‌ها این‌قدر منتظر ماندند. آن‌ها صبر کردند تا من به قدرت بازگردم؛ البته این کارشان عمدی نبود. هیچ‌کس، حتی با وجود سلاح‌سازی ساختار حکومتی علیه من، فکر نمی‌کرد بازگردم، اما من با خروشی بزرگ‌تر از قبل بازگشتم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76533" target="_blank">📅 22:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76525">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشجویان متحد</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s9YJdlmJu6V9fF2-29e78ImrzXbxw3WDcpsX8BRpnaquYUI5ZV07fSAVQ9AfEocmrrRZs1dpPHeEiMU154mvAzWZ5DBRSH4k-3C108dtzumAdCWPk-F4HpNHB1Cx201MxN_aODXncxasQw9G3eJkEVLox9cmJZ5f8xOTfNgwWGez52g7gokbKzufsckpLmBCN0vleSfeSd3XYib85C62EaGku-jpaLhQZmZP4Fl0zznG95_Nbpe23QLQRCANrpmRLh6EMDtBhKJWi4iKzFm7lT1ds5EmNIncel1Z9JZXuhxGPDxY8zOrJO29YvpKUEWxjMykONYmznc7f-TKQTpNDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pAEAel-yx1yrSXExbpDSh5REIIeWWB_Y_3NYs_cDUPRCnm-z4ODvgyF527Ntsq15tcx6_-Z_oMXxm6s7NhqS15G_1xLgAJ9PVSjBokxbz-tVMj4r_54vJBQN1OzSohA116EpiBLvo9N02mxKw8otfWW2NqSrmE_urofBZuLmnolZvrNBVC3fcr4NeyqxAble0aK_Oa4vJnfixOMcg9mZNePP19tmbpcxmWeul_BjR4VqQAskPIj5Xujgi7qAJ9IO6T8bb2tJdxbm_yd1lToy4o7oWq0ZOuX75SFrhM_dP1x9Cfd-lJjjBBfBFIZsnEWrJffxmLmzJyVHzAyBzdBB1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IM9fVcpdQMFv6RtNI3xd9m-z_MglwRRhLIdjEJeQq4lxQzQPvqOH1HyPfwFOHQEATHZUv06zvoxfMuwWNeirnSoLP7x3psDH1lUL6bGUyH-U0WoIFfuUHp5Q7mw1TbBny4Gy49Res8yGTVTP4xfQ6M3dzJGlBvyE3WIsMKYNqFq4XbT1X5lFpXHr7u1Vnj1M_l3kV-f5cZ-RvhswIVRkkLLk0TmsM1-JdPhIs0sWUYDwy-liL8DdMKQRmSBoOLTlUHbV4BjnRz9dioVCcgTxIUmO-CI7AgfqyFZgw5DiRpAwsad2PkYoXdPTKIgiiKw8KK0RR8qibd-q9cdgCziIqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XRga5ESWMjLIjyYBwT4CfrSR8Ce7xWZKGdS6LQonOatS4c-uIuFfPDnLaEbiatt2NxiX35axeBjipRbpXIGZwgERN1zR20TQnQYG2wammvYwk-QKEswArASXoBohhzg8qaTgeZURSKRmSHDlYy5gIcJbf-j0p9fDhUyDqsY4q1CmtlUQjLdTy8lZsLgQmo2Pkcu-oZ5IoglSq6oA798sp1wrI3iD1Yw3U3WQsv38CLdHnwPJ056JXqpjBNtV-9v-wA--r9yY_hvsVD5XU_R2wafiXsB4ZrNuMNWx4Q7u7W-HBGwcgqqdoX8-S9km9ROK5uvbmzIlZZwOs1MlJzgr_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kH9fzjYx4feKz2wucDhBFuYksFlUXLcL3jhbt8C2uIZwoI59-Azdlr15KsuwfOgL_8TsZwdqwOMZSS7LQg2mjw1zHPLO9IVa5wFVFru4tiG6TvWTikFILta1eB8dM1uPUKWzipII3RzYg4gig0CzF0xdHVNhFclrl51hH_GJ3-5OIu6tDw5LhdnHCwrzdsRyAAcZT_GmoiK8fmfzWHEDvqOQmP9to8qa2KLeiBGjzp3TlOEWIS7ZEDnz30neru5A0Rw3_mT5FeKg67iVT90Pg-ryHdWI_ULF0td5t70m7-dP3wM1Yx2kIEOcGperv7DSvcOSjWYl3-OD9S5PAxBQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kTWGtwqkeQ5negeYGI67AzZHo9ddRhhm7wWvsVKzggTfaIcP1CGXuhHvfsuowO9LQSt6ccsa_f0oNWjpBCawwunG-jNM0ePfCAbfWl8KonWt3FRgbMCVxlh0jL4vy1cQMnWajE2C-vuV-D0UIBtLMrRmGYYUaKXs13sCKpRlTT8nd9Lrop154wrS6HVcfg7B__xh4QdY1l-NbYmo4f6rKg5CeBaU5tTXoxg_YjX7JexNiZVxYAe5DyfJO-4duoGdSIhxVUhfy0tnbD5Ky3kwJbGoLwg-J_4gAYGArv_4G8PtEsiND8Q21vSwXD1vr4OB6VP0AW9rqrc0ryvZxBwMEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/grQYNdbBJdvjQaQzHdJuf6S6GAaa1oMhMqI-rhloPGVl1aCz5W4ngv6FA9bAMOrzXaM8YTKc5jobtCft9_FOymRa3EqCP3luiYtaQuz7HwKUmxPAUtwodh5yaX4tsZUN0ffre8CpsUjDvFdFfHFQbyfvV0sI8i-3Zb5Vdm3SwqtPPrBBoGOdufdXiFLN0keqGWkfheizj1m35MVnQAFY3-tzceualLcWOHPajowjk-IYO08NfqfLLIxHEXUah7BxqNiN9qbjZxj64WjvEPaLoRXDEQ-3wczaYCrVix9D7fclkJvMkGGUDAggqo_u_NPL7wwRclscYU0yq0-f0GAa2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0owT-WRESdAG6A4dnynM1CgLtdANVLkgms0dTprbLLLir5OoV73GF3KJmRSwNcyRdhZGE9aqk9hBIXkoYvA2J9_OZD9dnu4dsasCMvjAVhXnLZMGhLbyw3F7EA-H7vHNknE4_2lYstQ9lqp5YmSBKnLf-tmMHA0_GGcOtg9uFxGPo07xBzcpOjZ3301wwlLqo2H9xbwV4BkItziPf86nqsTfMj67DgBNevMV23BZ9473cOQTwuRk7oBXbr5C6g-Ff0P42p8H0wIP0DJ20FcSqmekAhrFkOrVzqm4HLdJA-OCqkb3nZ_85AwY3NOFZgYxStGyNT-3s_gKFs44o7BJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
صدور حکم اخراج برای هفت دانشجوی دانشگاه شریف؛ صدور حکم غیابی برای یکی از دانشجویان بازداشتی؟
🔻
بر اساس گزارش‌های رسیده به دانشجویان متحد، کمیته انضباطی دانشگاه شریف، برای هفت دانشجوی این دانشگاه حکم بدوی اخراج صادر شده است. اسامی دانشجویان به شرح زیر است:
🔻
رضا دالمن، ورودی کارشناسی ارشد ۱۴۰۳ مهندسی کامپیوتر: اخراج و چهار سال محرومیت از تحصیل
🔻
فاطمه خاکپور، ورودی کارشناسی ۱۴۰۳ شیمی: اخراج
🔻
حسین شادمان، ورودی کارشناسی ارشد ۱۴۰۴ مهندسی صنایع: اخراج
🔻
سپنتا سعیدی، ورودی کارشناسی ۱۴۰۴ مهندسی کامپیوتر: اخراج و پنج سال محرومیت از تحصیل
🔻
مسیحا باقری، ورودی کارشناسی ۱۴۰۲ مهندسی کامپیوتر: اخراج
🔻
فریبرز کهن‌زاد، ورودی کارشناسی ۱۴۰۰ مهندسی برق(تغییر رشته به مهندسی صنایع): اخراج و پنج سال محرومیت از تحصیل
🔻
پرنیان خدابخشی، ورودی کارشناسی ۱۴۰۲ مهندسی و علم مواد: اخراج و پنج سال محرومیت از تحصیل
🔻
همچنین در برخی رسانه‌ها خبر صدور حکم اخراج برای «آریانا کوچکی»، ورودی کارشناسی ۱۴۰۰ مهندسی صنایع، نیز منتشر شده است. هر چند بر اساس گزارش‌هایی که به دست ما رسیده، ایشان در حال حاضر بازداشت هستند و خبری در مورد برگزاری کمیته بدوی ایشان نداریم. هر چند صدور حکم غیابی برای دانشجویان بازداشتی در جمهوری اسلامی، پدیده تازه‌ای نیست.
🔻
لازم به ذکر است از میان هفت نفر یاد شده، کمیته سه تن(سپنتا سعیدی، حسین شادمان، مسیحا باقری) با محوریت فعالیت در شبکه‌های اجتماعی و کمیته چهار تن دیگر با محوریت اعتراضات اسفندماه برگزار شده است.
ارتباط با ما:
@Public_anjmotahed
🆔
@anjmotahed</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76525" target="_blank">📅 22:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76524">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba856aba9d.mp4?token=bQrXd_NQdXHOd7vHfc6bP8H5MT7mfbr4fNHcpL_s0bjoTvMIYfMmH9vT75HT4jrdiUMuBKyoDXhm5NEooOBFzKPN-qc_DPPFXbLorh6gpk47OYNJKdkExyT7Pklr-ztIGj2x6PwtoV32hmUIXmFAaO6PRL09Qln0bOyD_zWVNHOhaLOvzbgKyOF7ec_0Mwl9_9uwIBl3YMC5zNdrdHRC0oOqC7m9ncJ3l8PiT-WLPJxHyR9ZA033w02QYx2rGezAZMYnmKOcU_A54r0aNFviWnHPgO4KTCz0QCzy3KZSkMWAKuGAmMQXRWV7C3z5voZBQpmlNybiExAMdQ5S6Jv-Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba856aba9d.mp4?token=bQrXd_NQdXHOd7vHfc6bP8H5MT7mfbr4fNHcpL_s0bjoTvMIYfMmH9vT75HT4jrdiUMuBKyoDXhm5NEooOBFzKPN-qc_DPPFXbLorh6gpk47OYNJKdkExyT7Pklr-ztIGj2x6PwtoV32hmUIXmFAaO6PRL09Qln0bOyD_zWVNHOhaLOvzbgKyOF7ec_0Mwl9_9uwIBl3YMC5zNdrdHRC0oOqC7m9ncJ3l8PiT-WLPJxHyR9ZA033w02QYx2rGezAZMYnmKOcU_A54r0aNFviWnHPgO4KTCz0QCzy3KZSkMWAKuGAmMQXRWV7C3z5voZBQpmlNybiExAMdQ5S6Jv-Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه جی‌دی ونس با زیرنویس فارسی
گفت‌وگو با:
الی بث استاکی، مجری و مفسر محافظه‌کار مسیحی آمریکایی، میزبان پادکست Relatable در شبکه BlazeTV
برنامه‌ای که در آن از زاویه‌ای مذهبی و راست‌گرایانه به سیاست، فرهنگ، خانواده و مسائل اجتماعی آمریکا می‌پردازد.
او در میان مخاطبان اوانجلیکال و محافظه‌کار آمریکا چهره‌ای شناخته‌شده است و در این گفت‌وگو با جی‌دی ونس، معاون رئیس‌جمهور آمریکا، درباره ایمان، خانواده، سیاست داخلی، اسرائیل و توافق با ایران صحبت می‌کند.
یک ساعت درباره مسیحی زندگی کردن
حرف زدند
و ده دقیقه درباره نقش و نفوذ اسرائیل در سیاست آمریکا و توافق با ایران برای مخاطبی از اون نوع
اینجوری می‌پرسه: می‌خواهید یک مادر معمولی چه بداند؟
متن این دقایق:
https://telegra.ph/JDVance-06-19
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76524" target="_blank">📅 22:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76523">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp2Wvz0_Aw-l_AQJM0JLZO4AeTW1B863PIrOy7X-8GykTKfjK2RHOq2rW5b0HdrTQbHW1OD8eoGJJDxrWBzW71GSm-iHvgJ4aoWkcADczgP5jE6yWJ53k5h5ABlxkoctFqugsK22ZL0eD7xBwuHz27YlEWTLjgBeB1IfsrMe4IR4oF440vjRzX7vHXFfBFgMRArojWkMik5o_p_5T0mn5Afy0Y2iNjrOZeQNWHncoO75-VbDQ-GRHETOG6d64x3xYBU9IhVkKr4f5blIYPk0WL2de4HsaZCLJ4I5pHcfp95n70MwySboAlrIAYgBLXmaB4XS59e1oJWhaINXei7Cng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در یک گفت‌وگوی تلفنی با شبکه ان‌بی‌سی نیوز گفت که روز جمعه با مقام‌های اسرائیلی صحبت کرده و از آن‌ها خواسته است با گروه حزب‌الله بر سر آتش‌بس توافق کنند.
بر اساس مطلبی که خبرنگار این شبکه در شبکه ایکس منتشر کرد، ترامپ به این مقام‌ها گفته است: «بعضی وقت‌ها فقط باید آرام بگیرید و از عقلتان استفاده کنید.»
این خبرنگار همچنین افزود که ترامپ مشخص نکرد آیا مستقیماً با ‌بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفت‌وگو کرده است یا خیر.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/76523" target="_blank">📅 22:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76522">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ou7vOwrxZTy9jpaM5df5PbmD1IF83Vvn5TbYfq8ZQh5FBrI0L49qFPjQ3IGteCeuFM0Fo4N3F7JXzDxvMa_dXoZqrIWGCloCjJv6s8ECCKZdxBgedvXEfxuX7iiOwbGvFdMZBGIR5YSZytnDCNTOxAm_GLeQxjxMyZsWoR8kmBAX1rMZexMsMb0fHrGv7xU2XNYYbgqzbzP2XHH8t1YxlV-FckkwH8-ovEK9OJ8L3AQ9P-mOahUC4zEjyYDCuFmY-KvoFFXu4VmLANxpSUgZjbPHj5wA-tmTx2MpPEYWB9u-71ZRX1bApg5xJV5HkS-dfXqoV5P-zktltj8jEZUfyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نعیم قاسم، دبیرکل حزب‌الله لبنان، گفت: «تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
او تحویل سلاح‌های حزب‌الله را رد کرد و افزود این سلاح‌ها برای مقابله با اسرائیل هستند.
نعیم قاسم همچنین گفت که ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
دبیرکل حزب‌الله لبنان ادامه داد: «ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76522" target="_blank">📅 20:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76521">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cun6t3vs22LvNO4aOd80PtTomo-iSc2KYwLyJQOVs_XP65QdXEmnIWLNDwYHSoVFtlXE0_rXm_QXLc7nm-wPqHqhhSlttOqQ0YzR_LExwMyKDwu5qm5P-TJsqIf_k_VOWs8ZHTdVu9eMKXjMXPRBBMnB2P4vOsHqM1-D7OubLKJ5oRiKX-f2l-yT2x-dcqoEqHc2iXTL4mNGnMf23rM9SoO9bvyJ7quMXGjMZO2iD8RNyqGxSdU_DojEPGRsZSkpyoY0bcdStV0SN3FaMH3Btvpjcci1JQuUxm6Xita17RtovhGhqmJLE6n19jU-qjPxZwBQFGpycmKOjZJf0a3n5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت خارجه ایران، روز جمعه دعوت جمهوری اسلامی از بازرسان آژانس بین‌المللی انرژی اتمی برای حضور در ایران و انجام بازرسی از تاسیسات هسته‌ای را رد کرد.
او گفت: «بازرسی از تاسیساتی که دسترسی آژانس به آنها به‌دلیل حملات نظامی متوقف گردید، منوط به روند مذاکرات و نتیجه آن خواهد بود.»
پیشتر جی‌دی ونس، معاون رئیس جمهور آمریکا پس از اعلام توافق اخیر در گفت‌وگو با شبکه ان‌بی‌سی گفته بود که بر اساس تفاهم‌نامه میان واشینگتن و تهران، بازرسان آژانس بین‌المللی انرژی اتمی «قطعاً» به ایران بازخواهند گشت.
اسماعیل بقائی همچنین گفت در حال برنامه‌ریزی برای برگزاری یک نشست طی روزهای آینده هستیم.
نشست بین نمایندگان ایران و ایالات متحده که قرار بود جمعه در سوئیس برگزار شود، لغو شد.
سخنگوی وزارت خارجه جمهوری اسلامی اعلام کرد: «با توجه به اینکه امضای متن یادداشت تفاهم در بامداد ۲۸ خرداد به صورت دیجیتالی انجام شد، برگزاری نشست مزبور در سوئیس فوریت ندارد.»
او همچنین گزارش‌ها درباره بسته شدن تنگه هرمز را «بی‌اساس» دانست و گفت کشتیرانی در این مسیر در حال انجام است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76521" target="_blank">📅 18:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76520">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPo_JZvJ385RmQy42kNbPb_1X7h40u_BYOWHYdkqARB8ULnPX0LhnezdoSctzE8oOkFYVUhIhSw3f5TPb-991z_5aP4hXlDno5esjYrNc6ddmKydakjT55mEWNe_PkFsapZBrjT1jJQwfF64nLMk4PSCa2AzxFp7Krri1wLgCtcLOG0w2iZEX_XkAXCwZ-e6Qell0tyeBnrDIfq6StlXlLjc8x-kxTEUrap27O_fz-anfCDkCFUsHJVeXGzFupNLVMCT0QAIA6q526Gdb_j-rNs6jDNChHiZrsOih4rDbS1Whi1ftk0D3rnr2-2BiEryhAs97ipIgc4DX5gCJv3CwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی به رویترز گفت که اسرائیل و حزب‌الله بر سر یک آتش‌بس توافق کرده‌اند که قرار است از ساعت چهار بعدازظهر روز جمعه به وقت محلی آغاز شود.
این مقام که نخواست نامش فاش شود، افزود که مذاکره‌کنندگان آمریکایی و قطری با کمک ایران این توافق را نهایی کرده‌اند.
این مقام همچنین گفت: «درک ما این است که پس از تبادل آتش امروز، اسرائیل و حزب‌الله اکنون در وضعیت آتش‌بس قرار دارند.»
شبکه العربیه نیز به نقل از یک مقام آمریکایی از توافق برای برقراری آتش‌بس بین اسرائیل و حزب‌الله از جمعه خبر داد.
این در حالی است که نخست‌وزیر اسرائیل ساعتی پیش اعلام کرد نیروهای نظامی این کشور تا هر زمان که لازم باشد، در خاک لبنان باقی می‌مانند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76520" target="_blank">📅 17:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76518">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/teqBrAWzXDaByJpy4EsDGx8q2KKLtyA11Tl80_ICTmb9mJK4-jj5-awoS6y1dXTICnorQysOnkx7kGjn0JOijZjc4sbveMC8dxUauAbMAdysN6L1JrTyRhKPL-3Z7w4NHp8Fu6yWY8zSJt441PX_jwNArsqvAxMMOzq2tsmU5lVwsF0JEcGK9PXtAmEi7O2UGxMmsDV9YFNB1XC7vmmFWU2eU8CPM5ZTu00Ab1ZKo2-GV3ycUqoWCBZvaU8fCroSagouOqzyEAzbgkIqp2-CLHdK2VB5gIq15yzJ2LvTAjrRbNogU_t82HnVgeLYzMGKoOJ64U7GJqS3AuaLVUudQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957528437f.mp4?token=TQtZYBB_vzUiPdiLeEH0KOz3rbFKVi5fNOGG8kqwrgCPqUzTnPVv0tIok7LAbGJOUv-4ReiyDblFpfIrykjXGMkWzAzuje8-y4RsO9BIKeFdlGHZrxS7T4Fm08ArWQrs5gwWTMzJq6aVU1EkDU2wPqmzlx7DSAGFaKoTlbMWoeRPYijaw2rHU9QsKjaSalTvMgnYT06mlSw_1XmUiagd9A46CzS4e4d_SSCQFoSIsBCxPk-sW8Whw7X-uwa3y954y39xEd5_DrPQYvG8EL_FuA6rnpa6irh28dg7B7z6Ca_G3d45IV1IEJtx9f2wlTdZTgbH4_xgha0DOigxZHoLuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957528437f.mp4?token=TQtZYBB_vzUiPdiLeEH0KOz3rbFKVi5fNOGG8kqwrgCPqUzTnPVv0tIok7LAbGJOUv-4ReiyDblFpfIrykjXGMkWzAzuje8-y4RsO9BIKeFdlGHZrxS7T4Fm08ArWQrs5gwWTMzJq6aVU1EkDU2wPqmzlx7DSAGFaKoTlbMWoeRPYijaw2rHU9QsKjaSalTvMgnYT06mlSw_1XmUiagd9A46CzS4e4d_SSCQFoSIsBCxPk-sW8Whw7X-uwa3y954y39xEd5_DrPQYvG8EL_FuA6rnpa6irh28dg7B7z6Ca_G3d45IV1IEJtx9f2wlTdZTgbH4_xgha0DOigxZHoLuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امور خارجه ایتالیا روز جمعه اعلام کرد در واکنش به گزارش‌ها درباره اظهارات دونالد ترامپ سفر برنامه‌ریزی‌شده خود به ایالات متحده را لغو می‌کند.
آنتونیو تایانی در شبکه اکس نوشت: «سخنان شدیدا توهین‌آمیز رئیس‌جمهوری ترامپ… به همه مردم ایتالیا اهانت می‌کند.»
به گزارش شبکه ایتالیایی «لا۷» ترامپ درباره دیدار خود با ملونی در نشست گروه هفت گفته بود: «ملونی آن‌قدر می‌خواست با من عکس بگیرد که فقط از روی دلسوزی با او موافقت کردم.»
@
VahidOOnLine
جورجیا ملونی، نخست‌وزیر ایتالیا، در واکنش به اظهارات اخیر دونالد ترامپ، رئیس‌جمهوری آمریکا، این سخنان را «کاملاً ساختگی» خواند و گفت از نحوه رفتار او با متحدان «مبهوت و شگفت‌زده» شده است.
او تاکید کرد: «نمی‌دانم چرا رئیس‌جمهور ایالات متحده این‌گونه با متحدان خود رفتار می‌کند» و افزود این نخستین‌بار نیست که چنین مواضعی از سوی ترامپ مطرح می‌شود.
ملونی همچنین این رویکرد را «مایه تاسف» دانست و گفت او قاطعیتی را که در برابر دشمنان غرب نشان نمی‌دهد، در قبال برخی رهبران متحد خود به کار می‌گیرد.
نخست‌وزیر ایتالیا در پایان تأکید کرد: «یک چیز را باید به خاطر بسپارد؛ من و ایتالیا هرگز التماس نمی‌کنیم.»
در ادامه این تنش‌ها، آنتونیو تایانی، وزیر امور خارجه ایتالیا، نیز اعلام کرد سفر برنامه‌ریزی‌شده خود به آمریکا را لغو کرده و این اظهارات را «توهین به مردم ایتالیا» خواند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/76518" target="_blank">📅 17:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76517">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکمیته پیگیری وضعیت بازداشت‌شدگان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jo53hKa4UQVpTlxl-HO4mBSlLI6g6Y22vI-LCxdpo8VuhG9wQU5GQWIUdksZj-pJt0-9-OWL9gMJdec2qaarl0ivcUfCyuSXLZqKoZCM815ApFuzLiD3mLGSlqtxSxzlcSAxelL7iNTl_wMpZprgiqiWxMlxSu8AG91aByeclIRIa1N__4AVI_Q30vnSw6xHNt1GFm5g6Gylf1u77oiCFnYoI8je7c4Y8vkxgm-O-Q87tWLPKSUNx0gpRtjBMIPZvz4HDiLfC2u6Iv0QdkXrtnW3VqI1HAAZAMhh_lKNOK6A913xBm7fN5lgjHEOxJrZiJP5ygESGfbJPjMT9zbGgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅️
#محمد_نوروزی
، شهروند افغانستانی ساکن ایران، که در روز ۲۵ دی‌ماه ۱۴۰۴، در منزل مسکونی‌اش دستگیر شده بود، توسط دادگاه به شش‌سال زندان محکوم شد.
🔹️
طبق گزارش رسیده به کمیته پیگیری، محمد نوروزی پس از بازداشت به آگاهی ملارد منتقل شده و پس از ۴ روز همراه با ضرب‌وشتم فیزیکی به زندان قزلحصار منتقل شد. او طی این مدت مدام تهدید می‌شد که رد مرز شده و از ایران اخراج خواهد شد.
🔹️
او در نهایت با قرار وثیقه یک میلیارد تومانی از زندان آزاد شد و سپس توسط دادگاه به اتهام "اجتماع و تبانی و تبلیغ علیه نظام" به شش سال زندان محکوم شد.
این حکم هم‌اکنون در مرحله تجدیدنظر قرار دارد.
🆔️
@Followupiran</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/76517" target="_blank">📅 17:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76516">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJPIbYmT1Yhw900Kr2Yz3V-X28cyR0YayBdgvISwGswnrM6tScYE--Gt_9RD_uZ7qQkSCjjguGmXuU7K7_4MdK7jLq7i3GT97j4lVY6VDPF15fWkhHXt0VSw1MfzxoBqA7msFLKc0R6dBBoJCfPkTUp-YViwGEMIgTRROnaQ-c0JYbZ398TSGDYKTLNrNo05wkcOPRByEB0ed2ljh8AWGGpE-bEnJQLpbQ8wK-GOzvCmK1tY1cqCgatxG0IBcoCZS0IWuCo2m_BFOmQg2g5S2jKqIuOG75WDGkzxXRV50qIXRauw0TSz8qkFzmpp3pMFopo287lj1HkSJIylAgywsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز جمعه بار دیگر گفت که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در لبنان باقی خواهند ماند و وعده داد که حزب‌اللهِ مورد حمایت ایران برای حملاتش «بهای بسیار سنگینی» خواهد پرداخت.
او روز پنجشنبه، ساعاتی بعد از امضای تفاهم‌نامه پایان دادن به جنگ توسط ایران و آمریکا، نیز بر ادامه حضور ارتش اسرائیل در مناطقی از جنوب لبنان تأکید کرده بود.
نتانیاهو در بیانیه روز جمعه که پس از اعلام کشته شدن چهار سرباز اسرائیلی در لبنان از سوی ارتش منتشر شد، گفت: «اسرائیل حمله به سربازان یا قلمرو خود را تحمل نخواهد کرد و بابت این حملات بهای بسیار سنگینی از حزب‌الله خواهد گرفت.»
او افزود: «اسرائیل تا هر زمان که برای حفاظت از جوامع شمالی لازم باشد، در منطقه امنیتی جنوب لبنان باقی خواهد ماند.»
یسرائیل کاتز، وزیر دفاع، نیز گفته بود که ارتش در لبنان خواهد ماند و افزود که به هر حمله‌ای «با نیروی قابل توجه» پاسخ خواهد داد.
لبنان اعلام کرده بر اثر حملات اسرائیل در سراسر این کشور ۱۸ نفر کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/76516" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76515">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IT9DoZ0FHrLWeAG_o6pEenxtMzzC27E5zS_xlSEFGSsecvvjY0kiGVNMNcVz7COBeM439ezCI8mnRxeYwrxAG-yYqtGP-6mOaJDtM3YOh3iq-H_3RhtawhQiFnY_Xx6aS9pOPOuyeLU-iyN4QSUOn09n9L1cJ63ilnQo_uYPbQn1GfEcr8STmn_DyDJhG-XrHL26jq3nPSBG5Rq882movrwC_0aeeOsSA_w0_hS0t3XS05wRnCo2Hrj6EEc2Zq7B5cDFCgZf4ptzZ1mjN7BHal05e0-Zp_ozP3HalDa2RtqKO5_SocRhIRfSLB53FIg_EUiK-bj704R-Q7iFTS-PdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینعلی شهریاری، رییس کمیسیون بهداشت و درمان مجلس جمهوری اسلامی، در گفت‌وگو با دیده‌بان ایران، با اشاره به ادامه «تعطیلی مجلس» گفت: «مجلس را بستند تا هر آنچه خواستند امضا کنند.»
او با تاکید بر اینکه تفاهم‌نامه با آمریکا در نهایت باید به تصویب مجلس برسد، افزود: گذشت آن زمان که برجام را در ۲۰ دقیقه در مجلس تصویب کردند. ما یک بار از این موضوع آسیب دیده‌ایم و نباید دوباره همان اتفاق تکرار شود.
شهریاری همچنین از اظهارات عباس عراقچی، وزیر خارجه جمهوری اسلامی، درباره احتمال رقیق‌سازی اورانیوم غنی‌شده انتقاد کرد و گفت موضوع هسته‌ای نباید در مذاکرات مطرح شود، زیرا به گفته او «جزو خطوط قرمز» جمهوری اسلامی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/76515" target="_blank">📅 17:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76514">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a5NW7LDDkTqe6LtSuSVfUozE7p18G4LYnII8_BUPWNrDojaUfjGbMHquy9WyxXKGZkgOayXmgWy2yYmcXO28Pl1lj2xyonGgW57zDhHodtgs8Q_fTUnH5SZwA4npsCUiY_B7BdbHCxLMgWMt_vsZ-YrvBW4v8iOsor0Ng6YwFlUiOTcQkx5_hNzNQ60vQAyev6uRbJdSR4v7PpJ2cXzR9x9GGfQFqXVAMVK9SCxHI8TX_dpAhoQg4Jx_pQ4de_8Lj1D7tNI1y9ssahCcMjvZ8Ezp1Prd0Mn_wIHsoT981crA3sQ6G6bkfr_eITyWHr1YxFSOG4sxRNRmolq4ARNHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام پیشین مرتبط با تحریم های ایران درباره «صندوق ۳۰۰ میلیارد دلاری»: پیش نیازش لغو همه تحریم هاست که دکمه روشن و خاموش ندارد
میعاد ملکی، مدیر پیشین «دفتر هدف‌گذاری تحریم‌های خزانه‌داری آمریکا» در یادداشتی درباره موضوع «صندوق ۳۰۰ میلیارد دلاری» برای ایران که بسیاری از کارشناسان درباره آن ابراز تردید کرده‌اند، می‌نویسد: با کنار گذاشتن موضوع معافیت/مجوز نفتی و نگرانی‌های مربوط به عدم اعمال تحریم‌های جدید، باتوجه به الزامات برای اجرای واقعی بند ۶ (صندوق بازسازی ۳۰۰ میلیارد دلاری) و بند ۷ (لغو همه تحریم‌ها) به این نتیجه می‌رسیم که مذاکره‌کنندگان آمریکایی یا می‌دانستند که توافق نهایی ناممکن است، یا این یادداشت تفاهم فقط تصمیم‌گیری را به آینده موکول می‌کند.
ملکی که خود در طراحی تحریم‌ها علیه حکومت ایران نقش داشته در این یادداشت می‌نویسد: این چیزی است که «اجرای کامل» در عمل، فراتر از امتیازهای هسته‌ای، به آن نیاز دارد:
بند ۶ — صندوق ۳۰۰ میلیارد دلاری:
صدور معافیت ریاست‌جمهوری از تحریم‌های الزامی بخش ساخت‌وساز ایران طبق ماده ۱۲۴۵ قانون IFCA (معافیت‌های ۱۸۰ روزه قابل تمدید که در هر دوره نیازمند اطلاع‌رسانی به کنگره هستند).
خارج کردن سپاه از فهرست سازمان‌های تروریستی خارجی (FTO)، زیرا در غیر این صورت سرمایه‌گذاران با خطر مسئولیت کیفری به دلیل «حمایت مادی» مواجه خواهند بود و هیچ مجوزی این مشکل را برطرف نمی‌کند.
استفاده از معافیت مبتنی بر منافع ملی در قانون ISA (قانون تحریم های ایران) برای سرمایه‌گذاری در بخش انرژی و نفت.
در نتیجه، هیچ نهاد سرمایه‌گذاری حاضر نیست میلیاردها دلار سرمایه را بر پایه معافیت‌های شش‌ماهه قابل تمدید متعهد کند.
بند ۷ — لغو همه تحریم‌ها:
ماده ۱۰۴ قانون CISADA (قانون جامع تحریم‌ها، پاسخگویی و واگذاری سرمایه‌گذاری‌های مرتبط با ایران) رئیس‌جمهور اختیار معافیت ندارد؛ تحریم‌ها الزامی هستند و لغو آن‌ها مستلزم تصویب قانون جدید در کنگره است.
ماده ۱۲۴۵ قانون NDAA (قانون مجوز دفاع ملی آمریکا) معافیت‌های ۱۲۰ روزه قابل تمدید که در هر دوره نیازمند ارائه گزارش اجباری به کنگره هستند.
تعیین بخش مالی ایران به عنوان «نگرانی پول‌شویی» تحت ماده ۳۱۱ قانون پاتریوت: این موضوع نیازمند مقررات‌گذاری جداگانه از سوی شبکه مقابله با جرائم مالی وزارت خزانه‌داری آمریکا (FinCEN) است و صرفا از طریق دفتر کنترل دارایی‌های خارجی (OFAC) حل نمی‌شود.
تحریم‌های مرتبط با تروریسم، حقوق بشر و موارد همپوشان با پرونده روسیه: هر کدام مستلزم اقدامات حقوقی مستقل و جداگانه هستند.
ملکی در ادامه می‌نویسد: «لغو همه تحریم‌ها» یک دکمه روشن و خاموش نیست، بلکه پروژه‌ای چندساله در حوزه قانون‌گذاری و مقررات‌گذاری است و کنگره نیز در آن حق رای دارد. و این پرسش مطرح است که چگونه می‌توان اتحادیه اروپا را وادار کرد محدودیت‌های مرتبط با ایران را که در چارچوب پرونده‌های مربوط به روسیه وضع شده‌اند، لغو کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/76514" target="_blank">📅 17:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76513">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmDZJtFLeY3BPuN4LsZs57J2Fnelbreqsnrf2j5KsF0XpJ1Ik7ayeSHs8fazlBtjkzbY0vLVzcdZnNvkdXIMgaWyHq_7ek-6qckf6QO5knXdL_y9X0iekyYun-IYYuzPiQXp3cDcParC9O5OYvZYUrhyvOG7V0hIpAz0albi_fApS1AA96ZSjAcxOR5JGzfxI5D2hVeDHZAKTJ-0UrvpB8gJWney_f5uBLUVQCr9ON-DezQS7gK1PSph31creSM_rtvvXH6SMb32BNk4JXebtQaOh_IdndXnSuMZrS6j7I5e2BmaAJD6a7J0vWoBAa3o0b89vMWAHpxe4J0IGZeSLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه هاآرتص در تحلیلی نوشت توافق دونالد ترامپ با جمهوری اسلامی، برخلاف انتظار بنیامین نتانیاهو، نه‌تنها به تقویت موقعیت سیاسی او منجر نشد، بلکه شکاف بی‌سابقه‌ای میان واشینگتن و تل‌آویو ایجاد کرده و نخست‌وزیر اسرائیل را در آستانه انتخابات با بحرانی تازه روبه‌رو کرده است.
روزنامه هاآرتص در تحلیلی نوشت نتانیاهو امیدوار بود سفر ترامپ به اسرائیل و حمایت علنی رییس‌جمهوری آمریکا، مهم‌ترین برگ برنده او در انتخابات پیش‌رو باشد.
به نوشته این روزنامه، نتانیاهو انتظار داشت این سفر پس از «پیروزی کامل» بر جمهوری اسلامی، سقوط حکومت ایران و انتقال ذخایر اورانیوم غنی‌شده برگزار شود، اما اکنون نه‌تنها هیچ‌یک از این اهداف محقق نشده، بلکه ترامپ تقریباً هر روز با اظهاراتی تحقیرآمیز از نخست‌وزیر اسرائیل انتقاد می‌کند.
هاآرتص افزود توافق آمریکا و جمهوری اسلامی در اسرائیل به‌طور گسترده «فاجعه‌بار» تلقی می‌شود، زیرا ترامپ برخلاف وعده‌های اولیه خود، جنگ را بدون تحقق اهداف اعلام‌شده پایان داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/VahidOnline/76513" target="_blank">📅 17:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76512">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHc9dJNBuYb2Tg1FB3uVZ95phz4Z9qFCjCuoPRMqsqQgGAzYow2NwqdtXLJjAu9N7XwTOX8SKyZdUO15ze3UKqT2wwgt6l-4msZP2rbvmuCrdIE1n1WLLkd7XVNaxnZoBZgPVN2P-qHfdRJsc7QdgYq88kAiLMhN2Xdf11EaVuW35fmbGh_3uelR6-5lPDJ2-EfZpywtGBpyyQhSHvtLgfjaQZ99LftqFGk88PPE-FrkEl3nBhVUhiAKTKGtPVzJjHksma1UUfoYt6LkvNRJm-gtuXEjNJJYbpmT32pTn5YYt0bmxhNXq-O_CjuDiFoYrgy4MuCHRrtyy0SWF_wPdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«معین بصیری» ۲۱ ساله، ساکن شهرک اندیشه تهران، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ هدف شلیک مستقیم قرار گرفت و جان خود را از دست داد.
به گفته منابع آگاه، گلوله از نقطه‌ای مرتفع و از روی پشت‌بام شلیک شده و به قلب معین اصابت کرده است.
او در پی این جراحت جان باخت و پیکرش پس از انتقال به کهریزک، به بهشت زهرا منتقل شد.
نزدیکانش می‌گویند پیکر معین بصیری را از بهشت زهرا تحویل گرفتند و مراسم خاکسپاری او روز ۲۱ دی‌ماه برگزار شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/76512" target="_blank">📅 17:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76511">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t3ZOBOAKZGS2Xr_iZ1yEDr9GV2JBwqmW1f79_LcFQx1d7fcDv-auGs-NAB4qVwAA5Sb8EMm-4HxgVeeh4xYtWZxQJJEcnj1HiFXNT0B7S-n1bhuS4HyG9uPs6HGsBaIB_Pu3tvHHa8pqnG34t8UNBuGozNGYMxhkk-NaI4wD-wUGlxbl4kzjoES-BvyKv5XfhZp9jkmZXIztjfWJ3myfaFaUQG3sh7Ro30cnbnRO890hO42MmZoJIgD0Y4HnG8U3M-4XAt2BdGbQzB1Mh2Eb19GITdG_Nz-i6-qRs3sqBVNj_87C6tliDTN-UiHcJ2wU3oVVxckBhahoaETO2vl_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های ترامپ، ترجمه ماشین:
«جنگ، ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات ضدهوایی، نه رادار، و عملاً هیچ چیز دیگری هم ندارد؛ با این حال دموکرات‌های احمق می‌گویند ایران الان از چهار ماه پیش وضع بهتری دارد. اصلاً می‌توانید تصور کنید کسی با چنین حرفی قسر در برود؟ بعضی‌ها چقدر می‌توانند احمق باشند؟؟؟
رئیس‌جمهور، دی‌جی‌تی»
realDonaldTrump
«ما از سرِ درماندگی دیدار نکردیم؛ ایران بود که از سرِ درماندگی آمد. کارشان تمام است! این ۶۰ روز را هم طی می‌کنیم. هیچ پولی گیرشان نمی‌آید، حتی ده سنت!»
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 207K · <a href="https://t.me/VahidOnline/76511" target="_blank">📅 17:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76509">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N4vp1fid7PMcz4SxpJwqqLkSU_uokR_UhaC5AxI9tA1CVIoZzoCB-NvCf-feIWWif4OQxsX_Kkep06jVCkx63zWkN3DtrAgmSv3FTVdpiKN1-FzREag5HIA55Q0uNJ-70ajdNbpPFWK0ykfrG4_65NtQw45WOZ_d_gc7OeB3hFwdIlnbA5X-MkV-jquK_Z2SiT0XRjoCARip6J9igsEIRIzYP0VwawHkXBBWQU9ugJKu4qORSAAIKT6jJ9_0AZJZbBeZkYRc_Di79nUwV568RphEGEPxJeOkl1BJqblff6sqnfBvF1zG7C0ELDOAPR41bDkePkgzt7zROJK7SyYjCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A2C8szAcZOw-e4_27Hq8SudsVVhYW1081fBJKG9iexhOoun_c89q7Dj3OhfnFZttoP6f5fyb5wMqrsFp1snRh5gS-9r5mUOTfFuwIc7R58_jXkNCXfFcWcUWxcwoOVW6xU9oCAimJE-6plbuJcCzHHsb6x_aEcH8wcFnIej_jCBGhMhEK9A66-y2u3100YqgjnfK7243S1_gRzwTHuiJXqSYlP1CFtyzLKsKcBm69kTGgYsKmX5Rjk0ncEBtV5N0DEzvuclz_f19Ey4ScouUI3wMAD-E6aVIGB1VRV1v_FFlxQKH_ckHR4tMncTXdkGXJbL-z9gdlxjx6B74qyYtYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزیر خارجه فرانسه می‌گوید پاریس تا زمانی که اطمینان حاصل نکند مذاکرات درباره برنامه هسته‌ای تهران انتظاراتش را برآورده می‌کند، با لغو تحریم‌های شورای امنیت سازمان ملل متحد علیه ایران موافقت نخواهد کرد.
ژان نوئل بارو روز جمعه ۲۹ خرداد این موضوع را اعلام کرد. فرانسه یکی از اعضای دارای حق وتوی شورای امنیت سازمان ملل است.
بارو گفت تا زمانی که مذاکرات آمریکا با ایران به ابهامات مربوط به برنامه موشک‌های بالستیک جمهوری اسلامی و حمایت تهران از نیروهای نیابتی پاسخ ندهد، ثباتی در منطقه برقرار نخواهد شد.
او افزود: «ما به یک تغییر اساسی در رویکرد ایران نیاز داریم.»
@
VahidHeadline
وزیر خارجه فرانسه: کشتار معترضان دی‌ماه را فراموش نکنیم، مردم ایران بزرگ‌ترین قربانیان جنگ بودند
بارو که با تلویزیون «فرانس انفو» مصاحبه می‌کرد در پاسخ به پرسشی درباره سیاست فرانسه پس از «امضای تفاهم‌نامه پایان جنگ» ایران و آمریکا در قبال تهران گفت: «مردم ایران، بزرگ‌ترین قربانیان این جنگ بودند. آن‌ها از یک سو گرفتار سرکوبند و از سوی دیگر به رویشان بمب ریخته می‌شود. ما کشتار ژانویه (دی‌ماه) را که در آن خشونت دولتی بدون تمایز، معترضان مسالمت‌آمیز را هدف قرار داد، فراموش نمی‌کنیم.»
فرانسه حملات نظامی آمریکا و اسرائیل به جمهوری اسلامی را «غیرقانونی» توصیف و بارها اعلام کرد که در این جنگ شرکت نمی‌کند.
دونالد ترامپ تفاهم‌نامه پایان جنگ با ایران را در کاخ ورسای و در حضور امانوئل مکرون امضا کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 199K · <a href="https://t.me/VahidOnline/76509" target="_blank">📅 17:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76508">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biy4uFEvtBaStikVTLJVABZ3P066LdVAOgliTAHGMvseCc9OxMYEsYNDEXH79a294rBvNT1apniJfR1kuJ4i8HoLLQxIY_yXJbmcfa9_RJSO8iUS0ZDVo5WKmY0SeLUMG3M5ZYqV5OSg5G4DYLnzsO59nOLIrucuI_U2UkNoKWgoWNF6y75deynkK1ijTsrd8GKOGRBXVjk9pVDo06pe5Qwys_NBsFv3LzY9v0PUZZifTtNzFqD-ILzqGaUh5jfZX0_BI1OppmipxbStaG_oFtS0NwyyDGEH2ZONrkKBLHH3Rp85iW-_dvX3NvRJjzRFVOoeU8BlME5I_vn4nJytFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال از قول منابع آگاه گزارش داده که طبق توافق پایان جنگ، ایران حق دسترسی به شش میلیارد دلار منابع مسدود شده در قطر برای واردات اقلام انسان‌دوستانه و غیرتحریمی از خود آمریکا خواهد داشت.
به گفته یک دیپلمات آگاه از جزئیات توافق، این منابع مالی به‌صورت مرحله‌ای و در بازه زمانی آتش‌بس تمدیدشده ۶۰ روزه آزاد خواهد شد و تنها برای خرید کالاهای آمریکایی قابل استفاده خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/76508" target="_blank">📅 17:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76505">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sY9-WpY5626Zaltno60vkRz-1t5qGtko76qjkReDoe_XUh0atTYopw_q3z_OyxiX1mHahGaUQaEhDi_rpT9u6qTracQ4MN6spIML02xRfIX-gOWWiVzjnrx5xfg_TCpaT08GghPzjwKB33DaNZUqQVSchojPpyCxVHIU-ClW8wLtVG-cBuFKC0UfK6YRpUkfcVO7zj71I6woK7FmmLIBPRsAsV0n2_RP7TTHY10cC9rfP05-pw5vrrlU5E_MWO_dcSyuOZYRmr-4ya2B46Vs6c-PyGdwk44MYAqSVHhXW3kBKbqNj9bTXGE_Asl8NFdnqlhwdB_GXXOu5z6Kq-JuqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lDu_dRsRITmUPX5hVkx4iAFOCd_EZNmPVvXUAGS1QZ9w94j5BH_uG7HYkG-FVq7IJFMje9zhSXrzmbqjxi9c0P0YgCZx2iJxttdyP66swnN-L8_TFAXwv8iRIp4L9ztDVfzXBQs7U_fgKKdbDPxAE0jr06DAQOkihEYfUT1wAN_0xOVNfsn9_5tGywzLdPhxzn0STakFi62Q0Rl2r5b3oFSTgkmfJW0SVAJ57aTy3dwwGuz0GAjX29c_lJShDQHUEjnJPYnHay5asOD0hFk_gFX7jThOSHLHAR0vM-H-QEQUfRULF6TVZU-YzcIB591YmmNnjyPBt-SnmQfyA6-JjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tib39Vxrh98V_XAH98mASz0EZHHhmZUTIc8kaZiU25YPwAoDVfOTXToZAGRfOghrWHks50hTURMO4z-grvb8WKFM7XPI5l-cN-35B6TX4071rIkxPmvHqKr99lVokXLl74fTCJ5beO9P8pLegzWNCZnkR3AORKRmThc99CeWJkffilJPYrUnAsS2Na1CwPk7VZjg-rmcR_mXN6rLiUgHgVtcPE-2tpr6N0JEl4yrGQOSgCiFJQGls_9eTOxaNlxTjLZ8REcUHVVbzdK7a2pBEq7pcBsXq77MG90wOLaORu1q-ykB2Ra81DhRb5k-owLMLs7s8q1vI1Wts5hTvCi7_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
بيكر علی حسن‌پور را بعد از ۱۰۴ روز به خانواده
‏تحويل دادند
‏
🔸
⁧
#علی_حسن‌پور
⁩ در ۲۵ خرداد ۱۳۸۸ در خیابان آزادی تهران بر اثر اصابت گلوله به سر کشته شد. خانواده او پس از ۱۰۴ روز سرگردانی، سرانجام پیکر وی را میان اجساد مجهول‌الهویه پزشکی قانونی کهریزک شناسایی کردند.
🔸
اعتراضات خرداد ۱۳۸۸ که در اعتراض به نتایج انتخابات ریاست جمهوری سال ۱۳۸۸ شکل گرفت، جانباختگان زیادی برجای گذاشت، بنیاد برومند تا کنون ۱۳۸ نفر از این افراد را که مرتبط با این اعتراضات کشته، ناپدید یا اعدام شدند را در نقشه اعتراضات خود ثبت کرده است.
🔸
علی حسن پور یکی از این افراد است. سرگذشت کامل او را در یادبود امید بخوانید:
https://www.iranrights.org/fa/memorial/story/61687/ali-hassanpur
@IranRights</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/VahidOnline/76505" target="_blank">📅 17:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76504">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0JY66P_ptdwILmAGbAOtVKgUFldl0xMYmhdrknwj-0YWfarVwTndQDPFFdE84gAY__0_ITYAzPzOVo8sPRgvIs2exgyMml9DGSpqmXGKXffjWK-tPombyigyLhfNJ5cg1qSJ8OYRU-dJ936Ty9f3sx4mdXwqbWiTmBR44uz1hywu4qCT74kxrzl0HiAh5VsJkdjVMc9Q46atIn4oqaP_X-pRP5IztHG7WGK5obWZRDzC5GxOe9d-e9nZN7-FdgZGjkyR_6TpIckbGBZGcsWn3VWtg-76EaGFiB77sgwijyMf_uMp8h1QcyqYvH5LKJ-z8qOO9PDdzgBxdV3v9MBiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ملی لبنان می‌گوید در حملات اسرائیل به شهرک‌های شرقیه، حاروف، کفررمان، کفرجوزو کفرصیر در جنوب این کشور دست‌کم ۱۶ نفر کشته شده‌اند.
به گزارش رسانه‌های محلی لبنان، از ساعات اولیه بامداد امروز، حملات توپخانه‌ای ارتش اسرائیل به شهر نبطیه و مناطق اطراف آن ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/76504" target="_blank">📅 17:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76503">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTi-cWjzlRcZaPS-qvnLuspM9lKpcqGIktseVSWA0IXwCd04_x3ht6xcPppPUg5uaYiUPaTTCeOG7eKqcL2hp3RKOiYE6nHulVQ5LlFV96wx_YrD2E0rlxNyGDkcyFzrPEq0TD2z4BUtqLmLfMS-l6VxdYUrZLsTmjEy0mx0QBDI6Lys-fZMIRNFqcVnRuQ4ehuiX7WH_8BLiMoj_WS3VPwarimUc7COGflITCCfe28WRlloe-eowzZ2EfhHirTtjy7AwG9wqloWWjepoH50GLYP742iQFsRTjwqkIpn9_qmkrcn-4t9JlqGSlC93j2bcfrALYc4y0osz7twCYCNwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی اعلام کاخ سفید مبنی بر لغو سفر معاون دونالد ترامپ به سوئیس، وزارت خارجه این کشور اروپایی رسما خبر لغو سفر هیئت آمریکایی و لغو مذاکرات تهران و واشینگتن در روز جمعه را تأیید کرد.
لغو آغاز فوری مذاکرات بین دو کشور متخاصم تنها یک روز پس از امضا و رسمی شدن تفاهم‌نامه‌ای رخ می‌دهد که یکی از مهم‌ترین بندهای آن ۶۰ روز فرصت برای مذاکره درباره فعالیت هسته‌ای ایران است. قرار بود این ۶۰ روز بلافاصله در روز جمعه آغاز شود.
اما خبرگزاری تسنیم، نزدیک به سپاه پاسداران، روز پنج‌شنبه خبر داد که مذاکره‌کنندگان ایرانی پیش از آغاز دور بعدی گفت‌وگوهای صلح نیاز دارند نشانه‌هایی از اجرای توافق موقت از سوی آمریکا مشاهده کنند و هنوز تأییدی درباره سفر هیئت ایرانی به ژنو وجود ندارد.
در پی این انتشار این خبر بود که سخنگوی کاخ سفید هم در بیانیه‌ای که پنج‌شنبه شب منتشر شد، اعلام کرد ونس و هیئت آمریکایی آماده بودند به محض نهایی شدن برنامه مذاکرات، عازم شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/76503" target="_blank">📅 17:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76502">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b5H-7HK2rJdo-iHVdn8mhA-edN4YnW9mMkXx1tkStwnoW0RuovDMaOtdb9VXl8Mk5xZCJjMk0JRdDUvGAEXRJKEeegSpmTl3TlqtE0jkH5ou0PU1RHwCUSbU_xBz89OiPoBUE0t9lWaAb_sqvOyBuLQmZRVFSLAQCVB2yHWp2E43TwMob9UqnC9QrZtMhs679Gw_M777927pv2j72Ylwrojw0UbYlgK4jJK0vMDdx7hEMWfvqs6HKK59vLevNi6Z3zF74DWZk2ds1vb2fORQdPJR-gWemoQeEOo7qWQ9-p37xs4_yue6MG9iqfwfcIx16rFZgaLLffABFwcpAHqRyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود قنبری‌راد، متخصص امنیت شبکه و از کارکنان یکی از شرکت‌های تهران، با اتهاماتی از جمله «اجتماع و تبانی علیه امنیت ملی»، «جمع‌آوری اطلاعات طبقه‌بندی‌شده» و «ارائه اطلاعات به اسرائیل» روبه‌رو شده است.
بر اساس گزارش‌ها، محمود قنبری‌راد، شهروندی ۴۰ ساله و متأهل، اردیبهشت‌ماه سال جاری در منزل شخصی خود بازداشت شده است.
یک منبع مطلع به دویچه‌وله گفته بود که او هیچ سابقه فعالیت سیاسی یا مدنی نداشته و به‌عنوان متخصص امنیت شبکه مشغول به کار بوده است.
گزارش‌ها حاکی است که او در تماس تلفنی از زندان، پرونده خود را «ساختگی» توصیف کرده و گفته است که برای پذیرش اتهامات تحت فشار قرار دارد. همچنین اعلام شده که وی از زمان بازداشت تاکنون از دسترسی به وکیل محروم بوده است.
بر اساس اطلاعات منتشرشده، محمود قنبری‌راد ابتدا حدود یک ماه در زندان اوین نگهداری شده و سپس به زندان فشافویه منتقل شده است.
همچنین گفته شده که او از نوعی اختلال عصبی رنج می‌برد و خانواده‌اش نسبت به وضعیت جسمی و حقوقی او ابراز نگرانی کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76501">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u5mkdV9NPao0lEEXtH5KuQ8Ab16aM9khi2JCKNK1A0G1qyjFxk1QY1KxrqxRA60-gnkrszHc3BQl4Y2FLMnODuMKFw8xrbdAyFBqvUYGZD4L99_64E7rwwcKfPK2tvpqNEaIwYdxfCnlGtJ872eMgGeMUF2HgdQLmB1PD2U2xXfUSjPvdFFNfk3X6xuX3MrptycD5DDxs0c0I5bRfdILQdsgGCb3MUFaA7Y6aKW57ztKjWl_JIDybOWUjdDD719yFjmPm1mUEOGhm2OAdTKAhfKPSX2H1w8hEBUotMc5Jyjrv6ES7jwrMQKaaqwCeCoWrWSK7pHVqdGOv3gQfBg3Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تصویری از امضای تفاهم‌نامه میان واشنگتن و تهران  را
منتشر
کرد.
این تصویر مربوط به مراسم امضای تفاهم‌نامه در کاخ ورسای فرانسه است؛ جایی که ترامپ در حاشیه سفر خود به فرانسه و پس از پایان نشست سران گروه ۷ (G7) حضور داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76501" target="_blank">📅 05:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76500">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WH0xAfnt5SoJu6t5aHl9dUvpK6KjsmAw0_Esh0r48TszfCEnF0bH3zsnhnSVyJe-fvV9_yUEkOTAzWXytlXx8e3IRPfrfCzJkNEEpvc14BiFhpcfr8yzZ-wdpy0SBOjpxXoeelO7ZsBk72iSgSNb0c7L2mZUumHiVjFPriBywall1PlbQy2QQAxitk3PMY1DcQiZoZmBGplDIaIGF7bwO8juUE1vJmz4irSA4_8kOuCst4X7S5w3itkjecN6bsx8FUlAAVnbM5xeGr9oQE7q2f4g9vnEg0iTUUzPNEro5eE8_Uit68ndtfXwjFpyfvR3blLiw0c1vZYDoMdvMbTmlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در«گفتگو ی تصویری با اکسیوس» گفت یادداشت تفاهم امضاشده با حکومت ایران را می‌توان «نوعی تسلیم کامل» از سوی تهران دانست.
او این اظهارات را در پاسخ به پرسشی درباره تفاوت میان خواسته پیشین خود برای «تسلیم بی‌قیدوشرط» و مفاد تفاهم‌نامه مطرح کرد.
مجری آکسیوس در این مصاحبه به ترامپ یادآوری کرد که در آغاز درگیری‌ها گفته بود تنها «تسلیم بی‌قیدوشرط» را از ایران خواهد پذیرفت، اما یادداشت تفاهم امضاشده چنین تصویری را نشان نمی‌دهد. ترامپ در پاسخ گفت: «خب، احتمالا در واقع تسلیم بی‌قیدوشرط است. فکر می‌کنم همین‌طور باشد.»
رئیس‌جمهوری آمریکا همچنین با اشاره به جنگ اخیر گفت ایالات متحده ایران را «کاملا از نظر نظامی شکست داده است». او با تمجید از توان نظامی آمریکا افزود واشینگتن توانست محاصره دریایی موثری علیه ایران اعمال کند و هیچ کشتی‌ای نتوانست از آن عبور کند.
ترامپ همچنین گفت پس از جنگ با ایران، محدودیتی برای قدرت خود نمی‌بیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76500" target="_blank">📅 05:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76499">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HHOLLVSlwLLe-6Za59hYbdPR9PndzGer0CrjvOHGC8xvQseemmclTDOGtEOFNPeymeyuOxSuRIljjEMtsOQytZ5vskrwEIZcXnDLcMaBG2I92jB0MNUFoihhZWBqKOvC-mJemXOZj4ih9nDJK_TTkVzUKyt_HnDlHXMohsGRIqxRXHy9qdp998fEyac_QDtkpleAg7JI0tax2S1Mmmm1rKayiG9BAwfwAbyt4SCkDCDGkwSC478jjnIXNRNJOj3iTbhtfsrEpGD3Sh8JuUv1jyj3BssO3Zr2zo2ux25brPwDzd7H410q99iJVqEsMX-Yvy9mUf2u-8gl2rlcbSbTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر جی‌دی ونس، معاون ترامپ، در اطلاعیه‌ای اعلام کرد که او سفر خود به سوئیس برای شرکت در مذاکرات با جمهوری اسلامی را لغو کرد، زیرا برنامه‌های مربوط به گفت‌وگوهای فنی پیش رو هنوز نهایی نشده است و تدارکات و هماهنگی‌های این مذاکرات ساده یا قابل پیش‌بینی نیست.
در این اطلاعیه آمده است: «برنامه‌های مربوط به گفت‌وگوهای فنی پیش رو هنوز نهایی نشده است و هیات آمریکایی آماده بود در نخستین فرصت ممکن عازم شود، اما تدارکات و هماهنگی‌های این مذاکرات هرگز ساده یا قابل پیش‌بینی نبوده است. در حال حاضر، معاون رییس‌جمهوری امشب عازم سفر نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76499" target="_blank">📅 05:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76498">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cxjBgR2YitkVCJcFN-Cw5Rob4Ias5sKsU6N37HPiaBZAVRBmqur2Fcq9MKxMVysm5HnhIZVwEexYVflvS4fPeOWPeSYA_km7f_n5pE2OvLkg9jIPJob4eaQXODU2S1oJGFBU-uOjr1xOKUMSLj3eSvtC96u6xnO5hJGM_lktdy8qDqz_Z_6-DDvT3fnQwI9NW05WNvr45dzWPEprhvrLzndk-ubh8RvlhR8zv7MJrAhspwvuCfb9_TsaBIJX4aU1kFEi6v0gWRLJFi10KGU7bHKC_v_AtVFvfSVrcLxztbK_YSs2i88gfedXKVacMXWY0buwZwXIrtf_oiks7pXNHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری آسوشیتدپرس گزارش داد استیو ویتکاف، فرستاده دونالد ترامپ، پنجشنبه‌شب در نشستی غیرعلنی با قانون‌گذاران آمریکایی اعلام کرده است تهران از آژانس بین‌المللی انرژی اتمی برای بازرسی از تاسیسات هسته‌ای خود دعوت خواهد کرد و روند شناسایی محل نگهداری مواد غنی‌شده را آغاز می‌کند.
بر اساس این گزارش، ویتکاف به رهبران کنگره و اعضای کمیته‌های امنیت ملی گفته است تفاهم‌نامه میان آمریکا و ایران هیچ توافق جانبی نداشته است. با این حال، تهران و آژانس بین‌المللی انرژی اتمی نامه‌ای جداگانه تنظیم کرده‌اند که در آن دعوت از بازرسان آژانس و ادامه همکاری‌های نظارتی مطرح شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76498" target="_blank">📅 00:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76497">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7tH9idl3sy6Vmh0AvSmzV4quPE_U0-aQeZJAsSUhUJ5qRRzOSn2XhNlk5HdRp4lunhi0egoxYu97Y5x0oegiQB2XNaT0r8pHTdKLH6yoN2K-j10MSF3DdB8cWVaBNDXcmM7cbhgAAcAJ8B3bvIgrwXeuybeF2lRUX_nv6-u-t5LspSBtY4eItXqU3d44uulrVVv2gVRA8njzyXopsoK2rEV1WR5LCAUL9tqIl4NYDl2M_EUH4ivHpRODFGUb3-uky1XpuGqV6yCNcl5egmRaG-bx7_chIgt7z8it2g49OBWRiEDqg2QkY8zJGU8PqPCm_GgAJ0rDbsnv7qM5sGd2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کایا کالاس، مسئول سیاست خارجه اتحادیه اروپا، گفت هنوز برای بحث درباره لغو تحریم‌های اتحادیه اروپا علیه ایران زود است و این موضوع پس از دستیابی به یک توافق هسته‌ای با ایران بررسی خواهد شد.
او پیش از نشست رهبران کشورهای عضو اتحادیه اروپا به خبرنگاران گفت: «زمانی که شرایط فراهم شود، کشورهای عضو درباره مناسب بودن لغو تحریم‌ها گفت‌وگو خواهند کرد، اما هنوز به آن مرحله نرسیده‌ایم.»
اتحادیه اروپا در حال حاضر مجموعه‌ای از تحریم‌های چندجانبه علیه بیش از ۷۰۰ فرد و نهاد در ایران اعمال کرده است که شامل ممنوعیت سفر و مسدود شدن دارایی‌ها می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76497" target="_blank">📅 00:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76496">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpBErEp-SRdrIiDyWABmQwSMreerGZtDKp-6KGC8QU99PXQYZlJ6YAYNgLoFwkrE1trOpWfTSd5DEqZPWFhtGD0Mio3VnP2lhFMeTKYrh1ywORj_paC59tCmg2z9uHRtapx8Slc67ZoPsFRDVadxJzFnhuUsVMgM7PEuwtMHRjDqLAhyJop-VyZQtF0Z8JTqFIBDO8kodKYSYD_rdWMnl2lwtldabkmvc8HJYO_3g121_5HX5Wgs1byG0ntQWJuV0PX6qGyzsRpAZi9fKq5ZOcp1-zBsTWF1-Q_yF5bXK9lpTsPEz975OG_yKSRV4AN2YPEb1Jmz8TsC_eo8gRswGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المیادین به نقل از یک منبع آگاه گزارش داد هیات مذاکره‌کننده جمهوری اسلامی به دلیل ادامه حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس برای آغاز نخستین دور مذاکرات ۶۰ روزه را به حالت تعلیق درآورده است.
المیادین افزود: تهران پیش‌تر به آمریکا و میانجی‌ها اطلاع داده بود که پرونده لبنان در ادامه یا توقف مذاکرات نقشی محوری دارد و هشدار داده است حملات اسرائیل تا عمق ۱۰ کیلومتری خاک لبنان نقض یادداشت تفاهم و توافق چارچوب است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76496" target="_blank">📅 23:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76495">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hLOrHWqrObLfrsTRmTIa4nxgpD9dEpjR7KiBOGBreC6glTGzSxe1wCQ1IyTI8uZHd0tDfTaN4J-AHWj-7eu8tj7hHAHWXQE34klBqvmZh14bPad4bOcNnuhhUVs37E0boS9o5ogjq-KYOjXbrxki7LtMfzjdFY0WugYnRqbruQz1d3zzvUhIY7Bw9tu2bx6PNuQHg1t9jcc2J1qS41M_4Wh5yppY0l_onP08JcOBn3aCQxiQPPtv3ugPDGBjxTNDOPPdkvNICpxZD0otUJmDjv-h2yOoN5Pi-vLyoTEfF_4Kg-sZBe2_LXcamE4iFtp7hDCWqvujw7irLlLn0ARnsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت کاخ سفید:
رئیس‌جمهور دونالد ج. ترامپ تهدیدی را حل کرد که واشنگتن چهل سال صرف مدیریت آن کرده بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
یک پیروزی برای آمریکا.
🇺🇸
WhiteHouse
ترجمه با هوش مصنوعی به تصویر اضافه شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76495" target="_blank">📅 22:49 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
