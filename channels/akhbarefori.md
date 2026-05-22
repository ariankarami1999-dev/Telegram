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
<img src="https://cdn4.telesco.pe/file/sls4_Y8LxVvoFGRV2yIDclmH6DNsRiVOirhQu32wfCZa8em1if6SfkNqTaJY_Vl5SSmbJRdZnFfSImrpnATvqC5ZzMOjXnEnbVm6FEwfkEwNCh1_NuqXsQLQqhjGEj2Sf4tItK83DaoniOshtrgRzBgdMu_YqheWy28VswO08M-raLE03TV4APBx1PkhvaEvJod0DHPxefghAFGnD2Ne2drRfjPL1aQGpKMOLwEbWuCRPu-bzuH0PRImV1tx_pIPK-GmP1M5aL5AEiIdZy8g7b4_vn3H6J8dsIvTRHwuX0eSQ6pZQ3Fx_IVucwU_UupHPxYouyCjlnlkdfWDRusFFQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.93M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 06:04:48</div>
<hr>

<div class="tg-post" id="msg-653468">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef66287df1.mp4?token=NVTAH8lDl2CcAC52R4N19OwEtfLTB-plOWBihCQwI_lX3s_qNC__KwFPt7ToHS0FBElcFwQvvMqHMxlzDv-u20pgG_Zco7VtPABZaVcFPV2pKGhU1RvHsl2w9LE8EjMfu4iRem5ov_kdhrYjpwNDfGIEht8HGcLp9DT7eUuh8BjsI8EMZhsgm2vry_67JFJxttoJLmsKGCS_rUpwbpL7ZNSkV7-GHX8OPBC1RQq9fxqR-qqr0EuFms80KIaJn98DrUfu5cjmS6V0igTY6gMG-MSzdd-Ui05dPjd-Hnq826YjvCU00qSHeyoKQ4XpVcImkDTWEpaTXqs86wOmCtI1cok0uS8uLVRBeQSQFghT82UHw4mcZ_5zJCrm7MQIQx089U4aznLKUaazDDpFl7EkM2bwOi1C7ZCEQbRZ2btLsysnJYqW5BE_F4oamKkqoJ53tHem-LRut4p4pS_Ki18wCKW3oqSOT5pddrIQShtLEgwymqzeA7kp9SQ5jqkiVQJccYsRas9xXUrgtwsxtEFjbcELAHVxto6peVa1NVUmF_X9kDTUd7C3KhQ8EEeu-yw2OKSZyJIk9cIlmrVUhr4ywGhFNzoHYgOip38QeOp8YOfGouVEG7kJCHmL8XWf4vtXLvy9LEyBWUQIoPY3Sbk00hl2bEEaDgtvHiqrki9enCI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef66287df1.mp4?token=NVTAH8lDl2CcAC52R4N19OwEtfLTB-plOWBihCQwI_lX3s_qNC__KwFPt7ToHS0FBElcFwQvvMqHMxlzDv-u20pgG_Zco7VtPABZaVcFPV2pKGhU1RvHsl2w9LE8EjMfu4iRem5ov_kdhrYjpwNDfGIEht8HGcLp9DT7eUuh8BjsI8EMZhsgm2vry_67JFJxttoJLmsKGCS_rUpwbpL7ZNSkV7-GHX8OPBC1RQq9fxqR-qqr0EuFms80KIaJn98DrUfu5cjmS6V0igTY6gMG-MSzdd-Ui05dPjd-Hnq826YjvCU00qSHeyoKQ4XpVcImkDTWEpaTXqs86wOmCtI1cok0uS8uLVRBeQSQFghT82UHw4mcZ_5zJCrm7MQIQx089U4aznLKUaazDDpFl7EkM2bwOi1C7ZCEQbRZ2btLsysnJYqW5BE_F4oamKkqoJ53tHem-LRut4p4pS_Ki18wCKW3oqSOT5pddrIQShtLEgwymqzeA7kp9SQ5jqkiVQJccYsRas9xXUrgtwsxtEFjbcELAHVxto6peVa1NVUmF_X9kDTUd7C3KhQ8EEeu-yw2OKSZyJIk9cIlmrVUhr4ywGhFNzoHYgOip38QeOp8YOfGouVEG7kJCHmL8XWf4vtXLvy9LEyBWUQIoPY3Sbk00hl2bEEaDgtvHiqrki9enCI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میلیاردها دلار در آتش؛ خسارات سنگین به نیروی هوایی آمریکا
🔹
تحلیل‌گر ارشد سیاست خارجی: سربازان آمریکایی کشته‌شده در کویت در سوله‌های بدون دفاع غافلگیر شدند.
🔹
صورت‌حساب تبعات این حملات و خسارات، اکنون مستقیماً روی میز ترامپ قرار گرفته و او برای انحراف افکار عمومی از شکست‌ها، به نمایش ساخت‌وساز در کاخ سفید روی آورده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/akhbarefori/653468" target="_blank">📅 04:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653467">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
۱۶ عملیات موفق از سوی حزب‌الله علیه رژیم صهیونیستی
🔹
حزب‌الله لبنان در واکنش به ادامه نقض آتش‌بس، شانزده عملیات موفق علیه رژیم صهیونیستی انجام داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/akhbarefori/653467" target="_blank">📅 03:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653466">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtNEeRzZQQhJioxQ8q3ge0b2ZUaPx6oLInbOgJ1RszqIAkBi78fOOQruB8MerZzvIn8q6hG_MAL_5mf0XB5nzC0k-YrVQOkdGyiSLGFqkyOu9fMEnr-lgF6FrwyGpGoFNw43lFWbTU_1sfztgVU8JIG2UY84lE44w4Cy8B6Nm4rLAvUewYrDWlZrmYdpQ-FU_tSoaLJhqKcVAb5gZbLLXVTk7p1F1_NAsa9F7dAlX6jbjHwOWQiWEp3bTU3KQVhMh9VyiBph0XlrW7ZHeRbdI2osaVFYKVXWwvVkjbvN1dlyV5GWwMrQvtEEjT2lkLMrsCG0uog_wm7cG7Sv3p79OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعویق رأی‌گیری درباره اختیارات جنگی ترامپ در مجلس نمایندگان
🔹
مجلس نمایندگان آمریکا روز پنجشنبه رأی‌گیری درباره قطعنامه موسوم به «اختیارات جنگی» را به تعویق انداخت.
🔹
این قطعنامه را اعضای دموکرات این مجلس با هدف محدود کردن اختیارات دونالد ترامپ در جنگ علیه ایران پیشنهاد داده‌اند.
🔹
نشریه هیل نوشته به نظر می‌رسد رهبران جمهوری‌خواه در این مجلس این رأی‌گیری را به دلیل به حد نصاب نرسیدن شمار نمایندگان حاضر خود عقب انداخته‌اند.
🔹
اگرچه اعضای جمهوری‌خواه در مجلس نمایندگان هفته گذشته توانسته بودند قطعنامه مشابهی را با اختلافی بسیار اندک رد کنند، اما روند تحولات در کنگره نشان از شکاف در بدنه حزب حاکم دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/akhbarefori/653466" target="_blank">📅 02:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653465">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
هشدار بلومبرگ: احتمال رکود بزرگ در نتیجه بسته ماندن تنگه هرمز
🔹
بلومبرگ هشدار داد تداوم وضعیت تنگه هرمز تا ماه اوت (مردادماه)، خطر وقوع یک رکود اقتصادی ویرانگر در سطح جهان را به شدت افزایش می‌دهد؛ رکودی که ابعاد و قدرت تخریب آن می‌تواند با بحران مالی بزرگ سال ۲۰۰۸ میلادی برابری کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/akhbarefori/653465" target="_blank">📅 02:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653464">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaZQa4_ss2xSfj9clRZQnCJa_S6_5ghUL3SljbSbSltZDhO79KSUSKREuIaMz3cMuRuMWD_9gTUdPY4ce8IUcXhoEs3o6NVMxrQSZrc98fOuSGh_XSbOVoGLTn7SP8icIX27YHxmSDUxZrjHgd9vQLoe0YGCsvh22iAr3M2xSNYpVr22Zx85R4nMHJu_tY0Op4ciAIUQ9doayp_97hJpOLFl6YipHWq6x-KyDpCwjbmjeuRXJTlh8N5mrdfyzMT-D2UhHUO5_FJp6xaq9wFj8R3awBfkTOMweOE1MKBiOfgU5mGMUYrydiCFQLkIImjDe40ndm6uhBHMagtcR9XyBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصطفی نجفی، فعال رسانه‌ای در تحلیل فضای مذاکرات نوشت:
🔹
۱. مذاکرات پس از بن بست کامل و رفتن طرفین تا آستانه جنگ با اضافه شدن میانجیگران دیگر و ارائه ابتکارات جدید وارد مرحله تازه ای شده است.
🔹
۲. پیشرفتهایی حاصل شده اما اختلافات و شکافهای مهمی باقی مانده است.
🔹
۳. موضوع توافق کامل یا مرحله‌ای اورانیوم، مدت زمان تعلیق، زمان بندی رفع تحریم، دامنه کاهش تحریمها و نحوه مدیریت تنگه همچنان محل اختلاف جدی است.
🔹
۴. تاکنون هیچ متنی مورد توافق قرار نگرفته است
🔹
۵. همچنان احتمال وقوع درگیری بیشتر از توافق است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/akhbarefori/653464" target="_blank">📅 01:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653463">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPxwwBnaPwmjKaWwcs27XKUOgBcvzEczQ6d67vGAhImgIHxhPIqT6KqI-1l9m_0eCBGahBXVZZW35JTVB0eauIvHIXFfXzaoRk-433xHaFSmT5u8eU_GKt4hTkyvkTxVQJFlm7qaMa-iGM7CylB0HOSEpsODAY7IIzpV5c3FssGPgi2lMorR67DrX_ThoV0xapwfaDksghT7OKWeQeyRBJj_d8LEFrRU_TFe4YY2qZ-9yG_ixX1SDpf1VZUniG2cu7Zzk4u4EpAzsdezoTlEh-zE8sQPbiJt1KIeicaJWA-iwJKIVtCp-ZEJbNGR4t1c2gR-0-0cB7cgaNxWLJc_cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش فیگارو از تجارت مخفی اسرائیل در خلیج فارس
🔹
امارات ظاهراً دو فروند هواپیمای هشداردهنده پیشرفته از شرکتی اسرائیلی خریداری کرده
🔹
این هواپیما‌ها که مجهز به ایستگاه‌های شنود هستند، می‌توانند ارتباطات را در آب‌های سرزمینی خلیج فارس رهگیری کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/653463" target="_blank">📅 00:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653462">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
الجزیره: مذاکرات ادامه دارد/ به دو دلیل مذاکرات به ثمر نمی رسد/ افشاگری مهم واشنگتن پست درباره ارتش آمریکا/ ادعای اسوشیتدپرس درباره مرد اصلی مذاکرات
گزارش لحظه به لحظه از توافق احتمالی ایران و آمریکا را اینجا دنبال کنید
👇
khabarfoori.com/fa/tiny/news-3216870</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/akhbarefori/653462" target="_blank">📅 00:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653461">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/368c47b54a.mp4?token=IvSdkNHNICTpnaYPj0MvzswAQZOoDmDRmdPECIn1zN4lpoLoARLuqGE6LEd_mn3_OUgLnsV_FO8dLj5hOb4JVUN1EzhSiUAwm4ljf_coIY75Hk-UIv0gQkNDUDHG3_mi2GkJTB3cQGvukYzsAwXWN0O5bhPhmg2Z5OpklFpWA4h3n3_lqBbFVc46slnS194cisFFMPkZ6JXbhNS8k7LPvOin6EEoCxpME0KX31OzkIqglIJ7XGPT8FlUFvrIyIQpyTuhTE-_OnIrt1UPKj5AI3Cewfxmv617C0av8ELrJfYUSM_O04b1O9eVK54z9qbPeCItsn2m_k7qp9b4BWqpAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/368c47b54a.mp4?token=IvSdkNHNICTpnaYPj0MvzswAQZOoDmDRmdPECIn1zN4lpoLoARLuqGE6LEd_mn3_OUgLnsV_FO8dLj5hOb4JVUN1EzhSiUAwm4ljf_coIY75Hk-UIv0gQkNDUDHG3_mi2GkJTB3cQGvukYzsAwXWN0O5bhPhmg2Z5OpklFpWA4h3n3_lqBbFVc46slnS194cisFFMPkZ6JXbhNS8k7LPvOin6EEoCxpME0KX31OzkIqglIJ7XGPT8FlUFvrIyIQpyTuhTE-_OnIrt1UPKj5AI3Cewfxmv617C0av8ELrJfYUSM_O04b1O9eVK54z9qbPeCItsn2m_k7qp9b4BWqpAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ارکستر سمفونیک تهران در نخستین اجرا در سال جدید در تالار وحدت، از فراسوی مرزها نواخت
🔹
این اجرا در آخرین پنجشنبه اردیبهشت میزبان علاقه‌مندان موسیقی کلاسیک جهان بود.
دراین‌باره بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3216851</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/akhbarefori/653461" target="_blank">📅 00:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653460">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rn7GghqwW_i2Vp__Sz1r2u-8dxEJMBl5F-5tTJkXKOu-tEzqQmBbzLWoEKLz3BpaTwqOndcWy7q7IpDzlVbw6pdFXsXlEwx_Nl5YecjdIfAybELVw2p-M5lTYE6owAuyg74U8rTjOS0-WQZFsoraVVVIMmy6v2jquGdyTEF_2kem4sxJ1FHTysEcYg3Q9RY9uQWPL-oXxmZy_gwqrK-w_BFXxJNqM6dp40o-ln_-vFnnsEkyYVc5VCVWxDbiPSnh9g4jneIjWKu6yXPUemsgKmEmKSZN30ibGNsZiyt7PhpmtBk_yWRJiMcXCn6JDrRsCOK0cksGQbybjFpXmpQfbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: ایالات متحده ۵۰۰۰ نیروی اضافی به لهستان اعزام خواهد کرد
🔹
رئیس جمهور آمریکا: بر اساس انتخاب موفقیت‌آمیز رئیس‌جمهور فعلی لهستان، کارول ناوروسکی، که من افتخار داشتم از او حمایت کنم، و رابطه ما با او، خوشحالم اعلام کنم که ایالات متحده ۵۰۰۰ نیروی اضافی به لهستان اعزام خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/akhbarefori/653460" target="_blank">📅 00:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653459">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
رویترز: هنوز هیچ توافقی حاصل نشده، اما اختلافات کمتر شده است
🔹
برنامه غنی‌سازی اورانیوم ایران و کنترل آن بر تنگه هرمز همچنان از نکات کلیدی مورد اختلاف است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/akhbarefori/653459" target="_blank">📅 00:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653458">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔹
داغ‌ترین خبرهای امروز خبرفوری را از دست ندهید
🔹
🔹
ایران و آمریکا احتمالا بر روی این متن توافق می‌کنند + جزئیات پیش‌نویس ۹ ماده‌ای
👇
khabarfoori.com/fa/tiny/news-3216834
🔹
ابراز آمادگی احمدی‌نژاد برای مذاکره با ترامپ مقابل دوربین‌ها + ویدئو
👇
khabarfoori.com/fa/tiny/news-3216840
🔹
ماجرای دستور مهم رهبر انقلاب درباره اورانیوم ‌۶۰ درصدی چیست؟
👇
khabarfoori.com/fa/tiny/news-3216695
🔹
شوکِ ۱۰۰ درصدی به بازار لبنیات | صبحانه هم لاکچری شد!
👇
khabarfoori.com/fa/tiny/news-3216783
🔹
چگونه با وجود جنگ، تجارت جنسی در هتل‌های دبی رونق دارد؟
👇
khabarfoori.com/fa/tiny/news-3216745
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/akhbarefori/653458" target="_blank">📅 00:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653457">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
العربیه خبر منتشره از قول این رسانه درمورد جزئیات پیش‌نویس توافق ایران و آمریکا را تکذیب کرد
🔹
این رسانه پیش از این مدعی شده بود که به پیش‌نویس نهایی توافق ایالات متحده و ایران با میانجی‌گری پاکستان دست یافته است
🔹
در خبر پیشین العربیه مدعی شده بود لغو تدریجی تحریم‌ها در مقابل پایبندی ایران به مفاد توافق، آغاز مذاکرات در مورد موضوعات حل نشده طی ۷ روز و تضمین آزادی دریانوردی بخشی از پیش‌نویس توافق است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/akhbarefori/653457" target="_blank">📅 23:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653456">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213f1db8ef.mp4?token=UTvB_TxSpgezEHxtptJ8cByWDYWS0BBwT1NovvDJfimRZooLWUY7500FVi8Ml6KAE0HKRHOli7JCgscNGe4jDZ31Df5pIszDpElEe8VB7of2Nslo3tFoi6vCQOqjr-1E9xvOTutrXxy5AgeaDVcealYvBY5HfsNo8yQZLyIcpMcJxiuPBEQxV-49GT7M03r4XSRpBPiJH8foK617rPkbXghi9eI6MoJD3BxfVltU1LrSlsngQcA4AtK8qvesKw7r5vQbz3StOnIl1sCFi1LnHmyFCSU91IANdSvlo6Pn7QdKFZJ4yuDW7u0vQji4XtojBiykhRQWIBypMJ-4h7ZQ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213f1db8ef.mp4?token=UTvB_TxSpgezEHxtptJ8cByWDYWS0BBwT1NovvDJfimRZooLWUY7500FVi8Ml6KAE0HKRHOli7JCgscNGe4jDZ31Df5pIszDpElEe8VB7of2Nslo3tFoi6vCQOqjr-1E9xvOTutrXxy5AgeaDVcealYvBY5HfsNo8yQZLyIcpMcJxiuPBEQxV-49GT7M03r4XSRpBPiJH8foK617rPkbXghi9eI6MoJD3BxfVltU1LrSlsngQcA4AtK8qvesKw7r5vQbz3StOnIl1sCFi1LnHmyFCSU91IANdSvlo6Pn7QdKFZJ4yuDW7u0vQji4XtojBiykhRQWIBypMJ-4h7ZQ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: اروپایی‌ها چپ و راست برای عبور از تنگه هرمز به ما پیام می‌دهند
🔹
تنگه هرمز سرزمین ماست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/akhbarefori/653456" target="_blank">📅 23:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653455">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3db5c1fc5a.mp4?token=ENTCf7UKIp4TPjdyCFnsChXBLclYtwPHVdcG28TKAI2pmAtm8uHJgfsVhsZMn5HPT5ZDDngsZomBQOWDhjZ8LO26sMjl0a6eDUUrxqx7T5vi6KEl1_dzET7Vu1YdS1HSAoJEuy2uMCHfeZ32b4XEfyhEPo8WsPpGV-x1lCNQ7LZkIr0xqhErfuPRTKxCNXJ6n6coLpWRm0tWbyRj7zMT8BJxDQSjdEMchldtPyAbGluwOIFW83LlC1P3brju7GkQLp1CIloHQI5oIRaXPl20DrE7dIaZv7-7Nl2w8tEL-Y0Z6LgqqjWJl-3MTZbDExEDa7ZxeRas8Wq-TfJKm3sEfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3db5c1fc5a.mp4?token=ENTCf7UKIp4TPjdyCFnsChXBLclYtwPHVdcG28TKAI2pmAtm8uHJgfsVhsZMn5HPT5ZDDngsZomBQOWDhjZ8LO26sMjl0a6eDUUrxqx7T5vi6KEl1_dzET7Vu1YdS1HSAoJEuy2uMCHfeZ32b4XEfyhEPo8WsPpGV-x1lCNQ7LZkIr0xqhErfuPRTKxCNXJ6n6coLpWRm0tWbyRj7zMT8BJxDQSjdEMchldtPyAbGluwOIFW83LlC1P3brju7GkQLp1CIloHQI5oIRaXPl20DrE7dIaZv7-7Nl2w8tEL-Y0Z6LgqqjWJl-3MTZbDExEDa7ZxeRas8Wq-TfJKm3sEfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: مردم تا خون بهای رهبری و‌ شهدای جنگ رمضان را نگیرند، دشمن را رها نمی کنند
🔹
مشاور و دستیار رهبر انقلاب: ویژگی‌های رهبر سوم انقلاب منحصر به فرد است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/akhbarefori/653455" target="_blank">📅 23:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653454">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e2ba597cb.mp4?token=TkucCxDgoaDYyHB-EcNjQGZexioe7_AxlRe0qTlr_4_ClsL_8leYyhkyFWyx2zDzJGhrwX4PN4eYMVnvCVomkun2EdqFttYv5KYxoCtKv6cLUWqg8BxIKCSZrhmjoxi1HQ4Bwxvvh9eGgBNJrmiFQnxgbU49MeEcLCMI_-_bljweXNYoVzNX2LI9n33bMXdzkGxeF9LDOQS8O2fkCTAtvhn9AWZh4d4X3hFZHUVmTs7FBWOqMrDNKBPc67mG4Avna2Mm3s9TSUjf2L_B4fDV0QXWWjjIQTIQDEUvBqw31WRVziYGm0qzlCdGHROvXSulwRTMapRT1AgjdlES5x-3iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e2ba597cb.mp4?token=TkucCxDgoaDYyHB-EcNjQGZexioe7_AxlRe0qTlr_4_ClsL_8leYyhkyFWyx2zDzJGhrwX4PN4eYMVnvCVomkun2EdqFttYv5KYxoCtKv6cLUWqg8BxIKCSZrhmjoxi1HQ4Bwxvvh9eGgBNJrmiFQnxgbU49MeEcLCMI_-_bljweXNYoVzNX2LI9n33bMXdzkGxeF9LDOQS8O2fkCTAtvhn9AWZh4d4X3hFZHUVmTs7FBWOqMrDNKBPc67mG4Avna2Mm3s9TSUjf2L_B4fDV0QXWWjjIQTIQDEUvBqw31WRVziYGm0qzlCdGHROvXSulwRTMapRT1AgjdlES5x-3iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: مسائل ما با آمریکا وقتی حل می‌شود که آن‌ها مطمئن شوند که ما به‌حدی از قدرت رسیده‌ایم که نمی‌توانند در مقابل ما کاری انجام دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/akhbarefori/653454" target="_blank">📅 23:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653453">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a351191c93.mp4?token=uk9HOZt_JVluJNQFL1EqpkC59D0hNwJ6aB6NQsFmEk8kugIBhyzbYG6s6UF46pN6g6KrxXiZtsCaynLv6rs6cQGXFPo--3MJwT2aUHZ8H6D8iSJ4ZFJFsD85w4Cku4EY0YNyXmvp_Khcrt4xLd5ipBV1lkCwQ6owIOKk2oeJPXRPhGwI31zDQ4HzHor3xy1XhnSAouE27XbJx0shtubbiA6LDncRDHm-lciag5C5_XTjtikLLpK6kVKuN_Vgp3l0iyYv3vjfXCtaqWEzls-sPjpxBhOdkyk_KVonZCmyhdkxHKRDeYRWbeV5Fa9T_gUKQNyiB8GL_H77XKfiCSrSDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a351191c93.mp4?token=uk9HOZt_JVluJNQFL1EqpkC59D0hNwJ6aB6NQsFmEk8kugIBhyzbYG6s6UF46pN6g6KrxXiZtsCaynLv6rs6cQGXFPo--3MJwT2aUHZ8H6D8iSJ4ZFJFsD85w4Cku4EY0YNyXmvp_Khcrt4xLd5ipBV1lkCwQ6owIOKk2oeJPXRPhGwI31zDQ4HzHor3xy1XhnSAouE27XbJx0shtubbiA6LDncRDHm-lciag5C5_XTjtikLLpK6kVKuN_Vgp3l0iyYv3vjfXCtaqWEzls-sPjpxBhOdkyk_KVonZCmyhdkxHKRDeYRWbeV5Fa9T_gUKQNyiB8GL_H77XKfiCSrSDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: بحث پایان منطقه‌ای جنگ، دریافت غرامت، مدیریت تنگهٔ هرمز و رفع تحریم‌ها چیزهایی نیست که مردم و مسئولان از آن بگذرند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/akhbarefori/653453" target="_blank">📅 23:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653452">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USkOSpTt0bwbTKjLqVUlcsr5vjq07rsYBvDho37hahljhX8y05INc2gHZlyGOqH4YXbzzywGKe1xxilNrsvlZIln0OCmge8N1IR2t0k0p10jg86uFCyE8XaU1ZYC9Gd1BmzbBNS_Zq25V1cOWAKg9n3YrMdRogD3yQ8mcnB5D59biQa53zOIPeKN8P7vRQf0bzVPNMsjU8aldQVrQ4I642U0_n2iQzs6Eh-p73dPaIfYT51TymUWK80BhqlZYNe_pjxlOPvaXycCDOADmKHPwIG0v6tR9GFdHAdBjE8KcRGSudHhhD0Th6sOQkpSigyfcq5YYMEF0CJp2yIYwpXGcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رويترز: با نزدیک شدن به بحران عرضه، ساعت بازار نفت به شماره افتاده است
🔹
صنعت نفت در مواجهه با بزرگ‌ترین شوک عرضه انرژی در تاریخ مدرن، انعطاف‌پذیری فوق‌العاده‌ای از خود نشان داده و اهرم‌های متعددی را برای کاهش ضربه جنگ ایران به کار گرفته است. اما در صورت عدم پیشرفت در مذاکرات صلح، بازار جهانی ممکن است تنها چند ماه با یک نقطه شکست فاصله داشته باشد.
🔹
بازار نفت قبل از اینکه تشدید کاهش عرضه به طور جدی آغاز شود، موجودی انبارها را به سطوح بحرانی برساند و باعث افزایش شدیدتر قیمت‌ها شود، احتمالاً حدود سه ماه فرصت دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/akhbarefori/653452" target="_blank">📅 23:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653451">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuD22qei9PDUpZbfxBQGMs8SJV4_PffwZke8x_uSVHtLl6JEtC3trVbFbW1SHigvFRU5YAeFF7S64jYEUCVqOSqiB2wtGJ_Ru0WEtTU9OOcTduRJvufOcvfcyvGDV6QBOOGmcoeEDk5X9EYMC09BxsRf43xstp9ShOP3VkSA1MgaJZzPUf1eso01jfnjuqdYNvGlsPJAgqLJ7bx91n-uq94id3chlRKXOMMUpcb1zgkhHcRGflYNKKk1Yizvt4W9tnqk0juoHkjnD-tOUggzRdgXexO80Sej8YilUW0VxN7jABFD7i9FTHfdmS6tawt9mQwafmM-nTOjl93eIKOhzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری برای روز اهدای عضو؛ «نبض ماندگار»
🔹
همراهان عزیز خبرفوری، برای شرکت در این فراخوان کافی‌ست به پویش «نبض ماندگار» بپیوندید و با ثبت کارت اهدای عضو، سهمی در ادامه زندگی دیگران داشته باشید.
🔹
برای شرکت در این پویش:
عدد ۱۲۰ را به سرشماره ۳۴۳۲ ارسال کنید
یا به لینک زیر مراجعه کنید:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از ثبت‌نام و دریافت کارت اهدای عضو، تصویر کارت خود را برای ما ارسال کنید تا در این حرکت انسانی و ماندگار کنار هم باشیم
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_forii</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/akhbarefori/653451" target="_blank">📅 23:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653450">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
واشنگتن‌پست: بار اصلی دفاع از اسرائیل بر دوش آمریکا بوده است
🔹
یک ارزیابی جدید از پنتاگون نشان می‌دهد ارتش آمریکا در جریان جنگ اخیر علیه ایران، برای محافظت از اسرائیل تعداد بسیار بیشتری موشک رهگیر پیشرفته شلیک کرده‌اند تا خود ارتش اسرائیل.
🔹
این مسئله اکنون نگرانی‌هایی درباره آمادگی نظامی آمریکا و تعهدات امنیتی این کشور در سایر نقاط جهان ایجاد کرده است.
🔹
سه مقام آمریکایی گفته‌اند ارتش ایالات متحده بیش از ۲۰۰ فروند رهگیر سامانه دفاعی تاد که نیمی از کل زرادخانه پنتاگون را تشکیل می‌دهد برای دفاع از اسرائیل شلیک کرده‌اند.
🔹
نیروهای آمریکایی همچنین بیش از ۱۰۰ فروند موشک رهگیر استاندارد-۳ و استاندارد-۶ را از ناوهای مستقر در شرق مدیترانه برای مهار موشک‌های ایران شلیک کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/653450" target="_blank">📅 23:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653449">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnwEWS-0tWt7mkKqFP8rAFfvdAzSx3rXMkr8JUcGACTgNBkPCdpM4YUr1CoptniaCabWuehUyo_f5hCQhG2C58tKkdRioMy9vlMaQsUAt5ZjBwWtOJymNN6Ld9y4XYCFeiZV_xGkI5FPZRoAS7TM8xys57k0eZvcIYZ4VcPLUqfbElDQQaWJUsA5242Y-zz0U5IoGMrR-7hp4ro20q45u2PhFFxGxtxS2VDeNL27ohYBWRSC9dFfdi8GJpTeVast85XXwqDrPg93Ji9uHk4Fa_rHSKSwmwPfHUB5jdWqoxqzLsPD-gZkUzvOC_nCFmA00NUzWtx2gLPJLKJzOwvkrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه ژاپنی: ایران می‌تواند با جلوگیری از عملیات تعمیر و نگهداری کابل‌های اینترنتی زیر تنگه هرمز، بدون هدف قرار دادن مستقيم آنها بر این کابل‌ها اعمال حاکمیت کند
روزنامه ژاپن تایمز :
🔹
از جمله وسایل ارتباطی مهمی که از تنگه هرمز عبور می‌کنند، یکی از شاخه‌های کابل AAE-۱ (آسیا، آفریقا، اروپا) است که نقاطی از هنگ‌کنگ تا ایتالیا و فرانسه را به هم متصل می‌کند.
🔹
داده‌هایی که از طریق این کابل‌ها منتقل می‌شوند شامل ویدئوها، ایمیل‌ها، شبکه‌های اجتماعی، تراکنش‌های مالی و ارتباطات دولتی هستند.
🔹
ایران هم می‌تواند خودش مستقیماً به کابل‌ها حمله کند و هم شرکت‌های کابل‌گذاری را از انجام عملیات، چه برای تعمیر و نگهداری و چه برای نصب کابل‌های جدید، بازدارد.
🔹
نظامیان آمریکایی نتوانسته‌اند مانع عملیات ایران از سواحل طولانی این کشور در خلیج فارس شوند و تهران همچنان «توان نظامی قابل توجه» خود را حفظ کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/akhbarefori/653449" target="_blank">📅 23:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653448">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ابراز آمادگی احمدی‌نژاد برای مذاکره با ترامپ مقابل دوربین‌ها
گفتگوی خبرفوری با احمدی‌نژاد را اینجا ببینید
👇
khabarfoori.com/fa/tiny/news-3216840</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/akhbarefori/653448" target="_blank">📅 22:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653447">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
پزشکیان: سر خم نخواهیم کرد
🔹
وزرا و کارشناسان ما شبانه روز سرکارند، بدون حتی یک روز تعطیلی
🔹
رئیس‌جمهور در همایش راویان ایران : برای عزت و سربلندی ایران حاضریم تا جای ممکن فداکاری کنیم و باکی از شهادت نداریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/akhbarefori/653447" target="_blank">📅 22:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653446">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
اسماعیل کوثری، عضو کمیسیون امنیت ملی مجلس: اگر امارات از مکان‌هایی که در اختیار آمریکا گذاشته علیه ما استفاده کند، قطعا آنجا را زیر آتش موشک‌های خود می‌بریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/akhbarefori/653446" target="_blank">📅 22:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653445">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r750vc-gsCsnH66Q8MRueb3o1CBGSYP3MPmrKxPP-3mF4YLdZYTV8NEMLES8C_KRfgzU57XOT_0NAn_wa6nNUhQCfrGzNZfRg9mK8QNOFLIPJwoatZxOm1O12Yl4DXiuVk2JU1ANjltP4smotMnGofx-BXP4bCyPL_RN0uHf5FtUXOKhqMOyxq-S2Da3LX3Pza1lAeJiXlaEiliPtgQTqc-_LYorEGXv3zs54QhD8uZ2fuKgo1_RI62PgoIj0N2izTRmydn-lEHKS3aAxu04Fc5aye9zvO0Q6J8XEc0rNbgoC3ORbSYxbLdsiweYCQw24xpb01fN7yUNjxEd9DK3aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس از ملونی و مودی که زیادی صمیمانه است | هدیه آب‌نبات به جورجیا ملونی | حرف‌های درگوشی پشت نخست‌وزیر هند!
🔹
در جریان سفر رسمی نارندا مودی، نخست‌وزیر هند، به ایتالیا، یک اتفاق ساده بیش از مذاکرات سیاسی و اقتصادی توجه رسانه‌ها و شبکه‌های اجتماعی را جلب کرد: یک سلفی در کنار کلوسئوم و هدیه دادن یک بسته آب‌نبات «Melody» به جورجیا ملونی.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3216749</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/akhbarefori/653445" target="_blank">📅 22:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653444">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BV0bXh0TY44Ff6UqK0AMTrlcN20X-Y-6RkN616Ri_qQTxACQ6KbzdM2aQWTcWo-sbTStXkCsT5A1QxQhjvA9v48AChVlxliSNh2edsVSLEUpwUb91ytEdA1zhJUmWM8G8hDv0TLXz1TpEX2lu3bFgPrQeqULc-7foVx5GNgQVFYMkyENbKYuPDzAHUYfbyJcCkL9xLWrCtJK7PoWYffpLYBzcGFFBDfGdrwvwTgheljgaaV2IA6ou-DyVo77c0FLiCHDMP93JxU7deN2IVqOuIHPkV0X537S5-b8PYyv8WO0YT9oF3kzmXuKPGizqbVel1Na9YWqslCGBEWoVzIGWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعرفه گمرکی واردات تلفن همراه اعلام شد
🔹
بر اساس بخشنامه جدید دفتر واردات گمرک ایران و در راستای ضوابط اجرایی قانون بودجه ۱۴۰۵، نرخ واحد مالیات بر ارزش افزوده یک درصد نرخ مندرج در ماده ۷ قانون مالیات ارزش افزوده که ۹ درصد است، اضافه می‌شود.
🔹
در این بخشنامه نرخ ارز مبنای محاسبه ارزش گمرکی گوشی تلفن همراه معادل متوسط نرخ ارز بهمن ۱۴۰۴ در مرکز مبادله و هر یورو معادل ۱۵۵ هزار و ۱۹۶ تومان تعیین شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/akhbarefori/653444" target="_blank">📅 22:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653443">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 53</div>
</div>
<a href="https://t.me/akhbarefori/653443" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاه‌وسوم
رائفی‌پور:
🔹
0:13:30 آیاتی که به فرمایش پیامبر در قرآن جابه‌جا شد
🔹
0:26:40 حرام بودن گوشت حیواناتی که گاهی حلال می شوند
🔹
0:39:35 کثرت منافقین در ولایت پذیری حضرت علی(ع)
🔹
0:55:25 اهمیت و درس آموزی بالای خطبه غدیر
🔹
1:00:40 نازل شدن آیه در رابطه با پرداخت صدقه قبل از دیدار پیامبر
🔹
1:19:00 دعا و نفرین پیامبر راجب دوستان و دشمنان حضرت علی(ع)
🔹
1:24:30 علت داشتن عمر زیاد ظالمان
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/653443" target="_blank">📅 22:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653442">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromطوسی آنلاین . خبرفوری جنگ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c940235b7b.mp4?token=llSjw0pckQ9TXR9s49kASSdtls6rW1MPZtFTtD4Bh_oOvDXuBqI5zKel4rcFupd1OCX1Z6vvTuq4hI_-XzTe3n_zE5yGDGTgNti3DBia5oimeA55itx4Hc_ZgwIQoKESeTBlqlsVe41Xdz9nBTmCTBTNFhhQoLPXLtnUhF8hX20vmwo3hJ3DWB8n9mDQ1_e1B_f9HZ2TZQZhG_w7B-2LIWs2KBiU8pUuFTiH-MfiDn913nP7te7VV0Hy4IwCeqtYtB7yCICcUPDf4Dhw6tYOXmC0oWycvTD27L9lvX5lhyoybVW7Ry6rha7TOMsrORiWkapz0YC5f8HbJ-paKjgwAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c940235b7b.mp4?token=llSjw0pckQ9TXR9s49kASSdtls6rW1MPZtFTtD4Bh_oOvDXuBqI5zKel4rcFupd1OCX1Z6vvTuq4hI_-XzTe3n_zE5yGDGTgNti3DBia5oimeA55itx4Hc_ZgwIQoKESeTBlqlsVe41Xdz9nBTmCTBTNFhhQoLPXLtnUhF8hX20vmwo3hJ3DWB8n9mDQ1_e1B_f9HZ2TZQZhG_w7B-2LIWs2KBiU8pUuFTiH-MfiDn913nP7te7VV0Hy4IwCeqtYtB7yCICcUPDf4Dhw6tYOXmC0oWycvTD27L9lvX5lhyoybVW7Ry6rha7TOMsrORiWkapz0YC5f8HbJ-paKjgwAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های زیبای جفری ساکس رو ببینید</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/akhbarefori/653442" target="_blank">📅 22:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653441">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv6My12oQyG9i9TG-CSTtfslvBvu7yWOVLhmEaW86Dt2N3JyN9bsErmrOaACCm5uCWa8mmHEbiJnsDsbaoFnMkFA8U3gtmkyEl7FiJyzBf_GoKOw56YuwfvPj6dl9-i9HYw6dOqvmX9IvHdi4U8ZDRpihSqH8_jmOVZKfqhjdq08DtezKN1lTAsBUdyaM5cg2dDUFZyyaneOKL_q1ohr4uKVKo2AkrDwbkjyCOdqkcpQAFS7vg6iLOvdLv59bv_4wwaP4TcOStWahtK1FrT5Z-dEbQndafpK-8i-04MxQDfQBJ-B81uhph9eMjWE6hHIBDAHwqjFujXa8hOy0T_l-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری برای روز اهدای عضو؛ «نبض ماندگار»
🔹
سالانه هزاران عضوِ قابل پیوند، همراه با بیماران مرگ مغزی دفن می‌شوند؛ درحالی‌که هزاران نفر هنوز در انتظار زندگی‌اند.
🔹
با ثبت کارت اهدای عضو، به لیست بیماران در انتظار پیوند پایان ببخشیم.
🔹
برای شرکت:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید
یا از طریق لینک زیر ثبت‌نام کنید:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از دریافت کارت، تصویر آن را برای ما ارسال کنید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/akhbarefori/653441" target="_blank">📅 21:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653440">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HquzXOZKZqObo5aIM1236r_OcrZi6SIGyf80ttwChzzcLqU4QJBEUdUzrdNFvIUK0foyHaK-TuDXq2geXMzZK8oM8miVbeasgCAE1DpnxjDhNS0sDfh6aWU-uewxntaSNGvSO7aqxGcs0RgJImdTbISm0zQv54H2wGvWCYtyjAd_pE68Z_J7CIOXUwY84TBSa_ZMf2oWVhsUczR5XsbfokYe67W65J5k5cN1eP6HnWJ4WAhUoA31qwgDnkvx-CbW-S9RCVziKqcRUqtOJs8DzJ49ioXaYCPzEDmO0uDRxlWppQqFigSCIkW0ZW_yA8MToWO7eF9alY2tpXExfZd3ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اذعان رسانه صهیونیستی به قدرت نقطه‌زنی حزب الله
🔹
اسرائیل هیوم گزارش داد، در نبرد قبلی فرماندهی منطقه شمالی بعد از حمله حزب الله علیه تمام سیستم های جاسوسی در مناطق مرزی وارد یک حالت کوری و نابینایی شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/653440" target="_blank">📅 21:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653439">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bf946ca32.mp4?token=QLyXDbp_WmGNumJRxsmQzgBXdyTNqWzrmGZem45joYMlpYNn3MEUMXpe0W3H-rOC0bOceuyMSiEyJhaE3CKvsujB_DAZpEYPZ4RxRiJgvTjKxoB-rlSdv6ucFaz8kdroOYTdCdHzu6Gh0agipoX5OFKfmSyb3s4fMI_NLE5DQGLgZ4CWN_U9dYfiPjUQ_zwmAkEZ9NsJ4IPl4NgalyNyTtG8VG6hWv1oaNLRjhDOwwuTvrz6pTFAa42K45Yia_cGFy7Glw74ewHzvPJZ2kQfwLxkXdZZEFlMbCQ4vOXyQ7Fv1toHUupUd6x-3J2F2UBW4fbuuo1SpZksnmYwa68agw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bf946ca32.mp4?token=QLyXDbp_WmGNumJRxsmQzgBXdyTNqWzrmGZem45joYMlpYNn3MEUMXpe0W3H-rOC0bOceuyMSiEyJhaE3CKvsujB_DAZpEYPZ4RxRiJgvTjKxoB-rlSdv6ucFaz8kdroOYTdCdHzu6Gh0agipoX5OFKfmSyb3s4fMI_NLE5DQGLgZ4CWN_U9dYfiPjUQ_zwmAkEZ9NsJ4IPl4NgalyNyTtG8VG6hWv1oaNLRjhDOwwuTvrz6pTFAa42K45Yia_cGFy7Glw74ewHzvPJZ2kQfwLxkXdZZEFlMbCQ4vOXyQ7Fv1toHUupUd6x-3J2F2UBW4fbuuo1SpZksnmYwa68agw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر جنگ تمام شود و محاصره دریایی باقی بماند، آمریکا توانسته دست برتر را برای خود حفظ کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/akhbarefori/653439" target="_blank">📅 21:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653438">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCUM1p6TC5_VChTEJpQvlQzu6MDY-83G6MmCr76iXYjGP2sUjBhRX1YPST02Bxx6u6HiUwXOmLY7_G13Mm5k1colGD23ICYdCHZuua_rR0qMbwOpytPdWuXJ3ki_Eg322bgZiZccnhMl6clBbqeaLALZ1uqaYJHOjNylq1c3vWj2x4Cd566iNikGutkJZIOu7sTDW3ezGkaDRnVAvm_MwkbsU6T8QVL9z214phtJRcZUIzo5ww1egufBFHuMr-zGjsAOLof2FamAGTr3Jbzu7sY2j3_vVGM4zwK5IrnbEcisbGA2bDGpoPAq7urF6CjCndutCC6qh67qvrre0eCibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویتز: ایران در حال تثبیت کنترل خود بر تنگه هرمز است
🔹
ایران با ایجاد ایست‌های بازرسی، توافق‌های دیپلماتیک و بعضاً دریافت «هزینه»، کنترل خود بر تنگه هرمز را تثبیت می‌کند.
🔹
ایران در حال اجرای یک سیستم چند لایه‌ای برای عبور کشتی‌ها از طریق تنگه هرمز است، آن هم در شرایطی که کشورها تلاش می‌کنند ذخایر رو به کاهش انرژی خود را که به دلیل جنگ به شدت محدود شده است، تأمین کنند.
🔹
آمریکا نسبت به تبعیت کشورها از کنترل‌های ایران هشدار داده است، اما برخی دولت‌ها و شرکت‌های کشتیرانی این خطر را می‌پذیرند.
🔹
مکانیزم جدید ایران شامل یک سیستم اولویت‌بندی است که حق تقدم را به کشتی‌های مرتبط با متحدانش یعنی روسیه و چین می‌دهد و در رتبه‌های بعدی کشورهایی مانند هند و پاکستان قرار دارند که روابط نزدیکی با تهران دارند. پس از اینها نیز سایر دولت‌ها قرار می‌گیرد.
🔹
وضعیت به شکلی است که تنگه هرمز تنها با تأیید حکومت ایران بسته یا باز خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/akhbarefori/653438" target="_blank">📅 21:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653437">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
واشنگتن‌پست: آمریکا نیمی از ذخیره موشک‌های «تاد» را در جریان جنگ علیه ایران مصرف کرد
🔹
روزنامه واشنگتن‌پست گزارش داد که واشنگتن در جریان جنگ علیه ایران بخش بزرگی از ذخایر موشک‌های رهگیر خود را مصرف کرده است.
🔹
ارتش آمریکا در این جنگ مقدار زیادی از موشک‌های رهگیر خود را مصرف کرده؛ حتی بیش از آنچه صهیونیست‌ها استفاده کرده است.
🔹
آمریکا برای دفاع از اسرائیل بیش از ۲۰۰ موشک سامانه «تاد» شلیک کرده است.
🔹
این تعداد تقریباً معادل نیمی از کل ذخیره موشک‌های «تاد» پنتاگون ارزیابی می‌شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/akhbarefori/653437" target="_blank">📅 21:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653436">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
یک تحریم دیگر علیه ایران از سوی کاخ سفید
🔹
آمریکا، سفیر ایران در لبنان را تحریم کرد
🔹
وزارت خزانه داری آمریکا در ادامه اقدامات خصمانه خود علیه جمهوری اسلامی ایران، محمدرضا رئوف شیبانی، سفیر کشورمان در لبنان را تحریم کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/akhbarefori/653436" target="_blank">📅 21:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653435">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4I63IiRfQCRxn5mNKgwUbI9myEJNBgfo910iewzt_Ysoz-zOnCSZMHA73zzWYaqDtnZC5SgfoqoACU-N-oSVkOpTof0TaaIF1VXP0hdbXGd6i9p3Ym95uM8BfQ8F_NRl2hxUofQtsW_G5rda0K9MfWCKIomU_NdaEBPOqu3BQPttUA7MZb9R7MvZY25RpPr24KFRnxFIyZxeMP4EW4LRw8mgNBE-bAzPGwOPkP7IVKfPsxVN5oTOl9D852iZoD1rcl0hu756wcwRsM1TTowym32kp29QYJqa46G-oi79zQPeqCoz1o2ME2HHxQKyrXy2B8XWRZrtJSszqCFVAY9cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فایننشال تایمز: بحران خلیج [فارس] احتمالاً تازه از الان آغاز می‌شود
🔹
کشتی‌های که پیش از بسته شدن تنگه هرمز از آن عبور کرده بودند، تاکنون عمدتاً به مقصد رسیده‌اند.
🔹
اما از اواخر ماه فوریه دیگر کشتی‌های حاوی نفت، گاز طبیعی مایع، مشتقات نفتی، اوره، هیدروژن، هلیوم و... از تنگه عبور نکرده‌اند.
🔹
تا به امروز، کمبودها عمدتاً ذهنی و فرضی بوده‌اند؛ اما با کاهش و تخلیه ذخایر انبارها کمبودها واقعی می‌شوند.
🔹
از این پس، جای خالی محموله‌هایی که حرکت نکردند، به شکلی فزاینده‌ای احساس خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/akhbarefori/653435" target="_blank">📅 21:30 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653434">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd4e2eeed.mp4?token=SVKU6t6HDeIHA5ytNnNlzaYdlTMhLPWo3jlexiWngVS-_FqrBBFVVIobg_y6cghTTNUes6UF7cw7Mig-o2OP-xRmnVh5FSm5Id2K3kFcKglaZfeIrD9QmIo3wMA6Ubbs2rsxCmHGnAFKaQ7gyDSiYZR7APVVCylIXScb9v6ZH0w8EquKFF0LIGAESZZ8pmYEAji7x5GafV6CsNYC26Cqk29d97L6VJHoUrZ31aKFsKcySJxMHN6OvQyVLn8DdcXzYGB-sy0V8VUfBTg4AA10jlb2pc_0lM-Oq9fOlMMNxCaEsIg0Cp7S1gjwfs_M_EgLOtnRrKDLqqjM-bZiK6Q4ubRPpGIFhWK_3zDL8R2j_UaGlukgKlIJRiExwfrXAPTOKtEaUGl7bcaYsJ70IpPOPjq0ZUlC7CrzNtdoCZ86JUUzxAZG0uySDtO2nxPgsVzm6mmWBljqRXRUyZYVe7Kf9QtWd3qvf88Qmb_5MaO5_-lIoi_SWxPy2o5hHiV4jdwIRVlmQZoN6NF8toOfYf_awHUiXHNfAmoDPEMs7s4EOq9vsTPVOoFwZvnqJrKg9TGvDNalI2_peII0K3aefjuZ4ECno8W6_W3hWdk9_rRCKUf2oW0IgQFOnf7RgNFZRtFuCyQUXmLdrdMLWmfN1scWkR3uwL5OoTzL5trkSNfJnE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd4e2eeed.mp4?token=SVKU6t6HDeIHA5ytNnNlzaYdlTMhLPWo3jlexiWngVS-_FqrBBFVVIobg_y6cghTTNUes6UF7cw7Mig-o2OP-xRmnVh5FSm5Id2K3kFcKglaZfeIrD9QmIo3wMA6Ubbs2rsxCmHGnAFKaQ7gyDSiYZR7APVVCylIXScb9v6ZH0w8EquKFF0LIGAESZZ8pmYEAji7x5GafV6CsNYC26Cqk29d97L6VJHoUrZ31aKFsKcySJxMHN6OvQyVLn8DdcXzYGB-sy0V8VUfBTg4AA10jlb2pc_0lM-Oq9fOlMMNxCaEsIg0Cp7S1gjwfs_M_EgLOtnRrKDLqqjM-bZiK6Q4ubRPpGIFhWK_3zDL8R2j_UaGlukgKlIJRiExwfrXAPTOKtEaUGl7bcaYsJ70IpPOPjq0ZUlC7CrzNtdoCZ86JUUzxAZG0uySDtO2nxPgsVzm6mmWBljqRXRUyZYVe7Kf9QtWd3qvf88Qmb_5MaO5_-lIoi_SWxPy2o5hHiV4jdwIRVlmQZoN6NF8toOfYf_awHUiXHNfAmoDPEMs7s4EOq9vsTPVOoFwZvnqJrKg9TGvDNalI2_peII0K3aefjuZ4ECno8W6_W3hWdk9_rRCKUf2oW0IgQFOnf7RgNFZRtFuCyQUXmLdrdMLWmfN1scWkR3uwL5OoTzL5trkSNfJnE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت پرده عقب نشینی ترامپ از حمله به ایران
🔹
همکاری تسلیحاتی ایران و چین وارد مرحله مینیون‌ها شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/653434" target="_blank">📅 21:30 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653433">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gF89unhyjmxx2QuysMei-OkmjuEHXNeHfi6BF-vsC6Sm5U1Rucf7NwKNbQFEIvJsYKjaVH0kUBRDu5xm1WILaUTgNQvenIvVYFuLGbJSUek8MkfvnQIJA7zU3sE_Q4sGPpzPNKJ3IwgrqcZuiCHp_IytNn7-LF3K8yNQF1ybfT6xx6yMm0gbIDI4brYdxjREDc__lXJIF_m8sI2cvm21THxO-6GEZE-Gl7t05s4K96z9N8dGoMz7_5IkRVSFFCmJ_w7kKOvmlZpF6Rg_4Ts1MXt2e4_Qyimwy-VvIRoM3FqroLp-aFtJeYwEcKjjs3w7vse0pVwtfqdf3zJQNBzHRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان اطلاعات سپاه: جمع بندی نهادهای اطلاعاتی آمریکا این است: «گذشت زمان به نفع ما نیست و برای رهایی از مخمصه چندلایه، ابتکار و تهدید ایران را جدی بگیرید.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/akhbarefori/653433" target="_blank">📅 21:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653432">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae5f4c459.mp4?token=h_YaeDy_wh1COlaD2p_DwFrhvQKspT3s_wqZ_U-eIfi1R8Yh9C8xLwCQZswZqvJr0cWYWN7Z12a_PIMOhOJTkSpvX_Vg95IpdebNl1IcaGtNTSApjVvZT8n9-OfdXSOylpSPP46_G0kPwD1fplkUEenOAfs7AyAs62NygVlpk1UC2i34E-l1UWNi4cWdFpHabNdG-hf5jhCw1fjHWVasi39-q8tIGGs8z_tCIm9G4Db1ituyE2jCENq51cR2YByoyOnsPgpHYKZF7T9AUzwQOqbiQWHj5iGt_GEnZeKlcrLC3Yd77iHYQauJW7-hUuuG9iQEze3n3MKEUy01XACvkI1B_lYZJnYRrkw825jKuFStg8gb6S3tbJlLh4gd2qTOqwocfABIEJgach4lwgFX8g0vqJvU68n9zC5j_thTBj_JECUr21vQvBJkFwMb1rYfi7fvBcabIy04CPflf8xVs84VGJ5fgTegKt1G2mKupRciCgS81D2MidYIKU3B4taFYnDGdX5cCn60q5ytRTChohnG04JOZuN5El9QG3xMda_hb0XspD4xtNY-16TSRwOUrdfHaTn-JybywTTXmhbSsA9-gepqJ3M8YEVdcjf-rU8rqRucaLShvwkrSOeQEqLKHlCQEFtrAKcKqvuRK-f1C48DfigNt8hnHnZiqHyoSwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae5f4c459.mp4?token=h_YaeDy_wh1COlaD2p_DwFrhvQKspT3s_wqZ_U-eIfi1R8Yh9C8xLwCQZswZqvJr0cWYWN7Z12a_PIMOhOJTkSpvX_Vg95IpdebNl1IcaGtNTSApjVvZT8n9-OfdXSOylpSPP46_G0kPwD1fplkUEenOAfs7AyAs62NygVlpk1UC2i34E-l1UWNi4cWdFpHabNdG-hf5jhCw1fjHWVasi39-q8tIGGs8z_tCIm9G4Db1ituyE2jCENq51cR2YByoyOnsPgpHYKZF7T9AUzwQOqbiQWHj5iGt_GEnZeKlcrLC3Yd77iHYQauJW7-hUuuG9iQEze3n3MKEUy01XACvkI1B_lYZJnYRrkw825jKuFStg8gb6S3tbJlLh4gd2qTOqwocfABIEJgach4lwgFX8g0vqJvU68n9zC5j_thTBj_JECUr21vQvBJkFwMb1rYfi7fvBcabIy04CPflf8xVs84VGJ5fgTegKt1G2mKupRciCgS81D2MidYIKU3B4taFYnDGdX5cCn60q5ytRTChohnG04JOZuN5El9QG3xMda_hb0XspD4xtNY-16TSRwOUrdfHaTn-JybywTTXmhbSsA9-gepqJ3M8YEVdcjf-rU8rqRucaLShvwkrSOeQEqLKHlCQEFtrAKcKqvuRK-f1C48DfigNt8hnHnZiqHyoSwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظم ایرانی، تثبیت قواعد در بیش از ۸۰ روز ایستادگی در آب‌های خلیج فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/akhbarefori/653432" target="_blank">📅 21:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653431">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
رد گمانه‌زنی‌های رسانه‌ای راجع به جزئیات مذاکرات مرتبط با خاتمه جنگ
🔹
سخنگوی وزارت امور خارجه درباره فضاسازی‌های رسانه‌ای راجع به مذاکرات خاتمه جنگ تاکید کرد: هیچ‌یک از گمانه‌زنی‌هایی که در روزهای اخیر راجع به ابعاد مختلف مذاکرات مطرح شده قابل تایید نیست.
🔹
در این مرحله تمرکز مذاکرات بر خاتمه جنگ در همه جبهه‌ها به شمول لبنان است و ادعاهایی که درباره مباحث هسته‌ای، از جمله موضوع مواد غنی شده یا بحث غنی‌سازی، در رسانه‌ها مطرح شده، صرفا گمانه‌زنی رسانه‌ای بوده و فاقد اعتبار است.
🔹
اطلاع رسانی دقیق راجع به جزئیات مذاکرات توسط مقام‌های رسمی صلاحیت‌دار و سخنگوی هیات مذاکره‌کننده صورت می‌گیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/akhbarefori/653431" target="_blank">📅 20:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653430">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
دوران اعتماد به گفت‌وگو با آمریکا به پایان رسیده است
🔹
رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس: ما اکنون برای هر نقشه‌ای آماده‌ایم، هر چند آمریکایی‌ها برای آنچه در انتظارشان است، آماده نیستند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/akhbarefori/653430" target="_blank">📅 20:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653429">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
اقدام خصمانه آمریکا علیه حزب الله لبنان
🔹
وزارت خارجه آمریکا در ادامه اقدامات خصمانه خود علیه مقاومت لبنان، تحریم‌های جدیدی را علیه حزب‌الله اعمال کرد که این تحریم‌ها شامل چند نماینده پارلمان لبنان نیز شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/akhbarefori/653429" target="_blank">📅 20:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653428">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84f78c0103.mp4?token=eHfTor_wximiKoDXhmI_BHLSholJA6OoRs2R5IxqOYFvFtlH_SEYCCHdpD6gGo4k1MFNQ0iIAQ2rD10wBvSbv_FMFTAZDTkEiJYEutdQdwZ2WHNrqQf-s8cJ1h4IIh5URFIRCPvtIqM8ZH5cJCbBPqOJf9cM7s9b_3RYvPnoyZrviVuLl3SdYqMPHOo0Ex5udDMst-ww6HmG2HkWS7YsUTlo-tuX_NcARdsFoesPw4kinEZ_bCC1zAdBk7GgK_5osAkL-V-TvzSNE7dZhDGh-sxaTo521nazWdxG9WBrNcsFpND96mXVZKklp8oT_isVCXg6CSmzuQpBPRFPbHhP7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84f78c0103.mp4?token=eHfTor_wximiKoDXhmI_BHLSholJA6OoRs2R5IxqOYFvFtlH_SEYCCHdpD6gGo4k1MFNQ0iIAQ2rD10wBvSbv_FMFTAZDTkEiJYEutdQdwZ2WHNrqQf-s8cJ1h4IIh5URFIRCPvtIqM8ZH5cJCbBPqOJf9cM7s9b_3RYvPnoyZrviVuLl3SdYqMPHOo0Ex5udDMst-ww6HmG2HkWS7YsUTlo-tuX_NcARdsFoesPw4kinEZ_bCC1zAdBk7GgK_5osAkL-V-TvzSNE7dZhDGh-sxaTo521nazWdxG9WBrNcsFpND96mXVZKklp8oT_isVCXg6CSmzuQpBPRFPbHhP7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی مهر از مدرسه شجره طیبه؛ میناب هشتاد و دو روز پس از حمله جنایتکارانه دشمن صهیونی-آمریکایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/akhbarefori/653428" target="_blank">📅 20:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653427">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccMJVd5g0dcMIAtbW3Cp6Jnd40Nqmi4-uwSYnd2T1Kv9MiSTiWGMPmeOWuvu9doMFeoG88wti3vd9mmk9_QtyCj-k9Xx8IGpxdUNGzjFck3dhOg4pIl3_Y4uC3jUflHu94tU_bYUfjnuS9Tpnx3ieBBVAvncCyo815ow_t-BMCmndGgGzuMdsJYbyDXtJ3eTMXFtd7jmjDST1p1oQZkBQrQ1MqN_cYewwLTRQfhhDAPie1n9jnPGPkZzVHdmq6UyxffzQzPlIpfEF_6iMjcrBIP6zoE_oVe7PUAkS1Z1GPPYKCcjg_eu7NOfeRz20YBj_WXPthWLTGFig14gUai_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: ایرانی‌ها خواستار عدالت برای شهدایشان هستند
🔹
مردم ایران همانند مسئولان، حملات به مراکز آموزشی را «یک جنگ سیستماتیک علیه بشریت» می‌دانند.
🔹
با حضور در هرمزگان از تداوم سوگواری مردم ایران به خاطر جنایت متجاوزان آمریکایی در مدرسه میناب سخن گفت و تأکید کرد که از مردم ایران «فراخوانی برای پاسخگویی و عدالت» برای کشته‌شدگان شنیده می‌شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/akhbarefori/653427" target="_blank">📅 20:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653418">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JYwDy5EWyFDTyplNz_1l4yiE1OEoK4UjU-Bp8Lnic4CCGs2RaS1idb8flWX8RXMlLLDTN8L-k7Mx1-GXKA9UJqMXeK3j2Sa2garwpmiRbjkzWDM1zCeh8m6385HIy8WKF2Qvicq7qkug3Ge8iiNONsMPdOq8k9CrhkK42L7bCwh4WvhX7SKTjZL-JntJlnlesoRjTpEuliu4q1EiT-z0anHw1_COMNAcgCezWLABKwBX6vIyESldtVg37CvnDYtNwQJL0zGpBqLFMkPoPpee15XpKh6qA5OWjpsn5tBTrb_QjnB2di-8hEF16lVW-R513SULPs5ZrMRmFFyonlhS0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANvfznzenUOuKrDv2Iss2EJcqCeTjARqbikGOfHWL05QWtTVFfSzJcwkCHDaV_E5ko5srO3_jCrHGVzf8G5cIchdGQtP_DtzAJXkU8xufq6-HZLX-8e51099ZUz6l2nNtJ_Uuc9WKiB8syT9Lkb10pOzSnfmiADCoyuZqISFJYw_8b1zdQ1dJBTwnPu_x8CxsvvBU39i6NqEWP8CdYL5Zp4z8JXyo5FMyXoDmbGSGjKeo53Qx2cMkNrxe5VX3lW5jNYIhukiXRSObfWOowGjYuHTo7YHAgKKwHK_BM4121hnPeqhXarnHpTR5UkdIdoFv_H2kpB4jvdzETdFMMuI4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BhF3RYkzDR4CJjjV6VmHRSzPgNspF1GpsHNZ3BdNQ4HRXaXPsIitqvpqxSj_o5Sv5aLENZ37UDqwqk6-8VOwUcyyZ6EhRe1-RHFERaDVcSQ_GsvfkQQTbrd4dvWJ8LtmlBTADwNQKxv-9ECzrDqMJVfcVeH3tpFP8hysz2l0iWCEbpEgX7htK3V9YTVuAMbMkxoV3m1Db32Kz-s46im4DSU3jUxd8C4iTRl-qeZBj0stL6Lj7ox12l6Iw6Tb1R07LCdGblCv6xCVKIiqEEfJ96RKDxyiM74VFjsWJHSro3p2GK7Glkre1dCkvGfIp8JcI9JLllRnpd5aZUK0Ek2Msw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfjPfNqzmFgEoG4_Hn5390djkbzrKw-pzC7x37ZsWn5fu3W_qsZh37fMpZbMwTjiZytlTUTnwdzjN8b4i4Onf_8J8x0kgY45i6JohVPVwmuQhABX7sHp2sdasmEAi39sGpJBJrPZjjAEv5wQGuWf2o7h-3EcwmxgJt-RKo09nKXgbpWH5lhFceWRuTWn0OFmusg9MxjeOFnLZqj0tn3UBmCsxbgn7H19xUXU3NxxD8sgZdjc5Rvghhi4ZS4mHYcizDmsGvHIPlMu2JqiLImPP6rsrWftpZipk4mEPXGi4dj8KsNnrW1X_7JihweIyAsA69AMyzUeZP8Pbx26Kt7pSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njEBMt0bx_QWMXd5yAwHtv8r8E7BijmmAvmTNMZ2at4eJJvJaIaUy5dJkzb-KHXHphDbGCEfRxQ0eAcwTZNg4FlqMRTWWsX--UfiW4oeti2SUAJ5_tO09TeiLHB4vUaX-O_SWwVluOje65-bLif4pap4iafgleF13rnhMPXMaFA9RxM3zU0VgtJyg-hYhYJPDMU_UCDxSTF10vx3HMtNiWYLg-vfYEThLYtLVxyLxc25jJnadTtLnLEjC65xuXbruUrF9Ons6C4vv9njokK2Bo7VULKWt_T5rBtjmxk3iEf1QajR9Q86PIut6xX_ZVhzv4oQsHGnfoA9YWsJPskgcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYyw7ZBWQHY0vyp_6vK3Gl45VINSg-IXTkAJYqo_ObKBP0tdPSoWOEtaG_X1oJ95GnsIvj_oO2zl5VxDxXmcUxbIw7hkxLMRjB9frhTzgoaNQkS8SJgOgYESnP7mTT77ccbvfy_6fWZ2hk0Z5Ju4rC8ja3k8yrmVamrNoNnCZi4GOidtG-vSFKq2hvKashdsBGTkLDUdTK6fB-YNz7Razlxva0IK5_2MIGRrRKtM4AXdgP014WeguXxxeR9yJ3p6-_sZQeb24K-y_XGohtDeItnOpg-JQhCS2fE-A9QthFfTCSpW6iqZakvSjhK1iGDWbbNCMfAsbhqQdjgn4TNpZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APmV8wmlSUEjrhSc6YqNS_fBETFZJSs5Sn1z7qNL_zbb8T5mfw9dAeqE5M7R-xS3ZKrQjuHfQ0kfF6lM0ASCWH9rGf4vYTtLHJzVvo0Ejlgk_LX-sOawnRApAKGPPj65i48XOeBe8DpzyIjoJT_p35hc5V0Mm0k1uhclCJ_TPF70xEOiCCxhv5YUYk66Zo0xgvE755x1KG1QVLD6Sn6ESRaRGmuangqR4MghCSQNr4HOtpJBbdlIZxXNxm2SEE1LGx766AA8S2HvFU7QRvlAmpD4FYwpXiXKT2A2dLtkqoEb9IRP2dixYk6q2m1HIxGpzsRzCKCXauiho7jcTgBCNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3MQvBz3at01cj2Tc3f5OCTaAG7WG29uhex0P6Z4Lvt4BdsAOPJwlKEdLZZR_VUcsYowiaQux-3TZ8JoQNZjiRP18f_ykAFZRG-GOQhCk0p0hmMIK_5CzK_8NNXHO8xxpG4VWadLNVbOuj166rWg2pPDUpHcOU6swqPBRX-BHIRVMJLRQgNBiARLYHmhwNuZ84dCTw4kBcfyjn6NowDWoz3IE3aTP0e9yIDYEs047WTQOdYuhGbij2pWAEkbMN_kuV11oFO0Rk88oji7_qfMc_U0bwEaBV_y68CEk82u4YTBPQC-1Dv1gBOvcxa8HCdveiJPvA2DWjoqYkEScQBFBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت
#همدلی
امروز
💫
امروز هم سهمی از مهربانی در این مسیر جاری شد…
#هیات_قرار
با مشارکت شما مردم نیکوکار، ۳ رأس گوسفند را قربانی و گوشت آن را در راستای حمایت از خانواده‌های ایرانی میان خانواده‌های حائز صلاحیت توزیع می‌کند.
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/653418" target="_blank">📅 20:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653417">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ایران و عمان در حال بحث دربارهٔ سیستم دائمی عوارض عبور از تنگهٔ هرمز هستند؛
🔹
در این راستا، ایران هزینه‌های سنگینی برای کشتی‌های تجاری پیشنهاد کرده و معافیت‌هایی برای کشورهای متحدی مانند روسیه و چین در نظر گرفته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/akhbarefori/653417" target="_blank">📅 20:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653416">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emePojtTjKNGJc0bYsjssutVnxMisn3Xb25Gl-910ie134-P627aAWoE8dbuloLQsskCkz66MV1ochanc-iDRtrX9EvGTusQVtsu71h4Oc4dmXCt4DGpzJlviAn4k7bEc1XKWoivgN6jlP6n5_DtDvnCmyvrkDbjsAIvc4d4SQIfHitwb3eSbDPMe7oixiobpTJfYdaubEdA9hMtBL8qAxQvQSUsKGS7MGFFlEte13WYwzuUKatpsNk3988lX287kMd6Ah6KiV4KSFzqZ8Ns5E35I5KhUg6OyO-LviGldtOVm9qHTPDVjIk9y6hwmAfX5NppHFhDSQqLS8yirqc-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت انگلیسی رئیس کمیسیون امنیت ملی در پاسخ به ترامپ:
🔹
دوران اعتماد به «دیپلماسی» آمریکا به پایان رسیده و اکنون ما برای هر سناریویی آماده‌ایم.
🔹
هرچند آمریکایی‌ها برای آنچه در انتظارشان است، آماده نیستند!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/akhbarefori/653416" target="_blank">📅 20:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653415">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c9573f99a.mp4?token=oy_UkqsLikgyYFD0WZRL-L9NB_Syfsw0oFMKwIRdez7O3Dkmvs7vqmCls7enrhHJdVO-mLRdfcRYzM9BKF7dlONgmdEfXwWfgLxsQdVvhHF16xyJCAHA7AmeBYxcpIXRndMFkE3VE5OYGJU6Gl3EQnNZ6PRgYXinEBPT9HNEihKtvQbrNkZbcXGYlZPsgHC_REkwnCSE6a-riftvjFfgUrE9pWSHqytU_AwQQ0ioPJUMfkzj9fPgtazurb5o5uxy-b9wGagxvjOm3dUrFfwTzKKoVUN4VTS-EH0Y-87BGLjvf4Zznhot9sEWSoV_KBIc096N401lZdmBgY0DurXVtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c9573f99a.mp4?token=oy_UkqsLikgyYFD0WZRL-L9NB_Syfsw0oFMKwIRdez7O3Dkmvs7vqmCls7enrhHJdVO-mLRdfcRYzM9BKF7dlONgmdEfXwWfgLxsQdVvhHF16xyJCAHA7AmeBYxcpIXRndMFkE3VE5OYGJU6Gl3EQnNZ6PRgYXinEBPT9HNEihKtvQbrNkZbcXGYlZPsgHC_REkwnCSE6a-riftvjFfgUrE9pWSHqytU_AwQQ0ioPJUMfkzj9fPgtazurb5o5uxy-b9wGagxvjOm3dUrFfwTzKKoVUN4VTS-EH0Y-87BGLjvf4Zznhot9sEWSoV_KBIc096N401lZdmBgY0DurXVtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: ما کنترل کامل تنگه هرمز را در دست داریم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/akhbarefori/653415" target="_blank">📅 20:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653414">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2975fd5ff8.mp4?token=OHiEvbQcVZS4z5E_wAb5Scfm8aXtJuhi2vTiTap_ZUvXEBkBIIgCF4tLrBzFnF9GMD4x_8Lj3N3y3KPwAgRd_bPSh6GX5scxEM4iIjwCCnc9szp9W9m4uezOYyoxJbZ8j10M7ikCch-FhjBKHx26IUORhRYirk7e22luvr_OJ7gAQgReCJ-lDuRsSwFeS5Oht178ZxIfsPSKJ4ntHhGYFW99VS6oo9vI1cyjyy1kT6sn0h4hZhnFKPONaxMnq2ICcxrWlvQfmRSEidUgK9h5NWDzjDuk1ImzmtQlldMRbApNxh907KtQj5SKh_4byw81x1BPVSmOQDu9Wpmxdfdi_mSquWUb4XjkbleGNoDFJ8r8SAFrGGr7Wq_Zj7ohGeIm-_1Qc4Wn5d-nYhvse7weHtvKUk2QnzFkho5VejUa-yAwfh6jYjq7SoHyTrIv8MT1aiSSjItiRmu1LuZupfyqG-PKbQmUSa20FKWl3WKn_FNrvt_ILIC1nar2NFsMd9HH8kGIlWtwtILKh8xsnQq8d6Ra3QOcBkcxoDlsRd-bsD2nZd0B26gTEawQkufRPa4nbAu_0ekHOXpd_BZT2IpKXvfOnbPuenNEk6LMpqvwJdrvIgCEj2cfpTwwoxGFm3iN-XJh9B3wojFUx9c6F7T5h-WVnE1J-YSIq2qe7Qd3Hbc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2975fd5ff8.mp4?token=OHiEvbQcVZS4z5E_wAb5Scfm8aXtJuhi2vTiTap_ZUvXEBkBIIgCF4tLrBzFnF9GMD4x_8Lj3N3y3KPwAgRd_bPSh6GX5scxEM4iIjwCCnc9szp9W9m4uezOYyoxJbZ8j10M7ikCch-FhjBKHx26IUORhRYirk7e22luvr_OJ7gAQgReCJ-lDuRsSwFeS5Oht178ZxIfsPSKJ4ntHhGYFW99VS6oo9vI1cyjyy1kT6sn0h4hZhnFKPONaxMnq2ICcxrWlvQfmRSEidUgK9h5NWDzjDuk1ImzmtQlldMRbApNxh907KtQj5SKh_4byw81x1BPVSmOQDu9Wpmxdfdi_mSquWUb4XjkbleGNoDFJ8r8SAFrGGr7Wq_Zj7ohGeIm-_1Qc4Wn5d-nYhvse7weHtvKUk2QnzFkho5VejUa-yAwfh6jYjq7SoHyTrIv8MT1aiSSjItiRmu1LuZupfyqG-PKbQmUSa20FKWl3WKn_FNrvt_ILIC1nar2NFsMd9HH8kGIlWtwtILKh8xsnQq8d6Ra3QOcBkcxoDlsRd-bsD2nZd0B26gTEawQkufRPa4nbAu_0ekHOXpd_BZT2IpKXvfOnbPuenNEk6LMpqvwJdrvIgCEj2cfpTwwoxGFm3iN-XJh9B3wojFUx9c6F7T5h-WVnE1J-YSIq2qe7Qd3Hbc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع شهیدِ خنثی‌سازی بمب‌های صهیونیستی در بروجن
🔹
شهید حمید خانی، پاسدار بازنشسته و از نیروهای داوطلبی بود که هنگام عملیات خنثی‌سازی بمب‌های عمل‌نکرده دشمن به درجهٔ رفیع شهادت نائل آمد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/653414" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653413">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
گام بلند برای پایداری انرژی در غرب خراسان رضوی
🔹
با همت وزیر نیرو و استاندار خراسان رضوی، عملیات اجرایی پروژه بزرگ نیروگاه خورشیدی ۲۵۰ مگاواتی سبزوار با سرمایه‌گذاری عظیم ۲۰ هزار میلیارد تومان آغاز شد.
🔹
محمدرضا محسنی‌ثانی، نماینده مردم سبزوار در مجلس، با تبیین حجم عملیاتی این پروژه، آن را محرک اصلی اشتغال‌زایی و ثبات زیرساخت‌های برق در منطقه برشمرد.
🔹
وی ضمن قدردانی از نگاه ویژه دکتر پزشکیان (رئیس‌جمهور) و حمایت‌های دکتر طرزطلب (رئیس ساتبا) و دکتر خدایی (مشاور عالی استاندار)، این طرح را سرفصل جدیدی در توسعه صنعتی غرب استان خراسان دانست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/akhbarefori/653413" target="_blank">📅 19:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653412">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpmWizvfR5EWCAwmMuY_cXzbfiaqH-E4ikpa4x29LBj89M0HV_cRvDpONy7AjBI-MRcZ-CitnfTzg_z_ivYr_GiwZec-xIL12WL07oRmkOJLrXnI68nkg17ZMRAUur4jVg2bVQOIAzHohKwGzdKZgQek-Xd4BIRriyCp86olHOO082dBSTbOvkFyYy4nA_V0GUmlzu2QXk8fvZedbiHFB6-i_nQqnIAOo4seibZaQMOBSbxFp0-7Ciex6P-WPrWAvP1judbTZJAZbmsgmjpyQc4PffKCpQ69a-ZIh7Nn4XoEi2lmLUso7cUzmVeVo9QgIvf8qq2vcEWrNYdyhkLElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علائم عجیب بدن و علت‌ها
🔹
می‌‌دانید خمیازه بیش از حد یا بوی بد غیر عادی دهان به چه علت است؟
🔹
در این اینفوگرافی علت‌های برخی علائم عجیب بدن را خواهید دید.
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/653412" target="_blank">📅 19:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653411">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
روزهای سخت آمریکا برای پذیرش واقعیات جدید تنگه هرمز
🔹
وزیر امور خارجه آمریکا بار دیگر علیه وضعیت جدید تنگه هرمز موضع گرفت.
🔹
روبیو در این باره اظهار داشت: ما همیشه گفته‌ایم که سیستم پرداخت عوارض در تنگه هرمز غیرقابل قبول است.
🔹
اگر آنها به تداوم پیگیری این موضوع ادامه دهند، یک توافق دیپلماتیک غیرممکن خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/akhbarefori/653411" target="_blank">📅 19:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653410">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkStALHbBdv8IQgmJ4f7PtrIT6fj61Ta3FaCu7Ho16nnd_bm5_gX_LPZu21lu0gC6gpS-2DNkzLQ6N1Tzy6KSsHeWkIKHn4GS7s3itUeGhZBe14tRPT19YdKJmFbEMFwSUUT1Qg2CN6cVC0R7dFUjEUNDAusgT8VjpOy0KSVuUCSSnMn5UFf4xn1fmo7C9x3GMO2E4WfVSVul22J09YositvqqKmb2ie0uARyiqcpXMhw3yep73VjVZDAMftVzooAyvL6aq-QAS4XwYQbN1g4613bBpNCBLngFGX8u-0PdY0MsyoKAWBBwHIrA55ljFerfd6CZPxANLt2XBJ1Vvu7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاردین: ترامپ خود را در احمدی‌نژاد می‎بیند/ آنها خیلی به هم شبیه‌اند
ادعای گاردین:
🔹
با وجود تمام تفاوت‌های ظاهریشان، همیشه به نظر می‌رسید چیزهایی وجود دارد که محمود احمدی‌نژاد و دونالد ترامپ شبیه به هم باشند.
🔹
جذابیت متقابل بین ترامپ و احمدی‌نژاد چندان دور از ذهن نیست. این دو نفر سبک ارتباطی پوپولیستی و جذابی دارند؛ شباهت‌هایی در سبک حکومت استبدادی آنها نیز مشاهده شده است.
🔹
بدبینان ممکن است ادعا کنند که این دو علاقه مشترکی به لغو نتایج انتخابات دموکراتیک دارند. پیروزی بسیار جنجالی احمدی‌نژاد در انتخابات ۲۰۰۹ را با تلاش‌های ترامپ برای لغو پیروزی جو بایدن در سال ۲۰۲۰ مقایسه کنید!/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/akhbarefori/653410" target="_blank">📅 19:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653409">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
موافقت وزارت نفت با حذف تدریجی کارت‌های آزاد سوخت در جایگاه‌های سیستان و بلوچستان
🔹
نماینده زابل: از خرداد ماه امسال، سهمیه سوخت با نرخ پنج هزار تومانی به کارت تمام خودروهای شخصی استان واریز خواهد شد.
🔹
کارت‌های آزاد سوخت در تمام جایگاه‌های سیستان و بلوچستان جمع‌آوری می‌شود و سهمیه کل استان با مساعدت ویژه و مقداری افزایش، به کارت تمام خودروهای شخصی واریز خواهد شد.
🔹
این سهمیه جدید با نرخ پنج هزار تومان (نرخ سوم) محاسبه می‌شود. همچنین مقرر شده در هر شهرستان یک یا ۲ جایگاه سوخت برای استفاده مسافران و مهمانان سایر استان‌ها حفظ شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/akhbarefori/653409" target="_blank">📅 18:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653408">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxYD3sU0z-hqZXH3J5aoklxNhtlTQF-S1mXk-7naHww7d367t3cKtlHQc09EX4y5t4-EV6Vg_yXltbQH4NA31ppKU4kRGxUAd5JCYA-x1hqTkk9kCzctPcMVmpX5ksuQeGYJiJu2mGqIeuSgCHPI31J8uTmh2t1omO8HMdt-xBiTC9dZXRaDpjEXOFlJHKk_wj9WyygESXPIMIWAOHUurVkVCHgEXAC4z_i6f88BmVsg39IwN5qQrnt7grolWQ7OPVT24wUhHomvRizFQgFpxI-n4G4Mw8Ogf0OOxC4yHW4CYh7IkC4O75-WSzTDDO1YiHMzo13nc2Fc8nHUvN1P2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پای لانچریم
🔹
رفت وآمدهای دیپلماتیک پاکستان به تهران و بازتاب گسترده آن در رسانه‌های غربی، گمانه‌زنی‌ها درباره احتمال یک توافق قریب‌الوقوع را تقویت کرده است. اما تجربه تلخ گذشته هشداردهنده است؛ هر بار در آستانه توافق با آمریکا قرار گرفتیم، جنگی ناگهانی رخ داده است. جنگ ۱۲ روزه و درگیری اخیر، مصداق کامل این الگوی تکراری هستند. از همین رو، با وجود آمادگی کامل برای هر تصمیمی، یک اصل غیرقابل تغییر در دستور کار قرار دارد. ما برای هر سناریویی آماده‌ایم؛ چه توافق، چه رویارویی. اما این بار، اسیر نیرنگ دشمن نخواهیم شد.
🔹
هفتصدوپنجاه‌وششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/akhbarefori/653408" target="_blank">📅 18:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653407">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j05sZJOWvAZ6947VJeUm-0joQLJniyKJzQz1j9MZe2pwKQZCaoChx2qGVC5E6nPHEz4bUHWtM_LWYLfTKHYFcNYdjdBHwOwoD7p5OKA3s-CQN0nrXmIHkimTFohseKrzpjbW3f3xKT6U9FbYIIrDz1l0ovMlqZi8U0tByNoFwnfa_kG5KJnmq0vHzq7YH6qgHpsTRXl0KD5VtBDxo9LKaq-2-uV7c-ouR5CvNLpDDZd_Z0R4gbRO-m-H95MzT3NX0_uTRed1O4WgHnVvpPVqeysHJYh3eTy-uhgtBIW0_w-g2P-8HWC0DdTNBl55EDLMr7STSIwv0MC1Pu0dol6dZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/akhbarefori/653407" target="_blank">📅 18:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653406">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3516a0697.mp4?token=h6yF35qS6zNZ3I9yljwAR-rthc775BJszYVnNl96jc36g0sWTIDVyVnLAuwvi7yNtm3ey0bTZ7jUkTuaB1d-J6KV2G0R7wIzYCy7upik1F9DGeXoxpC9E0pDxN7gm9xOhzhqseOm2RapHSNoTIsZbKAc9UN64nMDDkUPMXR87MSYNpxBJmeRKq-z58NZnEQTgcZexZlFsy_1kdkN7If_nOp8nul0GQkNLvpxtuQB75ZEvgiydRtT30tSo7VPBta2YgDXR2Epe7cHnev3S1fFauI-a9NP3k3jdSIsQyw1Qnke5lCytqpIvzDqsD2GXTCVj3b6ilw8tb-P0uHoI0_yVTtHzG3JzfRhavJUvJKq4c4ioqdTi2dfNb2a4c7fwrwg3C2W4xIrz_69hLq7tUcFCDp9RnXBYHpoxJQ2PfNW0ASjbX7P9KW2eu_5fQCL7lothO8fjGPYyvIoc73zXKCvLD_-LHLZciFEdqsF9LV0GqRE3t2A5D-HPXIfyDt9z8-wvHzna-xrJEv2DCSNxMz6PJFJwNWEKbfBLpPRlSDHeYwd5DrrDd3y0mTZiptnP8nmlz4dkuhHRPjpWixYLoeLprvZApE-q4ITSGc5mTaz4QXd3epW991znEdKSbCOaO2WZt7gLOMNQ8NmvE1W_6e8l5z_aHUC1EnE_xnsBiLeg8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3516a0697.mp4?token=h6yF35qS6zNZ3I9yljwAR-rthc775BJszYVnNl96jc36g0sWTIDVyVnLAuwvi7yNtm3ey0bTZ7jUkTuaB1d-J6KV2G0R7wIzYCy7upik1F9DGeXoxpC9E0pDxN7gm9xOhzhqseOm2RapHSNoTIsZbKAc9UN64nMDDkUPMXR87MSYNpxBJmeRKq-z58NZnEQTgcZexZlFsy_1kdkN7If_nOp8nul0GQkNLvpxtuQB75ZEvgiydRtT30tSo7VPBta2YgDXR2Epe7cHnev3S1fFauI-a9NP3k3jdSIsQyw1Qnke5lCytqpIvzDqsD2GXTCVj3b6ilw8tb-P0uHoI0_yVTtHzG3JzfRhavJUvJKq4c4ioqdTi2dfNb2a4c7fwrwg3C2W4xIrz_69hLq7tUcFCDp9RnXBYHpoxJQ2PfNW0ASjbX7P9KW2eu_5fQCL7lothO8fjGPYyvIoc73zXKCvLD_-LHLZciFEdqsF9LV0GqRE3t2A5D-HPXIfyDt9z8-wvHzna-xrJEv2DCSNxMz6PJFJwNWEKbfBLpPRlSDHeYwd5DrrDd3y0mTZiptnP8nmlz4dkuhHRPjpWixYLoeLprvZApE-q4ITSGc5mTaz4QXd3epW991znEdKSbCOaO2WZt7gLOMNQ8NmvE1W_6e8l5z_aHUC1EnE_xnsBiLeg8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روسیه فیلمی از رزمایش هسته‌ای نیروهای این کشور منتشر کرد
🔹
ولادیمیر پوتین، رئیس‌جمهور روسیه بر لزوم افزایش سطح آمادگی نیروهای هسته‌ای راهبردی و تاکتیکی این کشور تأکید کرد و گفت که توسعه همه مؤلفه‌های آنها ادامه خواهد یافت.
🔹
پوتین گفت: «مهم است که به افزایش سطح آمادگی نیروهای هسته‌ای راهبردی و تاکتیکی ادامه دهیم و همه مؤلفه‌های آنها را توسعه بخشیم.»
🔹
رئیس‌جمهور روسیه در عین حال تأکید کرد که مسکو قصد ندارد وارد یک رقابت تسلیحاتی جدید شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/akhbarefori/653406" target="_blank">📅 18:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653405">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAFy_JhGo0EcVnpnO0iITathdPerNaQnCylJsnFy7zboVeNr5K50kC4R9A8xTiXmIguSIr0hw98hEFuZ5VK6EwNXtsMbm7_ZKZf_eiZj3dlLgeTq7qdTz2_YCnnKuAgP_3crdsr70nPeOGDLDE2vCKjCL9iku9kN4REuAadZ86cWv_2K5QfhK0jyAQ_LtWxuoeFLUicYR4dOcZ24ttkLb3EKgh-k2-wsJ8IC6tsDJ9h-iThrMZqbcLIjgpLVFCOKeQx8JxF71-tuwqD_t4gGpPlAaxYHZ1Dag5WoHxJ5AQc0YqAfhHkTtkJf-cnaHjuV0B47HZOIksX7FMGWY6_-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاستیک؛ مهمان ناخوانده خانه‌های ما
🔹
پلاستیک سال‌هاست بی‌دعوت وارد زندگی ما شده است. وقت آن رسیده با انتخاب‌های آگاهانه، این مهمان ناخوانده را از خانه‌های خود بدرقه کنیم.
شما هم به کمپین
#نه_به_پلاستیک
بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic
#نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/akhbarefori/653405" target="_blank">📅 18:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653404">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWKCZJqzgw6bZVQE0_nIvCRHjnqc1z5r-Mhhrnie66lycREfeyIgUr7j5txB7iFZdKljbL8d6NJsonpWoNBWD0Fhi-CQCnI4ElcfKTJzclAk8oSMmVgk8QsSkjj81SDq69imr5wd54TCGqYlHJCsEk33KHYh-8jxtRSEb2yjphbvvxdi0sVBphQgTc3TYdQtNAT_A_FL7k7xG-lxsyK5s5bRL7qTB9gJ3FQ70gMhzAwlg5EwI9D6UCBWnpKAMGlYz4FihMnt3E2e8IhDgkUoWBZLxvgByLl_kxC5HulGnXLqfgvTY8LID2JrjCS2UB0J8NLQ7XEGbvIU47zZPZ828Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطعنامه ضدایرانی پارلمان اروپا همزمان با سکوت در برابر جنایات آمریکا
🔹
پارلمان اروپا با تکرار ادعاهای حقوق بشری خود درباره ایران خواستار تحریم‌های بیشتر علیه مقامات ایرانی شد.
🔹
این نهاد اروپایی بدون ارائه هیچ سند و مدرکی از کشورهای عضو خواست که مأموریت‌های دیپلماتیک ایران که با «سرکوب فرامرزی» ادعایی مرتبط هستند را تعطیل کرده و تمام تحریم‌ها را به اجرا بگذارند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/akhbarefori/653404" target="_blank">📅 18:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653403">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
رفتارهای غیرانسانی مقامات رژیم صهیونیستی با اعضای کاروان صمود، صدای کارشناس صهیونیست بی‌بی‌سی را هم درآورد!
🔹
مئیر جاودانفر، تحلیلگر صهیونیست: انتقادات نتانیاهو از رفتارهای بن‌گویر، کاملا سوری و ویترینی است؛ این‌دو در انجام این رفتارها شریک و همکار هستند.
🔹
بن‌گویر قبل از ورود به کابینه نتانیاهو، ۵۶ بار کیفرخواست داشته و ۸ بار هم متهم شده بود.
🔹
این‌ افراد مدام به فکر جنگ هستند؛ چراکه آنها فقط بر أساس جنگ و خون‌ریزی می‌توانند بقاء داشته باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/akhbarefori/653403" target="_blank">📅 17:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653402">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP_H2vv337ip1RZfG557c1WbukEq4IbN70HDkSeQO3R0pToEusC7218aF4Uoot07idpoUR8gCb_arZoBrB9gJfxBzybIXmSa3D0cfqNukrV8Akx_9E4OThG-vFb69b2wzwJzZut3JhcsRMfcSk13QkuBck-vG_s9sx1rFuO6DanlE-ZG-sS8PedSDob_5FdFMOnagvu0_iiB8ME5NGN-XoY4ntLDuSfWUXAMOROoHVsO_D3x7x6ElCoX5qWadHRy2MMlf60QU7M410pWAsW0wsNEDSlRn89MEHJinbHyttjeB1zmzvNG3MFNuoZncbtrf9UPxbszGJbjk3rwx4mj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غول نفتی امارات: تا نیمه اول سال ۲۰۲۷ جریان کامل نفت هرمز برقرار نخواهد شد
🔹
رئیس شرکت نفت دولتی امارات متحده عربی ادنوک نوشت: حتی اگر جنگ علیه ایران همین حالا پایان یابد، جریان کامل نفت از طریق تنگه هرمز تا قبل از سه ماهه اول یا دوم سال ۲۰۲۷ به حالت عادی باز نخواهد گشت.
🔹
این چشم‌انداز از جمله بدبینانه‌ترین پیش‌بینی‌های مدیران ارشد صنعت است و تاثیر اقتصادی طولانی‌مدت جنگ علیه ایران را برجسته می‌کند؛ جنگی که به گفته آژانس بین‌المللی انرژی، به دلیل مدیریت تردد در تنگه هرمز، بزرگترین بحران انرژی تاریخ را رقم زده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/akhbarefori/653402" target="_blank">📅 17:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653401">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630c1a7be9.mp4?token=SWSplZpuZSo7Q3sLdOcn4NQMMqAoVr2PO0eSp6uuaKvmjvYRUnwEqqD7bON0NXE9GT8PKeowzV_tnlBpxWEMp5AfVbgNa0g8dwdavQJGXtu72s4YalqLI18ACjrJvs17Mo_IXQNE5aHTVWuiX6RqPahrpgipXvhePYqJDBpnmdTtJmXAM0n_BN9Ohuj0-_xzh791jDL2gjLIhRDyyvvubvlC7iM4wr4Gc0fSo4gGrb1CXGGYrFBhYw2VHwV3RQ9mZzyTdG5aB4alR4Eu-CxPflsiDWTBeTVaZLApJ5eONvit5_6RL3oXbeCLjYbtmcSFNl05OW3xdbpwIrlVsUNwYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630c1a7be9.mp4?token=SWSplZpuZSo7Q3sLdOcn4NQMMqAoVr2PO0eSp6uuaKvmjvYRUnwEqqD7bON0NXE9GT8PKeowzV_tnlBpxWEMp5AfVbgNa0g8dwdavQJGXtu72s4YalqLI18ACjrJvs17Mo_IXQNE5aHTVWuiX6RqPahrpgipXvhePYqJDBpnmdTtJmXAM0n_BN9Ohuj0-_xzh791jDL2gjLIhRDyyvvubvlC7iM4wr4Gc0fSo4gGrb1CXGGYrFBhYw2VHwV3RQ9mZzyTdG5aB4alR4Eu-CxPflsiDWTBeTVaZLApJ5eONvit5_6RL3oXbeCLjYbtmcSFNl05OW3xdbpwIrlVsUNwYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشای وضعیت سربازان آمریکایی پس از حمله مرگبار ایران به پایگاه آمریکایی: نه پناهگاه داشتیم، نه آمبولانس؛ فقط رها شده بودیم!
🔹
افسران آمریکایی در گزارش جنجالی شبکه «سی‌بی‌اس» آمریکا: انتظار داشتم ببینم صف آمبولانس‌ها به سمت ما می‌آید یا چیزی شبیه به آن، اما خبری نبود. حس کردیم که تنها مانده‌ایم. بی‌توجهی بسیار زیادی به ما شد که این غم‌انگیز و دلسردکننده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/653401" target="_blank">📅 17:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653400">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0LHIb-y--UkZ8BvCgrMqKAa3atL5BbfMskFTYWbabtp_EDBU9jwldRp9y9Wa4E2RBgOAc2_sfseh68JMG-O6a_Q6mhYfblGDTTbWx8S6qJya7HeaEF5qmypbLiNbwwqXcqOV1fR96Z8wu3ZvKWiqh0iouwrJ0pSLM7a807Rq3Htu93x1rQ7i2o-XXOsCH5jVv5IH5_DNXNgH1DI28UArJXQ0mP3YCYIcmbxbpERMvc2DQsX5nUF6EUdV08Z6CdlTQk7WDW8WUtrfkttcSxkQIVj-dReGDRP42Yslu2Vt8xEPFVPUU7fjsDo4ZwzoFEmxRq6I-WJ0GWdlbjE9EF1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شگفت‌انگیزترین عینک هوشمند رونمایی شد؛ دیگر نیازی به یادگرفتن زبان نیست!
🔹
گوگل با همکاری سامسونگ، تازه‌ترین شگفت‌انگیز عینک‌های هوشمند را رونمایی کرد. این عینک‌ها بدون نمایشگرند و تنها با دستورات صوتی کنترل می‌شوند و رقیب مستقیم عینک‌های «متا» هستند.
🔹
با این عینک‌ها کاربر فقط با نگاه کردن به یک شیء یا مکان، می‌تواند مسیر رسیدن به مکان مدنظرش را متوجه شود،  تماس‌ها را جواب دهد، پیام‌های متنی ارسال کند و جواب‌ها را از طریق جمنای به صورت صوتی دریافت کند
🔹
اما غافلگیری بزرگ، ترجمه همزمان صدا است. این عینک می‌تواند در یک مکالمه زنده، صحبت‌های طرف مقابل را فوری به زبان شما ترجمه کند. حتی متن‌ها (مانند تابلوهای خیابان) را نیز برایتان می‌خواند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/akhbarefori/653400" target="_blank">📅 17:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653399">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d9f1e65f.mp4?token=MJK1AwQmsStzaExEacXryRUzjBNXKXveCc6p-uU_yv2j2o3rDH4wri7j8M-PMNilHtmiJUxtdDHvJW1TJMXfHZPTHS15CkWFn5z0hRw0rbDPCBAegjuiaWTWqdxfOytDqItUTbkZ7l5HQXRHHwYcqCwpop4mGMIhDMiG2HE0DjP3-PuXoZfg0vGXudVx2PlWgxGG4WY1sK6GCORsxpcfkgFkG_v8zzBahi-CQvp6JCB4CqxLZpMxxKSDdNsBQfaJ1UOYHgRPVYNam66wgCGZ12lBzZzT84C1QVQGWhRHKZNNZpr9ihv2kFaSKQSBO-JMro-fCi-5Rv0_VwWQZGmmkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d9f1e65f.mp4?token=MJK1AwQmsStzaExEacXryRUzjBNXKXveCc6p-uU_yv2j2o3rDH4wri7j8M-PMNilHtmiJUxtdDHvJW1TJMXfHZPTHS15CkWFn5z0hRw0rbDPCBAegjuiaWTWqdxfOytDqItUTbkZ7l5HQXRHHwYcqCwpop4mGMIhDMiG2HE0DjP3-PuXoZfg0vGXudVx2PlWgxGG4WY1sK6GCORsxpcfkgFkG_v8zzBahi-CQvp6JCB4CqxLZpMxxKSDdNsBQfaJ1UOYHgRPVYNam66wgCGZ12lBzZzT84C1QVQGWhRHKZNNZpr9ihv2kFaSKQSBO-JMro-fCi-5Rv0_VwWQZGmmkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیگیری اتاق اصناف برای توسعه اینترنت پرو
🔹
فرشید شمشیری، عضو هیئت‌رئیسه کمیسیون تخصصی تلفن همراه و لوازم جانبی اتاق اصناف ایران، می‌گوید محدودیت اینترنت بین‌الملل، خدمات پس از فروش و تعمیرات نرم‌افزاری موبایل را با چالش جدی روبه‌رو کرده است.
🔹
به گفته او، بسیاری از تعمیرات تخصصی به دانلود فایل‌ها و آپدیت‌های حجیم نیاز دارد؛ فایل‌هایی که گاهی حجم آن‌ها به ۲۰ گیگابایت می‌رسد و بدون اینترنت پرسرعت، روند خدمات مختل می‌شود.
🔹
شمشیری با اشاره به اینترنت پرو تأکید می‌کند حجم و سطح دسترسی فعلی پاسخ کامل نیاز صنف موبایل نیست و اتاق اصناف همچنان پیگیر بهبود شرایط برای فعالان این حوزه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/akhbarefori/653399" target="_blank">📅 17:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653398">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ur1FWWifK7S5njGd_K1ybPOFmNktWxRKlAmuaDvbwcnr9pYp0dSZfO_RvfUPFSvKT0Dd2ktyxJvZAPoy6ITWO2MqM0hFr0dh2-2aV6Jrk61rJ9j5P8CHi-9GPnyECIU3tdqq47B5cvqVSgfuwm2l0Vr1wNmmflWX8bTtsl4gbGRv8PXwOuTf4Yu8wlliQn_I7RpaMoWHklzRh6rEoc1Y-aUyAytWhRepz-LmwX512cjK30cRMiCaQCJa41K1shwGKfFZ9oiHIHw0QnbpW9pb9tmc3WACu1aL8EIQkM81ShA0j11DWz_OOE6UQupqjkcWIQoJ5A5OC3CIE7nY5fhEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت وال استریت ژورنال از «شیخ‌نشین کوچک نفتی که بر اثر جنگ ایران منزوی شده است»
🔹
کویت پس از حمله عراق در سال ۱۹۹۰ هرگز به طور کامل احیا نشد و اکنون بار دیگر در بحران فرو رفته است.
🔹
با بسته شدن تنگه هرمز و آسیب‌های ناشی از حملات پهپادی ایران، صادرات روزانه ۲ میلیون بشکه نفتی کویت متوقف شده است. این امر جهان را از حدود ۲ درصد از نیاز هر روزِ خود محروم و منبع اصلی درآمد کویت را هم قطع کرده است.
🔹
تقریباً تمام مایحتاج غذایی و آشامیدنی جمعیت ۵ میلیونی کویت اکنون باید از طریق مسیرهای زمینی عربستان سعودی با کامیون وارد شود که هزینه آن ۶ برابر بیشتر از حمل و نقل دریایی است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/akhbarefori/653398" target="_blank">📅 17:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653397">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کارانه پرستاران ۶ تا ۷ ماه معوقه دارد!
احمد نجاتیان، رییس سازمان نظام پرستاری کشور در
#گفتگو
با خبرفوری:
🔹
برای کارمند اداری بعد از ساعت یک عملا دورکاری وجود ندارد و این کلاه قانونی است که آقایان می‌گذارند چون نمی‌توانند بگویند ساعت کار را کم کرده‌ایم.
🔹
از آن طرف برای برخی از نیروهایی که مجبور هستند به طور شبانه روزی کار کنند، هیچ امتیازی دیده نشده است؛ دولت باید برای این موضوع فکری کند.
🔹
درحال حاضر کارانه پرستاران بین ۶ تا ۷ ماه معوقه دارد. یک پرستار متوسط در ماه ۵۰ ساعت و بیش از یک کارمند عادی کار می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/akhbarefori/653397" target="_blank">📅 16:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653396">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
نظرسنجی تکان‌دهنده در آمریکا: جنگ، ما را ناامن‌تر کرد و ایران را به بمب نزدیک‌تر!
🔹
تازه‌ترین نظرسنجی مؤسسه امور جهانی (انتهای آوریل) تصویر شگفت‌انگیزی از افکار عمومی آمریکا پس از جنگ‌های اخیر ترسیم کرده است.
🔹
بر اساس این نظرسنجی، نزدیک به نیمی از آمریکایی‌ها (۴۹ درصد) معتقدند جنگ‌های اخیر نه تنها امنیت امریکا را افزایش نداده، بلکه کشور را ناامن‌تر نیز کرده است.
🔹
در سایه این ناامنی، اکثریت (۴۳ درصد) نگران‌ترین سناریو را باور دارند؛ احتمال دستیابی ایران به سلاح هسته‌ای اکنون بیشتر از قبل شروع جنگ است. ۵۸ درصد از پاسخ‌دهندگان از نحوه مدیریت جنگ توسط دونالد ترامپ ابراز نارضایتی کرده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/akhbarefori/653396" target="_blank">📅 16:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653395">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
وزارت خارجه رژیم صهیونیستی خبر داد: کلیه فعالان ناوگان جهانی صمود از اراضی اشغالی فلسطین اخراج شدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/akhbarefori/653395" target="_blank">📅 16:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653394">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pp1sTqR8rd06cWrqP1Ykmr7zshQs3yRRhWDKdbuWAoU02XhUSAscjHEyOdqm7ba8tvS86Cg5lpKBqxIcHBqf7PNoaGUang2Pz9IYyujXZzFMO-DLeMLKwiFhXIHYXM7WQm1WtOFnFqrF-T-6Q-_WGoFbkzirMwNJylruyuYs6EuSSOSfUCM2fYHdOrCVTeiOAGtMmJjefAUV-KC45Hz-VtSTShD_iTPkwrAnKCJihG-gVN62XPS19cGMu9I1I-IDTfvyAk_ZkaaKImN5Jf_a8EVDJ3YQRO6tOMIfQH3fYoii9m-hcngfyHnT1OU973S5zxWLLqCyWOqC4ep0wRt58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری برای روز اهدای عضو؛ «نبض ماندگار»
🔹
همراهان عزیز خبرفوری، برای شرکت در این فراخوان کافی‌ست به پویش «نبض ماندگار» بپیوندید و با ثبت کارت اهدای عضو، سهمی در ادامه زندگی دیگران داشته باشید.
🔹
برای شرکت در این پویش:
عدد ۱۲۰ را به سرشماره ۳۴۳۲ ارسال کنید
یا به لینک زیر مراجعه کنید:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از ثبت‌نام و دریافت کارت اهدای عضو، تصویر کارت خود را برای ما ارسال کنید تا در این حرکت انسانی و ماندگار کنار هم باشیم
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/akhbarefori/653394" target="_blank">📅 16:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653389">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OERmXVOMVD4JZzPei-4BxKhA3quQRuXakH7VWZ0D_r6piIv-TfGfNIt_RBLueMYq1gx3lNsFLesTVBhZ_2m8OejqIEjEWeDGuMAPLrOCLr7nH_3kl9x2iwC_FQETx7z_W3witwAWfnLieqW0oEdNUeQD3k1v976WKcCsbROoHkRJrmY4XYW5E9mVy9x4QDtG9nGbrC4uRt80_Ps2pHKN-GIw9t0Lpvplw8cXZ1ofUjm2N0DVeB2Cs3TNeFnVR-uHO51JJ4LIz44O4JrQMcV8F3CDM0mH04HXhw8FMKkoU0jrz6Oh-92fokC9-y-tAw3pzvfYicZ2B5XLJ_2D76eRbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGhUYp3mSfKlEqsOdXXq-MovUEL1L9kNgZIjOQ4tt59hdNkddtOxa1QP9WL-mtqMqJloO32eLmo7Sw9Q14Ly396uQNCKbRZvH5SJ1JTZ2dYEBdR7YB1ujuBRtbJt8_uCyGHsPlgy3GR2V1y99TxCsMEQyunn8E9xYqf80MaVEiLgvJ2WaGwie2V8QRuEO9vE5g9RvCc0bIHGIWqqZG4r1ZDbbKlVBlIcmEbA5cQ_2f3Yx-BYfIXf-KxPseFlxdLYPpU1mo16v2dYybTDR5umISOIrtJfC_H0fXQU865pkfr5CidreC3VgczlSTjXLwffngUta2RTGfKDUVJ2r1NpFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G1zmxA2jHmDmGqtjPM5AttQVUnCINUTJGPXMrTC799xUdoYvXEXhxA0AXeQwgs-3SG9XpRYPWxQQjY1NyDXZwostz8ctIYTEgBj8wbYC9QAQl8ACFkYcB1g2v60gJX2MvL6LDryKRS_GtmFjGGxIwlMNipwODD0SfVIJN9TS26aeL5ihJhgzam_l4vSqWsd5eG5pLwjVSROOX4lxbUUNvQXJsLrlKH1T1_TDdJNRYYdCFi-pLc1UpryQfTKNTjYFfaJbg3VhT9Qc1br_KKCNRvkOZDoAOqojM2iEdGzZyk2hVwgG8DTiAWemd0u8Z_2RuZ3od9fIEe_QMrkDJ-_mOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6oWlqoRVj_zYtqCv1mRrGq350kmrZx7yQEwA10MtaVoUi4dCoZkzayc_lWVjFW47ezhUQSJoSqirpWOHrrG25UZVjhzTgE3z90GAHh1Y2c0h4aCtDRjXu6XCL2fi-Ya2OxDtP0AbKmS5tuAR71xGuAc6iEdfpAsgTqeVoHZjYn0YnKQNCADwGkJbMRoSMb4XESafgymsmXAOCgyKZlD7T339EWTXGnh9F_JMsTlnlpvIct9eF-B8PLpB2LSYkpQq2ztXvx1q357aGMw-CyYeJtKtyfb0arZS5l90W3hyBwwr2ihA5Vzy3YXW8IosbEU5UTCeDxqUXa5ymoBsDeSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URvJPe1xaNf1yRcqbXaFpDMAY_YFouGa-BIcIkTPAnfb3CEpsRU83I61QyMA6n_Fs7_wnptNepU3ornRjxd_-fCMaoO-qE6-_czNpCFFsgqq3nNv_5_S58OOCuWXNYXfpawta8rM_3HtY86KrgeL5cGB8oelN9P6W9XkoZ2SnkMKYssoVrfLJ3KWjTfHZBERmXJABWkXIptLeGFXCevUSwrhyCgYFPQENiQaLoT5RNj_GkLbprUVL1mgKgpR4Wc5hokcHfcNXRBelVTnXdEbi0rDdxeiBdQIH92KmUHFsalt7enPchWfrPG2pNJOy9CZ0Ex6NuwqKAnFOFJqw86yJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیدار فرمانده کل ارتش با رئیس‌جمهور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/akhbarefori/653389" target="_blank">📅 16:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653388">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7fee370e6.mp4?token=E19xl6r2c9jnW3krGIWKzW4Hb0Cx8SJVVVRx3hF3W3OBzA-cbU_HkNWUX0KGumdYASTNwYnhNucD_92Rhdeuq7MrbMydsw248nFN9ejJMXUjt28c3hwjYte-RIOjs14kMtcqNbxzu1ToNLG2p6Svp6QtHF4bmf6vJhPLLc0lGrgr636emZHFFOxPtJa6570cJjFvXP9TSQANlJXWJj_aiOW71yHyrm6gUDZp4bNsK2MlCdALq4EVXFfppf9JbF2EBB8imz5pHhWnlsJ09Bbdw3w-LMK0AuELZVz8tATijntkN_9ZRKqZJpkDe0rOENWx10zv_gD3QxVlUAJec34rLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7fee370e6.mp4?token=E19xl6r2c9jnW3krGIWKzW4Hb0Cx8SJVVVRx3hF3W3OBzA-cbU_HkNWUX0KGumdYASTNwYnhNucD_92Rhdeuq7MrbMydsw248nFN9ejJMXUjt28c3hwjYte-RIOjs14kMtcqNbxzu1ToNLG2p6Svp6QtHF4bmf6vJhPLLc0lGrgr636emZHFFOxPtJa6570cJjFvXP9TSQANlJXWJj_aiOW71yHyrm6gUDZp4bNsK2MlCdALq4EVXFfppf9JbF2EBB8imz5pHhWnlsJ09Bbdw3w-LMK0AuELZVz8tATijntkN_9ZRKqZJpkDe0rOENWx10zv_gD3QxVlUAJec34rLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶۰ درصد زایمان ها در سال گذشته سزارین بوده و تنها ۴۰ درصد طبیعی!
🔹
اما این عدد تنها عدد شگفت‌آور خبری نیست؛ در این بسته خبر رسیده که قرار است به زوج‌ها تسهیلات خرید جهیزیه داده شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/akhbarefori/653388" target="_blank">📅 15:53 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653387">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7Bvd18uO-tfOXp2pMwoyeWsVlb_HgFwtvAULHZL228gIa7xw__DvN_XYKFv2U4oi9RtJl0xUBuT7pSMUOLbI7_YHJU7iS2znRff937TRFDimUXdaneG9WLwKCHEBkFCh-MimS7wAaAgkzG5Ba3wSN6W4ERVpEBIewdZTXqv8fTYeeMaQsIKWFvWHQs-oks3kp9duAry2hbBtR9x0a5Su9X6ymdRiqNvyTjI27mPjrt_nLZk1nyUAgxcBWFiWP2RVRzVW8RCuD4yrStP_Ryd3wbr642Enb5DfkUz9N9Fb1c8N6Wk9M3Jns1XsHX34Bgdsq-X_JVkNy-Ug8XzE2_Nww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: اروپا از تجربه نازیسم عبرت بگیرد و از بی‌عملی مقابل رژیم اسرائیل دست بردارد
🔹
سخنگو وزارت خارجه: تصاویر وزیر تندروی رژیم اسرائیل در بندر اشدود که شخصا فعالان دستبندزده کاروان بشردوستانه «کمک به غزه» را تحقیر می‌کند، عمیقا تکان‌دهنده است.
🔹
این تصاویر، خاطره‌های تلخ تاریخی را زنده می‌کند؛ زمانی که رژیم نازی، متعاقب بهره‌مندی طولانی‌مدت از مصونیت مطلق در برابر جنایاتش، خود را استثنایی، معاف از هرگونه پاسخگویی و فراتر از قانون دید.
🔹
اگر غرب همچنان شکاف بین ارزش‌های ادعای‌اش و رفتارهای عملی‌اش را عمیق‌تر کند، باید منتظر تکرار درس‌های بی‌رحمانه تاریخ باشد
🔹
اعطای مصونیت بی‌پایان و سکوت در قبال قلدری و قانون‌شکنی، هرگز موجب تعدیل این رفتارها نخواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/akhbarefori/653387" target="_blank">📅 15:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653386">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
تقدیر وزیر اقتصاد از عملکرد منطقه آزاد کیش در جنگ رمضان
🔹
در ایام پس از شروع جنگ تحمیلی جاری، با وجود شرایط ویژه جغرافیایی جزیره کیش، محدودیت‌های پروازی و آسیب‌دیدگی بخش‌هایی از بندر تجاری کیش و بندر چارک، سازمان منطقه آزاد کیش با اجرای تمهیدات عملیاتی، فرآیند تأمین و توزیع کالاهای مورد نیاز را مدیریت و روند قانونی خروج خودروها را تسهیل کرد که منجر به آرامش عمومی در کیش شد.
🔹
محمد کبیری، مدیرعامل سازمان منطقه آزاد کیش، در سفر به تهران و در جریان پیگیری موضوعات اقتصادی جزیره با مقامات ارشد وزارت امور اقتصادی و دارایی و دولت، گزارشی از نحوه خدمات‌رسانی، اقدامات انجام‌شده و نیازهای پشتیبانی جزیره ارائه کرد که این گزارش با قدردانی وزیر اقتصاد از عملکرد سازمان منطقه آزاد کیش همراه شد.
🔹
مدنی‌زاده، وزیر اقتصاد ضمن تقدیر از عملکرد منطقه آزاد کیش گفت: تجربه مدیریتی سازمان منطقه آزاد کیش در این دوره نشانه‌ای از ظرفیت اجرایی مناطق آزاد در مواجهه با شرایط پیچیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/akhbarefori/653386" target="_blank">📅 15:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653385">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjhsppqWCx_7RGkrnOQjSK5HL6iONbOeZU-daP4B8rHY2r1xdv5x9P1beOSOzp67iPEsG-Ti2zgd2dcOC9t1t6yHd9ZBiOyGPTs_kEYWY2KnStPKaXV0NDAneRL1zZns7fDtGip-QwaU1g-J-DiGQR8CrcQ0HhYEYz7voroaSbNLxhJWiR8UEcCHgQ8uAkxU9l9RclGFzY5S8Zcg70jY3SFE8KgTAD-o8z-Ud_D877nxIT5EAcheVd0Uj9DfgpcjMv-AqNmnFg4wxhVHKmtYOydmhI0ud_AVtPvPvNPJL8D7fUAyINK-CvKPavWskGxtSqwc162uRiC6eBGaq4HMTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامه انتقاد ها به خط سفید و vpn فروشی در مجازی؛ یک فعال رسانه ای از فشار بر کسب و کار هایی که برای بقای خود از اینترنت پرو استفاده می‌کنند انتقاد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/akhbarefori/653385" target="_blank">📅 15:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653384">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d438d2ebbe.mp4?token=mWUxUjoL3EAPN6u1xG5MGAxw4mIaDm1mVG1LRDTTTHijhRYoBfMoGoU8F5MWtjSNaWznptJqwU8JYstPJg9iYSwzUYuPR55t_1GIGbdzXOpp3PVTxhUHLDGStJouc9z6wruOr9ToUZfMhc4XEzl9pxaZSRVLPnNAXzOhwpC7Bu7253pp2pQXBr1Y83oKDxNsJAQdN2WjL_pEIG5ZuI8r1BP4fr4Z1XJWhLMPW-bqQHGzlyzJDEke9N7AfSOMYmh65so98xbBgXR8qKAfXELwTIB755qFc9wFWioV4BqDyw76pT1iRAgmz5VpO219OzYuitZSeQ3nh9AF6bDqBCQVig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d438d2ebbe.mp4?token=mWUxUjoL3EAPN6u1xG5MGAxw4mIaDm1mVG1LRDTTTHijhRYoBfMoGoU8F5MWtjSNaWznptJqwU8JYstPJg9iYSwzUYuPR55t_1GIGbdzXOpp3PVTxhUHLDGStJouc9z6wruOr9ToUZfMhc4XEzl9pxaZSRVLPnNAXzOhwpC7Bu7253pp2pQXBr1Y83oKDxNsJAQdN2WjL_pEIG5ZuI8r1BP4fr4Z1XJWhLMPW-bqQHGzlyzJDEke9N7AfSOMYmh65so98xbBgXR8qKAfXELwTIB755qFc9wFWioV4BqDyw76pT1iRAgmz5VpO219OzYuitZSeQ3nh9AF6bDqBCQVig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری برای روز اهدای عضو؛ «نبض ماندگار»
🔹
همراهان عزیز خبرفوری، برای شرکت در این پویش کافی‌ست با ثبت کارت اهدای عضو، قهرمان زندگی خود و دیگران باشید.
🔹
برای شرکت در این پویش:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید.
یا از طریق لینک زیر ثبت‌نام کنید:
https://ehdacenter.ir/api/gateway?code=120
🔹
بعد از دریافت کارت، تصویر آن را برای ما بفرستید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/akhbarefori/653384" target="_blank">📅 15:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653383">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irQRqkVQ82ILUd18-EDi_zaXkgK91eRy0nfiGMtEO9sOwq45ovroNWm8Ks1ZJFyRC-90eNUlzsaGvedI3K6kPD9GNGGl-EYQr_DJhgFflOHGF31LSKCAOKnHL1eQoJfr9o-hOd1wW9JaKPyUJxKg0CVRIbRDsmtQX26MiFpcjqibBO_WpkhReCyhjT2suiS9wKGgSroqGVgXkBWf-Jmdamwuyfb5j6n8UH6ytY7F_Boa5WxnRm6dtbItXhaOonKiYv6j38zhRMZSOHCkiH7UnImAb7HN-v7vmdgpTpTH2qV09gJgn37AvtjqgiMheHz3Z1kg_xSgzSYQwQIOqemCdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: ارتش با آمادگی عملیاتی بالا اقتدار دفاعی کشور را به نمایش گذاشت/ دولت با تمام ظرفیت از تقویت نیروهای مسلح حمایت می‌کند
🔹
رئیس‌جمهور، در دیدار با فرمانده کل ارتش جمهوری اسلامی ایران : نیروهای مسلح، به‌ویژه ارتش مؤمن، مردمی و انقلابی، در جریان تحولات و تهدیدات اخیر با آمادگی عملیاتی بالا، اشراف اطلاعاتی، انسجام فرماندهی و توان رزمی مؤثر، اقتدار دفاعی کشور را به نمایش گذاشتند و اجازه ندادند دشمنان به اهداف شوم خود علیه ملت ایران دست یابند.
🔹
دولت با تمام ظرفیت در کنار نیروهای مسلح قرار دارد و از برنامه‌های راهبردی ارتقای توان دفاعی، پشتیبانی لجستیکی، نوسازی تجهیزات، تقویت زیرساخت‌های عملیاتی و افزایش توان بازدارندگی کشور حمایت خواهد کرد.
🔹
امیر سرلشکر حاتمی: ارتش جمهوری اسلامی ایران با بهره‌گیری از تجربیات میدانی، تقویت آمادگی عملیاتی، ارتقای هماهنگی میان نیروها و به‌روزرسانی ظرفیت‌های رزمی و پشتیبانی، آمادگی کامل دارد تا در برابر هرگونه تهدید، تجاوز یا اقدام ماجراجویانه علیه کشور، پاسخی قاطع، پشیمان‌کننده و درخور اقتدار جمهوری اسلامی ایران ارائه کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/akhbarefori/653383" target="_blank">📅 15:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653382">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
رییس جمهور در دیدار با فرمانده کل ارتش: ارتش با آمادگی عملیاتی بالا اقتدار دفاعی کشور را به نمایش گذاشت
🔹
انسجام ملی و اقتدار نیروهای مسلح مهم‌ترین پشتوانه امنیت کشور است.
🔹
دولت با تمام ظرفیت از تقویت نیروهای مسلح حمایت می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/akhbarefori/653382" target="_blank">📅 15:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653381">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07ada4d4a.mp4?token=oP70LR-5eBMe_sXA3CCpVKCyJ5c3_6DOEKIVDivFT1Vm42gZHlL-gu0vH2tA72yfikiboNZyMOvb2w95igJrkHXcE0A0x0f42KMMSbyfYe9saolFJpOfh-YBfMC6kniX23RBRre_gDTlw7NAtR6vYC1lIiy_yk7YhTlPlfjRrqasGCxayIY4cC4JZt12OLYvYe76HWNXVQrKnvifQlQP5xiodR-dbLqW6gmiowbqDcCsWJB1hGF-IzMlxqPisxNfNfUVxJ4oI4V97-mRkAXQMMPSimENUDkR-xzIjZFMxwyL63z7azd4pI52YaKy-yh4-xye30BcLKB50FGNImkFFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07ada4d4a.mp4?token=oP70LR-5eBMe_sXA3CCpVKCyJ5c3_6DOEKIVDivFT1Vm42gZHlL-gu0vH2tA72yfikiboNZyMOvb2w95igJrkHXcE0A0x0f42KMMSbyfYe9saolFJpOfh-YBfMC6kniX23RBRre_gDTlw7NAtR6vYC1lIiy_yk7YhTlPlfjRrqasGCxayIY4cC4JZt12OLYvYe76HWNXVQrKnvifQlQP5xiodR-dbLqW6gmiowbqDcCsWJB1hGF-IzMlxqPisxNfNfUVxJ4oI4V97-mRkAXQMMPSimENUDkR-xzIjZFMxwyL63z7azd4pI52YaKy-yh4-xye30BcLKB50FGNImkFFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: رئیس‌جمهور و وزرای دولت برای حل مشکلات معیشتی مردم بی‌وقفه تلاش می‌کنند
🔹
مشاور رهبر انقلاب در دیدار تولیدکنندگان و فعالان دام و طیور: همه باید به دولت کمک کنیم تا با اقدامات لازم، گشایش‌های بزرگی انجام پذیرد.
🔹
دشمن آمریکایی‌صهیونیستی امیدش به فشار اقتصادی و تمام شدن تاب‌آوری مردم است و خوب می‌دانیم این بخش جنگ برعهدۀ تولیدکنندگان در سنگر امنیت غذایی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/akhbarefori/653381" target="_blank">📅 15:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653380">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0OGVdfhWu8Nh3p7D3YYtlmlXhKI5-BLtOWK6rsgnefMh-XGqhJuv8sPrMA9dSVzXj16b9b7lBXoW13dIUW_lqYokfY_j4p3453lJHs5E69L0vw9l-dHH0pzT3jazP_LU6YxY0AiNaU_kpnuYUBU1X4GYEvonkaeivGq2Nik2Ha0Hd9QFTlMsylNDVShXOpxdwuI1t50BXD031GT3y1guI0rjSNOANPYf_4sf3ePRzHMDzCzcUYQLrKT6YlLgTkPk556Mw6X8FAxyBuKuTcP8O9moLICfdCw63VaXrBbgK3rQGJvP-trHfOtHH8ravY5CR6Ph1NAtUzDCX1Cg0yRKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهمیه ۶۰ لیتری بنزین خرداد، بامداد جمعه شارژ می‌شود
🔹
۶۰ لیتر سهمیه بنزین خرداد ۱۴۰۵ خودروهای شخصی بدون هیچ‌گونه تغییری بامداد جمعه (یکم خرداد) در کارت‌های هوشمند سوخت شخصی شارژ می‌شود.
🔹
همچنین سهمیه سوخت خودروهای عمومی و خدماتی مطابق جدول سهمیه طرح مدیریت مصرف سوخت شارژ می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/akhbarefori/653380" target="_blank">📅 15:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653372">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vb07DoXqzejont6LQiC-XOeCBsDfBOEScKxPXQxmpLjc-zJ37xM_rw8dvT6_CPX14iEAtZrbCva8nAllf9gISX4bk49e3ObjTAf-_OLFWNLGRZWF_toxX-NcPRGuPs8k4Ur9yKGsE8IsLI6uBALKnDCBCSP3jeWAv7vf61BbzyKJ0lILC9tqwueEXWgi9_q5uE9Agx29AQfawzpt2BiouAwX-0hufUYgTZ7RZCya1v8O_VmfJ-tFJXWAp_4TwSS4f53bcZY1ePUu0Xr9cjcV_sF139kXjX4c89-QkrQ9_OgkXuJR-oEIW5KmPidz_OtJVyfuqJeLae5T3dyqM0mvxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSDNPT8N8J_uvTd4uajrrzrK0qtoLaSy3JyqQPqb1XlGCG2clUHe7O0bHkatHl1N2sz3nVb6C8wNx05DsF-twsTpPTwNTV7YNgufFaVaoqeNFwSq0Q6a1iyJbDwD2BB4mH9tnuCcUVLXT1yiOsANHHcss7-cizknmcof4HBrtU6MAjglnWKnZCreJPOm2t2oE1p_ahq1WXUrREGBsDAC_mmYwyp_ozsnzjv9Tgnud1Ak_ScqE0aD7ureS7eSs6EDrevQ68OPcs4OlMSTLvLRb07aklwuSyJM5t_xv4DZawNChTcAXN0VWNIFsIjy_4_HAWl2SaxeunfJ47RGADXYLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOk7p-VuEleSwmCERz50FYUj3eaiIuD4VpcLY-5o436e8DEdChNckkXblgO4XwxDbGpwSlLKbK7wjaRZIbMio7tBEhaH8LiItMW9ZJKgKXmQCteZvo9Ewz94KKZVYhIZZl0_3F__pJQHKSV_ojBG19Y6y-uSo9d5ct9fQH7Fj_894X3RXwB3bAFMFtkzTwcITpnG4QPgGvAXIc0fhNAAZZaE9cTCjgVPf7IDyi-I7zEEnFc_xPhvGKEKpDs6yF4xoYXp3mwl-Gj9Ch9W5gBy9FDLO0ulwd1KrS4jrl-GEveI0A112s7C4mhG93Di2WrbF0XRdFeTdgklrywq_JdV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FobAF7CEPNumFtUgljfNUanYm4pBs6-apf265aTcWNUdaKI61pzKL8i5xzI7ZLQlU1drIT1x6M9ST8_uIqjtCFilQ_j4rganF2cEfT2opbtOIIrpwKHCFtrZHgIveU1D6fDUyuPK63NKYWgmxQw65O9S0F5J0sglhn_FwiIq_LylYE2Spn0MffLMQlrT5yvZDuvMIv5MlPD2gcx8G5VvvHXl9diZZEY_4V0WfqLNYYwOYHtG52Bw41olDpi083e7ztzeVMXTuqUtNx4csUqiRSzYhpF6LGq2_3_IGtaM4UvrVpv-ZxN4VVvm32DCkn3VRpwFwG4BORlA-F9mPIO-xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ny0q37-MEedq52riTyr6LsqCJ0joCj6kwJxSDzYpp9ts1ohQOgzbeAeJxO9BBVDcCWuFbGM9ZOesg5TeaTh2AP6XlP79zu63lKsKzVYkVqsjRmLSzKiZ0BenlRyQh6IlxEkSYRgAcnXLRremEBN5lj-A7xmPZGBeQzb4LsCoEYDq93lcHU4z6wNAp5mbiP7U6Qg8O_QNSDL77HF8vZGl81EidDS3BuAONkKjyVV0L1bg0DMDXX1P-zt6NqgtsWrtHxnWN0un04S2Zk6Qq03GpThOzqz4KhIWYfMaX8Qi2IpDYERH0Vc7D4z7aAODeyggsg8LhO_8VLEUyBU2ZutyDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxqOvcR9X0Vn9e92gtcp4Iog_QRwY_byT3vHu48OjiDeLwrd7TVRRUomydg2wi2Q2XoTq47N31JBk6PvH9IWxJSNZYfYseBCDyzQiZCKYHG2GDNgKdS6kflZ7Ge5UQEOkiJ7PTh0AdhdZfZBsjWGS76DK7GE4W8FeasYQdGMYchUsXHpQKfSfe_4zkiGeakalDRORqZF62p3Rn8A6rEeZh6HOo15paQE-xh1dOLXHMDk3t_WlCcg124JbxybtYFPN6CNCaEYTqZaETj29S_JKUWCoQhUCVcpYAGWnL0uyhB2teBXekr0FD5pIDUhU6HCkgjaU-UUT6ITwSEDClxpWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AlV38GdwhC_lHOxzAjOHg_zmnqYvZzqjg8zEd56CX0SuRYtced4W_hUIGOT0GWLmlm9M2KjhbBMHbllmTxO3nrap9ycElYntGlQUQ1h-n7eN8MYQsYSpZ6eU0BHn-7n-WIphAngQZXJzyDc2gB6UCvAxuw5cgJXHfMh-DnZyRGtXOrPDIQoJu5bNqP-8XxSIG4sLSeMpjhLvza78_hIzF2SoI-52l-W2rd84m6-vBbft_4TirWYNLg-yA5TO1Y_AfnYv08MgSIROOJmex9FSp7EF3nYTCBuV0F-AZfm2MKvoC6lHPYpQyklnEmOds39rTrGgfQOddnW-hTtwS_4fmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KzFOgh09nI0lwTvz6sDiiEzLQIRe1GwABhjZGpzuJiF67uey-Lk_GTAHBVdlsU7i9vqWduwReb1T2qCxlsNxTjyxIhICvfG1Rz1pjBUPQ1vrQafmsZUPnV5CqLjB9ingW0o_lOGQVkW91X9B8fvSktbMuxwlAjH0YnqpEl_cU2beFilL1PV6w0lVEK34e3w9y41XPHZm3g68QoviFCwKTamNEQmlg2RfcHiACTq4K_3n0eBSaX2Ry7LpSEdToKx8Ez2hsedbSFXdFWzQIieuyLUg3T_aBHYxmh8USk8lNfxEaQq3ATB14t3uM7oTllk0dOs4D5BfJhibL7c6IaHziw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ویدئومپینگ شب گذشته میدان آزادی به مناسبت هفته جمعیت و همزمان با پویش «جان ایران»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/akhbarefori/653372" target="_blank">📅 15:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653371">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/229a942a29.mp4?token=GRawaUcqSMSqdQGw31_tvZrv-5OTtIt4BrboKkG4QyS0mQ9KQXc5QEajqNdFntInmnrSmX4g5ZGWw4LmiyhL_xMKRxkMrFj0j35bMNETg5I2Y59Eu8jsckn7WFIdliOQU2i5FSBPI38eyhc2AupL2zH2ZYz3wp9Y5-6Ol-sofavjT4xWC_Oh9Sl1dSZaCh9qsF3lsN70CHtzsB-c4N-E2us0AfKw0ClOndktOOmcEns-R_vpQB6tSVHbjY7I4tIgB3UNURWR3Alg2Ng85D-1DcuAz00Qdc6h_qRwi4ijq_XwtZO6zraO6Y6xO2zgRVoHJAfVZTspG9j2rz2qblqvUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/229a942a29.mp4?token=GRawaUcqSMSqdQGw31_tvZrv-5OTtIt4BrboKkG4QyS0mQ9KQXc5QEajqNdFntInmnrSmX4g5ZGWw4LmiyhL_xMKRxkMrFj0j35bMNETg5I2Y59Eu8jsckn7WFIdliOQU2i5FSBPI38eyhc2AupL2zH2ZYz3wp9Y5-6Ol-sofavjT4xWC_Oh9Sl1dSZaCh9qsF3lsN70CHtzsB-c4N-E2us0AfKw0ClOndktOOmcEns-R_vpQB6tSVHbjY7I4tIgB3UNURWR3Alg2Ng85D-1DcuAz00Qdc6h_qRwi4ijq_XwtZO6zraO6Y6xO2zgRVoHJAfVZTspG9j2rz2qblqvUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت بیش از ۹۰۰۰ واحد راکد به چرخه تولید با نهضت احیای صنایع در دولت شهید رئیسی
🔹
با راه‌اندازی نهضت احیای واحدهای صنعتی در دولت رئیس‌جمهور شهید، بیش از ۹۰۰۰ کارگاه و کارخانه راکد و نیمه‌تعطیل به چرخه تولید بازگشتند.
🔹
احیای واحدهای تولیدی راکد و اشتغال کارگران، یکی از دغدغه‌های اصلی شهید رئیسی تا آخرین روزهای خدمت بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/akhbarefori/653371" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653366">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U33gwu0crTHGXdOJJ5tpEk2RwC6s6lYZzYZA_EPIIc7SkAUqo8p2AmV2OzWsfEBZCK-KiULGdzEi9TlH0y3bo-7lOCulyyu9hX1I9rYoV7YcLXziP-jF56eFYdLJ8V3P68Njs0s1P-SPF8Yq4hd4NLWKIviVh_aTdG3lmWBOEd6G63dUYqBLRZOxzfdqqhmJKEU7pStSIHWw4eBcdmB_k_pct2GIT9JBTX_3jIysP3RoH0qVinZJxJCIm2od1FbvBPpi_Lhqr-6A_nUn36RDOq_XYa3KxVh-7-jsBw8-jSxDnl63syTithTA0Xk7N_1iix1gQmsvlthDuCy4Mrll3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TqIqhxiihvEDy7XkczHxnqS6bbC1-Zh4bOUAGJvghaEnRitNXi4FGsYmAUKT6ztteR2fwFCJpD842oXYOLY8dTVBULXnjlkdzTpGevXZgXuY_Ovma2d5ZFRpnPmtEa8VSVCE7-zupsgOEuadfcCb1nA_aItGg350E9347v2p9m5Fi5z2Dh8VpLJjimAuZ7QQo5Agll1cwCQgyAPa33dzw_XQCMVDSxXYlQGV_HJUWpNZbE5ojSd0TTWPCuQ2DVD8tfN1XhPtGg2XuEzAn_WsMnQ8EYMgUlBQ5KOk3W2zD85YwS003Nv-SyhE21mENxobs5N7AsGVGxW5aKHwFvyhzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfAELnSbz6pjWFyT3AoTkaZ9XpuZB-RLcGIpWW5CuQ_NFiDzGXiwcIoWnmUM0qJ2IB19jVI9UECr4xwyxuJ9PsHxjto4LXsbukCwnuujD_5ifAENYS5MNC1fXKEV3Prjwg5TldW5zhctpT62-1vAOh0wWMkdfecocBxD7EqlkPsKdt21pnda6zCEoUXf16oUxySjvsHxps45dvK1scoZLCzJSIUIMDWejcqaYS6B783RzxI_ZvLA8KEZ9g-y4Iq8AWKcHp_JJs4YZmERuw2fPj0QYizm0o18fBvurHXzU1ECPbVd9rl4fJX0ME-MQQudap4gxW6ay7IthPOozME2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qaSFXPmuVnudVJpCJnLmmr4ZkxfCSnpU724A1B2sw0OFUJ8_NHMi_h-OdddGDniWFt6SEWLyWaL5lAoM5GXO8m2wdM6mRpLYR9hublVqxSY-dyHcwFvF7AGR2t3OIPtI6M23jnxwQHoZ9yEreZ7BQpc_fGWeGNtQfBVcQHqwI1farzJBhAqWk-wB8TbtevW_h-Fk-XLZaEjCK5n8mez2KFIJm5jwONKfklqUkWX0CLFqOYMl4JC77oHRq5e26aZXoXkvijg7zA8dwv8j6x-Alwlvb28zp_1EU6b8b7vVMgYoPHhLvPIQCeVgL-HJp93zJ1nF5StrNk_2LJU1yM2KdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FKsUgVQMgNu41v14XJkubn_sCLHOWHg1oakQ_4dVbTyAr3Y07wMwWHD3QZD2AFkhzpBt3cB7pF2uLLmKVJ78Q0nG0qRuRt09cppgh2SBKV9lPAkx19aufRj1GtaSZmZPqyiAjyoUX8swXhW95WE26N7rYqPDl483RySror8Dh1eGH3b2YitblLU7-AyQhBCBHcGjt9OsUTle9jSKSu1xFAUB4epnDpvNaxSiyEymmyrmSYPq5ZIXD-X2lIT_j9ioJCLhV1rqdkKFL3-MoQmsWoC9NafQabE4mbrvutlKAnfzJ2cHncuAeu6NPRjb2vH2L8ssZwQ1R9bxW7p34YTIHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
‌‌
پویش مردمی نه به پلاستیک
🔹
مخاطبان عزیز خبرفوری،  همراهی و مشارکت شما در این پویش، می‌تواند به کاهش آلودگی‌های پلاستیکی و حفاظت بهتر از طبیعت کمک کند.
شماهم به این پویش بپیوندید
👇
#نه_به_پلاستیک
@na_be_pelastic
@Alo_fori</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/akhbarefori/653366" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653365">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عبدالرضا داوری: احمدی‌نژاد ممکن است گزینه آمریکا و اسرائیل باشد!
عبدالرضا داوری، مشاور پیشین محمود احمدی‌نژاد در
#گفتگو
با خبرفوری:
🔹
به نظرم نیویورک تایمز بد نوشته است و احمدی‌نژاد در حصر نبودند بلکه منظور آن، تور حفاظت بوده است و وقتی سپاه برای شخصیت‌ها تیم حفاظت می‌گذارد طبیعتاً، اطلاعات ترددها و ارتباطات آن‌ها را دارد.
🔹
وقتی محافظان احمدی‌نژاد را مورد هدف قرار می‌دهند، یعنی می‌خواهند او را از تور حفاظت خارج کنند. احمدی‌نژاد می‌تواند گزینه خارج از کشور یعنی آمریکا و اسرائیل باشد و این امکان وجود دارد.
🔹
این مطلبی که نیویورک تایمز نوشته است می‌تواند یک سناریو غیر واقعی نباشد. هیچ اطلاعی از شرایط فعلی احمدی‌نژاد ندارم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/653365" target="_blank">📅 15:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653364">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dH3hUmGfkFQV7zOuyXakovAKapFv3rZHBbe1PEHKJaQsaq5RzrXEMZLBOyILDgqA6bLhO9rHv_rSyOcjbMkxApmbfGlrZsG3efJ0R4PJ0G54QBunAJ8f8GmzuaYdAF9yOap49e03BZLKVRNmQR3sSqSB3Qq8_fvXpM7M30c3Zikfoq0XymRNwIXtBujYuaBhbQCCZLMCDvdU8NCzsKJ6iOE11KlUWddtiknmtg1ZdYJOz2uQ3fgqS2Xg_FUywh_VxHjvsh2jpWJzkoRCZRhyA8Y_IvdoFAi4VZTug9GrE1nBrFH6TsF99SgVL4UTdgy5B0XqErNaKqDwbR3-OgLG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: ظرفیت‌های کشور از مشکلاتش به مراتب بیشتر است
🔹
مشاور مقام معظم رهبری در جلسه با فعالان عرصه امنیت: دشمن به ناکامی نظامی رسیده؛ اکنون تولیدکنندگان باید با همت خود او را در عرصه اقتصادی نیز به استیصال برسانند.
🔹
جنگ اثرات اقتصادی سختی دارد؛ حتی یک مصاحبه می‌تواند شاخص‌ها را جابه‌جا کند. فشار کنونی بر مردم را باید در نظر داشت اما امکان رفع مشکلات طبعا وجود دارد و به همین دلیل مقام معظم رهبری در پیام آخر خود بر رسیدگی و توجه به معیشت مردم تأکید کردند که نیازمند تلاش مضاعف است و خوب می دانیم ظرفیت های کشور از مشکلاتش به مراتب بیشتر بوده و خواهد بود.
🔹
همه باید به دولت کمک کنیم تا با اقدامات لازم، گشایش‌های بزرگی انجام پذیرد. دشمن آمریکایی-صهیونیستی امیدش به فشار اقتصادی و تمام شدن تاب‌آوری مردم است و خوب می دانیم این بخش جنگ برعهده شما تولیدکنندگان در سنگر امنیت غذایی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/653364" target="_blank">📅 14:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653363">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvbTikaLoS1x_nkyjiV2l0OiwGA69SP5CEk2FwqgsAZkEKjtJl5_YAom5Mil9gHaoTzTKvdS4J0Lm3HyXSiqznOXNzpy8HFUjraNHPSslPTUxoN0vLvT_fVWA_rGUiGAoSiMQtG1dgrYhl6zjT7UnZ80N5WDPMuyD_kXQV4xxwxA734MS30c0zzn7DXcjLsZarGYJGu-R6tGu71L-ZERjk7jV4MEM8JlRYVgWVbvJ-HQaIsHIFQoE_9ROYGiEPicmsJpOflpwcqapMnJGgxu1iGUhmyZ17-s532DgekMAMz8fEy5QVYsRALFPxRPCY0_oA-IuWja3xxc-sQPaxUTJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا دشمن پتروشیمی را هدف قرار داد؟
🔹
صنعت پتروشیمی ایران با دو بال «ارزآوری» و «تأمین خوراک داخلی» به‌ عنوان یکی از حیاتی‌ترین ارکان اقتصاد ملی شناخته می‌شود.
🔹
این صنعت با صادرات ۲۹.۲ میلیون تن محصول (معادل ۳۹ درصد کل تولید) به ارزش ۱۳ میلیارد دلار، موفق به کسب ۲۷ درصد از کل صادرات غیرنفتی کشور شده است.
🔹
این یعنی از هر چهار دلار صادراتی غیرنفتی ایران، بیش از یک دلار مستقیماً از خروجی مجتمع‌های پتروشیمی تأمین می‌شود.
🔹
در سوی دیگر میدان، ۶۱ درصد باقی‌مانده تولیدات این صنعت به‌عنوان خوراک و مواد اولیه به چرخه صنایع داخلی تزریق می‌شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/akhbarefori/653363" target="_blank">📅 14:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653362">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61faaa0fd.mp4?token=XzUXBnnLJ7jwvxTZ0A7K4PmyvzVUs9HiTiJP5Zr4q5NFmXbO5XlTIAroiHLKCAwu6jxHG96izb3mdJ8Oa528UlOD6iIvIdP_WdHgvVSN4mzGG6sGo_lYQt114PWMQGWg_9Jc33LwKZebmPazvhhV9_5cD5WpTkUGXo5F3m_628Sa8lw0UhYCDWx_lkl2-BfHVbCKNgXr4mUHAps70At3adgzGu_LziMwY60YFlIWNAlmQBbq-89R10hSjhJ3TLQxK-DfzM-wlrVgEEsW88dh5u438DKbq0Zcv_opoTZRfRlK-OGDyPpkBEln_MruLFIi49o14AKCioU_dqXjLopM6ZPpYo2hix5sJRvF2R0fkXl2jbk8P88qqoj6jajEVhgOFrfO8OPL6Dz_w1Kbsd787aL1f0aktqr4gVBRCeA-nesIj_r4V-S-mXM-9KSH2JtJzBrDM-ArzN1V6On4tTd8iF2clJwYiV5em5oitn0Bm_BgGSydCKEe9duaqaBbMsxw_ijGtSwrpom6_etMOAAr_2knzkyth3flEcVRwYm-2BmpiNhvUNByLKMOhAwbF-t9gxmuzh7bsYrXfvZgct1NPU9KkfkwKSh5nAXnY3Oe14qGLvv3TlAzdvJQI7mCjENMD9dwEXVWx22JN-i4JloxufjZqmgnb-gbHUUgUnSSWxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61faaa0fd.mp4?token=XzUXBnnLJ7jwvxTZ0A7K4PmyvzVUs9HiTiJP5Zr4q5NFmXbO5XlTIAroiHLKCAwu6jxHG96izb3mdJ8Oa528UlOD6iIvIdP_WdHgvVSN4mzGG6sGo_lYQt114PWMQGWg_9Jc33LwKZebmPazvhhV9_5cD5WpTkUGXo5F3m_628Sa8lw0UhYCDWx_lkl2-BfHVbCKNgXr4mUHAps70At3adgzGu_LziMwY60YFlIWNAlmQBbq-89R10hSjhJ3TLQxK-DfzM-wlrVgEEsW88dh5u438DKbq0Zcv_opoTZRfRlK-OGDyPpkBEln_MruLFIi49o14AKCioU_dqXjLopM6ZPpYo2hix5sJRvF2R0fkXl2jbk8P88qqoj6jajEVhgOFrfO8OPL6Dz_w1Kbsd787aL1f0aktqr4gVBRCeA-nesIj_r4V-S-mXM-9KSH2JtJzBrDM-ArzN1V6On4tTd8iF2clJwYiV5em5oitn0Bm_BgGSydCKEe9duaqaBbMsxw_ijGtSwrpom6_etMOAAr_2knzkyth3flEcVRwYm-2BmpiNhvUNByLKMOhAwbF-t9gxmuzh7bsYrXfvZgct1NPU9KkfkwKSh5nAXnY3Oe14qGLvv3TlAzdvJQI7mCjENMD9dwEXVWx22JN-i4JloxufjZqmgnb-gbHUUgUnSSWxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شکار فرماندهان اسرائیلی یکی پس از دیگری در لبنان
🔹
یگان اطلاعاتی حزب‌الله با رصد دقیق تحرکات ارتش اشغالگر، راه را برای پهپادهای مرگبار مقاومت باز کرده تا فرماندهان میدانی دشمن را یکی پس از دیگری هدف قرار دهد. از فرمانده تیپ ۳۰۰ در شومیرا گرفته تا فرمانده تیپ ۴۰۱ که هنوز در کماست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/akhbarefori/653362" target="_blank">📅 14:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653361">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r51xX2dMvZYvQ-xkQ5yTyGSqGstuBRmzZlF4EnG7i3N06vfkVNDB6dalUu4cniDasq_f5BOspmkrlA6K9F1yY6ceWXJMJdRhrVcsS9n5oMMlcgSjP16Z3B4xckW6GsUCtr9OgestNPCeTsSlXZhrHbuvsBiTar0ypBIlWzt-5t3mGPztyj_SDuSyGFgCq2kD0BE_UEmygo9ppM25gD94qczSWnDx8srg4axtBFXTVPTtM7vFITI96FmdAHfCIrgB10wxAiLKi3ogTYB-s3dbQz1Miu8zjJZ3fyd1FLxEoe0rMdWkcb-kVKVLbz4u7ktGIT3mjTXJ-9RN9MvVoPAaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه جدید پویش ملی جانفدا: لطفا با توجه با توانمندی های خود و برای بهره مندی و نقش آفرینی موثر و متناسب با کارها و نیازهای مهم کشور در دوره جنگ و پساجنگ، جهت تکمیل اطلاعات ثبت نام خود با ارسال عدد ۲ به سامانه ۳۰۰۰۱۱۵۵ اقدام نمایید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/akhbarefori/653361" target="_blank">📅 14:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653360">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
مهلت دو ماهه مجلس به بانک‌ها برای تعیین تکلیف تسهیلات مسکن
🔹
رئیس کمیسیون عمران مجلس:
🔹
در حال حاضر حدود ۴۰۰ هزار پرونده متقاضیان معرفی‌شده از سوی وزارت راه و شهرسازی در بانک‌ها در جریان است.
🔹
تأکید مجلس بر این است که بانک‌ها حداکثر تا دو ماه آینده پرونده این متقاضیان را تعیین تکلیف کرده و تسهیلات آنها را پرداخت کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/akhbarefori/653360" target="_blank">📅 14:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653359">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0168d013f3.mp4?token=iBPNR60c8gUNYv9lC5xxIGEydUJmmvFd_gq4w9KQCwKGA2fojlzR7rUBeA81K5Lo-RQwzEXM9stA9RPJNsUjC4NC0FKcH-RlAHhzyFI4AFqqoWtzZlvWOo6IFwsV6YvKJIDFaWjzHjs1FWfOoATlWvJxIDM7NeFgZrHbwe_h0pmV_K4-WBsOuFwCA03jgN9jwaY0xVJHAUC6iSqMaPe8LsuRbJm9kg2U3HLNKaIqDO2Nrh3xOB2C6drfkIGELa9lxphSoZ5_Fq3xJ2gpFXZ41qiQIEV_qyZQ13vzJc8ONnN1YNxjN6E6-BYudr10G_y6Mm2QKod0GA_wTeFYFTMQvAuaCxt_tyOP6P1T_3_vblknrAZncGcbjuQt9VdnbrQ3h1H-PpeGyrD-3_iMavmSPHussbO7ymt_wOKED8HuE_I1esM382Mnytm6vOpXJjuQH8GOM3XEYHn5zcl0Wm1B5SaetJ2-R5Da288qDRvcVlqcvCRuuaJUOljbeQ6hVMYoSGSaz16lPszK8i2j-Px2cpfZ7vRZed00eWTKGl48GUJne7HyzkaeiRhOBBsBMM1MwN0e4bW3oiDQJ4IokTQEyC4L7EkofirljCxd92G2HwhH4XwUNrF7VCaJ_79xLC5xWulgr5yRuSiN66WtJRr1dJ26mmO9EGPFAUPregnnPZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0168d013f3.mp4?token=iBPNR60c8gUNYv9lC5xxIGEydUJmmvFd_gq4w9KQCwKGA2fojlzR7rUBeA81K5Lo-RQwzEXM9stA9RPJNsUjC4NC0FKcH-RlAHhzyFI4AFqqoWtzZlvWOo6IFwsV6YvKJIDFaWjzHjs1FWfOoATlWvJxIDM7NeFgZrHbwe_h0pmV_K4-WBsOuFwCA03jgN9jwaY0xVJHAUC6iSqMaPe8LsuRbJm9kg2U3HLNKaIqDO2Nrh3xOB2C6drfkIGELa9lxphSoZ5_Fq3xJ2gpFXZ41qiQIEV_qyZQ13vzJc8ONnN1YNxjN6E6-BYudr10G_y6Mm2QKod0GA_wTeFYFTMQvAuaCxt_tyOP6P1T_3_vblknrAZncGcbjuQt9VdnbrQ3h1H-PpeGyrD-3_iMavmSPHussbO7ymt_wOKED8HuE_I1esM382Mnytm6vOpXJjuQH8GOM3XEYHn5zcl0Wm1B5SaetJ2-R5Da288qDRvcVlqcvCRuuaJUOljbeQ6hVMYoSGSaz16lPszK8i2j-Px2cpfZ7vRZed00eWTKGl48GUJne7HyzkaeiRhOBBsBMM1MwN0e4bW3oiDQJ4IokTQEyC4L7EkofirljCxd92G2HwhH4XwUNrF7VCaJ_79xLC5xWulgr5yRuSiN66WtJRr1dJ26mmO9EGPFAUPregnnPZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زاکانی: آمریکا صلاحیت ندارد برای مذاکره تعیین‌تکلیف کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/akhbarefori/653359" target="_blank">📅 14:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653358">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
راز رفتار متفاوت ترامپ در چین فاش شد!
🔹
ترامپ را که همه با تحقیر، داد و رفتار تهاجمی می‌شناسند… چرا مقابل چین ناگهان آرام، حساب‌ شده و حتی مودب شد؟
🔹
جواب شاید نه در سیاست، بلکه وسط تحولات ترسناک چین پنهان شده باشد.
🔹
این ویدئو نشان می‌دهد چرا حتی آمریکا هم مقابل «ابرکارخانه جهان» محتاط حرف می‌زند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/akhbarefori/653358" target="_blank">📅 13:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653357">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqKep6-HwqBmh-2b5CXFx17LuCqDubfL7FS7fUaNutiSd1qS8EVywWYLsPNxt-tChrQjuZsv2eaITMXzcDfAWL5fW7aBA2EYxtwrRekXaxwflixYse5xfciaRHPwrkZFkfgq7buR1JNnT2iozc9UpQtQZpMxnPY6MSuFc1ec3o2H0ABq8qEHnrwowD8xWg7KgFQhcricPZbJEXGBm0uQ6RKU5Jfo4SveYP5ePr_N6S2UVrEwgoZp-PQmhXp4MLJ_2xIZNpVzzjgJf3_4VOKowlXzbVQ_b52MiBEgajJexi27WT_rVQvhoFukQuXYLbgQJgqq70UC-EC-QS_H-r89zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات ادعایی گفتگوی پر تنش ترامپ و نتانیاهو بر سر ایران
یک مقام آمریکایی به سی‌ان‌ان:
🔹
نتانیاهو روز سه‌شنبه گفتگوی پرتنشی با ترامپ داشت. نتانیاهو ناامیدی خود را ابراز کرد و به ترامپ گفت که معتقد است به تعویق انداختن حملات مورد انتظار یک اشتباه بوده و رئیس‌جمهور باید طبق برنامه ادامه دهد.
🔹
یک منبع اسرائیلی: در طول این مکالمه یک ساعته، نتانیاهو خواستار از سرگیری اقدام نظامی شد. مذاکرات جاری، نتانیاهو را ناامید کرده است. نتانیاهو استدلال کرده است که تأخیر فقط به نفع ایرانی‌ها است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/akhbarefori/653357" target="_blank">📅 13:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653356">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
اسامی ادارات پرمصرف برق اعلام عمومی می‌شود
🔹
معاون وزیر نیرو: به ادارات پرمصرف برق، اول اخطار داده می‌شود و در صورت تکرار و رعایت نکردن، فهرست اسامی مشترکان پرمصرف برق به صورت عمومی اعلام می‌شود.
🔹
در مناطق غیرگرمسیری یک ساعت قبل از تمام شدن کار باید دستگاه های سرمایشی خاموش شوند.
🔹
در صورت رعایت نشدن مصوبه، برق آنها قطع می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/akhbarefori/653356" target="_blank">📅 13:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653355">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
الجزیره به نقل از یک منبع پاکستانی:
🔹
مقامات ایرانی از پاکستان زمان خواسته‌اند تا خواسته‌های آمریکا برای مذاکره را ارزیابی و بررسی کنند
🔹
اورانیوم غنی‌شده، گره اصلی در مذاکرات آمریکا و ایران است.
🔹
فرمانده ارتش هنوز در پاکستان است و سفر او به ایران بستگی به نتایج سفر وزیر کشور دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/653355" target="_blank">📅 12:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653354">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
واکنش کوثری به اقدام امارات برای دور زدن تنگه هرمز؛ آنجا را زیر آتش می‌بریم
اسماعیل کوثری، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
قبل از جنگ به امارات نامه دادیم که این مکان ‌هایی را که در اختیار آمریکا گذاشته‌اید اگر بر علیه ما استفاده کنند، ما هم این حق را داریم که برعلیه آنها شلیک کنیم.
🔹
می‌خواهند لوله بکشند خب بکشند، اما این گونه نیست که بگوییم پایگاه‌های آن‌ها در امن و امان است و حتما به ضرر خودشان می شود.
🔹
اینها می‌خواهند بگویند چون ایران تنگه هرمز را کنترل می‌کند، ما هم استفاده نمی‌کنیم و به آن طرف لوله می‌کشیم.
🔹
ما هم می‌گوییم حالا که شما این کار را می‌کنید؛ یعنی می‌خواهید به آمریکا و رژیم اشغالگر اجازه بدهید که از سرزمین شما بر علیه ما استفاده کنند. ما هم هیچ موقع گذشت نمی‌کنیم که آنها به راحتی بیایند و آنجا را قطعا زیر آتش موشک‌های خودمان می‌بریم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/653354" target="_blank">📅 12:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653353">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
آمریکا تهدید کرده که ویزای هیئت فلسطینی در سازمان ملل را لغو می‌کند، مگر اینکه «ریاض منصور»، سفیر فلسطین، از نامزدی خود برای معاونت مجمع عمومی سازمان ملل انصراف دهد!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/akhbarefori/653353" target="_blank">📅 12:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653352">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
۲۰ ملوان ایرانی ساعتی پیش به میهن بازگشتند
🔹
سفیر ایران در پاکستان: از اقدام انسان‌دوستانه و خیرخواهانه دولت محترم پاکستان برای پیگیری آزادی ۲۰ ملوان ایرانی که به دلیل توقیف کشتی‌شان در آب‌های سنگاپور در وضعیت نامناسبی قرار داشتند، صمیمانه قدردانی می‌کنم.
🔹
در این راستا، از تلاش‌های خستگی‌ناپذیر نخست‌وزیر محترم و وزارت امور خارجه پاکستان، به‌ویژه معاون نخست‌وزیر و وزیر امور خارجه و سایر نهادهای ذی‌ربط، تشکر می‌کنم.
🔹
این ملوانان پس از تلاش‌های دیپلماتیک از سنگاپور به اسلام‌آباد منتقل و ساعاتی پیش به میهن عزیز خود بازگشتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/653352" target="_blank">📅 12:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653351">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bikMjEExAnP13-qEPrRpRcJgyti18QktuBk9A2fSxyR62uUN56RNLEBhboQ6tmPaWPYZv05IzFmpL77D-xHR7l7SLnstOvamq4GfIXLguncsBpSinvdOyehIAVA8V4pMxO1oCSoPXqzA7x2hnsmpi6uY9QWFXt2DsRcKfGtUpy6rDBjQIn1FliPc3ege_hGxeAFsUyuFy_EVLEabWH3nEemIaWrTrEqziF8DX6u5RUXSAHJ_3pT3Ym9NjGCOGuRzQUKVXX4smysx06dn3pTTDv44W-iWj91bsQmCtnNxMDogVoJ7aqJDGVRVJDakkzw5XLXTcRI0ZSJm-prB1gLQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عملیات شکار پرنده‌های آمریکایی
🔹
۴۲ پرنده آمریکایی در جنگ با ایران از مدار عملیات خارج شدند؛روایتی از هزینه واقعی جنگ در آسمان خاورمیانه.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/akhbarefori/653351" target="_blank">📅 11:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653350">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkHsfLQO9cS30_Iyny0EsBpBT0qcglPy8icnOVq6rrDgxX4sfFO82_SZlAeodyHOI2yyBpIDL4xTPX21VOT1sR-gGKdJTpW_DKSLJY152iI3f2W5oQ98hylB1NbNvW9EVAXLJjFdnqYaRL8IQJ1dI7biQiK5YB1pUIaaIh73pW-XSvsYUZLivy0uQreYanLZf6UzoWquiVeuvVh-3NWzdXiE3DWMfFZyvhuROPxSJTiakteK-F8WY1oaQQyfnthi_1RysEo2_fVqbb_zrAch7sgDBkVySrhu4t6utMubO9mxzWLgTBGFSLjLZk4H4MHjp2_Z8jR2JTRgO2CcAsTS5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهر گناه؛ چگونه با وجود جنگ، تجارت جنسی در هتل‌های دبی رونق دارد؟
🔹
به واسطه جنگ و تنش‌های اخیر بسیاری از کسب‌وکارها در دبی با کاهش شدید مشتری، افت فروش و رکود گردشگری روبه‌رو شده‌اند؛ اما در میان این بحران، بازار تجارت جنسی همچنان فعال و حتی پررونق باقی مانده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3216745</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/akhbarefori/653350" target="_blank">📅 11:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653349">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bc0005ed4.mp4?token=jgWLnUowRKD7OBHGXUAR21OoLugkxCYgYJXAsgsQmmQc1NsX3OrVmSd03Y4T1E4qckM0rCnObO0OOIaRyiqG6X7AczP9r4s7xXBJgFa79JrpoRo_FMqOMo2ltPNrU0LMmigJhIRB5pTZHopyFxTlWXN63LNF0cOWx4ne9mGFbwGqnx7HtoC1NuQ1gG_Nrc9zMccTMegtOFiKPzifRSj1IUiLZ4wW_hP0zDFQ2HGYWNpNmIHvNbXlDFkLNPidv_k99Pjk8-xyluMYXvCUqDwN5c0sBrcSwDnI4jcewzEAT1uzsiqgqZr-Q20AE6vJRQK4Zr-hnbdQPVc9t--pFstZ6YUOeCvjfMR3R8hj7KLFr3wO-TDqtB2O3wYjhi4fQPQveBR49qCVs6ckG6h3QNXXLBc5WdXCzm6uJat3UmheB0nLn79vvdHsr9JP_XEA174HQsFapLlpHbl0miT4tWGTKmseW9G-Tu3mCqxQcX_tg_oGvu1J9JEyomXMK6f_PjJExkDPnOxX8Lz5MLQLYgJ0hBC2TcWjdAHRrHRBDVuRPvvv2j0D3QoxM680M7cerDiF1JUZ3QlAA0CSzFATtq7uoFtFBGw-aOL9Ddi2D1HXM8_Pyw2xUHd8A30Sh3_w8tWMTH4TmRXzrBuq_6jjULNqe1-pH6NSi5dC3b4GgM-Ftgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bc0005ed4.mp4?token=jgWLnUowRKD7OBHGXUAR21OoLugkxCYgYJXAsgsQmmQc1NsX3OrVmSd03Y4T1E4qckM0rCnObO0OOIaRyiqG6X7AczP9r4s7xXBJgFa79JrpoRo_FMqOMo2ltPNrU0LMmigJhIRB5pTZHopyFxTlWXN63LNF0cOWx4ne9mGFbwGqnx7HtoC1NuQ1gG_Nrc9zMccTMegtOFiKPzifRSj1IUiLZ4wW_hP0zDFQ2HGYWNpNmIHvNbXlDFkLNPidv_k99Pjk8-xyluMYXvCUqDwN5c0sBrcSwDnI4jcewzEAT1uzsiqgqZr-Q20AE6vJRQK4Zr-hnbdQPVc9t--pFstZ6YUOeCvjfMR3R8hj7KLFr3wO-TDqtB2O3wYjhi4fQPQveBR49qCVs6ckG6h3QNXXLBc5WdXCzm6uJat3UmheB0nLn79vvdHsr9JP_XEA174HQsFapLlpHbl0miT4tWGTKmseW9G-Tu3mCqxQcX_tg_oGvu1J9JEyomXMK6f_PjJExkDPnOxX8Lz5MLQLYgJ0hBC2TcWjdAHRrHRBDVuRPvvv2j0D3QoxM680M7cerDiF1JUZ3QlAA0CSzFATtq7uoFtFBGw-aOL9Ddi2D1HXM8_Pyw2xUHd8A30Sh3_w8tWMTH4TmRXzrBuq_6jjULNqe1-pH6NSi5dC3b4GgM-Ftgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودداری شرکت قطعه ساز کروز از تحویل قطعات به سایپا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/akhbarefori/653349" target="_blank">📅 11:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653348">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43cc421836.mp4?token=TAYvDZG8b0hsPWRxUIO_BlY2KGrcDfpAvCeQ3hD7kV-9W6jcMNQyTtplboKBuQDMVkPEjlydsG90j1q3tv3P4x_HPflsoAMFMYqy4KmctSOulooYhOXH14LO2iiIZ25z09kFuyj6ZcURRvyEvR-YV7B51RkfTEFyL-Qdqki0KnKRMPaEcwWpeg7nBnY4DD2Ws0BiavK0Z4Abix9lcb-3uwY4AtDtrVwPl4Ho2hGU0GKZsabYQXxpaDWMyfdyNWIAb9UGkjIevkoU1MQ0JNpTIGYhLp0l0KVxJlXHR6wS1K87EMUAiRB81jOoboB9zxgoT3_kTUT9w3pkuNK6xgJ6bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43cc421836.mp4?token=TAYvDZG8b0hsPWRxUIO_BlY2KGrcDfpAvCeQ3hD7kV-9W6jcMNQyTtplboKBuQDMVkPEjlydsG90j1q3tv3P4x_HPflsoAMFMYqy4KmctSOulooYhOXH14LO2iiIZ25z09kFuyj6ZcURRvyEvR-YV7B51RkfTEFyL-Qdqki0KnKRMPaEcwWpeg7nBnY4DD2Ws0BiavK0Z4Abix9lcb-3uwY4AtDtrVwPl4Ho2hGU0GKZsabYQXxpaDWMyfdyNWIAb9UGkjIevkoU1MQ0JNpTIGYhLp0l0KVxJlXHR6wS1K87EMUAiRB81jOoboB9zxgoT3_kTUT9w3pkuNK6xgJ6bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توقف اسکرول. شروع کاوش.
به بهترین کانال‌های تلگرام غوطه ور شوید—انتخاب شده، دسته‌بندی شده و تنها یک کلیک فاصله.
🗂
کل کاتالوگ را اضافه کنید</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/653348" target="_blank">📅 11:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653347">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQ8G5OtYt53cDCkhZLl1MUYlrvIBsSuUWjioI8lz0fJXPLZUiOlDt9wYsZ4LLc38-GiOvlOTzOpIyCUKb1yMsWabduD8Xt6NVmf7lKYjZG1AwZgNL9unwuF7t54UZQP3Z46Blj1OojgdwbPGbZvMmnJ5s1h7HpJ7RNP_NwYjhEqVwrJ_g8xhyN4g4-I6xQePPeJZsSSzh0XNkrwIkA0u16stQoIfFEf4_QSMZeL15Nt6bWGGr5GiqIr7SFn_YgaVvyelAOjAVWYI-YdJ5z7u8aNDxJHFNqcD7PdkhPN3ScUI2mnSUyVbWmJFjOYMIWnmGy1GxaoBuXDLh2QKIgWnww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اطلاعات آمریکا: ایران به‌سرعت در حال بازسازی پایگاه صنعتی نظامی‌‌اش است
🔹
ارزیابی‌های اطلاعاتی آمریکا نشان می‌دهد که ایران سریع‌تر از انتظارات در حال بازسازی پایگاه صنعتی نظامی خود است و تولید پهپادها را از سر گرفته است.
🔹
«ایران در طول آتش‌بس شش هفته‌ای که از اوایل آوریل آغاز شد، بخشی از تولید پهپادی خود را از سر گرفته که نشان می‌دهد به سرعت در حال بازسازی برخی از قابلیت‌های نظامی تضعیف‌شده‌اش در اثر حملات ایالات متحده و اسرائیل است» این بخشی از گزارش امروز به استناد اظهارات «دو منبع مطلع از ارزیابی‌های اطلاعاتی ایالات متحده» است.
🔹
طبق این گزارش به نقل از چهار منبع آگاه، «بازسازی توانایی‌های نظامی، از جمله جایگزینی سایت‌های موشکی، سامانه‌های پرتاب و ظرفیت تولید سیستم‌های تسلیحاتی کلیدی که در جریان جنگ نابود شدند، به این معنی است که اگر آمریکا بمباران را از سر بگیرد، ایران همچنان تهدیدی قابل توجه برای متحدان منطقه‌ای واشنگتن است».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/akhbarefori/653347" target="_blank">📅 11:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653346">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904502ae0f.mp4?token=FalXlY-J0Evhk9iotqUgj90Di7ZAp1jCSw_CU2QDNNAgCQg_To1twVgK4REwZw9sv1dQsTlk4NET0OadTqFPCKGNalgYv2lHMP4IUYfQalIybDUEfUtr7O1JYdhAl7Hg7h6WPbZj7aCWV2qTVAPKaSMPDs35cVSpvDskgTIZWwUI9CerjomS92PJhb1auDQGOfij_eOH3P4AtXr8WPtXcM0KZlKQ6Xmjf_-2TFPCMq7bJMNvfzqwE2fNSMr2H0LLpfD0BCWzGJl2nDAnkB8EaJY2j3qnhlNpcQAG9zr_XS23jsC-7OC2SlzGK6wVraR-6JJIE3W6DxrUa7n7smSs_Lo04nZ5ccrnzDnJmU_qqEVOXBTRDSrs6UV4cwBDXvoilJ_0x02DrV59ZSgwASpf9TdjM9iYcPBNP6RGHqvTA3KuFf07_yrce301lHt_sjgt-sDZEU8g-edDp5fp8-ZKBwo4cHR3xOJcwxBK722oWCtHhUELXq0evk5Zp42A5V_QdxKaZx0T-6GyLN5DJUlxmErEUrQURIe9FNm0tGSAgW06MqqsgLb5pJ-C7wXFkHlylE6vFNq687OYRJtdEqMXvcXc64VruZmIdzz8OtgyQakl5t3qdt834uLLzf7jTlhMD4Qip529LoLUX9DaQZfbhfJ3Hng2lN_oWDISgaNTE8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904502ae0f.mp4?token=FalXlY-J0Evhk9iotqUgj90Di7ZAp1jCSw_CU2QDNNAgCQg_To1twVgK4REwZw9sv1dQsTlk4NET0OadTqFPCKGNalgYv2lHMP4IUYfQalIybDUEfUtr7O1JYdhAl7Hg7h6WPbZj7aCWV2qTVAPKaSMPDs35cVSpvDskgTIZWwUI9CerjomS92PJhb1auDQGOfij_eOH3P4AtXr8WPtXcM0KZlKQ6Xmjf_-2TFPCMq7bJMNvfzqwE2fNSMr2H0LLpfD0BCWzGJl2nDAnkB8EaJY2j3qnhlNpcQAG9zr_XS23jsC-7OC2SlzGK6wVraR-6JJIE3W6DxrUa7n7smSs_Lo04nZ5ccrnzDnJmU_qqEVOXBTRDSrs6UV4cwBDXvoilJ_0x02DrV59ZSgwASpf9TdjM9iYcPBNP6RGHqvTA3KuFf07_yrce301lHt_sjgt-sDZEU8g-edDp5fp8-ZKBwo4cHR3xOJcwxBK722oWCtHhUELXq0evk5Zp42A5V_QdxKaZx0T-6GyLN5DJUlxmErEUrQURIe9FNm0tGSAgW06MqqsgLb5pJ-C7wXFkHlylE6vFNq687OYRJtdEqMXvcXc64VruZmIdzz8OtgyQakl5t3qdt834uLLzf7jTlhMD4Qip529LoLUX9DaQZfbhfJ3Hng2lN_oWDISgaNTE8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا جنگ با پذیرش پایان صنعت هسته‌ای ایران تمام می‌شود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/akhbarefori/653346" target="_blank">📅 11:20 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
