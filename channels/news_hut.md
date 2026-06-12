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
<img src="https://cdn4.telesco.pe/file/rMEG76iajonlWiNtrKEY-iWZS2msMguS0BxNsEoi--vUNeeqQjaWTP3R1bHHXD17OVHycY6NUxXwL5B7aF1Jef_G1JLbC3sOJdhiHlvtizLgr5kySoXnXgjgMGhff19vkN-iMe5Lj5avvCQIdXPK_mqp0BGnVivVCKP4sHnsDuqSKSrihYA1R6Y51_U3rkuaUEHG5qDiMwzXuhrFaDXlp5pDWet15AfRUUQvMCEFEIVJ4pJCBzFfSgEN1x4EwvW5IZIyUy94rc4bRdx5ePy50qS4e5miM-dLqdPrQKgMkSTosiFtR2Dk0_EWsUIkLhp6obUy2kLQPL-VC9il3EimaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 225K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 14:17:28</div>
<hr>

<div class="tg-post" id="msg-65918">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GlTrQvFiRhhPGLpD0MGEtmSfFXKUr8nLBVm592SaHSSsY_ECfNsFKBRLPSw0vYlGvDHoR7HjMMRWPnCfiPzZBXMrsKzDWuN2gXGthb8Njm0VYLoec-1LlHjByZlHyXQBkYAygINSwamGBrI70G_UwKBCyW4erW-oNgiAPtd1yiibNroOJN2_5634ZdN7jaICRyeEvmuIBCdagOZ8mLDkUk17zPxFrC7U5ep-TPd3wuEU2oq60Xm7xSspF_tR8OQfF7TO5osSkh7XlsemRLR0Sf8_L7iICfWIJrQRY7gx4FMFQUt-ogupYgJIKSg97bTKCpeZNBt0h-GWDMm5Xbn1JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EXyQkHVJ_vv4xlZIE7mCJi1RAVid4dTRQFuK3NvFjNNDNo5Jqg108rZ1gup7J-g6QSf9GkRNtPb_WoQgIBk0KyBSndeUM9UOcCEvE-EvYC65UxKaPuwjMc17Z09-g1C1NjvVXrh_34G3tfZ7vJ7WYsBE4S-bPqz13wQIBFsNa7aAb4zQ6C1XWX2PByxFYGewcK5Szi_zv6I94XaCagB9NlWJVNgBUREX1cHCQWvaHBufNIXLvdLGQk4htJuJvIDglgjPBT_GrZIIrcZGYOPYdZtWJ12ZjGioScTl0eGF_xaa0W5C48b8ldq7KuXXrCAqb-ZV6hwm2H1-SxviDsgyMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصویری که یک پرستوی نظام در تجمعات شبانه از خودش منتشر کرده درحالی که چاک سینش پیداست.
@News_Hut</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/news_hut/65918" target="_blank">📅 14:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65917">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aed65f61d.mp4?token=GmS-gKmf_JafpKLmIeQL3HDEpa13qlBrVZuSHuPWh5u8BtqvqTr-HE7U2xjUglXj_5UvpgVNxjH2U3I0zPSFZF1NO8gairBIWzSG2M3s6UmXSdSfDjHmVoKa3lZdl19fqTfKxVw3WDonGlDNFnxNkf0mTDNiFsRHPpk7472f3XbHQIeEFrZw3eKrj6rWAiiop0HZvK-8CClDpibAUfts9v_cTsam06RX_AP3VaeQroRREtdIgClauhLqsMW6auwbhFquaC-SyuRqhFyUeqpvkCkfFtHbAZmWSFQAeh5UOuVfmV4cgAN6p4tOIeTcJzhWu7wKCapvdQ7hLxpT2aNl0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aed65f61d.mp4?token=GmS-gKmf_JafpKLmIeQL3HDEpa13qlBrVZuSHuPWh5u8BtqvqTr-HE7U2xjUglXj_5UvpgVNxjH2U3I0zPSFZF1NO8gairBIWzSG2M3s6UmXSdSfDjHmVoKa3lZdl19fqTfKxVw3WDonGlDNFnxNkf0mTDNiFsRHPpk7472f3XbHQIeEFrZw3eKrj6rWAiiop0HZvK-8CClDpibAUfts9v_cTsam06RX_AP3VaeQroRREtdIgClauhLqsMW6auwbhFquaC-SyuRqhFyUeqpvkCkfFtHbAZmWSFQAeh5UOuVfmV4cgAN6p4tOIeTcJzhWu7wKCapvdQ7hLxpT2aNl0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وزیر ارتباطات: بستن اینترنت امنیت نمی‌آورد. وقتی اینترنت قطع بود، وزیر اطلاعات، لاریجانی، رییس اطلاعات سپاه و بقیه ترور شدند. با بستن اینترنت، جوانان نخبه مهاجرت می‌کنند و این ضد امنیتی است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/news_hut/65917" target="_blank">📅 13:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65916">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‼️
ترامپ از زمان شروع جنگ ۳۹بار گفته با جمهوری اسلامی به توافق میرسه
.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/65916" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65915">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30551bbbff.mp4?token=gmEUSYh1Id2CYMkvQjd8xkRxZrXQy2bCXPa3gcYF3dQ6M4vNMmz_j8zHgk99ip3_UcrVsX2JAZu9AyRQRVOh9IP4svMixYbmd-EyX8W7ikGx-ahiGezaPUv9x0StBTNpzovw51MGtu3HTRSy4_hS10cWspENupaMfoM82LQiPgY_6K8ZDKioFjhAztjVTHUopzDKbOUYXYZPI5xA2jgnP9HhZ3Oq_b3EEShllxMYivkbFe65GuyvaAZ5svQYmRgcZu9OZXwHWyq98heLED-oZLO0UTrPaxdVdhKPU5_UJ_F2rn5jJc1raZ6YvwhevwjqTCWkpZhL1ojHiOdniXIRWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30551bbbff.mp4?token=gmEUSYh1Id2CYMkvQjd8xkRxZrXQy2bCXPa3gcYF3dQ6M4vNMmz_j8zHgk99ip3_UcrVsX2JAZu9AyRQRVOh9IP4svMixYbmd-EyX8W7ikGx-ahiGezaPUv9x0StBTNpzovw51MGtu3HTRSy4_hS10cWspENupaMfoM82LQiPgY_6K8ZDKioFjhAztjVTHUopzDKbOUYXYZPI5xA2jgnP9HhZ3Oq_b3EEShllxMYivkbFe65GuyvaAZ5svQYmRgcZu9OZXwHWyq98heLED-oZLO0UTrPaxdVdhKPU5_UJ_F2rn5jJc1raZ6YvwhevwjqTCWkpZhL1ojHiOdniXIRWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آتش بس در خاورمیانه:
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/65915" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65914">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65914" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/65914" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65913">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=Mh1IShvMz_S4Ag-WdztK-tuqfEX21jReeUcGqMt_tU0LJx-3ZckS3NHviB_VqCTk201JaxumAp8jK080kk53M8fIJnQFrOqUj0NcF09CmMlR-K_0VV2UtbtcKHAPrkE6vowL1XaXc8uNcvEH_wPNI0ulE_kQkdmGgeC_Rs5yLfSBzzT02jDTILERvZrYXuQDx5UQSKu-qzDAmyXawaTHbVZ9z-68E3qNXhU8RvsngUYS-GcI6oSaYCGcOHgPF_6wddoxCWbb1pGIt7Ps5kHZ8IsCKOtImrJwHLVB433kJ5L3d3W3QibfKfDZKMQDrE9eQR8ugvTBjtMXkUe4lGH6uhRiUAP-8DO_NMRwx8tbAuRTqmK7cy2cClIWfCAMvgf8N-59SAX6LL4Lnjs2M4kwNIxNn_8fkCL0yTOo5TMA6dbdegE7JvjvT8-yjML2tv6VjPuOuQl23TqIsB_Y9vvR9cJDAGRIEdl9z81J_Ynjm-TNf2YKTJoW9y3fM7Jgp64U_S0uUSdwBnmEetpb_o1_ybxuFhDiy7vwf6HF4FHY5cbcWnRnBLxUc4phn7KR9JowpOjFBEGfXJBA90SRLQsLV08kxHQWyYLwIuzQsM2dPLmz0C2K81dNJrUaUgpxLUZt5WGTgEbL-YEpujOydN2t45VXujkfkHqfpitY4tbWHeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=Mh1IShvMz_S4Ag-WdztK-tuqfEX21jReeUcGqMt_tU0LJx-3ZckS3NHviB_VqCTk201JaxumAp8jK080kk53M8fIJnQFrOqUj0NcF09CmMlR-K_0VV2UtbtcKHAPrkE6vowL1XaXc8uNcvEH_wPNI0ulE_kQkdmGgeC_Rs5yLfSBzzT02jDTILERvZrYXuQDx5UQSKu-qzDAmyXawaTHbVZ9z-68E3qNXhU8RvsngUYS-GcI6oSaYCGcOHgPF_6wddoxCWbb1pGIt7Ps5kHZ8IsCKOtImrJwHLVB433kJ5L3d3W3QibfKfDZKMQDrE9eQR8ugvTBjtMXkUe4lGH6uhRiUAP-8DO_NMRwx8tbAuRTqmK7cy2cClIWfCAMvgf8N-59SAX6LL4Lnjs2M4kwNIxNn_8fkCL0yTOo5TMA6dbdegE7JvjvT8-yjML2tv6VjPuOuQl23TqIsB_Y9vvR9cJDAGRIEdl9z81J_Ynjm-TNf2YKTJoW9y3fM7Jgp64U_S0uUSdwBnmEetpb_o1_ybxuFhDiy7vwf6HF4FHY5cbcWnRnBLxUc4phn7KR9JowpOjFBEGfXJBA90SRLQsLV08kxHQWyYLwIuzQsM2dPLmz0C2K81dNJrUaUgpxLUZt5WGTgEbL-YEpujOydN2t45VXujkfkHqfpitY4tbWHeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/65913" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65912">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
کانال۱۲اسرائیل:
مذاکرات نهایی آمریکا و جمهوری اسلامی در مورد برنامه هسته ای و مسائل اقتصادی است و برنامه موشکی در آن جایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/65912" target="_blank">📅 12:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65911">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
یه‌یارو بیکاری بلند شده تمام اسکناس‌های کشورای مختلف دنیا رو جمع کرده و باهاش ویدیو ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/65911" target="_blank">📅 12:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65910">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
رهبران قطر،امارات و پاکستان کسانی بودند که مانع حمله دیروز ترامپ به ایران شدند.
سران این کشور ها به ترامپ وعده دادند که توافقی اولیه با جمهوری اسلامی دردسترس است.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/65910" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65909">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9247426e69.mp4?token=rmj4r4wfGQWGRxJIgykI-vtQccwcDC2yDiHspPchOOQTM2QVjcEmmttJ0-BgXJcRallweN-77xM8RfJLlrCOdD4ATA-UPeZ9sJq3G-NaGND0yQrykr-Cy-U1pvMAi7drOk5DHPRa367EFLTL9G95EHyttRUpZ1zP-2S_lgS8kop6RbmCrAffy1G6TLHNgCwsl4A7keAdKzz9zWdSgQtz9gelxUzHBCftliNv6QRjsNZPdwQxOZjJ00OUu1WJzE25IFIjvnXJ9RD_WjkJNBsWXl9co2CKH-TelTQ29pIiYy7PDiccLTaGtmSo0bmfwnytFOs6RmvxP5qu7Xx8wLv4rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9247426e69.mp4?token=rmj4r4wfGQWGRxJIgykI-vtQccwcDC2yDiHspPchOOQTM2QVjcEmmttJ0-BgXJcRallweN-77xM8RfJLlrCOdD4ATA-UPeZ9sJq3G-NaGND0yQrykr-Cy-U1pvMAi7drOk5DHPRa367EFLTL9G95EHyttRUpZ1zP-2S_lgS8kop6RbmCrAffy1G6TLHNgCwsl4A7keAdKzz9zWdSgQtz9gelxUzHBCftliNv6QRjsNZPdwQxOZjJ00OUu1WJzE25IFIjvnXJ9RD_WjkJNBsWXl9co2CKH-TelTQ29pIiYy7PDiccLTaGtmSo0bmfwnytFOs6RmvxP5qu7Xx8wLv4rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو یکی از کشورهای آمریکایی پلیس به یه زن مشکوک میشه که ازش اسلحه بگیره. تهش طی تحقیقات زیاد متوجه میشن اسلحه رو تو واژن خودش مخفی کرده و با تهدید پلیس مجبور‌ به تحویل میشه
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/65909" target="_blank">📅 11:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65908">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
خبرگزاری حکومتی مهر:
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا منتشر شد. این تفاهم شامل تعهد آمریکا به رفع تحریم ها، خروج نیروهایش از اطراف ایران، رفع محاصره دریایی، بازگشایی تنگه هرمز، لغو تحریم های نفتی، و پول های بلوکه شده ایران است.  آمریکا موظف است طرح بازسازی اقتصاد ایران را ارائه دهد و در حالی مذاکره نهایی میان دو کشور باید در مسایل هسته ای و اقتصادی انجام شود، بدون بحث درباره برنامه موشکی ایران. این پیش‌نویس نیازمند نهایی شدن در نهادهای مربوطه است
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65908" target="_blank">📅 11:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65907">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک دیپلمات از یکی از کشورهای میانجی که بندهای متن فعلی را با من بررسی کرد، گفت که «ایالات متحده و ایران در مورد متن توافق به توافق رسیده‌اند»، اما اذعان کرد که هنوز تأیید نهایی لازم است. با این حال، هواپیماهای نیروی هوایی ایالات متحده دیشب با تجهیزاتی به مقصد اروپا به پرواز درآمدند تا برای احتمال سفر معاون رئیس جمهور ونس به مراسم امضای توافق در ژنو در روزهای آینده آماده شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65907" target="_blank">📅 10:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65906">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
⭕️
توافق قریب‌الوقوع جمهوری اسلامی و آمریکا بزودی در ژنو امضا خواهد شد و به‌نام توافق "اسلام‌آباد" نامگذاری می‌شود. طی این توافق یک آتش‌بس ۶۰ روزه که لبنان هم شامل شود، شکل گرفته و ایران می‌تواند با پول‌های بلوکه‌شده خود کالاهای بشردوستانه تهیه کند
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65906" target="_blank">📅 10:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65905">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/215d29fff2.mp4?token=rl-i8GEU6dA5sYtVGslP-HcWt5NXegbGY9ezN4_SZN7T0FJW7_ezSppF5hSbQcYHNXYc093r60xzsyOF6EKERakKJ--myf7SX4Z-AEpMljVIGpwqxSCq-926yP3zc0t5-Y_lnFVSUMe1mAWZZxVCvazK3aNlIAK_OjBXUvL8bR4qlFVUJim1XkDSNPcuZVnTrf0qOhZy4HDkJBlgChY2o89TsBjwxUEzuMN1y2u-qP8FVaCnEA0TPCYFMCcAJaJztBwF1QNU_COJi_rmnH_Azc3bZiu4V4PYJ8vsCxjtUGrAm0NFbO4RdmomdB_f5BEVEveoUl7XH4bxhjMZ10Vn7n6kXdZirr9AD9usra1i4yesXHllt4GlKHpLSxeb-fJcnzyG7AuBjsbw1YyS2owSkx_OcqvucNLHrJGxwQcLeb9zCCsNnZZwQSEBvGcwSTP89wgWMMxx67o1gRhmoKhcfWEqTjF5mo8Ejouaf_s-hwysfeFk9p21tmqg7nQWcLvwT2tiL09PMFFT6Po8HsbE9qvN50WkftXldaV71BJ9wWAjDURswvtDZQaH_lKZDwzXyBvfRrDt9I0wQ7FehHLFbjcMffzug6YeR9wnkOct-9pFor2RFRso9VhdL-GWuHCK7b98wpKKcRL9M3Afc4aZXvFxJVz6ZllEnqO7koEsCjY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/215d29fff2.mp4?token=rl-i8GEU6dA5sYtVGslP-HcWt5NXegbGY9ezN4_SZN7T0FJW7_ezSppF5hSbQcYHNXYc093r60xzsyOF6EKERakKJ--myf7SX4Z-AEpMljVIGpwqxSCq-926yP3zc0t5-Y_lnFVSUMe1mAWZZxVCvazK3aNlIAK_OjBXUvL8bR4qlFVUJim1XkDSNPcuZVnTrf0qOhZy4HDkJBlgChY2o89TsBjwxUEzuMN1y2u-qP8FVaCnEA0TPCYFMCcAJaJztBwF1QNU_COJi_rmnH_Azc3bZiu4V4PYJ8vsCxjtUGrAm0NFbO4RdmomdB_f5BEVEveoUl7XH4bxhjMZ10Vn7n6kXdZirr9AD9usra1i4yesXHllt4GlKHpLSxeb-fJcnzyG7AuBjsbw1YyS2owSkx_OcqvucNLHrJGxwQcLeb9zCCsNnZZwQSEBvGcwSTP89wgWMMxx67o1gRhmoKhcfWEqTjF5mo8Ejouaf_s-hwysfeFk9p21tmqg7nQWcLvwT2tiL09PMFFT6Po8HsbE9qvN50WkftXldaV71BJ9wWAjDURswvtDZQaH_lKZDwzXyBvfRrDt9I0wQ7FehHLFbjcMffzug6YeR9wnkOct-9pFor2RFRso9VhdL-GWuHCK7b98wpKKcRL9M3Afc4aZXvFxJVz6ZllEnqO7koEsCjY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه خبر:
با صراحت میگویم بخش عمده ای از شروط ده‌گانه در توافق وجود ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65905" target="_blank">📅 09:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65904">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6afe375b.mp4?token=pHHov_rkjbth0EWTAtbPbcMV0Ut0arFd3sMkFoPvr9t24KlCN6lKIaBUt_-AkiLnhEdaF9fVjx9H8ah0ScEZlUlRuStu2kgC_1wwrFQJdTbNaGalUMFsXjr-GH11l_nJ3sFBgBH6zjGHQAgEUSWy_zdzaZb_uQL1MPHpPXUJbnFP8zdvlKL9z4lT-mvVu294NYzVq_czLuTIZijnxhUdBbG7Vlpe1uEKWReBdDyM_mpy31oiurErTPriZ0L4NAJM661TgYOa6fc7i29r37f20CPXw2TZIiHe09vFNbNjQnNYK16iVQbRj19ZUn1-iR5lVa3RobNBAh1YThQS28ORqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6afe375b.mp4?token=pHHov_rkjbth0EWTAtbPbcMV0Ut0arFd3sMkFoPvr9t24KlCN6lKIaBUt_-AkiLnhEdaF9fVjx9H8ah0ScEZlUlRuStu2kgC_1wwrFQJdTbNaGalUMFsXjr-GH11l_nJ3sFBgBH6zjGHQAgEUSWy_zdzaZb_uQL1MPHpPXUJbnFP8zdvlKL9z4lT-mvVu294NYzVq_czLuTIZijnxhUdBbG7Vlpe1uEKWReBdDyM_mpy31oiurErTPriZ0L4NAJM661TgYOa6fc7i29r37f20CPXw2TZIiHe09vFNbNjQnNYK16iVQbRj19ZUn1-iR5lVa3RobNBAh1YThQS28ORqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته شده ترامپ بعد دیدن این ویدیو تصمیم گرفته که توافق کنه
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65904" target="_blank">📅 09:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65903">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhhsewN77S3JCMK5--mbQQEXD0bIjeiBHmxqQBGX2bPufWw3d84DiOX_REqNta-042XdEHUlOulmelLCJ_9-fvXTGkWrIV6-tNXYSkfcsvNbDUJzy8qQYmV5GK0xks8bofxbQBGEifxahwMpgTk4qDgO1fRH9R4mCx-NznpM32lwBqQyYPUxqLftiPOQe__awdugfIy8YVownQSKN0x7_N_DEKRjc2Cs5k3GL2Z9VO6SktMeD-HdZcOgjdZrN2s3RWaWzVTXrylRiwEuI2cTawdYDgqMQcOoyU9TF1KuCVUV7T8Zut9NfUHVvbu8Vx_0q7rNiBxQjSqPm-yBMeqbfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین:
اگر همه این دولت‌ها با این توافق موافقت کرده‌اند، شگفت‌انگیز است که چگونه همه این دولت‌ها به این سرعت امضا کردند در حالی که ما اعلام می‌کردیم که در اسرع وقت بمباران خواهیم کرد.از آنجایی که این توافق انجام شده است، آیا می‌توانیم آن را ببینیم؟
در این توافق چه چیزی هست؟میتوانیم آن را ببینیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65903" target="_blank">📅 04:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65902">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQ8AmelYGZd4b0EUH0FNnNjWv0nh3sVQs0bUz2AyQ7Cc8tBmkTAzhA8A9svfiNkBfki_LeJiyLQCv7pH9vg5ax7dcwejlGVxa6etJdT6F1IZ552jbhpTv50IRAD725VxuMB2gopY3N4cYnOpQDGNowFA8kOuDyMuvLAibB-xUiVdN3FA4u_gK7DH8B3SVRy1dfzSGtWbhc9rXXEbAzUBF2GtATk9oirXYzZKzMmUbjnYqjkYQ6YWcrVFC6gcWEWeehwyYthL64H4cpLMOUIECq2V0mjqp7AX8V_s9hpI17SekKWE2-BXaB0V6JX0GhTWsfoOSRoUVk7wtk08Je2nJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دقایقی پیش زلزله ۳/۱ ریشتر در پردیس تهران به‌ وقوع پیوست
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65902" target="_blank">📅 04:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65901">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
رئیس‌جمهور ترامپ درباره ایران:
ما با ایران توافق کردیم. معامله بزرگی انجام دادیم. هیچ سلاح هسته‌ای وجود نخواهد داشت.
مردم خیلی زود به خانه‌هایشان بازخواهند گشت. تقریباً همه چیز تکمیل شده است. ما هر آنچه می‌خواستیم را به دست آوردیم.
نکته مهم این است که هیچ سلاح هسته‌ای در ایران وجود نخواهد داشت. یعنی نه توسعه یافته و نه خریداری شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65901" target="_blank">📅 03:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65899">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78687e07ef.mp4?token=JzsTdPtFU9Jq1sFZ6IxYRl2eRPIkB6QKqzr3he5MZ1F7iY78msgTWTinbvh6K9uDWQU4fQlYYBUaQ1TF15dVLrhn4OZ7iBVx1FTot4VhSBk1k78G_gBVni5bqythLSWDGxtAPDu0fUOu-pKrlnVdmA-ZiTGOCPE_rUhHn4LxHY7s3fKdAjpjEFH-n7pJMf1f9yqMVEJ2e2CAj0TufMl6w31tdSH41xocfwaPxOLNX6k0lX1JY_uQKI3yBCYQdlqPo6gx19yX0_uFIMhsdaGzrwiznuylJrE_1_Ag4KK2jjkOgFoJQWw-Q_LMUg1b1ZGRpuOagesgwh8PgP756lzZ5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78687e07ef.mp4?token=JzsTdPtFU9Jq1sFZ6IxYRl2eRPIkB6QKqzr3he5MZ1F7iY78msgTWTinbvh6K9uDWQU4fQlYYBUaQ1TF15dVLrhn4OZ7iBVx1FTot4VhSBk1k78G_gBVni5bqythLSWDGxtAPDu0fUOu-pKrlnVdmA-ZiTGOCPE_rUhHn4LxHY7s3fKdAjpjEFH-n7pJMf1f9yqMVEJ2e2CAj0TufMl6w31tdSH41xocfwaPxOLNX6k0lX1JY_uQKI3yBCYQdlqPo6gx19yX0_uFIMhsdaGzrwiznuylJrE_1_Ag4KK2jjkOgFoJQWw-Q_LMUg1b1ZGRpuOagesgwh8PgP756lzZ5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ درباره ایران:
امروز جنگ با ایران را به پایان رساندیم و آنها موافقت کردند که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن تأکید داشتیم. این هدف اصلی بود. این ۹۵٪ از موضوع بود و آنها این کار را به قدرتمندترین شکل ممکن انجام دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65899" target="_blank">📅 03:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65898">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65898" target="_blank">📅 01:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65897">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KaFz4c_4si9iZVxGT7JafsY5om9ccGzjC_89NuMmXvDg9Dw6mY-sB5YE0j-IWjqIMcrtJWBFEA6F27AAliJtFDLvBg6poL8Cvu27NWmgywuF5XN4CWZbYgTtc_9Yk61XMAViknQZe9TICSE0MFHjG9CtIwBjK4pQe1FI7gfUrKeTT_XCWZcIIMLfvFSjAYluLLz0tkKauMM8rzrpLEkWtyOxfXTqh-mgeGWlq3lV7kMcn5ZYja6A9dSIZKyzvwIF9U5iMWZ71I-sVRQc3jUAWasASkoFM_6XeSlhedGc3NGES72uc-MA1I3ZH9H_u033KACgJzJERUUIXr2ivOSvaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65897" target="_blank">📅 01:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65896">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
صداوسیما:
شنیده شدن صدای دو انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65896" target="_blank">📅 01:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65895">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uq6vohSwkKAL9z1OQKzdF7PsKMVcNHeqKZyH6JvUnjctqY56YZxlkruBOaPzhY_aZUJLq4NZp-SwA3BMOBGz8DwdzlDQ8va1ovZD-kplh-ztr6eK2IrI43_QAto7cHZxQNiiKjBfjwjnqpzSR-gzTUfDk19kKootoB5Z2IZ2_v7WDonk6DyqvSy_TWvsjz5_Vkt8f4zuCSmb0ywjSESODFu5sqVFg-EHb9jgxjlGJGOT6hCA2VCZkbkuFAbd5bjdAi6OWzx4Y0OtSApwWCPKCfEUtoaD1oZ2H911RPuz-nEca2Swtwa9A_jiPTfEGkJbzRjZLVAVg0MHj3FtEN2iIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اعلام کد اضطراری یک F35 در آسمان امارات
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65895" target="_blank">📅 01:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65894">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دیگه نمی‌زنن
😭
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65894" target="_blank">📅 01:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65893">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
فعالیت سوخت رسان های آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65893" target="_blank">📅 01:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65892">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
مهر:
هنوز از ماهیت و علت این انفجار اطلاعات دقیقی در دست نیست، اما با توجه به دستورالعمل‌های مربوط به بسته بودن تنگه هرمز، این وضعیت احتمالی می‌تواند در همین راستا باشد
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65892" target="_blank">📅 01:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65891">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
گزارش هایی تایید نشده از انفجار در گناوه
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65891" target="_blank">📅 01:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65890">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
منابع محلی در سیریک صدای انفجار شنیده اند اما هنوز علت این انفجار ها مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65890" target="_blank">📅 00:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65889">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCxXac_zNnl45svKhFPglqSnncLHoODkN5HDEMdkqLdZP0LYNCcTjP5sbHI0HXV5pb-WEClF3GoocJRMGGiy4XY30qNRjYK9G9AvRGab-O_0n5xGxdYW98PK4xOJvyHOJCTSOAh7S3Quo4n3xe--t7vKIRMs4XMncDlXhXj4HuTSS3gT6y-nbpCryB5RrsR4gNsZjKOg1icIh2GU9O2sotOCYoBO0neLogD6Fv3moE2LDhg9SHcelqhZT9gLJDSyYukZaHdfTqrFfL3I5HXu616T9fios0nUwfy-fSJOMsblpjL3cUIM1dCiwY3u2Ek2f5mNowxwQ7sAdclH0wxD9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💥
تنها یک پست از ترامپ امروز 1.3 تریلیون دلار به ارزش بازار سهام ایالات متحده اضافه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65889" target="_blank">📅 00:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65888">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐀𝐌𝐈𝐑 𝐌𝐀𝐒𝐎𝐔𝐃</strong></div>
<div class="tg-text">الان یعنی با قاتل
حضرت سید علی خامنه‌ای
💔
، قاتل خانواده‌ی رهبر جدیدمون
💔
قاتل سردار سلیمانی
💔
، قاتل سید مقاومت حسن نصرالله
💔
، قاتل شهید فقید اسماعیل هنیه
💔
، قاتل دانشمندمون محسن فخری‌زاده
💔
، قاتل سردار حسین سلامی
💔
، قاتل سردار محمد باقری غلامعلی رشید
💔
، قاتل سردار موشکیمون امیرعلی حاجی‌زاده
💔
، قاتل شهید فریدون عباسی
💔
، قاتل شهیپ محمدمهدی طهرانچی
💔
، قاتل سرلشکر شهید احمدرضا ذوالفقاری
💔
، قاتل سید امیرحسین فقهی
💔
، قاتل شهید اکبر مطلبی‌زاده
💔
، قاتل سردار سرافراز عزیزمون علی شمخانی
💔
، قاتل فرمانده بی‌بدیلمون محمد پاکپور
💔
، قاتل سرلشکر عبدالرحیم موسوی
💔
، قاتل سرتیپ عزیز نصیری‌زاده
💔
، قاتل عزیز اطلاعاتیمون اسماعیل خطیب
💔
، قاتل شهیدان غلامرضا سلیمانی
💔
و مجید خادمی
💔
، قاتل سردار سرافرازی که بر بستن تنگه اصرار داشت یعنی شهید علیرضا تنگسیری
💔
، قاتل رئیس جمهور آینده شهید بزرگوار علی لاریجانی
💔
، و قاتل شهیدان دیگر مانند محمد کاظمی
💔
، حسن محقق
💔
، داوود شیخیان
💔
، محمدباقر طاهرپور
💔
، بهنام رضایی
💔
، اسماعیل احمدی
💔
، علی‌محمد نائینی
💔
، مهدی رستمی شمستان
💔
، سعید برجی
💔
و منصور صفارپور
💔
توافق کردن؟</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65888" target="_blank">📅 00:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65887">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما به نقل از سخنگوی وزارت خارجه:
قطر و پاکستان به‌عنوان میانجی‌ها فعال هستند
وضعیت مذاکرات از ابتدا برای ما روشن بود و بخش عمده متن نهایی شده بود اما آمریکایی ها مواضع خود را تغییر می دادند.
ایران ثابت کرده است که در آنچه را به عنوان خط قرمز معین کرده است مماشاتی ندارد.
مواردی که درباره توافق مطرح می‌شود گمانه‌زنی است و موضوعی نهایی نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65887" target="_blank">📅 23:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65886">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzD1_FVeBbxdFTiuMC1v6O9iK6y6xbG5c0-RyeclVbDb2RQ6qBs4UNNPPe3EfZl7D4kZvw-GX5vCgohcytxy3NcGvdwL0fV4bEeNj189izRz3ZUnx3UFJIDl06Wg8tkZFvcRt-2JgsIi9huwL17KacUebS9gjJPiVAgx5ZFgC-gmmEI-C-NFSKG6DRK2lsZ2T7HpWH4_isIkH4tJcsILDiQD7NUOSc3hSrNwXiS2OGLbt4Z3To8uhYucNMqfVmDqlxBfbz1CM31L0SgMc_b0GJ2ya9-vd1SUX45wdwDXcmrZw5e2JKGVnxwLLOi-AtC6przE77t1UZsnAqKAYwgxVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
دفتر نتانیاهو:   رئیس جمهور ترامپ با نخست وزیر نتانیاهو در مورد نهایی شدن یادداشت تفاهم با ایران برای ورود به مذاکرات صحبت کرد. اگرچه اسرائیل طرف این یادداشت تفاهم نیست،نخست وزیر از تعهد رئیس جمهور ترامپ برای اطمینان از اینکه توافق نهایی که در پایان مذاکرات…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65886" target="_blank">📅 23:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65885">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:  رهبر جمهوری اسلامی با امضای یک توافق موافقت کرده.  @News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65885" target="_blank">📅 23:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65884">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
دفتر نتانیاهو:
رئیس جمهور ترامپ با نخست وزیر نتانیاهو در مورد نهایی شدن یادداشت تفاهم با ایران برای ورود به مذاکرات صحبت کرد.
اگرچه اسرائیل طرف این یادداشت تفاهم نیست،نخست وزیر از تعهد رئیس جمهور ترامپ برای اطمینان از اینکه توافق نهایی که در پایان مذاکرات شامل حذف مواد غنی شده،برچیدن زیرساخت‌های غنی سازی،محدودیت تولید و برد موشک و توقف حمایت ایران از گروه‌های تروریستی وابسته به آن در منطقه باشد، ابراز قدردانی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65884" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65883">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: بعد از توافق سریع محاصره رو بر می‌دارم
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65883" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65882">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
رهبر جمهوری اسلامی با امضای یک توافق موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65882" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65881">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛ نورالدین الدغیر خبرنگار الجزیره در تهران:
دیگر همه چیز قطعی و تمام شده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65881" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65880">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇷
#فوووری: ترامپ: به من اطلاع داده‌اند که رهبر ایران توافق صلح را تایید کرده است  @News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65880" target="_blank">📅 23:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65879">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352ca9d87d.mp4?token=fvRnuBWIlFCTDCnKEx8WK1LSCZWzMoBiJofc7t4L1RCKbtVI4P8-HXzbd8zajKXLZEqxmOvgXCbRAmECVX7uvy0ugTGfeaDD3Jw0IvhKKs4lHqmYrucD8fo5pL1_0A3ZLoI6mj8LkpsZephnBlfjfpU9yaryxHmVa5ugFmWDAxuUsaWB1HOnQbNqGJ-_Hwq6ywTWpryTIgFqZcT5nmufe8zxApYjeslh5qLjhDIWoqSXWLNPKKPScpMJxO1_Myd9i_68XmakiX6bVOt_4Lc1PYAi6Qw-RoQsgvFDna5k-52B-bbwgQa5sd5wjQ2O3xpC2xqxNUFBexb0ukXn0kbbPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352ca9d87d.mp4?token=fvRnuBWIlFCTDCnKEx8WK1LSCZWzMoBiJofc7t4L1RCKbtVI4P8-HXzbd8zajKXLZEqxmOvgXCbRAmECVX7uvy0ugTGfeaDD3Jw0IvhKKs4lHqmYrucD8fo5pL1_0A3ZLoI6mj8LkpsZephnBlfjfpU9yaryxHmVa5ugFmWDAxuUsaWB1HOnQbNqGJ-_Hwq6ywTWpryTIgFqZcT5nmufe8zxApYjeslh5qLjhDIWoqSXWLNPKKPScpMJxO1_Myd9i_68XmakiX6bVOt_4Lc1PYAi6Qw-RoQsgvFDna5k-52B-bbwgQa5sd5wjQ2O3xpC2xqxNUFBexb0ukXn0kbbPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇷
#فوووری
: ترامپ: به من اطلاع داده‌اند که رهبر ایران توافق صلح را تایید کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65879" target="_blank">📅 23:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65878">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1ce54a8a4.mp4?token=cnSfroYuVfg6WH-oxSOsiELa6IlFemVRNaa1aLKYtKujInFXX6luV1R9uS7FT0L4ue9m3LgN1ySX8dwhIRhN0hzuveSFsm9YQk7lBrVuOjsY41WBozQ-7tIOJOONmCi79c_c9HdcqJWIUJ_HOUkJDwua8SUMsXd5r01Y5dEN4zah4-3tZJO_3Jmq_WwEPfiTnyHrYZxoe-ii5K3sd7bAPBXXQ_pn6ZO7deFNUeMmQeAlfr0ah29pCgOzQkHbXBWsJ8QwPlJWkGe34Lsznhjumy3oBwjWndbO7oiMtpw0HtaatlaR_V13-sV8ow8U-MEzVun6DbcgS6PXFuXZqYEgKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1ce54a8a4.mp4?token=cnSfroYuVfg6WH-oxSOsiELa6IlFemVRNaa1aLKYtKujInFXX6luV1R9uS7FT0L4ue9m3LgN1ySX8dwhIRhN0hzuveSFsm9YQk7lBrVuOjsY41WBozQ-7tIOJOONmCi79c_c9HdcqJWIUJ_HOUkJDwua8SUMsXd5r01Y5dEN4zah4-3tZJO_3Jmq_WwEPfiTnyHrYZxoe-ii5K3sd7bAPBXXQ_pn6ZO7deFNUeMmQeAlfr0ah29pCgOzQkHbXBWsJ8QwPlJWkGe34Lsznhjumy3oBwjWndbO7oiMtpw0HtaatlaR_V13-sV8ow8U-MEzVun6DbcgS6PXFuXZqYEgKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیرِ واشنگتن #hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65878" target="_blank">📅 23:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65877">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
منابع شبکه العربیه: طبق توافق، آمریکا تحریم‌ها را کاهش می‌دهد و محاصره را برمی‌دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65877" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65876">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldiDkbc6eExTlC4Iz-nDxErEz8sSmos6uRPXqcmg41WLGcKlk7U5QitP2Wk4fhn2YnEpVsXsizh8WzdV5DyOCexEURGC_svGZFMnZZ7QmGOn6-36lRYV8u3r3eOLQJGfYVWv4I6KzszYttn4PFvZ0yJXWZDt2np-YWLuuscEjDYuI3uE7BAJ_Rxu8PKTaiLbsPVcXyygixIMcXD3MPvIhF1cZIDSfzNeAIGo46-IfnWestFK7EPR3tVE1vrUpkkMlrbnKVmyXLxAjYh4husvA9a3ugOeIjYhvQKfMmM8OY26NW8YNX0Z_mNPZjAaN-kcTVdMNthiQopi3LomL-3IOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیرِ واشنگتن
#hjAly‌</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65876" target="_blank">📅 23:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65875">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e445beba9.mp4?token=PqyihOlIEdyrjezSCJ1jOBtEmbXgbhROwNvOzrYrOH8bI-eHURr5-nNFrgfLrUrkQ0FxouDcUQtLcy9W8WwWFN68wYHoGnEz149_L8OE53nh1EfgEHrmibdkwhagKUKMULHQXc2UD09sKyLB91aWQDidcSj0JAwkZ-xC5YfrI4hQh0R_IH-h8xH0168kR-2k-ks2ilzjdBXYvbD5BrsEiZGmQxLSiVX6DPjtYKn1puWDRqnqTlSActWJnWlpUSMErza1vZYG55Pvrb7MbnFlXoTxCXBKyc2v6RwSBv9vYyMdk_rED7HyjHiI494MiHz2qMYcbVPdDUvBGByCQZRda0xBfLbOBRCQRJQBFfDEGml6VnikCgA4mN517ISMphUlwwuPzPanWYOrFT617BECqrgNR_4WyOjvzvxvFRTrApkf3mRLM6Pck6SCROzCta6HY1NvBBEFIfhS7lrVfh9ul7I00CzgsJgGpKyXhUGwZ0xKd0z3ShUYZba2m6QY1Mgao4Qs9TB9WIDVtIHSQO77UsnpDdUMboM9-xSHYvR85TtA0UEDuXeJD69eNVVQ_iykoYIwoyd4MAx8nq-2ZDYLKDlyepGdQ539QopVIEA3L0lDXxdSMKZSz16mnHDTLQhUXa60XoJBY8hB_XOHsbQsDVO_oYWDi6rZqLbtcAxapV8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e445beba9.mp4?token=PqyihOlIEdyrjezSCJ1jOBtEmbXgbhROwNvOzrYrOH8bI-eHURr5-nNFrgfLrUrkQ0FxouDcUQtLcy9W8WwWFN68wYHoGnEz149_L8OE53nh1EfgEHrmibdkwhagKUKMULHQXc2UD09sKyLB91aWQDidcSj0JAwkZ-xC5YfrI4hQh0R_IH-h8xH0168kR-2k-ks2ilzjdBXYvbD5BrsEiZGmQxLSiVX6DPjtYKn1puWDRqnqTlSActWJnWlpUSMErza1vZYG55Pvrb7MbnFlXoTxCXBKyc2v6RwSBv9vYyMdk_rED7HyjHiI494MiHz2qMYcbVPdDUvBGByCQZRda0xBfLbOBRCQRJQBFfDEGml6VnikCgA4mN517ISMphUlwwuPzPanWYOrFT617BECqrgNR_4WyOjvzvxvFRTrApkf3mRLM6Pck6SCROzCta6HY1NvBBEFIfhS7lrVfh9ul7I00CzgsJgGpKyXhUGwZ0xKd0z3ShUYZba2m6QY1Mgao4Qs9TB9WIDVtIHSQO77UsnpDdUMboM9-xSHYvR85TtA0UEDuXeJD69eNVVQ_iykoYIwoyd4MAx8nq-2ZDYLKDlyepGdQ539QopVIEA3L0lDXxdSMKZSz16mnHDTLQhUXa60XoJBY8hB_XOHsbQsDVO_oYWDi6rZqLbtcAxapV8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره جمهوري اسلامي:
ما توافقی داریم که ایران هرگز سلاح هسته‌ای نخواهد داشت، که این کل هدفی بود که باید از آن عبور کنیم تا به این برسیم.
اما ما به زودی امضایی داریم و اسناد تقریباً در شکل نهایی هستند. بنابراین خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65875" target="_blank">📅 23:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65874">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
دونالد ترامپ: در مراسم امضای توافق حضور نخواهم داشت و جی‌دی‌ونس قرار است عازم اروپا شود  @News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65874" target="_blank">📅 23:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65873">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeHe7aTZZWGKVDxsOQNpIdHZ6DMm8pAp1wj59PH8C7FeghNjRl1tPP2dG3KafdtDXvm6HOZcQmHZwgL4MXRfwdQivTfjgcP_AV3yHVfebD9591CAX63aj349oU0a8QfiXHB1QZBFq7Q0YYclVlswd8aMStG3QDPuUrR1gmdXNIJYjMTD0F7Er017FHIGJWqsnt24Eawm4gGsl7oB8XrZbD_BgVpcCjfOhUSCkBoY6n5Q9fF_-NAuSGfSFpIUdvuWbkFsyinBlgkRn_uNuXx2UTDvYQFre9N2K0hayciUOqveVJEPtML7XK_8uUA2pCtIafwYQRsSGH8-mhO8nsM8WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آره داش آخوند های حرومی تسلیم شدند هفته دیگه جشن آزادیه
🤡
🤡
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65873" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65872">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ترامپ: توافق با ایران بزودی در اروپا امضا می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65872" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65871">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ترامپ: توافق با ایران بزودی در اروپا امضا می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65871" target="_blank">📅 23:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65870">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
دفتر امیر قطر: تمامی کشورهای منطقه در خصوص تفاهم ایران و آمریکا رضایت دارند
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65870" target="_blank">📅 23:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65869">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ به نیویورک پست : توافق «بلند مدت» با ایران تقریبا نهایی شده.  @News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65869" target="_blank">📅 22:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65868">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
ادعای اکسیوس:
منابع ایرانی امروز به کشورهای منطقه اطلاع دادند که توافق «اصولی» در مورد یادداشت تفاهم حاصل شده است، اما تأیید رهبر انقلاب همچنان لازم است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65868" target="_blank">📅 22:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65867">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
خبرگزاری حکومتی فارس:
‌ منبع آگاه: ایران هنوز هیچ متنی را برای توافق تایید نکرده است
هیچ متنی برای یادداشت تفاهم اولیه با آمریکا تایید نشده است؛ این را یک منبع آگاه نزدیک به تیم مذاکره‌کننده جمهوری اسلامی ایران به خبرنگار فارس گفت.
رئیس‌جمهور ایالات متحده ساعتی قبل در پیامی در شبکه اجتماعی تروث سوشال ادعا کرده بود که ایران در عالی‌ترین سطح با متنی برای یادداشت تفاهم اولیه موافقت کرده است.
وی دقایقی بعد در اظهاراتی مشابه خطاب به روزنامه آمریکایی نیویورک‌پست هم گفت که متن مزبور جمع‌بندی شده است.
ادعای ترامپ در حالی مطرح می‌شود که ایران و آمریکا بامداد پنجشنبه یکی از شدیدترین درگیری‌های خود را پس از اعلام آتش‌بس پشت سر گذاشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65867" target="_blank">📅 21:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65866">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
آکسیوس:
به گفته سه منبع آگاه از مذاکرات، قطری‌ها و ایرانی‌ها روز چهارشنبه معتقد بودند که به متن مورد توافقی رسیده‌اند که آمریکا نیز آن را خواهد پذیرفت.
این منابع گفتند که اختلاف‌ها در سه موضوع کلیدی کاهش یافته است:
سازوکار آزادسازی دارایی‌های مسدود شده ایران - مهمترین مسئله برای ایرانی‌ها.
تمهیداتی برای بازگشایی تنگه هرمز در طول دوره آتش‌بس ۶۰ روزه.
چگونگی انجام مذاکرات بر سر برنامه هسته‌ای ایران در طول دوره آتش‌بس ۶۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65866" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65865">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ به نیویورک پست : توافق «بلند مدت» با ایران تقریبا نهایی شده.  @News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65865" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65864">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ به نیویورک پست : توافق «بلند مدت» با ایران تقریبا نهایی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65864" target="_blank">📅 21:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65863">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🏆
🏆
بزنید افتتاحیه ببینید
🔥
🔥
Persiana Sports (بدون VPN) Bein Sports (بدون VPN)  لینک های m3u8 رو با برنامه های iptv player یا mx player - pot player - vlc پخش کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65863" target="_blank">📅 21:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65862">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(ммd)</strong></div>
<div class="tg-text">🚨
🚨
🏆
🏆
بزنید افتتاحیه ببینید
🔥
🔥
Persiana Sports
(بدون VPN)
Bein Sports
(بدون VPN)
لینک های m3u8 رو با برنامه های iptv player یا mx player - pot player - vlc پخش کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65862" target="_blank">📅 21:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65860">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gC20_C2FvuIPygLZOg80WYtCO0Uqd-vYhWkPpzlpbVu3rkVCbZB-Ro2hkTqahifmqCKkZnI_nWFVrjCXbH4eEORLcnhwwyCqF2dI0Z6SuNtZqcPmUT3uj3gEYfYI-fL1idnKl8yIfbkZO49unJgfxLrQJzuEP-lron-XMCyEn8icLVQrQt-r4uPFn_H2h6PvnwQBxGDkWJ7BINZl6yY7FtXp-3cb1F8TiXZJpFY4wM8wutVyvufT-eqPSUmiFJ1C8XUD9HLwa5W_WAbXs-qcsP8rqwLSgEWlPkCKKOWlv-KPD8Ja6lx1H48Axv5hmp9uj9Kl0P7k27oW9_8h7Eqgvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GkOnRTCLg_uhmMSJGWzBfYTYwmoIGCBP5XGIUx7YlwiM5UESC9M7_vaxjHTqLQ7JVOJaXRSPyY0yo-BvbIAYTS84s7SDjDoToOwHWw1cxiY02Ix0XZ43RFKfrQoE8Lw5I-aihtUkbFjpMt7G5nfI4bf4R5Lsm5uRcwxynd-gjgE_Wpi3z73Peb_iXkqQgi5g294EiRnvKqmD567F6-SjK6dkNcUJdO7v3I7jA7Njlh_dw9X2gfRu9pO63K6yKmrjtvcRmQzxE2fwF9e4GiWC5uOEbruN8CP3AX0T8tGTmcmmli-7XPhbEHVk_1B2QZk6l-zqiuh6oVt_S4Aw4aSeRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
اجرای شکیرا در مراسم افتتاحیه جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65860" target="_blank">📅 21:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65859">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGFR7pP8oLLfcuVmTczp6czif2kKhOhsDU66_XxC1OF3CpaB1u8S-AE-8vBE9Xov1mDxfj7zA-I25Zli_8F0jyUa00W_xZjKCtjsIa3k0f08DI7Gl91v5Qh7wArl7Cjs43VjlA-9DmO8-rWT8CZ7Pa0cyJFT8YVKPRQ06RwI1umdjVYsR5xP7e-izeRVkTEKss-dOcH0LBnLnHwwEVjuZKIdpAiNoIvAvIYuEyLCLOqwuOG4vZHZWqdQ826TbJFaOtI70nkrX-KGT9Vn5PC3i1kPDGSem5dd_ONdNN9YGroKMPWiNQzafebYSkunvRfoBMIO1pEJYrgPeGSgLvvj8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت سپی هست داداشمون
که در تمام سه ماهِ جنگ vpn هات نیوز رو برای پوشش اخبار تامین کرد، هواشو داشته باشید و می‌تونید از داخل سایت بطور زنده افتتاحیه رو ببنید فقط کافیه یه ورد بزنید
🔴
لینک سایت
http://Chosefil.com
🔤
لینک کانال
@officialChosefil
#hjAly‌</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65859" target="_blank">📅 21:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65858">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ=حرومیِ کاکولدزاده #hjAly‌</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65858" target="_blank">📅 21:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65857">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ماشالااا تراااااامپ شیردل
😤
#hjAly‌</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65857" target="_blank">📅 21:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65856">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJM9oDMlKUTTmPOcPiqiwHLYlF4G44dF85Gy91bxUBgE4pUXH6FYi0CeGk80tN-wqOULCW239wb55TR7wxu1rWXQQI-BmwnaVO8FQ3tI9hll2ybMXbhf0QVu5BZpKB3jQNuOAIVbKReead80k3BGePIW8SgS4wDUFOsdfcxW20zmYvlsGrqpDA3Y0FZm_aDJ8yOuOnKa0Cpp_7jrGT768NoxicZK_iEt7RJAHLR9UXVVrGpzCgM65odZedBHtApPWMKgTOTYHtgKnfF-kEhHOtiBNKEqwGhinGunYaBrcZPiL8XYJnGVbmqnURWqFdPuf0Mo4fwZOrRW5vrps6dUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
حملات و بمباران‌های برنامه‌ریزی شده امشب علیه ایران را لغو کردم.
با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایرانیان برده شده و تایید شده است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی شده امشب علیه ایران را لغو کردم.
مذاکرات و نکات نهایی، هم از نظر مفهوم و هم با جزئیات فراوان، توسط تمام طرف‌های درگیر، از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات متحده عربی، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران، تایید شده است.
محاصره دریایی تا زمان نهایی شدن این معامله به طور کامل و با اثر باقی خواهد ماند
زمان و مکان امضا به زودی اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65856" target="_blank">📅 21:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65855">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
#فورییی
؛ترامپ:
حملات و بمباران های برنامه ریزی شده عصر امروز علیه ایران را لغو کردم
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65855" target="_blank">📅 21:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65854">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
علی‌عبداللهی فرمانده قرارگاه مرکزی خاتم‌الانبیا: صادرات نفت و گاز یا برای همه خواهد بود یا هیچکس. ترامپ اگر خریت کند تمام منافع و منابع نفتی و انرژی منطقه را با دستور قاطع پودر می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65854" target="_blank">📅 20:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65853">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7e36d42b7.mp4?token=gH1PlxETwSp1n0WG9SvCEMzm04llVpD1fhFY2BAMnzGiRTFqCVj8SHmSNDU69Y9bBYL6vh_aUUKEwB1muWUBY-Y1Ip8EF_VPjB3Rmm_9f1BtkD7hNjpS3EFsLV24w0tLptAmwrkFLbOUGc-ULUbxcJqbzDt3dEysQ7I8GlahWTLl8blnuCztzj3EOFlu1VLm0h4NkabugmCeq8Yl7ZsM40e5qM8G743wdXgxLZI-bri-i3nMeq4TX9TDRzSXS5l5ApCKMfpOpBBISBP2Fa5jdTTIRgMiOFdGrADAmL7YjxR1bYgHRAP26l90gbVBgryyyGMlyz4xaJAqAxOej0A2zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7e36d42b7.mp4?token=gH1PlxETwSp1n0WG9SvCEMzm04llVpD1fhFY2BAMnzGiRTFqCVj8SHmSNDU69Y9bBYL6vh_aUUKEwB1muWUBY-Y1Ip8EF_VPjB3Rmm_9f1BtkD7hNjpS3EFsLV24w0tLptAmwrkFLbOUGc-ULUbxcJqbzDt3dEysQ7I8GlahWTLl8blnuCztzj3EOFlu1VLm0h4NkabugmCeq8Yl7ZsM40e5qM8G743wdXgxLZI-bri-i3nMeq4TX9TDRzSXS5l5ApCKMfpOpBBISBP2Fa5jdTTIRgMiOFdGrADAmL7YjxR1bYgHRAP26l90gbVBgryyyGMlyz4xaJAqAxOej0A2zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
تهدید وزیر خارکمبه علوم: اون دانشجویانی که پرچم پهلوی گرفتن تو دست و پرچم جمهوری اسلامیو اتیش زدن تحت تعقیبن قراره مجازات و اخراج بشن
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65853" target="_blank">📅 20:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65852">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeCYfvQ6I3Qa2MqzJSe5837MqEXG2QWf4eCGeBbA_t4PCuKvZKJ-mRJWfMt_vczJEYXkKs6ZySL8ZLhN6ArpXxQF-dEApbjZxF1iMArULyUQMZLw0XcyLJTy2KwbObG7YjVFe940u8Klf15B62syFqelSNx9zYAKSsVHuOWYvHDDkJ46PDTCYPF6naU8nodrKdOuJK8tv39Kg9Dva_3TGW4vEsFA7Y6VtnzanXvb9n7qJlukBuqfj3beil7097cunhZ2wlIq9mhcG6CFedMWIAUPq9tvK7WNN130wAJOjcl8dqIXO8K1G3-iNzUTPbQJA44g7iwMANgLreFdIG8Ccg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
قالیباف:
استراتژی‌های اشتباه و تصمیمات عجولانه، کل اوضاع را به سمت بدتر شدن تغییر می‌دهد، زیرساخت‌های انرژی و بازارها را منفجر می‌کند و باتلاقی بی‌پایان ایجاد می‌کند که سال‌ها در آن گیر خواهید کرد.
شما ایران متفاوتی را خواهید دید.
زارت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65852" target="_blank">📅 20:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65851">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ghs8TdScwpnWUDzK2EDKRM-4VRmoqaIieWS-w98jHIX9htT00-COhZ6zA6PvVDxBxdUKdocGFnpdEEG0MJHsnlh20NtHY79SERAejh2x8pbSoCxbhSTpRfXKPRjLMIp2soRwU5276zXCZlWCUhZd_N2YAjqjXHU31yddubykKWTXg61D5Dqj9AHgJGSk37PLpDjR73_Cv1hK08BqW0b-IRijt8qkBlKDfeXrNR3-ghG-tGIIHaHuqqt58Uahm9mDFEQs_zkMNuJ__4jdW9ry9OeVsz0WZ5SOWt8okfjSqEhXE1up-K6IyQ29qk_R-WljS3d9eK9s_3-XnnEP2c3WiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
به‌روزرسانی عملیات در لبنان:
سربازان ارتش اسرائیل فعالیت‌های خود را برای دستیابی به کنترل عملیاتی و پاکسازی منطقه شمال رودخانه سلوکی در امتداد خط دفاعی مقدم به پایان رساندند.
منطقه رودخانه سلوکی توسط حزب‌الله به عنوان مکانی اصلی برای عملیات پهپادهای انفجاری و حملات غیرمستقیم علیه سربازان ارتش اسرائیل استفاده شده است.
این نیروها صدها سازه تروریستی را منهدم و بیش از ۵۰ تروریست را از بین بردند. علاوه بر این، چندین سلاح از جمله دستگاه‌های انفجاری، موشک‌های ضد تانک و موشک‌اندازهای ضد تانک کشف و ضبط شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65851" target="_blank">📅 19:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65850">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heUlwmV_6F33oMD-UF66Ndnp-_yaBGWZCot7mH41ylK71r_lH0tzMCHavLE96NENiCiuyrWAMvoMQd1eneQrai-cRqV1l1nw2pdE2odlxb5TVxcPpayt07BFk7j2enmvwv6f6NwfFzL6x0NGbtNvTaGnoLftSIyQSdXHTvciiv-vuc_Kud8FvFm0z5tr-eaeVg_wqOOQdTr5KmetDkzjGMN4azeNBTCEkE1URLRv_ha5zC04Dw0xhk806AYMqnT6Kzq9LT_L7pYHYaITJRSwtPSWD25WB5y6Xj-IcQn_OB-JjdhbLcwNdyd4wgNsDbLDYsv9PhYEeBaZVlqjtEPHBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پست جدید سنتکام:
تنگه هرمز همچنان برای عبور و مرور باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65850" target="_blank">📅 19:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65849">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
الحدث: ترکیه، مصر، پاکستان، عربستان سعودی و قطر قراره جلسه‌ای فوری برای جلوگیری از شعله‌ور شدن جنگ میان ایران و آمریکا و پیدا کردن راهی برای توافق بین این دو کشور، تشکیل بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65849" target="_blank">📅 19:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65848">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
جمعیت هلال‌احمر اعلام کرد که در پی خطرات احتمالی حملات امشب، در آمادگی سطح بالا و کامل قرار دارد
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65848" target="_blank">📅 18:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65847">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmzwPgLzzw4dpSMMuW9bHCSuh_dQ9SRp3uhWktQLWF9eRhDwtB_tclSk0UejmXJxOmPehP8k3G4fGjtKDDWLHLXvSdJF2q8teHbNIMTYF3Do6SxX9dhkzAQjKJ7G8hEHlH62ybPFbUpNWhYRVwJ3WK-0VL02WyisloJB948rME1ubDAwLDi3fJ-_P-_PSEuUzz8DoePJad6PcXEkuK1CPWSGwo9UMt-q2Al3TB8jUUsPqRCShHITA5llN--bAFDq2z9Ai-UzVuiHK09ia-52Df4MZaZOyTfMdlFEsmA_0fjP2EPcbH8LgrbRL9jyJxQ8qTTvt-yNmT4_it3hyoO2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشیال
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65847" target="_blank">📅 18:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65846">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65846" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65846" target="_blank">📅 18:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65845">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns3Tr_SuzqsZD705Q-pw4azprpwx58iE-h0PFz1m7ACRpYt7IwXpIudmVZVqekZm0jB-pCi_IkTJJoQIIKKoA5pVlWHrGQOFFoMi5O8aE4rXsNOu5eLmjrYqTrIpatJRa19O2D9bFGzNUInEuguCFehOaSNmzsNRV_v6QjVSmXucLOLb1g-O5IpWpV21k8bYk-0Glts7JC4OEIfvqJ9-2Eqto6YGKqpcr3eprmbOTiKOr2W8phieM4s-I2Jc5G6xPuxBk7i1Ljg21yFXHCZj8qHU6extvGXGo-zmTGeeaf6HkIC0vQOnjZeXsxgKGJvIBvqOSUymjhd1GWHyEO2eig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65845" target="_blank">📅 18:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65844">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14bcfc7050.mp4?token=a-CZIWHTjPQhj4N7Dl6bQss3J6Qp17cpI6howMqjyrbNKT484BPPTNHMnDmjWq8pUCLKdsGO_edL57-yxIK81egdslUBnOMyV3KX8-9zCuRmK33zHX02-RUOtsQaDA8X80pNMTswHa4d3DQLDElXmWa75o22q6j6ESHlZ9fuENYCiODS59hzFhTDENyYbH1uRIf6iOBgAbESWdaOdhpuyxSVkE7ov5QTlcBYUsnUiHlqdNEsh-51_UVr_actzqEKA-l9LUy6eMw45e0kqBDF4wg_UG3lAaeE4npToMOs7dyEJoeNalkeEIJAmoluqvOMk1qyN0k10hoUWu2BTppaVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14bcfc7050.mp4?token=a-CZIWHTjPQhj4N7Dl6bQss3J6Qp17cpI6howMqjyrbNKT484BPPTNHMnDmjWq8pUCLKdsGO_edL57-yxIK81egdslUBnOMyV3KX8-9zCuRmK33zHX02-RUOtsQaDA8X80pNMTswHa4d3DQLDElXmWa75o22q6j6ESHlZ9fuENYCiODS59hzFhTDENyYbH1uRIf6iOBgAbESWdaOdhpuyxSVkE7ov5QTlcBYUsnUiHlqdNEsh-51_UVr_actzqEKA-l9LUy6eMw45e0kqBDF4wg_UG3lAaeE4npToMOs7dyEJoeNalkeEIJAmoluqvOMk1qyN0k10hoUWu2BTppaVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
'لحظه انفجار حمله حدود ۴ صبح به
پیشوا
در  تهران
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65844" target="_blank">📅 18:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65843">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVNhRFToYPz7vql13Sdn2fie51cN2ja7elaw4V8y-gED5PB9nOgidzD2Gxm5Xm0FLAtecjDh_On7rObNr6z8jQBxnmm5EcyCq5rJmnlu8wmA97tBF18sBS74huoy0Q7r1i_2EUfhoh_bRiEW1w0CZyrU-WBrvzoPt11ZBVt4VfX9PdvmIHtl1ecVK3iiHMcI9mCQUP_llEq1LDTHAWT_GRRZh_nsg6rtdB-KxlVwerdGLmK66jD2TviYby1ODlwmK6DpAPjH97g_uA99P0cTQa2_QHllNMiz2zQoMDzSp0cV0DJVTb16_CP1KrHuBLLvNtL9YMIfzaVzMaqbEPzJkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست جدید حساب کاخ سفید:
«رئیس جمهور ترامپ همه کارت ها را در دست دارد»
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65843" target="_blank">📅 18:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65842">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
اسکات بسنت، وزیر خزانه داری آمریکا:
رژیم ایران در بازی مجموع صفر که در حال انجام آن است شکست خواهد خورد.
هر آسیبی که به متحدان ما در خلیج(فارس)وارد کند با وجوه استخراج شده از حساب های ایرانی جبران خواهد شد.
هر عوارضی که به مقامات تنگه خلیج(فارس)پرداخت شود با وجوه استخراج شده از حساب های آنها جبران خواهد شد.
هر حمله ای که ایران راه اندازی کند، تنها پیامد های مالی و اقتصادی را که با آن روبرو است عمیق تر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65842" target="_blank">📅 17:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65841">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qd9wwXzFgRf6NedMyrutjuxMP613rUmXQJzu7lgydJbYLd3thH3kETQH4pK1lYsTnpikcCt61DoOWVWjXfr8CqLiN9eQYsSUjkcRUHmuZUIu-gkhtnb_IqCJWO963yxoafaYOEB0_0H3BrtUmwb87mUqRXXHx4D5EfimFheHqFOLubkThFeMi5knw79E19EXbJSxxXUdQQWNddzxWNEiCPBATekVApb72hWK8_yeDFPjbkr48p6llDCHJi7t66PZFwjOs0sycljgVTRxjUqKjHedNSwkJmj3Ow7nBL41dHF0vNpUbu99e-hSewlFuPLJCv8dUi5N6zdNiPNGZws44w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
ایالات متحده امشب به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمام اشکال دیگر دفاع آن، به همراه بخش عمده‌ای از توانایی تهاجمی‌اش، از بین رفته است!) ضربه بسیار سختی خواهد زد.
در مقطعی در آینده‌ای نه چندان دور، ما جزیره خارک و سایر نقاط زیرساخت نفتی را تصرف خواهیم کرد و کنترل کامل بازارهای نفت و گاز آنها را به دست خواهیم گرفت، دقیقاً مانند کاری که با ونزوئلا انجام دادیم، که به طرز درخشانی هم برای ونزوئلا و هم برای ایالات متحده آمریکا نتیجه می‌دهد.
از توجه شما به این موضوع متشکرم! رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65841" target="_blank">📅 17:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65840">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ارسال سلاح از طریق کردها:
ما در واقع به آن‌ها سلاح فرستادیم و صادقانه بگویم از کردها بسیار ناامید شدیم. کردها ما را ناامید کردند.
من با این تصمیم مخالف بودم. می‌دانید، من می‌گفتم، «نه، باور ندارم که آن‌ها سلاح‌ها را تحویل دهند.
فکر می‌کنم آن‌ها سلاح‌ها را برای خود نگه داشتند. فکر می‌کنم این یک ننگ است. اما من این را به یاد خواهم سپرد، کردها. من این را به یاد خواهم سپرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65840" target="_blank">📅 17:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65839">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
جی دی ونس درباره نتانیاهو:
نتانیاهو کشوری را اداره می‌کند که به‌وضوح یک شریک بسیار نزدیک ایالات متحده است.
اما حتی وقتی ما شرکای نزدیک بوده‌ایم، گاهی اوقات منافع ما کاملاً همسو است و گاهی اوقات منافع ما ناهمسو است.
نتانیاهو به‌شدت منافع کشور خود را تأکید می‌کند. گاهی این بدان معناست که ما در یک صفحه هستیم و گاهی بدان معناست که نیستیم.
آن‌ها به‌عنوان یک شریک بزرگ در بسیاری از راه‌ها بوده‌اند، اما ما همچنین باید بر آنچه در بهترین منافع آمریکاست تمرکز کنیم. و جایی که این منافع منحرف می‌شود، متأسفانه برای اسرائیلی‌ها باید سمت مردم آمریکایی را انتخاب کنیم، که همیشه این کار را می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65839" target="_blank">📅 16:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65838">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromromo heidary</strong></div>
<div class="tg-text">اسپویل
فیلد مارشال عاصم منیر، پادشاهان عرب به ویژه محمد بن سلمان از من خواستند که به دیپلماسی فرصت بدم و ایرانیا هم از من خواستن تا فرصت نهایی رو بهشون بدم منم گفتم باشه و حملات امشب که قرار بود زیرساخت های ایران رو نابود کنه و جزایر ایران رو از روی نقشه محو کنه متوقف کردم
از توجه شما سپاس گذارم</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65838" target="_blank">📅 16:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65837">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری از ترامپ: آمریکا امشب حمله بسیار سخت و شدیدی به ایران انجام خواهد داد. ما بزودی جزیره خارک و دیگر نقاط زیرساختی نفتی را تحت کنترل خواهیم گرفت و کنترل کامل بازارهای نفت و گاز آنها را در دست خواهیم گرفت، همان‌طور که با ونزوئلا انجام دادیم  @News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65837" target="_blank">📅 16:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65836">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEXQdTkni0w_5p4q8u_dsp4bSusrjzRkL03ugZdc48Ij_CINQrn83VJ2JaYRNiFxknEWAgViaHMs6_BVeO5VeS5aZDamgwG-0_XO-graAcUPn1voDZA-WewW0J9tFPZdVwnxfvRQunfOt_Jqpg6rir5D-ifjN3OVTI8JX_EfuYiGodH_bfpaYyUZCHPH5ITw-wxjsIUY5LGdNlDEtElvbYma932dg0NpwKA5rPyGI7RoHudcH7xLddeex_OIPk3pqE2BlwSZ7lvqMrJB6HlL-zp8RxjEBA5UQ_ggH3PzKLh_WsghyZNSur9uoUr_fZ4-fgpnVX7qcRmTvNCHeTmi-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
از ترامپ: آمریکا امشب حمله بسیار سخت و شدیدی به ایران انجام خواهد داد. ما بزودی جزیره خارک و دیگر نقاط زیرساختی نفتی را تحت کنترل خواهیم گرفت و کنترل کامل بازارهای نفت و گاز آنها را در دست خواهیم گرفت، همان‌طور که با ونزوئلا انجام دادیم
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65836" target="_blank">📅 16:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65835">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt_qQ2wrBE95Bln7E9s1op5P9DVuWuy3v0b5UrnK4YABoMYcH33mpnCZL2Ez_EmRJnQZjVShJgM3KiCCMkkSrjAg-rfHUfwmnzJ9Je3DMQlkcRCWwwsk2M0QUSKj1assRMJ2Ai7Whxqf1k2zGtwXv7WXA8XxpCqgxR5UU5ebRME_va6smjPfzzR0UVAx_q8CWcEGWbvgzT6srIVv90hhb_w2_Dk6_9sQbYZMsQfki-peLwfDEuEqgN1ITEhaYbWnUthdgLJc1XAgs5Dbk4HP_J33XwZNh1G-UH9mJb2WJnpl1iSLrAZ7FG3OSSgcT5vTgWn2f3h-oahLl-P0jGgb5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ایران اینترنشنال:
‏
محسن رضایی، مشاور نظامی مجتبی خامنه‌ای، در شبکه ایکس نوشت: «رییس‌جمهوری از تعادل خارج‌شده آمریکا تصور می‌کند بمب‌ها می‌توانند او را از باتلاقی که خود ساخته نجات دهند، اما موشک‌های جمهوری اسلامی او را بیش از پیش در همان باتلاق فرو خواهند برد.»
او همچنین نوشت آمریکا در برابر انتخابی دشوار قرار دارد.
رضایی افزود: «واشینگتن باید میان پذیرش شروط جمهوری اسلامی و از دست دادن آخرین بقایای اعتبار خود در جهان، یکی را انتخاب کند.»
اظهارات رضایی در حالی مطرح شده است که مقام‌های جمهوری اسلامی بارها بر ادامه پاسخ به اقدامات نظامی آمریکا تاکید کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65835" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65834">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
فاکس نیوز:
«ما آنها را بمباران خواهیم کرد.»
هشدار صریح رئیس جمهور ترامپ به ایران در جریان تماس تلفنی با تری‌یینگست، معاون رئیس جمهور ونس و نمایندگان ویژه استیو ویتکاف و جورد کوشنر از اتاق وضعیت مطرح شد.
دولت معتقد است که ایران همچنان در میز مذاکره تعلل می‌کند، حتی در حالی که نیروهای آمریکایی اهرم نظامی گسترده‌ای را نشان می‌دهند.
پیام ترامپ: ایران حتی نمی‌تواند آسمان کشور خود را کنترل کند. ایالات متحده ۴۹ موشک تاماهاک شلیک کرد که طبق گزارش‌ها برخی از حملات به اهدافی در حدود ۴۰ مایلی خارج از تهران اصابت کردند، در حالی که جت‌های جنگنده مواضعی را در امتداد ساحل جنوب غربی ایران هدف قرار دادند.
در مرکز این بن‌بست، یک توافق پیشنهادی وجود دارد که تنگه هرمز را بازگشایی کرده و محدودیت‌هایی را بر برنامه هسته‌ای ایران اعمال می‌کند. اکنون سوال این است که آیا تهران قبل از تشدید بیشتر فشارها، به میز مذاکره می‌آید یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65834" target="_blank">📅 15:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65833">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIY-1XNpRRiLEWlchHPkcW9qoPi1oKAVY_QzPuimeEp_EUEl-toIVz17f01i3VmnK5VBVxeEZKx1-9gNlQxvTWS1HpMSxAhwnt7xjd4p1hvbyuyrfDRaSf5NZj0kcwL_1tgWzTb-0UNg1uPFmapZ_D9-uazNRToXLKJKK3jAtcnFpf8ZljQ4QtA12z9qY2s6G8tQrv7rZOZR27XqjAHOCYRRimc87-wXa22PsiYgDM5jD6YAvdaXBGtWhFb4Y9Y1hLQL13k8l-hYHK8bhy6MyIi9j_f5BmtU1VhgJ4X61tn7gifni-8SywQYGaXw1bkqCldd36GqLC3q8ZPnAQfiKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی در ۱۰ ژوئن سومین نفتکش ناقض محاصره ایران در خلیج عمان را از کار انداختند.
سنتکام پس از تکرار عدم رعایت مقررات، دو موشک هلفایر را به موتورخانه کشتی M/T Jalveer با پرچم گینه بیسائو شلیک کرد.
اوایل این هفته، هواپیماهای آمریکایی کشتی‌های M/T Marivex و M/T Settebello با پرچم پالائو را به دلیل تلاش برای انتقال نفت ایران یا حرکت به سمت بنادر ایران از کار انداختند.
از ۱۳ آوریل، ۹ کشتی متخلف از کار افتاده، ۱۳۵ کشتی تغییر مسیر داده شده‌اند و ۴۲ کشتی کمک‌های بشردوستانه اجازه عبور یافته‌اند.
این محاصره به طور بی‌طرفانه علیه کشتی‌های همه کشورها که به بنادر و مناطق ساحلی ایران وارد یا از آنها خارج می‌شوند، اعمال می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65833" target="_blank">📅 15:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65832">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
خبرنگار صداسیما: شنیده شدن صدای انفجار در محدوده سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65832" target="_blank">📅 14:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65831">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPJXtYkvKEzk9CUuW1JoMz_0rrJB7FVcWlycYVRSa1Eh5vdhPt7SjoGk4d-C4t5mLsMAzClyLPjidJfHRdkFvZW2Av-UWlf39GU0asHBwqwxYFxINLXbF8rF0cQDiFzuFQc4vxD0Zf9o-PwLsdZIfYDmZLBoVopnV1F5RWeeLDImZv1okopLpUIIFOczpJUYkrtkTESt0N4k_cp_uaHXaPMXr4cUPTjaCoffHw5eXspa9t6TwzL3nlrgAutdSm7VsKpGNjtd-o0A-oLSnlTEaKitO7pF0qG49cIv4XUYwYX_-PavfOL-EGs1UnS9Tb6OQCItsvyV2TK03pH6KEOjkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚬
🚬
شاهکار جدید رستوران های تهران:
⭕️
پنیر+ گوجه+ خیار+ گردو= یک میلیون تومان وجه رایج مملکت!
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65831" target="_blank">📅 14:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65830">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
دلار: 180.700
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65830" target="_blank">📅 14:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65829">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
وزارت خارجه کویت:
حملات مکرر ایران نشان دهنده رویکردی سیستماتیک و تهاجمی است که کویت نه آن را می‌پذیرد و نه تحمل می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65829" target="_blank">📅 14:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65828">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7-IhLWtl8vuSYbeahs4CQYxPHXJjqw7viVi8QDB30uaNIbTjk88ZEUp1Nrl3hnGEl871xhqiJi6vqdU4Kb3OD7b-eJRq6jd41KVM6HJjUNLjby9w-2PEt725SSaxMCHdYQpUDVldMJlsvpfstNmPD8f8A5EY_IGE34kzmKZwR3jKrQPXngmvAINHg55eCFIhVE9B45U8qEj9fX_u1dQ0T0Oln9MysqDQNJkHXvSSQg9TGgvRmDOopd8WqEjkHvwWC_aNAX5e8kEPrpvo_pEmWSfNwyYETgVtSXvPf4QieFJbiSLl-ZBX7hnVkX0m64uIZrSMCjtY7dL0i0wI_aivQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل به فارسی:
دیروز عصر و دوباره امروز صبح، حزب‌الله، نیروی نیابتی رژیم تروریستی ایران، با نقض آشکار آتش‌بس، از لبنان به سمت اسرائیل پهپاد پرتاب کرد. حزب‌الله به لبنان خدمت نمی‌کند. در خدمت منافع رژیم تروریستی ایران است، در حالی که مردم لبنان و ایران هزینه آن را می‌پردازند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65828" target="_blank">📅 14:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65827">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwbaNQYFR9zDtujXWsd7HdgLVYKsxaIF-ybpraTdY3PSuxoCw9QJRR5xsj7SUlF4PJdB0nEEcyzx1Lh4-qWADvxBTP99To7pI4GoKVorU0KJRvJsV0Qn9ioJCkrDGGKrjIbx7b6Dgc92hhPmZcoxVTI7GUQUpmrmBo4ij2RVRIxvS5SqprvTeCNyMTVAnzdvS_e_kSb7HQLLOjblXW6IFWcCHTLCkvmi_Lr5TTap7YLBpvr84l6_Xv_HoDI6osirCVC25XYjkEv4MEcOR_Z8Q_H1qdGSd8WksVYPQMUPpybOx5BLDc3AdDvhJTQxD0-DNzHWpFbPrDoNyaJ3I-qXsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سی ان ان:
هیئت قطری امروز صبح پس از برگزاری مذاکرات شبانه با مقامات ایرانی که با هماهنگی ایالات متحده انجام شد، تهران را ترک کرد، در حالی که حملات آمریکا به ایران در همان بازه زمانی مذاکرات شبانه صورت گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65827" target="_blank">📅 13:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65826">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a59b3948d.mp4?token=tMVFNiKDzARYHOEOqWYKGBJ5sgg5OLGGKsgwmLdM_eTDNw0l05mpJ13KRDYugQUiby_5MzLdtkt0r6a3hHgVEKKSewkwIrIpxRcmkQY0q9pQFhYeiS87G7UEiatt52Ds0ocD4MzbMMr32F5pSqDkycMoG8VQkY4EtFJMJSPwB4hCxxO5re9sZPththPyslYdiwxqrePhj6mbzRgKTTf16sKVw8cQvbW6q0lqFELpZuygXg5Qb4NttAsDK7vjO6yVxu63aeJO0JweV_qpBtX5FKc5o1n109SHlAJK4rxOqPX7z2bzcSmNkYpa_BiGfT8HKi2ERt7FPdCrTK67o32hAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a59b3948d.mp4?token=tMVFNiKDzARYHOEOqWYKGBJ5sgg5OLGGKsgwmLdM_eTDNw0l05mpJ13KRDYugQUiby_5MzLdtkt0r6a3hHgVEKKSewkwIrIpxRcmkQY0q9pQFhYeiS87G7UEiatt52Ds0ocD4MzbMMr32F5pSqDkycMoG8VQkY4EtFJMJSPwB4hCxxO5re9sZPththPyslYdiwxqrePhj6mbzRgKTTf16sKVw8cQvbW6q0lqFELpZuygXg5Qb4NttAsDK7vjO6yVxu63aeJO0JweV_qpBtX5FKc5o1n109SHlAJK4rxOqPX7z2bzcSmNkYpa_BiGfT8HKi2ERt7FPdCrTK67o32hAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات امروز اسرائیل به اهداف حزب‌الله در لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65826" target="_blank">📅 13:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65825">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏
🚨
🚨
منابع ایرانی به رویترز:
ایران و ایالات متحده هنوز در حال مذاکره درباره یک توافق اولیه هستند
تهران هنوز در حال مذاکره با آمریکا درباره مکانیزم آزادسازی پول‌های مسدود شده است
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65825" target="_blank">📅 12:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65824">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7dae3f50b.mp4?token=gwpYiLAGkHnFvAnQgXF_Yt1LFI1R3pg3rKtrym9asPwQaWBt9SL4dZr9OxalA6hKk8ZtSdk4Pc_7xljRG2MC0umQxOFxKqZKgUry7IkWqNl-5UZR11I3np8O3TIJk95rSvLPNtxPTRBPNmA_48A0PWpr_d6lJ4bvwk2UKGj8SB_hNuKrSTouUC8G8TQS5KpYdKNPKFrEru42tFSOJc6aU7SxyI9-QhTodeDigL9-AtNf6A7v9KO93VLMkkmJus9tSgTt1IWCqJdJQc0LhdimyYqgzv72w_0nBxLAnJucmm0GU-xBbPr2FKxet_4lA33NbJ3aMYDlZrRA_V2XDExeeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7dae3f50b.mp4?token=gwpYiLAGkHnFvAnQgXF_Yt1LFI1R3pg3rKtrym9asPwQaWBt9SL4dZr9OxalA6hKk8ZtSdk4Pc_7xljRG2MC0umQxOFxKqZKgUry7IkWqNl-5UZR11I3np8O3TIJk95rSvLPNtxPTRBPNmA_48A0PWpr_d6lJ4bvwk2UKGj8SB_hNuKrSTouUC8G8TQS5KpYdKNPKFrEru42tFSOJc6aU7SxyI9-QhTodeDigL9-AtNf6A7v9KO93VLMkkmJus9tSgTt1IWCqJdJQc0LhdimyYqgzv72w_0nBxLAnJucmm0GU-xBbPr2FKxet_4lA33NbJ3aMYDlZrRA_V2XDExeeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
واکنش پزشکیان به سخنان همسر سرباز ناو دنا که گفته بود حمله کنید: انتقام که فقط جنگیدن نیست
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65824" target="_blank">📅 12:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65823">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">1xbet_ir.apk</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65823" target="_blank">📅 12:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65822">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65822" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1️⃣
▪️
نسخه آپدیت شده اپلیکیشن وان ایکس
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!
• آدرس سایت 1xbet:
🌐
bitly.uk/connect1xbet
❗️
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65822" target="_blank">📅 12:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65820">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88e4c73c3.mp4?token=UXrmBDT222TEBi8IYDDYHk4KMWWhLN02btlNtmPZdYNyttgJ0pnVipSzJWhHz7AgIErdCfS9aTm8VY9OA5VPmY1GGUXpBziME0RdNnD5sINpFtO6jJ7CP74bRX9BFKV2RWyJc3NKutrMkAQR672dhrGXAzOUM_yxlSGfeDprgue6YcXCdsNiZs-DxKSz_lFjTnPSOsYhf8fYvQg0NHE07FKxJni0LntumLnZJgkcKXIqOjn_rPtUVgh5__tIhtrSSVi4HkfC8DUVzuRVEcljY3Em_wKQ-zlRii5oQhunlcuFkgAQA8Lc3K9hXkrrIK5Yv3DJwKBP4D7E44IKVYEviQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88e4c73c3.mp4?token=UXrmBDT222TEBi8IYDDYHk4KMWWhLN02btlNtmPZdYNyttgJ0pnVipSzJWhHz7AgIErdCfS9aTm8VY9OA5VPmY1GGUXpBziME0RdNnD5sINpFtO6jJ7CP74bRX9BFKV2RWyJc3NKutrMkAQR672dhrGXAzOUM_yxlSGfeDprgue6YcXCdsNiZs-DxKSz_lFjTnPSOsYhf8fYvQg0NHE07FKxJni0LntumLnZJgkcKXIqOjn_rPtUVgh5__tIhtrSSVi4HkfC8DUVzuRVEcljY3Em_wKQ-zlRii5oQhunlcuFkgAQA8Lc3K9hXkrrIK5Yv3DJwKBP4D7E44IKVYEviQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از کشتی JALVEER که امروز در نزدیکی بندر شناس عمان مورد اصابت قرار گرفت.این کشتی را خدمه ای هندی اداره میکند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65820" target="_blank">📅 12:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65819">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDGtmUZJlAn_lNBaTOW-qS4c6QfVmgxSpEl88CLI6Uf6VIT6_r4do0rrczUK1xAFsHHO3evfC60QsRTt5Y-80iujDvRVuLuQsNFHkM3lmhWc-pM0kaPYIQhGHbOB0-ix-mvYP8SiB-7uiL1kXrAcvohs1Gc7GTHIaxiZ3gIJxM7gak3uZeJbBsVI9zysdOc0Hb05edkt-GuIEN2Hztsoi6gRCv0PWgaO4veQIhKEa4e7MS1qg4N78frbwBzgDkYKhPUfS2-06rEMwhKFV-Z8QT3-lEMqPRfg8_i8_MCL1BEPxm-GlTOxD6KdbCXa6YCKX-BqoDdDB0F-KI2n96mKAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه وزارت خارجه جمهوری اسلامی در خصوص نقض آتش بس توسط آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65819" target="_blank">📅 12:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65818">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bec45c0e2.mp4?token=idCMg1QqH1hPw55ZkEbDoEEm8fKM9K6_P2Yp7dapGkJhLw9JDu4eVGRmHxp02thwL2TGBZvv_ScaSyMgPeF0DMAVdslz09DrODSiRlDSX0c_RwFYanKu0asKn27fRoa0uSnLgqTgYZIm9pjFLUsUzR2oeaqce_rD0qV-aLFVDiPBXM6_0NoQ9bZ08icAYTlpUxuq4SV7A5ygZPCzhvj_7qkknNkxlfclz4DHiDxK_E7BdV8R_FQlYvdZNlnY2X6pUNW0DwA2ovBf4SKc2cf9rU1Nbry3al3UDZEwwTw5euOrEHL8R_Zi4ySX39_zL4xWbA53pC6tot7ZlsQOVgr5fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bec45c0e2.mp4?token=idCMg1QqH1hPw55ZkEbDoEEm8fKM9K6_P2Yp7dapGkJhLw9JDu4eVGRmHxp02thwL2TGBZvv_ScaSyMgPeF0DMAVdslz09DrODSiRlDSX0c_RwFYanKu0asKn27fRoa0uSnLgqTgYZIm9pjFLUsUzR2oeaqce_rD0qV-aLFVDiPBXM6_0NoQ9bZ08icAYTlpUxuq4SV7A5ygZPCzhvj_7qkknNkxlfclz4DHiDxK_E7BdV8R_FQlYvdZNlnY2X6pUNW0DwA2ovBf4SKc2cf9rU1Nbry3al3UDZEwwTw5euOrEHL8R_Zi4ySX39_zL4xWbA53pC6tot7ZlsQOVgr5fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لیندسی گراهام،درباره ایران:
اگه همین الان توافق نکنن، باید دست اسرائیل رو کاملاً باز بذاریم و خودمون هم از نیروی نظامی استفاده کنیم.
امیدوارم اتفاقات امشب باعث تغییر رفتار بشه.
اگه این فشارها باعث نشه که بیان پای میز مذاکره، باید استراتژی رو عوض کرد. باید با تمام قدرت وارد شد. کار رو یکسره کرد.
بعد از اینکه تکلیف ایران مشخص شد، به مرور زمان مردم ایران می‌تونن کشورشون رو پس بگیرن و مسیر صلح بین عربستان و اسرائیل هموار بشه.
همون افرادی که میگن زدن زیرساخت‌های ایران اشتباهه، باید بدونن که این‌ها اهداف نظامی مشروع محسوب میشن
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65818" target="_blank">📅 11:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65816">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0v_tLczbLtNU9ql5gEvu_c2E_-V576XnHw5a_7sDMAOsh0jYqaC0k-C-srQLEQ65qpr493MfbS2Y0dqOyk2U9FnrXFAB6PFyLl8aY95tSQ9i21v6XGyWD7TBoFwq6S43yoiEEzmizbIEWbs5yI2hXU2qHHPjLcanwxI38qrivLlBWkW5i0L7CNvyM04V6uiTIlGYAYI5dhwUPd192wCadUQ_s3Uuj6NdjdSC6IncUFrv_lQYkXo--Ke47rzVYwGj7Yww0d69hBUGfXjASauQjuEIzmP6GHA928Jnax0silyLHxHlSv5J9zdsrYOqCcCbvWX4mhcj98UkzxYUdrLFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qOYjnIzkVJmRLXpqGIlN6hy9eIyhFChRO6-J1-KPCO2sfZfBIFHECQ8LUFWy846KU1eLFdyBJsaZMuWzRXEdhewOULCIleBITceoQpeiLz2kqkOUFgcIztb0RQ5SuJwdofnVok6ygmg3mgwGj7ZOO7Pno4w9XGWBtIt-VJBWd-08pDbdhiRxbXGpn-xarVillXV3ffQQ29xKi_stvEoGjlrTzOFZ4MMRJOvdFrsjxKPHHdu9KvclrxjppRm9I8uS4JuFWH4c3DfoTP0pJ_YDgMAkxJX-l3kSpasR8UcJ8NbSO-Ie5e-9Y7JlOJq3B0XSNIDrpZirfCARUpIKxq78Gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وزارت کشور بحرین:
این خسارات مربوط به حملات دیشب جمهوری اسلامی هست و دختر بچه ۱۱ساله ای هم توی این حملات زخمی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65816" target="_blank">📅 11:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65815">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaF8q_kQ2AThq2Eaks-kh18TJfF-HYEgNkrqOdHJJ8UOSHaAu2u5K65XTcodxVzMEFOxEcl6UVDD26xCNAHJDbfTZjdSn1Z3L_tSxoOvicpIV8DxyfdEUO5ylljKlsrCzxui2RxHCXliGRfQmSGERoY7WRmvuu-XiJxDKBRv3XJ2GZFYOXGjip9xDl0G7nQuBiXtip4i2T0ba7ZX9_BESCZFZvHrrGuffJw7fmeFsGeC7B9-HLuemoO51O0PXVMr5HXGeF6qvZiEJuqioWuHTETdF5qYRjOeeTZ352fLNZsjitQVhU_qt_p6vB8FEHuYS3cn7gTBFfLhgmtO7pOQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلمان از پهپاد رهگیر جدید «کبرا ۶۰۰» رونمایی کرد
شرکت دیل دیفنس در نمایشگاه ILA 2026 از پهپاد رهگیر جت‌محور Cobra 600 پرده برداشت؛ سامانه‌ای که برای حمل و شلیک موشک هوا‌به‌هوای IRIS-T طراحی شده است. این پهپاد با طول ۶ متر و چهار موتور توربوجت، می‌تواند موشک را صدها کیلومتر دورتر از محل پرتاب به منطقه درگیری منتقل کرده و برد پوشش پدافند هوایی را به‌طور قابل‌توجهی افزایش دهد.
کبرا ۶۰۰ در واقع نقش یک «سکوی پرتاب هوابرد» را ایفا می‌کند و برای مقابله با پهپادها، موشک‌های کروز و سایر اهداف هوایی طراحی شده است. استفاده از موشک IRIS-T نیز به این سامانه امکان درگیری با اهداف مانورپذیر را می‌دهد.
این طرح ادامه‌ای بر مفاهیم قبلی آلمان برای ایجاد رهگیرهای بدون سرنشین مجهز به موشک IRIS-T محسوب می‌شود و می‌تواند لایه‌ای جدید به شبکه پدافند هوایی این کشور اضافه کند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65815" target="_blank">📅 10:15 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
