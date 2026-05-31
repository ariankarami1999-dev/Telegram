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
<img src="https://cdn4.telesco.pe/file/urFNX22FrJggyHxBjMD_j3Q5_l4L9NJN-jTYlsscJc-qppcgHVp1kf3V9evIbNGSonmr3J-lHWW7WWWJPuv4vu6zJqLDu7n1lIKqf-vbsYcUeeCrW0ij3gZOsWV_g2fyFuWfQrOtSHC7haPFQxeAc7-XfP2425_R3UDDia49UkIU45rnOZVgE3YO4mH8hsk8lhssIfPHktJY0CPN_AMNdoK9PeyJK1sAZyKaNtQMIDSugDIP8Fra94gsXNZZt3UYqo1_EW_8IQWbq5jKyaG0g0sn4CKZeRO6gWOeWtNZDUdc4QCVPIj_v0afBfT8_jM35yDv8dFJTZH3eUzfnS_ETA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 906K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 16:27:18</div>
<hr>

<div class="tg-post" id="msg-123954">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سی‌ان‌ان: اگر خصومت‌ها از سر گرفته شوند، ایران در موقعیتی است که می‌تواند تا زمانی که پرتابگرها و خدمه داشته باشد، حتی اگر تولید متوقف شده باشد، به پرتاب موشک ادامه دهد
🔴
هیچ چیز مانع از مسلح شدن پرتابگرها به ذخایر فراوان موشکی که ایرانی‌ها هنوز در اختیار دارند، نمی‌شود
🔴
برای آسیب به تاسیسات موشکی ایران از سلاح‌های بسیار پیچیده و بسیار گران‌قیمت استفاده می‌شود، اما عملیات بازیابی با فناوری بسیار ساده‌ای انجام می‌شود: بولدوزر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/alonews/123954" target="_blank">📅 16:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123950">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K6fr-g-MJ6j_jH5IaSv3i_Q6ygxXME0Jy9CD-UfZ_Hjh56ROQ91glbTOqnhMgdUFjjMwIvsht6PvkiloMS_0_aUK80r86yEz9KvbY5ZHmJhlRJwrhBiiu1eVzqO2b0OTr4Tb0VBb00EaXB520bYLToU9inLP9clkbmRqxIFqqEqy8MukhoK14MHz5nv1_pXcEHQTnQPjsl2Vmm9UwX10TT0OSCJ80FiSx7PdxP2zeJLNz_spG-lfmN7rJndgwrrwR9KEQJuXLyxA7Wo5phYDMyAin9mwZftn9eYYssXZpu_vqvFvhDuSXUu9RNW-ZVRuurFYDLzsqlSeC8ZmstHixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DK4IFBufc5BWsXubAYJo30eMnEtfneLPYtk6qhNbBPFVmQIbHCPQhxqmQLOSFzPGfwh57EJQsqTGFxwv3Q4OJ8dHyqaCKYsxZmK_2sZY3SinixC1S9waYWIKe1CoqDIQwvQ77LGoUH0-vKSNZyPoSoOdzGidQkWcblBgaAWxGLN4MhoAHw6v_Ld3rUbYdNguOkmMeS2wfg80Oq7MS1JYoqvz2bJA-TRv7HZ5Bm66v2UQCUjwToLyT_09iND8Bdp_naOMUdCsKuBFd9x6W7Qm_dSEZyUy8Z1CL8Z1m1Agrtzt3GbPpeA7VES2kEEpfI8veKzjSY2_Z6EVHHAFtW6unA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=bmRsOpV45ZfLJEfgbKtgJtFqooqbwOCOejb7lpmOQtI2AKlSs2rrTzF0iiDvOXjzMOBd8ejT2aD8iU7Rr2RxQLFGRJS1Y5bJrQ7BOhMPnvPsCNbCVnx1g9hbPQZdMhNgOvMLqp708vQHBjvMTjzebSA61ky6Ijk3gQrVhVn660Bc7F_9OJt0-YyZ82StwqNkUG4dg7vyAXzv7512rl1ko65sBVNxMoO8Y7OIrLd-dStb-JxHFbVL_3pZQPRA-K_pyazp0gNYX8X0t3ezKpO6uCJoFzgoe0nV2t_A_2Pkx_kmJwfEOnHc-VMlmaqfp7FmgkPWbrimz975GKPaKFhHJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=bmRsOpV45ZfLJEfgbKtgJtFqooqbwOCOejb7lpmOQtI2AKlSs2rrTzF0iiDvOXjzMOBd8ejT2aD8iU7Rr2RxQLFGRJS1Y5bJrQ7BOhMPnvPsCNbCVnx1g9hbPQZdMhNgOvMLqp708vQHBjvMTjzebSA61ky6Ijk3gQrVhVn660Bc7F_9OJt0-YyZ82StwqNkUG4dg7vyAXzv7512rl1ko65sBVNxMoO8Y7OIrLd-dStb-JxHFbVL_3pZQPRA-K_pyazp0gNYX8X0t3ezKpO6uCJoFzgoe0nV2t_A_2Pkx_kmJwfEOnHc-VMlmaqfp7FmgkPWbrimz975GKPaKFhHJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویرانیِ.های گسترده؛ جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/alonews/123950" target="_blank">📅 16:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123949">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
روزنامه کیهان: به دلیل نقض آتش‌بس در لبنان، میتونیم جنگ علیه اسرائیل رو آغاز کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/alonews/123949" target="_blank">📅 16:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123948">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
صادرات تخم‌مرغ آزاد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/123948" target="_blank">📅 16:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123947">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMl_9AaFryN_Crg6psE8uATV2jVxha9kCXEAGVsk-Dk03STfGek6X7gdnC5eMWQF_ZGtfWoyABrqAd80fKVlcxRHIxhoetDu1sxuEJeNJC4pyesJ3mPr37d3o3nB140O2m1qUMMOGxrgDgZsf98BmrMPQaKH9rtMee3G2DcdeIY9Cu6_ZwLEVHSOJWgaa_lrrTS9qpGTi-UfNyJwxwytg6jI87gQkM90jIcigmpdqDOCpx14WeoKtwjvwxXcnr9Use9NG3EWM66rqiu0IINxd7g64wYR2yZpMfVEMfHUIszchE9Wt77W3x4ScSIsTaPkrYYIn70a_6Q8PFEseYi_fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دقایقی پیش سامانه پدافند هوایی در کریات یام بدون به صدا درآمدن آژیر فعال شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/123947" target="_blank">📅 16:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123946">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سی‌ن‌ان: ایران ۵۰ ورودی از ۶۹ ورودی تونل‌های تاسیسات هدف قرارگرفته موشکی را باز کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/123946" target="_blank">📅 16:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123945">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvLC5NHGV792QR3ZV5wJ_8n2fdvAMkODd4RiXxSct43M6e85gX7K2MhJlaGT92s4_JRLPfbJW1dw-hqC-4llFkSMnyCbsDZmvZvoTAW0QJ8h3A_lu1hicx9rrwv0qPjOi1ZzkbZ60zyt8rn23CneHaF-CvtSzVzh9rbPwse_4etxyULFZZOHDqNlAdWIRp2YyocCI4aMb0Qy3RrdMwMlWI8bltSseufk6E3ZVS0RXEwaqwt5P3P0zW--JgLDFn3gldZKqrQhZyTZRARkCJcJqd1H7cUs3ogGp537KNf_jAsEyQg1x234i4lQObxVuWEPkX9CaCm04yj4DhyqefNtQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش به گزارش امنیتی دانمارک؛ سفارت ایران خواستار ارائه شواهد درباره اتهامات شد
🔴
سفارت جمهوری اسلامی ایران در کپنهاگ به ارزیابی اخیر «سازمان اطلاعات و امنیت دانمارک» (PET) که در آن از افزایش نقش ایران در تهدیدات «تروریستی» در داخل خاک دانمارک سخن گفته شده بود، واکنش نشان داد و این اتهامات را فاقد شواهد «مستند و غیرقابل‌انکار» خواند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/123945" target="_blank">📅 16:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123944">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سد کرج پس از بارش‌های اخیر جان گرفت و مخزن آن به ۷۰ درصد ظرفیت رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/123944" target="_blank">📅 15:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123943">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t74sZa2CaPjod89B1bE2-ykKXOLriVN8FUGwAkZGJPzbmx5k2WmvrvBXBhuvl8za_p7jLHwIxyRBfToIXLxuV9QJ3ufixfzB2UX5PsibmENJBZnY5hnz1RLIguHrE_xw2GvKjj3TjnZDPF_tLxwDupVpwMWoJ9dXdLU1BODQytrrgqXzFEbmmiW5DrwIH_Nnbn0yHoZ1VP8DeboNUIjMR-DRAfziCS6y1z1LK9AFSO9nf4zRLG4U-XHhG9FHOliCaiFwqf-j083_xeNgMa5JBmcxK4VfR_p09WWAdvbYPiyJ33ZnfaLNtsWL7e-WePSYPriJR5agMhrUllTl09etRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پخش برنامه «به من چه» که از روبیکا منتشر و اجرای آن را مجید واشقانی برعهده داشت، به دستور سازمان تنظیم مقررات رسانه‌های صوت و تصویر فراگیر در فضای مجازی متوقف شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/123943" target="_blank">📅 15:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123942">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزارت بهداشت لبنان اعلام کرد از دوم مارس تاکنون در جریان درگیری‌های جاری بین اسرائیل و حزب‌الله، ۳۳۷۱ کشته و ۱۰۱۲۹ زخمی گزارش شده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/123942" target="_blank">📅 15:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123941">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نیویورک‌تایمز: ترامپ شرایط سخت‌تری را برای چارچوب صلح به ایران ارسال کرده است
🔴
نیویورک تایمز به نقل از سه مقام آگاه:
رئیس‌جمهور آمریکا عناصری از پیش‌نویس توافق را اصلاح کرده و آن را برای بررسی به تهران بازگردانده است.
🔴
این گزارش به تغییرات دقیق اعمال شده در متن اشاره‌ای نکرده است.
🔴
ترامپ نگران بخش‌هایی از توافق احتمالی است که شامل آزادسازی دارایی‌های مسدود شده برای ایرانیان می‌شود.
🔴
ترامپ از مدت زمانی که طول کشیده تا ایران به پیشنهادات واشنگتن پاسخ دهد، ناامید شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/123941" target="_blank">📅 15:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123940">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac3936dc2b.mp4?token=ZzOHs8a5CIZqKFiar6-t5HTaLwK6CBc6E4DpqV3EV8i-ioTCOqpJb8Jq-JjDZ92M5ksL9zJxy76buIci0MVLbALqD7QW89S7-s3mjKY8-ackiP7hNoRrqy7ogt5RM0hUzFYetAjCqnw45WqX6DrqKkS-Iho9NlvAhfelFxBlb0kGQVcPcF2BP7rUqE0I-bDARkr6qgN3Cx0WE95c6IuVWE2v7mAOJJv7d4_jlWf2pD4t3FpUytZYCOLRJGQe9NUISgyO6XM6K2elX5378LSkfI7fh5gBiGjvxmgp1OqtUVUpXc3XRlgk8aX8BDakHzQ_-gfY2n7nzIsC_WdrWhLgcXOSUxRujuFDNBSg3nebfn41QA1HSzC-Z11X8Hbjnx7ZZp_605OHssjRjJy3dKyxudRVWDy62pYsC55SR2CG3Rgm4_ukW5OjCNaGbgH-8_XUhuDT-PmPB43-J0YGqORyBV70Woudr8avYbIGatcswY2PJKMtchpfaIc6WJRGHoM6dL0qXXx8a_XD7vPjqbNcUVL0FpXtrxs2r4FIPDyidB9ujGw7SVLXs-V0xNYaKH_fDyrWL8WkP7I4p-nrtk7cARpES8IfKqvRVvOXh0svIrFeJQWUWmKCaVOV8UxoGVxf2Zh1UHiePdKm_Y2-steSdXnanVWbgIlg4YO5ED2yIFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac3936dc2b.mp4?token=ZzOHs8a5CIZqKFiar6-t5HTaLwK6CBc6E4DpqV3EV8i-ioTCOqpJb8Jq-JjDZ92M5ksL9zJxy76buIci0MVLbALqD7QW89S7-s3mjKY8-ackiP7hNoRrqy7ogt5RM0hUzFYetAjCqnw45WqX6DrqKkS-Iho9NlvAhfelFxBlb0kGQVcPcF2BP7rUqE0I-bDARkr6qgN3Cx0WE95c6IuVWE2v7mAOJJv7d4_jlWf2pD4t3FpUytZYCOLRJGQe9NUISgyO6XM6K2elX5378LSkfI7fh5gBiGjvxmgp1OqtUVUpXc3XRlgk8aX8BDakHzQ_-gfY2n7nzIsC_WdrWhLgcXOSUxRujuFDNBSg3nebfn41QA1HSzC-Z11X8Hbjnx7ZZp_605OHssjRjJy3dKyxudRVWDy62pYsC55SR2CG3Rgm4_ukW5OjCNaGbgH-8_XUhuDT-PmPB43-J0YGqORyBV70Woudr8avYbIGatcswY2PJKMtchpfaIc6WJRGHoM6dL0qXXx8a_XD7vPjqbNcUVL0FpXtrxs2r4FIPDyidB9ujGw7SVLXs-V0xNYaKH_fDyrWL8WkP7I4p-nrtk7cARpES8IfKqvRVvOXh0svIrFeJQWUWmKCaVOV8UxoGVxf2Zh1UHiePdKm_Y2-steSdXnanVWbgIlg4YO5ED2yIFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرار سخنگوی دولت از پاسخ به سوالی درباره ستاد غیرقانونی فضای مجازی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/123940" target="_blank">📅 15:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123939">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e984d08a.mp4?token=LW-BmO9kBVgrrWQhEWU2xNLrTs-fR1eUqVDxWmh6Z852UvRV3NPaSPSLcRMRtNk_b71NoOjKS0H2OcaxA0x9aUMH5tAr7JoTBcsKRxPmX2LIbJLOV6e_7RjO2O_cbPOqiCQ3crzUYSLH2U81TH3UOOwKi1qJBVUdzTkX_sTiO1imUQcNi2VauRNR6glnfpqsOC-Of91vodbovbv2PAoUz0pP_k2uOEQuDf9N0LQVnjUUWyOAa81lItyKLCZKA8LaRsQvnM71SQq77ujjUo3VfdZTu-FnRhqhTxvqN3a8tpivXI_GDoHWGDXhqguZZu5M5fqixbpZeJwO7D5zcyrxbIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e984d08a.mp4?token=LW-BmO9kBVgrrWQhEWU2xNLrTs-fR1eUqVDxWmh6Z852UvRV3NPaSPSLcRMRtNk_b71NoOjKS0H2OcaxA0x9aUMH5tAr7JoTBcsKRxPmX2LIbJLOV6e_7RjO2O_cbPOqiCQ3crzUYSLH2U81TH3UOOwKi1qJBVUdzTkX_sTiO1imUQcNi2VauRNR6glnfpqsOC-Of91vodbovbv2PAoUz0pP_k2uOEQuDf9N0LQVnjUUWyOAa81lItyKLCZKA8LaRsQvnM71SQq77ujjUo3VfdZTu-FnRhqhTxvqN3a8tpivXI_GDoHWGDXhqguZZu5M5fqixbpZeJwO7D5zcyrxbIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام مهرداد مشتاقی «چه جوان خوشتیپی، چه رقصی، من که دیدمش یاد آلن دلون افتادم» یاد و نامت جاوید قهرمان.
🤔
عرزشی حرام زاده ، مهرداد مشتاقی تروریست بود؟ دینی که پرستش میکنین دروغگو بودن از واجبات شماست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/123939" target="_blank">📅 15:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123938">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ناتو: ممکن است در موضوع بازگشایی تنگه هرمز مداخله کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/123938" target="_blank">📅 15:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123937">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سی‌ان‌ان: ایران ۵۰ ورودی از ۶۹ ورودی تونل‌های تاسیسات هدف قرارگرفته موشکی را باز کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/123937" target="_blank">📅 15:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123936">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5g1lfR0Fd9NxlM6NjonioTeqsKb8IU0mIayPsP7uNfm6CwT93M_a1r2M1czdczmMioiH8gS0Wn-h7G9cUAegFFsk8RzmSlJJIjqOSjgpB5vG_IwH0dEHF9LJftLs2Q-4pEQDeqDBTxmhy3hJZPcwCh1ZrWiPljeYwRtgMMiRICoI5vwy5Ozp5wOn2Ndx_2eUHZv9eI0nSXiQHwXKgaaBaM4EM8RAUpTjei4yxwBtmjDnKlXBpZcsUdIXuk0J4rxIGTVLTiBN-ZgCDn2elrpB8ozxBQ7V9-4G0ZgGDBFKg9v9msKKBYaKxMNXnlclIMSJAlpP6QN7nkXrHQhWzrroQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارن افرز: نقطه بی‌بازگشت ژاپن؛ بحث در توکیو بر سر سرعت تقویت امنیت ملی است
🔴
دایسوکه کاوایی در مقاله‌ای اشاره می‌کند که در میان اکثر سیاستمداران توکیو، دیگر بحث بر سر اینکه آیا ژاپن باید امنیت خود را تقویت کند یا خیر وجود ندارد؛ بلکه مسئله اصلی اکنون تمرکز بر روی این است که این اقدام با چه سرعتی باید عملی شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/123936" target="_blank">📅 15:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123935">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odVkNHWvQBGOEfVcGghpveTCqqZ2kHb33gQtizeAKozkch7RiaFheobZt1k7hZrIKT_6qD4sLEBSb4vhOLMhD3ixuuTfdVsFCon1KcePZS_L_Gl-XtbmG1rZL9zroM_gKI69aJsVK0MlzGwK1VGs5NPdOiLRdFujyeykHQ7R2n5-MjCqeRY7jTX0u9Fo6W5joucu0m0X38s16YSPqvoI6r-Spzy3oUAqb1Ufa605m53_ToSSEAuJIv7GZGfN2HWuL3_85FJgjDSoCMyr_NuWjmW1W1BAsUESuOGfj3-I5Y2K7uyCXnGey87tjj_iTn7hLf_HrPlyh7i3rQyXZ9o-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: مشکل این است که آنها با انجام اجتناب‌ناپذیر - طفره رفتن و کم‌اهمیت جلوه دادن تعهدات هسته‌ای - به پیشرفت در تفاهم‌نامه رسیده‌اند.
🔴
بنابراین اگر رئیس جمهور آمریکا تعهدات هسته‌ای قوی‌تری می‌خواهد، ممکن است خود را بدون توافق تفاهم‌نامه بیابد.تبصره ۲۲
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/123935" target="_blank">📅 15:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123934">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
فاکس‌نیوز درباره آخرین وضعیت مذاکرات ایران و آمریکا
🔴
فاکس‌نیوز مدعی شد بنابر گزارشات جدید، ترامپ شرایط توافق با ایران راخ سخت‌تر کرده و شروط جدیدی در موضوعات هسته‌ای و تنگه هرمز اضافه کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/123934" target="_blank">📅 15:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123933">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
قتل پدر توسط پسر نوجوان به خاطر بیکاری...
🔴
مشاجره خانوادگی در محله مجیدیه به جنایت انجامید. پسر نوجوان پس از درگیری لفظی بر سر بیکاری و عدم توانایی در پیدا کردن شغل، با چند ضربه چاقو پدر سالخورده خود را به قتل رساند.
🔴
متهم دستگیر شده و به جرم خود اعتراف کرده است. پرونده برای بررسی جزئیات بیشتر در دست تحقیق است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/123933" target="_blank">📅 15:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123932">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZNe2UrGTdQU7vL_tONntxOkJr9BXvD5Mx27xUQiktQd4MaDmINvrSyFGRBAAfVfOTLQjJ4H-7gM1KOdGGxaT7e1ELtSz_kl8fI20-PlYVAnuNfrwBs8sgOwNpW8_IBbpxBPXmr-QrRazS_ldeuTeX4hJwKVwfYMfjK79Z8WfJbNGvyUEUhtkqhIrU_trRBv-w89-q9LPhqv6ZCA5tGh7xszzq4gQMLxV9FJR_DR_7eIvQ9f4Fxm1JOdnvZeF_X0RKa3C3yvhXxFxWvhNmNZD12W56pQqcN0pFpjWGAJU_nW7z75IPdY-K8z3af_FXkxu4cZnMsx4oM9Cqt1cO63lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ خواستار حسابرسی فیزیکی از ذخایر طلای فورت ناکس شد.
🔴
ایالات متحده گزارش می‌دهد که ۱۴۷.۳ میلیون اونس تروی طلا در فورت ناکس نگهداری می‌کند که ارزش آن بیش از ۵۰۰ میلیارد دلار است.
🔴
با این حال، فورت ناکس بیش از ۷۰ سال است که حسابرسی فیزیکی مستقل نداشته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/123932" target="_blank">📅 15:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123931">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار کنترل شده در یزد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/123931" target="_blank">📅 15:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123930">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
اسرائیل هیوم: ترامپ به دلیل ترس از شکست در انتخابات میان دوره ای جنگ را متوقف کرد و بعد از انتخابات جنگ را ادامه خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/123930" target="_blank">📅 15:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123929">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!  @Netaazaadbot @NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/123929" target="_blank">📅 15:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123928">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CBtjfUc9jnUb7-byoLm3EzQbqKU_H-jZzMMt9By49sWIUIH7P4Bnz24Z0VSnFadwvhFDfGUzhcA0Vn9_fQBz6iBlFUJtj5bnydYexs9lWZBL8YeEApO76ahkgmPxy7c66HQd0FQwuGpwrIYgfF7tVbDKYAuMrfkl3put7GF6CDvpYcRpJRUxoUdEE_H_YkrWgNjbHfUqK7XEVN1VB9GzPSCneW2K79a5RhfrQQNQEhJy9sNnkUJjs1efGO1_2Eq81vJbEVTynZSud91QF2MqugnEQZSA0Pvp7GUjEP8kmXpHJBeyw9UUAjA8Ev3cEOgMIztipfmVA5vZEv995rUDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
💎
کیفیتی که بعد از استفاده متوجه تفاوتش میشی!
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/123928" target="_blank">📅 15:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123927">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ایال زیسر، معاون رئیس دانشگاه تل‌آویو:
اسرائیل در حال ارتکاب «هر اشتباه ممکنی» در لبنان است و به طرز احمقانه‌ای درگیر یک جنگ فرسایشی در جنوب لبنان شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123927" target="_blank">📅 15:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123924">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec19bfa89f.mp4?token=rWGeQgzw_uJY_L41ctNR-rjD9RCbAsNH24yncLjirrKWz49AsQvIGeho0gj5PjR63Pz-S5Epy_bQ16ak13usDLblx0MZp_rwG9d3IuzwO0nxqeT_GkoqDl4oFtx5NT_80q_gsjUVuUUJmeOTjxv1RL2bcBOXXlYvb4ISWabmI9LmMONsVp4KYTm1wylCTZ0y9tIYMD_hCxCyEQzRC6Pf94ASmJvx-Mr1DESePiYP5cF5wF0lSMF9RJ0JJkuRyqmGcruNQb7J6WXd0D0O_pcavNp5cXPTvjFXNTyrdQjvmqNjZxjPwDlJVyrZNjqWSpwDJpdiol4vFQV_tTf9Nys6Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec19bfa89f.mp4?token=rWGeQgzw_uJY_L41ctNR-rjD9RCbAsNH24yncLjirrKWz49AsQvIGeho0gj5PjR63Pz-S5Epy_bQ16ak13usDLblx0MZp_rwG9d3IuzwO0nxqeT_GkoqDl4oFtx5NT_80q_gsjUVuUUJmeOTjxv1RL2bcBOXXlYvb4ISWabmI9LmMONsVp4KYTm1wylCTZ0y9tIYMD_hCxCyEQzRC6Pf94ASmJvx-Mr1DESePiYP5cF5wF0lSMF9RJ0JJkuRyqmGcruNQb7J6WXd0D0O_pcavNp5cXPTvjFXNTyrdQjvmqNjZxjPwDlJVyrZNjqWSpwDJpdiol4vFQV_tTf9Nys6Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لبنان، صور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/123924" target="_blank">📅 15:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123923">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
هاآرتص: اسرائیل به جای اذعان به محدودیت‌های قدرت نظامی خود در نوار غزه و لبنان، همچنان به گسترش میدان‌های نبرد در هر دو کشور ادامه می‌دهد و به دنبال دستیابی به اهدافی است که تقریباً دو سال است در رسیدن به آنها شکست خورده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/123923" target="_blank">📅 15:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123922">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
گزارش ها از حملات هوایی  در سراسر جنوب لبنان، بمباران بی وقفه در شهرهای بزرگ جنوب لبنان ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/123922" target="_blank">📅 15:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123921">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ul_qzBvg8eKVPtr7cQvGozrJHoCeBi7F3t9dCrDtWlaAN1Vzr86_ZN7-EbU9HP3gL6_CmgBN9mpUX2w4dSUtdhqEdtCYzA5QYKTWCAUQA4KIDHkmlNRytCaiE29f4n1aphqsW4IOBPm07EyqfrrYkRCTGseFgPzktx4nwII30JHjoZBYduMGjQfUfMrjL0c2Jo4rcDGPBe7nrEWJx35PBpdtRNvsefnJrGNzH5uWhAYqezu1NuLWW3QzxxQcLSqa1d847UkFEj6EBxovznXsxCbJOUfYJboPFtupyCLzGn0eJt1dOXB_ywiE7s4BPPTtQMsCg3_8U7UPw83QmC_rtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دسترسی دیتاسنتر همراه اول به اینترنت برقرار شد
🔴
اولین نشانه بازگشت اینترنت به دیتاسنتر ها  باید منتظر باشیم و وضعیت بقیه دیتاسنتر ها رو هم ببینیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123921" target="_blank">📅 14:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123920">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
منابع عبری: عملیات در جنوب لبنان بیش از یک سال پیش برنامه‌ریزی شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/123920" target="_blank">📅 14:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123919">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
تسنیم: تبادل پیام‌ها میان ایران و آمریکا درباره متن تفاهم‌نامه احتمالی همچنان ادامه دارد و دو طرف به صورت متناوب اصلاحیه‌هایی را مطرح می‌کنند.
🔴
تا این لحظه هیچ تفاهمی نهایی نشده و احتمال منتفی شدن هرگونه تفاهم نیز قاعدتاً وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123919" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123918">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزیر خارجه فرانسه: باز کردن تنگه هرمز یک اولویت اصلی است زیرا ما قصد نداریم همچنان بهای جنگی را بپردازیم که جنگ ما نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123918" target="_blank">📅 14:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123917">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jozFS1NSKJ92iO7LEVuBrGHHPMXWWLuxHSi_A3cQOC9qQyUhefOfark6Nkp993xnetLaQL7Yr3-nJA3loLyuGYAQaMIcLAZfqYTaqfe-oV4dvsopA1XwodY0Apl1FjKhdA-2OH69z6Vcx79XYJhQf2SPKsnHSpYG4KdopJJP4hau2bbmIoIkYVGHIpCKItEQAarS7kKg8E1X3CQ1Up0-ZZT7pVGfXNePFj5J7nGPEEI-m0tyjQwgbgG8JY6ppgFy3cLv1_Kw_Ydtbq9EWxSVe8b2O78RC-M8af54U465R50k-3UtCL2Ix9apcxEBEK_1M6erfe275WEBqb94LHRNzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرباز ارتش دفاعی اسرائیل، گروهبان مایکل تایویکین، ۲۱ ساله، از واحد شناسایی تیپ گیواتی، در حمله پهپاد انفجاری حزب‌الله در جنوب لبنان کشته شد و چهار نفر دیگر به طور سطحی زخمی شدند.
🔴
تایویکین، فرزند تنها، در سال ۲۰۲۰ همراه با مادرش از اوکراین به اسرائیل مهاجرت کرده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123917" target="_blank">📅 14:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123916">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m13QyZOMgzD732b7PlS1uH192KPUaD_NOP98fCTxXBUN5Zfm283oUQHbIZhe_dSYaFi_wy71IrEqkyAPDwgEV6yX-Vklpzdyo3imdzTjNwwUFzMNye5PLkkDjjkRaMMsHVW62R5WYygGN_atAwwpDXuTropQ24KkiT1f2Cq-QTshJuaYNkt74wpaZSmh4t1o0Q90sDoIcIc2-B3gxTPrkCEWJkz0wxuuLSvkwzs55hTikakOQJ0GFO6kzLzDCAhnpgALy-31uxVdn6Sc5g9TcqK1RoPZr7kTH75-CL8vnmFAAgWV7VXUPzLcRNj0NxVTPlqnTfNsovi37eLG3r_cnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آرتی: حمله اوکراین به تأسیسات جانبی نیروگاه زاپوروژیه و افزایش ریسک ایمنی
🔴
شبکه آرتی (RT) از حمله جدید اوکراین به محوطه نیروگاه اتمی زاپوروژیه خبر داد که در آن، گاراژ و خودروهای خدماتی این مجموعه هدف قرار گرفتند.
🔴
این حمله تلفات جانی نداشت اما به انهدام ۸ خودرو (۶ اتوبوس و ۲ ون) منجر شد و به گفته این رسانه، خطرات برای عملکرد ایمن و باثبات بزرگترین نیروگاه هسته‌ای اروپا را افزایش داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/123916" target="_blank">📅 14:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123915">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/123915" target="_blank">📅 14:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123914">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
صدای یک انفجار در محدوده شهرستان قشم از سوی چندین منبع محلی گزارش شده است. ساکنان مناطق مرکزی و جنوبی جزیره، وقوع این صوت ناگهانی را تأیید کرده‌اند.
🔴
بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123914" target="_blank">📅 14:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123913">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
صدای یک انفجار در محدوده شهرستان قشم از سوی چندین منبع محلی گزارش شده است. ساکنان مناطق مرکزی و جنوبی جزیره، وقوع این صوت ناگهانی را تأیید کرده‌اند.
🔴
بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123913" target="_blank">📅 14:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123912">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نتانیاهو: به ارتش اسرائیل دستور داده‌ام دامنه عملیات نظامی در لبنان را گسترش دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123912" target="_blank">📅 14:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123911">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
آکسیوس مدعی شد: یک مقام ارشد در دولت ترامپ اعلام کرد که احتمال دارد تا پایان هفته آینده وضعیت توافق احتمالی میان آمریکا و ایران روشن شود و واشنگتن برای دریافت پاسخ تهران آماده صبر کردن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123911" target="_blank">📅 14:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123910">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
رادیوی ارتش اسرائیل: حزب‌الله حدود ۱۰ موشک به سمت کریات شمونه، مطله و چندین شهرک در جلیل علیا پرتاب کرد.
🔴
آژیرهای هشدار در طول یک ساعت گذشته به طور مداوم در جلیل علیا به صدا درآمده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/123910" target="_blank">📅 14:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123909">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
حزب‌الله: مناطق زیربنایی ارتش اسرائیل را در منطقه کریوت در شمال شهر حیفا را با موشک بمباران کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/123909" target="_blank">📅 14:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123908">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
قالیباف: سربازان دیپلماسی هیچ اعتمادی به وعده‌های دشمن ندارند؛ ملاک برای ما دستاورد‌های عینی است
🔴
تا اطمینان پیدا نکنیم که حقوق ملت ایران را گرفته‌ایم، هیچ توافقی را تأیید نخواهیم کرد؛ تضمین این راهبرد جان ما است که کف دست گرفته‌ایم
🔴
خود و همکارانم را به پرهیز از اختلافات پوچ سیاسی توصیه می‌کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/123908" target="_blank">📅 14:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123907">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
جبهه داخلی اسرائیل: به صدا درآمدن آژیرهای هشدار در کریات شمونه و حومه آن در جلیل علیا به دنبال پرتاب موشک از لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123907" target="_blank">📅 14:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123906">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iP-SY2NNK9c4ojjeUS3FUejB2JUqiG-1RFfgwcuC5N6dWMfqlB12xcq9zZiRisil0gtKqT-nhfnNeQgHLy6XvcmuLV65gBg0H8ni5wAR7W-vAai5p2xtHF-lKDTjH2E4MuN97ZrwkPbCwVf6wlMDTzo_hL2oZgM5Lxeul_ueGXU9ZOibBbcGUY58PvAjmuGAdPMlKxdC2tHwq1KdRR9jA5gYMKMYDUDYxrWuIUTaeEt5JE9Gxhl8i1CbP255CztDmG6GI6IbAxnKRGacBLVrq9xPYp0YRouDOzsS4kPWwlgqYJ33d0NmRaSAjY8dSzFX6bRUmEPSWibZb95nAaWuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت طلا و سکه امروز‌ ۱۰ خردادماه ۱۴۰۵
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123906" target="_blank">📅 14:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123905">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-AfNkUX7NuAmG3w4O746DiPhkcOHTm3BkDGgHAbarGgJFCQbvBaLW5sDno1rO4G5ZRgs6RVBUClkuCM9RBZYefgSUMulluARqLvg8Ll2mxmtmsuIPX7Uw1-TM7-Q3EytAfYm_qFK5IOxYI9aSKyPdKBn09BjsKqD0pPQMNnSgc6LY6aI9CcMPNerubO4gIj6PETPIob0-apZW5djKPV0GgkZL1ijYlU3suKof40bU-_eYS91NXcMYjuIDgeEWmGfWkPrFJVYFkYHpp4PSa6hlSQO798riItG5NTzFE2KbNLsHiq604oRprEokChgXIWk1vKhSKUH-CiebeUqMR4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آشوب و درگیری شبانه در پاریس پس از قهرمانی پاری ‌سن‌ژرمن؛ پلیس ۴۰۰ نفر را بازداشت کرد
🔴
پلیس فرانسه بیش از ۴۰۰ نفر را که در درگیری‌های خشونت‌آمیز پاریس و دیگر شهرهای فرانسه دست داشتند، بازداشت کرد؛ ناآرامی‌هایی که شامگاه شنبه پس از قهرمانی تیم پاری سن‌ژرمن در لیگ قهرمانان اروپا آغاز شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/123905" target="_blank">📅 14:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123904">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21c0898080.mp4?token=NcqQgVlM6u1lUDK0eC93UNPfmJo4B_CRXbjZVXwIXxOBFOQfr6s9EXIC6lppMA4A36maZNAt8kpdISs5M1Wx4ab2oshk2g6PcL6GhEY9EBsnSWl-KBGjqFFePF3GkrxEPe8whTPw4pM18t7WU_MewyYxaF3PO8BYJGBfDgPZZk_KoADsfD1RiLgpAFq3X7-C1RCR7rdStFdXNuxuRZZeAGr0MjlWtPRkhaUEW82mvKKbeYGi4mwxgrSsSDUkOhJBaWj7rifsEA7ikzR7pTO6i-bQOsPQ9oTrrKm0amwZbWWuqMPPnpkmPrzm_4yBfoidkSC6N9y6Z41HP7SfF_bJzJHpQfFmuB4XxbIgQfKVfg1HAGm8hxxfTDnjC44WONeZqL7MyfBPt2orUP8wAKL_2qqZDGHuYQ6ipfMaTzja8XfskThnM-qdpsBfsvpltrd8jMqADUOVEpcgObw4PmR-a0lQTV-aI7IvEPfZGJOek2lJzgX9rhk9aQCKN-PS1jrkWknV4Zh2hZa0wl5OHYZBe7I06VKwstDODz4qCTOQ7Ncin09gKZm0RgF3Zq4np9mWUNMJBhap-QNhuLb6irrvYAWx3W3h231hQ-OaCXH3sCZa5cSEOJhVPHLzyEUGSQmE-s1HuUAcpTuojHgVttMSdKXNAV0jLplRfQszMJnRVWM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21c0898080.mp4?token=NcqQgVlM6u1lUDK0eC93UNPfmJo4B_CRXbjZVXwIXxOBFOQfr6s9EXIC6lppMA4A36maZNAt8kpdISs5M1Wx4ab2oshk2g6PcL6GhEY9EBsnSWl-KBGjqFFePF3GkrxEPe8whTPw4pM18t7WU_MewyYxaF3PO8BYJGBfDgPZZk_KoADsfD1RiLgpAFq3X7-C1RCR7rdStFdXNuxuRZZeAGr0MjlWtPRkhaUEW82mvKKbeYGi4mwxgrSsSDUkOhJBaWj7rifsEA7ikzR7pTO6i-bQOsPQ9oTrrKm0amwZbWWuqMPPnpkmPrzm_4yBfoidkSC6N9y6Z41HP7SfF_bJzJHpQfFmuB4XxbIgQfKVfg1HAGm8hxxfTDnjC44WONeZqL7MyfBPt2orUP8wAKL_2qqZDGHuYQ6ipfMaTzja8XfskThnM-qdpsBfsvpltrd8jMqADUOVEpcgObw4PmR-a0lQTV-aI7IvEPfZGJOek2lJzgX9rhk9aQCKN-PS1jrkWknV4Zh2hZa0wl5OHYZBe7I06VKwstDODz4qCTOQ7Ncin09gKZm0RgF3Zq4np9mWUNMJBhap-QNhuLb6irrvYAWx3W3h231hQ-OaCXH3sCZa5cSEOJhVPHLzyEUGSQmE-s1HuUAcpTuojHgVttMSdKXNAV0jLplRfQszMJnRVWM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بحث چالشی مجری صداوسیما و سخنگوی دولت درباره تشکیل ستاد فضای مجازی و موضوع اینترنت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/123904" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123902">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAiPeIteED0f0_tWeOXYViSz2v60t5TG5kUNOBXLFWYdd42janceK2H4behEr8kNpzZKCr0y1FAe74E88QLemiE9lOjJnT6Cs5DWpCz20kD3OtdxpzRVKnIAnEApxV6JtZpGK66KbMwJGcVlcUbK6_US-U8tgakn-SWz7tyOdBftaVLQk8uRtTbytg4sXzq_5H0mmf-5GITtPugpMZwTC2S5vDc8l4dS5AO8eMUctDAK-uxFeDjgRaAMEnaz4KB1X6gNVlKiG4nUh8G1HsbGQJboR-AMPVcfcZaKyRTwaf8So_YtgL2S1h4qUckABfdAqTxeHHwyzKNj2F4iRyfI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cm-Vd3STKpKY-hU78IBbF96_BbHhaFmL9BgDDtMtVMtLDcGueP-cMJuoZ-AKkFKTEHmS4zLq54VGqEoECahFFa6qsSgVzryzxgv6Kqvmmu7_nJPyynK6l4-5mscOMLtMOhSbjbQPBdjQCyXpBnnFcPGwaerPi02cw-enGNfICtT2LAEgdAwWt3MvLYsfMqiU5Y9gQf9L_IMM1otKN-2FJiDNVXfAaazNLKyEIpBEe-INoDMbid0pL_5d9tno8BnjL5MQ9mUwncefkykTKH4cwu2h38WgoGEYm68s6mVuGOfQbYAc5wSfauxb2oDLyb8sa3xXz3MzK-_n9ncQauFKIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
تأیید هویت یک دانشجوی کشته‌شده دی‌ماه؛ جاویدنام شهاب خورشید، دانشجوی معماری
🔴
«شهاب خورشید» ۲۲ ساله و دانشجوی رشته معماری، شامگاه ۱۹ دی‌ماه حوالی ساعت ۲۲ در جریان اعتراضات میدان کاج سعادت‌آباد تهران هدف شلیک گلوله نیروهای امنیتی قرار گرفت و در همان محل جان باخت.
🔴
طبق گزارش ها گلوله از ناحیه پشت کتف به او اصابت کرده و همچنین دو گلوله جنگی قلب و ریه‌های او را هدف قرار داده است. بنا بر اطلاعات دریافتی، پیکر شهاب روز بعد در کهریزک به خانواده تحویل داده شد.
🔴
بر اساس روایت‌های منتشرشده، شهاب پیش از پیوستن به تجمعات گفته بود: «یا همه‌چیز عوض می‌شه یا من می‌میرم». او ساکن فاز یک شهرک غرب تهران و اصالتاً اهل اهواز معرفی شده و بنا بر گفته نزدیکان، از بدو تولد با دیابت درگیر بوده و انسولین مصرف می‌کرده است.
🔴
همچنین گزارش‌ها حاکی است پس از کشته‌شدن او، فشارها و محدودیت‌هایی بر خانواده اعمال شده و خانواده اجازه نیافته‌اند برای او مزار جداگانه‌ای در نظر بگیرند. بنا بر همین گزارش‌ها، پیکر شهاب در بهشت زهرا، قطعه ۲۱۱، ردیف ۲۳، شماره ۱۱ به خاک سپرده شده و گفته می‌شود در قبر خانوادگی سه‌طبقه دفن شده است.
🤔
عرزشی های حرام زاده این تروریست بود که بهش شلیک کردین؟ داعش ما ایرانی ها شمایین
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123902" target="_blank">📅 14:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123901">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نشریه آر‌تی: لوکاشنکو تهدیدات زلنسکی را «حرف‌های بیهوده» خواند؛ توصیف ارتش اوکراین به «گوشت دم توپ»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/123901" target="_blank">📅 13:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123900">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/redJyeRHNMVK2fTirfTLWmfkG7W2_4CF5kqwV8zNbOf2RtsHv-f_V79dGwRkfNBB6OPu3ZRhjLFAM0fV6rS7ocDP1dDLYgZNIlJH6jVhkcca9GJKKS0Dychx1KmFDHBnXtEmp4TZ5uk3XWIsnde8JhNJXk-vPQxPd-LiYfGeCMnfnadMPPQSxbv_jpjLkVTtHXoVnblBsUUGoY9nUEoAVYfvREoZAyS7GVDPLcHLcWemV_5vPj9QwSqlZ_EmJnRTo-YaIj2PVv4rieG1RfBw0J1o9TWK48fKmxa7xnOy00vi4MzV8iOj0H-x04gmam402gKw8k2JOZiycKHEtlEQ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بررسی ۱۸۳۵ اکانت بازنشرکننده توییت‌های قالیباف نشان می‌دهد بزرگ‌ترین گروه این اکانت‌ها در ایالات متحده امریکا قرار دارند؛ پدیده‌ای بسیار قابل‌تأمل، به‌ویژه در شرایطی که برخی جریان‌های سیاسی در غرب تلاش می‌کنند از او چهره‌ای «میانه‌رو» و قابل‌قبول برای مذاکره ارائه دهند.
🔴
نکته مهم دیگر این است که پست‌های قالیباف که تا پیش از ژانویه معمولاً کمتر از ۵۰۰ لایک دریافت می‌کردند، همزمان با قطع اینترنت ایران در ماه‌های مارس تا می، ناگهان با ده‌ها هزار لایک و بازنشر حمایت شدند؛ آماری که با میزان دسترسی و ارتباط کاربران داخل ایران همخوانی ندارد و مجدد احتمال وجود شبکه‌ای سازمان‌یافته برای تقویت مصنوعی این محتوا را مطرح می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/123900" target="_blank">📅 13:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123899">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سخنگوی دولت: فعلا خبری از افزایش مبلغ کالابرگ نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123899" target="_blank">📅 13:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123898">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ویدیویی از برافرایشته شدن پرچم ارتش اسرائیل در قلعه تاریخی و استراتژیک بوفور، لبنان
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/123898" target="_blank">📅 13:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123897">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7db1c2c33c.mp4?token=Qp1y7ekZueiWIyJesOywgvLxnFUF0dGpDDO-OBSxFZWn18S7vOzupqCBLd1uDEW_gwzn1epfmq8z9seOOeM2bzwKwCAVsUIw91UKJ76A1_VfB0S947kjCxq5KcmNQJVOSlVB6UZvkFhZA6LzqWUl-rdTBmtNZ392hrhvWO6yUaKn3unR0WyCYNnaRNpK-oyJjl1jmAbslpo61Fj7-evNXk-wAPjVDMM_1aRgUY4LU6Jeue5rf1s1UWR7fr2dJZTgiJD1oxG_fC7gHvWQm0zZGhgIBUTEc312MxRn6jNtQMM06vTggehztFPUdoRRjHKLs440bDL-YsYfQ4I-MoTiUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7db1c2c33c.mp4?token=Qp1y7ekZueiWIyJesOywgvLxnFUF0dGpDDO-OBSxFZWn18S7vOzupqCBLd1uDEW_gwzn1epfmq8z9seOOeM2bzwKwCAVsUIw91UKJ76A1_VfB0S947kjCxq5KcmNQJVOSlVB6UZvkFhZA6LzqWUl-rdTBmtNZ392hrhvWO6yUaKn3unR0WyCYNnaRNpK-oyJjl1jmAbslpo61Fj7-evNXk-wAPjVDMM_1aRgUY4LU6Jeue5rf1s1UWR7fr2dJZTgiJD1oxG_fC7gHvWQm0zZGhgIBUTEc312MxRn6jNtQMM06vTggehztFPUdoRRjHKLs440bDL-YsYfQ4I-MoTiUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف : دشمن بعد از شکست نظامی، با فشار اقتصادی و جنگ رسانه‌ای دنبال ایجاد تفرقه و وادار کردن ایران به تسلیم شدنه
🔴
اما مردم با اتحاد و ایستادگی نقشه‌هاش رو خنثی کردن
🔴
رمز پیروزی حفظ همین وحدت و انسجامه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123897" target="_blank">📅 13:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123896">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vF-5GSfwyspdOnvYM9Edpqvjd4sstNv-jEqV5SfXvLUSuOPZcBCBuc1-5S_4JgTa-7W8hI_8g--GU6aAKbhBSnCXYWnhcNO6tsELTM9Qa1RhsuPQFSohSGtk3bcRygltdqhGVgnS-frcY0OUZ_1z6qf8gnbkolWRb-Ij0Nf-aLrX6Swb0qMakEdp6usB4aVph6yyWPrk12cuQNuPpjGn5vn1n6jcKwz7lpwdunra2w_SM2bxv-GPCKejeT9XiEPdoWUxXGqhxACJL-sTi5XREMvUCvLAy6Iu0I-mRjFbyEIJzrbVYv72JurXPpRmvwq4AlbNnTMTtQ_eoDVafC6kvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس با رشد ۸۳ هزار واحدی در پایان معاملات امروز به ۴ میلیون و ۲۳۶ هزار واحد رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/123896" target="_blank">📅 13:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123895">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7328c91388.mp4?token=cE7o_LKWKVyP1SSEpbsN4d_Cmsfx6p8xabZrx6DG9l8VZO0vhYO3y7iV9bBMgm4xltjxDBaGtZTFQ4kjdeXSSadf19MrKOtjuKRdDfSEXCa47PU3yuwsmUpjoke0NNO04d67gpSouMHsHuJE7CiJOJh3r9eKx6c_IG0rIpQVL1kmoyNT6o0I7WChRrPXbXJd3-aV7npD2zrCv7m1OJAWWUJnLj_GIV6rvxptmz2GpEi2I5uV6ZlYkRnPMw6vft1S9zV2LTXvSxTDvMQjHoIee41H-Fdm152sMrA5UW9pSimM8265kzvhaIt3BRtAMtP9vfKUggJbK-1gkjFjbSdzGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7328c91388.mp4?token=cE7o_LKWKVyP1SSEpbsN4d_Cmsfx6p8xabZrx6DG9l8VZO0vhYO3y7iV9bBMgm4xltjxDBaGtZTFQ4kjdeXSSadf19MrKOtjuKRdDfSEXCa47PU3yuwsmUpjoke0NNO04d67gpSouMHsHuJE7CiJOJh3r9eKx6c_IG0rIpQVL1kmoyNT6o0I7WChRrPXbXJd3-aV7npD2zrCv7m1OJAWWUJnLj_GIV6rvxptmz2GpEi2I5uV6ZlYkRnPMw6vft1S9zV2LTXvSxTDvMQjHoIee41H-Fdm152sMrA5UW9pSimM8265kzvhaIt3BRtAMtP9vfKUggJbK-1gkjFjbSdzGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوِ وایرال شده از ذوق کردن یه پسر بچه، بعد از وصل شدنِ اینترنت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123895" target="_blank">📅 13:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123894">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
قالیباف: چک سفید امضا به کسی نمی‌دهیم
🔴
رئیس‌مجلس: ما فراموش نمی کنیم که در شرایط کنونی کشور، دولت در میانه‌ میدان مدیریت مسائل و مشکلات ایستاده و نیاز به کمک همه از جمله مجلس دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123894" target="_blank">📅 13:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123893">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!  @Netaazaadbot @NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/alonews/123893" target="_blank">📅 13:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123892">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cQlQMrMP2aQuAIO69A7EnsBDQVG8BGNqzVGdZgCyUCffB6XMKmmgbD7Z-oP0PhE7-I0b0ruDnw5LKwA_nfoJJ4VLjilEWxE6z-LzDR37azpkdWEpc0EyncNchyWJ1GaIGKUq7hdmeQwwCc-AnPSPnYd0HY-JarQ2VfyRfDv7Do0bZyRfA2S04MVcDUaQ7nh5GaWgYA-heEjecnAcinDdX1WQOQOnDxr8QOTS9WA7H6gBMsOjgvNpJKFRCeUVbF942r29P4hAPMqaxKsQsQjDNdrIDjlv-rvz5TnI9MDiaOTVqGbi1IbfzZ8lurjip4fk8cN_iAJVMhm3yLNy0VyHOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
💎
کیفیتی که بعد از استفاده متوجه تفاوتش میشی!
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/alonews/123892" target="_blank">📅 13:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123891">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnqDdOa5DBKP42BL5TIu2mEczowbPMsCL3XLn1Aup53OUJSovEmWOUPqDCBJZ4q--Lgi1yt257w5K35EdklfCBEduhuMXlfzWlB76V6ac9exzRYIUGVKnY-kRDOIOqd2MDwWfj-q4s8F33sc97ZDfUJ7wPA73vlBL4cA0vTi2ONv0z5ub26aXNF3OuElzIVl7jZy-X8gY-kkM6DGyev_911CEzROawBV5SfTOZAAsqVHCK4w3MGzEPSxykdbCP23SAUZP7tnknb8rZqSq-Be6_KgQH7eQAsYvKTRtqPVK5tMvEqQEuJOy-otygF4dKw_BS9FCP36th8sCaAi8ILoWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امسال ۷۷درصد بیشتر از پارسال بارندگی داشتیم و سدهای کشور ۲۹درصد بیشتر از پارسال آب دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123891" target="_blank">📅 13:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123890">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
الجزیره: [جنگ آمریکا و اسراییل علیه ایران]، فضایی را ایجاد کرده است که در آن هر دو طرف احساس پیروزی می‌کنند و بنابراین تمایل دارند در مذاکرات احتمالی برای امتیازات بیشتر تلاش کنند و این امر تلاش‌ها برای کاهش تنش را پیچیده می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123890" target="_blank">📅 12:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123889">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
الجزیره: از آغاز جنگ، فقدان شفافیت داخلی در آمریکا در مورد اهداف مورد نظر، منجر به عدم قطعیت جهانی شده و به متحدان و دشمنان کمک کرده است تا جایگاه و رهبری آمریکا در نظام بین‌الملل را زیر سوال ببرند.
🔴
تمایل ایالات متحده برای آغاز درگیری با ایران، ارزش درک شده سلاح‌های هسته‌ای را به عنوان یک عامل بازدارنده در برابر متجاوزان تقویت کرد.
🔴
این جنگ انگیزه معکوسی ایجاد کرده است که کشورها را به سمت دستیابی به برنامه‌های خود و توسعه سلاح‌های هسته‌ای خود به عنوان عامل بازدارنده نهایی سوق می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/123889" target="_blank">📅 12:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123888">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
الجزیره: کوتاهی ایالات متحده در مشورت با متحدان و شرکای سنتی خود یا جلب نظر کشورهای خلیج فارس که مستقیماً تحت تأثیر تصمیم به جنگ قرار می‌گیرند، پیامدهای بلندمدتی برای کیفیت و ماهیت برخی از قوی‌ترین روابط و اتحادهای آمریکا از زمان جنگ جهانی دوم خواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123888" target="_blank">📅 12:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123886">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
هاآرتص: غنی‌سازی ایران دیگر موضوع اصلی طرح‌های توافق نیست
🔴
یک رسانه اسراییلی نوشت غنی سازی ایران دیگر موضوع اصلی طرح‌های توافق نیست و بازگشایی تنگه هرمز و ارائه غرامت به تهران موضوع اصلی آنها هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123886" target="_blank">📅 12:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123885">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5afb45638.mp4?token=a_YnIjnHzEJHXYtBGCWjYz-AIPgMC6KSm8GPItkf4k1KSJ812b-XPml4k4SojCCpH6Y2DWL1uPrkZCRrYB5oN40mJVqMBGKyRXlvyxX1fwY4pSDMGmtQhLbD_a_Ujd7Quc9KaxIRVDH4AneNZGbcKahtadw8fwP7MFmZWcRuQa655-jhJOkQKRB4z5e-naNb7oX3d6mmVAbHuWvjBUCjcHaXLcYyalYapSOnlc9wnyY_rfudJvOsf13tl1zXCBLJ99Cv72G5450buSGCvIk_Q4oWe8uDcRBTlAsQR_SEoEGY7YshhHt-w0eb2KLL-dGHFdyHa240JK5WtF0QSo20Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5afb45638.mp4?token=a_YnIjnHzEJHXYtBGCWjYz-AIPgMC6KSm8GPItkf4k1KSJ812b-XPml4k4SojCCpH6Y2DWL1uPrkZCRrYB5oN40mJVqMBGKyRXlvyxX1fwY4pSDMGmtQhLbD_a_Ujd7Quc9KaxIRVDH4AneNZGbcKahtadw8fwP7MFmZWcRuQa655-jhJOkQKRB4z5e-naNb7oX3d6mmVAbHuWvjBUCjcHaXLcYyalYapSOnlc9wnyY_rfudJvOsf13tl1zXCBLJ99Cv72G5450buSGCvIk_Q4oWe8uDcRBTlAsQR_SEoEGY7YshhHt-w0eb2KLL-dGHFdyHa240JK5WtF0QSo20Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :  ما ارتش ایران رو تقریباً دست‌نخورده گذاشتیم؛ خیلی‌ها از شنیدن این موضوع تعجب می‌کنن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/123885" target="_blank">📅 12:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123884">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b253c1d60.mp4?token=lkfGXnGAVB-hL9ZTWgsoVYDast_j9BiW-qriir_FRuMtgS5jKi3ElGXMdQF3CKOpbuj-iCMj3YwptJOmVe2xy4z37ig9LPQNz0WdufsbRSnt3pCut88lNI728wG-zxiLUcyzawewkphH3kMERIMBimlQEgErlPZYKXwi04YHL3NGoOD-lLi31d6G0rP0gnVoUfbR8OoV0WqJ3ty4mP_7th8rTBbEKPRfoIe1fkDzeh9-z6VgqOl1ELl8SGz_ES184QvDrPDo3VwHbC2FSYGBmct66yTkXfgX4VY40CWuHF9Y_GWMhBkAYac0afdjz1AjdTXT5z6p-EkYCbt1UZt7vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b253c1d60.mp4?token=lkfGXnGAVB-hL9ZTWgsoVYDast_j9BiW-qriir_FRuMtgS5jKi3ElGXMdQF3CKOpbuj-iCMj3YwptJOmVe2xy4z37ig9LPQNz0WdufsbRSnt3pCut88lNI728wG-zxiLUcyzawewkphH3kMERIMBimlQEgErlPZYKXwi04YHL3NGoOD-lLi31d6G0rP0gnVoUfbR8OoV0WqJ3ty4mP_7th8rTBbEKPRfoIe1fkDzeh9-z6VgqOl1ELl8SGz_ES184QvDrPDo3VwHbC2FSYGBmct66yTkXfgX4VY40CWuHF9Y_GWMhBkAYac0afdjz1AjdTXT5z6p-EkYCbt1UZt7vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :  ما اصلاً نباید درگیر ایران می‌شدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123884" target="_blank">📅 12:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123883">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سخنگوی شهرداری تهران: مترو و بی‌آرتی تا زمان تعیین‌تکلیف توسط شورای شهر، رایگان می‌ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123883" target="_blank">📅 12:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123882">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=OIq6ZQYhdAl0PHxIJxegt_C52MYHd0VZgxo0vP71rl2Jo_8_1YyoPyHAXTrK1Si-icVfMaH6kqJO4D6fIT1G2Hr_0ef5crFVkp5FMgExnHBp1kt3m9_Iai_hwTXUj3Aeka_t_p2e64FZ5Wl8e3LuhcWt5XS7h9mlRA3hzZ0BQqo0nzCvN_D_Wjyp7X4nvTbLurj8jA2La9MO_abaCbshO-XKcg7C7xy-iY-IXWtpQR_IjIehxgFLoi4F9DviG112hhO2GRY0-WHSQfpA_2un7njVtv7ac96fqajwXkvwa_Wy199uoIwNfY7RjzsXq6AZ6Ki_ggDJQdi7J02t-2KSWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=OIq6ZQYhdAl0PHxIJxegt_C52MYHd0VZgxo0vP71rl2Jo_8_1YyoPyHAXTrK1Si-icVfMaH6kqJO4D6fIT1G2Hr_0ef5crFVkp5FMgExnHBp1kt3m9_Iai_hwTXUj3Aeka_t_p2e64FZ5Wl8e3LuhcWt5XS7h9mlRA3hzZ0BQqo0nzCvN_D_Wjyp7X4nvTbLurj8jA2La9MO_abaCbshO-XKcg7C7xy-iY-IXWtpQR_IjIehxgFLoi4F9DviG112hhO2GRY0-WHSQfpA_2un7njVtv7ac96fqajwXkvwa_Wy199uoIwNfY7RjzsXq6AZ6Ki_ggDJQdi7J02t-2KSWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
🔴
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
🔴
ولی اونا میگن شکست خوردید... این واقعاً چیز بدیه برای کشور ما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123882" target="_blank">📅 12:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123881">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B23Z5sSVcIYO5rnOcXKpCmnzKo1t7H560EWXotBvWGqvNmcLxYg5AbDQA2kfMDoCA6Eh6CI2fH3rrduSRBBUJco6BCKsfGPOvkmYlhF2dV5LMbwMP7-ZzRjo9kCw1_llGV1sh2sw4TQd99s1xKYcMvxEUYQudh0yfOrfp1Uss7T9FsDrD1P8jLXTvEb8c7qP_gBqGzTPk1z79GIytq5yOZhyJrloxFh8yquGpUZVZ5nATRj9cN2WpiRZLbKMcqPG-oxgG4IiRbBU6B-qZNb0kqE5a84smP0bhiH12j65dNB0KmoaQCIPXElsxOFxAOzjoGS41b4K1ojt9slNF37rwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل بار دیگر هشدار تخلیه کامل جنوب لبنان تا رودخانه الزهرانی را صادر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123881" target="_blank">📅 12:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123880">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: برخی اخبار حاکی از موافقت آمریکا با شرایط ایران است
🔴
ابراهیم رضایی: همه موارد به تصمیم آمریکایی‌ها بستگی دارد. جمهوری اسلامی ایران چارچوب و خطوط قرمزی دارد که به هیچ‌وجه از آن کوتاه نمی‌آید. این آمریکا است که باید تصمیم بگیرد، تسلیم دیپلمات‌های ما خواهد شد یا تسلیم موشک‌های ما.
🔴
مواضع آمریکایی‌ها متناقض است. برخی اخبار حاکی از موافقت با شرایط ایران است و گاهی هم گفته می‌شود که آمریکایی‌ها مواضع خود را تغییر دادند. برآورد دقیقی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/alonews/123880" target="_blank">📅 12:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123879">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سخنگوی حکومت سرپرست افغانستان: توافق فنی‌ـ‌نظامی اخیر طالبان با مسکو برای حفظ امنیت و تقویت توان دفاعی امضا شده و کابل برای همکاری دفاعی مشابه با سایر کشورها نیز آمادگی گفت‌وگو دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123879" target="_blank">📅 12:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123878">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی گزارش می‌دهند که آمریکا به اسرائیل اجازه داده است تا فراتر از جنوب لبنان عملیات و حمله انجام دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/123878" target="_blank">📅 12:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123877">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937516b130.mp4?token=bukCYJCfVLiM4f5VpbxuU8MEVBh2uM_goIQH8OqFz-gUunC6LJVtJs5rODJkN0iG0bQ8D3hzi7SFfPJrSWmByYrIXAJ1A9QvSM5GoqdUSWyaJUSvU8vbXqouhiAzyBONZ2pjvRchgmQ41QbbxA1Xbw5uHMMnPgykWrfDJbX4OE9molf207chzTyy20tHBFOaQGrfHQfG9ePykP5Gj8w9vMNnf991FicGOk8FXXuUt68BcnoTsr-6WDQUhDAumoPos9u5I4YGyjT1B1RjbutZuMEAt7SAxbLFii_lVPBfrTIHtqn69R0PBxn0lEuexm2qbM9c9te_Z7qdA-3cvyIIuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937516b130.mp4?token=bukCYJCfVLiM4f5VpbxuU8MEVBh2uM_goIQH8OqFz-gUunC6LJVtJs5rODJkN0iG0bQ8D3hzi7SFfPJrSWmByYrIXAJ1A9QvSM5GoqdUSWyaJUSvU8vbXqouhiAzyBONZ2pjvRchgmQ41QbbxA1Xbw5uHMMnPgykWrfDJbX4OE9molf207chzTyy20tHBFOaQGrfHQfG9ePykP5Gj8w9vMNnf991FicGOk8FXXuUt68BcnoTsr-6WDQUhDAumoPos9u5I4YGyjT1B1RjbutZuMEAt7SAxbLFii_lVPBfrTIHtqn69R0PBxn0lEuexm2qbM9c9te_Z7qdA-3cvyIIuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از برافرایشته شدن پرچم ارتش اسرائیل در قلعه تاریخی و استراتژیک بوفور، لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/123877" target="_blank">📅 12:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123876">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pS6B2EkH7wU0FjUrbjI_kEQs__91O9VIrSydI498uVaZ8JMJDiGgtwJQaruBV1DYVisR8PfsVPH6FR_EWFnkbiXvetODUleDam821Ruo2zKwhg6lA_wYTnNKmwOtl5IXEpM1gsCI89Rf1k_HQd8dSDGFo299CXaZuqsA8nI96nhXwFUYyU2InJZNcfJ-IYYfTCGdSih38-GBrMIqp7quvETUN-4_d4LSuvsMcW2BgLb-9emajYZNAE7-ou2mOCtAFmPWHzuSSy0-Pywd6ncXny-rYOSAbZiq4LWmdSo_-ijX7NIwYekQJGWqL1l-uvuHPj7wJSA7MEYHUbaDf-yeMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اتحادیه اروپا در حالی که جنگ در خاورمیانه وارد چهارمین ماه خود می‌شود، در حال بررسیِ تعلیقِ موقتِ سقف قیمتِ نفت روسیه است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123876" target="_blank">📅 12:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123875">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEIfXd_oMWtXyqcTWh-2IspdJ4q20-EFNa8tdS6Ab8ARtL-MRr7-Rd6DYa4mrSKifpm1vOnUbjMwiuje57k-LpVfXZzbasrCdtowUIId2GKDjb9mN86AKgzIa-xGfkRLTQfqYr7d5maXgqDvATYWBSXf0peqz1qdBobyWH9yurGmdqUYX-3Ot1GfbnyDJ4e9gl7V2j5KDEOPXpNgjEMhHhTeSSDAbG7vNzFY2yHOjkDopT9KX18rEsOKQO_Qd5VeesGkhODbiLMK0oHD-RWPKFsi8bD7zZ3qd4vYuOe1NVSreJpqOCc_9S4ILmaNrXkhKW7P9un6bkDBueFD0506dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نمای نزدیک‌تری از بخش دم هواپیمای سوخت‌رسان KC-135 با شماره 63-8028 متعلق به نیروی هوایی ایالات متحده که هنگام حضور روی زمین در عربستان سعودی بر اثر ترکش‌های پهپاد/موشک بالستیک ایرانی دچار آسیب شده ولی کماکان در حال خدمت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123875" target="_blank">📅 12:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123874">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_9wQZlbZK37GcZMDJGA_EBnVGFPPCuTp3ZlXVn8mTpWod2DLusg4gzSJrzVglJisG6pdM269PRtEWiRbpvJKc1H-G10Th1svLL_KxpXd0LRIWmMXjABSKr9aZ2hcCAXDeq4i2ZBhwi50KiUX_6vk6jqhQiE7CUDuMxKQ7gTX4kid60iDBa9Qdbf_OxJl6tMPO76zgjaZ4mWaU5JHojwzRIcv9ZFR2qPXJ2L9yRm4oG5PKCTKOcQK3Cl5lNDaVdbkmrqaXv7Du-Enoe4J4Q7XMSeRsunNpFkR58GYa_RvS9GprXTuQ2B7W-eJAYps2VyfiKHu70sUjrDA-jhMXJJiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/123874" target="_blank">📅 11:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123873">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سپاه: طی شبانه روز گذشته ۲۸ فروند کشتی اعم از نفتکش، کانتینر بر و سایر کشتی های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/123873" target="_blank">📅 11:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123872">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUK14o2m2o__W5GSOLcn0O8aISBicMlznH5he61oag4UuK-oRJIvBWRAcO7FG0oMX9CZvUwczEo5_GZ9lHsOqL-5xOHVCNqOJNckcHyPrqOiAgGD3jsQYw6B6_PoYpN9_tIcUZ_NtaWrh_c3fH-DRyVXR2ndeCCF40sQtpJGWBRqIqF6Qt_tMz3I4LW79D3ESV6YjFV8FnEyZ89-3XOoJg9lWceREZnu2DQ8wdLR9IM_QIotSTpL_WhW6iVXrHW8JwzBY8CZ5nXNPCWdbQnOUmTftBk8Ic_5CpbVwuA4TPgEm628MnhprZNBWs5xCjys42eiZFep7zpZPW8dZiOXGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تردد خودروهای پلاک مناطق آزاد در سراسر کشور مجاز شد
🔴
بر اساس ابلاغیه رئیس پلیس راهور، محدودیت تردد خودروهای پلاک مناطق آزاد در سطح کشور تا اطلاع ثانوی برداشته شد.
🔴
مطابق این ابلاغیه، خودروهای دارای پلاک مناطق آزاد کیش، قشم، اروند، چابهار و ماکو می‌توانند تا اطلاع ثانوی در تمامی جاده‌ها و محورهای کشور تردد کنند.
🔴
طبق اعلام پلیس راهور، این مجوز تا زمان عادی شدن شرایط و صدور اطلاعیه‌های بعدی معتبر خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/123872" target="_blank">📅 11:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123871">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
منابع آمریکایی به خبرگزاری فرانسه:
ترامپ به دنبال توافق صلحی با ایران است که «خطوط قرمز او را برآورده کند»
🔴
منابع آمریکایی که نام‌شان فاش نشده به خبرگزاری فرانسه گفتند که توافق صلح منتظر امضای دونالد ترامپ است، اما او پس از جلسه اتاق وضعیت کاخ سفید در روز جمعه هیچ تصمیمی نگرفت.
🔴
یک مقام کاخ سفید که نامش فاش نشده است، گفت: رئیس جمهور فقط توافقی را امضا خواهد کرد که برای آمریکا خوب باشد و خطوط قرمز او را برآورده کند. ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد.
🔴
ترامپ گفت اولویت‌های او برای هرگونه توافقی شامل موافقت ایران با عدم توسعه سلاح‌های هسته‌ای و بازگشایی تنگه هرمز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123871" target="_blank">📅 11:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123870">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
بی‌بی‌سی: صدها نفر پس از جشن‌های دیوانه‌وار لیگ قهرمانان در فرانسه دستگیر شدند
🔴
درگیری بین هواداران فوتبال و پلیس در سراسر فرانسه منجر به بیش از ۴۰۰ دستگیری پس از پیروزی پاری سن ژرمن (PSG) در فینال لیگ قهرمانان مقابل آرسنال شده است.
🔴
هزاران افسر برای مهار ناآرامی‌هایی که خدمات اتوبوس، قطار و راه‌آهن را در پایتخت پاریس مختل کرده بود، مستقر شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123870" target="_blank">📅 11:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123869">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی گزارش می‌دهند که آمریکا به اسرائیل اجازه داده است تا فراتر از جنوب لبنان عملیات و حمله انجام دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123869" target="_blank">📅 11:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123868">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
میدل ایست نیوز: سرمایه‌گذاری میلیارد دلاری چین در عمان
🔴
دولت عمان با جذب یک پروژه استراتژیک یک میلیارد دلاری برای تولید مواد مورد استفاده در باتری‌های لیتیوم، گام بلندی برای ورود به زنجیره جهانی تأمین انرژی‌های پاک برداشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123868" target="_blank">📅 11:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123867">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5411c3d8c3.mp4?token=uHtttZZVnXnb-Ii-E3k2ps9AaqyfVc7qwGy0BipoEo5faaLVAIcM-Cp7o3sjumZmIxO6jMgZEeSzDEkLO8slMAzEG-LYksgH3wGN1G0H6AASh9jwclCb_7SM_2b9cRqVqMFEhC3Nxcv4mROV-Grb3C52RauILPOWiq0I5Zwm4iw1jcEeqNTlMCb7GyoWAVHYxRnFe0Js8DFz6JahocuB1P_B8tl3nNe7kWs6ENS8ZeVXYe-NuTggrv-3dgP1CtXiEAx7wlfx9BC2_A17sgJ1VJs9F7sSgUQMTf31RCDyL_lOEW8KhMvP8pJ4SBwrg_sgg9sGK4abPl5Wt4AICcn3fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5411c3d8c3.mp4?token=uHtttZZVnXnb-Ii-E3k2ps9AaqyfVc7qwGy0BipoEo5faaLVAIcM-Cp7o3sjumZmIxO6jMgZEeSzDEkLO8slMAzEG-LYksgH3wGN1G0H6AASh9jwclCb_7SM_2b9cRqVqMFEhC3Nxcv4mROV-Grb3C52RauILPOWiq0I5Zwm4iw1jcEeqNTlMCb7GyoWAVHYxRnFe0Js8DFz6JahocuB1P_B8tl3nNe7kWs6ENS8ZeVXYe-NuTggrv-3dgP1CtXiEAx7wlfx9BC2_A17sgJ1VJs9F7sSgUQMTf31RCDyL_lOEW8KhMvP8pJ4SBwrg_sgg9sGK4abPl5Wt4AICcn3fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از کافه‌ مروج شیطان‌پرستی در خیابان ولیعصر تهران که توسط پلیس پلمب شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123867" target="_blank">📅 11:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123866">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
فرمانده انتظامی خراسان شمالی: ۲۱۵ تن برنج احتکارشده، ۴۸ تن آهن‌آلات و میلگرد و یک‌ونیم تن آرد در استان کشف و ۴ نفر در این رابطه دستگیر شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123866" target="_blank">📅 11:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123865">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
الجزیره: روابط روسیه و ایران آنطور که به نظر می‌رسد نیست / هدف مسکو تضمین عدم انزوا، فرسایش یا شکست استراتژیک ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/alonews/123865" target="_blank">📅 10:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123864">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سنتکام: «پس از آنکه خدمه کشتی از تبعیت از دستورات خودداری کردند، یک هواپیمای آمریکایی با شلیک یک موشک AGM-114 Hellfire به اتاق موتور کشتی، آن را از کار انداخت. این کشتی دیگر به سمت ایران در حرکت نیست.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/123864" target="_blank">📅 10:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123863">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
پزشکیان: همچنان در برخی عرصه‌ها با فاصله‌هایی نسبت به کشور‌های پیش‌رو و حتی برخی همسایگان مواجه هستیم
🔴
فشار‌ها و چالش‌هایی که امروز جامعه با آن مواجه است، ساده و تک بعدی نیستند و راهکار‌های آن‌ها نیز ساده نیست
🔴
مدیریت نباید به حلقه‌ای محدود از مدیران و تصمیم‌گیران منحصر شود
🔴
نباید در جایگاه تماشاگر و خارج از گود باقی ماند؛ حل مشکلات کشور با نظاره‌گری امکان‌پذیر نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/123863" target="_blank">📅 10:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123862">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc46929eda.mp4?token=ZFH9Skelm9YAWZ2z044vsJImrIZYzJpFYg1He6XZTCQdIbW9RzXZQcSrEt8kBk3t3DZzIbF6A8R4-QLEzG-MsstgGFKBMWho3_Pcw3NJGSaPsWTWrWXrj58oGcWgrXdux2vrLUI9K1fh__7NIzj1yPA_Fiyf_kESrEkFnxpUshoY8ZhiFhub5hemTirBEzj8NmlocITJPMbfxckD_uBWFC_oyG8And9TuNVfFrjIIsmEr9ijhUPr6gvgB3HKKJVQF21FCFxMSCzWL6V3bYk9oC0nulzrG8GV-WrOCRwi837xIUxqQ_QUBLPxUFK339cSZB8wg3yj_purAntsWR6fpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc46929eda.mp4?token=ZFH9Skelm9YAWZ2z044vsJImrIZYzJpFYg1He6XZTCQdIbW9RzXZQcSrEt8kBk3t3DZzIbF6A8R4-QLEzG-MsstgGFKBMWho3_Pcw3NJGSaPsWTWrWXrj58oGcWgrXdux2vrLUI9K1fh__7NIzj1yPA_Fiyf_kESrEkFnxpUshoY8ZhiFhub5hemTirBEzj8NmlocITJPMbfxckD_uBWFC_oyG8And9TuNVfFrjIIsmEr9ijhUPr6gvgB3HKKJVQF21FCFxMSCzWL6V3bYk9oC0nulzrG8GV-WrOCRwi837xIUxqQ_QUBLPxUFK339cSZB8wg3yj_purAntsWR6fpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اگر به ایران حمله نکرده بودیم، از سلاح هسته‌ای استفاده می‌کرد و دیگر نه اسرائیل و نه خاورمیانه وجود نداشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/123862" target="_blank">📅 10:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123861">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=ew8t2FPVQAksFJ7KwrfQs8y7kIExhaWta1CZC91TLXzM8WnBLDMVP0eHkx8ybjxpJKWy6dWDinhrFyWi1XCfbmORrtr8u_I6h-tl8L6L3cOPM5LekC7wJSJ-T2qmDl9xMNisnupUX4MBNBuUjpRB7-2ZGW8Qacq0TKU0MEvyWwiD8QI4ma4uNx9ieDIK7LS945Pf3QriAKndd62pc_Nn37XeO50fhx_BTzNC60lN25G-qL74jWy7mwEyg6MDdEyeaRQWlg59ufvHK1chQxqwm-qTaZg0YISLBA5ngStxEe5ujltwKsmjeNcZFAchgn3AEoW0luMyR0Jjc5HobrfqCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=ew8t2FPVQAksFJ7KwrfQs8y7kIExhaWta1CZC91TLXzM8WnBLDMVP0eHkx8ybjxpJKWy6dWDinhrFyWi1XCfbmORrtr8u_I6h-tl8L6L3cOPM5LekC7wJSJ-T2qmDl9xMNisnupUX4MBNBuUjpRB7-2ZGW8Qacq0TKU0MEvyWwiD8QI4ma4uNx9ieDIK7LS945Pf3QriAKndd62pc_Nn37XeO50fhx_BTzNC60lN25G-qL74jWy7mwEyg6MDdEyeaRQWlg59ufvHK1chQxqwm-qTaZg0YISLBA5ngStxEe5ujltwKsmjeNcZFAchgn3AEoW0luMyR0Jjc5HobrfqCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ : اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/123861" target="_blank">📅 10:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123860">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7614fe349.mp4?token=Sw5157SHYs9MkA1yq4TbXj0pnV2LCm18Hs29PsPgP_CxWEzG1A_zwbdLvSfQm8MMUtoV1_vQHI0sgp9C09gSnax1if2MjEioupHBBD6GpmprbejkKY1WhLK2DZsd1LE7_PC1M834ZE2qqjoEmPI_azqTQZEqRotgfKu9T144yUnxb1cVI1Of3OZ21715tQffqrdXoFc1oGon8_Nc_J9YKtOSSDlaEYtxhljUj41Wq7mLycpPyneIDEvc-PCRTUNKxjTlJjaG4D4FkHu8u7DrKHkiba5Gv4ehzGFrwU7ss7QRRc704UpVY43IIYXss3ixk03PBEXxjTrSkKbp-rRGFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7614fe349.mp4?token=Sw5157SHYs9MkA1yq4TbXj0pnV2LCm18Hs29PsPgP_CxWEzG1A_zwbdLvSfQm8MMUtoV1_vQHI0sgp9C09gSnax1if2MjEioupHBBD6GpmprbejkKY1WhLK2DZsd1LE7_PC1M834ZE2qqjoEmPI_azqTQZEqRotgfKu9T144yUnxb1cVI1Of3OZ21715tQffqrdXoFc1oGon8_Nc_J9YKtOSSDlaEYtxhljUj41Wq7mLycpPyneIDEvc-PCRTUNKxjTlJjaG4D4FkHu8u7DrKHkiba5Gv4ehzGFrwU7ss7QRRc704UpVY43IIYXss3ixk03PBEXxjTrSkKbp-rRGFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره ایران: ببینید، دو چیز میخواهیم:
🔴
1ـ تنگه باید فوراً باز و آزاد باشد، بدون عوارض.
🔴
2ـ اینکه آنها نمی‌توانند سلاح هسته‌ای داشته باشند.
🔴
همین است؛ خیلی ساده است. سپس ما از آنجا خارج خواهیم شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/123860" target="_blank">📅 10:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123859">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQS6Fc3AA2PUC-wdBcKgv-36jXiLw-h-KZBBTyYTtKW8kGrIoZk0rDZd-tqerW3bSWOjodBRemdFY0EC4cp837MWkstMGSZxqN4kMEgpHATMrHhEIUkUw8RIrzwlIUEAp7ESHnVGyrf5VIjnhX2V7BwRjWqou483zcZ0P7Jb4ifWJPhLccNHzv1aS-DhchQJUnpUjGAkDCWjsrSOfp-8dp3SzG6mN6sm8j95EgJvbr2b2_q7uV3_3tvEFB5377oy_bvr-HJt7H2SB4SOfJ9vWzSrdiixDY9yPnbXP-1LZEhYkDxRKR_PAnG1b7MZNg8Oiwpq4HIf-E0AsZbqnAxh2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تلاش است جنگ ایران را تقریباً تمام شده و کاملاً موفق نشان دهد، اما روایت او با واقعیت همخوانی ندارد و پس از سال‌ها تحمیل نسخه خود از وقایع، اکنون با بحرانی مواجه است که با داستانش در تضاد است، طبق گزارش نیویورک تایمز.
🔴
در بهترین حالت، تغییر رهبری رخ داده است، اما ارائه آن به عنوان یک تغییر مثبت توسط طرفداران جنگ نادرست است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/alonews/123859" target="_blank">📅 10:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123858">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
آکسیوس به نقل از منابع: درخواست های اخیر ترامپ جرقه دور جدیدی از رفت و آمد بین واشنگتن و تهران را زده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/123858" target="_blank">📅 09:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123857">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
یکی از مقامات کاخ سفید، به آکسیوس:  آماده ایم یک هفته یا بیشتر منتظر بمانیم تا اطمینان حاصل کنیم که رئیس جمهور به خواسته های خود از ایران می رسد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/123857" target="_blank">📅 09:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123856">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
یکی از مقامات کاخ سفید، به آکسیوس:
آماده ایم یک هفته یا بیشتر منتظر بمانیم تا اطمینان حاصل کنیم که رئیس جمهور به خواسته های خود از ایران می رسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/123856" target="_blank">📅 09:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123855">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAGLiiYeyuZVmVSU_bOdIDlrRsxlzgybhmudsVi_5Xak_hUHMFy2MUcv5CaKUqnJ5FoL8nUbSrquVId9TzayjUNbCpnnT8PjMLarXA4Ry0sm5FXzp4ctErv6Rvh-sicdM-6zdUNhKkiTlgo41T1C7kN_fcpT_vKimiRpD6VybK82i8Jehv0OUejvAWAHxViTD_s5_UctIPaXFqGR1BhOUQXDuytYcEkI5Tfpc5a1kFJdIv_pOE-O5bk69Fqmjnm2o1wPO7yuS_85RLyx9zojwpRBgd7bvYJJQBx4oDGojcOtqfvO7SbhjyhXSmc-pjkWVIGbzbBbt4FTkedFEIal4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بورس برای دومین روز متوالی سبزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/123855" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123854">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xs4JsOhn1cbgDX8TgwYne0hzuqntgNt3r-PnQVg-cCGpZcUX61EsmCOZQQSwZFeM4laloE66LKkRuowauhiQ9Oh146kBmltOC-ZunodQX01fNI60x5dUDzwXwXkfitgfm9f8iVavo79CnvVIsutAr4k4YxNTxvcZ095QaMMs9eCfWqiVkki-5UV07pRmDmXV6uqUJ9oQUGKcZAZZdbQUpF3GX03N7fVTxEsFv7UwwVi06UhOyfuJZ6SjGdjfjbaQ5RbYfK7QoeDGN0jaFwIZeIpzmOuEslcKpn09_VnjtQSqnyw8kHROz8iDd5d6BO8I2Z6T1s_vn0bJN5O6pBi9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در Truth Social:  «دارید گیج می‌شوید»
🔴
دونالد ترامپ در پیامی کوتاه در شبکه اجتماعی Truth Social نوشت:
«You’re getting discombobulated»
که میتوان آن را به «دارید گیج و سردرگم میشوید» ترجمه کرد.
🔴
ترامپ توضیح بیشتری درباره مخاطب یا منظور این پیام ارائه نکرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123854" target="_blank">📅 09:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123853">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
روزنامه جمهوری اسلامی: دستور پزشکیان برای بازگرداندن اینترنت بین‌الملل کاملاً مطابق با قانون اساسی است / فروش اینترنت پرو هیچ توجیه قابل قبولی ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/123853" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123852">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
جزئیات ثبت‌نام دانش‌آموزان در مدارس سراسر کشور
🔴
پایۀ اول ابتدایی: اول خرداد تا ۱۰ تیر
🔴
پایۀ هفتم: اول تیر تا ۷ تیر
🔴
پیش‌ثبت‌نام مدارس شاهد:
🔴
پایۀ هفتم: اول تیر تا ۲۰ تیر
🔴
پایۀ دهم: ۲۵ تیر تا ۱۵ مرداد
🔴
ثبت‌نام پایۀ دهم (عادی): اولویت الف ۲۷ تیر تا ۱۰ مرداد، اولویت ب ۱۱ مرداد تا ۳۱ شهریور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/123852" target="_blank">📅 09:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123851">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUJF8gBH9aAWASY8Rr3U8iEq-UPeVBryhrMSQJZxYIHm4zwMeZ2-fg8gkOhy_cZM9pOjCchLam4YfE0bEOYWg9Xc29sWQ0gtrxnM5zX55p_7ITg0mEfXILmAS5TMuEw_A06Oy_t8YyINmusIftFAOpk4EY_O3mnoJvJ4e0SuK33bsKYB_69W3w6RSUCHG8Ic3iRoBJC7aqD-YZrHTubMpmKi03lO_-73OadO3RGd-4C3GdiQDkJfjAaEjizMn3VVGZA4VeCiF79k48ARS7xOGPQaW2jmh4qQLUO6XoPdNCVtwBl3JqbXKuQ2O5864wuALtEvW3lDdlNiuE53vbhXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقشه‌های هواشناسی تا پایان هفته برای شمال‌غرب، شمال، و شمال شرق کشور ادامه بارش‌های بهاری را پیش‌بینی کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/123851" target="_blank">📅 09:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123850">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
اسرائیل هیوم: ایالات متحده به نفتکش‌ها و کشتی‌های حمل گاز مایع قطر اجازه داده است پس از پرداخت پول به ایران، تنگه هرمز را ترک کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/123850" target="_blank">📅 09:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123849">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
روابط عمومی سپاه: : رهگیری و انهدام یک فروند پهپاد MQ1
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/123849" target="_blank">📅 09:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123848">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ در گفتگو با فاکس نیوز: ما به یک توافق بسیار خوب با ایران نزدیک شده‌ایم. اگر این توافق برای ما عادلانه نباشد، دوباره به وزارت جنگ متوسل خواهیم شد.
🔴
گزینه دیپلماتیک را ترجیح می‌دهم، زیرا امضای توافق به معنای بازگشایی فوری تنگه هرمز به روی کشتیرانی است.
🔴
تنها تضمین اصلی و اساسی که بر آن پافشاری می‌کنم، جلوگیری از در اختیار داشتن سلاح هسته‌ای توسط ایران است.
🔴
ایرانی‌ها در عمل قبول کرده‌اند که سلاح هسته‌ای تولید یا خریداری نکنند.
🔴
ایرانی‌ها مذاکره‌کنندگان بسیار باتجربه‌ای هستند و این موضوع زمان می‌برد، اما من عجله ندارم.
🔴
تنگه هرمز باید فوراً و بدون عوارض عبور باز شود و باید به طور قطعی از در اختیار گرفتن هرگونه سلاح هسته‌ای توسط تهران جلوگیری شود.
🔴
نیروهای ما به محض بازگشایی تنگه هرمز و پایان یافتن رسیدگی به پرونده هسته‌ای، از منطقه خارج خواهند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/123848" target="_blank">📅 08:56 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
