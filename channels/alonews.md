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
<img src="https://cdn4.telesco.pe/file/GPKg24XXa2wmqLwmi5fNgrEi-pVT83114BbcAyoLh7HZKJ8aVCSz2j0EY3VXAGrp53MJqDGSEiQr2DX8HV66MYe01mRg8WrBDu_bIrUKr6ZaG-RY6nh7SoYHZETvQMfyGy8TA4jsJ6zljki5flxExCKkFBEBh12BTSqAyFMCmbdxaPKFgpWiFQRTDHUQkWpwGwtbOddPqMmx-wN3dNxEJvzf-C-j2EkaaMV-q33xEPIL5WSb1gMe4ReGLq4b6EdWjiXK7k0E0iB7a1Of8mPmGwnNkAxPDHVkprfzLKvol_X-LT7cXKxvXfrvpifJv55dwCxpoaMTZtDh0Gk5NPTTcg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 993K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 11:35:11</div>
<hr>

<div class="tg-post" id="msg-139069">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
خبرنگار نظامی وب‌سایت "والاه" اسرائیلی:نشانه‌ای دیگر از تشدید قریب‌الوقوع تنش‌ها در خاورمیانه... ایالات متحده خواستار احتیاط و هوشیاری بیشتر شده و از آمادگی برای احتمال لغو پروازها و بستن فضای هوایی، از جمله اختلال در ترددها، خبر داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/alonews/139069" target="_blank">📅 11:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139068">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
خبرنگار الجزیره: حمله پهپادی اسرائیل محله شیخ رضوان در شهر غزه را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/139068" target="_blank">📅 11:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139067">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3328847f69.mp4?token=gG8bQ_wB_DfLMAbjt7LbwmwVZ5aVxcksZ2-KzmQe2ZObQ8ptbOy_LcwuHEIGtr2sOuza9U4Tm6u1QJEEJccJrreMq81PLgyB8JQnRyiqH4xtHqEHFULVALOqgxEZRXJ7av_mrhqfg594_s2ZkzGl_IrTFDPf7WEaZOTG13FcH66m5nnSyjl4mlO20TIBIRs6FwHcirOYtzK-6fvvD_Q5JkKv4rC8CT4KiSif73OHvBUREt1HHSTz8TtQt_PGikXOiF46MWpx6t3OG8uKMGBciYRbLbFTsyLc1fevqT_K1MjiWTVTZMSMOfP6yyXsStFaOaJn8X_YxWceapJGE4B1VI3NwLswau7T1O36399U3bIFi6V2lyA2loo7zSjD3PHl4-USvTwvjxf4C4lVe03lawFhCkIjdoTeQt1tKyoPrKJ8c12PYDLpOg99B2fUbB7i06sbTZfDU6sx-fNxePnjIuwMl9MFzelQj6lpUymv9SC4RwaP7LhxRYKn0SdV5jNh-8FO2B51eSMMtz3Nop_dZK2vrequJbWIVvbgLUbS29D1QrJe176yoP3ShvDDzpSkjW73k1KL-FN7iGl3XJnwfHkoshNbVQyZWJoKoDcs71uX8xybFRFZY_j2fVHL6UTl5jzv2ESo5LSrMPeB11k84DP_jU_3FKE1fuOaZgao--w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3328847f69.mp4?token=gG8bQ_wB_DfLMAbjt7LbwmwVZ5aVxcksZ2-KzmQe2ZObQ8ptbOy_LcwuHEIGtr2sOuza9U4Tm6u1QJEEJccJrreMq81PLgyB8JQnRyiqH4xtHqEHFULVALOqgxEZRXJ7av_mrhqfg594_s2ZkzGl_IrTFDPf7WEaZOTG13FcH66m5nnSyjl4mlO20TIBIRs6FwHcirOYtzK-6fvvD_Q5JkKv4rC8CT4KiSif73OHvBUREt1HHSTz8TtQt_PGikXOiF46MWpx6t3OG8uKMGBciYRbLbFTsyLc1fevqT_K1MjiWTVTZMSMOfP6yyXsStFaOaJn8X_YxWceapJGE4B1VI3NwLswau7T1O36399U3bIFi6V2lyA2loo7zSjD3PHl4-USvTwvjxf4C4lVe03lawFhCkIjdoTeQt1tKyoPrKJ8c12PYDLpOg99B2fUbB7i06sbTZfDU6sx-fNxePnjIuwMl9MFzelQj6lpUymv9SC4RwaP7LhxRYKn0SdV5jNh-8FO2B51eSMMtz3Nop_dZK2vrequJbWIVvbgLUbS29D1QrJe176yoP3ShvDDzpSkjW73k1KL-FN7iGl3XJnwfHkoshNbVQyZWJoKoDcs71uX8xybFRFZY_j2fVHL6UTl5jzv2ESo5LSrMPeB11k84DP_jU_3FKE1fuOaZgao--w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شورش زندانیان ترک در زندان یونان
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/139067" target="_blank">📅 11:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139066">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW5ltn4dP5mAje2eu01Bt5ctLkWS4yKuQ70vDmVT0GQjejn1s7pxPw6awfhGCGIVM_ThE-fR-ZPhQT_oS0pDkGOPLcqEl2Z9VEJPVMTDo_qty6KAOMRnW7GBnkPAUqB4_QZfysxJmlYHbKJyky-yvP9u9IEO6mMEz0qtJM6BDtuy74jcJ6fr67pgct5WcQe-aJthz_QoEcKslhlRg-GUbvxPWY0UVRftq37T2hK-TkD9B-kCRlVjMnWOVvtXzqAH8DaH8K_Xwwpl8_jdHw1YtC0YQ21CfoXKj0xzYfuFdkApsRqiodDkEe5_BAvAzK269eeDIuOIpwx5li-Y4tkX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت اتاق جنگ اسرائیل :
⌛️
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/139066" target="_blank">📅 11:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139065">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
مارکو روبیو : طی هفته‌های آینده تلاش می‌کنیم
🔴
ببینیم می‌شه مذاکرات بین روسیه و اوکراین دوباره شروع بشه و این جنگ بالاخره تموم بشه
🔴
البته می‌دونیم هر دو طرف روی یه‌سری مسائل خط قرمزهای جدی دارن و تا وقتی این اختلاف‌ها کمتر نشه
🔴
رسیدن به توافق خیلی سخته
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/139065" target="_blank">📅 11:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139064">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn8y8XDuEqSn21RbGiqhEAspVuq3trRG_jBcf5A56LmU-LWWvPL2NQct-GqZcSNVTOJ6E-fWjYpoVmU60zOkKy0Lq7QUYyXpAMNXA5WnAkeKeuDt1-e7do4egZCvuUHAiHESzv3A0RfPICM6XSmgMxSD1qBuoG-1eXhQGDp_97CQvP7JlSVq3_3MneNO6Luo3vvCKTL1E-YdDPIm_DFQHuzry0lj9qDU-e6ElH3uHJnpVn46eyp1GUqJ2k4enmX_GLsjTVTPg3lyRFuBpJRpzGHJ7Q2N9kWc6FhGJlEBjqIazlQK3-rbZgR9GqTxcDtq0IbvVtacl4jeqXLdwBAN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
نیویورک تایمز: بمبی که دو روز قبل بر روی یک خانه در قشم پرتاب شده است حامل یک تن ماده منفجره بوده است
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/139064" target="_blank">📅 11:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139063">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
کانال ۱۲ عبری: نتانیاهو موفق شد ترامپ را متقاعد کند تا حملاتی را علیه بخش های انرژی ایران آغاز کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/139063" target="_blank">📅 10:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139062">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سی بی اس به نقل از یک مقام ارشد اسرائیلی:  ترامپ و نتانیاهو سه گزینه برای جنگ، از جمله حملات نظامی متمرکز بر مسیرهای زمینی تدارکات، را مورد بحث قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/139062" target="_blank">📅 10:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139061">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXBjTLfOG2kvTlDPBvh9GDQV_h8Q61MPD5YwOnS2sJ126-FsaCuz4OecaSeTFttdDK_6bDH_bNHFWFS4ki6Z8oWwYZKCT0QeOUTgMK8UbgwTDxidaYvh3ayBg9IGUuFezIRpX2YFe_n6taX_glihtFImmTkKXEpmVbKCR9XiDV0SHYPEgxs1jQfIgclf3b78M9tso1pQ6JfUXmSyJ1jxNNJqh_uPwcsWqdr9G6k5IyeeARX4nqS3CWaYehl5rI2fF2PfjwqkdTDdkKqYSazgg8G-ItWUNTq--3BMmodac5oUtXk_33-unmrR6iTxggKC1T50YEZPg0kszJqy0OpXEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس تهران با کاهش ۳۰ هزار واحدی در کف کانال ۵ میلیون واحد ایستاد این لحاظ که شاخص هم وزن ۸۰۰۰ واحد رشد مثبت داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/139061" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139060">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77bbc3a7e0.mp4?token=Lq1_qDLF77GL-84wvElJb38z_6bxC2mc95qq0p6SvFznFhGpdYHUhC5XItCmvPWBhZJR3zGn6YrOKFMQLgh3GvV9zSJOpXzUOQTr6mVdH8tUPdu6OYqjJNUKVxokYuXHbHFmoeGH9dYqZm30PBqLL4J75G1dsHPg-f8oouUrvJBGsJoXnCYdc9m8u7MIpvsc3h1lU8gpVzNwIZ-ogmTZxytFbcoVCHC5TZOErWOmpuyAOvwvU9NRlloMBl9QvgDfUC6TMvTDTCqlk1-LmJgeRoODuSFBMy-kG2ELsrDLKYYy0GlVyuchCh9_-3m5XMCPPPIZps_qXXP7tO3j38DGIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77bbc3a7e0.mp4?token=Lq1_qDLF77GL-84wvElJb38z_6bxC2mc95qq0p6SvFznFhGpdYHUhC5XItCmvPWBhZJR3zGn6YrOKFMQLgh3GvV9zSJOpXzUOQTr6mVdH8tUPdu6OYqjJNUKVxokYuXHbHFmoeGH9dYqZm30PBqLL4J75G1dsHPg-f8oouUrvJBGsJoXnCYdc9m8u7MIpvsc3h1lU8gpVzNwIZ-ogmTZxytFbcoVCHC5TZOErWOmpuyAOvwvU9NRlloMBl9QvgDfUC6TMvTDTCqlk1-LmJgeRoODuSFBMy-kG2ELsrDLKYYy0GlVyuchCh9_-3m5XMCPPPIZps_qXXP7tO3j38DGIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی:  تنگه هرمز متعلق به ایران است
🔴
ما به ورود آمریکا در تنگه هرمز مشکوکیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/139060" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139059">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8bc7642af.mp4?token=aBqBRY8-67pyPdXoSmHT1Jb0RGuVqFx2BL_SntA2agPipEAZFj803aqTEsDqBxHzLCcmuay_j0-KB-9KKXrwqUgMW3hVAv6HaveCzErgW28lyx8JDUdOjXyXH0tnm6tJcBihUnCRz0qkOJ_Qbjn5ULWakoRpOQgcDXiundm2GQM3iZVJiYVCoyzyYgcoJJou8K4gbBAX3TRNFCl6dx0SpAexIa4Uad7I2DvjY8tlbkOkA2jKHTgKp--5SfbQstZpy32YS8Sp-_R1DCwSY8xKrZqyoBP3h_DY-3jmGWExj4QPvTK-a0FchD7DJXA4-AlCA-gBHrhQozHBUB9ZY2-fhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8bc7642af.mp4?token=aBqBRY8-67pyPdXoSmHT1Jb0RGuVqFx2BL_SntA2agPipEAZFj803aqTEsDqBxHzLCcmuay_j0-KB-9KKXrwqUgMW3hVAv6HaveCzErgW28lyx8JDUdOjXyXH0tnm6tJcBihUnCRz0qkOJ_Qbjn5ULWakoRpOQgcDXiundm2GQM3iZVJiYVCoyzyYgcoJJou8K4gbBAX3TRNFCl6dx0SpAexIa4Uad7I2DvjY8tlbkOkA2jKHTgKp--5SfbQstZpy32YS8Sp-_R1DCwSY8xKrZqyoBP3h_DY-3jmGWExj4QPvTK-a0FchD7DJXA4-AlCA-gBHrhQozHBUB9ZY2-fhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی ارتش: سرنوشت ۳ خلبان حاضر در عملیات ۱۱ اسفند ارتش هنوز مشخص نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/139059" target="_blank">📅 10:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139058">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی: ترامپ به‌طور جدی در حال بررسی آغاز حملات علیه اهداف انرژی در ایران طی روزهای آینده است، اما هنوز دستور نهایی برای انجام آن را صادر نکرده است.
‏
🔴
این حملات همچنین ممکن است برای نخستین بار طی چندین هفته، شامل مشارکت ارتش اسرائیل نیز باشد؛ و چنین تشدیدی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/139058" target="_blank">📅 10:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139057">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
زلزله ۳.۸ ریشتری بویین‌زهرا را لرزاند
🔴
این زمین‌لرزه ساعت ۷:۱۱ دقیقه صبح امروز در حوالی بویین‌زهرا به وقوع پیوست
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/139057" target="_blank">📅 10:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139056">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4mBrYvyJS889asiVxN0bCfZXl4ncQH-7m6_hK13HlYD5z9n8ol94AOztToHB1BDuhwvN6DTLaTdIzAbbkfbmBV-yEOFSxxhyN8rFbyY70cFnYeofScjD6Jb_74qIrLrbC3YGtZANi1e6yOqCOUxqYnc7axthjnxNfTFUVXbicAHmTy4VbIE2PSU1GQoLOZSm39ji5zP5bt4HLximTsPEHejoKdQsglkyBYd9vBnVDLlTILux7XNbV4Onfv7x7r32CO8Ei7MCNLhRqHbAAI3Xb4f7pqDY-MvoqpxhuXrO55TYjD9gKkNGzmB8977IAFfWdzSi9QwV4DT9o8YY57jrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستاد فرماندهی نیروهای مسلح کویت اعلام کرده است که سامانه‌های پدافند هوایی این کشور در حال حاضر به تهدیدات ناشی از پهپادهای ایران واکنش نشان می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/139056" target="_blank">📅 10:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139055">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dffd6f0fab.mp4?token=t2hZs6koE28Uwis-lEzs9j2dV3AGy_9AHsqfEZDCvmufkSPmh7fg0hQezdQxNU_Qv2anKugE2_CAD1C51o3adFSKtjWUFLtDZzc5HqQBj3ivT49Aek4EMHjW2RvtyOXathmVtIM5SsAJX1QmwmsHqGuNabRI18R4Zc6O3A_sjZyQ63TiyeDmHIw7y1Tgvohr_E8LBl4jtAMnhGDz2aNSyLbujwfNpKbMIbo0aUWLKhQ8Z2bEECC_RpfnvDA8mktR-t0YZVKoK-8lIcp6lVe5s53Hz5vfkbnip_zengfmfU_GwkKgl_A2LPG_fLtuIXvve-S5Zud6bviJAA48RhEw_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dffd6f0fab.mp4?token=t2hZs6koE28Uwis-lEzs9j2dV3AGy_9AHsqfEZDCvmufkSPmh7fg0hQezdQxNU_Qv2anKugE2_CAD1C51o3adFSKtjWUFLtDZzc5HqQBj3ivT49Aek4EMHjW2RvtyOXathmVtIM5SsAJX1QmwmsHqGuNabRI18R4Zc6O3A_sjZyQ63TiyeDmHIw7y1Tgvohr_E8LBl4jtAMnhGDz2aNSyLbujwfNpKbMIbo0aUWLKhQ8Z2bEECC_RpfnvDA8mktR-t0YZVKoK-8lIcp6lVe5s53Hz5vfkbnip_zengfmfU_GwkKgl_A2LPG_fLtuIXvve-S5Zud6bviJAA48RhEw_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف:ما جنگ را پیروز شدیم ولی باید پیروزی را تثبیت و ثبت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/139055" target="_blank">📅 10:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139054">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ارتش کویت از درگیری پدافند این کشور با پهپادهای «متخاصم» خبر داد
🔴
حساب رسمی ستاد کل ارتش کویت در شبکه اجتماعی ایکس دقایقی پیش اعلام کرد که سامانه‌های پدافندی این کشور در حال مقابله با «پهپادهای متخاصم» هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/139054" target="_blank">📅 10:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139053">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d1d389880.mp4?token=p3FgqN7bE5HWXPY-hiFZoLN0bs2EByZYGbaC0A_aDdYBQ23segJvQ2O5q0wiVqeODHwYSvqUxPKevlwzid2ufVSrPW2iWGa6FHA0h3vAmgzSXTWVGE3NWJMRzWsL4czL95kQJrUfKWsVDkL9yD4yF1spk28e0LFL1Suyeld32SKguJnEZCKyKjaGo2rec_kiAbS9_Z3pCONY2AxoKrek4BSe9rRiTORFBp8dj2R4nAd64R96nzloyBo0vxIXYO5OlW6aYl33R7WbNXEQQ22FiXy6CHpfEGjIj_IwkCUBgN_8nrZlwe3FfvEqvdUBX5g2JK1dCsUZiDykmtruDpyFSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d1d389880.mp4?token=p3FgqN7bE5HWXPY-hiFZoLN0bs2EByZYGbaC0A_aDdYBQ23segJvQ2O5q0wiVqeODHwYSvqUxPKevlwzid2ufVSrPW2iWGa6FHA0h3vAmgzSXTWVGE3NWJMRzWsL4czL95kQJrUfKWsVDkL9yD4yF1spk28e0LFL1Suyeld32SKguJnEZCKyKjaGo2rec_kiAbS9_Z3pCONY2AxoKrek4BSe9rRiTORFBp8dj2R4nAd64R96nzloyBo0vxIXYO5OlW6aYl33R7WbNXEQQ22FiXy6CHpfEGjIj_IwkCUBgN_8nrZlwe3FfvEqvdUBX5g2JK1dCsUZiDykmtruDpyFSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زمین‌لرزه ۴.۷ ریشتری جنوب ایتالیا را لرزاند
🔴
زمین‌لرزه‌ای به بزرگی ۴.۷ ریشتر شامگاه جمعه منطقه «کامپی فلگری» در نزدیکی شهر ناپل در جنوب ایتالیا را لرزاند و دست‌کم ۱۰ نفر را زخمی کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/139053" target="_blank">📅 08:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139052">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfTCJD3nUnM9p1Xxm9EMGLdO5KCG84Bgr8m5GwWzNfQOuZrhcYF77B3vh1rr9LD5jC_QMBq66NOOH7A0C0P51-yPIWsTzBszJ3iS74l-G87R2YHJwrCwroDz1WYishUz3uJnvK4OFxJU_fFamgQgXIi57mUbo_xKR4W4yLLeFVwD2qMENFk37lSuLdPjYcXhKAl-K01Mg7QGDF_kPNdYYz9CUl0gZqRyu1EHsR7BDnsUnn4VvkPOLBMkyP-Hc14yH3lTdyXiy5iysF66F_1cWebjOJv-CWDdxGZEekb-iVfEB5EOKu_sVLOaQ8slDTt73-YjiKF-2wXeDft9uOTF5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: مشکل اصلی ایران و آمریکا مربوط به حوزه هسته ای و ۴۰۰ کیلوگرم اورانیوم است و بعید است با بمباران زیرساخت انرژی و هسته ای، سیاست های تهران تغییری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/139052" target="_blank">📅 08:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139051">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
فاکس نیوز: موجودی موشک‌های «تاد» آمریکا به کمتر از ۲۷۸ موشک کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/139051" target="_blank">📅 08:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139050">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سخنگوی کاخ سفید در واکنش به گزارش‌های ادعایی درباره احتمال حملات به ایران در پی نشست کابینه آمریکا در کمپ دیوید ادعا کرد: دونالد ترامپ، رئیس‌جمهوری آمریکا، همچنان به راه‌حل دیپلماتیک متعهد است، اما به پاسخ دادن به حملات ایران ادامه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/139050" target="_blank">📅 08:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139049">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-DFyD9k6dZLTCLfVWadqoJAsaciS_KQgJl8uwHDsITJarS51RhvZFslwM0ng3YzHjDNqAuopex6fq_1UQJg7Uo4bj6aQnLH8UmMYCamL8-JQ3ANOvbx4cuQR8fVkpNy9b3cy0c6IoHSDDLvQibxIrzfumzp5JapV6w4DEm3tY_2ZYNaEvAgTEksx_IIDAzt1ce7qoK2rm6YzYHDW5YvkK9rFXCUsHYftQNNqPX4Ff_bC-DN8cLOcchuYQAcc-8pNOwDvNK2fOw3kgHkOSD4YkD1fFOCdMLL-DVNS-pRsmHCMV8oTW75bEFz0FLImFS6zsprBqz00rcjH31rw35eOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال: آنچه که در اسپانیا اتفاق می‌افتد، با ده‌ها هزار مهاجر غیرقانونی که به آن حمله کرده‌اند، در ایالات متحده در دوران دولت خواب‌آلود جو بایدن اتفاق افتاد، و اگر دموکرات‌ها دوباره به قدرت برسند، دوباره اتفاق خواهد افتاد، حتی بدتر.نگذارید کشورمان نابود شود. به جمهوری‌خواهان رأی دهید و به ایالات متحده افتخار کنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139049" target="_blank">📅 08:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139048">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658c5b0c9d.mp4?token=A3ePidRubFV6p97oKgy7tU7dOjVvwK8wU-xJ4plRnHBTArwRPfmad6eDkPVEo-q_B1wwTso1pwnax2foE7POPKlGFS9ZIeIFYvIkyzktQhSrwg1Y9QvnfyI5-d5u9XfNTPMFryuN7tzJWprR7xxP13a2b4-RjJ9BwlFyi9FR7Mo3AyjYAGbEEUVfG8IT6gabbz5UB44OFACMcDQIfmGm8M6nCewBYnS9-ln6gvM3xyS9H8U6pfY6uG0Ym5cAlYYzs9hhAoqS8Vp4gjU30ROuIeC7rh4jPSlNRVPtW2DgkEOQTWtJUtBUUlOvMkyfIR5tw7q97I81TCL9LDKGTCxCuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658c5b0c9d.mp4?token=A3ePidRubFV6p97oKgy7tU7dOjVvwK8wU-xJ4plRnHBTArwRPfmad6eDkPVEo-q_B1wwTso1pwnax2foE7POPKlGFS9ZIeIFYvIkyzktQhSrwg1Y9QvnfyI5-d5u9XfNTPMFryuN7tzJWprR7xxP13a2b4-RjJ9BwlFyi9FR7Mo3AyjYAGbEEUVfG8IT6gabbz5UB44OFACMcDQIfmGm8M6nCewBYnS9-ln6gvM3xyS9H8U6pfY6uG0Ym5cAlYYzs9hhAoqS8Vp4gjU30ROuIeC7rh4jPSlNRVPtW2DgkEOQTWtJUtBUUlOvMkyfIR5tw7q97I81TCL9LDKGTCxCuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا، با هشدار نسبت به پیامدهای هرگونه درگیری میان واشنگتن و پکن، گفت جنگ میان دو کشور «فاجعه‌بار» خواهد بود.
🔴
وی تأکید کرد وزارت خارجه آمریکا در حال انجام «کار دشوار دیپلماسی» برای جلوگیری از بروز هرگونه تقابل اقتصادی یا نظامی با چین است.
🔴
روبیو همچنین تصریح کرد که وقوع جنگ میان آمریکا و چین سناریویی است که «خدا نکند» هرگز رخ دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/139048" target="_blank">📅 08:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139047">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
فارس: مارو از زیرساخت زدن میترسونن ولی مهم ترین زیرساخت های انرژی دنیا در تیررس ما قرار دارن و اگه بزنن میزنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/139047" target="_blank">📅 08:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139046">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/139046" target="_blank">📅 02:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139045">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYkzXT18xjYkpYZXzzxtuwOsXeNQEfYW5y6LkhPJ_SJvhMC5Ola7Atn2vtpvvnllgxSSmIr0QwuWCeeXkY4kNcpWcfCauJ2iiqM05AwI0WSW1bqm6ItSTFMMjspRWCAsevFMC8iDLgv_XkE6HH0Vt6g6T_ZRoGaHvngvGeSW4Uyy7R5zJZkR8ebCJFZtOod6MwCTg9L9b-qIQ600vQhQE1HnbFXLBvwztqhIZSphM07w9u42gI9ps4Hb7oZ8AkJR3UOF-31kon0jQ3FDbJ9eD9sY-LNueIyzGJd-gPPpS06AAiLSL9ZIvg6-2CpEH7zTAUY_LzZ23giQH3PPfRKuDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتقال تجهیزات ضدهوایی به جنوب
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/alonews/139045" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139044">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
قشر تندرو واقعا احمقن، میگن اگه زیر ساخت مارو بزنن ماهم زیر ساخت منطقه میزنیم خب بر فرض شما زیرساخت بحرین و کویت و ... رو زدی. خب اونا پول میدن آمریکا بازم براشون میسازه و آمریکا سود میکنه، ما چه کنیم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/alonews/139044" target="_blank">📅 02:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139043">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
تسنیم: یه آشی برا آمریکا پختیم که یه عالمه روش روغن داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/139043" target="_blank">📅 02:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139042">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سی‌ان‌ان: ارتش آمریکا مقدمات لازم را برای انجام مجموعه‌ای از حملات علیه زیرساخت‌های هسته‌ای ایران، از جمله کوه کلنگ، فراهم کرده است؛ هرچند این حملات صرفاً محدود به این سایت نخواهد بود.
🔴
مقام‌ها گفتند که این آمادگی‌ها طی چند روز گذشته شتاب بیشتری گرفته است.…</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/alonews/139042" target="_blank">📅 01:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139041">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ادعای سی‌ان‌ان: دامنه دقیق حملات علیه ایران و اهداف احتمالی که آمریکا ممکن است آنها را هدف قرار دهد، مشخص نیست و دو مقام گفتند که این حملات ممکن است لغو شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/139041" target="_blank">📅 01:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139040">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ادعای سی‌ان‌ان:
دامنه دقیق حملات علیه ایران و اهداف احتمالی که آمریکا ممکن است آنها را هدف قرار دهد، مشخص نیست و دو مقام گفتند که این حملات ممکن است لغو شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/139040" target="_blank">📅 01:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139039">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
طبق گزارشات به تمام دیتاسنترها آماده باش داده شده تا در صورت وقوع جنگ اینترنت سراسری قطع شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/alonews/139039" target="_blank">📅 01:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139038">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏
👈
آکسیوس به نقل از مقام آمریکایی :
رئیس جمهور ترامپ به طور جدی در حال بررسی حملات علیه اهداف انرژی در ایران در چند روز آینده است، اما هنوز دستور نهایی برای انجام این کار را صادر نکرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/alonews/139038" target="_blank">📅 01:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139037">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
طبق گزارشات ترامپ یک فرصت دیگه به تهران داده اما فقط ۲۴الی ۴۸ساعت
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/alonews/139037" target="_blank">📅 01:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139036">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
کاخ سفید: تهران تفاهم نامه را نقض کرده است، بنابراین رئیس جمهور ترامپ بیکار نمی ماند و پاسخ حملات و اقدامات ایران را می دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/139036" target="_blank">📅 01:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139035">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
بازارهای جهانی هم اکنون بسته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/alonews/139035" target="_blank">📅 01:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139034">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: شماره معکوس حملات به ایران آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/alonews/139034" target="_blank">📅 01:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139033">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
رسانه i24News: ترامپ صبرش رو از دست داده و حمله به زیرساخت‌های انرژی ایران میتونه آسیب‌پذیرترین نقطه جمهوری اسلامی رو هدف قرار بده؛ تصمیم نهایی در آخرین لحظه گرفته خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/139033" target="_blank">📅 01:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139032">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
عوستاد خوش چشم: فک نکنم‌ جنگ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/alonews/139032" target="_blank">📅 01:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139031">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری/سخنگوی پنتاگون: وزارت دفاع آماده است تا در هر لحظه دستورات رئیس‌جمهور ترامپ را اجرا کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/139031" target="_blank">📅 01:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139030">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏
✅
‏ ️فوری/هم اکنون پرواز گسترده جنگنده‌های آمریکایی در آسمان منطقه
✅
@khat_akhbar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/139030" target="_blank">📅 01:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139029">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری/وال استریت ژورنال: ترامپ در جلسه امروز تیم امنیت ملی خود، دستور حمله نظامی جدید آمریکا به ایران را صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/139029" target="_blank">📅 01:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139028">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوری/وال استریت ژورنال:
ترامپ در جلسه امروز تیم امنیت ملی خود،
دستور حمله نظامی جدید آمریکا به ایران را صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/alonews/139028" target="_blank">📅 00:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139027">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/139027" target="_blank">📅 00:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139026">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/139026" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139025">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سی‌ان‌ان: به گفته مقام‌های آمریکایی، ترامپ از عدم تمایل تهران به پذیرش خواسته‌هایش خشمگین شده و این موضوع باعث جلسات عصبی پشت درهای بسته و تماس‌های تلفنی پر از ناسزا با متحدانش شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/139025" target="_blank">📅 00:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139024">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
گزارش شبکه سی‌بی‌اس: ایالات متحده و اسرائیل در حال آماده‌سازی برای بمباران اهداف مرتبط با انرژی در ایران هستند، و این عملیات ممکن است همین آخر هفته آغاز شود
🔴
طبق گفته چندین مقام رسمی آمریکایی، اسرائیل در جریان برنامه‌ها قرار گرفته و با ایالات متحده هماهنگی لازم را انجام داده است. با این حال، رئیس جمهور ترامپ هنوز مجوز نهایی را برای این اقدام صادر نکرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/alonews/139024" target="_blank">📅 00:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139023">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c52236384f.mp4?token=RRdNuH-A8_YDdP7Gzzf0hmSul9OpzwKwpQVENvSpieax9o4xLz4Qqh_egIqhSW3cBlwRRwG_9vLFqye4Grs4udKBH2FW4LA7KhpQmnG01aNMvhCl59glXr5cZAG9jIpnHEs_VRVavaWS5NwUA4U6MJLqPWvJaTEZP5DMCy8weRNDFHpmIq0nn40Ei_xIgvlGrheC1KajzlMd_STxs8Sd329lny1vy8Dje7qtbVMqsHBw95qqwp5_g4iDM7vQtORFSZ82IIUlDYN7d0zfuTDrT3LOma-LJhN_Kr-ZE7qJ-sS4-blaHwr1J43C6Qba55iXL70sgebvHLauALYMgP0ezQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c52236384f.mp4?token=RRdNuH-A8_YDdP7Gzzf0hmSul9OpzwKwpQVENvSpieax9o4xLz4Qqh_egIqhSW3cBlwRRwG_9vLFqye4Grs4udKBH2FW4LA7KhpQmnG01aNMvhCl59glXr5cZAG9jIpnHEs_VRVavaWS5NwUA4U6MJLqPWvJaTEZP5DMCy8weRNDFHpmIq0nn40Ei_xIgvlGrheC1KajzlMd_STxs8Sd329lny1vy8Dje7qtbVMqsHBw95qqwp5_g4iDM7vQtORFSZ82IIUlDYN7d0zfuTDrT3LOma-LJhN_Kr-ZE7qJ-sS4-blaHwr1J43C6Qba55iXL70sgebvHLauALYMgP0ezQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمزه صفوی:
برخی می‌گویند ذخایر اورانیوم ۶۰ درصدی باعث شد به ایران، حمله هسته‌ای نشود؛ این مغلطه است؛ خب اگر استدلالتان این است، چرا این را نمی‌گویی که اورانیوم ۶۰ درصد سبب حمله شد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/139023" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139021">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سنتکام: از زمان ازسرگیری محاصره بنادر ایران، مسیر ۳۰ کشتی را تغییر داده و مانع حرکت دو کشتی شده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/139021" target="_blank">📅 00:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139020">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ درباره ایران: اگر من برجام را فسخ نمی‌کردم، ایران ۶-۷ سال پیش سلاح هسته‌ای تولید می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/139020" target="_blank">📅 00:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139019">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1579fcf7a3.mp4?token=qUr0ypgjxBpepKuOySAsztHOKRKT0q3OeQV93ekQhr963EArUaFdioFakEC6sVWV_xVPxu3WMPqaGEbyNA06W60_oe1Eby5qzYJENGLfIVvCi1x3HkPLMe4x7NzVUZanM9ndq4XnlTkAjeYtokCbnr4Nudl3ZsejBEqcX17crzkyVuYWVMhp4AYstdMTGd238m0DKWs2pGMT8Lf9UEyW_BiVQLXNSgAImxRefWq63jdNrDEnRrRvlQw0WyWfNEpUGbyQlGaIOjQVGxxOhyH5yiOm_wyx5oB5Pm_aN2XL_G_VZChpvr6eZ3mdyyzyh0m412_v50OQ8qWX5l4tufNJWTom-s5-h9NcVGp0QCUKVbPtbLFFhPfPYhNokISkXU1sFMQOqUUhBle7qepB5PWfC3eEyTPz9dxVNvA4KHaX6wDUH1Ukuxzi74QNeYtZm9tqH8XfYmhPx6K2QQf0_mXSFBOeY1_v_KO3YAy943b_I-3dC6wxeEeoaTNE2W89WkNSnBr9jTbj3pPx_kdi3z8svHCK7Kesj3iaCIHNlt3iQCbo-J_XhIz08TCOA69VTHxOZQwJnuUJvuXL3cjZbno0p996IOLVo7-y_0j__Ck-lVSViHX6ekgNDzAeMVBRPGfe7r7bVPcrt8drTBgZKlBLST3WT03MfqNSL48i5MPsSJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1579fcf7a3.mp4?token=qUr0ypgjxBpepKuOySAsztHOKRKT0q3OeQV93ekQhr963EArUaFdioFakEC6sVWV_xVPxu3WMPqaGEbyNA06W60_oe1Eby5qzYJENGLfIVvCi1x3HkPLMe4x7NzVUZanM9ndq4XnlTkAjeYtokCbnr4Nudl3ZsejBEqcX17crzkyVuYWVMhp4AYstdMTGd238m0DKWs2pGMT8Lf9UEyW_BiVQLXNSgAImxRefWq63jdNrDEnRrRvlQw0WyWfNEpUGbyQlGaIOjQVGxxOhyH5yiOm_wyx5oB5Pm_aN2XL_G_VZChpvr6eZ3mdyyzyh0m412_v50OQ8qWX5l4tufNJWTom-s5-h9NcVGp0QCUKVbPtbLFFhPfPYhNokISkXU1sFMQOqUUhBle7qepB5PWfC3eEyTPz9dxVNvA4KHaX6wDUH1Ukuxzi74QNeYtZm9tqH8XfYmhPx6K2QQf0_mXSFBOeY1_v_KO3YAy943b_I-3dC6wxeEeoaTNE2W89WkNSnBr9jTbj3pPx_kdi3z8svHCK7Kesj3iaCIHNlt3iQCbo-J_XhIz08TCOA69VTHxOZQwJnuUJvuXL3cjZbno0p996IOLVo7-y_0j__Ck-lVSViHX6ekgNDzAeMVBRPGfe7r7bVPcrt8drTBgZKlBLST3WT03MfqNSL48i5MPsSJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: در مورد ایران، آیا ایده‌ای دارید - یک ماه، یک سال؟ چقدر طول می‌کشد تا آنچه اتفاق می‌افتد حل شود؟
🔴
ترامپ: همیشه سخت است. ما ونزوئلا را در کمتر از یک روز حل کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/139019" target="_blank">📅 00:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139018">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab4670a68.mp4?token=FQ-qY-uh1ZxC2eQYIf8zOJbLuirEL-zBB-53KI31Xdqeznc7rnWdbXYlVXFc1ipqS1A2YxFn5Mmpxdm1F0vSEucdvOD1yOLhfVBKDn4rmddTB5eqxxITXxkU-G8A9S8e0F-D3-L1X05GENeSK3-yjrQ8kDEE-zzhyCy4RitwWjaPydVMCygXXCzT_yyxWokXcb4MRH-SZk8MjTB0d8y746g02dBA_6fRq6CYoDoDrdZ8E_Ed2zyOtW7dhx7o7CGU3BA44nG6g1Omk8rxig_TGXVk4IbDmOHrjmktDtaZPO4kRxtq69BqWZYxZ2BcMTVY1ec7ye6iv3Y53gGHLYZBvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab4670a68.mp4?token=FQ-qY-uh1ZxC2eQYIf8zOJbLuirEL-zBB-53KI31Xdqeznc7rnWdbXYlVXFc1ipqS1A2YxFn5Mmpxdm1F0vSEucdvOD1yOLhfVBKDn4rmddTB5eqxxITXxkU-G8A9S8e0F-D3-L1X05GENeSK3-yjrQ8kDEE-zzhyCy4RitwWjaPydVMCygXXCzT_yyxWokXcb4MRH-SZk8MjTB0d8y746g02dBA_6fRq6CYoDoDrdZ8E_Ed2zyOtW7dhx7o7CGU3BA44nG6g1Omk8rxig_TGXVk4IbDmOHrjmktDtaZPO4kRxtq69BqWZYxZ2BcMTVY1ec7ye6iv3Y53gGHLYZBvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
قیمت‌ها، به‌جز قیمت نفت، به‌شدت کاهش یافته‌اند. وقتی دو هفته پیش تصور می‌شد که به توافق رسیده‌ایم، قیمت‌ها مثل سنگ سقوط کردند.
🔴
اما ما به‌دنبال یک توافق واقعی هستیم؛ من توافق صوری و ساختگی نمی‌خواهم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/139018" target="_blank">📅 00:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139017">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ: من دوست دارم که فرد بعدی باشم که در این سمت فعالیت می‌کند.
فرد بعدی که در این سمت خواهد بود، مانند یک نابغه به نظر خواهد رسید، زیرا تمام این کارخانه‌ها دوباره راه‌اندازی خواهند شد.
این کشور دوباره ساخته خواهد شد و او به خاطر این دستاورد مورد تقدیر قرار خواهد گرفت.
🔴
مک‌کینلی کشور ما را احتمالاً به ثروتمندترین حالت خود رساند. بعد روزولت آمد، پول‌ها را گرفت و خرج کرد.
مک‌کینلی هرگز آن‌طور که شایسته بود، اعتبار دریافت نکرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/139017" target="_blank">📅 00:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139016">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ در مورد ایران:
می‌خواهید همه چیز سریع تمام شود؟ به دیوانه‌ها سلاح هسته‌ای بدهید.
🔴
خیلی سریع تمام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/139016" target="_blank">📅 00:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139015">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c227c270.mp4?token=LDeR94r-zi16oRo3sxAYAg2OKsIFv3SrurOG480VYC9gPuzNFtF3mIrSBkuCAtgdeNOAoK7Fc2MlEwoYu7DkAFdqj-WprcZ-yVQ35IUPt5EQagbcVCPzcKqtyrU5z_sDR_LrquKb76apdk-p0x6AvbpzwSBriiV6Kp_rQUSgqXBUMCwWTJBKcJs_3zj7mc2ounDFUwbFaAM1zkZMPMxP-3T6MIGLU0vWLFLL9VsqameheB5S7qpuU8ZYCDrG8QgHrHZu-u6Mkpz5o5csELf-36G3DQSo8EVG7KI9ESgCQh6NStVYd6TZVSdHivujmTM88-08USiXp0YNV2-gu8CI1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c227c270.mp4?token=LDeR94r-zi16oRo3sxAYAg2OKsIFv3SrurOG480VYC9gPuzNFtF3mIrSBkuCAtgdeNOAoK7Fc2MlEwoYu7DkAFdqj-WprcZ-yVQ35IUPt5EQagbcVCPzcKqtyrU5z_sDR_LrquKb76apdk-p0x6AvbpzwSBriiV6Kp_rQUSgqXBUMCwWTJBKcJs_3zj7mc2ounDFUwbFaAM1zkZMPMxP-3T6MIGLU0vWLFLL9VsqameheB5S7qpuU8ZYCDrG8QgHrHZu-u6Mkpz5o5csELf-36G3DQSo8EVG7KI9ESgCQh6NStVYd6TZVSdHivujmTM88-08USiXp0YNV2-gu8CI1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران
:
من در حال انجام کاری بسیار بزرگ‌تر از چیزی هستم که گفته بودم انجام خواهم داد.قرار بود وارد شویم، توان نظامی آن‌ها را از بین ببریم و بعد خارج شویم.
🔴
اما بعد متوجه شدم اگر این کار را انجام دهیم، باید نوعی حضور و نظارت مستمر وجود داشته باشد؛ وگرنه آن‌ها دوباره همه‌چیز را بازسازی خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/139015" target="_blank">📅 23:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139014">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ درباره ایران: ایران نباید سلاح هسته‌ای داشته باشد. آن‌ها قطعا از آن استفاده می‌کردند.
🔴
اگر من نبودم، اسرائیل امروز وجود نداشت. آن‌ها وجود نداشتند.
🔴
آن‌ها دو هفته با داشتن سلاح هسته‌ای فاصله داشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/139014" target="_blank">📅 23:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139013">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f9a8262b2.mp4?token=b-MsFzW2PLLdr1Gj8n6HVk-jEb5KYK68EH5eYdpPio_AQosqRCyZYvFhbY2lIiPKwZ7sD1xtv9_4pfqNTBGg3TbfBX4JH3zjJTTvGG2TOaINH-QD0rEKb7sqB4tEzkTq1pQCkIP4asltKVoRxhjB95_-yBtQmoCZJnU70kVjEszRwKdstT4vfmSfhZ2FtkjfA38Cjz516X3JBdRzk3mApAZQvYdDjF3JmgsYC1UILRxO74BIqzY0F_QH5fbAvVdk1MGIIOVIXrLpo8OgvJviDt19drehnqHxXWmpWWCSk5cWTHDjAw0RQ0TSYLP7kTCOBYWDswDi6FOejP5p4HScGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f9a8262b2.mp4?token=b-MsFzW2PLLdr1Gj8n6HVk-jEb5KYK68EH5eYdpPio_AQosqRCyZYvFhbY2lIiPKwZ7sD1xtv9_4pfqNTBGg3TbfBX4JH3zjJTTvGG2TOaINH-QD0rEKb7sqB4tEzkTq1pQCkIP4asltKVoRxhjB95_-yBtQmoCZJnU70kVjEszRwKdstT4vfmSfhZ2FtkjfA38Cjz516X3JBdRzk3mApAZQvYdDjF3JmgsYC1UILRxO74BIqzY0F_QH5fbAvVdk1MGIIOVIXrLpo8OgvJviDt19drehnqHxXWmpWWCSk5cWTHDjAw0RQ0TSYLP7kTCOBYWDswDi6FOejP5p4HScGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:همان کسانی که آمریکا را ۲۱ سال در جنگ ویتنام نگه داشتند، امروز درباره ایران انتقاد می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/139013" target="_blank">📅 23:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139011">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895aff4f9a.mp4?token=q9fTSWibRGQt1BCFJ4d_e5HNEJfO9kxt0X5maRHgxY61vb5YE0UbPpSQ1AeDAir4CAhVP43mDdmdlchTthWdJEfomR8p8T2LlQXPEFJLkybBMjjyUUm5qL7uVCJZCMbJZfsaj8t-YXiHyRLtgcbFvMO_xLx9onN7tYEhWiViza6B8o6kM1cfGxSO1GSaPAXyB0DV7E9WL-DYH4cN2R9wybB4HTAWS_6_mXa6XNigBDRhkiIp-WMnyyGfbH0SpqQZjaJzgWE_g6xu5RDvDP_Fw9qsSyNuRswBz9r1QYprmLGCsZIVB3LJyOUe_-ygxaN_8OuFtYYGbkSOSix8v3rAmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895aff4f9a.mp4?token=q9fTSWibRGQt1BCFJ4d_e5HNEJfO9kxt0X5maRHgxY61vb5YE0UbPpSQ1AeDAir4CAhVP43mDdmdlchTthWdJEfomR8p8T2LlQXPEFJLkybBMjjyUUm5qL7uVCJZCMbJZfsaj8t-YXiHyRLtgcbFvMO_xLx9onN7tYEhWiViza6B8o6kM1cfGxSO1GSaPAXyB0DV7E9WL-DYH4cN2R9wybB4HTAWS_6_mXa6XNigBDRhkiIp-WMnyyGfbH0SpqQZjaJzgWE_g6xu5RDvDP_Fw9qsSyNuRswBz9r1QYprmLGCsZIVB3LJyOUe_-ygxaN_8OuFtYYGbkSOSix8v3rAmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره تعدادسربازان کشته شده درجنگ با ایران:در ماجرای ایران، بسته به اینکه معیار محاسبه چه باشد، ما بین ۱۶ تا ۱۸ نفر را از دست دادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/139011" target="_blank">📅 23:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139010">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5go8SXo632J7s5KfdA089XSLy6itFVzr54SJbUbZE8bwVGAxAvGvJztUanI2rpBiyxYWUSKtYn-0Cjmx_F3JrivXLwDOtsCveoa96rqrmxd0CeunBef-H5IGbBRzoDqLu1mwD3vU7Mf2kuzCEql6V-vh_aRpwAfhM2zMUdxVjJO_pn3cfKD7eLEzoOZdzYwBs0u6RXOk0yaJqxvaEGPr70CEZUpydNy62yTVN-AG8sP_C-XoG1SuD-f7S8grqLL8y1Pj5wwl_HbYrnHfpEskrN7sAkGUCdO6N9VvBQG8zhX6bGMoyqJx_Y-wzzlXORIvEhVlxB6kzjodcRZCpiZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پنج فروند هواپیمای تانکر سوخت‌رسان آمریکایی در آسمان خاورمیانه و در نزدیکی تنگه هرمز در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/139010" target="_blank">📅 23:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139009">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/139009" target="_blank">📅 23:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139008">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ: جمهوری خواهان می خواهند ماگا باشند، در واقع همه‌ی جمهوری خواهان الان ماگا هستند.
🔴
ماگا یا MAGA همون آمریکا را دوباره به عظمتش برگردانیمه که شعار ترامپه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/139008" target="_blank">📅 23:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139007">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-YgduDDtztyO9nbis3JNRPstUkf6Ww5YuqpdCKb9QlT_qv6oy3ZLDduwhwXaRApba3EcZugyRlz9dFV-UB81eLHNZzpLwddjqfPU04m-XC61pjzx8PGUmOSso5eNVhQfkUVCev8-PIrEB5j3XB1X30mwZWkscF87rmTQIvhgJFlCbJ__5UCUwTbQHcF4o2dbfu2luBVP2hN1kxCL8le4dWMJTmEGNipVn0ByXXli7pTgLBPYlk_rVA5jaVV84S-xIpzxE8PCl3hUIW8rJwU5ibxD5vPKDuuNFWQ_Znt_dsZUCUIxO5l3MfVDuv792wXawuBvRiZNtmIhoEnwI9qxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل پس از غزه، اکنون به سراغ لبنان رفته و با حملات توپخانه‌ای، شهر صور در جنوب لبنان را بمباران کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/139007" target="_blank">📅 23:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139006">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نیویورک پست: فرمانده سنتکام یک کارزار بمباران گسترده دو هفته‌ای به ترامپ ارائه داده که در آن خبری از حملات محدود شبانه نیست و روز و شب و به طور مداوم و گسترده و در همه‌ی مناطق، ایران بمباران خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/139006" target="_blank">📅 23:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139005">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزارت امنیت داخلی آمریکا اعلام کرد که ایالات متحده واردات از ۴۳ شرکت چینی دیگر را به اتهام استفاده از کار اجباری ممنوع کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/139005" target="_blank">📅 23:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139004">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
قطر از توافق حمایت کرد و از حماس خواست به مسیر توافق پایبند بمونه
🔴
همزمان گفته باید روی اسرائیل فشار وارد بشه تا این توافق اجرا بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/139004" target="_blank">📅 23:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139003">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
الجزیره: قراردادهای آتی نفت خام برنت ۱.۲۲ درصد افزایش یافت و در زمان تسویه به ۹۰.۱۲ دلار در هر بشکه رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/139003" target="_blank">📅 23:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139002">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
فاکس نیوز: پنتاگون پس از ماه‌ها درگیری در ایران با واقعیتی فزاینده روبرو است. ذخایر موشک‌های رهگیر دفاعی آمریکا تا حدی در حال کاهش است که برنامه‌ریزان نظامی در حال بررسی این موضوع هستند که آیا می‌توانند به روند فعلی حملات تلافی‌جویانه محدود ادامه دهند یا خیر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/139002" target="_blank">📅 23:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139001">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c9e5e82d.mp4?token=K0yuBY5Ugx4xaJUrFOxgoYisPvBrPsa5_mjVDuqjtMPTe52UAbSpO8UiRBoZorW4wAIdz0XHtsv5a0fGC1HOImotD8XBDPaGtei8i1-KH6NUqjyVNGS2l4OwhqpdB0bOR4YGp2uMu6m08lPN4Zu1u7H-xo7aNQ1Z84bFCYHJWBXvpjmYTvFrn-WlzzncGShcpmJV8QDRvoKoC_HWvcVNV6-4gDecOsZr0GxJjgzt3Tdev8LvRnhHRG6Smv2ZDN7XJ53N0gwjAIY87sY80aCAAC5dN11Y7GuFzO5iw0vh3E_k9gI0z9ZKyEyJVNwKdEr6L8PFul-f78Tm3qm5-7Skbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c9e5e82d.mp4?token=K0yuBY5Ugx4xaJUrFOxgoYisPvBrPsa5_mjVDuqjtMPTe52UAbSpO8UiRBoZorW4wAIdz0XHtsv5a0fGC1HOImotD8XBDPaGtei8i1-KH6NUqjyVNGS2l4OwhqpdB0bOR4YGp2uMu6m08lPN4Zu1u7H-xo7aNQ1Z84bFCYHJWBXvpjmYTvFrn-WlzzncGShcpmJV8QDRvoKoC_HWvcVNV6-4gDecOsZr0GxJjgzt3Tdev8LvRnhHRG6Smv2ZDN7XJ53N0gwjAIY87sY80aCAAC5dN11Y7GuFzO5iw0vh3E_k9gI0z9ZKyEyJVNwKdEr6L8PFul-f78Tm3qm5-7Skbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تظاهرات(کودتای آمریکایی صهیونی) مردم اسپانیا در مادرید جلوی سفارت مراکش
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/139001" target="_blank">📅 23:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139000">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78b78ee674.mp4?token=ZsE9_TFeXw47N5aaWJOJnp56ZikOTvwftni3xxnE9du3GPiZSXHysxW88e6pEokDcdZNLnFhEQb9M3Itv9fpFbtURRT9rCRWcZAxnF8YVySn_6KmsmNrWh3mOBiar0c5EKnsO3DPr4UOnUb3i2edsgQZfqg5CfTH1Wnu9e8OYEhnRo-1diMaLZVufTMiS3yuo_kCg7xhYE73dpLtYpG_K5-hwQpv_RdM1Kj2xmNdkahoP16B8tvkjFgAWFEH5N_flMlvdEpAizf2eVl_aI-5mOBjVshTOv19eCxtOqD43GRhWQONrMjds2u39Un2ZKS5MTGZiUdNqXVT9BymYeJS9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78b78ee674.mp4?token=ZsE9_TFeXw47N5aaWJOJnp56ZikOTvwftni3xxnE9du3GPiZSXHysxW88e6pEokDcdZNLnFhEQb9M3Itv9fpFbtURRT9rCRWcZAxnF8YVySn_6KmsmNrWh3mOBiar0c5EKnsO3DPr4UOnUb3i2edsgQZfqg5CfTH1Wnu9e8OYEhnRo-1diMaLZVufTMiS3yuo_kCg7xhYE73dpLtYpG_K5-hwQpv_RdM1Kj2xmNdkahoP16B8tvkjFgAWFEH5N_flMlvdEpAizf2eVl_aI-5mOBjVshTOv19eCxtOqD43GRhWQONrMjds2u39Un2ZKS5MTGZiUdNqXVT9BymYeJS9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پناهیان بعد یه بَست: آقا مجتبی پدر جهان هست و قالیباف هم برادر بزرگ جهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/139000" target="_blank">📅 23:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138999">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
جریان از این قرار بود یه دختر ۲۰ساله پسرها رو میبرده خونه و دست و پاشون میبسته و بصورت ارباب برده‌ای ازشون سواستفاده جنسی میکرده و فیلما میفروخته
❌
اینم محتواها که زیر۱۸سال نبینه/مشاهده</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/138999" target="_blank">📅 23:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138998">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
الجزیره: مذاکرات بین ایران عمان بر سر مدیریت تنگه هرمز همچنان ادامه دارد و تنش دوباره بین ایران و آمریکا، آن را متوقف نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/138998" target="_blank">📅 23:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138997">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
برنهام، نخست‌وزیر بریتانیا، از جیانی اینفانتینو، رئیس فدراسیون جهانی فوتبال «فیفا»، خواست به‌دلیل طرح فروش بخشی از حقوق تجاری جام جهانی، از سمت خود استعفا کند. او نخستین رهبر یکی از کشورهای بزرگ جهان است که به‌طور علنی خواستار کناره‌گیری رئیس فیفا می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138997" target="_blank">📅 22:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138996">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtouiMQY0achwuHNL0WWL58ni2q4yld9b9USoUWam02SJn_G1IEDpSk041eaJfzntX97z7o5--0C0PWVNUY3Il_ijE0ASR4uLiAgTq9SF3A3FuiUODPpeYtoLHgTPoaC08AgjZqAtAynbm_UKj3YbXzUWuOkK_lO4LXAstXqWz8Yb8QQ_AR_vvdjzQnpu4SZ3DJutK0ifdjqiu6ooX52e_ZJy-EtlhgUFlP0qpDezDUwlIkueXUgVrYokGbQ-U7lFuc4RZubtGv3AWDfE88iE85Q32lg48_KCrezGlAvgoxzm2jb6y0XNL9H6jXVzZsnoC1XZlGeto-Kez0XkUey6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: تمام جبهه نفاق علیه من شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/138996" target="_blank">📅 22:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138995">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سه راه ساده واسه پولدار شدن :
🪙
1 - داشتن گوشی همراه
2 - خرید اینترنت و داشتن تلگرام
3 - عضویت در کانال زیر و کسب درآمد رایگان و راحت در منزل ( دلاری )
⬇️
•
https://t.me/alirezakalejii
✅</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/138995" target="_blank">📅 22:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138994">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYd1W1EqYb7v2Qg91qhDKyWn1TapV0ojpw3jpKGxwwcjcKwbO0PqtWFx0jog4fUAmDlcSr4jHkrhFVeyZTRkl9ad1JKrzjtfJ_a79J4e7KVEhXawUgPcxVLqd2XPx9zXoSfo6zu4JalBXNt2Q5-jTjFYangm4vH-4XtfuyLmdWalGRxWLa7dETlfBK3EmCaALfe8xHBXXpjSai6AKT-kB2lH5k1uR3Z4pu7xOqMuA7eMwKfc_3VMvrTp6XA5oc8XPesETvUG2A12UTTIsyXQGjV_86ooYjljyilYNlTrOZyRMZ1MZl9eBc3PPLOJPLUWcYQTaYvq0VD0KPMGwmuOnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علیرضا سپاهی که میخواستن اعدامش کنن و هنگام اعدام سکته قلبی کرده بود به هوش اومده و بلافاصله اونو به زندان بردن تا کارای اعدامشو دوباره از سر بگیرن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/138994" target="_blank">📅 22:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138993">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
نورالدین الدغیر، مدیر دفتر الجزیره در تهران: گفت‌وگوهای بین ایران و سلطان‌نشین عمان در مورد تنگه هرمز ادامه دارد و متوقف نشده است، حتی پس از بازگشت تنش بین ایالات متحده و ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/138993" target="_blank">📅 22:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138992">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
خبرنگار العربیه: اسرائیل برای ساکنان منطقه غربی اردوگاه النصیرات در مرکز نوار غزه دستور تخلیه صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/138992" target="_blank">📅 22:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138991">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
واشنگتن‌پست: ترامپ نباید در مورد ایران به توصیه‌های جی‌دی ونس گوش بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/138991" target="_blank">📅 22:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138990">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27404f83be.mp4?token=gu6z5RJDipdGINHyxdTjkzYyW2Gc1cKyaXVUZL2UfhY9S0IVPc6QF-qKD2iv_Qo9iPXN5wrq5KVeDJJBJIsWCtvdnL3XWAtuOJwjleMlKwzwL035fmbEn9XLA4Ju_pLu-4WanGehDEX0md_vgc2yIIqijZ4zUN3BBzg2-i2VFBn9WWcDOxSQknJpVyB1hJrKzUnHLI6-S75EW0dTr9dnMQcipPEhRfKYE7FrbYVIw0MMNoolG_GVTyiAmYfhOtMRW8OUQCec55Mic624LIwh1dAsNi6gXxKTMGk1Wh_ymxNITVpIA1AMusH28FokXtC9Why2R-84oUXDFKKVepTprQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27404f83be.mp4?token=gu6z5RJDipdGINHyxdTjkzYyW2Gc1cKyaXVUZL2UfhY9S0IVPc6QF-qKD2iv_Qo9iPXN5wrq5KVeDJJBJIsWCtvdnL3XWAtuOJwjleMlKwzwL035fmbEn9XLA4Ju_pLu-4WanGehDEX0md_vgc2yIIqijZ4zUN3BBzg2-i2VFBn9WWcDOxSQknJpVyB1hJrKzUnHLI6-S75EW0dTr9dnMQcipPEhRfKYE7FrbYVIw0MMNoolG_GVTyiAmYfhOtMRW8OUQCec55Mic624LIwh1dAsNi6gXxKTMGk1Wh_ymxNITVpIA1AMusH28FokXtC9Why2R-84oUXDFKKVepTprQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس پژوهشگاه رویان: سال گذشته یک زوج می‌توانست به طور متوسط با ۱۳ یا ۱۴ میلیون صاحب فرزند شود اما امروز ما می‌بینیم درمان به‌خاطر بالا رفتن هزینه داروها و خدمات، نزدیک ۴۰ تا ۵۰ میلیون تومان هزینه ممکن است داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/138990" target="_blank">📅 22:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138989">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
قیمت نفت خام آمریکا در معاملات آتی با ۱.۲۹ درصد افزایش به ۸۴.۶۷ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/138989" target="_blank">📅 22:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138988">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a48f675ec.mp4?token=oesh0_1ko0NeuJqk9JFmLCraGytQtWAjh066X2ChWSYOobLDso-4QE-IguPEdPiZwp0HEby2JcPfa6BExoLNpt4TVEfWTgX_tjCN4QCi-6AJFZfdppl1xQsLqYjh4CAtycMfM7Nj_Ykc8j20oxPEUFPrE09jpxduMszcbECD_9l-IZgOghxAnbG_qQaeEczsxZms_DL1hzEP6_6HIl9oLM0fvMud_rZ5HgxH4anNZuIbmgcCEaZKmfvebw8cNpgNBw7LtaREFHyUCFWDS-PFCZUUS-E03kzp5RPuNoqPYAn7NcwklXpAJeMO_1_8URAaOTPvoQSZSQNwAsl6S4A4Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a48f675ec.mp4?token=oesh0_1ko0NeuJqk9JFmLCraGytQtWAjh066X2ChWSYOobLDso-4QE-IguPEdPiZwp0HEby2JcPfa6BExoLNpt4TVEfWTgX_tjCN4QCi-6AJFZfdppl1xQsLqYjh4CAtycMfM7Nj_Ykc8j20oxPEUFPrE09jpxduMszcbECD_9l-IZgOghxAnbG_qQaeEczsxZms_DL1hzEP6_6HIl9oLM0fvMud_rZ5HgxH4anNZuIbmgcCEaZKmfvebw8cNpgNBw7LtaREFHyUCFWDS-PFCZUUS-E03kzp5RPuNoqPYAn7NcwklXpAJeMO_1_8URAaOTPvoQSZSQNwAsl6S4A4Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراکشی ها  در اسپانیا مشغول غارت
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/138988" target="_blank">📅 21:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138987">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d64e33bb.mp4?token=hgQbIO70H2W_yaVKvPYTg3O5794pbc2IeTPvynIqRLnIKZeFr-j3FXrCuNAwlFHB9MvdqYkGLaafqYyHHGW3P_BCylQrTKzAnvIFb1rzqdRV5nH6Tg-YQ-zTd2q12gZdV06I2p1kSRMfYfPhqHqn9kZhUEjhCwjr23hlZVs808Ar_PpoUOmE95XKCQQGjnLU2bL7GwP7XJxOBu4qIvWtXMQ52XS4sVCd6peSAFEe5BXjAdAtNV4Bk91oF8wTPX2DeN6aLs5Oa9eRh9gDQ2PTSP8zbH3drp4G1RD9tysrYP8mSXMbBCF-cmcQKS7ZQgnRMhtdxe3onMmEj5xeRu33PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d64e33bb.mp4?token=hgQbIO70H2W_yaVKvPYTg3O5794pbc2IeTPvynIqRLnIKZeFr-j3FXrCuNAwlFHB9MvdqYkGLaafqYyHHGW3P_BCylQrTKzAnvIFb1rzqdRV5nH6Tg-YQ-zTd2q12gZdV06I2p1kSRMfYfPhqHqn9kZhUEjhCwjr23hlZVs808Ar_PpoUOmE95XKCQQGjnLU2bL7GwP7XJxOBu4qIvWtXMQ52XS4sVCd6peSAFEe5BXjAdAtNV4Bk91oF8wTPX2DeN6aLs5Oa9eRh9gDQ2PTSP8zbH3drp4G1RD9tysrYP8mSXMbBCF-cmcQKS7ZQgnRMhtdxe3onMmEj5xeRu33PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لیونل مسی: همسرم اجازه نمی‌دهد در خانه با پسرهایم فوتبال بازی کنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/138987" target="_blank">📅 21:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138986">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eba69de3.mp4?token=uChzHHGxbeV_IOxiRDI9S-7SodumLSLDLr_2f8CGMkXyC6HmHC-gQmEHobD04qeLNuV7cx2PHu_8VZL_KcpixxXLCpjtNUORgduna8VYwk31NOGjrLmr2iJPHkYV-Tz5PG6a8b5V8gMsvYYFh3MTx5K7rdSdhFKZ6COXpIkPMUKGI9nFlyfH6wDNkuvkKJX6Ul-A6Z-57M3SiSukvBNlcZJIIr7xZk0RBhxxF77z6I82r00Plm6fj10lxsghu7cnSE4HWL-bxRSta87V-YkjGR2-ef78hKMSJz2K8OxZXDpfkDaj9FiU5K65tSVHpYDeAJzrFrBG2-cTc5p3OlXtWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eba69de3.mp4?token=uChzHHGxbeV_IOxiRDI9S-7SodumLSLDLr_2f8CGMkXyC6HmHC-gQmEHobD04qeLNuV7cx2PHu_8VZL_KcpixxXLCpjtNUORgduna8VYwk31NOGjrLmr2iJPHkYV-Tz5PG6a8b5V8gMsvYYFh3MTx5K7rdSdhFKZ6COXpIkPMUKGI9nFlyfH6wDNkuvkKJX6Ul-A6Z-57M3SiSukvBNlcZJIIr7xZk0RBhxxF77z6I82r00Plm6fj10lxsghu7cnSE4HWL-bxRSta87V-YkjGR2-ef78hKMSJz2K8OxZXDpfkDaj9FiU5K65tSVHpYDeAJzrFrBG2-cTc5p3OlXtWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
احمد ایراندوست(بازیگر) فیلم رقصیدنش با آهنگ جمال جمالو رو پست کرده و تو کپشن نوشته تقدیم به روح اکبر عبدی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/138986" target="_blank">📅 21:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138985">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ef9957d8.mp4?token=tK7qW7oK4iUlu6q102Touau32WeBzaEQS3PGPiNQP1mpB3zeF8SFSsr35v-ppfipUpCoCOLIjQdhCkjAfqN8s2bM57QBE0oGufNHR_n1MF9xlIRnZvAkoDigTEgmCiLJVqGItJaOrt5aEtGsvHlZMnVc1rN3Hhr_usBVHGoot-Oj8eA0b07Dyzmd9stCghXdoDaKLhhtbjB9DAI4c2c63yP5IYCYoLC1s8yBAjX63NvTd_yQjXOIPpklzC2OlLDIxN5juc0WF9ILKSEr01p_VWGzu2zFB0dQ1Cz5OQjEYS1DQko4VfjrUmMfIx9z33OJyvlTfky0UJ2oaQ5wctJO-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ef9957d8.mp4?token=tK7qW7oK4iUlu6q102Touau32WeBzaEQS3PGPiNQP1mpB3zeF8SFSsr35v-ppfipUpCoCOLIjQdhCkjAfqN8s2bM57QBE0oGufNHR_n1MF9xlIRnZvAkoDigTEgmCiLJVqGItJaOrt5aEtGsvHlZMnVc1rN3Hhr_usBVHGoot-Oj8eA0b07Dyzmd9stCghXdoDaKLhhtbjB9DAI4c2c63yP5IYCYoLC1s8yBAjX63NvTd_yQjXOIPpklzC2OlLDIxN5juc0WF9ILKSEr01p_VWGzu2zFB0dQ1Cz5OQjEYS1DQko4VfjrUmMfIx9z33OJyvlTfky0UJ2oaQ5wctJO-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کامالا هریس درباره ایران: حتی اگر کنگره با آن موافقت می‌کرد، من با جنگ مخالفت می‌کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/138985" target="_blank">📅 21:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138984">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ویدیوی یک ساعته کل نشست پرزیدنت ترامپ با کابینه خود با زیرنویس فارسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/138984" target="_blank">📅 21:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138983">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
رئیس جمهور اوکراین: اوضاع در خط مقدم جنگ دشوار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/138983" target="_blank">📅 21:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138982">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ: شیوه مذاکره ایرانی‌ها مرا خشمگین می‌کند؛ آن‌ها هفت ساعت را صرف موضوعی می‌کنند که می‌توانند در ۱۰ دقیقه انجام دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/138982" target="_blank">📅 21:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138981">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
حاکم بحرین خطاب به ایران : حضرت محمد پس از قرن ها تاریکی در ایران به آن عمق روحی، انسانی و معرفتی بخشید، بخاطر تشکر از این کار حداقل دیگه به بحرین حمله نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/138981" target="_blank">📅 21:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138980">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
این شهروند عزیز حرف دل میلیون ها ایرانی رو زده
🤔
تنها راه نجات ایران از دست این رژیم فاسد فقط اتحاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/138980" target="_blank">📅 21:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138979">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
شهردار مسکو: یک پهپاد که به سوی پایتخت در حال پرواز بود را سرنگون کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/138979" target="_blank">📅 21:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138978">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0047000034.mp4?token=ClFO1uGFfhKKQEUBI862hbSyAWKHN17UTWGD1hkmo3Ug2nsmk0Pr16l_kPyc2Fn9oX8EfJE6er9sipNw7H0ZiA7RXPNTIlIGOCIMfASkLPJtqKkwbB3JqKnhwDz4ypHemtvzsorswTRmKXTBnlDCSkznqt5JPZNDtS7PHG_OkOSX1tvhAnJK0Wekyao7Ix57mDsg8ZACBV9RxLhCRavO0nPXIhX17X4harBbwLEfnZzX4HvXRl-NJzRGQ819luPupKadbbw8B7i10PRaFWxT1L2_W3SwXKEV2I7f33eHutj-HWMJGUR6upWofTuiA87z8M1DTagH4bm2mgelwnSTb6Q3HYUUdN5MwraJb6hMTdDYtTZsVwQDzrkERaArmRFwD-jV6OXJCOanfbyO9bXxgHrpbNxJjXGQ-ahAfmbWIgzUFuyss6lP7HH6oOuF1M_SApKVp9KaEVi0amg2Qa8CdTOawgipnCHqehzLU34liPetcgHmvvZk45bABrMCiioqyI83_vDWfRWz05hm5gfEKQhbf3spy2-cRQ-gr2g_7N_5hbGuD2F4cwFxFpA6gTpe3ddXjrI90tgjz2qYhNUWtOZAtw4QQs07FJjCaciJHbIEpbtcq6FQKAPRiJVC4uYuu6NG2_wcTNrSx0Zy0rfJfcMPcjs0cZNrRxWZT_Afmyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0047000034.mp4?token=ClFO1uGFfhKKQEUBI862hbSyAWKHN17UTWGD1hkmo3Ug2nsmk0Pr16l_kPyc2Fn9oX8EfJE6er9sipNw7H0ZiA7RXPNTIlIGOCIMfASkLPJtqKkwbB3JqKnhwDz4ypHemtvzsorswTRmKXTBnlDCSkznqt5JPZNDtS7PHG_OkOSX1tvhAnJK0Wekyao7Ix57mDsg8ZACBV9RxLhCRavO0nPXIhX17X4harBbwLEfnZzX4HvXRl-NJzRGQ819luPupKadbbw8B7i10PRaFWxT1L2_W3SwXKEV2I7f33eHutj-HWMJGUR6upWofTuiA87z8M1DTagH4bm2mgelwnSTb6Q3HYUUdN5MwraJb6hMTdDYtTZsVwQDzrkERaArmRFwD-jV6OXJCOanfbyO9bXxgHrpbNxJjXGQ-ahAfmbWIgzUFuyss6lP7HH6oOuF1M_SApKVp9KaEVi0amg2Qa8CdTOawgipnCHqehzLU34liPetcgHmvvZk45bABrMCiioqyI83_vDWfRWz05hm5gfEKQhbf3spy2-cRQ-gr2g_7N_5hbGuD2F4cwFxFpA6gTpe3ddXjrI90tgjz2qYhNUWtOZAtw4QQs07FJjCaciJHbIEpbtcq6FQKAPRiJVC4uYuu6NG2_wcTNrSx0Zy0rfJfcMPcjs0cZNrRxWZT_Afmyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک جنگنده F35 در پایگاه نظامی کالیفرنیا آمریکا سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/138978" target="_blank">📅 21:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138976">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I96_mMB7xsJ2usUbIMIiSq6-ZsftT7r02RCWLxYJ_DKYneH3QILmv0pQsa8b_ZGx9nk-PD4h2pTy2vAJidSTUA4iNgKSHosh4q8t-4ArRRbrjIVpOHB26jbx5CcMkJ0YIETEZexbTWZ3Td3_rKMI5a9txKtrZE4myuHJdpyuSP9JmlQgiLSBkmvY3h9MogRiCvr31ELCW46RrsCq7mK13AZ4HZkjeTFCfAnYPhvQT4u51cS8fTtrS6PEOuspXOqhl8lqO5YhTS9RKvFfwom9AyMC85xfc8MebhGWHcFhiJVhoT_aiyhV6XUuvzZAkDt8K7ntCV0X3tPTN3qc9i_UzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aqNW2jA1caJsCWjGaplLmDYOP-MZFoxaA9MPV-K4BuiN6mZzOAUPqE0duKEn9EhYlA-Z3GH0_og1eUYk-WjfP97KjpzL_KlUW_aEbJJoIcTzbN6VPIl04S0zC7S0jY0t2BvZIKQmbKGqSBMLyolkZ8VvJVE9fQw464sQIczaXehvRS6jyckD3Q8aFI1wPGuwVfCFMQXWfACV7YlleZXjtt3UQ4GqsYfwMLpJmWJZ-gKEN9BTOYNfI1nFYpvFfPoiGJjeCC6KnJpV15LEh-5xj_1yekIjn2mNNtM8lITqFRhF7cMR-mCi64OiwzffB52tEgBvW_0mHLlWFrmSPLBE0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
درگیری رسانه ایی سپاه و سنتکام
🔴
سنتکام: تنگه هرمز باز است
🔴
سپاه: تنگه هرمز بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/138976" target="_blank">📅 21:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138975">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">➕
حتما یک بار تست کنید تا سرعت و کیفیت رو متوجه بشید
✨
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید
در هر صورت تمامی سرویس ها قابلیت مرجوعی دارن و هرموقع راضی نباشید میتونید مرجوع کنید
خرید فوری از ربات های زیر :
🤖
@Team_express_bot
🤖
@Team_express_bot</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/138975" target="_blank">📅 21:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138974">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فیلتر شکن v2ray اختصاصی
✅
اتصال پایدار و پرسرعت
✅
دارای ساب برای اطلاع لحظه ای از باقیمانده
✅
متصل در تمامی دستگاه ها و اینترنت ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۱۰ گیگابایت — 39,000 تومان
▫️
۲۰ گیگابایت — 50,000 تومان
▫️
۴۰ گیگابایت — 95,000 تومان
▫️
۶۰ گیگابایت — 140,000 تومان
▫️
۸۰ گیگابایت — 185,000 تومان
▫️
۱۰۰ گیگابایت — 230,000 تومان
▫️
۱۵۰ گیگابایت — 340,000 تومان
▫️
۲۰۰ گیگابایت — 450,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 560,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 95,000 تومان
♦️
۵۰ گیگابایت — 140,000 تومان
♦️
۷۰ گیگابایت — 185,000 تومان
♦️
۱۰۰ گیگابایت — 250,000 تومان
♦️
۱۵۰ گیگابایت — 365,000 تومان
♦️
۲۰۰ گیگابایت — 475,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 675,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 240,000 تومان
▫️
۱۰۰ گیگابایت — 275,000 تومان
▫️
۱۵۰ گیگابایت — 390,000 تومان
▫️
۲۰۰ گیگابایت — 500,000 تومان
▫️
۳۰۰ گیگابایت — 720,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 820,000 تومان
خرید فوری :
🤖
@Team_express_bot
🤝
فروش عمده و پنل نمایندگی:
📩
@expressuport
📢
کانال اطلاع‌رسانی:
🌱
@vpn_express_sup</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138974" target="_blank">📅 21:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138973">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9d9e7e72d.mp4?token=oiJSs93hfTJXKC0cMSi0yyYg9S-7X-5BuLpxL5qj7RSpLKe_FL1iYEaExNKN6cQOq24QgoKDHE3MdTgeUSSeQ6FgPm2EHsEf5eSgyjRMTkE-2Cxv9I_kyYiNRJbCLGflgaTZeXS8nb0nhMJdNLbgSlPbOJotYRihcj72cLU5cI-qvTJ14C6VmRneM8_lAdUWkS6hEJJCkY2ZybbwF9o3TzCuH7nSuWVHeu-WdzFuq_zqXU3ZHI_xpqT6h41i9JJnhTvhR2O-WOrrLj2xzJklwFSLK6jzJHhTQfXmM7yGADexyk-aBI9FrjtQeALUDdwFIU6ExZty9mdjxkd0Bvhciw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9d9e7e72d.mp4?token=oiJSs93hfTJXKC0cMSi0yyYg9S-7X-5BuLpxL5qj7RSpLKe_FL1iYEaExNKN6cQOq24QgoKDHE3MdTgeUSSeQ6FgPm2EHsEf5eSgyjRMTkE-2Cxv9I_kyYiNRJbCLGflgaTZeXS8nb0nhMJdNLbgSlPbOJotYRihcj72cLU5cI-qvTJ14C6VmRneM8_lAdUWkS6hEJJCkY2ZybbwF9o3TzCuH7nSuWVHeu-WdzFuq_zqXU3ZHI_xpqT6h41i9JJnhTvhR2O-WOrrLj2xzJklwFSLK6jzJHhTQfXmM7yGADexyk-aBI9FrjtQeALUDdwFIU6ExZty9mdjxkd0Bvhciw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه مواضع نظامی‌های اوکراینی رو با موشک‌های سنگین بمبارون کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/138973" target="_blank">📅 21:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138972">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bi-48Tk2TPgbMlqi-hM_28sh54S2BI-dt73Mova0Y4Vvrcb3svGwIuZDya_0gh54QUNoKLhUrj8pM7BDjUaHDJ2c3zxGMe4i09D12eq0rfbS6B4ZD578SShEIUFzE8TpcbSmke9p1kDQaO3yLku8E4vNKbQLRZNNGrt2e1wgHZO_J3wIBt_QeW5pr0iD1P_EGOYm-tjtAlAsxnfWcZkCWTtXGlZN2xXibLKpd82i5yByYxlQKCnB9JKKVGB4X6BoRKnG3sMkqRh9YoigtoRBCxL_pKR1osB0JanF_BR3EjfzPbRwQrPtzPUZ5qPBBWQrQoXcLTrg0oukwrb2bZ4l4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط بیت‌کوین به زیر ۶۳,۰۰۰ دلار در پی مداخله‌ی آمریکا در بازار ین
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/138972" target="_blank">📅 21:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138971">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
اسپانیا: بیش از ۴۸ هزار مهاجر غیرقانونی به مراکش بازگردانده شدند
🔴
وزارت کشور اسپانیا اعلام کرد که تاکنون بیش از ۴۸۳۰۰ مهاجر غیرقانونی از شهر خودمختار سئوتا در اسپانیا به مراکش بازگردانده شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/138971" target="_blank">📅 20:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138970">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjQCWDxC5OAILqfJoyQCLTH-HyumPupCLq6-_fLNcKCNWnJ5v4LQPX3K926vlayVql4cgSJEWeNebomM6vjMHG2ZI1gS04QcXM-x0NqL15m1ORR0NJbwZWosmQwX7cdNW_UcR0R_HfT1M0UosOSdTn7icZjkRipilC6yuDHJ8FGT3gAiW_xOX4xSb74oKqn8Dgx4wb9thUTHuVLQWlRxq6Exrupy51dHaHEWiGQCPGfp4YNu3xWBhP_nhSolRjJwe501RgX-OGrm7cNUb49xo1bI5Sr1Tla1xBS8NyAu8qmjMmqZVX0HOq8_kYr8P9advz_5lpYmBKcBbKw3_iNbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ رسما از قالیباف و عراقچی تعریف کرد و گفت تیم ایرانی‌ها بسیار مقاوم هستند و من تحسین میکنم اونارو
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/138970" target="_blank">📅 20:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138968">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WSzXNbyvsJs4kNUwAfu_4k-7GFAsTeV5yEr68T_ZSyvl_m10NNP8ke8epa2NrAGESxY1pPrPDddIlMz9MjZUEeC99MSzCEJHUaMaBo87pFuBJ1G-r5jYkmbxxSMDyEiblSwN7ApJjj8T_PkLhcUSOzmEP1tjRXzwbG356eOFF8sAxrZJ2AxZEqtjXA8RjgHI6EOT3B850cMwfUEW5hJqbg5v2HZhQGG_eBV5c9swfjlW7WrcjKlgVgna-o7yAJ_dxzH2od1rz-Mqe1FjHLG3H86c-MIyF5E2bpTmQWygIK4cu2ffzn-RaXLOeqs3utXUlVyrKkBz4HgQh3Kpraq6nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dtf7uvjMqu1LeY3LiOlT0Su8VEwQ1ZgDue7mq6aiMLxceaVrvJjFE-DPom2lwqmSh4BXamFsb6yp3T5ccHJJkL2K5h8P0H7zhuz5duT7i_lT8uYU5Lm8TRgsg1ao-5RCry7k0DXRzji2EZ_VySQXgzIBupt_CFrr2zMJACwJop-4210I2DqjT0_LO_1vvmt3crJ1vHJJGKZdJ2htBqesrJgsP3Om59v4BArysWZEauLxkEe1Pc4jsUMsTdcOBhtomHzPEVIs0HEqma7BYX5GBKoRUG8LdnkN7XLboQTftNpyZCEZkX0kw0mKQ55mDwlNNRNhAxy5IeJsEUtY2o10Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بر اساس تصاویر ماهواره‌ای، روز گذشته یک ناو هواپیمابر آمریکایی در ۳۴۰ کیلومتری بندر چابهار ایران مشاهده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138968" target="_blank">📅 20:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138967">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
المانیتور: امریکا نیرو‌های باقی‌ماندهٔ خود را پیش از ضرب‌الاجل ۳۰ سپتامبر از عراق خارج می‌کند؛ سامانه‌های پدافند هوایی پاتریوت را نیز از اربیل جمع‌آوری کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/138967" target="_blank">📅 20:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138966">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a187554d6.mp4?token=l4R2lXwjVsq3_UpEVoI0vs2HhZCKmhnjCFs4_SqWiYGp-22R_JRu-oJhvWEquMVXpBZ2rPTW39ZJiIukcTzXfHOk9uKZjXzsVZgWq31zi8aGIaYu1b6FPn-JE5Zh2DCl1ZzDRKBmpFA9CavdyGBaZgHn-6dyPfIjuoOpHxOkdBl5344oErHY_d-b4ecVE7fcawWlt_xkIqdMOh3jk4rOswLbTaxi_TyxHnoYNZn90qJj7PWpYfCxVTAv9sfLQQhp2o2mrzi7iIquidChpVtoygbZaLV0LCipzrp6Gy2ZlmkIOTN3HGISOXZfvhD8UNPkZE1P8yXdkxppqEMZltg9NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a187554d6.mp4?token=l4R2lXwjVsq3_UpEVoI0vs2HhZCKmhnjCFs4_SqWiYGp-22R_JRu-oJhvWEquMVXpBZ2rPTW39ZJiIukcTzXfHOk9uKZjXzsVZgWq31zi8aGIaYu1b6FPn-JE5Zh2DCl1ZzDRKBmpFA9CavdyGBaZgHn-6dyPfIjuoOpHxOkdBl5344oErHY_d-b4ecVE7fcawWlt_xkIqdMOh3jk4rOswLbTaxi_TyxHnoYNZn90qJj7PWpYfCxVTAv9sfLQQhp2o2mrzi7iIquidChpVtoygbZaLV0LCipzrp6Gy2ZlmkIOTN3HGISOXZfvhD8UNPkZE1P8yXdkxppqEMZltg9NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: شما گفتید ایران هنوز برخی از توانایی‌های خود را حفظ کرده است. آیا آمریکایی‌ها باید برای این حملات پی در پی آماده باشند تا زمانی که ایران به سادگی قادر به حمله متقابل نباشد؟
🔴
ترامپ: آنها کمی قوی‌تر خواهند شد، شاید الان، اما ضعیف‌تر خواهند شد.بله، مطمئناً. شما همیشه باید هوشیار باشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/138966" target="_blank">📅 20:40 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
