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
<img src="https://cdn4.telesco.pe/file/LOmm47VkYr54Fv5EbfcjMyo2gps5sTghdTO5RHR9kdUOAneDgNFQpNfxfPAnX3Jdv3saBMTONFKAI46jOE42pzHAYaNkpe6MxqnJRsedTyz8wvdOcRH6vxigx9yJLBvHJB-Ix1zDo8bV196_dO3-Cok7WAeP8CJEmS6CCKEJ0UBGNjZGs2Waih6pLRmcQFfssaRWSvQ3-AGXSs1_nCxwZ-25W45zh92qnt28G9rSa66bN3i4RpjeOZmKiCu97Va1kska-3nCUvrt06yeMWHdyC1amusXvHNZp2WwQO8K_ztxYDMR3sTPTG7lt8UVXD4s8c--A02mvp4Q1IaLRIMKZg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.99M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 11:07:02</div>
<hr>

<div class="tg-post" id="msg-654126">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyaYdbyqYnJbG1AHi1RVXR4qutgBikAkluqjnlMju62gUL5iJVFSZ4a4Gede-rgKa6_8KEJ80WIwaiaVFfETTIufYJeqAMvfhYpGuRRPJg2Ti9xSJHXaT5eIaGoABAttmhI1vBTgMtr4qlPxQA8lNSDr4Rbp2Ju3sQg_HF23__6Zx8qz7kvGWSIkly0EHEp-GXiRk6AB0qf6Q2OOajINypbp8BquVeq__hNIORIdeaeFzJYxVjxn6ps07qedJIoB_9pEMkhpJdZ8vsVh8AFU53kXcYsNJr9atz6TcSeGAmVk7nmjL2Q3GnhPPWt99mJtllCPzyWNhBEfES5fiGBIAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشای دیدار رئیس شاباک با گزینه امارات برای اداره غزه
🔹
رسانه‌های اسرائیلی امروز از دیدار رئیس سازمان امنیت داخلی اسرائیل (شاباک) با محمد دحلان، چهره سابق جنبش فتح، در جریان سفر اخیر هیأت اسرائیلی به امارات خبر دادند.
🔹
رادیو عمومی اسرائیل «کان» با اعلام این خبر، گزارش داد که دحلان سال‌هاست در ابوظبی اقامت دارد و از او به‌عنوان مشاور «محمد بن زاید» رئیس امارات یاد می‌شود.
🔹
دیدار رئیس شاباک با محمد دحلان، نشانه‌ای مهم از تلاش اسرائیل و امارات برای بررسی گزینه‌های مطلوب این دو برای مدیریت غزه است، گزینه‌هایی که در آن امارات و اسرائیل برای حماس و تشکیلات خودگردان جایگاهی قائل نیستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10 · <a href="https://t.me/akhbarefori/654126" target="_blank">📅 11:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654125">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
سپاه: مقابل هرگونه نقض آتش‌بس پاسخ قاطع می‌دهیم
🔹
ارتش تروریستی آمریکا در ادامه ماجراجویی‌های مداخله گرایانه در منطقه و رفتارهای متجاوزانه، در منطقه خلیج فارس وارد حریم هوایی ایران شد و یگان های پدافندی سپاه پاسداران در راستای دفاع از حریم سرزمینی کشورمان پس از پایش های اطلاعاتی دقیق، یک فروند پهپاد MQ۹ را شناسایی و ساقط کرد.
🔹
همچنین با شلیک به یک فروند پهپاد RQ۴ و جنگنده متجاوز F۳۵ آنان را وادار به فرار و خروج از حریم سرزمینی کرد.
🔹
سپاه پاسداران نسبت به هرگونه نقض آتش بس از سوی ارتش متجاوز آمریکا هشدار داده و حق پاسخ متقابل را برای خود مشروع و قطعی می داند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 645 · <a href="https://t.me/akhbarefori/654125" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654124">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
طبق کسب اطلاع، ادعای شبکه سعودی العربیه درباره یادداشت تفاهم ۱۴ بندی ایران و آمریکا کذب و بی اساس است
🔹
العربیه ساعاتی پیش مدعی شد به متن پیش‌نویس نهایی یادداشت تفاهم مقدماتی بین ایران و آمریکا دست یافته که در آن موضوعاتی از جمله بازگشایی تنگه هرمز، آغاز مذاکرات درباره برنامه هسته‌ای ، نحوه آزادسازی پولهای بلوکه شده ایران و برخی موضوعات دیگر مطرح شده است که تمامی این موارد تکذیب می شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/akhbarefori/654124" target="_blank">📅 11:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654123">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7838afe4e0.mp4?token=lP7P-I2pa2uWMpTUQK-_pZn58nkylk_gw052jBcYB9c-chRw7ngvxmxyDteiHFxG2E1FRRxsWjsXmczjAHICemtpgLF2-rzOMVPwt8mn_h-nra9T8DtV_hYqmEH-XS7P7RmRnxUwds2qWSF4cby8I3pOBdXwauYjs42ystOHAp3YjydVkYLBz000t29Dd5qdKI3WLAh8_xaoaER3vc675O2tTHSdIP0qvqPoNxpTg0O-uYgubhEsJ5ylQvNF1Rd-acqlEJSafnl2BFhbATLUYoT13CfJna3cTcJ3EUqJOBvBEp9cufXVesYFGgSU5CihZ7qi2BvXVl3QSl5yw9Eq6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7838afe4e0.mp4?token=lP7P-I2pa2uWMpTUQK-_pZn58nkylk_gw052jBcYB9c-chRw7ngvxmxyDteiHFxG2E1FRRxsWjsXmczjAHICemtpgLF2-rzOMVPwt8mn_h-nra9T8DtV_hYqmEH-XS7P7RmRnxUwds2qWSF4cby8I3pOBdXwauYjs42ystOHAp3YjydVkYLBz000t29Dd5qdKI3WLAh8_xaoaER3vc675O2tTHSdIP0qvqPoNxpTg0O-uYgubhEsJ5ylQvNF1Rd-acqlEJSafnl2BFhbATLUYoT13CfJna3cTcJ3EUqJOBvBEp9cufXVesYFGgSU5CihZ7qi2BvXVl3QSl5yw9Eq6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت در پاسخ
🔹
دولت خود را مکلف می‌داند که بتواند مرتباً کالابرگ را به کسانی که واقعاً ذینفع هستند، پرداخت کند؛ لذا افزایش این رقم به‌صورت مشخص در حال بررسی است و ان‌شاءالله پس از نهایی شدن، اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/akhbarefori/654123" target="_blank">📅 11:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654121">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
‌رهبر انقلاب: امسال مسئلهٔ برائت از مشرکان اهمیتی مضاعف دارد و عمق و گسترهٔ برائت از آمریکا و رژیم صهیونی، فراتر از آیین برائت در موسم و میقات حج است و در نقاط مختلف ایران و جهان پس از این ایام مبارک، مرگ بر آمریکا و مرگ بر اسرائیل، شعار رایج امت اسلامی و مظلومان عالم خصوصاً جوانان خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/akhbarefori/654121" target="_blank">📅 10:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654120">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
‌ رهبر انقلاب: امت اسلامی و ملت‌های منطقه، ظرفیت‌ها و منافع مشترک زیادی دارند که نظم جدید و هندسهٔ آیندهٔ منطقه و جهان را شکل خواهد داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/akhbarefori/654120" target="_blank">📅 10:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654119">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJX-iXzWc8Gu8tzK-tvW90UuRe231nJp2oRf1d2XP-9NVs8DtH_TOPteONPtNNEtwuVw90H2TGASlNM4BMiQTdXzAWX7B22vAvvpFZZ_EyrSB_8WmVpgenl1WZVsxFUpd2p_JvZMZxZic7us_Hg4AuOZEAu2gh7syEMYMZyuA_aYh_ip30FKb-UAl6NY2jg90W4EQ4MDrVYY0Q7Jvtx2th_mI3-b90m6cXlyfyV0b-8iJVXLCUMQNoUy0yZ79mCkcMY2ZPiSJj3bxs5vT-KUd-lXY6pYRhyVfancRwZ-gqVU2uZbWQhTDtzLJ9unbOiPTTj8MS1Ik2nBWM-AlaOOgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کره شمالی چند موشک بالستیک شلیک کرد
🔹
ستاد مشترک ارتش کره جنوبی (JCS) اعلام کرد که «حوالی ساعت ۱۳:۰۰ روز ۲۶ می (۷:۳۰صبح به وقت تهران)، ارتش کره جنوبی پرتاب چندین موشک، از جمله موشک‌های بالستیک کوتاه‌برد، از منطقه چونجو در استان پیونگان شمالی (کره شمالی) به سمت دریای زرد را ثبت کرد.»
🔹
در بیانیه جدید کره جنوبی آمده است که ارتش کره جنوبی در واکنش به این پرتاب، سطح هشدار و آمادگی رزمی خود را افزایش داد تا برای پرتاب‌های احتمالی بعدی آماده باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/akhbarefori/654119" target="_blank">📅 10:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654118">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
‌ رهبر انقلاب: رژیم متزلزل صهیونی و غدهٔ سرطانی اسرائیل به مراحل پایانی عمر منحوس خود نزدیک شده و به فضل الهی و مطابق با سخن قاطع و آینده‌نگرِ ده سال قبل رهبر عظیم‌الشأن شهید قدس‌الله‌نفسه‌الزکیه، ۲۵ سال بعد از آن تاریخ را نخواهد دید، ان‌شاءالله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/akhbarefori/654118" target="_blank">📅 10:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654117">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrh8ULi8ioQb8u_HAEe-zyZNztrMRhV8fFcy_lWfcWD5bsiZtuyxhhSdcvBWtTvBbZ0EYxwfsDzNLbTDNo7qWTSoVM33uAeSNh2d0P_j0l6XXE1tHzUU1eLEVjQ80lkeR1Ym5mjYqpJ8_fV4TIzwd4EsFFUgNL3ONGrdu7YRjAKRkDFTqvnwIYBXfjNH65iTjwx5xOWPRKtc8kfR6GLihR2hXXw63dAW-PRh65wSf_k9dA7nl2EB6HzLR-QRDTTlMn94qTfcXyg9DoWkMWTsWKD7zx0N5BdqjrMFX_X1qC6uI58AOFauUmTj8EaWAw-zOL0DClKJnb4IMfyyAR8ytA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دولت‌های اسلامی را در راه پیشرفت امت و حل مسائل دنیای اسلام به دوستی و تعاون دعوت می‌کنم
🔹
بخشی از پیام رهبر انقلاب اسلامی به مناسبت برگزاری حج | ۵ خرداد ۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/akhbarefori/654117" target="_blank">📅 10:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654116">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
سرزمین‌های منطقه، دیگر سپر پایگاه‌های امریکایی نخواهند بود
🔹
اینجانب با صدق و خلوص، همه‌ی‌ کشورها و دولت‌های اسلامی را به دوستی و تعاون به خیر و نیکی دعوت می‌کنم تا با همکاری یکدیگر در راه پیشرفت امّت اسلامی و حلّ مسائل دنیای اسلام قدم برداریم. آنچه در این زمینه مسلّم است، عقربه‌ی زمان به عقب برنمی‌گردد و ملّت ها و سرزمین‌های منطقه، دیگر سپر پایگاه‌های امریکایی نخواهند بود. امریکا علاوه بر آنکه دیگر نقطه‌ی امنی برای شرارت و استقرار پایگاه نظامی در منطقه نخواهد داشت، روز به روز از وضع سابق خود فاصله می‌گیرد.
🔹
بخشی از پیام رهبر انقلاب اسلامی به مناسبت برگزاری حج | ۵ خرداد ۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/akhbarefori/654116" target="_blank">📅 10:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654115">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
رهبر انقلاب: آنچه مسلم است، عقربهٔ زمان به عقب برنمی‌گردد و ملت‌ها و سرزمین‌های منطقه، دیگر سپر پایگاه‌های آمریکایی نخواهند بود
🔹
آمریکا علاوه بر آنکه دیگر نقطهٔ امنی برای شرارت و استقرار پایگاه نظامی در منطقه نخواهد داشت، روز به روز از وضع سابق خود فاصله می‌گیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/akhbarefori/654115" target="_blank">📅 10:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654114">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98217d691c.mp4?token=bm5mePW0u6bd4snIhhy39UzEtiTld4M_NehGwL8_rStm9SHPVhJkChMVD83VmlUq9n4ypuNISu6D-nznFiM0aDw1t4cy5qfvy19BHKnmQWa1wgGiH90JIUGEcdi1D3gCofhwSPBOjw19qRi_3qLTvS2Kf5_LvWeM3O7tSZ0Sx0XAKfg3K-0SgyjikJnJH4WURD2Zt6gKtMKr0Sv_tGnm-oPk2vQKnHNt1m2zbP4Bm4XgmRpb8NTlkumIrCTxVHhdfZiKrSlYtDp3RcRsvSVqab3UQuEztxP0eOnthjBOUtUZQ_zlOZDbP9KzJHPxG2IZ3fXl1ft5ZdoV5rUz71bC5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98217d691c.mp4?token=bm5mePW0u6bd4snIhhy39UzEtiTld4M_NehGwL8_rStm9SHPVhJkChMVD83VmlUq9n4ypuNISu6D-nznFiM0aDw1t4cy5qfvy19BHKnmQWa1wgGiH90JIUGEcdi1D3gCofhwSPBOjw19qRi_3qLTvS2Kf5_LvWeM3O7tSZ0Sx0XAKfg3K-0SgyjikJnJH4WURD2Zt6gKtMKr0Sv_tGnm-oPk2vQKnHNt1m2zbP4Bm4XgmRpb8NTlkumIrCTxVHhdfZiKrSlYtDp3RcRsvSVqab3UQuEztxP0eOnthjBOUtUZQ_zlOZDbP9KzJHPxG2IZ3fXl1ft5ZdoV5rUz71bC5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیر آراسته: آمریکایی‌ها جایی در خلیج فارس نخواهند داشت
🔹
رئیس هیأت معارف جنگ شهید سپهبد علی‌ صیاد شیرازی گفت: نیرو‌های مسلح ما آمادگی خود را نشان دادند. بدون اجازه نیروی دریایی سپاه پاسداران انقلاب اسلامی کسی اجازه تردد در تنگه هرمز را ندارد و کشتی‌های خارجی هم بدون اجازه ایران تردد نخواهند کرد؛ همچنین قوانین تردد توسط ایران و عمان تدوین می‌شود.
🔹
دیپلمات‌ها هم پشت نیرو‌های مسلح برای پاکسازی منطقه از پایگاه‌های آمریکایی بایستند. آمریکا جایگاهی در خلیج فارس نخواهد داشت و چه جنگ بشود و چه نشود، این امر محقق خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/akhbarefori/654114" target="_blank">📅 10:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654113">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8dc0c560c.mp4?token=ewDcRVbCJTEQag7u8o25LlOjiAGYu9srM9uLLVanifB3z-P9CZ1Xs2cel-LNgXZsko-ONBQp0av-JeF7pFnDOvQa6rLRb6JFV-LDRyMBmcGT0ay1Iqt4QpzxxsiCuxRxf44DM8nhNS7mkUEkTMPiYR36agf9uqDhAM216nQyuvmRCoYZClI7RUPZpIn5dyPyeHl6TdCQhlz7Mnu5Pz0EKKuGxhY-48EMRopcSan6t6UEfdjhY1ngAuw2FdnfxKUVltEyTRhBFv9IQTFDzk05T3CI3GL5pyK99tovuuIIhs25hIkdfXDVhwCQuB77K9T6Wsp9uLW803TtPqeci32zmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8dc0c560c.mp4?token=ewDcRVbCJTEQag7u8o25LlOjiAGYu9srM9uLLVanifB3z-P9CZ1Xs2cel-LNgXZsko-ONBQp0av-JeF7pFnDOvQa6rLRb6JFV-LDRyMBmcGT0ay1Iqt4QpzxxsiCuxRxf44DM8nhNS7mkUEkTMPiYR36agf9uqDhAM216nQyuvmRCoYZClI7RUPZpIn5dyPyeHl6TdCQhlz7Mnu5Pz0EKKuGxhY-48EMRopcSan6t6UEfdjhY1ngAuw2FdnfxKUVltEyTRhBFv9IQTFDzk05T3CI3GL5pyK99tovuuIIhs25hIkdfXDVhwCQuB77K9T6Wsp9uLW803TtPqeci32zmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا بنزین گران می‌شود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/akhbarefori/654113" target="_blank">📅 10:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654112">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LH0zKIKdy7Wye3SbXK_YAQ8SbH3GQ_qD-RnbgYMJNELPUSfX30L_AbQw4RJ9hYFoz5QCI4E7nwHcDr6XkN046kqaaL598XBVWiC9oRMCuDMT3ctaLvMgw9ugvwvVGjPH8IfNr6kLhCAaWwJaSyYn2XeYAxxLBQWYfaCXbmjyxd1HWkkiktrvDHzm-O4OPl4slVZhbYVOwkbAoipkq8eqCAqZc9qQCWprm8sf-k1tcD9GcQp1g_UBEPcMGI4GvwXu_HFaHbujFposj12eAgqhAybDq_VqE4P7SqszDjSwSs6_C4MgH7-21Qb_8NJwm6d0-DzLNrugu1mVaUP60t_-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سلاح دشمن‌شکنِ الله اکبر
🔹
با سلاح الله اکبر بود که ملّت مسلمان ایران در چهل و هفت سال قبل قیام کرد، رژیم طاغوت، دیکتاتور و وابسته‌ی پهلوی را ساقط کرد، دست و پای امریکای طمع‌کار و مستکبر را از کشور بُرید و نفوذ صهیونیسم را بکلّی قطع کرد. با همین سلاح الله اکبر بود که پس از تجاوز رژیم بعث صدّامی به خاک ایران، مجاهدان غیور و جوانان از خود گذشته، حماسه‌ی هشت سال دفاع مقدس را رقم زدند... و این ایستادگی را تا سالها بعد در برابر محاصره‌های اقتصادی، کودتا، تحریم‌های ظالمانه، حملات بی‌شمار سیاسی و تبلیغاتی و اقتصادی دشمنان علیه جمهوری اسلامی، محکم و استوار ادامه دادند.
🔹
بخشی از پیام رهبر انقلاب اسلامی به مناسبت برگزاری حج | ۵ خرداد ۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/akhbarefori/654112" target="_blank">📅 10:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654111">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJjsh5CeaK81YRvPnIVRPoifD-gVP1yU2t3mHBmXHi7X9b8TWvC0x484F0zCmxZOCOz9TA_jk51HGSl0po_-Blg_oh4Nxz8Hz46gmcQOoFxlGDpioRLV6E1rWZYOK_keY0Hy0aYjt_uVGbMGiTSowBhnU7-bL1dCkhOIt3H0EMZah0txIi3PpyIudG34KVyPAeMZvxVTCnRwEIJKdixsflWDDYslIND2TdzvPYaMPbWrYSFx9u16QNb0ADc2IFE0rKT5d131z9qQSVi1xK5eq88vS5FbXAk6mvD1uAsHLQFFD5GZxNKGJdV97BbHt9SVSBGBClwLrg2eIEP0whBMvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر معظم انقلاب در پیام خود به حجاج بیت‌الله الحرام تأکید کردند
🔹
آمریکایی ها بدانند: زمان به عقب برنخواهند گشت
🔹
حضرت آیت الله سید مجتبی حسینی خامنه‌ای رهبر معظم انقلاب اسلامی در پیامی به مناسبت فرارسیدن موسم حج ابراهیمی، اَعمال و اَذکار پر رمز و راز حج را نشانه‌هایی برای همیشه‌ی بشریت جهت هجرت به سمت خداوند تعالی و رهایی از قید و بند شیطان و اذنابش و سعی و تلاش بیوقفه برای عمل به تکالیف الهی و رهایی از هواهای نفس و سعادت‌مندی دنیوی و اخروی برشمردند و با اشاره به تکیه ملت بزرگ ایران بر این نشانه ها بویژه سلاح «الله اکبر» از دوران نهضت اسلامی و پیروزی انقلاب و دوران دفاع مقدس تا جنگ تحمیلی دوم و جنگ تحمیلی سوم و ناکام گذاشتن دشمنان برای تسلیم ایران و واقعه اعجاب انگیز بعثت الهی مردم، تاکید کردند: امسال مسأله برائت از مشرکان اهمیت مضاعفی دارد و عمق و گستره برائت از آمریکا و رژیم صهیونی فراتر از آئین برائت در موسم حج است و از این پس «مرگ بر آمریکا» و «مرگ بر اسرائیل» شعار رایج امت اسلامی و مظلومان عالم خصوصا جوانان خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/akhbarefori/654111" target="_blank">📅 10:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654110">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">459345494016_1779778963692.pdf</div>
  <div class="tg-doc-extra">415.4 KB</div>
