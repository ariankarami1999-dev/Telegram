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
<img src="https://cdn4.telesco.pe/file/BuIeljnvCH4Dy_OvHVaKkCoDYWF8q11ZPScvC-zfUvJTqlsv_gMava8bts3q_3ET_PYXygpT28Vrf7fFAyCMwi4vA-MnZWgQ8ZGtb0JWO32SFy-dkGpZUd5pYQ9esOWO12esdIqFud7RukC8159nidbUMSJ87X2O1xxOp-VPEDUB0_D6i1aNd2nOPnMNt8RmgqSiTkbkw-Wf0xx6mFpFUPF23gfV5eqlf_rJiKHNVEhJVUhG-fYlMpxSfo-BC1eB-dflg0TZ5NaZYg1OnU9c9UlkzsW_zaxNpqAesrbXac_j8DTocUQumjei0UWjapwh3QePS4EnAA4yVgewUDMv5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 335K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 21:36:53</div>
<hr>

<div class="tg-post" id="msg-24559">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ks5Le3iGMEKgPLBOQ4_hxC4JiUancAHWvRQV-Lzahhhmoci4hnSdXx8Je70nplSXdRrfZ1EZGVuD6rhG-FXK1T1veDY5NtiIz3ZzHjTs5Y_BcsiorF_oNMvUT_7l-jXcafHuf9nL39fBVyU9dSBFUACWpy0rkaoNaU7sEgaL3EkBXV5R--AlKZhpGJQxWhD2t7anVHa320JS0sPsciJ_LE2mfYmyS1xmvC6raizHvUR5wPAGGEGUPyauWGFLsndMOxv_goCE2F3nwSUvu9dv1rRW2MWQA3Pd49TBCDKBCd7Kf47aDC8gUTefFk0gayEfYTrJe6o_DjR9iCzWmDu7Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ باشگاه اتحاد کلبا به ایجنت محمد مهدی محبی اعلام کرده که‌حاضراست با دریافت یک میلیون دلار رضایت‌نامه‌این‌بازیکن رو صادر کنه. مبلغ قبلی که باشگاه اعلام کرده بود 1.2 میلیون دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/persiana_Soccer/24559" target="_blank">📅 21:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24558">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiX51diyPx0-kj4WJmIBBSNDiJXaYR-hvvY8hxeUoqdnln6K-teHhDjVZ2na7NZqxrMJJseR2VP0p6u9i-X1EC6BFTh1nebW4nQR7rzUij8gmZXMYGDiOX6KDix1dPDhh2lrymRca2JiSgPoP5vQssTx7LAqS82pLgzlAudjSIgD04HaeFYIR0uZFlUgx3JQP3h3UJcnpdYHpAmpALAW-m4rV8SVxl0m7d7W3q9-YMGVd6kgkRoGHpItTfdUYxU2BKCGXJKh9AWaX-RzLEllufIWUQUARgWGxyy5M6hj6XcAJjPthAsC0dvuxB2q2oDNQQ35Xk1UH_NMlj0-LqnDWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
باشگاه سپاهان 72 ساعت به سید حسین حسینی دروازه‌بان 33 ساله‌فصل‌گذشته خود فرصت داده تاتصمیم نهایی‌اش‌رو برای موندن یا رفتن از این تیم بگیره. مدیریت سپاهان همچون بقیه بازیکنان از حسینی خواسته رقم قرارداش رو کاهش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/24558" target="_blank">📅 21:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24557">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTsEKx_omK7QRzdzED3yCnfGcmUzxjgXLTbO_huRrzOjLEpfc4W2IajkGuAP2p8zGtwdYacsLv0rhVn5gtyu31v3wv5TxbyTe6vqSDC1iGrYL_xNaPPquV2z8yQB2AH_t36w-qTVRrxbzc-wrv6FWVDj8skPkif2RRVYnnpIYkjQ059EM4OJA0wYNuHLehY4n_SestmwftXDPqi_3E-TE0UuOc4Sp5vhlVk-uV507_CDO-t5ULk1-s_wpGL_6gkIKZKrjJjZ5l66L-9zUXcJDJoYH1Zh45XX2NAbryspABtY00DhgWP_Opjz25CioruSuh4DRPPwosdV4P80j5221w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|رابرت لواندوفسکی با ایجنتش راهی‌آمریکا شده تا با باشگاه شیکاگو فایر مذاکراتی انجام بده و درصورت توافق نهایی با این باشگاه قراردادی دو ساله به ارزش 6M€ امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/24557" target="_blank">📅 21:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24556">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_52zAoaptBA2uZisKsrNOWGUqakKxq8ArBM8561dKC8MXJwhhuZHH1F4gLpJikvdR7T1J3nUTFLB1QB-iSbMR-e5O1kD4ZRaW-Iq6hfZvd8wubuNlclVyPBaJbEXgVsiE-cwn9rJ04YMZmjRQkwpQ7t3NYBdm0iOX4Kbx13YbastcG3_EmmnjGpDn5IrV4zm8c53KdT4K7KvNSOQJhsiBDz5CAYtEb6gVVpLXC1UF8tDGUfcOmq9inRk5nDQikr1nBDgIKnIkOFBF8PiLNoK5fXkeiAp5hxnaBbRAa9G9bN2-X3pe7KME4jC_Hvapkdu_yh7GKJR2AiV8e_K-EuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
🏆
#تکمیلی؛ سرمربی تیم‌ملی‌کره‌جنوبی بعد از حذف در مرحله‌گروهی‌جام‌جهانی ضمن عذرخواهی از مردم کشورش از سمت خود کناره‌گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/24556" target="_blank">📅 20:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24555">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=FxkQuneNuJ4mMnsBLQK0h6PlemWEpGB3yG6Lg0XmopeUlCKntSVeH4VFShv3gjZ_m0FszspF8O1gV7DGOYHa16vkCCgyI_HAZwT9yTe2dppxRat-Q1tOePv39_S6FGwsrlyQMqqYcF8EUiH9LvJX8gWvkmXKxt4DdkinMsN9HJ1PEuULDgOLApHlCcnwNn8rtCNMqjjbxqXUb3zWxnOtPd83yrx53PHzeEuSk4xyZVQjYP2K_63F_WcuZHNGCBlvE4G5vdRiKWwmrgYme9zuy3fvqHUfZQnws70jQ6W6LJIAEb3JXzMT-CjSV8CXNg5VSyd_ZmTjzvFZGXYH_zmWYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=FxkQuneNuJ4mMnsBLQK0h6PlemWEpGB3yG6Lg0XmopeUlCKntSVeH4VFShv3gjZ_m0FszspF8O1gV7DGOYHa16vkCCgyI_HAZwT9yTe2dppxRat-Q1tOePv39_S6FGwsrlyQMqqYcF8EUiH9LvJX8gWvkmXKxt4DdkinMsN9HJ1PEuULDgOLApHlCcnwNn8rtCNMqjjbxqXUb3zWxnOtPd83yrx53PHzeEuSk4xyZVQjYP2K_63F_WcuZHNGCBlvE4G5vdRiKWwmrgYme9zuy3fvqHUfZQnws70jQ6W6LJIAEb3JXzMT-CjSV8CXNg5VSyd_ZmTjzvFZGXYH_zmWYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌ازتاریخی‌ترین گزارشای صداوسیما از رقابت های جام جهانی که تا ابد ماندگار شد. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/24555" target="_blank">📅 20:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24554">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=pY74vQbMDLFrRkC_DrJUluhvkcvv8DuqQ_cKF0eI_YobYzbzKT2cMc4C-YZvKyY8VWYklVN-QosBCCTcle9lABdfkzNW2OkhRNujxKGlQfID0dr2BFLxA6EmPloyWytUwxaHCbGqRv5iPxqtK35xOeYkNapy6Xo3t0llmRMtT99A9zx6Uztme0mjZxcPAadn2zxEBMqxvDgoaoP9iGsY7_gSZJ0Nm5RHjS_ETGZpv28mC4GR7shGIAF6h6GpGooL8oUK5RCkl62jD6T6x9DkjB6dy5QZNvyxgUBGsfXkaEh-j-h3vl0VgMjBLkXI-5mecya_EDOsaupF7gTiMqA2rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=pY74vQbMDLFrRkC_DrJUluhvkcvv8DuqQ_cKF0eI_YobYzbzKT2cMc4C-YZvKyY8VWYklVN-QosBCCTcle9lABdfkzNW2OkhRNujxKGlQfID0dr2BFLxA6EmPloyWytUwxaHCbGqRv5iPxqtK35xOeYkNapy6Xo3t0llmRMtT99A9zx6Uztme0mjZxcPAadn2zxEBMqxvDgoaoP9iGsY7_gSZJ0Nm5RHjS_ETGZpv28mC4GR7shGIAF6h6GpGooL8oUK5RCkl62jD6T6x9DkjB6dy5QZNvyxgUBGsfXkaEh-j-h3vl0VgMjBLkXI-5mecya_EDOsaupF7gTiMqA2rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/24554" target="_blank">📅 19:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24553">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kr3pfjmshehlFoNMm9ZeEzhq3j072TZwb4RzqyahGwimX6dz1DLrtOsmjM6bOC08NyoouIwaPqfn2lGd4og6qh2u_MyEt1ImBbA-9S2ooCaD8WYa9MFPwjU6ga2o3WCq8Ts0dt-gl9LzqWCFXV1STfnv8l9y9A2CKQb7i87g-Iinh0bJnlGcgoP2YDZs1UnlEs7HDUBo8j8i2_Zg6LKP7YgiArpeH12fsdmQPOfUwkxdfISfdX5EhrWr1YlFXwTmPZTlb0loIHIEsu_82HXJVOZMPiZk-CBKPLY3QAPydfkGu8qFjKErNNa1_KRjp8pA4bnEKKr6KMyYWWJgNy-iLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ دراگان اسکوچیچ سرمربی فصل گذشته‌تراکتور؛ بادوماگوی دروژدک ستاره گلزن فصل قبل تراکتور صحبت های مفصلی داشته است و درصورتیکه فردا بعنوان سرمربی پرسپولیس انتخاب شود به مدیریت باشگاه خواهد گفت اقدامات لازم رو برای جذب این ستاره کروات 30 ساله انجام…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/24553" target="_blank">📅 19:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24552">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030de140d.mp4?token=sv-zVu1QxSdR7-Yy-FW0hXP05FJamXpZFaL_Wo3TevtT8LgN7N_GXU65_mj5nbLmYSMTKhWplbmX1ncU3W2MYpeVJnwCpWKNHgfYm3tCI_t7Gg0LJe_bkwfDQi2x2FTRRdcaTf0ArHyeqkutYxYxAmXTwgNtCq9ICzSCEp9UHRaFJdOHECxle5fBGOW6ZvsAR5sAvbp_jqh7fWwrJNmb4t0_oFdyNFi25l-Kb8c63xUwoSNMYPbiK4zWKtS5LyjMPNug25n36n1LJCHGWMACvgMVOFbNW551rfvMnKoG9zMA3RpSoa5ANMiL7fyFIBlMMt-vGXTu6lC-Jv3u0o22Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030de140d.mp4?token=sv-zVu1QxSdR7-Yy-FW0hXP05FJamXpZFaL_Wo3TevtT8LgN7N_GXU65_mj5nbLmYSMTKhWplbmX1ncU3W2MYpeVJnwCpWKNHgfYm3tCI_t7Gg0LJe_bkwfDQi2x2FTRRdcaTf0ArHyeqkutYxYxAmXTwgNtCq9ICzSCEp9UHRaFJdOHECxle5fBGOW6ZvsAR5sAvbp_jqh7fWwrJNmb4t0_oFdyNFi25l-Kb8c63xUwoSNMYPbiK4zWKtS5LyjMPNug25n36n1LJCHGWMACvgMVOFbNW551rfvMnKoG9zMA3RpSoa5ANMiL7fyFIBlMMt-vGXTu6lC-Jv3u0o22Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/24552" target="_blank">📅 19:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24551">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=o0PDx1syGn5Lj_IFQH23Mc1bnOy4JjoeFDfRUmZ5dO5FHnnojGj8O-pbZ5DVOEe1BBcbIs5vamsCQtmEvUBwz5tGZbkEhdXUlNBIWagW4WBDWRMDqz50P7PnHuPwVCTaZ0ck1g7CK1jE4qLDwo9nZjJmx7wT0zbfnWERrqD81N7rCXXfpaeCiba9KN7duUGBvL5O-FCgSIrCP4-H3r6lNVa-3nZItkdPGeuDP92VXyveeCyBgTL-E8KmdcuHdEftKc_o4UNc8Ae3pJgU4PdKookfcPdY6M_lxDKHwL6GDAOd2Hq0h_4NmCA4AI-qO5OoyjXWFq0khIbUcK1GrnYCzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=o0PDx1syGn5Lj_IFQH23Mc1bnOy4JjoeFDfRUmZ5dO5FHnnojGj8O-pbZ5DVOEe1BBcbIs5vamsCQtmEvUBwz5tGZbkEhdXUlNBIWagW4WBDWRMDqz50P7PnHuPwVCTaZ0ck1g7CK1jE4qLDwo9nZjJmx7wT0zbfnWERrqD81N7rCXXfpaeCiba9KN7duUGBvL5O-FCgSIrCP4-H3r6lNVa-3nZItkdPGeuDP92VXyveeCyBgTL-E8KmdcuHdEftKc_o4UNc8Ae3pJgU4PdKookfcPdY6M_lxDKHwL6GDAOd2Hq0h_4NmCA4AI-qO5OoyjXWFq0khIbUcK1GrnYCzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/24551" target="_blank">📅 18:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24550">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLOnSD2YSKkxkVP9Aglk66lhA4lYYbpPrH4OumNLCsLmEf96X-VYPz1uSo-jJii_j6OR62xDeDli3slJvSM6dDDt2XPOGmrmQuM4DeC4KSEdQ1KxOamUfUInNujuItLjlrKHxyDLTuMGUvZD_N4JxkNT7elSNow9tLhonWLgC-fuGmxG4FAxkx0Hd4Y7SKE_DRfwQfaCDcEsQo55PLNumnWdGsTqO0ljsJVOKXJUAaAzxhB9nZdyZBbIxPSFaBb9E4PG_ARtS8WclGvwDdf3-8BEpaPO5t-gYy5hyjX_IvY1Hoom7hGQl8TN8yJAVxYPHNimLvGCiL627Ac9EeqeHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه پرسپولیس 5 روز پیش پیش نویس قرارداد این باشگاه رو برای دراگان اسکوچیچ فرستاد و مربی‌کروات باامضای‌آن رسما سرمربی این باشگاه‌شد. حالایکی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده که چرابدون هماهنگی با ما پیش نویس رسمی قرارداد باشگاه…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/24550" target="_blank">📅 18:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24549">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcVxnK-RyYwR8yIeQtEJ2FAybIklz7xYHryT_NaGHBNYeqsapM6-mN9qhO3BaJArR0HG0qGo1sBqMfOkiHT8gitpWjRY0Lk22vvrT7m48huDcZ1VIymYX89XIhbUHA1-19O7o45P0iINO14h9Amxwma2AkHlxZEm3Vz6zoa7XxNsXbn45uU6W6k_LXUaGTufPT-tj-FB8NjkD9neGGIjGzdB9kmClVG7cZBASoXhDSQoRn1RHQjBCCL1IVsFfr0kzIdw4qdDcOMG-A2RNDi-gjd-kFdmM2SgqferJtdILLvE8zMq0cnaL2Fte1u63mm9q4KhhRMuH2v37r78TOpnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/24549" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24548">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxCT4C-tqUYqJUbXkc43jBbwzEnmm_mPSm4ICE2lpCxh9we37FCqOrDwQuP5py8ZffzYBENu0ob7vdbJPduR52kL9nGh4qCCHSdGlFopCGQAX8twGD8folCQBOK7gAY-6yqqKV00vGDRvHzEJGOQM4STkkbDtlG5VFE1xoSnLgZ4jfiMmmjeY-raJ_elIOv6F5Ne_qgGEAKOeHrr0Oz-YKj-HquhdCQhVX2hrVY9fcbv-XKmLA66YKDmKpGoiCs78ij4LeoIp9H1Bc68mM9bU0r1m9qvSvjjPoxPD8kXTPUaUbOsv6amVvfo99SougyrjIM7hdWor1BeZaSp5aHSpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌والیبال؛ پیروزی ارزشمند و شیرین تیم‌جوان و بی ادعای پیاتزا مقابل کوبایی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/24548" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24547">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Qw4qp4dxEDFqU8Q5JOrcr1CiJOqzRIqTXSDljYLzf_bm_cppHyNSCa5VhaqLJehNL_Fnj4LZAgmCVWOH91EQ9C2kAsye0MFLco3nZcbZvs6IhjejmHjXsPcKYriGJpNqp1DdIhsYsP86tBUt3NE1fJnQQ7qrbAjtw1PzkYiIZufswSqawf4maKWKrbjom_qAcNKOgS6xLLls7apOUvuxfvrT41B79OawQlj8p7cFrxnPRBAOSTFXNkkbyn-YOElxvb7kwB4Y3xvSBP1n5ddJQwNtRGSXjoB5g6cuLP4fm3jPpxAfPFgY0ZyCON9tbRNGPPD1n-m0cwI7GF1-fbSApQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
بالنزبت هیجان بازیهای جام رو چندین برابر کن.
⛏️
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔣
0️⃣
0️⃣
1️⃣
برای هر واریز
🔝
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
💰
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از اولین واریز
📇
امتیاز وفاداری با انواع بونوسهای روزانه مخصوص کاربران فعال لنزبت
🍀
🔣
0️⃣
3️⃣
کش بک هفتگی
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
📱
https://www.lenzbet8.online</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/24547" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24546">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=BxWR46lD21PHPgkoLQpUZ1Z4x_5t8maSD-vETOxJ311QrkK4EHm6O9Gb5fEklmuJ092gUOXk7ZZfUajliTmm9n1b9KdcPerxsb4XK0_kCWgr1MrmJbHRoEjgMkB8hf7hCoMh0sL56CkBquOklpPH6qhaeqfVt8dsIvqaxJJvY7suq5MDHuSQ0nbDU0MSO-PajW9rt-oQbL9p4FTQVFYeKjdtgEFsOCaLMTNzZ6Tz5HazDTNXHEEfsUtjM7ALMlne9Tsyx8accyaWkwYodraxNKQUjGzJNMRzk1_6pHIPsivLlQs_U3IR8RAykg3t6pRfdJuuKSU0Dxof03Kf3NkeLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=BxWR46lD21PHPgkoLQpUZ1Z4x_5t8maSD-vETOxJ311QrkK4EHm6O9Gb5fEklmuJ092gUOXk7ZZfUajliTmm9n1b9KdcPerxsb4XK0_kCWgr1MrmJbHRoEjgMkB8hf7hCoMh0sL56CkBquOklpPH6qhaeqfVt8dsIvqaxJJvY7suq5MDHuSQ0nbDU0MSO-PajW9rt-oQbL9p4FTQVFYeKjdtgEFsOCaLMTNzZ6Tz5HazDTNXHEEfsUtjM7ALMlne9Tsyx8accyaWkwYodraxNKQUjGzJNMRzk1_6pHIPsivLlQs_U3IR8RAykg3t6pRfdJuuKSU0Dxof03Kf3NkeLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24546" target="_blank">📅 18:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24545">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZk8c5Jhrre3xCGyOMIksqCLExIjxfj9Fo8poYUGDB4OWM75Peuc9_NGeNTrlU_ORtSl8zdM_4uln_m6N3wzmrp7bsmd1tLIYy5Jc2dHWpYn7g7Aho4AJdON_vZr4STNw-7efOi73VXb7iWEHBJeRdVKlLWo25DIa6OHUm9QlWyBlGGBtboXgEqJNMQ0wIOP3gaSJ2W_YIVkRuYYqk_WH1Sf9jBErBvaDviwY4ln7qKaZoWi72DgOkohBDcv6hh19MvFBKZh0cmMNEIURHTIAyV8bL3WQA0My20kyC8Qn511E8B6XfEzilxw4hD6G0EbY1_W5xgXgllkXIV8PdLukA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
جادوگرغنایی: کریس‌رونالدو میتونه راجب من هر حرفی بزنه اما بازهم تاکید میکنم این تیم به دراماتیک‌ترین‌شکل‌ممکنه قهرمان جام جهانی میشه. کیپ ورو مقابل آرژانتین همه رو شوکه خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24545" target="_blank">📅 18:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24544">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ema4j1ooSJbESNM_v-R3SOvnQTapSpt_3BCQNrBNNSor8UkIBtiRJolT41GBgnsON0TqodGFkOayvuSsAyf4A15hbtKlmlWQ0pjQI5rLW2CmqBfK9SJhpD9L8I_VADLR6QSXeUF-0vL_ce29HgTC2eNUJyldulQfRyyhoGpL_TXyS7D6dAdbiyJenS2CfqXs_crIwraQMFUmk8cPPz364L6ZtZTkMWlNH3H4EG8jO4KfQB59zubBALDdfnBGuqRyrv1Wpjs0OthIBwE3akpKLkXD5_n-7WhGZMBrzF7ng7tAwJrKp5owvumkp4J-11zap3eZnFMhdvb6M8fpRvWZqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇴
صحبت‌های خامس رودریگز ستاره تیم ملی کلمبیا درپایان دیدار با پرتغال و تقابل با رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/24544" target="_blank">📅 17:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24543">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSzGB67SdAGaRXEGZLiwF_ft94N_0_4RLYVzQSsm1PmsSncAnecT5BqcI3TZbiv6nOq-UMIhti29vfykaQCYg3XzQFsZx-35-J6DkggLpdaLG7lTHDE4JuIXmOp1BsCLbwMHup8EOFbNzUKlCOumwZDTf6auHjJHWZRmPMaOLQeMqPat585A8RjToyyWeNB1nbBWq7BtGXRQ7FQam62Vqf4cqPx1D1Hhv7-iDTfek4Aos2x19BHwxa6kh9P7rfpS2ye2b_4pHtelypt1bC4Jzcs1G-7da8_Xlky85ppJft5N2E-h3uKAt-bKVoMQYJODk3LPWqAGkNd60VU2qwZ5SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت دردناک و شدید خاویر کونسپسیون بازیکن تیم والیبال کوبا در جریان بازی با ایران؛ چه زجری داره میکشه بنده خدا. مچ پاش خُرد شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24543" target="_blank">📅 17:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24542">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwnOZ_m9JN_sIUuQI3fRuFgbifAaB-XF1laoAqvmT4DYfumxPW07DrTjpPPMUZTFYEQ96IsRd371DWkMUSmMQRA2FRtFKlKaz1jUY_E6Bk_SzUDZV43O65sX0o7s_43RHSYr4bAbFOAJ-TaA84Tqx7FLBuuukLayY0Qf25FevVzfRUmv8aOrMZ03UMfEcXoqIcim_z2vzupy3BbehCd2wWcPGUeeQBP5GmyaCQqEokEHVyYREAPpOG8bSEb1Efvt5gfmyMIGrxnz3E_wfirsp9wB0EjkvY8CUEWA-C53ufUmOEMDsf7ubwe9FlyTF_T0kUODrM-qOTK6aSGQRxUCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24542" target="_blank">📅 17:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24541">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-kg2ncUVlUXg4K3XO-TmXPQPDBTMsz0Clae2KzqC0wCLWNUHotoz5shQmak2LsKIP09MIiSIR4ifYvT9TryXkJrJpqgqm1BZsamAdUFsbOWBUhqNrONsVRu9wqsR4nKDhLVZPIuwvYH5XtviYNLOW1S6qzQN3kqdiG-Q-I2xsX5JcqoruT45usGWB6fDMKGRUVvq_CrIYlFlTDfTRNeD36XGUQcDqhOwAZh64-ZTlLLtjv93D9cqjr91Rwo2Un3PHCpLr9Gryo__IBf3kcrNJ6tJk7_EH34ueqxSWvGlIz6_Gw42yD-59f_Ne-_EXUL7Em2DmP7E482sBH6_oZBQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24541" target="_blank">📅 17:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24540">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikL4Qk2tPCmLjTAhmx8rndSanhUkqXZ7hR3T0g0i2IOzGsGUmLWt6gKBvolHnBr2IXWYI-hYuDehZo4N0N0F8Ci0Uqj1bxqwEdauTAXh-q-ceEIJPwdrJdzfJDwaI594oPVUEXNmh_0GsfYHv3KQVHabUEm32upeTSilGWN2WCs9VprVAB0pZxm1ArOy5zG8tGfmd5yjLZPpuA9jiuGXa4yCv-J_Bweju4EMUyphtzdEH35CTChOAc0m-QiYwMdBi1_cEoLm38EPKl1SpLeDzwVs03h-gzG50QbmL4zH850YGTrODjstp9SJFm4qcqwy_rx933zELBCBOzIFNgimlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/24540" target="_blank">📅 16:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24539">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiJg4U_QPMfONezQ3RUv8UZpCSPinOVicvgNYvU0XgwlyrTU9OL1yEEPlvjHhn6I9tqHSQlv-GImk6Mn1F5CCXnplCSTV50fkp_Vl9clNdSyrG_DCcR6PJiorUAkC9suisyAPjqW8HYqMUtW52MQHb1hTxSz5YJUGFp0CRy-zx_-bxtSGuTkV4BJq7L32p2v6lZHVvHbZkt92m0uXmPehrkmFOGQmCnFrVyDESHgPogfd9XrKFr4NsR8mEMasWy_NM2g97FQwyxeocd6ygDLoDQ0dXkX0itxIU8M4GO_DO2kEq9pKR83CiwVL2vNwdOPwdVy9Hpj5sZxUisI-jkNig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
سوپرگل دیدنی لیونل مسی در بازی بامداد امروز مقابل اردن؛ این ششمین گل لئو مسی 39 ساله در جام جهانی 2026 بود و 19 امین گل او در تاریخ رقابت های جام جهانی بود و با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/24539" target="_blank">📅 16:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24538">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dn07myubOlcHeRcSxL4WaTSG-JulvXyRXLlSD8aRXyGuQaA6KdrARfJrepKuptyuQUXcW0WidWG-0OpgklwIUUvlgZOFbTPkjoJPMlPnzgmmmdeAA4sCgRya9DAPF0VPH02gwXWAccQNYADoEuwbNNk984KNC4qJ4lwP0-ftF7Gpi8OMt1AdOiqACHFbqrQGbTrJth2EXY0E5elnjypwraHjFmBjBSvI3Oir65FCe9Is83fKvsHpmJPRd7O5-sKkAGg-HUQ9NeXHRAOtJvq9X_V_Oze_hP0QytYHQQwVhFiGJ4nWMlTc_eJYK23uaUcZFIu5e8mWTP_VsoI5paWhnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24538" target="_blank">📅 16:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24537">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=Zc_qsw_1D0IM3Mmth-sZQHYF0ErK6OQYGyN77LwCyj2ATFHDwyjn17V4khRZk5xia0xrQ--jlSYXK_bAB8W8uJOmtpjIMIL0Z2e6ZOHEa2XyiaXFrAlenOvjf-h_MkaC0xYQfA00KWumLHXVQY0K47UURuHfrfXlwCxmIMQyFsaIlBFCzbUV51YbyAnP3JM7fMNUs1-zPiUXeXUW4VlKBgBDpDZzuWkgxacw4aph_D6L_TJd6Fc67X3cysYvvK3UXCDJRvTRLPk_54ggKRBtPUYHmiViwRiPL3oF-KMUXcVcfMDz1frSd4Ds4dlUgIloThMMLUkwgHIrIsBtkotf8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=Zc_qsw_1D0IM3Mmth-sZQHYF0ErK6OQYGyN77LwCyj2ATFHDwyjn17V4khRZk5xia0xrQ--jlSYXK_bAB8W8uJOmtpjIMIL0Z2e6ZOHEa2XyiaXFrAlenOvjf-h_MkaC0xYQfA00KWumLHXVQY0K47UURuHfrfXlwCxmIMQyFsaIlBFCzbUV51YbyAnP3JM7fMNUs1-zPiUXeXUW4VlKBgBDpDZzuWkgxacw4aph_D6L_TJd6Fc67X3cysYvvK3UXCDJRvTRLPk_54ggKRBtPUYHmiViwRiPL3oF-KMUXcVcfMDz1frSd4Ds4dlUgIloThMMLUkwgHIrIsBtkotf8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم‌ لیگ‌ملت‌های‌ والیبال؛ باز هم ثبت یک شکست نزدیک و میلیمتری برابر شاگردان پیاتزا این بارمقابل سامورائی‌ها در پایان پنج ست مسابقه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/24537" target="_blank">📅 16:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24536">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COHdbmYdKtB5tSRyNzAKSzCHBDpMYz8bJziwrsvNFrky3GSNsJLxpyiNv-1bWuVmG_gYHffGduYlLRcYzAS69fhca8ReqprpSJv0L4FCgkmNDSxnULKWULZBSSs6gX8AnGisytqcnkbZMdeJNE1F5Ctm1foFlnR-26aOVNSbRWqngbZnFaFUALRqx4r8tuWIub6L0yNl4zNtshsM00ZHnCbCkf5c2hGnBqfRydWGIv0bbXJVLNQdkBtx90dzU8NNdcg_G9sCcfN_xRyqNwYNSXZFwH1ic3o_Yeo7kMupu7UHrQgIC3BGOulRkhvHy9Yhtx0Ni2ux7-nAnPYP02AChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا
#فوری
؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر درفصل جدید متقاعد کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24536" target="_blank">📅 16:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24535">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCKVYQmNdKc_HEqnWUnzta2rmLuVAT5digCngF52po758pvbd76s0Oa3Z2kq8VN49EVS-T88gmKuYjnweI2cZStWw_n4D3AOXNR631K6EYQxWS_NzwMS9XdlyRQZUFj23uE8ijVFhhJmiSnhv5o_2JvhKWPb1Ut-0fB05wpvpneg_-4_9Elxq0RikxC5cjqHYAY_W-0XUlruILxQBql0cYFHFABdSosQ6EzbhmIuf542Di-cHiseLbGsMDEMpjTd0k76VyxNNZNFtlh3izq7lkh2iTOtkAeBjWLX98WPsgw94iZ7Fd7sd9eaRR0OdHuv958JkKLADN7OgPapmpFVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24535" target="_blank">📅 16:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24534">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0_W8yB-nC-ncJ9Ayc0lAgAPo8He8yAM87Ja7vh56nM0CYm84WJ2XuSQOag8rWMxeUtn_Re8tGvxhGguQ8pmCBYdbcdvkAgRzGIpPDWxlhQnzYbSmQ_HkM9oHhxnMxnf96c0GEOiRJDMEk1jcBugjjQ2fqJOPoz0bzZayrcOPylULMrRsVFizsxKLv-M79NeRzzMX7nE0GNfTX3yTqd4WWJ6ve5RieiAU8gpIkvvFsz9QWZeJtOBQfpLhPdzRTsgItcfJZaqj3wOww4e7KFCyRqPuP1LsbqVNCL-BzBjssc829Ektd-XCC8t2mN5pJdHy2MFnOorpBeFwAq32we8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌شایعات‌مطرح‌شده؛ پیوستن دراگان اسکوچیچ به پرسپولیس منتفی نشده است اما یکی از مدیران بانک شهر گفته چرا باید این دو شروط اسکوچیچ رو بپذیریم. ولی چیزی منتفی نشده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24534" target="_blank">📅 15:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24533">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🏆
ویدیو کامل گل های روز گذشته رقابت های جام جهانی در روزاخرمرحله‌گروهی این‌رقابت‌های جذاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24533" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24531">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UK9XigW6u7bmYUaRSRtZkf4AYCPHHry4yXA8l0Biio8jQg9LvqEoVVvs6aWOXs_rbGATYuyt7ow4P2kkoiTToLoBVb5H9G8vHymstArzw_XxGo0SWx7dPB4hYCtZhlEZc_iGmz5KSwcCBmzT3bTYmJPouboNzrkjNO8yVyi9IyZ9TpEEx0PH6BiuBYIuDm6WWNAuBsrpoJZhY0V14G4JR6kbhTdXyxPRB4cuSUP8syPYQ_I6zqqfGytb05D4zOxNiRc7Jq9WH_mWjk3CxyTEdqo4YTddkQ1X6T6K72MVX3FxY9mGpClS7bge4hNN0rToe0I0dfok8JR7GE_rGRee-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=HaqNWKCSmJkXQ7U0-CQFNarpIcQzJ3pWiEwJTbUN6mMOSiB9zKXiapUW_Wa8NFwlI4Y-Xh_pcdOC04WgCYLNExvFoinhqNgTHJzgrFgE-DdQgl8ja2tjogYBuZfsJN7fw-baoyswPE-m3JyuwDCOz_oqL38IDPNSeWudO0ytiO34eyWhbOvWxbzGucjnZqNf4rOIs_TovwR9eG7aa42gRpx3N6jlayL_DJOdhjAJ7hPEtuw6t9bCbGNP_AGxEVCuhP-kJAFL38eQ-p-OOI0i0-Xl29y-PdjbZg-a3qgG-rvZV4ucc6_vx5HCE8zSxLB0dw1eu0vKbUTgrCo4DgxNRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=HaqNWKCSmJkXQ7U0-CQFNarpIcQzJ3pWiEwJTbUN6mMOSiB9zKXiapUW_Wa8NFwlI4Y-Xh_pcdOC04WgCYLNExvFoinhqNgTHJzgrFgE-DdQgl8ja2tjogYBuZfsJN7fw-baoyswPE-m3JyuwDCOz_oqL38IDPNSeWudO0ytiO34eyWhbOvWxbzGucjnZqNf4rOIs_TovwR9eG7aa42gRpx3N6jlayL_DJOdhjAJ7hPEtuw6t9bCbGNP_AGxEVCuhP-kJAFL38eQ-p-OOI0i0-Xl29y-PdjbZg-a3qgG-rvZV4ucc6_vx5HCE8zSxLB0dw1eu0vKbUTgrCo4DgxNRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شایعاتی پخش شده که آقای هنکاپیه بازیکن تیم ملی اکوادور با سابرینا کارپنتر خواننده و بازیگر معروف آمریکایی وارد رابطه شده؛ سابرینا در بازی اکوادور مقابل المان هم حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24531" target="_blank">📅 15:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24530">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWUMmcdQy4gbPFnoppVQ4Ql4XXZMb7hDBi2U_u2_Z9TJTuipybnErQIabFUzwCr2cQ8kTjf2UgYd63X2VNFfp5kZgt-3xvXHQOz9VqMEW7emBERC8kkTObEvwp99zS-t19JIpY-WMDB8-KImyG3cckplJbCq8TOzbssuLCYm9PH2tLcBYGI1h888u_xL09yC7RGRq0LuPJaFDpuuYTbZbKgVWveV0Tw5mthm0YOoTvYn-Ui3rgQtKPHQyhQ1tRonEkYiF2ae-Xm7Uz8Zj8Cm4yopaop6UmwU-vZ-JVTUkqkAu2rWWiOVRXmrv_6WoJouegXzneU5YwyRAsp-q94Jxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24530" target="_blank">📅 14:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24529">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqbPGNa2CEVHb7hAeiJ5Tg7-05Z0kvP3y8Jiqm63UZYDK92mHNP1QCwU1qVdzHC8XnwP4lWRQ9vUK6gPmih2d0yanZQKcoC2QUHbNi_ff9ilImnH_qQbEV7i8vcNbwax3X2WXl9E3HCr2e25Wr9Df-wqdW2OcGL29qatqOPzV2yVox6ISlWA2bMSJjqdPW9S1wK3Lxx0Cf6UDIEPRRn8DC4qo6bi7prRfIkoz4fIIW5s7YYEdgjcQ6KTAxrtBWU3Yu-8LYR4PI78UJBJ3T9H07Z-pA7Rcey8Xlb76GSE2TCloS6Y-kH5y49PCI1IeZvleDOsEFOLZVqICe6u4QwfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24529" target="_blank">📅 13:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24528">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=gXRePqjfoTj05oEEHvozpQAOX9hnpxLoutnF2c4bQ8S5rhPvWPu0CWV3ci028sJ2WEQ_APVdp23IGa7_Lz1jW3Z0Mk15opX9Ul5UxDC_mGeUwy-iyku-Ybc-2aF0emrY_PCX_7G2CW1CMFkqNOS1oCTWvouanyYZvEWsxiPkD0KRUsJcb-r-5aFVWhDpMkb7m-pLRF08LSgm5zFOJCnprxhTB8_tKWyf3FxJv3WvsWy_REarG4YB4IMxWOrLlN3NZcxpQbgirKv2uWzShHkqjqAFgfjUTbHao26PEE7vD6B3KajEKZVUBU5OK5fLSBaoGVTE-CWG4eSazGE-SCsGPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=gXRePqjfoTj05oEEHvozpQAOX9hnpxLoutnF2c4bQ8S5rhPvWPu0CWV3ci028sJ2WEQ_APVdp23IGa7_Lz1jW3Z0Mk15opX9Ul5UxDC_mGeUwy-iyku-Ybc-2aF0emrY_PCX_7G2CW1CMFkqNOS1oCTWvouanyYZvEWsxiPkD0KRUsJcb-r-5aFVWhDpMkb7m-pLRF08LSgm5zFOJCnprxhTB8_tKWyf3FxJv3WvsWy_REarG4YB4IMxWOrLlN3NZcxpQbgirKv2uWzShHkqjqAFgfjUTbHao26PEE7vD6B3KajEKZVUBU5OK5fLSBaoGVTE-CWG4eSazGE-SCsGPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24528" target="_blank">📅 13:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24527">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=tspkEOY47yLlzHoEGsyVuEgKhy2P0rgpmT9vRsJ8-HdVRDfCPWdvg-qMia0WRGXd9SKrITRrbII3f1K_TkrQ8FDe-g2RvQvWuBSLgjhmC3rYGpzA-rn54WtTH0EKo_uPDscg2RrGttbC2gdW-Ft0U_sYs1HlCdj7ElpaO9Fn-ZFS3grhn2Y1Uot4ZHGO1EWAq8Ub3gzMFYzRY-AH4tQ0OVnh8Htg_lf5NXae5LJXa7F2MxPsMVD6ZtmcmVDkZkD5El3a0O_ivxTL7ehxZMryBR285chMAd2vzd5fxF2V9vf44fFgIBRaBO38-ESCO4sWod4qSAN6kb7ZBIF67jGzkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=tspkEOY47yLlzHoEGsyVuEgKhy2P0rgpmT9vRsJ8-HdVRDfCPWdvg-qMia0WRGXd9SKrITRrbII3f1K_TkrQ8FDe-g2RvQvWuBSLgjhmC3rYGpzA-rn54WtTH0EKo_uPDscg2RrGttbC2gdW-Ft0U_sYs1HlCdj7ElpaO9Fn-ZFS3grhn2Y1Uot4ZHGO1EWAq8Ub3gzMFYzRY-AH4tQ0OVnh8Htg_lf5NXae5LJXa7F2MxPsMVD6ZtmcmVDkZkD5El3a0O_ivxTL7ehxZMryBR285chMAd2vzd5fxF2V9vf44fFgIBRaBO38-ESCO4sWod4qSAN6kb7ZBIF67jGzkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛
ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر ۳ الجزایر و اتریش حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24527" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24525">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldc3yl7Niq0mdCEA_YflqYVd6LhqVbuHna0ZihIo2w2Fv_HTl0LrgQ2_uB0xlwM5JOi_3nNpP9z-KNwAwwzBurorObO2LFahyrwJHoUcxBfzQEST76Hyj81oPsdWYAjsrjJdtpHJiFw1aLDNKLdMBbI9xKRXDFGitTQXsWeaTGx9efM02gZ0FGUmQ5EjdVI3FkoYOTvdZmywLJqZKJxPXamBysDN36TbNYqJysfK91cD-OW37accuIAZkJ5DhVPxazcfyYU9O6q66eKjjGGu18qeDy2TX-hNYPogY6VTr8FTrTu8Cblbkz_cv33WsEX4G8UoLI0P3t9UjcHbTmAg1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏که‌مردم‌ایران نفهمن و بی عقل آره؟ خدا هم یجور گذاشت تو کاست که ده سال ترند سوژه های جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24525" target="_blank">📅 12:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24524">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=DO72w7Nu1OzOumODPyy9ZqOYRfAUig0B2C3X3OofzD9nq5KuYtVK_M-ZxVAM7-Em5-tU-ktwJAbnGaRj7OqZoPEohsft7LOlo0Nqk5yRpRhBjaxjc9rp3Yea6BfI6Zdwd8AeDFeOEXR7AB76NO2sXRheVn1Vhf1oRCHobuurPkz2bf1rD-XWNWP2sD7m-0Mm3p5iuBv3hxvLYDq_O-JX407Xp4ZRsmz-RzG223JyawMQ7yUZHuN_VBYaajxuWGHlijFWBPGOA_noEMk_6fOnMyC52z_QbkEcE1_fhzbWVUgZlVWpipFzYg2ABFLRHvw0LnVm8X9WUH8zBPlhNzm9VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=DO72w7Nu1OzOumODPyy9ZqOYRfAUig0B2C3X3OofzD9nq5KuYtVK_M-ZxVAM7-Em5-tU-ktwJAbnGaRj7OqZoPEohsft7LOlo0Nqk5yRpRhBjaxjc9rp3Yea6BfI6Zdwd8AeDFeOEXR7AB76NO2sXRheVn1Vhf1oRCHobuurPkz2bf1rD-XWNWP2sD7m-0Mm3p5iuBv3hxvLYDq_O-JX407Xp4ZRsmz-RzG223JyawMQ7yUZHuN_VBYaajxuWGHlijFWBPGOA_noEMk_6fOnMyC52z_QbkEcE1_fhzbWVUgZlVWpipFzYg2ABFLRHvw0LnVm8X9WUH8zBPlhNzm9VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
وضعیت نهایی گروه های دوازده گانه جام جهانی بعد از اتمام دور گروهی+ جدول تیم‌های برتر سوم جام جهانی 2026 در پایان بازی های مرحله گروهی این‌مسابقات‌فوق‌العاده جذاب
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24524" target="_blank">📅 12:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24523">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agm7aCLOs4hyv_Unh2Harf2pQJ5zxdkBAvPO6O17xN6xuyp0ujhyGrb1DkDptV78s-1l-t5RFii0LUivhfidP2LjBnUDK0O9gaSfPgvRH2TlTsSLIURN1CwV9zuNpmMt_U_PujdCD1LNqYvZqL-gPk91-LppNI2ToqH9GKEY-1R8abt-0A3wlQJgzfOYs1VR38Cx8AsG9Q_qsEB0gZLHME8NMhKvcZ6kq18zkcXhLGpU3gapIRaO-udGmNXSnby7u6WxHjMQDvpvrShMHX2WE5ZhTRVl3BZpB9XcSYnQlmUPmGHNuxlbj1ox4_dCxewYDy_wzIN0kQqyXhdCIGSCow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛علیرضا بیرانوند به‌مدیران‌دوباشگاه تراکتور و استقلال اعلام کرده دو هفته‌به‌او فرصت بدهند تاتصمیم نهایی خود را برای فصل بعد بگیرد. بیرو هم از تراکتور پیشنهاد تمدید گرفته هم از استقلال پیشنهاد سه ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24523" target="_blank">📅 12:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24522">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKcfWuNwHLAHqVZ47YcUI4Vxmpx_zQg6RyIhT6_p8K2rmoxUwwiX3zexleU60UZ4jD7ZJknNJTHYp39KvLT9Evqfbq6rTBkTDI2hJhUKvl7t5vyUOtdss54aESIWQ2Xa9r6QpgGOgWiW3IGQjw5Vedw80hcKTyMdjY-ZP84VlAhYx1VdcozhF8KEVmKl_v-DWoxo-78kuHa5_J6V_SBFM0lg-cx-DCmpYcFkG1y4Ih-76ptvpo3MVP2GvvDClW8cImprCkCuLbKqfeBfwgdLJxv19Duo4tK4TvaKIzAPZyiR8g9Yzp7QsYkhJ-OXbxCCkIgzzSNi23QNrYR1tHodsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خود درگیری‌مدافع‌مسن تیم‌ملی بعدِ بازی با کیپ ورد؛ خلیل‌زاده بعد از اون صحبت‌های گوهربارش در تمرین تیم ملی خطاب به پزشکیان حالا بعد از برد دیشب انواع اقسام توهین‌هارو به مردم کرده.
‼️
حالا این‌کیپ‌وردبود که بزور بردین. فکر کنم اگه تو جام جهانی یه برد بیارن…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24522" target="_blank">📅 11:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24521">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftHmcY3TNGVsiB93d1AvhIKspGbUwKn9Rbpb61x-TyKjqVG-qU_tdjRVcj71zmfqy94wBYg5El-rVLpU5j_TwhB33Yc805pFQlhmgRJMmlW3WgRSotqfYYptYtjmKTFnSQLgEG5HhAjHC4a22uLSlD3O5sLoW-VqOPxJm_DmWNBuwmii43jPSN4bCyHpXvLcUWR03jszawFe2y9qyuQcqHB3zGlfi7NqxxUMFOUTsifNaO8w_SGnEjSCwLoB_MxNFSWrIBPC3TW20icGZVsBftLMZhHsNcDFOsW7n7ChPZe6DL6UxDv4CfV4PIyCzfI09fSCObuasrxdmh08SCo2PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#فوری #اختصاصی_پرشیانا؛قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24521" target="_blank">📅 11:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24520">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‼️
خوشحالی بازیکنان تیم ایران ازگل دقیقه 90+3 الجزایز به اتریش قبل از گل مساوی اتریشی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24520" target="_blank">📅 11:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24519">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/me7nHM-5qbDJ4DVPMGr1XlpSNBCNKzboSPDrdGt2StaORxJC3AP5ha_5lhOBgOEhfs7dII1OmI-T_ksJvd8bEQ2W7kamVtHvNvakbeIJuFJBWWs38K8fKK31aAW7EJdZ309vT7IOApRR9_LN_B0uyF_SmqAQTX2fIVzGv8geFBcK1GUt__N8RTD-_c7i5vEhnJkWyTQ19bMT73_m2QiZfflNc0ArqxT5LiVNEa9x1-iMc4jVyL0r0ChFnqdvrh2LjkrkY5R4fF7VVrck35G1ZaPOJBiYmWBEc3TUJCFeara4cW7NqNMEV0px9h4xpTpRiXu6q44_DaA5Q1oJ3JJlCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
‏3 قهرمانی‌پیاپی‌جام ملت‌های آسیا؛ ‏صعود بعنوان تنها نماینده‌آسیا و اقیانوسیه به‌جمع 16 تیم برتر جام جهانی؛ ‏صعود به‌جمع‌هشت تیم المپیک؛ ‏صعود به سه المپیک پیاپی؛ ‏بهترین نسل تاریخ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24519" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24518">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=EO7wGbJVI-eYdWvYyAX3-xryJ_uJpXNVUdrmrvwE5CRk-l3aa7lVN0I8MW3bWuwt4IgdLhUiLfiAi-WMvsFs9mKzNHV9lp_jdZ-ixyXo_JajYFhuDyy2mKQVOwrCO3YGJhqKFAt0wzrwReh1lMPTcCBMi1tR-67QppieFo8vDXa8_m_Pg4FDBZByKOE64lI8CK44boPMc5-dazjgCo3VBQsxheiGq0NW-rgrSYGJ1rQdL4uwb-alNSDZ38Y8u4fFGCREAzfcB0kOwnMCrIPJ_PT0WKri7Nn5zySRu2OM7vqAy1Gju-nIHOF_A31aVSPO9uEYbM6NLassQqljehr1NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=EO7wGbJVI-eYdWvYyAX3-xryJ_uJpXNVUdrmrvwE5CRk-l3aa7lVN0I8MW3bWuwt4IgdLhUiLfiAi-WMvsFs9mKzNHV9lp_jdZ-ixyXo_JajYFhuDyy2mKQVOwrCO3YGJhqKFAt0wzrwReh1lMPTcCBMi1tR-67QppieFo8vDXa8_m_Pg4FDBZByKOE64lI8CK44boPMc5-dazjgCo3VBQsxheiGq0NW-rgrSYGJ1rQdL4uwb-alNSDZ38Y8u4fFGCREAzfcB0kOwnMCrIPJ_PT0WKri7Nn5zySRu2OM7vqAy1Gju-nIHOF_A31aVSPO9uEYbM6NLassQqljehr1NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌میم‌از بازی و تساوی پرگل تیم‌های الجزایر - اتریش که توسط پیج‌های خارجی ساخته شده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24518" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24517">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">چرااین‌روزهاسایت
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالات
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24517" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24516">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=EUy_A8yUuV9-IeLnNIr0JAmMB6L7zPpOOwn1M9q7RpA5Zmn0i4Pm_t2Coez-oQGo-SeartJExkxNo2ZYW0HRRsLxA_CVm6FODnYYz0Kn9h4ccPJOKzfELV4866jNAfEhA2-SJQTVVmoeTggQHfYurzom4ii_Q5U9HBMIKTUjuwfJ7A9g5hwl8xJ-emRlEgwDb0S0TYqlLmPD4T763AFYxCqTL-It97qjrQyx0AlrBXOg6BCBwxs2iC5xf7KZIIlBQwqIeGzukla4vzK2FYR70y2QMjcW4-ZukGvrdm931bOd5NGRu_QI811eU9INm1FI5_qWLRi8Eu0iJvOn-9k-iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=EUy_A8yUuV9-IeLnNIr0JAmMB6L7zPpOOwn1M9q7RpA5Zmn0i4Pm_t2Coez-oQGo-SeartJExkxNo2ZYW0HRRsLxA_CVm6FODnYYz0Kn9h4ccPJOKzfELV4866jNAfEhA2-SJQTVVmoeTggQHfYurzom4ii_Q5U9HBMIKTUjuwfJ7A9g5hwl8xJ-emRlEgwDb0S0TYqlLmPD4T763AFYxCqTL-It97qjrQyx0AlrBXOg6BCBwxs2iC5xf7KZIIlBQwqIeGzukla4vzK2FYR70y2QMjcW4-ZukGvrdm931bOd5NGRu_QI811eU9INm1FI5_qWLRi8Eu0iJvOn-9k-iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ژنرال به زودی بعد برگشتن به ایران راجب بازی‌هاشون و حذف زودهنگام از جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24516" target="_blank">📅 10:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24515">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=XHmlHqBHUZjGYl0-eiXozYsXxtW9k18zWSir_ItHHKdmbaQC8GGOak3n5MTlzBGK31a2UOzMPVMre3faCpPp-qcjT-O2TVCDd1VeMmB6INo5R0FM2DoClkJEiSZkCczmxYWZxJfdTSwvtX-ozEK_ZVuD1UoHGbv1GqvW9yabGQorcXwSrOqZxUhmeOvMa-4ShCp8smCGByabFqRczCkpgQ2ymAgQ88sLUi338vCDp-7-_TaS5TrC7nWYUI9auguhdCXxHg5m9pRTTJGRYhdeaxyunJD776PJh6Er24Ia1_NqFYe23KpakWL-UXqqM3WqSDnJzXQK0iBkB349jQ5RrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=XHmlHqBHUZjGYl0-eiXozYsXxtW9k18zWSir_ItHHKdmbaQC8GGOak3n5MTlzBGK31a2UOzMPVMre3faCpPp-qcjT-O2TVCDd1VeMmB6INo5R0FM2DoClkJEiSZkCczmxYWZxJfdTSwvtX-ozEK_ZVuD1UoHGbv1GqvW9yabGQorcXwSrOqZxUhmeOvMa-4ShCp8smCGByabFqRczCkpgQ2ymAgQ88sLUi338vCDp-7-_TaS5TrC7nWYUI9auguhdCXxHg5m9pRTTJGRYhdeaxyunJD776PJh6Er24Ia1_NqFYe23KpakWL-UXqqM3WqSDnJzXQK0iBkB349jQ5RrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
باحذف‌قطعی‌ایران از جام جهانی و بازگشت آن‌ها ظرف 24 ساعت آینده به کشور منتظر اخبار جذاب لحظه‌ای پرشیانا درباره نقل و انتقالات باشید.
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24515" target="_blank">📅 10:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24514">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGC8h-fWsngWoL6CBuBkUX-HNFb_jtrPSSCilz5g3mHQca7Fb4xrOfdwnpLkOjceAq9sP4nDmPmyTaqMedCzcALOiObwsUYhTHajizQd8NjjRczDGy6q5KAFZQxOcH7ci9OqoRhbwmHd9tZNFH8RVImay5ntj-_LrCwcSzboHoO-urVZH-H2SfgsLcGn1KH4mKWQuyftMiSnGiBLT4WgTALZegR_TiBurUWA4xWYwnqzi2WuLPQxFg5v5qvsAMTy64oOFWSH2C06_6RwgUn21bx1rTqUtynW8JDzFpGKvX5-5ia8ohcvBoDkdSOMZy1Ggulv82sxC3eRrUnSjzoGLlQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGC8h-fWsngWoL6CBuBkUX-HNFb_jtrPSSCilz5g3mHQca7Fb4xrOfdwnpLkOjceAq9sP4nDmPmyTaqMedCzcALOiObwsUYhTHajizQd8NjjRczDGy6q5KAFZQxOcH7ci9OqoRhbwmHd9tZNFH8RVImay5ntj-_LrCwcSzboHoO-urVZH-H2SfgsLcGn1KH4mKWQuyftMiSnGiBLT4WgTALZegR_TiBurUWA4xWYwnqzi2WuLPQxFg5v5qvsAMTy64oOFWSH2C06_6RwgUn21bx1rTqUtynW8JDzFpGKvX5-5ia8ohcvBoDkdSOMZy1Ggulv82sxC3eRrUnSjzoGLlQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ مجری بی‌ریخت و مفت‌خور صداوسیما که بیس چارساعته خدا گوه‌خوری میکرد اینجوری روی آنتن‌زنده‌شبکه‌دو صداوسیما ضایع شد. می‌ثاقی هم که کلا فشاری شده بود گفته بود دو تیم بت زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24514" target="_blank">📅 10:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24512">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNtHuviScNYCir3aOtEs3SbQMslpzJjIB2mjyfIud2Ds6KhyqD95Fw8ZO1ulFuK2omVo1GJGxyh4JnHWJI9BeEAM33e1ME7YGmT5_2IQrxLwyi0SQojvGlz57VEjO555smOgYY7YVoTtSH4Dh-27LonFGkFfdJMrOsKIJ9_nCPDsctxfNYjbsMPYaTOH45zxXHeviy-3ldDhODJjjGEfsjfiWsBuoHTNxqxtBPtUkilD8HS8_xlBDeTlphkx5tuW6_EAY4s1puRoMe5UTOQ16tjKl-_PuNdmjlmSMPjs-KXzB9XaM9eLNt5iLPJwitPKH443ZWmhEMvXEJ6-WGS3yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24512" target="_blank">📅 09:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24511">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzE0dyRbpWjHkSOq6xZHiL25vWxi19o4NPlH6OWwoTNAju9OfDARkNpiV9nPgHVtzXDu8aDTs6pqdUhR3qo0IPmhi71Bnu7aY3kFquHCKHHcG9p6K7fLXHsvI9Ld4ADcYdNKg1EqRxfSm-HH-aW3o4TDPbN6x9QqXsetnL9uXfzxRWG-snhLzfIu7YcOL6KbWwu4cVzLbQH_Q6gesx_6_MdcRGMJD5FWlvw4c1O0EKhRt7x3qkqAoRuUb8aAfYeGkjTycu5pctAueZ90R_LprKetaYGZiSLylo1Ibx1o3UbNECeoAwo4Q7F_6NzddH_hJO3RbYH1GcLgF4Be3PsCww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛
این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24511" target="_blank">📅 09:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24509">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jQAaHW1z6SmWSNol4JHHg3QgAyzmTqMwlYHjeOYkXexdL4flr98IBScf8jKKvrmkCE_sKxfzjUf_P5iv4vFYsKbeDNLMcBMk8zMmgTJcnIjqFEjvf044cylsVuhvqSnX-bitA8Ac2hhXO9jP1Ir6o76dYFlFNrmy-8nnR8gPpGh7e0rXtzX-XxktAUPMUMyBUldSrqounab-WnD5TcKy9m6GOA_xr0p_B8PfSYbLUiIqUlB48ap3eEM6tRG0z9LRtEWd6e3D6wUUIxodPMzrWd5qOspCRhOxd7f89Och7IGZUJAuS5iBqt0iZA1IBF5lEm8h4dVkMXIkeyWr552xtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vc_bJGdNHOsHQLCbTAUi3YifP-KMxSYXrldhVQQise8UQn_evjjXeCxZQBMjGYeOKPKBY1u1fqY04R8kyrwJHlqFzQTQjwRMYW3tpQPS8iyBKXXtUhoRgbbMvuL-bpG7B6qLJbMuD5o1dDyHAr7m2WeEfVTsIhcQz6Q9tEvEPgQlFmyuqq3pK60VwvL1tBI9pQM8sbzXhi0fdgtF_gjtEXEZ96rJDapTvbc9Ua14j4hyiljKOAgQowjPkzxRObFA_UbU2u_F4M4fEWNcO-pLiLYz9GtnDdMOWjpcDWEEP-WIIBv_M9L-Pkt6tRCM4rFphItHw4bOMORGO4NuOR8dCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24509" target="_blank">📅 09:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24508">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛
گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24508" target="_blank">📅 09:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24507">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24507" target="_blank">📅 09:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24506">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=Lc1wqjJmaEj0b2YRuY3Fq3ndMjOiMCfKNcGlUfVmydmcMrdZu7vU-mu6pbh_KNqDv4HNqk6x1mKakud9eZuZ-FJsmyqHYPPeGZyl0Zqx2zMipu2qW_MHbAKlRw2mitdaUcyjulp6Ivq6rRgI8ixlPyGLPvam-C9fsMn9LOELFbIVxrBUeodbNWrcIgkxUy9aRuG0vz81-dN5CAmUF4TpXR2sBSVp_e7SmInyCw0dSZ5iTH2bMlwciknBaYa8I80NUunDL5c8CNlHxdaqhjG9a0daTVfZVj2_JQBXAd9u9FBb9DO9SjIo_3m4dMh5uDuaqyXDE70VXBosb97IA4DlGHxcOSPuNgzPjE0WJHMBt0SZR9r_L6-YqhMknrrmGpM_DSfWFRLEctmr9Psq27q6R8DHcsf1jsu7ewWvKQLer3PBjYTSIJ_dWpzARazH-8Ewd7UxejWquHME_v_ExfatpdnOfOsg5YD7Kcx5Ys26yic7LSwzR9Q5K4zpqa3VCYpRj3MjmOEjU1zu7W0oTKalAV5Yn5eN950qOhcTCR7cYwrY-JdlHVWZXSIIU-EAJiDhmo9lYd1ODUbLVSm33NIudgYAhquCeC4t4GYvZ6IIe2QjlqIYRBQTMZjJ3B41u41hX2TQY6u8xgLTDjKP4xIAjFZxkx3I1Qw8lVBcbBENMhU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=Lc1wqjJmaEj0b2YRuY3Fq3ndMjOiMCfKNcGlUfVmydmcMrdZu7vU-mu6pbh_KNqDv4HNqk6x1mKakud9eZuZ-FJsmyqHYPPeGZyl0Zqx2zMipu2qW_MHbAKlRw2mitdaUcyjulp6Ivq6rRgI8ixlPyGLPvam-C9fsMn9LOELFbIVxrBUeodbNWrcIgkxUy9aRuG0vz81-dN5CAmUF4TpXR2sBSVp_e7SmInyCw0dSZ5iTH2bMlwciknBaYa8I80NUunDL5c8CNlHxdaqhjG9a0daTVfZVj2_JQBXAd9u9FBb9DO9SjIo_3m4dMh5uDuaqyXDE70VXBosb97IA4DlGHxcOSPuNgzPjE0WJHMBt0SZR9r_L6-YqhMknrrmGpM_DSfWFRLEctmr9Psq27q6R8DHcsf1jsu7ewWvKQLer3PBjYTSIJ_dWpzARazH-8Ewd7UxejWquHME_v_ExfatpdnOfOsg5YD7Kcx5Ys26yic7LSwzR9Q5K4zpqa3VCYpRj3MjmOEjU1zu7W0oTKalAV5Yn5eN950qOhcTCR7cYwrY-JdlHVWZXSIIU-EAJiDhmo9lYd1ODUbLVSm33NIudgYAhquCeC4t4GYvZ6IIe2QjlqIYRBQTMZjJ3B41u41hX2TQY6u8xgLTDjKP4xIAjFZxkx3I1Qw8lVBcbBENMhU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24506" target="_blank">📅 09:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24505">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5znC4LLbj5lmxvTaXq77lHmC03v_xoFTCwyhpMD04Q4N6cBMbbikHsqqCBIGk6l7l_f5UfnUFXWOYXdLDZABee1ybLfHaFSjhb2DdCcO71r-58MKwH8jIhq_AfNH_Rb_uFaU0BHH74IoYwj2NVv-NLIaKnAVr0x7H9Es80pb_WnwPNkENJ1NCjg1GqQYeCq8GXF3AF7HDqwzfEa0q0CV1R9IHwSPM7fGyUfV_0iNK6LKwwMv-2qYehdfeuWYREbbBqCDZCqLCKXCc0Eo_RHa7c7IpAj5WA7TI7la-AJvWOBxMJQuYH3n9DVr79griwHczOvi0_B8IOO11JyDkv6zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24505" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24504">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=Eh7uHXsHmx_BAaeyfc72sn1tCVII36SF64qWDusD0iAAI97mlX0aeyWdQML6ywzVyLnAQq-4aIDUkv7ukqCAn3B0IydNgLwQb0hu9Q-EaVTrwzM5Pd6p5HZ66MeEKRPm8HWTmRlazkIufM6WLR-jn6P4I3h3eGjARgdB9cwl4osgyqNrPQLTgUTu3b2xbUM4Gdi3cGce8lv56imdIGXARuskwh0fJsUIAM6qxViGSn1xP5crVNSjFolQqY4mrZL1n9BGgjNQ9VyZrimhbebITDnhDhntMoZH9IBGCgTdNeN5XeVZgUBSUNeL090NpXK4uvBmSJmEF_1pIJvS6WyuIjYsPs_Gn_9JgATHNWWdh6cjJi3IFMRUZt7yGSZwXCLFh0v9NoZyYFKazzGw8DWRXEc-D5GPAKqdDQKM0kAbTT2dnG9COYBrnFt5KC8fFdMIpAweUX6tVK-sowFChET4DccrlUrWaBrq1eNlNzLanpt_8pbv0FJ9bDykXEvEihe7XMm0qSQzr8oo-24D_LdiXrb_jK7t2Y_DVrwNndyDKFK-QDu8tF6MpzS7obcnM9ROz1Lc9l_e607L4j5bNQ6EnwDNfaDXYfadszO63ky5PksVSPE0lnOjipEzbkn9ynVb_Y6v69GSbsaESHeFsHZEn2H75OvpAoug8PJszPkDNL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=Eh7uHXsHmx_BAaeyfc72sn1tCVII36SF64qWDusD0iAAI97mlX0aeyWdQML6ywzVyLnAQq-4aIDUkv7ukqCAn3B0IydNgLwQb0hu9Q-EaVTrwzM5Pd6p5HZ66MeEKRPm8HWTmRlazkIufM6WLR-jn6P4I3h3eGjARgdB9cwl4osgyqNrPQLTgUTu3b2xbUM4Gdi3cGce8lv56imdIGXARuskwh0fJsUIAM6qxViGSn1xP5crVNSjFolQqY4mrZL1n9BGgjNQ9VyZrimhbebITDnhDhntMoZH9IBGCgTdNeN5XeVZgUBSUNeL090NpXK4uvBmSJmEF_1pIJvS6WyuIjYsPs_Gn_9JgATHNWWdh6cjJi3IFMRUZt7yGSZwXCLFh0v9NoZyYFKazzGw8DWRXEc-D5GPAKqdDQKM0kAbTT2dnG9COYBrnFt5KC8fFdMIpAweUX6tVK-sowFChET4DccrlUrWaBrq1eNlNzLanpt_8pbv0FJ9bDykXEvEihe7XMm0qSQzr8oo-24D_LdiXrb_jK7t2Y_DVrwNndyDKFK-QDu8tF6MpzS7obcnM9ROz1Lc9l_e607L4j5bNQ6EnwDNfaDXYfadszO63ky5PksVSPE0lnOjipEzbkn9ynVb_Y6v69GSbsaESHeFsHZEn2H75OvpAoug8PJszPkDNL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24504" target="_blank">📅 06:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24503">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGs1sv3J1Zkw2pXV-aNGNKIVLDHAKybd-6NG_6eyDGa2qTAabJbZ1zEnBJw76UJ-rggKPEhbqE-oYvrHbcdOJwXZ42ZXbfkkAYfrhg49QY3UOPcMyTQmxJSMArV7nsT3-V5JgeKota-XKRiMGVSt-9TvcRxmbkaZuVFZCv4gSz7Tncg1JXJNA2pY8LdPcXru8iOaU9NOJotCk_BAkOB44jLU949N--HqWShzEPBmFb_H8GucEbhj2XEUtDquj9vmlCU7JDqzm34JLBxiNk5-Lew-nk2QUgcNyNf51MI1ofZv82lKLwze6c25tUPsAiEmT-qOgM3PgUeh6h2KRd8oyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24503" target="_blank">📅 05:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24500">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dUvackSAauuogwOrtcRV2mZWVVu-NS0N_DZc3Z81weRVqN__lCW_QQZWLkh5-ufBBdJH1KWLhP-FULVHLZDA7hHyc4AiTZmAz9kAB9ynEn4g32RdtRu2h4pmdWTJJY17S0N01LOw-rlU0DZbl9-w1brDIji_JZmNTjLjuAtjfc-N6ZHx1YbgG7cVfKNG6gAfIAvS_1i-CIbJQbLFzb2dGsyyUiKKOsv0afFBXndQxpxQEbwDl5TnNyVEE-_MO2Q8TDazjzoAvBW_M2vUjlKdmvp7JWZ9VxrUdVatCzpYaUq3BVWBMpMWgUKOQWJe8b563_vZ9A_JaVzJSVbF6L4tsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Odunm5sXpZ_pTSZ6ESoh1b49rs1HklfPOT1SFF7JiTgba1MZvnHes3Yv3z2Z9O9uvMiflx6nhg4QViV_kAnG4mO6ZWhmfypxtiyhG4EjAjui8DP3wgQJqkHW7-nKW54pLLG5pSR9-DhaPjrGj3VlgALb1NfJhlF_hJYQl5t2uKdJHZBUZEnarpMrVDcn8PjD72s0OPCQMVLajozP0ffRmAHlPsvTWBDeHGz12JkMH1j89jDBSOx5sqyCMvnttK3yRUrYGOvnZHnozeuWTxqLmgJ4egkEgPkigRgcSPurMHT46ufy8moB5JCsMuKTgGcnGhoAQvecMjMwUZlDv7w8Yg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی کنسله. این دو تیم دیگه تا فینال به هم نمیخورن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24500" target="_blank">📅 05:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24499">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oO_TlyBf0pNnQzK44t50WAWPlil3fdSKcPTU9GmeZ_9XRzHGWRaeksYXMyu8_XiJYmlPnDmn35j9KjaQMXvhTAG_KfBC5PNiiSYPOyBItLBwgasABB7_uV8kYaywzxBLzXSxDb1JAluL58zJpNxof8XyDHe6S_KV86qt5FazBbcG9NN2gi-VEkXu6W4qiaEI23yZOH-VjADsps0sBRJoKXFKPT_9zHwyMVMglOe0B8sjvlj3XT2BH2x7IEODDjDt7w51THhJk1B_EZUgHb5Xn5ETTkGdEDzc3Y4RF4HVoMPJlnh6ziinJG8qAdwBPNdDc5bxyMKhyco0YtsqtBz5Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ دراگان اسکوچیچ سرمربی جدید پرسپولیس قراره تا آخر هفته جاری لیست ورودی و خروجی سرخپوشان پایتخت برای فصل جدید رو به مدیریت بدهد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24499" target="_blank">📅 01:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24496">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24496" target="_blank">📅 00:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24495">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AL7pzfk1xyVexqZJFj9eStkGkLOOSGKTMIFFT11kt_2S5EcusfsNaBzgD72SAJolWaJcv6xIOw8tK-6lRp9fSQ0QVmK2cD7RLOsrHJkptpsuHAFwmXYZoxuwuLq3LSyi-Ept_Drzjq7752OBnMnhRUDTWNNBnu87utDIUgj-O-orazrxU3l1cw4Hmwd_PM3W7gl6KjfyRMRCemSVJ48aN-VwYfEcl9Orbaqd-ZYYLE4j5TwbqX9SUww54JGDHRfMbRL_JJQK6hV5SfxTEjcXWWufacaUDD8Sh_z8-J1swoF8UnNUnH75gYmwAspUFAjPcM2x4BuUZMW5GvsEBUnX1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24495" target="_blank">📅 00:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24494">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpavZCNjcwhHcTwwCXfwgV-RdvF3ZVcqjGLUGggIH5sjpy02_eDAoFvwdpH-SizVXsAlQlD1YgXgwzHBzqB5u4w93f2TKip1O-QeI9mi4BzsQxypwGs1zvIah5ta62iqWSAJ1B3LgV6SoTqGOMIjKVxZhOqHPQz2mdOXApSwWvKwf-LpLTPr2OW3UBN2OEgzkHXu-5qMuHBgCOJJgdWjum8W0B41MeB1O1rHJ0kGXI6e7y76JimNfNL1xcuZfVWWntkekQ7pexm0paD1Brc4OModwgDW5-WuJ5kRu_l7iuL8jx3q_kJS3JhORwoD-lE0wQ1UOZgaKYiq7_6mUNtfrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24494" target="_blank">📅 00:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24493">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApI_SgLev_oL8yqsrFjFCW5yelveOaPT1LGs2v6ruApRTCRffOMt49sVO7k6opd-GrmTrFJ3vLZtz-NIsNkH5maD3vPqvtIHx4uoURi-WGp338Ck5XFZg6q4LQKxscs9yzLixoF-V7SYjJQDQJ-CNRgtbpLbhPiEYjxX9xtX6AaAJi3W7wa3wa1gElNyfWHrjjgTvPG4vc7NUgVCeP0L7V-2GH-vfSeF9tHObO4SVeRrOIWyPElODtt0f7e0DV0jdoHZ7KSNAwDyMM_Mr9n2kYXNdndIKK5TaOKZmFXneZq0f-ofh3J8SU9A0BQ5nrX8kCVN-Z4mJd_mEDny5vMqHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت‌نزدیک‌به‌مدیریت‌استقلال به‌ما خبر داد که ظرف 72 ساعت‌آینده گابریل پین قرار داد خود را با باشگاه استقلال امضا خواهد کرد. همچنین به محض باز شدن‌پنجره‌تیم، چهار ستاره ایرانی رو به استقلال خواهد اورد و ممکنه که یه مهاجم خارجی نیز بیاره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24493" target="_blank">📅 00:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24492">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f250d91879.mp4?token=Sew96AwXJWAJq3LqhNdxHvFwrUhyRyqwrkmm54TrNYwhYx5cAbEdBsVCGrKD5QgGIkhnQO0zS0XeGasw9ek6XpvkAHdnMFxxbATrr8cXq8Yp67_wgmWLAZm0nYbJLAKdigL6-8Fv04qSMDh1OJWXM_m60Z8_nk-OMHVOAoUR7DCCN-NHA1pn64Cc1PiAvLNZLvtb9gwkMOw8eoUHYIFFUCoGR2dOivY6WktWLfiaGEEwWq17Y-u59WqN4sYerjQ6fUASof2oPY0YZAiYVKGNCtpuUGOHx816KNKfsV2PcrPvy6a3Ff7-ba0Lc7T48W6AT9JBRdOcy1mZapOgnBqyV5Bzp48S2WJBYGT_-xZ0-gb4xPNiVMUt-D9dEm2t4f1Fb_nYaP3S46OLbTSuBKQgfvQr-mD1wFnxoC8w7L8NBoERn-LMxXxAIkCNOZtnWoM78hmdGOQkRVwCtskoKyo8WS__GqDXiLoMWix1-4SXXTeyYoEyGQ6o5HTLRrAJy5a95OwVlLF-N-oJHIPcGBAbz54Wg4-ew3Zzuex4fJF38YoL3xK8cDJ9J4rYl0suVMQSLJnxpPrerlMg1TroPGUt3esnuq3z_DKEpwLpgcWdRbKV8kQ3saX2kpQQIVUe5gfQ7wNADQAcIBVrpagC68MknWWTw2wSmmoeVYfq7BjB5MI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f250d91879.mp4?token=Sew96AwXJWAJq3LqhNdxHvFwrUhyRyqwrkmm54TrNYwhYx5cAbEdBsVCGrKD5QgGIkhnQO0zS0XeGasw9ek6XpvkAHdnMFxxbATrr8cXq8Yp67_wgmWLAZm0nYbJLAKdigL6-8Fv04qSMDh1OJWXM_m60Z8_nk-OMHVOAoUR7DCCN-NHA1pn64Cc1PiAvLNZLvtb9gwkMOw8eoUHYIFFUCoGR2dOivY6WktWLfiaGEEwWq17Y-u59WqN4sYerjQ6fUASof2oPY0YZAiYVKGNCtpuUGOHx816KNKfsV2PcrPvy6a3Ff7-ba0Lc7T48W6AT9JBRdOcy1mZapOgnBqyV5Bzp48S2WJBYGT_-xZ0-gb4xPNiVMUt-D9dEm2t4f1Fb_nYaP3S46OLbTSuBKQgfvQr-mD1wFnxoC8w7L8NBoERn-LMxXxAIkCNOZtnWoM78hmdGOQkRVwCtskoKyo8WS__GqDXiLoMWix1-4SXXTeyYoEyGQ6o5HTLRrAJy5a95OwVlLF-N-oJHIPcGBAbz54Wg4-ew3Zzuex4fJF38YoL3xK8cDJ9J4rYl0suVMQSLJnxpPrerlMg1TroPGUt3esnuq3z_DKEpwLpgcWdRbKV8kQ3saX2kpQQIVUe5gfQ7wNADQAcIBVrpagC68MknWWTw2wSmmoeVYfq7BjB5MI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24492" target="_blank">📅 23:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24491">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQLXRM24Tn0YfhHoJ14PGkbUGp2aOwIOwM7dfXNCUBBuDJDL0IOvqijW7iKMs8VXYGgp1mXIHP9G0rNEoxI8srtFlPErdQo3CWM-vo0ZBw_jKnhDfPJAtvopf75rx2WaSUrJkEse0xyIYkd4F_xcu1fwyNu-ULtA9EhAKcHo-FKJzPUqx6REkq20cfLxIICK3GhbrHuCRuXs9XoOjTQOozgm42DHSYtVdyYr1815ek5_VS5nwa7ZAVdJTQoDmOsl65Z0a86vo_n9iZOJ2HAku2CCdm5A9fH4zccuHym2uhCRyFcGgCidtJjIHiICd7ooTDoU1IeSl5pV-V1R0Ez8UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
دوئل فوق‌العاده حساس دو تیم پرتغال و کلمبیا با قضاوت علیرضا فغانی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24491" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24490">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIfQH3sGkH8ZnFqb0MfcweEKK84E-TqsofuWDF02H3Cx-t_F2ouczdgj8njQjiDRm-aD5DP_lAIe9QDH6bDhdw31G03ljWuk9w-OqYdcdHM0vpymEOsAh3063QQSJuPene1xriBsgEhuwFYBKfiPnym_vEWv7vc7QORvPCf67um-SLHONAYQCkBdRpFijaszhuzZ9gF7DHJVImPxa7gtr5dMt645Jw4u5kJp37v6MQoaGef7LbXMIUQJqoho-40-b0YeK-V8g5lLeJjbrDPKZ2qz2UCvFJgVXhv25UCFIgupWRnYd2hYz96oxdCVDrFSm0gxxgnwTPAyi48uJ8wVgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
ازنمایش ناامیدکننده یاران والورده تا تقسیم امتیازات در جدال ایران و مصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24490" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24489">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_GVvbGLGBRGsdOhEQXX4_LFSsob7F41dCcVJM8rvtU-6KnVDlL4IMek6CJUHzdFv4f0ZsxcXGHE8pKxcDoZyZYP2_km_zwwb0j8hEWo4e568kUQSgu_3XUi2MkBtluhRJ-ziKOn-3eVW-fxEQXsLwRg5afWcOCEw5a6OAzdF4XnTX3ofLUhjVB3_tbS95HbX1qcIYTcvcb9GkuLhxzf5xjG1_cRWK6UKwU06taaSfVKcPVUdQPYIcIHEnOoUL2fw4c-fkJlpvxV3ruczy1r3xyNP6A-sFQbBxh4L2Cxys67FyCanBftWnzwce0dQOjcCnG1ewPqoIvyIu3QT2p5xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
هنوز چند ساعت نفس‌گیر دیگر تا مشخص شدن سرنوشت صعود ایران باقی مانده…
‏
🇮🇷
ایران برای صعود به مرحله حذفی تنها به یکی از این نتایج نیاز دارد:
‏
✅
🇬🇭
غنا،
🇭🇷
کرواسی را شکست دهد.
‏
✅
🇦🇹
اتریش و
🇩🇿
الجزایر مساوی نکنند.
‏
✅
🇨🇩
کنگو نتواند
🇺🇿
ازبکستان را شکست دهد.
‏
🔥
🇮🇷
شانس صعود ایران: بیش از ۸۰٪
‏
📅
تمام این مسابقات روز ۷ تیر برگزار خواهد شد.
‏
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
‏با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽
👉
betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24489" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24488">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=JktjAhuF7h785REDxblFHgDplvsOBopNsfLNQU4rILn_Lg6QNJ3XmXEe59lV1LIMQCTN4ilge3TmgYEc7D-ZZoIS9RBBHewfLjARlDx3QjtlB86CIHAqUeXUhDn0EUQJpvlcOWbVeyhLZGn4538CFGXjUPuH3l7J7WkKAp7by-NiuLKONu4bz8rmcaO5nDsNw_Rk_8u06JUdN1JrGAHMsmnk2llaeu_zDS3ahcmYj11WguMasb9TK7z6cRmzWTi_SA2hn-c_-bp1181GwUCvsQhq-SPLH8h1-TTyeWtMbIa57p28xKtpTnvp5xlXoPZ24EWyuuV9Et7yyNV8ZzXZ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=JktjAhuF7h785REDxblFHgDplvsOBopNsfLNQU4rILn_Lg6QNJ3XmXEe59lV1LIMQCTN4ilge3TmgYEc7D-ZZoIS9RBBHewfLjARlDx3QjtlB86CIHAqUeXUhDn0EUQJpvlcOWbVeyhLZGn4538CFGXjUPuH3l7J7WkKAp7by-NiuLKONu4bz8rmcaO5nDsNw_Rk_8u06JUdN1JrGAHMsmnk2llaeu_zDS3ahcmYj11WguMasb9TK7z6cRmzWTi_SA2hn-c_-bp1181GwUCvsQhq-SPLH8h1-TTyeWtMbIa57p28xKtpTnvp5xlXoPZ24EWyuuV9Et7yyNV8ZzXZ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیویی‌متفاوت‌ازگل رامین‌رضاییان به مصر؛
جدا از ضربه دیدنی و زاویه بسته رضاییان به شوت زاویه دار میلاد محمدی با پای راست توجه کنید که دروازه‌بان آماده مصری ها رو مجبور به دفع آن کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24488" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24487">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oar-6fhlMPZxvnRE-M3o8IY2bJTezfOj-UPvIXDHXGJ065ewRbo9qYOre6Wk1E7jEux2lveNmG2JM9EdTsD9BXoE7UgRWTgVdI9onsbBRoUF0y2kZMZPb5Hk-OabeRB1Lb-a9iQVSBVPLaYKKZBpz7s215MqbHgL7dqT1TMx_wLNJv0qu6vfwTS7Sh6YLyH2NFelY4FYC5pkjQJVjdcP1yMba9WYyuHwKma0pn_WOuk-Q88SRNHoI8tPB99tLgCLCLs49luRbg_R7BM4UreLPpJP_SbNKlZc5dxyVcxOmgNzF3U-XwBxybuvRb4ok6RSEGpfPGudjX9z7jbyAPfhSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24487" target="_blank">📅 23:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24486">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJywuouLWox1z5HxMXqRdrHr4Bs3h0TTs8aryqUL3a7j6yqwpOJOikLoKRaZtTyLz9hOt0FcGQlvWvYbBjCQlW6vxr6746i7KOle-A8y797XruGxRjC0D_GcGQ9-1vEN7Y0CKDOTs9YkFbIWJ_VnDETYn9xg3U8u1Hr0_aOhBBtllEdQxe5TNzRlim0APSJ6c-ARIxj8mToIKtDlnnMhnaTrBGTVmoGhm84EJA26LgOP_ZS6FkCojvxSpBMR5QEAQLtMQgPWIEJRHZOsTAIto6BYTBBD3tC97EVPYCrwAlr60KBt_7thh26Okq6DlIUp3iBnpNR1tQFD37JH791CUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بعدازبازگشت‌زودهنگام‌نساجی به لیگ‌برتر؛
حالا درفاصله سه‌هفته تاپایان‌لیگ صعود باشگاه مس شهر بابک به لیگ‌برتر نیز قطعی‌شد. اگه جدول همینجوری بمونه صنعت‌نفت آبادان در دیداری پلی آف به مصاف مس میره و برنده اون بازی لیگ برتری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24486" target="_blank">📅 22:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24485">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyXfVAlpLEYomPDe8QyHW9IM5DiAfVvXBWZ05VjJq8XpJPM41Ktogp4GwSsuhK9GQIYL-4NNlo7bdwo1gH0f2rmXCGL9hSONsRQ5-EVripYEgdnbCAB0qKoK50_2ejaZRiPI-0qulkCopHJF_pATic9xWM8kgyJMfVTkiwEDR4y-62QmiARF8Zza5hW_2AiRJA_M8nN7ILjUt0Uv0TsUuuLcbH92fwgTvNPLZnzlAM9sG58jKWKpP9T2SJKC1Sj96ZREJh_Eew_q3_BI9wzptXZwQO5q0qyupz3Kg6lBadEePQNDnhZcfCdY9Tvvv02GpOCJOPPl11g-7gbvTpeBDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24485" target="_blank">📅 22:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24484">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfH5GYNPQHBag569TdCZGgbZ8P7uwJu5XcQw-1xHmJXJkGRXom4pIn8YFVp7RJbiNPZi9cWzldDFOmNuRF6i2-EK9Ib1IMyRDNjiBThiUAs3YvP8UJSexwR3gQGSlCp3wQK-gi5bSCAoqQHRFb8FxJ-IFlsniGMRzudoZRHd5WgoVi0J8q8mCa90AdFJw_DXOxFJTez7v06i_16Y7bvSVgM88i2fBKyVB13B1xXC8PQ_Hx3p6fU8CKeItEgAXQJmWDy9sc6Zx4FkN55sLrgF1pjZT-bm-WDCf_Quul1CAr42zXmhkNuy8v-J36EoPmX_7fFhY2CWHk_JUmD17HBxrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛
یه زن‌وشوهر جوان تو شهر قرچک که تازه هم ازدواج‌کرده‌بودن بخاطر اینکه زنه طرفدار تیم ایران در جام جهانی 2026 آمریکا بوده و شوهره دوس داشته که تیم قلعه نویی ببازه از شوهرش جدا شده و گفته دیگه خوشم نمیاد باهاش زندگی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24484" target="_blank">📅 21:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24483">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEe1Sd-deQl9xmL4cB_9Hwept9HGDhw0FNIk0yH_gXIXS1rpA9gI1hca3xuqig5as9yITy4x0lEHHdq-Q91zLpKbb_v84bziR_aagN-PE2LyddauxobFsjSynodvhykoJ8eSFgCwQgTgNByPpv74zuOgSDgFjzvn5pfmqaHg7CV_lr2D-uIeNYdZpQN73GhBkdseT7CgB7JHvcz6N-UGM9fntK6PFD8RVvSL7Rxhgp5kcCaAVEQhFuF-6FbpEqr_uJawVSKX8rfLMZ4GXWEvFqmJ9tkETO48iY9y3LaJfNwkZv2GTbvRksrSXHTwoRcX4rjHFbeIIKCqA0mYB_KzQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇨🇦
بااعلام‌فلورین پلتنبرگ
: بایرن مونیخ میخواد در این پنجره الفونسو دیویس مدافع چپ 25 ساله خود را بفروشه و جدایی او از بایرن قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24483" target="_blank">📅 21:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24481">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIPlaNmiJxTm2kVuGGSGvRRayf1bTzWpxxOqyldVbAXWp3tJGr1-qgm6MuH-HrWL2TMBp9HqNh8uQYXsiuqzlzPwuGrNeJfU6CtyP9fjLmsLT8LtgtnytYfZstlnJNxuDBAK2tCK5_kkmGYjUObtwcwi5ZZi-uWWlfqoVWSZNMwXFWiR03s8iura-yqSi3tCbCgEg0kvJlwV4U_M0dhQ5m12NdcuIxxuOyvLXYHyUIrGJBoV--YP0M3uYZB45T1GDGq1xTFME5UvpxEZgInaRa-QVD7tQs2_OvQcDEq-Mk0fMvFCQlY7Cq0sy-bnMwdwJ5W8CkzFC71qJWSKxOpLHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24481" target="_blank">📅 21:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24480">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NO9_95U8d1lCqqOCIK6khgFpmmFNZcXsJdn5UgWXQgmdnKf60zzVpcpxSxdCvIQJFOUUTAbnE-s7AoS5tMgrbIS5rfxLmEZRgnGciSex5I9Ic932Jofzdyzq_7d7XvGnUoYAbT7COnjAebKYJj_YBCwwXtSNvBZdW15DP0o4QvgSX_BSS5kVanUQFkiX2zI4TJ8a2ljxqI0LhFtdU2P71bohdWif4Z3wAIt59TOQOmwk9IdBII-IRs-v5BYH_MonO0ZTvy2bGBu585UGtNwbHQi198fVc47IYMGVZohw-R7jWQjylTz9LhTijXdw5SPQ5jM8BZws6z0Jlz1ot2aneA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یه‌نگاهی‌کلی‌داشته‌باشیم به تیم‌های صعود کرده به‌مرحله‌حذفی و تیم هایی که در لیست انتظارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24480" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24479">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWHSYMlTYqAjqN509JCgA7xVAq3Qt1JAVtP__RnuLPwmm09zdCv6fpH8GH11SJKE-Vnzb38MkqjI-NVWSJ8-fjm7lzFPRsAarUSFGns1TVuv6VLHaX9_Mmy8duBZHOa1yYvgCiGImZeWxZliJHaJOcFUaMkR3IWpsftoHjqjaRmf8vql7A6G1mQT_qHN-DIu4ubGm3qJjXlyh6PmT-PTcC_2iFgsKHtvsb_HBNj812-YG2YaFY_xB6tajgnf97sOvVvSXUx67folYnwUThM3vTuI3z7ZQrqd437B13WsimSd9CqpfYpschRcFj3_Nw-Qtozh7Z-N3HVMAs7Om-ucZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرعقدقرارداد باشگاه استقلال با گابریل پین که از امروز صبح تو رسانه‌ها پخش شده رو شش روز در کانال پرشیانا اعلام‌کردیم؛ مدیریت آبی ها قصد داره بااین مربی ایتالیایی قراردادی دو ساله امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24479" target="_blank">📅 20:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24477">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=EqdB01y1jPjKPMSvuZMdT44R2l3dAbZUVHtr-B_FEzKsp7a84t_qTVQcOZS5n2QMu7RUJU3zp1FiwI-uTzBrNxLMmHq1jnjDRPqE1jL9EwYvPBbtjABmpY52cuL1HW5ImYB0nPnTQ9MtWP8hn32eEJP1AQ2lUCNaMnbnxjmgFUY_wWZB1JarVT9kv02QiC9WhMr1xR4TnmPBDQpXVxwvQAnr5bu-yWuEtsmo8KqOyL8DgdfTwnQwUAc5bX7iM3m-8X9umkspOMt-oIFlSF9DwnTnfpBZT2A1WJgbclvExmne_M2UsE67ExwneycyZzuWq9gxTqrmg4m-AH5PdVcn-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=EqdB01y1jPjKPMSvuZMdT44R2l3dAbZUVHtr-B_FEzKsp7a84t_qTVQcOZS5n2QMu7RUJU3zp1FiwI-uTzBrNxLMmHq1jnjDRPqE1jL9EwYvPBbtjABmpY52cuL1HW5ImYB0nPnTQ9MtWP8hn32eEJP1AQ2lUCNaMnbnxjmgFUY_wWZB1JarVT9kv02QiC9WhMr1xR4TnmPBDQpXVxwvQAnr5bu-yWuEtsmo8KqOyL8DgdfTwnQwUAc5bX7iM3m-8X9umkspOMt-oIFlSF9DwnTnfpBZT2A1WJgbclvExmne_M2UsE67ExwneycyZzuWq9gxTqrmg4m-AH5PdVcn-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24477" target="_blank">📅 19:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24476">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSqvEdrgloRbNTVwynTbumvISDIR4KPrCLSj9D5uH3fegZXfS6kIDSvW35XE5alYHBHPLoOHXPwXVlLQBce5-uBiQFk4w-wYDeahBW2qtQ6VBwMgrxcYwjS81fFMUl0Zsui7bsdrAoRd9in3k-1Q9ZC_QUQGnJf2KOkpsZ8zlWGfaeb_U3pxvNWd7EAjPkvLOqAWwsi2B3w5lO0nqYD8L8LVhSI1ybHhaAtrg_JDZ3PqHKs55qBKM1UQgTFVyjRgOz_NZ6YiC8nTWmui9oQ5zKlEQKMfLQE3v3lCS3FQT39GDGbP3L34ymewPrczquLUxX2IJKBGtiZyWF4ta_8_Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24476" target="_blank">📅 19:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24475">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3GY-RCWDl5eSiXtNODo3D_gCjnXsQECB0YoBgERxhTnkruG2xvQF61f_OZiy6UrvBgRhXKmRcqgrXgS2Z8b1imscD-DRHjs51IebFGfdfRstyCOHtNM3x2M-8D46G9JSsfV7n58G8J9lA0dSwIqwme1fFA0z526UAN-MVqF72xqqTKlO57fdcOJuNpshFulkkLD_0-fC4niGEebih_onJter1wv7X_I20IRrVJzcQev8WMvQCXT-ZoPdDW5BTqYm8EHrf2XGaljlNib4gv6lGi1xcpHZFlON8VSOj707jhNFZfYlciNmT2fRa0phogFORaFYStl4onfJoqW7hqd5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
باشگاه رئال مادرید مذاکرات اولیه خود را با باشگاه چلسی برای فعال کردن بند فسخ قرارداد انرو فرناندز آغاز کرده. باتوجه به اینکه انزو با رئالی‌ها به توافق کامل رسیده انتطار میره بزودی توافق نهایی بین دو باشگاه بر سر این انتقال انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24475" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24474">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhvY3GpJa4rhJi0tmx4MBsmObFjI8dzkbPlvuQU6LjNHJCDVAQi3QS9qd4eqHPoxP9mRVPYQRkOksi_5gDdH44Duv7Xjg2Was5dv7IagTq1mG_CGmxW06oemdZiMqWB9ywkOZ-MWE6TFrkh7f--hgQadKxW_jtS-YtqvIydketA0Z9ik-F9Ci4eCMdIQ_3zwYhJhppQ2lWUzEk8DAvWFJRG6xjM5gdznFWsFKWod-Lt1wG25R0-RFaOSaSc9gmdihTTqWhDVyvKLxum3pKjCAAZyi6zbhV13_BjyXw9jkMN953fGsmSz1bXWOFIxPW_JttmDzNvnT_9Sdhj_XuS0Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24474" target="_blank">📅 19:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24473">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdUeKirrp_0BMb7kRP01pfHXoGxsgm1aznbF4IK7-46ih6g42ldrl3cGgWAgR-l0cqR3qfC-oOhR_Pxcw0Ugr1AT5F1GfdE8-74O7zwTwQgruz8grvUU0QiSSsp4uzbcD-uJ3GnAOKCsKJUtFE__BCyE1jWW_rySPvPCAF_-5fLNevMTFJ3rOvEuIohbOMQGHgGEfOl_DdTw6RU-pqMTaK9heis97UKwX4isV8I7CwVfgWObYKEqCwFWr7ekZGtNUaFt0j0DEz8q98ONqzufhwK0-Y5PQxTYeyGHXatJSBjoEb6ZUvDhfuKAtW-wLO_7kLscCJxFaFXFyNYFehkCOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24473" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24472">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=KBGbHMRCXDICHHmlj8nvqqn_So2WqvYHNmoHiNa8HMQIjJswveq9aw9KOzXGeQ_06U_hk_gsBM263VTeI7ftYdKsnxT17MeD3Q7afS4DzbI7zgy-g_AkT0uKvkuAaUiKHhN609O3da71HH4G7SE2omcUj3Kk1SYQLeO4ATiVOLa1qvUhSplqIXkyVUDpx7ubDxVqVYtGox8LvxbjCrJ5YMAJDTLfKVoO20_V7KJdMfxfkRGCYEz-jQIaygUTZw6I5-O6HEXKF3VLsowDTgH-Ci7k5T2r-5Al-bWXIEWkTGElFpo2Fm1L6xSNgYjYRv7U53rPPDD6z6la-3txWepnNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=KBGbHMRCXDICHHmlj8nvqqn_So2WqvYHNmoHiNa8HMQIjJswveq9aw9KOzXGeQ_06U_hk_gsBM263VTeI7ftYdKsnxT17MeD3Q7afS4DzbI7zgy-g_AkT0uKvkuAaUiKHhN609O3da71HH4G7SE2omcUj3Kk1SYQLeO4ATiVOLa1qvUhSplqIXkyVUDpx7ubDxVqVYtGox8LvxbjCrJ5YMAJDTLfKVoO20_V7KJdMfxfkRGCYEz-jQIaygUTZw6I5-O6HEXKF3VLsowDTgH-Ci7k5T2r-5Al-bWXIEWkTGElFpo2Fm1L6xSNgYjYRv7U53rPPDD6z6la-3txWepnNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان و تیری هانری هم نتونستن جلو خودشون روبگیرن و تشویق جذاب نروژی‌ها رو انجام دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24472" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24470">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQ2hMbaB2f8SyKgtoqgTGjZ1m-duvGYxbkSxijqBPDmybyMPYDMc7MD1r5CCHtGeuifZAoHvQgdirtNljZ1c_TTD_4C8mLJ1ILg6WlTz1JZs9jhLjLA5xBFZQ9aeXT2geR6-kc5OcQUbrhlvDRj4MMAzoxTz7ImeubU12gPpoSaPjaLfEOIk0_8aFa4hXb2MhSOsoyMgyx6uI4PBeL8gw6UtBtukvuY1lBE0HP0_nJtjSsW-UoNkwUE3TB1UvhVhKSHRUNKwlbKU6cNZvvJPABsWSQHIOQj485mFmUP5wxlGRy2i9His2oyEHwlfnJitLYDrKBtYYxJHOkFzI3TXcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇺🇸
فدراسیون فوتبال آمریکا در اقدامی جدید به فیفا نامه زده و گفته‌آماده‌ایم که رقابت های جام جهانی 2038 رو به تنهایی در آمریکا برگزار کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24470" target="_blank">📅 17:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24469">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myWpFvbPNz_n9rI9tfkQUe3kz6JjkRuXcEGDmhFhU6TW-gt75g6H5GLhCC4LCMwuHLBZthW4lcgliykilg9g5Zgh3a-u5XBR35MkPc69Hy2DXsy4hLfGtE9ADLiQ9C4J_YbOaxWjD9qE_gBlRXvt4WKc3HZpFfqQi2W-_L2O1D77vWTWOh0AJjq90d8EqLgAmqKS949trlbraB_3LnH1YXVfUp6z6omdBjIdk0S7CLj-IszME4nTKVCuYieaRSJnOCY56BLtKrr1QeEbJvhn5KQ35vc80MqMIzJnGSTWk2hGfrbikAKDKmQ74PQvyEyibo5_tMNcY9SlA8HHtV-sOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ گابریل پین دستیار فصل گذشته تیم سپاهان از طریق‌نماینده‌رسمی‌اش آمادگی خود را برای عقدقرارداد بااستقلال و اضافه شدن به کادرفنی سهراب‌بختیاری‌زاده اعلام کرده و علی تاجرنیا منتظر پاسخ نهایی سرمربی‌آبی‌ها دراین‌باره است. این مربی ایتالیا از سپاهان…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24469" target="_blank">📅 17:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24468">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APTNVYNN5ZhGhldK7jG7E5VnDHesD-YS0G0ln-8g4_J7-zW1ZI6bU8Df2PX5QXjjXRNRt4L_4PNa0Us3z9Q6J9Xor-hFNSR8rrUCBE4Oai8R9TPEC1VOWJMVIEAgig3a8X9uTpfP6PnLkYr7sEMYcHRQ96pHzO8WHgudbqzDU7zeOH2EwTyvx6Vn-yBmSpjFinzzfJnJflchy1_FT6UbotXFUkj4TP1OZqSJYkj3e8gD1HPnBpPIgKlqRA8m03reZsiGcwhNf6HphZC1hq4hzaYT3iVWa8saIY27u-izJk6lJbtVJcCpqOlzTs4VByPxmSYY44RfFCCaMk_5QUjCdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دخترخانوم پاکو خمز مربی سابق تراکتور در کنار خواهرش؛ بعداز اینکه نادیا گفته بود دوست داره به خاطر رونالدو پرتغال قهرمان جام جهانی بشه رسانه‌های‌اسپانیایی بهش حمله کرده‌بودن‌که‌گفته‌‌من‌‌فقط نظر شخصی خودم رو گفتم و حتی اگ در فینال پرتغال مقابل اسپانیا…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24468" target="_blank">📅 16:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24467">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0TivUv5SWo-BeSwY3YvAKo7uag5iHT2O9l_BeqxBnbQGYKIhZiGIowHXTLtAYQ-Vk5beyk2y68ujDqCKxAcxBoEOlENtI2GuuRqCyC2ZIEAWrxPJOw6unVNN_kKQtgWvI6I95HUf1PcU0XEHJhdjgUNjXNhnzqx1wuDH4IBNZvurmuGuo6gu_vSUDmcqFEneeFphnazdFqLPsgw6seVXgqg7LR4Cy3IfGicq0uGnAhb6w8DIjDixcCo42EsbwPearLoO9yxeOFCwofzFWyJmbtINwCpvnykmDJBgAK-KlHITF6T-ugFBP_2J4P8vdwG3BVJnVp-Hk2mJs26osI-pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛ باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24467" target="_blank">📅 16:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24466">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUWLHIp7G_9U7m5IvK_BGC8UvGhvTml_2kUYq_XmG4Et-juhiSOUB8k7yHffitzejR96VX5RlC3XhynKgYlbR9LtASHNBZDFJtCTvukJ-LJpVqPB3ejLG1OVtloPQB2Wal3jVFbRx5K_gNbxpI_SnYDfbP95Xs1akC02r9DLNirpDqdnBToulRb6b7mnzdvVYsCBf4tuMfiSGqgU9GGU56gvlm27zjXnTfSM7_c1dRR6acfzWLgcWRmLjYyQwiiW7qPa1aMwvXqKcipw214NuRsJo6LNVqgabZoAG-hCSG15vuw4PKPo6zZg8JmwcVk4t0m3MTgtwPdC2mJTUYmanw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جان سینا اسطوره کشتی کج جهان:
ظرف روز های آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/24466" target="_blank">📅 16:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24465">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEl0XFdQi3PulEHWuj93g-VTo54EzzmaWLm0bWY8HiDRES0i0si_v5XAwG6pHU93cqNfGOtmXrwmRPV5iOENlfVcR_zILaP1WZLgOaQ_FSADHJJRaCf7XTf1ZrU6tqyPGa0YvdF7krze8b9w3yAH9tyITNxJk5D4JwzFVJnwkRldfS07xXdyH_ckEO5Q48z7gcajyyV-EzKcsSXGUPgMfYzPkUTXZ0rm8-zeFhICIJ-JlUgxV-uPshB--Q_UOO0t35ABwExSMenlu22R7jAW3smnkT3-KPmaE_CiDQlrv5kxTfzKRoZ1uruR8YRZtw47827KhEf2Cb-d0yCnadmGoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24465" target="_blank">📅 15:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24464">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbYo0ssQE17NLDOqaDOt-wT5F18_aHsZw-mj5WUJrScWmZqHW8Jtuf6e_MEL4UUEDY0NaPRfTgTlVdyk7z8Cr56qETtzAZByCWCWjNe4k6mN2ylRMy5lvRc8olc9ljNzkyk5YKKVVGKc-jvlKR4jRF_pI4W6MnFmpcW4o2DDo0WfLzQ-DEHi542DhhS3depEsA0kNlZjyKOQkZkXzNZYlgOW0TjlKPI2Coy-xKPOBALIlwMkIsm_rHqAfgaH7B2ymdant9O5_fFBauUDxraLxtuH39UFS0njCCI8uhhgJI2Jr1ipiIyruQQK6MSRYcFOoKLl_LNBAOYXTuTAz-L6xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ
: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن موقعیت مقابل آمریکا درجام‌جهانی 2022 و عدم‌صعود ایران به دور بعد، گرفتن کارت‌قرمزجلوی‌تیم سوریه و خراب کردن موقعیت ها مقابل قطر در جام ملت های 2023، قرار گرفتن باسن مبارک مهدی طارمی در خط آفساید و مردود شدن گلش مقابل بلژیک در جام جهانی 2026، خراب کردن پنالتی مقابل مصر در جام جهانی 2026 و کشاندن ایران به اما و اگر برای صعود به دور بعد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24464" target="_blank">📅 15:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24463">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvU5_EDQ-rHytMpFo4jHPBifozHM1VtO9lsGVlpwgeAGJTLooLJCsQMWZ2XuyqZ_nSHJ_XVpc-h8s2DPijiYolLkOWL7VeQcYmiFmgrEdE2aQsWIYlq5SEEZJekGQbvyKMCC_CHEsXbIwYup3u4vXce3UhvbnztOh6Mnvp_sZcduCvPco_3XUK7IkKMmBLQSinHvb3XGexEcg7zls82BqfzWUBYvdcj1CBxyUWTdieX5GHS902iho7n7gwr3v9DmjhL1r404rQVgkGBDEe4G7A8MD0gyUSNSD-cuTHPgtDeGBQAKP-ufjKiBee3WT_aECHG1rnf3IAxzh4mAL7nBiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24463" target="_blank">📅 15:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24462">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=LnMEaVbLzM7-a7IPJyMPbSXFbKOjaCREe5EcydzjUDAS0P3J2lMvL3jtDz7hEgoXQvs0c7HcWpGZXge9Q2NLnh6ll5ISyJPMLFgucYvOd7tecL5_OCgECL7Mubk25-DkdTIW5A_0oMQWyLVVuw2hEXJTv4QoZ3NFFE-In9alCX6GbwrDPo4wjB3rFJsT5Uif7of0rAoVAAsiwp4O_Keu9ULlcBasnHcRCAOWUa8zR64v2Kh6YV9fhRjGe9opkvC74ZLrtvKR-9BV5mLmrHFpanpuQR_2p9IZbTTK-sjArjdChMk0gpPBl13vSrYlm_NJPDaFa_wcldSgqemLClfccA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=LnMEaVbLzM7-a7IPJyMPbSXFbKOjaCREe5EcydzjUDAS0P3J2lMvL3jtDz7hEgoXQvs0c7HcWpGZXge9Q2NLnh6ll5ISyJPMLFgucYvOd7tecL5_OCgECL7Mubk25-DkdTIW5A_0oMQWyLVVuw2hEXJTv4QoZ3NFFE-In9alCX6GbwrDPo4wjB3rFJsT5Uif7of0rAoVAAsiwp4O_Keu9ULlcBasnHcRCAOWUa8zR64v2Kh6YV9fhRjGe9opkvC74ZLrtvKR-9BV5mLmrHFpanpuQR_2p9IZbTTK-sjArjdChMk0gpPBl13vSrYlm_NJPDaFa_wcldSgqemLClfccA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24462" target="_blank">📅 15:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24461">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=eP66ZgdFzW5EuCwnGHKHu97MpmSKbDWekP7GGxcX7qfMbUTmW_z8AvX4VS-lRj8ybyIqndo7v4FFfetFK2my3b4XKeGz8844Z_1F1fqrqRKNdpl5VQW0KSP1otFEBmulh6cLGXbYZiWvbHTj2Qe32hq0U63KT7eOh6KeWUByQaqj-yySTwEH1X6_Ks7D0X0mUAu_9JYOb6PcnKSCjwGcU8ro60ATNiPKGeFgfygc_qr-03v8UqHPFifLgPj5QTJge51KcmGaV352bekOogs81b4HOjFZue__AQGWdO6f6sru8aUvn47xJ_flNxGFQc4YQy9WJAZSlvQZR3IB8p7rKB0pE3LVW39du5FmT1fC51eHaQqQSbcozAEfV-uc5GfpieSQP4HnDFxNRuG86COsUabvK_lvXK1InaHwDt_oPRoIn23X0TdbvHXiQuEJpcxeNrFffgvzRS2OxOZw5SRSyJlS2wZFZLybFScslHdmpXgMaqDHiZ7A5wkeKxITuwuZVBmEg2ZsgBWAWcOX46vscDJA1UUxo4WL8rlWj1BoLFC46RRuM6v3mkHWjXoD4S288du-k8WpwWEC0SesTo6VT_GTF8gobAtSQGwQuoclLMRPGcAZ_FBIredtsFz7E2j7fWwCfUR5u3SBm4awbp_Jw_Lr1Aa4aJ0lsJHV80TFco0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=eP66ZgdFzW5EuCwnGHKHu97MpmSKbDWekP7GGxcX7qfMbUTmW_z8AvX4VS-lRj8ybyIqndo7v4FFfetFK2my3b4XKeGz8844Z_1F1fqrqRKNdpl5VQW0KSP1otFEBmulh6cLGXbYZiWvbHTj2Qe32hq0U63KT7eOh6KeWUByQaqj-yySTwEH1X6_Ks7D0X0mUAu_9JYOb6PcnKSCjwGcU8ro60ATNiPKGeFgfygc_qr-03v8UqHPFifLgPj5QTJge51KcmGaV352bekOogs81b4HOjFZue__AQGWdO6f6sru8aUvn47xJ_flNxGFQc4YQy9WJAZSlvQZR3IB8p7rKB0pE3LVW39du5FmT1fC51eHaQqQSbcozAEfV-uc5GfpieSQP4HnDFxNRuG86COsUabvK_lvXK1InaHwDt_oPRoIn23X0TdbvHXiQuEJpcxeNrFffgvzRS2OxOZw5SRSyJlS2wZFZLybFScslHdmpXgMaqDHiZ7A5wkeKxITuwuZVBmEg2ZsgBWAWcOX46vscDJA1UUxo4WL8rlWj1BoLFC46RRuM6v3mkHWjXoD4S288du-k8WpwWEC0SesTo6VT_GTF8gobAtSQGwQuoclLMRPGcAZ_FBIredtsFz7E2j7fWwCfUR5u3SBm4awbp_Jw_Lr1Aa4aJ0lsJHV80TFco0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای دم صبی جواد خیابانی و پژمان راهبر از این صحبت های امیر قلعه نویی شروع شد که گفته خدا باماقهره. جوادخیابانی هم گفت این حرف قلعه نویی چرت و پرت بوده یعنی چه خدا با ما قهره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24461" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24460">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346c907015.mp4?token=R7C2bznoxUp5Kq3uq_NUzjQM9Gs91jc9UByAa3DxPLllZs36HgRX72MEvoY_vi1A7aKRjNiwE_JNgpBU3h022gBywuMxsl197avG76Ulxh9jYFocfFsCudnOLOZsRsiNM00Iljjf4yfbw9YvXPPnSeUQZOssJGuUiszKMrbuX1B9zb44ftIoB8Cak0H88LVI8xUjoc7iG44-tmXsk1M0-QI3BZx3notR2B6Z1nUMWr1VeYAnfroqkPJTjuAiixXfpZ3zJYskaGtUjwIcZ5n2HYZA6G0Flr0GbqHsp7f29Pf52Kmt98SdxK5Wp8rZ8u_CbGfdbqjEgKOs5uBQay_X-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346c907015.mp4?token=R7C2bznoxUp5Kq3uq_NUzjQM9Gs91jc9UByAa3DxPLllZs36HgRX72MEvoY_vi1A7aKRjNiwE_JNgpBU3h022gBywuMxsl197avG76Ulxh9jYFocfFsCudnOLOZsRsiNM00Iljjf4yfbw9YvXPPnSeUQZOssJGuUiszKMrbuX1B9zb44ftIoB8Cak0H88LVI8xUjoc7iG44-tmXsk1M0-QI3BZx3notR2B6Z1nUMWr1VeYAnfroqkPJTjuAiixXfpZ3zJYskaGtUjwIcZ5n2HYZA6G0Flr0GbqHsp7f29Pf52Kmt98SdxK5Wp8rZ8u_CbGfdbqjEgKOs5uBQay_X-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مسعود اوزیل هافبک‌ترک‌تبارسابق‌آلمان‌که فراتر از یک هافبک بود، مسعود درتیم‌های وردربرمن، رئال مادريد، آرسنال‌بازی‌کرد‌. اون درقهرمانی آلمان درجام جهانی 2014 هم حضور داشت، اوزیل در خاطراتش میگه وقتی که آلمان میبرد آلمانی بودم ولی وقتی‌که آلمان میباخت یک ترک مهاجر بودم، بهمین دلیل سال 2019 از تیم ملی آلمان خداحافظی کرد و در سال 2023 هم برای همیشه از فوتبال کناری گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24460" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4eeQ2acaE1icYKfsAZMxpuNagWeDEcqUMTlzOiNPU1SicJeVktcJPKJjHSq6vPt4XYv19nmlJgtqJ3LyC0f_PD2NiPPhuNqssZssriIhNjZwtoqqmj6Wt-XJ6TOGdBuOO1He5kx6crx0tKi9uebpTogYkGkkpOqIXcE2c_USrAlnb4RaQObkDWg-qKocUZYaryjqkeN3hlOFzYHDwSQmiL0nMANZVc7XD7uelnfrvmp11yuyhZgsql_JcXVsRrVdnwXxffa5rzMlNecXf0K8FSyYT_eAtSE9whYTZxAPsCdcoUZfWFtnzmxxgbBG56t7WgF5cI4kWwkFT6ZUemwkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24459" target="_blank">📅 14:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2kJ4V05BGIfaQh42tkkVpiRHgvDL8SLD4AR9MohKGtKBHw85WrKkeXDHjgj0ND22C6Tysw2UPNX5lQnH_oRVBduJIBJEoBHHyjTt11272uEqsuWXyg-A0lVM4mlc8Or5jyTg6rbDvbPHA1N3xAInzK90OMHWI360hJFeqDIz4EfcVUZajxZc7NGrp3r-krgYFTB6QKDpP0dXZDbtDj779VOlDMCGIBCVSm7HJA-ELJD4Mt6uyMPpTeBl21iAzPk8VHMRfit5uYC_I5jB_bQnjDqUdNOJFss6D66DkEz21789_gjIptlG3et_retPQ3Sw0pY55rWd-Nd9ckwYQg9Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برونا مندونسا مدل ترنس اعلام‌کرده که تقریباً دو سال رابطه پنهانی با یک بازیکن سابق تیم ملی برزیل داشته و اون‌هم برای رازداری 100 هزار دلار دریافت کرده که البته گفته بدلیل علاقه‌مم بوده این رازداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24458" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24457">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=XUGdC2NzgIEv8moj_KPiXfjTSpBW02o3Jdl4q5fwUNqUvoTj8jy7H8Wnw-46Um3CgfFrR96KVbvjXoxm41HiDlBbGVcgKyYgBoRvu8pG85k4RcXfAJcau20FmbS8ihYN6YuVbZElj-AgoIVCNgZsTJkxRyEQOE0tC47QlMKCEDmhRgbCRESn31Xr0PIdIRMjD1-dsBVoqZiaqYMyk_SuVlqkPk-BVEJhAzSBi05ARqOQdBGoIvX559LNAWzX6uQ6Ctr44yHCChB3qTBR0rQRqHQcfJ5wS5N4rz9vlhKpv5QCA9wmv4rcN8q7cIQZmmfd9t95z_pqZGMOYjJ50EWkYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=XUGdC2NzgIEv8moj_KPiXfjTSpBW02o3Jdl4q5fwUNqUvoTj8jy7H8Wnw-46Um3CgfFrR96KVbvjXoxm41HiDlBbGVcgKyYgBoRvu8pG85k4RcXfAJcau20FmbS8ihYN6YuVbZElj-AgoIVCNgZsTJkxRyEQOE0tC47QlMKCEDmhRgbCRESn31Xr0PIdIRMjD1-dsBVoqZiaqYMyk_SuVlqkPk-BVEJhAzSBi05ARqOQdBGoIvX559LNAWzX6uQ6Ctr44yHCChB3qTBR0rQRqHQcfJ5wS5N4rz9vlhKpv5QCA9wmv4rcN8q7cIQZmmfd9t95z_pqZGMOYjJ50EWkYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24457" target="_blank">📅 13:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24456">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZNVhWiBJcPl9cTcESG3YsJ6nr9S497OtbzluhrgqACPYmfL8yrDHGjhVa2MRB6zPhG0B1pFhRIJuCOjl06QNVOKiJh9qBA1K93dkKqlJW-us-UMZVRnB1o6BpDp8HCeSCmJzTFZrn1shffzu6byGVVr3ruuez3f9KLLbQdtWWMzlEAl-sdtOx-JQl2fCULFkWwFUnqaF1btKjaRk6kcmU3KzxHwNpZsUdRmvbVRpBhvFMqW5sc4VhnvnzSUWWlP9mV3wCq2btLPOAJA1GLFYyCWTc10TgCyMoSqa9OjnpL_JiWo99rmsadz6FvbojR7oPgpdesSuNx_TtplS7wzbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24456" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24455">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZ-VucpdFZP3dHF_-Paam4UW3ZTiL3HZqeaZp2gy5MEn4rKs_040PmQ4eSwXysJFqalLKso-UFHtBmwb3GOOQr40a75inZ0GQu8CRUfGAgbopOnEYzQ3uECyGt9-Tnw8kstXHkDgfPTyNxvr5niLPAFP5U678DAq9l2uipIU218zWpMxgQwUcbeFOEdviF9oKGjuy1KGoxwxsb1w64YI6RRtciy9X9k0_fFt9QPlF0UxSWvCeRCj0RQ1RQb4BBjmPuBFJ1ZJq2L82McBAQtyCbyoH-2x11re5oKmmAeCw5I_deQ1R2y0nI9jrStfdAjyk1ZaOAY3JsyMbuQ7C7Fy2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24455" target="_blank">📅 13:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24454">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSx5o4JkW9bBN2iyG3DBFnMJtpSfrIFZJWeO4MF4u09PLE_q1rPZBj1rE0Dtr6KTYOOeTdrOqBKvQ_ULmGg7GNPiFFb0tq9EMxbNg23ogNwJ_sNwL4Slpw74RfiKOMVKv6WMvmU5O2E69S7_LMw8fH43-1ZYyr1ogWI_ZJPWvi8sMvAILVQee_ctIBRMtEnvsL0cMD4EraRUbqA9xOCqonFS--ac0SVKnpK4ng60Aq_eiK0feVJA_uLWdT3k5sIOCrE-AwtUNbeGX7EhYMMI2pVi5LWHsg01QtcMUWPjtFZgZYlggi6yjSQKTtx4BteMY-AVWp15R4XHiP9efaAnWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24454" target="_blank">📅 12:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24453">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKVWP6xlVd5y9Brtlmgnu6zWZrBRp_Hagk47JaKkybag_qHJS_a0tga4HQ-zhP0PHeO68pimvtDA_Fx56WUWWfuq828tISlZtfgIKHFrP9r91nTL2OuN9W8c7j6ZF7I4wbK4_nCKHHyyzygNXpiYaSBy2J2Hh2_utcUNw6k8-2wDyFotzrN8Mdu6xk-ZB5s9BP-Xir8uvheVKiFokeyKac9-ezuXS8hlf2f9pLlAUlIP8iMsP02ARh2ylfmxeFzpCqQaMXVDoamQJKpOLdBSRdxE-WmlJKIY37IdPUl8JL1Gv7JBcISdiVHWAiT9RQmARU9l8_LdT69WxwwMNQKtkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ ابوالفضل رزاق‌پور مدافع چپ 27 ساله فولاد خوزستان درآستانه‌جدایی از این تیم قرار گرفته است. همانطور که پیش‌تر نیز خبر دادیم رزاق پور مدنظر باشگاه پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24453" target="_blank">📅 12:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0xdkcwS4Q3g9B2r1-TAsvLE7eUZlPrAC8FIKzFpmIUqXSOIEsrts7Hy3rL6vgQ_KSsqkWJEE0NwOtCzviE4-VOcDc1EibfgwqZwsxXAMvb79Bq6EZWds-EU4_EEpNdiSnXULJ0cocVOZGZjrxiCptyLnxfe3P70F_Otbglg9KXy6lHsYKHVQu5Qh0w3ilvi_kJzSddB6q3eYKhbaYYEFSkOTJChmwyHySWUftdymMLetjTWJyMeHsCaHJhRBea6mE2bWsGSVtcDEw0U28pWjF_9QbY0gjsglpAj6elNY7wrdAtSsDyd_N2vTA1SDw_HRLy-hX80ThfqCA6qe7A-hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عذرخواهی رامین‌رضاییان ستاره استقلال از مردم ایران بعدازتوقف‌مقابل مصر: شرمندتون شدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24452" target="_blank">📅 12:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXGcZ0ZA5GV3fgLJ9AP3BJHKcFr3bnA25KA0fZ4RiPS1nRNDA0lamV_COnYvHCdtrJ1cwtYewLNV6FnsqxQ6RqAFjOEzCqep86y7fI6IVHwYj0UCwI9nZcG8bcrWZv0EUqy8INLuyxZcAC0DQ0bXloF9ghA_Bq1J8P3AO4zvVmGS5JlDOsqIcpwmnIPPNuCYK25eoEzq-D6PqxdWpI_cvoJpRbWfomltFtN8O6ImZWg6u5wcvHx23bXkjbfKEDi8QlLjN9L6OcC6UwK9kXurYNed5BvzGe6MorGGJckym59DCg3QWEHacIHUGdSDZy3fEZd2eLPQKXrHmzUb6IMYvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pcHsmtI8ojYByLqCyVS5G5dEClO_NdyE3-ig8kj2N1NXjdnW2CQLynFAGuFNT3L_IFTDtSz44vqanx7S_bClWsJXGXqhcQafaomeOm2e1xUC-2W_rxMRuPCqCNNzNNq2pQEKeoIlxO3H90gj9uquPUc03OvxuoVUccF64DVFoci9HOvVeLCjhMV-4kTGtykzXSj0ypdt7IRzTyONGNcXJLx8LPDVG9QiwR-qcVoxlgA5pr0HWeEd0vgnW3LYDZ8hpFVDXP_1hrs-tJ6QQ4yC-k55ZppOX80lxnmZ0sx3UTp8aZ9nxv-N6r_jHEFQIAZ9sT37ou2co3rNjvtlQJlZZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24450" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSvuW9r-xKxQYPGw5sP0qa-FFLYmFWx6QZakUpcjBntjbMZewnBH1Ck5n0-xQXhsRZYiBSK_P5GLOoEnBaFaOl8zpNOb38696U1ACQoi9bcz484mD2hXoJHKstXpVAYqmCytSJaqxYFbZF-b0VqrCmn_b8JWEqorMZgVBG5uKGl7NQkRah5gvzZhgAKdoAHkL0yydX_8Eyjbwai_THmwdEPL2PDZ2EF6IHBckPzfRReiVliVbAVSYWJNa8QDUXoUosMO5BENl0ibNrb4eZJ3rq_xG1Yi4ypWUL00YTxeI2TYFkoJrNOHuKosCOsqQCgNqZtfL4SWRvC30oZTUQx7dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی رسانه پرشیانا؛ با اعلام پیمان حدادی مدیرعامل باشگاه پرسپولیس اوسمار ویرا رسما از جمع سرخپوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24449" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bo5zBSXPM3FBqu2xv4gwTrCK-Z-vPtxNtY6zLEY9MRe6Kp3kv1h5ogAMJPNPeCC3a7hZojQ3xluiU5YYkpP9xEesY2nTmxhnYt44OwMBVbPrqAzj6fjv3HuHiWfpATriZ_S0LCJTI95Kajee9VZ69xXiVVKooY26R2mk8LUKykci4iwULnp3Xnc5bLFi8hzsn4plHg0ceERreoMAWQJ1pbu9oqKyMtnZ-ss_d2WOYaAjh4W0jzZ23U52EU6MiZEEXdBnum_lmawRy97wJ2yJVHmVmjpzE2FCKLsIBiRl3Or7p5Gm52O52LUV4_ExkkcX5d5Vxj-XkFW1p0SJGzf0-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
#تکمیلی؛یوسف مزرعه ستاره‌جوان فولاد به مدیران این تیم اعلام‌کرده که از استقلال آفر رسمی دریافت‌کرده و نمیخواد این‌فرصت‌رو از دست بده و ازباشگاه‌خواسته با فروش او به آبی‌ها موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24448" target="_blank">📅 10:47 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
