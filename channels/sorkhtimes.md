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
<img src="https://cdn4.telesco.pe/file/rT9ez1sDyVwCNaJL4euz_r-qKRZM5pgGc49ha5UWGmx6d0wEKp_7UhhfbtddSCeJF0jID4RaN1P2hb_L8FCUgTYarU_7QXB-l9PL07g8sleurcEqniD4PHaE2IElXHKHET0gByZulyZPs8dfU5yfDjUmylW1V_5VjwcqLF6LU_5YxvH1YYKrA3ZUa05lA24a81bbVlmA4XROwZSHdRcOMBxbmMRuRPVzjQSg8X_uqD3V9xoFmHa-vx1qfa2FLXnBBU110r_tnnAYb4VP8RvrJrrk7O2JH8mszq5yfvPDg4SFws7N8gSlqejBECuZhEI0qAqHPgmSUQvQDCymwCiT1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 13:52:58</div>
<hr>

<div class="tg-post" id="msg-131560">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔰
سرویس VIP
🔰
5 گیگ 1.4T
10 گیگ 2.4T
20 گیگ 3.6T
40 گیگ 5.7T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 199 · <a href="https://t.me/SorkhTimes/131560" target="_blank">📅 11:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131559">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEi-TcOro0nCr3aq_cWdXAkZ-rjtP9ev5lGmQaRh-pFwif3jDIwqSj8l9kzmhM8BoqkSUDQ2xNL-GLpk3BmN8oVHgA_Ei9roAz4vBNY8wrPz2RCTlWTNTQFa--Rctc7Ty20SNc2ox-SFbCy9VUkPD-eBR5IJJ0v02K2Dc0t4TO2clpIZIdns05EPcRGTQSzt-054eDhXQOQeDz0NY1m6h_TcFSVUW09uUiC5WHi25pZPxji4O83jkeUJTB28tnXGyXmlLtxMFgIB2IlSVIXrErMi8LDmyAuaknO0ntX5UZ_3KY_AsQ4hH-MK5RMsMqxRJ2HCOzDsA4B6-IKS-c_eCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
دسترسی سریع به سایت وینکوبت
✅
کاربران عزیز، برای ورود آسان و بدون دردسر به سایت وینکوبت، می‌توانید از ربات رسمی استفاده کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔹
ورود سریع و مستقیم به سایت
🔹
بدون نیاز به جستجوی لینک‌های مختلف
🔹
دسترسی راحت از داخل تلگرام
📌
همه چیز به ساده‌ترین شکل ممکن داخل ربات برای شما کاربران محترم فراهم شده.
🔗
اگر دنبال یه راه مطمئن و سریع برای ورود هستید، ربات وینکوبت بهترین انتخاب شماست:
🤖
@Wincobet_bot
🔗
برای دریافت تحلیل بازی‌ها و اطلاع از آخرین بروزرسانی‌ها، به کانال رسمی وینکوبت بپیوندید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 497 · <a href="https://t.me/SorkhTimes/131559" target="_blank">📅 01:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131558">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔰
سرویس VIP
🔰
5 گیگ 1.4T
10 گیگ 2.4T
20 گیگ 3.6T
40 گیگ 5.7T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 464 · <a href="https://t.me/SorkhTimes/131558" target="_blank">📅 01:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131557">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_H9jgJWkI_RKGTiyBYfH8F4K3H5q-ntgPdfSXDl_G3UWgGhHBfaXxYgQZSgNKDyEMCdCVZcUEboH0qG02caWvseqmCk9jAvJTLMz1aOf44RSBMwgra8WCzmAgLJnnnlw6xCqh81Pz1mu_q3_5ZcTMIuNsZVmeIz_Ow92Ir-jbWl2CVtODshBJtme3AMcV7qiFcXMlBzRAp8akWCrWeuTNHsh7cA_6CffeQ6LbvsCPzqu2JTNEojqA4FaIDM-WTFMLmH8Hu_mTxRQy6b5M0gAabb4OO9GZAK4lV9LU9EbwQ6hqn-A_oN4PIVG214z_gl9AawjYNOK1oSGftKG409BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سپاهان مجوز حرفه‌ای می‌گیرد؟
🔺
کنفدراسیون فوتبال آسیا (AFC) به درخواست فدراسیون فوتبال ایران برای تعویق در معرفی نمایندگان این کشور در رقابت‌های آسیایی پاسخ منفی داده است. این موضوع به شدت بر وضعیت نمایندگان ایران در لیگ قهرمانان آسیا تأثیر خواهد گذاشت. سپاهان،…</div>
<div class="tg-footer">👁️ 511 · <a href="https://t.me/SorkhTimes/131557" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131556">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🟡
سپاهان مجوز حرفه‌ای می‌گیرد؟
🔺
کنفدراسیون فوتبال آسیا (AFC) به درخواست فدراسیون فوتبال ایران برای تعویق در معرفی نمایندگان این کشور در رقابت‌های آسیایی پاسخ منفی داده است. این موضوع به شدت بر وضعیت نمایندگان ایران در لیگ قهرمانان آسیا تأثیر خواهد گذاشت. سپاهان، یکی از باشگاه‌های مطرح کشور، به دلیل مشکلات مالی و عدم توانایی در تأمین شرایط لازم برای دریافت مجوز حرفه‌ای، در معرض خطر قرار دارد.
🔺
بعد از آسیب جدی به کارخانه فولاد مبارکه، سپاهان با مشکلات مالی جدی رو به رو است و هنوز نتوانسته مطالبات این فصل بازیکنانش را تسویه کند و احتمالا هم با توجه به میزان خسارات وارده، حداقل تا پایان سال بعد، قادر به تسویه طلب مربیان و بازیکنان داخلی و خارجی اش نخواهد بود که همین موضوع قطعا بر روند مجوز حرفه این تیم تاثیر منفی خواهد داشت.
🔺
از سوی دیگر شرایط اقتصادی صنایع مادر باعث شده وزارت صمت نیز محدودیت‌هایی برای هزینه‌کرد باشگاه‌های صنعتی در نظر بگیرد؛ موضوعی که می‌تواند برای سپاهان، گل‌گهر و چادرملو دردسرساز شود.
🔺
نکته قابل توجه دیگر هم این است که با توجه به وضعیت منطقه و کارشکنی مسبوق به سابقه از سوی کشور های حاشیه خلیج فارس
،
قطعا بازی ها به سمتی خواهد رفت که رنگ بوی ورزشی نخواهد داشت و این بازی ها یک میدان است برای دفاع از نام و اعتبار ایران و حفظ ابروی ایران بسیار مهم است.
🔺
در این شرایط، انتخاب نمایندگان مناسب برای حفظ اعتبار فوتبال ملی اهمیت ویژه‌ای دارد، تصمیمات فدراسیون، در روزهای آینده می‌تواند سرنوشت فوتبال ایران را رقم بزند و بر روند آینده باشگاه‌ها تأثیرگذار باشد/ایران ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 519 · <a href="https://t.me/SorkhTimes/131556" target="_blank">📅 00:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131555">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
فوری ؛ ایران به شورای امنیت سازمان ملل اطلاع داده است که در صورت اعزام زیردریایی هسته‌ای آمریکا به خاورمیانه، سطح غنی سازی ۱۰ تن اورانیوم باقی مانده را به ۶۰ درصد خواهد رساند
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 657 · <a href="https://t.me/SorkhTimes/131555" target="_blank">📅 00:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131553">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
🎙
میثاقی: امیرحسین محمودی با 5 بازی لیگ برتری جوری درخشیده که الان داره میره جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 686 · <a href="https://t.me/SorkhTimes/131553" target="_blank">📅 00:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131552">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
محمد انصاری که در تیم جوانان ایران به عنوان یکی از دستیاران حسین عبدی فعالیت می‌کرد هم اکنون یکی از گزینه‌های جانشینی او در این تیم هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 689 · <a href="https://t.me/SorkhTimes/131552" target="_blank">📅 23:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131551">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
میثاقی: کارهای اعزام تیم ملی به آمریکا برای حضور در جام جهانی در حال انجام شدن است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 674 · <a href="https://t.me/SorkhTimes/131551" target="_blank">📅 23:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131549">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🛜
معاون رئیس‌جمهور: نظر دولت بازگشت اینترنت به وضعیت عادی است
🔹
حتی در شرایط جنگی هم بستن اینترنت راهکار درستی نیست، چرا که دیدیم وقتی اینترنت کامل بسته بود هم ترورها ادامه داشت
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 784 · <a href="https://t.me/SorkhTimes/131549" target="_blank">📅 18:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131548">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
ترامپ:آنها تسلیم خواهند شد... من با آنها معامله خواهم کرد تا زمانی که به توافق برسند.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 759 · <a href="https://t.me/SorkhTimes/131548" target="_blank">📅 18:32 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131547">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
ترامپ:
آنها تسلیم خواهند شد... من با آنها معامله خواهم کرد تا زمانی که به توافق برسند.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 695 · <a href="https://t.me/SorkhTimes/131547" target="_blank">📅 18:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131546">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔰
سرور یک ماهه Open VPN فقط تلگرام نامحدود ۱۳۰۰ هزار تومن
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 699 · <a href="https://t.me/SorkhTimes/131546" target="_blank">📅 18:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131544">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFmXfh_SUE1wPkgcJNX7ncynEeY4ar8j1_N2Kbw33K8-DAm6EkRC0gTvVLxWiGbWNEKT0gHp3AevNDpcOEVpwe_OP-_rhdpo9TouGIlOioDQl-n_OLDnUWPrpy_B92zTqbQhxUYkFTWgm-Uz3uqdV4Bom4J2okk_TkU2bp9fTK-PCBodR1qg8YIoWrcwcWJl9J6WsdUmONq-N1CIbomZd2qODpUprFxqgJg4LrHwAB8qDQ_e0XR4Hf38k0iu5SZ9Vdd-nIWKL98nsFIH66r3pnkirTtSddcKvQqKxitDHuTPs8B3-Zznu7tG0j09jj4yjjK8G72duCvA6kUmOL0jSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 694 · <a href="https://t.me/SorkhTimes/131544" target="_blank">📅 17:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131543">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
سروش رفیعی فعلا قصدی برای بازگشت به ایران نداره؛ حتی اگر تمرینات پرسپولیس بار دیگر از سر گرفته شود!//خرمی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 678 · <a href="https://t.me/SorkhTimes/131543" target="_blank">📅 16:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131542">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
سروش رفیعی فعلا قصدی برای بازگشت به ایران نداره؛ حتی اگر تمرینات پرسپولیس بار دیگر از سر گرفته شود!//خرمی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 687 · <a href="https://t.me/SorkhTimes/131542" target="_blank">📅 16:32 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131541">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
سپاهان  اصفهان دچار کمبود بودجه برای فصل آینده شده و از این رو قصد دارد آریا یوسفی را به فروش برساند تا بخشی از هزینه‌های فصل آینده را تأمین کند. ///خرمی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 628 · <a href="https://t.me/SorkhTimes/131541" target="_blank">📅 16:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131540">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
سپاهان  اصفهان دچار کمبود بودجه برای فصل آینده شده و از این رو قصد دارد آریا یوسفی را به فروش برساند تا بخشی از هزینه‌های فصل آینده را تأمین کند. ///خرمی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 637 · <a href="https://t.me/SorkhTimes/131540" target="_blank">📅 16:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131539">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">📍
محسن خلیلی، معاون ورزشی پرسپولیس:
هیچ فردی به کادرفنی اضافه نمی شود/ محمدی و رفیعی بازیکنان ما هستند
🎙
لیست مازاد در پرسپولیس شایعه است چون ما هنوز ۸ بازی دیگر داریم. میلاد محمدی و سروش رفیعی بازیکنان ما هستند و چون در تمرین غایب بودند جریمه شدند
🎙
با شروع تمرین در خدمت آنها هستیم. سروش رفیعی یکی از کاپیتان های ماست و حتما مسئولیت پذیری او باعث می شود در تمرین شرکت کند
🎙
از یک ماه قبل از شروع مسابقات تمرین را شروع می کنیم. در حال حاضر هیچ فردی به کادرفنی اضافه نمی شود. برای مجوز حرفه ای شرایط خوبی داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 627 · <a href="https://t.me/SorkhTimes/131539" target="_blank">📅 16:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131538">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
🟡
نتیجه‌ای تصادفی یا سناریویی از پیش طراحی‌شده؟
▪️
سپاهان در دیدارهای اخیر خود نتایج عجیبی را ثبت کرده است: تساوی برابر گل‌گهر (دو بار)، شکست مقابل تراکتور و پرسپولیس، و بردهای حداقلی برابر چادرملو و دیگر تیم‌ها. این آمار بیش از آنکه تابع منطق فنی باشد، روایتی متفاوت از لیگ برتر را به تصویر می‌کشد.
▪️
در پشت پرده، پرسپولیس سیاستی شفاف اما بحث‌برانگیز را دنبال می‌کند،تثبیت سهمیه آسیایی خود، به شکل ممکن فوتبالی. برخی فعالان فوتبالی بر این باورند که هدف اصلی از برگزاری لیگ چیزی جز این نیست و نتایج اخیر تیم‌های مدعی در برابر سپاهان، نشانه‌هایی از یک طراحی نانوشته را به هواداران نشان می‌دهد.
▪️
اکنون باید پرسید: تکلیف معرفی نمایندگان آسیا چه خواهد شد؟ اگر قرار باشد تیمی با لابی و سیاست‌گذاری راهی قاره شود، احترام به ماهیت رقابت‌پذیری فوتبال کجا خواهد رفت؟ فوتبال ایران سزاوار شفافیت است، نه سناریوهایی که اعتبار مسابقات را زیر سوال می‌برند.
🔺
سپاهان ۱ استقلال ۲
🔺
سپاهان ۱ تراکتور ۲
🔺
تراکتور ۱ سپاهان ۰
🔺
گل گهر ۱ سپاهان ۱
🔺
سپاهان ۱ گل گهر ۱
🔺
سپاهان ۱ چادرملو ۰
🔺
سپاهان ۰ پرسپولیس ۱
🔺
پرسپولیس ۲ سپاهان ۱
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 642 · <a href="https://t.me/SorkhTimes/131538" target="_blank">📅 16:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131536">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
بزیک، مدیرآکادمی باشگاه پرسپولیس و سوال در مورد همکاری با مهدی مهدوی کیا: من با مهدوی کیا مثل برادر هستیم و شروع کار ما در کیا با هم بودیم/ او اکنون با تیم بزرگسالان در امارات کار می کند/ لازم باشد حتما با مهدی مهدوی کیا کار می کنم و از تجربیات او استفاده می کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 602 · <a href="https://t.me/SorkhTimes/131536" target="_blank">📅 15:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131535">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
🟡
حذف سپاهان و سفر پرسپولیس به آسیا
🔺
فرمول جدیدی که از سوی مسئولان چند باشگاه ارایه شده، احتمال حذف سپاهان از بین نمایندگان فصل آینده فوتبال ایران را تقویت کرده و استقلال، پرسپولیس و تراکتور را راهی لیگ‌های آسیایی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 629 · <a href="https://t.me/SorkhTimes/131535" target="_blank">📅 15:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131534">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
محسن خلیلی: پرسپولیس
همیشه خواهان جذب
علی قلی زاده
بوده اما خودش نمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 616 · <a href="https://t.me/SorkhTimes/131534" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131533">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
دیگه لازم نیست دنبال لینک سایت بگردی!
📌
فقط با یه کلیک از داخل ربات وارد وینکوبت شو:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
سریع، مستقیم، بدون دردسر
📌
بدون نیاز به جستجو یا لینک‌های پراکنده
📌
همه چیز داخل ربات آماده‌ست:
▪️
ورود فوری به سایت
▪️
دسترسی راحت از تلگرام
▪️
بدون مراحل پیچیده
🔗
ساده‌ترین راه ورود به وینکوبت همینجاست:
🤖
@Wincobet_bot
📌
میخوای با تحلیل جلوتر از بقیه باشی؟
برای دریافت آنالیز بازی‌ها همین الان جوین شو
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 615 · <a href="https://t.me/SorkhTimes/131533" target="_blank">📅 15:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131530">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">📍
محسن خلیلی، معاون ورزشی پرسپولیس:
🎙
باشگاه برای توسعه آکادمی برنامه بلند مدت دارد. از شاهرودی بابت زحماتی که کشیده تشکر می کنیم. امیدواریم ریل گذاری که در آکادمی شکل گرفته ادامه دهیم
🎙
امیدواریم بازیکنی مثل امیرحسین محمودی را پرورش دهیم. سرپرستی در پرسپولیس؟ فعلا تا پایان فصل در خدمت هستم. برای پایان فصل و فصل جدید حتما در مورد سرپرستی تصمیم گیری می شود
🎙
جلسات ما با اوسمار هر چند روز انجام می شود. چهار روز قبل تماس تصویری با اوسمار داشتیم که در مورد شرایط جدید با او حرف زدیم. در مورد مصدومیت براجعه با هم حرف زدیم. اوسمار منتظر تصمیم سازمان لیگ است
🎙
او گفته در صورت شروع لیگ از اواخر تیر تمرینات از هفته اول خرداد شروع شود. جلساتی خوبی با سازمان لیگ داشتیم تا ببینیم بازی ها چه زمانی آغاز می شود. حضورم در معاونت ورزشی و سرپرستی وظیفه ای است که مدیریت به عهده من گذاشته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 636 · <a href="https://t.me/SorkhTimes/131530" target="_blank">📅 13:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131529">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">📍
محسن خلیلی، معاون ورزشی پرسپولیس:
🎙
در مورد نیم فصل که بازیکن خوب جذب نشده باید بگویم که سرگیف را جذب کردیم. وقتی نیم فصل بازیکنی جذب می شود اکثرا قرارداد دارند. بازیکن آزاد در نیم فصل کم است
🎙
یکی از شروط ما برای جذب بازیکن این بود که در فصل گذشته حداکثر بازی ها را کرده باشد. مذاکرات خوبی برای پرسپولیس داشتیم اما شرایط کشور باعث شد تا نتوانیم لیست اولیه خود را جذب کنیم. فرزین معامله گری بازیکن با استعداد است و در سه پست می توانیم از او استفاده کنیم
🎙
دنیل گرا را هم با توجه به موجودی های بازار و تایید اوسمار جذب کردیم. بارها گفتیم نقل و انتقالات با هماهنگی کادرفنی انجام شده است. در مورد نیم فصل که بازیکن خوب جذب نشده باید بگویم که سرگیف را جذب کردیم
🎙
وقتی نیم فصل بازیکنی جذب می شود اکثرا قرارداد دارند. بازیکن آزاد در نیم فصل کم است. یکی از شروط ما برای جذب بازیکن این بود که در فصل گذشته حداکثر بازی ها را کرده باشد
🎙
فرزین معامله گری بازیکن با استعداد است و در سه پست می توانیم از او استفاده کنیم. دنیل گرا را هم با توجه به موجودی های بازار و تایید اوسمار جذب کردیم
🎙
بارها گفتیم نقل و انتقالات با هماهنگی کادرفنی انجام شده است. ما همیشه گفتیم عدالت باید در بحث قهرمان این فصل رعایت شود. ما به سازمان لیگ گفتیم از کجا میدانید پرسپولیس تا آخر فصل در رده ششم باقی می ماند؟
🎙
اگر گفتم عدالت را می خواهیم باید جدول نیم فصل اول لحاظ شود که همه تیم ها با هم بازی کردند. امیدواریم تصمیمی گرفته شود که به نفع تیم هایی باشد که شانس حضور در آسیا را دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 686 · <a href="https://t.me/SorkhTimes/131529" target="_blank">📅 13:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131527">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🟢
هنوز برای ورود به سایت دنبال لینک می‌گردی؟!
✅
دیگه وقتشه ساده‌تر وارد شی و با ربات وینکوبت، فقط با یه کلیک مستقیم وارد سایت شو:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
⚡️
بدون دردسر و اتلاف وقت
⚡️
بدون لینک‌های پراکنده
⚡️
ورود سریع از داخل تلگرام
⚡️
همه چیز داخل ربات برات آماده‌ست؛ سریع، راحت و بدون پیچیدگی.
🔗
اگر میخوای بدون معطلی وارد سایت بشی، از اینجا شروع کن:
👇
🤖
@Wincobet_bot
🟢
تحلیل بازی‌ها و آپدیت‌های مهم رو از دست نده:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 786 · <a href="https://t.me/SorkhTimes/131527" target="_blank">📅 04:02 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131525">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
صدا و سیما: ایران آخرین پیشنهاد آمریکا را رد کرده است.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 746 · <a href="https://t.me/SorkhTimes/131525" target="_blank">📅 01:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131524">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTDSg86NnCn9b5_FS-BOg_67qIqvw7pPKK-UkImiZdW3CFPBOEeClathxceS3hOeobzDNCMxGcCqjAQaRWCNK4tlpF1yYWDLY5ukSGX7P_qizu2lNE5EEvs15AuUQcv_w88fNM47xqyBxR-5e-4MzjrlDdsOJHVlHd3gb_tCVNEI-Nk3r3ShaszfmfDFb9KN3EGL50vRu7TgWyXgoVbtd-FWxdwJERDKV2tKHfkcLOTxNIoIAGzejNcFD88FGSQvARbImbQ3joRpHTsMm-7jtTKRYSFIg6h7QRwPP6WXeLYRU0BQcGtwDjQMi1hKamI9pGCspjHat1crg3fBK0LYrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مصطفی نجفی مشاور محسن رضایی: بعید است مذاکرات به نتیجه‌ای برسد، چرا که شکاف‌ها بسیار بزرگ است. ایران علی‌رغم آمادگی جنگی، راهبرد «نه جنگ» «نه تسلیم» را دنبال خواهد کرد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 761 · <a href="https://t.me/SorkhTimes/131524" target="_blank">📅 01:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131523">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ur_-Qwhc8gNzHYHMyLZpPbj-Ntck-NUAWLxN9-DjQS0L3-rujRQCU03pdO5rpPp6b6BMDdJxBt0Rm_a41qqnLOr9g18JI-yK5IoRONGFp3s0Alk7s6igjcVdbNq8wJT_2VQvJc8yKC7CAcM1wq2BM-tWscYDQNxKpI9rekNJmOFg37t4iowTz4KeUZUcHy6SVRvj4Jum9lKMofnKsxSFWbgVWRV2g9eSHVRhU9ApomYWQipy8xa7qI1csHvv0wTpFyNkDr75SMGNDcJov1bgvVAH39EOxmQ6IorGzVqfysy0N2VzTkUTNztcAkIQhmT-a3fT7m0Oa9qcs-KHdTMq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ درباره ایران، اوباما و بایدن که بوی تهدید میده؛
ایران 47 ساله داره با آمریکا و کل دنیا بازی می‌کنه؛ هی امروز و فردا می‌کنه، وقت می‌کُشه و معطل نگه می‌داره.
تا این که بالاخره شانس بهشون رو کرد و اوباما رئیس‌جمهور شد. اون نه‌تنها با ایران خوب بود، بلکه عملاً طرف ایران رو گرفت، اسرائیل و بقیه متحدای آمریکا رو کنار زد و یه جون تازه و خیلی قدرتمند به ایران داد.
صدها میلیارد دلار پول و حتی ۱.۷ میلیارد دلار پول نقد رو با هواپیما فرستادن تهران و دو دستی تقدیمشون کردن.
اون‌قدر پول بود که انگار بانک‌های واشنگتن، ویرجینیا و مریلند رو خالی کرده بودن. وقتی پول‌ها رسید، مقام‌های ایرانی خودشون مونده بودن باهاش چیکار کنن!
تا حالا اون‌همه پول یه‌جا ندیده بودن و دیگه هم نخواهند دید. پول‌ها رو با چمدون و کیف از هواپیما پایین آوردن و ایرانی‌ها از خوش‌شانسیشون شوکه شده بودن.
ایران بالاخره بزرگ‌ترین آدم ساده‌لوح رو پیدا کرده بود؛ یه رئیس‌جمهور ضعیف و احمق به اسم اوباما. اون واسه آمریکا فاجعه بود، البته نه به بدی «جو خواب‌آلود» بایدن!
ایران 47 سال آمریکا رو سر دَوونده
اما دیگه قرار نیست بخندن!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 746 · <a href="https://t.me/SorkhTimes/131523" target="_blank">📅 01:44 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131522">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhm2ErFMAmLAw4lfxsZBoBM1Yk-oas33rsp-AHryx1To62peejS7ziFooDbhyRmriWTKsdYdu_i6sjlM3OU636ydjTkhDxOC4RiHmElxwhEJpBN1Bg_CKVflH2ZF7QwnqGiEvQG5OGq5NOav8BWUAxnSbHTT8GcN-op022pt_6k09Eeq-wW-YL3tu2hh2Vs4bXjrghAv1IVoTuFirT4isyFKbnD2zPqblrG_-CRJYX25aDBvI99LYnOdl7bZ0yFQfqhduGX7gmFqd9U0vYX0mJ8LmByoEFlpXhDJdUETvc2BaXI51q70sxndGd5vieCokox8wnaJFexa6l5-BBwOTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ: از پاسخ ایران راضی نیستم
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 679 · <a href="https://t.me/SorkhTimes/131522" target="_blank">📅 01:29 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131521">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
منابع دیپلماتیک به المیادین:
پاسخ ایران شامل درخواست برای پایان دادن به محاصره و آزادی صادرات نفت است.
پاسخ ایران که از طریق میانجی پاکستانی ارسال شده، حاوی بندی مربوط به آتش‌بس در لبنان است.
گنجاندن پرونده آتش‌بس در لبنان در پاسخ ایران، جزو خطوط قرمز تهران در مذاکرات محسوب می‌شود.
تهران برخی از تفاهم‌های مطرح‌شده را به تضمین‌هایی مرتبط با پایان دادن به تشدید تنش در لبنان گره می‌زند.
هر توافقی با واشنگتن باید شامل پایان فوری جنگ بلافاصله پس از اعلام آن باشد.
ایران بر لغو تحریم‌های آمریکا و آزادسازی دارایی‌های بلوکه‌شده ایران تأکید می‌کند.
تهران خواستار لغو محدودیت‌های «اوفک» (OFAC) مربوط به فروش نفت ایران است.
پاسخ ایران بر مدیریت ایرانی تنگه هرمز در چارچوب تفاهم‌های مطرح‌شده تصریح دارد.
توافق پیشنهادی شامل مذاکرات ۳۰ روزه پس از توقف جنگ برای بحث درباره جزئیات است.
ایران گام‌های متقابلی را برای آزمایش جدیت واشنگتن در اجرای تعهدات پیشنهاد کرده است.
مذاکرات بین تهران و واشنگتن در حال حاضر به صورت کتبی و از طریق میانجی پاکستانی ادامه خواهد یافت.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 741 · <a href="https://t.me/SorkhTimes/131521" target="_blank">📅 01:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131520">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
اطلاعیه رسمی ارتش:
ساعتی پیش یک فروند پهپاد شناسایی دشمن متجاوز، توسط سامانه‌های شبکه یکپارچه پدافند، تحت فرماندهی قرارگاه مشترک پدافند هوایی کشور در منطقه جنوب غرب منهدم شد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 709 · <a href="https://t.me/SorkhTimes/131520" target="_blank">📅 01:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131519">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
۹۰٪ کاربرا هنوز اشتباه وارد سایت میشن!
تو جزو اونایی یا میخوای حرفه‌ای عمل کنی؟
✅
ورود سریع به وینکوبت فقط با یک کلیک ساده:
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
نه لینک اضافی
📌
نه سردرگمی
📌
نه اتلاف وقت
📌
مستقیم، سریع، بدون دردسر وارد شو!
⏳
دیر بجنبی، از بقیه عقب می‌مونی.
🔗
الان وقتشه مسیر درستو انتخاب کنی:
🤖
@Wincobet_bot
📌
برای تحلیل بازی‌ها و آخرین اخبار سایت جوین بدید:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 761 · <a href="https://t.me/SorkhTimes/131519" target="_blank">📅 01:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131515">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
بهزاد داداش زاده: علت عدم نتیجه گیری پرسپولیس افشین پیروانی بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 849 · <a href="https://t.me/SorkhTimes/131515" target="_blank">📅 20:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131514">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اوسمار هنوز قولی برای برگشت نداده!
✅
🔗
شرایط بازگشت خارجی‌های پرسپولیس فراهم شد
🔺
فرهیختگان
: تیم پرسپولیس در نظر دارد دور جدید تمرینات خود را از اول خردادماه آغاز کند و در همین راستا به تعهدات مالی‌اش در مورد بازیکنان و مربیان خارجی خود عمل کرد.
🔺
این باشگاه اواخر هفته گذشته طلب خارجی‌های خود را از طریق صرافی انتقال داده و گویا هنوز این رقم‌ها به دست برخی از آنها نرسیده است. هرچند با توجه به شرایط سخت حاکم بر منطقه و تحریم‌ها، احتمالا تا دو سه روز آینده آنها به پول خود می‌رسند.
🔺
البته اوسمار و دستیارانش هنوز برای بازگشت به موقع در تمرینات سرخپوشان هیچ قولی نداده‌اند بلکه با بررسی شرایط قرار است تصمیم گیری کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 885 · <a href="https://t.me/SorkhTimes/131514" target="_blank">📅 20:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131512">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⏳
لیگ برتر برمی‌گردد؛ حتی وسط آوارِ بحران
✅
مهدی تاج بالاخره حرف آخر را زد:
لیگ بیست‌وپنجم قرار نیست نیمه‌کاره بماند.
🔗
در هفته‌هایی که خیلی‌ها پیشنهاد تعطیلی کامل فصل را داده بودند، فدراسیون تصمیم دیگری گرفت؛
نه خبری از لغو لیگ است،
نه قرار است فصل بدون قهرمان تمام شود.
🏭
کارخانه‌ها زیر فشار
🔺
تاج می‌گوید تیم‌های صنعتی دیگر مثل قبل توان هزینه ندارند.
از فولاد و پتروشیمی تا آلومینیوم؛
همه درگیر تبعات جنگ و مشکلات اقتصادی شده‌اند.
کنایه تلخ او هم جالب بود:
«در دنیا تیم‌ها کارخانه‌داری می‌کنند، اینجا کارخانه‌ها تیمداری.»
📅
تقویمی که به‌هم ریخت
🔺
تعویق لیگ فقط چند بازی را جابه‌جا نکرده؛کل فصل بعد را وارد بحران کرده است.
نقل‌وانتقالات،شروع لیگ جدید،
و حتی برنامه جام ملت‌ها،
همه حالا به تصمیم تیرماه گره خورده‌اند.
🔥
سناریوی ۱۸ تیمی رد شد
بخشی از فوتبال ایران می‌خواست این فصل بسته شود؛
بدون قهرمان،
بدون سقوط،
و با لیگ ۱۸ تیمی در سال آینده.
📌
اما تاج صریح گفت:
«امکانش نیست.»
🌍
چشم‌ها به جام جهانی
🔺
فدراسیون فعلاً همه‌چیز را به تیم ملی وصل کرده.
برنامه این است:اول جام جهانی،بعد ادامه لیگ.
یعنی شاید بازیکنان مستقیم از آمریکا وارد مسابقات باشگاهی شوند.
🎭
فوتبال ایران؛ بین جنگ، فرسودگی و اجبار
🔺
واقعیت این است که لیگ دیگر فقط یک مسابقه فوتبالی نیست.
بازی‌ها حالا وسط بحران اقتصادی، تقویم فشرده و فرسایش عمومی برگزار می‌شوند.
اما ظاهراً تصمیم نهایی گرفته شده:
لیگ باید تمام شود؛ به هر قیمتی/طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 889 · <a href="https://t.me/SorkhTimes/131512" target="_blank">📅 17:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131511">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">📌
خبرگزاری ایرنا:
تهران پاسخ خود رو به متن پیشنهاد آمریکایی از طریق پاکستان ارسال کرد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 849 · <a href="https://t.me/SorkhTimes/131511" target="_blank">📅 16:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131507">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vntb6C11-LbpypawlmAPmH8XMMSYTSK6aBLaIhN7xMp37lxabT7KLbolH5h5WcZ81XEuzPc2O56Lcz7kjVJXHK9hY7aJDgDecujxVBzeltYEyYjci7DcKLf_lXff94IrDt2ikl4YxGTZ_Dt-l5BzEnddj77fiarCWxNcWoM6aLoOQ4xVdE_Lsi08uaxvWqQjUgUFVjRjb7dBqddp-K70bgl2KwD5iEPWOSxVoyRudDoB66tzSX53HJwSRW-cGPjgiTxogf1BHy3wbRhb6kfxHszpR60ZEVsssg0i7oG_PPUnLmSoZyozLONdUmjCL_8df2stj6dVEzVbp4qBFVbE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ایگور سرگیف در گفتگو با رسانه‌های ازبکستانی اعلام کرد که به قراردادش با پرسپولیس پایند خواهد بود.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 914 · <a href="https://t.me/SorkhTimes/131507" target="_blank">📅 15:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131506">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWzR2c4LrAGLEIdUDAbqlKOeiVWXv-jQPtUzTDSyXYOwUZ30U_wCB2DR8yP6uGgf0SYtOTYqhF5kl-3ZEv9p8Y38GTenXxAzvdzCdXppl_4hyE6FtmsDiujM3q-jmv8v3xz8MYWg9-uIs36-Yuo8-f5ikINX5xRcVP8owovI2tPliiw11sLJ82hO5AF3_PoAzVRW6zzi0tFzcSA4syyfAYTvLzOd8c_5QWI8rtR-5jGKBXTCx_JqriSFHkGsCpBMmfDHkBko8Kic7bys-zKSJ9Qza5MJ2URNqYc5xejp4QJT3NmkfZ_qypzDlsamIJ_rKJm1sYE8mjQih45dSj8x3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
برنامه بازی‌های ایران در مرحلهٔ گروهی:
▪️
۱۹ دی: ایران - چین
▪️
۲۳ دی: ایران - قرقیزستان
▪️
۲۸ دی: ایران - سوریه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/SorkhTimes/131506" target="_blank">📅 15:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131505">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🟢
دسترسی سریع به سایت وینکوبت
✅
کاربران عزیز، برای ورود آسان و بدون دردسر به سایت وینکوبت، می‌توانید از ربات رسمی استفاده کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔹
ورود سریع و مستقیم به سایت
🔹
بدون نیاز به جستجوی لینک‌های مختلف
🔹
دسترسی راحت از داخل تلگرام
📌
همه چیز به ساده‌ترین شکل ممکن داخل ربات برای شما کاربران محترم فراهم شده.
🔗
اگر دنبال یه راه مطمئن و سریع برای ورود هستید، ربات وینکوبت بهترین انتخاب شماست:
🤖
@Wincobet_bot
🔗
برای دریافت تحلیل بازی‌ها و اطلاع از آخرین بروزرسانی‌ها، به کانال رسمی وینکوبت بپیوندید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 772 · <a href="https://t.me/SorkhTimes/131505" target="_blank">📅 15:14 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131504">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
فوری/ رویترز: مجتبی خامنه‌ای به نیروهای مسلح ایران دستور ازسرگیری عملیات های نظامی را داد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 814 · <a href="https://t.me/SorkhTimes/131504" target="_blank">📅 14:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131503">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
خروجی های پرسپولیس تا به این لحظه :
🔺
سروش رفیعی
🔺
میلاد محمدی
🔺
مرتضی پورعلی گنجی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/SorkhTimes/131503" target="_blank">📅 14:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131502">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1sv4t7YxGv27KYP7BJvLa5OGwm_TbcBD0AA8qBG55Hgns1WnooJizt6OY8mrZbnJQhXx3vQ5lmVahObZaGnacTKnib791-sJQDgj7GKKStm18P9XQzzBoy5JbPx0krvRvDuNsQhfH779nxLRu0IZ2oVY-9H3AbFa1GJeErL6ZGTLsUGmDO4u3i5M4wxIlALHU4OVYenxQte5_vPQK3b9P4u20CLDQ1xuTrHl8c_aKlmSjaqasGjnYZ-tHz5n_zafcGV_fN-oN8TLYgTlVy3ukkshq-MUFD8dZcXwjFPO0N1bRy78iZicctuL_hUoxz654FuZQp-N055meOQMbGQdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
افشای رقم رضایتنامه ۳ بازیکن برای پیوستن به پرسپولیس/رقم پیش پرداخت به ۲ ملی‌پوش مشخص شد
🔺
باشگاه پرسپولیس در بخش پیش پرداخت‌ها، از پرداخت مبلغ ۲۵ میلیارد تومانی به باشگاه هوادار برای جذب محمدحسین صادقی، پرداخت مبلغ ۲۵ میلیارد تومانی به باشگاه خیبر برای جذب حسین ابرقویی‌نژاد و هزینه ۲۲ میلیاردی برای به‌ خدمت گرفتن امین کاظمیان خبر داده است.
🔺
همچنین پرسپولیسی‌ها در این بخش، از پرداخت پیش پرداخت قرارداد ۱۷ و ۱۲ میلیاردی برای پیام نیازمند و میلاد محمدی خبر داده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 916 · <a href="https://t.me/SorkhTimes/131502" target="_blank">📅 14:49 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131501">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⚪️
مهدی تاج: 10 روز است که از کانادا برگشته‌ایم ولی هنوز چمدان‌هایمان را نفرستاده‌اند، نمی دانم سرنوشت چمدان‌های ما چه شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 891 · <a href="https://t.me/SorkhTimes/131501" target="_blank">📅 10:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131500">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
دیگه لازم نیست دنبال لینک سایت بگردی!
📌
فقط با یه کلیک از داخل ربات وارد وینکوبت شو:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
سریع، مستقیم، بدون دردسر
📌
بدون نیاز به جستجو یا لینک‌های پراکنده
📌
همه چیز داخل ربات آماده‌ست:
▪️
ورود فوری به سایت
▪️
دسترسی راحت از تلگرام
▪️
بدون مراحل پیچیده
🔗
ساده‌ترین راه ورود به وینکوبت همینجاست:
🤖
@Wincobet_bot
📌
میخوای با تحلیل جلوتر از بقیه باشی؟
برای دریافت آنالیز بازی‌ها همین الان جوین شو
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/131500" target="_blank">📅 02:04 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131496">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎙
⚪️
قلعه‌نویی: نمی‌توانیم از الان بگوییم قهرمانی می‌آوریم یا خیر
▪️
امیر قلعه‌نویی پس از قرعه‌کشی جام ملت‌های ۲۰۲۷ گفت:
▪️
پیش‌بینی فوتبال سخت است و نمی‌توانیم از الان بگوییم قهرمانی می‌آوریم یا خیر.
▪️
دوره قبلی هم شانس و لیاقت قهرمانی داشتیم اما بدشانسی شامل حال ما شد.
▪️
فوتبال در آسیا پیشرفت کرده و تیم‌ها به هم نزدیک شده‌اند.
▪️
امیدوارم در جام جهانی و سپس در جام ملت‌ها نماینده خوبی برای مردم ایران باشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 908 · <a href="https://t.me/SorkhTimes/131496" target="_blank">📅 00:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131494">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
‼️
🇮🇷
نیروی دریایی سپاه در بیانیه رسمی خود اعلام کرد: از این پس هر حمله به نفتکش های ایرانی با حمله به مقرهای نظامی امریکا پاسخ داده خواهد شد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 906 · <a href="https://t.me/SorkhTimes/131494" target="_blank">📅 00:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131493">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAdyXkzqfStUaZ84_8PrfqbNE3npF5Kl-K_1IAmrz4aP2SNnpH2B1aL3FV5RiaehEyCZ2mzYllHfsDRv4wiN19YGOsxBeKtx7Q6Mls-CGSYSCV0KjafI0xM5U5BdSClvGOZYmvCfK6IqDl0Uhg5yellSBIqUYTGZ8E_84yVv9XoZ1KeAqU4FaLIIL_Yn5m3-xusbpyd3IIZKVOxCPe7A_dpy_jo2Pmwa83snI7EUtxvLSghivpszeunhjJHt6BiCIZnZmRv09Qtfb1QgOFIp-daP-B8aXsSnS6oYJaH8s0bt3P8JNbmJ4abx0g8Ns5_gAzmkfr0YQLXCPzeKg9vG8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توضیح علی بازگشا مدیر روابط عمومی باشگاه پرسپولیس در مورد وضعیت خوب مالی باشگاه پرسپولیس و پرداختی‌های باشگاه در مدت اخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 910 · <a href="https://t.me/SorkhTimes/131493" target="_blank">📅 23:59 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131492">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
قرعه‌کشی جام ملت‌های آسیا انجام شد/ ساده مثل گروه ایران
▪️
گروه A:
🔹
عربستان
🔹
کویت
🔹
عمان
🔹
فلسطین
▪️
گروه B:
🔹
ازبکستان
🔹
بحرین
🔹
کره‌شمالی
🔹
اردن
▪️
گروه C:
🔴
ایران
🔴
سوریه
🔴
قرقیزستان
🔴
چین
▪️
گروه D:
🔹
استرالیا
🔹
تاجیکستان
🔹
عراق
🔹
سنگاپور
▪️
گروه E:
🔹
کره جنوبی
🔹
امارات
🔹
ویتنام
🔹
لبنان/ یمن
▪️
گروه F:
🔹
ژاپن
🔹
قطر
🔹
تایلند
🔹
اندونزی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 894 · <a href="https://t.me/SorkhTimes/131492" target="_blank">📅 23:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131490">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🔴
فوری
،
فاکس نیوز: اگر پیشنهاد امشب تهران برای توافق با آمریکا منفی باشد جنگ به سرعت آغاز خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 860 · <a href="https://t.me/SorkhTimes/131490" target="_blank">📅 22:23 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131489">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🔴
اگر علیپور از خواسته مالی خود کوتاه نیاید قرارداد وی تمدید نخواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 938 · <a href="https://t.me/SorkhTimes/131489" target="_blank">📅 22:03 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131488">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1Zvhl28NXZu63fKkb3vZU4M5RdCgZ7PvqGRxPLiRXQDv331RVnwRSmEjXZepzNLAAllM_b8gBg0qUnFeSnVsrBXKgbE6XDajV9yU5IQXpzNkZc0RxdeAk8-mcXfpwZpZrsnLeT7hFA2ZCi9of0cvStDkl6RVEDDB7q7wA2oYiakKe6VAM7WzyHFDRJ5Is9ifanLbC87BJmJjQLU6g7oXXPcBWyhkb-gc-7pDstX_pLENCw3tFvlr2XZbgU3pJjPEnHASJcvMszIzZyAVFMGvyYi8bWmjqZWuGYlr419TZJsxoQqT8RV14b6EpWreM4mac8Pzg6HHokGSRv7glLo_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگر علیپور از خواسته مالی خود کوتاه نیاید قرارداد وی تمدید نخواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 942 · <a href="https://t.me/SorkhTimes/131488" target="_blank">📅 21:56 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131487">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
اردوغان: مخالف گسترش جنگ در منطقه هستیم. ترکیه نمی‌خواهد جنگ آمریکا علیه ایران در منطقه گسترش یابد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 866 · <a href="https://t.me/SorkhTimes/131487" target="_blank">📅 20:29 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131486">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtCY6exCr3GlWmdKynAhVMsNDu4PJg4bwNRf_8a-JJ2ecUCWGL9o5Tq2MDU6mhkx8vUL-GK-fEZVNpGjh_OLW_QmYlEBT0669qGeGXs3OqlAnzAjsy5BNAHtKjJBVjtS8Tjs2Ys4UwaPIisaf9XgRvab5k9ORfUbAPK0OL4UAfdwBAJqx2vh9SH5W2-BwEY7Tqof5ip0lhnl8RL7-U_KwoZEdJDM-d-_6q8SVsoa5FOogm5gArJK2_SWOYGxetCu9yFqgG6hFTio-zj79LegkBtLAkuoN0ZeTZEQ9T5u_WMLWS1JvXs3fxqL6Bz8-Rm6up6oaJLWxRq4x_42ZcMGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ManCity -
🔴
Brentford
🟣
پریمیرلیگ انگلیس
⏰
شنبه ساعت ۲۰:۰۰
🏟
استادیوم
اتحاد
⚽️
شاگردان پپ گواردیولا حالا پس از درجا زدن نابه‌هنگام مقابل اورتون؛ با یک بازی کمتر نسبت به آرسنال، با تیم آرتتا پنج امتیاز فاصله دارد و اگر توپچی‌ها تمام بازی‌های باقی‌ماندشان را ببرند، رویای قهرمانی منچسترسیتی عملاً به‌باد می‌رود. سیتیزن‌ها امروز با برنتفورد رده هفتمی بازی می‌کنند که در فصل جاری، عملکردی فراتر از انتظار داشته و بالاتر از تیم‌های نامداری مثل چلسی، نیوکاسل و تاتنهام قرار گرفته‌اند. البته آمار کاملاً به‌نفع سیتی است. شاگردان پپ در ۳۴ بازی، (یک بازی معوقه دارند)، ۶۹ گل زده‌اند و ۳۲ گل خورده‌اند. این آمار برای برنتفورد، ۵۲ گل زده و ۴۶ گل خورده است. البته بازیکنان کیت اندروز، در شش هفته اخیر فقط یک برد داشته‌اند و چهار تساوی و یک شکست را هم مقابل یونایتد، ثبت کرده‌اند.
📌
در
ربات
وینکوبت
ثبت‌نام کن و با شارژ از طریق کریپتو ۵٪ شارژ بیشتری رو دریافت کنید، همین حالا شروع کن:
👇
🟣
[
برای ورود به ربات کلیک کنید:
]
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال سایت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 945 · <a href="https://t.me/SorkhTimes/131486" target="_blank">📅 20:29 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131485">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔰
سرور یک ماهه Open VPN فقط تلگرام نامحدود ۱۳۰۰ هزار تومن
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 825 · <a href="https://t.me/SorkhTimes/131485" target="_blank">📅 19:20 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131483">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY46PFD-w1VeyqmdzcuvOAjXD5-3MwehtYDSm7keEJ0vu-5LZaq_50ln5zWMpxklGlYoPfB_tSS3k2ssGo9CrI-e-WKNGwGzX9GEO_5dFGDGExsvHco-rUNN1Jyb2g4Mt_OMWn_D7lNEKm-Fj5THJt30KkCO30kFARupg5gnw_TMwuRL40I3SQeW8rrpWEQT5_YfPylcNKDSMJBAFXXMeSsnxpab1i54lHfDx_1mXHkd1IOU6gO4Q43sykrjTZ2LLfHTUat1DoTv5z_fvBbky7_2hTKFfXroINPJNXnu3KoSt3m0IVRkwOVRe_PjE9vGV2zVYzVnYGtZPlDqFkiomg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
روزخوش، مدیررسانه‌ای پرسپولیس: اوسمار لیست مازادی نداده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 872 · <a href="https://t.me/SorkhTimes/131483" target="_blank">📅 17:59 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131482">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rw5Bgw_zInoa1KG2enlEtibps7Ghz-iZS4Tk89E023N2KTeY3hIuxfqaUzehQ9DLCdekk24By1IUzdddZJkemKeI5hqy2dgE5KFDHmTOSIVCMLBRQiRarwEz2ogCFa9DGcCodJ-tI573NOWaqwlv7_gqDvzpRkCjftPFafYOlaQ5ATGaeIDzbFrlxXESmMsptiDuKY2eHs1UDOZVy4stA4wF3cKC0v_zE8dpm47Z4HA1oy62w17hsg8gB-FPGwsxoLvKZpL-en_VsgDfsBW7wTj1AKsBc2PS3CmPf-xFihYL0BqniR5KxNDtZLyfqD6clBdkS4TvLY1QXLKwMTKRjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔴
حمایت مورینیو از حضور ایران در جام جهانی ۲۰۲۶
◽️
ژوزه مورینیو در گفتگو با «فوتبال ایتالیا»: سیاست یک موضوع و ورزش موضوع دیگری است. تیم ملی ایران همچون سایر تیم‌ها شایسته حضور در جام جهانی ۲۰۲۶ است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 888 · <a href="https://t.me/SorkhTimes/131482" target="_blank">📅 17:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131481">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
🔴
باشگاه يرسيوليس پرونده مربوط به بازى  ملوان با استقلال و تراكتور را به دادگاه دادرسى ورزشى بين المللى (CAS) ارجاع داده است. اين باشگاه اميدوار است كه با پیروزی در اين دادگاه، دو امتياز از تيم هاى استقلال و تراكتور كسر گردد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 823 · <a href="https://t.me/SorkhTimes/131481" target="_blank">📅 17:54 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131480">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
⚪️
درآمد ۶۵ میلیاردی پرسپولیس در دوران جنگ تحمیلی
🔻
باشگاه پرسپولیس درآمدهای خود در دوماه اخیر جنگی را افشا کرد.
🔻
پیش از این باشگاه پرسپولیس درآمدهای ماهانه خود تا پایان بهمن‌ماه را منتشر کرده که در آن، درآمد تیر ماه ۲۱ میلیارد و ۷۰۰ میلیون، درآمد مرداد ۳۲…</div>
<div class="tg-footer">👁️ 896 · <a href="https://t.me/SorkhTimes/131480" target="_blank">📅 16:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131479">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
⚪️
درآمد ۶۵ میلیاردی پرسپولیس در دوران جنگ تحمیلی
🔻
باشگاه پرسپولیس درآمدهای خود در دوماه اخیر جنگی را افشا کرد.
🔻
پیش از این باشگاه پرسپولیس درآمدهای ماهانه خود تا پایان بهمن‌ماه را منتشر کرده که در آن، درآمد تیر ماه ۲۱ میلیارد و ۷۰۰ میلیون، درآمد مرداد ۳۲ میلیارد تومان، درآمد شهریور ۷۱ میلیارد تومان، درآمد مهرماه ۷۰ میلیارد تومان، درآمد آبان‌ماه ۶۹ میلیارد تومان، درآمد آذرماه ۷۴ میلیارد تومان، درآمد دی‌ماه ۵۹ میلیارد تومان و درآمد بهمن‌ماه ۶۹ میلیارد تومان گزارش شده بود.
🔻
باشگاه پرسپولیس طی عملکرد ۱ ماهه منتهی به ۱۴۰۵/۰۱/۳۱ معادل ۶۵۳,۹۵۵ میلیون ریال، درآمد داشته است و در مجموع تا پایان ماه فروردین، میزان درآمدهای پرسپولیس به ۶۴۷ میلیارد تومان برسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 864 · <a href="https://t.me/SorkhTimes/131479" target="_blank">📅 16:32 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131478">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
تسنیم: سید مجتبی خامنه‌ای به بهبودی کامل رسیده.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 829 · <a href="https://t.me/SorkhTimes/131478" target="_blank">📅 16:18 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131477">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
خبرگزاری ایرنا : به دلیل قطعی اینترنت ، این روزها خیلی از آنلاین‌ شاپ‌ ها مجبور شدن تو خیابون و مترو دست‌ فروشی کنن.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 863 · <a href="https://t.me/SorkhTimes/131477" target="_blank">📅 16:14 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131476">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس خواهد ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 889 · <a href="https://t.me/SorkhTimes/131476" target="_blank">📅 16:12 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131475">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwbmoWYXQNTOIALubneDS9NXKgzOTEG_IPTvTM09Q6XUMWUN2q-WWR8dSrWtNWFcfwvOOpHHAg2k7tXadUeAd5pT-c5al_i8Cf60tBD0RgDsCBByt-l62TY3M7wHob2bOp15HiuhK5TaLDsetGRTFTb3XtGSzcf6yuO17OHtFVF0c85_gCiC_pkrU5keGUal0NJ4F10BqpDjx8Cf-FqFk1ztZ_nWRMT4shPq1k4nCExENBAHZIkrg45IEkT5a86XLBWy54FIpTf28jl29oVNU9jqepfPK6QtRqOdiSsG_Zl03eOpUU6HmdMIFF5MyB4OCG8YCeXYGhmc1uQfhtxS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
۹۰٪ کاربرا هنوز اشتباه وارد سایت میشن!
تو جزو اونایی یا میخوای حرفه‌ای عمل کنی؟
✅
ورود سریع به وینکوبت فقط با یک کلیک ساده:
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
نه لینک اضافی
📌
نه سردرگمی
📌
نه اتلاف وقت
📌
مستقیم، سریع، بدون دردسر وارد شو!
⏳
دیر بجنبی، از بقیه عقب می‌مونی.
🔗
الان وقتشه مسیر درستو انتخاب کنی:
🤖
@Wincobet_bot
📌
برای تحلیل بازی‌ها و آخرین اخبار سایت جوین بدید:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 884 · <a href="https://t.me/SorkhTimes/131475" target="_blank">📅 16:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131474">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
کانال ۱۲ رژیم صهیونیستی:
◽️
اسرائیل این پیام را به واشنگتن رساند که بازگشت جنگ باید شامل تخریب زیرساخت‌های انرژی ایران باشد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 761 · <a href="https://t.me/SorkhTimes/131474" target="_blank">📅 15:59 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131473">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
⚪️
فدارسیون فوتبال اعلام کرد، در جام جهانی شرکت میکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 800 · <a href="https://t.me/SorkhTimes/131473" target="_blank">📅 15:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131472">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚀
تلگرام در عراق رفع فیلتر شد!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 838 · <a href="https://t.me/SorkhTimes/131472" target="_blank">📅 15:55 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131469">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
تاج: به دنبال برگزاری بازی دوستانه با تیم ملی لهستان هستیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 896 · <a href="https://t.me/SorkhTimes/131469" target="_blank">📅 11:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131468">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
باشگاه پرسپولیس پول پرداختی به خارجی‌ها را به‌روز کرد
🔺
باشگاه پرسپولیس در حالی که تاکنون 70 درصد قرارداد بازیکنان داخلی خود را پرداخت کرده است، به تازگی مطالبات بازیکنان خارجی خود را نیز پرداخت کرد تا دریافتی آن‌ها طبق قرارداد به‌روز باشد.
🔺
این باشگاه طبق قرارداد بازیکنان و کادرفنی خارجی خود، باید اول هر ماه مبلغ مشخصی را به حساب آن‌ها واریز کند که این اتفاق رخ داده و پرداختی تمام بازیکنان خارجی به‌روز شده است. همچنین سرخپوشان طی روزهای اخیر آخرین پرداختی خود به کادرفنی خارجی این تیم را نیز انجام داده‌اند تا طلبی به آن‌ها نداشته باشند.
تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 881 · <a href="https://t.me/SorkhTimes/131468" target="_blank">📅 10:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131467">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zk1o0mxPWU_kvDxTcGJw09q_Z3ntBfz-KLBlmo1odHTvkGZnjm__iuP9YMsQUU7bdTfI6oLmsScy1XoQsgbEw3SsKGyBKXbFrszC37biBpqf7JRAph3FpmbhBDwahJDRENsczrixj66A0qSKSWjQScZ-WK2EmvLDg4RNicKxEOEGAcC41Xpz2AkeDT4Bo4VAKJ5-D7oqKoYMFJd_gss53stA2o6YBAMQVuZMCcNtQQS9xvWFu-4yoYhfcSAWCh4l_wPGmJjXDxKPkWnH5jAkZMtH39YthowIJUWSiimQlXecbqPnzrIzj-LaaUWnhPEZ5UA-VIPg2jBH-ca-en2eTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاربران محترم برای دسترسی به سایت وینکوبت فقط کافیه از طریق ربات وینکوبت وارد بشید.
🤖
-
@Wincobet_bot
🤖
-
@Wincobet_bot
📌
بدون نیاز به جستجو، بدون لینک‌های پراکنده، همه چیز از طریق خود ربات انجام میشه.
📌
ویژگی‌های ربات وینکوبت:
👇
▪
︎ورود سریع و مستقیم به سایت
▪
︎دسترسی راحت از داخل تلگرام
▪
︎بدون مراحل پیچیده یا ورود جداگانه
📌
اگر دنبال یک راه ساده و سریع برای ورود به
وینکوبت
هستید، این ربات ساده‌ترین مسیر دسترسی شماست:
👇
🤖
-
@Wincobet_bot
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال سایت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 913 · <a href="https://t.me/SorkhTimes/131467" target="_blank">📅 01:27 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131464">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
وال استریت ژورنال: ممکنه دور جدید مذاکرات ایران و آمریکا هفته‌ی آینده تو اسلام‌آباد از سر گرفته شه اما جمهوری‌اسلامی همچنان با انتقال اورانیوم غنی‌شده از ایران مخالفه.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 822 · <a href="https://t.me/SorkhTimes/131464" target="_blank">📅 01:25 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131463">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی صداسیما امشب از بسته شدن تیک تاک توی آمریکا انتقاد میکرد و میگفت معیشت خیلیا به خطر افتاده! کشوری که ۷۱ روزه اینترنت رو بسته حالا نگران معیشت مردم آمریکاس :))
جدی دوربین مخفیه؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 960 · <a href="https://t.me/SorkhTimes/131463" target="_blank">📅 00:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131462">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚪️
تاج: تیم‌های راه‌یافته به لیگ نخبگان و لیگ قهرمانان را انتخاب خواهیم کرد
🔺
شاید بتوانیم مهلت معرفی تیم‌ها را یک ماه عقب بیندازیم.
🔺
۱۴ تیم مخالف برگزاری ادامهٔ لیگ‌اند؛ موافقان پرسپولیس و گل‌گهر هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 850 · <a href="https://t.me/SorkhTimes/131462" target="_blank">📅 00:39 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131461">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
بیفوما:
ادامه کار با پرسپولیس؟ چیزی مشخص نیست و نمی‌دانم چه اتفاقی خواهد افتاد، باید ببینیم چه می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 828 · <a href="https://t.me/SorkhTimes/131461" target="_blank">📅 00:38 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131460">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🔴
میلاد محمدی در آستانه پیوستن به پائوک یونان قرار دارد
🔺
پ.ن: به سلامت
👋
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/SorkhTimes/131460" target="_blank">📅 00:36 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131459">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
تلگرام آپدیت جدید داد؛ با 11 قابلیت تازه
تلگرام در آپدیت جدید خودش، تمرکز ویژه‌ای روی هوش مصنوعی و ربات‌ها گذاشته:
• صدا زدن ربات‌های هوش مصنوعی داخل هر چت
• گفتگو و همکاری ربات‌ها با همدیگر
• نمایش زنده جواب ربات هنگام تایپ‌شدن
• اتصال ربات به پروفایل برای پاسخ‌گویی خودکار
• ساخت سبک اختصاصی برای ویرایش متن با هوش مصنوعی
• جست‌وجو بین بیش از ۱۰۰ میلیون استیکر و ایموجی
• پشتیبانی جست‌وجوی استیکر در ۳۶ زبان
• محدود کردن رأی‌گیری بر اساس کشور یا عضویت در کانال
• آمار پیشرفته نظرسنجی‌ها برای مدیران
• ارسال پیام زمان‌بندی‌شده به‌صورت بی‌صدا
• حذف ری‌اکشن کاربران توسط مدیران گروه
• بیش از ۲۰۰ بهبود و رفع باگ
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 837 · <a href="https://t.me/SorkhTimes/131459" target="_blank">📅 00:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131458">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
تیم ملی (با رنکینگ 21 جهانی) 8 خرداد در کشور ترکیه به مصاف تیم ملی گامبیا (با رنکینگ 112 جهانی) خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 825 · <a href="https://t.me/SorkhTimes/131458" target="_blank">📅 00:31 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131457">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
با توجه به ضعف خط دفاعی پرسپولیس در فصل اخیر، اولویت این باشگاه در نقل و انتقالات تابستانی، جذب مدافع میانی خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 932 · <a href="https://t.me/SorkhTimes/131457" target="_blank">📅 00:30 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131456">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
اوسمار قصد داره در نقل و انتقالات تابستونی در هر سه پست دفاعی (دفاع راست، دفاع وسط و دفاع چپ) بازیکن بخره/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 950 · <a href="https://t.me/SorkhTimes/131456" target="_blank">📅 00:28 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131454">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
ترامپ برجام رو پاره کرد که مثلاً قرارداد بهتری برای امریکا ببنده. بعد از ۹ سال و دوتا جنگ تازه رسیده به مذاکره سر باز کردن تنگه‌‌ای که از ابتدای تاریخ تا الان باز بوده!!!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131454" target="_blank">📅 15:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131453">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9sqs94FchbsCubgVRbVcbrDDMqXrpcyIf9_dyFnU63PArtbNoDP5lTfxv-1h552lCzpIuCznHzEFG4FwBj-lejz698FxviCl1dEUCt1jP8S_jPZgqktnlNJ3i09XLcKyfa22ts11AUB5gctSBDeqxpE6pN0-z8WLZEjClu11FYfuz5tOj7fFiOlr7YCe2K70ch7ejKx0lK8PUrQvzGl8brXMhLJ8kbLEAwrmIGxwD00vOZnAk8PyfS_zyI_dOjjLGyoAtgtY8NN-jmukatTU5dnZmrMc0CbqR8B-nN_2mqMoMSdk36jhZlPsc_49kApYNv-eM20YuybZ_tUxpVIcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
دسترسی سریع به سایت وینکوبت
✅
کاربران عزیز، برای ورود آسان و بدون دردسر به سایت وینکوبت، می‌توانید از ربات رسمی استفاده کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔹
ورود سریع و مستقیم به سایت
🔹
بدون نیاز به جستجوی لینک‌های مختلف
🔹
دسترسی راحت از داخل تلگرام
📌
همه چیز به ساده‌ترین شکل ممکن داخل ربات برای شما کاربران محترم فراهم شده.
🔗
اگر دنبال یه راه مطمئن و سریع برای ورود هستید، ربات وینکوبت بهترین انتخاب شماست:
🤖
@Wincobet_bot
🔗
برای دریافت تحلیل بازی‌ها و اطلاع از آخرین بروزرسانی‌ها، به کانال رسمی وینکوبت بپیوندید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131453" target="_blank">📅 15:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131452">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAZ2IprTJiFN43lnDsTnniTzQP6yKqXrBW1aDuVLbIefKfGdJqHI8aLoX_CCX6kVsw0eBj9cGg0ifxjQkqj4e0bcS1l9pLWkAzLpqX58YWQUDg5g2NvLSW6n2vEmjRYUVgQ1y26gyvc4GuGMzbOCRyPO_zdAVJlSlt2SOf05376L9c5PHdbqts-Ays4u_xeAQQvbzIU7XLxpzVfn5K_hu_7jNyvUwxqOstQcvs8KaN5gW2nTDp464gVymXdrUlyNaKlqMX-OLFtCtWov9xMlHNF7CnGGOwR8AwfXOm20tH1XKReLkXh8dDYl7Z1G_WRTi2dPW6_tFRA-h1kCjsKfVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
حسین عبدی سرمربی تیم ملی امید شد
◽️
حسین عبدی که پیش از این هدایت تیم‌های ملی پایه را برعهده داشت، به عنوان سرمربی تیم ملی امید انتخاب شده و این انتصاب به زودی رسما اعلام خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 842 · <a href="https://t.me/SorkhTimes/131452" target="_blank">📅 14:55 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131451">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
بقیه خارجی‌ها همچنان در انتظار پرداختی پرسپولیس به مهاجم ازبک
🔺
مدیریت باشگاه پرسپولیس بخشی از قرارداد سرگیف را به صورت دلار نقدی به واسطه ایرانی او داد تا آن را به دستش برساند.
🔺
در بین بازیکنان پرسپولیس تیوی بیفوما، مارکو باکیچ و همچنین دستیاران خارجی اوسمار، نفراتی هستند که چند ماهی می‌شود حق و حقوق خود را دریافت نکرده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 916 · <a href="https://t.me/SorkhTimes/131451" target="_blank">📅 14:54 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131450">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
قرعه‌کشی رقابت‌های جام ملت‌های آسیا فردا شب (شنبه ١٩ اردیبهشت) در ریاض عربستان برگزار خواهد شد.
🔺
بر همین اساس، امیر قلعه‌نویی سرمربی تیم ملی فوتبال ایران صبح امروز راهی پایتخت عربستان سعودی شد تا به نمایندگی از فوتبال ایران در این مراسم حاضر شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 880 · <a href="https://t.me/SorkhTimes/131450" target="_blank">📅 14:51 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131449">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
دونالد ترامپ :
حملات امشب ما، فقط یه ضربه آروم و واسه تلافی بوده؛
آتش‌بس هم نقض نشده و همچنان برقراره.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/131449" target="_blank">📅 08:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131448">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiJG3_h0V5MUrL2SHk4KX089L3N-GSNWCqm4TS-02cdjoKd-3wQSe7GXGBrLe9_GabgDoJSlCxg6IrXVhGnZ8ayubWsuadzrLlIgoj6S70Skv9EZ3f2Fl-RQXaHHhRtP6Acslqn97WAWl0MUhLncPi-QI1bTRArQwomSTdAnVDmssj20toMWZaBucHxZCF5SkqaaKEqvyZsdpO5lSoyYYcHRb5-RPauOkRQmC_hy5fKyQaJww5Pd0rE1tVwMWRDPutozgT0lktyrwVf3vJOaZERYpPcHivSO1gaQL1HRgLzrdPGUMOQ71sXdV6j_bAHJY8Peb2ZwGtHpMA-FoDu1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پست جدید ترامپ تو برنامه تروث:
هر 3 ناوشکن ما بدون هیچ آسیبی با موفقیت از تنگه هرمز عبور کردن؛ اما خود ایرانی‌هایی که بهمون حمله کردن، آسیب زیادی دیدن و کاملا نابودن شدن.
موشک‌هاشون رو هم به راحتی سرنگون کردیم؛ پهپادهاشون هم دقیقا مثل قایق‌هاشون به ته دریا سقوط کردن.
ایران یه کشور معمولی نیست و توسط آدمای دیوونه اداره میشه که اگه سلاح هسته‌ای داشته باشن حتما ازش استفاده میکردن؛ اما هیچوقت همچین فرصتی به دست نمیارن.
همینطور که امروز شکستشون دادیم، اگه سریعا توافق رو امضا نکنن اونا رو سخت‌تر و شدیدتر خواهیم زد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131448" target="_blank">📅 08:01 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131447">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/selj_RTYzTVkJtlFrLiaObz_qM2VPZuhTyBrHFlV4RBtavLxFVASJy5WhEukMoxbyZo8_38D4eVIM5-qXxvuaBxMUOWROrvKn2f3XhA6GlP22Tce2_xI74-8a9WN0T8FBP2Ok6fg59IdlBY4YUW6glpu7KBTYZukeT598pSc-zP6cxyGzIZRMuthNPj9CiM-CHVmQst38zU09qh8OBc9OGqY3h1Op3bEU2iXRdXWgTWRs4FUaXoljlLnB2EjYfE1tU-Yx_bpNaJmHxL56CedUv1siwzcfsYLQSrbKORf9rFzDzPDy2OrWttlbpBDgnSY2IRGe8eW0hT7a8BYxJjhzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
هنوز داری دنبال لینک می‌گردی؟
✅
حرفه‌ای‌ها مستقیم وارد میشن!
با ربات وینکوبت، ورود به سایت فقط چند ثانیه زمان می‌بره:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
⚡
بدون فیلتر و دردسر
⚡
بدون لینک‌های الکی
⚡
فقط یه کلیک تا ورود
🎁
اگه سریع و راحت میخوای وارد شی، این همون چیزیه که دنبالش بودی!
🤖
@Wincobet_bot
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال وینکوبت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 938 · <a href="https://t.me/SorkhTimes/131447" target="_blank">📅 01:53 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131446">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
⚪️
🔴
سنتکام: نیروهای آمریکایی حملات بی‌دلیل ایرانیان را رهگیری کرده و با حملات دفاعی پاسخ دادند در حالی که ناوشکن‌های موشک‌انداز نیروی دریایی آمریکا از تنگه هرمز به خلیج عمان عبور می‌کردند، ۷ مه.
🔺
نیروهای ایرانی چندین موشک، پهپاد و قایق کوچک را به سمت ناوشکن‌های…</div>
<div class="tg-footer">👁️ 912 · <a href="https://t.me/SorkhTimes/131446" target="_blank">📅 01:17 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131443">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کانفیگ ها تازه ارزون شده بودن
جنگ بشه دوباره گرونش میکنن
😂</div>
<div class="tg-footer">👁️ 861 · <a href="https://t.me/SorkhTimes/131443" target="_blank">📅 01:13 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131442">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNgBc-pUxZiQkYRo9WkRZ9aDib2cePYCaGNIr3Q_NbEnyMjuYnIYuEptzhlPp7e8envoyaufEP1aJKqjmJrbxdkukkr7jcFRSHAFL5GnwSiayJmus-HRtynHXA_AGrT8Ok3dlbnc0vfjXXk6D8r7I530qebMIRA1i_eMn-Tmz8YYFgxehirZPhEKOZrx2hT5yPpJilbw354TCuvRjX_CmxtAMihTTpuGKCYPctCEmJD10uXjuV9CzKJ830l8mTA8neDRVrGiFzIMWU9llj8zrX9khKEldq2uKdH2usf32BYXzFSVChRUgrTC0q6JhZpOkJva1eIZbpncnoeGBhVDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
🔴
سنتکام: نیروهای آمریکایی حملات بی‌دلیل ایرانیان را رهگیری کرده و با حملات دفاعی پاسخ دادند در حالی که ناوشکن‌های موشک‌انداز نیروی دریایی آمریکا از تنگه هرمز به خلیج عمان عبور می‌کردند، ۷ مه.
🔺
نیروهای ایرانی چندین موشک، پهپاد و قایق کوچک را به سمت ناوشکن‌های USS Truxtun (DDG 103)، USS Rafael Peralta (DDG 115) و USS Mason (DDG 87) که از مسیر دریایی بین‌المللی عبور می‌کردند، پرتاب کردند. هیچ دارایی آمریکایی مورد اصابت قرار نگرفت.
🔺
فرماندهی مرکزی ایالات متحده (CENTCOM) تهدیدهای ورودی را از بین برد و تأسیسات نظامی ایرانی مسئول حمله به نیروهای آمریکایی از جمله سایت‌های پرتاب موشک و پهپاد؛ مکان‌های فرماندهی و کنترل؛ و گره‌های اطلاعاتی، نظارتی و شناسایی را هدف قرار داد.
🔺
سنتکام به دنبال تشدید تنش نیست اما آماده و مستقر برای حفاظت از نیروهای آمریکایی!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 947 · <a href="https://t.me/SorkhTimes/131442" target="_blank">📅 01:10 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131441">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj1x-YjhAeEEVidFZl0lkYIeOz3Cxl1QNtBWiiwIM5yRA2JS1oczapMfTJamOLUeY3r9jWTTiTt60iLWY4NjO7czvyXlQAhPLQ0bA-hN-PU0Fnr6Xoq-9nlQYWsQbEE9Cb3OIZGr6MdGLNEERxfT9R5-7zTXfmW81yv6qEzIjJTdRrA2J_g1wHfjeghM3rqD5_DTvbTd6q9a7A-fLzWNEUh4TdlRO7dLfriitdeucp0_ouX5aM83UC_SOrt5eE06lLmhQQi0DRI1E4nHvTP2W7vsHGHtaOcjgLmLSCQKSGf7V66cZLiF159sNAJ829x3qR_m706huDtycOfMCij0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔴
فرماندهی نیروی دریایی سپاه:
🔺
1- در پی نقض آتش بس و تجاوز ارتش تروریستی امریکا به یک فروند نفتکش ج.ا ایران در حوالی بندر جاسک و نزدیک شدن ناوشکن های ارتش تروریستی امریکا به تنگه هرمز، طی یک عملیات ترکیبی بسیار پرحجم و دقیق با بکارگیری انواع موشک های بالستیک و کروز ضد کشتی و پهپادهای انهدامی
🔺
2- با سر جنگی شدید الانفجار به سمت ناوشکن های دشمن اجرای آتش نمود.
‼️
رصدهای اطلاعاتی حاکی از خسارات قابل توجه به دشمن آمریکایی است و سه ناو دشمن متجاوز به سرعت از محدوده تنگه هرمز فرار کردند.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 848 · <a href="https://t.me/SorkhTimes/131441" target="_blank">📅 01:03 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131440">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
شبکه 12 اسرائیل: 3 ناوشکن آمریکایی هدف حملات ایران در تنگه هرمز قرار گرفته‌اند
پ.ن: بزنید عصمت شون بگایید
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 771 · <a href="https://t.me/SorkhTimes/131440" target="_blank">📅 01:01 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131439">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91924f4084.webm?token=S8c1-O2XPEPQAaqHq_rnHlpMrjPjNY_g9aYVfOSCAJBSF_VCMjv9-hGr1sRHrnI-NFUGUsYlB8HZ9utLRcdkEYniowPuetl93eESCttbor5L_UBbTzzkG9JKDX5esOfoFh00XsZ3soTW9ntusMVMM96CQVfQQaFtoaGDEDh_SE2SjQCD92lwRzBz4ahfrmfEF9awdMWk1ZnLaSmz9QmGUHgkYxukt8JJqk86BYWDcELgZJaeMY6Zqv8WY2flEvss8ATQnUXHLwYk1peZRklhs4Huxf5yW-kaNpWEVW90v_wZxjZAbxbs87Yf8B-O-_m4pfUVxFy5qRdmZ_ZuQUrZFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91924f4084.webm?token=S8c1-O2XPEPQAaqHq_rnHlpMrjPjNY_g9aYVfOSCAJBSF_VCMjv9-hGr1sRHrnI-NFUGUsYlB8HZ9utLRcdkEYniowPuetl93eESCttbor5L_UBbTzzkG9JKDX5esOfoFh00XsZ3soTW9ntusMVMM96CQVfQQaFtoaGDEDh_SE2SjQCD92lwRzBz4ahfrmfEF9awdMWk1ZnLaSmz9QmGUHgkYxukt8JJqk86BYWDcELgZJaeMY6Zqv8WY2flEvss8ATQnUXHLwYk1peZRklhs4Huxf5yW-kaNpWEVW90v_wZxjZAbxbs87Yf8B-O-_m4pfUVxFy5qRdmZ_ZuQUrZFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برو کصکش، بزنید کص کون شونو خونی بکنید کصکش پدرا رو همین مونده این کونده باقالی ها گوه خوری کنن کله پدر هرچی شیخ نشین کصکشه</div>
<div class="tg-footer">👁️ 801 · <a href="https://t.me/SorkhTimes/131439" target="_blank">📅 01:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131438">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2feb948a65.webm?token=uvBxBs4uBKONM7djK-pNhAva4R55qYzWhTtEPEfOsvLZpglAb-46NLSmn4dFxBvrSWqG1aBx65hF4D1ZRs2saKuHyw3JCB7ZYGp9papjZvXx6LojvusDxBOrnMG9p1mECdQYZAn8Ljju95CzOLqLz33n1BGTWBjjTIzjeXUOIBwj9gm8Xa5BRbD_zrO2e5RmBIRaLPfICHiLBfWBaktsByHDfN7enI24CMFhgcpRNHCJaPmIWRanis_bLSQ9aA7sdRw4mSjOigNVdzko27ONvN2h5MukModoVT0piYDi4tHW3iQMv3xEsx6ry9ALNZ8rgaG-d1SIBBE93hwpG2yQlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2feb948a65.webm?token=uvBxBs4uBKONM7djK-pNhAva4R55qYzWhTtEPEfOsvLZpglAb-46NLSmn4dFxBvrSWqG1aBx65hF4D1ZRs2saKuHyw3JCB7ZYGp9papjZvXx6LojvusDxBOrnMG9p1mECdQYZAn8Ljju95CzOLqLz33n1BGTWBjjTIzjeXUOIBwj9gm8Xa5BRbD_zrO2e5RmBIRaLPfICHiLBfWBaktsByHDfN7enI24CMFhgcpRNHCJaPmIWRanis_bLSQ9aA7sdRw4mSjOigNVdzko27ONvN2h5MukModoVT0piYDi4tHW3iQMv3xEsx6ry9ALNZ8rgaG-d1SIBBE93hwpG2yQlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برو کصکش، بزنید کص کون شونو خونی بکنید کصکش پدرا رو همین مونده این کونده باقالی ها گوه خوری کنن کله پدر هرچی شیخ نشین کصکشه</div>
<div class="tg-footer">👁️ 910 · <a href="https://t.me/SorkhTimes/131438" target="_blank">📅 00:58 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131437">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
فرمانده نیروی هوایی امارات :
❌
حملات دقیقی در ایران انجام شد ما با همتای امریکایی خود درحال حمله به اعضای سپاه پاسداران و اطلاعات سپاه رژیم جمهوری اسلامی هستیم این حملات به رهبری فرماندهی امارات با حمایت ایالات متحده انجام میشود و حملات تشدید تر خواهند…</div>
<div class="tg-footer">👁️ 906 · <a href="https://t.me/SorkhTimes/131437" target="_blank">📅 00:57 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131436">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
فرمانده نیروی هوایی امارات :
❌
حملات دقیقی در ایران انجام شد ما با همتای امریکایی خود درحال حمله به اعضای سپاه پاسداران و اطلاعات سپاه رژیم جمهوری اسلامی هستیم این حملات به رهبری فرماندهی امارات با حمایت ایالات متحده انجام میشود و حملات تشدید تر خواهند شد!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 851 · <a href="https://t.me/SorkhTimes/131436" target="_blank">📅 00:56 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131435">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
فووووووری از آکسیوس: جنگ در خاورمیانه دوباره آغاز شد.اسرائیل نیز بزودی به این جنگ خواهد پیوست.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 835 · <a href="https://t.me/SorkhTimes/131435" target="_blank">📅 00:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131434">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
فوووووووری
با اعلام رسمی شبکه خبر ، جنگ با آمریکا مجدد آغاز شد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 861 · <a href="https://t.me/SorkhTimes/131434" target="_blank">📅 00:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131433">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
فرماندار میناب تایید کرد که پایگاه دریابانی میناب بمباران شد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 904 · <a href="https://t.me/SorkhTimes/131433" target="_blank">📅 00:49 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
