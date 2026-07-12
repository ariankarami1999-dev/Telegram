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
<p>@persiana_Soccer • 👥 437K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 02:44:12</div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/25567" target="_blank">📅 01:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25566">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nfa-oitmz525IyDyuTHT9vpUomW5S8oeumiu3-4De7AeadTNFiZ2UprMoWGPXFbpw2YYI9fVQ-vAjUoVhscx_T8R26qpDGLpO2CQco7DcVv86KAiU4FYj0DEkQD9ebR8YcCqCEYqHkDJgSwMuqoPDqLgIgj5Aj4Keb09SRrMxke0QRiZS6C_X5KawdyazkIoqR1D4GpksZzApcfrzQTa7B66KYlEJDlfeNcNOnDLzBfK5_xKJ-N6uyr8IUZ1W0IvtHpibXwTopTrHOuv-p-bDdzgrzvGlKx2srP6Gk4ga6J0yGfaLtN1Zr9r51Ctse1PC3gF-n08UKZ4xH3m7MqU5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/25566" target="_blank">📅 01:37 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/25565" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/persiana_Soccer/25564" target="_blank">📅 01:13 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/25563" target="_blank">📅 01:12 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/persiana_Soccer/25562" target="_blank">📅 01:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25560">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st_ALKGkmD7LSHU7rB4kgY9G5poPloIEq1oBtJJH_Qi0Ugnie-9ftSlO_E8pApzBlXbh1XZZyUaqlCTesWOHE3_L-adwJXjnJ8lLeKVdHztKUzuywiu3Z4AD5JI8p9ZtIpThm_5K_0wBhQjR-h4bQbsEo4yfTlgNmaXOr5fPjXOgFbr4-aMVeuiXz1qjNDuOBEllmmXACiG0GCBTeW2W0zDxeIBufFXNEXuM1umkFuhAkGZqtUpOZiGbnjoRUIY_3PF0roRUyMXeDIqC1gwr-nUEy0KWGF4PQmf4Tz-HrTx62ftMyk4Oy8GF7weDH7xefhdWc-wyPARqbAMXhn60HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فوتبال ایران عالیه؛ خودِ بازیکن هم نمیدونه دقیقا رضایت نامه اش برای چه تیمی صادر شده. میگه خودم با پرسپولیس تموم کردم و داخلی امضا کردم. یک ساعت بعدش‌مدیریت‌باشگاه نساجی میگه ماامروز دزدکی‌ازتعلل‌مدیریت‌پرسپولیس نهایی استفاده رو بردیم و 800 هزار…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/25560" target="_blank">📅 00:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25559">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIcOzAo93kW8ifsGHXXAp9PGkMKx1BqRdOq6bbprvB_WCyp_Q2eZpzLLcN0ZPoIeVxWmp1u_GUuGa7E1gDn6ukPYGgIxOYnOSbIKF_XYwTE6AYa_Ssk4bkOhi2TnBUWE2e3RrXwM3sW3w6tM0J8vYb35C49hLh6LRNkZnUTvXWiLYxdEcjbvzSQLYliKRCUidbwYqiBQtYFgTmXNAXjz3jghfSImCyktqsvG4SL7L8m4x1gGplyvy-4juuFRwIAMZxGX3Z3cg2xBgBvzii4F_7nLmML2HcedMSK62pjCkUDvfJEKPhB8O2I-TBy583VRgUn2HzhccY8HQj04aowTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/25559" target="_blank">📅 00:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25558">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIJnXuks6_U-lN_uLyJNSdZUyisSDiY9LMeI8FhkHBNcIREgLVuQTorSumM4C4cI9eTehMZqUvqjxq8VcP3zA0YufQV_C2Wqy-tSKtuE-NhMEKmbz2q3kS1Ljtalq8Di-TFLnkjpImcluR8dvmiG_8TWhhQAxpda34ti83d1ydw66F3VvbV_XUXuwHHBNGLJDUdCBz7gm-8TsahoVTMFLGPGuWXXRIXbuDgaXNAzDt0qlRzXhCZaXHJBDG18WmZ4p8QZJN4Gb1QLkJ5VFfymAqAhbUMBUsMt1LO0zxx-_8quv5AA3zpEmfPvqedMhY94NCEpA5KWN5UECHExvs0rkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/25558" target="_blank">📅 00:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25557">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpJPnXdQ8MxpFGAtp5BPVEvC09GXYZ7MTFeJmInBe3LW8KfGMr53k6GUgFiW1hyJaML3ZLL3ZebA1lmxE4VJrtjyqzi_LG10Bg2lOoteli2cDRDRRYAmLOrzLKzSTsj7UhRNzoujaQdRjAA9YE7p-d4woABlVIUW-Wf3haLWF_zz63ZrYFT8aAHe_fyfft_uS_DQBm0f2TjSO-UcbGibmtudCzElGp1LPfYXp9cS_j4p6bbC-jlNjPUGlCJmCzBdNzhTYAdKhr4BQPb6G-og4NMglFuzMOovavDflxojewupm-v_55YlPY34h6EBsxk5plIB7Pbdn-vWrinGrTit0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کسری طاهری مهاجم جدید پرسپولیس: ظرف 24 ساعت‌اخیرکارهای‌رضایت‌نامه‌ام از باشگاه روبین کازان انجام شد و فردا باشگاه از من رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/25557" target="_blank">📅 00:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25556">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JynSYoJJOdg4vnG_LXmMQX08mHqtq2MpH3-7Y5AQSChdTcVRP3CXqvQ4TnQhk7GR31Ro7mJil-WnzkZTQgMhPbcY-1XMD0lfFtK3SJIhSyx1JhbfiQDBZQastgd5QlsQUgThcIewd7D37S9cB7_7V3etsfzPl2tYgmhQmEY6Ugu9aqm0XOFasI5xuwBT5lSsZjSGDM35p_z_stqQcp3SgOkzCrWaO6G5SfcaVtzhbLrpwqoQP0CgZdtVrTaTVc2X2bZDLar23wKS6M5tMdUfFOrIdRTWyeuD6b3vpTsozJmhkObgvbMzF7RSdb2YO-YbLy5jZKyaOyFG1Y_JKIRpnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه‌عجیب‌ زیکو بازیکن تیم‌ملی‌مصر:
لیونل مسی، بزرگترین بازیکن تاریخ فوتبال است، اما بعد از کریستیانو رونالدو و راستش را بخواهید، حتی حس نکردم که لیونل مسی در زمین حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/25556" target="_blank">📅 23:59 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/25555" target="_blank">📅 23:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25554">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDzh2d0ypJFhMq5CuyuyLhCQMe1LmZ2dprUioCnyhTQ9Bw_3gZIIsuXB1lRJ9mv3AbOhnGbefttGCj6RbmW_rYV-DjLTT4IxE_VAVDtk4X0LxNEx_pLBJhndaWA5liX1DJ2j09W_fnA9EXJYegfDBwtRMcwCG09s23KCkay3HpjmuYPdIVhJC0RVyva0rEVVNMCunc9n9mbjiD6wfcR_cl4MYgxsCwlYE8hgcfxy7xsymKa_DmAD4oOFFF2XAkOTIgQY6qYrtiwVE7KmUMheN5SjRuLnLpArKvoj9xSWK65sO_uxW6s-CNqW_oPRoPA3uxdxfvmJmHj6YTTdg4IGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
رنکینگ‌شش‌تیمی‌که تیم‌ملی آرژانتین در این‌ دوره از رقابت‌های جام‌جهانی‌باهاشون بازی کرده؛ به هیچ‌عنوان‌نمیخوام‌ارزش تلاش و کاری که آرژانتینیا کردن رو پایین بیارم، اماازحق نگذریم آرژانتین اصلا مسیر سختی روطی‌نکرد و سخت‌ترین حریفش، تیم ۱۹ام رنکینگ فیفا بود!…</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/25554" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25553">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQMammMSGbIEN0zu0eXYpe7mH7S0vEW6UMyjsJ0OUsxHDvNoOEjdtKa7VQkw7VABwUkpQoFJDYfnizh2IALb4a8gB-NBY6mjhG88bCab3Ijph7Tw7d98NpmGklarHVux-Mf-ejh6HVDAclM7nK3fLorfbEIgRWKYaZIqBujmTQGaiOm14CEGC--UQiMW4FsrSfuLPMXFkgHI4hrT3lS5vxpViIr6cR4-GTd1Sakc_2YYpNFvfT6FEeRCMAxzXf01cl0Pc4UUimzMDwftXEIUttmXTJIYHujSplwaIlTwU9NpRPWFX6eN9N7CuhP4rF2TpxDsBYVVaMwv5UAiEMDAwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/25553" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25552">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcFgNrvzTPws02Iigu9fSoxh2CHi14cV2aZbNEV3SD_a2zSIoKIyMkJe0KY8UqyNzNANCGpC1atT64hd2agJEPNrmTWjyz5FOiErYcHmQYNMsA2iLfiwyHlD7unooqQ6Qf36I2uZuOIhesPnmvERJaA4IpDSvvUjOeqpwk8KbQ00u_nFvVuM8p0k_L7PXfmlNOXM02HTSAaeMTNb-Oc2qQAsJ7_DkVZwM2xwrRFA2hHF999ZMntBhTJ12-Xf3JVQQpWSm_2gXhsdK_zeT7I1pXItrcopaJFmyYqCpAv3n_iBg2y2ARiz2gjOQKxRvlQ7sPCbGD6iqFoY8qfsp8MMMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛ جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/25552" target="_blank">📅 23:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25551">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">📊
🔵
عملکرد مهدی تیکدری ستاره جدید سرخ‌ها در باشگاه گل‌گهر سیرجان:  ۱۳۰ بازی، ۱۵ گل، ۷ پاس‌گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/25551" target="_blank">📅 22:49 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25550" target="_blank">📅 22:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25549">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu5ai3V-NXiQ3DUxdCQDTPMi-B7QzA5GiO4nUGtYoOiJ7CwcBSWVMXLR3JlVKa-IZCMbfDalHWOYeim-EQP5zW_26v6n8YZdudJRXbWozB26mIScS2Jngo6rG5OzzyixoNu-ZjFYeVPD5XVzc5rQBxg8AuyYGUKHLuWFK6CjW6m1MGrWxBZroLkPk6N23QeNrapwIK3i6Y6rQBw_xB_t2YsAVoGLVjy3b2K5FsyVOEnvCW7oxwHEk_uTK6380j38nIyV9JGl6q99wBQ51jEEQKHUTJgpMEVN57ZZWyJllHPG4_IEHI09IUfEr5uHWL5n3G7z7jlu27vYVX5uXWiByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس ساعتی‌ قبل با پرداخت 700 هزار دلار به باشگاه‌روبین‌کازان؛ کسری طاهری رو باعقد قراردادی یک‌ ساله قرضی همراه با بند خرید قطعی به ارزش 500هزار دلار دیگر به خدمت گرفت. بخش رسانه ای باشگاه بزودی پوستر طاهری رو منتشر…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25549" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25548">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfD-FvGdc7KuBykd-fFXj60v-5Ei7lttpgpdTHGrbDqhsqRtgtEJdqupnK0R0ahhMs6kt18EUiocnL8_XVm_dmfRltYXhUZoXEYrYsx3lrp0fV11Bf4zmIsFre47m5nr2ymWbEXwviUdGgy16-EgxtVcijsbzdFpbdT3gPRXVToN8S04tpcnyI9g-uyi13XeC_SOetEgxPOJA4IeBtYg7vvxjeMYhJuKCvCGyB_FOwJBUgyrxhtucMVeMOIPmkCK5fX_QNhGbd8wfHMptQLckZSYAGNk5ksuwUFp30MGLE0Tddux5x60Yt8VLlUEEGys9aBm99eSPJQACB_2Pmtiig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇱
فرانکی دی‌یونگ و همسرش که در تعطیلات بسر میبرند از چلسی پیشنهاد رسمی دریافت کرده. ژابی آلونسو درخواست جذب این بازیکن رو داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25548" target="_blank">📅 21:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25547">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROSfb8TzjmxrcgEVvg3p4innSQgYNZglWDg0BjyJc6MmIeOXMZKj-2rV1LkqlmxXYMY-OFhlGHlVGFVSQhgBMroIT3AmgjGR5luhs3mzN9AttzK617Fi_i-a_tX2koAwpUPGIhZCusRDW3W4VWl84DjjNQsfi2q7NS2utWMQnEP4rg8_ZqeEwQmAridD8uRPUKby7NLi-4qpbL_0xydukkIQ6iFsLWlf5JMalToACe6zN-pvecS2uJLKggEDgKrSGb_CbsbEcEuRh9GUOOHyHZy9FGH6OweF40Wx6DFOVGdz1a3ZQqUn41GamgBkZK6quiEkd1B9djJQqC16nK_Rgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌جزئیات‌ عملکرد لئو مسی فوق‌ستاره تیم ملی آرژانتین در رقابت‌های 2 دوره اخیر جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25547" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25546">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1YRQG2FkIxRs0A8uM7K0WPBwGYnihXivtREEAlmnEMt0Rzleyxx1JsbekvjUMM3g1D_fPgP1ZmPeN4JGBnL8VFpTw6v8DEhWD6WHv-LIukVF2IIyTj2-2AN_aRqDyj7fuDuPHZ2aoEskq7c5rnZdFkOgh4yANUBXO8vJ-v6v4WE0yWab-WnBs6MfHe5Xi-6Yyr7FSRNm9OsVUJeOcmDvJW2W6LJy655fbjnYsOjTAG0pljYUwqzcjURnww97p6-vy-2XAGyUUXhn4ctT_arBgd9aN0ncaQpNNiQGiX6veHIJ7zky0zWQb52KuvIMFkjJjs0lsCpK1IighuGWAVjmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اینفانتینو میخواد فشار بیاره تا جام جهانی ۲۰۳۰ با ۶۴ تیم برگزار شه. و ارژانتین و پاراگوئه و اروگوئه هم یک بازی به شکل افتخاری میزبان باشن. مشخص نیست فقط برای یک جام میخواد این کارو بکنه ولی ظاهرا عزم راسخی داره که این پروژه سنگین رو در سال ۲۰۳۰ انجام بده. جام‌جهانی ۲۰۳۰ با میزبانی سه کشور پرتغال اسپانیا و مراکش قراره برگزار شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/25546" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25545">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXNEgaKKyDACKqU4tgkpG5YzcTBeB4dPVeH8x5BDvF_Q6tzqF1wso8Oj9vOIK2LOcA1ZSqAeLatov0UrVK1LYXM6s_NydzEwTj9LwlIZC_q9e2Kp8hBs8jDjWNBKWDH3hBBnbsRzWQ4o7fcoosDS8y9Z9bAkKMJCku5gndgUQs3FUv5ureXroPTSr6OetmBfaceJ2Ptswr7k6eKG8YC4hNQ9gA02_ghEiWit-AqnnMv48NUSV8YwdEgJ62KIPXnUfYBCb3mC81wiQTX_5dbhIb_FHl3IWsIVqUMDzworR-IHSfgVuF1qZXNdwanK6hnA4UFtXLv_HLqL5S8av7B_Tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/25545" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/25544" target="_blank">📅 21:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25543">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY2FGKQBNHpJtxLsMxLq5N_D5mc7yhgOCexPviESN0L5wZ7h568TXZPn5OefyXglZRtmBmPrQlOzFKdeWgvqHuBj80PkvuECVAVhXoxfucWq_uCRvxK4DVz6iHuEWBBZ1daJZfr-6OpXwfmNphgiljyLke0AQzBCgvR_4_TpbGIWCgkXorMy430eIj2eYyJnfdjwtq3j6MyRdvN75C2roHGfMhGjZPCq0t_gwC231tavb-jB-rnQO-kvND6u5TvZ19ZvHTMQs31UEK0Swi4tWbKcc75dKb_rmCdyPwaopX-CxG9OfKVo45JM7kxh4MrSikXdGIEil7rwC1UyNqpgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طوری‌که سورلوث در بازی با انگلیس؛ نروژی‌ هارو به فنا داد؛ وایکینگ فن‌ها عکس رو میفهمن. برگ‌های هالند از خودخواهی سورلوث ریخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25543" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25542">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlta18X9RDKHdT5ctvHdXHZJeYtW1mCawL4hLOjuDMo9LApgJ4k5gLa84SeBnniJ9I-lN8s_D9klpmH_va1ER2us0oGdGDhLOxNdD_0eISvqduxgftTuMRhZxRcUcbeMuVmM8wtDIlWLdyz_cHnZVCi3mEyxBKBXYKjd7lmPHY24eTy-sP0ivYXHe1e3UEz10Sysl9XjJ2puRxa9lRorR7WeI_LNKgH-asqqyYATz8B9HB7ccDDWc0vlTbB_65gqCc6pYayqLIt2UFtrHzrGJrq4WSZv-Q9GvbKhGdhDJWsDZT7pfaV2OPyGFmArX0WRQwxdZaj_JtA0ivg4CeeHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو انتقال مهم امروز؛
آرسنال 20 میلیون یورو گرفت‌و لئاندرو تروسارد روبه‌بشیکتاش‌داد و مارکوس لئوناردو ستاره الهلال هم رفت آژاکس؛ هلندی‌ها بابت این انتقال 17.5 میلیون یورو به الهلالی‌ها دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25542" target="_blank">📅 20:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25541">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/104d086276.mp4?token=JLoAyFFCLKXF6R5VT_H7rVSTEVq1IlFpLoCoN59_AGL1LdBgZkqralzYqGqvRpNZ1kJmCMaQfoEzMaRy1u8mX_KcjH_FeYVKmb0u7Hj3CCjRgZCDbzffa2fcBRm0w8sRXVj87vT-XgHo8yv4MaixFMpji5ktMeBimJocaBN_4GlhQEB7I5bdfv8yB42Zpp1hgoHGv7bjgpfEVgxZ8RhJXtv0PBEV7DTL43iGW0dsab7AGQUMaVbxLRF1cl9ErJ9TT8z_rZ--f5W_iV_6KPqzta3wI9mnZ86yUYi866OvpPCy-0-bUfRqS88mGU9HoKDGuIe4JftEo-pOH4ymx4R7Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/104d086276.mp4?token=JLoAyFFCLKXF6R5VT_H7rVSTEVq1IlFpLoCoN59_AGL1LdBgZkqralzYqGqvRpNZ1kJmCMaQfoEzMaRy1u8mX_KcjH_FeYVKmb0u7Hj3CCjRgZCDbzffa2fcBRm0w8sRXVj87vT-XgHo8yv4MaixFMpji5ktMeBimJocaBN_4GlhQEB7I5bdfv8yB42Zpp1hgoHGv7bjgpfEVgxZ8RhJXtv0PBEV7DTL43iGW0dsab7AGQUMaVbxLRF1cl9ErJ9TT8z_rZ--f5W_iV_6KPqzta3wI9mnZ86yUYi866OvpPCy-0-bUfRqS88mGU9HoKDGuIe4JftEo-pOH4ymx4R7Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنایه جواد خیابانی به قلعه نویی و کادرفنی تیم ملی به‌دلیل‌عملکرد ضعیف در جام جهانی: فکر کردی منم عین مربیای تیم‌ملی‌ام که 180 میلیارد بگیرم؟
‼️
هومن‌افاضلی‌خیلی‌جدی‌داره میگه فکر میکردیم که میتونیم تا فینال جام جهانی 2026 پیش بریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25541" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25539">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2qRFCsvvmoXcPcpaOteUXJB0Q86EKl_YlbmeYtyuzQJsWu97wxWzFRnE6KeclpDNEFzrJDMRUlU82eXvi7Jjc2jDSRp748RqKSLWz20jcDs61OQXEwO7hOcbAqZhdVwbXQ381Vu4FrjBFTLejA1OYrK7yceK7KKXdoD0Y7d7bpAUzHNBBzK2PHP3hCX0TA13FE9AUGobxhS4J6t7EnkhBTNi9zO1oUIqcBBXqEGxvENbQ-X2GLNcjYIrSuVguWwf3FTZV8IOSUIdmGMxRyZsHUIffIHIhHZG9apIkP8TogATGOK2eIS5zUqOaqacXDHAo_fXXVxlb7j1J1i6BmiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25539" target="_blank">📅 19:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25538">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmHK0Nv7Ar_sqCUtuG_HRUv3m15unE4eR_WEV5g7n0uIfnA-sDTKa6WHlNsx_h9i9q14YFS5UEExjZIBddGeE_Pl_j7QzIThpn5r7JRi3D1Lre-X2mhXc4x4yGjb2kIjA-C_QCIQ964k930p17jaD9MEbE2DjxwmuXqxROOsmJ0shmsAyjA0-alvQZJ07uV1gyXV2P0Ar6Vak4D6Ar6QciLHG4tJ9waVdzO9mZC7tHXnBTO00Uswo4JSLgVORZkc8RPLcol6CSqCyWdHBQogKlDQPSRjkGuqCQTzB6VNcPIvTXLq_YSmDuQI_4TpggPiH2CZcSNNWVScqttQlkV4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینی در سپاهان موندنی شد.</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25538" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25537" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25536">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=BlNTkQsQs-M7BMVSqdtSnsr8uVIWOqJTom4bHGu1nx_XjpFyeO3lMEMq_U7IY8TCZvjFWs0mqa7XbCTJwNxdI_0AFyFAL6LfSeTCBwWoewDhkZqmHXNDho0eeqerL92q8yNz9_Vjx5CYcSezG13W4RX53Fzy08Zc-fV7yk_4SI-SeVISyBWNXMknzgkDuJpIujA-9CuG27_NTd3mzfP725L9Hp5US0e0zO0xOi-_IB2jqYU7MvaVjJzl0eznh5RWoPA9MT_jyEIDOjx6s2GF1SGC6_Cbwvp_69T2_WlIwxpvoaC-hMSTBLFpioVfWXptq7INoaAVwM-xBZHA4FNcwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=BlNTkQsQs-M7BMVSqdtSnsr8uVIWOqJTom4bHGu1nx_XjpFyeO3lMEMq_U7IY8TCZvjFWs0mqa7XbCTJwNxdI_0AFyFAL6LfSeTCBwWoewDhkZqmHXNDho0eeqerL92q8yNz9_Vjx5CYcSezG13W4RX53Fzy08Zc-fV7yk_4SI-SeVISyBWNXMknzgkDuJpIujA-9CuG27_NTd3mzfP725L9Hp5US0e0zO0xOi-_IB2jqYU7MvaVjJzl0eznh5RWoPA9MT_jyEIDOjx6s2GF1SGC6_Cbwvp_69T2_WlIwxpvoaC-hMSTBLFpioVfWXptq7INoaAVwM-xBZHA4FNcwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگهام ستاره انگلیس در پایان دیدار با نروژ:
مادرم یه هفته‌کامل بهم میگفت مراقب زبونت باش، نه فحش بده، نه به‌داور گیر بده که کارت زرد نگیری. آخرش هم مثل همیشه حرف مادرم اجرا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25536" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25534">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHVBM1Osdcs32c4gYd1_TwttiU6nhkWtAYJQXR2Tam3TbXnVrQpT7ulbaSuhewIEBYKtYShD4cmUX7HTjM2Gl-fZ0pSePrr-Uy_StuPWecrilG2FDR9AMEyMJ3r2V0Ix0KLehRFYZYt7N0Bxg1NgweRN7d_dECKbHA-sGC2ZuTwly0lkYNXcPLFmRI7tuso0nJ0L_Aj2uBVry2c6ELY107sJtMpq--Bx0dVpIXHCeG5gjYtCEydIPc-mOWokGdiorjzjwi8V0HzZtpqELgJZWYDS91rwnvAe4mMikQ-lKodgjn0DJWXrXOX3EwgUZxLiV1biAyAmqI5xUFDXgPc62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوسمار ویرا سرمربی‌سابق‌پرسپولیس در انتخابی عجیب با عقد قراردادی بعنوان سرمربی جدید به دوا یونایتدبنتن انتخاب‌شد. تیم‌یونایتد بنتن فصل گذشته درلیگ 18 تیمی اندونزی‌رتبه 7ام راکسب کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25534" target="_blank">📅 19:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25533">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iyi03NHvRJKZWB8-FK86aXpbipTzw2obiaQerUYCwKWF_PT4sw4072m0MDWEWT150XK31QLz2s7YeiOn4uys3_QllsWU2cGkFelUw0X3pz0QIxay0F9D5a3z5mPrSK4XGXyT5_Dv7scMrVRMiCKkXTyyQIdp50ks76EXkCYI9QwI4KF9R0O0mNXxpuOOb0R7Ws7bWlAc-2OeXcZq_NU6U6CBtBSC39zr6unzb5LhQ9hgUXGeYtKpR0hcLbMhfHtn_Xoz4O2t8zmqXlVNXnZ-s5_eIBxHaxNUnCYF-Tx-rzn_JRFPQNqma5u6vVvxR786VWPYzJrt3M1z77Gtxkf29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25533" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25531" target="_blank">📅 18:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25530">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=hXTGJqEWJ4CmsAnXhFr30iXXUfqRXqVNzZTaiO747OOAVydX7PtpIvtJm8ft8o_nV7Fs4Jj3fQynLUsX3xDVMobqs3nbh0dM7gV-hFn4IWhI9hutV-b8AVA0Of2CD-CNGl7AGAYJavoCDLhrYctgpexwqmTqv7SGVto92ekdFzaAS2RTjBk0tC5yEz1NtmNv0dss5rQ1kW1Z30DrstzBJ2oEwprYPcnJEguZpgDMBkUAKuSkNZjozK2-7qigXhR_Tfg-Bb-NXQBA1GaR44t_346ZLcp8ZHegLTp-X6ayPFGN7pg-bs77RAlJzgkk0B3UDfY0tPgxZA9nHdZhGpXquQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=hXTGJqEWJ4CmsAnXhFr30iXXUfqRXqVNzZTaiO747OOAVydX7PtpIvtJm8ft8o_nV7Fs4Jj3fQynLUsX3xDVMobqs3nbh0dM7gV-hFn4IWhI9hutV-b8AVA0Of2CD-CNGl7AGAYJavoCDLhrYctgpexwqmTqv7SGVto92ekdFzaAS2RTjBk0tC5yEz1NtmNv0dss5rQ1kW1Z30DrstzBJ2oEwprYPcnJEguZpgDMBkUAKuSkNZjozK2-7qigXhR_Tfg-Bb-NXQBA1GaR44t_346ZLcp8ZHegLTp-X6ayPFGN7pg-bs77RAlJzgkk0B3UDfY0tPgxZA9nHdZhGpXquQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسی تو نیمه اول با پینیرو داور پرتغالی بحثش شد دیشب: بامن‌درست‌صحبت‌کن، بی احترامی نکن. من باتومحترمانه‌صحبت‌میکنم تو هم باید همینکارو بکنی. انگار نمیدونی‌چجوری باید بابقیه حرف بزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25530" target="_blank">📅 18:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25529">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=mr2IuP2M0p3UJttxJr5Q0vB1qUfZebylnA-BuiIBhJJk5GbAulX81006LP_K3G2_15RAaYLldK27cKLCH-NaGiQjmUFeZX4hJUVA0QTajclOQ9h2CofH1K-LvASm5vCxBV8C6nd9tMccs5P1gqRFRKz1e4wu_i37iFFFEjfwyc_kmicRiQGYP5oQlDNNkDMalklzGO7XziLuroHXESno5UefK_IUb6bS4UTWZ3iURbU_MuYHNZkdHFwhrkR6JHj1RDhxthnpknOjBhn9GbEAJ04LWSiMqvFFX24xRXAP5USsicKr57lmOf1mtsnOeGTypH5ETS6Lmuf-alqwG6zgIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=mr2IuP2M0p3UJttxJr5Q0vB1qUfZebylnA-BuiIBhJJk5GbAulX81006LP_K3G2_15RAaYLldK27cKLCH-NaGiQjmUFeZX4hJUVA0QTajclOQ9h2CofH1K-LvASm5vCxBV8C6nd9tMccs5P1gqRFRKz1e4wu_i37iFFFEjfwyc_kmicRiQGYP5oQlDNNkDMalklzGO7XziLuroHXESno5UefK_IUb6bS4UTWZ3iURbU_MuYHNZkdHFwhrkR6JHj1RDhxthnpknOjBhn9GbEAJ04LWSiMqvFFX24xRXAP5USsicKr57lmOf1mtsnOeGTypH5ETS6Lmuf-alqwG6zgIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیوزیبا از لحظاتی فان و با مزه لامین یامال و داداش کوچیکش که این روزها سوژه رسانه‌‌ها شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25529" target="_blank">📅 18:17 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25528" target="_blank">📅 18:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25527">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
تو یکی‌از خانوادهای‌عشایری یه دختر بچه حالش بد میشه، بعدمیبرنش‌بیمارستان تست میگیرن میبینن باردار شده؛ میپرسن کار کیه!؟ میگه پسرعموم، دعوا میشه بین خانوادهاشون؛ برادر دختره که بازم زیر سن قانونی بوده میزنه پسر عموش‌رو میکشه، میبرنشون دادگاه خانواده عموش…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25527" target="_blank">📅 17:57 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25526" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25525">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmAHBY5sCU8uBAqN538y_CH5Up0j0uNrulI0dnlK03greAV1Y89HhPaNDBisucl9YPLlkH8_L-PE4BmV1uFCOi_6f6_b0QigEhufJGKl9jEOaa3Yyh-XsIS8EACmxhpqEmyKJo7ZiBFt1M9od-2pLbMV_5iYHRekYFVwRxQTwMurnmiMmnoxAGPYAJZLUCWjDRnzBqv5ZcI6GfUxgRTg2FmQ2lWN29nmNZpm2Q6wBs0ptG5TcmJakirjah7vnJJUkcSMbs2CoNF2gd0YiyWX5ST12StOnSp1ssHY6xu7ekHzxOtgcZ_hFCDcW3d49uomzAqskvTyktI1RewWe7RcRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25525" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25524">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqOZU71ORilO7d2VasL5btJ1pauFafUYnvUQLJk2Q12KtmD7MF4T96qs-3JeiYMPTFLIqY3o-eZT3q3orEZLcZO0Y0860fAS5-jialIX5gRaXfstRDmFv3IhcePuA28Il20aIbIX_OkDfl7yh-oNGs7mmMT9oY2FwucBXWhLfVQSuyu75vOVut265YTcEA9Dg3AYsW4UETmaQV4YmFiuph7RTmTib5eAjU2i5GF3jDO_E7JiAgv1cHSiX0VFHtSbpGEHYtPhYWMzn_eFIFHCZorYyJzfa24FeW6wkqfj-8dtdZyvNOWZKs7U6MPUqchr-N4O4stu6InLcDkLag8Rsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
عارف حاجی‌عیدی هافبک‌جنگنده سپاهان که مدنطر مهدی‌تارتار و پرسپولیس بود بامخالفت شدید محرم نوید کیا در جمع طلایی پوشان ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25524" target="_blank">📅 17:11 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25523" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25522" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25521" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25520">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=tjcjuH4Lc8k18tLBYE4SVQ_NPd1NF2UaJIMS65ej7DHy5cjivp5_HFeVRmrBQ4WadVRgMu5khnrIvbesHpMcsYzlTaClPs3iXimbCsH7r3eCuM6DexWKn3XSP63CDLyr8ChrZxaZ5lVYZUVwapUCqnvIoZJmBdxDInso4nFRS5gpzJERLsxPPkWcc27OWQnwFSKsbt-gMPztpmTo4SFxVQwsGy71pk0ZBCPdxACFctq7YU7mJdjsKJZqPG0TgxZGiAPpxZvAGDdjiUoA6Kfw_8DH3MA6FVKFnTqBv3mF0hQBT87XObCASUJKGyZNyYOA6lsyv5ZYd-fydKjCi_3GgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=tjcjuH4Lc8k18tLBYE4SVQ_NPd1NF2UaJIMS65ej7DHy5cjivp5_HFeVRmrBQ4WadVRgMu5khnrIvbesHpMcsYzlTaClPs3iXimbCsH7r3eCuM6DexWKn3XSP63CDLyr8ChrZxaZ5lVYZUVwapUCqnvIoZJmBdxDInso4nFRS5gpzJERLsxPPkWcc27OWQnwFSKsbt-gMPztpmTo4SFxVQwsGy71pk0ZBCPdxACFctq7YU7mJdjsKJZqPG0TgxZGiAPpxZvAGDdjiUoA6Kfw_8DH3MA6FVKFnTqBv3mF0hQBT87XObCASUJKGyZNyYOA6lsyv5ZYd-fydKjCi_3GgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شوخی‌جودبلینگهام‌ و ارلینگ‌هالند در حاشیه دیدار شب گذشته انگلیس
🆚
نروژ در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25520" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25519">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIju2VvZwC17cvRQiN5LccGqo2XO8LNBFOfQTfzDJ6evqqWflLOOapQnBusKXPpIhcHDYbt2w7P-LO024zKiYyXXLtZItDN9iCqBHVArwe_IZvDejyD8uIQxuwxNBhKrvqwjj-68slifVl3Uxy7x0dPlVzqcNrKhtvRamfRBu317uvssvEfw4IKeKZ0G5UNCfPwoU7iF04g6rBM6ZK2TvPL3FyIaj6Gg-opISIl9Kv07fIfZAA3IfDT1zzrpt4qqkYyCZjSdPmF3qZLxuyyxj6WCkmLVIyPa_dFaAe5ie84fvvP1ID_7BQkq99lDOJNXd13NGIKzuCuCes74xeGGcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25519" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25518">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVzxH_F6b7aQ4Xf6cbXlbYUwukUWCxSQPpYMUPHknGDU96rFOwYuVBgA0G3zX-3Lzm6GD9RP0ZAD1kBHkTo7CHwfenW8pa_6b4J2OMJjk-4_qE6kOfK0bdbwotPCa2pquja450XIycZUAmN0bdP2vClfbLrLwNooH0YfubzkESz7bI9Mia6S9lCa2TTMM9RLI79Pj723l76IuRFUKkgzHwOr7b_BwGzZyNo_5jhFFieTiQbHJcE8eMaIoeznVz7WBhZCU_T8hoNbVCirypN-_Hu-NrMLZgRlGITqwur4bTyJ0ULluNxKyqDA23bKmZpVCyKSOTCHWHWXYuAjR5Be-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دو تقابل جذاب بامداد امروز مرحله یک‌چهارم‌نهایی رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25518" target="_blank">📅 15:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25517">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR-Ya7jPtEVUDY_6o7KAptaCbjNhVifM2rkX__-HBGjI_sk2sAzjZxBapvG9_lKJdQYfaSaThkEh1_5RXInbifakPw10nx-yYCSCuEcBnQIX4phN5a61f-Yq2pCjQbJN6KsKGaoY8gvUW7k7aWteJkNhcgOr-LcpYRu8q8AecHr0ePN7w5Deu0W0lp8xNh0SBm3pzgCBnKDlx46E5DMhplmOnYuxaNWbwTZQ6VPyXPY8HFVHMDG2FmdSS_Z-zjSe58KYUuhx5cLdHDH39PauFpUZbDOH3dOPfanJOvEcTnkQ4SDSWBot8XDVwj9vhc-iayeD5HlwOJ1HrJgHFOXnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25517" target="_blank">📅 15:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25515">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25515" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25514">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxxyI1NFdmb5CRwYXr8kEPFHKQ3vZ1O4OwZNGmMra6j47ohzueE1FqQP1uSDNdEdFppxHJ1iLdCALZ2T18EtOAEDvyt76tAmkwAzBMI1WrDGr8HnGNge-mIwyqXhhKnKEdpRxnr4agSuYAOVVOVoadPezzwrJz8ZwL-2GRu3P4-Rlcq8SxyJD7f0LrIBBZtQO20tsUcGveRBsy6tp6aCySMJAxk5AJDKQcfGe1X5w1besPescAhTBZyj3EdypT3gWu7kX8rg7JdTfcDs9KbTRwhblyQHzXv3fsDdBaOEGyWpcRTkwDHTpLucaP1a8Q_3gN5Mvi8ZdA05_us_yXDO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا
#فوری
؛
یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25514" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25513">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJEcZCCrArsXi-lp5O1XXfm5O7-hCnrcwarc1ULSePKn0MNqtfG2MOGaGS_X6BQtHApRi-vYnpJtNplsprBgW8ssj3i6pT-jLP-uldbtc4Ttelx8_XlrXYyRpt1FupNv-d9aqFNu8iemGLLm1uR-1W4Yar7v-6eQJj_cJSZ38HgyFTjs1gfyRe0nwOvFdmWo3NbcKJRvjJqU-p-_Opz7dPRUCKjqzMtSOkn0K1k83QdweLapirqX-6ncuDOrz4aeeKHWu_iJl70NS23VF9bJLasrQ4ddRlazhhOT7mBGQd92tJKuPv8vVVJYGNYANN1hzhB-Ue8vRo5uV4LGNp7tKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25513" target="_blank">📅 14:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25512">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=tfC8rCml1H2yIADf4I-95yuaZr4SHxjaye1S1TSPr1vLDn3o3TKvp0VFBq8yQywsaXXFUIPt4GnvpysNisy1H4-ED3vIWKJKpfHGw0OR08CjQBNxcShCGCTImQB_IEAdbT3ONE-qE4_ShosiTYWyCsQP-ljFfADI67pZCXFgFc3JzCnkaVocyGfBGcngfx60OX3lmjuAFgaIIIFLMI2ojTLjbgVktYl1FD-KcKga61sIAOum5fRO2MMAiPoR6bG5UR099vfQFzHYTMTJQGFzfnk_XaIAvhcBRg2gzrnITIcs_HpGUVCDyRJoVrV3aRD01WuAPgLKx2K9u9I28sKfKFbJZWDUJ-vdKTgpPikI6s3MvJrDoGyHz4hPkkSidCoaWKd6DYIz_srnt7rqZITrAZyX3WzO2HfcWpOnNFzlCVTw7vEJpEmFw1JonoIC8nMp_W9h05FdEd2k4lPLgUHQ2FzfxsiFjlHW_ZfaRUNeB_7pOjwYBWrSgKwqyL1wZCwlx6mgi15A9NQAL21hKwwXl-IYoPuoSa0y-8VIFH40G3lSTbNU4p1W9sIljmp1t8M3z62R6tWJUE2g5Xz3K6snm13zD-k6LbFJLjpbI-s6kjmsfwLiw1MjiVPoW99BBMoCazy-fstbm-Ta4DySfBpzERRYeIbFQ17e0Yh-Fy_7GH4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=tfC8rCml1H2yIADf4I-95yuaZr4SHxjaye1S1TSPr1vLDn3o3TKvp0VFBq8yQywsaXXFUIPt4GnvpysNisy1H4-ED3vIWKJKpfHGw0OR08CjQBNxcShCGCTImQB_IEAdbT3ONE-qE4_ShosiTYWyCsQP-ljFfADI67pZCXFgFc3JzCnkaVocyGfBGcngfx60OX3lmjuAFgaIIIFLMI2ojTLjbgVktYl1FD-KcKga61sIAOum5fRO2MMAiPoR6bG5UR099vfQFzHYTMTJQGFzfnk_XaIAvhcBRg2gzrnITIcs_HpGUVCDyRJoVrV3aRD01WuAPgLKx2K9u9I28sKfKFbJZWDUJ-vdKTgpPikI6s3MvJrDoGyHz4hPkkSidCoaWKd6DYIz_srnt7rqZITrAZyX3WzO2HfcWpOnNFzlCVTw7vEJpEmFw1JonoIC8nMp_W9h05FdEd2k4lPLgUHQ2FzfxsiFjlHW_ZfaRUNeB_7pOjwYBWrSgKwqyL1wZCwlx6mgi15A9NQAL21hKwwXl-IYoPuoSa0y-8VIFH40G3lSTbNU4p1W9sIljmp1t8M3z62R6tWJUE2g5Xz3K6snm13zD-k6LbFJLjpbI-s6kjmsfwLiw1MjiVPoW99BBMoCazy-fstbm-Ta4DySfBpzERRYeIbFQ17e0Yh-Fy_7GH4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اگه ایران میزبان رقابت های جام جهانی 2026 بود؛ این مسابقات جذاب چطوری برگزار میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25512" target="_blank">📅 14:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25511">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1GqZTzLYAB29LwoPZqKleQmJCugE2ETXlJRKUOj4rQo-kdx4F1CeCeJ7rQZTaVjsMVhf6_yKU8CEIyInlbo41gMgb-W_z8ftIV1moLOCbHZgQhXtMHZBhJVfYSkQ7f_S0movfNIfQurTIz6yEo-6Y8Hgp7QnTflpUUe8JPA51mtkIS44eO0EMRU3CY9PIByq9I3mpirmP6MRG18aPES0r18hAIYeCaIoTPKASRzTcVwJsqgZUKGqHLjA6TaaKxJecILKUTm_YVckuJjxxUCQlX8uy4KbgeqS_xKma-h41B_MJ7nT8pq1slyDujsEA2pzFTpss4iSL6E2s1JfruRkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25511" target="_blank">📅 13:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25510">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRrY50AGh9ZdNt4wH9ZuxikDEqo-LDRtMHQC9hsS8CgdQvC-U0FMY96mylf_VPWRPBOlUDYXNHa0EwNMD1ZGtAky9j10yUGNmohCpt1v_0wFDILtvSO3PUwTCKdMUaphA3qrDdOSs4vqSJinIQFPyu22ewTh4j0QvU-CI4r4X3OQNYahYsJcLOYavrec8rjY901ZiE6e2IxuARsQLoY5LdU34Xun1EnPZ9yAvrNblkv4ZoL22TG4X0fErR1qqGZhTJpywptcFnUKE4eclRofYWpBzMiD-J8hUaueGaZyDqISSoUjnarnkqA7tdQbtM4TDbhRfY5dEn6eQx1fOeJEkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25510" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25509">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqbU-IHSJn9ENr-j-QXx6duAx31ritP-uGt8GCCkIzsWocg43eZTUiE9SzzVc7dkQUMSBErZXtkjdAcYlHE1Wk_4fihDpNsNNwi7w1SErnZqAqr3EC91KxOlXIsAAkZWPFDXCSbMJDfsBCPaxVYtNR1g4KdtKBgN-xTdr9bHv8tjJCgtPK0ZwWoCjXMJhKTG-3Frk3OijOtIBXEWXwJrNs3syTRKQjqtxhCwexcGWmvQnJR3PptMm11chBwEcZXAsiAshM45-TvAHfR4J6pBQnH7xQmTYsSwXXiyY_EmYe7vSygqS6dy0wxL2uMGH9QVCP_GNvNuWrxlaeGW_IRBag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25509" target="_blank">📅 13:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25508">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGieeKzNU9ix2NcSGt00LjOqA3xvtHNG7wbP-IqEJomopKjK45m6rrffVVw2v-H0reED28Uhp69z5oMa7UOnvmfKzqzQRe2MUfzDcvd-ENnCqEDePfc29__xPSi0cxm4baxsCC2A2Qw2KhsZQSRUBL78oq4DVR9KcPy4KOW_W9vzLW8xjNoc0okI0TbhRhVe9GjTyq0I9DB2oVXkJ2QZTUNTnb_hA-tUKiRkkplAb-tmw8Zw7NhOEeWS4sUT_92DxnDpCKx99AgacbHSbVKw_dW11p5AjcrG1fEJcbeacEUbFNQMtPu3VIJFkJGqsW00FllrvbW8cwPCVyRGCjU8Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25508" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25507">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVpiGEbMWZ5uNpjw2Oh2EWVRiOxIn0HnB9y_bDq0mZYWDDNQ4nDzjbjThbiGg1iEaDlGK1dP8FPVCAPL3ksbN5VQt1tw3wIkyfn_e3mpHi5yvPwJ70_7KlCRy58C7plIWmPdlC1RKAtYCU-KdnDYg0vKaWW2OAQmJIMJpANsP-eUYTVNiu9IvQ37uQS8rHCUP2hbHyiLwq_XNh4I-L5QvFS3uG1VFM1XjH-0qwGvgH2DWHObbsM2vDsd8zhGKDxxqiKE-euer2io3B_RE-Vj-gQ7TT92SVnDlhIlYOUadg9wHvztkepVhTq1sIhfv5oBGOc-zPLdYQ0C4MIbK-6KWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عادل خان فردوسی‌پور پیرو خبر دو روز پیش پرشیانا؛ مهدی ترابی برای عقد قراردادی دو ساله با مدیریت باشگاه پرسپولیس به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25507" target="_blank">📅 12:24 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25506" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25505">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=SCPnmcAGxI09AI7CHvxmU-mbj1V9-AyyeGmTTq8qCQA0hmj5ZT8Ito7SvXTXIhINXJOp_qBn77ONSrFRvta2XotQVnFIxNhNNXwRkHdmoqlpczzw_DpHbhpxefdIufCSuF6SzQ9y3az9etEM0niwwGE5tPpCVyjQGTjsBcfhNAD0Y3a5I9Koy57000OuTsPVco0SkiEQ7oJuihRM4rmcPv18kB8B5joUhHqdtcWNmfdtNQVFR0EIJhJgPmQxXiEm2E-SGTbtZOUivJQwLoTGo3rb0ST4vshEKGlDnXaC7WhdhxEhNjdKPAd0qK2OBvhT_8No4Y8fNniVM91Qnm2B6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=SCPnmcAGxI09AI7CHvxmU-mbj1V9-AyyeGmTTq8qCQA0hmj5ZT8Ito7SvXTXIhINXJOp_qBn77ONSrFRvta2XotQVnFIxNhNNXwRkHdmoqlpczzw_DpHbhpxefdIufCSuF6SzQ9y3az9etEM0niwwGE5tPpCVyjQGTjsBcfhNAD0Y3a5I9Koy57000OuTsPVco0SkiEQ7oJuihRM4rmcPv18kB8B5joUhHqdtcWNmfdtNQVFR0EIJhJgPmQxXiEm2E-SGTbtZOUivJQwLoTGo3rb0ST4vshEKGlDnXaC7WhdhxEhNjdKPAd0qK2OBvhT_8No4Y8fNniVM91Qnm2B6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25505" target="_blank">📅 11:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25504">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxxgIAG4VGRYO50pmuF92-gTWYyqV_vyy349QVU3tmG4yexUeKtZtB6UC4ZsYJXeLealsPlf097eoI1iAOGqAfSVMlvgs2xlDjz2MkoTI1omeFQThkuRsYDOAclHRzOJYPzkrVmF9uJSKqQ9BH3I99703ydXpmEI5wtVq8WYDXDWouGw6C9w44bg-B9KchdlfMcg5oMDYscwOe_DAYjUwZ6AHASh6bOSY_R3WBq3uJqHoGOYg_vvqNIYXFySOlrIbuiPieRGXZj72wcaWAhePEcGJlYj0pUNbVZ-YE0GD2-DRG-LXwhLEhQ-jX9oqdQXxXmMEBefQrRo41e6iPJZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25504" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25503">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLVRNglVgnX58Elxo61AqAiQT3v-VAqy0okH1COtHZYNzhcgCST9CK5RbxtbBqmnJacKCRWMS3MBWkQbq-klH8rAUgQnVHGqS4ece6Ov9FhmAlRnziTh_lOYtFqJOnHXQx_-QAGj0RMbePIZumG8hoemkFDrSVpU44hW4QKp171tCOBMrF3FlOCrgVIyLCNfg2tSAEY0FhLXLwuiPBR4r0XCPFtRECOrXc7r2qIOJVrXRV5OZIr5JnBm8qQI0ElbOmHF205Bh7HNzy1GRCcqg8FUFT3naYISkh5NBBUIy-KIY-KttcNFFQUwBjvisCSlSLRmFZjZj5xvOXiNDB28Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25503" target="_blank">📅 11:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=loWw_hn7Z7bGiWz_SZ_5AqroP2Q9t55JLBJptwiFD_49Qx0jsg3MMjClcA_n2Tin9YCNr4l9EVBgYjK3iiVPTl_NZlPY6P7tEmvgsI1vKbw-5ToURkruK6C73gBfnszh8rTPiHleL_nqzDw_PB7a_hlyGOnwZtm4O6Cyje_Du-F77mrbVWPfyUJ-0Lpqst3on8fsp5pElTsRibdFGeoSnTYLyPDWYvgEKKcCST991MxEFTRwpHkNn-UXAccOtmQxzDJkeYN8wjFG5AvzAKH_vCalMR5g-9VxNPJPEfQuqMgxkbaRpy6TJ14o--afgn5KappDy2KrO65GnZkCZ6sFSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=loWw_hn7Z7bGiWz_SZ_5AqroP2Q9t55JLBJptwiFD_49Qx0jsg3MMjClcA_n2Tin9YCNr4l9EVBgYjK3iiVPTl_NZlPY6P7tEmvgsI1vKbw-5ToURkruK6C73gBfnszh8rTPiHleL_nqzDw_PB7a_hlyGOnwZtm4O6Cyje_Du-F77mrbVWPfyUJ-0Lpqst3on8fsp5pElTsRibdFGeoSnTYLyPDWYvgEKKcCST991MxEFTRwpHkNn-UXAccOtmQxzDJkeYN8wjFG5AvzAKH_vCalMR5g-9VxNPJPEfQuqMgxkbaRpy6TJ14o--afgn5KappDy2KrO65GnZkCZ6sFSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
نروژفراموش‌نشدنی‌ترین‌تیم‌جام‌جهانی۲۰۲۶ بود. جسارت‌وجنگندگی‌کم‌نظیری‌داشتن و شدیدا دل‌همه فوتبال‌ دوستان رو بردن. به قول یه بنده‌ خدایی اگه ایتالیا مدل گتوزو تو اون گروه اول میشد جای اینا میومد احتمالا این مراحل رو به چشم نمیدید. من خودم بشدت فن ایتالیام ولی خب مدل اسپالتی و گتوزو افتضاح بود ولی مانچینی درستش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25502" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQR6dnmAaCfRFyJNHhlYTACmV8tbJOepncFCTwayYTctuVXbTd0lsYqZPw2mhNDzEPXmYc10BqZTgHfQLmBWq9zdSROoLgt5H8W-Nk6a4NwOrNpaGALxoR-anYRNBLhoNdOxEFeLgk8RKUCkU6yd3bY5_bS5uggWVZ3ejs_4-CKnfuS8ljOFOP0Kw-KBwyj23M2dz3YldYPH63I-EXHinhIGGKYECTiVpxtSiKr6Bz0zB8nJMiHIPULgmmjnXMD0XELIp7p5nmZi9VoyhVcqVcE-6I2NIpnbL1GLxrH5spJ9Ml4OleMM8K_WnnK-I-ixmAOlWsx9jbObxy_i2z4IVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=EG01hCRXRCeHNJDkSScod5z1JnVVPGypUn_BG9NV4hTKEHdV2V-jlF7GwTNpcyH5ZgXkOb7DxGplalky-DGjzIjCFf17tLtBoMuJD98HKLs2DAoxja7ARippFPtMO7eNy4CKJTbfKKlKpWyz6sevqajvgS1upP8ZehUq8r9yuG9ICIMG5_ijqZ_AMFV1-_4DhXrC-gB8FYnwONyH9TF4PZue6rBVp3DmOHPshe_8tcxhFh3-605r4TuwKERfOacoZexptltYYBmUkaQ1M0gCDnZP_WYFyCNWZqYwxYXMEMyEBhMa7Jf0LiM6WP3dMqDJApujGT5Xm56nIJVDMWYqUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=EG01hCRXRCeHNJDkSScod5z1JnVVPGypUn_BG9NV4hTKEHdV2V-jlF7GwTNpcyH5ZgXkOb7DxGplalky-DGjzIjCFf17tLtBoMuJD98HKLs2DAoxja7ARippFPtMO7eNy4CKJTbfKKlKpWyz6sevqajvgS1upP8ZehUq8r9yuG9ICIMG5_ijqZ_AMFV1-_4DhXrC-gB8FYnwONyH9TF4PZue6rBVp3DmOHPshe_8tcxhFh3-605r4TuwKERfOacoZexptltYYBmUkaQ1M0gCDnZP_WYFyCNWZqYwxYXMEMyEBhMa7Jf0LiM6WP3dMqDJApujGT5Xm56nIJVDMWYqUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25500" target="_blank">📅 10:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eudCk500Hd4nl3I3J07HroFILCQuK_panhG_BWv_zcUSRQV3j369tamSfzBFiW-Ro4vfgi7lzAin3N5T-vNRtt9FZP17Yiq-byeUrJRfSxQWN8csn_aZcgK4qeDb0j_YKDuhlxZU9GIfGO3TLPmLBd7w8lgOm5O7p0oILJ4dR7Ouk07RKGWPNeQYQsO5526p5oBxqMGw9pjUf1xkYoI9-X6OJgimPQeMfGr668xGkrXIq64JiinzQ79Lvoak--_UbMsFi2UGQ8nCQGs5eyUFQFZe8A47qXAyRUq8v0oeqROBox2MxV6pyNKnxZEdKXTQ187ILO0fTSCn4pSjVlGAbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25499" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3oTvLagrMdlLXm5Xc_TOdUlSslxU6r7_E1i2toVOVgDL181e8G_KLtoqjTacK5WXcNeTiEO0XeMQW8dzp8fTTazXGejuFA1TwopC_V1QgY1Ib8xzaeVJFCtlPXWPRHfEO0IUSom6e8XXRekWCCIcnMCDKfCBq7fIG46ce-LfZMq-KReI0wFay9DSD36AzuCTr1uNBKN-Lf9PYWCNEFGFQ-FRngfsioqcX9SjTiQjHwqCeuPEwbHQYjRh1IXKmlBNIEZbUL078Z5YMnlAzAc3ERaiErL6F6PCyOepMstbD0xbElnZlCxQHsQJhU7ChCNFp4KabdldgUbNAQgSUi2xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ جلسه مدیران دوتیم‌پرسپولیس‌ونساجی‌دقایقی‌قبل به اتمام رسید؛ نساجی‌رقم‌رضایت‌نامه رو550 هزار دلار اعلام کرده که حدادی‌امروز درجلسه‌به مدیرعامل‌باشگاه نساجی گفته تا400 هزار دلار حاضر است به باشگاه نساجی پرداخت کنه. قرار شده که ایری…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25498" target="_blank">📅 10:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25497">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=HKGY-gz3qmXrx0Z2rtQdAyxWTGMPg9qVW4BhOHJCn1PjLwlo_kvGH3VODamYvZuMJI0H-gEKAKYf5rqmJNLVfKHcWmMI02o1aCFSmJBFQOidyLOd219ooIOUjDtklu080tgaV6s9Syn8hgGgtEMgXtcrnDZsPN3Rm85nWbhENNZOZM2TY9EcA3ExJagzWYbkUo_wyumVfGH5PCQ1DWAOGiELotwWXY5yTt8j7rxGMLvDL_5xisKzGKSCWUpQoyPbZYwACyqMe5Hpd65w-jJPS-xeuBlWkNssBPLcd5qGZHM3uoOvzLVluJHLBpdhFexEiOujsbqYkrWaRw4A6kveBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=HKGY-gz3qmXrx0Z2rtQdAyxWTGMPg9qVW4BhOHJCn1PjLwlo_kvGH3VODamYvZuMJI0H-gEKAKYf5rqmJNLVfKHcWmMI02o1aCFSmJBFQOidyLOd219ooIOUjDtklu080tgaV6s9Syn8hgGgtEMgXtcrnDZsPN3Rm85nWbhENNZOZM2TY9EcA3ExJagzWYbkUo_wyumVfGH5PCQ1DWAOGiELotwWXY5yTt8j7rxGMLvDL_5xisKzGKSCWUpQoyPbZYwACyqMe5Hpd65w-jJPS-xeuBlWkNssBPLcd5qGZHM3uoOvzLVluJHLBpdhFexEiOujsbqYkrWaRw4A6kveBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس‌جونیور ستاره‌برزیلی رئال مادرید امروز 26 ساله شد. او تا کنون موفق به زدن 128 گل برای کهکشانی‌ها شده و همچنین برای تمدید قرارداد بااین تیم با فلورنتینو پرز به توافق کامل رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25497" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25496" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25495">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=pO_18tA0OfhIBczbc_Hx5uJevBxFp0j9jUsD6-SBKJbqRwWEHRLnv3AQ4q-bu_fkm04VWtJ5A4YkTQowzybP_SorLTUi-VqUQfZJLH4qTvLSI6OeLzxuv6FY9MtQHJYJIRIs1my4lEWolCF5FNI5VeGovArhlAk4ASNGQqHqAn21o8I4ofOTQjJljhdTZkpH-ij6iR-8MrpjhJQVBltBe0gSqALvy_LH01fSYs_SHuQLDvyA-Xhhdv7rAOFhf-8zbDZ8Y9YhpF8CXrx_6lnGZKA3ndAAFu4GWNC0KyZEEWoOXvv2iLpi1t1pcovDCG_9B42g0ErRGD-sF5jS1P9QAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=pO_18tA0OfhIBczbc_Hx5uJevBxFp0j9jUsD6-SBKJbqRwWEHRLnv3AQ4q-bu_fkm04VWtJ5A4YkTQowzybP_SorLTUi-VqUQfZJLH4qTvLSI6OeLzxuv6FY9MtQHJYJIRIs1my4lEWolCF5FNI5VeGovArhlAk4ASNGQqHqAn21o8I4ofOTQjJljhdTZkpH-ij6iR-8MrpjhJQVBltBe0gSqALvy_LH01fSYs_SHuQLDvyA-Xhhdv7rAOFhf-8zbDZ8Y9YhpF8CXrx_6lnGZKA3ndAAFu4GWNC0KyZEEWoOXvv2iLpi1t1pcovDCG_9B42g0ErRGD-sF5jS1P9QAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25495" target="_blank">📅 09:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25494">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efZ2J9i5Q8if2cTzo5aByV51XxDN6BOUv9cr5CL0Q0V-2gJBSOLY6S_rAqPJArHdr3ize1bahhC5XlYfnbc9tkZKFNqSp7cLcZU8RE6X6xr0IGEBwfto5-Vm-bY34X04NEUyQ-O3PUbcDItIrDR9xIwT2vVmG6nVaRJYdjvQYbLtlKorONWRcdupK-dkaq1nKBbfqrK5QZTGoF9dSrmTvnTu2RObragjm6rYiyyewIiznCgzpW80xYb1sjYjC6WnK2hTRBFcOHvjm9XSiwiZbd2OAapp-wUR0lWur_F_6cLZ0caHmyGwashuxI_hGxEafo1cSYjKXWLCVja_zRDPEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25494" target="_blank">📅 09:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25493">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1maCFOJqF942xTqO-Ruogml4njV3pT91WqiBkGhvNlENTqDGGwiqukszDwZn3UF0l9TQfbxL4r-NkhMbllaM6rS1T6PwQVoNl2j0Ico6CBHCRVkhCz4oXiS2JGU3LsdR9QSKJwSEE3H8Md_WdSyDtba6sJEFQsLKZifwmNMmdRJ7Hi3QFhjP4r2I6A0fmIqacce3YJIl6JccZf4IoL-l0bTi7HRP4gWXo8bpDBpVAFK4Pr0z-a05isKjgycD998ZRmDdpsiamv0YYFlPwa4CtS4BLAqspdJqpXbMiZfrTfKYewsf6TSFrcmCrKDXfSfO38BOExJFbtKo4hmEgn9Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی‌رسانه‌پرشیانا
؛ فرزین معامله گری مدافع چپ پرسپولیس بعد از تمدید قراردادش باسرخپوشان راهی سربازی شد و در فصل آینده در یکی از دو تیم فجر یا ملوان بازی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25493" target="_blank">📅 09:19 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25492" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25490">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehdfuG1SlPougzn4G_enlmm_O9BwLydUfmTUaOK--OpQsa_kTg4-lgDbjRRybrl46Mn93mZODm0gNzrWSz0tHKIBqft8XleH5UIazM2gxYYJvZvCHIemoA76wo9rePuGN04qDf6HxVGFRFTIzwMRHGUT4xB-RCcbJKv1L3DkY23vloiVcKfpDg877oVG5Yx3TnHmBESWlvGLlGPH_pEu0O6RTuKZHdRTdSk1lJd_8GJEuT8G1sjCu0LdqkkuAVlfw3qlNLV0ksJuL4QBzILw-kJ3hmIwFC-CkgM0fEC-c1vyF8bLnSR12GxBQ53AuEle7zkDz-HoFL-XshDJ-dOzMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nz6ZowogmndhLXpRWinEqY50c0s1M3zBRMNchYzIQmrdh-Ks1rMVN5SGmMOUdPNIFMoEaZst1s5UJw7nDNUvHaTXTHnxUk4wUtLQwiyrxka2OfyI_USxQGP5nT-MDoj3CEXhNNMX6V3mAassuBATusJoY5wrueJnNogV0pMRpfnz0SeSIZuHk5Lf1kcEKP44WXD48CwjZpzNWbfdxlxNDhY7OaxNyOiubiv3nH4-NW4Jchk7bnmo_9ZPO0Pr3q84wuJsPvp_uX_5h-TjgK8x-scg8QaSlGYXA_Ou1JMW5d_9xkicr6Q6yAOGLmZSUPIPQQpeFQmZYRTEhluhYlF0Nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25490" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TN4KfYPh8p5M2KQk19qWK-tRqNWZ59O3ME3oxvG_hUUJ6XkbB1EAFCVnNioNM2ThqdS9w3Jc0pePKrTkzKqr0lYIeGnsL3riOsYzrkhK2oK1cgi0QTn833W7eiazqusTPI6GdQJmUTjQR6dZaLlYd6WpTYhMyKVuWAaFGDYiWmevhhCxQgxFrM73HWhwhY6WDTCWKrVyXsN8wDJxaf2PGDC7jP2rzgynP-N5WuYZNf3CzPFkriGhFLnbPlqdkfbPgsqWOI-EeOkDctTuzAQYkjg9UGUTJvZcx4nhxu4dnNFkuYa6ocggDlkm-hNA5nB01Oyqg-791rZuTKhvjRWmiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25489" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u88YjfhajfgDT16S6PFjQS6a6lmcdLNBBte_N94HFGglrgthVz3qN-4Yt0xHxMFhKuDXWYS-l2WcGWlHyqegXFpgddPS1lExWzQzG5yyGCuWLApE2NKvhxPUSnZRr5tt9FYgr8dU_Mm5XzhvDlQZvcOzAuVxbPIhoUA3ZwtR1OnDOMYtBCZybUbaos2Dd2l9Wr-MNjAiUXNdcpFvDXOQLZZUuREKSPYBKKE6vAGrSu4OV4IkCLD_odTuo-LEHQcwSlVBeu79SZAUlzYiOHj7rVjFv093f32rqib9pyTIXjSuTO5XwfpeAxNSzBaKvoHgXPogBVjdTqKmiH-JEs_Bzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25488" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25487">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DygKG6ZBeBxsEmw19Gc_DutoJ-3JXDzIyNBqLaC3vPz1s1AshMb3byCo13lB3bUmB5scQjXnY6ULvVpubbZEWoAy8u3g1_TYYxgwqiCOD4mOR0w3LYuXlIf0n1n0mCQy49HeGe_i4tv_Qrar_lrq9sb1MAYufFwgsj4Kc6oYy2pilEhlufq7o4H3Wn5y1K1WNrYcCO7cdFRHZvckF_GPTkcn8uKbH2ULc2jGzQ38Xnj5sB_adF-sw_wz4rGCeHhcaA7KKsPsOut0c827_Aa2kcTvwwKb5J0FyIa7zvAkD5K6TVaLw71mur3LI7a-FpADDHbbpOFFBuknXZHFynuy9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25487" target="_blank">📅 06:19 · 21 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=mH8xnBtvEt7ao6tLNcxr0ugPbU2modO_fAQvu-9LkAkLiUIADMDGh_3JGGc6b6OgecK0k1iIG1L4Y5eE8I4KmUlYab9-qQXLuC2jbGm3Zq9zFwvPjLt5lVSMU8_XzAuEfleWokVGEmGAJXfKEUuYfnrV1ncOHG8uheylgUlgUQuKtE7lrN7x8upgyGNvRC55NkPBXKVrbze8i2QXc5UbATzHNH848F4_ooufIEtlYIGZqaKzIDjsLFF4OuB5bRjghcoLZ62XOON4snciBrjGV2tY8j4uj-XPWQngRjDCjMQsEzZwX7j4-gP3G22Di-IlSuTQq8gy8bpJ_oHvarEqDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=mH8xnBtvEt7ao6tLNcxr0ugPbU2modO_fAQvu-9LkAkLiUIADMDGh_3JGGc6b6OgecK0k1iIG1L4Y5eE8I4KmUlYab9-qQXLuC2jbGm3Zq9zFwvPjLt5lVSMU8_XzAuEfleWokVGEmGAJXfKEUuYfnrV1ncOHG8uheylgUlgUQuKtE7lrN7x8upgyGNvRC55NkPBXKVrbze8i2QXc5UbATzHNH848F4_ooufIEtlYIGZqaKzIDjsLFF4OuB5bRjghcoLZ62XOON4snciBrjGV2tY8j4uj-XPWQngRjDCjMQsEzZwX7j4-gP3G22Di-IlSuTQq8gy8bpJ_oHvarEqDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKACpiDBCo5EcY-TeNP7UNk2Nu6lY7syS8BVtwfiyDKWEfTCVtzaoM_e-5vqSZLNpnIeWQYEGYFD6oXzn3WCiskgfYJe61pvO3dZpyi3irNf1nrT-WXGnqow3bzBXWAiDRT1OOwuOrc4e9O0UvjvU7SVueG3Wz-hUTbf_fet22iJuSLG0VEppLAIpzbzhgNcbegGvcPcYGFY0Z7ooJL9UPyg_BROD2AAq8UEun-ARr8jX-QUKKSPsLxbroSFS5DADyFZ-MlYba1unkxTV1V4TK1EEVoIkHVOuzkFzDvnMwQ5U04rAHx8RZeEIOYFnyw8DFCHwHZTw8QmqxikpOqDhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cROsKOi02WnrAMXWZTfmEkDqENZ7UNsfU4JrRUqODxz3YZKdFv3pHyp5eDid1lMtqBGZM8UzoHVPPna5RMlkpWgpp-spGUK3-Sk_47D94EXR2zYjR9fnpEuz41jurw2ktL3LmdQNYxhNvJMDFG2dY2vyLQavEyOVLMsFDr1bR-vO1CPFhsQKmsZqDFTlA8nUwjrzSvL3z6i11gHkmf_TEZ056P3W-DNCxLRC9ZIEOpGn-MAcM34TV62uiY3Sx6Dt0bgaGuE_P7MnQIBWFEqAvZZrY5ji5kmAke7s6amUyQ2R_VPIeha8GQIGRjfW2KxvukhYRoDFURKVjScNMTtdgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25474" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=GMNOBWlBic5WmsInayzjoJ_y0ubrEf927aTw_OKv-MkXuQ8LqBgDR40xZrVNJGXkqH1oqHTrHqIhjoVH5PRn6wp8eXCFCZ8ZPmxlV4SX2Ixp8f1QwOzp6KGzsd5kjkBCrjs71vru58W-GzXyjr4N8nXiNOMfzVfVoU6jQHm4t5esUZ2kcJJB_IWDkQgnOeEcbxc_BmoSJbYO82CwQwZbBuOOT1WLG6ka0dgyEGs64m7pR-5zWYplxnbBP0FROs06zCn_26QxJLveQtDhW4Lc3AVbPpqidtKidhw0CNDLlIXo3EVGEdam7RiZ1-ijvpigS6vQV2qqbm3ofGaiz-DS7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=GMNOBWlBic5WmsInayzjoJ_y0ubrEf927aTw_OKv-MkXuQ8LqBgDR40xZrVNJGXkqH1oqHTrHqIhjoVH5PRn6wp8eXCFCZ8ZPmxlV4SX2Ixp8f1QwOzp6KGzsd5kjkBCrjs71vru58W-GzXyjr4N8nXiNOMfzVfVoU6jQHm4t5esUZ2kcJJB_IWDkQgnOeEcbxc_BmoSJbYO82CwQwZbBuOOT1WLG6ka0dgyEGs64m7pR-5zWYplxnbBP0FROs06zCn_26QxJLveQtDhW4Lc3AVbPpqidtKidhw0CNDLlIXo3EVGEdam7RiZ1-ijvpigS6vQV2qqbm3ofGaiz-DS7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25471" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXeUN2jRKBAjiytfcOJkr_N_wMXMwQKLY0zGqEZMBWXflfBp1kHC5twfzz0wZ0OVdxX-csVSc1Kq_dgLwMaeB25O-ecCBlkU7zXpftGX_0hyk-GbJ43tZEFQ2b80940WXIUMP3yPsX6WlsxdteJJhjCb3b91ZGs-nGFX-G43CKL-FTps2wIVY4dbKWxuXYf0V46JZGZK6iqC8Rr95NPCMPP_n9saLXGbd3sIKxWrdsy48TtEJrhMbkUHxOT1bEUgcVIUjMR9K5ggWozkD3gdfASYbMwdy-u9PEbpZUFStSJ1uuT-NXIIWrWGNCEOzn9PmWqa-wCGNUn6BbgqsxDQyQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=uKXLBhNsC1sZBHgBdsrf2YTvTLoP6DvFceCnmL72coEzxsVRaPtO4o5betuRSIYPDr-QJodb5bjE3cE_d8gvxVIzhdgwwDpl9KKTNOtvEVeRVs8kj4X1dx8UqQnedssDfi_7KJE4gpR5yTn4-zto8ki_KBXxjiA6De5ZrGCbMHBL5UjT6qLP1cbHIC2eeICsO1PS-v4Ir18xN4S_yv_gJ--oZMoBiMcG93c3Se5fJosioplWoJbQIeBma_TpqXG-UvnEBeOGbjncFMKgq24KPyBsuI3AIF9Pfm5KjQQpTvTGaut89UYrWfTH9uzqoNKNvGBIg6EoUiW53vHCCwq_yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=uKXLBhNsC1sZBHgBdsrf2YTvTLoP6DvFceCnmL72coEzxsVRaPtO4o5betuRSIYPDr-QJodb5bjE3cE_d8gvxVIzhdgwwDpl9KKTNOtvEVeRVs8kj4X1dx8UqQnedssDfi_7KJE4gpR5yTn4-zto8ki_KBXxjiA6De5ZrGCbMHBL5UjT6qLP1cbHIC2eeICsO1PS-v4Ir18xN4S_yv_gJ--oZMoBiMcG93c3Se5fJosioplWoJbQIeBma_TpqXG-UvnEBeOGbjncFMKgq24KPyBsuI3AIF9Pfm5KjQQpTvTGaut89UYrWfTH9uzqoNKNvGBIg6EoUiW53vHCCwq_yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elN3GmCu1WCGqZ4_N9c5mSwFh_DwHkzJMH-SumoR-87cxil1iH5wfrpplV2ZQBtFfB_WyUhqCrC1UxHVJ-pQRAeGVmZRIVR8hoTH_omdsF3-nJUjIPnpdNTG6TVk07NcianJsXgVPzqwvDZyi2DLzHjwPvdbwjYBhersXa8--xvWPFqL3youuc4kBI_CRPqQR6N19HPZptGSNirsRBsX1LLL0Wa0t2pN8G9LeuzQUSrTZbFO0MM4egdw2s0wT3D0s8clij-xznpigc5mWzGVynD4uV9SXFd34lT8j7Ue6OX6ksPq98x-3i9ECKLtLn9wfeJ489Ss09Tjd7InErGY1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LljZDT2aAMCp3S4-KjGtEuI7h_TadkNJpPu8rh4MNrNC1f5kZWAXtrD_LtB0wLwU0ZF4fpdIvjS7cS95StMEzyngmn83lH1kpCNwrkqCM6QY-xeoSn-wex3UJr3un8LGRDXV3FLk3XUPaCq9t4lXjGTz7OQIICy7bMIvXeT7jCxq04k6FWahwovAVA8MCnXqlAJynb1anMO6dtl5Agg47bHRecQkVOAIfIH0BHAI2IRvW7nrt4XHpXePXZgJpEm0cuRER9hVMsq3OBpAVp7HbgjFTwVJoKjvKTAe7p0F8raBrnCCborFmS0_U4N9VyU-hSfP_QtrQ_6O8944PMbs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SggziA5aTAHqelE0B3OopEDGItFKsCWg8dLo76yFvd8b0ubvNl71tc_Z0gNHNMeX9eUiZzqRFDFsp7mzI2d29FYDDSOAZL8l5vGQ2gjoWbuyXVpbrRpf8f4jSguziForS_19vkjN4s1FZp8XXW4GJhENTa35tDmgTWMNxtLYI-xBhkafGPAwWQ1diqkKQD7JAcZO9TX9CHPnWYkbIgidlFXFM784xvzzFmOpbarsho_zGAEQ2fGi4Ed_FCQH2n_xd02x-LGeyWq1OgUNubPzHwWt2-xByWhnDMQ8hmzQI1jrtURFY_EGBdhuLJPVE3WvSqvTiWQskhJE6ByIGng4EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAp7wrnszQR6I4TQYmlC9H5PmTeXVlk07tsmd80PPYUP6cwkitAtkaKK0gwi-P0Ik8tSq19YvCz86YcInf-zsnNHc3FB2Cl4o1S7xX39L0HMN8rbEpYVVTaw6ND8gotNxuh5vLq4egrN6W0TLzAzCIsrS5YvQDMxjn2M5xzIx3rTXtwLx698CbDF7SmROMG4bcpAZu4NieyU2tRK7drxuECW2OkxUSgfo-OV59G2nYXjYS3wVtXKDE3miDARaKdJ--Xqhuc38awN2MVddh4LQsWjD1F5i38bBflV7_YM5ht3nLJIVmkAYgL1pCKFnNONda1x9s6_UdBYuw-DLjzJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تقویم
؛ 12سال‌پیش‌درچنین‌روزی؛
بارسلونا با پرداخت تنها75میلیون‌یورو لوییز سوارز فوق ستاره خط حمله لیورپول رو بخدمت گرفت. آمار سوارز در بارسا: 283 بازی، 195 گل‌زده،113پاس‌گل، 13 جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=lyVqoNCRQKRGbr2-JlkoMJSNr4XiyCDjT3lLq8cVcXFWasuaH8TbrURJGEpTiJk9l2ov-0IUaO4M0JqZ6Hd-YANQ8G_h8zRJGYStPfH5Z2Y3lJRBAIY9shBM_MN1aCg1uhw6ydFcBvqa8FcMU41zNKfmOEGQXu44XDs3buLFtvLGQ4kSiF-xaKIL9WofAkebGNFA-Rf1tveqIvZ7NUKmedRZrFDTaEJviYKmhN2D8yyYJWEOKSPv17tYXHMMeKRCRs2QzLD7M3nUqToRQ6Q1zoVtUDNlTT9oll9jAJdh3oAOE3mfbS9q4asU8OLqi0IgS3WR_rTK15wJGoGInK0Y4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=lyVqoNCRQKRGbr2-JlkoMJSNr4XiyCDjT3lLq8cVcXFWasuaH8TbrURJGEpTiJk9l2ov-0IUaO4M0JqZ6Hd-YANQ8G_h8zRJGYStPfH5Z2Y3lJRBAIY9shBM_MN1aCg1uhw6ydFcBvqa8FcMU41zNKfmOEGQXu44XDs3buLFtvLGQ4kSiF-xaKIL9WofAkebGNFA-Rf1tveqIvZ7NUKmedRZrFDTaEJviYKmhN2D8yyYJWEOKSPv17tYXHMMeKRCRs2QzLD7M3nUqToRQ6Q1zoVtUDNlTT9oll9jAJdh3oAOE3mfbS9q4asU8OLqi0IgS3WR_rTK15wJGoGInK0Y4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛
جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
