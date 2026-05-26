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
<img src="https://cdn4.telesco.pe/file/IhvyOaqUacOi1_M3f_487NVX9KJCyfcXHPI3fho1Hw93Em7lMDlKgYpBoSxp89C0m9LPi82cTTyaxXey7gY9GrWvahBtJoy8mDUBd2yx8E4_1ZtqQ3fW8rh64eC4SOcjFgPkU1eVPZnm_EGoXMkwMgokZRTEzjxWYhIclf5QLAkuSOC00Ob5t0b73fS5lKcNYrqJBwDI8jWhR63hd0ovL2yryW8CObHqhuIS4W3M9Z_TbLzgTQr-DStuA9QXQNkGxVWhMQAKw3Rmv7Hq4kff1jm3KtelyHkGyew2pMJHeqI_yB2FXh3lC5uJqZVmKE6G2TlAuttLJKAF6cqABbrN9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 935K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 17:41:59</div>
<hr>

<div class="tg-post" id="msg-122831">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
تماس تلفنی رؤسای جمهور مصر و ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/122831" target="_blank">📅 17:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122830">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
بررسی‌ها نشان می‌دهد از میان وب‌سایت‌های مهم، موارد زیر در دسترس قرار گرفته‌اند:
🔴
ویکی‌پدیا
🔴
اپ‌استور
🔴
پینترست (Pinterest)
🔴
کنوا (Canva)
🔴
نوشن (Notion)
🔴
تردز (Threads)
🔴
کال آو دیوتی (CallofDuty)
🔴
پابجی (Pubg)
🔴
یاهو
🔴
دراپ باکس
🔴
پلی استیشن
🔴
ایکس‌باکس
🔴
بازگشایی اینترنت به تدریج در حال انجام است. به همین علت ممکن است برخی از سرویس‌های بالا هنوز در دسترس گروهی از کاربران قرار نگرفته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/alonews/122830" target="_blank">📅 17:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122829">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxfnBpxm_PySPASjdkf8D5bPNMzsyF-7EfmToW4B3OMCEDT9NW6HwpsLqaVg4_H5Tc5MGsbF2ZuE4CJ2vsao4BHleqCQoQroKLvBEWK97cWr8OND9ogjIHPhOc2jlevkZ8vo98YwgoF_njYkUHGZ1wNJUA3V3-LQ9_Ei4CLTaV25s_DMp_Q1jy1HUXPCHQAOK4IBmeHo-V1lpSqr9gqIiBoOGGnfYpaQShNRkQIUzSiQj6ldxbYqiO626wYkZ5duejDZwYOvTs-0Ujaf2PvoawA7kxNwc6RpGehmthtGTlcjHIcrzbBaAOUB7ck6kXXiUzlhsNVBmnUCqAWM8UGOQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار در نزدیکی کشتی در سواحل عمان گزارش شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/alonews/122829" target="_blank">📅 17:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122828">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
رسایی: آقا بازش نکنید
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/alonews/122828" target="_blank">📅 17:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122827">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuyAhuudeKooChh7fDwLD3mrHhYytu9GMAFa9_cPV9hi98-H6gVO5tekN9xkbNc8OfYkJTaG2f0aPbsVEFGl8aVa2xWPttv0M7cU6A91XlE3b7HOCRpmmsAMsVCYifyyEJ5ppChe2cwpPj1PHqxXfnS4_dN9mPcW4lPu-RwJ6uFBkWn4z0K0MfZEpVIsPdDEx7zLrk-krbmQBy83hZVBy3g9yXW1BbHNOjNjS6frBgDwCUgLK6RmZ0ZiIbkyKE5AKhotTfZUlxszcyS96brY0tJgluAzELjm4EW5TOgzu3FRWca_LDdLIyAMWt3x-S3oCNIivpwyJGbFxwyyC-_L5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) در لبنان فراتر از خط زرد (خط توافق شده در قرارداد صلح سازمان ملل) عملیات زمینی را آغاز کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/alonews/122827" target="_blank">📅 17:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122826">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
روزنامه هاآرتص به نقل از یک منبع آگاه نوشت: ارتش اسرائیل عملیات زمینی خود را در جنوب لبنان گسترش می‌دهد تا کسانی را که حملات پهپادی (FPV) انجام می‌دهند، عقب براند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/alonews/122826" target="_blank">📅 17:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122825">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نیرو زمینی اسرائیل دستور تخلیه اجباری برای شهرهای مشغره و سحمر در دره بقاع شرقی لبنان صادر کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/alonews/122825" target="_blank">📅 17:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122824">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
طبق گزارش ها ایران ارتباطات رادیویی را در مناطق خاصی در داخل روسیه  و گرجستان  قطع کرد — و برخی از ارتباطات در ایران به دلایل نامعلومی قطع شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/alonews/122824" target="_blank">📅 17:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122821">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZbzHnh2PvACpaybWii7IsKeW4Kytwb4P88WcF4QtaghZNqwlsNUkv2aLFnomcCEM7Qn4mCBrz8kiLeVmrsKYbuyW15fu8X_U6-npLAYIxGcOCJGgdYCB1FculQhuusVS-jAt3MOOEZ_1EYlsZNJcZEqB-bmym95PnqHm43WbyOYCoG4ztjFMUN7BDi0LhseDyzQX5ek4b98zdMyNfquBrxVEw_ZpbMR5yp4pDi5S9utguoMLsMJjVyeLGeaogKNiJPZHyVowCF6UCX-aq2W2uNPzYWJkF2HtWX7KmvpPsA0S7Ci3y_zNdxt_1fcCrq1qepTisfharzyTmHXwPVv6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9CYuNtUSxpJeY_V-lbmMPgYlqM1KTMoYtjPVqAu0Wn9_NQZPk7pBF5pweab84018qtFtQXIzEoBsAIBzU-5_tnI3m1QH_HynDo0vcRIVZ8kHTBpuyZjP3uPtK4jMjMdpZBBrMyPF5ecW0QAUkbC9xRlUP7xHxos6IbiAeW-IqOhhd5GtQJ5XI-tJI_VbVsz9QX0cqG_lczDphIq6-04n4RAL8TNqdCLVD-FcAQTzMRVklLQjoLocnAPbVg-kN7705AknvqJ9EsNvZVueli_BE5Bsa70BOZxfllo1kVWbhHdWwDkgiMwtLNtO2zWEquxca18yyDPzNkNmODXk6WP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tevxC8VM1DgNcnZEBLQ7sUNGEFcS6qqkXLjTma5rKRXPKSJgQHmQy9IWxXNouVqQj-25KmUgrzTapFrNmwDOMLvEdyBYWB5P6PGNuS7yMPQRvf-iGLIz-7nHI2k_ptxBzfQu7quWEGWFfFKl7T9llsOl72y24YeCeBxkLwlUsbotEpOgbHU0qVskMxea0wp3SxIVK_MK4ax5BwvmNbxPwzGwa1j4FvgZTOYwyTFWXtlqUtlaI3NMKMJtkPwPlGspR_Y3ZROZydv2fvWVG7ZKQjDzGB7jBDqZlZ-Wb0i_Iuz1RFWzzqT6c0m731kZG-oZJdbvSEJFv41KI4mldufdjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی به کفرتبنت، خربت سلم و زوطر الغربیة در جنوب لبنان انجام دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/122821" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122820">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
تسنیم : ترامپ به بیمارستان اعزام شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/122820" target="_blank">📅 17:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122819">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tre4t3CT3faIpr5gvAA0QbUzUOtzWpOiKdS82GQSV9vTyCeXxCPbeY3liYhM3hcsVz2U1jFnGNP5meBMeVgHzryS3BRpxupT8HHrKDntSgsAfNVSgwoW-10rpbL1ioZ-b3zpYEoC7nzPYt5TAGYTi3KZ37mApwdNF_9vGAwTZ4oPxigmovv4Zdbsr9QTuzgigu22QXygFnewcM4tPNGr8So5sy4t7WYp-xvb8CHz3DrBbRes7E9GT7Ir7iqMAqSpm9-6Ew6hZxUp0X0ezul_uzdIuP7Y2s8qKOGF-YZjrAU05qd-ULvKzkHLwDnQY9ElnIRu8nP3Fh7SGAIvaq5smg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عارف: گام نخست دسترسی آزاد و ضابطه‌مند به فضای مجازی برداشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/122819" target="_blank">📅 17:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122818">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkrlKLNJtMFP633NTumKVREVQ1MJpweXDNtmDK0VhtS77a7bQEAIVsZukzcpIBQ6iY89dcB7uN4l0p3mrvlu7rF53F5yKMeMcOqkM24BeogIWoKsJ7oOyR6iseIyO78vji6hVjmml9o2fFMVskjTK2FC2NXMEuklavF3bNPVybHPHRbepuNKqKKhL27Pv7pOxQAHfxmDWLVetfD9Tz1VPU9OHDVkr7qu359gAPjUjhRNQaZdMa4gOCURhIAoCXM81_gHiryH3tq7RXQhI7TxxfPl6sgY-ofugPXLg_t7TOUoIfg2hT_5ZP-C_bVhorWCFOlVWFAzDDmM03nXOyPYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صحنه‌هایی از معرکه، جنوب لبنان، پس از حمله اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/122818" target="_blank">📅 16:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122817">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
تسنیم : ترامپ به بیمارستان اعزام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/122817" target="_blank">📅 16:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122816">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری / گزارش ها از زلزله در مشهد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122816" target="_blank">📅 16:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122814">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KORMaq-gPVQ_5BRQiC-0hoKJwWlv-DjkoQ4_3H_9wKH00s4AvUIxO0-ZITWrMuy96Qcf3Fp7_bp8yV0vQxTwEVM4ApLaULVwzp6ZoH7LhNQIMVdT1VthqFiNeaoVjOWO6v72qWyzkpqmqKwIPEwrbE8RE9n34VBoe4CF40nxvd_zXf4CbjxARMJyAdeHP3OHl4CJHOq0c3phFKa2wTBbQjvmuU_M5KwocRXq6g_GFguyWksKU3AGq7w3Yxpsk-JTSW9Zc27YXG1bmdoYZAtm4XJ78iyMJNJyJsly7mh4dUgVyxElPAdRSRilCOoT_r6YOO7ZmXQgFA0HQeBKtQQ7UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R92ae5kgg9LvzN3n6AlrWRiDKJgJamAOsV6W0md_La_e5DD5DlhxqDRZ_rCJbdzeigqAod1Qj_2VNIT4X6-PtwOrcp3k31SsWFYBxwQDyXRoP3GnZX-ICKwlN3Si4oYscHybF1vLcZdhRKocK2RXP-ebVlUx7bUn9NUDqC3ttClxO79N-mOY3mawC6_NUBUYSdfwWGuzvvO9SLfX2CD-sebRgCUixjQyezEO7h2Of3aTUKB0lFQXKe-pb752zLJt-IBPu4aK6WKKE5aIlfCf02p1BmUeV--52kMuEnvjMNQ0bDtUd3JFdYE-RiAwZ08jLdtnpXAAV2_4ITUfJgCmtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پست های جدید ترامپ در تروث سوشال
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122814" target="_blank">📅 16:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122813">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
فعلا پروکسیا و یک سری VPN ها روی مخابرات،شاتل و بقیه مودم ها وصل شدند،نت موبایل هنوز باز نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/122813" target="_blank">📅 16:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122812">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcnxqjrjAVjutfzSzVvMITWypNAzbiDmDV_nKSeJhlmTatdY-81AlqrKeRF16KVDXMVMU-euwIM1CtCoa0L0eL25-rPiQZ3iRSsTHLYlzsgvoBg9wQtCQH4A3hw7SiOwZA23Y3WWVQEKgssJhe02bV0tPcOs1W3wzC-Cgg0FK-QRZWPf2NpIt8w-JCmWGK27vvYrNELrV-f0GCDpPxCTKDolLOacC-TBR0w0_d3k73X-tszSyXG9Rtp12jQ2dYIvrPTxw3eNV9tCNvwZKY7HQBTorYgYDeEXz3MIEvTlaZfs0hBZwH0zpcqhLlQ_3yXurxvOdAkAd2Ta-bfigyu4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت کسب و کارهای اینترنتی بعد وصل شدن اینترنت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/122812" target="_blank">📅 16:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122811">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
تکلیف اونایی که پرو خریدن چی میشه؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/122811" target="_blank">📅 16:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122810">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lygyh9BsazoL1WT1RfHNqLoYLEkR7um9mAG8Bf0lWZh9dfmlVQBRj2k007QIB6OPDztlSmMzFeUPYrZCPOgmKKQZnEPCtMlj8WCm1smmEAdBEj_-Ft2cFEAV_HjEMTDtkpHgH2nzJtn1FWu7S1ex90tXUAOIwySoYcIETQ_KiObLSZ2HsWr91yT7Hop2Q1lm7XfjbaRdVkSjnqHsX1_iMqOIfRMdwFcaugLuDqkZ9uDy028gjRsHBTi5PJukzLSff2FTkQKaZmDfBH9Dl-j6GthfiGPuzyRXjE5PBHEClbv3drdmD7r_AHTo-oIcADdDeJudz_fxGM6vL_ltlEzNHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعد از ۸۸ روز و حدود ۲۰۹۳ ساعت قطعی و انزوای شدید از اینترنت جهانی، اتصال اینترنت تو ایران تا حدی برگشته
- ولی هنوز معلوم نیست این وضعیت پایدار بمونه یا نه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/122810" target="_blank">📅 16:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122809">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ادعای وزیر دارایی اسرائیل: ما در حال تغییر خاورمیانه هستیم
🔴
ایران امروز بسیار ضعیف‌تر است، حتی اگر هنوز فرو نپاشیده باشد
🔴
این هم هدفی است که با کمک خدا به آن خواهیم رسید.
🔴
نگاهی به وضعیت غزه بیندازید. نگاهی به وضعیت لبنان بیندازید.
🔴
ما کاملاً معادلات را تغییر می‌دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/122809" target="_blank">📅 16:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122808">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8z2_gqtp_qSbzrnufmU009Q-KXfFA43CPPWI52V35LTVcxY2YhtOHaYGAveCJcDxD7tDZszcB0LZ2aRC_6t1LMqVgIvUwIG2txhDTyMObeWnGBjtOyN46q5sogoluH0Sd_rm0luoMvt9uIHIfSiHrst2PBHlHleE2W97NBoPZwF_BihrpGmT8NxbACh7ef5FZ-ivDczan-SzTbAjJ1-xHhR_UwX6dEYVH59KBfGUl0AUJtR0wW73x4C3n4A4oPxxSN1CRvAXL4zQON5IOKG_AjaPNWZpjADAf49LYCW1BL89nP9c3aAJXXQWBMkukUfnY13Db2KRRxlCgR7N_ZWDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال:
قالیباف برای گفتگو درباره پایان جنگ برای دومین روز متوالی در قطر مانده
🔴
وال استریت ژورنال مدعی شد مقامات ایرانی و میانجی‌گران عرب گفتند: «محمدباقر قالیباف» برای دومین روز متوالی در قطر مانده است تا درباره توافق پایان جنگ گفتگو کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/122808" target="_blank">📅 16:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122807">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری / گزارش ها از زلزله در مشهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/122807" target="_blank">📅 16:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122805">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ادعای وال استریت ژورنال:
بر اساس گفته افراد مطلع از موضوع،
اسرائیل از آمریکا می‌خواهد که آزادی عمل این [رژیم] در لبنان را به عنوان بخشی از توافق صلح پیشنهادی با ایران بگنجاند.
🔴
این تلاش، می‌تواند به یک نقطه اختلاف دیگر در مذاکراتی تبدیل شود که ایران اصرار دارد هر آتش‌بسی باید شامل پایان جنگ در لبنان نیز باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/122805" target="_blank">📅 16:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122804">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سناتور تام کاتن: رژیم ایران تا ۹۰درصد تغییر پیدا کرده و این یک موفقیت است
🔴
پ.ن:حتی رژیم غذایی پزشکیانم عوض نشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/122804" target="_blank">📅 16:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122803">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اینترنت هم برمیگرده اما اون داغ تا ابد میمونه</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122803" target="_blank">📅 16:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122802">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKZyuBA64_1iR1mmgbHFZ6YL4A3sQIHHw6u6p0gh2WqJapYjG5C5zKmiHf1BGQ_I1TxCYyeQrFyBOCV1YgJvd9oc5XQkAobJKnVY2QADHPAaR_1pmLCBxn8qiYG8XCVlXulnchTzt7yvC03X7YSC-YEPVyT4fpTyG3gZyTsRQbNFsFIOCR59lwAsAfm0gzWyZ0eLo8Qo8OP6wQRY0GNNv8V5XxrTWWPdgP3yRwPS8Zg1O3qN1vDtf42_fFLqwgENitqCj_-ZouenSYvRuDIuJRtIHoe2C059PY6S1OWDOnfR5g5cYe34g-DuRcVX9YOWasisrPpOK62XUnkkS8a0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینترنت دیتاسنترها نیز در حال بازگشایی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122802" target="_blank">📅 16:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122801">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ccc8c541c.mp4?token=dj3bN0_SDbWS3rcRTP5mAEjtXmZ_jKFUbCW-a1SM4zlXOcaY_tyPnX6YzbCdoYR8WbPy8B5gyvnYUS_i4JkMPJ__QNHun5KM26eXiow-t7nBaTdNQME8J2ODcxiM-KJ7nDA1W1dK5r6qHpN1Bikg-co0kjZnNGjFS_eMZPcfc5uFTwk4u-uHH_B23tBoGwX8o1MVVllz9KIWdZY4js4ekWI5Uy5MoKKoMZ-IleVt86MplR-wO3peMO65rs3RMZaQn7TYZYi6jH4bCeq8KgUaa1exzdXcuYJFY-nQEoUxVg9PooYiqnI3191bLHlhN83l7wqUum0MgN0PtPY8Ry8OPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ccc8c541c.mp4?token=dj3bN0_SDbWS3rcRTP5mAEjtXmZ_jKFUbCW-a1SM4zlXOcaY_tyPnX6YzbCdoYR8WbPy8B5gyvnYUS_i4JkMPJ__QNHun5KM26eXiow-t7nBaTdNQME8J2ODcxiM-KJ7nDA1W1dK5r6qHpN1Bikg-co0kjZnNGjFS_eMZPcfc5uFTwk4u-uHH_B23tBoGwX8o1MVVllz9KIWdZY4js4ekWI5Uy5MoKKoMZ-IleVt86MplR-wO3peMO65rs3RMZaQn7TYZYi6jH4bCeq8KgUaa1exzdXcuYJFY-nQEoUxVg9PooYiqnI3191bLHlhN83l7wqUum0MgN0PtPY8Ry8OPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو ساعتی پیش تو مقر کریا با وزیر جنگ اسرائیل و رئیس ستاد ارتش جلسه امنیتی برگزار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122801" target="_blank">📅 16:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122800">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNJ23u0kfv9oS4mFKb-WFzxjb-AMgb8DWRKMXq956Ts2luaUp8xko8WPPlDd0m2M_1_gpKH17Zk2fZQTXC2s6_-E84DC7wwTzZHdYhjU9YWrNDGG6hmPS2jDdNW-l63X7XsqpJB4l0cfJXcfciwYQgLAPna_JIZru-BmADlnajXhoF2b6NduMIinrocj-AmIAT4ZnGMkFQvlXy1um_lVRDqltSK0NpvwCv8bQaOCueB7GV22eXF84Q3dY2bCy2heYbffU0Ft3oXvGVrr2rRtQ-Pjm_KuUcN6me5P8QSbKAdnlxdSTe4wieIT5icYJ-M1Sr0P4P5lz8jn0ILa0c6iLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/122800" target="_blank">📅 16:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122799">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-oR4ar5G3MzYoClXAxUJNgtH9JEm0EfAyE5bSSkyFlnKibTxB-0tkicB30Ntn-K2kTBwXrv81umDWfO8cUK4IYAoYNAT7O_U0ZzuOYm9Lzw8ZMBOocsuMJ4gFJT3bgJTIPvEM1_jj7-OqGTwd65Y95NQXgX3oiKvHBVvQy1_K7rPJAPbVd-od2BGQito4JsuZdxIKAQdaGYMAzu7aA5VVMtUgCCpag8cAYJzBhzoMgLwMSnJAMNTt7PNWySnnxOCa0ToAP9lLorTIFxGghtkRvWdJlkON65oCcUM3-kSBtyQPSIoqyycljueNhv83I6q6lJZOarUwCo9KfCnnfXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی
: آقا بازش نکنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122799" target="_blank">📅 15:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122797">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWEtI2xp_MrRtJjhxXW6_j1w3o4IkMXru0vw8P6nEtOSEJNxjBLHKEOEpq-Fy4EspMQiwWycRObqFD-UKDtVLZ4021Nf9CjpC5dC22Gm2NkEwzN_TXKfjwyzGI5x9hhVzWjVWjqTZH-VT52xKf0tDrBE_y5v8S0PHRHXyUd8dWKVFsDALhI8ljdxmdBv9dTgyMKJ3Eb0n3yZVU4a9XCpCPsbB072CKbV4YXwYNHoX1lA0LpNh77GrLIa2iY4qX4rWj5QR4OjUCZbE0zXdzWjnWgirf6yGkcOm7kwNRyo2a-cGyuOZqa1VgWSFAl9MiCs2Zgbgx1lqeLwon-33F_XKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستار هاشمی، وزیر قطع ارتباطات :
با دستور مسعود پزشکیان، فرایند برگشتِ اینترنت کشور به وضعیت قبل از دی‌ماه 1404 رسما شروع شده؛ اتصال جهانی ایران هم از همین حالا شروع میشه و تا 24 ساعت دیگه دسترسی کامل مردم به اینترنت ممکن میشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122797" target="_blank">📅 15:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122796">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
الحدث: گزارشی از یک حادثه در فاصله ۶۰ مایل دریایی از مسقط در سلطنت عمان.
🔴
یک نفتکش از انفجار در اطراف خود در نزدیکی مسقط خبر می‌دهد.
🔴
خدمه و نفتکش‌ای که در نزدیکی مسقط دچار حادثه شده، با وجود نشت مقداری سوخت، در سلامت هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122796" target="_blank">📅 15:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122795">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KHWC0mdD0TCRaC4kEtV5zyJoPEZmZcHC7UrUDgUodVY3ll5lGPckKZdFdhNKS-RiVytQo_6jxBAGrUUcO1IWxo_0OU56WaNHqPmaDW3SXOJa96isD8gCot28qsMJFoW070qzwjoU4coqtWExvz3Vp7pmASNfm9SNWhWfgABToIQkB-Ud-kQweHghEoKdECJcOCQXKCPPrsEo8QEDXD16xeeymN8MkAFUYo0XLlgeluSJXFFXnrCuOuTfNCVz1loVcclmGo9w3h0C8Uxwgwnl29WumzIEdIoOB4xYRkG495gKoQWW5gxsOWTeji_SBX5Sha8oyJnb8hnPyf4pFw6y_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه بیانیه‌ای در محکومیت حمله آمریکا در شب گذشته منتشر کرده و می‌گوید: «ایران هیچ شرارتی را بی‌پاسخ نخواهد گذاشت و در دفاع از ملت ایران تردید نخواهد کرد»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122795" target="_blank">📅 15:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122794">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه، وارد ارمنستان شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/122794" target="_blank">📅 15:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122793">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
تسنیم : طبق اعلام دیوان، تا وقتی پرونده‌ها و شکایت‌ها کامل بررسی نشن، هیچ‌کدوم از تصمیم‌ها و مصوبه‌های ستاد فضای مجازی اعتبار اجرایی ندارن و قابل اجرا نیستن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122793" target="_blank">📅 15:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122792">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
یک سری دسترسی ها به اینترنت وصل شده بود که دوباره قطع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122792" target="_blank">📅 15:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122791">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
فارس به نقل از یک منبع آگاه:
گفته شده آخرین اختلاف جدی میان ایران و آمریکا بر سر آغاز مذاکرات که مربوط به نحوهٔ دسترسی به منابع مسدودشدهٔ ایران بود، با میانجی‌گری و ابتکار قطر درحال برطرف‌شدن است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122791" target="_blank">📅 15:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122790">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2UOSE6kQpmRCfS4HjWMVzf5eHA_qN0Mv-GSzaFbBL0nO6gS59q03mco-aOOBVSSEks94a8PYk1NU3OiYBp1tGzUjfsfVxLdKLucJzDfNqZUSQ2P7qFWsCaBtc-VwxHRzsDEioMfRWYJZ5hGlHGAoo5MsRfFp0FRbQvhPqARZBMQsWbZmrAx8iZvvceBL3g0DBhZa1A1FrvSw3PfbgUto37onxmUQHXjdaZbGUUC6N3Tcctc30_Mr2HaqOy6kUghV1RXxHCsRbvt8KLJWpvlYCusmGXC1caMl64Uc94U_4mo_hlRu5F8PaRjNDWB7oC3pDcWtxxsRrP0itCbPPS7DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
از صدا کردن اسم جاویدنام غلامرضا خانی شکرآب تا اعدام شدنش به ۲۴ ساعت هم نکشید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122790" target="_blank">📅 15:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122789">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F23qZsNLDBX9G4Oci7sqlbR2y_mYPnSmRsMDo8NT9cxaG465uw6kYQulP3TH-Ue0AYTlRWchRmpZ0gI4pmyRxEahZ6w-Oj6_NBzquRxFq82ztE6loN_lQR1IvP7wwf415LdXkLfGXQX008K8NzFX-x0FDbGLKP4y8v2uZa_h0b5Nevd1Wf8utrKp6TK7by2WsWo3VcWT_CN5FJebbE_u2SMfKXe2Fcqz6HzjnK-ogJ24f3-uYtrorfKhah86AqblH5Xko_YFb8-S8XGwzZ7xhLPc4Db6q8QFCXWoXz8tQLVOBfC-aVBOaogfvSEmF_UDDI5u1JMqXsBZa6jEB8vSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل سد بقاع تو لبنان رو هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/122789" target="_blank">📅 15:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122788">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTFN7XoV7RzC2vbOMTwAIUv859npIt02Yhc9pviFWhLot_jjC-aRiBKBBxBFXmtbDGCjG-4E55yX4cqgQiM8MglZgvc5dv6XLxbVmYFX7h8lL1VXTfGtFPRI_NbHQcpeteOYF9UCL9T1WA9Ke7GNQmEKDFAaPhRRwG07U4oBhhk-ThmJIccMAskQUBa1rejz4e1PSsMSHtUVGJSjr-f-TSDKdU_f2wLBTYRjJbzrkNydfIoig_fe_dkrDomckp03mh4D5MN2r1nC7NKciAnEdBECzYhAR09q9zvfJF7xy2aev2U2raRX_LOQiVKAfRLUww2u-oGBDPLGNn0joMUduQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: بازی تمومه، دولت عمیق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/122788" target="_blank">📅 15:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122787">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngsSRujRCVZ9-wJp1CYsq6UlH8SQMa8H0WAkD8QsA_18vdQIxXKjTXUdx8tQKQLHZ-_YGkcxyi3nuqoThtGMiM5PywzbDmk5PJC1qr1TFD7DoPF6m5A_5fLxAQsMCaA2nxX-vFF19NjCeycSy-5QF4QKVi6lBw2ok34smaptyc-UqsqOnd7bz23AUqXKLGgMEo0Rd7eaVNTCQuCeVRAJ3JDJ4eQxuxhVyqQKq70cXETMb01V42gq9zDq8Gxn9ju_wsWcBoNeYLG2QtUXWVtaLd318yLwT0frsXJxRWGTa0DVSoDLTd4xakdmuVngrzV3dvJFrsVVld17oONS9kkj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجتبی خامنه‌ای : اسرائیل 15 سال آینده رو نخواهد دید!
🔴
غدّه‌ی سرطانی اسرائیل به مراحل پایانی عمرش نزدیک شده و به فضل الهی و طبق آینده‌نگری 10 سال قبل پدرم، 25 سال بعد از اون تاریخ رو نخواهد دید، ان‌شاءالله.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/122787" target="_blank">📅 15:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122786">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزیر کار: تا کنون 260 هزار نفر برای دریافت بیمه بیکاری ثبت‌نام کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/122786" target="_blank">📅 15:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122785">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfslAFL1-6zPccejsthgyA3McpDu5Z58VXYd79a8rBxP4u7VvqDIniNmqMTQ1qdRMrj8kw4eYfu-ZjFZexIKvsUvuuEm2NGX1Cfhd3HcYAXKPUU_XpBSmZNymZAgqYhDfxd_vQSlaXssfnXviFAfQBrNyyw5tgJbQPNnw1UR1Tx_n0Aby_BXHG0-oiAoZRkO2KfStRkqSvdNAx237I-svjwdewaSRd4nFhGF4x90bjBUxdmn2OhsSjC-vf88YqObds9oPhgFFnN9PnprVjaGJjo6LlddLcYKZf-HS40eQl6klkt_DXHqW6IiVOw7P_k2EsQ-2YWUk9U5StQ3jHSagA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی دولت:
گرونی تو همه دنیا هست و فقط ایران نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/122785" target="_blank">📅 14:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122784">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⭕️
⭕️
اپلیکیشن‌ها را فقط از Google Play یا App Store نصب کنید.
🔴
فایل‌هایی که در تلگرام، کانال‌ها، گروه‌ها یا از طریق لینک مستقیم دانلود منتشر می‌شوند، اگر از منبع معتبر نباشند می‌توانند خطرناک باشند.
🔴
نصب این فایل‌ها ممکن است باعث شود اطلاعات شخصی شما، رمزها، حساب‌ها یا حتی دارایی‌های کریپتویی‌تان در خطر قرار بگیرد.
🔴
قبل از نصب هر برنامه یا باز کردن هر فایل، حتماً مطمئن شوید که منبع آن قابل اعتماد است.
🔴
امنیت را ساده نگیرید؛ یک کلیک اشتباه می‌تواند خسارت زیادی ایجاد کند.
⭕️
تحریم ها ارتباطی به موجودی کریپتو شما در تراست والت یا سایر کیف پول ها ندارند.
🔴
درصورتی که کلید والت خودتان را در برنامه غیر مطمئن وارد کرده اید حتما نسبت به تغییر کلید و انتقال موجودی به والت امن اقدام کنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/122784" target="_blank">📅 14:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122783">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
از عجایب مملکت:
🔴
فارس: اینترنت وصل نمیشه
🔴
ایسنا: اینترنت وصل میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/122783" target="_blank">📅 14:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122782">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
فارس:
ساعت ۹شب بیایید پشت بوم و بگید الله اکبر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/122782" target="_blank">📅 14:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122778">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qHRHvBXKlIQMh81XQxx6dPRuUgfrbQjm48zbuMN3JpiuvzguHLVEGjr7N1hCBUhnuWmBgDbRMqQ76DShsM9u0-A3RVb9OujMUiId-NWsn6rWmepzBDOe3UI3g9nn7pdRO1WuHgmA1dX5lwz4i8D25eeFtS8Wu_uipEBNnke0PCYjsuxMYgHN0-f-sQ1GmiS-j0UfZBH7iTqc6R4OrjOzkiAu4_29GSlCaib-Ew-N63KiDVUvhC9PjY3uqczpFv9Gucg48CxrN_Ct3Xrjf5lxS8m-TrtK-rMcUMJry1blpWCyupRReA4wIjd9dvuFsCj7KvQEs6sKRZkAaHxo1rYCAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jsdkxmdCZTEgCMBH2K4hUfJ9Je6RPKGZiegKEQ-xIeZLb30uJ-ktHqW31V9FLQIx_wCI8lGoFm9sOh4Uu-7p3-xOf65cfMqQXskuICjHAy_9vbr3EeU7DKOjJ1nVzCbOBJOTdv90NqeUjvOiTwtsZ_xo5fIorcCW70hiVofutnLSkc7Ico9C998yzN5njwEsvB8zs0eSVZ32j9kn0vmv31A83aMv2-ty-WIzOueRb8269AZGyn4D2CBcW5FHbtUZ5athIvAIHHsdxAVgzg7y8Q2ev9Fz4ZizBELRsov5NI5G7D8UjQpxKqx8TH-IkCFkPKYyvEkoTF8orloqF_xXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxTb2NZRR8JXLE3aKwHMVsFhiV0jVqeB1kLDtq7e_I70Ra5_qm9IIJhJPmc08dHt0U2hXw5rdGMHHTiJyCawDNenr8071QqDqqiKmMfupb7u_U9PduREOtTMMQnHBOpfmE-DRwAI6J4nowysY63e2N-6U3Qak-ujykgnQDr71kTcNfGzKkjCvMXWYzHRa8C6VYABulroYVpYauPLSfRoHkd3M8XJVV1_TuiebYRkuYQbPpz0ju5QtgoUyxAiU1QzlRDTrMAnIs4Xu5fjwvp9NVIaiOq-oJ30o-1QM1teRlZhiaQsv1mdcVJMmNCoH63DIBt_ruzeyF6eaJjJDb63lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhNoYbcxcgIJI4GQK5p6nSBRuJRx2xC14xWChmuGlXWwOqDkpQOQAs0DG5m-1_mFCuoDO4wHv2vrjc02Mt8jXteeGkOLgkrY07oH0JQg_NKII2yAfSDKi5ZQWsSQFZbXChYmHRpF4Lt3RXThBQpCtdTrQkiIZ_mqbm4OQ4eUGeODaybSSZJlY1rC9kX82pyHjd4dgSzv1p_ityzFqTJ_-URTnGFOFS1brkyuhmbBE-nClTSgRxBWOYkeEeqNEmK5oKlR7rPZuFlfvQMO-sMsSqIInX3EDt29PJ87C1TNAZm4FYVgWqTExN3nz9oFFuTlcBnQ2gzJ4If6AJL8j5rmMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مرکز رسانه قوه قضاییه:  با دستور موقت دیوان عدالت اداری به دلیل بررسی غیرقانونی بودن ساختار ستاد ویژه ساماندهی و راهبری فضای مجازی کشور دستورات و مصوبات آن تا زمان رسیدگی قانونی قابل اجرا نیست.
🔴
دیوان عدالت اداری ورودی به موضوع قطع یا وصل‌بودن اینترنت بین‌الملل…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/alonews/122778" target="_blank">📅 14:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122777">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
رسمی/با اعلام قوه قضاییه اینترنت فعلا متصل نمیشه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122777" target="_blank">📅 14:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122776">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
رسمی/با اعلام قوه قضاییه اینترنت فعلا متصل نمیشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/122776" target="_blank">📅 14:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122775">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ستاد مشترک ارتش کره جنوبی اعلام کرده که کره شمالی دقایقی پیش یک «پرتابه ناشناس» را به سمت دریای زرد شلیک کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/122775" target="_blank">📅 14:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122774">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
فارس به نقل از منبع آگاه: هیچ مذاکره ای بدون دریافت پول‌های ایران امکان پذیر نیست
🔴
یک منبع نزدیک به تیم مذاکره‌کننده گفت: هیچ مذاکره‌ای بدون واریز پول‌های مسدودشدهٔ ایران امکان‌پذیر نیست.
🔴
گفته شده آخرین اختلاف جدی میان ایران و آمریکا بر سر آغاز مذاکرات که مربوط به نحوهٔ دسترسی به منابع مسدودشدهٔ ایران بود، با میانجی‌گری و ابتکار قطر در حال برطرف‌شدن است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/122774" target="_blank">📅 14:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122773">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
مرکز رسانه قوه قضاییه:  با دستور موقت دیوان عدالت اداری به دلیل بررسی غیرقانونی بودن ساختار ستاد ویژه ساماندهی و راهبری فضای مجازی کشور دستورات و مصوبات آن تا زمان رسیدگی قانونی قابل اجرا نیست.
🔴
دیوان عدالت اداری ورودی به موضوع قطع یا وصل‌بودن اینترنت بین‌الملل نداشته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/122773" target="_blank">📅 14:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122772">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزارت امور خارجه چین : از روسیه می‌خوایم که به کی‌یف، "اوکراین" حمله نکنه و از حمله گسترده خودداری کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/122772" target="_blank">📅 14:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122771">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
روسیه: به تعهدات خود در خصوص نیروگاه بوشهر به طور کامل عمل خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/122771" target="_blank">📅 13:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122770">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی تدریجی اینترنت تا دقایقی دیگر خبر داد و گفت: دسترسی کامل مردم به اینترنت تا ۲۴ ساعت آینده میسر می شود.
🔴
بر اساس اعلام یک منبع مطلع، برخی سرویس‌ها…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/alonews/122770" target="_blank">📅 13:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122769">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXodhQnvtsvb84rAcI8NxSUFHT2v1gGHYd9E0k0ybG-Z2k4h62epjjNkookU-8G8kLAg8Xn0bBOslvZ1TvOg85YF_H4WWdjuUaelwpLVRw11AF9Cv2nExGie9molcKnRKOMLhAXZ8hDgncyOeTYs-8GLoAGA1oYcHSoYY1hXRmJ-l38m14uKIB4GgmdPYEpRp8R-SNIE361QVZwT7Zw5VnzCdEefbcjxgtdPYkxcTNYZARzNCYFAvQkOilmhzoeY0TAbptsmEZC4n_AajhoJyosmFWQ7hHgw0dPq979L-JyJcVyN3tu4tXY2rfZFKjEe9PdFb8rPJ3fnPaRgu7Tp3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ راجب ایران در تروث سوشال
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/122769" target="_blank">📅 13:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122768">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
در قرنی زندگی می کنیم که مردگان ۱۴۰۰سال پیش برما حکومت می کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/122768" target="_blank">📅 13:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122767">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سیتنا: دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا 24 ساعت آینده
🔴
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی تدریجی اینترنت…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/122767" target="_blank">📅 13:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122766">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزارت خارجه چین: ما همواره از دستیابی به راه‌حلی صلح‌آمیز برای پرونده هسته‌ای ایران از طریق گفت‌وگو و مذاکره حمایت کرده‌ایم.
🔴
امیدواریم که طرف‌های مرتبط در مذاکرات ایران به راه‌حلی دست یابند که نگرانی‌های مشروع همه را مد نظر قرار دهد.
🔴
ما آماده‌ایم تا در حل سیاسی و دیپلماتیک پرونده هسته‌ای ایران به نقش سازنده خود ادامه دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/122766" target="_blank">📅 13:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122765">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سیتنا: دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا 24 ساعت آینده
🔴
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی تدریجی اینترنت تا دقایقی دیگر خبر داد و گفت: دسترسی کامل مردم به اینترنت تا 24 ساعت آینده میسر می شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/122765" target="_blank">📅 13:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122764">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
گفت‌وگوی پزشکیان با رئیس جمهور عراق درباره تنش‌ها در منطقه
🔴
دو طرف بر اهمیت توقف جنگ و پایان دادن به تنش‌ها در منطقه از طریق گفت‌وگو و دیپلماسی تأکید کردند.
🔴
پزشکیان و آمیدی همچنین بر ضرورت ترجیح زبان تفاهم به‌منظور تقویت امنیت و ثبات در منطقه توافق داشتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/122764" target="_blank">📅 13:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122763">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e1bdf653.mp4?token=eFPaw0fKT0xhtY_j1wXMTruztls6wKt4jJtIwwjAjOaTaXLaefqSPhLSgtzBtI1wxg01-914ucrjEsU40sikldl4Z9zAvnbtd5M87F2yfw3Bed_mobfa2ljMShduYzXwxpSdg457Eincz4yYez1yBVbDm6MofxaeI-OUfcQDa86EhV4nX4iOdlxnzsYAAA1RM54t4pTJqF1PhRCeQBBcyOwKXkOz_UCbl7nRKU7JC165vSGSqlYHqVQdqBudFePt4-yW2YNVn-Aa4HeVRKPS2OldAjpQmQdmfp6CZD7Dz-spw1t1z-hcK-nydH_JjuJTt3w9XJ5kdMw-Avu_OvZxUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e1bdf653.mp4?token=eFPaw0fKT0xhtY_j1wXMTruztls6wKt4jJtIwwjAjOaTaXLaefqSPhLSgtzBtI1wxg01-914ucrjEsU40sikldl4Z9zAvnbtd5M87F2yfw3Bed_mobfa2ljMShduYzXwxpSdg457Eincz4yYez1yBVbDm6MofxaeI-OUfcQDa86EhV4nX4iOdlxnzsYAAA1RM54t4pTJqF1PhRCeQBBcyOwKXkOz_UCbl7nRKU7JC165vSGSqlYHqVQdqBudFePt4-yW2YNVn-Aa4HeVRKPS2OldAjpQmQdmfp6CZD7Dz-spw1t1z-hcK-nydH_JjuJTt3w9XJ5kdMw-Avu_OvZxUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل :  دیشب بیشتر از ۱۰۰ موضع و نیروهای حزب‌الله رو تو دره بقاع و جنوب لبنان هدف حمله قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/122763" target="_blank">📅 13:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122762">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
دادستان تهران: ۱۳ مدیر شرکت‌های پتروشیمی به دلیل عدم رفع تعهدات ارزی احضار شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/122762" target="_blank">📅 13:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122761">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5zWeJgAwXSuCAWCVmp80_Dw-igLvJLA4L1ktYxlVLXaJSwjwH8ETCaGkLKdKPe66wbjjrp7caZOvg9VXoxX_dy4k3xhmyohiBEFRV9GcjezQXh4DZ62JGIdra3NXcm1S6-1vEjaOjKdNyrVMBWcLde9k9HNDRuq-IhKCDMK_AwagHbMZnjazPxv74NsYvle7cww3civNQxfFZMKPnuyXKHqW8ZDXebQBInuHbPQmS8oHA1i7DQTtbIZ0v8x7Sq5F6E2YpFD5nzf91LcADRZ4xxDkAVrlEValjuVyEdJ8QkLjmDlYs-qqMq9tt9wtaGEd0wqUUHfz00eJmqTchdjkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) هشدار تخلیه فوری در شهر النبطیه صادر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/122761" target="_blank">📅 12:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122760">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
تسنیم به نقل از  یک منبع آگاه نزدیک به تیم مذاکره کننده: طبق متن ۱۴ ماده ای یادداشت تفاهم، منابع بلوکه شده ایران باید در طول ‌مذاکرات آزاد شود که این مبلغ ۲۴ میلیارد دلار برآورد شده است.
🔴
ایران تاکید دارد که نصف این مبلغ باید با شروع اعلام یادداشت تفاهم در دسترس قرار گیرد و بقیه در طول ۶۰ روز منتقل شود.
🔴
سفر قالیباف به قطر هم برای تفاهم درباره اجرایی‌سازی این مطالبه ایران و نحوه دسترسی به ۱۲ میلیارد دلار در گام اول و رفع موانع بوده است.
🔴
با توجه به تجربه تفاهم بر سر آزادسازی پول‌های ایران در کره جنوبی و قطر، تاکید بر این بود که مراحل اجرایی با دقت پیگیری شود تا این تجربه مجدد تکرار نشود. به همین دلیل با استفاده از تجربه نوبت قبل این سفر انجام شد تا اختلالی در دسترسی به این مبالغ پیش نیاید و از این جنبه سفر نتایج خوبی داشت.
🔴
مذاکرات قطر در مجموع خوب بود و موجب پیشرفت در مذاکرات کلی شد. در این حال نباید فراموش کرد که آمریکا به عنوان یک طرف بدعهد شناخته می شود و از این جهت ایران با احتیاط فراوان به مسائل می نگرد.
🔴
همچنین یک منبع مطلع دیگر در واکنش به اظهارات سخنگوی وزارت خارجه قطر مبنی بر اینکه این کشور پولی برای ضمانت تفاهم‌نامه ایران و آمریکا نمی‌دهد گفت که این اظهارات قطری‌ها در کل اشتباه نیست چرا که منابع مورد گفت و گو در دوحه متعلق به ایران است و ربطی به ضمانت تفاهم ندارد و ایران به دلیل تجربه‌های قبلی با دقت‌نظر و سخت‌گیری کامل به دنبال بازگشت این منابع است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/122760" target="_blank">📅 12:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122759">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b03851a697.mp4?token=BIX9THiHcTJeqdQxBavSmeq6OJ3RlrYL6ecSmlqpNSmN6QioKF9G7AXWwn8PV2dWR0AJ1U03EgHymUgwZuGEY6MYni3wND4B82xp7E_Q-wxIhGpS9CnoSuXYWzyIi-HQnxPX41Bx7ZSMmO2kMEqVxXyOfYeB7thE7aDxFMboB8tXI8AlDqvwTU-RFnDrH0X_QcA21dGIXSyYuN9t-ZywRoQnn7LBKJvBq0277c966Y0dGq6RFvXIWVhU9wb3FRsvlphwFmgoql-P4eXzUsSaaivWRI4cf8OIbsFSn8Io08yBtSS7h2etS1vFTJaQaes4P6scnnGs4F15WMZPBM1IOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b03851a697.mp4?token=BIX9THiHcTJeqdQxBavSmeq6OJ3RlrYL6ecSmlqpNSmN6QioKF9G7AXWwn8PV2dWR0AJ1U03EgHymUgwZuGEY6MYni3wND4B82xp7E_Q-wxIhGpS9CnoSuXYWzyIi-HQnxPX41Bx7ZSMmO2kMEqVxXyOfYeB7thE7aDxFMboB8tXI8AlDqvwTU-RFnDrH0X_QcA21dGIXSyYuN9t-ZywRoQnn7LBKJvBq0277c966Y0dGq6RFvXIWVhU9wb3FRsvlphwFmgoql-P4eXzUsSaaivWRI4cf8OIbsFSn8Io08yBtSS7h2etS1vFTJaQaes4P6scnnGs4F15WMZPBM1IOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امنیت ملی اسرائیل بن گویر: اگر دولت لبنان کنترل حزب‌الله را ندارد، آنگاه سرزمین‌های جنوب لیتانی — و حتی جنوب زهرانی — باید به یک «منطقه امنیتی» برای دولت اسرائیل تبدیل شوند.
🔴
ما باید برق را قطع کنیم، زیرساخت‌ها را نابود کنیم و به آن‌ها روشن کنیم: اگر تروریسم وجود دارد، شما رنج خواهید برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122759" target="_blank">📅 12:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122758">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وزیر دفاع طالبان به روسیه سفر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/122758" target="_blank">📅 12:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122757">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزیر علوم: در خصوص نحوه برگزاری امتحانات دانشگاه‌ها، ظرف چند روز آینده تصمیم نهایی را به اطلاع دانشجویان خواهیم رساند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/122757" target="_blank">📅 12:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122756">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ادعای آسوشیتدپرس: میانجی‌گری قطر توانسته است به یک تفاهم میان آمریکا و ایران درباره «دارایی‌های مسدود شده» دست یابد.
🔴
انتظار می‌رود ایالات متحده و ایران امروز توافقی را درباره «پول‌های مسدود شده» اعلام کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/122756" target="_blank">📅 12:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122755">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZ6bufY8jQHLV4bYLATF2H0toO4ah_wnY0890UxahZVBg_O_vFS24Sv9ewqdGub9w8GMLCyJ1XP8bQBi288kSnC6-sW4WRzW-CaIWYmmUcPo9msPK613L1_ZE3-T4qplNhpF754MRK-kEKdcfaLr04n2aqplCdT4HEtUZ2M_Z1HH4ikr1WjVa_wGnpeMgc2wXAh-Pc0raZNcf_MZQ7p_Ju6m1vZ3KetBiSy29oLS4hTIAXI9o8Sc0pYrjqe77olyrYzMtmjpzGWiMsSR0zJy2JOfRU9ewHvirlQqFwK7u9Yd_vmlfjyJmuJKM9fPT82x5z3v7tpPjnLA7FTKJpm6AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدارهای پهپاد در منطقه خط رویارویی، شمال اسرائیل فعال هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/122755" target="_blank">📅 12:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122754">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سخنگوی دولت درباره گمانه‌زنی‌ها پیرامون افزایش قیمت بنزین: ما در طول جنگ گذشته آسیب‌هایی دیده‌ایم که قابل انکار نیست
🔴
تولید داخلی با اصلاح ساختار‌هایی که صورت می‌گیرد، باید مدیریت شود
🔴
درباره عدد و رقم قیمت سوخت چیزی در دولت مطرح نشده
🔴
افزایش مبلغ کالابرگ در حال بررسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/122754" target="_blank">📅 12:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122753">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
اتحادیه مرغداران: قیمت واقعی مرغ ۳۸۰ هزار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/122753" target="_blank">📅 12:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122752">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0befa76344.mp4?token=i149rEaiYXvSR77XL9GWScxthHalTLG8k6mce5KXf0q6hl6NC8m_Er3Kxg6JkJbAd4oGbaWOAYUaH3C8-6nw6kmrurchnibiGleY3kTpMJEL0bdnVIfhT8u1AeNOLceIyxcnGYgn9sC5shyvl5_sPLBRlFEb1f5TSnr0PNpwr_8eBRGuc20wGXHst8X_D1G1e2LKVyt2DWkVMnsSPjD0Bjjd2Y14-s3sQQcc-TBkLkmp7y4WvHYc8httfTJJ46nJj4ZuhlvqWLEObajuhcllp8lx2SEZI1Kc3vBEduESV6EX1T6jMQbgfrUnch4v8jdg1tYLqwcQKmgKWRX3Pt8o-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0befa76344.mp4?token=i149rEaiYXvSR77XL9GWScxthHalTLG8k6mce5KXf0q6hl6NC8m_Er3Kxg6JkJbAd4oGbaWOAYUaH3C8-6nw6kmrurchnibiGleY3kTpMJEL0bdnVIfhT8u1AeNOLceIyxcnGYgn9sC5shyvl5_sPLBRlFEb1f5TSnr0PNpwr_8eBRGuc20wGXHst8X_D1G1e2LKVyt2DWkVMnsSPjD0Bjjd2Y14-s3sQQcc-TBkLkmp7y4WvHYc8httfTJJ46nJj4ZuhlvqWLEObajuhcllp8lx2SEZI1Kc3vBEduESV6EX1T6jMQbgfrUnch4v8jdg1tYLqwcQKmgKWRX3Pt8o-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایران یک ماه پیش به نفتکش «ایده‌میتسو مارو» اجازه داد تا از تنگهٔ هرمز عبور کند و نخستین نفتکش ژاپنی باشد که از زمان حمله علیه ایران از این آب‌راه عبور می‌کند.
🔴
ژاپن که به‌شدت به نفت خلیج‌فارس وابسته است، هنوز 39 نفتکش دیگر در خلیج‌فارس دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/122752" target="_blank">📅 12:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122751">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuF3W8hnlGy-fn4jdY_Ij8scDpPeIJI41N3Nl0tGF6yzqsmEXqSrrUVBbLKG_-Wd7xbmg--7Ibvr4KCPF0bugkHHnHQfgR1JiBncHLB4ie3bOroBDrNvbLIBkoVCXwKFt520wpIchsE1v_N1XkrQ0vTAjsjoW0X24YDYjvWJwXId5h665ieG4LZXSLR_-KOIR3tLazczNIqJqPaHi1mdr8Rn0If7fEqwISJHlJRpNqurNzbYjbIziVNgXlb8-BKYw-IHxUGm35Mz8NcMLViHogpntX13_ArJ15pyVpimqVAj8IER5pPmJmnoOqzH6PrxT8DDZXIerEY94SnWKYloug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آکسیوس: به نظر می‌رسد اظهار نظر ترامپ نشان‌دهنده‌ی نرم‌تر شدن موضع ایالات متحده در مورد ذخایر اورانیوم غنی‌شده و نزدیک‌تر شدن به موضع ایران در این مورد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/122751" target="_blank">📅 12:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122748">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJXfwq3hpoTw33gDV298ptt4ju7-6ITO36TKnJcirKfmsiJnBcv0hya6XqbGoOUXbg1-gmFfQyLn9p7zv5yxrR7dcgHuoqInk99YPbqgpyMdcnsHcNpHqN9q82dOREO4GiqqjKMwbgZNYDP43RGIMOIeGWWg6jketusDHoZjP01fKmf1Bxv_aYY5cqEQacaZAS02ilyTpLvubcbqkSTGGMunFfxpSGl53E1vwbrZw2YN4ZWz00iK72W9ZGlMOJyTCucBHCJIJMpoMXDUtXyB2hBVFQ3pmd8wWvnI3A46VYlVO73eivEfkTMUQr8Dj6HshsTIu9gIyc8CLeknpT23rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eLs217l2U11e1DoQcTPqvtpRAEm1vw92AJ8X0zC55uFsmngXQ0oU7m-ziRCG0pCFzB5rS-R1cq7zclNk7SIjpcnHDJ86eQU2JAlq5JO566oVRTns9jjFh_tmknZBJmhmLruHxdofBg8xqJAX7qaKhIPpEtbx4yutkbqsIxFPyqMxTTzh4iGQR6SEsuuwOOY1zccwq4MdJ1Zs_OYmucAS0TL8QJcxZErGcrnZR-tgIdj_Ydjf8xvmrL_C-qmIoLe6-hJIQ4HNmEfe2FQ4mNjQ-n0XpRiKZ74Z0jtbXMJ6f8gUM-K8laU5UYJPTQOpfMimeVIZFLHU4tXvlPMPthXmvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_it0rTE19tqAgePcoPr5-Bs5uuxZ6sfWElNSoNCvBEM7YmwoB5PYyq8ezwOT87Lv5vxlZo-k95GQJiX4WLz1hwntsea-Qd-2nzIlcH4u7I0_R-w-pfwoTYjQKafY3zeRwRgQeBhqPWGgM3shGPK4JL0FLxRdwuSJIlY5PivZQxaQtrM3O_Ta-jNsVoQodVS8DS3dIaxamcUwo-wjPHmAi8WFZ0F7d74nmD_SdgkCxfZGzbAoDRKvOga4HaIwuCwXDn96VOFnaFvHTxHuxS918KzmH8y5PRv2-bkghS817NFgIRhO2DFlPHsdrepWuujGqXqd-ZzyLOuUSdHEMPe7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
امروز صبح حداقل شش حمله هوایی اسرائیلی به یومور الشقیف در جنوب لبنان هدف قرار گرفتند.
🔴
جنگنده‌های اسرائیلی و آتش توپخانه به طور مداوم در طول صبح به شهرها و روستاهای جنوب لبنان هدف قرار داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/122748" target="_blank">📅 12:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122746">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33b61f7620.mp4?token=RBugfKn0EBA4cc69lhRjQj_spPsNIJArXwqc-wcNoPhH8WSa7RgMutV42aSdyWB0eN3NpFw3lL8ukGlzbHWXgrGGuf7hhkBYcld1uCUNm-f5t1yeVEcpFWI3kIhVbIBEK3EeopM1Sf08-0agj-howbgs4DGUl7vE8UtW754wCTzdVidUaB7-LO-a6KP6o6S9je97XS4abnuDLSqGdnhcfp24b3T_Ex0j4JaHEFA54HlLOZr0Ox7vyHaivQWxLEvP7rN-sGZ5oNQy-UYAMBk3duQhehyXTcLMqeAJDADBAVHKMPg85cYovr0FPTjMgzO3VDiYqhKuVyXRdaBf7leNeVQaRJufU_7mzL_05wX-8DPHaAsp6YlIB_CCxx-gFZjAtqCopkcwRIGUA5nNZiNeP7UQSgdxAU60woYdw1GhTloTJ7wbw8uugpcDbXWduvHpE0IIeksR1LEJYeGCzUIt8JBD3Um5DOap-HERAv5C1IhCJEotVXNEUH7JqwVX_zvvNTFxERc6Dl5fKv08tijfoFRd8whxISGqzKadCwdkm7hU3KNKCNTCSPhtHuOeFWPUoSkllYfhezC_-KMwtd0mFbvEMjtXjXiZ9C-qqmq9zAmEiLgqhultwdNikWEXLrX07h2RwvafXk8quoaKs2yyzCDIoGWQwj759irPz58gqik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33b61f7620.mp4?token=RBugfKn0EBA4cc69lhRjQj_spPsNIJArXwqc-wcNoPhH8WSa7RgMutV42aSdyWB0eN3NpFw3lL8ukGlzbHWXgrGGuf7hhkBYcld1uCUNm-f5t1yeVEcpFWI3kIhVbIBEK3EeopM1Sf08-0agj-howbgs4DGUl7vE8UtW754wCTzdVidUaB7-LO-a6KP6o6S9je97XS4abnuDLSqGdnhcfp24b3T_Ex0j4JaHEFA54HlLOZr0Ox7vyHaivQWxLEvP7rN-sGZ5oNQy-UYAMBk3duQhehyXTcLMqeAJDADBAVHKMPg85cYovr0FPTjMgzO3VDiYqhKuVyXRdaBf7leNeVQaRJufU_7mzL_05wX-8DPHaAsp6YlIB_CCxx-gFZjAtqCopkcwRIGUA5nNZiNeP7UQSgdxAU60woYdw1GhTloTJ7wbw8uugpcDbXWduvHpE0IIeksR1LEJYeGCzUIt8JBD3Um5DOap-HERAv5C1IhCJEotVXNEUH7JqwVX_zvvNTFxERc6Dl5fKv08tijfoFRd8whxISGqzKadCwdkm7hU3KNKCNTCSPhtHuOeFWPUoSkllYfhezC_-KMwtd0mFbvEMjtXjXiZ9C-qqmq9zAmEiLgqhultwdNikWEXLrX07h2RwvafXk8quoaKs2yyzCDIoGWQwj759irPz58gqik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌هایی از جنوب لبنان پس از حملات اسرائیلی در طول شب.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/122746" target="_blank">📅 12:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122745">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC4r2EE9jxY509hhLQO_9Wqr4drzB5LOGMXE6PN3PHAoh6oXA0Sbw7j3ftM-RFyx-sA4Vu1c_2r_QlX7gjTxYeL6OvKFfffmFJF0NukfACvL8lHO2JekgmNF2zsfW3IPZS4676iLEt-ddLnufTQWDivjvHjvuaGIP14AeUe7hAgybrRA04W4JwqoI_k7YFsjXt8ZQai1r6mr3B3dyenWH5Nv_W7ShoUBqiJIOfYT-n6nxIPZnKxr-LDqTB6Mj-RK8vAkvB1e-ZqrR0Yu2dOJFtZd8Z-BQizK_NmgUyYRyBotX8RsMuOoAysOIBlj4cvKQBjRDU7JVNZeDHp_wjLWBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اتحادیه کانفیگ فروشان ایرانی بیانیه داد:
کار جمهوری اسلامی ایران بسیار زشت بود. تاکید میکنم بسیار زشت! آن‌ها اینترنت را باز کردند و حمله‌ای شدید به دارایی ما زدند! تا 24 ساعت آینده مهلت میدهیم که اینترنت را قطع کنند. اگر نکنند آن‌ها را به عصر حجر. برمیگردونیم. خواهیم دید چه میشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/122745" target="_blank">📅 12:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122744">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
امروز صبح حملات هوایی اسرائیل به مناطق متعددی در جنوب لبنان هدف قرار گرفت:
🔴
ارزون
🔴
صریفه x2
🔴
برج قلاوی
🔴
کفرسیر
🔴
کوثاریه الروز
🔴
کفرا
🔴
مجدل سلم
🔴
یحمر الشافیق x6
🔴
برشیت x2
🔴
حارس
🔴
دیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/122744" target="_blank">📅 11:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122743">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
رئیس‌جمهور روسیه، ولادیمیر پوتین، قانونی را امضا کرد که اجازه می‌دهد از نیروهای نظامی برای حفاظت از شهروندان روسیه در خارج از کشور که توسط دادگاه‌های خارجی یا دادگاه‌های بین‌المللی دستگیر، بازداشت، زندانی یا تحت پیگرد قرار می‌گیرند، استفاده شود.
🔴
این قانون در مواردی اعمال می‌شود که دادگاه‌ها بدون مشارکت روسیه عمل می‌کنند و صلاحیت آن‌ها بر اساس معاهده بین‌المللی شامل روسیه یا قطعنامه شورای امنیت سازمان ملل نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122743" target="_blank">📅 11:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122742">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
پزشکیان: دشمن از توان تهاجمی نیروهای مسلح ایران غافلگیر شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/122742" target="_blank">📅 11:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122741">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
حزب دموکرات: امروز از قهرمانان آمریکایی که در جنگ ترامپ با ایران فداکاری نهایی کردند، تجلیل می‌کنیم.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/alonews/122741" target="_blank">📅 11:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122740">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: اسرائیل بسیج اضطراری نیروهای ذخیره را آغاز کرده است؛ از جمله یگان‌های توپخانه‌ای که به‌تازگی از خدمت ترخیص شده بودند.
🔴
این اقدام در چارچوب افزایش آمادگی‌ها برای عملیات دفاعی گسترده در لبنان و در پی ادامه حملات حزب‌الله و نقض آتش‌بس انجام می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/122740" target="_blank">📅 11:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122739">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نت‌بلاکس آپدیت جدیدی از وضعیت اینترنت بین‌الملل ایران منتشر کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/122739" target="_blank">📅 11:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122738">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سپاه اصفهان: تا ساعت ۱۳ امروز احتمال شنیده‌شدن صدای انفجارهای کنترل‌شده در محدودهٔ جنوب شهر اصفهان وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/alonews/122738" target="_blank">📅 11:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122737">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
واکنش سخنگوی دولت به پلمب برخی هتل‌ها و کافه به دلیل مساله حجاب: رویکرد دولت، رویکرد پذیرش همه مردم است؛ همان‌گونه که در طول این ۹۰ روز این اتفاق افتاده است. مردم ایران می‌دانند که دولت قصد حذف یا کنار گذاشتن هیچ گروهی را ندارد،‌ موضوع در دست بررسی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/alonews/122737" target="_blank">📅 11:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122736">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
مارکو روبیو در مورد تنگه هرمز: «روس‌ها با سیستم عوارضی موافق نیستند، چینی‌ها هم با سیستم عوارضی موافق نیستند. منظورم این است که هیچ کشوری در جهان از سیستم عوارضی حمایت نمی‌کند، به جز ایران.
🔴
بنابراین، این غیرقابل قبول است. یعنی چنین چیزی نمی‌تواند اتفاق بیفتد. تنگه باید باز، بدون مانع و بدون عوارض باشد، و بدیهی است که این کار باید بلافاصله، به محض توافق بر سر هر چیزی، انجام شود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/alonews/122736" target="_blank">📅 11:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122735">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWe2YDDD-IICDx8qHE3BkTKeEHNTtA5Od-nMmQRkgPmtTSJZUrjcFFKkBj23-G5oFt1hsZ8fQ5GkVR06lwfd_hzo9JKRDu4C06rQzWA7OAlAZh4T8ACxAMg2BLqWyhiDfB2fKj5Q00PlNJjVMg4_TmTAKzPSliOjWgEZpOiTT79jxffasg3t8QSdu7aBLFZ-FIWkPO67b7MDywRJLnRUnNW2TvuiUgzT-Lv2aoHllAPD-_aPr97SCowvffapHu1tgfNbBCQDgR17-W1uPjFtQqyF_aWBPgcEumfBAbkgKnxfVqUsTiX6vp8lHARI0MVfSzWfmYKs6H7rDWvPDDHj8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نت‌بلاکس آپدیت جدیدی از وضعیت اینترنت بین‌الملل ایران منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/alonews/122735" target="_blank">📅 11:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122734">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سپاه : دیروز یک پهپاد آمریکایی MQ9 را پس از رصد دقیق اطلاعاتی ساقط کردیم.
🔴
با شلیک به پهپاد RQ4 و جنگنده F35 متجاوز، دشمن رو فراری دادیم و از حریم ایران بیرون کردیم.
🔴
حق پاسخ به حمله دیشب امریکایی رو برای خود محفوظ نگه میداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/122734" target="_blank">📅 11:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122733">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزیر ارتباطات: با دستور رئیس‌جمهوری و پس از برگزاری ۳ جلسه فشرده کارشناسی، فرایند بازگرداندن اینترنت کشور به وضعیت قبل از دی‌ماه ۱۴۰۴ آغاز شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/122733" target="_blank">📅 11:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122732">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رویترز: استرالیا، هند، ژاپن و ایالات متحده با وضع عوارض ترانزیت در آب‌های بین‌المللی مخالفند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/122732" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122731">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سخنگوی دولت: بازگشایی اینترنت توسط رئیس جمهور به وزارت ارتباطات ابلاغ شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/122731" target="_blank">📅 10:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122730">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران: فکر می‌کنم هماهنگی و توافق قوی درباره اینکه پیش‌نویس اولیه باید چگونه باشد وجود دارد.
🔴
فکر می‌کنم، مانند هر چیز دیگری با چنین موضوعی، چند روز طول می‌کشد تا همه چیز تثبیت شود، حتی تا حد اختلاف نظر بر سر یک کلمه یا یک جمله.
🔴
یا این یک توافق خوب خواهد بود یا اصلاً توافقی صورت نخواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/122730" target="_blank">📅 10:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122729">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
پزشکیان: هر تصمیمی که برای کشور اتخاذ می‌شود باید مبتنی بر شرایط واقعی جامعه و در نظر گرفتن وضعیت معیشتی و روانی مردم باشد.
🔴
اگر جبهه داخلی تضعیف شود و مردم در سیاست‌گذاری‌ها مورد توجه قرار نگیرند، تحقق اهداف ملی در شرایط جنگی نیز با دشواری مواجه خواهد شد
؛
چراکه این مردم هستند که ستون اصلی پایداری کشور را تشکیل می‌دهند.
🔴
وحدت و انسجام داخلی مهم‌تر از هر موضوع دیگری است که باید بر روی آن کار شود و معنای وحدت نیز صرفاً در شعار خلاصه نمی‌شود، بلکه مستلزم تحمل دیدگاه‌های مختلف، شنیدن صدای جامعه، در نظر گرفتن مطالبات اقشار مختلف و تلاش برای بازگرداندن مردم به شرایط عادی زندگی، کسب‌وکار و معیشت عزتمندانه است.
🔴
یکی از اصلی‌ترین اهداف دشمن، ایجاد شکاف میان مسئولان و تضعیف انسجام مدیریتی کشور است و دولت تلاش دارد از هرگونه دوقطبی‌سازی و انتقال پیام اختلاف و تقابل جلوگیری کند.
🔴
از نیروهای مسلح به دلیل پایبندی به مأموریت‌های حرفه‌ای و پرهیز از ورود به مسائل سیاسی و جناحی قدردانی می‌کنم
🔴
این رویکرد حرفه‌ای، مسئولانه و مبتنی بر مصالح ملی، سرمایه‌ای ارزشمند برای کشور و نظام محسوب می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/alonews/122729" target="_blank">📅 10:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122728">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
مقامات آمریکا به الجزیره : ایرانی‌ها تو ۲۴ ساعت گذشته چندین بار تلاش کردن به نیروهای آمریکایی حمله کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/alonews/122728" target="_blank">📅 10:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122727">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
هاشمی؛وزیر قطع ارتباطات: بازگشایی اینترنت به وضعیت قبل دی ماه در حال اجرا هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/alonews/122727" target="_blank">📅 10:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122726">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoxyOVuXUQOrmELe96uYgy3xlCdixXIAbD_vl6uPCfZQJoV0jYw8sEOnwgvawf7BPWTWl_j0tXCV4CmachfZDORbzYRdAp1qvF4k7g4PpCPt5m9U1FBP9Ns3H6AJy1HV-I-zjD0eV2h_Y1qsJ830Irj_XaDr0L-WBRKe2_ZeKUdmsjB-fveVSHBZHLQ42d9x4ti7CHw6wMgSo-yG3DxxNsOnRupNmXWdIpXs4UYzIlzZcd04a6Ju_AC-9iNo0RvoTr15nSKMV5VaHgjjP_n2ZQCoLo_hd259BSqyRFmNqN8KGdhXaVY7f48laYn-M1mAMjJoDEn4n2kqtBuo8Lr5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا ساعاتی است جیمیل در دسترس کاربران ایران قرار گرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/alonews/122726" target="_blank">📅 10:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122725">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سیتنا: آزاد سازی اینترنت به تعویق افتاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/122725" target="_blank">📅 10:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122724">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سردار شکارچی: اگر از صادرات ایران جلوگیری شود، جمهوری اسلامی ایران از خروج نفت از منطقه جلوگیری خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/alonews/122724" target="_blank">📅 10:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122723">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: چین از تلاش‌های پاکستان در تسهیل آتش‌بس بین واشنگتن و تهران قدردانی می‌کند.
🔴
چین و پاکستان بر اجرای ابتکار پنج ماده‌ای برای بازگرداندن ثبات در خاورمیانه تأکید کردند.
🔴
چین و پاکستان آمادگی خود را برای مشارکت مثبت مشترک به منظور بازگرداندن صلح در منطقه اعلام نمودند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/alonews/122723" target="_blank">📅 10:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122722">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: جلسه کابینه داخلی امروز در پی تشدید تنش‌ها در لبنان و توافق احتمالی با ایران برگزار می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/122722" target="_blank">📅 10:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122721">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
العربی الجديد به نقل از منبع نزدیک به حزب‌الله لبنان: تهدیدات اسرائیل ما را به عقب‌نشینی وادار نخواهد کرد و موقعیت ما دفاعی باقی خواهد ماند
🔴
هرگونه تشدید نظامی با پاسخ مناسب مواجه خواهد شد
🔴
تشدید اسرائیل و نادیده گرفتن همه توافقات، دولت لبنان را ملزم به عقب‌نشینی از مذاکره مستقیم می‌کند
🔴
ما تحت هیچ شرایط آمریکایی یا اسرائیلی تسلیم نخواهیم شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/alonews/122721" target="_blank">📅 09:58 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
