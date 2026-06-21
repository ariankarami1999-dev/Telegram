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
<img src="https://cdn4.telesco.pe/file/R0QujRp0kFMGFtf6GFXynj4rVje2RDKrKsBeb3RNzUpdc3X2eJ98d2R991Ej8CwSnFNxcTHIkRoao110YM8KpDwMsdSbQ50buVGrNVxD5-hn44FWYbOrcA0yKc2Ggo_YU1RYjzJo8TG3j1C9FbnXG_2nKZFR-kJm6gk-JxQO0HuhCTR29-3V7RDsfdRqnZZ3xdIxL5T2ziIcQRcRjd9N6LhBknGb1B0Ux-BJ-93N28C-HpF6jN-a259ATY9yZhzh1IlF_Gg70nMRru1zCHv_C9SvwahXvUM3IFeFHS4V9nx7q3vCVsOw7Uo384ZLFktqSslbpccLKgixcSS7IrUsvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.4M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 21:50:26</div>
<hr>

<div class="tg-post" id="msg-661949">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uF1Czo3VtAmpoW-l8kJwR0yvRql63KC8J7vLXZmswlYApA8CkWZiKJBT8im2JtMfRNZ2kLulBM3Zm_dElCX_TLp4mztDB4pMTR6ymrXc4iC5yhoheIxy-V9LqzDdMmnEzU9F59cDC289r9UJ9iYgBje_aQzJXfYS-mPoDp3WY59PhV5RK8lL2u27-_VQ82M6ofHMxjnuvHhEgWwvuUuB1IRwBanzwWqmYiO6KLE2MTxQId_ieOwv2mCaj12H3F9yq3HA-6KOKeb7TaFuxxNdyaS9GBCZ573Hi1RSiO-VMsB5EKjD_7pmhEXaQljQ7wI4nAGLmME2LrJukmxRKM35Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PsP9QwFAAsPtvWOsze28XXMnJ3Y6f4DZWHJaZcwrGNI_NSU4Fi1xykiA8L5irXLUtVpu9qg3o--O_kNnMMsgwLfmqahkNgn-Z390rT5BGxw_chEdewp4npvcEYMRlpY2Y-qXkrlq8VmFC9FdPJAuF-GnJo2-UorYYjs1ziZ3wv4wuXUvJ8O6rB-swe-djf924u_tbNOmkVK30LgoINNwT2c6ErcL6gZ_QyLBHjIYc7_TvrYX-dTKZeNwWANndBnuKp355J2ItHU2MIv6PUHOFkZQ3gVUmKT9QgY39p7sRO9JEX-vgqK1rdHOICH0n6oGADXalW-Fmcq4DbSPjV7DGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
میکائیل و محمدطاهای عزیز، فوتبالی‌های شهید میناب؛ بچه‌های ایران تو لس‌آنجلس و روی صندلی‌های ورزشگاه به یادتونن و به جاتون ایران رو تشویق میکنن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/akhbarefori/661949" target="_blank">📅 21:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661948">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
شبکه کان اسرائیل: ارتش اسرائیل شروع به کاهش نیروهای خود در جنوب لبنان کرده است
🔹
دولت ترامپ از اسرائیل خواسته است که عقب‌نشینی جزئی از جنوب لبنان انجام دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/661948" target="_blank">📅 21:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661947">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
اهدای پرچم گنبد حرم مطهر حسینی، برای تکریم و بدرقه پیکر رهبر شهید
🔹
عتبه حسینیه در عراق پرچم متبرک گنبد مطهر را برای تکریم و بدرقه پیکر رهبر شهید به سرپرست سرکنسولگری ایران در کربلا تحویل داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/661947" target="_blank">📅 21:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661946">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
جولان نظامیان رژیم صهیونیستی در خاک سوریه
🔹
منابع سوری از نفوذ یک نیروی نظامی وابسته به رژیم صهیونیستی به منطقه الاصبح در حومه جنوبی استان قنیطره خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/661946" target="_blank">📅 21:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661945">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromایران روشن</strong></div>
<div class="tg-text">🔴
امشب یه اتفاق عجیب توی بازی ایران و بلژیک قراره رخ بده!
این کلیپ رو جدی بگیرید و مراقب قفلی زدن روش باشید
😁
#ایران_روشن
💡</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/661945" target="_blank">📅 21:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661944">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: ادامه‌ برنامه مذاکراتی هنوز مشخص نیست؛ واکنش‌طرف مقابل به پاسخ رئیس هیئت مذاکراتی ایران، در برابر صحبت‌های رئیس‌جمهور آمریکا مهم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/661944" target="_blank">📅 21:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661943">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97e68e530.mp4?token=myfx3vjqUlXaTLVUbPZ148-Rp_qxnb0sttwDZJCCiR2R6E0O-xcY8LFs_f6BhQlLNlsu7PIsNvGdJWHTETklwpfEueIAskz8PdJqDjDWAnbiFouBM_lIYykaBtL9b6m7IzAsy6FBfmAyCfNx0wCOiuD_y6pptFh9v4AOAjd0EKqEAto71NAMqPzu5-pkOPeht7p-hpOKS7xJ4b65hM-CMl6jdQdZ5JHiLUy0eixGr8-PFSasHbQEB1uTEXnhsbzpXI3p0mPYuXqrw3D35gbR3l-zVLze6c2VrG9ZsOMU-YsUgB519U6Zxqgpnti-iHzQgG0tB8e0QZ_OFkZZWdFMl4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97e68e530.mp4?token=myfx3vjqUlXaTLVUbPZ148-Rp_qxnb0sttwDZJCCiR2R6E0O-xcY8LFs_f6BhQlLNlsu7PIsNvGdJWHTETklwpfEueIAskz8PdJqDjDWAnbiFouBM_lIYykaBtL9b6m7IzAsy6FBfmAyCfNx0wCOiuD_y6pptFh9v4AOAjd0EKqEAto71NAMqPzu5-pkOPeht7p-hpOKS7xJ4b65hM-CMl6jdQdZ5JHiLUy0eixGr8-PFSasHbQEB1uTEXnhsbzpXI3p0mPYuXqrw3D35gbR3l-zVLze6c2VrG9ZsOMU-YsUgB519U6Zxqgpnti-iHzQgG0tB8e0QZ_OFkZZWdFMl4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات آخر در ناو دنا دقیقا چه گذشت؟
🔹
روایت هولناک یکی از پرسنل نجات یافته از ناو دنا در حسینیه معلی شبکه سه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/661943" target="_blank">📅 21:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661942">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YylRNuW-jP4hf48R0zRkTAAcFf54g6lo2vEoKlbWGPLudib9LAIMMjHgZ7JBenCUWHEYnw4r4P3X0QplBGmcgzsKCl14-l_WkVknjMR8hKf7_knt1Zdx_G03gTzNGzdGkn04fMMFrVl2FAnANf8sGbdfbLxC33X9FiYDutCWMXYnn2UuL_sdkI2sAaOABBd3zsbq0KMMpI8FqStItlXIRsISlBBlUUXyVIfgZDOdFw0uh-OY8AjUW2XRQCrc5EWWHB2xI8QyAoZfsHK4J6CdeeSI5ggelBTyIEyxAY5Fx2rAr0tqeu-ygkkM9TS9D7z-6b1zT7p1DT8MM9B5o8NooA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرچمی که معاون رئیس‌جمهور آمریکا در مقابل آن قد علم کرده است، پرچم بلند آوازهٔ جمهوری اسلامی ایران است؛ همان پرچمی که آمریکا سال‌هاست در آرزوی براندازیِ آن، نقشهٔ تغییرش را در سر می‌پروراند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/661942" target="_blank">📅 21:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661941">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: ادامه‌ برنامه مذاکراتی هنوز مشخص نیست؛ واکنش‌طرف مقابل به پاسخ رئیس هیئت مذاکراتی ایران، در برابر صحبت‌های رئیس‌جمهور آمریکا مهم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/661941" target="_blank">📅 21:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661934">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mOMR2_jerdMjHFhaRyMKoaP24xQyUd9CNXOZ7RSdYLLHGoWtUg1ipMJOwqnRobSRUxwUBbOKx7Wexm_27WxHUqDJaPCFXju6ODWLC3-5X10wnZ1Wo6_sA4Jov5YwF5uf54RCUf8ceef1dQEfdeGrRuW-sOGGtr19wO6_jXWZBYyFmzup955G9TTxPl0PxECi1DyDewgqW2pGthbcJD-P4h-Pyk2vdh-K3wdAyAR5S38VO_xeeOQr0KOd5yqt30QhYe_JupDcZBDxCGYZAvLqHI1O77KeDqm0NWreJGT8RIPaFeO4sGReYtphLrEEJqcETuYVmcTPbYUlTM-CNsrYUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RM8CqTyxM5Czbiq86nZHjUotjcs86GHLu4vF_6hN4Lot1S3eVm2h6SUrsLWYI7XoN9eXOPicPY2uCgMDUsg3dDk5T4yGqncNOZzFq8oIuo1wlwpQp_TFPYRF_XHvKe5SL8_WM6qFIkYe5dyQ-Ie7aoVtbo3CtUlWxPdIwvckJe076x7UPOC5-2dxKC83an7DqRIzDN0D5lvvwksmEYbhDk-v4VVvAB4aNXmmgcgG9El_9zsZxZWvV2Pd2UdRrDYPOzED1iEt4q1L40MppK08qnQz3zFUdTQ53jQj2tgdBLGdffMv7UdrRosDx9kPKi4M76trVXQkX55SuKlOld4RwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1AClHakAgv1Rk6WCYeYFHgn_PNyBqX62whIxIR8CKMbMFaOnuer8M8dmklU3M4bAex5DM_0jTy26M81NB0964t2i8NMEyIphY-wykcLjCwsxctaerAS6G7x0Wv0HenZ_o4kxbkGetfeI-EHfgyEeAtcJ6SRfyIvPue68y7AtKJ-Jh7FHzmTP-IfnG2wZEf3k1yK27jpZa6TzqMPckYO8ykZIkuL9bJZ7Gliofbdf1-ZkhlfjeMrwUj9y7_vXLpzhJkpegNheupX_8lxuT2zn8hl2-J-p3f6Y2zdf3L-QRAXfniYLZvokhJvxPKTWWTTNvyRHaV3oW9QVzrojEBSnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rw7LtKIcMa5kngG9ZQ-XGcr1t6OJEPhGo_rUMZnwelGlCIwnA3PAt4ww2okued0-nrgogZjOuO3dxs3_52nB57k1oBZO2KF23pFfI2JCpe0hs6-_Th4SSEzHnn3sJMGp516e05PSYe9KLd-tQZ1-g0RQwlIkFow1WWHq6q367s8sfZ1_kSNZf76kUgDyc14NcV-4LWddm0a6fVaU2d6NGLxTzaQE-oC1FquSn2jGfq36LNA5DGZ8mTV9vqZ9MxILX6PwLISF-CSo2W8Wh2GcABdEJYlGoZ05N5s9ihAo0And5PBi_jZxqATCG6ufudnV2v8H6bmCpvPw8G8yZcSqbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a_JTvxHiZyhZg_F5CUpqltr-Leblh3fOggK1TqObcda-CBaxHjH4QuGI-ia7o3bWpX3jj2YWsquWJrcZ413BQvVgY1OSQ-Tc-Phax1P1QXUj510Z9vLarcgjwYlq8PxdFHOlWptYpvow61O7Qt8a54dMDZWtwyryaoJ--CJA5YeLZcfjWnKhrq61vWTSRN9PiXqiUtHEi-tkqdd-g60Ac5jAlr30Xjm0XyyIat808aucT-kdQKfjSzCExPbtL5HTSCWH_J6POD-_u91IMd0g3Le1gPB0PDQQZmZTi9w_6HsCdxNV7Yxy-D1hEogV53KKpztokihvfSqoJuz1ImGusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bS8zGNzFewjGxj0qyronOjUvKW0nq8YXFBCqQm_QqYnIMa1qyMxuzfksQvhjqfn4vhoU4Gmfd12-ycYT49wdFE9X7fu05PfZuY0oSwMEUZT6o_EcJGy8mjHQA0-p5hXBuN1vxytFDw7R1Bcjs6OPDhHU-4S_3aKxGR_F4PNNJj4lrtkbF1LuhkYUINhunl0NBpcPHGwqV2Qpssv8E2s4l2eIoHwst1m5iaYAV-s8qv2aRNmRFReDQfpbS8vJiSnOCJD4-sP-0EuaTuALc6OG2azInn7qqp_rGdr5XykQrS8j80MC8Wdzf4T9ezbImPjk4BhS8TIkmYtnh7aEkcFszg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2YaV97Nu3ezSHqWAcn-zDcpT0WXWHlLjXU1FXF5Qk1RK6CEtr9cUD3IiKxCphoTwosob8vocnWc2oaNFRukS-5w6tOQ6oFVzjjKgnRAbzdjAR0zcqjdwqEPbKotHLlwui--Hh0pxEGPEewWf-B-Sb0-52HkMVUlSTB-X4rnx-y1ZxHLVfF55MehPQf6ERfaK_ouYM_UGyPpi2ZAEkw_j0fN7412ipAaJnMmaesJIHBXv_ei4Ie3dtvaOintoYA49mMZmaSYkVaulB5Dd9zb20yRFbx0OJ67pmXhQj-KcjpqF_ndKE-Q030EQUgkNO2C4SC4NNuJA6EAK_4dKtCM-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از رختکن ایران و بلژیک پیش از شروع بازی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/661934" target="_blank">📅 21:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661933">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8fazJhRgsPyinHoKOFzPwD8raCa6gzpDaUfi39PHswgFiOZNR9QtfWWA07qiSi7loFm7wU6KwcIFCBYdHVRFBwHbpWKde7UKjB8IHyFjQXvgNKZ7JP3Wj4-d4wqO9iv0vpDSy2wqccWKnxnVTXEWKyecqt1hD89F9j7sWbTFT-q6_59fY15bYzgeYH_2pa_vbdbBHF4Hj5Xer0PEzF7MPTFCaGCSFTJMAqu1MOW3J1B2lqAV-1ABeKWwWmckAv8zQqOICOBfmpUmvXKGBZVPwoPO8VgfJRBt9HsfFFLwizBXPB9a3aCHzmT5qYdbaDzEVHxz_1HwR834TrHS88nfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایوان؛ غول هوش مصنوعی جهان
🔹
ارزش شرکت‌های فناوری تایوان به بیش از ۲ برابر تولید ناخالص داخلی این کشور رسیده است.
🔹
دلیل این اتفاق، سرمایه‌گذاری بسیار زیاد شرکت‌های هوش مصنوعی است که باعث افزایش ارزش بازار سهام این کشور شده و چون هنوز به نتیجه کامل نرسیده در تولید واقعی جایی نداشته و بیشتر بازتاب انتظارات سرمایه‌گذاری و آینده این حوزه است.
@amarfact</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/661933" target="_blank">📅 21:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661932">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97f5f3735e.mp4?token=ZT3qreQH8ytVY7VgDSgMJMmzhBas-BrSTbBnX9bXGOZ8wN2Pi_Melx09xxWg5pg-jodS-iWsBYKuStgR7aN1wcoJmYdhOnu6ZtO4U1r6hVnMQ-wUybDKtPs47U0TgT1JsyecU2W8f_iS9VxBco_V_1Rw6vH8GcqbW_836RAThrMrwOFOqzZ-JJ1CDr8pLWDJHqFVAM_6mnewfOfcm4T8vgSswFZnbp49bEXChFfuYBc7H3pEnAlVGTHINGi5sVoPvupOGhaPWIjXDRqbZKYxGiiAmbuaIfb8_m0umpVN1il_HKb1vdo-sRtM6HHLGfFwozxudn0eScswXQdZsHDebi8tNR_PucGEjwbfbDS8MxpJ9o7ilFbCUQIUWikmybg51Y-POB548Id0IJsvY9oerRQaPMEwHSV-r0EGo2Lc8JsxG60poKZa-qW0Q3ZWWgFHLD8j93G07Izg7K2mG6753Vt_lV737BrpagH-wMFfogwwHCFBK6iAsgw3laL2M4WH-TMlgtej-8553q1n8Gybo-vHI5zxDPLb6aA7L4C8hH4OB3YsAaD-PzWTOJQuFyBE1NlOwQyNhceIxQPQ_Kln8-aPDbQHcaN5l-HUY9AYcN_uysb_i5QQe2DPnukJulA46kejR2C3UASSFUx8VEGZWNcVUE5bF6ohaSnDjcvxuhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97f5f3735e.mp4?token=ZT3qreQH8ytVY7VgDSgMJMmzhBas-BrSTbBnX9bXGOZ8wN2Pi_Melx09xxWg5pg-jodS-iWsBYKuStgR7aN1wcoJmYdhOnu6ZtO4U1r6hVnMQ-wUybDKtPs47U0TgT1JsyecU2W8f_iS9VxBco_V_1Rw6vH8GcqbW_836RAThrMrwOFOqzZ-JJ1CDr8pLWDJHqFVAM_6mnewfOfcm4T8vgSswFZnbp49bEXChFfuYBc7H3pEnAlVGTHINGi5sVoPvupOGhaPWIjXDRqbZKYxGiiAmbuaIfb8_m0umpVN1il_HKb1vdo-sRtM6HHLGfFwozxudn0eScswXQdZsHDebi8tNR_PucGEjwbfbDS8MxpJ9o7ilFbCUQIUWikmybg51Y-POB548Id0IJsvY9oerRQaPMEwHSV-r0EGo2Lc8JsxG60poKZa-qW0Q3ZWWgFHLD8j93G07Izg7K2mG6753Vt_lV737BrpagH-wMFfogwwHCFBK6iAsgw3laL2M4WH-TMlgtej-8553q1n8Gybo-vHI5zxDPLb6aA7L4C8hH4OB3YsAaD-PzWTOJQuFyBE1NlOwQyNhceIxQPQ_Kln8-aPDbQHcaN5l-HUY9AYcN_uysb_i5QQe2DPnukJulA46kejR2C3UASSFUx8VEGZWNcVUE5bF6ohaSnDjcvxuhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور بازیکنان تیم ملی فوتبال ایران در زمین چمن ورزشگاه سوفای
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/661932" target="_blank">📅 21:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661931">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/811b297717.mp4?token=E2F65jIGk5LGmYsPbldcoabvk_OICXVL3tC9Ms1vsB03_VO2YBWnQ70Ud2S6RfXDASPq_p5tUw690e33mKFzvSW-TJdc3fvp8AXZFN4A0W4GNrTgXYekpKklwcDoP_vr469vnAs2QdwZsTwgtjQsg2f6LGtsJLQifjBlMc7Hhpo6q5qh0ZeTqaJgI4TeI5MZ6tCGOsWH055G1pZq_KOBjyIFN5QVKHe3_C55US6z8Zv3zJP1IjnvtBf3F-3GIz0POopBVM39szt8WzDZSkDhKJ-nikxj7p9Moa254OLv6EByfIhWz9Df64Iqq4uPWGkU-WlkXbF8ZbcDFBPe_C_7PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/811b297717.mp4?token=E2F65jIGk5LGmYsPbldcoabvk_OICXVL3tC9Ms1vsB03_VO2YBWnQ70Ud2S6RfXDASPq_p5tUw690e33mKFzvSW-TJdc3fvp8AXZFN4A0W4GNrTgXYekpKklwcDoP_vr469vnAs2QdwZsTwgtjQsg2f6LGtsJLQifjBlMc7Hhpo6q5qh0ZeTqaJgI4TeI5MZ6tCGOsWH055G1pZq_KOBjyIFN5QVKHe3_C55US6z8Zv3zJP1IjnvtBf3F-3GIz0POopBVM39szt8WzDZSkDhKJ-nikxj7p9Moa254OLv6EByfIhWz9Df64Iqq4uPWGkU-WlkXbF8ZbcDFBPe_C_7PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهار آتش‌سوزی در هتل فردوسی مشهد
🔹
عصر یکشنبه، یک اتاق در طبقه ششم هتل فردوسی واقع در بلوار شهید مدرس مشهد دچار آتش‌سوزی شد.
🔹
بنا بر اعلام سخنگوی آتش‌نشانی، این حادثه هیچ مصدوم یا فوتی نداشته است.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/661931" target="_blank">📅 21:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661930">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
المیادین: هیأت ایرانی تا زمانی که ترامپ عذرخواهی نکند و اسرائیل از جنوب لبنان عقب نشینی کند، به مذاکرات باز نمی‌گردد
🔹
ایرانی‌ها اکنون تنها خواستار توقف تجاوز نیستند، بلکه خواستار خروج (نیروهای اسرائیلی) از جنوب لبنان هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/661930" target="_blank">📅 21:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661929">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افزایش مبلغ کالابرگ در انتظار مصوبه کارگروه
احمد فاطمی، عضو کمیسیون تلفیق بودجه مجلس در
#گفتگو
با خبرفوری:
🔹
با توجه به کاهش ارزش واقعی کالابرگ در اثر تورم، افزایش مبلغ آن مورد موافقت قرار گرفته است.
🔹
به دلیل محدودیت منابع مالی دولت، احتمال افزایش ۳۵ تا ۵۰ درصدی مبلغ یک میلیون تومانی کالابرگ مطرح شده، هرچند برخی معتقدند برای جبران کامل کاهش ارزش، باید ۱۰۰ درصد افزایش یابد.
🔹
زمان اجرای این افزایش هنوز مشخص نیست و اعلام نهایی آن به تأمین منابع مالی و تصویب کارگروه مربوطه بستگی دارد.
@TV_Fori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/661929" target="_blank">📅 21:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661928">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87c6a83a78.mp4?token=VavZrAoXKTKCML9XIudLkgJ_akm7MetEczdxelxx0USAqvz-Gi18TpoRFM8ab5Yk0PTGxsxWfclP7XRdK7E1_ILdok4IgZityxRR6Hs3Bpfa36_Ov8QG3qgKjTQy0JK9VMn1Yd2tpvHtxT8Ma0UW8_MI7hAJBvh0PR5GdVyd77O2XStlqFuRAeu3Y2HemvyK8FidheEhriG5neeKF31AFkHs5NpcZUEPPGfMeojza6Q9clAwV_OEf-uzC1tnzP9pgyfgWAmYTdqYEFGFwRpKbSbAuWsbno9hu7RdvogBkakcsUkSNH9ux_xB8GVxFuSwvdTz4-BI1Zd7dZaUIT_cfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87c6a83a78.mp4?token=VavZrAoXKTKCML9XIudLkgJ_akm7MetEczdxelxx0USAqvz-Gi18TpoRFM8ab5Yk0PTGxsxWfclP7XRdK7E1_ILdok4IgZityxRR6Hs3Bpfa36_Ov8QG3qgKjTQy0JK9VMn1Yd2tpvHtxT8Ma0UW8_MI7hAJBvh0PR5GdVyd77O2XStlqFuRAeu3Y2HemvyK8FidheEhriG5neeKF31AFkHs5NpcZUEPPGfMeojza6Q9clAwV_OEf-uzC1tnzP9pgyfgWAmYTdqYEFGFwRpKbSbAuWsbno9hu7RdvogBkakcsUkSNH9ux_xB8GVxFuSwvdTz4-BI1Zd7dZaUIT_cfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از ورزشگاه سوفای محل دیدار امشب ایران و بلژیک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661928" target="_blank">📅 21:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661927">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
قطر از ادامه مذاکرات ایران و آمریکا استقبال کرد
🔹
محمد بن عبدالرحمن آل ثانی، نخست‌وزیر قطر با استقبال از برگزاری نشست لوسرن و و تداوم مذاکرات میان ایران و آمریکا استقبال کرد.
🔹
او از پاکستان و همه طرف‌هایی که در شکل‌گیری این تفاهم نقش داشتند قدردانی کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661927" target="_blank">📅 21:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661926">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
حزب‌الله لبنان: ایجاد منطقه امنیتی توسط رژیم صهیونیستی در جنوب لبنان را قاطعانه رد می‌کنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661926" target="_blank">📅 21:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661925">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dtepqy4dexHVvyuQGcKFpYpg2HK_M34X0C-a1S0srsNGeq8XYztTPn3RVJ212sH24dLdNZTyjxbdpOORWUdaTeLo4eruBOBj3YKdd7VWJOpa4L3SBk7sHnx-opaSMCI9Aov4k3e1jkNzeFJ2c-O6T64x7Q090AX5HuM3rzNDsK2VANySUUTbTwezxoAfIawHcf5vggD7i_Dd9JZRjoeyYHACmNzGmxy3XXnXNYlFYe8DQ8PdKXQ1PwfCaicOf2qnq2cRjpvsA577nKMLAQWYIGf0JmGQZud4VS0Luc8QlN_CDjpzKOpBhBo1UlL9Zl4sKEnKmEinTvO3-cPsqnWUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🎁
با اولین پیش‌بینی‌ ۵ گیگ اینترنت هدیه بگیر
بعدش با انجام فعالیت‌های مشخص‌شده:
1️⃣
امتیاز جمع کن
2️⃣
توی رتبه‌بندی صعود کن
3️⃣
و شانس برنده شدن جوایز میلیاردی رو به دست بیار
👉
برای کسب امتیاز، راهنمای تصویری رو ببین
👀
هر فعالیت تو رو یه قدم به برد نزدیک‌تر می‌کنه...
📱
ورود به همراه من:
https://www.mci.ir/-4S0XAJB</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661925" target="_blank">📅 21:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661924">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hukHz9ylk1d7i7itHBkiHVjQIEVl9NDN-SV0IklWO17mp_7EnfvYyJfJj_QHgqWHU0_2bsgr2d3pGAqPhFr4D4bXSTe0zjZ7h40G_KxGp9kW0W1RO-9KzrTAe8zI2ikSp8MucbG4BIPLs1M6MRrU-OTYuUfqM7vvd-KXTPptGbXjGjFj2-FsHp-DhV8Qa8NvIFracqz2mIAYn8DdUx9RWtVZnCCHZX7a7ltzU_-WWNHMhkV493HVmw-9qwSmDaQrYcHaikC-Hm5rN0NzBnoD0tnEJsiKFVPoaUZhlP9WtObZFy2sLgIxGFfRAYrh2j5RZo_LtCQ07vtK7aOqGyFYag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تخته فنی جلسه تیم ملی ساعتی پیش از آغاز دیدار ایران برابر بلژیک
🔹
از توسل به حضرت علی اصغر (ع) تا یاد ایران و شهدای مظلومش در میناب.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661924" target="_blank">📅 21:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661923">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaqTmDmdfTQ6J1cDWmCR3kVjYm_k6D_to6kyP5qwNsfo0pca1ys5fhVIOQrZhSGnTLvU0VRCqc8dSZkwyzyOOZzGhEpNCn5qazrpgSncMxcXinygIc3SR6-2k10iJe3d0ywizioE4YcBTDgzw3Svz_j4ozEGdvAU3TKmC0-LNoq4ZAnrYSm0vXbEeChNA9QVpXfBW-lZmBltihno1wfFKpaDCMiCRE0gHMBWWyMK_vQeSmg7BK-sr3IiMfYn7YP4YV6eYyZ5pRz4a0Sa8cps1b2b2MH0rr2TWwJH7j0FJFfKReMRgfK_QOWa9bi4T46xAI9ZmxiWw7oLtPuppWRxiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیب تیم ملی فوتبال ایران برای دیدار با بلژیک
🔹
این بازی امشب ساعت ۲۲:۳۰ در استادیوم سوفای، لس‌آنجلس آمریکا برگزار می‌شود. #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/661923" target="_blank">📅 21:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661922">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
وقوع انفجار در حلب سوریه
🔹
علت انفجار هنوز مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/661922" target="_blank">📅 21:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661921">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ایرنا: هیأت ایران پس از دیدار با هیأت قطری به‌عنوان یکی از طرف‌های میانجی، ساختمان محل مذاکرات را ترک کرده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661921" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661920">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
شبکه ۱۴ اسرائیل: قطر و پاکستان از ترامپ خواستند تا پیامی برای کاهش تنش تنظیم کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661920" target="_blank">📅 21:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661917">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
کانال ۱۲: اسرائیل در حال بررسی «عقب‌نشینی‌های محدود» در لبنان است که شامل خروج از قلعهٔ بوفور (شقیف) نیز می‌شود./انتخاب
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661917" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661916">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
منابع العربیه: هیئت ایرانی به محل اقامت خود بازگشته است، اما مذاکرات برای بازگرداندن آن از طریق کانال‌های واسطه ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661916" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661915">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e72e4364a.mp4?token=GvR-GNR9KJ8m8fPER9_l9SB7fczCi8xeYesP72TvNZiuk1Kb2UfNb7GIV1kYoDnQsPvWJx3pECSR_tChJ0bPZPqxsud7JEIR_zP2_ZIWB818tgyi9DiiHv5dyARRzJHYvaYZSB_oz3ptnkgSB6hPjjGtxcVzg4T1YrcAYOSGifGBgWjNc1ytTKmnVNSBLzp8EMi94GHn5IaVq5t8vj4VHt-cb9f1lj8rza2u6NJ25KZAoM4oIdNV3n91Mx38qpBz09WCPqHnUuY6esM1aTXadBByeidpltrVaUW_grqrYkyT7sfz4JjsqQiKD8bDEqcbQ7lvmjWpoOSfqxO8noIflg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e72e4364a.mp4?token=GvR-GNR9KJ8m8fPER9_l9SB7fczCi8xeYesP72TvNZiuk1Kb2UfNb7GIV1kYoDnQsPvWJx3pECSR_tChJ0bPZPqxsud7JEIR_zP2_ZIWB818tgyi9DiiHv5dyARRzJHYvaYZSB_oz3ptnkgSB6hPjjGtxcVzg4T1YrcAYOSGifGBgWjNc1ytTKmnVNSBLzp8EMi94GHn5IaVq5t8vj4VHt-cb9f1lj8rza2u6NJ25KZAoM4oIdNV3n91Mx38qpBz09WCPqHnUuY6esM1aTXadBByeidpltrVaUW_grqrYkyT7sfz4JjsqQiKD8bDEqcbQ7lvmjWpoOSfqxO8noIflg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای ایران
🔹
در آستانه دومین دیدار تیم ملی فوتبال ایران در جام‌جهانی، مخاطبان با ارسال پیام‌های صوتی پیش‌بینی خود از نتیجه بازی ایران و بلژیک را با ما به اشتراک گذاشتند.
🔸
شما هم پیش‌بینی خود را ارسال کنید و در حمایت از ملی‌پوشان کشورمان همراه شوید
👇
#برای_ایران
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/661915" target="_blank">📅 20:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661914">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8TdUjpM7eunD8aOotZ8MikD6vYbfEuuDfQsO2XPziZpPfTbGft24WJV1n_2x2uzPgzv5MMsy3m7oShhXmuC-5QQM0N2QJpp0UhqdGBEwqXUAg7k4VZ5OjLyfuPL16lLMnjbqcDo_OXSynOs_Fe5Vq-UM5awi6C62jGdVYtKmFgaA2OldV81JbNM7Pq-SLZEHHX9mKrvFz6ojUme56V-NlNs-Me_ZSrAERo0XXrQqPmN_zHwl__feDGNEAP0mwmAZ8yGPbE5zQdoqV6vYCXquEcTWAf4kxdSe2rEIJBqF0Om4T2iCzQfQZVXv_3A5_w4RIUXn7zbIrUy9mDYtHK_eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیب تیم ملی فوتبال ایران برای دیدار با بلژیک
🔹
این بازی امشب ساعت ۲۲:۳۰ در استادیوم سوفای، لس‌آنجلس آمریکا برگزار می‌شود.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661914" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661913">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3LgykSF1h6p5Cm5oo03oLY618bWkSBMFLpd5-xSaKRxDOaErvDtDeqy7Y2OX-F02rP_IZLGhhm5q8LrGHaqfqU9k5hWvQYE5QA4-_g5v7CfzOrSQ_HWwzIfi2QHsQGnU_NeO8AL1jPzxl8bod9Us7lOTAaZpW-BmYAA1DCk85JJv7BA9-acqWkLwrIazwzuJawPS7QoV8BD9y2TKqIZ7CrViHYyphWrZI1zWnTn9QlXLKZshgjmbDq4_wBUwHWr34oFKlP-FvZB4CMZ_GFz66b6x4GnYrnSgcbbM0-1jJPsWvnnhgA6U25I-9ajOYGrMH_RDHUbllIUlnMFt4Tz0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاف عجیب رونالدو در اینستاگرام
🔹
رونالدو در اتفاقی خبرساز، با اکانت اصلی خود زیر پستش نوشت: «تو بهترین بازیکن جام جهانی هستی، حتی اگر تیمت به تو کمکی نمی‌کند.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661913" target="_blank">📅 20:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661912">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/012eab6938.mp4?token=X7Y6xk2eSey2hi-fSIT32ze3iO0g8ft2X6BsYKqfpGV0sl6rOgPIaKC_ZaNkyEKsjnvxwfD4uLmrAsCZB-UOjaMvPF6tEjIdbKLb40K9h13N8vP48z9APxmzkF5ApriJr9UixUZNGQONNpD78TF9Bbt8YJffBWX4NUHDRqkYO64e-GhRtd66RomVW40jVHSXhIDbwZCGRnMfpkFiz-IgJneIpc0WGsXCmpJbRrZ6XcDMVAT1OU1pdMWIcnuM5vsa8sliWJjfnoaV9F4C-ZkxqW4XYp5B1LMDGWzFAE2AqIdNRFoLW_2qyQ5r4N5ZHkVvBD5T7G7TV93sv-1RrG8lxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/012eab6938.mp4?token=X7Y6xk2eSey2hi-fSIT32ze3iO0g8ft2X6BsYKqfpGV0sl6rOgPIaKC_ZaNkyEKsjnvxwfD4uLmrAsCZB-UOjaMvPF6tEjIdbKLb40K9h13N8vP48z9APxmzkF5ApriJr9UixUZNGQONNpD78TF9Bbt8YJffBWX4NUHDRqkYO64e-GhRtd66RomVW40jVHSXhIDbwZCGRnMfpkFiz-IgJneIpc0WGsXCmpJbRrZ6XcDMVAT1OU1pdMWIcnuM5vsa8sliWJjfnoaV9F4C-ZkxqW4XYp5B1LMDGWzFAE2AqIdNRFoLW_2qyQ5r4N5ZHkVvBD5T7G7TV93sv-1RrG8lxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخالفت هیات ایرانی با عکس مشترک در ژنو  یک منبع نزدیک به تیم مذاکره‌کننده:
🔹
هیات ایرانی با برگزاری مراسم دست دادن و عکس مشترک با هیات آمریکایی در آغاز مذاکرات ژنو مخالفت کرد.
🔹
در پی این تصمیم، پخش مستقیم و مراسم عکس لغو شد و نشست بدون حضور هیات ایرانی در…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661912" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661906">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e38b668a.mp4?token=kUdgEu0T48sV4YypnS1plQ3vgaK663B8UU0qF2dQUSkugW4ioh8IfY4nCfoMWHj8PMEKq0PpEyE3IVv0wq6XZ52lrS3J_uk52TXWPAv94LLIfv0XlwsurwjLiJzG46Xrqj0EYJEhkwgI9dBOvS-M6ZezVKwM57sprf6uoQ-otCS9muwhqNZp6kYzs2t9ct5PZbCfIM-uPYWrVPjeUpMAJpgZD1FJzAy2I7T1nYJ26eYjG5etJ2oP73sF8rXiuMmmupE9dyxIUhChaBu5jODs44VOfD8YD-EqhxFB7mJ9uRaoaxicNo5MfbqXU_y1mil1C3B_BlBwJAYtuTtw-ByspZL7nua6BvElccVJreb7vttVvRsfH7_QEjidxRzrSThOrz7GOsaBYbDyj5QCdUJ8WBvxsDkjRY8tzEC_Z7NRy0bCLDaFrV-HxJMuluYc9OXXbTB93yUSOIs10Ac2w5F_qIO79kqhujKDhglASa6NwXf4IqVTglpzF-3ic1evPH8EJwnmN0ByGVZm0V54JB80749iZlo2kQ6DFixmvMR99QpnOKn2r4uQ0UeIZxjQlasW3klsjcShTiv_BIa2I-NZFfuTjkUTkueLs_m3n6jcHt7DRU31cKkKUjkcTwQlaOHDz6FkZMQuVUJ8LN5chOM424OTIbQrwVjYUeafPaN5oc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e38b668a.mp4?token=kUdgEu0T48sV4YypnS1plQ3vgaK663B8UU0qF2dQUSkugW4ioh8IfY4nCfoMWHj8PMEKq0PpEyE3IVv0wq6XZ52lrS3J_uk52TXWPAv94LLIfv0XlwsurwjLiJzG46Xrqj0EYJEhkwgI9dBOvS-M6ZezVKwM57sprf6uoQ-otCS9muwhqNZp6kYzs2t9ct5PZbCfIM-uPYWrVPjeUpMAJpgZD1FJzAy2I7T1nYJ26eYjG5etJ2oP73sF8rXiuMmmupE9dyxIUhChaBu5jODs44VOfD8YD-EqhxFB7mJ9uRaoaxicNo5MfbqXU_y1mil1C3B_BlBwJAYtuTtw-ByspZL7nua6BvElccVJreb7vttVvRsfH7_QEjidxRzrSThOrz7GOsaBYbDyj5QCdUJ8WBvxsDkjRY8tzEC_Z7NRy0bCLDaFrV-HxJMuluYc9OXXbTB93yUSOIs10Ac2w5F_qIO79kqhujKDhglASa6NwXf4IqVTglpzF-3ic1evPH8EJwnmN0ByGVZm0V54JB80749iZlo2kQ6DFixmvMR99QpnOKn2r4uQ0UeIZxjQlasW3klsjcShTiv_BIa2I-NZFfuTjkUTkueLs_m3n6jcHt7DRU31cKkKUjkcTwQlaOHDz6FkZMQuVUJ8LN5chOM424OTIbQrwVjYUeafPaN5oc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
کلیپ های شب هفتم محرم حضرت علی اصغر (ع)
🥀
عمه بی‌تاب شد از گریه تو گریه نکن
دل سنگ آب شد از گریه تو گریه نکن
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/661906" target="_blank">📅 20:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661905">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0731c4b28.mp4?token=a-4cOLXqZiU7AR552QLSVwdWXnSTjaI4iZ16-2RleM1nOm7DRjhPeiKl4WZdfu2H_xlKWoGkT0CvT4PEEsBCuiVq54qENMLcqEVhPtXr1fdS_SzpgWkVHb0oqDB1f_NjxahTMqCtKVK5Z659Wy_g-o1QbV5YZXX4Tk3VCIKLSnRdk-VtMX9zmRypRWK_kU13agL7dsp0f9RxHNfuj47D_vYOaYeUtnYZPMNINjnsuzVVytBQ8ewYSQQxWbIzhjERseiPf3glsS-9q7nmzWOb8eCMhOB5wUfqNwJ1HbVJloWp9Mx5hfysiIhXZBhggoH65O0MRKfYQ2WzA7rhcQz5cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0731c4b28.mp4?token=a-4cOLXqZiU7AR552QLSVwdWXnSTjaI4iZ16-2RleM1nOm7DRjhPeiKl4WZdfu2H_xlKWoGkT0CvT4PEEsBCuiVq54qENMLcqEVhPtXr1fdS_SzpgWkVHb0oqDB1f_NjxahTMqCtKVK5Z659Wy_g-o1QbV5YZXX4Tk3VCIKLSnRdk-VtMX9zmRypRWK_kU13agL7dsp0f9RxHNfuj47D_vYOaYeUtnYZPMNINjnsuzVVytBQ8ewYSQQxWbIzhjERseiPf3glsS-9q7nmzWOb8eCMhOB5wUfqNwJ1HbVJloWp9Mx5hfysiIhXZBhggoH65O0MRKfYQ2WzA7rhcQz5cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل چهارم اسپانیا به عربستان توسط حسن محمد التمبکتی ( گل به خودی ۴۹)
⬛️
🇪🇸
4️⃣
🏆
0️⃣
🇸🇦
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/661905" target="_blank">📅 20:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661904">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/005e3db47d.mp4?token=frDAM8lHw_mWeFKvE-8gQHbuKqMg4q3GdNpprzn1y-vLWVL_tvi5fH-J0ffTTS1v_qKtYgNdljgSUIOQhEcoW-ux6eSCL3jfUYyKIoNsxUStQBahsTE32OclbvgyE9xaSAQc1oAXNshPO_OiXs5KuMtG3b24aK1XuwAjojhFA00pABTPo1zN-OiNB2lywefDzuiKd9H_Qr1Zu3gGhURLPd-_Y9UBf0YSwEhInYoKnBcZAYj-7MRvP1gCOnsrDGNFETZSGODsuZuZzun9XIvLiaGNKNHp2mvpNjZfbNBaBIMD2vGCKHoQHOg5qIQce_9Yqf89Vfw4V6d5UtKatwCQbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/005e3db47d.mp4?token=frDAM8lHw_mWeFKvE-8gQHbuKqMg4q3GdNpprzn1y-vLWVL_tvi5fH-J0ffTTS1v_qKtYgNdljgSUIOQhEcoW-ux6eSCL3jfUYyKIoNsxUStQBahsTE32OclbvgyE9xaSAQc1oAXNshPO_OiXs5KuMtG3b24aK1XuwAjojhFA00pABTPo1zN-OiNB2lywefDzuiKd9H_Qr1Zu3gGhURLPd-_Y9UBf0YSwEhInYoKnBcZAYj-7MRvP1gCOnsrDGNFETZSGODsuZuZzun9XIvLiaGNKNHp2mvpNjZfbNBaBIMD2vGCKHoQHOg5qIQce_9Yqf89Vfw4V6d5UtKatwCQbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🔥
قهرمان فرالیگ شو
🏆
همزمان با جام جهانی ۲۰۲۶ وقتشه خودت رو به چالش بکشی!
⚽️
در مسابقه «فرالیگ» نئوبانک فرارفاه، نتایج مسابقات جام جهانی را پیش‌بینی کن، امتیاز بگیر و برای کسب جوایز نقدی روزانه و جوایز ویژه پایان دوره رقابت کن.
🎁
جوایز روزانه:
▫️
نفر اول: ۲۰۰ میلیون ریال
▫️
نفر دوم: ۱۵۰ میلیون ریال
▫️
نفر سوم: ۱۰۰ میلیون ریال
▫️
نفرات چهارم تا شصت‌وششم: هر نفر ۱۰ میلیون ریال
🏆
جوایز ویژه پایان دوره:
▫️
نفر اول: ۲ میلیارد ریال
▫️
نفر دوم: ۱ میلیارد ریال
▫️
نفر سوم: ۵۰۰ میلیون ریال
✨
هیجان جام جهانی را این بار در فرارفاه تجربه کن.
📲
همین حالا وارد
نئوبانک فرارفاه
شو و به جمع قهرمانان فرالیگ بپیوند.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/661904" target="_blank">📅 20:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661903">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAb_DlFMt8Iv9azAGgjkHWRD6hZCj8PsKpxUTXHrYPkJ3juP_LMReYnA1BTJDe6Q0y2f--pMo450LcmeInjvgyPUBxMda3NBlPaSSyuCK6WYBQQujH93ygMeCZTN3lBryfqQIaw2LXM6S7hx1TpjYI8UyA3rIocXmXJlceDVTdJqMqKtyw7a8BBXQVtJM9Bg5uqkAs8_rN9Lt__83QrjuxOPRUxq9WEhcw2PJDkZ_gP6QFkCBqMO-YaQ76Sz2beOEYg0Of7ta75_dgAeaqKdkXPrcWzsn3ngGX7SDYhiVE9RzKCkDvtbZycayMpRkRmhiDKb47Qb2v8IbzWbfQNe0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
خبرنگار اکسیوس: یک دیپلمات حاضر در مذاکرات سوئیس ادعا می‌کند که هیئت ایرانی محل مذاکره را ترک نکرده و مذاکرات بین ایالات متحده و ایران همچنان ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/661903" target="_blank">📅 20:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661902">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
بقائی: نشست سوئیس بر اجرای تعهدات طرف مقابل متمرکز است
سخنگوی وزارت امور خارجه:
🔹
نشست امروز در سوئیس برای پیگیری اجرای مفاد یادداشت تفاهم ۲۸ خرداد ۱۴۰۵ برگزار شده است.
🔹
وی تأکید کرد آغاز مذاکرات توافق نهایی منوط به اجرای بندهایی از جمله پایان جنگ در همه جبهه‌ها، صادرات نفت ایران و آزادسازی دارایی‌های مسدودشده است و بدون اجرای این تعهدات، ورود به مرحله مذاکره نهایی ممکن نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/661902" target="_blank">📅 20:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661901">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
روایت تکان‌دهنده یک تجربه نزدیک به مرگ؛ از بی‌اعتقادی تا بازگشت به زندگی
🔹
00:04:15 شاکی بودن از خداوند در تمام طول زندگی
🔹
00:08:20 عشق ورزیدن به امام حسین(ع) در عین بی‌اعتقادی به خداوند
🔹
00:14:00 سختی بی‌اندازه جان دادن از بین دندان‌ها
🔹
00:29:20 آرزوی خاک بودن تمامی سلول‌های بدنم در حال سوختن
🔹
00:36:50 ناچیز بودن آتش این دنیا در مقابل آتش جهنم
🔹
00:46:10  شفاعت حضرت زهرا(ص) برای اشک‌هایم بر امام حسین(ع)
🔹
00:59:20 توصیه تجربه‌گر به انسان‌ها براساس تجربه نزدیک به مرگش
🔹
قسمت بیست‌ویکم (خاک و خاکستر)، فصل چهارم
🔹
#تجربه‌گر
: باقر حسین‌زاده
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/661901" target="_blank">📅 20:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661900">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
یک منبع نزدیک به تیم مذاکره‌کننده: هیئت مذاکره‌کننده ایرانی در اعتراض به تهدیدات ترامپ محل مذاکره را ترک کرد/ تسنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/661900" target="_blank">📅 20:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661899">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
تشییع بقایای شهدای مدرسه «شجره طیبه» میناب ۹ تیر برگزار می‌شود
معاون سیاسی استانداری هرمزگان:
🔹
بقایای تفحص‌شده شهدای مدرسه شجره طیبه میناب روز سه شنبه ۹ تیرماه ۱۴۰۵ تشییع می‌شود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/661899" target="_blank">📅 20:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661898">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
پزشکیان: تقویت معیشت مردم اولویت دولت است
رئیس‌جمهور در جلسه هیئت دولت:
🔹
تقویت معیشت مردم و امنیت اقتصادی کشور مهم‌ترین اولویت دولت است و باید توجه ویژه‌ای به وضعیت معیشتی جامعه و افزایش مبلغ کالابرگ شود.
🔹
وی همچنین با اشاره به تلاش دشمنان برای تأثیرگذاری بر روند مذاکرات تأکید کرد وحدت و همدلی در کشور شکل گرفته و با هوشیاری مردم، این توطئه‌ها بی‌اثر خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/661898" target="_blank">📅 20:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661897">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e1e49a53.mp4?token=Qu21mbmrjJ77qyLA8an7ORZAvdw5q4yHMiiyps1K3_HNIljW4Rmg4jNKyo702yAsNZjv6dceCBO1aKUp28DuwuuKYYRyFxabIqe-RXiTaT_xT6m12bjbbwgMKYacWpb49FymfM7Q9HBzvF-etw50gOLRIqnILJnasjST8cHhM29EP596Fu2oFOuVJLeYfs4Wny5rqEkUotVx1j6tO7cy2ftft-RmC1N5kb7vp5STh6q8SCXu6FwbUxW1K8PtKLlRqRWX83bHvdaNWKdYUIKuVOWAxhAhfX6AG3kbTParfcyFlgRSnfWWqeyMnqNOuyizXqBgmv9efUTTUudA9-lIaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e1e49a53.mp4?token=Qu21mbmrjJ77qyLA8an7ORZAvdw5q4yHMiiyps1K3_HNIljW4Rmg4jNKyo702yAsNZjv6dceCBO1aKUp28DuwuuKYYRyFxabIqe-RXiTaT_xT6m12bjbbwgMKYacWpb49FymfM7Q9HBzvF-etw50gOLRIqnILJnasjST8cHhM29EP596Fu2oFOuVJLeYfs4Wny5rqEkUotVx1j6tO7cy2ftft-RmC1N5kb7vp5STh6q8SCXu6FwbUxW1K8PtKLlRqRWX83bHvdaNWKdYUIKuVOWAxhAhfX6AG3kbTParfcyFlgRSnfWWqeyMnqNOuyizXqBgmv9efUTTUudA9-lIaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قربان‌زاده، از اعضای همراه تیم مذاکره کننده: اگر خاتمه جنگ در لبنان حاصل نشود مذاکرات ادامه پیدا نمی‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/661897" target="_blank">📅 20:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uGFeNgx4xGWzwmWYNxe1qnH8h8-YktzxGPHpJmXpUGurmwAArnl4TvOB8-WsbWtVUY0vM-taWsTcED4bRPpn86mUpyczIKSNLmtHuGiAeBlvnvSeyz-B3bjnMt7nTf_-rY9sZTliGYeSsb8TqSQ2k5HvWjM3YJhl_WykxyVjneRIqMhZ-8DK-zVtI1Zo0I9scI8_YBrEL4gZlgGNkkTLi4KBFGvspw8hOny3QHWKi3TpYFpsUpAa04ItmJ3JrL668PEbdTrepkWWH99YlswOj1zWY37BRpc5gvPyodh0EVrr1CqZSIUO8CUFEomzUELgngT4Ugn_NPGZ-7MQ0alLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dovkrVENBIZhaCLl-t1tgylRgzRDrt4yO2LA-r-918w1fXrz__0lt3uGaATakS4jA2V3y0YgIu2GIMpNlDUuK9yrVFYb1zI0P2ZuG606CDLp-me3gxKzPYSN9SdRWZ7v_-pJU8dGp9L-MCPEMSkpDdGLjCSXs0nLHlJ_h2fXBhudaGHJ-wdwOUsukQytjv_Xh_U3lx_7Kdj_WbWuaYfjn-Av8wabE7sRaE-HN9eHEWDTcILgURz14IoFMSO7tsPVN9laFYV9NtQcni6MKSA1dT6eUrh8noOcrQfOYo8SMEG-KEwOo0B-aKA-3lYc54xNMtuiSJTcQfuv2gg78GQHcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر دختر نوجوانتان می‌گوید «هیچ‌کس من را نمی‌فهمد» این کتاب را به او هدیه دهید
🔹
احساسات دخترانه فقط یک کتاب نیست؛ دوست صمیمی برای روزهایی است که نمی‌دانی دقیقا چه احساسی داری.
با تمرین‌ها و پرسش‌های جذاب به دختران کمک می‌کند احساساتشان را بهتر بشناسند، درباره‌شان حرف بزنند و با اعتمادبه‌نفس بیشتری با چالش‌های زندگی روبه‌رو شوند.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/661894" target="_blank">📅 20:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661893">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
یک منبع آگاه: تهدید ترامپ مذاکرات سوئیس را متوقف کرد و ادامه آن را در هاله‌ای از ابهام فرو برد/ فارس
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/661893" target="_blank">📅 19:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661892">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e1d1264f.mp4?token=inovEzCN65UZrkccjZoAAtfibfeqkbpQMggP7Jvoi8rUluBpggnyXyqTM0mf7OF5XE_iLoLSxc2t-MR_5Pd47uLHv7yTENqB30hX-h7CWgOOyOqhOhN3wBbwQe_2jG38YLg916I-301twlwPs5-Zkhm4APbhvHOATp8LNrK3eQSt--IqI3-FcDK6bLXQis-aO_DogsuOi_RJlvuilVqCYz4dmqgDaw74HSyq4bwUfHUmWjIBlm5EqitNkHr8e6bzX7Q8e4E-fQ40ipUVMrKa57bxRFu3NfBlH78o4LnrzBG4cDlEzt8Ff9gfp7ypDwfZ5QyWjB3KpjmEp2TtglJzXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e1d1264f.mp4?token=inovEzCN65UZrkccjZoAAtfibfeqkbpQMggP7Jvoi8rUluBpggnyXyqTM0mf7OF5XE_iLoLSxc2t-MR_5Pd47uLHv7yTENqB30hX-h7CWgOOyOqhOhN3wBbwQe_2jG38YLg916I-301twlwPs5-Zkhm4APbhvHOATp8LNrK3eQSt--IqI3-FcDK6bLXQis-aO_DogsuOi_RJlvuilVqCYz4dmqgDaw74HSyq4bwUfHUmWjIBlm5EqitNkHr8e6bzX7Q8e4E-fQ40ipUVMrKa57bxRFu3NfBlH78o4LnrzBG4cDlEzt8Ff9gfp7ypDwfZ5QyWjB3KpjmEp2TtglJzXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم اسپانیا به عربستان توسط میکل اویارزابال
⬛️
🇪🇸
3️⃣
🏆
0️⃣
🇸🇦
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/661892" target="_blank">📅 19:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661891">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b5b33a66.mp4?token=J2-E2tZvnUeXFeWTDszEHQUTzuQ5DU3yw1Sbhx8yX7H2GQYm0QLFlRiDTUiPiROioWB5lvSvDUjhhC4Ug_Ic14b7M0yAXCzJ1KKg-FV11RoRRwbfUySX-rUk9_IS71r6Wes5Ij2JT45SU6byimDw9apG3MysjZSXE0Ip0Rj9hSJKolUYvoxFzlT4UimjVqTLzyGwEQweuwBWrnSbeoLd-kHm-3naoNN5eRAOO_4YQNZugIoXtkSupBwdEOLbGi70O4fBFH-bD-GSdrfe32uzMHknJXW0mu1ATVUv2d9d-9-fdunG24ZGgvXOPSAXSfU5AivFadOY4yddoDSkpAtMhYMzlgDNjSx5hwQHnwn39w-SysPN25BvdkkAO6ONuvWRuX3Hr2D0uETsgUWbfi4Ns0cE0JN5WuIjWi5Xko4RAHU-O1lNDwoQ70bveohEFrYFcwzZxS2KXtmUVIKG3xEu39ZGddVP250ksej4X_OqnQYIK8kolqQhvqMmJrUdnoJHY544Siv_bcL3t0VCl_dRkCLywgkcnUjqizdcjGWT2dROgY3f7-m-30ZW6x6Xbk6aeUrTr3eC_jpfqNZdSsEQsNUlj1Lm7IQ8u4Zn4Z6YDD4XRlyRwFnDCmc69E3kjTtgF0UupH3_I_3FS22Y5Vo8BAKVC4fF9PU_Gh-zWBOG898" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b5b33a66.mp4?token=J2-E2tZvnUeXFeWTDszEHQUTzuQ5DU3yw1Sbhx8yX7H2GQYm0QLFlRiDTUiPiROioWB5lvSvDUjhhC4Ug_Ic14b7M0yAXCzJ1KKg-FV11RoRRwbfUySX-rUk9_IS71r6Wes5Ij2JT45SU6byimDw9apG3MysjZSXE0Ip0Rj9hSJKolUYvoxFzlT4UimjVqTLzyGwEQweuwBWrnSbeoLd-kHm-3naoNN5eRAOO_4YQNZugIoXtkSupBwdEOLbGi70O4fBFH-bD-GSdrfe32uzMHknJXW0mu1ATVUv2d9d-9-fdunG24ZGgvXOPSAXSfU5AivFadOY4yddoDSkpAtMhYMzlgDNjSx5hwQHnwn39w-SysPN25BvdkkAO6ONuvWRuX3Hr2D0uETsgUWbfi4Ns0cE0JN5WuIjWi5Xko4RAHU-O1lNDwoQ70bveohEFrYFcwzZxS2KXtmUVIKG3xEu39ZGddVP250ksej4X_OqnQYIK8kolqQhvqMmJrUdnoJHY544Siv_bcL3t0VCl_dRkCLywgkcnUjqizdcjGWT2dROgY3f7-m-30ZW6x6Xbk6aeUrTr3eC_jpfqNZdSsEQsNUlj1Lm7IQ8u4Zn4Z6YDD4XRlyRwFnDCmc69E3kjTtgF0UupH3_I_3FS22Y5Vo8BAKVC4fF9PU_Gh-zWBOG898" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
⚽️
پاس گلِ مردم ایران برای تیم ملی
به امید درخشش و پیروزی یوزهای ایرانی در جام جهانی
🐆
💙
#همراهتیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/661891" target="_blank">📅 19:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661890">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced4c2682d.mp4?token=SiaGPOYLd3BBmB6aAUDBkUvEjfdh8_WuhQ-yh8qE8NWeJP8bXqzl7aUCowYBMwOK82Dp2Z0dxizhQcIkbLqNwOVdCbVu1aZhQHxkncJn6RIqTDwX_3kBKZm0L2MMTbA556cDL3uW1Pzk1ApdTx26k6K9q86lTpTLfRnBMdR5zz9OZZxu8UeSWeV_LKrJODEaAonLh9dgreMJUtylZPbfIP38nyvFYChtimI8VN0SnRptcvHjo_UHpfr1UuG19XJ_VYHLWIKcIDjqHM6ysnZbsPptJOjkOAGcwNf7QJcxQWjNCzy-TrL9FWyJkg6Z13caeor-KGbcbGLLIRurRp8lyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced4c2682d.mp4?token=SiaGPOYLd3BBmB6aAUDBkUvEjfdh8_WuhQ-yh8qE8NWeJP8bXqzl7aUCowYBMwOK82Dp2Z0dxizhQcIkbLqNwOVdCbVu1aZhQHxkncJn6RIqTDwX_3kBKZm0L2MMTbA556cDL3uW1Pzk1ApdTx26k6K9q86lTpTLfRnBMdR5zz9OZZxu8UeSWeV_LKrJODEaAonLh9dgreMJUtylZPbfIP38nyvFYChtimI8VN0SnRptcvHjo_UHpfr1UuG19XJ_VYHLWIKcIDjqHM6ysnZbsPptJOjkOAGcwNf7QJcxQWjNCzy-TrL9FWyJkg6Z13caeor-KGbcbGLLIRurRp8lyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم اسپانیا به عربستان توسط میکل اویارزابال
⬛️
🇪🇸
2️⃣
🏆
0️⃣
🇸🇦
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/661890" target="_blank">📅 19:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661889">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78513744fe.mp4?token=pyz0-iBQO-lcO5jF3T29bdNMcjEVK1qaNCnX6CSoYDmgwvnoua6bdEEDa5EAJj4bVYFunp-qJhb_Caa6I4y5pyD_0xyRU41BjhEa77283fTeluks-Ph9JtTOLZE_cEX93vQJey2yifBA2QCv8DTDx2PekNy_UFQpy4Hg9uf6brDhS2A3LM8y9Fffn-xGQKNUan9xQzK2MhFGhsWfp96SyBVI9LMwdhcvE_G9c8pgXh9sx7SY4EbaoJttGbdEQMDze7f0rvwy-LmbJ_ExM7VLHH1rfmDVCQKwaT_1j9-2CPUMv4gYWcCeHcTRx5_b3ZZTxCOh2Hdwwbt5bIh2tNboxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78513744fe.mp4?token=pyz0-iBQO-lcO5jF3T29bdNMcjEVK1qaNCnX6CSoYDmgwvnoua6bdEEDa5EAJj4bVYFunp-qJhb_Caa6I4y5pyD_0xyRU41BjhEa77283fTeluks-Ph9JtTOLZE_cEX93vQJey2yifBA2QCv8DTDx2PekNy_UFQpy4Hg9uf6brDhS2A3LM8y9Fffn-xGQKNUan9xQzK2MhFGhsWfp96SyBVI9LMwdhcvE_G9c8pgXh9sx7SY4EbaoJttGbdEQMDze7f0rvwy-LmbJ_ExM7VLHH1rfmDVCQKwaT_1j9-2CPUMv4gYWcCeHcTRx5_b3ZZTxCOh2Hdwwbt5bIh2tNboxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیخ نعیم قاسم: دولت لبنان باید از مذاکرات هیئت ایرانی درس بگیرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/661889" target="_blank">📅 19:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661888">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b44562b5c4.mp4?token=dJXONuQCIuE65r2mvwNR-hZSleLfuGC3d2oEBHS0NhKl3xBgvBy-jeR6bA7JMm2VFeG6zdQYUs-L9144IWkABauo-UG3wToQjHtxbmJz8M5cj1Gg_lW9yJzx1uLcUM5C5SUf0PfCSHKSRBWax7CHqa8mMi4geBIu2txKXyznleMZJUSC9-MxDyDuaQq9wmXmgREzfBCBuVQFEDA4ia5Tx-po2FSiUqcfN5HopiDPD6176vzjDnHIsfz8O1mCVBEWIiFRL5TyDIpcEzNJyqvZBnQzL2ZTdimsHNWnyb6Zk8nuaw5PSfmXlHWqglzZTBvT6K7CdIGxImRNCKjf5vTxMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b44562b5c4.mp4?token=dJXONuQCIuE65r2mvwNR-hZSleLfuGC3d2oEBHS0NhKl3xBgvBy-jeR6bA7JMm2VFeG6zdQYUs-L9144IWkABauo-UG3wToQjHtxbmJz8M5cj1Gg_lW9yJzx1uLcUM5C5SUf0PfCSHKSRBWax7CHqa8mMi4geBIu2txKXyznleMZJUSC9-MxDyDuaQq9wmXmgREzfBCBuVQFEDA4ia5Tx-po2FSiUqcfN5HopiDPD6176vzjDnHIsfz8O1mCVBEWIiFRL5TyDIpcEzNJyqvZBnQzL2ZTdimsHNWnyb6Zk8nuaw5PSfmXlHWqglzZTBvT6K7CdIGxImRNCKjf5vTxMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهدای میناب هوش مصنوعی نیستند!
🔹
خبرنگار خبرفوری خطاب به تیم های ایران در مذاکرات و جام‌‌جهانی
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/661888" target="_blank">📅 19:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661887">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
امتحانات دانشجویان ارشد و دکتری دانشگاه آزاد حضوری شد
دانشگاه آزاد:
🔹
امتحانات دانشجویان مقاطع دکتری و کارشناسی ارشد طبق روال عادی به صورت حضوری برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/661887" target="_blank">📅 19:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661886">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
قالیباف: تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم؛ آماده پاسخ هستیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/661886" target="_blank">📅 19:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661885">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ماجرای شهادت حضرت‌ علی اصغر(ع) به روایت رهبر شهید انقلاب‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/661885" target="_blank">📅 19:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661884">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QirP5eec-7BUY3Y_upNdoY7tdhaVVQTTTbuUO-edw-k2KWRiNSSwcQY8W6re93XgjHxdQtnkzJNMbVv4d0SvprnRwI0EFv0-WrCD7nwYJt7-kSKY9vNNe1phbp6xCA76CpdYG_qRg9J_zM-1gLdFe66LdCLigMa_wve9SCJA2RePMvym7T185OeZTFVneq27Ilj1T7ysoFxVDKL7_ysERE9VGL1xJ5rwMT9J7aLlmRozI82lvBEkaNwCWYQv3p5848Peb3OMapwltsi2Y5kngF7hzuKvrgxtmkIsoU0YZQzzmA6va0Hhi6Cd52ChTbB47bKh0UY22MDh-Vj50dkwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم؛ آماده پاسخ هستیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/661884" target="_blank">📅 19:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661883">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb59e01f5e.mp4?token=KKNsS8YjLTfsFnDiiHJb_A_ws-GUKjVVkM8JVnGVmMRUIJCbfAolLfF8NdupV6E5Ld3-hlsmcUG5QT_mymIq01ycD9evse3kiIAKQJ4plHuuodUH3w1KEHRG1qR7_PzQ2CZ5ACMp-p7r53emaNIeqigv3owgrDbCruGBh68PAEEVeKBbyCsCOgmdjQkTdSMpzumIH5suhhFRVRiMarbnIPEGJCFMt9H6fN2FWRjXpFi6I5gWVMEOEcL0JfCANeAiuS2u8PPsbRxEWcxo-d5fqp1Uy8y3z1zPHYk4OaLNggOH5bWFzccSpQFmWh0KMdKW6kvfVCivCXSXZzxhHi8w5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb59e01f5e.mp4?token=KKNsS8YjLTfsFnDiiHJb_A_ws-GUKjVVkM8JVnGVmMRUIJCbfAolLfF8NdupV6E5Ld3-hlsmcUG5QT_mymIq01ycD9evse3kiIAKQJ4plHuuodUH3w1KEHRG1qR7_PzQ2CZ5ACMp-p7r53emaNIeqigv3owgrDbCruGBh68PAEEVeKBbyCsCOgmdjQkTdSMpzumIH5suhhFRVRiMarbnIPEGJCFMt9H6fN2FWRjXpFi6I5gWVMEOEcL0JfCANeAiuS2u8PPsbRxEWcxo-d5fqp1Uy8y3z1zPHYk4OaLNggOH5bWFzccSpQFmWh0KMdKW6kvfVCivCXSXZzxhHi8w5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول اسپانیا به عربستان توسط یامال
⬛️
🇪🇸
1️⃣
🏆
0️⃣
🇸🇦
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/661883" target="_blank">📅 19:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661882">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPTkt1xSycD5VaZTpHf1i0pq7LM_T7pZ9V77RTxvRDkStRNKXrqxrGWnXDPLsq_xUm_T8JIisqpVgEhlK5UBowf_LlM0z6Wv-TE5gItd2onLVgDafvonC4wSJYDN73gcw02QeuvDbpng7VTsKEKl9UBlZ-qJKtmnDe8plxFB4YNEftkhRkjwlRNnA_qMFNxaPDximBxZut3BTvDjMgIoXDDjKP9ml9McJeaBnLBhnDxYNI-d3Pq-AUYrKDOSR0mqxrAGebIQHgNbEcpOAEMJyQ8nVU7SbPSj_stdaoAAurpAcfi4sgDea-JlY3Ddh_z2gTCqqjG72Y7UHNuCyuOdHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/661882" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661878">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tD2qhXKyo51krI2URK55DyjhXJM1MS4dCL7qGqO7SH3hS7gY0aaURz2ji7eDMl2J4RDhLMRYlGroXLr6jyIuJxIJXFOSSB2cGGwlDWb7Xexrk01tL4Kh6X_-SgCvTYbMfqQ2fSkwDz4P2K_ZYr52pLyet9KTF2TPSOvKkiUEZKlfXNk0oo8tXFYsAyBgIbepkOQmVw8n2rtGKJnBiduq0leZYANv9D3lTRg4bg9hRud0Ge6YRW17H3XK03rt57oV74VEVtwJeQM1bSwVE2PsDPXyJTtIwQfoQniHV38CWHWLitjaze0V22a5jFMcwtougPkJLUelFRx-0n0ckAm5Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u-3lrfXJs61cPoShTXO2fgKARg2tQORzQLj1BvLf1PQ8iOhqSsZ6m8bLmDBiLkOIUZ3Xm46KQlum7Oe-WI2rgHqAlJWzbChrjwdGX_u-IQgmNLfppSqiOpiBUtYffBn6VYQDK1X-g6PeaXndlrRmASdqEt9Wer3jdAdwJfnfIPFTB5ZFtXX_dt3cKtgZ9ne6DTGR-1SRL56tjsY_VLnZ5g_7g1QESibtwl4TfNzWXlAE1bqyejPRgHVlxNsGggMfsQ6lNJYgmd3PRJZWX3U98qsmQQm3-lLya0To0pfpTyERhJQ8wA8ykZkQPZs_1R_r04UsFnMp9C8pl42CjA4meQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3akP-Zgs_KrVYh5CW9B0COvZDLzGBaNdGkiWpBNkFM8iemWWVAqD2UBYT4p7rfu-c7eG3w1ZotO-5U1acSa6xLTO_p6OFOuRUoZb87bnX8tSeyybvxOdFDuoH5OpXAI8ClPqSopPgDJ3oXC2AhwCcziP4VK8Ptq84iKjfnpMbc7vFTqYW8lez6cT9MO3FHkGQppOo38wPFj_Tx4vzpl4VQLXaGEoIVkSUfGoaMNy10pwuFgz5NP7bq8WYDNX-XeGNoemdXFSNxYIeZgmENdk0_kkFnR9WzQatkBEjGVH8pbpJf53e0gIdBME6V5s7bkqfLAVY0ACi8LzqNUv856dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BR5pM9_Fdz1PknabaxxrWXJ0oZ_nCnE16pBlkWQzgsFc5z7axWFo6LdJG7s2vdBe24DhEuhLbntjoGDj4giH1rZHaBm4M2_5A_u8uiWQdXPDPhwDpmaBIvRno-QtFA90W2z6LF_bQ7LTp0Qp7IdI-7rXcjxjG5cd8PnQsvMVuIiyYC05-XnUbsIpHGRxPDDRle_e8fBUazVjVCFZpkrcZQm5aPeRJKRL_OUJ0Rv14gir2KN9dXaaD_q7qI7iBCncX-df7bOsd9-yH1hJGlEJsqY3bItVNWUY_OIcUEWOCzdUEcCG9tHWo5I5Z6F9DaL6wdBg_1EdoQtqmOmigAZq5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نشست چهارجانبۀ سوئیس پس از ۸۰ دقیقه گفتگو جهت مشورت‌های داخلی متوقف شد/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/661878" target="_blank">📅 19:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661877">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
عبور ۲۵ میلیون بشکه نفت در یک هفته
مدیر عامل شرکت ملی نفت:
🔹
از دوشنبه هفته گذشته، کشتی‌هایمان از خط فرضی محاصره، با ۲۵ میلیون بشکه نفت عبور کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/661877" target="_blank">📅 19:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661875">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a76c193639.mp4?token=mqVZ0mFpOVhdB7HNr8h7qW_V9e_PQFbVos-CfPNzgFRvkp5gxyPlEGeQRF5EmxPMUkHh8jQp1oB_WjqorISKT-Neakg5FMfhLnxD5IvPeYXKVoaTM2JhUaYkWb_hK8ZyKoLuXfgPdJCmZhYo128_nlkCuyOpXK34oF-qcq_SrAIB7uZEbuWKrthZK4DFQBkjX27soGOhuDmLwv9nluPVLKprzkNYLR9QexToD1xEwcqngabZA8qEqnuqpfy1Wnrs0ac4KI9n7XAk1rvelTqHTFPYVc_S6obZ4EMY1WYBWYPzTf_XRV8W6NqO57sTPd9RRuvsvvegpaAyV9lwZoGCnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a76c193639.mp4?token=mqVZ0mFpOVhdB7HNr8h7qW_V9e_PQFbVos-CfPNzgFRvkp5gxyPlEGeQRF5EmxPMUkHh8jQp1oB_WjqorISKT-Neakg5FMfhLnxD5IvPeYXKVoaTM2JhUaYkWb_hK8ZyKoLuXfgPdJCmZhYo128_nlkCuyOpXK34oF-qcq_SrAIB7uZEbuWKrthZK4DFQBkjX27soGOhuDmLwv9nluPVLKprzkNYLR9QexToD1xEwcqngabZA8qEqnuqpfy1Wnrs0ac4KI9n7XAk1rvelTqHTFPYVc_S6obZ4EMY1WYBWYPzTf_XRV8W6NqO57sTPd9RRuvsvvegpaAyV9lwZoGCnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران آتشفشان فوئگو در گواتمالا
🔹
فوئگو یکی از فعال‌ترین آتشفشان‌های آمریکای مرکزی است که از سال ۲۰۰۲ به‌طور مداوم فعال بوده و در ژوئن نرخ انفجارهای آن بین دو تا چهار مورد در ساعت ثبت شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/661875" target="_blank">📅 19:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661874">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f8c95159.mp4?token=aspQacoe8eBE-2ztwEUhbOwF4vMbE_ePv4ZdnpuI8VZL4Rp-eX1zBvbnmTgItuVD2r0ihR6FATUBLqs0PJHECP_gwXj1LAEtW8lQuaFNQdxVcXkX6DHLBBZSTtnztKnZQeuxzGOWpwlNr4JD75Rg3bfIn6t3qHWKScG6tPdfpPamBwYDHrBlL0KTarGQ8-QvN90kuQRRTGV5H_0C-WXHlpcguo_YKWZlKUv-ZpuFFSka3lJRPpRJLsmpdIaTNLBV1VdDgB7IbOVW8ML5KjvBiPe-RKEy9JwumLvfxd9K0IVOGU6cSspgDEKSfh5NovFzD0x-4KYAQca9xIG9jsz3rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f8c95159.mp4?token=aspQacoe8eBE-2ztwEUhbOwF4vMbE_ePv4ZdnpuI8VZL4Rp-eX1zBvbnmTgItuVD2r0ihR6FATUBLqs0PJHECP_gwXj1LAEtW8lQuaFNQdxVcXkX6DHLBBZSTtnztKnZQeuxzGOWpwlNr4JD75Rg3bfIn6t3qHWKScG6tPdfpPamBwYDHrBlL0KTarGQ8-QvN90kuQRRTGV5H_0C-WXHlpcguo_YKWZlKUv-ZpuFFSka3lJRPpRJLsmpdIaTNLBV1VdDgB7IbOVW8ML5KjvBiPe-RKEy9JwumLvfxd9K0IVOGU6cSspgDEKSfh5NovFzD0x-4KYAQca9xIG9jsz3rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عماد بهاور، فعال اصلاح‌طلب، در برنامه «وضعیت»: جریان پهلوی یک جریان فیک مجازی با حمایت کشورهای خارجی است؛ پایگاه اجتماعی سلطنت‌طلب‌ها سه، چهار درصد بود و آنها از طریق ماهواره با نوستالژی، رویا‌فروشی کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/661874" target="_blank">📅 19:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661873">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
شیخ نعیم قاسم: ایران مقتدرتر از گذشته ظاهر شد  دبیرکل حزب‌الله لبنان:
🔹
رژیم صهیونیستی در جنگ علیه ایران به دنبال پایان دادن به مقاومت بود اما به این هدف نرسید.
🔹
وی افزود این تجاوز به اهداف خود دست نیافت و ایران با وجود هزینه‌های سنگین، قدرتمندتر از گذشته…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/661873" target="_blank">📅 19:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661872">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
ترامپ ایران را تهدید به بمباران کرد
🔹
ایران باید فوراً از ایجاد مشکل توسط نمایندگان پر دستمزد خود در لبنان جلوگیری کند.
🔹
اگر این کار را نکنند، ما دوباره به ایران ضربه‌ای سخت خواهیم زد، درست مانند هفته گذشته، فقط سخت‌تر!!!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/661872" target="_blank">📅 19:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661871">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD48dQdntsKam5CyhUTKtjA8LG4mGiJaIaEABT-JnD-dj5MpqsVWy1ibBET5nkGIfBUch3TPtTDtLNWlTYMdDKR3DsO7MjKhzST4mTxZCbF3gZZFVyjFkRcqPypihUgZVc6NWLP-kUhkwfT95o4LvNG4OF5h3suYGuOi7Gbq8TfSE3lk_XkVDlZ9Cs9ThhAae7zJx2r9LNhvhsDafemEJZW4GKfH9AyDAgvi2YYmPgfNM1KhPzYrCzw3d9G9PzqeZ3FszCg3ehhCQ8IEzllJWC768yiX0tboJ2AMxf2XNyTUbNSRHKoo2gJ77HVcagI4pZLUu0ohTMiedElKXgPlQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سید جمال‌الدین اسدآبادی؛ جهانگردی انقلابی و اندیشمند
🔹
سید جمال‌الدین اسدآبادی عمر خود را در سفر گذراند؛ نه برای تجارت و نه برای سیاحت، بلکه برای بیدار کردن ملت‌ها. او از شرق تا غرب جهان اسلام گشت تا مسلمانان را به علم، اتحاد و رهایی از استبداد و استعمار…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/661871" target="_blank">📅 19:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661870">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
شیخ نعیم قاسم: ایران مقتدرتر از گذشته ظاهر شد
دبیرکل حزب‌الله لبنان:
🔹
رژیم صهیونیستی در جنگ علیه ایران به دنبال پایان دادن به مقاومت بود اما به این هدف نرسید.
🔹
وی افزود این تجاوز به اهداف خود دست نیافت و ایران با وجود هزینه‌های سنگین، قدرتمندتر از گذشته ظاهر شد و نشان داد از حق خود عقب‌نشینی نمی‌کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/661870" target="_blank">📅 19:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661869">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
توقف مذاکرات در صورت عدم عقب‌نشینی اسرائیل از لبنان
🔹
گزارش‌ها حاکی است اگر بند اول تفاهمنامه اسلام‌آباد درباره پایان جنگ در لبنان اجرا نشود، مذاکرات ایران و آمریکا متوقف خواهد شد و ایران وارد فاز پاسخ سخت می‌شود./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/661869" target="_blank">📅 19:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661868">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ادعای العربیه: جلسهٔ دوم مذاکرات اندکی بعد آغاز می‌شود؛ هیئت ایرانی به سالن مذاکره بازگشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/661868" target="_blank">📅 19:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661867">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_rHHPWAbDESYrvQ8zB4cK389YslzNBwM3hjkvHeAchfcTIJq9sNGsLTwcfrzIHwVd65LZKsMI4s6mSFU8TxP_AKaE9GStHn6iq6eg_A_kJiBhgrAcHdHbdNv2ZRodWOAAfamsaVHyqfLnbEKdu3dylxxcosIDfUohpHhQJdq67ZimtfAfbZsbblNqCtLbyQqBJIQxCKU7Vn84iNxxvSw0GmgJWQtnnHpJibzdLIMyNQIGN36eaE7pgz2m_aZpc7IU_UPhwEO-k0wsZ_fnEZ9ZV7NgJl0sTFJzterVLq1lqGh_wb5zr1jvRQ8iOogJUhmTa9XPWILVrtqVRdR89WsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آزادی بیان فقط برای اسرائیل؛ وقتی فریادهای فلسطین را خفه می‌کنند
🔹
کارتون: کمال شرف
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/661867" target="_blank">📅 19:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661866">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvAQQ_QT1eHU_puRSp0WzC1NSOXu7Xv1qUHruaaFMpGmaSZhob8osMomwdpbfeaOBbnxWhQFxRu5uHfgWxqXrZz6sb5eQNzIRvSNF5n8Mys4ZZo2Zkp7pcj-jqTjCtmrmQ1tp3SVQrLM5WcKMw7Sv3t-Qj4WP3Z6ZzJJXKJfugo1BXDddZsDuF7HFuViGDMqtT_L_8Oz6SpX0ql08J2p6Y5QFURRnAh1YFqdBvzLkapmdt7P2j3gBaKHMJJCSondq78d1YKy7c-_XJEdOUgUTt7I4VDXHggTSEYOVHewKvwzD8vcEYPHrAXpAYlsLBuiD9CJn1MJj8nHjgeEyN9zDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/661866" target="_blank">📅 19:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661865">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a20ddb73b6.mp4?token=indw0r9YsMod7WIq9DCq14Wu2eV0IIlUyNspuBqv1xipOZyRemL2yGznraOLHKit_BGCIKHh_G2nlYqlWPQPtYHZadVReAk2h1YQkdQW46hezQkk32vtSi0Appf88i_bC0mpP2e60MUw3rGUaXkY5gLoxqkSPf8z5PvaIuVNNMM5X6q5h5QJRqGn3qyGOHgYFUhXX6-wBfkXy35OmE8cPN8g9ns3Mm5jVrjt26N9Ns1JK6U8YWAJ7pSBUm5UJmlmI5_y0jbxI2xVMvfBEgYmsFD9qHYEAXjDMlVhxo4H8opxXpAPOlYv89SpxsycJ8RoiK1-JdO2BnxCrdHG8VIdZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a20ddb73b6.mp4?token=indw0r9YsMod7WIq9DCq14Wu2eV0IIlUyNspuBqv1xipOZyRemL2yGznraOLHKit_BGCIKHh_G2nlYqlWPQPtYHZadVReAk2h1YQkdQW46hezQkk32vtSi0Appf88i_bC0mpP2e60MUw3rGUaXkY5gLoxqkSPf8z5PvaIuVNNMM5X6q5h5QJRqGn3qyGOHgYFUhXX6-wBfkXy35OmE8cPN8g9ns3Mm5jVrjt26N9Ns1JK6U8YWAJ7pSBUm5UJmlmI5_y0jbxI2xVMvfBEgYmsFD9qHYEAXjDMlVhxo4H8opxXpAPOlYv89SpxsycJ8RoiK1-JdO2BnxCrdHG8VIdZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیرحسین ثابتی، نماینده مجلس، در برنامه
«
وضعیت»: به جای براندازی باید جمهوری اسلامی پوست اندازی کند، اصلاحات یک دکان سیاسی برای یک مشت پیرمرد عاشق قدرت است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/661865" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661864">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
سی‌ان‌ان: تمرکز اولیه مذاکرات ایران و آمریکا بر لبنان  سی‌ان‌ان به نقل از منابع دیپلماتیک:
🔹
مذاکرات ایران و آمریکا در سوئیس با تمرکز بر جنگ لبنان، تنگه هرمز و ذخایر هسته‌ای ایران آغاز شده است.
🔹
به گفته این منبع، گفت‌وگوها با فضایی «صریح و بسیار صادقانه»…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/661864" target="_blank">📅 18:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661863">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29839d320.mp4?token=hGaGa-0ufRkp1s8KZdqvknvgCzrRevDAvVWHU9KQ9FZDhAustsRoCe4pMhfzCjtnY9b612MNhFzkYrTSTrKVuxC3YN6uhGl2YzlUGkp7oVOGWmU0ZBbjNwP45gdTdVXjk-tR3OFmmTZywhzgtiLk0rk-dsL6XDs1_zx_i2eRmuD_udwLD861OkXDoDmWo7UvJ3HXlsAnRkOe_iR0fOXRQtI_WLpAgNxji_hJ_3vCCQ-tTiW1ca68BIYSDlqFKFf94r8N_HT7tFl612UQSdGJpd7wwke-fjtFSj81GdHkdGSbhF-3ZymSzkCmkVk9iyQStEeURpS6wazew8bBSHvw6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29839d320.mp4?token=hGaGa-0ufRkp1s8KZdqvknvgCzrRevDAvVWHU9KQ9FZDhAustsRoCe4pMhfzCjtnY9b612MNhFzkYrTSTrKVuxC3YN6uhGl2YzlUGkp7oVOGWmU0ZBbjNwP45gdTdVXjk-tR3OFmmTZywhzgtiLk0rk-dsL6XDs1_zx_i2eRmuD_udwLD861OkXDoDmWo7UvJ3HXlsAnRkOe_iR0fOXRQtI_WLpAgNxji_hJ_3vCCQ-tTiW1ca68BIYSDlqFKFf94r8N_HT7tFl612UQSdGJpd7wwke-fjtFSj81GdHkdGSbhF-3ZymSzkCmkVk9iyQStEeURpS6wazew8bBSHvw6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
نتانیاهو: تا زمانی که لازم باشد در جنوب لبنان باقی خواهیم ماند
🔹
و در مورد ایران، هرچند تحولات سیاسی باشد، اجازه نخواهم داد ایران به سلاح‌های هسته‌ای مجهز شود.
🔹
تا زمانی که من نخست‌وزیر اسرائیل هستم، این اتفاق نخواهد افتاد.
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/661863" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661862">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
اسرائیل هیوم: شروط اسرائیل درباره لبنان
اسرائیل هیوم مدعی شد اسرائیل برای پذیرش خواسته‌های آمریکا و ایران درباره لبنان سه شرط مطرح کرده است:
🔹
عقب‌نشینی کامل نیروهای حزب‌الله از شمال رودخانه لیتانی، برچیدن زیرساخت‌های این گروه در جنوب لیتانی و آزادی کامل اقدام نظامی اسرائیل برای مقابله با هرگونه تهدید آینده.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/661862" target="_blank">📅 18:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661861">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0bcc2190.mp4?token=ixiAhDOVJ6rNGdD7zcF4TDrYc-1-_Yhb38fQJx7omO6Odwovg7jqE-CZinovXRUWp7b5e4MpwGRaD_SUUzDpJMkpbOqw1Ul2ccwBhuqxoFoA_tbQGHkq2dbq_5xLioFnErC_62HXrtpQr1j72WUNm9SI6JDBNXrYL0gT_Bbxj5nqAshCl5BJoFNnPwVihtk4d5qKuXYHjYAgEC2imAOnS9XfP5snueOxR3rHftu9Nd2aWjIcYQx4V9cHDvA0GlCdjJSilAz10Lzj6wZib4j-JGpcyaIgbj09zxZnMO7uBizvV076-xf9-dYOQPlyPYpI3ss51_lJKH1uV226QM6b3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0bcc2190.mp4?token=ixiAhDOVJ6rNGdD7zcF4TDrYc-1-_Yhb38fQJx7omO6Odwovg7jqE-CZinovXRUWp7b5e4MpwGRaD_SUUzDpJMkpbOqw1Ul2ccwBhuqxoFoA_tbQGHkq2dbq_5xLioFnErC_62HXrtpQr1j72WUNm9SI6JDBNXrYL0gT_Bbxj5nqAshCl5BJoFNnPwVihtk4d5qKuXYHjYAgEC2imAOnS9XfP5snueOxR3rHftu9Nd2aWjIcYQx4V9cHDvA0GlCdjJSilAz10Lzj6wZib4j-JGpcyaIgbj09zxZnMO7uBizvV076-xf9-dYOQPlyPYpI3ss51_lJKH1uV226QM6b3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیندسی گراهام: به مسئولین ایران می گویم؛ اگر گوش می‌دهید: وقتی از حزب‌ الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد
#Trash
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/661861" target="_blank">📅 18:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661859">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cAdWCPyNkJmLb7o6IwfzrcNElhtvC_PZC25IhR3ZaUWdtk84YGtU-hjX8-14q2nOofjKYgcGkMM_blmyALUb7wRDFNHL7HDUwf0UcoLlSrlKzn467emiRJ4oYsNLNbzYtpHc7s7lLbZ1L4H91wVFrCdHdhr-XapltEVe2vcBpPG7cs4GdzAOrk2TWDSRCeImPJFLyIAwnD4XLpnkhA4LgnwpzP_kIf83pOIbX7lLK-TL9i3LO4wOSNjuLOMxbEFkmkN9GiLTMiryx7CVQ2wkQO-KdGztud_ble6l6voEy-fJ_N5x_6fkgYdoW1-GF9WdIT89JrnSAEGAPjq4rJdWQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6Ln8S62kMCthVIgGKCdv_TU5gVH22yOamQSE7lSIqCvxig0ExBsPirGnYQ4EJOrujZ_aWsXZKDwQrv4tvdNP-QnLKfT5DtfrsWWjysKSF1X1xjbC32yv3w-NL5a5QsggwsyOQ-J6-vcjWCjp6PwtknbM2eiRgJaAI8tc3C5mlpHyNHA3Bu2GFPsvPsxRO9IRqGQEysy7VcSGlptYvvur3r2ZQ0HOUtHk8hYX8B7TgPNEiIHd_fuhYAiwNGXOwqwo2NwHCuTFzFIJtA9fJbD6sqm_wxTPPg3lvYRexl-dWl8LeaxYCyzIwdqa_rWAW3n72kfs__jZFVGg7cfTsOpTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نشان‌سینه محمدباقر قالیباف رئیس هیئت مذاکره‌کننده «میناب ۱۶۸» در مذاکرات امروز
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/661859" target="_blank">📅 18:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661858">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
یک منبع آگاه در تیم مذاکره‌کننده ایران در سوئیس: هم‌اکنون دور اول مذاکره ۴ جانبه به اتمام رسید/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/661858" target="_blank">📅 18:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661857">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سی‌ان‌ان: تمرکز اولیه مذاکرات ایران و آمریکا بر لبنان
سی‌ان‌ان به نقل از منابع دیپلماتیک:
🔹
مذاکرات ایران و آمریکا در سوئیس با تمرکز بر جنگ لبنان، تنگه هرمز و ذخایر هسته‌ای ایران آغاز شده است.
🔹
به گفته این منبع، گفت‌وگوها با فضایی «صریح و بسیار صادقانه» شروع شده و طرف‌ها همچنین درباره ساختار یک دوره مذاکراتی ۶۰ روزه بر اساس یادداشت تفاهم ۱۴ ماده‌ای هفته گذشته بحث می‌کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/661857" target="_blank">📅 18:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661856">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
یک منبع آگاه در تیم مذاکره‌کننده ایران در سوئیس: هم‌اکنون دور اول مذاکره ۴ جانبه به اتمام رسید/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/661856" target="_blank">📅 18:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661855">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNb2x_2Eraoj7YBZVHjVRbwLrdyRGEXD80rPbfB6nk3PY5ywrN9w-l6xs59Op0e73V_mqcaHusDBRDLMWZ8rBNHgLV74ERDUgFLmWXiDJhnz7MgoAo46o3ZKHZ4MBvugcAZWxb8AAQ_qdZUxDDvNYV00biYDF_1PQfINyrLWl0YkdQIGn5jjMuxmmYOv-hmiztYa_mi-ILSlSvFuZauVhyBTMBTCxIdlJkhpCaz2BT4VE5B8QJk98SXBFSc3LeJAX-VgXddJD-_aUumWMWhZ8OBCWoux2cvD0p8vLpzbcM23MqQiD944FG3q83zSKi9q_Hi8pxLDVX9D0IPcwnY1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرندی: ایران دیشب پس از آتش‌بس در لبنان تنگه هرمز را به تدریج بازگشایی کرد
تحلیلگر مسائل بین‌الملل:
🔹
ظرف چند ساعت پس از بستن تنگه هرمز توسط ایران، رژیم صهیونیستی با آتش‌بس موافقت کرد و کشتار کودکان لبنانی را متوقف کرد.
🔹
تا صبح، ایران به تدریج تنگه را بازگشایی کرد. ترامپ اکنون تهدیدهای توخالی می‌کند تا اعتبار این بازگشایی را از آن خود کند - اما زمان‌بندی چیز دیگری می‌گوید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/661855" target="_blank">📅 18:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661853">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f6f22c4f.mp4?token=MFNwzfI5JdaSgNq-Sw8vGN-m5SsUR8punUXrAU94pQP4m3TVVSuLFwGtbL8oee0lW7gpHpQktH-xEhJirAFG26_ny41OMOJG3z66q_ftRODXx-0q7Evy2T6bv_N2kY9BLcm6iWuoQvCvXTGCsBEz0G45p7ShulmsskKerUSD9OZAruOZpvcP9EgMTmzFi4nXcHuXQdnZNvvP3hCIlyl_xUy6Gr2pXO8IFk9tOuFYF8OBXDvtk33aeZQvPL2V9ut857QAQJK3hFj8ZKrrfqjsth6A_62eRaJNLxMnfDMphh11FmU5IEnDtSg6Qqe2eVo5yUDedGfT3WXCj8HtBeBn5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f6f22c4f.mp4?token=MFNwzfI5JdaSgNq-Sw8vGN-m5SsUR8punUXrAU94pQP4m3TVVSuLFwGtbL8oee0lW7gpHpQktH-xEhJirAFG26_ny41OMOJG3z66q_ftRODXx-0q7Evy2T6bv_N2kY9BLcm6iWuoQvCvXTGCsBEz0G45p7ShulmsskKerUSD9OZAruOZpvcP9EgMTmzFi4nXcHuXQdnZNvvP3hCIlyl_xUy6Gr2pXO8IFk9tOuFYF8OBXDvtk33aeZQvPL2V9ut857QAQJK3hFj8ZKrrfqjsth6A_62eRaJNLxMnfDMphh11FmU5IEnDtSg6Qqe2eVo5yUDedGfT3WXCj8HtBeBn5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجاح: اسرائیل ممکن است توافق را برهم بزند؛ ایران باید تضمین‌های عملی بگیرد
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
«تنگه هرمز را باید خوب از آن استفاده کرد و نباید یک لحظه از آن اغماض کنیم؛ این امروز یک سلاح جدید است.»
🔹
هرچند ایران به نتیجه خوبی رسیده، اما چون اسرائیل احساس شکست می‌کند، ممکن است برای برهم زدن توافق تلاش کند، بنابراین ایران باید از آمریکا تعهدات قوی‌تری بگیرد و این تعهدات نباید در حد وعده باشد، بلکه باید کاملاً عملی و قابل اجرا باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/661853" target="_blank">📅 18:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661852">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ارجاع پروندۀ یکی از معاونان رئیس‌جمهور به دادسرای دیوان محاسبات
دیوان محاسبات کشور:
🔹
درپی طرح موضوع واردات بنزین و اعلام آمارهای غیرمستند، پرونده یکی از معاونان رئیس‌جمهور به دادسرای دیوان محاسبات ارجاع شده است.
🔹
این نهاد همچنین با اشاره به مغایرت رقم اعلامی «۶ میلیارد دلار» واردات بنزین در سال ۱۴۰۴ با داده‌های رسمی، خواستار ارائه مستندات مربوط به این ادعا شد./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/661852" target="_blank">📅 17:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661851">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
زنگ خطر HIV؛ سن ابتلا به ۲۵ تا ۳۵ سال رسید
حسین پور، مسئول پیشگیری از بیماری‌های ایدز و هپاتیت دانشگاه علوم پزشکی مشهد:
🔹
آمار مبتلایان به ایدز به ۶۵۰ نفر رسیده و سالانه ۵۰ تا ۶۰ بیمار جدید شناسایی می‌شوند. ۷۰ درصد موارد جدید از طریق روابط جنسی پرخطر منتقل شده‌اند و سهم زنان از مبتلایان به بیش از ۳۰ درصد افزایش یافته است.
🔹
متخصصان تأکید می‌کنند تشخیص به‌موقع و مصرف دارو به مدت ۳ تا ۶ ماه می‌تواند ویروس را کنترل کرده و احتمال انتقال آن را از بین ببرد./ اخبارمشهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/661851" target="_blank">📅 17:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661848">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
محسن زنگنه، نماینده مجلس: پزشکیان فرآیند ارزیابی عملکرد وزرا را آغاز کرده است/ اگر لازم است دولت وزیر نفت را تغییر دهد
محسن زنگنه, عضو کمیسیون برنامه و بودجه مجلس:
🔹
پزشکیان فرآیندی را برای ارزیابی عملکرد وزرا و مدیران دولت آغاز کرده‌اند. اکنون نزدیک به دو سال از عمر دولت گذشته و طبیعی است که ارزیابی عملکرد اعضای کابینه در دستور کار قرار گیرد.
🔹
همان نکات و مسائلی که پیش از جنگ هم مجلس درباره آن‌ها به دولت محترم تذکر داده می‌شد، در دوران جنگ نیز خود را نشان داد.
🔹
بخش‌هایی که در طول جنگ با ضعف‌هایی مواجه بودند و علی‌رغم تلاش دولتمردان بعضاً مشکلاتی ایجاد کردند، عمدتاً همان حوزه‌هایی بودند که پیش از آن نیز درباره عملکرد آن‌ها نقدها و تذکراتی مطرح شده بود و نیاز به اصلاحات و تغییرات در آن‌ها احساس می‌شد مانند وزارت نفت/سندنیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/661848" target="_blank">📅 17:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661847">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
سقوط هواپیمای اسرائیلی در نزدیکی واشنگتن
🔹
گزارش‌های اولیه از سقوط یک هواپیما متعلق به رژیم صهیونیستی در شرق واشنگتن دی‌سی خبر می‌دهد؛ حادثه‌ای که به کشته شدن خلبان و دو سرنشین آن انجامید.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/661847" target="_blank">📅 17:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661846">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8bZ84Pcz2bWxVmv9XVzPZy2hr7zNbAy_lPutZTSLp3rFqakLj2Dxl3F4EQq9Qy4ro_1muQuWwc6pziYFiCH8hrCVOKxAYtGwjbeDltq6lAzHjx9rd_OigXWc9UYgvOESSJr5cfb7LJ6Fy2DnlXbt2B-0c0oCO5exlwbIUDv7dzacCEaAW2ht4sD3aNB3LeUCXSXU6OHp3ZfGHJxByhfTvlCBKerGqCtTsDoK1dgoelv3rnPHN11DWjJTiLle_OzrsoZaH6kw8-vUBT542SN_Oia1rG-ol9COM30bGFf4QVjIaxVNl4dOC5O94MmWNqdISuimH_8SpOTAtAnyPNpsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش قاطع مرندی به ادعای ترامپ در مورد تنگه هرمز/ هزینه دریافت خواهد شد
🔹
تحلیلگر مسائل بین‌الملل: هزینه‌ای دریافت خواهد شد. این قطعی است.
🔹
ترامپ شب گذشته مدعی شده بود «در طول دوره آتش‌بس، به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/661846" target="_blank">📅 17:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661845">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3XNsn5jGBn3SfHNPUCDRYY_kPwI8k3AXr9QPFOa3vMTOCIR2rc1P0nC8FHHhJ2q4SXENeHI3Hka5sARw5WW1ZCl6YnFcfabJvqN0-qBo0Q9nQwEEJKpRmuC8Jdum9aNoc-QVyxE8Mld62E8BTgnd34tX9CgW63S-OlQnttGzSZm6J6NH7KD8xgIwGaG-wucze-6KyE7VdbVRokqEXXYM1QwTceRAI92Y1R0BC3md_DheDvzJfowA_326fpVp5GxM0aPkNkSSSHpe0Yo1fVv-CIqjCyfAFtOkVlW1keQxm-142bDS-OyytpPWTduhSyN9aC8dblTHvc6P-FBR-0Xvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکثریت آلمانی‌ها از مشارکت در مأموریت اروپایی برای تأمین امنیت تنگه هرمز حمایت می‌کنند
🔹
بر اساس یک نظرسنجی، ۵۷ درصد از شهروندان آلمان از مشارکت این کشور در یک مأموریت اروپایی برای حفاظت از کشتیرانی در تنگه هرمز حمایت می‌کنند.
🔹
با این حال، توان عملیاتی برلین محدود است و آلمان عمدتاً می‌تواند نقش پشتیبانی، شناسایی و مین‌روبی ایفا کند. مقام‌های نیروی دریایی آلمان نیز اذعان کرده‌اند که این کشور با «کوچک‌ترین ناوگان تاریخ خود» روبه‌رو است، در حالی که با مأموریت‌های فزاینده‌ای مواجه شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/661845" target="_blank">📅 17:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661844">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
فرانس ۲۴: ملوانان در تنگه هرمز گرفتار شدند
🔹
با وجود آغاز مذاکرات ایران و آمریکا در سوئیس، تنگه هرمز توسط ایران بسته شده و هزاران ملوان در این منطقه گرفتار شده‌اند؛ موضوعی که می‌تواند پیامدهای اقتصادی گسترده‌ای داشته باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/661844" target="_blank">📅 17:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661841">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e60fd748c1.mp4?token=OX7NzZ1TPzyfwcvOvE-D18TjCKAsArbinBnmSkNvAi1ji7ZSEfKNPqXpugOIbeWAl9vRUPHX5PYBzWrs06LSWihoKWkAlsJ5RQUzyzruK1LzJCxnPrrjT7ca_fVfOyDQD9WD6vX_0IjFM7ZUlw1vX1eeapJU8ojJ6NNXwfD8cIfLa1t-tTeFnlfebvQsHufng1NuCDGtxtU4sYrxWuEESmMh7aE7blY8206wPHjIUQX-z0j7GlEq_uk67eUq-1s4X8-gQ9tmu4OBgjq2obUIsqsZkOAkDYOEYixA9yXfnVqhJx3vqVEt6CfGFw32Hcb0BPgLOLZxQl-GH5KNvmahxoI31KEeBj5XZCWIawgO8QI_s-CV2DNkADAZsaUYBQMOYBFgSWD7RiWIAENUff3yNFe0J3GvbGrJ9uGHBAI-qNxnO8-JvZLZl2cGuDCCDf5FVTojsqTvME6Sv035-4mLOQP8mB2OunX4edVysbxarzgnxnc9rRf10Ee2Hb_YJn-QtRb2pVtLjzHkU23ZNL88LPhGvMQVh0IIrYinP7DS3sJWXIQKONFDadlvM-3AqRixJu8zeoTl1Go3CkwUW6RI6I_wkEBQydlN_D40ZhcjQSGc048NEdkibicZZDYMWoopEzu5dK0EsdtgjVYvIYgjMn5hkMTUUT014sF6JvmTKKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e60fd748c1.mp4?token=OX7NzZ1TPzyfwcvOvE-D18TjCKAsArbinBnmSkNvAi1ji7ZSEfKNPqXpugOIbeWAl9vRUPHX5PYBzWrs06LSWihoKWkAlsJ5RQUzyzruK1LzJCxnPrrjT7ca_fVfOyDQD9WD6vX_0IjFM7ZUlw1vX1eeapJU8ojJ6NNXwfD8cIfLa1t-tTeFnlfebvQsHufng1NuCDGtxtU4sYrxWuEESmMh7aE7blY8206wPHjIUQX-z0j7GlEq_uk67eUq-1s4X8-gQ9tmu4OBgjq2obUIsqsZkOAkDYOEYixA9yXfnVqhJx3vqVEt6CfGFw32Hcb0BPgLOLZxQl-GH5KNvmahxoI31KEeBj5XZCWIawgO8QI_s-CV2DNkADAZsaUYBQMOYBFgSWD7RiWIAENUff3yNFe0J3GvbGrJ9uGHBAI-qNxnO8-JvZLZl2cGuDCCDf5FVTojsqTvME6Sv035-4mLOQP8mB2OunX4edVysbxarzgnxnc9rRf10Ee2Hb_YJn-QtRb2pVtLjzHkU23ZNL88LPhGvMQVh0IIrYinP7DS3sJWXIQKONFDadlvM-3AqRixJu8zeoTl1Go3CkwUW6RI6I_wkEBQydlN_D40ZhcjQSGc048NEdkibicZZDYMWoopEzu5dK0EsdtgjVYvIYgjMn5hkMTUUT014sF6JvmTKKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رژیم صهیونیستی به این توافق تن نمی‌دهد؛ ایران باید هوشیار باشد
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
اگر کسی فکر می‌کند رژیم صهیونیستی به فشارهای تحمیل‌شده تن می‌دهد، اشتباه می‌کند.»
🔹
آتش‌بس احتمالی می‌تواند تاکتیکی و موقت باشد و جنگ هنوز پایان نیافته است.
🔹
فاصله‌گیری ظاهری آمریکا از رژیم صهیونیستی ممکن است صرفاً یک بازی سیاسی باشد و ایران باید هوشیار بماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/661841" target="_blank">📅 17:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661840">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ترامپ به فاکس نیوز: اگر با ایران به توافق نرسیم، از کشتی‌های عبوری در تنگه هرمز عوارض می‌گیریم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/661840" target="_blank">📅 17:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661839">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClnfVdqEQ_kqD1Dvam5A6HrQF5VuwC_Yl-FoiJXqO-eEVzg5suVkftFy18rBiaT_jNzhFuMkqB5M5_4KhRDgiKi8SBl1TcFGlOQjRQK9re_ioe33_Xgh10EPiAPrZTGcoS9PGz54sgyTZDrO8S5bHQ4fpJZZ26CvQRdB7RHyzqdmq1udMJC3uqx-XRl8DRlelQ4EMzT99AlhEdoCVTMThR2TWr_xJK2IQHU4-ir6PzLfR-3toc1TVGEHqqOJnBMVfXKcCILlC49-kltUSkw7ygi4BNE89LvFrkKoWFxF3eOm4AQRprw7scDxc8akJKAIvzBtRK8pNmX-F0aSHQsaEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ ایران را تهدید به بمباران کرد
🔹
ایران باید فوراً از ایجاد مشکل توسط نمایندگان پر دستمزد خود در لبنان جلوگیری کند.
🔹
اگر این کار را نکنند، ما دوباره به ایران ضربه‌ای سخت خواهیم زد، درست مانند هفته گذشته، فقط سخت‌تر!!!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/661839" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661838">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ترامپ درباره ایران: دیروز ۱۹ میلیون بشکه نفت خام به دلیل این تفاهم‌نامه با ایرانی‌ها از خلیج فارس خارج شد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/661838" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661837">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
توهین ترامپ به پزشکیان: مواظب حرف زدنت باش!
🔹
رئیس‌جمهور ایران، پزشکیان: ما از حق خود برای غنی‌سازی کوتاه نخواهیم آمد.
🔹
ترامپ، رئیس جمهور کشور بازنده جنگ: بهتر است مواظب حرف‌هایش باشد. بهتر است خود را اصلاح کند، وگرنه ما بقیه کشور را تصاحب خواهیم کرد! #Devil…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/661837" target="_blank">📅 17:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661836">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803b709f3e.mp4?token=FeOff773HPljMbcQQ3rgke09x7ihMS1ZxFbii10i6IMiq3K7RHTviMsIJk8LG0DXkyIH0GV2bMyGtT2dmTBOnWHAHF1jO4MmLX_abwcf1ZuPz0gTwWgJ2ka0pFnGrEgtmxJ8BYLf2jzBmHaZ9h6xRK--nUm2qkOe3mKQLq1RrP1mm9hRv1716d2xGNbqxW1pSG4ER2oEwUU8_3EDxyfkpAjThez6rjK6T_Yu8eu-sf3sU89eVwdMx0ji7o_5u5VE6b3_Gk_jb6tkrWMR7hir_GUZ-9TB06lUaLXsVhUCJP0ySJNdKFgyoaAuEPeNvfoOQuXK5b2lNuIpEpRq0SQoQ766jc8aIRmKzjKANHhvlPA3R2edRq5u46rLYRXnBTdZL6Tc28iqGDaIKuwXaXHU1gMiIZS6nsIz8UtR2tLbB8LCvlOaPqZAoVPDCvbu-aUOdWwrPsJB6rvgy6wo-OoXsroYL3AMrlWwl_ASr-ZQQm4Onus-sjrVO-qZnoznRlPZHu1mkIaUYPiTiiEEcsJ1t8sI1lknJGoZBM223-GPsPE2ctXAz-rp3fEPts4k2FeT8yofMbIoOFsdH1hN9nxU9ChpKXwml2NnmF5I7sEywNvNDiYGqT69WaXAiygoE4OYvBswi6_-1UmMUqqewVoAsF6RwaJz5H2guYLX3X5i41U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803b709f3e.mp4?token=FeOff773HPljMbcQQ3rgke09x7ihMS1ZxFbii10i6IMiq3K7RHTviMsIJk8LG0DXkyIH0GV2bMyGtT2dmTBOnWHAHF1jO4MmLX_abwcf1ZuPz0gTwWgJ2ka0pFnGrEgtmxJ8BYLf2jzBmHaZ9h6xRK--nUm2qkOe3mKQLq1RrP1mm9hRv1716d2xGNbqxW1pSG4ER2oEwUU8_3EDxyfkpAjThez6rjK6T_Yu8eu-sf3sU89eVwdMx0ji7o_5u5VE6b3_Gk_jb6tkrWMR7hir_GUZ-9TB06lUaLXsVhUCJP0ySJNdKFgyoaAuEPeNvfoOQuXK5b2lNuIpEpRq0SQoQ766jc8aIRmKzjKANHhvlPA3R2edRq5u46rLYRXnBTdZL6Tc28iqGDaIKuwXaXHU1gMiIZS6nsIz8UtR2tLbB8LCvlOaPqZAoVPDCvbu-aUOdWwrPsJB6rvgy6wo-OoXsroYL3AMrlWwl_ASr-ZQQm4Onus-sjrVO-qZnoznRlPZHu1mkIaUYPiTiiEEcsJ1t8sI1lknJGoZBM223-GPsPE2ctXAz-rp3fEPts4k2FeT8yofMbIoOFsdH1hN9nxU9ChpKXwml2NnmF5I7sEywNvNDiYGqT69WaXAiygoE4OYvBswi6_-1UmMUqqewVoAsF6RwaJz5H2guYLX3X5i41U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهین
ترامپ به پزشکیان: مواظب حرف زدنت باش!
🔹
رئیس‌جمهور ایران، پزشکیان: ما از حق خود برای غنی‌سازی کوتاه نخواهیم آمد.
🔹
ترامپ، رئیس جمهور کشور بازنده جنگ: بهتر است مواظب حرف‌هایش باشد. بهتر است خود را اصلاح کند، وگرنه ما بقیه کشور را تصاحب خواهیم کرد!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/661836" target="_blank">📅 16:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661835">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635a9253a5.mp4?token=HYPPlsUAlIO0Dmli6cLkqTuKUOWoSLoK6jPKHsKf0fjtVBbyilDg-XoLiYBax2tjpyff6wFS7krsm6H06erDKfQDtp47p744a2bf6S0YCG2YBEsXwjNE3_AaJUNEDu46uT1X17rb-YxBtzlQEkCQQKAWyusHpmsDCIFGq8pBI9zgRg4UVe8lBJfsOrgFU05BVDpmMBIRtzpqpKF-Y3CLTMYt3CMR50VmgwUr2Xk-SrzjSWwg4bO3Os5r5kdNRzFCa26i70asob5Qdi_nEgX9WLofs8h86tFFjvPl7s19xLxD9EoStOnX5Uc85CLkQE-VOLPE2mUUwrB9WA57MDZMMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635a9253a5.mp4?token=HYPPlsUAlIO0Dmli6cLkqTuKUOWoSLoK6jPKHsKf0fjtVBbyilDg-XoLiYBax2tjpyff6wFS7krsm6H06erDKfQDtp47p744a2bf6S0YCG2YBEsXwjNE3_AaJUNEDu46uT1X17rb-YxBtzlQEkCQQKAWyusHpmsDCIFGq8pBI9zgRg4UVe8lBJfsOrgFU05BVDpmMBIRtzpqpKF-Y3CLTMYt3CMR50VmgwUr2Xk-SrzjSWwg4bO3Os5r5kdNRzFCa26i70asob5Qdi_nEgX9WLofs8h86tFFjvPl7s19xLxD9EoStOnX5Uc85CLkQE-VOLPE2mUUwrB9WA57MDZMMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ مسئولین مذاکراتی ایران را تهدید کرد
🔹
ترامپ گفت که با مقامات ایرانی صحبت کرده و به آنها گفته است: «اگر تنگه هرمز را ببندید، دیگر کشوری نخواهید داشت. حتی به کشور لعنتی‌تان هم برنمی‌گردید.»
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/661835" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661834">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چند کلمه با هم‌وطنان لس‌آنجلسی!
🔹
محمدرضا احمدی گزارشگر تلویزیون در بازی ایران و نیوزلند و بعد از گل دوم ایران، شاید ناخواسته یکی از عمیق‌ترین تصاویر این جام جهانی را در چند کلمه به تصویر کشید "ایرانی‌ها رو با هم دیگه می‌بینیم، با هر شکلی، با هر شرایطی، با هر پرچم اورجینال و فیکی؛ نیم‌خیز بودن تو ورزشگاه و دلشون با تیم ملی بود."
🔹
بله؛ می‌شود بر سر هزار مسئله اختلاف داشت، می‌شود سال‌ها از هم دور افتاد، می‌شود جهان را از پنجره‌های متفاوت دید، اما بعضی نام‌ها آن‌قدر بزرگ‌اند که اختلاف‌ها در برابرشان کوچک می‌شوند. ایران یکی از آن نام‌هاست.
🔹
گاهی یک مسابقه فوتبال، آینه‌ای می‌شود برای تماشای حقیقتی عمیق‌تر. حقیقتِ مردمانی که شاید در زندگی روزمره کنار هم نایستند، اما وقتی نام ایران بر سینه بازیکنان نقش می‌بندد، چیزی در اعماق جانشان بیدار می‌شود؛ حسی که نه مرز می‌شناسد، نه فاصله و نه اختلاف.
چرا؟ چون تاریخ همیشه افتخارها را حفظ می‌کند، نه اختلاف‌ها را.
🔹
ایران فقط یک کشور نیست؛ روایتی است که هزاران سال نوشته شده است. از تیر آرش که بر افق نشست تا واژه‌های فردوسی که این سرزمین را از فراموشی نجات داد. از اشک مادران تا لبخند کودکان، از شکست‌ها تا پیروزی‌ها، همه در یک نام خلاصه شده‌اند؛ ایران.
🔹
امروز وقتی از گذشته سخن می‌گوییم، کسی جدال‌های کنار میدان را به خاطر نمی‌آورد، همانطور که هیاهوی منافقین در جام‌جهانی ۹۸ فرانسه ماندگار نشد. آنچه مانده، تصویر غرور یک ملت است که برای چند لحظه، یک‌دل و یک‌صدا شد.
🔹
در روزهایی که تیم ملی به میدان می‌رود، هر گل ایران فقط یک گل نیست؛ لبخند میلیون‌ها ایرانی است. این لبخند را دریغ نکنیم.
🔹
جام‌ها و روزها می‌گذرند اما آنچه می‌ماند، خاطره ایستادن زیر یک نام است. سال‌ها بعد، فرزندان این سرزمین از ما نخواهند پرسید در آن روزها چه اختلافی داشتیم؛ خواهند پرسید وقتی نام ایران در جهان طنین انداخت، دل ما برای کدام سو می‌تپید.
🔹
و چه خوش گفته‌اند که وطن، فقط خاک نیست؛ وطن بخشی از روح آدمی است، روحی که نامش ایران است.
@TV_Fori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/661834" target="_blank">📅 16:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661832">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ادعای
ترامپ درباره توافق با ایران: من یک گزینه ۶۰ روزه دارم. بعد از آن می‌توانم هر کاری که بخواهم انجام دهم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/661832" target="_blank">📅 16:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661831">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
جزئیات مذاکرات ایران و آمریکا از زبان وزیر خارجه پاکستان
🔹
وزیر امور خارجه پاکستان، با ابراز خوش‌بینی نسبت به نتایج مذاکرات ایران و آمریکا گفت کمیته‌های فنی در حال بررسی پرونده هسته‌ای، پول‌های بلوکه‌ شده و مسئله لبنان هستند.
🔹
سه تیم فنی در این مذاکرات حضور دارند و اسلام‌آباد پس از ۴۷ سال موفق به انجام یک میانجی‌گری تاریخی میان تهران و واشنگتن شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/661831" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661830">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
مذاکرات هیات‌های دیپلماتیک و سیاسی ایران و آمریکا با حضور میانجی‌گران پاکستانی و قطری در محل هتل «بورگن‌اشتوک» آغاز شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/661830" target="_blank">📅 16:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661829">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3522dcaf.mp4?token=gmOuhP4zcTu6aqZe_cWXqi3UR_V9qsmCwjzGdbnXOnrUqeX6MRXDogjKlG8P3cdHtk2mvNPQR_g2uPVkfMiymhXqU5O-QqdAIwg7xnccLpBeKH1nsAVvWm0NUUNZcIBccrfx5FSVVzP6Ng09QLTGmpPFLQA0_cIWVXG4B7beqJXCMbhoWZkZhaSB7i5l8G0uwkPwBz16GGM0uGCgHjW-a0232iGGEUdArjxRWoc0v76Tg62GO1KKlOBG4MSHEOl20bZG4kLjJPsqNoVh6cCiObs2kJOjcgF9TvuD5uIO5bIW6r-Xq_Y_SVhZg6smSCxyJxUpCGTrtARyCx3Oo9WnIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3522dcaf.mp4?token=gmOuhP4zcTu6aqZe_cWXqi3UR_V9qsmCwjzGdbnXOnrUqeX6MRXDogjKlG8P3cdHtk2mvNPQR_g2uPVkfMiymhXqU5O-QqdAIwg7xnccLpBeKH1nsAVvWm0NUUNZcIBccrfx5FSVVzP6Ng09QLTGmpPFLQA0_cIWVXG4B7beqJXCMbhoWZkZhaSB7i5l8G0uwkPwBz16GGM0uGCgHjW-a0232iGGEUdArjxRWoc0v76Tg62GO1KKlOBG4MSHEOl20bZG4kLjJPsqNoVh6cCiObs2kJOjcgF9TvuD5uIO5bIW6r-Xq_Y_SVhZg6smSCxyJxUpCGTrtARyCx3Oo9WnIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیم مذاکره‌کننده آمریکایی وارد محل برگزاری مذاکرات شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/661829" target="_blank">📅 16:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661828">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
مخالفت هیات ایرانی با عکس مشترک در ژنو
یک منبع نزدیک به تیم مذاکره‌کننده:
🔹
هیات ایرانی با برگزاری مراسم دست دادن و عکس مشترک با هیات آمریکایی در آغاز مذاکرات ژنو مخالفت کرد.
🔹
در پی این تصمیم، پخش مستقیم و مراسم عکس لغو شد و نشست بدون حضور هیات ایرانی در بخش تشریفات برگزار شد./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/661828" target="_blank">📅 16:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661827">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ترامپ به فاکس نیوز: اگر ایرانی‌ها تنگه هرمز را ببندند، کشورشان نابود خواهد شد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/661827" target="_blank">📅 16:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661826">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ترامپ به فاکس نیوز: اگر ایرانی‌ها تنگه هرمز را ببندند، کشورشان نابود خواهد شد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/661826" target="_blank">📅 16:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661825">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7a642d2a1.mp4?token=NUjEukbIq_nPhAPIomlXGCYA7gDzjFoJT3rBBeXSJI_Os02FCgcONl0gXHvgo105-NtBgedwAoBMuMm1HFzgdy0GSQjCVH-GBYtv32VsUspAEapIMCHvbolOEpXIJqfFs019leUOuVxzcNX0gjmugZVK_0kgBvbabA_CN68Ofa9DL6vwulFVmRUxeXc97iXxzlyK9Y2V6nDvXU3AQH75wJWxHFn-3DRfoJjw4iN_YEZWhgFkWo2VK-w0-QkSd9fu95gNFnzZh8EXtQBpCZA1HwjOGiq55fd-XUDpTutl-y6z0i1MOO30lAlA4J4aIbnDuAfVU61ZjLNSJgafxn39AELUzQTV5wpw4QVpzwu0rPuspHAZcOcXRhOqbHyVBUNxOwhGu4MxNgEV6V3FO7EfpCHWFdfhihd-_XIsj5k0ADHhZZNcPo2HuPeTHOS3l2reDnXyLyYBF1ocBJxcL-gh3Xqgn8YK8mfXlZLrQaDyIx6HyPhij9FaC3gh-1LcUAPrN30uV23AI3iJrvgIBB0g8mVCcQggn1hsLcAMrQcnGdxgP7uGafD0lM31PZefvhjFrD0P7VbqLnLhNsE5Aie7qsMC2sjYSMQMlU0jxazc8AMXk6L-68eSOqUfqzAi87IswYj8Ng4mYw1TiYR1KTPzhWTY77et5auG8c03CbvDW78" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7a642d2a1.mp4?token=NUjEukbIq_nPhAPIomlXGCYA7gDzjFoJT3rBBeXSJI_Os02FCgcONl0gXHvgo105-NtBgedwAoBMuMm1HFzgdy0GSQjCVH-GBYtv32VsUspAEapIMCHvbolOEpXIJqfFs019leUOuVxzcNX0gjmugZVK_0kgBvbabA_CN68Ofa9DL6vwulFVmRUxeXc97iXxzlyK9Y2V6nDvXU3AQH75wJWxHFn-3DRfoJjw4iN_YEZWhgFkWo2VK-w0-QkSd9fu95gNFnzZh8EXtQBpCZA1HwjOGiq55fd-XUDpTutl-y6z0i1MOO30lAlA4J4aIbnDuAfVU61ZjLNSJgafxn39AELUzQTV5wpw4QVpzwu0rPuspHAZcOcXRhOqbHyVBUNxOwhGu4MxNgEV6V3FO7EfpCHWFdfhihd-_XIsj5k0ADHhZZNcPo2HuPeTHOS3l2reDnXyLyYBF1ocBJxcL-gh3Xqgn8YK8mfXlZLrQaDyIx6HyPhij9FaC3gh-1LcUAPrN30uV23AI3iJrvgIBB0g8mVCcQggn1hsLcAMrQcnGdxgP7uGafD0lM31PZefvhjFrD0P7VbqLnLhNsE5Aie7qsMC2sjYSMQMlU0jxazc8AMXk6L-68eSOqUfqzAi87IswYj8Ng4mYw1TiYR1KTPzhWTY77et5auG8c03CbvDW78" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروج خبرنگاران از محل نشست چهارجانبه در پی شرط قالیباف برای عدم حضور رسانه‌ها در این نشست
🔹
درحالی که ونس و هیئت‌های میانجی در محل گفت‌وگوها مستقر شده بودند اما هیئت ایرانی تا زمانی که رسانه‌ها محل این نشست را ترک نکردند وارد اتاق نشدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/661825" target="_blank">📅 16:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661824">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e86ce32a0.mp4?token=dG9RhAQxmnIibzOJG4cpVfQ_Bv6gU8ks4NoCEZWtCuuSD7lp7x4n-Ht1Bd6pQyQR-6US0DlGMKZbb-EcTeFQ7B9DtYz6qsaD6xfwsbiez5Wjt9044gy0xvY4NHpwm7Xxg1zSQvN-7WNOqFF6hNZQFzBGcSSw9vK1WVpBbvWjWJ3R2uP_e1oS1JzY4BLbGbAFdHlWJsGLzkfzH9VTvmw5QTZJd_b7uFjG2t1_VB8o6nIxPeUKsjb8d2fOsXb8f4zYiqqiR_GKMp71jC8BXDMZXPQ975EfCk508BbCIy4PxCEzqLFYAtTjFw5Y4C1qmG4I5TyEs7gSix5_kxbPcqwqtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e86ce32a0.mp4?token=dG9RhAQxmnIibzOJG4cpVfQ_Bv6gU8ks4NoCEZWtCuuSD7lp7x4n-Ht1Bd6pQyQR-6US0DlGMKZbb-EcTeFQ7B9DtYz6qsaD6xfwsbiez5Wjt9044gy0xvY4NHpwm7Xxg1zSQvN-7WNOqFF6hNZQFzBGcSSw9vK1WVpBbvWjWJ3R2uP_e1oS1JzY4BLbGbAFdHlWJsGLzkfzH9VTvmw5QTZJd_b7uFjG2t1_VB8o6nIxPeUKsjb8d2fOsXb8f4zYiqqiR_GKMp71jC8BXDMZXPQ975EfCk508BbCIy4PxCEzqLFYAtTjFw5Y4C1qmG4I5TyEs7gSix5_kxbPcqwqtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور هیئت ایران به محل برگزاری مذاکرات چهارجانبه در سوئیس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/661824" target="_blank">📅 16:38 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
