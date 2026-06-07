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
<img src="https://cdn5.telesco.pe/file/VgNbf-e1ZHXDCRREoYooY-RC33BOoPlCj2W1jKXwT58HOf_-KZQNoJYpHJ9IMm5zr2kIbNdWaxzh_icZ3oe3DSyZJQKuT1HYmRwWlJJUYZ03VAEyesLwB-P2ep3t-KRO3LuyYSBvwa-qXVQfzRycYn5tm1xEhuLgviO-JabNdBbNAudgvMBU6c8rzK6o0FtRPvd-v0zUziZT_YTINCDe1G1xyAEChC08UbQFaBZdaPv6PkGMfZdre3Hyx9csnyZmr9pdzXvf1GguUzfBVcmZc_oTG0Udc-Tjgs9mv2BUqX6EwG8vecQR5fY3W6MKK4K-hDClRrzedsv9n7mE67iCwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 254K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 01:28:15</div>
<hr>

<div class="tg-post" id="msg-91446">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fG5dgRbpFoyUs57CdM7aDqsYhJlJLPQLOBHNaEKfuxZS_x0dQXXfYR-UP5lo_qMdFgYJo8lcB9wUV_xqAgPckpydVvw3vXn2qf9ch6aIr2DEGyPFHefEEncVJpa-aCjwbqBnyx9ovAaJvTZTqLSQyCnkLrsunRu4d7NlN1UYgmF2yjp2M5d0eR-XpBY-jtIt0YvPlVzhkeuuVGQ60SyE3jlidsafAgjMb1c6p4tek1OaRJtExu2HT7-s27kG2utMejEqzpGwyhRrx-87rR3ErhNVKtHWlsmCNm-a34vFInpqhew1J3gEtNbik6JfUntDqSij6jMc3An_PjDSM-mGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
منابع مختلف اسپانیایی مدعی شدند که پرز یه گزینه جذاب دیگه بجای اولیسه تو آب‌نمک داره که ارزش ۱۵۰ میلیون یورویی تعیین کرده و بزودی اگه اولیسه رو جذب نکنه، سراغ این بازیکن میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9 · <a href="https://t.me/Futball180TV/91446" target="_blank">📅 01:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91445">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/46b3a86a4f.mp4?token=s6wPggOJc3qRHyZ7zoGaKksZZVVvEvttGcD4O0DJ_gDU2nlbznxoghT6irZby2B5mLIn4fWHB5AgKVHr1AZLRZeHsSYSJuKiY2uBj0MASAB6oT5Wx4mNoK0ie1e8oCTPXYa79rOpLbI2-mFe4r9Z7hLqj5OLyeg3lKvHmEXCYXfc69f0VSbzmATy-vdFefujlOwjfX95UNJt-jYRbwOO5oI27mW8Jbga60n7Z87jPZ-eXuwEBER54atxPDgfdGEKLTcYRYuXSgAvMZoKkjTyAZauYOKB-hCguGKthzuVjFbWNPTd8jAU-iqqwOqIfSxTKdYcVekVYEzUZux6zoks3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/46b3a86a4f.mp4?token=s6wPggOJc3qRHyZ7zoGaKksZZVVvEvttGcD4O0DJ_gDU2nlbznxoghT6irZby2B5mLIn4fWHB5AgKVHr1AZLRZeHsSYSJuKiY2uBj0MASAB6oT5Wx4mNoK0ie1e8oCTPXYa79rOpLbI2-mFe4r9Z7hLqj5OLyeg3lKvHmEXCYXfc69f0VSbzmATy-vdFefujlOwjfX95UNJt-jYRbwOO5oI27mW8Jbga60n7Z87jPZ-eXuwEBER54atxPDgfdGEKLTcYRYuXSgAvMZoKkjTyAZauYOKB-hCguGKthzuVjFbWNPTd8jAU-iqqwOqIfSxTKdYcVekVYEzUZux6zoks3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این لامصب توی چهار دوره جام جهانی و در طول ۲۰ سال، انگار اصلاً پیر نشده و چهره‌اش هیچ تغییری نکرده!
🙄
کدوم آهنگش؟
۲۰۰۶
👍🏻
۲۰۱۰
❤️
۲۰۱۴
👎🏻
۲۰۲۶
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/91445" target="_blank">📅 01:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91444">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15a206df4.mp4?token=Jf8cwTIsCX9LHFYROyJ_7ZWDTYBPhLcFT6lBqGpOHnLVTxGAzigETAmYO05VSzHib2IqybMba4lOKhGCWV4lBucnFlk-bCdeJcRdc47JeiKA6xnbuXAd6CnWti5vfdNLFehVIT1KWuK14TKdTjQgzUa-51r8O5_s8xvd2oPMj-3HHKwknNvHO8lF0xVvElVV70r5gvCnS2U48_d8SGJ9pVSOdZY_qtrSkGcLyDDYQDEP8BeA8Wg6mXqKdRdCJgkraHKpf6ueAbId6MUOBZOtbaYyEgNJbEybI2jccAqcoATvrrh-H_Tzgws-C0Qj7CSWQE3ezTTrNbeEdn14uRZURQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15a206df4.mp4?token=Jf8cwTIsCX9LHFYROyJ_7ZWDTYBPhLcFT6lBqGpOHnLVTxGAzigETAmYO05VSzHib2IqybMba4lOKhGCWV4lBucnFlk-bCdeJcRdc47JeiKA6xnbuXAd6CnWti5vfdNLFehVIT1KWuK14TKdTjQgzUa-51r8O5_s8xvd2oPMj-3HHKwknNvHO8lF0xVvElVV70r5gvCnS2U48_d8SGJ9pVSOdZY_qtrSkGcLyDDYQDEP8BeA8Wg6mXqKdRdCJgkraHKpf6ueAbId6MUOBZOtbaYyEgNJbEybI2jccAqcoATvrrh-H_Tzgws-C0Qj7CSWQE3ezTTrNbeEdn14uRZURQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت صداوسیما امشب:
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/91444" target="_blank">📅 01:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91440">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWtbUsOifn1otdJC8jG3kCJLD-NqaYz6xifXrEtDKNM64FHkSKp798cySq1r6h76o_u1PqdlXvwXAuYVVWlRAut1ob7MLuGJM1oZDFZ690Y_sYoEZpzKKMjSw5wT90tTc03vcavEzON4J1PGMRs3ZZeLIs4QE0oz7DVDIOC6zxCMyqzT9rXYmWKYXGA-I7Lxhc3wMIYcu6VLH0OYG67JvEYGZPPUTBbkMLXw-iyxrqBDyvvynHwckgAcx_tstd8WUEPYKGJf64rKjihh_paazNJ9T6WuK5ZpbubEI192ivx8H19aG8bzI80JqG1WXPSCbIYSyigGpAbiP9f-w_2UGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QcDobAnXgd-Bmrvuc0zsg6llj_v86OtOpXc8JTM-bW8-ABcRmuYMnAeoaFN_1a5W9tN4ryXhSsJkTYGSQuxoIuyN3MJdCG7xFZ1k9YLP-QgDQy_FtRfvUGEwqq7YS3CQFPU5xQ95-qxARB4Wluk7B6quf89dCF3AnPkc4nBsxkAkO8qI3JvHpJAEhXFTzh741xwccoYTsc9L6T5SgwC5PxEvhAMKf1tVrpiFKqaaqX69utJlFoeoM4GgSHd3MWybg_oOz0C1D4arXmq9bb1g8wp5XzfbRLQmvXaMjIJEuBg-5zQYF6QyD48dpm9jX1jMzLE64cf0mURHzarQO4BREA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qgogB9WDEYBgYYIysycHu8ezeb8V6LHbLzWmY0I4pS_ku-CSk_PxWadlD7pUtUTT57MZVWh1vVOMOYbuDyqtsSNRu15E5sb_TprUUo4xi0Ni7qO_YLq5DzEmc2AqUEA29c2b-QElYBD5Yp1CsF7lZfaGq85er9eeJpnhmlvkqGOtnaHu5Dk4D23Tk7mGn9SnUiYDhlQfBnLgAyEdHzeiY4TFqNx8b8oyzWCMevNNR1Zpwt9kdiWWZUjZN8XMc_oPMFpWlCBtx_O_SwVNFkIjMAVRXvD66Ja-CI8iWnpv8gaDWij8rg8GLPLZij3zYch67EvSJT_6cik0EjcNtDaMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGIzbZ4fkq27-ANBBqNlyA_Hg5f2BQDpXh9B6fGRD9oRyi5LhqnSM1MbvQF2-RDunKTbVz4zZmaOnlHjNIUEAbi9dHAPk0F2VJTnGkuLfDItrySijVn3iauCL8YzHWLdt_a454LUAzL0_8NvD2o_MHjrGCb0FTrhbOPL9vGFbPI4n5n12hIiBfhuBCIdRGgxLcCSie6GHj-jyrsBwuVQhDoL-Cnz-HKg5NamP3lA5kcr_niFXsdW_h3gJpzFGrIVDTUdN9jnu0RxWN2ITNyNiJyVf5Kj4X9OofrqRGBJI6BT2FvpkbmkSNMB1oj0n50GQUPKfvDKzLryXhcwRAwldg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
شروعش که اینجوری بوده خدا ادامشو بخیر کنه..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/Futball180TV/91440" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91439">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
یدیعوت آحارونوت: در گفتگویی که کمی پیش به پایان رسید، نتانیاهو به ترامپ اطلاع داد که قصد حمله‌ای قدرتمند به ایران را دارد. رئیس‌جمهور آمریکا اعلام کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/91439" target="_blank">📅 01:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91438">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: اسرائیل و ایران هر دو ضربات خودشان را دریافت کرده‌اند و منطقه به درگیری یا حملات بیشتری نیاز ندارد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/Futball180TV/91438" target="_blank">📅 00:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91437">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
پروازهای فرودگاه امام از امشب تا اطلاع ثانوی متوقف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/Futball180TV/91437" target="_blank">📅 00:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91436">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/U2i67D4Z0c7d8LFmo8Uett_-_JBGTmMeGpnTTE4S_r6rVgJAal3QZdTQfPupO0JpoRhy-HrKaQDovbD-GHBpqk2LIcu20x3gT-ipAjOKbkMqSRWwV1xCu-GSP3cNrY_rSrKJK54ae0W0aw2HxDbAVLcs4CFRhqwV03wbp1HZzW63TPIub9_Ykt6T2Naxy6yRTr3c32bXC4HhRZntwsPM4w4RNsNT6mti48J7ZOPKO2C4ayDlaFhJUEqALKoLnN_P-wRrfOcELB53d439vXPctd4cvKmaspiVlxhGLcmMlWOKRRWeoj2R7NfvvY4V3IrU_c79MLGXLXF3uhAqgBgY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییی :
🇪🇸
Miguel Blazquez :
خولیان آلوارز 100 درصد به بارسلونا خواهد اومد
‼️
وقتی باشگاه پیشنهاد 130 میلیون یورویی رو ارائه کنه، او بازیکن بارسا خواهد شد
باشگاه در حال کار روی مراسم معارفه با حضور تماشاگران در نیوکمپ است
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/91436" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91435">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jowdc1Ae1mF4GdbzrnxSi4CxljujnZlKFDiHbTnxJVIsorXyXpCyqPRLFojPs6IaKaPT00BOd_DzA_1TnX3DA28uTIRk1ZLf-kac5NZpSQiRGBk8JIrdluGwfFLXtmsn9B59n-NMN-sjGIklJ-kvQCJIKRimhRYHAb50nwX4U0e4m1etyjjkLgY9ItaeGQ83yDONumHX5I28nepMqrB2ixb8wT14Uee9PcgQEPuM5Clkkd7bD5KoqODVfsNtxE4Il-QXXdzjEp0vbOakN-5UtiFAXx9gdf8lkxvBnVl8ix2h61KW033VhNdyYOyX2yV-Ka9SeyqKL4kO7vtVzug9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرفایی که ترامپ تو تماس تلفنی به نتانیاهو میزنه تا آرومش کنه و جلوی حمله رو بگیره :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/Futball180TV/91435" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91434">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFRdRL8kGJOiUXdB16IctrzzwJKLzM_1n-R6ELZRJbKoeCDGzrEtGlfI1464bEKExvwLlHb1CTIzIQVozFIxXld6ehi4OK-jfIdNGbe_PCoUAkfIqmqryZhF6H5WZUFDe8aSAYqAxqEwUt4Qh6waWkNaURSnfwMbBXBsl6q8vbI0PpfsK6eUgOka0g5JeqSR5_GEVibG0IympZ9FRoo7lnAd_twyiaVZm2dZ7YCJMjQjvwknBUrWpDKhzYURuwZdM_Wge95oKfb0MaDfaFxdQNfSZDnXabPosV8xSHNx3w6b-wUu_xZcUGXTVoC9hnH04s8U8uLJd6kZIgIRQ7tNHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه چیز به نفع کارلتو در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/Futball180TV/91434" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91433">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc3b1eadd2.mp4?token=cvZzForzokulMT35YgwTqNn1lxttu64nAM9gJAMtojihQ4Vsw-3IyAFkcGZlOBCuWByt4cj4hlGtwh_PCQzzLHqRt9SPbV9Eq2iDpHFXt9LPi8KRdGnRacRBA-rxCoBu3lDv6v2gjMLVgj-5KEwbP_lN2fuMNLjuoDCWP7bcTBb4WxFbRipCX2KKXu4qaMjzgJFTA3KWgnzszVAgvsoMT-b4WQszAyaSTBoB1TQEB9h0jbwFO5rTUicp8Sj619Z3fEAJXcmNZ3B7EBHiCEKKquI-y8ULVCVMsjolT9DvPg-OILBOy5Uti-Vt3Tj3NgoulLkYUSZ20mTNoAqFORycLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc3b1eadd2.mp4?token=cvZzForzokulMT35YgwTqNn1lxttu64nAM9gJAMtojihQ4Vsw-3IyAFkcGZlOBCuWByt4cj4hlGtwh_PCQzzLHqRt9SPbV9Eq2iDpHFXt9LPi8KRdGnRacRBA-rxCoBu3lDv6v2gjMLVgj-5KEwbP_lN2fuMNLjuoDCWP7bcTBb4WxFbRipCX2KKXu4qaMjzgJFTA3KWgnzszVAgvsoMT-b4WQszAyaSTBoB1TQEB9h0jbwFO5rTUicp8Sj619Z3fEAJXcmNZ3B7EBHiCEKKquI-y8ULVCVMsjolT9DvPg-OILBOy5Uti-Vt3Tj3NgoulLkYUSZ20mTNoAqFORycLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#
فوری
؛ فاکس نیوز :
با اینکه ترامپ به اسرائیل گفته پاسخ نده اما اسرائیل همین الان جلسه اضطراری تشکیل داده تا تصمیم بگیره آیا به حملات اخیر پاسخ می‌ده یا نه؛ و اگه پاسخ بده، چطور این کار رو انجام خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91433" target="_blank">📅 00:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91432">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paHdePMaQlL1y_gVTPUN7JcroUWOYqLXzqPJA-PiR7xLwFM7dyj1QOvqXdqBbeD0HDCB39eDgOiuKCHAwazJKrm4MrazYKIMOjpfd30P_jPzo9vumj6j8HSDNoetXjLJcwxYhbv_DWqVZfux1KO7I8CrKqUyuC9vWdvFOHEpzXsHBA1MyvH-wUxsScrLIYtvDIgWIH7aEAARZ7JLuNlNbvU0KyLxTnGAGzcXMOfa3ET1X60Ci3dLqZ8KigNCrvwr4G5ViSHY8U2V-MZmVGFEMkPsL_X0O3o83Lq9kj2jSUDCcC14E5p5Ea31QUNPK_xSSg4nFkydfjfcSmSnvy3bXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مراکش
🇲🇦
-
🇳🇴
نروژ
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
یکشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ردبول آرنا
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
مراکش در
۱۰
دیدار اخیر خود،
هفت
برد و
سه
تساوی کسب کرده است.
✅
نروژ در
۱۰
دیدار اخیر خود،
هفت
برد و
دو
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر مراکش
۲.۵
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نروژ
۳
.
۸
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب:
۱.۲۷
🧠
وقتی از بازی لذت نمی‌برید، متوقف شوید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/91432" target="_blank">📅 00:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91431">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
بیانیه رسمی ارتش اسرائیل در واکنش به حملات موشکی سپاه پاسداران
‼️
‼️
رژیم تروریستی ایران در تلاش است معادله‌ای جدید ایجاد کرده و با انجام شلیک مستقیم به خاک ما، در واکنش به حملات ارتش اسرائیل به ضاحیه ، قواعد جدیدی را تحمیل کند - ما اجازه چنین کاری را نخواهیم داد!
‼️
‼️
ما در واکنش به شلیک‌های بی‌وقفه حزب‌الله به سوی شهرک‌ها و مناطق مسکونی شمال اسرائیل دست به حمله زدیم. اجازه نخواهیم داد حملات علیه شهروندان کشور اسرائیل ادامه پیدا کند.
‼️
‼️
ارتش اسرائیل در دفاع و هم در حمله قدرتمند عمل می‌کند. سامانه‌های پدافند هوایی در سراسر کشور مستقر می باشند.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91431" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91429">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFU-ZEbp9QGHW9VyMccPzAebjqiiB_TJkuLIFfV7XEiqMbiP5V-C9TZ15oiglwWEBdhMQ54UrQO5F_kzjMTbZHKbTrJHApdBqbZJI2TplJh6d3RnptKjSODVdCJougwI0zjO7XeFpdu-LNpaUTLsbl9yuhsF_5VQno1jRjV3B5VhQwW0BGGAlQZSTbC4jqmhf4bXq9QyYYW9T6BojRT69F4-sfI_h6Q15I1AgAhDNn_KcIRrkzyLo7j_K2DnSo46Y75GLWYB2YsHV4B1lDzX3CCQQ54X4S-VfY6hXHx23kJsIslrT8KcXdHRDMEfHjILp5-t5hm73SLDDXZGYQsInQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1GM_liwJeFebROJkydajNs5SMP5j_MmXwwNHbqTmWnphvDLjF--LqAG9nxTcLXEC03_WSquJoDlqsVWNHZCdDz4obfPnkKSBFGKinecerhk1z_TCFxOVzc7Icj0eF5hdUBKTrFvIZbp686YEn2qPFJSvORr_kH959-eebbZVUDKHIp05SVOPG1mLnloHSHPwV5eW6LzDSn3MUX-4BgV3TVwNEfzJ09QvrN5c4wZZqELlTTeAur7Q9KrwJIiRj8Meyv6dtUXV3rAy0c-dl5pf_02LSAbWy5RZGKTHMTxDWriEzJ6wSB924qdlMGoO110amNgY5twlGYzOrIa7GuIrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇭
فدراسیون فوتبال سوئیس از وجود مارهای سمی در کنار محل تمرین شکایت دارند.
‼️
اونا در ساعات گذشته به دنبال راه حلی در سریع‌ترین زمان ممکن هستن تا به محل دیگری منتقل شوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/91429" target="_blank">📅 00:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91428">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
ترامپ : نتانیاهو جوابمو نمی ده اس ام اس دادم‌ نگران نباشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/91428" target="_blank">📅 00:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91427">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
ترامپ : نتانیاهو جوابمو نمی ده اس ام اس دادم‌ نگران نباشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/91427" target="_blank">📅 00:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91425">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
فووریی ترامپ:  اگه تا آخر هفته توافق شد میام تهران تاسوعا عاشورا غذا میدم تا ۱ ماه هم سیبیل و ریشامو نمیزنم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/91425" target="_blank">📅 00:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91424">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDU0mJeU3LTzSFDF_vyEqa0rZqTeB2_u8XcJBb-lalfmfTIZR7aTYvChmexcDdscTx-0K3dbAnyasAYoxJLOCCJJd-w7mJVCWpPu-d9VDwm8FJErstmoFSQAVRiLPIZJLSH8mxw_sUx1GS42U9pDvxkngR2VzuiOKdRdWnQm9C0mEzJ8pWkczoxK1IQaw4pUQEgYAIogDCkNVer-IQwikDt2m6c0frl5J64UpTyBmxfOrA989jACYXhMf9e9J7H-6U_BP-gZ44n4LgWynMwvlzH-tR7EbhdvgVvtiZhOp522SnvyaaPxuUgeWkqWynwYh8WS0C6cIHH7fEUPRXDizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عزیز ییلدریم به عنوان رئیس باشگاه فنرباغچه در انتخابات پیروز شد و هاکان صافی را شکست داد؛ وعده هایی که صافی در صورت پیروزی انتخابات داده بود:
❌
لوئیس سوارز
❌
میسون گرینوود
❌
هاکان چالهان‌اوغلو
❌
مریح دمیرال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/91424" target="_blank">📅 00:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91423">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
ارتش اسرائیل : ما به عملیات خود در سراسر لبنان در واکنش به حمله جمهوری اسلامی ادامه خواهیم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/91423" target="_blank">📅 00:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91422">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d9632a96.mp4?token=u9OMCIzslidBuKU5Phrgc5JqdHyxNLe_8lgyXkIe8QbtJurGQEpQ3-UywLOL6aaM_zYqa4MYLLQE5h__AQWFy0JxYpaGAwF8yrNkyhvKsCgHIDvrM-NYSsADjq6Ln3Xm9mvitxvP01dMo4mW2-N_kFVGgHodxoDGs0_ipXmlHykdIa6Iq3KskVG3-MwE_dZ9q9GX2bbRzi9IrOB5vM91qpbsCkf_ecSiG0yw5wcfdzmEHisE3ex5q4mws9CBgFaFkDcKihRETnxJOe5p4syfsrQxMS77NIcobfduMCJb8ai_zGgwFBmR-8kIMdqHJE-qEfqWE9DgZI6pRZq3Ju7pbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d9632a96.mp4?token=u9OMCIzslidBuKU5Phrgc5JqdHyxNLe_8lgyXkIe8QbtJurGQEpQ3-UywLOL6aaM_zYqa4MYLLQE5h__AQWFy0JxYpaGAwF8yrNkyhvKsCgHIDvrM-NYSsADjq6Ln3Xm9mvitxvP01dMo4mW2-N_kFVGgHodxoDGs0_ipXmlHykdIa6Iq3KskVG3-MwE_dZ9q9GX2bbRzi9IrOB5vM91qpbsCkf_ecSiG0yw5wcfdzmEHisE3ex5q4mws9CBgFaFkDcKihRETnxJOe5p4syfsrQxMS77NIcobfduMCJb8ai_zGgwFBmR-8kIMdqHJE-qEfqWE9DgZI6pRZq3Ju7pbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
این بار ۴۶۲۰۴۷۲۱ ام بود باعث صلح شدم به خودم افتخار میکنم الحق که جایزه نوبل حق منه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91422" target="_blank">📅 00:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91421">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خوب برگردیم به فوتبال
مراکش تا دقیقه ۷۰ یک هیچ از  وایکینگ های کله کیری پیشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91421" target="_blank">📅 00:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91420">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
فووریی ترامپ:
اگه تا آخر هفته توافق شد میام تهران تاسوعا عاشورا غذا میدم تا ۱ ماه هم سیبیل و ریشامو نمیزنم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/91420" target="_blank">📅 00:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91419">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
ادعای سخنگوی ارتش اسرائیل:
هم اکنون رئیس ستاد ارتش در حال تصویب طرح‌هایی برای حمله به ایران است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91419" target="_blank">📅 00:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91417">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
ترامپ : هر کدام از آنها خوش گذراندند، اسرائیل حمله خود را داشت و ایران هم حمله خود را، ما به حمله دیگری نیاز نداریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91417" target="_blank">📅 23:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91416">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی قرارگاه خاتم بالاخره پیداش شد: اسرائیل باید حمله به لبنان رو متوقف کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/91416" target="_blank">📅 23:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91415">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🇺🇸
🎙
ترامپ: به توافق با ایران نزدیک شده‌ایم و نمی‌خواهم اکنون در مذاکرات اختلال ایجاد کنم.   @News_hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91415" target="_blank">📅 23:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91414">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اینترنت به شدت اختلال داره!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91414" target="_blank">📅 23:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91413">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
فوووورییی صداسیما:
خونه نتانیاهو رو پودر کردیم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91413" target="_blank">📅 23:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91412">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حملات اسرائیل به بیرون هماهنگ نشده بود؛ اصلا از این موضوع خوشحال نیستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91412" target="_blank">📅 23:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91411">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حملات اسرائیل به بیرون هماهنگ نشده بود؛ اصلا از این موضوع خوشحال نیستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/91411" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91410">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خلاصه اینکه بالای ۱۵تاحواشی و خبر جام جهانی توی تایمره قراربود امشب پخش بشه ، ولی حیف
💔
کاش یه قانون توی دنیا بود که ۱۰روز قبل جام‌جهانی همه جنگ ها متوقف بشه تا بعد بازی فینال 🫩
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91410" target="_blank">📅 23:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91409">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوستان یچیزی
محض احتیاط دیلیت اکانت تلگرامتون رو بزارید روی دوسال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/91409" target="_blank">📅 23:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91408">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
ترامپ به فاکس نیوز:  پیشنهاد من به ایران این است: موشک‌هایتان را شلیک کرده‌اید، کافی است. به میز مذاکره بازگردید و معامله‌ای انجام دهید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91408" target="_blank">📅 23:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91407">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
ترامپ به فاکس نیوز:  پیشنهاد من به ایران این است: موشک‌هایتان را شلیک کرده‌اید، کافی است. به میز مذاکره بازگردید و معامله‌ای انجام دهید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/91407" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91406">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
ترامپ به فاکس نیوز:
پیشنهاد من به ایران این است: موشک‌هایتان را شلیک کرده‌اید، کافی است. به میز مذاکره بازگردید و معامله‌ای انجام دهید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/91406" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91405">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
جبهه داخلی اسرائیل اعلام کرد که رویداد در شمال کشور به پایان رسیده است. می‌توانید از پناهگاه‌ها خارج شوید
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91405" target="_blank">📅 23:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91404">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">عجب ملتی داریم
تو نیم ساعت از اخبار جام‌ جهانی رسیدیم به اخبار جنگ‌ جهانی
هعی خداااا بگم شکرت خندت نمیگیره واقعا؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91404" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91403">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران رسما اعلام کرد: پایگاه هوایی رامات دیوید، هدف موشک‌های بالستیک قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/91403" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91402">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
فوووررری
هواپیماهای سوخت‌رسان آمریکا از پایگاه اسرائیل به پرواز در آمدند!!
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91402" target="_blank">📅 23:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91401">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الان کادر تیم ملی رو گروگان بگیرن چی؟
😂
😐
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91401" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91400">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
#فووریییی
؛ موج بعدی حمله از قم و کرج و کرمانشاه آغاز شد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91400" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91399">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ifRmKINl9OFcb_xU0NfIbmBVGbhQA-ifZr0L4IsWLnAeC6fLmDcDjo0xbRWvepXjLggCQfal-VFclSstljjoMT8r5WnhpgutSYvbDUpJbV17VXYI0jbe4JeqU8sH3m3fOQwT044KxtU4nFUODsn9Otzgkrv9nxfam6rP_OvneddYuoKjERaPHD5_2AB7ZA_bWRYdBkxyjtmN9xmNPapaMoCS41MolM5wZZuDsN9IAy8WROkT6K8Art2wnZRU309UP-UsjEAKb-VrGnvXaNRfUBsCW2h-tekvus1KrfGBoOgbZ00kt-RoP2-tDwoxt5iXX-v2z2azVDgaReUWYQauKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعییی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/91399" target="_blank">📅 23:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91398">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سرعت اینترنت کاهش و دچار اختلال شد!!   @Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/91398" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91397">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🚨
موج جدید حملات موشکی سپاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91397" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91396">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
کانال ۱۲ اسرائیل:
امشب اسرائیل به ایران حمله خواهد کرد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91396" target="_blank">📅 23:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91395">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
ایران نزدیک ۴۰ موشک شلیک کرده است!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/91395" target="_blank">📅 23:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91394">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb2bd2c8a.mp4?token=DZl5XCgDs80z2eZP2g6r-cDLRnIFEDA5JA4IoGW3hDTPAnXBaRgfMMFYl5H4cS87DbMtHm4b83zkBo0IFBsVgtfEHORbTL2VpW99T2ZjBXGcsBb_Owols-EdWf5jSxgTXJZI_87W7QX0ii0_AaLYZ5IFgAICBtY3B20W9Lw-QvKUyKJu6rSPgqkvHuvjgbiwxmzM14lPMGL_eFoM1S9EasV2NWO6A8MTCPBtyfKIZ08GyB-qyuU8GxisPVe0z0cm0wqJiUU6awloNglpmUmNqXAZ8sFnlkO_gpE3jHX-NdUlUdXP1Z4zNjGxLHCLgk4tqPB7MQi0bVcIOyScdeNDug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb2bd2c8a.mp4?token=DZl5XCgDs80z2eZP2g6r-cDLRnIFEDA5JA4IoGW3hDTPAnXBaRgfMMFYl5H4cS87DbMtHm4b83zkBo0IFBsVgtfEHORbTL2VpW99T2ZjBXGcsBb_Owols-EdWf5jSxgTXJZI_87W7QX0ii0_AaLYZ5IFgAICBtY3B20W9Lw-QvKUyKJu6rSPgqkvHuvjgbiwxmzM14lPMGL_eFoM1S9EasV2NWO6A8MTCPBtyfKIZ08GyB-qyuU8GxisPVe0z0cm0wqJiUU6awloNglpmUmNqXAZ8sFnlkO_gpE3jHX-NdUlUdXP1Z4zNjGxLHCLgk4tqPB7MQi0bVcIOyScdeNDug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
وضعیت کانفیگ فروشا، دانش آموزا و دانشجوها:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/91394" target="_blank">📅 23:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91393">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
والا نیوز: اسرائیل در حال درخواست چراغ سبز از آمریکا برای هدف قرار دادن تأسیسات انرژی ایران است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91393" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91392">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHCVSBXz1QHMHqCcxByFcz_EgU39WphQIFvEoln-VKcBE7VbJmmyRRc90finIAW2Fd8wwuImDB81LXX8alvuppQrzmE5IKkoLUkH9vXx4w5S_U82547P9IqWEzgkQ-p4o-sMU9sRrkVuuavNiyVAREFqEfxjfOqv-sfM5DI2I7glxE9sEzCEnIZLlaStGMJHDVJfoRYmtGrcLOnVmM31QIv31buh2bv0p4K_Ioxlr13lHCegUy0FDkxNO4HVuhydFd94dWyBBvAks4uSdEnZukdq7bFQEeb-uVarp5CmtD14zfwmmVIyoLfyFKmwj-q4Wd5GHuwY3dKbmCa0ugJUHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
آسمان ایران کلیر شد!!!
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91392" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91391">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-poll">
<h4>📊 وضعیت اینترنت شما چطوره؟</h4>
<ul>
<li>✓ مثل چند روز گذشته و تغییری نکرده</li>
<li>✓ الان داره ضعیف تر می‌شه</li>
</ul>
</div>
<div class="tg-text">سرعت اینترنت کاهش و دچار اختلال شد!!   @Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91391" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91390">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سرعت اینترنت کاهش و دچار اختلال شد!!
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91390" target="_blank">📅 23:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91388">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a284a8676.mp4?token=Mj_La-QoaZ8qnU860KjQnfOS3kRL8eTNjDsQTFRwHUdAqHJnHfVXpyVMjGytXocZ9G-hMk6cAmbp3iTCrgb5q_lmHcdco9YuuC6Bp9jsCmDv2HDiXI_VWMNNnSYPTXhkLFK-LVkFeWU8tu1M1-SSB8k6K6DG1KSXC24LNUcmMVHOe3OX9v6XXLJZPQ_WK6F95d1wrDXJCT-klXgha5NnCEbEb0YZVsUERo5dQrACfSR4qcXC90n_bEC3VE0PVUqy8nI0KbG-cfixUgrnfWFN_GCzQx5xSYemkUUaVCiutpBu2kpl9_neNy_Fp0YCqM5N9_Cxyr4yfBgQXGYt6A0S1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a284a8676.mp4?token=Mj_La-QoaZ8qnU860KjQnfOS3kRL8eTNjDsQTFRwHUdAqHJnHfVXpyVMjGytXocZ9G-hMk6cAmbp3iTCrgb5q_lmHcdco9YuuC6Bp9jsCmDv2HDiXI_VWMNNnSYPTXhkLFK-LVkFeWU8tu1M1-SSB8k6K6DG1KSXC24LNUcmMVHOe3OX9v6XXLJZPQ_WK6F95d1wrDXJCT-klXgha5NnCEbEb0YZVsUERo5dQrACfSR4qcXC90n_bEC3VE0PVUqy8nI0KbG-cfixUgrnfWFN_GCzQx5xSYemkUUaVCiutpBu2kpl9_neNy_Fp0YCqM5N9_Cxyr4yfBgQXGYt6A0S1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رهگیری موشک های سپاه در آسمان اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91388" target="_blank">📅 23:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91387">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خیلی دردناکه که تو گروه ها و کانال های ایرانی هیچکس از احتمال حمله متقابل اسرائیل نگران نیست، اون چیزی که همه رو میترسونه قطع کردن دوباره اینترنت توسط حکومت است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91387" target="_blank">📅 22:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91386">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
فووورییی بیانه فرماندهی قرارگاه مرکزی خاتم‌الانبیا:
اسرائیل با ادامه حملات به جنوب لبنان و ضاحیه بیروت، از خطوط قرمز ایران عبور کرده است. در این بیانیه، آمریکا به حمایت از اسرائیل متهم شده و ادعا شده که از سلاح‌های ممنوعه نیز استفاده می‌شود. همچنین تأکید شده که ایران پیش‌تر هشدار داده بود در صورت گسترش حملات به ضاحیه بیروت، اهدافی در اسرائیل را هدف قرار خواهد داد. در پایان هشدار داده شده که اگر اسرائیل به حملات خود ادامه دهد یا به اقدام ایران پاسخ دهد، با حملات شدیدتر و گسترده‌تری مواجه خواهد شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91386" target="_blank">📅 22:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91385">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fubCz7TpCliAQSjE8pQIY0BZOQAWR40SkiVUXSkHe3n1bYCfM1k-1ePDozR3Gn-zabnVVxiByHHkmOIxPpRKR0MCCizV6dGcaAXQA8U7rhcvzQGRs3VaVlGKKOtooaJm6o9XwH8vi7Mw3XRRxive10EifcU7hKdtPsgDCLLt1zUzkvUtVBXHBPovNsBsPvhT8pbYjZ6UZPDKZJEzTEWOe8O-aMY1I5AT7aq1d8uH1Da1anrLTcqpZmZDYABopMckoNBFTaK6fUqJEsjTC56mhCRvdFCzn5WyPxtw1mZ_vAZXxnmZQVkXDU8suAG5JUu2J5Z6W0r07rthry3o4DHaMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بن گویر وزیر امنیت ملی اسرائیل: امشب تهران باید بسوزد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91385" target="_blank">📅 22:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91384">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d76423eea.mp4?token=FG6eUMOOFg-3_N2EQ8Tv2Y6ZgmY1bXzGuiR3nC8l291dvnixxCwvsq1Geh4WO-iCVrYHTmGPCXNrfUaDX9aPF7vIAaEANOGpVuiTOLVcHsOoXWQSUTsdHHmUikqnUAInfbVJAbFGRvEe8W254_TBN_hfq3jv28pc2g058GoJGRv0rwDRWbZGJvwQTtAskbt0jP5bdrsOCc65MC_WqkbRU772ThEoKs_fNRArQAFQJFY9D3blaDTOVzlvtbo9CLNEaXIumqrMnfo1aXFN4iKarDobN0gS7t9KOKCwiOs59bPEICVehktDSD1ApiyO6WiGjLTq8Ju2E41sR7U6YUIZUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d76423eea.mp4?token=FG6eUMOOFg-3_N2EQ8Tv2Y6ZgmY1bXzGuiR3nC8l291dvnixxCwvsq1Geh4WO-iCVrYHTmGPCXNrfUaDX9aPF7vIAaEANOGpVuiTOLVcHsOoXWQSUTsdHHmUikqnUAInfbVJAbFGRvEe8W254_TBN_hfq3jv28pc2g058GoJGRv0rwDRWbZGJvwQTtAskbt0jP5bdrsOCc65MC_WqkbRU772ThEoKs_fNRArQAFQJFY9D3blaDTOVzlvtbo9CLNEaXIumqrMnfo1aXFN4iKarDobN0gS7t9KOKCwiOs59bPEICVehktDSD1ApiyO6WiGjLTq8Ju2E41sR7U6YUIZUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات جدید از اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91384" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91383">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
حمله همزمان از اصفهان و تبریز!!
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91383" target="_blank">📅 22:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91382">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
فووورریییی
موج سوم حمله از تبریزززز
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91382" target="_blank">📅 22:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91381">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqpyO-wS-6fdwMDT-keFSKpNsA-pDkTQt9bRm-IBiHxPRUSiyNf38k4x60iExE3ZFaWXl0e8tdOE5mQse5_FsHOuRg2UHMmG0NxJ9g3LmQev_iBaNspiHlzURthbT2m44eFzijt7w_KeOXqpm97YXmcXUIFCm5yn4WDFo7ETe3r6l7C-YMXgvSzW_poH9YlSBO85hgNudj3q4H86tyvBVDxYBSmKIsIoo5IxcDnmWbRo1sdE2dwKggOWCbRPp4HsbxsuqP6g4lk58TpVjo166zurT0eorpPrcLyRf7pmqvdqbFGSQMtMDZb6610eVWs6XrPxu9yBVH_h2xmXeYe9KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
فیلتر شکن تانل شده با قیمتی
عالی
⭐
- 5 گیگ
75
60 هزار تومان
⭐
- 10 گیگ
130
104 هزار تومان
⭐
- 20 گیگ
240
192 هزار تومان
⭐
- 30 گیگ
340
272 هزار تومان
⭐
- 50 گیگ
540
432 هزار تومان
⭐
- 100 گیگ
990
792 هزار تومان
🔥
20 درصد تخفیف ویژه جام جهانی
JamJahani
👥
بدون محدودیت کاربر (999 نفر)
🔥
با خرید یک سرویس 5 کانفیگ پر سرعت
مولتی لوکیشن
دریافت کنید
🪐
|  تنها راه خرید مراجعه به ربات
🤖
| ربات :
@ActiveNet_Robot
✅
| پشتیبانی فعال تا اخرین کیلوبایت
🛍
| بهترین سرعت و کیفیت در ایران</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91381" target="_blank">📅 22:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91378">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgBeb7kQeym6Ew7Jt60DKAq4bza6MT-Y7WWmHRxmONIeDewRHRQj6SJrn9HRf-pNOr19s84vVFzncrLrLyPC_j3bMxDiLGGt1HA15T7JsPqVACjlpLZiEQk_KzerP-fM780SgZejyfI8hlZ5-lvSGkMW5w6gIwWQjYFngtgD1Jxfaft8tG75MKAEKqEG7mFk5zYVOo1CmHy__efTrmd1N3sMDJcytyzbYHiWguPj9eeog990Uwc1P7BZuZxf44-T0fRAZh_za2WbZv199RtPxrd1GQjk7Zn2k68eKQsC9LqyrSxMrUKKy1P2cbsUpyWqoCv_U7jo7dupnUWcpLgpXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91378" target="_blank">📅 22:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91377">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بیایین باهم یه خواهش از پرزیدنت پزشکیان بکنیم نت مارو قطع نکنه
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91377" target="_blank">📅 22:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91376">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
مقامات ارتش اسرائیل به رادیو ارتش و کانال 14:
چیزی به نام پاسخ محدود به ایران نداریم و حمله میکنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/91376" target="_blank">📅 22:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91375">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
❌
جمهوری اسلامی لحظاتی پیش 4 موشک از کرمانشاه به سمت اسرائیل پرتاب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91375" target="_blank">📅 22:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91374">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
❌
جمهوری اسلامی لحظاتی پیش 4 موشک از کرمانشاه به سمت اسرائیل پرتاب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91374" target="_blank">📅 22:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91373">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664dea4d38.mp4?token=j8_YvJ3yhRdp6J3ZJSJV4XrfmqBhdO4uVD0pd29yD_K9i8Fwo3MizoR3Gfj7iCQHnhR4db9S67x-pZDC7_5gxHFAPoI8psHwpjchG5GHXCGuKjf3BCz0dJOBKEbM5zupvqN2B5V9qxtPDjvB1Hcyg9F8QsvLR1PamtNna3NWFOwXyYPDuKyp6r9Om4ajhnAawTcsCvXWpvaA52SH-ps614N6g-8WBeApa3ExP296952KBvJx_it6NRDJDrdt1nR2glCYtqRATu2UR-FyzsCMebnaW2fgAhitHfmB46gaXW74QD5oNZ1cGfzWvAWxGsJld5cU0ZFg2JPYPA4nUFRdWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664dea4d38.mp4?token=j8_YvJ3yhRdp6J3ZJSJV4XrfmqBhdO4uVD0pd29yD_K9i8Fwo3MizoR3Gfj7iCQHnhR4db9S67x-pZDC7_5gxHFAPoI8psHwpjchG5GHXCGuKjf3BCz0dJOBKEbM5zupvqN2B5V9qxtPDjvB1Hcyg9F8QsvLR1PamtNna3NWFOwXyYPDuKyp6r9Om4ajhnAawTcsCvXWpvaA52SH-ps614N6g-8WBeApa3ExP296952KBvJx_it6NRDJDrdt1nR2glCYtqRATu2UR-FyzsCMebnaW2fgAhitHfmB46gaXW74QD5oNZ1cGfzWvAWxGsJld5cU0ZFg2JPYPA4nUFRdWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت پیوی کانفینگ فروشا بعد از اولین موشک:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/91373" target="_blank">📅 22:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91372">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بابا من تازه ۴۰۰ ۵۰۰ تومن برای نت و کانفیگ هزینه کردم
😐
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91372" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91371">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مدارس و دانشگاه ها و مراکز دولتی برای ۳ روز تعطیل شدن!
احتمال حمله اسرائیل؟🫪🫪
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91371" target="_blank">📅 22:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91370">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">چرب کنید حداقل ۲۰۰ تومن قراره بره رو قیمت هر گیگ کانفیگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91370" target="_blank">📅 22:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91369">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UITmPPJ5WdfxpPUaseqhTEysIJIlbPazDSnXGuQFVK_9Hvw8NuX5XbiH--o2-XockIsR05qFpDFr9fOVQS_MwSEii7UQ3bC_O-ycgPYhwOpX3rH2R__1kpZCgvFTDQm1Tm1zltwAF_tVqZxTFXCxURWe9h4NrjB6S-XUyVYj6oRf0aJt5kMXqZiyMc4i7kIq2Htiam5njxNLmYI7DMJwWUkc1NLdwb0xbaLaLVDM_bWaYwlYzm4j4EvyngH1_nlhr1V5a9V6JrTT20IPlZPVKPGbM9UQzs9OhQ6oh9_97WA5R5DTLQYTmd2Xls-521wPHHnSeGmbPHa3qPdMTmHaMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووورییییی</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91369" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91368">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
فووورییییی</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91368" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91367">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15acd81b3d.mp4?token=NP-9JG7cO7148z3fHwVLFiUML1Rq0rnx5ApYMyJP2sHMAhNa3OIZSCFqCk5EXAxOLxguF8URvvrk3OJ0E6_bbbC0OS4yh8uUkYH8cZmjlAHWTJB3SJ2aHeEZStunEh4dQmwemPAIoHTgIPxMa6YS5PBNZJUc2B3jEnrsrE656KbyTF2ACuKbn-I2YCRHMjNpvmzPHUhc7LAa7-2nGqYEkuQJMA_bcvB6K4DP84tbWAdkAdiXJ9dXBkWK4UZUnO8GpCsnbNC2IJFND1S2FDR241eqHVvgiKJMk7X079eYZPx_BpjnYzdK4yam9bGjX-qqhRUUc5DpqUjcmSRCJDfNNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15acd81b3d.mp4?token=NP-9JG7cO7148z3fHwVLFiUML1Rq0rnx5ApYMyJP2sHMAhNa3OIZSCFqCk5EXAxOLxguF8URvvrk3OJ0E6_bbbC0OS4yh8uUkYH8cZmjlAHWTJB3SJ2aHeEZStunEh4dQmwemPAIoHTgIPxMa6YS5PBNZJUc2B3jEnrsrE656KbyTF2ACuKbn-I2YCRHMjNpvmzPHUhc7LAa7-2nGqYEkuQJMA_bcvB6K4DP84tbWAdkAdiXJ9dXBkWK4UZUnO8GpCsnbNC2IJFND1S2FDR241eqHVvgiKJMk7X079eYZPx_BpjnYzdK4yam9bGjX-qqhRUUc5DpqUjcmSRCJDfNNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به نظرتون کدام تیم قهرمان جام جهانی میشه
☺️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91367" target="_blank">📅 22:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91365">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SB4YW-17dXFX-vxl6BYO1X-E-VxOzC-toiuJwgrzerGQjIZcbKpvULvtFtTJvCL1qa0m4mh18oWaxbVr7X24skA7Aox_sVf6ICATOUu-fSwHjkMZ7u14WBLfW6_gcf4Vshh3GS5bTPK4p9y0z_iablsl44qHQntdB3FBnsJLtWr6HOpQBIqDJrWXNlvM4UimMoLL4tlHpxok3pgLJ1q-aGUnBHFTumkWSjxxDflaDYPiEIMEkLEP08Ci9ICWZDYR0BCOvmE6QBbjXTp0oiU_UZzs2_ah_pIhz0gXi3Ewpxy3tr8m6UzMGVoYL7SJxYp7JzHYBMBySOrxC3YaDpfVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/475c525760.mp4?token=KOOA3A1eKJLXT2eO1P7nlK-8HGC1OLB8CDVleQ5vXxjqWauB6zVaamMe2Bc27mBCzzK46KGitJYIJliWtrH2p91u1Wx5OLg2zIS1A-q_QZCyhWpTur1weefXrRIvxFbjO8bPE9TDSTu3-AI7gIr28l_r0XDET-AMJcFO6YoSZk2jvGOantO_onGuAIbFyFDTccSAcn0q1LbyTVaeqzMdKD7Ip51BxoHxlKaPQDtpMISy2jCjl6nGJo4VPwEQNlBZjW5VBBUuKouollBCxhXRl_vTlXqHy1JP0FadjI8myaWx-zCZV9yY4fTkaBXZ_HfI9H3nwFK7QHuO6h2eQDxa8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/475c525760.mp4?token=KOOA3A1eKJLXT2eO1P7nlK-8HGC1OLB8CDVleQ5vXxjqWauB6zVaamMe2Bc27mBCzzK46KGitJYIJliWtrH2p91u1Wx5OLg2zIS1A-q_QZCyhWpTur1weefXrRIvxFbjO8bPE9TDSTu3-AI7gIr28l_r0XDET-AMJcFO6YoSZk2jvGOantO_onGuAIbFyFDTccSAcn0q1LbyTVaeqzMdKD7Ip51BxoHxlKaPQDtpMISy2jCjl6nGJo4VPwEQNlBZjW5VBBUuKouollBCxhXRl_vTlXqHy1JP0FadjI8myaWx-zCZV9yY4fTkaBXZ_HfI9H3nwFK7QHuO6h2eQDxa8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثر هنری خوشگل و ناز آدولف کروس تو جام جهانی مقابل سوئد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91365" target="_blank">📅 22:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91364">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7uy2q4g8TQ81AU7zuScR0IFXjjgLd4N-sOsBiu6u4oiWm9Q0Paw4QMt_uTdztfF42m5M-RvYYZBSHYCzItc9cZQx7s5n9kL772ebcyTrVaG7faa5va6P3n9w_CBFB6jYaG6B2FjsDynAyFL11v35VCbehVs8OIqCB94ExugWjr-jx9_t0Zee6i0HPKAuIVj3BdgrKs7vLdjohJXY7xc7ULQDFlOruqD2uurYfUKre7k93HZHx1pR5pggRWtrjAAMSgavDksVJ3q4RGScxHZT45-mD6wpyzAej6er7QCrC32OZsoBk06j3dXnKcS5pY4cTfq-zqHSZt7P-QI81Cpdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
10 شگفتی بزرگ جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91364" target="_blank">📅 22:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91363">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlNB1Y3qE9XNYKDLknyGP6jRvh0NvV3es-R94KL_054wUVPJGXmZfggrv_KcOyJEjXtnli0kOosimAWgF6MOgKvGQrdbsZVFB-qv-gLXfC5aSzvecozAIYWsDmNYIA1jFUIgUFQHHCrpRlG-Z-FPIcopMLRM0H1Yry_ALtLWUQ4CmKJkPdG0q04q10eENWPxzRwU9LlPCjGQIHOa4G0G72pup8dEHUoHYOSIBnH9IzQx0XvhhYqENWD8hGz0Jz74LsGzheto1BPU7Qd2wVVhFN4biv8jQtrKsbobBc4vErrGZ01FKz-pRXO3QOBX-54HfPZc-q8QjkAyMshYVNgywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰۰۶: حذف شده توسط آلمان
❌
۲۰۱۰: حذف شده توسط آلمان
❌
۲۰۱۴: حذف شده توسط آلمان
❌
۲۰۱۸: حذف شده توسط فرانسه
❌
۲۰۲۲: قهرمان
✅
۲۰۲۶ ؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/91363" target="_blank">📅 22:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91362">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
#فووووووری؛ فدراسیون دانمارک اعلام کرد که خطر از سر اریکسن رفع شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/91362" target="_blank">📅 21:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91360">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشمامممممم؛ اریکسن وسط بازی دانمارک دوباره قلبش گرفت و سکته کرده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/Futball180TV/91360" target="_blank">📅 21:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91359">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAKqJ30L-h6-hlHNeFbYs4AYuaLjJLibqKoDag9jM2B0FsKV_9zEmfv2y2N26AD12ekpS1JXU4TS9hV0CX6KstT216erYJkBQ-2W06yXEn5yyBbKYkKnPJtGp6ttUXyCxW8aDS5HA6w8x66fzRwEcQgKcV5Uz54JBjyqFluCRxkO4SVmNsspQR-hadJvtraSdOW8HBmARi8iGdmkZtUZ5B0BASExHGgZRfphxS5H7y28FvdzZTgms8iL0_rz4327D5kKwp7LQ6gwLAJXfW_AUu04ko0UiG1OfLB2vxaTsQmu9NWlepD5TJX6OBLE0WQ-T6eKH0IaDMnTcvggBXTOSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برند کیت تیم های حاضر تو جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/91359" target="_blank">📅 21:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91358">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🚨
د اتلتیک: نزدیک محل اقامت تیم انگلیس درگیری مسلحانه ای رخ داده و 9 نفر زخمی شدن!  @News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/91358" target="_blank">📅 21:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91357">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thad4hD9GNXUu8J-wJwUmMJBOdFVVc8Bm_SZ7sWY3Pxb4MlNWMPLOOR6uVvBKO0WsZP7NLblhurbkm0UFw5BnLdInjEZfVmqod-GfdEfzDIWLzbf6pw0-bRuW3E0owO8P2fK1q5OwzGuP-nPrEDrrPeoo2ophIWd3yEUOFbz3xCv9bHE7bWGRYpmn-ShQVjY5SsxbmFN_jYknW2gCUgLlS2uepkl3CA7DPvrZXtqc0_wiu4Z-uEN67EgQ4pxbI9CUWCVMQKbD_oYuQl4BvEjlaQ4kIlU52k9R1aVpm7POjQWIqt9oQqG4RbUJm-Wwcwgklvi7eA3tTtHw43zY2cs3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
‼️
داور بازی رو تموم کرد و اریکسن به بیمارستان منتقل شد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/Futball180TV/91357" target="_blank">📅 21:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91356">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5QnCN_p1ATv3lTOAhwYh5NiV8F33l-O24dBIy0aUGxF05ANxcuWZLe-MmY3B-B6jK4ITlBNZgd2e1-8J_zUMUmdeGlFbed3oyqKri8AOg_LSJK5obJ3bfLYkRp-2oMoVUvjfrJW_HML-kigh9Ja-CWLRXWNg4hTPVtrRBLOj_Nvrs9uMzPfL6NsCNMwxldCg4aY48XbXeJVAJu3yWtxVsXuf-cxsJD5lWPLa8D1OqUdOZ1sXE1_YHzFro_qVij7XmVDUIub7Abx5njCSzJa0V4DkzTzZKPN90B3Zp3ig9zdBk50C-M31oWoW0rZQdKU-SR5KBC6PgcjIylvt_PiZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشمامممممم؛ اریکسن وسط بازی دانمارک دوباره قلبش گرفت و سکته کرده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/Futball180TV/91356" target="_blank">📅 21:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91355">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf69fb6576.mp4?token=Kx2W3Ti57-zxzxnEV77GHKanBpZDg0wjNdBtdmLrYXmeW0EYDed0gjvcJtuqAeWzzDDs8JQJXXuHMOgLdiv72BZZehk3RVcMx16q5ohrdjg4vAjDaEOKteZHNzWbn-KKobhl1FG8xuTKa-0H1OpVh5Lfum1LZ3Dt4w_-B8gqoemFkDvsh4xzM1_KTyYDGk4xYCgEEuhPuV8Ej-lPb7kKVvuWHB5OSF5tqIndCja5HTT398b_73vs_LAy1WSmvPd86v_wVj-3yMHLeTu4hl91gGi3wozlxoy9zI6RkeR49lLxzhRp35SUx3yAWtP2pD91XSaXtRHCRBBWVZoEeJcj5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf69fb6576.mp4?token=Kx2W3Ti57-zxzxnEV77GHKanBpZDg0wjNdBtdmLrYXmeW0EYDed0gjvcJtuqAeWzzDDs8JQJXXuHMOgLdiv72BZZehk3RVcMx16q5ohrdjg4vAjDaEOKteZHNzWbn-KKobhl1FG8xuTKa-0H1OpVh5Lfum1LZ3Dt4w_-B8gqoemFkDvsh4xzM1_KTyYDGk4xYCgEEuhPuV8Ej-lPb7kKVvuWHB5OSF5tqIndCja5HTT398b_73vs_LAy1WSmvPd86v_wVj-3yMHLeTu4hl91gGi3wozlxoy9zI6RkeR49lLxzhRp35SUx3yAWtP2pD91XSaXtRHCRBBWVZoEeJcj5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشمامممممم؛ اریکسن وسط بازی دانمارک دوباره قلبش گرفت و سکته کرده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/Futball180TV/91355" target="_blank">📅 21:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91354">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhi6mkVbX6GaF_lxALRkEqrD7ZNyFm_PLck57Tz6C29b_d2di3s6iOOROfa3LmMSEPw1m124ByrbNrqed6UpthkCP8axMC1LufxK9Yps0mNm9wrb3W-2QpaAaG1gnjM8MTzu83ZwYksRtTw1xjY2Qoh7X43g6nlJi0ztipbAJlxHdmdFfIIpC-p7dSxa2egyyo65Ahe_s6nhK96gyQRTApq-a6bt1DSl3-yt7IQ7ZhsUyJUhCXZgbewXtEQkp8qTzWlSDWa9uQo94mHABbV7rX51wccEenvakKrKcbtihqok2OkRUuajXBT26iMn9MrCjQANDoCXZcv7HF4iUEl1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فلورنتینو پرز برای نقل‌وانتقالات تابستانی رئال رقم ۳۰۰ میلیون یورو بودجه تعیین کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/Futball180TV/91354" target="_blank">📅 21:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91353">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k81ubeZ-MqDOBf0kpW6UqjpK3mVGqmebMCog1CPdm1ty2ZriAOHYXNFhVNZ4rfC5dpNwe-zE7n65_UAaQTUcUlgcqgMBzaX6XbvFwIfmPU8Q6cSNKWx6DDEWtmr0uOTaRdulZtxlWo8LEzm2sUYWf-stoTHz2rfDFrtYqE0wrpB7uKK4KemmhrPNhh6in3SChhkAbNlwzUXXBDBYklLSD7CSTWxVVz329BRgEe57WFu-kHNwPR9czL7d-DiJ_PApXP9__qjtFTXHWJeFwTqdqibmPTeRQcIXHUl_DkdGot8loA1M_Jrp67FqzoUdeUu31iaBMtEpcvDNEgf22ID1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسکتبال هم جذابیت خودشو داره
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/Futball180TV/91353" target="_blank">📅 21:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91352">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e07c2b244.mp4?token=b5kGyo3mMXPNtbJIFJvrMZWf3WqEZADOT9WyiAbPFcEvj6px14A3ENGBjw2ZE9itYb4_Pog05Z1NKZswLWib8b5VUgCq1DeP2nY_MeC-_mC9_JUKtbv6Xzu12Wq497dLlZloaIierwD4oBTRr2BW98dwEM9bhu_xLS8Pd0wvVrEm1ewAntcW18oXbbm2wPXe7gjsphP2unkyyhHm2o5om8rKbXjkvE1dqOJmcFlyzLm48ElxvV6ItS9l_km2WZHYXLG2ZiiOb4Ty1zkU5cO84Sqf6bowNq8ZJKNvXEC0tOe4CS1TGlGlvdTrb1DFwbs5gKgH-LiEDFAV9IWwCzdg_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e07c2b244.mp4?token=b5kGyo3mMXPNtbJIFJvrMZWf3WqEZADOT9WyiAbPFcEvj6px14A3ENGBjw2ZE9itYb4_Pog05Z1NKZswLWib8b5VUgCq1DeP2nY_MeC-_mC9_JUKtbv6Xzu12Wq497dLlZloaIierwD4oBTRr2BW98dwEM9bhu_xLS8Pd0wvVrEm1ewAntcW18oXbbm2wPXe7gjsphP2unkyyhHm2o5om8rKbXjkvE1dqOJmcFlyzLm48ElxvV6ItS9l_km2WZHYXLG2ZiiOb4Ty1zkU5cO84Sqf6bowNq8ZJKNvXEC0tOe4CS1TGlGlvdTrb1DFwbs5gKgH-LiEDFAV9IWwCzdg_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح میم: لجندددددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/Futball180TV/91352" target="_blank">📅 21:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91351">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f9934c86.mp4?token=K76O9gh3TKkCgkMB7Ql0Zdz4ms2nE0k1qskjIb5LM64gLWF3vcjSnqRyTcH5iQW5XfioVNDrV5yB0SIF_27cwWaYGOLlq8OWkSx5nIXw0sVrpSweOGjYHXFI8ZxAyNBtFP3qGVsrymahULNSrrFexSR2R_Eq8bTb7-qrpWvD3fazfWTQpBkt6DaYLQUklcanqpcDbf0hwHXK6bYjE9ufyArbz0oub5AzcrGviJp7pfg4TSVJNO8Rn8dTQ4IW9fDN3tnPGiy14PJa_QWRe8_pXBZ8YVM9iySsH0F-31REJdPegN4iOZ15HN8tLUuyyipDQGDk8X0HoT5c3Fb25-ty0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f9934c86.mp4?token=K76O9gh3TKkCgkMB7Ql0Zdz4ms2nE0k1qskjIb5LM64gLWF3vcjSnqRyTcH5iQW5XfioVNDrV5yB0SIF_27cwWaYGOLlq8OWkSx5nIXw0sVrpSweOGjYHXFI8ZxAyNBtFP3qGVsrymahULNSrrFexSR2R_Eq8bTb7-qrpWvD3fazfWTQpBkt6DaYLQUklcanqpcDbf0hwHXK6bYjE9ufyArbz0oub5AzcrGviJp7pfg4TSVJNO8Rn8dTQ4IW9fDN3tnPGiy14PJa_QWRe8_pXBZ8YVM9iySsH0F-31REJdPegN4iOZ15HN8tLUuyyipDQGDk8X0HoT5c3Fb25-ty0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانو زهرا گونش از زیباهای والیبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/Futball180TV/91351" target="_blank">📅 20:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91350">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏
🚨
‼️
هشدار جدی پزشکیان: صدا و سیما نقدهای غیرمنصفانه کند مجبور هستیم پاسخ درخور بدهیم
🔴
@Perspolis @RedStarFc</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91350" target="_blank">📅 20:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91347">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇩🇪
🇪🇸
#فوووووری؛ هربرت هاینر (رئیس بایرن مونیخ):  ما باشگاهی نیستیم که بازیکنانش را بفروشد. اگر فلورنتینو پرز می‌خواهد پیشنهادی برای مایکل اولیس ارسال کند، می‌تواند خودش را از این زحمت بی‌نیاز کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91347" target="_blank">📅 20:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91346">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnpINz_bM2TRHUjcsocWt02NasG7B4-0EO6PiS3_glXcvYwhY0e0-PucHAGuUj5-umIZss43tKLzo3q-8JO6WBOkSA8H1CfFvlto9CD3E46Xii9x_be51wIiQEjfmXOiV3Tbp_lEPUaAwbC1SoFfH2A6eXiFDmhnGrKB4ouClIEecJ4414ok8XCO37-wdw9w4CXOUZ4wiuVErp3tS6g5Z34kviwg4GhG5mSgV_NDXL90kKewPZGfC9Tx9hUS3B2fZIFV-0WBplhXrHqPi3fCzFmoxsn4wcL-hAW8TbhTP8mXiMFhbE0_w9p0ylIKFTGgcxtuOBfLgfkG0OIqJf7S0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇩🇪
🇪🇸
#فوووووری
؛ هربرت هاینر (رئیس بایرن مونیخ):
ما باشگاهی نیستیم که بازیکنانش را بفروشد. اگر فلورنتینو پرز می‌خواهد پیشنهادی برای مایکل اولیس ارسال کند، می‌تواند خودش را از این زحمت بی‌نیاز کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91346" target="_blank">📅 20:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91344">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bzabup-cpxIhDtvv7WxMDpLxa5_MDhzb3Ogj8zqIW8bnlZDE0cHLHjnx0kAmcqFupBuaY9jnDq6JEA_xqJ269Ej46b1YJbkQIkfhR2ogDRxtEebh9TSByO0ga0jWltmBHeucQ1A-NpuoLD5gQmFn4yL1pg-sXp_3hAb9HDEllqE8l1gkFEST7jlx0kNdoUfNvP4l1IphW8CHFvMAn8knm4s6fS_inldDCqtwrOA0iBduGPF3CWQhxq6YqazQTyBEsEdhJZ7D-mSl6pCPtEpMwuk8P7MyqIZprVISkGyQd36F9QBbBZeScvtYagPsid5Ctm-4Ksa7DJxi2Vbnk2jxcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکت؛
کریم بنزما فقط به یدونه جام جهانی دعوت شده و بازی کرده و بقیه رو غایب بوده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/91344" target="_blank">📅 20:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91343">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0x0tj3dkg8e6JPZk2EovsvQOFVdAzbQfvvhj5EuJ2gzGfrQ0A1IkDgdEQtBV-3kyS8CQK8m9377_vQ4Lc2a3krYVnZzptpjAHTx2QEvj7ZnF6ujmbXOLi3yoMMNMUrj8kOK78Vf3I3DWzfI7sCCgAfLewmZx2uTvFj9ATeXKS-dPskKQmkr_CQ9hdclimIY69WQC7E6fcix6IxK0RWB6RPMUV64DA5QClIz13fEUB9uwfyMG3scKoyog5C4SsUTjuNs8Q7Qb6LsYdcUBLFL4tzohc3z1sOVBER49k3dv8fTNqm3UMnNkM4bX6ucCKfUILga86HWmRuHXHIG5daj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
چه کسی در جام جهانی گل‌های بیشتری خواهد زد؟
🚨
🎙
کیلیان امباپه:
⁉️
وینیسیوس جونیور یا لامین یامال؟
وینیسیوس
⁉️
وینیسیوس جونیور یا هری کین؟
وینیسیوس
⁉️
وینیسیوس جونیور یا لیونل مسی؟
مسی
⁉️
کریستیانو رونالدو یا لیونل مسی؟
کریستیانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/91343" target="_blank">📅 20:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91341">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hxy365AsVjnjlevmRJSYib9ZKdyjSV3de9dqSx04n3hIcuLB_iOIbz4ovr1WPZbr7DG66LbHkccJRbjuMvZBv2xp5DbWJkTK2nAiQ6UyGhWeJfZ2deJLsRvmsvgWXKBcnnTDkODm4NRkv7rHBC0-peB-U1FVVga-euV7hDTka7WmoSmEcAkv2ATbAUAJbMjUjuFrSmagMRYYKa8ThJ5_QZVPxH2Sb9DT3tM89_M0kb7SlqeEsZ2hHB8-ptPaOKruIt3p4TKRnapG0lX5c9RDz-iUMoa7tNJpnNLTHywiOe9q_1zTEKnTVFQpGfvNkd3sbu7i2jlXWdrDg5HLQXcCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SfUKXRAgL4fLewqdeBwLqAdfG6V-fmtv9R2-pU1rvERq_suBxtnMT3OrfqY1K5EiC4PmoWGT5UWoUxWZEaT6uF5Ad4YTWdi--2x7JaC8qkwo0xHpyhy4MTAXHteWPydgakc_vJe-22V4BJWLaFHzBBhXFvwvYTuNzBV8akYqFlHBaLoyWqrIOKjKXVkTmfuB5v1qLCJ5jK2Q6roqGWVn_6MROxKU1Kdq8tIPB2eZf84EaQtfkzhAf4orh25vZ5aOmoFi_QEtSie8miEhAb_vrDVZg25XsKoVDLxOlxp-_pqhBLGeHyPMHRJUFMhyI0ia-5RpM38YFrtikJmNIII6dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظر شما مراکش قوی نیست؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/91341" target="_blank">📅 20:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91340">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiesHcgKUUnvysjMNVuOMroytO0rf-GfAVyxw2nH-xoLv6DUVxHOSVw4fIHlpWU4SOxv7lB6zKobwiRp5iS8Q0mT5E-Lrp2PqY8BGvpyVbeeGLm0dngd3PTrcXcdG5XqDGy_wPiF10sJdZoL3N0uABoo1f5zaKnQqFM3x9NgdXJfIiofmrOBnBCHFjaGfOfVch8DAZ_Y-DTSIvr3EkOhPZARDcDxnk-lkg9Y8jEaQU2hXLrYjyBtN-rdUyCuZJip6TSXsM9alrTOluJjFaMLNTw743y2YDI-z0NUsuxaQA38-JRqsVqNhUhkAesEa98PpYl8wkuyH7JcVzdfN26hVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرژانتین با هدایت اسکالونی به 18 پیروزی متوالی در بازی های دوستانه دست یافت
🔥
• 5-0 مقابل استونی
• 3-0 مقابل هندوراس
• 3-0 مقابل جامائیکا
• 5-0 مقابل امارات
• 2-0 مقابل پاناما
• 7-0 مقابل کوراسائو
• 2-0 مقابل استرالیا
• 2-0 مقابل اندونزی
• 3-0 مقابل السالوادور
• 3-1 مقابل کاستاریکا
• 1-0 مقابل اکوادور
• 4-1 مقابل گواتمالا
• 1-0 مقابل ونزوئلا
• 6-0 مقابل پورتوریکو
• 2-0 مقابل آنگولا
• 2-1 مقابل موریتانی‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91340" target="_blank">📅 20:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91339">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vs-mVpk5Vir09P51CYDhALxIWxY81IXvmqTTZoA56-R0e8Fea3Oz73dDnXBP8XsyYIeIZelVrBVE1g9ardbi2UqcJJpJmaeHvxVGxE1DHU2YlUFtstRTCFTXrAy-knbhGwhx9S6JH6OG9JKJViJF_e-eQMD_0TQ5n2oIoFnQoKCsoRjQDt-7EBwpZkwt6lo-7rYq64zGfKux5v5laL-mQtsesZwLWjZPEMrtO36mr4d22o3XY63f9Fu-rcprv1sAvjvbDWSU-wTCpyUbQ9Ad9BYLoSOK3xEBNR6uYYqUef7D63tTtJHA8CiaYRjRmAeTDUWogLuNPmaKYt9ANigDkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◉ 5 توپ طلا
🏆
◉ قهرمان اروپا
🏆
◉ قهرمان لیگ ملت‌ها
🏆
◉ فقط یک جام کم داره...
🌎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/91339" target="_blank">📅 20:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91338">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVWp87ApDvlBwNe47igueYaADUDbMy_esreIfEuFtJU0q8DLbZYD1vukQyLGVTqsOjjzBwj86HwUZzbBKde-9BApDVy7wU07jIhSfw6DJG3DJ-JwthyJs1uKSi7uFoC4nwzlorkDvRItZuihNnT0toSaKJ4zo7zka18hYeTQHVZB7Z5yIxwCtFzTMHZdVnyZ7NpL79_zgIjGqmvdIr7XfC7bvAGVq3y9nC3VSsEif2OvqZOe0KYevqGBVLmrSP2U4T2UQdXrQW_NXKUzk4CVAlg1TuVOpNE2aTVfr7Mivth9bMN3Y70Si2bxShXmsY14MMcTUXUYnJTcPxVHmwU3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وسلی به دلیل مصدومیت از لیست برزیل خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/91338" target="_blank">📅 19:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91337">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_wrnAE9q9_0JnZkcxEYRefKy3RW0AvK3_eZsI96yTMXEKAZnpK3wAsXUM080a2NugmoaicK1gLbJfxy3d1r5ew9RgwCVOLkpSc6gaJ0hVRhxaHGYpnzYXOP5b46NPeL4aRNp_-4qByXzjYC3rlrAhBrwYdun3qQj9mVqolb_xn9pQWR6fqogvbMFbZv50XrseL89OsU3c_eTnvl2vtO-qlNep39Si13OcbMv6xOiFh-Je419DS4fIBxYcJcJdMvJ646jStfJ2Eca6qPbU1gAjmjJf0wuYqQTV0EN39BlhuWYjleqOxWcVE07GZWChENWUtddu4gsEVC_aBPH_LXpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وسلی به دلیل مصدومیت از لیست برزیل خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/91337" target="_blank">📅 19:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91336">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afa8f6077e.mp4?token=VloENB2ipZ14IN276kYdvQtfozM8z-phrfxqG_F-JyQZdwzaDGcxtsbcvryeDbLq7rnFNena0IiG5UimLVS2lraOQH54NmSHrTfs7h7DGOrgJf_XJbWg2FRetGmfgKxLtDlcIHldXtB0YL7pbtu5wET_Wh25OMdqno26wMAr0VOY35KKIQLO3nkXdXKyK02XDIh2iyIB9jlW0TN1IdywSyudU5Pa0XlbSIl12AGq8PM1g_725fs8vlkzzx7SJqJCfzK_8sBeQUkOQoYjWf8URmbX5DlNKIUpjiRpDeMmaidFCaAeIPLB8MMMVQ4brnU-L9eDXnuJBi0TL8pdLjiF6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afa8f6077e.mp4?token=VloENB2ipZ14IN276kYdvQtfozM8z-phrfxqG_F-JyQZdwzaDGcxtsbcvryeDbLq7rnFNena0IiG5UimLVS2lraOQH54NmSHrTfs7h7DGOrgJf_XJbWg2FRetGmfgKxLtDlcIHldXtB0YL7pbtu5wET_Wh25OMdqno26wMAr0VOY35KKIQLO3nkXdXKyK02XDIh2iyIB9jlW0TN1IdywSyudU5Pa0XlbSIl12AGq8PM1g_725fs8vlkzzx7SJqJCfzK_8sBeQUkOQoYjWf8URmbX5DlNKIUpjiRpDeMmaidFCaAeIPLB8MMMVQ4brnU-L9eDXnuJBi0TL8pdLjiF6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانو زهرا گونش ستاره درخشان والیبال ترکیه
🫶
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/91336" target="_blank">📅 19:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91334">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TqtPDf1WmNp6FbY36mwQMyIjgVXVKUoWP9tfpGHkNTegwq7ojOHdo5pHaIutJzLI3d0VPSMJjcBkz1ZHZIxlg9sRe7KRJWO6m0wGp5XBx5JmpXWRV9Q7Hisg-J-BMBcGsxSrR0WxzOxA-kQ6v5Dh9SflPCJXjpC71c2e0U25TogNBrxcidY3pje8UgS1MT-m64BXfMz69KHdNc5VQMDxKJTDCArERJfIBgndInlgXt9RXKm6phcLNVCp6ZTwfSi8snK-xw7-kio74RYs-1YsTAHG78yxsmi5grjPDfRTSqYpdPrAKVX1SJXSwYPEwBIaqfUoQLfsmUd8MjaPEXqSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RPPok8uqG88SbQgpb1VBrgIuR4E2-HAYHmVO4uljBrtaiETDtggfI_2ueHR8CCKqq-UUNkZWg-41qkmX2OmMiaXS0PctHVwI7FPrEqqA-maRI4FM58s2JNd2iDOI88MnRFL6Uh_hTExpHrmPiKAgVnSOedCrnDYnE5Mkd3vicKRI6h7ulckVVMwb8X7BrT2BjEvgbSyRFT6JlEiRlcj8NCI0YrW888eyCI1LxRhO8SZBY0mHJJWZT_noVeiAODTNl0KQkQvEBj84Jz2SRsMa99hryLfPBe8C2QgxDPJIKz0raD53K_ZUFEkWF1hfqNsnKnF9_3qwkpwhZyAkGEci4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حتی یک درصد هم نیازی به تست DNA نیست...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/91334" target="_blank">📅 19:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91333">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a6ddb8bf2.mp4?token=GiQ4CZEwzzAmujcCsueyLSlF4BG8GPOckLHeb-hLU5fFUYjjL1Ypfjitng5W_6QRHmtXeWBk9eT5Noj-vPzXwasp53k3W1VZJpuvor6Cduena6ha_PM8W9nbs-AVvJrvEVq04pFkLoW_nh3hmrQcuRpcYcnzdE8PZSPzF-Za2dBwOxqwYU-a5d5Oam0ACblszLczDd-eYwqbmffyU0p7YCJVSLHTTWm1SpnpTd8X05mxu6l6jP4NSaFNH5i_abEYnJdoQU1IL8fEQYDB5vwfPgv1ehGfL2Suva8tN8vZI1IhP3ciXr1pYvwoOVEUQG_nINwsSHyxxfUSrwtd5wsExg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a6ddb8bf2.mp4?token=GiQ4CZEwzzAmujcCsueyLSlF4BG8GPOckLHeb-hLU5fFUYjjL1Ypfjitng5W_6QRHmtXeWBk9eT5Noj-vPzXwasp53k3W1VZJpuvor6Cduena6ha_PM8W9nbs-AVvJrvEVq04pFkLoW_nh3hmrQcuRpcYcnzdE8PZSPzF-Za2dBwOxqwYU-a5d5Oam0ACblszLczDd-eYwqbmffyU0p7YCJVSLHTTWm1SpnpTd8X05mxu6l6jP4NSaFNH5i_abEYnJdoQU1IL8fEQYDB5vwfPgv1ehGfL2Suva8tN8vZI1IhP3ciXr1pYvwoOVEUQG_nINwsSHyxxfUSrwtd5wsExg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیروس دین محمدی: در یک بازی وقتی گل زدم، پدرم در استادیوم بود و از شدت خوشحالی سکته کرد و فوت شد
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91333" target="_blank">📅 19:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91332">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVRVFelmwENCQjKIGPNfeEU14ZPL3QC-UCAgjEFcZoKh3atemUCVnAy47oNlPblxrldKJM2jC6zakgHYYPYTmND7inM1htCnFsdpCVEKdmmIZKCJx26GI_ZxxM6XjU7tuf1VJtDJZytz0zrfnQ-ChzIlEYLUSSej1KKiXCjyjP0-b1hJ0LJEZvHAfJfiAasHb6JV368Ej9GZZNUHVSiX_6fHTy_ID0Bmgzd8D4RSWTrmF_vH9QTMQgHAOet_VAYk71WAZRpKL4VsPqxdbIVGmsOqtPIs8ZkZFtzUt6OrVNSdL6OJ_Y2CxG4YRi1yA_zZm1MASBbz-5JZ75c02IxWbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال:
اگه جام جهانیو ببریم، به مدت 3 هفته ریش و سبیلمو نمیزنم و میذارم‌‌ رشد کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/91332" target="_blank">📅 19:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91331">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHQC9OLKH0InFD93yurkhlV9lQ79eLfdVaxxI5SdCBf0uZwlhUNz_KiavnJpxVS7EK8pHDhtQNxfKSeoe5JMakB2xwgDrIFmwyy0YNKVIMR48wkdQj4rSs5rIdwi3bSxi48JKca33B9qckpHf8Pvy0-qZapumjEoLieEWAzJ0EamsSu76OUewXQuLYDddYGBmqqfb-WNIBkj4S6up1QX9DP-F9_sMfJMboHA2V9vg9RbKkJvwE5CTKL_KxQA7EHAqDsL678ohtvmbB0IPy2Hcs_idlupjqdiic2FM9yJT_M8Oj9O7tWBgw2d8kAdG_8Z0a0uH9fAD4PR2ytb66eEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزش کنید دوستان ورزش
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/91331" target="_blank">📅 19:11 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
