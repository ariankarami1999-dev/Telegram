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
<img src="https://cdn4.telesco.pe/file/VMgGQxL6bhKehABhUIU8wDVruIKyQWqiGnqdqqRGGVG3kzH_lpok2_axE78H8lGXxf9elbnY3bdzSBWVIGi7tdmxJ4VXyT8HB-JdERodLGxpZBhS2hClsec_hTrX8vr_q75VACr8K27kWXKRMVHbt3JN7wokYvxL8MvXyn-eiYuMTZLhBp4yyYFXRuIgxwKBJx1ghayHbcUUCayKBEJP3Ie0PscF9iOB3geGmDOs6Hn-t1x2KGNcP2_XSkDM2tEdZUff2b3a2ggcPPOZp5QRcGDCuaBhBzNQepyXeZLEu5f-eHkD6CLRuNKqqEXjrqd5xGejLsimrSZWV0cHp_LKLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 135K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 21:13:13</div>
<hr>

<div class="tg-post" id="msg-89951">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7iNDEZHl02Bxdjas8JwI7nLWdvF2D6g4YQLrEsocGNTspU8gFmbqyKxxIf-OnFZMFDDPW6B-HOnvNvzxOCJCzbMLyms9RLQRUPR3tM6SRMlx0Q8YOlurVzh2pyZqXYTmhBA8G1m-2U37n0l-OHUEAon4EZJh7kPtoDTKYq3rb76puJxnYvESDpNUs3TRhQmgrAtiAFtVByguuG8iqCKZNMzYhf4DYXfud4Q90CRVnVs2Tuw_Vkh5j0S6hoowrS8VCTEM9YmyyV5jtcJlSWS0fcsArsYnjZ6kkmxiSuC6YqvZj_JAgtlvUBXdQ_3BFECi_WkhSNZBi0fqhAffMt2xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
قرارداد آنجلوتی با برزیل تا 2030 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 962 · <a href="https://t.me/Futball180TV/89951" target="_blank">📅 20:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89950">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5OsKhxtyWYIoH-AYFnP1saohpso6WvrJHzb5fEZnCWzNNX3fZEIIgpm_UBjg9MyZ-T6EPg5nfdKOKHbnxWKdz1z6epgUJnggJZIlF6mlbAvGup8-zyQsuLJwIQdr7NEF73id0wY33N7qSql0ptlCMYnr9ltxS2ZIWusz_QVg-XQSAYGMtbYxiY92aOSWXrGMKLN9K4SfgdFWY0HfT0NgbQ7Xgf6nN-X-i6de2kEenwOTBNIxfdto1_E6n9PHcDfaMFzNbOVXJZ0F4yOYiZ5lUvr-Hfpq_k03XgL1kxfTYsCL5TYTsDPt3m7HMXkILUBHAq7RwgZ1I5U73Cw5hEPuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
فهرست‌ابتدایی کلمبیا برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/Futball180TV/89950" target="_blank">📅 19:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89949">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🔵
یاسر‌آسانی در گفتگو با مدیران استقلال اعلام کرده که بلافاصله پس از پایان جنگ به ایران برمی‌گردد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/Futball180TV/89949" target="_blank">📅 19:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89948">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMbBAjw1LQjAAQoz2o8WjOSoctmleMwLtRamQHZ9IKYeqdCxUi-aVaxnN45SHdyqMBQCf7538LELWstg1JDPjDYibmCzTPI13z23JC4QjeZYQq0fVQt3NYI3EMEUvq-fSbLDxPOI30gxbk2tqKetuWQXbmCJABf1FSeZWXmOS7MpJCElFRb8pjXvEk1oIV_8qe0UJSW8iqnPM-jJ5mFZW7J1Ow28kAaXh01J2V01st-I5DBH24kZYKrELIrfGatOVqtQB6X17hTBhyImKKV6JRlXzkbbIc7CPMq6gdROduI4ohHSvSMyOveRJCZp3QN3uGhDZOH0qUlda0SqqR-5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ژائو پدرو ستاره تیم فوتبال چلسی هدف‌بعدی نقل‌وانتقالات بارسلونا در صورت عدم جذب آلوارز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/Futball180TV/89948" target="_blank">📅 19:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89947">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/173bf1e753.mp4?token=hXJW-Zpx-K_K_eZo2x8YfQU4iIRKRhFzzB7l-nXVQ7ppvW53e-fWBHeNKaorfG9qUsm69Sf_-5YXsq6OfbZ--aRqCgkvYV4CVW_i_RTRJ-NltQywrdCL2olUiSZlbL_93DTBlbHexShf3h6I6U_5ycP5DqxJvU_bIofIyZxs1siujvMF5_o723mj3FzFFRyfkAd7Bft9q0HHWxKB1jRsaE_sHy7EmFOleNRnmRkfTkleuXlPRVyyagIu_3VxaDOJn0j4a_aRJPI-bVMCKN8h_e6QPwEfsjchFVZNHGc17NOyiYitIHGwFUwPSIBGeTDoBynHk2TccxvM0UvSFyd1ooO9fLp0x4C_JKOcCYiBEC8alCx2zGPF2dCaFeYVgh3IxdC4WIc-iS50dEY0edAYnAkLfK6uEbrupOjkRQs_16qyBH4kgGGsAd3uYT55vRPmRy4GB3sSGPDqusvjQZNGVj_IzhzQGAH3maYmdYoq5up__NPqHpQM5vslZ1mXOjw-dnsVShEhrXgc0BBkEjA65rcdtdpkVgzbpXbJyjKvPyYqT7TcWzop3peq2kayh-GydmPuiliKubdf2Jl-IVLq8RTyEhvhKzzxWEyorL9BapZCuQICPFgRa8DE0PaDqILcjeLbD1XcrjwmiTZf4IpFSfzzgvWPGpThRRoZMVbP-GY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/173bf1e753.mp4?token=hXJW-Zpx-K_K_eZo2x8YfQU4iIRKRhFzzB7l-nXVQ7ppvW53e-fWBHeNKaorfG9qUsm69Sf_-5YXsq6OfbZ--aRqCgkvYV4CVW_i_RTRJ-NltQywrdCL2olUiSZlbL_93DTBlbHexShf3h6I6U_5ycP5DqxJvU_bIofIyZxs1siujvMF5_o723mj3FzFFRyfkAd7Bft9q0HHWxKB1jRsaE_sHy7EmFOleNRnmRkfTkleuXlPRVyyagIu_3VxaDOJn0j4a_aRJPI-bVMCKN8h_e6QPwEfsjchFVZNHGc17NOyiYitIHGwFUwPSIBGeTDoBynHk2TccxvM0UvSFyd1ooO9fLp0x4C_JKOcCYiBEC8alCx2zGPF2dCaFeYVgh3IxdC4WIc-iS50dEY0edAYnAkLfK6uEbrupOjkRQs_16qyBH4kgGGsAd3uYT55vRPmRy4GB3sSGPDqusvjQZNGVj_IzhzQGAH3maYmdYoq5up__NPqHpQM5vslZ1mXOjw-dnsVShEhrXgc0BBkEjA65rcdtdpkVgzbpXbJyjKvPyYqT7TcWzop3peq2kayh-GydmPuiliKubdf2Jl-IVLq8RTyEhvhKzzxWEyorL9BapZCuQICPFgRa8DE0PaDqILcjeLbD1XcrjwmiTZf4IpFSfzzgvWPGpThRRoZMVbP-GY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ستاره روی لوگو فقط برای قهرمانی آسیاست؛
تاجرنیا: لیگ برگزار نشود، قهرمانی حق استقلال است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/Futball180TV/89947" target="_blank">📅 17:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89946">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQJqQRR2IL7TRFILrPSqok27xWNAzeYQb2oT1MvC8CgaW3c7GyNaQSEas6lziQgrIt1y52TuZN_Kc_TGD0TYTHUvmNmvUvxkhId4lG4Gxc-D0Tl7XyZ8lT-qCKC7-qfWAsrPshZrrTOeAQW_180FqtOegFvHs25cA_CNmLPWfBHw1pPANdMO3xJolFpMhYOvuYomcems0cgXIeJzB3JD5QBvjPZBI4mKquLqoYc1PNl-hoMNC_qmwQcZYN_Rqn18fOm5wCkSNa3Vp6Q4Hn8-FX9-f_Nbf1Xunz7diri81gGzf-LetPsORY-2cI2TtesIkPKo0vwdWyFgW2XM-kQFpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامزدهای کسب‌عنوان بهترین بازیکن فصل لیگ‌برتر انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/Futball180TV/89946" target="_blank">📅 13:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89945">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89945" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/Futball180TV/89945" target="_blank">📅 13:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89944">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izKnaI8-pQeeu_dx82AY_78hVOXBsqjVxKx9-jX7jL7R_10TtNE9uIfPq1-48y6CyLzTzqqm-N2PELORFDIPSR56xhcRZCfveKe1FbkJttrLBjSufWZGiEPCXwncLMe4zlXgpbPnexp_TK17TRyBFOQNmng-Amv_PzArePZ5-yl3idYr5oYgR4xmd5QE-4iPrJMbVQBCsupM-cYYEWkvmCmhGekLvnCoHfTiFiBTEKROdAVb8lLBLrA0FDEZ8AoxnMzMbomFHZvhN_d175eVc6YkMAYkfw06k4V_h-1DvcJE6CKj2KYzM3JbJHZ3fIlEF9sSv0Bz1byigre8m1t7NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نتیجه بازی جذاب
🔵
منچستر سیتی  - برنتفورد
🔴
را در 1XBET پیش‌بینی کنید.
🌐
بالاترین ضریب ها را در 1XBET پیش‌بینی کنید.
💎
گستره ی وسیع از گزینه های قابل پیش بینی (قبل از شروع بازی و هم زمان با پخش زنده مسابقات)
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
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/Futball180TV/89944" target="_blank">📅 13:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89943">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e925e8e321.mp4?token=H6UIYBI5HD_BmVZrTpFVzfmWfaMulK1ywYTZN4FKb0fRMz30kCqa9-EUXdycoDTFOXXHx8E01E2HPVc9_r3X_kXED-B1cAyWy_nyqAxoJGIoBhRikD4wGlrREsv6ntRQsA4eLRtNMtd2pupUYn6t6Qcnt6LpHR-PmuUnS8oxBmkV85wh1TTqWqcemac3mrapQez_wW8sY7jLCRcdGAgxsdRzMFcyUK0H_u6euaiTzDH0SqRwQMBBAtir16VEEaZuooQJjZF4ktYo2GFoQRQGmhmuDSLGHpr07sNwBhbhwXmqLIub9l2RCdVIatQh_NtVWaSqrzPBxHSFuC5VIxluHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e925e8e321.mp4?token=H6UIYBI5HD_BmVZrTpFVzfmWfaMulK1ywYTZN4FKb0fRMz30kCqa9-EUXdycoDTFOXXHx8E01E2HPVc9_r3X_kXED-B1cAyWy_nyqAxoJGIoBhRikD4wGlrREsv6ntRQsA4eLRtNMtd2pupUYn6t6Qcnt6LpHR-PmuUnS8oxBmkV85wh1TTqWqcemac3mrapQez_wW8sY7jLCRcdGAgxsdRzMFcyUK0H_u6euaiTzDH0SqRwQMBBAtir16VEEaZuooQJjZF4ktYo2GFoQRQGmhmuDSLGHpr07sNwBhbhwXmqLIub9l2RCdVIatQh_NtVWaSqrzPBxHSFuC5VIxluHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تاج: AFC چون زمان نداشت با پیشنهاد ایران برای اعلام سهمیه‌ها موافقت نکرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/Futball180TV/89943" target="_blank">📅 12:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89942">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF1G3YxvcmPNpL6GRRRMS4IooRjuQIAbTzxkGZYHfuO0KG480YNp7imY0LmHBwTFaq-zIWtWx3EmNKaY894QEcpWYOrx4079yTb76iHXxsQ-M3DRkv10Fv6yIdU8F85Pa5N7iw7D1OAMtckoe05IewnRlILZwp8p8t199_t-izTdGgqLuaTrZ-VMO4DBQZG2jQi7b5WTeeENwJwWlT55V1WtpRmTQo8v4fVlvzowtgiH18KHV55RbQBXj6rh1Kn9c-5aZ7H0uXNmnojRsmw_y1mezQQtf4EJhvp8Dkjnqam5REYTwvuAk6_mrVAtsJPRzsPe6bXT8pQDiK_r2ariBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ژابی‌آلونسو به چلسی
🔜
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/Futball180TV/89942" target="_blank">📅 12:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89941">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fru36ND6T1Cs3efdRRJ-NY9L4MkL19wmgMD1DVsBEhRdVP_MZHJYyEuoOdrW9bu_c0_IJGIwkBcceH5voRhOct6DRk7gI78C-2mcL8KCjMFs0gW26WbPJtoLgqErmcw6-ZlKDiSQ07TJZM5CBamaDnbVe80zdBBqcbX78ejerzQKQ0tjdIwNj0OhlsudGl5OII4DEeyFvJXfhy2k9ocOokni1MZk_h7yu7urSm9hePJrllGnE_SXvc6GnnmrUq4IBD0KcmNx-E6LPGzXbotv0PE8Uj8iBJdqqMiBr63b1Ucj_n2ITlCIVMaJlAKGzWcVU5FN_1PEfQLbAB-oLqWaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی از کیت اول فصل‌آینده منچستریونایتد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/Futball180TV/89941" target="_blank">📅 12:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89940">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvujH9Jq61qOUcbaN0h3YzFe4uP3hsNaHEwAh-l5bTUBt9Gqs2CtgOVxcWhVLtmMJN1AZeDBVyVkpsK6WpZaRVov8-DbvkWXAssy2TpN5XaVIKivPX4rmSNx8zxg4R1_371qu5uynoRnfUxkeU-jW-YcQAhEoD0kuCES4B0Yanq8dwIavEtZzioe0xFS-1tKf1mwZeXrBAj7VstYv_zq_nERs9tE5rwzlm9d9TBU4iOhxqm60No6wtYsYuyx5sqgBORRbfkEkNyM01JZOugA4Yk8uASbme08KrtTSjqkPnDYyvdbQHp3Azoo939G8uSvKbpRUI8EN9RcNCaseWcD4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام فیفا، در بین نیمه بازی فینال جام‌جهانی، شکیرا، مادونا و گروه BTS اجرا خواهند کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/Futball180TV/89940" target="_blank">📅 11:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89939">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZuP4t1r4QcxVYuPf2lbo0-_7US3Qsw-Elj5yVyn-icyIijrx6vzdt5Vw9u407SAyZyXDZMj7mcs5CT5hSgXwjlOsHPKHqhWt1gIzPqgRI_zg-YT49WGND0agvCufiJJQXfwBih1gXzURoh5hmCCWPSA5QgGSHx3osWdivaDV0h5VHtIMwRWJ__e3DWKCL3ovd7yZc9iOsadb3ETN9ATiPYZ0UOLUpOkjD7cwDVa5i9GZkhFSEYBVcOLzUpNvRS6hEWiL94G0Js1Bjkra5-npDgg25iDekEcDqCmdrMM3iDEjo30d2Z7gOmrgN3Hx183BwqzoCE3iiiV1SWuAYHf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اعلام لیست نهایی بازیکنان تیم ملی نیوزیلند، یکی از رقبای ایران برای جام جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/Futball180TV/89939" target="_blank">📅 11:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89938">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qf-rbjOePQ5XCaZCpRo_NvGbcfZEvslFyzOhbi3wmZ0dHi0Dba-a7zBOMh8jAMDktm2VeEZ3Jx976Lnrc8VMmbtIP2JVroxoc9na3Bos5udiYxbcXilxXI1Mryy2LUXIIwOs0vdA0-M54hN9L-XGCq-0uSwqUIQnPujP4TXmDDiMy4E6p-CFpiiSTJU-17Un51OR4wjx26i4u8qt0T9wJu5m6gD3Gnf9_5QpZ_SggvnvjVcFXDN3WQiGzke9WMmfsAz2OCc94nLpXTv-V_0Y2aLffk0QK1Q_QnVelExvP4AlH1y5xQXGrjjjs3cqdm2aFlKj1tyxg9kmiLjoeIBcFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نصرالله معین خبر خواندن سرود برای تیم جمهوری اسلامی را تکذیب کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/Futball180TV/89938" target="_blank">📅 08:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89937">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/Futball180TV/89937" target="_blank">📅 00:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89936">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pqszfrTzkKApcBBKIRe2RkXucZjFRm2JefTDKY7hBLe_S6riBkzJdphKZPzM_JuAICbDcklS0ZlfPslD5vCnxPg8a7p0ytFX--6ZyRA3rHqaUQ_qPVaUoMWziOtqCLCorIALfxQwMiubC7T1JnSG7jPZQRX0hQlbzDDoieAfbofiW4a2mRSxXGwTo0OkHT-5zFe9p-SIsW6zqT9rVGkOSmO39frZ_6EQfcoRXA0OthsPNVyXU9pkNFTqLL5dADaiGhmx0PToxo4gTifC-_xW5rME7DQY34tlQu-4Tlfyv3aVfaFr9Dq2irBe-5NflRMi_rlTLbt2g4ljW1U1Njn0vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/Futball180TV/89936" target="_blank">📅 00:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89935">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqA83AqyPjvJUwrgoa34TQUL3UwkwUwIVfUv_TLr8KoCemp_eTkQBoK-FPXGnjA2dyrjqqjAvjBQFubj1xpr6cQX8mhM0UYpLxgbRr6wJRA_JrxyzH-7GvXkpCuPQBGoPI1a1WfqJHLW-D6GBEuyFp4pTFKmOVFdCWcxEr4huyEw3IdR9ffmrKXUfU5-s9X8RAo2_4xPTijyR22ca6BOev7sByzUnOGHjqBdmW8nS75wSV11qGarMa1wdNjzpzglrfcJ8ebNm2itN5Dy92i0thcrdIlpQgH9CIf9dnPX2o6yXRZEMfAlAfgMozH5HCj5JvgbD8pyApeLzIh27LqUjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🇫🇷
پاری‌سن‌ژرمن قهرمان لیگ‌فرانسه شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/Futball180TV/89935" target="_blank">📅 00:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89934">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeuE5fZqt-gjm7fB2UXTbs7wPKXK_jAhfBckdx3QXLtBwmC79DP1KCZTPEz3PUxaBWQ3H3JycLVM6xn7wgXOMGGT1iQCoLfGIcLyNmjk2Y_viAWlNwpM-12b7cC91-1_lbkztarXo4p1NEAa78HniAbN4PKlu2wAVdiJy41u-ZH9qEL0NPPRnapFZD-ZbmMAbIWygY3yYd2JIjKM0ovyp4R2UeldWIXa9IDyZBTgiCdFZ4nvhoGVTKPfGOJb-vUWpo8Zb0-5vRVeiYFvbd3Id0_sIyyib55Rd4XN5AO2vvEADUpahmGv_rFlsbFR97dg6vPwULFvdwIRkk3R4U3CUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
اینتر با برتری دو بر صفر مقابل لاتزیو قهرمان کوپا ایتالیا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/Futball180TV/89934" target="_blank">📅 00:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89933">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjKiv69BTdp0MGXxBIzpOOOqnDThi0nAkJjZ4IMQKIV7FI-H7sHzRtAZxJxJ8L-BxrAmwY_D1NCEHRoV6Q4gdkohoN4kM5ySpXCk9irxghZKW_OkYFvw3wXBw_DX5rZaCelzpIhOC2xKSo9vGth0aoolrGAz8mPeJ5BBnxah6Xh4eGXrDD9v3yOyAukhDMr33EkS8P0yOF-3-OfL-AEMAVbKODm4XRieR2extlZ1hcjSO6FYsdyAtgh7RLv0UExtBmkjY9oGUZ4DadDOAtfYDUSU2oQcYxvMnv_PoAky2qgJWJuglBvNfkYbmhdXoAO6bKKe6irdgCeYdLpQBNyajQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مایکل اولیسه به نخستین بازیکن بوندسلیگا از زمان جیدون سانچو تبدیل شد که در یک فصل بیش از ۱۵ گل و پاس گل به ثبت رسانده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/Futball180TV/89933" target="_blank">📅 21:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89932">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoh6rsJIEZ3zOI8H9H56dKDIKU13y1eQmX2lV3hTghRevvwInqcLmhS8jylokl8fzgq18q0qs-uw6rg7gU2F0YpKkbNtbyI9aHEgIItef_T8R3PwU3meJW0F594g22mc2FkMGcRzePXcAhLjTjzfFLKekB9uWnLVUNlILekHIEBj6D9iM10jDyyG2a-W2-pUj4bi4dRSihtSQIx6QRVLEEepZqSXwJDs1cANxOpL22YOcTsx2cb72RGIPwInz3ZUDkwJ-Ka8FYHQ3ekY563DCzEU3sU6J_CLicC6_AMVoRg-1EOf2xCF1qoy8ViN6jh44R4xdtSk9sWAjifg5hjM9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار و عملکرد مارکوس رشفورد در بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/89932" target="_blank">📅 20:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89931">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89931" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/Futball180TV/89931" target="_blank">📅 20:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89930">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY-_PaQu7pyq6oKLsrjyxkE1CvrqNZjzMGiDlC_RCQ1r7RWLYbGjBSeqE753lngq3E9YLdd1gSY7RA6xMaomakB50S_fgaZHA7loWuInpZWGdwi92m4vssl19NWG0NTarX2phy4o5eQRaYQE9b9MOBoz1-p7INWu615yBcLNKRDNrVkQNs3aUVQx5FDd583ObutwCX-5dOxsLpBHoTPmJgYvYNSjtbEXiY1fFuJ7A5ChpjHHXUHAVenwzPV-f-WtpsS4L4m_SzeV7HSRj5Kg8DAwD5kgpZXZ1dcnLHaKGZ5TqKN-Xzz5ZT1Z845K2vZRiVhV_w6OQVSMLUewvkQ8Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش بینی بدون ریسک بر مبارزه
Verhoeven
🥊
Usyk
🔸
اگر پیش‌بینی شما اشتباه باشد، یک کد شرط رایگان تا سقف 100$ دریافت خواهید کرد!
🎁
💥
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید.
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
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/89930" target="_blank">📅 20:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89929">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
باشگاه سلانگور قهرمان فوتبال مالزی با ارائه پیشنهادی خواستار جذب یاسر‌آسانی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/Futball180TV/89929" target="_blank">📅 17:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89928">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxZE5nlAX0kZq-ngOGczpMvZBQFagaUqfuGSvMEVBHk3pKUcrGJWX8fz2f3ElwimnUhh7OTqji0HiaVq_U_uO_Q7QRcXVaR8mGRls_61W8YGtQLiK3jqKP8jQMhQuecI35NLiUGuiq3koWKC6cRI68urX7B5QtFkrZKC3fSU_MokEahEmqrGcfnsvgAmYCGyKUjP9xFC-vCFbH5ovUrNOkeDxiGfbACwZzkGPfvv4BLMXethtI9EAxRRDrAOvhLePKeLbFqW-3tM62SZd4Lb6ARtsX0-dVN3_vR3k1xGgS9LK134_v41jKoQ9NlobeajZ1GTCXGFntHeAACU5cSzlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
اتلتیکومادرید پیشنهاد تمدید قرارداد با افزایش دستمزد به آلوارز ارائه داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/Futball180TV/89928" target="_blank">📅 15:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89927">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOOo3Uw_DUZJwIpSpOy4KABuuH7UWP2qAffzVkF4VDokLEEBsoRE5cT3laxUhZ_uZaZf7j9qG_dRHvRv04vFkictwPVIBx6L9upUcIEHBPK7eP52uMpzYq4l89BPWvFKOCPjeSdGqTdS4CC-2lojIAN2EzbKb-GRLkjkk_PAakzoZNAjx58hStU7Vp-pFS5Z0OQ72YLbigL81XovNLvFTPTMHf5kUCLnlM4X1l3MxsS_ezoaklNd8Z_Vt9C5GD_eMSg9Yjz5Lxv2P1u2nmrfwzdwAm_46WXiKDYClO1KvGti1k-TYGMXMlkli4Gl9QuVri0-Ks-HZyfIJhaZCZBZZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
باشگاه بایرن‌مونیخ درحال تکمیل قرارداد با آنتونی گوردون ستاره نیوکاسل برای فصل بعد است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/Futball180TV/89927" target="_blank">📅 13:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89926">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=sEwH6fx8jIYr0MjT66Pth_RO08H7pAF_6VcabKR8Q_RKSKyor_tlmt_yVMQx-jNhyBfQaaT1Jj6hg5TLMY727tT6SefJo_K_Z7IcPGuVXrqKByYcRlsL5bomVclQeFT9-zHy50lhklQ72iwRwZOTOI78VKls9pcK-anD1hjYp-mWTb_MNmcPFp2fOwSt-to6p3EdlQVSQhxYfh0cDJ-JKuGRhB1AK0ui5tzeQvPyEwkXL12j4BqdoXdbKyPQXSiu_MXHlWPFgezEUKuzaqPdKrNcGmrZfvlppTRtCHlAX0kvCqyxPsyCXdwUjCBgzCHKEET_AG2IlJieWc9j6YFsSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=sEwH6fx8jIYr0MjT66Pth_RO08H7pAF_6VcabKR8Q_RKSKyor_tlmt_yVMQx-jNhyBfQaaT1Jj6hg5TLMY727tT6SefJo_K_Z7IcPGuVXrqKByYcRlsL5bomVclQeFT9-zHy50lhklQ72iwRwZOTOI78VKls9pcK-anD1hjYp-mWTb_MNmcPFp2fOwSt-to6p3EdlQVSQhxYfh0cDJ-JKuGRhB1AK0ui5tzeQvPyEwkXL12j4BqdoXdbKyPQXSiu_MXHlWPFgezEUKuzaqPdKrNcGmrZfvlppTRtCHlAX0kvCqyxPsyCXdwUjCBgzCHKEET_AG2IlJieWc9j6YFsSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در ایام‌آتش‌بس درحال بازی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/Futball180TV/89926" target="_blank">📅 13:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89925">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfkGL1s_MXDJY9c3444LaF1d072vrGrWr1gKUTGO6KKpEz6bfq_3qHxV_ww4VVjxkRWBvA7eF7ITS3NbOsHzy3IbHH-LwoVreWMgmJNZ9vwdWW5EuKRCd-121NcenS0Rsf68QZUksaiieY9oEl4dzboovnPCp0-bfBoembJKK-B2Y5yOBWVLK1fXyEDrEDvDxjjWqE3Q8IAQp3zkx3V00gwAvuBjW5_0jqghekrNil6Rahtey4sGetBcTxYcXSGrxDR1NiQmZ3xo1naOLe9Gcz8k_usjFDPBYcVo7bduUF2deEI6wUvu5yvbIhhSDfp1zg8drCond8YIoVQSrNvAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
برخلاف اخبار منتشر شده، رئال تا این لحظه اقدامی برای جذب رودری نداشته و این بازیکن بزودی قراردادش با منچسترسیتی تمدید می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/Futball180TV/89925" target="_blank">📅 13:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89924">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeyD67d9b6MjB6jRSqNOtlvYn5WB2uvoN6fdjLWkKduTocCvIt1-1KD0BlKEHjJ1mGmNszHj0kpr_5UKSSozDs4lhxdMJDoPfvq0KFcoBnFkP-g6ahmuM3BF5aX9M_L3_mLUexIqP0HmiF_6hAXkCeh-qbqkA89GOFR1vNM_fAVFnwq53WKqasEbCN8DhI7Nh7ecYZsbw2n0Lva4z5U1VMW6gJIXmtg6zhWynt9-x5gFWypqZttyg6Fx7Fq6F7Umuzk5G5KHhNmDv6ZE-lStSP855JrLCYbGy3-zS_n1KUjheCUfnDtn0P7kxZ4Z1EfRvGsC3EzaHsp0Z1I55NS8cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
یک خبرنگار مطرح لهستانی در خبری فوری اعلام کرد رابرت لواندوفسکی پایان فصل از بارسا رفتنی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/89924" target="_blank">📅 12:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89923">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzRp5WlPaGvK52VAzFOMfm8ZgEgM5yqkyfBecyf1cQfV8QsADgjUmmZbQXwFqjmgd0Y6Ylb21f9Zqq7qZ8AjBQE5Vwg2VreIildkf64EWmMToSO5JoWOBt0btpN6RNPoIwQz1gY9MqegC8Yo7EbFzoc6vE_r0WFnBauLoq1F6HHblTW7X-qepnyFtU40MiDm2FPM7NKChyqNMJ1mqcubBjOIdg3aaolnT7_uj25avNRyN0ef5mW1BmZVWK9VpuPOMbyiHb_jTi6jSByDnn6VlHpqAcQ0Cr_NkbUAxMjC41nRKxafuPJt1XRv8CyCmNmLo0C8Zw8uUBBDyQX7YWaoRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فلوریان پلتنبرگ: قرارداد مانوئل نویر با بایرن‌مونیخ تا ژوئن سال 2027 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/Futball180TV/89923" target="_blank">📅 12:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89922">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggHhLijzrEQu3kEWNg0P1jBckDpybQnxag-YgKft4rtkoeppIXqGUFWVRHSSjuDZ-3KDOdtVDdvHW4y-CDuNzMu2RCV93ZPpJolvmI6870QcOwcgzpbEszStiwEZ470gvG-BTFcG5u2KnsQEz5pbu1N-oWOKP66VQ5AfZx0DqTJ5hTr8k6ZfKGDI2iAaSUir3tajplaJ369znAORCA1F7D-r2Mg-gMUNTwrhMSJZv7xOM24dgWROsLiKwxy1uLTPIHHFKolOlH-SjtDDI5SpCv1HNwkh9IYY_DZJSzYOM2hhKohOREGjAL-a08PKF-1uxO2d_hCt7aBD2bBD0A4zjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پاری‌سن‌ژرمن قصد دارد برای جذب فده والورده از رئال‌مادرید اقدام کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/Futball180TV/89922" target="_blank">📅 12:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89921">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uELcb6__gYZPvmZGYxSQbeLfX5DPmuxV5PaFp5YKjvBhtZL9ewZd5coCF-y5gAH1zBYWE_R4Wuk6J-fVGuBFNSjCVfYT_3RMg2tmATtglSaWr9wizpKRQIKCWFvAvcmF1PfeRcvYZJ5UCBvKLSoEvOic1chtMH5tZzZbYp97Ei_pQy7hwtdTdAtjhGfSNXkJmnSXcfRk5eTfnO_APk-399qp0qGWa7olhJOW0Afd1n_fgy8ov360NeY78_0lrqv34a6R8g_QGaaKJul6DiTe2k5FnuKL1gaJ4aFpG26N10QaMCPczk5PrPLB8tejgV4qu4Fzm4Otlgz3uk4Yo5C3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
فهرست اولیه تیم ملی بلژیک برای جام جهانی ٢٠٢۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/Futball180TV/89921" target="_blank">📅 12:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89920">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axZx4c1RNsv98CNeHjbzQgx0pPxzJSWJ7a1grp8eC0LD7Um1Ozp_ZTY_O0VOqJ4zNJEY9QE6qYpTwX5sONeoPF2LvJpQMe5LS3BKCoO_oxqw6ukaJt4itRzdUUbuVJsr9pENBbBkVj1MyyVlTL7BDAnpNDU9ZMI-oR0PzQ6I970ThM6dwN9J3pUbihCSXshH2x5EabfXMntujdRC6HQ859tFskGBdrNfZXrGIZY3OIwM703ev7eieLPz0fJQM3MYZ1oOlgw2HkDKzwmU9tJk7kmjXUd8-fnQyarPxWmB7KfzLKH28_QwwzIFOORsdEHfhTJuxl5-7t5lX-XWKpBEqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پی اس جی مذاکره با اتلتیکو برای جذب آلوارز رو شروع کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/89920" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89919">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89919" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/Futball180TV/89919" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89918">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erMa6UIqQ6_K-AcY7yBvJ3iw3l4_ilUiKMF3mkVuYVuSgloD3rVzPBbPx-aJXkywXeIncYUvP_DBp2J_KPdBOXEtqJ-dBbhOtg_8s4alIZ-8dbw2AR1Z8B8Dyic5F77ZkXBTKwNqrfbKSP2mpFVyXBR31hTsCRa_Z91SbfUCJlXgMGwN8s-cl4qbxvp2demnQVbPuQmJn2BGDEJMHf-LLgAO42_UyfTUp52C2Z-eNQNCN6FuoMD004m43EZ5-2-M5hqT0ZVwCfKnwFFUosdTqrzs4H7fkj4v1_N2LEAKFvYg6dHXivSoZKBb3yDtSRgf7pS0mleH-IEA4gaO_B3DWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/89918" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89917">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇶
آمریکا برای جام جهانی به پنج بازیکن تیم ملی عراق ویزا نداده.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/Futball180TV/89917" target="_blank">📅 11:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89916">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745061c8fb.mp4?token=KlfNkK8-8KEITIs0Vt_EJRXSjexvMRlriRzW-x3Ci2RX6UTAExzmkaStRu_jWUt1Lp8MtKcX5dBIxGCP8tarT66lD9Hdv_E_5o8foJMvs5o_i55Snl9QJIVS-DSOVR9AVB7l0YVynVckfxdaftgW-NFYEeX8vJ8O0OIEPM_bIGh5nI1RcOX2qYL78-bCFfNiFSlbSUxXgW4tde5MWUUqvK6jxtIBtCAKrSicdShb-KPa-1c2SxG4y1_MSlNtRZhQtj77A4d675dQEV6obPThU2ufTzvmZLXJA_0vLvksfzNiBNQO_zML_5uDTe11-PANPAl2Icf8ejIlEUGD3rQ6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745061c8fb.mp4?token=KlfNkK8-8KEITIs0Vt_EJRXSjexvMRlriRzW-x3Ci2RX6UTAExzmkaStRu_jWUt1Lp8MtKcX5dBIxGCP8tarT66lD9Hdv_E_5o8foJMvs5o_i55Snl9QJIVS-DSOVR9AVB7l0YVynVckfxdaftgW-NFYEeX8vJ8O0OIEPM_bIGh5nI1RcOX2qYL78-bCFfNiFSlbSUxXgW4tde5MWUUqvK6jxtIBtCAKrSicdShb-KPa-1c2SxG4y1_MSlNtRZhQtj77A4d675dQEV6obPThU2ufTzvmZLXJA_0vLvksfzNiBNQO_zML_5uDTe11-PANPAl2Icf8ejIlEUGD3rQ6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درگیری هواداران الهلال روی سکوها در دیدار شب گذشته الهلال مقابل النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/Futball180TV/89916" target="_blank">📅 11:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89915">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJzwCFTdhiZNg8BQv2STimQ2jrWVefQbUDTY3cphLnngDbtqwhN7Pezd59AzL1Si3aYlYkeZddcBUGzN5ACOzfwwJ2xwbcmx5INv-kWv8Zuimy8gP2mAzhfDUKd3fbBMuQv3scUKdd794T4pvpeZzKdO-u8PhyXaVHpdOELllbElm4MIIU7J1g61qGEH8UQNagMyOuLrLswZ3htUc1k5H7kpC5jS5hZVxV2dpXxcyzbyzIlZ6ht6BDchdYVRqrfTRNIbmwzH_snKKS_DH3zOjrPA_Sew704OBsQGR_yR7tISrOlTVC9EFg0FHQf2_pMd38zE1AnDBBA7LaVTLw3elw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با برد ۲-۱ مقابل الچه، رئال بتیس موفق شد بعد از حدود ۲۰ سال غیبت، جواز حضور در لیگ قهرمانان اروپا فصل بعد را بگیرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/Futball180TV/89915" target="_blank">📅 09:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89912">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حمله پرز به بارسا:
پرونده نیگررا بدترین رسوایی در تاریخ فوتبال است. باورم نمی‌شود که هنوز حل نشده است. داوران همان دوره نیگررا هنوز قضاوت می‌کنند. آنها هنوز بازی‌ها را مدیریت می‌کنند. این غیرقابل باور است. بارسلونا برای خدمات نیگررا به مدت دو دهه پول پرداخت کرده است و این داوران هنوز در دهه سوم قضاوت می‌کنند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/Futball180TV/89912" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89911">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
پرز: رئال‌مادرید مشهورترین باشگاه دنیا است و سایر مسائل خنده داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/89911" target="_blank">📅 19:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89910">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
پرز: با هیئت‌مدیره فعلی در انتخابات شرکت میکنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/89910" target="_blank">📅 19:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89909">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
پرز: دوران ریاست من بجز امسال با کسب ۷۶ جام همراه بوده. هرگز فراموش نکنید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/89909" target="_blank">📅 19:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89908">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
پرز: مثل سگ صبح تا شب کار میکنم(جدی)
😂
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/Futball180TV/89908" target="_blank">📅 19:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89907">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
پرز درخواست برگزاری انتخابات رئال مادريد رو سه سال زودتر اعلام کرد
دوره فعلی حضور پرز تا ۲۰۲۹ هست ولی او برای نشون دادن اقتدار خودش امسال انتخابات برگزار میکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/Futball180TV/89907" target="_blank">📅 19:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89906">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
پرز: متاسفانه استعفا نخواهم داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/Futball180TV/89906" target="_blank">📅 19:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89905">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
نشست‌خبری مهم پرز رئیس رئال‌مادرید تا دقایقی دیگه برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/Futball180TV/89905" target="_blank">📅 19:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89904">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNKRX6gG8l_tQjDqT753yXYve1yW4O-s6vHRzxCiX1qhREh2cKv9T_HN-d5TaTOZsW_g2GLuhfaX5D6Uur3GkXo67aY4VgPmJfteT-_F7OPnfz8A5QjxwfJ4aPeAiMRwmg7X-1CXpF1Hy8HG0dgn_rUhgT71u24IN3qdQiRhPyOq7USj0VDGA9lmJaLt0o8hDd88FlANmKxAzYdXR3PxSZtAtHodh7BibAODjalrYelDud91R74ze7MhHZPxjQi-I5O83cMNlTMEtBg4-L_SXvde3EWjSZt_3FzKCBPG1w24NrcJLST3ile_rxm-mViBxB26_u7q0rv9bVq1uX52CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نشست‌خبری مهم پرز رئیس رئال‌مادرید تا دقایقی دیگه برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/Futball180TV/89904" target="_blank">📅 19:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89903">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPwrBV_bP_JHfxASCtqFLlfXJZOm5R7HQ6Axw4Rhrxt4iyXdxBXxElXoHFKpi5hvontbo_qBkFrUo4C4cPTmV93_X73mbh_aINr6euX8O1wjO34VdfErSPHgwjJkfPwGu9rlr1o4UNrBjlNWOPh8IfUQ_ufC_zoVydQuZcdqLcDsqo2ZKJcomF6RkJlbTS1v9Bx_n5CtVRR4qLz5eDzFsxnxZ1pwKZHavk_R_eJzomce31UOwQeTkXzsgJ5lZtTLPK8e_2SLtFOcHKV_Y1ZnJAB_1B1UMFSpU72obeVjhu60YKJZHHn3sPVOzKsz7cl4lvkJFCbSiQgl-LN8ryklMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو راموس باشگاه سویا را خرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/Futball180TV/89903" target="_blank">📅 14:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89902">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmcSXIGNXJLN09KMhOs4yoBvn6Ws9AHitJVM9wAn3pPWenie2epvlgBeDo2mwKUAsdcDn6Y6_nzlHlNQ_VM3fLiB_eHAhhOJp5p5OnJL2tFiC2imfqY43ZOzDpo4ih83HSF5GPBWmGwjIx8eFFkyv6VnGJb4Dso0AgG-vs6rL_CMeNlb1hPTZ4Zil-W91T-PWXDI0DQJbXH4FAuKY83wwk85CXHdJ-6adxE2otDtG8Ai-B9n7xIPOCvqfM1C47SxcztaHPj8BHsxU2LcO7G-Pit_7Nca2PVAnh7GGwUNb2txjN70htC4Dcwcf7nqzdO-Bdn1zsPc92TMQ3SlHfjuGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
لیست اولیه قطر برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/Futball180TV/89902" target="_blank">📅 13:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89901">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqTiebO8rYdwq34IWGVjFZJo7RQbzL9BbmcOZT725mj2d9x0zKlAvjjV3f0NWe87wzdDRAqhGXzhsnMVjeL2txuQdR7iwKcHgKwsSY82fYZGXTCgXtH_sZ7fMIJpvWIVkuHt_RUuGDIRj9qyYD7eEcJSPTcwKiPcV55qyqdp37bj79BVMfNhggODuISgqU_q--2QafID3DY4vyZJFAYlL_o_TEvagPDWC2nVTH5lztVxxOSopJrF9Mivnasj-35KtdxNK77o6xsYeB7IF-HjnV5510S9rFVI1IqB0BMP8Mc2oPOgtW8vqxoSfQEVd2RlF_PVzFdhSzZma7BVdbb9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
پیراهن اول یوونتوس در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/Futball180TV/89901" target="_blank">📅 12:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89900">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf4tzJXbHemhF05ygAYF6_eOBmnTbUCwh2NFwcB01yuQKyt9q3KVfolIPQBN1P8F8JnT1RR6MygWmXM4AcOzDBrn_4QSm8CBVYZvj4n8cQkBKKPihYTLfkfTH7HOXPVQWd-srjBeSXRI80HItUvBHBJQ-1pKRUsZWt-mRvGdj6-tahSKVP7zKCWlisy3Gyx5kgBGDQjxSYXN4Ezwgx0so-7W9K6TCkGydjguZ6gHW8KDKpEokhtbryI-UYqA_Ur_UkX8yZKhHoorWxZf6TOUaUDRJXJHNfMz7brfCy60scXNiqL48EMfBL9tvAM3-0MafkS8-mIAgQae_54_MDF4Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی‌خواستار هایجک ژابی‌آلونسو برای هدایت تیمش از لیورپول شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/Futball180TV/89900" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89897">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pd2Gy3MzBt-63ZTODY1qdr5VDW0fSsOxJvqhF-8Q4nVcmZ4CIllmzhnpavbcyFoi_9YS3c9TnmURbc1XVA-ZBTXMacdOXrK3Emk0uVIzzp3aslWT2t0RbBUOwFBVHRsu2o2yU7Y8Orx6NWtXScnSXzz9hRUVn2KfOV_4lQHkO4akQLALdM2qtztR7nKegwB3R7L_wS66G1T8S_yQVKR-u_FcCAiyFOSDZO-jx349sUDxXNcnjfPCTg382llc6dV1wsDOzWIBBsltWZ-GGv4wn6I8j_ErIDSz80TY9xpLrrbb5kyCS1ywhApDq952wTASNJxA1me1pMke1PCL5ipnTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی‌خواستار هایجک ژابی‌آلونسو برای هدایت تیمش از لیورپول شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/Futball180TV/89897" target="_blank">📅 11:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89896">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqeqa5GqiMdRzKu3BlXlOOc5yBDmBB0hhMVzxUJMIWG23WSMvJSDrLZrwhaY73oe_JmM9mG9zU8Zg19ZKC9aPWCYBKaJPcuIY2QvKSjudLn-oyPFxeP8j4LTrpsk_14VpxxXNLlaOGj5vzzWoiM48GWUJlYm2iwhtk7m9REZvex7V67rpyMbVkS_EiO0zN-wcp2XXwrlyUJuijzrtp8KmiNMT_lj-uIk1_cwcqrqIwuPqrl0DueCa8g71wQUZskN6Awfh10cHehpMrMJRdyunu_fNXOrSdyaiTLcXe705omKRNN-MibbESaQ4tNjgLzUCQhnzQ0fNjSOkG_SgU60yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رسانه‌های اسپانیا: امباپه خواستار فروش والورده توسط رئال‌مادرید شده است هرچند وینیسیوس و بلینگهام شدیدا مخالفت کرده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/Futball180TV/89896" target="_blank">📅 11:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89895">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0SgB1N-S4Eqg8OOcrV_GftGvQZQz5Dth8CIEwo8Y14Aq1PmpfpYTUTXf-qeo0WgbZUd0XqPsg36_yzMlczDY8OY0WB4u98Lzp9BM4O7QknuGQtIzs8zXeIEK82sj3vKop60QBf0HJs-9CJoKZ_To95IBElrABqIFC3UrTqT2ceemh9rkaWaHKjbQwmzxzii0dD4vbeYqKXeSPpqpxmOOk5XhwXDUSQJG9KQukNL_mZL-uWkLclr5TpzNr0HVdcrcn0eF9NA9rR6mFzYHGkMiG5JwF71VHhuCH-FDnFOZe3I1q1ab8vYuM7Q3v6BE9IeIQqyakGH7A4FuX0xmV5oug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نبرد حساس قهرمانی لیگ‌عربستان
🔵
الهلال - النصر
🟡
🔥
امشب ساعت ۲۱:۳۰
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/Futball180TV/89895" target="_blank">📅 09:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89894">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d894a4bd.mp4?token=JfNoERHE7edBQ-W1RuGERMhPZbKOSmJaI2MI50mL9xPH3SpMd4vOsepPCJJmG_EGCxDTk2HVNpiwYu0-_hLJdqgxeYTZBJs6dHO8xTAVkCucsfy5f3rtYD2rQgg1W80TazDDSc7_VZDvrfn8C_vJGtlpd92seOfsRt4MT2V7RHoPNMQ5e6gujJDCrJUPCpXJee-RSpdbBWu3PFLb05t-6IoIEe9VXKW-GoOi_FQdAks93JBIgIeOE-KgfAcsencF6TpVMGDzGYDIjMeIZXUDqpOL6zy8tE-2EBTp4qgDpYzGKegsjAk34zYkUZhOMFGEv0DRYA1YeO_DsFkW3ZDipA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d894a4bd.mp4?token=JfNoERHE7edBQ-W1RuGERMhPZbKOSmJaI2MI50mL9xPH3SpMd4vOsepPCJJmG_EGCxDTk2HVNpiwYu0-_hLJdqgxeYTZBJs6dHO8xTAVkCucsfy5f3rtYD2rQgg1W80TazDDSc7_VZDvrfn8C_vJGtlpd92seOfsRt4MT2V7RHoPNMQ5e6gujJDCrJUPCpXJee-RSpdbBWu3PFLb05t-6IoIEe9VXKW-GoOi_FQdAks93JBIgIeOE-KgfAcsencF6TpVMGDzGYDIjMeIZXUDqpOL6zy8tE-2EBTp4qgDpYzGKegsjAk34zYkUZhOMFGEv0DRYA1YeO_DsFkW3ZDipA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی محمد قربانی برای الوحده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/89894" target="_blank">📅 09:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89890">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=ScEGb_vRd89KS0mkuh6yuyiJNAN6zSIkLARwBGk2koExmUiM8DpXwS-WlIrhwD0iKAT33SMwbvArCegHNev71Xv89MjvoMRzjN6pm-Q8txSBFS3H9UuH-t6eCg65babSRyLka-HWgVM7CJr7aUfxehLqrCfiI1c63RHjNqJrrl6vnFv2piw6Xs6iZG6gGVKxjZsSBVQ3QMMCTgjYnTvXL1I2jVOOHAhA3E8SpBRiB6SG4q_DNIHDpi0YYWuGQEM79-6sneHCyUPOnwMQMbx0JhjJOm1kcQZ7zN8_dO0SaiL_ksOTQITWypwMcwJJq3euwxg0_vQI7tPhYQ8E17pN2kAVrGJVzNeTW91Ni8nOx6JtdQx_FGhx7CEC3OlhY9I59u3ZtU2H4WHoFPM-v9RI3vbmBOZhgQk6WbX1rEFc80QujcFEY4yj2XYv-0FK1QTX7mi2Qc1IegZEiI_L-YhUIAzGs-hRRA4TZ8tniQQ2witVESXG4bAuJaYh_IK6vVicgWuNsRoCu-hKfg_59mTzKOXxp8OAjSmEeLwcL35deyqU_ZTXct8P7-DR5VGTReWfi4oNAGch8dM-bLF5od3KZ3jAHpfzmezrxnX69vpK5uZK9ZDfKC3k8-Ler7ItrrgsAh24T2_nWh5iaUhoVSwWTEFmQ3AnVWJE8aBIfHR0hMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=ScEGb_vRd89KS0mkuh6yuyiJNAN6zSIkLARwBGk2koExmUiM8DpXwS-WlIrhwD0iKAT33SMwbvArCegHNev71Xv89MjvoMRzjN6pm-Q8txSBFS3H9UuH-t6eCg65babSRyLka-HWgVM7CJr7aUfxehLqrCfiI1c63RHjNqJrrl6vnFv2piw6Xs6iZG6gGVKxjZsSBVQ3QMMCTgjYnTvXL1I2jVOOHAhA3E8SpBRiB6SG4q_DNIHDpi0YYWuGQEM79-6sneHCyUPOnwMQMbx0JhjJOm1kcQZ7zN8_dO0SaiL_ksOTQITWypwMcwJJq3euwxg0_vQI7tPhYQ8E17pN2kAVrGJVzNeTW91Ni8nOx6JtdQx_FGhx7CEC3OlhY9I59u3ZtU2H4WHoFPM-v9RI3vbmBOZhgQk6WbX1rEFc80QujcFEY4yj2XYv-0FK1QTX7mi2Qc1IegZEiI_L-YhUIAzGs-hRRA4TZ8tniQQ2witVESXG4bAuJaYh_IK6vVicgWuNsRoCu-hKfg_59mTzKOXxp8OAjSmEeLwcL35deyqU_ZTXct8P7-DR5VGTReWfi4oNAGch8dM-bLF5od3KZ3jAHpfzmezrxnX69vpK5uZK9ZDfKC3k8-Ler7ItrrgsAh24T2_nWh5iaUhoVSwWTEFmQ3AnVWJE8aBIfHR0hMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درخواست صالح حردانی از مسئولان برای معافیت خدمت سربازی ملی پوشان فوتبال ایران
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/Futball180TV/89890" target="_blank">📅 00:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89889">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3c6bcff1.mp4?token=cl4vhukuwWGFxTV1EHS2O_h7Wr_7myJES9Ml9-zoxMDlK3HxxfbrVeR7SA3pt9ezxWQ_ncdB2990GvDhv49YphfnpNr5IZCY9nJe0a2YZUdLDSsd6o5iTQ8F2hEAsHbcs4IWM-Uf9fucAHEsdfeO3BHcCvEYKIYW1hcFK5dSxXcYZkUCthhgWNcVD_bzJ36stXiRrxbKEh9NFnLkF-aXvNmPssjXyRImv3VaEMA6TvKug1F1rMbof7mqhrTqVJDUsJKpNM3nflpSmPNSa21iLFZnddG59lhjYZXRH3Aohf7o3pY15rFCkfeHEgq4PEL-nElOcXy4wlbNnbqeQi46sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3c6bcff1.mp4?token=cl4vhukuwWGFxTV1EHS2O_h7Wr_7myJES9Ml9-zoxMDlK3HxxfbrVeR7SA3pt9ezxWQ_ncdB2990GvDhv49YphfnpNr5IZCY9nJe0a2YZUdLDSsd6o5iTQ8F2hEAsHbcs4IWM-Uf9fucAHEsdfeO3BHcCvEYKIYW1hcFK5dSxXcYZkUCthhgWNcVD_bzJ36stXiRrxbKEh9NFnLkF-aXvNmPssjXyRImv3VaEMA6TvKug1F1rMbof7mqhrTqVJDUsJKpNM3nflpSmPNSa21iLFZnddG59lhjYZXRH3Aohf7o3pY15rFCkfeHEgq4PEL-nElOcXy4wlbNnbqeQi46sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لامین یامال در جریان جشن قهرمانی بارسا در لالیگای اسپانیا، با در دست داشتن پرچم فلسطین حضور یافت.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/Futball180TV/89889" target="_blank">📅 22:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89887">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381c992189.mp4?token=voQH13wdZEb_DnXrSvLvheO8wcTgHTq2k0xmM_NeAMiPfNvDYmJ2W23bYRQphlWbQ3eaYzELbBd1FCqus7qlcLsQyOYPBszgEO956LQIaqiTDv6_dT9s93OBF-vwgFSwiCC_y69x0PP4oYoOU_8e3ZpfcnbaT6X42Fglnfbl5u5fdrCKM6xvhArCLeBLd2_Yy20F67WGvQwvElonOcB8ENFo5b4FJ1ZNqZk2zwLn_Zmd6s5SVd19NuOZVERe929T15dEPQ2Qdibo3A-0F7DXW7CcZ6ONn5BmCUBzrzs3OjbjH9ni1EwzqltDuSte1H4XBZZhMgj2gzigmwC7aU_ksL68BMTcRTN78MAeoWY7Tah1razQ3dxz5poq-Od4041c2EpPU-voE3-cWSOHZr9ijtlqYO8_XOuWQ_Xyqqouf92tYiu95i-JULDtTR_P7Dgb31CQkitgdoUwKcql3WiyFz0Ad0iwYK0Rpw3qJgtktNCv6oRpmBssCn0ep6GypHVTtLwPN3bV8BIyRSTOGpJ0-8odnEJ4zjO5jg4IRoI3F_GZrOZsHh6F3Ii_cfyVb3A_5EfnDVN6QjvIdgd4k2ficbQRxBukfwg3d55jTDbQFf4uu5QbA8XfoEan5zUKMK81RwQEY0uq9jB19q0jdtt_ceDJSyn4Uugrw2-hIqDMRmc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381c992189.mp4?token=voQH13wdZEb_DnXrSvLvheO8wcTgHTq2k0xmM_NeAMiPfNvDYmJ2W23bYRQphlWbQ3eaYzELbBd1FCqus7qlcLsQyOYPBszgEO956LQIaqiTDv6_dT9s93OBF-vwgFSwiCC_y69x0PP4oYoOU_8e3ZpfcnbaT6X42Fglnfbl5u5fdrCKM6xvhArCLeBLd2_Yy20F67WGvQwvElonOcB8ENFo5b4FJ1ZNqZk2zwLn_Zmd6s5SVd19NuOZVERe929T15dEPQ2Qdibo3A-0F7DXW7CcZ6ONn5BmCUBzrzs3OjbjH9ni1EwzqltDuSte1H4XBZZhMgj2gzigmwC7aU_ksL68BMTcRTN78MAeoWY7Tah1razQ3dxz5poq-Od4041c2EpPU-voE3-cWSOHZr9ijtlqYO8_XOuWQ_Xyqqouf92tYiu95i-JULDtTR_P7Dgb31CQkitgdoUwKcql3WiyFz0Ad0iwYK0Rpw3qJgtktNCv6oRpmBssCn0ep6GypHVTtLwPN3bV8BIyRSTOGpJ0-8odnEJ4zjO5jg4IRoI3F_GZrOZsHh6F3Ii_cfyVb3A_5EfnDVN6QjvIdgd4k2ficbQRxBukfwg3d55jTDbQFf4uu5QbA8XfoEan5zUKMK81RwQEY0uq9jB19q0jdtt_ceDJSyn4Uugrw2-hIqDMRmc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ: من از کردهایی که به آنها سلاح دادیم تا آن را در داخل ایران تحویل دهند اما آن را نگه داشتند، بسیار ناامید شده‌ام.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/Futball180TV/89887" target="_blank">📅 19:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89886">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754e02ec47.mp4?token=izATqa9uyEaDu48wNIWvtZsjHIqFpLou_TQRgp4B93Ac4q5RRBMRXjqxlgYWe98aSJJsQCWpJTa3DpWHDWCsNa6lITTqGSaU3bLoIIvMvWHk4o5oedsVX2sGl1_zJby6biqfT7L40IjMusQoSEcL7ZIbOB8WzvzD3W2zB7Oz-_Q2eQt9Koel08PuwYjSpYnW-KGhqvy1eVFtImY_fRXfj89ukN97rLn3zBbO-ESSd_YkBwvBezOh3B1Z0X_5HJEztYBlsfvXqSPxMB8B5Gwhj0doxqiQKW_tdqZS2_HP_2QoKlO0vTTpZV0ysGGQeSD-T5jFjQ_9LdyooqoCFjSnMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754e02ec47.mp4?token=izATqa9uyEaDu48wNIWvtZsjHIqFpLou_TQRgp4B93Ac4q5RRBMRXjqxlgYWe98aSJJsQCWpJTa3DpWHDWCsNa6lITTqGSaU3bLoIIvMvWHk4o5oedsVX2sGl1_zJby6biqfT7L40IjMusQoSEcL7ZIbOB8WzvzD3W2zB7Oz-_Q2eQt9Koel08PuwYjSpYnW-KGhqvy1eVFtImY_fRXfj89ukN97rLn3zBbO-ESSd_YkBwvBezOh3B1Z0X_5HJEztYBlsfvXqSPxMB8B5Gwhj0doxqiQKW_tdqZS2_HP_2QoKlO0vTTpZV0ysGGQeSD-T5jFjQ_9LdyooqoCFjSnMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😄
🚬
شزنی‌همین الان وسط جشن قهرمانی بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/Futball180TV/89886" target="_blank">📅 19:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89885">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYOadZ9qVOGMTjIHW0BxV7D3HtGd9-VzuhBy1YmFbCPlXFawQhrEOWr6de2kw0QGntJ74Z3U48IQ6lGTODS-baLznEsa35xywDup80UurT8cFNQCR3sgPGHtaGEvmWALz2TB71k-SCqUIFxy2N1kUVh_Q9qsIqQdbo48xgRS3yqLnLjzhbTauudY_jCFgUewwiRbmjgOmdQfiL0ZH0TuAFLNpo753XHTARtlCdg26qkkpYkcpO3VhHzjYKN5MqsS0CzfPICjtMiijEVeeM3Z9qu8jXvvJIOMpF8qQH_tXrTE4Sl62s2eVsnhVd5KzBUvDhL9n7deCRmIsFgb4pQrOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ایدول‌خبرنگار مطرح آرژانتینی: لوئیز انریکه سرمربی پاری‌سن‌ژرمن خواستار جذب آلوارز ستاره اتلتیکومادرید شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/89885" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89884">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeTfZvLoQaKKiZB4Y2gcT0ALS9Qc-z3g7Rj74Lw2uX7jw0E7UZxRrR82iSmap9Zbip3wnKY_dVLIPBsRbiQQfXKfos2ozPi04XrOEOKJYSo-1WGniYEYoM3tlfLN2odtbMfj02Wq6uwcKinfGSUJLKXMwG5W4Y9FINLVuJwRQwb4Nwbcb_nE5p7f3WeRNDd_FNS-nO6Fddrg0jSinti36JZ_WvpTYbnrzq8CQEtzFXCFcStOtBga2izECKoNgUanseHaYHaifiWXlhqJAbN7iudF2VWLn379dodhv9ewBjxuIdE70EmEurDPUmwQKLKHvQ9wnkyKNFjNwYG0BSrA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇧🇷
لیست‌ابتدایی تیم‌ملی برزیل برای جام‌جهانی با حضور نیمار ستاره این‌کشور
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/Futball180TV/89884" target="_blank">📅 17:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89883">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AS7sLKjz9hS0sRifo5y5_R_q35iNRsLO_XwVoVlNxwSHsKKNjYH-WZWBT4G3GYlBCCri4U9G09fHOhc2Io_d78uaxih6WU2WoXMWr77rq9Gh87Q8JXze5gjc61xLAA3oy0YgMCV3SOAMv9TmG89CI_uLHeNWHwJTRDG3-KXFHHBSiaZAM97i1ltRx5YaDDJRapcPsotJYngbXsvOy3RFr8Tm25wrH17TM6dGQo6fdKlxyWzcoXg-RnwgXMMbtBU83EqdniSGZip1KQiXj6i5HVUMJcoR3TUYy4vsIq6o1Mz0w8D7T-9bZWWXId4vGqBj61sgolrbuK2M1xVRyVmwPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
👀
انریکه سرمربی پاریس: باید بگویم که به احتمال 99,99%  قهرمان اروپا خواهیم شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/89883" target="_blank">📅 17:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89882">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAVdK4lrCdkSVdV9tTS28pMUnEKjIlLd81phpQHjA74Hn5pMqh2Z2hasV6f0pshhDJV53HvI59KW6U76ztWv1DFHuqSfrJxfDuFzP3L_cO3EvfYnsThmmari5BRCQSHay-cHz3b1NrxOZ4QjGp3hiMC4tFrMe4c5hGHgfXaB7vFvPGli-bwfONRfHQeDNlzZw5wJGDd_h3utDeTVry4SlC9JfNQiaxJtUCu5VhceZbmHmR6nrhWtZ8HEe2X42Rc_dFLp5GpOXPgvWNFqESrMkhNcHIMaic83xl2YNKjnHJfsNZVlWo8EEvWgOdQRqInSE9i7q1qLqHcXDj1FoqJVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👋🏻
خامس‌رودریگز اعلام کرد که پس از جام‌جهانی از میادین فوتبال خداحافظی خواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/89882" target="_blank">📅 16:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89881">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaN0BgCZK6PmvGmSSzODp6LbKeVB_0xSFxfnRJTPd2DynW--h5PP1sNqqtDFobSN9wyRE18QOkJok3MkcsIM2qtVoo_GsmOsv_foSUtFajoNlRRM9F0zYpVXSJQkwTrevMs7uf730FzHc5TmZAxNiKRvZ8LOMEs--2vK6NU-TD_ctT5sEbF1HJI3a0hloeyQM_xNfAh2sNa5jE8gpvskyFoe1KlyVZeDYdLesizo5KZNzpSWvT6gJ7F-514JkfNK2rezBF1qM90tmd2rImAe3-8-vco-vbZ-RNFBoB-VaQ0y7xe7Ytw78ZC0GDB1tcXMBhQHP18-XCmqT0D-Q36bQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
دنیل‌زیبرت آلمانی داور فینال UCL شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/Futball180TV/89881" target="_blank">📅 16:41 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89880">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAb8nze9SHV3UJn4S7oFKU7_vHIxDpvgnGjaQlxyNl7t1_h7h9bZUmozTrSpsj3Ej6_pgB0hR9I9eGR-H4IhJf47jLhwKMCmsj5hp0I0BAK397f190mPlndTgPGcy2w1pVmohFTbKBZuO_V7KNVk-9lepoIhD3bhzpjcM6T6ZTrY0bQ65razFcevgkDVZBagaVpzZJKCFSvAMOQLfrq30c9T_jTalKlNFiG_QPvUDOEKunJ0Kw5Bmh-GU_otBwgAT0EOJVpv2gV3d4fblb7cIdvAZ8KC7fpwn4XK6GHzVWokF_ZYITQ_zTOkqqixahgc4VGGUBYkeVfOT81ZRqMEyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
فهرست ابتدایی آرژانتین برای جام‌جهانی، دیبالا رسما از لیست خط خورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/Futball180TV/89880" target="_blank">📅 16:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89879">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6bFw9iW_GlZj7YWYBrLkyrRRrM0UE6XxQtWgVR4o5AuRZtlCHXKkIV6duiXtZ0BvrADvnh9jnkjIAqE62nqAP8j6QsY7vpSXXmUaXFXosAKX6O0rU4xzQ5Y-oWiVhCVu1NV9KM0ICw76T8mHz8O6RijnXYKAX0SsmsaaGrgiUkfkifyzzgVfrb-IZj25fOs82sv4etYSPTV_ojG2zAyYoITorfmgZeOxybTtojWH7Mm8elizuApzx9HM5zbQfeAz5VBgw9d2kfXstqeeA3BRUxaBOARMnvV5Y0YZ4XftwCNJCOIP82LVWF189hMxv26yzEPWQG4oeUJO-JKJ58XtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💼
یک ماه تا شروع جام جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/Futball180TV/89879" target="_blank">📅 13:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89878">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
⚽️
در آستانه جام‌جهانی، یک شهروند آمریکایی به ویروس هانتا مبتلا شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/Futball180TV/89878" target="_blank">📅 13:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89877">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
کنفدراسیون فوتبال آسیا درخواست ایران برای تعویق در اعلام نمایندگان آسیایی را رد کرد و بدین‌ترتیب احتمال بسیار زیاد سه تیم استقلال، تراکتور و سپاهان نمایندگان ایران در فصل بعدی رقابت‌های آسیایی خواهند بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/Futball180TV/89877" target="_blank">📅 13:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89876">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jyq39f8nfzP7eMuw9_UOUVXnkaXkNb4iSEHY1A4jmCKTY0M8regtvfT_FBisI6uyK6JhMTc2HsVFY-DzgNaCfmYLen_wqjjwxCVXJW1ZDvfxnsjoRXLLOyQYx2AIKVTbuPo3Ik76NSC2U15ceN_6r0TIxkce5Une0uRxeCILN_L5eOiRo1IHgmz_gLnMY9zYosiSvQ7kdM2320pFrITI_Edv-f7THOX7rsj5B9GzVOlSgUBgP8VuJsR67Lll3kn8EiCQoG6KGRzCNDkdo9G7IEjtGFsuVJsk35VTR-xxciDeKSkq-VI6QxnlDBHZqH2DPHbLymq-PZKlwG_198I0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ رسانه‌کوپه‌نزدیک به پرز: ژوزه مورینیو با قراردادی سه‌ساله سرمربی رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/89876" target="_blank">📅 12:07 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89875">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7fq0TzG3aKgmLnhsaerlpiQB66KdPN8pTsh6Aqd8IZdOT-VmEykKhE2pYUEqGE147Dc8tBD2eA3NSbaazBaTpjnhZcmXkO5A9SIKSW9I-x7hLNV6q4RecHE3QbOQZrj4RGVD1oMcWr0scy1N8yBW-ml3F0Xr4kS4Eym03km1VtWvPHI_caaP7ZeuVb13ufENmrQUzmVWjLj9pQKfQi0xfxN54N5zjWtCgJKduRjZcAIwc6UsFNLAAqzU7dr2mIXbB8ZdH3_gsSB2_nrw-ORC4djVG_Ze7rlIxAlfiW1qZNRmvSRglg_zJscravraD_C4rxrJeTC9o5x7k862gkerg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
نیمه‌نهایی سوپرکاپ اسپانیا ۲۰۲۶/۲۷
🇪🇸
بارسلونا X اتلتیکومادرید
🇪🇸
🇪🇸
رئال‌مادرید X رئال‌ سوسیه‌داد
🇪🇸
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/Futball180TV/89875" target="_blank">📅 09:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89874">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSwBFs80DOqDdBK4763mAakayPqH941EzD_9AKt_H7UBJgCM5Ouknn8kuqvTwIbgOxvnVbPRXdKbsEV519I4FtnT-B53TNaiheP0hF_CEhNB20gSk_s_ceqXO7FLNujup2TuSzu_cX3FhAA67JF9-ddTGS9_w2Cawm2N0kXqKOiLpSXbuW4jZw8zthdZ7oem3rfs4Q2bNqgLlFWT6EPnQb3fbfSd44w1a_8EqBtuAThHYq96DsO9MUn9N1FVC47j1CZ7-geN9GcyX7_WsgYgVs8jcn10zZqZW5W-qCDAt2Z-KidALVYpOqpLTQb_msbnbqlAZu5p06WSx7KG_BVnug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمار در ۱۷ بازی اخیر سانتوس: ۱۱ گل و ۴ پاس‌گل‌
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/Futball180TV/89874" target="_blank">📅 09:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89872">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a87231df3.mp4?token=LTbMD3UFr7FKkTTqPKG8q9B-H-MiwwDttpeqH1wdZk7glONzkZTTHAgIM2gC-lgh31mAK9Xw8GEKDc-jAo6TTbLNZv2v_kleMYkvuMrrg2VJug5eGBkyVMs_9x9_4rl8fE3TFJpYHlS8bTt2mP77ayyb0_AoeSFZ-8yBOEysxVUBB012NHAln2YySIZmb8R6huKnvcN5L5zp5J4jssOpK517sEfVZsX8wrN_obyrItFXMDMWdePbsXxXGspIB_-e6VnVzXnWVI8O_T80eJD1qA8XmWzKJcnKbKPDsq_FoiYqf-JOu2G7Cw5CvCKjRWhYacrOASdk3n3EN-GQLquYqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a87231df3.mp4?token=LTbMD3UFr7FKkTTqPKG8q9B-H-MiwwDttpeqH1wdZk7glONzkZTTHAgIM2gC-lgh31mAK9Xw8GEKDc-jAo6TTbLNZv2v_kleMYkvuMrrg2VJug5eGBkyVMs_9x9_4rl8fE3TFJpYHlS8bTt2mP77ayyb0_AoeSFZ-8yBOEysxVUBB012NHAln2YySIZmb8R6huKnvcN5L5zp5J4jssOpK517sEfVZsX8wrN_obyrItFXMDMWdePbsXxXGspIB_-e6VnVzXnWVI8O_T80eJD1qA8XmWzKJcnKbKPDsq_FoiYqf-JOu2G7Cw5CvCKjRWhYacrOASdk3n3EN-GQLquYqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
جام‌قهرمانی لالیگا رسما و شرعا تقدیم بارسا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/Futball180TV/89872" target="_blank">📅 00:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89871">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CN5YlpXjVHc7hL3pU97TG4JwV6e7lPJEf71htFZMPVsfxgSlHiTHoCB9hlWHzRxj6Q7D11tKZNyny7qEltXX9rTIZ9MJPaiX1-mtJYcLPajNErU3L-MMNWnuAeNeG_603FNfGY9LA5Kp4Au1ArEQmN-w_rfu0RXmOyQxmiQUC8Xyo48RGfjs0XlWOZ3AWO95LcmUbQ8HCcmLq6t-xle6VcT4ZJjZwYW4vfBkNFG2pYdTqehjk7O3_Q6UL4I6SzwP41ad9dEDEWDJh6WKVVwiT7_yyqaY8fjhkx0KZ8rS83Z9-72uCZmuaVtlVfQFqakLPl75-S7ntWUhuIQA305fKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
لواندوفسکی برای سیزدهمین بار قهرمان لیگ داخلی از میان پنج‌لیگ معتبر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/Futball180TV/89871" target="_blank">📅 00:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89870">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZG8Z4gQybXhW0Id7utW6hyEBsx75q8RodrZPoRuGYNONiyGqTcaCWDzTvC8zzpl5pLs2GeapXjnrFbIkff1ummiiVYYg3ZQun0GPV_ZVXDJhGpQO4Wpv9Xbr_hZ2YJi5-CkBFW03k_p6zRb0bgnEX2oVLcNl_XEJchiCwLnD_MAOycwuqIhsATzl_HFAF0rFUhI8hmaDBjy97nFX3_4J7Nj_CNJDzagu4y-WQgD2PXxHELJ9Ur_lnIXBt6GnbUJrASilCTwcmCBrcjgKVfOsVYodqYdA0fpVcy-ubggwQFSYR1HxYC7U50__HCvzH8NpweU78bCNPguFuZmNQcuMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرافتخارترین باشگاه‌های اسپانیا در عناوین داخلی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/Futball180TV/89870" target="_blank">📅 00:42 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89869">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEvbFoingc2-lvz7MuuDe-ONUldtvxt4-bBnQVJotxGEDXpMm_KYW-6DDLZ2INcznqGBUfjh8-xkAVSevD0z3hYH867vdM727Ihnn_YLUJf8H-852SKxjeenWnEzC39ePSI8a2oOz7WJ5L8n3OJVVJ8mpsKgpr244JsKIyld2XsDaf01fSZ5IX6pIBqF_hOr2ub5vo96_EYWC14lDzQ7FO2tYXXc8pGbWXfYl5yQt5m-LoW9XL8Ot8yQaWa3HsyDvot68-Id1eBFztjX0G6wgttCTmK-wMi_ozM2mEouNQpK3DnRSeJim4P46tjMZeV5-DoP0S_BYIxXmuEBSb31Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️‍🩹
استوری لیونل‌مسی و تبریک‌قهرمانی بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/Futball180TV/89869" target="_blank">📅 00:40 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89868">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
😂
آربلوا: پنالتی واضح ما گرفته نشددد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/Futball180TV/89868" target="_blank">📅 00:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89867">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPka5yHX12NYGu0SFgzglK7_4hCGtsmSUA3rxUSnIOcj5Qq0kj3vputSc2r2iC-GkMa5P1-RNaVmtcvFQ6a_yoJBo-cHDnKwVMtTXh_h6f1MoN_6pCsR23ynOYb33XYavwTmB0yg0OPYLePnnPU6AN7SpL2x99YLNPQ7tgG8jIwOjYIzuI9_uMKhfVJ5qWLOtbfVgHo_wB4uhUScYprSU118bPDFaa1XM7RWIvPDg9JnYwVrUwTRD_MUHD84H8eae1GiK_9H5wN5lo3EBAZlNVMCeCe2ixPkBqs4vCB8Ys19VfPnssOpHoXHbDhU14ES3A2CatvGktUjr_w0jOumbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
باشگاه بارسلونا با قهرمانی امشب، به رکورد ۹۹ قهرمانی در تاریخ خود رسید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/Futball180TV/89867" target="_blank">📅 00:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89866">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8_qwkbBGXCGysVSgd9Soxl3oc_4GecNwB8CrWS2u1HmN7TXUPc6q5fLnsnE3CTOA9PAHM1JBcahlRhxt4jAB_18XcDiinMvnrKIKIBgShxZFCBmvcBhrAN90T0e-hTJtxzp_3YYLiP4jSO7MyloXU1SnCjJgh-8pKs9UG7gtySWnFt1FM7k1IT_Rokubr9k3VQUk523pUUJSwcMP4DqrsALuX_jP0vdvKsJSHLHTaHzK6utYdma1K8Lz9z1BRZrcVZItXi61agEIY_Iq6yqKeZaRdLaxVsq7xxCn1yhXNBaxCwDveIyTK5bXx6RunOWq4Pl5xBnrQdE5yVvjzShaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبریک رئال‌مادرید به بارسلونا
🇪🇸
🇪🇸
🤝
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/Futball180TV/89866" target="_blank">📅 00:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89865">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLeI33u21DRPmzA7d3EOIzBaVYBveIVbWXuldrElzwJrz7RpEq9oISgylqhawujUzBFI0O-0RV86Qa3RoPupawDV6yr6hWE1D9b6gtI7lROJ38dbMeYiW9Z3wfiBBKkrEIrolgPrWla4wr4edTFd8POG5z-RjWEn9pGLXa1KVUgl7ZwwEAPCDM6EreCihht442JGJjPHRl8AsuK-HHXzo70dx8mYRa_oSkv-sIBaCywlyBLCMBxcphUa97nTLORE-4kXBxZQJ2VwJT25C4IFMPUpWDjP1MMV2mXyI6IDFk1_iMOBP7QZ7E0vrE_qrv79ooL30u1Xiz3mfjmQ8KhGsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🚨
یه آمار جالب و بی‌اهمیت
📊
لامین‌یامال ۳ قهرمانی لالیگا
⚠️
کریس‌رونالدو ۲ قهرمانی لالیگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/Futball180TV/89865" target="_blank">📅 00:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89864">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksRXv4DJ3vo9BFsAmEgnZ9tqSdziO4HjTvnlX0vuIgj6KIbSNaBr2DLLd73RmXNNYGpNHmag83GrpEZHvzMnVo7kMmAwyknz9uDLhbWPOaoyLcMcT2Axt2-WUuo5T41UjGOjd33XxNLAbz4If-v5058z804dPxk3TA5oVYto_O4DmdSxZRRf-Zxv2docng4s1_kDnEkC1p61y4RxeyttHp5wKLBh_4yzeFQFdreDqogawC4UUHsRoYbPZrNKY5HyAqg4qAxOsnVSflgvl1-ar2iKybwaaeDDxqIriGpbb4jY_kCXUt6cM_2JWIEZXKoWtIDRDOtQ_kY19fQr_EohOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خوان‌گارسیا بهترین دروازه‌بان فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/89864" target="_blank">📅 00:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89863">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZw1VvD9Ai4-nYrRJ5eC-pg99ifQlACYX68XfYQ41K0NhtfkVMem_4eC4AmFbmQJ1whxlOGunw_fsEYxZlUaOLPvM7u7cD75CI8LwInUMta8BEGEBB4jJwVnMnRbSTIZ8E-lRlGEUOBGsko9psT-r-Z9W_Z8LqdIrFPkdg5w0mPn4Y07HsqMbhcuNUHqc8HzdZXqfxl1TC6NfYmTahavrcSx-d2YJ7Bhi5ZYIRlI0zSiotksddo5LoRk1Qb5bc9Tnkn0IGCNMa6T7aSk-lPNYAYcDilMWC2XYFtCAb6Wo_ipwNoP7GvvoYE7nq6lqadNER3oGeTx0w6pnQlFloALLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
دومین‌فصل و کسب‌پنجمین جام فلیک در بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/Futball180TV/89863" target="_blank">📅 00:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89862">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEGEbSOAcL3xingd4U9mXOiDBhO8nHf-xVhaBY_cNRlemnrtKvZmmjl1q-aj0X6KnFefZCyKoMK6nT_9Z2-6wtUuvdEuF9yO-fuc220fViLB0lcxYjAPYVV4G8-_NjJvl7k2jNpxNmhU09jh_zeiDZHlWCe-7MHv7IoyrFi1QacZNLQ1JiDIfaZXfmKnSMuKjfw5bhgLRxKbCLtiYMHAbVTdpD-bK075WsI8U5sJUfAzrr5_qMZYNvQOSxuDs-y37s6OxbosF591LaRihXEsIu__XsorPV_XrlsR4H5bQyfBH9r2HVJeFdAEM_vqFEm9f680SlpAFg89wqtUcgKAmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
بارسلونا قهرمان لالیگا شددددد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/Futball180TV/89862" target="_blank">📅 00:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89861">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رئال یکی زد ولی آفساید شد</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/Futball180TV/89861" target="_blank">📅 23:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89860">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AymkbmFDTLDUmA21uwJT1uJUwwZNsvOSsjS7TkSQkgP1V7laRWLPcfawelgrDmzcdpAiJdujmq0Co5EQ3YiwSAkdKid0M3mMwO1WZIRgKYyTeiSMxxZ_eK8OxiYTy_q1WIeJEAmPcIxfOgEBrZVqid2bLpGvEdCi9Z3Y6-v1PqQHEau4lJtdpDVAKSDyZ8wT4pWmmlls9wy3--VnbTWgdQ46FsruqhiQG9u9ByKvvlocYYXBwMHnKf_SSOYa62TX-xmnngbt0bf-ul6dFlBjj8PiH97RjRFkEe5jFWJdtfwd35J3irAVkarb8pUSsWAgrETwNP0AeNNF2GR0UEzXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ ترامپ: از پاسخ ایران راضی نیستم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/Futball180TV/89860" target="_blank">📅 23:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89859">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAlY3IZCMbS-xbqnm-BhzAGMPSf0BF-tmjDlOvU_W3FY29hYM4J6tGJ8WBCtxAasGTub7Pocoznqp7u2lFiQAyAJF-Wk6_tjl4IMSqBeZKS-9gzQNVQniaNX8JwrvjF82RW6du21M4Qp0r6r6RP7BVf7YHkTI5YvPxThlRnqaa_T3Wh1htXY750OKn6vxgY2ckZC3cQ6ahegJEBhUMC7Qg0Fiwwoxesd1Svdc1G0TDnl8GozIM8bpP7W9SyhdONzrKcY1_v5Z9vI9QjndcB9CEol8d3tKRqbhGyYNIsBhxa7ZNM2sRnjsPghFBjbMD6rV64IAf6nMe24vsKCJcsGbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری امباپه وسط بازی :)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/Futball180TV/89859" target="_blank">📅 23:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89858">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4cd35b145.mp4?token=LRZMKPcMvNp0KuC6aL8zDyNML6OG9MHegDUPCIuVsEkto27ir7HOEzC7Y2eqT4eKBOtJFYJXlJ19pnjmjlxODAbUSiNJ67FFkzeaCz8onY9V7SWZ15A8Krc3fKDEhrT4ZXwSeUEZV-dpfpBR8c6kRyHSuPs9Viq4Ltx81LNW6zn05Eo3lXZsNKjAIKA3hpF-GhC2vPiHixXJ8bXF5B3wdnZy5-qqyInfX8wqZQeCGuAwCzHbLNYn8-ArYdt9H39Vewl2D1JCs0qUEJmTj8vTmqk8jZ0y-qSEC5jGC554IKlm3pssfARrI2n6IYDckb2ZlwTCXKWAGwxfTqJofY0g1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4cd35b145.mp4?token=LRZMKPcMvNp0KuC6aL8zDyNML6OG9MHegDUPCIuVsEkto27ir7HOEzC7Y2eqT4eKBOtJFYJXlJ19pnjmjlxODAbUSiNJ67FFkzeaCz8onY9V7SWZ15A8Krc3fKDEhrT4ZXwSeUEZV-dpfpBR8c6kRyHSuPs9Viq4Ltx81LNW6zn05Eo3lXZsNKjAIKA3hpF-GhC2vPiHixXJ8bXF5B3wdnZy5-qqyInfX8wqZQeCGuAwCzHbLNYn8-ArYdt9H39Vewl2D1JCs0qUEJmTj8vTmqk8jZ0y-qSEC5jGC554IKlm3pssfARrI2n6IYDckb2ZlwTCXKWAGwxfTqJofY0g1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوممممم بارساااااا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/Futball180TV/89858" target="_blank">📅 22:56 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89857">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
فرررررراااااان</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/Futball180TV/89857" target="_blank">📅 22:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89856">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بارساااااااا ۲۲۲۲۲۲۲۲۲۲۲</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/Futball180TV/89856" target="_blank">📅 22:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89855">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گگگگگگگگگگلگلگگلگل</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/Futball180TV/89855" target="_blank">📅 22:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89854">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e39aabd36.mp4?token=qA-SDviApmwgY8iA3PfsNWe6yRXqNYm6XI3ULVwEJesRyxpY16bOZMxb24XdYQ6Ax7vSaRCL4jF8N5L4psBmapGH45_ETJ0dOIAkbVs_JVihITMmDtXZn0kqlxfpALThZ5lpEDTEJzTqLBcgPIUtoUF8uo5YHZoQqh6DM2ADvzUuUTiH6frRxAO5gycoYNA-Rz52qHYauxqdFCCIHevR_vX4tauoEaeULaakShYVWSQt2iRQZh2r8xaCqRlFNk4b6015bDa-6LykuiqKRfeUCgKsrYCSmSLlpg9SAyCMkd1wTJ7fnDZ6dRW3VJN9-HMkp--Jg5WwwCHOCYGQcjEq1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e39aabd36.mp4?token=qA-SDviApmwgY8iA3PfsNWe6yRXqNYm6XI3ULVwEJesRyxpY16bOZMxb24XdYQ6Ax7vSaRCL4jF8N5L4psBmapGH45_ETJ0dOIAkbVs_JVihITMmDtXZn0kqlxfpALThZ5lpEDTEJzTqLBcgPIUtoUF8uo5YHZoQqh6DM2ADvzUuUTiH6frRxAO5gycoYNA-Rz52qHYauxqdFCCIHevR_vX4tauoEaeULaakShYVWSQt2iRQZh2r8xaCqRlFNk4b6015bDa-6LykuiqKRfeUCgKsrYCSmSLlpg9SAyCMkd1wTJ7fnDZ6dRW3VJN9-HMkp--Jg5WwwCHOCYGQcjEq1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
گل اول بارسلونا توسط رشفورد در دقیقه
9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/Futball180TV/89854" target="_blank">📅 22:49 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89853">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWlkMDjZ4N2z1ZvE5oSl_3aSIAH9xvAQRcTQ8Ng-4wlmeMmRN2qBWtQfPv-bzHS0U2OC3M97u3NcP9mlYnD70qkj3D2Dw-X3qrLlquUjrkcC6Efzzvji3DRgmNiyY0wPS2hJ4gCSMM601tZGksvMKRg7lI05rDo26bfaux3jSQYxqH6TilEXjlgEQjvMpVCqC18X_xbnImBh3uaZS0tV_ARXyBWDIqK_q1LTF190VAPBy6wtF414A6qrcQZ3OwtuGwieTwDJqA0-lTLxf8t9IvnSC8RMYyg1g_Dkv6yPplRzVq7utmpE4cH4cY_vNoQgdXenRda8tXYoWXWSmuhEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزيدنت ترامپ
: ایران ۴۷ ساله داره با آمریکا و بقیه دنیا بازی درمیاره و هی وقت‌کشی می‌کنه!
تا اینکه اوباما اومد. او فقط با ایران خوب نبود، خیلی هم بهشون حال داد، متحدای ما مثل اسرائیل رو ول کرد و به ایران یه فرصت بزرگ داد.
اون ۱.۷ میلیارد دلار پول نقد هم با هواپیما فرستادن براشون، کلی پول هم در کل بهشون رسید
انقدر پول بود که خودشون هم موندن باهاش چیکار کنن! ایرانی‌ها قبلاً همچین چیزی ندیده بودن.
اون موقع عملاً احمق‌ترین معامله تاریخ رو انجام دادن، چون یه رئیس‌جمهور ضعیف و بی‌عرضه داشتیم. بعدش هم اوضاع از اونم بدتر شد با بایدن خواب‌آلود!
۴۷ ساله ایران داره ما رو اذیت می‌کنه، آدم‌هامونو می‌کشه، اعتراضات رو خراب می‌کنه و تو منطقه مشکل درست می‌کنه، ولی دیگه اون دوران تموم شده. دیگه نمی‌خندن!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/89853" target="_blank">📅 21:31 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89852">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGz5Tiy0myKWTi9rmHo8y2Etn008kzJmMmZUf7M15m06LKb0m-pmc5ecrAYqrA_jJxcXkYS_0oWQCbbfFruRZ7ExlbxgdJOPF7RAx0GaX-uF80Fok9towY3oC3Sh4jxC-55LyJPJLuJKVtr5zyXapXA3Bn9Y2lTzeyQmcDXyNHMfut9e88F9nT685azb9gzfPKbOd1iN5HRZtf4gryjLeZK0ahshJjkiiro_knfJCeMql-dawSCN7BgoTLF_MjPbVFUsd1CMD4rLWhHmv_4S9BoP601HnT6_bphP59qS8sYOu4YFPJ-hXOlEXg-ab7krA5oMv0dihUr8YZDaWCjVTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترکیب رئال‌مادرید مقابل بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/89852" target="_blank">📅 21:24 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89851">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrtGZXTpW0UrGxypmqk7TghfeUEzx6TpfVqnIZB1uS_aU3s_njNXNkeibQ2nrVyP83vj7k03Op_WO1yekfRzv-w78MbuHS2Xu9v6ksaAMdKtRiyM85moy7XGylnvdGfT3laPuh3e9SKJg2dmzoFPAepRBGdwAeQuQ6BskPkAAYy6DI3X-jmL0cp9DzimrNxBStIHTJ1DJTKDhBUaFpaYsxflNnlLZqB1Fyk8JtPRE_6Hxw5WZg1VkUUBs2HJXd0ksEo79dUcNcfkVJYjDm9p91YYjQ7Ys30F1iRb5pq1bHLmZEzHhOia480C15HElSJhGu3QNLq94Z7bsZD37VAL1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترکیب رئال‌مادرید مقابل بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/Futball180TV/89851" target="_blank">📅 21:06 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89850">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
آرسنال با برتری مقابل وستهم صدر جدول رو حفظ کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/Futball180TV/89850" target="_blank">📅 21:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89849">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b416a65c.mp4?token=XnxXuJ2isdMFXLBPo-x81hCCzL-gs2q-l-kOx7v0jDYrpHOWYGp2PdYkAv8Rh5hLKxuShipVAil-wevC5tsyZjD6y3gdtIs9td-2gUQRXLWgtA6tQ0Bde_G1qHf1Q-mcTCyhOfnUf2nr97c6AyJZ-3SnZKaQU2AXaWguEu7ne_xsr_zhxMe-0j2JR0_EXUaBP0djESxQ8o_cjw2K5h8B1DnB98UL_PrH8i3G7oooF3NYtppxQCtAl7Qc9ZRxrFPypwJaMUD5VZ201mpoPPagz_mayC2ELBxpw9WXEHUvmn3p-rRA39rzzXqT-C5IvjjnPI-I4EB8Q8T2LOp77ySzwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b416a65c.mp4?token=XnxXuJ2isdMFXLBPo-x81hCCzL-gs2q-l-kOx7v0jDYrpHOWYGp2PdYkAv8Rh5hLKxuShipVAil-wevC5tsyZjD6y3gdtIs9td-2gUQRXLWgtA6tQ0Bde_G1qHf1Q-mcTCyhOfnUf2nr97c6AyJZ-3SnZKaQU2AXaWguEu7ne_xsr_zhxMe-0j2JR0_EXUaBP0djESxQ8o_cjw2K5h8B1DnB98UL_PrH8i3G7oooF3NYtppxQCtAl7Qc9ZRxrFPypwJaMUD5VZ201mpoPPagz_mayC2ELBxpw9WXEHUvmn3p-rRA39rzzXqT-C5IvjjnPI-I4EB8Q8T2LOp77ySzwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😊
هوادار گالاتاسرای در بازی دیشب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/Futball180TV/89849" target="_blank">📅 20:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89848">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57353990a9.mp4?token=eRp8DWudMnTprbRAYW8EVV2VaQI1vKb5FxwDZvJnBhvXD_RTOPVCu8d9pknxoDAvaNz6NgxdjDzwqMB-RbX_TnZYM1X8v8PxP_MWp14SpzhErUDahr6Lgqji-qh8VF6AWPHIOONnxbwZR4aXH1k-g9zTfega3Ym6gA6LaXXQxRuCdflW4MQ9w-CG13gjG1bhm2rlbTqmx4sL9ZCCl_1Kzzu6nO9Cn8MJ0C9_nqseZjykZCUCqI-EI66c0q6zpaOr7yK9QWRvKy__ShkalcgGuR1isQefhiewSTwc5cJvRQ-ALgpBVZrtzHTBTczRf5oslrRQTqyNcCs1altEV99idzeN5py-W_tUeitk6n1naQxmE27U0w-mnRgdFJYh1WshGsWeXONSPVKawRDzx47EeJR4Pl6f2skiHsENi_drTa2u2UaBKHQKRI04vN18lRhOUAOCWfEB20qS5UBahJEbWAlcqAsxuL1WMdRv3clzAhwIN6z1bbwL6LmyW9NNWLSUemgwuf7KwlBSs0l9hf18W2RKeggHCFN7BvSFAsaaFCzcPZ1BGwXJUboet4impYvddV-NBQcnuYVCbGU-nok6wlEIzQ0KHa51rDI8FhqEveAGAdrDJf2YTPs9nwQ37ucQL8DZHKIwDlancFMWxtVdIhNtb0vED95_yerVnnNZ6Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57353990a9.mp4?token=eRp8DWudMnTprbRAYW8EVV2VaQI1vKb5FxwDZvJnBhvXD_RTOPVCu8d9pknxoDAvaNz6NgxdjDzwqMB-RbX_TnZYM1X8v8PxP_MWp14SpzhErUDahr6Lgqji-qh8VF6AWPHIOONnxbwZR4aXH1k-g9zTfega3Ym6gA6LaXXQxRuCdflW4MQ9w-CG13gjG1bhm2rlbTqmx4sL9ZCCl_1Kzzu6nO9Cn8MJ0C9_nqseZjykZCUCqI-EI66c0q6zpaOr7yK9QWRvKy__ShkalcgGuR1isQefhiewSTwc5cJvRQ-ALgpBVZrtzHTBTczRf5oslrRQTqyNcCs1altEV99idzeN5py-W_tUeitk6n1naQxmE27U0w-mnRgdFJYh1WshGsWeXONSPVKawRDzx47EeJR4Pl6f2skiHsENi_drTa2u2UaBKHQKRI04vN18lRhOUAOCWfEB20qS5UBahJEbWAlcqAsxuL1WMdRv3clzAhwIN6z1bbwL6LmyW9NNWLSUemgwuf7KwlBSs0l9hf18W2RKeggHCFN7BvSFAsaaFCzcPZ1BGwXJUboet4impYvddV-NBQcnuYVCbGU-nok6wlEIzQ0KHa51rDI8FhqEveAGAdrDJf2YTPs9nwQ37ucQL8DZHKIwDlancFMWxtVdIhNtb0vED95_yerVnnNZ6Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
جو اطراف استادیوم نیوکمپ
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/Futball180TV/89848" target="_blank">📅 20:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89847">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
ترامپ: بالاخره به اورانیوم دفن شده ایران زیر زمین خواهیم رسید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/Futball180TV/89847" target="_blank">📅 17:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89846">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
ترامپ: بالاخره به اورانیوم دفن شده ایران زیر زمین خواهیم رسید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/89846" target="_blank">📅 17:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89845">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpMy-eTquvClTUUF7Kj_tdM_5lNW3xiDdRr5mTAGwpVIzJ-9v3mb-KirtQ8iUJ_K0SAtmsQNGtVzc85wZHWfjSnWLCEPuMp3QT4UUkI0_L1498xHFDFCf8ye5zJyDLHCiEJJCsYPh3pCrK-XcTWS6iiSoYz2MHEHl58bb7Q6yFJ8Yqf4JowgsHBOE_4-MsrwbycNwTEhLmIbgFnOlY2MBtV9yASwl9jVqAxzTxNGRCnqVjJ88NBKB_PzYOO3nDk1xew1i2VqPC4dFO-VJQVmFlxcXHXOS5E-xy6KBiZjw0OT3AYWgOlNPkw_7szLRZfIb9F952Z-S5FBYbYPMqmbZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
منتخب این‌فصل رئال‌مادرید و بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/Futball180TV/89845" target="_blank">📅 16:00 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89844">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWJoX7nTVXdK3K5c6ldK3JgE0uxH8-Hfvy70rpkaur_DhLYyAqbtIIMpu9lgvQKPzrP6IRTW7U1Ixp8-BFu9d8plbpOa2hnNVkJLTeOLv-QvI6Q2tCswgCmkKr-9OBjzORRqo7S3ShAmqpgEDCDqVFOUwpDGg8vzr4fOW9SVbaLo09x5y8zW0Nv6AnQqlSNgQnA3z_Vye8jqrzrcAeiOk5IW6jl5-ds7_fBjQxN9OAujZk1qCpwSBMd793fkjMZmX-PE03h4NBc5LvJgoWjJPjll0JVTnMaEhp1RfZGK7FnvwzZDrKdofJWDcfArGPvElnrVgmwb7ChwzYqL--dLeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
هانسی فلیک در الکلاسیکو:
‏۶ بازی‌ها، ۵ پیروزی‌، ۱ شکست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/Futball180TV/89844" target="_blank">📅 15:04 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89843">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utkbWVPExJrhehq959fR4Fh_zCCDfDcKtMivFuF3M2Qj7md1Xn1DxqUMUkAZf24XcfULnc5jJoDg4sx_iwhkgvujTjCrNaLR7IuXRSymTnkkcOS6RAmCoGLWGkWGblq3rxxcgmxjlJd_jqPVYcC4koBazEtXjSGdbjl0WuAhwMBRkk_IIyCoHNgyPqkUx8BjEuN46czQqD8KxU6u-8vAhpVHPgrpRY5FIXpbDK4QvVAYDHEQQ5JqI4AVBAb4fyvVMjfHru6d-K_wlXk6wVuyrP_uNKc_zjUYXQU0i2nCm-Sob4GAVhe99e5KIgZ5Vckj-A4DwAD5LTNV5zNEyp4hgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست رئال‌مادرید برای الکلاسیکو و غیبت امباپه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/Futball180TV/89843" target="_blank">📅 14:53 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