</div>
<a href="https://t.me/akhbarefori/654110" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای، رهبر معظم انقلاب به‌مناسبت برگزاری حج منتشر شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/akhbarefori/654110" target="_blank">📅 10:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654109">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVvG0knGtfS39mU6qjb-Sje9uQJrZDYJZ20D6hDDi193j4GQDisDO3VdoqfX3wNkVKKrMqOu1pRAIX52ymNpp0SOwwHafwZBcCcJgcF6leeZqejMBHnTSdqeBSAuUktIQoct7vNs9dVIVQKHF0LKRaSghUVpj_7UQyYoh0ZmZNII6KRUl04Z4N97MuBa_ku8jwbm8ZnsI7NhnPH-CbVu6hJq4J-GUjB4aAVmUtDye_gHt9q55S_y40wzCCigbTbBElTShBRB4D9Yq5Pylakqeuw3alWPcwyI6huxgA0t96WKlO0PfF7VKRkUysp4FtXKbDLOvdu1SbeiNkAuXrzgew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسکو: غرب تروریست‌های سوری را به جنگ ایران می‌آورد
🔹
رئیس سرویس امنیت فدرال روسیه (FSB) اعلام کرد که سرویس‌های اطلاعاتی غرب به تلاش‌های خود برای استفاده از جنگجویان تروریست سوری به‌عنوان نیروی نیابتی در جنگ با ایران ادامه می‌دهند.
🔹
طبق گزارش، به گفته الکساندر بورتنیکوف در پنجاه و هشتمین نشست شورای رؤسای نهادهای امنیتی و سرویس‌های اطلاعاتی کشورهای مستقل مشترک‌المنافع (CIS)، غرب در نظر دارد این نیروها شامل افرادی از کشورهای مستقل مشترک‌المنافع باشند که در گروه تروریستی داعش و سایر گروه‌های تروریستی جنگیده‌اند و اکنون در زندان‌های سوریه به سر می‌برند.
🔹
بورتنیکوف تصریح کرد که این شبه‌نظامیان در حال حاضر به اردوگاه‌های ویژه‌ای در عراق منتقل می‌شوند. او تأکید کرد که بدیهی است چنین نیروهای عاملی می‌توانند و خواهند توانست نه‌تنها در غرب آسیا، بلکه در کشورهایی که از آن آمده‌اند نیز به کار گرفته شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/akhbarefori/654109" target="_blank">📅 10:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654108">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83b1739b88.mp4?token=q_2LPRBrmwYiGJJekvUXWJiroGt6pI52D0YcJ8rC2RN5DZMuoatAwuaNb5uR48kLOgD1tVm8GNZQUkvNelO8alD7X8PQllbUuxVBCkdzCx-dTD7W7PuvGmNEqez2YtMztYs_3Or995pUxBUM3Afrp1ZJG5eV1AUaEqT0UjCX5vvxUQXVe0yOJ49t6R85BIAoVamFsnXnlmqJEs1mrT4HIj7B8qaBy0pysKkLsJpOk132QUVkskkv_N4PSNkIAgIS9JoWHUe78JmaMYVhZQg1IErwLeUe_c4SD7ZUtU_eerFahYdPxLwas4jGzCOgjoGPNm8cJJ1q-9u87qZsQjrizw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83b1739b88.mp4?token=q_2LPRBrmwYiGJJekvUXWJiroGt6pI52D0YcJ8rC2RN5DZMuoatAwuaNb5uR48kLOgD1tVm8GNZQUkvNelO8alD7X8PQllbUuxVBCkdzCx-dTD7W7PuvGmNEqez2YtMztYs_3Or995pUxBUM3Afrp1ZJG5eV1AUaEqT0UjCX5vvxUQXVe0yOJ49t6R85BIAoVamFsnXnlmqJEs1mrT4HIj7B8qaBy0pysKkLsJpOk132QUVkskkv_N4PSNkIAgIS9JoWHUe78JmaMYVhZQg1IErwLeUe_c4SD7ZUtU_eerFahYdPxLwas4jGzCOgjoGPNm8cJJ1q-9u87qZsQjrizw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«نبض ماندگار» از مرز ۱۰ هزار نفر گذشت
🔹
تا این لحظه، ۱۰ هزار نفر از طریق پویش
«نبض ماندگار» خبرفوری، برای دریافت کارت اهدای عضو ثبت‌نام کرده‌اند.
🔹
در سال جاری، بیش از نیمی از ثبت‌ کارت‌‌های اهدای عضو کشور، از طریق پویش «نبض ماندگار» خبرفوری به ثبت رسیده است.
🔹
به پویش «نبض ماندگار» بپیوندید:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید
یا از طریق لینک زیر ثبت‌نام کنید:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از دریافت کارت، تصویر آن را برای ما ارسال کنید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/akhbarefori/654108" target="_blank">📅 10:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654107">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
کابینه امنیتی رژیم صهیونیستی امروز تشکیل می‌شود
🔹
کانال ۱۳ رژیم صهیونیستی گزارش داد که کابینه امنیتی رژیم صهیونیستی عصر امروز در ساعت ۱۹:۰۰ به وقت محلی تشکیل می‌شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/akhbarefori/654107" target="_blank">📅 10:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654106">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de5a1a73a.mp4?token=iuMlE_8HkLg6UeUoSaIezbJ1JcqwNjzLVQX5wd1crs6uxECbs8aoNU6kTHMpDODGoNaoSMC7m9Bi8m1Z6Z8_qxBMPUOobzU4ygeS5_wSsJJaBZCTTeaWW1KjoMiz1uqj3RE_UhWGQDEOf5kaAIk_OMcTOutzT-lOHDmhxEYi6ZASrmYrFxJEk1FeE4EEICQ1bZvRyJ5lGBXKOBweonfZeQTtsUorQZOJBWMfodG2vDGFYotw8zF1ufw9V0WC3L5kO1uZX7S6DoCX6j2gbv95Rau-BloJ1Fw5aNrJwSRTy9TNvwKYuN8cNnHPmhL86lrs_0T0ReY4jscsLcC2SqsljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de5a1a73a.mp4?token=iuMlE_8HkLg6UeUoSaIezbJ1JcqwNjzLVQX5wd1crs6uxECbs8aoNU6kTHMpDODGoNaoSMC7m9Bi8m1Z6Z8_qxBMPUOobzU4ygeS5_wSsJJaBZCTTeaWW1KjoMiz1uqj3RE_UhWGQDEOf5kaAIk_OMcTOutzT-lOHDmhxEYi6ZASrmYrFxJEk1FeE4EEICQ1bZvRyJ5lGBXKOBweonfZeQTtsUorQZOJBWMfodG2vDGFYotw8zF1ufw9V0WC3L5kO1uZX7S6DoCX6j2gbv95Rau-BloJ1Fw5aNrJwSRTy9TNvwKYuN8cNnHPmhL86lrs_0T0ReY4jscsLcC2SqsljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلترینگ دودش رفته تو چشم فعالان فناوری
امین شریفی، مدیرعامل پیام‌رسان سروش‌پلاس:
🔹
با وجود سه راند فیلترینگ در سال ۴۰۳، طبق آمار مراکز افکارسنجی، تا قبل از جنگ رمضان ۳۰ تا ۴۰ میلیون کاربر فعال در اینستاگرام و تلگرام داشتیم. اما حقیقتش بی‌توجهی و بی‌تصمیمی مدیریتی باعث شده دود این وضعیت برود توی چشم کسانی که در این صنعت فعالیت می‌کنند. مردم اشتباه فکر می‌کنند که ما عامل فیلترینگ هستیم، در حالی که بارها در نامه‌ها و مصاحبه‌ها به این مدل تنظیم‌گری اعتراض کردیم. سوال اصلی این است: استراتژی جذب کاربر باید حذف رقبا باشد یا ارائه یک ارزش پیشنهادی واقعی تا مخاطب خودش انتخاب کند؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/akhbarefori/654106" target="_blank">📅 09:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654105">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
اعمال محرومیت های چک برگشتی از ۹ خرداد
🔹
بانک مرکزی: محرومیت های تعلیق شده برای چک برگشتی ناشی از شرایط حادث شده در کشور با پایان شرایط اضطرار، از ۹ خرداد اعمال می شود و برای صادرکنندگان چک برگشتی، علاوه بر مسدودی حساب به میزان کسری مبلغ چک، پس از این تاریخ امکان افتتاح حساب و صدور کارت بانکی جدید، اعطای تسهیلات و تعهدات، صدور ضمانت نامه و اعتبار اسنادی و صدور دسته چک و یا ثبت چک جدید وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/akhbarefori/654105" target="_blank">📅 09:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654104">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hb9-EReJA_v9hUWgWBScCgTxOPscom55IO0PGS66Rfj3c9xRfHpoaW5Yey1KN0whptVKxXj42TwmE9SC5xyWyNwdNLJ6moshNREbpEqJE2Jih3GuJGiYjaHEP8JfrApWv_fCNgm-igfFOw4w4V-C0IzBp3gTUZHU-4RIwPgZFb-joCW44YuQVB3OYm-rE0oaaszT13HJwyCLbRrUM-XZDoW-sZ17pYgVh3a3oq-XMkW0KQJwxxkSYQUe1-Exl07mcCPZ5AOWeuZXWgCtSwGfJOsgRQkhVdSNE2gNj8B1KfbYWIiAzdCHN3ZuapoQWf2j47UtQHKsBPKPQYbVJCK5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توافق ایران و آمریکا در صورت انجام، نصفِ راه است، راهی که باید به سرمایه اجتماعی، بهبود فضای اقتصادی، نفوذ هوشمند در نظم جدید بین‌المللی، حفظ توان کشور و امید به آینده ختم شود وگرنه این راه اشتباه است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/654104" target="_blank">📅 09:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654103">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0gjqsiJ6DyT1i6d229D2lCoM8sWylAynvFE4CwIpQOmG6DMn98694dgWcgJY-j-EAlv4JcpDEwL8ysF9zvgplOK_OY3xLwJrH7d8e_5CuFDQ-rHFUoOX4UtNlJDZ4tdZbbPgF2sq84bQLak2n5ozWpl3BYyqbnHVlXfUOgww2LppZi1myTEYVoZ_-pbLGbqZhhbiE0A6D9gHi8i-zNDDznMOIh47lOkSY96_N0jdUiFhyYNG4UMMzIVU7TWcOF1y4hHvPI_Kiu6W_MzS66EHJrvu_r1tZS6PrcDrF_fX8uz1Kt-qkyW8QXwO3evupYzCvx5gIfP2aLxVn5T-5avmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعمال محدودیت در شهرک‌های اسرائیلی از بیم حملات حزب‌الله
🔹
به دلیل ترس از حملات حزب‌الله، محدودیت‌هایی از سوی فرماندهی جبهه داخلی رژیم صهیونیستی بر ۴۳ شهرک شمال اراضی اشغالی إعمال شد.
🔹
در راستای آمادگی برای پاسخ متقابل حزب‌الله و بنا بر دستورات فرماندهی جبهه داخلی، حمل‌ونقل در خط مقدم و منطقه میرون لغو شد و کریات شمونه و سایر شهرک‌ها پس از نیمه‌شب، اعمال سیستم آموزش از راه دور را اعلام کردند. همچنین محدودیت‌های مربوط به تجمعات تشدید خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/akhbarefori/654103" target="_blank">📅 09:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654102">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c9c3a7d3e.mp4?token=eLuWtZ2dL9MDpmL9OmPnsk3kDm5qgRaqUhpv8uuZG2Am-1dOomoo5VOomnpc0mayKGr4b5pjnfeE35RbA5C9Acqn-R9r4BWZPzCM6jxneZqrbiv5Y2_eNXb-I5fHngj47PDoD4YsEEOM6iHxM3efAJDPPKHeWOwiOYeZ7xolQgckVQJlLPTx9G5_LJPRiqN8K-5f7a_QzNxTWR5zu6xMdb2YIOhQH9g4kZA7uZjwHkzWWaaV2VGvk8RC8q1jHeqCbXzMNdGlDa6SnGl6M2qdDF9rMniVbUNVRAVfLkZ7MSLgMGvBWDufS-ZMQPAhpYrGVk9p3EktXxxpDYtVkCwdqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c9c3a7d3e.mp4?token=eLuWtZ2dL9MDpmL9OmPnsk3kDm5qgRaqUhpv8uuZG2Am-1dOomoo5VOomnpc0mayKGr4b5pjnfeE35RbA5C9Acqn-R9r4BWZPzCM6jxneZqrbiv5Y2_eNXb-I5fHngj47PDoD4YsEEOM6iHxM3efAJDPPKHeWOwiOYeZ7xolQgckVQJlLPTx9G5_LJPRiqN8K-5f7a_QzNxTWR5zu6xMdb2YIOhQH9g4kZA7uZjwHkzWWaaV2VGvk8RC8q1jHeqCbXzMNdGlDa6SnGl6M2qdDF9rMniVbUNVRAVfLkZ7MSLgMGvBWDufS-ZMQPAhpYrGVk9p3EktXxxpDYtVkCwdqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون رئیس جمهور: اگر نیروهای مسلح ما آن روز صبح آن پاسخ کوبنده را در LNG قطر نداده بودند، دشمن بقیه انرژی و زیرساخت ما را هم می‌زد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/akhbarefori/654102" target="_blank">📅 09:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654101">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMBGqdto3odF029TvjrVHAcip5tWFkybSe93HckguXxtNw75BGHRldDSifptiLZrBspRv-yGsEtif6JcBB9QhkOG08MoKEJtMGVaftURZbTjRD_ULtShPRI2m6C3FSyAaZPIt6vXWCeGmUyfr11M2TNg4Jyhe-9sqhIqA35841WdRhrav5uIEtH9XKoIn2B5KiVmHIcP-x9HEli1Dk4NDDVUrMRj41PPWsILrTGt67HBkSX54v-DjlidCBOJvMoXYUso0jBKg00diHtpc6nIubM8J9dMEkHt8GtX5QXu331o9j-rNy2Og_mI6T0eltGqEMDWrkc8JsJYr3NhXw4rBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیچ آتش‌بسی در غزه وجود ندارد
🔹
ویدئویی امروز منتشر شده که یک مرد فلسطینی بر پیکر دختر ۶ ساله خود گریه می کند. او در حمله اسرائیل به یک چادر آوارگان کشته شد. آتش بسی وجود ندارد. هرگز در غزه آتش بس برقرار نشد. و صهیونیست‌ها هرگز از سلاخی کودکان غزه دست برنداشته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/akhbarefori/654101" target="_blank">📅 09:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654100">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c740b029de.mp4?token=tgPtfvLWqh70imGNMkASw0kV-nNKv_DzyA7NNEfTweKeTs5edGgr9Pfwn0TSOspmKQR131P5jQ-sAZCTIgHTtsciJcWbrpISzhEPHTDxB_HrXNQmAPcd00IM3HtVzmJD6LU6FqaD_yxUyvSFroOvHuANKKN-mLxjlfXfFYHyWqhfmISDW496NViytFbjiY8E_s43FrN8P8C7WSR9HyQTsUhQKDjjXfgRAIsTDgYMmWCNMtiipBSRG4A2YeYDggTM4SnJ2oOFp88OdZWkYato9LKQK4LGtzZYzXELz0GdfXNYsGYLgjfncQ4o7Ck6EE1U_LH5dou1zZLrVl1Gw_rUog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c740b029de.mp4?token=tgPtfvLWqh70imGNMkASw0kV-nNKv_DzyA7NNEfTweKeTs5edGgr9Pfwn0TSOspmKQR131P5jQ-sAZCTIgHTtsciJcWbrpISzhEPHTDxB_HrXNQmAPcd00IM3HtVzmJD6LU6FqaD_yxUyvSFroOvHuANKKN-mLxjlfXfFYHyWqhfmISDW496NViytFbjiY8E_s43FrN8P8C7WSR9HyQTsUhQKDjjXfgRAIsTDgYMmWCNMtiipBSRG4A2YeYDggTM4SnJ2oOFp88OdZWkYato9LKQK4LGtzZYzXELz0GdfXNYsGYLgjfncQ4o7Ck6EE1U_LH5dou1zZLrVl1Gw_rUog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ صریح معاون رئیس جمهور به میزان خسارت به بخش انرژِی و زیرساخت در جنگ رمضان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/akhbarefori/654100" target="_blank">📅 09:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654099">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T2bBN3vTG_pTXyBSD5aYeR_C9yo4467PjIw_8imkCAIA2NAzZiTc2_wMe1HriICycKPd-E8lOOxS62rHudb9aQ439O-dAFTREIIH8pUUXq8fMErg-bwE12DQHAa6yRA2DcNAiJVKzaIebG7yO8Zq64Fwp6YHZLLUBURmoUWJeZXojyznmjIhKo7Lesv1JhUB_YqpStEc6PAxWzGXQOqu3mswgkHstf_KwcDLdm6jmCpPM6HG6EA7nhh3Q5IhwLuEAh_WUfQgwwOWc6EYS4qb0t-tqrCSaYNGXAkr_sigSi4zzBvPu8Bf80Jc3rV6rs7S1oGwWsRmNPZZpZSFqkdEbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
تا دقایقی دیگر پیام رهبر انقلاب اسلامی به مناسبت برگزاری حج منتشر خواهد شد.
#سلاح_الله_اکبر
📲
@rahbar_enghelab_ir</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/akhbarefori/654099" target="_blank">📅 09:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654098">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
سردار شکارچی: اگر از صادرات ایران جلوگیری شود، جمهوری اسلامی ایران از خروج نفت از منطقه جلوگیری خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/akhbarefori/654098" target="_blank">📅 09:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654097">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5elqmWbz-OgPwviRtrwqIyXeuyhSah5iHmGYuhKS6e_C02R1Z55uyS3oCi7QE1aldW7RKTLgowLaCgWaLNVwXINXLbcvAYPyiwU6GP4Nuo6_xDLttmJIikzBURB2SstRiSgcyWYKwf_JbaTSCavhVuFISXDSjQ2SG9sZM5s6-0AMbITcVptKMdux4jg4_8WOObyWfFiCiy3FnaFPaMO6dkAdg2iVXIEDk9g5wdQe7FxOYbonljYB3y6Bvkkk2zwI_0xRxqLvHnbTAv6085m_S9eXa9dzByv5Nu1NCWR42O8FlrtvwkQQRUJWflfacDgUp_KKZewlSjX50njoX9_SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از محمد، کودک یک ماهه‌ی فلسطینی که شب گذشته مادرش را در بمباران رژیم صهیونیستی از دست داد و پزشکان مجبور شدند به‌علت کمبود تجهیزات بیمارستانی در غزه، یک پای او را نیز قطع کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/akhbarefori/654097" target="_blank">📅 09:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654096">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
زیر نویس شبکه خبر: اذعان آمریکا به انجام حملاتی علیه ایران؛ سخنگوی سنتکام به حمله آمریکا در جنوب ایران اعتراف کرد
🔹
ادعای سنتکام:
🔹
[شب گذشته] دو قایق در حال مین‌گذاری در تنگه هرمز هدف قرار گرفت.
🔹
سامانه پدافند هوایی بندرعباس بمباران شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/akhbarefori/654096" target="_blank">📅 09:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654095">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avg7x0d15vK1vQXs1-v393NknVQIKBh64Z5bvO1uZqLb_SL-Ucl0YWQ75d-TiLuJ8nRPzwrDBrOblmsVFNUmqqyzYY9XPKi3uufInAftcjRfbDSfRY1oiJxCKBxjcvAIpKe-lilgKVt3Kr_RhxEWj69UhMC1cUHpwc-br4dxsjZE2pWoN7Lrcsr9_VBgEW5EiQM4kKG4t439SHw5MZjALwbKsuRmCpM3fdfKKeX_ez5PIqtP6BwVHEhr_SfEoNhIiRre9At7edRCGavQ9rw42vVv7j-KeORxZNaSnlwLVcgP63DvWTt0D3A-sd9vkPE3zz2oR9Wqm_HR8XGwVQI2gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار شکارچی:اگر مورد حمله قرار بگیریم، حملات ما شدیدتر، سنگین‌تر و قوی‌تر خواهد بود
🔹
سخنگوی ارشد نیروهای مسلح ایران در مصاحبه با شبکه الجزیره هشدار داد: جمهوری اسلامی ایران برای جنگ آماده است و در صورت حمله جدید آمریکا و رژیم صهیونی، بانک اهدافش را شناسایی کرده.
🔹
پاسخ به هرگونه تجاوز جدید با آنچه قبلاً بوده متفاوت خواهد بود، دشمنان قطعاً با غافلگیری‌ها و تاکتیک‌های جدید روبرو خواهند شد و حملات ایران، در صورت ورود منطقه به دور دیگری از جنگ فراتر از مرزهای منطقه خواهد رفت و بسیار شدیدتر، سنگین‌تر، خشونت‌آمیزتر و قوی‌تر از دو جنگ قبلی خواهد بود.
🔹
اگر جنگ دوباره آغاز شود و از صادرات ایران جلوگیری شود، جمهوری اسلامی ایران از خروج نفت از منطقه جلوگیری خواهد کرد.
🔹
در مورد تنگه هرمز، ایران با هدف ایجاد امنیت و حفاظت از تجارت و اقتصاد بین‌المللی، این آبراه حیاتی را قاطعانه و با قاطعیت مدیریت خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/akhbarefori/654095" target="_blank">📅 09:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654094">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سخنگوی ارشد نیروهای مسلح در مصاحبه با شبکه الجزیره در مورد تنگه هرمز: ایران با هدف ایجاد امنیت و حفاظت از تجارت و اقتصاد بین‌المللی، این آبراه حیاتی را قاطعانه و با قاطعیت مدیریت خواهد کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/akhbarefori/654094" target="_blank">📅 09:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654092">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
۲ شهید و ۲۰ مجروح در پی بمباران اردوگاه آوارگان در جنوب نوار غزه
🔹
منابع خبری فلسطینی از شهادت ۲ فلسطینی از جمله یک کودک و مجروح شدن ۲۰ نفر دیگر در بمباران اردوگاه آوارگان غیث در منطقه المواصی در غرب خان یونس در جنوب نوار غزه توسط رژیم صهیونیستی خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/654092" target="_blank">📅 07:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654091">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2003476c.mp4?token=nquT2Ez74e_0eVbbTm8_pwOOKlBlpj99ceHYAphnqIBDh3gm4_Cw_MjxB--7DIl_RZxxWV-uIkB1ohs-FO83f3xgcg13_7n-nYP2edTMznWooJbu4xy4a_zZu_6FsVGCkHBZP3vhrbRPVYn-oFguVjM5QEuVGOgPQe-AnyWvRk7MQMoDuvBh-mqiji65s3Bhrs_Q9p65iPxGoW3VnBan__ScbZ4HQ-_Qe2nFXglOalwx7UgVzcvCMz9UZNZNGeDP5WGAdnhbM3kyVUzwnjMqmbh3tY0-AQF5c-ztX1uPpxxtj_A3p3ReNdRR2C8ofrzTeebx5YJcd7pVHz_k9oyJ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2003476c.mp4?token=nquT2Ez74e_0eVbbTm8_pwOOKlBlpj99ceHYAphnqIBDh3gm4_Cw_MjxB--7DIl_RZxxWV-uIkB1ohs-FO83f3xgcg13_7n-nYP2edTMznWooJbu4xy4a_zZu_6FsVGCkHBZP3vhrbRPVYn-oFguVjM5QEuVGOgPQe-AnyWvRk7MQMoDuvBh-mqiji65s3Bhrs_Q9p65iPxGoW3VnBan__ScbZ4HQ-_Qe2nFXglOalwx7UgVzcvCMz9UZNZNGeDP5WGAdnhbM3kyVUzwnjMqmbh3tY0-AQF5c-ztX1uPpxxtj_A3p3ReNdRR2C8ofrzTeebx5YJcd7pVHz_k9oyJ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو حاوی تصاویر دلخراش
🔹
سگ هار آمریکا در منطقه باز هم کودکان را هدف قرار داد. در جریان بمباران جنوب غزه، خانواده‌ی یک کودک به شهادت رسیدند و کودک یک‌ماهه نیز پای خود را از دست داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/654091" target="_blank">📅 07:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654090">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">قسمت بیست‌و‌ششم - پادکست کافئین</div>
  <div class="tg-doc-extra">ابومسلم خراسانی</div>
