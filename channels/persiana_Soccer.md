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
<img src="https://cdn4.telesco.pe/file/ByJo-9dl89Khdp4gk2KH5hMFuiT452PcrZi90zHfIs75IwHbZB6rYJgkT6DzNhuVUQoDv832gkclwpTzaX_cysIlIBR8AIPACTNcGXlJybR-IsGuR3Xe3ti0whTYux6uUjSzM_lIfb5wacgCk1lC7CbfBBSBG1aIXU4iPCbFZg9mwI3QifZAYkNM20cAViU1OOjuFS_VXvdHPPtJ0leyyzOWpPPBNcDr3DCxXfqRpYqcgJPFWZBhRBgnVBgF3RyNVTuOt9jCPuheSRZJeM3isMkzZeklhwwGCjVg5NVQfu2iuTiS-3XFjc08PfKdr-V7Cpv8labVVcMU1yaJz1p-Xg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 246K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 13:31:37</div>
<hr>

<div class="tg-post" id="msg-23433">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=IcbMK3ogAUvHkVPV8SMrk6h8CQC9F2CLOe0FVRLgEiY6Yb8MGJ5qp10qUQ_fDOnP5yapOASKMjJGdAIPRXZL0U0grF5kCVpqoMdHyiLDMwlT8O071vsLTXoAhiF3DEe4paiLcXfvhRbKqXHKEO230WHRO9chlDChjTZaBkIikuBvR2fVx5B69FtMq1tZ_cpuNcipnEu34ajH6TRGbADQFmjw__oaUqCz9y2YDkcq0_GemjY2OgsZDfxgzZUdIlnLzFNYsxnOqZZ-Fj24qOIRHnm_X6b-wCwwNPEG_8Ox5G4JcM-UTGUW5lqVB2hj3A5cMCLRsdRQFKMBzwNObitbqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=IcbMK3ogAUvHkVPV8SMrk6h8CQC9F2CLOe0FVRLgEiY6Yb8MGJ5qp10qUQ_fDOnP5yapOASKMjJGdAIPRXZL0U0grF5kCVpqoMdHyiLDMwlT8O071vsLTXoAhiF3DEe4paiLcXfvhRbKqXHKEO230WHRO9chlDChjTZaBkIikuBvR2fVx5B69FtMq1tZ_cpuNcipnEu34ajH6TRGbADQFmjw__oaUqCz9y2YDkcq0_GemjY2OgsZDfxgzZUdIlnLzFNYsxnOqZZ-Fj24qOIRHnm_X6b-wCwwNPEG_8Ox5G4JcM-UTGUW5lqVB2hj3A5cMCLRsdRQFKMBzwNObitbqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/persiana_Soccer/23433" target="_blank">📅 13:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23432">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=iMz2r2UbAJymHHwCo7i2h-rCGPFNYbPPpL6Lb3plPAE21WfLIStXJmDpburF4nEP6E2VmLewWulXgrQrvFPyhTcSFAAweOcFSvsAat-QMlksItU7mRQl6xeppl09bCRlOXzqcaxpcNdpZbYSBcBgDec_R_OXWmE7E6yVE3lhVOQ6UBdd8p_tLt7awtMN3kB2fbvjRuh3hwRl07VWJrFhvlhfyKs7cg2gnrvtKBGiDgrp8iqXiJVU4owGkbS1f5zxt84h97RclknZU3TO5RXFJAjpGZnff-MLSWsPLezxoi01EbFFTiFDqGYefvQ41xWFdM0F-F-Hbrz3DgpfR9CNCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=iMz2r2UbAJymHHwCo7i2h-rCGPFNYbPPpL6Lb3plPAE21WfLIStXJmDpburF4nEP6E2VmLewWulXgrQrvFPyhTcSFAAweOcFSvsAat-QMlksItU7mRQl6xeppl09bCRlOXzqcaxpcNdpZbYSBcBgDec_R_OXWmE7E6yVE3lhVOQ6UBdd8p_tLt7awtMN3kB2fbvjRuh3hwRl07VWJrFhvlhfyKs7cg2gnrvtKBGiDgrp8iqXiJVU4owGkbS1f5zxt84h97RclknZU3TO5RXFJAjpGZnff-MLSWsPLezxoi01EbFFTiFDqGYefvQ41xWFdM0F-F-Hbrz3DgpfR9CNCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شهردار شهر سیاتل اعلام کرد که ورود پرچم‌های شیر و خورشید ایران برای بازی تیم ملی برابر مصر مجاز است و از ممنوعیت‌فیفا پیروی نخواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/persiana_Soccer/23432" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23431">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXyzXSFLLh9SfcpT6OnEsKWLoMf4KNaZgs8EWmNFfyXSD5xlcQ1I3RMliTyBD_AWGmDO-a6hyERp-aT7i4_KErBqhKiC1FqrA45iji_SGI7Mnu8EMV_IjJWl_Deb7vxRR4r9QVj_yUjJY5xCjKfpnKchNaTqfHJu4Odn7tR5Nx_V2A-GJTAA91J2ZakGG4ukT-bePyHBhgep5RpjbCf-wzxBHGUDN2Hom2LMvqXOfBColtUBPfb4LTR6HhwP4m8ulap9xR5zT4chLsmdWkvNlM44FrddReGMvbzF246vEwYwAO4yMDnftrT2jwjeROg97pEuCURYIZI7_Ut1lfDpJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
حرکت‌ جالب‌ و زیبای فیفا برای جام جهانی؛
تیم‌هاییکه‌سابقه قهرمانی در جام جهانی دارن، لوگوی طلایی روی لباسشون‌دارن و تیم‌هایی‌که هنوز قهرمان نشدن با لوگوی ساده وارد زمین مسابقه میشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/23431" target="_blank">📅 13:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23430">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKWcPK6UeeUUeAWm6WIVzVArEJsJMI6pbEfrYIjj02fv5s1qyWaiEftTF_0sGjckB0xAWvTcIjetk_GC2l7kJkk6JmM9gN1WSdyY_3Bx1rhZw-Lrdo73NBIOsHWbopLo6Vo9ca5XPWUTUoKb-8jPgLNbOP-v8ZGfzTuhqgYy7ekdXPGXpzt2bYAOOdXdBbiobHt0vd0S5YWFonQi4YWCS_mPNk7dvs70eCsmMxI9qieIRrLNe71bsOpVD-BaUi8Z2rrt6Q2lnSmnXE1sQh7q-xPVNUxK2Y3NIEt3nbLlOBg0s9Ru2tTrGyLFQvWkIYwQEsMPvLmNR4yfA72zhIDd3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/23430" target="_blank">📅 12:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23429">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=Spyl_BaHjAvsf8bpPeSQxBFS9JWL0Sx9OFzwDFMJnW3RfBFfCMqsK46tiwtexnT4EALhSwDVI8u9gg3DeMup6jOMO925Ipt4wxmNLPqMxKfKBBlN1WC-kQVSMFRDKVyFjnbkducDQpk1Ks3DpLWW6mmjBEjRghXM6iYBjR5T9oLUOPBl6tpB0g8YEkr5RWpoNeNKce_kLtXTqpk5NIgYh-iMu1gR_QoBCPLySQ2o6O6_h6q5Up184xyEM4rFJ__05IFphb_vaNkP0JljzQuaYoZinb6da8FbT3fEhzF7zOHUEveL7CoS_Rxxd3zixCcJcExtxCq7a4wb-XyXViKTKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=Spyl_BaHjAvsf8bpPeSQxBFS9JWL0Sx9OFzwDFMJnW3RfBFfCMqsK46tiwtexnT4EALhSwDVI8u9gg3DeMup6jOMO925Ipt4wxmNLPqMxKfKBBlN1WC-kQVSMFRDKVyFjnbkducDQpk1Ks3DpLWW6mmjBEjRghXM6iYBjR5T9oLUOPBl6tpB0g8YEkr5RWpoNeNKce_kLtXTqpk5NIgYh-iMu1gR_QoBCPLySQ2o6O6_h6q5Up184xyEM4rFJ__05IFphb_vaNkP0JljzQuaYoZinb6da8FbT3fEhzF7zOHUEveL7CoS_Rxxd3zixCcJcExtxCq7a4wb-XyXViKTKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های‌ابوطالب‌و‌قیاسی؛یک رولکس که قلعه نوعی بهش وصل‌شده؛ عروس‌دامادها میتونن با پول این شجاع خلیل زاده رو یک فصل داشته باشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/23429" target="_blank">📅 12:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23428">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT3peM-1W2hi5-1aSCF9h11YHou68S3b3KS-DoguSwS3HPaMIyEfw7D10Kh8PJ3jZZJxCaF6KHgC0D8hCvTEP8JHhXPBERxj4j5r_qHWGFkX4JmjD9YVSJLb1LOzHLAGyuxzvACy_hb6dFswBdjvftpYjDhO4ZkcUELkcg5u2xdXL1CFX9RkfxpDsS6aFm5Qxrmo4okMhMdyBITEERvcAnlvLJvMEjF1jzQvbN-YdmLSrYmwzsjyWJSLkH1zh7XgFnbYJlO_gtvL9QvXlWONZYxyMGGRhYUmf2XN2XO8TVse2T97GKYlivD2IpV7u-zUgG4BAzh1EEWCEW4D7JX3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/23428" target="_blank">📅 12:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23427">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOlLB_FdfY_0biRmEOkhJ6BCoJwwExxARYfbFaQoxh0CrmXbDT8LUlH5a3RLtuiZGXVmzBe3wgZzGJWZHu1mg5AzaoO9YbLvaBxglA-xEkjNPfqo866-DwI9vQqXJH5CsOn5-BzQ3UXhLfN8ALypPln2RVJHgW7ARJEBtasW8IHVWgR6Yl4wrKPSgdDjqvyFME8yqh57pldnpVbdG411Xk2FUeDtGk0fazusAZFXuTNstW-jpS_3EZZDg0nvi1FXhlL5So9HxZu8JfidjzoK2PWw8ULVD7hsnlxuSXqI3QYJwa3Wkq-IiQP0801eMevz4zkEtF9mDYbwcTb0mSZW1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇺
سرمربی‌تیم‌ملی‌استرالیا در حالی تو ترکیب تیمش مقابل‌ترکیه ۶ بازیکن با ۲۳ سال سن یا کمتر به زمین فرستاده‌که‌سرمربی‌ایران در لیست ۲۶ نفره‌اش فقط به ۲ بازیکن از این رنج سنی اعتماد کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/23427" target="_blank">📅 11:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23426">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kxhj2zFewoguUOKO8M84xkUs9dbGerF6ITkEWS7nJtE_CLLSV8_PMSZOXM39eOJQuL2OG9rTc1uzkmUUL_FHaWVyaW--_HwWPBatfZQhCSMgUyfgpD5mjx5qEs9S5GBgvy0TO05kPvgFuieQryiY3Iyu53U1DqOduiklTKlNVV5CUGirzxQr5zhdpl2QiqIyC2ZqeEYc9IBU4gByXj4hDnk1Kc4bwICbrw5QTbWIGpVNHoLnJ6f6pCR57tMVwZqbvtyx_AXSjlEo_1izpF7NmYZbYcUE3lj6kJhgh8bM0ViSTNRP3fH-iA5bY7PPMxpsaw4xOpoRbGndGl3fRiL0Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/23426" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23425">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQG5aD6ByznKVPbRULvJVm0De31aazr7jn-mpOqi5kdIDpt0shR05Jxz6txf40kGxMTQxsbouU7xS9c8wKsCUMYOP97QGT1ZIT67R7HnoHpxqQgCO9MkapYZRern51WRf6u07Eao6mvRamNdY7ixH4Y0BYKuGhROuDfKBQd45c9ET1A6A46yZQaOG-O-c6LlfiZssqrMRJqBIOmoUgCSft4CN-UjCEdS0igODQiSkLbxWbCIlPmYIWcoiFXTeotuW_eFTwEBsnNihOOO-c-D9nhTRyLds1L0dYMk624GaFBYDZ5gWKYue_PdEXdNtlwc4aq5R7DByvuhV3KnBSRhHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
⚫️
#تکمیلی؛ روبرتو مانچینی طلب 15 میلیون یورویی‌اش از السد قطر روبخشید و رسما قراردادش رو با این باشگاه فسخ کرد تا ایتالیا رو در یورو آینده به جایگاه‌اصلی‌اش برسونه. مانچینی در یورو 2020 ایتالیا به قهرمانی تاریخی این رقابت ها رسونده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/23425" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23424">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QidJ5Ts0KNnMDIca2CkVUSLehtQ1RhiobW3km-8cJ8CItQ4X7n-Gt3wn5OGOgRlYHPNg6V0OHmXi8QXwYvAbtfSU5jq_zMaK2BgsdyBPeSI6rovNsQFgP471-UOKgIEqIGWFvBXxLwOcWSiBMFh29CNR3cO2zkrdpPiEbZSEJZQ2BkQovRFm4bqs7KMdij7JN-nH96gursUZVcFOk191_apRM_9QFU-UVvFWakho5Sq_fjeQPI-ZFm9CX80J-xrlemu91M87Yn1OtluVyvRfAub1jSygHQ0FGdbaHun_DLKC3_6prG6WyJ4YIZZ7CO8KXzj-_TuIgmU5LClSzbxnPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/23424" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23423">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lgKJqTdNC4tyrdyhv-qahCM44pXIi3jpGuvqJCbxhAsSGeGagDkQL28qHkDLndoqDDnWW8fpsXweET3PaNqRbe_YkCCBx8VzFvyDvKLRN6_gb97ky-KANkOZKNFtIpDvLUcx2E3fgoSFugJT-WU6MBMrtAUMTOgZW_loKMX1jQaS6r9n1mriw8b2RiShJk4cWmdZboLmZdfzJETqY-46N-7-xcHrfopull3aNuDW_MR9fJT-4NeYrfYKsFs6BcUNRhflXNWr9Bjd1ZsWuMnLZ9wVwNAL1HMZOimddHOTeldA6-65wYdl2cDeDJ2nTsv8QJfezw9Oq8He0-iaxjIHuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">MelBet | جایی برای پیش‌بینی‌های هوشمندانه
درجام‌جهانی 2026 هوشمندانه قدم بردارید و روی پلتفرمی با اعتبار جهانی پیش‌بینی کنید!
🔥
امکان شارژ کارت به کارت و هات ووچر
اسپانسر رسمی جام جهانی
پشتیبانی از زبان فارسی و کامل‌ترین برنامه موبایل
قرعه‌کشی و آفرهای ویژه جام جهانی
✅
حرفه‌ای،مطمئن و درکلاس جهانی پیشبینی کنید!
📌
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌ Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/23423" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23422">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWW-JB09P-7yAESSHmL0vID6Pc_On4Lfywlju6z8yboScAAn_LxdHvr9yD-8lRpYuSAtgnIBb_kq1C-qOINgXKs_Q4OjV5SH40wn2jgH2BOiGowq9MKMfGEPLIjayJ631RkJAyXXvHviMGulYlpADIE5UCUDBKhqcxTZc12_boTEbNA9blqrf0h5OdUBLQT7G0YRp6imki5OGOTJAkl4cl_rYz3uu-fQs_3IR9o6gBGsr3Txnt3v6_N57EI75gXTpWR-cWtlishwWtAxlavqKU6QUT9-eQFvAbonIWKPOx1deR43TxdvSaTYAFys8EMNzBhrIBRtQi861ZE8FkLRdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
طبق شنید‌های موثق رسانه پرشیانا از نزدیکان کسری طاهری؛ روز سه شنبه کسری طاهری بایکی‌از دو تیم استقلال‌ و پرسپولیس قراردادش رو امضا خواهد کرد اما فعلا رسمی منتشر نخواهد شد. همون روز سه شنبه ببنده درجا همینجا میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/23422" target="_blank">📅 11:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23421">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJo_F4ZvivJCBfoVYPHhq9SC3ks0nd5GEtQKj5UT7JN_5uGhh8YZypHjV4BMMPyP_nIkZgSi7Y9mR2GSyssOqjycr8Xq2SXUrrgvDLQnRaMnFYqZihaz0HhpHnmcl9029GSIm2yRkNM18AZRkMywQEkWzhUp5GxdsaHZtHVq2jN1ljwfxCpUwQh-GkRZopOoAx4YYLLc1IMH4bY4nySDu1P8Sr0mOURbvK1SrMoACVwTjIin4ROJjYo649KDthlzp9I6zmZYgT4IllpmddNpGtx089tigiaHe4oLW0xnZhr0plSrSseglune8xpgEysLISy8_5Ncl0Fqi8InxsetCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C و D رقابت های جام جهانی در پایان هفته نخست؛ استرالیا قاطع و دو هیچ ترکیه رو شکست داد. اسکاتلند هائیتی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/23421" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23419">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/je47p3uSx0Spdm9Vr4OnUc9AW_XH3jGENSjNjvmP6zCz1E-y38cOJ3uMh3HaheCsdbkKVXrib-bW4qw9Ppvsw257HQlL2tVt0kvDfGVFXFITi87J04tQMl4EL8eAASAkANXwiGXzo8LGhMn3gYr8Cg5ND9XEXj3oy6w6jh03ThhZSHnvoEAMp0mOBZjjuU9WAZ8Ym8QV3NKHRjPFakmQ4bLTWnt6lT4dj7ACZ43Y7Ma3M0KeRRJ-kx5HBdUJ6jWxYHS175XRZ6HBWXrdZYo5iQE45An14TsZtKGzdr9n30kNScDzbig5I2kPZStY9rn0g-p5nd7CRzbbe0-QK7Znug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Np_g05i5rO05ZUSnIW9_CBQdPhkmsQhkxOaO-th8Yums3TyJNYscw3bk3EESg6Fu9npa9339TAonpo8v26BDRHsDZOL5Ccy6w14wpM_XzmGMfSNDu0QcKKcxW56kavsUj34jGq9UHunBf-8rDxPVzdFyHlZmywF_PDfDUT4DiV8j0BFUQbot-GzePCBAE91ofxQzZL3ig4lLFJvDEDs1hDk1JKUwUSNazXmDmD9wPmsENtwAJspIm1kgOhPj405ZEehMrEMFszFFlkpautbSf56_hjv2QxoAUICfsJyPFhJhlCZP668QvMZilk_QeY1yv9_zaTnvlFnh2hW1ocmaNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی کاپیتان مراکش: اعتراف میکنم که در نیمه‌اول روی اون‌صحنه باید اخراج میشدم که شانس بامن‌یاربود و داور ندید. لیاقت‌پیروزی در این بازی رو داشتیم. هیچ موقعیتی به حریف ندادیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/23419" target="_blank">📅 10:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23417">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSUh-_ql-If-4KjbjqH_kiWUWFdfofjAbXVfvMUMnuqXNRRGaHgWYsd7tpsc0zk1HRvCFokdg6Fxp2KrdK2_-G8y8Rjyp-iOIBK0cLejzaopKZ_3G3ffhgMhe-AkBrMlUHEAAaCfWOotut047DuIIbsEBOCkS98kfvBgAMb3VxDx5itwE2_h7cUGUoAYpRUzk0OjTXFWpthEfDHellvTPxRNz2LZUqastHkJ5SaMU5QhrZQf4HqRt_T8I2sVK27q0xQZBrJpV7J3BPbBaX-WM_PfGDtyVAihZ086CHnzHH6roHYYyJkWW4ZdMGUBrrDvdAkX-LbLKW1-VrsJEwMygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=AzzjSC-PcHJEt_hRyxcY45YB5Mog0SwahDFePmpu2mdCWTeHhfFDXbi2ypEwJQ7_h8hXSJmiMYX5BoaJRF-gFTgtyI5ZzHmxd021231EFq1IZvGFxliGDgd22_sy9KoVUYoF3hfREOUGVMiM95C1dWmUUVVITv71oaJ00_K_7rT2bhlMMmbwzWdLNhRZJkdIM-GIooB9dY82sawA5Jn3UrgP5CIv66A6y3j1l9GohKV9zxow2Gaf9iiT18T5wQOmdZUbIAGuiuPrRhECYV9yzNefX7bPmISRLIOhDUI8L1YO06vkB_qjZCW88vYY7Hst7fj5gcS4p-g5p3xkdaSDlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=AzzjSC-PcHJEt_hRyxcY45YB5Mog0SwahDFePmpu2mdCWTeHhfFDXbi2ypEwJQ7_h8hXSJmiMYX5BoaJRF-gFTgtyI5ZzHmxd021231EFq1IZvGFxliGDgd22_sy9KoVUYoF3hfREOUGVMiM95C1dWmUUVVITv71oaJ00_K_7rT2bhlMMmbwzWdLNhRZJkdIM-GIooB9dY82sawA5Jn3UrgP5CIv66A6y3j1l9GohKV9zxow2Gaf9iiT18T5wQOmdZUbIAGuiuPrRhECYV9yzNefX7bPmISRLIOhDUI8L1YO06vkB_qjZCW88vYY7Hst7fj5gcS4p-g5p3xkdaSDlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
برونا بیانکاردی پارتنر فعلی نیمار جونیور و کارولین لیما اکس میلیتائو در ورزشگاه بازی دیشب برزیل
🆚
مراکش درهفته‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/23417" target="_blank">📅 10:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23416">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eb4mnne2MDT6UvMKT59BenLoWPaWozRWtxJRwzLQI33aJBNxLGl9i_eZJIECFpZjUDA1As-Tfxzu977p7SrGihs7CdhklMZHXfHQZBQhpm0l3eVJFq-y4EigsUajZiE4bOg-rGAqlldHjMlgvJO4ZeUe1wq7mLAzqTMuneX3fALPJReq4kUlg76M-siDCg6eyjmDWW5WLKhwTZzAojbEKJehBzwza6BfZn-_3eNL5f307NO86PgEo18BJ4OSo5IWf1lRrkHBdsx0mVFEpa2vByNYcnx55HaMPv4vb0Vt8rsb1WSbGop2JSFTxgZF3qeUMTgEfiH-Nn32as1da4HuMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ازکهکشان‌اومد زمین بی‌بال پرواز؛ مثل شهاب از اسمون اومد با یه راز؛ خرید اونو قصه‌مون شد آغاز، امیر10؛ ابر قهرمان جدید ایران و جهان
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/23416" target="_blank">📅 09:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23415">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=KPibLAMiQFN5Q5WVmyccHrPzywTokm76DN0qUdz2-J2ffhivMaYFW17gI9pp2caMb22zrnvM3YUx8igC8HiY1HrriA3ViKryTL2XnzgrMREwJCJ4yZkYmtQMPMkiq4RnHNqs_KJhQ8fb7w89ymhyvXm4N2gvmFTpIv3ju6TK6OYAA8-yYI_2VqlvPywlJbaqlW_GTkpndp_0530205gAwD7Uxod2mOSRF251cLlqG6TCOaVI3rCYeISMAPMuzryZyatk3FGnYVZH7pqSjcNOCCqk2f_bLXkC3N6E_dgBDoR3y8PNd36UET7g2fUS3s_bX0Lkxz0D86l3r7phaxQ75A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=KPibLAMiQFN5Q5WVmyccHrPzywTokm76DN0qUdz2-J2ffhivMaYFW17gI9pp2caMb22zrnvM3YUx8igC8HiY1HrriA3ViKryTL2XnzgrMREwJCJ4yZkYmtQMPMkiq4RnHNqs_KJhQ8fb7w89ymhyvXm4N2gvmFTpIv3ju6TK6OYAA8-yYI_2VqlvPywlJbaqlW_GTkpndp_0530205gAwD7Uxod2mOSRF251cLlqG6TCOaVI3rCYeISMAPMuzryZyatk3FGnYVZH7pqSjcNOCCqk2f_bLXkC3N6E_dgBDoR3y8PNd36UET7g2fUS3s_bX0Lkxz0D86l3r7phaxQ75A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نگاه عجیب ویکتوریا همسر دیوید بکهام به تام کروز و حرکت عجیب‌ ترشون؛ درسته ما فرهنگمون خیلی متفاوته ولی‌همچین‌چیزایی دیگه مورد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/23415" target="_blank">📅 09:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23414">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxyyPlQhTTpB7p1iMeDoZN1IO3N-kUU67Kbdbnzp88DxDW8Km6iS4nqDkOaYJL5dw6rsXPRL0qN5UZTk2x_sLpxX2nbO55-fz7OzHy320OoyQgXaLJVG1wTuQDOjqc1WwXj5r-tva0idFAwi6uLNBPgjF0MOK2IbC2p12x3-vad_0okGSbPDl_J2IK7ZrI2jdxTuazyR5MhAubMtd7aeNmHmETsoO0T_gokw_CZHFRUL8_Hewj8pM9hjRWKgTfEX9rzESZkN058KLnhrNWkxmvjcC572kIChABgbZgkGwkG8yrdtwZSmDUZzUpxJiX1f6koQrvLdMmjlG6F02urk-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
درحاشیه‌تمرینات‌دیروز؛ بازیکن‌کره‌جنوبی داشت وسط تمرین یواشکی از گوشیش استفاده می‌کرد که یه‌نفر از کادرفنی این‌تیم اومد گوشیشو ازش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/23414" target="_blank">📅 09:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23413">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da531b194d.mp4?token=a2UJ7uCFxgU6F6ouE_NnwLDCwW3StWul6boDBeShMwYpwlU7bNhNduRQVM8RpAuJEJfRWY0YCYPopifph8h6Ke8Bv_DOHyoF19pChv6VeyPsenR_EvIwFJSuw_HyaoS760spMNl-NCZA8zgxzwgOOcaiUmKgvcKz70X6BNMaLs9PzvDHDcx0is0vJFQ2cpfc8VpcTffgtbzJ-nNmbunVbTHaNx0YRPSDvbUp_g-ogjDO7Vchct5947IfNutw8q_FVK4n0Mrlmb_yMR6IlbV1BPq6ieokrLuVMACQvX9-k6YNH5gfoBS0i4OQU1Yk5q16Kpe1YeY0QWelJPupDSqoqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da531b194d.mp4?token=a2UJ7uCFxgU6F6ouE_NnwLDCwW3StWul6boDBeShMwYpwlU7bNhNduRQVM8RpAuJEJfRWY0YCYPopifph8h6Ke8Bv_DOHyoF19pChv6VeyPsenR_EvIwFJSuw_HyaoS760spMNl-NCZA8zgxzwgOOcaiUmKgvcKz70X6BNMaLs9PzvDHDcx0is0vJFQ2cpfc8VpcTffgtbzJ-nNmbunVbTHaNx0YRPSDvbUp_g-ogjDO7Vchct5947IfNutw8q_FVK4n0Mrlmb_yMR6IlbV1BPq6ieokrLuVMACQvX9-k6YNH5gfoBS0i4OQU1Yk5q16Kpe1YeY0QWelJPupDSqoqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23413" target="_blank">📅 04:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23412">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCS7yh9mGJu26UlEa8XBTzFOZuyRMBuX18-tF4hT1DYtF3haCUqcJWaaKaWzq9yxCVkPq3Z_PwNHyAXr88VaB0ZMIiinzpK2hWDojUyP0UtQGJJHPX_M6hEpQGytNgdI-pChgrCG6sYmaYyit0qzIFaRJpqn0XYhNTcfCWaeCl_8C9_uebJ9KOL8cSy1Hqgd2dKtr28HymbZE1G7T0uCsRw55TO6G6Q7QN-CdGprtyZgsYUvklU3fSZ2PFp1d0u5blaBnV75n8KvYgjuAo_8VxJPn6RgNfsLqvoMgQ7cmekiHRHsnlj8FPLPwIvwFbaqJvRSm-KQkfR5LQEIeG1nOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23412" target="_blank">📅 03:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23411">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی برزیل - مراکش در هفته اول رقابت‌های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23411" target="_blank">📅 03:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23410">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/23410" target="_blank">📅 03:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23409">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlEJExQPY8SEEAkLVeCZg1xHU0VfVw5DiyP4UO7CLY88izxMmi9n4s4gF3e1tB_gDQyF90Ho-sugYgUD_IM76cnM5xd8P203PdtslasP1xX-OX9hTB1p_qd3Zgu-LbIFly07BoHFryCvJeZ7ru1IwMUvAZIYRS-m7tNYK5Sv0jlxWwFcQ2_biiZbpFjqpgpIBjR_LiqKMdsCsRGt_o7SMhupcBbJIDbFn5KrJPezONZGwGxCdyW9tewOYY-2WGCmqT7v2FIFLQ1wovOreTZQWDusfyWKzS2yZveilJ4dCfWARpeotzUwv05wCkIV7EVEJsdKCE7cFuOyGg3j4i5ZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/23409" target="_blank">📅 03:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23408">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858efb6719.mp4?token=jDvKGaUDDRAMyT-i3bB0qiIFl48Pbofv2zDSD7ImuR420dH66qiVTIBPKljRuH039pp-_LJo7MOmzi4KAwffTcBzOpHy8v-x1XO_rtb7m4QVRLv8nnXZth4n6VVrDcWF05oqHu8xNvXQLuoJwZFjQx918nZ1ryx8nKsryyv9S3gsqUSythpTcdMFEXpBtHi-Axq6M6YjncYI9bujLNY0CbRHyMMFLm0mp83FgOwMW47viN9E3lfAGXDnm4SPQaQfEXxqjcKwgNykFQ6Es9Gvxs0Q7CzTEtb-rp4k-ExBBxF9xpAIku2gr54CngkQRCbYsO3vOIAykl5IJMWiZSsspA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858efb6719.mp4?token=jDvKGaUDDRAMyT-i3bB0qiIFl48Pbofv2zDSD7ImuR420dH66qiVTIBPKljRuH039pp-_LJo7MOmzi4KAwffTcBzOpHy8v-x1XO_rtb7m4QVRLv8nnXZth4n6VVrDcWF05oqHu8xNvXQLuoJwZFjQx918nZ1ryx8nKsryyv9S3gsqUSythpTcdMFEXpBtHi-Axq6M6YjncYI9bujLNY0CbRHyMMFLm0mp83FgOwMW47viN9E3lfAGXDnm4SPQaQfEXxqjcKwgNykFQ6Es9Gvxs0Q7CzTEtb-rp4k-ExBBxF9xpAIku2gr54CngkQRCbYsO3vOIAykl5IJMWiZSsspA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23408" target="_blank">📅 01:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23406">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAN7-mz-ZHNUhWPvizZBEJeYf1ieLq-atVzOfX4RHp2rPwTmIDSPPmbxSxDF3xlR9T68IcX79LEBXd2bOIOal8dYBLebitYUbEJHdxz_Vas89tgpd0Ck38OJTA6kjL2O51BrI6X6RSOnn-fe5G3IWRF10cRh3CmQKyDCRxKQFAaZMBBzcsVgcXlyeEAsUu7XzN1_ALojBTwNYQz73LCmNdVkYuFQ0wPQJxz1iKJmu-aH3LulgCYWxr3yPJPfpDAzhyjIi-YHkDYXUjmXwygSmRc0ZIsrzkiXtJ9_BMvXp__Z9I-gtfqt9n4rKH-lcXrTLmJeeDy-MPPG4qWcv58hOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23406" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23405">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLfWNDOYzWu7ijCi6TyT2MIuNoGt5CkRMUVEfX_N0BfmOf4UiGnMk1WGwQ7vXy8uhmGtuVUD4aZQ3-OaA1OwcacrRaoIdwwy8VpGD2dXFue4mb4s_6QPgEZbFFvAqJ8AhgSagtWZORZz2Zr53hkfXZmcVX8PO_RJS_ye2-KSvp5jtNCgZsz86UaJgR-1GGA-Ub6IQ7yQ1qoHIqJQ1jsfd6YSrS5eIWuTP-pXfKysRuUC9vl12keVRGXL0OBOLrVBZvsMTrznW3PLw-MMznWZjvgARATnbLZoguQKfjpzcisTxdFprctISDQdir7JKyWdOcbKpivnn220jqY9XzaB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
از برد آمریکا با درخشش بالوگان تا اولین امتیاز قطری‌ها در تاریخ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23405" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23404">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0Vgr99u2E-t3Um9JP9H8w7qZBSIM-THWeP7B9GyMoZ4q89FO3gqCKKD_jnvOvGzjy5QTs0aHl00Ijv9Aw4YdR2mFcnFDQW0U4sQ7JqhHp4VAGEsmM5dSe8cjsn3qIIaNcj5X9JpzTiaiPDDr_-9wfUf-N2F2ue0wdr68LOM4XM-ebxrmf2CxcfLQkZOqwTNRb8Zlh3-Ke5ZQB6Q0C3IYPYn8BT4D7rMmXc96rblgOX1c7N45d0MZrmYUWCO5LrGyUfn5F12P-1ngjrLnlqL1kbCKteTFw6anUPrxbuSuBpi_DYK70VYzVcTum6uyurL1eo1T1PraPNqM0c57qhctQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
توم‌میخوای‌ازمسابقات جام جهانی فوتبال پول دربیاری
؟
🥇
✅
کانال
ورسوس بت
کارش تحلیل و پیش بینی مسابقات جام جهانی به صورت حرفه ای
🍑
⚠️
توم‌میتونی‌از پیش بینی جام‌جهانی خیلی راحت پول دربیاری فقط کافیه با کانال ورسوس بت همراه شی
📣
🌐
ادرس عضویت کانالشون e23:
👇
🔪
https://t.me/+vEPd1hF2Y38yMWI0
🔪
https://t.me/+vEPd1hF2Y38yMWI0</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/23404" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23401">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-IDtR9uvLoeKJmJl8ME1k22-uatKM_kI5aNHCnzR9OexYkDwgUIAbr5eNdhNP84faB2AkSHaitwm46J6IalWN9z8ajaISNYChPqjGdbJenNUY5h7QW5wqlp__VTyuBlUKWVaj6WBT10KDBP4toxLzSNUgw4UD_zj3WL9IYRCTqt0JiLfPVtY24UNv9HW4vGVwiUp8U-ph5NgECicYhTT01RZqWq8TdEUOACXd-LQJvOQ5yxoRzg51fLGfGr60aRSu7cHipkBLqDpBmZNwi6bosZ0qRqBfVH6mwCFS04Bes-6-YcOi4LIIClRXol8KOmjkmkoS8WovfkdGeXjtd9kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه اسپورت ترکیه: کادر فنی کایسری اسپور نام پنج بازیکن رو در لیست مازاد و فروش کایسری اسپور قرارداده‌اند که نام سیدمجید حسینی مدافع 29 ساله این باشگاه نیز در این لیست دیده میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23401" target="_blank">📅 01:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23400">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=W81eI3_ZThzgqDvlQRbfSrmsK1zTtk11weSwIxxQudwn2O0DgZorzn1XcM7tdO7phZJ_Bzfkdhlgaf8tJwdD7ulpqU0A218bK10CkJOD9UwalCiZADEwg8MiRmC6C4MQLZlkU_xhSDlrhB_NJ9EhkQVLQRQU3K3Sro_Sx-F6X5-KctHDeS9cyXLQwxeo44S1UoYyPmf8KbNoV42g4g6pN6Ku32beBPgNAS8hIbFF4Pl0M352c0vPzh_E-uAJtLXSuHxiCwtYYurjb4Fplww1ov3wbKr3YHbUFNUIx9izmb47WiDgFma1bb_BrB2nnnS3r5i5JP7mhN59zcHlGBm4eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=W81eI3_ZThzgqDvlQRbfSrmsK1zTtk11weSwIxxQudwn2O0DgZorzn1XcM7tdO7phZJ_Bzfkdhlgaf8tJwdD7ulpqU0A218bK10CkJOD9UwalCiZADEwg8MiRmC6C4MQLZlkU_xhSDlrhB_NJ9EhkQVLQRQU3K3Sro_Sx-F6X5-KctHDeS9cyXLQwxeo44S1UoYyPmf8KbNoV42g4g6pN6Ku32beBPgNAS8hIbFF4Pl0M352c0vPzh_E-uAJtLXSuHxiCwtYYurjb4Fplww1ov3wbKr3YHbUFNUIx9izmb47WiDgFma1bb_BrB2nnnS3r5i5JP7mhN59zcHlGBm4eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23400" target="_blank">📅 01:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23399">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
رتبه‌بندی‌کشورهایی که دارای زیبا ترین زنان دنیا هستن؛ ترکیه با اختلاف در صدر جدول قرار گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23399" target="_blank">📅 01:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23398">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evfKd2dGfBMrmzK0ZXmLFFF6Wg5dVOvwbo4emuteJjdYb9y5EfBCOpq_9npxHZpPcDmmx17Q7R3Tp_PzDvaQtWnYxBVGEvdGcVcWL6ikqoANCNdS9XY6no7nJYRjR_d6C0Ts6YhWxit9B8GXWttlqtd1biXNmcjKnkgiQiPx3CLxJ8DtAnEGxxQN5pw2SUw4H4GG0c529LK8d4vmc9ZP3spTB9Qvx2rP0ZGKJqnmjcMigkxr0m06AYIDo08PfjnmGC2U49WnKcNNA69SegdVGImODzdR4gmoHD4faCils8xIttkJVW9SSUGtRPWwQMpsjrLDHbaVfb_hmPkq3VwvSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌رسانه‌پرشیانا از زبان کسری طاهری مهاجم‌روبین‌کازان:مدیربرنامه‌هام با دو باشگاه استقلال و پرسپولیس جلساتی برگزار کرده‌اند. بزودی تکلیف نهایی ام برای فصل بعد  مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23398" target="_blank">📅 00:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23397">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=o-aAS8yLefRS0TTuoeqC6H1UCof5wO5Xr4fZMxIlzGzJK9xlIH1JLcjdzQuFs7_6jjnbAB6vHEnDbbHbOKFzKX724jyoZj5QC_Ad-34WmWxYaLAK6C6RP5x4CTf2ZWppcInvpf84wCsPVQutUen21K9knSiYbfTdCVwDllo_ScbS6Ow-oz1S7vUtSf2C9GNVQsrgboEwFSsYHZJnltbahqc0AJEHIZ7kwF1QYJSZz_fSwL7tMKf5UuIYUL7VxCz1VkA5M-bpMRRqUK0PKpqmeVhNkRvN9NBuZptAoPTMZw-JzcPNF-UaneBJxesloPAvl-3Org8FBtR5d6DZXm5u3Ch2r4C0QoSNzFzqGYwHXjcFETzsK_3ZwbGe4fmx8v-_uhmw5wQsvbfuTE5yTn4dxxLN1IG9oG9aS75HD-uh0bTx4dljMM3Il7ovMyzrFy9ow3Iql_9MPADX0p903wGTv7o_3Y5GvttKKJrYue6_rScdYbJoc_JN0FW3Y6_Zr4nPCZqvCLOMar6Vazu90ugD8DsYjOti38qA3EKLjJ-VFAGYmRrYXXtn6Mvz4PGPDNAMIzV1F3q4IavEZPm8BzRRasjnkJEDZSEBCXw783UMc3im1ntl4rAP2lUTFroUgsQ9ZIjioI_BGAfgpxhV9v7yEtGrfSD0AmD2XVBF_D2qNPc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=o-aAS8yLefRS0TTuoeqC6H1UCof5wO5Xr4fZMxIlzGzJK9xlIH1JLcjdzQuFs7_6jjnbAB6vHEnDbbHbOKFzKX724jyoZj5QC_Ad-34WmWxYaLAK6C6RP5x4CTf2ZWppcInvpf84wCsPVQutUen21K9knSiYbfTdCVwDllo_ScbS6Ow-oz1S7vUtSf2C9GNVQsrgboEwFSsYHZJnltbahqc0AJEHIZ7kwF1QYJSZz_fSwL7tMKf5UuIYUL7VxCz1VkA5M-bpMRRqUK0PKpqmeVhNkRvN9NBuZptAoPTMZw-JzcPNF-UaneBJxesloPAvl-3Org8FBtR5d6DZXm5u3Ch2r4C0QoSNzFzqGYwHXjcFETzsK_3ZwbGe4fmx8v-_uhmw5wQsvbfuTE5yTn4dxxLN1IG9oG9aS75HD-uh0bTx4dljMM3Il7ovMyzrFy9ow3Iql_9MPADX0p903wGTv7o_3Y5GvttKKJrYue6_rScdYbJoc_JN0FW3Y6_Zr4nPCZqvCLOMar6Vazu90ugD8DsYjOti38qA3EKLjJ-VFAGYmRrYXXtn6Mvz4PGPDNAMIzV1F3q4IavEZPm8BzRRasjnkJEDZSEBCXw783UMc3im1ntl4rAP2lUTFroUgsQ9ZIjioI_BGAfgpxhV9v7yEtGrfSD0AmD2XVBF_D2qNPc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛دشت‌یک‌امتیازی و ارزشمند نماینده آسیا مقابل تیم پرقدرت سوئیس در واپسین دقایق بازی؛ لوپتگی نماینده اروپا رو متوقف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/23397" target="_blank">📅 00:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23396">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=tikkuf5VS0yMkKhlFI2fcRQldXIERGJxf529k0mv00Eui4YVLRpkfEQCrvRWmsgDzdvLXv1iLzYdRi1IrL2SauXqh9FE6dNV1_MM4sYDaEUPuMtzCu0oPY_1i9N9QyMN63Vdmmwf9ymPpBevAp5jNNvv3Ew2vQpUgTLNE4kST3vqoDugSW1rHoRIcKXMHZZtLhgGK-yTNujwRDaofw-Wt5q7sOgT1QCOKkOX9nskdGkBG3iU9hEVSZIizyXEBoQZPKt6hFGDV4eAxRL6T9O3m2K-nt8HjDwnaz3fGb0xLNdxB9KDg5Nd1iC274InTIrE8-zNt6jD7SQYudXi3MMxVbMCUQOg2x0ICZK_8ug55Z71V3w9dVMAgjRy-s3loEBy0QW3R-GuJi4APPuR6-2Ar543Vq5tAytWSF1b8gV-IFo1LQxkYSfAxGk5qsf4ZLNruXv2_fvz0HTy5LsMDaqt8IKvGHAG6j70-dQ746bQeIb9x8cFVUhVxhHeqwAoAZ6FOdzNlx20N34gWfj4HFCsbik5hKGlL0RBiNBAWrCk2iI8Wo_6AtjZT8HsLGt5nQHruaXLVROYI1xsGIdRVOQd0p-9_0lrBsus93FuKiiiJQCUJffl28c0L24nhStb-Mz3WXJolXoM9m1KSO4dqSBpyXcTcAdOYPRjzDOI2Cf_Aao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=tikkuf5VS0yMkKhlFI2fcRQldXIERGJxf529k0mv00Eui4YVLRpkfEQCrvRWmsgDzdvLXv1iLzYdRi1IrL2SauXqh9FE6dNV1_MM4sYDaEUPuMtzCu0oPY_1i9N9QyMN63Vdmmwf9ymPpBevAp5jNNvv3Ew2vQpUgTLNE4kST3vqoDugSW1rHoRIcKXMHZZtLhgGK-yTNujwRDaofw-Wt5q7sOgT1QCOKkOX9nskdGkBG3iU9hEVSZIizyXEBoQZPKt6hFGDV4eAxRL6T9O3m2K-nt8HjDwnaz3fGb0xLNdxB9KDg5Nd1iC274InTIrE8-zNt6jD7SQYudXi3MMxVbMCUQOg2x0ICZK_8ug55Z71V3w9dVMAgjRy-s3loEBy0QW3R-GuJi4APPuR6-2Ar543Vq5tAytWSF1b8gV-IFo1LQxkYSfAxGk5qsf4ZLNruXv2_fvz0HTy5LsMDaqt8IKvGHAG6j70-dQ746bQeIb9x8cFVUhVxhHeqwAoAZ6FOdzNlx20N34gWfj4HFCsbik5hKGlL0RBiNBAWrCk2iI8Wo_6AtjZT8HsLGt5nQHruaXLVROYI1xsGIdRVOQd0p-9_0lrBsus93FuKiiiJQCUJffl28c0L24nhStb-Mz3WXJolXoM9m1KSO4dqSBpyXcTcAdOYPRjzDOI2Cf_Aao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/23396" target="_blank">📅 00:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23395">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF1x7gzpO4kemMvKDlpxpcNmP35E1UKJBoJmZCNM0oLSk6woB1URRW4l-p4UQ7GxaRQHvx_UrQu5Xh_1c-bMfTU3rzB2gCm37nWDCHTFhijM5HlBowPmVTey4SL12etWopVPkuSDuki3Nc2xY_bI1q6fUxulgt_Vrc34IWIXs65J-8G8EAw1mL_LgFU7vvJC5og2lmOd5tc93xhjg3kV2mOYS4SazHRKNndXw0fPg6IRoc2KN-mTK8EfO6yRANsTB5T1jSHDDCys2osPnPSd6jU1Bmls0-T9bH-qWC0wOGqtwJTUrdgiEb3fzWKORNCNEut8uuG8A1gmCsJhqoqWoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23395" target="_blank">📅 00:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23394">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpPzHsXvglIOsLO2a9WdVX-_MeRRr-i5ZaAZn-dU-jHKQP1T15mgbCSyPjP6SZy56KT4PrSMcxnp7OtBp-E_79KWci3ThM5Dy8NZZeaHmN0_hsXAU9I_0AeGQSE-dQK4JEmR-QgPcgl1rEbYP6XFLMpXgH3Qyy5FWh315GPqTVeKtuZ1_cbJo5d4p9vol2_AgIy4DW6SRsgSkKo4wDsQzZd-ug6p--GBlNWS7E6XnUX6oYlRbR6ewd6VKPO3ALl7puOi5nz4y0P8y0LYG90jW8LnzC09wGOhvNrShLf65QlxzNNzMuLlUIcRsqtqUdF9KfV6l1SgmOHNujmNJZiTrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خداداد عزیزی ساعتی‌قبل با حضور در دفتر مدیرعامل بانک‌شهر مالک باشگاه پرسپولیس قرارداد یک ساله خود را با سرخپوشان امضا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23394" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23392">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHq40FHuC-KuWeCKlO9t_oZ6bLoEpJVmNCM74Z5nAxToLh776RVQEmpiFupUcrugO2ppL7TQ9RCcQL3L1dIzaE7O2AMa3-NnC31vAlHI7pDxJNmKKZF8m3w755B4obyp3eAGWShIlSeRD4cqZadzVgobBj0V6ammy2Qs5LAxYgOwQ0hdEjAlV_lMkPizyiypz1F_HKOSN0iNjOCjLYE1UmTC_RWLdZv5_7xf9EbegvA4lrpvd6x5OSlF_KACWIEUUNVaHXiWQdUQe4wjRSMKn-eO9D8QhUiioqIG1CdfUg93mVp3caYI1RsUFuQn3y7yKEM1vRIGY5s5h_Ist6l8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CznaUJcx_ezXDLf_PhgDBJCZkyP_MmvYtFwR2HQDHBRX3zZ2n7lIlyvdEkqYYGncLCTwXn21bamEsn3-GaHtvkTun6Dl0L15QLjgkoCzgV8zGmIIFK2AgtKGi6ML9_4Kxsc-n9oCftE83UWldG60UL2jnxcFOsHechL-9QbU08cbfwalFM2AYzX-rHRToytw4hziAXVe38CvkE7Agek2Cb0C1bhFZZB2gwNDEM8Ia_S-RgeCGQSoJlqzTBB-o-jUqjWc5hP3Dt2DJOKU-LHDsm-V-yd1GWx7H9BA6TOLCFQyELMc7bHsWA1GDchYoXizrQYJlmhq0AQKMkKqqzwUtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی
؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23392" target="_blank">📅 00:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23391">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=YHE-4ra-deD6mSHEJxqv5K6nvBfShQGgSSOdlkDg9gyoXSePTMZDQDnTzGPw77SPhvFcTMon8EnkNwdXsTLAe7tuyMFqKw7HD0cUp0J7u5wBIFrFi5OjnLg0NCyvciCcsnLSC4v-yr_Lk4BZD__HddTGkvdyCI7aFCvvCW2mO38TSqu2rG227CaYp4wVk0u8wwPit5nYtnrQHYYJFtdT14X7ymMqQaVsmHENdacmSUQ6o5mvQfJlGXOrj9Fir4EZVKRnMiicx6bxi7L4pj3aPf9UDf9iNuz2gYUeqVO7geZM7zL24R-hderOwzmiX5lJ0YvRxKhFUD_srKEIanGZ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=YHE-4ra-deD6mSHEJxqv5K6nvBfShQGgSSOdlkDg9gyoXSePTMZDQDnTzGPw77SPhvFcTMon8EnkNwdXsTLAe7tuyMFqKw7HD0cUp0J7u5wBIFrFi5OjnLg0NCyvciCcsnLSC4v-yr_Lk4BZD__HddTGkvdyCI7aFCvvCW2mO38TSqu2rG227CaYp4wVk0u8wwPit5nYtnrQHYYJFtdT14X7ymMqQaVsmHENdacmSUQ6o5mvQfJlGXOrj9Fir4EZVKRnMiicx6bxi7L4pj3aPf9UDf9iNuz2gYUeqVO7geZM7zL24R-hderOwzmiX5lJ0YvRxKhFUD_srKEIanGZ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23391" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23390">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roTi8GiT3mIWhCH2chGWiH9T8AHioj8nWKbYmy1TPybaxW-CdySNcDjw0gZa5-3JhEI7AdRgN6FuKnK2Ugjev3d4felVTrpATIH3XWrB2B6f6begyl7-6LN4ijxa9N2zETG8MxWliUerVgrzvixOFHMtMs5v7yjXirVo7Y0e3CtKVWS_ksZQfDCoF_HHHPWUwtbT8n_KrT9FWDUNzTLvm9HaJ39QwGjqA7CnzYiX23L3r48GmwgsZTRwc-c-3780XeKQdOUfpjPtJWewlgrtBp-mOFgEN87td-IRR4VogvWA3lwewQPjDt1pFJvY-IyOpO26ph4nuwguoRoOiQyraw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
فابریتزیو رومانو:روبرتومانچینی سرمربی السد گزینه اصلی سرمربیگری‌آتزوری است و منتظر تأیید برنامه‌هایش از سوی فدراسیون فوتبال ایتالیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23390" target="_blank">📅 23:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23389">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAq3bdhOu_B4_gAzUeYqZdMUpH3zlZMNNCVocODozLxSf0OR7ruGRS4GDq9Bi9YW5BpMiXT9QF9UWIcSl_9-3ma8LDPHqJnQsNpirr4lXgutkOHrbnmc6MDWrT6Xqh4fKQukc0G24imh2OVsBeErxRIwvAnDhtyb1Gg7_YzFA3PEYk9zmsd6l07j-opTdFeiAgT05SESVZoQYmaIbFRWI9u8JGprwYdGxLdn86XVoFc0AnlC9H52oFqeekFd0PekWum_6gnkxH8yesBK-cQU2lDnA2YVZ7B3fZGw9y0RZG2-VUwlE00lcHykRid_nTpZY5IzzZ-DjPf8zVbCDRApdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌نخبگان|پیروزی ارزشمند و شیرین شاگردان روبرتو مانچینی مقابل شباب الاهلی با طعم کامبک تاریخی؛نماینده‌امارات‌تا دقیقه 75 دو بر صفر از حریفش جلو بود اما یاران مانچینی در واپسین دقایق بازی کامبک برگ ریزونی زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23389" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23388">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWJrdSLK-kCALbGvdBRkXdlGv0znL0o6YHiJBTI3zw9s1q-EVkdrKStsWHwJ0xFVEKVfE-q1MuHUp2iK6j6dLXBHLAU1fcKEs72ZhGczmV6JixPgWyxfERtcwI4Gav1PXyYuCV8c4Jdr3GJZh_hRMQ1VZECxtV8YTmC65ZBvMvDR1HIdx-Ii-F8DPHxezRecimHn64-xuhSn40CHPjZWlMmgA0fKJhqrcLwd1VJF5iR_nboH_YIqRo9sftm7CVeGXR9DDHlHKM2o4hKj4O-Ko2Q5BPZM8m6dj7LQLe9UyC9Qwdj2_AfUoIS7IBbv2UJH0PntyCiOhvMVlUk-Aw8FZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23388" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23387">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=qk9i7kP49dnXsYqcfwY3xTcXpFiHfXCUUyK65B7TA2FWc68KihL_J_Fzvv5Q9olZjHWX7PqWbA21z9ZLsQc9ykKd7GUcvk14JOC2S7WI1TqvIxxZ3pDVZXI0cnk4N5qzYQDdG08dmY9nMlB3GJVkiV1RX_-Qvn7YuLQ7UV-MGhURS1H30QcdJaEUtyjFUXOB0vJIeF-k98CWoqZnMHtCV4zsTXEzOobtIeOKX_4kWUnju07VdETDtPywDQTen5iPT9LuCtrpOspEN8a7vjd-gkLjSUy3JKpEHhsv1VSZs8IdQODPjrhVA1N_umlkzLZrYkAL2sJWXq16zkeGXBtnzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=qk9i7kP49dnXsYqcfwY3xTcXpFiHfXCUUyK65B7TA2FWc68KihL_J_Fzvv5Q9olZjHWX7PqWbA21z9ZLsQc9ykKd7GUcvk14JOC2S7WI1TqvIxxZ3pDVZXI0cnk4N5qzYQDdG08dmY9nMlB3GJVkiV1RX_-Qvn7YuLQ7UV-MGhURS1H30QcdJaEUtyjFUXOB0vJIeF-k98CWoqZnMHtCV4zsTXEzOobtIeOKX_4kWUnju07VdETDtPywDQTen5iPT9LuCtrpOspEN8a7vjd-gkLjSUy3JKpEHhsv1VSZs8IdQODPjrhVA1N_umlkzLZrYkAL2sJWXq16zkeGXBtnzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23387" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23386">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3cqZLqwoD5rZjS3PVu1UF5h36KP1NK4szkIcNBhUJAX6W6Ld8p7tEGWjv9lQ-K5Id42T4ZIsuUnsLGPUPuAPS9BruYLis27yRZPNkjb6hN76XjwOqa6SJc6fbmZs--vx_j1zTetzGICXZuQYtQNMIsx6SrtDClMLe74c8bBTrClUpX99rR9Z02cZjXRwaLANHRuo2-AS-TSBbnPzZkkNSIXzBbnRn2EO0c1FlJG60ninj82JY9O0thlZheqxgk1D6aFOHKgWNpX8TuWfJxPUcaoV4UCHO5E3Vd34-ZAByK2_6wQkGssF2OkVMuLvjgjZazq2BiIfjW57jCbSivLmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏کل رقابت‌های جام جهانی ۲۰۲۲: ۴ کارت قرمز
‼️
تنها مسابقه افتتاحیه ۲۰۲۶: ۳ کارت قرمز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23386" target="_blank">📅 21:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23385">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=kdfDD41hKy93_I7Bz80I6zG8F3UohJVP2VwTrEbiCzfx8bL0J_YO07r31h0lhF8TqraCF3To8G5BIfCY9u7sG6owOg4x93DXmd8dxVeXPVXaDQnffyCR4HpQbG3PwnN6rhc4hRNafgLrC5wxlSkOQG3G_HnN92CVO6UAZqjf_Z7GXLbELZo8kJ_dPaukNFbpZGtM3ziIbKHZW4vpJpTN7bYe0YPr86xDeB2FwCe_cE-u5kT-Y4qaib4raF-jBWykvDgPiapBAw9cES9in0ahkjT0rk5IllxSaCb0WuBE3E-BHvsqzIBx6WZXXhS0p6lT25Aq3ddz-dC-zabByfKlvIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=kdfDD41hKy93_I7Bz80I6zG8F3UohJVP2VwTrEbiCzfx8bL0J_YO07r31h0lhF8TqraCF3To8G5BIfCY9u7sG6owOg4x93DXmd8dxVeXPVXaDQnffyCR4HpQbG3PwnN6rhc4hRNafgLrC5wxlSkOQG3G_HnN92CVO6UAZqjf_Z7GXLbELZo8kJ_dPaukNFbpZGtM3ziIbKHZW4vpJpTN7bYe0YPr86xDeB2FwCe_cE-u5kT-Y4qaib4raF-jBWykvDgPiapBAw9cES9in0ahkjT0rk5IllxSaCb0WuBE3E-BHvsqzIBx6WZXXhS0p6lT25Aq3ddz-dC-zabByfKlvIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
شبکه فوق العاده MagentaTV شبکه اصلی و رسمی پخش‌کننده کامل جام‌جهانی ۲۰۲۶ در آلمان که با گرافیک‌‌های تاکتیکی مثل هیت‌ مپ، آمار بازیکنان، موقعیت‌ ها و لایه‌ های داده روی تصویر زنده، دقیقاً شبیه‌بازی‌های ویدیویی این بازی‌هارو پخش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23385" target="_blank">📅 21:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23383">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQXHo0Pe3EhCWzrVsJHe4tYdFLB4UYciiO4hvLctPfBejaIOzqI5Hsmq4wCxAE77mkeA7pIFztQzNCcKXbXVu87mGeIR1Myt9eSZC_Ew806WO3SXsLAWfAZyN4gnDaCr1YC383hvSamc28_QvHY5nGU3plJl0wP-kzWjWsvC444pg6G2zPbyGNrQNN-08MkXvJdyvwMFvySbAYCgmaaCxf3k2Sx80tSJyQtFoS_zFQfEWpWyyBnlj-e0HTW2oHZU5-BUITjX0-RQ6erZIBD8hFWHW1G-HAhae4apweaMU0vWVNu7sVI1zWb03n0wkwvaskV3jOQvCEwDDs6l5uYbbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجید جلالی که یه‌زمانی‌میگفت امیر قلعه نویی از ژوزه مورینیو بهتره اومده رو آنتن زنده میگه تازه بدبختیهای فوتبال ما بعداز جام جهانی شروع میشه. مثل سال 2011 و قبل از اومدن کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23383" target="_blank">📅 21:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23382">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bX97SgTpD34vqIb5nCn5w-QP5OQ4QwLet71K2PhzbldMkFICS_q8owtivc7CIFrADXZfXh0fWrFoi1DjprCsVHebKjLFPG9WVukwDJGaPekPE7YdQaQ9CefIw5spjK7yFdl1-JhLKLdB2EQ6WE0LbqKdTYLpktaCLNP3TPZjy04I-nLuTp6Tz4bRoJbyImQ9ZDDPDEHQkCQyc2wKNruRO07vjYD38Dx_sBKyYatjs9BXa0E1xFkJ2E809ltKlaLl6-Y-NDGlG9u58HaaULkJTqAMXCb06FFTCKz_5hi4g2HS9HxMRq7N61t9SEGW54wMfzx7pXvLOXjS6m42pIgJUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
دیمارتزیو: اگه بردلی بارکولا قراردادش رو با پاری سن ژرمن تمدید نکنه اونوقت سران PSG دنبال جذب فران تورس ستاره اسپانیایی بارسا میروند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23382" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23381">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c77121522.mp4?token=VlU0FkusqrCs7NB65lqNyxlNIJ3Nv00h0FZFYpzNZ_XE2DW2ArYjRbqpsFM0Gt9nwApae8fP1PYc7wm205cmAfZdHmxyaodAaaSHOfuZ0kIkp_XXf7gT2U7bbHdP8Mn6DiPjMo2wI-e0BNyt2uOhDivr-t9L2eOpkh7swydLYh_qMqCUSJGld0tObjv3GthnwyaMlCt6-CyVD5K6JtYo_T9s_OquX0kASfojC-4aIEjCI3ImI-HXNDGaaNurIzojuTbWkUdwnMhCwkNQ3dq0dXSFS2NGq_y2kF21VAvsXOvfk-pwEXWxZUPyGMKMvP-HeINmcOWM82vmf-h5m9ifRIohNVVAyGK_Zt8CK3oIzULfxNI7VVWVyNpmkBFVV1xRaYM17JSe7ODOxzmqIabVwoKk869Ng9sjEP1KOM8029DmBtyL0fqZZsc5-528fJS1wpp3krYSnMrK30Ypdn-hNP_GthwL1JYVmZAqpWoQZiSvz6E7wbzOGRYG4NxztZQ-u6e3UY6cV1BwtRF5ZSBJhQFw03wnP-dKiycHxse9m3TwQiEOzq6bqQLrBJFJYTM-EnVW2_P2UADDcS40KamC06D-YdxdtlZ2gsoCtyotjs09VmQTzNsucvAjWuUGBlCblS1cu5pmsU0MBCbXBTUxFZDPF9RNABsIjZI4lOOzAk0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c77121522.mp4?token=VlU0FkusqrCs7NB65lqNyxlNIJ3Nv00h0FZFYpzNZ_XE2DW2ArYjRbqpsFM0Gt9nwApae8fP1PYc7wm205cmAfZdHmxyaodAaaSHOfuZ0kIkp_XXf7gT2U7bbHdP8Mn6DiPjMo2wI-e0BNyt2uOhDivr-t9L2eOpkh7swydLYh_qMqCUSJGld0tObjv3GthnwyaMlCt6-CyVD5K6JtYo_T9s_OquX0kASfojC-4aIEjCI3ImI-HXNDGaaNurIzojuTbWkUdwnMhCwkNQ3dq0dXSFS2NGq_y2kF21VAvsXOvfk-pwEXWxZUPyGMKMvP-HeINmcOWM82vmf-h5m9ifRIohNVVAyGK_Zt8CK3oIzULfxNI7VVWVyNpmkBFVV1xRaYM17JSe7ODOxzmqIabVwoKk869Ng9sjEP1KOM8029DmBtyL0fqZZsc5-528fJS1wpp3krYSnMrK30Ypdn-hNP_GthwL1JYVmZAqpWoQZiSvz6E7wbzOGRYG4NxztZQ-u6e3UY6cV1BwtRF5ZSBJhQFw03wnP-dKiycHxse9m3TwQiEOzq6bqQLrBJFJYTM-EnVW2_P2UADDcS40KamC06D-YdxdtlZ2gsoCtyotjs09VmQTzNsucvAjWuUGBlCblS1cu5pmsU0MBCbXBTUxFZDPF9RNABsIjZI4lOOzAk0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نوستالژی
؛ بدرقه‌تیم‌ملی به جام جهانی آرژانتین درسال 1978 قبل‌از انقلاب هر کشوریو بگردی از اون موقع انواع و اقسام پیشرفت رو داشته بجز کشور ما که گذشتمون از وضعیت الان‌مون‌به‌مراتب بهتر بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23381" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23378">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n9Ch3YjKdLM382XOzgWN5341kypVoBIGwrzHT0MOOu0DRPjdXxWd9LeQ1a5xQPBP7zEkYOp-tTIQnIBWTgR7O9T1ExMuq6NATRclgw44L3mP8szNzEAaZP5cLaz8WFO5c5mFx4fSwCswX5-VckYQXeBVickHir2WqQ8TKC9qhDtbpDF-hJjQ2Tf9AiU098JHj5A0jgQLqKSzm7AjUWaa6MXmxejJGHl1s6K23oCQ6_4bzrQWGRXzbx_3GgPV9992FT91rkBoaeXBtV3TnO5RqAv93fDFbM6eIl61AuPGOGKTke-ETyIONALS7tVQKFVouFHm2LUdSRViEhbRWvwoeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NUtfMzQN8hzCDafmceMnFYiOuOomtSBIBGh5865G8AL4dfI0r1LpA7xTjbEB1XuhQ5DwG-L0mVsDv-swRDM2KsanJmNzy-u8aHO_u3DjUt712u116ovuoOYCkEY7L7MRzXKP2pD9iODN3SDt7Y82dgQQB3TzqEtUXGPiMPbnRRuU7G80CnrUjMMIrUTuAjdjyL7gMMjJPP13lTvoWL2YCwcGVEjCJ_ea2srA4fBkdThfPF4ZErYW6NvXG8RF9NdkliB7Y2flaW-RIZEdr6GtudXxhSnubjfMBqCamek5vHuH65DfIMuVbzPFXWS-qAHIxn3Gs4szoPl9FlTX7-hPdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23378" target="_blank">📅 21:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23377">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=jBLrwJ_iHZpOQOjUrwXFwtneUEzSVLeyr5rHUEGUdIvK7W8IGspDl4uQcPTAZr1vVf1qOyiEhhv0oab693B32C9ulZH-ZWug7kwcMWDXDGBq2K0LNHDutm2F8oyyeesVFpjidpxscuCcgE0tIwj2sOkDNk-m-9tp_PXz8TdHYC7bHR_Tp7GUN66PDn91CbRqCybdI7xr5gua9uuaW99yDeHPGKfCT2QcWN57CCA2uQFK4lZSvRuIWt3eNK4PotsaU4f02-eqCiblL0rDOCB7xpG1KfW8tXtluEYDapi5KIbxl92oiGfKZXnyJPhrba6fCUodm56W1bJdJ3WEUye2rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=jBLrwJ_iHZpOQOjUrwXFwtneUEzSVLeyr5rHUEGUdIvK7W8IGspDl4uQcPTAZr1vVf1qOyiEhhv0oab693B32C9ulZH-ZWug7kwcMWDXDGBq2K0LNHDutm2F8oyyeesVFpjidpxscuCcgE0tIwj2sOkDNk-m-9tp_PXz8TdHYC7bHR_Tp7GUN66PDn91CbRqCybdI7xr5gua9uuaW99yDeHPGKfCT2QcWN57CCA2uQFK4lZSvRuIWt3eNK4PotsaU4f02-eqCiblL0rDOCB7xpG1KfW8tXtluEYDapi5KIbxl92oiGfKZXnyJPhrba6fCUodm56W1bJdJ3WEUye2rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌ شنیدنی‌ و با حال جواد نکونام از پنالتی تاریخی و چیپ گلمحمدی مدافع سابق تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23377" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23375">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=hzTnttWOS-63O0eMRQRLNMX46nIqsU31zIExqzR7xYRSY3MySjYDVeZKT_LH7WqfAaSKBCMQLMOMA2Pa4L8PHDTCPXWZAXTikDb1_ipNmxGPWfCIN6qYCBJHp8CucbB9TNlICfDkxCfO_GPX6kEsTclGz5BjqLUfDsRYPRDCi60TbSpuOOpy7zV3Ppka9Ke5St4jTWitcMK9BKfOkWTLoazmXc28WyLWP14S5ACHe4p7Bk-zvKD4z0PhnNGZEeZI2lNna8C8tVgN3IELvSJxkjDDWHy8ITC2KsBTx_7vASNPaTN8nVqUYSTE9948IjL-7_5fJ8ZW9WqsVevxFC_anA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=hzTnttWOS-63O0eMRQRLNMX46nIqsU31zIExqzR7xYRSY3MySjYDVeZKT_LH7WqfAaSKBCMQLMOMA2Pa4L8PHDTCPXWZAXTikDb1_ipNmxGPWfCIN6qYCBJHp8CucbB9TNlICfDkxCfO_GPX6kEsTclGz5BjqLUfDsRYPRDCi60TbSpuOOpy7zV3Ppka9Ke5St4jTWitcMK9BKfOkWTLoazmXc28WyLWP14S5ACHe4p7Bk-zvKD4z0PhnNGZEeZI2lNna8C8tVgN3IELvSJxkjDDWHy8ITC2KsBTx_7vASNPaTN8nVqUYSTE9948IjL-7_5fJ8ZW9WqsVevxFC_anA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
هوادار تیم قطر آماده دیدار حساس امشب این تیم مقابل سوییس درهفته‌اول جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23375" target="_blank">📅 20:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23374">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=Thk3CDevH180VVNAfuXCCVEcRZuxGTGIhzyUiytJPiF5NcaX7MasY6ava3_FNbl1iciKavc6WFS0xrd_cBGDJjjG84D0Un4Q1nxqB70nUSPu8jI3nfAzXTOaz322L5cbaoxv4znNgjK48PczEGbqeA0LsvrfEaJjzzXqwe924orwTyOWmhuBa2ZeymJkNisnFGu1gGxUf9o5aGgQbptsd4YhZIlLdTiFRXIhACn1YdZ7l1GTeqbuGKj3WoTJYWXoFQ-K1fJlZ54qOPlhPBWN-3jS6-VJvef6O_AhJnHe_dUS2spEMiMW45ZnHKA7nupZqgsRI3hXIByTc8fYdOqpCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=Thk3CDevH180VVNAfuXCCVEcRZuxGTGIhzyUiytJPiF5NcaX7MasY6ava3_FNbl1iciKavc6WFS0xrd_cBGDJjjG84D0Un4Q1nxqB70nUSPu8jI3nfAzXTOaz322L5cbaoxv4znNgjK48PczEGbqeA0LsvrfEaJjzzXqwe924orwTyOWmhuBa2ZeymJkNisnFGu1gGxUf9o5aGgQbptsd4YhZIlLdTiFRXIhACn1YdZ7l1GTeqbuGKj3WoTJYWXoFQ-K1fJlZ54qOPlhPBWN-3jS6-VJvef6O_AhJnHe_dUS2spEMiMW45ZnHKA7nupZqgsRI3hXIByTc8fYdOqpCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مهمونای قسمت اول برنامه های جام جهانی
🔴
امیرحسین قیاسی: رامبد جوان
🔴
سایت ورزش سه: خیابانی و خداداد
🔴
عادل‌فردوسی‌پور: نکونام و کاوه رضایی و دیبالا
🔴
ابوطالب‌حسینی: علی‌پروین مادرقحبه برو دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23374" target="_blank">📅 20:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23373">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=Y4zWQI5yY0sA-rdeom5omiHR_FwrRBoNU6k119U61DwUO9ReR5ExbsufuS5QCzEKcLmVgEzeVWW4U4LeJ8ufmiLfU_N2CSI6kLzyqHn35PYv0sky2B2rXvFrWGJXJTirnSgujbecqqCTgPlKYCjxJFNhXdu3Qm2JwNa6LGe4lVYQl7ZHO-yRuytDLjyBTSAAEECP4gnVV5o0W1vBzXv3d6PHoWuM6Izmz0J8obpr5DuQHhyN0endT9iA_ZnnaCprqc8bkv71-6a8q7gNoPmpVAB5svmWsKUMW0Uv100PGbDIysk_tQru7gBx7WQhbYGY6mHU-yu0Uyg5zuOymR6Yd3a7W_cdl-Vu_ez5E72B0AFrovc_zYwvge6dmxCz6Mk__AZu7WWzPPFWBHT87uhGGEONL69ARHAt7KKgYl1JxmZwwL5sWzfJ0tsnAUzqVK4HgdxGhW29an90ApgypLFU7C8OWfB4UGulgkzUNdgbK-BVJ8FUdwq076813LzE3Q1eHJjOwg0e5yyTxICEEwpoxAQ3bCfMxLv8gZFi8Dt3to0_iq4LezqpEIpSEaiWFADOdmzHnodCrwZ3vDjg2ypbLITCc19THKQo8Xw4cynAOAiKWJK0Urd0bmxAPkG-gdd5LsiKz6W2USsoGrqaJ8_qUyygu7LytPfrEQonDzJP8yk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=Y4zWQI5yY0sA-rdeom5omiHR_FwrRBoNU6k119U61DwUO9ReR5ExbsufuS5QCzEKcLmVgEzeVWW4U4LeJ8ufmiLfU_N2CSI6kLzyqHn35PYv0sky2B2rXvFrWGJXJTirnSgujbecqqCTgPlKYCjxJFNhXdu3Qm2JwNa6LGe4lVYQl7ZHO-yRuytDLjyBTSAAEECP4gnVV5o0W1vBzXv3d6PHoWuM6Izmz0J8obpr5DuQHhyN0endT9iA_ZnnaCprqc8bkv71-6a8q7gNoPmpVAB5svmWsKUMW0Uv100PGbDIysk_tQru7gBx7WQhbYGY6mHU-yu0Uyg5zuOymR6Yd3a7W_cdl-Vu_ez5E72B0AFrovc_zYwvge6dmxCz6Mk__AZu7WWzPPFWBHT87uhGGEONL69ARHAt7KKgYl1JxmZwwL5sWzfJ0tsnAUzqVK4HgdxGhW29an90ApgypLFU7C8OWfB4UGulgkzUNdgbK-BVJ8FUdwq076813LzE3Q1eHJjOwg0e5yyTxICEEwpoxAQ3bCfMxLv8gZFi8Dt3to0_iq4LezqpEIpSEaiWFADOdmzHnodCrwZ3vDjg2ypbLITCc19THKQo8Xw4cynAOAiKWJK0Urd0bmxAPkG-gdd5LsiKz6W2USsoGrqaJ8_qUyygu7LytPfrEQonDzJP8yk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل‌ فردوسی‌ پور درباره یک اتفاق جذاب و متفاوت برای‌عاشقان به فوتبال و موسیقی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23373" target="_blank">📅 19:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23371">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/geP0X1eyRX6p50W7ySoGhvvd1_rJK5Fm54OhrKQUYIruDGX-PQgGhHi1TU8zgzKgdLoqRbZOS8xAE-QTIEPvO4R2IHY1KsZ69q-xctEBEA1I4MSwmjHMmQaQbGofh-_jjS127cHZnGjaKC0o_oNzYQXHSSghd4vIFVvW15HnGWN9nKc8orHmVZWo2-Zg8tr2mti3o1rK1mAdzYhBsamliwTJ7o8a3THZiEvvW9sDYGG6e_uW7YudZgRWwWvPWhYtJ5oW7olYM_OzKK3ZVwjWJNAI3S9fJjoxvHoRc9gS0y6LEx-RyeZxJ5rllsBlN6mI5DjlFSmkKEHKQTsmOJNAZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lneyBuSBJAiwM5leSF2yuHzhqVX8Bn2uPBV6DGPiN_9qWA4lueToAnr1q2mjVlPi2sMMhUSRNGYdQ9RwlXCcEPbl5bfLtOcqLbK7HsQoSd8O3dkcVy-n1KIFg_Rq7Xd5CoEX_78RJBVyGJq-NowcWRPSY33xJ2unK3E5MrT5kENqL1Rjl4To-04crVuldWcbvfvsZ7RUKS-8kVV36okSPOM_VWxy-Oy9R_YtGXoAJog0FV5wFa-aSKM-d6-3xe7w3YlO6HE6zdEnpPTbMzKGL28Yk_-hVLGUm1QmVSvHegHDhMqLJOvCmjigkawHqYm4KBnxHTWsjGE4kNBiuqrqLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23371" target="_blank">📅 19:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23370">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFCqZDLzm7VDLNEqOCYUGe72MAns6-xp00GNlfkC1Zvmsq8FKvXQIgQkIIfZEgvefkudXLDl6zuFyQVIilqWEp-jNSagpPp8-E-twHlUl_c2O5IjykLjQVgXjwmQoLbmmsS-rS3MOi7HTjgFjH4V_Oc2MQ3mPfe3-7wEGZE18YPOrSDNbHOxU4U_n5ONXJX7grPcQhl9Bvznobt8-0cJvULiULHaYFZoPvPip30wNsbSHtMLSZ8Q7wx8QiXuek2MPbC0cEqpGlha-zM9XsOJCM_Bu5k_pBXdKrEl17vBQ2Gt9MGxXKhZnHXc5UUpPh50iNpvQaHUVnMyePStxbpzdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23370" target="_blank">📅 19:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23369">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPE6pxuBUF_FhNMEGulgAumtBYvazAMiC_UQNUGwNh6MWsRgBQI_apLj_Wsy27kavdcuGtWSz18xL_qHGx5JUHYmzPmFTpRBFlckfn3Gv9YH6xfwPRdUows3a6Bi9tO3lUYAmVe9v2apRZqN8Gt1bMxDhWlpMQGpmRG44Gv80qQ807xJK9UF8ULsg9GBmrM1oJE1DaoFhtwY6J1GiPUYeE5adYvJxIrhrmA91vfGTEEHOenG22eG5CK1IokGKom3zW_ESQD719RdGoUsXMQAOK6PMFjc9b9LPykPitK0SHZ5byds3o5nwgudIYWQg_fmDp2hJLlxNjzpPhKyXdnJqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23369" target="_blank">📅 18:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23367">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WjtcxrApTpEDdXs_SZLefqZ9qxZ0VFf6ktRfE1jsHkw-24ZN2Y8OwXHKGfgt-9OhZREZcsUR-aHMBG8hMrYoQFiR49Bk9G_lvMYdYjZTupqN9KO4S-hm_74lzT1fvNQh1lrlOSKeuMoCR0grsRq1DRR8KgVS_Y_Fg2VMfxewxYsyIHMNV8MMP3DRqEbGeaBCKA33noaCRL1XHFek7-riz19mmNIJZjZ9Ow-GqojAtCQR9DxqXd6J7vd5H7Kpy986mx15pkBhI_sfh67Mxi8Ou_XTqXjJttnyQXSE1Idsgjbb420fwnXVCAHpe1CPJ89GbeXrFHitEczcklc7FWIM4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J7_ZDJlmSEM2w2BC4y_R8Wrt93Nr_lQU9lRSUgTKpihmZeJLVR1jL6yy5BTMZYYYkwGpZVYfUQ5meIox-wugPfI7-aaHjVLj0VH_xjvtnYpiaJT3nUhhTWc3POQo5lauugBAQOTERhLziyyWSyAU5lUalhi6xgDaQEKQcveF9Xx54HKZxSP0KTihvLkCobux6IWLiYJX4WlTbyLNl3HV2sGD2VW7j8I0GrFntFO73bDuerHSSbtYzlgtUTLMVAstbjlsWEnDwEKnQ7_V1dyoZF1Z3HNgdlfJ4_oxKlLw-RoqIWE45X-UQ85WIfrL3O9ztd9ElWngZcPKbCB6eNVnzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23367" target="_blank">📅 18:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23366">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uC7TlT7g3hLYxhGtbfqOzoFdwsYVZoycdap7GGBb-qE-aVk2q_-dzDgW4CvY5ns1jhQ-v1-_RFf8MyGQ7w2-2OjBBlcfFfL-0awlUrtj6UPETZv_e03S-2M2KZ6xnjHQdjiAecVv2wnudPKP80_usYI9f97qnvxa5aKhHMYWTVHoIXesEKUe9F8K-W_PXa874_LUD3n0-Z6KNUyrAQr_Q6i9-IxF4QzJmAaENv9nFaiZ57SZlTJsKH3-gVkU5kssJkpMGTLhUe6FjCaldLBoMPSn_jx_zxo21_dIbjTLXLP0B3eUSgcsmqbfNsETiEOpgwiFjJpX2GPIQlTClxtzVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23366" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23365">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=WIj6FYOSK6rP-HcAg4bO24J5DSZKtTHOdakRTAks7NkLi2JUArWW1kJRu0JR_pXjLJ8UiurhNvx7uycPzapbuGPzPMu-8Njygx4QnW21vv_0Agamuq6dql2iZi8T0WHMUUx_nF3srys2cT4A9zvuvU36lVamIM0Dg5N52NaVELzHITk6bFhXxhQjIQTr2yo9qZO6SUwUl3YWJGuoxJvIeFmRHvm6aOGXLPdyF5d4o9SMq5pMmj6COjqhTS3P5XVJQ5HPrh2NM8dToYVMYmefj0IWuQCSF_O4lR6FDbc_2R-kD7SqTlIa9cv_k4lA3JffOrs-qi4bbdK01ytFpDaYkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=WIj6FYOSK6rP-HcAg4bO24J5DSZKtTHOdakRTAks7NkLi2JUArWW1kJRu0JR_pXjLJ8UiurhNvx7uycPzapbuGPzPMu-8Njygx4QnW21vv_0Agamuq6dql2iZi8T0WHMUUx_nF3srys2cT4A9zvuvU36lVamIM0Dg5N52NaVELzHITk6bFhXxhQjIQTr2yo9qZO6SUwUl3YWJGuoxJvIeFmRHvm6aOGXLPdyF5d4o9SMq5pMmj6COjqhTS3P5XVJQ5HPrh2NM8dToYVMYmefj0IWuQCSF_O4lR6FDbc_2R-kD7SqTlIa9cv_k4lA3JffOrs-qi4bbdK01ytFpDaYkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23365" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23364">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ardYVDxcHTahtjmPUS1gSZWd_VnQdvrpwMEa8GlLdZt7q1bKtrZqBUmKeUxcTwaLmSP3SmUddzTgPQtv1mnmysL_UaEvU-ISj-TQULJ4WSywK1KBiXyVBynOKrB-FN3IubZ2qnfDzjk2zNWWLLFhhF_TO5tuo0TYkVw4gxc9jb9KI4WGa3E_koWI6T5FyQNfElmnLP7uSsV8t6wCrIPSMYLTON8X4gFrG1wfMqsvjzn5Tq2wxKIAnhFVYhG_w0SsvpgvHMKNxBjfyY5eWgGUL9iAO-r0PCzImegoZQXfB714we8BKfoTeGtv-BCDKfCwwAl3UWjtg1Clp9e_uBtOUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط یک پیش‌بینی تا رسیدن به جوایزی که همه چشمشون دنبالشه...
🚗
پژو ۲۰۷
📱
آیفون ۱۷
🎮
پلی‌استیشن ۵
این فقط تماشای جام جهانی نیست؛ این شانس توئه که از هیجان مسابقه‌ها، جایزه واقعی ببری.
⚽
پیش‌بینی کن.
⭐
امتیاز جمع کن.
🏆
برای جوایز طلایی رقابت کن.
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/23364" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23363">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1mYZyupNpO37JIb9YVI1HvwmdGet6ZMMKnVuOvjGFTHBPJ49u7Dmx0GxKOQr347NmuW3atxUeCvaAUPVt0r2K7yTjqb1p3f77t6sPN692mS1Sp8LAFVdYb8OWY-TtX4ocULS8nEwuyUV2y6oqnGixs_E3nPhDrNjQWk2Tzyc9EtkjCmF8MRQJO7_DUQJJfE3NZ3XvPT96OiMrs7RJW8y6eTiGJtIa8-W7s8UVH2j37wjQiZfnQBag_jdG6AP8IPpNYGuolXX8h2eMxNl-kbPbzarZfOvUISYvNG1OsKYe0VqC-lvCzQOtytNWdaNge_pQPK-HJTPDOztjogCXqfig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23363" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23361">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aznJ064rUnwO21rdmgbQbFX5d1xs8mDTlRGJw5ApXfcywnHwZra7zJ1kj-y1bKI2fqKUpbfCkNC40TYQhBbxJiuJUh6VjlcdDqJ5gZSNUgiqEoMNjpAf8VNimD3DJ2k3HF9o4SGsa_Rg8qAhnUwBiTXZPMg_YYD6SbUD4ajXurmUG2xv_8ZJDCPHucPGULF8r0mW4f-HB9WZM1Gg26CSxHuUajzu3X1uQXluvvESsIjAHA_U_bXTabsgAEd4wOy4wH3leqZqjW83Tijb-GlDLt5bnnNVaH9Rc7JgOYnS-pHDWk5n1_DNtmRju9cBPhW_nszC3pNFOyhsvj3-2K-nmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران به عنوان‌ داور دیدارحساس‌دوتیم‌ فرانسه
🆚
سنگال انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23361" target="_blank">📅 17:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23360">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfJ-fpI-JJK-vvsF7pWwqluw8NoUIIk3ehOAhxJdNXSm84QHb-FeineU81JMM-zDa8zVvamCykrUyx1bZLdQuu7hEl23PtNEJJjd_L1gaKEMiTHNKdhQ9T8tb7TJuivi4r5yCOcyCEHfTBnfutqOtWs0urHIxR9rOWj7f2L1_3FdsZ5VsEmlWxREFOmGsmtOctgeSyJS5ukqZ67C4-ogOWdBF1RXWobO7W54Gb9IdiNmwnEl3Uqc1AcRJKxodpA7trXPgK86C1IFn0RJSLMz_10RjQnt3HGo6FVMlsUkhB_Y_g6LlZ-K4eTv41kJNJXQ2DDCMELpvqxbJ45nqIc0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23360" target="_blank">📅 16:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23358">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJTxIdFfQSRH9fMOh27eAFUpOLq9fRmcCuZmTCbGrIPiwPnI450Fbm-rdv3l7M3iPfuSwhUV0VYv7iNoOcrP3UBqNf-v5jYHxMA5jLN0N5UGotYujSMfUwiJge0UHm9JJrfcIZGW3noh6Rr3QN74Hdv67rb6slvrOK-gHykQ_4nBO7ORYRGiJIB2X3te0TPXdm8QXXK3Gy9UW4sGx5oHfd52ROVDksLeUvFgFlzkhzQYUfAZAOKX4FIFK_hRotWQvlxE1ESiKONYMODlcDqRKjq4f6qRROW0WjjtFsxdmIOHeP7Cn5LoPhe_z_RORoRz6OvQDggrAqP9osBjpHa-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LI_tclkWDs-rIjf8FU2f26wR_4mS012Ur_iuXORTdzrgJlW4kbAe4k9YHqhc2K780HphaStC75pt8IvENdSbCC-CIpe5ZEJ5Hr6yXweIt2du5J7zTYAJ689JjIpjJ7y3TWP_CzA2HxY9MLkcEfmfWYu6BhUVX6H2koXggOVvefonL8xYDwfpuIzB_BNSJQv_9g3TKv7PHp-gngGi0wNI6O3RmylV3eCwN4elJnU6_4kSdVVDpOLG3QNCYxnSFxTSEUtWrv7iTPgqzdnJqMyu2voRIru8g-_LpOxfC14NkJkzjhw03ZVQ7Emhrytxkc7ANC3_p_Ei7D1MLzeEoKsJUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دوست دختر پسر 15 ساله کریس رونالدو: من رابطه‌ ام با کریستیانو جونیور عالی است و شایعاتی که منتشر شده کذب محض است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23358" target="_blank">📅 16:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23357">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7Mdz9T9QvVc7ho81O6idZ8U1u1KiQuF5l76bkZMQxv78CKRqH1UV_3hqAYRfm6IWLywNxkCvBQnfj3qDrAT03qIApzACujEHvcP77LfZ3CSoY7kMy6xrdHFp3xfZ3glsZWP3eF4FBRy0oAuYj8-3Nut4FAavhI0rpSt8k6qrv3zUBzQtl5j7kzn8ULgmrVlWP1VRx_f0-3NOhSUUhGFf9E-3bFFFbLkYtAbr-vBxs7Fk0ILwKnkc8LL5myVWXT22HZ6lByyKmlc8Z3ZeepH5vLB4AJpFhHIbAOT7dP22mBM8kkUVDX5c91RW2mGtPAS4kUo_TI6n1a1IRwIkDeq7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23357" target="_blank">📅 15:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23356">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqi4TKbXVz3sbpixqxoPEQFee01H2XNrHZAxxOoFacgoneDwoPyemkrPA26IjkvV8bKotKPqAfSJpbJjde8vQFMkk_0T4vx9f84EC-Tz7t5_mi_z9U0S0b4THmhHuz2XHOeBwAaZbdr4W_axLo0xSQBkAc5KLjNd-aa_eEjgXA2Iw_5Jn_d9z4rw2o2uEaBQCOacpMygAL6XP2g2RZNJCLfeg3ehbTjJadrrAUwEOOEW5MwhDuTncy-fJVKC39-UXPTXLQ0rYHG2rHUy8z7tKDMG5_-AG5XFWTWbGk7L7zJyDxaAbidKkxPmG9_IGAseB95vlrRto57n4vC8jwpSzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23356" target="_blank">📅 15:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23355">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByMpmzwH_5slDTCAhBUUfykK-a9P_VOwUgHCCxC4-3IBjv8nFm5BpXGdFCLQ_po6DRRapE247w0g9ZoGIiwQsL9NWNdgZ_WVsI8WhDVVpnGRIQU_yn9IrF91mx8xH1J6ig7TMkEW_m7aRxiTTcS_15UJcT4GeGXNZq5vVjoTIs0KB-pBpkiaoZzUakOmwYGb98erV6RWBDH6-5l4Vh6BWPuAd4y3DKp12UBtwoA8FBe8Q_COQ9yHV8r11FK5KW88xnLelCggDw86GaB9HJKOnelXzrGhJ9dl9xydl4ohJuDSXxEWP-3KagbxM02yHhHiO72GumDa3E4PVQiTz6EMdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23355" target="_blank">📅 15:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23353">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwT4z6DZ6X2KDP7_2HocZGf7XBvnfD3xBRhWBvELGBmgZkgmVhp9U_yxlj8ZPeBtxcdc1LAa4Mpjth8cY2rwniJzub0N0a9bIQPIZwrauvcDAbLGX7K8a3Jf4K96rdOszdaeZTBQAhSW7LTRrj7gMDOVpLNrW4HwnIknfLes4fcdUYo6IYJrBqkatLNWA4k2v3pVAlGU6ryPhuKnsIOlhM_-p6PuyqWdxdJstcv5p5ktb4NZbj-0PREcl_F1ji394TKIe0MOUMdVe1o5nR6mTYyi8a9Mh-DNhD_tU0rcFZ0hqO5PzHJN01g-YfkZ_PZ0GfW15rQ7WUHeIS70x9Y48g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fIDpXfPzhzTdr1scURf5Y4M7lbqQ9lfJVhmUzoXiwY6Bi_LE5J7dQKDnv8cJrGHNy4fmu5nLArcden1OEyxcBQcj-ialw1KH7wNBldHFbYIW4qBEFXqLyDrggrJsjpK5DSO2rWFEHsokYEaxIRdVNvqCkhIvaTToCgZZn5024AONgY4-ZcDt4fdUzEgSp2WH11_j8rVm-7RkTOA3Dm91q-Rf14EsubRynggM0zMEIQR3vEJTZNNVfWRYz3RIh03vuiHCkqpm7xe4HXEBpkORSFM4oU63dUNfGBaHXE0lJ8vDfyNKU1zsyi0VeIaaTuJqFJk-vJJ0bafrEvnKVndhLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نگاهی به کارنامه کریستیانو رونالدو و لیونل مسی در ادوار مختلف رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23353" target="_blank">📅 15:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23352">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTKRgdcRcI9VWm8UU9rIuhX0az3X6Uxhv8q0kOToXi7sk3ziwUPVUr7RyZHkmEi83zHqbbA1LUiGzE4SNTyr1EVLIlbRj9HJBTRuCArTQn_pZpWGUDhOWEQZlv1WljOxsQWmDx-XWExqKHhC89feW0B-lgK8T1junTKOiTpa2tTsIUWHGs1Meq47y1Sd9luEbbzoLH9j0oc-zpXBJEjJq7g_6npYSko9nqynrUCRfT4LXR96MdM0Q4uIaUeVj8e69xUD5Ovn_wOJQGoH8ZevXNsvKFva_oWKuEhVKwTNzDp1WXBfTuPpc8HI9nnSFrGEhAKe71UrkhmnhVaC24RPcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ‌ملت‌های‌والیبال؛ جلسه‌‌مهم پیاتزا با بازیکنان جواب داد؛ اولین پیروزی سروقامتان مقتدرانه بود.
🏐
ایران
3️⃣
-
0️⃣
آرژانتین
🇮🇷
25|25|25
🇦🇷
23|19|23  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23352" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23350">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YgL7vnLcTGpysx7cl0Y1IXhOLy_JwcLYizWCZwo9uSzL776Omg4nGKfmdP7g97rypztMAP7UcoN_M-bJ2rlZryvRhb9887V7xyxJYDYQ0d5xMspUMFKa4BBJzd-5nau3TV66ZKvCbnWiQd56o9FWpajFCKppKgSL2JhOMVIamH6jrT1fcyi349En8WIvJrnUKl9lDLWpg5HUSVxFM_TbarpENnE71T4rRAjB-EHBjdlzCIJ_Ck6Pk3pI3qUxczLdKmzX9WEGcYN2DeuXTtipNqqUOWOxlXvgTMy6QKNBL9sw1Ww5FED-YSt33rxx9a3MPDYAUQusq07NUBxCaa73IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ghA7T1389oEbKcR4k-VJSLRWlX8lQ7sGZ1k-djxwvd51vUi745R948ByitadPqs45-8MH6mNVoidmJEz6OW_hBMvJZba2dMbhWjmWCL7356YFjK8YBKFY4ZZJBifnJ0b0f3Zpsu3mOcPALQXo6Uhm1n0Js6tbpTJXmAaUOE7aBcjcsJsrQZlYmwJmycBmTp_IA2NZWO49gIXIxyF05dY4qCEkgRw_S7XfnZDrbyiPAZqkEaqWJyfURBNvmIBKkOSIvTNHOTujeHaFN7iHvSj5KrK0gW54L7_1icUaMqsnqojAnWL1WO7_xjg1p1Owkl74Y0IoTEyHsuQJMmwwVTLnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇬
گزارشگر اختصاصی بازی‌های تیم ملی مصر در رقابت های‌جام‌جهانی 2026 ایشون هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23350" target="_blank">📅 14:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23349">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVNu3N6CF1CN9swKoRMirI07NNidZ5VbtVEVtKYyjmqCNChxz6leaLt3z5f5-g6XWeJ-10yCmwXO13nvEalcctmMRqsEx00ysKUWE_3MEraumF3uRf8ph9KGwmGHvs-7k9aFFeZH7CbssyqwQ5AUaTUw6fZhaRV4UZF8a7PqxrceewU-ZOa9KMMBD6rpwINk34ku2Ec2Yl1Sez47l857MW6ePCKMJYI86XWIrtm403jYHpbvMCO7_vRPlNeMa8SpWE0NM3Rp1y9AiIGwK4kGjM6-iQz6b5Vm3DF8b-gWvzH0sru8li2uOXXWjnGXfLJW0nU7IW64BEI5fgST7P4yrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23349" target="_blank">📅 14:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23348">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=JOeEcGzdlIyvuCiZ5BF4_EzNduG9Uzgx4nXK3V11UzXXeupz1CXuoJPs9GO2GvTU1yMFuQrdtNWrbhw9xnANmoUo4XURPRg-xhLbrSij7mWFykh2BY6wxkz0vSGCPIkCbxGyIZ7nC-P2qDAihk7Xi6ucQSo-yWIKUBxYQPJQ7RSGacUzOB3m7AdOTMOatooFYFSdj0bU2tO2clt9UJS7T2JUodo6WHoG-gdbzgMyB-BY3aFqML5n986dogUJ5yyCydgUHg9JiPEZBhRtloI8YtBkej1GSoZBtPBtwStiBeYGNnJlDMoIyynTcbKOdkHLulQo-MbBIWotrwlJWnYvRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=JOeEcGzdlIyvuCiZ5BF4_EzNduG9Uzgx4nXK3V11UzXXeupz1CXuoJPs9GO2GvTU1yMFuQrdtNWrbhw9xnANmoUo4XURPRg-xhLbrSij7mWFykh2BY6wxkz0vSGCPIkCbxGyIZ7nC-P2qDAihk7Xi6ucQSo-yWIKUBxYQPJQ7RSGacUzOB3m7AdOTMOatooFYFSdj0bU2tO2clt9UJS7T2JUodo6WHoG-gdbzgMyB-BY3aFqML5n986dogUJ5yyCydgUHg9JiPEZBhRtloI8YtBkej1GSoZBtPBtwStiBeYGNnJlDMoIyynTcbKOdkHLulQo-MbBIWotrwlJWnYvRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
اسپید یوتیوبر معروف در حاشیه بازی بامداد امروز آمریکا میگه‌ رونالدووپرتغال قهرمان‌جام جهانی میشن؛ زلاتان هم این‌مدلی بدون هیچ‌حرفی بلافاصله میکروفون رو از دستش‌میگیره‌ومیگه برو بیرون بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23348" target="_blank">📅 13:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23347">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2ikemnycEowrXojGPlWW3dTbJwoeETx2qlUVFUuw9i5EMJc52-ByoNSQjXDTixStjhLYuVVOWyw4mXMqMIcVY19zzT5crmpeM6QiWE70lmAnbn-7IusacZgnqW8cv-6uuZzJe_YTYHoUuSu6ycrAOd6xaO3UB3VxdbUOOj_jIMUvi9xSCrKTpUvQRdxIMhl7e39PMVh6k8qU_HsjergYOarebWH3iIRqYnGHMEzLsojskweiM0kXkNFVgyhPJ_8PSPA2t2xAyaEG43qF_f_6ZtymC_3qnQ8LspTJtid6LYSH9lkgiHzUc3ANUbx2HvxvQxiwmthg0BOzj14I2U_dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23347" target="_blank">📅 13:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23345">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRH1CZ_hG53jouCYE5ve6ZBbNKf3AHPI3Fod1l61aI-JlkzoXyRAqp6COvtl2N66z1DE_RaHN2sjxIcJxdc5AjML9iek_Oh1oezeV1kIbqTuz-2FaiorBQSD2ImMpGgIT2ltzpI-mhPHDnqfObbszt9gNfb5ypy3BOhfp_Cw4mG7rstdxeP7UD8IMB1xT2HhXzKlHICHx8PT6rLtiue98O_m_A0t-FwW6vraeKW1pnpBczY9g8vZJexuOxkpr4raHcKlN66FKMBrgr-iwppR1y-Ou1-9j3IJuSjcu-HG6aWKS6bFNaYJjDO9CMyRZYhd0oQ75LXoI4c1QTpuATu9Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ES342eq72AFdxOcS_8yRDIEHzQbyCfka8LTGzYCQulXh2URu-wVFRGO0e2WhD8Wo6SxsHs1pgT3k2h-ou86Vq_Nbes4FThG4w8TbCjkQdwW3ljpW5f_2nYNerfDzAdDP83fI_h5v79SqWdD9O7UQ_BCqS1mJOQX-_sBptOGiud4rnC1110pdwI3t-IWCVuggIceADzgREgTzc4tZLCh43NTs7neHVnM0_7splWN7m0sxYMlr5FwvYhaskc1idWGchLSlMNNjf5_VdP0USUSk1ijeHvXPCj-cUXA8RZEXHSNgKx23BUROPJUyEMlbLfkNvraHcYXZfHtdHFfLwAettg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرنگار معروف باشگاه شاختار: بازی دیشب بارسا و پاری‌سن ژرمن فوق العاده بود. انریکه یکی از بهترین سرمربیان حال حاضر دنیاست. همچنان معتقدم که باشگاه‌رئال‌مادرید قهرمان این فصل لیگ قهرمانان اروپا خواهد شد...!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23345" target="_blank">📅 13:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23343">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMiXhfL1oToBkccOEeeNDUPWFS6ZE8me-NSAHLO7uRcumiuZ3y88xzhzOD10hxnRVp1bCDi-57GeCm7QAebFVXfph-2wfqD_iZxGQUML84KQcFl5mFCmN37sYWiyLF0gxQweA7xXdw2wXm7FxznymVZLhb-dcL8sqA_hPvgi6LoEcPgzzpAFYJleegh8iu_bJHoJO9fqoKfATtZt3yV6BgHaNzoeD8LopNACCwxqXLNerjXdlEeq9uKq0hlwL_tvMXZi578pQHxtxwABQZXV5ROwCEoQbh476gO93LV4JLeFkjV0q5mF-J6PeW4eAId4e87iXy1wx0__pMoNDwN89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23343" target="_blank">📅 12:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23342">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnOh9pH4GTyzPaZiEWnV5DBlS3WXFZZle2xn021Fb7RB1G2kZsjzhNxgcCgmIrJXxHweBdVUFY_SupQZth8k97Ea4737KsDmEdtusYBflo_gmT9bYynOdy29yfCPJ54ntrSxZImfSzwhqbbK3niKS3YDuIUawLcS35sRymm25CL_vlNVKRhGXGO3ZYkRTDKThAMkQGk-Rws7KsNAqjVxIYiCNGxwNe4SDeC9zURogCnDHNWGTlZr3f4lfdjxdh__ngzk0KqWeLFN94ceGZtYKDqk-GR9mRxi0Lxg4EBj6lL7H39Lej1yKIDVVJfWBQFpu1jDG8SRFo3K3YNgiTFkGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیف‌وتجهیزات تمرینی تیم ملی انگلیس در حین انتقال از فلوریدا به کانزاس سیتی دزدیده شد. بنظر میرسه که هری کین یکی از قربانیان این اتفاقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23342" target="_blank">📅 12:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23341">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnfPlk-Ud8SV7HG8qpvjQOlizEepkNpc9StEQiJa62C_vjg_i7v3gQHouZkYNGU_9QhmThJenqxT05LaElcQhCknd1I_9u2Xo2kyBG9MlmLPwp8vlJ2WSsV5GcAhQ-thn_eBOkzyZi930_8RnORzbLKYjeYqqh1KVZ_tnsi5tg3acapnLG1R7_BzI1LZxqfp3HT6JoxAQUVBJQnnJqJkKZZuDb7ItO4dYymIGS9hDPm6n94CsDcUxk-Y93tayxR9xAWZAoayK3pTMBoZhTo1pXDVqoEljt68PmRz5Ys4jb75PKEIagx_QNMazDCHNSUTA6KwLWMxa1K_UqzFOQC1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه سپاهان برای فروش محمد امین حزباوی، آریا یوسفی و مهدی لیموچی روی هم مبلغ 220 میلیارد تومان میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23341" target="_blank">📅 11:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23340">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2Oy4mhX1pI_Y3XW1GpqlhZ_M5CDfNs3AGVOAdDNVRIGBacSLW-XojsPsJ8ZoTwYcerHc-lT4LGLISL4eCNObaq9rCNtNawtBo3ExTWu5HQdB5Bnz55IBDVMKZs1drWQ__y_GIObpCe23AJ7D_wkRv-6XjzIWkEVxOD-azxIVZ8yBjsEtJGAumhv1Dik5mRFN9yQaGvgg0fxYiBTiCG0DVuWV_44HzgwrpZvRwG_dIZQw8scPpbp3NKkhCsGeiQQn1PcTWNygnQ4B9-__2g-vnP7Oq1TaEf-Y9AuCEHizEzGus4dBQ4u0qeLFGh9zdpX6kTh-QgDWijq95TtSv-bKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های‌دیداربامداد امروز دوتیم‌ملی جمهوری چک
🆚
کره جنوبی در هفته اول رقابت های جام جهانی
‼️
هوانگ این‌بئوم با ثبت یک گل و پاس گل و آمار بیشترین تعداد لمس توپ در زمین به عنوان بهترین بازیکن دیدار کره
🆚
جمهوری چک انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23340" target="_blank">📅 11:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23339">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8NVr8WqbnpUFIfzij77tX-ku6OrJfsVoTlXo-SgB_m3t2G8op_25e6AHKX3Fu7K04zi0v7mAAetzSn4n7b8wrU0-G1uLEkLCrAEew7R28sPvybUS9e1Vj_D9Ttfub03Wd-JCpKAzkItwPNndYyFHrk-1-yCz6r6v_eNbypVQqVXTT-pgn_ghv0F9cT1UOH-Qq1QwnRbw1PAWEPnhWnwX9WYzERrh_AuBvifTTz8yHrsWF25REZmd6hrXVYE42p2q7Y4XUcZXugu7RiNmaS3fx9laExDdtvhaC8xGnmKHgo8mL14C0fwWvqTM1_vpstVWhXHyQHmrKmeOAMtmw8sNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
10 صفحه برتر در اینستاگرام با بیشترین تعداد فالور؛ کریس رونالدو بعد از اینستا در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23339" target="_blank">📅 11:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23338">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7yBUUl7q9Jr0SxQaqbcTYZdk_wl2H4763MFYC7H-cd9mVaA9OF2MnRyMrfjZJodE8csJ5FFZIcGheUwujoIXCvoq6I-NYafsbrmx0FwrTEjNpQZA-ztq7gsEE_c0__KOz9Hn8xnB_74aBqJAtqi6QXGwVDpnokg2ezunoSYvAcgPo0vnkpdcAcY5T9gUl2RIOne2OLmi-e-IetPLxr5uGkwSjMGSiQrHssA_hBIjR0IoJdn5UCvh6_VvNcyY_uGtZ41yZLW1cFIH-1uAkmSFX79qugx2Vf2s_HUAV7tBhN_xPJy2lB2wovR-LIGqbY1l-Tj7rVoNJBfxmwkB9u0QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23338" target="_blank">📅 10:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23337">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EE036XcBFVyvfpFhZTLr4-GJ5jOSaf2clGQdiFiaUmKK53iO8hGRJG1mEL96GvKHuYALSqrxmbw96DW72MahPMFyM0Z3oAVNDUwA-asNG95xGzV_QPLccaCFDN5iNEbcpV0WtSpKlCTp6y1jajkpyim1FLeuvrEgGetP0eyrPf0zeOqkCk_id7SNNVklAeSKQdnPOzYKSC8NDhJj5E_RfquHY8_Gn4ciKGZYhRHzAOHJCjo394QyE62xY1B8JIeyY2KFODKDg_Zx-pxwDYpuUHK-viKPJuOArxKaXFm67VWX2unom3Enpq6T-BpEe71yeHwHm-skXtrazxWaAeRFFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23337" target="_blank">📅 10:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23335">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29987e4127.mp4?token=GFDAH_qFggEJXu59XYcU32vumVoOgHmXnrQuIq1sb4IeW9oQvuFhEhHKKGAsWwS5ch9ddz7TUBE5DwsxkV3Hz3xpGYKNIfWqLbbopBepuBJ_j8UvQwxXk-p2lzAWXkhpjytiUB3xhCR_XdV2ga3gI0cW9-SsDpEwp3FNdHMTrBvas0jQyEqgrdw5f1v1p6G9akQ_FP4YV7UDAarp2Axm7G9CPhFMUUlAcD9drWGTah_eFdcrEENz4uMUbyMNVELw_g2_LVUoNwWm6Z4ZrJgRpdYDIrEiDnYoA9tKg5aIFiiuCX65ib_E0B6ovKdXagViVVCals74LBf3fP5nPWO-y0z0GHo5RsYQR8KZ1NK1S-yAkRQZHRBszE4L-guOoxGyeIHYSSrBPumsAdU_z2a2TGY9zRp3ccizFdRWFHHwe7PWkxshWYljS20A_UK43-nKA_b-fVaz4zt_OPtYp2pPIk3Qy3dW_NnhlhAsYLCjwxMCHNUoc2l348lPE0TYH2ms68FcV-qZZKF44RONBSvDUtHbJbOL1fYyC_pxhUzf44y-tPYsR9KZvw9JmbnZmRRidOvZVuiHwI5i590J_gAAiWHl275QSdBFqYLQd2UymzVbSvr92Bssofd0Aj-n0mrKcpxNKaRQsTmBLKSIoSgRMSuZJcqJWrlZ60jCxK3PfRY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29987e4127.mp4?token=GFDAH_qFggEJXu59XYcU32vumVoOgHmXnrQuIq1sb4IeW9oQvuFhEhHKKGAsWwS5ch9ddz7TUBE5DwsxkV3Hz3xpGYKNIfWqLbbopBepuBJ_j8UvQwxXk-p2lzAWXkhpjytiUB3xhCR_XdV2ga3gI0cW9-SsDpEwp3FNdHMTrBvas0jQyEqgrdw5f1v1p6G9akQ_FP4YV7UDAarp2Axm7G9CPhFMUUlAcD9drWGTah_eFdcrEENz4uMUbyMNVELw_g2_LVUoNwWm6Z4ZrJgRpdYDIrEiDnYoA9tKg5aIFiiuCX65ib_E0B6ovKdXagViVVCals74LBf3fP5nPWO-y0z0GHo5RsYQR8KZ1NK1S-yAkRQZHRBszE4L-guOoxGyeIHYSSrBPumsAdU_z2a2TGY9zRp3ccizFdRWFHHwe7PWkxshWYljS20A_UK43-nKA_b-fVaz4zt_OPtYp2pPIk3Qy3dW_NnhlhAsYLCjwxMCHNUoc2l348lPE0TYH2ms68FcV-qZZKF44RONBSvDUtHbJbOL1fYyC_pxhUzf44y-tPYsR9KZvw9JmbnZmRRidOvZVuiHwI5i590J_gAAiWHl275QSdBFqYLQd2UymzVbSvr92Bssofd0Aj-n0mrKcpxNKaRQsTmBLKSIoSgRMSuZJcqJWrlZ60jCxK3PfRY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چالش جذاب هوادار ایرانی با کیت های تیم های حاضر در رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23335" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23334">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c684a93218.mp4?token=RjCegigwVqGC9-n8eaZWTeVL2qS0kroXOippYZ1KD-ViLW4xWEgAI5XMyYNeuSAZCCw4ZaHCwSbfhIKnxXdTZokR4-9zN3KTKBG7HOcZEHGOgXM4yO6pQgr5CFHVBKsFkHWEFpGwCah2hY67pcK60nSx9ly_drJE5vgnX1716VlkydtaMbAGcFXml-t910kIgLZDKuBU9n-R_rhqfPwWjfpni9y457yY69YPx9h3QmTCFqrfOnzOKUfpnLtqKq0-sjYV5pZLXKTagBiVI3T_hnuw0QQww4ruMrih6D-ukZxw0kuidwx4cg7uR2zKW_0I1z82YppgySSaaQJdzFeNmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c684a93218.mp4?token=RjCegigwVqGC9-n8eaZWTeVL2qS0kroXOippYZ1KD-ViLW4xWEgAI5XMyYNeuSAZCCw4ZaHCwSbfhIKnxXdTZokR4-9zN3KTKBG7HOcZEHGOgXM4yO6pQgr5CFHVBKsFkHWEFpGwCah2hY67pcK60nSx9ly_drJE5vgnX1716VlkydtaMbAGcFXml-t910kIgLZDKuBU9n-R_rhqfPwWjfpni9y457yY69YPx9h3QmTCFqrfOnzOKUfpnLtqKq0-sjYV5pZLXKTagBiVI3T_hnuw0QQww4ruMrih6D-ukZxw0kuidwx4cg7uR2zKW_0I1z82YppgySSaaQJdzFeNmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
بازیکنان‌بایرن‌مونیخ چندسالشون بود وقتی نویر اولین بازی‌شو انجام داد؛ منتظر کارل بمونید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23334" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23332">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtbUmpvmk_5EsctNJx8-JcF4A1jfAys_7mSSW0hWRw11xOcNEs09Y27FlZ14MVc4i1Bw6oOYbksOJOBBRs-tHSmPyiNLa9rLhJF5q7MXWdEpQgjhLx-NVF22i-09x24zG9C7uycanTnNpfNemvxN6qi0APIeU-yMQaXUouhkxqJT7ApIsUklEcLXTfdXHK0IA8o-51dkQBzCTR5V_FDSs93gYXuan0PcT18RM6ZSvyFuScbtS-p4uAPuZ76eFX1PCZOIA7Sz2Rfu1dyceeT0BiboNnwqx1T1rdhaFLvvHhdCQVnaS754uphDq9g6iX9EBGIbWxtmWVLhrnUZiKrnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ باشگاه استقلال طی‌ساعات‌آینده مطالبات یاسر اسانی ستاره آلبانیایی آبی‌پوشان پایتخت رو پرداخت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23332" target="_blank">📅 10:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23331">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|آتش بازی یاران پوچتینو در گام نخست‌ رقابت‌ها مقابل پاراگوئه
🇺🇸
آمریکا
4️⃣
-
1️⃣
پاراگوئه
🇵🇾
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23331" target="_blank">📅 10:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23330">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fehXs7Z4ePYX_sAPLDvAHIr1jGLJinzXZZXD0m62BbMuEnOOK8cmvAJt_4jJVmlrdc-eGGH5-OF1w7DT_5JTKJDpWGGIjiTevIPCNFxK4H3CsXH9oYzlgHWclgmseECILpFWtBub1Q89Pm1Mc-A_0u3de6EF1BWnY-yXt2_-dgKJtuiFTpIlr7MYitmH6zJjWJPHJsvR4QJ-AAT4SmwQr0kMzqUdBIvfokQFSRed7Ih8hnC0Je6sL91-0xwNgXDYOcLwDVFP349M0QXnSFUWTCnTudV3IHIrAV2jFkdVIf3B1yg2GXsYPESrNDyVa2rPXa0hR1izNZJkQdGty7GAAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف یاران ادین ژکو مقابل یکی از سه میزبان جام در ایستگاه اول.
🇨🇦
کانادا
1️⃣
-
1️⃣
بوسنی و هرزگوین
🇧🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23330" target="_blank">📅 09:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23329">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291a03c3c.mp4?token=PxrYzYBUiy90nZI70JSPWii3GYYMNpchXpgwDOd6F4qAizhXhnG62DAsR39uIsr5vTYCxqR5G49YdmqCqPzpsOLL0pY5_booa2wHDahuSMGYBZEp7uBxmK8cgBc-ogMlJ_k4VMGktIqdnUBKfatLo-wmi9nUkTfE6GwGwKZFZW_d9crDxtLMPpYWZCxqMIzcetfyI_PWKPqo81qBcYlbR7-ECOhdiB09jrWkJpRayIODzoCxGbIRcvAeIf3Ynl4aPML11mJWrbjiuqWQUXWcNaVVGpj5RkMQLPO4DxMxHOR9qqqIm5szmQQeV7kZ9sJ6SUyakcYGOVjmrp2SKUI_jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291a03c3c.mp4?token=PxrYzYBUiy90nZI70JSPWii3GYYMNpchXpgwDOd6F4qAizhXhnG62DAsR39uIsr5vTYCxqR5G49YdmqCqPzpsOLL0pY5_booa2wHDahuSMGYBZEp7uBxmK8cgBc-ogMlJ_k4VMGktIqdnUBKfatLo-wmi9nUkTfE6GwGwKZFZW_d9crDxtLMPpYWZCxqMIzcetfyI_PWKPqo81qBcYlbR7-ECOhdiB09jrWkJpRayIODzoCxGbIRcvAeIf3Ynl4aPML11mJWrbjiuqWQUXWcNaVVGpj5RkMQLPO4DxMxHOR9qqqIm5szmQQeV7kZ9sJ6SUyakcYGOVjmrp2SKUI_jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تیکه‌سنگین عادل‌فردوسی‌پور به امیر قلعه نویی بابت ساعت دستش در مراسم پیش از شروع جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23329" target="_blank">📅 09:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23328">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d11f7375.mp4?token=i-KQAtgol6XeEqhI-sDbgipgy7s7ysL7E8zojq_ed2cUg-binAN8nEGZ2x7KLe1Y9ntPDwQRXN5EIp0bBsjWA1qrwTsxcxitmLcfei15DlytFA-XZVTf3tZ5VPr4DuvV0gY-_7nz_M_48YLOZU35XUhp6b4aX3Tj5mt4wT3M8UHBlNn525_vFALMUUR6VOK6IZRc3s9WubaBLn3kiMpwGNeVKDFtx0uBOoYAfsPltp-uA4vPtd8s6rTLdy5unw5qzvn3k7L8JkZtKIuDLpJcqcMyzrClfufaJ0y8GgpmhcOmdbU9M8J_Zl82g0aaF0vV2rJJZlXrpnovGayYPm25uVeTLA2SHn3OMik8C8OrLdtq5wVUbgOX2vIQByzCJt4cjVLzS85lKMpnE5eoN87Iu_ykPWmEfBe1sdaHQ73b9ZMXDw1ODk9buKuZl-pQLZdfIT803NN4QvBCX2j_xMK3JZEnFkobT2OxkGZvXYfK8v3sevDeYJCM2JhZf10F3Rj78qafqBAE8OvuyAM8lD122F8srV9qxPsSLEIuYz6XjqTsa6-gjGHC6p7t0Jo3H8dFdL6M9khKWnz13H1TXpcRhwf196U3wfZDhJv_71u2bpivCoNId1fvzZguYl8n35g1yK2J1aCCZSGJk8S_Xx87wum6E2HkuZLpNKkGWJm_AJ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d11f7375.mp4?token=i-KQAtgol6XeEqhI-sDbgipgy7s7ysL7E8zojq_ed2cUg-binAN8nEGZ2x7KLe1Y9ntPDwQRXN5EIp0bBsjWA1qrwTsxcxitmLcfei15DlytFA-XZVTf3tZ5VPr4DuvV0gY-_7nz_M_48YLOZU35XUhp6b4aX3Tj5mt4wT3M8UHBlNn525_vFALMUUR6VOK6IZRc3s9WubaBLn3kiMpwGNeVKDFtx0uBOoYAfsPltp-uA4vPtd8s6rTLdy5unw5qzvn3k7L8JkZtKIuDLpJcqcMyzrClfufaJ0y8GgpmhcOmdbU9M8J_Zl82g0aaF0vV2rJJZlXrpnovGayYPm25uVeTLA2SHn3OMik8C8OrLdtq5wVUbgOX2vIQByzCJt4cjVLzS85lKMpnE5eoN87Iu_ykPWmEfBe1sdaHQ73b9ZMXDw1ODk9buKuZl-pQLZdfIT803NN4QvBCX2j_xMK3JZEnFkobT2OxkGZvXYfK8v3sevDeYJCM2JhZf10F3Rj78qafqBAE8OvuyAM8lD122F8srV9qxPsSLEIuYz6XjqTsa6-gjGHC6p7t0Jo3H8dFdL6M9khKWnz13H1TXpcRhwf196U3wfZDhJv_71u2bpivCoNId1fvzZguYl8n35g1yK2J1aCCZSGJk8S_Xx87wum6E2HkuZLpNKkGWJm_AJ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
طرفداران‌کشور‌های‌مختلف حاضر در جام‌جهانی؛ از سری جذابیت‌های بزرگترین رقابت فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23328" target="_blank">📅 09:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23327">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⚽️
ویدیویی‌بسیارجذاب‌ومختصر و مفید از مراسم افتتاحیه رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23327" target="_blank">📅 09:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23326">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isHiUlsvzBDpWW1mYJkckp9lLWpE6Tl1mZov7Ps7fZXvhRriNCuChn8Ga4Rj6uPvTOYG9vNWqw2om4MO6as6LCVn0iQ2MPB8wNwZu5JtiOyZ-wbXwjoUvkJ8uXaGjZjtY5Ya1cSw5AEVVRb-FVJ81KtTG-tXCku5voYYxJXVLIywtk9jPue0ci3cpeUB8DzANKMO6k8yxXQYrI0NLC5L2xo0r57E9eFc4qNpBLew7VC4JfilXkTjMyv0ZZSBTAoJxYXwWytnEKSUXnhR0KeZXVt2tfEiHSu57jQSiSM0I_wtyEBiQ1PD1gqatnnlkq97g1-QyMCuoelhcLbFAKFCFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حال بازیکنان تیم‌ملی والیبال تو بازی امشب اصلا خوب نبود. این صحنه دو ببینید. باهم تعارف میکنند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23326" target="_blank">📅 04:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23323">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZD_n6mhlmv7ggOpFW24xGq1XCzIX84CqVK6KR9pGJaQeNZtl7d99KbQumJRldD0f0ZH72nH5jECflCNJuZd3HxwFMxc2JY0QF2-cBF75fuqJEC55YOx6tRc_VGcO0poEoj5rCtWb7rkn_5RsQpIs6v6sBBlYdcGWx7EnhNz3BpNvQcgFUuJGM0xsC7Betth-E5JNg76bEougqoxwrbkPMAs6zCkAT-F-70BUDM-KRUhmL0V1UfgqmhvWUlYj7_Oq46biE80w_hKaCH8svtAJ-mQ5vKF1DtFjRiuyWbW5w3cXw9QQUel9JhI4ArJ4gEDASWFgFl5mCtwV6O9nemkBSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RoEUsOqrg86DaHqPn-hhTJi9wBiS-ZF2nf3BmabFidh3Brikai7K7W96mten4QOLKj2sTTYJZy1-hgGgIph-pL3vpx8FiFfCD74Z991y_KOAyZickWcZIa8ZmRRQt9VCO5FXOU7c8fAyS6zESBG0i0gmtY2EZKJ05VobMyQr_AkgGh2Nrs15tB68LpgH6QazQHRYF8qQZN3pqQgxujFbF09ZRGDbL4ARiuji_xrmqfpn9QJRfgbHGCIuExwguHbIj25QRtQwJ0kuX891-a0B3g2dNfzWUI85Udwd8U9CQxAnimISXFVgs4lnKT-4CBnbb8omkumk-wHOjqt-dooQnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
امنتیت بالای شهر تیخوانا؛
در ساعات قبل رو به روی محل کمپ‌تمرینی شاگردان امیر قلعه نویی یه جسد توی صندوق عقب یه ماشین پیدا شده که در حال تجزیه بوده. این ماشین هم توی پارکینگ محل اقامت شاگردان قلعه نویی بوده که دقیقا رو به روی کمپ تیم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23323" target="_blank">📅 03:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23322">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvJYYdR_F7YD2ylByIP_hpoPSydDhQ-xpbd6Geq4um72xn5D8yBZMT5kPN3ax8YsSQT7ahC_6wMoq3nC7u2W_htQ4gX8hJrT6Py_vvPaEW9MoxakGbiob4JAE7EnzhamlQ4DDTiqTULBeHazTzNa7FCh78k3KtZUxzCnhBjR7z4OqAs-sNlBhGm8QXLHt1LecKUTBSUgCuO45DuDcnIUNRgmV277l7Vh9ZxOgn4N6vPvcMCXEXppDZaQpmc-fT4vyGERQon7lDDewF96nqm0QqsHe_JBZxsNI9RDOUUW28XAifEA9GO9yibqu-7GhgFEt0elmsF9hyYqMggeF9-ZLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌کادرپزشکی‌برزیل؛ مصدومیت نیمار جونیور رو به بهبود است و این بازیکن از هفته اول جام جهانی دراختیار کادرفنی سلسائو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23322" target="_blank">📅 01:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23321">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWLR51IqNUp16T6rYUOHe0tEafWNuw-ZFeok0QyIqnfGUAs84JaJPT_c_H1mDoM04d29u-Obm3R86UDpLhOw4NbNbFQesRD6fKmX2zMBdoShd4Z3_deqOope1fPXID63-iHnahPRB0Uy4ZZNxLJ-3bFufx3LP0bceFqh1tVlOwi5oMeJ6FmhqAFiPlJhHafqru0I0tMyVqd0fJfm5Qbk56UB7BQfnZd18NW4s9wxKeJ4QhW1hxkuxmyXQloQOWGisFwyvR8XZlz2pje_BPNy1Bf-LL7ySuvVOorUFoqrWoRlrtIRFTHrbyK0ScbLghJ1LgUwHn00Sf9SAey6fUvrzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات|نشریه‌موندو:دکو مدیر ورزشی بارسا بزودی با ایجنت بارکولا ستاره فرانسوی PSG جلساتی برگزار میکنه و پیشنهاد 50 میلیون یورویی به PSG برای‌جذبش ارائه کنه که ممکنه قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23321" target="_blank">📅 01:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23320">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">▶️
قسمت‌‌ دوم‌ برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23320" target="_blank">📅 01:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23318">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMzTrN3JrU0N-8hSfyFn2vVyqYRCEMN_cmlYQkSVuGL1f6Gxm65fEOz5NXylLqkiqZ20CPRhbB7GHeoPTJttCPFv8SWRRMsJdd0pCeBaXiKOFFJoEqQiHblk2eA5hbsNg84Y7THZMLo9LDm9WS8aVGUOQeAqrBJVXo4ROsWiB7v5ha2tQTm2Qnn3ONIV9YuZqdPRnqE4jol96bpet2wALQiNz4lmG-XV_eS6JN1zFfd5j30puPO1QO7XYOchBSZopWaIg3H__vser8FedXh23N0h_g1QoAa2aWqeHiJxAS3W97IGqlpXtjF8bxSIvEfz6OARVilvgDYIDql2N9A1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23318" target="_blank">📅 01:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23317">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONc-e42M4i2LJAX5C9JLQzYk1d7kVEgRoy4BP372VzYP88cBOLG8Ep_LAHXEmvA0gc2w9L7wPjEUGWBNl1hQN86jKnOb2NVbp97OdeJ7GHzdN4_3Ti3pkktmQkvTasfakDUYze_26ZKkEATlV5l7E0x3Uu9W37bU8esy83p_kU5nXX4_qQtDGZu9nLVTobnSMWBcESnGwSeBbitcZhsqC0GUC_geyPy6_9es5Vi4ZEFFHLJgZ8on8-9f7JlzP0_LGkctnEq3Jss6QfcizH15rJ14R-mA1v5ZUI0LlvFUB6qKCrVlbAOH2oSbt85wCPRWj-pD-RyUtCOA2CftTUcKGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری بزرگ کره‌ای‌ها مقابل چک و توقف کانادایِ میزبان در مصاف برابر بوسنی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23317" target="_blank">📅 01:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23315">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mFTTlNubI9R2BQB_ldZKyj9tGuJMluqtWTgLVyykHLZKq1mn3clhf8JV6WTTN938y_kNDEMhGcd84BuCMWVtDxWfOXTlD4L7n3y-badHAf9UXiej_x-CHfJd9kBusqF9rl6N7I9SIBYAdfupxfk5tmklQ7PM7ivhhNpeRLX1iIq425vALJshdTskPk_zdymeZPSIv6OPNyKZuvXeLBBvSwfvn1vlrcga85A17Seo0SFFzIvCJGHe7iZK6jZyy8yvv7amYONpFh7R86lJU9q5MSFUuOhH962p9RmV7jbYQP8GV5iclgXrRUuzJ7X4PbgBROWQ9Kj_QNJEact_K2eUVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oeHk-DEjOccDTXbBTVu_ameZvcNfO4VI1sCEabbFz3-emOeSg0ng01twSiLmo5HFEPz5KYVF1M4aErrIC4k5nOt2481VLX1dcM0UCU8BkQse2JSuwZCeFFTxOB5_E7BOH8CfkqU-YaCMH2k25VNUCDLw1hoBUCSTnq6j5U2X6vXlNs65s47rRhrlyroTgEm2y8fVm3W1SD9Rb4JiMYKVj65ktKIITP8tXKL9nY4rimyeQQpOs6o4bxL8gIYyKEnG7S2Aj823gqKmtCqYjVGGgI4FdkTJFlRF4tuTRox0deCbGV7mKhYHsGJCJapSVeCiEmQaYDkX2YIpfhSAm_030g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📹
شات‌های‌جدید نادیا خمز دختر پاکو سرمربی سابق تراکتور؛ ایشونم بعداز اینکه اینترنت مردم ایران کامل وصل شد پست هاش رو شروع کرد به انتشار. حدود 70 درصد فالوهاش ایرانین که اون سه ماه نت نبود اونم پست نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23315" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23314">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUj44djwxTCDg-B4l2Bzj42bj_Z_hSA87YG3eqcskO-Xy2Z5gA9ME4tR_3iqaAjKAJch4r9mVckLdx3fzMc2bhBkDXwAiQPlSfTFT6PgIuGM6SRLZfUrv_4KDc769DF31MUD13LXuCvvMQuqvXMHulRI5ICo7qCHnplnSjho8D4mh3LL22SCmJ5OEgkaJ4KghaAt0d96D9lMzIQBiE69LdhPhTGYNpCHawd8Wi0Ecd-QorPJgpDG7bpJgazc54ENTmdCPyYqK21Jr746kRYyab4BEA4y0VqFzO1ow-MslNH8RYIho7etqvlFok7Zj-pexqyF3hku1Xgk-W873duZzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رونمایی از استایل جذاب و گرانقیمت قلعه نویی دربازی اول ایران مقابل نیوزیلند در WC  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23314" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23312">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5uJ92FflENWNTISyG7B2upmMJQqEw57lnQzOpgxvc55j39ZRj6oyYRHQxEeTEu1S56sduj8H1MjtusB2W4LLStVi2ZtTIfVXekrPu7YRrLFxCVhquJmrdpdKGhZTf392fDKjcNz_RfVjp5-ouPL7xzkPHI2iLfadI47sBUb0nJ6STgi70WuF5A1lX2tShh2OXsV0jbuPXrzGp_ErQZ0AiJFln2_eTyW0c4giVp-e6vEOnWVUgRbdNvKjt8QELnigkSY7jcDW4Ov8U97TrC6WhCcsWmc-TUPWV57zTn920jK3g5LVOeyCgsvxzgMgFocBZPhwfsLs0GPsCYqAXSMVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میثاقی‌به‌منتقدای‌تیم‌ملی‌روی‌آنتن زنده:آدم مفت بر از جا خالیی ......تره! همون شعر شایعه رو میگه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23312" target="_blank">📅 00:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23311">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e109d357.mp4?token=kX22flw8Dv7X6Sk_DGwikOKI8Skf-8EinlO5Ljex3GPgqpUoB30eXV6AVmhpxhlWKAI21ztc7-ZTe9VtH1EtzdABLhF_RaffBJ9VtfTiI93th2wJBSkRO885d0RgNHiA_il91gE8YOwR0Euxv6mbtPJviAB56ojT0pdlfNoQRpu7kE8PnGBGcQ6mB0BlJOgUdUuAMPnPzY7LvSb_qr2A30NEjmT95HG5C8_3KWY4rzJ1WRgWBVP6pmhtlCaLoCCaVCl9nUJTcLQ0IwDjM92XuMagxMCgashwtOz909jkTGR6z_6SaKAA5apkOcyf9GuK7qNweP5NyVlHLYjgl1PV_zZOg9L4w-mAqBdJpLVwIHxEDiu75zk2cgxGIihXde-rYge6S_VgFcV2I0wHrKOTO_zXVFeTlgxRw3GW4nSOSJTO9b8IuK49g9njxWN4dOyCOwx9AY-orAHATuMVrwmpNndePDeG8McqMsnlPWP2NmqqbXrOX2Wyek3c-Lt_TAbfpV-J-eJsx_vuuYowdu--FqWAcJ4viUg1WTH4_ri6yMNrr6FZyKEThMdsCTqo0Z3g2sAujAOmK6VdRwD3Fv2cASpiSJo-3uA0CO3tr48b8Ntpf4vMUwhPsZrm3B5vVtX5Na9YghY9FbkDEiUsGCVeS8pUaENEoPrCjq9goj_3CxM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e109d357.mp4?token=kX22flw8Dv7X6Sk_DGwikOKI8Skf-8EinlO5Ljex3GPgqpUoB30eXV6AVmhpxhlWKAI21ztc7-ZTe9VtH1EtzdABLhF_RaffBJ9VtfTiI93th2wJBSkRO885d0RgNHiA_il91gE8YOwR0Euxv6mbtPJviAB56ojT0pdlfNoQRpu7kE8PnGBGcQ6mB0BlJOgUdUuAMPnPzY7LvSb_qr2A30NEjmT95HG5C8_3KWY4rzJ1WRgWBVP6pmhtlCaLoCCaVCl9nUJTcLQ0IwDjM92XuMagxMCgashwtOz909jkTGR6z_6SaKAA5apkOcyf9GuK7qNweP5NyVlHLYjgl1PV_zZOg9L4w-mAqBdJpLVwIHxEDiu75zk2cgxGIihXde-rYge6S_VgFcV2I0wHrKOTO_zXVFeTlgxRw3GW4nSOSJTO9b8IuK49g9njxWN4dOyCOwx9AY-orAHATuMVrwmpNndePDeG8McqMsnlPWP2NmqqbXrOX2Wyek3c-Lt_TAbfpV-J-eJsx_vuuYowdu--FqWAcJ4viUg1WTH4_ri6yMNrr6FZyKEThMdsCTqo0Z3g2sAujAOmK6VdRwD3Fv2cASpiSJo-3uA0CO3tr48b8Ntpf4vMUwhPsZrm3B5vVtX5Na9YghY9FbkDEiUsGCVeS8pUaENEoPrCjq9goj_3CxM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف یاران ادین ژکو مقابل یکی از سه میزبان جام در ایستگاه اول.
🇨🇦
کانادا
1️⃣
-
1️⃣
بوسنی و هرزگوین
🇧🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23311" target="_blank">📅 00:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23310">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-rsXiXJy24Fy8-Mqw-cNeO6PcMucJ00alzmgGgIiQC0gHNFUwpohXU6PlUEWi9qvs8reSYRMOe-sQoeL6epXqdqvrFzzyMYMkwKXTsJtd8x6z__Bi2Em2spNUnez3zRkl3Zk-RSvNxfnNeAECZNAtQwvA1qe4Jy-dBY1NLJ-BlssTkxDbySI_vv4LKoK-o_JJXpdww2-eLE7EIC9jE71Ry66jJppLuVjlU20mhCypNVBs1cKvOOY7ifvFxVGb40Et7-DboDHfcRygY0i0RZbRTzMGOe_8Lw86rHeilkzRyx6i8eFXmNSuR27bCIEK7L6atX2Xw-SUBFdMgeYxpqyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول جام‌جهانی گروه B؛ شماتیک ترکیب دو تیم ملی کانادا بوسنی
🆚
هرزگوین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23310" target="_blank">📅 00:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23309">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/al1NrWt3g2w3eWuTsAXZ8dM1AFuYbE5tiGOz6MAmKcbn7n8tY3FTy9NE8zpLbD4xWCm1fu-LFB3FnP3qgrcslKenN7iEYgFcFuLU86zGXvI8TqACzSWLwsc8m_eaR1Z7ZR9httTz6ojsEA72UeBNBHOPQ-4pkVU97nCnrGqhUgEYLq4YAxA_fg4E_70j3PgyM85acsWUf0av7FCY9j6bT_un8oO_dB-LKDJu5Yn4tQ_krNzdzQ2R9fQsrLM6aZw10HctuuGcXfL_2ngqTP05EtpJHhm7IESsr-uZzLLD7pQFv3Wo5LqS927XsGJa80DcsQ5JhTZJ9oTt_c33XifEOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23309" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
