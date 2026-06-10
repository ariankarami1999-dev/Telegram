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
<img src="https://cdn4.telesco.pe/file/WaIisjjQRvtJP1DajXDstszTfTRPLKR4X8fQf9fJ5EnPMvBY97-C01z0C0_7slXrTk5fAmPmlzff651eV_Rqikq0CPN4umyDoRlxKU0mujeJrTN16nisPHESGFUIWArJzqtoMhDaUpvL8iIxxxmIcIVjwj6jKDHsBHgug0rD8-C90saEmHAEVoRNVrLrlhRISXPwoxR6CcnujSdQcGf6sMkNcZSJdqXm-fGCHB2VMANqHb8wdnlXg6MLJXGSiuZdtoMoA1T3jf20-4SFa7rj9LGKXH4Py9A-os4xiJPr92bSm2izwv4l6-u-jcYj8z2ue8JJjNBwDXnJxEF5v0-Eyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.63M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 14:36:43</div>
<hr>

<div class="tg-post" id="msg-658018">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tqpm71swWzAmiql7MgEqm5o8mAlFRm2frYBSLBx3lrXPHgm-tQpWG8iBEzvIlN2Y30bjZ6ullDskZSUSZblbhoRfEe7ZfzP3DBaO3cos8VKleXSaN2eZLS9OYOoPS6UB-ylxg98AndhjwGmqq7F-O6UBIOAxDUvE1JzmEZtkIhjeT_kIoUgIiwFPtmb1oiQZFjjfsR-YIQDQ9UAIe6nkycCxbjiFMecVbwUCOcdmQt07hmUjLyvveGDMA4Y12F8ZCSIjwpD1qLhvlHd3PFZ_0DFIq2S96rW8MLapt2pEVqASUE1RZ3Hy1id1ov4fcouLgjrNJ50NnwS1lJCBI0GOVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ کالای برتر تجارت جهانی
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 11 · <a href="https://t.me/akhbarefori/658018" target="_blank">📅 14:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658016">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
قالیباف: جمهوری اسلامی ایران به هرگونه تجاوز با قاطعیت و بدون درنگ پاسخ می‌دهد
رئیس مجلس:
🔹
با وجود شهادت فرماندهان و دانشمندان در جنگ ۱۲ روزه، نه حرکت علم و دانش در کشور متوقف شد و نه توان دفاعی و بازدارندگی ایران کاهش یافت.
🔹
فرماندهان شهید و دانشمندان کشور با سال‌ها مجاهدت و ایستادگی، نام خود را در حافظۀ تاریخی ملت ایران ماندگار کردند.
🔹
ملت ایران ثابت کرد که پیروزی نه در تجهیزات و امکانات، بلکه در میدان اراده‌ها رقم می‌خورد.
🔹
جنگ‌های تحمیلی اول، دوم و سوم به جهان نشان داد که مسیر فتح و پیروزی از دل ایستادگی و شهادت می‌گذرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/658016" target="_blank">📅 14:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658015">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c69e0ed52.mp4?token=NHd_fv1mZOYOyCm6rleGfcgFTv08iIHdn8JN1dxq5wuhRdYh9Zm60Wt6Q1wqB_IwHPyCVlpcPzv8K4Gy0Nl1UOVwr4FLhN1vx0I8gXfV6IlweVvr2b3JMxbkeoewyfUj0kWHuauRkDPE16OLBZUgYiXMbcZDGk4UWT2V3zDVo3QvJGdy6b5TGyoV-cXs7dcVrdEKJ2STmBOtb3WOgvh_u3iqGAsOTwyYRnSyw1xxVTUqQN04ecMsG6Cy_mBw3FE5FxpYIJjqho8TRKRk0ybj6lVruT32oHyguf1BvgZI54CZrmRsTIvU1cXPazL8nuPZBf348vi2N-4eLygsLQvHxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c69e0ed52.mp4?token=NHd_fv1mZOYOyCm6rleGfcgFTv08iIHdn8JN1dxq5wuhRdYh9Zm60Wt6Q1wqB_IwHPyCVlpcPzv8K4Gy0Nl1UOVwr4FLhN1vx0I8gXfV6IlweVvr2b3JMxbkeoewyfUj0kWHuauRkDPE16OLBZUgYiXMbcZDGk4UWT2V3zDVo3QvJGdy6b5TGyoV-cXs7dcVrdEKJ2STmBOtb3WOgvh_u3iqGAsOTwyYRnSyw1xxVTUqQN04ecMsG6Cy_mBw3FE5FxpYIJjqho8TRKRk0ybj6lVruT32oHyguf1BvgZI54CZrmRsTIvU1cXPazL8nuPZBf348vi2N-4eLygsLQvHxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مادر شهیده زهرا حداد عادل، همسر رهبر معظم انقلاب: داماد من قبل از اینکه به خواستگاری بیایند تافل‌شان را گرفته بودند، اهتمام زیادی به یادگیری زبان‌های خارجی داشتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/658015" target="_blank">📅 14:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658014">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887a04c96d.mp4?token=uyjTxu1cNIhgsZOxgEh_7U2Q_sREID5sKWvu_uoRaGHC12KnuNRbJeEC75GuhAolSUYzaElMbRU-FoCgnI6KK-2-PMqA2X3-GRGXMtitm_Sdslz8pRu6GYtf9Q1LbxM81pTGW-Rfd-9YmHAbgeLHOKzYibPb3AGY2r2K-Wqd7NufdAHH2L0cVstqcBddR1xdW5cO5XwgW4ahpjZUSrB0gS0QRNQVNgW49lr9w8_foCtNZT5jZ_2Xq77v44cjowyzcknQ3IKgXxEwPAOtIgNGLmQzQZ0bVEkOmrdRS58F9WxyKz1Mguydl3DW044DxPhdUWofhs6fEETVSmcDvg9nXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887a04c96d.mp4?token=uyjTxu1cNIhgsZOxgEh_7U2Q_sREID5sKWvu_uoRaGHC12KnuNRbJeEC75GuhAolSUYzaElMbRU-FoCgnI6KK-2-PMqA2X3-GRGXMtitm_Sdslz8pRu6GYtf9Q1LbxM81pTGW-Rfd-9YmHAbgeLHOKzYibPb3AGY2r2K-Wqd7NufdAHH2L0cVstqcBddR1xdW5cO5XwgW4ahpjZUSrB0gS0QRNQVNgW49lr9w8_foCtNZT5jZ_2Xq77v44cjowyzcknQ3IKgXxEwPAOtIgNGLmQzQZ0bVEkOmrdRS58F9WxyKz1Mguydl3DW044DxPhdUWofhs6fEETVSmcDvg9nXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی خضریان، عضو کمیسیون امنیت ملی مجلس: مطلع هستیم اردن پایگاه و آسمان خود را در اختیار آمریکا قرار داده است و حملات به اردن پاسخی دفاعی بود/ تاکنون ۱۶ پایگاه آمریکایی در منطقه مورد هدف قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/akhbarefori/658014" target="_blank">📅 14:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658013">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0072a5f4.mp4?token=kuqyOkBsul6Y5ox8RnQHOKkap-cakLbp03cU1fuxzyVGmKzerAbRA7cx9C-ylX22JLxekzwbP3oBGGlXFTRG0OifphsiElVsLBoNTwISPZ04-T7nZwTm8maXCk_BcH4nSv1c4bkAPAJaCbTSaHcHKM89iRN1HuNNaqu-YQYVOtzzFD8mXA7UXU9jKWC3_UWCT5wT-KaJetuCr1d1QONsMG-32E9E7rd-yioVOLW7o9WIZu2VgJWTZjcOex8LFUsidSHkPBTq1HCzeWwUIw2lbEAjXySYxihBbKwDQzl6Ohf1OFUfAZ-7aXuWH8_sLBshQp8Bs_mVEd0TlxB7OJog0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0072a5f4.mp4?token=kuqyOkBsul6Y5ox8RnQHOKkap-cakLbp03cU1fuxzyVGmKzerAbRA7cx9C-ylX22JLxekzwbP3oBGGlXFTRG0OifphsiElVsLBoNTwISPZ04-T7nZwTm8maXCk_BcH4nSv1c4bkAPAJaCbTSaHcHKM89iRN1HuNNaqu-YQYVOtzzFD8mXA7UXU9jKWC3_UWCT5wT-KaJetuCr1d1QONsMG-32E9E7rd-yioVOLW7o9WIZu2VgJWTZjcOex8LFUsidSHkPBTq1HCzeWwUIw2lbEAjXySYxihBbKwDQzl6Ohf1OFUfAZ-7aXuWH8_sLBshQp8Bs_mVEd0TlxB7OJog0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت یازدهم از فصل چهارم
🔹
در این قسمت روایت قسمت اول از تجربه‌ نزدیک به مرگ آقای مسعود نبی چنانی که به دلیل بیماری کرونا به کما می‌رود و در آنجا اجازه ورود از تاریکی به نور را ندارد و در کنار روح مادر همسرش حقایق زیادی می‌بیند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: مسعود نبی چنانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/658013" target="_blank">📅 14:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658012">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c50a24bda.mp4?token=Cs9mlhMQcM_DKik88MDQBnhH35DUxtYexTJg1Fnlq1quMZ7BGy1jpbrzqwB8JMM2aDN4DYXkuj8QCb9XZ07LvnEiQBY5rN2QPvCQoSxX7T3DWfynFt9hhLyWJoHbhy5wMeNGoRuqZh5R-zsSVrUaXw2WtiMFcbg5NL77wGqEQIMCMbj4H5Mq6MFInsR2odfaoT8zCMWtCYISEZZQrYF-OcoE0_riuBHaHISlbh8J-mmLONA3zgc8C1wG-MthlY_2Zl4lN2uijUwocEJTi4wPKyAZFXN2tk_GkWq516Vw0eODY8TxXWTU8ZL_jWLHkeI2oTx4Rswp3boTH-NfGBE0r34s79LU0BQnd68W5DRprrtHnhvS5HOSl4wydRNwDDCIFnVBBZB8skUwKm08PD7fCG73My_xaDfr0oAxIVISiFwtfTthWbfLhHYA3AhO1NyVW56iuUoJM8bi5Jq_17pXOhAWa77CYrqv6p5a1sTx_VBS23_Bhn9AMXpNKSkr61OrpfkB7zY4w3CfquW36Fq_TOjusCuabD07qW4e9rQfI0-Xil2_KiNjsHJzuoR23ZO-yb2dFa1i4qjJJ8Ox0Ty04-4LFemFRjh3KVxiaVWC382g2XOb58Uk5zNxO1Na0egLW5WWvSYAsLahOd3tQ2jNxKjbbsq8KzNUkvZ1eBDl4MM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c50a24bda.mp4?token=Cs9mlhMQcM_DKik88MDQBnhH35DUxtYexTJg1Fnlq1quMZ7BGy1jpbrzqwB8JMM2aDN4DYXkuj8QCb9XZ07LvnEiQBY5rN2QPvCQoSxX7T3DWfynFt9hhLyWJoHbhy5wMeNGoRuqZh5R-zsSVrUaXw2WtiMFcbg5NL77wGqEQIMCMbj4H5Mq6MFInsR2odfaoT8zCMWtCYISEZZQrYF-OcoE0_riuBHaHISlbh8J-mmLONA3zgc8C1wG-MthlY_2Zl4lN2uijUwocEJTi4wPKyAZFXN2tk_GkWq516Vw0eODY8TxXWTU8ZL_jWLHkeI2oTx4Rswp3boTH-NfGBE0r34s79LU0BQnd68W5DRprrtHnhvS5HOSl4wydRNwDDCIFnVBBZB8skUwKm08PD7fCG73My_xaDfr0oAxIVISiFwtfTthWbfLhHYA3AhO1NyVW56iuUoJM8bi5Jq_17pXOhAWa77CYrqv6p5a1sTx_VBS23_Bhn9AMXpNKSkr61OrpfkB7zY4w3CfquW36Fq_TOjusCuabD07qW4e9rQfI0-Xil2_KiNjsHJzuoR23ZO-yb2dFa1i4qjJJ8Ox0Ty04-4LFemFRjh3KVxiaVWC382g2XOb58Uk5zNxO1Na0egLW5WWvSYAsLahOd3tQ2jNxKjbbsq8KzNUkvZ1eBDl4MM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرایی تبدیل ایران به قطب چهارم جهان از زبان اندیشمند آمریکایی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/658012" target="_blank">📅 14:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658011">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
شورش در مکزیک در آستانه افتتاحیه جام جهانی ۲٠۲۶
🔹
یک روز به بازی افتتاحیه جام جهانی ۲٠۲۶، معلمان معترض مکزیکی برای چهارمین‌ بار اعتصاب گسترده‌ای به خاطر کم بودن دستمزدشان به راه انداختند و این‌بار تا ورزشگاه میزبان افتتاحیه رفتند. اعتراضات تا جایی شدید بود که ارتش مکزیک مجبور شد وارد عمل شود و این ورزشگاه را از دست معترضان نجات داد!
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/658011" target="_blank">📅 14:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658010">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
️
انهدام یک پهپاد متخاصم در آسمان خوزستان
🔹
یک فروند پهپاد متخاصم توسط شبکهٔ یکپارچهٔ پدافندی ایران صبح امروز در محدودهٔ روستای چال بلوطک شهرستان اندیکای خوزستان منهدم شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/akhbarefori/658010" target="_blank">📅 14:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658009">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f133308e2.mp4?token=GSA6EwGvKUeA6GTF5DJSRMYgTdQhhNZxVDRi66RiH0-bctc6q-FpTOIjkS3XWqVrmeFj3Njj2t3ez396l10vlm6rQsGDLq_sggbqwLQ8qM3c_CqwaB5UY0Gvz_nTPgSKX_BsdyHiXfhvOIMY9eU9n6kv6z8E_MUSm1fdNFJPKmvlVGoR27GbMZ-RXAJ2ZiaocCN8Zb0ruxFR5KObT2yJjT2kH4v1tGqWzW8LrtvBhZKTVhEm_KwZOFyhE4UhLkwQ5YiBF3pZqZOZiYteDXeR5mKa1wLebWBA8B0XATANxFTjI-daQrQMvG5Yxm6Qe4ptDPNPt74Fqcix-avyB-wSYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f133308e2.mp4?token=GSA6EwGvKUeA6GTF5DJSRMYgTdQhhNZxVDRi66RiH0-bctc6q-FpTOIjkS3XWqVrmeFj3Njj2t3ez396l10vlm6rQsGDLq_sggbqwLQ8qM3c_CqwaB5UY0Gvz_nTPgSKX_BsdyHiXfhvOIMY9eU9n6kv6z8E_MUSm1fdNFJPKmvlVGoR27GbMZ-RXAJ2ZiaocCN8Zb0ruxFR5KObT2yJjT2kH4v1tGqWzW8LrtvBhZKTVhEm_KwZOFyhE4UhLkwQ5YiBF3pZqZOZiYteDXeR5mKa1wLebWBA8B0XATANxFTjI-daQrQMvG5Yxm6Qe4ptDPNPt74Fqcix-avyB-wSYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران خانه همه ماست... #ایران_من
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/akhbarefori/658009" target="_blank">📅 14:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658008">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24df01c49a.mp4?token=II1IhYoGLex6TjiqzbCbXjgyW5YNvh9JYEs2lRNJyhKgnI79ZJVkdPgfdIE4wUKW0Qu6TRQiNia5Nv757vl2yZ5VdK2KpvUTjMt6PchwIdygAaUEdOG58Xk8mYMSPNfB7hqPQa9K_kxu5OOjnQ3wIN22xfwtScejJ845OYAafT72kgrUMJVjb9oMnTRAMX7bEsmy06iGsatFvpQLH1lQvjof8Bo2J5pSC20yNO-RNiAnQO5in3zfCFFLrsQtYCzLjaukuQdktM9OFIpxg9bGHxjd1ll7vTEa4zPjBR-viOMTS6gq20n0-D1nhgYvhywbe9jf24fmmEAJtqPv3Ed5mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24df01c49a.mp4?token=II1IhYoGLex6TjiqzbCbXjgyW5YNvh9JYEs2lRNJyhKgnI79ZJVkdPgfdIE4wUKW0Qu6TRQiNia5Nv757vl2yZ5VdK2KpvUTjMt6PchwIdygAaUEdOG58Xk8mYMSPNfB7hqPQa9K_kxu5OOjnQ3wIN22xfwtScejJ845OYAafT72kgrUMJVjb9oMnTRAMX7bEsmy06iGsatFvpQLH1lQvjof8Bo2J5pSC20yNO-RNiAnQO5in3zfCFFLrsQtYCzLjaukuQdktM9OFIpxg9bGHxjd1ll7vTEa4zPjBR-viOMTS6gq20n0-D1nhgYvhywbe9jf24fmmEAJtqPv3Ed5mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویرانی گسترده صور لبنان در پی بمباران اسرائیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/658008" target="_blank">📅 13:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658007">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت راه: برنامه‌ای برای افزایش قیمت نهضت ملی مسکن نداریم.
🔹
اموال ۴۷ نفر از خائنین به وطن در خراسان شمالی توقیف شد.
🔹
اردوغان: ما هم در معرض تهدید هستیم/ حملات به سوریه و لبنان را تحمل نخواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/658007" target="_blank">📅 13:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657998">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJxALYHF90TKyifi76d5ECvWyXIKTXD_aYuXTP2GpCABKlFYBgVgVRBJ6Fedbh4OAKrOFsEx43sJqB7Hgfe_bQZHaZJMj4lheqFS0xiCaIvNvPpqkwxqmEU4n6_hkwUNUEt-lGK7yttICznU1ZdwpRYZGJZMPOwrShSTNRrhludM3lUsKnbi2K8UsRSAbky3jwj3HPUWKhEEjslLR18hMD5DzK9d3y-Nys-t6KrjuZq9RjM5bz1avzj_vq3sHvZktVCTd8rJAn_XYxZCrXRiQt7Z-eF12JUG9PjgnMLkiJOwDYOumCAHge6Qi6cu2Jb5pxAdPIamIpVgnuCAlxlVnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UsUQeqmOOBMA3sCVaA0KpZeH8oSnF2EFPNJ9zrrOo0XU1e6tlUn02HoW_AVRjEe3IzbM0-wiOY5n4VaUkGNdxoh3rA6GGqtonB-1QTy3V7TTVg4RB2bHVri6cyZPftA3qvDp3M3sNV_Txvur8mSQJh5wohK4LsdXJIGsfnc3jXOCIfdMNJ9Ql4MTH1m8wuyLJa4QhcUhJ3iozm7C1dJe0Pkk6EqZzbJV5-Nc1lfnmgZZb4a0LtVYEt4m6yhS8p7crQ43zBSOrP4S3Wmn3BCWDOlAKVYVublPjsvkJpY_4MrJ18ycGoSly5TvdHi9GKq6Mh56k4FMwblH9T6-cNCKRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQOWidPAB6pdv8WuBTF_gESTyJZbaxhj5crFsLN8njpUuQaKhc1sj5PR3Gt5BxyKrwJL9kssJuoSJg3lnOJnmzYNPkuXfkj5-OHpq-yQVcqJbN6r_WOGk4tewyPZodKHScCXgDM9LG9gJEmtm40mL4tOgvUYZRXRSVyvNcb4Fk8zEnyLuvXy9yxocI6ADsZiFS3UqYpBadnmaxuNt5-SZelV2n6bBkbEdbErE6GMs38Wy3nOl0yyzNWooV4tDOsdSjtgU9xAbZI_L_4nZBOQVeUumaTIHs_GRuJqFNu0CH_xCREJBnZIfsDewtjxMRRtG_Wrb_LyEdJmJvqgEsSd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdmAJUP9aaiNn5niTdNbvUVooHCxf7dibAZzfq9UFartUuW-JEsCNYNVkFbkWttD5HP-MSw_pKRnNN_JgGT8gbEFcG3Y9x3fnjJ3bLdpOEasOCWId69p48LoS9GV2FKeQEzdJffsq-GChH4Cd38djr87dyRJOYnQFRoG1CWMzyfVV_q9Wssei9G9Kwl5m9hqUkCV9JKbbkn6-jKbJiGPPL7b4RR0OTdyqEG6Vo1A2wvJJ1HWVWUR1Tpt2fFE-OEY0wrQAJKoF0BtizzlveBc_s_UMQ4u4p6tqPjSuYOl4taZB_UMZDuABOoO9Pipzmub6EXoaA9Kd9WyM2nkgJubJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-ksnoirdPvlHquxfYN1WQ07UeH6958sCcUByWd_45Rf3J9OXyH7lpmVv-egQHiJtGbnxdxUpr0hWT8zYUds7r2ylDgfTpGlCHXq8Qyt5t4yIbpXopUFVOLlnXPYZlRHVCmHIMzcgFv0Lx9qa1Zs6Hjo5AyJTOLEjUtjQ8Ce0cgn3u0wtEez2JwIewb63BYHZ0J2evOcDIkKoPDD0O2KyfdryNsXzebVc647UH9yO5PxBSJuziG_whhZftG3AqogU0dhe0MwgqX1_a-yTmJXBSlNv2cJ-ilEuALwnwQImOBwgxHT4VOlGQwiMZSx8lfo-DIMPoc5ANT_IFgEFrBEjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-pTuMRvVFhkyunygK0IDqyFlwQJGWm34gW2TGuzII3Bkv1H2rkLSgZVyML_lgycm4IYoO3iFVLQpUhyY03ek7glGz2VBU7wGDydnHoirSdmf88PByHBk6p95ilGyVuwtVtc-2t-MoGpViuvc8KNs-xGijskyROsxrQmlQpp-_o_gW4kP4BFgOk9tIb8jDtsBJVBd1WollN5JtgrzdxbfrXU9aiI4u6CTa9MMr6L2dydet6tuL8vVlSxvN-Wb_mw06_B_pxhxu_mEUwYX5qHqakfJSyPAiGaIgfVODPRgjGuNAsDhZH-UYr8MlUta1wQN1va4C42lMAvSlqQSiYIIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_882jEr5kJxwVHzWc3b6jkcni8H9dwmfsRRGwsL3QV3BpwbwtlajoZnXvI8tMue3G9pJzIvWk075PLUBjQywmBc1tySChcqK3gLJZTnigQFJbVSyu2keR9eqJXEFVjDW3A2ZzXpA7EhLyk5Kt0fZvLUK0zKWb3hcpTDRszLokeJeHkhxmwMQGtqNEhP_PyzbsuoPcIvpBQK9rbniKjjKDIHbwrVNA7dLT8Hn6jLS93Z6VFDCH6S6E5pj2TVXBfOG80c1ltvMyArIoXiZW8u7hYW3kMBYKC-NlT5A6816ypUBwo4Y7ov63MIWSa8eIJrms8Kf2tkAqqSomrOalfCSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kAx5MGgTRbJLyES-BD28x1V3OfkEwR1sWPdRa31agstED5uCMY3MY-jXgEBfs9Z4GjVhY8KnQ8sFLJe8ag53KpHQ_MqL_fVTPzD2Ffa1_joqk5hCVimPLf5Mz6_vTB-7IuxyVeE78ypAZeatk3OFGlQ_tVRaHuMvo6UBRb3e1cFCCDuIZkGB-_ulrvsh8PYvu0ETk8cXZnN614Ktt1J7-GjvlyTZPdVoowMIq7mqGUUfzxcvyjecAPX1zqYQXF0j4pgMl4EbMFDKbyzLDKH5RvzfaNdePlq-HrGJzeROxIv4fECVe8Tz9PVKloYIAbugEgRNQ-QOOaxS__JH4UkGNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۸ استایل پر طرفدار پیتزا در جهان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/657998" target="_blank">📅 13:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657997">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54533a804c.mp4?token=otNeQ1_WSfkalSTS0lTVVwiC7I8Ggy7s8feuZHfcBjcrvoHhHpJ9yuZS8bc4jF0ro82E3CC72Ra7g3ai7EkYV0xQ40lFuNz_VBWpa9s3ljDn-02u9kZ5qIkQqM6QGFg0Q8c7scr2WejZzobgDNmY-z6PxJ4z1dBzQa-g4oS7vAcbcqiisXQl8l2VxOrTMqJI7Jkk5kYwmwBmcLsdwJ4vXfn1h5pGCyqvZUfpZPuF3r1HYh9E2qt8B2Z7l9HlIzzFkYmHGZzLtzDgi-KzdYvX_oaS3kWRZV3QUJRd2cWDtgyYl3a8xPELpL70sgTJ7d3WRs2udOuh3wE5P33YW6mS8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54533a804c.mp4?token=otNeQ1_WSfkalSTS0lTVVwiC7I8Ggy7s8feuZHfcBjcrvoHhHpJ9yuZS8bc4jF0ro82E3CC72Ra7g3ai7EkYV0xQ40lFuNz_VBWpa9s3ljDn-02u9kZ5qIkQqM6QGFg0Q8c7scr2WejZzobgDNmY-z6PxJ4z1dBzQa-g4oS7vAcbcqiisXQl8l2VxOrTMqJI7Jkk5kYwmwBmcLsdwJ4vXfn1h5pGCyqvZUfpZPuF3r1HYh9E2qt8B2Z7l9HlIzzFkYmHGZzLtzDgi-KzdYvX_oaS3kWRZV3QUJRd2cWDtgyYl3a8xPELpL70sgTJ7d3WRs2udOuh3wE5P33YW6mS8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: باید از حالت نه جنگ و نه صلح خارج شویم   رئیس جمهور:
🔹
دشمن خواب این را ببیند که ملت ایران تسلیم شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/657997" target="_blank">📅 13:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657996">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-Jv4BFXnUI0T_PnwDS1vCyLn8GUWWhtw31DV7CZ2cq1Wl4T1_Fsb-HIPJvVmiG4LcaARSryBWelxe1DCLgOd7JgSu9NVFK7wTzQQh9qDiAr13EJc8HE0ZhKWE1kspnmQPzYgqqNmG6L4CuP6jmXhO_6t3jV-E5CAyFI4cv5-xw12ZvD_liJrEOamJVUc-sFCBXQwNHNnTYRWTpZuYFQT1w05faWavNp_O5oHs32Br8bynKZTaqOIWNWCicHrdRausedn1KrRAhBs3eT1udLcwABFcay-0U6KDp2BPp5y9RqCBDUF64cM_cUFHM0IaafM0WG8zwaK4cIGGUUa-80wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر کشور حاضر تو جام جهانی، چندتا بازیکن داره که متولد همون کشور نیستند؟
🔹
ایران: دنیس درگاهی، سامان قدوس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/657996" target="_blank">📅 13:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657995">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085a6fb159.mp4?token=sUMCPLyt3J29H0hrOsbCf0MEtYv6VftQ2pDpVAGKXpg3KvxfZC_NACtownHSVQNkucCaPeYeW4nzne5RNjXP0CvupTFaTMlvlMsh0Xp6eZultb7iaM7_FhmS_2z91a6s7yUaKF8wa1zKdufsRaSB5QkX0srcLRs2EO_JgrVSlzrOk3xE_C5Jgaw-jX-RiL-x5MDOTKUBNOlcX9wFkVO2SVWNrPeKTx6OTJjVaCvJs_fFGOI3RJ4yfiblWfxcTVcS7PJcqOVXeiV06Scbk1cTpmXkED6AX7FKAfimzkgTuyeAqVFfE0MOinQmg6J9wPZFpBIIvXGv64vomktVqZrwHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085a6fb159.mp4?token=sUMCPLyt3J29H0hrOsbCf0MEtYv6VftQ2pDpVAGKXpg3KvxfZC_NACtownHSVQNkucCaPeYeW4nzne5RNjXP0CvupTFaTMlvlMsh0Xp6eZultb7iaM7_FhmS_2z91a6s7yUaKF8wa1zKdufsRaSB5QkX0srcLRs2EO_JgrVSlzrOk3xE_C5Jgaw-jX-RiL-x5MDOTKUBNOlcX9wFkVO2SVWNrPeKTx6OTJjVaCvJs_fFGOI3RJ4yfiblWfxcTVcS7PJcqOVXeiV06Scbk1cTpmXkED6AX7FKAfimzkgTuyeAqVFfE0MOinQmg6J9wPZFpBIIvXGv64vomktVqZrwHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بمباران نبطیه توسط جنگنده‌های صهیونیستی
🔹
جنگنده‌های صهیونیستی شهرک حومین الفوقا در شهرستان النبطیه در جنوب لبنان را بمباران کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/657995" target="_blank">📅 13:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657994">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX-klUvTpBkJehst6P0cTirVLj6uxjHlCtNjO2vCAYUI9pQcGHI161cd-eveBXsFZZ6Ko6FStOUJEsjuTY36eFDYxVm6QGR9MR_wgDDbol0Hfcz28tUKNICmyRTRkiSnhh5wQarpNos950rFprYeYXYQh70LT5gj_CPBuV13DTTfRaGayDl391uMZ-y20W__ip-ws-AY-tNNsEDFQ4vxw8nSdJS1oUeLLKpSg6IRfYZPvnNj2CTqFCbW-WtMY4S0Ccaf5elnJlQpNeTeo05TYzNKFPhWkIpCMKpOY4_HLsvNixjY57Fo7iR7GJUNm52nuI9xDbcG_-9ZRc5GwAvarg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویش امید در زیست بوم ایران
🔹
هلیا، گونه ارزشمند و در معرض انقراض ایران صاحب پنج توله شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/657994" target="_blank">📅 13:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657993">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNqkxg3o5Yatx1YBx9KIfdtWoAF2pipraRaO1_NU4Cnqv5RBqLjVVvuIe9mBYOM9jnUXkQUsh-H2GSt5kklJcPPvtOi5y9l1S2aGvpCwVfUX9Ej11P6cfGtKq9rPFrBAVVz2YWsfGoYy0J-mU3Q_IaaN2w_Q81RlAvwhb-51GJS-Q0XoGClnkv4FOxnWaeD79iOwKSGkZRTMtETtM9BtzIFI0T0hQ1dizOKyBrvch_m58dGTVJYp0vYeKePHxI4iG8w4nDTTmqfAH2t1d69-zT2791GpFSnmLBBPUrY_y04CzAUmnhlrNbAcXoeuJbTBuGF9Lhv3YYKCL6D6jFfYYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خسارت ۱۵۰ میلیارد تومانی حملات دشمن آمریکایی به تأسیسات آب‌رسانی سیریک  مدیرعامل آب‌وفاضلاب هرمزگان:
🔹
در پی حملات آمریکا، زیرساخت‌های توزیع آب شرب شهر کوهستک و ۱۰ روستای بخش بمانی تخریب شده است.
🔹
این خسارت که بالغ بر ۱۴۰ تا ۱۵۰ میلیارد تومان برآورد شده،…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/657993" target="_blank">📅 13:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657992">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
گزارش حادثه دریایی در نزدیکی سواحل عمان  سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
🔹
گزارشی از یک حادثه در فاصله ۲۰ مایل دریایی شمال‌شرق صحار در عمان دریافت کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/657992" target="_blank">📅 13:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657991">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72050b3b4.mp4?token=NfTIqmpeOTHoivZ4ZwWwS_kuMrxWLih26q7OyoGvzd8KXRKRxe1qf8m6y_gDoeV55FYWlepFxJoAZ8K_37hPhXUAJGT0UbDSJzyrL59EN4biLD0bmOVsIsuyi2V1qVL3fxrIXgd8I3r8GvNcUe0vB8sFGhbs7YxxVLKZEQZXvG3NvX-iI_uEzQDtIMxxzXmdmUUs1DWX5irD_Z4EtO2fc4Z5NYkY3EoBc0VU30leWxQr2CpRBiWwqxLzNweBbvNZpTp_6mmnkCvjT26gvDwLEW9tpSxUxbflBaS1JeFoVsg0jD_XRt5GzkXknjmGQIOBcrv9XVns4WgfdvWzHJW_Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72050b3b4.mp4?token=NfTIqmpeOTHoivZ4ZwWwS_kuMrxWLih26q7OyoGvzd8KXRKRxe1qf8m6y_gDoeV55FYWlepFxJoAZ8K_37hPhXUAJGT0UbDSJzyrL59EN4biLD0bmOVsIsuyi2V1qVL3fxrIXgd8I3r8GvNcUe0vB8sFGhbs7YxxVLKZEQZXvG3NvX-iI_uEzQDtIMxxzXmdmUUs1DWX5irD_Z4EtO2fc4Z5NYkY3EoBc0VU30leWxQr2CpRBiWwqxLzNweBbvNZpTp_6mmnkCvjT26gvDwLEW9tpSxUxbflBaS1JeFoVsg0jD_XRt5GzkXknjmGQIOBcrv9XVns4WgfdvWzHJW_Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زندگی میان شالیزارها و جنگل‌های همیشه سبز مازندران
🇮🇷
#ایران_زیبا
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/657991" target="_blank">📅 13:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657990">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKEbH76u0OnaM27zC-a5uk_t8zoWrTgNgF-Hgz4AOTjarfTl5P7IO82EKlHBZrJTodWPRzBfr3jZzJRt6dFiLSg1nbe49y5j9yIIrVsqGSMKey6wqNVmPnOhmwOBazNwlpMJ5yn7lW0kw2e2_RPn3r7qZJxf3Fj9p6IH23FBQaoOl5SrCQQXwKaDcTdEgArL_uvJZHXIoMx_eL8l-f3LUWu6SI4voyjCNmxpYVZk782VWNOGqHNlgKlubvzoE9KC-_i8OFTXhWK_XnK5xlWN2zrLT0zBPvelvZu6bXE9VjXHfVH3eVZEvOhg9VrV2JTjoETf8Q4BRaSx9G32_Jm4og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش حادثه دریایی در نزدیکی سواحل عمان
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
🔹
گزارشی از یک حادثه در فاصله ۲۰ مایل دریایی شمال‌شرق صحار در عمان دریافت کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/657990" target="_blank">📅 13:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657989">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
آلبانی علیه داماد ترامپ؛ معترضین البانیایی: پروژه لوکس کوشنر را متوقف کنید
🔹
در ادامه اعتراضات مردمی در آلبانی علیه «جارد کوشنر» داماد ترامپ که در حال ساخت استراحتگاه مجلل در خاک این کشور اروپایی است، مردم دست به تظاهرات زدند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/657989" target="_blank">📅 13:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657988">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
منابع از وقوع آتش‌سوزی‌های گسترده در مرکز اربیل و شنیده شدن صدای انفجارهایی در نزدیکی پایگاه آمریکا در اربیل خبر می‌دهند
/ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/657988" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657984">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bba0f34ba3.mp4?token=Q7XWbMpKrvLYWxgtbEJTGM8vLo0vz7j_jW8WXwjZkr8Fmpm0wdI6HP154otsPBjNHTIBQP15L5PpbJ7U-5-EQ-iZ_nQkpoOR5y21CwRUzyl6VCM_loRoucXhZQmLEzNR2Igi_L-tI9xFJpNyPxYOTpV4ST2wPvkGoOzYKMz76i7zdM__-JbPL_YqX6DCqj5OXszrQgpuY50-6gHijdvKSAaMqgDCppwkeRZanJBsz-_i_henZEGT4tuX9SiwXyoSw810j2_RQd1prAqLsoPfVLbqF5c8b06xjGWNZ94JSZjO36WEWi_PQ0sOSRxUsWYY9yqNsijhuYzEQg2kw41LSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bba0f34ba3.mp4?token=Q7XWbMpKrvLYWxgtbEJTGM8vLo0vz7j_jW8WXwjZkr8Fmpm0wdI6HP154otsPBjNHTIBQP15L5PpbJ7U-5-EQ-iZ_nQkpoOR5y21CwRUzyl6VCM_loRoucXhZQmLEzNR2Igi_L-tI9xFJpNyPxYOTpV4ST2wPvkGoOzYKMz76i7zdM__-JbPL_YqX6DCqj5OXszrQgpuY50-6gHijdvKSAaMqgDCppwkeRZanJBsz-_i_henZEGT4tuX9SiwXyoSw810j2_RQd1prAqLsoPfVLbqF5c8b06xjGWNZ94JSZjO36WEWi_PQ0sOSRxUsWYY9yqNsijhuYzEQg2kw41LSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراضات ضدمهاجرتی در بلفاست به خشونت کشیده شد
🔹
پس از انتشار تصاویر حمله یک پناهجوی سودانی با چاقو، اعتراضات ضدمهاجرتی در بلفاست ایرلند شمالی شدت گرفت؛ در جریان تجمع صدها معترض، یک اتوبوس، چند خودرو و یک ساختمان به آتش کشیده شد و ساکنان آن تخلیه شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/657984" target="_blank">📅 13:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657983">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVEbMHiGFLBdez6bSv-tekHLR3H8bVnu2-MVeQTfMStyDRjFYBrbVnWOg-p9Okg52otz1Vw8pivZJHy4iYN0QLvUbiSNTCTgDnvHKyj5y-E0BWjJVk8iLsAILf-R6U2O9jTHLemAW9hX-2JoEvKcWrp7vKSCbac0ka9KpkZ1LLZy8z0ZRbjPOToQEyHW6pnhQqmjjqTX-j40abDhFUsLr1jpI6Vi9RcNh4Zos_kAAl-iogAk1zbleSv7ipuEVAtGdDsFN3wCPfEUQj9Ai-OsZ0BYcU9NLbNMaA_AWy86ms97sjnTzSue-1jMj4FHOVSw59sU2L7dV1An3NtMvGSgmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمسخر ترامپ توسط کاربر آمریکایی: چرا ایران هنوز هلیکوپترهای ما را ساقط می‌کند؟؟ آیا آنها نمی‌دانند که ارتششان نابود شده است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/657983" target="_blank">📅 13:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657979">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6CDO8ivUjkg8HunBEx6dx1SUPBhlZQyihNJmeGGBkKdiNkrnh7Em9EGDzwwSXXntd-nvstLYfPOps_5fwqJWMrzg9coYLge4wgzKWHMFWGMTUEZvELiDTIDj5WR4gMSV9MRAyJ7ra2yQOotdbeB_4uAEd4pu_k7tD5eOvQUYEG0OJOPZrkfwsyuWHp-5XP6OjYDvQcNtndP4e4b9vdaEjtnaaGyc2t_RWVzzXhx4ZpJ8DDwoUP3mG-JnWkXSreORKCCnUuMlQYRXlkEk1Gr85xGSNUnGis0OEa7Wj-RstcUUfS0pw32xbvdhXYa4Hoyz3lLFDJRsYdWIArV_avVYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8xakLz0aqCkHnqyfvi41IFwvk7g5xXGlQWqq5oltiRa5PQ-KetqgSVWxmmlgcueEIO0HEgZ2zhRn236iR4LIsqyPUL8rOY6DF8O8KUmJRTH6qdDMH7vWuIkuZVlGHsFlUlFmXb5fkT17Ot8Pt4gAiLk6wAwKRQI75bosR5R-jc_mKMiqfXFt0cBDfclKw_QMNUPUfoA2mTs3oZFOLVTQNJqVibacaO7Lgwv63JlMwOsafiU-qWh2Mg4Lunqqk5437LRn328jEZEzKdTGBXwEfVgnsBCtuIC-bVCuM9Tm5vFXszI9kZPgalkNj_lM7jrwiNjray4_4EXsLqHPLlFxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OCvAoV8cMrQQmi9MMT6etaWf07a87pF3D_dXff6H93g10eI6rCXq6pYcMLhf6jClmYCGRN3IAd8-dWsFrzxbgMME81173KzrCWNgoZyl06tebcGc4VZl3CCmF1V1_L8hE715okBw0h2FiMO801i1udfxI6PLpMT6QcPnpZKtiF4iD2hS9v1xB7wqjGoNdOmwiBr2cGFzcbIVzMYcGltfXI8Xjm8hqYZ-9SgLDnJWaDf1B8VSp7RKxHXeVQHJmREZoLmyZIFAAr0XlEEvFFwY9glgVPnNgzDZ5oydkpq26fC20-nMYQh-iWd0XdtQCz9fRWD0KFrO1Ce_C4b0e3ITjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIYE1UtIHRYAORdts9vT0axkTpdc0yVjVEZtrfDYpSjH5NwlV2dW2XsfWB3L_uqXgk11Obd04Jd2xaFI3MZVm4TlOMbWt5RQcHYZckfUnZ_ZZ6Fi2-Q3wkSqWDuQaZq96-jeAfrfmfkHOE_J6A-u8BOcdKwF5XhRUDwMOrfvniruphd99_ViCWhNylR8ejhqvW2MF2rawvynZuLXjaTYTEYJcdNB88Qu2-KlitkS2RY_yPmToYc9UPhlStcPRr11eXFpGhUUbmbZ5ND9mqw8AxVy6ICcJ-FJxtS2SBjzlTpD8Sw-EJn0QTY_yNCWNvUreBtQAJxI0d9-arPFgJU-DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نرخ‌ جدید بلیت‌ اتوبوس در مسیرهای مختلف اعلام شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/657979" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657978">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
هر فرش ایرانی، هزاران گره و صدها ساعت تلاش را در دل خود جای داده است؛ اما چیزی که آن را ماندگار می‌کند فقط نقش و رنگ نیست، بلکه داستان‌ها، فرهنگ و هویتی است که نسل به نسل منتقل شده‌اند
.
🔹
شما کدام فرش ایرانی را بیشتر می‌پسندید؛ تبریز، ترکمن یا اصفهان؟
روز ملی فرش ایران گرامی باد
🇮🇷
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/657978" target="_blank">📅 12:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657977">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
روایت پزشکیان از دیدار با مقام معظم رهبری پس از حمله دشمن به جلسه شعام
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/657977" target="_blank">📅 12:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657976">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8fe3c6691.mp4?token=JCLMMUgzAey9rshHCCg8ANFSOa5Po9LZeyWtEvUBQf0Ed7BV8VYYSdr1nMUaz1AHlKgR4ClXUUUSbHncCpvGtPRzGBjxNmoPTa_rtPhl_ZHLDpxx2dt6Neo_VH9j6PCFTzJRGsZvBSs6tXknkNvvfnmy912NCm4aNP8YQ6JCbx_spK_BJJDJAedMSHvifFf1fPQRxMr1-P5_CD0KGgdjwapFsb0r0WZSXjLQDb7l2vWn6Mh8DNsoQqyeodzP6iqQ0Tj5JUe5JIH6yU7nfBNzCERdEe1DrHOmo5XMU-gDwxP6j07oNysKb4zuTffN7kzhXOK2Wj-FXX4PN3jzDLS8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8fe3c6691.mp4?token=JCLMMUgzAey9rshHCCg8ANFSOa5Po9LZeyWtEvUBQf0Ed7BV8VYYSdr1nMUaz1AHlKgR4ClXUUUSbHncCpvGtPRzGBjxNmoPTa_rtPhl_ZHLDpxx2dt6Neo_VH9j6PCFTzJRGsZvBSs6tXknkNvvfnmy912NCm4aNP8YQ6JCbx_spK_BJJDJAedMSHvifFf1fPQRxMr1-P5_CD0KGgdjwapFsb0r0WZSXjLQDb7l2vWn6Mh8DNsoQqyeodzP6iqQ0Tj5JUe5JIH6yU7nfBNzCERdEe1DrHOmo5XMU-gDwxP6j07oNysKb4zuTffN7kzhXOK2Wj-FXX4PN3jzDLS8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت پزشکیان از دیدار با مقام معظم رهبری پس از حمله دشمن به جلسه شعام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/657976" target="_blank">📅 12:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657975">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpF1K8rWchvbLXEyhnrzXuOJHIEgDL0jsfhSN7JyuhjoO3xe2wxDpGmBjdDiq0a86NsRca49eQWRcTXRVDoWLtc_FCkYlArYigO7uoH7vhu5XYwd-U8ZtQ51iONxR3iqaS9JSaSZYWCoWzCq0NtWswnzI786KaTVQHG1FA4OKXUpjLtM6ZgpKlp99l_B0E_nx-36c2fxGPmykKzrylLRGym-P0CE2C7mjXjqZHPxk8krq5pydNv4OPLkcjnuHm8N7KFvOfkMCAOTfTAAgzHibd4V4JfEE-vh1yN5MekyKPLUlNQnOL06Ov69BG_HiUrwFQTZqAlUABUP0uAtoTYlLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ۵۲ هزار واحدی شاخص بورس
🔹
شاخص کل بورس با رشد ۵۲ هزار واحدی در پایان معاملات امروز به ۴ میلیون و ۵۹۳ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/657975" target="_blank">📅 12:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657974">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a9b3aa89.mp4?token=UtgZjQnLbZqWE4BXOLFQ9OmDLz8xYnSinfG7VGeAggQLH9nvxSwLImc81doEXpB5xemV06zoqCaX8_sSj7odXhuCnXkvAB0k_MR3du2KhJjjgwh_s79exr4kQDhcJ_WLqhjLgU3acDcwP4aVkFyGVHDmzPZRh1TIG3UGJHoXwlcNWbjjEcY-ME5N0tSkqVY1y1iMj3cqcWQe-ekq8WnX00bdbQFg89P-hl5N9Lda8uuvcyEKLFX6o93cOkmM6svnC1cnz2dCmL3zqfY2KVifot4TbaSa7CxO4sWgTiHc8vOzJrvmRWuEMI6Vi0oTE85Tz-rFuHPEoMsKT29g63JlVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a9b3aa89.mp4?token=UtgZjQnLbZqWE4BXOLFQ9OmDLz8xYnSinfG7VGeAggQLH9nvxSwLImc81doEXpB5xemV06zoqCaX8_sSj7odXhuCnXkvAB0k_MR3du2KhJjjgwh_s79exr4kQDhcJ_WLqhjLgU3acDcwP4aVkFyGVHDmzPZRh1TIG3UGJHoXwlcNWbjjEcY-ME5N0tSkqVY1y1iMj3cqcWQe-ekq8WnX00bdbQFg89P-hl5N9Lda8uuvcyEKLFX6o93cOkmM6svnC1cnz2dCmL3zqfY2KVifot4TbaSa7CxO4sWgTiHc8vOzJrvmRWuEMI6Vi0oTE85Tz-rFuHPEoMsKT29g63JlVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی از تمرینات آماده‌سازی تیم ملی ساحل عاج برای جام‌ جهانی با قرائت قرآن و دعا
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/657974" target="_blank">📅 12:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657973">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
بقائی: (جهان)اگر می‌خواهد ایران را بفهمند، بروند زبان فارسی را یاد بگیرند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/657973" target="_blank">📅 12:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657972">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
انفجار در قشم تکذیب شد
فرماندار شهرستان قشم:
🔹
انفجاری در قشم رخ نداده است و صدای انفجار شنیده شده مربوط به قشم نیست.
🔹
ساعتی پیش صدای انفجار از سمت دریا در قشم شنیده شده است اما هنوز هیچ منبع رسمی منشاء و مکان انفجار را تائید نکرده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/657972" target="_blank">📅 12:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657970">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
انتصاب اعضای جدید هیئت مدیره مرکز خدمات حوزه‌های علمیه با حکم رهبر انقلاب
🔹
بر این اساس، حجج اسلام والمسلمین حسین رحیمیان، محمد جعفری گیلانی، محی‌الدین مکارم شیرازی، قدمعلی اسحاقیان، محمدمهدی حقانی و محمدحسین احسانی، به همراه نماینده مرکز مدیریت حوزه علمیه قم، نماینده حوزه علمیه خراسان و رئیس جامعة المصطفی العالمیه، به‌عنوان اعضای جدید هیئت مدیره مرکز خدمات حوزه‌های علمیه منصوب شدند.
🔹
جلسه تودیع و معارفه اعضای جدید هیئت مدیره مرکز خدمات حوزه‌های علمیه در روزهای ابتدایی خردادماه جاری با حضور حجت‌الاسلام والمسلمین محمدیان معاون ارتباطات حوزوی دفتر مقام معظم رهبری، دکتر ایروانی معاون نظارت و حسابرسی دفتر مقام معظم رهبری، اعضای سابق و اعضای جدید هیئت مدیره مرکز خدمات حوزه علمیه برگزار شد.
🔹
در این جلسه ضمن تشکر از اعضای سابق و رئیس مرکز، براساس نتیجه رأی‌گیری از اعضای جدید، حجت‌الاسلام والمسلمین حسین رحیمیان مجدداً به عنوان رئیس هیئت مدیره مرکز خدمات حوزه‌های علمیه انتخاب شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/657970" target="_blank">📅 12:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657969">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaY1Zs0BlqxDyaGYAzFQfHoRsZxmjcBPRiDDV08JMaiqycRbVYE6LhjvtDb9RQadwy_ZZWfkNcOhAd3TcTA1nAE6u1k1xfTFslD7HrRIvWgGow5EiSKYTjVLK2UHCQMhcx6Nlsip5MDQaFkQji-7_zYBeNJ7RM5647PIEpscBIWSj9iZ5cG6Dk_H9jJX518NjHpo7rVd1a9ngOFoQ7eEZgkYJeUD5rIoFKj38EJbV3wOkuP4EORC40sBCYM1nRyHcA3h6I1iHETP1dwtmRbobS96x1bUkcI0OlxnpNhKVA4gRA5MG1sZc39Lb9GOhpC_FyjHW3e3cKHhUzEhzjc2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخاطبان عزیز خبرفوری، «مسکن مهربانی» فرصتی است برای روایت تجربه‌های شما از انصاف، همراهی و مهربانی در بازار مسکن
🔹
اگر صاحبخانه‌ای منصف را می‌شناسید، او را به ما معرفی کنید. همچنین اگر خودتان صاحبخانه‌ای هستید که با وجود افزایش قیمت‌ها، رهن و اجاره را به شکل منصفانه تعیین کرده‌اید و تلاش کرده‌اید شرایط مستأجران را درک کنید، از شما دعوت می‌کنیم تجربه خود را با ما به اشتراک بگذارید.
🔸
فایل صوتی ۱۵ ثانیه‌ای ارسال کنید و در آن نام خود، شهر محل سکونت و تجربه‌تان را معرفی کنید.
روایت‌های خود را با الوفوری به اشتراک بگذارید
👇
#مسکن_مهربانی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/657969" target="_blank">📅 11:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657967">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1yaILG44YlgeNPAfxEEx5kMzs6xrBiH14-rfiUkdpjf9xTRy1BuzTMFCruM-2NpP9s64gOEIDxLN1X2vJh2-i2zbvlOXm23jbJ-c0Iz6GzOzslPwWNSa4X-jHpAZA4QVz8CONZ7wOPLGGmYIoofLvDf4KZh5tuWzgfiu19UpCSe6Mk1RP5SYpnms32b2sm1yXo8nV3z1GdWlXAtVQ0Aje52OHbHeg0VHqARwqU--g_S61LIw8dCDvu6HuoJPQkBDkyFd_v9kW2tT5fDBvnprJO-pE_uW1lxcrCNlUxBS_NVPlhAqyL0xlKrMoUeh77mAXu9JvmkGWIHR8cTqBfKgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سخنگوی کمیسیون امنیت ملی مجلس به تناقض رفتار آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/657967" target="_blank">📅 11:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657966">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88af73221b.mp4?token=kD0mSJYgq_boPeqXPsH6M4bS8naIcWh71oTAVZtELjA7UGWtmxoqn-bdHDSFKdyaOLQR6589kJqCHlPaX4DMgCBT00LBOmORO0ZQm8D7nyxYLn1zLipNIke1JEtAeJuKRdzWc2l1G6027z1uZy-RhpdgfDp2ECvaJQTn8nJp7Qcrv4aMt96P-8tRa2CKFugeyx5N77tuYdPqfZmUUojSscY1rZDmQuQiOigqhAkTExOQdwebiVF6wkiexXQpNRuDml7zMRiVIfzVo9H3vyiXvXx-Jo-d1k1IiYjbNnO_B8cToi-FpGDMmrLuvC-mDzheuB7ML9PwQsCN8aRtw8bRbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88af73221b.mp4?token=kD0mSJYgq_boPeqXPsH6M4bS8naIcWh71oTAVZtELjA7UGWtmxoqn-bdHDSFKdyaOLQR6589kJqCHlPaX4DMgCBT00LBOmORO0ZQm8D7nyxYLn1zLipNIke1JEtAeJuKRdzWc2l1G6027z1uZy-RhpdgfDp2ECvaJQTn8nJp7Qcrv4aMt96P-8tRa2CKFugeyx5N77tuYdPqfZmUUojSscY1rZDmQuQiOigqhAkTExOQdwebiVF6wkiexXQpNRuDml7zMRiVIfzVo9H3vyiXvXx-Jo-d1k1IiYjbNnO_B8cToi-FpGDMmrLuvC-mDzheuB7ML9PwQsCN8aRtw8bRbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر لحظه انهدام پهپاد MQ9 ارتش تروریسیت آمریکا با آتش پدافند هوایی نوین سپاه
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/657966" target="_blank">📅 11:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657965">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2166226625.mp4?token=TAGUCewbbGF8GxBuPl0Yyemp19ycRV8b8FY7ujwwr_x3luv6chn8MFo9AQQ6TgT4QpknbeKJw05fi1S68MT3QHckSU_op4D3eIy7TdCPsx2zSf3hBSRI5jx5IAimEl1dixw48cjLSFoN7e27_5HfX8WNubOAcjee8C-QHqOL0nT8AhMVL9blNBZ0PCBooFg1O_z-hDztxgGULDmlp1kUybetvNoO71PfJ5pP_VGtrXk5YUhJGkcFlKWYovC74u25_dPqlgTBFWkkXDqNIA7EMlfXBIXzxsCtu08en7B2nwSWJwPFWQbjCmssREs8iMGdZJiEyCYz60RfWPwxApgibQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2166226625.mp4?token=TAGUCewbbGF8GxBuPl0Yyemp19ycRV8b8FY7ujwwr_x3luv6chn8MFo9AQQ6TgT4QpknbeKJw05fi1S68MT3QHckSU_op4D3eIy7TdCPsx2zSf3hBSRI5jx5IAimEl1dixw48cjLSFoN7e27_5HfX8WNubOAcjee8C-QHqOL0nT8AhMVL9blNBZ0PCBooFg1O_z-hDztxgGULDmlp1kUybetvNoO71PfJ5pP_VGtrXk5YUhJGkcFlKWYovC74u25_dPqlgTBFWkkXDqNIA7EMlfXBIXzxsCtu08en7B2nwSWJwPFWQbjCmssREs8iMGdZJiEyCYz60RfWPwxApgibQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار آهنگ جدید امیر تتلو از داخل زندان
🔹
امیر تتلو که حدود ۳ سال است در زندان به سر می‌برد، آهنگ جدیدی به نام «رفتم که رفتم» را منتشر کرد؛ این اثر از طریق تلفن زندان ضبط شده و در بخش پایانی آن، صدای گریه این خواننده شنیده می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/657965" target="_blank">📅 11:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657964">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d0d226502.mp4?token=efrHWANVsOy9vP11L5UYxQFXw_3OrTpzzWcDcv1W7xG3ERvciSEbxPY6i4gph5hAkTvieptiIFOFubqznPMqzBuNBHQbS4vjTT-Y4uQtdWeIEtQAtLlNnlaPc4aZma3xcLe24YJOpg6h9lsss3-Umfc5R9P-3sj9qH1Fg8Ze7GZhC-58S2nxIumbl_Ij5vR7KQwZ1cnZw0faiAjBRFTaO7CuLx68vqO4al5S3xAxprhFqJPWH5lDMq7vDGlLR87edKHa44SYYw15wSyfOQJ7ApIlkqacdjI_jfmMfPmjXcDaxjseJdBI5eAA8hKTgP7EH2LsfUyoRTMNcD5y2Myd7FzJCiUszKihWObNXL6wE_D2wLbE5VA4D8pQb4AhujvfFXC-k93AZ4BzV5GNU43ZQpYETBGpR3_gIRS3CkJwqvCNBvU28JBlIg2OJJO0OKgHRtW6ep8L8ixZJqoe-6pzHkJRyJ4D0LQgMle1lEQAI3aHRETwX2MC6x8PY4_dE4Bt94ua-I6nsGoTf3JFufK8_8M3JS-J8GSe8jlXab46avVbTAQZWREojEvQUuQClnIBdtMimwvK5Iz_-iuTR2ZQdP6zZ1FR-6SbmGu288fmxsVK7LBa099zohPFycn9ondtpPO3Muur3jVHsV2DwZ7wV3wlCBEnguG_DLvO02sAxEs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d0d226502.mp4?token=efrHWANVsOy9vP11L5UYxQFXw_3OrTpzzWcDcv1W7xG3ERvciSEbxPY6i4gph5hAkTvieptiIFOFubqznPMqzBuNBHQbS4vjTT-Y4uQtdWeIEtQAtLlNnlaPc4aZma3xcLe24YJOpg6h9lsss3-Umfc5R9P-3sj9qH1Fg8Ze7GZhC-58S2nxIumbl_Ij5vR7KQwZ1cnZw0faiAjBRFTaO7CuLx68vqO4al5S3xAxprhFqJPWH5lDMq7vDGlLR87edKHa44SYYw15wSyfOQJ7ApIlkqacdjI_jfmMfPmjXcDaxjseJdBI5eAA8hKTgP7EH2LsfUyoRTMNcD5y2Myd7FzJCiUszKihWObNXL6wE_D2wLbE5VA4D8pQb4AhujvfFXC-k93AZ4BzV5GNU43ZQpYETBGpR3_gIRS3CkJwqvCNBvU28JBlIg2OJJO0OKgHRtW6ep8L8ixZJqoe-6pzHkJRyJ4D0LQgMle1lEQAI3aHRETwX2MC6x8PY4_dE4Bt94ua-I6nsGoTf3JFufK8_8M3JS-J8GSe8jlXab46avVbTAQZWREojEvQUuQClnIBdtMimwvK5Iz_-iuTR2ZQdP6zZ1FR-6SbmGu288fmxsVK7LBa099zohPFycn9ondtpPO3Muur3jVHsV2DwZ7wV3wlCBEnguG_DLvO02sAxEs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر لحظه انهدام پهپاد MQ9 ارتش تروریسیت آمریکا با آتش پدافند هوایی نوین سپاه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/657964" target="_blank">📅 11:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657962">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuL4rs3h6KoX5New9Qsn_4fRM5t-s4Ulw6xUVL6e96KZeXQYE-_w8sqC7kX8ti0dbsU62p8TnUGDKX38ZTFmCj8wOUJS2omAry3OLN8RChAe40NpEdD0DHGKeyoVyBwTuBlJnItaIZeXxZ_6Ax1RCngBV1YswEDimO4_oUPem4cVYeI6MzbIKqfxn1Ri07n4yEumI_4mkFBghLnf9gGp4pnqmmnZWnQCCOjB5ea82cJ0DYwWV6h3sIXlwhVccvzlwWxdEsvLNbgSgwh1HDI3d_Ejjad99pyAwzphcESkNdlIi5zvEaFxJMXyYutagIftXadDgrM9x1ROwfpvYYL4ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-biwmhovjU-IBE1lk1peaiXufiHcLMJnwmIEZdU9z_h7ujj71B3Wr_1GNEWdgis_KveU3Vzge4HmJyTF7_FtqyUQQ4xatq-hv4zrWhbq6SXVuX-kL2EfL-7RMRZA9t0DZwOAULvrK_x2mQpVLmAQEyu0HQMWrEvZOKV1uZdP_cKFTRbGoc5-PDzohQwN7fos1bvN3KB_llkfIvlQTLvr60LsNUVuUhURX7a_rC1Ios4QuXtBtcAyBZ1wgWzyul_kC6kLa4gR2kl0F5uiccYlWYCWIK4uFGkMA2CvVWPLCBFT-13j-ZN8rie7YRVl8-pRLJx1cyC1HVlkCgwejGYXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
استقلال و تراکتور در لیگ نخبگان؛ گل‌گهر در لیگ قهرمانان آسیا ۲
🔹
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌گهر در لیگ قهرمانان آسیا ۲ شرکت می‌کنند.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/657962" target="_blank">📅 11:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657958">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ادعای سازمان هواپیمایی: پروازها طبق روال عادی در حال انجام است
مجید اخوان، سخنگو و سرپرست روابط عمومی سازمان هواپیمایی کشوری:
🔹
در‌ حال‌ حاضر تمهیدات جدیدی اعمال نشده و پرواز‌ها طبق روال و برنامه‌های پروازی در حال انجام است./ خبرفردا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/657958" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657956">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZt-enFw-ss6ENHEgqLhX7rho4twndbCJP1knDKymzx1lbDD3Bx-cwczGxJlynD3blgLzAVLwHRhzBoY6YY_B6_UWR3vtU2ve5QWc_6BsgiaohOAVQ8p4JJJ5IqNIDluXPCgqOsYlj-4vrLEKUqPWTA8yU2IKxjglAKGJEmkCL1u4Ukq4Gm-v-gKqjMZyG8OMkgwaRnpaBKFyc7H5EfijZgbR4w3ZP2Mm1rZX19dS9lSZWhYAssvLegUwZFpJmdsHgC6rpPvc8yl1fUtZZRCj2jTq8KS4CSYAo-GNCAi7xUmvjfWzu-0QfTXS2y1PGO9SCoB27maB5ZOJZdoLyfoDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت به ۹۱.۳۴ دلار کاهش یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/657956" target="_blank">📅 11:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657955">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4w5suylZHHXCZ94tAqhc75BvObaQ34J4Nx5GGPDQyO_WYi4XE23epAvlaWISvviZ4_HePT2PmUZRiLt8lkTJ_W0-YAo2tSO7qAlZOk3CEcecFKTWA1yRNwmgWRlo6eOYlQ9c12pC_MkzD26WU2THxR_pi52oWLK8f93Y85V7MoqjGJjQHayDwxl7zgV3r2K3y-u7aGMu-AA0WA26B9llmRhU8flIY0HhaKALu7s7vvj82QXOrY8CJioaDydZW2jswbjZ72vkD78GY58WMZCOWIjB4XitU2zEU9boQyiQEc5nXY4fnNPjCw6S0NiTKZakdn793e9qeje3tzUXJdACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینجا خط مقدم جنگ است؛ سربازان گمنام جبهه تولید، با دستان پینه‌بسته‌شان از مرزهای اقتصاد کشور دفاع می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/657955" target="_blank">📅 11:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657953">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO7ESkH7eDrs7kqFBbsCk2mg1qCiVfR9I8DzIvlinRUP3ACpLIsw4GPZYVJcAqPfbzTsO06gS4YvV3v-F_u6GT4Hx9UyEWsUgFcegdYg4ryQE_bRgYFjsqwjqs_6vQHb1x6b9CzLk3KnBrG_Kepidmd4IN6Jyw2H-m3esZl0Iwhctlp6KoVz9PR1ISMIzMCD5f3Vvp8FHIJZqYl9ehL-rxY57xMOamZkSHIchtpb61nj0XPhs0cqhQDhbakVnATsr8ce7UfTW-k8qnFsTatISA3BXu2IyaVFj8XkUXqWOoyzlZjedM5pftcczuLJ3PKpjVT4Pw0o3gRnIfmRgVnr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فدراسیون والیبال برای دیدار تیم ملی والیبال ایران مقابل برزیل در جام ملتهای والیبال
🔹
این دیدار بامداد فردا پنجشنبه ۲۱ خرداد از ساعت ۰۲:۳۰ به وقت ایران برگزار می شود.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/657953" target="_blank">📅 11:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657952">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92e56a49cc.mp4?token=Uek04GXBFVXDYua2JdZBYEIlDD8G0UtCbujLWIcWxQes-lXE7yuAYlwg5IQp3brhHFsZR1vKDI7jZ-g_IavI1is4KkfSEWNHVEUmjZUEaQ6yqdN4RHLt103HLrB62MsMNGpicftNDdLAn5IEu8FlafLVtqoUCUpNbf9ucFR4zcTdQA5UTA4_vJsvzPCxvKyYqifc6kwtIb6emOLwG01JVXRky8j84mTZ-UNBdNEk-k-c1LWD3MpySQf7rm-kRIzO_9qHjGdUiLoyraeD6z5Nrsx2P10qHHsgEbtGCzjEKqVvoxTK9ZGEkcdsSg2-_bqCGEBns5nedHIaj5JhiE4fKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92e56a49cc.mp4?token=Uek04GXBFVXDYua2JdZBYEIlDD8G0UtCbujLWIcWxQes-lXE7yuAYlwg5IQp3brhHFsZR1vKDI7jZ-g_IavI1is4KkfSEWNHVEUmjZUEaQ6yqdN4RHLt103HLrB62MsMNGpicftNDdLAn5IEu8FlafLVtqoUCUpNbf9ucFR4zcTdQA5UTA4_vJsvzPCxvKyYqifc6kwtIb6emOLwG01JVXRky8j84mTZ-UNBdNEk-k-c1LWD3MpySQf7rm-kRIzO_9qHjGdUiLoyraeD6z5Nrsx2P10qHHsgEbtGCzjEKqVvoxTK9ZGEkcdsSg2-_bqCGEBns5nedHIaj5JhiE4fKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا همه دارن مو سفید می‌کنن
⁉️
😨
توی خیابون که راه میری، انگار پیری زودرس به همه سرایت کرده؛ همه درگیر موی سفید شدن، اونم فقط به خاطر افزایش سن و ژنتیک
😢
اما حقیقت اینه:، فقط رنگدانه‌ها غیرفعال شدن! من خودم هم همین مسیر رو رفتم، موهام داشت سفید می‌شد، اما با این روش علمی و ساده، الان دوباره موهام مثل روز اول «مشکی» شده.
♦️
بدون نیاز به رنگ موهای شیمیایی
♦️
کم‌هزینه و ساده تازه، برای اینکه خیالت راحت باشه،رایگان بهت مشاوره میدن حسرت جوونی رو نخور دیگه، روی لینک زیر کلیک کن
👇
👇
bam30.com/ads/landings/22703-2e958
bam30.com/ads/landings/22703-2e958
bam30.com/ads/landings/22703-2e958</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/657952" target="_blank">📅 10:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657950">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9ER6LB-3uexiIrpicGAr6RuDh0dJRCIU0RIRGJgVQxnhm9dL8Ig5saEcnWPeZhmYIpxNI1411AkprjD46raSIAlU1sjtiQ-JpoGXql78gARwynrAj1x4OeeUoyUipKq_T6dxuBKINbSxQmielUZtATWGPBJxcChsExDS5457bTEwbrvNJu96kQkqXmRQ45pVnX7OjRvnL_mNzYoAJaaUmFu6TQpCNIMUWS7RxKNZtJdwWKxjd7XWjJcNA7Ns_gWT0-2WCfiLG-crPeXQbJa6JkWV0tbXLBuUkSITqJK9puRM-enmINspgnlAtdSvSUHpBU3CIvqmflkZFAqki444w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیفا سهمیه بلیت هواداران ایران برای سه بازی تیم ملی در جام جهانی که در آمریکا برگزار می‌شود را لغو کرده است
🔹
طبق قوانین جام جهانی، هر فدراسیون معمولاً بخشی از بلیت‌های بازی‌های تیمش (حدود ۸٪ ظرفیت ورزشگاه) را دریافت و بین هوادارانش توزیع می‌کند.
🔹
فدراسیون فوتبال ایران می‌گوید این سهمیه از آن‌ها گرفته شده و دیگر نمی‌تواند بلیت رسمی در اختیار هواداران ایرانی قرار دهد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/657950" target="_blank">📅 10:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657949">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYHVWD28lrI_go1vFw_Yw1G6mtKoNaQT9VW2pMGbol2U0WjoYRtqTOiNVhfWRVXu-PYuETnnJoSnyBeYr-uR2EB4wo4uprxg7RKqeTMi3lFCpQr-OCLNiDyDbPtNbePvTBb0f9fTnevj2eZ3DhIBlVI2q5P4ucYbLaCKhW7JRW81qInI7L11CCgQbTY8VObbnirMeLs2X15i3BKDJQCNs8qd9bTUdEDV2Uexx-VtZoBXxolGFJyh6O7pUhSwoJ1vQXid4B9gPoc6ZS8F9SsbcGq4sQfnSRrdCG-VNMH7kukvtXVSYgipX6QtUwHyL9WYazCu1CUmphXMUml7wARTxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه هیچ صفحه‌ای در توئیتر ندارد
🔹
سپاه پاسداران اعلام کرد هیچ صفحه رسمی در توئیتر (ایکس) ندارد و تمامی اکانت‌های منتسب به این نهاد جعلی هستند.
🔹
پیام منتشرشده در یکی از این صفحات نیز با هدف ایجاد تفرقه عنوان شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/657949" target="_blank">📅 10:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657948">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXV903533MFWbvxPc4VI5l92t69gRK1TThzRMWEICqnpvqiv_LLVAddKozX4AMwjhykpn3wAQO6-uTW3ap_hCoflWyXxFsY0hy5NELBSsp8YJdMG8kYS-A-1x64F75UZ3wopF2r9jxjf4aMsTk-r9yyNKgLRLfUBoViLpS-aty4Ep3Dwt2Q6cOJ_kquo6Vr5tDtXnYG8YYllDGgPCiRvUnPY7UE9HdOTPDon_VuqrOx_gR6PAIxcEGjWkpa_LhqRLN0Yc6Gek60EEsfoAVzC0GU1IIquZDM2cHJp1BCaBFUblTOmB1uzARTXt8WyIIuQ5szl9wzxqQVWE_qCF12stw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت یک متر مسکن در تهران چند؟
/ خبرفردا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/657948" target="_blank">📅 10:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657947">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
امتحانات مقطع کارشناسی دانشگاه‌ها مجازی شد
معاون آموزشی وزارت علوم:
🔹
امتحانات مقطع کارشناسی به‌دلیل فراهم نبودن شرایط حضور دانشجویان به‌صورت مجازی برگزار می‌شود.
🔹
این در حالی است که آزمون‌های تحصیلات تکمیلی طبق روال حضوری خواهد بود.
🔹
همچنین در صورت تأخیر در اعلام نتایج آزمون‌ها تا آذرماه، شروع تحصیل این دانشجویان به بهمن‌ماه موکول می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/657947" target="_blank">📅 10:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657946">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9JBi9i72n3LYWRzYYiWnU6naIHJwXSfzp4A-SuKmm5icpPIAeyZ30CD11jQPAuWyObfXJssGFTs2E8XptrBExaSv8dCoZUV3ei3HVocydg4EeeuguJCdF__VFFLduoqff746FXp2ksZRHgooxuQA51seNhIELnXSBH_kw-7Q3WGBieX8QqaclK6vC0bV_imRoem5M0bKZLUrFqbSCcnwwjplxZKI3P-9B8A7QOw8SCQlscho2iOjQ44xXkiqXZ0hZdku1SRJbQI6wLjSF3NS6g-ykYUDn37ts4UhIZKp0X3khUczxc9RFlZRr_hcnZFW-7K3CpayiTjzRPcqXx3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر توییتر: ترامپ ساعت ۶ عصر: ایران نه نیروی هوایی دارد، نه نیروی دریایی.چیزی باقی نمانده!
🔹
ترامپ ساعت ۷ عصر: دیشب ایران یکی از هلیکوپترهای آپاچی ما را بر فراز تنگه هرمز سرنگون کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/657946" target="_blank">📅 10:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657944">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a482f7f99d.mp4?token=Mu7nfekMmyj4SL_GZbBM-iCJuw0CUbhYzXbLfb5Gr549c2FnlkgyGBFco5dKLwmUdt8TPeSmTvd8kLOY4_1aGiLDT5y7fUOPlVACqnCx8m42nwG3WrLy-ODS_1GUQX49snPrHO3eWyWPK8dVTp4jprSTGRDJpNKsVgdC6d7u-SBR1jDm2NFJZmBOg_iYGEabHV5FUdGjxV4o-x7nzkZjwY_WmYIvJV7PXtvYvQC3HCmeqV6YdNKkF4Js3wCKB7zhkCKGf7QpnLopb-8CZizWDiIeL_nEKrJdKbcXfLSJZDWgV5euOShnZcMRsb6c6BSRUv5CsQ1fJfuQRdq8hs6OdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a482f7f99d.mp4?token=Mu7nfekMmyj4SL_GZbBM-iCJuw0CUbhYzXbLfb5Gr549c2FnlkgyGBFco5dKLwmUdt8TPeSmTvd8kLOY4_1aGiLDT5y7fUOPlVACqnCx8m42nwG3WrLy-ODS_1GUQX49snPrHO3eWyWPK8dVTp4jprSTGRDJpNKsVgdC6d7u-SBR1jDm2NFJZmBOg_iYGEabHV5FUdGjxV4o-x7nzkZjwY_WmYIvJV7PXtvYvQC3HCmeqV6YdNKkF4Js3wCKB7zhkCKGf7QpnLopb-8CZizWDiIeL_nEKrJdKbcXfLSJZDWgV5euOShnZcMRsb6c6BSRUv5CsQ1fJfuQRdq8hs6OdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات حمله آمریکا به زیرساخت‌های آبی سیریک  حمزه پور مدیرعامل شرکت آبفا هرمزگان:
🔹
نیروهای آمریکایی به زیرساخت‌های حیاتی توزیع آب در شهرستان سیریک حمله کردند.
🔹
در پی این حمله موشکی که ساعاتی پیش به وقوع پیوست، دو مخزن استراتژیک آب در بخش بمانی هدف قرار گرفته…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/657944" target="_blank">📅 10:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657943">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5ITvqYn_KGiQ6klro30fq9-phvMV1GgK9vOyPkJTEZ8iBkEvxaNAsMKNFrSg0u69ltA5wemdYYwU3U8OgQ5fJY7pbI1nT47C7DxpBZ7Ja4jEYc_TTzlgOHxjXuxkkiljZBF3qczWeoPeUwQwO5EFPOZLG_OGG9MrL2fVE2a-hxRr5laYVYRGa9SQOkOppHUGeY1WbyBj6cPqMVRJpSd3BCydvEcvHn4KEp7ILZk-h_utn9jgHX2YvRkxvqiibAsOQgW5rg5vl4WDfNJfhoY-Oukt1R8QZPQaRidwUxZPsdglGCyXUqQIAQ2cuh7L4Jt2xSOOb0BCbAAu33C_Fqxvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخستین عرضه اولیه ۱۴۰۵ بورس تهران، مربوط به گروه توسعه مالی فیروزه با نماد «
وفیروزه
»
فقط تا ساعت ۱۲:۳۰ چهارشنبه ۲۰ خرداد
ادامه خواهد داشت. با توجه به شرایط بازار انتظار می‌رود این عرضه اولیه با استقبال گسترده‌ای مواجه شود. شرکت در عرضه اولیه «
وفیروزه
» در
تمام کارگزاری‌ها با ثبت سفارش خرید از طریق سامانه معاملات برخط امکان‌پذیر
است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/657943" target="_blank">📅 10:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657941">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a9eb7155a.mp4?token=KdMXzyO4agTTXywl5o7mSMPf5tkiADM61FvfqDgtWnkJm8jTIZI1gO4r1EPyIvqKlK8GDZ8z1SBYWK2WdCDUl8dj9GG2aW6jUoCP_ZQJFULJwnP6qcNwPfTEBPCPYt5D_-q-ZhRjPwXawWS1sorviWPjzHmdIlVuBSs1HgFZ1f6TYytdKTqJ4LhqbEwDcFsl0VCdNm6XyN0FFM1oLqh4_-zLdCFcJQBFcvyp2XXwQkHBjrsQzjDeGI5ojsnejpDFSyX8MCGEcXwssvcwgLG6JfuDbJiA2_wtAt2Te0ZwvPcISSle7Pdo8iST4cUQWeE3ILyA0So1ypUymBXEVsBH9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a9eb7155a.mp4?token=KdMXzyO4agTTXywl5o7mSMPf5tkiADM61FvfqDgtWnkJm8jTIZI1gO4r1EPyIvqKlK8GDZ8z1SBYWK2WdCDUl8dj9GG2aW6jUoCP_ZQJFULJwnP6qcNwPfTEBPCPYt5D_-q-ZhRjPwXawWS1sorviWPjzHmdIlVuBSs1HgFZ1f6TYytdKTqJ4LhqbEwDcFsl0VCdNm6XyN0FFM1oLqh4_-zLdCFcJQBFcvyp2XXwQkHBjrsQzjDeGI5ojsnejpDFSyX8MCGEcXwssvcwgLG6JfuDbJiA2_wtAt2Te0ZwvPcISSle7Pdo8iST4cUQWeE3ILyA0So1ypUymBXEVsBH9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرگ از بیخ گوش فیلمبردار گذشت
🔹
در جریان بازی دوستانه مجارستان و قزاقستان، دوربین فیلمبرداری از ارتفاع سقوط کرد و تنها چند سانتی‌متر با برخورد به فیلمبردار فاصله داشت!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/657941" target="_blank">📅 10:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657940">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0cb9d3c2.mp4?token=C3W3mf02ZXHCIEz8Ffoi2z6RWFJe6naUF5B-G5EW8WCzwT_7eDl3jRvYiKuXrZzYpaDAajzJvm7rsUrFYN1odgCsTICWF9TVcVdXB4IeZE7Npm1R3Wu6tYVXU3gY5qrZchfN1nz0w_aM60AQ_AzZicf8P7yYdMeqHA5cD_TQFwFP-_ybDzDJyj5BPHGTIKHX0aTJ3YMpP3931Gha7WQWdWI9sdL_GI7eomvv9TazaTUETf_-KVvoSP5crpPjAqIcCLQt2LfJzTn_2TJsnRA2rTzozZbU3ZkD_VWfDxxLxegazMmJbKnqpFbt9mIVndtqeYYL7eGchp12SzepLhJbyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0cb9d3c2.mp4?token=C3W3mf02ZXHCIEz8Ffoi2z6RWFJe6naUF5B-G5EW8WCzwT_7eDl3jRvYiKuXrZzYpaDAajzJvm7rsUrFYN1odgCsTICWF9TVcVdXB4IeZE7Npm1R3Wu6tYVXU3gY5qrZchfN1nz0w_aM60AQ_AzZicf8P7yYdMeqHA5cD_TQFwFP-_ybDzDJyj5BPHGTIKHX0aTJ3YMpP3931Gha7WQWdWI9sdL_GI7eomvv9TazaTUETf_-KVvoSP5crpPjAqIcCLQt2LfJzTn_2TJsnRA2rTzozZbU3ZkD_VWfDxxLxegazMmJbKnqpFbt9mIVndtqeYYL7eGchp12SzepLhJbyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شده پرچمتو تکون بدی بخوره تو سر یکی؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/657940" target="_blank">📅 10:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657939">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ریزش قیمت طلا شدت گرفت
🔹
قیمت طلا در معاملات روز چهار­‌شنبه بازار جهانی تحت تاثیر تقویت ارزش دلار و افزایش قیمت نفت، کاهش یافت و به پایین‌ترین حد خود در ۱۱ هفته گذشته رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/657939" target="_blank">📅 10:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657938">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07c7ed1810.mp4?token=YPHGKO-eoYH19gUCEJfzDnMqbhMzVRNq1w_wZqEpx_cg_zvg0bbi3sGtPy8_mf2p0yjiA5XDMsVCaaBtH8o6Mythvce5moYVpvyx2gXEcoSCPE_9OTTlps-QgayNUqNlZNQ_F2DYU4Iw2fUfH-_JIeMsjcO5T7eL80zpiyUvyQ-dzZVPbmURMJwEjETK3RuSlRGktDcDoqb5RmEq3uT93eKTKjagDcc0bwu-Gbc0weHo68wET9mYdKXXcrhwkvlC4fL7xsNHO13pmHeSnJeIrIOSxBcl3-qVnIbG6sVWxYYRO_w3zNCix-V8_yQilwVbIQPnwV4nNLtbX-f_D0-1zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07c7ed1810.mp4?token=YPHGKO-eoYH19gUCEJfzDnMqbhMzVRNq1w_wZqEpx_cg_zvg0bbi3sGtPy8_mf2p0yjiA5XDMsVCaaBtH8o6Mythvce5moYVpvyx2gXEcoSCPE_9OTTlps-QgayNUqNlZNQ_F2DYU4Iw2fUfH-_JIeMsjcO5T7eL80zpiyUvyQ-dzZVPbmURMJwEjETK3RuSlRGktDcDoqb5RmEq3uT93eKTKjagDcc0bwu-Gbc0weHo68wET9mYdKXXcrhwkvlC4fL7xsNHO13pmHeSnJeIrIOSxBcl3-qVnIbG6sVWxYYRO_w3zNCix-V8_yQilwVbIQPnwV4nNLtbX-f_D0-1zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رؤیای دیرینه صهیونیست‌ها برای نابودی ایران
/
بمباران، تجزیه، جنگ داخلی!
🔹
اعتراف تحلیلگران اسرائیلی به اهداف شوم و دیرینه رژیم صهیونیستی برای نابودی ایران!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/657938" target="_blank">📅 10:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657936">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f03dc55a4.mp4?token=UW-ZSJBZzaGALb_XpKoxJQzpQYYajDWdA5gXKsBEJViODcaZYGYmiU2D6tVsYrKC2f2fpPj2Njlle5N3vYnfMrCKB6BM8s1cZnSSydm4cmQ0fY_4smXN9d8U0yAUOnmZcBBKfrz2KMcFUIBW149O10J83X9EF5Du1SSnwSiIoAlseLTqpL_3Wfrpn8uSity25G1JOhiGcCv3WdaVDGQs2DPNOMkor_6vMmdVmQ5hToM1lLblp-mLL5335kofWDmgQejErf6GpOuVT-xdmAEj2V4CLSfcvi9NFkmCwNIZ3sAJooenbbPR0ro1FwgQ0Z0Wk7Aa5NNXw-pr4NROgJinQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f03dc55a4.mp4?token=UW-ZSJBZzaGALb_XpKoxJQzpQYYajDWdA5gXKsBEJViODcaZYGYmiU2D6tVsYrKC2f2fpPj2Njlle5N3vYnfMrCKB6BM8s1cZnSSydm4cmQ0fY_4smXN9d8U0yAUOnmZcBBKfrz2KMcFUIBW149O10J83X9EF5Du1SSnwSiIoAlseLTqpL_3Wfrpn8uSity25G1JOhiGcCv3WdaVDGQs2DPNOMkor_6vMmdVmQ5hToM1lLblp-mLL5335kofWDmgQejErf6GpOuVT-xdmAEj2V4CLSfcvi9NFkmCwNIZ3sAJooenbbPR0ro1FwgQ0Z0Wk7Aa5NNXw-pr4NROgJinQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور کمالگرایی می‌تونه مارو از مسیرمون دور کنه؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/657936" target="_blank">📅 10:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657934">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fck4YC2EKYickN6adhU4nS7w6BWX7JX8-4pyyMpTkU34Ggz5lWgEbkpUPFuVwBwQ4ST_xdxqtVIrL9xq1WiN0O-8K0bi10ArDEaVxvhWq52tRnlYFn00K4PumlH8n2U2WUdTqTNa__iKDalWqGU3cHGjEWSlJS2ItbuNtpjRMTPS-Ca91FjpooR3uMd-cTZ66GjyqvlZliEWMA_0COq22PONw7LflxIH8AKV7YJ4ditlp0n9vN06ux8HGlx-fsUreh8WFGyDcEBbC3bQeiDYWB6HbUGtdEWd1DrWQKNPObHQ3SPvxb8TYHl5HCJ12V9MgOAr1QNaGJiaTqoDmPEvjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرصت خرید کیا اسپورتیج از طریق کوشا خودرو
در ادامه عرضه مستقیم محصولات کیا که از ۱۸ خردادماه آغاز شده، متقاضیان می‌توانند برای خرید کیا اسپورتیج از طریق وب‌سایت رسمی کوشا خودرو اقدام کنند.
فرآیند ثبت‌نام و خرید به صورت کاملاً آنلاین و از طریق بخش «فروش اینترنتی» انجام می‌شود.
🌐
وب‌سایت ثبت‌نام:
www.kooshakhodro.com
کوشا خودرو
فروش و خدمات پس از فروش کیا در ایران</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/657934" target="_blank">📅 10:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657933">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3863f2a74c.mp4?token=XCml89kdhzXggqgKxRigmcP6BMLXfhjUP6czBXshz_AfvFOfitcVFYtShXE1tOaEir2aAp8pwBIybvPEL3Nw-HslOa1HdDWqDd0dD9bkLgK-xvHgoajIVDIV1Vi5WU2cfPPEhiuVoWpd7liPWgjeYf-hojMBpEqCt2gW-GbJZPof-ikBabPhYIgc5BGaxCLkrlyOKwuoV45kXupBA016RZDv71744qStr1Y4ta9ZAmWHGn6qHhbR7cRqwaKwIhMu5YwbSMAXur-QrRYivD86d4xWyd2_TNMSYIN2SBVcBKz33NBZpa3VNsVoK_k8ZM-P2SNzgtXIC0EoXrVSDvlAkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3863f2a74c.mp4?token=XCml89kdhzXggqgKxRigmcP6BMLXfhjUP6czBXshz_AfvFOfitcVFYtShXE1tOaEir2aAp8pwBIybvPEL3Nw-HslOa1HdDWqDd0dD9bkLgK-xvHgoajIVDIV1Vi5WU2cfPPEhiuVoWpd7liPWgjeYf-hojMBpEqCt2gW-GbJZPof-ikBabPhYIgc5BGaxCLkrlyOKwuoV45kXupBA016RZDv71744qStr1Y4ta9ZAmWHGn6qHhbR7cRqwaKwIhMu5YwbSMAXur-QrRYivD86d4xWyd2_TNMSYIN2SBVcBKz33NBZpa3VNsVoK_k8ZM-P2SNzgtXIC0EoXrVSDvlAkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهادت یک کودک شیرخوار به دست نظامیان صهیونیست
🔹
تصاویری از لحظه هدف قرار گرفتن یک کودک شیر خوار ۷ ماهه به نام «سام ابو هیکل» با گلوله یک نظامی صهیونیست در الخلیل منتشر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/657933" target="_blank">📅 09:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657932">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
تماس‌های خانگی رایگان شد
🔹
شرکت مخابرات همزمان با افزایش ۴۵ درصدی آبونمان تلفن ثابت، اعلام کرد مکالمات درون‌شهری و بین‌شهری برای مشترکان خانگی از ابتدای خرداد رایگان محاسبه می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/657932" target="_blank">📅 09:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657931">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4JIXklxSRNqbVOJxUKLUsKWL7d8j1BEWh5Q_n-Igr0ai1uTuiNSC2t6pJKy_SrmwzT_ZEGypijne4MWuFckBg4uQhk3A4feirfdSIPEK6xMc14jAsTDUahpB6EZn5RaRWPWYPo5xwcUz94wJQTAs027KWTsLC9_uJVKqfUUIKGEfUSm2z6fPEdlFkI_y2FNLqZ7qjYjB3aAPGBuJ9NqTUpkN8Wi1UOo_alZRZ_dkKgT3CRORU9acSwMz67ABE1iBVI4VCLOL4EuThCIRAceyE66iEyYnH1d8XLcdnMx-riCI2lEUzYISjMufsaNtnqt5VTVX9mLc0OnuiEA5n9u0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حادثه دریایی در آب‌های یمن
🔹
سازمان عملیات دریایی انگلیس گزارش کرد که یک حادثه در ۸۸ مایلی جنوب غربی بلحاف یمن اتفاق افتاده است.
🔹
در این حادثه، یک قایق با ۶ فرد مسلح به یک کشتی باری نزدیک شده و تبادل آتش بین قایق کوچک و کشتی‌های باری رخ داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/657931" target="_blank">📅 09:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657930">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
بازی شطرنج میان ایران، آمریکا و رژیم صهیونیستی؛ ایران بنا به چه راهبردی به تجاوزات اسرائیل به لبنان واکنش نشان داد؟
🔹
پاسخ ایران به تجاوزات رژیم صهیونیستی به لبنان برای برخی ابهاماتی را به همراه داشته اگرچه مشخص است که این پاسخ در همان پازلی تعریف می‌شود که بسیاری سقوط سوریه را مقدمه‌ جنگ علیه ایران ارزیابی می‌کردند.
🔹
امروز به وضوح مشخص است که تضعیف حزب‌الله می‌تواند موازنه‌ قدرت در منطقه را بر هم بزند و هزینه‌های امنیتی ایران را در تقابل‌های آینده به شدت افزایش دهد؛ به‌خصوص که جنگ حزب‌الله با اسرائیل بخشی از ظرفیت نظامی این رژیم را در جبهه لبنان درگیر کرد و مانع تمرکز کامل آن در جنگ ۴۰ روزه علیه ایران هم شد.
🔹
براوردها از رفتار اسرائیل در جنوب لبنان حاکی از این است که اهداف این رژیم فراتر از تضعیف حزب‌الله است و تخریب گسترده روستاها و زیرساخت‌های مرزی مقدمه‌ای برای اشغال بخشی از خاک لبنان حداقل تا رودخانه لیتانی ارزیابی می‌شود و تضعیف جدی بازوی زمینی ایران در کنار رژیم صهیونسیتی است.
🔹
از این منظر، تضعیف هر یک از بازیگران محور مقاومت تهدید موجودیتی علیه امنیت ملی دیگری را تقویت می‌کند. بنابراین پاسخ ایران صرفاً واکنشی دفاعی نبود، بلکه پیامی در جهت تغییر قواعد درگیری و تقویت بازدارندگی فعال در برابر تهدیدات اسرائیل و آمریکا، در راستای حفظ منافع امنیتی و ملی ایران و لبنان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/657930" target="_blank">📅 09:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657929">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/035a4f599f.mp4?token=iVRv5JCdEzicPR7eYLBnbi7HRKJikR7r4PeiPp9wB_RUnC_MkoLZXs52Cm2nutSqUHQwmK4KKt4AqDzyPEOoS1lQ5fJ6Pw1zl_pIF2ED9jkDs26GGx-vENLQ2oxNG4JR9mM4fD8uqEC258_cpQdzN315Y1jE04PTlzEufAF_fgSE55IrEXlxQXD-sqnKTpwhO79PBPFxcoM6ddO_60z5LdbvJAmBsLJ73SY-CT_AL4_B3iPtaDAzHhOnT3yddJIDoZqAdF9C_5lfHtJut6mbPU9HBo1ouVZ53WSt53OxX8jPT5HeSQrqJ0hVNmdmgmjoD9Bz9K2oI_d-MPoqYrF6uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/035a4f599f.mp4?token=iVRv5JCdEzicPR7eYLBnbi7HRKJikR7r4PeiPp9wB_RUnC_MkoLZXs52Cm2nutSqUHQwmK4KKt4AqDzyPEOoS1lQ5fJ6Pw1zl_pIF2ED9jkDs26GGx-vENLQ2oxNG4JR9mM4fD8uqEC258_cpQdzN315Y1jE04PTlzEufAF_fgSE55IrEXlxQXD-sqnKTpwhO79PBPFxcoM6ddO_60z5LdbvJAmBsLJ73SY-CT_AL4_B3iPtaDAzHhOnT3yddJIDoZqAdF9C_5lfHtJut6mbPU9HBo1ouVZ53WSt53OxX8jPT5HeSQrqJ0hVNmdmgmjoD9Bz9K2oI_d-MPoqYrF6uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سایت Global: کمپ ایران بهترین کمپ جام جهانی از لحاظ امنیتی است
🔹
پس از حوادث امنیتی در نزدیکی کمپ‌های انگلیس و سوئیس، رسانه‌ها از استقرار ۳۰۰ نیروی ارتش و گارد ملی در اطراف کمپ ایران خبر دادند؛ آماری که در میان تیم‌های حاضر بی‌سابقه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/657929" target="_blank">📅 09:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657928">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ادعای نیویورک تایمز: ایران به جای تحویل ذخایر اورانیوم، آنها را رقیق خواهد کرد
🔹
نیویورک‌تایمز مدعی شد توافق احتمالی هسته‌ای شامل توقف ۱۵ ساله غنی‌سازی، رقیق‌سازی ذخایر اورانیوم ایران، برچیدن برخی تأسیسات هسته‌ای و بازرسی‌های سرزده خواهد بود.
🔹
به ادعای این روزنامه، ایران به‌جای انتقال اورانیوم به خارج، ذخایر خود را با همکاری آژانس بین‌المللی انرژی اتمی رقیق می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/657928" target="_blank">📅 09:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657927">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044ad13ff6.mp4?token=m3bwwvUOwVW6DbzSxTfoh-cctm0pW9sVdaADp2zqe6M4t_j7Fu-piUk3TN9zc2Zk2sVvtYdjVuYN2_LOSrUIjxtBPSq7VFkbCfF8oOis7ewomdC7-7dhmj0vlQB3eTP9Nu1xTr0SDv06f1PMiecv_wsOkd7hcNOOR1ltHjqmFbI5Z9PYKRWJE4I08wl6ZzOifxk8a3u8CyjtwPlgY7Keig34xi5MJIHTjZY-gFU9rG8T3Q8SNUCCylt8K_roxXixti4hM_nQVjYy-RfX6kvXzipFXbLElOZyYc22lb2RiZptxiyUB68-qh-NLocERxmLltBUjEKlwE_8OCkxqpYMQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044ad13ff6.mp4?token=m3bwwvUOwVW6DbzSxTfoh-cctm0pW9sVdaADp2zqe6M4t_j7Fu-piUk3TN9zc2Zk2sVvtYdjVuYN2_LOSrUIjxtBPSq7VFkbCfF8oOis7ewomdC7-7dhmj0vlQB3eTP9Nu1xTr0SDv06f1PMiecv_wsOkd7hcNOOR1ltHjqmFbI5Z9PYKRWJE4I08wl6ZzOifxk8a3u8CyjtwPlgY7Keig34xi5MJIHTjZY-gFU9rG8T3Q8SNUCCylt8K_roxXixti4hM_nQVjYy-RfX6kvXzipFXbLElOZyYc22lb2RiZptxiyUB68-qh-NLocERxmLltBUjEKlwE_8OCkxqpYMQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی عجیبی از یک انفجار اتمی در بندرعباس که ساعتی قبل در پخش زنده شبکه خبر منتشر شد!
🔹
در حالی که خبر درباره سازمان توسعه تجارت ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/657927" target="_blank">📅 09:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657926">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d0cc9941.mp4?token=GmbYz5RiypZOvYRuzuBli44eWKrKcNTFZch7fmYf12NYMY8n6iMUJOwjvqwL9AszoDv1krTxmG_g7ObamlpIrwpKKH6fIymiCOFNJrDBpNnNMg7zy9VZG86G34WbWwgC0uJRgLS1cEt-AJCKCI-4OSDUAyh9CXqp7aXWBC0upN_5c04jqWGeqQBHbNJcW8JkCEtvRbV60jGmP0XxjTFFKV8DdQen1KgNSm6Up6FVqliLuRFGic4Yn0ZixppsvwRw4pmsIVhNc1-QB7O4tV5G2hpMzy4ra5Q1ntJ-FVacYtikyWaVOHRwoBXQD3Cj6zk5kBDs9KPis_0jU4fEcMmRLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d0cc9941.mp4?token=GmbYz5RiypZOvYRuzuBli44eWKrKcNTFZch7fmYf12NYMY8n6iMUJOwjvqwL9AszoDv1krTxmG_g7ObamlpIrwpKKH6fIymiCOFNJrDBpNnNMg7zy9VZG86G34WbWwgC0uJRgLS1cEt-AJCKCI-4OSDUAyh9CXqp7aXWBC0upN_5c04jqWGeqQBHbNJcW8JkCEtvRbV60jGmP0XxjTFFKV8DdQen1KgNSm6Up6FVqliLuRFGic4Yn0ZixppsvwRw4pmsIVhNc1-QB7O4tV5G2hpMzy4ra5Q1ntJ-FVacYtikyWaVOHRwoBXQD3Cj6zk5kBDs9KPis_0jU4fEcMmRLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دختر شهید نصیرزاده: پدرم می‌گفت عزیزانی که کار رسانه می‌کنند ارزش کارشان بالاتر از ارزش کار ماست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/657926" target="_blank">📅 09:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657925">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaae64f0bb.mp4?token=udNtaH2M5_2T-k09nUbmsBFUB39zMetjX6tTjeDvpR58x_VySkKKicGLU5kLPeAVOqDLX0pzfVr7bAc_STTFUpo4Nop4hgLUakmjbfhTFXrXQG8kzQcPGafxYViqIfS5muNSvKVD9fLXFqEOCX5UbKDF7L0gb1kOBKEnU_PDD6Egu_ZWExXuMMDSgMij_BLBezoM4DOKDichT94867gypCKDqCz5d0ew7zFbYmXVeSuedhahYFCpo8Mky_Jw6xXSjySr_HYd4UePT-Izarz_3E6rencbH3VwEKXjlQHYHelPy8cU8_VXJ5UWMME4QQBCsyhtNJXioZrPVSm5Jvtp3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaae64f0bb.mp4?token=udNtaH2M5_2T-k09nUbmsBFUB39zMetjX6tTjeDvpR58x_VySkKKicGLU5kLPeAVOqDLX0pzfVr7bAc_STTFUpo4Nop4hgLUakmjbfhTFXrXQG8kzQcPGafxYViqIfS5muNSvKVD9fLXFqEOCX5UbKDF7L0gb1kOBKEnU_PDD6Egu_ZWExXuMMDSgMij_BLBezoM4DOKDichT94867gypCKDqCz5d0ew7zFbYmXVeSuedhahYFCpo8Mky_Jw6xXSjySr_HYd4UePT-Izarz_3E6rencbH3VwEKXjlQHYHelPy8cU8_VXJ5UWMME4QQBCsyhtNJXioZrPVSm5Jvtp3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت عجیب استادیوم‌ محل برگزاری دیدار بامداد امروز آرژانتین و ایسلند در شهر آبرن واقع در ایالت آلابامای آمریکا، ۳ ساعت قبل از شروع بازی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/657925" target="_blank">📅 09:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657922">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf9f16584.mp4?token=LtBsG8ZtY1egvCUG-kJtZ53ErlF0GiOY5MOub0F7QIG_rDn-fsF-O05PkXJ_nqgrR4ABUUFlbaVOmu_0t8YuXrrom6ti9xLy5T1f4JOetBWBHC2vPkGyww1SyZ0OTrTxzLLRglJSErGyC7QyMAEbBpi2owaJ-MMnzvIna0ro-MvQgn6u-ZH9WQSpKhuaDtUVrwn3Sy27wUGHlVmqg-aTFsz4a91IjumDKYSUElqf4P4YJBu6nXB5VIYRHw2gdEgtgZT60Pz-GpqCyClaFiBsbq4IdZvxS5t0dlu_adV1w7rCt4QnYgEEtMf_3eYVmY4byH9X0vCo9z1W5fINYvsYwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf9f16584.mp4?token=LtBsG8ZtY1egvCUG-kJtZ53ErlF0GiOY5MOub0F7QIG_rDn-fsF-O05PkXJ_nqgrR4ABUUFlbaVOmu_0t8YuXrrom6ti9xLy5T1f4JOetBWBHC2vPkGyww1SyZ0OTrTxzLLRglJSErGyC7QyMAEbBpi2owaJ-MMnzvIna0ro-MvQgn6u-ZH9WQSpKhuaDtUVrwn3Sy27wUGHlVmqg-aTFsz4a91IjumDKYSUElqf4P4YJBu6nXB5VIYRHw2gdEgtgZT60Pz-GpqCyClaFiBsbq4IdZvxS5t0dlu_adV1w7rCt4QnYgEEtMf_3eYVmY4byH9X0vCo9z1W5fINYvsYwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایه کارشناس فاکس‌نیوز به ادعای نزدیک‌شدن به توافق با ایران، درحالی که حملات ادامه دارد: اگر فردا بشنویم که به توافق با ایران نزدیک‌تر شده‌ایم و تقریباً به آن رسیده‌ایم، فکر می‌کنم کمی پذیرفتنش سخت باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/657922" target="_blank">📅 09:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657920">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2007b0e50.mp4?token=d2JoBzdKGvSx5XzVPP_BUTXa4koibSueObke4Jx87K6_uIJgeNZc7QQDtsmEBHal82eQiZlFSYcmN6Qkrgy9nYE5sjE5Ni7LM4B0BsF3oKCCpLublMzythsLQ6j8M6u6pAfmSBnyB1ZUI1v7zSvLueEv8n32RkOdBsh8PM0HqkZNf_F5R3bO_UFGpiyWvwPIJy3g3yZVG92FObEQiqgU7ovPALosW-qzqUPWcLY4Vq7DEfwEZZULoCfnthpvuBS4lA08dHl7be-k_lSBq6dqeDK8n8HYCKOC2yU_3Z28qGcPjUKNJKKPb08u4ceqyfXGQRUVMhg5wwCfxUTSjC0jHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2007b0e50.mp4?token=d2JoBzdKGvSx5XzVPP_BUTXa4koibSueObke4Jx87K6_uIJgeNZc7QQDtsmEBHal82eQiZlFSYcmN6Qkrgy9nYE5sjE5Ni7LM4B0BsF3oKCCpLublMzythsLQ6j8M6u6pAfmSBnyB1ZUI1v7zSvLueEv8n32RkOdBsh8PM0HqkZNf_F5R3bO_UFGpiyWvwPIJy3g3yZVG92FObEQiqgU7ovPALosW-qzqUPWcLY4Vq7DEfwEZZULoCfnthpvuBS4lA08dHl7be-k_lSBq6dqeDK8n8HYCKOC2yU_3Z28qGcPjUKNJKKPb08u4ceqyfXGQRUVMhg5wwCfxUTSjC0jHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روايت رهبر شهید انقلاب از روزی كه پيامبر اکرم دست عزيزان خود و حضرت علی (علیه‌السلام) را گرفت و به ميدان آورد
🔹
بازنشر به مناسبت روز مباهله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/657920" target="_blank">📅 08:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657919">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4ao_Av0pFo2cckvgrFp5MYSilu9yhAVBlytBlI4KygbryYnnWBcFYtP95EZ-r_AdL2Q6j5b-4YbWuZ6b9siop7dmdCEMFSbnne8bEYKVBL0fu_rkd_ZZJi2utLAuFXwlluVALpKyx-RUbunjeNQLgSE1YwmsEQ7mU4bXvqBBbf-iRBFeN_8-jDKTeuxJN5iaidIZOko5-ehY8lRVMWOKHorqhaI5D04jAT88AV6ti0sH10Zt9QMvr8aG81ZH78feP3hvQVhwQjZeqQbvOAACs_ANsaicpEFuuvTE7HE50GBT2UBlM9cahGuDlap-wKi9GPZ8WwvzPXVU083gCq0gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مباهله؛ روزی که حقانیت اسلام در برابر تاریخ درخشید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/657919" target="_blank">📅 08:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657918">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
وزیر علوم: سهمیه جنگ در کنکور ۱۴۰۵ قطعی شد؛ جزئیات نحوه برگزاری امتحانات
حسین سیمایی صراف:
🔹
همچنین امتحانات دوره تحصیلات تکمیلی، همانطور که کلاس‌هایشان حضوری هست، حضوری خواهد بود.
🔹
کلاس‌های درسی و امتحانات دوره کارشناسی نیز غیرحضوری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/657918" target="_blank">📅 08:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657917">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPPaaD-FOvQURzH17uSVLMSSoCSuQ-ISJW_EgDwlUivF18ofA9pgww96uQrIjpg12STLfGN9WkK3D3GcoSRmUoOg_iNPlAxoDTXzFvKmrWWcVhyhBUYH7NJBMKa-y4fV9iTG3Afe529PRx73gLqsWpxvkhUz3XEeKihoT9wcgdvq_xNeQS_4YAa-MrT5Y27Uj1qrMY1b-T_CpFVoSOjr-1Zbw9SfkWNiGCQMvvHXkPSG-gclZNcWTDjmjI-D1l45C8FxIjaec8FGGGAtAUs3VMPqxBVJjPE2B8WyqEF0V1EsEYuQytMZDl-i1IjEvt5LBhBwn3ILhoM2tRm7PEs3kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونمایی از تابلوی نتایج جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/657917" target="_blank">📅 08:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657916">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7377d61fd8.mp4?token=O8OSH7zJr3yB5ifzwZTRyxWRcAln07bkEgpmUWwsCHTnA3z02W6RIqzHSUFhelvOON1D3QJ0bA_xj5KlPAPpvlm6rM88pBgrimVu7hPTY8Ger107VuF1LMhb4zb3pQVaxirieBeQMyfWXUVk6x50nNe8JIskRV3OFcKZw5pSculiyoFtMJFMZRn8XXL5nZBbkCDn0kGpCizk5f3guApKWn5FVYCmQaFe-s_dwtnuTGJk9xFQvnF0MMwuevsN2tKUBvZ030aZdojlSU5Ou4p-hWmWbR_OyThU3urVnE1SbmYeSuQaOSrqojRPd5P09QRufV35LVM4hjeFav7HDEAcsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7377d61fd8.mp4?token=O8OSH7zJr3yB5ifzwZTRyxWRcAln07bkEgpmUWwsCHTnA3z02W6RIqzHSUFhelvOON1D3QJ0bA_xj5KlPAPpvlm6rM88pBgrimVu7hPTY8Ger107VuF1LMhb4zb3pQVaxirieBeQMyfWXUVk6x50nNe8JIskRV3OFcKZw5pSculiyoFtMJFMZRn8XXL5nZBbkCDn0kGpCizk5f3guApKWn5FVYCmQaFe-s_dwtnuTGJk9xFQvnF0MMwuevsN2tKUBvZ030aZdojlSU5Ou4p-hWmWbR_OyThU3urVnE1SbmYeSuQaOSrqojRPd5P09QRufV35LVM4hjeFav7HDEAcsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهر: منابع خبری از شنیده شدن صدای چند انفجار در شمال عراق خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/657916" target="_blank">📅 08:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657914">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9589895de9.mp4?token=NXY7QVvD7lP5gRr9spdOVge67EN0BQkzitYcVnOwka_IOqYFvpdn1JQrnPGADHbXqZVSCGb4oz6kmkesoPkdbRGE2UBADjnPTJWwG4ZuDRzLkEOauyttuECrJ_eKqQ4p5gKGSGWdFqnhdhoySlvHeRD0irJX8fyLA_2ZDmvvygq3jEeOXQ0wzIDB-btI_YKO0DcR1bvkR289MXnDOF8oS9wUMeBBIL0oTH3g_vqksk5BaFnRzPJEPv4MnZMGM0_0Oqo6mQglCXblHmwdW-xWnRr10aOqjF7r7wF2eO44SkpgZldYQBw-ff4bEBAr3Bl-0TSc2-EMqc74KUy4BqBs2RZQPBrHo992miWy4eYeB5A4NlsuMmweyOFNJpUXbw9DXVKVWRtR6YQ-TLUH94gBG9uz0nErns23I-cO3RGHmbYtfRpd9ex0zhGGr-sX5mi26-JSB20gQN5IwRXfdl0c68GSYK0nyt4y4c0iQO-6GAe2Dr7DK8eGWaHQ8gWugBKpuJoySMSoAXzvpLOYQUaHhKGQkWFamFVQbvvLHMmmCmVTIeMIgR-f6PCvMfH7XgOVgqwVb--0URu1meUAZc-hWTrZfNJXv5mNYQElCKsWSuPrs0NvCcNIdS3edgkNFDpu3WiBUh4VGlD8dBYZaIbrnIOH-KugoqHDqGEBiZ0p-Vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9589895de9.mp4?token=NXY7QVvD7lP5gRr9spdOVge67EN0BQkzitYcVnOwka_IOqYFvpdn1JQrnPGADHbXqZVSCGb4oz6kmkesoPkdbRGE2UBADjnPTJWwG4ZuDRzLkEOauyttuECrJ_eKqQ4p5gKGSGWdFqnhdhoySlvHeRD0irJX8fyLA_2ZDmvvygq3jEeOXQ0wzIDB-btI_YKO0DcR1bvkR289MXnDOF8oS9wUMeBBIL0oTH3g_vqksk5BaFnRzPJEPv4MnZMGM0_0Oqo6mQglCXblHmwdW-xWnRr10aOqjF7r7wF2eO44SkpgZldYQBw-ff4bEBAr3Bl-0TSc2-EMqc74KUy4BqBs2RZQPBrHo992miWy4eYeB5A4NlsuMmweyOFNJpUXbw9DXVKVWRtR6YQ-TLUH94gBG9uz0nErns23I-cO3RGHmbYtfRpd9ex0zhGGr-sX5mi26-JSB20gQN5IwRXfdl0c68GSYK0nyt4y4c0iQO-6GAe2Dr7DK8eGWaHQ8gWugBKpuJoySMSoAXzvpLOYQUaHhKGQkWFamFVQbvvLHMmmCmVTIeMIgR-f6PCvMfH7XgOVgqwVb--0URu1meUAZc-hWTrZfNJXv5mNYQElCKsWSuPrs0NvCcNIdS3edgkNFDpu3WiBUh4VGlD8dBYZaIbrnIOH-KugoqHDqGEBiZ0p-Vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش هولناک خبرنگار آمریکایی در نشست مطبوعاتی کاخ سفید: اسرائیل از صدای ضبط‌شده گریه نوزادان برای بیرون‌کشیدن ساکنان اردوگاه آورگان و شلیک به آن‌ها استفاده می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/657914" target="_blank">📅 08:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657913">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
تصاویر شلیک موشکهای سوخت جامد و مایع دوربرد قدر و عماد و خیبر شکن به سمت اهداف امریکایی در منطقه در پاسخ به تعرض بامداد امروز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/657913" target="_blank">📅 08:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657911">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36823db122.mp4?token=NmR6kf26mnA1LR3SyEscqvuJVC0SrJiaA8TXXjaCenkfxihhpEowQFKMQoJAtRXQuL2dl4HWQI4jiLtBbl14WeqfKjMU5J3twHJ0Cz3DLtqxTLKXyKrfUhnNX3zSC3g11sl5mxTICFF10ejdN5mWnIN6s4ZOFIt4zihD04DabheCwmby5D7YLLmg_nlKRddRxT3M9vPW8UBOXv0LJ_4vqRSmX0oH97QgJGMz6QxN3Ap6WeTHkXiBbc6VI-lUFCJJI6IHXudMlkO2EN540JpDCn7EMPo_QCJ73IJOhHIq-Ub_bw6SKdFsZwPR4QsKoUdxm9Wj_gZZMj6bliJipgmZTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36823db122.mp4?token=NmR6kf26mnA1LR3SyEscqvuJVC0SrJiaA8TXXjaCenkfxihhpEowQFKMQoJAtRXQuL2dl4HWQI4jiLtBbl14WeqfKjMU5J3twHJ0Cz3DLtqxTLKXyKrfUhnNX3zSC3g11sl5mxTICFF10ejdN5mWnIN6s4ZOFIt4zihD04DabheCwmby5D7YLLmg_nlKRddRxT3M9vPW8UBOXv0LJ_4vqRSmX0oH97QgJGMz6QxN3Ap6WeTHkXiBbc6VI-lUFCJJI6IHXudMlkO2EN540JpDCn7EMPo_QCJ73IJOhHIq-Ub_bw6SKdFsZwPR4QsKoUdxm9Wj_gZZMj6bliJipgmZTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک اشتباه رایج در حرکت شنا! #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/657911" target="_blank">📅 08:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657910">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyRpecMaD1Twoq1eSev4jQo36moVIcI6EDSnFfWlo4Kk7Cv5NjBeqYtgVp1KMp8S6Ncq-RBxNN-Y6f-5xxtVHpK5Wp21rCMuB8eLt1E6zZgj5_UHa-E1goZlj4ZTq5iQIZGo5vHQlqQbgOhEdM3qX9bS-b3QKI3_0rwoYxmh70Ik26B2iYp53p_tkVXmu6HZEPdr5Nm2hg-ZmRLRNb3yD03k2gXxqU4-__AfmGh1pHlkj-2n0wKGcEjMrsntrSwSwsQVIuUlnt_cOargNumJqLv2eIdIiUGIc2BSMjBwPofJhudnQVILt65s5ChEg8fAvxQ3geKH8G7rw9ywIZ_UdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه در خصوص اقدامات تجاوزکارانه آمریکا علیه ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/657910" target="_blank">📅 07:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657909">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
قطعه «تهران» با صدای قیصر
🔹
من شهر زیاد دیدم ولی هیج جا برام تهران نشد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/657909" target="_blank">📅 07:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657908">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzKZKrfM64HDWPTHu1s9ae11Ukds4_oRFzT11pLeQHGxNuRlH_93DG_Cf-kUdxO0agCzz1D-Rram_30E4NgDphCS8L_hB-W3UsJlxdBnFX_zCIP_I4lsXNp53udoCymQ9et1uWpzzxiIflFsdslqHSWW3V_oa-XukaJU9e5NEHLV21B5DMpHrAcCmNUKbchNjJPjDw0abFDJunatGqQx9n_ep1tPCxnvicNcJNMY8K_Apht52inZC2R0QTi2YUHRFKmBOKRi4OOABfSlvdPh8Vt23kyVqzkT3PK6LDYkden_NVidEkSPSxvF9wAOjNCrkSqy4-HX6hB2NsJKG4EyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‌
انتقاد آمریکایی‌ها به سوتی جدید ترامپ
‌کاربر آمریکایی:
🔹
خدای من! ترامپ به معنای واقعی کلمه «افزایش شدید کسری تجاری» ما را جشن گرفت. او حتی نمی‌داند «افزایش کسری تجاری» به چه معناست. او فکر می‌کند به این معنی است که ما بیشتر از واردات صادر می‌کنیم، که خوب است، اما دقیقاً برعکس است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/657908" target="_blank">📅 07:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657907">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_YHMkjk8qi-J099ER4NXlGpdLFUn6_mYmr2mKuW-sCvtICXFIG0hPebpfX2V8GQQc5-IWgtvsn6NP3K5WGy-5CDKAHGzm0NTrgxXrWyNVYnBPzkx-a-bMgblh793bcYnJeIu0hrKXStU3krn2AZGwMBa0YTJoWABaJHcUDAfcC-eY7WQfaQNDdP3VZxPjt_rW4ieTNUKbrsln7UBT9bMw9_UVU2G43CFZ9Sl_qLQwV_hhl0rhesIh5f92bRVwv0xENINrDPj4_wTeDkI-RghwyBMaqGNVhnZb4NbO8bFnGZ7pBKutJX7EFP48agZ7yec_OyNomP3Qnx4eo_Evve-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه هیچ صفحه‌ای در توئیتر ندارد
🔹
سپاه پاسداران اعلام کرد هیچ صفحه رسمی در توئیتر (ایکس) ندارد و تمامی اکانت‌های منتسب به این نهاد جعلی هستند.
🔹
پیام منتشرشده در یکی از این صفحات نیز با هدف ایجاد تفرقه عنوان شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/657907" target="_blank">📅 07:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657905">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fdbba6d5c.mp4?token=Bzv0I-bnBu2c-MLSBk5wrLhzdamuuRy9qsLj2bVogEgkXJioYnkq4CiRmuvg8jD5FumKSA2TIDJZ-Y5hGCEZHw620nV0zFxxdS9kU9zTqbPbhb1LiJY11n9w-UHCv6iA5_My-wHKSxuHu-hJVBWDCry__YEa6NkqdlB8QDVZUOTcy34vJIAi3xfl90uN7LOV14p4IkiYMhmyAoeKiDoAMSo1hC-r941SHVk7VjYUO37Ubi1vHK73uMcVuPRrGpaNtJtbofoItMgZnia91IwAASPuUrh5gsVd7i_lW1f7iNwpRT6n_EYmv37mhCN2iPOvr81z6lueNlFxNCP3-K-zQCXjZNKFNH2GOliNbG-wZg9TBvWd1ul7bPXV_9rj-qIzvHM3q5se6prnW051coD-wSV22Hzv5_b8tV8Xu5We9xAXKEG4dvrGPZCCOD4gLSr18y0p0US2O5qQKKrshXjuP_DijncU-uKz8gaD0I34QOHupK4RID7gYSma9viQjkCbZ05z3uvTZxFtSLTT8elaYGBo-eqO8QXupbx9oEP-vAQcbq8facbG0-FrKDa-OYSKk7OEcB_s5Rr_DnJbEnNBqPH88mTGo7FP3GL1dKei7UgHx2yIprnMqX-q1LHBp7plkxjLiYSmntlUdzI1kV27rvnwovL84L3Ej73QNUTVePA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fdbba6d5c.mp4?token=Bzv0I-bnBu2c-MLSBk5wrLhzdamuuRy9qsLj2bVogEgkXJioYnkq4CiRmuvg8jD5FumKSA2TIDJZ-Y5hGCEZHw620nV0zFxxdS9kU9zTqbPbhb1LiJY11n9w-UHCv6iA5_My-wHKSxuHu-hJVBWDCry__YEa6NkqdlB8QDVZUOTcy34vJIAi3xfl90uN7LOV14p4IkiYMhmyAoeKiDoAMSo1hC-r941SHVk7VjYUO37Ubi1vHK73uMcVuPRrGpaNtJtbofoItMgZnia91IwAASPuUrh5gsVd7i_lW1f7iNwpRT6n_EYmv37mhCN2iPOvr81z6lueNlFxNCP3-K-zQCXjZNKFNH2GOliNbG-wZg9TBvWd1ul7bPXV_9rj-qIzvHM3q5se6prnW051coD-wSV22Hzv5_b8tV8Xu5We9xAXKEG4dvrGPZCCOD4gLSr18y0p0US2O5qQKKrshXjuP_DijncU-uKz8gaD0I34QOHupK4RID7gYSma9viQjkCbZ05z3uvTZxFtSLTT8elaYGBo-eqO8QXupbx9oEP-vAQcbq8facbG0-FrKDa-OYSKk7OEcB_s5Rr_DnJbEnNBqPH88mTGo7FP3GL1dKei7UgHx2yIprnMqX-q1LHBp7plkxjLiYSmntlUdzI1kV27rvnwovL84L3Ej73QNUTVePA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از دنیای لگو تا افتتاحیه جام جهانی ۲۰۲۶ آمریکا؛ این ویدئو را از دست ندهید!
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/657905" target="_blank">📅 07:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657904">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtBR5bQlQZ20FOvZ9rYyRnTpGhRCZLBO8Zgx2eCk-R_GC89t1owRVgd_zuV9mr-451sZKkiN0wCSiTdEULfzOYUxeSVjMzlLHCIMCqGHK1iPIBjWQPiS7Qm-a1rDbtCi2oQwljphwmbWqKT-ki2QG-cLQ4IlvEdzRiBgz6icRYf2Jnr0gzCcynDDX7vJjLhunw5w031t4LowG3PDOLQywlm2RPe-xjjOVldmIk1hfV-sR8tyccCciDzrByok3rJsmDc-D7dUcq8QTyIv-Sbf2hd1wxhogwB3iwyXs8Pluw6lEANBmDwIdSwvSsky6_SfDKO8x5goCLorGkKxFSQWMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۲۰ خرداد ماه
۲۴ ذی‌الحجه ۱۴۴۷
۱۰ ژوئن ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/657904" target="_blank">📅 07:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657903">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2YaMlxhMyMjnyMPL1yOeBiYfx-Dk4XozgcUuaOeVzROebNCMCsTjOT0LF6LJyLqk1UI-Ee01NRrT1OXfDnahxNVMiBIPHOFHJoNakCjUKx2nrk0whzeb_1JdJPhwu3SEDPq1aMyNox4UtgfTRterUkk1jjFUcYDUdhKEf8ne485nGBAdhjT_VvhQPLKs3wLS_sUohQFXXvHWM5DW_ua8Y-ZOTwhMqeEN2z1fQZTXn5srwS6ARR7yp34YV6G3EWj_Sjz1AtBkepT-NbLhBIvqVl5FlUuyvvIy7GCHdZZYB1H0NYRxjpjU4A9hZATzaO3Sj1qkdBxqgj8mn2RYYUUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سینای ۲۰ ساله اهل یکی از روستاهای همدان
در نبرد با سرطان خون است و مادرش با دستانی خالی، تنها تکیه‌گاه اوست
😭
💔
تهیه  داروهای گران‌قیمتِ بازار آزاد در توانِ مادر سینا نیست
😔
برای اینکه سینا به آغوش زندگی برگردد چشم انتظار همت شما هستیم.
😭
🌹
با دستانِ پرمهرتان، مرهمی بر زخم‌های این خانواده باشید:
شماره کارت/شبا خیریه نیک:برای کپی کلیک کنید
6037691990491201
5892107046740463
940190000000116489768002
پرونده بیمار
|
مجوزها
|
پرونده‌های تسویه‌شده
|
تلگرام نیک
|
سایت خیریه
|
برای گزارش پرونده های درمان زیر ۱۸ سال پیام دهید
@PoshtibaniDarman
⚠️
مازاد کمک‌ها صرف امورات مؤسسه و یاری به سایر کودکان محروم خواهد شد.
💚
آدرس کانال ما :
👇🏻
👇🏻
https://t.me/+YQ8wu_Q7QahjNmNk
https://t.me/+YQ8wu_Q7QahjNmNk</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/657903" target="_blank">📅 07:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657902">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال در خصوص تغییر نظر ترامپ
وال استریت ژورنال به نقل از مقامات آمریکایی:
🔹
ترامپ در ابتدا نمی‌خواست علیه ایران اقدام تلافی‌جویانه انجام دهد، اما پس از توصیه‌های وزیر دفاع و رئیس ستاد مشترک ارتش، نظر خود را تغییر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/657902" target="_blank">📅 07:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657901">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
طالبان: ۱۳ نفر در حمله هوایی پاکستان به افغانستان کشته شدند
🔹
سخنگوی طالبان افغانستان: در پی حملات هوایی ارتش پاکستان به سه ولایت افغانستان، دست‌کم ۱۳ نفر کشته و ۱۴ نفر زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/657901" target="_blank">📅 07:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657900">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
مقامات کویت انتقام ناتوانی در مواجهه با ایران را از شهروندان می‌گیرند
🔹
دادگاه تجدیدنظر امنیت دولتی کویت یک شهروند شیعه این کشور را به بهانه عضویت در حزب‌الله و نیز سه نفر دیگر را به اتهام همدردی با ایران به مجازات حبس محکوم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/657900" target="_blank">📅 07:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657899">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
تاکنون هیچ گزارشی از بمباران در خوزستان نداشته‌ایم
معاون امنیتی و انتظامی استانداری خوزستان:
🔹
تاکنون هیچ گونه خبری مبنی بر بمباران نقطه یا نقاطی در استان خوزستان از سوی دشمن، گزارش نشده است./مهر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/657899" target="_blank">📅 07:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657898">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
منابع عربی از انفجار دوباره در بحرین بدون به صدا در آمدن آژیر ها خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/657898" target="_blank">📅 07:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657897">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حملات رژیم صهیونیستی به جنوب لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/657897" target="_blank">📅 06:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657896">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اعتبار کالابرگ سرپرستان خانوار دارای رقم پایانی کد ملی ۳، ۴، ۵ و ۶ شارژ شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/657896" target="_blank">📅 06:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657895">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
حملات پهپادی ارتش به پایگاه‌های آمریکا در منطقه
🔹
ارتش جمهوری اسلامی ایران با موجی از حملات پهپادی، پایگاه‌های آمریکایی و سامانه‌های راداری ناوگان پنجم ایالات متحده را هدف قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/657895" target="_blank">📅 06:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657893">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">منابع خبری از حملات هوایی رژیم صهیونیستی به شهرک‌های النبطیه‌الفوقا، حبوش و کفررمان در جنوب لبنان خبر دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/657893" target="_blank">📅 06:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657892">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cad7c4a14.mp4?token=hp5fKlnl3BFTaNapc2CRLKmolOLFhdKubxNuLgoH_4Np20u-EyYEaC96A_G6S7dA6QkiI6ex7kMacB2TVc7Vfqc1I-kU6gf4X3QMcBEdiHxIG7SiTw6Zz1pClJuCzIikI_TVjlR-UtW8KTfSMFK0ERzHn1uWWoTBXlyxF8XMcrOQQJhewyR31-KEnMEXPANJu4yerJtH-27f5JmlGJ5neMUzO3r_HZmEotghxOruMdr9zZkzyoLe_u19FxcnJGeiiUxGK12xF0gN9SBBTiAzJWvaIKJYQlRiS2lLoYjJNnupm-WDDEDt60unG4frg3BN0CMf_aMYHZVpEVczmG5WIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cad7c4a14.mp4?token=hp5fKlnl3BFTaNapc2CRLKmolOLFhdKubxNuLgoH_4Np20u-EyYEaC96A_G6S7dA6QkiI6ex7kMacB2TVc7Vfqc1I-kU6gf4X3QMcBEdiHxIG7SiTw6Zz1pClJuCzIikI_TVjlR-UtW8KTfSMFK0ERzHn1uWWoTBXlyxF8XMcrOQQJhewyR31-KEnMEXPANJu4yerJtH-27f5JmlGJ5neMUzO3r_HZmEotghxOruMdr9zZkzyoLe_u19FxcnJGeiiUxGK12xF0gN9SBBTiAzJWvaIKJYQlRiS2lLoYjJNnupm-WDDEDt60unG4frg3BN0CMf_aMYHZVpEVczmG5WIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی منتشرشده در منابع عربی از اصابت به بحرین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/657892" target="_blank">📅 06:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657891">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">در پی سومین موج حملات ایران به پایگاه‌های آمریکا در کویت، ستاد کل ارتش این کشور از تلاش سامانه‌های پدافندی برای مقابله با موشک‌ها و پهپادهای ایرانی خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/657891" target="_blank">📅 06:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657890">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هشدار عراقچی به آمریکا: منطقه را ترک کنید تا در امان بمانید
🔹
وزیر خارجه ایران در واکنش به نقض آتش‌بس از سوی آمریکا که با پاسخ قاطع ایران مواجه شد، به واشنگتن هشدار داد که اگر می‌خواهد در امان باشد، منطقه را ترک کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/657890" target="_blank">📅 06:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657889">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ادعای ستاد کل ارتش کویت: سامانه‌های پدافند هوایی کویت در حال حاضر در حال درگیری با اهداف هوایی متخاصم هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/657889" target="_blank">📅 05:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657888">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcc150c12.mp4?token=jUf7-kj5QF6eRm7jdo9RdBKn26ZOvFKQ31gSn98R630R14pBFsp4SaCmWegvKluiwuRzpF-_nWBHrKjYSW9WVJS4ZR3A_q7k87nxiKsOtuMhaWYhlBno8sSnsDOV6QqVpaXmHGHt7jY28XYgqp20FhsyEsNFzACvAJa-JgMXpGrkdJFMN3K3YpMDFBa7izKgQgHCNi2VVyFibm97xka81VCoG-kH_LkUcBb068OWNMZsgPOUXsA2qX2HYS7yKIqN5cVnRLGV0QzWbqWUJhIqgf4xl2Hl-VAo6c2LkjlgVNrVWoVVLZQcgRGceYVEYDX3iz7mBPba4N2yh03f6qk5mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcc150c12.mp4?token=jUf7-kj5QF6eRm7jdo9RdBKn26ZOvFKQ31gSn98R630R14pBFsp4SaCmWegvKluiwuRzpF-_nWBHrKjYSW9WVJS4ZR3A_q7k87nxiKsOtuMhaWYhlBno8sSnsDOV6QqVpaXmHGHt7jY28XYgqp20FhsyEsNFzACvAJa-JgMXpGrkdJFMN3K3YpMDFBa7izKgQgHCNi2VVyFibm97xka81VCoG-kH_LkUcBb068OWNMZsgPOUXsA2qX2HYS7yKIqN5cVnRLGV0QzWbqWUJhIqgf4xl2Hl-VAo6c2LkjlgVNrVWoVVLZQcgRGceYVEYDX3iz7mBPba4N2yh03f6qk5mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رد موشک‌های ایران در آسمان اَمّان، پایتخت اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/657888" target="_blank">📅 05:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657887">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">موج جدید انفجارها در کویت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/657887" target="_blank">📅 05:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657886">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یک‌ منبع آگاه نظامی: ایران با استفاده از موشک‌های دوربرد سوخت جامد خیبرشکن، آشیانۀ جنگنده‌های اف۳۵ آمریکا در اردن را هدف قرار داده است/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/657886" target="_blank">📅 05:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657885">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بسم الله قاصم الجبارین قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ  سپاه پاسداران انقلاب اسلامی:
🔹
رژیم جنگ افروز آمریکا در اوایل بامداد امروز با بهانه های واهی چند نقطه در جاسک،…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/657885" target="_blank">📅 05:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657884">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تلاش سامانه‌های پدافندی آمریکایی در پایگاه الازرق اردن برای مقابله با موشک‌های ایرانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/657884" target="_blank">📅 05:24 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
