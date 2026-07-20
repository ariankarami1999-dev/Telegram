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
<img src="https://cdn4.telesco.pe/file/RVZYYWzaUqyi82X1EOAybPjls-dKsXvtMnCEMhggy13j9qS7bVEE8TvubgnSF_Y0eKlxGar7kOgXMHjOreL1uPRB8JdEjgu9DgGXLsw-MoPvTJiDdnPhL6MmRCsj8GxNKyVj6vYgXapDjumHZ-uMD3ZEaXNU5dNPXJ9SXF-VxsPLYWYxFO3CDubf79vtWaxxDuHDOrF_qxEqA9UYgPYcLuPertbA0Jc1fAKVRhOE6EEt2h1t_zqaVePMPIJrJOIMsI6vB0-JaEi2BmYvdzlHeO-xz8xko6SuSCo7pQsReNkte2KcSXANCsI_BgT2SulYw1ox2pPrVNY25_TU6aNsfA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 415K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 22:18:40</div>
<hr>

<div class="tg-post" id="msg-19079">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کانال ۱۲ اسرائیل: شنیده شدن صدای انفجار در بندر ایلات
احتمالاً این صداها به دلیل شلیک موشک به سمت اردن بود.
@WarRoom</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/19079" target="_blank">📅 21:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19078">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyGJnMmkbM6Eopfz98Dtoj59_5W8kTIqeL0WOplmNcH-CaSTy-_KxaOY96VCDLTLomGIfMYSbHpyYMbUOIVs5mxGaZugZEwjI9ZV0MTCMahdSg0FHVxcG0ETNvxYQa_cN2hCXy1YHLZsRB_Dn5p-lueMF0ZPyOhKe_bb1rUsv7lUhf2cMjyiRIRHN6uzrdR1DtZGg0auBRlFzQCn_5fI1Qqk9qhMnQ_YXRIpX_8bKb9Q4ha-hiigiw18kWh6Yp3EcrGFfLZjVxIfda2r3bAuOsTq-cZQVlb-IsTb2RPCs9NU1AbwkQKUC2QMHZ8GMQxifqRRg8p1ZbnC8f87tiVVWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشار همین الان سه تا موشک از غرب تبریز فرستادن خیلی صدای بدی داد
@WarRoom</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/19078" target="_blank">📅 21:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19077">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شلیک موشک از تبریزززز
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/19077" target="_blank">📅 21:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19076">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یک منبع امنیتی اسرائیلی به شبکه i24NEWS: ایالات متحده در روزهای آینده، مرحله بعدی عملیات نظامی خود علیه ایران را آغاز خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/19076" target="_blank">📅 21:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19075">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کاخ سفید:رئیس جمهور دونالد ترامپ، فردا شب در مراسم استقبال از تابوت‌های سربازانی که در حمله جان باختند، شرکت خواهد کرد. این مراسم در پایگاه هوایی دوور (Dover Air Force Base) برگزار می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/19075" target="_blank">📅 21:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19074">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPSYNB0p-X2QayUiWWehV44ImM3WVlzLVXUUClUu8ktFytOfizM_fhdO067tXnrLDhQ7xbKpV3aunCplvFBvIAQPhMXXXRMgS8gLNLHsiUqcCkwt_mEnK0w6D9FC0bQFwuP-PJNehjzA-w4CyZHImW851X5BgvDIfuogngV8m-CJGm_pIldUkyfVlb5Nn4wCuJEi2688RI4hgwtSDV5qYELDQoBeuYneUlyXtPbz8sxi8ffE7BbI7ilzYXpb8asKwsbeFPirLnv8IO7bMmehA8MMP9_mlcSMMc_Imu74SUAmx2AL2CJ1C0nlDxJ72ZsoaXdyTbPk5CgOYPw0RPgQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد گزارشی از وقوع یک حادثه در فاصله
۸ مایل دریایی شمال‌غربی کومزار، عمان
دریافت کرده است.
افسر امنیتی شرکت کشتیرانی (CSO) تأیید کرده است که کشتی توسط
یک پرتابه ناشناس
مورد اصابت قرار گرفته است. خدمه کشتی با ایمنی کامل آن را ترک کرده و توسط یک
یدک‌کش
نجات داده شده‌اند.
آتش‌سوزی همچنان مهار نشده و کشتی در حال حاضر
بدون کنترل و در حال حرکت سرگردان
است. همچنین تاکنون هیچ گزارشی از
آسیب زیست‌محیطی
منتشر نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/19074" target="_blank">📅 21:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19073">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">منبعی در سپاه پاسداران به نایا که از افشای نام خودداری کرد: تیپ ۶۶ ارتش ایران از دزفول به سمت آبادان منتقل شده و نیروهای ویژه هم در آنجا حضور دارند. این عملیات احتمالاً در جزیره بوبيان انجام می‌شود که محل پرتاب موشک‌های آتش غیرمستقیم آمریکایی ATCAM به سمت جمهوری اسلامی ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/19073" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19071">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmmL2u25teoKJq_RtuZMxEy5cA4rKJnOyOUdmDV9Aqw90JNzntEDkd-Nhn6xKOoipLPB47_LgZBNFvTnyppxQXQYUfCAo76MoQLwHt-MNRCmQ4LbSeFF388qpLv2pLy-2YTzyzcmyEIFjkTeVKDqVHvooNL5cv5P6T9QGkaXdMTCHcrp04Os2fbohyDX9zNJT4AaZNB_LlZOi_5xlWekBNRLx3KLE3YgCYs3XAnuvdAXPwwy_VSLf9gFRgIDHC2XiNDxY4YVWSEf4_LCOdgtq0aJfdfT2VNR1gdIGAM6Eb3qqOZloZGYBxIOrbIdbUuzW2lXCb_QPXcILurRxGg7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز تجارت دریایی بریتانیاUKMTO: یک کشتی در 17 مایل دریایی شرق دیبا، مورد اصابت یک پرتابه قرار گرفت و باعث آسیب به چرخ دنده فرمان شد. تلفات جانی گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/19071" target="_blank">📅 20:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19070">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کانال ۱۲ اسرائیل: جلسه کابینه امنیتی و سیاسی اسرائیل درباره ایران با حضور تمامی فرماندهان و رؤسای نهادهای امنیتی آغاز شد
@WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/19070" target="_blank">📅 20:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19069">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReESBOCDqpsHY1YKuSWJPfZn-Zy8R5ST5ArWum7_v3abphytjSmEVSYJokLDgzYpyZ59e2slKlxh1QU0rgUX921x2CeMWIfgMXyoy0oe_fr7SvJ_KMEYH6WlqPUKunjD5uty9fwBu0wtwDL9158lm2yxss39ILUdJEWWCo0pm1BxUs-ozUAx5wWxkXeJ3yOeb5Fp8vcNyrlxsqbENJYtJndkr7z76Ef72ZD9wz2BlCDzqlsw1Q3bo-Uy0bIkjKrFpN2TY9q7CQEy5FU-b9w2WxUr9X1DU9UZarX8g_sAWwQiMIk-zctiPCUszEIn1psdqN4N1HEHjLGhA6GQlOQcZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
بنیامین نتانیاهو در مدت حضورش در ایالات متحده آمریکا،
به هیچ شکل و تحت هیچ شرایطی بازداشت نخواهد شد.
او در حال مبارزه با
جمهوری اسلامی ایران
است؛ حکومتی که به گفته ترامپ،
به‌تازگی ۵۲ هزار معترض بی‌گناه را کشته
و طی
۴۷ سال گذشته
نیز مسئول کشته شدن سربازان آمریکایی و افراد دیگری بوده است.
تنها کسانی که باید بازداشت شوند، افرادی هستند که ایران را به این
چرخه بی‌سابقه مرگ و ویرانی
کشاندند؛ موضوعی که
باید سال‌ها پیش و در دوران رؤسای جمهور پیشین آمریکا با آن برخورد می‌شد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/19069" target="_blank">📅 20:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19068">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رسانه تندرو عراقی : ایران آماده حمله زمینی به کویت شده، شاید امشب!!!
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/19068" target="_blank">📅 20:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19067">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDxQ2U37e5Rzbb7rAzGIaRTA0yPHPTkeYmljPfsIiJeN0ihOyvSyjr4zyWeQzmQOSus-Ka3RlU6NbplCfWQfuIdZFZM4Yc2Lj-SOpum-oc_-jXQrHx_zTTcbsFU3hwIFxCgHdJ5vjFowAdPc36m-jS5bczSP8ODLZT1hbE9_I6XK_5fRf0qdDpqyRlveQO2_27ATmK8FqHSbdVdyxHqGXM8u-kCoOBi6mt1oynobRIdjV6e54qwWGZjdyWr9aEXoOLqMQsXBeK6HcpBuDpwgqsjDkZTB_GGz_BVZmBQXqObE2LS5hI3w0bG1FPDHfIDg90uQKkbEJZMjQI3Og3A4rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ
در‌تروث
:
«هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن را
چندین برابر
خواهد پرداخت.
این دستور به
وزیر جنگ، پیت هگست
،
رئیس ستاد مشترک ارتش، دنیل کین
و
تمام فرماندهان نظامی
ابلاغ شده است.»
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19067" target="_blank">📅 20:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19066">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اف‌بی‌آی: هزار دامنه اینترنتی پخش‌کننده غیرمجاز مسابقات جام جهانی توقیف شد
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19066" target="_blank">📅 20:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19065">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naaqSQ3UzivlNb8Iu-k_DI2BAlN7dLPIg9Hi8HxOgZzMeM0SyB54M7Kg2HQPBbNrniuY1URLvi-FxJFcyREZhv2DnDht3i_9GSJtGRhPXfwkTCedUDGLm5wC5A7x5DdZ92L-Wss_lytu29_ocjupRFd085xiekhbsI25eILAYxQikoJu64dyoMVHgzJR3rcIdtmsI5rxFfyvu8MToCB0T6DtYkN19qjDSHllt5NDWPN9d53iHJTEaHWCHRPZgGSflU9Hy1WPFEJh8RwEdsjBfEEKTr6Bt8SfNLmUOc3y11EXBXDxRj1HX6gi-DuF7wUG5kjo6nHCErcCf9gxWwUBog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فدراسیون فوتبال اسپانیا تصویر دونالد ترامپ
و اینفانتینو رو از عکس دسته جمعی لحظه قهرمانی به کمک AI حذف کرده حالا همه توی کامنتها دارن به این قضیه اشاره میکنند
@WarRoom
😁</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/19065" target="_blank">📅 20:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19064">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یک واحد صنعتی در حومه شهر خمین هدف حمله قرار گرفت
معاون سیاسی امنیتی استانداری مرکزی: این حمله حوالی ساعت ۱۹ روی داد که تلفات جانی در پی نداشت و خسارات احتمالی در دست بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/19064" target="_blank">📅 19:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19063">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23dac038f.mp4?token=XSlhuLJcQe2OjpeNvULVsWTVWxZx8UtxHBDLmHFmQPkRM61yOZxeIUzALmi3nGEm5kn0YlF08dFwV81PUHghWTKlarUHRHavp1wbBGrC29uS05ssRRi_kOXsOeLySZsHtJuavEoWVB8xwhOjpdhYWxNoGDPW9_r-O531jYE6eJbm9JDw3Bq8UnxsP9ShItCTQmxQ9PxHJxXCD5yKk14574D57aEHf9s0v7b3cO7F6mG8llcUwN-XZxJTl_rzr4QKXPbXaAMaVRHZcwpaAh6PAxIXrvdi2JJcrUgWF-VB7fzR-jDakau6XZ5S0o0es9PyASLRncuLA_5UXzIEJJ9iJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23dac038f.mp4?token=XSlhuLJcQe2OjpeNvULVsWTVWxZx8UtxHBDLmHFmQPkRM61yOZxeIUzALmi3nGEm5kn0YlF08dFwV81PUHghWTKlarUHRHavp1wbBGrC29uS05ssRRi_kOXsOeLySZsHtJuavEoWVB8xwhOjpdhYWxNoGDPW9_r-O531jYE6eJbm9JDw3Bq8UnxsP9ShItCTQmxQ9PxHJxXCD5yKk14574D57aEHf9s0v7b3cO7F6mG8llcUwN-XZxJTl_rzr4QKXPbXaAMaVRHZcwpaAh6PAxIXrvdi2JJcrUgWF-VB7fzR-jDakau6XZ5S0o0es9PyASLRncuLA_5UXzIEJJ9iJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجاری در نزدیکی ساختمان فدرال نیویورک رخ داده گزارشی از تلفات احتمالی منتشر نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19063" target="_blank">📅 19:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19062">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سنتکام : نیروهای آمریکایی مسیر حرکت ۷ فروند کشتی تجاری را تغییر داده و یک فروند دیگر را از کار انداخته‌اند، از زمانی که این کشور محاصره بنادر ایران را از سر گرفته است
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/19062" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19061">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ارسالی : شیراز صدا انفجار اومد همین الان سمت قدوسی شیشه ها لرزید
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/19061" target="_blank">📅 19:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19060">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039c676d1e.mp4?token=jUvn4v5Fblhl1rKdYmdOJoZeml0_4Q1mfTzoT-0S_CgWdzJ0pCG-Wr6uHVldVjLO7urw2GHztji29sKwcItzrOrncTTipp7erZ6ZGohOaVqtnvCiQY5erzYIK4IVUFSA-1OY3aNIBNo0UW0vWfwJSkQldaY_YGl-fLLMuaHWbsQG1nsQ8U9rDNoPw4ldB7VaSyCCThcthvP9P-N4WB8Y82Qewns8WUd5ni3DESczAWILhe5ban60ikSkr2bBKUgII5l-DzoZRFblbRzvisZOKT-j_DG0KCnSwJN6dXiN7VP2ibvy6QVOBB2Tn_JHONcC8eHU41UVZ14Uh1eeMoj98w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039c676d1e.mp4?token=jUvn4v5Fblhl1rKdYmdOJoZeml0_4Q1mfTzoT-0S_CgWdzJ0pCG-Wr6uHVldVjLO7urw2GHztji29sKwcItzrOrncTTipp7erZ6ZGohOaVqtnvCiQY5erzYIK4IVUFSA-1OY3aNIBNo0UW0vWfwJSkQldaY_YGl-fLLMuaHWbsQG1nsQ8U9rDNoPw4ldB7VaSyCCThcthvP9P-N4WB8Y82Qewns8WUd5ni3DESczAWILhe5ban60ikSkr2bBKUgII5l-DzoZRFblbRzvisZOKT-j_DG0KCnSwJN6dXiN7VP2ibvy6QVOBB2Tn_JHONcC8eHU41UVZ14Uh1eeMoj98w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب شدن موشک از لار
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/19060" target="_blank">📅 19:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19059">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزیر امور خارجه فرانسه: امروز، تعدادی از کارکنان سفارت ما در ایران برای چند ساعت بازداشت شدند، مورد بازجویی قرار گرفتند و تحت فشار و تهدید قرار گرفتند. اتفاقی که برای دو کارمند سفارت ما در ایران افتاد، بدون عواقب نخواهد گذشت. دو دیپلمات در سلامت هستند و در ساعات آینده به فرانسه باز خواهند گشت.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19059" target="_blank">📅 19:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19058">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هواپیمای هیئت ایرانی منتسب به وزیر امور خارجه عباس عراقچی، در حال فرود در فرودگاه اسلام‌آباد پایتخت پاکستان میباشد. @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19058" target="_blank">📅 19:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19057">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کمی پیش پرتاب موشک از شیراز و هم اکنون پرتاب موشک از لار !
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19057" target="_blank">📅 19:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19056">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJNEJzvgwk7K4G0AqauiVUvfgG6Xh01bpguHseU53PmfoeUP06K7joN1tKaYwVmobrvdcVp8n1HglMbl51WjmKDXTk9jRpExlpF3csJTsHozcc5bskP7R4tZ_JwJ2bYroO0TCF7BNpCY22AmT6Y77HcTdAkL0Z9VYIMulzqILa8M2wwNkjJxILDwlcKHeiTvIZdZ4o6yV6dVi-LBnxrWymujDj2IwiOEe9yDqxUuCWHjXWXGPFLRbGdCIgFLWEYkxySsJwQ7vE_lP_9y3BOz0_NOKh5IR6UQiZ2ADm1tDF9yNmCppDOyOTVHJkzf5OcX-o-73R2fHkjmEjzNwnONrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هیئت ایرانی منتسب به وزیر امور خارجه عباس عراقچی، در حال فرود در فرودگاه اسلام‌آباد پایتخت پاکستان میباشد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19056" target="_blank">📅 18:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19055">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تنگه دعوا شد ، صدای انفجار‌ از تنگه
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19055" target="_blank">📅 18:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19054">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏
اکسیوس:
عقب‌نشینی ارتش اسرائیل از "مناطق آزمایشی" در جنوب لبنان، فردا سه‌شنبه آغاز خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19054" target="_blank">📅 18:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19053">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ddb70d86.mp4?token=bKSNeQlLYjZa3iXL-F7547ccRp9ziRgAIhWSYfJ22L-RSYff1mrdmqiZtIfSSALHud_RWn50i8eFEe59gTRDgvn_avokyojWXCXuhp4Z_ztjIBTls2dqh2gTZEjMMMVwaqx_JfUWRdlNWpRM9HcoAu5ILG_mn4XV8lAYR2d7B7BBcTbrz6Bl4eblT_qJ5Hmi78oyUJtSzQpA3xx2R4Bf3qbZfFY06ELHW4vc3Yn-1dXZsW5suOaSgDHMsxoynjnu4gIdKFSEd0xhFPVnsMEsgUKwirLF8y5p6zimbqe1o84pF8K0mK2wpfGQCy4eP10d93-akHpkUVsvtof1KAJVAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ddb70d86.mp4?token=bKSNeQlLYjZa3iXL-F7547ccRp9ziRgAIhWSYfJ22L-RSYff1mrdmqiZtIfSSALHud_RWn50i8eFEe59gTRDgvn_avokyojWXCXuhp4Z_ztjIBTls2dqh2gTZEjMMMVwaqx_JfUWRdlNWpRM9HcoAu5ILG_mn4XV8lAYR2d7B7BBcTbrz6Bl4eblT_qJ5Hmi78oyUJtSzQpA3xx2R4Bf3qbZfFY06ELHW4vc3Yn-1dXZsW5suOaSgDHMsxoynjnu4gIdKFSEd0xhFPVnsMEsgUKwirLF8y5p6zimbqe1o84pF8K0mK2wpfGQCy4eP10d93-akHpkUVsvtof1KAJVAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما
زنده : مردم
عرزشی
بندرعباس با زنجیره انسانی ۵ کیلومتری به آمریکا پیام دادند: اگر از سد نیروهای مسلح عبور کنید، با ما طرفید؛ هیچ صلح و دوستی با ترامپ نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19053" target="_blank">📅 18:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19052">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دیدبان اتاق جنگ : سلام یاشار بندرعباس کلی موتور کراس با اسلحه  دوشکا ار پی جی اومدن ساحل مستقر شدن
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19052" target="_blank">📅 18:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19051">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خبرگزاری صدا و سیما : بر اساس گزارش‌های اولیه، یک نقطه از شمال‌غرب شیراز هدف حمله هوایی دشمن هدف قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19051" target="_blank">📅 18:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19050">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش‌صدای‌انفجار جدید شیراز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19050" target="_blank">📅 17:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19049">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97808c9f22.mp4?token=s47Y0uACjeX2rerdl1uOPTdCJ_fMGoGf2pndIgigOZP9gZVFBzcbwrTfcjdmWWKhFBaaBmhThl8BxHLHhtLUFLYFosfBmUQwCg14wxR8bqHsk252SSGyKDswhpsNGVUbmiBDJv6CSFCzrx8VXEwVnDUTzwhnQhqSycGF_JIIzCOoQVONE2m20Ry36YpCQy6wWMM8pOB3h3b78xAQWIdw-JphU_DompH_WPkvcTOEPnVbOYRVUrn30Gz-Sc0SUhbTtTsn1mFxB5XkPEzD1oSrVVVWAz3dzMJFabfzPIx2Wlvk3V5Gqyqt491I7WyxINv0n_jgBuo5JZmRxUOWeYwzfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97808c9f22.mp4?token=s47Y0uACjeX2rerdl1uOPTdCJ_fMGoGf2pndIgigOZP9gZVFBzcbwrTfcjdmWWKhFBaaBmhThl8BxHLHhtLUFLYFosfBmUQwCg14wxR8bqHsk252SSGyKDswhpsNGVUbmiBDJv6CSFCzrx8VXEwVnDUTzwhnQhqSycGF_JIIzCOoQVONE2m20Ry36YpCQy6wWMM8pOB3h3b78xAQWIdw-JphU_DompH_WPkvcTOEPnVbOYRVUrn30Gz-Sc0SUhbTtTsn1mFxB5XkPEzD1oSrVVVWAz3dzMJFabfzPIx2Wlvk3V5Gqyqt491I7WyxINv0n_jgBuo5JZmRxUOWeYwzfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار شیراز ، گویا صنایع رو زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19049" target="_blank">📅 17:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19048">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">عضو کابینه اسرائیل، الی کوهن: "ایران به خوبی می‌داند که چرا در دو هفته گذشته به اسرائیل حمله نکرده است. اگر مرتکب اشتباه شود و حمله کند، ما با قدرت بیشتری نسبت به عملیات قبلی پاسخ خواهیم داد. ایران به اسرائیل حمله نمی‌کند، زیرا از عواقب آن هراس دارد."
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19048" target="_blank">📅 17:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19047">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارشهای متعدد از شنیده شدن صدای انفجار مهیب در شیراز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19047" target="_blank">📅 17:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19046">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65823663be.mp4?token=ZJcfsZLuNPI0kqCKvmNcWbF9ivA5tMlkCjOVYvVrjxJnHXJ3XIY34sGMZFaeXwPgXASa2T-y8vf-0KrPWvfZu5r9OMlS6_w4qzww9sA3gcv-WVKYlTT6hoMxsl_Bmm6V23OCa9Ak8PxYqKWJzcn7cMKhfkRlC4hKPfrnltrjJ-lAVLgi8qCslN3Xczk0Ji5l0vm1E1wBzPwad_Quw4Pr6DMdrBGOQxd3bzkkswaFlZHCOx8Dlgnpf46HYJmPPNIiW3KqodXI-wRUBm7AK9GtYC7K7yUNnB1C8U8cboYwGZk7u2Ug9PO5qo50N6VEaW1Xy9Eug4yDC95DG2xfzLpq3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65823663be.mp4?token=ZJcfsZLuNPI0kqCKvmNcWbF9ivA5tMlkCjOVYvVrjxJnHXJ3XIY34sGMZFaeXwPgXASa2T-y8vf-0KrPWvfZu5r9OMlS6_w4qzww9sA3gcv-WVKYlTT6hoMxsl_Bmm6V23OCa9Ak8PxYqKWJzcn7cMKhfkRlC4hKPfrnltrjJ-lAVLgi8qCslN3Xczk0Ji5l0vm1E1wBzPwad_Quw4Pr6DMdrBGOQxd3bzkkswaFlZHCOx8Dlgnpf46HYJmPPNIiW3KqodXI-wRUBm7AK9GtYC7K7yUNnB1C8U8cboYwGZk7u2Ug9PO5qo50N6VEaW1Xy9Eug4yDC95DG2xfzLpq3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از امیدیه خوزستان الان
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19046" target="_blank">📅 17:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19045">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هم اکنون چندین انفجار کویت را لرزاند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19045" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19044">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-W4yHdvHJkToR6tQApBScjjS01TY5YDmKyNJVWye1hgvUP2Lr9fBBdwsgZo4xVaBavIicKkzoywg0A5BZwjD91u5fWNUM1tvJINoe4Z2d66SNhgQ0liNTYlK_OlIw37sr-CyHU4QB84ccoVHnDznOV5sdOnJYopqOKv_YR09wThcYg0tnHrIaaM6jUqODv9u9BlFfRcJJXKSTD4MZCciJ14Mh3167AjGc_WGQFWtQmw33FV3u_rZ7MDrbtyK7EnZDDpaCJEl4RX-FQyVt_Mp338ooCcEaf8YfADDQKVdggD3pVeZzocJIEHGo1C-YlMgbdMGJE1hdpqtPsMxXZHhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریانوردی بریتانیا: حمله موشکی ایران به یک نفتکش عربستان سعودی در تنگه هرمز ، الان @WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19044" target="_blank">📅 16:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19043">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صدای‌انفجار بندر عباس‌ مربوط به نابود سازی مهمات جنگی بجا مانده است
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19043" target="_blank">📅 16:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19042">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تحلیلگر نزدیک به سپاه:
پیشنهادات اخیر آمریکا شباهت زیادی با الگوی پیش از دو جنگ 12 روزه و 40 روزه دارد،
اعزام گسترده جنگنده های آمریکایی به خاورمیانه در روز های اخیر از قصد آمریکا برای جنگ جدید خبر می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19042" target="_blank">📅 16:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19041">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chj2Q4hfxPcaTvyqUK4z_qWwftTy24-SwRbh6swvBVqqKbcOp4iAt3gCqbiF-TabCxXWXkqefXL5V6YxBd8fIrNM-Z338bZvF64ANXC4HRM4xjssuvDwLkOvtUue-pGUsTh0QziN2RawDiRrrjNSbh1d3UKeluAvaaCu3vYFND5mLzhcp6-0uI26GeFCw_PZgU0Gyh87-W3RYPa8nFUGp0c1BzdKRexPwTUxrw3zjNtac0h8esIP6T_8DU7cPfSqR5JOMOa_ajsVVTJU1CCkKOeh89AKLM2157KeT2WIxLmSd8pdWZn6NDXeiCPb26aYUXGcqiMt8atX3URTBxnEzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ توییت مسیح علینژاد درباره اعدام یک جوان ۱۹ ساله ایرانی در جریان اعتراضات دی ماه را بازنشر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19041" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19040">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">درگیری‌های حوثی-عربستان سعودی:
حوثی‌ها اعلام کردند که محاصره دریایی عربستان سعودی را در تنگه باب‌المندب آغاز کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19040" target="_blank">📅 16:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19039">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نیویورک تایمز: تهران و واشنگتن در آستانه یک «لحظه سرنوشت‌ساز»  بر سر جنگ قرار گرفته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19039" target="_blank">📅 16:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19038">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بحرین : ایران ساعتی پیش به سامانه‌های ناوبری هوایی ما حمله کرد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19038" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19037">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مقام آمریکایی به CBS:
تشدید تنش به زودی آغاز خواهد شد،
هواپیماهای ترابری و سوخت رسان آمریکایی به صورت پی در پی و بی سابقه در حال ورود به خاورمیانه می‌باشند
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19037" target="_blank">📅 14:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19036">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ممباقر بعد از چند ماه عضویت در اتاق جنگ با یاشار : آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و می‌گویند دنبال توقف جنگند. روی هوش ما اندازهٔ آی کیوی مختصر خودشان حساب کرده‌اند.
ما در شناخت این آمریکایی‌بازی‌ها به مرحلهٔ استاد تمامی رسیده‌ایم و بر این اساس آماده شده‌ایم. اقدامات باید مؤید ادعاها باشد نه ناقض آن‌ها.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19036" target="_blank">📅 14:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19035">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyGeEm95MMXQg8DEN5-yqAQUhAYeFAQiHAQn8zgQ12eakiY-SDjZ_H0Dpm0PUuyP1wWRUXn67_RHeXrsXoiEgg36K1jrJaIEwq1SR6B7-wXi-EefJLbAQwjQCk8zcqSwPgUPa1rLX8VkJNoq0A45xGj2tbkJFoaCHXFwpSn8LXjefPXy9jr7vgjJcGhAy2p6SL0htJUvhd2dz7Ce95fi5tE6LlCRXsiK_IZTRrNUC2PoBHZC7NxY6KHbfbmOo3Q4pPU1FObxQiali_JcMQr_H9j9YipjltVmV7tSNctdqFWrHqE4o4HBGYXxDw5x__xddzF8GXvMW-Kk3krVBOCDkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به دنیا آمدن پسر معاون خود جی دی ونس را تبریک گفت.
پسری به نام
Alec Neel Vance (الک نیل ونس)
. در بیانیه مشترکشان اعلام کردند که مادر و نوزاد هر دو در سلامت کامل هستند.
فرزندان جی‌دی و همسرش اوشا ونس(حقوقدان آمریکایی با ریشه هندی) (خانواده‌ای از مهاجران هندیِ تلوگو)
Ewan Vance (ایوان ونس)
– متولد
۲۰۱۷
(پسر)
Vivek Vance (ویوک ونس)
– متولد
۲۰۲۰
(پسر)
Mirabel Vance (میرابل ونس)
– متولد
۲۰۲۱
(دختر)
Alec Neel Vance (الک نیل ونس)
– متولد
۱۹ ژوئیه ۲۰۲۶
(پسر)
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19035" target="_blank">📅 14:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19034">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STC0mrlK2P7gSfXL5aXKh_lyIJIbiJCcX7dzwi96Rqai8ZnDTquWDALiAHHImOnnhxOUEXKR678CRIGLaZCk0EXZqUZ41gpphAdi7XH-GVoYaRDh57aQBb6l8ZGrZURayMm6qKo_xxBrKkHn2HfpTQHyygOlZgpKIKQ4RTmyLPVy0KD66PjIpM_gdW1uhdG8lXaCo2LTMO2LKF4_vRNOuGgF_qMx6_6kK_40wuvaIlVYLh9ehK8Q2NeC81EQm5-s8KrmVEyaMZSZAp0ImTAJgCRmJJUUGTDvVjtCPfltpiBjnebueoweurHRLk-L-50nCTgEVODarPnP3eZT4bgh2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای نتانیاهو  به مقصد نا معلومی بلند شده سپس چند دور زد تا جهت مقصد گم شود و بعد فرستنده خود را خاموش کرد!
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19034" target="_blank">📅 14:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19033">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کیر استارمر
امروز،
۲۰ ژوئیه ۲۰۲۶
، در دیدار خصوصی با پادشاه، استعفایش پذیرفته شد. چند دقیقه بعد، جایگزین او
اندی برنهام
، رهبر جدید حزب کارگر مأمور تشکیل دولت شد و قدرت رسماً منتقل شد. این انتقال معمولاً در فاصله حدود ساعت
۱۱:۴۵ تا ۱۲:۰۰ به وقت لندن
انجام می‌شود(حدود ۳۰ دقیقه دیگر بهصورت رسمی)
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19033" target="_blank">📅 13:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19032">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8bc26544.mp4?token=TP69k1zV3L9YbESg6fVWKlaOufZK3YXN2HYBL8J50ioGhrazjUJkG2CFS_HZXbe14tuRUPS_uYsHaowur4dtRu6XfYwMXT6pFMsXiqp_WfOQdU7ejNMOZxFA1UPX55oBJnfcH6LMMeRNCdoFOmGrCdR9k56cDf4OTMaddkkZxxJHRBKU-2IdWR0reOcWhmM-2vtnLO74i4Cihwar_Gq14I5OiqQ1jJm3S7MdYK0fjojclx6i1zt0SNjHboKF_hjCFOpHZ2EU9F_c4__HkByk_Sc-CsIeuFsETtCRPrIITpV4QmKBnOLk2y3qoJoCTxAjacBjnxtpsPDV0xl4OAswIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8bc26544.mp4?token=TP69k1zV3L9YbESg6fVWKlaOufZK3YXN2HYBL8J50ioGhrazjUJkG2CFS_HZXbe14tuRUPS_uYsHaowur4dtRu6XfYwMXT6pFMsXiqp_WfOQdU7ejNMOZxFA1UPX55oBJnfcH6LMMeRNCdoFOmGrCdR9k56cDf4OTMaddkkZxxJHRBKU-2IdWR0reOcWhmM-2vtnLO74i4Cihwar_Gq14I5OiqQ1jJm3S7MdYK0fjojclx6i1zt0SNjHboKF_hjCFOpHZ2EU9F_c4__HkByk_Sc-CsIeuFsETtCRPrIITpV4QmKBnOLk2y3qoJoCTxAjacBjnxtpsPDV0xl4OAswIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روبیو به سی‌ان‌ان: از طریق کانال‌های متعدد، نشانه‌هایی مبنی بر تمایل ایران به مذاکره به دست ما رسیده است، اما شکاف فزاینده‌ای در درون نظام وجود دارد.  اگر ایرانیانِ خواهان مذاکره بر اوضاع مسلط شوند، این یک تحول مثبت خواهد بود، اما چنین چیزی رخ نداده است. @WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19032" target="_blank">📅 13:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19031">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118dddcf1a.mp4?token=QyN45YNLOTmIqiF3NJsut5hxBMqlYqVRkd1Z1Qw4emlTL6wu-XELx-WdG-Y0FhoZ10slIsDnW-RZOCPpM35GrvrCIZhA8-0XzfOFRGHaj4Fkklu23WAg-ZmNuub_TMxpKbjzW4gGWR1GHnlQ4jcFN9n760UJ2gUhkX2Yk4Cmwpzbf9v1jNFlB9dmtrSZkNdgNrlYdPHrNZKgS3tUm7sBBfQeFZHHvUQvxUWmiIq-9CEtNEgHmKBPGV7QyUkGs-CJ6qntC2cOfV9L2rAwZhwPMLXcnVSU-7F5H0KNsz6ge8xojvBPXA8kBsi6hBzjeKtLDX5C52StNdiYYE0_G7WyC4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118dddcf1a.mp4?token=QyN45YNLOTmIqiF3NJsut5hxBMqlYqVRkd1Z1Qw4emlTL6wu-XELx-WdG-Y0FhoZ10slIsDnW-RZOCPpM35GrvrCIZhA8-0XzfOFRGHaj4Fkklu23WAg-ZmNuub_TMxpKbjzW4gGWR1GHnlQ4jcFN9n760UJ2gUhkX2Yk4Cmwpzbf9v1jNFlB9dmtrSZkNdgNrlYdPHrNZKgS3tUm7sBBfQeFZHHvUQvxUWmiIq-9CEtNEgHmKBPGV7QyUkGs-CJ6qntC2cOfV9L2rAwZhwPMLXcnVSU-7F5H0KNsz6ge8xojvBPXA8kBsi6hBzjeKtLDX5C52StNdiYYE0_G7WyC4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستند ساز حکومتی در صحبت با عراقچی : ترامپ راست میگفت مشهد سقوط کرد بود !
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19031" target="_blank">📅 13:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19030">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjUrX36Ot1N7J0PPFCsJuOt4-tiD7WokDZkYz9OjFYVhI-En5jpPmHIegh8XPyXCxNfjhxJAXqYj5-rMTYPEyXfyVyZSZqP_xJaTOth_xlmXJ5VgKgzBtBy_ADpQdUQWe0oYYNLfpPYyAQKbNkbLZR0RgWHkZxz54A0TQfeAVQuMdyxuvrPHgzDgWEKtQ6dP4j20DXRLBSF5NqkU_RBrrAGMeDiJRQYGTWWeICK4I42iHLK1m_0Nsaoh45_JLMjfPi25jeipNmVTr9RZ-oQJ9LVgN_5_GTmWsHBRch3u_XEFTUe0LgEx-4HLDaXmrwqWmqNRvj9ZPcyiOUdU8k5SLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون عملیات سنگین اسرائیل در نبطیه، جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19030" target="_blank">📅 13:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19029">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">روزنامه اسرائیل هیوم : نتانیاهو امشب جلسه‌ای امنیتی را به دلیل تشدید تنش‌ها با ايران برگزار خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19029" target="_blank">📅 12:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19028">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سازمان دریانوردی بریتانیا: حمله موشکی ایران به یک نفتکش عربستان سعودی در تنگه هرمز ، الان
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19028" target="_blank">📅 12:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19027">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نیویورک تایمز: پنتاگون ده‌ها مجروح از نیروهای ارتش آمریکا در جنگ با ایران را پنهان کرده
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19027" target="_blank">📅 12:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19026">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">عراقچی مدعی شد دونالد ترامپ در روز چهارم جنگ با سران گروه‌های مسلح کُرد مخالف ایران در شمال عراق تماس گرفته و از ورود زمینی آنها به ایران حمایت کرده بود. او افزود پس از اطلاع از این موضوع، با مقام‌های اقلیم کردستان عراق، نخست‌وزیر عراق و هاکان فیدان، وزیر امور خارجه ترکیه، تماس گرفته و نگرانی‌های تهران را منتقل کرده است.
‏به گفته وزیر خارجه ایران، دولت ترکیه در جلوگیری از این اقدام نقش مؤثری ایفا کرد و علاوه بر رایزنی با آمریکا، مواضع محکمی در مخالفت با این طرح اتخاذ کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19026" target="_blank">📅 12:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19025">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">روبیو به سی‌ان‌ان: از طریق کانال‌های متعدد، نشانه‌هایی مبنی بر تمایل ایران به مذاکره به دست ما رسیده است، اما شکاف فزاینده‌ای در درون نظام وجود دارد.  اگر ایرانیانِ خواهان مذاکره بر اوضاع مسلط شوند، این یک تحول مثبت خواهد بود، اما چنین چیزی رخ نداده است.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19025" target="_blank">📅 11:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19024">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f146b0f2.mp4?token=pi5ycDDV4dmwGDLlJNWXwEXd7qI0esPIIMzwiLeNVkaW7FMqB9G928UTbSZLcEzRXjGLujur7fCLitx8AL-t6cgfQgq2RKlcOYHpSfBjkj7tGvu6o9_47bq8leVfcbf7AwNg-RMR7QSBbpdSUDCduLuVioBTUhyyvnuQIkdN4--v_zX78ShAhw8ogVMNosiDXUXDAsHnFFHXLBCgIcrGSIxUXPu_0L6WPipFrGq9P9leqWHFDdTkKS-XDDXactVSkTGgCImNEuIqoKa8GfQHf_wAtJroc0PPABMNJqWC7xP7au-4Kp7o_7LuIeMtj3pm9WiipsSlhjCw5aYzlXMzqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f146b0f2.mp4?token=pi5ycDDV4dmwGDLlJNWXwEXd7qI0esPIIMzwiLeNVkaW7FMqB9G928UTbSZLcEzRXjGLujur7fCLitx8AL-t6cgfQgq2RKlcOYHpSfBjkj7tGvu6o9_47bq8leVfcbf7AwNg-RMR7QSBbpdSUDCduLuVioBTUhyyvnuQIkdN4--v_zX78ShAhw8ogVMNosiDXUXDAsHnFFHXLBCgIcrGSIxUXPu_0L6WPipFrGq9P9leqWHFDdTkKS-XDDXactVSkTGgCImNEuIqoKa8GfQHf_wAtJroc0PPABMNJqWC7xP7au-4Kp7o_7LuIeMtj3pm9WiipsSlhjCw5aYzlXMzqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت امر خارجه : در شهر به ما پیشنهاداتی شده
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19024" target="_blank">📅 11:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19023">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">صدای انفجار شرق تهران اعلام شده کنترل شده است
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19023" target="_blank">📅 10:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19022">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عمو یاشار تهران صدای انفجار اومد به جان مادرم راست میگم</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19022" target="_blank">📅 10:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19021">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐂𝐘𝐑𝐔𝐒 ¹⁰:⁴⁸</strong></div>
<div class="tg-text">عمو یاشار تهران صدای انفجار اومد به جان مادرم راست میگم</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19021" target="_blank">📅 10:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19019">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گزارش صدای انفجار جدید تبریز
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19019" target="_blank">📅 10:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19018">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اسکله سپاه طاهرویی سیریک همین الان ساعت ۱۰.۴۱ دو انفجار
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19018" target="_blank">📅 10:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19017">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">صداوسیما : انفجارهای تبریز اولین انفجارها از نوع خود از زمان آغاز حملات جدید آمریکا به ایران در روزهای اخیر هستند. @WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19017" target="_blank">📅 10:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19016">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نهاد دریایی بریتانیایی: یک کشتی که در فاصله ۸ مایلی شمال غربی جزیره "کمزار" در عمان قرار دارد، مورد اصابت یک موشک قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19016" target="_blank">📅 10:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19015">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">روبیو : هیچ تضمینی در مورد عقب‌نشینی اسرائیل قبل از خلع سلاح و انحلال حزب‌الله وجود ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19015" target="_blank">📅 10:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19014">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مهر : اصفهان رو چند دقیقه قبل زدن و یه صدای مهیب به گوش رسیده @WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19014" target="_blank">📅 10:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19013">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hr6WjCC2PGjtPLUpSai4iaYGz4nOsmymTibnSnv8m39c1TL468kT0rSrzeCeFr3n252ApuZNWqh4pDn0zUXzU6mGhsiYU861aSBkT3_mGti_bSu5ZnfUCxHKF2eJ0gDL0XXPCrgQoKQdf0mYyHJNJSsB4gQHNQtvUxFqUA1NnvlYQM4MqMwOalckXUiMeCrjqgBSFYIDPNfdvtyH-dllXkrrcKPmAisJwJC6dOgxdfi0VhuFia1CZEcf2ZLTI_wVmzMmPyANLbC8YojxtF0rOAhTP8OEFvDfA6B3-AZhlrj46qY53bYPqrhSn6HdfGZ6C2YznTkndmo7wtreMLBVvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ماموریت با موفقیت انجام شد . . .
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19013" target="_blank">📅 10:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19012">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مهر : اصفهان رو چند دقیقه قبل زدن و یه صدای مهیب به گوش رسیده
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19012" target="_blank">📅 10:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19011">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اتاق جنگ با یاشار :
امضای لرزه‌ای انفجار هسته‌ای با زلزله طبیعی تفاوت دارد ، ترس به دلتون راه ندید، ایران کشوری زازله خیز است، فقط الان هم زمان شده با جنگ
@WarRoom
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19011" target="_blank">📅 10:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19010">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وزارت دفاع بحرین:
هدف حملات هوایی شدیدی قرار گرفته‌ایم و سامانه‌های پدافند هوایی در تلاش برای مقابله هستند
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19010" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19009">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گزارش انفجار در کنارک
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19009" target="_blank">📅 10:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19008">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دو انفجار بوشهررررررر @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19008" target="_blank">📅 09:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19007">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نقطه‌ای در حوالی ارومیه نیز هدف حملات آمریکا قرار گرفت
مدیرکل مدیریت بحران آذربایجان‌غربی گفت: بامداد امروز، نقطه‌ای در حوالی بخش سیلوانای ارومیه هدف اصابت پرتابه دشمن قرار گرفت.
در پی این حمله چند نفر مجروح شدند که بلافاصله با حضور نیروهای امدادی جمعیت هلال‌احمر و اورژانس، اقدامات اولیه درمانی برای آنان انجام و مصدومان به مراکز درمانی منتقل شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19007" target="_blank">📅 09:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19006">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6PWYtRiGymq0vApBaXb7x_VImKwMcmAppRV2mYRqo_gzWVn6ifwfBnzf7CDTkH4CneypeaTRlPPZUO7rNgwZeh7xy4w3cTd_LJT1NDLcLhM_-JFR4VrBKXr7iS7YVAzD6MqkmdH_gWJCEtq3XC5ypgkwbcGLwe4DZJlZpNFYh8YCq4PgfDs3SDvgehO7_PgA_ROm4rp0M-CGSKpNtOkGnxMj7o-hoPKGkWuVISA5uTskFU5awfdiy6t6XNU0sBpRMi1B3b7GIfUCftLmrKtxAkIiysFeGT2s6K8GdacmkPWDE_Zk4rYMjR24uKDsF0yo7WjLug_e6dFG8ISdu5oLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو زلزله شدید ساعتی پیش به بزرگی 5.7 و 5.2 ریشتر در کوزران کرمانشاه به فاصله 5 دقیقه در ساعات ۷:۱۳ دقیقه و ۷:۱۸ دقیقه در عمق ۸ کیلومتری رخ داد
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19006" target="_blank">📅 09:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19005">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">صدای انفجار در بحرین
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19005" target="_blank">📅 09:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19004">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش صدای ‌انفجار اصفهان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19004" target="_blank">📅 09:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19003">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">واشینگتن: سفر رئیس‌جمهور چین، با وجودی که پکن به «دخالت در انتخابات آمریکا متهم شده»، طبق برنامه انجام خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19003" target="_blank">📅 09:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19002">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دو انفجار بوشهررررررر
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19002" target="_blank">📅 09:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19001">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">چابهار آخرین نقطه قبل ناوه دارن برمیگردن رو ناو بشینن هر چیزی مونده خالی میکنند چابهار …
@WarRoom
⚠️</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19001" target="_blank">📅 05:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19000">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">چابهار ۳ انفجار الان و ۲ انفجار کنارک
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19000" target="_blank">📅 05:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18999">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3690b0e4b.mp4?token=Q-R99BMG9TVbBApkzPdJoo93UcA6sMcf8tLcF-oW35T1fCAbsW6YI4jnwJmuYgZHiAuglG1WKf-ani9MMGzguQYyn3RUYu99Q1pKQx5qtASO5dUM4OzvtSpzg_uhkUDGJz5h-HYKS0Wr2bOYdw9izL_kiR39W4vgp_1BhnOB-c-3vQQrGzp_WIn78Q5qu5Ljw55HHaAVBu47d5NbCh1vfZYCOprLVtsi3XBnkb5O8yrYUPesAGW3pz1xfupCdRjUQ5ATRkXdajdHDIqvGIoD97WBtpDyMR-OmZWzTGJ_xnQyrFhmRCXTr6qWBCWrWNMIvuziTCE-QHhIVMGx3HHV3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3690b0e4b.mp4?token=Q-R99BMG9TVbBApkzPdJoo93UcA6sMcf8tLcF-oW35T1fCAbsW6YI4jnwJmuYgZHiAuglG1WKf-ani9MMGzguQYyn3RUYu99Q1pKQx5qtASO5dUM4OzvtSpzg_uhkUDGJz5h-HYKS0Wr2bOYdw9izL_kiR39W4vgp_1BhnOB-c-3vQQrGzp_WIn78Q5qu5Ljw55HHaAVBu47d5NbCh1vfZYCOprLVtsi3XBnkb5O8yrYUPesAGW3pz1xfupCdRjUQ5ATRkXdajdHDIqvGIoD97WBtpDyMR-OmZWzTGJ_xnQyrFhmRCXTr6qWBCWrWNMIvuziTCE-QHhIVMGx3HHV3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد
نهمین شب متوالی حملات علیه ایران
در
۱۹ ژوئیه، ساعت ۱۰:۰۰ شب به وقت شرق آمریکا (ET) (۰۵:۳۰ بامداد ۲۰ ژوئیه به وقت تهران)
با موفقیت به پایان رسید.
به گفته سنتکام، نیروهای آمریکایی
مراکز فرماندهی نظامی، سامانه‌های پدافند هوایی، مراکز دیده‌بانی ساحلی، توانمندی‌های دریایی، محل‌های پرتاب موشک و پهپاد، و شبکه‌های ارتباطی ایران
را هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری و خدمه غیرنظامی عبوری از
تنگه هرمز
بیش از پیش کاهش یابد.
سنتکام افزود که
به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)
، ارتش ایالات متحده ایران را در قبال اقداماتش پاسخگو می‌داند و نیروهای این فرماندهی همچنان در
آماده‌باش کامل، متمرکز، مرگبار و آماده اجرای مأموریت
قرار دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18999" target="_blank">📅 05:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18998">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سپاه:
هواپیماهای ترابری بزرگ C-17 و هواپیماهای فرماندهی و کنترل P-8 ارتش آمریکا با موشک‌های بالستیک در فرودگاه عقبه هدف قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18998" target="_blank">📅 05:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18997">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ارسالی : درود بر شما همین الان کلی امبولانس و اتش نشانی دارن میرن سمت خجیر ، انفجار بوده
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18997" target="_blank">📅 05:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18996">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18996" target="_blank">📅 05:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18995">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmQpXZTDOALOIp-NzzxW1H3bju5tF9ATmkLCGVGVchfFKR8JZDmohN6IOig4yGsPdenPlxl0h5_WRYX7xuatIWlIKx4Xu65lf1UMuXjp0f4KWgFRogVmqbQPsny__FEEDf7AQp4lqfgpR4DuqvDJe3N7E5w0e6CHb7P0_vRKVdwQmwBiOFyUfxq-LBR5fOE4rPcwWbTmwgDI9281k0Io8IXl6Zul7cEe_aUO8xU-C53VQX03N63mJL4Z91ajp_1SmCR1fkJUl9vVF0iL0IbrB1GF61UKQZvglwxO1J3IGgNqLXIlnXN6wD3V3hJVQ88bcn9Ym0G3U5HjHpSLWIgUUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : درود و عرض ادب یاشار جان.
من سمت شرقم و اینجایی که زده سمت خجیر میشه ولی من صداشو نشنیدم ولی دودش معلومه.
تاییده انفجاره شرق
@WarRoom
یاشار: من بالای پانزده پیام دارم که صدای انفجار را شنیده‌اند. حتی یکی از کاربران با ماشین در خیابانها افتاده و دنبال مکان انفجار میگردد. ممکنه حمله هوایی نباشد و یک انفجار دیگری باشد، ولی به هر حال این دود مشاهده میشود و صدا شنیده  شده.</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18995" target="_blank">📅 05:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18994">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شهرهایی که امشب تا این لحظه مورد هدف حمله قرار گرفتند؛
💥
تبریز
💥
بندرعباس
💥
چابهار
💥
ماهشهر
💥
سیریک
💥
کنارک
💥
جاسک
💥
خورموج
💥
دشت آزادگان
💥
خرم آباد
💥
سربندر
💥
دزفول
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18994" target="_blank">📅 04:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18993">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گزارش انفجار شرق تهران
🤯
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18993" target="_blank">📅 04:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18992">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گزارش انفجار کرمانشاه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18992" target="_blank">📅 04:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18991">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارش انفجار کرمانشاه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18991" target="_blank">📅 04:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18990">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دقایقی پیش, مرکز تجارت دریایی بریتانیا: گزارشی مبنی بر وقوع یک حادثه در فاصله ۸ مایلی شمال غربی شهر کومزار، عمان، دریافت شده و یک کشتی در حال سوختن است @WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18990" target="_blank">📅 04:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18989">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">به گزارش خبرگزاری صدا و سیما، حملات هوایی ایالات متحده بندر سیریک در جنوب ایران را هدف قرار داد تا عملیات جمع‌آوری اطلاعات ایران در تنگه هرمز را مختل کند.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18989" target="_blank">📅 04:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18988">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رسانه های رژیم : به دستور مجتبی خامنه‌ای ، موشک‌ها و پهپادهای "ولایت" به زودی به پایگاه‌های دشمن آمریکایی در منطقه ضربه خواهند زد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18988" target="_blank">📅 04:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18987">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ : اگر نگاه کنید، پس از حدود یک هفته و نیم تا دو هفته از آغاز جنگ، احتمالاً جلوی پیشرفت آن‌ها را گرفتیم؛ البته نمی‌خواهم از واژه «احتمالاً» استفاده کنم
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18987" target="_blank">📅 04:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18986">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">صداوسیما : انفجارهای تبریز اولین انفجارها از نوع خود از زمان آغاز حملات جدید آمریکا به ایران در روزهای اخیر هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18986" target="_blank">📅 04:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18985">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دریا بانی گروگ  رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18985" target="_blank">📅 04:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18984">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فاکس نیوز : فرمانده کل قوا(ترامپ) هیچگونه مذاکراتی رو قبول نمیکنه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18984" target="_blank">📅 04:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18983">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFu1DHOvBfGw2e7ay0nR8O7vaiLt9W6j1mkwpO8zprzuJKQhmRBMRZzQOz9iodMkRBjZwkpXPAASbmzHtg9ul76un3ZmfJXEeRnaX1TDMfmyK7VVRYalQv8jpfiyrf5tC6Jz-QdbQYgirZdN16qf3EqSit7dGM2fUwa7CJjB5DREWVpL_Qq_tIMd0zSTmwPngeH12ZjMKozGWqZzF-TDf6nL7bSo0SQD1jt2RunzBGmrKQQpvexRvq1ptv4PUqxiEVeyaiYKxPTdJe2AW23PJo9EtDZaz3vNvw4GrxKgi95rGi8E6sl3UD2EfJrDpzLcBgvRf4J9u8shyEoDoCtt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقایقی پیش
,
مرکز تجارت دریایی بریتانیا: گزارشی مبنی بر وقوع یک حادثه در فاصله ۸ مایلی شمال غربی شهر کومزار، عمان، دریافت شده و یک کشتی در حال سوختن است
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18983" target="_blank">📅 04:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18982">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebbc46a29a.mp4?token=Au4IfgB6Qqb6nD8bd94zIcFKY8FwdKqFjei3O6FPtrWNS_np-iv_pcTVTYOd8kAW3q_ptQReh54Qb0jK7oIl8g8iFuwCQSSgbL4lsDcjXR13Hzkeu57Vix7tX5siuQMkUMFiNbXwOpT7OxIUUKNJa5l1_3Hbk1wMUZkNdnd3L4hAYZq20t-3YMSsskB5TvNhStbwlH_OWGRM-codZNb9qSL42L_GCOYNmTbOTAJ-6BODgl4z0RAKMEgjfPyt-_3uFwA3zZhW_aHPScFDJgmj6jWoc_vspPpqhKwI8cuefrb4QrZs-7T07lGch4l-il10uGQkyg5PtZp9JLp-rAQQC0dp5WNtAmf29MRg8ZxeyEnX8g07iNH60U0_7tPMvO0FWyfPjrHOHIdsJVL3Ebgxn6gzuDysAAHlaFcLSwFqouyW2BMzwTzJNOoXcHYxvi-3VeOi1uHEjzmeLUqepB0XN1pEwFqIcFdxoiT3vaM1IbvcuOdQAXIfTOpEwgGooRM7Zbxbb3v3QKND1mE-20BDlYqy98lzhHWdzzwTpJfKaZM8m6As9JGmICMPtBj9t04H4PDrMy4RnMmoKn_liDkhq7OhgW8sSyWA2wFC2ahPF888kwluAljgXYT_dDvRO_SQ1ljrGbzgf0VovBHQJnrKGudGqDQDVG8bpKl2CL4eTQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebbc46a29a.mp4?token=Au4IfgB6Qqb6nD8bd94zIcFKY8FwdKqFjei3O6FPtrWNS_np-iv_pcTVTYOd8kAW3q_ptQReh54Qb0jK7oIl8g8iFuwCQSSgbL4lsDcjXR13Hzkeu57Vix7tX5siuQMkUMFiNbXwOpT7OxIUUKNJa5l1_3Hbk1wMUZkNdnd3L4hAYZq20t-3YMSsskB5TvNhStbwlH_OWGRM-codZNb9qSL42L_GCOYNmTbOTAJ-6BODgl4z0RAKMEgjfPyt-_3uFwA3zZhW_aHPScFDJgmj6jWoc_vspPpqhKwI8cuefrb4QrZs-7T07lGch4l-il10uGQkyg5PtZp9JLp-rAQQC0dp5WNtAmf29MRg8ZxeyEnX8g07iNH60U0_7tPMvO0FWyfPjrHOHIdsJVL3Ebgxn6gzuDysAAHlaFcLSwFqouyW2BMzwTzJNOoXcHYxvi-3VeOi1uHEjzmeLUqepB0XN1pEwFqIcFdxoiT3vaM1IbvcuOdQAXIfTOpEwgGooRM7Zbxbb3v3QKND1mE-20BDlYqy98lzhHWdzzwTpJfKaZM8m6As9JGmICMPtBj9t04H4PDrMy4RnMmoKn_liDkhq7OhgW8sSyWA2wFC2ahPF888kwluAljgXYT_dDvRO_SQ1ljrGbzgf0VovBHQJnrKGudGqDQDVG8bpKl2CL4eTQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امشب ایران رو بازم شدید هدف قرار دادیم!
این حمله در پاسخ به کشته شدن نیروهای آمریکایی بود؛ ۳ نفر از نیروهای ما کشته شد
ایران از نظر نظامی تقریباً همه‌چیزش رو از دست داده؛
فقط تعداد کمی موشک، پهپاد و توان تولید براش مونده، ما تنگه رو کنترل می‌کنیم و ایران هیچ کنترلی روی اوضاع نداره
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18982" target="_blank">📅 04:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18981">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ: امشب حمله بسیار قدرتمندی علیه ایران انجام دادیم
ایران آسیب بسیار شدیدی دیده و نمی‌تواند سلاح هسته‌ای داشته باشد.
ایران ممکن است تعدادی موشک و پهپاد داشته باشد، اما تعدادشان زیاد نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18981" target="_blank">📅 04:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18980">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دو انفجار بندر عباس
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18980" target="_blank">📅 03:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18979">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7kq_YgMtqiUobb8AtnuujkIfuenZjdeGL65VIShUZxdWSonlZNgFJ59bpfY3OjBfaWDOICdO0Pn3lgulHLYUmJq0zLCiuknxja6pAzwviiaDyZvt27C45Wh-SF-C9yopJerh57FGD5POGA4AgmSQk6_L1YQ7ZiFDOx4mFz1ztuVq-XneZAaLUg4NACfMeKRtdLuBf4O1DjtKb2wqEGXBkURwjvxbXYE6uh0SimQF-6kfyodXGF2cbNBLjp62MdARS3Ea4HoyQDSEERBkuPccpbbygNh_NMs22a-N1NOB6FV6ZP0cPn2jJe6ej6Oh0Efv6mRmtalr_jaOnyXps5erA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنارک انفجار سنگین
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18979" target="_blank">📅 03:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18978">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLpEfZ8s_l6-bqL4n9LTGWRpoy0LwCxDum0hQn5yKLuuyc3gE8JQ5BNF8rmId-iBUDnou95ewgajeOw5VO2CK-A_9Fb-lVTnhpnTUa1Cfxk7PZ0crNk7rRgEBPM2Z6BjoNxS91IA-USgmxc1JatW8Zth36Mdoo1RP_vEUbgS9jZ7b_AkYym8fE1YI6_csbBLYM9wNZhjK7zBhKcNbeZZatSdZjJFFRnSA5en0TsHPByZLQV5s6-yZ8Fm-FyS3fHznBZE-PQCbucja6aInqwDD5jDO-T6yhqKdR7SqcVDutacwJe_UOsSZgL8y4BhinpvjcoZMLVq0_IKmoj6dQwhcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیریک اسکله طاهرویی
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18978" target="_blank">📅 03:47 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
