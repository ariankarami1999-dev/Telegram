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
<img src="https://cdn4.telesco.pe/file/FLqrrkH7dfYZnlFJ_0DR1tfCWC2Ylq_8ogAXJieR_QKRaIZdAb4pkAfMlNvMIZ2-JmAkPWK3Vb0pQu0cKG8_QEL3cE7F1I3k11NA1acX0ZIEPtGqcjNeHx8qwtdgs-kmnEY9wfpKSjF81KC8rPbUgHyz5edwXhxm9-cutXavYU2HSLMODpjrzBhrrV7Q9jp6QDXSXm-Gr_Ht08ZFJy5ijmi-GquDd7IqsV8hSWtFoHP8MnlLm5wpGL_VjeZ0vegLQ8W-HEAB1IyozVrjlPCfUJCsPxGC7ZSBhwZdKAjizXI100yge9WQBp0dhCuJdLTJCpJGWu59CQRtTWLlPqkTCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 495K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 16:17:25</div>
<hr>

<div class="tg-post" id="msg-25351">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/814d6e3065.mp4?token=B5VMU8uqkmMmxfZ_Gwpjhvmodaf4DShZCFg5UJSVe2q6xa6gRNEByP3VzRmy8qrfieSndIVsRGawHq5IKLqJCFr2Q_jH4zy2-YvlncOtbI5EivNxkWeNgQmWwUWhA3rp6JLObVcgXnKQMiN2jJ6lnYj8zCkKY-63LTYKxPPzbOET2xB7dBURbdnU4QLC_QBRwQaFj9uZKzbXDVxFhipEu4co0-RZTbgbIpRVRXl3ciYUixScLgTe50-eqTtRB6j2gDMWY2-dCR9mIYNMILBVnrzHDcqJYFmKXjZHbelyau9dceOV2sqZW-Nb9XrcHIkRc-zUalRNZi1dt1csSmfrlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/814d6e3065.mp4?token=B5VMU8uqkmMmxfZ_Gwpjhvmodaf4DShZCFg5UJSVe2q6xa6gRNEByP3VzRmy8qrfieSndIVsRGawHq5IKLqJCFr2Q_jH4zy2-YvlncOtbI5EivNxkWeNgQmWwUWhA3rp6JLObVcgXnKQMiN2jJ6lnYj8zCkKY-63LTYKxPPzbOET2xB7dBURbdnU4QLC_QBRwQaFj9uZKzbXDVxFhipEu4co0-RZTbgbIpRVRXl3ciYUixScLgTe50-eqTtRB6j2gDMWY2-dCR9mIYNMILBVnrzHDcqJYFmKXjZHbelyau9dceOV2sqZW-Nb9XrcHIkRc-zUalRNZi1dt1csSmfrlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ثبت‌شده توسط ماهیگیر مینابی از گشت‌زنی یک بالگرد ناشناس، احتمالاً از نوع آپاچی، در نزدیکی تنگه هرمز در صبح امروز منتشر شده است. این پرواز پس از انتشار گزارش‌هایی درباره هدف قرار گرفتن یک نفتکش در این منطقه انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/withyashar/25351" target="_blank">📅 16:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25350">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUDyPbKRmDp-9IxWVtRNNDUbbldnvEnfEa7ETF7dFf4OuCwEIzS6TJHle8PdaQN_oyq60xDFrMqFpc0NqbjvsRkcglPE9dLFHwRIgjswn7qDB52mi8YbOSx5otE8ibiJ9PoOk0Jhc0Sw2ds4YLI9nBxsK0sVdK1o3aYbYzKRsG-ODg83KLhBXWDiONKw0F3ccvvRDajt3sXpLKEI2ajb0h605Y41Ek1ipV-02W38TuROS9arOGi8dTPnpO7LTqU5lWtilGHxglBfOvgbfD90NtkpcWWrET5JV4ovqAypoRBsgRD5HE7kSXiW_6a49X3DCyPwOfLBbxiDfC3euARskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: من به ۸ جنگ پایان دادم و به پایان دادن یا حل‌وفصل ۲ جنگ دیگر نیز نزدیک هستم. تمام گروگان‌های اسرائیلی، از جمله ۲۸ نفر آخر، چه زنده و چه جان‌باخته، را بازگرداندم. همچنین صدها گروگان از کشورهای مختلف جهان آزاد شدند و به خانه‌هایشان بازگشتند. در ونزوئلا در جنگ پیروز شدیم و دیکتاتور خشنی را که با بی‌رحمی بر آن کشور حکومت می‌کرد، دستگیر کردیم. علاوه بر این، جمهوری اسلامی ایران، بزرگ‌ترین حامی دولتی تروریسم در جهان، را از دستیابی به سلاح هسته‌ای بازداشتیم — و کارهای بسیار دیگری هم انجام دادیم! با وجود تمام این اقدامات، نه من و نه ایالات متحده آمریکا جایزه صلح نوبل را دریافت نکردیم. عجب!
@WarRoom</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/withyashar/25350" target="_blank">📅 15:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25349">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پزشکیان: جایگاه فعلی زیبندۀ ما نیست
@WarRoom</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/withyashar/25349" target="_blank">📅 15:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25348">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خبرنگار الجزیره: حمله هوایی اسرائیل به اطراف شهر طلوسه در منطقه مرجعیون در جنوب لبنان.
@WarRoom</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/25348" target="_blank">📅 15:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25347">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آسوشیتدپرس گزارش داد مقام‌های ائتلاف به رهبری عربستان مدعی شده‌اند ۱۳۶ هدف نظامی در مناطق تحت کنترل حوثی‌ها را منهدم کرده‌اند. هم‌زمان، انفجارهایی در صنعا گزارش شده و سخنگوی وزارت بهداشت وابسته به حوثی‌ها گفته است حملات دو نفر از جمله یک کودک را مجروح کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/25347" target="_blank">📅 15:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25346">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-c4Z0nHpd2SV-X8Grp1j_CqTHMtGBNU5eR0gFM9VGeyLqEFNmGYd6tlMoKRuyc_WOiqOIpF0Gn0i3kx-JlP88yE8rH294OdNcX_GYJIFnsWs8dvmO3kKCR1pWDxu7ysBUr8ilKB958skatJNIdk-wYFkIFa7qz32exJOn0NyyKMSeLtqsJbpet9U_GpHQY8m5uPGLSdKZr0p4UjRvVIOzG6TgToHOa-DnIFkg2JMHHR_21e4UiONe21USsZOz-8MQwSvlnmjz-Kjf9dMDDqvmKzuJVvE_Y00yxLC7G7hKxC-C6-AyGLGK7Gybyj78grFTpyN5svQclGd7TAJLrGcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا:
تا سقف ۱۵ میلیون دلار پاداش برای ارائه اطلاعات درباره شبکه‌های مالی سپاه پاسداران
سپاه پاسداران انقلاب اسلامی از سازوکارهای مالی متعددی برای تأمین هزینه فعالیت‌های تروریستی خود استفاده می‌کند؛ از جمله فروش غیرقانونی نفت از طریق شرکت‌های پوششی و ناوگان سایه (کشتی‌هایی که برای پنهان کردن مبدأ، مقصد یا مالکیت محموله‌های نفتی به کار می‌روند).
@WarRoom</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/25346" target="_blank">📅 14:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25345">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">جلسه خطرناک اتاق بی فکر ها : نفوذی ، سوپاپ اطمینان  ، کودن ، چپ ، هزار چهره و … در منزل محمد مهاجری @WarRoom
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/25345" target="_blank">📅 14:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25344">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zzr4L6JOBQxQ7bp-TFyP8ew6nqwAy7UW5eywmapcN_OQKw-CK_4Yioz6RphOKcAVQ7ZQldKAFpzHaRgDR0H5gFKais2OpQrxbYwHvtL-PtfWWPOyx23OPw8lue6KY5f-KOZH39YG0rLcWC4LAM2RDw9A4UHtqW9YgXZ80J7Lzgw7MezgfLgncEP6lrHvaUE2CSBx4HubEpVIFm7B2negEKjMWVNxZCntSi_pxTy_XihigHJMC_yw3CXMlDYTXhRgJ3mlH4EqCV9pmC1pQnZdV11JTC9ZsiNZcmsPteyxMbeCWxFl3kdMck7n2BE_9NmelAEBHHbxRQxdnPIgRrnRJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه خطرناک اتاق بی فکر ها : نفوذی ، سوپاپ اطمینان  ، کودن ، چپ ، هزار چهره و … در منزل محمد مهاجری
@WarRoom
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/25344" target="_blank">📅 13:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25343">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5467fef82.mp4?token=N7JrSX98oIhrjLNREqjEHQYT4dU-YUARK3k1xkE1N49r5WuXnsIte7UkVyMD3tPAXfsgGyITf9PT063IANBTPtwzrWfpLDDUAaVLeLWRhfht3IK_00WMPp8noNMUB0dNocCmFeZ2i5ejDb1Po_94zk-YIw4ZYragkw9ezlW7V8lqEBIB30DLReHU0OWCexguV6JUdKhU8d8plNUrkCrkWi-H3vmG75b2QjKNsfnMpaplUGu9AyKVGKcad4rE-lKOKywmo9ScgbP5HJ9QBAR3nV2FWQxcQ6NowmJ0knkdQFI9Uy-2qVlJkRr8WmRlyIwRPgwNFb20zaW4Ao66YvwMBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5467fef82.mp4?token=N7JrSX98oIhrjLNREqjEHQYT4dU-YUARK3k1xkE1N49r5WuXnsIte7UkVyMD3tPAXfsgGyITf9PT063IANBTPtwzrWfpLDDUAaVLeLWRhfht3IK_00WMPp8noNMUB0dNocCmFeZ2i5ejDb1Po_94zk-YIw4ZYragkw9ezlW7V8lqEBIB30DLReHU0OWCexguV6JUdKhU8d8plNUrkCrkWi-H3vmG75b2QjKNsfnMpaplUGu9AyKVGKcad4rE-lKOKywmo9ScgbP5HJ9QBAR3nV2FWQxcQ6NowmJ0knkdQFI9Uy-2qVlJkRr8WmRlyIwRPgwNFb20zaW4Ao66YvwMBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی رفته یه پاساژ تو محدوده سعدی تهران یه منشی رو کشته بعد هم خودشو
@WarRoom</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/25343" target="_blank">📅 12:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25342">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کرملین: ولادیمیر پوتین با هماهنگی مسعود پزشکیان، دیدگاه ایران درباره راه‌های احتمالی حل‌وفصل مناقشه را به دونالد ترامپ منتقل کرد. دیمیتری پسکوف، سخنگوی کرملین، گفت پوتین در حاشیه نشست‌های ترکمنستان دو بار با پزشکیان دیدار کرد و پیش از گفت‌وگوی تلفنی با ترامپ، او را در جریان این تماس قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/25342" target="_blank">📅 12:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25341">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35bbce1ecb.mp4?token=Jt_FTOhRZ2XnEcmwF2YFaOV-4nVGSXfBw_bTzLqMdY2mvQBMNMi355KyHYCGS5fXAyqR4ISE5zRFXVUMNbDKhvvj7ZQ_uCbW2Q2doUbG3Ep5YPbjNpXD-nleu6zo944ARRm6vgL4aoOKtQi_qzhWotBFLpr1PDDwSPWibGBYi-QJ_JhgTKzw9MQavfuvCPZZtIaDKCPGrxMSvl2HKqO-UcY8iMmpR_UE1XcGtjBA9lC3yNTtz24ncPEsOPhtAnA0_Ylud7xVk4UTd4JZJFW0cImFPzUXdIfstP9CaazOasvJjyFI4IOag0D8zmeybHpqGGVf9lPZxc7ExSdPhVfoeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35bbce1ecb.mp4?token=Jt_FTOhRZ2XnEcmwF2YFaOV-4nVGSXfBw_bTzLqMdY2mvQBMNMi355KyHYCGS5fXAyqR4ISE5zRFXVUMNbDKhvvj7ZQ_uCbW2Q2doUbG3Ep5YPbjNpXD-nleu6zo944ARRm6vgL4aoOKtQi_qzhWotBFLpr1PDDwSPWibGBYi-QJ_JhgTKzw9MQavfuvCPZZtIaDKCPGrxMSvl2HKqO-UcY8iMmpR_UE1XcGtjBA9lC3yNTtz24ncPEsOPhtAnA0_Ylud7xVk4UTd4JZJFW0cImFPzUXdIfstP9CaazOasvJjyFI4IOag0D8zmeybHpqGGVf9lPZxc7ExSdPhVfoeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیک موشتبی در تجمعات دیشب ، سوژه خنده کاربران شده است
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25341" target="_blank">📅 12:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25340">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c561009016.mp4?token=PXMnkdn7neLmfg1Vg0ibEewvTXKbfk3gvUMCD0UN0-uWiW5CO5xEPHVVE0C8Q_U_WkP93z3ryoQsTS9VWNT_1-iuSxaapNtp-ug8MvTNS1skcAD14Fy-depTS_mn65qBnO2a2NGx1VQUp3Fg0zrNoy7m-g1WjNptfQRD8UnFx70I6PGZxbkIyT2e0vG3OReDc8O4G3EvUvWc8edkCH8lLeQEb9ZQVfWKB4LRBWqbWgsOD6IA5vmX-qenn0ZOGqS_50TgKnuuN6OH6tkL5MFhhClnZnPrsiWyG-USBY4yu8MeedUfitaDLzzCZmOz9YYP5GiA5l7pRlUXJ3WBPjj-lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c561009016.mp4?token=PXMnkdn7neLmfg1Vg0ibEewvTXKbfk3gvUMCD0UN0-uWiW5CO5xEPHVVE0C8Q_U_WkP93z3ryoQsTS9VWNT_1-iuSxaapNtp-ug8MvTNS1skcAD14Fy-depTS_mn65qBnO2a2NGx1VQUp3Fg0zrNoy7m-g1WjNptfQRD8UnFx70I6PGZxbkIyT2e0vG3OReDc8O4G3EvUvWc8edkCH8lLeQEb9ZQVfWKB4LRBWqbWgsOD6IA5vmX-qenn0ZOGqS_50TgKnuuN6OH6tkL5MFhhClnZnPrsiWyG-USBY4yu8MeedUfitaDLzzCZmOz9YYP5GiA5l7pRlUXJ3WBPjj-lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم اکشن‌کمدی «مچ‌باکس» (Matchbox: The Movie) با بازی گلشیفته فراهانی و جان سینا و به کارگردانی سم هارگریو، دیشب از اپل تی‌وی پلاس منتشر شد. داستان فیلم درباره گروهی از دوستان قدیمی است که درگیر ماجرایی جاسوسی و پر از تعقیب‌وگریز می‌شوند. داستان فیلم بر اساس برند اسباب‌بازی خودروهای مچ‌باکس ساخته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25340" target="_blank">📅 11:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25339">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رویترز: بازارهای جهانی در پایان معاملات جمعه، ۹ اکتبر، با افزایش قیمت نفت و طلا بسته شدند. نفت برنت با رشد ۰٫۴۲ درصدی،
۱۰۴٫۷۲ دلار
در هر بشکه و نفت خام آمریکا (WTI) با افزایش ۰٫۳۹ درصدی،
۹۱٫۸۵ دلار
بسته شد. طلای نقدی با رشد حدود ۱٫۵ درصدی به
۴٬۱۹۴٫۳۶ دلار
در هر اونس رسید و قرارداد آتی طلا برای تحویل دسامبر با رشد ۱٫۴ درصدی در
۴٬۲۱۶٫۳۰ دلار
تسویه شد. نگرانی از اختلال عرضه انرژی، تنش‌های مرتبط با جنگ ایران و توقف بیش از ۷۰ درصد تولید نفت فراساحلی آمریکا در خلیج مکزیک از عوامل اثرگذار بر بازار نفت بود.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25339" target="_blank">📅 11:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25338">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آسوشیتدپرس:
سریلانکا اعلام کرده فعلاً برنامه فوری برای کمک به ۱۹ نفتکش ایرانی گرفتار در آب‌های نزدیک سواحل خود ندارد. این کشتی‌ها بنا بر گزارش، با کاهش ذخایر غذا، آب و سوخت روبه‌رو هستند و دولت سریلانکا نگرانی از تحریم‌های ثانویه آمریکا را نیز در تصمیم خود لحاظ می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25338" target="_blank">📅 11:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25337">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f0fa0967.mp4?token=mCCtHZ2CPoDKgRPu-49rVR9bLi_dV0_KP4an6CXoyrFJ9IC4UEcfhk_Ah6hEBYiOhd4_emuCTAm76ERHlzy2kHjmYDw8OpR40oNpwZXHPY7ezCdC1UTqaCOECJHDpHxIE9zPk1jr526kh_qukUyLQxHtZX-0AaVFcmB7dTUcqqbazB1kDNu1cYjuv4TNPYPOte1ygW4KfnhbjtJqGn005i2fuiFn0hx-5uyuNrNyQlBHGSSp6gURnwVGyO6cHgY6zSo3ija06m02xzTGxhW1R3l4vbqPIPuK-1wqgFqMqyd8H0i18i8GjngvPWMRJbJMPc0WBOwsWYY7h39_3lOt3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f0fa0967.mp4?token=mCCtHZ2CPoDKgRPu-49rVR9bLi_dV0_KP4an6CXoyrFJ9IC4UEcfhk_Ah6hEBYiOhd4_emuCTAm76ERHlzy2kHjmYDw8OpR40oNpwZXHPY7ezCdC1UTqaCOECJHDpHxIE9zPk1jr526kh_qukUyLQxHtZX-0AaVFcmB7dTUcqqbazB1kDNu1cYjuv4TNPYPOte1ygW4KfnhbjtJqGn005i2fuiFn0hx-5uyuNrNyQlBHGSSp6gURnwVGyO6cHgY6zSo3ija06m02xzTGxhW1R3l4vbqPIPuK-1wqgFqMqyd8H0i18i8GjngvPWMRJbJMPc0WBOwsWYY7h39_3lOt3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما یک سال پیش با بمب‌افکن‌های «بی-۲» آن‌ها را بمباران کردیم و از آن زمان تاکنون نیز به بمباران آن‌ها ادامه داده‌ایم.
آن‌ها هرگز به سلاح هسته‌ای دست نخواهند یافت.
ما عملکرد بسیار خوبی داشته‌ایم. این ماجرا خیلی زود، به هر طریقی که باشد، پایان خواهد یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25337" target="_blank">📅 11:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25336">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فایننشال تایمز:
حملات به نفتکش‌ها از تنگه هرمز فراتر رفته و به بخش‌های دیگر خلیج فارس گسترش یافته است. این گزارش از حمله به نفتکش ترکیه‌ای «Acers» در نزدیکی قطر و نفتکش بزرگ چینی «Gem No. 2» در نزدیکی امارات خبر می‌دهد. افزایش خطر حمل‌ونقل دریایی هزینه فعالیت نفتکش‌ها را بالا برده است.
@WarRoom</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/25336" target="_blank">📅 11:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25335">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پنتاگون آمار تلفات نظامی آمریکا در جنگ با ایران را به‌روزرسانی کرد:
با اضافه شدن ۲ کشته و ۴ مجروح به آمار قبلی، شمار نظامیان آمریکایی کشته‌شده به ۲۱ نفر و تعداد مجروحان به ۸۶۵ نفر افزایش یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/25335" target="_blank">📅 10:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25334">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">المانیتور به نقل از کریس مورفی، سناتور دموکرات ایالت کنتیکت، پس از دیدار با امیر قطر و میانجی ارشد این کشور: توافق با ایران برای پایان دادن به جنگ، در شرایط فعلی قریب‌الوقوع به نظر نمی‌رسد. مورفی همچنین ارزیابی کرده است که چارچوب توافق احتمالی احتمالاً بسیار محدود خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/25334" target="_blank">📅 10:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25333">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/074cfb2840.mp4?token=nLvmY74ANNP06sb-RhIJzzmTndTCYsven7Tt_RLvu4t1UdkIiGCBJv7DF6yzeyoGnW-6THzkAXTKWfiCd5vNtM2-ScpsoKl0MZnlhbJZiagIr2dkrfxCa2ZzWYChVO6_rY2qiFYJncD2vQsF_F8Tv_u9_EejNZvMSmj2HDZg6506R5M4l6WVC6HUsEiUip3nlFIIr2hXzUYo6nt72mFLnFkDfWRs8JclAr4X1vLQmkHHa5p3GhOF_kw8spmeyy2eIucD073idzIkXRhCrEDoLC1IqBlAkgZctA7mD8sIRz5juwKLOusKZrk58yeEWxMr4jGgAipk25ZpaTzgOd83Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/074cfb2840.mp4?token=nLvmY74ANNP06sb-RhIJzzmTndTCYsven7Tt_RLvu4t1UdkIiGCBJv7DF6yzeyoGnW-6THzkAXTKWfiCd5vNtM2-ScpsoKl0MZnlhbJZiagIr2dkrfxCa2ZzWYChVO6_rY2qiFYJncD2vQsF_F8Tv_u9_EejNZvMSmj2HDZg6506R5M4l6WVC6HUsEiUip3nlFIIr2hXzUYo6nt72mFLnFkDfWRs8JclAr4X1vLQmkHHa5p3GhOF_kw8spmeyy2eIucD073idzIkXRhCrEDoLC1IqBlAkgZctA7mD8sIRz5juwKLOusKZrk58yeEWxMr4jGgAipk25ZpaTzgOd83Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: این جنگ یا از طریق نبرد پایان می‌یابد، یا آن‌ها توافق‌نامه‌ای را که ما می‌خواهیم، امضا خواهند کرد
اگر اجازه می‌دادیم آن‌ها به سلاح هسته‌ای دست پیدا کنند، شاهد سطحی از مرگ، آشوب و ویرانی می‌بودید که هرگز مانند آن را ندیده‌اید. و من جلوی آن را گرفتم
رؤسای‌جمهور قبلی باید مدت‌ها پیش از روی کار آمدن من، جلوی این اتفاق را می‌گرفتند
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25333" target="_blank">📅 10:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25332">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بلومبرگ:
ایران با وجود ماه‌ها حملات آمریکا و اسرائیل، کارخانه‌های تولید موشک و پهپاد خود را حفظ کرده و همچنان توانایی بازسازی و تکمیل ذخایر تسلیحاتی‌اش را دارد. به گفته مقام‌های آگاه غربی، تهران هنوز ذخایر قابل‌توجهی از موشک‌های بالستیک و برخی تسلیحات ضدکشتی در اختیار دارد و می‌تواند به‌سرعت بر تعداد آن‌ها بیفزاید. این مقام‌ها همچنین مدعی‌اند که روسیه در حال تأمین موشک برای ایران است؛ ادعایی که وزارت دفاع روسیه به درخواست بلومبرگ درباره آن پاسخی نداده است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25332" target="_blank">📅 10:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25331">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ : ایران یا خیلی سریع همه چیز را به ما خواهد داد، یا دیگر وجود نخواهد داشت. آن‌ها این را می‌دانند @WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25331" target="_blank">📅 10:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25330">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3d0a7be4.mp4?token=fosIzmhxVD_WhfPS-hwlj1rdpE0RViEvdNgq7a22gHGxFheQmRqoO2MEFb2ZOM6rIaBmooU3i_NqXwfpWVB_HiMAaqXikYZZeeXd52tZ8aa7NNrNPFeA-bfq74bw_w8LvcXhGYK7DonAq9zKL0oHQOBEmP6vNNRYI7NpflJB3MV5D-JKsMK1u-a_MxZdotTwW8qpSUsmlBr3jiZ568P6QEaDX7tY7i3eOKJYMPAFMlkNkdRzjl2jzV64EivV89B0p8ZzCMft9BBQ3HT6timLAbh_sWqMkVcyMGBceoony_KMMY-RGHdNaKo-yVZSNhqnUnnDiQOjM6PonmlCeCoN0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3d0a7be4.mp4?token=fosIzmhxVD_WhfPS-hwlj1rdpE0RViEvdNgq7a22gHGxFheQmRqoO2MEFb2ZOM6rIaBmooU3i_NqXwfpWVB_HiMAaqXikYZZeeXd52tZ8aa7NNrNPFeA-bfq74bw_w8LvcXhGYK7DonAq9zKL0oHQOBEmP6vNNRYI7NpflJB3MV5D-JKsMK1u-a_MxZdotTwW8qpSUsmlBr3jiZ568P6QEaDX7tY7i3eOKJYMPAFMlkNkdRzjl2jzV64EivV89B0p8ZzCMft9BBQ3HT6timLAbh_sWqMkVcyMGBceoony_KMMY-RGHdNaKo-yVZSNhqnUnnDiQOjM6PonmlCeCoN0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : ایران یا خیلی سریع همه چیز را به ما خواهد داد، یا دیگر وجود نخواهد داشت. آن‌ها این را می‌دانند
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25330" target="_blank">📅 10:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25329">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نیویورک‌تایمز گزارش داد کاخ سفید سمت سخنگویی را به کیتی زکریا، مفسر محافظه‌کار و مشاور ارتباطات نزدیک به دونالد ترامپ، پیشنهاد کرده است. او پیش‌تر نیز برای مدتی سخنگوی وزارت امنیت داخلی آمریکا بود. در صورت نهایی‌شدن این انتصاب، زکریا جایگزین کارولین لیویت…</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25329" target="_blank">📅 03:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25328">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/450a7d0c9a.mp4?token=WUftHVcscDgQgS57I_arjdIWyLnNlrFT_j71DQE4p4IanRLW5hMhMzSicWfURbGugwY_C07Mdu3Sva2XfvWLxiQZVc_x-iuzrUA2s3500lCS6bDuaIEg4X4amcUCHb9W3R5aOiuDGCLfXv05NK6k2-QW-cJzzEXFKHwfi11T_YVIJk8dJXagYtjGs43G7kmJZfCOfnxpaupkvb2i8SDgIMENy-ONr_9AmN8PVe5TOhnXBlH9kUWuIh2FqsSQ2QtaOT0fJtIZVAYpeheFGGyNW_aQwDq-SqrF6x7fDKXJI3OjvoB_u7HnKT9LeXPWbn0eVb9ttXyfKoMAoAODAICJ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/450a7d0c9a.mp4?token=WUftHVcscDgQgS57I_arjdIWyLnNlrFT_j71DQE4p4IanRLW5hMhMzSicWfURbGugwY_C07Mdu3Sva2XfvWLxiQZVc_x-iuzrUA2s3500lCS6bDuaIEg4X4amcUCHb9W3R5aOiuDGCLfXv05NK6k2-QW-cJzzEXFKHwfi11T_YVIJk8dJXagYtjGs43G7kmJZfCOfnxpaupkvb2i8SDgIMENy-ONr_9AmN8PVe5TOhnXBlH9kUWuIh2FqsSQ2QtaOT0fJtIZVAYpeheFGGyNW_aQwDq-SqrF6x7fDKXJI3OjvoB_u7HnKT9LeXPWbn0eVb9ttXyfKoMAoAODAICJ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا اقدام نظامی به انتخابات میان‌دوره‌ای آمریکا گره خورده است؟ چرا همین حالا علیه ایران اقدام نمی‌کنید؟
دونالد ترامپ: ممکن است اقدام کنیم
. خواهیم دید، اما فکر می‌کنم آن‌ها به‌شدت در حال شکست خوردن هستند و کشورشان وضعیت بسیار بدی دارد. ارتش آن‌ها شکست خورده است؛ نیروی دریایی ندارند و نیروی هوایی‌شان هم از بین رفته است. تورم در ایران به ۳۰۰ درصد رسیده و این کشور در وضعیت بسیار وخیمی قرار دارد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/25328" target="_blank">📅 02:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25327">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کرملین: در جریان تماس تلفنی، نه پوتین و نه ترامپ نمی‌خواستند زودتر از دیگری تماس را قطع کنند.  @WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25327" target="_blank">📅 02:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25326">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کرملین: در جریان تماس تلفنی، نه پوتین و نه ترامپ نمی‌خواستند زودتر از دیگری تماس را قطع کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/25326" target="_blank">📅 02:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25325">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">من همجا هستم
🫡
فک نکنین نمیبینم</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/25325" target="_blank">📅 01:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25324">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تحلیل بازار
🤑
💵
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25324" target="_blank">📅 01:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25323">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">زلنسکی به ترامپ: " دادن هدایایی به پوتین، منجر به طولانی شدن جنگ خواهد شد."
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/25323" target="_blank">📅 01:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25322">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خوش‌قلبه تاریخ‌ندان ، مارک روبیو :  «ایران تلاش می‌کرد توان نظامی متعارف خود را آن‌قدر گسترش دهد که دیگر نتوان با آن مقابله کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25322" target="_blank">📅 01:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25321">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_V0fLU6YerLyfi2ihepQgI1e1d4dgeL2M3J0Iu-61oJXa2vvk9MYIRWjqV6ZmGUPCbAKFU_eluz0GX5VavBcRr4lARwaxvrf2xA9fRDhe3Adtcthyryi4FWU6O0Q8buoiL1xtHXZuIGyU5178d3ZMEYlNs_eX5eEICEqXf4FhYohYnmWpVLaeClSyGKTaw0azlgxsPbwcECRg1wfGtS-KM610hSC14tsc33NmH7AWoSFyq7DvGcoD3cNb66mI1Ih3L3--LGk4GywKOtlVederw6Cwm-ANUgYH8PKORcBc70ghq3QNVvDHlU9-3r-X9sZuvDW5yKlETvkc9sna1NAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب چند کپسول پیکنیکی تپل از سیریک  @WarRoom
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25321" target="_blank">📅 01:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25320">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">@WarRoom
زمان حمله
💥
⌛️</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25320" target="_blank">📅 01:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25319">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25319" target="_blank">📅 01:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25318">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25318" target="_blank">📅 01:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25317">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ: ممکن است زودتر از حد انتظار به ایران حمله کنیم.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/25317" target="_blank">📅 01:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25316">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پرتاب چند کپسول پیکنیکی تپل از سیریک
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/25316" target="_blank">📅 01:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25315">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9893251f9d.mp4?token=NxumhaU8jDU8XEGoywjX2AZGf5BYdOhh03hywza1hmM8WA48_K-iTdD9gExAXDleUYbLMtDg_kz0g0rBbGr5nseJb1QhX5QDgUueqF4q_fGPzv94RM9nALG5XJA6cEfF37_4tGFqqp3xCf5y42gYUwGDhholNcYB5xBD6HUMsAGkHLlnus_elS-FMgcodZ4gHufz7WgUPevm9gq3JdQe0dC_LhEe0yRRTi-EEd3Z6ybK59mIQJbhdgd-GfhRSoARNv2VI9uFSICPESQNkEmV5VwkPu-hjahYsCOc8KPCthbGLlnkuqCiZUtbmTTCVr_QhL9icuV5herW3vuljLIvjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9893251f9d.mp4?token=NxumhaU8jDU8XEGoywjX2AZGf5BYdOhh03hywza1hmM8WA48_K-iTdD9gExAXDleUYbLMtDg_kz0g0rBbGr5nseJb1QhX5QDgUueqF4q_fGPzv94RM9nALG5XJA6cEfF37_4tGFqqp3xCf5y42gYUwGDhholNcYB5xBD6HUMsAGkHLlnus_elS-FMgcodZ4gHufz7WgUPevm9gq3JdQe0dC_LhEe0yRRTi-EEd3Z6ybK59mIQJbhdgd-GfhRSoARNv2VI9uFSICPESQNkEmV5VwkPu-hjahYsCOc8KPCthbGLlnkuqCiZUtbmTTCVr_QhL9icuV5herW3vuljLIvjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو رو دیدم حالم خوب‌شد
🫡
اول باید هوای همو داشته باشیم تا پیروز بشیم
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25315" target="_blank">📅 01:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25314">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25314" target="_blank">📅 00:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25313">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نمیبخشم و فراموش نمیکنم
😉</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/25313" target="_blank">📅 00:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25312">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaedbc2620.mp4?token=Vj-9JzokpdWor4HKGluq59ujfbq5H1s_CcyE1kySMIQzK2yySVQ7SF2y-qj2Vn6wgIAl3jZMH2lG2JT5L2XZz7lKFMK2s8_Pyx7xcVx7fwRASZzClaQWS3ofpRUcjwOdeLL9x5RwzxSjoHhFbVh2jjq_423sNdsQEPRsLe6iu-iErOKAqKdwE-EEjw5buWb-J5hJuA0qZFml4sU5O6pSETfL6uCxgfVQpAKXqXL7eyDpDQb8B5FGBnqo4OVBTwkuMLU-yX5UYE6iZ4t75_hAVwBIkthgMksWrSy1YPqycGl4-BEhtnxUQ-9J6a_o-JkLOCxgwdOReVd4wWeB-uVx-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaedbc2620.mp4?token=Vj-9JzokpdWor4HKGluq59ujfbq5H1s_CcyE1kySMIQzK2yySVQ7SF2y-qj2Vn6wgIAl3jZMH2lG2JT5L2XZz7lKFMK2s8_Pyx7xcVx7fwRASZzClaQWS3ofpRUcjwOdeLL9x5RwzxSjoHhFbVh2jjq_423sNdsQEPRsLe6iu-iErOKAqKdwE-EEjw5buWb-J5hJuA0qZFml4sU5O6pSETfL6uCxgfVQpAKXqXL7eyDpDQb8B5FGBnqo4OVBTwkuMLU-yX5UYE6iZ4t75_hAVwBIkthgMksWrSy1YPqycGl4-BEhtnxUQ-9J6a_o-JkLOCxgwdOReVd4wWeB-uVx-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: زلنسکی گفته است که به‌خاطر توافق نفتی‌تان با پوتین، شما ضعیف هستید.
ترامپ: چه کسی این را گفته؟
خبرنگار: زلنسکی.
ترامپ: باشه.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/25312" target="_blank">📅 00:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25311">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25311" target="_blank">📅 00:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25310">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25310" target="_blank">📅 00:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25309">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0b707c6d.mp4?token=YIQ_rxGVnae4WQSIgQyPU3G0vCO0i3sOwntASogC8ceJVy_kRqk1PHdxdyS14a18LdplwagJahsAlRh34OI3dpX3RLYlIQHvKEqXi2KXxG4Oo4rO0TfKoAcMhioyIur0eTNfEd2cuA0hjkGqX7AK5VcJrC5D_B77KsieLPz4bcEih1hM5RhUjE4F1ljMNy77bDILbX3QM24xsnpGWklTK6r2zAf5JhX_7P_tT9BWpfAPg3-c5XdPVsJVveHVeWRyePg5FPno3yyHsLCYs6gD_asxJLMoT4TUX0_c801K72ORQEnxWMat03Oe-LnnHF2_hbvWQN5tTnRIBwXEmnThvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0b707c6d.mp4?token=YIQ_rxGVnae4WQSIgQyPU3G0vCO0i3sOwntASogC8ceJVy_kRqk1PHdxdyS14a18LdplwagJahsAlRh34OI3dpX3RLYlIQHvKEqXi2KXxG4Oo4rO0TfKoAcMhioyIur0eTNfEd2cuA0hjkGqX7AK5VcJrC5D_B77KsieLPz4bcEih1hM5RhUjE4F1ljMNy77bDILbX3QM24xsnpGWklTK6r2zAf5JhX_7P_tT9BWpfAPg3-c5XdPVsJVveHVeWRyePg5FPno3yyHsLCYs6gD_asxJLMoT4TUX0_c801K72ORQEnxWMat03Oe-LnnHF2_hbvWQN5tTnRIBwXEmnThvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در کنار مایک تایسون در کاخ سفید: امروز با او مبارزه نخواهم کرد، اما مدت‌هاست که طرفدارش هستم. ما مدت‌هاست با هم دوست هستیم. هیچ‌کس مثل او نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25309" target="_blank">📅 00:41 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25308">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">استوری های اینستاگرام رو عکس دار‌کردم مطلب رو بهتر بگیرین ، خیلی باحال شده دیدید ؟
instagram.com/yashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25308" target="_blank">📅 00:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25307">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/017aa950d4.mp4?token=DirPQarLe_Damc3V-h0o-tsFRqrhOC8ZZrvL5GkFkFDDe_9bjjoax3drdKa6t_mbKDE5dW2nVXEBuFiEOMWfsNEl6sFzPIr3zgTin0l5B0rF-6ZsQo0MvbGhg6VlOvwI1OXhbySp9h8BqUB8NoOPFo0V56mLKbyNtwNm9C2cu3avcPl-bHBZUE_27jZzf2bf2pPKzTSS-dpVQRQBB7nAeUO3zhy3WpDpwchEMBASlO9jkdbCihVXmPpjASMF7bfmuCex7DGGUp5R6pojUNWj0zpb6vgAlv4y2sMyTBR52vLKbCp9V7cQYZzej3VB692wfchksUKcaVZxyiV5nqgzCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/017aa950d4.mp4?token=DirPQarLe_Damc3V-h0o-tsFRqrhOC8ZZrvL5GkFkFDDe_9bjjoax3drdKa6t_mbKDE5dW2nVXEBuFiEOMWfsNEl6sFzPIr3zgTin0l5B0rF-6ZsQo0MvbGhg6VlOvwI1OXhbySp9h8BqUB8NoOPFo0V56mLKbyNtwNm9C2cu3avcPl-bHBZUE_27jZzf2bf2pPKzTSS-dpVQRQBB7nAeUO3zhy3WpDpwchEMBASlO9jkdbCihVXmPpjASMF7bfmuCex7DGGUp5R6pojUNWj0zpb6vgAlv4y2sMyTBR52vLKbCp9V7cQYZzej3VB692wfchksUKcaVZxyiV5nqgzCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25307" target="_blank">📅 00:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25306">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کاش زن داشتم فردا نهار کتلت درست میکرد شاید میزد
😁
یا موسی</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/25306" target="_blank">📅 00:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25305">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqxjhgyPu-9SUy0ulzMJElC1tAwxlmS6TEPu_YJW1rrC2DyzLung7b89QNk9na6O-a6145O2Z_mzpwIKHev4Nhyg114ByFW0KoJp6RclEx0dxtjWtjlbVvC1jm7zD4AbGTlKZY4ANP1H7Tj96I8i8NhaLEEkofHTW4WOAwv1K2wet4R5-I_1be22tZoY8exp-VqGHHFGIstodDsO_wJENuYp-H5PIWUmL91DJpjDUPnuQuRmALjZUW4uos0qJlfZqui9pV3XIoBlFXz1mmp-o_sKxpZYQt63iQ1M8BcIXFj3I7NdabtbGr0TCWRg7mAnW5wXf8qDcLgkIs_o4qy4Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه فارسی وزارت خارجه آمریکا از شهروندان این کشور خواست با توجه به شرایط امنیتی منطقه، برای لغو پروازها و بسته‌شدن حریم هوایی آماده باشند.
به هیچ دلیلی به ایران سفر نکنید و اگر شهروند آمریکایی در ایران هستید، فوراً کشور را ترک کنید.
همچنین به شهروندان آمریکایی توصیه میشود از تجمعات بزرگ دور بمانند، هشدارهای امنیتی را دنبال کنند و اطلاعات سفر خود را در سامانه STEP ثبت کنند.
شماره‌های تماس اضطراری وزارت خارجه آمریکا:
از خارج آمریکا و کانادا: ‎+1-202-501-4444
از داخل آمریکا و کانادا: ‎+1-888-407-4747
امور کنسولی شهروندان آمریکایی در ایران:
ایمیل: BernACS@state.gov
تلفن سفارت آمریکا در برن: ‎+41-31-357-7011
توجه: بخش سوئیس حافظ منافع آمریکا در تهران موقتاً تعطیل است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/25305" target="_blank">📅 23:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25304">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">علیرضا بیرانوند پس از اتفاقات روز گذشته و درگیری لفظی با مدیران باشگاه تراکتور، امروز در اردوی این تیم پیش از اعزام به عمان در هتل حاضر شد اما در اقدامی جالب مدیران باشگاه تراکتور او را از اردوی تراکتور
اخراج کردند.
@WarRoom
👃</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/25304" target="_blank">📅 23:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25303">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نیویورک‌تایمز گزارش داد کاخ سفید سمت سخنگویی را به کیتی زکریا، مفسر محافظه‌کار و مشاور ارتباطات نزدیک به دونالد ترامپ، پیشنهاد کرده است. او پیش‌تر نیز برای مدتی سخنگوی وزارت امنیت داخلی آمریکا بود. در صورت نهایی‌شدن این انتصاب، زکریا جایگزین کارولین لیویت…</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/25303" target="_blank">📅 23:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25302">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ: به‌تازگی گفت‌وگویی بسیار موفقیت‌آمیز با ولادیمیر پوتین، رئیس‌جمهور روسیه، داشتم که در جریان آن توافق شد روسیه فوراً بیش از ۳۰۰ هزار تن سوخت دیزل به بازار آمریکا و بازار جهانی عرضه کند. همچنین، ۵۰۰ هزار تن دیگر در طول ماه نوامبر و یک میلیون تن دیگر بلافاصله…</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/25302" target="_blank">📅 23:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25301">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شرق هم چنان گزارش سر و صدا میاد واسم
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/25301" target="_blank">📅 23:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25300">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سلامتی همگی</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/25300" target="_blank">📅 22:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25299">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhcsMHD5mgj-pzJFeeXr4Ih4JIo4OE3aknNgxbsJ40Gk_3JPcand3NXRL-r7TMxSpxDvoXGjim8rzfxg9xzxVJ5e4c_1DqMf0c90xRmfCRk7LRuFe5lRgSW9fiv4Jxsap4TSeWLJgMogDEoAvBlQbaHnrrUJQBv_J2s85ksnPYJaWzGqTmx0HoXdKeK4CU1fH1Nx7LTtPvYwRrqmFTUpp9Y4SS5nkuMPMmZUVLsFizuZbUJCzsOsQgRHqlQKZ1bZg4LBBD9TKh4h7EFcHFYoKyvFzLzE51vIQyxafpu9tOVniHmxccvhfvoii9eg1_EK0M4NNMxvNEERjQ6gjKUXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: به‌تازگی گفت‌وگویی بسیار موفقیت‌آمیز با ولادیمیر پوتین، رئیس‌جمهور روسیه، داشتم که در جریان آن توافق شد روسیه فوراً بیش از ۳۰۰ هزار تن سوخت دیزل به بازار آمریکا و بازار جهانی عرضه کند. همچنین، ۵۰۰ هزار تن دیگر در طول ماه نوامبر و یک میلیون تن دیگر بلافاصله پس از آن تحویل داده خواهد شد. علاوه بر این، با توجه به وضعیت پالایشگاه‌های دیزل روسیه، این کشور در مدت کوتاهی پس از آن، ۳ میلیون تن سوخت دیزل دیگر نیز عرضه خواهد کرد. با توجه به کنترل کامل ما بر تنگه هرمز و این خبر بزرگ درباره تأمین انرژی از روسیه، قیمت گازوئیل برای آمریکایی‌ها و در واقع برای سراسر جهان، به‌سرعت و با کاهشی بی‌سابقه پایین خواهد آمد! پایین آوردن قیمت‌ها برای مردم آمریکا، به‌ویژه کشاورزان، دامداران و رانندگان کامیون، بزرگ‌ترین اولویت من است. این خبر بسیار مهم و بزرگی است. همچنین باید روشن باشد که ایران به سلاح هسته‌ای دست پیدا نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/25299" target="_blank">📅 22:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25298">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">امشب مثل اینکه من باید جنگ راه بندازم</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/25298" target="_blank">📅 22:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25297">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اتاق جنگ با یاشار : ترابری ۲۴ ساعت پیش تا همین الانه الان ! دارن پرررر میان (عرزشی هستی نبین سکته میکنی) فقط آخرش که مال همین چند ساعته یکی از‌ زیبا ترین پل های هوایی شکل میگیره @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/25297" target="_blank">📅 22:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25296">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfsvHWhH6HTrrXa1az9ToeoDnXoTOjzLpjjaJd1rBxdObBuZo-IOcby7BDVnDposkT3wi2ctnA_J9kK0YoUojfWQzIQY1zmcPpJzYcN2eGyGV12VJ67JYuuepTgTTgI8lsjtFPn2F-ncK03vuTYOd9aQu1PmN045_VflzEHzd9eSlpOXrq1SoueUes7PVvThkP4i0IK6jiT5sj2wGyBTqMK6Y91r3ldwwPdnxzNmB8-WNBryA1pRpT7IT3BwD3pl5I6GpbNuXfD2i4RItgfxCUsYoHIwtqd8CSu0AkM1zdaP-vPbbXBTnAvXxYnTwulz-RsyQqqY1t-tAN5NZph40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز گزارش داد کاخ سفید سمت سخنگویی را به
کیتی زکریا
، مفسر محافظه‌کار و مشاور ارتباطات نزدیک به دونالد ترامپ، پیشنهاد کرده است. او پیش‌تر نیز برای مدتی سخنگوی وزارت امنیت داخلی آمریکا بود. در صورت نهایی‌شدن این انتصاب، زکریا جایگزین کارولین لیویت خواهد شد که در ماه اوت از سمت خود کناره‌گیری کرد. پذیرش نهایی پیشنهاد هنوز تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/25296" target="_blank">📅 22:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25295">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خلاصه پیغام های زیاد : تهرانپارس بین فلکه دوم و سوم انفجار شدید اومد آسمون رو دود گرفته و بعد صدای تیر اندازی شنیده شد! علت نامشخص ولی حمله هوایی نیست @WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/25295" target="_blank">📅 21:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25294">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">معاون وزیر خزانه‌داری آمریکا: بیش از ۱۵۰۰ فرد و نهاد مرتبط با ایران را تحریم کرده‌ایم
وزارت خزانه‌داری آمریکا دیروز هم ، تحریم‌های تازه‌ای علیه
۱۷ کشتی مرتبط با ناوگان پنهان نفتی ایران
اعلام کرد. هم‌زمان، وزارت خارجه آمریکا نیز ۱۰ نهاد، ۶ فرد و ۵ کشتی را هدف تحریم قرار داد
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/25294" target="_blank">📅 21:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25293">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGia56Mryujy1Nvyz5nSSDhbcOIxZOhgUB5spM7r-QY8o8aI-90Mr8YRqXTmgaA3SaENlK7BrfK93DSBoijP-8HU-inhRYU_Ty3jwyskP-fjzAkruz4kb4jW4upkrlzwiRXerTXZ1jEPKFhHCejJYXIaffV7BEoHMVFarZ2FDQLuUkjomQnmBr86qkKsFNIVWQWdbYXVdYGO1Cda5CHpAyWrB7oQ9Sj6TqBLXlDdLtKPdo_69icgLwIssTwjbgQ31dK6Rdn_RAR6ABfRIuofb3jyrdj2sRO1Hjr7mSwM_wjGMqs-c01rIxyccD_Kq8XKLLLqbt-Ec8AxRt8gxvV4Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: تا ۹ اکتبر، نیروهای آمریکایی ۱۳۳ کشتی تجاری را برای رعایت محاصره تغییر مسیر داده‌اند.
یک بالگرد نیروی دریایی آمریکا از ناوشکن موشک‌انداز «یواس‌اس جان پل جونز» برخاست؛ ناوشکنی که در پشتیبانی از محاصره دریایی آمریکا علیه ایران فعالیت می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/25293" target="_blank">📅 21:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25292">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bedb14bbb5.mp4?token=aTxrfLaHQZKwcdVyRVYR92tw3N0ajW6FeVgAG4ZF68fcEk1GoZ3bFjAwNLNNGC7u9zneKSicQDt3WBaSK0DnbCatJ21Ii-6oZtTGu1qom51n2nXeATQ5KCUDGta6oGi2UtpFbwIBJivXHmjFQU5DIzbXr6QjdUwPc1hBXwggGMvPBaNl9FZie0IdOdqBQoR1nqm7EYF1Zb19eF5XlyixAKzD68hqKa6Ua8cgpjIkKUi7WhlmqCgl1hpfxtL3BogafGFDhj4a54Ji-TjFvae03zFHdLjwsT6U8RqKCRzgMtVStJv5vH3btPUi4FY1MvR8COgoGuENLBvR6rcv-Bn1Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bedb14bbb5.mp4?token=aTxrfLaHQZKwcdVyRVYR92tw3N0ajW6FeVgAG4ZF68fcEk1GoZ3bFjAwNLNNGC7u9zneKSicQDt3WBaSK0DnbCatJ21Ii-6oZtTGu1qom51n2nXeATQ5KCUDGta6oGi2UtpFbwIBJivXHmjFQU5DIzbXr6QjdUwPc1hBXwggGMvPBaNl9FZie0IdOdqBQoR1nqm7EYF1Zb19eF5XlyixAKzD68hqKa6Ua8cgpjIkKUi7WhlmqCgl1hpfxtL3BogafGFDhj4a54Ji-TjFvae03zFHdLjwsT6U8RqKCRzgMtVStJv5vH3btPUi4FY1MvR8COgoGuENLBvR6rcv-Bn1Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏سنتکام : به لطف نیروهای ما  که با موفقیت مین‌های دریایی را از مسیرهای اصلی تردد پاکسازی کرده‌اند، مسیرهای عبور آزاد از تنگه هرمز برای تمامی شناورهایی که تحریم‌های دریایی آمریکا علیه ایران را نقض نمی‌کنند، باز است؛ در نتیجه، هزاران شناور تجاری با ایمنی کامل از این تنگه عبور کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25292" target="_blank">📅 21:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25291">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سخنگوی ارتش اسرائیل: امروز جمعه، در حمله‌ای هوایی در منطقه مرزی سوریه و لبنان، یوسف علی الحسن کشته شد. به گفته ارتش اسرائیل، او با هدایت جمهوری اسلامی در حال برنامه‌ریزی حملات علیه نیروهای اسرائیلی در جنوب سوریه، از جمله با پهپادهای انفجاری و راکت، بوده است. ارتش اسرائیل مدعی شد این طرح‌ها خنثی شده‌اند و اعلام کرد به اقدام برای رفع تهدیدها ادامه می‌دهد و به توافق با لبنان پایبند است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25291" target="_blank">📅 21:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25290">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انتقاد و تکذیب روایت تاریخی مارکو روبیو درباره جنگ‌های ایران و یونان باستان
مارکو روبیو، وزیر خارجه آمریکا، در سخنرانی خود در آتن، با اشاره به حمله خشایارشا به آتن در سال ۴۸۰ پیش از میلاد، تلاش کرد میان تاریخ یونان باستان و سیاست امروز آمریکا ارتباط برقرار کند.(تورج دریایی: ایران‌شناس برجسته و استاد تاریخ ایران باستان.)
می‌گوید این روایت بخشی از زمینه تاریخی جنگ‌های ایران و یونان را نادیده می‌گیرد؛ از جمله شورش ایونی‌ها و حمله یونانیان به سارد، مرکز مهم هخامنشیان، در سال ۴۹۸ پیش از میلاد. همچنین فتوحات اسکندر مقدونی و سقوط امپراتوری هخامنشی نشان می‌دهد که تاریخ این دو تمدن، برخلاف روایت یک‌طرفه از حمله ایران به یونان، مجموعه‌ای پیچیده از جنگ‌ها، لشکرکشی‌ها و رقابت‌های سیاسی بوده است.
آتش‌گرفتن آتن واقعیتی تاریخی است، اما استفاده از آن برای ترسیم تقابل تمدنی میان ایران و غرب امروز، نیازمند در نظر گرفتن تمام زمینه تاریخی است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25290" target="_blank">📅 21:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25289">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فرمانداری چابهار خبر واگذاری ۱۱۰ هکتار از اراضی این منطقه به افغانستان را تکذیب کرد. این شایعه پس از انتشار گزارش‌هایی درباره اختصاص زمین در بندر چابهار و منطقه آزاد برای سرمایه‌گذاری افغانستان مطرح شد. با این حال، تکذیب واگذاری زمین به معنای رد کامل موضوع اختصاص اراضی برای سرمایه‌گذاری نیست؛ چراکه اختصاص زمین برای اجرای پروژه‌های اقتصادی با واگذاری مالکیت یا انتقال اراضی به یک کشور دیگر تفاوت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25289" target="_blank">📅 21:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25288">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سپاه تصاویری را منتشر کرد که نشان می‌دهد پهپادهای شاهد در جریان جنگ، به سمت کشتی ها پرتاب می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25288" target="_blank">📅 21:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25287">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ایلان ماسک به اپراتورهای موبایل اعلان جنگ کرد!
اسپیس‌ایکس با توافقی ۸ میلیارد دلاری برای خرید فرکانس‌های رادیویی باند ۸۰۰ مگاهرتز، گام بزرگی برای رقابت با اپراتورهای موبایل برداشت. این شرکت همچنین مجوز استقرار ۱۵ هزار ماهواره نسل جدید برای ارائه اینترنت مستقیم به گوشی‌های معمولی را دریافت کرده است؛ طرحی که می‌تواند وابستگی کاربران به دکل‌های مخابراتی زمینی را کاهش دهد. البته انتقال کامل شبکه موبایل به فضا هنوز واقعیت ندارد
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25287" target="_blank">📅 21:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25286">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a757bdbbc.mp4?token=ViEI_L6oj9VaALC34PsbxTx1584cXnLH_cjVj4dyp_Tewxcq-bg9aGDa97A4aR-dqPwrqZ0nWwx3ty80QjrYXs31Qymj_XQLtmRnuN-GDS-ua6-gjUrZOA3HmHCWh-Ix7reHQxqbqT4sT9aa6YNPv-Ir5RI1UasWqshiFOhKewrVIZ1w31jDRblyQyiPYzn6BXNyPQ8b_Xasp0SGdke4Du-I_qqT3-J7mIA44cjdeXGHDxmtHjXNK8y-bWJjb14U5YHaFLkRjjRPEZ5prgVPQA_d8cmeIDpgwsnbOfdsJikPejMVU3KLTjOvgAAxybHbaV0-AJV7tzeX_njCqLFJOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a757bdbbc.mp4?token=ViEI_L6oj9VaALC34PsbxTx1584cXnLH_cjVj4dyp_Tewxcq-bg9aGDa97A4aR-dqPwrqZ0nWwx3ty80QjrYXs31Qymj_XQLtmRnuN-GDS-ua6-gjUrZOA3HmHCWh-Ix7reHQxqbqT4sT9aa6YNPv-Ir5RI1UasWqshiFOhKewrVIZ1w31jDRblyQyiPYzn6BXNyPQ8b_Xasp0SGdke4Du-I_qqT3-J7mIA44cjdeXGHDxmtHjXNK8y-bWJjb14U5YHaFLkRjjRPEZ5prgVPQA_d8cmeIDpgwsnbOfdsJikPejMVU3KLTjOvgAAxybHbaV0-AJV7tzeX_njCqLFJOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس ، معاون ترامپ : می‌دانیم که مردم نگران هزینه‌های معیشت هستند و این موضوعی است که هر روز با تمرکز کامل بر حل آن متمرکز هستیم
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25286" target="_blank">📅 21:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25285">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">واشنگتن‌پست: یک مقام ارشد دولت ترامپ اعلام کرد هرچه متحدان آمریکا سریع‌تر مسیرهای حیاتی ارتباط اقتصادی ایران با جهان را محدود کنند و منابع مالی و منافع جمهوری اسلامی را تحت فشار قرار دهند، واشنگتن زودتر به هدف خود خواهد رسید. دولت ترامپ با تشدید فشارهای اقتصادی، محدود کردن صادرات نفت و مسدود کردن مسیرهای مالی، در تلاش است ایران را به پذیرش خواسته‌های آمریکا وادار کند. با این حال، هنوز مشخص نیست این کارزار فشار چه زمانی به نتیجه خواهد رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25285" target="_blank">📅 21:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25284">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25284" target="_blank">📅 20:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25283">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خلاصه پیغام های زیاد : تهرانپارس بین فلکه دوم و سوم انفجار شدید اومد آسمون رو دود گرفته و بعد صدای تیر اندازی شنیده شد! علت نامشخص ولی حمله هوایی نیست @WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25283" target="_blank">📅 20:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25281">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BqY7K2ye3nNv2R9boBD7J3_3h2p_qORfKi4Mu5fPhmdp8ZI7S_FdcSVF_BCEc-ETH-I3bX8MCJRTB_H23KsNEqlhjAUYKGEcVuNwKBB57s0Yeh4sYPlZpj88ZF3ksu9p76GIjVvrIYzBNnwgHoFTRCSiFZToHbTTwM8xsApZTPa28b-PR3O69fuTZRLHMnU3OFdCVSMqaNTy6sc_SN-pGa_wYpPcWustQKO_mkdX_c2Y1Stiv9gu-y3ILAqjR27ZThG48C_FnaZ4z9SeGxzhWMIvA-p8e5TtXDUPqbm6DPnhkh2gWM8tfJcpPUUelqMblf7MXO6RuMo6f4C_purd7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XFFcNMdPgr0fOxloUo8AT6UIjuZDhE8WvBMBF8BMvmLO3Y0sE95TtPOBYI65_aePvPDowJ6Sjf86XLStlcd0ZHQLkx8VRTnYSvkZSfAf_-yJUFXjGQb4lkIzd-sHRc-oky5TPiDFuoy91-9uRLQEnL4XlQA0dRHGrx_auO4WEYcOWZHO1E-GIoOF81AMpIVBOwv_TGJqB_XKLOKC9wAGaw4_bRHgB4FdtUfiLiKwSsPy0LZX4FQHVdEvTf2c5SEtbbQlO7HCyS-zrfXsnSLTtMVgFVGkGXruYWsE4d_5imqFisfsZBOfeS5Gkir2dXeBNNkYSMU2bm1QvjSVfR2wEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خلاصه پیغام های زیاد : تهرانپارس بین فلکه دوم و سوم انفجار شدید اومد آسمون رو دود گرفته و بعد صدای تیر اندازی شنیده شد!
علت نامشخص ولی حمله هوایی نیست
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/25281" target="_blank">📅 20:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25280">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">هم اکنون صدای انفجار مهیب از محدوده فلکه سوم تهران پارس ، شرق تهران ، دود مشاهده میشود
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/25280" target="_blank">📅 20:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25279">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a4aeebe5.mp4?token=FuwvQw9bkEKrv0FOGN5NbpoAtwE3mS7-RPL3jbTgn-ueHBf5CF7ONRF3MeBf30nCqrCD4gLJvrGCqf_xH3WGMAGzlfkgOcYrKrFy1zqPhXwX1nLHgveIFmQomueIz3WhTTgmpvI2-Ap_TjKzrtE_5ccBz9g23Jr_81mKQRgWcpQM28zSppQQHGdLkXPKquAaUsrLAitEyDVcY-b6Rkb3tNILiqcJ5KWbPqzrtYdw9klANhWL6Btn7E7AVkZZdHc8GReNhJxlG4CUcMLbhnhbTLZDRRTzbarhhs19_ZYoJogODWALC4WSqHJ17H_U_1E8pBWspZGNxwyg6Y_Gok5XCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a4aeebe5.mp4?token=FuwvQw9bkEKrv0FOGN5NbpoAtwE3mS7-RPL3jbTgn-ueHBf5CF7ONRF3MeBf30nCqrCD4gLJvrGCqf_xH3WGMAGzlfkgOcYrKrFy1zqPhXwX1nLHgveIFmQomueIz3WhTTgmpvI2-Ap_TjKzrtE_5ccBz9g23Jr_81mKQRgWcpQM28zSppQQHGdLkXPKquAaUsrLAitEyDVcY-b6Rkb3tNILiqcJ5KWbPqzrtYdw9klANhWL6Btn7E7AVkZZdHc8GReNhJxlG4CUcMLbhnhbTLZDRRTzbarhhs19_ZYoJogODWALC4WSqHJ17H_U_1E8pBWspZGNxwyg6Y_Gok5XCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: بعد از آن، موشک‌هایشان به سمت کشور ما حرکت می‌کردند. آن‌ها در تلویزیون با این موضوع شوخی می‌کنند و می‌گویند: «تو گفته بودی قرار است لس‌آنجلس را هدف قرار دهند!» اما واقعیت این است که مسیر پرتاب موشک به سمت شهرهایی مثل سن‌دیگو و لس‌آنجلس برای آن‌ها مناسب‌تر بود. البته احتمالاً پیش از آمریکا، اروپا را هدف قرار می‌دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25279" target="_blank">📅 20:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25278">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بن‌گویر وزیر امنیت اسرائیل : زنده باد جنگ.
@WarRoom
😂
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25278" target="_blank">📅 19:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25277">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b2196422.mp4?token=X_EjDSwoy-758RQQ5gy6vq5cLdfgnsBNH30AdoYMyBFIeH1GS4zcWXF9ZVla0rr-OqyLpIi0WC3AXxu3siexp-ZKUnG2GTC_UXD83yLtm7t3LOgl2zJa1nG75KdfyTy1uqOdcS52xN5nDBqUeaOZ_CBNqbl4Cv9IlvsObRjmbP0awPwEurwa5gyzXjZNUwEvuMAT98BbZ0rycy55CPiwCHaNcziyfLKBb9ZK5tuqHdtX6Zx-6qGO47NkW01l8lGjNRHZno52Koux4kwR81yb_cNUkMhBFHU0mmoLtZmFAg_oFNzF9EwzH4TdeTuVUTO28znXWEsWp-MvfX8WhQPRlHtTXgQrpetCRmhtj3GloOCMGRBZwXkKGPQ8YYc2rN6kMMisN04UT0mOP26tPAazjnWedDG8BBE7hAmjslCJq45i3m-mL_6PeDMoPBlVwYho9aQ3sjmPgrBkqN211_9AXQTvzgx9E6gr-Qbn5Izhz3LJfmQOfJ8m42djJipbC_zOIxV8kzFDY3JvH0mP_XR-LFSCcTd3OXUExqDdLIyfj-06D_XgVfFX0j2Pwda3cPPMggG6-bkb5dcNFvdBsDRlmfIG_i5HXUtZOQ-6tCHax9SDNhb7LU7GGgPQweVYoEPJKpFiCxhrdTk5G-9HIe4THtkUqYvFpP5H9UCfoFEhU44" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b2196422.mp4?token=X_EjDSwoy-758RQQ5gy6vq5cLdfgnsBNH30AdoYMyBFIeH1GS4zcWXF9ZVla0rr-OqyLpIi0WC3AXxu3siexp-ZKUnG2GTC_UXD83yLtm7t3LOgl2zJa1nG75KdfyTy1uqOdcS52xN5nDBqUeaOZ_CBNqbl4Cv9IlvsObRjmbP0awPwEurwa5gyzXjZNUwEvuMAT98BbZ0rycy55CPiwCHaNcziyfLKBb9ZK5tuqHdtX6Zx-6qGO47NkW01l8lGjNRHZno52Koux4kwR81yb_cNUkMhBFHU0mmoLtZmFAg_oFNzF9EwzH4TdeTuVUTO28znXWEsWp-MvfX8WhQPRlHtTXgQrpetCRmhtj3GloOCMGRBZwXkKGPQ8YYc2rN6kMMisN04UT0mOP26tPAazjnWedDG8BBE7hAmjslCJq45i3m-mL_6PeDMoPBlVwYho9aQ3sjmPgrBkqN211_9AXQTvzgx9E6gr-Qbn5Izhz3LJfmQOfJ8m42djJipbC_zOIxV8kzFDY3JvH0mP_XR-LFSCcTd3OXUExqDdLIyfj-06D_XgVfFX0j2Pwda3cPPMggG6-bkb5dcNFvdBsDRlmfIG_i5HXUtZOQ-6tCHax9SDNhb7LU7GGgPQweVYoEPJKpFiCxhrdTk5G-9HIe4THtkUqYvFpP5H9UCfoFEhU44" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما مانع دستیابی جمهوری اسلامی به سلاح هسته‌ای شدیم و این موضوع به‌زودی، به یک شکل یا شکل دیگر، حل‌وفصل خواهد شد.
ترامپ: ایران دیگر ارتش، نیروی دریایی، نیروی هوایی یا سامانه‌های پدافند هوایی ندارد.
ترامپ: دیروز بیشترین حجم نفت از زمان آغاز جنگ از تنگه هرمز عبور کرد.
ترامپ: دیروز ۲۸ میلیون بشکه نفت از تنگه هرمز عبور دادیم؛ رقمی که از زمان آغاز جنگ بی‌سابقه بوده است.
ترامپ: خبرهای مهمی درباره بحران گازوئیل داریم و برای حل این ران با قدرت اقدام خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25277" target="_blank">📅 19:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25276">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b00c1954a3.mp4?token=JdRwLlYmQy-dG5_3-GyN8WiRVWQK7wwR28kbXlE5yzsQrdXG6lMvYxwb2-QRpnYYHJikBcJ8r8m1v7iJ0bds90dyT-ytgosKy1B9a58RXVZSoHZQaVuyfw-z9DQan2lS_NU3Ids2WjTwUhP5u3QyWLsNV2BNalL6zFOEEIYnAKfi09CFz1hOve1HG94xlFz-cn-WfSB0uFFw7WxTtv-FKwtnymb5RmOUL-eD_3u5jn_laMUYHEy_PIv300uoJYRhbrRwIYYRBk44RH_dWJwHpqFMWWpnZtIlstSva9nE-I1XckJeCs5q26AnE2Xhkr32REaogrKJDLNAFi0Kv1763w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b00c1954a3.mp4?token=JdRwLlYmQy-dG5_3-GyN8WiRVWQK7wwR28kbXlE5yzsQrdXG6lMvYxwb2-QRpnYYHJikBcJ8r8m1v7iJ0bds90dyT-ytgosKy1B9a58RXVZSoHZQaVuyfw-z9DQan2lS_NU3Ids2WjTwUhP5u3QyWLsNV2BNalL6zFOEEIYnAKfi09CFz1hOve1HG94xlFz-cn-WfSB0uFFw7WxTtv-FKwtnymb5RmOUL-eD_3u5jn_laMUYHEy_PIv300uoJYRhbrRwIYYRBk44RH_dWJwHpqFMWWpnZtIlstSva9nE-I1XckJeCs5q26AnE2Xhkr32REaogrKJDLNAFi0Kv1763w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: دیروز ۲۸ میلیون بشکه نفت از منطقه تنگه هرمز خارج کردیم؛ فکر می‌کنم این رقم از هر زمان دیگری، حتی قبل از جنگ، بیشتر است.
ترامپ درباره محاصره دریایی: ما محاصره برقرار کردیم و هیچ‌کس از آن عبور نمی‌کند. انگار اگر محاصره را به ایتالیایی‌ها می‌سپردم؛ شاید آن‌ها حتی بهتر هم عمل می‌کردند، اما شما این کار را خیلی خشن و با شدت انجام می‌دهید.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25276" target="_blank">📅 19:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25275">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edb5373c67.mp4?token=S9UxPndMvv_rX-yn19WIrkFdTs2i31c_gvDkwUu94MTLd0JhiwlVE87rLBuDh9-hzQDRIfB4bOq8h01RtD9LXRw1ssWZ9SK-nLWDKQqxL0KnAAbaL-ff8KFcQ_6pgmGD3IaoVLy7uskHBGow6fL1fj03n8VUpQcVPwt0ISV57CzCTBzTpZKJrm389hc9X1JStDgGyKiJTFH7Ye60Fuv-fOOFjE093oHHw2NvpkFRiGUGJY1cQm2HzKIRMCXSXhM2RUP9M4xc7S_7PfFEaeWOjmsFLNtE2BOJwGOfD8fuNYKQhEPM4GwqwpSe_T_Bh0nAydUMGvwL9RinG_xRMuua9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edb5373c67.mp4?token=S9UxPndMvv_rX-yn19WIrkFdTs2i31c_gvDkwUu94MTLd0JhiwlVE87rLBuDh9-hzQDRIfB4bOq8h01RtD9LXRw1ssWZ9SK-nLWDKQqxL0KnAAbaL-ff8KFcQ_6pgmGD3IaoVLy7uskHBGow6fL1fj03n8VUpQcVPwt0ISV57CzCTBzTpZKJrm389hc9X1JStDgGyKiJTFH7Ye60Fuv-fOOFjE093oHHw2NvpkFRiGUGJY1cQm2HzKIRMCXSXhM2RUP9M4xc7S_7PfFEaeWOjmsFLNtE2BOJwGOfD8fuNYKQhEPM4GwqwpSe_T_Bh0nAydUMGvwL9RinG_xRMuua9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران و محاصره دریایی: ایتالیایی‌ها شاید حتی بهتر از شما هم این کار را انجام بدهند، اما شما این کار را خیلی خشن و با شدت زیادی انجام می‌دهید.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25275" target="_blank">📅 19:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25274">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2623ad9e11.mp4?token=McWKoPAxeBzIG7wEIO8hIJjgeGGaMhHrK9NIEtg8hPq5NAHGSdB4IJ7M1kzyAv-4x1EkePtdG2s4pcq54gOG-MfJG6LMd4Ai2bN501PRn39JEDU0mKxfaTkadbBbwRZyks5y-QVKEd_O_6EHNSro1WLfWxkS6dTO-1G3QtC4Z0nb7UsrMgyP7jhRLlCCazQ1eTi1TaGfGNKOB8gS2Un_TE_zJpMZYbtUPMo8tuJqbbmC5EwDn05i7i_HCzXf5i2SqoXCIN6xua3Sr75VdNAvjh-zlMQvg82zYwNe4seA420JpwvYuJmsyWevzDv_wbmeceBZ3zo44xzfhQc9jdDUYqFsmdnQhHfQWtU5ePYTuNdV7WfTWqzOYXufz8YpoP_6uNyuXoQsWoVASrLYno2QrsIi419Ya6O6HjpajiVAsfVjnDcx_afMWLrnXl9rv7-QWcpRESX24Pa-TMEIHg7jJYV-asngrP8x36sIYT8pURcJjoWibbbPavbunUNekL7OZ-RWfH45xi25WrfNmas3FrSkxNCpMpyl7OMADnodpZ-A1sDjdbQKe-thSLTBFsYgDyHCNrD9U96vbVRvX4dAthdtJRRdBQRAduoL201tt67lmiaPWOPtSf66s8WLoo0BMZQnKnV3R6ZVbeDErg4UpEcGpZPL4bNQYuJVZlXRQ28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2623ad9e11.mp4?token=McWKoPAxeBzIG7wEIO8hIJjgeGGaMhHrK9NIEtg8hPq5NAHGSdB4IJ7M1kzyAv-4x1EkePtdG2s4pcq54gOG-MfJG6LMd4Ai2bN501PRn39JEDU0mKxfaTkadbBbwRZyks5y-QVKEd_O_6EHNSro1WLfWxkS6dTO-1G3QtC4Z0nb7UsrMgyP7jhRLlCCazQ1eTi1TaGfGNKOB8gS2Un_TE_zJpMZYbtUPMo8tuJqbbmC5EwDn05i7i_HCzXf5i2SqoXCIN6xua3Sr75VdNAvjh-zlMQvg82zYwNe4seA420JpwvYuJmsyWevzDv_wbmeceBZ3zo44xzfhQc9jdDUYqFsmdnQhHfQWtU5ePYTuNdV7WfTWqzOYXufz8YpoP_6uNyuXoQsWoVASrLYno2QrsIi419Ya6O6HjpajiVAsfVjnDcx_afMWLrnXl9rv7-QWcpRESX24Pa-TMEIHg7jJYV-asngrP8x36sIYT8pURcJjoWibbbPavbunUNekL7OZ-RWfH45xi25WrfNmas3FrSkxNCpMpyl7OMADnodpZ-A1sDjdbQKe-thSLTBFsYgDyHCNrD9U96vbVRvX4dAthdtJRRdBQRAduoL201tt67lmiaPWOPtSf66s8WLoo0BMZQnKnV3R6ZVbeDErg4UpEcGpZPL4bNQYuJVZlXRQ28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : ترابری ۲۴ ساعت پیش تا همین الانه الان ! دارن پرررر میان (عرزشی هستی نبین سکته میکنی) فقط آخرش که مال همین چند ساعته یکی از‌ زیبا ترین پل های هوایی شکل میگیره
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25274" target="_blank">📅 19:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25272">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">😾</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/25272" target="_blank">📅 18:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25271">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رویترز: دولت ترامپ تحریم‌های گسترده‌ای علیه دیوان کیفری بین‌المللی اعمال کرد که ممکن است دسترسی این نهاد به خدمات بانکی، بیمه و نرم‌افزار را مختل کند. این اقدام در واکنش به صدور حکم بازداشت برای بنیامین نتانیاهو و دیگر مقام‌های اسرائیلی و تحقیقات قبلی درباره…</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25271" target="_blank">📅 18:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25270">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یسرائیل کاتس، وزیر دفاع اسرائیل: یائیر گولان اکنون با حذف خامنه‌ای و عملیات «غرش شیر» مخالف است؛ نفتالی بنت با عملیات «ملت شیر» مخالفت کرد؛ یائیر لاپید بخشی از قلمرو حاکمیتی اسرائیل را به حزب‌الله واگذار کرد؛ آویگدور لیبرمن می‌خواهد بزرگراه ۶ را به کنترل یک ارتش عربی بسپارد؛ گادی آیزنکوت می‌خواهد از لبنان فرار کند و منصور عباس پشت پرده پنهان شده است. اگر این‌ها گزینه جایگزین باشند، چه جای تعجب دارد که همه دشمنان ما برای سرنگونی نتانیاهو و دولت راست‌گرای او تلاش می‌کنند؟
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25270" target="_blank">📅 18:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25267">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIz0gbdjJHT_4pNq_ufPIsvsl1P_Qk9lr9XlwyqY2YyoOJ0gh51DmhouzfTBAC1qp1kgpkUJi5hamQXl1LF1B4ZXeeSjOBziUrpxsvnnCJCngNaZo4TchB79ZPlUHR8aaRGv7jPp7XQWvZNC_VUSIvxr3V531c0Jj_JfFKRfN00Kcd2d_2M1YFDKmOGoin9C8axACZUWL-U2_0VB3eU3Xx3GxOBjhIwrUAJcep5cMX1uSKw9fxgQ4MWBsz3po-Y3LhuF07gGcGSVrqUmBKtmEaKjpo5bYAJIXk6pfkXUeSCIY32bcKP3_v_TcbKm5v5xpQ5Xo4LRxZX6YNYmaCNw_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/683fae1eda.mp4?token=qNu-y8hHMmVWdNLlOvCN62tYFngehhFExBkNNTltIVafy-J0QPZPa2JKHa53XX2LIxJZa6xpPVP02YSwRvRGrcwGvELzv5onVWveWx2sykS6Ye-8Uijj4zmp91gvcuBireOTtSEvrMa72WyFhRiJ2lFcc06dMvEgZyqSSHDhStqP5OFvM8p6BW4FePte__oWshgUDfnKXy8LX_CrJj5sgfsDCp_r_kpy1PoyjkbfUW-tDnr9DgeSjknjLOCXIAvi0GNI0Za8axXjgpYVkvz0TxRwJqp4QpZOWWjpZ3_pr6wNlK3bcKmYjWYz_6QdWcQoNDQWUVIiehhrkM1pFJ_otQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/683fae1eda.mp4?token=qNu-y8hHMmVWdNLlOvCN62tYFngehhFExBkNNTltIVafy-J0QPZPa2JKHa53XX2LIxJZa6xpPVP02YSwRvRGrcwGvELzv5onVWveWx2sykS6Ye-8Uijj4zmp91gvcuBireOTtSEvrMa72WyFhRiJ2lFcc06dMvEgZyqSSHDhStqP5OFvM8p6BW4FePte__oWshgUDfnKXy8LX_CrJj5sgfsDCp_r_kpy1PoyjkbfUW-tDnr9DgeSjknjLOCXIAvi0GNI0Za8axXjgpYVkvz0TxRwJqp4QpZOWWjpZ3_pr6wNlK3bcKmYjWYz_6QdWcQoNDQWUVIiehhrkM1pFJ_otQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع محلی از کشته شدن معاونت اجتماعی انتظامی استان سیستان و بلوچستان در منطقه چشمه زیارت زاهدان بر اثر یک بمب کنار جاده‌ای خبر می‌دهند. @WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25267" target="_blank">📅 18:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25266">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رویترز: دولت ترامپ تحریم‌های گسترده‌ای علیه دیوان کیفری بین‌المللی اعمال کرد که ممکن است دسترسی این نهاد به خدمات بانکی، بیمه و نرم‌افزار را مختل کند. این اقدام در واکنش به صدور حکم بازداشت برای بنیامین نتانیاهو و دیگر مقام‌های اسرائیلی و تحقیقات قبلی درباره…</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25266" target="_blank">📅 18:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25265">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رویترز: دونالد ترامپ که بارها گفته بود شایسته دریافت این جایزه است، امسال نیز برنده آن نشد. جایزه صلح نوبل ۲۰۲۶ به ناوانتم «ناوی» پیلای، حقوقدان اهل آفریقای جنوبی و کمیسر عالی پیشین حقوق بشر سازمان ملل، رسید. کمیته نوبل از تلاش‌های او برای تقویت حقوق بین‌الملل…</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25265" target="_blank">📅 17:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25264">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نیوزمکس : وزیر خزانه‌داری آمریکا گفته  است دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن تمام مسیرهای زمینی ورود و خروج از ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25264" target="_blank">📅 17:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25263">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">منابع محلی از کشته شدن معاونت اجتماعی انتظامی استان سیستان و بلوچستان در منطقه چشمه زیارت زاهدان بر اثر یک بمب کنار جاده‌ای خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25263" target="_blank">📅 17:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25262">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/von-RjIKdxxAX5t3NbjcwS-m-z5NKkHW5HDFqrSV1Uys3yHdZkSRaukP9rrzWbEcZPYqEda_dL22aHK44l1CplHMjPNDmiu4IXSSxMDwggA7UhQGdbo6Ri9tYPEWOhFtZlzFarxdmJBfMgbW3Z41UwQ-09aUiC2pkhQB5Rv5NiON8OCbq1fhLpX0JPCV5QOpP1tlqIjawo1-k67rs3r4tuupw-6FvTp7YQpJusqflzzAA26hTpNJI3ZqGLIH_tBOpVW3IKXfBxZv9fvNzeQJFEpjbEQ2J_DDdUtu4_D3soW2FV8QE2Ktg8qsJsUdnh_8Q9Z4UoSBGwK2yG7qP0pC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:مربی تناسب اندام ناو هواپیمابر یو اس اس جورج واشنگتن (CVN 73) که در کشتی با نام «رئیسِ خوش‌‌اندام» شناخته می‌شود، اعضای خدمه را در طول تمرین در آشیانه هدایت می‌کند. این ناو هواپیمابر به عنوان یک شهر شناور، دارای امکانات تناسب اندام متعددی است که به صورت شبانه‌روزی در دسترس هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25262" target="_blank">📅 16:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25261">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بسنت: سپاهی‌ها دیگر نمی‌توانند برای دیدن جراح پلاستیک‌ و دوست‌دخترشان به خارج بروند
اسکات بسنت، وزیر خزانه‌داری آمریکا، از اجرای کارزار «انزوای مطلق» علیه جمهوری اسلامی خبر داد و اعلام کرد دولت پرزیدنت ترامپ با استفاده از محاصره دریایی، محدودیت پروازهای بین‌المللی، مسدود کردن مسیرهای زمینی، و توقیف دارایی‌های دیجیتال، در تلاش است ارتباط اقتصادی و مالی حکومت ایران با جهان خارج را قطع کند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25261" target="_blank">📅 16:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25260">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سپاه پاسداران اعلام کرد کشتی غول‌پیکر حامل گاز مایع (LPG) با نام اِن‌وی سان‌شاین (NV Sunshine) متعلق به شرکت نات‌ویت، هنگام عبور از مسیر غیرمجاز در جنوب تنگه هرمز هدف قرار گرفته و در بخش موتورخانه و سامانه رانش دچار آتش‌سوزی شده است و هشدار داد اقدامات علیه کشتی‌هایی که از مسیرهای غیرمجاز عبور کنند، به تنگه هرمز محدود نخواهد ماند و این شناورها در سراسر منطقه تحت تعقیب قرار خواهند گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25260" target="_blank">📅 16:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25259">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">در سرقتی بزرگ از کارخانه شراب‌سازی
مارکزی آنتینوری (Marchesi Antinori)
در منطقه توسکانی ایتالیا، حدود
۳۰ هزار بطری شراب به ارزش ۵ میلیون یورو
به سرقت رفت.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25259" target="_blank">📅 15:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25257">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25257" target="_blank">📅 15:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25256">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آکسیوس: احتمال ازسرگیری جنگ با ایران طی ۳ هفته آینده
به گفته باراک راوید، مقام‌های آمریکایی به رئیس ارتش اسرائیل از آمادگی برای احتمال آغاز مجدد عملیات گسترده علیه ایران خبر داده‌اند. زامیر هشدار داده این اقدام ممکن است به تعویق انتخابات اسرائیل منجر شود.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25256" target="_blank">📅 15:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25255">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سفارت مجازی آمریکا در تهران
از شهروندان آمریکایی حاضر در خاورمیانه خواست به‌دلیل شرایط پیچیده امنیتی،
حداکثر احتیاط را رعایت کنند
.
این نهاد هشدار داد که احتمال
لغو پروازها، بسته‌شدن حریم هوایی و اختلال در سفرها
وجود دارد.
همچنین با صدور
هشدار سطح ۴ (بالاترین سطح هشدار)
، تأکید کرد: «به هیچ دلیلی به ایران سفر نکنید» و از شهروندان آمریکایی حاضر در ایران خواست
فوراً این کشور را ترک کنند
.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25255" target="_blank">📅 15:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25254">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اخرین ویدیو ترامپ شب حمله</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25254" target="_blank">📅 15:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25253">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اورشلیم پست : منابع اسرائیلی دستوراتی دریافت کرده اند مبنی بر اینکه ، اسرائیل در صورت شناسایی آمادگی ایران برای شلیک موشک به آنها ، حمله پیشگیرانه را انجام دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25253" target="_blank">📅 15:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25252">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">العربیه به نقل از یک مقام آمریکایی: حمله گسترده به ایران در آخرین لحظه به تعویق افتاد
یک مقام نظامی آمریکایی به العربیه گفت ارتش آمریکا روز یکشنبه ۴ اکتبر، در آستانه اجرای حمله‌ای گسترده و مشترک با اسرائیل علیه ایران قرار داشت و نیروهای آمریکایی تا نیمه‌شب به وقت آمریکا در حالت آماده‌باش باقی ماندند و انتظار برای دریافت دستور نهایی حمله تا ساعات اولیه دوشنبه ادامه یافت؛ اما در نهایت دونالد ترامپ دستور حمله را به تعویق انداخت.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25252" target="_blank">📅 15:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25251">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الجزیره : حسین موسویان، دیپلمات پیشین ایران، و آلن ایر، دیپلمات پیشین آمریکا، ارزیابی کردند که درگیری در هفته‌های آینده احتمالاً
وخیم‌تر
خواهد شد و توافق صلح نزدیک نیست ، آکسیوس هم در گزارشی گفت
اختلاف اصلی پا برجا است
و نشانه‌ای از کاهش اختلافات از دو طرف دیده نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25251" target="_blank">📅 14:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25250">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شاهزاده رضا پهلوی در شبکه ایکس: «
تا وقتی این ساختار سر کار است، اصلاح ممکن نیست و سقوط ادامه دارد.
سقوط شتابان ریال، نابودی دستمزدها و پس‌انداز مردم و گران‌ترشدن زندگی روزمره، نتیجه مستقیم بی‌ثباتی، فساد، چاپ پول و سیاست‌های نابخردانه جمهوری اسلامی است.
تورم نزدیک به ۹۰ درصد، مالیات پنهانی است که حکومت از مردم می‌گیرد
و به جیب کسانی می‌ریزد که پول چاپ می‌کنند و زودتر خرج می‌کنند. تورم مهار نمی‌شود، اما سیاست‌های شکست‌خورده‌ای مانند دلارپاشی ادامه دارد؛
سیاست‌هایی که فقط ثروت خودی‌ها را افزایش می‌دهند.
»
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25250" target="_blank">📅 14:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25249">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کان‌ نیوز عبری :
ایلان شاگيف، یک مقام سابق ارشد شاباک، ادعا می‌کند که نخست‌وزیر بنیامین نتانیاهو بارها از پیشنهادات سازمان شاباک برای ترور مسئولان ارشد حماس خودداری کرده است.
او گفت: «هر بار که ما آماده بودیم، ایشان پاسخ می‌دادند: آمادگی خود را حفظ کنید.»
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25249" target="_blank">📅 14:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25248">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دو شهروند ایرانی در بریتانیا به دادگاه احضار شدند , آن‌ها یک بررسی اولیه و مشاهداتی را در مورد سفارت اسرائیل در لندن، یک کنیسه قدیمی در بریتانیا و سایر اهداف اسرائیلی و یهودی انجام داده بودند.
در کیفرخواست ادعا شده است که این دو نفر از این مکان‌ها عکس و فیلم گرفته و راه‌های دسترسی به آن‌ها را بررسی کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25248" target="_blank">📅 14:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25247">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رئیس‌جمهور ، زرشکیان : ما همواره بر اهمیت گفتگو تاکید کرده‌ایم، اما گفتگو زمانی ثمربخش است که با استفاده از زور و اجبار نباشد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25247" target="_blank">📅 13:52 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
