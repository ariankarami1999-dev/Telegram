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
<img src="https://cdn4.telesco.pe/file/laffSY4yuB4hVz9J6dYcC2n365dmzAYqNKWIc3h2D1JSs-pWvsudktTYEZ_te1fdZOJfPBTIh3c2aek583FBi960ZI4Al61SqmZQJToiZhNXgZucqtkk3tkbf3Q-ZmP6iHcP4VhPB851UL_Qhjmu6jvNbL6__CD3Ev7IEyXq6krkdRGr8G76OMoCr_-9oni1LEu_7LEMPEpgxkulVajJ_cJ_SeL0mLhnn3V_acSLZxs_Al1D4pis5hQp7sa61O--xpwyKNNTgfw7BcsN5aSDerEvLxUyUtkXMA5r-aQy9Genbi860VH27LqCXrGpR7bthJvwIh8Fz54CLTiCI_BAXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 05:08:07</div>
<hr>

<div class="tg-post" id="msg-17092">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">منبع اسرائیلی:   ما به حمله پاسخ خواهیم داد، حتی اگر در بازه زمانی فوری اتفاق نیفتد.</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SBoxxx/17092" target="_blank">📅 03:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17091">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کارت نابودی حزب الله را سوزاندند تا کارت باز کردن تنگه هرمز را نگه دارند.</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/SBoxxx/17091" target="_blank">📅 02:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17090">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ: «حملات ایران هیچ  تأثیری بر توافق ندارد. ما قرار است یک توافق بزرگ انجام دهیم»</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/SBoxxx/17090" target="_blank">📅 02:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17089">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ از نتانیاهو خواست «چند روز» صبر کند تا ببیند آیا می‌توان با ایران به توافق رسید –</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/SBoxxx/17089" target="_blank">📅 02:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17088">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اگر تعداد موشک ها اندک باشد عملا همان حمله فرمالیته است</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SBoxxx/17088" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17087">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ایران پیامی به اسرائیل مخابره کرده و اعلام کرده است که موج جدید حملات خود را به پایان رسیده تلقی می‌کند و قصد انجام حملات بیشتری را ندارد، مگر اینکه اسرائیل حملات جدیدی را آغاز کند.  — کانال ۱۳ اسرائیل</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SBoxxx/17087" target="_blank">📅 01:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17086">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c631c9b1.mp4?token=oa9MhXzXz1DlL37orbQ6UjjwVc-2shkyFiq2SIen5xvzlFX81mAWdWbKrSlFwM4HF2DryczSxRPYhlC-ZvrIPuIEOKyiTCMIVZ0_c_LfyVc1oAPk5sKu-CUH_YYHEP4oa8YH2FJ8wpqw3i6xCQmNGuUPxFHu1toyruy7LODuPzxTV2baKMNhlmmDFsMUEiII_CKci7OMxIkNZ6yXaWg3BjGp8F1SA8-3Ttlr8ISsEzyRR52l8fIyN8_nUkHc-tam6JJCaaJlPjO99ITO4NcL8fAUCxzjCWdBT97zu6YPnuwpj1K6hw6vjRnYLn9-p_NgJ1lvDIB2jm7rCaVLq_WM-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c631c9b1.mp4?token=oa9MhXzXz1DlL37orbQ6UjjwVc-2shkyFiq2SIen5xvzlFX81mAWdWbKrSlFwM4HF2DryczSxRPYhlC-ZvrIPuIEOKyiTCMIVZ0_c_LfyVc1oAPk5sKu-CUH_YYHEP4oa8YH2FJ8wpqw3i6xCQmNGuUPxFHu1toyruy7LODuPzxTV2baKMNhlmmDFsMUEiII_CKci7OMxIkNZ6yXaWg3BjGp8F1SA8-3Ttlr8ISsEzyRR52l8fIyN8_nUkHc-tam6JJCaaJlPjO99ITO4NcL8fAUCxzjCWdBT97zu6YPnuwpj1K6hw6vjRnYLn9-p_NgJ1lvDIB2jm7rCaVLq_WM-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقامات عربی به کانال ۱۳ اسرائیل:  «تلاش‌هایی برای جلوگیری از جنگ بزرگ‌مقیاس جدید در جریان است.  در حال حاضر تشدید درگیری‌ها پیش‌بینی نمی‌شود. ما برای جلوگیری از هرگونه بدتر شدن وضعیت با ایالات متحده در تماس هستیم».</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SBoxxx/17086" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17085">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مقامات عربی به کانال ۱۳ اسرائیل:
«تلاش‌هایی برای جلوگیری از جنگ بزرگ‌مقیاس جدید در جریان است.
در حال حاضر تشدید درگیری‌ها پیش‌بینی نمی‌شود. ما برای جلوگیری از هرگونه بدتر شدن وضعیت با ایالات متحده در تماس هستیم».</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SBoxxx/17085" target="_blank">📅 01:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17084">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سپاه پاسداران:    عملیات امشب صرفا یک اعلام اخطار بود و در صورت تکرار تجاوزات پاسخ‌ها گسترده‌تر خواهد بود و تمام اهداف آمریکایی-صهیونیستی در منطقه را در بر خواهد گرفت.</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SBoxxx/17084" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17083">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یک مقام ارشد اسرائیلی  گفت: «پاسخ مورد انتظار به ایران شدید و گسترده خواهد بود».</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SBoxxx/17083" target="_blank">📅 01:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17082">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل، عیال زامیر:  «به محض دریافت چراغ سبز، ضربه‌ای سنگین به دشمن وارد خواهیم کرد».</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SBoxxx/17082" target="_blank">📅 01:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17081">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتانیاهو ترامپ را از قصد  اسرائیل برای انجام یک «حمله عظیم» به ایران آگاه کرد و ترامپ تأکید کرد که ایالات متحده در آن مشارکت نخواهدداشت</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SBoxxx/17081" target="_blank">📅 01:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17080">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ به اکسیوس گفت:  «همین حالا با نتانیاهو تماس می‌گیرم و به او می‌گویم که در پاسخ به ایران حمله نکند».</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/17080" target="_blank">📅 01:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17079">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل، عیال زامیر:
«به محض دریافت چراغ سبز، ضربه‌ای سنگین به دشمن وارد خواهیم کرد».</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/17079" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17078">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ به اکسیوس گفت:  «همین حالا با نتانیاهو تماس می‌گیرم و به او می‌گویم که در پاسخ به ایران حمله نکند».</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/17078" target="_blank">📅 23:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17077">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhWVzZEUoBDgXJLbkWjI2oWBtJxIWUI-a_TMTlJUWrtbAFsrhFmiH4k7F9gYr_dI9gA1VM2OiAE2bEeYbiREKUgeqFjVMeiynFtpT2XIcOvVMSl9ac6_9Jd2nBeL2lwGDSy1F9F-8-VEM7BWp4g-acLIQtQHMK4F425Cw1sdWhcb6rmUoC0rSpyhx3jw-lI0J-mE71wIpdDaAZrLGSDTd_Yb_lFy2Tf8qMmDt0pfZaNIV2mdNGXl71dHJC1sFIfveqNwmyTRp4fdRdsvJTJJFQ0ntUnGITSODfd1FszlH4RXYfhmadUy0ft0kvzpdvXqZbz_mkM1lYtpMtoUWNl9Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست حاج عباس</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/17077" target="_blank">📅 23:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17076">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دونالدک نازنین؛ حافظ ایران زمین !</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/17076" target="_blank">📅 23:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17075">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دونالدک نازنین؛ حافظ ایران زمین !</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/17075" target="_blank">📅 23:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17074">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">— مقامات اسرائیلی به سی‌ان‌ان گفتند:  «اسرائیل در حال آماده‌سازی یک پاسخ قدرتمند به شلیک موشک‌های بالستیک ایران است».</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/17074" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17073">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">— مقامات اسرائیلی به سی‌ان‌ان گفتند:
«اسرائیل در حال آماده‌سازی یک پاسخ قدرتمند به شلیک موشک‌های بالستیک ایران است».</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/17073" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17072">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت که حملات اسرائیل به ضاحیه بیروت امروز صبح با هماهنگی آمریکا نبوده و افزود که «او از این موضوع خوشحال نیست.»</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/17072" target="_blank">📅 23:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17071">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سخنگوی ارتش اسرائیل:  نیروی هوایی تاکنون تمام موشک‌های شلیک شده از ایران را رهگیری کرده است.  ارتش اسرائیل اکنون موشک‌های شلیک شده دیگری را به سمت اسرائیل شناسایی کرده است.  سامانه پدافند هوایی به طور مداوم تهدیدات را شناسایی و رهگیری می‌کند.</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/17071" target="_blank">📅 23:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17070">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ به فاکس نیوز:  پیشنهاد من به ایران این است: موشک‌هایتان را شلیک کرده‌اید، کافی است. به میز مذاکره بازگردید و معامله‌ای انجام دهید.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/17070" target="_blank">📅 23:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17069">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پیشنهاد من هم همین است.</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/17069" target="_blank">📅 23:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17068">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ به فاکس نیوز:  پیشنهاد من به ایران این است: موشک‌هایتان را شلیک کرده‌اید، کافی است. به میز مذاکره بازگردید و معامله‌ای انجام دهید.</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/17068" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17067">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ به فاکس نیوز:
پیشنهاد من به ایران این است: موشک‌هایتان را شلیک کرده‌اید، کافی است. به میز مذاکره بازگردید و معامله‌ای انجام دهید.</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/17067" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17066">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گزارش‌های اولیه از انفجارها در تبریز.</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/17066" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17065">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سپاه پاسداران:    عملیات امشب صرفا یک اعلام اخطار بود و در صورت تکرار تجاوزات پاسخ‌ها گسترده‌تر خواهد بود و تمام اهداف آمریکایی-صهیونیستی در منطقه را در بر خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17065" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17064">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سپاه پاسداران:    عملیات امشب صرفا یک اعلام اخطار بود و در صورت تکرار تجاوزات پاسخ‌ها گسترده‌تر خواهد بود و تمام اهداف آمریکایی-صهیونیستی در منطقه را در بر خواهد گرفت.</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/17064" target="_blank">📅 23:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17063">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اگر تعداد موشک ها اندک باشد عملا همان حمله فرمالیته است</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17063" target="_blank">📅 23:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17062">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پرواز جنگنده های اسراییلی به سمت ایران</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17062" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17061">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">امروز آتش بس ۶۰ روزه هم‌ تمام می‌شد</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17061" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17060">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سخنگوی ارتش اسرائیل:
نیروی هوایی تاکنون تمام موشک‌های شلیک شده از ایران را رهگیری کرده است.
ارتش اسرائیل اکنون موشک‌های شلیک شده دیگری را به سمت اسرائیل شناسایی کرده است.
سامانه پدافند هوایی به طور مداوم تهدیدات را شناسایی و رهگیری می‌کند.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17060" target="_blank">📅 23:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17059">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اسرائیل در تلاش برای کسب تأیید برای حملات به زیرساخت‌های انرژی ایران، در تماس دائمی با ایالات متحده است.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17059" target="_blank">📅 23:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17058">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پرواز جنگنده های اسراییلی به سمت ایران</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/17058" target="_blank">📅 23:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17057">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">موج دوم حملات از ایران به سمت شمال اسراییل</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17057" target="_blank">📅 22:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17056">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8cFogUc6ub-KWdlUGvSkqkvbY5HNP5Bt7rwlvysRJPt1qeCu61d6W5abidrGzDmNmnlGf30G-CrIfFxSSFayJjlA9xrkqH_KLRQP71ivLodN2G49waVprM-tFxFD3OGDtnyq0WIWu68-jhO2x9Em0iTo4Rk9VI_9g9pz-eDF-Uh47WwllK4JRjM3N_sPOEZyaH9qlugfUE2DPzjcPcQUh-wY_zaka8sw3gPhN-zcagUVp8EZSIDQ0oxraHn2RIzkSRrJcZt01QDoZujdZzpVpomKSmyLRn1uJ5LwRC18_6SeR7fO7aAj42x829ZkRxYnuWF_smTeHmXN7256-0Cog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست حاج عباس</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17056" target="_blank">📅 22:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17055">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به رادیو ارتش گفت:  «شلیک‌ها از سوی ایران به سمت اسرائیل به معنای اعلام تجدید جنگ است».</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/17055" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17054">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزیر امنیت ملی اسراییل ، ایتامار بن گویر:
امشب تهران باید بسوزد!</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17054" target="_blank">📅 22:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17053">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">موج دوم حملات از ایران به سمت شمال اسراییل</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17053" target="_blank">📅 22:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17052">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تمام موشک‌های شلیک شده از ایران رهگیری شدند</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17052" target="_blank">📅 22:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17051">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به رادیو ارتش گفت:  «شلیک‌ها از سوی ایران به سمت اسرائیل به معنای اعلام تجدید جنگ است».</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17051" target="_blank">📅 22:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17050">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به رادیو ارتش گفت:  «شلیک‌ها از سوی ایران به سمت اسرائیل به معنای اعلام تجدید جنگ است».</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17050" target="_blank">📅 22:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17049">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پرتاب موشک بالستیک به سمت شمال اسرائیل، حیفا.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17049" target="_blank">📅 22:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17048">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پرتاب موشک بالستیک به سمت شمال اسرائیل، حیفا.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17048" target="_blank">📅 22:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17047">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">غریب‌آبادی، معاون وزیر خارجه ایران، در واکنش به گزارش‌هایی مبنی بر استفاده آمریکا از دارایی‌های ایران برای جبران خسارات جنگی به متحدان منطقه‌ای:   دولت‌های منطقه در موقعیتی نیستند که غرامت مطالبه کنند</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17047" target="_blank">📅 21:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17046">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بازسازی کشورهای عربی با پول بلوکه شده ایران!  رویترز: واشنگتن دارایی‌های مسدود شده ایران را برای حمایت از بازسازی و تعمیر خسارات در اختیار متحدان خود قرار خواهد داد.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17046" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17045">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ایران با صدور هشدار نوتام آسمان خود را  بست</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/17045" target="_blank">📅 21:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17044">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17044" target="_blank">📅 19:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17043">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">قطر یک اطلاعیه صادر کرده است که پروازها را از طریق فضای هوایی خود بازگردانی می‌کند و مسیرهای جایگزین برای هواپیماهای در حال حرکت از دوحه و فرودگاه‌های عربستان سعودی ارائه می‌دهد.
این دستور که از ۷ تا ۱۴ ژوئن اجرایی می‌شود.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17043" target="_blank">📅 19:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17042">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">این رسانه گفته می شد تحت مدیریت شمخانی است.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17042" target="_blank">📅 19:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17041">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIfYSpFQSSCbZN4OmHR3r9MzbFQoGtM3WtlAyR5hWyqtIbrGKjqW2kAN2pPfAUEYdPhvbqkSzr0e8sRCzGvfIoqsAqjAzCtSjO-IEfJzXxNep2M8OQw8D1POVpyw8A4klShl67bVayXlXCEeD0XxYgIDKfIX9xiz7MTRnzekUAsM9BjeueEtWY_eBo3h1zYrs_WLltOEG5z5XPOA3mjeGkkvmSPSuahVaafcL1g2_TzYCnhKWc03_l-4nNp85G3_bRLT_u90phAT7DkJVIp2_rbgUUs5QQ_QAnLhBeJ9I5GGsTs_yN8ECijCyhdnRERU1LbOLMXKnG90rfzGDcqY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17041" target="_blank">📅 19:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17040">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجنگاوران</strong></div>
<div class="tg-text">🔸
آمریکا، قدرت اول نظامی جهان نتوانست...
امروز تحلیل‌گر های زیادی هستند که حرف هایشان را با این جمله که آمریکا با این همه ادعا و قدرت نظامی نتوانست اینکار و آنکار را بکند شروع می‌کنند و بر مبنای این گزاره شروع به توهم زنی می‌کنند.
مثل همیشه، شیطان در جزئیات است و مشکل آدم های ساده لوح و متوهم بی توجهی به جزئیات.
خیلی کار ها هست که آمریکا می‌تواند انجام بدهد اما انجام آن ها هزینه هایی دارد که صرفا در محاسبه هزینه و فایده، برای آن ها نمیصرفد.
باز کردن تنگه هرمز یکی از این کار ها است، فایده ی باز شدن تنگه فعلا برای آمریکایی ها به هزینه اقدام نظامی نمی‌صرفد. اینکه برخی، بسته شدن تنگه را نشانه ظهور قدرت دریایی ایران و تغییر معادلات جهانی عنوان می‌کنند، توهمی است که به راحتی می‌تواند باعث هزینه بیشتر برای کشور بشود، چرا که اگر باعث اقدام های جسورانه و افزایش هزینه برای انفعال آمریکا بشود، باعث تغییر در محاسبه ضرر/فایده و حمله مجدد به ایران می‌شود (البته که در قضیه تنگه هرمز آمریکا منفعل نشده و رویکرد هوشمندانه و بدون هزینه ای را پیش گرفته است).
این مسئله درخصوص تغییر رژیم نیز صادق است. خیلی ها دوست داشتند هزینه ای پرداخت نکنند و «عمو ترامپ» و آمریکا همه هزینه های تغییر رژیم در ایران را پرداخت کنند. حالا هرچقدر هم که برایشان توضیح بدهی که در تاریخ سابقه نداشته است که با حمله هوایی رژیمی تغییر کند و  حمله زمینی به ایران هم جزو گزینه ها نیست، بازهم آنچه دوست داشتند را باور می‌کردند و امروز که نتیجه را دیدیم، برخیشان می‌گویند آمریکا قدرت کافی نداشته است!</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17040" target="_blank">📅 18:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17039">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">به حمله رژیم صهیونیستی به ضاحیه پاسخ دردآور خواهیم داد  سخنگوی کمیسیون امنیت ملی مجلس: امشب به آسمان سرزمین‌های اشغالی نگاه کنید.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17039" target="_blank">📅 18:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17038">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تشکیل جلسه فوری شورای عالی امنیت ملی ایران</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17038" target="_blank">📅 18:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17037">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تشکیل جلسه فوری شورای عالی امنیت ملی ایران</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17037" target="_blank">📅 17:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17036">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ:   رهبری جدید ایران منطقی‌تر و باهوش‌تر است و (آیت‌الله) مجتبی خامنه‌ای بخشی از روند تصویب توافق شده است  اگر رهبر ایران بخواهد، من آماده‌ام که مستقیماً با او صحبت کنم، اما هنوز مستقیماً با او صحبت نکرده‌ام.  من این جنگ‌های بی‌پایان را دوست ندارم، و…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17036" target="_blank">📅 17:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17035">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">امروز اسراییل به ساختمانی در ضاحیه بیروت حمله هوایی انجام داد که گفته می شود تا ۵ کشته در پی داشته است.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17035" target="_blank">📅 17:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17034">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فوری | ترامپ به ان‌بی‌سی:   من محاصره دریایی ایران را جنگ نمی‌دانم، اما هر کسی که می‌خواهد آن را جنگ توصیف کند، انتظار دارم بتواند این کار را انجام دهد.  ایران روزی ۴۰۰ تا ۵۰۰ میلیون دلار بخاطر محاصره دریایی ما از دست می‌دهد .</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17034" target="_blank">📅 17:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17033">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فوری | ترامپ به ان‌بی‌سی:   دلیل اعمال محاصره دریایی بر ایران این است که آن‌ها سعی کردند محاصره‌ای اعمال کنند و اکنون ما محاصره‌ای بر آن‌ها اعمال کرده‌ایم.</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/17033" target="_blank">📅 17:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17032">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ:   اگر به توافقی دست نیابیم، ارتش ایران را بیش از پیش تضعیف خواهیم کرد تا نیروهای ما بتوانند با اطمینان و امنیت کامل، اورانیوم را در اختیار بگیرند!  هیچ پولی را آزاد نکرده و هیچ تحریمی را کاهش نمی دهیم!  لبنان بخشی از توافق نیست!</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17032" target="_blank">📅 17:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17031">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ:
اگر به توافقی دست نیابیم، ارتش ایران را بیش از پیش تضعیف خواهیم کرد تا نیروهای ما بتوانند با اطمینان و امنیت کامل، اورانیوم را در اختیار بگیرند!
هیچ پولی را آزاد نکرده و هیچ تحریمی را کاهش نمی دهیم!
لبنان بخشی از توافق نیست!</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SBoxxx/17031" target="_blank">📅 17:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17030">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ادعای رسانه اسراییلی: تعویق حمله به ضاحیه بیروت در پی مداخله آمریکا  سازمان رادیو و تلویزیون اسراییل  گزارش داد که طرح حمله نظامی به ضاحیه جنوبی بیروت به دلیل دخالت‌های طرف آمریکایی به تعویق افتاده است.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17030" target="_blank">📅 17:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17029">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سخنگوی وزارت خارجه و سخنگوی تیم مذاکره‌کننده اسماعیل بقایی در مصاحبه با سی‌ان‌ان:
ما چندین اختلاف نظر در مذاکرات داریم، که مسئله اصلی پذیرش حقوق ایران، از جمله حق غنی‌سازی، توسط ایالات متحده است.
از زمان اجرای آتش‌بس، آمریکایی‌ها چندین بار کشتی‌های تجاری ایرانی را در تنگه هرمز و آب‌های بین‌المللی هدف قرار داده‌اند.
وضعیت منطقه‌ای و آتش‌بس بسیار شکننده و خطرناک است و این وضعیت نتیجه رویکرد بی‌محابای ایالات متحده نسبت به منطقه و آتش‌بس است. نیروهای مسلح ایران با تمام قدرت به هر حمله‌ای پاسخ خواهند داد.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17029" target="_blank">📅 15:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17028">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">Secret Box
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/17028" target="_blank">📅 14:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17027">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnimTUsFRJn7I2IRk8e11wMsQIUcgrEuLvneD67HHmaFpGtcDD70GOUinzJoGN6F5MjZYlxRyzOUyFf8_sTDkQtEExyWnUr1bKmIRXTW-B3UJG7_v0kup4deBycB56aRtp9ZXbT2Rh99zPdRbymsEFM43zkqouhM9dzxjOhIUrlJGH6JkJUdCuR3KsxUhSU2KM1c3pH8-mkFVYPadz-3X2okoTIeQ1r-tWydG2T-6XV9CMohNEOquzTb2NyrN_cNYpV8nEl8FmFYnz3-PPjGElysoXHnLLVkymuZCW9Z3drYUb3lWfoSp2cfOMsdV4B8oC608_scyuAduoHr1is7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرانجام کتابی که وعده دادم درباره پیوند ژئوپولیتیک و بازارهای مالی ترجمه کنم، به چاپ رسید.
به نظرم در این شرایط که چندین جنگ همزمان در منطقه و جهان در جریان است و تنشهایی که میتواند بزودی تبدیل به جنگ های دیگری بشود، فقدان وجود یک دیدگاه تحلیلی چهارچوب بندی شده و متدیک به پویه های ژئوپولیتیکی منجر به ادراک نادرستی از بسیاری نوسانات بازاری شده و فرجامش افزایش میزان خطای تحلیلگران و معامله گران خواهدبود.
این کتاب را که پاسخی به این چالش است میتوانید
از اینجا سفارش داده و تهیه کنید.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17027" target="_blank">📅 14:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17026">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ3nSxOR7z17GgFjZKvhEbVW4fz16NycRUI2rkX8U_GJgtl0aYRAWoUnFwsA2Ln3mZ42gh0TmQwris12kyWf6HouIG2l5SpwzjqnA_LaM-zOBiKkh0O6svpjExJiUGbTq2w22AkySx3yDt13hATRX3KY-yFOGpcf7enKurHrio6A-6N5VBC_lrPanPlQ7gxo6yBn4rl_HF5lVkSnX3JhdA4NAgob2E7B2VB8kMKUxANq6j68Q80vI2xZDwlTNhTiGxtFUCSiwQ9xeAUaRuVnhKzRAp9NYP_V-nxwQhcoTpS4tKtdPvPMp3YH-dR3JTqTjZCqXrtVEs_3V31aU77A3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▪️
خبر این است: وزیر کشور پاکستان پیش وارد تهران شد  مایلم یکبار دیگر صراحتا هشدار بدهم که ابداً نباید حسن نیت داشتن پاکستان را پذیرفت؛ پاکستان یکی از فاسدترین کشورهای دنیاست که توسط یکی از فاسدترین نظامیان دنیا اداره میشود. نظامیانی که وابسته سعودی، آمریکا،…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/17026" target="_blank">📅 13:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17025">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دقت کنید که سنتکام می‌گوید که دوباره «سایتهای راداری نظارتی ساحلی ایرانی» را در گروک و قشم زده اند!  پیشتر اشاره شد چرا مهم است.</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/17025" target="_blank">📅 13:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17024">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بیانیه حماس در پی تیراندازی امروز ۲ تن از اعضایش در یک شهرک اسراییلی
«جنبش مقاومت اسلامی (حماس) عملیات تیراندازی قهرمانانه در مستعمره کوخاو یائیر، شمال قلقیلیه، و همچنین عملیات قبلی در تقاطع مستعمره افرات، جنوب بیت‌المقدس را تحسین می‌کند.
این دو عملیات در پاسخ به تهاجم مداوم اشغالگر به نوار غزه و سیاست‌های ادامه‌دار یهودی‌سازی، کشتارهای خارج از چارچوب قضایی، گسترش مستعمرات، بازرسی های بدنی و حملات علیه مردم فلسطینی در کرانه باختری و اورشلیم صورت گرفته است.
اشغالگر، هرچقدر هم در سرکوب و جنایات خود پیش برود، موفق به توقف موج مقاومت در کرانه باختری نخواهد شد. مردم ما مسیر پایداری و سرسختی را تا رسیدن به آزادی و بازیابی حقوق کامل خود ادامه خواهند داد.
ما در برابر تشدید سیاست‌های گسترش مستعمرات، مصادره زمین، کشتار، بازداشت، آوارگی و تروریسم مستعمره‌نشینان هشدار می‌دهیم. تأکید می‌کنیم که این جنایات امنیت یا ثباتی برای آن به ارمغان نخواهند آورد، بلکه منجر به تشدید بیشتر درگیری و مقاومت خواهند شد.
ما از جامعه بین‌المللی می‌خواهیم مسئولیت‌های خود را به عهده بگیرد، با جدیت برای توقف تروریسم اشغالگر علیه مردم و سرزمین ما تلاش کند، تهاجم آن را پایان دهد و رهبران جنایتکار آن را پاسخگو سازد.»</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17024" target="_blank">📅 13:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17023">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">زلنسکی: روسیه عمداً سایت ذخیره سوخت هسته‌ای را در حمله‌ای «بسیار شنیع» هدف قرار داد</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17023" target="_blank">📅 12:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17022">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">قطعی برق خانه‌ها از اواخر حرداد شروع خواهد شد  آرش نجفی، رئیس کمیسیون انرژی اتاق بازرگانی، صنایع، معادن و کشاورزی ایران: پیش‌بینی می‌شود که این روند از اواخر خرداد یا اوایل تیرماه آغاز شود و مردم ایران احتمالاً به مدت سه ماه با این شرایط درگیر خواهند بود که…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17022" target="_blank">📅 11:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17021">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXpDsrvQjPfoaNJV6al7QYwuQzQwIJNWLpT6yPLLM2E-Cq5onFPt109jXfW6bUwS_C-dpiKFY0-1fbPkLztA-Oi-LFodcWjfQke3sI5GPxJ3U85Kg24yU2iw54Lycu7Q5Q3gTZVypDeN78YkT8AKHIjX8eFcuOWz2JQFT3KCcj72tL5uwRLtqK4H5xOOMn7KP72u4fUh75rbp5LpwAwPDn6fuhLBzHDWAhOk_kEBl5XWRU6d5_aAUDuaHD_SMQsjjQSgwps5BdbXO05DXTAsJEE2P25mFmfMOyR1JDKklmgGJyG0MgMli4q-TQyZPGqpEGfiZf-_uKLU71sbOC8IKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فناوری_هوشمند،_جنگ_را_به_انتخابی_احمقانه‌تر_تبدیل_می‌کند.pdf</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17021" target="_blank">📅 10:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17020">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بازسازی کشورهای عربی با پول بلوکه شده ایران!  رویترز: واشنگتن دارایی‌های مسدود شده ایران را برای حمایت از بازسازی و تعمیر خسارات در اختیار متحدان خود قرار خواهد داد.</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/17020" target="_blank">📅 10:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17019">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOj8yxihRYWEDRFNIEVfbzIaoLAWDVGnW3e2UEwV20IT23Ded-3n5_L9XLeExb2a082VLJqTJxYzZ1LnGPPikmxZQ7VkD0EsZlYf7EODEswAfLAwI9k9K2fbUTyLP_UY-hp2ytymFUF2edZrWVwVJ8AZxKyVli_eWUKhx8XbFGx0AVn6Gh6nGGQVka9bCok4PYqdYW9TxsF73AdNd-F5tNwGJHKozkdzhC_FslxEIIvBZjBvIN2ct_CcgxonuCWF7aSBi1emMXuDPqw-73sFZNmUWhvrWPRdLAOE4wl3IsvbOh0BVOHWA2AXFyA9fVo-1sHMH8VLPHxKUzWVgxbxvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازسازی کشورهای عربی با پول بلوکه شده ایران!
رویترز: واشنگتن دارایی‌های مسدود شده ایران را برای حمایت از بازسازی و تعمیر خسارات در اختیار متحدان خود قرار خواهد داد.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/17019" target="_blank">📅 08:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17018">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش های اولیه از حمله آمریکا به مناطقی در جنوب کشور</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17018" target="_blank">📅 07:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17017">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش های اولیه از حمله آمریکا به مناطقی در جنوب کشور</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/17017" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17016">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">باراک راوید خبرنگار اکسیوس:   دو منبع آگاه به جزئیات به من گفتند که معاون برکنار شده‌ی رئیس موساد، یک سال پیش بودجه‌ای به مبلغ یک میلیارد شِکل (حدود ۳۵۰ میلیون دلار) و تیمی متشکل از صدها نفر برای پروژه‌ی سرنگونی حکومت ایران دریافت کرد!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/17016" target="_blank">📅 01:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17015">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تبدیل ایران به یک دولت شکست خورده (Failed State) پلن B اسراییلی ها بود که ثابتی نیز به همین اشاره می‌کند   پلن A اسراییل، تغییر رژیم و کمک به روی کار  آمدن یک دولت غربگرای حامی اسراییل بود که فعلا شکست خورده است.  در این صوتی طولانی که ۸ ساعت پیش از آغاز جنگ…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/17015" target="_blank">📅 01:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17014">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trLFt0HPd1QGc3wbbG-2EKXKePHzcQ4rc7QxSbkyrVJv3FffNxcdVyj9r5uHil4w85pac8vDQb6mgNDJ-6eN06A-doh8hd_sSKH6tXSEO5HHvqm_w_E-l_sroCt2JaTe-ElstM4Pw1F6jaSobT44SXxWS3oXmKEMXc5odjkZrH_VVWNWbSCNzqveyo5DpyCns5YsT9BVnDSQEz46Oo5hZ9bGlja-rOZ4Sjez6dIXz1RcUcsYC6mPUqhAUnbPfNCL3Bac1ZZYpPD_MRm0pY1SYPIa1H97cKH8A6uR_EryM8u_G1mjGcCawVO9q-5eqaDOqv6hgMlmnPoKXW06c6YWWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهش ثروت شخصی ترامپ به سطح 6.5 میلیارد دلار!</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/17014" target="_blank">📅 23:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17013">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">محمدجواد لاریجانی: رفتن آقای قالیباف به اسلام‌آباد غلط بود و هزینه‌ای بزرگ بود
▫️
ترامپ معتقد بود برجام کافی نیست برای همین آن‌را پاره کرد تا امتیازات بیشتری بگیرد.
▫️
دلیل آنکه آن‌ها در میانه مذاکرات حمله می‌کنند آن‌ است که ما وقتی مذاکره می‌کنیم به آن‌ها سیگنال می‌فرستیم که می‌توانیم با آن‌ها کنار بیاییم و برد-برد کار می‌کنیم که آن‌ها فکر می‌کنند اگر بیشتر فشار بیاورند، امتیازات بیشتری می‌گیرند.
▫️
نخست‌وزیر پاکستان، آدم خوبی است، اما لازم نیست ما و آمریکایی‌ها را مقابل هم قرار دهد تا مذاکره کنیم، باید میانجیگری بلد باشد.
▫️
اگر ما بخواهیم خودمان با آمریکا صحبت می‌کنیم نیازی به میانجی‌ نداریم. /صداوسیما</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/17013" target="_blank">📅 23:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17012">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نخستین سند قطعی دال بر خودکفایی کامل کشور در تولید تریاک</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/17012" target="_blank">📅 22:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17011">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">▪️
خبر این است: وزیر کشور پاکستان پیش وارد تهران شد  مایلم یکبار دیگر صراحتا هشدار بدهم که ابداً نباید حسن نیت داشتن پاکستان را پذیرفت؛ پاکستان یکی از فاسدترین کشورهای دنیاست که توسط یکی از فاسدترین نظامیان دنیا اداره میشود. نظامیانی که وابسته سعودی، آمریکا،…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17011" target="_blank">📅 21:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17010">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دقت کرده اید هر کسی میانجی این جنگ بی پایان ما با آمریکا و اسرائیل شد به خاک رفت؟!  راند اول قطر میانجی شد و همان روز ایران به قطر حمله کرد و چند ماه بعدش اسرائیل هم به قطر حمله کرد و در جنگ اخیر هم با حمله موشکی وحشتناک ایران به تاسیسات گازی راس الفان، بیشترین…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/17010" target="_blank">📅 21:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17009">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9QVNtfeKoelN36A9dxGrVyFPWz2XZCFdXtEdWPGJcEkbYcdNhZiCT1Ph28rhY-PvwKOkSuiBDNwGCVNJ4szcfGBtD1Q7M7id3nEdhR7CAfLtRDmTncc9Uxx8VGBjuzgG57EWfmTqooBs_VfZOD_HPAa1WpV7LT9R0b_dDkzRdAl2CdAhzOVYNelGp0we6yl8rXTu9JlIbwqusyPZzgFiln2GpQARDf_Lj-t3P1vyMgqpDFz6XO7q2U7faGQTSbhUVrwkMnqAwKm_-a_s2wr0dIham1SMSuP-pyfEysnqx4hNrQuEp_vxIMY6ijBh_PSG3aTQeyc-Avtx5pOOWzgqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ایران در سال ۲۰۲۶ با یکی از شدیدترین فشارهای صادراتی خود در سال‌های اخیر روبه‌رو شده است. داده‌های منتشرشده توسط شرکت ردیابی نفتکش Kpler و منابع تخصصی بازار انرژی نشان می‌دهد که از زمان آغاز درگیری‌ها و تشدید محدودیت‌های دریایی در اواخر فوریه، توانایی…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17009" target="_blank">📅 20:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17008">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وزیر کشور پاکستان، محسن نقوی، برای دیدار با مقامات ایرانی از جمله وزیر امور خارجه عباس عراقچی، وارد تهران شده است.
— خبرگزاری تسنیم</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17008" target="_blank">📅 20:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17007">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تروریستهای ازبک دولت الجولانی را تهدید کردند   گروهی از تروریستهای جهادی ازبک با انتشار بیانیه‌ای دولت سوریه را به اعمال فشار علیه خود و تهدید به بازداشت و اخراج از سوریه متهم کردند.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17007" target="_blank">📅 20:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17006">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">من بعید نمیدانم در این سفری که علامه جولانی به آمریکا داشته ، به پیشنهاد عربها از ترامپ دستوری جهت اخراج این وحوش اویغور و اوزبک و چچنی و … دریافت کرده باشد</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17006" target="_blank">📅 20:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17005">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPR1GR1U1RA2aT9xpjBkW1W2rcS325el8SMMDC5WageBcMMAsi8hw8XIB1V6elYesETYKffxSdGsOKlmXWp-dk9W0ZQOAa_bG9vnatyYRmd73j4BJiYvKgDKhjPmAwS9LjuPlWgI52hQyDXuArNjD0VMhVboDJDzHvI0WcTZsKeAVkUMkRDzxG47Q5MGdv2x9HY6BN4GvcSa9BchPIDNcOCN-VgF5rUPzaxh_c-rG7PB1pCLhkfJBc16TygTb9eiEGYmcI7anyCbI0ko39Njz2fwTvYNQn2zlkwcTX4n4zFot7WrUK_IMud7XwAxyReWUiZQBA8nudwt9clnY5IrmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا چرا غیرقابل دانلود؟!</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/17005" target="_blank">📅 20:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17004">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شما ببینید وضعیت این منطقه گه گرفته چطوری است که پاکستانی که خودش در‌ همین مدت در غرب (بلوچستان)، شمال (وزیرستان) و شرق (هند) غرق در تنش و نکبت بوده حالا دارد برای ما میانجیگری می‌کند!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17004" target="_blank">📅 19:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17003">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پیروزی اوکراین با ربات ها و هوش مصنوعی !؟  در سال‌های اخیر، روایت حاکم بر جنگ روسیه و اوکراین حول محور بقای کی‌یف در برابر ماشین نظامی مسکو می‌چرخید. با این حال، شواهد میدانی و مواضع تحلیل‌گران غربی نشان می‌دهد که ورق به سود اوکراین برگشته و اکنون صحبت از…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17003" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17002">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7JbnAj3Q0Id3SkyftmC_0xppOQV_yeeFxPnyfXToukTy0VhtyRuDOLjtRFX7fPmnmZt-iT5thjLTRm42GOI088B9WDgDHz3tg8zuHDplzGTyxv8qwz_uAFIUMYVuXQ8MI4d1Cf0OiDuPLTcHL8zSXtK8SSe95hCAEkcb7fRtxVLiO5RJj8JXgj2MxgFNikQOdI_bVoeE0ko0ir1zSLfuIvQTddlp_Oio3OpijZ0DR1glWvAP16EmA0dxO7ErnI13PHKqwVlxPYrmie2fG-DZOb2tsEZHBubKsg7kc0_c_a9u1YxIRB_mNz8RZXNTVpzzlOr2zJUnoh2oBV6g3TiMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
ربات ها درحال بازنویسی چهره جنگ امروز
♦️
رباتیک در میدان جنگ به عنوان نظامیان  برای کارهایی که بیش از حد معمول خطرناک، تکراری و یا با پیچیدگی خاص برای انسان است بکار میروند.
🔸
از هواپیماهای بدون سرنشین، عرضه به تانک های خودمختار به تانک های خودمختار، روبات…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/17002" target="_blank">📅 17:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17001">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔻
برخی شنیده ها حاکی از تلاش گروهی از نمایندگان مجلس برای استیضاح وزیر ارتباطات به جرم اجرای دستور رئیس جمهور و بازگشایی اینترنت می باشد</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/17001" target="_blank">📅 14:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17000">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">📡
اینترنت پاکستان ، به دلیل اعتراضات مردم علیه حکومت ، در آستانه خاموشی قرار دارد</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/17000" target="_blank">📅 13:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16999">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✈️
پاول دوروف ؛ مالک تلگرام
:
فیلترینگ و محدودیت‌های اینترنتی، روسیه را به «حاکمیت دیجیتال» نزدیک‌تر نکرده، بلکه از آن دورتر کرده است.
به گفته دوروف، متخصصانی که می‌توانستند در روسیه سیستم‌عامل موبایل بسازند، به‌دلیل وضعیت خراب اینترنت، در حال ترک کشور هستند
او تأکید کرد تا زمانی که گوشی‌ها بر پایه سیستم‌عامل‌های آمریکایی مثل iOS و Android کار می‌کنند، حتی اپلیکیشن‌های «ملی» هم در برابر نظارت و سانسور از طریق بک‌دورها و فروشگاه‌های اپلیکیشن آسیب‌پذیر می‌مانند
دوروف این سیاست را «تغییر بسته‌بندی بدون تغییر اصل ماجرا» توصیف کرد و کنایه زد: مسئولی که به نام حاکمیت دیجیتال، اینترنت روسیه را خراب کرده و کشور را دهه‌ها عقب برده، شایسته دریافت مدال امنیت ملی از آمریکاست</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/16999" target="_blank">📅 12:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16998">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCnXvO12bisKYFP0bnVT6fVKP7XJL7tavJW7KVoNxUfcYA3BFXwo8gobcVIWBnVx1u-NKnVf9MZoL7dRc3MD0edH_0Y_SBPzawl7896HOQGB9rJ-p2lOde0RR0RooNDFvnc78PYoji-FO9pGqkHrVsrvU6Ko1hYRCU2GC8qcaPaD6-GnzNeAAsxc7DEgE-_t1BvF6Y4rFw-M0AP-ackgFtAIGMXdHSvFMIftauhDR0DEI2Vd-uO4d-Ues6PpTBBR_iHpbWtHG4-mPniB0MCiAsj5moes7MwavdvvpOzZr1w3JkwuKvgmeFeR1URvA_19Dp3bbe9PCBl_UTjLMMgDEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
اینترنت پاکستان ، به دلیل اعتراضات مردم علیه حکومت ، در آستانه خاموشی قرار دارد</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/16998" target="_blank">📅 12:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16997">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">این یعنی نه ایران و نه روسیه از این جهش بهای نفت حداکثر استفاده را نبرده اند؛ ما به دلیل محاصره دریایی آمریکا صادراتمان افت کرده (پست ریپلای شده را ببینید) و روسها هم به دلیل حملات سنگین پهپادی اوکراین.  عربها هم که عمدتاً ضربه دیده اند و لذا بزرگترین منفعت…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/16997" target="_blank">📅 11:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16996">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ارتش لبنان اعلام کرده است که چندین نفر از پرسنل نظامی، از جمله یک افسر، در حمله هوایی اسرائیل که یک خودروی نظامی را در جاده الخالدیه–نبطیه هدف قرار داد، کشته شدند.  بر اساس گزارش‌های رسانه‌های لبنانی، این افسر دارای درجه سرتیپ بود.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/16996" target="_blank">📅 11:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16995">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ارتش لبنان اعلام کرده است که چندین نفر از پرسنل نظامی، از جمله یک افسر، در حمله هوایی اسرائیل که یک خودروی نظامی را در جاده الخالدیه–نبطیه هدف قرار داد، کشته شدند.
بر اساس گزارش‌های رسانه‌های لبنانی، این افسر دارای درجه سرتیپ بود.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/16995" target="_blank">📅 11:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16994">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دقت کنید که سنتکام می‌گوید که دوباره «سایتهای راداری نظارتی ساحلی ایرانی» را در گروک و قشم زده اند!  پیشتر اشاره شد چرا مهم است.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/16994" target="_blank">📅 09:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16993">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فرماندهی سنتکام:   چند لحظه پیش، نیروهای مرکز فرماندهی مرکزی چهار پهپاد تهاجمی انتحاری  ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند.   پهپادهای ‌تهاجمی تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای آمریکایی پس از آن به سایت‌های…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/16993" target="_blank">📅 09:35 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