</div>
<a href="https://t.me/akhbarefori/654090" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
ابومسلم خراسانی
🗓
وقتی تمامِ جوانی و تخصصمان را پایِ ساختنِ کسب‌وکار و رویایِ دیگران می‌گذاریم، آیا پاداشِ وفاداری می‌گیریم؟ یا دقیقاً در لحظه‌ی پیروزی، توسطِ همان افرادِ ناامنی که خودمان به قدرت رسانده‌ایم، حذف می‌شویم؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/654090" target="_blank">📅 07:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654089">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/280cde0e7d.mp4?token=AAGDMDCKRxDwWQn3Exg0cfs5myiub8qPRksP7nOjCPZFcxdCIEjqb3D2O7n0cp45KELAeL8fsNxT3C1HPti2eP7XMtr9rI6l4r5UggALRSmOH6cRlP9bOHUrLlyDKNyHBne1bK1MdOJ8EHBmho1wmv7-_09mWhIvWcdDE0Wovxv5CJRO585JWe8XkNQa39L3qWOcNkLAQaqmoyR6hbjqGxajU6d_DnhiVFk331Y-3qte8fIkUAGY9DqmMAEJpCaYkDqqihZqgHPRi5mknjPxtFIKBZhYfKhLTr871IinVy1oE3lexnXlSdGM8JAR7fSzcBq0pUDLsiaJLku5pwgt9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/280cde0e7d.mp4?token=AAGDMDCKRxDwWQn3Exg0cfs5myiub8qPRksP7nOjCPZFcxdCIEjqb3D2O7n0cp45KELAeL8fsNxT3C1HPti2eP7XMtr9rI6l4r5UggALRSmOH6cRlP9bOHUrLlyDKNyHBne1bK1MdOJ8EHBmho1wmv7-_09mWhIvWcdDE0Wovxv5CJRO585JWe8XkNQa39L3qWOcNkLAQaqmoyR6hbjqGxajU6d_DnhiVFk331Y-3qte8fIkUAGY9DqmMAEJpCaYkDqqihZqgHPRi5mknjPxtFIKBZhYfKhLTr871IinVy1oE3lexnXlSdGM8JAR7fSzcBq0pUDLsiaJLku5pwgt9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابومسلم خراسانی، سردارِ سیاه‌جامگان و تراژدیِ ساخت رویای دیگران
#پادکست_کافئین
| قسمت بیست‌و‌ششم
☕️
در این اپیزود به سراغِ استراتژیستِ نابغه‌ای رفتیم که با یک قیامِ طوفانی، طومارِ خلافتِ بنی‌امیه را در هم پیچید و حکومت را دودستی تقدیمِ خاندان عباسی کرد. اما تاریخ یک قانون بی‌رحم دارد: کسی که رویای دیگران را می‌سازد، در نهایت زیرِ آوارِ همان رویا دفن می‌شود!
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://www.aparat.com/v/ohc3lx2
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/654089" target="_blank">📅 07:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654088">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XICKfm5DQrsjOgL3C0uHbSnOWFg_2ZW5st6HLFYq09VMqbxO1NgDR_mA256tweohlHxIqdPkjQ7vpCAxGbMp6QLnvxfSqccZcd4QYfif6BOABW5TlzNuIt9RV-YQnJ6zn4uY5Jjv_yUvtEzXjCh7cCnAR2i4dTWXEwE_QG9J4oGDDjWYSb4dnjyAIoZUS6jBsF7CYKZRHiCJnkRC1nkK1JoG2RbRt4DvgFv0K2X4Rg3BD6401TndGKwApYuNlS-8JSPG8XxwE9p9u6MvUE23tWRuzZU4S2rwyRV8zgN457wP4KeE8Eq2SF3_RnyQXblsk6GiqjE9sUHVKfmzYQWTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۵ خرداد ماه
۹ ذی‌الحجه ‌۱۴۴۷
۲۶ می ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/654088" target="_blank">📅 07:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654087">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
سخنگوی سنتکام ؛در جنوب ایران عملیات داشته‌ایم
🔹
سخنگوی سنتکام به الجزیره: نیروهای آمریکایی در جنوب ایران حملاتی در دفاع از خود انجام دادند.
🔹
این حملات برای محافظت از نیروهای آمریکایی در برابر تهدیدات نیروهای ایرانی انجام شد.
🔹
ما همزمان با خویشتنداری در جریان آتش‌بس، به دفاع از نیروهای خود ادامه می‌دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/654087" target="_blank">📅 06:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654086">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
عصبانیت سناتور جنگ افروز، عربستان را تهدید کرد: سازش نکنید با عواقب وخیمی روبرو می‌شوید
🔹
«لیندسی گراهام» سناتور جنگ‌طلب جمهوری‌خواه آمریکایی: به ترامپ می گویم که در اصرار بر اینکه عربستان و دیگران به عنوان بخشی از این مذاکرات به توافق ابراهیم (سازش و عادی سازی روابط با رژیم صهیونیستی) بپیوندند، قاطع باشید.
🔹
در صورت توافق بین تهران و واشنگتن، عربستان و سایر کشورها در صورت عدم پیوستن به توافق ابراهیم با عواقب وخیمی روبرو خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/654086" target="_blank">📅 06:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654085">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: اختلافات آمریکا و ایران ادامه دارد
🔹
یک نشریه آمریکایی شامگاه دوشنبه گزارش داد که واشنگتن و تهران همچنان بر سر برنامه هسته‌ای و لغو تحریم‌ها اختلاف نظر دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/654085" target="_blank">📅 04:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654083">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQBs8r5feoQ8sqY_EwAsojYT6q3gIcIhBSqnaMBYsJVgZl5IEA1aVjrxO6RNu14Q_-Fv-NT_3Ha0KXoAzKTlTNeVAh7yczf0h0hE1NZAJyhZrmONh0Yzcxs1bwtUzTFJou5CmuSJEX6JOIF4andAmm5gBFftIMrcNfxxyuOsP2x4ttu5PTLiqkUATb91EtP915eZSmgEJAxW-u8mP93QbdVj_awnRZUBo105yyc7kOcl47z30HHZxMxlQne_k6UHzYwQsq_RHvHOap_YHOgZhIgSk_z4YPdgTNr7fBqMo4H0Yobg_N1JwD2DLN6XKAHIjdGKp4Y2fDY5tYxhcigong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تأکید بقائی بر محاکمه و مجازات آمران و عاملان جنایت جنگی لامرد
🔹
سخنگوی وزارت امور خارجه حمله آمریکا به اماکن مسکونی و سالن ورزشی لامرد در روز ۹ اسفند با ۴ موشک بالستیک را جنایت جنگی شنیع و نابخشودنی خواند و تصریح کرد: آمران و عاملان آن باید در هر محکمه صالحی تحت پیگرد کیفری قرار گیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/654083" target="_blank">📅 03:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654082">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
هشدار حزب‌الله به اسرائیل درباره گسترش دامنه جنگ
🔹
یکی از سران مقاومت اسلامی لبنان شامگاه دوشنبه گفت که تشدید تنش‌ها توسط رژیم صهیونیستی،‌ در پی آزادی عملی است که آمریکا به آن داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/654082" target="_blank">📅 03:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654081">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
خبرهای داغ امروز و امشب را به انتخاب مخاطبان وبسایت خبرفوری مرور کنید
♦️
🔹
آتش‌بس نقض شد؛ آمریکا حمله به ایران را پذیرفت
👇
khabarfoori.com/fa/tiny/news-3217914
🔹
اینترنت بین‌الملل فردا باز می شود
👇
khabarfoori.com/fa/tiny/news-3217890
🔹
رهبری برای مداوا تا ساعت ۲ بامداد دهم اسفند مهمان ما بودند
👇
khabarfoori.com/fa/tiny/news-3217778
🔹
کانال ۱۲ اسرائیل: تصمیم برای حمله بزرگ علیه حزب‌الله لبنان گرفته‌ شده
👇
khabarfoori.com/fa/tiny/news-3217652
🔹
سلاح مرموز آمریکا و عربستان علیه ایران/ جنگ پهپادی تهران - ریاض آغاز می شود؟
👇
khabarfoori.com/fa/tiny/news-3217866
🔻
ویدئوهای منتخب را در آپارات خبرفوری ببینید
🔻
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/654081" target="_blank">📅 03:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654080">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhNdqIuzsDODllyLUMyK7iH8AnqH8fdkBFds6nVjyi2pgvqXuehb3tPhlfaXvKA_PFhfONcgXilzu1wB_3Vf8OjwdkMGw58oUcdt7zq3apMRWC_Ti0mNnzg094svD8Y8w0QkLq8keQaZ5rFjlkXrKMKL5qh_zWDKbVOTJNoiVSWSmS9FySu7Bq-_KcQTAJeoESPtvnGZUsaivAzdtEcbjpvfLV4n-a4GoU2-YyiB20WHR6Ai0l4Vu_Dv2g71tFNXBwJejvM0MLRcEpn03D_naqAFzVX4uT3_Qp2wCtMQRydNF5newhREupLA8JfLcQq22pRDDWYRwzVzLC2p53gT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اذعان سنتکام به نقض آتش‌بس با ایران
🔹
سخنگوی فرماندهی مرکزی ارتش آمریکا بامداد سه‌شنبه به نقض آتش‌بس با ایران از طریق حمله به اهدافی در جنوب کشور اعتراف کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/654080" target="_blank">📅 02:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654079">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP2zPv6468CxI0wkCmgb9mTyM_RPOTIUQrVCYnWBctZG_EnOJSUsZyufYRkvEe3zJmzDeoYpmswTAmS0vC6gidRN6oGyLsOs1nJCkQNwKbtpmbElVlY20oZ0nP6VNCeEXsRuH18fdDEN_Qhitl5Jioi32B8UayzgDv6auiNNa0LZc0KWKRJjkN32g7bVBYXuMS4Aa7rKAYqtGrpQY5D7OBooDU4tmSnEE_ncNP6zckJodWiaO3TS0hf3y6lvSKh7k1uho0iic7hNNFNzv4ICpjCDWkZ-QdC9W4S-LJxY9tslO4RBKQHthxdUFWRW4OhsOvejHySU6u_x1F4EMQ9FAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ بار دیگر زیاده‌خواهی درباره اورانیوم غنی‌شده را تکرار کرد
🔹
رئیس‌جمهور آمریکا بامداد سه‌شنبه مدعی شد ایران یا باید اورانیوم غنی‌شده خود را تحویل دهد یا آن را با حضور ناظران، نابود کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/654079" target="_blank">📅 01:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654078">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5aZwzsbituUBO9s-nATkr6JCH3ZuvR2a6AomqlqPTcrrSaCR29ov2UWCOFuWB9JP9OmS7ALCMrNo8SocTQa33pZGQVWtx4YYGA8c_K7rVzjlSNvgk9MunBp3wuE1AE69v_u-Y7fwlOF1ipyy0wjmebRwfOyTXjySAhiR9a0sI01TAJReXgNh8RrcVJTj2MIV5cLouMDYQYM4Q86UGDTexYl_Q48uY8gNxYwPl7EUItjOZCQ4Nrz0Ue-bL4S0M91NdAztIIvZPMyfyTQw2OjkhW3O8igavni-n_O1dZDURVBKT_2cB3meX7wERfGVHzMe_tBhK9TIghB4cUlS57Otg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه خبر: منبع صدای انفجار در بندرعباس هنوز مشخص نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/654078" target="_blank">📅 01:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654077">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
دو قایق نیروی دریایی سپاه پاسداران در خلیج فارس توسط جنگنده‌های آمریکایی هدف قرار گرفتند و چهار سرباز شهید شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/654077" target="_blank">📅 01:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654076">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
مهر: اوضاع بندرعباس کاملاً تحت کنترل است
🔹
منشا صدای انفجار از منتهی الیه شرق بندرعباس بوده است.
🔹
همزمان برخی از شهروندان از شنیده شدن صدای فعالیت پدافند در این شهر خبر داده اند.
🔹
اوضاع شهر، کاملاً تحت کنترل است و جای هیچگونه نگرانی برای مردم شریف بندرعباس نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/654076" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654074">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
دقایقی پیش مردم در بندرعباس صدای چند انفجار شنیدند
🔹
هنوز محل دقیق و منشأ این صداها مشخص نیست.
🔹
همزمان در خلیج فارس حوالی سیریک و جاسک نیز صداهای مشابه شنیده شده است.
🔹
سحرگاه امروز یک فروند پهپاد متخاصم در محدوده خلیج فارس توسط نیروهای مسلح ایران منهدم شد.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/654074" target="_blank">📅 23:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654073">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcVG8nSoWGHSyLPsMzJVrPbqonZwNtK8Ufo_81gJl9b6qSrroOlIETzIiqY7Z9_-ihzK5TvLZDZoDwdrQcIFjRbclrob8GiImYGlkykCk5a6saKDlvLbimbmxyUJosbBniSo5ceZUIpcjMe38f6BEDw2ogbw3zp7c3jhJuiWLFf_JZl6dwgAoQQU2B1xsEcBDUx9gzfLC5klfKXCeulIzLzb2Cg1Y72qcjXlDcprcvkGe1OtZGgWRuF079ZEcmVfE_DIWtNE5IzrOCu4l7X-Sky5YsQjo0VZwUwSTc5IyXBQFABBUxTv-ZcbrZDRVF1bx5dPcgOnA1pIeyCw9kLUBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وظایف مسئولان و دستگاه‌های اجرایی و مدیریتی در جنگ
🔹
مروری بر وظایف مهم کارگزاران نظام در شرایط فعلی کشور براساس پیام‌های رهبر انقلاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/654073" target="_blank">📅 23:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654072">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc38a79f3e.mp4?token=A_KSvofc0bBYPFoQ3UP_5I53AekrChTJJikx5xd5ndtlvwGjH6Azot6A4DJzoDL6FsHkNNRfEf32ou-5_Qr8HIBzgXnz613mGK-EZIE9VfdUK2jYJLKBuPmGkdO6SeEw3-bIdQ40C5x1Yxxx788BRSCj0OFaB6bFH55FD1bkyRUhAk9SnhqAW9UiXqfLN2L_B5u-J_X9LPy7ujiqXwrr4yEaHG6-qoYgc2qfJDVRN4Q1RdGzBz0ZbGkN9bKrNMhIPUw6OVgjjkbUv4pJlMU43sCqFmlJ70CBd-ilYhL0teh2QSBRvDtF0aQLuzeT519YH12RraQ1eV0vHGTm0agbGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc38a79f3e.mp4?token=A_KSvofc0bBYPFoQ3UP_5I53AekrChTJJikx5xd5ndtlvwGjH6Azot6A4DJzoDL6FsHkNNRfEf32ou-5_Qr8HIBzgXnz613mGK-EZIE9VfdUK2jYJLKBuPmGkdO6SeEw3-bIdQ40C5x1Yxxx788BRSCj0OFaB6bFH55FD1bkyRUhAk9SnhqAW9UiXqfLN2L_B5u-J_X9LPy7ujiqXwrr4yEaHG6-qoYgc2qfJDVRN4Q1RdGzBz0ZbGkN9bKrNMhIPUw6OVgjjkbUv4pJlMU43sCqFmlJ70CBd-ilYhL0teh2QSBRvDtF0aQLuzeT519YH12RraQ1eV0vHGTm0agbGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا ایران به سمت ساخت سلاح اتمی می‌رود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/654072" target="_blank">📅 23:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654071">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e1d60f76.mp4?token=Ug5YWekOD6gTaAZ-W8LtdDC7E8emsQvgGTi3j41cqjh71DQt2x2OOqDrCyDp_lN5jYupk2OjGwJ-oKS8tuPjFud1ov3v2vnorm7WyQhgbH_DMyNHVAD-60dPk_ZCd3MWcgXT_pDKco_uGO-72v--LrGJieGrP4DHVFLeCK39o1R1iYzPnhn96miu2As4ZrTmHp-wyBjcvfXKcAyOxXZ-wdFeq2s15c4xjqgNpHHHrjaFmB_wrX2d3okNV-s1C64AYwZ4cMOf8_9LAZ9FcL7UrM24T5tqiqCLaG6o77tt98OIPhHI36HPHJN9BXG1GL1wlt3tkUfnWVNk1xwRXOMjlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e1d60f76.mp4?token=Ug5YWekOD6gTaAZ-W8LtdDC7E8emsQvgGTi3j41cqjh71DQt2x2OOqDrCyDp_lN5jYupk2OjGwJ-oKS8tuPjFud1ov3v2vnorm7WyQhgbH_DMyNHVAD-60dPk_ZCd3MWcgXT_pDKco_uGO-72v--LrGJieGrP4DHVFLeCK39o1R1iYzPnhn96miu2As4ZrTmHp-wyBjcvfXKcAyOxXZ-wdFeq2s15c4xjqgNpHHHrjaFmB_wrX2d3okNV-s1C64AYwZ4cMOf8_9LAZ9FcL7UrM24T5tqiqCLaG6o77tt98OIPhHI36HPHJN9BXG1GL1wlt3tkUfnWVNk1xwRXOMjlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: اگر توافقی با آمریکا شود به معنای پایان چالش‌های ما با آمریکا نیست
🔹
در شرایط موجود بعید می‌دانم که آمریکایی‌ها وارد توافقی شوند که خواسته‌های جمهوری اسلامی را بپذیرند و این موضوع خیلی دور است و اگر بپذیرند باید عمل کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/654071" target="_blank">📅 23:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654070">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceac5dbe5f.mp4?token=ebZjYs8DOQ9J-Pnkn-FSjt0hreLaatvQmDqfeqFqSXJKSIMbHFbQR4K5njKXOi6E_fbBVATjxW_im93Um5k79HMBg3HoHh9cc65AqV_e5r199ffO39lqc7SmedvI4kdte4xPVtWWcoSAuL2NdNIP4tomqUyiz5BQCGvh9Ao-Cmu_xxVGEDQ-fGKgL2j-xfdzdX5hL7EyXLEnPpUnT3ConlXO3gkPlat3kTxVBXc6woENgLudMW_jBvPQ7aOJZpjARHriT7sRDiGpj-DrIQ3qoYaD-AJwWScKiUspV694wUq0rMFQ93C6ij-QJJAszYytKzN0ljFPQRrr756hT4KgZIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceac5dbe5f.mp4?token=ebZjYs8DOQ9J-Pnkn-FSjt0hreLaatvQmDqfeqFqSXJKSIMbHFbQR4K5njKXOi6E_fbBVATjxW_im93Um5k79HMBg3HoHh9cc65AqV_e5r199ffO39lqc7SmedvI4kdte4xPVtWWcoSAuL2NdNIP4tomqUyiz5BQCGvh9Ao-Cmu_xxVGEDQ-fGKgL2j-xfdzdX5hL7EyXLEnPpUnT3ConlXO3gkPlat3kTxVBXc6woENgLudMW_jBvPQ7aOJZpjARHriT7sRDiGpj-DrIQ3qoYaD-AJwWScKiUspV694wUq0rMFQ93C6ij-QJJAszYytKzN0ljFPQRrr756hT4KgZIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: پهپادهای دشمن همچنان در مرزهای ایران در حال گشت زنی هستند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/654070" target="_blank">📅 23:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654069">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
۲ تلاش اسرائیل برای ترور شیخ نعیم قاسم ناکام ماند
🔹
شبکه الحدث گزارش داد تل‌آویو دست‌کم دو بار به تازگی تلاش کرده شیخ نعیم قاسم، رهبر حزب‌الله لبنان را هدف قرار دهد اما موفق نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/654069" target="_blank">📅 23:14 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654068">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c740ca854.mp4?token=IzYze0teOdYi5mVF0IbE7z3KWujTe-qdZjE5KEZz7qJEErzD4Ry8-BAdgDqOtBSbmfbKYMP75Zi_gxKQwW44VA2IjvO6PgHNXtC1ZjrqxBKdOcpVGeGniTdJLK4A92d_6ZugvmPIqo7_tHK_xYqpAba4Z3r4cw2HB84kL18f_jyPlxrwon1fADoupFGFUm6G7iW0UTj-sXbyhO5eO4D8or4UOUhp5SjidJUBjiS__haNCC8_CP0ylpqd6kp5HNpVnDBEeDOlrSnLu9bT-hak5S4u8MFmYy_bXBm44DU-v9LfJYTKZ2r57InWbYEOcgqc57nZ7tY4CSq_TU3SH62i-rRmXwNQYJMWVM3RZVj1MCfywVhPZ-ZQXjUoQhO_PfmCQpMuJO-tNVRNNJbrppqn4TzyZkLi6dDL-HjxHm9xnuSFzQRVXpl6wiKySfF3RsrtgytwUWSfzZyR7GV38lqZ50kF1H88xCatGe5TeuENccqocJhR32AIy8Tza5Mj5RwVzc3Vo7TOhOOuthfGsMx0QS3ifO0U_w7bGpvEneKP7vvJ_oe1qPC4IyE3pVD2y5svt8VEBItIymHvDE1npkPM6hKV9sS7ND7hn0peU3xqc-Kkx7Vf4bpSdZp14Z08NGMb5e53fNSofBOFM5y1TB4YbVkKcccJHlS5o8774-TCiRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c740ca854.mp4?token=IzYze0teOdYi5mVF0IbE7z3KWujTe-qdZjE5KEZz7qJEErzD4Ry8-BAdgDqOtBSbmfbKYMP75Zi_gxKQwW44VA2IjvO6PgHNXtC1ZjrqxBKdOcpVGeGniTdJLK4A92d_6ZugvmPIqo7_tHK_xYqpAba4Z3r4cw2HB84kL18f_jyPlxrwon1fADoupFGFUm6G7iW0UTj-sXbyhO5eO4D8or4UOUhp5SjidJUBjiS__haNCC8_CP0ylpqd6kp5HNpVnDBEeDOlrSnLu9bT-hak5S4u8MFmYy_bXBm44DU-v9LfJYTKZ2r57InWbYEOcgqc57nZ7tY4CSq_TU3SH62i-rRmXwNQYJMWVM3RZVj1MCfywVhPZ-ZQXjUoQhO_PfmCQpMuJO-tNVRNNJbrppqn4TzyZkLi6dDL-HjxHm9xnuSFzQRVXpl6wiKySfF3RsrtgytwUWSfzZyR7GV38lqZ50kF1H88xCatGe5TeuENccqocJhR32AIy8Tza5Mj5RwVzc3Vo7TOhOOuthfGsMx0QS3ifO0U_w7bGpvEneKP7vvJ_oe1qPC4IyE3pVD2y5svt8VEBItIymHvDE1npkPM6hKV9sS7ND7hn0peU3xqc-Kkx7Vf4bpSdZp14Z08NGMb5e53fNSofBOFM5y1TB4YbVkKcccJHlS5o8774-TCiRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: تا اقدامات پنج گانه اعتمادساز آمریکا انجام نشود، مذاکره معنا ندارد
🔹
اتمام جنگ در تمام جبهه‌ها و تضمین عدم تکرار آن باید از طرف آمریکا اثبات شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/654068" target="_blank">📅 23:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654067">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjAVNPuNIJJIUsW9fpTnQ62_wHVjFAMb70jukTxOwUPDah9fCSXO-C1Uf_-WFtrU4UuG-t52vY3Q2sL44sXDUb_iOTJmduuMTty5lYUQ4XG_Jj3PL4u1UfPlc624jOILlPZWxJsAH4w8ntH_z8VU-sbUQUIzoObF-rUA6i6BTZa3pa82LgPlZnu9pEEuAKFnh06FfFQWJQQg1KGC40fhVbbqQEEq3BOELabBP8zO9WhThc95--Nxt65pTi2oq5I5mGABJtOd-43JhnAlwkX2Im9R6ilhJ2DGms5b08cv4l2vWjYlPugNh9WrJhF8ggKi3f5FjFKI8ZATP-6GcZ1jUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفت‌وگوی وزرای امور خارجه روسیه و آمریکا درباره ایران
🔹
وزارت خارجه روسیه روز دوشنبه خبر داد که سرگئی لاوروف و مارکو روبیو در تماسی تلفنی درباره «ابتکارات دیپلماتیک برای غلبه بر بحران در تنگه هرمز» تبادل نظر کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/654067" target="_blank">📅 23:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654066">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
رئیس سابق سیا: آمریکا بعد از جنگ اخیر تمایلی به استفاده از پایگاه‌هایش در منطقه ندارد
🔹
دیوید پترائوس، رئیس اسبق سیا و فرمانده اسبق سنتکام در مصاحبه‌ای گفته که ایالات متحده آمریکا بعد از جنگ اخیر علیه ایران تمایل چندانی برای استفاده از پایگاه‌هایش در منطقه ندارد.
🔹
پترائوس گفت: «ما از دسترسی به بسیاری از پایگاه‌هایی که معمولاً در اختیار داشتیم، منع شدیم. البته حقیقت این است که خود ما هم حالا که دیده‌ایم ایرانی‌ها چه توانمندی‌هایی برای هدف قرار دادن این پایگاه‌ها دارند، دیگر تمایل چندانی به استفاده از آن‌ها نداریم. این تهدیدها بسیار فراتر از زمانی است که من فرمانده سنتکام (ستاد فرماندهی مرکزی آمریکا) بودم؛ یعنی بین سال‌های ۲۰۰۸ تا ۲۰۱۰.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/654066" target="_blank">📅 23:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654065">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4bf824f0.mp4?token=D-kWHWkncTNDRnydjrk1uMu2vj6qdmJSp5Gt7AFYg-MWSyktH6W5bMAVYgWVl9RqixK_uHKpy5mIjbLs6f2USaZc4ZDFYEO4-ecI3S8yLlAhSd9qNAoPhfLEyssyVD0B0XhOpTwPQaWPrRIoI_s3hvZKk5pD0nk5WDDxWPKwycBEv_amjY5l2Gx6JyXvhIsA7h9gIPoFTu-ipoDbN34lPYWnqGohs5bhvaKXOczvZsw_YjPTX2c0Nu8Lf1UVdG-oPmlcZnZ1KK7xZ-UDMlqHpRR1sh9F4beDy10Cmu48l2isYXv_rw3UkCuxT6zudKDMxddgbzi3IHYNeNTNqwlBAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4bf824f0.mp4?token=D-kWHWkncTNDRnydjrk1uMu2vj6qdmJSp5Gt7AFYg-MWSyktH6W5bMAVYgWVl9RqixK_uHKpy5mIjbLs6f2USaZc4ZDFYEO4-ecI3S8yLlAhSd9qNAoPhfLEyssyVD0B0XhOpTwPQaWPrRIoI_s3hvZKk5pD0nk5WDDxWPKwycBEv_amjY5l2Gx6JyXvhIsA7h9gIPoFTu-ipoDbN34lPYWnqGohs5bhvaKXOczvZsw_YjPTX2c0Nu8Lf1UVdG-oPmlcZnZ1KK7xZ-UDMlqHpRR1sh9F4beDy10Cmu48l2isYXv_rw3UkCuxT6zudKDMxddgbzi3IHYNeNTNqwlBAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: آمریکایی‌ها هنوز درباره آزادسازی منابع بلوکه شده ایران هیچ اقدامی انجام نداده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/654065" target="_blank">📅 23:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654064">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
فوری
🔹
۵ پیش شرطی که ابتدا آمریکا باید انجام دهد
🔹
رئیس کمیسیون امنیت ملی خبر داد:
🔹
۱. خاتمه جنگ در همه جبهه‌ها؛ مخصوصا در لبنان؛
🔹
۲. محاصره دریایی آمریکا علیه ایران باید برچیده شود؛
🔹
۳. پذیرش حاکمیت ایران بر تنگه هرمز؛ اگر محاصره ایران برچیده شود، تردد کشتی‌های غیر نظامی برقرار خواهد شد؛
🔹
۴. تعلیق تحریم های ایران طی ۳۰ روز؛ از جمله تحریم نفت
🔹
۵. آزادسازی منابع بلوکه شده ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/654064" target="_blank">📅 22:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654063">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcea-dBwP0MCXTqeu6sF9XTOFjpxu-X8Z8o83pqXWPl7rsv2g-BFCsXAQ-1Cpq03TjU9TRJDfcW-B8381MCdHl_CaMMT3tKxT1M4IHzr-cFTKJIbk_ZbNXz0BfXu8_rypnuels96PmqCRb3Olqa8AqYqkZ1NRqp0zOc7SmSX-LqOXM-z7N2EBI8i3ONHyF5A7J8YhnP2FCEBWbzS7857Ys_wzw9L3saNmJJRIGGR6_DYsDycKg_zfRfZ25g-R9LRoGV5OR3QASfywzDVyqqNtjjSXklQjF2NUdc6BAtehRYSatqC5POT7TSeBfJC4K99lrMh6GCzswZ8wl4Z--arUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سلاح مرموز آمریکا و عربستان علیه ایران/ جنگ پهپادی تهران - ریاض آغاز می شود؟
🔹
اخیرا یک شرکت تسلیحاتی آمریکایی و یک شرکت سعودی شروع به احداث کارخانه ‌ای نزدیک ریاض برای تولید پهپادهای رزمی الگوبرداری‌شده از پهپاد شاهد ۱۳۶ ایران کرده اند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3217866</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/654063" target="_blank">📅 22:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654062">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjyxlVQNYkHVXDYfviSS3aNS1auiIrgAaD5zr-FQKKKxOzobR3wA1lX0gV-rU9hhcsZPJrYRskKKil9t-GXPJ6YaqP_0R1_nFjgiOk57zHbv26KkYC3R-375qslzwxGVdK8yArU0dirNJvFZukv_KaHZ0FgZbde7pv_RfPYU7t-L8yXQfCS7v1_xuKQ25tDnB4jvUmeYEaTKI_vDbb7Qk9IFieVlIlCaooXFMJOAKKanXJN9jBT0vR9epELEjKMw7qyUHYMBrY_UrwH1TghkC3jFOg2Sa4wJK-MUThO7jJKtxHOtyKguFdVyWiv5fbh15mB74SvWT1alaj2jOXU6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطر فوری
🔹
قالیباف، پس از تمدید ریاست خود بر مجلس، در سفری فوری و از پیش اعلام نشده به همراه با عراقچی وزیر خارجه و همتی رئیس کل بانک مرکزی، راهی قطر شد. مقصد این سفر گمانه‌زنی‌های گسترده اما تأیید نشده‌ای را برانگیخته است. برخی رسانه‌ها محور گفتگوها را آزادسازی دارایی‌های بلوکه‌شده ایران می‌دانند. در مقابل، گروهی دیگر موضوعات راهبردی‌تری چون برنامه هسته‌ای و امنیت تنگه هرمز را هدف اصلی این سفر اعلام کرده‌اند. تا لحظه مخابره این خبر، هیچ منبع رسمی جزئیات را تأیید نکرده است.
🔹
هفتصدوپنجاه‌ونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/654062" target="_blank">📅 22:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654061">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa05d72b98.mp4?token=o1P-ayWz0Dyc3GRkfN5NLnq7j4WC_eU-wUkW6YDuuK8a5Oy0Xnf-e0GTC9rxEDuS8E-pzL63rT9r7igYK90hDPtbHU9AjnFj6YAFmEDWHhEqb7cE4NVZMtJ0zK9KJpdmWcerq7lXqau-CD7O7FK2jKkpgtPMXD7WflJna4ges4UibZ0NvNH_KkK2_D_ZOrOiZl_5frGPPHGmWoDFhVQeMWaskV0JGfl07zH_rzYAzvfhldRzRpQusK9Mo2olLEydhQE1cQqHgV4imiBQ3JPvTfC0c1hj-4k2afqNuCZR88RGwYQqTNSz7y5HWlwDdLoNBuOs0nIMc8_xajSrTYSlyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa05d72b98.mp4?token=o1P-ayWz0Dyc3GRkfN5NLnq7j4WC_eU-wUkW6YDuuK8a5Oy0Xnf-e0GTC9rxEDuS8E-pzL63rT9r7igYK90hDPtbHU9AjnFj6YAFmEDWHhEqb7cE4NVZMtJ0zK9KJpdmWcerq7lXqau-CD7O7FK2jKkpgtPMXD7WflJna4ges4UibZ0NvNH_KkK2_D_ZOrOiZl_5frGPPHGmWoDFhVQeMWaskV0JGfl07zH_rzYAzvfhldRzRpQusK9Mo2olLEydhQE1cQqHgV4imiBQ3JPvTfC0c1hj-4k2afqNuCZR88RGwYQqTNSz7y5HWlwDdLoNBuOs0nIMc8_xajSrTYSlyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: آمریکا هفته دوم جنگ از طریق عاصم منیر اولین پیشنهادش را ارائه داد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/654061" target="_blank">📅 22:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654060">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmRWMfvPq0qhw1v0V88J_9nMEbhk26IQ-eb84JOAq3aDEfWJv61ZzOUwiNB1OYyAroBwfBIGDHvtGc6u_z-sbdZmGled1CCcOcgyZAs1MO5Y-IPRqjZ0r6nv9INU9woIzliAPdILxMxiDnqHeTawSBQM6oPjnYX08c392A-cQUKN4FcfaoDr1FpQxSLIN_FxphcECBjMn23iPfyMnTSSNmBnZGrHGhRCE7HawgNgeITX8vLdEJYzjaL7qYcN-bLSrmPVLo0WfnJZLQdzPnoU25DViHJH3TQT2Nym5Zla41u_O5rAr2OYKR--IOveLYJ5Oz5iaARPB034MVlcZCPmmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همنوایی شورای همکاری با اسرائیل علیه حزب الله
🔹
شورای همکاری خلیج فارس امروز دوشنبه ادعاهایی علیه نعیم قاسم، دبیرکل «حزب‌الله» مطرح کرد و از اظهارات وی علیه حکام بحرین به شدت ابراز خشم کرد.
🔹
جاسم البدیوی دبیرکل این شورا،‌ اظهارات نعیم قاسم را «غیر مسئولانه» دانست و مدعی شد دبیرکل حزب‌الله در امور داخلی بحرین مداخله کرده است.
🔹
وی ضمن دفاع از سیاست سرکوبگرانه دولت بحرین در قبال مخالفان سیاست‌های آن، مدعی شد که این افراد علیه وطن خود مرتکب جرم شدند و برای ایران جاسوسی می‌کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/654060" target="_blank">📅 22:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654059">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
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
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/akhbarefori/654059" target="_blank">📅 22:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654058">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۲۰ فرودگاه به چرخه فعالیت برگشتند
اخوان، سخنگوی سازمان هواپیمایی کشوری، در
#گفتگو
با خبرفوری:
🔹
در حال حاضر، کارشناسان سازمان هواپیمایی کشوری، در حال ارزیابی شرایط و رفع محدودیت‌های موجود هستند تا زمینه بازگشایی فرودگاه‌ها با حداکثر ضریب ایمنی و امنیت فراهم شود.
🔹
تاکنون ۲۰ فرودگاه فعالیت خود را از سر گرفته‌اند.
🔹
روند بازگشایی سایر فرودگاه‌ها نیز به‌تدریج و پس از احراز کامل شرایط ایمنی، امنیتی و عملیاتی انجام خواهد شد.
🔹
همچنین فرودگاه تبریز به زودی بازگشایی می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/akhbarefori/654058" target="_blank">📅 22:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654057">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJSQULCyBprYoSZk3unkItlvkJ952Cw4R7GZ8IWR-IeAWvZN6jVDJmA8_2QHYJCgnC4z8UwFCs3mWyZOFbD60qxLtqaovirhx9LKwmucpPVpu_X7nOzjy0tdBinavkUe4BPSg6gpisBvGqsbekToyEGQo2E1CJBavXooKVrnKOSebcBTEgvc53X166uG52SyfCPtALe2D2UPv0sUZFVY-4Gl_IUzeBF4eGp40XPwXgKy7FC6BAZbvkMlHOYX56ohxbui1iUg5JWyjcSftqXBSuWzcIHyRe16g-ZwSGdlP62EkI2LBNushejWPW5uINvL0y-PSBDte1KQ3BKNQr2M3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس امور اطلاع رسانی دولت، ابلاغ رئیس جمهور برای اتصال اینترنت بین‌الملل را تایید کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/akhbarefori/654057" target="_blank">📅 22:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654056">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1913aef4a8.mp4?token=GJSgDYkLiAmFueAwGTCLStggKD2y58-awe4Yp5XuYVR4Wg_XQcNWVNam9vZxM2DENesIA87tH5lQUSnnzG8iZIoMiXnB-JZRPQfocajJjsg-eaL9a9Xgrg72JjmNszSpKEZzB0fFDU1x5hZkl_eS4SovIW5RaXbtO5fytBmt-8RAhy_qYlvyDDExJ31xy-6s4Sp1GKh3cyl-upC9V18eQ_O_tFNfTsdwXp2RZsK7phToRI0VHN4oQb49oV2-MhLPAGKzzfUptVWX1mYmrFEI5tsKAyFTwKY5FgwFG0Y0XHFMxCTXldA4YDNoBtA0Gj1LANKIWNUbLquK04YHzBtS8WyieWuk38UulcxIjnQ1_x3kZ6sPH3vjzyMODfN2TG_QjDA0ueRUiwT4krfBfGE1togWRLo5LgKf_V6gVQbCWQC_LypU9-A4RWaAcfBzzhB5gq8y0QeTOe3kSntx6sLY6QWfd0Y4s9uZQMC6sPqXSJar13mov_Q52JlI6ZMETCCP0924JLv4FCpmoimhVvjZrdVZxpwFJXhX7zditq_9Nw2V6fMzSmaoGD85lsZxzZJdUfnNQ_bnuxk0aPhyJXzjTB9NQpIflSoFX4gr9nhfc8HnM1aJNsVDLRenU5i9GDG9Iov67iT0xn7IZevwAo7IoP1lb_lUty-SbD9cJ4vOuhE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1913aef4a8.mp4?token=GJSgDYkLiAmFueAwGTCLStggKD2y58-awe4Yp5XuYVR4Wg_XQcNWVNam9vZxM2DENesIA87tH5lQUSnnzG8iZIoMiXnB-JZRPQfocajJjsg-eaL9a9Xgrg72JjmNszSpKEZzB0fFDU1x5hZkl_eS4SovIW5RaXbtO5fytBmt-8RAhy_qYlvyDDExJ31xy-6s4Sp1GKh3cyl-upC9V18eQ_O_tFNfTsdwXp2RZsK7phToRI0VHN4oQb49oV2-MhLPAGKzzfUptVWX1mYmrFEI5tsKAyFTwKY5FgwFG0Y0XHFMxCTXldA4YDNoBtA0Gj1LANKIWNUbLquK04YHzBtS8WyieWuk38UulcxIjnQ1_x3kZ6sPH3vjzyMODfN2TG_QjDA0ueRUiwT4krfBfGE1togWRLo5LgKf_V6gVQbCWQC_LypU9-A4RWaAcfBzzhB5gq8y0QeTOe3kSntx6sLY6QWfd0Y4s9uZQMC6sPqXSJar13mov_Q52JlI6ZMETCCP0924JLv4FCpmoimhVvjZrdVZxpwFJXhX7zditq_9Nw2V6fMzSmaoGD85lsZxzZJdUfnNQ_bnuxk0aPhyJXzjTB9NQpIflSoFX4gr9nhfc8HnM1aJNsVDLRenU5i9GDG9Iov67iT0xn7IZevwAo7IoP1lb_lUty-SbD9cJ4vOuhE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی «تنگه هرمز» اقتصاد جهان را به «وضعیت قرمز» می‌کشاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/akhbarefori/654056" target="_blank">📅 22:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654055">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4HC5ZosdQrH_r2ENa3aN5j7f4cL1NNZ0SaamMTGMCik671OarpmniA5Bd8nT9UHQac62jMcv797tWUUIvKs8igz89uiSeOyGKebBckQc3zf1uAphrmQ5N4Ol3nM0I-cPFVwq_G3AGurL0L75uu0iaPj4gpF7F0yykwvwVnJkzb-NYpMpp9fdlKWN-vYmcCTUvuu_NrAbaDobLk654xsyNGrvshniGWgjyQ1gI3NRHBV8JQ15DL1SiJBo5Y7oVUhi4tDI366SHTJ3UbDcAkAz4wjq1-40CDI0LFpe7t6yd3XD6PrJqR12LETWqaGHZXyZjpqJTBXnJ9HxTTjV9vcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معادلات جدید حزب‌الله؛ آیا باید منتظر تغییر در غرب آسیا باشیم؟
🔹
جنبش حزب‌الله اخیرا دامنه عملیات‌های خود را گسترش داده و با پهپادهای انتحاری، تلفات بسیاری از صهیونیست‌ها می‌گیرد؛‌ همین مسئله باعث وحشت مسئولان اسرائیلی شده است.
🔹
«تحولات لبنان و مواضع ملی‌گرایانه و توأم با شجاعت مقاومت به رهبری حزب‌الله، بارزترین خلاصه‌ی مسیر ساخت خاورمیانه جدید، بازگرداندن کرامت به امت‌های عربی و اسلامی، و شکست پروژه استعماری آمریکایی-اسرائیلی است.»
🔹
«عبدالباری عطوان» تحلیلگر برجسته جهان عرب با اشاره به سخنرانی‌های اخیر نعیم قاسم دبیرکل حزب‌الله و نبیه بری رئیس پارلمان لبنان، نوشت،‌ این سخنرانی‌ها نشانگر یک تغییر مهم است که منطقه و امت اسلامی را از حالت تحقیر، ذلت و شکست کنونی خارج خواهد کرد و به تنها گزینه مؤثر، یعنی گزینه مقاومت در تمام اشکال و صور آن، و در رأس آن‌ مبارزه مسلحانه بازمی‌گرداند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/654055" target="_blank">📅 22:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654054">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
وبملت اثرگذارترین نماد در صعود شاخص بورس
🔹
بانک ملت با جابه جایی حجم بالایی از سهام به عنوان پرحجم ترین نماد بازار و ثبت خالص ورود ۳،۹۵۰ میلیارد ریال پول حقیقی، علاوه بر قرار گرفتن در صدر نمادهای پر معامله، با اثرگذاری مثبت ۵،۱۰۶ واحدی، بیشترین نقش را در صعود شاخص کل ایفا کرده است.
🔹
با توجه به رویکرد مثبت بازار از تحولات سیاسی، در نخستین روز بازگشایی بازار سرمایه پس از رفع محدودیت های معاملاتی دوران جنگ تحمیلی رمضان، نماد بانک ملت (وبملت) در پی برگزاری مجمع عمومی فوق العاده و تصویب افزایش سرمایه، بدون محدودیت نوسان قیمت به تالار شیشه ای بازگشت.
🔹
بر اساس این گزارش، بانک ملت با اجرایی کردن افزایش سرمایه ۴۲ درصدی از محل سود انباشته، سرمایه ثبت شده خود را از ۲۳۸ همت به ۳۳۸ همت افزایش داده است.
🔹
بر این اساس، در جریان معاملات چند روز گذشته بازار سرمایه، نماد "وبملت" با قیمت ۹۱۰ ریال به ازای هر سهم بازگشایی شد که حاکی از ۴.۷ درصدی نسبت به قیمت تئوریک بوده است، این روند صعودی با استقبال گسترده معامله گران تا پایان بازار تداوم یافت و قیمت پایانی سهم با ثبت رشد ۵.۲ درصدی نسبت به قیمت تئوریک، در سطح ۹۱۴ ریال تثبیت شد و تا قیمت ۱،۰۲۰ ریال ادامه داشته است.
🔹
اعتماد سهامداران به سهام بانک ملت به عنوان یکی از ارزنده ترین سهام بازار با سودآوری بالا و بالاترین تراز عملیاتی در بین بانک های فعال در بازار سرمایه، از جمله دلایل صف های سنگین برای خرید سهام این بانک بورسی عنوان شده است.</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/akhbarefori/654054" target="_blank">📅 22:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654053">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 57</div>
</div>
<a href="https://t.me/akhbarefori/654053" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاه‌وهفتم
رائفی‌پور:
🔹
0:10:40 نماد برکت در یهودیت
🔹
0:20:30 بلاغت و فصاحت بسیار زیاد در کلام حضرت علی(ع)
🔹
0:33:00 هارون باعث سجده کردن و ایمان آوردن ساحرین شد
🔹
0:40:40 خطای تغییر صلوات توسط اهل سنت
🔹
0:48:40 چرا هارون حضرت موسی را برادر خطاب نمی کرد
🔹
0:57:00 خواب شنیدنی فاطمه بنت اسد و تعبیر آن
🔹
1:03:45 منظور از الم نشرح... چه کسی است
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/akhbarefori/654053" target="_blank">📅 22:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654052">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5093129d.mp4?token=hCBik05zJHPZlgcdaY9J8sm3mje-fsKWhrMufeqM38BGZW7WTZG69kS7qJe9V8tMOskhS_AEWriN1K8x2Xpj0XCMvRhUBoCHBzjYw6_CUJczc4cWaXSvy1PG8ldSrwQrZYVVzQV7KM4vM3nzCrUw1sVwqpfbWOs9ojJ5pmW5o1M09_Eslp0uCX2ntYbuKzkcBr9rVmT_KT1_y2dVctW-4gnUwj1G2XNW6wDHe1KQh8s16oBBmApWNJCW0eD9O49Gr-OH-NwxCvml-cfQoyXkfHHgLyN9VmPTPYsnD3AGIABsmcEOXv8RxelPwpRVZIDy92YT9yz1oQU2UK5vAhu7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5093129d.mp4?token=hCBik05zJHPZlgcdaY9J8sm3mje-fsKWhrMufeqM38BGZW7WTZG69kS7qJe9V8tMOskhS_AEWriN1K8x2Xpj0XCMvRhUBoCHBzjYw6_CUJczc4cWaXSvy1PG8ldSrwQrZYVVzQV7KM4vM3nzCrUw1sVwqpfbWOs9ojJ5pmW5o1M09_Eslp0uCX2ntYbuKzkcBr9rVmT_KT1_y2dVctW-4gnUwj1G2XNW6wDHe1KQh8s16oBBmApWNJCW0eD9O49Gr-OH-NwxCvml-cfQoyXkfHHgLyN9VmPTPYsnD3AGIABsmcEOXv8RxelPwpRVZIDy92YT9yz1oQU2UK5vAhu7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در جنگ گذشته مقاماتی که در پناهگاه زیرزمینی بودند با وجود حملات سنگین آسیبی ندیدند
🔹
حتی برای ترور برخی مقامات ۲۸ بمب سنگرشکن به مکان مورد نظر زدند اما اتفاق خاصی نیفتاد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/akhbarefori/654052" target="_blank">📅 22:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654043">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WO1cTwignQyaqfDUsg77CeWShUKcoGXWyiRB8UK12xmLxSUVaqPSCMf6A66fOe2G09Eo_erFaCqvhnls-GkzV2dvKAcCUTDk5AI3X0-S8wwKXeFicVWCMQprp1dQRDOG_D1FeNUWrsWCvcoAUEwiuv_mlEXmMPt77fJnxisnT8RMeZkRabBArtrO8MqfCjj8vDkQtvxgWLqGiBESR4eyjWsj0kdz8ZzQuw7noEjPYk9rlYw3A-2rw1j2K-6rBIRz0RBePs4PevfeWWb8JzQBoGx21cUdQTxlTufG_e_86AtynJQRzrL_Yjp1RTRq5_MdkgI7UlkvQY-b0tHy7V_Pxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1S-WaMhwa9pYWoNZkoUpV0r5UA-4sF48Imc4YImKszX8j_QIYlrL56WeDUy8MTrIki_kdQKGAlkacpEdv1xwt4hCZ69U66Su3Y6RB7Kv3rVydA0g60NhgMSnebvMoS9grbgNqfmHiIMJzr1NA89aC5OB2ZXJV7e8Vemz5M_kopXQ-lnxf54Of1j2I5QOOfZ9owrJkOHyghTTQ-_-OwHsybrF_fVKlW2kSxRejey48hnuMvsl8MmVcRBkKKsXgexe3rz1LWxeMbb1nkIEhwbziD7wSulMisGxGx_mRWYexbmUlB4YdoztvajOP9IIPzOoyC8D_38aP1y5BBVF6Z-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUS9WV2BZAtluD2A8p8uHfjhy6uwT1ezcD3XH9F8qFcgoGW548kCdfQMxe1VY_71g0zC9Z7OlFH_MqNP24uT-7AvNaAyNfYp8pOzRy74Kr2OXNQY-772TlJbCZ-Ubx1xeyk4kg67vX9f1W_2TRSm5QbozIPB9I3WQrqLhWoi1e_lf1vD33FS9-xfhIJQnV4CAxjYHiaeKqCx3QU9n3M69g7d2sEkdgLMNwfMk3IYgSg40rXVDPvWXkJ019mjKpuD6lLeGLn-7l3B68LjnKmZ125I9pYNJ1VfrzATOlDRrsZSXJgt8ZFGJuh1Ty5SdFBEpF1vkBaKm1ZmpqVy9aHLag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GvnDP-VLS9VgzhF2YAdB132TKJN4CPk70Efd5BnTfh-ugjo4vah4uR4O7GiXRBYhrLsNAJA8HTOBYcV_62DvV-CahrrArG7Nv0vlDtu7g65YaX-qKcs42bME3dFwVewgx_mEmnuoXMjZ2zPEX1yyrifYvRgqwyEfBJnoM2bPofmunOsc2vlDFPvpOSmx_ssyqPB7e4Bfv3ZIiUg_ErZxy38IF5VSmp8qPxmFZFjeuOrdZPySmNKN6II0OdU5TcfLxfQ5HhHa50Rf2vX3_0-7J4WrVa0JJtCJpwcmOoGDmr7DosI4RVFTkfssUDtNnD2nWpM3jZjyKt2m6eMre0Y3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcKaGzTZpSUwLXyuApt12K6OGuaimKvLImLqNlfLcrMkSAuWckraRM0lef8IkrMX53JDMAJUjQxL_MZ9vrOWaW1XEtgTzkQwvYZH5C-YjrdnJ1ju8ZrTQNGQKHG65HJDn8LDVGD0_qi_cBy9P2Cwrx_KhT69-c3AhCCeEB2htGt5_gbf25rrtKnmB3B9tpJBKjYL04czn5WgmJLpgpibdOLgmFptycMJS0jvSuZqc-ZXgz2RVmu46ILRJqPlwhUHNfCJU6NwBfwDrezAGVdnv2G9AT6QJqH7t-epIm-gdiSUgFZljjC4goJ_NBqE8h33oAKEBxKMyzfbpjqrxJa-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vaRcr-uDZvUqOaQvvtR6gDpntJc3RXd-btHf_9hkpJy0-wzGPw5ZPwP1UoEoD_5jIBJa0Wzqh2VL6E5hLZGP9mvOygCPKONANcM0N2wXdERemEDuDfsBWWOwuGrDJqTg46Z500bZj2ajUc24GdSkwAFwGwfCrIIX8i8RNq8q9NWZ0x-78RKnkCldlKp2nzo9w0uQ_4Su0WC3SFR6sJ2EUIauYN8F5_FCnOUvL2FzaWZ_-yLrcuNWoK5--YNem4jL51ptf8AhERFexU-N3UoLs4rH2IazpKs7xcaSrzknFuG7nF0NVRk2SWiE_v6xkVBrt2n1kBAnm22-GvYNoDamBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8dq68G_3BxPhP8x76oDZHvqk-Jstv9ta9VqrlG7BOLt1r4pHW80PuK7haKYi4ahWjn5yohGbo-jgIkad6I8PHT94pl3w14aSqrqvC9lC0h5UK1M0ulbrjNS0MKqvUEviC3mYhiTiAFT0Mc_IRxGd5zLuARlz1KrO3tJbvH_81fAkC0dKxHtVgvVWvPwgrt5BASJco3wdl1JQbrZFp0W0SLy0e0nskimRMvoGLycTM3jmSxKs8bm1hbI9kSyo7csCkOZP9yXdQPwKq4e4Z8Gbwu3254Rbqsa_hEBx3cXNyBnkJLEM7SxX52qjIDLUyHHjRSNeYEwB8j5v3BrNjSu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-6-AykO_JJ8JdW1RJnJ1_VLXDJRm373dbSvt4mR6Ya3nu75eFCzRikpCan3ZPchig54T9NHHuN5uQMoJOvkzSiBfMtLN5TUX5mm_x6c3CvDbnjmP6Y_UGIY7H_BAbbncoy23yWhmxhrlXxlewGIyyV-qnln8A7_LLWqcZ1rTC24SWc9Qni_Hib65vg1c_9zb-O-a3WyUzGDEcJVDgAzfPC7AjUX5lWErXzSe00c9H3BHFRvmT2kxLR0USkUZrlc4Wq1T_Y4gb0zlZPsKk30YmKsTzqe7VEDKpBdqv-JhkoCVMtdkjzuTFHdSFE9uZBSuwrSTR5edv8U7g33M7Q22A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LW7ApeF6TBgayyNLPJNA85VqVT6z0U8TQN0UkgiKPvWLyiHAmYKcOoYxBBS4QeMtmuU4MYzjxFDD_0sQHEQPZdVdUXMCthDktLb31rMFvyw8lLSXTgAl_sYQM_y9c7qZ8BV64amY14u7Ln5mELjTAi5K-cb85tDyckG6mhp2GazNSo3CfeAUKa2r-sV6-AlkTXYApHJQpDxDXBiNdBSj9PCbcYP8vdpHIVwyMCzsNUgBSnwcmySsap-ZUCVOfSxXoEivyWF2ycmHzbMQ_kjvthkVkm1iV_npbqXVvhsPTtw0pVHyT19aydwUxccoyeCAU6RNq7FP_EqPLR-pwwFCtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت همدلیِ واقعی
💫
✨
#همدلی
اینجا یک شعار نیست… یک جریان واقعی است.
#هیات_قرار
با همراهی شما مردم عزیز، ۳ رأس گوسفند را قربانی کرده و گوشت آن را  در راستای حمایت از خانواده‌های ایرانی میان خانواده‌های حائز صلاحیت توزیع می‌کند.
این جریان، با شما زنده است
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/akhbarefori/654043" target="_blank">📅 21:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654042">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
گستاخی روزنامه صهیونیست: هیچ تکه کاغذی نمی‌تواند اسرائیل را از حمله به ایران در صورت عبور از خطوط قرمز باز دارد
روزنامه صهیونیستی جورزالم‌پست:
🔹
آنچه ممکن است بیشترین شانس را برای بازدارندگی ایران داشته باشد، احتمالاً هیچ تکه کاغذی (توافقی) نیست. حقیقت تغییرناپذیر این است که اسرائیل آمادگی و تمایل خود را برای حمله سه باره نشان داده است.
🔹
اسرائیل اکنون به وضوح به ایران و منطقه پیام داده که برای جلوگیری از بازسازی تهدید موشکی، حتی به قیمت حملات مکرر در مقیاس بزرگ به خاک ایران، هر کاری انجام خواهد داد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/akhbarefori/654042" target="_blank">📅 21:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654041">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79a8fcba2f.mp4?token=B64rptrlPd4hE8azgT4m8LOqsnKOUeOlj9bU2irAKtWqbwjB21NKIKiR1MSYWvlgVQfzZfLnPA2bFDplYbMQFN3BFFD4o7xMyy1GARBog36m-ILhUThboFtNGK0qLIEf_-rKlKx0YyS3pdHlft30MhvC1_SgWD3ar-C62UVYpeYtibMvohZv1JkGHSB1QXnnEWDNI6AVd2rKy89Bkg4UCATZ1NK2bnNWLWOvUDjVWs7l59jc1TIK2nRcTvbHhBbMe4er93sUKJf1rBHM7BHbLVMlMAFhuis0xfUSGYhl8aJuxDlPfo2_r1-FzSk9OokENG5MxySXuqiw0som7qWwLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79a8fcba2f.mp4?token=B64rptrlPd4hE8azgT4m8LOqsnKOUeOlj9bU2irAKtWqbwjB21NKIKiR1MSYWvlgVQfzZfLnPA2bFDplYbMQFN3BFFD4o7xMyy1GARBog36m-ILhUThboFtNGK0qLIEf_-rKlKx0YyS3pdHlft30MhvC1_SgWD3ar-C62UVYpeYtibMvohZv1JkGHSB1QXnnEWDNI6AVd2rKy89Bkg4UCATZ1NK2bnNWLWOvUDjVWs7l59jc1TIK2nRcTvbHhBbMe4er93sUKJf1rBHM7BHbLVMlMAFhuis0xfUSGYhl8aJuxDlPfo2_r1-FzSk9OokENG5MxySXuqiw0som7qWwLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر ایران تصمیم به پاسخ به تجاوز آمریکایی‌ها بگیرد و جنگ را فرامطقه‌ای کند کدام نقاط زیر ضرب نیروهای مسلح ایران و مقاومت خواهد رفت؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/akhbarefori/654041" target="_blank">📅 21:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654040">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چراغ سبز مجلس برای حضور سردار آزمون در جام جهانی
عباس صوفی، نایب رییس فراکسیون ورزش مجلس در
#گفتگو
با خبرفوری:
🔹
دعوت سردار آزمون باید نظر کادر فنی باشد و در حوزه فنی نمی‌توانیم نظر دهیم و قطعا نظر قلعه‌نویی موثر است.
🔹
سرمایه‌های ملی را باید حفظ کنیم و ممکن است فردی زمانی اشتباهی کرده باشد و بخواهد الان جبران کند. پست خیلی خوبی سردار آزمون گذاشته بود و ابراز اعتقاد به ایران کرده بود و انشالله بتوانیم با نگاه اغماضی، سرمایه‌های کشور را دور هم جمع کنیم.
🔹
آزمون در صورتی که واقعا ابراز ندامت کند و به لحاظ فنی، مورد تایید کادر فنی باشد، می‌تواند به تیم ملی برگردد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/akhbarefori/654040" target="_blank">📅 21:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654039">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21453ebbc9.mp4?token=EAeZZEA18xiZeWUPgyooxLakr_J3hYCJOP2BjFmbAxKzO_BhFxHoZ-VUPoNbHf1Cruivtk0V7N2CO_lxk859eDC1mHfUsAnISs6ShOkK68-b36y39JuWM_pgZFweIkjisoqEvnyObJtgrXBVmjHVSHJB7uGJc0mzV5G_a9wBPyR4vSHGQaHp5RrQYyopvReUFkUyq1x-Llljz1kMzprDvyX6CtAJeX14BDBjnWLeKTnNKma7Evgtz-XDDuaIazmay8hmfdjioJBRzsWAOChik0n44IXoLLJB_goxgbnAxCmiRV9l53SOsnlxpD27y4KL5GtuU5reM8gst8Sg3pKrUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21453ebbc9.mp4?token=EAeZZEA18xiZeWUPgyooxLakr_J3hYCJOP2BjFmbAxKzO_BhFxHoZ-VUPoNbHf1Cruivtk0V7N2CO_lxk859eDC1mHfUsAnISs6ShOkK68-b36y39JuWM_pgZFweIkjisoqEvnyObJtgrXBVmjHVSHJB7uGJc0mzV5G_a9wBPyR4vSHGQaHp5RrQYyopvReUFkUyq1x-Llljz1kMzprDvyX6CtAJeX14BDBjnWLeKTnNKma7Evgtz-XDDuaIazmay8hmfdjioJBRzsWAOChik0n44IXoLLJB_goxgbnAxCmiRV9l53SOsnlxpD27y4KL5GtuU5reM8gst8Sg3pKrUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: اگر ارز را در زمینه کالاهای اساسی اصلاح نمی‌کردیم، مطمئن باشید که الان با قحطی مواجه می‌شدیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/akhbarefori/654039" target="_blank">📅 21:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654038">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
مدیر روابط‌عمومی وزارت ارتباطات خبر داد: رئیس‌جمهور دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/akhbarefori/654038" target="_blank">📅 21:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654036">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96a26c75c6.mp4?token=kJv7TKEuhYGw3_6KJyD4hNuJIrRT02fONa4g4M6vUNzAGD1tVduSyBhbmcJEPOYKkIppeXu8H5vxLwRFPG_bnWYDjt6DKZu8tKO5uR-kRQzR-KHuQkVXKC5E_yrLyZOIUfAcH-U5vS731ibLM3KbSjr2h57JZ0xJQROHjR_SDL5rk2igujwseyqDJz7GDYipANpQ-90PEezfJ1TqDrXWoDCaHUyjNxKxFvIJeRAfOdT058nKLUfERHSnS2TjF_Psn31ooaLDOGneXmrwXWe91c7-MZuQ8lI4CjHSGhMJ5e-9S2gtdYq-ZUMYZT8obMSoUM-08e6bpw3q2trDxAmuDrWXq2IF7bx9H6dLypn0Q9ZYEp5xFGzi-GnzA5bAXIeoXtLfMPmlcedLDOW7AHo0nJfS8CCM5WYdleU0AF5Z-JgzzNKdZVP76y95VHQozoVbG7TnK8I5-VoDhRl30RR5dq9G8tZ9d7IVEB6aJkfrj0GSMJyfT9zO7ImYgCVBXcwDtcoIDcb0acWO8GaEffTl85Dbmhxz1TZCSHoO0lubhk9hO3m73HMFmYEQeIuL9CXW-N7DuRv8g18O3fP-hrEUpvf5pYTXDYKD6LltJmGcpmpmcVDiIojI2P1_UI-4qj9DYd_ctDyAZoXDsXCZzevd23y45Lw_8HKu8g8q7U5d-Q4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96a26c75c6.mp4?token=kJv7TKEuhYGw3_6KJyD4hNuJIrRT02fONa4g4M6vUNzAGD1tVduSyBhbmcJEPOYKkIppeXu8H5vxLwRFPG_bnWYDjt6DKZu8tKO5uR-kRQzR-KHuQkVXKC5E_yrLyZOIUfAcH-U5vS731ibLM3KbSjr2h57JZ0xJQROHjR_SDL5rk2igujwseyqDJz7GDYipANpQ-90PEezfJ1TqDrXWoDCaHUyjNxKxFvIJeRAfOdT058nKLUfERHSnS2TjF_Psn31ooaLDOGneXmrwXWe91c7-MZuQ8lI4CjHSGhMJ5e-9S2gtdYq-ZUMYZT8obMSoUM-08e6bpw3q2trDxAmuDrWXq2IF7bx9H6dLypn0Q9ZYEp5xFGzi-GnzA5bAXIeoXtLfMPmlcedLDOW7AHo0nJfS8CCM5WYdleU0AF5Z-JgzzNKdZVP76y95VHQozoVbG7TnK8I5-VoDhRl30RR5dq9G8tZ9d7IVEB6aJkfrj0GSMJyfT9zO7ImYgCVBXcwDtcoIDcb0acWO8GaEffTl85Dbmhxz1TZCSHoO0lubhk9hO3m73HMFmYEQeIuL9CXW-N7DuRv8g18O3fP-hrEUpvf5pYTXDYKD6LltJmGcpmpmcVDiIojI2P1_UI-4qj9DYd_ctDyAZoXDsXCZzevd23y45Lw_8HKu8g8q7U5d-Q4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاش ترامپ برای کوچک‌نمایی آمار تلفات آمریکا در جنگ علیه ایران
🔹
رئیس‌جمهور آمریکا مدعی شد که در دو جنگ اخیر (علیه ایران و ونزوئلا) ایالات متحده آمریکا مجموعا ۱۳ نظامی از دست داده است.
🔹
این در حالی است که پایگاه اینترسپت چندی پیش در گزارشی افشا کرد که پنتاگون آمار تلفات و خسارت‌های آمریکا را پنهان کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/akhbarefori/654036" target="_blank">📅 21:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654035">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a81erOeAi7uU3it88g6SXjJHof4NhbAeKe3-2M7a_H7FrSaEag8SMw6nHzrzVKapc0CmEQVbrJ98fNGPqNgDK7lUHSdwhv9TuQNxraCmMZkIjJelRF6okw7R5oRLkq_Yx_Jel9N6HH3by2iJulZqegLcjHM1F2Bg_aP1cIIQW6R9V3yX2kRZ09WRHMA9jBSa3aJCscD8OUW_IJXftY-dxOPTx61AApzPL93YbYKNl6cg8pypvkgg7sfUXuxIXaft_irFtFonjRVse_lGlWVzrHXj3-aQyljcj-Zk68UYdTx_xSB6PuFGyxvh7DdG2HE_SHpHuuS5iIVzN-ncNoFiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا استفاده از کتاب‌های فیزیکی در مسیر حذف است؟
🔹
در این نظرسنجی بیش از ۲۴ هزار نفر شرکت کردند که سهم بله ۳۷٪، سهم روبیکا حدود ۶۱٪ و تلگرام ۲٪ بوده است.
🔹
در کل به دلیل افزایش قیمت کتاب، حدود ۸۵٪ خرید کتاب فیزیکی را کمتر کرده‌اند.
🔹
همچنین حدود ۵۰٪ به جای خرید فیزیکی کتاب از راه‌های دیگری به خواندن کتاب مشغول شده‌اند.
🔹
سهم افرادی که افزایش قیمت باعث شده به طور کلی میزان مطالعه‌شان کاهش پیدا کند حدود ۳۴٪ است.
@amarfact</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/akhbarefori/654035" target="_blank">📅 21:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654034">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
اسرائیل به دنبال گسترش عملیات نظامی در لبنان
🔹
شبکه ۱۴ اسرائیل اعلام کرد که نتانیاهو و کاتز( وزیر جنگ رژیم صهیونیستی) درباره گسترش چشمگیر عملیات در لبنان و تایید حملات علیه ساختمان‌ها و منازل مسکونی گفت‌وگو کردند.
🔹
این رسانه عبری تصریح کرد که اسرائیل در خصوص گسترش عملیات نظامی در لبنان با آمریکا در حال رایزنی است.
🔹
طرح صهیونیست‌ها برای گسترش عملیات نظامی پس از آن انجام می‌شود که حزب‌الله به خصوص با کوادکوپترهای انفجاری خود تلفات و خسارات سنگینی به ارتش رژیم وارد کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/akhbarefori/654034" target="_blank">📅 21:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654033">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDhddHwaM33l387OFYAtEDn11KzzqjuE4l5Alh_JhW5pX2CQARbn6OjjIpAiFjpy-aD8_eJqRZouPqH9Fuct0u4ORa03qIsjWuBPKb-IQGzYJ4Q0sTU1DWxJp70hzckj36rZJITpnGHWikB7wJmZn6CMmS_vp0krh0228fp_L9eUBY3U8MArUwuo_Pz-e3I9ElBah9C339jB3YxmDe62MYYoeHtNFpBkMGJRrrXgjoOsZR9px9H7_N9_VniMRUsdc8LySFpj2PyCeqOYiBc6qlmOpYlCxDcVtDnVFiG9l4KP2pCfDOjNBMGdrvRUqTteQ_r4orNRuU0hIOx_xq1Lgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسکن در دهه اخیر سالی ۴۲ درصد گران‌تر شد
🔹
قیمت هر متر مربع خانه که در سال ۱۳۹۵ در تهران حدود ۴ میلیون و ۴۰۰ هزار تومان بود، حالا در اردیبهشت ۱۴۰۵ به میانگین ۱۸۰ میلیون تومان رسیده است.
🔹
نرخ رشد اسمی متوسط سالانه از سال ۱۳۹۶ تا ۱۴۰۴ معادل ۴۲ درصد بوده است؛ یعنی هر سال، قیمت خانه به طور میانگین نزدیک به نصف بیشتر گران‌تر شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/akhbarefori/654033" target="_blank">📅 21:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654032">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گفت و گوى مژده لواسانى با خانواده‌هاى «مردان ناو دنا» در بندرعباس
همسر شهيد ناو دنا: اولين فرزندمان سه ماه ديگر به دنيا مى آيد / اسمش را پدرش در ناو دنا انتخاب كرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/akhbarefori/654032" target="_blank">📅 21:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654031">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
یک منبع در وزارت ارتباطات: مصوبه بازگشت اینترنت به وضعیت قبل از دی‌ماه ۱۴۰۴، دقایقی پیش از سوی رئیس‌جمهور به وزارت ارتباطات ابلاغ شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/akhbarefori/654031" target="_blank">📅 20:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654030">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2FxhmxrDF-Wv9zrPt8F_kEB2oZjPFUvzMlWeujECnsZVpk6jff0LUx8fRzp16ijHemRP5jrEF8jmz4k3ZpIAem4WIOT6TBa6_RhMhG5lxKb1nCFuOC9dNK4smMgCbEgHwX2wtwhtHYh7JKMI0eutVYJCU2ADu4stdYzbAd8dDcDI8AK8jHc63X8553PP60_r3accGoox2SZLJscgN5T-wvikWZHTcGXSXszR1iRPEbC7w_JJZOLxg7Lcc0i5wJPgcpekFfArLb02YJGj-2vMAw-eZdhFbrTUUSnYG8wFbGBCprLyzP1ZqKyRW6NOF_l914_DaH_tOeZpbG-UsEmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربه اصناف از اینترنت پایدار در روزهای بحران
🔹
قطع اینترنت بین‌الملل، ارتباط بسیاری از اتحادیه‌های صنفی با اعضایشان را مختل کرد؛ ارتباطی که پیش از این عمدتاً از طریق پیام‌رسان‌ها و کانال‌های تلگرامی انجام می‌شد. در این شرایط، اینترنت پرو به ابزاری برای حفظ ارتباط پایدار میان اتحادیه‌ها، اصناف و اعضا تبدیل شد.
🔹
اینترنت پایدار، علاوه بر تسهیل ارسال اطلاعیه‌ها و دستورالعمل‌ها، امکان برگزاری جلسات آنلاین، آموزش‌های تخصصی و دریافت سریع بازخورد اعضا را فراهم کرد. فعالان صنفی می‌گویند تجربه هفته‌های اخیر نشان داده دسترسی به اینترنت باکیفیت، دیگر فقط یک نیاز فنی نیست؛ بلکه بخش
ی از زیرساخت ارتباطی و عملیاتی اتحادیه‌ها و کسب‌وکارها محسوب می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/654030" target="_blank">📅 20:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654029">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b41a3263.mp4?token=Jtq8EFhVN_YDj31xBnZFZy3bTcDDQk1M0H6Q0OfvnmPfDlLIBMfV_bcwiLKjHPJ0CKRw9P9O_H_8KWQiDNvsWntuzERNBwGznCOgBzY0BDxbG67iQbCJyWm1flIz_FncBPiMrg6hQztfpzNaIj60hQv9l7FIB_Ti7o8UhALLG_vM8sfxcVvMfipTZVkox7AeLoC65GFJx5mUdPnTo0K8g2d2jh3mDoAPX8Q8oVZmsh9o39n_F7Dyz_WaIsy-nKoCfGCH9GXZJDRXqbk7XFNQ_dn6exaQPIwX1I5DcDmMDUMJMBqU3V7YGqASujvkYWnOMyHOFUYMzZZmuXORAYaXFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b41a3263.mp4?token=Jtq8EFhVN_YDj31xBnZFZy3bTcDDQk1M0H6Q0OfvnmPfDlLIBMfV_bcwiLKjHPJ0CKRw9P9O_H_8KWQiDNvsWntuzERNBwGznCOgBzY0BDxbG67iQbCJyWm1flIz_FncBPiMrg6hQztfpzNaIj60hQv9l7FIB_Ti7o8UhALLG_vM8sfxcVvMfipTZVkox7AeLoC65GFJx5mUdPnTo0K8g2d2jh3mDoAPX8Q8oVZmsh9o39n_F7Dyz_WaIsy-nKoCfGCH9GXZJDRXqbk7XFNQ_dn6exaQPIwX1I5DcDmMDUMJMBqU3V7YGqASujvkYWnOMyHOFUYMzZZmuXORAYaXFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عباس اکبری تروریست: مسلح به کلت بودم و شلیک کردم
🔹
او که در کودتای دی‌ماه ۱۴۰۴ با به ناامنی کشیدن خیابان‌ها به سمت اماکن نظامی و انتظامی اسلحه کشید و تیراندازی کرد صبح امروز به جرم محاربه و اقدام علیه امنیت ملی اعدام شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/akhbarefori/654029" target="_blank">📅 20:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654028">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
لانه عنکبوت اقتصاد ایران
🔹
یک سوم واردات ایران در گرو یک بندر جنوبی در امارات است. ۵۳ درصد صادرات ایران به امارات، سوخت خام. ۱۶ درصد واردات از امارات، ماشین‌آلات صنعتی. این یعنی خط تولید ما دست آنهاست.
🔹
تغییر مسیر یا ماندن در نقطه خطر؟ ویدیو را ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/akhbarefori/654028" target="_blank">📅 20:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654027">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c723e189ec.mp4?token=j0HqQ_75-iclDTY_IV_ulqXhjpF9yCFOE2HIWBkfe9s4lskP3I67AN8a90ff7T4hEeoVYJ-NtcoTVi2hH0B9M5XT4s1T7ZwPmKkXunvNPb-d3x-92Zxp4znH2RsEAHzYCsNxCzoB084P0J2R99iaS8Ulvd9Tjbefqt_5nQKOuDM1HTUek_3udmMa3rMHiyTwbmHzt4ipiTWvjtI92etv1U2YLWCZRRYf0Hru-l9vJCHfWC8e-RfkUiRKjm5cjFClE4gsN2v2Pkmoq38nouTWo0haW_03RgCX7sEzNHxYmJ-282SPUYsdSTETWU2TicLZqK8_bHTytEI9w5HS0AnJ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c723e189ec.mp4?token=j0HqQ_75-iclDTY_IV_ulqXhjpF9yCFOE2HIWBkfe9s4lskP3I67AN8a90ff7T4hEeoVYJ-NtcoTVi2hH0B9M5XT4s1T7ZwPmKkXunvNPb-d3x-92Zxp4znH2RsEAHzYCsNxCzoB084P0J2R99iaS8Ulvd9Tjbefqt_5nQKOuDM1HTUek_3udmMa3rMHiyTwbmHzt4ipiTWvjtI92etv1U2YLWCZRRYf0Hru-l9vJCHfWC8e-RfkUiRKjm5cjFClE4gsN2v2Pkmoq38nouTWo0haW_03RgCX7sEzNHxYmJ-282SPUYsdSTETWU2TicLZqK8_bHTytEI9w5HS0AnJ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان مرشایمر: حمله به ایران بزرگ‌ترین اشتباه تاریخ سیاست خارجی آمریکا است
🔹
نظریه‌پرداز برجسته روابط بین‌الملل و استاد دانشگاه شیکاگو: تصمیم به حمله به ایران در ۲۸ فوریه، بسیار فراتر از جنگ ۲۰۰۳ عراق، به عنوان بزرگ‌ترین خطای تاریخ سیاست خارجی ایالات متحده ثبت خواهد شد.
🔹
این اقدام جنگ‌طلبانه، فاجعه‌بارترین اشتباه استراتژیک واشنگتن در عرصه جهانی است.
🔹
پیامدهای ویرانگر این تصمیم، آسیب‌های جبران‌ناپذیری به نفوذ و جایگاه بین‌المللی آمریکا وارد خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/akhbarefori/654027" target="_blank">📅 20:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654025">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
زخمی شدن ۶ نظامی صهیونیست در حملات امروز حزب‌الله
🔹
رسانه‌های صهیونیستی از زخمی شدن دست‌کم ۶ نظامی ارتش رژیم صهیونیستی با جراحت‌های خطرناک در اثر اصابت پهپاد حزب‌الله خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/akhbarefori/654025" target="_blank">📅 20:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654024">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHcwnqrOd6-yhrPpoh76A-7UFir7LF56YRFSVA60Gok2g79_fznvvsaICWMAR_sV8zctdKxMt_0Kf8zesrUybWEva9Trqi8y86dre-VfPKFJd0miSqnfuFI1NFrGYaaXhHLuF5-yuPLmmTjTw0Qdmj-ntR8OWrpNWosS9kK4m0ZFWSmnbomy13B0CPjnI2AFa4IhtK1EWcf7z-GhtNPbCxxERrjQQrE6OLIW2BHL9kunVN0N6MdDjwYCc8g7B9udHPKn2N3Jv9VcLAkj6DVsIIeCpaSI798sboOEirevdEWkg3lrlBunBsz-aGxuYZKgFAqRuCK0Ha8fRGRrHWYWOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیغام عاصم منیر به چین؛ توافق ایران و آمریکا نزدیک است
خبرگزاری آناتولی:
🔹
همزمان با تشدید تلاش‌های میانجیگرانه اسلام‌آباد بین تهران و واشنگتن، فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان، روز دوشنبه به وانگ یی، وزیر امور خارجه چین، گفت که توافق آمریکا و ایران «در شرف دستیابی است».
🔹
منیر، وانگ را در جریان آخرین تحولات در نقش پاکستان در مذاکرات با هدف کاهش تنش‌ها بین ایران و آمریکا قرار داد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/akhbarefori/654024" target="_blank">📅 20:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654023">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
کابوس شبانه جدید برای صهیونیست‌ها
🔹
با تجهیز FPVهای حزب‌الله به دوربین‌های حرارتی، در حمله صورت گرفته، یک سرباز صهیونیست با موفقیت هدف قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/akhbarefori/654023" target="_blank">📅 20:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654022">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOMxEBTvBDHJRSlmzQkckBZIKumTq1I23nTa62zpd-W4ya_boOB4mwFsOGlEcqHGQTZisUkhLi91lIvo301gBKobw7FfoSLnx340sBEcNpInvEM-jV7PkfSA9cbG_G-_NHxGORgTs7BM3OpeOMbWTfHTjYaGVVP4z4wUlVmW7mffemY50TrAW7QQmXdGhF-f8cvW7RkissnSYz3F0P-WjY453BXOpBbWcTpLHOZgm5dcV2-EwI01QQbMWKCFH6G6Um2P95P95ldQVWKJ72NfpPRcq39gvjQbqd7qmRVe_crUKMyhbs36ij3JMcemQXhreChwUc6hICZXf93ueuuVFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجله آتلانتیک: جنگ ترامپ لنگ‌لنگان به شکستی ناخوشایند نزدیک می‌شود
🔹
جنگ ترامپ با ایران به خاطر فقدان یک راهبرد مشخص و هماهنگ، در حال فروپاشی و حرکت به سوی شکستی خفت‌بار است.
🔹
کار به جایی رسیده که حتی نزدیک‌ترین متحدان و حامیان سیاسی ترامپ نیز از پیامدهای اقتصادی و نظامی آن ابراز وحشت کرده‌اند.
🔹
این وضعیت منعکس‌کننده سردرگمی مطلق کاخ سفید میان ادامه یک جنگ فرسایشی پرهزینه یا تن دادن به توافق‌های تحقیرآمیز است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/654022" target="_blank">📅 20:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654020">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPcXCkTeraHs8_oc8s20hbbBeb4CdoqmVUaxQv0VInwrIyA0KjImPYyxV4wIPIqW_j8Iy-L_1LvRYE_5bC9y8aq14_bP9fJ31SVHXCMne1tWxnOch_618R7OINt2DknyCYAIT4aDtW3uUX_T8oOlfgAjT7ST90RWIWmXCAVH1DPHZo2DT5lHTDZco7PfpTSBwsX6qsLp-aasGjK8OMZ8Xcl7yl1fUpDsxAv-FizXaEiKRZTdqu-MJBb8HKtFPcchtPxuTwXVLXgpqjQ8itgl9YsBwItN9xvr44G8Hy0rkAXznBTFSiCtGPg-cSegNCvfLpdw3kLgRPcgVCaiGDc02g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیر تاریخی شاخص کل بورس در دولت‌های مختلف
🔹
بورس تهران امروز هم در یک روند رو به رشد قرار گرفت، به گونه‌ای که همه شاخص‌های بورس امروز سبز و افزایشی شدند.
🔹
شاخص کل بورس با معیار وزنی ارزشی با افزایش ۸۳ هزار و ۳۵۲ واحد به رقم ۳ میلیون و ۹۹۳ هزار و ۱۴۲ واحد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/akhbarefori/654020" target="_blank">📅 19:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654019">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3LBbsxRa2Jy_uoe4Wch8nO8DEZ0kwgukXR1zvobji4lgdnityxXsyg9nSIf2h30-Mkof5L_tUsFXCsD_w5klcBWD2ghdKxq2LjcnGk7tP-QKH2lMuZt3Z8QhWXT5NfNFbLVfK8JekXZ3CLOlKVhW29m9KvYQlCeQndonItuHeRBY1DNcmVslBPrgSSgurnvE_tLD_Fbv-_ceeON5wK8p8SxUu9qZa_h2GVxmYI94X6Tanz6e5wtSWpI1KvIJX8G7rlHhQi-7EM6CDHxh9ej2auhwHptd9XuyxgNTKewUh53j0Ek2uiQyOr5t97lA53CzUsdATs_bEI3fKLH_oASVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران یک‌پنجم ناوگان پهپادهای ریپر آمریکا را نابود کرد
🔹
ارتش آمریکا از زمان آغاز درگیری با ایران ۳۰ فروند پهپاد MQ-۹ Reaper را از دست داده است که نزدیک به یک‌پنجم کل ناوگان پیش از جنگ واشینگتن را شامل می‌شود و ارزش آن نزدیک به ۱ میلیارد دلار برآورد شده است.
🔹
به گفته ژنرال دیوید تیبور (معاون رئیس ستاد برنامه‌ریزی پنتاگون) ناوگان ریپرهای آمریکا که دیگر تولید نمی‌شوند، اکنون به حدود ۱۳۵ فروند کاهش یافته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/akhbarefori/654019" target="_blank">📅 19:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654017">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6vasdUCBvdaPGCr6pXdEinNbXFm8jj373r3qMuJ-Q2KKE3DFZHAKpFGxCvtHAaj6vzOMCT5KFr0bvNCJm2iyjoqEW4GJWLn2qqUkamjyKsK54GoPru8u4urbZgA8MA1_qwZefIWxciaDLN0RM8sQjo13WyaMeHXZayG0lWNcebfDyBGtrFMwWxVxT-u4e6uOLuzIJwWXW5NdaLUaBhC2duk-FxFFJXDkliysjMoKBVb4yO5z9JWvaAxWUA-8bybtEFXVTNLgvUsEBTH5fTkLn6HMW_7QI0oo0v7XuAmQmeOyiYLmZ3obCNHXNSVHcTlcZv25jWhlUBgozXHnAKaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ بار دیگر به ایران حمله می‌کند؟ / ۵۴درصد شرکت‌کنندگان در یک نظرسنجی پیش‌بینی کرده‌اند: بله!
شما هم کامنت بگذارید و درباره شانس جنگ یا توافق نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3217351</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/akhbarefori/654017" target="_blank">📅 19:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654016">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUJwvQ_QUnLHbYYK2FcVFkZRTEI4CbFHiJdXmG4tnuFzznvaX0WEsYOhlnD5dodvI_8ICq5b8G3-D0qTJcmkLCoZBy-l-DAURrIluBeUguIUhj8dkMFuJb3gw_qyS1o1aVAppKW3vPNfqyunjvpnsoiJa03OAqhpMyXyvukxdwCGwZuMi_6s-k51ZJzUW5oVvDyEW9ZAMJiUtQligEH6JT_5EY7OPX1H8mAduh3gMR1-SNHK3zCiPb4TD7D7OBjLzhwppdXzkkvxlO-hS0X8kMP-dcZMIle-i_7eMzq1Xeg_sCWNZbPq1KtnMj0cr7gqK4OI1rtu0qqUMMBrhsGODw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین پیام دبیر شورای عالی امنیت ملی به مردم عزیزِ ایران؛ عقب نشینی در‌ کار نخواهد بود
▪️
"عقب نشینی در‌ کار نخواهد بود"
▪️
این را میدان نظامی، میدان دیپلماسی و مردم مبعوث شده حاضر در خیابان با مقاومت جانانه خود نشان دادند و دشمن را زمین گیر کردند.
▪️
حالا بیش از هر زمان دیگر کشور نیاز به وحدت و انسجام دارد تا آمریکایی‌ها و صهیونیست‌ها در این زمینه هم مأیوس شوند.
▪️
میدان وحدت و انسجام هم یک میدان دیگر در مبارزه است. تلاش همگانی برای جلوگیری از هر سخن و اقدام وحدت‌شکن، ایرانِ عزیز را به پیروزی نهایی خواهد رساند؛ ان‌شاءالله.
▫️
محمدباقر ذوالقدر | دبیرشورای عالی امنیت ملی | ۴ خردادماه ۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/654016" target="_blank">📅 18:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654015">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
غریب آبادی: واشنگتن باید توضیح دهد چگونه دادگاه را با موشک جایگزین کرده است
🔹
معاون وزیر امور خارجه: در ماه‌های اخیر، ارتش آمریکا در کارائیب و شرق اقیانوس آرام، ده‌ها قایقِ مظنون به قاچاق مواد مخدر را هدف حملات مرگبار قرار داده؛ عملیاتی که نزدیک به ۲۰۰ کشته برجا گذاشته، بی‌آنکه بازداشت یا دادرسی عادلانه ای در کار باشد یا افکار عمومی از ادله و هویت قربانیان آگاه شود.
🔹
اکنون، یک بررسی محدود درون‌سازمانی در پنتاگون ناگزیر شده به روند این حملات بپردازد؛ اما پرسش اصلی فراتر از پروتکل‌های هدف‌گیری است: آیا یک دولت می‌تواند در خارج از میدان جنگ، «ظن» را به حکم مرگ تبدیل کند؟
🔹
مبارزه با قاچاق مواد مخدر مسیر حقوقی دارد: تحقیق، بازداشت، ارائه ادله، و برگزاری دادگاه و دادرسی عادلانه. شلیک به انسان‌ها در دریا، بدون محاکمه و بدون شفافیت، چیزی جز قتل فراقضایی نیست؛ همان نقطه‌ای که نقاب حقوق بشر از چهره مدعیان آن کنار می‌رود.
🔹
واشنگتن که سال‌ها برای دیگران نسخه حقوق بشر نوشته، باید توضیح دهد چگونه دادگاه را با موشک، و قانون را با مرگِ بدون محاکمه جایگزین کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/akhbarefori/654015" target="_blank">📅 18:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654014">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d47069e70.mp4?token=QK6hh3yAktQhbz2Th11idiKN57v_zVg2xfwVqH3QHm1ZYeVUdk2V3ORGEP4XlessFYYK1IB4Nd7vKH9vCNflZn611peSWjLe3ftJVxdA5Ar2xN_Wf-y6COEnfGyvh0m1klF1JltqZurB4GSqz6B4wFx3RtiMG1yZkv1zIHWxfGg08h8BTy_t1jYlVqR1k6qGcEfW2ezvd9UGozaCtTv-Y6stuwPppGD3j0aFaYY7VPBXQhDZAjmE3M2EPOS59Y6ix6gr_ddcGmBd6-vdR3IaKg2gMBnmSGTSwrQAutlyUAgm4QvtbivKhiChMlePmaDNt7QUIMoUpHlFLwcDjZAXyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d47069e70.mp4?token=QK6hh3yAktQhbz2Th11idiKN57v_zVg2xfwVqH3QHm1ZYeVUdk2V3ORGEP4XlessFYYK1IB4Nd7vKH9vCNflZn611peSWjLe3ftJVxdA5Ar2xN_Wf-y6COEnfGyvh0m1klF1JltqZurB4GSqz6B4wFx3RtiMG1yZkv1zIHWxfGg08h8BTy_t1jYlVqR1k6qGcEfW2ezvd9UGozaCtTv-Y6stuwPppGD3j0aFaYY7VPBXQhDZAjmE3M2EPOS59Y6ix6gr_ddcGmBd6-vdR3IaKg2gMBnmSGTSwrQAutlyUAgm4QvtbivKhiChMlePmaDNt7QUIMoUpHlFLwcDjZAXyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شرایط دریافت بیمه بیکاری تسهیل شد
🔹
وزیر تعاون، کار ورفاه اجتماعی: شرط بارگذاری کارت پایان خدمت و مدرک دانشگاهی برای دریافت بیمه بیکاری حذف شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/654014" target="_blank">📅 18:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654013">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyFCg0yTBaQ4i1AVet9sIGrUDNtbBXJBiSsdHd0p-pdUlgqXwb9Z03ZactpiB3SHUKDQ8VljCjnlMadgp51i2H9FESnbJfALD66xUfoNxqZCKa0EjLFKRYIVBRBCjGkSsyzA12_OooOvCo6ScUMO3GLSSy391uYt7i7z29zC5g75fNsbJBsQ-vBOgkqMDQevgAe_1lUJA7MiXSHZKN-GNR3YOIPnJsdRAciFtJHYhPjMO8ZKZYUT3K3z_rb5f1o0IQkjvcTHkV-I-K4-BksX_Dop9Svk5Fwa9bfnHGwpBGDLqZptkXBxc9jGRVw3_MYKc-_xvUkB5KyV7I8oM7pDNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت‌های جدید لبنیات اعلام شد
🔹
دبیر انجمن صنایع لبنی از افزایش قیمت ۴ قلم پرمصرف لبنی خبر داد:
🔹
شیر نایلونی: ۸۴ هزار تومان
🔹
شیر بطری: ۹۸ هزار تومان
🔹
پنیر یواف ۴۰۰ گرمی: ۲۰۳ هزار تومان
🔹
ماست دبه‌ای ۲ کیلویی: ۲۲۸ هزار و ۷۰۰ تومان
🔹
هفتهٔ گذشته نیز قیمت شیر خام با افزایش ۲۹ درصدی به کیلویی ۶۰.۵۰۰ تومان رسید.
🔹
گفته‌شده انجمن صنایع لبنی و سازمان حمایت برای افزایش قیمت‌ها به‌صورت لفظی توافق کرده‌اند و هنوز ابلاغ رسمی صورت نگرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/654013" target="_blank">📅 18:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654012">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b1019673.mp4?token=AQxggCCmY4uwhHM3NmiOKKbfvmGayDgYNNtJn5cUn-kbjH2KeTR7yDIMBIp128MuN7qtgWcnL08jbNdsn3PkBL7rzSPXQkyZ2VjFHoh0W3erShFJHKxXLC19f5fzPJcVnemckqQ8om6sPcUYx2blATSGxecTpWlhCmswFfAMWkryheHzHdhmm3VWb4yXaftneCcqEbrL4PZF9VfqfcxOR3EK79X9vkK0GqpQ5DUsdAx82KnIMi5SDvRw66VDMrPPhkEDeuGm_FV337bNwW3YN8mF7Yqf4-GyO3Bp7FoMSjB_jXpujcmXxe2mhwRHWJogt3OIbQNh5CVXgNfeMjuj_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b1019673.mp4?token=AQxggCCmY4uwhHM3NmiOKKbfvmGayDgYNNtJn5cUn-kbjH2KeTR7yDIMBIp128MuN7qtgWcnL08jbNdsn3PkBL7rzSPXQkyZ2VjFHoh0W3erShFJHKxXLC19f5fzPJcVnemckqQ8om6sPcUYx2blATSGxecTpWlhCmswFfAMWkryheHzHdhmm3VWb4yXaftneCcqEbrL4PZF9VfqfcxOR3EK79X9vkK0GqpQ5DUsdAx82KnIMi5SDvRw66VDMrPPhkEDeuGm_FV337bNwW3YN8mF7Yqf4-GyO3Bp7FoMSjB_jXpujcmXxe2mhwRHWJogt3OIbQNh5CVXgNfeMjuj_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر نفت: باید عرضه بنزین کشور را بطور خاص مدیریت کنیم و در تلاشیم تا تاسیسات آسیب‌دیده به سرعن به مدار تولید بازگردد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/654012" target="_blank">📅 17:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654011">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ffe5cedf4.mp4?token=khY4pDpmgXXiPXp2gY6gXhyZ5LPoasWHVxY4WCTkFnJ8XEiqNN7KICtVtLOOejbId4IT3TJq5rltQ4dPeRpI6izVPLFUOKxQ8oEx0MGBZX35gefMleEX-lpyWdB7N2m-s0_f-AAMJ58dzoagm5nNphax2Y7CDgVayH4RPc8M-OAT61vsPchP5DALLTxtoEEEiObM2h0_FYEnX3xGTmTolXy0KosU8xZiex7efRQMc1tvYnNuX__lchMPdI3YhGFb4I8CULG6ZYJdx39jM1q2a6wCmaAY4zoFQIMYZlDocbWZqZMrMUdoJRe1hABwt_-NXnRAINjXcFzOT-A9TzqpKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ffe5cedf4.mp4?token=khY4pDpmgXXiPXp2gY6gXhyZ5LPoasWHVxY4WCTkFnJ8XEiqNN7KICtVtLOOejbId4IT3TJq5rltQ4dPeRpI6izVPLFUOKxQ8oEx0MGBZX35gefMleEX-lpyWdB7N2m-s0_f-AAMJ58dzoagm5nNphax2Y7CDgVayH4RPc8M-OAT61vsPchP5DALLTxtoEEEiObM2h0_FYEnX3xGTmTolXy0KosU8xZiex7efRQMc1tvYnNuX__lchMPdI3YhGFb4I8CULG6ZYJdx39jM1q2a6wCmaAY4zoFQIMYZlDocbWZqZMrMUdoJRe1hABwt_-NXnRAINjXcFzOT-A9TzqpKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوتی‌های عجیب خبرنگار ایران اینترنشنال در پخش زنده سوژه کاربران فضای مجازی شد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/654011" target="_blank">📅 17:05 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
