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
<img src="https://cdn4.telesco.pe/file/dX0oWOuu89-Z48s_Yi0UCAKCCBknH2JM2iUil9Da5tkZB-ZI-0rIHeC42nGZAnwfhEzVKFHiH2qifBBQeUiPUQQej1eklRa7HUPaC9_n1pVfQE2LWlevAMJtAxWqE9QQ-XR1caM4cd04pxXe6LJlCt1LALZmgAcfFcA8wKsRwnk_t3vYFIyJaZifdGTebO6quIWMOiTwSmvBOVKqvqfEaYVwRN6RuTxMUOfnUqqu3rLe1r9bxsHvM7r11SrwfOYvfljonvMdXeIaj5qvyFVq15H59X8vJ5s39ijcwCBk1pZREnrEPBHTTq8B96OuWW-DPtS3E0pAM_ZjYtQK0pRrpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 06:16:46</div>
<hr>

<div class="tg-post" id="msg-441331">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87021e9d4.mp4?token=Rb4UbQXGm4KwuV6rUuNUOFI6locOoJpD7KPIyIUgSo42Lk0WC-Wk-WFllf7XBRjeHd-OUEddGmPlHuhtkHj7h-sGbYHNcgQlELURVzc5OgkuwFoltz4vSt67pQezIPg2wz8bzpOHiG1BtcykF84luAvDqymfcVzuzqokc1PcxgpTOzBiIJ6zI9Wd65TrBK_Kc3ZAFXWfVBGavuR0nQQ8BWkVR5CMoVLS8fIqkPK-Fnt8vhF9HbQTCb37idZBEx3PKIBC7Dqq30_VYjDu-TgsWtFFmXz3tJR0rGhLo1C_AQFZTyJ64nDXlq8O6ytI4G1dkCwhTWPbZbXoJWBc8mf5SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87021e9d4.mp4?token=Rb4UbQXGm4KwuV6rUuNUOFI6locOoJpD7KPIyIUgSo42Lk0WC-Wk-WFllf7XBRjeHd-OUEddGmPlHuhtkHj7h-sGbYHNcgQlELURVzc5OgkuwFoltz4vSt67pQezIPg2wz8bzpOHiG1BtcykF84luAvDqymfcVzuzqokc1PcxgpTOzBiIJ6zI9Wd65TrBK_Kc3ZAFXWfVBGavuR0nQQ8BWkVR5CMoVLS8fIqkPK-Fnt8vhF9HbQTCb37idZBEx3PKIBC7Dqq30_VYjDu-TgsWtFFmXz3tJR0rGhLo1C_AQFZTyJ64nDXlq8O6ytI4G1dkCwhTWPbZbXoJWBc8mf5SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیاتزا پس از بازی مقابل برزیل: اگر به فصل قبل نگاه کنیم، تیم ایران بازی با برزیل را سه بر صفر در یک ساعت و پانزده دقیقه باخت، این یعنی بهتر شدن را شروع کرده‌ایم.
@Sportfars</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/farsna/441331" target="_blank">📅 06:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441330">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
آژیرهای هشدار در شمال اراضی اشغالی در پی شلیک موشک از سمت حزب‌الله به صدا درآمد.
@Farsna</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/farsna/441330" target="_blank">📅 06:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441329">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
منابع عربی: همزمان با وقوع انفجارهای جدید در بحرین، ستون‌هایی از دود در منامه، پایتخت این کشور به هوا برخاسته است.
@Farsna</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/farsna/441329" target="_blank">📅 05:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441328">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
رسانه‌های عربی: پایگاه هوایی «علی السالم» محل استقرار نظامیان آمریکایی در کویت، هدف موشک‌ها و پهپادهای ایرانی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/farsna/441328" target="_blank">📅 05:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441327">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آژیر هشدار و انفجار در کویت و بحرین
🔹
منابع عربی می‌گویند که پایگاه آمریکایی‌ها در کویت و بحرین نیز هدف عملیات موشکی و پهپادی ایران قرار گرفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/441327" target="_blank">📅 05:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441326">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171db0c3aa.mp4?token=Vw1W5KS6GYUk5kKzYvleXrTFp75ZCF3LW3on314Cv9vAAOSHuUQEJQ0kFgtQnn4kIbsa46pR9FFK11qiBKTADKo_oxHoKfkrJ2hy55D_AA-yzpEmHzoKpT3SPxIOGT0Jslik9l8AQoHiXVRy3bUxRTsFnlQUdONoxsjprBglQLmDEodY7P_GLDTSNb5B8ihO1nagS_Tl5LEU4fiGttzAKS6tfl0YPPndDTSlvgZS7V4NaCwQMMPNV32qTEeW4W9pDqvjUqxzA3PxpiQMvOEZgMvE3hhZPr28WFNQriYWUUEO6fUgbEh8YuX7oExZANwdyuOyvZomt8Z2LzkB6Asl1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171db0c3aa.mp4?token=Vw1W5KS6GYUk5kKzYvleXrTFp75ZCF3LW3on314Cv9vAAOSHuUQEJQ0kFgtQnn4kIbsa46pR9FFK11qiBKTADKo_oxHoKfkrJ2hy55D_AA-yzpEmHzoKpT3SPxIOGT0Jslik9l8AQoHiXVRy3bUxRTsFnlQUdONoxsjprBglQLmDEodY7P_GLDTSNb5B8ihO1nagS_Tl5LEU4fiGttzAKS6tfl0YPPndDTSlvgZS7V4NaCwQMMPNV32qTEeW4W9pDqvjUqxzA3PxpiQMvOEZgMvE3hhZPr28WFNQriYWUUEO6fUgbEh8YuX7oExZANwdyuOyvZomt8Z2LzkB6Asl1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکمیلی/
ناتوانی پدافند آمریکایی در اردن در رهگیری موشک‌های ایرانی
🔹
رسانه عراقی «صابرین نیوز» نوشت که انفجارهای مهیبی در پایگاه‌های «الازرق» و «موفق السلطی» به عنوان محل استقرار نظامیان آمریکا در اردن رخ داده است.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/farsna/441326" target="_blank">📅 05:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441325">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda5748c50.mp4?token=iixxj40bRx5LhCCZuHPScliYHmbkBWr7E6fMgfHBM6N18PK8ftwVBsNXZ_q6xwKr3WZYUAVcLaJUcVhFlaHnrKNycExgGek71TQc5Blqy2ExniDdKevSvcbMO2_SpkRiVTteVzoeWufA2g9rB5-SKlTqVCpcZIGb-7wbAOPoAFLiPuxXQ_l1EuA1ybDSpWQwWucGisRprTa3uLrQOdLIapmaRPz14mXG6WDCYt-ujsPdOIvPtmkhZipeUzivYmX1_dGCXsucg1arPtxOzOWqcZRRXkBVvosBQ3y4qXna7qYaeF1VbNG9tGAtu2xNpG-VnRb3C0qhZv3nDmhZy31qig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda5748c50.mp4?token=iixxj40bRx5LhCCZuHPScliYHmbkBWr7E6fMgfHBM6N18PK8ftwVBsNXZ_q6xwKr3WZYUAVcLaJUcVhFlaHnrKNycExgGek71TQc5Blqy2ExniDdKevSvcbMO2_SpkRiVTteVzoeWufA2g9rB5-SKlTqVCpcZIGb-7wbAOPoAFLiPuxXQ_l1EuA1ybDSpWQwWucGisRprTa3uLrQOdLIapmaRPz14mXG6WDCYt-ujsPdOIvPtmkhZipeUzivYmX1_dGCXsucg1arPtxOzOWqcZRRXkBVvosBQ3y4qXna7qYaeF1VbNG9tGAtu2xNpG-VnRb3C0qhZv3nDmhZy31qig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال‌شدن سامانه‌های پدافندی در اردن
🔹
منابع محلی با انتشار تصاویری از فعالیت سامانه‌های پدافند هوایی در اردن، همزمان با هدف قرارداده‌شدن پایگاه تروریست‌های آمریکایی توسط موشک‌های ایرانی خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/441325" target="_blank">📅 05:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441324">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تعیین‌تکلیف پروازهای لغوشدۀ حج؛ بازگشت زائران در ۲۲ خرداد
🔹
سازمان حج‌وزیارت: زائرانی که پروازهای آنان در روزهای ۱۸ و اوایل ۱۹ خرداد لغو شده بود، طبق برنامه‌ریزی جدید در ۲۲ خرداد به کشور بازخواهند گشت.
@Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/441324" target="_blank">📅 05:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441320">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fb30eiMIL7QdXf0kajfMHQvf2Kmp6rVhBwvwp9NSwtSZdirPCDisiAxWEqOD9AxlYCF9mQea-WtHn46MH1eDr9cyXim2ujc1X_RpfNeoL3lzBvODs-rpuUAfus6ax2eW5LHSRKDd1uR9bR82ZX5_dSOwibfqTOzqxy2O_ANYi8UpF6XIVSxhMfqXicdUHd0Me_lSHex1vXnjc_GEN-Axsu_ctuenjuRP-83s3oDi63JlfdbcYvYTWPH62P7ECDsCJYLgqIezrwfhNqVeanv2AMOWcEfjNDSDchN46XXrg4tcAUDlAFHLi4r_BUOSWrHikNnWQDkmlSYVfIwzNfnSWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QXYNLjbszZhXgV5jy0iC_SYrZ7KxJiiaytgbQbmwEDHJcd8O1ngcYJH3nJT_KpuoF6wI_4hiOKsWXLaqC70bP_ktfoNrPcASlet4HX-lvOkbmLycsbD5dfkRD9SxGwz3NAt0Z-_OGWs_rz7wuH8RImq6eS40kg85UWQCFtVcNgckz3_IiEGcm7nb3d6LN-rvUiC6PiD1v-b1_esRgDBVMs5Eqy_hGb_oRazpBwPy5xQ75Nx2xwsOpMBkMwP6EAo28CFGXA6IfzFQ-ZhYIPcDbu-6ortHr9nB5u8Tn-4VfIMR2LbAeZg69SIDjUyFB6KvdMOWjKQ7Cuy-3-peqPKfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iDjc4urOFGiOhYrrreHRmJhZFL2a912IQpx4VHhfhDfinVEyavOdh_sUlQBwCGxNvaUO0W-aetoKTxw7w31aE1ThldYhy2AnOrDyP8xSDHKPlPMc0eBdN8OZqfc8tytPMuX4jU2CvAPO0LvRLgU5u1bzJc8m9H32FQk9ifxaTNcwZoKwEPb_TziaP7_TuTht4skBYjMqUy0bd6n8B8bkDjGkQU-5dXocnlbqoIxq65wdlBrtf6mIosT0HFUXjsOIyR_RK6O7Z6CiLH-1zQE-Yne6cEYixyOqfpL4-mhFB2ZoTP5ehKyzWyHVxYH0I66anSj_elqvRwaW44JJ3ktJRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EyJzp9_u4zFf9jGo2gEA2VlrAbEhwpl73TPKk9PVFnZGu_XWJJOz3hweQQtLWyQlfw-FdgiGqmKs54sE8nDh1f_ndvcOYDZYeqserCCWPDVYNfKEnC-8BjrMxQkzCh0JKZ11Wf8rc0hVjDzkN9-ocf4VIJZFPKiyUA58or03BgLyJIHboYSKEc7QNvlndST4yO0MBXxOLeSaVYKZQH1EX-rGCSNBSSnqQklbEE9Ck6VvxJiH5NGQJCdSElbYctNar2KfatSOUL0idAXg5c-2Q6WwC5pBNml7_z0L-t8wRm76TMfrFFe94Ih1GRet0y4UsRvI35nZTBO-InCbiU8bYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۲۱ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/441320" target="_blank">📅 05:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441310">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PuEvO51upIkQoHYtu8fp0NVngDBXe2Y4MXtswKybcnbVrwpsq8aYXkGhnikjy3G5S-xAlgRR5tZGT9r-gRb_FcJcrHraIZC1P2hmQZclsPfYPrfq5SWOn5FAMKJoSbA_BDsFl2zvR0sL3dMR05SBufMhtajTCLfVmnOrFiVdXon8dTmAo7rkCEkhcEawbEJRJN1pREIqs5iMzrzbkhowuFLoPViOHriEEr5MP83kEsz6GMwl-F47ksc9cc8Nfb5_l0zgqSpoWOo65-BfZM-q6WSQUQMhb-v6Jkap_Th6ntRqUYReIAIoplljQbvQ-3ooF-sK1O_8yS8JgAvUsc09kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hBLFyRlx_dIA-9YzHJuZkxHbx-eh-Z9fo3-hWZUT08EiBRw3-cjwjG98Qf4z4mCnRZP05WSukw4DJXD7L4pBS86bL3qcPmU3sQDPYVteUEpGeOhBVShVLP4XMl8ykb6d2nGGHkV_aDiVrFtIFsJttCvcl9vOLhq5qBjyPF2KJFi8IodFQRYAW8uY8ZRAHgvh7G-2yBqz25abMVgqCK8tu9lHZUBxv9QRDFCXK2xKyCk-kUIklPR-PD7o3Igs4I-psnY1M1eIkQJW9aBICkklX7OCd-JeKZ7VtEE40ABt85OeKbG0bOSmUgLBdi3Nt20k6xvU5AeOJiCoVFxZcyfUBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3MMDtLnMfp5E5NlHQ1nsi_YGRkeV17sq0W3YX-IwhtBx0YXq_XC1LuJqzN9k5hcbJwxZI-1fjECjVtWYpCe-IEsQYswEjdMw6rhDfBKWNy8LOYr3Bmo6lKm-A6-4wHC7KBpfnVsaNpNmfE1iMsFMkqqSb5RQkGDC2H4FYGSJ9xHjhoBjupM927vcmuUG0_u_lkoA5fBsBr6eE2SJS5LpEk8SgP0Ip6zfflHIG8bplV_OoQwzGqkB61Z87ihihVJeLUj_tDXsHGJn91JfFJMRSZwIIwwuZ7OuZWFHdNsCukyrzfzw3pXMiuehdLdmx5cbRvZy8vzUX8OCrmFT0kWeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9aIBUOK-yhoYp3lqIt0oyiTXnD3uwBwP3MXzuY1XdHlsJHhEYKscW9ENOeJXRBJNLQ26oTq7GNF2J7ES-Yh-tNkS-vrE7PTaLWsF60t7ajAxm88Oj97MO8Rqenj2rbKgPP-Zpu-6CVeXPp3LqekFh4T63k4vlCcKDntnFRaBhp_QftsoHKTcotYfdIQl91X3BCkPw856MSsdr4rRg-gJpjPJZImJwF42QOvsp_jVz930xFr0bOKWTMmg_aYL079p_x33Ok64stPL4vtNGBEGvN3UpfIwNtXUf4qA8gB4Rc9mitP-CAbGaTKyR-COGBuBLtDoxc8wOw1_74KPuLNZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOaMVaQvrxko2iKTFd_TpP5DCC6SSxYosVWI1WVz5uMJnvWiRz335ZPH3ja3Ud_tHiCfYzHsl_Gsb4I07EAggiOJDYnrsm88MSXCfgKcLoosIGw-H-LbCSVIskYRnc-lBZSS9FHowkc4Tx9fSZoiMr0jGii9b2hfhJHh450I2Ouabu0pLUPSQAK5BblFkB94XB_sPEJIkCta_SqQAeoMBBrMYhHILGTqFHTTYc-9E7hpwVyfmnLn89FXkjuJs-MS0Z8FYKKUvXU2KFGv1HjGOQSXw7aDViKYBJHITbcVLMojr182L0ws5Gi_bJTMTfpg5QbYuRRlhD7lo372Smg25Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3VILuGwavpUNyueKUQT49wRtSCVrSEXcZ0jx5wWoHWxneBS5-ItJTB2cnVm1Zd1Z-X6-vPw26ffCb4xc2dWgZY5QI7s0aHYqUsQs97pARhBrKKk4wVzNhbz2VSivqFi6PNricMe4Ay9vC3w_m-HmD3_dxbqXKX2Ahkyv08CtNiESa1UF-DDNCypWBXaSi3xqETJqIFkXJMz92E-5Jl7-Rjk6nrxZ629SQNaeTBrT2PnhQb4Ur0Ap6iykUrr-ag7nhh94TWMXMuvTblbimzhIgX0dJ4K-LBB1WhumQ2GbhAOJgg5xFUR65In1Yuckf6sthKapEIQE7V79_kJksnLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cD0CS9P7DSv7KR5v9a_-m6gGPYdhTV5b1uP31P06W-dpaddfCC2Gxnk99fv-Bkjo51DNf6rTrJdOLj9h62YcHJw-0VzUxYKq4gQiC2qZO2kTC_j8tI92hRhEJQzB60cq0ZOKPd-KrnYyh9cpSjuzlQH28dkxxpvrv8zfSBCDmOjqSCZOpa23CelqtvSyZ1fl0OyBgmIoBiQs_ecL-JDycyaAoJq9PuhNeiXYZhQJokM-COaG6NIP1iayCW4oVhxg7-TRypBok59GSg4NAe6UHNMGiHo7DfVI8Wx2sMzHi6eIFrKUPXdlM7dv3_Hfi2MhQF_ZZp9R0OrTsQT5M-_-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPsfkWhf4Em7gMjB9aLVI-rnxnj9Ob9LuYoDxYGqH0m-9vI_oL7Sv5immwXyZK3z3vGu2lnJeCus35PakMyxWRNCaWNgjFsuaLEz8cbFEImu3uFcdzyYNxKF-PrgyaAJAH79kOZQiOzbJMmTuF8Imklwkvm0lvujFr_Ymshb4Th4Bi_O5TVaQtS3hbVtpXNs28rD71hgiFWEtmz7U3n0Lh0O19efpELFuFWoCb2Cb2fQdNJ-pUCUjhOu3a5avEbR9GDpGWcGblAHMIv3sKwjBgg57O3zaYSew-w_WUKmhSEVhbJeptVWMSP48U8uReyByHbbFFSBpECwZ5ltG1xjvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aApvj703HGlMtW8t6IViS5kj9hvX7qBeJsWBgisJXWdIUIhwpUgu8k558dV_Al-6T8POeauC363LWXjuyxCmuF4xTF1Rwtuz4aQNLaRggHPPHoDA-1U1UEfsy2cn6Kld0nrVwqGvinpZzXOZGMTHvXTqkeUTyO8dU8hzvSq7pPD5ev6EW2P5_V5g61g86UQW3Aqutr0wYlxzPbTJgOkDKZMH7JbJiJ0DY1zV_y3w58h5gq5iUWQKUsEIOCcJX-CvhUFe0vyI3Fz4COxylbwYA2kt221WvqAOLyuAlu7W-4UnjuUUH_sy683VxFtPLrCDJ-qCSOKzWgyajjrQy4L8Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mFtRsv3RpCqoxhN3gwutAAzZw-F0qdlatbJJ4At0X5hVCozulPXZVyxV6WJXVOLlxM6oMQACmw8DX6U43DJ4cQ6elUoztTxSaEWrZ6Huctdoe48iymC9ckPcDU-G9VfW9yxIA1-Ks4YqtopHBHU74vQPHcb3Z9Mxi5zAVZZc4vC86DZ0xDUWYsspj3GGz4tkTzGOvVhnzV7rlvmfQv2ET_5fQFmvEIutXG_2JC7YshejnNCV76tHCOwO5HbrVeJMdQ-mQwBf-HYVuywjBj6T3eRlrDhN6C-V3Ar37Ou9Xj7UYMugOT_jZm-qjG-hQHQ6cNzqREChVJOuhn84t-qczQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/441310" target="_blank">📅 05:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441309">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌
🔴
منابع عربی: انفجار‌های پی‌درپی ناوگان پنجم آمریکا در بحرین را به لرزه درآورده است. @Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/441309" target="_blank">📅 04:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441308">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVUQrcoCfmnm2Da-gEHzaz38UNnQFdTq3rp34VEBLWbRPJaDMOMW2e82t2kyZo1yv0x9P1KT-7RfamY1jyDtnumxIVnIUeD5E91YlWX0HHvvslXbLyRl_rZvPz7dQrpicl65XvrKH0iE6X1735WCQIkoucGeUS_GqMQGnMtow9RDQ3gZzMv2KNWojxAq8J6PpU7oeUvuBGqnSDy4izV8RF6e0AJRBUsYalKUw-4Yya4IDu20EXQE7tdX82N1ex_lIqM11NHgtV2TySQUMYrHeBpi65eygmeWsyLIefHWbOWp6u4XAKz9FahTTVFpBmYfXpE3Qorg60cwxg0_e0-u1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
فرمانده هوافضای سپاه: تنگه مقدس هرمز را ناامن می‌کنید؟! منطقه را برایتان جهنم می‌کنیم.
🔹
سردار موسوی: تنگۀ مقدس هرمز را ناامن می‌کنید؟! از سراسر ایران منطقه را برایتان جهنم می‌کنیم. این پاسخ جسارت آمریکایی‌ها در منطقه است باذن الله.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/441308" target="_blank">📅 04:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441307">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شنیده‌شدن آژیر هشدار و انفجار در بحرین
🔹
برخی منابع عربی گزارش دادند که همزمان با فعال‌شدن آژیرهای هشدار در بحرین، موشک‌های ایرانی به مقر ناوگان پنجم نیروی دریایی آمریکا اصابت کردند. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/441307" target="_blank">📅 04:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441306">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLRuWVhliHiThBT6aqBQzl1KWb2xChgFUgLBL_44J1GUyzi_klwn_aD58pouut7MRX-KAq7x9OA0p3wteF2-MAmkwW58yzSSudlF13Ed_lB7q0TEySQ2wrPZYhYAj8NDC5Jhy7ezWnEJRANwG7wkPe9S8qdYEYIKap6V0CDBJwp8xbXo-GpfGj2lvPUH17NgKQmBZd3FFIie_yRUWn_HTOhBWwK6DVGYrrZ8Yl4a7CoPVJeO2KS9_yNU9CzNCCa1unoLBb8ay6rZh5qndu5ER2G8fGD5EzUx4FfYgP7dPKB5UQAvN0sH-j8l5mLxgz4h2hV6KiKkObxkX6GSjmMWCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تردد در تنگهٔ هرمز ممنوع شد
🔹
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): از این لحظه به‌دلیل ناامنی در منطقه، تنگهٔ هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می‌شود و هرگونه تردد مورد اصابت قرار خواهد گرفت.
🔹
در ادامهٔ شرارت‌های آمریکای جنایتکار…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441306" target="_blank">📅 04:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441305">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">شنیده‌شدن آژیر هشدار و انفجار در بحرین
🔹
برخی منابع عربی گزارش دادند که همزمان با فعال‌شدن آژیرهای هشدار در بحرین، موشک‌های ایرانی به مقر ناوگان پنجم نیروی دریایی آمریکا اصابت کردند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/441305" target="_blank">📅 04:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441304">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
سپاه پاسداران: ۱۸ هدف مهم متعلق به ارتش شرور آمریکا طی ۲ موج عملیاتی مورد اصابت قرار گرفت
🔹
نیروی هوافضا و نیروی دریایی سپاه سحرگاه امروز در تنبیه متجاوز و پاسخ به تعرض ارتش کودک‌کش آمریکا به بعضی از واحدهای خدماتی و پاسگاه‌های ساحلی سپاه و فرماندهی انتظامی…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441304" target="_blank">📅 03:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441303">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
سپاه پاسداران: ۱۸ هدف مهم متعلق به ارتش شرور آمریکا طی ۲ موج عملیاتی مورد اصابت قرار گرفت
🔹
نیروی هوافضا و نیروی دریایی سپاه سحرگاه امروز در تنبیه متجاوز و پاسخ به تعرض ارتش کودک‌کش آمریکا به بعضی از واحدهای خدماتی و پاسگاه‌های ساحلی سپاه و فرماندهی انتظامی و محوطه فرودگاه بندرعباس، طی ۲ موج عملیاتی ۱۸ هدف مهم متعلق به ارتش شرور امریکا در پایگاه های هوایی علی السالم و احمدالجابر و همچنین پایگاه‌های هوایی شیخ عیسی را مورد اصابت قرار دادند و منهدم کردند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/441303" target="_blank">📅 03:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441302">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
تهاجم پهپادی ارتش به ناوگان پنجم آمریکا در بحرین
🔹
درپی تجاوز ارتش تروریستی آمریکا به جنوب کشور، ناوگان پنجم این کشور در بحرین، آماج حملات پهپادی ارتش، قرار گرفت.
🔹
در این موج از حملات پهپادی ارتش، آنتن های ارتباطی و تاسیسات راداری سامانه پاتریوت ناوگان پنجم مورد هدف قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/441302" target="_blank">📅 03:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441301">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd9f7c8b7.mp4?token=jDRzXz4XX4iCugWOwX8z_8yC1OOl8XlDlopMFVNFTpFWqerV8aguwjevpqLYg5TmxMgxsjaOE56CuCY99VzWCAglw_kehqHQwjj9vEr8K4RKSyesNIBj6V0M9xci9icEi8CYpBh3TFQKwMWQvcGFsAqcBeHNpoqpk2JD_qxnEOlfAB8gk2Ew6TlVgCo0S9o5tsj_nOEzEsAQT7ZAOsqS_VVQn7jPM56cvA2TnXfAdl5fWoRkzFTexKPyPyeKoJrdeWlQjQG8VmnuVBAgycUuRbPw0lfRErJFshwAYCWsPNkkWDRU6S_Mk3V1-xPG9VGfnna3ztr85IkwB4AyiYCaf5tsYCSX5f2QMZUkSgDF8cqCrw5dIVYZ73QpNkBVmZ3qH98tgOag6qp6DFj8Mi6sk3bLVYQrl90sX3wHqdtCxZZkVVDX_07pag46TnHm9Jkj0gBUPiKHRQvpNudAXLHI39o_0dicNXuVwGICaIibmWHxy28TJfZRT5DU-NkxGu_tG-3CS1ZwGkBy93gGaeQTgfMBvstgxzxWE_5aDbhxYmrJcnVJ7ZN60ilQX5gftMx3BfDnJWrKG_pMuZktZs7ujlX9jYA1WwPqNNrM8mvrULU7O3raOc8icWrRqPT_GDdoondJjEcbIXlG98PTQ6EE3Rw2zSCP6_J2Tede1vSlxJs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd9f7c8b7.mp4?token=jDRzXz4XX4iCugWOwX8z_8yC1OOl8XlDlopMFVNFTpFWqerV8aguwjevpqLYg5TmxMgxsjaOE56CuCY99VzWCAglw_kehqHQwjj9vEr8K4RKSyesNIBj6V0M9xci9icEi8CYpBh3TFQKwMWQvcGFsAqcBeHNpoqpk2JD_qxnEOlfAB8gk2Ew6TlVgCo0S9o5tsj_nOEzEsAQT7ZAOsqS_VVQn7jPM56cvA2TnXfAdl5fWoRkzFTexKPyPyeKoJrdeWlQjQG8VmnuVBAgycUuRbPw0lfRErJFshwAYCWsPNkkWDRU6S_Mk3V1-xPG9VGfnna3ztr85IkwB4AyiYCaf5tsYCSX5f2QMZUkSgDF8cqCrw5dIVYZ73QpNkBVmZ3qH98tgOag6qp6DFj8Mi6sk3bLVYQrl90sX3wHqdtCxZZkVVDX_07pag46TnHm9Jkj0gBUPiKHRQvpNudAXLHI39o_0dicNXuVwGICaIibmWHxy28TJfZRT5DU-NkxGu_tG-3CS1ZwGkBy93gGaeQTgfMBvstgxzxWE_5aDbhxYmrJcnVJ7ZN60ilQX5gftMx3BfDnJWrKG_pMuZktZs7ujlX9jYA1WwPqNNrM8mvrULU7O3raOc8icWrRqPT_GDdoondJjEcbIXlG98PTQ6EE3Rw2zSCP6_J2Tede1vSlxJs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اسرائیلی‌ها در حملات امشب به  ایران نقشی نداشتند.   @Farsna - Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/441301" target="_blank">📅 03:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441300">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
تردد در تنگهٔ هرمز ممنوع شد
🔹
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): از این لحظه به‌دلیل ناامنی در منطقه، تنگهٔ هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می‌شود و هرگونه تردد مورد اصابت قرار خواهد گرفت.
🔹
در ادامهٔ شرارت‌های آمریکای جنایتکار…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/441300" target="_blank">📅 03:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441299">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6sxKtSc8ypCuBe25EflyUsJ0D4HSXFwAuwNSGw8szOLu9-sHaf8cMlwn2ao4PSSTjodpiX1-_ZtqAFSfcHRHktKdvAMUeyxQ50XpMbVXpsLM2wgK5qD24C7x31aAi6sk9xlvJMFgaK0OcIPw7bnVVzXimoAnjIjMB7UNCy38CB6bnFu7d2DI__YHY9vGelIPruH7unFjN6l9-RCpG81_g_MJ3MP7GVOY9agdG7vF_jY1UVn4W4NFHVG62CSx7n7e-fi4eUFJEgOV1kCnEKzlPgIgRTOIXCYWVBnZa_pbKpUNwJgVdVjh7ddsCHh38T-buQPSkSXgnLzAIee8TV8Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ درباره توقف حملات به ایران
🔹
رئیس جمهور آمریکا در مصاحبه با شبکه «فاکس‌نیوز» مدعی شد که تجاوزات نظامی به ایران و نقض آتش‌بس به‌زودی متوقف خواهد شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/441299" target="_blank">📅 03:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441298">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ادعای ترامپ درباره توقف حملات به ایران
🔹
رئیس جمهور آمریکا در مصاحبه با شبکه «فاکس‌نیوز» مدعی شد که تجاوزات نظامی به ایران و نقض آتش‌بس به‌زودی متوقف خواهد شد.
@Farsna
- Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/441298" target="_blank">📅 02:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441297">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌
🔴
نیروی دریایی سپاه: تنگۀ هرمز تا اطلاع ثانوی بسته می‌شود
🔹
درپی نقض مکرر شرایط آتش‌بس توسط دشمن آمریکایی، تنگۀ هرمز تا اطلاع‌ثانوی مسدود می‌شود.
🔹
هشدار می‌دهیم هیچ شناوری از لنگرگاه خود در خلیج‌فارس و دریای عمان حرکت نداشته باشد. نزدیک‌شدن به تنگۀ هرمز…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/441297" target="_blank">📅 02:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441296">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
تردد در تنگهٔ هرمز ممنوع شد
🔹
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): از این لحظه به‌دلیل ناامنی در منطقه، تنگهٔ هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می‌شود و هرگونه تردد مورد اصابت قرار خواهد گرفت.
🔹
در ادامهٔ شرارت‌های آمریکای جنایتکار…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/441296" target="_blank">📅 02:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441295">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
تردد در تنگهٔ هرمز ممنوع شد
🔹
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): از این لحظه به‌دلیل ناامنی در منطقه، تنگهٔ هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می‌شود و هرگونه تردد مورد اصابت قرار خواهد گرفت.
🔹
در ادامهٔ شرارت‌های آمریکای جنایتکار…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/441295" target="_blank">📅 02:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441292">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
تردد در تنگهٔ هرمز ممنوع شد
🔹
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): از این لحظه به‌دلیل ناامنی در منطقه، تنگهٔ هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می‌شود و هرگونه تردد مورد اصابت قرار خواهد گرفت.
🔹
در ادامهٔ شرارت‌های آمریکای جنایتکار و با توجه به آغاز حملات ارتش متجاوز آن کشور به برخی از مناطق جنوب در استان هرمزگان، از این لحظه به‌دلیل ناامنی در منطقه، تنگهٔ هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته است.
🔹
ادعای آمریکا مبنی بر عبور کشتی از تنگهٔ هرمز تکذیب می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/441292" target="_blank">📅 02:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441291">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تکمیلی/ گزارش‌های اولیه از حمله به کشتی‌های آمریکایی در تنگه هرمز
🔹
رسانه عراقی «صابرین‌نیوز» بامداد پنجشنبه گزارش داد که کشتی‌های آمریکایی در نزدیکی تنگه هرمز هدف حملات موشکی و پهپادی نیروهای مسلح ایران قرار گرفته‌اند.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/441291" target="_blank">📅 02:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441290">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
تکذیب وقوع انفجار در عسلویه
🔹
بررسی‌های خبرنگار فارس در عسلویه حاکی است تا این لحظه هیچ انفجاری در محدوده پتروشیمی و پالایشگاهی این منطقه صورت نگرفته است و اخبار منتشر شده در این خصوص کذب است.
🔹
فرماندار عسلویه نیز در گفت‌وگو با خبرنگار فارس اصابت هرگونه پرتابه و وقوع انفجار داخل محدوده این شهرستان را تکذیب کرد.
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/441290" target="_blank">📅 02:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441289">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌
🔴
گروه هکری حنظله: بخش بزرگی از موج اول و دوم حملات ارتش تروریست آمریکا تا این لحظه به‌خاطر عملیات واحدهای جنگ الکترونیک مختل شده است. @Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/441289" target="_blank">📅 02:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441288">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌
🔴
گروه هکری حنظله: آغاز پاسخ ترکیبی، قاطع و ویرانگر اتاق عملیات مشترک فرماندهی سایبری حنظله و سپاه پاسداران به دشمن تا دقایقی دیگر رقم خواهد خورد. @Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/441288" target="_blank">📅 02:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441287">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌
🔴
گروه هکری حنظله: آغاز پاسخ ترکیبی، قاطع و ویرانگر اتاق عملیات مشترک فرماندهی سایبری حنظله و سپاه پاسداران به دشمن تا دقایقی دیگر رقم خواهد خورد. @Farsna</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/441287" target="_blank">📅 01:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441286">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تکمیلی/
گزارش‌های اولیه از حمله به کشتی‌های آمریکایی در تنگه هرمز
🔹
رسانه عراقی «صابرین‌نیوز» بامداد پنجشنبه گزارش داد که کشتی‌های آمریکایی در نزدیکی تنگه هرمز هدف حملات موشکی و پهپادی نیروهای مسلح ایران قرار گرفته‌اند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farsna/441286" target="_blank">📅 01:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441285">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌
🔴
گروه هکری حنظله: واحدهای جنگ الکترونیک و اختلال سیگنال «حنظله» هم‌اکنون درحال مختل‌کردن فعالانه سیستم‌ها و سیگنال‌های دشمن هستند. @Farsna</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farsna/441285" target="_blank">📅 01:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441284">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‌
🔴
وبگاه آکسیوس به‌نقل از مقام‌های آمریکایی: آمریکا حملات را با هدف تحت فشار قراردادن تهران برای امضای توافق انجام داده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farsna/441284" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441282">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌
🔴
سازمان تروریستی سنتکام: ‌به دستور ترامپ، ارتش آمریکا حملات بیشتری را علیه چندین هدف در ایران آغاز کرده است. @Farsna</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farsna/441282" target="_blank">📅 01:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441281">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
دقایقی پیش صدای چند انفجار از سمت غرب بندرعباس به گوش رسید
🔹
مردم در کرگان میناب هم صدای چند انفجار شنیده‌اند.
🔹
هنوز محل دقیق این انفجارها مشخص نيست.
🔸
دقایقی پیش یک مقام ارشد آمریکایی به رسانه‌های صهیونیستی گفت که حملات به چند نقطه در ایران در حال انجام…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farsna/441281" target="_blank">📅 01:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441280">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
دقایقی پیش صدای چند انفجار از سمت غرب بندرعباس به گوش رسید
🔹
مردم در کرگان میناب هم صدای چند انفجار شنیده‌اند.
🔹
هنوز محل دقیق این انفجارها مشخص نيست.
🔸
دقایقی پیش یک مقام ارشد آمریکایی به رسانه‌های صهیونیستی گفت که حملات به چند نقطه در ایران در حال انجام است.
@Farsna</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farsna/441280" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441279">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در سیریک و قشم
🔹
دقایقی پیش صدای انفجارهایی در قشم و سیریک به گوش رسید؛ همزمان پدافند هوایی در قشم شروع به فعالیت کرده است.
🔸
هنوز محل دقیق و منشا این انفجارها مشخص نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farsna/441279" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441278">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
گروه هکری حنظله: ما هر حرکت و هر جلسه مخفی دشمن را دیده و شنیده‌ایم. به‌زودی دشمن خواهد فهمید یک سال جمع‌آوری حساس‌ترین اطلاعات چه معنایی دارد.
🔹
ما منتظر حماقت شما هستیم، زمانی که نتایج یک سال جمع‌آوری اطلاعات فاش خواهد شد. به جهنم خوش آمدید!
@Farsna</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farsna/441278" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441277">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f5d98526.mp4?token=dScEM_vaV5pr2jNZmtIkUzG-lcp6WDFl0pcokEMKt-LDR_ag05c_WssQghrJVZHBOUkLR8HZ096E8mglkKdqvJMOeFD2jbrpe5_2xM4F0Bj7E01KL6mt0wQ2yooEO0hR8aGKmXcl3qOR8nNk-mlketXGX-hZoK-4JOnrOSMxOKdR8artgWFJrMB1ctyEYFNu7sYywai6VYe84zYo79xLIaZDLWAJa7AZa95fHAm5oJ0oy_COaMlLKavFfANyOTAptxzxmhRNjdFsjbBfkoo-3_v4nzLwDfPFnSxYCOMnfqjHyKmFamEUocr3ywfQBnERmkTsw8Y7l_AAcp_PDGE3jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f5d98526.mp4?token=dScEM_vaV5pr2jNZmtIkUzG-lcp6WDFl0pcokEMKt-LDR_ag05c_WssQghrJVZHBOUkLR8HZ096E8mglkKdqvJMOeFD2jbrpe5_2xM4F0Bj7E01KL6mt0wQ2yooEO0hR8aGKmXcl3qOR8nNk-mlketXGX-hZoK-4JOnrOSMxOKdR8artgWFJrMB1ctyEYFNu7sYywai6VYe84zYo79xLIaZDLWAJa7AZa95fHAm5oJ0oy_COaMlLKavFfANyOTAptxzxmhRNjdFsjbBfkoo-3_v4nzLwDfPFnSxYCOMnfqjHyKmFamEUocr3ywfQBnERmkTsw8Y7l_AAcp_PDGE3jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محمدی، تحلیلگر مسائل راهبردی: کشورهای منطقه متوجه شده‌اند که اگر می‌خواهند امنیت داشته باشند باید هزینه‌اش را بپردازند
🔹
تنگهٔ هرمز دیگر به حالت سابق برنمی‌گردد و هرکس زیرساخت تهدید ایران را میزبانی کند آسیب خواهد دید.  @Farsna</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farsna/441277" target="_blank">📅 00:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441276">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ce3772115.mp4?token=aqCzPz1kpGC23p8JhZsHXhheYiZjlf0ffECL0JNGkwKbe9C3CGM_O6e677_dXcCq8UfH8hxpDVxkQWBf5BUSfL93aegsiBYLnMXHv3hDBcnISy2l96VUUb7K9pZ-0BeezjuG-RF6lo3hNpsrpNdDjurvkXnV3JdeQUPNJm_CiSARdxNAZiJrppiYIVr27U1KwnDGekmqw9Ny2pW_x1XcHbtbr4xljl7BN8fDc9eqnPUNHhFxbboJQ5QfaEk1ZltZ8XJQm1mDL1vGbcC05Smkmbaz8a9HNDz5x_P2CGKmhc8fzItCmbIsbYSHwe_I-cswZujEoTrUSA0CXmYKfL5tcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ce3772115.mp4?token=aqCzPz1kpGC23p8JhZsHXhheYiZjlf0ffECL0JNGkwKbe9C3CGM_O6e677_dXcCq8UfH8hxpDVxkQWBf5BUSfL93aegsiBYLnMXHv3hDBcnISy2l96VUUb7K9pZ-0BeezjuG-RF6lo3hNpsrpNdDjurvkXnV3JdeQUPNJm_CiSARdxNAZiJrppiYIVr27U1KwnDGekmqw9Ny2pW_x1XcHbtbr4xljl7BN8fDc9eqnPUNHhFxbboJQ5QfaEk1ZltZ8XJQm1mDL1vGbcC05Smkmbaz8a9HNDz5x_P2CGKmhc8fzItCmbIsbYSHwe_I-cswZujEoTrUSA0CXmYKfL5tcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محمدی، تحلیلگر مسائل راهبردی: ما درحال آمریکازدایی از کشورهای منطقه هستیم
🔹
کشورهای منطقه متوجه شده‌اند که میزبانی نظامی آمریکا برایشان تبعات دارد.  @Farsna</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farsna/441276" target="_blank">📅 00:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441275">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c52c0921.mp4?token=eIbWVPmpWJ1AfzLrcF_HJjR7zJ4NjGp2f9ePQ9mWdRBcwMnTnrUQ7lYydXAgQpZ4h9lwGF7GFwJcl3lVBOUGuE8Gnm5cL8OgyomGSGVw9wvSubJjQNOqvIIpHtp5fmZbqSgTinUWIqxpt87oDfCBZPx2yLuKQ5P2zkBh4jxSIpq32fKXGFgqWWuLwyAMiTwkusYhKGWn3sWiRG_K7B5ouHLoEwYZhnNtmFhE0aE2eIxBHZZc-4StPAovOimsOcewGJ8bygysuMAqV9sU7BRGbT3Glb_sBiycWWZPCKikK7zGxpZ2GwImnUD_NtvQtCe0Reswy5NLW93IT9IiNcUBGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c52c0921.mp4?token=eIbWVPmpWJ1AfzLrcF_HJjR7zJ4NjGp2f9ePQ9mWdRBcwMnTnrUQ7lYydXAgQpZ4h9lwGF7GFwJcl3lVBOUGuE8Gnm5cL8OgyomGSGVw9wvSubJjQNOqvIIpHtp5fmZbqSgTinUWIqxpt87oDfCBZPx2yLuKQ5P2zkBh4jxSIpq32fKXGFgqWWuLwyAMiTwkusYhKGWn3sWiRG_K7B5ouHLoEwYZhnNtmFhE0aE2eIxBHZZc-4StPAovOimsOcewGJ8bygysuMAqV9sU7BRGbT3Glb_sBiycWWZPCKikK7zGxpZ2GwImnUD_NtvQtCe0Reswy5NLW93IT9IiNcUBGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محمدی، تحلیلگر مسائل راهبردی: با دشمن صلحی درکار نیست؛ از دشمن تحقیرشده می‌شود امتیاز گرفت اما امتیازی که می‌گیرید باید طوری باشد که فردا مذاکره به‌هم خورد امتیازی که گرفته‌اید باقی بماند.
🔹
ما به دشمن امتیاز اساسی نمی‌دهیم و امتیاز نقد می‌گیریم و می‌دانیم…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farsna/441275" target="_blank">📅 00:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441274">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/289c9b07a9.mp4?token=fYqOXRGxelSYwphk3KNiFqtUZKtczQ7lWecCEHEQ-OFlqtcdc7Elr6oY-KSYwUlbCuXBTx5PC0_yR1HjXwQQkVP4_J0DOpgxuP2zwrXL9a8EYVzrGkYVgmnONHrAHbEGqZG4F_FDI-MVp0GwGtuTQYz05gk14CzK97rhNGZfPRO794F6BYvMmT3XI70nvtigrcTgXSFrU6a7hvLGhgbt2T7tHzZuVv6Fc7ZzWBugkboj6YZmPsVBBs-j4MMVoijA1I0CIWZKGDFtFmOMIEj_IAIQTitUX3U_q5tBQzmf7zV7-wpBrYLPSB7JGND_rQ5WDIraWziOIL030dEmMIMUdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/289c9b07a9.mp4?token=fYqOXRGxelSYwphk3KNiFqtUZKtczQ7lWecCEHEQ-OFlqtcdc7Elr6oY-KSYwUlbCuXBTx5PC0_yR1HjXwQQkVP4_J0DOpgxuP2zwrXL9a8EYVzrGkYVgmnONHrAHbEGqZG4F_FDI-MVp0GwGtuTQYz05gk14CzK97rhNGZfPRO794F6BYvMmT3XI70nvtigrcTgXSFrU6a7hvLGhgbt2T7tHzZuVv6Fc7ZzWBugkboj6YZmPsVBBs-j4MMVoijA1I0CIWZKGDFtFmOMIEj_IAIQTitUX3U_q5tBQzmf7zV7-wpBrYLPSB7JGND_rQ5WDIraWziOIL030dEmMIMUdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی، عضو کمسیون امنیت ملی مجلس: اگر آمریکا در یک تفاهم محاصره دریایی را برندارد، ما حتما باید با روش‌های ویژه محاصره را بشکنیم.  @Farsna</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farsna/441274" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441273">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1576c09b9.mp4?token=U5BinM-CZeYbVyLDcYPAIcQOVprXqM92tVcYZgENQ_lXecM-E8of6vWmhmGXmUf-3SUk9VTHf9j9vlnXnhT_qS-3IeAtomLGmSI6F_KrL_Aui5L5nFkQQK4JW5zT2NIuuB1QPOdU6BWZismFjCg49fKIat5absWioy8qQF2cVuZLhpcrmjF3TiQL7Kn8lzWcSxqux7zovJHzbw-T_jLiPfUVgK9ycDfOdel2YtjMRtWihlzoyxluw-P3s-_9zZj7H9Vw6mOOhtEjkxVyuJ-Qqfqm9Cb83LlU6S8Q6HNsgwQ04VNfD6jiekczXKkEn9nSnYb0D9onwsNBCBKEgr9xKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1576c09b9.mp4?token=U5BinM-CZeYbVyLDcYPAIcQOVprXqM92tVcYZgENQ_lXecM-E8of6vWmhmGXmUf-3SUk9VTHf9j9vlnXnhT_qS-3IeAtomLGmSI6F_KrL_Aui5L5nFkQQK4JW5zT2NIuuB1QPOdU6BWZismFjCg49fKIat5absWioy8qQF2cVuZLhpcrmjF3TiQL7Kn8lzWcSxqux7zovJHzbw-T_jLiPfUVgK9ycDfOdel2YtjMRtWihlzoyxluw-P3s-_9zZj7H9Vw6mOOhtEjkxVyuJ-Qqfqm9Cb83LlU6S8Q6HNsgwQ04VNfD6jiekczXKkEn9nSnYb0D9onwsNBCBKEgr9xKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی، عضو کمسیون امنیت ملی مجلس: دست نیروهای مسلح ما روی ماشه است.  @Farsna</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/441273" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441272">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/decbecc010.mp4?token=E0wiSYvwk96UtFSVBNtyy_siQ-5I4wQ7Z0hJKECmbhGOGmtkz2Us0HRsXbUX1h2ZCV1joiIhFfTI4wXVicq-Z-pWakY0dbN8JeYngIKYU2QLSG8GBz7iGcwbWFGypRWWOQXWfMSccylmVyz9eGsHfRC7o2yBaoGb2y9w--FGwZy_wrDJcL-t7ThyxkJr-q2P_ZesIip_rb10nfPkClZRjwDTjIx_mGT_nrDkK0fLd-Ze0kFs6phEUbyFSie6LGca9cv1Tb6C7Rgf8bLuQo2ImG2s6q-NbwoOanoujjifu1x2n8S06uifA1s1ElwdQAGcYwVywLCBmYL95mrEazPrZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/decbecc010.mp4?token=E0wiSYvwk96UtFSVBNtyy_siQ-5I4wQ7Z0hJKECmbhGOGmtkz2Us0HRsXbUX1h2ZCV1joiIhFfTI4wXVicq-Z-pWakY0dbN8JeYngIKYU2QLSG8GBz7iGcwbWFGypRWWOQXWfMSccylmVyz9eGsHfRC7o2yBaoGb2y9w--FGwZy_wrDJcL-t7ThyxkJr-q2P_ZesIip_rb10nfPkClZRjwDTjIx_mGT_nrDkK0fLd-Ze0kFs6phEUbyFSie6LGca9cv1Tb6C7Rgf8bLuQo2ImG2s6q-NbwoOanoujjifu1x2n8S06uifA1s1ElwdQAGcYwVywLCBmYL95mrEazPrZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی، عضو کمسیون امنیت ملی مجلس: ایران گزینه خروج از NPT را در اختیار دارد.  @Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/441272" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441271">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8f9a9f8d.mp4?token=QVaximrlZrSuBHej2s9_NrpO4s7ncBaLzWvcPFJSzEex7JR85Q8ZkPqwkPiuAcbKawNc_D5ZEHMLBPz0x_nRE5dyL91LZqGo9LS4VKHLRuPQltqqgSCD-DIF2XaaIKvG2faSZEo1DT9LUvXqOk9isB9YOltApc80sd2ucZ27rlfzO17fL3UEpd84wNK-gnr4GcdM6qjGwe3KYxztI5XnZS7U59FQUbjooB_Owq8QmEzagjmqKeE9X93np5o_zOxQb-b7kccriG93pjD1yLgJWiWpIbJjxnFUD-HW4Yu-priEJaxBQoREvH8LxgCrTNSiU5fpLlCS4V9D4lPqMq7Wug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8f9a9f8d.mp4?token=QVaximrlZrSuBHej2s9_NrpO4s7ncBaLzWvcPFJSzEex7JR85Q8ZkPqwkPiuAcbKawNc_D5ZEHMLBPz0x_nRE5dyL91LZqGo9LS4VKHLRuPQltqqgSCD-DIF2XaaIKvG2faSZEo1DT9LUvXqOk9isB9YOltApc80sd2ucZ27rlfzO17fL3UEpd84wNK-gnr4GcdM6qjGwe3KYxztI5XnZS7U59FQUbjooB_Owq8QmEzagjmqKeE9X93np5o_zOxQb-b7kccriG93pjD1yLgJWiWpIbJjxnFUD-HW4Yu-priEJaxBQoREvH8LxgCrTNSiU5fpLlCS4V9D4lPqMq7Wug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی، عضو کمسیون امنیت ملی مجلس: دست نیروهای مسلح ما روی ماشه است.  @Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/441271" target="_blank">📅 00:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441270">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ceb7ab56.mp4?token=hB5QTRL-NDo3nmIBLA4PQQz7_YQnkUcot3mziwDaRdPiAWXOkShY-fyJANDpHUJGFahouICNHKBNSbiLuOW4X7yThaVaFZmHMWPmR1El8kCe5oc12GufRZUBTcyJoaXF89YBQE6bZUPxRnonjTHyFrF8ztdPZLrQc1CM37g0dRZP69Kf9uBH47M_Zm5szXGJb6B-Um_8R4_RT9OuQ3ahrvV2DUkTJm4CW-_Q_ouLvwdF_EmKlnPU2BZsIG9IW1J2vIEkkMO7ROidayx2AQyTgB6RdLz_pXJDcmSb4pLwVcmnekhuA7WYzlsuANKqvx5o3lgPyMIPhjMgJiQ-WV3Lug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ceb7ab56.mp4?token=hB5QTRL-NDo3nmIBLA4PQQz7_YQnkUcot3mziwDaRdPiAWXOkShY-fyJANDpHUJGFahouICNHKBNSbiLuOW4X7yThaVaFZmHMWPmR1El8kCe5oc12GufRZUBTcyJoaXF89YBQE6bZUPxRnonjTHyFrF8ztdPZLrQc1CM37g0dRZP69Kf9uBH47M_Zm5szXGJb6B-Um_8R4_RT9OuQ3ahrvV2DUkTJm4CW-_Q_ouLvwdF_EmKlnPU2BZsIG9IW1J2vIEkkMO7ROidayx2AQyTgB6RdLz_pXJDcmSb4pLwVcmnekhuA7WYzlsuANKqvx5o3lgPyMIPhjMgJiQ-WV3Lug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی، عضو کمسیون امنیت ملی مجلس: دست نیروهای مسلح ما روی ماشه است
.
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/441270" target="_blank">📅 00:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441269">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
منابع خبری از حملات هوایی رژیم صهیونیستی به دو شهر در منطقۀ بنت‌جبیل در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/441269" target="_blank">📅 00:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441268">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/177d95a081.mp4?token=lDOiCa9vC2RLE6OkY-ax2jz-hutgvu94Ki4XlW8CsvUv5FCwAkBj028QmgUN-xdpVsnxpJO8NHPH9VATZ9IKY0XYFn3HwJyTv2pxM7JyWeJGRjE1OFFnkk3iN_98Xe9L3KEGTiPpo6hz7lZwEeKJTXsUcCFOIgrViPvv-bS0RpgSM9_gf98Ysphq1yyPPXvSryaRC9bN8Wui6Q2tHa4NsbxswNMLGo-canS0x4hjY_bZXD12xB4N59ziIaMi0OBHEJhG1tEwE0ahf_vwk18J3WdKUY4e4HtUNnWni-JNpzusYurSGOTgCnqJLbRl340YmnqpHTqYc86U9Muo8QJSDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/177d95a081.mp4?token=lDOiCa9vC2RLE6OkY-ax2jz-hutgvu94Ki4XlW8CsvUv5FCwAkBj028QmgUN-xdpVsnxpJO8NHPH9VATZ9IKY0XYFn3HwJyTv2pxM7JyWeJGRjE1OFFnkk3iN_98Xe9L3KEGTiPpo6hz7lZwEeKJTXsUcCFOIgrViPvv-bS0RpgSM9_gf98Ysphq1yyPPXvSryaRC9bN8Wui6Q2tHa4NsbxswNMLGo-canS0x4hjY_bZXD12xB4N59ziIaMi0OBHEJhG1tEwE0ahf_vwk18J3WdKUY4e4HtUNnWni-JNpzusYurSGOTgCnqJLbRl340YmnqpHTqYc86U9Muo8QJSDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محمدی، تحلیلگر مسائل راهبردی: بیش از چند هفته‌ است آمریکایی‌ها تلاش می‌کنند راه کوچکی در تنگهٔ هرمز باز کنند که بگویند تنگه را باز کردیم
🔹
یکی از دلایل دست‌وپازدن ترامپ این است که ۲۰۰۰ کشتی در خلیج‌فارس مانده‌اند و منتظرند آمریکا راهی برای چندصدتای آن‌ها…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/441268" target="_blank">📅 00:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441267">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/831dcd69a4.mp4?token=pA1blcYxkvxkz3IlQFyLuXz6VO0qTHdXDmfo8Wp_nwUpnD1Wa7CgEzw3FF0c_ERh8vIuNufFjt0USxB128Vibf2hqUbJYFeO9_xfhf16TnilKOSbHQFhQe94QTUcEvd0mt7oUmc9nKoQsDxSMucme_mB82xa70NGEmwxxMm7NyL-zA0F7Eif6Up4el54WaNE-obJ1xWz16sKth4R-7UciwnWNPfdLB3aaHzbfWNfCDF_zBpwoyM4UnNGurv6Gf-ln4MHcmMYa5qceCZUKsqBWC8YkFm3mGUE_XIuqg4nsG5NtzJmp-JKHeNJVAbIxETLbXE3LM2lSUPyMlYicoGYMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/831dcd69a4.mp4?token=pA1blcYxkvxkz3IlQFyLuXz6VO0qTHdXDmfo8Wp_nwUpnD1Wa7CgEzw3FF0c_ERh8vIuNufFjt0USxB128Vibf2hqUbJYFeO9_xfhf16TnilKOSbHQFhQe94QTUcEvd0mt7oUmc9nKoQsDxSMucme_mB82xa70NGEmwxxMm7NyL-zA0F7Eif6Up4el54WaNE-obJ1xWz16sKth4R-7UciwnWNPfdLB3aaHzbfWNfCDF_zBpwoyM4UnNGurv6Gf-ln4MHcmMYa5qceCZUKsqBWC8YkFm3mGUE_XIuqg4nsG5NtzJmp-JKHeNJVAbIxETLbXE3LM2lSUPyMlYicoGYMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محمدی، تحلیلگر مسائل راهبردی: آمریکایی‌ها دنبال خروج آبرومندانه از جنگ هستند و مهم‌ترین کاری که ایران کرده این است که راه‌ها را به روی او بسته؛ چون آمریکا اول باید شکست بخورد.  @Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/441267" target="_blank">📅 00:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441266">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd6f08402.mp4?token=Uxv7lN17TCwJBSFy9lQvHC0jcTJ7dyyKsNNyExu5kC0DER6d99fUw7lbYBn-QE862rxrk3Iawmv3dLjvhpGi-iTwbyuCMi29yrwys2Z8mTB87nl4rEeXGmPZudT4xJhN2HGjQ305CiMKlSJefvL08eB51IKJLHr7NY1mQLEbXqNKFzFl7FUrtFhDWBdHgkJQu4Jq5lyetSuf3fl13xEfaUvncFvt34rd3LAGbXC8nKd2Dqd49sbJ2Nea8z_MkXJ0Ce9V73z_wQva8pAdHT5I1qCKUvcM9kvn67DRevPSFFlwyU_Tq7j7JB1iypQGK4bm3J0Pnd0VcspoXfbSTX6uMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd6f08402.mp4?token=Uxv7lN17TCwJBSFy9lQvHC0jcTJ7dyyKsNNyExu5kC0DER6d99fUw7lbYBn-QE862rxrk3Iawmv3dLjvhpGi-iTwbyuCMi29yrwys2Z8mTB87nl4rEeXGmPZudT4xJhN2HGjQ305CiMKlSJefvL08eB51IKJLHr7NY1mQLEbXqNKFzFl7FUrtFhDWBdHgkJQu4Jq5lyetSuf3fl13xEfaUvncFvt34rd3LAGbXC8nKd2Dqd49sbJ2Nea8z_MkXJ0Ce9V73z_wQva8pAdHT5I1qCKUvcM9kvn67DRevPSFFlwyU_Tq7j7JB1iypQGK4bm3J0Pnd0VcspoXfbSTX6uMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محمدی، تحلیلگر مسائل راهبردی: آمریکایی‌ها دنبال خروج آبرومندانه از جنگ هستند و مهم‌ترین کاری که ایران کرده این است که راه‌ها را به روی او بسته؛ چون آمریکا اول باید شکست بخورد.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/441266" target="_blank">📅 00:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441264">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
یک منبع اطلاعاتی: تحرکات آمریکا با دقت کامل در رصد ماست
🔹
یک منبع اطلاعاتی در گفت‌وگو با خبرنگار فارس اعلام کرد: ایران کلیه تحرکات ارتش آمریکا در منطقه را چه در زمین و چه در آسمان، با دقت کامل رصد می‌کند.
🔹
این منبع اطلاعاتی تأکید کرد: همان‌طور که قبلاً نیز هشدار داده شده بود، هرگونه تحرک نظامی علیه ایران از سوی هر کشوری، چه در خاک خود آن کشور و چه در حریم هوایی‌اش، به‌معنای مشروع‌شدن آن کشور به‌عنوان هدفی برای جمهوری اسلامی ایران تلقی خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/441264" target="_blank">📅 23:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441263">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎥
روی پیراهن تیم ملی در جام جهانی چه بنویسیم؟
🔹
مردم پاسخ می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/441263" target="_blank">📅 23:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441262">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/977e93de8f.mp4?token=ToXySO2Tt6JKPWKYmgXxNE-mSLu8vp_hZ7sJIMlpcnnW0X2iIkmvxAEvxJ6zxtLFtih7cssuY7Nq-N3xJW-f7MFJiUhLhMIGptFdlmGTxmiPmgTgy_yQ4JOR0fSs2F8ufUB9GFU22GW_qiSFoPqwLHoMWnUg_dnQzSxYw4TACUgL3aIQgyTH7CMnJuPXFMqy-tlaKXYszZMZ_VgYGJZrixEafFaTZNl6v_t0rzaaEUm_IjD4IGoF5_bDdmBfaf7hoINiqkt6LEsiAz7voGH8iybq3zLWRYeqL6c4EZXaUsrP8QWpeo1RG3N_7qaFxJ1PrWZ4jP9pGtbgmzDhMs61Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/977e93de8f.mp4?token=ToXySO2Tt6JKPWKYmgXxNE-mSLu8vp_hZ7sJIMlpcnnW0X2iIkmvxAEvxJ6zxtLFtih7cssuY7Nq-N3xJW-f7MFJiUhLhMIGptFdlmGTxmiPmgTgy_yQ4JOR0fSs2F8ufUB9GFU22GW_qiSFoPqwLHoMWnUg_dnQzSxYw4TACUgL3aIQgyTH7CMnJuPXFMqy-tlaKXYszZMZ_VgYGJZrixEafFaTZNl6v_t0rzaaEUm_IjD4IGoF5_bDdmBfaf7hoINiqkt6LEsiAz7voGH8iybq3zLWRYeqL6c4EZXaUsrP8QWpeo1RG3N_7qaFxJ1PrWZ4jP9pGtbgmzDhMs61Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم انگلیس در مورد تجمعات شبانهٔ ایرانی‌ها چه می‌گویند
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/441262" target="_blank">📅 23:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441261">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a44HQw2q_vorlMk6m9iHFwhl0aPFOYzai_QSF6iCUwT0DtbmAHVtxd3fPn-eracnXnWu0g4tvAEHSUkc3UMDgFjZrRQTcYlSW39GSusjMJhgM37M2-EmWd3GHksfDHOkBoiPKqfKzPXbEzYgDwAzNZqTW1wVTv0QQf7-Db_8E5VGqEWvK6dHeMx1QYPhxtsTDdSIvO0oPOl18pSUAWoCOLJmZXgkpR5n_oWD4YhOptqRcwYoVzQjhiOzGY9m4QJQjhcsuPsC_5xTgycNM7d9qlejQCjzCb4EbpE7BjbkBRb3pRMjZU3iMiHl-l8Be8Zz_xMnQuqLsrJ0aKHvyomnWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی آتش‌نشانی: آتش‌سوزی در انبار فرش میدان قیام مهار شد
🔹
نیروها مشغول لکه‌گیری هستند و تا این لحظه فوتی گزارش نشده. @Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/441261" target="_blank">📅 23:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441260">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DB7ggdZhz9BlM7jDFv1_Qgqqea4PRKKlCx_MkPXMikHfOJCikoqc_eit8edPBrZc9fIUVmsWIFwLyOhsq1DTz-mGJ9Nym5CYa-P0-Oj7DTYZXz6oh7ZwrBmiAxnwTsRlyAol7zJT02SVlLHdtq4Io5afBiMalAj8_TldOKS9GBmnGQS3p_MowIqdlTNKKLZR_NxNA1g21J6RCThwNGHWrZhGTGzgFPFviAu11jaBLpyKRSy7och_gNXew1HN1p3tLpcuOzn009hU_DtvegWCMR_TVPzERMmWwGuVF4pthx3kX-Ms21Mnu22Xtdyi8FUetLCAD9e1byKPx0CNI0VzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ کارشکنی آمریکا برای حضور هواداران ایرانی در ورزشگاه
🔹
فدراسیون فوتبال: براساس مقررات فیفا، ۸ درصد از ظرفیت بلیت‌های هر مسابقه به فدراسیون‌های حاضر در جام جهانی اختصاص می‌یابد تا هواداران هر کشور بتوانند نسبت به تهیۀ بلیت اقدام کنند.
🔹
فدراسیون فوتبال ایران…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/441260" target="_blank">📅 23:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441259">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e748be8bdd.mp4?token=UjdNb7BS6p--4Bsyzc-6cUawdm17x6nWLMdSb39PKXEfEnf1Cp-AAnYxhK8zoojqDVRc2GmLAVF_exTaM5XAu693XiWSH2nu7TV_gfp4NTi3TlrzkrLHU6gyCOIek74KIQ18inAw_yt7boSzMpDFrXnISiuXIG-rSDxiwZ21BSK2clhmvLMcjeUgiS83J5fuPtGCFB-lhJKmJeZWOlv1Ad4E8ZUDVPTSt8M9IDsh5VDWyT7vxMCot4b9Cz6s7QBSlT1VVSpHanPiLo4NNooVhyZREIf1hMLjrhySOPreO3Z2l-QBJd3ruA-rimCUTPttvqdRruldKMTTUrU2tU9x01sDB47adCoHarkVzsoV3zSjnhmWEEHwt2erq1Y6WzETX-5gCF-QBqrirIqQwZ1IG__Y981O6vW0g5_IreYfzD32BLGPfQ7rKj8BeYPDjNiKtH5HWSAtkXvfClKXyts9QUN6uVZ72lFmX31PXvznsUZnAzZWHYcPdW3M_dlfvDXqwlKpPe2yv3PtD1zuFjzjinuvDoj63lgkojTIYv2RZhhxdn2D9AngxwmJgcRrQhDaey0oQGfzjPrMDD8btDuOFAi8lF_pPCB5_CcZoaqvGk1ljcowz24PX-l9H9iymeLChNku5Sa_AhElhE800Njm4CXw70IXjooTUI1R2hd1kI4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e748be8bdd.mp4?token=UjdNb7BS6p--4Bsyzc-6cUawdm17x6nWLMdSb39PKXEfEnf1Cp-AAnYxhK8zoojqDVRc2GmLAVF_exTaM5XAu693XiWSH2nu7TV_gfp4NTi3TlrzkrLHU6gyCOIek74KIQ18inAw_yt7boSzMpDFrXnISiuXIG-rSDxiwZ21BSK2clhmvLMcjeUgiS83J5fuPtGCFB-lhJKmJeZWOlv1Ad4E8ZUDVPTSt8M9IDsh5VDWyT7vxMCot4b9Cz6s7QBSlT1VVSpHanPiLo4NNooVhyZREIf1hMLjrhySOPreO3Z2l-QBJd3ruA-rimCUTPttvqdRruldKMTTUrU2tU9x01sDB47adCoHarkVzsoV3zSjnhmWEEHwt2erq1Y6WzETX-5gCF-QBqrirIqQwZ1IG__Y981O6vW0g5_IreYfzD32BLGPfQ7rKj8BeYPDjNiKtH5HWSAtkXvfClKXyts9QUN6uVZ72lFmX31PXvznsUZnAzZWHYcPdW3M_dlfvDXqwlKpPe2yv3PtD1zuFjzjinuvDoj63lgkojTIYv2RZhhxdn2D9AngxwmJgcRrQhDaey0oQGfzjPrMDD8btDuOFAi8lF_pPCB5_CcZoaqvGk1ljcowz24PX-l9H9iymeLChNku5Sa_AhElhE800Njm4CXw70IXjooTUI1R2hd1kI4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسهٔ بی‌پایان مردم کاشمر در ۱۰۲ قرار شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/441259" target="_blank">📅 23:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441258">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6803b8b548.mp4?token=cLPcki--mbdftr2oVJuCj8_qFrEUzmz1wIWjtMaG_8LfE9NzdrZObElBruiyH22AHsj3rl0EkbNRvIVtR5O-6wL4ltoo5a7Pig8s8cn_IUVB1iC5OpwDE1f5hFgmmwWs1GiLJfFRcjMzEsI25DzJNiHuMFdW3EN5knzMqX0oizAlfUhjh_wMKvQAKCmIWY4BHG0KpMRKMO-Ch7A0nCDB3u6LaPUGIA8SR58IfWnYYpnQGeL7kEYzWDLDEkqRuMtt6QJpMrvNRW8v_H7GoXjJr0dWviilXgBeXlcanoD-XhySYN5ac8Xs1RAf1so-snady3CogeksjoB2xJQQalmM1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6803b8b548.mp4?token=cLPcki--mbdftr2oVJuCj8_qFrEUzmz1wIWjtMaG_8LfE9NzdrZObElBruiyH22AHsj3rl0EkbNRvIVtR5O-6wL4ltoo5a7Pig8s8cn_IUVB1iC5OpwDE1f5hFgmmwWs1GiLJfFRcjMzEsI25DzJNiHuMFdW3EN5knzMqX0oizAlfUhjh_wMKvQAKCmIWY4BHG0KpMRKMO-Ch7A0nCDB3u6LaPUGIA8SR58IfWnYYpnQGeL7kEYzWDLDEkqRuMtt6QJpMrvNRW8v_H7GoXjJr0dWviilXgBeXlcanoD-XhySYN5ac8Xs1RAf1so-snady3CogeksjoB2xJQQalmM1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سینه‌زنی خرم‌‌آبادی‌ها در موج ۱۰۲
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/441258" target="_blank">📅 23:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441257">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHR8ndACOL2IyCd9hggb3EnyRsAkrHfcRYr9iW3QVfKV3UDUzGI7gTbtH6HXezZ4_xGc_yCuywfNwlWUS4wVcrQxDK_tNLjhIkpVC9QL_KLKVX4zcX6TBexg0s19T-fDOM7Caem0WygCInFO5JxAsz1ZNltUWhQJS7yZNt8CV1k6FRnFvsHyFvprSrLkstebenJSRBvBjZz09wwuVHFRKdj-0_G7k8UlhglfAU6f_VO_f8ioP9Rp9gJtYdzuJqWNG4qUmTBglpYwfHPTvf5BaHerxsswE0HRWU7DaoH1NRLDED_GBHmLKPFBjuK1GWXZT1EdpcNlfHsaKpMgqnqeDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای همزمان گروه‌های سرود
«
جان‌فدای ایران
»
در ۱۲۰ نقطه از کشور
🔸
به‌صورت همزمان روز جمعه ساعت ۱۷
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/441257" target="_blank">📅 23:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441256">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841fdb1a3a.mp4?token=ok3gLRxpsAHQSEqqVzDsIsPt2jDIcxmiDylhQJKSJlfbrI_vdfO46v6hnMF6EIrTGw71Yse0la0iWjO_kjTsny9s8NrKZOEZRsMU5odha5CRX2cH5wJZgwKSIv8BKEyXwfR_D8x1ZBGTO6MEfzVj28xAzFnwylsFAV2Zhg35QrBRN52rka9jhZDvAlZwkjonfwBampKuMVce6leBfp5iycmkbkOfon7Qn15Bq7EjIB3dwOnRqfrBpSo9SwqgtYGwhJm5_HwGxxmzEpHNJIfBz0J5ef3TScYh_Cao_zbXq35b_wVkUtjjYmHW-9sjK5NKAgFUFUG55WHJp2vgKfxenbFjXtTdw0aEZ9NJ59VZLFF-hKE0NwgnatgOUeJT4KNsC_4OJbEp01ucF9TAKiVMheDLcV01Y33wh1WN2PU3JsxEkeIwUrlaYybwYaS0IeGUFLkTbMvTDdtPhUYkiw-Ocsa7WOusKohEWq_H9KBxBfQyvD_GtQrUJfK1Yo-V3k78xhlP3Fb0yp-Dp1QQd0N0Z4sc6GwyxN9BKJfhZTBHDVFKFfzJCxcjAYSJ-Tpr6IC6AawI6RSkEKdP8yrhJEOIDuugJp_Uy471OUMMea5Mis1liIycRAvOm8DhIsFs-j0W4GGL6b8oUvMstW2R1imDMkEwfhvuKGgSDXvImMO6PTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841fdb1a3a.mp4?token=ok3gLRxpsAHQSEqqVzDsIsPt2jDIcxmiDylhQJKSJlfbrI_vdfO46v6hnMF6EIrTGw71Yse0la0iWjO_kjTsny9s8NrKZOEZRsMU5odha5CRX2cH5wJZgwKSIv8BKEyXwfR_D8x1ZBGTO6MEfzVj28xAzFnwylsFAV2Zhg35QrBRN52rka9jhZDvAlZwkjonfwBampKuMVce6leBfp5iycmkbkOfon7Qn15Bq7EjIB3dwOnRqfrBpSo9SwqgtYGwhJm5_HwGxxmzEpHNJIfBz0J5ef3TScYh_Cao_zbXq35b_wVkUtjjYmHW-9sjK5NKAgFUFUG55WHJp2vgKfxenbFjXtTdw0aEZ9NJ59VZLFF-hKE0NwgnatgOUeJT4KNsC_4OJbEp01ucF9TAKiVMheDLcV01Y33wh1WN2PU3JsxEkeIwUrlaYybwYaS0IeGUFLkTbMvTDdtPhUYkiw-Ocsa7WOusKohEWq_H9KBxBfQyvD_GtQrUJfK1Yo-V3k78xhlP3Fb0yp-Dp1QQd0N0Z4sc6GwyxN9BKJfhZTBHDVFKFfzJCxcjAYSJ-Tpr6IC6AawI6RSkEKdP8yrhJEOIDuugJp_Uy471OUMMea5Mis1liIycRAvOm8DhIsFs-j0W4GGL6b8oUvMstW2R1imDMkEwfhvuKGgSDXvImMO6PTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر پیش‌رو، روایتگر آخرین روزهای زمینی مردی است که نامش لرزه بر اندام دشمنان می‌اندازد
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/441256" target="_blank">📅 23:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441255">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hThZ__sGe-LWdBVHNy49SRcs50f-vwKWYfK2QTEA8NFVNU7XyyFJBPY7x5MuW3YK1WWhgfOGQtxjiPTyx7Xk5AZ-FciBgC6tLVL76E-8JBi7R5stEwwXC_JkiuQUCf1qn53ncPCBNtRmEr1Kr7jdREFw-yZ_5kcy8qsjGWIHaBmVnScldiwCxhRHwx5MxdqSSfsfPoKCN9_HQOYSJ8Q4icNvcUJBT3Uqi_CPyEZbk0dbnxYRAH8BAW5ZfE0S76fBtFiqHFKb8y7MYcVlRHVUIrCk57dpxdZmqQSu-X40exufRtRMH5Epgr2sWbi5WYp0bQT2N-LM0hF0QnDxhs_0hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس کمیسیون امنیت ملی مجلس: این‌بار جنگ محدود به منطقه نخواهد بود
🔹
خواهیم دید چه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/441255" target="_blank">📅 23:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441254">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b30113c6e.mp4?token=HgtqPBLW6PKT8K5RruLkcpf9ca_p3JBurPeBHzjNAsn2ahwA80X96kRHsIciRS2tPRGhatWc5hUKnTWsPT3UwYndYcCsEmw7wvbk0J-EJgC3M-3uBNXOM-HclmVAAjk61fYIaD9OTBZmbnsi56znwHldv1m45ABx3z61wfURBF1HXpSJXRzwO5CQCoKi3ZCzInfujmrRQhwppdQkvT8uEgu4t1qpTFFhMiTwAdXkMj_Gje3eVMQDhkH7kEp62zsz5Pbyvej0qfN6qEdSbO4DCz3NPlqvv3MP14AEGpeKbDokuRkkCrRaslVRzqbynJb_QuMCV40njWr8S7ep_OL1tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b30113c6e.mp4?token=HgtqPBLW6PKT8K5RruLkcpf9ca_p3JBurPeBHzjNAsn2ahwA80X96kRHsIciRS2tPRGhatWc5hUKnTWsPT3UwYndYcCsEmw7wvbk0J-EJgC3M-3uBNXOM-HclmVAAjk61fYIaD9OTBZmbnsi56znwHldv1m45ABx3z61wfURBF1HXpSJXRzwO5CQCoKi3ZCzInfujmrRQhwppdQkvT8uEgu4t1qpTFFhMiTwAdXkMj_Gje3eVMQDhkH7kEp62zsz5Pbyvej0qfN6qEdSbO4DCz3NPlqvv3MP14AEGpeKbDokuRkkCrRaslVRzqbynJb_QuMCV40njWr8S7ep_OL1tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش حماسی خرم‌‌آبادی‌ها در موج ۱۰۲
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/441254" target="_blank">📅 23:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441247">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inWNkl_YoSQtNWq0hwekJfTi5icGWojuj2pPparsgPEjwu1Xw5Puoso1FcAlua6eAMA_Xs0l35SL2wQvH2exTmnS82AOg3M51r3PCS56ZIi_AFhmvihqUBohZmKVnpyHfmHmzWD3UZCPKJmnlkJLO2nY-ZvGKQVe4qGOSk9V6Y8G0Thi9zrrefYBkzRoc8g0KBZVALekHVTgkUH_GZWIaR0tzV-qH1bHZ-PDUkWUNgeYvqx_viptlLBDW_Fe9luj0cpZINd4_Uca7_xK9TE2iKQWxjh5TrrBpSzF4Em3tmHU2Z-6CgVub_ShqDj-FF0TcaZRqF0J0soChkvPc-V-sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P3lxGZPvebZ1YVGBQzdVxTpoPSxn2U3imIOPr66-WWaBBgM_g_aE_f6uR6txc5_-BjC9Iu1tFytluJI2ppUVi4gCqzh1pn5_TvfFgZGjPmbIa40EJYZAwXKfL4QVJ06-4e4IgzOOYn8nBMI2yfgtOQs7AcXKCM0SA2RsskpkKong8gTun9uxyNUnJgffGr76swYCDm_bQvpzMq3PJ6zwQyXo0GiVxMOeist7hIEdyoUjkNi16ihFJdkpPMx52HsmgDZciYjnq71aFAUArL7auwqexLZi8qtN64Xff6v4zfcH1B0wHzkjp120Lpzr71MIlxncitC1i4Nvh6DnAsOddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qM_zYscHY17DGxI86PTOKx59XNhOfgfnQV1y-Aah8fOwZhBvgltLjJKxN-KFZahUby2Ustu7Ih_W6Kbb3CQqyNj_8SH1NyQveJRIe1PzUFvMrxR6UABGMk3epBYjpPAh4T1h-lR490K3Q8o5wTjJWmgoztAAYVh1qWI7EOyQ9pwAbq_tVp1eArj2rG2ti0VFWbPs8aS369FEG0knODyKKgJV_shEe-9ha2XdiJ5WOrXKBRtEKC1qA1sx_EYvwUXt70FGMOOkKKO4jpHJU7H8nV30H4pxgL3BWg4WeTPJf3PiZPuhKUJ9ChRTO1Gkb31oxbkub3oozcSs0kfZLQ76EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCqlPuiYUcyWV2-iCiO7iEUhsYi7l10NirYu1GmoJUrlKbucKkYCSRhzSq0IiSpYG7EO6ZDJBUaAEKE41hBv2IJo_eHRKIp7DG1MQls_L7XylqvNesqULLeUZMLGoaMvOIQp-yAXaMogkQQFkzO8_ZoF8pK8E4cAR8a_buWE5iRKZ0RmhsbX88E8jvm6SDwV8CzRrbohOy4gQpmQ2Do7iH8koDCF2csW_1EqWMpYi91IzPwvQrbMIp5EI-77lqtHImYQmBGWVF-5G0AaULMZ6gOoEKvELsNuK9dP-_ydmNmOLf8lt6KBMMzPCUM-81poRSvyj97EWaKeP8vN8qejgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e6t1vcsP_Xq_----OxVX7Et7RIlQcqBqXl6a72WBXxuGy1HpBgrxqf8Q7AaAJbkD54Bmbkak2CSZuEzTPHSVNmXaK3EPd4sHkCzYOTbeOBv1Qpl-v7GGBKeSRSzCMvwVxZ9S8iOEkP-zjiuFv8eDn2F-slUt7olDXD49nTBgVxvrMWEMrbRDd93mjBu1Jrc6xaEZg7V1VESY1H4f-fy4GwIhvM_NW35W9djqSwVHyKHL7lfItaGWCSw4psqz1dNnKBiOfYkWwR6ZA_9SrWccg7G0HfXpaKZncmnV19xI4Yx0vEgnBp2gU7ObyxmtQG0i_cnlHDQ0pnXB76nHmDgYAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9rOcxHsxE_GzPew6BsKaXI_Z1C1l5gpwYUaWQcXVqbabfpBxltMYKnsCMcFYaNQpd8T07Gg4GIbQ07r7yWVLpqC8nwRy9fRUoK-lDXFQIH5Yy9X1QCiKWmM69QmFihHl3QWFlP2OZ1RU6eY_pQokOf2EQgjy5rHjUMkxwr4JTPsAr7pPCjyTOMCx96wEUu7j8kSgZmQQk5vYjxfisIaZKZl4Q4Grl7vfFzjOeSJsmBxET8qXk_5cIRTat144i87b9fXQMcaMs0TvHqHyPvB9Z5lbRj2rqz2dV-UFy_vJg-xWoEonOUmxjbte3GlODjb20gSwYrZ_zJK7al9hpSRMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQSNejUthocO5wD1sAAeJcT4SXdKlMOkmtXg9M5EhLXr-m6QDh2QM6xk20FvPF_mLM8Kleojgxr7ND1M741jFh2KIQRK_V6aJtxPKyxl-5ISDCFtRAH730EN3pbX7Yik7qq0XukJJcRwpWvD9A2pDnVnwE8XqQVM9SGQz5XBULyqwt4-lWAmTJGaODfnwOrHZR_4xNRCCNhCDWVQbXVLXm8vBWEOqsZrAWxCcf-FLvnba4IMfGPW8_u8SKWo5bKZ9JLv6KZNM2cqtHkKizJar0tbfdn6qx_5k_Zk0AsZLn6HJgzKKUXHytoYQ3FYwSZWzmygC4MwWmUt2uctenmKcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گشت‌وگذاری در موزهٔ زمان تهران
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/441247" target="_blank">📅 22:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441246">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6ce26d886.mp4?token=ngBxbdb2cOwUqrWfH1eccpiKPTY_GB0ui-bpX7mPR1Z5UGEgNc-2Jaoz9biv3Rj0dyiUwfvLa4uSVsJMy2lKkOlr9X2yE8JgqhAOWdzl_XHig9-eotqHmcryy4tk2esLfAtWiabUi7Y7Wvi2dnDZI6w35Zf7a8wi_FOOZyFPeBgO8mcbvXcYixmIsGCIqeH9Wd2l38axnir0e2kPmkmd7jf_eBfLpertAA81odUX4xXpeg536XiYYUnfjWsdGn-51CZEsM3vvMbPlczZjCFNaD0lvW9XgNNoNhpEI1_dmtjdFNVKnjMPDc00ISi8ix-UXFkuuIq6HpN7sizT-k72uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6ce26d886.mp4?token=ngBxbdb2cOwUqrWfH1eccpiKPTY_GB0ui-bpX7mPR1Z5UGEgNc-2Jaoz9biv3Rj0dyiUwfvLa4uSVsJMy2lKkOlr9X2yE8JgqhAOWdzl_XHig9-eotqHmcryy4tk2esLfAtWiabUi7Y7Wvi2dnDZI6w35Zf7a8wi_FOOZyFPeBgO8mcbvXcYixmIsGCIqeH9Wd2l38axnir0e2kPmkmd7jf_eBfLpertAA81odUX4xXpeg536XiYYUnfjWsdGn-51CZEsM3vvMbPlczZjCFNaD0lvW9XgNNoNhpEI1_dmtjdFNVKnjMPDc00ISi8ix-UXFkuuIq6HpN7sizT-k72uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دروغ‌بافی ضدانقلاب این‌بار با تصاویر جنایت اسرائیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/441246" target="_blank">📅 22:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441245">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94dcf0afa0.mp4?token=PgNKitqCSzWooYac_wp6_mX4fqesSIbP46VPE46ZMC_0vWX6yLii8w8fXZ3d98osIF1k4gXJBPEepms1GEcKwSzkY_pM93pWaW4m6NUWxeRDTCC5lCNQwO1b6-2NynzKQ18cPfPnuL_RkxfGpJMXny6PRUPS8JI7x0LW3Aj4BgVqCPtQvC-K3R27tEVkySIjSfpPlJZzU87QKQj6QvFeKqDH-xC0BEIbSKVHaB4aVdercXin38e1rV4MYIa5_WZM72_HUa20D4tEhJ3jittv5lednHKouvog1v9jaoWf79AwbHidcNj88CJZPTEgn97t5TlS0ZtU2nAVLSZxTbI_d4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94dcf0afa0.mp4?token=PgNKitqCSzWooYac_wp6_mX4fqesSIbP46VPE46ZMC_0vWX6yLii8w8fXZ3d98osIF1k4gXJBPEepms1GEcKwSzkY_pM93pWaW4m6NUWxeRDTCC5lCNQwO1b6-2NynzKQ18cPfPnuL_RkxfGpJMXny6PRUPS8JI7x0LW3Aj4BgVqCPtQvC-K3R27tEVkySIjSfpPlJZzU87QKQj6QvFeKqDH-xC0BEIbSKVHaB4aVdercXin38e1rV4MYIa5_WZM72_HUa20D4tEhJ3jittv5lednHKouvog1v9jaoWf79AwbHidcNj88CJZPTEgn97t5TlS0ZtU2nAVLSZxTbI_d4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم بجنورد در اجتماع شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/441245" target="_blank">📅 22:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441244">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ae39f9353.mp4?token=J8NLdPb3r46v5ebEbrLtwJp3QJedBFDQqoLLs-BOOXsq9QXL207fbYRHxgi-TuTyzJqqQQIWWlDiMnourUYkhudTgfCsG2BPLcOdxnhherYkUo06IRThGuzlHkNveG1LFlo7Paldbbc9eK9rUW1SO9SZA6n39v56GDmFywXrRZ-Ax19qd5aBDoAK_bU1EXX-K_7pXlS_0wXcExGpaLDHsjs-tgx7HIqMiwmrdDkJLctW0x3AAcSsf0E3C5VIe8Tpq12aNqdk7dOf8hRiMvcHzCE-UR7-KMQsnC0eH63eBc2nJg8YA0WekbnVHDAnRxqoN6vj-lUnrBR6ONvSgdRibQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ae39f9353.mp4?token=J8NLdPb3r46v5ebEbrLtwJp3QJedBFDQqoLLs-BOOXsq9QXL207fbYRHxgi-TuTyzJqqQQIWWlDiMnourUYkhudTgfCsG2BPLcOdxnhherYkUo06IRThGuzlHkNveG1LFlo7Paldbbc9eK9rUW1SO9SZA6n39v56GDmFywXrRZ-Ax19qd5aBDoAK_bU1EXX-K_7pXlS_0wXcExGpaLDHsjs-tgx7HIqMiwmrdDkJLctW0x3AAcSsf0E3C5VIe8Tpq12aNqdk7dOf8hRiMvcHzCE-UR7-KMQsnC0eH63eBc2nJg8YA0WekbnVHDAnRxqoN6vj-lUnrBR6ONvSgdRibQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سخنگوی آتش‌نشانی تهران: ستون دود سیاه رنگ در جنوب تهران مربوط به آتش‌سوزی انباری در میدان قیام است.  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/441244" target="_blank">📅 22:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441243">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809d557261.mp4?token=UKerPT9Dw5oSNQmNfqPO5TPj0jNEPjndM94nqmeAx20isLuWN3Tw0Tj0PNSmAuvTfEgIVj6UZRogpKZFWlyVEw3-_Yw4_qnrGzdm0A4wHUsSWVxegaTh1T3p4zn3CYsxZTq7KpZnXLUpcSvqIbELc5_l92Xe6KWpd3wkbbkwjN24wGPBIgltCWYGWAVaO3xJhZ0GK9GXggqoOitKk0kcadJzH92A-QS4YRd1rjb1Hq_cLhiGfCGARuRL0ttWMt4IrnXZ_eaX_FlXr4QokIC3BKfDmsy18QssPUFrV52toAasOXy-_ehdZJuvVcebHLuI3D2E_4StCZr5gL2enjnxrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809d557261.mp4?token=UKerPT9Dw5oSNQmNfqPO5TPj0jNEPjndM94nqmeAx20isLuWN3Tw0Tj0PNSmAuvTfEgIVj6UZRogpKZFWlyVEw3-_Yw4_qnrGzdm0A4wHUsSWVxegaTh1T3p4zn3CYsxZTq7KpZnXLUpcSvqIbELc5_l92Xe6KWpd3wkbbkwjN24wGPBIgltCWYGWAVaO3xJhZ0GK9GXggqoOitKk0kcadJzH92A-QS4YRd1rjb1Hq_cLhiGfCGARuRL0ttWMt4IrnXZ_eaX_FlXr4QokIC3BKfDmsy18QssPUFrV52toAasOXy-_ehdZJuvVcebHLuI3D2E_4StCZr5gL2enjnxrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور حماسی مردم شهرکرد در شب ۱۰۲ تجمعات خیابانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/441243" target="_blank">📅 22:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441242">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaS7FpKAbT7Qni3TQu6ixCHgFogbak95qsOuGvhhVyfKV_1qx5bR-IELr3bdAR30M2Lw1ykb2X0mGfY2_-380zGK5eMiYJuAvwmBDQsF3QGb0WYS0Cc5tvem31ipk3oZV0NUE5Tr_oae0O4TNqVUaTeLRItQjCeTvdBa3QXztN6QQoeA5_Ve2jtAfnxwEMcRR0_H8BM7cbG64BJalCWVrttQeQbDcOwAzTpAH3KKDap25lhLzsvKWGmmAsEHlw1AGz1sbkJLBheTB-SHJjBEkTmuBl2pzOa4kw2ItAXG9UdJYT2SGSoEx5UuQAcuiU85xOcJRqr6vUDoapaggLGHKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوسمار به پرسپولیس برمی‌گردد
🔹
برخلاف برخی شایعات مبنی‌بر احتمال پایان همکاری اوسمار ویرا و سرخ‌پوشان، باشگاه پرسپولیس برای بازگشت او به ایران اقدامات لازم را انجام داده است.
🔹
احتمالا او حداکثر تا روز یکشنبه وارد تهران شود تا در روند آماده‌سازی سرخپوشان حضور داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/441242" target="_blank">📅 22:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441241">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
منابع خبری از حملهٔ هوایی رژیم صهیونیستی به منطقهٔ بقاع غربی در شرق لبنان گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/441241" target="_blank">📅 22:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441240">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a70dd69dc.mp4?token=O6jZkXsz0YcspyLsrPC3lhqhWUIolZn5tW84YvkCKwZdZZseFJR-pppFK_dasrWvfd1jI6flD7lB1PCGhMnLB5-iopDE5-dTbf7V6m08eEQxkA4FbYtd_eFxyABqcO5F75sgYZqjRjvHR2B5M2cjQPwk3ChituJ8rp-oOXwUtNosSB9xNFlyAL47LnrBCuRgVbbjXdfVaIIXf9YVSLhAbdueM1NeN9-epgXTJ7Vfjad8iNhd0Y_f__kycpKqbWGWS5Ijgt3xfLv6bQubOhyo4vL6PWQsujqVRiXIbxZyd9s5EWyVOm6ycmiSF4X7X2XxyyRYKekIUiydouA-svl6QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a70dd69dc.mp4?token=O6jZkXsz0YcspyLsrPC3lhqhWUIolZn5tW84YvkCKwZdZZseFJR-pppFK_dasrWvfd1jI6flD7lB1PCGhMnLB5-iopDE5-dTbf7V6m08eEQxkA4FbYtd_eFxyABqcO5F75sgYZqjRjvHR2B5M2cjQPwk3ChituJ8rp-oOXwUtNosSB9xNFlyAL47LnrBCuRgVbbjXdfVaIIXf9YVSLhAbdueM1NeN9-epgXTJ7Vfjad8iNhd0Y_f__kycpKqbWGWS5Ijgt3xfLv6bQubOhyo4vL6PWQsujqVRiXIbxZyd9s5EWyVOm6ycmiSF4X7X2XxyyRYKekIUiydouA-svl6QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم اولین سالگرد عروج خونین سردار شهید سپهبد
حسین سلامی
🔹
فردا پنجشنبه ۲۱ خردادماه
🔹
از ساعت ۹:۳۰ تا ۱۱:۳۰ صبح
🔸
حرم حضرت عبدالعظیم حسنی(ع)
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/441240" target="_blank">📅 22:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441239">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a02fb960e2.mp4?token=qmTatjcC3Dqi8HJohVa5hfGTf-i-cmQXhiNm0464XcBlfyxp3f-m3L2kjB-6eUfEQcpmDd4cTScPxPOVrkXFs5Z13cuXY1NdvXqjwG7hRQla7iWsQ1NTnmPgFFZnj_JsPVmosQ5dE1PHpETWJA8yQ72Phg_IAD8hkvnumriWY747UlkF9RuB3Ei6iSfX0KjPWnDcobf9j9RDihyOhJZk0b29Bc8rWeDTRrA1i9LTu8lvACAOLmAh_4Nt1jbP_CCyJCcebxJuuqo8FSgjCEH1MJJuCriT9HRT9n43AlhMCeVZa6nBJ13LY-n51yBsjchdWvSaIYoDrm5-2xQf2Ig7Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a02fb960e2.mp4?token=qmTatjcC3Dqi8HJohVa5hfGTf-i-cmQXhiNm0464XcBlfyxp3f-m3L2kjB-6eUfEQcpmDd4cTScPxPOVrkXFs5Z13cuXY1NdvXqjwG7hRQla7iWsQ1NTnmPgFFZnj_JsPVmosQ5dE1PHpETWJA8yQ72Phg_IAD8hkvnumriWY747UlkF9RuB3Ei6iSfX0KjPWnDcobf9j9RDihyOhJZk0b29Bc8rWeDTRrA1i9LTu8lvACAOLmAh_4Nt1jbP_CCyJCcebxJuuqo8FSgjCEH1MJJuCriT9HRT9n43AlhMCeVZa6nBJ13LY-n51yBsjchdWvSaIYoDrm5-2xQf2Ig7Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۰۲ شب ایستادگی مردم گرگان در میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/441239" target="_blank">📅 22:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441238">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_piwebNWnlowRgWu6W-YZMoTA5sdHBxuZVxDEFVeFdPYBKNY8afCoTdhOM6t9jNpDmE00p__jfFJlELJH1dcPtguUoevBJjD4tIZ6o6WeR9bHP9SkLFlwu8MhZooN7lRjo05IMCBu0Azr9n6o0VHJR2Tb3JmtFzOkJpL8Q8tqiUDczzbFbXX0ULFuZVo8Xeg_W4POQqSW6lBVfD_IHkAFx7BGOQ1SK33FMBjcfWwZ1SRpguN-QcMWkPjeZqVD4-3yf8e1OoNDiahSVH8-rbt8y3VrDmkKVkUfBuXlMUnRvcVa1nycIoYsgb_ETRdbNBrMOPYLgWtFM4HkgnRrUVkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهراب گزینهٔ اول استقلال
🗣
براساس پیگیری خبرنگار فارس، درحال حاضر سهراب بختیاری‌زاده گزینه اصلی سرمربیگری استقلال در لیگ ۲۶ است.
🗣
قرار است شنبه هفته آینده کمیته فنی جلسه‌ای را با حضور تاجرنیا برگزار کند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/441238" target="_blank">📅 22:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441237">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INKOqIokcIU5i7mdMcfEzPw316yhPWZaGlKlGUGq84XHJffNbUfkHfsHF0aRXELSLr6-YJw97nwZ9oF_zP6aBEzaJP0dTLZS4efan1JGImleBegLP2WxCPwrU5h9mSGE3I3z3h2WkP-y6D-_ubLoApxd_7TbrjTTn6eyQjrBGIdm_9YU-4Si0cGJAONQlpugCAqsuhoIReGSDyVkLuUZZ1y0nSSGNC_KjZCixh5bk9U1X-7KlcGSIKB9HLBpo_qK1H6AL5aLyUo08bRIY4_f1C7EtTaePmlvypB09u1DtgSJKaDvESSuvjbpcDNCx2i87bEEj-GgNnmzjB4JeYWMRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
خسارت دشمن آمریکایی به تاسیسات آب‌رسانی سیریک
🔹
مدیرعامل شرکت آب‌وفاضلاب هرمزگان: زيرساخت‌هاى توزيع آب‌شرب شامل ۲ مخزن بتنى به حجم ۵۰۰ و ۲۰۰۰ متر مكعب با تأسيسات مكانيكى مربوطه مربوط به شهر كوهستك و ۱۰ روستاى بخش بمانى با جمعيت ۲۰ هزار نفری در پی حملات دشمن…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/441237" target="_blank">📅 22:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441236">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/669589d65d.mp4?token=AxivdZ9Hu9CgrOGqV2T5Iyhs6T-63cnn797Bpvq4l9cr1Uh6hlJfhTG-SybcXeGeBAFcTpEiza7bFG2xxP82KtT919706-qHFXdH7X6OGkM4pGdo5Wc1_XcyMODCcu4AbSP5hjO66sLcjQ4ykwlDv6HJKSobTewcvEb6qB9nCnPsbMuB03pOG4QXuYAq8TZv8w2ewsfGOGhqzxdyJgKVOig_fDCOoVVPLTFQLh67SkQTv603TFn5CStmpyT7DY0HkNjLMPAZLBel3D4SYXuC6NVSsgI2Tp9uM3nCObCvKxpz5_ngugM1wF2K8ET4u3Wx2IZC5aSB0VqYa58Ikn4_q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/669589d65d.mp4?token=AxivdZ9Hu9CgrOGqV2T5Iyhs6T-63cnn797Bpvq4l9cr1Uh6hlJfhTG-SybcXeGeBAFcTpEiza7bFG2xxP82KtT919706-qHFXdH7X6OGkM4pGdo5Wc1_XcyMODCcu4AbSP5hjO66sLcjQ4ykwlDv6HJKSobTewcvEb6qB9nCnPsbMuB03pOG4QXuYAq8TZv8w2ewsfGOGhqzxdyJgKVOig_fDCOoVVPLTFQLh67SkQTv603TFn5CStmpyT7DY0HkNjLMPAZLBel3D4SYXuC6NVSsgI2Tp9uM3nCObCvKxpz5_ngugM1wF2K8ET4u3Wx2IZC5aSB0VqYa58Ikn4_q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدف قرار دادن یک تانک مرکاوا توسط حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/441236" target="_blank">📅 21:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441235">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_j_wILaVmt42yrCMEIUppkJJXGOBTTzG-LsLxDwohdRSvGklc9MeMz_t8tEk5xSyrsF3dmZvvDJFGhM_WU1MEQGAJTYKuCksXVRTiFIrgx6FxMHtDmfwj0uNdqNvl1YINu8pVNVcSSp-72sezWg4q59dufeLYplNAMFWniuSSCSVH74Pi1Lcicbwct7VrVHGCC7Bo76gG_nF_dAcAwI2PQfVhrXjI5xl8wdIDysG43rwL4exCuw-A9w16srcpjpUEl5QOc9WsIi2obmpGYUZDaNQfCkwhXko8RS1LuiN4rmM6ErqtHLZe2hE4svxfS4VVg5mUmb7NBCHHLRn9pnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش تورم آمریکا هم‌زمان با کاهش ذخایر نفت
🔹
جدیدترین آمار وزارت کار آمریکا نشان می‌دهد که تورم این کشور به ۴.۲ درصد رسیده است.
🔹
ترامپ ۴ هفته است که بیشترین برداشت‌های تاریخی از ذخایر راهبردی نفت آمریکا را انجام می‌دهد و تا ۵ روز پیش این ذخایر به سطحی رسیده که نزدیک به کمترین رقم ۴۰ سال پیش است.
🔹
دیروز هم آمارها نشان داد، آژانس بین‌المللی انرژی، تاکنون برای آرام کردن جهش قیمت نفت ۴۰۰ میلیون بشکه به بازار سرازیر کرده است اما اقتصاددان دانشگاه میشیگان می‌گوید، این ذخایر تا ۹ جولای (۱۸ تیر) تمام می‌شود.
🔹
حالا آکسیوس رسانهٔ نزدیک به دولت ترامپ می‌گوید که دلیل اصلی جهش تورم آمریکا، افزایش قیمت انرژی به خاطر جنگ علیه ایران است که در حال سرایت به اقتصاد این کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/441235" target="_blank">📅 21:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441234">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎥
جشن ازدواج ۳ زوج جوان بروجردی در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/441234" target="_blank">📅 21:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441232">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQdA5Ry-NqratKSHeqAfIXxUpWIrUtPtNmzj6ASGxTehALzXdQTkgRfHTBrDxUyjGQHGDbPf96qkaV5K6PO4-xYWwPUfjacAPPYZ75lcawcocAF6EpsYYBuCN-O0OVvi7wVAaXKoZRKTqYDpnDnSHd55PiroPAP2cmbv7uPMpj_2oWhomMqoYxMol7D9wmLFRnmYdMitXnMALuUEP2LkoEFrlrytkHQkQ_g2W03p-OomJI8XcGwJVviqkEg0xHKX8hZmgUdTRZj8zyB_vhIZ2SUu9lUP1SCSufwR_LoxcJrXNPEOc-i0Qcs4GKkU9SVqwQgCtNZe8WY7U3BbwYJ-kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در عالم رؤیا: تنگه هرمز را آمریکا کنترل می‌کند نه ایران!
🔹
​رئیس‌جمهور آمریکا مدعی شد که ماه گذشته دستور اجرای یک «عملیات مخفیانه» را برای حمایت از عبور نفتکش‌ها و کشتی‌های تجاری از تنگه هرمز صادر کرده است.
🔹
​او ادعا کرد: درپی این عملیات، بیش از ۲۰۰ کشتی تجاری به سلامت عبور کرده‌اند و بیش از ۱۰۰ میلیون بشکه نفت روانهٔ بازار شده است.
🔹
​ترامپ در پایان پیام خود با ادعایی مضحک نوشت: «این تلاشِ به‌شدت موفقیت‌آمیز به‌خاطر آن است که آمریکا تنگه هرمز را کنترل می‌کند، نه ایران!»
​
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/441232" target="_blank">📅 21:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441231">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4760ea160.mp4?token=MUynR45MfqO0bh35G2fJCELMDe6I-GN6_yCiLQxqXSxNe904MXbAkGBTeRGjJtezo6uVVxonkQ8tWXOqLD9RDE1OIzxxj1gerbKLlYw7NhPLQewWZKeVzZwdi28402EKiX5nD3tIehrpKniIIHUi8zyeaX0ZSd4q0VyHhmV95cBeMHzxjki9rna-DRqWyU4dedgFLWQBcJUCMNqA4UeXB3Vql8QnKFeFVkqVanO_Hqxgr0RvGsn4nAGDCqZMLf54WcW8Liv0Cc14rMVjr2oRQ27jQpgJCUMlfQ_tqavXrskEUO1hkciLLQQk5iQeDMNb_NJ_bTC-TO58yr_MJ_0nuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4760ea160.mp4?token=MUynR45MfqO0bh35G2fJCELMDe6I-GN6_yCiLQxqXSxNe904MXbAkGBTeRGjJtezo6uVVxonkQ8tWXOqLD9RDE1OIzxxj1gerbKLlYw7NhPLQewWZKeVzZwdi28402EKiX5nD3tIehrpKniIIHUi8zyeaX0ZSd4q0VyHhmV95cBeMHzxjki9rna-DRqWyU4dedgFLWQBcJUCMNqA4UeXB3Vql8QnKFeFVkqVanO_Hqxgr0RvGsn4nAGDCqZMLf54WcW8Liv0Cc14rMVjr2oRQ27jQpgJCUMlfQ_tqavXrskEUO1hkciLLQQk5iQeDMNb_NJ_bTC-TO58yr_MJ_0nuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی فراجا: افرادی که اعتبار گواهینامه‌شان تمام شده باید به دفاتر پلیس +۱۰ مراجعه کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441231" target="_blank">📅 21:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441224">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lw5HO6neuhC9ma6UY-GBBJxl5kNqUy8yNjmU1u01Rz5vTfaUQ1xrug9NPBbAZUpOtRQTyY4Wkh4KqE_J7Z5Z0sGg7VFA9N4MUFJXkOD20aAh7L9af_jls4qE5eKKg2Jnpt5NmTZ5P1UKTayWcTjlUpTSNSgHob_EX0xlrt5hRLq7PJPCPK7Z68o8kH3-saQXSpYRfKz5B9g7Dr2pyuoRhZUdGD0SUPgq4k9QAjmyiBbF4LWb2TdcGpP9V6OeNt7b5hL3n8UGSTqZjx371PIwphxBfbbp2yE_7H-Q5jMewAraFsEWJTAeNlEQFLIkLn4bFlDzhIzs9bNLuARSs2b_kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFgXVeDfvT_uGGLsvap6Z0jPJiWjRBejIjzCpU7IdzkK9fSTqLwVzSpESP92-5zveT18xW7AZBr1DD5MFtBIFLDsF0BxauVsCuEASm7RviYW28-_3MafJopeteQArXyAV-EAJSh1R9LMQ2kl8wvIBVrSz1-m2KAORNW57iS73EVLh8yh1dz-Cwp8znDOCvMiInHRKHoVtiAWls4yShC0lJqrhFYcsjXisNaF_Sn4j5-76O7s8kz4ugfFza4_hPATwFtrGpScq844j9Q-5cWZ-WVylwYdGEGNYepH3LW7itBS0CEsZQ-0ks97-_r4ikQ7bkcijYvJwudLIbETXZWdZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W6fzeWI0ec0xt_SNbQjyWVyOhAeTgRYUUXrzsjswy51lZBR_Ks1TolenQUsgfbDhAuV8-VYWGtIL42eaSe75AllneipmUbaa0NTlBuMDkpi3CQDmnVONowg7phS3iGS9uvYqW7cPFCUJx49tLflvy3anNPQaXNkaUTZNE2kh4c9nZfjN3XmdkORpjdp0cxf65Co_VJLEXvEWa-IAyoirzTQo9d3Na8ER-Hbrdp9_MYctrQ3RE1wwPNMaGbhRFf00PX5QQtEmL-mZPhU2U5RjXC_YSJOKrEwg-hQvb9bbC8nX-qQUeCTtAfiTp3BVhztZ89fZnhmO3H8k5cBsGiGSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HQrWFYuvKuLWxOdT3kvNgIkjqcIGlGR04K0gk8z4kTNuUknRCQCZmMawiEjbNhDYdpjyujAbp1a-8mXbwV1atC2dCdZcZmeEi98m3ZF2KyFYczqz8QTPPxkL-DLFcmNg5bnm6h7v3j-cGhG1Ws1IXYXSz-MQqRw2A6fsVIaPgPcNGxF9a8GAeuTqmg2pFZNRzmkfsMlBYossuSG9w7MvVd5SRGMXyXYJIbBdEzXSxhRkM4SbpawQyAdo6KE-8NeOnddzfmhXIcy--OuQUQ1jbPusi2IDFZ5M8OPEuSE5OVKCSdOixduD3tKefqhGFk5JGIcbFkJIo2pHpOucDTteeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWA_6cgocgJPI4A4Mc2dxMvER-IsxRSNZdQDnWgNtuGpg2uTJV4t38AxAeR_vielAL36sEFX4Bd9yi8dW3WFmoY8RdY3rmVwvrdB5gOL0YeEA2C6Rn2OQw-SVMgOUJ1y3uJi1xBvzw13LSLV5dRnRO7CalZQOlsSKF3EiPDH4kfBDb_ADhadks6muqdGu4CGQytnk6Gjcd7fsvH6axipBauEKCGRLNAT7Df5tNI8Yqzd7hMW_1buaYZeR_HSgL6eT9zCJGL5y3OQnJrcVFwuelEm1dqoDACmAt3L_rBO79_rz7KOzUSx4X_mCKTvFCt6dlyMerTzWvWfPqocyPdLZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jrVmYiVhB7TYtGd6osZ3f5aUjb7ACfDZK-M0RggNUO7IK9BgY9ShKOhYEGbVf5j_Kb3X8S8VyH9SxFXZLLZ83P0R0gOFkpag7tVa_z7oAFH01MTi6xnwod-ZbNQNHnZLDvLBQjL-RcWCJ0pQR2QgkWy6GzH9l524D5KWi_Lk_cNBTYJdT2JNyQcmBBCQys5FzpCMdl_JrSf4jAfYvWJHBfIInMK07qV5YE1Hbzvbsuo_B03E-1-HyH66oWWNQj3PMeoWx9-6HWkY1Eqa6h6L_JGhqS1hD7ftmDJSibklVV38JqLmZaGv1F0JUO2j53BE7biq6VZDhIg01KQC0jz0ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NDKoPmfqSj5WWRS6Z-eTIbtaorHKq2lljMl_t4q-xvolwy7XoVSbd3c0wEfiMj2UKNU3vt5b4GZp8rrevbP7yKaozj5CD53rYt2-UZWDeWCyzbbQbrIdN1apJQB3woQbMZ5WpA5oFbbifD2yDQscoxtn_c7CtkB_AyuI0rdb-8gfYg-SA37JPNrj5gw4fop89xvoSLuXbDfagee1m9laS_NYgvJ0vvpV8G4SVZZbL73ihc1f9kbIpFhvoCrNWz33ioWaw9vqldII414OzVKtU0JN99l7I6-idgxcBl58gMeSgngs99LpZEJtxPnFLxxvtp75rUCzO1NgHndm_hbruA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید مدیرعامل سازمان انتقال خون ایران از خبرگزاری فارس
عکس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/441224" target="_blank">📅 21:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441223">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/628a22c800.mp4?token=rqfPv7it8bhf6OQFbtj06ZuCbU7YdKBZ5Fcg0osjehDCJVLjFVQb5IH7Oej0dEVh41RQhRdjUpy8Xk4UoV2DFXsCZxOosR94iicRZggmjkbFe-e1N-5VUZbHa89BVziLUc05Djod2REKkKjri4G-N93VUCk1hbgmhvTm7x7L5fMJrWa7suM9x15Bzx6esfMqgFJflLgUm6i4EMLh-crqgblAUzofAtQ1NJhFLq6HLWOrEIjKbUvSUURg7p54dCZT7d2wpSiAejuXBuGuEdaPdWT4DcVZV617UwQzrLAvnOraReyJGHFXCkjtZTXKd5tXPieoYGv8LvSZ4NCXSrRNmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/628a22c800.mp4?token=rqfPv7it8bhf6OQFbtj06ZuCbU7YdKBZ5Fcg0osjehDCJVLjFVQb5IH7Oej0dEVh41RQhRdjUpy8Xk4UoV2DFXsCZxOosR94iicRZggmjkbFe-e1N-5VUZbHa89BVziLUc05Djod2REKkKjri4G-N93VUCk1hbgmhvTm7x7L5fMJrWa7suM9x15Bzx6esfMqgFJflLgUm6i4EMLh-crqgblAUzofAtQ1NJhFLq6HLWOrEIjKbUvSUURg7p54dCZT7d2wpSiAejuXBuGuEdaPdWT4DcVZV617UwQzrLAvnOraReyJGHFXCkjtZTXKd5tXPieoYGv8LvSZ4NCXSrRNmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استمرار حماسهٔ مردم مشهد در تجمعات شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441223" target="_blank">📅 21:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441222">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHTzh6UAP-COFZpoyTHq5-ybxJjWjy5nrTAyDCOtWBcOhyvR5Skj63YbMaZOUIGitJMMGUVUpmkGuX7-t3hId-1RZgjXJZmPIvA-QrGpti4KtSz6MjZx0UH1ytVwtnvNDBwte8llhsR_YzllhKl1iOeejvHaZDz3n7CI9tI8gEiq3OJWNbsp2ShOEOGhETH5kyKd8eCkZ2TfJxcTpVqKMszWxD2DKuPkMa3Au6JJN636_kMBB_sdZWuu-e41F6MxmnHVmTY0emL6GtKXBIOHvPUSQ_XPyz8u9vzdcRWwttGppbSzjV52kny-kXtkNstuYdCj-QQiah09tPwYadP29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
خبرنگار: آیا به حمله به نیروگاه‌ها و پل‌های ایران فکر می‌کنید؟
🔹
ترامپ: به تو نمی‌گویم، اما می‌توانم این کار را بکنم. @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/441222" target="_blank">📅 21:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441221">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtvOIhTLNkQc7TshB8ruw2m6PlFL98Lw8PUAekiiqKio_0HOEq0fq8w1r-ZcWz0Rn-fIxpTO88xPUp1sylytVQsMxdMEAzZjZqtAPw4OHPeRumqqnpxVjghP7tI_NQE-OAZSww1VXm0RvNAsaHKPDikZsmSYu2wXXrWZXf--J747VaxjOSAZzO-zhAzesqKkoLLy06yMB-M0DPEvQUF5hkNq83X7xaJrFEyGt8QrfGJrGo6mBYvAWxh9stA3lUFleWUOBZFSV-qVKXdOYwubRCrKlCU8i2EcLUNssy3nQPck1yQAtw9d6N3rtgVJLIwWK8Mki0ed3e0EfQPRcJ9dJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر من نبودم، الان اسرائیل وجود نداشت.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/441221" target="_blank">📅 21:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441220">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONphVNEBZomegJzNeq0xhBo9q6dyKPsP097SskrTXk41G__x5o478DPP5gWREa9p-OfWq9bAgqNFtD4VxRrmqCeswgU71MOIExopVvWVCyXmSu5Y4igRwbR_6Ufxrl986FWvX-WUVIUWY5IRuqIMpREsZSgWkMjO5ixVhhz0XKn0Dj1KPrSCPdP26YMEwXAsPwm_lFOXfYKxzFiD_3xq1C2KjfjcVik4qg527a8udoWvsEBgTqCgeqYgIJ72GmbPrifJvCDTe3_2htFXNynjOmiahS8EjCvayBSf2W9U-5vdjviAfIfVRWOLoqPLz0P8Cwkh6R9HUYdEH13BOY6Mdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ علیه ایران سود هواپیمایی‌ها را نصف کرد
🔹
انجمن بین‌المللی حمل‌ونقل هوایی: اختلال زنجیره تأمین، ۱۱ میلیارد دلار به شرکت‌های هواپیمایی خسارت زده و جنگ علیه ایران با افزایش ۷۰ درصدی نرخ سوخت، سود ۲۰۲۶ را از ۴۵ به ۲۳ میلیارد دلار کاهش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/441220" target="_blank">📅 21:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441213">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7tZu2weZNHv480f32OFISQCFFwN-e2XN7U0zHdDZBFpfVcQqrL-ZBqACNCHm2xXMzotk4fwXG2QbASvj3e9hdZJJv6JKQQij9btDCCtMgG2W7TmkvrkvPpza8JZFRclWd-J3JkqyHnKrxA63U-gg9Z6loHvbQv_Aa1LV6WlH4FkNOi-F5Wko4Q43BXABYmLj4T57b1IeKCFoZPxht4of8MZ1TXImqR-Ft58c2tnOMK5RbfcFw2KT21jmqztcJqTt2WaDvnJuU_z08Bc4Fw4L5kUQoRzOVCrwGzLd2hZdesXkhjwpZQ8MuaVm63BsUkg6nqBwNoMhNC2T4pClRUGBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s5r5FBqGxeOhmwTMuAa5kxEFyFNEuN2yWw74fqhM7c4-xhNJ-pY2v95_A5bxtgLlkliaCePFPW1TXfk_7Yc-a4PxSGMeODJ3LjUD8hY85HXyzqvTsEp_LH9m0o4baI0SU30GdTYpdEutVshdgxEJlTqg_W4bI3TCwwVmN5GUdDVg3ip637H5piegxTy2bCL-mkzihSLicGFECHaI2yWpMoy4HVg3af0ZaBsNaQfroenMHYRWARQUXd43eiP-mnmQCm9Euh6gSYz0rzqRV3EvYmycY6I1TmMeoyd-r3bJZTwsNkQz__WsN2-O6SUz_JTH2hx6Asi6oGSrG83feOJtLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Srs4LyG1d_ZGpwEhMfBAabHYIYezucSbFjQD-lFrihDbYLqi-RZ1op84km55HZGNbSSRUJ4VTWv_LyY3bentAd3pJw48KGv5EnzVZWm3h41hahMYeSKsztz9CY_QuWJUKahXt9U9NAaOIG7euguTM_XS9A2ciXa4KXbrM5BpjTeDZMURet-0UspCfs9dAy-fD76K9tYVbJO6-MbPvKDbV4swGh7qTKIzdAgczIV9EVicyuOZuDUcWXAAnrHgVLCxoTe-b6mpZrTxZIY-XykJ66YYDkyrAHiHaJAildUS7W-ggfloqz62wlTztA_3bkHEKteQSPnn6YYHUvctgXNFLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIGiOsnEfGKPTQO8h-5LA26xg09-ThCeNxIy-mh_6gQ1dTJCMTE2YHQ62uro7fA8OdfSq4LL7bgUSv1Ijpxix2CLLxu79XXI_37p1o_xmrIOkyeSJYq5bvKkh3OFfXzAC5yrFvYeTeY6_a8YM5rd9TztYRTQ9VT1Tc0HKXzIgyYwOqkbP3MH8cFIO47FpYwyOpBEnbV0fiHZ7YfLUd_jktXU0rE66tjOpIz5g2K1-Hff_wTWPNyyv9pxzCRUERRGSUwQShvInhuDr2kDQbdZbBDD4hF-ufT3gIQIn2gyfJ_CcQLpOUEUMKLma0ilOVnJL7J3tm872KtZZtKyVQ0j8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bf1lVRvODw_5AY19oE8yaS1a2L36EKHh33BhB8yWXeAEuDldv2GJKrMHSaSYIHAjrBpwCzpEFMJf3467I02BE6Z8iRc1eM7G6ZtzxC8ymeWLvzuJwQSvcBcNfPioBCYDgXqmCS1JomFI6w6LrkLmVRK33VRrK_C4IUwSgB7TdPkNi1VQI6ODeGWaAev2sjTrVk4KidDvuXzWUY06TyJ-5nSnFqjFMWmGPvnEstdhbPyNlS6_pKS-BX4BapKlpQ_jwpnAt-h60Lp_5ShBiBg7wqpAXdOOXvuWhJlgJc0UIrxbLiusjsd-B7PGmnkBw8AVjubfi-55LOyU9d13OuxPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWHzfPHyqSzL4yr-TR7tf3RE15JIo4Z5xB7gCbHTweQXS2ifJ81PYofhtkkczKz5l9bTKrUS0XYhqDr3I2uPiUWjOMKzyCGFoBmR8rAFSgVM8cIIJwCf3JvxcFWZP04OWo5dCf_2rM2NsICAH94CzUKMGD1KdhAvC_iF80t1otHdlv3xI1Y9FAvBGL_3W8I12rgvMIcKmOC7lN7OL5xfvuLv77ZvaR2857LlFF-BM2CoRlW8mhooHUpuD1LGWVUrDPI0CQVJHK38Inl2Ur0jygsZH0QgU0ngBLDkmghkZ1cmSg0h450Nq810YAHefXZnLZgXRe2GQnCPWfS_lHzIKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/urLaJCPIAe440AFGVX70JD8DICoo_bWkho_QPyIvcrDRFo2S4rx-TFIlWZ7U9orrV1IQEeZ648OaJ9TxZ9b7KUtbpvtW-iPbK8tskIIJH_5o15vwzo6aSORGcCo9atX6i78JPsHjg3AJhri6Zkkojz7pj3h-696uBNKEN3RgZZvv4ZV2BtcWEbI7SbMO0h1mD_fPuCMpKRpMMn1qVFbxu8FMEAsJFxhnl-d_C1QTiZ5z2DzpM3cS2iUf4vpIqy7wZGpmvk8IPenXwFTt2hubgCAt9BXfTbb27U1yHF9z-_9RWbLM7Pu2tYQKCDho-3-hdsmc5eg_b3JrWr1eZrmlpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور رئیس شورای شهر تهران در خبرگزاری فارس
🔹
مهدی چمران صبح امروز ضمن بازدید از تحریریۀ خبرگزاری فارس، با مدیران این رسانه به گفت‌وگو پرداخت.
عکس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/441213" target="_blank">📅 20:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441212">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سیاست تکراری آمریکا و تحریم مجدد ایران
🔹
وزارت خزانه‌داری آمریکا چند فرد و نهاد ایرانی و چینی را به فهرست تحریم‌های خود علیه ایران افزود.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/441212" target="_blank">📅 20:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441211">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9I0gNginCMQmq6qkwdbVUmYlFzV6MqmCUPLrxJSNpltxW9EXE4_GGHXE1BnVuSnhqfTSFj5DFGz1rD4iIiaGwoB331hBnei4cIkc-tC359MzPdKWdPB4ek_tQ-33q4eDkU0Oq46cm7Xo80urcddvMdp_X6tvEwSLi1yg8GQGjp3wtvxgdU_ObX6nocjkbppHoiEdzKaiEc1z4-bFxbAoOQwn7rLloHP3kJl5g487BnInCvcSv0jC6x4mQcYv5CFZ8syNfuGO7AlMUyZ7veKokrdRcqu4mSM7oEifON8sEfexr_-94cjhtGlP_i_bZ_TXPsn6hSOjfZMlILEEcjlIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: تهدید به هدف‌قراردادن زیرساخت‌های حیاتی نه نمایش قدرت بلکه نشانهٔ استیصال در برابر ارادهٔ یک ملت است
🔹
ایران با تکیه بر دانش و توان متخصصان، وحدت ملی و همبستگی، در برابر هر فشار و تهدیدی استوار خواهد ماند.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/441211" target="_blank">📅 20:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441210">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🎥
خبرنگار: آیا به حمله به نیروگاه‌ها و پل‌های ایران فکر می‌کنید؟
🔹
ترامپ: به تو نمی‌گویم، اما می‌توانم این کار را بکنم. @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/441210" target="_blank">📅 20:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441209">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
سخنگوی آتش‌نشانی تهران: ستون دود سیاه رنگ در جنوب تهران مربوط به آتش‌سوزی انباری در میدان قیام است
.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/441209" target="_blank">📅 20:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441208">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
حزب‌الله: یک خودروی نظامی ارتش اسرائیل در شهر القنطره هدف پهپادهای انتحاری قرار گرفت و در آتش سوخت.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/441208" target="_blank">📅 20:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441207">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‌ آب شرب کوهستک و ۱۰ روستای اطراف تا فردا وصل می‌شود
🔹
مدیرعامل آبفای هرمزگان: عملیات اجرای خطوط لولهٔ جدید برای تأمین آب درحال انجام است و پیش‌بینی می‌شود آب شرب مردم شهر کوهستک و ۱۰ روستای اطراف تا فردا وصل شود.
🔸
بامداد امروز درپی حملهٔ دشمن آمریکایی به…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/441207" target="_blank">📅 20:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441206">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4bI8nr_QISTr9MJxGWBQoLtwGEuTEgf3kYQMJGMPF_5S1luFDOWoPeEqJm1HsOeT7nO2SLWE7SJh2NAimkZKiN9eFtSKu_aikMliHrSNs0o8ElGCuARl3ebhFUvTNtNtrHNRsNzHxnMg5Tgo-eCTJV28k2lxJHmW3ABKoV96esEJFblrXzVGQfhyqutyeWpKbnh3fjG61RW3n9q3ofXxn24JAqiFxdKH-8S9RnYulQY67h2W3btXkCvzB5kwzrlXasF-2zkeFbwPzPL8JoLRb2myAI-U4trSJYZB5sMpu82iSF-RUcKwo3ILhQtIXACSFdZCzui-plBuN5QTLIYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
دستورالعمل پرداخت تسهیلات قرض‌الحسنه ازدواج و فرزندآوری ابلاغ شد
🔹
بانک مرکزی ج.ا.ا دستورالعمل اجرایی پرداخت تسهیلات قرض‌الحسنه ازدواج و فرزندآوری در سال ۱۴۰۵ را به شبکه بانکی کشور ابلاغ کرد.
🔹
بر این اساس، به هر یک از زوجین واجد شرایط، مبلغ ۳۰۰ میلیون تومان تسهیلات قرض‌الحسنه ازدواج پرداخت می‌شود. همچنین در صورت احراز شرایط سنی (زوج زیر ۲۵ سال و زوجه زیر ۲۳ سال)، مبلغ تسهیلات برای هر یک از زوجین به ۳۵۰ میلیون تومان افزایش می‌یابد.
🔹
تسهیلات ازدواج مشمولان ایثارگر نیز تا سقف ۶۰۰ میلیون تومان برای هر نفر و در صورت برخورداری از شرایط سنی مقرر، تا سقف ۷۰۰ میلیون تومان قابل پرداخت است.
🔹
تسهیلات قرض‌الحسنه فرزندآوری نیز برای فرزندانی که بیش از دو سال از تاریخ تولد آن‌ها نگذشته باشد، به شرح زیر پرداخت می‌شود:
▫️
فرزند اول: ۴۴ میلیون تومان
▫️
فرزند دوم: ۸۸ میلیون تومان
▫️
فرزند سوم: ۱۳۲ میلیون تومان
▫️
فرزند چهارم: ۱۶۵ میلیون تومان
▫️
فرزند پنجم و بیشتر: ۲۲۰ میلیون تومان
🔹
این تسهیلات بدون نیاز به سپرده‌گذاری و با ۶ ماه دوره تنفس برای شروع بازپرداخت اقساط پرداخت می‌شود.
🔹
متقاضیانی که پیش‌تر در سامانه مربوطه ثبت‌نام کرده‌اند، در اولویت دریافت تسهیلات قرار دارند.
@refahkhabar
‌ | بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/441206" target="_blank">📅 20:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441205">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشهدگیفت | محصولات متبرک و زیارتی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhM2lxnC-ZNoS0UB9xtc6sBciuXqxy1GrjYiPHv0m655vsjHOFP6AckBp5--EYBWatpfbKwIhJtMqwHxsXlYqr09-Rskan4hzICxUpwmcIJNyfqxI-YQ1i1b_JJZswr5pEPbGoER7cp4fFpxDTHnpDXXpBFfQJ7f53zFSrWAGEpY70OYrPEhMEAnt4wH8Ei_ysnkAWhboyv5Lum7hKcuFqbOdI5mEDSaJAzthK4EfvpSu7y-xdafWYtlwj2MD_AOye1XC1zV5sfjUyiYJr6YbS2bHH8a5X_DjSK_Yak_icds6IFgDLCw04AF7h_7IBHRVORGlbZL1qawwtfj8uj3sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهارشنبه است،
روز زیارتی آقایم امام رضا (ع)
روزی که دلِ عشاق، بی‌اختیار راهی مشهد می‌شود
سنگ روضه منوره؛
قطعه‌ای از حرم مطهر رضوی، برای وقت‌هایی که میان تو و زیارت، فاصله‌هاست
✨
✔️
دارای شناسنامه اصالت متبرک
🎁
به همراه هدیه
‌
📌
بهای سنگ متبرک روضه منوره؛ قالب دایره 480.000 تومان و قالب مربع 380.000 تومان
‌
💬
ثبت سفارش و ارتباط مستقیم
@Mashhadgift_sup
🔗
برای دیدن سایر متبرکات به مشهدگیفت بپیوندید
👇🏻
https://t.me/mashhadgift_com</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/441205" target="_blank">📅 19:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441204">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/441204" target="_blank">📅 19:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441203">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
حادثهٔ دریایی در نزدیکی تنگهٔ هرمز
🔹
سازمان تجارت دریایی انگلیس: گزارشی از حادثه در ۲۰ مایلی شمال‌شرقی صحار عمان دریافت کرده‌ایم. موتورخانهٔ یک نفتکش ‌آتش گرفته و خدمه در حال تخلیه‌شدن هستند. @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/441203" target="_blank">📅 19:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441202">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344d92cb3b.mp4?token=az3q5RojM_7ZyX6t9IwO7WKZ6dbmHHBN-SdB3t9GvxjANXQkk_n97De5kw8C33WGgUGUqepzARLq-ng7T8Frrm1fXT5oTRU7yIUMzQpCpmWpu3abELCOeqXhJP1wmrstL9uipbjUyOfrpu51gvbKdIc1bqiVKk90MQ7AFFkRoHIG7H_BdIaTcn2W9OQq64Jm8t0ErxMFYD30ruXpoxs6WI-R7119IlxIAEBOH_N4lNrIa9C4XWCXkWPnqZpAFL7l8NfqyieWbM1D2qJ5RyUwf6FA-esOWq960XhreuhmsNnn2oX2CkiYKVFtte2M0wptkQHXkTNRrGMTv5vXWfbSAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344d92cb3b.mp4?token=az3q5RojM_7ZyX6t9IwO7WKZ6dbmHHBN-SdB3t9GvxjANXQkk_n97De5kw8C33WGgUGUqepzARLq-ng7T8Frrm1fXT5oTRU7yIUMzQpCpmWpu3abELCOeqXhJP1wmrstL9uipbjUyOfrpu51gvbKdIc1bqiVKk90MQ7AFFkRoHIG7H_BdIaTcn2W9OQq64Jm8t0ErxMFYD30ruXpoxs6WI-R7119IlxIAEBOH_N4lNrIa9C4XWCXkWPnqZpAFL7l8NfqyieWbM1D2qJ5RyUwf6FA-esOWq960XhreuhmsNnn2oX2CkiYKVFtte2M0wptkQHXkTNRrGMTv5vXWfbSAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران مدام ما را احمق جلوه می‌دهد
🔹
ایران مدام ما را احمق جلوه می‌دهد، چون با چند رئیس‌جمهور خیلی احمق سر و کار داشته است. خجالت می‌کشم بگویم چند آدم خیلی احمق اینجا نشسته بودند.  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/441202" target="_blank">📅 19:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441201">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d250ea597.mp4?token=FojrtapEeuatsXhvI_j-Cp6wOHzwGDY51FFe1OqYGMtAGyz7rujZ7oF4Haib9P3yoTpCtIzrDzRBdI5CoiLhIKp9dn7eZ3n7ax_qAeFWAAwnmRzZ1N6dfAJGwHTu15IBFnYodp8-3qKU_6K5qAH1WFoC-a4YEKK2YiXeijDw6Yjqcbqi0eBKGgMiBSqm2lx3QDrTmfcS2a68gLVxEkcZ_YJmfstXx1l-hjKuB8571Sz6GeDqRnff4b7iWYJJyK6AT6CtuWLXDozoYlkthiACZP9x20_-etH7JYy0qPQw2Fkx1QlTiGu275H7x1dE6cGyhMmSiGGz8aPUbkgrLw_lkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d250ea597.mp4?token=FojrtapEeuatsXhvI_j-Cp6wOHzwGDY51FFe1OqYGMtAGyz7rujZ7oF4Haib9P3yoTpCtIzrDzRBdI5CoiLhIKp9dn7eZ3n7ax_qAeFWAAwnmRzZ1N6dfAJGwHTu15IBFnYodp8-3qKU_6K5qAH1WFoC-a4YEKK2YiXeijDw6Yjqcbqi0eBKGgMiBSqm2lx3QDrTmfcS2a68gLVxEkcZ_YJmfstXx1l-hjKuB8571Sz6GeDqRnff4b7iWYJJyK6AT6CtuWLXDozoYlkthiACZP9x20_-etH7JYy0qPQw2Fkx1QlTiGu275H7x1dE6cGyhMmSiGGz8aPUbkgrLw_lkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران باید توافق را امضا کند
🔹
رئیس‌جمهور آمریکا گفت که ایران بایستی توافق را امضا کند. او گفت که این توافق یک توافق «خوب و معنادار» است.
🔹
او همچنین افزود: «ما امروز دوباره به ایران ضربه خواهیم زد.»
🔹
رئیس‌جمهور آمریکا مدعی شد: «ما به حصول توافق نزدیک…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/441201" target="_blank">📅 19:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441200">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🎥
پیراهن‌های ورزشی شهدای میناب که هیچ وقت پوشیده نشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/441200" target="_blank">📅 19:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441199">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRxcUWaAWCvO9jhS7nlNkCD-kVPY8PEJwHGAilyZaEJCcGEbRo7ERRJlfcjNcT98MXcriAxT5H6dGYtR6sfefsIFt3kujS-up8ycnmaLuLbxIRg3hK3zE5_s21Gq1l2ILGwM6EVgbu_E8Agx4K_oKus0KSBNkpPILs32FjMGON567-Pakp0zTrfGvnJKXicvpQT7_X0Rd8oNR0qI2kPnAf8-cgdSUt45e-GO9gBJqfhyYp1Il_kJ43J70gXdKDtc6iRDg9Jiv2JSYMF5nMtkcl5u1UNtzhdt3hRID03VPKMHiYZNojqDzqnp0dbtGm7vhOfG_4rihRLW2bfR-cbvtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
کدام پایگاه‌ها صبح امروز هدف موشک‌های ایران قرار گرفت؟
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/441199" target="_blank">📅 19:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441198">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ1DiOeI0opDSByyBMr_V4WDNIghUXjLPT_7N_ZiLklVPBtfV-SB7YP1EJCSJNz6VT7nmBcrR2Fh697_XmIe_68azu-7D5SF4eMTUaicefI4QvqvkltHzUqyYP7quK2KyS7cr5OZ9r-7elGZrKYd0dJ8tZ6CIl2FslFHdYRlEz9wp5UxSOElKdbP0PNztoCnpcMPqVZAL_ORSr-q_Hldb-4tImHcJSrgiEwPdsO_nfwOMg_lDt-5UMfEuu0NZWE4Rl-bwxaPEOr5bUwsIspWcMHhb-rjdkxsYyC5ZZcoaG_CjQR7blsgmPcbFLIFR0AaqlaQlyO4-aWg2YMq45dKmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران باید توافق را امضا کند
🔹
رئیس‌جمهور آمریکا گفت که ایران بایستی توافق را امضا کند. او گفت که این توافق یک توافق «خوب و معنادار» است.
🔹
او همچنین افزود: «ما امروز دوباره به ایران ضربه خواهیم زد.»
🔹
رئیس‌جمهور آمریکا مدعی شد: «ما به حصول توافق نزدیک هستیم ولی ایران همچنان تعلل می‌کند.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/441198" target="_blank">📅 19:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441196">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7dDTWydp2TayUSt8UZkYXPQ0fZCGye2_98YPywV8atyqoaeJvg8AJryE1KR3dv40e16DJ0Xu3OzpHO8OiL7OSqGEWJSfcFuG_OAIPhbsobYsT0OkkM0bBltaATgP5KZousupwUIAyprgOtOuXoMbtEfssQhTNKAKNzAbqrPU3lNbDpHJ1WoO849ZXfwPqkm3AVG5-Lx1-Ku4TP-EyM-nl77Xqu6jzRYXFylXAK8uOQQKgC_Q4mdwJqzGKyfTQ9GuYVKiOFHge7q24m9_YAWcLzslCOJvnlPfl6KWspThlAANHi9WJVr-j4mIjV-fsIVJlCiQMsrEN3d50eL14rDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملهٔ نظامی، یکی از گزینه‌های روی میز ایران برای رفع محاصره
🔹
در کنار دیپلماسی و توافق سیاسی، گزینهٔ نظامی همچنان یکی از راه‌های مطرح برای پایان‌دادن به محاصرهٔ دریایی است؛ گزینه‌ای که به‌گفته تحلیلگران، نمونه‌های مشابه آن در باب‌المندب و خلیج‌فارس نشان داده حمله به ناوهای آمریکایی می‌تواند هزینه‌های سنگینی به واشنگتن تحمیل و آن را به عقب‌نشینی وادار کند.
🖼
اما در صورت انتخاب این مسیر، سناریوی حمله ایران برای شکستن محاصره چگونه خواهد بود؟
🔗
پاسخ را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/441196" target="_blank">📅 19:22 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
