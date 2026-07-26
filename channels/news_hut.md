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
<img src="https://cdn4.telesco.pe/file/PYvkd-GTfp9RNpmKWmsuepLgvDaLAPwRDvz7YXofKsG_C-LMOf7PppC9eW_AR1JjDu1K_zN3hSYYsV9ZmGs0Yvd9t9vJtqDQ2kyyeehLKb3SxEHnC2DC1ZTBOhWV31OlZ2_VOJObeSwD7RND4WcFRmHN-6gImuHzvbII2IVMA4DCYaneKJmq-OCEsQ8rB9lZ77kIVRFKR3aBTMjCWrpe6RkuDQ9_D03xAY7anW1INRYqyVoWhQt-8sjCmR_XioTG0M8xRlyi6QyQhaxWppCN4PquuF7D9L3iiRnocQRSCwcc72X2cDpSFRp02KffArMwGsL_Si4hIyiD1LZatzbH-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 147K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 21:25:13</div>
<hr>

<div class="tg-post" id="msg-69022">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbeqHRoYFDIkOOY0akZ1BOqNs3G-GChr9bx1bbevs725x3ZIEUc1LIqzoa5HTih4UuHWgWNd_er-MAsGqfbsSnUr31N3PvKL4bHY3jOyV8pGo7ph5P5A5fy4W_MWfsPARa1Wcevivu1DHSgn_5hiLVXTn9hv9ZrTGNAwnu07tnIdo9KremnOGfQAPviVtDM2y0SLhdsYIyNVejjlvFXcSfOD_WNejeVVoT6xAIfDVH8Uq0vJQ2tI0gHa9t9p68uUVVBNdPpJE0nFEIbsPBj1NjU37XY7neHolLEoerR5oMfowm8jLGuigVnUtUSY2jzkJ5WQHFGXrgvqbKMdU8OIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ان‌بی‌سی نیوز:
فرماندهان نظامی آمریکا عمداً به برخی از موشک‌ها و پهپادهای ایرانی اجازه عبور از پدافند هوایی خود را می‌دهند تا ذخایر رو به کاهش سامانه‌های رهگیر را حفظ کنند.
با توجه به اینکه ایران از آغاز جنگ نزدیک به ۹۰۰۰ موشک شلیک کرده است، فرماندهان اکنون فقط با تهدیدهایی که به سمت نیروهای آمریکایی می‌رود، مقابله می‌کنند - و اصابت به باند فرودگاه‌ها، رادارها و انبارهای سوخت را می‌پذیرند تا پاتریوت‌ها، تادها و رهگیرهای سری SM را که جایگزینی آنها سال‌ها طول می‌کشد، حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/news_hut/69022" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69021">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VO3x_yOkZ1Nh1aSNC9PNZdGBreW8lSjBsW6FlZA9E6CW8eUqwtuLBYUXHo4YKTarMvWlzvHw6aIT1Y3oVQyAAIHcX8oYfyexB72eh-vDRT41W1uSiXoW6X5KFgtrPecRG0r5rMb2WfhMofPUVENB0KqYtl9_EW1NdH3N4qmFgNHsGRiKD3zBvs78F86zhvJUd5E_CUU56UmQl0cATD-R-MEwiyKJX0m1IWhdgyZIVK4Ny4jr9A3uYvV35anvr6PtA62olYimTxmEd8XMN0IsGGyba_q8aZrswn0I8seYOl7vXsFHhvWEbfIlk4fK3ElPox8ExWOijxs1qwjqa1SMEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عراقچی:
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و موجب کشته شدن یک دریانورد شده است؛ اقدامی که نقض آشکار منشور سازمان ملل و به دستور اسرائیل، با هدف کشاندن اروپا به جنگ آن صورت گرفته است.
در گفتگو با «کالاس» (نماینده عالی اتحادیه اروپا) و «لاوروف» (وزیر امور خارجه روسیه)، تصریح شد که اقدام آن عنصر مفت‌خور در کی‌یف، هرگز بی‌پاسخ نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/news_hut/69021" target="_blank">📅 19:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69020">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78921238e.mp4?token=foNhdtwJQKho_gCIKy1OBgW0XkpieEAw9tk09DAPSxd8-Cja6JSZ0A4oF9JISCy6tuzEAvS7QZtDfb18_KtJbqwHTUNfnXQRqz0PkDhs5AolRz-9-tqOnEfl5EKH7uINRpFSNkRR7CBFiUgf13qZ1ZPdUxcKn5mESOPMwDh1rs5FUPRLw_LRHiePCvCRcHos2Z1YVAgkPdFqup1aPspdz08PTd2U5NCYlBQSjbCk2YGXTXmx_L-_bbJuClNqPcTvn2QVXbQc3fTHYBfwKE2b9Oom49lEQ-Gy2JlJNQSh8YNmHce0YI34t2burs453EiVqokBPFRIQbGFgwUp2g_K0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78921238e.mp4?token=foNhdtwJQKho_gCIKy1OBgW0XkpieEAw9tk09DAPSxd8-Cja6JSZ0A4oF9JISCy6tuzEAvS7QZtDfb18_KtJbqwHTUNfnXQRqz0PkDhs5AolRz-9-tqOnEfl5EKH7uINRpFSNkRR7CBFiUgf13qZ1ZPdUxcKn5mESOPMwDh1rs5FUPRLw_LRHiePCvCRcHos2Z1YVAgkPdFqup1aPspdz08PTd2U5NCYlBQSjbCk2YGXTXmx_L-_bbJuClNqPcTvn2QVXbQc3fTHYBfwKE2b9Oom49lEQ-Gy2JlJNQSh8YNmHce0YI34t2burs453EiVqokBPFRIQbGFgwUp2g_K0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوتا جوون خواستن برن جزیره لارک دیدن قایق نیست برداشتن شتر هارو انداختن تو دریا دارن میرن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/69020" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69019">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd02960948.mp4?token=RTbYuxlLCDmMEleV--o4CYoWhHtAJTMpxA8zR2b5U0Q8CZxmA9vLL2mhJQFE-SrJrMQ8aed_DmZpDxFeiVzV4FrtqAoKyv74n2NwJtx4Owg2yxHMXTwj_JmxqngP0X5l9eeVlGQl2ipywCAOWRS6rGOjmOWcL7Xpi0OoJRNqDNQaGe9c8J01QB-QGl42Mj8XKiUkJlU1D0Sk7zDaBZJfRdfCL1PjX-aq6IWLOMb5OEGvR8iIBU9DAZNVsL5KL_Hk9UQm8qeedY6OuqSci7M2WbQQj_MD3D-70bKY_CO7UKVxSVArmqRPGLv_KJa2Nc9xNXtszCkvnJMWubkluf4xRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd02960948.mp4?token=RTbYuxlLCDmMEleV--o4CYoWhHtAJTMpxA8zR2b5U0Q8CZxmA9vLL2mhJQFE-SrJrMQ8aed_DmZpDxFeiVzV4FrtqAoKyv74n2NwJtx4Owg2yxHMXTwj_JmxqngP0X5l9eeVlGQl2ipywCAOWRS6rGOjmOWcL7Xpi0OoJRNqDNQaGe9c8J01QB-QGl42Mj8XKiUkJlU1D0Sk7zDaBZJfRdfCL1PjX-aq6IWLOMb5OEGvR8iIBU9DAZNVsL5KL_Hk9UQm8qeedY6OuqSci7M2WbQQj_MD3D-70bKY_CO7UKVxSVArmqRPGLv_KJa2Nc9xNXtszCkvnJMWubkluf4xRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ویدئویی دست به دست شده با این مضمون که اگر فکر می‌کنید ترامپ واقعاً دنبال اینه مذاکره کنه با جمهوری اسلامی سخت در اشتباهید، این ویدئو رو ببینید تا متوجه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/69019" target="_blank">📅 19:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69018">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=N70qWbOSlzoRyX8Bx7EdCaQvNZrgp_NudCwccpi4IC_qeQaW1oR6-PGjVruMftNUyweJ95s3dClptGn68oVSHwauOEXldrpzwR_YcDEilzfmn27PXz3YCKko5xJlCvAQG1iEhzp-dH6xajMANuaRSyvBnqeB8sOHcy7sgHXYxZ6m-ObZwRHhMRWfw7UoOEjSntZ9PolKkBfApFVE849zcgERDctq0oiBcZJe2cIMxQH5462YZlVCthigKTaXYuE8_BIWjW1ySOaUcre_9lxk6NSR6tIm7GOQE6nOxRZjX1F7dzJTJgQ0qfosOPCFIjNaBD53ZH8lyAocnXLNZwxhog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=N70qWbOSlzoRyX8Bx7EdCaQvNZrgp_NudCwccpi4IC_qeQaW1oR6-PGjVruMftNUyweJ95s3dClptGn68oVSHwauOEXldrpzwR_YcDEilzfmn27PXz3YCKko5xJlCvAQG1iEhzp-dH6xajMANuaRSyvBnqeB8sOHcy7sgHXYxZ6m-ObZwRHhMRWfw7UoOEjSntZ9PolKkBfApFVE849zcgERDctq0oiBcZJe2cIMxQH5462YZlVCthigKTaXYuE8_BIWjW1ySOaUcre_9lxk6NSR6tIm7GOQE6nOxRZjX1F7dzJTJgQ0qfosOPCFIjNaBD53ZH8lyAocnXLNZwxhog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
مداح حکومتی خطاب به ترامپ:
"تو گوشِ کَرت اینو فرو کن، خارک‌و‌سه جزیره مال ایرانه"
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/69018" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69017">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hm0Jj9lN-z4W_ajLriiR0duhnv-GVsedoKabU3HUh_xVWPaaEiNHZP2pnE0E7Z5Wn1v3DBraNagsuc98T9koSw-IXT5uFD_DRDxkQUhUy_vj9eHNFLrxLfB6jd3yqeGTY8-fqSMdd17ra4PdyySddpgaC_FXXm2Yg71_58kdB6fhJJ4qEFwr0WYHs_NglLvAqRb1KM8jPhVlA4kE6kLQxlUKT328V5FsUBEoOZzLTNY_Wf0IjhoJ-pgVZkY2inqQu3K_0Q8wWFxOPx_RmaZWXEGW6s3BRk2mAtDZXJjbWd8yzrYyfmNd_Q22YXXnOUcQn0mv-j11SpdFBMAmhlkGzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
العربیه:
- ایران به پاکستان اطلاع داد که از مذاکرات خارج نشده، بلکه مشارکت خود در آنها را به حالت تعلیق درآورده است و تمایل خود را برای از سرگیری مذاکرات در دوحه، ژنو یا اسلام آباد ابراز کرد.
ایران به میانجیگران گفت که با ایجاد مسیر جدید در تنگه هرمز موافقت نخواهد کرد و به پاکستان تأکید کرد که باید طبق یادداشت تفاهم به مذاکرات بازگردد.
ایران خواستار آن است که مذاکرات ابتدا بر تنگه هرمز، سپس بر دارایی‌های مسدود شده و در نهایت بر مسئله هسته‌ای متمرکز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69017" target="_blank">📅 17:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69016">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=BQ1Kl_QBWfL4UaDlToECrfqBqKIIzJbLsFgBe9NSieB1yFFBIIWVFy9ywWa5LSdknTDWi-PI6MPP-ADN8g38Qr1I_O90NEtKAW9EQNewHx7oT3iw2PpygbAcgZPpisb74Kw0NqGdUQ9Ngu2YRtYgJ2tFpOKTtuN9JkHsqPkDDn2ZP-medtUm0T5MIqfWwTVN2AwfqvID7ZqXFrqIK62CoAJM--bYx68MermWiVayfjAgx1tOyNMZb4x7aSqofA6QWsAFRFFuX3n5vCDRiA4t9vHjN8w6CF8_q5v7qRLVbxqEuWgaVJlJHRJriHul5DGMJWX28LF-coPQ_smNW87T9YE2QcWpyPkOufrymRIxsHLHEcv95wDFi4lkXj13cR0w6SFsbBSXeIGHtI1rRIa8KVEZDhC4VGalJUrPiD34Z5NGFgg4U5cp_byFaJMoADdFdJhQC9TQnyB77_738ZL9wRDuk4ahbVLqHB1-2-jF5cqMJzZbbd-eAhvnaNNtXNiWaOANZd4hiclRUHi1z4ZIfXVQouxwJ5F4S7CuYuIrlREb383iNQntAiMHFCWizpG6ZPevm2uyAxPj3OudlvpA0TmLNunx-GcLhoe1Nw_xce8KDLVAckK_L30FhTcoL9IBN1EpqfsKu4OROWI73ArjMr3Sg5QjFEbbVEgz_dQ-RbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=BQ1Kl_QBWfL4UaDlToECrfqBqKIIzJbLsFgBe9NSieB1yFFBIIWVFy9ywWa5LSdknTDWi-PI6MPP-ADN8g38Qr1I_O90NEtKAW9EQNewHx7oT3iw2PpygbAcgZPpisb74Kw0NqGdUQ9Ngu2YRtYgJ2tFpOKTtuN9JkHsqPkDDn2ZP-medtUm0T5MIqfWwTVN2AwfqvID7ZqXFrqIK62CoAJM--bYx68MermWiVayfjAgx1tOyNMZb4x7aSqofA6QWsAFRFFuX3n5vCDRiA4t9vHjN8w6CF8_q5v7qRLVbxqEuWgaVJlJHRJriHul5DGMJWX28LF-coPQ_smNW87T9YE2QcWpyPkOufrymRIxsHLHEcv95wDFi4lkXj13cR0w6SFsbBSXeIGHtI1rRIa8KVEZDhC4VGalJUrPiD34Z5NGFgg4U5cp_byFaJMoADdFdJhQC9TQnyB77_738ZL9wRDuk4ahbVLqHB1-2-jF5cqMJzZbbd-eAhvnaNNtXNiWaOANZd4hiclRUHi1z4ZIfXVQouxwJ5F4S7CuYuIrlREb383iNQntAiMHFCWizpG6ZPevm2uyAxPj3OudlvpA0TmLNunx-GcLhoe1Nw_xce8KDLVAckK_L30FhTcoL9IBN1EpqfsKu4OROWI73ArjMr3Sg5QjFEbbVEgz_dQ-RbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا از انواع بمب سنگرشکن و هسته ای اگاه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/69016" target="_blank">📅 17:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69014">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=eCeyXEAS90Ms4bWk3r3oXJqZ-geH2lnQq1q9eYt8Cv6prDnTVR9N05lABubjnqTmZd2c3MBqYru2Yz9HiILcp-qZxeRhf2DddfodKWfRhhgIEVWGfxeHUxJWKQJqw5Q867b50IkfS9oMYzzA_lTshzpyaMjxY3zZFAUNZyoYVfPYJgykUwGvg3Pj5HgfZk6JGDqglVDBP2AhcFwAti_cBYYsS3c1OHvMLPdhNDRonAkHqsTbLlmcpvm5Py75mLG-hcdDEsDpUFxEXZLl3gsjNTkw2RbffeLB1UCjl2CSxFXBG183KOYMgvkZZ64Z0tNBNxR99ozHss3K3BsOvk5BjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=eCeyXEAS90Ms4bWk3r3oXJqZ-geH2lnQq1q9eYt8Cv6prDnTVR9N05lABubjnqTmZd2c3MBqYru2Yz9HiILcp-qZxeRhf2DddfodKWfRhhgIEVWGfxeHUxJWKQJqw5Q867b50IkfS9oMYzzA_lTshzpyaMjxY3zZFAUNZyoYVfPYJgykUwGvg3Pj5HgfZk6JGDqglVDBP2AhcFwAti_cBYYsS3c1OHvMLPdhNDRonAkHqsTbLlmcpvm5Py75mLG-hcdDEsDpUFxEXZLl3gsjNTkw2RbffeLB1UCjl2CSxFXBG183KOYMgvkZZ64Z0tNBNxR99ozHss3K3BsOvk5BjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👑
شیوه برخورد با آخوندها در زمان رضاشاه از زبان خمینی.
رضاشاه، روحت‌شاد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69014" target="_blank">📅 16:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69013">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g75wtzPZw2SblXu6oXv5BZ6InUgOfJGiJNDS6VdHetuZLJ77wDSsl7o_Q20Kk2v4W4U6ri0uz2DrjIBinIkSc3s3Ik-Vd9TqKtwMcYNL3Epxj6dhCKz2Ugmjot4AA_9G9360td4-p1TFkLN27Bj0JLgmTxb-gzuahMSos42sSYWuL7NeFwp7CxexRid0KLmW0QrSxXka4tfSMmxkregjXJssT1N2CwPw-gWjm6dlUHqfG8DA4vrtEpOETP5upkUbokYxGH4f88BjeK2Mb8ekMwYkaz_mhl68CfeJChCOtIeytOtriJAaR-ZuY76eRTu2aNIzk3FoOnkWr7X1Vxg3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
العربیه:
آمریکا و ایران به پیشنهاد مشترک پاکستان و قطر برای ازسرگیری مذاکرات، پاسخ داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69013" target="_blank">📅 15:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69012">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH-NTtkv-Up4LkjTEf8KPckOUWDbxnriyLA65RRPt518bla9DVh14li0S9MDzsQER3PcDHiPudoI6M4KoZM2dVGSesa3Z8ETS24l_waza2LiJR2m9jBeENORsPlnQAbCSk2jvygpAbbH8cG0R5m9NYdJ8m4G2jOr6I3Jna1M-s2eGNhXr4Ewz2sl8k3-CWn3gR792ZZk6IjakKo4j_uNu3t4Si0IPQyIDxw1_IsnCoCGrNgbO3Z1BqftXM48FenACPR7_p5QcwBnNno2FCtHncE98frk6EkT2mdOKgV4u-V0Xf_YC7V20_Cr4s7f0GzrpSYQWkn_obU2JpqxbS8PZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امجد‌طاها روزنامه‌نگار عرب:
ترامپ حملات علیه رژیم جمهوری اسلامی را نه به دلیل مذاکرات، بلکه ظاهراً برای انتظار جهت برگزاری جلسه رهبران اسرائیل و دریافت آخرین تحولات از سوی آن‌ها، به تعویق انداخت.
این وقفه بیشتر به خریدن زمان شباهت دارد تا تغییر مسیر؛
تأخیر به معنای توقف نیست و آخر هفتهٔ پیشِ رو می‌تواند سرنوشت‌ساز باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69012" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69011">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=NbvSKvRjnN_HwY-a8jtZWyDeSfKANY9kv1huz5KGbphcfVLwFPxE_3BT2cwqowx7Eb0D4vgY9Xk_ArsMpQ4TbFMKvqviI5VaeaGOC0LNd80fi2Gl8AP_0cy_HpPuC5I-drxN1XKYHIBjbNAMBLxhLavwa22snLqaC_GnBZFRpVoMcxsKFP4kl9yKvJ-y-Ye98Nb0o3zA0iZtzkgm6LvKkSHZdoN0ats_RO4IYcgjtXq40UwTNWhLlttsl9ZCgohtUWnZkSNN_JoFmNnTy2wM3vhp1e2BT5Gq4q8w-IxvOku8Jl_rnj_0qdRn0R_2_gJWn06rUMOcZXUmMehfzJrjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=NbvSKvRjnN_HwY-a8jtZWyDeSfKANY9kv1huz5KGbphcfVLwFPxE_3BT2cwqowx7Eb0D4vgY9Xk_ArsMpQ4TbFMKvqviI5VaeaGOC0LNd80fi2Gl8AP_0cy_HpPuC5I-drxN1XKYHIBjbNAMBLxhLavwa22snLqaC_GnBZFRpVoMcxsKFP4kl9yKvJ-y-Ye98Nb0o3zA0iZtzkgm6LvKkSHZdoN0ats_RO4IYcgjtXq40UwTNWhLlttsl9ZCgohtUWnZkSNN_JoFmNnTy2wM3vhp1e2BT5Gq4q8w-IxvOku8Jl_rnj_0qdRn0R_2_gJWn06rUMOcZXUmMehfzJrjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
فردا به دعوت پرزیدنت ترامپ به واشنگتن سفر خواهم کرد تا با او ملاقات کنم.
پس از آن، در مراسمی به افتخار یکی از دوستان بزرگ اسرائیل، سناتور لیندسی گراهام، شرکت خواهم کرد. باید بگویم که او از زمان تأسیس اسرائیل یکی از بزرگترین دوستان اسرائیل بوده است و شایسته است که این افتخار را به او بدهیم.
من با رئیس جمهور ترامپ ملاقات خواهم کرد تا در مورد تمام مسائلی که در حال حاضر در دستور کار است، از جمله وضعیت ایران، گفتگو کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69011" target="_blank">📅 14:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69008">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LHRd6ziU10MYZnjCkxjDvNuFiNRsOj-aOyCzAUrNjbvjUMQhaZZ84WLOxJHPEo7Uzx57X4NuPAyMhpycLadJLe16etp81qA49RuoCtMFXsZ2EQ0sjb_hAOyC3aOPpJprHuUPYIyw0XA8bnc-ZmEz4UdExTHcejfp_5wl-oU9F8yHBTS7Cv9_a78m8Xdn0tgzEOqI8iXLm2QUkJQFX-iPPakMEa3osK6eLUGzyo_sio5s7VuRzfPu9vQLHY-VMmclYr9Bgd-nH-OgVOTLkwZ_0conZDDkAC2ukaakWa7labGcCnqIiMiCwbSF1h4eTsQA9E_f8jTV-XFTZMsPicRGbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VhM_LCqynRbZ266g7KnyCRJf15p8chELdYMfkhw7O-NrCFhIvTZnrZXaOmB8yCxUT-651pPxhDlBomOxB6vDR3MZZ3g-NciJK1f5yd40ZEuzige_0lmBbWmC7d1jFGbEG8x6_Xq5zT7yPmdhHXJ4mcS9H0x7cjnACicR-64aIgyxfg6LQ9g3QQtKszryCl5vO2-p5rh_Xf2EDXVJRd8ljP4P822trlz6lzQM6a-GPlf-3rU4DWTWgBIsnCeyXbYlWnoNNGTnOtN7WyV8vqMiZZA5fC6gOH4ZAxn4xm8FLGanscRTWdEVpvkdol6OxdmcQeFlL0QJhxBjYmbD8yXJvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=ZdIxXiJCFaL4XZS92FtVJC5xM9j3FGyFbqKW2qNBMvoxCMl5AkclwiJzavpF6272f3nhgGpaZz-QBmOITzARcSrqQgtqssgd311r6rP5QRV8KAe2OfenqaeXQ4XtSun0Xi8poVMAc1700s7thEkHqAYK09ygf1nnhEj0I4n22Yi3U3IkhC3fztFguURofM_MEZf4-Fn2Y1huMlRs3RnANsEZBmAcV1oES679xrAqb5_iMbvD5BBXn9TpMQdw7a5j5oujQJOxYR4bej7Tu13oA9vmmhufe3Ro6ScsaFq_v6N3BVcM10VtG3UWxHSNWwK3nTggJktV8ynK1sKjUpaEOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=ZdIxXiJCFaL4XZS92FtVJC5xM9j3FGyFbqKW2qNBMvoxCMl5AkclwiJzavpF6272f3nhgGpaZz-QBmOITzARcSrqQgtqssgd311r6rP5QRV8KAe2OfenqaeXQ4XtSun0Xi8poVMAc1700s7thEkHqAYK09ygf1nnhEj0I4n22Yi3U3IkhC3fztFguURofM_MEZf4-Fn2Y1huMlRs3RnANsEZBmAcV1oES679xrAqb5_iMbvD5BBXn9TpMQdw7a5j5oujQJOxYR4bej7Tu13oA9vmmhufe3Ro6ScsaFq_v6N3BVcM10VtG3UWxHSNWwK3nTggJktV8ynK1sKjUpaEOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۴ ام مرداد، سالروز درگذشت رضا شاه بزرگ؛ بنیانگذار سلسله پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69008" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇷
محبی سخنگوی سپاه یه لیست از خسارت های آمریکا گفته:
⏺
در حوزه راداری و پدافندی:
۷ مرکز فرماندهی و کنترل
۳ سامانه ارتباط ماهواره‌ای
۶ رادار پدافندی پاتریوت (سامانه‌های پاتریوت به قدری ضعیف شده است که موشکها و پهپادهای ایران بدون رهگیری به هدف می‌خورند)
۳ رادار کنترل و مانیتورینگ هوایی و دریایی
۸ سامانه راداری کشف و اخطار اولیه
۷ رادار دفاع موشکی هوایی
۳ سامانه راداری EPS
۲ رادار EPS 117
۵ رادار برد بلند
۲ رادار پدافندی
۱ مجوعه راداری تاکتیکی
⏺
در حوزه پشتیبانی و لجستیک به منظور کاهش توان عملیاتی:
۶ مرکز تعمیر و نگهداری جنگنده و بالگرد
۳ مرکز پشتیانی و لجستیک
۱۲ مخزن سوخت
۱۷ انبار پشتیبانی تسلیحاتی و قطعات شناورها و هواگردها
۶ زاغه موشکی
⏺
در حوزه زیرساختهای عملیاتی:
۶ آشیانه پهپاد ام کیو ۹
یک سوله آماده سازی جنگنده اف ۱۵
یک سوله پهپادی که ۸ پهپاد آکبند در آن بود
۲ مرکز فرماندهی
یک سکوی سوخت‌گیری ناو هواپیمابر
یک آشیانه هواپیمای پی ۸
۴ سکوی موشکی هایمارس
۵ آشیانه جنگنده
۴ مجتمع پدافند پاتریوت
۶ سکوی پرتاب موشکی
یک ایستگاه پمپاژ سوخت
۲ مرکز مخابرات سیگنالی
یک مرکز داده‌های اطلاعاتی
یک مرکز هوش مصنوعی، پایگاه مرکز پردازش داده مربوط به شرکت آمازون
یک مرکز دپوی شمپاد (شناور مدیریت‌پذیر از دور)
یک اسکله سوخت
۴ شلتر جنگنده
۶ رمپ پرواز و توقف
⏺
در حوزه عملیات هوایی:
۱۱ هواپیمای جنگنده و بالگرد (روی زمین)
۱۷ پهپاد شناساییی و عملیاتی (۸ تا آکبند بودند)
یک هواپیمای جنگنده اف ۱۵ داخل شلتر
یک هواپیمای پی ۸
یک هواپیمای ترابری سی ۱۷
۸ هواپیمای سوخت رسان
۴ بالگرد سنگین
۶ موشک ذخیره
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=nLicy3rafCJLsc3AxY-i47xiglqh5HAJKphrTAD1wZMMpOLba0HWtW2357NB0ELBFhal1YeTatQ3vk-THhJzsKN46jhxjgvseEE2DAEaWuyO6U6KMXCXwFD5HtDpPwfqpO9yY1niNwIAD82z2ZiG6RS2Suu4oPUD066stiUDqvzuQCf98FuWUpCRR1ZDBhfyfJnjCN02as6FOQtXudSbV5ABQ8WeXMYUnm_l0LurkLothAqh0f1_HbMLmd797tfRisDN2fzOVW9u9FzcXF4u4e7zvBTiuWl_dDSghQpusTY8C5VI1ltJkhWxPFgrB_z4gg-lD-JNMdNVf8HMmQOBjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=nLicy3rafCJLsc3AxY-i47xiglqh5HAJKphrTAD1wZMMpOLba0HWtW2357NB0ELBFhal1YeTatQ3vk-THhJzsKN46jhxjgvseEE2DAEaWuyO6U6KMXCXwFD5HtDpPwfqpO9yY1niNwIAD82z2ZiG6RS2Suu4oPUD066stiUDqvzuQCf98FuWUpCRR1ZDBhfyfJnjCN02as6FOQtXudSbV5ABQ8WeXMYUnm_l0LurkLothAqh0f1_HbMLmd797tfRisDN2fzOVW9u9FzcXF4u4e7zvBTiuWl_dDSghQpusTY8C5VI1ltJkhWxPFgrB_z4gg-lD-JNMdNVf8HMmQOBjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=W95ah6vXvS1e38BtdKTfRKVsrzhnUMEEzaAnJ2DdWH0QtETjQDtLz2truOJWa2BIiRV_EMWyY_uoWg9Cgekhl17XrVCdmLeovwyD5koiRTJtYCpaGiXopE2FyAmvoDGrTXby4qFd6wW1FRgMHwDFbsfFpbWw-SQCJEf68E0cUVUPX0TVRgHe2at-8vUz5KpzSibIuJjdOtrofibvSi4duAv4y1nprf0TDQC66lQcxZgiySLYFr7_AQlIhbqqFKuidbEYh_p8Lp8umU-nnVkzrb3ln_q8O9W0w0aT2q8jcezWq5c2R7u04gNYJb3-pHhHMi_cvVNfuQ5wTnaJuJJzpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=W95ah6vXvS1e38BtdKTfRKVsrzhnUMEEzaAnJ2DdWH0QtETjQDtLz2truOJWa2BIiRV_EMWyY_uoWg9Cgekhl17XrVCdmLeovwyD5koiRTJtYCpaGiXopE2FyAmvoDGrTXby4qFd6wW1FRgMHwDFbsfFpbWw-SQCJEf68E0cUVUPX0TVRgHe2at-8vUz5KpzSibIuJjdOtrofibvSi4duAv4y1nprf0TDQC66lQcxZgiySLYFr7_AQlIhbqqFKuidbEYh_p8Lp8umU-nnVkzrb3ln_q8O9W0w0aT2q8jcezWq5c2R7u04gNYJb3-pHhHMi_cvVNfuQ5wTnaJuJJzpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبل از مرگ خاطرات آدم میاد جلو چشماش
من موقع مُردن:
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuT63B1GKxsVNAKqRniCAOCIUaGABCPKioWq0veF0wpQxRwTHMm6yPBV0vdUTlHocifarYQ8ElQsUtVhu63bzxKlG-Z_7mfp5OgN5AaJ54_h4u7Cupl9rgFSjPAZxU6QtIbvb2mfwj_K6_9x7ZHcilwXNxuYBtTpvJk7gFPr5ACnYCP2drwcV-bDDfAIPEH7pdzpi5a_2GHx0NRlHcYJtVTJJ6gm7QejECQ6My_r1932nS6XVRD1g47NZH-n-SodnHdVZVy92kFiUtnGbm-BHW8VsX5aGGx3GdLnkB5aIoNtq4e4NRlpwcY32lGxZ3XcbMW7bLH0j9J8wN2RinIZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک پست:آمریکا طرحی را برای ربودن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران بررسی می‌کند.
نیروهای عملیات ویژه آمریکا در حال آماده‌باش هستند تا «پیچیده‌ترین عملیات تاریخ نظامی» را برای تصاحب اورانیوم غنی‌شده ایران از تأسیسات هسته‌ای به‌شدت مستحکم‌شده، به اجرا درآورند.
جوزف راجرز، معاون مرکز مطالعات استراتژیک و بین‌المللی، گفت: «گفتنش برایم ناخوشایند است، اما فکر می‌کنم محتمل‌ترین راه برای خلاص شدن از شر مواد هسته‌ای ایران — دست‌کم آنچه اکنون در اختیار دارند — یک عملیات نظامی است؛ زیرا مذاکرات پیشرفت سریعی ندارند.»
یک منبع آگاه از برنامه‌ریزی نظامی روز جمعه به واشنگتن پست گفت: این عملیات بسیار پیچیده شامل هزاران نیروی زمینی خواهد بود که به تأسیسات هسته‌ای ایران حمله می‌کنند - از تله‌های انفجاری عبور می‌کنند، از خدمه ساختمانی استفاده می‌کنند و یک نیروی دفاعی بزرگ را در اطراف این سایت‌ها حفظ می‌کنند.
به گفته آن فرد، از آنجا یک تیم کوچک از نیروهای عملیات ویژه، عملیات واقعیِ بازیابی را انجام می‌دادند؛ فرآیندی که «بسیار خطرناک» توصیف شده است.
این یک عملیات لجستیکی سنگین و دشوار در یک محیط رقابتی خواهد بود. ارتش ایران کاملاً نابود شده است، اما آنها هنوز از افرادی که از مادورو محافظت می‌کردند، پیشرفته‌تر هستند.
بر اساس گزارش رسانه مستقل و مطلع «های ساید» (The High Side)، این گروه از نیروهای عملیات ویژه می‌تواند شامل «اسکادران نقره‌ای» (Silver Squadron) از تیم ۶ یگان ویژه نیروی دریایی (SEAL Team 6)، گردان دوم تکاوران (Ranger Battalion) و گروهان ۲۱ مهمات ارتش باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt8n_TpB0cFjFBi2s1PaMRRl7PeUTtpqBFH-tTkq0ukwrlfIKpSJxcmGN8y-huDKaIl8z1c6C81fUyKW8TVDbL0wRwS2GvXHXXPojazRy2RjXhMUYgpwUuZqg0OlzsAHF4YLDAR-I5IbhwIP8rZfNty-kmGKl9aYX_vlFNLMEilg7YouudwY9vBCPnHHdGClvdeWc61AjJwwY5IO-y2QAsL0mDL5-1NDDcijEN4vxhcQgmeEGeWt89siWnFBvwgMRCHWPUfWRmUEdat0O24bLGL2pfRSIYHWhWlw3PwNKr7T6BvBRu3F3BcwDVOBYnZ3wVV85UeV0FIWuubvnIQmUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae9373361.mp4?token=pRKZ04vyMhnhri09akDm1LPWReurQFVrzBBwIOcV7MfLIsmlOkOMJXWIvmdCcJyH3RwX7u7OlNPY081RkqkruGP-sv8g4xNM37Jdh83kmrFJoQ8sRVt3mAnFDYLLfazwnRfc205MYHPn43-T_twUCcy68UHwT4GQlOuYDZ_sGyVweYx3EdRGsph_cGZ4ULZ1vcuntExI0noes-i0IvayLJKsaHNJGXX-dHmYt3uGRqv9mqIB-QnR0d1IcQVb_I6B6YJM-8Ouu60wk8MnoyElCvB8s-c5ekhGa9SH4dTg4TLNQihOGFxITReOCsebZRtDDBXovv2wJ0P_dTvk2QOtjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae9373361.mp4?token=pRKZ04vyMhnhri09akDm1LPWReurQFVrzBBwIOcV7MfLIsmlOkOMJXWIvmdCcJyH3RwX7u7OlNPY081RkqkruGP-sv8g4xNM37Jdh83kmrFJoQ8sRVt3mAnFDYLLfazwnRfc205MYHPn43-T_twUCcy68UHwT4GQlOuYDZ_sGyVweYx3EdRGsph_cGZ4ULZ1vcuntExI0noes-i0IvayLJKsaHNJGXX-dHmYt3uGRqv9mqIB-QnR0d1IcQVb_I6B6YJM-8Ouu60wk8MnoyElCvB8s-c5ekhGa9SH4dTg4TLNQihOGFxITReOCsebZRtDDBXovv2wJ0P_dTvk2QOtjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو خاورمیانه همه دارن هر شب در هم میذارن.
🇮🇷
واکنش عباس داوینچی:
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=VbAC8Km6g0iw-dtMVHakNoh0kZ31HqXXWtp60VQ1BztEoBUIq-h-Wf9gykRv13WBo6BSxex5mEkqpvhV72SS_P_RD1sZZ11SthOdgchxJMCvt8S0GkJZPsXCsqAQ7h7JuFCuMHZxD1ILsOtPrKFAgiQ7NJUqsH8_wqQtzh5ARyw7NjOW1lnUrdz70rY1AMyA63_ePTl_eQ0w07rcgQVRfSgcnOr02hB29PhTgPbsgopdXS8zDBAoi2uJSDZHdOdYFptuXHPnAh6vhcBm5Z6q4mEsEpf5zG5Z8zlhDu0uQEybVw4RFJQA4-PSz5IcoHljVzY8tUXf-ZZVbq3xPvuHGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=VbAC8Km6g0iw-dtMVHakNoh0kZ31HqXXWtp60VQ1BztEoBUIq-h-Wf9gykRv13WBo6BSxex5mEkqpvhV72SS_P_RD1sZZ11SthOdgchxJMCvt8S0GkJZPsXCsqAQ7h7JuFCuMHZxD1ILsOtPrKFAgiQ7NJUqsH8_wqQtzh5ARyw7NjOW1lnUrdz70rY1AMyA63_ePTl_eQ0w07rcgQVRfSgcnOr02hB29PhTgPbsgopdXS8zDBAoi2uJSDZHdOdYFptuXHPnAh6vhcBm5Z6q4mEsEpf5zG5Z8zlhDu0uQEybVw4RFJQA4-PSz5IcoHljVzY8tUXf-ZZVbq3xPvuHGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
محاصره دریایی ایران توسط ایالات متحده همچنان با تمام قوا در حال اجراست. تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی ایالات متحده (سنتکام) مسیر ۱۲ کشتی تجاری را که قصد عبور از این محاصره را داشتند تغییر داده، ۲ کشتی را که از دستورات پیروی نکردند از کار انداخته و برای اطمینان از رعایت کامل مقررات، وارد عرشه ۲ کشتی دیگر شده است.
پیش‌تر در روز جاری، نیروهای آمریکایی عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «چارمینار» (Charminar) با پرچم کومور در دریای عرب به انجام رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام در تاریخ ۲۴ ژوئیه، نفتکش «لاوین» (Lavine) با پرچم موزامبیک را در دریای عمان از کار انداختند؛ این اقدام پس از آن صورت گرفت که خدمه کشتی چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران حرکت نمی‌کند.
نیروهای آمریکایی همچنان بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_grE6OHQBPvQvezozuJenYYGsYRXjuQknrzZPEc9mW5gvXTELXK_aSk-YtmRDlCjPIsst2tPyrdAJbInR1JWlIB3UvcdiKT8wUGxsA09eBBV-XHRhZyehHMmjUDfYlqQEQJKG_KsdC9Qb8ufsn4KCdU2EuVTn_KdEq8pmmSoUqv8U4ujFPyKYku8IKjEii_lBaFJvgfJ0p9aAWSJUjY0vi9Z2rcvjaNYOYTGmpRh09VE2543mmK4fnwnoiesIjP4TR5rjWdQuc6mALXba7Kgcq2d8wV0HjNT_vdDNCy_J5bWpw_VqKYtZzHBWfi5foN-eOGT8fP3E2Dvj7DsUcJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=dZemuUSUHeLd_TDxsVHw5FtiPkwMKgsQ7d8KndpgmHDoNEc1hppSUdOAawigR_tig5Od9nMS7W7O8XyWIvtIJUf1vUN3kXLqiHaE4l4j8rAmrnu9BPqxp1gg-7ASdq1E_ksUmXkBgTVjsA8M20B0ujtEFEWjCt2HAa9mKbngR2V7cIvnFFXqE6dR45bAFUxGb2GhBM7l25wkuaOULDlC_HH-xV9rEKu4Ma4Bq8Z6q_e0mOydHjPWvPg8eowBNE3hAxa_8y1MI4rJWLW7FxaxEV_HbEa4DmrKDjZI7ZpcIbrEu3LG7BglcEQeWGItHT2jzdNUPbx9dg62IO5lhpldHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=dZemuUSUHeLd_TDxsVHw5FtiPkwMKgsQ7d8KndpgmHDoNEc1hppSUdOAawigR_tig5Od9nMS7W7O8XyWIvtIJUf1vUN3kXLqiHaE4l4j8rAmrnu9BPqxp1gg-7ASdq1E_ksUmXkBgTVjsA8M20B0ujtEFEWjCt2HAa9mKbngR2V7cIvnFFXqE6dR45bAFUxGb2GhBM7l25wkuaOULDlC_HH-xV9rEKu4Ma4Bq8Z6q_e0mOydHjPWvPg8eowBNE3hAxa_8y1MI4rJWLW7FxaxEV_HbEa4DmrKDjZI7ZpcIbrEu3LG7BglcEQeWGItHT2jzdNUPbx9dg62IO5lhpldHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیروزمند:
تا کی قراره ایشون ( مجتبی خامنه‌ای) بیرون نیاد؟
🎙
مجری:
تا نابودی کامل عوامل جنگ.
⏺
پیروزمند:
خب اینطوری شاید ده سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1C3-VgQcfcryqgOkebK_uQ365IIOulvJo-pLPGzmcngvq6gxp1Ex58Hfgta2j1xmSjLUHa_-E09v8344vGZhO2k5rDxbCwPLHG7lJ7aQqNZXYElPU-Lk0YA9GcJYyq8xMmN39iGmoEnE_tsIO1flK473XF3cPR-jqEERP3r7f2RaPP1-JejBJXklxqXGIa5eWLkMzzhJo9J9AE3xkElaN__iOA4Viec5x0uGRWfqGTP-JE8awT5hpXZ7pBrRUmpZdETrcqSmTZGuaJn13x6uWxiA-F_5SoeVuAp3SMnBSHp0lxNf4_LbSi39qte2zIazTLnqamE5MYVlB9VbEnb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJA-5wUYFhQ0ErrHe1NevRq7vQZdJweh7cLtIpI4AyKoEXPohUvWR5Qhs2jCfo4lwQB4BUr64E1c1sCrnFiOWDcN0h6v1YA0oCLrdYKmqwkdf0Qt2_IA_UrHBgxmQ0nt5bWsj0BVAm8PTEe8NwKM3m10i7jdf0qDmG7ss5DoJuZAyxHDXEQuRKVnQ5lYwfhoopiUQpG1NeXmctggJqfkgtL3_GyzpGfjj1WQuJ_42LKnRT8Tb6D5F-sv3g8TfIkxPyEMuO8xTBnmeKqZeapZYmGnxLl_F1gI6voNaeJMW92CSb-yKWS7nhVKTqEy9l3fVJqmZ75U2GlHZ2xkxR1ERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5v7W5kj0oqKG-bbrFxcJV7DJvEZj-gIIAHfGSHvC-GfGt8c8pC4-DyUA2hF9hduInLEWCTTPkthdQrVVAfhYh8h8E5doXs8pVo0_IwqvHbmdSxjr6VoaJ1NnBxkQqzPST-3obnV7VmWD58EOoRUwvG3taqjKCS9Dkh_2rPNpKmYQPAeliJQAsogFhtmNdfL6JYw3o09DqGKhZikj_9PxXcFh9BHEU8L1a_r536lQYefYABXfiv8rRXwFdiwMgc97TnDRO8p2iGXL6S1Poxp1Yn-VGQssYE71ojmLHmOQ28-bLYYAm14JFYT02ML8jSbfUC8lcM8-taGDzpCM3YQ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=HJK6uHUOUXnzVoZ8JyvJz9fcP4_8_fqgDlKY9JAJVCTKLzp09VaMMnVtLhScW8A0Tl0dgdTgjfW45nCyO2vYJ8Y5qByuk7u1IcFHMfdpsDG1ud0WPh7Rogn9H-yvv0Xyiq_stj25tR3GT-RR7GRmR_7XptandDAwxCj9hTQ4nCLpo7Qw5rYqQgE658qyvuAP2knVUKq0waQHkCyXirdlZNPe6ORFVKG5aNnvBaOqGxBzFQu4g03pZEpaUQ87k5RmhGAV3VEN8UGRGWMLbYcBZPgpxvGI0PBT3k1UO_02ATBL7P7J3Ge-FnMcboSoFJyRrO1Qh7Xwvg5A04nCjOoFkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=HJK6uHUOUXnzVoZ8JyvJz9fcP4_8_fqgDlKY9JAJVCTKLzp09VaMMnVtLhScW8A0Tl0dgdTgjfW45nCyO2vYJ8Y5qByuk7u1IcFHMfdpsDG1ud0WPh7Rogn9H-yvv0Xyiq_stj25tR3GT-RR7GRmR_7XptandDAwxCj9hTQ4nCLpo7Qw5rYqQgE658qyvuAP2knVUKq0waQHkCyXirdlZNPe6ORFVKG5aNnvBaOqGxBzFQu4g03pZEpaUQ87k5RmhGAV3VEN8UGRGWMLbYcBZPgpxvGI0PBT3k1UO_02ATBL7P7J3Ge-FnMcboSoFJyRrO1Qh7Xwvg5A04nCjOoFkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ساعاتی پیش یک هواپیمای آمریکایی در فرودگاه جده فرود آمده است. به نظر می‌رسد این هواپیما یک هواپیمای آواکس مدل E-3Sentryباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxc9Qym8xalQhVnW67xkm66pQ_zSItx_HIeCdoDE3kKoEsP3jxCDCCiMXqsw9GYh1cFri3q1jp3yzVdCZ-yX6xRxB4jcdutc2j89tNYSSwTZOwHeLvrT8cEZKsUoZAfmZQR1MV1NcJ2237HNkGOXQpazwO3HN09JxPP6L_uqWme2zfu8tVW2Qrenw1zzmTgkhdDKmhRlTmcccqbNaoqObcV-SplkpXravQlcsp2FMJuEFuwKjdIwb_Gaeim3jV6ixxLYQorhAM0rd93npLQmUZK3eSStKH8FzEBDpuDQHJJ7oc2jlDHzXO4nyZkASA0kGfjMmDt7MTOggXS12U40QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=nvRPXd6JsJ5DkgCndPFIPMhI-6wAvOVF2bYLhWm8fTQ3wV04NyQseqhwTaTrG0-jFGWaxa6EzFKzmUDtlYafQ-wpM6OgOYDLy8uAdIBttjXYNL7T1XW3Jsv2rosdgUZOYzjRUbLqsf_uchTIlDxs-cgRYXJ5u-7T58tFFDoFIm1V5iRkgC4y_7sz6Su9PBGh8UIekb1vNg2DzedFx6vhRstdXGPi_-dR3NRLqlMYrh04_0I2klgk5he25_X19DQS5LB9qujIK0rQ89nYnLy2cAf7QdaxR_ArU_GdUASbFd5_ifBxRp9p9lFGCOolVqpH0ctC2zyznwHjj4w807np5w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=nvRPXd6JsJ5DkgCndPFIPMhI-6wAvOVF2bYLhWm8fTQ3wV04NyQseqhwTaTrG0-jFGWaxa6EzFKzmUDtlYafQ-wpM6OgOYDLy8uAdIBttjXYNL7T1XW3Jsv2rosdgUZOYzjRUbLqsf_uchTIlDxs-cgRYXJ5u-7T58tFFDoFIm1V5iRkgC4y_7sz6Su9PBGh8UIekb1vNg2DzedFx6vhRstdXGPi_-dR3NRLqlMYrh04_0I2klgk5he25_X19DQS5LB9qujIK0rQ89nYnLy2cAf7QdaxR_ArU_GdUASbFd5_ifBxRp9p9lFGCOolVqpH0ctC2zyznwHjj4w807np5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=ppppKPTccOL62CZawbdi_fa7NLwRoTnpH1MwCMZ-4bKnef6O9N83B4hnwATg5KbyBYun6LrOpn5P77Hwps9GytlgX1LLZCNFjexA4v8Bd_dcY3YbDoEkdb9YTPr_9_9ZnJyXMXrIfGGVgcrnHj4E89iWpoq8xw8dc_xpEwbKzspWVeDDK2bM-tgvAQwQGyX1cEtUaPSP7tGz1hTHqdmlTU7ghbhJXaI7xQdsOVMlHSUiNp9XaTdWmptrY_rGgYSwoYMdi-2d_cAtnBCO6n64j_-gyuKECA4AhcCv5hWmXgb2MQcDGTi4ctS6j79AOnsb0R8HgRAl5jp-rh2NAsbSKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=ppppKPTccOL62CZawbdi_fa7NLwRoTnpH1MwCMZ-4bKnef6O9N83B4hnwATg5KbyBYun6LrOpn5P77Hwps9GytlgX1LLZCNFjexA4v8Bd_dcY3YbDoEkdb9YTPr_9_9ZnJyXMXrIfGGVgcrnHj4E89iWpoq8xw8dc_xpEwbKzspWVeDDK2bM-tgvAQwQGyX1cEtUaPSP7tGz1hTHqdmlTU7ghbhJXaI7xQdsOVMlHSUiNp9XaTdWmptrY_rGgYSwoYMdi-2d_cAtnBCO6n64j_-gyuKECA4AhcCv5hWmXgb2MQcDGTi4ctS6j79AOnsb0R8HgRAl5jp-rh2NAsbSKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9esvzNIcONC4nDcq0aFOW64uckWHK0D0RGGrp6XFurg7jSMAxzKQaU9h8tYv_o-uvDrez9OHZRi3gvVDzljrhXH0OGfeZ5qdt7D0WT6cVoaiPH4aphSUDI_dBFrLjfJBUdP481ABIw3qN8IrogosYTAimRWGDU6bSQrCw9rtbr7zBNx50IFYgvbBOth6y8oUhpk2Yn75UP5qOgVVxub_ThhRGEhOD5SIV4jMfGLtukxI-IWPSovwwkGbO_YMXj-JaKS1aKMc10lIm6lT6rZl2eV_vY0qKza4YSNqkeQiapqTgM2P1y2Yn06Np6Gb8NsFZMgA3mN4FWKgZ_Q6oPKrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=cQP33a7K7uZust4n-j0WXRAs3XN_PBAkCgCkYwrzwEyy6fReKCi5uk52h4SNh0lC7NLPMAPpey34WYKluVK1NpVHy8zU80NaKjhVa-2nvQ2l4NpSQmQEAisUgZGlqjk_zC7TWFA5rxW2D9TjnJdhK05j0RDdfBHxjXt0ZwpR7QuaI1TUBiPaRTTuI4GnQwTuADlAL-UIdX-bJJaP2pheQI5IwrIHklQd_5yx4uy-LU-AK2azpvJLtddqfZddObl2ZDAv8sFYCwIfgJLTbeS-lFmS-3LEfdGkKQFlufK77ulA6QmHV6O-YkNzfurNGzE3sN6a8CBIui9RGi1LYjIXKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=cQP33a7K7uZust4n-j0WXRAs3XN_PBAkCgCkYwrzwEyy6fReKCi5uk52h4SNh0lC7NLPMAPpey34WYKluVK1NpVHy8zU80NaKjhVa-2nvQ2l4NpSQmQEAisUgZGlqjk_zC7TWFA5rxW2D9TjnJdhK05j0RDdfBHxjXt0ZwpR7QuaI1TUBiPaRTTuI4GnQwTuADlAL-UIdX-bJJaP2pheQI5IwrIHklQd_5yx4uy-LU-AK2azpvJLtddqfZddObl2ZDAv8sFYCwIfgJLTbeS-lFmS-3LEfdGkKQFlufK77ulA6QmHV6O-YkNzfurNGzE3sN6a8CBIui9RGi1LYjIXKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=acM96Z_E74w0qKpUzkwm6sW9o0Mw-XdH-TorcDQG86V7zqt_rVAUC33Nbjt9qDEBCenaz7CNbvypw6NeIAIjHaaRk3I-_WoutiSo6DIl266BBiGhSX_Pg7TYjFwtLE1NE9Q3VEg26SCNLh6SoFi7nEenADB1KbSxqwd3BXE-WsQzPqHUEH9F2d4tgdWxToHJgYzxIwk8Yp4AhJvVIrbtn-XTVXSZQsFvWRnj7txTvtqtu7jNK1ioumkz0cjIFOuGQ4gJIOu3JW4pq5k_rAin7JZ8ulkZIX_8JT-kSWMuGAKmAAqgljqMuID0gM1Dobr8Qf1JHL-RmOTFEtLa_B7CTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=acM96Z_E74w0qKpUzkwm6sW9o0Mw-XdH-TorcDQG86V7zqt_rVAUC33Nbjt9qDEBCenaz7CNbvypw6NeIAIjHaaRk3I-_WoutiSo6DIl266BBiGhSX_Pg7TYjFwtLE1NE9Q3VEg26SCNLh6SoFi7nEenADB1KbSxqwd3BXE-WsQzPqHUEH9F2d4tgdWxToHJgYzxIwk8Yp4AhJvVIrbtn-XTVXSZQsFvWRnj7txTvtqtu7jNK1ioumkz0cjIFOuGQ4gJIOu3JW4pq5k_rAin7JZ8ulkZIX_8JT-kSWMuGAKmAAqgljqMuID0gM1Dobr8Qf1JHL-RmOTFEtLa_B7CTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از طرفداران حکومت، با انتشار این کلیپ آمادگی خودشو جهت
مبارزه زمینی
با آمریکایی‌ها به رخ کشید
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=vFm66_OVeP9O_AiXpNxCNhVzY4vQrRlcABBOlzKpxNHKyHlN_zLk9ngB35PWCZ91RsAKjKpeOOo1OQW9LeR-GH5zQTioIVPJ9njX-lfWNNdAA8q-AS_-QukUEH3cBClPUvfkZT_KSZmbESn3QXQGSFyBlL0XXGRvNvWRrNfA6R2z6Mv2xE9BE0ViYr-Jro4MY57lGA4JDCMx9NmnTn09wV27xU9QqXKCZ_PhNSQ4XOPJPzWMoC3aj0W_Gi94Rwyu8ifS4kmG7BpXAY9MRgHWveKG6_e5GsC81I8AWDWVXw_Hmou9pJ3ke6pkxxgL3H6rgyBt-4R_l3ku-__575q_2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=vFm66_OVeP9O_AiXpNxCNhVzY4vQrRlcABBOlzKpxNHKyHlN_zLk9ngB35PWCZ91RsAKjKpeOOo1OQW9LeR-GH5zQTioIVPJ9njX-lfWNNdAA8q-AS_-QukUEH3cBClPUvfkZT_KSZmbESn3QXQGSFyBlL0XXGRvNvWRrNfA6R2z6Mv2xE9BE0ViYr-Jro4MY57lGA4JDCMx9NmnTn09wV27xU9QqXKCZ_PhNSQ4XOPJPzWMoC3aj0W_Gi94Rwyu8ifS4kmG7BpXAY9MRgHWveKG6_e5GsC81I8AWDWVXw_Hmou9pJ3ke6pkxxgL3H6rgyBt-4R_l3ku-__575q_2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای دیروز پزشکیان که تا به بحث مذاکرات رسید صداوسیما سانسورش کرد:
بعد از جنگ 12 روزه، علی خامنه‌ای رسما اعلام کرد که ما دیگه با آمریکا گفتگو نمیکنیم و صداسیما هم اعلام کرد.
یه روز رفتم پیش علی خامنه‌ای و گفتم خودتون گفتید نه جنگ - نه صلح، حالا ما چکار کنیم؟ گفتش که برید مذاکره کنید و ما به دستور علی خامنه‌ای گفتگو با آمریکا رو شروع کردیم.
تو آخرین پیامش هم گفتش که برید مشکل رو حل کنید چون تو حالتِ نه جنگ - نه صلح نمیشه کاری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fPtRxmVGHL1u8IzZ1ioir-G8hCDmXEM7WeWnvne06qRV60u20klIqhi9bJkhPPHCehreZpC0oPvzJ4-7pbXWhn54gwrLjFrpG2NzE10YeMJU_37ZfuWRLJBGvjLfYWg4wizEdpuFZJ_yHTTV5Ul48UUCJEXw1L-IlsweEZQfzP4VD85dHg0hub5ckw1O7tWv611MEz-67ZBFYThBDzqENLQclW2RbR9yyiZGJJdAS_eUUlB5IME1cowQMMGR7KDST1yM-VNRTdLh8fMmx21MPH5aBJUUObaPeWtOiUbZMALDBYK8-_cshZprHjWG1PBbgDxyiM7YgOH_stKA0s3SIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fPtRxmVGHL1u8IzZ1ioir-G8hCDmXEM7WeWnvne06qRV60u20klIqhi9bJkhPPHCehreZpC0oPvzJ4-7pbXWhn54gwrLjFrpG2NzE10YeMJU_37ZfuWRLJBGvjLfYWg4wizEdpuFZJ_yHTTV5Ul48UUCJEXw1L-IlsweEZQfzP4VD85dHg0hub5ckw1O7tWv611MEz-67ZBFYThBDzqENLQclW2RbR9yyiZGJJdAS_eUUlB5IME1cowQMMGR7KDST1yM-VNRTdLh8fMmx21MPH5aBJUUObaPeWtOiUbZMALDBYK8-_cshZprHjWG1PBbgDxyiM7YgOH_stKA0s3SIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=dPjNpC3M51PUP8fuWL3nOCgI9wn0_07oazf6uHJqu11bNQ4ceTZMJS_a_mG0HxV1-8XPwpl41DrhPgi7PivH9HBgP0XNnwCJKWNzDCIdo9GV96JyXSubMWBNm1tzVVWKBiyDHOTe6_Dr8SPpQxUmC_fbjMYxs6swtmu_flui7tOBfxlOXvANfkD8_7doo4_-lS9E5FATL36UjPPwapGBVyZ_3jqPo_AvtSnSwxQ5JPSHKiSuH7sMbHhdFc86V03UxO4X75RdFjCVoZjVnX7TRuZUzXXtUmWtfY0dQr8zTd1TfzhSvIQGWi2q42-HoZN5gTJEwp2XJukK4AvhsAkyGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=dPjNpC3M51PUP8fuWL3nOCgI9wn0_07oazf6uHJqu11bNQ4ceTZMJS_a_mG0HxV1-8XPwpl41DrhPgi7PivH9HBgP0XNnwCJKWNzDCIdo9GV96JyXSubMWBNm1tzVVWKBiyDHOTe6_Dr8SPpQxUmC_fbjMYxs6swtmu_flui7tOBfxlOXvANfkD8_7doo4_-lS9E5FATL36UjPPwapGBVyZ_3jqPo_AvtSnSwxQ5JPSHKiSuH7sMbHhdFc86V03UxO4X75RdFjCVoZjVnX7TRuZUzXXtUmWtfY0dQr8zTd1TfzhSvIQGWi2q42-HoZN5gTJEwp2XJukK4AvhsAkyGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfOGSDb7VJLrDkxd8_lrhLJXDt4UESlrU9tXnapXFpneVD9JvDsd11TMDwMsxJYLPIDxr7gLUDX9tulVbWWoPPodxrCD79tZmBF0AiumeWoN0IBHUazz-YUumSqwMfDYjTq9l6xaegC_PwjTrzsM9M0YLD930e31YntRad9crQuY6NFru59PhiQf_hkiFtbU-pB4cOCIzpmzZiHefj_QdnHE7egvyXB1FaFHrbsQVGsUxqTeIAzKXP1PF542oFbNX0R3SxZ49PcSrYOuH4psRn7LJyAl-wgPMIAu2KG7vNLj5GnPD7yJIQK-fjLgzxwVV7kMs9HFKePe-bp_wwqJRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=A3QnCY3xh6Y6RJwRb2cf7LqartYX-8WCAioTIhJ7O_coS5znrERAjaFNiOjRMRINDZnvEdalH8GfXCymvJKsPcFH3_bG-q0bhDXmcXoxs6YsR2Lcz-oI9nJ_Fr-sibjFXvWeOQO5uYObEnRdZsGdVfZCccKMo5DXO-CAcoJXJbkZ5V9AreORkQ_o-ffFX3GH7qv9jk1oiFm0W1NQdqofiZL-R_OEbkp9ILqRwHZ1IW5sVsegqqAoK8K_mK15vO9fhLf0Gm9KZqrRhQZDnVxkQpfA8VpG1ppaA30NJ0hstwZ3biEfVyQAlRd84pzFSjWkSl8Q1QaEp1bEEE1Nvhwx-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=A3QnCY3xh6Y6RJwRb2cf7LqartYX-8WCAioTIhJ7O_coS5znrERAjaFNiOjRMRINDZnvEdalH8GfXCymvJKsPcFH3_bG-q0bhDXmcXoxs6YsR2Lcz-oI9nJ_Fr-sibjFXvWeOQO5uYObEnRdZsGdVfZCccKMo5DXO-CAcoJXJbkZ5V9AreORkQ_o-ffFX3GH7qv9jk1oiFm0W1NQdqofiZL-R_OEbkp9ILqRwHZ1IW5sVsegqqAoK8K_mK15vO9fhLf0Gm9KZqrRhQZDnVxkQpfA8VpG1ppaA30NJ0hstwZ3biEfVyQAlRd84pzFSjWkSl8Q1QaEp1bEEE1Nvhwx-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حمله موشکی حوثی های یمن به پالایشگاه جازان شرکت آرامکو
عربستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqB_Lc4YquB2yLpVwsPt9wO9eku_EKrc86ngfvZXQMcrqWuauo73r103wQN-zYJ7ySlDm_cqdgJl7yVh46UAw3v7UCrj1dtZwPp9zriftxg5DFLow2SkgNPSpxDl2XW7siVsn0rk_GsBsTGYMwwqCdQLFr208H_lo-7yLXw5wlMrmh6VPpS_qQxODfF1l_JEdpFaMqFiJue6isaj1qzFpojWb9Sdu5BRraCgu_sW7hMTLjAwkLh4K9WT2djAQSAfbq8HTiaEKvVxCc_TE3YHCbRuI2DBWnE5jr_urqY-nD6Cx088vv9M3vl8GXzGdeHCAEosTqVHMAhDlVWrnb_FIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=B6V_S9fYDjOMZbiv4xXWgFA6GfeIJzQefY3WYcmlVX8JKul6Fk85LO_RkQyemQ3vEahkrQzhNyv_BULb9ZYqPV1G0-dIhm4wUKfbSFGfRsWNM7y25w-_uzzUC7MlNfHoUF4hJ_URtFB8g7shujyf8hmA-sCF602BBU2KJqzTe7d7hcWhSYX3FF8pfL1QNeJjjWkOY0XRqZos0fiI4JUFqc7OaYn5JL0fg_90LXggpsyPgpOhqehGvP0qXplUkOtz0PNrHo3gecD87BUKEErNSIklvrBlYFkvSvcfwZKdTgvbo1lX9KO0YZHWyHlm530eqYPtydYZ5fD-EXvnd2fFlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=B6V_S9fYDjOMZbiv4xXWgFA6GfeIJzQefY3WYcmlVX8JKul6Fk85LO_RkQyemQ3vEahkrQzhNyv_BULb9ZYqPV1G0-dIhm4wUKfbSFGfRsWNM7y25w-_uzzUC7MlNfHoUF4hJ_URtFB8g7shujyf8hmA-sCF602BBU2KJqzTe7d7hcWhSYX3FF8pfL1QNeJjjWkOY0XRqZos0fiI4JUFqc7OaYn5JL0fg_90LXggpsyPgpOhqehGvP0qXplUkOtz0PNrHo3gecD87BUKEErNSIklvrBlYFkvSvcfwZKdTgvbo1lX9KO0YZHWyHlm530eqYPtydYZ5fD-EXvnd2fFlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=hHrgual3I02ha-wR8qJpBxAjdOC0IAIuxj1sFLHMkIK3tEgKRRsEkmgC6d62ABo8FsHmDdPhWNKdhurrg6IvuID4xZ0EBYcE6HYLvim_jWZAFu9TyKWR1uXhoZFnYR44_RtXio23bD7e4-tWw5ODQ_71B9g4_UKtgZ1xs203P5QbhdxjyHM_e4Jx24luVxq26L9gwWBKOan7gDVl97x53wjTv-w6sTdyy3ORzlF_F2FcZ3lK_MUjKUy7qv1E2RK4PoP-rLinzkNOTv-xm6f2uniJ1j2T3Xe7aF1eQQS-E-WraVi8jQRcb6Fm8om0OfGaQUYl_g7pnS5ajehcKslYQIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=hHrgual3I02ha-wR8qJpBxAjdOC0IAIuxj1sFLHMkIK3tEgKRRsEkmgC6d62ABo8FsHmDdPhWNKdhurrg6IvuID4xZ0EBYcE6HYLvim_jWZAFu9TyKWR1uXhoZFnYR44_RtXio23bD7e4-tWw5ODQ_71B9g4_UKtgZ1xs203P5QbhdxjyHM_e4Jx24luVxq26L9gwWBKOan7gDVl97x53wjTv-w6sTdyy3ORzlF_F2FcZ3lK_MUjKUy7qv1E2RK4PoP-rLinzkNOTv-xm6f2uniJ1j2T3Xe7aF1eQQS-E-WraVi8jQRcb6Fm8om0OfGaQUYl_g7pnS5ajehcKslYQIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از یک تحلیلگر سیاسی که زمان پهلوی هم بوده:
یه نفر نشسته بود تو کاباره داشت ویسکی میخورد.
طرف کی بود ؟ قصاب بود !
به بغل دستیش میگه ما ک اینجا نشستیم داریم ویسکی میخوریم بعد تو ببین اون بالاسری های فلان فلان شده چه کیفی میکنن و چه بساطی دارن پس.
اینطوری ناراضی بودن مردم از پهلوی!
مردم رو اینطوری ناراضی کرده بودن روشنفکرا.
بهشون گفته بودن میدونید شما خیلی بالاتر از اینها هستید.
انقلاب رو روستایی ها نکردن انقلاب رو روشنفکرا و دانشگاهی ها کردن بعد اولین ضربه رو هم خودشون خوردن.
به مردم گفتن عاای شما وضع اقتصادیتون خیلی بهتر از اینا باید باشه ببینید اون سرمایه دارها چیا دارن که این همه خورد خوراک به شما رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=nuvFSepfxcErTapmeNSZ3O8D6Ts8Yx-eMCyEYVJc6dc9Fp337S6VqT70k2SqYmTbBuNxLRn39Y6Xdjg3f7yb5R4pmLcQ197Xpz_Q-ognUUqYyrJwbC_pYAxFeYvwpp_AVudCGDxJg4DpjzO_uqUJ25i2VC-hcG4qvXNJHeF-45I5vPB-Zpqika9frkWDIkcrcV_mZQML3zFImb8mTqnRbpKt0pn-KMG0X4bi6fFo5i0bLIg1bhZzqNtO12ngdTEg3IF2onyHQnyT4Jy2CF4XTqKiWt61Dg285KvlZVKpr03ZGfaDpraDt6K_fGoOjhX3ev3z-x6lfpcrYPn6sf1I7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=nuvFSepfxcErTapmeNSZ3O8D6Ts8Yx-eMCyEYVJc6dc9Fp337S6VqT70k2SqYmTbBuNxLRn39Y6Xdjg3f7yb5R4pmLcQ197Xpz_Q-ognUUqYyrJwbC_pYAxFeYvwpp_AVudCGDxJg4DpjzO_uqUJ25i2VC-hcG4qvXNJHeF-45I5vPB-Zpqika9frkWDIkcrcV_mZQML3zFImb8mTqnRbpKt0pn-KMG0X4bi6fFo5i0bLIg1bhZzqNtO12ngdTEg3IF2onyHQnyT4Jy2CF4XTqKiWt61Dg285KvlZVKpr03ZGfaDpraDt6K_fGoOjhX3ev3z-x6lfpcrYPn6sf1I7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره رهبری ایران:
«حالا که همه اهالی رسانه اینجا یک‌جا جمع هستند، باید بگویم که ما به دستاوردهای فوق‌العاده‌ای رسیده‌ایم که رسانه‌ها هرگز درباره‌شان حرفی نمی‌زنند؛
برای مثال، در دوران دولت من، رژیمی که زمانی قدرتمند و هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شد
رهبران پیشین آن کنار زده شدند
و اکنون توسط یک دیکتاتور گی(همجنسگرا)اداره می‌شود که با اختلافات داخلی دست‌به‌گریبان است.
با این حال، من شخصاً برای باری وایس در شبکه CBS آرزوی موفقیت دارم. او زن فوق‌العاده‌ای است.»
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=n0EDAZXhj9UdfeOdACpMCgaGMXzWcFFdul0qw8UfLf52A3xhXbk9BcwE8roFYznb6dT24lTyo3AvSF8lh7ihpSf4R26K5juIlnCb4aCdfsA3bCWFB50HgvGMggoQHPtyHGwpVDMzClwoZVayKvf2BLnzbr04RBGVDCi5G77dY_fQ10-l4qGcVe3drb7oRPcW8CfPF3_Fy1F9F_2_sNG6TASSn5dfqA1kXDJxpsiTfPiIjHmQ8QO35_pyHVwrCuUN26HDA2OVeyx2PdNbIPsdUX2Un07Ael8QcUemll1VN_kUGLA_yUkQOz18mWFYa01iW4MFhs_oR4pBcCiquvTWi7UYt79QDY-fJfzqGsyvDTToUYndOTbbQz6Setui1O04pmXFJhKdbcOjO3Hj46dTvOb53vpMrzaLAZJWN40toIji3Z0qVkJbOhEVRxzi-05RolyDPODusFZr7w_1MOUOe-4YH2VRUdvP660Ic2XnLxdDJOTVwg3R5JmwVrhq-kmUol4ts-FcTaxqh8qGcJwLltX8WCPyQq1H_HHk8ylAAotAptoXW2UoxRQ0IoyX9XCm5dIx2HCqTA5QaVFHodyfhLCU0L51fHhyMnO2d3-7pMJt_wEei5EwoRUPsSSJSyD8YXuPv6zH9K3pGRw6zt8r-vw3JiqMRh9SuodRDhKC64M" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=n0EDAZXhj9UdfeOdACpMCgaGMXzWcFFdul0qw8UfLf52A3xhXbk9BcwE8roFYznb6dT24lTyo3AvSF8lh7ihpSf4R26K5juIlnCb4aCdfsA3bCWFB50HgvGMggoQHPtyHGwpVDMzClwoZVayKvf2BLnzbr04RBGVDCi5G77dY_fQ10-l4qGcVe3drb7oRPcW8CfPF3_Fy1F9F_2_sNG6TASSn5dfqA1kXDJxpsiTfPiIjHmQ8QO35_pyHVwrCuUN26HDA2OVeyx2PdNbIPsdUX2Un07Ael8QcUemll1VN_kUGLA_yUkQOz18mWFYa01iW4MFhs_oR4pBcCiquvTWi7UYt79QDY-fJfzqGsyvDTToUYndOTbbQz6Setui1O04pmXFJhKdbcOjO3Hj46dTvOb53vpMrzaLAZJWN40toIji3Z0qVkJbOhEVRxzi-05RolyDPODusFZr7w_1MOUOe-4YH2VRUdvP660Ic2XnLxdDJOTVwg3R5JmwVrhq-kmUol4ts-FcTaxqh8qGcJwLltX8WCPyQq1H_HHk8ylAAotAptoXW2UoxRQ0IoyX9XCm5dIx2HCqTA5QaVFHodyfhLCU0L51fHhyMnO2d3-7pMJt_wEei5EwoRUPsSSJSyD8YXuPv6zH9K3pGRw6zt8r-vw3JiqMRh9SuodRDhKC64M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzA5sHBWT2s0fEVI7C-ynJ-rcr7nF_9Uy38PWY02SZ4nPYxnQh5n-WgJVfK-bvyUcJ4QyQkZ632BfPqATQ0ePJyv3H1uMxLEeC6c_HkokVyCMK60H3NWA_uVAsa7HBzeIW18MWRd9x97N6DZYbt-79uVi_oX0eY-qjHoi46zPt1GI-FsukE0mZLBRS-WxkzQS2-32OQ6kqM-XOSNVT6MTHfGU2Pcv5YMKK2JlZe1mXUt1O8c34CO061g739E8SVJVeEobtczbGztfldWrMeAkCUaJtS4wAMZ_NVea1SauwoN0bs9tbrhyHYEbiaUCZEKrbMrPE6A4eqW-RB8GhYg4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=aJm2RKvtHNN_EKDCyUDpbUI1bgGs-omA63xX3cq1I3YeH2sOHdDCtnwIOX_RDWCjB-JA3FGWr3TxyrTzjXBSMvTKlAIWhHaeL3_wd0e2QN1Px-bYhZ4P93gr542z13xliytMpAPJTp0YzkR1a6fl-4hKqCuB1_Ck1QdFl2CjyFU0oTd72CB07FAq0SJgwpomdagUU_FhyvRscnPFtyu0-Dwcb3ZxPcqn8cWJQRodbwMKbowhtpw8xujyOHrzcQURRxcp1swdzGCAJ-wSre8-dwFIa6IFuSjKceeqaSA1jTxntkte9NJ39vCYj65WiZNALVYKNNMcpOBgFBURw8cK2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=aJm2RKvtHNN_EKDCyUDpbUI1bgGs-omA63xX3cq1I3YeH2sOHdDCtnwIOX_RDWCjB-JA3FGWr3TxyrTzjXBSMvTKlAIWhHaeL3_wd0e2QN1Px-bYhZ4P93gr542z13xliytMpAPJTp0YzkR1a6fl-4hKqCuB1_Ck1QdFl2CjyFU0oTd72CB07FAq0SJgwpomdagUU_FhyvRscnPFtyu0-Dwcb3ZxPcqn8cWJQRodbwMKbowhtpw8xujyOHrzcQURRxcp1swdzGCAJ-wSre8-dwFIa6IFuSjKceeqaSA1jTxntkte9NJ39vCYj65WiZNALVYKNNMcpOBgFBURw8cK2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA0ZdAg4mT3i6xKuUpcEwvbQa0vaC7lXCptkGd4S5KknE_viZ1rkJqdtsoY4b8Ifh1ou4GGuHM5YxkgIOUb3xHN2_WRSMd2MWYjr-qpIARGd1mPQufBktLpJmBEZZI92wksaQsP-ghiDFgxg4o53QGxonjIDx3s9KoaHNbJ64aqOnX9GNV4q-nBsnA6wurkCL7Y0RYOGCgMSDprBeB-QpoXxh0D1FK2Tcim8mlvjHd_XRhsUTbHp1B-3osZbx1Frrnuj_lPgMhrHKZZIusyFMwON59f8Npswy6UcP3L7zSAwPW93hw-qYRxcjHjC6QRuVdum0253ronNuOaWzNtzEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOuefJxmvrcuJBjW7ryef8iMhO1Su9bq-kgMDmgsXelS0KS10r2CO-4Xr_GZX5extcHrE86oa726FwatAa3yHfRhSTqV8t6dpCtu8j4aDCfNNj6xhYpfn5Awmm4Wp7zN5UGV8M5n27ap3ifHYhjb5eRk597SgvpTi9jP1Pw_BKZcKCI3ozbv6HYtd2GSatHmUdOk37xyPCqbTR0trbgIj4BhN235h5N6N0uOYC2BV2l4Ovsd03Ng7ui0fi30eyHnya2tRtR1Eol4RA_a3o_3hMYAW90UONnpcGRep_o83Wv8cWGIK7lESyCZyr9RE7WRji3rx0G7Y5tN6FK59B86Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poWhfSlD1siljrhp__2hJCTLZKBvAfjgGlMhyM2eNGZ9In6WSyM06jmTRb27XvujzxjVYx_yu2sKYkPBpb73dgK97iKUuM1xA4G_HPACPbvNr78id9En9O5OYo5W18eHTtUCYTNq2UPJ1pDgQ3oC4-VatFq_yYeo5q4xA9I6K6jW-mwhV4Ha1kI_WqjyA3ITZKBL0WOCcxAiXzTrLv4s5D3zSJiXBpC_Ms69ow3X-KhZaMqHcFQmYIJNS-0cMuDmqJjilznajOUoUXhWDHV8iOBdyNA1wOZuHM1mIBhD8dd7aGxdXuLDR0OXMWQ2pvHfG_1HWxLrVjF4E5ehArFo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2Zs2L5H9LgpZ5pRawLERtRsCqC-J5qLLjCjKBZEduX2Y4HMPnY3gzW4Lk8xOsDSMgoahbeeDNPGZJWkcK-XJx2up6BIAd1Q4EeHqrMVQzhmj35Phj_Vf_EmiDdOsKBhSXQ1UYYtn_xFZFWuSElHTTsUeZOAhagA2-YXbQsOxK4Up5tctyc4yapp6WqR4KIiv-cNrfFG9FG9zO_O99854vljuX6X4tKFFzJ8WWP18dhV0QM9ZvTCJuynWgBSf8Rou-_CYjowS8kBVNPQX5JowXth_nR-rLsX5CZ02RNm47l7Th9o2peP1KNSxP0-jk9-RBQKXKys1skAcRKknMHh9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSmu5rlqHY99vC2mpi7UKlurndUX_Io4qIAyhZq6i0MuUYFa4QT9W8rAWzZ9TTdGQvPkOwJlOdhq4VkXT6gPLgVnAoKXfzLmSLscdOIqqs_FT_TFrU-IRGmBtosqk5SmU9t1iczsbNEKqb8kPTvuZj8mgCaC4BN3rLsaRkpGOkl1NtcY3TAPhgv83rHRsBy2tGZQOIHX3Y2VnoK3aoJzAD_D6Se6lcwIOxXJy-5BhdMJ6DTymNkuLSVyWJqXOxa3-kB9kngFvh-Kg-o3IliOCU5THO18oFBlRfbMks7ydF73JxYQMayI6KBvCTaDsJTriLImTCH1xBY_KKDNpv1JNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2ZCQdsy3_-HHGSkmV9H1h2-MtFAwIbSWRzecIWFmmPgnQzrKsHRStdluvcZfXx9tJMJNuDLi0M53KKws06gcNWZxvjTIqQqwAOdypTWPru5tfwvJmhA3gSHEbcck_g9YP9Uz8ysjkUBVloT5GDA3SFOT1A0X9Ao_D662iySbacLqa9RCCkgn2OqMsTVM1USzetOdddV5UP5Ob1cwb0q77_mYFtaV-dOkZotMffakLmZSI_KULTxDLxTfJHbAjdrzHiVGB2_ewkfkUopV5M1VZXY5Qh3UTEjsJ6VE8HjVRJelsUjBllB8MiitCec4TeUYm3QLQ1CXt-rO7HKWR-P_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=UEEGDWeyUCqD3dohRqqiVqdKMac1idme98X1pgkXmHtyjdYGAC3rJvouK3agC7zC-O-1L8IbQ0eL5fZdqLC7viUaXhTXVf-sF1VS0Ss9_lN7HQk2-t-wZ-zWkpVVOZOE_Urb9G2WM8_-_iB02uH9MnJWdnjvJAQHU_HrCC_cIXOOPgtGihcbRve_57rFESdJhQgGT1B87w4VjFPC_85MSDDU6Llq5RKQKibZD-qmhYG_GriiI844zAMFP5UNJS_rWii4Aq-4B0x0IW8UwmFp22gJtC6kT8dZkQdbUV1kPENhqEUhBrvh-RhNSes5vtNE8SZ89B6P831CtRYyQQSL7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=UEEGDWeyUCqD3dohRqqiVqdKMac1idme98X1pgkXmHtyjdYGAC3rJvouK3agC7zC-O-1L8IbQ0eL5fZdqLC7viUaXhTXVf-sF1VS0Ss9_lN7HQk2-t-wZ-zWkpVVOZOE_Urb9G2WM8_-_iB02uH9MnJWdnjvJAQHU_HrCC_cIXOOPgtGihcbRve_57rFESdJhQgGT1B87w4VjFPC_85MSDDU6Llq5RKQKibZD-qmhYG_GriiI844zAMFP5UNJS_rWii4Aq-4B0x0IW8UwmFp22gJtC6kT8dZkQdbUV1kPENhqEUhBrvh-RhNSes5vtNE8SZ89B6P831CtRYyQQSL7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=COZotVyPnAfinz2_IGcSK4qYpimiq5ZC5nFKt4pCMzOuST05A6BqF2ul0ZuyzhqP4M05HkUfUlsCv4b272NlxTt8hURw_G-v6iXsP6zLr1eQsZYF9MtYlRFovHAO007MEe9DrFfTve6GKw74VWD-byeOHo_tOjSi3KMkRakeHJ5_Oco9wnJ98UiXoTTPZwlVkz_aQs8NDROjwhv6mGis4N25S1fea35hQsIFbc_zRVKXO4psHn-9ZZe50wHpvEpWgjLgoyFAb7ZMT3XKphCfFhxETEmoSDcS1S3VuOsPqrqDpyOEEjhBJWftedxK43FTauPUgiyrJre7Lpfg6RpCgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=COZotVyPnAfinz2_IGcSK4qYpimiq5ZC5nFKt4pCMzOuST05A6BqF2ul0ZuyzhqP4M05HkUfUlsCv4b272NlxTt8hURw_G-v6iXsP6zLr1eQsZYF9MtYlRFovHAO007MEe9DrFfTve6GKw74VWD-byeOHo_tOjSi3KMkRakeHJ5_Oco9wnJ98UiXoTTPZwlVkz_aQs8NDROjwhv6mGis4N25S1fea35hQsIFbc_zRVKXO4psHn-9ZZe50wHpvEpWgjLgoyFAb7ZMT3XKphCfFhxETEmoSDcS1S3VuOsPqrqDpyOEEjhBJWftedxK43FTauPUgiyrJre7Lpfg6RpCgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=WIWYYZ_bYJTNMi102kQw6UWu-PrSRcZCFzxGgutFulPXKgtzjELp-VH7iQBriVtiH-bGse-F6VOENIfjYe_DCmX6lUt-fFL2evokunK1mRPfT-fZpuPneASCwjSj7DlygNPa-f-cfaPLiJb9IVKF_NYcEvb5K1uOqRYyVUdIPox75Pp8__mbtRMyL-NLDZNXXo1lA8srSb3NlQqqO9nHoCzNbr7MNnMDcRbbzMcXD3qvfKAkN1NMmpH5wqWnGRmr-rtNPwxwOd5Dsz69k_Y1FDWzRABKtHiP0jUt8ZfAq23Nn-Zbilv1bPHLTIPpqaKJ08bzqaKcSdTCuSIQp2t_yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=WIWYYZ_bYJTNMi102kQw6UWu-PrSRcZCFzxGgutFulPXKgtzjELp-VH7iQBriVtiH-bGse-F6VOENIfjYe_DCmX6lUt-fFL2evokunK1mRPfT-fZpuPneASCwjSj7DlygNPa-f-cfaPLiJb9IVKF_NYcEvb5K1uOqRYyVUdIPox75Pp8__mbtRMyL-NLDZNXXo1lA8srSb3NlQqqO9nHoCzNbr7MNnMDcRbbzMcXD3qvfKAkN1NMmpH5wqWnGRmr-rtNPwxwOd5Dsz69k_Y1FDWzRABKtHiP0jUt8ZfAq23Nn-Zbilv1bPHLTIPpqaKJ08bzqaKcSdTCuSIQp2t_yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=DOcqcBC5aAJSdYOp2Sxn_V2WuIkZ9U2ahINDVEfosIKGcuk3o1phhfAz473A8M4CUAsflzi1nflKQCKeVfWIccqiTCKgD9uDinulrfOPs39QbkEwRVekuO9MtZzBWP3pE2Bx8JXFqTx-fWJ-49Lkr7FFjeuHzRp-Hq5ymb-5VdxtkcVBYP-VFUzTvSIwPOhhH1gPMillBRWRzThcBzFOsShMaJyoF3KWFvniEJm7yVEWNQEETmH1WgKexK5z6vsHr-A2kM_NofOW9X2WTbboB6nvdf-V3m63HrMV_r4wwkWEZL1-G_i-c25NMkk0RArqMwmtHo_ZlO9xbjKX5zdzqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=DOcqcBC5aAJSdYOp2Sxn_V2WuIkZ9U2ahINDVEfosIKGcuk3o1phhfAz473A8M4CUAsflzi1nflKQCKeVfWIccqiTCKgD9uDinulrfOPs39QbkEwRVekuO9MtZzBWP3pE2Bx8JXFqTx-fWJ-49Lkr7FFjeuHzRp-Hq5ymb-5VdxtkcVBYP-VFUzTvSIwPOhhH1gPMillBRWRzThcBzFOsShMaJyoF3KWFvniEJm7yVEWNQEETmH1WgKexK5z6vsHr-A2kM_NofOW9X2WTbboB6nvdf-V3m63HrMV_r4wwkWEZL1-G_i-c25NMkk0RArqMwmtHo_ZlO9xbjKX5zdzqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=ssRfZjBjAB_OCqoV8wUjwsneXrnAkpcqmg3gtJ_DaM_AGSlQibm2W2eKnZPFVpI0JX_NsA5XcwSaV4sZcu9TyjKp4mA9--gq_BMJLAia_s78lee_64L2wePtnKDdpjppLfJFCNhU2xRHqiK6xIs1wQVlQP2ZEjv2t7edJtUhkl_deYsBLZDLFa3xKN4u0zBJsxtIra9T0piwhUkWoMyYEpitR5VuKwt68dq4voCkcF32vJMiHAz8-y_ZHGxi7XGPD6f3lUw9KzlcsS3NAsqvUpfIgljF4zr_3HQFhHM2zyJn1n8ocfeqIbUxmpY8oJkVhiisOOvp706nYZFdnxxUMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=ssRfZjBjAB_OCqoV8wUjwsneXrnAkpcqmg3gtJ_DaM_AGSlQibm2W2eKnZPFVpI0JX_NsA5XcwSaV4sZcu9TyjKp4mA9--gq_BMJLAia_s78lee_64L2wePtnKDdpjppLfJFCNhU2xRHqiK6xIs1wQVlQP2ZEjv2t7edJtUhkl_deYsBLZDLFa3xKN4u0zBJsxtIra9T0piwhUkWoMyYEpitR5VuKwt68dq4voCkcF32vJMiHAz8-y_ZHGxi7XGPD6f3lUw9KzlcsS3NAsqvUpfIgljF4zr_3HQFhHM2zyJn1n8ocfeqIbUxmpY8oJkVhiisOOvp706nYZFdnxxUMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=TK9YWa_2ocn2ff-Dm33vgopNkBU9VEb78ZyS5RpF03mkyoIXCKyyKt-FuGBw3zKSVQg2cNh3QrxVsFP4dpe9bKOhCRh9DNv-w5Ibto3ByrqzkLHRO_UYXksiZF6NizZO6b1vyTmvGRxjvCC1P2q9iumn1y7CwLjfaL3Yu45bMhLGxyCeavgSCTiycN65HhTAgQxmtSx4FnDBEk-6XwdVtEzKY5xChrI2fqgpNNzr7O6BMzQkux72_lezP7ntbh1P_kDM1TM1NITzKn6vLVne1AJrViNcbZwpP28TYhkGcQ0iq23Suju1PmhVpMXw45v9u2TSM08GTJmCCk2vWcGVGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=TK9YWa_2ocn2ff-Dm33vgopNkBU9VEb78ZyS5RpF03mkyoIXCKyyKt-FuGBw3zKSVQg2cNh3QrxVsFP4dpe9bKOhCRh9DNv-w5Ibto3ByrqzkLHRO_UYXksiZF6NizZO6b1vyTmvGRxjvCC1P2q9iumn1y7CwLjfaL3Yu45bMhLGxyCeavgSCTiycN65HhTAgQxmtSx4FnDBEk-6XwdVtEzKY5xChrI2fqgpNNzr7O6BMzQkux72_lezP7ntbh1P_kDM1TM1NITzKn6vLVne1AJrViNcbZwpP28TYhkGcQ0iq23Suju1PmhVpMXw45v9u2TSM08GTJmCCk2vWcGVGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما درباره بمباران نیروگاه‌های برق غیرنظامی و پل‌ها صحبت می‌کنید. بخش بزرگی از جهان این کار رو جنایت جنگی می‌دونه. شما هم همین نظر رو دارید؟
🇺🇸
ترامپ:
به این سؤال جواب نمیدم. شما از کدوم رسانه‌ای هستید؟
🎙
خبرنگار:
نیویورک تایمز.
🇺🇸
ترامپ:
حدسش رو زده بودم؛ نیویورک تایمزِ ورشکسته!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4sKjXJcQ3FKz-FzDf-eO7Utatwt-sPtFvIQ9kh6JzGvyyHrXaCLkbO7bIB3oyUTOZHinuMOYTWgB1NhwNraxLFSdXRFR-O_9GjSCBMdMp6SbnZKOCCLzA3Y0O3iehgzJn3XTfu1IhbXM5JsBzaOmYjkr49k-4SiXE7xBAGwbij7H1ooM3Zi1lzknvkXjQkk9jowmKbaiqAxt5OGOpQVtzqm4fLetpqeIqGTziqYlCgcUIVRQcR-MZJbBU0m0mq1mpaIzNDky6fGPu2dvW8Zwgn0OD6QI3XVB3GY32cSJqsG-P-X6lL__z8xS1rzuAbJiNh3AITublMOD7BRTvkV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhktrQWtrU6C0IvWYYajs1OxEkjsKn9ti9oIaIbM-BhzontvSIign1v8r1hdKyVeMbKj1o_vSJo6hwdPPRm4U3oH5TbY8KKvdiD3flWqATzSmHbdwVKxidng3wcjJPKR4-Qf3cGIFwJskQDXlB3taZhGc-4rtKSz4gFoWKuxvI6Q_KeBwIArgt3vGE4Jfl3LjDPXyAt7YIOhYrRQwBM-xzPTyFoz-dTMy0WhBB8xFcIZXfGHVHItXgOE9ZMubHt6jA4ATDjO4lCt6Vb7RpD_5mN5xm0V1ZF1NOSk4WkUEQto4L-HPWPHjFVFR8M1fDK63yQ27giWHiHsKGIQBlJ2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVyFg8Z0erN10z4VfyNRY57R4gMh3-2TYbcM2Z0-J1MLgtaYhj8tdk7j3IX_dYfsIqeCR7czQT1AMRqYNIz6Shs66sV1FHT2ZmPJTUvxgPBMiELSs5CMb6m32WWFGtfAFxCw9V1Hi6qKpxHquhnfzLlfgn-_3476u9WZi4oEKSl8kUDVZwi50LiDUP6wqbycFHbwUTfyTOs3LX2PQ9BDZVRekI5z5yo6H9krI_ysv2BhfqNf4EaKukxgiT-pXZqbitezYnoDV-UGPmzP13c98yojZvsNVeB1h6SsjgUhKJGpm0xXWfsxIZ1PdnGbZW6d96EZSvDwQlgxO1BNwpyGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=Ww0eTP33A-b71QsxxW-ZQ_eGMoZN0bSgPzHBlJAFtU0pqNRsvLI0IIPMNVW9-nhwJLyHZZGpp1IMIfyCLCLJhkf_irT9lGQUKsy84SEaK-IZBxilLZJYpDQhtkcdYA4CTKvJSUUDHVZuHUre0QMM4Psd76pAPPeBaswyVltV5HZNcT-bjg0ySLVdS6ELaXbKcSVjZ8iysfp-H-k5arwdKM5nefSLmHxzDw7dgZUgurYRfcbaBLcDa9lVggeDknI-qk8hqjOnUAaEGJ3Nqdc1tLzJDd4IciIY9o7P-kQyyvZ77p5jUj5KR6018ntMD2CVXwEQAY6Ai6KDZIzS6hdEUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=Ww0eTP33A-b71QsxxW-ZQ_eGMoZN0bSgPzHBlJAFtU0pqNRsvLI0IIPMNVW9-nhwJLyHZZGpp1IMIfyCLCLJhkf_irT9lGQUKsy84SEaK-IZBxilLZJYpDQhtkcdYA4CTKvJSUUDHVZuHUre0QMM4Psd76pAPPeBaswyVltV5HZNcT-bjg0ySLVdS6ELaXbKcSVjZ8iysfp-H-k5arwdKM5nefSLmHxzDw7dgZUgurYRfcbaBLcDa9lVggeDknI-qk8hqjOnUAaEGJ3Nqdc1tLzJDd4IciIY9o7P-kQyyvZ77p5jUj5KR6018ntMD2CVXwEQAY6Ai6KDZIzS6hdEUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آخرین مصاحبه اکبرعبدی با گریه:
ماهی یک میلیون تومن به خانواده ها پول میدن
وقتی روغن یک میلیون و هفتصده ، این یک میلیون روغن برای چی میخوان مردم ؟ برای جق جق در خونشون میخوان که بریزن صدا نده ؟
حالا روغن خرید ؛ باهاش چی بخره که چیزی درست کنه ؟
نمیدونم این خدا هم حرف گوش نمیکنه ، من با کسی حرفی ندارم فقط از خدا میخوام به همه کمک کنه
فرقی نمیکنه فقط به ایرانی کمک کنه
به هممون کمک کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDu-eafyFSfYYDYeFqxfnv-8RlzBSxnEXZ1uUAIR6yH_GWMWrbjiEtz-K8-_M9g5LIiTFjy0gowZPMGJsUbhO52DQXzcVYY_eet4Kjqn2UlqlxpLmP7ZecLvDyvnHVx-f0Df-Gwzk0KoPkH1lRPgkKjivDalnjLWq7jixXdf_axeheU6dZ0fykrfSVkS9h84oYr-U8z5IY7z0hDFs_TMaLAwZB-edMnBUT8dwk36YUifjTrVFbR8vrQTAj1EzTPJC_9b_ijj-aPqzv14k0UDAd1jZ4zATXsuo8zHM6Mt0kwBbCagDT2pfox4SVj4DaelQGGzeRGSP9t__OKSvk87mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co3W3viXgTgu4aY0MDLAzariXl9Yx2HwmMIKmpNsJsfozQNYWsSt9saG-ho2HPEzg3SsyHp-j3M9-SMe6TuNNrCJUM604mi7T2Ag0vbvOMOIIOcF51qiqndl8A2EDUUtHgYOlMtfG1U_wdz8saEJcr28r5SCXc5g9dwAyXGvDmsnRurG_XStwdnCRdwRCT92_Z2VwGQscGq0_hWu2idl32i67LSo9-liRjPi-U-wy-sqT76TQRiVACB3SfbvwE17Hzl36-E4Rju1c1Q4hsxeqSQg3SD5owowWgu2Zo_qM79OpyEetrxrCMRr_gwFp206xxgR05NyYTyUM9CQz9DDyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=qbmgN60WEEaS9oTL37BN8txAncDZYvNXsgNox9IbX4KtZYwMHTpzm_VI4sroWE4Te4gpf0sacVZgG3Yr9BrIxvSF7x-BsNYgVrvw86dlZ5upPr-59Bo5CIAV6FERG-pi0QSboCbvcTLtRscaaU00VVadCXVB0FR1mCakcH0n1egAHARHyp5NGnZ2cdosOpsRoFKL0upZilRnJveKEGjmzFqbujX-pi_6IR3auDODhqUfD8FXIZnHG8TFbl1Po4rie7nlx0mKoek9pjtO-IeEFIAigVk6JU-Hn25XLb9C4zf4IezEh970DX9U8y--Fiaqp35xniCe5sP7FYrEg4l2Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=qbmgN60WEEaS9oTL37BN8txAncDZYvNXsgNox9IbX4KtZYwMHTpzm_VI4sroWE4Te4gpf0sacVZgG3Yr9BrIxvSF7x-BsNYgVrvw86dlZ5upPr-59Bo5CIAV6FERG-pi0QSboCbvcTLtRscaaU00VVadCXVB0FR1mCakcH0n1egAHARHyp5NGnZ2cdosOpsRoFKL0upZilRnJveKEGjmzFqbujX-pi_6IR3auDODhqUfD8FXIZnHG8TFbl1Po4rie7nlx0mKoek9pjtO-IeEFIAigVk6JU-Hn25XLb9C4zf4IezEh970DX9U8y--Fiaqp35xniCe5sP7FYrEg4l2Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPs52dR3bQdHm6FIe0Ka6RM7id0xjvnZQCkP9PGDkAUTWnEkU5XZVIoy59a1sHS5R0aGo_9MIXaxEh5-V8eOdACHIncYza9X6mpzu_wfpXChFIXJ2ZFimexIMrSt6_nSSTAsWlVnkmCbN86agiURVy1znjpy6ChWpzTHqbfxGPZM4VHwCgCGW1HaRTPK7NZDI88hObyFtWp4mA4V3cr4xxL8QnFMxCymTV-JQ38u_BYB6eYWRW0dLGRFso5kFRa1G3rVMXabU74o0lEDzT7oFa72di7KZtjPW3p1ojTSIdzhZHrB-owtlP_MRo-Ho9iHEMcDszog7p7Ws1nG7X3pTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ:
رئیس‌جمهور شی در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت؛ و این گفته شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم؛
ضمن اینکه خودم هم لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
به همین ترتیب، رئیس‌جمهور پوتین نیز با وجود جنگ هولناکی که در اوکراین جریان دارد (و روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز چنین است)، به من گفت که به ایران سلاح نخواهد فروخت.
او درک می‌کند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را می‌پردازند و من هیچ اطلاعی ندارم که آن سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به عقیده من، دو کشور عمده‌ای که اغلب در ارتباط با موضوع ایران از آن‌ها نام برده می‌شود، در این کار مشارکت ندارند. اگر چنین می‌کردند، برایشان بسیار بد تمام می‌شد؛ و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJD9o4GLgcpcLswfj5bk2MK2IYCO1FDqgfVCvq9vXe7G2bpUoOA8kqB0ospLThyh4O0UOuiwN1thrS3K2hkp0pWgCzYuk_8rVtzrlFg-DG8V0_9t9GRzBuayF5fcIe7ZXplIyuRdcsTueO7ThF4cXx1RseCJ_8dwdSw2dRI8eZKilJkKgxjk7JMkcr6W4qYHjtAXVBcUtJoV6wwIfUAOnw2HbPnvx8HRtMz9DgOoYHeD_EfzHY4RKteZOEFXfWMHCmKrZaZBcdMElzL-6-NGqX0kc9BcGgMNLITBsWfw0gP__OZEmIL5daeslPyATXQluJYiPl8-6fccQcyZkXISjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X5GJtu6lyb00NyIdGBgx12C9ZehDwlb8G-S1kSDHbTUS50-Hw4qtkkxfNyvt-4t_oXai6eG488oPdY4tmQ0PupaKCeC1EV_fy4AwV0UNJk6hPBobKAUqYO4pQ3GSEOgEkJ7YJ7WSjFIM67EiIVnCfdyJsrcCER0xsJ-Uqa5iqPecV7oiY5HAoK5FmoIPnDKOzldGD35Yn6Ow2PW4D5j-M90v3wNT2i1lB5mXFag7GTzpblm3T9BWa4sVCwinTX_raHl6rRZ0J_pAFlno89bmlxZJKY4ECGLj6SKGhOAHmjQv-CbIu1rbYuYO6yRK4PXcFdiM5oBjzjFUGpm4Jj82Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQwSvCAS412C-360uG9QaI-c_5tXXF1nOCLDRe-lfSV7ML37hlruttAV5T5NxXGeNAoc-cIUcaHsfkE6IFCGG4U1reyMXsgIqE2ryHcPdXWg1I6UFEWSLfZjRsSXC1APei0w9F5w4U9cmwMrahuhN0PDkoxgTlVlc3tmzZx-zcJoZQhdrFpXptjuBHvYkT3FRjwDvs7Mjzp3vtGQlNlDWArGxgw9IvNc69I3GFOHpnV5JYB7KxfRx6rles2L294aGiLhH4ktyiubIkIE01zsb1uf3lsAUmYlprFu7CyDbwcPpOJRqdZb4a0D552fW0jrwRhnVoS9ytb9pq07nXGGYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=iD53_ieuwF_nqXfs1wiZ8vdw_UE1n-CktJ_BgS5Ofd0x_nRFpoC8eN7nsTiioN8seg2qYP5jeKkEmL51nhgZYHrfdr2HdNXS2Z8sNzvS8SU1QoBYPd0BWAv5U6Tv9ZIbourKocKCMUbgScF8TLxNlQ2hxAOq1ERhRmCkgFpgvJ2KTognufrgMVjVOLUQmfA8Fzxc5J4vxJ2fUpsBHgvG-rTGTI0LyjuVpPGCMZ_K73iQXFE8auN-OJJYWKF48GFyfDjEeD9qTJ6q0NqZDo0O010FAs5YqT5HRinjRMxY1oINmNq72Nh299qgh9RIpF4cyT-z5Of90C1O3aMbiv706g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=iD53_ieuwF_nqXfs1wiZ8vdw_UE1n-CktJ_BgS5Ofd0x_nRFpoC8eN7nsTiioN8seg2qYP5jeKkEmL51nhgZYHrfdr2HdNXS2Z8sNzvS8SU1QoBYPd0BWAv5U6Tv9ZIbourKocKCMUbgScF8TLxNlQ2hxAOq1ERhRmCkgFpgvJ2KTognufrgMVjVOLUQmfA8Fzxc5J4vxJ2fUpsBHgvG-rTGTI0LyjuVpPGCMZ_K73iQXFE8auN-OJJYWKF48GFyfDjEeD9qTJ6q0NqZDo0O010FAs5YqT5HRinjRMxY1oINmNq72Nh299qgh9RIpF4cyT-z5Of90C1O3aMbiv706g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=eB5tU6aUH35gIVybu094DO4Tx_2j2E5l90UBq7XbBz3Yhr_4-D2QPqZS-NpJ9EQiyEPIUCyZDkxITfKLDIPBoCXm4SeNgeuDCMHvFdFkuSVQNqQNVXtaNgPiSo35--lFMuW6WECwLBZ_-GdunNJhmM5gcLL6wex60ESwk0sHvzDjD4TFcrqXI_4kOKwkZw6YDXQJuPPyOIdoexV6HmDm5Q5sWkdCVBq62wjXaJpM7jTOLJ3FRUNG9WL9X-a1dpgGGXMISTC9nOpNpcrvnYtV0ttG7sKJHSihYT-1LCaFE8R4lupdUhoGhOCqSpix605Yrbg4LJKxn7iota7jMI37XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=eB5tU6aUH35gIVybu094DO4Tx_2j2E5l90UBq7XbBz3Yhr_4-D2QPqZS-NpJ9EQiyEPIUCyZDkxITfKLDIPBoCXm4SeNgeuDCMHvFdFkuSVQNqQNVXtaNgPiSo35--lFMuW6WECwLBZ_-GdunNJhmM5gcLL6wex60ESwk0sHvzDjD4TFcrqXI_4kOKwkZw6YDXQJuPPyOIdoexV6HmDm5Q5sWkdCVBq62wjXaJpM7jTOLJ3FRUNG9WL9X-a1dpgGGXMISTC9nOpNpcrvnYtV0ttG7sKJHSihYT-1LCaFE8R4lupdUhoGhOCqSpix605Yrbg4LJKxn7iota7jMI37XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLVwVfjfA5htjIhYcGW_WWiyAnJpwXozCncwhND04xocBOboGyMWvrN5_YSjvb3r17uN0CM7olQREGWrX2XigwM2EBZJkHpX5Zi3kY08dJhqdaBhu461ixH2zkbZvH0DhVLQcmkAWJ6ZbcXowpwlN4kSUSo_NEB-l6ULOLpF0JM4wAPC8f7rvaJgyHW9vhbkHhWtiYkVIuPtgOybW5pa0DMMWTf15hppKMTAPqbRjuD-kJbmoC0i-ftIYaNlYojpFU78DChyvpd460TKpHfJeP43sH9gEn_2nvsb1-D-4xHqtUoenDbNKd2MpuGGH-M8CwIGuiJQQHNUUJX-EmSthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=SiVcueuZJsXPEr_pUWnn-7AUUFvHrxQx8ZlfHdgSQYvWgD9C3CYVorQEi_Yha7avEy3aIP84brdH2KetcQSRD0-sqZMWO0HF6OcyMebCZ1xMytplQKwCRw-K0uNjaCNz_Wdq-zNS3lcCjaI7gP94a5g4IMfXdNuXyIbex7LBZidzOo6nUaoGB3eGDqixgSYkNioiDzgvzuAYPobMHVVTT5TBmaLObQbqND8LAbkbW6SbGLo1_UYt6UNUPevKSYK1s_xgLkM-shAmKr5kyMaziVt9SU3Qmgui-B4oRPEl7lU8IV-W-L42_jjvEE7vcObWZPp5U6CKIjqPIcKhbcYfNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=SiVcueuZJsXPEr_pUWnn-7AUUFvHrxQx8ZlfHdgSQYvWgD9C3CYVorQEi_Yha7avEy3aIP84brdH2KetcQSRD0-sqZMWO0HF6OcyMebCZ1xMytplQKwCRw-K0uNjaCNz_Wdq-zNS3lcCjaI7gP94a5g4IMfXdNuXyIbex7LBZidzOo6nUaoGB3eGDqixgSYkNioiDzgvzuAYPobMHVVTT5TBmaLObQbqND8LAbkbW6SbGLo1_UYt6UNUPevKSYK1s_xgLkM-shAmKr5kyMaziVt9SU3Qmgui-B4oRPEl7lU8IV-W-L42_jjvEE7vcObWZPp5U6CKIjqPIcKhbcYfNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
❌
👑
مقایسه تسلط زبان خارجه:
وزیر امور خارجه کنونی دارای دکتری علوم سیاسی از انگلیس
با
نخست وزیر ۵۰ سال قبل ایران دارای مدرک کارشناسی علوم سیاسی از بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=ngkHnvpdHWmGq_CFEmcAXTrvF_I1pW7eoa_daPMggknOFrUkeL30BW3SVS83nqv6vk-vFVe6FCDbeYmr3A_39gF8lSUk0RULU9SvUUqFrihIO9kVm6yxUKQg2uxcviRYQHpSebetBv2Bu0XsHdNAUuSESRCzMhOpQ668Pj3yZgbAm333oaHFfiIZiB6jgT4EJqZFCA8d7k6Dy6jpcGlsQmUBfBFSChHs4b2TLH5VgIhhSwKtB3idcExYYwyMfxfQwVzUvkMe7DDukwJKeambCvgeMTu8X-6S814HxbYS--3suS8NAhfZEodLdYfhuP8TtCAPF6w46OD5aUKrFdNit5KXaRVoIyeGqJ--cPNX6JFKK2XSKim8HLeAy8z4vt1utQx4SWGtgLynl1JHfoDwt5G_ipV46hYQqlkp14H-aSnSELeefRRMZHOGPclAYnZZiYEozU7i03D-vb-sTBJLIeFQWJLKqWl6TT1sVdfDF_66akytwL-f974s1AtN6VXlIet1PPXrwH9GJ0DA1I0GCATTaw5cjgUBQAuAT_lnXdEc6xZXNly37IOVyRFx72HaoVm0KCTBuKYqZhDJDWxWD0mtYCWfKaKAmr2T7Wxy47l0XZKZo-WygXvVsmPFXGveShHF35AY4bMfUAWtpi2ikIDuNzSL161nrgAGKcjhEcY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=ngkHnvpdHWmGq_CFEmcAXTrvF_I1pW7eoa_daPMggknOFrUkeL30BW3SVS83nqv6vk-vFVe6FCDbeYmr3A_39gF8lSUk0RULU9SvUUqFrihIO9kVm6yxUKQg2uxcviRYQHpSebetBv2Bu0XsHdNAUuSESRCzMhOpQ668Pj3yZgbAm333oaHFfiIZiB6jgT4EJqZFCA8d7k6Dy6jpcGlsQmUBfBFSChHs4b2TLH5VgIhhSwKtB3idcExYYwyMfxfQwVzUvkMe7DDukwJKeambCvgeMTu8X-6S814HxbYS--3suS8NAhfZEodLdYfhuP8TtCAPF6w46OD5aUKrFdNit5KXaRVoIyeGqJ--cPNX6JFKK2XSKim8HLeAy8z4vt1utQx4SWGtgLynl1JHfoDwt5G_ipV46hYQqlkp14H-aSnSELeefRRMZHOGPclAYnZZiYEozU7i03D-vb-sTBJLIeFQWJLKqWl6TT1sVdfDF_66akytwL-f974s1AtN6VXlIet1PPXrwH9GJ0DA1I0GCATTaw5cjgUBQAuAT_lnXdEc6xZXNly37IOVyRFx72HaoVm0KCTBuKYqZhDJDWxWD0mtYCWfKaKAmr2T7Wxy47l0XZKZo-WygXvVsmPFXGveShHF35AY4bMfUAWtpi2ikIDuNzSL161nrgAGKcjhEcY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عباس:
چهل روز جنگ و محاصره بود هیچ کالایی کم نیومد
بله قیمت ها یکم افزایش پیدا کرد که طبیعیه
یکی از مهمون های عالی رتبه ما اومد ایران و تهران گفت من وقتی شهر دیدم تعجب کردم
گفتم این همون شهریه که جنگیده و محاصره کشیده ؟ من فک کردم الان بیام تهران شهر مفلوکیه
همه دنیا داره به ما احترام میزاره جز خودمون
من رفتم عراق حرم اونجا استقبالی که عراقی ها ازم کردن عجیب غریب بود اونم ساعت 2 شب
این استقبال از من نبود از وزیر خارجه جمهوری اسلامی اونا به من میگفتن قهرمان
عراقی ها این همه شور و شوق داشتن اونوقت صداسیما یدونشم پخش نکرد
یه نفرم اون وسط تو حرم گفت مرگ بر سازشگر
با مرگ بر عراقچی مگه مشکل حل میشه ؟ من اگه وزیرخارجه نبودم باور کن پشت لانچر بودم الان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfBLyU54Qk9BHtuR5lWk-HLhtNivKZK_93UuA3Bsrgj3wnPPRBvoahHxrQUm9hYpxw0jp65jFwBcsOJJ-M2U8JdCmDMnAfqEiBFJ2Uq4KqSIXJ4JA4c6mOi0PIu_puQ3qsjFecG_DyxL4R9h6fkMVcm-QbK7btKkDkHRDIl-8KM3cZ3pokwuDaDKeiDiBdmwcw3fVK02qjL8HeW3Ly79aIj4KmjZNrVwqmX2FIWIZzytza5ahirm6h4qoJLneQODrWNKAxxGu6rx971b_txmvW5vZIgZWuWF4XmJgb10AVMeNIkPoen5y35l5DstFUmv5xtaM6c9wI9huv6vnp-xPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvlsIG61_OmwikD-6w2ED6hfRnbYH38y5mnQX1-CGz9QPn0FJGr8Gbvkf6_W9hkAxhl3p70gb9t4cP0S0GCZMC7N8h2Va_ExTlB-oExh4gpyVBuu6L_HI50nNPk-cLEenXHI55fX02TDKfEKYLNEk5OCl4defNfUo9OgOcOJcnp_FAUTVC03h3ummtmGugF_j8x8tzm6OOj4JTVGuhc3aLxpjBrdejSj09reMpMsvgOCx0O933KwE_mjlUC9fbM_CZJww4Ic7pmRl-uuczqg-0X4A5vkivHEI0Ri6qKmzGUg-l74ZUHw89Z57-rlLizrwW__b4GkV3Mn3GS8EV9Y7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DecaU7fnzQIGXncuE1BFMFrdQXLMG3sphX0myTwvhGILByOrda9phvA9u2wid-myyr35rJvgfOuKHm37t4oHcSuYrxOVf0zqxIU3m74Mig-QSPOuvF-CDG5HVxGjuIHwl9lG2j5Jp8ADfCImXSRYTRgvmvrzM3NyGpktsLfktUH701X4OW1taZ0NWBgVKaQ_rUIFP6EV8s0GQQsbG6WAEaZRN-aFikZWemSP-KCMJk9efpy3T1_rCd-TabWeGXU0shhwAjbNG7i-75aJGoSesF-SlYJpNV-kj-QTXHw3P1OH7SgqAt4rlySp-JA0avw2U5BZgsKNxw8GsW-FUEDMVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ER0jXxEu7xE28e-Bav-xWNMgVmzVFreg2XvAmX_tJMDzSFbmrg060xKD_WBj6fJzhNdezQrvMzA-554I3m0Pd8kF0Xxf5sVJm48CV_pAzsU4vMnDgrMQLgMkk99gPbdiIydLfQWnUftKPQrz9TJ088vHUhnT6x5Hw8WiwNB9PJ0f7kIFG92beE0WQP3qaaOsfzbjVzUK7x4_iezR4jSg09M2bRGxRymVnMbXjlSV_ZIjIYPW_jXFQZ3B65mVSUt7lAchA5TAugQKAyhtHWZcyral0upBuGK7PKdoEeXYZQojqruNtYypgvIvuRpCOjdbcPQIlkV9g9hjskWdZ6EfSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=GLrVjQQtyE3RKyMqi_1qYAgASQS3SUQBq4RrYa0UwbvaWQYIg_tu9RRs3wCPnsw1zm0g-q6Kz_8tnjkE8goWrvzVfkxRHZRiN283AyzhcEaqsylLiF3QDUK7rK5gjdQlabnGwzcQHsB_N6v9gfzX00H4yJOOuEmyst8tP-bOtYC0CEcmUt5ng8eksFfX3sc8PdG_or6iCLpZAEsqjU2iB_ggZ8YSwbGqKGk7Y6UJvfDo-IGFOwPsLog-L5zYfIzK8klgvVUtCUiljPSHeUGFdYQyPENt6ZZDNJs3dBwfhQjneukEwlTqy3PeLXttCPtv9reExYcPPvDTrXAtgiSTyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=GLrVjQQtyE3RKyMqi_1qYAgASQS3SUQBq4RrYa0UwbvaWQYIg_tu9RRs3wCPnsw1zm0g-q6Kz_8tnjkE8goWrvzVfkxRHZRiN283AyzhcEaqsylLiF3QDUK7rK5gjdQlabnGwzcQHsB_N6v9gfzX00H4yJOOuEmyst8tP-bOtYC0CEcmUt5ng8eksFfX3sc8PdG_or6iCLpZAEsqjU2iB_ggZ8YSwbGqKGk7Y6UJvfDo-IGFOwPsLog-L5zYfIzK8klgvVUtCUiljPSHeUGFdYQyPENt6ZZDNJs3dBwfhQjneukEwlTqy3PeLXttCPtv9reExYcPPvDTrXAtgiSTyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeydNsO-V2mYcwpZ8RxvaQA4jVIA6TskHEX1mcHrKMYOMH981MdkB8N8PxK3lPi9V79FLCoa3XOeEX9ESTosDhtB1xhtwTXkgjd4C5mqaXcBafMGz-Br-RRzNav2ZWi9IgomfLk6dfbnXWcI8d1xhsT8nou-MV0y-8ANcOqR59ygOCXiXpPoc-lpO50-4G2gHjKCMnv33dt594egEqXW7cwc-zTjUOMLY1yrGfwUL8BeohsbvjEVtGweR3qAg6iHBmPeXxpo1ZVNZXxQTjv4wHJxkv25GXE6oq3Rb3_mAoTGogg56TlChfwrOzK6pUmMjNxvNFCoVVgJrfjuvNzvlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3dwH-g7JWApaaanhVqmMh3-9SLYLJVNDsaSFa9bOIJCGcmxOQjCRhgBFEwZfgbwYgjjo7jo7XuAMOv0SqLUAhJLFfvrH0VgF4iHV1g52Xqvk1PIlR8mCwrcY7jRc0Fe1vWxQKFPH9useLnfXbHJWmBf9OO93BB-20lOcq4wdXoQPMGpAm7b3xjyUA-TUklkCMGSobPVQaAach_wj3nUn32g6W0H058USTK83RxG2oXxXYlLnB1qLZTnLQekbSPTlgPP5vLR3ON-_dAXivzEfh0nSBUbWL3oy1Lp4Y6i-kU3IHks-KJIfsyMaykYCowDL86PKAyL2JKYpOb-ocG94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=Ni-gPMcyk_nH6qFKVJxnjvlAa7Uq8q7nOQ0y4-gsdc-PH0Z4GEmSR7drdDDvRifvNpWo-BYsLUJ4fFHG0SHYu309KJINeuIX9eZF1s-Jlo_p1y2Jc-fmpg86wkyoMVm33FJqqrQCh0SRUORZiRNxLnGWEdpfNp0L2m1QczpJgyj-0YWkxpwHx8PMRp-y3RJLJKfsLhH7iFwsp0MjpMnwJAps8R5KJ5p9m2Wpeq4G2B2Or1ga8U1NqZcba0Y6ipDiMtl1YGDWBmyq34a5pCrj_jBKmLXrijkIBjY8r0fWYf4u5UwWRQNC2V8UQPDwycXRfVOwjb6jyJpkhdT66AHk6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=Ni-gPMcyk_nH6qFKVJxnjvlAa7Uq8q7nOQ0y4-gsdc-PH0Z4GEmSR7drdDDvRifvNpWo-BYsLUJ4fFHG0SHYu309KJINeuIX9eZF1s-Jlo_p1y2Jc-fmpg86wkyoMVm33FJqqrQCh0SRUORZiRNxLnGWEdpfNp0L2m1QczpJgyj-0YWkxpwHx8PMRp-y3RJLJKfsLhH7iFwsp0MjpMnwJAps8R5KJ5p9m2Wpeq4G2B2Or1ga8U1NqZcba0Y6ipDiMtl1YGDWBmyq34a5pCrj_jBKmLXrijkIBjY8r0fWYf4u5UwWRQNC2V8UQPDwycXRfVOwjb6jyJpkhdT66AHk6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=PsO-xsKzrvT8RcWaFR6yDZ3llilFF78b6Y3AgvLu-k8aPXDdVLwNzapk_0K-xvjlxGlqBawEeTqR-yZ2zfwwQOjrarOmvaBGpg-XU6v829T3FDvIcZ2A9aItaTDH_lgyr1fc3k2m7kMT7-5abw2EXZd21bIQfL2nwbsoxQ4_FMC8imNQfB2jyOAfm92sdOpYrmwrQ9SaK1RxG0k1ltXlKb7_EmgT848yzOhjEphraAlzHxHWBNPazoYi72XUg0dC-9jK5atjeyc9vyu8rVJfqARSjOifxwuCrtM0iTCk1rEPNSOEctkfdoYKFN9yPCwYUXE2KmvUfMGn2WO90HiEhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=PsO-xsKzrvT8RcWaFR6yDZ3llilFF78b6Y3AgvLu-k8aPXDdVLwNzapk_0K-xvjlxGlqBawEeTqR-yZ2zfwwQOjrarOmvaBGpg-XU6v829T3FDvIcZ2A9aItaTDH_lgyr1fc3k2m7kMT7-5abw2EXZd21bIQfL2nwbsoxQ4_FMC8imNQfB2jyOAfm92sdOpYrmwrQ9SaK1RxG0k1ltXlKb7_EmgT848yzOhjEphraAlzHxHWBNPazoYi72XUg0dC-9jK5atjeyc9vyu8rVJfqARSjOifxwuCrtM0iTCk1rEPNSOEctkfdoYKFN9yPCwYUXE2KmvUfMGn2WO90HiEhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=c0Hq1VNs_R_UVIuatKTnjxIjcQJRLd10xP6Je4mstIzfSBOx-O8ET0ePke8Jg2GnAaKUL5PFdYs1gBkNdIGKdHrbx9ZkRrvjwmtNagke4kZ7K6PupWDhvRAVJavzCV3QrEoQY8xyjnVEf9jbn-_HcEHTc6-SnyN3SZPegNeZVXnzzJ0rvokM2SRqWjTNo-UqVcQQR9GaWtnMQOEO5NpEWyo2fIhgG6qRGRgm-n34ydWM7_LkJOWsFWz8QBFS69Z6bHULltinzu_KbEUNpF5bikMktSyPYV2N56LcjoUMNeUAciyH_oA4AuL8RihJvKw0Em09K5JKl2BnA0bgQ6abtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=c0Hq1VNs_R_UVIuatKTnjxIjcQJRLd10xP6Je4mstIzfSBOx-O8ET0ePke8Jg2GnAaKUL5PFdYs1gBkNdIGKdHrbx9ZkRrvjwmtNagke4kZ7K6PupWDhvRAVJavzCV3QrEoQY8xyjnVEf9jbn-_HcEHTc6-SnyN3SZPegNeZVXnzzJ0rvokM2SRqWjTNo-UqVcQQR9GaWtnMQOEO5NpEWyo2fIhgG6qRGRgm-n34ydWM7_LkJOWsFWz8QBFS69Z6bHULltinzu_KbEUNpF5bikMktSyPYV2N56LcjoUMNeUAciyH_oA4AuL8RihJvKw0Em09K5JKl2BnA0bgQ6abtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=i0Rk1KmF4r2iMyT6OaFO96uvemzZOVC_EDr3PCbiU2afRV8UWarI79jiO6L3FT2F5pyz5-y1mg0lZV3D-O9NAvWtsIsNkib1ya8fK32xc-e1Z80VwoSb7cV63h7mCsw0smbIhq-YBXgonVIGitSOgZzovP-eL07IQ5VVMiV81MO1RlmncJWuTbGQhfB7gFVdF8h11M5TOgOt-SesUc5JUuPtsknDeQ7OrmyvtKc2GLBLDp8IvZIZ6iSJUkDsD3wshKwIh2lfzsp-1KLjC6EQ9yLqJ_w62FZ3QWr4yS5d2lIgeY51BzJBWIXwTRKv65ThYP4IAc-EeyHcTAGXKQ1izQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=i0Rk1KmF4r2iMyT6OaFO96uvemzZOVC_EDr3PCbiU2afRV8UWarI79jiO6L3FT2F5pyz5-y1mg0lZV3D-O9NAvWtsIsNkib1ya8fK32xc-e1Z80VwoSb7cV63h7mCsw0smbIhq-YBXgonVIGitSOgZzovP-eL07IQ5VVMiV81MO1RlmncJWuTbGQhfB7gFVdF8h11M5TOgOt-SesUc5JUuPtsknDeQ7OrmyvtKc2GLBLDp8IvZIZ6iSJUkDsD3wshKwIh2lfzsp-1KLjC6EQ9yLqJ_w62FZ3QWr4yS5d2lIgeY51BzJBWIXwTRKv65ThYP4IAc-EeyHcTAGXKQ1izQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=NbRq4Fbw2qeNKheqz50arFX6CMt1bkrj5_ck3dgxdgiMLatgo3Ta71OU7i6XEG4XGpYjzwr7JNUrKqP9MrPMh6-nRbTb0VCmFJy1c7qApp7zQ9vL2p1xQwxrgQG3s3muRhRbEHu30R3Ir9_bKwE22cRwYUlozY5z_iwkZdlQkY_mUTTej6xQfcHa7F48JzKVXBp-y6e1jjL72EDF-YkftHzx6ygEW3BRYGYB7cb9q1p8NyU-WPPz2QaombtYWxxM4kjN7_N2slyRmhFUUVxrz-MP0EOVjMiq2wHcmkY0ihUvTFb2eHH1vY-BN4IosGSncNd7fRYXGexBGwGhVv-HXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=NbRq4Fbw2qeNKheqz50arFX6CMt1bkrj5_ck3dgxdgiMLatgo3Ta71OU7i6XEG4XGpYjzwr7JNUrKqP9MrPMh6-nRbTb0VCmFJy1c7qApp7zQ9vL2p1xQwxrgQG3s3muRhRbEHu30R3Ir9_bKwE22cRwYUlozY5z_iwkZdlQkY_mUTTej6xQfcHa7F48JzKVXBp-y6e1jjL72EDF-YkftHzx6ygEW3BRYGYB7cb9q1p8NyU-WPPz2QaombtYWxxM4kjN7_N2slyRmhFUUVxrz-MP0EOVjMiq2wHcmkY0ihUvTFb2eHH1vY-BN4IosGSncNd7fRYXGexBGwGhVv-HXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=SJPckEm9dwKlltIZ86u-nf2dq0cd0JX79JgIiErfhuLGCmhheyTDH7wD4vBhcUmhFv9QjmICTb9PY4Z3xkoEuKA3-zmbN7Etzl8UsnOC35LrjMvVkOWcgC5YHZfVeIcJQVHho4CAv_yshx1OIc8zQHQhywNAKKRHyuFiAjtzS0iHU1sxJbJOST2ZpzqAz79SaC3h2WhbxavgjW3PD_6Hqk6Y7EqyzNCdhx6u6XgQIN_Ho7Xrf91r5saM6LfLg_2s_UoXm3OP27bImgTuHZSJRHGuKAz3G1qrUd7h7Ujljf4E80lt71rSJIwyT5h8PxW5HywG97o9Y1MIm0Femn8Q9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=SJPckEm9dwKlltIZ86u-nf2dq0cd0JX79JgIiErfhuLGCmhheyTDH7wD4vBhcUmhFv9QjmICTb9PY4Z3xkoEuKA3-zmbN7Etzl8UsnOC35LrjMvVkOWcgC5YHZfVeIcJQVHho4CAv_yshx1OIc8zQHQhywNAKKRHyuFiAjtzS0iHU1sxJbJOST2ZpzqAz79SaC3h2WhbxavgjW3PD_6Hqk6Y7EqyzNCdhx6u6XgQIN_Ho7Xrf91r5saM6LfLg_2s_UoXm3OP27bImgTuHZSJRHGuKAz3G1qrUd7h7Ujljf4E80lt71rSJIwyT5h8PxW5HywG97o9Y1MIm0Femn8Q9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndKQtyEtHDriQC7B9xia-8Wvkbj_54GRM1Uz7gM7sVYdVWLmwj91Vpog0SY65TLus2-AY8gfUMwKjbAM1TLOsZMRDrl_93daFbfF5Ck0XBjkrHCbaMT8BP2K3q03G0pXI5lanbw6H3Pw_0bAiJT7XCRGN5OLQpBJvXlctNCwCNNurQsIDFUfyXjbJbzJe1Is-7UpudBMaXNaSyceyha0ruDePeR-U7E9bwkkN5sL5cdTqEPQwULJKeco4t84D06fnNnD5tgJZuHaaZ0bAADODXhAxWfPtIx17qoIcOSLbqGXEHW_s7VD8grS9bzwCu-IRRKunEnjIH4vDCga2yWq_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pym3_pIOgH98CSxwSR9Lkwae2cs6PG5nARg7E5qstw1A-BQScrpNSfET180fYLQbJZTKfaKE038uWLSsko1pL8Y9qzRHlyDHfMgFxGDpZn36IanQaezvRb2MKEb1lGt7wUJzX00nJEi9aysVoJkpPoW66pmCC1KSTcrDFbt2d2Qwiz0wPmge9u3cY7tZMYmluUwW_jvRl-QgF7lIqtuhFF12F4EIUnRN5lxhu2oqRjJcNinXO9SXj0-hFYS6aMTvU-oAts7XOLMBpUkCtfSLkCGCnaJgW1Bi2csUefKrH7fbRgqvXEPnTgZY5Ee4DoIAlJuT41lntYYcqu7xYIfMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRGYWg1eBIuPFJZRx9bXiULkbRBvEULVVEtvLIWAe6bafpX7e3vuLrjwV1tZEUtt1RmFm06WCf8ssu-HLf4MXKDgR0z0CE2E9dak9Z19cdVhIoQCE7xDAj06WklePq4hFFqWEhPklgoTdnQjdx2mSuV0VAiFkODlByZDC4EpOnyCw8cc-VwqQiKilpRPOJ2IpLwlmE4f2YlS1i0kPC2WE0knDs_p5ASw5gwefjl_FPjUNhjDAb4O8WGk5PP1c7fNNJpnT3H8sOhQPGW4heFBolVmvc1K8AYPMXeNJjyZtiO_cDU9LPfoQH1Rwa7SSf1QgQPiNiA8cflh56qGHIuY3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=RftBZ6v73FVU9EBXFDVOZjidAbNR7UMjITtpFjX4j_Ng2_RlzQUqovvRdP4XrO5x39UlB3a8bp24hEXEgrIBN_wLXxmUP2CeiqSiMVCknFyJISSsTq2u20VShrIR0KBXPY7z1JSIPPzO5P5nUmTaosMNFBm25FbQx8qn2Oxq7yKuupIrhMy5lZt8UYpSUI7FaRUslD6SEcq9C2zCbp21BmIMCPgGq33mLanGX0PYlIU590JjsFI-shhlT7V4VRzp4OpQEbRp3nAtByVzBSrJ9GoPacCLUw4TMPHiBf2HgFxxki9maa2HpLMrceQ2tqzYiqesultC8r1Lt7w5wQlnIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=RftBZ6v73FVU9EBXFDVOZjidAbNR7UMjITtpFjX4j_Ng2_RlzQUqovvRdP4XrO5x39UlB3a8bp24hEXEgrIBN_wLXxmUP2CeiqSiMVCknFyJISSsTq2u20VShrIR0KBXPY7z1JSIPPzO5P5nUmTaosMNFBm25FbQx8qn2Oxq7yKuupIrhMy5lZt8UYpSUI7FaRUslD6SEcq9C2zCbp21BmIMCPgGq33mLanGX0PYlIU590JjsFI-shhlT7V4VRzp4OpQEbRp3nAtByVzBSrJ9GoPacCLUw4TMPHiBf2HgFxxki9maa2HpLMrceQ2tqzYiqesultC8r1Lt7w5wQlnIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=ZeNqJc9eSbBHp8QEqEkBjM1gb6CC9S_oDlPPNz332nF8NAHO7n1rjnUswfnBX6TUveadJsRynxs_AugetBqOiLjPW_PQVDZVp7Ha-lwIt6GKZnvAqafjiBctWz9fFgu4vpmU1Jb0kruiAkQkVW2CjJEM9THu1rqu3RZMiUOqXSsvdmHfkTQmYujOh9ZCMaPUCRIAUJnKwPppOYAC0gLB__PKfm4fhdC2Bj70y5DfxZd275g8KuIXXNi1s_Wgc-A5yDzaAXI2ajQads-cVOcoba6fw1tiAiWpNsxI8XiDC1C7jVTp0NCc53YcIAlbG48QpSyH6wRYE9Swi7NaKAkjoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=ZeNqJc9eSbBHp8QEqEkBjM1gb6CC9S_oDlPPNz332nF8NAHO7n1rjnUswfnBX6TUveadJsRynxs_AugetBqOiLjPW_PQVDZVp7Ha-lwIt6GKZnvAqafjiBctWz9fFgu4vpmU1Jb0kruiAkQkVW2CjJEM9THu1rqu3RZMiUOqXSsvdmHfkTQmYujOh9ZCMaPUCRIAUJnKwPppOYAC0gLB__PKfm4fhdC2Bj70y5DfxZd275g8KuIXXNi1s_Wgc-A5yDzaAXI2ajQads-cVOcoba6fw1tiAiWpNsxI8XiDC1C7jVTp0NCc53YcIAlbG48QpSyH6wRYE9Swi7NaKAkjoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
