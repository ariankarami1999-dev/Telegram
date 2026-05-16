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
<img src="https://cdn4.telesco.pe/file/Djkz2xaIjtNyBioPz-ZWNDJkWkjdX3d8rdmuTscYXyct0K2YbsoTfD9H_vYgrL0Rhe_PIY6S_37F4KbP5g43-DNE-YBa7aGy_DrIbYi3ilDI_yBEo7jCD2N-CNA95E_6WZZqz5LoGHDnyDnv8UUNoPoZzAKhTyhI3FGN_216FCzu1LKHfwaRthuHbZD4ZVLL9YpkywMElIdI2PuA7AiJS3Qc92o2GCbe7kIstCM8_8xPglzFFQ4Zfotah8J76VfT15n6Bd1q6kNQ_yITTCWx2RpRiB1n16fM9HLZoEiAZRWS8yZT7r7z_9-P3Wufo-W1MSMDuCAXZ-FiUPgLNA8vmQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 262K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 02:07:18</div>
<hr>

<div class="tg-post" id="msg-11432">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc37be173.mp4?token=kLsHwF_QILKCl_wOPzgbOZsfokGNtIzs_MBO_yYJHLeEKvA0gyolF0V-JkQUwFsklQjPiuK3c2kE1kZuYnzFQta3wo8KgjsuTFN6BpJy6Rj3mly5QqQkfFXh5_l6ykFzkaSp8Y62EeT0etW3jbdSOM6Bt0xPoGJvj2VtEA9UIqDwANk_oJ16Qhg0iKmy4VP21AFokhBpBXKlOHa1JGXWIt0lSRnnGJJM8_WzrPllFQDnKTcoWOuIioVcB672CeikK8fjg4f_3eGKC2LlEE8eKtCCPJyDmnw0ETjzpAoOQ1Oy_M-1apfKgIHHphSSvSy_Szi991-Y0l7DvrRSSB70tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc37be173.mp4?token=kLsHwF_QILKCl_wOPzgbOZsfokGNtIzs_MBO_yYJHLeEKvA0gyolF0V-JkQUwFsklQjPiuK3c2kE1kZuYnzFQta3wo8KgjsuTFN6BpJy6Rj3mly5QqQkfFXh5_l6ykFzkaSp8Y62EeT0etW3jbdSOM6Bt0xPoGJvj2VtEA9UIqDwANk_oJ16Qhg0iKmy4VP21AFokhBpBXKlOHa1JGXWIt0lSRnnGJJM8_WzrPllFQDnKTcoWOuIioVcB672CeikK8fjg4f_3eGKC2LlEE8eKtCCPJyDmnw0ETjzpAoOQ1Oy_M-1apfKgIHHphSSvSy_Szi991-Y0l7DvrRSSB70tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
حدادعادل: والا منم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
@withyashar</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/withyashar/11432" target="_blank">📅 01:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11431">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ایران به عبری ی توییت زد ک  پیام روشن بود لفاظی نکنید... המסר היה ברור: אל תהיו רטוריים... یعنی کار ایران بوده؟ مث ک کلاهک اتمی اسراییل اونجا نگهداری میشده</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/withyashar/11431" target="_blank">📅 01:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11430">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSoul</strong></div>
<div class="tg-text">ایران به عبری ی توییت زد ک
پیام روشن بود لفاظی نکنید...
המסר היה ברור: אל תהיו רטוריים...
یعنی کار ایران بوده؟
مث ک کلاهک اتمی اسراییل اونجا نگهداری میشده</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/withyashar/11430" target="_blank">📅 01:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11429">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd5a8240dd.mp4?token=G2aB3D9zhtybpt_nGx25SrvHey9lQxkE2GY941pODpOUvrrmUWkAFmXZZjgqSpMjfKVTkX9MyVGe5vhNy_oTX6Zm7B_ntjUXiZXmmsWMRLqRtBlaXTm8HKWg9TqiTbVT999qmThXf9LaeoHAqu49JqX7m_9uflmKP_sW2-klrA0TjFKIVmcggrjAG492aIH918-Gwzzck6E_iXdlwS0oUPPJbGGlMNAnhm1yM_m1o9jrEkh25UocJZHJhDWjUdBcfN_KQwr2r1Kx0HiuKyQsNTQr-SMXfYLauI1pRzkt1honnQSclSEQglX9YbwGyhB6okpesqVzNgz9E_SvLx8uxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd5a8240dd.mp4?token=G2aB3D9zhtybpt_nGx25SrvHey9lQxkE2GY941pODpOUvrrmUWkAFmXZZjgqSpMjfKVTkX9MyVGe5vhNy_oTX6Zm7B_ntjUXiZXmmsWMRLqRtBlaXTm8HKWg9TqiTbVT999qmThXf9LaeoHAqu49JqX7m_9uflmKP_sW2-klrA0TjFKIVmcggrjAG492aIH918-Gwzzck6E_iXdlwS0oUPPJbGGlMNAnhm1yM_m1o9jrEkh25UocJZHJhDWjUdBcfN_KQwr2r1Kx0HiuKyQsNTQr-SMXfYLauI1pRzkt1honnQSclSEQglX9YbwGyhB6okpesqVzNgz9E_SvLx8uxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناو هواپیمابر جرالد فورد به خانه بازگشت
@withyashar</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/withyashar/11429" target="_blank">📅 01:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11428">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63af08e0ad.mp4?token=ZVuwptOOWg21Xpuwld5MggPmWPHcuOzbZBKPC4WH9EP39MtfnY6DLpOljvnq9QOXEBBv6RREKJHpA8ZS0Cidum2txRW7GkRfDBvjEfImpUupBHbdWfcmyt-gdA9xN0epXYpo71lWOWfUijEQtVEjl3Lqi7vk5Pn7Mof3OD0J53voGwm_TNyKpbDFeBidLJfbEkixK1lBVmJ4Sz47QkcsXzj_cquFNd5ZJUH7W8SvdZjXRoGnMa-euf0d1xUokDuYU8B36JJ1MPFuHaZ4xae_zEi3Av_RBojxxsnnOj6Ls3e9cCu3RpHWiG5WLvNkyHb6VQgtzDqr75EQHW2J-qXYnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63af08e0ad.mp4?token=ZVuwptOOWg21Xpuwld5MggPmWPHcuOzbZBKPC4WH9EP39MtfnY6DLpOljvnq9QOXEBBv6RREKJHpA8ZS0Cidum2txRW7GkRfDBvjEfImpUupBHbdWfcmyt-gdA9xN0epXYpo71lWOWfUijEQtVEjl3Lqi7vk5Pn7Mof3OD0J53voGwm_TNyKpbDFeBidLJfbEkixK1lBVmJ4Sz47QkcsXzj_cquFNd5ZJUH7W8SvdZjXRoGnMa-euf0d1xUokDuYU8B36JJ1MPFuHaZ4xae_zEi3Av_RBojxxsnnOj6Ls3e9cCu3RpHWiG5WLvNkyHb6VQgtzDqr75EQHW2J-qXYnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار سنگین در بیت شمش اسرائیل و دیده شدن ابر قارچی گزارش شده که در کارخانه شرکت تومر رخ داد. این شرکت موتورهای موشک سنگین و سبک، از جمله موتورهای پیشران موشک‌های ارو ۲ و ارو ۳، موتور موشک هدف سیلور انکر، موتورهای ماهواره هورایزن و موتورهای موشک باراک ۸ و باراک ام‌ایکس را توسعه و تولید می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/withyashar/11428" target="_blank">📅 01:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11427">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/withyashar/11427" target="_blank">📅 01:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11426">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8cf2c560.mp4?token=Lcjls6ZHH89NtjRz6MEYfAimeiRRmsPSyJw9Llb_mzg0a5A0k0Bx9nkCxZHticm3NWeiou_xu0uUu-IGLN9a8HkD7M6QVr3JiL9yYWdYXCRQJyt6Fy-eziRQ9BTB5r1CaSQpYwbr99pl0F2jqIP7p6DYToVYu6eCo0U6ruEK_3CL0fyLUSHBTiHCAuLjK0ucvv2iR8MoHisP-EjrqLefPgWdrw6b9ouCMSR4ZwwHi2NSvDaJ3qaG8el5sUCZ1BbMLGErpb0oM9nXnoTyIObdEZsqQ6ZpT6bKtda49-Odgebpbrh-kiiVBB6I0tYvJEzIdrrTu1238T_h4fzmMWp-nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8cf2c560.mp4?token=Lcjls6ZHH89NtjRz6MEYfAimeiRRmsPSyJw9Llb_mzg0a5A0k0Bx9nkCxZHticm3NWeiou_xu0uUu-IGLN9a8HkD7M6QVr3JiL9yYWdYXCRQJyt6Fy-eziRQ9BTB5r1CaSQpYwbr99pl0F2jqIP7p6DYToVYu6eCo0U6ruEK_3CL0fyLUSHBTiHCAuLjK0ucvv2iR8MoHisP-EjrqLefPgWdrw6b9ouCMSR4ZwwHi2NSvDaJ3qaG8el5sUCZ1BbMLGErpb0oM9nXnoTyIObdEZsqQ6ZpT6bKtda49-Odgebpbrh-kiiVBB6I0tYvJEzIdrrTu1238T_h4fzmMWp-nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب بیداریم !
@withyashar</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/withyashar/11426" target="_blank">📅 00:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11424">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏ جیمی دیمون، مدیرعامل جی‌پی‌مورگان چیس، درباره ایران:
‏آنها ۴۷ سال است که تجاوز، قتل و کشتار می‌کنند. دنیای غرب اجازه جنگ‌های نیابتی را داد.
‏ما درس عبرت گرفتیم - باید سال‌ها پیش به سراغ سر مار می‌رفتیم.
@withyashar</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/withyashar/11424" target="_blank">📅 00:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11423">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXFqG_9ZtE0VexMbKRXGK_ZkOyW_XENgnaQ5GVFLXYsLKUmnDBiFmREPiYocYM43h9PvSrx6tOTNGJolrz5vl0elW1wEqZh7dsouWrheaXPrXOb7Fa2-B3R306tSR5Q05aiZeTRkPpVN-Pl-rssFCXArZR4vrgxjhnEybedPe_zHZi80Dh6kkbZsK-8EX5IXgnmtcYwMQuiCTWrff4nWQljHP-fx-IgjBg2lkGyv6DCjLd5OHCExJjdAJrxfh01b6ynDX_6pGF77Q93bNKT0YtQPMX8oHHC4Wq1tr6P5aLYJEEpa4kr19rYkx7vfrnqeVG6nuy86aCvEia0X0yhKMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد امین صابرکار، دانش‌آموز ۱۷ ساله بسیجی بوشهری،‌ حین انجام تمرینات تیراندازی اشتباها با آتش خودی(فرندلی فایر
😬
) کشته شد
@withyashar</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/withyashar/11423" target="_blank">📅 00:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11422">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">@withyashar
فرهنگ ما همیشه غالب میشه</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/withyashar/11422" target="_blank">📅 00:21 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11421">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42c743cc72.mp4?token=JsRDz7xlV2A8YjTk8Z-ObY5TrxCU_fl2w3BNOFeqKYQTCrC6CsRjMtPgXUYlpULnDR60lMrKOHBqzVBO4NuXsQctlzYy9mtHVy4sH02-G2nkKG6F2QXGmUN_y3vmQiHXo5zpMO28PVHEDbIgXTvjBixZCEahzmK5OcYDG2EixMZu4eOELaXJ-IgSXWSLKN3CIGP5fK9Ndni2ylbSNyd0HJeWT53L2sCHyDgo8vHQbNEijkhGktkbZ-1Opd7CwW4XV3vFmLLqat1c4MxK63llWrGtMTjB60PkigYM2t91gTDHby6qdyAxTQi-2A6ZMjCermF7BjoIHpH9Q7IZwM2FyxgEFZb0I37KrvaEkNhJdRNITFm2FCqyn_I2o3OEcnwzJaxdqXiXMXzslG7BnIQGBAQ7dxgP51LiKcHktD0ZMxuomvvytjgOPvRIb7KrSOhJ2mh27guOLfVUBD8gumHp7jU6MPpaFlU9m-Dl-ya4P-SM_TQoGMjGxSEe2a3f15pU-wfOTtImySC0k0K3VBCqqjLoN2EBGmi8xv3rMxWjPLWrQ1ligg-JQRJG1BHH6RgON-4IGpZCgqd__KHTvh3KSVyHhEjQUAtqzwVlHVvmzCvMZL8kRasgAYynODdoDKrFKGsr1mc8bxl9UzbNnRuDUnnOwcWNLTvNL118kHuThN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42c743cc72.mp4?token=JsRDz7xlV2A8YjTk8Z-ObY5TrxCU_fl2w3BNOFeqKYQTCrC6CsRjMtPgXUYlpULnDR60lMrKOHBqzVBO4NuXsQctlzYy9mtHVy4sH02-G2nkKG6F2QXGmUN_y3vmQiHXo5zpMO28PVHEDbIgXTvjBixZCEahzmK5OcYDG2EixMZu4eOELaXJ-IgSXWSLKN3CIGP5fK9Ndni2ylbSNyd0HJeWT53L2sCHyDgo8vHQbNEijkhGktkbZ-1Opd7CwW4XV3vFmLLqat1c4MxK63llWrGtMTjB60PkigYM2t91gTDHby6qdyAxTQi-2A6ZMjCermF7BjoIHpH9Q7IZwM2FyxgEFZb0I37KrvaEkNhJdRNITFm2FCqyn_I2o3OEcnwzJaxdqXiXMXzslG7BnIQGBAQ7dxgP51LiKcHktD0ZMxuomvvytjgOPvRIb7KrSOhJ2mh27guOLfVUBD8gumHp7jU6MPpaFlU9m-Dl-ya4P-SM_TQoGMjGxSEe2a3f15pU-wfOTtImySC0k0K3VBCqqjLoN2EBGmi8xv3rMxWjPLWrQ1ligg-JQRJG1BHH6RgON-4IGpZCgqd__KHTvh3KSVyHhEjQUAtqzwVlHVvmzCvMZL8kRasgAYynODdoDKrFKGsr1mc8bxl9UzbNnRuDUnnOwcWNLTvNL118kHuThN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوش جان میسپریم به فریدون عزیز تا من موتورم رو گرم کنم ویس بزارم
@withyashar</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/withyashar/11421" target="_blank">📅 23:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11420">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZm-WAsBthphr3bFduDdjYgRpRdHcMsbJJ-F1tynGrhGtkqbPNLGioOn3F8xbd8Sv5oHia_KD_P2d2PEDO3e9d5wYkxoVFaPVTdz_DIyFMDYd6SUATZX10WJZeDK4649yN_gicJQUjbPEjsiSqF8Sj9upcQg_XuJvBz9iyId9mt3G4pn_RVWOD0mD1yY2haOy9LSnoDdz-4UTfRIU5rAQU1FBzd2dWyIky6DVecSG7MS9wJgSANJqgdwVN1k6gk6l4Q3suFFR84vfwE7Xj_oJzX3KzQ7YnC8vc0AeQ8TFZbwhnmGCsqMbaAyMZ4O_X7M1RufdiwBdJ5_Gj07o0ZP-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : آرامش فبل از طوفان
قایق تندرو با پرچم جمهوری اسلامی دیده میشود …
@withyashar</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/withyashar/11420" target="_blank">📅 23:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11419">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/withyashar/11419" target="_blank">📅 23:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11418">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMJdBKQ74rjfcEJPXudL5Hh2F7Clw4p2hL1JeQDWhdHZxA8oklWdWHat67ts1GElTmbg_5v0y-vrxT-2uPXGx7r-ACZGXqKfGYJp4wH9Yvvjf6nSQ6YeqIslyEqDjy3sjJ-9PhIBDUB-9HF5d7dx2ilp6ytJzT1Anv5acm_fVFA1PQHWXmWFQGM4wZnO26B86QZvRmQKQ12qA3EWQRPBoaNgeuq-Nv_yBBkLUFUp5-7LRgrdO7ASzEibQa8E5lVzWKcs7W8y_Q66Vxqe3OYjkvnQAcmeCdgzuNGTQrCKAx6UomgSWd5TvllwTOKPVBl3rm8EBAJuI3psCLKFAEyX1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاورین شاهزاده (امیر اعتمادی و سعید قاسمینژاد) ، علی کریمی‌ رو به علت واکنش ‌به کنسرت و آهنگ شاهین نجفی آنفالو کردند  @withyashar</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/withyashar/11418" target="_blank">📅 23:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11417">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">شاهزاده رضا پهلوی در نشست آینده تکنولوژی در ایران:
ایران می‌تونه به کره جنوبی تبدیل بشه، اما به دلیل وضعیت سیاسی کنونی به سمت الگویی شبیه کره شمالی سوق داده شده؛ جمهوری اسلامی در ذات خودش قابل تغییر نیست.
@withyashar</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/11417" target="_blank">📅 22:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11416">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کانال ۱۳ اسرائیل:
اسرائیل در بالاترین سطح هشدار برای احتمال از سرگیری جنگ با ایران است.  در صورت از سرگیری جنگ با ایران، احتمال دارد ایران در روزهای نخست ده‌ها موشک به سمت اسرائیل شلیک کند.
@withyashar</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/11416" target="_blank">📅 22:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11415">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قلعه نویی در لیست نهایی جام جهانی آزمونو خط زد و گفت باشرف هارو دعوت کردم.
@withyashar</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/11415" target="_blank">📅 22:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11414">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وال استریت ژورنال : ایران و آمریکا بر سر یک موضوع توافق دارند در حالی که بن‌بست دیپلماتیک بین تهران و واشنگتن ادامه دارد, هر دو طرف می‌گویند که در حال حاضر درباره سرنوشت ذخایر اورانیوم غنی‌شده ایران بحث نمی‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/withyashar/11414" target="_blank">📅 21:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11413">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نتانیاهو : اگه آمریکا دوباره بخواد عملیات نظامی علیه ایران رو شروع کنه، اسرائیل آماده‌ست
@withyashar</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/withyashar/11413" target="_blank">📅 21:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11412">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFapo1414</strong></div>
<div class="tg-text">داداش ناموسا من اونجا بودم داد میزدم به شاهزاده میگفتم حتما با یاشار ملاقات حضوری بکن</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/11412" target="_blank">📅 21:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11411">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hy4MG0Xs0crPl-bdKMTxSKtOtSGeLF7DuOiGwQYlVR_emiUhUl8ur6rXwGeJ8GlvnNKkoaCogPgkvzddFWddnT5VEaVY4nPZ9N9KkTZtYT6cPTB2b5Q7VxNirE5OejYHgRDMLUrunu_UyuPzQYD7o4GI75mNWRELKa2_usw6jJaKXFqbnhqWyIEiRl2fACbX-VjGGXrH2QzdQdXoTHYf787Eu0LEHWNyUPWZbo0Sv0M5p5HSegScKfRYFC24BYrlXF4g13q3-F0pNBA-hbqXsb8RRJdX6VtueRPpBJQhoGJpRDwq1o2AOyRhMznjw-iqxJ7cpYZcaVQXBdu_jiMMkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو سخت ترین شرایط بهمون روحیه دادی، تو جلسه ی بچه های تکنولوژی با شاهزاده به یادت بودیم!
❤️</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/11411" target="_blank">📅 21:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11410">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فرهاد مجیدی با البطائح به دسته دو امارات سقوط کرد
@withyashar</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/withyashar/11410" target="_blank">📅 21:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11409">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این ناو گروه در حال فرار هستن یا چی ؟</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/11409" target="_blank">📅 21:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11408">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromH.E</strong></div>
<div class="tg-text">این ناو گروه در حال فرار هستن یا چی ؟</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/withyashar/11408" target="_blank">📅 21:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11407">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkk9VjPAGNuIHMLlMlS1fZGwCzD-L8oGMG0plfxK9E_1Pr-PQBqUbmO7vSSV6twCcja133KPKObNbBu3XhUrsbo37rvIIntvlok41uxkfxD3ROYEG49O1Kq_kA_UhKj9YWnC35d61FtN-VJtEYCtSfENK_pp-B_HNnlojd90R1lUS5DjNg5pElchVcQP7gJ60KD4GJ7B_NOUbKQLZ4ZjsVJkZK612QVlqTmjLbxZPA8U8uCGpjJiqcDZGbX8DAJW4j9YpCcRokfm5jiQ3nSeqtt3B86hm8ehq7QRFbLOtIhW9wkE9B6bQyoxBexNOrbUp2NDd12AB44zv-Ea7zkI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناوگروه  آبراهام لینکلن با سه اسکورت با سرعت به سمت دریای عمان می‌ روند  ، ۲۶ اردیبهشت. (مکان 260 کیلومتری چابهار)
@withyashar</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/11407" target="_blank">📅 21:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11406">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شبکه 13 اسرائیل: هم اکنون ارزیابی‌ها در اسرائیل بر این است که جنگ با ایران در روز های آینده از سر گرفته خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/11406" target="_blank">📅 21:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11405">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ: اگه به آمریکایی‌ها آسیب بزنید، یا در حال برنامه‌ریزی برای آسیب زدن به آمریکایی‌ها باشید، ما شما رو پیدا خواهیم کرد و خواهیم کشت.
@withyashar</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/11405" target="_blank">📅 21:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11404">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ در گفت‌وگوی تلفنی با شبکه فرانسوی «بی‌اف‌ام‌تی‌وی»:
آینده مذاکرات نامشخص است اما اگر توافقی حاصل نشود ایران روزهای بسیار سختی در پیش خواهد داشت
@withyashar</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/11404" target="_blank">📅 20:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11403">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">العربیه: طبق گفته منابع آگاه پاکستانی، در بحث تنگه هرمز، پیشرفت‌هایی حاصل شده است
@withyashar</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/11403" target="_blank">📅 18:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11402">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75a350642e.mp4?token=gi16V0sFQm6YGa8oJpGWxo-C0SPq2BRi3RJbr_NBx_HqroTO2Bi843-R7h4wc8JhQ0mRbmc7Ul2b6T_QWpoEoOSH0zBC0KPte6X2uCdLP_uB-6GksBRi8ZzNuhKKKkqK3dcfMCxpi3b_50ryRGjGK44Qu7D667B1VTMjdQWqKcUTJvufMQxsjlUUtFcOWmLNrFgid51aKDBnE9hxLnTGHBII1Av7wU_zOs2MUKuhFftEoy-dFY3iTqT0xCjZfndfjCdCqk774Q_LkaRqKgFdI9oZdg3iP3oxrCdVmx1uQNJD_1NQSrVmBgXYnuPm3DVa_APrT8W6CqQvghnGlKYsEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75a350642e.mp4?token=gi16V0sFQm6YGa8oJpGWxo-C0SPq2BRi3RJbr_NBx_HqroTO2Bi843-R7h4wc8JhQ0mRbmc7Ul2b6T_QWpoEoOSH0zBC0KPte6X2uCdLP_uB-6GksBRi8ZzNuhKKKkqK3dcfMCxpi3b_50ryRGjGK44Qu7D667B1VTMjdQWqKcUTJvufMQxsjlUUtFcOWmLNrFgid51aKDBnE9hxLnTGHBII1Av7wU_zOs2MUKuhFftEoy-dFY3iTqT0xCjZfndfjCdCqk774Q_LkaRqKgFdI9oZdg3iP3oxrCdVmx1uQNJD_1NQSrVmBgXYnuPm3DVa_APrT8W6CqQvghnGlKYsEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوئل نهایی ، وضعیت الان!
@withyashar</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/11402" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11401">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTm bzx</strong></div>
<div class="tg-text">عرزشی ها اومدن که خبر مرگ بابای سپاهیشون رو زودتر تو چنلت ببینن
اخه از رسانه های دیگه ۱ ساعت حداقل جلوتری ستون
😂
🔥</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/11401" target="_blank">📅 18:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11400">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_TnkN0KtQR9To8UEHc0sTLdDRbEUrqFBYzZPelxAvsuV9_1xm6yWe5rlUAX7Dm7zFQqVRzHAxmoSNFuQ-0l2mhqX5xlKowToLgTB5ORwOYfEjjsGBDhqYq1q0yMJ7eKHljJL5AC6LTZXtpYMXcVHx7YL7rURYQYeOg1HqUVJDfcTR59XXq4v-X7WAAI2psespbuSkt5-w3H0gZHf0hijagejvwlK1jgz3Zf4IHcPN-CjpJAAyC3JGHQcRU00dza4t2kgo_Y-KHDwSORhT2aHoxTK269Uqwdx4UILErnqkMky1s9qqhMSO4rzdVcrHheMpwIKl2x_ykQU7RsEj7jAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ :
شوخی نداریم!!!
ببین قراره بعدش تو موضوع مورد علاقت چه اتفاقی بیفته!
@withyashar</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/11400" target="_blank">📅 17:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11399">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سقوط یک شهر پاکستان به دست جدایی‌طلبان
منابع محلی روز شنبه از تسلط جدایی‌طلبان بلوچ بر شهر راهبردی دالبندین در پاکستان خبر می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/11399" target="_blank">📅 17:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11398">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فقط برای یک پست که نمیشه ببندم مهندس ! کلا ببندمم که یعنی میگی خنده رو از روی لب چندین هزار نفر بگیرم به خاطر ده نفر. ما اینجا هدف اصلیمون مبارزه با اخبار سمیه و روحیه دادن به مردم. اجازه بدید در عرزشی سوزترین رسانه ایرانی بسوزند و حرص بخورند</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/11398" target="_blank">📅 17:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11397">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from➖</strong></div>
<div class="tg-text">میتونی ری‌اکشن رو هم ببندی داداش!</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/11397" target="_blank">📅 17:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11396">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">این پست اوناییکه استیکر خنده گذاشتن رو از کانال مسدودشون کن</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/11396" target="_blank">📅 17:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11395">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐇𝐚𝐝𝐢</strong></div>
<div class="tg-text">این پست اوناییکه استیکر خنده گذاشتن رو از کانال مسدودشون کن</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/11395" target="_blank">📅 17:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11394">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">لازم به ذکر است شخص اینجانب ، یاشار در اتاق جنگ هیچ رابطه و تیمکشی با هیچ گروه جناح و سمتی ندارم مسیر من مسیر مانوک خدابخشیان و فریدون فرخزاد است و هم پیمانان من فقط مردم واقعی و وطن پرست ایران هستند و برگ برنده ما همه با هم اینجا برای عبور از مسیر فقط فقط فقط خود شخص شاهزاده رضا پهلوی است ، یک بار دیگه خواستم اهداف و مسیر خودم را مشخص و کلیر کنم
@withyashar</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/11394" target="_blank">📅 17:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11393">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مشاورین شاهزاده (امیر اعتمادی و سعید قاسمینژاد) ، علی کریمی‌ رو به علت واکنش ‌به کنسرت و آهنگ شاهین نجفی آنفالو کردند
@withyashar</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/11393" target="_blank">📅 17:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11392">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9ZOj6kvQHacKmFNy8fyEj4sxzhJM-09bHrTkacAgS1QfK-yaunqtzWHbIoAwfVBzozNdofn0PEo5SnxPNQPzpT3wwbA4ivKzeSAPbtHoQagJ9MXdzcFyCQbtQ98ZeS-jXJ0zX_WYZuiWJFgmswS5PWiAEUpgu1RPgCz1YcntnhRQbP9Qu-jc43lfhc5AyOGADfIxBWgTxZ5DTh1o_SkPcMMsOEfqZIUbM8hhQv7sy_PdVst_AuoQBffyv_6RZXM4KpNqzfg2YE9RZt1_fwwfgbHdGd5lNi19GPJYDUIeOszTICGd5SxzXps-ebtc5zLkELqKUYhGFfkkwBbC4OGpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جهانی پسر بچه … به یاد جاوید نام های کوچکمون مبارزه میکنیم تا  نسل جدید این درد ها رو نکشه !
@withyashar</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/11392" target="_blank">📅 16:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11390">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ایسنا: وزیر کشور پاکستان برای دیدار با مسئولان جمهوری اسلامی ساعاتی قبل به تهران سفر کرده.
@withyashar</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/11390" target="_blank">📅 15:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11389">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کانال ۱۲ اسرائیل مدعی شد: ترامپ بزودی با اعضای کابینه خود جلسه اضطراری برای پایان دادن به اوضاع ایران برگزار میکند.
@withyashar</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/11389" target="_blank">📅 15:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11388">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/525b5bf33d.mp4?token=aTL08U-_JmEciKREnClO0PdepzG99n_IQ3bK5ACQO4grH8MWtdMFjLm_i8_BOm8b5RMQmQh-Kwa4nnIa4WOQJEB7qx_cfZ7v-qI4F4gXoKyzRvTJlFaN6MNQ1AbQM2vkPpDsL5RAonYp0rjtL-w9yg4zF4VXLxvpIiW3nWibCQZEs-l5HWWEZO4YNGqrQ0UDLn5yd6VpmV9r2cCn_FZhxzLbkS3YwGi9JQfqfM4TiWH0prg892exWD4q2oKfTYhabnpLWBMgnO7xt8aqpAlbhSSWRjyQ5kk_FyLb2KmEI1khJSUapMCqalWPE9iTin76FpE-bmpiU2X9Mv7kyrhhVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/525b5bf33d.mp4?token=aTL08U-_JmEciKREnClO0PdepzG99n_IQ3bK5ACQO4grH8MWtdMFjLm_i8_BOm8b5RMQmQh-Kwa4nnIa4WOQJEB7qx_cfZ7v-qI4F4gXoKyzRvTJlFaN6MNQ1AbQM2vkPpDsL5RAonYp0rjtL-w9yg4zF4VXLxvpIiW3nWibCQZEs-l5HWWEZO4YNGqrQ0UDLn5yd6VpmV9r2cCn_FZhxzLbkS3YwGi9JQfqfM4TiWH0prg892exWD4q2oKfTYhabnpLWBMgnO7xt8aqpAlbhSSWRjyQ5kk_FyLb2KmEI1khJSUapMCqalWPE9iTin76FpE-bmpiU2X9Mv7kyrhhVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر کلی رسانه ها اینه که ۷۲ ساعت طلایی پیشه رو داریم
😬
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/11388" target="_blank">📅 14:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11387">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شبکه فاکس نیوز: ارتش آمریکا درحال آماده شدن برای دور جدیدی از درگیری های نظامی در ایران است
@withyashar</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/11387" target="_blank">📅 14:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11386">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ایال زمیر، رئیس ستاد کل نیروهای مسلح اسرائیل اعلام کرد کشته‌شدن عزالدین الحداد، فرمانده‌ شاخه ‌نظامی «حماس» یک گام مهم و موفقیتی بزرگ در عرصه عملیاتی است.
او افزود اسرائیل «با جدیت» به‌ تعقیب و هدف قرار دادن سایر رهبران و فرماندهان حماس ادامه خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/11386" target="_blank">📅 14:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11385">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciz6o8CUMUD0-LuZsTqt0Ke338rJtOYQDEt996Na4dG1JDadcfKcONiOEqwTqfXmwWQ4FcGaZD1EGjKlnI_9Q-5OI1ChRdtyRnH2MEnGY3BVQPKstyLgihpF3L_hjV1HuiZy-80zwQHSYWy5BxwMvqHmAeWpya7cc_OIeFattQwuU_42OENo4BWUA837ZymN5bcrRQxpCozVifgh8EGtV_fSgx8ojg7IviSjA-w2-XfHOnOV_bpbVVrumq7Nk5x3G-UAqjoLvLbI-lXmeK3sqFfo3_Qk-DRnkD7sOfv-bG_7wqJeBEjtlmARrgWedUrt3pQA6hNgLxvGKjOOQzt-VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما هم میدونه چی میشه داره آموزش کار با سلاح رو میده
😂
اینا رفتنین شک نکنید
👋🏾
👋🏾
@withyashar</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/11385" target="_blank">📅 13:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11384">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPooria</strong></div>
<div class="tg-text">آقا یاشار عزیز،
واقعاً دلم می‌خواست یه چیزی بهت بگم از ته دل.
مرسی که با کارای دلی و عشقیت، بهم نشون دادی وقتی کاریو با دل شروع می‌کنی، چقدر می‌تونه برکت و موفقیت بیاره.
از اون موقع که تو نوجونی اون سایت برای پروموت کردن رپرها  ساختی تا همین الان که با تمام وجود وقتت رو پای این کانال خبری (تلگرام و اینستا) می‌ذاری تا مردم خبر درست بگیرن، یه چیز بزرگ یاد گرفتم ازت — اینکه عشق و نیت خالص از هر چیز دیگه‌ای قوی‌تره.
بهم یادآوری و یاد دادی که پیشرفت فقط با کار زیاد نیست، بلکه دلی و با عشق کار کردن توی کاره.
دمت گرم ، واسه همه این زحماتت، واسه الهامی که بهم دادی، و واسه اینکه خودِ واقعی‌ت رو بی‌منت به دنیا نشون میدی
💚</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/11384" target="_blank">📅 13:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11383">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">جسی واترز، مجری فاکس نیوز:
ترامپ درحال آماده‌شدن برای دور جدیدی از حملات نظامی به ایرانه.
@withyashar</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/11383" target="_blank">📅 13:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11382">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ: 5 بار با ایران نزدیک توافق شدم، ولی روز بعدش زدن زیرش
@withyashar</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/11382" target="_blank">📅 13:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11381">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نشست آینده تکنولوژی در ایران، با حضور و سخنرانی شاهزاده رضا پهلوی امشب ۸:۳۰ به وقت تهران ۱۰ صبح به وقت غرب آمریکا سانفرانسیسکو
@withyashar</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/11381" target="_blank">📅 13:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11380">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سنتکام به نیویورک تایمز : کشتی‌های ایرانی رو با ماهواره و چند روش دیگه ردیابی می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/11380" target="_blank">📅 12:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11379">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آسوشیتدپرس: بازگشت ناو هواپیمابر جرالد فورد به پایگاه پس از ۱۱ ماه مأموریت
وزارت‌جنگ آمریکا اعلام کرد پیت هگست، وزیر جنگ، روز شنبه در پایگاه دریایی نورفولک در ویرجینیا از ناو هواپیمابر جرالد فورد و ۴۵۰۰ ملوان آن پس از ۱۱ ماه مأموریت استقبال می‌کند.
این ناو ۳۲۶ روز در دریا بوده که طولانی‌ترین استقرار یک ناو هواپیمابر آمریکایی در ۵۰ سال گذشته و سومین رکورد از زمان جنگ ویتنام است.
@withyashar</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/11379" target="_blank">📅 12:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11378">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کانال N12 اسرائیل: جنگ سوم با ایران نزدیک است
@withyashar</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/11378" target="_blank">📅 12:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11377">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نامه زرشکیان به پاپ:  ما به راهکارهای دیپلماتیک برای حل و فصل مسائل، از جمله پرونده‌های اختلافی با آمریکا، پایبندیم و بعد برقراری امنیت، عبور از تنگه هرمز به حالت عادی بازخواهد گشت
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/11377" target="_blank">📅 11:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11376">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رویترز به نقل از یک منبع آگاه گزارش داد که متیاس گرافستروم، دبیرکل فیفا، امروز در استانبول با مقام‌های فدراسیون فوتبال ایران دیدار می‌کند و درباره حضور تیم ملی در جام جهانی ۲۰۲۶ «اطمینان خاطر» خواهد داد. این درحالی است که مهدی تاج پیش از این خواستار تضمین‌هایی از فیفا شده بود.
@withyashar</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/11376" target="_blank">📅 11:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11375">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کرملین امروز اعلام کرد که ولادیمیر پوتین، رئیس‌جمهور روسیه ۱۹ مه (۲۹ اردیبهشت) برای یک سفر دو روزه به چین خواهد رفت. این سفر در پی سفر دونالد ترامپ، رئیس‌جمهور آمریکا به پکن انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/11375" target="_blank">📅 11:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11374">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">چمران رئیس شورای شهر تهران:
رایگان اعلام کردن مترو و اتوبوس در تهران کار احساسی بود و فردا آخرین روز رایگان بودن حمل و نقل عمومی در تهران است و تمدید نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/withyashar/11374" target="_blank">📅 11:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11373">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شریعتمداری:
مذاکره به جای خود، اما جنگ بدون پاسخ پایان نمی‌یابد
/
با شهادت آقا شروع کردند بی‌انتقام تمام نمی‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/11373" target="_blank">📅 11:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11372">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کانال ۱۲ اسرائیل گزارش داد انتظار می‌رود دونالد ترامپ، رییس‌جمهوری آمریکا، طی ۲۴ ساعت آینده تیم مشاوران نزدیک خود را تشکیل دهد تا درباره ایران تصمیم نهایی بگیرد. برآوردها در اسرائیل حاکی است تصمیم درباره اقدام نظامی ممکن است بسیار به‌زودی اتخاذ شود.
برنامه تلویزیونی «اولپن شیشی» به نقل از یک مقام ارشد اسرائیلی گزارش داد که «ازسرگیری درگیری نزدیک است» و اسرائیل خود را برای احتمال «چند روز تا چند هفته جنگ» آماده می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/11372" target="_blank">📅 11:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11371">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qswIwrXNDZ32GsrOSx446M5vGYroHIaZ3hb46qj2R9uq9xhKhXHDmeJLLpDJPY92FzfL7xM-SqCBsoRhySTf9IrrXeAKfsKRc3iZyrAVWmqomN1uaKL9Z6sk4hwRzuTvVcByowZJKGdi5IGfZDZLOmPJim2rxCuznI49NCvSbrQNhJS-xuASQX5fzLrrUtaHRHOy4jxJB6mFRtA4bZsl9LVTPTVvNs0Zfuk6C1nzTRxlEXmGCmHShLRtYb1F0w9ni3GbIJFziUtYIAMnRTZbBa8ew5lsPqJrjUMFHqkn5pH52_NM8v4hcfImYynKLfmQYNzJSHOT-RIjuZZ-bloB-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری مشاور قالیباف تو اینستاگرام
🤣
@withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/11371" target="_blank">📅 11:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11370">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/11370" target="_blank">📅 05:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11369">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/11369" target="_blank">📅 05:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11368">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نیویورک تایمز از قول مقامات نظامی آمریکا:
اگر جزیره خارگ تصرف شود ، نیروهای زمینی برای حفظ آن لازم خواهند بود.
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/11368" target="_blank">📅 04:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11367">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561d76df7d.mp4?token=ijfZwJ9ELxGOYEdZXJjfabzYirzBJ9jdR8BTNGfcbyAhf_BY5Xn2kGpj8XtPcduPDfIxpZG1oUESZXY6jQYkmp3mDpVK0YZxtEyOAduD-4uJ3D4E-ITM8XdMxex7izKN99Ro42BzKe3koNh7SRPTJlYPS4XcAnmyBjFC6x6wnmff0N5SGPVINkppETtw83251IwDcVZQBptL8i_PkhK19dhvTr0eQXKF4C_fWYwlZxvQK7sc_yncmsrPkOe0Y9hKs3ouRXq0v139b_JGTnUmqpW7MUNIpbj1ro-iXzyz9ycSP7sUvkg-lq2OJ4A11fQH8pQTRmzDfWg07lXx1tKi_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561d76df7d.mp4?token=ijfZwJ9ELxGOYEdZXJjfabzYirzBJ9jdR8BTNGfcbyAhf_BY5Xn2kGpj8XtPcduPDfIxpZG1oUESZXY6jQYkmp3mDpVK0YZxtEyOAduD-4uJ3D4E-ITM8XdMxex7izKN99Ro42BzKe3koNh7SRPTJlYPS4XcAnmyBjFC6x6wnmff0N5SGPVINkppETtw83251IwDcVZQBptL8i_PkhK19dhvTr0eQXKF4C_fWYwlZxvQK7sc_yncmsrPkOe0Y9hKs3ouRXq0v139b_JGTnUmqpW7MUNIpbj1ro-iXzyz9ycSP7sUvkg-lq2OJ4A11fQH8pQTRmzDfWg07lXx1tKi_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها چیزی که می‌توانم بگویم این است که این یک موفقیت بزرگ بود.»
رئیس جمهور ترامپ پس از سفر به چین به کاخ سفید بازگشت و به خبرنگاران گفت: «ما به توافق‌های بزرگی رسیدیم» و این دیدار را یک لحظه تاریخی خواند.
سپس او به اتفاقات بیشتری در آینده اشاره کرد: «اتفاقات زیادی افتاده است و شما درباره آنها خواهید شنید.»
@withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/11367" target="_blank">📅 03:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11366">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ: افزایش قیمت‌ بنزین مرتبط با جنگ ایران «درد کوتاه‌مدت» است که بسیار کمتر از چیزی است که مردم انتظار داشتن.
وقتی به کسی میگید که باید کمی بیشتر برای بنزین در یک دوره بسیار کوتاه بپردازید، چون میخوایم جلوی تهدید تکه‌تکه شدن توسط یک دیوانه، یک فرد دیوانه رو بگیریم، و آنها دیوانه هستن با استفاده از سلاح‌های هسته‌ای، همه میگن که این خوب است.
@withyashar</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/11366" target="_blank">📅 03:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11365">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/11365" target="_blank">📅 03:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11364">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">صادق هدایت میگه دیگه
میگه اگه کارت با سر و کله زدن با ادماس میفهمی چه ملت شریف زبون نفهمی داریم</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/11364" target="_blank">📅 03:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11363">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83bfd5694a.mp4?token=BRiagJcpc-Kio3g1Jfb_kuH0COb5-auzQ_mgoXVbb3WnmLlQ3HcM1XEk2tLzxJjmIxc8PhzXWSPjPej220Z2MDHW0V9pV2Zj_tR1JXU6NMrd4LaNzmlG4Bnq04j8CDQRGiZ9sXyzA5XPfNERk6ZE8h508LbKvzYVEZ_NSqFJBCoewW-7pHwNCbylbqMDUVf70OYkbLPL8-ZNhn5S89RO0i1zEEoqtGREmle9xUFcicxSkXlHs8nXlkz6o3DrGRftfaHyMfq3SEWJeVFY3PXoVanoPKqIw8Wdi6FPxi2DoCA0_2JTR3ZVPRqhn8mEtCkxr-kcfWRGRXfgWM5nW4QaGYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83bfd5694a.mp4?token=BRiagJcpc-Kio3g1Jfb_kuH0COb5-auzQ_mgoXVbb3WnmLlQ3HcM1XEk2tLzxJjmIxc8PhzXWSPjPej220Z2MDHW0V9pV2Zj_tR1JXU6NMrd4LaNzmlG4Bnq04j8CDQRGiZ9sXyzA5XPfNERk6ZE8h508LbKvzYVEZ_NSqFJBCoewW-7pHwNCbylbqMDUVf70OYkbLPL8-ZNhn5S89RO0i1zEEoqtGREmle9xUFcicxSkXlHs8nXlkz6o3DrGRftfaHyMfq3SEWJeVFY3PXoVanoPKqIw8Wdi6FPxi2DoCA0_2JTR3ZVPRqhn8mEtCkxr-kcfWRGRXfgWM5nW4QaGYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اف‌بی‌آی ترامپ یک توطئه تروریستی بزرگ را که قرار بود توسط یک فرمانده شبه‌نظامی تحت حمایت ایران در خاک ایالات متحده، کانادا و اروپا انجام شود، خنثی کرده است.
محمد السعدی - رهبر کتائب حزب‌الله اسلام‌گرا - بیش از ۲۰ حمله را برنامه‌ریزی کرده بود. هدف او اماکن یهودی، از جمله یکی در نیویورک بود.
جان‌های بیشتری نجات یافت
«بنابراین او به اینجا آورده شد و امروز زودتر در دادگاه حاضر شد.»
می خواهم در مورد این عملیات محتاط باشم تا کسی را به خطر نیندازم، اما همین کافی است که بگویم این تلاشی بود که نه تنها اف‌بی‌آی، بلکه شرکای اجرای قانون ما در خارج از کشور را نیز شامل می‌شد.
@withyashar</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/11363" target="_blank">📅 02:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11361">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc0ddeea66.mp4?token=eUncpEdSgGeDuHVPNKRDOCdF5aopnfYc76HyHl7atsxjAvOE6-mnNO_dLB8VLZcHsVFf6shYiGxtL4N4JvyKeqveuCfZgA5oSpCVQOYTxPagETmz2GOqCVaNxUP_vjYsxXaswaWiue2_IjaPSidCPkj5qP-UfdBawrxg29mbp5dxbe9CAFD9AhmIR6lBOG7K9m5KT2vXOIXWFMnLV5lh8zpjggDajXow6t5jZIk0N19X6YsnZdFkVWkRYtSM4OTORs0hK89fk5NZfEIVOBuyIWh6AA981c9WP1J5NnL8zgP58U2ZEKYqfoEMeebFNoykaK_uTMcD5GZxMbPPe9HB6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc0ddeea66.mp4?token=eUncpEdSgGeDuHVPNKRDOCdF5aopnfYc76HyHl7atsxjAvOE6-mnNO_dLB8VLZcHsVFf6shYiGxtL4N4JvyKeqveuCfZgA5oSpCVQOYTxPagETmz2GOqCVaNxUP_vjYsxXaswaWiue2_IjaPSidCPkj5qP-UfdBawrxg29mbp5dxbe9CAFD9AhmIR6lBOG7K9m5KT2vXOIXWFMnLV5lh8zpjggDajXow6t5jZIk0N19X6YsnZdFkVWkRYtSM4OTORs0hK89fk5NZfEIVOBuyIWh6AA981c9WP1J5NnL8zgP58U2ZEKYqfoEMeebFNoykaK_uTMcD5GZxMbPPe9HB6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما ۹ تا دوربین مختلف  در فضا روی سایت هسته ای ایران داریم
می‌تونیم اسم طرف رو هم بخونیم
مثلاً اگه اسمش محمد باشه، ‌که خب بیشترشون محمدن، تقریباً می‌تونیم حدس بزنیم که حدود ۵۰٪ اطلاعاتش درست در میاد
@withyashar</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/11361" target="_blank">📅 02:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11360">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ : ویتنام ۱۹ سال طول کشید، عراق حدود ۱۰ سال، کره ۷ سال، یکی دیگه ۱۴ سال، یکی ۱۲ سال، یکی هم ۹ سال
- ما فقط دو ماه و نیم اونجا بودیم
- چین هم این هفته سه تا نفتکش پر از نفت ایران رو برد، چون ما اجازه دادیم این اتفاق بیفته،شما اجازه دادید
@withyashar</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/11360" target="_blank">📅 02:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11359">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac35dbd92.mp4?token=Na_H5fkANLeth3QRqJpSr3jVVBdAPHJnHA6QokAPOgFxCaU_u2gDuX9fCHjtKQ1Wqma2yN9xK5LAfIuxlK8GZnusphXKOLkp6kZXKFTuFHQg1_c_UWXHOPQq6ml_4REGySYOMdrJIMQD237XruOVvJL6YifdH_COoZgQuiM6Ufs4gS9e2bO26gjRkxB-d14XbVgpy8GZuu8nW8FThZ-wGrVXDi7iAt5O57TRUHj69fa0XV9AyK_G7Q9lXVKP3iFDYltYFDPdOGdM_sfkRUSsgVbrIJMmBq53LyAFi03sWfu1lM0jBANsGfJ2BWyR7FDHR2UrigC252MpQExqvrJ3Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac35dbd92.mp4?token=Na_H5fkANLeth3QRqJpSr3jVVBdAPHJnHA6QokAPOgFxCaU_u2gDuX9fCHjtKQ1Wqma2yN9xK5LAfIuxlK8GZnusphXKOLkp6kZXKFTuFHQg1_c_UWXHOPQq6ml_4REGySYOMdrJIMQD237XruOVvJL6YifdH_COoZgQuiM6Ufs4gS9e2bO26gjRkxB-d14XbVgpy8GZuu8nW8FThZ-wGrVXDi7iAt5O57TRUHj69fa0XV9AyK_G7Q9lXVKP3iFDYltYFDPdOGdM_sfkRUSsgVbrIJMmBq53LyAFi03sWfu1lM0jBANsGfJ2BWyR7FDHR2UrigC252MpQExqvrJ3Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجریان صداوسیما برداشتن یه تصویر هوش مصنوعی رو گذاشتن و دارن تحلیلش میکنن!
😂
😂
@withyashar</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/11359" target="_blank">📅 01:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11358">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فقط حال من رو فروشنده های بازار که با مردم سر و کله میززند و جماعت زبون نفهم و میبینند درک میکنند</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/withyashar/11358" target="_blank">📅 01:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11356">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer"><a href="https://t.me/withyashar/11356" target="_blank">📅 01:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11355">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/11355" target="_blank">📅 01:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11354">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نیویورک تایمز به نقل از مقامات آمریکا:
دستیاران ترامپ برنامه‌هایی رو برای بازگشت به حملات نظامی به ایران آماده کردن، اگر او تصمیم بگیره با بمباران بیشتر از بن بست خارج بشه.
از جمله گزینه‌ها، اعزام نیروهای ویژه به ایران برای هدف قرار دادن مواد هسته‌ای مدفون شده است و ممکنه از نیروهای ویژه برای کنترل جزیره خارک استفاده بشه.
@withyashar</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/withyashar/11354" target="_blank">📅 01:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11353">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVjBLV02uWxkpjdspvM1yQcFJFrD2tTkWrvF4wucb4I1DbG940N6OrYv-HwGG1X0tY8fFv2ZJdbzNG2M_Iq9bnqOIbo1qmffDUqGKoYil5dHTxNQvJXeIliJvtgspplPwAt5DKYGU1ARZLnl-NXXkxQa4OwyfkmvgwgU0E2M0L-H5wzWRVeESmfdxeruR89ttOfFPYY7fWQO-CF4SfZHGItyiY2CfHJaJuHz2M7qWsqTgn5qpr2U350JJq_wwkPpx0V-FjqLJ-gQrgg6zm04hZjssNScnsUR-GQFIbgkHmakjaw8C30e74GT4-r-91bUClJoR1DZbXrcBCRIVtg5Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد جدید مجله تایم: چگونه دیدار ترامپ و شی، نظم نوین جهانی را نشان داد
@withyashar</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/11353" target="_blank">📅 01:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11352">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ خیلی عجله داشته هیچ فیلمی عکسی از رسیدنش نیومده بیرون ! عجبیه</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/11352" target="_blank">📅 01:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11351">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db11d28292.mp4?token=d3oL1a2h9-BdRK_ruM97JT3Mhw-wDPnPk9ANA523kUCXqkcRcwvi0DfnmHy9W1QMILkdBNyYlaiOnzNdWHItL3c_vOIYbIkM8AaOfRx2QAxjXCLhvmvjTVbx8fMoaX4bChfvJeLoXGCykrHgKY3ZrFU7Nr7NmkalEtQns8r_k04IhKg4gcZTN8wXcO3kyjtg4LTze_UH5X8hX8W2lCLFjPVzwq4H1bNa_FIfa2OjY2ZFI4GWDRWaubzznTzD2MEGG73UyMVooWrGU09pG4Mt3xHAzsB0d42N2_E51kBnfR3E-I-6lgcLyAmPCeB8qjFXbMNuve0IEL327F8hZVwLwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db11d28292.mp4?token=d3oL1a2h9-BdRK_ruM97JT3Mhw-wDPnPk9ANA523kUCXqkcRcwvi0DfnmHy9W1QMILkdBNyYlaiOnzNdWHItL3c_vOIYbIkM8AaOfRx2QAxjXCLhvmvjTVbx8fMoaX4bChfvJeLoXGCykrHgKY3ZrFU7Nr7NmkalEtQns8r_k04IhKg4gcZTN8wXcO3kyjtg4LTze_UH5X8hX8W2lCLFjPVzwq4H1bNa_FIfa2OjY2ZFI4GWDRWaubzznTzD2MEGG73UyMVooWrGU09pG4Mt3xHAzsB0d42N2_E51kBnfR3E-I-6lgcLyAmPCeB8qjFXbMNuve0IEL327F8hZVwLwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/11351" target="_blank">📅 01:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11349">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ در تروث : تینا را آزاد کنید
@withyashar
تینا پیترز یک مقام انتخاباتی سابق آمریکاست که به‌خاطر دخالت غیرقانونی در سیستم‌های رأی‌گیری بعد از انتخابات 2020 زندانی شده و حالا ترامپ از او حمایت سیاسی می‌کند</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/11349" target="_blank">📅 00:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11348">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/11348" target="_blank">📅 00:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11347">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/11347" target="_blank">📅 00:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11346">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/11346" target="_blank">📅 00:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11345">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نیویورک‌تایمز به نقل از ۲ مقام امنیتی:
آمریکا و اسرائیل در حال آماده‌سازی گسترده برای احتمال ازسرگیری حملات علیه جمهوری اسلامی هستند،
این حمله ممکن است از هفته آینده آغاز شود
@withyashar</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/11345" target="_blank">📅 00:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11344">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یه مسیج درست اگه تو دایرکت دیدی به من بگو ! انگار‌من کشیش کلیسام ! یا کلانتر محل !</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/11344" target="_blank">📅 00:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11342">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">امشب حمله‌ست؟</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/11342" target="_blank">📅 00:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11341">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSea</strong></div>
<div class="tg-text">امشب حمله‌ست؟</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/11341" target="_blank">📅 00:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11340">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBnlnEqGSs356aCiVbK7iLm9euYtgmiwg0XbVzYFsXDXFD_OJEsNMU57Mv2eQEqrx_OMHWGhYvZNKTSrkfrxhFcph1x5kx8WhEs7PFeETnblKacGv6FMy45Y7_fSnBDFMIH-C0riekrSQ6lZT19WYr332n6Ag7hU-EFnMjkLPeVkvy9hN2RCGOpCA13QsZDPUVEpljWECq1N4vAbj1qK7nTF-Eoo7tp_YCQvMiTH5UD-EmivYVq-J_HggARoeH2uWFJyvbLtOO5xQ5lzJ8mpz-rfNUs00sgEwcOnr3MCcC7YyWEzYbIvChBLrgxyaADdqVeszd8WXrN2i7ZqQoJi-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما هم میدونه چی میشه داره آموزش کار با سلاح رو میده
😂
اینا رفتنین شک نکنید
👋🏾
👋🏾
@withyashar</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/withyashar/11340" target="_blank">📅 00:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11339">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اگه امشب شب‌زیبایی‌نبود و امید نبود الان رد میدادم ! با این پیغام هایی که دایرکت میاد</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/11339" target="_blank">📅 00:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11338">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM</strong></div>
<div class="tg-text">عمو یاشار ما امشب منتظر اومدم اومدمیم
😂
🫡</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/11338" target="_blank">📅 00:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11337">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یاشار یچی خواستم بگم روم نشد ولی کلاهبرداریه اگه امکانش بود اطلاع رسانی کن  ما پیوی ینفر رفتیم برامون خاله جور کنه واسه معرفی ۲۰۰ از ما گرفت بعد شماره طرفو داد گفت یک میلیون ۳۰۰ دیه برامون بزن گرفتیم براش زدیم بعد اومد گفت برای تضمین ۱۳ میلیون بزنید بعد اینکه…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/11337" target="_blank">📅 00:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11336">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahd</strong></div>
<div class="tg-text">یاشار یچی خواستم بگم روم نشد ولی کلاهبرداریه اگه امکانش بود اطلاع رسانی کن
ما پیوی ینفر رفتیم برامون خاله جور کنه واسه معرفی ۲۰۰ از ما گرفت بعد شماره طرفو داد گفت یک میلیون ۳۰۰ دیه برامون بزن گرفتیم براش زدیم بعد اومد گفت برای تضمین ۱۳ میلیون بزنید بعد اینکه کارتون تموم شد برش میگردونم حالا ما بهش گفتیم ۱۳ میلیون از کجا بیارم گفتم کنسلش کن ۱۳۰۰ بهمون برگردون اومده میگه اون مهریه بوده دیگه میره برا خالهه
ولله به این پفیوزا اعتماد نکنید اگه امکانش هست بزار چنلت بقیه هم در جریان باشن</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/11336" target="_blank">📅 00:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11335">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ رسید آمریکا
@withyashar</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/11335" target="_blank">📅 23:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11334">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نیویورک تایمز: آمریکا محمد بکر سعید داود السعدی، فرمانده ارشد شبه‌نظامی گردان‌های حزب‌الله درعراق، رو دستگیر کرد و علیه‌اش کیفرخواست صادر کرد.
او متهم به طراحی حداقل 18 حمله در اروپا، آمریکا و کانادا از پایان فوریه شده؛ این حملات به عنوان انتقام از حملات آمریکا و اسرائیل علیه جمهوری اسلامی برنامه‌ریزی شده بودن.
@withyashar</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/11334" target="_blank">📅 23:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11333">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7f890274.mp4?token=mvAcIpX7SIiaJOkiL6eBdMkAOYg0yECTYkBsYAy0pSI0l8jomsRHJKGKK28zvfJpcneDkWdZJUx9x968JDPMreCSUweL-2_4wmtlnTa44k3z7IjIaZRe7E0EY03ECTcKVyiRf_9NtQGIrYMjgIBKs1HAju-17rjjCiWiLnmihj7bOObuZNyNdg6vcWD80JnPCCTxT5I5jxPsEerX8MmLIGsYDjba_H_bkxZtQ7DaxftIxgu0QaZdGsJJK-O2c1rWn85GFowqKOtThriuJivEkHD0kIMo7ic2joaF7pHCFTAdXfR0ccoEbYUot0zR6J50nRUWITXP561B07Nq6n5qxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7f890274.mp4?token=mvAcIpX7SIiaJOkiL6eBdMkAOYg0yECTYkBsYAy0pSI0l8jomsRHJKGKK28zvfJpcneDkWdZJUx9x968JDPMreCSUweL-2_4wmtlnTa44k3z7IjIaZRe7E0EY03ECTcKVyiRf_9NtQGIrYMjgIBKs1HAju-17rjjCiWiLnmihj7bOObuZNyNdg6vcWD80JnPCCTxT5I5jxPsEerX8MmLIGsYDjba_H_bkxZtQ7DaxftIxgu0QaZdGsJJK-O2c1rWn85GFowqKOtThriuJivEkHD0kIMo7ic2joaF7pHCFTAdXfR0ccoEbYUot0zR6J50nRUWITXP561B07Nq6n5qxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه خداحافظی ترامپ با شی و خوشحالی او از سفر موفقیت آمیزش
@withyashar</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/11333" target="_blank">📅 23:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11332">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7aab5fc3.mp4?token=i_3kTBJd2iajWUgJIRkbyvDtlyAQkXEegJpes_DgxTFnAFUMT4CXlMX66Sm-irk-8TgX9PpuO3WnRZClrV8vlZvk21QcVmafKCTMvn-DGGz00DUvX-p_ygDc6wtHDU91ymDRmVGJ6E9rodgQSWcja44aEv0UUiLPOmj12G4cR6RjLFO5FbPZi4AyN-kS6qLMnFRD8mSDg_GI3oGX_b1wgnuVKF_FgCIIF2X-JBSJwk32abq5D4lcAJtdF-y5UMmbRf0igMR-w-cq45cdMKbsnmLTbxO74i6E5ehKM1zwnbmXwriLWG2-VqfZBNWbezRbpw3kqAx_h0Qwtj0a5PljEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7aab5fc3.mp4?token=i_3kTBJd2iajWUgJIRkbyvDtlyAQkXEegJpes_DgxTFnAFUMT4CXlMX66Sm-irk-8TgX9PpuO3WnRZClrV8vlZvk21QcVmafKCTMvn-DGGz00DUvX-p_ygDc6wtHDU91ymDRmVGJ6E9rodgQSWcja44aEv0UUiLPOmj12G4cR6RjLFO5FbPZi4AyN-kS6qLMnFRD8mSDg_GI3oGX_b1wgnuVKF_FgCIIF2X-JBSJwk32abq5D4lcAJtdF-y5UMmbRf0igMR-w-cq45cdMKbsnmLTbxO74i6E5ehKM1zwnbmXwriLWG2-VqfZBNWbezRbpw3kqAx_h0Qwtj0a5PljEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مایک والتز، سفیر آمریکا در سازمان ملل ، می‌گوید که یکی از «نتایج بزرگ» سفر ترامپ به چین این بود که چین موافقت کرده از ایران فاصله بگیرد.
@withyashar</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/11332" target="_blank">📅 23:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11331">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">منابع عبری :
گویا ترامپ با یک حمله محدود جهت فشار بر سر تسلیم شدن موافقت کرده است
@withyashar</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/11331" target="_blank">📅 23:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11330">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">واشنگتن پست: جمهوری اسلامی واضح‌ترین بازنده دیدار ترامپ از پکن است، با مخالفت علنی پکن با اختلال در هرمز، تعهد به عدم ارسال تجهیزات نظامی به تهران و توافق بر اینکه تنگه «باید باز بماند.»
@withyashar</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/11330" target="_blank">📅 23:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11328">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">l وزارت خارجه آمریکا اعلام کرد آتش‌بس میان لبنان و اسرائیل به مدت ۴۵ روز دیگر تمدید شد.
@withyashar</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/11328" target="_blank">📅 22:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11327">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/11327" target="_blank">📅 22:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11326">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed7b9efa.mp4?token=tLp-Gl-M373MRh8lO8qeeW_Vf1ZPKNDzgFwTypdfcwxDCUh3-LOGsOLuoQfNDIZ4foupgY6RQPxd6zZDAbCdXjPVyM3DndFKSVyQC9Ax7P7bGthl0kwLTYVgW59A-L3F4D36jgqSaqNVfobL52P0LwFRmOpBY08AO7JRh53eqUTjztvGCuuq0uEMLffy04jjjahg0bNZACRwLGZR_DMyUw8Sp7Q-1F-ZNWVe4cBLiqJIk1hiz8MAKz1YkNeXz57qPk0YjEiSUuJ3aLv4nXBsbFyQd6VSHCSyi23n5A6lyOj771i-hpBW4xyYyoY0CJg0SJjKlBkszFPay_ZlKZ7sjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed7b9efa.mp4?token=tLp-Gl-M373MRh8lO8qeeW_Vf1ZPKNDzgFwTypdfcwxDCUh3-LOGsOLuoQfNDIZ4foupgY6RQPxd6zZDAbCdXjPVyM3DndFKSVyQC9Ax7P7bGthl0kwLTYVgW59A-L3F4D36jgqSaqNVfobL52P0LwFRmOpBY08AO7JRh53eqUTjztvGCuuq0uEMLffy04jjjahg0bNZACRwLGZR_DMyUw8Sp7Q-1F-ZNWVe4cBLiqJIk1hiz8MAKz1YkNeXz57qPk0YjEiSUuJ3aLv4nXBsbFyQd6VSHCSyi23n5A6lyOj771i-hpBW4xyYyoY0CJg0SJjKlBkszFPay_ZlKZ7sjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/11326" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
