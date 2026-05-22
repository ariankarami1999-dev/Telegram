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
<img src="https://cdn4.telesco.pe/file/PkmP68KdnmaAU9ui13KRvbPDQoDFM0aD0XtqFXj3i64roOfD25hlbu1CcZGSqU8Mixrq2L9cdPYZvZjT4YqA0zLsUEXsvAVBt1rt4XRaoCGew3nrrbhoo_1NsznAUxFQ7DC8sbZ1JzNErlDIucui04Z_pOtDeOfCXfKW1ebt2_pDa9F8G6fWS_VHkiMQ00p2sh3TugDg5wbXmKUuSbnpHUfcSz_osA_kjWf6uofe0bvkfdlPqmGmncUAYCi1HiiJZZiENJUiWrC3WLXJ4d9NzL3pHxRXvL3-K_qwSrqt0U4QC7qoZrwR4ZZaifhJJL_D8COgNy5C_hzPkQBtDniBaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 941K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 19:15:28</div>
<hr>

<div class="tg-post" id="msg-121812">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وال استریت ژورنال: صادرات نفت ایران از طریق دریا به دلیل محاصره به سطح صفر کاهش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/alonews/121812" target="_blank">📅 19:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121811">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
مقامات اتحادیه اروپا اعلام کردند که اروپایی‌ها می‌توانند انتظار داشته باشند که قیمت نفت و گاز حداقل تا پایان سال ۲۰۲۷ بالاتر از قیمت قبل از جنگ باقی بماند و قیمت سایر کالاها نیز روند صعودی را دنبال می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/alonews/121811" target="_blank">📅 19:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121810">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
العربیه: اگر تفاهمی بین آمریکا و ایران حاصل شود، توافق تک صفحه‌ای به نام «بیانیه اسلام‌آباد» خواهد بود
🔴
پس از دستیابی به توافق احتمالی، مذاکرات جامعی در یک بازه زمانی مشخص انجام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/alonews/121810" target="_blank">📅 18:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121809">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9d0a89230.mp4?token=JYednKkgUEuNcRvDd3jxIoE3ON3-fvkjKVFEvymjA1ym00rBeqEFY9uGgpOaU0egyJBiT1fvfBEHVZWMyRYz9SAMhE75FfQtsdQ3ggQPp46nRAaOKKHKdwDYqJ316DuLb1y6655iodKFjgwDjP_Tba1cYN0asretTJsZLxuxQTUk7j2F5nCPYx-ON8X_2ujXS3gscTgl8UtYnjemYKeIHadqJAvhTcSxE_ElE7QPzhWNY7Jm5OVkb7b5KsEmNGoKkap98c3hrhyyCHaLqCYm_8DwQQBBA9IRWdvmZILCA44JLnLwknuuJTZatoaidG3jk7qn4Qfalovf7N3hYCtZAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9d0a89230.mp4?token=JYednKkgUEuNcRvDd3jxIoE3ON3-fvkjKVFEvymjA1ym00rBeqEFY9uGgpOaU0egyJBiT1fvfBEHVZWMyRYz9SAMhE75FfQtsdQ3ggQPp46nRAaOKKHKdwDYqJ316DuLb1y6655iodKFjgwDjP_Tba1cYN0asretTJsZLxuxQTUk7j2F5nCPYx-ON8X_2ujXS3gscTgl8UtYnjemYKeIHadqJAvhTcSxE_ElE7QPzhWNY7Jm5OVkb7b5KsEmNGoKkap98c3hrhyyCHaLqCYm_8DwQQBBA9IRWdvmZILCA44JLnLwknuuJTZatoaidG3jk7qn4Qfalovf7N3hYCtZAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم هایی از دومین دسته فایل‌های مرتبط با یوفو/یواپو نشان می‌دهد که یک جنگنده اف-۱۶ فالکون آمریکایی در تاریخ ۱۲ فوریه ۲۰۲۳ با استفاده از موشک AIM-9 سایدویندر، یک شیء ناشناس پروازی را بر فراز دریاچه هورون سرنگون کرده است.
🔴
بایدن دستور شلیک را صادر کرد و اسناد منتشر شده در نوامبر ۲۰۲۴ نشان داد که بقایای شیء دریاچه هورون بازیابی شده و آن شیء «از شرکتی بود که تجهیزات پایش آب و هوا می‌فروشد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/alonews/121809" target="_blank">📅 18:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121808">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
یک مقام ارشد پاکستانی به سی‌بی‌اس گفت که دیدارهای وزیر کشور پاکستان در تهران باعث شده مذاکرات «در مسیری مهم» پیش برود و به همین دلیل فرمانده ارتش پاکستان برای پیوستن به این تلاش‌ها راهی پایتخت ایران شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/alonews/121808" target="_blank">📅 18:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121807">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkT5LygdtTYbri52EL_JcTw0mv6O2MOsKKimlaUVI337hbE3KBqr2S5x_aM3TPGZw0ns3k-NPstxljkc8Zfxo4DMUskvlClRc2Ew_jBHf_fRhbb9IH7Jsu-tSBnZy6PWxq4SFApNoGerOus_GEKjsBLlAq1rz9AybjkmEEFTSc1LPVv0WNkbX6tS1MdJl8KBAM4ps4S-gMIn-fXQA8qpuoAigs_T6sq2biaY785jK0bG0cSSb7ylOlBOQb2IkF_2CYgASdV8ReZGJ5Hfs3tQQMDAiLWqORsVZltur4iJasdwkl66nt3PR_2hsWmQcMCWLs403XWa4fl281X54k-YOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفیر ایران در چین: چین ابتکاری چهار ماده‌ای برای صلح و ثبات در منطقه خاورمیانه ارائه داده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/alonews/121807" target="_blank">📅 18:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121806">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5f5038c4.mp4?token=BhhHzjUXLQiOS9B09A55HDo2vCmLGOz2DNwArEr9pq39EUG3MaavMUq59nxsxm-2xX7YexJbm5HHhYj6uRjm6MmGMHyqxIad9Bb74yqRhKmYWOWsHyjoZA41RJkb3qLyE-SJ26R4QKTtvOlbXmmHwxJq5ItsjLUN1NaFLTS7JYC7Z1PAhIE8grebQBHU_gKnegSOQkDKoeBbGGCBu_SCzgCGg75Dn4uDkniZUDO6Q6e0TvmRNX2wQPaEi3zoML9vCr78_tnkFg8hJOBWo--sEJS8HmJ3Wd1adXVRPyvas2lvtvsCWiDgmAi4aosPu3Wwhe_c0aUBCjvaWtdzy96hvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5f5038c4.mp4?token=BhhHzjUXLQiOS9B09A55HDo2vCmLGOz2DNwArEr9pq39EUG3MaavMUq59nxsxm-2xX7YexJbm5HHhYj6uRjm6MmGMHyqxIad9Bb74yqRhKmYWOWsHyjoZA41RJkb3qLyE-SJ26R4QKTtvOlbXmmHwxJq5ItsjLUN1NaFLTS7JYC7Z1PAhIE8grebQBHU_gKnegSOQkDKoeBbGGCBu_SCzgCGg75Dn4uDkniZUDO6Q6e0TvmRNX2wQPaEi3zoML9vCr78_tnkFg8hJOBWo--sEJS8HmJ3Wd1adXVRPyvas2lvtvsCWiDgmAi4aosPu3Wwhe_c0aUBCjvaWtdzy96hvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم منتشر شده در دومین دسته از پرونده‌های مرتبط با یوفو/یو‌ای‌پی پنتاگون، یک یو‌ای‌پی را بر فراز سوریه نشان می‌دهد که «شتاب آنی» دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/alonews/121806" target="_blank">📅 18:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121805">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
رئیس‌جمهور روسیه، ولادیمیر پوتین، به وزارت دفاع روسیه دستور داده است که پیشنهاداتی برای پاسخ به حمله اوکراین به کالج و خوابگاه در استاروبیلک ارائه دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/alonews/121805" target="_blank">📅 18:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121804">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
وزارت خارجه پاکستان روز جمعه در واکنش به گزارش برخی رسانه‌های بین‌المللی درباره سفر قریب‌الوقوع عاصم منیر، فرمانده ارتش این کشور به تهران گفت که از چنین سفری «اطلاع ندارد» اما آن را نه تأیید و نه تکذیب کرد.
🔴
طاهر اندرابی، سخنگوی وزارت خارجه پاکستان، در پاسخ به سوال خبرنگاران گفت: «در حال حاضر از هیچ سفری اطلاع ندارم. اگر قرار باشد اعلام شود، مطمئنم در زمان مناسب اعلام خواهد شد. در حال حاضر نه می‌توانم تأییدش کنم و نه تکذیب.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/alonews/121804" target="_blank">📅 18:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121801">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DOL3w8CsI-533rlj5mIXsA8a4FkXT-ApQufd8swsCCFCmMOEFLroDONHI6t1whoFu9PjEtJ_YRzc8fTLucq-TszAj1B_joH8FOcUsiXyReFLZMqYYXWmgXrTDNxOLjmQEe9RWM6l5szLD8TRe9XmlyMuQxCXoFfyhLf_51Nc6x5ygu66aQc6IWcKUghCzcpN4-gJh4parL4EBPNGm1my4SffA8YHseg4ERUsRFN3MvqATLL638TPqr6jCF7ECExAGyQHpNwQa58kKXJHCK_34q97bW0xRD4AJHXodby6QFpc7gi7riEnbADh-d0mXYLT_jZWT3Hbuil2jxYdb5IMUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HDWZ84cta2YGWtU3nbq_JOtym6jzZKWhzg5l2IHPZ6E2FR8DQfMtPLJErLWqsJgrykXzwAy2f80ioIa-KjB82P90YKT2UP3U52zhpvWLlY0h7l1Ia6LP5zq-65sLnXXCFTCyicyJm_JI82r89P52A6A73KG2PHt1MLAEeZNk4K_3I_PPGDPr1ZdU3qpJS65EMdbic7AilwuqFLz4H50lBsPxCW3H-x5ZopUhwea3YK_-SRcX8UL9hXU_7ysRN3k8un2_EnxfZw1YlTgQ0-0YUzuFRZ8nDGqtUvYNjs2LvNWV8yCAsFjSR53VMWlMAxhYtE90KVkxiudu4aDmpSwuNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71ae5b427.mp4?token=ashkBCNp-7ui6vvXRgwwa-UDT5kY1ZWDSL-3lk18IhHN9TWERAEXNaTHARClrF2PLs6-INhhMaNevQ7pKXUWa7dBhqmozEXCkMvyl6Riy0jOiYIFX290KkRDwR5baWHm_M1k9c52Dw-3JzhhxZRQRuwr5p4yDYdw611NhBUuiXpSPPpB-annNCu2fa_PCWo9S6VdoYXaLjjk3amjHYuCOy8JcDCDEPoHPz_XSwcJEViy_SohFrnEU13-7QcFA8R9UbC_nt-JBYQ1yZWieeASeeAgXMC_ISaQF2lY-qBJJdOYCAhWlhJBhbHSjSRxAvItRL8xlmo2iLu1CM0_iq4Jmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71ae5b427.mp4?token=ashkBCNp-7ui6vvXRgwwa-UDT5kY1ZWDSL-3lk18IhHN9TWERAEXNaTHARClrF2PLs6-INhhMaNevQ7pKXUWa7dBhqmozEXCkMvyl6Riy0jOiYIFX290KkRDwR5baWHm_M1k9c52Dw-3JzhhxZRQRuwr5p4yDYdw611NhBUuiXpSPPpB-annNCu2fa_PCWo9S6VdoYXaLjjk3amjHYuCOy8JcDCDEPoHPz_XSwcJEViy_SohFrnEU13-7QcFA8R9UbC_nt-JBYQ1yZWieeASeeAgXMC_ISaQF2lY-qBJJdOYCAhWlhJBhbHSjSRxAvItRL8xlmo2iLu1CM0_iq4Jmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حمله هوایی به منطقه قصر زعتر در نبطیه، جنوب لبنان انجام دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/alonews/121801" target="_blank">📅 18:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121800">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
پوتین: من از وضعیت «در میدان» آگاه هستم، مشکلات زیادی وجود دارد، همیشه در همه جا مشکلات زیادی هست.
🔴
روسیه همیشه از هر آزمایش سختی بیرون آمده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/121800" target="_blank">📅 18:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121799">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رئیس‌جمهور روسیه ولادیمیر پوتین:
می‌خواهم به نظامیان نیروهای مسلح اوکراین خطاب کنم: دستورات جنایی هیئت فاسد کیف را اجرا نکنید؛ در غیر این صورت، شما شریک جرم خواهید شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/alonews/121799" target="_blank">📅 18:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121798">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رئیس‌جمهور روسیه ولادیمیر پوتین درباره حمله اوکراین در استاروبیلک: در حال حاضر، ۶ نفر کشته شده‌اند، ۳۹ نفر زخمی شده‌اند و ۱۵ نفر مفقود شده‌اند. جستجو برای یافتن بازماندگان ادامه دارد.
🔴
تاکید می‌کنم: هیچ تأسیسات نظامی در نزدیکی خوابگاه وجود ندارد
✅
@AloNews…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/alonews/121798" target="_blank">📅 18:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121797">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f777705c.mp4?token=aoEVJxCK0pHyg0RDIt1fuN5zYHXWmiI05h670wGC9UMHz5dcJgEtVn95QQE3c1-X_tiSIly0ZYpStdUQmyraH-6XDTdQKSvr-s2E6vcbqxIeKSerI-STPEP1IH53z-XsaQnSWsKjGidU6jEgBDXS909PbPaTQVl6IYaf4u031Sc31SzqqEabujcbtyl9Tr83IBqmf529kwgCow-EgWY9ucCcUL-_7z9rE_b9BcqtBczbDVoOXmK0WSuDdZu8pERAEQIGQHq4v6P6FV90J0CvO0osEFY0vrBLpRNaiQYQdXFQEqElX5GbnxfHXTUrTXcb6iHldU7LAnqzvJPec1ntbW40vhCJn7vU65C5kLgAhNpqPL_Nxy2_KrwqN9TjxZZOdMmWQDaqTGMtTq3djGshJ_iF1M0Br7Sg1EuQraGAr2GHMsq9A7O-IVrQKLrQlmlpe-prcm49GIWm6bg5ovW24tsa8_uEqmibApZwvIpdCEBylUT13Gu5kcJFzWNesLu6IvHMhoKzqkgfOXJ3EeJn5zSkmVDSBRH2F2IxmzlwwuSduKn6Xm67M6ECcE7MMCMalTgmDRiHmhM0qmM8_B7LXBZQOXRWEJhkaVP7bf1CfwSBgX8j6OSZqNn5U10Z6k7R3-ixQvT27K_BoAoOwjfDkP02Le8UjUgUhJ0ddZjENxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f777705c.mp4?token=aoEVJxCK0pHyg0RDIt1fuN5zYHXWmiI05h670wGC9UMHz5dcJgEtVn95QQE3c1-X_tiSIly0ZYpStdUQmyraH-6XDTdQKSvr-s2E6vcbqxIeKSerI-STPEP1IH53z-XsaQnSWsKjGidU6jEgBDXS909PbPaTQVl6IYaf4u031Sc31SzqqEabujcbtyl9Tr83IBqmf529kwgCow-EgWY9ucCcUL-_7z9rE_b9BcqtBczbDVoOXmK0WSuDdZu8pERAEQIGQHq4v6P6FV90J0CvO0osEFY0vrBLpRNaiQYQdXFQEqElX5GbnxfHXTUrTXcb6iHldU7LAnqzvJPec1ntbW40vhCJn7vU65C5kLgAhNpqPL_Nxy2_KrwqN9TjxZZOdMmWQDaqTGMtTq3djGshJ_iF1M0Br7Sg1EuQraGAr2GHMsq9A7O-IVrQKLrQlmlpe-prcm49GIWm6bg5ovW24tsa8_uEqmibApZwvIpdCEBylUT13Gu5kcJFzWNesLu6IvHMhoKzqkgfOXJ3EeJn5zSkmVDSBRH2F2IxmzlwwuSduKn6Xm67M6ECcE7MMCMalTgmDRiHmhM0qmM8_B7LXBZQOXRWEJhkaVP7bf1CfwSBgX8j6OSZqNn5U10Z6k7R3-ixQvT27K_BoAoOwjfDkP02Le8UjUgUhJ0ddZjENxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور روسیه ولادیمیر پوتین درباره حمله اوکراین در استاروبیلک: در حال حاضر، ۶ نفر کشته شده‌اند، ۳۹ نفر زخمی شده‌اند و ۱۵ نفر مفقود شده‌اند. جستجو برای یافتن بازماندگان ادامه دارد.
🔴
تاکید می‌کنم: هیچ تأسیسات نظامی در نزدیکی خوابگاه وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/alonews/121797" target="_blank">📅 18:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121796">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ادعای بلومبرگ، امارات متحده عربی به عربستان و قطر پیوسته و از ترامپ خواسته به جای حمله نظامی به ایران، به دیپلماسی فرصت دهد. کشورهای حاشیه خلیج فارس نگران بی‌ثباتی منطقه و آسیب به اقتصاد خود در صورت ازسرگیری درگیری هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/alonews/121796" target="_blank">📅 18:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121795">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6bec467d.mp4?token=XXZefo_-t1J2AVxVdwK-WQPIhEb5lHl4GcF63o-KTa1AoxuHZzzugkbIWbWc-CB6g9tBgPFsYK3lmLCYerM8WCCLt72gNYCfD89I45IC8-42G9o4C7iewpyia9nIEBrE2YTht9mTiUCbX9kjKtb0_L3wNn92EXItjd4xSdR4vfsURjasQy8NLH5OGu-rJtlSqXYzKusuqfyfxF5MGAanU2k0YlB7nrXSrMI3JFo83PLOe-Yrq_nqbSLpjQbyXvb9bO7TOysxax9xvE31l6MnWwI72h_7rCTiG5EqgcUJHae32J-9UX2NNaWExecA1ExB6nJG1hrl_nTvJP0-oOEVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6bec467d.mp4?token=XXZefo_-t1J2AVxVdwK-WQPIhEb5lHl4GcF63o-KTa1AoxuHZzzugkbIWbWc-CB6g9tBgPFsYK3lmLCYerM8WCCLt72gNYCfD89I45IC8-42G9o4C7iewpyia9nIEBrE2YTht9mTiUCbX9kjKtb0_L3wNn92EXItjd4xSdR4vfsURjasQy8NLH5OGu-rJtlSqXYzKusuqfyfxF5MGAanU2k0YlB7nrXSrMI3JFo83PLOe-Yrq_nqbSLpjQbyXvb9bO7TOysxax9xvE31l6MnWwI72h_7rCTiG5EqgcUJHae32J-9UX2NNaWExecA1ExB6nJG1hrl_nTvJP0-oOEVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روت: اگر من امروز جای پوتین بودم، خیلی خوشحال نمی‌شدم.
🔴
اما باز هم، هرگز خوشحال نمی‌شدم اگر پوتین بودم — به‌ویژه در چند هفته گذشته، چون اوضاع به سمت درست پیش نمی‌رود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/alonews/121795" target="_blank">📅 17:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121794">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
نت بلاکس: قطعی اینترنت در ایران از مرز ۲۰۰۰ ساعت هم گذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/alonews/121794" target="_blank">📅 17:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121793">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0651d460f6.mp4?token=rvHU7ugFRoDeAftRFR43lkrNOtagnROW_WHS4qJTzvR1QDyzeL554cJwNn22JSBTlhz8AQMgFQ-fMArnoyKaTMADv542SQ3Df1Zf96yz5vFKrTdwCrNnvJbOi8kVCbaLOcVdg4zhEZFLYoNTqxAfPI3qXNYnJpGhhRdzbKIFb07zjvRVIQJRprI_sqXyPdDTqFQ-rsRFb7mUJu2-nCdNYQG9iBI2rORuN7VjNtjJZJzwdLUwqWj35jEeU0zKMtsrsb4sIYOP8Z6tp_aNMbuehBzIqgwwNpCpvmO5UO3QiAZ0JajgqOxhzWIZZBZNzZjib7I_UApjQfLW6ZXxzd1DhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0651d460f6.mp4?token=rvHU7ugFRoDeAftRFR43lkrNOtagnROW_WHS4qJTzvR1QDyzeL554cJwNn22JSBTlhz8AQMgFQ-fMArnoyKaTMADv542SQ3Df1Zf96yz5vFKrTdwCrNnvJbOi8kVCbaLOcVdg4zhEZFLYoNTqxAfPI3qXNYnJpGhhRdzbKIFb07zjvRVIQJRprI_sqXyPdDTqFQ-rsRFb7mUJu2-nCdNYQG9iBI2rORuN7VjNtjJZJzwdLUwqWj35jEeU0zKMtsrsb4sIYOP8Z6tp_aNMbuehBzIqgwwNpCpvmO5UO3QiAZ0JajgqOxhzWIZZBZNzZjib7I_UApjQfLW6ZXxzd1DhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیرکل ناتو مارک روت: ایالات متحده نمی‌تواند همزمان در همه جا حضور داشته باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/alonews/121793" target="_blank">📅 17:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121792">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqmzzow_AVRAOnRbb63kG8YbRsSGDan0ywbC7Rc0YI8H9DmpDmVq6pR3ug86vucck9k7rPJBhhuzezYf8ETdkdDbWLChg-hg9MUyoJtdv0IVymEm99mlreOsx0MCcrl7hVoIzFFv0-0kGUqHcVEp6jzu1eQuNyQGCkshPoW5tSD8lfwRbjiKsoxbgYTc_3xrjNfQ08rsvb6ja_1ayJ2_UO-xemW7ybDSALkMNWYLM9t4NRyI9FuLo6O0KwsqfuLP1SCyWj9VBubyEPyReiz5OQ5a2qnW8RZZy_yw9oOCMoWI6YsTemB4OVuWNHU3moNwoTJyz-Jd2byyeKHYBJka2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نورمن، خبرنگار وال استریت ژورنال : یه منبع میگه هر چیزی درباره پیش‌نویس توافقی که داره می‌چرخه، دروغه و صحت نداره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/121792" target="_blank">📅 17:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121791">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMJCN9D7kTRa4o68gEM3r-xehzpUYgIoKA1R7bUTZYRkh0aYd3rcwmRkUC1pavRTqnmVmL749O3-OMko-bjuvmTcXTA4qUglIs4vDkiUQNuomQbC26B3GM1A6CCGQFnOwJRkJedUIR-eTZVDaCGjqkHv2RKcjI2t_RMKTn5f7hb6GccCMPJYrTprmczl5DLZJ-vmcYlReG9TLeIk6YPIULkW4tSvkmQ4QVux9hsLU6c9qKqWUDVhYUH-DQn7b70CjSoTeh-98QQbvSx2W7eZ6Lk49E7Qs79JfzZzZWzcPOwrei6WvgZxjXVCIIBKO5G1cpdRpeyc1XoTphv3tRgI_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال: رکورد جدید بازار سهام!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/121791" target="_blank">📅 17:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121790">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e0bea3a3e.mp4?token=BD71f0Ms1A-aU5sEMjrbeD3ID5OwGCUhAcUdp9XTZH6c6hIbdPsFuaczpL_cqc56buKuvhZY1lxdRXqqN-UxebHxkkb64hWXw-2x4kqb7RV_d0NyppnXywLxwpjLO5nqBDVSaK6bkfok1-HlihCesfoJIQgJfbTg0mrpzyMnEyXNK40Rg-NGFbvDoBsQsdLnDPwPxVLBQpWbC_PLw_jRpemASlwYfzJIPD4uFsaPIMVVcT9F7vjvepMITPG46IxF40LlDLr3fJRT-9hEcTH6ttaaH41B9ZFrWODQ1CVzi64xn2MPCpCTZSUJx2Fw8dHzEqFEKTTAWdbL60OpodnebZM4dE9y7wkzVdOfcOMpD2zU0tc6mPlqm-iugg6SrTmyLxMNa8oRH3Gro9QMKQ38DJ0jD-YHYfLD8uDOM9ZTDd8WCl8nENASS-D8BXeWGdUpo_r3Od5-EySkpltzLm9R2zf2CwIFBajSaFKgpe6dNHbpXtcHJz3qQnOyBLz5jmmsyF2k_VaJvjPtoUHevbZVbstpO6ZORlxxeGOFoUrO7OcpTBeBfE67GT3NrX0xkT8rHEnGpx6m7mDzuBPUXUIbjiZfJttmQnrlh90V_-dH2dIFQjJ_x_WKXEDPRS8OCY2MoTfuR3kk6bOtz9U8DbMQXmG_CqjhGJC9sz8gdi5NbsE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e0bea3a3e.mp4?token=BD71f0Ms1A-aU5sEMjrbeD3ID5OwGCUhAcUdp9XTZH6c6hIbdPsFuaczpL_cqc56buKuvhZY1lxdRXqqN-UxebHxkkb64hWXw-2x4kqb7RV_d0NyppnXywLxwpjLO5nqBDVSaK6bkfok1-HlihCesfoJIQgJfbTg0mrpzyMnEyXNK40Rg-NGFbvDoBsQsdLnDPwPxVLBQpWbC_PLw_jRpemASlwYfzJIPD4uFsaPIMVVcT9F7vjvepMITPG46IxF40LlDLr3fJRT-9hEcTH6ttaaH41B9ZFrWODQ1CVzi64xn2MPCpCTZSUJx2Fw8dHzEqFEKTTAWdbL60OpodnebZM4dE9y7wkzVdOfcOMpD2zU0tc6mPlqm-iugg6SrTmyLxMNa8oRH3Gro9QMKQ38DJ0jD-YHYfLD8uDOM9ZTDd8WCl8nENASS-D8BXeWGdUpo_r3Od5-EySkpltzLm9R2zf2CwIFBajSaFKgpe6dNHbpXtcHJz3qQnOyBLz5jmmsyF2k_VaJvjPtoUHevbZVbstpO6ZORlxxeGOFoUrO7OcpTBeBfE67GT3NrX0xkT8rHEnGpx6m7mDzuBPUXUIbjiZfJttmQnrlh90V_-dH2dIFQjJ_x_WKXEDPRS8OCY2MoTfuR3kk6bOtz9U8DbMQXmG_CqjhGJC9sz8gdi5NbsE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه مارکو روبیو در مورد مذاکرات اوکراین-روسیه: ما درگیر شدیم زیرا تنها کسانی بودیم که روس‌ها و اوکراینی‌ها با آن‌ها صحبت می‌کردند. متأسفانه این گفتگوها نتیجه‌بخش نبودند.
🔴
علی‌رغم نشت‌های اطلاعاتی که حقیقت ندارند، علی‌رغم داستان‌هایی که در بیرون درباره مجبور کردن ما به اوکراینی‌ها برای اتخاذ این موضع یا آن موضع وجود دارد که حقیقت ندارند، اگر ما فرصتی برای برگزاری مذاکراتی که سازنده باشند، نه ضد سازنده، و شانس داشتن نتیجه‌بخش بودن را دارند ببینیم، آماده‌ایم که آن نقش را ایفا کنیم.
🔴
در حال حاضر چنین مذاکراتی در جریان نیست. اما ما امیدواریم که این موضوع تغییر کند، زیرا آن جنگ تنها با یک توافق مذاکره‌شده پایان خواهد یافت. این جنگ با یک پیروزی نظامی از سوی یک طرف یا طرف دیگر، حداقل از دیدگاه سنتی از نحوه تعریف پیروزی‌های نظامی، پایان نخواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/121790" target="_blank">📅 17:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121789">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
الحدث به نقل از منابع دیپلماتیک:
اگر تفاهمی بین واشنگتن و تهران حاصل شود، به صورت «توافقنامه» یک صفحه‌ای خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/alonews/121789" target="_blank">📅 17:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121788">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aebf124457.mp4?token=U1AuPFnyrehzErOr-CKkB7YWverbjDsArFTs7-9f5r4_SVp0zI6jUmu0Y9fxtstM8ESaKjlKmgcTGkT-A-uy8taPNqdRsflxAnpocfBzbtVoi8v84qxc6gOw1CBCnfVkLw0dHhGgMDh1iKizM59NAhonWomq77kyZ63T1u8vtGGMYPES2sVw3Iv5IAM91JJhvP9i5xD6UwPZ6XMsevImWFKm5kVjdvkFZqmrcxFAfCaaM_j3RAmUeIGY478C1tH-qsbm-LKHv7jXmSeel9Te50VMY4AKks5jN5Xe2N5dzb_VxeoQZKfwI_0Brg0o6DypbPdm7CSr_RwZhzQgPjxMVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aebf124457.mp4?token=U1AuPFnyrehzErOr-CKkB7YWverbjDsArFTs7-9f5r4_SVp0zI6jUmu0Y9fxtstM8ESaKjlKmgcTGkT-A-uy8taPNqdRsflxAnpocfBzbtVoi8v84qxc6gOw1CBCnfVkLw0dHhGgMDh1iKizM59NAhonWomq77kyZ63T1u8vtGGMYPES2sVw3Iv5IAM91JJhvP9i5xD6UwPZ6XMsevImWFKm5kVjdvkFZqmrcxFAfCaaM_j3RAmUeIGY478C1tH-qsbm-LKHv7jXmSeel9Te50VMY4AKks5jN5Xe2N5dzb_VxeoQZKfwI_0Brg0o6DypbPdm7CSr_RwZhzQgPjxMVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه مارکو روبیو: امروز درباره گرینلند بحث نکردیم، اما امروز جلسه‌ای با هفت کشور در مورد قطب شمال داشتیم و بسیار مثبت بود.
🔴
قطب شمال نقش برجسته‌تری در ناتو و در بحث‌های پیرامون ناتو ایفا خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/alonews/121788" target="_blank">📅 17:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121787">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
الحدث: ژنرال محمد عاصم مالک، رئیس دستگاه اطلاعات و مشاور امنیت ملی نخست‌وزیر پاکستان در راه تهران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/alonews/121787" target="_blank">📅 17:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121786">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
روبیو، وزیرخارجه آمریکا: ما در ارتباط مداوم با فیلد مارشال عاصم منیر در بالاترین سطوح دولت خود هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/121786" target="_blank">📅 17:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121785">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وال استریت ژورنال: یک توافق جامع در دسترس است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/alonews/121785" target="_blank">📅 17:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121784">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
قیمت تتر در حال ریزش شدید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/alonews/121784" target="_blank">📅 17:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121783">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
آکسیوس: پاکستان، قطر، عربستان سعودی، مصر و ترکیه همگی در میانجیگری مشارکت داشته‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/121783" target="_blank">📅 17:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121782">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری/آکسیوس:
میانجی‌های پاکستانی و قطری در حال نهایی کردن عهدنامه ای هستند که شامل توافقی برای پایان دادن به جنگ ایران و اصولی برای ۳۰ روز دیگر مذاکرات درباره توافقی گسترده‌تر است که برنامه هسته‌ای ایران را نیز در بر می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/121782" target="_blank">📅 17:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121781">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وزیر خارجه آمریکا:
در مذاکرات با ایران پیشرفت حاصل شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/121781" target="_blank">📅 17:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121780">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b116c4d535.mp4?token=AyrPSJ0US7l9fUTq7FmTjp0jJx6IshhEdnE7chEfyw7qf56-poSDyHZIBlAtOCLnIVCJa5aTZ-m2tAWGO1qpfhkJQg6Tc9z1hkf80lx9yK97cRCTxEMtNMc9UDmHcl-ofIuftKaf7wjBk_OpGzx6SsU-DVUHoK-PdnFZ-ptZ91nTdFcViDS16IUAJx51sWV0Do4nXjl2YYXtoyIxLVR2wifNNCXSv8RRTal-y8GLw5CT4s9xSsAudeFiMB8zul3yzmmSCyt5Y_6sKDsljYoD3yE7KnQ1A1ZXGXAsSYwdAFEEbcA09Db1ufdzLjLX6hgh2UW2oD9uRBJnWDcEC2xqPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b116c4d535.mp4?token=AyrPSJ0US7l9fUTq7FmTjp0jJx6IshhEdnE7chEfyw7qf56-poSDyHZIBlAtOCLnIVCJa5aTZ-m2tAWGO1qpfhkJQg6Tc9z1hkf80lx9yK97cRCTxEMtNMc9UDmHcl-ofIuftKaf7wjBk_OpGzx6SsU-DVUHoK-PdnFZ-ptZ91nTdFcViDS16IUAJx51sWV0Do4nXjl2YYXtoyIxLVR2wifNNCXSv8RRTal-y8GLw5CT4s9xSsAudeFiMB8zul3yzmmSCyt5Y_6sKDsljYoD3yE7KnQ1A1ZXGXAsSYwdAFEEbcA09Db1ufdzLjLX6hgh2UW2oD9uRBJnWDcEC2xqPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو: ایران داره تو یه آبراه بین‌المللی سیستم عوارض‌گیری راه میندازه؛
- این اصلاً قابل قبول نیست و نباید اتفاق بیفته
- اگه این تو تنگه هرمز جا بیفته، ۵ جای دیگه دنیا هم همین کارو می‌کنن
- چرا کشورهای دیگه دنیا نباید بگن ما هم می‌خوایم همین کارو بکنیم؟
- جدا از اینکه تنگه هرمز برای همه کشورهایی که اینجا هستن حیاتیه، برای خیلی از کشورهایی که اینجا هم نیستن، مخصوصاً منطقه هند-اقیانوس آرام، فوق‌العاده مهمه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/121780" target="_blank">📅 17:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121779">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0699174b2.mp4?token=KNW3ODrWrmXuqwxOOc_Gfq0rgRIbOsv64yGcqh0cMaHxByoFIj-NofCq-pjsiV_SrnGM54ukcDw3y4Se7AqlwlIVkPC1J2175pf4vVaoEppSEYoUOiUrxzoiWdVHXkncFvM30RS8Cg7GYOw4xR04o6_iZxQFyGM-wP2JHcqzMIJo01Ahqxosr7AkFLd8LT6JFh4vy4YjGsB9qOb07OYjB3A6KNxQhjpLWtSKyQb0uK4G2T5lQCeWAF0-ljiND-OhqiRezbTuEtpnyW-cgz5cJcnoP20GFjb03lC3QV7__-Xb2tRDVeBGMJgmJfnYN5Rxx5SM12P0fQGO6tHIm7kVZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0699174b2.mp4?token=KNW3ODrWrmXuqwxOOc_Gfq0rgRIbOsv64yGcqh0cMaHxByoFIj-NofCq-pjsiV_SrnGM54ukcDw3y4Se7AqlwlIVkPC1J2175pf4vVaoEppSEYoUOiUrxzoiWdVHXkncFvM30RS8Cg7GYOw4xR04o6_iZxQFyGM-wP2JHcqzMIJo01Ahqxosr7AkFLd8LT6JFh4vy4YjGsB9qOb07OYjB3A6KNxQhjpLWtSKyQb0uK4G2T5lQCeWAF0-ljiND-OhqiRezbTuEtpnyW-cgz5cJcnoP20GFjb03lC3QV7__-Xb2tRDVeBGMJgmJfnYN5Rxx5SM12P0fQGO6tHIm7kVZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو :
- تنگه هرمز کامل باز و آزاد باشه و ایران کامل قید برنامه هسته‌ای رو بزنه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/121779" target="_blank">📅 17:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121778">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgK3Tsrblk4ioqHXO8z-j_TJCohjIhadwdmrRh777x1TuJDzYlQvUty75Fqo2zItwSBrw2WyZ8-RmttcAit7MoORVAk5_30sjyOJnO_4pGwKuCfQP3PFvm5AxJWFNaC2u9ZDYyNk4OYkhuOnBP_AtfdqAbEaI0meqOvQlBSahbWScsXakcUUD98IwnhbmRVVfqfSwYAnGZwr7epG_CYqZbz74M0LRVw2BKTXs-zBvbTzro2rofwC2cLYP1voaJObvPJjT1L8FZh7G45SzrmYs91PK3qoUP-mrVvq5gZeC5p2KkguB7Wmjc6t8ofMCGtLFM9PdbWlrc4w1rnPUOnYkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید، خبرنگار آکسیوس:
عاصم منیر فرمانده ارتش پاکستان، امروز برای بستن توافق بین آمریکا و ایران و تموم کردنِ جنگ، راهی تهران میشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/121778" target="_blank">📅 16:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121777">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ادعای منبع نزدیک به مذاکرات ایران و آمریکا به «العربی الجدید»:
🔴
سفر فرمانده ارتش پاکستان
، عاصم منیر، به تهران
به این معنا نیست که توافق در دسترس است.
🔴
گزارش‌ها درباره وجود پیش‌نویس احتمالی توافق صحت ندارد و اینها صرفاً گمانه‌زنی‌های رسانه‌ای است.
🔴
وزیر کشور پاکستان پیام جدیدی از آمریکا به ایران منتقل نکرده است.
🔴
سفر مقامات پاکستانی به تهران در راستای تقویت میانجی‌گری اسلام‌آباد و نقش آن و تمایلش برای جلوگیری از تنش‌زایی است.
🔴
تهران همچنان خواسته‌های آمریکا را افراطی و غیرمنطقی می‌داند و معتقد است مشکل در واشنگتن است، نه تهران.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/121777" target="_blank">📅 16:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121776">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری/منابع عربی: یک هیئت قطری نیز هم اکنون به تهران رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/121776" target="_blank">📅 16:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121775">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWY3po0Zjw_6mvzGDdoOVSlqDBIq4Mlbt6N_z8lFUwMnqEgiZwNYuD84R_taZ8ypI8pltWLHZTThEUI6Asb43uNqX9U86UN2X-wEHfJ9Mg5QaMEH5iOMyqswAhRk4J4axJ2E9KArO3ysFm4-cBkrpGGguAauRPZ-8oA23B547IevEm3pspROKjHEOUVSKAZ8eD3e4xkRmBXMM4v0vVfN73zzJj2D7g6e6OGeD7qPKk7X0016g9dmBKw7_9s6SiqK092jCvcxAcS9Qw_UeCnulpDBVpvX5HiRBPXcsMcRZh_G8YAvk3M7kfxVetgpIQAoy-M8bT9oz3hvSd7nSQttsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه اسرائیلی i24news:
احتمالا در مذاکرات پیشرفت قابل توجهی حاصل شده باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121775" target="_blank">📅 16:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121774">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
الجزیره: شهباز شریف، نخست‌وزیر پاکستان، قصد دارد فردا به چین سفر کند. برداشت این است که
او پیام‌هایی را از تهران به پکن می‌برد
.
🔴
پاکستان در حال تعامل با بازیگران متعددی است: آمریکا، ایران، کشورهای منطقه و البته چین.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121774" target="_blank">📅 16:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121773">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
شبکه کان: رسانه‌های عربی اعلام کردند که آمدن عاصم منیر، که قوی‌ترین مرد پاکستان محسوب می‌شود، به ایران، باید نشانه‌ای از پیشرفت در مذاکرات باشد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121773" target="_blank">📅 16:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121772">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e3909efc5.mp4?token=CiqrsMxR3tDynfPO6amsq-xuGdeV1uzGxwPfTIHdv8tQumNMJLlX6SLoQgt07aU1plE88HM2ZeQLj-64PMndpbTaByiMcnRoV02_0-O2wJBs7XYN2JfVltuxanhHo5--GVZrOcFJt_ovyNVBqkSbHxKzDqnuY2E7fmDnwLwVhx2FRdQwMZr3e23aVRo-amj3zXJIHsMZTpG2Ckj4m_RtdY0KDq-ItFPkDJNqkcZfATOl3EwqSejul0aVspr1taE_zW8RZ8uAhzaYtmCxRss8Wh112dMnlp7UvQVLG-8ECRm-4NsSIHRsDjOqT7f2DjkGzVTeRpbf729a-99_OJ8XP6AZF9TXTRl_XW6afH3NbDN7sZq850Km_2VcVlpOTUCUXSYlXYO0Fwyo3CopgRlQN0imhZFoUENl5Dem4UgIsmZ9fQW8_iq1Xn0hWZ-nkWlUeWENbC7Ca1kzdlCa4_xGrdNHSrg50sW7-PcJPNr-PcpBe0NGQPLMsEtJiRMMyh4A-impJafHY_UeUm-GFuuLcMz7IkY_shesmTZvee0J52j1l3MA4L4xVjlod5krQYp1Ezb7Rysb8acXCn_vr8C1BFmVlFzlNcOypanm1aMTQSPsCrdxZtl6MqzQq9N5-JqnJnh3UC7e40udz0oL9_Af08g1P1V9gI4utWUOqHjbjzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e3909efc5.mp4?token=CiqrsMxR3tDynfPO6amsq-xuGdeV1uzGxwPfTIHdv8tQumNMJLlX6SLoQgt07aU1plE88HM2ZeQLj-64PMndpbTaByiMcnRoV02_0-O2wJBs7XYN2JfVltuxanhHo5--GVZrOcFJt_ovyNVBqkSbHxKzDqnuY2E7fmDnwLwVhx2FRdQwMZr3e23aVRo-amj3zXJIHsMZTpG2Ckj4m_RtdY0KDq-ItFPkDJNqkcZfATOl3EwqSejul0aVspr1taE_zW8RZ8uAhzaYtmCxRss8Wh112dMnlp7UvQVLG-8ECRm-4NsSIHRsDjOqT7f2DjkGzVTeRpbf729a-99_OJ8XP6AZF9TXTRl_XW6afH3NbDN7sZq850Km_2VcVlpOTUCUXSYlXYO0Fwyo3CopgRlQN0imhZFoUENl5Dem4UgIsmZ9fQW8_iq1Xn0hWZ-nkWlUeWENbC7Ca1kzdlCa4_xGrdNHSrg50sW7-PcJPNr-PcpBe0NGQPLMsEtJiRMMyh4A-impJafHY_UeUm-GFuuLcMz7IkY_shesmTZvee0J52j1l3MA4L4xVjlod5krQYp1Ezb7Rysb8acXCn_vr8C1BFmVlFzlNcOypanm1aMTQSPsCrdxZtl6MqzQq9N5-JqnJnh3UC7e40udz0oL9_Af08g1P1V9gI4utWUOqHjbjzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرستاده ویژه ترامپ به گرینلند جف لندری:گرینلند به یک توافق نیاز دارد. گرینلند می‌تواند همین الان روزانه ۲ میلیون بشکه نفت صادر کند.
🔴
فکر کنید این چه فشاری را در تنگه هرمز کاهش می‌دهد، چه اهرمی به آمریکا می‌دهد... وقت آن است که دانمارکی‌ها پای میز بیایند و بیایید یک توافق انجام دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121772" target="_blank">📅 16:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121771">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aphrgEar_Kvrs-uLkRz1rWHoe2kTlAzJWQipi8D7r_kWZ_Qli4s8-jplxfe7g3_NKyCBJ0zVkoquMjNdQYQM1cZW4N2ZmFzpdRj1icGcj-5Z3LGo4VadOZqVZeQdDJdrLl0hlI_ZoxA5z78Vb8Fa_p1HQVGnk_kWMFqCOH1MywtoEp4Ae8xmdpV6KJAi3UPcaoSqo1wdgl2ITJTMDf108guIyJPuELC-BNR1UZ_0Q-x-MWNdEEjPqif_-5MEl_qTAj3L8yhQWUz-Vx0sFADEJ0TatpeBbDc4xW8mttlIVsbs--RIrPZQakrgULfb-10c-5Twm352OyUefXFOz126uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه کان: رسانه‌های عربی اعلام کردند که آمدن عاصم منیر، که قوی‌ترین مرد پاکستان محسوب می‌شود، به ایران، باید نشانه‌ای از پیشرفت در مذاکرات باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121771" target="_blank">📅 16:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121770">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری/الحدث: عاصم منیر، فرمانده ارتش پاکستان در راه تهران است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121770" target="_blank">📅 16:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121769">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRnZjsHK5cn0phUylHCyNhjygSpoLw3M3V33magZ-fXj-KP33BETvBbtuh0JVKWQvjba1nuYs1iNqTpaagVv-U_e8HOUAeq6NnE6XrftFMc6Vr2ibNTM8I4zLYCODlWEpl-wKA078eYyK6YWTvJ1iMjRnvtO-HRgCU264L_awP11jo98IsFXwHq_uhYIacmr3NYuxL_L0a62wFdbgIEf0kTvXJNLfuHC9uENFyce2IPOzH2YZHIVu1KvWAKKqsOA4nsT-H-m87WUypiaa6dAsMStAY2GXSt5KpFJyuXDUAPX3prSflRWxGr0tVw2L4uVUcRGIRH0vS-m0vVm-WOvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه منوتو دوباره خدافظی کرد و از پایان پخش و اتمام فعالیتش خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121769" target="_blank">📅 15:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121768">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری/الحدث: عاصم منیر، فرمانده ارتش پاکستان در راه تهران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121768" target="_blank">📅 15:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121767">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
پاکستان: سفر عاصم منیر به ایران را تأیید یا تکذیب نمی‌کنیم
🔴
سخنگوی وزارت خارجه پاکستان درباره گزارش‌ها مربوط به سفر فرمانده ارتش این کشور به ایران سکوت کرد.
وی در پاسخ به پرسشی درباره سفر فیلد مارشال عاصم منیر، رئیس نیروهای دفاعی و رئیس ستاد ارتش پاکستان به ایران گفت:
🔴
ما نه می‌توانیم این گزارش‌ها را تأیید کنیم و نه رد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121767" target="_blank">📅 15:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121766">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/elo7HH1e6viYjdLK3uTiIZsWcgTIB8Pia5BMIn93dhcxgjtH013nciR8gYJDm8EK6RohuYWLrdGOqerLsN9R6MHlmf0pLsq2Jn986_yjVQeihEXAqRfrMmCl-r4h_XlyTd1tVJ3U8b7312_7opwPclELW1RkC1eSc6-yviOEp7KLBMOnomY0OJdDbGl-GT5aV9bYtx0aDgqa0DvNVcXoT-3o39G6vcGz1EvfptTttabM3JcSYXzlz9uPXtV-2-x7ixdMMLYvQr73daiKBYVGCIEMkec29t7BM5qkczNYQCwr0sIO5-3JH_CT2Uj44S564B-zREDTYBYUX8ERyL4qaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکت تلخ:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121766" target="_blank">📅 15:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121765">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
صداوسیما:
حکم قالیباف رئیس هیئت مذاکره کننده
🔴
اسماعیل بقایی سخنگوی وزارت خارجه، سخنگوی هیئت مذاکراتی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121765" target="_blank">📅 15:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121764">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rzm9h27xNNij-dSCIJ94WTSyR4ADj8hO7cqd7cu1KXSvW_qvxBF8p5Ecu-J82qrmIxaoVge0UJx7WN9HHZGWrztbhR7SnGxiK8dOqgeV_ztoIlGMLH1bmrsfaOqztMmnv2_xu2Lk0Ip5XnWMVhJKErprhWU75odqmQP4lMPoadOt0F0padZpflHdISaTxsyu8Wpr4rPKR6HatRJctQdzlKL-gqSqRS2dPoZCc-fo2NcE4HQA4gAkq4euW4drmh80XtP1OYhU7ajChJnQ-A0wsfdZ5rUpy6lEOYicP-XV0Zbv3TLSSQgeWr2_ZzzmDn3nzdjbxQ9R8EIzb2fgA_KvqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ شب فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121764" target="_blank">📅 15:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121763">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e9244fd77.mp4?token=QhvjILqjcDlRUB61vzCbE6T75oiRCR5yerAVEuaLp7cAqhvpWXvS1r8eyRFlq5b_Li5kIhAcMg_rHnvTB6qz_IsOsn5C4UsQsvfgzDX40VjoVdKANmV2J7KSJ_pu6bJppV6K2f4jAnift83GyprTUke7yYCLp0VGtd6IPp28jCUkwOvHciKM0l0EoSZjQFCK0YgZ7yXcB73Ks3-ZVxTqZzcUdMbZRo37kpt1MzNbmesoOcaXZnesXo0w6-PJLwJZ_bo7eZ_cIiQVI91XnfWsrFTDMPLCrBw0sD4jLqLfKFzbiUsVKAIQj4-EUEmLF0v-tivrEgymvxCKC_vPOfgwlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e9244fd77.mp4?token=QhvjILqjcDlRUB61vzCbE6T75oiRCR5yerAVEuaLp7cAqhvpWXvS1r8eyRFlq5b_Li5kIhAcMg_rHnvTB6qz_IsOsn5C4UsQsvfgzDX40VjoVdKANmV2J7KSJ_pu6bJppV6K2f4jAnift83GyprTUke7yYCLp0VGtd6IPp28jCUkwOvHciKM0l0EoSZjQFCK0YgZ7yXcB73Ks3-ZVxTqZzcUdMbZRo37kpt1MzNbmesoOcaXZnesXo0w6-PJLwJZ_bo7eZ_cIiQVI91XnfWsrFTDMPLCrBw0sD4jLqLfKFzbiUsVKAIQj4-EUEmLF0v-tivrEgymvxCKC_vPOfgwlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعال آلمانی حاضر در ناوگان «صمود»:
در زمان بازداشت هر روز من را کتک میزدند و آب و غذا نمیدادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121763" target="_blank">📅 15:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121762">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeC6B1IVR_HMSnpPhhcpz-ED0ySOV5pL1dLdrDw6LwQziLA_xTlKBl71sXLfYmGWvhfpszJVXYElzraOjAM2u0MwW6-gayEW51Etiq9BssvngaFtR8IS_diDijXnAOzo6FrDfQt3KGfkZJRs-tfKJxsI-C30pbfLJYFb-18JIec9XxHvhCW1rX1tIQHNHiXexCDj7ubzHdJ4sn6gdc17Jh6RRGIsu1fL1sonOkcTZnlaL-E2R2HNPfOd5a1bNMBNcOltrXMB1V70rK6LJcpqigDxjWHMSae_v3TgPPOFuuuVku_Sh2Qp-H7BzBcdDAXPsDF2aGRpTONfeltJKhZa5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ پس از اطلاع از لغو برنامه چرخش نیروها به لهستان توسط پنتاگون، از وزیر جنگ پیت هگستث سوال کرد، طبق گزارش WSJ.
🔴
ترامپ در تماس اخیر به هگستث گفت که ایالات متحده نباید به لهستان به دلیل رابطه نزدیکش با کاخ سفید بدرفتاری کند.
🔴
این اقدام برخی مقامات را شگفت‌زده کرد زیرا این آلمان بود، نه لهستان، که رویکرد آمریکا در جنگ با ایران را نقد کرده بود.
🔴
کمی بعد، ترامپ برنامه‌هایی برای اعزام ۵۰۰۰ نیروی اضافی آمریکایی به لهستان اعلام کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/121762" target="_blank">📅 15:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121761">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وال‌استریت ژورنال: ترامپ شخصا خواستار اعزام نیروهای بیشتر به لهستان شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/121761" target="_blank">📅 15:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121760">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری / فاکس نیوز: مذاکرات بین ایالات متحده و ایران همچنان در جریان است، با نشانه‌هایی از خوش‌بینی محتاطانه که هر دو طرف ممکن است در نهایت به توافق برسند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121760" target="_blank">📅 15:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121759">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaAQ423A_uu4DX4yXNEtwc5YKo71WZQUqJSSXt1-Xz2ikvb-WTjealrvKOFSRVsaohe0nLlX5uM1MRHVMYRQ6HB6H_ZWkYZNO_jqOPs22Qfpfyl_aO5Y872Ud5q_8LcAccrdZJOOrc2wE00IFxCvCxJ00dchl7kuhSyy2fvTRfV0f9pjaF6RqUYLi0jUAGNx8YEhpSopvwnqU4vDLBiURaNEJEi2xNo4M9Q2wajfV5Sx4dWMaU02J_ONQCUGviI13Z7AJ6-pIXcACkiF8ZU_FxDek6t4HuMtkv1fNkS_8CRspXgz4FBOkuH_qvJLoB4LhUSIhSvY2-SBnDclLpxWZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بحرین، کویت، قطر، عربستان و امارات تو یه بیانیه مشترک گفتن کنترل ایران روی تنگه هرمز رو قبول نداریم
🔴
محکومش میکنیم و از کشتی‌ها میخوایم با «سازمان تنگه خلیج فارس» تماس نگیرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121759" target="_blank">📅 15:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121758">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c194f6c50.mp4?token=iZ_CyOKpv-1t04To2x50tyoC1cGXbYVFtpMpUT6AduHqqOdMpQ0MxaXdd4iVBHNAYYO2B6vIHr3XJCdgdR8Me-z1LlRzpBDVOrz6wNVtKhp8iUrpljf0O3s2UjGXFmMn7bcS4SDKkt6HkiUo6sjRXWtOIDz9VFNzci3DpCdtj0y2kiJwyF_eiZWOCN5QVc-JzU82hV3waEzi8a448-4xVRFIQ5x_wr57UTtqp85m3OLzDHES9JrkaTRiHMnKYzBZdo52cgpZ3HJHlt3ER_z4E2tRGdxjRp3cI0D2GgUd9nECPr190kpGlPpQjR8NbG4wYug4iLhTunLOcxNZquNrKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c194f6c50.mp4?token=iZ_CyOKpv-1t04To2x50tyoC1cGXbYVFtpMpUT6AduHqqOdMpQ0MxaXdd4iVBHNAYYO2B6vIHr3XJCdgdR8Me-z1LlRzpBDVOrz6wNVtKhp8iUrpljf0O3s2UjGXFmMn7bcS4SDKkt6HkiUo6sjRXWtOIDz9VFNzci3DpCdtj0y2kiJwyF_eiZWOCN5QVc-JzU82hV3waEzi8a448-4xVRFIQ5x_wr57UTtqp85m3OLzDHES9JrkaTRiHMnKYzBZdo52cgpZ3HJHlt3ER_z4E2tRGdxjRp3cI0D2GgUd9nECPr190kpGlPpQjR8NbG4wYug4iLhTunLOcxNZquNrKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل اعلام کرد دیروز تیپ ۵۵۱ که تحت فرماندهی لشکر ۱۴۶ در جنوب لبنان فعالیت می‌کند، پنج مبارز حزب‌الله را که وارد ساختمانی در شهر منصوری شده بودند، شناسایی کرد.
🔴
این مبارزان سپس توسط حملات هوایی اسرائیل کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121758" target="_blank">📅 14:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121757">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
حسنعلی امیری عضو مجلس: طرح جایزه برای کشتن ترامپ در حال تصویبه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121757" target="_blank">📅 14:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121756">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
بلومبرگ: تداوم مسدودی هرمز، رکودی مشابه بحران ۲۰۰۸ را ممکن است ایجاد کند
🔴
تنش بین ترامپ و ایران بر سر ذخایر اورانیوم و تنگه هرمز پیامدهای خطرناکی ایجاد کرده است. این پیامدها شامل قیمت نفت می شود و خطر رکودی مشابه رکود ۲۰۰۸ را تهدید می کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121756" target="_blank">📅 14:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121755">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
امیرحسین ثابتی: دور جدید جنگ در پیش است؛ شاید هم شروع حمله از سوی ایران باشد
🔴
گر از همین فردا بخواهیم به دشمن حمله کنیم و در حین جنگ نیز هیچ موشک و پهپاد جدیدی نسازیم، تا دو سال به صورت شبانه روز میتوانیم آنها را بمباران کنیم و هیچ مشکلی از این جهت وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121755" target="_blank">📅 14:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121754">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
حملات هوایی اسرائیل به دیر قانون النهر در جنوب لبنان شش نفر را کشت، از جمله دو امدادگر و یک دختر، در حالی که شش نفر دیگر زخمی شدند که در میان آنها سه امدادگر و یک زن بودند، طبق گزارش خبرگزاری ملی لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121754" target="_blank">📅 14:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121753">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وریر خارجه انگلیس: از مذاکراتی که ایالات متحده در حال حاضر با ایران انجام می‌دهد، حمایت می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/121753" target="_blank">📅 14:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121752">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
اتحادیه اروپا : به خاطر بستن تنگه هرمز توسط ایران، یه بسته تحریمی جدید علیه تهران اعمال کردیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/121752" target="_blank">📅 14:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121751">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
دانشگاه پیام نور از تصمیم قبلی خود برای برگزاری آزمون‌های حضوری عقب‌نشینی و اعلام کرد: آزمون‌های نیم‌سال جاری (سال ۱۴۰۵) به صورت غیرحضوری برگزار خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121751" target="_blank">📅 14:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121750">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس: جمهوری اسلامی در خصوص خروج اورانیوم از ایران هیچ مصالحه‌ای انجام نخواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121750" target="_blank">📅 14:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121749">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gue9Z-7iFJjYdpex2cDQJzA1x9LRdGnvmfX0hlaCo4Kc_ezrGG9HpNPBf8DHIhX5c3Ay9EpPPe0i307wjWBs7yq-DWiylOFC3dnCCA1rpi8B8pTd8nBoIbA5IK4sD5uiAcrkAdYSTqn2Vjt-MUAvbahqqe1cFDSJpbEE1qHfFGxR54XnI4yQlCldC-gtrjLysp-yt-Z7IEKhNbExcrznhfZGxZWId-iymRbWXfiwWh5YoYAcOwcf_ZQqPDfNkpjmdb8OQuDFxS3aDILjDxm1ffsXUDSc9TnQQncr5su5kPn9G-BDAn-LetPHxPAaLN_52x82HgsuZ87ELAA4Bqv8Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social: کولبرت بالاخره در CBS تمام شد. شگفت‌آور است که این همه دوام آورد! هیچ استعدادی، هیچ رتبه‌ای، هیچ زندگی‌ای نداشت. او مثل یک مرده بود.
🔴
می‌توانستید هر کسی را از خیابان بردارید و بهتر از این آدم بی‌ادب باشد. خدا را شکر که بالاخره رفت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121749" target="_blank">📅 14:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121748">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029e0d7a1d.mp4?token=qa_kLSrAzdOfp6hBcMXnCZfqxJck11-5AtrHmmy9kF5n1nZ0kCajOCSdSX-96htNk-BZtQl6GyDF2AXSKzvBpYXpox2cn-VgWQpwMVt8Xrs3QN50Uir7QSsFKnQqJpcfVhH0mDYyFiOoL_LeB_nAlfcfz0Zpk1-si46tt9mT7tOxE31h9EbOEoZCDxx6j4W4saqmkr0wvNRIqQi25mmUFJ3qbyf7OuFiDK1TFEyEYZeP5B1xJON9ReC5hgJaMNhgOt0Tfz5byL5kKCsoqHUTroX7G-KT384_g_hFKQVvvNUxuYAo6gaRDb5NPc6k0HGPXmrlh9xqkm_W9hpQASXuBlcNCth-gRPGZ6kcmg6vGBbX1aeJTdzx6UiG3TursSOAK4JeNKG1zFVSZZJwsTJAI_hPRfnxAPquwc7zT-qCSyXa0BIdiGhZO3TENIwK-qId1haXzgMbl1T5sb0gd6AK7LruqcskOuWXbDA1MPUjuuiz7La_PLUq4bZjxaJGgmpQYmf2cPiuO1U8Zex_srbGRAeeVNDJgl1LWntuSaVQfORyAnPNK9bZwD_DrTxJBkcyuFK9Mxio3zThJijbDLqLHNDOVzHn6QrWOICLeq5NtLUMKLpQk5ZxBpxp7klkzpBTJdUdnNGLpO4pBjq2RYntQZ4XLWSwvuFaskAbWz3Gch0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029e0d7a1d.mp4?token=qa_kLSrAzdOfp6hBcMXnCZfqxJck11-5AtrHmmy9kF5n1nZ0kCajOCSdSX-96htNk-BZtQl6GyDF2AXSKzvBpYXpox2cn-VgWQpwMVt8Xrs3QN50Uir7QSsFKnQqJpcfVhH0mDYyFiOoL_LeB_nAlfcfz0Zpk1-si46tt9mT7tOxE31h9EbOEoZCDxx6j4W4saqmkr0wvNRIqQi25mmUFJ3qbyf7OuFiDK1TFEyEYZeP5B1xJON9ReC5hgJaMNhgOt0Tfz5byL5kKCsoqHUTroX7G-KT384_g_hFKQVvvNUxuYAo6gaRDb5NPc6k0HGPXmrlh9xqkm_W9hpQASXuBlcNCth-gRPGZ6kcmg6vGBbX1aeJTdzx6UiG3TursSOAK4JeNKG1zFVSZZJwsTJAI_hPRfnxAPquwc7zT-qCSyXa0BIdiGhZO3TENIwK-qId1haXzgMbl1T5sb0gd6AK7LruqcskOuWXbDA1MPUjuuiz7La_PLUq4bZjxaJGgmpQYmf2cPiuO1U8Zex_srbGRAeeVNDJgl1LWntuSaVQfORyAnPNK9bZwD_DrTxJBkcyuFK9Mxio3zThJijbDLqLHNDOVzHn6QrWOICLeq5NtLUMKLpQk5ZxBpxp7klkzpBTJdUdnNGLpO4pBjq2RYntQZ4XLWSwvuFaskAbWz3Gch0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از آخرین وضعیت تنگهٔ هرمز و کنترل آن توسط ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121748" target="_blank">📅 14:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121747">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
طبق داده‌های دولتی ژاپن، صادرات خودروهای ژاپنی به خاورمیانه در آوریل به دلیل اختلال در مسیرهای کشتیرانی ناشی از جنگ علیه ایران، بیش از ۹۰ درصد کاهش یافته و تقریباً به صفر رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121747" target="_blank">📅 14:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121746">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
اتحادیه اروپا : به خاطر بستن تنگه هرمز توسط ایران، یه بسته تحریمی جدید علیه تهران اعمال کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/121746" target="_blank">📅 14:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121745">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
روبیو: برخی از واکنش‌های متحدان ناتو ما به عملیات‌های ما در خاورمیانه به خوبی مستند شده‌اند و باید به آنها رسیدگی شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121745" target="_blank">📅 13:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121744">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc6f8a0346.mp4?token=NweTeTHopUVZdOSMi_aqPY2d_DgH_ExXdRpJcBRLtg9XAykcxOkKSLIO3JSUn_eqISve_Tt3dHCl454ov1S2p0Mw2j_BK4YmvpZjvAxq7bu9ZtOP1xWWJ9ITP03eNP8_Dx4YC9LBp2r1IhwIIxefnkZWnGgKcUjgBYgzIaDQqe1ogLZmlHfVixSAWGenXIkJixZgIQna0Vf-hemBu4vLyh1j-x6jRzzfmnAoxeQv4OUII0nymwRzFxVOFoBDGkSzEYliPnX4BSRwJCmNNdgok7A1ErCFedycyiR6ChpUZsWRYLYpkqAGGhL6eBfwddS4oq_nqjb7WGfGLL6e4q3z3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc6f8a0346.mp4?token=NweTeTHopUVZdOSMi_aqPY2d_DgH_ExXdRpJcBRLtg9XAykcxOkKSLIO3JSUn_eqISve_Tt3dHCl454ov1S2p0Mw2j_BK4YmvpZjvAxq7bu9ZtOP1xWWJ9ITP03eNP8_Dx4YC9LBp2r1IhwIIxefnkZWnGgKcUjgBYgzIaDQqe1ogLZmlHfVixSAWGenXIkJixZgIQna0Vf-hemBu4vLyh1j-x6jRzzfmnAoxeQv4OUII0nymwRzFxVOFoBDGkSzEYliPnX4BSRwJCmNNdgok7A1ErCFedycyiR6ChpUZsWRYLYpkqAGGhL6eBfwddS4oq_nqjb7WGfGLL6e4q3z3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه ویدیو از خرابی‌های بعد حمله‌ ارتش اسرائیل به لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/121744" target="_blank">📅 13:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121743">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سی‌ان‌ان: آمریکا نگران موشک‌های کروز ساحلی ایران است، زیرا این موشک‌ها می‌توانند کشتی‌رانی در تنگه هرمز را تهدید کنند؛ ارزیابی‌های اطلاعاتی نشان می‌دهد که حدود دو سوم لانچرهای موشکی و بخش بزرگی از موشک‌های کروز ساحلی ایران همچنان فعال هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121743" target="_blank">📅 13:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121742">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
اسلام‌آباد به شدت روی چین حساب باز کرده است تا به پیشبرد توافق احتمالی آمریکا و ایران کمک کند، و انتظار می‌رود نخست‌وزیر پاکستان، شہباز شریف، در مرحله‌ای بعدی به چین سفر کند، طبق گزارش العربیه که به منبعی پاکستانی استناد می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/121742" target="_blank">📅 13:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121741">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وزیر نیرو: با وجود بارش‌های خوب امسال، استان مرکزی و استان تهران در وضعیت ضعیف آب قرار دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121741" target="_blank">📅 13:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121740">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
الحدث به نقل از یک منبع پاکستانی:
هیچ جایگزینی برای توافق موقت بین واشنگتن و تهران وجود ندارد
🔴
کاهش فاصله‌ها آسان نیست زیرا هر طرف سقف بالایی از خواسته‌ها دارد
🔴
مسائل بزرگ در توافق به بازه زمانی طولانی در مذاکره نیاز دارند
🔴
آمریکا و ایران بر مواضع خود درباره اورانیوم پایبند هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/121740" target="_blank">📅 13:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121739">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbeee07e55.mp4?token=ISDDhwiWZWm-S95QNd0N076ODS3iMxm-9uFcftBssMV2lpTMKJ-aCeBbGjUr0_K9_E_UeECUKB77hxsN_saSMh_A5MiLC9JkqmSJLgEGsFoJAhVn2L2evQqvay7H6ZOCeceTIyAigsAZHxV4TiTWr550_FmyCuxPMeriiZEWMwKIAVL9k_sK9MsjlYRG1CcZybHmzFs7bGIe569U2fpECiAswA1CSGjMY3wvkZ1_WvyklQ_Me3r1L7nyR9MZHydnXufUxlwN8FqDWYrGS388FtOhjX0BYn1R7HQvhXtGNLyNva5iu_piZRqKfyHwgeoABCp2QQAcdRFRah9Go7JvoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbeee07e55.mp4?token=ISDDhwiWZWm-S95QNd0N076ODS3iMxm-9uFcftBssMV2lpTMKJ-aCeBbGjUr0_K9_E_UeECUKB77hxsN_saSMh_A5MiLC9JkqmSJLgEGsFoJAhVn2L2evQqvay7H6ZOCeceTIyAigsAZHxV4TiTWr550_FmyCuxPMeriiZEWMwKIAVL9k_sK9MsjlYRG1CcZybHmzFs7bGIe569U2fpECiAswA1CSGjMY3wvkZ1_WvyklQ_Me3r1L7nyR9MZHydnXufUxlwN8FqDWYrGS388FtOhjX0BYn1R7HQvhXtGNLyNva5iu_piZRqKfyHwgeoABCp2QQAcdRFRah9Go7JvoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: "درحال حاضر، در سازمان ملل متحد، قطعنامه‌ای داریم که توسط بحرین ارائه شده است. ما بسیار درگیر آن بوده‌ایم. این قطعنامه بالاترین تعداد همکاران ارائه‌دهنده را در تاریخ هر قطعنامه‌ای در شورای امنیت داشته است. متأسفانه، چند کشور در شورای امنیت به وتوی آن فکر می‌کنند که این امر تأسف‌بار خواهد بود."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/121739" target="_blank">📅 13:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121738">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نیروی دریایی سپاه: طی شبانه روز گذشته ۳۵ فروند کشتی اعم از نفتکش، کانتینربر و سایر کشتی های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121738" target="_blank">📅 13:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121737">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
عربستان: با هرگونه تلاش برای سیاسی‌کردن حج با قاطعیت برخورد می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/121737" target="_blank">📅 13:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121736">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c641e7ef.mp4?token=bQBTpiE3OrQo57UzipZ5SK_NKZHa25hDIhWUKQAP_CKU3fU9ft-o12Gkm1DZF7AjhWpxBpGaHoj9-Bzmfvy-3szcgqwCk_MYYh-Td5SLVFNiH4tG6DqRJScxEdi3zTS_F5sj2EREVQud_pKnPNHl9iGJ3hM_Z3OPbVqzXKtbdKy8bUiJ_jg_kXPP-R-iLXNDpMnh1HVS7b0rcLRBO0ft7rVlAysIDqFVamCrNzVnE__fic8StLaxRy2AFtpLJuRZYMz6t1rXgOxCkEy7ESPCHurqz4qmgLhx5_fVJWb-aKel__JqrklTkjvIMF6GxMBd1z3gpDTnFFeuap14jQr47Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c641e7ef.mp4?token=bQBTpiE3OrQo57UzipZ5SK_NKZHa25hDIhWUKQAP_CKU3fU9ft-o12Gkm1DZF7AjhWpxBpGaHoj9-Bzmfvy-3szcgqwCk_MYYh-Td5SLVFNiH4tG6DqRJScxEdi3zTS_F5sj2EREVQud_pKnPNHl9iGJ3hM_Z3OPbVqzXKtbdKy8bUiJ_jg_kXPP-R-iLXNDpMnh1HVS7b0rcLRBO0ft7rVlAysIDqFVamCrNzVnE__fic8StLaxRy2AFtpLJuRZYMz6t1rXgOxCkEy7ESPCHurqz4qmgLhx5_fVJWb-aKel__JqrklTkjvIMF6GxMBd1z3gpDTnFFeuap14jQr47Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو :  اینکه آمریکا داره توان هسته‌ای و موشک‌های دوربرد ایران رو تضعیف می‌کنه
🔴
برای خاورمیانه، اروپا و کل دنیا خیلی مهمه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/121736" target="_blank">📅 13:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121735">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
انور قرقاش، مشاور رئیس امارات: دور دیگری از درگیری میان آمریکا و ایران فقط مسائل را پیچیده‌تر خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/121735" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121734">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
زلنسکی : یه پالایشگاه نفت روسیه تو یاروسلاول رو زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121734" target="_blank">📅 12:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121733">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CShAIR_hgOfAssz3ywOuayPFyCuvE5Ig9--1U-m8rDiQwkAY80zpOzizGMXVrtWlT3au_pjptggs6M6qiCfuKHIclZOoUlTU3JZ9EQ17kZoyAynG9aUjpKyjs9hVMMkxsqva4EupJZAwAajBNF1ikp48S-KaTEiXIyJQN0MsV5sIJHd61nHdi2PSE_byim7oxbEetsUU4e9DYcZ8RF3I19RtJVuI4FV4DtzLy3OztVGL33R5WOBIbtLhjl9_3s3Za_OC3AwJ7QDT8_WVnLzqp0_Gdgbie1gJwFiE7Emj8HZf4leRH2bIj4RZvOHvNGsZD2MtlIbgDu-gIzr1paQw2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای فارن افرز:
«رهبران خلیج فارس از قبل، شروع به تنوع بخشیدن به تأمین‌کنندگان سلاح و مشارکت‌های امنیتی خود کرده‌اند.
🔴
برای اینکه بتوانند در مورد آنچه برایشان اتفاق می‌افتد، حرف بیشتری برای گفتن داشته باشند، باید هماهنگی بهتری بین خود، چه از نظر نظامی و چه از نظر دیپلماتیک، برقرار کنند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/121733" target="_blank">📅 12:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121731">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQlio8AMeR_zeG0Oa3IWFmL4MiQF4c3Vq85c1aZm47gHY1_CFr91MgWEXJO9VWvK1D_Mpy46cs7Mej2g_yRVNq6cOaOym2hEkm7JkjTbIDN79IjnoK-N0SfKObc1K8D87wORoNxhJnl1pB_6whCRlY75FD9PdF0CtA6rvyjNnDxTydlsWhQjWkShAUcbtghJiuBaJctFPPYDGdguLCGEUbazVi_5Fk5d5mFDL05PRb7RkOjRqNv3yePOP6oxoPWnb8vxhxl5aWsnDAyWVtJDwXEGlWyUgqvpxE9UhtLSN8C5TXReju-qvQY2Sd-zLL5FdTJSQ3A2aiBuOsEcmac7WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ox6IHJQ23zDG18BqkgavFxXKVxziS4eBxfdyoJr665vBsGxgLpfTYpMncXy6UAMueOlP7xOOEueNikvXGBZkgdN7DuiYShqI8D5OIS-d5E2yjh5s76mcZJ1IzgPj3bHC1X6ANz81qlqrE49GhPje9HdTQZ0wXoBZ-P9f-dgNS1YUAkM94JMYf6g2yUuglcvAvB-tt1bjBOXNGaeBcpmNOUF2cuyEyv2i8TIoS1QqHk3JQyR_AUIyzm5z_ctXdAVrhAWS6ctOgDRIw0QUTV3nqgOoHMMau1JZ-_Rwtrvx0Z445kFXxELSEvL273touOxJyOTRihHDv74XNzkbYS4wsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارتش اسرائیل به "میفدون" لبنان حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121731" target="_blank">📅 12:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121730">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
تلگراف: قرار بود ترامپ با اتخاذ موضعی سختگیرانه‌ تر در قبال چین به پیشرفت هند کمک کند.
🔴
در عوض، جنگ‌ها و غیرقابل‌پیش‌بینی بودن او به جاه‌طلبی‌های نارندرا مودی برای تبدیل هند به یک ابرقدرت جهانی آسیب می‌رساند.
🔴
درگیری در ایران به هند ضربه سختی وارد کرده است. این کشور به نفت وارداتی متکی است که بخش عمده آن از طریق تنگه هرمز وارد می‌شود، بنابراین افزایش قیمت انرژی باعث تضعیف رشد، افزایش تورم و ترساندن سرمایه‌گذاران می‌شود.
🔴
مودیز در حال حاضر پیش‌بینی رشد هند را به ۶ درصد کاهش داده است - بسیار کمتر از ۸ درصدی که مودی می‌گوید برای تبدیل هند به یک کشور توسعه‌یافته تا سال ۲۰۴۷ لازم است.
🔴
در عین حال، ترامپ به چین و پاکستان، دو رقیب اصلی هند، نزدیک‌تر شده است و سال‌ها تلاش مودی برای ایجاد روابط قوی‌تر با واشنگتن را تضعیف می‌کند.
🔴
مودی اکنون در تلاش است تا با جستجوی قراردادهای جدید انرژی در خارج از کشور، کاهش فشارهای هزینه‌ای در داخل و حتی منصرف کردن هندی‌ها از خرید طلا و سفر به خارج از کشور، آسیب‌ها را محدود کند.
🔴
این بحران مشکل عمیق‌تری را آشکار کرده است: با وجود رشد سریع، هند هنوز فاقد قدرت تولید، زیرساخت‌ها و نفوذ اقتصادی لازم برای رقابت با چین است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121730" target="_blank">📅 12:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121729">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا مدعی شد که فکر نمی‌کنم هیچ کشوری موافقت کند که برای عبور از تنگه هرمز هزینه پرداخت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121729" target="_blank">📅 12:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121728">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ادعای وزیر امور خارجه بریتانیا: ما با عزم ایالات متحده برای بازگشایی تنگه هرمز به روی کشتیرانی موافقیم
🔴
شرم‌آور است که ایران با مسدود کردن کشتیرانی بین‌المللی سعی در ربودن کل اقتصاد جهانی دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121728" target="_blank">📅 12:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121727">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4b97475f3.mp4?token=HXXzPLnuA7D3yhJEfNHD2o6RQS7QEPuz281Ohkp9JUaPstM8I0hK5AdW6dcUpePLSM1SRqIVpnQ329okPR8UskoYgDbqPQy3WcgGoeoZxnFOUDta1Y30zfsBY5OG7L6yk5EjdXa-QQVsYlRGdsTd5OULOf-REGXyAhLT5TC__jBa6oILqhPoYnBL43uzxgfFj0wICRkaWJOdpYcD8FhlNeFJtjFVTu93TgIGgSVbaBzbSBpzbVNRSsMEfmZjj0AJ5cF1N143B-Dy94Mkunrq3cZdaA15-TmzQZs6O20XRmCdo4Z5cLmKO4LjQ62V8bK5iNJWONBUcKhZKmp3nIu-UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4b97475f3.mp4?token=HXXzPLnuA7D3yhJEfNHD2o6RQS7QEPuz281Ohkp9JUaPstM8I0hK5AdW6dcUpePLSM1SRqIVpnQ329okPR8UskoYgDbqPQy3WcgGoeoZxnFOUDta1Y30zfsBY5OG7L6yk5EjdXa-QQVsYlRGdsTd5OULOf-REGXyAhLT5TC__jBa6oILqhPoYnBL43uzxgfFj0wICRkaWJOdpYcD8FhlNeFJtjFVTu93TgIGgSVbaBzbSBpzbVNRSsMEfmZjj0AJ5cF1N143B-Dy94Mkunrq3cZdaA15-TmzQZs6O20XRmCdo4Z5cLmKO4LjQ62V8bK5iNJWONBUcKhZKmp3nIu-UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو می‌گوید تصمیمات در مورد نیروهای نظامی ایالات متحده در اروپا «تنبیهی» نیستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121727" target="_blank">📅 12:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121726">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ادعای منبع پاکستانی به الجزیره: اصرار آمریکا و ایران بر بالا بردن سقف خواسته‌هایشان درباره اورانیوم و تنگه هرمز، به بن‌بست در مذاکرات انجامیده
🔴
اسلام‌آباد همچنان نسبت به امکان دستیابی به یک توافق موقت بین واشنگتن و تهران خوش‌بین است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/121726" target="_blank">📅 12:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121725">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: نخست‌وزیر پاکستان در سفر فردای خود به چین درباره ابتکاری مشترک برای پایان دادن به جنگ گفت‌وگو خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121725" target="_blank">📅 12:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121724">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزیر امور خارجه آلمان: ما در حال آماده شدن برای مشارکت در تأمین امنیت تنگه هرمز تحت رهبری بریتانیا هستیم، اما انتظار ماموریتی مشابه ناتو را ندارم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/121724" target="_blank">📅 12:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121723">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / وزیر امور خارجه آمریکا: در مذاکرات با ایران پیشرفت‌هایی حاصل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/121723" target="_blank">📅 11:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121722">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
رویترز: وقتی که ترامپ گفت «تمدن ایران امشب خواهد مرد» مقامات آسیایی و اروپایی نگران بمباران اتمی ایران شدند که می‌توانست منجر به تشدید تنش هسته‌ای در اوکراین نیز بشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/121722" target="_blank">📅 11:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121721">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0874c8216.mp4?token=SKhbo05ucEzgif-PB2sftCXRRKHd9Umb7MMmsjjub9AQ2RDTwgVeIuP5aSaQ-y51DBAYSLMqdcQMSfToElHJAj_8_1chqi1-IP1PC11JN1P-dckf8FTgANMxEIQ4UExv07vEtVe8BI1AS8nLDhxou-rU0UYbZ5G03qpJgA8tiYsuo7Y9J3MTwu2EHy4641ylXmiDeNIP3aEdCDnnDclypGagUZX1ZIE7nCxlm2zNu5KAR7rfgBz4weFo6-tTgmw6Gg1qeY9sLOB2uoIaxV91mQjxfMT26jnqLkLbucdNMGIUPn6EszZIHbRb_UasAZKKT0Sg1gWmCC_JZlj--fhc_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0874c8216.mp4?token=SKhbo05ucEzgif-PB2sftCXRRKHd9Umb7MMmsjjub9AQ2RDTwgVeIuP5aSaQ-y51DBAYSLMqdcQMSfToElHJAj_8_1chqi1-IP1PC11JN1P-dckf8FTgANMxEIQ4UExv07vEtVe8BI1AS8nLDhxou-rU0UYbZ5G03qpJgA8tiYsuo7Y9J3MTwu2EHy4641ylXmiDeNIP3aEdCDnnDclypGagUZX1ZIE7nCxlm2zNu5KAR7rfgBz4weFo6-tTgmw6Gg1qeY9sLOB2uoIaxV91mQjxfMT26jnqLkLbucdNMGIUPn6EszZIHbRb_UasAZKKT0Sg1gWmCC_JZlj--fhc_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله با پهپاد انتحاری، یکی از باتری‌های گنبد آهنین اسرائیل رو زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/121721" target="_blank">📅 11:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121720">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
گزارش در وال استریت ژورنال: ایران از غول تجارت رمزارز بایننس برای فرار از تحریم‌ها و انتقال میلیاردها دلار برای تامین مالی ارتش خود در طول سال‌ها استفاده کرده است - از جمله انتقال رمزارز که این ماه انجام شده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121720" target="_blank">📅 11:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121719">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
روزنامه وال استریت ژورنال: وزارت دادگستری آمریکا تحقیقات خود را درباره استفاده ایران از صرافی بایننس برای  دور زدن تحریم‌ها آغاز کرده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121719" target="_blank">📅 11:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121718">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
بلومبرگ: پوتین می‌خواهد جنگ اوکراین را تا پایان امسال به پایان برساند، اما فقط با شرایطی که روسیه بتواند آن‌ها را به عنوان پیروزی معرفی کند.
🔴
این شرایط شامل کنترل کامل منطقه دونباس و تضمین‌های امنیتی گسترده‌تر از اروپا است که به طور موثر کسب‌های ارضی روسیه در اوکراین را به رسمیت می‌شناسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121718" target="_blank">📅 11:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121717">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a8a3dcb3.mp4?token=q2jZeAQjS1oVhX9O4eCMwVCb_9gPgP_iYiEj3lR1c4YA47VKDhFwAuSGG7mE43YQ87WNckYOBaoYD4aBkQ2tY44FdgXmuxke-pRLsA0GzeG-7TCLjY6ZrkMbBwlm9i8bftRbEJ3Yt-bbvEBKcds6ajKJjqCEC_rHY_4oDma0_TfFhzvTZve8T8PKjT5KRwHzCjZ7PPL5EmyQHBFC_uIu5JF1sSNVVx_Nl83OR55pbrSG6DLYCkzC5IHJNEnSJvVU3eHeYHvm-CmuY5_eF0r8lTo6jDZYhKhz7w36sw8OG5xzh0TKmJ-TzgZktd4W2RIpMTlWu5SdkIVcbv9-l87InA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a8a3dcb3.mp4?token=q2jZeAQjS1oVhX9O4eCMwVCb_9gPgP_iYiEj3lR1c4YA47VKDhFwAuSGG7mE43YQ87WNckYOBaoYD4aBkQ2tY44FdgXmuxke-pRLsA0GzeG-7TCLjY6ZrkMbBwlm9i8bftRbEJ3Yt-bbvEBKcds6ajKJjqCEC_rHY_4oDma0_TfFhzvTZve8T8PKjT5KRwHzCjZ7PPL5EmyQHBFC_uIu5JF1sSNVVx_Nl83OR55pbrSG6DLYCkzC5IHJNEnSJvVU3eHeYHvm-CmuY5_eF0r8lTo6jDZYhKhz7w36sw8OG5xzh0TKmJ-TzgZktd4W2RIpMTlWu5SdkIVcbv9-l87InA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیرکل ناتو: تفاوت ما با چین و روسیه این است که یک نفر همه تصمیم‌ها را نمیگیرد
🔴
مارک روته، دبیرکل ناتو، اعلام کرد: «ناتو یک ائتلاف سیاسی و نظامی است. تفاوت بزرگ ما با چین یا روسیه این است که در آن کشورها در نهایت یک نفر همه تصمیم‌ها را میگیرد.»
🔴
او افزود: «ما یک ائتلاف دموکراتیک و نظامی هستیم و به همین دلیل تصمیم‌ها همیشه بر اساس ملاحظات سیاسی و نظامی گرفته میشوند. ساختار ناتو این‌گونه عمل میکند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121717" target="_blank">📅 11:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121716">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9d60253b.mp4?token=dzfvwL7EoYAeITMvZUG_jY-EXi_2TFd5w_hgca2oIE4VsVFCYiXmA92a45vdd-2RYHcPL0kPw6Lb5jIAXETAYtuAY6OEu5PkCilVch-8xZB0r8ztQv1BRLxzNlPd0uxa4RB1X1gWCOE_QJfGYlGGNmKurcckDYEmqmG-C189UBiM6fqF_tKZQhLy2Hm4PTkKkXoICHMP2XBLODAOfIHBZG7NzLC4_mwGc1vwDvMyTUOYZY3jTWXxW0lhTrCh1XzFlIsTEHnlLnQvx2g6LJ-rKx079ZGXaVmSa96HnKe6J8-5KapSX6LfD0nSK_Imz_oSQd9KKlGDSf5oTHqgorfDxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9d60253b.mp4?token=dzfvwL7EoYAeITMvZUG_jY-EXi_2TFd5w_hgca2oIE4VsVFCYiXmA92a45vdd-2RYHcPL0kPw6Lb5jIAXETAYtuAY6OEu5PkCilVch-8xZB0r8ztQv1BRLxzNlPd0uxa4RB1X1gWCOE_QJfGYlGGNmKurcckDYEmqmG-C189UBiM6fqF_tKZQhLy2Hm4PTkKkXoICHMP2XBLODAOfIHBZG7NzLC4_mwGc1vwDvMyTUOYZY3jTWXxW0lhTrCh1XzFlIsTEHnlLnQvx2g6LJ-rKx079ZGXaVmSa96HnKe6J8-5KapSX6LfD0nSK_Imz_oSQd9KKlGDSf5oTHqgorfDxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دولت ترامپ فروش ۱۴ میلیارد دلاری سلاح به تایوان رو متوقف کرد
🔴
تا مهمات آمریکا برای جنگ ایران رو حفظ کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121716" target="_blank">📅 11:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121715">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmE7UQrr5Ic6J9j_SI5ryrD_YBTdf0PYbUHWupZRbsqzV8ZSsUWJL1Vo1uCmOnXWQyVJHPlk8EoLSDak5MQPYNEAGiF7dU4xDBf8LJz-Y_8lXH1iU71NeWA3RPK6_UWHLqkiaVa1WqaRC1_mETiihFooefw2s34QnMSzOsdDRlJR35WftsCFO5TD73_Sy0kyZEzxujlGDWGTOWu5QErvt7WlvGMPzOdAzelHTFWF0lD1S1QOVD3KT-77csPn6VSkELj6LPC7J3LWJI10Q7-I9HbJOJblRHa7smVl5NekyVNdIo-VLtNl_2BuU6iJe_UZ1DwSaf11Jpm0pIOLOAyhyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ناو هواپیمابر آبراهام لینکلن در بالاترین سطح آمادگی عملیاتی قرار دارد
🔴
ستاد فرماندهی مرکزی ارتش آمریکا، سنتکام، با انتشار تصاویری از پرواز جنگنده‌های نیروی دریایی آمریکا از ناو هواپیمابر «یواس‌اس آبراهام لینکلن» در دریای عرب اعلام کرد گروه رزمی این ناو در «بالاترین سطح آمادگی عملیاتی» قرار دارد.
طبق بیانیه سنتکام، این ناو همزمان در اجرای محاصره دریایی آمریکا علیه بنادر ایران مشارکت دارد. فرماندهی مرکزی ایالات متحده همچنین اعلام کرده در جریان این محاصره دریایی، ۹۴ کشتی تجاری تغییر مسیر داده‌اند و چهار کشتی دیگر نیز «زمین‌گیر و مجبور به توقف» شده‌اند.
🔴
سنتکام پیشتر ویدیویی از ورود نیروهای آمریکایی به یکی از کشتی‌هایی که قصد عبور از خط محاصره را داشت منتشر کرده بود. واشنگتن میگوید هدف از این فشارها، وادار کردن تهران به توافق برای پایان دادن به جنگ و کاهش تنش است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121715" target="_blank">📅 11:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121714">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سپاه : خنثی‌سازی مهمات عمل‌نکرده در خرم‌آباد(فردا)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121714" target="_blank">📅 11:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121713">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
دبیرکل ناتو: تعدادی از کشورهای اروپایی تمایل خود را برای مشارکت در تلاش‌ها جهت بازگشایی تنگه هرمز ابراز کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121713" target="_blank">📅 11:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121712">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
الجزیره: مقامات دریایی بریتانیا مدعی گزارشی از وقوع حادثه‌ای در ۹۸ مایل دریایی شمال سقطری، یمن شدند
🔴
عملیات تجارت دریایی بریتانیا: کشتی نزدیک شدن یک قایق کوچک با ۵ سرنشین را تأیید کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121712" target="_blank">📅 11:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121711">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
الجزیره: مقامات دریایی بریتانیا مدعی گزارشی از وقوع حادثه‌ای در ۹۸ مایل دریایی شمال سقطری، یمن شدند
🔴
عملیات تجارت دریایی بریتانیا: کشتی نزدیک شدن یک قایق کوچک با ۵ سرنشین را تأیید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/121711" target="_blank">📅 11:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121710">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وزیر امور خارجه کانادا: ما به محض دستیابی به آتش‌بس دائمی، در مین‌زدایی و حمایت از آزادی دریانوردی در تنگه هرمز مشارکت خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121710" target="_blank">📅 11:01 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
