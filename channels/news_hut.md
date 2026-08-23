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
<img src="https://cdn4.telesco.pe/file/QaD8XCH7rpu4vnOa94wSLMWcZGQvoe_2txXQqSRTP1KMLalMuYX73ll74_JUEiY4R-NrgzPMKQgpR_fHMGvKdDsgvRI6QMeSYH_Sp0r0bxqGlsBlaadN6wHimC6p5_iy0g9tUjMU6B7Tl3QcJvjo88iOSgUpki7qGf0YVlseGJkN3zl7M0IbrjiIbkDdc0DhEolpgAfJjKaTnd4T-H4qMXR7cmL3rR_9BqXBBi1T8f0j-X7AuwKx5n-Nh76rHLRN_EqPdvs6jnheirgQxb_DC8Jt9yRSPDdEwdZ_D0QPnaHenj5xnErEEb_oPiGYxuNlsb70Tl0OSMbLtoK6bnTz1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 118K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 13:44:23</div>
<hr>

<div class="tg-post" id="msg-70455">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">💵
دلار: 1,980,000
🔼
هرگرم طلای ۱۸ عیار: 21,907,000 تومان
@News_Hut</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/news_hut/70455" target="_blank">📅 13:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70454">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd4541c3f.mp4?token=NwwgvAJcxwx1O94uf5HkcA4m3X97lVX2Kf_iNB4-9u2HE75jy-B_wHIfPCK3kJjNFYNg1MATViNdAON3STLP-NiHNOqEE8uh833PNG6zTPeas07GYIuXlY4FfamD_KEqI4LUWOqrWa4WNi6hrz_gO56d-zrnRuVT63wZNy0zlLol5Mo5A4BAZnZRf75z_Ke2kjCnrMTVw-t6Cu4iWtD6DvPC0on-B1c6Ueg_bIYDv5rXThS-S96ER8saSWARDFutXgdioqSznM2g36J0JdD7LYlnGSPlB8LUoz54E0edSq8_KQFKobiqkDPRoTfOkZ79j5yvuf5oqb54WJQDmCEbdEFZiv97RKhCbXeNWGOKGAuvunQDHARaFt88tTC-3BZ5aPPuZl9werMQUYbGuvPafRyjW_M78-tbRNJ7wxZ8dMko755X1mR3T3NwfmhPXPkPf4D63FuquioSXePotFiLe2GVfmt-J9vMG538LHQXVjo4PB_E0qQ4a6aDcnMrOSKyQxeQEwobPgB90-Hf5rWjmOeDaX8YYs6npQAhblFKzThdZ8uYTSsxQy6XvsWS9qJcF5F3gGyjmGe7Mb66GRjQqoYwYdX_iTLznr_xl0uSMgs2M-VGLK2CP7orV3Lna1Vwf5OH_2d-TsL6o02vwEu1RPeVFXspPMwNVdSwSL5T-gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd4541c3f.mp4?token=NwwgvAJcxwx1O94uf5HkcA4m3X97lVX2Kf_iNB4-9u2HE75jy-B_wHIfPCK3kJjNFYNg1MATViNdAON3STLP-NiHNOqEE8uh833PNG6zTPeas07GYIuXlY4FfamD_KEqI4LUWOqrWa4WNi6hrz_gO56d-zrnRuVT63wZNy0zlLol5Mo5A4BAZnZRf75z_Ke2kjCnrMTVw-t6Cu4iWtD6DvPC0on-B1c6Ueg_bIYDv5rXThS-S96ER8saSWARDFutXgdioqSznM2g36J0JdD7LYlnGSPlB8LUoz54E0edSq8_KQFKobiqkDPRoTfOkZ79j5yvuf5oqb54WJQDmCEbdEFZiv97RKhCbXeNWGOKGAuvunQDHARaFt88tTC-3BZ5aPPuZl9werMQUYbGuvPafRyjW_M78-tbRNJ7wxZ8dMko755X1mR3T3NwfmhPXPkPf4D63FuquioSXePotFiLe2GVfmt-J9vMG538LHQXVjo4PB_E0qQ4a6aDcnMrOSKyQxeQEwobPgB90-Hf5rWjmOeDaX8YYs6npQAhblFKzThdZ8uYTSsxQy6XvsWS9qJcF5F3gGyjmGe7Mb66GRjQqoYwYdX_iTLznr_xl0uSMgs2M-VGLK2CP7orV3Lna1Vwf5OH_2d-TsL6o02vwEu1RPeVFXspPMwNVdSwSL5T-gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طرف رفته ماشین "شاهین" صفر کیلومتر خریده، بعد بهش گفتن با مانیتور؟ اونم گفته آره؛
حالا که ماشینو تحویل گرفته دیده مانیتورش روشن نمیشه، دست انداخته پشتش بازش کرده دیده توش مقوا گذاشتن..
@News_Hut</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/news_hut/70454" target="_blank">📅 12:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70453">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNrlstaY-OElzmcghYzTA3uyRqgBjuym_SUL_1vPcX9xpHI0iKwDOG6vjeD2tXMbTQXa2Eie75L3HOSfPtxevdfPiFpPpyXAEebKFEKbu26fKofsy2FFrZnTdOuSypdVaDdHoaRP0QJVjQIMglsf-gwCwsnq1iEc6Fq2pYvhPkQrffoE1C-IhHdhnrfFhV_7pvf4c-JrbhYWXpfMLsKNyncbmJdwr2ZcQS_qHbvpDEcse2Vw3IzD7-wvhbyoqd-X3YPsxNdI_QaU5pu70oAD0vTosjt8rv4ckRiK0FD_hFWYBPbfWHGb9OfUmJvkwok6DM9RVtMOZmUfe27mVxLxjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد کنکور و امتحانات نهایی قیمت چادر های تک نفره حدود ۵۰۰ هزار افزایش یافته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/news_hut/70453" target="_blank">📅 12:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70452">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70452" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/news_hut/70452" target="_blank">📅 12:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70451">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YozeQ7qhI4vdffPZUHi8SlAAchECiYtaBVw_qLA0rXsQjdncal8oB7hQE964vhja525xiXaTmiSWSrhnhOrZPdQtEXBHqHd2K3_wr6jPF_50zqbjk8lR_wOvGtkXLjPOICjkwo6TfJsz3W7akOI4Shgt009iK3fSFzmurHLTRQEMuEzJV1ZIeVgGMaFY-CWOr1MqhXno6sG_Ef3Um5SAC4K7vKXb_b6nLbP_yB2NnrCAtwqtmankskxvp7b8WnGcjc7KISpMjlXLNfesy2R49byL6GCuTXWsgPHwWsvQ1fNxSraV3CnS3RgxNA0d4zOb9uJ52AI2BxPcUhxZd6kk2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r1
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/news_hut/70451" target="_blank">📅 12:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70450">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25b2c22e49.mp4?token=CSFEOUKsgH0UxaZJ-TWFo-mmNbw7iVwt5EeZolaA-Nin5dJ_gV4i3p93SEwxKVc6iIRx2fcfRzDfoNpkELULWDPhjYlePNznnKSv4nnnxzSwDYc2Ez29qd-OVp6YvJWQAlhf4zy2-kp-FWhIvEatchTq4327vnmd3aB_EA49vHX0xMSUZ2G6xhYVra2armZsaQI-Sca25FGVigqi86o23L8Sj8FWP_LZYyokYJPFeDihAXz4yt0LJt8vGz7ujihCQezR_ieOrKXfqhHCQVC67KRu9a1rsFAxQOSya_gFIRZCO3PaI9cMbKgdhzjgwEUZvHNlGkWAbdQLblC8MUUi8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25b2c22e49.mp4?token=CSFEOUKsgH0UxaZJ-TWFo-mmNbw7iVwt5EeZolaA-Nin5dJ_gV4i3p93SEwxKVc6iIRx2fcfRzDfoNpkELULWDPhjYlePNznnKSv4nnnxzSwDYc2Ez29qd-OVp6YvJWQAlhf4zy2-kp-FWhIvEatchTq4327vnmd3aB_EA49vHX0xMSUZ2G6xhYVra2armZsaQI-Sca25FGVigqi86o23L8Sj8FWP_LZYyokYJPFeDihAXz4yt0LJt8vGz7ujihCQezR_ieOrKXfqhHCQVC67KRu9a1rsFAxQOSya_gFIRZCO3PaI9cMbKgdhzjgwEUZvHNlGkWAbdQLblC8MUUi8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
یه دختر ایرانی رفته یکی از روستاهای روسیه فیلم گرفته و نتیجه‌اش قراره شوکه‌تون کنه!
فرض کن یه دختر ۱۰/۱۰ داره لاستیک تراکتور عوض میکنه یا سیب زمینی جمع می‌کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/news_hut/70450" target="_blank">📅 12:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70449">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0832bfae35.mp4?token=tLBlE-xBF-pD1yhDgsGdyAlYWTtBqe4tvunurEpKx4k7FDbQ7UiygORLQMEPG4ztkajrlzj13XxfBfBqyjDKd8P71GACJO023tD2zdBpvg-fzycq9ByfXev24HORR_XVWn_fvSBoiCGXRNOWngIIpTFHiAVPotdxI1EYSQu4aFSMd1Q0HQKwuuNm3Iaz3E0fagb7sKefieBEJdEFUctAKZsocaOvAhHvPYXGgJZgAgfDXF4k4hHr0_4q-z-iKGY-lUmvPTo8X1UUaAAYO7MpIc5HLu3hPCbvU2D4mlghxGbTb_2K46HqEt5BVrHLEq5L3OSItJ7gJLz7EngCON-SfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0832bfae35.mp4?token=tLBlE-xBF-pD1yhDgsGdyAlYWTtBqe4tvunurEpKx4k7FDbQ7UiygORLQMEPG4ztkajrlzj13XxfBfBqyjDKd8P71GACJO023tD2zdBpvg-fzycq9ByfXev24HORR_XVWn_fvSBoiCGXRNOWngIIpTFHiAVPotdxI1EYSQu4aFSMd1Q0HQKwuuNm3Iaz3E0fagb7sKefieBEJdEFUctAKZsocaOvAhHvPYXGgJZgAgfDXF4k4hHr0_4q-z-iKGY-lUmvPTo8X1UUaAAYO7MpIc5HLu3hPCbvU2D4mlghxGbTb_2K46HqEt5BVrHLEq5L3OSItJ7gJLz7EngCON-SfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی ساحل میانکاله مازندران، حامیان حکومت با چادر دست به اعتراضات زدن و اعلام کردن مردم رسما دارن لخت میشن، ما دیگه تحمل نداریم، یا دولت برخورد میکنه یا خودمون دست به کار میشیم.
@News_Hut</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/news_hut/70449" target="_blank">📅 11:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70448">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⏺
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:عاصم منیر فردا به تهران سفر می‌کند
این سفر در راستای تقویت همکاری‌های دوجانبه ایران-پاکستان و ادامه کمک‌های پاکستان برای کمک به تقویت صلح و امنیت در منطقه صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/70448" target="_blank">📅 10:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70445">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8129d80281.mp4?token=Ke5L30Z1Kdz-u5T0-srB7zsLOC9yq3WUHZXyUEfSi7RaaOTrqxQLnk3oN0G5FuQAcM856Oc4GVWskmVx-0hJ2dUciw3_N1FWNk0wACbR4iOXwJlWAz3nePr_mz4zf4fZj3oqrCX14IjnS5E0LXzXgyFb0pDf4uEof1ueMONKS5vqDUU4xh2B1cHd_br19IoyPUDNfMwybeLA3dgD2NEhqmoWwSJUAe2Rky8nIQqQmTs7AyuL3kKRQIObo1CdNphet4-FAZX-xFfW6yk_9y-gFSYr6wjzO9H294_ayACTC6lU3F7I1alEsPdUs3YvFE9_pV3ZwAObPmu17Kd7bumWcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8129d80281.mp4?token=Ke5L30Z1Kdz-u5T0-srB7zsLOC9yq3WUHZXyUEfSi7RaaOTrqxQLnk3oN0G5FuQAcM856Oc4GVWskmVx-0hJ2dUciw3_N1FWNk0wACbR4iOXwJlWAz3nePr_mz4zf4fZj3oqrCX14IjnS5E0LXzXgyFb0pDf4uEof1ueMONKS5vqDUU4xh2B1cHd_br19IoyPUDNfMwybeLA3dgD2NEhqmoWwSJUAe2Rky8nIQqQmTs7AyuL3kKRQIObo1CdNphet4-FAZX-xFfW6yk_9y-gFSYr6wjzO9H294_ayACTC6lU3F7I1alEsPdUs3YvFE9_pV3ZwAObPmu17Kd7bumWcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درحالی که تمام شعبه‌های ساعدی‌نیا پلمپ شدن، کافه قنادی "بابک زنجانی" تو شهرک غرب تهران دیروز افتتاح شد و قراره پاتوق جدید بچه پولدارهای تهران باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/70445" target="_blank">📅 10:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70444">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc8a06759a.mp4?token=culBKM1J382X3lV1WsN2lbeOYiGlTBnrfJ7pFZwVG6Joby9BtaQgRyOpQwecbsIFDIBppv7AjPtZ4JYnK0eILVTXpJMseP8QngOaP6fLbFFwlpdmH6inEecNo87faVsH6_2hHX1ijmjg9QPMq9TlMRrouIvNK2_p-IITWVvbLBJ0eKs6VLeIcqzNpbnFR89-lyPnJ-O4ZGSzu3L5jnzQCJ4pjcPId4Qc3Jluk-WLrVXGgBY0umt04YePUvRd4KuHuZ_cpNbkUCYrCBWf_15GconeFWO5kGxHvzPOqU7ucrKRv4HmAkEPZyDKsEWbgzF0EZMbvzSH2Qw14A4HdAityg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc8a06759a.mp4?token=culBKM1J382X3lV1WsN2lbeOYiGlTBnrfJ7pFZwVG6Joby9BtaQgRyOpQwecbsIFDIBppv7AjPtZ4JYnK0eILVTXpJMseP8QngOaP6fLbFFwlpdmH6inEecNo87faVsH6_2hHX1ijmjg9QPMq9TlMRrouIvNK2_p-IITWVvbLBJ0eKs6VLeIcqzNpbnFR89-lyPnJ-O4ZGSzu3L5jnzQCJ4pjcPId4Qc3Jluk-WLrVXGgBY0umt04YePUvRd4KuHuZ_cpNbkUCYrCBWf_15GconeFWO5kGxHvzPOqU7ucrKRv4HmAkEPZyDKsEWbgzF0EZMbvzSH2Qw14A4HdAityg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یادی کنیم از سخنرانی طوفانی «معمر قذافی» ؛ میشه گفت این سخنرانی یکی از دلایل آغاز پروژه سرنگونی قذافی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/70444" target="_blank">📅 10:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70443">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyIwXT9NvK_z7j6-BQpfPvHEL8x225BUgyrIke_diN7mhwmwGOuByZ8AJRGome_WBQqtEennNsJrTGEtYFge0d9le3mxE9MO8UrBGrkBgE6AHHqG9HaNDxmo9jI2xwjoDNl7_6q7rUIBYgNH_xl33vhFXYtH1EExoqM3ewvBQ_Kt41USbX8xNgavaCbad3LVGle1ZTg_5t94hByxbsajSUF4R8BaL2XzzOEBLVk1hgu9HAZteLGStaZTbC9aYgjXpw4lvdcWUMx1fHkI3_HGfs8XSX91ESNX2EO3EX0O3T4tYOSiuuEFnXiGCV63WIGZLewaQc3MVO4bPNerP-Me3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت کنکوری که گذشت:
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/70443" target="_blank">📅 09:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70442">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78b2128551.mp4?token=KOTXWOPMoJCwNBocAw7nb6CDtoq20SV8chod8AwkR-_m2603wHMDxXFrDA9LublXdZDlkjRxMUw8ZlgsSukTBZhxm164H4Q5PLF65-GoxlYX35_KT71a6fKmcwdUi4YXYyEfkamxjYGAXfu_Z9Na-j6nfg3A8EK9lOd40JibEL7Rin5iRZl-nLyh7sqvKKNwLR5enE21Pf_BIj8x3YwEVd14TllkPlx4VDmJ8iIEgb2eA7p4AuQKDlMwtOoB5ECzblk5W8brACUEfcVbSwiT9cjUG_A8lUVdwBOZt-DomAjqNO2IMU9-t6jPyhA7MlnUxnC90B-AgzvgEZqpYIqJ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78b2128551.mp4?token=KOTXWOPMoJCwNBocAw7nb6CDtoq20SV8chod8AwkR-_m2603wHMDxXFrDA9LublXdZDlkjRxMUw8ZlgsSukTBZhxm164H4Q5PLF65-GoxlYX35_KT71a6fKmcwdUi4YXYyEfkamxjYGAXfu_Z9Na-j6nfg3A8EK9lOd40JibEL7Rin5iRZl-nLyh7sqvKKNwLR5enE21Pf_BIj8x3YwEVd14TllkPlx4VDmJ8iIEgb2eA7p4AuQKDlMwtOoB5ECzblk5W8brACUEfcVbSwiT9cjUG_A8lUVdwBOZt-DomAjqNO2IMU9-t6jPyhA7MlnUxnC90B-AgzvgEZqpYIqJ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
📰
مراد ویسی، تحلیل‌گر ارشد ایران‌اینترنشنال:
🔴
جمهوری اسلامی با سه‌راهی مرگباری روبه‌روست:
تسلیم شروط آمریکا شود
وارد جنگ شود
بدون توافق و جنگ، با فروپاشی شتابان اقتصادی مواجه شود.
🔴
این وضعیت اختلافات در راس نظام را تشدید کرده؛
احمد وحیدی، محسن رضایی و حسین طائب خواهان ادامه تقابل‌اند...
پزشکیان و قالیباف با اشاره به محاصره بنادر، قطع صادرات نفت و کمبود بنزین، توافق با آمریکا را ضروری می‌دانند.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/70442" target="_blank">📅 09:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70441">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">💎
میدونستین تو دربی بت
✅
با شارژ بالاتر از ۱۰۰ دلار ۱۲۰٪ بیشتر حسابتون شارژ میشه
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/70441" target="_blank">📅 01:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70440">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70440" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر D
erby Bet
✅
✅
✅
✅
واریز و برداشت ارزی و ریالی
‼️
✅
بونوس 120% اولین واریز
‼️
✅
بونوس برای 4 واریز اول
‼️
🎁
بونوس ورزشی هر شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🎁
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a31
✔
@DerbyBetOfficial</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/70440" target="_blank">📅 01:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70439">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8QyTbDVFlNc-uSpKJTdXz9kZeLacGOH0O9oXLNU9bReSGwvoJA1ZcwD_QXVKYN_qUe7yh68O8ut9cGbz8OPbXJmOmTBDL-jtmFQYfKwqlx490gPGzcT7wtCdyzj6s0nzDCR0w9Z282ecA7jyGDt58RhbssNw6OWxuYFdjLYdiSMNYW8GlIcqN4PViGdysxZCa5rFZtLn66WzZoWqovtS9JuyNM1FZ7_sEDm66LlHXb4UXqX-jVqdChdO4DU53sVXxtBTwOrcqcvXe4nougEXXrL3f-dDb3MT55pWPTwLiXxT74PdxaldiXVT0rFG_ogaDCmvrre_aekq_wV-QZhRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ با انتشار این پست ادعای مارک تیسن مبنی بر اینکه بیش از ۱۰۰۰ کشتی با اسکورت از تنگه هرمز عبور داده شدند را تقویت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/70439" target="_blank">📅 01:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70438">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J75e18vPc6u7xsUuc7xMYkbdIZmTmh6DxaTL9Dycb8KmeNA8Uk8L7BxCgHIfe6-tQB4Xu72bxqtVbLmI0wGCLJ0s1TGsLpuz2oyImxTNeQvm6bbU9dibS9p1DME9ycg4O2alU5G35pRwOIPAUhvsUa6HIxMqVEXgh3j8JBv0wDwzsq2mSxKla0UsllA8GGCO7gskhwNM9k2VBUiqnAFg6xL_qdoHXIBz45qQaoq6uJipY5m3UthTomxJ8vjHx-WlrjtD8K-dhu7-s9C_NmuOOqUS1l1nqKDIz6D8883S40txxcDcaHOvaclCQz8DTP9hU480BEq1InH-L-iVUpmPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
املاکی مجدد این تصویرو با عنوان تنگه هرمز قلمرو جدید ایالات متحده منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70438" target="_blank">📅 00:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70437">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39665a7cce.mp4?token=Wk5zDvVLPRukXAPT9IKcmG3z43VYnFzk6Vw9_Tw-Tt9s-o3sXeiXWyJSfqXHXtPOr-kgwmbIWBuufJdAThsfqCF6-_Ri4WbMjaSLn3AVMK6ugl6yFa8dfEAr2Er5w-3j1SNWqfljEkGPGaBbXGq9aujR5OS00l-cULaCDn4wNBo2Ep-zIUtHWbeMHsIbklt48QQT2wWyD0c84zuw_nCJpcdjMlj8hfQd-MjUQuPqmPhjUhjVh9MvnshIGFx9ms2HbnJRcFcAT3ZEiObBMyeHEhodxL-AiQ314tnoF1e7jfdn_pw-d32RNGL2S9tMzH7_R9DzUHPCuUyAb5g6vBkvMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39665a7cce.mp4?token=Wk5zDvVLPRukXAPT9IKcmG3z43VYnFzk6Vw9_Tw-Tt9s-o3sXeiXWyJSfqXHXtPOr-kgwmbIWBuufJdAThsfqCF6-_Ri4WbMjaSLn3AVMK6ugl6yFa8dfEAr2Er5w-3j1SNWqfljEkGPGaBbXGq9aujR5OS00l-cULaCDn4wNBo2Ep-zIUtHWbeMHsIbklt48QQT2wWyD0c84zuw_nCJpcdjMlj8hfQd-MjUQuPqmPhjUhjVh9MvnshIGFx9ms2HbnJRcFcAT3ZEiObBMyeHEhodxL-AiQ314tnoF1e7jfdn_pw-d32RNGL2S9tMzH7_R9DzUHPCuUyAb5g6vBkvMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
توصیه‌ام به مردم اینه که کم کم از تو همون خونه و محلات، شروع به تولید چیزهایی کنن که نیاز دارن
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70437" target="_blank">📅 00:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70436">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/927919a024.mp4?token=jGFYAL9UC5gmxd5Mp6jumPBgQtOJRRLdibnUymluBnyyoohtngP6IbC4aqFRboi_G--ZEkjCTXRxLiRaZm9hGlZx9sfhR6aEfyATKqf-SOupg2drHG5oTRrOjg8GYXtQsTNTzdHD3bqvLxprdtUpkkDNd9qNAX-M0OtelPeri-rQcpTFD4rG4N5C0Ps5YLfou3BzvYyybBZF821O9zbSnr1_7GogANPX6Jjz5CktWGvsFKfaONLjlljAKZbaD8uWObqX93eZrw9PB9XlHadFT6N28AXHeKpPOY8Q4mzfjfuI1WyPVs1psRxGIcXr56IfnjLzJQ5sv0pRovwcoREG7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/927919a024.mp4?token=jGFYAL9UC5gmxd5Mp6jumPBgQtOJRRLdibnUymluBnyyoohtngP6IbC4aqFRboi_G--ZEkjCTXRxLiRaZm9hGlZx9sfhR6aEfyATKqf-SOupg2drHG5oTRrOjg8GYXtQsTNTzdHD3bqvLxprdtUpkkDNd9qNAX-M0OtelPeri-rQcpTFD4rG4N5C0Ps5YLfou3BzvYyybBZF821O9zbSnr1_7GogANPX6Jjz5CktWGvsFKfaONLjlljAKZbaD8uWObqX93eZrw9PB9XlHadFT6N28AXHeKpPOY8Q4mzfjfuI1WyPVs1psRxGIcXr56IfnjLzJQ5sv0pRovwcoREG7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
محسن رضایی، دبیر شورای عالی امنیت ملی:
🇺🇸
🇮🇱
نتانیاهو به ترامپ گفته ایران رو 6 ماه محاصره کن، تسلیم میشن!
ترامپ بهش گفته اشتباه میکنیا، نتانیاهو هم گفته آقا تو 2-3 ماه تست کن، می‌گیره.
آمریکا به طور کامل از حمله نظامی ناامید شده و محاصره اقتصادی راه انداخته.
هدفشون هم اینه که یه عده معترض رو بریزن وسط خیابون تا اونا به F35های آمریکا کمک کنن.
محاصره و تحریم‌ اقتصادی آمریکا ادامه پیدا کنه، شرکت‌های آمریکایی منطقه رو می‌زنیم!
تا الان هیچ کاری با شرکت‌های آمریکایی نداشتیم و فقط پایگاه زدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70436" target="_blank">📅 23:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70435">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35614b49f.mp4?token=s2U_zMRiClT_XiKVwWrH7pEU6NgWd-oLxPmI-yWG6OCZT9Id0Ql6AWa4JQfjtx0CIkEyYoeHzznxVYGa6TBv3F6FKdmogNUUpxbq3Jw1tIDvHbhttQjCSFr5Op5xsEENcPoDGwvZYvoIA0zY7_MawpBsg7jzYDC55cAgwk_YLJiC6osSCqrKEVbKFOerr4e1kSYEHRQmHp2ZhI4GNhzjSIhDjeNaLoymEiAcKf5h9bk_W6KM6grom_Csc4M9hN_fGZjsUmzg6LUKti4CzbtUrbALEf32KUsHaaWbDXZkFHtSOaea46XxKHQ--QadXWFGMgk3FvyrUW4jPZ_vPbIq6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35614b49f.mp4?token=s2U_zMRiClT_XiKVwWrH7pEU6NgWd-oLxPmI-yWG6OCZT9Id0Ql6AWa4JQfjtx0CIkEyYoeHzznxVYGa6TBv3F6FKdmogNUUpxbq3Jw1tIDvHbhttQjCSFr5Op5xsEENcPoDGwvZYvoIA0zY7_MawpBsg7jzYDC55cAgwk_YLJiC6osSCqrKEVbKFOerr4e1kSYEHRQmHp2ZhI4GNhzjSIhDjeNaLoymEiAcKf5h9bk_W6KM6grom_Csc4M9hN_fGZjsUmzg6LUKti4CzbtUrbALEf32KUsHaaWbDXZkFHtSOaea46XxKHQ--QadXWFGMgk3FvyrUW4jPZ_vPbIq6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
فیلد مارشال محسن رضایی:
در رفتار دیپلماسی ایران قطعا اصلاحاتی انجام میشه و تکامل ها پشت سر هم صورت میگیره
تصور جهانیان از آمریکا به کشوری خوار و ذلیل تغییر کرده و ایران قدرتمند تر شده
ملت ۵ هزار ساله ایران با دولت ۲۵۰ ساله آمریکا داره رقابت میکنه
تصمیم رهبر انقلاب برای آمدن فرماندهان جدید نشونه جنگ متفاوت و غیرقابل پیش بینی از سوی ما هس
حتما شیوه جنگ رو تغییر خواهیم داد
دشمن روی تفرقه و اختلاف حساب باز کرده ولی وحدت ما کمتر از لانچر ها نیست
حماقت ترامپ باعث شده کل جهان خواستار دستیابی به سلاح هسته‌ای بشه
در جنگ جدید اقتصادی نیز به حساب اونا خواهیم رسید
ترامپ خالی بند است چندماهی هست اصلا حرفاشو گوش نمیدیم
وحدت بدون اطاعت از رهبر انقلاب ممکن نیست
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70435" target="_blank">📅 23:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70432">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0dsfEjcvcWFVMXw4vCQK2DJcdnjNvvXUP7Ts8wytIdfVL8qgWsQXUn2NLUfhUPFTxaQGRYLN4sU7HzhkyUeNQ_114FekN6ayzLbeIMOki_WD5VcW3qJw4SHRxhJKEZZZbTV37A261IMoceAHiOYavDUKyhUqotFoDG5G0e8rKFQS1Xkx92twCp5uNfgRCKm5avKbanVfBdJrhDH583t_i8YtqEYQqHFt0Mg8DjnUKfV8gv2xFvW9N1R8v-JshTIST-ti0Q5knp76ER7dfbhReVw9ciOxb8x3c82D0UlCWNOuucZAQqp2qwHoqOHVZAyJnInKRY90kOWVVAOg47pow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dI4oZqN0p0XZ4jl8UNc9qTiN_ohHZhm0LOgLYfFhYd4Ip3u5JFcZqSJpk4ztDs3znI6qsQ1phCWs9dmUuFFgGQOLjIAO6qE4bfn9W2nahYaZJC-2hXO-izMLQv-r7CxnMvSLPlB2NS_FYdSuzS1TkOrPaZYgdRz5NN92QznXs7VkzHbwJiRamuhO9V3vldxADdHr01MaJzi5YbJVGCq8rTmhbNtpLX4pR6bGt27nN7Z9Z6gbsSksCdaQDevcgVInAU7qg9Hihz6I5qAk73WZ6NzZ1MC1mg8jvrVNsqAi0C0i0SUxieSHqTLQ6WvUeFYmzkfDl3CKVmmG6nqi5ESkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KJ8rViFAzHTR3EvtVez1CP8DnUtRuWwOTzMLuL09e4NVhAGG_hNdxxTNaZlrYeemqza37am2QyMyEobOoft3BxAiXWW4q-ZhXIlhL1pSSiSC9rl3d-UULP5PG5dlk6uo3-xDUnixiq6zIQKmO_5iOaXw3fILe5e9LimIXZrArKScuYQs5HNOTn96I6sXztFT5Y82jMDq7CnH0dmE2aAoMd1CSNZfQKKOd-sdjNeQEQbvKXDOhOKKA0JV2gYIzqd4rfmwRKJ-6fqZhUTFuMHc-ZUQyP9Pejet75w3o5Ce3aCy58V0YHkpZAe2Aqc-NY4b_zE94X0H8GL7zj7MVVE3zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
جفت کنین؛ یه دختر به اسم نگین، سه بار به دوس پسرش خیانت کرده و پسره بخشیدتش.
اما بخاطر اینکه پسره با خاله و دختر خاله‌اش رفته بیرون تهدیدش کرده رو صورتت اسید می‌ریزم!
چند ساعت بعد دختره پیام داده که حتی اگه صورتت با اسید نابود بشه، بازم مال منی!
من پنج بار تریسام زدم اما تو وظیفته منو دوست داشته باشی!
فرداش رفیق دختره پیام داده که نگین مسته و با یه پسر به اسم امیر سکس کرده، اما خدا شاهده قلبش پیش توعه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70432" target="_blank">📅 23:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70431">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
گروهی موسیقی در جنوب ایران همراه با جمعیت، آهنگی سنتی به سبک بندری می‌خوانند و با افتخار نام رضا شاه را فریاد می‌زنند
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70431" target="_blank">📅 22:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70430">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toxu3Rm1WRzv0uv3H7R59q65tYiltbCbv8k7CUroEP6OSnuTkMoHlMKOPvi0FfaSfe94sdJyiexPrAzwr6FAycBBxXjkFwC9UW_sPrY7-_rZ-u9oGNZaf8GenPTTynXlEDj5y9227Y_J5QYEsO0ByZV6pUT7G8iVRgfaxwFbe8QTcV8umAe_7E8he8hvhnvarjf2TNUelfbFCCSx3dmMHraxQL057AuS_jDDAIDe-NUedNzhL8VPNHIhvR3nPdw5v2IWak3YkTrS4W3_GnvA93spRMtCJB_mQ8S1asPgrUoTqqrMrPTZEmKRLq1z8RuwR0S2t5mQzcWkI3XMKL1Qtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اینترنت یکی از استان‌های یمن رو قطع کرده
حالا خبرگزاری تسنیم اومده نوشته اقدام ضد انسانی :))))
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70430" target="_blank">📅 22:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70429">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b6fb2242.mp4?token=tMYR_AmH_-jkcmMwqlhUcep7_zXxOvzQaYShBoDlDjbFvnZ3v9fAMhtzbZY3RvLh_SfV20HKjFqhEzBwQHb07Rrym0Knse7c7Yeo2RyBxq_Mwf0VXFSyoGJKQbrT8GlqPz49qA9h28Fkd45xkGv4nEmK6kXZx_9Ygog_gxntkCeJGZjxE4KACQ_QHVJOuE6kNHb38jfH8CwuAy6HqGwB9lKCUTB7nqALgDiVo8Ou--hDfJ6XbDwvh6d9D2WJEhiHOcE2_otmn5ErCbn8W91e8lUp54KpQtVR8LY9LjpStbDaorTfFymkzTcj9_2jYm_W-Z614btdcuDYvK9mG2B85Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b6fb2242.mp4?token=tMYR_AmH_-jkcmMwqlhUcep7_zXxOvzQaYShBoDlDjbFvnZ3v9fAMhtzbZY3RvLh_SfV20HKjFqhEzBwQHb07Rrym0Knse7c7Yeo2RyBxq_Mwf0VXFSyoGJKQbrT8GlqPz49qA9h28Fkd45xkGv4nEmK6kXZx_9Ygog_gxntkCeJGZjxE4KACQ_QHVJOuE6kNHb38jfH8CwuAy6HqGwB9lKCUTB7nqALgDiVo8Ou--hDfJ6XbDwvh6d9D2WJEhiHOcE2_otmn5ErCbn8W91e8lUp54KpQtVR8LY9LjpStbDaorTfFymkzTcj9_2jYm_W-Z614btdcuDYvK9mG2B85Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه عده از مخالفای بی‌حجابی تو محمودآبادِ مازندران رفتن فرمانداری و علیه آدمای بی‌حجاب شکایت کردن؛
حالا فرمانده نیروی انتظامی محمودآباد هم با این سیس و خنده‌های ریز اومده بهشون قول داده که با بی‌حجابی تو محمودآباد برخورد می‌کنن تا یکم آرومشون کنه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70429" target="_blank">📅 21:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70428">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48faea4858.mp4?token=id4wu-5LDbgc9P4IshfyYmjv_95B6uipuCSlKh6mLaMnMk1Sg2FPWSxFSMeXQT-Qt-nPG-znJhSeW91orJW4TBklUVT_vjwjD-0Zt6b0KaOjJUzbo_htqSzAGvuTn-zO3WkspYiLyb5wdmVdzn9XjUKnWwyLeeWiuUzUoAY4lJcRCT-9hyaZMy2IVknHJtuQ7DNGz0LZ6OqBElbjalO7lXdvq69RJUYAC5mkTq21s0Bo6LoGEVofz3b_ZRWYeMdwz67TzzzFdyWs-QF3T5lGh8Gl3zcufNYsnvoGRcCQXot_t1z3vSQz7qKfxCmIPcvPsYAQqKwpFPb55prOjEoaGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48faea4858.mp4?token=id4wu-5LDbgc9P4IshfyYmjv_95B6uipuCSlKh6mLaMnMk1Sg2FPWSxFSMeXQT-Qt-nPG-znJhSeW91orJW4TBklUVT_vjwjD-0Zt6b0KaOjJUzbo_htqSzAGvuTn-zO3WkspYiLyb5wdmVdzn9XjUKnWwyLeeWiuUzUoAY4lJcRCT-9hyaZMy2IVknHJtuQ7DNGz0LZ6OqBElbjalO7lXdvq69RJUYAC5mkTq21s0Bo6LoGEVofz3b_ZRWYeMdwz67TzzzFdyWs-QF3T5lGh8Gl3zcufNYsnvoGRcCQXot_t1z3vSQz7qKfxCmIPcvPsYAQqKwpFPb55prOjEoaGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاید ماساژ هپی اندینگ به گوشتون خورده باشه، حالا چی هست؟
بعد از اینکه ماساژ صورت گرفت، آخر کار نواحی جنسی مشتری رو لمس میکنن و ماساژ میدن، تا ارضا بشه.
حالا با یکی از خانمایی که ماساژ هپی اندینگ انجام میده مصاحبه کردن!
میگه هفته‌ای ۵ نفرو ماساژ میدم و از هر نفر ۵ میلیون میگیرم!
یعنی با روزی ۱ ساعت کار در هفته به غیر از پنجشنبه و جمعه، ایشون ماهی ۱۰۰ میلیون درآمد داره!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70428" target="_blank">📅 20:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70427">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‼️
اخوندی که بی دلیل و بی اجازه از یک زن ایرانی عکس گرفت!
زن ایرانی شجاع بهش حمله کرد و چند تا مرد دیگه هم رفتن بزننش.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70427" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70426">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
⚽
@Tipster_Mafiaa
@Tipster_Mafiaa
⚽
@Tipster_Mafiaa
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70426" target="_blank">📅 20:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70425">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivUBTYQDZ88LcQFP1-6NF458VkX65B7J-p_rG2sFS-6SUzrYWAQjaWQ1NkQ4Yna1As-WnlvNHNLyD22hODVVC-fIidpxp5ggh83hke-9dC-DiRMGegJl-5_YMlvdpCwnnHm_9qmjviE2W3oqCXSNR2ilromoFCaGneTeKNfdcPueBpmze-9SzT7KDDAw7dNZGZYA8WJjrCYG7niBilvyAunXdvBnOx6u_Kn-v-NOfaHB9XPx49-PHK9d6O-xO4LEeZOKUgW5ez4Z1I71440q3DLfRr-TwSZdr_5H6CbTgTldhQrDkFX5ZKWABncpjtjRnKAYgdxxXuyyEczqrz51Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70425" target="_blank">📅 20:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70424">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89c9ecf73f.mp4?token=AH5EoFuGs5wixE9_D3K98sXOERVmOlXbyOMudwR1GdSo0Fbfsr1owBj4gQpmYpZoQe-VyAyIMppsUhK9-tniTSXEfww0huCW5L3sPx-rCrds2Wi3cQfcmVA8d4hvuoNUrcN0yWTs7amz0QOqMy3wWKLVS0-G8XTGndoKIB4BOUj6glnDPkVJaaYSr4Vbnr9tUEav-4uGubscfgCPG6SMUdYR82JngRgCOX8gZHuf3aGjs1qa7aZWFu2UKi2FD7yx8gE4BXnaSty8STOUhlFzoRzmY0R7h0pERkPziqXPDQew1u0BUnJ9fp1u2_fNHcv1pA4npE8ILAZMAxFfhjE-jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89c9ecf73f.mp4?token=AH5EoFuGs5wixE9_D3K98sXOERVmOlXbyOMudwR1GdSo0Fbfsr1owBj4gQpmYpZoQe-VyAyIMppsUhK9-tniTSXEfww0huCW5L3sPx-rCrds2Wi3cQfcmVA8d4hvuoNUrcN0yWTs7amz0QOqMy3wWKLVS0-G8XTGndoKIB4BOUj6glnDPkVJaaYSr4Vbnr9tUEav-4uGubscfgCPG6SMUdYR82JngRgCOX8gZHuf3aGjs1qa7aZWFu2UKi2FD7yx8gE4BXnaSty8STOUhlFzoRzmY0R7h0pERkPziqXPDQew1u0BUnJ9fp1u2_fNHcv1pA4npE8ILAZMAxFfhjE-jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
۴ سال پیش گفتید تحصیل تا کلاس ۸  مجانی میشه، به کجا رسید؟
❤️
محمدرضاشاه:
اون که مجانی شد هیچ، دبیرستان و دانشگاه هم مجانی کردیم
🎙
خبرنگار:
گفته بودید سال آینده درآمد سرانه به ۱۸۰۰ دلار میرسه..
❤️
محمدرضاشاه:
۲ ماه پیش رسید به ۲۲۰۰ دلار
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70424" target="_blank">📅 19:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70423">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tddO0U_-BeKKuALUFuchRUbZwKEdegwOrHHHFPBmL_RBxu7fTFvEgLRlMVYJ4MxG8wWBVi6Ali5SefsMX4ykBzMJ7_d0omu2tp7IgHJRIwm23tfGwX2v62VFnUKtyAj4uTG4Ot0uBmrLJHnayY77pHatD-ET0jU4mRF9GGXlcyivAgItmV_asG5nESn_ETjiM6nG29xoBwtR6f2AFVQnpDr9pEqqQbNjW_Z6ykTE3sVlx5vTCmuOdf8hnWzu6qWBvTCyyPL8dptfyxmvLljPCncupDEZs7oCi4rhVzYApSvqNl5t2gTPhEqkMQof_K8j5b97UB9U2lL8_J9cpKdqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
📰
اکسیوس به نقل از سه مقام آمریکایی:
شامگاه جمعه حدود ۴۰ نفتکش در هر دو جهت از طریق کانال آب‌عمیق جنوبی از تنگه هرمز عبور کردند.
در طول شب، حدود ۱۶ میلیون بشکه نفت از طریق این مسیر جنوبی از تنگه خارج شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70423" target="_blank">📅 19:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70422">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193d1b1501.mp4?token=TeCDx1c7TDZaRbaPgVNFHVBGsAHip_vo9UdhqvThxfGEBPYYOe1Qe1CRpwrlDhtZAsi-vQ3TDDB7UuRcqZQV_yZYyzdxMOi80QJ9Tcn-T0D__It7KZIjHNxbX7aBe7wveDSaRzYH5oMDtdUbi4SWGb_Z-EIpaPIRYb8QqOjRCFSiMsmpJduMDhhAiS2f-xZyD5w81XQXumt1Rd3xzH8V26Odi2HXT-3_i0bFGkCZ823rqU8fYzH1J0qnDr8qfiIHvB5mOdVFDupCdtgqinUk_TwG6va5wz_8fzG3pPcbxzV6ateJVDlJA1PP_POPDoq9jcLgWFvnK445s4_EXVdABIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193d1b1501.mp4?token=TeCDx1c7TDZaRbaPgVNFHVBGsAHip_vo9UdhqvThxfGEBPYYOe1Qe1CRpwrlDhtZAsi-vQ3TDDB7UuRcqZQV_yZYyzdxMOi80QJ9Tcn-T0D__It7KZIjHNxbX7aBe7wveDSaRzYH5oMDtdUbi4SWGb_Z-EIpaPIRYb8QqOjRCFSiMsmpJduMDhhAiS2f-xZyD5w81XQXumt1Rd3xzH8V26Odi2HXT-3_i0bFGkCZ823rqU8fYzH1J0qnDr8qfiIHvB5mOdVFDupCdtgqinUk_TwG6va5wz_8fzG3pPcbxzV6ateJVDlJA1PP_POPDoq9jcLgWFvnK445s4_EXVdABIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
علی عبداللهی، از یک کارخانه تولید موشک‌های بالستیک زیرزمینی بازدید کرد تا از آخرین پیشرفت‌های مربوط به تسلیحات بومی مطلع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70422" target="_blank">📅 18:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70421">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e0051dae.mp4?token=Di0hOOzwrNSY23FuKILoj_nielQiFjCitTkuI1T0hJ9DdnXdAC6eiIwsFX6n075WjS82nCBqr5ROMfrckh82afvtnK8pGcsEqfihEUwhC8Jbqjl9HvGadBfv2dqzZraVdBywPWgCcbUbbTdGLtNqdhlLiMBGaQg6rswAY2Wwct93EjWjmiNxbfeYDf0lwMvm8OGxlnX3RUICpXonQXZBRzhamJKGwHMVR-mLjm_X45FhBOyM_UZ0r6vIT_72VKJujzfEvi8zmlcaJzf_Dbmv7zJyKH9AQS12OYcyPzv813xcMXBxTqRjXnR-l8TSlNBKM_1wyvP8cFYpjPPydJE--g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e0051dae.mp4?token=Di0hOOzwrNSY23FuKILoj_nielQiFjCitTkuI1T0hJ9DdnXdAC6eiIwsFX6n075WjS82nCBqr5ROMfrckh82afvtnK8pGcsEqfihEUwhC8Jbqjl9HvGadBfv2dqzZraVdBywPWgCcbUbbTdGLtNqdhlLiMBGaQg6rswAY2Wwct93EjWjmiNxbfeYDf0lwMvm8OGxlnX3RUICpXonQXZBRzhamJKGwHMVR-mLjm_X45FhBOyM_UZ0r6vIT_72VKJujzfEvi8zmlcaJzf_Dbmv7zJyKH9AQS12OYcyPzv813xcMXBxTqRjXnR-l8TSlNBKM_1wyvP8cFYpjPPydJE--g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
📰
فاکس‌نیوز:در حالی که دولت ترامپ آماده می‌شود تا موج جدیدی از فشارهای اقتصادی را بر تهران اعمال کند، او می‌گوید که ایران در حال تغییر موضع و نرم شدن است.
ترامپ می‌گوید: «آن‌ها اکنون دارند کوتاه می‌آیند، چرا که وقتی کشوری دیگر نیروی دریایی و نیروی هوایی ندارد، حرف زیادی برای گفتن باقی نمی‌ماند.» او می‌افزاید که بسیاری از رهبران ایران کنار رفته‌اند و «اصلاً نمی‌دانم باید با چه کسی سروکار داشته باشم.»
این اظهارات در حالی بیان می‌شود که ایران سیگنال‌های متناقضی ارسال می‌کند: رئیس‌جمهور مسعود پزشکیان می‌گوید شاید زمان آن رسیده باشد که «همین امروز به جنگ پایان دهیم»، در حالی که رئیس مجلس ایران لحنی بسیار سرسختانه‌تر و تقابلی در قبال ایالات متحده در پیش گرفته است.
اکنون فشارها شدت می‌گیرد: انتظار می‌رود اسکات بسنت، وزیر خزانه‌داری، روز دوشنبه تحریم‌های جدیدی را با هدف انزوای بیشتر ایران اعلام کند؛ تحریم‌هایی که روابط ایران با روسیه و چین، چالش عمده‌ای در مسیر آن‌ها محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70421" target="_blank">📅 17:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70420">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7d3e5c370.mp4?token=QLE6E3RBuNrBgvVhh1hgYzDKFRg4Kin4uCXgJiu1OPt4lHU8CmM6YHbPydG94QO0MBR-r1_zFfMa77qiuviYbfk_yJeElGXLtdugi4Pyk5546QEmLrjaMO7gZKC7VQEHXRovg38qcUAEtwWdduA56m6mQyyfsMxpxylZgqWC4FJrHqXMfisk5cSZtinn8dP7-9WJVJzGep7meX8bqeCR08HTIeN104CKwXfNSivKX_-N1TNd2OVV88-vY3297b9eab6061-uUwrLmxKqCLwt3i7ThDlGVnTCwmBeUJbALFpD6ta7TVqqx4TTqx6u_0rqBb_Es9vSURCD9oK32FVbL35t5QPV3gKKsJuxdrn35Q2XMx855qTEq6TbXFiixQaGLHuqIZLXZrNxzubg6Me2mdStfNuI99ihJs7GyQ_6VJC7X2XkpX2xQkp41-tpzxl2IfhFtU351nqKRVKImIn76teHq_vESdb_N2fh8RHrZUXOW4k5INqrXW8fmCwzbgB1BGHxXqww9C9bMOYeU4U7nhcvnVLMwfy_he_jCshHLX1PLF5hWaf9W-KSo6sMqtp28LGx-29a0nYy4DYazy_aSOJcydzcvESQhiUOg76QLaP6FW8qVlcpSUsec05MQQVb5J4P9JpC1tgz47lzo-EarOyIAaSq3QRbDRcUkgPVB8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7d3e5c370.mp4?token=QLE6E3RBuNrBgvVhh1hgYzDKFRg4Kin4uCXgJiu1OPt4lHU8CmM6YHbPydG94QO0MBR-r1_zFfMa77qiuviYbfk_yJeElGXLtdugi4Pyk5546QEmLrjaMO7gZKC7VQEHXRovg38qcUAEtwWdduA56m6mQyyfsMxpxylZgqWC4FJrHqXMfisk5cSZtinn8dP7-9WJVJzGep7meX8bqeCR08HTIeN104CKwXfNSivKX_-N1TNd2OVV88-vY3297b9eab6061-uUwrLmxKqCLwt3i7ThDlGVnTCwmBeUJbALFpD6ta7TVqqx4TTqx6u_0rqBb_Es9vSURCD9oK32FVbL35t5QPV3gKKsJuxdrn35Q2XMx855qTEq6TbXFiixQaGLHuqIZLXZrNxzubg6Me2mdStfNuI99ihJs7GyQ_6VJC7X2XkpX2xQkp41-tpzxl2IfhFtU351nqKRVKImIn76teHq_vESdb_N2fh8RHrZUXOW4k5INqrXW8fmCwzbgB1BGHxXqww9C9bMOYeU4U7nhcvnVLMwfy_he_jCshHLX1PLF5hWaf9W-KSo6sMqtp28LGx-29a0nYy4DYazy_aSOJcydzcvESQhiUOg76QLaP6FW8qVlcpSUsec05MQQVb5J4P9JpC1tgz47lzo-EarOyIAaSq3QRbDRcUkgPVB8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این مرد ۴۱ ساله درحالتی که مشروب خورده بود درحال رانندگی بود که پلیس گرفتش
:
از ماشین پیادش کردن میبینن دکمه های شلوارش بازه و یه دختر بچه روی صندلی شاگرد نشسته
۵ تا دختربچه خیلی کم سن و سال هم روی صندلی عقب نشستن ، پلیس بهش میگه اینا کین ، میگه اینا دوستامن
درضمن یکی از اون بچه ها هم حامله بوده
در نهایت این شخص به دلیل سواستفاده جنسی از کودکان ۳۶ سال حبس میگیره.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70420" target="_blank">📅 17:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70419">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/357928b911.mp4?token=M-2c8Bcb_tzF3ylFkoMXxOLR5VTwmnUEE_oNy4Q4Fwbg645Om8JufdMKoeyEUzELgG7uQHd5azdJA6YLHUcZiIdKUeWPAlingKRnx79jdbeNSendpj_HGZTPrKzfVJl0EVE5T006Lp_0UqTqAP_WWkml7YNsEIT4UbdB_K39HZrZjr-jdGNHbOzEiQ9mQUNMw6u8ObT_WjUE5hZDWypILHfDIu01FE1jsYu9mhpRU-xnPWqOO8cDHKmYoHPNZcSZ6haPzFIseVNnBcqXKxLOdXJ3m4gXR0Qqy5nrZSV0j23HZJXRen9nWBFNmJqg-z7j3P3aibnf3unyEVeQ-ZnqSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/357928b911.mp4?token=M-2c8Bcb_tzF3ylFkoMXxOLR5VTwmnUEE_oNy4Q4Fwbg645Om8JufdMKoeyEUzELgG7uQHd5azdJA6YLHUcZiIdKUeWPAlingKRnx79jdbeNSendpj_HGZTPrKzfVJl0EVE5T006Lp_0UqTqAP_WWkml7YNsEIT4UbdB_K39HZrZjr-jdGNHbOzEiQ9mQUNMw6u8ObT_WjUE5hZDWypILHfDIu01FE1jsYu9mhpRU-xnPWqOO8cDHKmYoHPNZcSZ6haPzFIseVNnBcqXKxLOdXJ3m4gXR0Qqy5nrZSV0j23HZJXRen9nWBFNmJqg-z7j3P3aibnf3unyEVeQ-ZnqSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دخترا :
خیلی برای کنکور استرس دارم کل بدنم داره میلرزه .
پسرا به روایت تصویر :
خیلی استرس داشتم که چجوری کیکم رو بخورم که تا آخر امتحان کیکه تموم نشه ، که نفر جلوییم بهم کیکشو داد و کل استرسم رفع شد ، دمش گرم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70419" target="_blank">📅 17:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70418">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c46390cc4.mp4?token=IMbhWxkZW0-EZ1lyQp5l6WKwdramoTfA9GsbbrVPnVu_F8K22ewTEm0uEiUbx6NC2gR-kz41g0eX2QgmXO1JsyWOB80r3j3zUl7f59moFQhd0Guu1urNYJJFsESVWU9mxvj3G-6v30bCtw2NJ3lZi2rHWui869hPphbrR-mDJ7cdOxVBGYoKBHjXibegFXHeY2cjhISILhgXqTIO6Tmr3nwzf5KW4y5bzQlGO_7-QIQ2EyEAWKEBZX3i5UeB2LYmBOBvg2ZuSfu1tDYDX1dST_wJ5Ih8YJkX1-y3tiCANlj7kHq5mBRQ6UbUNYrzkVMZ93mQHmlxe8OUYMOCJrqMKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c46390cc4.mp4?token=IMbhWxkZW0-EZ1lyQp5l6WKwdramoTfA9GsbbrVPnVu_F8K22ewTEm0uEiUbx6NC2gR-kz41g0eX2QgmXO1JsyWOB80r3j3zUl7f59moFQhd0Guu1urNYJJFsESVWU9mxvj3G-6v30bCtw2NJ3lZi2rHWui869hPphbrR-mDJ7cdOxVBGYoKBHjXibegFXHeY2cjhISILhgXqTIO6Tmr3nwzf5KW4y5bzQlGO_7-QIQ2EyEAWKEBZX3i5UeB2LYmBOBvg2ZuSfu1tDYDX1dST_wJ5Ih8YJkX1-y3tiCANlj7kHq5mBRQ6UbUNYrzkVMZ93mQHmlxe8OUYMOCJrqMKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
قالیباف خطاب به رسایی:
حضورت اینجا خلاف پروتکل هاست
ولی بخاطر عمامه ات ایرادی نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70418" target="_blank">📅 16:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70417">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e1045a89.mp4?token=PG9TA6f0gVjzzoxkSvN17RmNc1eqtILkJ4Wp7TR-KzPuO2rmG9x069oDeI0ZmD04LGCiGDTlTHcxCHxV4x8wlEkh4-r16B-kR6vQTy940CpCSdvaH0vaL80AjYiZ3aflYKCIwtbqObtOeXjwr3qsnBiXQa4N_6XwboG9Yu7C16qP2v85nyWfktodmaRdtseUmESUHMf4UwzPEPvqEPWm75RX1c4577H26B_WHAmDBxnE4eN7cfJXka7BgI42g0mFw9bn6b-ha1fz_uS2MQY9SeHW74BVV0173cQMIRRt3np-A6aM2au6IX2WM0qa_tKHcAo59IZP2GA2JmlI5XWvrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e1045a89.mp4?token=PG9TA6f0gVjzzoxkSvN17RmNc1eqtILkJ4Wp7TR-KzPuO2rmG9x069oDeI0ZmD04LGCiGDTlTHcxCHxV4x8wlEkh4-r16B-kR6vQTy940CpCSdvaH0vaL80AjYiZ3aflYKCIwtbqObtOeXjwr3qsnBiXQa4N_6XwboG9Yu7C16qP2v85nyWfktodmaRdtseUmESUHMf4UwzPEPvqEPWm75RX1c4577H26B_WHAmDBxnE4eN7cfJXka7BgI42g0mFw9bn6b-ha1fz_uS2MQY9SeHW74BVV0173cQMIRRt3np-A6aM2au6IX2WM0qa_tKHcAo59IZP2GA2JmlI5XWvrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
#تاریخی
؛در این ویدیو، به بررسی نبرد حرّان میان امپراتوری اشکانی ایران و روم به فرماندهی کراسوس می‌پردازد.
کراسوس که برای کسب ثروت و شهرت به ایران حمله کرده بود، با ۴۰ هزار سرباز رومی در برابر ۸ هزار سوارکار و ۱۰۰۰ سواره‌نظام ایرانی قرار گرفت.
ایرانیان با استفاده از تاکتیک تیراندازی از روی اسب به سمت عقب، پشتیبانی بی‌نظیر ۱۰۰۰ شتر حامل تیر برای تامین مهمات و ورود سواره‌نظام که ۱۴۰۰ سال از تکنولوژی نظامی اروپا جلوتر بودند، توانستند ارتش روم را به‌طور کامل در هم بکوبند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70417" target="_blank">📅 16:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70416">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpnE_mcfw3WXUdAfVrvFaTKr2dc1iLrfgtlQEZywvSnPSXYCHS2fHF_vyb2c14kp2hxRtTHSA9f_dHdn_4UyTwQd0Sgjx4lvimMjBI2jPxytJI9Lue84JK4BJqhznUI8nP2-JbFNkpyayK7zkV8CE9ftPsXNDMt8tvLLQh2SkAeCE1rghcKxtdrd1-0TXzbXVGtSSnPZ8o5LaqGWzmagfoEudP_B5isz4rJULVeqtdPxh4H6h9BFy4QlNIh-kxe3GxmvUry6JGEWXIG2rpB7Ua372MV5cX4f5aTIbqksf-x38aH75PyPdU_Pw6dOeqr6hhFKtLVLUuY6pMvMd91sfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یه خانم رفته لیزر و خجالت می‌کشیده که اپراتور زن باشه، گفته یه اپراتور مرد بیارید صیغه بخونیم‌بعدش منو لیزر کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70416" target="_blank">📅 15:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70415">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
قالیباف:
ما پیام‌های متعددی از کشورهای همسایه درباره
شکل‌دهی به ترتیبات امنیتی و همکاری‌های اقتصادی جدید در منطقه
دریافت کرده‌ایم.
ایالات متحده امنیت تک‌تک متحدانش را با قلدری و بی‌اعتنایی مطلق به منافع آن‌ها به‌خاطر منافع اسرائیل چنان به خطر انداخت که آن‌ها برای لحظه‌ای، تمام هستی خود را در خطر دیدند.
یک نظم بومی و مستقل که واقعاً صلح و امنیت را در منطقه به ارمغان خواهد آورد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70415" target="_blank">📅 14:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70414">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szRvBYYbVhzvqY-bsGuLvzPw_94QlNmwVrB5ng-FHy9xEkOxKdTRt96nAlury8IiQl3b2-jYuvx9IZ85FMP2IXgldYxFAUk3QgLxrHT60gTrt4L5Qpoy8cQDdYxHDT03zo3utIEWZ3S7iOAsDJFgcL5ubQNG-xNPM3TqZqNnHXnbE0AVYDTKTRQD-SOzD5Umbu-wbrZkFDth1sil-f2C2ylVrr-LuIQrYKsJK1CX1_ICL59Vcy5vzqq2YyhaAmG7uybfEHzOsdkEgUicqcd4kC6HfFSTmHsU3NmiQO7Y9z9gGp6rBP894YQI3CkHZ7ONIYcLPIAguquD849_RKKEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تصویری وایرال شده از پزشکیان:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70414" target="_blank">📅 14:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70413">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df1159d44f.mp4?token=Osb9udNGIU6SP888CsSyuZC7m7mfWMPmHyrgv7unvsf3iEmPeNHV4-w658HYDEZ0lihauy4xn_CXwyWxsoUJVpVgKja4ndlhhr5cs8blA4d2FTOT0M5y_uDw3Slas0jKRKyxi7lDbUcoHE5y2c0CH5AFAOQfqPLJHrFd04LyUqitva8m40Q9UJTzu4AdWPMuY4In0bp178NJNGZXELaAFD69d9aTTr8FyUPY_TsldfmFfOhpSpIw5mi0SiIALz2Z-1LJZ1HJLAi77kQDMM9DYIyEpbJm4CoJjDBKfXY5JQiuOcClEbvr8NcqH9XXXYkXUbViL33458LYMGGkmCoZyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df1159d44f.mp4?token=Osb9udNGIU6SP888CsSyuZC7m7mfWMPmHyrgv7unvsf3iEmPeNHV4-w658HYDEZ0lihauy4xn_CXwyWxsoUJVpVgKja4ndlhhr5cs8blA4d2FTOT0M5y_uDw3Slas0jKRKyxi7lDbUcoHE5y2c0CH5AFAOQfqPLJHrFd04LyUqitva8m40Q9UJTzu4AdWPMuY4In0bp178NJNGZXELaAFD69d9aTTr8FyUPY_TsldfmFfOhpSpIw5mi0SiIALz2Z-1LJZ1HJLAi77kQDMM9DYIyEpbJm4CoJjDBKfXY5JQiuOcClEbvr8NcqH9XXXYkXUbViL33458LYMGGkmCoZyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:وقتم خیلی خالیه باید چیکار کنم؟
خب الان من چیکار کنم؟ نظرتون چیه برگردم و دوباره ایران رو بیشتر بمباران کنم؟
جمعیت حاضر: آرررررررره!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70413" target="_blank">📅 13:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70412">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmAUaHMYs_mJBAiZF2oEhnoRAdOLl8xTD2riqzfz2NDNpD_ZoxXcSibWeVcvqJXJVrFtboK8gT49WcVZ7Z1Jz1ImFX7s1CYwif7DtNCci1k0oAsQVhHcTFMLN8YIQMhS_FtQ0glfdxDdAQaq_eCY7LVRcpCdSdg96XYHRW5HQvRfY0BkV1RxZ8woe2BndP0Na8QObGFW53FEEmwtQIAFAC174Si_zxRldtiCXSIRu1rlu7UYRpUF-2rE1faap6v5jn3zOr39KC3qW-NEFkK95wbeOwjSYxglIazohLluMIpsPmH-XrcAr2ETWCpekS1Dex8StrA7Htt68wDUfkQVRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
باقرزاده: اوضاع جسمی خلبانان ایرانی در قطر خوب نیست
فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح با اشاره به وضعیت جسمانی نامناسب برخی اسرای ایرانی در قطر، خواستار اعزام یک دستگاه آمبولانس هوایی از سوی کمیته بین‌المللی صلیب سرخ برای انتقال هرچه سریع‌تر اسرای مجروح و بیمار به ایران شد.
وی با بیان اینکه محل نگهداری اسرا بر روی آب، شرایط مناسبی برای حفظ سلامت آنان ندارد، از دولت قطر خواست اسرای ایرانی را دراسرع‌وقت به خشکی و یک بیمارستان مجهز منتقل کند.
باقرزاده از دولت کویت نیز خواست با استناد به کنوانسیون‌های چهارگانه ژنو، حقوق اسرای جنگی را رعایت کرده و زمینه برقراری ارتباط اولیه آنان با خانواده‌هایشان را فراهم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70412" target="_blank">📅 13:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70411">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTm_xS0S0qrJcJ3iWQMZeGv8VJkWvh24CN4FYs5hn4elgdhdVJp6Yo-d1As_3QAsljS7OGH4bUrMKqpDgT-G_nsW1ZpSm0IpeLb6xk6FvbRuj0440uKHdSZbWqXV6Gb_Y2r2fRrCBkxix2Hr117JzQ7dDJb-7I9naExA8b5CNUzBa2yc29NRDjzOiKKJLCR7nEsCNsPYEeZxYpEHFi83EDwO7a5b8_ECO_VDgHxFjauHTOWN0BdB7G0bWPh-amCfwkhT4MBYgHCT3NgpxyX6wVAP1r6ibFJQrjPYk0F3sJ2tr3FN6uC92-enzCY6uspzEVMn2vt21DbFv0_iyc1VnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇪
یک تانکر نفتی متعلق به شرکت "ادنوک" امارات، با موفقیت از تنگه هرمز عبور کرد. این تانکر، شب گذشته، از مسیر تعیین‌شده توسط آمریکا عبور کرد و توسط جنگنده‌های آمریکایی اسکورت می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70411" target="_blank">📅 12:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70402">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQ54EaVHupOiWbPsL5xirtcK5PlOBJE9lpgGlCPjWO3nfLrjD9x7BeDz6nDqpHm7nGGtY7r1RbvGlyajyXuUcg8tWcdhqznyGkWCzHeGZo8RMeAgRuTyt7OEoIS7T_u7yhkdyx4Y-X6f7tJHPAz0TqpKhErq4hYdbXoandqnbivtrHK74MBD4JWO97iD46CsZ-Lnx45D3fIaUnR315nz-qzRsXGMiwNJrYp4pnvBLVSz54OAw9kGXPcBvznT2l0RqZQfEMgaJDdkBnIupQ31AdIjeka20-eBSp8x_39fk7BczSzLQJXon6wDMRhkiCwB0RkPK0g0RALRJLg7JEDR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d67kFCqzfufh0dMqPfRCRN_ufSoVxKdWGe31CKpAl_nfSNhZRhLeJmTwOsRk9gUp3tpSlB3PPEK0xAHYSICjX--tgkkfS7mFwQSMcDOmb1EB3ymxi0vElb_B4Lc_ZOFjBmGHqsps1yU7qbd6HbrlQaXcdMXexr4SE12o5jFa8ZaphOAnXGZV4CclKB4OE_FGEWFbXKgJjahZkF1-fvbIsTc6GnVshkl64c6KhKgJqliaamc57IF3otmMmOWEzMcDRFDnRZIT6KEP7UFPoR07irALyKXWW965ZibgiVPjn0ewzkOdP-vYnvVARelWwvWQQHYsn1i9ZEoKfkREzpLsBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DX_81D-XklmT4Jc0DsPupchCMVUGEZzB8aR_fxQKGRFk-M7fF9Bx2YXObpYmQWZwsm1cBixJRO76Bz8wqT7VhERqcekMgruzycNABXpqZW-_bav2zTCd-57oRdmwVPGSNuNZJWiR3hE8O9LmUb2mtVldat0B2Y5TLin1Uszjp-zr2v941xleuozB19f7_0xHdcR2uPr1TFLAv1o7Cege40X0NhfDgz_JEdcalccVO8jX44MQJh8nsO3HL2Rmg-7aA3USh3y601ij13ns--MRlfuINpYxbTRajReQ4vS5rRLbK_encRS3WJzrk5gcEjbbLiONFRq9Lt540p6ytb5EAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/izJ_BuuiQrBxwtAgi28iXnsTAlQ7NeSOxnNrnLBIf0qvJoFTz6ln9T9azqQonUcB5iIyt8rJY5oDJcd26NSw6K4lY2NSIiY3lHf7ywxn25MxBOxTkj2BWcedfF660zkKmwfALuW-j08C9lPiHE1v2H8KFz8Y6bC8sehrdPEPF-sAVb3KCJHB3SkiZ3tkWfTCkaVR8DfS9Re7pCsCWNCLE1cYbT9cj5JZeNOZ7q4IEarJG3JjQRRZ2pzxZZOL-Ya-Cdp4rDvWTBZ2bWArZLY-TeGOT3Tnsr_rsVoyfueBE-TcF81AmNYTqI8rFb0gPC_GecFk0F7hG1q84hCCM6t_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNfEm5tUt8W4HXG1w4PR9rvcgEUxOfubHRfgFpMIRgmpwlI3ps85CZWscsQ9k63sH0HjtK9nCmJDelr2xPoCtTg53Wh1Gihwv8kaU8hbJw3l-ak91KwMqWKq1m-fmTHL1L8HunkQLvK_Blvq7A28cpquqzFIX4v-jaIhyEdkLJxpdH-mQb2rO8HYnmpCRXzlJ7VIENDRCz7ojvbDFaYJm6qXtewfeiPNly2nCHjofwCPV3dH_3EPxFGWU6B8Fk0SQTer4ua2EO-B5h-k-qBmDfW1jNjDD1MXnb2lcoiqR9lO1lJ7JhxHeFHHdLdd1nnu1tBNlIZXaw9AaDLaIjMBPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YJQzC1lHr1kYBuUOQ4nSbsstQhbxH1MuJP5_-ZuPbyziFtXPv00TWAxzXmro377urZc7HvAGHM1t2fndSwrHT5vi81R2Frr6_upWc_jaFa58VhzM_ttqYsYXiCjP17D5K7nyojBe1-4EEAL9AgEOs-Qk2YXdN_tFd7cjavPGtYGvZRBB8mVWk5GdkP2rfJ8hfDnKlojGAB-ZCE1YOR7gsLHIzMr2z_LdR7jWzObaGj9qmF8NXiAKNb-_bgDr0HI0HMuBd6Qct17kPw49bL0E_VFxQdczrCC5_IcqmkSLilKgoqBszHqsWnb7YcJ5YHeCJZ1VWXgDMSKtdhxoiOUe_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3DkAXWW39x1agjiMId3f5CJQfNIXFc8Mgq2ts90ebIsrvpACHMHkRpIPsv0aXJyWnFAbIcLGXoE2Ap-4Rkko31_0VwDoBBhDIMzNnkJvCQfpNfbzjZmU9hxdwIwPotArP_4yAm1hXhD7MEtR2C7VB2UxE8zeW4Nzix58jZAo-l4Bp12eeGH2bx8bZ0wjZ_Hdfg7PwHRv--3f6pjYncR4MB4fo3G7OCmRV7DMSB6TrT78dquv_DLvE7mDu5EeN0sSuyw40K6ILDqKFXGNOhaKq_hSTl3bZ4nhXKqWtjZ1lJeTdbHOwf3wAXtMaDsHBOk1APJ6P-U7MLM61zN03WNeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGi9lsnEvGv3NjOVYjz3WWiIwo49s7W1KyhvI73H70DSZOHFRyKBjJssH0AgllaScmtNB0Vyu0RjsxmxGoLbZRp7BdQqGGilFrlSmrHeYeY-jodSp1i4VEKm71rcgReLLCJEdlwsaSfcdUFDnMyGWYR00c4yCbAG6Lc0vxxoiFGMIXnu-R5BgKjxYc-H76qDUKAOPxV5TiuEph7wGVmYXo6grFt2ngVgzFU-HX81Djq06AM1bswFKZ9l3QsrcGjP2We28rPp6jrAuFcdqeJu-xlwY7OZuwWolcKCXijFTP3ToqlNVwibhwh3DMtr-gcQdJL2gvIdwAgWodR5pisCrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ceIKpSitHX9eBx5wrqKFZfcyQRVsCXKFT-wfFldt7qMKYXtWvdoN0OS2cNz7tQMWc377x_KlhtCWxdDignfnQCs-n1ZzYG4IjUbUyO9YKUjIh-DPYr5m21lK_ZIsKC-CpWCKYbmKR5fLilJYJWbFN-3Pl5qPZogvGQZfrJULANcioa09zNRKMUAxBofoZY69Glr7-MCquAvjWtAgWchicOo6NFfaX6F5eRMPex0yBC0QG1pfaNa0mgHP7pACyMghApo7JbsKgcV62KbejgM3aHDJbKgAC53u1-GtOS_TfgPzQmVI95c_-aLwqe3mqGZciXDhW35r7aN6mQZi6C_bQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حملات سنگین اوکراین به پالایشگاه‌های نفت چاپایفسک و نووکویبیشفسک روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70402" target="_blank">📅 12:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70401">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70401" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/70401" target="_blank">📅 12:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70400">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARWFTI-n84gzDQiuTU14Ae3hzOFF5bwptT_YIBungwlaC76MZJB7D-FlAfJVDUOWBtiqpyM1I3T1dkEZuhZqTudFAliPs2uJtZtuivHCwXmcrK0pMCp-t6FQXjH9tQodORNpdgEeQEmbIM8j54vUpId-eXhiL9M0_X6Uk6LurGBJX0c4wbSMDZInyHgeMQcwYRAaXcJlgqMaZKKMkZR8r2NcJsAw_LdA2lK3cGXKW4h7F7SLYTAUcEUO3jJH7g0LdYNPUsvv64gBDeFHYvgBeRKunr958OF4xNHY9S8OQTipOOnX-pzvH4NljlsDdvUF5TvrBLRoP1wkum4uUdCS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a31
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/70400" target="_blank">📅 12:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70399">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163f624c09.mp4?token=sS6QCjkNclMpa5NQjQx-hDyXxBHi6SapVHNtppH0hCunyd9MzfQbhfAbrS4dzdPQtiXOS8hoU-2J6UMUgmp8TZmD99X2naTqnOo_STS3ZqRXBHri0el75ZgA8bZ7dCzKkmg4fGNvlmo3jwAvOzOrEMjRU9U7mysa3rsRjwnMb0zWViWMqQWAcsbSrfHMYNmOUFQiN1lXMaLfhf6tTXY2Fvzznq10FwrN9EdWj0eYgjaNghxt27ZdL4DQH-98Rfk_rwhhe2dK8dVVsNfHylAywEF0MgAwnX-6cwv8CIapYON9iY36ZnU52DTQwdn2F7x5A-bwfasXwDEOyE02cCl5_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163f624c09.mp4?token=sS6QCjkNclMpa5NQjQx-hDyXxBHi6SapVHNtppH0hCunyd9MzfQbhfAbrS4dzdPQtiXOS8hoU-2J6UMUgmp8TZmD99X2naTqnOo_STS3ZqRXBHri0el75ZgA8bZ7dCzKkmg4fGNvlmo3jwAvOzOrEMjRU9U7mysa3rsRjwnMb0zWViWMqQWAcsbSrfHMYNmOUFQiN1lXMaLfhf6tTXY2Fvzznq10FwrN9EdWj0eYgjaNghxt27ZdL4DQH-98Rfk_rwhhe2dK8dVVsNfHylAywEF0MgAwnX-6cwv8CIapYON9iY36ZnU52DTQwdn2F7x5A-bwfasXwDEOyE02cCl5_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
توی فرشته تهران، یه مازراتی بجای اینکه ترمز بگیره، گاز داد و این شکلی خودشو ده‌ها میلیارد پولو بگا داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70399" target="_blank">📅 12:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70397">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWhqloQNj_xtUyJW50kaBqse8oJvYspockbOfenF_ua4Rh-vb9bL8JLMO1LjfDw_R5ygr0tf6aSDvLGJtBfKh2-sDb84Iqu5AonXBZjUzt7yqDZGuQ9YrJ8uG2I54aNddt63xFKT9-nDsJd0DPWyqf8z529paN1lxI3lIvFRSdQZf_mVisM5Z9dLFwXpQFGu2P0JRSEdQek3SFD2gyGpb1OTEMt05rCIyNR-r4nCMS8yq3llkgOkfjdz8JFqCtT12YwS7XwpwBxS59DOBCBTW6kT7yb4pr752CEn33EITmBLVY7WgblaB62GL_Y--a34pYoGXVUn_doUY95Zp_X5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d025747579.mp4?token=mHWUFYJANiCv_HXDpl4-1EVNAgSyuTCcHr4ugqSAqz2A7aQ-FUsGYUgoqnFTkxblRsIENP269c1Tjq0_yAH0M0jc7aLbPmuSPY7a87sMcdlUduPpUcD2jFEeu8jGQCeYp3IwIdydmsEiRIzzW8dcBW_5RnXTY0OkTBeRTtVZpi0mWwjQinT5jYftxjYt-2KzOrP1hiFjzUdXWxCbK-kjDMjZl6S0MPUW8ewVC5nCYdMKM3yFZ0jhM8NgUBtPwi8DLOMWKtXAQebSFxESc65iBEnps4WcXZqxq7K7HNcozJCmdqqkyiSf3JIuhy_Jufe4uPUn914-5XZ80ol7T56L5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d025747579.mp4?token=mHWUFYJANiCv_HXDpl4-1EVNAgSyuTCcHr4ugqSAqz2A7aQ-FUsGYUgoqnFTkxblRsIENP269c1Tjq0_yAH0M0jc7aLbPmuSPY7a87sMcdlUduPpUcD2jFEeu8jGQCeYp3IwIdydmsEiRIzzW8dcBW_5RnXTY0OkTBeRTtVZpi0mWwjQinT5jYftxjYt-2KzOrP1hiFjzUdXWxCbK-kjDMjZl6S0MPUW8ewVC5nCYdMKM3yFZ0jhM8NgUBtPwi8DLOMWKtXAQebSFxESc65iBEnps4WcXZqxq7K7HNcozJCmdqqkyiSf3JIuhy_Jufe4uPUn914-5XZ80ol7T56L5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خواهر پژمان جمشیدی :
برادرِ من امام‌زاده نیست!
مثل بقیه جوون‌ها، عشق و حال کرده و همه‌کار میکنه، نوش جونش چون شهرت و ثروت داره.
ولی وصله تجاوز به داداشم نمی‌چسبه چون اصلا نیازی نداره‌
ترانه علیدوستی؟
یه بار با یه کارگران بوده که زنِ طرف فهمیده.
یه بار با یه بازیگره بوده که دوست‌دخترِ ده ساله طرف فهمیده.
یه بار با یه بازیگر که دوتا بچه هم داشت بود که همین باعث شد هم اون بازیگره طلاق بگیره، هم شوهرِ ترانه طلاقش رو بده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70397" target="_blank">📅 11:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70396">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLvcMEKZvOBoUE2Iu_YcHmtQy_FmnUtaiazJSGjMS4-sLzcdsGWNC0kCFv4XsogB893yf2yYS3cJBj5K70vEHhUO7tnHEiZ_PYwMej2NdbQ6n8AIMkp25FNGaJd6nughH9U8I4wdX7Ql7hdYAjXMwvMhXp4n26wbXiTaFbejc0D4VmRiuKorLakax6o-N9bi2NKoI8x024Rd_BUuWkIvMkdLjEfYwXVKJ9gFtjVBC0BWny8bktPKhZTrPNodMoNf_9BDJtCPZgIeUHzmHrCyaRhYJD1msltved8hyfxBJbkuCKhFi_p7Mp3IWgrq82LE197R5DrjEDft1WKWDT7vtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شاهزاده رضا پهلوی:هم‌میهنان عزیز،
تلاش جمهوری اسلامی برای افزایش قیمت بنزین، بار دیگر بی‌کفایتی و نابسامانی ساختاری بازار انرژی ایران تحت سلطه این رژیم را آشکار کرده است.
در شرایطی که جمهوری اسلامی منابع کشور را صرف تروریست‌های خارجی و سرکوبگران داخلی می‌کند، مقامات نظام و نزدیکانشان در غارت اموال ملی با یکدیگر رقابت می‌کنند و بی‌کفایتی رژیم در اداره کشور کمر خانوارها را شکسته و ایرانیان را فقیر کرده است. تحمیل افزایش قیمت سوخت به مردم، اشتباهی نابخشودنی و خیانتی بزرگ است. نمی‌توان بهای سوخت را با کشورهای دیگر مقایسه کرد، در حالی که درآمد ایرانیان به ریال و زیر خط فقر است.
مسئله سوخت و انرژی در تقریباً همه کشورهای جهان، حتی بسیاری از کشورهایی که منابعی بسیار کمتر از ایران دارند، به‌طور روزمره و بدون بحران مدیریت می‌شود.
از یک سو، مافیای قاچاق سپاه روزانه ده‌ها میلیون لیتر سرمایه ایران را از طریق تانکر، خط لوله و اسکله قاچاق می‌کند و از سوی دیگر، مافیای خودرو، خودروهای بی‌کیفیت و پرمصرف را به ملت تحمیل می‌کند. این فرقه تبهکار که قادر به حل مشکل نیست، از طریق دستگاه پروپاگاندای خود بار کمبود سوخت را بر دوش مردم می‌گذرد و آنها را عامل افزایش مصرف و قاچاق سوخت معرفی می‌کند.
جمهوری اسلامی، رژیمی بی‌کفایت، فاسد و ضدایرانی است که خود ریشه این نابسامانی‌هاست و هرگز قادر به حل آنها نخواهد بود.
تنها راه نجات ایران و پایان این چرخه ویرانگر، برانداختن کامل این رژیم و استقرار دولتی ملی و کارآمد است. «پروژه شکوفایی ایران» برنامه‌های روشنی برای ایجاد توازن میان تولید و مصرف سوخت تدوین کرده است. این برنامه‌ها بر پایه بهترین شیوه‌های آزموده‌شده جهانی و تجربه ملی ایران در مدیریت منابع انرژی استوارند و پس از سقوط این رژیم، در دوران گذار، اجرایی خواهند شد.
👑
پاینده ایران،
رضا پهلوی
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70396" target="_blank">📅 11:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70395">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56910ac654.mp4?token=fUvFowciFDguss9pWU2xNShAQMh19SEnKvX2-BZFazXJ0e-npI7x_RxQ6dQMo3sT36osf4EQs_Gn-pGs7JzS02rI8KjYZNXmiWvWR6ICrAW5XyXZMhgfUSJYzgxGEF8px2h5VEkV9VltyTtCtIlxhQwmvcluyA3Y-6bPrzITEcQ39tKHSs0bDyfy5ElmQFf69UmjKUomRwj5ET98mR_hMc9OvsNb49ICx1vgRB2XcnD-ZWqcW1rkodHvKo5Sat5bFFmBvYT7CCwvdgUdNxQV0NGEJ6SHf9XoGwRFEYM1lbt7EDZjR1RONyA4N1_nmNK79hOSj72nLXEnlP1DCp9OaIuRCblGYlM00-8eQWeqElsL0Vl8VNTF5wNxqvUPYfl3mR8wTJeQDsTZn4uszwEEL2DI1d1vkwwI1ynlS1cvT6ZNSO7JRBD8r0gmsIr7vHsTVTZyASoQ_7V6kC_yvQ9mJwCLWyKn4EpxekKdLvqkjA11WHmsstXWT4rwUVKRLUp7Emr9OlsbCOaKtrEvLY9SBALUwgC0IjpxmJvP8YGqccakRSlpMWSj6ueELPoJCg-gMxs5IK7eZ9_Vn3BjfTJ6LkVu4N4bLj3V7Hskm84781kQymCnPQ-PgrCFFWVxwH2LynWWeuBtFN3cl31BDMUN_3WvrSmPppS9-kOpxV8oAY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56910ac654.mp4?token=fUvFowciFDguss9pWU2xNShAQMh19SEnKvX2-BZFazXJ0e-npI7x_RxQ6dQMo3sT36osf4EQs_Gn-pGs7JzS02rI8KjYZNXmiWvWR6ICrAW5XyXZMhgfUSJYzgxGEF8px2h5VEkV9VltyTtCtIlxhQwmvcluyA3Y-6bPrzITEcQ39tKHSs0bDyfy5ElmQFf69UmjKUomRwj5ET98mR_hMc9OvsNb49ICx1vgRB2XcnD-ZWqcW1rkodHvKo5Sat5bFFmBvYT7CCwvdgUdNxQV0NGEJ6SHf9XoGwRFEYM1lbt7EDZjR1RONyA4N1_nmNK79hOSj72nLXEnlP1DCp9OaIuRCblGYlM00-8eQWeqElsL0Vl8VNTF5wNxqvUPYfl3mR8wTJeQDsTZn4uszwEEL2DI1d1vkwwI1ynlS1cvT6ZNSO7JRBD8r0gmsIr7vHsTVTZyASoQ_7V6kC_yvQ9mJwCLWyKn4EpxekKdLvqkjA11WHmsstXWT4rwUVKRLUp7Emr9OlsbCOaKtrEvLY9SBALUwgC0IjpxmJvP8YGqccakRSlpMWSj6ueELPoJCg-gMxs5IK7eZ9_Vn3BjfTJ6LkVu4N4bLj3V7Hskm84781kQymCnPQ-PgrCFFWVxwH2LynWWeuBtFN3cl31BDMUN_3WvrSmPppS9-kOpxV8oAY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کجا بفهمیم طرف قوای جنسی قوی‌ و کمر پر ملاتی داره؟
این 4 نشونه‌ رو تو هرکی دیدید یا فرار کنید یا سفت بهش بچسبید:
صورت رو به سه قسمت تقسیم کنید، قسمت پایینی از دو قسمت دیگه بزرگ‌تر باشه.
فاصله‌ی بین لب بالایی تا بینی هرچقد ارتفاع، عرض و عمق‌ش بیشتر باشه.
لب پایینی گوشتی باشه.
سوراخ بینی گرد و بزرگ باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70395" target="_blank">📅 10:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70394">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFHxOhYUnjaNqi28-OY3tZnUZvO-yBPBdyU-3Cb2FdIGx1u-bPPZ5kZN8rBsN8wdxYa10f08NlXhcCzw5iXdEg0FoNe6MtOIFoYBLQajPA1377mOtELc_-khKQXH6wIFtV0RuBvGYQKmhqeaVWbGdCxnyLobQ0feRZ5fsnNho1pz7wEABwpvKQXcur7BX9YOJE-jNCgSxgkLGM38d0F57ZkRfR5y99w7B-AD2YILzODOo6ozKdgR_WMc29S-WC-249I4NWYjxLpXgsP8m9sPHvgVuCYv3Qa8a-4cSRV1410oJy_CmZ-RuvD95w9YwKAW3BmLJp8UvgVsRRTkFnM_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
〰️
سنتکام:
نیروهای آمریکایی مسیر ۶۸ فروند کشتی تجاری را تغییر داده‌اند، ۳ فروند را غیرفعال کرده‌اند و سوار شدن به ۲ فروند دیگر را انجام داده‌اند تا از رعایت مقررات مربوط به بن‌بست اعمال‌شده بر بنادر ایران اطمینان حاصل کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70394" target="_blank">📅 10:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70393">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49fa266ff.mp4?token=DDhuCyDCcZlOCWHa29EIdItEiCUr2b5dLbXzHYu62jaj9ksbZSDa_Aqxyovv1A8nDwqaaaxmb3e1BQ84-ARX-X6n0E4H7UX6L7rSaHveP5tOQoAfaLqg52EBr7Rif5o-t0bOzjn4RYCCr4RkhfAWgAa4_7EU0lTj31-fvpajkE9fIpHrmj94fuCK7V-eyACQLY34DHo-7MprXFyVcAiKHnoaM1XWvryOcn5xi_MWEfwJKledxe4j-gYIc48NYXelu-_HJfziSlilNvmuI8riy7DXWIJjIcrVqY0evUbl3GVjJBorLyBMOxaJroZNRfz_U_Kyk9NKIb0F9TTw9ak2Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49fa266ff.mp4?token=DDhuCyDCcZlOCWHa29EIdItEiCUr2b5dLbXzHYu62jaj9ksbZSDa_Aqxyovv1A8nDwqaaaxmb3e1BQ84-ARX-X6n0E4H7UX6L7rSaHveP5tOQoAfaLqg52EBr7Rif5o-t0bOzjn4RYCCr4RkhfAWgAa4_7EU0lTj31-fvpajkE9fIpHrmj94fuCK7V-eyACQLY34DHo-7MprXFyVcAiKHnoaM1XWvryOcn5xi_MWEfwJKledxe4j-gYIc48NYXelu-_HJfziSlilNvmuI8riy7DXWIJjIcrVqY0evUbl3GVjJBorLyBMOxaJroZNRfz_U_Kyk9NKIb0F9TTw9ak2Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Ai
❌
IR
✔️
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70393" target="_blank">📅 09:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70392">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15aadac163.mp4?token=PiKmngOoLoJHuiEUNZzE5HTsqGoEQwGWvbfuAn07OYZyLU2plwVLqf6Z5_qJUDREe8L9JErskDgpI0aEDiCpczaDsmRCvYKcZ3PE1vGxoOVpS-bQXr4DH1gW7wl0w8bgZm1JlyN62wVpHBjIVm16uxeQOgViEa4iCLFRbqmpKTdWazEEXCzlnBLXJroPtpFAc-ckJObJqO0cLwTpEaAShB5W_Lc7EtoX5OpI71lGW4zTs9Jee9jlcJ8GnF0UYEheP4fEKFvjLvynRRPpDCxYa5rI01n4f_drfQylGlo7af73i2pmih7EwoXMOwBQ7CuJ0hLVQOZVCnRtoeH8SHoCVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15aadac163.mp4?token=PiKmngOoLoJHuiEUNZzE5HTsqGoEQwGWvbfuAn07OYZyLU2plwVLqf6Z5_qJUDREe8L9JErskDgpI0aEDiCpczaDsmRCvYKcZ3PE1vGxoOVpS-bQXr4DH1gW7wl0w8bgZm1JlyN62wVpHBjIVm16uxeQOgViEa4iCLFRbqmpKTdWazEEXCzlnBLXJroPtpFAc-ckJObJqO0cLwTpEaAShB5W_Lc7EtoX5OpI71lGW4zTs9Jee9jlcJ8GnF0UYEheP4fEKFvjLvynRRPpDCxYa5rI01n4f_drfQylGlo7af73i2pmih7EwoXMOwBQ7CuJ0hLVQOZVCnRtoeH8SHoCVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مصطفی خوش‌چشم تحلیل‌گر صداوسیما:
ما همه کاری رو در دنیا میتونیم انجام بدیم.
بریم چندتا مین کار بزاریم توی خلیج فلوریدا.
خنثی کردن این مین‌ها هم کار آسونی نیست و کار سختیه.
شما برو چندتا مین پیشرفته کار بزار اونجا تا یکی دوماه مصیبت بکشن.
بحث من الان تنگه هرمز نیستا من کاملا جدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70392" target="_blank">📅 09:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70391">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70391" target="_blank">📅 03:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70390">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=mGy-CqXCks3cNIMtWakB1Jy4laDdKuFUiip7IdVBQSHC8eu209ULa-DuYRT7YDVBc25NbcadPSpxoaXJXAqnNVs3V47WQoOoUXFGNjio3aTP19StWOesaVz1IePbAmW5B3WQgg36iUF4c3TNyN5BqsxUa9R-YN2i8CNfJWFkYfHBzlJr6aGQdfh5WiOkPq9LBfvAr76rBsL77F3-Xjci3CcgsA_3RGtNucmP2p4MxlDnEOOmBzhFhqqZR6kcGQLEhS09CgmM5AaQssMrY_pJdOwkpNGhliE4Ye01dAPCgiPU0SHesyO_GBKh2I2V0420gnxDdKawZo29cDumdgaO5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=mGy-CqXCks3cNIMtWakB1Jy4laDdKuFUiip7IdVBQSHC8eu209ULa-DuYRT7YDVBc25NbcadPSpxoaXJXAqnNVs3V47WQoOoUXFGNjio3aTP19StWOesaVz1IePbAmW5B3WQgg36iUF4c3TNyN5BqsxUa9R-YN2i8CNfJWFkYfHBzlJr6aGQdfh5WiOkPq9LBfvAr76rBsL77F3-Xjci3CcgsA_3RGtNucmP2p4MxlDnEOOmBzhFhqqZR6kcGQLEhS09CgmM5AaQssMrY_pJdOwkpNGhliE4Ye01dAPCgiPU0SHesyO_GBKh2I2V0420gnxDdKawZo29cDumdgaO5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+UfR2NG4GjAMwNTQ0</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70390" target="_blank">📅 03:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70389">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWenBj5TEMiBRpEA8oFpGiGYXl3HV1IM90IX4t-UQtxg41FxXnywy1BN1eU9BPyi5MTEjFCiq6COluoVEG6q5wZA7iG-XvfINJ9BgJ8eQ0deykIwLg0pNHxsrj1QVrKmWkb6YIsoxtene3hO1MpDaHDhbiORmQeVxtfURhpHDMO0H8KW2Aw6TrsgeWphd7T_5EXeAbxrGLo-SXozrU4askOT5WFHoYoFfiXP4VEhXD0JFBk97koe32g4V0rld21jt_aYcS7P9J3x-ScCYtepV2xzyquWyTQESa_TldKh6I3NPe14hDmaL75oajun_Vuq2-1l_GSUpx6iSZMUh10UxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فعالیت پنج سوخت‌رسان و یک هواپیمای هشدار اولیه در اطراف تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70389" target="_blank">📅 02:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70388">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c253cab7c2.mp4?token=cI9H0olHvPqD9gv_qIDEPm7ZgrX3Qvo9GujdAFEcHT8UNstda2tboJ3XZF5NZNjig_nwG3wbrr5yDAwsvNQP7QGURjKcvfVxyI8bE_y8uDCIx7wfI7nXWJ4Ml4MMuVjVUBjzUHyHgpZLhJbLkhMnNbvao5Is_C2zZCU-b3qgo1AChGXxiUOilgSBYe9uhz7KZQqJk-29s17il00a7Z6Y0PNUkpLynhYhy8IpflTIIcx_MuDb-BO720fwqdxzX-H_lZUtdkQzBEfMqpmXU2iecLtAGCTCHB8kOLKx21DzM-AYLRIUAsBpytKqJpJazrmoyaznffPQ_AbMbn9DTiN4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c253cab7c2.mp4?token=cI9H0olHvPqD9gv_qIDEPm7ZgrX3Qvo9GujdAFEcHT8UNstda2tboJ3XZF5NZNjig_nwG3wbrr5yDAwsvNQP7QGURjKcvfVxyI8bE_y8uDCIx7wfI7nXWJ4Ml4MMuVjVUBjzUHyHgpZLhJbLkhMnNbvao5Is_C2zZCU-b3qgo1AChGXxiUOilgSBYe9uhz7KZQqJk-29s17il00a7Z6Y0PNUkpLynhYhy8IpflTIIcx_MuDb-BO720fwqdxzX-H_lZUtdkQzBEfMqpmXU2iecLtAGCTCHB8kOLKx21DzM-AYLRIUAsBpytKqJpJazrmoyaznffPQ_AbMbn9DTiN4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
〰️
سنتکام:
ملوانان نیروی دریایی ایالات متحده در حالی که ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» (CVN 73) در دریای عرب در حال حرکت است، عملیات پروازی شبانه را بر عرشه آن انجام می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70388" target="_blank">📅 00:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70387">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4291f4458.mp4?token=SZ77NYsnHExALRVBcbDq22xWdTqgOq4p1NY-2gp4GorGOcANUWMZ1zZulkgb_qJ0_p5sSGhgRd8iQaxX325KIWMWGsX76y2szjCKwHlckhMFSt1eFi56cu2UrVaYE0d0r4kqivwVfUI7d4P13geb0YmQ2v_yInf60xrEyXCb47qy3wz3Js39guKI45VULS5M3rZL9ej5LiiOuP8vn-4uzAbydxPF6T2k8ZUE4rHNC2X_2uD3qZnNV25respIaWDxfPFbQ5h3FUY8cKHFyRZ8R-TsR-OPpB7qrI6kgbClqVRcB3oI7vgyuQMSnKAKgpd6JWc4tWwjVq_Jbe0hot3B3ILm05pL_iHfpjrQrVZcUAbN3t3SPY6IGkD2OkIIFN8Vr0RXTI-iyxCUsr1IasvxSFVHxz2ZOrs0Y4QWueRbNv4HwXQQBQlTEIrY7TvQMllW2wjMsuVs2pIk8A6cRbdkkP14pbM2hZwyA_EbNewywruG7YXqNarM4alktsP1X47DPQDm0SmKu9HzWx6yfdoeMta6p_xqYy98z0bCzSUl-nbpgSUiioA5qyzQQapYhNGRPnfhxZTwKSZNey7Mc-MZvijYQmG5WncUCo-qrZTN2GMBvYnfI7yeQqDTQn2tOvh3_kXtNNuV0IUF1hLmJ380x8SrjcouPfhjlcAmwd_B11M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4291f4458.mp4?token=SZ77NYsnHExALRVBcbDq22xWdTqgOq4p1NY-2gp4GorGOcANUWMZ1zZulkgb_qJ0_p5sSGhgRd8iQaxX325KIWMWGsX76y2szjCKwHlckhMFSt1eFi56cu2UrVaYE0d0r4kqivwVfUI7d4P13geb0YmQ2v_yInf60xrEyXCb47qy3wz3Js39guKI45VULS5M3rZL9ej5LiiOuP8vn-4uzAbydxPF6T2k8ZUE4rHNC2X_2uD3qZnNV25respIaWDxfPFbQ5h3FUY8cKHFyRZ8R-TsR-OPpB7qrI6kgbClqVRcB3oI7vgyuQMSnKAKgpd6JWc4tWwjVq_Jbe0hot3B3ILm05pL_iHfpjrQrVZcUAbN3t3SPY6IGkD2OkIIFN8Vr0RXTI-iyxCUsr1IasvxSFVHxz2ZOrs0Y4QWueRbNv4HwXQQBQlTEIrY7TvQMllW2wjMsuVs2pIk8A6cRbdkkP14pbM2hZwyA_EbNewywruG7YXqNarM4alktsP1X47DPQDm0SmKu9HzWx6yfdoeMta6p_xqYy98z0bCzSUl-nbpgSUiioA5qyzQQapYhNGRPnfhxZTwKSZNey7Mc-MZvijYQmG5WncUCo-qrZTN2GMBvYnfI7yeQqDTQn2tOvh3_kXtNNuV0IUF1hLmJ380x8SrjcouPfhjlcAmwd_B11M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی پشم‌ریزون از زلزله شدید چند روز قبل در کلمبیا که باعث شد ساختمونا برن رو ویبره:
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/70387" target="_blank">📅 00:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70386">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
⁉️
دقایقی پیش حوالی یوسف‌آباد و امیرآباد و فاطمی و... در تهران صدای فعالیت پدافند شنیده شده.
عده هم میگن صدای تیراندازی بوده و همه چی آرومه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/70386" target="_blank">📅 23:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70385">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc11d1c4b.mp4?token=mfVNAOQxDfo84-hysut8J1dJnhJnJ-N28sd93S_YjJipT_a0TDumK9XjBIXvSmGXzxFL3ZJ0nyb0dI4MGsDXX7beVho1yhz6on-F-lzL6D9qER2sg64lGrFgWQvPSmaEeCBp9CbOw5qw9FUc624vqXPi20rIXuv5T9V2Vgh86_rTSpLQLp1pbLf6whE_XPg5D-5gj0reKNPm4Oapr8reYNr-KmgEDisGUGE34WGqoMDlSpqld4Qtk203YX_AndH_7ZHyvvoLDm1zGkbXNPhJcYcqV535kmXSHwrIge_GlGL3NNrLD-4pp-4nDFR8t3azsGa_PLOKBYYIM3wahyIwkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc11d1c4b.mp4?token=mfVNAOQxDfo84-hysut8J1dJnhJnJ-N28sd93S_YjJipT_a0TDumK9XjBIXvSmGXzxFL3ZJ0nyb0dI4MGsDXX7beVho1yhz6on-F-lzL6D9qER2sg64lGrFgWQvPSmaEeCBp9CbOw5qw9FUc624vqXPi20rIXuv5T9V2Vgh86_rTSpLQLp1pbLf6whE_XPg5D-5gj0reKNPm4Oapr8reYNr-KmgEDisGUGE34WGqoMDlSpqld4Qtk203YX_AndH_7ZHyvvoLDm1zGkbXNPhJcYcqV535kmXSHwrIge_GlGL3NNrLD-4pp-4nDFR8t3azsGa_PLOKBYYIM3wahyIwkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ظهوریان، نائب رئیس‌کمیسیون اقتصادی مجلس:
افزایش قیمت بنزین مثل چیپس و پفک نیست که راحت بتوان قیمت آن را تغییر داد
هیچ‌کدام از ۳ طرح مطرح شده، برای بنزین مناسب نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70385" target="_blank">📅 23:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70384">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9209031f2e.mp4?token=KDntkEoJzBEO8lwo3ktLIImabKbiKfCNgpUf6ID79fRKptUmQUhWhlerY8k1yvKict-DFRiCfhMbNIKHHQ8vZqPDfbK7a5hDPi3aNEkqkBMW4WMrhXJ7ePhBNb4gY3VxrR0oA_GDvqPGZRuCsZF8QW_ObV3gCI4_-9FRH46Kcgz8Cpn2y8whKWlP_kSwlGpF2zRpnieHjW2LeFHMt2B0WzqzsZMp4HeXFzlhaTqPiPQEDtNoCl9npuAVTkPnKMYICprGzcl-lmExpVVh9BS6QXb-fEu_OVw69anZEnF8TM5-uOEIigW5EHRSJ_XmTxGe6v70AzAQg9jXuVIgpHBEqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9209031f2e.mp4?token=KDntkEoJzBEO8lwo3ktLIImabKbiKfCNgpUf6ID79fRKptUmQUhWhlerY8k1yvKict-DFRiCfhMbNIKHHQ8vZqPDfbK7a5hDPi3aNEkqkBMW4WMrhXJ7ePhBNb4gY3VxrR0oA_GDvqPGZRuCsZF8QW_ObV3gCI4_-9FRH46Kcgz8Cpn2y8whKWlP_kSwlGpF2zRpnieHjW2LeFHMt2B0WzqzsZMp4HeXFzlhaTqPiPQEDtNoCl9npuAVTkPnKMYICprGzcl-lmExpVVh9BS6QXb-fEu_OVw69anZEnF8TM5-uOEIigW5EHRSJ_XmTxGe6v70AzAQg9jXuVIgpHBEqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
❌
🇮🇱
فرمانده سابق نیروهای ویژه ترکیه، زکای آکساکالی:
اسرائیل نمی‌تواند با ما رقابت کند، ما مانند سایر کشورها نیستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/70384" target="_blank">📅 22:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70383">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXDsWuqk_8yte0oSMnnYgEpQaFtJMI5OBK2OkWZXEMyTv7a4sn-mxWMChk3Qix630Gs_oxnrzJVhqbwBMao3hTlwyK1E3umS-oMixyH00SjQ0Qs2r3Pd5kVQfq8pX2lNDZ9u9BAjAr5luXCHYwmhJY2VIQ_oyx6BdPiLEAQHwe78m6fN9gWK69rqvPOAYCZPaWMAuiwePRRqxRpvOPalk0-ISHYUphSIkCR5I9NAcmpvo-omi-zIxIZ4x98458jq064vDUBnBuzOsVt6VWMzvalflxqujtmHU3OPJAvsJ4bJuuz6L0mxg0r7c3jwHmj530KzWEsUMlOhrTw1dUzkZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ بازنشر کرد:
رئیس‌جمهور ما به ایران هر فرصت ممکنی را داد تا سرانجام رفتار خود را اصلاح کند، از نقش خود به‌عنوان بزرگ‌ترین حامی تروریسم در جهان دست بکشد و به کشورهای تولیدکننده بپیوندد. او درباره پیامدهای ادامه مسیر غیرقانونی و وحشیانه‌شان به آنها هشدار داد. اما «رهبران» آنها چیزی جز رفتار تروریستی و قانون‌شکنانه نمی‌دانند و اکنون رئیس‌جمهور ما به وعده‌های هشدارآمیز خود عمل می‌کند. این‌گونه است که رهبری واقعی عمل می‌کند!!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/70383" target="_blank">📅 21:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70382">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7188f3aad0.mp4?token=Z5JQo5Upln1a1c-qMX5AIxJ9wikY8p3DxsBxitMuUilPYESsShwI31lqkMWUk7FPUZl2TZJ3Da_Cx8ju_xcvpy_zZb1ok1Ya2tCvZUTxH1LU13CZqJZqPvg-4lifmiufvyTUlcizZDqnaHLQH1PbUgZAA9UbqB5dzvpWK-AJ7j0_VuCpjhoWbQt4zItYFenqOU-Hp61Rr1WlFduSvMqbm28uvj84PAPm9-ejtMk-c2PNYrhx1jUUDdNxfPyAD1giCbHLAo6ASCtZfJ2867_CoPlKT-V-XIAEaoK8Mpj1U4mCigxuQbwRn9l-ZGaDDfqGYe6GLGt1CxDY9LerZbp1Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7188f3aad0.mp4?token=Z5JQo5Upln1a1c-qMX5AIxJ9wikY8p3DxsBxitMuUilPYESsShwI31lqkMWUk7FPUZl2TZJ3Da_Cx8ju_xcvpy_zZb1ok1Ya2tCvZUTxH1LU13CZqJZqPvg-4lifmiufvyTUlcizZDqnaHLQH1PbUgZAA9UbqB5dzvpWK-AJ7j0_VuCpjhoWbQt4zItYFenqOU-Hp61Rr1WlFduSvMqbm28uvj84PAPm9-ejtMk-c2PNYrhx1jUUDdNxfPyAD1giCbHLAo6ASCtZfJ2867_CoPlKT-V-XIAEaoK8Mpj1U4mCigxuQbwRn9l-ZGaDDfqGYe6GLGt1CxDY9LerZbp1Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
در شهر برن سوئیس در تابستان، خیلی از مردم، در مسیرهای مشخص بعد از پایان کار وارد رودخانه آره (Aare) می‌شوند و همراه جریان آب تا نزدیکی خانه‌شان شناور می‌شوند.
لباس و وسایلشان را داخل کیسه‌های ضدآب می‌گذارند و در نقطه مشخصی از آب خارج می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/70382" target="_blank">📅 21:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70381">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNtpSnCjGfBRfdCZxJ8PwCDQnbTzzHksPo0eG0-NlBXpsYWxqJRrc4NtQBG236gJ2KMMQTc-C1a5WNH-zK5BBMwN9_Q5GQxm72vUuW9nIibxI0sJlx7lC0l6npcgf0PHHmns7RSiZ5HsKLT1Bo38cSq7kwj4dk888RcdqWrTWVaHCChAc-_PZozofPIHNGxHmdpzr0TypMmYp4FmCZscD2pR-UKsOe1_LQL8lW8UFnTP3hfBKi9jfZfP5wZYLgKRDT3CajVjF64UkiKgtHCE29wtTF8E0c8gvFH9XYTgF3e4OkUsQnkmNVrGCskNciwFxe-idimKM7OzBJBujOvkvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ایالات متحده ثابت کرده است که زبان دیپلماسی را نمی‌فهمد. آن‌ها نه تحریم‌ها را لغو می‌کنند، نه منابع ایران را آزاد می‌سازند و نه به دزدی دریایی پایان می‌دهند.
با این حال، تاریخ نشان خواهد داد که زبان قدرت، آن‌ها را وادار خواهد کرد تا نه‌تنها این اقدامات را انجام دهند، بلکه از ملت بزرگ ایران نیز عذرخواهی کرده و برای همیشه منطقه را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70381" target="_blank">📅 20:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70380">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTpk-yMZNpyJ5oToMGXWoTGfx-arnLk58h30bdkOB1mvl9yWRwwcSVTR0kWd-dkgBxEoZI324vKWrLbtk193i7KMu7IkS_C_7YDnX8YdzU-SKCMvv6QCsfjhTNkNLf-XPh0u9WxhC198lIzyYFLc4tgtTBUSrO4JRzU3dKHmTttmsbivypuA90XzvuvwuEO1I4YgmbtI4r8TSBN0XMdLRveVFFSbixwDCn5BCNaMSZ3hui9_KqjdrOr0HDtgsDbunDwVVAoSLS8ZWMDDC3lrOTZZCkyBbj8JykM87Y_6C-xzthsS4MXSQwgNGUqxazOP0eZEG9eUYlFRpHPgsLmE4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی:
۱۴ سال پیش: «فلج‌کننده‌ترین تحریم‌های تاریخ.» شکست خورد.
۸ سال پیش: «فشار حداکثری.» شکست خورد.
۵ ماه پیش: «تسلیم بی‌قید و شرط.» شکست خورد.
امروز: «ویرانگرترین عملیات اقتصادی تاریخ.» محکوم به شکست است.
ما این فیلم را قبلاً دیده‌ایم. همان حرف‌های پوچ؛ همان قلدرها، اما با چهره‌هایی متفاوت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70380" target="_blank">📅 20:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70379">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781f58184f.mp4?token=XaIAmjl4kFWZU5AXXdHj4arRAbzf70XmghybqR1SWuNPzzJ08mj5CkqQe8IauuknQ_8_1HLdhPeK_18b9zH_VCI783uskMFTiI20xAoP8N88vn-JLJ7bKqISUXE7XVGBmeWEO1sf36-BfIGm-2WSyBkqnJbtiPI48o9lQfWEZZnUTr9YamwBVTFqBGWk9QpIt4hHKPbx7CfVMnhoh7iC8Dujs1QcvHCqmhdYiMyM97PkvPnZvn0QU7XLU9K1G6eyzvCEWrF1nQ7HjBynuGlSFNctc1KdDWckUeTIZhyAClw0vMffM026cETr4zyA3uI5VMHejyZPItuYR-7BdhbwnrmFS-NFKMGLiyODsqLVGSg6Xhb66gU2OhqemWyWcJJPXXipvHHMkR6-cA8lspzdnLXhgdtPX5UQm_7W08iTh5ML9UlDN--t95Zb34P36rsdnaEaeNxtPQN6GPR3THOwLT6024t8OUn1OZ_6_764u2u0LFEL-QjIJUn2l2wn-AuwEfJDBSfna3XCuxsgtQHtpsG8EkBEuB0EVwWS9MGgKnfZaxiC6Cv3jj5a0PlsUD_-sg_d0UGkqJT3ThqheCL9-7gO--TCl8gh_h1LtKVbArEEY_CAE2IW-gCT0QvFBzvKjlEY-eDjp2soWI31_dBCezlbzfkngPYzqCrAOMt4gI4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781f58184f.mp4?token=XaIAmjl4kFWZU5AXXdHj4arRAbzf70XmghybqR1SWuNPzzJ08mj5CkqQe8IauuknQ_8_1HLdhPeK_18b9zH_VCI783uskMFTiI20xAoP8N88vn-JLJ7bKqISUXE7XVGBmeWEO1sf36-BfIGm-2WSyBkqnJbtiPI48o9lQfWEZZnUTr9YamwBVTFqBGWk9QpIt4hHKPbx7CfVMnhoh7iC8Dujs1QcvHCqmhdYiMyM97PkvPnZvn0QU7XLU9K1G6eyzvCEWrF1nQ7HjBynuGlSFNctc1KdDWckUeTIZhyAClw0vMffM026cETr4zyA3uI5VMHejyZPItuYR-7BdhbwnrmFS-NFKMGLiyODsqLVGSg6Xhb66gU2OhqemWyWcJJPXXipvHHMkR6-cA8lspzdnLXhgdtPX5UQm_7W08iTh5ML9UlDN--t95Zb34P36rsdnaEaeNxtPQN6GPR3THOwLT6024t8OUn1OZ_6_764u2u0LFEL-QjIJUn2l2wn-AuwEfJDBSfna3XCuxsgtQHtpsG8EkBEuB0EVwWS9MGgKnfZaxiC6Cv3jj5a0PlsUD_-sg_d0UGkqJT3ThqheCL9-7gO--TCl8gh_h1LtKVbArEEY_CAE2IW-gCT0QvFBzvKjlEY-eDjp2soWI31_dBCezlbzfkngPYzqCrAOMt4gI4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یک آخوند در تجمعات شبانه:هنوزم از کنار بیت رد میشم بوی گوشت سوخته آقا میاد
🤣
🤣
یه روز یکی بهم‌گفت بیا بریم بیت هنوزم بوی گوشت سوخته حضرت آقا میاد
گفتم اغراق میکنی چنین چیزی ممکن نیست
خدا سر شاهده رفتم بیت دیدم هنوزم بوی گوشت سوخته آقا میاد
نامردا ۱۱۰ موشک سنگین به بیت آقا زدن
حضرت آقا بدن لطیفی داشت اصلا ایشون آرزوی کربلا داشتن هروقت میرفتیم‌کربلا میگفتن به نیت ایشون قدم بزنید
الان رهبر شهید شب جمعه ای کنار امام حسین نشسته و داره ما رو تماشا میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70379" target="_blank">📅 19:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70378">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyalegEEyv1HBVhneW72rVeQwg4hVvYKwq38Hp5zTQDsB0G-z8YR_Td1F61-hQStVHs5uq6Lb7tT4Zna7vrz7JWOBbsZ_GN71rOd3ReGAiU66EEgZ59gBCnelUeLOk9C_9WfdJEP0hqGg4nD4y58-9VKTAABPvxWLxgmoVA70aFMHAM1PIV8zuhXgnTSMgoprumbpLl5UmJsqtvi4QiuV7oQUoIMUKp9xnENqrlzWTqXlnsRxBcPhGy-Q5VC4RgE9bfA4rqu1A0MnwxrpXpJAS5kFezX3Vndf85dErk9lmDvqaTEkG9WAD1Fr04w3DUI1hPyNRpYv9dhlIkcCRjBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
〰️
سنتکام:
تا تاریخ ۲۰ اوت، نیروهای آمریکایی مسیر ۶۷ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70378" target="_blank">📅 18:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70377">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb50540ec1.mp4?token=UuyZoT_ZJ6vmzFHhgh9pjEvNDOiQ1bOK5JvEtti8XJcurnembMxl6eJ21duYxbQgsoIq-hRp7l6WbtNL-JUprvGVV_hdSKgl2Jx24DaTZnSnVK2NsgA5UjLhAvoLTLc1NIgn9qoCN0jtc9ILhKnZYpA1P1RGD01E4Ycl5GViZzfiW24VZjWWrBsUteLnqyEZrM_9AJHTvfuQGXNCse3Dvf5L4K4GmpaZtE6Xlx-KdJLehSLutMbM1MCk94xsrCFK-z7aQEhf8L-UAF6Nbd9TRhYt5dyvr-q_qs3P-MNC7s9IrJZqzZKys-bqISBFXc4p9xPL7-xgutHaPbVisXGvZF3bM2oLIFnZemFZJl-YzDAGsPvFjJxRxr-hG245e3V7_6EFziWPf-1vdeOyzYic97r5oj8gXXFzqZdhoME6Q7Zw4fGDUT1IfH0MrJeF4lEwpV9867B2j-vegPVrlgBcdSO_mkQjp3mQI4UTSXjGdscerp5NUftnkCGESSpNvXCwZd8dnjiX729EkNSMpahNnZ3Rmv1h9B421y-h8GUdZE1BBSxgIMyVawKft1o5LnQlGFNY3q9iQ6UsRc5ElPryY7skC6wkkfAJEv9fgo4kC0-lZDlUeHWERBc5WYhrDzE8kNGvYFLYvoVqSWpPeT4P7V05kOYW6R2B5wDvoAcbc9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb50540ec1.mp4?token=UuyZoT_ZJ6vmzFHhgh9pjEvNDOiQ1bOK5JvEtti8XJcurnembMxl6eJ21duYxbQgsoIq-hRp7l6WbtNL-JUprvGVV_hdSKgl2Jx24DaTZnSnVK2NsgA5UjLhAvoLTLc1NIgn9qoCN0jtc9ILhKnZYpA1P1RGD01E4Ycl5GViZzfiW24VZjWWrBsUteLnqyEZrM_9AJHTvfuQGXNCse3Dvf5L4K4GmpaZtE6Xlx-KdJLehSLutMbM1MCk94xsrCFK-z7aQEhf8L-UAF6Nbd9TRhYt5dyvr-q_qs3P-MNC7s9IrJZqzZKys-bqISBFXc4p9xPL7-xgutHaPbVisXGvZF3bM2oLIFnZemFZJl-YzDAGsPvFjJxRxr-hG245e3V7_6EFziWPf-1vdeOyzYic97r5oj8gXXFzqZdhoME6Q7Zw4fGDUT1IfH0MrJeF4lEwpV9867B2j-vegPVrlgBcdSO_mkQjp3mQI4UTSXjGdscerp5NUftnkCGESSpNvXCwZd8dnjiX729EkNSMpahNnZ3Rmv1h9B421y-h8GUdZE1BBSxgIMyVawKft1o5LnQlGFNY3q9iQ6UsRc5ElPryY7skC6wkkfAJEv9fgo4kC0-lZDlUeHWERBc5WYhrDzE8kNGvYFLYvoVqSWpPeT4P7V05kOYW6R2B5wDvoAcbc9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این هواپیما پس از گرفتار شدن در تلاطم (توربولانس) شدید، ناگهان وارد یک وضعیت کاهش ارتفاع تند می‌شود؛ وضعیتی که با پر شدن فضای کابین از صدای جیغ مسافران، موجب وحشت آن‌ها می‌گردد.
تلاطم هوا می‌تواند باعث تغییرات ناگهانی و شدید در ارتفاع و سرعت عمودی شود. اگرچه این وضعیت از داخل کابین ممکن است بسیار هولناک به نظر برسد، اما هواپیما به گونه‌ای طراحی شده است که در برابر فشارهای ناشی از تلاطم‌های شدید مقاومت کند.
بزرگ‌ترین خطر معمولاً متوجه مسافران یا خدمه‌ای است که کمربند ایمنی خود را به درستی نبسته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70377" target="_blank">📅 18:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70374">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s3QLlfQwKKzb_zdP5oI4YNBWE_59CSXWP_5_HbZfhiG8Tpot1QXhnCWe4r2y4djfUAB7aGh4RHgx3fV65YqnGQG1iHh55Yz1xlwGrT8FVZMYPne_U4z2nnzK3-BWCtQEwK7qt78YdP94IjIAEJvF5L3FIjeLfbfEyOPDmWvAzNAjfjV4YJhP5nbHiSZ2-peCNrQGWd8570T94XDCrqztg60vAUFcyK5lFCFazs91BK8dQ9F2S3L1gCQ50F_QQD34XcSPW8R-WvnYaWieRzBsB5RpFszk4sSbq2NJyAUr0pIQGc8HKmI-6tJQnPp60cnZFwgCaVhOIOF2ew-dp4hRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjZ5Ftn5-O72vsBgeie0rfQSboJB5Cm3stliGY1mgx7YbRHLhSQ0IQ2J0K2S8kKlS8eDeyV5Onq3b5PILmCRR83v1mKOU_KUaiK5IJDLdDhdRpdOecBvl8msVcq1gMYSMvOxvX4KhOq5sl4SwV6ziTV4PLtxfmuSB1ad0E3w_r9xKqQBuepeX4wsM1QhgAaHvGdiV272Nu_LEl7vfCtz9m46cLJCSPH-lTLKo07yOWVvpsmGOkPkqCE0kAVd7ta_MCYuG1sFvLlOhnIf4HcdeRfuJHWkTbm4vWQIlotvv6ARHkcvntK9BVQrDPQMQ7qHP67pZ1RG69Yw5wdsoc_Z0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee703d2eeb.mp4?token=i4YKNNgTFJJ-h80-7ramYxyJmtS1Z-P77FTzqMp7THMJumVNjzirohr7C00nmxLnyJz3WpCdOYaizTYqIiWBXI8H8mDNT-63HkzIPNRia3db4bPQM-3g2mk-d4Nvxd37-w_qmMjWaQwH483_8Wr9Texw99swQRZ7ZBL6rP0Sh01RX1tMC_Usm--xHaTQOORQZPl1uvqZVUsMOjz1XUQM8D4UOa1UAlsHXff8T0fakbx4sHtwNw5IAiBEt1zd8YvU--vDKQb-58CF7MSPGzyc35rBL-k1NaT194ZP49o3gop62CTOXBi65GSewYJNrrdPsAMBYb6fJs9zNNcfEMwUkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee703d2eeb.mp4?token=i4YKNNgTFJJ-h80-7ramYxyJmtS1Z-P77FTzqMp7THMJumVNjzirohr7C00nmxLnyJz3WpCdOYaizTYqIiWBXI8H8mDNT-63HkzIPNRia3db4bPQM-3g2mk-d4Nvxd37-w_qmMjWaQwH483_8Wr9Texw99swQRZ7ZBL6rP0Sh01RX1tMC_Usm--xHaTQOORQZPl1uvqZVUsMOjz1XUQM8D4UOa1UAlsHXff8T0fakbx4sHtwNw5IAiBEt1zd8YvU--vDKQb-58CF7MSPGzyc35rBL-k1NaT194ZP49o3gop62CTOXBi65GSewYJNrrdPsAMBYb6fJs9zNNcfEMwUkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر لب ساحل ، با این پوشش ساعت ۷ صبح رفته و از اون ور یه مرد با شرت هفتی اومده بهش گیر داده که تو چرا اینجایی پاشو برو تو قسمت زنونه...
دختر هم میگه داری بهم استرس وارد میکنی، مرد میگه استرست بیاد بره تو کونم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70374" target="_blank">📅 18:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70373">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">امروز تو ویپاری رو برد آرسنال
⚽️
100 دلار بزارید 245 دلار (25.000.000تومان‌بونوس میده)  سود کنید.
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70373" target="_blank">📅 18:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70372">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/70372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g39
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70372" target="_blank">📅 18:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70371">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea7209957.mp4?token=CocG6vxFx-k1ZjM1KfasxZMwCV-y7Owz4SCIN1GNNXsEFvQZIfx21rd_KohpP6zMtzOYHkh5DZDAW9FftNkmHk2oQmb7PmYq78BcGcwCzUuDyQfJkal6VjPHvz60WZfLB_il9Bb2vGmUfbp0S3N5tCwrCJNzgfLY0FT2jWVby2rO9CaDbuVLGWXU1T-x7twAwNZdnaAfhZ3a2LaL-yzjX4ES5Sf0rNxX-Sck_0zZw1wpbn4tVT_kcMenf-VMW7e4_vWJHz4jvNa2ZkGRNSC56oD9rSVGfEaUIVkE9UQfr3sDzcMzL9Ts9EDoxBizVqx8n85Tseu1d9LDd_gc3HFcvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea7209957.mp4?token=CocG6vxFx-k1ZjM1KfasxZMwCV-y7Owz4SCIN1GNNXsEFvQZIfx21rd_KohpP6zMtzOYHkh5DZDAW9FftNkmHk2oQmb7PmYq78BcGcwCzUuDyQfJkal6VjPHvz60WZfLB_il9Bb2vGmUfbp0S3N5tCwrCJNzgfLY0FT2jWVby2rO9CaDbuVLGWXU1T-x7twAwNZdnaAfhZ3a2LaL-yzjX4ES5Sf0rNxX-Sck_0zZw1wpbn4tVT_kcMenf-VMW7e4_vWJHz4jvNa2ZkGRNSC56oD9rSVGfEaUIVkE9UQfr3sDzcMzL9Ts9EDoxBizVqx8n85Tseu1d9LDd_gc3HFcvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سری دخترا بخاطر اینکه امروز کنکور دادن، این شکلی از پدر، پارتنر و... کادو گرفتن:
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70371" target="_blank">📅 18:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70370">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8650fb289.mp4?token=Gc4igRFDe-mWRfuQtD9ribksqR4oFhDvpyls2088XSKzAviKr8So7QPxFi5uSMD9VEl1W3TibD2JmbUhNXPd1IbqLSqDpHk0TCabmwUymnecwjAU6jhI0U4B7M-HVgQfds3uhfWgoOhannCzhjarm0-4-1aGGyt8psg_tkrHJHKGkPGrvmnTAHOfdDgy4-EhXb_4wAOLmI2ts2w7mGPemcmRhHGCyJnyuOnY3lUMZbYY02APXQqm3p_B5ZA02AhGnzI43uoKzcIcagX4A6cMcf7oQeT_CZKU473CzXjLSL4PCkg0wNlPzMclpN4CtCG5XCzswLead9XQP2_Khbn8xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8650fb289.mp4?token=Gc4igRFDe-mWRfuQtD9ribksqR4oFhDvpyls2088XSKzAviKr8So7QPxFi5uSMD9VEl1W3TibD2JmbUhNXPd1IbqLSqDpHk0TCabmwUymnecwjAU6jhI0U4B7M-HVgQfds3uhfWgoOhannCzhjarm0-4-1aGGyt8psg_tkrHJHKGkPGrvmnTAHOfdDgy4-EhXb_4wAOLmI2ts2w7mGPemcmRhHGCyJnyuOnY3lUMZbYY02APXQqm3p_B5ZA02AhGnzI43uoKzcIcagX4A6cMcf7oQeT_CZKU473CzXjLSL4PCkg0wNlPzMclpN4CtCG5XCzswLead9XQP2_Khbn8xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر به اسم امیر 850 میلیون برای دوس دخترش طلا خریده! حالا برا چی؟ دوس دخترش Pms بوده و میخواسته حالشو خوب کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70370" target="_blank">📅 17:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70368">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/600be60d87.mp4?token=SyeRZBMHuyZBWtRQmj-ZD-CCAhdiOTmJaf0wwGwPgk_iTR5yOd2bP68uF5xEQq7D0yJEKbwN6lK0OQPbTw_lJqbGKzF02m07ajzZWAVjGwufNEpUfjNCLRdSPHq08uGgCTa6DMTDqM60koPcPp2aHAmV9ZpukzkUXYEnDjqlGcXQWi5yIgNeqBo_jcKpiPQYK0mtpdxXigfo7gkTDZNRk5XdsV9vVCZh3jBCVWgnYf_rjvx1aUvlLnziOQBCOFrsn1S0QhT6qvPKnk-ujrfzzXEptmL_iGCJhzOm84z7ODKoz_WVUiXerHqhlUyybXnvSnSFy2jAmgVrykixkZrMkg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/600be60d87.mp4?token=SyeRZBMHuyZBWtRQmj-ZD-CCAhdiOTmJaf0wwGwPgk_iTR5yOd2bP68uF5xEQq7D0yJEKbwN6lK0OQPbTw_lJqbGKzF02m07ajzZWAVjGwufNEpUfjNCLRdSPHq08uGgCTa6DMTDqM60koPcPp2aHAmV9ZpukzkUXYEnDjqlGcXQWi5yIgNeqBo_jcKpiPQYK0mtpdxXigfo7gkTDZNRk5XdsV9vVCZh3jBCVWgnYf_rjvx1aUvlLnziOQBCOFrsn1S0QhT6qvPKnk-ujrfzzXEptmL_iGCJhzOm84z7ODKoz_WVUiXerHqhlUyybXnvSnSFy2jAmgVrykixkZrMkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود پسرای مجرد به سیتی سنتر خلیج فارس اهواز ممنوع شد!
بخاطر اینکه پسرای مجرد دختر بازی و دور دور نکنن، ورودشون به سیتی سنتر خلیج فارس ممنوع شد!
ورود دخترای مجرد هیچ مانعی نداره و میتونن وارد بشن، بزودی قراره در سیتی سنتر و مراکز خرید سراسر کشور طرحی اجرا بشه که؛
ورود پسرای مجرد ممنوع بشه که جلوی بساط دختر بازی گرفته بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70368" target="_blank">📅 17:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70367">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a5f935a3.mp4?token=vnja9ZFjHtHSwQb4nA1IsYPKs08F95vxblVMY9fgyaBm09IoefJfR8fORIdqM6_hVEKQmAJkuHUpZx6NcFdNJlV3Ln5tTBoP9lD4eCakyYpxFAdXKdAKS8N0lR8nKcz2osPcJgdCXYpckmnVsbDfiPItbsNYiDNfm6JSxvTHg9xprhDKyxSt5F4M1ZorN_ls4R6X-4g7KU0qEE2cnTOjKLd-zqLANyKcvTUKxK_ILs5s1uQ_cXH8sNUtRoTu2ujTOdjr-XLCt9ro4-ypqY9iSQ_ZhjV2epnHXaz3-hsiNK1et-TSA5HWjgXvslf2Qh4nAQZP0fMcnnATcVUT3VCnOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a5f935a3.mp4?token=vnja9ZFjHtHSwQb4nA1IsYPKs08F95vxblVMY9fgyaBm09IoefJfR8fORIdqM6_hVEKQmAJkuHUpZx6NcFdNJlV3Ln5tTBoP9lD4eCakyYpxFAdXKdAKS8N0lR8nKcz2osPcJgdCXYpckmnVsbDfiPItbsNYiDNfm6JSxvTHg9xprhDKyxSt5F4M1ZorN_ls4R6X-4g7KU0qEE2cnTOjKLd-zqLANyKcvTUKxK_ILs5s1uQ_cXH8sNUtRoTu2ujTOdjr-XLCt9ro4-ypqY9iSQ_ZhjV2epnHXaz3-hsiNK1et-TSA5HWjgXvslf2Qh4nAQZP0fMcnnATcVUT3VCnOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کارشناس صداوسیما درباره نتانیاهو: نتانیاهو خیلی مرده؛
همین الان آماده ترین عنصر برای حمله‌ به ایران اسرائیل هس نه آتش بس میفهمه نه خستگی
نتانیاهو مرده واقعی هس نه پشیمونه نه خسته این همه زدیم سرش دوباره فکر حمله داره
با خودش میگه تا وقتی کله زرد توی قدرته باید ایران صد در صدی رو به زیر صفر برسونم
به هیچ قراردادی پایبند نیستن و چون ما براشون تهدید موجودیتی هستیم قطعا اقدام میکنه مجدد
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70367" target="_blank">📅 16:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70366">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpXfFA3hkuEKMiDAdGamNxrs-Kb33zKPkugAHLw2NzYykycL4-vNqNTjt5IOE_KbsqUUs39L46Y5l_9I-pYKim1-JkRjy-z_GYDSY2pMyOmLvnvowJn-PFhHgAVL4A30mUr6ilEmbLhy9QitkwTr3m9uBODEC4XOkh_a-sBY75W9vo-HUjnmOtyIrXdL7UIPQ3zomRKzrK_a8sKhIhHO-KCcbjkI2fAHRd4ncmjJ3oi69X4bjusMHigZVy-bVcGQatfJujFWtRfQj6I2CAG0srxLNAB9XremB2wFlJRl9fYHD35ZX7V9foLmwp-gQyvh1SEi1rEYPW5-trt8gHS6yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
پزشکیان:   درباره هزینه تأمین سوخت، چه کسی گفته دولت باید بنزین ۱۳۰ هزار تومانی بخرد و بعد آن را ۱۵۰۰ تومان بفروشد؟ ادامه این روند، منابع دولت برای افزایش اعتبار کالابرگ و پرداخت تعهدات مربوط به گندم‌کاران، بیمه‌ها و معیشت کارگران، بازنشستگان و کارمندان…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70366" target="_blank">📅 15:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70365">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⏺
🇮🇷
پزشکیان:
درباره هزینه تأمین سوخت، چه کسی گفته دولت باید بنزین ۱۳۰ هزار تومانی بخرد و بعد آن را ۱۵۰۰ تومان بفروشد؟
ادامه این روند، منابع دولت برای افزایش اعتبار کالابرگ و پرداخت تعهدات مربوط به گندم‌کاران، بیمه‌ها و معیشت کارگران، بازنشستگان و کارمندان را محدود می‌کند
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70365" target="_blank">📅 15:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70364">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzrVObMDfoZv3GQyJYNhm3RRqxOYHFNjQs5InRbpQRdsWCG2fP1Ubjl8MmPk3ASk98ZlKkb7jILbTAVckPIkUv9B8VSGuAqNVLkdVLfHxk5Ap9uZfP8mkXlxX7vzaNYqYDP9e4EbQ6hDGmpP-8JjLwNvF4OkQeJfhAs4Plc1Oj-ze-fzdV6YeSXMJgrAzDoa2gSuZ8q6XYJ5Kli2R6RLsN-BTtbSD27G_fgajzRU_Knl8jn5KcD9l1OQwuYIWnyJMDfNY82_LpEOjMK8PP0-2-2x9T-0Dwd7GLD5eqEpiqVCxWyvY6fCW94lvI8VocgLkcI5eryZJVQgHGAkuvWI4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
مسعود پزشکیان:
بهتر است جنگ را امروز، در حالی که در موضع قدرت و عزت هستیم، پایان دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70364" target="_blank">📅 15:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70363">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/356ce94a67.mp4?token=DaF0Sj-Gf811gX5sGtZYT-ELDr-YTBvSRJmL05_BryjgRSTRXNib0-l5MvcAB2FygyP5yqNveuVIYKbsCxBEfwAqwoJ8vygdL-phahlWBd2UNoGoRGXAMnZH00sE3n7BADnwbdAWC4ReBxtrSz575mrATz1HEeEuxIPrrIcdr8vFfKXayxZTYwYkJWpVgMDPVlkOZb9JA36QAWVaAOB1lY4xYEbrxPt5OKaeOnsQ_4YaBtiJjAyYTnAUkTCqHAzYTKT_7MzEDZ9Ceg1uSRHWyyGHu_2m8MuiKiCWAl3FQN0Vx7hPfiIsmUmf6Xpt_p9o4PmtTmbYH43zSc8l8j__gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/356ce94a67.mp4?token=DaF0Sj-Gf811gX5sGtZYT-ELDr-YTBvSRJmL05_BryjgRSTRXNib0-l5MvcAB2FygyP5yqNveuVIYKbsCxBEfwAqwoJ8vygdL-phahlWBd2UNoGoRGXAMnZH00sE3n7BADnwbdAWC4ReBxtrSz575mrATz1HEeEuxIPrrIcdr8vFfKXayxZTYwYkJWpVgMDPVlkOZb9JA36QAWVaAOB1lY4xYEbrxPt5OKaeOnsQ_4YaBtiJjAyYTnAUkTCqHAzYTKT_7MzEDZ9Ceg1uSRHWyyGHu_2m8MuiKiCWAl3FQN0Vx7hPfiIsmUmf6Xpt_p9o4PmtTmbYH43zSc8l8j__gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وایرال شده از زنی که با اسپری عکس زنای بدحجاب تو لندن رو رنگی میکنه مردا تحریک نشن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70363" target="_blank">📅 14:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70360">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/az4iNRpm_Y2PnkkvdYnUaHi1ukKHHRG4Oi8fY9s4MDXEnI6fkk4NzFMPU2ysUos44RqnsVJcNh18spWrR3chGRHB64Vk9CwmjgHigHNyx9iVMVpj4h3sXxoII30oB4legH_oHnZ2yXvN__cdm_M9uX3_0HyCryEtvb28ievNpP_RPGOu6cW0N9Sc9SkGXUJXckIug501LF18RQ-43rJ6GGYAaFnDvYezfRjTaTtSlvdZLAdImNcOlfiN_K7EX9iX4rHwhKyoz3e62gFPvLpX7IaS9faSh3DOMreDU--PvNTIeFWgFwb7W-x4dcVRciU_wfzcVu5RmbB9BupNnpugzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnW3SJe-Kr6vc9r6PP9iNkPXQIPM-xvSWo9GJ2zRimXkrgsst8fyBanG091OVNHIt679kBPUXSGg7HjocTXC6ONLP5ZoSH5icg3w15BekO_QG8e2vqrDX5JXTys6LxbSD7dSaXZ_wKrmt6p5lfJuTIcE1anD0SKhw43KEQBkXsOtYazYGUFH8oRkeioC8_8Wo93bcX7RvBsGQFpnnBjA3ZBjbDkDfHoKuY9HWiM7CMAQUODXiGMBuoKofEnB5Z54kLemjNvzh-fFGOkAIk5bEtPP3ukYOYq5_kma7kqkLu8MCGS5ZTcdHXqadqlZ_G1oDZaSYnBE4hF9sGLJH0oTJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxXhBvNeX5SjcA6e0AwZL0pGyq_k5j9nrj1vnELDrgTIjDchbO3f2j9U_lfYqrhQzBp0rcPbbbF0h66eKpyqMCdph4dtXjCOpdwgah2WOA_BNk37yhUgi5KV4dWjCphZJpgXprDFaEpgX5pVO9899ATsx5JRWihCklb3JFfDoEoT8GXSt-wo6mZR7PI6NchBbPNr15UDmzGQyWhFsed1OQobwBfGeJ-JUlwEC9gqBdsj5AXAXwpmHnKC5fqxlnW36ZJlFob0dnuiEioOr1X9_IJIvwdtOvfLNjhFIRLLS6kx85fYt3hbn04xNDwn0iTNo_VHw9vy8vmj1GNsVkNzdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💢
🇮🇱
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70360" target="_blank">📅 13:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70357">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ea-6qmALTDftMm3H5KkvMOgRupUp7YcMthA8OlF70nRRM_BRjIZ32uHUvPhoa-nIHuiktGfMCO5x5APw2WvLtV1q5VaBbgrg-sIkMU6GbS4mK4J7DmkFdo5r29F-ISoNDD-kxFcmRERUG1EIgvr3PETc-hVttysIOW5TxQTsLLUQVgPn4U0nTpxdQjG40yNsJb84d3hmaW6j1DT1mUKdaB8x2vL-1F3sg-rphCy7pZyoENpJwo1RGzSEfFs30PDfPkfmXMA4B9KaZPzUZEqtaCqo_XyLe7Qfy0Qyb0a4NMREl-qssvv2znVWxsTNBYQ8B0IhOp_sDmZY_jpJ1dO-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86f5f06d38.mp4?token=Z3UGcHLH0Tcm-DoScTBttgG1fLPxKAloqa_qciGSoss6TBZbFF6e0O-hlb0ZZakRlz9poHveq7dpJ3lfqE8Y3C2BwYY980yDUosOKfyVMvOlVpdM9XR15zVCIUiIqhuqxvoTbPl7DjgWUp8Az3EB_2KNAfpDIrqjFQYT5Q6mUzSjWWLECSlGuqvZy_7azeHXn9X4NuwQdNCH-y2xUVumf9PmHO8OmutzFYvcPmciEyxJzrSeIdvEFPFGb22VlBg_PrywA3Wt5Bx4Y_ULaPOzrJguMvzHCueZPnqTIx8pcfrGPdZNCF5QXe4Efp591amVA9szGMj3GZyxQAzo7uXHeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86f5f06d38.mp4?token=Z3UGcHLH0Tcm-DoScTBttgG1fLPxKAloqa_qciGSoss6TBZbFF6e0O-hlb0ZZakRlz9poHveq7dpJ3lfqE8Y3C2BwYY980yDUosOKfyVMvOlVpdM9XR15zVCIUiIqhuqxvoTbPl7DjgWUp8Az3EB_2KNAfpDIrqjFQYT5Q6mUzSjWWLECSlGuqvZy_7azeHXn9X4NuwQdNCH-y2xUVumf9PmHO8OmutzFYvcPmciEyxJzrSeIdvEFPFGb22VlBg_PrywA3Wt5Bx4Y_ULaPOzrJguMvzHCueZPnqTIx8pcfrGPdZNCF5QXe4Efp591amVA9szGMj3GZyxQAzo7uXHeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رضا گلزار تنها رولز رویس کولینان منصوری در ایران رو به قیمت 100 میلیارد خرید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70357" target="_blank">📅 13:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70355">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee66c3b75.mp4?token=jLDUepn9rxR7nPF-zl5zTy0rMFbo6Fm1fkwDjkOCVOljUejmt7q2VDL04WLmkXSgRPJ-6aDI9AyPMdvz8UTPnJczTB5IvlDVvd6oJ4hwjv4TyvzMPWo5PukmoOleHu4L_fQmp8Pezcllk_zPHaWrhjv8Teb1OXpEfkw63gNH3u0yMROLI2_OHlkJfSJ7eqXKWdz6BXT42KRkGdlVkorxWkfJ011rlM5rp5RTmv-WhMXbpouab8irgx39ayx2xszVHH9Z42VeY1PaQ0G83c6A9EnG0FIgH5Q26pn1WLwX24ngh0bWFttatsXTr_n5F76oT_08xas4y0oAWe8K2tPEYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee66c3b75.mp4?token=jLDUepn9rxR7nPF-zl5zTy0rMFbo6Fm1fkwDjkOCVOljUejmt7q2VDL04WLmkXSgRPJ-6aDI9AyPMdvz8UTPnJczTB5IvlDVvd6oJ4hwjv4TyvzMPWo5PukmoOleHu4L_fQmp8Pezcllk_zPHaWrhjv8Teb1OXpEfkw63gNH3u0yMROLI2_OHlkJfSJ7eqXKWdz6BXT42KRkGdlVkorxWkfJ011rlM5rp5RTmv-WhMXbpouab8irgx39ayx2xszVHH9Z42VeY1PaQ0G83c6A9EnG0FIgH5Q26pn1WLwX24ngh0bWFttatsXTr_n5F76oT_08xas4y0oAWe8K2tPEYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو تهران یه دختره بخاطر اینکه دوست‌پسرش باهاش قهر کرده؛
واسش مرسدس‌ بنز AMG GT 53 4MATIC+ چهاردر خریده که شاید آقایی آشتی کنه
😶
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/70355" target="_blank">📅 12:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70354">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70354" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70354" target="_blank">📅 12:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70353">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzhAd9WrRNgJdyIrq6EnF9MmFlI61wHVEVCbLmp3lJ8uW3YOed-8F-8GiQCXCJyhooGy4LPpZ1dPpvqyYoDFQOe6HC0hng-BF9MGLWjT2SkPFNjXBWBCfc3fWPdJs2-QtYSWIZCNV-prVVzS2Xf3I0fQOqdjy_ooeRxIRJNN3UXs4SC6UqpdrKRLiqoCr3YgjVGy7WOTA5kOxN1UwCLA4Xx4NavQVEa2_3Hp6ZcEE_aXMQsW6IWgN9SyJanyxRBu7OEKxpwEGZ4HI-bqBSiyhRMVjBuiI1GFuRBQUZy9TEWQdXNH0fEz9nazECCnIaN5GgyVUrIJvJ7SMCIcnZ62zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r30
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70353" target="_blank">📅 12:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70352">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3219c52e1.mp4?token=sGON9z7p-pjL16bd2ZwHr_9Cr-k4r0nk_llFmJ7saCfUW4OMhgA37Ebdjd9TH23d89IBOvG3FnhtUqeA40utueoIr8otsjiAo52dAQKP6DPuo-Jzplhto7n6FgbVXRb4uoF645QwTDSaUmmhFAsbI-qbf0Qu-hFT0YaQhQWlZ4NBfY-cBe9FPhInE9uZt8UHs7z9km_MEDRwv4L-0nI2e8AwP_M1_i_SfkQ_mPjFDEngJ66O82PGVbyA6YjFi_Pi8Z7fwwFEXTgELH3y1132UNWhn7k73iQ-6sYvm7wnqIwLjjWp1Siu9AMixZMUlPjB95mMqpM89n5bTT8ZXq5bRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3219c52e1.mp4?token=sGON9z7p-pjL16bd2ZwHr_9Cr-k4r0nk_llFmJ7saCfUW4OMhgA37Ebdjd9TH23d89IBOvG3FnhtUqeA40utueoIr8otsjiAo52dAQKP6DPuo-Jzplhto7n6FgbVXRb4uoF645QwTDSaUmmhFAsbI-qbf0Qu-hFT0YaQhQWlZ4NBfY-cBe9FPhInE9uZt8UHs7z9km_MEDRwv4L-0nI2e8AwP_M1_i_SfkQ_mPjFDEngJ66O82PGVbyA6YjFi_Pi8Z7fwwFEXTgELH3y1132UNWhn7k73iQ-6sYvm7wnqIwLjjWp1Siu9AMixZMUlPjB95mMqpM89n5bTT8ZXq5bRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اوه اوه اجرای بازی "نون بیار کباب ببر" بین دو نامحرم تو برنامه‌ای که مجوز وزارت‌ ارشاد رو داره!!!
همون طور که ملاحظه می‌کنید، چندين مرتبه دستِ این دو نامحرم حین بردن و آوردن نون و کباب به همدیگه برخورد کرد...
پس چیشد آرمان‌های امام؟!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70352" target="_blank">📅 12:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70351">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c0b55713.mp4?token=rwhGrw20GinKSRI0B1tjdavO462ljSAeQU8TGvkGe68CMee4CRnxbpvZELNVZPxzGRN5thlTKicVpkOTXfrQdfVzjVeXSAVkmkmh1u0dIFb4NhB1j3UJJKQRqCtG1wcGeEA5yzPzX_p_uRx1aQ-VrSv5E622xNw3tps8sQJQHvI0FpDjZLbsPfPPu26i0KP5aezImgtGr8GU9EAkS4GA1FLOK0gVbEMKoOPjkGiwdWZjQsVaa6bgOCbtMIhObRw7NjSaLMxKpjLaESrMOyYq_ntQpkprq_avrJIRDCGlXHUyivmjroDkuN8qEdQQ-WC4N4vZi7YburiSnoHk1I8Png" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c0b55713.mp4?token=rwhGrw20GinKSRI0B1tjdavO462ljSAeQU8TGvkGe68CMee4CRnxbpvZELNVZPxzGRN5thlTKicVpkOTXfrQdfVzjVeXSAVkmkmh1u0dIFb4NhB1j3UJJKQRqCtG1wcGeEA5yzPzX_p_uRx1aQ-VrSv5E622xNw3tps8sQJQHvI0FpDjZLbsPfPPu26i0KP5aezImgtGr8GU9EAkS4GA1FLOK0gVbEMKoOPjkGiwdWZjQsVaa6bgOCbtMIhObRw7NjSaLMxKpjLaESrMOyYq_ntQpkprq_avrJIRDCGlXHUyivmjroDkuN8qEdQQ-WC4N4vZi7YburiSnoHk1I8Png" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیروز تو ابهر - زنجان ، دوتا دختر نوجوون اينجوری با موتور صاف رفتن تو دلِ تریلی که پارک شده بود!
جفتشون مصدوم شدن ولی خداروشکر آسیب‌ها خیلی جدی نیست...
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70351" target="_blank">📅 11:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70350">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab8c63c27e.mp4?token=pQB6nPb0tbtTNwpmSuK5Sw2gbRmF5LAxstMmHs_t_PUFPRGEJHquJvzIBCrWvRXFQfenHvxFHw8bfcgPDlIwLpt7ykDZVrkiMZTT8GS7mqH1t_0atgQ6xvB7ZkOZlHodxTDActLS4yEWATzCjwIEZm1x_k6dwP1FUCpKzMEx0ueGA7msp6MaxVj8DIQacOu0SxK2A8rN-alV-BewGdpWarKLR8Pu3yFmHIS484_HlTfndBpPAiEFtUZ8SmCgLCMSIoabOBKNP9pdcL4AiGnV0hk1vkfrE_NvNEW1cizUlRvF1bcO3Zv9oMwD3rfpgDwqVfDvj5AUcMUm1s6M48cHWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab8c63c27e.mp4?token=pQB6nPb0tbtTNwpmSuK5Sw2gbRmF5LAxstMmHs_t_PUFPRGEJHquJvzIBCrWvRXFQfenHvxFHw8bfcgPDlIwLpt7ykDZVrkiMZTT8GS7mqH1t_0atgQ6xvB7ZkOZlHodxTDActLS4yEWATzCjwIEZm1x_k6dwP1FUCpKzMEx0ueGA7msp6MaxVj8DIQacOu0SxK2A8rN-alV-BewGdpWarKLR8Pu3yFmHIS484_HlTfndBpPAiEFtUZ8SmCgLCMSIoabOBKNP9pdcL4AiGnV0hk1vkfrE_NvNEW1cizUlRvF1bcO3Zv9oMwD3rfpgDwqVfDvj5AUcMUm1s6M48cHWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بعد از تبرئه پژمان جمشیدی؛
حالا دختری که مدعی شد مورد تجـاوز قرار گرفته به برنامه‌ یوتیوبی ترانه علیدوستی دعوت شده و ادعاهای خودش رو مجدد تکرار کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70350" target="_blank">📅 11:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70349">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f25ab02a82.mp4?token=eTNZXZIb3vAZkoOu1rBJfSP-Bi6nTG_qnJONB_CurSLmQXIPHwpBxmrevTvFZjNtYhgg30pIvMeR5Or4XYc24iD2_6bUHWjUQ1A_DFIEwCfRlqPdTnc3oCZVJIKlA_8wApKy0RKkdMAaraSZOcAwybd5zJ3ULMJL7fbZjRVGYFVIDowJ72KI3LNzkpnGfwXkxt0_mDHWlmF0Z-x3v07y4Q-ZANP436637EBEWaL0dTDqa7XgUV3DqDqzFLsuEpxixIkHaqtnVbTHnmnsWxRuicvAmiIDUQJNOsVTRDNSG3Sc8QCj2u-BX6TyOkOhagxJ4AxaJOoHFLtu69o0WXhTlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f25ab02a82.mp4?token=eTNZXZIb3vAZkoOu1rBJfSP-Bi6nTG_qnJONB_CurSLmQXIPHwpBxmrevTvFZjNtYhgg30pIvMeR5Or4XYc24iD2_6bUHWjUQ1A_DFIEwCfRlqPdTnc3oCZVJIKlA_8wApKy0RKkdMAaraSZOcAwybd5zJ3ULMJL7fbZjRVGYFVIDowJ72KI3LNzkpnGfwXkxt0_mDHWlmF0Z-x3v07y4Q-ZANP436637EBEWaL0dTDqa7XgUV3DqDqzFLsuEpxixIkHaqtnVbTHnmnsWxRuicvAmiIDUQJNOsVTRDNSG3Sc8QCj2u-BX6TyOkOhagxJ4AxaJOoHFLtu69o0WXhTlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
کارشناس صداوسیما درباره علی خامنه‌ای:
رهبر شهید یه پله از امام معصوم پایین تر بود هرحال هرکی نمیتونه نائب امام زمان بشه
خداوند متعال خامنه‌ای رو تو انفجار مسجد ابوذر برای ملت ایران نگه داشت
اما تو ۹ دی(منظورش ۹ اسفنده) اون همه موشک خورد به بیت آقا که خدا رهبر جدید رو به ما بخشید
اونجا هم خدا مجتبی رو از شر موشک ها نگه داشت
خدا خیلی حواسش به ما هستش اگه ما بهش حواسمون باشه
موقع جنگ رفتیم نماز با حضرت آقا یه آرامشی داشت یه جلالی داشت یه شکوهی داشت بی نظیر
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70349" target="_blank">📅 10:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70348">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced1bea644.mp4?token=fxEn2XX9QWOy5RLk7FlVMHzCBUOzX6n8u3_zLtQi3PFOFyLruiaOmA9Jf4T-uB9CyuyP0HlSHbBw9enKrn1frs_ZyYGeHVn2vIx-4ekLn1TTYJy3CUoZUPcnBJqWLVOsvrLR82dHZwoZFN0_uqlJvuI16kt_1wq8qYflp5mhMLNMkuH1xzrSMsvt8yoXNwwg89n4O700RFToeFRjhAZu7Lld1kUyiyWOAlWUW3_22ymAwpf2waL1vv8FYcnnpTrORPmSJm82vQm2MnhaFVJYZDQRsadkZO9LHNfzCbD5vIcQXMs-hDUMEftxp5lSd2bgwutraFzdgEI2FncFhmHZmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced1bea644.mp4?token=fxEn2XX9QWOy5RLk7FlVMHzCBUOzX6n8u3_zLtQi3PFOFyLruiaOmA9Jf4T-uB9CyuyP0HlSHbBw9enKrn1frs_ZyYGeHVn2vIx-4ekLn1TTYJy3CUoZUPcnBJqWLVOsvrLR82dHZwoZFN0_uqlJvuI16kt_1wq8qYflp5mhMLNMkuH1xzrSMsvt8yoXNwwg89n4O700RFToeFRjhAZu7Lld1kUyiyWOAlWUW3_22ymAwpf2waL1vv8FYcnnpTrORPmSJm82vQm2MnhaFVJYZDQRsadkZO9LHNfzCbD5vIcQXMs-hDUMEftxp5lSd2bgwutraFzdgEI2FncFhmHZmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم وایرال شده از یه چوپان که توی پیجش منتشر کرده و میگه:
بنده مرتضی ریدم تو مملکتِ جمهوری اسلامی، ترامپ سر کیرتو میبوسم، بزن که خوب میزنی
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70348" target="_blank">📅 09:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70347">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac295420e6.mp4?token=gzdeRp0o8KgScxH6q1zFIlUrSrHtATCphzRgvGgLJ4zQKsEBnMEqAtxO74KDxjtb6tmdqcHZH0Uj3XdkklVvSAAL1dSrMWoJNmuj4zZP6B_8jyvyinYO-JDnjISHJieNnee5Sw7AV2piFT35kSBffJ6NS2j-TPcPddbD_J46wW_mzOtWrk4kiG6diWMC_qii4YiNROmdWCpCCXDRChn_8SAS0RkN5LP0EiUVTvreAhAifilZkeU8H0R4zv4Ada3jRA-tgqDcUYUdqgnujORP0dICFfaezQIFGQyIjDCl5-o68HLVyiId2vvt-CB8iKlldpVqQmozNL30qJ-oYhElaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac295420e6.mp4?token=gzdeRp0o8KgScxH6q1zFIlUrSrHtATCphzRgvGgLJ4zQKsEBnMEqAtxO74KDxjtb6tmdqcHZH0Uj3XdkklVvSAAL1dSrMWoJNmuj4zZP6B_8jyvyinYO-JDnjISHJieNnee5Sw7AV2piFT35kSBffJ6NS2j-TPcPddbD_J46wW_mzOtWrk4kiG6diWMC_qii4YiNROmdWCpCCXDRChn_8SAS0RkN5LP0EiUVTvreAhAifilZkeU8H0R4zv4Ada3jRA-tgqDcUYUdqgnujORP0dICFfaezQIFGQyIjDCl5-o68HLVyiId2vvt-CB8iKlldpVqQmozNL30qJ-oYhElaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر بچه به زیباترین شکل، جواب اون مجری که گفت جنوب ایران فدای جنوب لبنان رو داد.
نسل جدید آگاه‌تر از چیزیه که فکرشو می کنید!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70347" target="_blank">📅 09:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70346">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📊
تحلیل فوتبال فقط حدس نیست؛ آمار، ترکیب، انگیزه و فرم تیم‌ها مهمه.  در کانال ما بازی‌های مهم ملی، لیگ‌ها و دوستانه‌ها رو با بررسی دقیق منتشر می‌کنیم.
🎯
انتخاب‌های پیشنهادی روی گل، BTTS و بازارهای مطمئن‌تر  عضو شو و قبل از شروع بازی‌ها، تحلیل رو ببین.
⚠️
…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70346" target="_blank">📅 00:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70345">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=NDqWbEwlE-6ajoHTRbWpjc3vzge-qvabwpZH6J8ijcmlOZLadvHYYMQk_GkjDJXyzy1hX3N3S-KRwLZpHbkO9Zrp2Ms2foDbfmhsiWctci3NqXKoCptP_ovJ0ePStiBEz9nt5G6VghR43i2wfRyxP9WSHXH23GkdGStPLBnv-Au3zZvsLgC2ONJQSQJHKferc71zdW7jGM4Ng_Ga_pl1QGzg0vuEiFyHqgasUQc_7pDH3RRmrvSkjO8cUTqx5zcJ3-_5eNc9IH4zpxNW3mOPX6TrManixeKur9RPvEh8Ba17j0FLpVEWHjoc6bAZmiGjs_VdBEFuKExWMopZpnkqBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=NDqWbEwlE-6ajoHTRbWpjc3vzge-qvabwpZH6J8ijcmlOZLadvHYYMQk_GkjDJXyzy1hX3N3S-KRwLZpHbkO9Zrp2Ms2foDbfmhsiWctci3NqXKoCptP_ovJ0ePStiBEz9nt5G6VghR43i2wfRyxP9WSHXH23GkdGStPLBnv-Au3zZvsLgC2ONJQSQJHKferc71zdW7jGM4Ng_Ga_pl1QGzg0vuEiFyHqgasUQc_7pDH3RRmrvSkjO8cUTqx5zcJ3-_5eNc9IH4zpxNW3mOPX6TrManixeKur9RPvEh8Ba17j0FLpVEWHjoc6bAZmiGjs_VdBEFuKExWMopZpnkqBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تحلیل فوتبال فقط حدس نیست؛ آمار، ترکیب، انگیزه و فرم تیم‌ها مهمه.
در کانال ما بازی‌های مهم ملی، لیگ‌ها و دوستانه‌ها رو با بررسی دقیق منتشر می‌کنیم.
🎯
انتخاب‌های پیشنهادی روی گل، BTTS و بازارهای مطمئن‌تر
عضو شو و قبل از شروع بازی‌ها، تحلیل رو ببین.
⚠️
شرط‌بندی باید با مدیریت سرمایه و مسئولیت‌پذیری باشد.
https://t.me/+nbm7Tb2pz8VjMDlk</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70345" target="_blank">📅 00:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70344">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7469eeed2.mp4?token=k8AZilFUuZ8YWJ420C0dOCHeTkIYpn9sGf02IIuAZwANh8PQdaIt6MSIcJPOwb0PHKHGBPj33OykNDYciqilklydtw8auR6kFdsVu1yfqQOGXaaQEOcOjZ7eYy-XCDAhalzIKriLtHqTDeaWBw9aL4L7zrbLPRSKPkILKegaU_BAmsbsdtjoCn0XQx433Ti45riC1F3tk8VQ4OCXCMFyd7Q64JBb3tuWPPPMr4VIpVAx0BfyT5jC1YMVEsFLzAu2Sar5W7OGlk91p-V4X0VoTRuLu9gfNaSCP93Gh8E0ck0r15kmR4nl8Z7ES3qL5-siwzkzyhNNT3TffFQpwzf51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7469eeed2.mp4?token=k8AZilFUuZ8YWJ420C0dOCHeTkIYpn9sGf02IIuAZwANh8PQdaIt6MSIcJPOwb0PHKHGBPj33OykNDYciqilklydtw8auR6kFdsVu1yfqQOGXaaQEOcOjZ7eYy-XCDAhalzIKriLtHqTDeaWBw9aL4L7zrbLPRSKPkILKegaU_BAmsbsdtjoCn0XQx433Ti45riC1F3tk8VQ4OCXCMFyd7Q64JBb3tuWPPPMr4VIpVAx0BfyT5jC1YMVEsFLzAu2Sar5W7OGlk91p-V4X0VoTRuLu9gfNaSCP93Gh8E0ck0r15kmR4nl8Z7ES3qL5-siwzkzyhNNT3TffFQpwzf51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
آیت‌الله جی‌دی ونس:
تنگه هرمز اصلی ترین اهرم فشار تهران هستش
موثر ترین چیزی که فعلا داریم فشار اقتصادی هستش که به ایران اعمال کردیم
اونا هم به ما فشار اقتصادی وارد میکنن
بهترین راه راه فشار اقتصادی هس نظامی چاره ساز نبود و اونا الان زیر فشارن
ترامپ خیلی واضح گفته ایران نباید سلاح هسته‌ای داشته باشد
تاسیسات هسته‌ای اونا نابود شده ولی آیا دارن بازسازی میکنن؟؟
ما میخوایم یکاری انجام بدیم تاسیسات هسته‌ای اونا نابود بشه حتی شانس بازسازی نداشته باشه
افزایش قیمت نفت گاز تو آمریکا طبیعیه ولی به زودی پایین میاد
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70344" target="_blank">📅 00:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70343">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
لحظاتی پیش صدای دو انفجار در سیریک شنیده شد.
احتمالا موشک شلیک کردن به سمت تنگه هرمز.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/70343" target="_blank">📅 23:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70342">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mon4Gfiv2fQQS6Z7L-spWPcHhB42okhAjoh00dMb4H3V_Uf7E58nbhONJmzr3vQszJ8ghtbPNOky7527SSrO6ciHCQ-QHznpaeEtyruBx3iW0KuDz-bMnxaxfMOKJ-9rg4Qu5tNREXvf6o_XFmJClyfeZGZzc9ETFJad5nLCjpxsKHiOqc1iBGbNOFamhMhUeIIOvQe59byIgDE9tgQW9J-D6_POh1DzefajWSTLM_Bvj3mKJLSd0iovEluYnBRdRmQ-XcGCc9dplb0mmFT5bqtd1qEqnfU7YuhDGBG0RQeV0jqfuBo4BMnpBAr2NPdMTkyK2MCSThMFTp3gYjQY_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
پلتفرم X زیر توییت رئیس پارلمان عراق با عنوانی جعلی برای خلیج فارس، یادآوری کرده که «خلیج فارس »درسته
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/70342" target="_blank">📅 22:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70341">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264b3e2171.mp4?token=JPYpkvjRsDWIZZ_3X2sEI5rA7zJ_jtBu87RMJo8g_L2e1t09TdfVPEtNEAX0WudPTDoVAudO1idFAk8wuKUF0Zi1alimyvNMyx08ra33TqQ3zh_n4-O0ahPDUQgHJYhmwUhaRFxQJN693lZ53jJZjIJnHf2c0OZ2GIU8ckp0S41wVr5-YQsuLCl3Vc3aBasyKrm7c72-YKwz6xJOWSOXqPUhrLuSJ5kVOWvHqWrEw0xaAvq2KFM0rQpYoOx2Tyw32PqhoU7Fx9j_QUFH497CAB0CyFhuKPCyrv0YVN8VfrRFJAxrA2DXYUTe4qxX81UBop6RPJHUFGKvGVnW46687Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264b3e2171.mp4?token=JPYpkvjRsDWIZZ_3X2sEI5rA7zJ_jtBu87RMJo8g_L2e1t09TdfVPEtNEAX0WudPTDoVAudO1idFAk8wuKUF0Zi1alimyvNMyx08ra33TqQ3zh_n4-O0ahPDUQgHJYhmwUhaRFxQJN693lZ53jJZjIJnHf2c0OZ2GIU8ckp0S41wVr5-YQsuLCl3Vc3aBasyKrm7c72-YKwz6xJOWSOXqPUhrLuSJ5kVOWvHqWrEw0xaAvq2KFM0rQpYoOx2Tyw32PqhoU7Fx9j_QUFH497CAB0CyFhuKPCyrv0YVN8VfrRFJAxrA2DXYUTe4qxX81UBop6RPJHUFGKvGVnW46687Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف، اوایل تیرماه:
خودم رفتم قطر، با امیر قطر صحبت کردم و 12 میلیارد دلار از پول‌های بلوکه شده ایران، طی تفاهم‌نامه اسلام‌آباد آزاد شدن.
🇮🇷
همتی، رئیس کل بانک مرکزی، دیشب:
هیچ‌کدوم از پول‌های بلوکه شده‌ی ایران هنوز آزاد نشده و همش شایعه‌ست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70341" target="_blank">📅 21:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70340">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7FLk6U4TXak_L-t_TN_OP150iNjcOLFKs-LyVqwar4znFRjznRx6uqs2UrERnhcqy0SrOioQBuCKG3hvo9PvlONByet-YLRZYRm0aU95cNn4qO6cCAZuEchndQq2MMvFCXUfO9s9A3ePGbkMlajZkB_S_H8ZjTozBw0KzVDNp1cdFZHjlyGtGluKsx6grmc-HSTukp7UoBa2liLIfr4JrHlIxXNyxroIRugU0PLPrJds7KuGbvUT1DLsUFDfYw6OcI-YdWyoMwdInFZZRlX6ljm_BNeTkeix1NI8YwOiu2ZCKR-bYlACrXkJgdw3Xzbh1mZ9HCrM_Z8iFfl3CsXiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بزرگسال‌ترین داوطلب کنکور ۱۴۰۵ با ۸۵ سال سن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/70340" target="_blank">📅 21:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70339">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7149fa402e.mp4?token=QIW0JEByvrqlaBheo2w5Wc4FxPn6oxJr67CmVPWwWgxYMr5eDm79unNn4mP6ne7zfROoUX-0nuqPFT1av7mTQnmhkv9d525KqbWZU10yNujD8xqXyq1TBUMmABfIuvqPL-pcefShHonUbiXTvLG0y-GkU-_z7rG4RhlCWrxauUQXT9vnyvFDrDuPSs1UeMDwaNWGvxt1s8DjGEXExwjCvLf6QSUzHDmgkyDZTjMhKL-v8QMDVDX0W-_5_-DIIb2BkTJaS6K9l7S9a4YpN3hn5eWGr8JqSgo4asWY7msHzhNi-55QUlZDRjPIJN6dXwzOb2GbxXlxfEAYlgGIeTRJbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7149fa402e.mp4?token=QIW0JEByvrqlaBheo2w5Wc4FxPn6oxJr67CmVPWwWgxYMr5eDm79unNn4mP6ne7zfROoUX-0nuqPFT1av7mTQnmhkv9d525KqbWZU10yNujD8xqXyq1TBUMmABfIuvqPL-pcefShHonUbiXTvLG0y-GkU-_z7rG4RhlCWrxauUQXT9vnyvFDrDuPSs1UeMDwaNWGvxt1s8DjGEXExwjCvLf6QSUzHDmgkyDZTjMhKL-v8QMDVDX0W-_5_-DIIb2BkTJaS6K9l7S9a4YpN3hn5eWGr8JqSgo4asWY7msHzhNi-55QUlZDRjPIJN6dXwzOb2GbxXlxfEAYlgGIeTRJbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شهبازی مفعول :
نوید محمدزاده یه پست گذاشت زامبی ها ریختن سرش
فحش و ناسزا و تهدید و انفالو که چی ؟ حق نداری با این زامبی ها اختلاف نظر داشته باشی
این وضعیت زامبی هاست
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/70339" target="_blank">📅 20:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70338">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e91c8463bd.mp4?token=korKnjF7wOIUgkJKszaQsSNuDs34VkEWqg-IZJYCXeeP85AYelYd47nQW_7F0KrFj0rd7ym66MpsBc3Z48f0VKQCmRONoRozBP9rKWokIst9wNRKZs-cf32TV5Fq9jpfH-bLEiDNyLjjw8YZIjfSUE2uAsGHK6k9EYZnN6UPcuYB6rFOYHcPJROYJEcyKga1870qsUx7u-eEI4jCN2VpLlzjTt6IZGweB2ylQ6_aoR_WHUAVVk6YFbrAm6Md42DC8FBk3UOEox0-xRyaCu_Obc1siAeW_VpXMcUN0Jc2nTS8HBuPAO4TcmNsYEBw6bRs2aQo659F6xLDRkYJhjTLRaHiIcqeA9RVtn4mKN3b1IcjqjViEzqlZH7306Oq7kCYJFecBxeSMqcdCt7ODX7X6Si0mj5p93enh5hehw1VMQOdWpTaXH77UvcmL2u0QIRXY1ki0cVvVHT5r09qJYmIvj1zVVp7VklXS3xihH67JFa1q0IguuLPzB9sCzNskUw4rVgI-Zu_Qlg9L36vN-W0JM5NvUVzN-cFU6Y37ICI1erWWPwWY215aBtMFK_Rac0Hec9NJ_Tez5y2OWqp_0dCLNcqttXKHIfRlk8XcIwkuUCH8uuQP8-onH1QJbf4_1CE2lMLR6S_kvDZo070FEEihsCiLvmahJ2ppg4NsPKfqKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e91c8463bd.mp4?token=korKnjF7wOIUgkJKszaQsSNuDs34VkEWqg-IZJYCXeeP85AYelYd47nQW_7F0KrFj0rd7ym66MpsBc3Z48f0VKQCmRONoRozBP9rKWokIst9wNRKZs-cf32TV5Fq9jpfH-bLEiDNyLjjw8YZIjfSUE2uAsGHK6k9EYZnN6UPcuYB6rFOYHcPJROYJEcyKga1870qsUx7u-eEI4jCN2VpLlzjTt6IZGweB2ylQ6_aoR_WHUAVVk6YFbrAm6Md42DC8FBk3UOEox0-xRyaCu_Obc1siAeW_VpXMcUN0Jc2nTS8HBuPAO4TcmNsYEBw6bRs2aQo659F6xLDRkYJhjTLRaHiIcqeA9RVtn4mKN3b1IcjqjViEzqlZH7306Oq7kCYJFecBxeSMqcdCt7ODX7X6Si0mj5p93enh5hehw1VMQOdWpTaXH77UvcmL2u0QIRXY1ki0cVvVHT5r09qJYmIvj1zVVp7VklXS3xihH67JFa1q0IguuLPzB9sCzNskUw4rVgI-Zu_Qlg9L36vN-W0JM5NvUVzN-cFU6Y37ICI1erWWPwWY215aBtMFK_Rac0Hec9NJ_Tez5y2OWqp_0dCLNcqttXKHIfRlk8XcIwkuUCH8uuQP8-onH1QJbf4_1CE2lMLR6S_kvDZo070FEEihsCiLvmahJ2ppg4NsPKfqKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
این مناقشه با ایران؛ ما از آن عبور خواهیم کرد. نمی‌دانیم چه زمانی.
🎙
خبرنگار:
آیا کارزار اقتصادی علیه ایران، چین را هم شامل می‌شود؟ چرا که چین شریک اصلی اقتصادی ایران است.
🔴
بِسِنت:
بسیاری از گفتگوها بهتر است به‌صورت خصوصی انجام شوند.
🚨
🚨
⭕️
بسنت درباره ایران:
ما شدیدترین تحریم‌های تاریخ را اعمال خواهیم کرد و به شما می‌گویم که این کار نتیجه خواهد داد.
این روش در ونزوئلا، پس از آنکه دست به محاصره زدیم، مؤثر واقع شد؛
هم‌اکنون در کوبا نیز کارساز است و در مورد ایران هم نتیجه خواهد داد؛
ما این رژیم را ساقط خواهیم کرد
!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/70338" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70337">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">💎
میدونستین تو ویپاری
با شارژ بالاتر از ۱۰۰ دلار ۲۰٪ بیشتر حسابتون شارژ میشه
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70337" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70336">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/70336" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g29
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70336" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70335">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47dcddfa33.mp4?token=DEy7Fm6RrT_oSCXySR5DTO-E3I5BDjj5jAxVAydy8l3QwaGtoDaTs8PWGWCkvHFhV439ix8CRr7hO9VzBqXqO3IDoiliLBFnaL7jdliUeTnFm1KEHuPyFcosKjF90Myzo_ieIEMmxXI2CeAO9NL8FDd96eo0ZxrXpz8FM9fOARqkDt7jqjk2lg7nyji9ytZre4aVAtdvOAYoNfbhm8x0TaX_ra2kFW3JzngZVo_n9rvoFVFdBwQofpTN5kjSHU_4wuAww8qx2qRAjyjlmHIOE9EP_aOAurzcl0Ekk-52yCsymwbISaEJIh-Earf8nVRwhqZgsRxj43v879jPFgKvZad6f0Mwk35hPBN_fqjdhiLv89hxKfcfkMCI-b2MbRYfIIvbSfU-cQo86IxqkOby9M1bD5pQqQoU1C2-OehTwaaxV4GGw9nmQbdANmUF1DCsvc788kaqUe4rNkO03HA1nX741fPfityLTeSxkwvK3MQ_RMaQ69sKp4jYOu6s87mAvkhxOkdq5BHh0EOwY_OdOkf_GZaxg_1OW1mjxEleeP2LUycHkSSMT23EQGfZ6yZ2uzJFVrpfznVaQ5umhY_Af-bobjgs-gLGLzWkE4MfSaecOxPyWAAp2Z9vf7AxhrWCFdic63Un0GhVg5izve3cPXEB3Q4FIAQCAYI0KLAv71g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47dcddfa33.mp4?token=DEy7Fm6RrT_oSCXySR5DTO-E3I5BDjj5jAxVAydy8l3QwaGtoDaTs8PWGWCkvHFhV439ix8CRr7hO9VzBqXqO3IDoiliLBFnaL7jdliUeTnFm1KEHuPyFcosKjF90Myzo_ieIEMmxXI2CeAO9NL8FDd96eo0ZxrXpz8FM9fOARqkDt7jqjk2lg7nyji9ytZre4aVAtdvOAYoNfbhm8x0TaX_ra2kFW3JzngZVo_n9rvoFVFdBwQofpTN5kjSHU_4wuAww8qx2qRAjyjlmHIOE9EP_aOAurzcl0Ekk-52yCsymwbISaEJIh-Earf8nVRwhqZgsRxj43v879jPFgKvZad6f0Mwk35hPBN_fqjdhiLv89hxKfcfkMCI-b2MbRYfIIvbSfU-cQo86IxqkOby9M1bD5pQqQoU1C2-OehTwaaxV4GGw9nmQbdANmUF1DCsvc788kaqUe4rNkO03HA1nX741fPfityLTeSxkwvK3MQ_RMaQ69sKp4jYOu6s87mAvkhxOkdq5BHh0EOwY_OdOkf_GZaxg_1OW1mjxEleeP2LUycHkSSMT23EQGfZ6yZ2uzJFVrpfznVaQ5umhY_Af-bobjgs-gLGLzWkE4MfSaecOxPyWAAp2Z9vf7AxhrWCFdic63Un0GhVg5izve3cPXEB3Q4FIAQCAYI0KLAv71g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از یکی زیباتر و حرفه ای تر:)
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70335" target="_blank">📅 19:15 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
