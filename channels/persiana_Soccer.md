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
<img src="https://cdn4.telesco.pe/file/BeLSskF5GDFEfoeftmQ0aCWSxrsQ31UgjHXCXaY0nEdiz6N_AHst36mPCFvflWGfT_sKxfd0M1SdUXMTwMOYxOG32_sCyBDEyM0DsnZe3ejmQaXDJ-XitrhcNCma3EddPN5CbKH3Xg4hM54nRn-bIw4wj6dHgAw32DZRNkeMgsIxJFDPWDzrIOCxINE7dVQkVWIi0oOo_2Ef2-CGobgzd8Pc3MfNDoBw7YHiu301sczTvW_fzSvilswaJ5WBKE4Tc0fYW8glcBG2s_-1h00Srg4Z4ULxm3VKKtdrJrJ_axQxZ5bgH_FzVdUnyu46SfELSRPyKGvDfE673w2k0-IJhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 442K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 04:29:35</div>
<hr>

<div class="tg-post" id="msg-25567">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iit51OLH6yRtsqADh795Jztamu1YIR48zNET5rPKlv64tNQB8thNjh0TEIuvrWRLNXMaaezBFkFuid-5D5yiKoTixpRJ6p_VslKUxinKnoidhui_xg6ff7I0BC_hgKFtYQEXNanwx7N-Wc_Hstc24EOnyO_M5hY6g4dwM32p_-H324T7Gr8UVk_8faj8AEIlY4AvoKBvJoxF0W0MQR6WwYuAkTnBub7gV3Du1pWqGblGfZBnmU3rx44HSRRc00dmO6a0TAllfyBcW3yXNXtySZHCoGIBsv-PG6T3ZbNBx7i7u0D4SI_UkH_IUdSUVcmBc4LDd-Gl9Tr-Zx38we3nOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2AorHUgtGkpOX5aU9ShHba2rMzRhE_EHQ5rqV6P3HaapjNt-sgTC3yyfyCbRxC56CdNbBBMo8qyeN1i349gwtLGElhClm-vcmS4HQE5-I3TfcNVrmRDVul_bEtprufSqBNGa_KaHoGy3oaMgkqe0lkgJATC9R0HWl6873JZGJMKttZQloaSpfye7IGVdWAUmgxejWMrlrXWWmxcTgtMvMohOQ1wqhLwgkEtStU0nckHh09nclKrNOM0hMb0MnTpM_hgVoDopUEfD9AAep-hGfBPFmO1yRL1AqGiHLOrcILN1AYngCgdJBf7NZPmRCSV8rq1TXynEhyyPrXzcyzOOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/25567" target="_blank">📅 01:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25566">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nfa-oitmz525IyDyuTHT9vpUomW5S8oeumiu3-4De7AeadTNFiZ2UprMoWGPXFbpw2YYI9fVQ-vAjUoVhscx_T8R26qpDGLpO2CQco7DcVv86KAiU4FYj0DEkQD9ebR8YcCqCEYqHkDJgSwMuqoPDqLgIgj5Aj4Keb09SRrMxke0QRiZS6C_X5KawdyazkIoqR1D4GpksZzApcfrzQTa7B66KYlEJDlfeNcNOnDLzBfK5_xKJ-N6uyr8IUZ1W0IvtHpibXwTopTrHOuv-p-bDdzgrzvGlKx2srP6Gk4ga6J0yGfaLtN1Zr9r51Ctse1PC3gF-n08UKZ4xH3m7MqU5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/25566" target="_blank">📅 01:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25565">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=JYFGsyrU6qIWvvzJN7u6_-d9Vk2mjqozm7mghcOcirIagEPzYTl6a_qj4l6TlZXlXwVj4vYxr9yyG2KRdRINuFM41ngv9nWkoubaPurbl81cRhrVKOVu7AXk5NplcQXYxU6GA-IPOkvgLCrJonvZjY0sCwNO2C6WB98v8XIF1g-gzE8--17HyGVq8swddEKJgU3FTEqNOBSNbBBc_7fZ3dbn8sSCytXzP7iVHxuzmVom7rgwGLdF2KYsngrkqRUABOmZ-YQWJbaNFI3VQpLmk8GX8t6L3mxPqB7qqDtfnEUqD5BPeCAfu4NiKpBJhIUtfFGdMurSDaiw4pOu4QohDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=JYFGsyrU6qIWvvzJN7u6_-d9Vk2mjqozm7mghcOcirIagEPzYTl6a_qj4l6TlZXlXwVj4vYxr9yyG2KRdRINuFM41ngv9nWkoubaPurbl81cRhrVKOVu7AXk5NplcQXYxU6GA-IPOkvgLCrJonvZjY0sCwNO2C6WB98v8XIF1g-gzE8--17HyGVq8swddEKJgU3FTEqNOBSNbBBc_7fZ3dbn8sSCytXzP7iVHxuzmVom7rgwGLdF2KYsngrkqRUABOmZ-YQWJbaNFI3VQpLmk8GX8t6L3mxPqB7qqDtfnEUqD5BPeCAfu4NiKpBJhIUtfFGdMurSDaiw4pOu4QohDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/25565" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25564">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd764fc92f.mp4?token=bCggAcMYdbTfTl8RoXs7_hQAYFzXgXnydjDRjWdKfi4KeJ9OBMBbuW9ElE5WIrL1fyaLUgjyJuZRPK3uHH3k6t5mH4L-8G6YtHrA4Mf8NPqPDOtsTNQrZKkjb5D-oyi3y2hBlHgdBQgL5b8CKdh179UI6Mis0mN-xqtuyRTYSoiYDuFoMnFASpzMnbh4YBev0_efa-ZVDXSy6AFih-iP_PZoVqtoFONf991rCbcQ6U-b80QzV6evhWGIWR-MOk1Y0WmUK1CpWKD1OWWtHTWxJEvf-xgaCucRc_kEttXAdlwrLv09Ep0WBoQ-gysCmOFOxppbEECgG1xVloTLru4M7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd764fc92f.mp4?token=bCggAcMYdbTfTl8RoXs7_hQAYFzXgXnydjDRjWdKfi4KeJ9OBMBbuW9ElE5WIrL1fyaLUgjyJuZRPK3uHH3k6t5mH4L-8G6YtHrA4Mf8NPqPDOtsTNQrZKkjb5D-oyi3y2hBlHgdBQgL5b8CKdh179UI6Mis0mN-xqtuyRTYSoiYDuFoMnFASpzMnbh4YBev0_efa-ZVDXSy6AFih-iP_PZoVqtoFONf991rCbcQ6U-b80QzV6evhWGIWR-MOk1Y0WmUK1CpWKD1OWWtHTWxJEvf-xgaCucRc_kEttXAdlwrLv09Ep0WBoQ-gysCmOFOxppbEECgG1xVloTLru4M7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تکمیلی؛ علیرضامنصوریان سرمربی‌سابق‌نفت تهران از بیرانوند خواسته‌قبل‌از پیوستن به‌تیم استقلال این پستش‌رو از حالت‌ارشیو برداره و تو پیجش پین کنه!  علیرضا بیرانوند از چندپیشکسوت‌استقلال خواسته حمایتش کنند. منتظر استوری‌های حمایتی هاشمی نسب، منصوریان و مهدی…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/25564" target="_blank">📅 01:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25563">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ff28adc2.mp4?token=iZCDb6K1-6pu-lUZa1d1AwTdoB5wSMPaXTum2G2Y5_Vb2lMn6fqKyJ0pkcz95weGYcfg3hUcqYVyA0cvmye_ZRc103VXvc1IjB314yTjYplb9Fo-Z0DI_U49-ScjcO_64N-skZJVBOW89uUcWk65FHeLaJmwWA0kTAD5KSIQoakyo30jqsJ_H_eE06S2OJN608rOjlfk8zwXbIFp705RI407xbrSoJ09VTLStB-gbwFmjCq3VVwFhBS4_-zFGtvvT7bmZYcrC2vbo8hApDO29zl9G9AL8lO7WSuag4WNBjjC7J-RBIb5Gbzl9YUBSxI--_H8-fJAkbrXPiS0_R-Qng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ff28adc2.mp4?token=iZCDb6K1-6pu-lUZa1d1AwTdoB5wSMPaXTum2G2Y5_Vb2lMn6fqKyJ0pkcz95weGYcfg3hUcqYVyA0cvmye_ZRc103VXvc1IjB314yTjYplb9Fo-Z0DI_U49-ScjcO_64N-skZJVBOW89uUcWk65FHeLaJmwWA0kTAD5KSIQoakyo30jqsJ_H_eE06S2OJN608rOjlfk8zwXbIFp705RI407xbrSoJ09VTLStB-gbwFmjCq3VVwFhBS4_-zFGtvvT7bmZYcrC2vbo8hApDO29zl9G9AL8lO7WSuag4WNBjjC7J-RBIb5Gbzl9YUBSxI--_H8-fJAkbrXPiS0_R-Qng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
خاطره‌جالب‌وباحال فیروز کریمی سرمربی‌سابق دوتیم استقلال و تراکتور درباره یکی از شاگردانش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/25563" target="_blank">📅 01:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25562">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qY4sm-MDalFaOrFdFo05u5Jjoe8SpLXPnnvU3M7fAB9G_RpdQgaNmkVxBQarS66uLcfjja3u9D0f8KBmWVxI2GoPUJvhjYIJXjJ0ZykSos2cf30zFhjM_QYVrrbBSPmMY8BPoZ4IKv_sPkKbHExxiTDUaaKqSPyn7xg9a7vNwtzCu7Uim1D1TSB7s7oyz65VCytnrjFzcekuibNLEatLhwyrINCgj_iOZ7TDh8a6IiPqVqvHrrVr5u_NKgsF5iYsfSHaMyDwQet6AL4IzF4qHoFPJ6txByzF9tuqQBZOzvvSWlq3FfYZQJP0-V6dMFcwDWprVMPu_vRzBVidcrLkEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید تو شبی که همه رو برد بلژیک لوز دادن ، ما تو بت ویژن از آپشن‌ساده‌سیو و آندرگل؛ ۳تا اپشن وین گرفتیم
☺️
🔥
از جام جهانی فوتبال تا جام ملت های والیبال و… هیچ ورزشی از دست ما نمیره
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/25562" target="_blank">📅 01:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25560">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st_ALKGkmD7LSHU7rB4kgY9G5poPloIEq1oBtJJH_Qi0Ugnie-9ftSlO_E8pApzBlXbh1XZZyUaqlCTesWOHE3_L-adwJXjnJ8lLeKVdHztKUzuywiu3Z4AD5JI8p9ZtIpThm_5K_0wBhQjR-h4bQbsEo4yfTlgNmaXOr5fPjXOgFbr4-aMVeuiXz1qjNDuOBEllmmXACiG0GCBTeW2W0zDxeIBufFXNEXuM1umkFuhAkGZqtUpOZiGbnjoRUIY_3PF0roRUyMXeDIqC1gwr-nUEy0KWGF4PQmf4Tz-HrTx62ftMyk4Oy8GF7weDH7xefhdWc-wyPARqbAMXhn60HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فوتبال ایران عالیه؛ خودِ بازیکن هم نمیدونه دقیقا رضایت نامه اش برای چه تیمی صادر شده. میگه خودم با پرسپولیس تموم کردم و داخلی امضا کردم. یک ساعت بعدش‌مدیریت‌باشگاه نساجی میگه ماامروز دزدکی‌ازتعلل‌مدیریت‌پرسپولیس نهایی استفاده رو بردیم و 800 هزار…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/25560" target="_blank">📅 00:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25559">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIcOzAo93kW8ifsGHXXAp9PGkMKx1BqRdOq6bbprvB_WCyp_Q2eZpzLLcN0ZPoIeVxWmp1u_GUuGa7E1gDn6ukPYGgIxOYnOSbIKF_XYwTE6AYa_Ssk4bkOhi2TnBUWE2e3RrXwM3sW3w6tM0J8vYb35C49hLh6LRNkZnUTvXWiLYxdEcjbvzSQLYliKRCUidbwYqiBQtYFgTmXNAXjz3jghfSImCyktqsvG4SL7L8m4x1gGplyvy-4juuFRwIAMZxGX3Z3cg2xBgBvzii4F_7nLmML2HcedMSK62pjCkUDvfJEKPhB8O2I-TBy583VRgUn2HzhccY8HQj04aowTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/25559" target="_blank">📅 00:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25558">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIJnXuks6_U-lN_uLyJNSdZUyisSDiY9LMeI8FhkHBNcIREgLVuQTorSumM4C4cI9eTehMZqUvqjxq8VcP3zA0YufQV_C2Wqy-tSKtuE-NhMEKmbz2q3kS1Ljtalq8Di-TFLnkjpImcluR8dvmiG_8TWhhQAxpda34ti83d1ydw66F3VvbV_XUXuwHHBNGLJDUdCBz7gm-8TsahoVTMFLGPGuWXXRIXbuDgaXNAzDt0qlRzXhCZaXHJBDG18WmZ4p8QZJN4Gb1QLkJ5VFfymAqAhbUMBUsMt1LO0zxx-_8quv5AA3zpEmfPvqedMhY94NCEpA5KWN5UECHExvs0rkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/25558" target="_blank">📅 00:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25557">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpJPnXdQ8MxpFGAtp5BPVEvC09GXYZ7MTFeJmInBe3LW8KfGMr53k6GUgFiW1hyJaML3ZLL3ZebA1lmxE4VJrtjyqzi_LG10Bg2lOoteli2cDRDRRYAmLOrzLKzSTsj7UhRNzoujaQdRjAA9YE7p-d4woABlVIUW-Wf3haLWF_zz63ZrYFT8aAHe_fyfft_uS_DQBm0f2TjSO-UcbGibmtudCzElGp1LPfYXp9cS_j4p6bbC-jlNjPUGlCJmCzBdNzhTYAdKhr4BQPb6G-og4NMglFuzMOovavDflxojewupm-v_55YlPY34h6EBsxk5plIB7Pbdn-vWrinGrTit0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کسری طاهری مهاجم جدید پرسپولیس: ظرف 24 ساعت‌اخیرکارهای‌رضایت‌نامه‌ام از باشگاه روبین کازان انجام شد و فردا باشگاه از من رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/25557" target="_blank">📅 00:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25556">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JynSYoJJOdg4vnG_LXmMQX08mHqtq2MpH3-7Y5AQSChdTcVRP3CXqvQ4TnQhk7GR31Ro7mJil-WnzkZTQgMhPbcY-1XMD0lfFtK3SJIhSyx1JhbfiQDBZQastgd5QlsQUgThcIewd7D37S9cB7_7V3etsfzPl2tYgmhQmEY6Ugu9aqm0XOFasI5xuwBT5lSsZjSGDM35p_z_stqQcp3SgOkzCrWaO6G5SfcaVtzhbLrpwqoQP0CgZdtVrTaTVc2X2bZDLar23wKS6M5tMdUfFOrIdRTWyeuD6b3vpTsozJmhkObgvbMzF7RSdb2YO-YbLy5jZKyaOyFG1Y_JKIRpnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه‌عجیب‌ زیکو بازیکن تیم‌ملی‌مصر:
لیونل مسی، بزرگترین بازیکن تاریخ فوتبال است، اما بعد از کریستیانو رونالدو و راستش را بخواهید، حتی حس نکردم که لیونل مسی در زمین حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/25556" target="_blank">📅 23:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25555">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a89f9e96.mp4?token=YHUyvdH1JoZimsC0rneIcmlo445oaGGO5yDDsdGcy3CnWMpVr2d5nEtjeDRUl4wMpErk2D5-Z4YedRpxoIVOsfJKSbKSzqGb6Ug60JO3GuiidErBX8QQih0eQrAfflPcYRBp94cjmmgaSkHMBLtm4G4NHOEf4k1N04LG6jjFvTrfbKRvargmTF0skSHczQ_RzvFlDMso7AU_kaRrHfEhoPwfM6TMR9y2AaBHuJcN5aPpQq6-x8yrjMyOzsEwV-2ilJ7MZyg8ei0RML0TLQvmVI8AEnf0rsa0ivuIPAi0Gypftm-tNxHYxLOO9fjKPlyR5KEWyZBSIpDGSFFITb7HPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a89f9e96.mp4?token=YHUyvdH1JoZimsC0rneIcmlo445oaGGO5yDDsdGcy3CnWMpVr2d5nEtjeDRUl4wMpErk2D5-Z4YedRpxoIVOsfJKSbKSzqGb6Ug60JO3GuiidErBX8QQih0eQrAfflPcYRBp94cjmmgaSkHMBLtm4G4NHOEf4k1N04LG6jjFvTrfbKRvargmTF0skSHczQ_RzvFlDMso7AU_kaRrHfEhoPwfM6TMR9y2AaBHuJcN5aPpQq6-x8yrjMyOzsEwV-2ilJ7MZyg8ei0RML0TLQvmVI8AEnf0rsa0ivuIPAi0Gypftm-tNxHYxLOO9fjKPlyR5KEWyZBSIpDGSFFITb7HPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش جالب فیروز کریمی کارشناس شبکه جم اسپورت درباره صحبت‌های طارمی در رحتکن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/25555" target="_blank">📅 23:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25554">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDzh2d0ypJFhMq5CuyuyLhCQMe1LmZ2dprUioCnyhTQ9Bw_3gZIIsuXB1lRJ9mv3AbOhnGbefttGCj6RbmW_rYV-DjLTT4IxE_VAVDtk4X0LxNEx_pLBJhndaWA5liX1DJ2j09W_fnA9EXJYegfDBwtRMcwCG09s23KCkay3HpjmuYPdIVhJC0RVyva0rEVVNMCunc9n9mbjiD6wfcR_cl4MYgxsCwlYE8hgcfxy7xsymKa_DmAD4oOFFF2XAkOTIgQY6qYrtiwVE7KmUMheN5SjRuLnLpArKvoj9xSWK65sO_uxW6s-CNqW_oPRoPA3uxdxfvmJmHj6YTTdg4IGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
رنکینگ‌شش‌تیمی‌که تیم‌ملی آرژانتین در این‌ دوره از رقابت‌های جام‌جهانی‌باهاشون بازی کرده؛ به هیچ‌عنوان‌نمیخوام‌ارزش تلاش و کاری که آرژانتینیا کردن رو پایین بیارم، اماازحق نگذریم آرژانتین اصلا مسیر سختی روطی‌نکرد و سخت‌ترین حریفش، تیم ۱۹ام رنکینگ فیفا بود!…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/25554" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25553">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQMammMSGbIEN0zu0eXYpe7mH7S0vEW6UMyjsJ0OUsxHDvNoOEjdtKa7VQkw7VABwUkpQoFJDYfnizh2IALb4a8gB-NBY6mjhG88bCab3Ijph7Tw7d98NpmGklarHVux-Mf-ejh6HVDAclM7nK3fLorfbEIgRWKYaZIqBujmTQGaiOm14CEGC--UQiMW4FsrSfuLPMXFkgHI4hrT3lS5vxpViIr6cR4-GTd1Sakc_2YYpNFvfT6FEeRCMAxzXf01cl0Pc4UUimzMDwftXEIUttmXTJIYHujSplwaIlTwU9NpRPWFX6eN9N7CuhP4rF2TpxDsBYVVaMwv5UAiEMDAwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/25553" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25552">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcFgNrvzTPws02Iigu9fSoxh2CHi14cV2aZbNEV3SD_a2zSIoKIyMkJe0KY8UqyNzNANCGpC1atT64hd2agJEPNrmTWjyz5FOiErYcHmQYNMsA2iLfiwyHlD7unooqQ6Qf36I2uZuOIhesPnmvERJaA4IpDSvvUjOeqpwk8KbQ00u_nFvVuM8p0k_L7PXfmlNOXM02HTSAaeMTNb-Oc2qQAsJ7_DkVZwM2xwrRFA2hHF999ZMntBhTJ12-Xf3JVQQpWSm_2gXhsdK_zeT7I1pXItrcopaJFmyYqCpAv3n_iBg2y2ARiz2gjOQKxRvlQ7sPCbGD6iqFoY8qfsp8MMMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛ جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/25552" target="_blank">📅 23:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25551">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">📊
🔵
عملکرد مهدی تیکدری ستاره جدید سرخ‌ها در باشگاه گل‌گهر سیرجان:  ۱۳۰ بازی، ۱۵ گل، ۷ پاس‌گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25551" target="_blank">📅 22:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25550">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GP9VVbBkx-rFjbAwESiLHmm2PtNAl1UJrjYrFWWRyeFa_1SfluVsrAPEAuwwTxsqkLPcFtktRmjpI-aC6d0FuUwiGlKxnx19qQkkZVIrS9P2_yDkoqx5oxn3sqtgUAdA7-y9tP21IFXwvAH9dhQ4unhTv6ObWJypLkUtwFagBurdrFCeuL1y7xSFWNezL6Ymc9d9v5SpbRa2DEkyID1u9riUDUWniMpVZ3cu8KaMgpfUJYBsrLkObnhssmiK1MGpfFX02NLfQU3URAJ1G5v1LPsLx3XZTKhRGv2uIeri91jB10-tzG_t6L-0io5BEKaj_es_74bEaV29W-DMUyWPfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25550" target="_blank">📅 22:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25549">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu5ai3V-NXiQ3DUxdCQDTPMi-B7QzA5GiO4nUGtYoOiJ7CwcBSWVMXLR3JlVKa-IZCMbfDalHWOYeim-EQP5zW_26v6n8YZdudJRXbWozB26mIScS2Jngo6rG5OzzyixoNu-ZjFYeVPD5XVzc5rQBxg8AuyYGUKHLuWFK6CjW6m1MGrWxBZroLkPk6N23QeNrapwIK3i6Y6rQBw_xB_t2YsAVoGLVjy3b2K5FsyVOEnvCW7oxwHEk_uTK6380j38nIyV9JGl6q99wBQ51jEEQKHUTJgpMEVN57ZZWyJllHPG4_IEHI09IUfEr5uHWL5n3G7z7jlu27vYVX5uXWiByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس ساعتی‌ قبل با پرداخت 700 هزار دلار به باشگاه‌روبین‌کازان؛ کسری طاهری رو باعقد قراردادی یک‌ ساله قرضی همراه با بند خرید قطعی به ارزش 500هزار دلار دیگر به خدمت گرفت. بخش رسانه ای باشگاه بزودی پوستر طاهری رو منتشر…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25549" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25548">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfD-FvGdc7KuBykd-fFXj60v-5Ei7lttpgpdTHGrbDqhsqRtgtEJdqupnK0R0ahhMs6kt18EUiocnL8_XVm_dmfRltYXhUZoXEYrYsx3lrp0fV11Bf4zmIsFre47m5nr2ymWbEXwviUdGgy16-EgxtVcijsbzdFpbdT3gPRXVToN8S04tpcnyI9g-uyi13XeC_SOetEgxPOJA4IeBtYg7vvxjeMYhJuKCvCGyB_FOwJBUgyrxhtucMVeMOIPmkCK5fX_QNhGbd8wfHMptQLckZSYAGNk5ksuwUFp30MGLE0Tddux5x60Yt8VLlUEEGys9aBm99eSPJQACB_2Pmtiig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇱
فرانکی دی‌یونگ و همسرش که در تعطیلات بسر میبرند از چلسی پیشنهاد رسمی دریافت کرده. ژابی آلونسو درخواست جذب این بازیکن رو داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25548" target="_blank">📅 21:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25547">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROSfb8TzjmxrcgEVvg3p4innSQgYNZglWDg0BjyJc6MmIeOXMZKj-2rV1LkqlmxXYMY-OFhlGHlVGFVSQhgBMroIT3AmgjGR5luhs3mzN9AttzK617Fi_i-a_tX2koAwpUPGIhZCusRDW3W4VWl84DjjNQsfi2q7NS2utWMQnEP4rg8_ZqeEwQmAridD8uRPUKby7NLi-4qpbL_0xydukkIQ6iFsLWlf5JMalToACe6zN-pvecS2uJLKggEDgKrSGb_CbsbEcEuRh9GUOOHyHZy9FGH6OweF40Wx6DFOVGdz1a3ZQqUn41GamgBkZK6quiEkd1B9djJQqC16nK_Rgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌جزئیات‌ عملکرد لئو مسی فوق‌ستاره تیم ملی آرژانتین در رقابت‌های 2 دوره اخیر جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/25547" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25546">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwtcM2alkdqF4w8iEgwVqmGzFX40p4s9wCYPtwTrmAbQ_rwl6Lp6r9HgFQKTnxjtCq8ysdtoBinGIpVScc5hVuG1T8sk0nNxTKo43j5SDVOFsVuILsArjgsCiTw0b_x7Sg5jMmQv6-swNHx0Dq66uSzzx44i8z0OHFYUbOyQc4UrDC7ck4ROibLCXOd17LNDUsaF_17gkqBUm363Q5UhEubEAYQ6R9RwKQHDHQHnwuLof8zQzqu6oohSrYlVx9w7niHO1kZicByVaHKdflTkmlPzCUWW8dl-b12kakzZqOP2sWxgunN7gjzBpoL9H8qOhAx2jYAI_nHKFwzvPQ9gdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اینفانتینو میخواد فشار بیاره تا جام جهانی ۲۰۳۰ با ۶۴ تیم برگزار شه. و ارژانتین و پاراگوئه و اروگوئه هم یک بازی به شکل افتخاری میزبان باشن. مشخص نیست فقط برای یک جام میخواد این کارو بکنه ولی ظاهرا عزم راسخی داره که این پروژه سنگین رو در سال ۲۰۳۰ انجام بده. جام‌جهانی ۲۰۳۰ با میزبانی سه کشور پرتغال اسپانیا و مراکش قراره برگزار شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/25546" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25545">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoF9aSQxWGGMzNcflZ8aZFCkGCPNAoGeN62I75wWpqbklQaw_725HP5GVHHjELuyL_Te276kHaqqURMUmqmdIifivj95WeickwwgADVnOyvo254r6LmXUbfr5QpQKx6_a_ys7VVfmCW651mhr1WPb8gJCOZ-jW65QNYCUac4ES47O8ltQnx0XWGvNxeeIYFEP12bofNSGtJD3cettSlP9x3Ck5rfipHANIwTtQQfGP1PQvACF5DC6ySo7bsSpRn-gdaUD9SMEJR40brW8Ki6IHQFLtaN7ke-fbR456xIdNFmTXP_HjcEnNnCH9z8lv9ubQ6szqwW05ITIPiZWLm7yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🆚
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
🆚
🇪🇸
🏅
تکرار فینال دوره قبل یا شگفتی در راه هست؟
🔥
🏆
اسپانیا و فرانسه از یک سمت و آرژانتین و انگلستان از سوی دیگری برای رسیدن به افتخار حضور در فینال جام جهانی ۲۰۲۶ با هم مبارزه میکنند.
👀
⚡️
آیا این بار هم یاران مسی و امباپه در فینال بهم میرسند یا مسیر فینال متفاوت خواهد بود؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/25545" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25544">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d86d8e16.mp4?token=FXbRifL0KOPWq5uHkEHy-8OFFDTpY4u0UPZZgmx3fCzcUYwGJ2WVT_zCsPtiRxF3to-_lAFlJupS80ak_XwBYakL010KJ-iq4OXN7Zwrn9_W74hmmLjJESruQETaGqt09s8q53qY_kUplG4QBstfP4hN49q_kqnrECrNv1SqIagBqDDyAmsehbTwWXePbgB6S-8oDQi4W9Qrs6nxbSL4VlFRy3-mSwS9TWSEhHBIhYtTSQSWGeDsUg7qqhClfmf4fXjhQwfjje6JB2fbbUU430NVSnYeGvP54wkNLcDWu_y4xoB2D_HrVijC6fOAWpQsha-KCUATyUO3uZCj0_ao0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d86d8e16.mp4?token=FXbRifL0KOPWq5uHkEHy-8OFFDTpY4u0UPZZgmx3fCzcUYwGJ2WVT_zCsPtiRxF3to-_lAFlJupS80ak_XwBYakL010KJ-iq4OXN7Zwrn9_W74hmmLjJESruQETaGqt09s8q53qY_kUplG4QBstfP4hN49q_kqnrECrNv1SqIagBqDDyAmsehbTwWXePbgB6S-8oDQi4W9Qrs6nxbSL4VlFRy3-mSwS9TWSEhHBIhYtTSQSWGeDsUg7qqhClfmf4fXjhQwfjje6JB2fbbUU430NVSnYeGvP54wkNLcDWu_y4xoB2D_HrVijC6fOAWpQsha-KCUATyUO3uZCj0_ao0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/25544" target="_blank">📅 21:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25543">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY2FGKQBNHpJtxLsMxLq5N_D5mc7yhgOCexPviESN0L5wZ7h568TXZPn5OefyXglZRtmBmPrQlOzFKdeWgvqHuBj80PkvuECVAVhXoxfucWq_uCRvxK4DVz6iHuEWBBZ1daJZfr-6OpXwfmNphgiljyLke0AQzBCgvR_4_TpbGIWCgkXorMy430eIj2eYyJnfdjwtq3j6MyRdvN75C2roHGfMhGjZPCq0t_gwC231tavb-jB-rnQO-kvND6u5TvZ19ZvHTMQs31UEK0Swi4tWbKcc75dKb_rmCdyPwaopX-CxG9OfKVo45JM7kxh4MrSikXdGIEil7rwC1UyNqpgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طوری‌که سورلوث در بازی با انگلیس؛ نروژی‌ هارو به فنا داد؛ وایکینگ فن‌ها عکس رو میفهمن. برگ‌های هالند از خودخواهی سورلوث ریخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25543" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25542">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlta18X9RDKHdT5ctvHdXHZJeYtW1mCawL4hLOjuDMo9LApgJ4k5gLa84SeBnniJ9I-lN8s_D9klpmH_va1ER2us0oGdGDhLOxNdD_0eISvqduxgftTuMRhZxRcUcbeMuVmM8wtDIlWLdyz_cHnZVCi3mEyxBKBXYKjd7lmPHY24eTy-sP0ivYXHe1e3UEz10Sysl9XjJ2puRxa9lRorR7WeI_LNKgH-asqqyYATz8B9HB7ccDDWc0vlTbB_65gqCc6pYayqLIt2UFtrHzrGJrq4WSZv-Q9GvbKhGdhDJWsDZT7pfaV2OPyGFmArX0WRQwxdZaj_JtA0ivg4CeeHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو انتقال مهم امروز؛
آرسنال 20 میلیون یورو گرفت‌و لئاندرو تروسارد روبه‌بشیکتاش‌داد و مارکوس لئوناردو ستاره الهلال هم رفت آژاکس؛ هلندی‌ها بابت این انتقال 17.5 میلیون یورو به الهلالی‌ها دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25542" target="_blank">📅 20:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25541">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/104d086276.mp4?token=ly2fNo0Nu14LS7CpiWKOsANaIqYiii5q4TpHWrNM1zz7ybj6CpT5olNy0oB9gqZIgIua_T-15oqY-p3HGKahzNXHOfdHXDKiZgeArr3ki1y2QDlT3T9ESQ6hgr3VyltrT94XkYmA653g8RG1rP4gPdtWnB48k19Ni8bsSSjpoJOt1UjFFmZuLBshImsYh6-oRFKxFavO7NarL7Vw12RrYj96EQznbn8Wl8gJis707ejCKdJ5Al01Tr4v1ouePQmhi1gNr1gybGikcErwlUkMLt6c2Pk-j-PYhomxwhBdVa0_m2KrSioT2z6Z0rxtqUdKq3N6sdLvLSfZBlbTp5CpbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/104d086276.mp4?token=ly2fNo0Nu14LS7CpiWKOsANaIqYiii5q4TpHWrNM1zz7ybj6CpT5olNy0oB9gqZIgIua_T-15oqY-p3HGKahzNXHOfdHXDKiZgeArr3ki1y2QDlT3T9ESQ6hgr3VyltrT94XkYmA653g8RG1rP4gPdtWnB48k19Ni8bsSSjpoJOt1UjFFmZuLBshImsYh6-oRFKxFavO7NarL7Vw12RrYj96EQznbn8Wl8gJis707ejCKdJ5Al01Tr4v1ouePQmhi1gNr1gybGikcErwlUkMLt6c2Pk-j-PYhomxwhBdVa0_m2KrSioT2z6Z0rxtqUdKq3N6sdLvLSfZBlbTp5CpbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنایه جواد خیابانی به قلعه نویی و کادرفنی تیم ملی به‌دلیل‌عملکرد ضعیف در جام جهانی: فکر کردی منم عین مربیای تیم‌ملی‌ام که 180 میلیارد بگیرم؟
‼️
هومن‌افاضلی‌خیلی‌جدی‌داره میگه فکر میکردیم که میتونیم تا فینال جام جهانی 2026 پیش بریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25541" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25539">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2qRFCsvvmoXcPcpaOteUXJB0Q86EKl_YlbmeYtyuzQJsWu97wxWzFRnE6KeclpDNEFzrJDMRUlU82eXvi7Jjc2jDSRp748RqKSLWz20jcDs61OQXEwO7hOcbAqZhdVwbXQ381Vu4FrjBFTLejA1OYrK7yceK7KKXdoD0Y7d7bpAUzHNBBzK2PHP3hCX0TA13FE9AUGobxhS4J6t7EnkhBTNi9zO1oUIqcBBXqEGxvENbQ-X2GLNcjYIrSuVguWwf3FTZV8IOSUIdmGMxRyZsHUIffIHIhHZG9apIkP8TogATGOK2eIS5zUqOaqacXDHAo_fXXVxlb7j1J1i6BmiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25539" target="_blank">📅 19:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25538">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmHK0Nv7Ar_sqCUtuG_HRUv3m15unE4eR_WEV5g7n0uIfnA-sDTKa6WHlNsx_h9i9q14YFS5UEExjZIBddGeE_Pl_j7QzIThpn5r7JRi3D1Lre-X2mhXc4x4yGjb2kIjA-C_QCIQ964k930p17jaD9MEbE2DjxwmuXqxROOsmJ0shmsAyjA0-alvQZJ07uV1gyXV2P0Ar6Vak4D6Ar6QciLHG4tJ9waVdzO9mZC7tHXnBTO00Uswo4JSLgVORZkc8RPLcol6CSqCyWdHBQogKlDQPSRjkGuqCQTzB6VNcPIvTXLq_YSmDuQI_4TpggPiH2CZcSNNWVScqttQlkV4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینی در سپاهان موندنی شد.</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25538" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25537">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT8lysGTSIcySF5T6-moibako0eIPYYtwpqzqet3cdYaa2vsy2jSXd1Qy2b1W6nu8e1RxEmjBLkM4z03OTKHhV5E0yjt5X9Tpvy_Pkd39VvueivwqYCAy23e_4DVSaQ9PFXBYMwBwoST2fGlJ_x02KTI4-Q3JKGtes8xJtEtC7c5612f7bALddACDLvs3Ei-UvKgYvylBbGG2QTmF1-pUo8OBzG4_VYe1Y0oJdCzph3giM43Nl2iWurdlFb3xrkC5gV_hzK3pG5F5j70UTfhFdj0hSSI94DD11ecL91xVcLAiZc-nL2LGD5DDf3dVtKV2ErkufsM-Xfd1ylirzMR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25537" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25536">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=ZMMhasOgeoD_YO1N1z2rd1jL9h6f9uN_Sb6JVb1iCotPO02_Tdw-brX5inC6iA5o2LbLYB75i1CjmvdZQ0t3xSse5-g1tiJ-Wi8kXpqV9MsQuwuOKaeXyZ0qlEfFCWcNvuMEvrZv-TleeS4d16hJROizPgEU_JLYp5A3OIVvOnzUeqr0q4PT-xsCVqFtyJSM27hGAl3K5IfS5v-fJy8CBNNsfl8yr6OuPOPCGXcr9ixIBOp5A5kErGk1Ku3ujZCrXp6EXQ3OLa4VdgvgVnS51ozhYFqYaWMG1W4vL4dBbWhYAChZ7IMhbDXFSMukr2ma8VZyH6-rrOywk2LK8CIojw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=ZMMhasOgeoD_YO1N1z2rd1jL9h6f9uN_Sb6JVb1iCotPO02_Tdw-brX5inC6iA5o2LbLYB75i1CjmvdZQ0t3xSse5-g1tiJ-Wi8kXpqV9MsQuwuOKaeXyZ0qlEfFCWcNvuMEvrZv-TleeS4d16hJROizPgEU_JLYp5A3OIVvOnzUeqr0q4PT-xsCVqFtyJSM27hGAl3K5IfS5v-fJy8CBNNsfl8yr6OuPOPCGXcr9ixIBOp5A5kErGk1Ku3ujZCrXp6EXQ3OLa4VdgvgVnS51ozhYFqYaWMG1W4vL4dBbWhYAChZ7IMhbDXFSMukr2ma8VZyH6-rrOywk2LK8CIojw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگهام ستاره انگلیس در پایان دیدار با نروژ:
مادرم یه هفته‌کامل بهم میگفت مراقب زبونت باش، نه فحش بده، نه به‌داور گیر بده که کارت زرد نگیری. آخرش هم مثل همیشه حرف مادرم اجرا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25536" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25534">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHVBM1Osdcs32c4gYd1_TwttiU6nhkWtAYJQXR2Tam3TbXnVrQpT7ulbaSuhewIEBYKtYShD4cmUX7HTjM2Gl-fZ0pSePrr-Uy_StuPWecrilG2FDR9AMEyMJ3r2V0Ix0KLehRFYZYt7N0Bxg1NgweRN7d_dECKbHA-sGC2ZuTwly0lkYNXcPLFmRI7tuso0nJ0L_Aj2uBVry2c6ELY107sJtMpq--Bx0dVpIXHCeG5gjYtCEydIPc-mOWokGdiorjzjwi8V0HzZtpqELgJZWYDS91rwnvAe4mMikQ-lKodgjn0DJWXrXOX3EwgUZxLiV1biAyAmqI5xUFDXgPc62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوسمار ویرا سرمربی‌سابق‌پرسپولیس در انتخابی عجیب با عقد قراردادی بعنوان سرمربی جدید به دوا یونایتدبنتن انتخاب‌شد. تیم‌یونایتد بنتن فصل گذشته درلیگ 18 تیمی اندونزی‌رتبه 7ام راکسب کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25534" target="_blank">📅 19:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25533">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iyi03NHvRJKZWB8-FK86aXpbipTzw2obiaQerUYCwKWF_PT4sw4072m0MDWEWT150XK31QLz2s7YeiOn4uys3_QllsWU2cGkFelUw0X3pz0QIxay0F9D5a3z5mPrSK4XGXyT5_Dv7scMrVRMiCKkXTyyQIdp50ks76EXkCYI9QwI4KF9R0O0mNXxpuOOb0R7Ws7bWlAc-2OeXcZq_NU6U6CBtBSC39zr6unzb5LhQ9hgUXGeYtKpR0hcLbMhfHtn_Xoz4O2t8zmqXlVNXnZ-s5_eIBxHaxNUnCYF-Tx-rzn_JRFPQNqma5u6vVvxR786VWPYzJrt3M1z77Gtxkf29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25533" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25531">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nm4dKF9netNceUd1VQonlbmfyjr-FE8titpYNJ3BPLMOQlHxh043OXgcEZNnso8szDnNS92X4NbQ3X-26w2JH69VQiLNIpgRfZSJxFAfjz07nyDMt9Q8kVe0lYZx99E2bs7zsW5k5D57F3iTX9r3WQb_EoozphQ3kO4Ar0kgjj3EdL4GuRyBxRzAz6wjKyuQWbYaMGt6zP8v-seUHRujnBJgSlgDfchR26QEB2MdAY84lu3YGEvLQZ0NP50jrAYKC2iBIqS2aV5DEFlYcRa1UjlJ0NkcoVw3q5cCVfiY2oYUkEkNl1lIbMmUKbQuBD8frCtpNXoTrkAY-aD_pmG19A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=sqrRDSudeuhmXjY9ZIvXPAGWlr_JAYczpXmhgMWgi0kehHwZVzQbUaQgCiORt8sBV_ll9cDjur0hPh4EGxxgbs7ium4msfBGwTZn29HUaL1eJyEIzcLeCSRtF92gB6EIOTh8uodaIpx60kjygbyNVYoS_KUqZ62auRn_WVUVlf-ywRoykoJeefxnosoQ7_nXLeoJRfSNtZPj3DIp0ImbaAB7rJySyScrzFxQ9XQ-f0INmcLxLmGbT-iaQ7MLS4WKoXT-FfKn6XTHoDoTxoBOOq1x8siwQ3Y4VtIMabob7fR6gh2EiOLaWrE8DS51Zi8yFwtcEtIeiJD6OCTCT1aPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=sqrRDSudeuhmXjY9ZIvXPAGWlr_JAYczpXmhgMWgi0kehHwZVzQbUaQgCiORt8sBV_ll9cDjur0hPh4EGxxgbs7ium4msfBGwTZn29HUaL1eJyEIzcLeCSRtF92gB6EIOTh8uodaIpx60kjygbyNVYoS_KUqZ62auRn_WVUVlf-ywRoykoJeefxnosoQ7_nXLeoJRfSNtZPj3DIp0ImbaAB7rJySyScrzFxQ9XQ-f0INmcLxLmGbT-iaQ7MLS4WKoXT-FfKn6XTHoDoTxoBOOq1x8siwQ3Y4VtIMabob7fR6gh2EiOLaWrE8DS51Zi8yFwtcEtIeiJD6OCTCT1aPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25531" target="_blank">📅 18:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25530">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=hPI_WlGBzTMfenE3WlvKk7t5uhx36V6cbp3bsptMxcdfyxQ7LTErys2cqS3kX7ziZ3uiVeHCjZ9wE0fJFP7D21tc4fM7QFPAeEx0DVhQQo9wa3M4IWSCaPZZwR8tZDPTgCI3Zw4e465popJV75ljgbup83MhR6a1CrwwUR45iNUuosD6IrDCG6MdVctTXmpLkbX7YqXqW72CfRBh99eh5Pi3-AEgnCnWrT6Pcvqkq5pOdXja97JWtv8crErZAfaYO-B-gLgJYvwHWPEYr8SqLnHEIzfXz5AU20lDwF5MTxVUdKUjTtie-ynqAaBv7mGfx8W7HRG0wKfP-PVY6T6F-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=hPI_WlGBzTMfenE3WlvKk7t5uhx36V6cbp3bsptMxcdfyxQ7LTErys2cqS3kX7ziZ3uiVeHCjZ9wE0fJFP7D21tc4fM7QFPAeEx0DVhQQo9wa3M4IWSCaPZZwR8tZDPTgCI3Zw4e465popJV75ljgbup83MhR6a1CrwwUR45iNUuosD6IrDCG6MdVctTXmpLkbX7YqXqW72CfRBh99eh5Pi3-AEgnCnWrT6Pcvqkq5pOdXja97JWtv8crErZAfaYO-B-gLgJYvwHWPEYr8SqLnHEIzfXz5AU20lDwF5MTxVUdKUjTtie-ynqAaBv7mGfx8W7HRG0wKfP-PVY6T6F-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسی تو نیمه اول با پینیرو داور پرتغالی بحثش شد دیشب: بامن‌درست‌صحبت‌کن، بی احترامی نکن. من باتومحترمانه‌صحبت‌میکنم تو هم باید همینکارو بکنی. انگار نمیدونی‌چجوری باید بابقیه حرف بزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25530" target="_blank">📅 18:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25529">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=veDBNYREE4DsNiJOydpLDOKpA1gFin5_xf02-aZZxFyNFE4psfINy7hIyb2mZ6SX9dCHajb0VOMgdL0I__ObMa280VccR4o7lye8lnvCdONlQDPQUAqzTePKbwYI6vCBZYdnzRpaiH-JKxBwsOTwabT0UXr5W0qcjk4ntqOA2uQig_4RDS4IoakZYCFtPwQ4zY8t61kfL940I1uKbXXUBHckBiRF4bXI1DvP9K8eZnSzMczeQ8jtg7klm2qiuxmjbJ7OKh3za-jGIhr1Lx4JUC7xYi_D_rxs4CFvFYhcBRkKNzjs3Lh64r6IQBJwGj4T7N9NWGk5Nnc3Uyu2qPc1CjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=veDBNYREE4DsNiJOydpLDOKpA1gFin5_xf02-aZZxFyNFE4psfINy7hIyb2mZ6SX9dCHajb0VOMgdL0I__ObMa280VccR4o7lye8lnvCdONlQDPQUAqzTePKbwYI6vCBZYdnzRpaiH-JKxBwsOTwabT0UXr5W0qcjk4ntqOA2uQig_4RDS4IoakZYCFtPwQ4zY8t61kfL940I1uKbXXUBHckBiRF4bXI1DvP9K8eZnSzMczeQ8jtg7klm2qiuxmjbJ7OKh3za-jGIhr1Lx4JUC7xYi_D_rxs4CFvFYhcBRkKNzjs3Lh64r6IQBJwGj4T7N9NWGk5Nnc3Uyu2qPc1CjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیوزیبا از لحظاتی فان و با مزه لامین یامال و داداش کوچیکش که این روزها سوژه رسانه‌‌ها شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25529" target="_blank">📅 18:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25528">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPoD2Tq8mNs9nAZlbr9UNWNJAIqSGuJXrWTNk_Zu18Yhu9YMaOdbnH7kNkqW7c2k024jKqT_KJRBRTVF3LDYNrmKzcEfARX3xd1mzeNHH6WEtWf2cJ9NoaS_soFIEe0rdVk1075AWxs9DmlWYqTA9FuaUmB_soqFKXjZrMWY6e5Bf_dtLGp4Izbqecfqzyf6fvDKViUQ_SeccpHYYfK1bpc5i5o4-X3YMG6L1gPt2maibCea4irKVmIkTm27npgkp0naeN_gZdQryEjkWj7DOWYXNA6ufarMhXZK1pa-WiAccIJJC_aMgxhPwanDg-xTA52x4ifXtm4wn_nIkJfKaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخباردریافتی‌ پرشیانا از اصفهان؛
مدیریت‌ تیم سپاهان‌ با‌ حسین ابرقویی مدافع میانی 29 ساله باشگاه پرسپولیس مذاکرات مثبتی داشته و درصورتیکه حسین‌ابرقویی بتونه رضایت‌نامه اش رو از سرخپوشان بگیره راهی اصفهان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25528" target="_blank">📅 18:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25527">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
تو یکی‌از خانوادهای‌عشایری یه دختر بچه حالش بد میشه، بعدمیبرنش‌بیمارستان تست میگیرن میبینن باردار شده؛ میپرسن کار کیه!؟ میگه پسرعموم، دعوا میشه بین خانوادهاشون؛ برادر دختره که بازم زیر سن قانونی بوده میزنه پسر عموش‌رو میکشه، میبرنشون دادگاه خانواده عموش…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25527" target="_blank">📅 17:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25526">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZQumKjx26UpqqAOTYbfEpRrljlXPfesSi_6u0FN8efem4n7tiWGVTsyjb_64pb7tmzvxvSFbTEVgslZpd7OQ4nHes-Ji-_H2nilTVFLHrLsA8p-ZPXlWcnWTgoryQH9RJ2Z_KsKSGxng2RyJ2xm1MFdbHaP2UBBB_3Rp_XTqdBk1ev7rgIEru-a7gKXbp3ApAyxeIPCDF8KoSj2ciQGJUh6mILmEHCuxBvMDJ9ja-nvJpfckG4FJ3kyvja-K9zmBn-hsd1FeLBvo8sLruBiXinz3VNToOsQZ-dI-cKIvtNSwUjqhUARaON13ob0NLGhNG_0tNIJT928USBKTh1cCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تقویم
؛ پنج‌سال‌پیش درچنین‌روزایی؛
مدیریت باشگاه استقلال تهران هفته‌ای یک الی دو بار از سجاد شهباززاده مهاجم جدید خود رونمایی میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25526" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25525">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mouA8xBHBUBunqQBXlWnWaXjekl5qieQbRa_2YkMWZmyWjUnEE2G6F5pgHUOFkZwXfbZbw3z4A5HHWVhbVHkpDXlG6ZIfJO29Iz4GFTOPIh1dA5Gnnu-rOj_7tdbU37yQ0JcXApWGPYC1L00lVWhUUL0rgUZrSFWagMLwDe8Gmw78o4vtaIYbrWsCZndUHOUY8W4dfyVRmLjad_Vx85yr1lMfrMPPZFfWq1VLwSJjVO78Ewm74OgpHq7F7cge3XipfWqW4fmmjN4SrXdC_ndMHhbzpBFK0xnm1wDZQfHsjz9Pj0FWeIiByRDRU4LmMKaociKXExzxgcaVTyNCUzTGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25525" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25524">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqOZU71ORilO7d2VasL5btJ1pauFafUYnvUQLJk2Q12KtmD7MF4T96qs-3JeiYMPTFLIqY3o-eZT3q3orEZLcZO0Y0860fAS5-jialIX5gRaXfstRDmFv3IhcePuA28Il20aIbIX_OkDfl7yh-oNGs7mmMT9oY2FwucBXWhLfVQSuyu75vOVut265YTcEA9Dg3AYsW4UETmaQV4YmFiuph7RTmTib5eAjU2i5GF3jDO_E7JiAgv1cHSiX0VFHtSbpGEHYtPhYWMzn_eFIFHCZorYyJzfa24FeW6wkqfj-8dtdZyvNOWZKs7U6MPUqchr-N4O4stu6InLcDkLag8Rsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
عارف حاجی‌عیدی هافبک‌جنگنده سپاهان که مدنطر مهدی‌تارتار و پرسپولیس بود بامخالفت شدید محرم نوید کیا در جمع طلایی پوشان ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25524" target="_blank">📅 17:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25523">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=D0a5folWIUZNOM5ZUgJwBUcrvEfUQo-3k2Kh2kStte3n895AhmUMD31TKKZUcrNJOZ5Unym16ClJN_aaJXaQXC6cqI7mV8Rm22PIhgIq9Efaz-kHGPs0EbRooDvPn6hWHtOmZLHK7y0s8h4eXDWKr5OAkFhBqKoZ6n5hasoCUR1iruk7evwOH6cEpkEigg2AJRVQrjDY2oYDsw1L_-iKO2bFM6H67WjzNzH2KZj_MzRhYV-_xyERmz4oELjJtNWPcH2kk5rmCrt8IERkFl0ZYuYrfl78QyatNu6Jld4cNHd3vuecppiuT5Zu3ZRLAg3sIw385YVkLsIC3m28X_4sZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=D0a5folWIUZNOM5ZUgJwBUcrvEfUQo-3k2Kh2kStte3n895AhmUMD31TKKZUcrNJOZ5Unym16ClJN_aaJXaQXC6cqI7mV8Rm22PIhgIq9Efaz-kHGPs0EbRooDvPn6hWHtOmZLHK7y0s8h4eXDWKr5OAkFhBqKoZ6n5hasoCUR1iruk7evwOH6cEpkEigg2AJRVQrjDY2oYDsw1L_-iKO2bFM6H67WjzNzH2KZj_MzRhYV-_xyERmz4oELjJtNWPcH2kk5rmCrt8IERkFl0ZYuYrfl78QyatNu6Jld4cNHd3vuecppiuT5Zu3ZRLAg3sIw385YVkLsIC3m28X_4sZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هومن‌افاضلی‌از کادرفنی تیم قلعه‌نویی:
شجاع پاهاش پرانتز برعکسه اگه پرانتزی بود پاهاش اون گل‌هم افساید نمیشد ما میرفتیم مرحله بعد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25523" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25522">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=eDHAZTxkO_uNocpW57pD5RI15tRILU38gUI4SEwH-HMOsneiNevUsiWLwMGM6Pd3U4oNHCnjG6fYmq0UtwT00utwJj8CppWowB6T3_uR61hXt0z6mYN67hUgfdVCziLIscZUPOqMJpGPEioJAaja9x_4Ivm88Qg5Eg_0LbpY_DCOrEl49vhLY77wz3hTBjeN9Suk0_NxvsE5e_ikqTXp2uAvIqsPfVIzYOioCVN_dwp6ht7luIOxb3qJveYarogeZZMYJ-ozuMUjTB_1VG8ocNbO5MsgzGG6fy_mKrWJYYZr-O7Fb0N6QOoPfiX3Ri6cUHvjljHQ_T1ghcTuyWDQlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=eDHAZTxkO_uNocpW57pD5RI15tRILU38gUI4SEwH-HMOsneiNevUsiWLwMGM6Pd3U4oNHCnjG6fYmq0UtwT00utwJj8CppWowB6T3_uR61hXt0z6mYN67hUgfdVCziLIscZUPOqMJpGPEioJAaja9x_4Ivm88Qg5Eg_0LbpY_DCOrEl49vhLY77wz3hTBjeN9Suk0_NxvsE5e_ikqTXp2uAvIqsPfVIzYOioCVN_dwp6ht7luIOxb3qJveYarogeZZMYJ-ozuMUjTB_1VG8ocNbO5MsgzGG6fy_mKrWJYYZr-O7Fb0N6QOoPfiX3Ri6cUHvjljHQ_T1ghcTuyWDQlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل فردوسی پور
: آقای اژدهایی، خبرنگار صداوسیما وقتی‌صدتا موشک‌خوردیم و صدنفر آدم کشته شده ‌میاد میگه که همه چیز عادی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25522" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25521">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4009214e91.mp4?token=BEV1127EWPyWvrmNJIKjbKxGDt7T_ezFHBoiCkGY2xQB44-cdEgOQkfxcVf1SWKuajw8MeBDYei6x7RN-CcbwTBwz0DMrItJCCahTZdgymZ6JJv7-KCe0aLZefOxffcB3z-EUQvUPyBZssBlFdpBORxWq45PSYWTCgdJq4yh7-87qVATyBeJawmW0UWkfKDXzMt-X8MbPScZC7sH9rvaBpXVYYMCsynxYm9KSRvsaE3d2llBcA5Y19dimDq7o9cLgqh03RJAQIQhfW9jMB5GK19FwOrIKVqmcsRE023bBqXaAIZScHzZckORLC00KopGGjExWgfFXbNcxD8wY5WJ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4009214e91.mp4?token=BEV1127EWPyWvrmNJIKjbKxGDt7T_ezFHBoiCkGY2xQB44-cdEgOQkfxcVf1SWKuajw8MeBDYei6x7RN-CcbwTBwz0DMrItJCCahTZdgymZ6JJv7-KCe0aLZefOxffcB3z-EUQvUPyBZssBlFdpBORxWq45PSYWTCgdJq4yh7-87qVATyBeJawmW0UWkfKDXzMt-X8MbPScZC7sH9rvaBpXVYYMCsynxYm9KSRvsaE3d2llBcA5Y19dimDq7o9cLgqh03RJAQIQhfW9jMB5GK19FwOrIKVqmcsRE023bBqXaAIZScHzZckORLC00KopGGjExWgfFXbNcxD8wY5WJ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازی های جذاااب
جام جهانی فوتبال
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای‌مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای‌ورود بسایت‌فیلترشکن خود را خاموش کنید!
▶️
‌
Link
🔜
MelBet1.net
▶️
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25521" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25520">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=lKJb74_Jvypxatz6LpuM0n8K8aqdTDPCv8f-yAt-S6X01FEJq-b8Da2Ygjpcwwlp3SC_PcXuU_wr5PuXpRssVqp1wfSIwed7fE94ybU4UJUDSmWmyzJMWVW2QITZaCTO2QmWF_kQUwQ6olxxaqkLdZ6GteOmXgAI-R0BQN_BTofqmaAQ6GvHgFfQE84DD8B8iC-HWWX_vhRqMJU1X6cTQ3iCH5ccPbdR8ehHWxz5bwOUPLsDzhwwYPWSDz0Dos2Oc7erlnFzaGdrkFQ8M4-sfQ4SkuhiEF_x5NDgQ7jtVcyNucHIXOAULMUgQYSQ1Cj6WzvTu0sv2AgyufZc3vW1kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=lKJb74_Jvypxatz6LpuM0n8K8aqdTDPCv8f-yAt-S6X01FEJq-b8Da2Ygjpcwwlp3SC_PcXuU_wr5PuXpRssVqp1wfSIwed7fE94ybU4UJUDSmWmyzJMWVW2QITZaCTO2QmWF_kQUwQ6olxxaqkLdZ6GteOmXgAI-R0BQN_BTofqmaAQ6GvHgFfQE84DD8B8iC-HWWX_vhRqMJU1X6cTQ3iCH5ccPbdR8ehHWxz5bwOUPLsDzhwwYPWSDz0Dos2Oc7erlnFzaGdrkFQ8M4-sfQ4SkuhiEF_x5NDgQ7jtVcyNucHIXOAULMUgQYSQ1Cj6WzvTu0sv2AgyufZc3vW1kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شوخی‌جودبلینگهام‌ و ارلینگ‌هالند در حاشیه دیدار شب گذشته انگلیس
🆚
نروژ در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25520" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25519">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIju2VvZwC17cvRQiN5LccGqo2XO8LNBFOfQTfzDJ6evqqWflLOOapQnBusKXPpIhcHDYbt2w7P-LO024zKiYyXXLtZItDN9iCqBHVArwe_IZvDejyD8uIQxuwxNBhKrvqwjj-68slifVl3Uxy7x0dPlVzqcNrKhtvRamfRBu317uvssvEfw4IKeKZ0G5UNCfPwoU7iF04g6rBM6ZK2TvPL3FyIaj6Gg-opISIl9Kv07fIfZAA3IfDT1zzrpt4qqkYyCZjSdPmF3qZLxuyyxj6WCkmLVIyPa_dFaAe5ie84fvvP1ID_7BQkq99lDOJNXd13NGIKzuCuCes74xeGGcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25519" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25518">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVzxH_F6b7aQ4Xf6cbXlbYUwukUWCxSQPpYMUPHknGDU96rFOwYuVBgA0G3zX-3Lzm6GD9RP0ZAD1kBHkTo7CHwfenW8pa_6b4J2OMJjk-4_qE6kOfK0bdbwotPCa2pquja450XIycZUAmN0bdP2vClfbLrLwNooH0YfubzkESz7bI9Mia6S9lCa2TTMM9RLI79Pj723l76IuRFUKkgzHwOr7b_BwGzZyNo_5jhFFieTiQbHJcE8eMaIoeznVz7WBhZCU_T8hoNbVCirypN-_Hu-NrMLZgRlGITqwur4bTyJ0ULluNxKyqDA23bKmZpVCyKSOTCHWHWXYuAjR5Be-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دو تقابل جذاب بامداد امروز مرحله یک‌چهارم‌نهایی رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25518" target="_blank">📅 15:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25517">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR-Ya7jPtEVUDY_6o7KAptaCbjNhVifM2rkX__-HBGjI_sk2sAzjZxBapvG9_lKJdQYfaSaThkEh1_5RXInbifakPw10nx-yYCSCuEcBnQIX4phN5a61f-Yq2pCjQbJN6KsKGaoY8gvUW7k7aWteJkNhcgOr-LcpYRu8q8AecHr0ePN7w5Deu0W0lp8xNh0SBm3pzgCBnKDlx46E5DMhplmOnYuxaNWbwTZQ6VPyXPY8HFVHMDG2FmdSS_Z-zjSe58KYUuhx5cLdHDH39PauFpUZbDOH3dOPfanJOvEcTnkQ4SDSWBot8XDVwj9vhc-iayeD5HlwOJ1HrJgHFOXnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25517" target="_blank">📅 15:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25515">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25515" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25514">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iemHWhmlEULcP0mSzqxSpkO8MmhGRgeDhlDtpTd9nUC33BbJqy6dbl__2uM3mSrjvJDinoxjEHFeQu0xMfHN6R78QUCUGM6uPN7ow3rAE9O0Z4P3NBvw4zoP5Cgby-rrTPB17qvg5nn0-i6wDNd7QgGu-3Kj0jyTvBCTVnrr49eemkj_oyPun_GnHeD53XTeZjfPQHVOz-a8bgTyKI681jxU0IO5GPDCgFM4oVDiO8OwFgRZhpixEEsAUjA5e49CXJBKD1b-7O_NU41ACJyrXbmckRP4iGiBIAo57Iw-7wfY_ObI5AJ2P9zD9hrEIusPBon5EX3Xhb-SPtJ2Rgn_QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا
#فوری
؛
یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25514" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25513">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N77ueMFsKqAbdy-beDAmjPktSWskh5WqRu5OF7mIXwXUDLKADkeqqeJEEQuG_AQ9icdkaq2e4vgiH47nXx_qitDxglguZ0yrz0ytpRNmGxH4z2omtQ215-Bz7cNnSCq5_3WFF1SSHRQ8ttRksNnnHcdsXbDL7pJdNHsu45TNgRcdO2uIj-0pQzlqUFuqn13fl_hHufcn0iY_WKUYPyLDd8yojH3lMox0Za8uOR997wd6ixN2FCfnwv79PvejEX7PaF4RhUQkzmXQEPrHF_ZMUULRN6r4rH2AGaujOwudMtiTkRKjsj_2-G46258IqiHxauT1JB2JUTUdezhDG6sBuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25513" target="_blank">📅 14:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25512">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=dnBOrEarq4xtchSSRrGDOt4cvdP32YCXG7UDaNrbUP6aBVIhzZongbEHWsjR5CczxZXsjEa-b5VgZCx9UxfGtsDeyJ9z_ShFiK8k9TmOSRnKIz54L30Z35BOAvVEuQUptNnwCD_LDHyBIk_fw_olcHTViZ0EifpkD8c0hVcmzBFuomn35O7BMx741WIRXxApDV7QVtcc6LDfR6XM-otqBKZ9gie6fUOc48lFXacCDLwZLf6mHpIRWFgKOjCYBUpkc8VQH-kVvf2zwHgqTKQ4zUnjn-P3aoQHRwzzeSJfmU9otDrS4TnABs4qj6m8M-yjQ2vAkB_TaTtQrIQFqMq-rZZ4nYibmBVJ-WWBxtNwFkVudFsxP2qoPuXoR8DtLrse9NHE7RAsM7DT1e2k3Y35EQ1_UFT8hYUCRoaO3WL96Y0YMZYN-8rhiULVLku1sMv9qYU3WRQD3DU0r099Q3ya5vDvUUxBynz4yfU2bToJFH50SAXWfxh1E3Fq7Q0p-ZoAqRofHRJIG-e55ocyhKKdUOPrKecnEeBl_opid9nKlU5eftx7xQ-T40VRUGEy8N30uOGKqjoA0h2dYWSe7ae8cpw0rjllGKcpOex07jZZQwWB2ZJ9jo1g_FIwIC668HIe-JidFsw7tybnqYOPwzvRmiBiRbH5VkbnlHcSKjVw0Yc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=dnBOrEarq4xtchSSRrGDOt4cvdP32YCXG7UDaNrbUP6aBVIhzZongbEHWsjR5CczxZXsjEa-b5VgZCx9UxfGtsDeyJ9z_ShFiK8k9TmOSRnKIz54L30Z35BOAvVEuQUptNnwCD_LDHyBIk_fw_olcHTViZ0EifpkD8c0hVcmzBFuomn35O7BMx741WIRXxApDV7QVtcc6LDfR6XM-otqBKZ9gie6fUOc48lFXacCDLwZLf6mHpIRWFgKOjCYBUpkc8VQH-kVvf2zwHgqTKQ4zUnjn-P3aoQHRwzzeSJfmU9otDrS4TnABs4qj6m8M-yjQ2vAkB_TaTtQrIQFqMq-rZZ4nYibmBVJ-WWBxtNwFkVudFsxP2qoPuXoR8DtLrse9NHE7RAsM7DT1e2k3Y35EQ1_UFT8hYUCRoaO3WL96Y0YMZYN-8rhiULVLku1sMv9qYU3WRQD3DU0r099Q3ya5vDvUUxBynz4yfU2bToJFH50SAXWfxh1E3Fq7Q0p-ZoAqRofHRJIG-e55ocyhKKdUOPrKecnEeBl_opid9nKlU5eftx7xQ-T40VRUGEy8N30uOGKqjoA0h2dYWSe7ae8cpw0rjllGKcpOex07jZZQwWB2ZJ9jo1g_FIwIC668HIe-JidFsw7tybnqYOPwzvRmiBiRbH5VkbnlHcSKjVw0Yc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اگه ایران میزبان رقابت های جام جهانی 2026 بود؛ این مسابقات جذاب چطوری برگزار میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25512" target="_blank">📅 14:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25511">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/by1JV7hc4cVvBTKlZzrkX45e6VNztXs7Vuf_A39VnbcDHBl31Rfk7gk4FTGpmEb8St_R2AiDxbI9enE3aSMNn6FoP1o8vIOSQJRZkLazeZdMokkj-dPGwQ_e3ec0yg8AY3nhleet1OmOh5_XdGqVZyJfpcKxzabubLZBL6Iu64CUt827Ml63ToslKT_7WQzcOduPwIO1MCjdZW-V0Zc9-ouw_2MIbl1kICuefLyEgmnEHYrxJLOVntxGQfxNoxGd3qaBDHk0bRljSKjiz6vbiMeRTjSmuviCTgZyS71twf6c_j5zj-QDU2rTKvLvM0VLJMtuI9L6QZ1WsqqYtlRACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25511" target="_blank">📅 13:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25510">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic3HinZIS0GqnDQyaQ9F4nyIW2AlHo7IK8nGVyfoNCHoB2duuvzFGPYHMpZCPIXdcwlLyTZZF5tRzp4U2qHN14JCn2qxG3m0vc_AIPjDcXxioOKwRVUm4onrOP7wPSbKE8HcmCt8N0e3629z8dKTLEg_ZUZTOiUzZ2PVbyn-BvKmoUUcgqOZBnuA-H1zML45YyKRqOkP6iFa-aAJ9xQ6sjV0z1fKURahTPysoJEgqT-LcirNxgk1nSlroXZTfxJTigvc2zsBcqA_WtncZjJkHRn_IEcL5jZdPzQy7XvHXbbY4jP-h12_bA-7-QPNnR9yinJym4vm2GvSPTIT8ffsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25510" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25509">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqbU-IHSJn9ENr-j-QXx6duAx31ritP-uGt8GCCkIzsWocg43eZTUiE9SzzVc7dkQUMSBErZXtkjdAcYlHE1Wk_4fihDpNsNNwi7w1SErnZqAqr3EC91KxOlXIsAAkZWPFDXCSbMJDfsBCPaxVYtNR1g4KdtKBgN-xTdr9bHv8tjJCgtPK0ZwWoCjXMJhKTG-3Frk3OijOtIBXEWXwJrNs3syTRKQjqtxhCwexcGWmvQnJR3PptMm11chBwEcZXAsiAshM45-TvAHfR4J6pBQnH7xQmTYsSwXXiyY_EmYe7vSygqS6dy0wxL2uMGH9QVCP_GNvNuWrxlaeGW_IRBag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25509" target="_blank">📅 13:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25508">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwcx1VZ6lPnpyNdTwacZE0tUTpn5_YDvbopwjlPYrxQWSPqsNcgnL_MHkDjqQZaI9tbCDTmsYmYRPOdX_m7eaVj5vPb1irW4bDzJTYzEin56T8I-ehyPEDhtBANNrbR5BfAbMKxCUd7e19EK5V_JpSavE0Kuval869A-xp9Roq4zuKooFyuwfbM0yuY4FX4wA3cRo6rk4ymhc7aAt96HNqllyPzVCkG03sFF_rhM_rs0vCas0Z07p7_R4w6VF5UBXiIlg2H9ukUC4wDbjwCAzK0YdXPytr_WuMiWxiIf2N7mH2-rl52v7xTs3E3tBAMdRQHKHstWM4Bs76v4_iMyeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25508" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25507">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVpiGEbMWZ5uNpjw2Oh2EWVRiOxIn0HnB9y_bDq0mZYWDDNQ4nDzjbjThbiGg1iEaDlGK1dP8FPVCAPL3ksbN5VQt1tw3wIkyfn_e3mpHi5yvPwJ70_7KlCRy58C7plIWmPdlC1RKAtYCU-KdnDYg0vKaWW2OAQmJIMJpANsP-eUYTVNiu9IvQ37uQS8rHCUP2hbHyiLwq_XNh4I-L5QvFS3uG1VFM1XjH-0qwGvgH2DWHObbsM2vDsd8zhGKDxxqiKE-euer2io3B_RE-Vj-gQ7TT92SVnDlhIlYOUadg9wHvztkepVhTq1sIhfv5oBGOc-zPLdYQ0C4MIbK-6KWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عادل خان فردوسی‌پور پیرو خبر دو روز پیش پرشیانا؛ مهدی ترابی برای عقد قراردادی دو ساله با مدیریت باشگاه پرسپولیس به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25507" target="_blank">📅 12:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25506">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6pirnEhanEAfdU1fFgMrlDSrHTWqVc9_8CX53tnuyVivvqxBNwVT59aRqjAxaQ3z1nNDHZv_q6gqS4DHE4E925jLKZv2EPdYWXGjaXa9z16Ekk2bviYc67MKKkEMaWlzEyCqPqR7yGjShx_Ca-t1Aeudy5vkljMhhjnGsAA2hw-6c9yExYQIIa91AJT9AJHwyvklPzk1N6K-0c6UmIGICYbC1QXlooidCx8602rrpoO7LAl5xwUzdZ82EHmh16xv-Dd2mHY3Ga778z-k7BacvvDz3ACqSdyFVFiuEkAdRxjPdfaz4JDU0Qbwe7tIdZQux4cqg7svitn8QYZ8vWS7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا
#فوری
؛
سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25506" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25505">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=QYfInW3Q9Jdlg96DWfBvEQIKz81r5b2ZklFalj0seXv5v1f_DuaQhS9W-rMMSfW6etEhoVjIpS9KeiJBBKUeJ3pKy5MROXdFtKpVmT9x9Pf_DNjWOgZROEVZeea82vSdez7bIXlcoyPyEObhxet43n1D76cIqo1CF0NetMH9rktppMdB2pHgvX5378bwnFHC0ZBNGTnn2bzYz8lnwymW13xgjkyqrTKPRul6XWKK6zNohPUQeKTO4DQI5t6ZlV2cbdLDXv5xfSNjhzQJ7MXQRuhnjKxqG0scCrXk898XrRGRW51-yRvkOjg58ijC39CldTggAru7P4woDzGqnkPStQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=QYfInW3Q9Jdlg96DWfBvEQIKz81r5b2ZklFalj0seXv5v1f_DuaQhS9W-rMMSfW6etEhoVjIpS9KeiJBBKUeJ3pKy5MROXdFtKpVmT9x9Pf_DNjWOgZROEVZeea82vSdez7bIXlcoyPyEObhxet43n1D76cIqo1CF0NetMH9rktppMdB2pHgvX5378bwnFHC0ZBNGTnn2bzYz8lnwymW13xgjkyqrTKPRul6XWKK6zNohPUQeKTO4DQI5t6ZlV2cbdLDXv5xfSNjhzQJ7MXQRuhnjKxqG0scCrXk898XrRGRW51-yRvkOjg58ijC39CldTggAru7P4woDzGqnkPStQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25505" target="_blank">📅 11:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25504">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9AoUNgyPbHta8ZC_xcqlt88IPfbBuyrhNK__zwvCsrWcAeDMVWiUOLJ9Js-2tPqu6Rgt0VRlgbI4PFIlDiw8pTmSDHcCEvIJKwoC3DuT40VgzjGaFkMfodZRSJK8wzdi32JLqo6-P1kdlm8Hzd4IaMakhw95RulKWB-la-IcHyGG0cAV8Ac_K-t9ShuArOWLk24tlTHvoY1Ba4e7VQw7dwd2H8PoNR_xtiE3Ujd1irPFJ87MjxM3RCPlM7aAO2Zx9hEHxrHWbajYT1pBzqdEcF16W0-2pYcaDPEU7EJhB7hEtbWGx_ixMjWqwlVUsaX_SNo8ueE73U3lZChyJuqGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25504" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25503">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLVRNglVgnX58Elxo61AqAiQT3v-VAqy0okH1COtHZYNzhcgCST9CK5RbxtbBqmnJacKCRWMS3MBWkQbq-klH8rAUgQnVHGqS4ece6Ov9FhmAlRnziTh_lOYtFqJOnHXQx_-QAGj0RMbePIZumG8hoemkFDrSVpU44hW4QKp171tCOBMrF3FlOCrgVIyLCNfg2tSAEY0FhLXLwuiPBR4r0XCPFtRECOrXc7r2qIOJVrXRV5OZIr5JnBm8qQI0ElbOmHF205Bh7HNzy1GRCcqg8FUFT3naYISkh5NBBUIy-KIY-KttcNFFQUwBjvisCSlSLRmFZjZj5xvOXiNDB28Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25503" target="_blank">📅 11:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=afv49PxoLdmi3MkJmjOZ-lJo3jcpRWKPmmUXKY9Ns5HhQzUSFld8bA-VeqWfY0Vb9pobwqz-zL58aHWXJB8BBy-QdbBE9d2FmoLrit5H3F9tZYpPo7FFPKU51QhPnh5_B6cv4wnyzKf4FgJgvnPy9HRA67z4NgDt6C-nqwwRwPB2BFqYyqqvSUxLJj8eh-nhGPGmS0kZuqe6r4mc6YoDR-lkPtLII7oTErHNB4kBBVIZQc-0r6wghrXUsL_6V9MYI7ukJRG4Dm_a1M-vgK-oJgVdQfNC_xmVJqL0A-6yk0huo1EAWWOovDree8q_cB_Dx6YNIYv3KdtTmBSUP3eDtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=afv49PxoLdmi3MkJmjOZ-lJo3jcpRWKPmmUXKY9Ns5HhQzUSFld8bA-VeqWfY0Vb9pobwqz-zL58aHWXJB8BBy-QdbBE9d2FmoLrit5H3F9tZYpPo7FFPKU51QhPnh5_B6cv4wnyzKf4FgJgvnPy9HRA67z4NgDt6C-nqwwRwPB2BFqYyqqvSUxLJj8eh-nhGPGmS0kZuqe6r4mc6YoDR-lkPtLII7oTErHNB4kBBVIZQc-0r6wghrXUsL_6V9MYI7ukJRG4Dm_a1M-vgK-oJgVdQfNC_xmVJqL0A-6yk0huo1EAWWOovDree8q_cB_Dx6YNIYv3KdtTmBSUP3eDtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
نروژفراموش‌نشدنی‌ترین‌تیم‌جام‌جهانی۲۰۲۶ بود. جسارت‌وجنگندگی‌کم‌نظیری‌داشتن و شدیدا دل‌همه فوتبال‌ دوستان رو بردن. به قول یه بنده‌ خدایی اگه ایتالیا مدل گتوزو تو اون گروه اول میشد جای اینا میومد احتمالا این مراحل رو به چشم نمیدید. من خودم بشدت فن ایتالیام ولی خب مدل اسپالتی و گتوزو افتضاح بود ولی مانچینی درستش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25502" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQR6dnmAaCfRFyJNHhlYTACmV8tbJOepncFCTwayYTctuVXbTd0lsYqZPw2mhNDzEPXmYc10BqZTgHfQLmBWq9zdSROoLgt5H8W-Nk6a4NwOrNpaGALxoR-anYRNBLhoNdOxEFeLgk8RKUCkU6yd3bY5_bS5uggWVZ3ejs_4-CKnfuS8ljOFOP0Kw-KBwyj23M2dz3YldYPH63I-EXHinhIGGKYECTiVpxtSiKr6Bz0zB8nJMiHIPULgmmjnXMD0XELIp7p5nmZi9VoyhVcqVcE-6I2NIpnbL1GLxrH5spJ9Ml4OleMM8K_WnnK-I-ixmAOlWsx9jbObxy_i2z4IVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=N3JHCMY8AYMOFPFoHBW2myiSVL_7y6s0fGaJFrNotexNQMr2BSRyAkUWGPRimtXNvXiIPoGLkuOc0tb1Ch2uMer5IuhC7Ppsqb014DYws-P5s9Auhtj2WYv2yLUo4OtjBq5UTQGvj_TULvmid4ymyJC4lnv7oILOE_Xn5hIT17Lm9aTSosiE2iBxkeyp5iA0B4ZZs93ueiVrYTyAcgZX3Vz-B4r-Xo6u-zCS-spiboY-1jZwmTXnF5KpgjqOwSzI05OU9oet1PXWycKo4yUpPDlwmfiQqranfT2N-M0BzwFVdImUVwFIySNFmy3hjEUKOkG7kD-p_YDSacaVYNqtQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=N3JHCMY8AYMOFPFoHBW2myiSVL_7y6s0fGaJFrNotexNQMr2BSRyAkUWGPRimtXNvXiIPoGLkuOc0tb1Ch2uMer5IuhC7Ppsqb014DYws-P5s9Auhtj2WYv2yLUo4OtjBq5UTQGvj_TULvmid4ymyJC4lnv7oILOE_Xn5hIT17Lm9aTSosiE2iBxkeyp5iA0B4ZZs93ueiVrYTyAcgZX3Vz-B4r-Xo6u-zCS-spiboY-1jZwmTXnF5KpgjqOwSzI05OU9oet1PXWycKo4yUpPDlwmfiQqranfT2N-M0BzwFVdImUVwFIySNFmy3hjEUKOkG7kD-p_YDSacaVYNqtQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25500" target="_blank">📅 10:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eudCk500Hd4nl3I3J07HroFILCQuK_panhG_BWv_zcUSRQV3j369tamSfzBFiW-Ro4vfgi7lzAin3N5T-vNRtt9FZP17Yiq-byeUrJRfSxQWN8csn_aZcgK4qeDb0j_YKDuhlxZU9GIfGO3TLPmLBd7w8lgOm5O7p0oILJ4dR7Ouk07RKGWPNeQYQsO5526p5oBxqMGw9pjUf1xkYoI9-X6OJgimPQeMfGr668xGkrXIq64JiinzQ79Lvoak--_UbMsFi2UGQ8nCQGs5eyUFQFZe8A47qXAyRUq8v0oeqROBox2MxV6pyNKnxZEdKXTQ187ILO0fTSCn4pSjVlGAbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25499" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3oTvLagrMdlLXm5Xc_TOdUlSslxU6r7_E1i2toVOVgDL181e8G_KLtoqjTacK5WXcNeTiEO0XeMQW8dzp8fTTazXGejuFA1TwopC_V1QgY1Ib8xzaeVJFCtlPXWPRHfEO0IUSom6e8XXRekWCCIcnMCDKfCBq7fIG46ce-LfZMq-KReI0wFay9DSD36AzuCTr1uNBKN-Lf9PYWCNEFGFQ-FRngfsioqcX9SjTiQjHwqCeuPEwbHQYjRh1IXKmlBNIEZbUL078Z5YMnlAzAc3ERaiErL6F6PCyOepMstbD0xbElnZlCxQHsQJhU7ChCNFp4KabdldgUbNAQgSUi2xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ جلسه مدیران دوتیم‌پرسپولیس‌ونساجی‌دقایقی‌قبل به اتمام رسید؛ نساجی‌رقم‌رضایت‌نامه رو550 هزار دلار اعلام کرده که حدادی‌امروز درجلسه‌به مدیرعامل‌باشگاه نساجی گفته تا400 هزار دلار حاضر است به باشگاه نساجی پرداخت کنه. قرار شده که ایری…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25498" target="_blank">📅 10:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25497">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=E2r-d6FaW8_VJBDwUqnEavkz7xowDRpl98JssjfDFdWnhEYjRBkVs2ENKFfYlAeQfGVKTmRahIK3i8XPIXrMpqm6Ol3Ral_-usIWJ_rLcAbvbi6_3pSaKiPxe9h77A_TLmoa21F4yG9vubOjatQmOdcdZoJNaTsCbsLxYjO62GwFnm-RaAS9HuZdZ62fwCDPu6omRpYYE2f7ie913dWIGaNby1QTMyy4BjbnAgJZupv4P7Mv21qhV_olhcUjbzlJSqFaaGW8-z0P7S1GxWvvW98y6TSKrK2AsUOTGU_Mg1v3zjOPDS7vjBsvp8gmy4VMKZ4zwOsyOGMD-JuDKrOddQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=E2r-d6FaW8_VJBDwUqnEavkz7xowDRpl98JssjfDFdWnhEYjRBkVs2ENKFfYlAeQfGVKTmRahIK3i8XPIXrMpqm6Ol3Ral_-usIWJ_rLcAbvbi6_3pSaKiPxe9h77A_TLmoa21F4yG9vubOjatQmOdcdZoJNaTsCbsLxYjO62GwFnm-RaAS9HuZdZ62fwCDPu6omRpYYE2f7ie913dWIGaNby1QTMyy4BjbnAgJZupv4P7Mv21qhV_olhcUjbzlJSqFaaGW8-z0P7S1GxWvvW98y6TSKrK2AsUOTGU_Mg1v3zjOPDS7vjBsvp8gmy4VMKZ4zwOsyOGMD-JuDKrOddQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس‌جونیور ستاره‌برزیلی رئال مادرید امروز 26 ساله شد. او تا کنون موفق به زدن 128 گل برای کهکشانی‌ها شده و همچنین برای تمدید قرارداد بااین تیم با فلورنتینو پرز به توافق کامل رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25497" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25496">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAr9qnOhsqJbQ-yQaMehndxFV4IFsi7DyRIz7zmqpWJBFNznaMkOxnvVY7HOZ1RQcYZc7jrx9lI9Jg-X4qVHCbswv1nWCYg4B_9DbKFqXGzqydObpRS8KEPsOoeEiDSLQFNgHGqY1e1QMKp4C5FcbaO80VX-NIA9dgXTKgKC0dLhgTjhpalTkgVxhDKHJL95vUFBSZldqLw4tESqpfIwZYG5tQrzG0ra3StydbJ5BywdK1SCUzyLb3mr3d5CeZeSoFEITpdPnJS5xEv2jPhIkmgvKcoO4yiOUmATBoGcGE2OsK01TbKGaR3YHfdNcXGUGvrUD0Dbtvto1eVIScu9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری بت ویژه ی فینال ویمبلدون
🎲
بدون ریسک در وینرو پیشبینی کنید و از تماشای تنیس لذت ببرید
🎁
🎾
فینال تنیس ویمبلدون
🎾
🎾
زوروف
🇩🇪
✖️
🇮🇹
سینر
⏰
امروز ساعت 18:40
🚨
ورزشگاه سنتر کورت
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
بابیش‌از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr21
📩
@winro_io</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25496" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25495">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=Xwiuqjj9sjF-LI2Ae1n-Ab97Akze6ECUpU72Zqnj4cs18Sl7QYV_KoDftBMdWizGbmURDu4S96fxMesglsiz-b9lLnOcegOklyj_gBDFCOGg9hArpHp3bD9sO0gKfflTnLkBPROnmzv6BZFWMYmbEZiqn3QCwbPDL5ChdJfzfHGRp4_pKDV5UUBHdWwAHJvOnfH5D4rKcMvXHWFVJFTBoPnjjSmagq2Zr5sELtIXFhvgBDlSuH4K-WPXXIHQLSF8vqRodkPaWl9u1KJD6BHfuxi1TYH7vwnpGnaXubM7KspsCkHHUQSKoZwRkHUAUKJdnPJaInEgPZrHNXXSlqZMUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=Xwiuqjj9sjF-LI2Ae1n-Ab97Akze6ECUpU72Zqnj4cs18Sl7QYV_KoDftBMdWizGbmURDu4S96fxMesglsiz-b9lLnOcegOklyj_gBDFCOGg9hArpHp3bD9sO0gKfflTnLkBPROnmzv6BZFWMYmbEZiqn3QCwbPDL5ChdJfzfHGRp4_pKDV5UUBHdWwAHJvOnfH5D4rKcMvXHWFVJFTBoPnjjSmagq2Zr5sELtIXFhvgBDlSuH4K-WPXXIHQLSF8vqRodkPaWl9u1KJD6BHfuxi1TYH7vwnpGnaXubM7KspsCkHHUQSKoZwRkHUAUKJdnPJaInEgPZrHNXXSlqZMUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25495" target="_blank">📅 09:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25494">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efZ2J9i5Q8if2cTzo5aByV51XxDN6BOUv9cr5CL0Q0V-2gJBSOLY6S_rAqPJArHdr3ize1bahhC5XlYfnbc9tkZKFNqSp7cLcZU8RE6X6xr0IGEBwfto5-Vm-bY34X04NEUyQ-O3PUbcDItIrDR9xIwT2vVmG6nVaRJYdjvQYbLtlKorONWRcdupK-dkaq1nKBbfqrK5QZTGoF9dSrmTvnTu2RObragjm6rYiyyewIiznCgzpW80xYb1sjYjC6WnK2hTRBFcOHvjm9XSiwiZbd2OAapp-wUR0lWur_F_6cLZ0caHmyGwashuxI_hGxEafo1cSYjKXWLCVja_zRDPEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25494" target="_blank">📅 09:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25493">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyYSsJCh80aq3tiZHmjS8FpFqz33o7tZhWRbF0VSyD8psEOdxtXutB6smSqu-b_FdpEHTSQ1v5I3yB16xAD0pvPTwCSovqZX-u8BxjpQT4wzWWU4Rp1pkMlh2qIhVbC_GKetnkJ4hU2VwgCyCa86oANz9BwWN7qe4hBZQqGTwSznTWI4RvoKes57tOhSrO3mj3gGdilsktm6Fb_A1kJuqhqZGnnrwqmnG6aOL7bziPjTOfLIp9RnAnhk7qJfCSvFj9MYacauvfuW6JJmvLO5_imSNQ5fVDEhF_GzJKHwRBGel7f9UV5urd3wYMCgmBTV1yAK-4IZLlw0DLZ6QOz0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی‌رسانه‌پرشیانا
؛ فرزین معامله گری مدافع چپ پرسپولیس بعد از تمدید قراردادش باسرخپوشان راهی سربازی شد و در فصل آینده در یکی از دو تیم فجر یا ملوان بازی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25493" target="_blank">📅 09:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25492">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=Rcz7Y5GTG4hCEYBPYpAEGtheKW__yqWedtH9UV3SHVSU5f9S3VQL6v89QSZqv-vN3l5AMtaV9aNLz8Y5Br9yWj1cqgz-yHfsyHhBQ8YiTGGX5QA22nnDaoEQI2fP6lZ4wzuiel138pCi4WQ-qgUHaGvrnij2Et3pEWGXoIt5-mDUjBc_MoMfNGukaNVBwYLehbronW5B4wnOFNuKO_fCsYnUmxt2rQ1-_BM7XBPY_3syt9sD_XQMxh87TH6c4wpqVmZY0-PTRPA3hCAfuZxX3LI1xrZmDCUvjbUiZwFug8EcirTEVYNJDWLqhx1R9No5rLdlIRox0xRojDH3bOLInA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=Rcz7Y5GTG4hCEYBPYpAEGtheKW__yqWedtH9UV3SHVSU5f9S3VQL6v89QSZqv-vN3l5AMtaV9aNLz8Y5Br9yWj1cqgz-yHfsyHhBQ8YiTGGX5QA22nnDaoEQI2fP6lZ4wzuiel138pCi4WQ-qgUHaGvrnij2Et3pEWGXoIt5-mDUjBc_MoMfNGukaNVBwYLehbronW5B4wnOFNuKO_fCsYnUmxt2rQ1-_BM7XBPY_3syt9sD_XQMxh87TH6c4wpqVmZY0-PTRPA3hCAfuZxX3LI1xrZmDCUvjbUiZwFug8EcirTEVYNJDWLqhx1R9No5rLdlIRox0xRojDH3bOLInA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25492" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25490">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBQYvMENm2f17Bmpam7f8ZpXlmp1uRmaWhfyPAw4p20z4NbOvkKT_LwiCyL6spZNroxkijAjPza7dEdhejGJOo7Nb_s5HwWwiKZvmp0_AUl1DZc1pCYCyu1sXIvTS_r0eIs9bhM4CYi6d-Xx7AHMYhN8g45C8jDl58IqJEi0uhPblNuw8o8Y9BMuKM7gz71sYrMuMLKUCwa5WhSBDWo8zYPsvofrKKdm_0GWxOCQeZxgfyF3aR98k1727p0fUXSnGLUK9LdPZJAcNE6rsDW9R7MHmBgUmZaztdyh8wJ20zIQGfdIScYQ6GLDN0Bo5twev0x8BXpV7w4nXAX2dSwRmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nz6ZowogmndhLXpRWinEqY50c0s1M3zBRMNchYzIQmrdh-Ks1rMVN5SGmMOUdPNIFMoEaZst1s5UJw7nDNUvHaTXTHnxUk4wUtLQwiyrxka2OfyI_USxQGP5nT-MDoj3CEXhNNMX6V3mAassuBATusJoY5wrueJnNogV0pMRpfnz0SeSIZuHk5Lf1kcEKP44WXD48CwjZpzNWbfdxlxNDhY7OaxNyOiubiv3nH4-NW4Jchk7bnmo_9ZPO0Pr3q84wuJsPvp_uX_5h-TjgK8x-scg8QaSlGYXA_Ou1JMW5d_9xkicr6Q6yAOGLmZSUPIPQQpeFQmZYRTEhluhYlF0Nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25490" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TN4KfYPh8p5M2KQk19qWK-tRqNWZ59O3ME3oxvG_hUUJ6XkbB1EAFCVnNioNM2ThqdS9w3Jc0pePKrTkzKqr0lYIeGnsL3riOsYzrkhK2oK1cgi0QTn833W7eiazqusTPI6GdQJmUTjQR6dZaLlYd6WpTYhMyKVuWAaFGDYiWmevhhCxQgxFrM73HWhwhY6WDTCWKrVyXsN8wDJxaf2PGDC7jP2rzgynP-N5WuYZNf3CzPFkriGhFLnbPlqdkfbPgsqWOI-EeOkDctTuzAQYkjg9UGUTJvZcx4nhxu4dnNFkuYa6ocggDlkm-hNA5nB01Oyqg-791rZuTKhvjRWmiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25489" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u88YjfhajfgDT16S6PFjQS6a6lmcdLNBBte_N94HFGglrgthVz3qN-4Yt0xHxMFhKuDXWYS-l2WcGWlHyqegXFpgddPS1lExWzQzG5yyGCuWLApE2NKvhxPUSnZRr5tt9FYgr8dU_Mm5XzhvDlQZvcOzAuVxbPIhoUA3ZwtR1OnDOMYtBCZybUbaos2Dd2l9Wr-MNjAiUXNdcpFvDXOQLZZUuREKSPYBKKE6vAGrSu4OV4IkCLD_odTuo-LEHQcwSlVBeu79SZAUlzYiOHj7rVjFv093f32rqib9pyTIXjSuTO5XwfpeAxNSzBaKvoHgXPogBVjdTqKmiH-JEs_Bzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25488" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25487">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6lPCvbZeAr58AU-sxouyWNqx814j950rYUdLEXNhjrD3m2Y3Cd5EmBuStCv8ZFD9ZwO0qXN9FF7zYwFSXkgEHzgrwK9_scO0dqOIJBkt4_mY7widsvM4LM-nT2zDc1YolN9BHBGrJEyFPzLL7IHEp7TM2y-7w9PZL0ebEyr_2xIJShipECPEqE1ut9LEfSDR4leD7ECdFODXXCkalOCUMmSiria7yI4zMdpy9JTPnc6AVzmKC8hs3MKiRe2rWd_4r6HkvZFLKFRh6SZBwVvvOztNxEvUX-gsKl7HVYHU0JLO_pJ_o5FsMpq8Rf3JlmkXT5jzNISHw3oeID180zdFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25487" target="_blank">📅 06:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWHnPvkktJjPSLK2IX--XjCzRZqfLJ9jG7T-i15PG-4gjC57n7Cb27ghY8Ltl0q-zBc9McGu_L9E4TPl4Yc9axBpdVdAaiV6ZmOEIB59VjppFvDmsCDBgOQYsCfawUDQsiJEGyl4E7wJjkGbXlluVCr6WDobdiItDRgRiXOSdaJy8kBclVkfZ9uRAwnU-oYe117jHrbHtfghPRoApy7hE4uBk0_fEb_UIcQqfPXh0P7UtOxXpVTflVrGQh318_chWXi4x-np6AJcaZoja-OnNNY6rSVu9Ch53pKADVAAQGjmo1nrrj107CRGPQs8UGihrIKr0sr9PjBNRFsv_BJW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش‌چیشد که به این روز افتادی؟
چیبگم اون شب جای‌درس‌خوندن‌نشستم‌بازی آرژانتین-سوییس دیدم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25486" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=tIAnzBmnOFk9YmLuXHrAX34RUxQ1guuYpJ5n4NXApzD9-aSo7IxEp8PIhbi3VA2HBs0NEzmt3F-En6YAw2SDBSVcqP3gQ9_WDlNeCbhuKg6egiu4mHr5jxsOpFa1LMLG0LIT410fxm7F60vjcXeNbGWLu1AMWdBnxzjh_dE42Drg270gR3uKbtAUqoj8TXpVnQa-icpneEkzECcZ_fVza4oWqg4V89rgVSam7h40NW08wh4dtC3F_nsqUHZDLRhAiZiGcRZKzJPUyokXfTbLxvIFrXwHKPOhCk45tnZFp7M97V2iuvXT7KiMEg0i7EiMqkVrWVd1wPV2XhMAEn3X1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=tIAnzBmnOFk9YmLuXHrAX34RUxQ1guuYpJ5n4NXApzD9-aSo7IxEp8PIhbi3VA2HBs0NEzmt3F-En6YAw2SDBSVcqP3gQ9_WDlNeCbhuKg6egiu4mHr5jxsOpFa1LMLG0LIT410fxm7F60vjcXeNbGWLu1AMWdBnxzjh_dE42Drg270gR3uKbtAUqoj8TXpVnQa-icpneEkzECcZ_fVza4oWqg4V89rgVSam7h40NW08wh4dtC3F_nsqUHZDLRhAiZiGcRZKzJPUyokXfTbLxvIFrXwHKPOhCk45tnZFp7M97V2iuvXT7KiMEg0i7EiMqkVrWVd1wPV2XhMAEn3X1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
واکنش‌جالب ابوطالب‌حسینی از رابطه سرد بازیکنان تیم ملی پرتغال با کریس رونالدو در پایان دیدار مقابل اسپانیا و حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25485" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbmuYqUCpguBYOLw0mTkVnQM30oM-hUgMRQsWkhnebRUD2uRcALOFht780zB6IHL7NxF-2BORuAZtWH_aagfBH4bFLeRL-k_q1gUzi4ehYGDnxoWHaObXQBgxarvYUIScKnBGmgyBJ65x8Rgtwyee7c6YGmOplGj0rQ3wr4wA77PDxDU-EcPS-AtbxokznIlYW5BAmv_XEJsRkvLpw0o_IvdJSXMA2sf1x_vLJSGw2pX60h66eImp1qhD2bOiMPRPug2uLOS7rGoq9Od6ogx0iFCXvFHyz-zzpfRxA0Vff7gBDpJ3cQn1sZVQUez2NriRQBOpr_psYMbKyEU0Z8qHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25484" target="_blank">📅 00:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6uy4Csff1ozIONdpJQtnrNzvh5w4iAkfNl0O24RGAZj9LM_95FlmrLGpiEVp90B2UJs2C-rs9aheFteuFLwc7vNt1mmXvaC8it5B4MZvVNY8Fa4Kgdip1hq8fODiVGyJh83DQ-7WOP401SdecXOoyP612U0tZQ_QkcrgzJDLylAGUG5rFhsr77RPcYjz-W2QDsvSggeUmnoUMlxKaMTDhJOboALQe43j5sj0XUPyU2qwQySAX7sZVdX2JgyDhUv5OImhHgQuOaicIZJr7RRWofRh--VgO-etkMM5q2p3wjykQvtPQ1q0EWanrbOg4dE80Zl9hpRLpwfwV_oLlUbXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25483" target="_blank">📅 00:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25482">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqfT618zA5fCNVn6sC9wlvVio5gMuLWb_uBZRcN_7lSDbvqzCNlIac4dZA4oWZ5X02FL6ls6scgdaUStRqt7ZqGHubUIDmsnXX-mnRw613Qey9w95dmoS8OVKIdysULf841HNhVP6HKzEXtTNkGMS89pEUSyNKQ75ha5jda_YtupmEDV_Lz2iS8hN7Lhkn0YMWj9YnaYz2Sj-YSgXTS5m3uAjrYzN4QfrBxA6x3uVIujTeJtVe1zpArCUwLZMSTFl3OM_oyd51RvEaaHak4GJkOypbYsOYB8YNWSJZUf3u6vAmcp2LNwlb2IoX-bmlSP69zoQtugKAW5Ux4yCFCJ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25482" target="_blank">📅 00:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G22QhVctRho2cT3GJvnxft1Aa3Mi6h25gRBdcumJchIjOTVLmQTw2N4SCaiEbA2m70yCCTwFELu1rsSOPZwPQlvNcjykO8Ir-_ZMG7ALTAd4J_ouFFUnBeUySmX1lNRXhg0lkA_urCwn2bPKNsK6ycdcnF8SAsz_Fiwg1x97h4BJnZRDVbuywlMgtqtWpTojxKGBMRfhrQ6nTwENJQUV5tzGjUgJDRspo4o4LEIunlP5OYxBIIxUhsuAZHp01pbjf9JOAM5Y6b2cn-sAMoojJEkBfuc5-L4X7P0oprJ0WqOlTfPrj5eOZcxIgZ8WZ64sqxj1a3nT7R2ZR1ZO_0gIiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25481" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-k6HS08OUQ99Q5dFqVkYSK3xQAVNEtImghUX_jpM7gBWNtP7tN_pKZBtpUC9MeoSveAfG3B-pWNurjJdfUWhNzZId2pkvDminXecPZ0rUTXX9aAhTUXEMlOSrNA99q82REKp9uwFvgmGLD4E0jno2_ifuTpHSdnpgMMeZB5SoWDNVW2dJ9Lxm3CnRKAXBB5MELuDYVUD66ryRGmU7afq7cu7pEnpMBBVOUsfsLBIkWkr1SvlZCnMzQSjzHyrFcn2mbz0yeMKUv4fe3kqWjhObvwa35AQ83k6BRZMqlIbVkhCgjRJH2SGzIzSHfvRMvLNz5gazqXxleEFDKe1kVoOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b3qSb9Weut5Hv6IiPTt6Vb4uBzCQGGwoL6qv2G5WV4NniqAsQL5gZO5r3EQk8taSy7wXh33fJqXp7mGyhFgsWgZ0EWV6Qd8cAEqvxbldhb_MZQxpxi5M9CjLuDDRwyLZ3KRhhAgY21P4pabZIH6Y-BKNL5VPRH-ZrC3tZ3b_Avw96yTGjH-0F6Q7GavfCTr9tJuvQZ0jVmkbdbcm3lhbAMSByefKyNCpe3-OJDQgwrkHB_0be2jYwDgDWFWzx0m759fXwwg7FJH569AZ6sTBWuzKOEHlVu3j4X3KToT_322DCOE4nCZH0NCP2Ppx5tpnxoGbctOekFfbWGyyGlS_Tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25479" target="_blank">📅 23:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vX8ETimGVO-f7jXcEDj5Pcngsk3RQ46oJU4f7CqvkCPyEGyqIsoUvjqY-1vRo7im4Sx7ptAIJtOe99Yc2I6S_vrEc4ajVRU07faDIC6kRV4IoLnD5SI1qjUOuGirU0QtTONunGnPeaBioq-NaPqL-k8115px1TUQpyyU7ffISOBtF8zf8KpfedwhPPfZ6E6qb391pBBP9i9641FlvrBSFFlq70s-Tw6nAqrzQkxvMceM26zd-3BPfBMoXAcnj8DVlpUZ7VH1_XmmR7B1N_MgfnNkeAIxtqYwGOHQu1pTm9J6QEEjJRETp55kzP1kz1yIVpCTf7oXoGQYEWU4RbhxLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد سرلک در حال مذاکره با باشگاه فولاد خوزستان تا درصورت توافق مالی بین طرفین به این تیم اهوازی بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25478" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25477">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oh81_NUw6afUZ9v67Us8iAk1wrYzO2KiGz2NZMp8zeDdya1XyPn03nKDKzzooXyaMkbw7uMAlJ4bo5r1e5yGOqCZZ5io8TunB1de_lgZsjCub9rgTV8bw8sy7jAlDCfuHdqRjiBC-CEOqnHp53ZoAkLxd_zHjYSHDMSbwKQtqzD6oXeKb7J3TKlJmVEBe6iiog9o2YVf-nRpXS2HyPzcEXa3utULbxK7JDDw8X8tCxnTOaKbojD3cvZC0eh8RGuO_o85Tl4e59sgRKJhdJD3WM7wZ3uLbMLrzS48m3W1iw5_ZEKfzRO7X_tz7U_vUBbJgbCMZLejgoDDLMNQvM3hBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25477" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAFd1FEioV1KFv-JorzkKb0tV_59e1vKi-xA1gzXz3lsHWqASl8b5CYT1PkWTfZn_hQ29LUzYgknbhXBFGtUsXTaX4YG9Hk5IjYjVrSBrV6nTQ8lVcmiumeaB-eLR68Lyya8jhZLzTfpIrJzA_P4tr9FoTPf9dKIhCg1b1PdcpmI6g_EiU4urnzantwdK_GV87ESbmeK4uCbrzdKmLjkYFUmdXWka1BgdXBHc-GPswTxA_W5EYaDwCNMbFidQTzH9Siz5TGEx4DjCD0B2ZYEltcaxNlGXDDG3E2Xnzq6cbFtguTjSpXbvClh5coPMZkBICyZ73iOv7Yme90xLVV-7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ روبرتو مانچینی برای‌عقدقرارداد چهار ساله با تیم ملی ایتالیا با فدراسیون فوتبال این کشور به‌توافق نهایی رسید و انتظار میره به زودی پوستر رونمایی از او نیز منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25476" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25475">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=pt186-I7-C9NWpuyPqIjCJZu3_-0-uun7S1_TLXYagiLhWdLGosO8tVI0d6q_89sqBu7SZHljqn2iqvdb8TF_7sZgXKPmByjX8J1aCLWabU00xD8x5zGArzAozcKBwVtXS981HUa1BelROaO0f7mRmgDmQV3TFaMIba33hIePxLxzHzOgE5vwS2FIJqThMVttZ1KRyUHj7P99oGbY2oN36MEAZ9KjYHA3qcrDvqPAEwsKv6bNfm2gT_qy2VyxNSD2BoI2w38zwMEp3Sx1J52RQD_r3PmAa0FcVE6h2JKxK3bOHQN0COtq__JFsk1bw2m2xeqnwazjsuqBnu9VNGdkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=pt186-I7-C9NWpuyPqIjCJZu3_-0-uun7S1_TLXYagiLhWdLGosO8tVI0d6q_89sqBu7SZHljqn2iqvdb8TF_7sZgXKPmByjX8J1aCLWabU00xD8x5zGArzAozcKBwVtXS981HUa1BelROaO0f7mRmgDmQV3TFaMIba33hIePxLxzHzOgE5vwS2FIJqThMVttZ1KRyUHj7P99oGbY2oN36MEAZ9KjYHA3qcrDvqPAEwsKv6bNfm2gT_qy2VyxNSD2BoI2w38zwMEp3Sx1J52RQD_r3PmAa0FcVE6h2JKxK3bOHQN0COtq__JFsk1bw2m2xeqnwazjsuqBnu9VNGdkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
روزی‌فهمیدم مسی هیچوقت‌تسلیم نمیشه که بعد دعوت به این برنامه‌ازمجریای حشریش جون سالم به در برد. لعنتی‌ها ببینید چه گیری بهش داده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25475" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSOKmSC03t4ZtDLeDwcPqn9Jhb0kwkuLKSwr5KtzxkfRPQkhB9iJNyQEHLjeTZYRGrPylMXop1TYFG81PqS6cThyBgKF8XzHBmY7Mp-u-1mZwkIGpOtX7w573RBd7hYthxblpubJy3v9fYl6nZfbwTCKZqPGbhT8UxpeGxEfbCCMqhH23MasGPFERan_HS1TsaoIZu4rKJI2KYWt_vU-lmJNySZE7N_mkCfqGLvr20z91TW1k3v9fRnHW5bdu4nfLTctYg3q973H2_khcgOkryQQUPO459NUdQMn-OvzyR-K1M222TlFXr7IqZIvPjVeeU_EB95b5R74lw9In6rCQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط پیمان حدادی مدیر عامل سرخ‌ها درباره وضعیت علیپور و محمدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25474" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=Y_q1ZDJMnFrS5pLPY8Uo-2l7w3LNFFwcSW4dEKq9YHhJLSQnk0GpuWf6TUiHAJu72orfDUBSSQ_61VYIHOIFA09YhzCGCppoPbTSS2tVYKfnMUzVsiX2-4YThU7uQxBgm6Py5PPOsuGJg8lRt7WDllgbAYxnoPwLfhR4p7Kzvle8UIUBKrDfENmJnS6SfWylCTy_kIocRTAhf04f0C7TFX8Na0tjcgeSxQB6f3P0UYd8boPwj_Yi__wSA4UBU3p6ARlkX0gHwdqyZoMa5ARexncsXGhyHEpyTmczTXFYLHXAWnyqfO7Nr-6Y5hP1Np1vyyLoIqs_A18v8o2r35-5vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=Y_q1ZDJMnFrS5pLPY8Uo-2l7w3LNFFwcSW4dEKq9YHhJLSQnk0GpuWf6TUiHAJu72orfDUBSSQ_61VYIHOIFA09YhzCGCppoPbTSS2tVYKfnMUzVsiX2-4YThU7uQxBgm6Py5PPOsuGJg8lRt7WDllgbAYxnoPwLfhR4p7Kzvle8UIUBKrDfENmJnS6SfWylCTy_kIocRTAhf04f0C7TFX8Na0tjcgeSxQB6f3P0UYd8boPwj_Yi__wSA4UBU3p6ARlkX0gHwdqyZoMa5ARexncsXGhyHEpyTmczTXFYLHXAWnyqfO7Nr-6Y5hP1Np1vyyLoIqs_A18v8o2r35-5vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
صحبت‌های‌ندیم‌امیری‌بازیکن‌افغانستانی تیم ملی آلمان در رقابت های جام جهانی 2026؛ این بازیکن از دو تیم آرسنال و چلسی آفر دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25473" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25472">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHURr4kyB-Q56xv9yBOX1Y4mw-jYKKmO_gb0N-KSkxkGkeCYw7kimzvEBQSVBrL5nhkUGZEUzIaUflO_n4ITHv56DrOQkDeYtr2HaoFMnTYXnWQk9SPhNMYgCHe5iAPMimXEWVSGmB4qYcAXKH1LyVAErJj9-XduW4INaJOX3cV__Hw8Dvpb1pQOYncZbCDIypkxTtd3UmwSmzced8WGGvscCIXEm5NlmCXlYaoPQvZmPW8_N-0LEi-UWL5PXUszGzcli5zB1ss5juhpcjYWKxmu_B9si0U_MY4pKS9RpD445-v0BbNZ1NyIAhEXuyhRk8lT8kutrajJfqZgQTvHag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قدرت پیش‌بینی‌ات رو ثابت کن!
⚽
🔥
دو مسابقه جذاب:
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🇳🇴
نروژ
🆚
انگلستان
🏴
🎁
500 دلار فری‌بت
بین تمام کاربرانی که نتایج را به‌درستی پیش‌بینی کنند،
مطابق قوانین سایت
تقسیم می‌شود.
🤖
پیش‌بینی خودت رو از طریق ربات تلگرام ثبت کن:
👉
https://t.me/betegram_bot?start=p6_r4EF37DCE
⏳
فقط تا قبل از شروع مسابقات فرصت داری!
موفق باشی!
🍀
⚽</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25472" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25471">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3V0lHt8EFVMH2NdmsqPVUv181yGF44OUBXWrcaL-veMN5E7J46y0xNm08KNhe_p5WgqgO4l0p-jBVLFSBDiF_8KMYdL4h-YX4NET0NdagK2E41YXtMN8w3weaJ9cuc30alVytgI4RLAeOaNdA5GqLOy0YhHIOczyF3lKGZRyFqqhfdGB2KtZfvSS-05DyyYLB1Tt7VGQZ8N97pDVPq8m_R1FMRB1Zk1xS3SDjVVPOY9dNOspG8TctjhfLyhzM4pZ5ClKvOm84cwpzm-NiibmDTp3Baz9SejOINqX1I8O7fHTh1IiczLUy3UUclx0qdYqMNEPepwrUjWB2Q_DK3hUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25471" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae_ZmizATp0KsiAIbu4wnyvNf2wkm8zFSs2_YAZd9HbaVNWTDL7LAztEzo5wcNs3W_i1lUtNqaZSTbUwi_BGkv8puuQjK4gg1e3pRGNhVe_Im-eqiVm7eKNepYW_5o5oUd8IhR2U6PGhdwhWVZv-08cAjgZq5vvNgdRIEhKqe24DG5o00gvOoJoYRz3laVoh6Rd85dtM-FdFPtFUKtz2cFzIDNZwiG7cuuTjwM032Oi-V7gTHX1qqqLlZIFcr26foN2VepS1w2MSMrQXrKiefu0KuDs0bGGvnXsOdrvQGXTAHlsgbcmzt0Zh32WzZkxdO1uKNEStJw01JyXi6aIPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جالبه بدونید بازی‌هایی که تو این جام به ضربات پنالتی کشیده شدن در نهایت تیمی که پنالتی دوم رو زده برده که این‌فکت هم درنوع خودش جالبه واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25470" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=qldCrZX1YV6sRx3oNTMWrDct6lCpz8gRQoqInXWLJAOJ4RPmsnBBflreQzvmZwBjkskWOV2HvMXo7NDB3tHyHMLWXCV4bcQRUJ3rqiTxT4EQsWnRGz8nwgfSbmDboWmINLI8U3AczXOOGtGClKtisUNX-8ccDxaMx58eTbY3Ki6f-mY_yJGWthd9yvajXyhGEfxNUCIwPll1JLYeqBYy9biiApntE0hMsaQeI3xlQ5NY8oG8XGIaVJ9I8iqeStk0_HESCO7KidfyklHl9pvRh4sFMU9KnG1V9akP_nUahSJSB-_QYZsW58j-KjPpZEYQpN-EDdMmYw6KveLHO-z35g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=qldCrZX1YV6sRx3oNTMWrDct6lCpz8gRQoqInXWLJAOJ4RPmsnBBflreQzvmZwBjkskWOV2HvMXo7NDB3tHyHMLWXCV4bcQRUJ3rqiTxT4EQsWnRGz8nwgfSbmDboWmINLI8U3AczXOOGtGClKtisUNX-8ccDxaMx58eTbY3Ki6f-mY_yJGWthd9yvajXyhGEfxNUCIwPll1JLYeqBYy9biiApntE0hMsaQeI3xlQ5NY8oG8XGIaVJ9I8iqeStk0_HESCO7KidfyklHl9pvRh4sFMU9KnG1V9akP_nUahSJSB-_QYZsW58j-KjPpZEYQpN-EDdMmYw6KveLHO-z35g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس که دوهفته پیش با ایجنت علی علیپور به توافق شفاهی رسیده بود حالا 72 ساعت به‌این‌مهاجم 30 ساله فرصت‌داده که برای تمدید قراردادش به ساختمان‌باشگاه برود در غیر این صورت قید او رو خواهند زد. درباره میلاد محمدی او تمام توافقات لازم رو…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIFODyZsyz53YVPmokWvTk3qap0SPly49fTevJzdnXj4vDzTpKSGIqUw3HPxy0cExR7UUNkzBS1gy4LQ2ZVGEZlo1HNVyB9mxVzGtaDZ-60qFI6tlZCcBn0u3YTKSMmmi98QKUY1RKOdSuKkjBpsyGyOaH-lBMao1xyWli3fOWFM88rqjl17NGYsgIK_Gc97L1SV_kQhPfLRWJ1IKoZY3-qeNzkGIFhvRn-qHyZtnnjlVYK341DqqLjlTTeYZ9RrwYO1a94V0H2n4AAIHl3n-ZYoDlIrXoQegbs49q9MgONKjiik5gBygHnULV8wpOMJax1Vc3ulygCn5hcFwMwjVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25467" target="_blank">📅 21:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XE0Uqe5FadSvSpc9kZY-K4E5semTTiCb6UZVcfnkE9Doc2CM70cF-8WYHBPfyCnMTw5Ha5ESAp97wR4i7BCnXDDYlhbnVj9zPYnYQkLoPfik4HI00uoM0dCbob3Vkn6J5zt7V5oMQvYMMQVtg3uNLk6EVR4lq7WX3fWjM7ejJBQDy5mR9Vv5eQWO4Gi5JgLf2qXl7X_94YJSyL55Dyj6YCaW4fAgKYMWPJnlNMS8cKzhzefhp0MA65V8WSatRP_PRSABk-R9bs5A9jHO_kjSVp6zy5AZIE2UDz22x9s4ibAYusPU9Pbq-_IitkXgJ8ra1U7r-ssznjKmvlLH6GV8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9q528gf38iWvqHrW9x7J__0B1EhwN5VGARYCqTHNyhyR9RFZw_AEczwxnZQY68fOhK74NwLFoiC3Mg6v24giya3ee6TILbFXHeo3EiynKPcf21GAyojeiKiQDXWeGRrURF8sKV02f0vgS3eqF8SNRn3zr6yBaGV7I3Ia6DX3GGdtP0yGLv3RRAIObotmEKaksAipGCzPwle223gYxDxBhgEL2RKwDwPqjP_vtvIw7MlNPwtumHiUdV7ZXNK0m8YTece63lnYoE96Om1U6W56OULjZbm1ZOuX9YgJFX7kNXhrdpKlaHgPCPrABgXOAH-gNRt-uutT4oICzkBIoBFUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwafUvunLMQ4PAs7rN1S28QqyVUlpIZj46yY-Q9KSasd6VILgKxU8KqBCFyk6-V67TtnXbW8FQqLVnUYxjAYBi5xSdMX0wW0w2-59h9MTLuNdXCa579U5S_2rJWLN8r5NiugKOX8EavktB3ZsOJ2iZWTvOxEc--tZ-czaZQX_qQX47ciHFuF06hvEB4wbbnRfByZZ-ZLpMc4uABRpX4iJWIsbUst7a92IVTfWfTs8zTF2eOIUeTK9QkuMRGDL8QPcbtUM_6d7DBns1E01os2Mm5xTjbUPCabktSH-JS1505vVe-nqZwZzt5RFxxj67mK99ka3M_UPE56t9wo0j_7rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0BvOaFbUVoybqpUEz-S_UPzi2I9HV4kgBl39QSVJb3ORNZBgo-Rr5Po4RybdzDDGaRV2TM35oUBsPrTnQYCvSgfboIKvG1dzKn7BxBw9vm0MRKoHx9bhyGtIZ3atlx0BgTIoc39Zt3vlwscKDya29taCNHHr8pgSgfM78oixGk84forj7EXbD4sAGBGvqjn5Ob7gZGUJWr3yr9FeNqzLJcyWbawQS5r8TghByV2Rt2-FKM1c9ptycbWRPLhVm4V-m0BZHKGiOP4wcLIaaMms0KxmZ53HH4-zgoyfN7RXuzeB5nB9cqRcovZxktkGg48m7VMuFo1RKMeCpFfnsYHiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_2be0dMaKZ2aSjJqBwTgRncNu_eLWqinPwJDYGxiCu-TY06mQ-Tc5hCQ4BG5wFosvUmQTfvQjHcXsObHypeXwE-9zOlHl408Qp62lSQx8W9_JDkHWKjNhKbVFedEhYUvXeDAQxkzyT4o1RS-RF7zm8wcnwz7UhrxqJEVU38QMGY1cU5w7x6NesVW3kT3JOWrxfAJa7o_IEeKMHQTfuuTDo3R4JrG_huSdmgT5SJr2NL83YysDHwfsY_y85kWPhZfJRNFBZrd9mo-qWFjyHDzPYoJirw7XXiCik_fX2CE-DD18yY3njQaPIFsPDVeOc8puy05RPUkwgPhsO5w8aq9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruV3RWk44bmoS8J1rWkLLLJrI7ycp6gTl4MzFmBw1ZQH41OHG-z0mG9-vSv7JfPvMGOA5eFV4uyjCXscDhCgGRxiEupeNk69zJAxNWO0RBq4yKJP9XNEm2wqc--kWXOklcsc-F7hNZOD5d8otkq0caKsubrVU-NymKl0coWqRGNgofPx40UY2kilTrRqHR7m6tunawMfeYDgFfOVKJ29OoXSeYN6t0sRybXB3fZHngsLvVUxSzzlmVOdY_qxGT7CaPItBBNlPABYo_Er2axtmtfu-k0RkJ7ldkHnL0YeVCGowIA2Lw8i7YbyNhqBKGKmriJHAEkbzde3xdIU729jFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1OyVu4wjDbaF6e_MBouyCA0I8olzmHFHhqkxk3RHYbWXhcpzkJVVUKc0vxrhgt2MJpw7a30iG7xc0iHMXUMObj0bj8aTPAt-eixejl0CTOAEUnCQmXGwUWvKBsglem1tqeK64S5AR-zAIpa8BmRmmN-WFJhdKDOsw2OSbkqIkQThoN9FKpck1HkSQs8z9k9Ui6t6to2r3rXzr7755Sq2jsDsKiTYT0pTL4ONImEJ_L-fQK8XYiAMHi4SDOgOGtG-S_OnU7cvx1hMNkeyJDkgsP4OwjSf2ZgHdKtopBtrCDSOn47QujqnhKcpcD0cBPh2qd-D3JzNaGBrkwKe3vb-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تقویم
؛ 12سال‌پیش‌درچنین‌روزی؛
بارسلونا با پرداخت تنها75میلیون‌یورو لوییز سوارز فوق ستاره خط حمله لیورپول رو بخدمت گرفت. آمار سوارز در بارسا: 283 بازی، 195 گل‌زده،113پاس‌گل، 13 جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=MpoMhYPxcT10ecz31oWCy9jHxqF3BhzOSL7oH4xxcmcLk9nuCO2lUXjuLaJTP6diBDhIwwNx9YacWFXKf8m0k-cEdgMcrR-S-JFX3toWAs554jOdICYHaejyliiTOYxiET95rGpvk6L_mcGK27cjb0T4Xkmw0hu4sN3jwRgvPQOc9J4SU3ngWwji1xwnmWe1Q43ejpQNVi74UZ8l4Xa1PSKrvWMpq7E9DyDIG-tbt-apsKq7DwqM0xibNIS11hughlwPkEbavJhaBXIEx6KMnVtWl5biGotOVAe1hHDeZhPONpGJGH_izEwpTHfWJsAI9jSMtDw-tC-gxywadac6hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=MpoMhYPxcT10ecz31oWCy9jHxqF3BhzOSL7oH4xxcmcLk9nuCO2lUXjuLaJTP6diBDhIwwNx9YacWFXKf8m0k-cEdgMcrR-S-JFX3toWAs554jOdICYHaejyliiTOYxiET95rGpvk6L_mcGK27cjb0T4Xkmw0hu4sN3jwRgvPQOc9J4SU3ngWwji1xwnmWe1Q43ejpQNVi74UZ8l4Xa1PSKrvWMpq7E9DyDIG-tbt-apsKq7DwqM0xibNIS11hughlwPkEbavJhaBXIEx6KMnVtWl5biGotOVAe1hHDeZhPONpGJGH_izEwpTHfWJsAI9jSMtDw-tC-gxywadac6hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛
جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
