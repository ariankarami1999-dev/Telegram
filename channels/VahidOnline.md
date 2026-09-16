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
<img src="https://cdn1.telesco.pe/file/VEq_Rj8-vm-egh7Cm9i3IbN0odY2iQ80uWUd0si_WF2h6WIKg6aWWs2WZLA6cDzg-v7-N0Lcv8cRpCDhRoa6dBDVOZCYw5DDwU8PtcNbntly9Z1wQBvTJe-3w1xq383VBqU2t-7-PhKR5RxoKBju8cdvC4gAFGxJtvT5XSRvK82fdskvfKAzi7CR6uOeR_yXDlemWy87fJleRbXvzV_L-asb8KyIp8v8TlIGN_ndiuSSpr55yo7xh1kXYdvNDuGYv1utVM7hspnPbaDrEUcNXF7aeGpW2WeFBwQzoeuGgWDWOSUxNx-LVgYPbRVcFk-uwuT7N9qPVFvIuVmNo0dOjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 04:24:08</div>
<hr>

<div class="tg-post" id="msg-78399">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BGuOyJ_tUNtpH-HqU7DPK9bIXCao3s9WqUSRZ2bYGgvYFWcYXTv8bhcv6Mb-UF8q_ZSqCkTME1dbwkRH0jFJZFDMt_UagVt00QquUbZ0Ltm3WBGF185RGqKUTd5_O-uyGRgBH_rUyUj_LFrmjv7nxWjtEZk-CEqxlv56rk3mWO6pYfXErnTEBDMdRyFxRKbLRqKiLFo8JTrdOVzvsXUG7aZoeLDp26WmZSwTN3zuQ8yjzxFQqqae_AaWR6r7rn6IRTgEqhGEwl8yN3kALw0dqv_aD3hHW71E3JiBfLARV44Hxi4u9pgKVyGlLN9NOwUigxjgHeCSBkOJ4dAavj1UYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KidXzJzFtMyPdJXCj62RbXh82-I2u6jfB28t5Nc4rRDgiYl4CDGBKLUjqaDzm8woEJ1RxSroOvRKx7kdKIR0RQuUuzAIFpd77o1jFsqhlIj3Zm-W5bUWkurK4cHsldQpHabf6Fw7xI6HXYa-6FaX6fqMrIHVKNGo_ZaAwCNHrwF_6-NaqQpAC6B9gJrH5P8HxV7Ih9aKb-5Z4n1esXpL3hGqhMdZrqznY4T-t0ayO2cJKYV5KDBreEgk2kR5btmxyOwg6XaIDFCjmXsBjxF5juBcnuhU9ILdCLgeCrLKgy4RiiS15CxN0vTSKhcxm22Jt49ErQndktq0fpk8Z6Wwww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jrJ3goHKQjQJMM9rTmsrHqIhJsP1-nRGilvKQ3eJf38blgZjTj6lFYZ8vrvco_MmyAF1j6MQH1-BKlx21g-1_y9vI-TCw0_ja2UUZ6cwUIIEdJL6ZBNCRQ6_pmQqV6JzSS45vmo8gtYpJwApi9Kq2pCjqL1zZMbLEtZCWs0dK_o2J7DilIVQlYzNNH8OSnThwQhMC1FQOHyC_3z3lq6DbbUCSqB_SY8b5TKx6V74hldBRL4Fj3q0xahNFeBIdUTWTK7KqmWi9GdaSKueYXsbgvSfU76cL7Tc-WTxIggNEf6Zofgy-hl99D4oQGPWeEUjLfjKb57QFdUlexTVJkasVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AftwQPD19Fd2T4bXxwce0nzPTy6uMpQ8Pc1q6WcZ_AsUhrcJJvv-53CKXz-Cq_s5AdOyeWSJIntHLo8EYRw9Mr1DQwjzyDR8QZxeaqYcG4fVffXcmJ1QYUBpcvhl4goEXAt2M3qeSQngb8kc7XvXugaj68ySOoVaKULDe2B3V2B_fYAkTJhJQvwodf5ejIMUL2ijbfXeRZ8Y4UPtAcGiSnz9o-btwHF5BU2byHg7cjFTvf7ntClxvgx0KrLvDkNfgda3kzvO4SBL_PXWZUNKZFo-3J7AzNBwyidz0ybBlqul_DH9-y3yyT-7SWC-0PhsadKesNOamtoWcr9j2nxBQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lzNCZfro1lRRi1cY1nVsBFpaweNS_KNvBUFudYj-UJHzjY9qIuJXEZBGR0j3K9KYArCSBgTN7BnuOCPcRP1hnqkSaySrFSWDnBMQatYuBGJZ7_VZu7a5zLf4mhhpvIKdH_kmOclntv0I9G4pH-wNsR7JQ86eAuU-dQtR3aVsRnNgNjv0dw3vYBkOG1NDsAWfBU0Va4uKs9drNrnr3BMOIb7frXmXC18ehjB82saxvmXB2Sej1DRsNc2cB2gxQ-32qDYUPrH9MzN1hPHjTLrdquDOo1IGWPlSA2CEhqKkTJEMJcfj4S6qx0caZTaFAVmt7AwhDJRCYAXw7-KZ92F0tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mvKwqWStnRWNLdlonzEoBKO_coirkVk4-_Im8vi7DLYNhRAy5io8psShqzDWPOsYx7OqKEODBVeUWKezNEIPFJa_aiRw9gl-vdUvGJZLIqbDm4GQI-ZCzAewwrBcYiFX5c5yGlDiWOIvaZYl9SUT8noRBv7mxeQ3aYtZ-VlIAiyXO9o4kDeb1cwzxvxi_iikrbtAv1Xfmr8z8DzY8TFUATXvi5xX6FsYYgFimN50w_tJqHmBiACev4W6lJJQr3hbtt3xA6JcGR__6bP-jPMcxGcpiyzfzqE3XVeKWT5T7rcMTFJSVHbeDysmQlTMHbZ2B2a4XHgot8NsbvBl6JsqoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سی‌بی‌اس‌نیوز گزارش داد تصاویر جدیدی که به‌طور اختصاصی به دست آورده، برای نخستین بار گستردگی خسارت حملات موشکی و پهپادی جمهوری اسلامی به چند موضع نظامی آمریکا در خاورمیانه را نشان می‌دهد.
این تصاویر را نظامیان آمریکایی در اختیار سی‌بی‌اس‌نیوز قرار داده‌اند. یکی از آنها گفت خسارت گسترده به پایگاه‌های آمریکا به اطلاع مردم این کشور نرسیده است.
در تصویری از پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای چهارموتوره بویینگ ای-۳ سنتری دیده می‌شود که موشک به بخش عقبی آن اصابت کرده و دم هواپیما از بدنه سوخته جدا شده است.
تصاویر دیگری از این پایگاه، ساختمان‌ها و آسایشگاه‌هایی را نشان می‌دهند که بخش‌های داخلی آنها تخریب شده است.
سی‌بی‌اس‌نیوز همچنین از ثبت خسارت‌های مشابه در کمپ بوهرینگ در کویت خبر داد؛ پایگاهی که محل استقرار و آماده‌سازی نیروهای زمینی، خودروهای زرهی و شماری از هواپیماهای ارتش آمریکاست.
پنتاگون به درخواست سی‌بی‌اس‌نیوز برای اظهارنظر درباره این گزارش پاسخ نداد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/VahidOnline/78399" target="_blank">📅 04:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78398">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQbFaT1KiEDDcwyTsoFUKOhOAZuOCUW5pVsYfMHOkoeZucvqSFCShhGcvObO4hmv_fVTWcQyuiaFR1HvfQ13PV4VhzED2lZypDWWK0q0TsZHzBmOcmnZiHRBr0dqWQWQfMz80XzIl5xbpslXiMIE_oRUQe-M3lBSVNNQNRAv1hIPSnc_wGgsk9Ko0J_TWpJzx-B38LVRVkcMIeTyAHVajoqjj_-AASBr_HfgdvTNPT6FzrFsZP1bEfTmmUFgfxOX_OndpXOU6mrBvPQe1bw-PjIJ0L7k2ynaTjCnshf-ncaqKDgqK1w2VtSGzHcDaDfkJawboay2Fcqr3nUwAPxwbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی در یمن اعلام کرد پدافند هوایی این ائتلاف یک فروند پهپاد پرتاب‌شده از سوی حوثی‌ها را که قصد ورود به حریم هوایی مکه را داشت، رهگیری و منهدم کرده است.
به گزارش خبرگزاری رویترز، ترکی المالکی، سخنگوی ائتلاف، در بیانیه‌ای گفت این دومین تلاش حوثی‌ها برای هدف قرار دادن مکه بوده است.
به گفته ائتلاف، پیش از این نیز حدود ۹ سال قبل یک فروند موشک بالستیک به سوی مکه شلیک شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/VahidOnline/78398" target="_blank">📅 03:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78397">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XlpHilwTlaMRHnnDTZfK-qdk0MSGiZqIy63sT7JE0dvBG94bNp7xXCEEA6p_Y2vwG-RbJUZR7huXnXkRKdOnMF8mxhOTZw_li2BAcYeymmDc5k5bAag9Cgvx8MbazvZ3qynD2wJ69qktrFrI0Qay6dSIeQJjab705nAQCYeJNjJ82GEj-YTgD_CbXe3fECqsNj6T2QjGQXhRoi7MxAAydmgG7cRRiik0sASW87a60f_LjtLk5Q6C6ukp3FP4drVfZVHFw36wZDISQmW5DfSHSwblLiAKm3QsJpJRwm8T5Da_VgIOVHAHVUGH6FYXOyc-B4v6AWtRH8JfGLTe0ZXleA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو مقام اسرائیلی گزارش داد فرماندهان ارشد نظامی آمریکا، اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر هفته گذشته در نشستی محرمانه در آلمان درباره جنگ با جمهوری اسلامی و تنش‌های منطقه گفت‌وگو کردند.
اکسیوس گزارش داد نشست محرمانه فرماندهان نظامی در آلمان به ابتکار برد کوپر، فرمانده سنتکام، برگزار شد.
به گزارش اکسیوس، برد کوپر در نشست محرمانه آلمان، فرماندهان نظامی اسرائیل و کشورهای عربی را در جریان برنامه آمریکا برای افزایش تردد کشتی‌ها در تنگه هرمز قرار داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/78397" target="_blank">📅 21:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78396">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=Noa8_KeDIHRwu0rSFaiMsN2vUmOQRppWjDgaqusH2LR4ohdxKFBLedofRewh1j8TNwBKFAmy41Y5QLtfn4SvrlN77IheVBfB9F6MRpYR7cCD30sJ72N6TvwgEDHGWGOBrPFyRj7b3CjamY9WHvUz9Jn-14WKdGmNARMWTiIVnm-aZc-gEoetNbXvkZT62QVMv-xtAn1n5-u1R6owHAJcMjQC6_qDV1sUkvrcufGmBuBWdGPy7cCgdwDr3rRrnGZaTMi-h5V5jFDFSu_auibd4tWk9WNgprR5oe7y7Am3HxT3ugD7tC7aUqYica1XYOxXMMHXh_U5XN9M_kRKDBFjow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=Noa8_KeDIHRwu0rSFaiMsN2vUmOQRppWjDgaqusH2LR4ohdxKFBLedofRewh1j8TNwBKFAmy41Y5QLtfn4SvrlN77IheVBfB9F6MRpYR7cCD30sJ72N6TvwgEDHGWGOBrPFyRj7b3CjamY9WHvUz9Jn-14WKdGmNARMWTiIVnm-aZc-gEoetNbXvkZT62QVMv-xtAn1n5-u1R6owHAJcMjQC6_qDV1sUkvrcufGmBuBWdGPy7cCgdwDr3rRrnGZaTMi-h5V5jFDFSu_auibd4tWk9WNgprR5oe7y7Am3HxT3ugD7tC7aUqYica1XYOxXMMHXh_U5XN9M_kRKDBFjow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده در جلسه سالانه درباره وضعیت اقتصادی آمریکا و سیستم مالی بین‌المللی با دفاع از سیاست‌های دولت دونالد ترامپ در قبال ایران، گفت رئیس‌جمهوری آمریکا اقدامی را انجام داده که به گفته او، رؤسای‌جمهور پیشین آمریکا سال‌ها از انجام آن خودداری کرده بودند.
اسکات بسنت با اشاره به جمهوری اسلامی گفت: رژیمی که خود را وقف شعار "مرگ بر آمریکا" کرده و به‌دنبال دستیابی به سلاح هسته‌ای برای تحقق همین هدف است، اکنون با سیاستی متفاوت از سوی آمریکا روبه‌رو شده است.
او افزود: تحت رهبری رئیس‌جمهور ترامپ، آمریکا دیگر صرفا در حال مدیریت تهدید ایران نیست؛ ما در حال پایان دادن به آن هستیم.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/78396" target="_blank">📅 21:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78395">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KRdy1fb9f88VW743tXkhcVayhz-wWTwTH3fOa2GBWu6r87GKaT0vRGuG7n_nz17zbhoC8tX-VWeSeLyDJnqRwHj40tU1f6gnlEC--DbsSrFF3yB3WT8wDNDiuCwvORF6l3jYRkNvRU7vewEykPaupqNwqa08vdB8TiFnQGbgHhIgQUkF8pBs0t_ifeOz922XUTOBDlNBvt2WVzGtq15g9YoA-h0_wSbLAw7p33fj_yicR5WyDSUD9ytkhZ0M38_tOEGdEldi4ThY7L8aOk_r5EUH7yg9Wr17MiP37XMRJYHg-DaTxwP1CYXA5PC1BR632dHU4Mh6eQsSUpTWmm7xEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره خبری که تسنیم با شرح
حمله به قایق‌های صیادی
منتشر کرده بود:
وبسایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش ایالات متحده روز دوشنبه ۲۳ شهریور ۱۴۰۵، دو قایق کوچک ایرانی را پس از تلاش نیروهای سپاه پاسداران برای تصرف یک پهپاد نیروی دریایی آمریکا در تنگه هرمز منهدم کرده است.
به گزارش اکسیوس، نیروهای سپاه با استفاده از این قایق‌ها تلاش کردند یک شناور بدون‌سرنشین آمریکایی را که برای گشت‌زنی در تنگه هرمز مورد استفاده قرار می‌گیرد، تصرف کنند.
پس از شناسایی این تلاش، یک پهپاد آمریکایی دو موشک به سمت قایق‌ها شلیک کرد که به انهدام آنها و کشته‌شدن بیشتر سرنشینان منجر شد.
تیم هاوکینز، سخنگوی سنتکام، تلاش نیروهای ایرانی برای تصرف شناور آمریکایی را تایید کرد و گفت این قایق‌ها «تلاش کردند یک شناور سطحی بدون‌سرنشین آمریکا را تصرف کنند، اما پس از واکنش قاطع نیروهای سنتکام موفق نشدند». او تأکید کرد این شناور همچنان تحت کنترل عملیاتی ارتش آمریکا قرار دارد.
این در حالی است که رسانه‌های ایران حمله به دو قایق را به شکل حمله پهپادی به «قایق‌های صیادی» گزارش کرده‌اند.
به نوشته اکسیوس، این دو قایق در نزدیکی بندر کرگان و جزیره لارک در استان هرمزگان هدف قرار گرفتند و احمد نفیسی، معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان، حمله را به ارتش آمریکا نسبت داده و از مفقود شدن شماری از صیادان و آغاز عملیات جست‌وجو و نجات خبر داده است.
این حادثه در شرایطی رخ داده که ارتش آمریکا تلاش می‌کند با افزایش تردد کشتی‌های تجاری در تنگه هرمز، عبور و مرور دریایی در این مسیر را به وضعیت عادی نزدیک کند.
یک مقام آمریکایی به اکسیوس گفت ارتش آمریکا و کشورهای عربی خلیج فارس در ماه‌های اخیر تردد نفتکش‌ها از تنگه را در طول روز نیز آغاز کرده‌اند، در حالی که پیش‌تر این عبورها عمدتا شبانه انجام می‌شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/78395" target="_blank">📅 19:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78394">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=UaqJvXK21SqG9nCQtxNk8NNGExbhWT3n21UeUHVgJSGrQiE7aIEQF8UPts3Jo8UXh8MXUSnJ_7wSG57eO_C2F34zTzqX_CXXtIP1OstcsDg9JqDXnvXeN-BX7QC_dw_izlkrK9gS-yDFu7F1BvqlcUNoZxEpvJik7NtiHPq4IOsqRHlzzDYDx9m9dE8isE72KKe0NXAzDHzyvfdr0MZ-vw-TPqDj0JKWnjgIlQ1QH7yUezRNxkAqgzO-dHOLH5rbEwKkELN0IHNNiLeeNM03V0zy8u3QYC2UeHxRuNocP1cgjoEJgeBpP5DZFzvFzfvMjA6Nh2mN3B4xDkX2MxSqtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=UaqJvXK21SqG9nCQtxNk8NNGExbhWT3n21UeUHVgJSGrQiE7aIEQF8UPts3Jo8UXh8MXUSnJ_7wSG57eO_C2F34zTzqX_CXXtIP1OstcsDg9JqDXnvXeN-BX7QC_dw_izlkrK9gS-yDFu7F1BvqlcUNoZxEpvJik7NtiHPq4IOsqRHlzzDYDx9m9dE8isE72KKe0NXAzDHzyvfdr0MZ-vw-TPqDj0JKWnjgIlQ1QH7yUezRNxkAqgzO-dHOLH5rbEwKkELN0IHNNiLeeNM03V0zy8u3QYC2UeHxRuNocP1cgjoEJgeBpP5DZFzvFzfvMjA6Nh2mN3B4xDkX2MxSqtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیوی منتشرشده در خبرگزاری رکنا، لحظات پراضطراب داخل هواپیمای بوئینگ ۷۳۷ شرکت سپهران را نشان می‌دهد که دوشنبه ۲۳ شهریور پس از برخاستن از فرودگاه مشهد به مقصد کرمانشاه، با ترکیدگی لاستیک مواجه شد و با گزارش آسیب به موتور، مجبور شد به فرودگاه مشهد بازگردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/78394" target="_blank">📅 17:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78393">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dzDsk9RAnAFE-hmU9NsDTW3gAPLyUhgsMSR1ivOJawn9kHYF9pH3zjiMP-CApUHrVfR3xwhXtZpl5eYd-VT0dosZ4QOKxXbTH8mccNprn-v0530y2AkPAcaq-EHlNG4aMvG8CatkpgYu4ng6H_qSrU5l627VbU5s4ahN3Oj2DxIsB7_Bj5QlttXnw62Xsl0gFG0WnfCiNjmbJ8uuAT73A91aXg0avDmBednaE-6PJOuoEM_FjHNSEmq-65jxAx1YWZzdZIa3bhCFVbUU7MzivjYYJ7nIa_vhR7SnU7nnzjNA_VsOY-nCh-4fCfuIPFelkc1rmi7lAg0rXnygCwjU-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر رئیسیان، وکیل دادگستری روز سه‌شنبه ۲۴ شهریورماه با انتشار پیامی در اکس، از تشکیل پرونده کیفری برای رضا درمیشیان، کارگردان سینما و تئاتر ایران خبر داد.
به گفته رئیسیان، سپاه با شکایت از رضا درمیشیان  به اتهام تبلیغ علیه نظام پرونده قضایی تشکیل داده رسیدگی به شکایت از او در شعبه هفتم دادگاه انقلاب تهران در جریان  است.»
رئیسیان با اعلام این خبر گفت در دادسرا برای رضا درمیشیان قرار جلب صادر شده و سپاه پاسداران به عنوان شاکی، تقاضای توقیف اموال او را کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/78393" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78392">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2dJGGvHtX8ei49q8lefbiVF26mjRSnyWvqC6J-k5kCLV2q2XQ5qTwhtCHQ62jPONZcsKRgYOcTFHhQNWgFHPjxwZCc7wz7bqoKJl0q0PsoGj3vRoJgxIeq7SraPMH8Qpv1_zKr10g8iuSBVVxU6errRE0C9kgypJtJNJsBnVL9tF_8z5-mQioKKw9Qr6KeZCPasIN90hlW7x_ElQ2m9MplmcxU0MQj9rHrfV6PzuneV3W6Va_9hVTyPe1djv10nrVUc3cM5BHLzzwmjJx6xR6ZPrmjf9J_CCq6PszPLCo9vQcE9EyhbOB2E8Xvrn6h9PSLnjZSeFnK7Khha3WozHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استودیوی «کارگاه» با انتشار عکسی از آزادی «آریا کسایی»، طراح گرافیک و یکی از بنیان‌گذاران این استودیو، پس از نزدیک به دوماه بازداشت خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/78392" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78391">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kafXox9X7HFT2II_4RzwljqdfDy5mt2Phu2GrUChiXOkDrNVj4mWp8eyiEjoKqohlMFjDWOmG3drPPi7nRzcyB4bvd_yfCJHp3kqibW7sDm5WP6839BVxXVRcKEdimHBxNkyjhEWOOUhjuKP6yDYJ2_CS5RzFrAlw65wnOpxhEMTTGKj6dmhyxIe_bu0ETT4lxuxEOCoVskaTyJtY1W-HS5Y9Jjcx1cI6oeNBEdWwjXLiQqKkpnePK_hpPTYLwDCG5T5AOrp-mAzQThzlAVvbeO5gQ50xg4a1xRQeSJCFtcikxWgBQhVj4vH8Ls4LvGfKluxElY1ljIYfPeqHu9gUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس تهران می‌گوید فردی را بازداشت کرده است که شامگاه دوشنبه ۲۳ شهریور به سمت «جمعیت حاضر» در میدان پونک تهران سه کوکتل مولوتوف پرتاب کرده بود.
میدان پونک از جمله میدان‌های تهران است که از زمان آغاز جنگ ۴۰ روزه تجمعات شبانهٔ حکومتی در آن برگزار می‌شود.
بر اساس بیانیه‌ای که فرماندهی نیروی انتظامی تهران منتشر کرده، «این فرد حوالی ساعت ۲۱:۳۰ از بالای ساختمانی به سمت جمعیت سه کوکتل مولوتوف پرتاب کرده و پس از آن گریخته است».
در این بیانیه ادعا شده که این فرد «قصد خروج غیرقانونی از مرزهای غربی کشور داشته اما ماموران با شلیک گلوله از ناحیه پای راست او را دستگیر و به بیمارستان منتقل کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/78391" target="_blank">📅 15:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78390">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LaZfK8uGwtS_TRO_KQYc3oAdv0SAyhc3eym37IR_uoXcD53hEE5QcCGE31D2XiNLcFPaGXG1XTfz_aIvs5UBkVT_LOnXFoTmYM4R7c4tX0JmzfVyPWt5a4uvH0pK9SOaWUTIQzPdyZB3nUC2dhsDyF9DXtR6mgkg_VCB4yIbZsq33B3SG3QVmxXWvCM0d-rAFQl_IGgkAExlWdnRz4RQH7ek0nBsEKgGAgvn5iUMJHmrw0Y9yxVcQ1-vb3F9-Y8nOXceMbMghlbl494FYJHUelcjIgFTBoUk8mS6vWw5Vb8bKRY6EGZG2-3V6tTw6BOXCmD5bSF03RbF9bArxRsOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش رسمی آمریکا از هزینه‌ها و خسارت‌های جنگ با ایران منتشر شد
یک گزارش رسمی نهادهای نظارتی دولت آمریکا می‌گوید جنگ با ایران به «کمبودهای راهبردی» در ذخایر برخی تسلیحات پیشرفتهٔ ایالات متحده منجر شده است.
نخستین گزارش رسمی نهادهای بازرسی دولت آمریکا دربارهٔ عملیات «خشم حماسی» که روز دوشنبه ۲۳ شهریور به‌طور عمومی منتشر شد، می‌گوید مصرف گستردهٔ تسلیحات در جنگ با ایران «به کمبودهای راهبردی در موجودی‌ها منجر شده و گلوگاه‌های پایهٔ صنعتی برای تأمین مجدد مهمات را آشکار کرده است».
بر اساس این ارزیابی، پنتاگون برای مقابله با این مشکل در تلاش است روند خرید تسلیحات و زمان تولید را کاهش دهد و ذخایر مواد و قطعات حیاتی و برخی مهمات را افزایش دهد تا در شرایط اضطراری امکان افزایش سریع تولید وجود داشته باشد.
این گزارش همچنین نشان می‌دهد آمریکا تا ۲۹ ژوئن (۸ تیر) حدود ۳۳ میلیارد و ۴۰۰ میلیون دلار برای جنگ هزینه کرده است. نزدیک به دو سوم این مبلغ مربوط به مهمات مصرف‌شده بوده و ۳ میلیارد و ۷۰۰ میلیون دلار به تجهیزات از دست‌رفته اختصاص داشته است. بر اساس این گزارش، ۷ میلیارد و ۴۰۰ میلیون دلار دیگر نیز در ردیف سایر هزینه‌ها قرار گرفته است.
پیت هگست، وزیر دفاع آمریکا، اواخر ژوئیه (اوایل مرداد) هزینهٔ جنگ تا آن زمان را ۳۷ میلیارد و ۵۰۰ میلیون دلار اعلام کرده بود. شبکهٔ ان‌بی‌سی نیوز نیز پیشتر به نقل از مقام‌ها و افراد مطلع از برآوردهای داخلی گزارش داده بود که با احتساب هزینه‌های گسترده‌تر، رقم واقعی جنگ می‌تواند به ۸۰ تا ۱۰۰ میلیارد دلار رسیده باشد.
دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه و همزمان با انتشار گزارش ارزیابی «عملیات خشم حماسی»، در شبکهٔ اجتماعی تروث سوشال نوشت آمریکا اکنون بیش از هر زمان دیگری در تاریخ خود تسلیحات پیشرفته تولید می‌کند و این تجهیزات به‌طور روزانه در اختیار نیروهای آمریکایی در خاورمیانه و دیگر مناطق قرار می‌گیرند
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/78390" target="_blank">📅 15:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78389">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZbbsjez-8K17dX2i9mzh1xJUA-kfoBt4IRJqRZ2BAsiHZffe1aRV9u1zf1UL9EuZWZS-FK_XKv_GP4NiXmECmc_aQv_apDYhrKjgijF36m9KvNXrc2LH24xu3bhA0WgWf1GqbOtpxIGWmfHpWOa9ohOSZ_xD9zrERGaCGw47XTn4i6B-OdfkMjPAqm58E61JsT7LJ5_umZTLq4eEhhrifTz6uWZbhdlZK95xmpbmXNzmvoACrc7PbO96cF7LmdnLBa9ExN2947jWVPfh_NC9hPFHFeQqj_3iFxkwl6w0raSH9ZxFeM-qnXlaZmtKU9xYABXzr_4FiFqp62u1B4fSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پروژه امنیتی با نام «علاج» با انتشار اطلاعات شخصی شماری از ایرانیان خارج از کشور، از شهروندان خواسته است افراد بیشتری را شناسایی و به این سامانه گزارش کنند. صداوسیمای جمهوری اسلامی نیز به تبلیغ این پروژه پرداخته؛ پروژه‌ای که مشخص نیست چه نهاد امنیتی یا حکومتی آن را اداره می‌کند و اطلاعات هویتی منتشرشده در آن از چه طریقی به دست آمده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 202K · <a href="https://t.me/VahidOnline/78389" target="_blank">📅 15:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78383">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HTd0apYZ_2J-TWkJNw9lODEZlRUjuP0Ni4lyFHUTnKtyt7oPgUpXBscMhCUtQ9OF_E46xt2daeeIbtNkEqTgjBbkqhPzoEl_hplOHfLs2NLEuj1XnULJPkdrn0Hr9MFp3LVoAJM4geGcMXegmQuziqHRmvmuarXfKWkGNalaQess4b_DGqebYTFV-Kfud9DTD6LsCd0bhjH10R6BGdvQvc7hSvXJNvVmBvvyum1MmJQdfM1sxJo4p_d8JTfW9f8IcHijB4I64LVWmheUqP3zgDNLf0yVCLrdwa80fIxv5t0mrNAcUxMVoodxGLhiIZOYiE0CiK6cO0UJytz7pPohIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/clVUWyeTEXFwqPzIkyOpdzXxUZ_H6WqsPH3X-aa77r6ktd2AZcfFHBsukssto7UUewydBvHQiFY5yoVvd4vpdzR9xUsny2yWZxMB42iVL2tXmG6LBANLfwgHJw_rVjtPebWRSX8u0zYxY-m40W7qnVe5qfwHv0vHZxMiD9XEHkeAxuYMq5urtXOHcfwvgeXRuDxgTPKI_h84sA91Ui4DHiDtqe-WoFAR6mbKFNUUERjf9PIP8J5bUtUN9IftyFqt4_lqEOf6xuI46fZjV-csVl69Ed4lxiNhRUcMuY3XbLklVQnAp5CO-KlYPTbpvp0Hom9MRukZ7GMehEMJBMno5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bxygsAzD--AKpAzh0Qz4ZQx3lKIOXtTEp6NNfKpip1qrDNM9NSgZjxnYe_COf_MLt4ieRy310jm8MVDgBC8xHFB-0X73MJInjJt0jz9R3xozi_L2ySPQmwtcNz7j7arMaADhS1NhkatqSkyGZpQPqYw3OdWgu2badhQ3VmnSGY-hZ0HVzGmP7UZjile0j2zJv0act-iqGzsGc843fqdCsNPJx96DHDX5I2cSAJj3lc0fgt3clNVowcqTYZ3X-sBMDkYWe6-Paj06dSgwQpSVrUB2dC8Anz1gxMT1jkXiJ1GpUYUYtyv6AcMCUPykP7MX8JwurJOg0BcS-hKtIOgYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IepsRah6quMbcgPWjke1-24UM9oSUJ-G-UZt8aRGC_BJ29sEpBxPgYk1WgXkH-HKoAllsod00Yn4WHLF9XEm9HpwJZlUDIriyDkZYiXRfEHu_mGQV89H7suXdsrtttYhb9BGxlnojUZR-XDrHtW-KQ6XEsLKdawARTVGsSbw7ycm1N7BfCLCAT5xO9CbI1fATEDPrjJFOovlm-ViRYizSzTzzBUzDKr_wcTSNeKuIr1N9x7gFluh9_1ArZvFqzfZUgoyhgaQKf3lJ1bdUyXw1u7mP-1nVXKW9VxujFiCfObT1Eqcb57sKUfzBEP8s-LFHQmYsI4dYGCgw5F5UoNdYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R5janpliyyu6yjv-6JVPi8PWoNT2bE4JyPU7NGSeU1bMjK7EpT0xkTo5IRAF4t4fMyslI2P4fVFTz_RYrcaW1ZW3ogVRd1052I9kKBodl7_2xf1mfRvdeNO1K8T_UI3oe81Ls_Ql2G265wP2IoUexRN1MQCQLX1CbrZg1-xS04OXakeBVYaKAMG_HkbucdKkLMqCMD-K-SCj9f38DcA1v8bdCAgsTOCZbuhOwKO_iNnYAT-Gm5aMotvzZKn6ptF2NudzwTc2193ebdJb3XkRkRY6HIXXTdyq44ZahFdhkvb_aJWQouk9xko2RWk7BPJrcFXXO55E2wfo3JHo31DgPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FIsvMZgBFStwl062oLBg9Ej9maaXaXVYECQ7WfTQuMxTOiRgJAWYkeFRyAFPywznBZSHnbNF0LW9Ag5LXQun5yVPm3EMiKZkLF9_A5_ziGo745BiOlHK6mw8iEWqR3S1DkWOGYlLPzN_YFHVKCkboQdSq4UNxlxuU9dDAEwzmQ1WXU8hIOu5T7Nuf58NEdBA_QGEhOTmg65McuvCLJea_Fuxp9sGRIg-TfSa6vb_ied0p_f_-cQs2V57m4Tz9qI5a4wh5UEPSQSSyMN8f-A5u5eMCCsq34W8taCCiR4vG0n-9U7K37p8eRBPSv-2O5DhHvFCPs3tIMcKqKiKEB1Kng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«پویش جان‌فدا»، کارزاری وابسته به نهادهای تبلیغاتی سپاه پاسداران، ارسال پیامک برای ثبت‌نام شهروندان در دوره‌های «آموزش نظامی و امدادی» و سازماندهی آن‌ها در قالب «گردان‌های مردمی» را آغاز کرده است.
در پیامکی که برای شماری از شهروندان ارسال شده از مخاطبان خواسته شده از ساعت ۱۷ سه‌شنبه ۲۴شهریور برای شرکت در «دوره‌های آموزش نظامی و امدادی یگان‌های مردمی جان‌فدا» ثبت‌نام کنند.
پویش «جان‌فدا» از ۸فروردین۱۴۰۵ با محوریت «قرارگاه فرهنگی و اجتماعی قرب بقیه‌الله»، از نهادهای وابسته به سپاه پاسداران، راه‌اندازی شد. سامانه‌های اینترنتی، پیامکی، تلفنی و ثبت‌نام حضوری برای جذب افراد بالای ۱۲ سال در این پویش در نظر گرفته شده بود.
@
VahidHeadline
دیروز کلی پیام دریافت کرده بودم از شهروندانی که می‌گفتند در این پویش ثبت‌نام نکرده‌اند ولی اون پیامک براشون ارسال شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 197K · <a href="https://t.me/VahidOnline/78383" target="_blank">📅 15:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78382">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfGgCxBAL7CLRNpW7AFqDo3cCslksYpLpSpgxCf2GDY7RMgjf1C5OxoiqdRIqno7Ea3afDo--KNjcDvTtmp-mDnz-jAqEPij7X6CpzQEm9Sy7Dg8TjzXVKPlAg7Lad2Q44ZarvdMW0fSlFg7lplkHtYPb8TFfgI8kVwg3uJ21EQRsWXHyYBRRM0XQkZSntFFI5C1qeLh_3pJ3Rn_fPQEEb648X6hj5RuJu6vZjU6fITU2aeXhxLzIOWp7XFS00UozL5N1jQAhbfs91becPYiqSTjzWQ5fWP6yqX8B0bkHdYDm6ZzaKFxQ1Ki7y0k98cRjbIbrDYFVgbDQRqgubg1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دادگاه فدرال آمریکا روز دوشنبه، ۲۳ شهریورماه، به عدم اجرای دستور دولت دونالد ترامپ برای محدود کردن مدت اقامت دانشجویان و خبرنگاران خارجی در ایالات متحده حکم داد.
‌این دستور که به گفته قاضی دادگاه به دلیل «استدلال‌های بسیار ضعیف» دولت صادر شده، قرار بود روز سه‌شنبه به دست وزارت امنیت داخلی آمریکا اجرا شود.
‌بر اساس قانونی که دولت ترامپ سعی دارد به اجرا بگذارد، روادید دانشجویان خارجی و روادید افرادی که با برنامه‌های فرهنگی در آمریکا اقامت می‌گیرند، به چهار سال محدود می‌شود.
‌این قانون همچنین می‌گوید که روادید خبرنگاران نیز نباید از ۲۴۰ روز فراتر رود.
‌هر سه گروه، بر اساس قانونی که اکنون دادگاه جلو اجرای آن را گرفته، برای اقامت بیشتر باید بار دیگر اقدام کرده و روادید خود را تمدید کنند.
‌به گفته قاضی دادگاه فدرال، اجرای قانون جدید تعداد دانشجویان خارجی و روزنامه‌نگاران و خبرنگاران در ایالات متحده را به شکل قابل توجهی «محدود خواهد کرد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 192K · <a href="https://t.me/VahidOnline/78382" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78381">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLts2cf_CldyhiyTVfzRXqDcOtI6IlkrwlBmz7H7F76Yphkign9gy0zn3d4dfTAGhpV7WZL-9HFIGkGNFbgomzWYZP2reXdjlZc0VU5r_K9TR6Jld9U30_SrdZqI3VgMRId-gV3upoPcL-ATvP3Li7TJSPPwHn_9StoAf0Y4H_tOB7Y3NF3r8Hs6DY38RBitFee-IZPLYZXNh3NJIkKxbNN_X7Jz0emAmaLHVqPhVfenIVvHl_4n5zPVOwBJXiMmS35gVxFf_-YWz508okHAnPezmMV-1zKU3orwIaT0cGJFRyZR5K2QgmdDHdtWe61C8HeACv9KxNleWmeTa06RDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه اتریش اعلام کرد برای سفر محمد اسلامی، رئیس سازمان انرژی اتمی جمهوری اسلامی، درخواست معافیت از ممنوعیت سفر سازمان ملل داده بود، اما درخواست رد شد.
بنابر اعلام این وزارتخانه، رئیس شورای امنیت سازمان ملل به وین اطلاع داد که درخواست به دلیل نبود اجماع رد شده است.
وزارت امور خارجه اتریش افزود با توجه به تعهدات بین‌المللی این کشور، ورود اسلامی امکان‌پذیر نیست.
اسلامی در راه وین برای شرکت در کنفرانس عمومی سالانه آژانس بین‌المللی انرژی اتمی بود که اجازه حضور پیدا نکرد. او از سال ۲۰۲۱ در همه کنفرانس‌های عمومی آژانس شرکت کرده بود.
ممنوعیت سفر از سازوکار «اسنپ‌بک» ناشی می‌شود که تحریم‌های سازمان ملل علیه جمهوری اسلامی را بازگرداند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/VahidOnline/78381" target="_blank">📅 15:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78380">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZOa6vOCpK2LAXx-_lyS8rL_9Q98Yj3JwVfAvbZIcvl_2lfJfcL0oPRuRReJyrxbqscIgJeSJfTjbRktnnbmwMUrjkaC4AzLVENodvxbRz9s4bl_PInfzZA_4Dyo1tKM5LrK8dSIfbOStnsk53ylenQaB5CcdIk-WnUD0amB5OCUP5pavRlOjbLA-mlJpHHSluRML8WeNa8qB9JS__dqC5CX2FKVmDKIjqn60nDAeVOdFlQ7n9OURwNefYUXe41dcQ3ylYxEm1NLcWKGDwWYYGiBVIDYbAWGmcHUBA9f2IYZJMa_latUPL-PRwBF4Jdi7VzMVAeNZFj9Dswj8bsLZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش الغایا پس از حمله در سواحل عمان و آتش‌سوزی در موتورخانه، به یکی از بنادر این کشور یدک‌کشی می‌شود.
بر پایه گزارش رویترز به نقل از مقام‌های عمانی، ۲۳ خدمه از شناور تخلیه شده‌اند و دو نفر همچنان مفقودند.
روایت‌ها درباره علت حادثه متناقض است.
سپاه پاسداران اعلام کرد الغایا با پرچم پاناما هنگام عبور از «منطقه ممنوعه» جنوب تنگه هرمز با مین دریایی برخورد کرده است.
فرماندهی مرکزی آمریکا ادعا را نادرست خواند و گفت شناور «ماه گذشته با موشک ایرانی زده شد و از کار افتاد».
سازمان بین‌المللی دریانوردی گزارش داده بود الغایا روز شنبه آسیب دید، بدون آنکه علت را مشخص کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/VahidOnline/78380" target="_blank">📅 15:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78379">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bIP5yz1uI3vLeQ6xxhSUs_1lBTlBdvI3VaUd3mEnlu-nvvq83BH0DJO5Ekv6w0w9uazLEwbLU9IVd1EXtUttvvI6GMh4qaAC2U3EmZSWGWeYoSzFbk0mi1l3_gj4F6GfBp6F-FF-eseNod0K0NeJ7JPmrDKXoWd4USCOb2sy40yn2nbXtIWp-lBPcxWmaH0VRCPbL4_YPSSer-cJK88zGH1LoktMvTKsHQgLapgQ7s47BnOfHOtGoshCjm3pSN2GIHEd-cCJfDtz-q_JhWeD1tLoBX9r_bITmVmU-a54s0MRDo_l2zeVL_RHaMRsKkoLIkCo1ooNSYf_SY8m5M9lFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست‌کم ۱۰۰ معترض در ۱۳ استان ایران در خطر اعدام هستند
سازمان "حقوق بشر ایران" اعلام کرد دست‌کم ۱۰۰ نفر از بازداشت‌شدگان اعتراضات دی‌ماه در ۱۳ استان ایران با حکم اعدام روبه‌رو هستند؛ بیشترین شمار این افراد با ۴۶ نفر مربوط به استان اصفهان است.
بر اساس فهرست منتشرشده، پس از اصفهان، ۲۲ نفر در استان‌های تهران و البرز قرار دارند.
همچنین ۱۰ نفر در فارس، هفت نفر در خراسان رضوی، پنج نفر در مرکزی، سه نفر در یزد و دو نفر در سمنان در این فهرست ثبت شده‌اند. در استان‌های خراسان شمالی، گیلان، اردبیل، ایلام و قزوین نیز هر کدام یک نفر با حکم اعدام روبه‌رو است.
این سازمان می‌گوید فهرست منتشرشده تنها شامل معترضانی است که دست‌کم در مرحله بدوی حکم اعدام دریافت کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/78379" target="_blank">📅 15:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78378">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uLMnSaXXq1iuImpTpbKzeCKfD8o4jlLlUgiHqfXmKmt7ybpjBCaVrmi_-xa8qbaGsS8ILRV4p2Lh4lTm3umHRq3QAKKqa4Un724uegQ5DgGkoLMNlkmTBRf4SjFNk_sguXqtZIR-A_KyijRzmtjWLLcWC_cB6Dk4UNc6eWMZ6gVfiaRgwMn5kmb4UHWDiz-DQ4aiKWDVeUXC_sy0pwjtRZvY6lF0-9JLW23sEx9f9KxzTAUwZj8_J7Yaw5ZwM_FAB5FJrs_S2glDXz99vkFlCrUWmsm--U5Z21e5XQtEyKtsb1Ac0QyUIP1XXDIslj66xyFetA-FY22jPxiETSotwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، شامگاه دوشنبه ۲۳ شهریور ۱۴۰۵، از حمله پهپادی به دو «قایق صیادی» در حوالی بندر کرگان در آب‌های خلیج فارس خبر داد.
بر اساس این گزارش، در پی این حمله که تسنیم آن را به «آمریکا» نسبت داده، تعدادی از صیادان حاضر در این دو قایق مفقود شده‌اند.
عملیات جست‌وجو و امداد رسانی برای یافتن مفقود شدگان آغاز شده و نیروهای امدادی و دستگاه‌های مسوول در محدوده حادثه در حال جست‌وجو و نجات هستند.
تسنیم نوشته است جزییات بیشتر درباره این حادثه و وضعیت صیادان پس از دریافت گزارش‌های رسمی اعلام خواهد شد.
@
VahidHeadline
آپدیت:
اکسیوس: آمریکا دو قایق سپاه پاسداران را منهدم کرد
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78378" target="_blank">📅 03:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78377">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QqrwM7bsxnSYI5Q7VBFggMcBMNS-6_9O-YOc0UAY1mER9AWGevsMNyIuGj4pirtp8fOxwbHYguqzT-tsmzdo9SK1fNINFxPoBjs2t1F3g_8hSB_R7AArZYgodZjBLbabS1cnUGIn7nPL4njKUMLICUBKgAvVVd5fMuDXs2VdxqMr7ZrOGHTDX0MBcoIxADr0FpraX3Yq2AdHKxvT6jSWyaOrJtSqnH9KJR61q0JPKGyAUS50njafu3cHu9YjpPATy_QoHkKNw5AUb8g7SxSafpGedqb4x2KQiDJth_olviS924nn0AIL6t0tst6jNfPWc6tSA9RJc9VK3bzEyIYgAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی نیروی دریایی سپاه می‌گوید یک ابرنفتکش که به گفتهٔ آن قصد عبور از «منطقهٔ ممنوعه در جنوب تنگهٔ هرمز» را داشت، «بر اثر برخورد با مین دریایی منفجر شد».
خبرگزاری‌های ایران شامگاه دوشنبه ۲۳ شهریور با انتشار بیانیه سپاه، نام این ابرنفتکش را «اِل گایا» به شماره دریانوردی «۹۳۲۵۳۳۶» اعلام کرده و افزودند که «تلاش برای مهار آتش بی‌نتیجه بوده و کل نفتکش در شعله‌های آتش گرفتار شده است».
فرماندهی مرکزی آمریکا (سنتکام) این ادعا را «نادرست» خوانده و گفته که نفتکش «اِل‌ گایا» که با پرچم پاناما حرکت می‌کرد، ماه گذشته هدف موشک ایران قرار گرفت و از کار افتاد.
@
VahidHeadline
پست سنتکام، ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است یک نفتکش با پرچم پاناما اخیراً در تنگه هرمز با یک مین دریایی برخورد کرده است. این ادعا کذب است.
✅
واقعیت: نفتکش «El Gaia» با پرچم پاناما ماه گذشته هدف یک موشک ایرانی قرار گرفت و از کار افتاد. آخر هفته گذشته، ایران بار دیگر این نفتکش را در حالی که در آب‌های ساحلی عمان قرار داشت، با یک پهپاد هدف قرار داد. این نفتکش در حال حاضر توسط یکی از شرکای منطقه‌ای یدک‌کش می‌شود.
ادعای کذب سپاه پاسداران نمونه دیگری از دروغ‌ها و تلاش‌های آن برای ارعاب است؛ آن هم در حالی که می‌کوشد مانع تردد کشتی‌های تجاری در تنگه شود
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78377" target="_blank">📅 23:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gK2C6QEEGIn7PS_kFWGTnIX5aNO9mr6D11Tr-9o2MtzjgymyHEeR0r8AFbcqIWhg5g-WstagJ-4ZyQgL0giikjFq8vCS_8S2TKl4tWZm0mG2f8nt5vysvxJZ0LDWQjewBAeQ1cKwAcQ2bSadwKDJwQKaInNL8vgFBRSi9dnnE8w2SeV9vGwUsPBB7Um9koaqecgYFScy7s4Ywaf0VHj5GHNhviNIPNeobfy6eWJsZFXn-EuYAY9CLHiZMf58ipJoBlfgUNTCOkHVbn8Yd_T_a6lqfNhVyY30U-yzcP0TjLacb52ePR5FwO7EdBqDqHiZyqge52_iWL3v-VSCwI8nOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RvyAfgPuyD3Oz08oG3x0Ibt1FIXomf11GT9rbZT19JiSDjLBfTMewTr0brCk4JbtFCzMB-tBRJr7ml-G36ea75Ikk3DaKxm8H43m9masHXB1auSLCtpjcvRNs4FUCvJ2lDXe7-ypM33pxe5CKt8G90hfIjwMkxD1Kio9YSSRYEGOOiQZ2viBR8jzFBulciV5ahFpY50uEuTcAJq7GSt97cFo2YJ1U4YszwebKP3-ZkYCYn8uTeUZyfdCBGWtgMIATQ7MAcrQ3AcHRt_pKrHWMt9F3n_SAZTB1fHlsKZZ1cgDP4HuXYb7Apl8zALpCDo84qPJXrrr1NS9IEU-nYLO4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پیامی در شبکه اجتماعی تروث سوشال تاکید کرد که افزایش قیمت‌ها در سراسر آمریکا ناشی از سیاست‌های جو بایدن و دولت او بوده است.
او نوشت که حتی بهای نفت نیز در دوران بایدن بالاتر از سطح کنونی بوده و دولت او مانع از دستیابی جمهوری اسلامی ایران به سلاح هسته‌ای نیز شده است.
ترامپ با اشاره به اینکه قیمت سایر کالاها به شدت در حال کاهش است، افزود که بهای نفت نیز به محض پایان یافتن درگیری نظامی با ایران—که به گفته وی زمان زیادی تا آن باقی نمانده است—مانند یک سنگ سقوط خواهد کرد.
در دوران ریاست‌جمهوری بایدن، به‌دنبال وقوع جنگ روسیه و اوکراین و بحران‌های بازار انرژی، قیمت نفت در بهار ۲۰۲۲ به بالاترین سطح خود رسید؛ به طوری که قیمت نفت برنت تا حدود ۱۲۷ دلار برای هر بشکه افزایش یافت.
@
VahidOOnLine
رئیس‌جمهور آمریکا در شبکه اجتماعی تروث سوشال از کشورهای جهان خواست پس از پایان درگیری‌ها، هزینه‌های ایالات متحده را برای حمایت از کشتی‌ها و کمک به عبور محموله‌های نفتی از تنگه هرمز بازگردانند.
ترامپ با اشاره به اینکه نفت در حال عبور از این آبراه است، تاکید کرد کشورهایی که هیچ کمکی به آمریکا نکرده‌اند، باید خسارات و هزینه‌های این اقدامات را جبران کنند؛ زیرا واشنگتن این ماموریت را بیشتر به نفع دیگران انجام می‌دهد تا خودش.
پیش‌تر کریس رایت، وزیر انرژی آمریکا، اعلام کرده بود میانگین تعداد محموله‌های نفتی که با حمایت نیروی دریایی این کشور از تنگه هرمز عبور می‌کنند، رو به افزایش است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78375" target="_blank">📅 23:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78374">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZEkXDc8bVORcyUFJglT7CNgqDjS9j8KIxLGql9sU38Gyc9oJRoxEuW3R30N8pe4dobOYd2emd5yB1BuefR_PvQHfXBQHhys2rXhRUGI_BSsudrtJ04mONRa-F_WmU7fIq1f9FLw1oBbfzt9QLxMm6xWMA0DJBArrLhj_9PMc7YdVAgEx_2ocbJUlErBa0VbCwWx1oTK4T4oQWcgIBSUctkbtjuvBlVTsnNfIw0dy-QfOY4bVF0EZh1GK8Qjxwg10HvAsUvR9S6YiLo35xXUrsLdsP5S7KwB0oBuyFuyanRvU_1PynWtmsrzQUIP0KIhGyypX0x801ywPSF9AZOzQyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایرانِ شکست‌خورده می‌خواهد خیلی سریع و به‌شدت به توافق برسد.
من تصمیم خواهم گرفت که آیا ایالات متحده آمریکا وارد مذاکره بشود یا نه — ایده‌ای که نسبت به آن آمادگی داریم. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
ترامپ نوشت: کشور در حال ورشکسته‌شدن ایران می‌خواهد سریع و به‌شدت به توافق برسد. من تعیین خواهم کرد که آیا ایالات متحده آمریکا وارد این داستان خواهد شد یا نه؛ چیزی که ما نسبت به آن نگاه باز داریم.
پس از انتشار این پست قیمت نفت اندکی کاهش یافت.
اظهارنظر اخیر رئیس‌جمهور ایالات متحده در حالی است که ایران گفته برنامه‌ای برای مذاکره با آمریکا ندارد و شروط متعددی را برای توافق با واشینگتن اعلام کرده است.
در همین حال، اسکات بسنت، وزیر خزانه‌داری آمریکا در راستای برنامه فشار اقتصادی بر ایران موسوم به «عملیات طرد اقتصادی» از همه افشاگران خواست تا چنانچه اطلاعاتی درباره «تسهیل‌گران تروریسم ایران» دارند در اختیار وزارتخانه تحت امرش قرار دهند.
او با انتشار پیامی در شبکهٔ اجتماعی ایکس خطاب به کسانی که در سراسر دنیا اطلاعاتی درباره شریان‌های حیاتی اقتصاد ایران دارند، نوشت: «این شانس شماست. اگر اطلاعات قابل پیگیری برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت جایزه باشید، صرف‌نظر از این‌که کجا زندگی می‌کنید یا چه کسی فیش حقوقی شما را امضا می‌کند. اگر چیزی دیدید، بگویید».
او همچنین بار دیگر تاکید کرد که وزارت خزانه‌داری آمریکا عملیات طرد اقتصادی را «برای قطع تمام شریان‌های مالی رژیم ایران و حامیانش» آغاز کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78374" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=qeWbjN4D18NWiAk7OfZ94hA2js_9xsCQMyf2H6V3q6O51JeCO5TBjURAmJ79hBYkT7RfhENSptw1_KecAnS2GrEqDrkYO49CpUxTHSq74_14sPCujCv7r4SophT947kBB7cYzpteDRreTkLt1g4uvDKVv7AyazjByeg_ddDHqIsi6tsswBD8tnuX3Z8PzlB68ORyCU8jzdQSsago5ptZbKkc1arXgSnYa-bocne-KBsEVenvpBHJCCm20Jc21FUfp8Fvmr0rD3y3Q2ftZeF_9Nwh8coXS4M1iagrBxFF5YKl76OaCCVyHsSEGgkUcV_jEnJGCcqp3gD6kuVglkYOhg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=qeWbjN4D18NWiAk7OfZ94hA2js_9xsCQMyf2H6V3q6O51JeCO5TBjURAmJ79hBYkT7RfhENSptw1_KecAnS2GrEqDrkYO49CpUxTHSq74_14sPCujCv7r4SophT947kBB7cYzpteDRreTkLt1g4uvDKVv7AyazjByeg_ddDHqIsi6tsswBD8tnuX3Z8PzlB68ORyCU8jzdQSsago5ptZbKkc1arXgSnYa-bocne-KBsEVenvpBHJCCm20Jc21FUfp8Fvmr0rD3y3Q2ftZeF_9Nwh8coXS4M1iagrBxFF5YKl76OaCCVyHsSEGgkUcV_jEnJGCcqp3gD6kuVglkYOhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رشت، حامیان حکومت شبانه به آشکده سحرخیزان حمله کردند.
در ویدیویی که آشکده سحرخیزان منتشر کرده بود، عبارت "آش برای افراد با حجاب رایگان است"، به دیوار نصب شده بود و در چرخش دوربین، چندین مرد محجبه در صف ایستادند.
همین بهانه‌ای شد برای یورش و تخریب مغازه.
این اتفاق یکشنبه، ۲۲ شهریور ۴۰۵ رخ داد.
دادستان بلافاصله علیه آن اعلام جرم کرد و مدیر رستوران بازداشت و خود رستوران پلمب شد. ولی انگار این واکنش از نظر لباس شخصی‌ها کافی نبود و دیشب ریختن رستوران رو تخریب کردند.
via
pkhwshhal
,
yaghma_fashkham
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78372" target="_blank">📅 18:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشگاه تهران - دانشجو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQ8-D5B1F_idJ0VL1poRj48nK4meDpXIWwFE9z90m4bBEoMyt2LctsPrB7I1c89hoVjfuNloRxtWdaXg-JWD50WPc5bv2tnw5xnn9STmEZO-iim2aoRlRMN0e99OtW3mxVBDNkG_sKabtnvRH9UgQP3TiBljRV3DlIAcT_ZsmF9tpa8gU-nSc9kQ3fX5unxZG7c0f7xGCWAfkKebGHuxFxK6-y6zDzI8Yl1ww-SKNjViKlolf4EtmdiYBV4AOKSK8ChyETB_PuN_xe-nHXG2pt-Lk0a2uQPE1yTeP3nxskaldQlK4CoVTV7QsJtnH8edGEV1H5rUC5A0hYKYV3sfpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اتهام «بغی» برای محمدپارسا گلچین، دانشجوی دانشگاه تهران و دارندهٔ مدال طلای المپیاد!
بنابر گزارش‌های رسیده به تهران-دانشجو،
#محمدپارسا_گلچین
، دانشجوی ورودی ۱۴۰۳ کارشناسی ادبیات دانشگاه تهران و دارندهٔ مدال طلای المپیاد ادبی، به «عضویت در گروه
باغی
» متهم شده است.
همچنین، «اجتماع و تبانی علیه امنیت داخلی» و «اقدام تبلیغی بر خلاف امنیت ملی» دیگر اتهاماتی‌ست که به این دانشجوی نخبه وارد گشته است. او در جهت دفاع برابر عناوین مذکور، به شعبهٔ ۲۶۸ بازپرسی دادسرای عمومی و انقلاب مشهد احضار شده است.
محمدپارسا گلچین، شنبه ۲۲ فروردین ۱۴۰۵ به همراه جمعی ۱۸ نفره از دانشجویان در جریان یک بازدید دوستانه، توسط مامورین مسلح و به‌طرز خشونت‌آمیزی بازداشت شده بود
. پرونده سایر بازداشت‌شدگان نیز در جریان است و در انتظار دریافت حکم و احضاریه هستند. درصورت دریافت اطلاعات تکمیلی، گزارش پرونده‌های سایر دانشجویان متعاقبا در تهران-دانشجو منتشر خواهد شد.
#سرکوب
#بازداشت
#دانشجوی_زندانی
دانشگاه تهران-دانشجو
اینستاگرام
🆔
@Daneshjo_UT</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78371" target="_blank">📅 17:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=lAwRF28J173nZsAfL-pZtqEMu1JXNNjKpHFB7ytwK9eyPxMRGFKPo0uIF99bC1RAAFrWBZoAy1ctGpzp1Dh03CO9D9mtY59SY3B-yk7PK7YOC88xrGK8u9ybINHlEqFOlrhk41b5arjveMw3DqrE0TZJU51k8_EfG18avHXYCCWWKohsd-rkfufOI7IQBBEKFSnXPbDU5AHi0W1V-BXGzrpROZ4oUvacc1vPlKEBWZwIq1vVLHWfuTqvTfJ3R3jX62x_iUSSYd0spnn84UCDWEyljBObclAlZecZQiN27NLQpfPYzMuwn1Tzvyi6Tr_x0mRbGBpJTXtujl_zlwiDqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=lAwRF28J173nZsAfL-pZtqEMu1JXNNjKpHFB7ytwK9eyPxMRGFKPo0uIF99bC1RAAFrWBZoAy1ctGpzp1Dh03CO9D9mtY59SY3B-yk7PK7YOC88xrGK8u9ybINHlEqFOlrhk41b5arjveMw3DqrE0TZJU51k8_EfG18avHXYCCWWKohsd-rkfufOI7IQBBEKFSnXPbDU5AHi0W1V-BXGzrpROZ4oUvacc1vPlKEBWZwIq1vVLHWfuTqvTfJ3R3jX62x_iUSSYd0spnn84UCDWEyljBObclAlZecZQiN27NLQpfPYzMuwn1Tzvyi6Tr_x0mRbGBpJTXtujl_zlwiDqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفحه اینستاگرام رستوران «دستپخت بی بی» در تهران، به دلیل انتشار یک استوری با نوشته «هیچی کتلت بی بی نمیشه» به همراه موسیقی متن «بی بی گل» از معین، به اتهام «انتشار محتوای مجرمانه»، با دستور قضایی مسدود شد.
پیش‌تر نیز در سال ۱۴۰۱ نواب ابراهیمی، آشپز، در پی انتشار دستور پخت کتلت در اینستاگرام خود همزمان با سالگرد کشته شدن قاسم سلیمانی، بازداشت شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78370" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/shN7FgPr4i91bLDFq84UE73qgHHEWBd4WRI8tZSexjgUOWBki-qXErZM9TeBXPiaVvcgxk-HDMGhz1HzaM6aGHFqZ8TB9aODfJV6q-0rHCJ1b5JAEC8B82hW8UXNFD6Un6ZNEENzuiHPRS2fSzAKbPLxjL2AXsAeqf0ysWZZmRzAQyDxV7PaL-s-8bgxluBDUQOsd4I00kt42oqHPW0nViEupjx3se7UkuxYbZBlRNCqfbi6ASByMa8TKVXfLiTEgnodv0CWO6fhxych_1HYzGf3fdkjSSUdQFgUJFhFqruZe39Dr9FRxWun6m6FwD92WMIajI0gwpyxqUVVoJRJpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CDqGi0Jo6Y0LZh2QEfYbMeS9HDeDc3kY0c3mFeJxgrzIS-evSejwvm2gB9HeUZ4ByQ8Q7mFRAlArn7IiLJemTzDI9yGxUJZOgKMNnONBqWSISVv8B8YYAf96yXkFu1boyImOBJGA0QW-jdW6fByB2WD81L8mVk1rSK53YFGOFvFu0VpNbF8hMPEPL8lcqCih6P7XxorzwRmQKJQEHkyHBG5b1bRT_sXjYpHSpxmldj2xMhvBh4lzssHpHbBFqSu2sJJw1DrPMVoGhMVyJkRLdoX2BGVyK6xgy02EetY0YPtxCvtCJYh3f6IrYsmIExWV7u8MJuFzvBMZQVaaasp0sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«یحیی سریع»، سخنگوی نظامی حوثی‌های مورد حمایت جمهوری اسلامی، از انجام عملیاتی گسترده با ده‌ها پهپاد و موشک بالستیک علیه اهداف نظامی در منطقه خمیس مشیط عربستان سعودی خبر داد.
سریع گفت پایگاه هوایی «ملک خالد» در این منطقه هدف حمله قرار گرفته و آشیانه‌های جنگنده‌ها، رادارها، باندهای پرواز و انبارهای مهمات از جمله اهداف حوثی‌ها بوده‌اند.
سخنگوی نظامی حوثی‌ها این عملیات را پاسخی به حملات هوایی عربستان سعودی به یمن دانست.
@
VahidHeadline
«محمد بن سلمان»، ولیعهد عربستان سعودی، امروز دوشنبه ۲۳شهریور۱۴۰۵ در جده با دریاسالار «برد کوپر»، فرمانده فرماندهی مرکزی آمریکا، سنتکام، دیدار و درباره تحولات اخیر منطقه گفت‌وگو کرد.
خبرگزاری «رویترز» به نقل از رسانه‌های دولتی عربستان سعودی گزارش داد این دیدار در شرایطی انجام شده که درگیری میان عربستان و حوثی‌های مورد حمایت جمهوری اسلامی در یمن شدت گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/78368" target="_blank">📅 16:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K03IXDUAp0rsP8-lBJus-Ewra8Z2Tib1vRxIYjIEdpmoU2eug1kS8vOdsZr02ee0ZhpbKJEZbmgBIEv9WDGxTJFzBbySZxqmdFuk1ILu0SrS1AmIieehDZLVA9RmeLrj2q-0N1ozMyqGi4Oni8H0TwyJ4ckQv9XaBNNV8ylE_6xUSYEO-kQM_R3HQGtPos6Z55sdgf98TojziymXxGZp8e4sCbLM-N7jFDWOgIw6Gwt1EkDAyHffqPMl-xU4LWj-A5QwFYuxgiYIzMs73z9qDFxqtFFNO2RRedkIyZJLQMkxdsHBPVfnbBrZREWOb9P5rcqBiGa4GCWlVLuA7ZPnig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین امروز دوشنبه ۲۳شهریور۱۴۰۵ گزارش‌ها درباره کمک نهادهای چینی به جمهوری اسلامی برای هدف قرار دادن یک پایگاه نظامی آمریکا در اردن را تکذیب کرد.
خبرگزاری رویترز به نقل از وزارت امور خارجه چین گزارش داد پکن «قاطعانه با این اتهامات بی‌اساس مخالف است».
این واکنش پس از آن مطرح شد که روزنامه «وال‌استریت جورنال» به نقل از مقام‌های آمریکایی که نام‌شان فاش نشده است، گزارش داد جمهوری اسلامی پیش از حمله موشکی ۱۷شهریور به پایگاه «موفق‌السلطی» در اردن، تصاویر ماهواره‌ای این پایگاه را از نهادهایی در چین دریافت کرده بود.
در حمله موشکی جمهوری اسلامی به این پایگاه نظامی آمریکا، سه نظامی آمریکایی کشته شدند.
براساس گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی نام نهادهای چینی را که گفته می‌شود تصاویر ماهواره‌ای پایگاه را در اختیار جمهوری اسلامی قرار داده‌اند، اعلام نکرده‌اند. این مقام‌ها همچنین دولت چین را به مشارکت یا دخالت مستقیم در این اقدام متهم نکرده‌اند.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، نیز روز یکشنبه ۲۲شهریور۱۴۰۵ به گزارش‌ها درباره دسترسی جمهوری اسلامی به تصاویر ماهواره‌ای یک پایگاه نظامی آمریکا در اردن از طریق نهادهای چینی واکنش نشان داد.
ترامپ گزارش مربوط به دستیابی جمهوری اسلامی به این تصاویر، پیش از حمله‌ای را که به کشته شدن سه نظامی آمریکایی منجر شد، «کم‌اهمیت» دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78367" target="_blank">📅 16:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78365">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gzXjJRELxLin4bn16T7ZbuI-Bq_MRJq-XA6GtVfGEhtvX6ks8bxUuULII9cvZbykZ2gizq39nxsbuBaDEZ04FDbe0t4rlxP5uwQicNp8napfKLc_r4QgV7gDQTpZzOlaVubmxVnAcrn9Wc40cA69xxUoXaFHj8Le7d5rSTxUZzX0gQHKkm3p7lepkqBl8K2nd9UKeSLnQUxo3u6nU0Pap3TmJN6-e9Ce8wWll00rvWm-5MIOadIuIwBoJ5k8szlmwC2lFTnibR_dGqUs6DmT8phZtjuC0Z5T559k__NExykXXghbfKtJzWBBwaned0bZSZ0emNe_7ol5ZjnCmJ-A_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/avxn93VMWOUrb8t61DV9GxdbAuMpCCdOKzqe1KA9mHMMBcU1Aj-EfeV29uzq6pLRFk_Xk2JlsZqPxGUalRgYUtaTlx6DxrmvEwShPLkENwHG0zSyBffmpY2A13j5DhBvJiw8gwzR7ohurRRjzqn-_umJAPwyGkJazEu_JGwzZuqcAbx5lettw9jMPoSZ_9JB_JoQHZhZle9SQ4Axh7wMLhEOmm2hDh1LZno0Ckk--2Z3y5PpkQwLtzX56SJkyCWVnqdjB50DMwvppnYxECKe5kWF2AmPr1KhUlVK4jGxTnLDCQ72EY7LPdJ7v0Di1hnmnOaaW2YrI5Rqn-a1to74Dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز دوشنبه و پس از اعلام خبر صادر نشدن ویزا برای محمد اسلامی، رئیس سازمان انرژی اتمی ایران برای شرکت در نشست مجمع عمومی آژانس بین‌المللی انرژی هسته‌ای در وین، از احضار کاردار اتریش در تهران خبر داد.
بقایی با اعلام این خبر گفت می‌دانیم که این تصمیم تحت فشار آمریکا گرفته شده است اما این واقعیت، چیزی از مسئولیت اتریش کم نمی‌کند.
@
VahidOOnLine
پیش‌تر:
به گفته یک مقام آگاه که با اسوشیتدپرس گفتگو کرده، محمد اسلامی، رییس سازمان انرژی اتمی ایران، برای نخستین بار در چند سال گذشته احتمالا در نشست سالانه کشورهای عضو نهاد ناظر هسته‌ای سازمان ملل متحد در وین شرکت نخواهد کرد، زیرا از سفرهای بین‌المللی منع شده است.
این مقام گفت اتریش از کمیته تحریم‌های سازمان ملل خواسته بود برای اسلامی معافیت از ممنوعیت سفر صادر شود، اما این درخواست پذیرفته نشد.
این مقام که اجازه اظهارنظر درباره این موضوع حساس را نداشت، به شرط ناشناس ماندن صحبت کرد.
اتریش به عنوان میزبان سازمان ملل متحد در وین می‌تواند برای مقام‌های تحریم‌شده درخواست معافیت از ممنوعیت سفر کند تا آنها بتوانند در نشست‌های بین‌المللی سازمان ملل حضور یابند.
به نوشته این خبرگزاری آمریکایی، حضور نیافتن اسلامی در کنفرانس آژانس بین‌المللی انرژی اتمی نشانه دیگری از وخیم‌تر شدن سریع روابط ایران و کشورهای غربی است.
از زمانی که اسرائیل و آمریکا در جریان جنگ ۱۲روزه به تاسیسات هسته‌ای ایران حمله کردند، جمهوری اسلامی اجازه دسترسی بازرسان آژانس به تاسیسات هسته‌ای آسیب‌دیده در این حملات را نداده است؛ این در حالی است که تهران بر اساس تعهدات خود در چارچوب پیمان منع گسترش سلاح‌های هسته‌ای، از نظر حقوقی موظف به همکاری با آژانس است.
آژانس همچنین نتوانسته است وضعیت ذخایر اورانیوم ایران با غنای نزدیک به سطح مورد نیاز برای ساخت سلاح هسته‌ای را راستی‌آزمایی کند.
تحریم‌های سازمان ملل که دوباره برقرار شدند، شامل ممنوعیت سفر، تحریم تسلیحاتی متعارف، محدودیت‌های مربوط به توسعه موشک‌های بالستیک، مسدود کردن دارایی‌ها و ممنوعیت تولید فناوری‌های مرتبط با برنامه هسته‌ای است.
با وجود اظهارات این مقام درباره احتمال عدم حضور اسلامی در کنفرانس، خبرگزاری دولتی ایرنا روز شنبه گزارش داد که اسلامی تهران را به مقصد وین ترک کرده است تا در کنفرانس آژانس شرکت کند و با نمایندگان کشورهای مختلف دیدار داشته باشد.
مقام‌های ارشد کشورهای عضو آژانس بین‌المللی انرژی اتمی قرار است از دوشنبه تا جمعه در مقر این نهاد در وین گرد هم بیایند.
آنها درباره بودجه آژانس تصمیم‌گیری و آن را تصویب خواهند کرد و درباره دیگر مسائل سیاست‌گذاری، از جمله پادمان‌های هسته‌ای در خاورمیانه، گفت‌وگو خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/78365" target="_blank">📅 16:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78364">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JWl55D-p6cBG8ja3W2sj5QASEAKuhLHz0SEN82o8UJhV_Qp1Zaw6mi-7s2M8PIhL4pR9lbg5gOrpMGGqgIkn0zOGz-eUunnfo6R-2OV5yD3jgtrUlXC44TpvvwqW_Il45lyWy5nCiOaMB70TawkWihwclzrjn-cEEnH084nZTfn7kFMqSzdadhGTPngZX9N2Fj0_vQTdlLKy9NFGzoyCELFKdjTYuKe0kEJEz6ze8fqGD_gNi9BBpDILi8ZgkhOvDHPIM_aFjgi4MlcRbc5P_FLQfgxqy6PnWUhBCauRK_it7lnJyoJzn8xMihiQwyacgLCc7uckt4E9ptSjQRKOsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آستانه چهارمین سالگرد قتل حکومتی مهسا ژینا امینی از اصفهان، رشت، فومن، مشهد و نیشابور ‌خبر از تشدید فشار برای تحمیل حجاب اجباری و حضور دوباره گشت ارشاد، حجاب‌بان‌ها و نیروهای لباس‌شخصی در خیابان‌ها می‌دهند.
یک شهروند گفت در میدان علیخانی اصفهان ون گشت ارشاد مستقر شده‌ است و ماموران «بدون تذکر قبلی»، زنانی را که حجاب اجباری ندارند بازداشت می‌کنند و با خود می‌برند.
شهروند دیگری فضای اصفهان را «به شدت امنیتی» توصیف کرد و گفت نیروهای گشت ارشاد در مناطقی چون جلفا، مرداویج، چهارباغ و میدان نقش جهان مستقر شده‌اند و با زنان بدون شال و روسری، برخورد می‌کنند.
یکی دیگر نوشت: «در اصفهان دیگر ون گشت ارشاد نیست، اتوبوس است. با اتوبوس دختران را جمع می‌کنند و می‌برند.
...
در مشهد نیز شامگاه ۲۲ شهریور، نیروهای مسلح وارد پارک ملت شدند و به زنان تذکر حجاب دادند.
شماری از شهروندان از رشت گزارش دادند برخوردهای قهری درباره حجاب اجباری در این شهر شدت گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78364" target="_blank">📅 16:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=B7aJzrh_Y9tSdxdOifxKWkMBk8eTAHbP_oRRSM1z67M_JiK5Lff_rQQ_EIQWB4mZANG3zdEtXefJ8XAuc1_TM9HEx7aHt9R8xrhFFZ8cQPyQ0FyZWhTVT3uwPLczLdJnwM5BSgHt6rnZz2_Xx6lVqNf545f1w1ybU5hM3gNkBhKxTYodXEQQBXKaEmJhO9R2kMOOvNef4IfHWvYeLTMNaVQt96iXTGUm-0rEFi6QbOyO6fFsSXBBTQB4JNu7_4losm5p9irGOVhggy9CR7eECE9zx7J55l4486TKMSm9rXhTVeAP6uj3rCuVV6sjaecpsQbuB568lRMs0OIC-sMO0w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=B7aJzrh_Y9tSdxdOifxKWkMBk8eTAHbP_oRRSM1z67M_JiK5Lff_rQQ_EIQWB4mZANG3zdEtXefJ8XAuc1_TM9HEx7aHt9R8xrhFFZ8cQPyQ0FyZWhTVT3uwPLczLdJnwM5BSgHt6rnZz2_Xx6lVqNf545f1w1ybU5hM3gNkBhKxTYodXEQQBXKaEmJhO9R2kMOOvNef4IfHWvYeLTMNaVQt96iXTGUm-0rEFi6QbOyO6fFsSXBBTQB4JNu7_4losm5p9irGOVhggy9CR7eECE9zx7J55l4486TKMSm9rXhTVeAP6uj3rCuVV6sjaecpsQbuB568lRMs0OIC-sMO0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ویدیوی نجات خلبان آمریکایی در ایران
۲- یک نفر از ۷ نفر سوت موشک که داره به سمتشون میاد رو می فهمه.
سعی می کنه به نفراتش خبر بده اما نمی دونه کدوم طرف بدوئه. در نهایت یک انفجار هر ۷ نفر رو می بلعه.
A_z_im
سی‌بی‌اس پس از پنج ماه با یکی از دو افسر ارتش آمریکا گفتگو کرده است که در نیمه فروردین‌ماه هواپیمایشان در اطراف اصفهان سرنگون شد.
این افسر که براوو معرفی شده، لحظه برخورد موشک دوش‌پرتاب با جنگنده اف-۱۵ آنها را مانند برخورد یک قطار باری توصیف کرد و گفت به همراه خلبان که در این گزارش «آلفا» معرفی شده، تلاش کردند هواپیما را نجات دهند اما خیلی زود دریافتند که امکان نجات هواپیما نیست و باید خروج اضطراری انجام دهند.
پس از خروج اضطراری (ایجکت)، آلفا و براوو در حالی روی زمین در بیابان ناهموار در ایران فرود آمدند که حدود هشت کیلومتر از یکدیگر فاصله داشتند و هرکدام تنها بودند.
آلفا سالم فرود آمد، اما براوو خوش‌شانس بود که زنده ماند.
براوو گفت: چتر نجاتم در حمله اولیه آسیب دیده بود. یک لحظه به بالا نگاه کردم و دیدم چتری وجود ندارد؛ ترسناک‌ترین چیزی بود که در تمام عمرم دیده بودم. همان‌جا مکث کردم و دعا کردم: «خداوندا، اراده تو انجام شود. اما اگر قرار است از این ماجرا جان سالم به در ببرم، به کمک نیاز دارم.»
او در پاسخ به این پرسش که «فکر می‌کنید هنگام برخورد با زمین با چه سرعتی حرکت می‌کردید؟» گفت: براساس توضیحاتی که دادم و جراحاتی که داشتم، متخصصان معتقدند با سرعتی بین ۱۱۳ تا ۱۶۱ کیلومتر در ساعت با زمین برخورد کردم.
او افزود: یک معجزه در روزگار مدرن بود. باور دارم این اتفاق گواهی بر لطف خداوند در زندگی من است که باعث شد از آن لحظه عبور کنم؛ به‌گونه‌ای که هرچند دچار جراحت شدم، اما آسیب‌های فاجعه‌باری که می‌توانست توانایی‌ام برای زنده‌ماندن را از بین ببرد، متحمل نشدم.
این سقوط باعث شکستگی کمر براوو شد. او همچنین دست و شانه‌اش شکست، مچ پایش پیچ خورد و سر و صورتش بر اثر بریدگی و خراش خون‌آلود شد.
براوو گفت، مجروح بودم، اما همه ما آموزش دیده‌ایم که با شرایطی که با آن مواجه می‌شویم سازگار شویم و بر آنها غلبه کنیم. با وجود جراحات، تا جایی که می‌توانستم سریع از محل فرودم دور شدم.
براوو به سی‌بی‌اس گفت امن‌ترین جایی که می‌توانست به آن برود، ارتفاعات بود.
بنابراین با وجود شکستگی استخوان‌هایش تصمیم گرفت از مسیر کوه بالا برود و خود را به خط‌الرسی در ارتفاع حدود ۲۱۰۰ متر، برساند.
@
VahidOOnLine
چیزی که می‌بینم رسانه‌ها و کاربران فارسی‌زبان دقت نمی‌کنن اینه که این مصاحبه نمی‌گه که افسر آمریکایی با دست و پای شکسته کوه ۷ هزار پایی رو بالا رفته؛ بلکه می‌گه خودش رو به ارتفاع ۷ هزارپایی رسونده. بین این دو تا خیلی فرق هست.
در نظر داشته باشید که خود اصفهان بین ۱۶۰۰ تا ۲۰۰۰ متر از سطح دریا فاصله داره. یعنی ممکنه ایشون فقط با صد متر صعود خودش رو به ارتفاع ۷ هزار پایی برسونه.
Ardeshir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78362" target="_blank">📅 08:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78361">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KDl-vVH9OmJPCPJ_MstJDwMyyMW9Sr1UJs4HjdeuFZ-58-eshthQRrR0FyPlBOHf_C8neGksOdDiuSBRzM_K36mI6AoECfAmTErWmUPy37RHtPFBQ0-5IiBkgh5gV8rIZNCE7q3aQvOcbJLmB_GkzOL_SwofPV2liqj1g741Edt958Dug_Brqy1R5YbAFQcs1lv-ji2L5D5_uMJ9ptcgf3o-MarY0C9S4J6PAWL78MwKdPXqhF_n8Q9c7xkcBFQ3L-0xRYnUdHDHGyDxmVuCtnbAIT2jz-slHPJSpGLyspJsg9AgkZA3LdmH0LIxkSiqttTNqZIFB70zm6pmGnHhfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه عمان از تعویق‌ نشست ایران و کشورهای حوزه خلیج فارس و منطقه خبر داد؛ نشستی که قرار بود روز دوشنبه ۲۳ شهریور در شهر صلاله عمان با محوریت وضعیت تنگه هرمز برگزار شود.
بدر بوسعیدی، وزیر خارجه عمان، روز یکشنبه ۲۲ شهریور در شبکه ایکس نوشت که این نشست «به منظور دستیابی به اجماع» به تعویق افتاده است.
او تاکید کرد عمان همچنان به تقویت گفت‌وگوهایی که به «ثبات و همکاری پایدار در منطقه» کمک کند، متعهد است.
عباس عراقچی، وزیر خارجه جمهوری اسلامی، پیشتر گفته بود که روز دوشنبه در نشست هشت‌جانبه وزرای خارجه کشورهای ساحلی خلیج فارس و دریای عمان در صلاله شرکت خواهد کرد.
قرار بود در این نشست درباره طرح ایران و عمان برای ایجاد سازوکاری جهت تردد امن کشتی‌ها در تنگه هرمز گفت‌وگو شود.
تعویق این نشست در حالی اعلام شده است که آمریکا پیشتر تاکید کرده بود در مذاکرات مربوط به تنگه هرمز مشارکت نخواهد کرد و هرگونه مذاکره مستقیم با جمهوری اسلامی را بر پرونده هسته‌ای متمرکز می‌کند.
مقام‌های آمریکایی به کشورهای منطقه گفته‌اند واشنگتن درباره وضعیت تنگه هرمز مذاکره نخواهد کرد و موضوع اصلی مذاکرات احتمالی با تهران باید برنامه هسته‌ای جمهوری اسلامی باشد.
مارکو روبیو، وزیر خارجه آمریکا، نیز پیشتر گفته بود تنگه هرمز نباید تحت کنترل جمهوری اسلامی باشد و آمریکا برای تضمین امنیت کشتیرانی در این مسیر اقدام خواهد کرد.
در مقابل، جمهوری اسلامی و عمان تلاش کرده‌اند کشورهای منطقه را در گفت‌وگو درباره سازوکار تردد کشتی‌ها در تنگه هرمز وارد کنند.
قرار بود نتایج رایزنی‌های تهران و مسقط درباره مسیرهای امن کشتیرانی در این نشست به کشورهای منطقه ارایه شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78361" target="_blank">📅 22:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78360">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOAlfVQb7Y6AiynIFeEjqg3dhKqb6lQWqAvJ0Bb-lWEf--i01JpXTs6j9fDIPrRl0Z-K2Ozpix-yj5hA7Zi7pz7TGs6FbQvJnP4IsbJGCrHp0GDe5G0jIzbvX6RJ7okuQU2pP9gFPJrcO6kEkC_sBtKay8kiof778nSoks1K8-c-t6G3Hrq_gxbNA8mvNrxixoi4fZgwjeGuB3v_peDMJ503WrrSThJonItvG6kusyZT2cLUy5S73voFp71PMbNpAklBqj1kfcjvBQoA571x5XCc-S_PGs-DUsTX63BU47T3EHd81rkk26j7iLfMq-5uCuu2s_Y06D25i9e6g0C7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه نیویورک تایمز روز یکشنبه ۲۲ شهریور ماه در گزارشی به نقل از چند مقام ایرانی نوشت، مسعود پزشکیان، پس از حمله نیروهای سپاه پاسداران به سه کشتی تجاری در تنگه هرمز در اوایل تیرماه گذشته، به‌شدت خشمگین شده و این اقدام را «بی‌پروایانه و غیرمسئولانه» خوانده است.
این حمله‌ها که منجر به آتش‌سوزی یک نفت‌کش حامل گاز مایع قطر و آسیب به شناورهای دیگر شد، درست زمانی رخ داد که ایران به توافقی با ایالات متحده برای پایان دادن به درگیری‌ها نزدیک شده بود.
بر اساس این گزارش که فرناز فصیحی به نقل از مقامات ایرانی نوشته است، پزشکیان پس از آگاهی از این ماجرا با احمد وحیدی، فرمانده کل سپاه پاسداران، تماس گرفته و با لحنی تند خواستار پاسخگویی شده است. با این حال، وحیدی ضمن سلب مسئولیت و ابراز بی‌اطلاعی، به رئیس‌جمهوری اعلام کرده که نه مجوزی برای این اقدام صادر کرده و نه شورای عالی امنیت ملی از این عملیات مطلع بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78360" target="_blank">📅 22:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/930e263d13.mp4?token=TBpH6oWfqfayPjzRPggOmj3jdCj60VTSYosb2Tuc4mGt9f4akZk-Hb7geDgAW8lK2iZOimlwoJ9AeiPikCKXMK7hHIVyDNPNsuSzYronXza7wr_LaFoqEsp-PDszRr1pvBuZoZd4k8_dtpDBXH8wneKs-tB1kh3Ur2K_vK-2hJrtwowyKc1m3xvM1dVGk5oFZ_toZr4J_jb_LJtxWAS5XupeZZwnjC36sdCwo1VyvdafKf9aBcqxgUNXFtYkdsY-MI_ydxleBHoAc0WQTBTAQEQWkSrrp-frfuqXtbs2GUwzQi3-ZUWaOa4y7bAivnZbxpUj3USR5zu9pVymIGksCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/930e263d13.mp4?token=TBpH6oWfqfayPjzRPggOmj3jdCj60VTSYosb2Tuc4mGt9f4akZk-Hb7geDgAW8lK2iZOimlwoJ9AeiPikCKXMK7hHIVyDNPNsuSzYronXza7wr_LaFoqEsp-PDszRr1pvBuZoZd4k8_dtpDBXH8wneKs-tB1kh3Ur2K_vK-2hJrtwowyKc1m3xvM1dVGk5oFZ_toZr4J_jb_LJtxWAS5XupeZZwnjC36sdCwo1VyvdafKf9aBcqxgUNXFtYkdsY-MI_ydxleBHoAc0WQTBTAQEQWkSrrp-frfuqXtbs2GUwzQi3-ZUWaOa4y7bAivnZbxpUj3USR5zu9pVymIGksCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش، پس از اعلام نرخ سوم بنزین در ایران، تصاویری واقعی در شبکه‌های اجتماعی منتشر شده بود درباره اینکه بعضی از تلمبه‌ها در جایگاه‌های سوخت (پمپ بنزین) امکان نمایش همه ارقام بنزین ۱۰ هزارتومنی رو ندارند و مجبور شدند در ادامه نمایشگر یک صفر بچسبونند روی بدنه تلمبه.
حالا محمدباقر قالیباف، رئیس "مجلس شورای اسلامی" در «ایران»، اون انیمیشن رو پست کرده.
ولی درباره قیمت سوخت در یک کشور دیگه:
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78358" target="_blank">📅 21:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QP_toD6lTbJPpDVjV3h4Ow324RhWGljr9bXNhb5TYpZ7pHC5y1BC5LBvonrYkSBJpTj1kMVwwU2A_3R5zy_Y_AAPnowv9DczUQpMm0f0NHKW6rlooRigc7fFY1aJK90wsVcMhylgSeukBg4BWCDnT68YWLFhS1umfMqq3SYaBxjEW9uHdfQ-ISyRGQD1fcQA93vqv3gXdcetEooQwyxq0VZf8Plmu12criWvfg6_XZYZjKhUxOCPw2rs1MQB4vc0xTFjDhiQZ01eFMajvBpuewNz5q5Ni-ul9VfaXOPaiB22dVPovP48bdCJ-BAJrWU7gu59hRnL735yVA7MOrEBxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین رسولی‌نسب، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در شاندیز، به اتهام «محاربه» از سوی دادگاه انقلاب مشهد به اعدام محکوم شده است. او در حال حاضر در زندان وکیل‌آباد مشهد نگهداری می‌شود.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، روز یکشنبه ۲۲ شهریور ۱۴۰۵، گزارش داد حسین رسولی‌نسب به «محاربه از طریق مشارکت در تخریب اموال عمومی» و «اجتماع و تبانی علیه امنیت کشور» متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78357" target="_blank">📅 18:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kd-UxwfZ46TcwKY8nFpcbaJw9kpeyKcHJOLXuMCEyRl6ECYlRUb1Cr1nFOexYxblZDuHHo0yUiO9hGyARLUcvBjw6r8cvH4wrTtDKZMvr0eXrNAudgAEfN9SidR73TnNm0GVy9PCr1P6adshivZD1bQaROeb2UNbs0Ez4gZcqiO763zN23ZykqAt_A5K01pMo2mpCH462LNzB7G678uSaiWL2ecw5WkC_VMtaKey4G9FZpk8lqAiqnekYR7X4-QEtZ7Ef8EEUXfFx5KhsOZPI2pBam0Fj7uVJu_xQTaCcWw9Z-Hy3kzPCvbMNO1TMyXyWBpx8aveJ3TCz2rlKbRPdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ohfXSjE2jEKLtku7ZBmSSBDXYZDABJLgqpDXoRicmOFcP17fUhys8Cjww4e3l5RYlJ7vexVFNtQJkjx_vhFB26ImGYKm1yY4tynRJqcCt4Dw_X9Dc0k07Yc1BP1qjnbQ6VCg0r9WpejBqsLmbTj5TE7JOfj8wClqLmEUriPMqSbGNXB5y9tZVRKu_WRjICcQgX8vqOhV-p-w_v9khuYNc8qXGV0vgw8xGYd1GmzUPGfVL0dX_lf70XG0ObmEwna6nVUw28AaHk29YcAfBkKDHJqBAhXcn5w579jj2Bltj2-HOeSLt6GF0gtn8n13Oya0Hw5nHBwVsqyLvTOnBNANmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان ثبت احوال: در کارت ملی‌های جدید از هوش مصنوعی و بلاکچین استفاده کرده‌ایم
quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78355" target="_blank">📅 18:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78354">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uzum15G4I4xz4wdEDeJEyIKYtIkgPWV-lK6RFj4H90kHwzxeRxjATOSwx0zZeqNdIZw7YT8yIVC8zWTPWBVWR1VrKCvWbu8wJRYA8hkM5gV96UVu10kwXA4fm6Kz-eDYZfkLHEuVNPCBNJYzG8tk5o5tKcFWFC_kZjHnG_noLO4JTBSOBxBavfr9ThdCpXz-KEcz-07S5E9Sztd65DBOGV9tVgznmVyvtJ5AOZP-3M-cZTrCu9vC6k6RJTLFHFzfoDoqjhTqWqkYYc6Lsi9alIDiGDJBfthAzg0u4g6sgFSEMJ9amPz5u20KHC3o6kSmCwWyLdZd-4DUBriwjF8B-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز یکشنبه ۲۲ شهریور۱۴۰۵، گفت «موضوع ایران» ممکن است پیش از انتخابات میان‌دوره‌ای آمریکا پایان یابد، اما در هر صورت جنگ با ایران بلافاصله پس از این انتخابات تمام خواهد شد.
ترامپ در جریان سفر به ایرلند و در حاشیه مسابقات گلف اوپن ایرلند، درباره احتمال توافق با جمهوری اسلامی گفت ایران به‌شدت خواهان توافق است و به‌طور مداوم با آمریکا تماس می‌گیرد، اما واشنگتن تنها توافقی را می‌پذیرد که به گفته او «درست» و مطلوب باشد.
او همچنین در پاسخ به پرسشی درباره دیدار وزرای خارجه کشورهای خلیج فارس و دریای عمان با ایران گفت این موضوع برای آمریکا اهمیتی ندارد و تصمیم درباره دیدار با جمهوری اسلامی به خود این کشورها مربوط است.
قرار است این نشست روز دوشنبه در عمان برگزار شود. ایران می‌گوید یکی از موضوعات مورد گفت‌وگو در این نشست، مسیر جدید تردد در تنگه هرمز خواهد بود.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز بار دیگر گفته است شرط ایران برای بازگشایی تنگه هرمز، بازگشت آمریکا به تعهدات خود در تفاهم‌نامه اسلام‌آباد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78354" target="_blank">📅 17:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q3GxVvE_G025TTgkq_iAtcqgxMEgcnploWDpBk-PjE7dCPOPF7YIFiuh7tlaSPROMHU31EZzsz39cC3gdzl_IbFKMYW_GvECJJKyt-0T9eI7zYIyeU_3RnKM0_2P9eiC8HKbJY3-CYRLJ05qCo1k6knHAFKyExbU57FMr1ZSB5B8xTdl8dc5pD3BMTVgkYUP4UJH9ng3Bj944IZe0da7ppSz1Xz8n7J0W948iTviSwm4ZGVXq7aiZjJXdHYna-M9dSv9bweSgypZKYOeRtdBnKQqBnLkEkZzh-kyYjlD_f2oqbnna8kmFOUZTzy2XqIsa2kelojaYzZL9Hf9YkVxMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h5QJs8neQ0CrWDqaC_M0gpDxeqvdkPLxPZI-RijTNfist7vHFHdtJ2v6yPpZZrvux8T5DOrTLfKReO8H_CIdkjS0hoA1Z7eh0nNzwzdZ4gfYBlMeSGBobzGcsIxijuq0gIdWiAKaOvV9pQAaa5r0Q4OG1Q7wZipeux5CBkE5-sGDJ6wMTsR8lC5P_QSDRXdK2sFFNZ-Cs1IJwWeB4lOsm5G2shgZYi39NiDuYt7JbaM1TjBIkw0v1xP0ssXdzuElXtY41W9Jp_JdiDFuba1ZZLwvilzJRjvLJMY0_F_CLuM3R6mf2Sh2hu2yJbhK43jyNArHk6YIaVWQWe-m0drk3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) روز شنبه، با صدور یک هشدار امنیتی، از هدف قرار گرفتن یک کشتی در تنگه هرمز خبر داد.
این نهاد نظارتی دریایی اعلام کرد: «گزارشی مبنی بر وقوع یک حادثه در محدوده تنگه هرمز دریافت شده است. یک کشتی هنگام عبور از تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفته است.»
@
VahidOOnLine
امیر تیموری، فرماندار شهرستان قشم، اعلام کرد یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب‌دراز جزیره قشم هدف قرار گرفته است.
به گفته فرماندار قشم، در این حادثه یک نفر کشته و سه نفر دیگر مجروح شده‌اند.
تیموری عامل این حمله را آمریکا اعلام کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78352" target="_blank">📅 15:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=n3EDgcFlEr2_ElIQ9T4vBQw7PFpyMbqs8Dyj06CxiKEvq0zkX9zPz07l1ZbdNPFrxdox20g6vkoLLdZn2FueO0M07Mcc6Bhm2enKAxWhdv5O38h_sVfpZUfUsbgu-P8tRNow92qvfF7q7tkyiT_S00i6tAMOnRkYXINlHkV3FKVrQ74zMB4zu8v-Qtck1kspJGrRswH3SHZt4Cc5eOtbkm4E-3tDvkKi8pbiuQa-8cNLvJOp5X3Oo0prN6BqqUb57FKzohesQNaGPrpUdiMcXLbner1zFt0AC3MVhIJxxz2_k_gI-ap7ClvbRIGmGCAoyBha-CLwd6M3abQm7TvMYDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=n3EDgcFlEr2_ElIQ9T4vBQw7PFpyMbqs8Dyj06CxiKEvq0zkX9zPz07l1ZbdNPFrxdox20g6vkoLLdZn2FueO0M07Mcc6Bhm2enKAxWhdv5O38h_sVfpZUfUsbgu-P8tRNow92qvfF7q7tkyiT_S00i6tAMOnRkYXINlHkV3FKVrQ74zMB4zu8v-Qtck1kspJGrRswH3SHZt4Cc5eOtbkm4E-3tDvkKi8pbiuQa-8cNLvJOp5X3Oo0prN6BqqUb57FKzohesQNaGPrpUdiMcXLbner1zFt0AC3MVhIJxxz2_k_gI-ap7ClvbRIGmGCAoyBha-CLwd6M3abQm7TvMYDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تور اجبارى اتاق شلاق براى "عبرت" متهمان
یکی از شهروندان با ارسال ویدیویی که مخفیانه از اتاق اجرای احکام شلاق ثبت کرده، مشاهدات و تجربه مستقیم خود را با بنیاد عبدالرحمن برومند در میان گذاشته است؛ روایتی که به‌زودی در قالب یک شهادت‌نامه تفصیلی منتشر خواهد شد.
او درباره انگیزه خود از انتشار این ویدیو پس از چند سال می‌گوید:
«آنچه در جریان بازداشت و صدور این حکم بر من گذشت، در برابر حجم بی‌پایان ظلم و بی‌عدالتی شاید اهمیتی نداشته باشد؛ آنچه برای من اهمیت دارد، تاباندن نور بر گوشه‌ای از این سازوکار مخوف است تا همگان ببینند مردم ایران برای داشتن یک زندگی معمولی با چه مجازات‌های تحقیرآمیزی روبرو می‌شوند.»
@
IranRights
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78351" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=C9zIi3uydGhz9WHWDVA_IMBvapDZ4LRTTXHeWRlgu18RjsTAWP5742-jv-arQketkmFlG4z2sCeQJ5KBskr9XUUPjANQO-ype3Lf0GrsK9Pp8jf4I5K0nkUzOAvBf-dAZls9xuKaiupav0bsuk-FvHDmDww4FIhbsZlsTnn9qCEJjX1IGasvkJRTmrbQY6opmqfjtRZuXfqdP4jBnYlv6kBmLF5NugfmEIMz-q7xi0pNBHgzgkOkgNpyo41K3R3drA3x87COUW-5jZPNnU4TNgu5hkFx9qfF_PA6WDHI6ym2m5XgEc6HCWQCnlCAQ5IhFBekpBAD_zTnKb6Bnu_KFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=C9zIi3uydGhz9WHWDVA_IMBvapDZ4LRTTXHeWRlgu18RjsTAWP5742-jv-arQketkmFlG4z2sCeQJ5KBskr9XUUPjANQO-ype3Lf0GrsK9Pp8jf4I5K0nkUzOAvBf-dAZls9xuKaiupav0bsuk-FvHDmDww4FIhbsZlsTnn9qCEJjX1IGasvkJRTmrbQY6opmqfjtRZuXfqdP4jBnYlv6kBmLF5NugfmEIMz-q7xi0pNBHgzgkOkgNpyo41K3R3drA3x87COUW-5jZPNnU4TNgu5hkFx9qfF_PA6WDHI6ym2m5XgEc6HCWQCnlCAQ5IhFBekpBAD_zTnKb6Bnu_KFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهوری آمریکا در جریان دیدار با مایکل مارتین، نخست‌وزیر ایرلند، در دوبلین بر اعمال کنترل مقتدرانه و یک «محاصره دریایی باورنکردنی» بر تنگه هرمز تاکید کرد و گفت این اقدامات مانع از جهش شدید بهای جهانی نفت شده است.
دونالد ترامپ همچنین گفت نیروهای سنتکام به‌طور میانگین روزانه ۲۵ شناور و قایق را متوقف و توقیف می‌کنند؛ اقداماتی که به گفته او بیشتر آن‌ها در تاریکی شب و در جریان گشت‌های شبانه انجام می‌گیرد.
این در حالی است فرماندهی مرکزی آمریکا، سنتکام،
امروز
اعلام کرد طی ۶۰ روز گذشته و از زمان ازسرگیری «محاصره دیوار فولادی» ایران، مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78350" target="_blank">📅 23:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghPhmj3ol3QfLChwO7h3kioL6Iky9Dqbn5NhuljXeWKirLVLHHzEq9jFD45m6GLgJsQwYhhk1yYrV7JPvfOH6HbDxz3OpiUTKTIAL75s_ttysGuieEx0zoU2obhqO_VA5hL2dJu44Pseh5rL75jMvuMiDh0IwaCv33nUtbnxkCot8l4_o35y-flDFeqCtv9fKa0l-d9cPkhMTcgACaEoSgceQ35hsuyMEWLztR5LizAdhKqp4Im6vca75RZBosa1CroKzPMyLe0TlMd6X3_JhLdPSi5x61JZyPMXUirKglSHie6gbPc1P9bNQo7PzGkYsF5_hWnq9BczB2X-4RXYYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واژگونی یک دستگاه اتوبوس حامل کارگران مجتمع مس سرچشمه، در صبح شنبه ۲۱ شهریور، یک کشته و ۳۸ مصدوم برجا گذاشت.
سید محسن مرتضوی، رییس مرکز فوریت‌های پزشکی رفسنجان، با تایید این خبر گفت ۳۸ مصدوم این حادثه برای دریافت خدمات درمانی به بیمارستان منتقل شده‌اند. به گفته او، بررسی‌های اولیه نشان می‌دهد ورود یک دستگاه ون به مسیر حرکت اتوبوس باعث انحراف و سپس واژگونی آن شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78349" target="_blank">📅 21:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRk3c0pJqiON5UO0_vjZTK1_LNMq-xLjNlGly0tFHxaGSygWk9QgV38gWh6x_j4JkXc4qdzUUKD_xIYL13q5RpKFSgnD7BDQQgMJs06A4vY4egXADbNaaGV0wszcb3UtttiSZ2GTtQQU27niVEPWpYdOwLZtgc-uQTtqkQsNRc6Dwjn_fl6XSyayLPa-5Mm3P_grJnzxHYc3w2Onz_UvVbVdqoBe4vcUHqOIgdp5andI5p2JKfx4Z1na0YLuy9Fqq1xeKkc0hxtSsKu30MeeqSKU6dF-TpUmu7wOBFZtu50sqymOcu89pq9oYVVXlhDbnCr5vqE_ng-bZi-s9MFZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع امنیتی عراق به خبرگزاری فرانسه گفتند نیروهای امنیتی این کشور سکوهای پرتاب پهپاد را منطقه دورافتاده الطیب در استان میسان در جنوب عراق و در نزدیکی مرز با ایران کشف کرده‌اند.
همزمان خبرگزاری رویترز به نقل از دو منبع نظامی در عراق اعلام کرد این منطقه مرزی پس از کشف سکوهای پرتاب پهپاد بسته شده است.
کشف این سکوها پس از حمله به خط لوله نفت عربستان سعودی انجام شده است؛ حمله‌ای که ریاض و بغداد گفته‌اند از خاک عراق انجام شده است. بغداد روز شنبه گذرگاه‌های مرزی شلمچه و چذابه را نیز بسته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78348" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIi0jTHr3zcShM2d9OuUNYxQjBX8v4LlMkWC08Zi7ICZeEQ5NAWoqp8rvq00vkWgrklZe7dEM5bsOEGNJvdtcfuGobDtHvXv-cNlxE3Zuc5jOwRc7w6jgaaoCPUy5T6V0u7_pmcTFXMt1ntkFrdx9PdTDzIJJ0VPDUVx5L0cYOq-0EBCXsnA3S6ip83sjqXmS9OR2roIFWs7AAgGKsRBG21CXhpU4CHdTWQgl_ouXVdC0qEIAynnBi3OsEeh9LhnNrkNW6v9yKMOhAFnvdIafMkfFcb5P98YbGwSMxtPf_nnzTrPGHPsgNJjdAjAg_EwWBKRpIjJN_du2ZfKOlOLww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، به نقل از یک منبع آگاه گزارش داد تفاهم نهایی جمهوری اسلامی و عمان درباره مسیرهای جدید کشتیرانی، به معنای بازگشایی تنگه هرمز نیست و باز شدن این تنگه به اجرای هفت شرط تهران از سوی آمریکا بستگی دارد.
این منبع گفت تهران و مسقط پس از گفت‌وگوهای فنی و دیپلماتیک، در اوایل شهریور درباره جزییات مسیرهای جدید ورود به خلیج فارس و خروج از آن به توافق نهایی رسیدند و قرار است این تفاهم به‌زودی با حضور وزیران خارجه کشورهای منطقه اعلام شود.
بر اساس این گزارش، تفاهم تنها میان جمهوری اسلامی و عمان است و کشورهای دیگر، از جمله عراق و کشورهای ساحلی خلیج فارس، برای اطلاع از جزییات مسیرها و ترتیبات تردد در نشست حضور خواهند داشت.
مهر نوشت مسیر ورود به خلیج فارس به‌طور کامل و بخشی از مسیر خروج از آن در آب‌های سرزمینی ایران قرار خواهد داشت و تردد در این مسیرها بر اساس ترتیبات تعیین‌شده از سوی جمهوری اسلامی انجام خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78347" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=vdLSO8Ze6sfz_GRG04eyULZH_vWJXew8LKRJbuGkbbWpY8sbXMUFDWi9DhiUei2eXN74MDhpkvPKhoX5zGn938rAnBNYyA3og4YWP6Hf3KXgfVAdWk5P8DiZLqaNy-QyM-ou7Q6zqmpVJZMJEBlOQZerwgBIaGcIc3siUB6nr-IkYuMEOWTb5aIQ3_mIO4EaRBviiwvEtdsuWtI27ZmlFHuMnDTF-Lud8Xw4dRZPFtB9nQzBwgLdxnn-kfugD2xMARkHAFgW01iAEnUuomErgTzoNCb8XntbUuYMN2fnWTgaZGXpSLCd4QhZoYoNAA8OHWerQWP23TxeOTgvg4Nfww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=vdLSO8Ze6sfz_GRG04eyULZH_vWJXew8LKRJbuGkbbWpY8sbXMUFDWi9DhiUei2eXN74MDhpkvPKhoX5zGn938rAnBNYyA3og4YWP6Hf3KXgfVAdWk5P8DiZLqaNy-QyM-ou7Q6zqmpVJZMJEBlOQZerwgBIaGcIc3siUB6nr-IkYuMEOWTb5aIQ3_mIO4EaRBviiwvEtdsuWtI27ZmlFHuMnDTF-Lud8Xw4dRZPFtB9nQzBwgLdxnn-kfugD2xMARkHAFgW01iAEnUuomErgTzoNCb8XntbUuYMN2fnWTgaZGXpSLCd4QhZoYoNAA8OHWerQWP23TxeOTgvg4Nfww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت امور خارجه، روز شنبه ۲۱ شهریور ماه گفت اطلاعات تهران نشان می‌دهد حمله موشکی آمریکا به لامرد از خاک یکی از کشورهای حاشیه جنوبی خلیج فارس نیز انجام شده است.
اسماعیل بقایی در گفتگو با رسانه‌های دولتی ایران گفت این موضوع نشان می‌دهد آمریکا «برخلاف همه قواعد و اصول حقوق بین‌الملل» از خاک و حاکمیت ملی کشورهای دیگر برای حمله به ایران استفاده کرده است.
او تاکید کرد ایرانیان این موضوع را پیگیری خواهند کرد.
بقایی همچنین گفت برخی کشورهای همسایه، برخلاف «اصل حسن همجواری»، اجازه داده‌اند از قلمرو آنها برای حمله به ایران و «ارتکاب جنایت جنگی علیه مردم» استفاده شود.
در نهم اسفند ۱۴۰۴، یک سالن ورزشی در لامرد فارس، مورد حمله دو موشک قرار گرفت که منجر به کشته شدن حداقل ۲۱ نفر، از جمله ۴ کودک، و زخمی شدن ۱۰۰ نفر شد. این حمله اندکی پس از حمله هوایی به مدرسه شجره طیبه میناب رخ داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78346" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2qBK6HZRrpXVm58RDSfj87gTQZqunGYb2mWH6KGd7AFtMC1PXIdLaVtq9umVaVSSiGc5w9Dipjn7VsjGIIi5lMLgm6KeUyAvbawcb1oKcUohZcLsfSR3L8kG7oEyR8Kfh9QBdwTftYfA4XVjHF8Iwh0bTETObCqPLoHUpprLmDvldXs47JUbJla947ug_sbAfdwGR0Znr0XFXFTmhL-WKBay1gqHbgUJI1XqGKXZE6kyyDLI60cDR5QxhGBqFPdXGNrCaSZ_7kBQ3aIlAMElZp3w8G2EaceFYDk5owtruPSm4rryzdF3_dvVXllkdymrz75OV5weCU-cn_HJavObw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت احتمالاً جمهوری اسلامی مسئول حمله هوایی به عربستان سعودی بوده که به تعطیلی خط لوله شرق به غرب انجامید.
او روز شنبه در دوبلین و در پاسخ به پرسش خبرنگاران درباره مسئولیت ایران گفت: «فکر می‌کنم مسئول‌اند، احتمالاً خودشان‌اند.»
ترامپ افزود با محمد بن سلمان، ولیعهد عربستان، گفت‌وگو کرده و او را «دوست خوب» خواند.
رئیس‌جمهوری آمریکا همچنین گفت حوثی‌های همسو با جمهوری اسلامی با دولت او تماس گرفته‌اند و اعلام کرده‌اند نمی‌خواهند آمریکا مستقیماً وارد درگیری شود.
او گفت: «آنها به‌مراتب ترجیح می‌دهند ما درگیر نباشیم و بیشتر شناورها را عبور می‌دهند. فقط یک کشور هست که از آن راضی نیستند و ترتیبش را می‌دهیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78345" target="_blank">📅 15:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=Bt4_PIrOvZQXQ8j5Ad0-dCqm1GsEzBA_bYvgsZGc0NZMOh1qxngPs9M8O2OMyYUhcB2eUysGW8PSqZkb7vJrzOja2aj_neF427pMyjFAHzlu3m2VAAdmdfsQjsdv83qYXRlUOFFvSxXaRE2dnmEjMuYvqXs-YiPUjPHhEGb_El9IQ_EVik-XlOnJCNuhI7mfDfC-iDmw6-Y9S_QXNNDLIuBNOiLyVVk2dovSAyZleBMJ0AHTyPvTkd5ggoaIiIPE9FVS4hmakNBy7uCFOax7P8EvFViK0ewGm3HMdCwg-jMy4e-74fgwkVlOPw2vgAiT7fHJPapVuOIDBf5-iIHkiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=Bt4_PIrOvZQXQ8j5Ad0-dCqm1GsEzBA_bYvgsZGc0NZMOh1qxngPs9M8O2OMyYUhcB2eUysGW8PSqZkb7vJrzOja2aj_neF427pMyjFAHzlu3m2VAAdmdfsQjsdv83qYXRlUOFFvSxXaRE2dnmEjMuYvqXs-YiPUjPHhEGb_El9IQ_EVik-XlOnJCNuhI7mfDfC-iDmw6-Y9S_QXNNDLIuBNOiLyVVk2dovSAyZleBMJ0AHTyPvTkd5ggoaIiIPE9FVS4hmakNBy7uCFOax7P8EvFViK0ewGm3HMdCwg-jMy4e-74fgwkVlOPw2vgAiT7fHJPapVuOIDBf5-iIHkiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای منتشرشده در رسانه‌های اجتماعی نشان‌دهنده ازدحام در خروجی مرز بازرگان است.
برخی گزارش‌ها دلیل اختلال در تردد از این گذرگاه مرزی را «محدودیت‌های ظرفیت پذیرش در سمت ترکیه» عنوان می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78344" target="_blank">📅 15:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78343">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUtsi3BgcIbgS26np-XfaWUz3W2PsXHlIxqdThNvYNZOENVTxYjyjImpofi2OXm5Tu14sYjkjpPD-kzHyuS_6HRL5FAfrfx9nHwlx26YBD0n_wl0EVjz38IiXjoumGxxMUcs5JjyHi5SS5nJHTQPSGpOZ8xyTuBkAEkZV3w57pb546pluEC8tt3akn02blsltD2YYmoC70F9MSgm5td-PW92EXX559tensDxN2LMlfWU1DZtY3TNOg4IoHOgOwxVFvyHFnYKPq58qAKwsRPqcWf5GOEpcOoI-94M6VIjpep774y6EYUZC6GfsKN-uPktv4W1aXf4cKD5kPzoQLFdoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون استاندار خوزستان اعلام کرد مرز چذابه نیز همچون شلمچه از بامداد امروز با اعلام مقام‌های عراق تا اطلاع ثانوی بسته شد. بنابر اعلام ولی‌الله حیاتی، هیچ تردد کالا و مسافری از این مرزها انجام نمی‌شود.
ساعتی پیش رویترز بع نقل از دو منبع امنیتی نوشت عراق پس از تازه‌ترین حملات پهپادی صورت‌گرفته به عربستان سعودی، دستور بستن گذرگاه مرزی شلمچه بین عراق و ایران را به عنوان یک اقدام احتیاطی صادر کرد.
مرز چذابه در استان میسان عراق قرار دارد و دفتر نخست‌وزیری عراق بامداد شنبه فرمانده عملیاتش را برکنار کرد. این برکناری پس از آن انجام شد که تحقیقات تأیید کرد آخرین حملات پهپادی به عربستان سعودی از خاک عراق انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78343" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V4gdpPt8t2YIRTOpdvZm3zx566MXLRuKR_oCYEzo3fDiK9P7m_V8-oW7YsRh5ZxVD80ELsXx78EBzuHRkztqWOP6dpJfDfwS1Ll8E1I9CRXrZstYjKsDsmA4vH1QAkZUQypneGjzC685wTd-SqC1_i_ToHaV5TzS4MoGe1B9azYNgEXOjfv1nnvOIWa3GEohzDu_b5-bMSge2aix0KPJhy72exa0YdTKTcUBpwuup0qIGfgtbYCN05ia8yWXDu3RiO5Zpakz_fnqWEaBrfymNhzUwJwYaqa8btlVKl3wy_IZNikef1RuudY-SGLGA2b6mA9YUAhmcbirCUXgEEj6rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fm2ZRfyUXW37wwVKhlbSVQlq2JH0ykZMlsYeV2FzGBw7lqQjfdWHOX1CtHREKyIpNwIW9fT-c5n0bFA51XMYvoRy7KJQP_VlM6eOTZ8NBBzv_Hs35L8fsbkxdwN_ax3ewn8jQq6MsXtS-gEnGG5NFJUnahBIdS9Irxmd_L_Q1tVC5lwTMHSp3q7madN-1a04-1hb4BwdghP5_Z78uJKzgpAM197r7vjtNcS2FgsCRpvGWbDoCJF1jzki2qjH0sOOSM2t_vum4TYtS70By5pTtyINu6K4YZ45ijPAiU6MB9mhF0VDTP42KHO9w3Unn0NuDn38OWBvbawwm7NAZ2im5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درگیری میان نیروهای نظامی و امنیتی جمهوری اسلامی و افراد مسلح در منطقه «بخشان» سراوان، پس از بیش از هفت ساعت همچنان ادامه دارد. «شیوار نیوز» از حمله به نیروهای حکومتی از دو محور، شکسته‌شدن بخشی از حلقه محاصره و خروج شماری از افراد مسلح از محدوده درگیری خبر داده است.
این درگیری حدود ساعت چهار بامداد شنبه ۲۱ شهریور ۱۴۰۵ و پس از محاصره یک خانه مسکونی آغاز شد. شبکه اسناد حقوق بشر بلوچستان پیش‌تر از استقرار گسترده نیروهای نظامی و امنیتی و استفاده از سلاح‌های سبک و سنگین در این منطقه خبر داده بود.
براساس اطلاعات منتشر شده از سوی شیوار نیوز، نیروهای نظامی و امنیتی پس از آغاز درگیری، محدوده حضور افراد مسلح را محاصره و مسیرهای منتهی به محل را مسدود کردند. بااین‌حال، در ادامه افرادی از خارج محدوده محاصره، نیروهای حکومتی را از دو محور هدف قرار دادند.
@
VahidHeadline
قرارگاه قدس نیروی زمینی سپاه پاسداران اعلام کرد در جریان درگیری با افراد مسلح در شهرستان سراوان در استان سیستان و بلوچستان، سه نفر از نیروهای سپاه کشته شده‌اند.
بر اساس اطلاعیه این قرارگاه، این سه نفر با عنوان «پاسداران گمنام امام زمان» معرفی شده‌اند.
قرارگاه قدس همچنین اعلام کرد که تا پیش از ظهر روز شنبه، چهار نفر از افراد مسلح ناشناس نیز در جریان این درگیری کشته شده‌اند.
این اطلاعیه جزئیات بیشتری درباره هویت افراد مسلح، گروه یا سازمان وابسته به آنها، محل دقیق درگیری و چگونگی آغاز درگیری منتشر نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78341" target="_blank">📅 15:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AqIJCohlpDOmz6r_wm0nBWc3cD-d-3Jb8lOB6IGX788h4_FqCioAnR_neWabdyBMPyqiA0n9Om7NQz1lJz4aj3JQfF9jPjCkz40O_oJnQo_-M0IEUw6EMrbLVY4GVlCCBR_JZlZEXRtnmf0tJOI1Ja2-kyiWzaJnRya2j_jVs-JFJNKtG-7AbmUqLEToyDNFM8vXls_HAbY8dMxNQTkszxFq4K1q1-u0TY4WrEclnfCns6fm30-7r0pvwb8SXIHY2VflyaEgP-ptEQU7Rn5R24idqvbGrSPGH7nDa7n9_ElN8PDIbZ2Z5ZuLfmN-Ug4Pzw6FW4JaWM3rkoqKjpHkyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سودا ابراهیمی شمس‌آبادی، بلاگر ۳۳ ساله اهل بندرعباس، که از ۹ فروردین در بازداشت به سر می‌برد، به اعدام محکوم شده است.
بر اساس این اطلاعات، شعبه سوم دادگاه انقلاب بندرعباس به ریاست قاضی خواجه‌حسنی، سودا ابراهیمی شمس‌آبادی را با اتهام‌هایی از جمله «توهین به رهبری»، «فعالیت رسانه‌ای و تبلیغی برخلاف امنیت ملی»، «اقدام اطلاعاتی و امنیتی به نفع دولت‌های متخاصم» و «عکسبرداری و ارسال تصاویر برای رسانه‌های فارسی‌زبان خارج از کشور» به اعدام محکوم کرده است.
دادگاه همچنین او را به دو تا پنج سال حبس، محرومیت از برخی خدمات دولتی و مصادره اموال محکوم کرده است.
حکم اعدام سودا ابراهیمی شمس‌آبادی روز اول شهریور به وکیل او ابلاغ شده است.
بر اساس اطلاعات رسیده، ابراهیمی شمس‌آبادی در جریان دوران بازداشت، به مدت ۲۰ روز در سلول انفرادی نگهداری شده و در دوران بازجویی تحت فشار شدید قرار داشته است. خانواده او در این مدت از محل نگهداری و وضعیتش اطلاعی نداشتند.
قاضی خواجه‌حسنی که این حکم را صادر کرده پیشتر در سال ۱۴۰۲ از سوی مقام‌های قوه قضاییه در زمینه‌هایی از جمله صدور بیشترین احکام و جدیت در انجام کار مورد تقدیر به عنوان قاضی نمونه قرار گرفته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78340" target="_blank">📅 15:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78337">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UxSC6kMJpGp_AUyOzbb8F_1DVzRJ6JP4rVnv5f1MEv4iNgBy6tdjfQzeJHhqlKaXHKsxdRDUCm4AanNcf3NwaSGOPLw8W_cbAjJK_8SgcIk07IFCpM4s__a8qvvykf3WkxbK21WQspUCctkHCOE5NSoh2jgSvZcJ2efWjeOetcndJGI7G73EWlsfpCfTZbtLr1gkH3_2T8VM_y3Xu3YrtwklJUTcrfZhtZqYvocn_KII-aVg7kQPeSBD3S4goCPznLRjGDlOVf3Lj6aJVXQZ3w08FSQYIlhWAazWVvmsnC-IkvTZgrGKwVb92XcJumWywSjmKQw1-1WKW7K8STQMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q647DV7W0jONfWZCfQQ41C1ZoByPuwORNR3hZEkwr1UWJntoiCyE479B5cn3Q43qaEQVICJ92mtrnELIPX30u9u5Sm2YSjlEFTyET4UyQv9N6S0kVxZCvH0lg2t6oHCPEyQB1nVL6OohbqK2KUF-gqqNIaHfLU18wx50Z4HvakGD6HBTSezscN1vIskizyectts_UDSZj_1ahsxYaBL9gQ1JpPCYkr8ZTp_iEx_AZIsyrVX3rHgCO80iolZkmIBOhpyqqhM21vCLu0e1MYxbQ_iCf1iAjbopaCvBOEfWfwrflehaiCDO-udzj4oc-uR7HTHOe927HiKQU1PPGPx29g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X7FnYHNgDYfqtZiFHHs3JnJIS0hSmNCizo57Cw9y31L6QR61KTf3ZGmBw38t9vyIfO6BpepBUROEEiKP-qGvDAdXQlsHipQPPtL9M24cmhmtbevjCh6HFE_dKM00Z-WyCMTEHlD9mtsqX3fScMDVf9Hh3dzDJQyZqqRh95gqB1x_3f0mbEDNcuk-SOnQZWY6ZaKXBuELaa6b4Kr9QslfKvL55dx05Iim2J4iygGwgrmzo2aFQTOeYhmgGwIF_BGxy9ydcFUuxWrjaX7tlVPB-roFRyDYuOlg_DSu6EdSWxhWm3w7ArZi58YwHbOYSCs4RPY_BJMuEjw1k61ztbjsOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت انرژی عربستان سعودی روز جمعه ۲۰ شهریور با انتشار بیانیه‌ای اعلام کرد که خط لوله انتقال نفت «شرق-غرب» (واقع در مناطق ریاض و مدینه) صبح پنجشنبه هدف چندین حمله قرار گرفته است.
در این بیانیه آمده است که به دنبال این حملات، عملیات انتقال نفت در خط لوله مذکور به صورت احتیاطی متوقف شد.
این رویداد همچنین منجر به مصدومیت تعدادی از افراد شد که خدمات درمانی و مراقبت‌های پزشکی لازم به آن‌ها ارائه گردید.
@
VahidOOnLine
وزارت خارجه عربستان سعودی اعلام کرد خط لوله نفتی شرق به غرب این کشور با پهپادهایی که از عراق پرتاب شده بودند، هدف حمله قرار گرفت.
وزارت خارجه عربستان سعودی افزود بنا به درخواست نخست‌وزیر عراق، در این مرحله تصمیم گرفته است اقدام تلافی‌جویانه انجام ندهد.
@
VahidOOnLine
خبرگزاری رویترز گزارش کرده که بغداد دستور تعطیلی گذرگاه مرزی شلمچه میان عراق و ایران را صادر کرده است.
دو منبع امنیتی عراقی به این خبرگزاری اعلام کردند که عراق این گذرگاه را به عنوان اقدامی احتیاطی و در پی حمله پهپادی از مبدأ عراق به خط لوله نفت شرق-غرب عربستان سعودی، بسته است.
گذرگاه مرزی شلمچه یکی از مسیرهای زمینی اصلی میان ایران و عراق است.
براساس گزارش‌ها پهپاد شلیک شده به عربستان از استان میسان عراق شلیک شده است. این استان در قسمت جنوب شرقی عراق و هم مرز با ایران است که مرکز اداری آن شهر عماره است.
@
VahidHeadline
رویترز نوشت: به گفته این دو منبع، عملیاتی گسترده برای تعقیب و پیگرد عاملان این حمله به عربستان در جریان است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/78337" target="_blank">📅 05:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78336" target="_blank">📅 22:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVwiya7ThjkPzGinul50zDbTwzBS-u5U7qMTEvfxTY7jLzsbuXeFx2KAqUThcG4MNec2L0DZVOEiEnZfE6VeFXiBsQWCOBeXc_-lo6Z-kxQ3RnESTPKPrZ7esvnxyI8R91gYcxqKD1CHd8lYK1HwtF6nGkWfsO1b8lBr25vgyk8KufjArFfyQUgC-DPDwu5brx010If7hrKlEkKLG-V2ROAcyXeQHk4nXMgl9XAZCpgP2pYugP5m9viYpXpsPJdvlAXAM18OFugwiTPHqr_1r9oH7EUGoP19MN_ICpzlEXAwZUqaHIUkWssg-ao31QsHhQJgY-Rq_OR5cZZ9XNfbrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس دولت چهاردهم جمهوری اسلامی که به هند سفر کرده است روز جمعه ۲۰شهریور۱۴۰۵ در پایتخت این کشور اذعان کرد که فشارهای آمریکا بر ایران به مرحله «دشوار و خطرناک» رسیده است.
او با اشاره به این که جهان امروز در یکی از «پیچیده‌ترین مقاطع خود» است، خواستار «همکاری عملیاتی» کشورهای عضو بریکس شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78335" target="_blank">📅 20:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=EAidLjb15PirmkDZo81HHiWcB-5CMeaz1zFJ654y6up05zLK44gpygH6GwjyvwfFwxk9NJAlcfu29lgUPu-jM2u7g6B6ySM2uifkayrH8PPWEpF4hQY2954ei8buWAECpgCG1O4NZOUNY5Gf3n1gypVbA2w3aG_MkUYqbpbKK62CBnRfUR9Wp2MOGFodhCTygw25bXnwAA0yhI5z3-F01xOZuQLDxriJWVa2kqa84H-AjrYCbeuo-pH5KYNpI0TRxqYrKwOeTB353VDw2KbzxPwgsGUgKxdDaOD0TkReBuBP07fAKe8tWjv2nR51ytvD-pkMoiqmEI_EOlY5IO6Ocg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=EAidLjb15PirmkDZo81HHiWcB-5CMeaz1zFJ654y6up05zLK44gpygH6GwjyvwfFwxk9NJAlcfu29lgUPu-jM2u7g6B6ySM2uifkayrH8PPWEpF4hQY2954ei8buWAECpgCG1O4NZOUNY5Gf3n1gypVbA2w3aG_MkUYqbpbKK62CBnRfUR9Wp2MOGFodhCTygw25bXnwAA0yhI5z3-F01xOZuQLDxriJWVa2kqa84H-AjrYCbeuo-pH5KYNpI0TRxqYrKwOeTB353VDw2KbzxPwgsGUgKxdDaOD0TkReBuBP07fAKe8tWjv2nR51ytvD-pkMoiqmEI_EOlY5IO6Ocg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواهر امیرمحمد شاه‌کرمی با انتشار ویدیویی در صفحه اینستاگرام خود، از حضورش در مکانی خبر داد که به گفته او، برادرش آخرین لحظات حضورش در آنجا را پیش از بازداشت سپری کرده بود.
او در توضیح این ویدیو نوشت: «۱۸ شهریور، برگشتم به همان خیابانی که آخرین نگاه‌های برادرم آنجا بود؛ تا صدایش را از همان‌جا دوباره بلند کنم. این‌بار ایستادم برای صدا زدن نام امیرمحمد شاه‌کرمی.»
در این ویدیو، خواهر امیرمحمد با در دست داشتن تصویری از برادرش، نام او را در همان خیابان فریاد می‌زند.
امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، در ۱۸ دی‌ماه در شهر قدس بازداشت شد و پیکر او حدود ۶۰ روز بعد به خانواده‌اش تحویل داده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78334" target="_blank">📅 17:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957af9390d.mp4?token=B2mA7P0vgJ8K573RqdP6zaYNS3ZtNwtU3kpO3DNURK3lr_i8AdW-cAQ5tHRNrR-yUcC1r8rsRNzmNhc8rHzonexA7zrjR3GCYeYskIqc1IEC86c2NZfhdcVaWMbsiR9bA0NMCrkkRjbZr-Oi44qCDyBpDf24Az3cjvDdLSTzpaHOYFPIJo0KL7eLfxWZXN6fM6Yb81SQEVwjvop8HmyBLIBTZqgdIdqvL5h5JYlK_pHp297bnTRc9u_Bz76xn4kVAy_1pVGsEz_Ly3EYHqFFGFt__50tFxIrVllxISdXQdiod2SUq2mRID5M_mpsG4L5AieiunbRDAhXCZg6kTUo4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957af9390d.mp4?token=B2mA7P0vgJ8K573RqdP6zaYNS3ZtNwtU3kpO3DNURK3lr_i8AdW-cAQ5tHRNrR-yUcC1r8rsRNzmNhc8rHzonexA7zrjR3GCYeYskIqc1IEC86c2NZfhdcVaWMbsiR9bA0NMCrkkRjbZr-Oi44qCDyBpDf24Az3cjvDdLSTzpaHOYFPIJo0KL7eLfxWZXN6fM6Yb81SQEVwjvop8HmyBLIBTZqgdIdqvL5h5JYlK_pHp297bnTRc9u_Bz76xn4kVAy_1pVGsEz_Ly3EYHqFFGFt__50tFxIrVllxISdXQdiod2SUq2mRID5M_mpsG4L5AieiunbRDAhXCZg6kTUo4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تسلیحات کشف‌شده در علی الطاهر را ایران برای حزب‌الله فرستاده بود
نخست‌وزیر اسرائیل روز جمعه ۲۰ شهریور اعلام کرد نیروهای اسرائیلی در جریان عملیات در ارتفاعات علی الطاهر در جنوب لبنان، مقادیر زیادی تسلیحات را از زیرساخت‌های حزب‌الله خارج کرده‌اند.
بنیامین نتانیاهو با اشاره به تسلیحات کشف‌شده گفت: «مقادیر بسیار زیادی سلاح از آنجا خارج کردیم که سال‌ها توسط ایران سازماندهی و تامین مالی شده بود.»
ارتش اسرائیل پیشتر با انتشار ویدیویی اعلام کرده بود، نیروهایش پس از به دست گرفتن کنترل عملیاتی ارتفاعات علی الطاهر، زیرساخت‌های زیرزمینی و روی زمین را منهدم کرده‌اند. به گفته ارتش اسرائیل، این شبکه بیش از دو کیلومتر امتداد داشت و شامل ده‌ها راکت، موشک و پهپاد و همچنین موشک‌های ضدتانک، مین و مواد منفجره بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78333" target="_blank">📅 17:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toX9ZjRMop4G2esyZkdbMW9iC_ZzKkRzqia85P415WupIkIjkahLkyLg52XWbtHrnYGlKBzZFQIBqEtdlYz_2TrvgA7jXsmH1fleMrlzAvlOnnmKHEoqwONnC4US12KWVhnzn847pGQBKJpENQ-qFLP9qaaUGyBf-2BXuuxGeUSFguJAcxXT08Wd4DzMizCOU9R9UHxeEb3TU-P3kCrQIAM4Wb4oulECJkhpjFQwW2Bj1Fz_iiO0n0WYqLfkbJ-0nzhUA8fDvhOsHzBUwq4O1eWgmLY7UziBdwSZ4RNqbw3BGbKSzkOpdcRulr1v3xHkD5H09z5BMIB0CMfCVaX57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، گزارش‌های رسانه‌ای مبنی بر آسیب‌دیدن هواپیماهای آمریکایی در جریان حملات موشکی اخیر جمهوری اسلامی به اردن را رد کرد.
او پنج‌شنبه ۱۹ شهریور در مصاحبه با شبکه نیوزنیشن، در پاسخ به سؤالی درباره این گزارش‌ها، گفت: «نه. هیچ خسارتی وارد نشده است. هیچ اتفاقی نیفتاده است.»
کمی قبل از اظهارات ترامپ، شبکه خبری فاکس به نقل از یک مقام ارشد آمریکایی نوشته بود که موشک‌های بالستیک ایرانی در جریان حمله گسترده موشکی سه‌شنبه، ۱۷ شهریور، به هواپیماهای جنگی آمریکا مستقر در اردن، آسیب زده‌اند.
فاکس‌نیوز این خبر را به گزارش جنیفر گریفین، خبرنگار ارشد خود منتشر کرده است.
شبکۀ خبری سی‌بی‌اِس برای نخستین‌بار این موضوع را منتشر کرده بود که در جریان حملات موشکی ایران به پایگاه نیروهای آمریکایی در اردن، «چندین هواپیمای نظامی ایالات متحده، آسیب دیده‌اند».
ارتش اردن روز چهارشنبه ۱۸ شهریورماه با صدور بیانیه‌ای گفته بود که ایران در طول شب قبل، ۲۰ موشک بالستیک به سمت اردن شلیک کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78332" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78331">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ESoNtvdULjZarpM9PYY_BCUIWhIYOiR8KzUrQzYcCiDsnaacnUm4GM_Pec2wZuuK4z-lbEG-IfQBW6anFeCV-iTsLlvIfoh3uCQzLnYYVqmwtXaT7cBFisAgun-YC_7xtlGDdjZdyqY8_XISakrU_S7QrXvT0-RV6bu__czk7zqHpiUkaT2iZLWZVHf6kWRsjsteOws-7aSz4l2LRonIK4b4AK0Y_SbyUA-mi7JuFX3JgJgPztRm5Sq4bnwtpeRG7h2kjQjPWO5iqUHUjQ1jK19nnU8ydkX-4VHhxw-s3hmJeXLtWEy-g8dzm5sFZUtGHuP3RoGHSD7JhK1tSxD0oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت آمریکایی «آنتروپیک» اعلام کرده است که سه عملیات مرتبط با حکومت ایران را شناسایی و مختل کرده که در آن‌ها از مدل هوش مصنوعی «کلود» برای تولید و انتشار محتوای تبلیغاتی، طراحی سامانه‌های نظارتی و تهیه اطلاعات مرتبط با هدف‌گیری نیروهای دریایی آمریکا استفاده شده است.
این شرکت روز پنج‌شنبه ۱۹ شهریور در تازه‌ترین گزارش اطلاعات تهدید خود، مجموعه‌ای از موارد سوءاستفاده از مدل‌های هوش مصنوعی آنتروپیک را تشریح کرد. این گزارش فعالیت‌های شناسایی‌شده و مختل‌شده از دسامبر ۲۰۲۵ تا اوت ۲۰۲۶ را پوشش می‌دهد و علاوه بر ایران، مواردی مرتبط با چین، روسیه و کشورهای دیگر را نیز بررسی کرده است.
بر اساس این گزارش، آنتروپیک حساب‌هایی را شناسایی و مسدود کرده که از «کلود» برای اجرای عملیات نفوذ با هدف تاثیرگذاری بر افکار عمومی استفاده می‌کردند. سه مورد از این عملیات به عوامل همسو با حکومت جمهوری اسلامی مرتبط بوده است.
آنتروپیک می‌گوید هر یک از این عملیات از سوی فرد یا مجموعه‌ای انجام شده که یا مستقیما در یک نهاد تبلیغاتی حکومتی ایران فعالیت داشته یا به نمایندگی از چنین نهادی کار می‌کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78331" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQDxacv4z_-g9_VqKhieqOMLFj_vmfp-e6_k90Ylmgi5teefmPZuTjFrlNB2t2dzgjkduQexV1zHrYMReCZUVQSCgfxDXTHfQhE69YFPZGqnq-Ej6WmQ41anUbe7pEartZrkxwTA2MG8kMX0ZfEDY27PypkT0x-C5EOFStNCMTV0VQSfWlx8yKKuA-LGCUqFOTHnzr8I9gM-uS4OxLyqOeEdzvCPPpmpGYYJRbMyrY_mJ1V7m2HAm_B530dGq39eYbcq-5H_cFgbSENBgFl8b060YEZDuTAbb2GB_7ilMcpgJhmass-bZiyEVuZ5KnkAkjAic6lIaP2Nt8N3bpaKyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت مخابرات ایران با انتشار اطلاعیه‌ای در سامانه کدال (سامانه اطلاعات جامع شرکت‌های پذیرفته شده فهرست شده در بورس) اعلام کرد هزینه مکالمه تلفن ثابت با تلفن‌های همراه از روز جمعه ۲۰ شهریور ۴۵ درصد افزایش می‌یابد.
به گزارش انتخاب، بر اساس این اطلاعیه، سقف هزینه مکالمه تلفن ثابت با تلفن همراه از ۶۲۵ ریال به ۹۰۶ ریال افزایش یافته است. این تغییر در پی ابلاغ دستورالعمل افزایش هزینه تماس تلفن ثابت با تلفن همراه، تماس میان تلفن‌های همراه و پیامک اعمال می‌شود.
شرکت مخابرات ایران اعلام کرد میزان دقیق تاثیر این افزایش بر درآمد شرکت هنوز مشخص نیست و آثار مالی آن در گزارش‌های دوره‌ای منتشر خواهد شد.
این شرکت در خردادماه نیز هزینه ثابت ماهانه تلفن ثابت را ۴۵ درصد افزایش داده بود. هزینه ثابت ماهانه مشترکان خانگی در تهران و کلان‌شهرها به ۴۳ هزار و ۵۰۰ تومان، در مراکز استان‌ها به ۳۲ هزار و ۶۲۵ تومان و در سایر شهرها به ۲۴ هزار و ۶۵۰ تومان رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78330" target="_blank">📅 17:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=r_OBzgQ4zm33_YBI0VFhUTFvDHH1_1Gx2cyD1UF2mEFW_3wbd1m4NCQEqS9uImq_B4ykduNJwzgC22E1kOWq-lnOvFDrSnD8l96I9424e9p1HvEHQaJe8qc5YGQKnPk67G2sxGIlSLCiR4zn1geoRdCa7FGLBWTsiJy_NZcUaSjxY0e6izK16TUCRnvAnEMHhnRIhp_TQFPPo6YeprmA3kfDbnv_WFaP42aPJ2Tw8YEcWktVAcrdu1Gt0J2Sz2VO8LmvN3snhG1vbQsA8sGvG4BLvlH586wnhVRXC9UNgmtkGz_okSX8xtxtv7XKD0GG8yzKQunXHgGJVKYyhxEqnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=r_OBzgQ4zm33_YBI0VFhUTFvDHH1_1Gx2cyD1UF2mEFW_3wbd1m4NCQEqS9uImq_B4ykduNJwzgC22E1kOWq-lnOvFDrSnD8l96I9424e9p1HvEHQaJe8qc5YGQKnPk67G2sxGIlSLCiR4zn1geoRdCa7FGLBWTsiJy_NZcUaSjxY0e6izK16TUCRnvAnEMHhnRIhp_TQFPPo6YeprmA3kfDbnv_WFaP42aPJ2Tw8YEcWktVAcrdu1Gt0J2Sz2VO8LmvN3snhG1vbQsA8sGvG4BLvlH586wnhVRXC9UNgmtkGz_okSX8xtxtv7XKD0GG8yzKQunXHgGJVKYyhxEqnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی زارعی دوز دره سی، زندانی سیاسی و یکی از آسیب دیدگان اعتراضات سراسری ۱۴۰۱ که در زندان قزلحصار کرج محبوس است، توسط شعبه ۲۳ دادگاه انقلاب تهران از بابت اتهام «افساد فی‌الارض» به اعدام محکوم شده است.  بر اساس اطلاعات دریافتی هرانا، حکم اعدام آقای زارعی دوزدره‌سی…</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78329" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78328">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78328" target="_blank">📅 07:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okBWXGEPyTG0LlQwfyrrJNovSdIG5dQzzMBhx_W0HEkJHK2sOLvUtXGzpInmkKJKRVABddfGqlhQGt6DafVK1GV_z5ESQMKx01PbQmVAmCpX5PVRffVWZfuriNhOYP00LzqZ5JgwBvVOY4UgIfMzfQXS_yLrUhO17phKO6XIrpq6SuoEHJa1Z8Ex7hvLRxtpf_cUR-rdObxVBxd1B-ZKNZvs1QacygvY2MF0T3TUkLSR1_mlzst2G7T9luTH82XVZrn6HDPmCUfw3HQ85r6we8Ut0RDb-O-gHZCQDZmq6IlpdfNEHwTRI8CFDattgO_41vJlzYFmPRC1etzzzPPpLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا در دومین شب گردهمایی انتخاباتی میان‌دوره‌ای جمهوری‌خواهان که در دالاس در حال برگزاری است، بار دیگر، تنگه هرمز را «تنگه ترامپ» خواند و گفت «ما تنگه ترامپ را کنترل می‌کنیم». رئیس‌جمهوری آمریکا بار دیگر تاکید کرد که هرگز نمی‌توانیم به ایران اجازه دهیم سلاح هسته ای داشته باشد و نخواهد داشت. او گفت که ایران در حال عقب‌نشینی از همه جا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78327" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8pZ5c4fpPj_ooI0xL2jDCmNdqQwH_KAbJfaV3OUqCRIgmv2Xkm9fdut1akYAv8QnpPVbp-shDh31GE6kYGr_7rEJnURiq1VX-kDHryUzH-LsdGwW5DAo_VxRvo28JDABTP7Sr7qOL0v_IXTNTmM_oOtTmEeysVm8Wa9r--ZhRIm2iIMFC8M-dAz7BeJySZ34cRrJISSeffbrnqjrnCJHu7u12fVAcLkA8HuroRcYUOD-TQtWPStOvtuTN4Flg7yqZiD6Xwa5v6McOD6jZFyN8AnjOJbyZfLrnWHJPLYXM4zec9V53O9_-WDbm30WPyuTl8EE60jqc9_c5fKgK5LFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هانگ کائو، سرپرست وزارت نیروی دریایی آمریکا، به اپک تایمز گفت نیروهای جمهوری اسلامی خسارت گسترده‌ای به پایگاه پشتیبانی نیروی دریایی آمریکا در بحرین، محل استقرار ناوگان پنجم این کشور، وارد کرده‌اند.
کائو در توضیح استقرار اخیر ناو هواپیمابر یواس‌اس آبراهام لینکلن و الزامات لجستیکی عملیات طولانی‌مدت گفت خسارت واردشده به پایگاه بحرین بر امکان پشتیبانی از این ناو تاثیر گذاشته است.
او گفت: «خدمه این ناو جایی برای پهلو گرفتن نداشتند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78326" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYToeV2TbG1dklPvRtoXnmSeGDgQC-uFJ46ZnaUNJBmx18zuXN5DbCB6xI7dm_X-Uqswlit7OhkNtgLa5hbosW_Oef2i145fXxP_0vVf3bK8su_KCaxxG9V2TSyNwV8Dqj9E2iiO_xwPFOL9exNqYh_NLi9ZNUBOma6Z0ujvdiHu6bK_HFVOfk4QxVwJ-qCvHLkMCEamfKkSB3ipybRnnY4hAEpMpxdBkHrxsKR4uRbMA0IFZHlhY7N0MyIVebLGmfMI9dpWJL6BReXJ6SZeu87Su0p2DkhjDp2OBmTJKWJ4456LUEBc7q9XbrWkMZbrdWDZKMwZ05qD7UFGhOidZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت پنج‌شنبه ۱۹ شهریور هم‌زمان با تشدید درگیری‌ها در منطقه و افزایش نگرانی‌ها درباره اختلال در عرضه انرژی، بیش از شش درصد جهش کرد و نفت برنت به ۱۰۷ دلار و ۶۳ سنت در هر بشکه رسید. نفت خام وست تگزاس اینترمدیت نیز از مرز ۱۰۰ دلار عبور کرد.
بر اساس داده‌های اویل‌پرایس، قیمت نفت موربان با بیش از پنج درصد افزایش به ۱۲۲ دلار و ۴۸ سنت رسید و سبد نفتی اوپک نیز با بیش از چهار درصد افزایش، ۱۱۲ دلار و ۲۵ سنت قیمت‌گذاری شد.
افزایش قیمت‌ها پس از حملات به نفتکش‌ها در خلیج فارس و دریای عمان و پیشروی حوثی‌ها در سواحل دریای سرخ رخ داد. رویترز گزارش داد تصرف بندر مخا و پیشروی حوثی‌ها به سوی جزایر حنیش، نگرانی‌ها درباره امنیت تنگه باب‌المندب و مسیر صادرات نفت عربستان سعودی را افزایش داده است.
هم‌زمان، تردد کشتی‌ها از تنگه هرمز به‌شدت کاهش یافته و داده‌های اولیه نشان می‌دهد ۱۸ شهریور تنها هفت کشتی از این آبراه عبور کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78325" target="_blank">📅 03:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=g0I6Ne4DPc_UJF-U8hfCmBZ1gECmPcg8TEZEeUlnE7Eipj2BEll8STFK72njv-riiFGvpjgawyTny6v1yOzUVQJZbfOb-spJuXYBg2EgNnxEgT1hVdKqBHWb8AzFb6XplH1-yCWjBgCGPPtxuZpY4coU2K9ZJ2jzt0vJhx4fq3ENNEa_AZwCz5KgnqpfZeDSFH5v4I96ZcywIbwgLozO6lR-WvwlcsqQPqLe670KxHjbw_0U1GViUvE3TUXMx41hLX1oYs2w-v-NAHMZccScWqAJoOG3hpgj5iSRMdi1BxEstTE7e4rmA0OTAtTt5IHtpgy-D5IW0R9mtGlPSS47ow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=g0I6Ne4DPc_UJF-U8hfCmBZ1gECmPcg8TEZEeUlnE7Eipj2BEll8STFK72njv-riiFGvpjgawyTny6v1yOzUVQJZbfOb-spJuXYBg2EgNnxEgT1hVdKqBHWb8AzFb6XplH1-yCWjBgCGPPtxuZpY4coU2K9ZJ2jzt0vJhx4fq3ENNEa_AZwCz5KgnqpfZeDSFH5v4I96ZcywIbwgLozO6lR-WvwlcsqQPqLe670KxHjbw_0U1GViUvE3TUXMx41hLX1oYs2w-v-NAHMZccScWqAJoOG3hpgj5iSRMdi1BxEstTE7e4rmA0OTAtTt5IHtpgy-D5IW0R9mtGlPSS47ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار ویدیویی در شبکه اجتماعی ایکس نوشت
:
امشب بزرگ‌ترین پایگاه ایران در خارج از ایران، یعنی تونل‌های علی‌الطاهر در لبنان را نابود کردیم. در حال تکمیل مأموریت هستیم. سال نو مبارک!
پیش‌تر ارتش اسرائیل اعلام کرد شبکه تونلی حزب‌الله در ارتفاعات علی‌الطاهر را با استفاده از بیش از هزار و ۱۰۰ تن مواد منفجره تخریب کرده است.
به گفته ارتش، در این تونل‌ها که طول آن‌ها بیش از دو کیلومتر اعلام شده، ده‌ها موشک، راکت، پهپاد، سلاح‌های سبک، موشک‌های ضدزره، صدها مین و مقادیر زیادی مواد منفجره کشف شده است.
بر اساس اعلام ارتش اسرائیل، با انهدام این سایت، عملیات تخریب شبکه‌ای متشکل از هشت تونل به طول مجموع ۵٫۴ کیلومتر در منطقه علی‌الطاهر و قلعه شقیف تکمیل شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78324" target="_blank">📅 01:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78323">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oh2vJE_vU8Dz0uux-dVdi_LjRT4uRmbDOf0mWYdjQ3cBmv0g7n8lo6zfhNMsL6axQ8BiSZ0hVybNvF9dhh3lNkcAb6-cGn_gW_Gv_YeqkG-2EgxJ3MFJbgKpsBifhejCNCaKfGYPKgxOCRFx7cW0VkYYGBlR0BPTe5ZGRSlPBf51B-dI5MkuvQB-gwvW1w7P_IXjm3a6oDktQF7vJIKnbbhsbWlLcHDvZuNP1M6je9a5QvFfOs3I0FD9hVkCtCwvxfogv1fbMkPTbRZJwz38naEz4AKTaGEeFc5kKpLIUUu9L7v-4tJkXmtG_MwrBbOFdc7wr4UYA7uTdPEqab0Y3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا، یوکی‌ام‌تی‌او، عصر پنج‌شنبه به وقت واشنگتن از برخورد چند «پرتابه» به دو شناور در نزدیکی سواحل عمان خبر داد.
بر اساس این گزارش، این برخوردها در فاصله چهار مایل دریایی غرب شهر خصب، در استان مسندم عمان، روی داده است.
طبق این گزارش، کاپیتان یک شناور اعلام کرد که شاهد آن بود که چهار پرتابه نامشخص به دو شناور نامشخص اصابت کردند.
در پی این اصابت‌ها، یکی از شناورها دچار آتش‌سوزی شد و از وضعیت شناور دوم اطلاعی در دست نیست.
مقامات عمانی در حال بررسی این واقعه هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78323" target="_blank">📅 01:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78322">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=tea7PDs_-Nrp04-cE4a386N3XWpIalpe8UP9nrPa-qESUqWBWA29jG396wNW-5M0ZMQHsUXvNrIgxuGpX1Uw2AfPLQbp-J-5jNP30_9KNiRpyvKuL8j9wDNyz2lEjtA53ooPo0A_jyBOkYQeEiWoJh_J2xMdoEawb9wZvD6X1oBE-8TTVzSdNf9iWh-j1yI5BiqQhz0MvpeY2dxHvMNOuM3-JQmrX8cHYE6OkivIMk9NMKY9Py43IpFlljX1gHUdUvxZ2G1w_WwoQPBZp9VCrUnzy0FiybmMidJR5-_5tORiT-d6cbReyv0jRlT8FdECuR5Qbn4AyfJ0FwS60N0z0w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=tea7PDs_-Nrp04-cE4a386N3XWpIalpe8UP9nrPa-qESUqWBWA29jG396wNW-5M0ZMQHsUXvNrIgxuGpX1Uw2AfPLQbp-J-5jNP30_9KNiRpyvKuL8j9wDNyz2lEjtA53ooPo0A_jyBOkYQeEiWoJh_J2xMdoEawb9wZvD6X1oBE-8TTVzSdNf9iWh-j1yI5BiqQhz0MvpeY2dxHvMNOuM3-JQmrX8cHYE6OkivIMk9NMKY9Py43IpFlljX1gHUdUvxZ2G1w_WwoQPBZp9VCrUnzy0FiybmMidJR5-_5tORiT-d6cbReyv0jRlT8FdECuR5Qbn4AyfJ0FwS60N0z0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران روز پنجشنبه ۱۹ شهریورماه تصاویری منتشر کرد که به گفته این نیرو، هدف قرار دادن یک شناور بدون‌سرنشین آمریکایی در ورودی تنگه هرمز را نشان می‌دهد. سپاه اعلام کرد این شناور با شماره بدنه ۵۸۳۸ و از نوع «سیل‌درون» بوده است.
علی عظمایی، فرمانده نیروی دریایی سپاه پاسداران، گفت این شناور بدون‌سرنشین «جاسوسی» متعلق به ارتش آمریکا در تنگه هرمز مورد اصابت قرار گرفته است. او همچنین گفت: «تنگه هرمز مسدود و تحت اشراف اطلاعاتی و کنترل هوشمند ماست و هرگونه تحرک خصمانه مورد هدف قرار می‌گیرد.»
نیروی دریایی سپاه در بیانیه‌ای اعلام کرد ارتش آمریکا طی روزهای گذشته شناورهای بدون‌سرنشین خود را به تنگه هرمز اعزام کرده است. مقام‌های آمریکایی تاکنون درباره این گزارش اظهارنظری نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78322" target="_blank">📅 22:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q9QAQSPHzRkPGzBK5hiYPLcwU3xbDZXMkJe3tPGcYIgdQG5tVAGnpjxgxQch656FBw9VURAUnsuOkXuHeUZl0spJiMyg_XI9apvFyCQ1ijvdod-TNWHrpfSgej_s2Y-U4nOxOhPgi1iYT0v0uKQuzl16FolvODNNd4lehA80PYXu-tsXsR4C_too6n5TO0gDE7FL9I2Ztnmg-Z7gslrRCEG9KBMk1Zlaw2oHQ8ypg-5TgQBYyKlvc_CwlHtdVvugfSJfB053M5lNcp9gMG9Aj46tA5vnEDOvSFlj8A_kejXGQ21rJdeTdtlqFUVbkI3J-eofp2wmn2JS-XMQmOlzjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، روز پنجشنبه ۱۹ شهریور در گفتگو با بلومبرگ اعلام کرد این سازمان بر اساس تصاویر ماهواره‌ای، شاهد تحرکات ساخت‌وساز در سایت بسیار مستحکم «کوه کلنگ‌گزلا» (Pickaxe Mountain) در جنوب مجتمع اصلی غنی‌سازی ایران بوده است.
گروسی با اشاره به اینکه بازرسان آژانس هنوز موفق به بازرسی از داخل این تونل‌های عمیق نشده‌اند، گفت: «نشانه زنده از تحرکات در اطراف این سایت ساخت‌وساز وجود دارد، اما اطلاعات دقیقی از فعالیت‌های درون آن در دست نیست.» او یادآور شد که ایران پیش‌تر قصد خود را برای انتقال تجهیزات به زیر کوه جهت «مصون‌سازی در برابر حملات» اعلام کرده بود.
این اظهارات در پی ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل مطرح می‌شود. بر اساس گزارش‌ها، آژانس از ژوئن ۲۰۲۵ و پس از حملات نظامی آمریکا و اسرائیل به تاسیسات هسته‌ای ایران، امکان راستی‌آزمایی وضعیت ذخایر اورانیوم با غنای بالا را نداشته است.
دونالد ترامپ، رئیس‌جمهوری آمریکا، بار دیگر با اشاره به این سایت زیرزمینی، نسبت به هرگونه اقدام ایران هشدار داد و در یک تجمع انتخاباتی گفت: «ما متوجه فعالیت‌های مختصری در کوه کلنگ شده‌ایم. به ایران توصیه می‌کنم دست از پا خطا نکند، چرا که مجبور خواهیم شد ضربه بسیار سختی به آن‌ها وارد کنیم.»
از سوی دیگر، سی‌ان‌ان روز گذشته به نقل از منابع خود گزارش داد که ایالات متحده در حال توسعه سلاحی با نفوذ بیشتر با قابلیت تخریب اهدافی در زمین‌های سخت مانند کوه کلنگ‌گزلا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78321" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78320">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grBjbrcISQvo9bISsS-SmmDBCeoO-kBkUiWJlMU1xqvTX4_vxZe5hK6rLksnAiKK51N8RbW_5vin9CjlC9o-VJ6-E2JOBBRFnakDpiqdLfw9j7Cm9a2Ob7n9s-iTrUYaYCzbAu03cPRZhBL0dd5tmIDZPf6tjuLUaqESAl0g1z_zPsYNleBLQBlL8VCuzBk_3xOlYjJjx0XKPCvZKNH_DQE26MRmZFcFMK5RFSM_XMnECejGoZIZxhlawk3ZGx6O1MO4bMSaNnvFAQOg72Yp_yWA7VO8BwpY6DrDYtkXowADQgSEIO0McIyHAY4k123NhbQSY7Bjrr5_1zrazwo4xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه قبل ماموران امنیتی به منزل خانواده «کیاوش میرقاسمی» از کشته‌شدگان اعتراضات دی‌ماه۱۴۰۴ یورش برده و «سمانه عصاران» مادر او را بازداشت کردند.
به‌‌دنبال تشدید فشارها بر خانواده میرقاسمی حالا صفحه اینستاگرامی مادر او از دسترس خارج و کنترل آن به اجبار به دست نهادهای امنیتی افتاده است.
تمامی پست‌های پیشین این صفحه حذف شده و تنها یک پست به دستور مقامات قضایی در این صفحه قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78320" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78319">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGc32MFEtoT8CVRSPMMTcRpiDjOBAbKLbTZKABSyxnvD3Is9DJgeqXdPou5qELR1uMwnYOoHgb3S8RZk0XeD51OcghzZ9Yh9kvbc507xWSFBsChN2FnBneRjNl4qrfC7BmbGfBhhXsB5eNNSLXulj1cJv8WAeWd8TE0_qzZPVEHgy9SLZQZPZA_BYnhlijo18Ocb_kYzvnsTwlYbyUtQDjtZGVQOIxr-vRQXz1QSnc8NqovhYtRGkwm4iyAVoNYVSO4KHwNFzo8ug3jhDD807PdcWUjoq2ApW2CwWS94emRLuEQBsBQSEwueMHPWvyZ11k8_4SuscGsKHTT0NDMZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس بریتانیا دو نفر را به ظن ارتکاب جرائم مرتبط با ایران و نقض قانون امنیت ملی بریتانیا بازداشت کرد.
این دو فرد در لندن پایتخت بریتانیا و در جریان تحقیقات مربوط به فعالیت‌های مرتبط با ایران بازداشت شده‌اند.
پلیس متروپولیتن لندن با صدور بیانیه‌ای تأکید کرد که این تحقیقات، با هیچ‌یک از حوادث ماه‌های اخیر که در اماکن و ساختمان‌های مربوط به یهودیان و جامعۀ ایرانیان مقیم بریتانیا رخ داده بود، ارتباطی ندارد.
هنوز جزئیات بیشتری از هویت افراد بازداشتی یا ماهیت اتهام‌های منسوب به آنها منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78319" target="_blank">📅 18:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XSSM5BF21g8mOuu1czLxcQEvr4xLKwAV7D0OKiJoK5Ct_3LE_-xIHA07h4qOIPXAzcNjVIMajnIiaWKwSfhfGT6TFYSG8LzJaEUi6fTWy5vx9-rREpCweUkmj6uExwLKinlCJLmx4qDs8JOAKhSd8Gfry9beNaPxxFZp5D4fkf22SP0j_UgvYdMmqgAZFBP9q86h9W1DGfFlNJwIs5VgNqmNez0X0dh28cMt0XonrcSyF98twC8X9i1hHi-Uup67Dxgnw87gj1iQxqEzPsA8hrrKgi4xrEzmVC2wPf2mzKVw7JYHATTnBWJXC3wIwJ40Qi3KHvnbxbuBm5AW3Vr1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lpyGj_pXvd9i3tSn06vfUN2qXxLxTVYSPlTz0lS0K93U3GFXD-3Uq7CCSOTppA_sLmzSy-bdraYawIP6Q4kSdRfdJulyEt-SIz0-nlYD-43oANODVeY6QC6xHOS_Hl6xY-vgApaoIK0_Bch25tb3JODauOx-jN3EkGBsZLQ0-gXwCOGV06xWsJTYyyit44D8ZxOBS7hf_jW34w40hMUbxONH48v2d_V6KLzE24e-bsnh6g-lILcho6tLbZY0CyCNKhoBosoRYY2kpR4WBDOTawE0kBw5fz_9LUO_7Lbkj-1XHltDimVL6G9RhCANT4Vja5dnapWAvOk1hdY_CD50zQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اکانتش در توییتر:
MaryamAzimih
مریم عظیمی، مهندس ایرانی اپل، که پیش‌تر از بازداشت و انتقال خود با چشم‌بند در خودروی نیروهای اطلاعاتی جمهوری اسلامی در مشهد و تصور مرگ قریب‌الوقوع نوشته بود، در مراسم جهانی رونمایی اپل، یکی از فناوری‌های جدید دوربین آیفون ۱۸ پرو و پرومکس را معرفی کرد.
عظیمی در ویدیوی از پیش ضبط‌شده اپل به‌عنوان مهندس کیفیت تصویر معرفی شد.
او در بخش مربوط به دوربین آیفون ۱۸ پرو، قابلیتی به نام «تصویر مرجع اپل» را ارائه کرد.
اپل دوربین این مدل را پیشرفته‌ترین دوربین خود تا امروز توصیف کرده است.
حضور عظیمی از دو جهت در میان ایرانیان مورد توجه قرار گرفت: نقش او در توسعه فناوری تصویربرداری در یکی از بزرگ‌ترین شرکت‌های جهان و مخالفت علنی‌اش با جمهوری اسلامی، از جمله روایت شخصی او از دوران بازداشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78317" target="_blank">📅 17:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FcW9QHsW8fCDdf3jACMz9p-FRpS3rDqUNXXf--o0nLiHMJLqLPbNAx9PgC7ENLSxzo3SsX5avKkZXaWkLUFZ5zW1s-q3cbhaXq2RcBljTKxQTypyfaBXxPkKCz9VlEG5ktYH1_nqyqVdMIR-_IQmusA0PviVtcO5h6wwreIjH8C3_5Dohqb7yU6lFu09pS7ZUI7k3VrKBFux_nPQlZglyxQd1T0esgYGjE-Wna8PvTyAaT2dCo-k0up07MTelP4jzjFZu9tZF1HQ9cw0YaA11xrmS0bHSKV15uVwxZiHGSnn0RooswpBgnpcRrFdA9lYBIeFUWK1hifiQ5eeDUuquw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YR-H6Q_UcH13J4EgZjxXd9GDY6_5PFofbIMAyqJaN7wy6-rtaV_JbRxFCq2xTJ6plrlReMMZw0FIoMcRc0gjTLCeLH0UdPKlikKE4RINhdlJIt0vGh4Fk41bAEL2P9b6fbrC_Fy46ZpUgbE8uaHLiedIFuOc3Vriye24RwSy1YLD9wcDjAclCVWkHwvoW0Ft4tOqizxPUHXmjcmNJi7hc4RGOx313BjT8P6dl2E-LjoNA0FqiUPkhjQT4Hl3WJGxOOqaCfnj3b9rYcHINqkRQQa8uzQDP2e30mijXR10vsnkFDe6mFmplsuXocyTdeX4C1jMMcGu9a9_NjRQDdTMpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78315" target="_blank">📅 16:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pzh9icbjQlQdH-aZ0xFpcLNCSD3EMKaGJOfren5A4hjwiNB9pTAYFR1Ni7bRNmTps7U7kfJ8MJPZe6aaSBAS3pWa-8UpBcswURroQWLXYRbaIRbNc6AVS_SZZFLR_fX0Tg4SvkIX0kTED2skr1nPUCZJzAq0f8657ChRaPdI5nJ-PJD1SJUFZ9vp8cZ90rF7XU0iXnvAoQ-W9CZqqe202kCmPP99h5nJo5ThrMOjSfF5kUH45yY2AVxtAVyOJss_6DTuSPuypeUNk_ZRyb58iR6uXba8HCcyAQBBT004drNReQVSfCo0pDywvsK2y_3aOGc6WOLZblXxWgZwHZ_3jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند افزایش روزانه قیمت ارز در بازار تهران روز پنجشنبه ۱۹ شهریور (۱۰ سپتامبر) ادامه یافت و بهای دلار به ۲۳۵ هزار و ۷۰۰ تومان رسید.
dw_persian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78314" target="_blank">📅 16:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqkEMTk6momI3mrwIRNdKlvhILb34kpy61AoZLYdyxwiM5Nr6CDHzwuxAvPd3N2bGmVgLBN0eCL_D8PCh52pdEhJFk6yrZ2oOL4U87f_2eN1m1Kfix2nJMLP9c5ReSl6H7t6NARHOtvzGWNLJ0f4DiLNnT1KnV0ZCGG9X8i21EzRRKmrhf1JIOvEEro059JSt87TrvG_V355vIzkEpBdZikacCY7Wj0nj_5RbMoagFgX5ImhFEaNZn9WnTygY4jcZLU19_asJWyKGrXLXfQHg2WqsrPGmHG-QLm-RXzMPLz--x9BVOHa_RXHRc9Y67HA1uUJ_AnHBacX9QEroxL52Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی افزایش تنش‌ها در خاورمیانه، قیمت نفت شاخص برنت روز پنج‌شنبه از ۱۰۲ دلار عبور کرد که نسبت به روز گذشته حدود یک درصد و نسبت به ابتدای ماه حدود ۸ درصد رشد نشان می‌دهد.
طبق برآورد اداره اطلاعات انرژی آمریکا، ماه گذشته تولید روزانه نفت ایران به خاطر اعمال مجدد محاصره دریایی آمریکا ۸۰۰ هزار بشکه نسبت به ماه ژوئیه افت کرده، اما هم‌زمان تشدید حملات جمهوری اسلامی به کشتی‌ها در تنگه هرمز و آغاز حملات حوثی‌ها در دریای سرخ و باب‌المندب به نفتکش‌های عربستان نیز باعث شده متوسط تولید روزانه نفت کشورهای عرب منطقه در ماه گذشته ۹۴۰ هزار بشکه نسبت به ماه ژوئیه کاهش یابد.
مجموع تولید نفت ایران و کشورهای عرب منطقه در ماه گذشته ۶.۷ میلیون بشکه کمتر از دوران پیش از جنگ خاورمیانه بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78313" target="_blank">📅 16:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78312">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pz6FRu5O_Rk6vxGuJeBhAtH74HBkb3m7PL0yc4dEdJkkr8vIq_bVETYXLIkKXNNmYkjJ2CETOxbk5KCF0bYixW3kw-N_pyVfXEWrbxbo465BCltkpgaEx67peC3DoOf1N4vVJ_uX-CEjBWdkNqoTAdTty6CvfOttGhR94tV3n6FNoUw_Wy9OyuEdva5ZHPCKtdVQKVSeYpQhXKUINiRZUdMd3A_mC_Y2dyNf_-5r_d81VLXDSvDkFeQX-OfkmSKg8vPU1oDbcRkYPesx_Ay4VuPsErI5zL5wacDQFS-9_KDqIy8MRV_QflSv5ptRanXyPQuTyC366jRuCvYqyBeb4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع ارشد ایرانی و سه فرد مطلع می‌گوید حکومت ایران با استفاده از سازوکاری شبیه تهاتر و با دور زدن تحریم‌ها، در حال وارد کردن میلیاردها دلار کالا از جمله تجهیزات نظامی از چین است.
در این گزارش که روز پنجشنبه ۱۹ شهریور منتشر شد، منابعی که نام‌شان اعلام نشده گفته‌اند بر اساس این سازوکار تجاری مخفی، نفت ایران در ازای اعتبار برای واردات از چین در سال‌های اخیر، یک شریان حیاتی مالی برای تهران همزمان با افزایش فشارهای اقتصادی و نظامی ایالات متحده فراهم کرده است.
آن‌ها گفته‌اند که این سازوکار همچنین به چین، بزرگ‌ترین واردکنندهٔ نفت خام جهان، کمک کرده است تا به نفت تخفیف‌دار ایران دسترسی داشته باشد.
به نوشتهٔ رویترز و به نقل از منابع طرف گفت‌وگو با آن، ایران از این سازوکار برای خرید دارو، وسایل نقلیه و تجهیزات ارتباطی از چین نیز استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78312" target="_blank">📅 16:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78311">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=f4U9XC6sJE6akeZExQnwRPEM_yZ9YeegPeRTomhqVKnWyRMWPDz3uPzlofP8FedDi2O2bGnZyzZclrnRdieNY7QVRM0kit7iR9Lj2D38dYtIqF8g0rGegnYuNIEp9afTXG2DLBiCNnKVfZJZ7Ugda37zXSJA-qbpib2_SxjHSmZF2ug7MegDKApRlCMRMsZ6m5rzJQj9Sc1V_7v8zgrcL_abKfnx13BGBTb8nYMSxcGB-AnelcNkzjWWqAlXpxdiaXxec66MooFVgO7Zfv9xU8SXjP7bRwLTROFNzsvK5OwqLnwQr1UITgOaCdYo505lygIKxXvDKXSjSXsSnSQ3Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=f4U9XC6sJE6akeZExQnwRPEM_yZ9YeegPeRTomhqVKnWyRMWPDz3uPzlofP8FedDi2O2bGnZyzZclrnRdieNY7QVRM0kit7iR9Lj2D38dYtIqF8g0rGegnYuNIEp9afTXG2DLBiCNnKVfZJZ7Ugda37zXSJA-qbpib2_SxjHSmZF2ug7MegDKApRlCMRMsZ6m5rzJQj9Sc1V_7v8zgrcL_abKfnx13BGBTb8nYMSxcGB-AnelcNkzjWWqAlXpxdiaXxec66MooFVgO7Zfv9xU8SXjP7bRwLTROFNzsvK5OwqLnwQr1UITgOaCdYo505lygIKxXvDKXSjSXsSnSQ3Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تخریب «کاروانسرای روس‌ها» در سبزوار:
quotes
خانه واجد ارزش تاریخی «تومانیان» معروف به «پادگان روس‌ها» در سبزوار روز چهارشنبه در روز روشن با لودر تخریب شد و اعتراض گسترده فعالان میراث فرهنگی را به همراه داشت.
تصاویر منتشر شده در شبکه‌های اجتماعی نشان می‌دهد که یک دستگاه لودر روز چهارشنبه ۱۸ شهریور بخشی از یک بنای تاریخی معروف به «پادگان روس‌ها» در سبزوار را تخریب کرده است.
«پادگان روس‌ها» یا خانه «تومانیان» در سبزوار با وجود آنکه در فهرست آثار ملی ثبت نشده بود اما از سوی میراث فرهنگی به عنوان یک بنای واجد ارزش تاریخی اعلام شده بود.
معماری این بنا متعلق به دوره پهلوی اول بوده و در زمان اشغال ایران توسط روس‌ها، ارتش روسیه مدتی در این بنا مستقر شده و به همین دلیل به «پادگان روس‌ها» مشهور شده است.
مجتبی کاویان، مدیرکل میراث فرهنگی و مدیر پایگاه بافت تاریخی سبزوار در گفت‌وگو با صدای میراث گفت: این اثر بدون هماهنگی و بدون مجوز میراث فرهنگی تخریب شده و اعلام جرم علیه تخریب کنندگان این اثر واجد ارزش تاریخی قطعی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78311" target="_blank">📅 16:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78309">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OlRD3h_ZCbDGzySTbUkxg1TH5NTSmBBj0ALegq5GAW2QhBPaw2FY5KbwjcWm5o0gkGHfwOeQX5n4JeItx_NnEkksww3PExXFQnOpLsOA2zTcHBqftOMNtloMgAcScy8xOjhvCJeCc4DjK91b5fEqdN9YgUl4mYlh5yG9I7zglbzzTyQGye5MzdGyhQOJDtlSjxC0qaYlGRttk6yb47xaCT26tlgJiqixRPid-C8RqalhKlLdq3B8UEEvDASUfdG8aRrTtzrhv77cnKZn3k7DMIvYFTIhTo8r4O9YV69pUMRHhQ_aKFbePpx9DSjzciNPiqR8ogKxFVyFNhjPgG15eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/STNp2V-_GHmDmHHC3RXwdmgri-A-zaEDYdPl5u_Useo1NjQxr-mEJ0ejzXsbmkaGdTnYXcx5_Rg3vKSktFvI8nxz1nLU3uHH0O71Wd9qFds9waWKJSGvf3urY8THuTEQ0FsThuDjgrwGM51P6un_bSQMcvtrzoTxvZ5LEvNHILoZtVKs-FR-gss3G4R9E47Ey6OkfF_vqMQMLYQhj6_DWczgbZwKCErIoqTGiLcpOJGy0kib0tw0VsZTFmAzJ4V0K_5Riyo1-znC9MPvQKrsWVgBVbQcluelSLibEa1gkk7RKVYMjKFkWV-A8dGKQMphy23wLBTe0E5kc_ogoRbEnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ از مشاهده «تحرکاتی» در کوه کلنگ‌گزلا خبر داد و به جمهوری اسلامی ایران هشدار داد: «توصیه می‌کنم ایران زرنگ‌بازی درنیاورد، زیرا مجبور خواهیم شد بسیار سخت به آن حمله کنیم.»
ترامپ در ادامه از حاضران پرسید آیا ایران باید سلاح هسته‌ای داشته باشد و پس از پاسخ منفی جمعیت گفت دولت‌های پیشین دهه‌ها تلاش کرده‌اند جمهوری اسلامی را از دستیابی به سلاح هسته‌ای منصرف کنند، اما به گفته او، مقام‌های جمهوری اسلامی ایران «زبان گفتگو را نمی‌فهمند.آن‌ها فقط یک چیز را می‌فهمند و اکنون به مقدار زیادی از همان نصیبشان می‌شود».
@
VahidOOnLine
رییس‌جمهوری آمریکا، در گردهمایی جمهوری‌خواهان در دالاس گفت جنگ با جمهوری اسلامی مدت کوتاهی پس از انتخابات میان‌دوره‌ای سوم نوامبر پایان خواهد یافت و تهران خواهان توافق با دموکرات‌ها است.
ترامپ برجام را «یکی از بدترین توافق‌ها» خواند و گفت جمهوری اسلامی در مسیر دستیابی به سلاح هسته‌ای قرار داشت.
او افزود: «اگر من برجام را لغو نکرده بودم و اگر با بمب‌افکن‌های زیبای بی-۲ آنها را هدف قرار نداده بودیم، اکنون سلاح هسته‌ای داشتند.»
ترامپ گفت در آن صورت مجبور بود با رهبر جمهوری اسلامی تماس بگیرد و بگوید: «جناب رهبر، حالتان چطور است قربان؟ کاری هست که بتوانیم برایتان انجام دهیم؟»
ترامپ در ادامه تاکید کرد: «ما نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. موضوع بسیار ساده است. نمی‌توانیم اجازه دهیم آنها سلاح هسته‌ای داشته باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78309" target="_blank">📅 06:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78308">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78308" target="_blank">📅 06:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78307">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78307" target="_blank">📅 06:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78306">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78306" target="_blank">📅 06:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78305">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پیام‌های دریافتی:
سلام الان ساعت ۰۰:۲۵ قشم صدای انفجار اومد
قشم صدای انفجار اومد
وحید قشم بد زدن تمام خونه لرزید
#قشم
00:24 نوزدهم شهریور
صدای انفجار و لرزش
قشم صدای شدید
شیشه ها لرزید
موج انفجار شدید همین الان قشم 00:25
وحید قشم یه صدایی اومد
شیشه ها لرزید
صدای یک انفجار بندرعباس
وحید جان انفجار شدید ساعت 12:25 قشم
سلام صدای وحشتناک باعث لرزش شیشه خونه شد
سلام قشمو بد زد کل ساختمون لرزید
همین الان نزدیک قشم صدا انفجار اومد.
خونه لرزید.
صدای انفجار به بندرعباس رسید لب ساحل نمیدونم کجا زدن
درود به آقا وحید شبت بخیر ساعت 0:25 انفجار سنگین از سمت دریا نمیدونم قشم بود یا جای دیگه ولی بندرعباس به شدت حس شد
قشم لرزید
موجش قوی بود
شدید بود خیلی
توی دریا بود انگار
سلام داداش وحید .صدای انفجار مهیب در قشم شنیدیم
خیلی مهیب بود ..
۰۰:۲۶ بندرعباس انفجار رخ داد
فقط صدا نبود
در و پنجرها هم تکون خوردن
صداش انقدر جدید بود ما داریم میگردیم میگیم لابد اسانسور ساختمونمون ول شده
🤦‍♀️
صدای انفجار در خونه لرزيد قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/78305" target="_blank">📅 00:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78304">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/692967643d.mp4?token=VvO6yp3jxCiwWkW4iF5JnP-0iBqKHowrqY8jy146bXlRomYEMmdb_XS0BY0kret4NeTe5MWBsDIoaA7OO1oJDyujG27vmBtenksKeVHE9A5fgYPMt6TljpPc5-Gez2WMvmZ8xedOcpqTZX3NqUH_VUE0-7oNdjpGOkdapL_Vrt65WOy1prdj9WRxUsFgpSo9t1SPXfjdgtcUCGaEVh4_AFkA0K-baxbabPpS3DqxfuUct5TVo5t_1b8JbK62x6Savx4f4SmO7dRoAy28fyxKEy6KimFBl63rBXGPmBlzB78Z3X_jHPP5ZQqAO1aGiOKZfCohJiBWrgwbv-odeQrvxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/692967643d.mp4?token=VvO6yp3jxCiwWkW4iF5JnP-0iBqKHowrqY8jy146bXlRomYEMmdb_XS0BY0kret4NeTe5MWBsDIoaA7OO1oJDyujG27vmBtenksKeVHE9A5fgYPMt6TljpPc5-Gez2WMvmZ8xedOcpqTZX3NqUH_VUE0-7oNdjpGOkdapL_Vrt65WOy1prdj9WRxUsFgpSo9t1SPXfjdgtcUCGaEVh4_AFkA0K-baxbabPpS3DqxfuUct5TVo5t_1b8JbK62x6Savx4f4SmO7dRoAy28fyxKEy6KimFBl63rBXGPmBlzB78Z3X_jHPP5ZQqAO1aGiOKZfCohJiBWrgwbv-odeQrvxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز چهارشنبه ۱۸ شهریور گفت که از دید او جنگ با ایران «بلافاصله» بعد از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت.
دونالد ترامپ پیش از عزیمت به سمت شهر دالاس برای شرکت در اجلاس حزب جمهوری‌خواه به خبرنگاران گفت: «فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام خواهد شد. چون آن‌ها (ایران) دیگر نمی‌توانند دوام بیاورند».
ترامپ درباره وضعیت ایران افزود: «آن‌ها مستأصل هستند و تلاش می‌کنند بر انتخابات تأثیر بگذارند».
ترامپ در پاسخ به پرسشی درباره حملات گسترده طرفین در اطراف تنگهٔ هرمز گفت: «حملات توسط ما انجام شد. ما ۹ نفتکش آن‌ها را زدیم. قرار است حملات بیشتری انجام شود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/78304" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78303">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/739c863db9.mp4?token=TE-MV9LRoPrkFG7urHpT0nUwbs_xQQpAFacCViZvCQ1Zp5vbY4NNC5dPgVIwABjWRbyASUvcVfVBe4sCSfwrlU3lKKHDDAuC247pEujgPdSP37uqvY9Ra3bCJb0tnRruci2Pbpig7CiKi37P41IgyZ65SfxbOrrgFzzOA_FUsnD6mp5DGRVrpOmvSgg-jjq129yGC7rml_bq4VUqEsuJU0wfywMQPndW5RS0uGFgLrEZ02vIraareH9CQckaO56Gq0UCkfpCmfwMfWQffsFUVWgf5y-qve7ED1O16jKZ-1ZhvfUP6Q_hWVrIc0nbCjSa8Lx_oWQy3Ccp3XL3-A0vZg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/739c863db9.mp4?token=TE-MV9LRoPrkFG7urHpT0nUwbs_xQQpAFacCViZvCQ1Zp5vbY4NNC5dPgVIwABjWRbyASUvcVfVBe4sCSfwrlU3lKKHDDAuC247pEujgPdSP37uqvY9Ra3bCJb0tnRruci2Pbpig7CiKi37P41IgyZ65SfxbOrrgFzzOA_FUsnD6mp5DGRVrpOmvSgg-jjq129yGC7rml_bq4VUqEsuJU0wfywMQPndW5RS0uGFgLrEZ02vIraareH9CQckaO56Gq0UCkfpCmfwMfWQffsFUVWgf5y-qve7ED1O16jKZ-1ZhvfUP6Q_hWVrIc0nbCjSa8Lx_oWQy3Ccp3XL3-A0vZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامعلی حداد عادل می‌گوید حکومت فعلا نمی‌تواند «به علت شرایط جنگ آن‌طور که باید وارد جبهه حجاب» شود.
این عضو شورای عالی انقلاب فرهنگی و مجمع تشخیص مصلحت نظام در ادامه می‌گوید شرایط کنونی کشور از نظر حجاب «بسیار سخت‌تر از سال ۶۰ است که شروع به کار کرده بودیم».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78303" target="_blank">📅 21:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78302">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AQ_KY6R_bfXdR2IhHI7HzO_y3PVBkluZqGycGvP2KmlXFJBFcz_JgTu0n3jiqaY0G2fGPwQDAEbvqkBKem1gUdLZvELwKdOt4CLJt_jW3msUFdTb_t-4OA0a8fKW7ELnsIwDrNJFQJR6MSYAzVeDXNYU5TVHGgl7ow32sJxQJT36uKONvyFAcFevYaJ8htLLFs-VDAxX6BTfaup9H9bgMwb06TjfdFUrWoNsmEdyO91XBiKRlZS1QpA1-kLtbvqV5Im80pPs2tyyPcHI-LXak7zidCc2hxtfZElQU5-1U76v4w-up5eiQ5Viw-C9ydwCgQdprx2elODZ0Dtzk4WlUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز روز چهارشنبه ۱۸ شهریور به نقل از منابع دیپلماتیک گزارش داد که شورای حکام آژانس بین‌المللی انرژی اتمی با صدور قطعنامه‌ای، پرونده ایران را به دلیل نقض تعهدات منع اشاعه هسته‌ای، پس از ۲۰ سال به شورای امنیت سازمان ملل متحد ارجاع داده است.
این قطعنامه جدید در پی قطعنامه پیشین شورای حکام در ۱۲ ژوئن سال گذشته صادر شد؛ فهرستی از موارد «پایبند نبودن» ایران به تعهداتش که درست یک روز پیش از آغاز حملات هوایی اسرائیل و متعاقبا ایالات متحده به تاسیسات هسته‌ای ایران تصویب شده بود.
بر اساس قوانین و الزامات حقوقی، گزارش رسمی این نقض تعهدات به شورای امنیت سازمان ملل، مستلزم تصویب دومین قطعنامه از سوی این شورای ۳۵ عضوی بود که اکنون به سرانجام رسیده است. این اقدام می‌تواند مسیر را برای بازگشت تحریم‌های بین‌المللی و افزایش فشارهای دیپلماتیک بر تهران هموارتر کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78302" target="_blank">📅 20:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78301">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F2eNqWtfxiMXvSNTXsJypm8fo6QlDDCkd6Bre0u2SMY3Y2ahTiru_lZNnbaXPl1DSM6zs1Ec3OqtLw13IzXyRjdAJCQ2LKGr7c6VXwvir3349mm7CfcBG9TsnJEYNGEKsvKaZf3TrIhszoiHHgyyGGSB09BMHgj6SwIM34VrMLDrpTI2-0jWFsCaQVx_TudABxn9WIsRINkUm1gwpaozpSjRP5IPKHKNfIDicjA8DMrsPqm6ZjWHf_yn-ZvukdCNDMXaDRzMHJ5hpaTUmGoqSxWxkdID_KpjpdiVaWLrNVBvjVWiQdwhATRdWJL-8Go8Yo8L3Xoc93_SpF7AtppxXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: 'شناور آمریکایی در تنگه هرمز، سمت جزیره سلامه خصب عمان، چهارشنبه ۱۸ شهریور'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78301" target="_blank">📅 19:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78300">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=ktoCp30e9hnlolWOpuTJI53oyLkZRmNPJr6mE7EI0V8kvG7hyI4Dktl2nMmhpcR2kGC8xc0gowxy4RaOQO0GdK-jdju9DzM6NJpa4LkBTMeJGKcJzs0zx4i1jx_BBSxVRsNh01td06mhJyOVRau4ADUp21r26VGq_Lkfh5blxOXS0giJ-xkHGwrbNHaP6PdZlKNDQO9OOcDR4IKdEEdMMrll6JkspiYEuaOM6IK8Vxv0tDFxhBwtnTbnVK6mjXLZgtyvJ8Lh9s7BXtf86JevDj3LVhkfLTGYqBGL9K1zsv9R7yQN_6RRRxnXGm1p7CTEqaE4unlTDSTTUv-TEu1obA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=ktoCp30e9hnlolWOpuTJI53oyLkZRmNPJr6mE7EI0V8kvG7hyI4Dktl2nMmhpcR2kGC8xc0gowxy4RaOQO0GdK-jdju9DzM6NJpa4LkBTMeJGKcJzs0zx4i1jx_BBSxVRsNh01td06mhJyOVRau4ADUp21r26VGq_Lkfh5blxOXS0giJ-xkHGwrbNHaP6PdZlKNDQO9OOcDR4IKdEEdMMrll6JkspiYEuaOM6IK8Vxv0tDFxhBwtnTbnVK6mjXLZgtyvJ8Lh9s7BXtf86JevDj3LVhkfLTGYqBGL9K1zsv9R7yQN_6RRRxnXGm1p7CTEqaE4unlTDSTTUv-TEu1obA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با حضور در قله جبل‌الشیخ (حرمون) و اشاره به تسلط بر مناطق مرزی سوریه و لبنان، هدف اصلی کارزارهای نظامی جاری این کشور در منطقه را شکست و سرنگونی رژیم ایران عنوان کرد.
نتانیاهو در پیامی ویدیویی، به حضور نیروهای نظامی اسرائیل در مناطق مرزی سوریه و لبنان اشاره کرد و گفت: ما اجازه نخواهیم داد هیچ گروه تروریستی در مرزهای ما مستقر شود. این یکی از دستاوردهای عظیم ماست، اما کار اصلی هنوز باقی مانده است.
نخست‌وزیر اسرائیل با ابراز اطمینان از دستیابی به این هدف افزود: کار اصلی ما شکست دادن و تضعیف کامل رژیم ایران است. ما بسیار به این هدف نزدیک هستیم و می‌دانیم که کل این محور سرانجام سقوط خواهد کرد و ما این کار را انجام خواهیم داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78300" target="_blank">📅 18:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78299">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X24iarPPtkDJIyOO06brT0WvNmR31QWzX8XGIC-Mvg-UhRTCM5Czke-TJKupmFsAkgA_-TDv6tuLK0Cnm3_FAqe0Y90f_zwV41HC8MlSQZty_s7BzdccHrFD7G232ZY04NgT6IYfkVuMC3x82BT4hOETElxdOxhAHRWwkOta-njo0iFBv6YD3IGQay5ioPJMWWlFrzp3u2IJ9Tq4IYDJhbIOza_nUUpBDWNIoK0NNzJVfbfvI_iLrT5cpnIRp5hKNzC19PpVJToGGQ2nPf5SknIzZMNvZEjO0iML52HtPEhT_Kk0ZSptqP-XECz05YdvGlC0KJm3vBgjfrPF9UvU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه پاسداران برای پایان وضعیت کنونی و بازگشایی تنگه هرمز از آمریکا خواست جنگ و تهدیدها را متوقف کند، اسرائیل از لبنان عقب‌نشینی کند، محاصره یمن پایان یابد، ۲۴ میلیارد دلار از دارایی‌های مسدودشده ایران آزاد شود و مداخله در برنامه‌های هسته‌ای و موشکی جمهوری اسلامی متوقف شود.
حسین محبی، سخنگوی سپاه پاسداران، روز چهارشنبه ۱۸ شهریورماه گفت اگر آمریکا خواهان پایان وضعیت کنونی است، باید ضمن «توقف کامل جنگ» از تهدید دوباره دست بکشد.
محبی در بخش دیگری از سخنانش تهدید کرد که در صورت ادامه حملات، پاسخ سپاه گسترده‌تر خواهد بود و گفت: «اگر دشمن دو یا سه هدف ما را بزند، ما با ۲۰ هدف پاسخ محکم می‌دهیم.» او همچنین گفت جنگ کنونی برای نخستین‌بار «آسیب‌های راهبردی» را مستقیما به آمریکا منتقل کرده است.
این اظهارات در حالی مطرح شد که با تداوم محاصره دریایی ایران، صادرات نفت از طریق تنگه هرمز متوقف شده و فشار تحریم‌های مضاعف دولت ترامپ، باعث تورم کم‌سابقه در ایران و رسیدن قیمت دلار به ۲۳۳هزار تومان شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78299" target="_blank">📅 16:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78298">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tP-IK6dCee1pjMJjvgHegbmuYvEp9zB6qPSht1oYaRnzarfujiq5QqmcygBvtJbuRIFk2yVRlaUVYgejGam5SPJ7RfGllNZsi33YfcFV6x1FYKqWngM_FgX94rF8YbUPPG2vdTIlV2hrsL86S2xEMUs6uvRV-fB_1bekc48YVcOUXnnGfy07s8PcBtc9KMNPXc-biMVmLRBFtvm5C-5n71ARcvDZZk5Q7u2FzDMPlNoPMB6P-8W0oterKrS2MW8FR1DXj_BDNjo6FBekF54un2PGaxLditDdjnZGprSetUSYdTQMP8zo7t9Uai1lejCu_wJcaoQh_gn2q2xIEZO5YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارزهای خارجی در بازار آزاد ایران روز چهارشنبه ۱۸ شهریور ۱۴۰۵ رکورد تازه‌ای ثبت کرد و نرخ دلار آمریکا از ۲۳۲ هزار تومان گذشت.
برخی وب‌سایت‌های اعلام قیمت ارز نرخ دلار را در معاملات ظهر چهارشنبه تا ۲۳۵ هزار و ۵۰۰ تومان نیز گزارش کردند.
هم‌زمان قیمت یورو از ۲۷۱ هزار تومان و پوند بریتانیا از ۳۱۵ هزار تومان فراتر رفت. این افزایش‌ها در حالی ادامه دارد که ریال طی دو هفته گذشته بیش از ۱۵ درصد ارزش خود را در برابر دلار از دست داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78298" target="_blank">📅 16:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78297">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD2iBUQixGEYWOKgN5bzEpux5eAk5ZXkiBN3kZrzl6x8Ud9vJ5sE2JMDtvMrxNjTAB-hpp3WJivrC1pNXdVDIfz5p1JtaS-gKdOm7WPAxaV_ZgtLRWBjLDwC6C0ECiW1NEvVL59pVzNmMuzD39JG6yMQ2f8M6g2pCxi6w45voGXY33E2ZVtoPIF7vzqqa2CBbuCA-NDxyU-rWkLBtEIdbuKXr5GEUgpkt5D1zBohv0CezQUfh5GVr1-qW_NevQnCGSLjygXcI9Jtf4Lc-iTx3snjQE0QBb8FcEWKwJOEL2HTuU1FXscFHs4CC1B_sDwBntaLEUaiswGylQCv_wfXLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت خام برنت برای نخستین بار از دوم مرداد به ۱۰۰ دلار در هر بشکه رسید و بار دیگر وارد محدوده سه‌رقمی شد.
افزایش قیمت نفت و ارز در شرایطی رخ داده است که درگیری‌ها در خلیج فارس و منطقه ادامه دارد. شامگاه سه‌شنبه ۱۷ شهریور، آمریکا اعلام کرد پس از حملات موشکی ناموفق جمهوری اسلامی به دو ناو جنگی این کشور در خلیج فارس، پنج نفتکش مرتبط با سپاه پاسداران را منهدم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78297" target="_blank">📅 16:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78295">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kQn5y99xmu5G2MUElKIkWbfmGhHGOjnQ8aaDRK44lzVRc51ksbZ5HQzUG4_8Bn05Cgt3NZ4Lx15tm0nsUf4_ZEGvHAFlnEBy18lVat7bgB0JDnFHQY63K86oCLCVdO0q2QC7iJWT8FJZEVkOi6ZwHKxtWi4qVq6U8nj0xgPqHlH9_9anODG4PMtDfxdZsfJRCCLgOlM8AbP2JcY3cxD_qntl1xaCY1h1PqQFhU58kU61YomKhZuzapAKXWKFTi0BxYiKfFovVHPyUZlYEIa4iOWU6eyl85YiRi-QJfiaksaoXMbsDutqP4JIsKxs3jha0nQujXuOK9SqW_gMdTaX1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ea7NHUZ-Eu_0KKy_BcxLlIHEgfz8eCwyoWervGhJEzDKBsO6XWdUJG1LRPxnam4y0Xk-8bL8jREve1S8vbO6DtbbHoy8Hi34Ls97azbxnXRD4BZS7VwqdobxOQ-bTGTnAnX1OwZNHekdoGDuWZ1vY3gXPWwkRpOXaSbeaYk7zRweM4AjUn967yzhrUiIpUIbds_6q2XThb8RvAmO7fS3TRPlc8RKAxEYeyb-EVk8ofpZ5vQIHsvlwzfMl3TWmXFEkxhjSVDlENITmI71A8_-PHfhYAEHxS89A4l1Wvm2oeZ4gigwQtrD65rzRO08ikOuMVKHT6KMVxynJxwI8AJDqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا (UKMTO) ظهر چهارشنبه ۱۸  شهریورماه از وقوع حادثه برای یک نفتکش در ۲۴ مایلی بندر راشد امارات متحده عربی خبر داد.
براساس این گزارش، «کاپیتان یک نفتکش گزارش داده است کشتی‌ای را مشاهده کرده که در حالت لنگراندازی کج شده است، که احتمالا نشان‌دهنده ورود آب به داخل آن پس از حمله با یک پرتابه نامشخص است.»
@
VahidOOnLine
مرکز عملیات تجارت دریایی بریتانیا اعلام کرد یک نفتکش در ۲۸ مایل دریایی جنوب شرقی بندر فاو عراق با یک پرتابه ناشناس هدف قرار گرفته است.
بر اساس این گزارش، ناخدای نفتکش برخورد پرتابه با شناور را گزارش کرده است.
خدمه نفتکش در سلامت هستند و تاکنون هیچ پیامد زیست‌محیطی ناشی از این حمله گزارش نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78295" target="_blank">📅 16:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78294">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XPiGLT7AHkilS_a25e40WWnZPHay20b1rLNx3unMjgm8mJjerr9WONgX7f2cNWMPAF3IM7P4xqaTpLw-CAZnRkFqD8rOfwX7scvv4QVyOYAzkZQ250wPiA1R5vXr4og24VXxDAGHnZpfCpNClfPk7zyHKoANu3NZTkQGwrs07lKgRPBe91t4-BpEY27UsTa47Qq9D02cCKDTzbFQ3EMJyK8B_lJLuexwsbP_w04ibK_ALpvHFqO62H2X2s9oWKolnWWhFGlBbfnzoe9Y5dLn84wJXZKS63ZDdiePOgoRvHe-W5HVLh62MwsNy6r5mx4ru2eBSEzhDy7d_u5LsVt9Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
🚫
ادعا:
نیروهای سپاه پاسداران انقلاب اسلامی ایران (IRGC) مدعی شده‌اند که دو ناوشکن نیروی دریایی آمریکا را که در خاورمیانه در حال عملیات بودند، هدف قرار داده‌اند.
این ادعا کاملاً دروغ است.
✅
واقعیت:
هیچ ناو جنگی نیروی دریایی آمریکا هدف قرار نگرفته است؛ تمام حملات مورد تلاش سپاه پاسداران شکست خورده‌اند.
در همین حال، نیروهای آمریکایی تنها طی هفته گذشته موفق شده‌اند ۱۰ نفتکش ایرانی را منهدم کنند.
این شناورها بخشی از یک شبکه سایه چندمیلیارددلاری بودند که منابع مالی سپاه پاسداران را تأمین می‌کند و ایران قادر به دفاع از آن‌ها نیست.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78294" target="_blank">📅 16:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78293">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YdkWUafbN99lBp9ZFdoRMtKCYdcClFzdJ0_UkJ1G096vjPgl_K0m9ZA5X8hy3S8de37gPq-PDl6sYpwDSsM7CvcHHCam2xHmd7uqVHVT7cBpB12vJoUUvjghhu3x6wWTS9gmgdJenMyTpbVQst2WlI_4hCiiVhrRvNIyD7FleWeW3AbmDJGbtG3r_f73Ax1th9VpYDUud7gCzKJAj4VNSQlpM4vlmuivOIxD5whtr0t7Fh3fu_02Om7e49FkFMgnm4TToI3d5ZPH4oWtQDgN9fOrZ75MQ77Ld0uRTNXt9m74NjBtENvUKCusS8gw58EmVlDLKp4CpM8kqaT3ZDMhLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ماموستا محمد نزهتی»، روحانی اهل سنت و امام جماعت منطقه چیانه در شهرستان پیرانشهر، در یک حمله مسلحانه کشته شد.
سپاه پاسداران او را از روحانیون همکار با بسیج معرفی کرده و مسئولیت کشته‌شدن نزهتی را متوجه آنچه «گروهک‌های تجزیه‌طلب کردی» و «صهیونیستی-آمریکایی» خوانده، کرده است.
براساس این بیانیه، نزهتی سابقه «همکاری طولانی» با «بسیج اساتید، طلاب و روحانیون» داشته است.
سپاه همچنین فعالیت‌های او را در راستای حمایت از جمهوری اسلامی و آنچه «وحدت شیعه و سنی» خوانده، توصیف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78293" target="_blank">📅 16:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78292">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11f95a9d62.mp4?token=F5PKUs6ZjD15HbG8Za1PZJIn1Nc9q9C1ESReIBxhNyQ63KWMnijkZMGPYApbywKpqDyijtvyaX1vpw25j_gxyZNQsG1D-oWQVk22L3vj5fys6rt3Rv9JwfFWKIKov7s-bQ_13omTQ9omzSznw3BRHWXnXEfrczYAC4F_7iOpH1t9rlk2dUEpp0aB5OjJbO0-GqBf-tsBf5WK3wT1GJegif6tVuZ_2cB1oHQJnNeLNah8BZWtFCDbAjIsESMbdywbGbXSLBvbbi4FcKx-9hhZ18VqXVHTb1DwzBPtLg4qCb7qb6ggnHozrsxPtpKzXpYXhS4o6O3xS63n3SsxfiC5fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11f95a9d62.mp4?token=F5PKUs6ZjD15HbG8Za1PZJIn1Nc9q9C1ESReIBxhNyQ63KWMnijkZMGPYApbywKpqDyijtvyaX1vpw25j_gxyZNQsG1D-oWQVk22L3vj5fys6rt3Rv9JwfFWKIKov7s-bQ_13omTQ9omzSznw3BRHWXnXEfrczYAC4F_7iOpH1t9rlk2dUEpp0aB5OjJbO0-GqBf-tsBf5WK3wT1GJegif6tVuZ_2cB1oHQJnNeLNah8BZWtFCDbAjIsESMbdywbGbXSLBvbbi4FcKx-9hhZ18VqXVHTb1DwzBPtLg4qCb7qb6ggnHozrsxPtpKzXpYXhS4o6O3xS63n3SsxfiC5fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشک‌های مادر یسنا (فروغ) اسکندری در سوگ دخترش
یسنا اسکندری، وکیل دادگستری و نقاش، شامگاه ۱۸ دی‌ماه ۱۴۰۴ در منطقه آریاشهر تهران هدف شلیک نیروهای جمهوری اسلامی قرار گرفت و جان باخت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78292" target="_blank">📅 16:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78291">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KfsfTngR-UrMAvPLigy1Mv5M7m3gdV83M3GU5R6uVjl7yAAfr0GzW__Z1f0zm3LXyK0m7GtEp2Nh0L7Zf5hrP84wRF8Rr4Fcuoje9PfJESuXxAsGPB4bZ3QDu1Q21DgaFkDDgBQp_XjkinG34mHXJvj_1x2ltbkRagtgJIf8MHd79Ys7PCfqYtwb9yjYERP_A10ibLJFn8FagF75ryVIFuGSpFDmTYuICjAJADmiuem4r5hVgFndnThQKhYRtsdim7MhszWsPkAjlwiwR_16mCDjy5FHPI0YDwsw1F0Xu4Uy_oNKzT5euVXb7yGIAo5RKaXZcOr_oRqfJhrMZziqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران: دو شناور و هشت نفتکش را هدف قرار دادیم
سپاه پاسداران که در طول چند ساعت گذشته با انتشار چند اطلاعیه از حملات موشکی خود به مواضع آمریکا در اردن و بحرین خبر داده بود، در آخرین اطلاعیه مدعی شده است که در واکنش به حمله آمریکا به ۵ نفتکش ایران نیروی دریایی سپاه به «دو فروند شناور آمریکایی و هشت نفتکش» حمله کرده و «خسارت های زیادی» به آنها وارد کرده است.
در این اطلاعیه که بامداد چهارشنبه ۱۸ شهریور منتشر شده همچنین ادعا شده است که «۱۰ فروند کشتی متخلف که به گفته نیروی دریایی سپاه، قصد عبور از «منطقه ممنوعه و ناایمن تنگه هرمز» را داشتند حمله شده است.
این گزارش‌ها هنوز از سوی منابع مستقل تایید نشده است.
با این حال، سنتکام در اطلاعیه نیمه شب سه‌شنبه خود هدف قرار دادن ۵ نفتکش ایران را در واکنش به حمله به رزم‌ناوهای خود دانسته و گفته بود این ناوهای جنگی خسارت ندیده و در حال ادامه ماموریت‌های خود هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78291" target="_blank">📅 08:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78290">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=IoODrezqufbTaAH-kvItbwtJdp9jLB6pE8FggTq__u1oqNAC3RlDqidlbfmmIiCPRl-HZRPyoell6KLZ-OYk9vIL7u4s03dNd8quvnV3T4uGAiOs5oQlSYRpIV-dO1HFQdDG5ZAEPFpOrmB_7eVV7gkNf9PTijFx7j5z84uwwPKEFDpPdsbDv7FyH1v2OC_aRPxmBsjHtvbfQ-RaGfBed3DzGKTr3J_etUG6v2xaByiW2O1wVt4FEqtOv7ORZu0wWajytDFx18Mk9F7gR4TtHP9-tpTAhP_Rt6wIUQLrXnfHjbIbOClkjuBbnUuuGnxinhi3L1R5E4UVVPD9MADFaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=IoODrezqufbTaAH-kvItbwtJdp9jLB6pE8FggTq__u1oqNAC3RlDqidlbfmmIiCPRl-HZRPyoell6KLZ-OYk9vIL7u4s03dNd8quvnV3T4uGAiOs5oQlSYRpIV-dO1HFQdDG5ZAEPFpOrmB_7eVV7gkNf9PTijFx7j5z84uwwPKEFDpPdsbDv7FyH1v2OC_aRPxmBsjHtvbfQ-RaGfBed3DzGKTr3J_etUG6v2xaByiW2O1wVt4FEqtOv7ORZu0wWajytDFx18Mk9F7gR4TtHP9-tpTAhP_Rt6wIUQLrXnfHjbIbOClkjuBbnUuuGnxinhi3L1R5E4UVVPD9MADFaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) با انتشار ویدیویی نوشت: نفتکش ریسکو روز سه‌شنبه، پس از آن‌که در واکنش به تلاش‌های سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی آمریکا توسط نیروهای سنتکام منهدم شد، در خلیج عمان غرق شد.
@
VahidOOnLine
M/T Riesco sinks in the Gulf of Oman, Sept. 8, after being destroyed by CENTCOM forces in response to attempted IRGC attacks on a U.S. Navy warship.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/78290" target="_blank">📅 05:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت 4.19 دقیقه صبح بندرکنگان الان صدای انفجار اومد
در و پنجره ها شدید لرزید
سلام صدای انفجار نزدیکای بندر دیر
صدای انفجار شدید.بندر دیر.
ساعت ۴/۲۰ بامداد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78289" target="_blank">📅 04:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78288">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EqT7bwdehUHDRWIfY5fEl2KXSsi9PpNM4I4wavo7JPIn_2KdCHCKyPjZtEpcxFbk--gn7RHsoVMHzDGyXHAr8-ZmndM9aoG_EcgPX14B2wjqWG2Y6nvDKawiq4VWPwp8pvWacwHhZ2EtKpkiBnGFixtNTuHrZNcakLRw7Knuw-bqiuN86dQ1FMBihw90lhhplsICd8px8T-HWyqMXiSS4iXETqoWbjsMzHkaowkaiL-J6pXf3Ihnvo1UW5i3Oc9YTk3HAobLRLnzGorFq2TXg5hSDx9FKKFVNbQcalV0L_nmrQv-FSXaN76bG0o716pAESlp4yDCv07wnJcKt1dDTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای خطاب به «مردم مبعوث شده ایران اسلامی» اعلام کرد که با رمز «حیدر کرار» به پایگاه الازرق اردن حمله کرده است.
در این بیانیه آمده که به محل استقرار جنگنده‌ها حمله شده است.
پیش‌تر اسکای‌نیوز از رهگیری موشک‌ها در آسمان اردن خبر داده بود.
تلویزیون دولتی سوریه نیز گزارش داد که پدافند هوایی سوریه برخی موشک‌ها را که از ایران شلیک شده بودند بر فراز شهر مرزی اربد در اردن رهگیری کرده است.
برخی رسانه‌ها در ایران از جمله همشهری نیز گفته‌اند که سپاه با «موشک‌های خوشه‌ای» به اردن حمله کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/78288" target="_blank">📅 02:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78287">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d875f49ad.mp4?token=c-VLjTRW9bCTYkKw8I6Hjvr1iATqjYBlevJZe3XdXx4EXSf-HMzEB-cpnMG908qAftYy7uXAz5OUQRUyQzGwOEV9ANeXVfxdi4zDEPXxmZva8X53XKgT41pnOW7AgfB1F0gQ1CcXhUhFHnfOy768-sRXCBkdzUFtoNivDfY2cNs5h5U5QaoSwgZDoFrONLVmzunEU6Kf66BDjA6w9_CO_SCeopsNZAkbULK7UoMYlNpvxwRkWLqG16gsarKf6ZWZn6Zt1Oh66FBldzQdHeEBXHeyh_rLfuNDavWbbzFIeGk6W5-1n2mj3JNaVYVwW-quSYW5XFCxPN3-V5nSLgQX5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d875f49ad.mp4?token=c-VLjTRW9bCTYkKw8I6Hjvr1iATqjYBlevJZe3XdXx4EXSf-HMzEB-cpnMG908qAftYy7uXAz5OUQRUyQzGwOEV9ANeXVfxdi4zDEPXxmZva8X53XKgT41pnOW7AgfB1F0gQ1CcXhUhFHnfOy768-sRXCBkdzUFtoNivDfY2cNs5h5U5QaoSwgZDoFrONLVmzunEU6Kf66BDjA6w9_CO_SCeopsNZAkbULK7UoMYlNpvxwRkWLqG16gsarKf6ZWZn6Zt1Oh66FBldzQdHeEBXHeyh_rLfuNDavWbbzFIeGk6W5-1n2mj3JNaVYVwW-quSYW5XFCxPN3-V5nSLgQX5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین
خبرنگار:
آقای وزیر، بخش زیادی از توجه افکار عمومی آمریکا معطوف به آخرین تحولات در ایران است. می‌توانید درباره حملات آمریکا به نفتکش‌های ایرانی صحبت کنید و توضیح دهید که این رفت‌وبرگشت اقدامات در ۲۴ ساعت گذشته چگونه بوده است؟
مارکو روبیو:
بله، این رفت‌وبرگشت کاملاً روشن است: ایران همچنان تلاش می‌کند کشتی‌های نیروی دریایی آمریکا را هدف قرار دهد و هر بار که این کار را انجام دهند یا تلاش کنند انجامش دهند، نفتکش از دست خواهند داد. فکر می‌کنم امروز هم دوباره شاهد این موضوع خواهید بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78287" target="_blank">📅 02:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78286">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b638672d55.mp4?token=o8I7PDRvR6ofL0WTXJn9rq0wIg-S5aXgMo4zvmxGRQ2Gaf-XJTojeZVRdfmgjh3wb0ty1E9L1X5wKS9wnPZJhTWi5aVHQl-gtzcEnXlgGwNS8gbVD9YwLtT5_kKE8aWA1sSduJPlb-WBZx265p9xpU2ayjYdl7GW7cgI1-gFb36BaagBJ3QDAc8xOt8faD2E4hm20j_0pE0RlagJF27VDHG3Mb9oO01esWbptLmWt9oFdI5ozAt-8RCkV8NuUSmnp2UUmULA8RGN4FlWKIikOl3s80egNaCn8PkvzC-VgcQJQ61uI5RWwbXe_lkNsawyx_bKQ9BOgsCd5hIzrx9Paw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b638672d55.mp4?token=o8I7PDRvR6ofL0WTXJn9rq0wIg-S5aXgMo4zvmxGRQ2Gaf-XJTojeZVRdfmgjh3wb0ty1E9L1X5wKS9wnPZJhTWi5aVHQl-gtzcEnXlgGwNS8gbVD9YwLtT5_kKE8aWA1sSduJPlb-WBZx265p9xpU2ayjYdl7GW7cgI1-gFb36BaagBJ3QDAc8xOt8faD2E4hm20j_0pE0RlagJF27VDHG3Mb9oO01esWbptLmWt9oFdI5ozAt-8RCkV8NuUSmnp2UUmULA8RGN4FlWKIikOl3s80egNaCn8PkvzC-VgcQJQ61uI5RWwbXe_lkNsawyx_bKQ9BOgsCd5hIzrx9Paw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: "
آمریکا ۵ نفتکش سپاه پاسداران را پس از هدف قرار گرفتن یک ناو جنگی دیگر آمریکایی توسط ایران منهدم کرد"
"U.S. Destroys 5 IRGC Tankers After Iran Targets Another American Warship"
ترجمه ماشین:
تمپا، فلوریدا —
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) روز ۸ سپتامبر پنج نفتکش حامل نفت خام ایران را منهدم کردند؛
این اقدام پس از آن صورت گرفت که سپاه پاسداران انقلاب اسلامی (IRGC) طی دو روز گذشته، دو بار یک ناو جنگی نیروی دریایی آمریکا را با موشک‌های بالستیک هدف قرار داد.
ناو جنگی آمریکا با موفقیت از حملات ایران اجتناب کرد و به گشت‌زنی در آب‌های منطقه ادامه داد. هیچ‌یک از نیروهای آمریکایی آسیب ندیدند.
در پاسخ به تازه‌ترین حملات ناموفق ایران، سنتکام نفتکش‌های حامل نفت خام سپاه پاسداران
M/T Kaviz، M/T Charminar، M/T Horizon 1 و M/T Riesco
را در
دریای عمان
و همچنین نفتکش
M/T Derya
را در نزدیکی
جزیره خارک
منهدم کرد. نیروهای آمریکایی پیش از حمله به کشتی‌ها و از کار انداختن آن‌ها، به خدمه دستور دادند کشتی‌ها را ترک کنند.
ایران از این نفتکش‌ها به‌عنوان بخشی از یک شبکه چندمیلیارددلاری پنهانی استفاده کرده که منابع مالی سپاه پاسداران و نیروهای نیابتی منطقه‌ای آن را تأمین می‌کند. ایران هیچ وسیله‌ای برای دفاع از این شناورها ندارد.
در ۵ سپتامبر نیز نیروهای سنتکام سه نفتکش حامل نفت خام ایران را پس از آن منهدم کردند که سپاه پاسداران تلاش کرد به یک ناو هواپیمابر و یک ناوشکن موشک‌انداز هدایت‌شونده آمریکا حمله کند. تمامی تلاش‌های سپاه پاسداران برای حمله به ناوهای جنگی نیروی دریایی آمریکا ناکام مانده است.
centcom
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78286" target="_blank">📅 01:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc7356e9f5.mp4?token=OjYpRqh2NLv6o8iKY7B33r0ODc1jDd_COmuC_msvFwpuLUzvyrgMPtt9_yRXaQXcZq3d2b8ces29ChhOzCHpIWv9_fRvlLfX4O0pcfiUgLHjS8ZDyQpjpZhHwMYu6s27G_mubzWEAqohR6rzWbs9zaDTNWWomAHRvTS7QHSf2ZKXME7zLk3eMkBjkGCtFcgWcDeA7ZXqLw6Job5ki4CuQCGd4-l-X2NsfZ_NVMeZUflCK7e_zBYRM6gjw2AHz2h5YnE_9qdAhUJ-zD4ozs-hiJS3N03FOeq47uHR3_OD1eN9AKcooTNRrwkMr3pVKAapgYhiJY04xH-7I1H0yPkfOA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc7356e9f5.mp4?token=OjYpRqh2NLv6o8iKY7B33r0ODc1jDd_COmuC_msvFwpuLUzvyrgMPtt9_yRXaQXcZq3d2b8ces29ChhOzCHpIWv9_fRvlLfX4O0pcfiUgLHjS8ZDyQpjpZhHwMYu6s27G_mubzWEAqohR6rzWbs9zaDTNWWomAHRvTS7QHSf2ZKXME7zLk3eMkBjkGCtFcgWcDeA7ZXqLw6Job5ki4CuQCGd4-l-X2NsfZ_NVMeZUflCK7e_zBYRM6gjw2AHz2h5YnE_9qdAhUJ-zD4ozs-hiJS3N03FOeq47uHR3_OD1eN9AKcooTNRrwkMr3pVKAapgYhiJY04xH-7I1H0yPkfOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنا بر ده‌ها پیام‌های دریافتی از صفهان، یزد، خرم‌آباد، خمین و شهرهای دیگر چندین موشک پرتاب شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/78285" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RzXbyp97qLScnKYljHs7Lq_7SQycu3WwgGlFCb-R7GCNsLxfSzRJz0k-GqjlHyMRnQNVZ_zzi3WU71j-gJtlZoZ8hsDzS81tW6zNL8UbIaxOPaoAuQOEnhrAKIS-magpD3JrlN5H-HH8896Fb33BcCu086PDmAB2F5v9l0NmEFEW9WPWtKUapvv8cZeAtWZptjVcBwZYUYsQg_dKi3Wlfx0DSNNCNnP3_nXMtpHT5WGRCxSCCRMB7hVPx1glk6iktGZvxEH31LGV_DfS7yCBm48PlUTyikkmc6i5hBJl_De966QD0t8RUv6qQ0NA3d3C78VkqAaeQvGc8k-DM6xy4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی گزارش‌ها از حمله ارتش آمریکا به اهدافی در جاسک و اطراف جزیره خارک، رسانه‌های حکومتی در ایران تائید کردند که یک نفتکش دیگر نیز در اطراف جاسک هدف قرار گرفت و خدمه آن با قایق نجات در حال انتقال به مناطق ساحلی هستند.
پیشتر رسانه‌های حکومتی در ایران گفته بودند یک نفتکش در اطراف خارک هدف قرار گرفت.
رسانه‌های اسرائيلی و آمریکایی به نقل از مقامات آمریکایی گزارش داده بودند که علاوه بر اهداف دیگر، چند نفتکش ایرانی نیز هدف نیروهای آمریکایی قرار گرفته‌‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/78284" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78283">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GcBue3zd-39BBC0LUut5tfpC8WznDlWd6Pzgz-q11GAYqbAENWc6fGuGKMPBE9mfxYqyca3vm4Rm5d-duKgFVLLRRIr8NyT5EZu-XPsUzuIR59jLr6NxkaKnL66z2bYfirHM7WF-3CQcIYuT8Cu9P-sfUNCiu8LmvzSVuAMxcnvYsCU5xC7f5Y61kJPD3b3X40boegAUsKXjsDGVGrqcItSuQWSz0aNV9TJuH0eVHVM6jcTLdanJjkyOjmI5vNC91vnJ8pVNg03TapFBNQTLbg5x_qUVa3FohvWHi1nC8q_FUkqXQQJ1pTeY0uGwS9Eg2J8RSET69l1LNrZNAISngA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار سپاه به خدمه نفت‌کش‌ها در کویت و بحرین: شناورهای خود را ترک کنید
سپاه پاسداران انقلاب اسلامی هشدار داد که نفتکش‌های مستقر در لنگرگاه‌ها و اسکله‌های بحرین و کویت را هدف قرار خواهد داد.
در این بیانیه که در رسانه‌های جمهوری اسلامی بازتاب یافت، اشاره شده که آمریکا به «چند نفتکش ایرانی» حمله کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78283" target="_blank">📅 23:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78282">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KF8MCBO8EUo_vlSMtbLYu19pzZ2Nad7xzhKJOR-oAwg6LzV2sBosth1GaAPvZH_IUvtdzjIKkDr34F2j1UuX6-gEwKQzpjIkf02Qc6K-rfDIhxCPD7Niz7SntUWPBqAJM7RV2kwSwk0KgPmfHP0IkwyGCQOaM0MYac5ZI0Mjfgfjajn1H_I8kXRvqHDbaLhCJfmpK_CzEFH2vdpwiMytMSD9WyAQH-yjY2ZsNeLKtXHiG2zjeb8D0OmpMnMKCTIa4d_QESfOXhRiMBKXIPliAzIX9gFSuqm1N1cqiQDV11ZwuXOUfZ7x0RcqK7rklv2rO6kyC9UA6cyH3rwxsnZVmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز: ارتش آمریکا نفتکش‌های ایرانی را در نزدیکی جزیره خارک و جاسک هدف قرار داده است
شبکه فاکس‌نیوز شامگاه سه‌شنبه ۱۷ شهریور به نقل از مقام‌های ارشد آمریکایی گزارش داد ارتش آمریکا اهدافی را در نزدیکی جزیره خارک و جاسک هدف قرار داده است که شامل نفتکش‌های ایرانی می‌شوند.
فاکس‌نیوز به نقل از این مقام‌ها گزارش داد، این حملات بخشی از تلاش گسترده‌تر آمریکا برای افزایش فشار اقتصادی بر ایران است.
مقام‌های ارشد آمریکایی افزودند این راهبرد شامل غرق کردن و از کار انداختن نفتکش‌های حامل نفت خام ایران می‌شود.
@
VahidOnLive
خبرگزاری تسنیم، رسانه وابسته به سپاه پاسداران، گزارش داد که یک نفتکش کوچک ایرانی در فاصله ۴ مایلی جزیره خارک، هدف حمله موشکی ارتش آمریکا قرار گرفت.
تسنیم نوشت که این نفتکش در محدوده لنگرگاه جزیره خارک مورد اصابت پرتابه نیروهای آمریکایی قرار گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78282" target="_blank">📅 22:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78281">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRdkTfFsug5Mk_noFnWBKoDtR4B4yZR5YQlI1VM_O3WGqBE_hnj87d3pewJtYmkO0HtGYKa4S_3lKKAjDBOaGf8bbPjklVkWioUPV7IApDVdfy2qshWvOmocKlKGSbFHZq71xYbCTS4AtBYYmtajQXidWXIj1mMPH5OTXC17uASYjGhobFEYd_kbNkv7VToqr_niOKWSYDOXbU3LWLCa0DQXXxu4eQnIjPoNzYq9S-_vdiq2T-nfU0JfA4svHb6B1iao5OhObo0k9l5lRjbxA0Zn6sJOIy-uFyTMaypmgVJlCtJz5RYOVpxVdSH0l_Wj26I3TxviQaRX4_8ovnJ9rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، روز سه‌شنبه ۱۷ شهریور اعلام کرد ارتش آمریکا به سه نفتکش ایرانی اخطار تخلیه داده و آن‌ها را به هدف قرار دادن تهدید کرده است.
عبداللهی هشدار داد هرگونه حمله به نفتکش‌های ایران با واکنش نیروهای مسلح جمهوری اسلامی ایران همراه خواهد شد و پایگاه‌ها و منافع آمریکا در منطقه هدف قرار خواهند گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78281" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78280">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">"صدای انفجار از حوالی ساحل جاسک"
خبرگزاری فارس وابسته به سپاه پاسداران:
حوالی ساعت ۲۱:۴۵ امشب، صدای انفجار در شهرستان جاسک شنیده شد.
منابع محلی می‌گویند صدا از سمت دریا و نزدیکی منطقه سنگ سیاه به گوش رسیده و انفجار در دو مرحله و با فاصله کوتاه رخ داده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78280" target="_blank">📅 22:42 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
