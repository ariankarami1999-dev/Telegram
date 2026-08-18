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
<img src="https://cdn4.telesco.pe/file/ruQz66cNyZAQfFMlewHMgl1m3B0dTLs8wEP4mTYC4_IK2ggdPrihuAqD8lCW5WHV24fPFg5VvLjdbJZB0yNNorzr80PeXelWRgu9na4ILKLOPC6Tu_WphVJKKH_4u2xGWi68ATefeBp_JwKOsVb1rGuukDz8NEihUchHV7m4SzQfa3vBJ6YrYDYJFZThYIidjUnR4HwZl6hmut2VSfFb2dNniRG3CGwctGXT5NG9s-FtaBGSp-1JpF_VD5jREbsEr_lgJBITnyKlKyveaOKAIVjZ-gF545otO4bZKx7NWUlmDNr9u1VdvOV3j5xSgsYElsscegTG3ehP95BgieNjfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.1M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 15:56:28</div>
<hr>

<div class="tg-post" id="msg-682238">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dca9c54e6.mp4?token=UxV7Hqz3g4_OYvMpNDxBBpBWd3Spmj3pSWoN3HJMxpOUflYgRIXeKkX-BQuOdF2Tu_E1weE2DSKpudyUZa8xgMbGMTQsbgBHiVewKEiet0a4n-TZpEuQvZBuHDgvkvkCyv7qGNi3GEUgcx0CtMXRwB8FU1BrJFYHSmoPPkMVQ4V1oY7Bc4piDIWEVhfOuOh62I0v5U4rwuC_kGOFXbytNsiDerhv3hDmhiWpAb5MkPmtehB6jK_OtrHLiXhcJH96NKKoX_cxgFrXX-YX6naTWEppbZQNL310awBHmbkOTbMobFOWyOXnxpnu4G5EX2e0lrwG2g_sVSBA5ST82Muyqi8JhKKmrD7CZLlf6n2VxJpaKFq00CDDKwzNKkYNW4ucYlxUiflqvfW0ahOBnX3bZmRqMRuqOKFSPw1oJW6RCWZta0MYlP331pX3sGDXFQkxezuBM5t7s4SCymAHtRVOU5ze3A3DH-jJhPu2BJomzsXMkOlvqtu9KIrRdY-_t6hnd8YuCDjporpJ2Eke6WVpS4AmpRKXftvM3BXNWWOcgdGwAR-WKD1o88imIpIVX9CSbQ-CJaw3QZMU7Tg7Y7MaRFJ9OAZ_TURv1QiX-BuxFA8-rXC_hZKx5_B2uXQeHqMl4vD55bJRV_3K53CV27etXcMn2l1FoPfMpW4toapa19w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dca9c54e6.mp4?token=UxV7Hqz3g4_OYvMpNDxBBpBWd3Spmj3pSWoN3HJMxpOUflYgRIXeKkX-BQuOdF2Tu_E1weE2DSKpudyUZa8xgMbGMTQsbgBHiVewKEiet0a4n-TZpEuQvZBuHDgvkvkCyv7qGNi3GEUgcx0CtMXRwB8FU1BrJFYHSmoPPkMVQ4V1oY7Bc4piDIWEVhfOuOh62I0v5U4rwuC_kGOFXbytNsiDerhv3hDmhiWpAb5MkPmtehB6jK_OtrHLiXhcJH96NKKoX_cxgFrXX-YX6naTWEppbZQNL310awBHmbkOTbMobFOWyOXnxpnu4G5EX2e0lrwG2g_sVSBA5ST82Muyqi8JhKKmrD7CZLlf6n2VxJpaKFq00CDDKwzNKkYNW4ucYlxUiflqvfW0ahOBnX3bZmRqMRuqOKFSPw1oJW6RCWZta0MYlP331pX3sGDXFQkxezuBM5t7s4SCymAHtRVOU5ze3A3DH-jJhPu2BJomzsXMkOlvqtu9KIrRdY-_t6hnd8YuCDjporpJ2Eke6WVpS4AmpRKXftvM3BXNWWOcgdGwAR-WKD1o88imIpIVX9CSbQ-CJaw3QZMU7Tg7Y7MaRFJ9OAZ_TURv1QiX-BuxFA8-rXC_hZKx5_B2uXQeHqMl4vD55bJRV_3K53CV27etXcMn2l1FoPfMpW4toapa19w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض نمادین به جنایات رژیم صهیونیستی در مقابل سفارت این رژیم در واشنگتن
🔹
فعالان ضدجنگ در واشنگتن با اقدامی نمادین، خشم خود را نسبت به استمرار کشتار غیرنظامیان در نوار غزه نشان دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 613 · <a href="https://t.me/akhbarefori/682238" target="_blank">📅 15:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682237">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
از کمیسیون صفر تا خانه‌های بازسازی‌شده؛ اسنپ چطور پای زنان ایستاد؟
رکنا نوشت:
🔹
حمایت از زنان در سال‌های اخیر از سطح کمک‌های مقطعی فراتر رفته و به یکی از محورهای مهم برنامه‌های مسئولیت اجتماعی شرکت‌ها تبدیل شده است.
🔹
در این میان، اسنپ اعلام کرده است که با اجرای بیش از ۱۶ طرح در حوزه آموزش، اشتغال، سلامت، توانمندسازی و حمایت اجتماعی، بیش از ۵ هزار و ۴۰۰ زن و دختر را در نقاط مختلف کشور تحت پوشش اقدامات اجتماعی خود قرار داده است؛ اقداماتی که از حمایت از زنان سرپرست خانوار و ایجاد فرصت‌های شغلی تا آموزش دختران و حمایت از زنان آسیب‌دیده از خشونت را در برمی‌گیرد.
🔹
یکی از تازه‌ترین اقدامات اسنپ، مشارکت در تهیه و بازسازی ۲۰ خانه آسیب‌دیده از جنگ برای زنان سرپرست خانوار در هرمزگان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/akhbarefori/682237" target="_blank">📅 15:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682236">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e305080a.mp4?token=EFXyIeQc_hsNl7-l4Ut7lXYYWmyf10c9_MkeTmB-2ICj6UlwD4Zq2qiygT4n_JRS0TvJuVtFzoOG1OAdwzpRxDB9JFREpDcHx6TfuNax8YywOmuF3SJmmXerm7793RbQNDUajSkmXi2t9ScUiroCMX4VGhrUfKAH4ssfFIoP0ZSlmLCgv3v2zgFkgUNGMsu8nDmOJmAaWTyxBYkhI60-YJpnOpdSAz8p5tNC-2z_tXHjcIPDBqgHnB-xnKOWVGbBEslG_bdTUypLfxDCLo1_UvXHDsS2hQ33VtakeY71YQd8Rmk3tQRX4aDe5g2UTfT1G4yknCcofFrN9Nbq-z57_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e305080a.mp4?token=EFXyIeQc_hsNl7-l4Ut7lXYYWmyf10c9_MkeTmB-2ICj6UlwD4Zq2qiygT4n_JRS0TvJuVtFzoOG1OAdwzpRxDB9JFREpDcHx6TfuNax8YywOmuF3SJmmXerm7793RbQNDUajSkmXi2t9ScUiroCMX4VGhrUfKAH4ssfFIoP0ZSlmLCgv3v2zgFkgUNGMsu8nDmOJmAaWTyxBYkhI60-YJpnOpdSAz8p5tNC-2z_tXHjcIPDBqgHnB-xnKOWVGbBEslG_bdTUypLfxDCLo1_UvXHDsS2hQ33VtakeY71YQd8Rmk3tQRX4aDe5g2UTfT1G4yknCcofFrN9Nbq-z57_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفتار صحیح با مواد غذایی به زبون خودشون
😀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/akhbarefori/682236" target="_blank">📅 15:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682235">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff225759e5.mp4?token=nAwJXPuNHAHSU2GiBeN9HzBEtqCQ89IFgzZa43kMKDfYKagQ3r2uRVDLDDMJ7PLe0jAH206qT0T71a6blG1xlQyoUR-9KetrGnpkJFdGTKU4MvOzFjz42_M4n48mHALz-7RVXm8rGuGl-OJiE-VLZYdP2YBVFOajGnFjf9s_2YpoGSr78TOASblm9Zw3Qx0bw36di20vYnwhTFFz5T6Fc-hGOiXX8LCGi1W5d1KuEz2dzcjaLEEjSQpi_lVido2zjjdePULA59jvd7LWuwum9DqmGBkEbM9qGIBmxHzYT0KEcRctUroI6NSuQa9snabodDM66Yb6BLVFYtAneKrGmYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff225759e5.mp4?token=nAwJXPuNHAHSU2GiBeN9HzBEtqCQ89IFgzZa43kMKDfYKagQ3r2uRVDLDDMJ7PLe0jAH206qT0T71a6blG1xlQyoUR-9KetrGnpkJFdGTKU4MvOzFjz42_M4n48mHALz-7RVXm8rGuGl-OJiE-VLZYdP2YBVFOajGnFjf9s_2YpoGSr78TOASblm9Zw3Qx0bw36di20vYnwhTFFz5T6Fc-hGOiXX8LCGi1W5d1KuEz2dzcjaLEEjSQpi_lVido2zjjdePULA59jvd7LWuwum9DqmGBkEbM9qGIBmxHzYT0KEcRctUroI6NSuQa9snabodDM66Yb6BLVFYtAneKrGmYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: حامی اصلی ما در مسیر مذاکرات، رئيس‌جمهور بود
🔹
وقتی آمریکایی‌ها درخواست مذاکره را مطرح کردند، پزشکیان معتقد بود باید از همین طریق راهی را برای پایان جنگ پیدا کنیم.
🔹
انتخاب قالیباف در تیم مذاکرات به‌پیشنهاد رئیس‌جمهور بود و حتی در صورت‌جلسه‌ای که تهیه شد پزشکیان اصرار داشت که «باید نام آقای قالیباف به‌عنوان مسئول مذاکرات نوشته شود تا من امضا کنم».
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/682235" target="_blank">📅 15:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682234">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab02ee3fce.mp4?token=L_xmhFgKRm1LBG5hTUS28hENEnJuVArdaJp0PWPNq4OOyovih4RFmtoEd_B36FZ7XNi0l63pkIqR4rdZ87S29OU0qrnzwO1Abf_j1oNXlcWrb2a-WDFpc1PQPOs6nMNebbfh66jke-9i_LZEVtYzWlv47nWm9tjYC7GScMG0SoMaI5VeQz9ftXOQCKY0STG7g39Hzr962ZigekHT3LOypGxbX0Zm0kqaXRrRi7kwoiLhIoHqCdZsCSYnBV42vU4i9SkUGLzq7gOpcgZDXDxe-30eYjt0NUPFoBUSl8Xcu-FaQTSOCgX3vQ5yt0BLSMaOD2oZ9wbfIVTjpdWOYmkgOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab02ee3fce.mp4?token=L_xmhFgKRm1LBG5hTUS28hENEnJuVArdaJp0PWPNq4OOyovih4RFmtoEd_B36FZ7XNi0l63pkIqR4rdZ87S29OU0qrnzwO1Abf_j1oNXlcWrb2a-WDFpc1PQPOs6nMNebbfh66jke-9i_LZEVtYzWlv47nWm9tjYC7GScMG0SoMaI5VeQz9ftXOQCKY0STG7g39Hzr962ZigekHT3LOypGxbX0Zm0kqaXRrRi7kwoiLhIoHqCdZsCSYnBV42vU4i9SkUGLzq7gOpcgZDXDxe-30eYjt0NUPFoBUSl8Xcu-FaQTSOCgX3vQ5yt0BLSMaOD2oZ9wbfIVTjpdWOYmkgOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط با یک نخ و سوزن لباس‌تون رو به سبک پینترست استایل کنید
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/682234" target="_blank">📅 15:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682233">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
منابع خبری لبنان: پهپادهای رژیم صهیونیستی امروز حریم هوایی بیروت و ضاحیه را نقض کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/682233" target="_blank">📅 15:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682232">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdjXD4kKWAEs2VAZpLFur8Ovp5-cSp6edJfHkyy4yfIZ-coCj5YEv-pHH1-UpeXG3feE4-6Itj6ztBPyCc1BlfitBAPP2yJelOMRnKFg9L3UkdD8ZHMfQlJC0HTdGJnkZY7MhtQEgBVHDoDhcAXQsBedWz23xmCTqxkE9hQAk9uzxhIDM8LrnTbx_tese0XQIz6vP4yR81D3uI-Rv6PsQO0pe4hIV8CtS8b4JjIXxy9PrL96u21-udHP2gIUw9UdvFbyZ0Gpnm1uag71PXVI0L2VORM_pgsGP0v7ezAW4mqhyY6250Hspe8iS6EFs0LAi3i2qo5yXA6CSJyE7te1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
صندوق نقره «یاس» چهارشنبه ۲۸ مرداد پذیره‌نویسی می‌شود
صندوق «یاس» جدید‌ترین صندوق نقره، چهارشنبه ۲۸ مرداد ساعت ۱۱:۴۵ از طریق تمامی کارگزاری‌های بورسی پذیره‌نویسی می‌شود.
در حالی که میانگین حباب صندوق‌های نقره به ۱۲ درصد رسیده است، این پذیره‌نویسی سرمایه‌گذاری با حباب صفر را فراهم می‌کند.
⭕️
اطلاعات بیشتر و آموزش شرکت در پذیره‌نویسی را اینجا بخوانید.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/682232" target="_blank">📅 15:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682231">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeXJKvB9KXSbyQ_X1n6J7dW9G_lqqnzie9JKpXef70DgNf3vO2-3IbOVdGa9plSJ0L_1bBFX-9G37A7se38c59n8cO5lFAEmnOxITiDdvL9LTw7twzAjgT3oSzrIZ9B1ZJZjDpIHF4ThcEYjekVP5iXPsaHM4-Ukcp_fq3cxfHN3hUcwY7xTZukmFK9y7mSZGxCNqqdu9i0NPO5Oe8ldbgIxI24G2LmzBDcApOBDm-RYN2vJcAMV7av_bt5-aNolgnHYfTUu7z7kAvQiBG9hzZ2xcaPlJs8LfcSaGT8_23z4YeMir6f-EupkaZfVFoQl2gZCmVWaIH3V4E_FWCajgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیاده‌گویی ترامپ قمارباز در تروث سوشال: تنگه هرمز؛ قلمرو جدید ایالات متحده #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/682231" target="_blank">📅 15:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682230">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
حمله توپخانه‌ای رژیم سعودی به صعده یمن
خبرنگار شبکه خبری المسیره:
🔹
توپخانه دشمن سعودی روستاهای پرجمعیت در منطقه غافره در شهرستان الظاهر در صعده یمن را هدف قرار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/682230" target="_blank">📅 15:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682229">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
هیل: جنگ با ایران در حال تضعیف امنیت آمریکا و متحدانش است
نشریه هیل:
🔹
اختلاف با متحدان، کاهش آمادگی نظامی و افزایش تردید درباره تعهدات امنیتی واشنگتن می‌تواند به همان شبکه‌ای آسیب بزند که قرار است امنیت آمریکا را در برابر رقبایش تضمین کند؛ روندی که به گفته تحلیلگران می‌تواند در نهایت امنیت خود آمریکا را نیز کاهش دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/682229" target="_blank">📅 15:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682228">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsqEugslXIdfrF1n4PhB3BwEEXkEPi3iZdBksV7wpU7TeSh7dqTgr1zrwOnfSFupRCHrTo98EPuC5mAnRQkl0nZ0kvMWwUlJf8yRT0LjpT3zYq__YxsbGNpaMnvCX48Rz3MouZjgKcVZs1cjQ4KoGHhTfa2laQiPHZrTbm4Ji1U3FK9AEAceSUGSdA8IdGg2jp_-F0rN-SK0wJ52WoGXqNz7Efsy2hfq16BOfgi54c5DGTWeeoC1iUvVWkGtSUncFsiZF4FWWrbDI6l3SqCJrTXFvBaa0vIi1DsCh_WtPAPLmgun1lbpEl7hQCMEpnn-3vhSHLr9Fvr5M7Tsx2YZeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیاده‌گویی ترامپ قمارباز در تروث سوشال: تنگه هرمز؛ قلمرو جدید ایالات متحده
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/682228" target="_blank">📅 14:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682227">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">قطر: تلاش‌های کنونی بر تنش‌زدایی و بازگشت به یادداشت تفاهم متمرکز است.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/682227" target="_blank">📅 14:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682226">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6Nh_zFGSTX4a7Ogix0pee2vF2V5-Z3jYxWzTLYyl6WY31vWF88siV4EzdWkypUsvQU6FJkq7CMaZpaP2WLBL_dzRLUWi3fo-7mtE-HQIQpSxcJJ5E-aCA-A8mv97VK9iGHmfmyQmf49iZ8OCrj6e5HcIwgsHuXdaHsINDG9N3-zhCODVUfMdHvjtJbbl_Ryk4iOZNGh2sF2gXyPRHgNx-O1twmJK3_g3E2V5LFcdTjDkxL84XVm-pJshYn2AdVMMN86mipyyyRAlQnLf7hf76x9m9A38sI4MotmS_gFgG8hfdLrneX0oXvzmDr3dPEGXy6ulZFJsZYWeVSsdI7giQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفتگوی خبرنگار و ترامپ خرفت که مورد توجه کاربران قرار گرفته است
🔹
خبرنگار: شما حالا پنج ماه است که در جنگ با ایران هستید.
🔹
ترامپ: «خب، ما بیست و یک سال در ویتنام بودیم.»
🔹
خبرنگار: «پس شما به آمریکایی‌ها دروغ گفتید که آن را ظرف دو روز تمام می‌کنید»
🔹
ترامپ: «ساکت باش. تو یک خبرنگار جعلی هستی»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/682226" target="_blank">📅 14:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682225">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تا زمانی که سایه جنگ وجود دارد، افزایش قیمت بنزین نخواهیم داشت/ در زمستان قطعی برق نداریم اما قطعی گاز بیشتر خواهد بود!
رضا سپهوند، سخنگوی کمیسیون انرژی در پاسخ به سوال خبرنگار خبرفوری:
🔹
قبل از سال ۱۳۹۸ صادرکننده بنزین بودیم اما حالا به واردکننده تبدیل شده‌ایم. نظر دولت و مجلس این است که فعلاً شوک قیمتی ایجاد نشود و تا زمانی که سایه جنگ وجود دارد، افزایش قیمت نخواهیم داشت.
🔹
بر اساس جلسه وزیر نیرو با کمیسیون انرژی، قطعی برق شهرک‌های صنعتی از دو روز به یک روز در هفته کاهش یافته و قول داده‌اند که از اول مهرماه قطعی برق خانگی نداشته باشیم.
🔹
بیش از ۷۰ درصد برق کشور از نیروگاه‌های حرارتی تأمین می‌شود که سوخت آن‌ها گاز است. به دلیل تبعات جنگ، بخشی از تولید گاز کاهش یافته و ناترازی بیشتر شده است.
🔹
برای فصل سرد تمهیدات لازم دیده شده تا سوخت مایع جایگزین گاز نیروگاه‌ها شود و ذخیره‌سازی‌ها انجام شده است. ان‌شاءالله در زمستان قطعی برق نخواهیم داشت، اما قطعی گازمان بیشتر خواهد بود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/682225" target="_blank">📅 14:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682223">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473515205c.mov?token=vpbiRFyWpAarax-1namjN5CyWzYgzD6QTz3uOUi5JvJ3PjEHEVPNwMDCSqY3lBcy-1Q_6y7J5BtqH8WpN7-R0Lbsb3HkoJOOYl5w4cHhBUzbrGttHEO0elfap4a7l1tZoDeRTVUZuYLjJ4BJ7lV3Xb3rp4SQjlMXMlunnHJfFvOmzPSmxCAzEoZYTy63YEOXrdwa1UuSR9mk2G3LCO4zkUTXoORp8PSRWndGRgLTpEA590C643fOZjk-bOjE9HoOoJKO_ihRvDSLJvBw9gZ1SQ5wvFypZoVYBZ6qqfsAHjl4d08kJWbSUMqgSpVXBGKMR3yWx040aXnLKZdiefsA9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473515205c.mov?token=vpbiRFyWpAarax-1namjN5CyWzYgzD6QTz3uOUi5JvJ3PjEHEVPNwMDCSqY3lBcy-1Q_6y7J5BtqH8WpN7-R0Lbsb3HkoJOOYl5w4cHhBUzbrGttHEO0elfap4a7l1tZoDeRTVUZuYLjJ4BJ7lV3Xb3rp4SQjlMXMlunnHJfFvOmzPSmxCAzEoZYTy63YEOXrdwa1UuSR9mk2G3LCO4zkUTXoORp8PSRWndGRgLTpEA590C643fOZjk-bOjE9HoOoJKO_ihRvDSLJvBw9gZ1SQ5wvFypZoVYBZ6qqfsAHjl4d08kJWbSUMqgSpVXBGKMR3yWx040aXnLKZdiefsA9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروگاه خورشیدی ۱۲۰ مگاواتی منطقه آزاد ارس در آستانه افتتاح
🔹
عملیات اجرایی نیروگاه خورشیدی ۱۲۰ مگاواتی ارس تارلا امین در منطقه آزاد ارس که حدود یک سال قبل آغاز شد، این روزها به پایان رسیده و آماده بهره برداری و اتصال به شبکه است.
#روایت_توسعه_ارس
#منطقه_آزاد_ارس
arasfz.ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/682223" target="_blank">📅 14:23 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682222">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
بقائی: ایران وضعیت خلبانان ارتش را از مجاری دیپلماتیک پیگیری می‌کند  سخنگوی وزارت امور خارجه:
🔹
از روز اول که مطلع وضعیت خلبانان شدیم پیگیر آنها هستیم. ۲۵ اسفند اولین مکاتبه با صلیب سرخ در خصوص پیگیری خلبانان را انجام دادیم
🔹
مطالبه روشن کردن وضعیت خلبانان…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/682222" target="_blank">📅 14:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682221">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
آتش‌بس هیچ
🔹
آتش‌بس ۶۰ روزه میان ایران و آمریکا در حالی به پایان خود نزدیک می‌شود که به دلیل بدعهدی‌ها و اقدامات آمریکا، از همان ابتدا نیز چندان شبیه یک آتش‌بس واقعی نبود. در طول این مدت، موارد مختلفی از نقض تعهدات و افزایش فشارها مطرح شد و همین مسئله، آتش‌بس…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/682221" target="_blank">📅 14:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682220">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
تپه استراتژیک؛ چرا رژیم اسرائیل و حزب‌الله برای هر وجب از «علی الطاهر» می‌جنگند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/682220" target="_blank">📅 14:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682219">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قطر: تلاش‌های کنونی بر تنش‌زدایی و بازگشت به یادداشت تفاهم متمرکز است.
🔹
بنیاد شهید:  آمار شهدای احراز شده جنگ ۴۰ روزه، به ۳ هزار و ۱۶۸ نفر رسید.
🔹
معاون سیاست‌گذاری پولی بانک مرکزی: تأمین منابع مالی پایدار کالابرگ در دستور کار دولت است.
🔹
پارس جنوبی برای گاز زمستان سرپا شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/682219" target="_blank">📅 13:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682218">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/183aafb25a.mp4?token=inEXx0F4OYZS5RnXQqUKycp-4vo7l0xVrnVdrDc-K0K1k9p-c13crCAFdjJZydKuHLZ7eRnB4BdOxn5YLPgVL36wT1IQig-IKgbLe_XxXVIZV4BXURtCeeOTfmuVa9F7IF6hf2s0xfe2cqvDvvIUfWvGMv_iovhTLM-vFsNXu1NZBDgCi77n6d4O2orbuq2lV_-_mKgGKtu2Kw91h91nmrDdtlc42HNDhIkh-TCQ0n7-aMe4iMzPNc0DENkH7CkipK-b-ZTDwHqzMBHNB0TWD841dnkegNOQ-OjiLjXQ_ayfY2nuvu0kGIhTZ2a7gqizktsyfTaK1qJtU5ECaIIoTTIRiXehAj0_wIKgwnOfOy-0aquMulNpVGHRtMnJfZz4ufQkXezLsgmY_JomG7MijZx1uTZ7BnfY_JxEp66NFXO9jiBz7kiVmou4XHKoFmJmK2iTP-z2_qMi5KEqM1Avd_V20dkFjSc4R-kN7hZH562NrXVaX52dk785FL9CIJq7UwHHMQYQU088ovcoSMTvxRFnehRdl0mLSLNDyrpPcn36zIDDdktPYvSmRh257Z2tCTm3bOs6dKMlxG69OQYF1_JgJMZ_HN6EXh-2V8oPUNqdvm-XknC6F2WIwZdnVdkjmohF07Sa8j4I8GW20sYOOfMooCxbcNl14XFFH4VJh-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/183aafb25a.mp4?token=inEXx0F4OYZS5RnXQqUKycp-4vo7l0xVrnVdrDc-K0K1k9p-c13crCAFdjJZydKuHLZ7eRnB4BdOxn5YLPgVL36wT1IQig-IKgbLe_XxXVIZV4BXURtCeeOTfmuVa9F7IF6hf2s0xfe2cqvDvvIUfWvGMv_iovhTLM-vFsNXu1NZBDgCi77n6d4O2orbuq2lV_-_mKgGKtu2Kw91h91nmrDdtlc42HNDhIkh-TCQ0n7-aMe4iMzPNc0DENkH7CkipK-b-ZTDwHqzMBHNB0TWD841dnkegNOQ-OjiLjXQ_ayfY2nuvu0kGIhTZ2a7gqizktsyfTaK1qJtU5ECaIIoTTIRiXehAj0_wIKgwnOfOy-0aquMulNpVGHRtMnJfZz4ufQkXezLsgmY_JomG7MijZx1uTZ7BnfY_JxEp66NFXO9jiBz7kiVmou4XHKoFmJmK2iTP-z2_qMi5KEqM1Avd_V20dkFjSc4R-kN7hZH562NrXVaX52dk785FL9CIJq7UwHHMQYQU088ovcoSMTvxRFnehRdl0mLSLNDyrpPcn36zIDDdktPYvSmRh257Z2tCTm3bOs6dKMlxG69OQYF1_JgJMZ_HN6EXh-2V8oPUNqdvm-XknC6F2WIwZdnVdkjmohF07Sa8j4I8GW20sYOOfMooCxbcNl14XFFH4VJh-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاش میشد برگردی آقا...
🔹
بغض و گریه دختر بچه برای رهبر شهید در محفل اربعین قرآنی‌ترین رهبر جهان اسلام در مشهد مقدس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/682218" target="_blank">📅 13:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682217">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
میدری: افزایش مبلغ کالابرگ در دستور کار است
وزیر رفاه:
🔹
دولت به دنبال افزایش اعتبار کالابرگ است، اما میزان آن باید با بررسی کارشناسی و توافق دولت و مجلس تعیین شود؛ چراکه ممکن است پیامدهای تورمی داشته باشد.
🔹
وی همچنین از فعال بودن حدود ۶۹۰ هزار پایانه فروشگاهی و بازنگری در مبنای دهک‌بندی خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/682217" target="_blank">📅 13:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682216">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGRWSy2j5eCbR-6JD7FO20jhZvN9naIhkkTv-GorVcQWhNKxh-G3Vl8HtUdhtVmaY8FVEzRKcMeFo0hX9EMZgZ95D9vz0NRyXPLqZ9psLcCdC0Zsapk_Gnl78Y8ECC79Hbhwck21GBNCHL2eaouKvkpgIJsrkYfmWNyPwuvnz1QEkRW88nEYHhr1WC0YVMAaJZxPB5lQDWkC-nYqhLfZHdbNdHPXvQe25Ns0HJvMQeE0ZK224A1uQHCdYEXXDglmuuK0Sl0Gro0gDqSw2wqUIPKVOljaz_hsXvaWWGylq8VDXCJ40VMz4Z5-QePYtVaCM6JsGcvf2lQmYSkrIdB5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رامین رضاییان به فولاد خوزستان پیوست
🔹
با اعلام باشگاه فولاد خوزستان، رامین رضاییان با عقد قراردادی شاگرد حمید مطهری شد.
🔹
رضاییان در نیم فصل دوم لیگ بیست و پنجم هم در این تیم بازی می کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/682216" target="_blank">📅 13:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682215">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33b3a5c840.mp4?token=ccPmS71X1GszIDxUmHcjuxpd-9cISV9Keq98XYV-lgoUrXO6L17Wo71IDo362utLxRE35G162hoH4l9taGLpCDtqV1OCSFQdvCzQcJaMaFRpa5XEAMx6WwLozPLvFkwOpUOjl6hQUnMpx-kaAurkOMuqFmUz_o52LVxIsN0SvPXRGxnb0fpWonGcxmh4pI8MtqEo7-8PnUFoWjU6pUn6RnMf1zjq_Tvqk62cMiK_q6f2i8yVtVtcFc9_1qs1ymfv4sLF2BgdW4ySgGuYW4HyWtkpmYTKIok_iZl-dd5ks6MB7WfJR4mxo5s7Ug5AZS4Jc1m5gYOXqTBEUQHgdATgog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33b3a5c840.mp4?token=ccPmS71X1GszIDxUmHcjuxpd-9cISV9Keq98XYV-lgoUrXO6L17Wo71IDo362utLxRE35G162hoH4l9taGLpCDtqV1OCSFQdvCzQcJaMaFRpa5XEAMx6WwLozPLvFkwOpUOjl6hQUnMpx-kaAurkOMuqFmUz_o52LVxIsN0SvPXRGxnb0fpWonGcxmh4pI8MtqEo7-8PnUFoWjU6pUn6RnMf1zjq_Tvqk62cMiK_q6f2i8yVtVtcFc9_1qs1ymfv4sLF2BgdW4ySgGuYW4HyWtkpmYTKIok_iZl-dd5ks6MB7WfJR4mxo5s7Ug5AZS4Jc1m5gYOXqTBEUQHgdATgog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خانه‌داری برای آموزش ربات‌ها درآمدزا شد
🤖
🔹
زنان خانه‌دار هندی با ضبط کارهای روزمره خود برای شرکت‌های هوش مصنوعی، داده آموزشی ربات‌های خانگی تولید می‌کنند و ساعتی ۲۵۰ روپیه دستمزد می‌گیرند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/682215" target="_blank">📅 13:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682213">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-vxJbmbH3dvQFZumTcA6crzk216WywcMJ7-ox0zX7uM_omA8FOzLPVj2yU_IhcJcWG-MkjDTNORLjocnNOsCMtLm_2jHZds3pVgNpj60fj2HV1Z5cplwCOSPBAJbtp41oZCQfGMMP7izwD7o2XAWwD-IHVHvZNvbiRKVOzMzAEcCK1A9xhhhuyeMJD9ObadGXcqYJP3NRVZbhw149IrWbm4RkzDEq2jieuA5ZaBKu8U1zMNj4t53JKivx808-q0PhrmT7Z1KT5bJ5pH8axITbBmzItUido1_eFKC3CzieCFbeMYOUhYgSVbF5Nm_bWM_wQtkSct24f6p937SE7Wow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونمایی از دستخط رهبر شهید، سید علی خامنه‌ای بر صفحه اول قرآن هدیه شده؛ محفل ۳۰ هزار نفری اربعین قرآنی‌ترین رهبر جهان اسلام در مشهد مقدس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/682213" target="_blank">📅 13:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682212">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‌
♦️
حمله موشکی یمن به مقر مزدوران سعودی
🔹
منابع یمنی از انفجارهای شدید در استان مأرب در پی حمله موشکی ارتش و انصارالله یمن به پادگان نیروهای وابسته به ریاض خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/682212" target="_blank">📅 13:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682211">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
تکذیب اجرای پرونده پژمان جمشیدی از سوی وکیل مدافع
🔹
وکیل مدافع پژمان جمشیدی درباره اجرای حکم پرونده پژمان جمشیدی: حکم موکلم اجرا نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/682211" target="_blank">📅 13:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682210">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtRu2CDga-WVdiwXVPcATDyoqzvX7f9zWpj5T-OxuX_BC34t_mMZpAkzv5JoPMVPHXGJgE8kqwhXQf3KefVtQ_LQ9_lRItvABxBYk2EC1aswKgCPWeH8K5HJfPRiz6OcPf8mdVdWfinmGA0mZ-f3-H-_uGCpD2mCmSigBJ_LEKBT990-485Ky7FJxLBHC7jblfV4tA20DFnz7cPJyv4nhYrktNW_oHqFrbVnXY8nmcG7ngPAMB7XXmRakG7oGJQtjApAJnXbUAljFm2s_jr6bAKIW5aK369BSgU3x1IqTPA9zDlqZChZAZilqDBBZGek1-oRHHOpYRuRnVuHHp29Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احتمال حمله ترامپ بعد از انتخابات میان‌دوره بیشتر است
🔹
در حالی که برخی تحلیل‌ها از پایان مهلت ۶۰ روزه میان ایران و آمریکا و افزایش احتمال درگیری نظامی سخن می‌گویند، امیرعلی ابوالفتح، کارشناس ارشد مطالعات آمریکا، معتقد است اساساً توافق ۶۰ روزه‌ای میان دو کشور وجود نداشته و آنچه مطرح بوده صرفاً یک تفاهم بدون تاریخ انقضای مشخص بوده است.
مشروح گفتگوی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3238433</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/682210" target="_blank">📅 12:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682209">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
رئیس سازمان ملی مهاجرت: در ایران ۴ میلیون و ۸۰۰ هزار نفر اتباع زندگی می‌کنند که ۲ میلیون و ۸۰۰ هزار نفر از آن‌ها مجاز و مابقی غیر مجاز هستند
🔹
از ابتدای امسال بیش از ۲۰۰ هزار نفر از اتباع غیر مجاز را طرد کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/682209" target="_blank">📅 12:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682208">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f39b672bd9.mp4?token=rfm7joG6tRPnmePClt_yTnjTCpr8ZE2OTQ73b_nhirJL67JgOrn5xDpQwT08s_Ur6wLPsoGza9q02YDkI4kmSB31b-e68PQF1q7ohu_3llor6aPt8R13XCNZAyBhJtoLlT0yO6m5yEnXFXD_3LDCCXXYHOD40Ibe4ImUrwb0BcLvx4z7BKwbTTz3ii8YeJpuaKV7l5LkTU3Difj-ioAWjgF4itvZGnsMztnkbHlxsv2rYyCzfNCjGLwCqBGpwv8aUb4ZFJ-_oGDBcngZ4g9fh_kb7U0EF3lJbrvNZM9Hs_9zwRZE_u9RONLeeA_0vRBVugqHiMh4xyAVaAZ0-bUeWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f39b672bd9.mp4?token=rfm7joG6tRPnmePClt_yTnjTCpr8ZE2OTQ73b_nhirJL67JgOrn5xDpQwT08s_Ur6wLPsoGza9q02YDkI4kmSB31b-e68PQF1q7ohu_3llor6aPt8R13XCNZAyBhJtoLlT0yO6m5yEnXFXD_3LDCCXXYHOD40Ibe4ImUrwb0BcLvx4z7BKwbTTz3ii8YeJpuaKV7l5LkTU3Difj-ioAWjgF4itvZGnsMztnkbHlxsv2rYyCzfNCjGLwCqBGpwv8aUb4ZFJ-_oGDBcngZ4g9fh_kb7U0EF3lJbrvNZM9Hs_9zwRZE_u9RONLeeA_0vRBVugqHiMh4xyAVaAZ0-bUeWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
این روزها با قطعی‌های برق، داشتن یک چراغ‌قوه معمولی کافی نیست!
🔦
چراغ قوه دستی ۸ کاره LED Torch
هم چراغ‌قوه است، هم پاوربانک، هم ابزار نجات!
✅
نور LED پرقدرت
🔋
قابلیت شارژ با USB + استفاده به‌عنوان پاوربانک
🧲
مگنت قوی برای اتصال به سطوح فلزی
🔨
چکش شیشه‌شکن اضطراری
🔪
تیغ برش کمربند ایمنی
🚨
چراغ هشدار برای مواقع اضطراری
🏕
مناسب قطعی برق، خودرو، سفر، کمپینگ و نگهداری در منزل
❌
قیمت قبل: ۱,۴۹۸,۰۰۰ تومان
🔥
قیمت ویژه: فقط ۹۹۸,۰۰۰ تومان
🚚
ارسال به سراسر کشور
💳
پرداخت درب منزل
👇
قبل از قطعی بعدی برق، این ابزار کاربردی را تهیه کنید.
https://memarket24.ir/product/brief/30291/180124/</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/682208" target="_blank">📅 12:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682207">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a268a17b9e.mp4?token=NZjNgDpTxVEW9KA62PdhkpGKLpf7w8d3XdVFjCzCiUxqa3KeOtDTCp2xnytAcgqxO32hRwUHliCwhkGEfd9kvcXD2AEJLQQsdeuYrEP4UGiD_ZuItz0_FftIc4WOJE315FFsSA5ok_lbqNtxeZ_M5KKMel4UEIxI8W0FWqMQYS4v1cl7ou8atrFf8Hfoi5ARQRS_LHvPJWpJncO4Hx3OVYLF-0lfSesKCGv6mZHAG8IEUscsgUWmHNpyiHB3bSA-CVGu-_g0YDPLn-0ROyveD7_d9zCpgaSlg29ZzScpvw7PmI2vc77m5T-UO7WSErlSrdxx7WA7t8-2RasKmZJ7TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a268a17b9e.mp4?token=NZjNgDpTxVEW9KA62PdhkpGKLpf7w8d3XdVFjCzCiUxqa3KeOtDTCp2xnytAcgqxO32hRwUHliCwhkGEfd9kvcXD2AEJLQQsdeuYrEP4UGiD_ZuItz0_FftIc4WOJE315FFsSA5ok_lbqNtxeZ_M5KKMel4UEIxI8W0FWqMQYS4v1cl7ou8atrFf8Hfoi5ARQRS_LHvPJWpJncO4Hx3OVYLF-0lfSesKCGv6mZHAG8IEUscsgUWmHNpyiHB3bSA-CVGu-_g0YDPLn-0ROyveD7_d9zCpgaSlg29ZzScpvw7PmI2vc77m5T-UO7WSErlSrdxx7WA7t8-2RasKmZJ7TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وسیم الاسد به اعدام محکوم شد
🔹
دادگاه جنایی حکومت جولانی وسیم الاسد، پسرعموی بشار اسد را با اتهامات مطرح‌شده به اعدام محکوم کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/682207" target="_blank">📅 12:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682206">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8SDrhN1bWSnU8oj_Je7J-JIG7XUR5RD2B9d_nRRXkGX4QmtNbRstjTMtd262b4b6cCzxX4UKY4HCda7cM1WmXJ9W8eROb0DkcaabFu7BsPI_ZD4n9ZL7sT_AFzzhYm3SOe-3_1OIIY-4XwU49Ebw-_to9MB89QjmEfAyykGH7vHATTZzWUD9BYQEr9j_4rKhWKD2GjBgCos-ZflmuvjJhYthpu2PM4LNlYY0gdF753AUQSD9wKkazl2_z4xX6Ur0CDm4LqD1Lscc3jcHAGR9lbi3GI8038Z7z1mRsND2fWlbVnRF-YLMlXEoXfPW_nOmqEY9WU2Vzwu2VRT5--ZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس از ۵ میلیون و ۹۰۰ هزار هم عبور کرد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۵۰ هزار واحدی به ۵ میلیون و ۹۴۸ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/682206" target="_blank">📅 12:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682204">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a663516da0.mp4?token=SiNDM4hge-hHHVh6S5JSz-B_6JVSnujA_uahTulwUrZAexu1rPKuBrwLn-RPdQS1xtA59Jg5-zCUWpu9m_zCDgqbI5o0MrxcuIrmsnBEAVCV_HCaMQrmKAW-ztyNz317AcX-FXpaFC3Fq5rC9IqZQb8HXadx6KfnOblMSpMZx2voiNEfXaGu7LyVM5o202y1gx2WMRMIq7V524gVe0CKuie-Sn3sNYHIqmXWTpSmHxvmEHpSbRtlOyuXdqPUs6NgYN5eVmRti3Xj-ikdERXGmq_nlDLx93TDu-Z0RSxOBzz33f6d3kchALjLN-NuaVSZgdp17KDyUu317fTavq5fjkwvgJ-Ss1ZxMPTrzOggiU5arhJMw9sMRR6CV7Rw4P0tJTZ9HKfGa9sJ_v_SNITlFrRZ05gV6cr9uThgQNbWp0wvPDA_alnmfmJB68tPSVVmqP0Q9b7SLb-f1U3qCoZSOvSYtU1RUqd56efnntTmxVgjYnUrzEU_fK1wZ1yAtzfM3QlDocc9KcGqLcsIi6jnAbwBnCRzcH8QSzBa2SdvmubWqenlumWdTj3qi08AWyH6q5GyJlAgDwUINrUWtgDIbHACCZAQcSl0khZdVfsNk2husxzCctAxcYPjXp2v16BARUkX8tsf3lx7JYcLm78HPQ5yytGsaaXtTB3l3iIS4YU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a663516da0.mp4?token=SiNDM4hge-hHHVh6S5JSz-B_6JVSnujA_uahTulwUrZAexu1rPKuBrwLn-RPdQS1xtA59Jg5-zCUWpu9m_zCDgqbI5o0MrxcuIrmsnBEAVCV_HCaMQrmKAW-ztyNz317AcX-FXpaFC3Fq5rC9IqZQb8HXadx6KfnOblMSpMZx2voiNEfXaGu7LyVM5o202y1gx2WMRMIq7V524gVe0CKuie-Sn3sNYHIqmXWTpSmHxvmEHpSbRtlOyuXdqPUs6NgYN5eVmRti3Xj-ikdERXGmq_nlDLx93TDu-Z0RSxOBzz33f6d3kchALjLN-NuaVSZgdp17KDyUu317fTavq5fjkwvgJ-Ss1ZxMPTrzOggiU5arhJMw9sMRR6CV7Rw4P0tJTZ9HKfGa9sJ_v_SNITlFrRZ05gV6cr9uThgQNbWp0wvPDA_alnmfmJB68tPSVVmqP0Q9b7SLb-f1U3qCoZSOvSYtU1RUqd56efnntTmxVgjYnUrzEU_fK1wZ1yAtzfM3QlDocc9KcGqLcsIi6jnAbwBnCRzcH8QSzBa2SdvmubWqenlumWdTj3qi08AWyH6q5GyJlAgDwUINrUWtgDIbHACCZAQcSl0khZdVfsNk2husxzCctAxcYPjXp2v16BARUkX8tsf3lx7JYcLm78HPQ5yytGsaaXtTB3l3iIS4YU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همیشه یادت باشه همسرت نباید در برابر خانواده‌ات احساس تنهایی داشته‌ باشه، حمایتِ محترمانه، پایه‌ یک رابطه‌ امن و سالمه  #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/682204" target="_blank">📅 12:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682203">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d27438302.mp4?token=MBBr-2uG04otA0gpRH95n7_ORlqcsAcUyQUByEJiXP4_OHuX0HEM0uYBf0dVqmyoND24mAt3OCAbvbp8kBZbMUkALfXSj4MF80N06Wdazr_tiwW042idOOMNE1SSfq_V3j5EI950L6gzp4P44pfSiNlzMmvuJH5q0xE3YoF-Em-prjXj-DfNWJfEaJ9cMYYuaX10aUtCUX9pv_itAUsKuXog1EQEC5jJqORLzC3VkLdrn6b1fREXhgfQdjxSnlZWXWkxeDrkc5OzR9OGo_i-SSp-2x56-D2gP3892KRxTXoV1VxGg8tzJcJkqXn1loHW_2k0cWq7eqYFditvcCSjPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d27438302.mp4?token=MBBr-2uG04otA0gpRH95n7_ORlqcsAcUyQUByEJiXP4_OHuX0HEM0uYBf0dVqmyoND24mAt3OCAbvbp8kBZbMUkALfXSj4MF80N06Wdazr_tiwW042idOOMNE1SSfq_V3j5EI950L6gzp4P44pfSiNlzMmvuJH5q0xE3YoF-Em-prjXj-DfNWJfEaJ9cMYYuaX10aUtCUX9pv_itAUsKuXog1EQEC5jJqORLzC3VkLdrn6b1fREXhgfQdjxSnlZWXWkxeDrkc5OzR9OGo_i-SSp-2x56-D2gP3892KRxTXoV1VxGg8tzJcJkqXn1loHW_2k0cWq7eqYFditvcCSjPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جهش کرایه ابرنفتکش‌ها به ۵۱۰ هزار دلار در روز هم‌زمان با اختلال در تنگه هرمز
🔹
گزارش‌های جدید بلومبرگ نشان می‌دهد که هزینه اجاره روزانه سوپرتانكرهای غول‌پیکر (VLCC) برای حمل نفت خام از خلیج فارس به مقصد آسیا، تحت تأثیر خطرات عبور از تنگه هرمز، به مرز بی‌سابقه ۵۱۰ هزار دلار نزدیک شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/682203" target="_blank">📅 12:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682202">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8c1b68c6.mp4?token=AxsADPbaxlKnrq4Ru_QSPrImuMWgIgJNEOzUJ4UUolae4qsQmpPGcU2dpI-Kip3NZvnQbSZx6MkiiNr6cs37OOJJ-lel3vSiJKVJXMSh5sNuu6ryjYKjpdVVhmlSRfjjrsuWAV8RLWbE7qISBSO_7X1Lm_k3Azp1saYx8STueDsUFH4I5RgNWeBsm6pbePqawcgafwFoy64E05dpmfErWdmZD-O8N4qwL3rGhxIxXSHp20WPnJtvr4NEOiJ1yI-nlLyVERgC21pli91nkbFkIyffm1Yy08-k49UPrjmJeRqQFFGPNM0tAaRVVcUzvm9h5OApJUM7ZsICplcq7Fp255bYsOX1DqScGX2gd5RM2D9wwnVkyAkAy_Zi2DDsvYs-gAQXtreTFvR8Q0DsnTM1wqTPSKnp_94GTUvIIgwVytIz0SzNT92yTkVbkc8h2ow1UJ2QP-8rV6eWHu3R4SFUYDVtqzfp-10m-yJeed73kSc_NoIwLAu8iLj9C0omRpg5idfYypas4zUVu7TOJH3OqjnjtO92dRKEoW7zNpfUeAmkPk1yBvWBJYa3fHjCfFQYkW4ikr81lNAR68SHiM_oL9udVB-A7yMKN5oKkdlJcxa3riiCTOMXWYjPGCtGD6dzhIPV16EP6MFP7ymOqUYYsqwtzVQxDxKGKdeKMmKNbUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8c1b68c6.mp4?token=AxsADPbaxlKnrq4Ru_QSPrImuMWgIgJNEOzUJ4UUolae4qsQmpPGcU2dpI-Kip3NZvnQbSZx6MkiiNr6cs37OOJJ-lel3vSiJKVJXMSh5sNuu6ryjYKjpdVVhmlSRfjjrsuWAV8RLWbE7qISBSO_7X1Lm_k3Azp1saYx8STueDsUFH4I5RgNWeBsm6pbePqawcgafwFoy64E05dpmfErWdmZD-O8N4qwL3rGhxIxXSHp20WPnJtvr4NEOiJ1yI-nlLyVERgC21pli91nkbFkIyffm1Yy08-k49UPrjmJeRqQFFGPNM0tAaRVVcUzvm9h5OApJUM7ZsICplcq7Fp255bYsOX1DqScGX2gd5RM2D9wwnVkyAkAy_Zi2DDsvYs-gAQXtreTFvR8Q0DsnTM1wqTPSKnp_94GTUvIIgwVytIz0SzNT92yTkVbkc8h2ow1UJ2QP-8rV6eWHu3R4SFUYDVtqzfp-10m-yJeed73kSc_NoIwLAu8iLj9C0omRpg5idfYypas4zUVu7TOJH3OqjnjtO92dRKEoW7zNpfUeAmkPk1yBvWBJYa3fHjCfFQYkW4ikr81lNAR68SHiM_oL9udVB-A7yMKN5oKkdlJcxa3riiCTOMXWYjPGCtGD6dzhIPV16EP6MFP7ymOqUYYsqwtzVQxDxKGKdeKMmKNbUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: افزایش قیمت بنزین توسط دولت، تدبیر حساب‌شده نیست
🔹
کاهش مصرف باید با بیشترین عدالت و کمترین نارضایتی انجام شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/682202" target="_blank">📅 12:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682201">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
قالیباف: گلایه‌های اقتصادی مردم را به حق می‌دانم اما امروز زمان اتحاد است
🔹
خیابان، محل میتینگ‌های انتخاباتی نیست بلکه میدان‌های اتحاد مقدسی است که باید هسته‌ سخت ۹۰ میلیونی را در خود جای دهد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/682201" target="_blank">📅 12:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682200">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
به کنکوری خانه «این‌ها» را نگو
🔹
شب‌های آخر قبل از کنکور، فضای خانه برای بچه‌ها حکم میدان مین را دارد؛ هر حرف نسنجیده‌ای می‌تواند یک اضطراب تازه ایجاد کند. خیلی وقت‌ها ما به عنوان والدین فقط می‌خواهیم محبت‌مان را نشان دهیم، اما کلماتمان برعکس عمل می‌کنند
🔹
این جملات را پشت در اتاق کنکوری بگذارید:
🔹
«این همه خوندی، اگه نتیجه نگیری چی؟»
🔹
«استرس نداشته باش! اصلا کنکور مهم نیست!»
🔹
«چرا داری استراحت می‌کنی؟ درس بخون!»
🔹
«همه آینده‌ات به این کنکور بستگی داره!»
🔹
«نکنه امسال کنکور خیلی سخت باشه؟»
🔹
«فقط همین چند روز رو هم بخون!»
🔹
«ببین فلانی چقدر بیشتر درس خونده!»
🔹
«از فردا که کنکور تموم بشه، دیگه راحت می‌شی…»
🔹
«فلانی (فامیل) پرسید کنکور چی شد؟ منم گفتم فعلاً که درس می‌خونه…»
🔹
«واقعاً فکر می‌کنی با این وضعیت خواب، رتبه میاری؟»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/682200" target="_blank">📅 12:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682199">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb53b37fde.mp4?token=TEduGOZ_gJpmECCdoY-0-9QDChQGfHOpykM2ephBSNbEUtzfpZdalJnfYikjFEQfrbhBEU8ksG-hQu2daCB_C5ExFee6YhYZHch23ZaUeThXgdx6ZDyc781yHezvIOJhN-EosYWWdzLE2ut9evZYWl-3XuNe_OLRscKKJ8EX-DpOJjsGHYt4JPf6EjfAkzlmQded7QGIanbktQe7EzZeII0sAlJ3D7O4SG51Ih4-NKzbGBRdUPs4_KEpWqaEBGicemXY1FPakasS4OemdyX0aG0FdrQ3kz1ME6z9av2p1XFwHeVGiJnIk9wUoWCcpCx7xpiTAFMdj2pwJCn-GF4HEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb53b37fde.mp4?token=TEduGOZ_gJpmECCdoY-0-9QDChQGfHOpykM2ephBSNbEUtzfpZdalJnfYikjFEQfrbhBEU8ksG-hQu2daCB_C5ExFee6YhYZHch23ZaUeThXgdx6ZDyc781yHezvIOJhN-EosYWWdzLE2ut9evZYWl-3XuNe_OLRscKKJ8EX-DpOJjsGHYt4JPf6EjfAkzlmQded7QGIanbktQe7EzZeII0sAlJ3D7O4SG51Ih4-NKzbGBRdUPs4_KEpWqaEBGicemXY1FPakasS4OemdyX0aG0FdrQ3kz1ME6z9av2p1XFwHeVGiJnIk9wUoWCcpCx7xpiTAFMdj2pwJCn-GF4HEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: گلایه‌های اقتصادی مردم را به حق می‌دانم اما امروز زمان اتحاد است
🔹
خیابان، محل میتینگ‌های انتخاباتی نیست بلکه میدان‌های اتحاد مقدسی است که باید هسته‌ سخت ۹۰ میلیونی را در خود جای دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/682199" target="_blank">📅 12:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682198">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
قالیباف: تنگه هرمز تا رفع محاصره و تحریم نفت باز نمی‌شود  رئیس مجلس شورای اسلامی:
🔹
قبل از رفع محاصره، آزادی اموال بلوکه شده، رفع تحریم نفت و پایان تهدید و عملیات نظامی در همه جبهه ها و دیگر شروط تفاهم نامه، تنگه هرمز باز نخواهد شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/682198" target="_blank">📅 12:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682197">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff311c541d.mp4?token=VMlc4O0ERRS7vmqZv_aiyPFVKUAKGoX3cySLtOLwUtdtHEg93jKQOJP_0We1I4pywLdJNPR5fs3uqwlbid01FEE-WHwOrf6ZBo_jwWKFjJrc2UOMvZcx_6RxFEIRgSu6f4E4liF0KKGOnfxrj8NsWKNeb6uyzovrQ5oBEZD0DWMr7I3PsnC0KIx2-_jYnAuNSBEZ89rvLBTowfBgrEiLe-9M1K2UCrpKycyO2Qlhvb9cXibAHuxZhPHfe81ynN5w8o2ozTIJIzYE0FiFUVTEeMBigl-ueSUzw5G5O-VDr9gvpOs-BafTc9bY4gsISPSrqf7rJzgLFY-8VWF5UVehzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff311c541d.mp4?token=VMlc4O0ERRS7vmqZv_aiyPFVKUAKGoX3cySLtOLwUtdtHEg93jKQOJP_0We1I4pywLdJNPR5fs3uqwlbid01FEE-WHwOrf6ZBo_jwWKFjJrc2UOMvZcx_6RxFEIRgSu6f4E4liF0KKGOnfxrj8NsWKNeb6uyzovrQ5oBEZD0DWMr7I3PsnC0KIx2-_jYnAuNSBEZ89rvLBTowfBgrEiLe-9M1K2UCrpKycyO2Qlhvb9cXibAHuxZhPHfe81ynN5w8o2ozTIJIzYE0FiFUVTEeMBigl-ueSUzw5G5O-VDr9gvpOs-BafTc9bY4gsISPSrqf7rJzgLFY-8VWF5UVehzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: تغییر شیوه‌ کالابرگ  یا افزایش اعتبار آن ضروری است و باید هرچه سریع‌تر اجرایی شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/682197" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682196">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9VMGbRabqwcGNuub2VfvJEsnTAPQnFjKTKJlglGpuOa6rjw_0HQ0vTnK3i1ZyJPnH8yrIHQHr4JEd5_odOLvYEYalilSeIRTZcbXBCqEaR7EQkliTo9kh37aDq2uK8fojEMPPI6J7q40Q4U8vG7OS1T-cspdB6yndsJEJ_gYhJI6Q3ZrgLcY4IBUaYIvmoknO1q2LR2UYX8aBQAfbbyXozN6Qf354RXPsBuvpshlGiSY4feB2_jBzunN05D7Ki7KaLljEHRFDm4MimZewaMkMgjUCpuNzP0VcHD_wjoT10fiaQNbQ3QcR3XE0VxZ0imEyMDevSut29N1dcUctpC6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش هفت‌برابری تجرد قطعی طی دو دهه
🔸
جمعیت مجردان قطعی کشور با افزایش حدود هفت‌برابری نسبت به دو دهه گذشته، به یک‌میلیون و ۲۰۰ هزار نفر رسیده است.
🔸
«مجرد قطعی» به افرادی گفته می‌شود که به سن ۴۵ سالگی در زنان و ۵۰ سالگی در مردان رسیده‌اند و همچنان ازدواج نکرده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/682196" target="_blank">📅 12:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682195">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFeXLppET8m4zG9FRM1gX-uX5AHguZnWMa2_Hi-bAWYbMX3wXFWdAid22ua55rpso0x3YXIj_KIPU7-3RoIUI2M50XuR-3S4yaUwfPFkrvkwzExLQlyrxAMVvS2Klhue7Q1FeCHNNXIDi1Lucfsia_31fD0I-gYjGL2S-dfEZswXK2llRfMaRPSFr7VbhS6py9W0bW5kWGLxTMvanFJpbQSLKtUX0NiTudNW8Y9cmIqhI3Zxrk_Cwfb0Gxyg1ovBOem_hHPg9u3Y1WAsxXyh-4Jod9pnpJXV0v7cpTqJcgiRnYXyG5aCK1mRzLChCuFC3WF0pQ70lUrWqBAESIfp5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیگ قهرمانان آسیا ۲| هم‌گروهی گل گهر با الجزیره، آرکاداغ و المحرق
🔹
به گزارش ای اف سی، در این رقابت ها تیم گل گهر سیرجان ایران در گروه دو با تیم‌های الجزیره امارات، المحرق بحرین و آرکاداغ ترکمنستان هم‌گروه شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/682195" target="_blank">📅 11:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682194">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f696b3e535.mp4?token=ivwPlpe7iz8WF-V48SztgfCwO_Hm3UrjumY2ekilaCZfqwUS7Pd3rmh1yjWUlEb6fK4wzmNX3YlfXfpIzqUdCv6Yet2UMUexRBTjpSF1OBpFtgv5aznHJul9ASptztQ2OfnZV_vER0UVSS6mlXeapWBBZ8EtEWIf4JVXITwExnLXBDsCQ_uHFVtFsOnXNuundkWav_og2ESaIFRA-cxvFhrJbrmAxh47gvP282LA-yG5ltOV2dme_9zIJWtCiEXe2bn0IlI3lhuBaDZNnuIECifa7hK4Xm_-kV_vTRJck2SFv6prpaqEQ95fVXfc_Pkt4yLmHtIOgzIxMqByehGhawTVXWZ9L0uqui-Lhg1pg0bm0S_tcrk_q_UfhU5zP1C8WTt8fmQIBvudvqpgyuVUuUH2HQenIg-Yb0wOlo4Hf1xr1Na4PwtI4v1Ds2hV01zza8mJaz3HygntB8vOAzVKV28VSfuYVfqAsvn1K2djJFg4iBoCJWl7mTJovkL9WWcU60NT1LQaPkPF0aFWIHFsZifhD8y6fogHLwXqnVorBF-WZehUMFn_EW3_xhkDSV1DRK_tSVtEn0R2Sd08QDibWUJrVp3-y7yjXQaPFZv5puzlvIq43AOvo1OvYMzLIu2b3f4BhNsxCE9dJXuW5OQrStlqUQ3gyWSQqiziWTti6E4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f696b3e535.mp4?token=ivwPlpe7iz8WF-V48SztgfCwO_Hm3UrjumY2ekilaCZfqwUS7Pd3rmh1yjWUlEb6fK4wzmNX3YlfXfpIzqUdCv6Yet2UMUexRBTjpSF1OBpFtgv5aznHJul9ASptztQ2OfnZV_vER0UVSS6mlXeapWBBZ8EtEWIf4JVXITwExnLXBDsCQ_uHFVtFsOnXNuundkWav_og2ESaIFRA-cxvFhrJbrmAxh47gvP282LA-yG5ltOV2dme_9zIJWtCiEXe2bn0IlI3lhuBaDZNnuIECifa7hK4Xm_-kV_vTRJck2SFv6prpaqEQ95fVXfc_Pkt4yLmHtIOgzIxMqByehGhawTVXWZ9L0uqui-Lhg1pg0bm0S_tcrk_q_UfhU5zP1C8WTt8fmQIBvudvqpgyuVUuUH2HQenIg-Yb0wOlo4Hf1xr1Na4PwtI4v1Ds2hV01zza8mJaz3HygntB8vOAzVKV28VSfuYVfqAsvn1K2djJFg4iBoCJWl7mTJovkL9WWcU60NT1LQaPkPF0aFWIHFsZifhD8y6fogHLwXqnVorBF-WZehUMFn_EW3_xhkDSV1DRK_tSVtEn0R2Sd08QDibWUJrVp3-y7yjXQaPFZv5puzlvIq43AOvo1OvYMzLIu2b3f4BhNsxCE9dJXuW5OQrStlqUQ3gyWSQqiziWTti6E4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: تغییر شیوه‌ کالابرگ  یا افزایش اعتبار آن ضروری است و باید هرچه سریع‌تر اجرایی شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/682194" target="_blank">📅 11:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682193">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/257319fc15.mp4?token=jXmI2llmQMQOQqi3Jl-tQPba3Ad5yKzUVa1NdZE3-GiVBH6_Myy4oWaUEgC5Dyp5H8Eyb2Qg2tPm4xotqQ028jPrsZO73OSLGwpZHFpL-LdZ5aGWNpebo_Ywh7o_B7CAmOkIzOiVWwI2nUL_LgDgigj98d15qbb9uaVTN8XEX43z-e_0lW-8XE5yrGgQ-sQURJDnGJ8PxDXcvjirQtjejKU5xQSDqPWwWlZXUJ0D_9mcHpcbEfhMHfOrrZRkyDQug5Cy6Uo9XokzYV7kMFLx29PLpxo0nyZl8knM5Goo8Tw3Is7EfInJu7Gi1uXpzvQ3Kjtp0vpFy5fNHoVxtPyCGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/257319fc15.mp4?token=jXmI2llmQMQOQqi3Jl-tQPba3Ad5yKzUVa1NdZE3-GiVBH6_Myy4oWaUEgC5Dyp5H8Eyb2Qg2tPm4xotqQ028jPrsZO73OSLGwpZHFpL-LdZ5aGWNpebo_Ywh7o_B7CAmOkIzOiVWwI2nUL_LgDgigj98d15qbb9uaVTN8XEX43z-e_0lW-8XE5yrGgQ-sQURJDnGJ8PxDXcvjirQtjejKU5xQSDqPWwWlZXUJ0D_9mcHpcbEfhMHfOrrZRkyDQug5Cy6Uo9XokzYV7kMFLx29PLpxo0nyZl8knM5Goo8Tw3Is7EfInJu7Gi1uXpzvQ3Kjtp0vpFy5fNHoVxtPyCGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از جام لیگ نخبگان آسیا رونمایی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/682193" target="_blank">📅 11:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682192">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c0f25f27.mp4?token=UTjAyHX0wtS3WqjuTiNFq-_DSPb97VY31WbXX06g9O7zRPsqGO9Bnay-hUJgRM88iOnNNstqW0Aeuth6GNRbeTFpiGFghN0dosDtHmD5N_jsYM2QqAkbCS-xS0NFaSM9yka2SOaUnqlRZXs9Ko28NeWcFvnSCUqrq1dUOg2yzjy_HiiP13bt2DgsjGuVLmrzijmj_wRq_ef_-H_QvXByVOHJZqnH8kr5m9M-VRNvN8UfLg_6LZCVR6peG0YkUAXUjraNIHHfNwzKsB26jJj1bZFPABY0Is4ECEZsGoawKzmPNI3_7TCpnUQT-NbEgw-nMik-_bnqTWnh1RdCpDY9arxNYUL7_2Y8hSC3KhyJihpfZ4ITGUgZUrLyQa2iz0btq9yCs5zVM4_8_hFRCtqfiSqKRcm5K6D6-hQ7ltpH_mWeAweKX7TEUS4jg-AhZDvxaDezjzUZSmJbvB3NgFIOm1jGgFmKJAigH938qRX1WzP4159Q9OSbHGHP4krI2QXShszf6EA2TN1YXCrBNqSXgx1qivynscSFwndgQjBJXgHKrbskBLRHpuwTXXRnxEtqW8L-hPUfLFJzVJjPyD4QgIE81LfghppW1kqMoKoNu_3mjxd3d3GuCtTGaYbpo3nJTJTpI8q-SWRP_MYbRDyWClSLKUhljc0HsVyAHqgqJos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c0f25f27.mp4?token=UTjAyHX0wtS3WqjuTiNFq-_DSPb97VY31WbXX06g9O7zRPsqGO9Bnay-hUJgRM88iOnNNstqW0Aeuth6GNRbeTFpiGFghN0dosDtHmD5N_jsYM2QqAkbCS-xS0NFaSM9yka2SOaUnqlRZXs9Ko28NeWcFvnSCUqrq1dUOg2yzjy_HiiP13bt2DgsjGuVLmrzijmj_wRq_ef_-H_QvXByVOHJZqnH8kr5m9M-VRNvN8UfLg_6LZCVR6peG0YkUAXUjraNIHHfNwzKsB26jJj1bZFPABY0Is4ECEZsGoawKzmPNI3_7TCpnUQT-NbEgw-nMik-_bnqTWnh1RdCpDY9arxNYUL7_2Y8hSC3KhyJihpfZ4ITGUgZUrLyQa2iz0btq9yCs5zVM4_8_hFRCtqfiSqKRcm5K6D6-hQ7ltpH_mWeAweKX7TEUS4jg-AhZDvxaDezjzUZSmJbvB3NgFIOm1jGgFmKJAigH938qRX1WzP4159Q9OSbHGHP4krI2QXShszf6EA2TN1YXCrBNqSXgx1qivynscSFwndgQjBJXgHKrbskBLRHpuwTXXRnxEtqW8L-hPUfLFJzVJjPyD4QgIE81LfghppW1kqMoKoNu_3mjxd3d3GuCtTGaYbpo3nJTJTpI8q-SWRP_MYbRDyWClSLKUhljc0HsVyAHqgqJos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ
کوبنده تحلیلگر عرب به کارشناس آمریکایی: چرا ایران را متجاوز می‌نامید؟
پاسخ منطقی تحلیلگر عرب به کارشناس آمریکایی در دفاع از ایران:
🔹
چرا از درک واقعیت طفره می‌روید؟! چگونه ایران را متجاوز می‌نامید درحالی که این شما بودید که ۶۰ پایگاه نظامی پیرامون ایران ساخته‌اید، ساخت این پایگاه‌ها از سر علاقه به ایران بود؟! نه، برای حمله و تسلط بر منابع نفتی این کشور بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/682192" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682191">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e99328643d.mp4?token=SaWw1gOrhCPCJ_9LO6xf6KZel-66UsbnBeIPQvRUWA3fJki75Er7ewmLB9m51i5LqmdjhSuxV63rV4PlQfYnJAQIEHQrzl_4knEqOYA3-UBJ2tdF2vi71sYiS6xwcelANEav7TuTl2auqo9T5Xo9pG-wBAHE0LHBSswxzlUnGUl1mHC_n_oDnt9Uud2xPtV7z7LzmLP6608EjGPXco5MGwXok4uFXKZP_pwuxAdeAKjrLBArC83nfYv_aEB45dZilQ865QbKth30zqsLl7Q41QOYlbL9t46hPk6ueIwSDnCe_DxDFMqjEpbRQguZFkQat4xlcUcKK9Vw2BuHDIy0ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e99328643d.mp4?token=SaWw1gOrhCPCJ_9LO6xf6KZel-66UsbnBeIPQvRUWA3fJki75Er7ewmLB9m51i5LqmdjhSuxV63rV4PlQfYnJAQIEHQrzl_4knEqOYA3-UBJ2tdF2vi71sYiS6xwcelANEav7TuTl2auqo9T5Xo9pG-wBAHE0LHBSswxzlUnGUl1mHC_n_oDnt9Uud2xPtV7z7LzmLP6608EjGPXco5MGwXok4uFXKZP_pwuxAdeAKjrLBArC83nfYv_aEB45dZilQ865QbKth30zqsLl7Q41QOYlbL9t46hPk6ueIwSDnCe_DxDFMqjEpbRQguZFkQat4xlcUcKK9Vw2BuHDIy0ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره جالب عراقچی از دوران سفیری‌اش در ژاپن و روایت‌های او از آداب ژاپنی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/682191" target="_blank">📅 11:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682190">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBZ1i3tx4v7J6Kyhbxich6KaujXXyfR4w3k-mKYydaxKYTiiEr1O4IFBobQBlE1DAYllj-LC6VMQuyxxcl_-6rokDMW8CD-PXlqxvsM3bpQVMZQVLJEu80GS4HuTAp9jhK3YGZBJs9rbXX6BR7dCrZPfufoNejKkT-Zm2hTj0Jd-OsOrQqsLPFh5nXPj5e79k2T2n9huLpjNdDGmLL_wGky33klw3mUE3Si4Kzl4eOZWxxdX94O4ZGw7a-4s7qERS5ITD08pXPVYBtlZoleExC795tcr4DUtCwvMTi7WjrlOfxxi7GUmUd9TuniElFf66wHQeHzmqqBnIUGWLTxswA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاریخ ثبت‌نام و برگزاری آزمون‌های دکتری و کارشناسی ارشد سال آینده اعلام شد
دکتری:
🔹
ثبت‌نام: ۳ تا ۹ آبان ۱۴۰۵
🔹
آزمون: ۱۶ بهمن ۱۴۰۵
کارشناسی ارشد:
🔹
ثبت‌نام: ۱۶ تا ۲۲ آذر ۱۴۰۵
🔹
آزمون: ۱۶ و ۱۷ اردیبهشت ۱۴۰۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/682190" target="_blank">📅 11:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682189">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
برنامه‌ای برای افزایش قیمت بنزین وجود ندارد
سخنگوی کمیسیون انرژی مجلس:
🔹
تاکنون برنامه‌ای برای افزایش قیمت بنزین وجود ندارد و تمرکز دولت بر راهکارهای غیرقیمتی است، تعیین
نرخ چهارم بنزین
در حال بررسی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/682189" target="_blank">📅 11:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682188">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/682188" target="_blank">📅 11:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682187">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
ثبت سفارش واردات تلفن همراه آغاز شد
رئیس کل گمرک:
🔹
ثبت سفارش واردات گوشی همراه آغاز شده است، مجوزهای لازم از طرف وزارت صمت صادر شده و سهمیه نیز اختصاص یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/682187" target="_blank">📅 11:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682185">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675abb3bd8.mp4?token=gpoyq1Ha3zAV_PYoipu-5eQB6meVJYE-veRLSYO0mGFnPWJGh9wq5tDqjlmOxJIyU6efijWJuMtuye7RbpFkTP5tJOgJGTNQ5xkpcnwy0tq9CxTVLrTkgGq8h91UtRqfGtLfbnccaa3uvJR2f9U0PvTOA3_OhDr4QUUfPPsGzoTenJ-9jVDCmNqIMH92Q-r4Yh0X3RR2QrL9FBgnf1k-fmMxrMrWu_g61IAXEGIgb0aexc_F4u3r2BJ4mtAAOFPcE7n41sbrTR7mAjdU7Wkhnuemu4Fr8L3w4M2CDl6iGtGVO1cgqpMOilQv4r8VMkZDs5HcltakGvHsgcvsk-w_ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675abb3bd8.mp4?token=gpoyq1Ha3zAV_PYoipu-5eQB6meVJYE-veRLSYO0mGFnPWJGh9wq5tDqjlmOxJIyU6efijWJuMtuye7RbpFkTP5tJOgJGTNQ5xkpcnwy0tq9CxTVLrTkgGq8h91UtRqfGtLfbnccaa3uvJR2f9U0PvTOA3_OhDr4QUUfPPsGzoTenJ-9jVDCmNqIMH92Q-r4Yh0X3RR2QrL9FBgnf1k-fmMxrMrWu_g61IAXEGIgb0aexc_F4u3r2BJ4mtAAOFPcE7n41sbrTR7mAjdU7Wkhnuemu4Fr8L3w4M2CDl6iGtGVO1cgqpMOilQv4r8VMkZDs5HcltakGvHsgcvsk-w_ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دانوب راز سال ۱۹۴۴ را فاش کرد؛ کشتی جنگی آلمان نازی پس از ۸۲ سال از آب بیرون آمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/682185" target="_blank">📅 11:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682184">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مجوز تردد خودروهای مناطق آزاد با پلاک گذر موقت ۲ ساله صادر شده و این مدت تا ۱۰ سال قابل تمدید است.
🔹
سخنگوی وزارت کشور: شعام تأیید کند، انتخابات شوراها تا ۲ ماه آینده برگزار می‌شود
🔹
عمان، میزبان آسیایی تراکتور شد/ باشگاه استقلال: عراق میزبان احتمالی تیم در مسابقات لیگ نخبگان است
🔹
مرغ منجمد قطعه‌بندی‌شده به اقلام مشمول کالابرگ الکترونیکی اضافه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/682184" target="_blank">📅 11:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682183">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OY5DP343jtKH-yqhOvVAThlgs9n33d6gJV2r1uKaSfc7mz5ZiAoGN-LNY5-0jFL4sgDNY4LCRqituQuoqpf0KuDDbnItzpKp4GYpWF3CTt1NLN4BTwlhO0ktgl-ZH1LOTnd6HMjT8g6cBwS9kZPAtn_7uNyDN1XSeE1CCEg8cslAOOIVWxkaWpD51hcezJDL5rRAlWRXtgSahVv3uZ621DpL6GBW3h-8nnHHFFf2wucpSWizSuH0BDCEtDXY-MWIciq4j68QRCIgs8KDr1V_ZpdbovEdBkSx0TzCkQJJyEdBm03j4loof4-_qj-rSHi7S0ekfjUZwckAbCnxn5m94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌ روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره
02191551808
در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/682183" target="_blank">📅 11:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682182">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
اولین تصاویر از ۶ متهم پروندۀ قتل حمیدرضا رجب‌زاده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/682182" target="_blank">📅 11:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682181">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ll13D019e3x-C3k5-8_DGxIuam_TrzsW5tKlhJfdxS7MINXYRdP0wL_fx3Mk3GhQfu4FptT-jOjfhPhzE2pDFi-I5zzY7wixyFgQRBAFbF3ISmJNCxHBRttjDK7l0MlroSVgbtnRk7G4mIogVVuUqoJAYrRCC4v9-vlTfIJ5K352JLs-rVVonlkINwKMMtAo4J-jFuR46hQqwXL1upZeGPJpRXYd2g9QWdAJjvb9i4d72NRi_Oq2Iqo2zdPdC25JPny1ukJufCwmlFYpr0f4WMHJ5YRr_ihc2G5cc1_sWKnRtX5dvDM8aQ8HZ8Suflnhe2HG8x37p5JyOZoZ4DFPww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا بعضی میوه‌های خشک مثل نمونه‌های بازار نمی‌شوند؟
🔹
با رعایت یک‌سری نکات، می‌توان میوه‌های فصل را برای مدت طولانی‌تر نگهداری کرد و در زمان مناسب به بازار عرضه کرد.
#چرخ_زندگی
در وبسایت خبرفوری بیشتر بخوانید و برای ورود به بازار آماده شوید
👇
khabarfoori.com/fa/tiny/news-3238317</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/682181" target="_blank">📅 11:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682180">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
حمله پهپادی ارتش یمن به پالایشگاه آرامکو عربستان در جیزان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/682180" target="_blank">📅 10:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682179">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDvmAHN4_VDJKNoRLWYvid9zmd3ptaUlp5hBqGpwD2d8gvgUnSP6ZSjT3VAk66_bqyvetyd__gJEXNRbXztjdogjJbb5lioUMqUXYkCOxMxtNGBA-4pIJytFEgZ8NMz9mvUH_v2xLEHn5g2XXdMzm4ctzwLQXxdUabohwwgvL81j1yd4VgGA5XZQ8xH4aU4DBrqeplt1mlTNbkOUvCgHHMq0OepBf-Vn6dT_CupPkawu3x331VsGejyMVgDoFeQ5eKTAeUbwGhGB2auYzyADWJQ-lvkGyL9TjzXwDbepq5j4yZTjTWpCqgUnVHTI8F05-4WekcyOqMPHDsnRc4Q63Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
♦️
«هدیۀ آمریکا به ایران »؛ از لاشه F-۱۵ یک قبضه سلاح GAU-۵A به دست آمده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/682179" target="_blank">📅 10:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682178">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a03aca0ab0.mp4?token=rXFirlk1SHO-w511yR-MfiwXXlWQelT0-kH6ZpUZYZDSKfqBOLBuJ2nW8TWG_FuYjWtJN0YmFUPZ-j-XusM6ZJhdJaJ5D4T4s3GSnvDbjkT6EA1KPgCJ8QPfaGgCgAKhv6YY9QUrcDxO3UWJOSnXJr9RaAsqAeAnaTPYf_3nIyEf7FEqT4SELo8vO27GPuKMIPxcd4__Wf0O2AfApCcRilQJJR6V3hTrnyJcPuPppSXuZgZmh7Qf_vhI-wMfLX7EjuWZa-oiMFXyzKIqO-rz-bZjPy6A9IXD9w0yQmtu_5FzWbklEE6jmWvApoLtVF46g6pA_Mfnbka_wXzFCc-H-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a03aca0ab0.mp4?token=rXFirlk1SHO-w511yR-MfiwXXlWQelT0-kH6ZpUZYZDSKfqBOLBuJ2nW8TWG_FuYjWtJN0YmFUPZ-j-XusM6ZJhdJaJ5D4T4s3GSnvDbjkT6EA1KPgCJ8QPfaGgCgAKhv6YY9QUrcDxO3UWJOSnXJr9RaAsqAeAnaTPYf_3nIyEf7FEqT4SELo8vO27GPuKMIPxcd4__Wf0O2AfApCcRilQJJR6V3hTrnyJcPuPppSXuZgZmh7Qf_vhI-wMfLX7EjuWZa-oiMFXyzKIqO-rz-bZjPy6A9IXD9w0yQmtu_5FzWbklEE6jmWvApoLtVF46g6pA_Mfnbka_wXzFCc-H-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردر هزارساله جورجیر؛ گنج پنهان اصفهان
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/682178" target="_blank">📅 10:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682177">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St8fQozW0E1_HuMrMMVyxT2IryxDk2xLumom_MRS-jumrn1BA5YEWspGj0cLUgwJdsjO7CSDHHBpni2Z8DYmRQrdnK1oGwkz1oxdI-hX0IbrkGJwr83HL8Hlnuq0jgXTO9xqAqXAObrsKyT-avGi7-VJpR6qWmpScm2iVsKUrJisWy9W6SM9NiNcFM3ezd_1g8DP8oD_Sw5fHzNaoWC2PyVaZTeloiJjd2RfOBuefWq6znhDRu4X_u7A-T7M3kuh2RscGneW5USHofMtxEs0ETvs3pC8PteRFnZGJ6XPY-Kd3TnPxfQLq7fmjJC8FIpHEGOWaR6HiHJg_zbKty_FXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/682177" target="_blank">📅 10:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682176">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb9f1c65c2.mp4?token=p7CADoHlQu1AW-TfQT5aZpe9ikFiot7oDybspgvie6lA0O_OYILk0SiGnEvVBAnhqjvZn6wRaI2-kz36Wguig4ACJ_YD83svlvD4lntd0h0ej3viN2dnpUKftSvj_xXNfeeg77QtWLfWwSwU3SRGO0-L25gkOCpZ2kmnEVQsDTbDtXhYiM0B-qkDI8eP1ZIzaWQt22my5_r57s1p6PctZwDf8QnN3cxPU7S7FkMHkbEbyZreVtzev1xrnBHuUvcntejP2ULowGdv5S52CsCKkeYil1hbmxOST_xMfKT95J7eZ9cqnvL_Q4QLkTj8WK5tI5zKiIXICJGp1ZYJOdCYVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb9f1c65c2.mp4?token=p7CADoHlQu1AW-TfQT5aZpe9ikFiot7oDybspgvie6lA0O_OYILk0SiGnEvVBAnhqjvZn6wRaI2-kz36Wguig4ACJ_YD83svlvD4lntd0h0ej3viN2dnpUKftSvj_xXNfeeg77QtWLfWwSwU3SRGO0-L25gkOCpZ2kmnEVQsDTbDtXhYiM0B-qkDI8eP1ZIzaWQt22my5_r57s1p6PctZwDf8QnN3cxPU7S7FkMHkbEbyZreVtzev1xrnBHuUvcntejP2ULowGdv5S52CsCKkeYil1hbmxOST_xMfKT95J7eZ9cqnvL_Q4QLkTj8WK5tI5zKiIXICJGp1ZYJOdCYVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره جالب عراقچی از دوران سفیری‌اش در ژاپن و روایت‌های او از آداب ژاپنی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/682176" target="_blank">📅 10:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682175">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxX6GDLBOGAT3IRSZFCVUnC2nuEsvFPDL7Y7nhmvBZ7QTJg342qA1o4XjhmK3MvwaGDw1I3EbzKdlOrlk50D6JsFjqsUPbL14gKNX7SkxUzpJMcoEh0KMOafQ5Gcm5r__IcALTWpFahSc6YYr8_6N1bzyFtfXg0dNJveb7vsJGNjM0X-aMHfQP09NkjUty4HFT9zaVxQrhwSLmC7WPNVzUwz1yvhhj1uyo9kGWE9kdFroax7h09YHX5Up74rnTJMtLI8Z_ZFbq-NzKgvX_tHqu3XjC0FHlda7ova6d63U2K2ug2tv27JZru9xKZxUi9pOkmOU_8cFvaohzzPvFeIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از سوی رهبر معظم انقلاب برگزار می‌شود؛ مراسم بزرگداشت چهلم «رهبر شهید ایران» در تهران، قم و مشهد
🔹
سه‌شنبه ۲۷ مرداد، ساعت ۱۷ تا ۱۹
تهران - مصلی امام خمینی رحمت‌الله‌علیه
🔹
چهارشنبه ۲۸ مرداد، بعد از نماز مغرب و عشا
قم - حرم حضرت معصومه سلام‌الله‌علیها
🔹
پنجشنبه ۲۹ مرداد، همزمان با شب شهادت امام حسن عسکری علیه‌السلام بعد از نماز مغرب و عشا
مشهد - حرم مطهر حضرت رضا علیه‌السلام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/682175" target="_blank">📅 10:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682174">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نمایندگان مجلس از پاسخ وزیر جهاد کشاورزی قانع نشدند و به او کارت زرد دادند
🔹
جانشین فرمانده‌کل سپاه: پدافند ایران بیش از ۲۰۰ هواگرد دشمن را ساقط کرد
🔹
نتایج نهایی آزمون دکتری تخصصی اعلام شد
🔹
قیمت جهانی طلا به ۴۴۵۰ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/682174" target="_blank">📅 10:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682173">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14aa6f057.mp4?token=Tl5qpdqKIplPanspopZNC6FXtRMvf14IzSsVvCxIIXwjmZHrlj9UF_lV0Y-jB3ZGZBQnkVaZp-CSD_mqTrBQk7Hs0phcH4Jz945hNYnYJnNhyxymDUM5EedRyGACGbG5q2614HdLLSQu4Z9KUyQXZH6ZaPm2qac69IjHxKdJ7nn5EQiRS2P7v2tpiNXwmVe2Q4UqEoc2SHk2rNkKRFLGIRqpOhrTzB77IgNQe88rsfoPtBqVw-37-MSh7AyJk0jpDstbYQpLXz1gHphgaoseJuSc5_7_ExmetmbNaw6tVJ93zK5pznn4UUcRqbl6V8wbl-cUgFqn7HQP4LAUH_eXNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14aa6f057.mp4?token=Tl5qpdqKIplPanspopZNC6FXtRMvf14IzSsVvCxIIXwjmZHrlj9UF_lV0Y-jB3ZGZBQnkVaZp-CSD_mqTrBQk7Hs0phcH4Jz945hNYnYJnNhyxymDUM5EedRyGACGbG5q2614HdLLSQu4Z9KUyQXZH6ZaPm2qac69IjHxKdJ7nn5EQiRS2P7v2tpiNXwmVe2Q4UqEoc2SHk2rNkKRFLGIRqpOhrTzB77IgNQe88rsfoPtBqVw-37-MSh7AyJk0jpDstbYQpLXz1gHphgaoseJuSc5_7_ExmetmbNaw6tVJ93zK5pznn4UUcRqbl6V8wbl-cUgFqn7HQP4LAUH_eXNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال و هوای تهران دهم اسفند ماه ۱۴۰۴ بدون آهنگ و ادیت
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/682173" target="_blank">📅 10:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682172">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIDZMw-te-CmNArElDpTwmeT9ExlqYkWy7ZCfXiV1JKJF1XkIjAt_t8D2dcs40wxQAXYoGGVUxMRR8EiDDeI8joT-sstoM1rVo0_JEEvzuwy0dudWPXDLOAVUtLr1g9DZbObO770ES1lmid4fd7fT3nMpU3XAJpndlMIvjZ8lq-CKWSRLfxGnBkvwaietDa0KPfrLFtPLN84XZXAFoWL3UddKtv3RmPJZvbA2QMrE__mOknUUQ_fWGPxyF7d6BSVuDa2MnU5sYay6JIqlGany6lgqbV0qHBlB188XPovdov3KEbwsVIuY5Ekds0RKvSGCLv1SUIX7Ugz1gbo7e7ugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیگ قهرمانان آسیا ۲| هم‌گروهی گل گهر با الجزیره، آرکاداغ و المحرق
🔹
به گزارش ای اف سی، در این رقابت ها تیم گل گهر سیرجان ایران در گروه دو با تیم‌های الجزیره امارات، المحرق بحرین و آرکاداغ ترکمنستان هم‌گروه شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/682172" target="_blank">📅 10:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682171">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3efaec8230.mp4?token=azPUogLC-Eq699iqVtmgX1bf7l17xMCixytqEBG9ef2cK90-bSHtG-25zKQ59uETvsTmNfaWQNtZH42lXD2H7qgJYVq-QLNt5_GRcePSzdM-J5aWcyNujc9snmYSNBo1Q7AqegaX_r5kXprfnWlAbXQ3kkhtfM8NQU1kvyXeGNa51AnFRfT5USlDZMAmcs1TWJqnfrnAw1869qEHpJpbWqg58iLk8GFnyy4bWSjdJaehfZEL-73T5L0lPSPqk9_6m1IYfnKi69P9pOTndtlJfH01eNeOkf4zzVVpYbkDPapKRuQuNPCcVgpv8vJHl5iBgPlSx30baOI8DLiUjZCLLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3efaec8230.mp4?token=azPUogLC-Eq699iqVtmgX1bf7l17xMCixytqEBG9ef2cK90-bSHtG-25zKQ59uETvsTmNfaWQNtZH42lXD2H7qgJYVq-QLNt5_GRcePSzdM-J5aWcyNujc9snmYSNBo1Q7AqegaX_r5kXprfnWlAbXQ3kkhtfM8NQU1kvyXeGNa51AnFRfT5USlDZMAmcs1TWJqnfrnAw1869qEHpJpbWqg58iLk8GFnyy4bWSjdJaehfZEL-73T5L0lPSPqk9_6m1IYfnKi69P9pOTndtlJfH01eNeOkf4zzVVpYbkDPapKRuQuNPCcVgpv8vJHl5iBgPlSx30baOI8DLiUjZCLLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیاین با عطر و طعم این سمبوسه بریم به شب‌های آبادان
😋
مواد لازم:
🔹
سیب زمینی
🔹
پیاز
🔹
جعفری و گشنیز
🔹
سس فلفل تند
🔹
نمک، فلفل، زردچوبه و تخم گشنیز ‌#آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/682171" target="_blank">📅 10:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682168">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jm1RzNCPZ_bkHkfP-KurkpbEf60pd-xnftOo4fmWrD3Lcx0XpL70VX8w3jq0NorCTviGWfLEq58pxc7-y0oOH7Nl1_itFiXwdAk0Jy069sBEfDDRaSH8wmNkzG8bWkm0A023OHc-naVBWIlhM-d0CkymilFVixujIZC_g9Qma5tf3vVkN2F97nX6eCGCn2GzUVoQJEtUEbEeeAwofqx_vnrhrDWmslTtXHUbxr-BQcWsvh2_GgPuSvboaBSesEB1RVWqhuMZVXEHuf6TguyFmC_8Qyh7LpJV4LN0lAUPpxwWaML-eywEIUtFp8oZOrnlYGggXda_7sr1ovdyQzeGOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQwODZfFiz2rmS02A4rf-NeHVpry6Pm-UWV7GaRA93-He6CbFqZ_T5r-4Vf_0tPW7QCNuigyWb0mzSsHvdpk9wiMSOb7F1oGb9pe-N6IJqZFwcl2Ab7wNl4lqanwCtQG34m3Yd3yEO-Lu7cA3QVEz8U9fisi1BpA54fLkMc5mrmUT3v6RPXuhgXyKxPMafzFCegUzYCS00EjRtFEyNMzm3PnPGzFAIE8BuRLWJRMuM4hMmrgF-A0bbeX7zeZAKnL3ZZsngGifzvJBgXb-vaLDPvglQlcVSAvAdGjtLIiCHlRxdVaBK5IRLB_qJccaRhcaNRp19TAJIyJ18UTF1TlFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFcXy7oufXyhtxOrsuWl8JH3zeQanJE3-Qb08ar9v_xgRQE9gdGkJoQzIKNeGKWwSoRmRXdHFS1B1uDqj4hZgfQuNABNxhL7rvQESpznoqgUdN_zNY4iiBSSud_K64XnxeG1Ho0JrJdgyxt2Ino5IGly6di-GSSToWJ3hC1bYT7zs3pNY5LiKirAz_pqNpRJQkLP19c4SWlz1GjfxmMGncUSYdn8ZtNqJqoierXFrQ97XpksXXl-4A3Erqh_DITsMC5hLx3p9FcDUyU12z8g-LsMe3d7-zLN8hAHEODlWuk5_aApJZ1rPqKhcNMurxHYbQVhc3sKp0kIT6ezA2uyqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از آتش‌سوزی پس از انفجار یک مخزن سوخت در سلیمانیه عراق
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/682168" target="_blank">📅 09:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682167">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e916058f48.mp4?token=k-416ft_oZ3saZ4R4smUQWFPSzyzIA_vrvKu-AhhpOUJ0Nx7RVScJ1aCceWedwTdyIH5wIAbtvkMxmoRL_WiYnILrUw5wxJC3y4koIrJI1QP0XdxfGty-80XFZhbQqQEs4NPJ-A0a35fjVtvWKX0jzrTmMWk1bsL56-xeh3ua4kYVExc5v6SW6IWryGgTHmgWyokVuHz38ft7ZkpbZsjXrreyYrCfcijFROAGRENhCX2YNNKS5s0KAELLLOSRIdmONo0BapbY68rbKBb-09WPM6tWzfEuLGu16hYnhWQjQoFcUMzVAPDw7l8Re2aOCwGT050wKrueZ4TKTDXpZPR-6tr0r2ZNNI4Kf5lF2ZzH-wv7WvCiF1rfvcvCFxjjN-VV0QpRBFIL9_txdioVCWQYM1vMdcW9fHvtk-Z9RoBfzATfq8JsYoUow3dADZZWqPH-v9HIBCuB7NrMuJSD0-DATW6i6l_MYYatcpWSgeeRp2nD9HjzCAkgVGRbuDDXw1XKxfudwHD6hVaWV7DtEm7dzX6PIYg4lZX6u8te1uaw7Fnh_DPJNb6Ni9HjKgtvqzOOyV4TOcvZpeX6iZXFx6HZRXKUpbkHb6PrNbL67mZWOWNYEDxKOwUZRLmOZH2BkElHs7NkmVdsKrXKR_LAWMe6n7SZwilkMbddeKrLCU6MaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e916058f48.mp4?token=k-416ft_oZ3saZ4R4smUQWFPSzyzIA_vrvKu-AhhpOUJ0Nx7RVScJ1aCceWedwTdyIH5wIAbtvkMxmoRL_WiYnILrUw5wxJC3y4koIrJI1QP0XdxfGty-80XFZhbQqQEs4NPJ-A0a35fjVtvWKX0jzrTmMWk1bsL56-xeh3ua4kYVExc5v6SW6IWryGgTHmgWyokVuHz38ft7ZkpbZsjXrreyYrCfcijFROAGRENhCX2YNNKS5s0KAELLLOSRIdmONo0BapbY68rbKBb-09WPM6tWzfEuLGu16hYnhWQjQoFcUMzVAPDw7l8Re2aOCwGT050wKrueZ4TKTDXpZPR-6tr0r2ZNNI4Kf5lF2ZzH-wv7WvCiF1rfvcvCFxjjN-VV0QpRBFIL9_txdioVCWQYM1vMdcW9fHvtk-Z9RoBfzATfq8JsYoUow3dADZZWqPH-v9HIBCuB7NrMuJSD0-DATW6i6l_MYYatcpWSgeeRp2nD9HjzCAkgVGRbuDDXw1XKxfudwHD6hVaWV7DtEm7dzX6PIYg4lZX6u8te1uaw7Fnh_DPJNb6Ni9HjKgtvqzOOyV4TOcvZpeX6iZXFx6HZRXKUpbkHb6PrNbL67mZWOWNYEDxKOwUZRLmOZH2BkElHs7NkmVdsKrXKR_LAWMe6n7SZwilkMbddeKrLCU6MaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگیری ۲ شرور معروف افسریه
🔹
۲ شرور سابقه‌دار که به گفته پلیس با قمه‌کشی و قدرت‌نمایی با سلاح سرد در محله افسریه موجب ایجاد رعب و وحشت میان شهروندان شده بودند، در جریان عملیات پلیس اطلاعات تهران بزرگ شناسایی و دستگیر شدند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/682167" target="_blank">📅 09:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682166">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
رکورد تاریخی کانال ۵.۹ میلیون واحدی شاخص بورس شکسته شد
🔹
شاخص کل بورس تهران با رشد ۲۱۱۰ واحدی به رقم ۵ میلیون و ۹۰۰ هزار واحد دست یافت. این در حالیست که شاخص هم وزن ۷۸۶۳ واحد مثبت شده که نشان می‌دهد مبادلات سهام نمادهای کوچکتر از نمادهای شاخص‌ساز جلو زده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/682166" target="_blank">📅 09:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682165">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47af4c7f3.mp4?token=AZGCY5SUQw18m9tfAJrAHBsJ0qU_TctdcsQuGqwApQv8xMWmdZHiftHJoVxN53tNQMNR0-QZZKVb25JsUrojAO8EOR3I41qApN2bVPJCmcJSfU53XLHpz5Djym5YEg0de6vlUfT5mHBD-0w3o1OLyqipgJra5UdKgxg8Oukzqk-dZQSVo4rMkBAV3gT8ehdCXO0Y58eRYH89H-rQ4skVMvTkqeLUqBGtvvD2DLQOx94Wyyv61bxLNu-5V_cFXbLvbcjvcobk6xKDtpDpIgYU0L0eZ1VTYknSciroPvASrgiEinqHtSNy7nxGVhWaC6bmE0VRAgTBiWJSUZ9tDE1ugA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47af4c7f3.mp4?token=AZGCY5SUQw18m9tfAJrAHBsJ0qU_TctdcsQuGqwApQv8xMWmdZHiftHJoVxN53tNQMNR0-QZZKVb25JsUrojAO8EOR3I41qApN2bVPJCmcJSfU53XLHpz5Djym5YEg0de6vlUfT5mHBD-0w3o1OLyqipgJra5UdKgxg8Oukzqk-dZQSVo4rMkBAV3gT8ehdCXO0Y58eRYH89H-rQ4skVMvTkqeLUqBGtvvD2DLQOx94Wyyv61bxLNu-5V_cFXbLvbcjvcobk6xKDtpDpIgYU0L0eZ1VTYknSciroPvASrgiEinqHtSNy7nxGVhWaC6bmE0VRAgTBiWJSUZ9tDE1ugA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخریب منزل شهروندان فلسطینی در جنوب الخلیل
🔹
نظامیان رژیم صهیونیستی منزل مسکونی «یاسر أبو صبحة» را در منطقه «خربة الفخيت» واقع در «مسافر يطا» در جنوب شهر الخلیل، به طور کامل تخریب کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/682165" target="_blank">📅 09:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682164">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
همچنان بخشی از سود سهام عدالت ۱۴۰۳ پرداخت نشده است
فارس:
🔹
براساس اعلام شرکت سپرده‌گذاری مرکزی، بخشی از سود عملکرد سال ۱۴۰۳ شرکت‌های سرمایه‌پذیر سهام عدالت هنوز به حساب این شرکت واریز نشده و در نتیجه پرداخت سود عملکرد ۱۴۰۴ نیز فعلا در دستور کار نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/682164" target="_blank">📅 09:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682163">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
سید عباس عراقچی: خیال باطل «تسلیم بدون قید و شرط» محقق نشد
وزیر امور خارجه:
🔹
کسانی که دنبال تسلیم بدون قید و شرط بودند، در فاصله کوتاهی پس از آغاز جنگ، التماس مذاکره کردند.
🔹
ما با اقتدار جنگیدیم و با اقتدار هم مذاکره کردیم. باز این تعبیر را عرض می‌کنم که بسیاری از وزرای خارجه به من گفتند: شما هم جنگ را بردید و هم دیپلماسی را بردید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/682163" target="_blank">📅 09:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682162">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">#چند_خبر_کوتاه
🔹
عراقچی: مصمم هستیم مدارس ایرانی خارج از کشور گسترش پیدا کنند
.
🔹
ادارات بوشهر چهارشنبه تعطیل شدند
🔹
خنثی‌سازی مهمات عمل‌نکرده در محدوده پایگاه هوایی بوشهر آغاز شد.
🔹
انفجار در نزدیکی مرز لبنان با فلسطین اشغالی/۶
شهرک نشین زخمی شدند.
🔹
زمین‌لرزه‌ای به بزرگی ۵.۷ ریشتر جنوب مکزیک را لرزاند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/682162" target="_blank">📅 09:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682161">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b3492a78.mp4?token=bYYzEWIck2YCKkraJ17AYBfVy3TOSp7wk1JcLdS2SR44MLnQ4mrZVPIes6pl6VtTMAW2_m0q8ZLRZsi8mzY4mYJnEMeCyiTSqdlAk0MUNJ63JlyC6ICN6RFLIBgze42r2RxsJRmZo7o_u__azFFGoTpe0vyn0HNI8WQMKP7xZylajP7Z4nXc4cavxtlqbCYHDaN9TnVX1mLwgLRjFasMN-yQN-tLvVGGBLo-2dm5Kefna16YgIagwQS1D5PnYelod4mI41CMvkXDoYYdaCBwPyQLJfNLKcWX_fw0TqLH7oqpgixBc8sHoml-ETOTt6XDaI61pDXOesVi-gh9nB7McA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b3492a78.mp4?token=bYYzEWIck2YCKkraJ17AYBfVy3TOSp7wk1JcLdS2SR44MLnQ4mrZVPIes6pl6VtTMAW2_m0q8ZLRZsi8mzY4mYJnEMeCyiTSqdlAk0MUNJ63JlyC6ICN6RFLIBgze42r2RxsJRmZo7o_u__azFFGoTpe0vyn0HNI8WQMKP7xZylajP7Z4nXc4cavxtlqbCYHDaN9TnVX1mLwgLRjFasMN-yQN-tLvVGGBLo-2dm5Kefna16YgIagwQS1D5PnYelod4mI41CMvkXDoYYdaCBwPyQLJfNLKcWX_fw0TqLH7oqpgixBc8sHoml-ETOTt6XDaI61pDXOesVi-gh9nB7McA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساحل شیب‌دراز قشم از آلودگی نفتی پاکسازی شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/682161" target="_blank">📅 09:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682160">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJ12_5NoHhU4360VxNLfPQ7x2GqPTDG8ClRtzf8aNU5jIvtLn61ckxFyseOsUKUtuPjhERNu_gHHXNWBgyxKi-XxO_k2w0grmS4aw9dK9_2EVa5X9Bzel2QRZ9FDMyYTcAZNc1glZ8mERRP0CusDB89pCaPnmmhY9NuHZfhTKHUuF_hxjCbKm6ghPukqyEh6xB5fYn6j1YKfefXXS-3urVNJhsUGAPjeGEeikVau-CEZ2gpcyWRNCfzJ9zckXfL_Ulpwb4Tz7Mxq6i5iwdsPTgkPeBua1l7SGfGqdc-2vk717tQ89QijgzhSyRym7S77MwGt0bag5FXnzF6_DohVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روغن‌های آغشته به مواد روانگردان به مقصد نرسید
🔹
پلیس فرودگاه امام خمینی(ره) از کشف ۱۹۸۰ گرم روغن آغشته به ماده روانگردان شیشه که داخل چمدان یک مسافر جاسازی شده بود، خبر داد. متهم به مراجع قضایی تحویل شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/682160" target="_blank">📅 08:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682156">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d4b1d33fe.mp4?token=BJfheCkK0HdCkIEROZP3cd5WwQfKipNB6-w1nCUauocPrwXzm6o6HG_T17XD2NCYvqiho5wE9KfyHEhcAG7zfbJ_R1YSZmzVKC_atmm9yWLgBVFeVBE5BFQ3EbUd7JyrrKkDcLv6eVlE_rc4Jj5dfwDHEGklTQfuhGCJn1G04KpdEkpnx4aaJFQ1_yO6_y63vk7k4BSgGidMzVokE3B-EA971CBFR6AOb53p3wL_KPphdJWjroJiSShxxzL5QCS4CFI0_kOLlkCaSs_8ogRumG_Sej2SV_jgdTU3P33KUhc3IQhxcgeUtfa_Q_72pjAhws5TTDRcE4ZdVR8q3tlROQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d4b1d33fe.mp4?token=BJfheCkK0HdCkIEROZP3cd5WwQfKipNB6-w1nCUauocPrwXzm6o6HG_T17XD2NCYvqiho5wE9KfyHEhcAG7zfbJ_R1YSZmzVKC_atmm9yWLgBVFeVBE5BFQ3EbUd7JyrrKkDcLv6eVlE_rc4Jj5dfwDHEGklTQfuhGCJn1G04KpdEkpnx4aaJFQ1_yO6_y63vk7k4BSgGidMzVokE3B-EA971CBFR6AOb53p3wL_KPphdJWjroJiSShxxzL5QCS4CFI0_kOLlkCaSs_8ogRumG_Sej2SV_jgdTU3P33KUhc3IQhxcgeUtfa_Q_72pjAhws5TTDRcE4ZdVR8q3tlROQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات «سوپرمن» اینجاست!
🔹
یک شرکت چینی از ربات انسان‌نمای پرسرعت «سوپرمن» رونمایی کرده که می‌تواند ۲ متر به‌صورت ایستاده بپرد و به سرعت ۱۲.۶۶ متر بر ثانیه، معادل حدود ۴۵ کیلومتر بر ساعت، برسد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/682156" target="_blank">📅 08:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682155">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df9764dab.mp4?token=heDMmn9z0jCtRyFlxdKPYBAHJTnShsLgu8q1yCp8XSNrcvSkkkYscLMBzFjwoBl3_1Dd2kr_5-p7VTuMhlZUBWRlAaH-8FQ9yGpt-6YZ6GGTxpU7vw1kpoWGT-kuw8u7fjdz753PeQhRdRiIcXcSMxK3NVXQiUEPJgD6JWtnEsx-OXKSIEwwAkY_va8VimJyOuKM3Y7N0kNLRV69xrmHwc5YFy6oKwN368VFexZ0mqTsOfIugeO-eyGsuLw-hKpF2kn5V1sWm-wQWGiVXhkbAcnO4GiMd4XECmShR8TQIZjBeIpVshhkK6pKCvLrhOVF5OnyyjIZJnpzczF9fFHYajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df9764dab.mp4?token=heDMmn9z0jCtRyFlxdKPYBAHJTnShsLgu8q1yCp8XSNrcvSkkkYscLMBzFjwoBl3_1Dd2kr_5-p7VTuMhlZUBWRlAaH-8FQ9yGpt-6YZ6GGTxpU7vw1kpoWGT-kuw8u7fjdz753PeQhRdRiIcXcSMxK3NVXQiUEPJgD6JWtnEsx-OXKSIEwwAkY_va8VimJyOuKM3Y7N0kNLRV69xrmHwc5YFy6oKwN368VFexZ0mqTsOfIugeO-eyGsuLw-hKpF2kn5V1sWm-wQWGiVXhkbAcnO4GiMd4XECmShR8TQIZjBeIpVshhkK6pKCvLrhOVF5OnyyjIZJnpzczF9fFHYajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراسم افتتاحیه فصل صید ماهی در دریای جنوبی چین
🔹
چین پس از پایان ممنوعیت تابستانی صید، در ۱۶ آگوست فصل ماهیگیری در دریای جنوبی چین را آغاز کرد و ده‌ها هزار کشتی راهی دریا شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/682155" target="_blank">📅 08:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682154">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
هشدار هواشناسی: تداوم ۴۸ ساعته گرمای غیرمعمول در سراسر کشور
🔹
کارشناس هواشناسی، از تداوم حداقل ۴۸ ساعته گرمای غیرمعمول در کشور خبر داد. طبق نقشه‌ها، دمای جنوب به ۵۰ و شمال شرق به ۴۰ درجه می‌رسد؛ همچنین رگبار در شمال و وزش باد و گردوخاک در نیمه شرقی پیش‌بینی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/682154" target="_blank">📅 08:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682151">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8064346f28.mp4?token=Icfxmpz_uJGio4HJmB9cOSbN5rLf1OEwpJ5f9SSbORDWTLXWyBicgYmSEMwz9MpIm1-SCKv2utiijnlcHnK5_8fLHEx-TQi1LnD9vnHvuSUgpDKDmUF7QgJ-hLgYemfDH9Ttduh91EZCtDMsQng3EU08gBqCl3TbriJk4CTjoLl5vEIi6XtM2Xf37-oktNBMw7O12RjUK_WUJxACxi6GfGzT7KyCP-8ldeBhO9l4zPCLAOZP7oOQyBDKuar8xTe99fzFxYT2o0F-N9uPiWmBXV_pkJ3OxI1uD56LSFq5-qn7gqzkg8zbTbrB5Sc3TmJtI1APqXGr1xQfFrjG-kT3sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8064346f28.mp4?token=Icfxmpz_uJGio4HJmB9cOSbN5rLf1OEwpJ5f9SSbORDWTLXWyBicgYmSEMwz9MpIm1-SCKv2utiijnlcHnK5_8fLHEx-TQi1LnD9vnHvuSUgpDKDmUF7QgJ-hLgYemfDH9Ttduh91EZCtDMsQng3EU08gBqCl3TbriJk4CTjoLl5vEIi6XtM2Xf37-oktNBMw7O12RjUK_WUJxACxi6GfGzT7KyCP-8ldeBhO9l4zPCLAOZP7oOQyBDKuar8xTe99fzFxYT2o0F-N9uPiWmBXV_pkJ3OxI1uD56LSFq5-qn7gqzkg8zbTbrB5Sc3TmJtI1APqXGr1xQfFrjG-kT3sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ حرکت ساده برای اصلاح فرم بدن و صاف ایستادن #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/682151" target="_blank">📅 08:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682146">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e116f039a2.mp4?token=vvdqd-PnKA09OEZ8fgQF7iPFK3EAUx6_Qz3nwJf92pvbGJilrmGcU7SytkqLplyMSbOgtORMQoo2h7S60FXmLvJ3vP0ZAkTEWTvJjey4e8w5Xu5wlDRQg6eIOhOF8uYzVTDmvGYyjKS_Zv65NjHaqx4aJ4ahPbX7knCWJQnYLwQGKnfoXCUgwRyRjdIfNLHvJjBdcXnIR6OYWu5XFj4qahtA3D-6WH0_1wqSIDg3Jgq2-fP4jsDyi9JF4xH_uQTm5rHypnHdrIADndCCZlVGTjjlggTTcI0jyUw_x4_lkuJtAzQX28oFYmFEEQEi5CDe6ofsz-3f4Ejddfws7AEe-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e116f039a2.mp4?token=vvdqd-PnKA09OEZ8fgQF7iPFK3EAUx6_Qz3nwJf92pvbGJilrmGcU7SytkqLplyMSbOgtORMQoo2h7S60FXmLvJ3vP0ZAkTEWTvJjey4e8w5Xu5wlDRQg6eIOhOF8uYzVTDmvGYyjKS_Zv65NjHaqx4aJ4ahPbX7knCWJQnYLwQGKnfoXCUgwRyRjdIfNLHvJjBdcXnIR6OYWu5XFj4qahtA3D-6WH0_1wqSIDg3Jgq2-fP4jsDyi9JF4xH_uQTm5rHypnHdrIADndCCZlVGTjjlggTTcI0jyUw_x4_lkuJtAzQX28oFYmFEEQEi5CDe6ofsz-3f4Ejddfws7AEe-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از آتش‌سوزی پس از انفجار یک مخزن سوخت در سلیمانیه عراق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/682146" target="_blank">📅 07:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682145">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0CNNnYUUTfXSHpmF2jCgoQn1A44Lj2vfCOXWfkVc8J1ejqmJU7Pqy7tQSgCdWtFjSMvmDJdDeR2qk6ylhcuZSU6QQLQH4r8MUn-gv0woZ-tGSn6j6GRkL61XqQUT71YhcTqOEcanbS0otdHzaNtyMs9LPy9w2aPTQTVeCRSjwa44uOlufIm19Je1J-ZIkGmMZeXSPov2tt9w8pxAL0Y8U2Go8t3MOzPIcTkK5A8gXmCjpixl9tVMtvw4hFVvRDB9MiAs4_RlZZ_zhXrRqWIJKNGIF2f0XfoZBp4BJy4yj1pmzZp4sXZ2JJLO5iEuv44N6pSjTH-NmPeyBrBTI4-kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار: شما گفته بودید اگر عمان در مسیر بازگشایی تنگه هرمز مانع‌تراشی کند، «حسابی آنجا را بمباران خواهید کرد». آیا می‌گویید دیگر صبرتان در قبال عمان، که یک شریک راهبردی است، به پایان رسیده است؟  ترامپ:
🔹
فکر نمی‌کنم آنها رفتار خیلی خوبی کرده باشند، اما…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/682145" target="_blank">📅 07:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682144">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
شروط ۴گانه «کتائب حزب‌الله» برای همکاری با دولت عراق
🔹
خروج کامل نیروهای دشمن آمریکایی از زمین و آسمان عراق
🔹
اطمینان از عدم بازگشت نیروهای دشمن آمریکایی و رهایی از تصمیمات سیاسی و اقتصادی از هژمونی آمریکا
🔹
حذف نیروهای ترکیه که شمال عراق را اشغال کرده‌اند
🔹
منحل شدن نیروهای پیشمرگه، زیرا آنها مسلح‌ترین شبه نظامیان و خطرناکترین برای وحدت عراق هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/682144" target="_blank">📅 07:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682142">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQhzuTg9r-t9lNfcB-WUg47WbBCpT0dR92PsDPEAKWxWWD8oYYCcRjlUz1xPs6Z3JeYXc0u-HclAdZrDomGAyCt5nuRn2O308MXk7Ae8nYuRJLPIg35QS9BPqGgruOn3bdVKDDwYlhIFZER1cOGL6RCZy_DQH0sjMtNirTy-d5rLwEpyvY5L7WfFn8Lowe0JP1D3QYfs4tMrjq867L28qSIlzGUQkgKNXNuWmHFXnU8ewezZG4dsg5PJIE_OFD3xg_2xmNYkpq7-Yq8OEhineTK0pf2G8UkVlbkp70HVySDc6Td71sFxfZ5fvx3CkfiDCqC9YfQK_JZzxIvRsgoXkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۲۷ مرداد ماه
۵ ربیع‌الأول ‌۱۴۴۸
۱۸ آگوست ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/682142" target="_blank">📅 07:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682136">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru5EKm0er9KJ3553A2V7fa2dmqDAjzfWDe1Rlr_--By02llkNj9vaF2KJR2ryvzb6le-pqwPsM3W-jpIk1xwYLqhNl1ZK6gxVvTtH6oMloN4qAWlKunC9dCpDZRZCWCbJW7hAksEemyjeV4as4xBCYx2Va3pAFLA_dy5xuuBeGtZr6JavIoft6A1NdJD998-mCajEHsvk7QPBMjpH6rBkUzlfL6SE9HIfYUzLsu4INtKOcikF7p_UR9M1y-DuzRkYh6VeG8tsF_apsHPbgWsh35LhwvarGvfqRqQ-Dp80kPoHlR2xDrXOBw5VJ7egbiL25wW3qiAl1WGXqAVb83NUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید ترامپ با عکس کیم جونگ اون: هی دونالد، ما رفیقیم... مگه نه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/682136" target="_blank">📅 01:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682134">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrbAd7TmmnmORmNSXWRpIYNn4qIr9LRi37NSawP6wUSsk2xmbchRvMA-irlRxxz_vdng55nQ1Y3_9N3qeI-wylzyojRwDJpQlBSy_zCTQuH9oiHy5D-cCjDMBrZHJBDSQBaotTnFM-hTVBJvl1z078oUoxz3CTworsfSHkh0z_wWXjpwNKwrk7n26VZvP29LFxV7Qy9SNFbou3-1ZY41FtTPtqJm9pFbvxNPKEyyYwLmoiwAKK0AAhjbXekcpUbidH1rVBMRAQHcpZiqo7qZMC1ZPKW224ECNz0RzMt3xGrTty4WUWeGglc59vbsW7vEpkWTgK5wcmopTchRwSuTPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله به نفتکش یونانی پس از بارگیری نفت روسیه در دریای سیاه
🔹
بر اساس گزارش های منتشر شده،‌ یک نفتکش یونانی پس از بارگیری محموله نفت روسیه در دریای سیاه مورد حمله قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/682134" target="_blank">📅 01:13 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682132">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vozNR94ns3lXc-LpI3stJp4PjobtaD0VVUx066BTbKOX36QIcwnB44tCjYk-aqhVx_NxWaXseo-m8yp8WGy4YaajFqHXHSZJbWC73_MQRJXC1EWZ7A-3ZGVaqcwPCM20bvHDnASvob1wtCbsrKnih6WsLx9rHnQ9m8hru54C4J_vgmFYbgDQdIANIS7Ut03SPrY8UZCpMspFuTYbHWPqXa51bvflSjic-2Sqm-JmAc6dKzbvSqN02uA8Iip7in-ZM54CwbwIIono9pR_pIcxt07EXPTB_8odai8_u_iNqIe3UZJjDSEC3gd4KZk_55GNrW90ZKWxM_M0UKlknYNA8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشتی حامل سلاح عربستان در باب‌المندب منفجر شد
🔹
یک فروند کشتی باری با پرچم اندونزی در منطقۀ راهبردی باب‌المندب، واقع در جنوب یمن مورد حمله قرار گرفت.
🔹
این حمله در حالی رخ داد که کشتی مذکور در همان اسکله‌ای پهلو گرفته بود که پیشتر نیز هدف حملات مشابه یمنی‌ها قرار گرفته بود.
🔹
یمن اعلام کرد این شناور حامل تجهیزات و محموله‌های نظامی متعلق به عربستان سعودی بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/682132" target="_blank">📅 01:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682129">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4ChHloVO6zTY-b3CS4lymrnAxY_ZvyHpVQoP4TRrFKfBqyCI55lsJnD_8FdavfVn64b6_5Ue74LmLwwQigfWc0UqZDL3VzgBDEQgvTaK6WoVGcrZ-myNeGsfNOX1MJHRhF0KRbqyckI8YGkZLjKtmxJlUAxKSttxExIGP2zM5VEl7nrpYzDTJQxKJoXtWFZ8d1puyM9He9DRcfjkqwu3_I0dNcpbRLA4oZIXmkMBvS9qJr0wujSHDfC36VyJJIPNU7MjLWv7QR2SgSdDf4uVoi-E9G3gDqJcFf3KnZB0X5Ux3NuuDP_jjtWxF44zKIPoXyvp-ZSTu1HsB3nzSsERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
﻿
اینجا اسپانیا یا پرتغال نیست، اینجا لاهیجان عروس گیلان
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/682129" target="_blank">📅 00:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682127">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4pliuGLUWS8lEce0gfp5-dt_S4BNWQJNWsxg36ASLdIYqmwVItCgXqernxl7rm4-KE0Qyp72N3MfN4vJfQTJt5mpyQHFYG2LYt4Wf-uwr8vGm5IIdAgUtp_67S6vvQ8TS9xFuxNleUy1Ro_j4H3YnMnwvc3PivvzPDaeUrTlRJYslIhbf2JX70dfADkJ2_Tv_A0Fqm_ibUo-OOAja2NqHKzMhVWgU0E9054CPYT9t22I_Q6k7j6CeV9ZEc4cjLLxfQmwW4ChcBxdaTm3KbvxEZlYIW9z0xIeiMAb2K8MqkRg5AWdRxWNa2SuNWeRXMvHInliVUCAsFirNEyMsrK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دست‌خط رهبر شهید بر صفحۀ اول قرآنی که هدیه داده بودند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/682127" target="_blank">📅 00:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682126">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۸۸ درصد دانش‌آموزان در مدارس دولتی درس می‌خوانند و ۱۲ درصد در مدارس غیردولتی
عبدالوحید فیاضی، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
بیش از ۸۸ درصد دانش‌آموزان در مدارس دولتی و ۱۲ درصد دانش‌آموزان در مدارس غیردولتی تحصیل می‌کنند.
🔹
دریافت شهریه در هر پایه‌ای از مدارس دولتی، به‌ویژه برای پایه اول ابتدایی، کاملا غیرقانونی است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/682126" target="_blank">📅 00:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682125">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر راه: ۱۰۰ فروند از هواپیما‌های ما در جنگ آسیب دیدند؛ آنهایی که عملیاتی بودند و انهدام کامل شدند، ۸ فروند بودند
🔹
ادارات فارس به علت مدیریت مصرف انرژی چهارشنبه دورکار هستند
🔹
صید ماهی شیر جنوب برای ۲ ماه ممنوع شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/682125" target="_blank">📅 00:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682122">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUSgmwWUWmKn5dUrNkVor5LrR7hNHLyLdF2FEyEZVbr7J3xALEqvrAq_hYr8uiRPdEm_WrQle3zbH92kx5ksEs5PQo3aIY9mESk-gw_F1HGfYiNnqzT6VBsc24tm5PwPDuMiEZ3Fb4pPKNcXlF5JDW3rOgQvbd0s2Pi52wiAQsyFmrJdHhvKZAN-lApjUI5SFamZS8sg3tDAgasEW4bgaXlWLcTguaY1-slXvWjrAdrQyR8MDDUZulpgdAr4Wd61JzZ1rIP4XPkkOlkqPePix1domI_9FophcIaS_g25fGvs2nwW9eXX8EnB3_I0xwbymsS984jpx8Z-9X4uKfEzpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/682122" target="_blank">📅 00:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682121">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUgHBB1A3uVSd21j8WLwT0DyD8hizrg9EwpD15nUkySh3EifjudtB6GPv5P_i0u-gSgyNd1Kln_n1uTqK9vAU6OBnyiSRofVRG-fvXxY0yURka4NswApNXznLOPFcYhKOJkDmpfKHccMbIrZVlyLRjBRAP1ZNJ2SV2l9dJ1S1nbsBuAJLMILEhctsiMiOSruKMOJdQqM3hBHl5OcRJY_As3EjQMVPB4FjAYRROcbsHQF0tq0i0fqoitZhGFdopiBkHuRTuLwiDS_9mGn3sfzIBsqJ6JhCOJARnmKJD6dokU35HtgKH4uy0Imeg3nvm1WZEpxizUehtWVmiFc3rFuKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش عراقچی به عملیات پرچم دروغین در کردستان عراق؛ دوستان کرد ما، هوشیار باشند
🔹
هیچ چیزی حمله نابخردانه به دفتر نخست‌وزیر بارزانی را توجیه نمی‌کند. دوستان کرد ما باید در برابر ترفندهای پرچم دروغین که با هدف ایجاد اختلاف میان همسایگان طراحی می‌شوند، هوشیار…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/682121" target="_blank">📅 23:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682118">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBv8NuxD6qR2YNUfV0eP0Be8LhnVwhThTyTi2aoxRifizMD5Fycg0yHQo-NcUwdvB6fvEGdoeZbE5EyqsODrAqVgA9-kkbB-yEDYD0CRKNkAOeRyx4dDYlgUczwV4ZiXn5udvy4o8-gXBwWrEC_WJ1-8Azu4z0OCceFA0_nbzVsYtaquHPpQlsdjEpJGuxG872vxJAfhp7Wm2iGst9i17kPLbzBsPMojQI_qwoy08hCAN_zgvJ7jA7r9oe8J7aVJUXWsywhg4_8Rs4NROP-5fZMWXjngDAQVo9YqEPrskjcq8VtLV1C3nT-bR2iYfKa7KlQaL5wjOiQ6leKhBjFaxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ft_sAVJVyVT-YQRZ9iR_PVMpPPlv-NhGSwMmfo5ZcVUK3WsoHUSVvZ6TweE8kWL0mrtHcmy8t-M2Grj9QXFkmKqvwgCrCJw3JXbg3xOZydeZUxgv7izlrndNIuLsdN49_XrgNKmPJl-hu9cTCL-v8VxbD0vsCgMalm-T61FxNPfSzDu1_DCTb3_Seq_ERiKWPuI-fNAgYwv_0k5-KptiX6kXM3a6_i_ku0pCbPAULvLg9XYONbd_3jaAjRgKwi27TtIODBv28mXDTRyBkEFU_MiYIgpbi_-noCTeoLFSFFwPJL6lMQwyktMkJWaOUMcE1whE1S8z54H-zrUQWrjETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntMSAFNbcHvvjZDAYcw2_vC6c8vsGvNlM7I0u5NWP5yIciFlBabp82NvhgqjCiQid0W3I0AghehWgxQ4AnVZ14D1E-37EKMe_gjqK2pWnt9XCyjykKOn2bfupz3UkHTHcVTCxKtQBDV7yDKJEJr7ysurnDAX6WqZwR0SOwVF0Pl239yHbPDUtAh6S2D9t0J9cviBb0JqZl3lAO-JFcfNZeqSa78wAl0fEoQjhxOx0ZTl6zvY0h5P3sC5CoaeDIt5fHcOnaStVO26D1-Ml-JwvDUZ6T4Ml9dTJuuIet5N62GgilTzia_oLIAySUncdFLShm5kZt9XdYTM_-P2zEWEdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
هر قطره آب ارزشمند است. با کاهش زمان استحمام و رعایت الگوی صحیح مصرف، می‌توانیم در حفظ منابع ملی سهمی مؤثر داشته باشیم.
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/682118" target="_blank">📅 23:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682116">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daf722c295.mp4?token=rOJewH4tv41ldXGJJx393lZNhyFioLNFAjZwKqcJJvtwDZhiE4a5uhUXWOtrafTkfnGfiHSCOkFbfLoZblexigzm0GK3ZsutScfJVYLIQEwAGjR13jR4pFQFs3sxuEsFXSSClgt9VOEV8XF98uqUWg8l7Nl-iadKN2Pwu6WAZ3zEFP5PEY3E2b4pEAk-K3fn6fYfBW36JDH_IxY1cdlhKR35NImfYRiEShoWgCLJET4nX4vZY-5F3rLH-UHX9r-ehJV1-e-lVSH6vqa64H4lec-vEIQS30rX_oPPKjxPEpqwo-W2fJxa2oLZgT8nUyS-Zg7-tWHyos5JlVFP2uG9NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daf722c295.mp4?token=rOJewH4tv41ldXGJJx393lZNhyFioLNFAjZwKqcJJvtwDZhiE4a5uhUXWOtrafTkfnGfiHSCOkFbfLoZblexigzm0GK3ZsutScfJVYLIQEwAGjR13jR4pFQFs3sxuEsFXSSClgt9VOEV8XF98uqUWg8l7Nl-iadKN2Pwu6WAZ3zEFP5PEY3E2b4pEAk-K3fn6fYfBW36JDH_IxY1cdlhKR35NImfYRiEShoWgCLJET4nX4vZY-5F3rLH-UHX9r-ehJV1-e-lVSH6vqa64H4lec-vEIQS30rX_oPPKjxPEpqwo-W2fJxa2oLZgT8nUyS-Zg7-tWHyos5JlVFP2uG9NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک روش کاربردی برای تمیز کردن کثیف‌ترین کاشی‌ها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/682116" target="_blank">📅 23:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682115">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
بورس در آستانه فتح قله ۶ میلیونی
🔹
در بازار سرمایه امروز، ۹۰ درصد نمادها در محدوده مثبت قرار گرفتند و ۵۷ درصد نمادها با صف خرید بسته شدند.
🔹
هم‌زمان، سهامداران حقیقی حدود ۱.۹ همت از صندوق‌های درآمد ثابت خارج کردند و در مجموع ۵.۲ همت نقدینگی به بازار تزریق شد.
🔹
ارزش معاملات خرد نیز به ۲۷ همت رسید. تداوم این روند می‌تواند شاخص کل را در معاملات فردا به سمت مرز ۶ میلیون واحد هدایت کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/682115" target="_blank">📅 23:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682114">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeJ_WujvAREa5EVa6n68w-oxtUVNgDlMNJqYXVFrcKpw3AOZNKk1Gf-VwLJjNoiDnlKDMbbrczi8XCF4iTXLCecE3n68cHzzGlCv5P9BaTVMnWyjNmFRkiSGo1JDEvDUSoh_bSZOhayc2SUCTlnShBNpXEAwvuEnBVTNOgqVdkGtUMUMxRYj8XfcYdNFwL6wjFl6sAzhakGh_j7AeocZ8umvuDGfpffWKfU9llTRu1uqaMAk_ltFjt1EuCfDkn_T1Rj5n5BMDlbEtROPEq5j3dfjTZUxaQCS4Whu3n4pXlEkiALzf5wrBniHLgId7D4hLbqrfKqAUyODpYnU6bG-jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکذیب قاطع پسر ربیعی:خبر خرید ۳هزار میلیاردی شمش فولاد کاملاً کذب است/ پس از شکایت رأی دادگاه را منتشر میکنیم
🔹
صالح ربیعی، فرزند دستیار اجتماعی رئیس‌جمهور، اتهامات مطرح‌شده درباره خرید شمش فولادی از شرکت چادرملو توسط شرکت «تهران تینو» را ادعایی بی‌اساس خواند و آن را تکذیب کرد.
🔹
این ادعا توسط عبدالرضا داوری در شبکه ایکس مطرح و وی مدعی شده است که فرزندان علی ربیعی با خرید اقساطی شمش فولاد به مبلغ ۳ هزار میلیارد تومان، باعث وارد شدن زیان ۸ هزار میلیارد تومانی به سهامداران چادرملو شده‌اند.
🔹
صالح ربیعی صراحتا اعلام کرد: «این معامله اصلاً وجود نداشته شکایت میکنم، رأی دادگاه هر چه شد منتشر میکنم.»
🔹
او در ادامه با اشاره به منبع این خبر، آن را اقدامی هماهنگ از سوی جریانات خاص دانست و نوشت: «اونهایی که نخ این آدم رو از بالا می‌چرخونن و امثال این براشون خبرکشی میکنند، از چین تا گعده‌های خودسر و باندهای فاسد، هر وقت اسم علی ربیعی وسط بوده منافع شون رو در خطر دیدند، بار اول نیست.»
🔹
بر اساس این واکنش، فرزندان ربیعی قصد دارند از طریق مراجع قضایی این موضوع را پیگیری کرده و رأی دادگاه را برای شفاف‌سازی منتشر کنند.
🔹
روابط عمومی شرکت چادرملو نیز امروز ادعاهای مطرح‌شده را تکذیب و از پیگیری قضایی منتشرکنندگان این ادعای کذب خبر داد.
🔹
پیش‌تر نیز علی ربیعی در موارد مشابه، هرگونه سوءاستفاده اقتصادی توسط فرزندانش را رد کرده بود.</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/682114" target="_blank">📅 23:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682113">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c6698ce2.mp4?token=sSbHIJBrVQQHi5QPLyMMQSn_tLWL0ZcKTkETd0PrK5U7A6gmoH2dEkAJ7M9TxwP0cFttiLrm8e9Gx9UYm5b_HpzIIMXDRGRzSdTUa8UydMASsV-Yqi3k1PaPEqMgwNlxDFKYCQfMunkU-5VBAE7L3AggM-9jnEFXhwPqoJjskDWOlGivhamU3vl0NvH8fCas9n2d7VYgn2ZXRHsXJKW0Wrj0m6pdPOeLOsj_TgC3Z87Ta2cmmikj74OFC30qk5sVla7SeE-8fpD9k41JFe9VBeyphRypIQoF-KnTdyZdeH_0m8X2IgbveSjUk3vGaCyzegbOtUYaXMvTiOPNWtV0lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c6698ce2.mp4?token=sSbHIJBrVQQHi5QPLyMMQSn_tLWL0ZcKTkETd0PrK5U7A6gmoH2dEkAJ7M9TxwP0cFttiLrm8e9Gx9UYm5b_HpzIIMXDRGRzSdTUa8UydMASsV-Yqi3k1PaPEqMgwNlxDFKYCQfMunkU-5VBAE7L3AggM-9jnEFXhwPqoJjskDWOlGivhamU3vl0NvH8fCas9n2d7VYgn2ZXRHsXJKW0Wrj0m6pdPOeLOsj_TgC3Z87Ta2cmmikj74OFC30qk5sVla7SeE-8fpD9k41JFe9VBeyphRypIQoF-KnTdyZdeH_0m8X2IgbveSjUk3vGaCyzegbOtUYaXMvTiOPNWtV0lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: تا حالا زیادی صبر کرده‌ایم، لازم شود از NPT خارج می‌شویم و خودتان می‌دانید این یعنی چه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/682113" target="_blank">📅 23:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682112">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
رئیس اندیشگاه بیانیه گام دوم: رهبر شهید، هدف انقلاب را تمدن نوین اسلامی می‌دانست؛ تمدنی که زمینه‌ساز ظهور خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/682112" target="_blank">📅 23:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682111">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f77b99b95.mp4?token=UzBpmxsTGBWTxKcPw59P8gde42_jb6RKpvRWKXvGOEBE2kLZvdcbxngjXllE8lEx1SOwS_5NS8hdqMVczkhS54jekTueKCQLJpm1mNA6qCaQJ3hbrHWSToACRt1nopL9vLE8axIaWmDTZA77i9H6E9bDr3AzUVaqLzIyAKiIT1Sre_4e6cwdOoZcui0YwMui-jFF7_EszX3zoo6HJEd6cdvdwvrdmwArWFgRLKECmTZLvF7gYGXTB_HQ4ndeRPsRj0ZB0t5PKBWrPXppTtqL3EU9Sh0yFwS3_ZB9dl2TH77Ki73Se0L264_mftf-uHMp5jjAGiV9b1Xh9VtYOJLN2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f77b99b95.mp4?token=UzBpmxsTGBWTxKcPw59P8gde42_jb6RKpvRWKXvGOEBE2kLZvdcbxngjXllE8lEx1SOwS_5NS8hdqMVczkhS54jekTueKCQLJpm1mNA6qCaQJ3hbrHWSToACRt1nopL9vLE8axIaWmDTZA77i9H6E9bDr3AzUVaqLzIyAKiIT1Sre_4e6cwdOoZcui0YwMui-jFF7_EszX3zoo6HJEd6cdvdwvrdmwArWFgRLKECmTZLvF7gYGXTB_HQ4ndeRPsRj0ZB0t5PKBWrPXppTtqL3EU9Sh0yFwS3_ZB9dl2TH77Ki73Se0L264_mftf-uHMp5jjAGiV9b1Xh9VtYOJLN2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این قانون مدیریت پول رو یکبار برای همیشه یاد بگیر
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/682111" target="_blank">📅 23:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682110">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06507043fc.mp4?token=uEFawcvUUI1wQ6QhvnLXDxUwy1WKPjmrIWtZZujR-YxeDhPJcabkWw1qgw8hZm5CL-QzpnLaOaA047HsUi1XkVO5WgavWFXZQzYAbqC6yOiNCVef6GOY_-sl-60x6ix7AZDi5gS_ux62I7YP-7m5MqFIEE8CNWSsxMIiEIKB1xHyZAlo7IpvplCI82y4juvlwl_584GXG8Pova3dWV5lzEAQQcjCiavRgqWlheXcEXKgFxcHG58PjRQG3fWPWeEhSlC0If8beEQC9U1BT1aRtjEHhbDLNAV4RjYonreLwOhT68OGr2xvp9tlRDZ1i71nZl1rKyTHUSTOpyTdWDfmFzfPHWykEtlZrIrnFPs5Ff_X9ZRm6qV7TXD1Kw-RBuA4EmhSNEZWb3puqgYs8XPXPo2_Tw8_UH9snzVfiKmkLiwRTnMymH-HXCAuX2HiW5k44gHbVJqXnQVYeZ2Ky0O6YXXuh0K5zzWgLqqYtiyQx6PhnYaKuGhmukzVxQp_nFmhKq08gDIs6pq8kFIKEqNqm7OrL0VB_OwApEv1vLgGtdECOMiOQqjtL6eMmc8OValLwZGBzei20W_iSmsiMPHdxgr3AVkEjEZUUZIjj33NSWnpcLNYrK0vFRZnAfTB6Zw1-wog57S4ye2Mk3E1A0do3HOfQvVOWHuqC1309CXDiOY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06507043fc.mp4?token=uEFawcvUUI1wQ6QhvnLXDxUwy1WKPjmrIWtZZujR-YxeDhPJcabkWw1qgw8hZm5CL-QzpnLaOaA047HsUi1XkVO5WgavWFXZQzYAbqC6yOiNCVef6GOY_-sl-60x6ix7AZDi5gS_ux62I7YP-7m5MqFIEE8CNWSsxMIiEIKB1xHyZAlo7IpvplCI82y4juvlwl_584GXG8Pova3dWV5lzEAQQcjCiavRgqWlheXcEXKgFxcHG58PjRQG3fWPWeEhSlC0If8beEQC9U1BT1aRtjEHhbDLNAV4RjYonreLwOhT68OGr2xvp9tlRDZ1i71nZl1rKyTHUSTOpyTdWDfmFzfPHWykEtlZrIrnFPs5Ff_X9ZRm6qV7TXD1Kw-RBuA4EmhSNEZWb3puqgYs8XPXPo2_Tw8_UH9snzVfiKmkLiwRTnMymH-HXCAuX2HiW5k44gHbVJqXnQVYeZ2Ky0O6YXXuh0K5zzWgLqqYtiyQx6PhnYaKuGhmukzVxQp_nFmhKq08gDIs6pq8kFIKEqNqm7OrL0VB_OwApEv1vLgGtdECOMiOQqjtL6eMmc8OValLwZGBzei20W_iSmsiMPHdxgr3AVkEjEZUUZIjj33NSWnpcLNYrK0vFRZnAfTB6Zw1-wog57S4ye2Mk3E1A0do3HOfQvVOWHuqC1309CXDiOY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیحات کارشناس پدافند هوافضای سپاه دربارۀ هدف‌گیری جنگندۀ اف-۱۵ و بقایای باقی‌مانده از آن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/682110" target="_blank">📅 23:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682109">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
پولتیکو: رئیس‌جمهور چین قرار است برای نخستین بار در ۱۱ سال گذشته روز ۲۴ سپتامبر در سفر به واشنگتن با ترامپ دیدار کند
🔹
انتظار می‌رود در دستور کار این دیدار تحولات ایران و تنگه هرمز قرار داشته باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/682109" target="_blank">📅 23:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682108">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
ترامپ: دنبال تمدید تفاهم‌نامه با ایران نیستیم
👇
khabarfoori.com/fa/tiny/news-3238469
🔹
رامین رضاییان وسط تمرین زنان... ماشاءالله!/ عکس
👇
khabarfoori.com/fa/tiny/news-3238424
🔹
مسمومیت دسته‌جمعی و عجیب شهروندان پاوه
👇
khabarfoori.com/fa/tiny/news-3238237
🔹
معشوقه افشا شده ترامپ، خبر اول شبکه های اجتماعی آمریکا/ چرا ناتالی هارپ برای ما ایرانی‌ها باید بسیار مهم باشد؟
👇
khabarfoori.com/fa/tiny/news-3238475
🔹
از نقطه سبز در گوشی‌ خود ساده نگذرید
👇
khabarfoori.com/fa/tiny/news-3238009
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/682108" target="_blank">📅 23:28 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
