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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 08:01:41</div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/25567" target="_blank">📅 01:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25566">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nfa-oitmz525IyDyuTHT9vpUomW5S8oeumiu3-4De7AeadTNFiZ2UprMoWGPXFbpw2YYI9fVQ-vAjUoVhscx_T8R26qpDGLpO2CQco7DcVv86KAiU4FYj0DEkQD9ebR8YcCqCEYqHkDJgSwMuqoPDqLgIgj5Aj4Keb09SRrMxke0QRiZS6C_X5KawdyazkIoqR1D4GpksZzApcfrzQTa7B66KYlEJDlfeNcNOnDLzBfK5_xKJ-N6uyr8IUZ1W0IvtHpibXwTopTrHOuv-p-bDdzgrzvGlKx2srP6Gk4ga6J0yGfaLtN1Zr9r51Ctse1PC3gF-n08UKZ4xH3m7MqU5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/25566" target="_blank">📅 01:37 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/25565" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/25564" target="_blank">📅 01:13 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/25563" target="_blank">📅 01:12 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/25562" target="_blank">📅 01:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25560">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st_ALKGkmD7LSHU7rB4kgY9G5poPloIEq1oBtJJH_Qi0Ugnie-9ftSlO_E8pApzBlXbh1XZZyUaqlCTesWOHE3_L-adwJXjnJ8lLeKVdHztKUzuywiu3Z4AD5JI8p9ZtIpThm_5K_0wBhQjR-h4bQbsEo4yfTlgNmaXOr5fPjXOgFbr4-aMVeuiXz1qjNDuOBEllmmXACiG0GCBTeW2W0zDxeIBufFXNEXuM1umkFuhAkGZqtUpOZiGbnjoRUIY_3PF0roRUyMXeDIqC1gwr-nUEy0KWGF4PQmf4Tz-HrTx62ftMyk4Oy8GF7weDH7xefhdWc-wyPARqbAMXhn60HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فوتبال ایران عالیه؛ خودِ بازیکن هم نمیدونه دقیقا رضایت نامه اش برای چه تیمی صادر شده. میگه خودم با پرسپولیس تموم کردم و داخلی امضا کردم. یک ساعت بعدش‌مدیریت‌باشگاه نساجی میگه ماامروز دزدکی‌ازتعلل‌مدیریت‌پرسپولیس نهایی استفاده رو بردیم و 800 هزار…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/25560" target="_blank">📅 00:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25559">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIcOzAo93kW8ifsGHXXAp9PGkMKx1BqRdOq6bbprvB_WCyp_Q2eZpzLLcN0ZPoIeVxWmp1u_GUuGa7E1gDn6ukPYGgIxOYnOSbIKF_XYwTE6AYa_Ssk4bkOhi2TnBUWE2e3RrXwM3sW3w6tM0J8vYb35C49hLh6LRNkZnUTvXWiLYxdEcjbvzSQLYliKRCUidbwYqiBQtYFgTmXNAXjz3jghfSImCyktqsvG4SL7L8m4x1gGplyvy-4juuFRwIAMZxGX3Z3cg2xBgBvzii4F_7nLmML2HcedMSK62pjCkUDvfJEKPhB8O2I-TBy583VRgUn2HzhccY8HQj04aowTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/25559" target="_blank">📅 00:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25558">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIJnXuks6_U-lN_uLyJNSdZUyisSDiY9LMeI8FhkHBNcIREgLVuQTorSumM4C4cI9eTehMZqUvqjxq8VcP3zA0YufQV_C2Wqy-tSKtuE-NhMEKmbz2q3kS1Ljtalq8Di-TFLnkjpImcluR8dvmiG_8TWhhQAxpda34ti83d1ydw66F3VvbV_XUXuwHHBNGLJDUdCBz7gm-8TsahoVTMFLGPGuWXXRIXbuDgaXNAzDt0qlRzXhCZaXHJBDG18WmZ4p8QZJN4Gb1QLkJ5VFfymAqAhbUMBUsMt1LO0zxx-_8quv5AA3zpEmfPvqedMhY94NCEpA5KWN5UECHExvs0rkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/25558" target="_blank">📅 00:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25557">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpJPnXdQ8MxpFGAtp5BPVEvC09GXYZ7MTFeJmInBe3LW8KfGMr53k6GUgFiW1hyJaML3ZLL3ZebA1lmxE4VJrtjyqzi_LG10Bg2lOoteli2cDRDRRYAmLOrzLKzSTsj7UhRNzoujaQdRjAA9YE7p-d4woABlVIUW-Wf3haLWF_zz63ZrYFT8aAHe_fyfft_uS_DQBm0f2TjSO-UcbGibmtudCzElGp1LPfYXp9cS_j4p6bbC-jlNjPUGlCJmCzBdNzhTYAdKhr4BQPb6G-og4NMglFuzMOovavDflxojewupm-v_55YlPY34h6EBsxk5plIB7Pbdn-vWrinGrTit0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کسری طاهری مهاجم جدید پرسپولیس: ظرف 24 ساعت‌اخیرکارهای‌رضایت‌نامه‌ام از باشگاه روبین کازان انجام شد و فردا باشگاه از من رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/25557" target="_blank">📅 00:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25556">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JynSYoJJOdg4vnG_LXmMQX08mHqtq2MpH3-7Y5AQSChdTcVRP3CXqvQ4TnQhk7GR31Ro7mJil-WnzkZTQgMhPbcY-1XMD0lfFtK3SJIhSyx1JhbfiQDBZQastgd5QlsQUgThcIewd7D37S9cB7_7V3etsfzPl2tYgmhQmEY6Ugu9aqm0XOFasI5xuwBT5lSsZjSGDM35p_z_stqQcp3SgOkzCrWaO6G5SfcaVtzhbLrpwqoQP0CgZdtVrTaTVc2X2bZDLar23wKS6M5tMdUfFOrIdRTWyeuD6b3vpTsozJmhkObgvbMzF7RSdb2YO-YbLy5jZKyaOyFG1Y_JKIRpnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه‌عجیب‌ زیکو بازیکن تیم‌ملی‌مصر:
لیونل مسی، بزرگترین بازیکن تاریخ فوتبال است، اما بعد از کریستیانو رونالدو و راستش را بخواهید، حتی حس نکردم که لیونل مسی در زمین حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/25556" target="_blank">📅 23:59 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/25555" target="_blank">📅 23:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25554">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDzh2d0ypJFhMq5CuyuyLhCQMe1LmZ2dprUioCnyhTQ9Bw_3gZIIsuXB1lRJ9mv3AbOhnGbefttGCj6RbmW_rYV-DjLTT4IxE_VAVDtk4X0LxNEx_pLBJhndaWA5liX1DJ2j09W_fnA9EXJYegfDBwtRMcwCG09s23KCkay3HpjmuYPdIVhJC0RVyva0rEVVNMCunc9n9mbjiD6wfcR_cl4MYgxsCwlYE8hgcfxy7xsymKa_DmAD4oOFFF2XAkOTIgQY6qYrtiwVE7KmUMheN5SjRuLnLpArKvoj9xSWK65sO_uxW6s-CNqW_oPRoPA3uxdxfvmJmHj6YTTdg4IGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
رنکینگ‌شش‌تیمی‌که تیم‌ملی آرژانتین در این‌ دوره از رقابت‌های جام‌جهانی‌باهاشون بازی کرده؛ به هیچ‌عنوان‌نمیخوام‌ارزش تلاش و کاری که آرژانتینیا کردن رو پایین بیارم، اماازحق نگذریم آرژانتین اصلا مسیر سختی روطی‌نکرد و سخت‌ترین حریفش، تیم ۱۹ام رنکینگ فیفا بود!…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/25554" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25553">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQMammMSGbIEN0zu0eXYpe7mH7S0vEW6UMyjsJ0OUsxHDvNoOEjdtKa7VQkw7VABwUkpQoFJDYfnizh2IALb4a8gB-NBY6mjhG88bCab3Ijph7Tw7d98NpmGklarHVux-Mf-ejh6HVDAclM7nK3fLorfbEIgRWKYaZIqBujmTQGaiOm14CEGC--UQiMW4FsrSfuLPMXFkgHI4hrT3lS5vxpViIr6cR4-GTd1Sakc_2YYpNFvfT6FEeRCMAxzXf01cl0Pc4UUimzMDwftXEIUttmXTJIYHujSplwaIlTwU9NpRPWFX6eN9N7CuhP4rF2TpxDsBYVVaMwv5UAiEMDAwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/25553" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25552">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcFgNrvzTPws02Iigu9fSoxh2CHi14cV2aZbNEV3SD_a2zSIoKIyMkJe0KY8UqyNzNANCGpC1atT64hd2agJEPNrmTWjyz5FOiErYcHmQYNMsA2iLfiwyHlD7unooqQ6Qf36I2uZuOIhesPnmvERJaA4IpDSvvUjOeqpwk8KbQ00u_nFvVuM8p0k_L7PXfmlNOXM02HTSAaeMTNb-Oc2qQAsJ7_DkVZwM2xwrRFA2hHF999ZMntBhTJ12-Xf3JVQQpWSm_2gXhsdK_zeT7I1pXItrcopaJFmyYqCpAv3n_iBg2y2ARiz2gjOQKxRvlQ7sPCbGD6iqFoY8qfsp8MMMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛ جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/25552" target="_blank">📅 23:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25551">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">📊
🔵
عملکرد مهدی تیکدری ستاره جدید سرخ‌ها در باشگاه گل‌گهر سیرجان:  ۱۳۰ بازی، ۱۵ گل، ۷ پاس‌گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25551" target="_blank">📅 22:49 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25550" target="_blank">📅 22:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25549">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu5ai3V-NXiQ3DUxdCQDTPMi-B7QzA5GiO4nUGtYoOiJ7CwcBSWVMXLR3JlVKa-IZCMbfDalHWOYeim-EQP5zW_26v6n8YZdudJRXbWozB26mIScS2Jngo6rG5OzzyixoNu-ZjFYeVPD5XVzc5rQBxg8AuyYGUKHLuWFK6CjW6m1MGrWxBZroLkPk6N23QeNrapwIK3i6Y6rQBw_xB_t2YsAVoGLVjy3b2K5FsyVOEnvCW7oxwHEk_uTK6380j38nIyV9JGl6q99wBQ51jEEQKHUTJgpMEVN57ZZWyJllHPG4_IEHI09IUfEr5uHWL5n3G7z7jlu27vYVX5uXWiByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس ساعتی‌ قبل با پرداخت 700 هزار دلار به باشگاه‌روبین‌کازان؛ کسری طاهری رو باعقد قراردادی یک‌ ساله قرضی همراه با بند خرید قطعی به ارزش 500هزار دلار دیگر به خدمت گرفت. بخش رسانه ای باشگاه بزودی پوستر طاهری رو منتشر…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25549" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25548">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfD-FvGdc7KuBykd-fFXj60v-5Ei7lttpgpdTHGrbDqhsqRtgtEJdqupnK0R0ahhMs6kt18EUiocnL8_XVm_dmfRltYXhUZoXEYrYsx3lrp0fV11Bf4zmIsFre47m5nr2ymWbEXwviUdGgy16-EgxtVcijsbzdFpbdT3gPRXVToN8S04tpcnyI9g-uyi13XeC_SOetEgxPOJA4IeBtYg7vvxjeMYhJuKCvCGyB_FOwJBUgyrxhtucMVeMOIPmkCK5fX_QNhGbd8wfHMptQLckZSYAGNk5ksuwUFp30MGLE0Tddux5x60Yt8VLlUEEGys9aBm99eSPJQACB_2Pmtiig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇱
فرانکی دی‌یونگ و همسرش که در تعطیلات بسر میبرند از چلسی پیشنهاد رسمی دریافت کرده. ژابی آلونسو درخواست جذب این بازیکن رو داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25548" target="_blank">📅 21:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25547">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROSfb8TzjmxrcgEVvg3p4innSQgYNZglWDg0BjyJc6MmIeOXMZKj-2rV1LkqlmxXYMY-OFhlGHlVGFVSQhgBMroIT3AmgjGR5luhs3mzN9AttzK617Fi_i-a_tX2koAwpUPGIhZCusRDW3W4VWl84DjjNQsfi2q7NS2utWMQnEP4rg8_ZqeEwQmAridD8uRPUKby7NLi-4qpbL_0xydukkIQ6iFsLWlf5JMalToACe6zN-pvecS2uJLKggEDgKrSGb_CbsbEcEuRh9GUOOHyHZy9FGH6OweF40Wx6DFOVGdz1a3ZQqUn41GamgBkZK6quiEkd1B9djJQqC16nK_Rgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌جزئیات‌ عملکرد لئو مسی فوق‌ستاره تیم ملی آرژانتین در رقابت‌های 2 دوره اخیر جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25547" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25546">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEOPi3BvMcEKXrpZPjJ87-vmQHOUZfNK9a7O-gq6Ogaj4ipUmFN_v9uzM_nBG21N5CovR-FFMfkv7dvVBVwLSmiQObUVTeemSw4G1B0jBpVuWicdXl9M4AEjgfeWImsgKRP5Gca6dztOoDMaMktP8ISrVB7rq-NRupRXCPHBfUwHobcLxJuewxY4mCPUHSqdzpKRpULX5FBZdiDnEK4cnXCUBdoVojWkNDIncETlMFIFSodUodhiY6ek5xxMfHnRPTOTBo_Jx72m3TfJlPurArFO8odmXrj453X5QPHAkRbIdn98ncF2ARtIddirnY_8pp8g2qgGpIBFZM_Im5SAFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اینفانتینو میخواد فشار بیاره تا جام جهانی ۲۰۳۰ با ۶۴ تیم برگزار شه. و ارژانتین و پاراگوئه و اروگوئه هم یک بازی به شکل افتخاری میزبان باشن. مشخص نیست فقط برای یک جام میخواد این کارو بکنه ولی ظاهرا عزم راسخی داره که این پروژه سنگین رو در سال ۲۰۳۰ انجام بده. جام‌جهانی ۲۰۳۰ با میزبانی سه کشور پرتغال اسپانیا و مراکش قراره برگزار شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25546" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25545">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMN_j7V6AlVUWQn_akxbpqKazQu6McE6IiQQRREkfhaviY5VhUzQPEEbx_5pwBs2WxGnkITDXRWduivOC8h1lYPy3faj3lU9R6Rn4KZl7EdLoHkX6l_5cPMzxCs6qxQSQcCLR5N1I_XKzOsjZt4hla1zAuVWvbNgdyoNxvDmUMwTurfqROApJ537_9cqF5iaecWXDFgLP6bT_wbviwJ702gWFyanTEzJLAK2z90dSubEsVY8l_vnw4llPP_MftDvKLZCYJ581FVuwH2PfdXRy052XB1GAVspuntG4Rzr8Yjd5vfs_9WDRvaPzMUSbksd0EZkUfGFOU0JkxICBW-hOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/25545" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25544" target="_blank">📅 21:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25543">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY2FGKQBNHpJtxLsMxLq5N_D5mc7yhgOCexPviESN0L5wZ7h568TXZPn5OefyXglZRtmBmPrQlOzFKdeWgvqHuBj80PkvuECVAVhXoxfucWq_uCRvxK4DVz6iHuEWBBZ1daJZfr-6OpXwfmNphgiljyLke0AQzBCgvR_4_TpbGIWCgkXorMy430eIj2eYyJnfdjwtq3j6MyRdvN75C2roHGfMhGjZPCq0t_gwC231tavb-jB-rnQO-kvND6u5TvZ19ZvHTMQs31UEK0Swi4tWbKcc75dKb_rmCdyPwaopX-CxG9OfKVo45JM7kxh4MrSikXdGIEil7rwC1UyNqpgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طوری‌که سورلوث در بازی با انگلیس؛ نروژی‌ هارو به فنا داد؛ وایکینگ فن‌ها عکس رو میفهمن. برگ‌های هالند از خودخواهی سورلوث ریخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25543" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25542">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeY3eAx9q0Wg0_M6r7tnThQmcdQEPGT2x3j1DVvimQ7Ab-3CJikQ-dpbLYiwogpFhCHCASdFYh5orjVgCUQv77xatfDxFB_qWw5W83Vr_NfOk-Ibk2Y97RNasjz8nstBuKZWx5fPR-V3Xei5QndhMK6x9wUNS2HdOa-aCa1rApmUAsIypIafTUoYzysnMrmIYM0TILijRGTGKWaMuPqSbmuH9UppYaI89m7miZkrxZSZE2ZbVxBl2o7SOCSYjoNE-UntnnRFg0IA0t359j0-0m7cJOqSNFfUlIjHriPXlJzPMm61wGWc3eh2g6ICeU_P49Omo35rS7jZUH8trQ8F4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو انتقال مهم امروز؛
آرسنال 20 میلیون یورو گرفت‌و لئاندرو تروسارد روبه‌بشیکتاش‌داد و مارکوس لئوناردو ستاره الهلال هم رفت آژاکس؛ هلندی‌ها بابت این انتقال 17.5 میلیون یورو به الهلالی‌ها دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25542" target="_blank">📅 20:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25541">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/104d086276.mp4?token=ohH6Vx1vkG9QmfUYj8iiEDE6rfv68vZelClVd-MIO8zXXE8GHJp80C2OZHlxDzW6XI2fEZdkCjg2zll-xaIapcth7ZXxkGuIXl-HzpCtcfx-fQOnZyJ2-hZ-03jNWBqTrmKVfrFys2RlOEF5utO3NYaXPhg76wM8jm01av9KZ4TyCUP75Hb5jJrm3NIXC8YBad_z_O2DXgAHu8OMtjme9xlQSmc1Uxh8CufTWuvRoknLMw53acYsGHUUmnYYWeYmCSCqriyP8m5BcfjePChp1PEqwj3LNF3tRCaB8q8RJJaRAhlSzItsL3X9GHY7Xk6vBZa0Tt04SmB9E9m3zZAG0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/104d086276.mp4?token=ohH6Vx1vkG9QmfUYj8iiEDE6rfv68vZelClVd-MIO8zXXE8GHJp80C2OZHlxDzW6XI2fEZdkCjg2zll-xaIapcth7ZXxkGuIXl-HzpCtcfx-fQOnZyJ2-hZ-03jNWBqTrmKVfrFys2RlOEF5utO3NYaXPhg76wM8jm01av9KZ4TyCUP75Hb5jJrm3NIXC8YBad_z_O2DXgAHu8OMtjme9xlQSmc1Uxh8CufTWuvRoknLMw53acYsGHUUmnYYWeYmCSCqriyP8m5BcfjePChp1PEqwj3LNF3tRCaB8q8RJJaRAhlSzItsL3X9GHY7Xk6vBZa0Tt04SmB9E9m3zZAG0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنایه جواد خیابانی به قلعه نویی و کادرفنی تیم ملی به‌دلیل‌عملکرد ضعیف در جام جهانی: فکر کردی منم عین مربیای تیم‌ملی‌ام که 180 میلیارد بگیرم؟
‼️
هومن‌افاضلی‌خیلی‌جدی‌داره میگه فکر میکردیم که میتونیم تا فینال جام جهانی 2026 پیش بریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25541" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25539">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2qRFCsvvmoXcPcpaOteUXJB0Q86EKl_YlbmeYtyuzQJsWu97wxWzFRnE6KeclpDNEFzrJDMRUlU82eXvi7Jjc2jDSRp748RqKSLWz20jcDs61OQXEwO7hOcbAqZhdVwbXQ381Vu4FrjBFTLejA1OYrK7yceK7KKXdoD0Y7d7bpAUzHNBBzK2PHP3hCX0TA13FE9AUGobxhS4J6t7EnkhBTNi9zO1oUIqcBBXqEGxvENbQ-X2GLNcjYIrSuVguWwf3FTZV8IOSUIdmGMxRyZsHUIffIHIhHZG9apIkP8TogATGOK2eIS5zUqOaqacXDHAo_fXXVxlb7j1J1i6BmiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25539" target="_blank">📅 19:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25538">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmHK0Nv7Ar_sqCUtuG_HRUv3m15unE4eR_WEV5g7n0uIfnA-sDTKa6WHlNsx_h9i9q14YFS5UEExjZIBddGeE_Pl_j7QzIThpn5r7JRi3D1Lre-X2mhXc4x4yGjb2kIjA-C_QCIQ964k930p17jaD9MEbE2DjxwmuXqxROOsmJ0shmsAyjA0-alvQZJ07uV1gyXV2P0Ar6Vak4D6Ar6QciLHG4tJ9waVdzO9mZC7tHXnBTO00Uswo4JSLgVORZkc8RPLcol6CSqCyWdHBQogKlDQPSRjkGuqCQTzB6VNcPIvTXLq_YSmDuQI_4TpggPiH2CZcSNNWVScqttQlkV4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینی در سپاهان موندنی شد.</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25538" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25537">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJozcccqzwnlVAlQG74CeYk_wEDUpd4A_t6ZjgyCNxYjy4dSVe7xvZRcRVFlFOYu35LZ7hiz0ZdNKBugQm5CtkBVpZR3ssQEw1Bb4yP9jgfI1oZxhGwEVoXCrf2TMm3Q7BpyAqWd7-CSpaSuCQpZFPigEQu2peiXe1sxi6vjHSYUN3J0WlZVT_cqRpP5I8O8DvTh3k02YDMN_bCHsQvLPbjA8FGal8ctic_gqOJUI0O8t6_bgr47qdWWl3x07VaI-0Hqhr6UFvKWoqVwdQO0wg64YfIpYq-FJ3t0rkfqtzrpzZSLsR4UMXbF7qgehCVUD1Z0DSToqCv7MJMHg4uXYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25537" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25536">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=EBB1E7OFSz8pG7ayu7XijhmXHNMKKYNZzTI58FwHibQQBENiTHuCs3Zz2Lx56fItTvr4jnAAJiVzq43bsVZMXWtkBQxaeM8TQ4lNVxArg_PFb04_hT0F52qicjQnLTxlcgE7RubdBZK4QPtA45NDJFcHv4Tn2Y_0JuNeVgxZM59PhmEBWBzgSd5ydL_r2SuZGvX8JMnsMjm6pKtBw6YBQCpPuZZT1iiaZOJKXySTTyU2fbohACGQE0GUz89vtFy2KTkNBtYyaMQj9ELuanGySRZFEwrqodxXwOF9qbCWrz2ksWuRJ6gFx3mNSDm1A7KXmOTFZwn4l_xwmOijPV7qXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=EBB1E7OFSz8pG7ayu7XijhmXHNMKKYNZzTI58FwHibQQBENiTHuCs3Zz2Lx56fItTvr4jnAAJiVzq43bsVZMXWtkBQxaeM8TQ4lNVxArg_PFb04_hT0F52qicjQnLTxlcgE7RubdBZK4QPtA45NDJFcHv4Tn2Y_0JuNeVgxZM59PhmEBWBzgSd5ydL_r2SuZGvX8JMnsMjm6pKtBw6YBQCpPuZZT1iiaZOJKXySTTyU2fbohACGQE0GUz89vtFy2KTkNBtYyaMQj9ELuanGySRZFEwrqodxXwOF9qbCWrz2ksWuRJ6gFx3mNSDm1A7KXmOTFZwn4l_xwmOijPV7qXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگهام ستاره انگلیس در پایان دیدار با نروژ:
مادرم یه هفته‌کامل بهم میگفت مراقب زبونت باش، نه فحش بده، نه به‌داور گیر بده که کارت زرد نگیری. آخرش هم مثل همیشه حرف مادرم اجرا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25536" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25534">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qr7OeaEheDCMRQWAy7AL45JIQzBGe24BtpNi2St9IbrNcBf8sCpuSJC7nssNBEDOwhdN4_704FS1EoXGMlc3KijXAFDP3g-bQPX6dTcobGROaX0wcGmUUa5gUbSyPsnScGhFWKSrnGsyb51AQlR_oi30HmlrTv_WxqQIGTquqCas585npfehqrUPq5v9ef-o9Cz3-cDCyBG9-HYNrRtuOK9ecYosjzGqMFBrcNknmbHqdxp3Piu5YwfK_9yXnPh3eHAYlHMBo-a1c85eHiHV3ZNMgVCDe_MpidGIRBxP6wThAdaU-ujcVRH2ymOSQp2d-PJrDV586M0VB9odTZ4WWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوسمار ویرا سرمربی‌سابق‌پرسپولیس در انتخابی عجیب با عقد قراردادی بعنوان سرمربی جدید به دوا یونایتدبنتن انتخاب‌شد. تیم‌یونایتد بنتن فصل گذشته درلیگ 18 تیمی اندونزی‌رتبه 7ام راکسب کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25534" target="_blank">📅 19:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25533">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuvYd0EG__aDF40RELZUXWJGl8geXaJ8DuhxplCOqrLArSz0FExQNXfJlrQ1Pxxk_a4Oo1YkBJpHiyRTaIgDdT0mbvipx5uU2BqHMMPDrKRr659JkPWS_5wUkl13-mOxr7MlPJQ74od1pg1d0lQ0W3C6iEkiQI5G9aVP7m5bSuLOMFeYdf03kobG2Hc8Z3Pgw0H8RodKeknj0akUHxkOMUAJxd3dOXExhO3eZnbI1tLAp_paj0eaM8PFd6OEb-B1eAPy1MMOGDIOOeWRftXEFuYU137Jca2vVkieR0snIyypN5THqU78mG5sVX-qEPse13Z57ZzCpUtXEIZnk-7Axg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25533" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25531">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icRtbTkprnueEH4FNU0wIZgOnJJnlsD-_1F1sbtU3Y22-IP60LsGcr1Vb8I5i8qbnCHKFFZ-IV-NJh36dZta_IkFgsWuNH1cJjPQK8uv1GfHpEBqmq6pS_aaSr1qUCoA5LtECZmb1ojU81K-zQtDkqI3BbwguFDM9RStWwGnzIW6FPn1__pGYPLHD5PMfeAw9dZ0CiPY865fGO6ygLPRPV6aEkfvACpqjQWs7TpAfgSmriCMKnF1iXkLgZS8XwRAmVTS2Z355qztWbG9-RT7lkBaxTxNtDRZw3Z0PH1mJnF1Gf2aiAwcmcMKvbus4vYjMQYMBPTR_PlCNQzxeqLLFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25531" target="_blank">📅 18:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25530">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=Vw0lXK9Cc9dNM1g4Ss-ojXn9QqiQ8dfMx9Z7SPTL5_btXVAqeyuyElv1iNCfR91eUVAC2mHKJM_PkAAtqZTjiXwsfjH0bQW7jTK7znojbl3h2eDiV0p8PydKtiXTIB9Pq15FbGNPZ5pS5FYPWNwYessYTdyLzQBnyu_vY5mfXBts-l5WM9v6OQr398I4aRJBy4HACap5-jsV3MHxxn744A35pZD9VmZArN1Q1lfVsi1hMq--i6_KkB3JPXKEq-h53BziQcQ1PUkcRofnW7MSh6f5gGoMjafmRYnA61jRXQR9xoweBAoXeiEGXwh4AFQSLVKT-AbWXRbUQRJHn4_YNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=Vw0lXK9Cc9dNM1g4Ss-ojXn9QqiQ8dfMx9Z7SPTL5_btXVAqeyuyElv1iNCfR91eUVAC2mHKJM_PkAAtqZTjiXwsfjH0bQW7jTK7znojbl3h2eDiV0p8PydKtiXTIB9Pq15FbGNPZ5pS5FYPWNwYessYTdyLzQBnyu_vY5mfXBts-l5WM9v6OQr398I4aRJBy4HACap5-jsV3MHxxn744A35pZD9VmZArN1Q1lfVsi1hMq--i6_KkB3JPXKEq-h53BziQcQ1PUkcRofnW7MSh6f5gGoMjafmRYnA61jRXQR9xoweBAoXeiEGXwh4AFQSLVKT-AbWXRbUQRJHn4_YNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسی تو نیمه اول با پینیرو داور پرتغالی بحثش شد دیشب: بامن‌درست‌صحبت‌کن، بی احترامی نکن. من باتومحترمانه‌صحبت‌میکنم تو هم باید همینکارو بکنی. انگار نمیدونی‌چجوری باید بابقیه حرف بزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25530" target="_blank">📅 18:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25529">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=VGmxCVelnVk7p2vdslUHHyxCXRPvlG2jee9nVBVeb6RCLMrs4zP3Cqv6tCHh4GJ5rMUEOD8YnpOY6Xj36tu5s5pf1pE29Gz8ZnWZKx9CCQeN5iYWm1oiqz4kzjsmYl-lI7yvohtXbkJGOpXYisMkPy09jIn_BKp2QQXr5WqksHMkTnGzqd1FP9miEvg4qlkcJynzM0_eMAkdggucGC7kiSmCpnSWhgCE-2PVzThuhI_-gQcktCB7R0eYTjsOInlYxDksMAIhxypTasImulQRqbk6QVi2eXWZoYGWw04HWJcxdsm_hydOWyG5ZwNQhF18UM3XUVZy0o_O3Z_WDSznZjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=VGmxCVelnVk7p2vdslUHHyxCXRPvlG2jee9nVBVeb6RCLMrs4zP3Cqv6tCHh4GJ5rMUEOD8YnpOY6Xj36tu5s5pf1pE29Gz8ZnWZKx9CCQeN5iYWm1oiqz4kzjsmYl-lI7yvohtXbkJGOpXYisMkPy09jIn_BKp2QQXr5WqksHMkTnGzqd1FP9miEvg4qlkcJynzM0_eMAkdggucGC7kiSmCpnSWhgCE-2PVzThuhI_-gQcktCB7R0eYTjsOInlYxDksMAIhxypTasImulQRqbk6QVi2eXWZoYGWw04HWJcxdsm_hydOWyG5ZwNQhF18UM3XUVZy0o_O3Z_WDSznZjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیوزیبا از لحظاتی فان و با مزه لامین یامال و داداش کوچیکش که این روزها سوژه رسانه‌‌ها شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25529" target="_blank">📅 18:17 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25528" target="_blank">📅 18:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25527">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
تو یکی‌از خانوادهای‌عشایری یه دختر بچه حالش بد میشه، بعدمیبرنش‌بیمارستان تست میگیرن میبینن باردار شده؛ میپرسن کار کیه!؟ میگه پسرعموم، دعوا میشه بین خانوادهاشون؛ برادر دختره که بازم زیر سن قانونی بوده میزنه پسر عموش‌رو میکشه، میبرنشون دادگاه خانواده عموش…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25527" target="_blank">📅 17:57 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25526" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25525">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoreoFCqP5JzPBGn_sEpA1wNood3x83knFhy6lmJarzgaDlD7u3Ed4zCNhf8T3h9PZM8bDbu8ezAi12wqiEiuu4wP5Qh-w3Z1SzxvZtgROR42Fkfff_0jRQGGt7lM6ZeWW-XmDqV3Iu-tcLbIGzEKEqY4zOPw64JOEsVP8wkp9Wkc_V_QAQfBq_H6V36l8cqdRA7rt81zGVma5Shpxqa04yZwIezgQtnC9GJw4zUp5Clqmbofjxvg5zUyVkqGzreSS2Uy6JZNXwidtXab0WJ7zAdK-zjy0C67JzmNC2WceUhr5qa9PuVeK7WthaWkrjMx6S1ia9GUs0FpXpIEdorHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25525" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25524">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBQgpgyNa3lpNFqjFGcuM3AAszSGjiS4yhyk1rdzH3iLK5tpMeVaQjMgjz1uVqeoeXtGzhUEErpPuBdS4hygq3FW-hO5WsMfdutbU9l30btldtfJKZprHt-iqRi5x324s25AhQu507UxqYBPIiCJNzXrE1i95lupER407BSE7l6BYRDCFxktrH-vEO6nJ3_ocjtGLRvZnLUyvvzKE3Xa_nK6IqhmvaDLHd3K_2sbLs_tCdc69COmrNVNfFYsSX_dT7wJOxf2YX3U2OsICVBPdpTDofCVle92AoxXhNnEJSCgwrDbcn3fe-0p87AyKKBPwgdJSIOxgNMj1L26x9HSBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
عارف حاجی‌عیدی هافبک‌جنگنده سپاهان که مدنطر مهدی‌تارتار و پرسپولیس بود بامخالفت شدید محرم نوید کیا در جمع طلایی پوشان ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25524" target="_blank">📅 17:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25523">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=tzhDPX_HzqcDS5ztI_jAG5dlS7T2NNZGrR1XITwDyELUw2T23ubpgGXgf7GwLImwTKMpUHTmXX9aoCmMYRUnJpQeSF6_f-LvtjdcRe64DMSbyE2dTrHRBXXngR_69JrTed9j1ylVR3ZhhHg1rbfttJ1p7NqmKPofC8tCd82ZJKsdfHIxJ9lUOCqRZMzDjzplUYCGosXLzbAH-Oce6mlBIB8CBnKmkvq_5XtSonTyR-fnw_RU9un557pJjV9azjVua3rJu3hmAay8wQb1YxIcaHVDPqaUHdIv99ZLsKzCcGHuoBKx7K2_UI0e8SfS5y1xPQoq2Uvi1se5VGSAcCBamw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=tzhDPX_HzqcDS5ztI_jAG5dlS7T2NNZGrR1XITwDyELUw2T23ubpgGXgf7GwLImwTKMpUHTmXX9aoCmMYRUnJpQeSF6_f-LvtjdcRe64DMSbyE2dTrHRBXXngR_69JrTed9j1ylVR3ZhhHg1rbfttJ1p7NqmKPofC8tCd82ZJKsdfHIxJ9lUOCqRZMzDjzplUYCGosXLzbAH-Oce6mlBIB8CBnKmkvq_5XtSonTyR-fnw_RU9un557pJjV9azjVua3rJu3hmAay8wQb1YxIcaHVDPqaUHdIv99ZLsKzCcGHuoBKx7K2_UI0e8SfS5y1xPQoq2Uvi1se5VGSAcCBamw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هومن‌افاضلی‌از کادرفنی تیم قلعه‌نویی:
شجاع پاهاش پرانتز برعکسه اگه پرانتزی بود پاهاش اون گل‌هم افساید نمیشد ما میرفتیم مرحله بعد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25523" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25522">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=Wcry8lW39QtqHD7s1ACrW3vRx4SwQR3OmyHM6E4WLL_nlEIKB4sTziQqruNHbJCygkoIPR_fWlB7Lvh0IK3C2jjhzUywMdIGRzEiRCOyFnJejAjnWtKdHiag-PiuXdrVRKC-r2D0SsZlYu3U9iQyzuNCMiepaigfosXLm0Ma2RoiQd7J6me1fxtgwTO5Qrgsia82ur5nmzB_mFG3DoOlQssKL9Iciaj1C7CDHeBUn7LeMHMgmUddSYDOXz1YFhLAr8W8oEkFZgYnvodG-96EoaefYl7u_Hjanl1JC5GJSb7iaDYT_HoRsjYuzUjjh3GrCKAvhyS8KLDDYTD7oyI4RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=Wcry8lW39QtqHD7s1ACrW3vRx4SwQR3OmyHM6E4WLL_nlEIKB4sTziQqruNHbJCygkoIPR_fWlB7Lvh0IK3C2jjhzUywMdIGRzEiRCOyFnJejAjnWtKdHiag-PiuXdrVRKC-r2D0SsZlYu3U9iQyzuNCMiepaigfosXLm0Ma2RoiQd7J6me1fxtgwTO5Qrgsia82ur5nmzB_mFG3DoOlQssKL9Iciaj1C7CDHeBUn7LeMHMgmUddSYDOXz1YFhLAr8W8oEkFZgYnvodG-96EoaefYl7u_Hjanl1JC5GJSb7iaDYT_HoRsjYuzUjjh3GrCKAvhyS8KLDDYTD7oyI4RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل فردوسی پور
: آقای اژدهایی، خبرنگار صداوسیما وقتی‌صدتا موشک‌خوردیم و صدنفر آدم کشته شده ‌میاد میگه که همه چیز عادی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25522" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25521">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4009214e91.mp4?token=FBr0TMrNmoByd5bkRwkmy9f0x5d0-b9qcLZi0mJenrqEJjG3ZFgfurnCKeUCw1mDoKjGv9PbwegKaTzp2CPb3y18Y70Rn0fUbArzm0JawtZPwxJMVdAZ-IO46eNSzq29KaDG4WYuUZmsrlheHK9MlZ1KikJOJuWtVPQFlgYGHL-RRN_g1cDWOw9Ds8aBoeHEBWKVChSrh3eCmBEbPw-xol9dvjAnHTnS9AChXAzBe50qWhp6LafLQhY_ti4tsv05E7UYZQcPwKVo7P0U1ogeIQ2SdRKr3HPNIC_88B1zwUfRTKmXvOlkPMuOT7pSURk2n40RM6CTNFbK3Z34MqnRUA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4009214e91.mp4?token=FBr0TMrNmoByd5bkRwkmy9f0x5d0-b9qcLZi0mJenrqEJjG3ZFgfurnCKeUCw1mDoKjGv9PbwegKaTzp2CPb3y18Y70Rn0fUbArzm0JawtZPwxJMVdAZ-IO46eNSzq29KaDG4WYuUZmsrlheHK9MlZ1KikJOJuWtVPQFlgYGHL-RRN_g1cDWOw9Ds8aBoeHEBWKVChSrh3eCmBEbPw-xol9dvjAnHTnS9AChXAzBe50qWhp6LafLQhY_ti4tsv05E7UYZQcPwKVo7P0U1ogeIQ2SdRKr3HPNIC_88B1zwUfRTKmXvOlkPMuOT7pSURk2n40RM6CTNFbK3Z34MqnRUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25521" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25520">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=QLubN_rBVVPUdfeHHKpybGe4D9jgA-ltqJXU_gcnmOOL8w3a2hnOqgrP3j0dIXFcb7uqCQL7Hh4Sh75XHzcLJy4obKwMbIkeXtCckWVfiUUkO-lqY_mXt8ZO7XhozLylHYER6vkn-telQRwKH68MfJuHd0Nkr4xUHzP8V1amKGBb4oyUUnzUO7-JfsCgDjajjIOOzswePGjpKVFJ0EwKkOvQidvFkK4pRN2iL4bxMraggQzrJBANx_eShXNSHoyBRSa_fAV_JF0o8JX7xA5DDwE9DgAt17jtyT3wSBswVJdBXiagSJZDg_7qE_6H8vjFiwzRXpdQ0yHfBbmeeXatKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=QLubN_rBVVPUdfeHHKpybGe4D9jgA-ltqJXU_gcnmOOL8w3a2hnOqgrP3j0dIXFcb7uqCQL7Hh4Sh75XHzcLJy4obKwMbIkeXtCckWVfiUUkO-lqY_mXt8ZO7XhozLylHYER6vkn-telQRwKH68MfJuHd0Nkr4xUHzP8V1amKGBb4oyUUnzUO7-JfsCgDjajjIOOzswePGjpKVFJ0EwKkOvQidvFkK4pRN2iL4bxMraggQzrJBANx_eShXNSHoyBRSa_fAV_JF0o8JX7xA5DDwE9DgAt17jtyT3wSBswVJdBXiagSJZDg_7qE_6H8vjFiwzRXpdQ0yHfBbmeeXatKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شوخی‌جودبلینگهام‌ و ارلینگ‌هالند در حاشیه دیدار شب گذشته انگلیس
🆚
نروژ در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25520" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25519">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRW9GEPFvOlX8nftd37o4Vl7xXushhxQuQVM1O3KiBtJKAnz6xdCzxKEMApswLjbBNjKKqegMwKEum4MCb__rykQxHL6-3QIaIOiWiYP7ABa0vgpUZpUCvtg3BVBQAZ7NY6QGJtA9NMDz0irHn1HeO46yjdbDJSYqBedX0Yc9dUna4ZAuQHnA8OWNCd5_CyIKRYgQLRrvpdlvBnbN7QO6k_HLhvqzvy1YmUXXoCxIfdkvD47z277JzGu54SwtHcXdnwlwmfw0HvugOi0r2-hFCM4Zj7J1ZSZPjGmtV3AyaIc_c0tV6fz6N4r3w9mSM03YpJvkC9rJiewKnQyp1NQWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25519" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25518">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3q2D7JTSoXB9rJYBSaDzeIUacSxw3YqFW7EVderKNShEe6SO22GtURy1wNjrZnWI25yBNH2gKx0GwZ9Auprn-uPZX0RDDtfn0QSfOtf9CUaSwrrFK4tHjadYvsO_XVTE6v3tSGMUSWINrWqF2ILtKRgNNjxawJZsqtogyHSEv0-75L4gXek_m6rTNjPp3NAkKlgehrzxRZoit6ZLWt-ndfPMdB0T5KVBIHtKCOOKCBJr0QlPknnX_C7P_3GZZDNhVvXFfoPksODnoCvbBHtIowUE3WvMbjWaYYtlFmP-wHq3Eea2VisLT_ViwzEXwQRJzu6A99s4p3n6u4K387nqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دو تقابل جذاب بامداد امروز مرحله یک‌چهارم‌نهایی رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25518" target="_blank">📅 15:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25517">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR-Ya7jPtEVUDY_6o7KAptaCbjNhVifM2rkX__-HBGjI_sk2sAzjZxBapvG9_lKJdQYfaSaThkEh1_5RXInbifakPw10nx-yYCSCuEcBnQIX4phN5a61f-Yq2pCjQbJN6KsKGaoY8gvUW7k7aWteJkNhcgOr-LcpYRu8q8AecHr0ePN7w5Deu0W0lp8xNh0SBm3pzgCBnKDlx46E5DMhplmOnYuxaNWbwTZQ6VPyXPY8HFVHMDG2FmdSS_Z-zjSe58KYUuhx5cLdHDH39PauFpUZbDOH3dOPfanJOvEcTnkQ4SDSWBot8XDVwj9vhc-iayeD5HlwOJ1HrJgHFOXnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25517" target="_blank">📅 15:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25515">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25515" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25514">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7soCYKv-hvcyHDuXNZYknsVyOqdNHl9IPZgtDzsL2E819rCw-PZSBOrVOj8914O0lhMN_uEywOMHHGs14WlNBTgpuT6Eg5OFmpwDlrLHZku57c1dCNU8UoyJyKjGC3ZABBvMK7SO_DAjbvp7QRE33sQ-YG_6XEh8ByPfdAW-FJFiZXJPQx_YrLcwOO2rs-ju0wyfhqYiCkXFdF7yitMumycMOhqN1LLsCF8TGOmU4K2CLiwb2pa1pP6KN9NkNMtKf9-86cnVd7YIjOJKwZjrqJjDHOdhnd0y7ZtSuY1jjSvjrlvMref11TFxGoRTgPtHkfS2x3XB7bDwFF-wGyaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا
#فوری
؛
یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25514" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25513">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zg8UvkQcHsKHfc5EXyhFprFzTNjRoUcMmqT_OM1M3Zx72zA2twtYyUyLLGDCo67QP_BeA0IK6gPXp26FtI7t79o0kmrs2yEld-4KsjnbCiVejgO4f0_4mg8DvwBvJxE0ktVOXN6MEEtWoluC2XrT2Enj7dQT4b2n6pkN-GSf9tZ1JRmaMEKwQ-iFDzaZtoTAlJlad6GL6U2AzdJK0nHnt7VaryzJnxZ-Ds_glUcv02wtFlUkTFjdjsL5rQB71kR-CVxW9qyEgtvDy7PS_izo1YQqYyYlcshWfMHQqzj_Ug-mKJz-wejpTcpcHUupozxttLxS8sczsS1LkJEISaR33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25513" target="_blank">📅 14:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25512">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=pMXOr-JbVd-FEpUghlMN7cGpaZdEscoZVm2C5FFDTOfH889kcjNX-X9Z7lHrdS-6zNSSQ9Ob1rG8QIkU-4bm5H182BWpoV1ylmZ0Q59SvVlC5LA3SNAJoQcxkZyEEzfWDSpGjO3xJmveLnOYd9dsNAvv_ZLJsu_2j8WUDYY80Ht8Sb2XAb8YEldot3n0fA32ochdEhUui2uqOsv64g61kXZQGrT0JdspGFdq0-VKtv0jQxH5LbXWU6OyJiKssZEeYjSDa0GDGCadU6p8xuMdqTCbqcvf56sfaZfMu7G-oxHrr3t84djsLkBlm_-c_EaiVhScNuDD-5cLiI5zNZjPdh57Wyv8HZ9RylXNjVImAPNE_JxemxtVA8495K0EX41s15gaDo9ZntvpclYJpq7bGD-qDwJ2cRMVNm9AD-4pdKiE16kLXrd9CvwdgEYseDYelD7tyAQv7pjATJOelg6IGCkwefCq8QOkqTVzkelwIW33pj2zUKD2WibF6A6fsbk-vBkQ4ZP1LRXHzIzzcsJTfDL6GeHBHDPDA-jGw5dOwL1lWtXbLiM873OFue3xFmHIClzMwdO7V44hYUY05oWCrhQ_y2aITG2PqElO0F3B1yF12RnSWjTXofD7kjUNU_wtQ6wtsa5LqzNAF8JBzsuyJXFkjZ43TdOTDO5iNPfUwC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=pMXOr-JbVd-FEpUghlMN7cGpaZdEscoZVm2C5FFDTOfH889kcjNX-X9Z7lHrdS-6zNSSQ9Ob1rG8QIkU-4bm5H182BWpoV1ylmZ0Q59SvVlC5LA3SNAJoQcxkZyEEzfWDSpGjO3xJmveLnOYd9dsNAvv_ZLJsu_2j8WUDYY80Ht8Sb2XAb8YEldot3n0fA32ochdEhUui2uqOsv64g61kXZQGrT0JdspGFdq0-VKtv0jQxH5LbXWU6OyJiKssZEeYjSDa0GDGCadU6p8xuMdqTCbqcvf56sfaZfMu7G-oxHrr3t84djsLkBlm_-c_EaiVhScNuDD-5cLiI5zNZjPdh57Wyv8HZ9RylXNjVImAPNE_JxemxtVA8495K0EX41s15gaDo9ZntvpclYJpq7bGD-qDwJ2cRMVNm9AD-4pdKiE16kLXrd9CvwdgEYseDYelD7tyAQv7pjATJOelg6IGCkwefCq8QOkqTVzkelwIW33pj2zUKD2WibF6A6fsbk-vBkQ4ZP1LRXHzIzzcsJTfDL6GeHBHDPDA-jGw5dOwL1lWtXbLiM873OFue3xFmHIClzMwdO7V44hYUY05oWCrhQ_y2aITG2PqElO0F3B1yF12RnSWjTXofD7kjUNU_wtQ6wtsa5LqzNAF8JBzsuyJXFkjZ43TdOTDO5iNPfUwC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اگه ایران میزبان رقابت های جام جهانی 2026 بود؛ این مسابقات جذاب چطوری برگزار میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25512" target="_blank">📅 14:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25511">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVKkvyaDKbf5BIfmFodOhgFM6V1_3vTRaCJmyPbl4nu1TmitdT5plc72eIe_PooOPx7Ccf40q5ViO1iJ5rN9rvkGP2b_V_RYVNMRQabMzCBYmoUrS9lfzsNHnTtKxv9Jw7WD4H82bqiKTHnwb5cVZk_JncOr0DRfbEqWi-ifnhuj34ssvAu4UVa3spqYfKPKmLRJbO_snAT9LEUcSr944n6rgHutH08Z4fafms-q_UacX3Snkmdd1mZGPpKp2gF6dnGrhbrp54pDUgO1Qava2KK-0n37i9nVkMh0NfdRqEimzN0AQK7OEyoWo1HcS5vE1ZjQ1qcBnVXcfkFFoYH4cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25511" target="_blank">📅 13:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25510">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ute5fxuQWjJ9e43FlIGdyMsEhKYhatICYWDY5QyGtQENvyXiamhQMX-0zHF9QhHJKTusAKKkwAVEue_Z_4CIbQQGq9BXt54oEo_qFk9BPaKn9Gj1_tNfW7JRKm8bmwql_Tdmu5SCXvDUOs91nhgD72yidyX7PGmUJ8bs9eN2O-rL22QZSrK8YF3fx8zU97l2Ni5E1-cXRHet5uPUgiK8cZiJpiDq_7RXFYoKAOWdfc0mh8g3guZHFJLHxPUMUX0a6nUiHfw4OQkt9n_mAvUDYxNxsLPiKcwHYn0E_afiA6BmBYMjAWPjXSuM4Tg4Gkf0chWYYzD5DkB3Yw-kwWfOqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25510" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25509">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkVvavSGj4-n0ssbTgfnsYGXv80HOut8qg6e1QL3QW_eY0YMSv9qZkGNti4dsgD3rTYfyYXK1YaGxVI9Ci0eQ931gnL_nmg_TdlmpF-ov7atllSkRumqcLJZ9Fei3WK2mg-4iXvjha4-otywqBPwdNVMjxMfw8ohBswOoulxyBGD-Sx5q9_X9DvfJ-iXeTSm0A1aOfwtyeFIZaC07i5qy3b46VGvI3NeNqpnfX7MqKdllzFjWswex9WDYqcei2hySjcgAvXkMz3W-XnS7Pv3Fb63llluxMrcWcAT1zcANNSaaEmxW5nClz-VSa3cuHTxgt4HxMbOXOuvCOAx5NgrjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25509" target="_blank">📅 13:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25508">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yer-u6QP2Hvvferew_9PJeGghPTeP_gidj9znNSCJQReTBRIodLqZ8dnNmdwSycKHVp1jysNXid4waTWMUUpDDEBiQn7hwNfYQg8SZNJZVgz2ZcmJTjjd_21a3fdIOuR12NoWYimpLZUAWbTdVE64aQcrZA3ejEnH5dQAI0JIj6OMGdRHSMjSKbubQ9IsCetfBkvq4QXhN0iK9yc_-yjxFywcVdpQmTE_mqDAN8hDE8ygg-QWf5G8HejSpI1qnUJc8Nkx0Otcpxt_xCQVrBR9qPKzDfRIV75SqxMts1RQ27DI7D7tDudlbdN331xq1EYpZxjkRZuFZQD09TZ_EClmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25508" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25507">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVpiGEbMWZ5uNpjw2Oh2EWVRiOxIn0HnB9y_bDq0mZYWDDNQ4nDzjbjThbiGg1iEaDlGK1dP8FPVCAPL3ksbN5VQt1tw3wIkyfn_e3mpHi5yvPwJ70_7KlCRy58C7plIWmPdlC1RKAtYCU-KdnDYg0vKaWW2OAQmJIMJpANsP-eUYTVNiu9IvQ37uQS8rHCUP2hbHyiLwq_XNh4I-L5QvFS3uG1VFM1XjH-0qwGvgH2DWHObbsM2vDsd8zhGKDxxqiKE-euer2io3B_RE-Vj-gQ7TT92SVnDlhIlYOUadg9wHvztkepVhTq1sIhfv5oBGOc-zPLdYQ0C4MIbK-6KWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عادل خان فردوسی‌پور پیرو خبر دو روز پیش پرشیانا؛ مهدی ترابی برای عقد قراردادی دو ساله با مدیریت باشگاه پرسپولیس به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25507" target="_blank">📅 12:24 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25506" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25505">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=L8QMLaPFffYea20zZf89x0qoIlwq6rQ8wbODyJQxK9nHqUgzrwk1HlPiyntkyx_C1aP_G0BQxzMTC86a-dgCRgbZjtEAUFXHEE12y1VrfiPaoUBBO9GbyriWmmv6QEPz-yCLCkp-P1iwNgQ4EI6FhT5N7h6ylny0OmMKdEBpwm1Yl_ItZlfoQ3nxLiRpgxYxBIBbMhir9l_fU7lFD3yi6Emvf5fBD-QrV8-KGYNz8mkXRYH6NdOe2WVdI0X5r65Zgctjhsinui7TZgQLUdHhxrbdC-_NIkyiisnx0chKKNKBfcBOwvEe4ee53Gdg37fbr3v8fDbIzZDWGzamyWAckg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=L8QMLaPFffYea20zZf89x0qoIlwq6rQ8wbODyJQxK9nHqUgzrwk1HlPiyntkyx_C1aP_G0BQxzMTC86a-dgCRgbZjtEAUFXHEE12y1VrfiPaoUBBO9GbyriWmmv6QEPz-yCLCkp-P1iwNgQ4EI6FhT5N7h6ylny0OmMKdEBpwm1Yl_ItZlfoQ3nxLiRpgxYxBIBbMhir9l_fU7lFD3yi6Emvf5fBD-QrV8-KGYNz8mkXRYH6NdOe2WVdI0X5r65Zgctjhsinui7TZgQLUdHhxrbdC-_NIkyiisnx0chKKNKBfcBOwvEe4ee53Gdg37fbr3v8fDbIzZDWGzamyWAckg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25505" target="_blank">📅 11:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25504">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgD1aHZh7MwQ96YyamwBlEHzqxST0FgeBzekBnc8wdlWzzVCo2aMZ3ot5va_Js79yCzOv0votHMOR6esM8D8kbuByVBqQJtJw_W32aOZuY9Q70P3pEygm5LcRiifJMaU2_cf-1-BzzhG3naXVx6Z9L2PLdHgr_S4ituUIqEpvUxq4_hklrXYfpr_oFgIs2eGkqk6zZLeozR_M5ms0J-cJ18pPCnFYh6PcohMUHzzIXy0ntyIsePTigIt12AhCBxfDnBTGKe_0L2oLWv0r4JULw9GNgDMFPu9GI11ky-ZD8T7sjQybciaddduA4H3FPDL8r5Y7d_nfP9YJd3saZNGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25504" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25503">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk7qSSgXhrkIlRfIX7XO5eujLvqL2si2Y4M2MAYdZA5mMbfHwbD0Gq4FvtO_LmGqkS8zDKpq9pj_wKp0U1hIYnNtpe_X_wuWJYYeOf07DSXPKfRwzieOJlKmAAHJOEKNVcKeWYIUloKA1QYbZwnnUvOTaeNCUqNOZ_6OOqtFqp4J7tn2qpFjAcal6Jz8FkRU-wnEg16NCw_SjKqIxhFyr_9RYTbSo2HgN1zMpNenRa_scUf2zrNFZtzEWatSbzwKhCkmz-nSkm9KO5GFVeJvuMlxQjkA1qP34ZHXemwp8QRyrdgE__eYmhiaO7o7npHXwB2ruNEHtUuoNBLTgceKmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25503" target="_blank">📅 11:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=gXs08NypoBWVakBzHtF8cFH7YSNuUEjZRmnEYQUtB7YEfwgiJSOabY_5gDf4Sl2OQ-i05s_Qpc5kK-tZzJWJX1RDRavqeKLrM1ZrTRu_o32VFTqC7oJStociqp9n7CoR05_WdZeIACgKR_ISqxprjT13RboTWLpXCmGhVFekC1PhjuR1vSwipdvSzn5j78q-p2nhiboFBrq0UZ0xHZ1r-m49b1-qT8gu71CFGuKrvM7TEl0HW-Ot8bKbWgvPt6iUVKSw7p_lFQ-YXbcoRPYqbwTlfUdk3YGSzvU3CLU2rMFfeWmLw79qwXvkU1iaK-zhDHWRz9VxfK9ke-X5TUbPYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=gXs08NypoBWVakBzHtF8cFH7YSNuUEjZRmnEYQUtB7YEfwgiJSOabY_5gDf4Sl2OQ-i05s_Qpc5kK-tZzJWJX1RDRavqeKLrM1ZrTRu_o32VFTqC7oJStociqp9n7CoR05_WdZeIACgKR_ISqxprjT13RboTWLpXCmGhVFekC1PhjuR1vSwipdvSzn5j78q-p2nhiboFBrq0UZ0xHZ1r-m49b1-qT8gu71CFGuKrvM7TEl0HW-Ot8bKbWgvPt6iUVKSw7p_lFQ-YXbcoRPYqbwTlfUdk3YGSzvU3CLU2rMFfeWmLw79qwXvkU1iaK-zhDHWRz9VxfK9ke-X5TUbPYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
نروژفراموش‌نشدنی‌ترین‌تیم‌جام‌جهانی۲۰۲۶ بود. جسارت‌وجنگندگی‌کم‌نظیری‌داشتن و شدیدا دل‌همه فوتبال‌ دوستان رو بردن. به قول یه بنده‌ خدایی اگه ایتالیا مدل گتوزو تو اون گروه اول میشد جای اینا میومد احتمالا این مراحل رو به چشم نمیدید. من خودم بشدت فن ایتالیام ولی خب مدل اسپالتی و گتوزو افتضاح بود ولی مانچینی درستش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25502" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hltxo5voZLx38Ty_jB_CBL2WJzN9hIDtTkvx5dI4OLmLb2_QBQNxsISMwSd75sf_9EHYbGMZOInLvZmZKRbhx7hTrmZrpTHaPi-dxmbGoerxTSPs9q-rE1fZhhN6PI7RkgXVlyF6Ykz1tecgMtVQuWWrx4OWI4bJSdM4gg2tq9TgZnFq9XbBXGxY-_sDn4Zzk6d4_EKADDGtyT6NmAmERpyoSWM9OkqvRaF8vRl3tKsumhlSq2o4Z08FGyV5LNu5SfiiompLBNb_MKO65-4ZnYMr3vud4HSYt2yiTgws7uT2kDQC4VWCE2W7jpDSspLoh_lnKQY5JJUpOOHxlu2OAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=MCHJGuJJxIqOA-NAJh_aCgD_C6FHMyk7uI7QnIGomm58Ob_KLgVsfsunBBJ9fx1NWe7smllJT1BvRnm_V2DZhfMEC8K7UzGwL7dTjTar3ONTPS7bqCushB6ldPy4puLNASbottVv6FKVLXTbTzJp0_1vSs3uLCRtq2uwRnOpqyVBcmaABLYawJqkPazvKooJM6OzAH9V2ngNirKdUYRkJ4PE746SJh1tHgllHvH0hQnoD4MD4uFMjaZgr_YNVHvyQu30L52dIm-fVMS2z2Iwh-cspkAL4MKy0rRvvKBbyjVARLxFn9azEja5gWb6WIc_avIlqcI9N7-UYGNGMI2a8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=MCHJGuJJxIqOA-NAJh_aCgD_C6FHMyk7uI7QnIGomm58Ob_KLgVsfsunBBJ9fx1NWe7smllJT1BvRnm_V2DZhfMEC8K7UzGwL7dTjTar3ONTPS7bqCushB6ldPy4puLNASbottVv6FKVLXTbTzJp0_1vSs3uLCRtq2uwRnOpqyVBcmaABLYawJqkPazvKooJM6OzAH9V2ngNirKdUYRkJ4PE746SJh1tHgllHvH0hQnoD4MD4uFMjaZgr_YNVHvyQu30L52dIm-fVMS2z2Iwh-cspkAL4MKy0rRvvKBbyjVARLxFn9azEja5gWb6WIc_avIlqcI9N7-UYGNGMI2a8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25500" target="_blank">📅 10:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqyCR33FjopA7RTBKXZgns-8JvUKkbxc1dzd2LbnupMeY-nrVcTaaJ09AYCxiZ0GuU_scwp1jmeYf3TM2JUPx9uO9nLgHrNBuBae8Qi_WNGWM56M4gGmG1IQtqEfauLU6OR0lYuvByPq4dJ9NTZZVoZ_M5lMY_WUjvMIowjS7GEmYAr7T9V8-4NZ129140t8EHXxXwlf52kQ8mUJgUCmdNwA9EVQBTsFJYiZ0RJWm0FStkgMsjEenjEDA6YiIC8AV2-EpWMFF1vqycNpSHlcJe3wY6s8zY5l4U3ni8iZYJTlr3FsjhJfn1bjFt9RAr2kV-SE11DZwqp12ZdSV0OxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25499" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHrKWPOerMg275WVakT7Xv8WOE14QyNdgRbb4qnTjOb6zM00Y5OT7Dc-SYVoCcdUuXJ_7cKiRf4KsUv5oy3ZPpIcXPOKBITjz52JxkuJWAyNB9EwfRS7AF9gccBGnB6nI_AqtsVVdFgEY8-fi_fVn5V3FG0gzZhmFyVUK72mX5S9zLMhRS6r3qxJgRRG55lgtulpoJLUUmoSFW4xfz5IlDKga2etwLBPhjymuKHb910fzuaqlkFX841UpS17kFi2Bc5-wiwE06QkqCZP-pQCx8b_wm9Iu1cs18-Ps4YA_avBdtf2_TS28oeaskTtlzDEQcsqj5esWls41x78MlQKZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ جلسه مدیران دوتیم‌پرسپولیس‌ونساجی‌دقایقی‌قبل به اتمام رسید؛ نساجی‌رقم‌رضایت‌نامه رو550 هزار دلار اعلام کرده که حدادی‌امروز درجلسه‌به مدیرعامل‌باشگاه نساجی گفته تا400 هزار دلار حاضر است به باشگاه نساجی پرداخت کنه. قرار شده که ایری…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25498" target="_blank">📅 10:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25497">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=LrpAk5NXS7oGk6EQX3AWv-lcFoVnDPYM68H-VvRbYl2UE_cAUoFj-EtCFcv3CKQGkuMm8Olr_zdaZ7P7e37Dj99wIPTN9stcrwjvNI2Yb8mqMk-ZzHlBF69bWY2qRFck_2-wL7ZBaE9oKYaKZBcdfcFz54xUWQyI4yKBk960NSI0S-9Pfiddckbpd6_5_78kt3QU6CzlRYx55QQdEi2GntxSwohHY3fDA0fLM8xylRpUfz8XPfxDnxcCXPBDPhkDQWEn6aRFV_XG2vA9-o2Je6Pgj66okWILQ6NKQl7OZcsYHqqDbh0WfoaSWwzk0BK4OFsRKZwsUwveUm_1Jo5C2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=LrpAk5NXS7oGk6EQX3AWv-lcFoVnDPYM68H-VvRbYl2UE_cAUoFj-EtCFcv3CKQGkuMm8Olr_zdaZ7P7e37Dj99wIPTN9stcrwjvNI2Yb8mqMk-ZzHlBF69bWY2qRFck_2-wL7ZBaE9oKYaKZBcdfcFz54xUWQyI4yKBk960NSI0S-9Pfiddckbpd6_5_78kt3QU6CzlRYx55QQdEi2GntxSwohHY3fDA0fLM8xylRpUfz8XPfxDnxcCXPBDPhkDQWEn6aRFV_XG2vA9-o2Je6Pgj66okWILQ6NKQl7OZcsYHqqDbh0WfoaSWwzk0BK4OFsRKZwsUwveUm_1Jo5C2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس‌جونیور ستاره‌برزیلی رئال مادرید امروز 26 ساله شد. او تا کنون موفق به زدن 128 گل برای کهکشانی‌ها شده و همچنین برای تمدید قرارداد بااین تیم با فلورنتینو پرز به توافق کامل رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25497" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25496" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25495">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=HYYv5g22wBjStdBFLDz0KXB31z4IleMH_sqB123l-s2o4kx7ZR86PpnVm7RIrxc2bPwfkAx5zZjBVwwtky6eglpgPLzwG3qt3RC8awvNsIZ6Huvaxe7lkvmeR5cmhmbXuiYu7Nt5r3jWiGkGtm621dVU6_KN13XQjtCjdUmVh8tPY6RSI13A6MI3XAd81vQ3qLi7uDxSDz8TqsfhccFa5u6vGn5bgHjNh0813fhsC3Tq2L_IC-Y5Wj3XL0zmmrSZcFIA4DEbyRFGdRLEioiAJ4BrrXN9HTH7tYZhS80R2BXzXclcjRr2g8nv9b3rytG-ds1epNPpz_h00W4ZPIFjhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=HYYv5g22wBjStdBFLDz0KXB31z4IleMH_sqB123l-s2o4kx7ZR86PpnVm7RIrxc2bPwfkAx5zZjBVwwtky6eglpgPLzwG3qt3RC8awvNsIZ6Huvaxe7lkvmeR5cmhmbXuiYu7Nt5r3jWiGkGtm621dVU6_KN13XQjtCjdUmVh8tPY6RSI13A6MI3XAd81vQ3qLi7uDxSDz8TqsfhccFa5u6vGn5bgHjNh0813fhsC3Tq2L_IC-Y5Wj3XL0zmmrSZcFIA4DEbyRFGdRLEioiAJ4BrrXN9HTH7tYZhS80R2BXzXclcjRr2g8nv9b3rytG-ds1epNPpz_h00W4ZPIFjhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25495" target="_blank">📅 09:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25494">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3CPwqqBtBS13NZTKwNNRQmd-6gKBrwnik3CVY_fFw58K4mu6BH9WlznEfWwEd9ywYWvEMwv3J8vGGhrEqiT-f3KQVTIJP_aYIYGKkoKH2rXyZwKf-9jqQNEuu6rd3Oq4o6w3gqhtSRFo-XSDwKw7Pe0lshm1nsFFAd42CULGnLe1OX4ZwJWz8kgL6szpOTPwCgJxxZ3nGwDcEt3BxXpz9sEFWy_-hs5LjZOY7tsrYuwItbal3Q8aM1gmCNvhHcLusFvh1bgz-OpPiy4VJ80hZAzMgg0tyXSe8mK-KAYzpWt8DeqkmtVfYcz_VKYmt3DyOYNz0eql2ZZ2ZcxkwHTaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25494" target="_blank">📅 09:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25493">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pe07uMHHFAcsZHK_oJ5ADnMNKpldepJAZjnaE7l4mdLzZlatOVQhhxHUGGV_Vgt8KzCRBUNscg_JO60MlpHMPi39icO452XpD_zteCAB9cigMypnakQ86QtaDPVOXou6wgxpCPljUCG73o3jKwj2Wl5ut-ymZ5O9id4qLCv5T0AZwMthtfLmtJU0reVAFbMgKKdOLo2eLNoKFgtBP1qT6iVyF7_LBk4QZcx7_usBtHmXtIf2OGIaeL5PbzMQD4XcgK2dglXUmuGOSfAsRxCZwR1OftfcIY19nyMQ0sVpyGLGEqhOJyu3oPpP8t8BdCmrdWGNIbdYWyJ57TuP19UkrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی‌رسانه‌پرشیانا
؛ فرزین معامله گری مدافع چپ پرسپولیس بعد از تمدید قراردادش باسرخپوشان راهی سربازی شد و در فصل آینده در یکی از دو تیم فجر یا ملوان بازی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25493" target="_blank">📅 09:19 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25492" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25490">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ib9ZxxnlQi4IOAASpK7N5v_YxPN_b1gtPBrcCgs4q1UDfH1GKEFhterpJdcu52o970uPEobxEKwTpuIDPy2GYlteYnIp-sPu-qM8_x0IKGp7siILKViv0eefT9vmHVKxrJNTOsbpIQn6X9DqFgqFpIVuWmOjBEWWzFZDIe6C0h6fnNLjJcTOtmcaJA5tIrh3H2Gp_ARB5Zz4iwwsGZZfkPro4sFQGxT_980yDdZb9W53cO3uHIU4_qzXArQEI3L3yZaI6-4IgP2-CyDavODEEswrUxgUx2jUvgS-URnP140YYCMsbVo2hGK-uwzydXz7Ujd_hUDpksLRHwzqwrY2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X48EbxgcoX-NQOIIpMZpSXhT6KJPtq4U7-LN6Q0pmLCn-aWFsgBc9djaHoXzAGCfT1q8nVTKFAfxvS1jn86ntTQB4eiSWnd2kFu6qIsCEvKJdk1EFCz6aALKa6YgR1XhrBxAN99RBbV6QuSGyRFDsC7PwdgqBd3hEQaCbIB-cpmfDRWz1RG2YppTg7tRKWvVKTpb7E3E0NuaUT4gl21WFU9Jg4vs3vAf9XeUVWKI1B2a-5l-eDL5DbVsukc7oxNwKYqUNRiYqHCvW9LHiw0j_DLZfVnAh5vB2rdHiHPGVoAxFpMdW5phKPVtKQ4XMSN-n5pL1_gpHi2cBpuqnqur5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25490" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TN4KfYPh8p5M2KQk19qWK-tRqNWZ59O3ME3oxvG_hUUJ6XkbB1EAFCVnNioNM2ThqdS9w3Jc0pePKrTkzKqr0lYIeGnsL3riOsYzrkhK2oK1cgi0QTn833W7eiazqusTPI6GdQJmUTjQR6dZaLlYd6WpTYhMyKVuWAaFGDYiWmevhhCxQgxFrM73HWhwhY6WDTCWKrVyXsN8wDJxaf2PGDC7jP2rzgynP-N5WuYZNf3CzPFkriGhFLnbPlqdkfbPgsqWOI-EeOkDctTuzAQYkjg9UGUTJvZcx4nhxu4dnNFkuYa6ocggDlkm-hNA5nB01Oyqg-791rZuTKhvjRWmiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25489" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u88YjfhajfgDT16S6PFjQS6a6lmcdLNBBte_N94HFGglrgthVz3qN-4Yt0xHxMFhKuDXWYS-l2WcGWlHyqegXFpgddPS1lExWzQzG5yyGCuWLApE2NKvhxPUSnZRr5tt9FYgr8dU_Mm5XzhvDlQZvcOzAuVxbPIhoUA3ZwtR1OnDOMYtBCZybUbaos2Dd2l9Wr-MNjAiUXNdcpFvDXOQLZZUuREKSPYBKKE6vAGrSu4OV4IkCLD_odTuo-LEHQcwSlVBeu79SZAUlzYiOHj7rVjFv093f32rqib9pyTIXjSuTO5XwfpeAxNSzBaKvoHgXPogBVjdTqKmiH-JEs_Bzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25488" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25487">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XppUCgWBOCgeg-UXwQ1et4X5j4EosXNeNaW6M9e0D6H7MwvkzWLYs-zB4tHLZyZAf5Hy1PzppXR-NkrVUANvg_I3-b-r6IvoC_2kr891XyXrlod6zzU7imbSwgf4jZidwV_t9PPxwUFWul6u6384VCPWnn6lYJO3Z-e7KOngClzurdUiIGtLGQ9-d_Lw02LcEMuuaGczB7TOqqtmC9qFjANUmiNRwl3C0RPK7_LY8nXU1aPQ9K-BTqKs4x6l5tvpgkT_7rxn5f_4I4KHhND2ga95OnmUnuOEyZPtYxFCzSob3MqdTZdF4CFwbXugfIDQTwSABL8JFsqJDqELtiOevw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25487" target="_blank">📅 06:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWHnPvkktJjPSLK2IX--XjCzRZqfLJ9jG7T-i15PG-4gjC57n7Cb27ghY8Ltl0q-zBc9McGu_L9E4TPl4Yc9axBpdVdAaiV6ZmOEIB59VjppFvDmsCDBgOQYsCfawUDQsiJEGyl4E7wJjkGbXlluVCr6WDobdiItDRgRiXOSdaJy8kBclVkfZ9uRAwnU-oYe117jHrbHtfghPRoApy7hE4uBk0_fEb_UIcQqfPXh0P7UtOxXpVTflVrGQh318_chWXi4x-np6AJcaZoja-OnNNY6rSVu9Ch53pKADVAAQGjmo1nrrj107CRGPQs8UGihrIKr0sr9PjBNRFsv_BJW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش‌چیشد که به این روز افتادی؟
چیبگم اون شب جای‌درس‌خوندن‌نشستم‌بازی آرژانتین-سوییس دیدم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25486" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=o1c7liaLexbDvLh3KTngsS6E1jaq2dyCgmFvz-tJRXTY6z4SlGykjZfY-pHgq68m97PqBOFOgDtTjkXh6nhOy7JuvKUpwo087gYySuPbMah9CEEA2YwLHvb-JMt6lAX7NZM-U90sj-at9gyjp69P5X7H8yByH420zo_D4TCJRwmYqVDuSET0pQZU1OJerTOcOTz3AeUvEiCnPAJvLcFdiwIcnNkTp0ZEHKkDsWV6XhqCR_TP6jCUhTNTb0znKWYvxVbKkkJ709uUSz0p6i4xeLV3EAXzXi0vyj_2gBac0daI592KJE1ze-5QsIvNaalTf98G7zmmZFGO6aTsiFoyRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=o1c7liaLexbDvLh3KTngsS6E1jaq2dyCgmFvz-tJRXTY6z4SlGykjZfY-pHgq68m97PqBOFOgDtTjkXh6nhOy7JuvKUpwo087gYySuPbMah9CEEA2YwLHvb-JMt6lAX7NZM-U90sj-at9gyjp69P5X7H8yByH420zo_D4TCJRwmYqVDuSET0pQZU1OJerTOcOTz3AeUvEiCnPAJvLcFdiwIcnNkTp0ZEHKkDsWV6XhqCR_TP6jCUhTNTb0znKWYvxVbKkkJ709uUSz0p6i4xeLV3EAXzXi0vyj_2gBac0daI592KJE1ze-5QsIvNaalTf98G7zmmZFGO6aTsiFoyRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
واکنش‌جالب ابوطالب‌حسینی از رابطه سرد بازیکنان تیم ملی پرتغال با کریس رونالدو در پایان دیدار مقابل اسپانیا و حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25485" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbmuYqUCpguBYOLw0mTkVnQM30oM-hUgMRQsWkhnebRUD2uRcALOFht780zB6IHL7NxF-2BORuAZtWH_aagfBH4bFLeRL-k_q1gUzi4ehYGDnxoWHaObXQBgxarvYUIScKnBGmgyBJ65x8Rgtwyee7c6YGmOplGj0rQ3wr4wA77PDxDU-EcPS-AtbxokznIlYW5BAmv_XEJsRkvLpw0o_IvdJSXMA2sf1x_vLJSGw2pX60h66eImp1qhD2bOiMPRPug2uLOS7rGoq9Od6ogx0iFCXvFHyz-zzpfRxA0Vff7gBDpJ3cQn1sZVQUez2NriRQBOpr_psYMbKyEU0Z8qHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25484" target="_blank">📅 00:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOrMedVAsTXtWR7o8q_04KkHMgVOcCdjuhEtGt4IHI8_mrNTs3UCqIt_DtkFt3jl7DOhJaOjPtLcsX07I-1iQaWddfoq6vBrbd4O62rQhbUXD9QMCKT8eTSGbA4MiqAV2Y--fqX7RshIParC9SUDYTcmi6mz0YsBrkx-hmjWgFJC_SrKehY40cy0Ocf6QJm60ytsQ4myXJGcJW4nFihfZZG1bDcdcyC-3a_jmz3Sfc7G8H5QN-ugcd9kFsAA7kBV2Y_0Xkmx9C7dKRA3Ix5qp_JFcmIkbJLev3XESf2SMZMsTiAM8aqZYAATgnCh3TT5NO_Qdh_cX6t7AL9Dt7SQbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25483" target="_blank">📅 00:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25482">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nxi0SuH4GDkneFZHz-qr6Ti5UXygu3bX6BcUVF1Fa_MjVz8CYbTzhQQgsBBtGodc8iykg0TjHSjTI5wk8TJBLuCdF4kHgZ8VPgBiO26Kh60fpu36aXDJg7C8h9m_BzSfwY6sY5kxaqR5yfHM08n35pUywFmbYt-eHnWlkluUgIqmr8irIQivCK3Gi3OEd-Rgsic2daKO4mE5R-NYNwiZYC0Z6h-nms8xTmVn8E5hN7PbmQ1cMKHzjKZt8J97B1rNwM4V_2wqyRy3orC239UNayaP0Ny39-8Z6kkd5To0myYblUvWsfCLC5S-_wCViasPg5r8NTDC6oGCpoJcr1ZIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25482" target="_blank">📅 00:18 · 21 Tir 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fsG6fpKB5we1N8zb4TTyJK4LgKIsIGMojLGoBNIfwAvtLZO-LNBHb2VSwEhXAF0h0U0VcC4WQbRikLCN2dcRuv33b_j2i2HqN8NFsBathkSt9JW13d9IH6zavCcJUnsC5yZBLpFtqKwGKedVWtLIsQJHSwCsdBCGJCTi0dtWiSU6pB7HZ1I0xb3qgeG9PX8aIznlR2ErvgPNUmvKdYxOLxMKGv-ifOYHTfLEnlMSqb-rcPFFpHychMhx-3KFa7OyiMeI6wFzWHdZlch-DnV_0U6kzihq-NlabsrLsHZL8izKMtAPPvxQMlQJIL6k5JvL7fBs_dxb6V9kfQtWlF-ZhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEw-CM0I66AdaXbUIGRgyZxiFqJOWfZp4jcU0XMtnntfUUxyHaESt6OssSgr4ZeKTtLCeMj5jEpkrhuaP0G41l6O4LTKVXdN7xFPO6IPqJv9OylAGuQ-wLgZGd58Haq1awCaheBDl4RzYbHSdcYFGSBvcRs9q4GSfgkOl2DRRd9u9fiIKnWaQtVJ67BR4sCOmmIFowM_JHx_tv_jg6b87V5xPB02m6tFNVzO1UJkiLkg2zj7r75SW2lZLHUSh2H32XPlUmAvpZdzfItSU5lZViGQLz5U5RdcsBgcrg7Yzlwf3cvBOFlU4WcV-fquc903csdMNq8obPhfdWbebpZPZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25479" target="_blank">📅 23:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vX8ETimGVO-f7jXcEDj5Pcngsk3RQ46oJU4f7CqvkCPyEGyqIsoUvjqY-1vRo7im4Sx7ptAIJtOe99Yc2I6S_vrEc4ajVRU07faDIC6kRV4IoLnD5SI1qjUOuGirU0QtTONunGnPeaBioq-NaPqL-k8115px1TUQpyyU7ffISOBtF8zf8KpfedwhPPfZ6E6qb391pBBP9i9641FlvrBSFFlq70s-Tw6nAqrzQkxvMceM26zd-3BPfBMoXAcnj8DVlpUZ7VH1_XmmR7B1N_MgfnNkeAIxtqYwGOHQu1pTm9J6QEEjJRETp55kzP1kz1yIVpCTf7oXoGQYEWU4RbhxLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد سرلک در حال مذاکره با باشگاه فولاد خوزستان تا درصورت توافق مالی بین طرفین به این تیم اهوازی بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25478" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25477">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kovggs9XPK8qz1jXcmz5-1Vk_uEvpqRAM6bF_IKvHyu5hpLuUV3QV3rhTnXNqdMj-e0bojlwKoFjeRMhvL6AzgE7kviSWMWQysduQG_lz86-qSn4hjie_zUxR6-b_GwPkRBwNBd5LJme9g3-9bq-m92-tBHj5T7V2CkmIciDEVEw3DOlYRdtFOwKYo3lfwmE-etHxjNJNRTDXRpsF1JSjvM7h07GHnEWHBxWIHWo6Ug3Ks5GdXxD5WDNrUKx1D1X5AYzdCrFJ73wX8R4K6azOVIc7bV7GCBWXVY1zk0Zm-SyM5yCdU6O4BYz08EC1TbJ63GjCu9q7SkH7FWpCToqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25477" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0jca648bS1UGHOqj5lcYtXUfcB7ZLf-oqrZdiJctIBU5osuaOKo4BZer0pC9w2hODQHtpbqjO1iLCi8MFKd8JLpLrgIX_seBu9Ksl-i7uftSNkevlqidZtVUDkVFPaJ8SiAN0cbbCeYxbviyM1hCkk4f9Ygtll_R1-f8GGydTdAfeUuG26X6Wx5y9TobKNqMZZjuxbpen0hvnWYktM0J6MBlcZyTdS02nCsPBySrGHPhbyCdOJXFoo7J6FlwWnyg_qUOc8HUzFW42QaYNGAt8ZK4QcrIY924lHWRXzeb1mrACHMyDeLYePPTX8o_lj2YndH7O_niNX_4rFpWg2vpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ روبرتو مانچینی برای‌عقدقرارداد چهار ساله با تیم ملی ایتالیا با فدراسیون فوتبال این کشور به‌توافق نهایی رسید و انتظار میره به زودی پوستر رونمایی از او نیز منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25476" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25475">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=GCcsycGQf_tA_ELH5ndK0oj1yJavmDpXTnJgGXiYEF2yfGm0HIVq0ueb6xfhpl5WXunQ6CF7xpmHNE7p9KpD8InWCLTVqybSVJkw7rFo1_GnSscXvQ6EO92v9k8ZXlcKD27Q9xaUQ0NFiulkELxLp8NUbxWbVQ1vl3SxRoPyMMLv_Emylw-0Am8jHYHuEFBZDTcvcdB7dQfI7xMvm7OL-45Mzxm_sDTj85FZuHH7gOMUfGoPplZzcND5nTdFbVrN1ry-3WFPgmiBI5BD9N3rFcMftoCg7n42b0XWG_fx47p-kst2BaKQCu-eywLL0Ylgibv_aXdwgUSGohBerWvlYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=GCcsycGQf_tA_ELH5ndK0oj1yJavmDpXTnJgGXiYEF2yfGm0HIVq0ueb6xfhpl5WXunQ6CF7xpmHNE7p9KpD8InWCLTVqybSVJkw7rFo1_GnSscXvQ6EO92v9k8ZXlcKD27Q9xaUQ0NFiulkELxLp8NUbxWbVQ1vl3SxRoPyMMLv_Emylw-0Am8jHYHuEFBZDTcvcdB7dQfI7xMvm7OL-45Mzxm_sDTj85FZuHH7gOMUfGoPplZzcND5nTdFbVrN1ry-3WFPgmiBI5BD9N3rFcMftoCg7n42b0XWG_fx47p-kst2BaKQCu-eywLL0Ylgibv_aXdwgUSGohBerWvlYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
روزی‌فهمیدم مسی هیچوقت‌تسلیم نمیشه که بعد دعوت به این برنامه‌ازمجریای حشریش جون سالم به در برد. لعنتی‌ها ببینید چه گیری بهش داده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25475" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7d9ZbO7hNpgnrBCG8YXUWW0enF8lZhNFarVJWqrQyCNHVm1sG81QR0Hl9im7Jx3WCidMTwQcB_Q4h-pWg5bd2QTXEIyTxtZKXwE0gf-DRPGTG-wuyycxQ3dBPLt02DE27AaBp-2NTBa__Xyv_G3Qingpxb0hOWISnXyc0YteyLOruIx8yFA79j0uHN_kLzKQc6VUi6Tx0kDSBX_xu-tH35LbnGr4zWPhHn6eM2ypuxp0m3MPP5wXmr-A-Hc0qUfUexhUmO3o5rcaf08MwC5BjbzWbQQE9JccTU_-OZzZKJTGpjxghOQ_Y32gKxGp7cJE_brkwUbEu5r13jKxIPCeA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=rlahzVFnmmMWDPGTioNeKPRBs7y0DTnN46gLkIvTJZutLVeQqA3yTV4KwmIAGyDjCW8kuYcLqQ-k4b2HKoxuWN1dAgu7DEm4fP4OHq1_meEFEdH4dpj1tENjGgJOgCu-qYw9-YeQGFzLzuNZ1853H3f94yGWU_duQpDDwm-jB-2yXd2dyWwqSxG1HEDZtbuFse588TTl95jYOB6PC26DYnhNNWFtfyDVueb3TQrHkJvmUekH7ApuOJeIDFMNCZr4ivZ4xvUNhJlt2ij_XddDj_Yp-IQteEdlMkengF73OHN25Tl4ILwY39kwvE1UGQ7x0xHekXeLAp1RA4W9zhUubQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=rlahzVFnmmMWDPGTioNeKPRBs7y0DTnN46gLkIvTJZutLVeQqA3yTV4KwmIAGyDjCW8kuYcLqQ-k4b2HKoxuWN1dAgu7DEm4fP4OHq1_meEFEdH4dpj1tENjGgJOgCu-qYw9-YeQGFzLzuNZ1853H3f94yGWU_duQpDDwm-jB-2yXd2dyWwqSxG1HEDZtbuFse588TTl95jYOB6PC26DYnhNNWFtfyDVueb3TQrHkJvmUekH7ApuOJeIDFMNCZr4ivZ4xvUNhJlt2ij_XddDj_Yp-IQteEdlMkengF73OHN25Tl4ILwY39kwvE1UGQ7x0xHekXeLAp1RA4W9zhUubQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4Y2j-K1V1dAY1vClg1y3Q7NVjbOaoos4kvkcCwdd_AkiAie9claF-P6wZWh4sSKdHQmb4CyjMCZ1tt7MtMpq_U0E_EZ5gmLjVbjxGBgfeV6yXheA2iw_qNb6AyDZK94v0EyjFfJL_D0Wg4LKB0M8FAHce1mcq_s8XVR12jIW2YgOw5Kn9iSiFLLJ-7XzOXv27BtdYeoPxkKorVnSJVFfWWWDpuy-VACPmxqIw-CZ_AVM7Nt7q1B3d-j-AmpTMG-YlYVCMlyNSwhAYdgfo8frmTZ_DvGj7j16S9U0qIwtmgeKPoM1_hYGQhuv0GTcnrEbN8mc-WcYMnYg_kA13MLAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TX7H5nMkA3SQYMs8hxfVuo0N4LujLUMY8aEZun_RYpZDYWB77GeCQ4CxqSwSaglIxFEqqiMENmABD2GUla8IwiqS83fn6HN_p7TsH6tIkpWUoU2iFvJA_0bNlNGV8LtqvMcMZV-w6Kjvi34GtbegFADubIs71RQNnLDPKuBo97EBcU3hX0b-7IIxcI9qlLnaXOWqzrMeKLMPvJ6YbO_rRutB3df63uMjcWyYgbrCexI2QGJj2Ncz0Rr1dpNo7Lj4Xi0TBFmAh5pyOWJjzBwSPZG5mXuO5igHptUQtE3Fzf6p-XWzvIq7d6BSRpyTUWs40f9DYykazsg-P3JznfjJOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جالبه بدونید بازی‌هایی که تو این جام به ضربات پنالتی کشیده شدن در نهایت تیمی که پنالتی دوم رو زده برده که این‌فکت هم درنوع خودش جالبه واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25470" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=rLuZsDdyzwRTZbMFYD7slZhfdRtXfTIXmLmUh-cZtwabG2OgBTDtUluyjsEAleAlWNA9-xeVcy1_bt4BEIshN0oxg3qismzIxt-3b2xeGuwM8ZiM5Co4Ihb08vc32Rsj5JAYkjtUtOI8Cm0hK31EUmlbLBLs6eDaAQRK3DRTZYjj7oRw4s34vGhy3dZAY3vPgJnFB9LC9DscJab_XNVaEKbTThHLOzXoULoFsDvcVX9-EaR-aLeCqqU7ZgcXuoijk_4Y12LVXi069NxBNvVeD9iFbsY9LiVmWSExL0wEL1cj2GgC_jFskHofGb5BdCGc14Ourgp_htMo7Af6_7rsHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=rLuZsDdyzwRTZbMFYD7slZhfdRtXfTIXmLmUh-cZtwabG2OgBTDtUluyjsEAleAlWNA9-xeVcy1_bt4BEIshN0oxg3qismzIxt-3b2xeGuwM8ZiM5Co4Ihb08vc32Rsj5JAYkjtUtOI8Cm0hK31EUmlbLBLs6eDaAQRK3DRTZYjj7oRw4s34vGhy3dZAY3vPgJnFB9LC9DscJab_XNVaEKbTThHLOzXoULoFsDvcVX9-EaR-aLeCqqU7ZgcXuoijk_4Y12LVXi069NxBNvVeD9iFbsY9LiVmWSExL0wEL1cj2GgC_jFskHofGb5BdCGc14Ourgp_htMo7Af6_7rsHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس که دوهفته پیش با ایجنت علی علیپور به توافق شفاهی رسیده بود حالا 72 ساعت به‌این‌مهاجم 30 ساله فرصت‌داده که برای تمدید قراردادش به ساختمان‌باشگاه برود در غیر این صورت قید او رو خواهند زد. درباره میلاد محمدی او تمام توافقات لازم رو…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25467" target="_blank">📅 21:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEJKFCj5AuRUuE6VYJXcaKhrKJ1r4-wv3-SlB2po3_oM-HO87Ihtd0Bp-Rr8p7xxUcTShx7ZQP1PUslxJlflC2Zn9M55YuZXsRoO8nh7xlcFJibcFPedtM3UpRaqmmmxqQZT2JqiPrGwaifSfB4_z5ywWydVrrhDsdKaQnd7Qqpi1ijwNtJV5EH3Xalfc4JF-4faGlFcqEG6XIrtRRSOJlr7JHEamiohj6V8XJTMqA8mDOM-pudKy5M5t547mUg89Qk7YDeQ4cAvltcaIzQA_vpJiaEUOAhzAt1HA03cy9ENA5skBn7Dxhb5iZyn0D5YQ-4MLBK9eu7Sxc-X4DyB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXxcnGnyeEbSPKKaKTfkPIOL-H17z9T6o1p5q36fN_xVcvr4ver8sVFLz60vWNkca5f__fpThgl9IPFqsRDyuBMoNURiu6c3dgYyeE8ouBIlRjE9YXcGCHy4hWVxVbHXA88HlbtIK6H-5fewVyGc-HhgSllGgufP7_8ax1gTJR2LPNB6zcbx3BuvIBR14SkQ61CgWlFTCXFgOBFwOc-fydEm3ynyx7vMP0PwBZTp_WoQ-UgX7v-ohYfnxKnnIag2Qhnci9p8ShScjBswYIKnxGYu6e0lbAGsrkSmBbMEoykIv02O5F2Mso_bZ1pRbd1WG-M2_V8TtTZPYR03dnbzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9lPVsEIFxeEA87ESHDNOip8ME7XECnOrX1czX7QC1J_4eirWI-whAQp-8dWsEr0av4nF0fFISDSi6r-Dd48mPlqYxGzzKFpeLXYWjittfGcJNdlgHf8xha6cgErAaHpnH4N8TAVfW9sw4xI1IJvwa8Ml-z5Dw17X6PufxByu8ctHaYkMk_xb-YM8Zhp047grMDMdKN-hepnMPSxLW62jt_AiZ8wAZiaEB71JHev0UBlrDQWmn4dhMQ7tCh0gkQuh3AA-ZFHaXsgIa_gKQ0SG6p91SiNrFswjczZ8c11wPzwYdLBfLu-3s6pkNUrTchj6AxcwurGCXs8VYe1RVul5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbYJJmQirQU9xOfkVGHUabXYKZPl8kQiDsbCO2jXkmJYNe0ARGSLmqT06HJo_PLOTxwQZQFV0Gl4xVyd_59wfoz0g3bMRx4WIDuoJjM9FVMwPe12aal7Su01WS3ijKRWTI0Mzd9DA0bCZZK8MggTxISVRoHnF3MkJKVGHnVFD8yx9DLOPNCQHrtHwdm1FWBD35rvfengc0d5rNuPG4RMsjiICMG_6mIuSmVPF3ttskds7737F23CzAbLvYPUWfXhUhgFSkDWoJFP569cb6d4O0l_ZIscrrifhsP2VxtIhXhjGpYx-sR9puwF0cBAK5TWhURwYNiReM6yoBiCaeBd2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZPvaDAaK_xfWL9nhmmNL7glNDGrInZ6njxWy_LNWRCyNCZzohH-9yptNOInB-4vkOxrfqWY_SMEyC8Qij9k6A9MbTQpB4yHxh8yiORm8soq6vyRwSwAcBHw5w2cSgp08p1CVuKeUKeyM2yQSS0--8CUGI9Ox00It1k6rfdg7_AoqtE4xGWY7_ps2wAyP9tS47aCrtGulzcstmyJKje6UkCgsk2k2UNvqTQBxeLMYFOLIpRZOftosJQd7CcVBCAlph0FNCP5qJADeSjyUFYZqmxJpsacdk2itCm97jtySSTK_zVErrG8nu-79AXAaN6IKiDk-DZTe5gT1onrKegQIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/er_dbX87DoxuE_KZ0FWIHID-jH6I2rope0yMusQRXtrt_nWmXBls8k1yHZRBub_BemLJKrPYSj8ZuNGEWtVV__oQ09KAGfigvOMVcvE3kxyCrjlKa1za9j2ZvZjYJxur-rhk2DNJQU8tg5Zsyfc0-RFh6_Vimq2ZcFrCKtxKB-3IGrZ1yzdTbenLyeqLiG-ROAVuDkIu-HVKlK1WdSyfYqKeiEze6Qjhdn6Uox_pxa3ODjPEQbI5RhJpR9u-OS5LAXGQU_7xsx5lLBw6H3Oc_V3ngEW2K2lBZuo-Ij0x_W3UYS447NAc3yvZW-bd7SHeccCIr91xxo2uggTjLmeUfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfshgnMqbAtJrgX1bnsJ9P-Egxlhaq1NqL8IoW1-FHL19fUaHc-dZIWwYeqYkek7QMn9lF-nljUgHeZmKmJJ9aONpgPBRjsz6U5Vg4UU4gGY93Z62dmt0z3WpIizSvuMgwbSCALWBJyTuV4gsQfGD5hXkvANGPj2rNauKoTh-TadoZ4GVmgxvdS7tnmo8gHiT9IvgXGv8l3acqncwlTCUUXmOGAwF5BIdYK63i_upSVZSWzt59bJ_eRTiVYxv_jEvkJ5_KxF91r_4LoZIEcWjD2V8mG_JyOT0DkVM-bvVBJDBKqxEc_q6uEZeP15AXZFo0inPlRdMjHA2UFfZi8Fuw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=jYnxEXeDySSHgJePYROq6R3kDcrA6q30133jPlB1g9ttgANNu4wyWC-yslvkVL4VdvoVHp-ZqwHHWenexeY5rysR6XxJROwTFwWSHFHgWlS3GnVvk8SvHR1hCE2WyM-gv_rg-jbo1TFkziWIPgeXyuqPvTgezXKKuYQc6b6CevwZOwySpk25bziC50T7EaRWKKybqfvKQ04osPkg7aQPeGi3KPy0SVtJzagIue_og9Du7oYZeUJMLkWA--wFohg8JrCF5gJ1d7ndTra7a3ZW0repcJz_XWBLjbHY1NWwoWzIwPtT_Qoo_hIRQzjpL8gomwG-4ulaOhkzBK4Uqk1rqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=jYnxEXeDySSHgJePYROq6R3kDcrA6q30133jPlB1g9ttgANNu4wyWC-yslvkVL4VdvoVHp-ZqwHHWenexeY5rysR6XxJROwTFwWSHFHgWlS3GnVvk8SvHR1hCE2WyM-gv_rg-jbo1TFkziWIPgeXyuqPvTgezXKKuYQc6b6CevwZOwySpk25bziC50T7EaRWKKybqfvKQ04osPkg7aQPeGi3KPy0SVtJzagIue_og9Du7oYZeUJMLkWA--wFohg8JrCF5gJ1d7ndTra7a3ZW0repcJz_XWBLjbHY1NWwoWzIwPtT_Qoo_hIRQzjpL8gomwG-4ulaOhkzBK4Uqk1rqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
