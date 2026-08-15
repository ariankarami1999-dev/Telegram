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
<img src="https://cdn4.telesco.pe/file/ms86JJlYhOMwDwdhKjAuwSRFrJM-QQoBJ4Vksim2gQxrU3u_5tQbS09L1oiDw60ecVAi5yZiRMRaE2jnu2C_fPXsCZGIP3IrOhMqtkaPNR6V7O5FUIxNXe5ZAnq61a-QFtI9g248dTpHZpDpSniHwGNFP0FaxcqsXvZFas0AStdfZsWgk4r9oo8VDRn1jJ1EkS_NYO09CIH1ob1qyPIOGnvTbAbqRAD3oiXbSkZKgwzHtoZCaogcn5VcjuKHqINO-oiADkSpnOa3Qd076Q8jUapUd5Hwvxe5vnPdAtiYzHREJQ8j8TSPI5m11kwutiYfcFXOX20n-MJDbUZzxvVp_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 636K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 21:45:18</div>
<hr>

<div class="tg-post" id="msg-27811">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsDXYNi3GvetYbPxoeSq0fY2qe7BMeMerNkatjJqTTFfLwSaZQNaf007tnHshkrapVi0UuH5u5KrWv2B3AaAXbLjjYN7ym9ZAENt_d_ehN_i4_Bg2yV6lvdLR6ra2hpTEQoyW9ZZbdHh6u8a5tuLzb12S0OazMmKxUWNKIIpOxjMHqdkgM7VX_LhDjP1nMB5JRonbdAz96ASLoZtMkYfeZU5OHtU4FazqHAOTh0uYjL9lEirnHClmLDp1iXLWyLAou1Hddzn9w8qa6J4lCvZwOYbWmWGSvb9fvt2WKNQpgF6I63Dv58pYiWNOomx2wz6bSosfUqYSSpRYihjTiIerg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ دشت سه امتیازی شاگردان تارتار درگام‌نخست با درخشش ستاره های تازه وارد.
🟢
شمس آذر قزوین
0️⃣
-
2️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/27811" target="_blank">📅 21:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27810">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsK9qxMTFR0y9DZDSQy8_hXDS2BqQVXomi1xUgtpw2K-m9-p8j4I3DuyafMotE3k0Liah_MvAXfznxUjM-JgwmhzEGQnTAXWPsaxZ_CSJ__aBxswjFxfEJnQwi_3834BU03EvCaQEQomHuUCFhVPKzEachiv1Mq92sosVqvQGn5h_eEhtlYUshj9mTTLidoyBBF4tuxkFy5qff4ZDC8ccQJw74y7O1RWJ5dYu_4xOSxBTbX1TZitqECOWrTtiPOEaeARkbQxo9Tfcke7Urr-F3VUC3D2FsKl1V_L85EXjgb_42XrZAGSxCopw7SaVTmlMMMU0EABTEcWvI3TpDKVAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به شمس‌آذر توسط محمد عمری در دقیقه 15 روی توپ گیری خودِ بازیکن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/27810" target="_blank">📅 21:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27809">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64bc0e0471.mp4?token=qReI0Bb5JsaP-xt5alFBO8bLdGSMifIGLCxQG2vrHSRqYrA1UqG-rOFk8wlO1dFxOw4LuAXx6YjIhln50N-utGAP8Hlud7x8rMGpHcBVlB4s35rQLTsXZaVC_EnK7sJIAQRgPHpqL5deeeVF_CFFyAHCM2Sg9OgdKC4iVkdVFC5r6duhDqtNIwxo5CMe76SDvsIYr4vb5XX4sfpoLcwvcI7P8tZm8uHkA6nX7AxTscFGOKP6S5nx82ZIKI9IskCcZKrFo_EmdG-SsOw9YLpZ7JP5L4lYalAUKcaPOQj-82N_74Zc2HiHzAkZkfblbEpCwCZFEFvcq7fxNdlbt5yBUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64bc0e0471.mp4?token=qReI0Bb5JsaP-xt5alFBO8bLdGSMifIGLCxQG2vrHSRqYrA1UqG-rOFk8wlO1dFxOw4LuAXx6YjIhln50N-utGAP8Hlud7x8rMGpHcBVlB4s35rQLTsXZaVC_EnK7sJIAQRgPHpqL5deeeVF_CFFyAHCM2Sg9OgdKC4iVkdVFC5r6duhDqtNIwxo5CMe76SDvsIYr4vb5XX4sfpoLcwvcI7P8tZm8uHkA6nX7AxTscFGOKP6S5nx82ZIKI9IskCcZKrFo_EmdG-SsOw9YLpZ7JP5L4lYalAUKcaPOQj-82N_74Zc2HiHzAkZkfblbEpCwCZFEFvcq7fxNdlbt5yBUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
استقبال‌ویژه‌بازیکنان وکادرفنی‌تیم النصر از کریس رونالدو بعد از ازدواج رسمی‌اش با جورجینا؛ وایب صورت CR7 خیلی خوبه. حلقه دستش رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/27809" target="_blank">📅 21:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27808">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqDq9i5DdgQv2NSIGnkmyyHxX1eZAgZmKCESqRjV3MaRVbt6DEd7xF94BRsOx1ZetmcS_H3mdJedPaO35qUKcvx7fihyd_xk1QNFgDyuXB6YhOMe72AgNlzWtQY-CRGXsvB2snfmFbO7in9msToqFIDMUCcONVMJ0PYovDp5P_9slWFr6CTItabQY6N3ACL_vrO4Joi-507i3jMywpmVdGqHllGcVcxmUeHyHsQOeo5K1sMPE2tWCdijj8vFDGnn56MKCPSkFTI7e3JflRMhKHYhsFvE3OOGsQbPHdrKNM3xosvqHdCqsdpDChJP7dfXaw5S5ISXy7vOncp3hsMEQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
باشگاه‌سپاهان‌که روزگذشته با کسری طاهری قرارداد امضاکرد به‌خواست‌محرم نویدکیا بار دیگر از فیفا استعلام‌گرفت تا مشکلی برای این تیم در شروع فصل جدید پیش نیاد و با مثبت بودن استعلام فیفا از کسری طاهری رسما رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/27808" target="_blank">📅 20:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27807">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">📹
خلاصه‌دیداردوستانه جذب و پرگل امروز دو تیم آث میلان
🆚
منچستریونایتد؛این‌اولین پیروزی میلانِ مدل روبن آموریم در مسابقات پیش فصل بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/27807" target="_blank">📅 20:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27806">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed602d7201.mp4?token=j8B7Sv-g7_SBo9xzCm2MGFRHYCWfQ8_kkHg1K0mEcnDbXGu4LUq3NlcQyOKi0JVtEBmUkHxwdW-e4-e1cNfMULmdMyRcv7ftH7Z7uct7Vwd4e2XHwa4L_aliEvas3TOFlIXrwoY2ST21lLfRCAJUOMI2bSbFJbxzc-yQVzv3oGvo4M08coxj4tqkw7TEVGsI7ohiv9q4lIThefOLmbJBA3nNHSCVCJ4Fpen8y9JyYnZnD1x7ypiapAYY3DiUMllHbc7HxQSGbv0GtgI-LO8wstiQGid1Ja3i5xzEPtBjVWtT3r3La3Z605IORqJe6_IuHnbRMJT4OYJ0VN-iJsDSww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed602d7201.mp4?token=j8B7Sv-g7_SBo9xzCm2MGFRHYCWfQ8_kkHg1K0mEcnDbXGu4LUq3NlcQyOKi0JVtEBmUkHxwdW-e4-e1cNfMULmdMyRcv7ftH7Z7uct7Vwd4e2XHwa4L_aliEvas3TOFlIXrwoY2ST21lLfRCAJUOMI2bSbFJbxzc-yQVzv3oGvo4M08coxj4tqkw7TEVGsI7ohiv9q4lIThefOLmbJBA3nNHSCVCJ4Fpen8y9JyYnZnD1x7ypiapAYY3DiUMllHbc7HxQSGbv0GtgI-LO8wstiQGid1Ja3i5xzEPtBjVWtT3r3La3Z605IORqJe6_IuHnbRMJT4OYJ0VN-iJsDSww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
با حاضر نشدن بازیکنان مس رفسنجان در بازی امروز مقابل صنعت‌نفت درپلی‌آف‌لیگ‌برتر؛ بازی سه - هیچ به سودصنعت‌نفت شد و تیم محبوب آبادان بار دیگر به رقابت‌های لیگ برتر خلیج فارس صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/27806" target="_blank">📅 20:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27805">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUTF-EiWQU3L54rMyyyTKj5Nk5fDcFNfvHQZtTcLxKo8BPMFQm62K0XPsFrDrspvPhVT4eAr50Ven7w3K-LqAmglrQfHYThw61IXhSgr81Pz1MPy_n-MAFJY9vzPIJGL7478VSlYv0yFX8ApKipW-TSO9miKgbW7cy3fTt__acAcSS9GN21cVDd0OmTrOXpRYR3vhZCB_Kgdg4kdGG5Pj4uYj1KB_dH3lI-ISn0kUjS2_Hh5k0ts1XFvRxdy22_b2u8s2Owx1K9eWVb742EmzdxHwXrNBJb6vY2hnkeJZRyBjXzQ6BW6M0xn4njQzwBJPlfC4IC2k-fvLEN9DsY6yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید خبر پرشیانا درباره‌محمدجواد حسین نژاد توسط‌مدیرعامل‌تیم‌پرسپولیس: مذاکره کردیم. رقمی خیلی‌بالاتر دومیلیون‌دلار به ما گفتند اما چیزی که برامون مهم بود این بود که خودِ حسین نژاد هیچ علاقه‌‌ای به این‌انتقال نداشت و بما پاسخ منفی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/27805" target="_blank">📅 20:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27804">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLwMJYN-6iJM_WtViJr81jUsHkvO6SPlbWcfqex2t5bYgBFpUpUtR20uemjzTVgmWMs_pYfdzaj-RfOBLDUWOS-uuO1tAJHqJyGOE9Kvyb4Necv6oTVkjcWbjNXJ5BWXoz2I8exNjygIPzQQG3VGPi87L1TDOuar0EvthKDBbkGMZ2HzY-Y8ArGTIVWevtodMosbEbETeMgqUsNzqYvTViBvebnW5tsp-jgLkUNj3IRLjmGla63RNis8Ffz4xQMZ6WwRxImaQTmb1MUfuzAbVvhWQSdaIlZ0XkS87Z-FqoOGp49pLfARCFha9ExJfThjE17QLGFKwocnY8lFjIlVaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
در جذاب ترین دیدار دوستانه امروز؛
تیم منچستریونایتدِ مدل کریک مقابل شاگردان روبن آموریم در آث میلان با نتیجه چهار بر شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/27804" target="_blank">📅 20:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27803">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCMcvJ3f7r3_FgrpNZziIj7DfAXia0v7e2ALPAAc7Vhc8vChGIHx-YMM1tK_PQHQEBQ9Li4iTjfeCaTS54zszaxxUIPANSUONjYgYH0nZ204Z-F8HAekaxc7mJwLSRpKtNl8ngUfNm8MX9coXNj5sFXZFUkiisrqEHODmzKnc8nTnKmhd86FDS4i4KgqFNwFG6YAtxkyd8tndJMW-l6qkcmZiy9bUrhCo3In2UwY38JlXcF0d31pUQkw--IGwlvrsgGWOIHa6Zrb99_0Wuy6ud4PJnMJg95nOMdzh9vsEHMv3yd2h1YxlrqWNzmwRsJU2s5VEy7pUyi--yRZb9cMvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی و شرط بندی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
تا 20%برگشت باخت هفتگی
🎁
10% شارژ اضافی روی شارژ دلاری
🎁
و15%و20%شارژ اضافی نقدی برای 3 واریز اول هر روز
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
sg24
🎯
ادرس بدون فیلتر سایت:
✅
https://mafbet.com/fa/?btag=260368
✔️
کانال تلگرام سایت:
👑
https://t.me/+8eCDvbzSV5JlZjlk</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/27803" target="_blank">📅 20:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27802">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35ec76430d.mp4?token=AsjNPnIGArbKN-FBc57ykdSKqIvj5FyY8CWkSllb-R8voMq3yD_T5JZLUoXesoKqdQs7PW_eNyrmMWNgg-xr_Jnb5cxL336kyun01V5h62XaqxWArcbRES5ptnK7OBCkFvupiuJ0Hk7zO6sV40S_ulGF1L-BBwEuDlmcrnIGkBXefhkED4LACG9ph10KOWXeUcd9QEG6XSvJIsQRZWV0MhiJnspGqdwBgY4fEDRlaiXKL2CMgXeA_O6FM3xDITsP7nzUGbHJGUQzpLhvf4UFhdhEjDeLcxIfcXtKq25e_bN9vaPmOaxMFJYbRaRJFq-mHCiMU6rOAt23P-w4uQLzhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35ec76430d.mp4?token=AsjNPnIGArbKN-FBc57ykdSKqIvj5FyY8CWkSllb-R8voMq3yD_T5JZLUoXesoKqdQs7PW_eNyrmMWNgg-xr_Jnb5cxL336kyun01V5h62XaqxWArcbRES5ptnK7OBCkFvupiuJ0Hk7zO6sV40S_ulGF1L-BBwEuDlmcrnIGkBXefhkED4LACG9ph10KOWXeUcd9QEG6XSvJIsQRZWV0MhiJnspGqdwBgY4fEDRlaiXKL2CMgXeA_O6FM3xDITsP7nzUGbHJGUQzpLhvf4UFhdhEjDeLcxIfcXtKq25e_bN9vaPmOaxMFJYbRaRJFq-mHCiMU6rOAt23P-w4uQLzhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل‌اول‌پرسپولیس به شمس آذر قزوین توسط محمد مهدی محبی در دقیقه 10 روی سانتر جلالی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/27802" target="_blank">📅 19:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27801">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5771e6cffe.mp4?token=gddKcZe0zTnJWC44JKkmqn6u1m1hoshVtvVVkBT-_WwGbfHYgEYVozreun2hBe-dRHD2E1By6Yjl7BizLRgIG5BEvi7UuWB8YHqXoQyxZYUmBF-LdqBHbwzUfg-l805MHS3k3-QjOEfJe50o_CXG0brOyG7d4GFCg_7o-3JagVLKXlQgF4TON0Bc7TxOvliB6fojUk7IxcqU9UKc4haOMbu3vgSUWhU2qtfHSivrlhuImiEmLZV5ZSzuJsVXUWpcmjkplHbMZIgkRa9uomWmJYoEjWVIi9CWr8FKhTeypUSsTm-8AX98hUh5z0o3RYVOS77DYO_sx2BLumZ1Ly8DQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5771e6cffe.mp4?token=gddKcZe0zTnJWC44JKkmqn6u1m1hoshVtvVVkBT-_WwGbfHYgEYVozreun2hBe-dRHD2E1By6Yjl7BizLRgIG5BEvi7UuWB8YHqXoQyxZYUmBF-LdqBHbwzUfg-l805MHS3k3-QjOEfJe50o_CXG0brOyG7d4GFCg_7o-3JagVLKXlQgF4TON0Bc7TxOvliB6fojUk7IxcqU9UKc4haOMbu3vgSUWhU2qtfHSivrlhuImiEmLZV5ZSzuJsVXUWpcmjkplHbMZIgkRa9uomWmJYoEjWVIi9CWr8FKhTeypUSsTm-8AX98hUh5z0o3RYVOS77DYO_sx2BLumZ1Ly8DQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل‌اول‌پرسپولیس به شمس آذر قزوین توسط محمد مهدی محبی در دقیقه 10 روی سانتر جلالی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/27801" target="_blank">📅 19:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27800">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ab0f14bad.mp4?token=qrQDy6kItnwkHatWqIPLqfOekxlJHEnQ12c-E2cl0LJ5KxPL_38oejRul6Oq2V48wYub_8hM0OcKbXO-nXrrAIuyeIRsUpfUaqVZUt7d_qNRVnnvOnfR-JVUYPrYCATsjORwh5rj9HRq0pZUQu5B7ma6cuk9q9o2xJta2v0QTz7rqTHV5DNcFfhi5vGd8uJZ8PMUAaIVcL03GdOPiiNSWsJDqH5MsdXiCTtTdaaOAsdT17eFooVOXHTO-ftJzY79rDiladImwL-hu-R1S8C3QeDoiP6vY3wBWAa6N34ck0Cf0Lk3ObB-BVfj54NSxg_WvVGobjAD4oSXpx8DtlqPpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ab0f14bad.mp4?token=qrQDy6kItnwkHatWqIPLqfOekxlJHEnQ12c-E2cl0LJ5KxPL_38oejRul6Oq2V48wYub_8hM0OcKbXO-nXrrAIuyeIRsUpfUaqVZUt7d_qNRVnnvOnfR-JVUYPrYCATsjORwh5rj9HRq0pZUQu5B7ma6cuk9q9o2xJta2v0QTz7rqTHV5DNcFfhi5vGd8uJZ8PMUAaIVcL03GdOPiiNSWsJDqH5MsdXiCTtTdaaOAsdT17eFooVOXHTO-ftJzY79rDiladImwL-hu-R1S8C3QeDoiP6vY3wBWAa6N34ck0Cf0Lk3ObB-BVfj54NSxg_WvVGobjAD4oSXpx8DtlqPpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ محمد جواد حسین نژاد دقایقی قبل ضمن تشکر از باشگاه پرسپولیس آفر این تیم رو ردکرد و به‌پیمان‌حدادی مدیرعامل‌سرخپوشان اعلام کرده که فعلا قصد نداره به لیگ برتر ایران برگرده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/27800" target="_blank">📅 19:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27799">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06d9e3d33.mp4?token=O5TXeC-1v34JoT4Y6uyq1b-pKHM-ZcXDBusueOGLkQriyvG_-pG2PYMkTdZbgBRicbMhvEQjskqgYieJeNcMTFtWEoXze-YH8__aWxXZ0gTQ5bgb9k9PDOXYC-r9tr7mG6zWjHaYkVU38Yr8jsjVg5nHbo4srcsUbYagmKDHNeghklh0pfmAiRFkQP5iLaSZqYqL_Ry5qo27ByNCPMwAL5ujE05gZ_LqWskkXgqcKDfeJFKrSsDFXr0v-sEWLJdUcGFCJNVqJlBBllYOtPQLB_qQyPIJ7dwC5_3w_W61gKevNzGl_K0EWERce1p6bj5_rJtFBSIvLbzKdo-ZEkvGUQ2DhK7PeXlwnYD4_KJ_utIaJuO72aX8wMJBl9_tZQWajDfrLpmdGucFp7mOi5WFiUIkCNd0yNzTa3l1yoNGNAa0wsRA3x3ILTRPTFy0lMZGAEcXPpJf8860USNH2B9N4jvDrqQMvya88ExQuvdPv4MaI5lTbeClQ4mO8NlekjDT3BsN2G9kf8V3afDWrgOMuuNkEr-MIf2mu-QYpCIH-Bh1EbIiykiFaBDPeTn47DvXyvh8RVsP1Ld5_BSb5mwTRDYJFQ7LE38-BcHjqD_YVxMiIYuLXGKM5MqYGahqxw_h7cr_zEpAVH9VoLjuv4UIXmDE-k6yXb_gpyIT9wxnnoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06d9e3d33.mp4?token=O5TXeC-1v34JoT4Y6uyq1b-pKHM-ZcXDBusueOGLkQriyvG_-pG2PYMkTdZbgBRicbMhvEQjskqgYieJeNcMTFtWEoXze-YH8__aWxXZ0gTQ5bgb9k9PDOXYC-r9tr7mG6zWjHaYkVU38Yr8jsjVg5nHbo4srcsUbYagmKDHNeghklh0pfmAiRFkQP5iLaSZqYqL_Ry5qo27ByNCPMwAL5ujE05gZ_LqWskkXgqcKDfeJFKrSsDFXr0v-sEWLJdUcGFCJNVqJlBBllYOtPQLB_qQyPIJ7dwC5_3w_W61gKevNzGl_K0EWERce1p6bj5_rJtFBSIvLbzKdo-ZEkvGUQ2DhK7PeXlwnYD4_KJ_utIaJuO72aX8wMJBl9_tZQWajDfrLpmdGucFp7mOi5WFiUIkCNd0yNzTa3l1yoNGNAa0wsRA3x3ILTRPTFy0lMZGAEcXPpJf8860USNH2B9N4jvDrqQMvya88ExQuvdPv4MaI5lTbeClQ4mO8NlekjDT3BsN2G9kf8V3afDWrgOMuuNkEr-MIf2mu-QYpCIH-Bh1EbIiykiFaBDPeTn47DvXyvh8RVsP1Ld5_BSb5mwTRDYJFQ7LE38-BcHjqD_YVxMiIYuLXGKM5MqYGahqxw_h7cr_zEpAVH9VoLjuv4UIXmDE-k6yXb_gpyIT9wxnnoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ درخصوص وضعیت محمد قربانی زیاد پرسیدید؛ به‌محض‌اینکه باشگاه پرسپولیس مبلغ رضایت‌نامه قربانی رو به حساب الوحده پرداخت کنه هم چون دانیال ایری در کانال خواهیم گفت... فعلا تا جایی که میدونیم بانک‌شهر بودجه رو داده مدیریت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/27799" target="_blank">📅 19:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27798">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwwxiLBEmGJM5M0F3hlYrJTbKteoW7QISZUxK6S_dSDre9m728n7OnvomQJWsXW1f7g5_R7of9qJb6mS_uovLHxf6VpxE9zZRNEFNn4TXnRsfsHDGACFMwnfdbEIj02nMHA5VcTVD_KaXgFIfnYKL9sfcFRGfiGYkfbeBcpZHiEzR9CXGaCeTq8Lx6huld3IPxwWxhpD3zvbWV8AkPgaTf2C0BTU5d_SGIndEmInt7q7QG8ynbpu_W0l95e8ycKtcCmuBA6CWCcKq2WoAP2O2wg1v9N_doNq6HGiGP2kXf-40uJJ1woiQtTmri2H14rsr-nX9SfxjcC_whFerJ-7OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ ترکیب تیم پرسپولیس برای دیدار امشب با شمس آذر؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/27798" target="_blank">📅 18:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27797">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQ-RToRVSJ-EYwfyrES3lTVXct56j4XbZofUlywquQh3A8GCbYR3j2GNm3zOJ4dWSb1fXl0_sFySt4R6avGclaEP1eI8u6cWW0D6JFsw_Kt-4RcBdI6TvFHgz3fYLTUQq6CA00pplJ2n8eNDjImkOEFtbLi-vcECCJUL5Mb5BKXM2B5goCmlY3U2yQyRKWmxS0s6t1idH5sgvFBz42Oyp-wgZ-qJtGFwl9e3h-EPTG1L7WctCE2rnpnz4XPEpHRPW6U0d4x1U6hYEU9Db0SSUAv2qXGEz0zH_m_H-xChBLwzNcuKCjs3AJAba4XS-gh4ROjQ2QYg-4cih2Gkz6lQKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب احتمالی پرسپولیس برای دیدار امشب با شمس آذر قزوین درهفته‌نخست رقابت‌های لیگ‌برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/27797" target="_blank">📅 18:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27796">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyrbH20wKI6cVf_Zal9gvIlXYZ8odIHIDa2dbedJHdKyQ63R0ITOjpF3eXD1lxUQm5L_MRSVQibEMvw2jruemm7Xzdc3sK9kEb8GpdcLjUOWXmfAnJnpm7Qh5V96MbiDxn4ozaracXZJj1br3LHzkQabAqlLiis4381XzULpU4FzkSpnxBkCIRPFeAJ4Q902XdEjTb5We5WUAlRH5pM0AJx8qXsOFl0u6i7cxo2-wdN2HNG5XS4fJdXRg2ZDhxxOHWgWD-1n0ee4E4X9M9BWt-AW1FTida1XU4-DnnFR3O-wporz1ElittoML7i-LZb1ZxHfvMKrnSwQYPcQ8LsH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط کارشناسان حقوقی‌فوتبال: آسانی مشکلی برای‌بازی‌کردن ندارد.
🔵
هوشنگ نصیر زاده و رسول باختر دو کارشناس حقوقی فوتبال: بازی‌کردن یاسر آسانی برای استقلال کاملا قانونی است. درصورتیکه قرارداد او در فیفا و سازمان لیگ فسخ میشد و قرارداد…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/27796" target="_blank">📅 18:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27795">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gy9x70o3bUeC0qtrCqp0RAp0mKKGR5AAxlymHTqselgtDpn-KfJTIXNglTrZKLEvWwc61Ia8K6SyHQc3B-1b0IrjGxHpZreMgf9BM3iGb-5ZDiVEsDCFEzV2SwPXIh-fo9yq1OuP1ZbEtfa1bJF6DWiUlAmDe7zX7tpvSvN_fIioYbbv5gqWKJlnSJOe-yqS08Oxak8MXXNxAHUfyh2VIpVX8KUJdJBOdaNhAxYly6WpLrymLptSd1vjIjRjL2rRVD8U-eg5zI1GOnlfbZmCaQCGILSC4molGawkdq6y_zWlNCArFYkkv7LH67vHzwmgfHOYNQVVajI9m3bqVSCXWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛مدیربرنامه‌های‌محمدقربانی دقایقی قبل به پیمان‌حدادی‌مدیرعامل پرسپولیس اعلام کرده باشگاه الوحده رو راضی میکنه که با همون 800 هزار دلار رضایت نامه قربانی رو بگیرد. منتها این پول باید همین امروز واریز شود تا کار انتقال سخت نشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/27795" target="_blank">📅 17:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27793">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmI8s1kGmVIjwEnevwp_hALYN-woNCNebO1e0ZIwLokK9Wzi9y9YXgiR9VRW5IL5k8c8pgB0pY0jl9bznIIVSyY9uiHvw5QXNy3A147fa2XPC_tYngkYr8uxgqERKjhx2v6nZFFkk7E195ELU-GaDolXhefjG0muBRKmZ867I7Ns8PtxxQjC-41olek8c43twLr9je5j1OsPCq-DdXpuABrUIx8YfRV-xdWAKoaPjw1WXK1sgnQxS-JnY8r8oAk9xw3ma7YyBKPL4Mq3XOl03H8TpPO-kkqmmUKQ3NCNqQtDjVYycdlJ_Su0Vb3VoHNP0Xolvxqhgx5KKIKQ6_TW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HEuPofLfKCWpxaUzt8qbD_btDypRCI25VlNGa1upkKfzF3aC-J39EVuL2x_4xfYyab6pkod4d3BjqIRK2SwHyCuMW9kl6vePjJ1uMDylBSir8Y6Nm_iwpShhr5vGOMsw1Bnp_Y6JvoTPxzqA0v-3addYoN7CcZ6kgizqm3l2wnPVhupC4fA4g3p543i9HN8ppc8Rt1a1hQ_MnWWw4gzYEFIKOSkQXrChgVERiXgfj0pZxu7TCiVNQrXEFlGrPoVAwWIpfQ6L8iSR22J-7j-DQEarDUr2HQ5ITvJSjPuynXtwl4Fy_J7a6Fugiz2eM5KOwsNhkkEJwXH7y9FQa1wZ7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ویدیویی از گوهر خانوم که رامین رضاییان بزرگ قصد داشتهه تو امریکا ترتیبش رو بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/27793" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27792">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4ce395aae.mp4?token=T60qcUdP3ZHpO05LNiE080arFxVDTy-G6j5KTeDiJW7vn9I85p3b8sfHZXHBQG7tOK5BA47NQb875bkq53uef5wDdtF8JvOt9oPzHw1I_73KiWjGuYH7zA4EJhkNruzeIvy7SnOW5Cpe07dpU0n9Wj7297w_7V9Qn9AlKFaUASRFFlbj4X7Y70BOw3WHae67P6iasZZbiItsDemg68D8WZfUmuvwZYVi2UH0v28Rh88U4DSNLvLYLSmGefEnwqB2TdP5WYB2G0ohEXzoN0upuquW7LBbLR378c6lbD8OIscT3LuEH935UsTwJzaz_iuUswZLSWqS0MiD4FOrJFp9Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4ce395aae.mp4?token=T60qcUdP3ZHpO05LNiE080arFxVDTy-G6j5KTeDiJW7vn9I85p3b8sfHZXHBQG7tOK5BA47NQb875bkq53uef5wDdtF8JvOt9oPzHw1I_73KiWjGuYH7zA4EJhkNruzeIvy7SnOW5Cpe07dpU0n9Wj7297w_7V9Qn9AlKFaUASRFFlbj4X7Y70BOw3WHae67P6iasZZbiItsDemg68D8WZfUmuvwZYVi2UH0v28Rh88U4DSNLvLYLSmGefEnwqB2TdP5WYB2G0ohEXzoN0upuquW7LBbLR378c6lbD8OIscT3LuEH935UsTwJzaz_iuUswZLSWqS0MiD4FOrJFp9Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«گوهر فرشاد» بازیگر دورگه ایرانی-آمریکایی: رامین‌رضاییان‌جلودوربین‌ها گریه‌میکرد و ادعا میکرد که حاضره برای مردم جونش‌روهم‌از دست بده اما در دایرکت من درخواست‌های زشت و مثبت 18 داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/27792" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27791">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzA5Ep8Mm-v34k0gN8zg5W9Q2fQjztM16DnbD6ky-u4M8y_CIxlyFH9wQ9_fN7etj-s0k5FNo2_9C5Di1dY8wo-9rqkT8qtYkxu4euXMq7GrzhuXuNKdONNHA6m-qm0igSTDqfPRJ7yp4CSMAM_X8LUW9OXqHWpDzJdk-ofNXw8T9N2B-Q-LWmwZf2iuuhlkYO5Y3ozwCib9lfEcMJgWFw6Pf3-lrArH6fVuppXm0zYmKOcbI-bY1_FQZ1IfTGmuX8mMroXVmlt8BNNGDVu8t9AHaZu0E7EJeGseuRJqBI3O41CGOcLv6cOGJ-RRlL50CL-TfFeXPgW4BPLZZOu9Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نیمار ستاره برزیلی:
من آدم رقابت‌طلبی هستم. همیشه دلم‌میخواد برنده‌بشم و تمام توانم رو میذارم. گل میزنم، پاس گل میدم، به تیم کمک میکنم، بحث میکنم، در نهایت اگه هیچکدوم نشد فحش میدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/27791" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27790">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrEkvqdF6bJhGOPLTgAlQwjk2HvF_yJy-uI8WiCtzUZ5M8jxzGCistg48qJgTcZ5IvDImqn6uIglT9mCQHgFBHXKmeNByCeoNCdcZ2zf4JGSqW5GxaFLB7KjLdvwoRvDuie1pm5lSjFZG1SCWleXs1W5D2z_drJThWCtJrsALr2CA85SyM7bBh6iOuafDm1BSf8Ljg6ayHTImOn9ffUPD5SEXf7z-LpCfO_X1jqmwq4J1t_YmeYkWNFttqmEdEzMhjtTGDs1_6bTzDYgI2h6IME83f5Ya-5OSuoh4ir7dMkCYEADoFoD2ac87MtdYqvdatiSRzOomg3exONYC539dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هفته اول لیگ برتر ایران
🇮🇷
شمس آذر
🆚
پرسپولیس
🇮🇷
🗓
شنبه ساعت ۱۹:۳۰
🔴
انواع آپشن پیش‌بینی برای این بازی
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/27790" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27789">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d76ee0536f.mp4?token=nCHIgSt7sNq0s_styE3MNKTrz8At1mijBgBGc9WlD5jJOaPPFRxIr3mLjlSyBu-9ls7W_pH6Z85tLLZAkT-vX8RdInspoyHYDiwcDMqYK0-HKvcI8U-G6LPOCq_tPt9FvOM5K6_hOAdS4p8nj3rGmOAci-5oHhzNu6Tha1zi-YeEW1Un71DRzw7Y-5R_tlgjW57DuTeXp3lmJbl9_YGNzJ8ltW2YfcfvJl0BVOf2ObHVlWA5zMWKQU3xiHv2JYTnxab1AlgyZgrbLjaWEScW7de3GOdDiYhttVEb88bifwpgthl8SwK4oRRYGJRiDLuudV99CSA-qV-jyTIPnt78VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d76ee0536f.mp4?token=nCHIgSt7sNq0s_styE3MNKTrz8At1mijBgBGc9WlD5jJOaPPFRxIr3mLjlSyBu-9ls7W_pH6Z85tLLZAkT-vX8RdInspoyHYDiwcDMqYK0-HKvcI8U-G6LPOCq_tPt9FvOM5K6_hOAdS4p8nj3rGmOAci-5oHhzNu6Tha1zi-YeEW1Un71DRzw7Y-5R_tlgjW57DuTeXp3lmJbl9_YGNzJ8ltW2YfcfvJl0BVOf2ObHVlWA5zMWKQU3xiHv2JYTnxab1AlgyZgrbLjaWEScW7de3GOdDiYhttVEb88bifwpgthl8SwK4oRRYGJRiDLuudV99CSA-qV-jyTIPnt78VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«گوهر فرشاد» بازیگر دورگه ایرانی-آمریکایی: رامین‌رضاییان‌جلودوربین‌ها گریه‌میکرد و ادعا میکرد که حاضره برای مردم جونش‌روهم‌از دست بده اما در دایرکت من درخواست‌های زشت و مثبت 18 داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/27789" target="_blank">📅 17:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27788">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط کارشناسان حقوقی‌فوتبال: آسانی مشکلی برای‌بازی‌کردن ندارد.
🔵
هوشنگ نصیر زاده و رسول باختر دو کارشناس حقوقی فوتبال: بازی‌کردن یاسر آسانی برای استقلال کاملا قانونی است. درصورتیکه قرارداد او در فیفا و سازمان لیگ فسخ میشد و قرارداد…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/27788" target="_blank">📅 16:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27787">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLdsD3WJb8Qo27hADt7CHBrg2Il-bULJ6OfUvsKYzhvbeZYKdg4VQIYQTKVinOx0zNoq1kZ_Rj8V7R_B3EZ_0GXHRRqA7aiJZCoSb2bjnPckFCv41WgNTBf_pHoC7EL0xqy01oph2iKGDT3LC7ob1EI_bvq6utURkH7XBJSkrn9IGdr6V7ZRZyI_YSd7sYuaX5yr17NPRjQmoezQGW4IePARAxR9NNozFMtzUg7OAYCtv3U1I10U8qDVs-Vn9MofUNxtN7-ubjBsFedRA8qcdIfI6xdPMFGdHHs6DVFYxHp--FEODItbEqcRDdlJEmK1H_JhdovgcXr2TiqFATIbYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان بزرگ تو آنتن زنده گفت تو امریکا حاضره بوده که حتی برای مردم ایران جونش رو هم بده اما گویا ما بین بازی‌ها بفکر عشق و حال خودش بوده و خواسته همونجا ترتیب این بازیگره رو بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/27787" target="_blank">📅 16:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27786">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F992kacYh7ky0eE9OFTD1ytrZLglZlO-_RlJOokYqnjKdl8C3gg6FZ98zB03x40846iXvvQt5aCgeEwm_56_3XAEtRqO7XP2SQzzHtCuWQEZCeH-eNoZ4hXOtd6_FByOkyDvrJh3afMHjC_Ds96S_wNo6HQibmo88vjV1To5WMv3uWabS6PES1Tn9tPxcWLAOgguoXHqi4Kgx8dOmotO4jClmSay2-lznusU5CyQPeK_wfCYUL33gdqK4bKT8VrmgHNQcTjdtAXzcTq7RRd5GLugExLrY2i5zlIT8O0kUX_OugvwEnfZ-TOrJDZ5yopsT1GBNmTXPETxZde6jHOkBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ اوایل هفته‌آینده‌هلدینگ‌خلیج‌فارس مدیرعامل جدید باشگاه‌استقلال روانتخاب خواهد کرد. محمد رجائیان مدیرعامل‌سابق آلومینیوم‌یکی‌ازگزینه‌های‌تاجرنیاست و درصورتی که هلدینگ تایید کنه مدیرعامل میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/27786" target="_blank">📅 16:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27785">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbcuHMmXQGF2AQdFHjuQ20Wk3JXFkwvK1iccFC5vQAXZbKtsjMpn5xQHgQXUqh6JfuRScENxFatjkAoRZodEwZOcP7S9-naBpl7T-5dUn1RxUBx5X758LthC9xt4rFxZOyRvNLyfG1pX_FxoPhEOFsnm-C2kicEYTW98WBeWc11M3zigSYeWwh2q79ayzKgQYVyuFi_zJR1xXOMEegOkRW-hTutwmKFKS08e2urHllm28Yg6_-7csT168Qz4_JH1hBo-0VsR2k7ugCA_5i0l0a0KmOPXWbTW8m_x_NOP1IT1zgFv0N_SdZPmaJPUw3FTxlbv3hLj64nLoT92g7xoKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب احتمالی پرسپولیس برای دیدار امشب با شمس آذر قزوین درهفته‌نخست رقابت‌های لیگ‌برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/27785" target="_blank">📅 15:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27784">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3GplRFnQd5WPWeCu6vvdTzDNnU4iKLwAIJF-VFm7J2dqFnna-kH2aiUqojD9NDaE1u9ve8io9fS0Zblq2xOSfiaH3XslMvGdEhpbXRxjn86vu2vz0kCsHJutXCrOT2CY6WelNN3vmeJ-wUj9KoWDDKCFJZUb-54R9GEqn4ctIxY3Adz1miFtQRBP50sT9o00f9VO4hep-ZuA50UaxMC5L3fG_hIWmDphPeskzN07LOi73kGumL7co9Yq0GVRgwnSqUe5O7dRy6MQwOfJRnXh-YE47DqZ-IICkkGtKPlYWDasQA6I3A265Pei0hzufTyLt33bQBJ6zyQ0LwATQZ7Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خانمی به اسم‌«گوهر فرشاد» مدعی شده رامین رضاییان تو دایرکتش‌درخواست‌سکس داشته و از او خواسته در ازای دریافت مبلغی باهاش سکس کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/27784" target="_blank">📅 15:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27783">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4420878c6f.mp4?token=CWyjJrpRFHMO3ZBHoYpO7trlbSVeQtG2o0unuZLFBoJXwYmCDP0W0UBAiBGM4caHF4xpUIi6J95VpVXugYRwVmHEx4APzW38m8vZVMW8-pQ_iSXu3iN1bArvUNnDK7xDqiVKbaoqxw-WqsFoaK17F7S7Bc54gzCdLvYYn9ytmQmcgiZzOS_Nz20A5bbqOdUNzM8V3RiOmCl4KgPZGX6an-yhCsOJ7FudSrzzvlkenf3JM2j7PBJMz5WZ0DwpcfFZrMBiDJz4FksRM0TQl0hdr_b2lFOZjcgxLqBb4rHjwV3jmgQBvT2pQTFSMwMh6yOC02A9b9SXEim_YPbZ1Kb7Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4420878c6f.mp4?token=CWyjJrpRFHMO3ZBHoYpO7trlbSVeQtG2o0unuZLFBoJXwYmCDP0W0UBAiBGM4caHF4xpUIi6J95VpVXugYRwVmHEx4APzW38m8vZVMW8-pQ_iSXu3iN1bArvUNnDK7xDqiVKbaoqxw-WqsFoaK17F7S7Bc54gzCdLvYYn9ytmQmcgiZzOS_Nz20A5bbqOdUNzM8V3RiOmCl4KgPZGX6an-yhCsOJ7FudSrzzvlkenf3JM2j7PBJMz5WZ0DwpcfFZrMBiDJz4FksRM0TQl0hdr_b2lFOZjcgxLqBb4rHjwV3jmgQBvT2pQTFSMwMh6yOC02A9b9SXEim_YPbZ1Kb7Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
دیشب‌عروسی‌هرناندزمدافع‌فرانسوی PSG بوده که حماسه‌ها‌خلق‌کرد. امباپه از دیکتاتور به گاو چرون تبدیل شد، حکیمی دی‌جی شد و دمبله خواننده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/27783" target="_blank">📅 14:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27782">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AObI6SftixGwqEPLlaYX2cuc6oPNJjlYNuWQKXhX5ro0gxY0m0kkBvgCPToUT_FnDPPDyzzalIxewtpT1vVGPoCrnwlp_r4CNe8Wmr3jHZM3X_tbI-kxYgFxVgBDxYYONMWBwrJ4Nl06oXVQxCUf17Jynq9FxXGqKugHn3xf5DAxyPPW_1nS25EGBMw-Nb4kmAndy7MCYvkaAOVQyKUYvWLwWbq4xh_VeAlfG3ekPWW3E02pjKzGwjiMz31SBgiA4L6oTUvGT3jn2QBpAVB8jRl8bIXMgzvz3OCJ5OKLse_Fw5m80CFOfrXGwXMuHG-4jyn-XY_TGxdOQzsQDQYZnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
ویدیو لبخونیِ لیونل مسی فوق ستاره اینتر میامی که خیلی‌هم وایرال‌شده مسی به پسرش متئو میگه: متئو دیگه‌چی‌میخوای؟ پول ندارم دیگه همون هات داگی که خوردی بسه دیگه به‌همون راضی باش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/27782" target="_blank">📅 13:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27780">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kze4zntFW01T1zHhI9H6ZPz0f6lSV4g4JwqrwoFQHdX70zMSrdqIQdr9JVyy26tTkTf0EoRpu2Xu3o3lzwrK9cCUQbp7jpajsmFjUz0OTBCQOcVtPmB7nxcWBmGIUl2i7Igm2GK592WkNRXWHyERly8yFZSLyjxGbaqIVbW_zH9NbWIpJLo9VgPoDw8eUrlDMVP6EJ3DQNA6KuGXnPSMxuUHthi0S5PqJdiWDx0RpJABamr2BqYggUb3KyZ52isyOvQ_aaaTaP-sgpH5DaNCXk1Dm23b7RgsfdBoAozWTmQt0rBw4rdQm1tycaWnMCHyt28tuJHX-tvUnKQnjQEpkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/27780" target="_blank">📅 13:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27779">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">📊
🔵
سعید سحرخیزان، اسماعیل قلی‌زاده و صالح حردانی بانمرات 8.8، 8.6 و 8.1 سه‌بازیکن‌برتر دیدار امشب استقلال مقابل مس شهر بابک شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/27779" target="_blank">📅 13:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27778">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46566583a.mp4?token=nGCFCVRJbX5IGx4ao0B-Krm_mH4Axajo80mwgSzpxkLC7WflhqNy1lFQcaaMxHvOP9NnR5DkOFkkGPsLTUNY_ImmlOesIFjvJK9MnSjdRZXdR0mx7UFbboZjzvYSYbcnRCZvdlE0Ftm54fIR8ZAjKLXo-Be6hsaf5Z-uENGjwH8aeIDib4pwdC2Fm4n9-RXNhYVhdCmua2oD_R32e6M56Anzcfd3bVtbnvdtFS5AzKwvBfoV_sKRQz86XtiiCKhm_JmVBeTABFYwuuFoNxnftW4MplUp4UU867XHPHKWrgvUA2JX6GFxG-v2pTmaSZm87qYrcVQfWgBLF9F2emVBjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46566583a.mp4?token=nGCFCVRJbX5IGx4ao0B-Krm_mH4Axajo80mwgSzpxkLC7WflhqNy1lFQcaaMxHvOP9NnR5DkOFkkGPsLTUNY_ImmlOesIFjvJK9MnSjdRZXdR0mx7UFbboZjzvYSYbcnRCZvdlE0Ftm54fIR8ZAjKLXo-Be6hsaf5Z-uENGjwH8aeIDib4pwdC2Fm4n9-RXNhYVhdCmua2oD_R32e6M56Anzcfd3bVtbnvdtFS5AzKwvBfoV_sKRQz86XtiiCKhm_JmVBeTABFYwuuFoNxnftW4MplUp4UU867XHPHKWrgvUA2JX6GFxG-v2pTmaSZm87qYrcVQfWgBLF9F2emVBjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇪🇸
رومانو هم‌تاییدکرد؛ فران تورس با عقد قرار دادی 4 ساله از بارسلونا به PSG پیوست. پاریسی‌ها 55 میلیون یورو بابت این انتقال پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/27778" target="_blank">📅 12:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27777">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoAVNLYJsQhbzLOxfM1Jb4DybSW85ddkOMYXDOuJwAsGHbyBTN0rC6bDxbS9C4XKQhPqFJgi2KpQXOy830FLgMvqSrGaakoitL5CnKk4MdF6xiUX8sWHUmZsIJeNvtPCeYthiLnGtG-KTrAWhvqMwUURFcS7AKUfY7eCYmOaufyTHUG4al0IscZ0F37Zr5OPBg5p-YYmWL8Ikqy0h-7iv_njKDoysj85SXzwmqNSetUDog1c5l489YPSyi2CbNcNKAiyuFJvFk7lTCxQp8DzvOv0pGg57KCyLWeGhm18BudogxJDtLQruREf4JemncTcgKstZoCUrploW9H2MQwq9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مدیرعامل بانک‌شهر فرداصبح بودجه لازم رو برای جذب محمد قربانی دراختیار باشگاه پرسپولیس قرار خواهد داد. مدیریت‌باشگاه پرسپولیس‌آماده‌اندتاسقف 800 هزار دلار برای محمدقربانی هزینه‌کنند. این احتمال هست که مدیریت الوحده یه مقداری مبلغ…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/27777" target="_blank">📅 12:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27776">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5fwZgAvzZuWdytjYMM-wL92SxCttp2nQims3sD5KLqVecMQaOnxqv_uHwYeR21Ja810eqLS3HN5T-ygljZT_6inseDIRaZPA0iHSZdUA8wx_AtHAR9JZB2gR3vAmrXipdOd6kumLLGKm645uTIvhfBhTxxU8x2qvmlI7ETuiiwPoBowIfZBhJI-Fmniz5uel6HdatuUqtoQoEysK_5Jmqj-6jqvSAhxP1_p-Uw7OYXdIom6Z7JlCWC98I69Etp6RhG1ZobpNAk-6ZxL5L1sHMbdH6tS1lVERLPt1rZMeeT1JvipGP37WbsiBpXT3mq5TV7crQyjXODU20kBeu3Tpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
نتایج پنج دیدار اخیر پرسپولیس
🆚
شمس آذر؛ پرسپولیسی‌ها باچهارمین‌پیروزی متوالی مقابل شمس‌آذر فصل جدید لیگ برتر را شروع می‌کنند؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/27776" target="_blank">📅 12:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27775">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5920f02928.mp4?token=HnDu_aY5YBI4C_7w4bfWpUMHMy41oI_4IbJ6KOucYGpSK9KJy4fAf8dD0Z0x8F_OWrjqsECBUrKSxMBkziDWiudxwoCssmU4NMiLD9Bw0oMhnhxx2quvwKdDsDcONbmEQS2XBiPj9gmRjyNF04WYDSz7qJ90iZBwXdVBMou0bmhA6pynTnDEO58DW1TlBQqvEd1sU_rxgoGkVJOoeSSfl8EjsablJlLfA0A__1RYkt-ZJPeObdgqLroIDsghBNeQdZb_za4Rk6KNoRpZHz9UjpDbpJAcZXU-BMimHIBloOAeiNxi-MjGRuvsIsBpUXR1SqjP6Zup77z1GheRpQ284A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5920f02928.mp4?token=HnDu_aY5YBI4C_7w4bfWpUMHMy41oI_4IbJ6KOucYGpSK9KJy4fAf8dD0Z0x8F_OWrjqsECBUrKSxMBkziDWiudxwoCssmU4NMiLD9Bw0oMhnhxx2quvwKdDsDcONbmEQS2XBiPj9gmRjyNF04WYDSz7qJ90iZBwXdVBMou0bmhA6pynTnDEO58DW1TlBQqvEd1sU_rxgoGkVJOoeSSfl8EjsablJlLfA0A__1RYkt-ZJPeObdgqLroIDsghBNeQdZb_za4Rk6KNoRpZHz9UjpDbpJAcZXU-BMimHIBloOAeiNxi-MjGRuvsIsBpUXR1SqjP6Zup77z1GheRpQ284A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
حضور هر 3 پسر لئومسی درآکادمی اینترمیامی؛ طبق گفته نشریه‌آاس قراره که بزودی هر سه بازیکن باعقدقراردادی‌بلندمدت به آکادمی لاماسیا بپیوندند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27775" target="_blank">📅 12:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27774">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LX_fwcd0dS9ncGN7wRtOhU0h8d7_z2VHhypjDPdhBUc8eo-bLLFbafN8VtXVIgLVjzkPxgUaXMvelZHr5Uf7vTUGntQ8xGaJgSCY9RsG3JN661FYbui73zm2wN8D-BBdFDaBBUTKZ5GkiS6bnTM8sy6yQwnmVB401B0YOYYSkgu3j9bRpopgs-5F9lqL5-P9DKLLJkCncJi4SsVAtNKVNwMlQ2t6oe8ax0YeNiRqqjVspd-nSVOBbAk2Ugsa1Yntk6kYaV6m1i60NXw1Iv7pJd9FvqpFhj2TmhidkJV-MvC2rgsshK5YZU2OYkpmXgBb5bi-psFB-zh1m6mW8GHoQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛ از مصاف شاگردان تارتار با نماینده قزوین تا دوئل کلاسیک میلان و منچستر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/27774" target="_blank">📅 11:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27773">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6R22PfuRzNfVcgCN6G1sfD8CDZQ0BfbSswpR5hllVnEBBsduJ6dY6zBDzaHihRUweG6NY4o5gkhDkdLMUraTGvlaJRkfTCVPTuVqSfUQ_skKjZJ9FbE3lYqksFY6XzPASNotK6n-0kqh0SI8nmVThpEN0gamqYFTrhsckpy4j3xynTybVl6RjzCIUlOvFmfb1tM0pT1gGjLrWK2Xd4JeFKz8tvKbCuKz47jhpSnenRdsvJW_EEffd4q9-fVXbl0O4mjC5vGjDT9zm9iTxodosAPvr3A8fRZTIfNJ4fwrU2EyLy5oErysWiBYVghHYBilJR1b8B4ea8MMGzMOdYK-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال تاساعات‌آینده 25 هزار دلار به حساب جوئل کوجو واریز خواهد کرد و پرونده او نیز بسته خواهد شد. همچنین سهراب بختیاری‌زاده بخاطراینکه نازون به‌فیفا شکایت نکنه به‌مدیریت استقلال گفته مشکلی برای بازگشت نازون به جمع آبی‌ها…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/27773" target="_blank">📅 11:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27772">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eECp6p-tcD4YRbL5075kLMu24LlqxttnrcPf07pNM6HtOh11yrbACpXD5qe9iohn-v3FiEONBLgIYZlS5bL5khmhwo1w9UjkBYXdfhM0pvMmg5vVb0me6OUYt_9Cj7v-OWJzyurlxv2cDvAmBaJy4BVK6dvUqU1M_Zj3Ore07S4YuYy7FdIZE36oVShNPgk6DJyHKHMJfZjYvCma4p83YWyNEfKBL0gNCy_UjOPX8eQkG_kCSjwNn5qsNlOkD6cQWC0Zc6pFxI0zKzXoH6aXsaRKIiEzuCzq-fqJoc-sZBXddmGUSz-QZ4RN_nktktPTm4S72WbRAn7kS60UhAEzZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی_پرشیانا #فوری؛ پیغام جدید محمد قربانی به‌باشگاه‌پرسپولیس بعداز درخشس در دیدار امشب‌مقابل عجمان: پای توافقم با شما هستم. رضایت نامه ام رو بگیرید به تهران خواهم آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/27772" target="_blank">📅 11:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27771">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1Y4ssT0rrBz_wexRae9APFqZURUvSeRe0N3GqogMCVVkHGbFE95aOxLS0ohZlQuMpmeOJgumL6_cu9nIDNbgIEI4ll1xBGFhBCIQbA_hjeLSWtqbfOF_hyFnaDosgoC12YoGOYLu9QFPdaO6QGP6C1fJMLoNPw45FpC3bxtjbxo7UmgiB3EkfX5iOlfZTlyAasObUXZui6w0fThCdoDHDN6tNSEv4KHibo4xHNtfBLRZKx42dTaUjcZFYJbD9G7urACRXH0t81ifMGhxWJTweeuZe08RLVeVeEjs3xFSXpAh6ca-X6GsuIEP0MByTlOqZFXLSGFGJ8A-L6HNBISYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال و دوست دخترش در پارتی شب گذشته؛ به محض اینکه تمرین بارسا تموم میشه دست این بچه رو میگیره میبره پارتی‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/27771" target="_blank">📅 11:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27770">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebfea836a8.mp4?token=qeSuevx6Kt-AZ0gjxAjhG6HbuhuoSmMYGeAgMj-KAtp_e40_TnapEsb0178VIP8c729200pCNWMHt_mIlmVF1EkkcIJUDQ9dSJcZWbeeAfeE1jkMfRQvcHXatNhzfpHzLP_zJ2eWbUzZFNR22hKmCBzDL93tcUbdr7OFl1DiaMVgvKsuX4UeE3dlGRf6pHUXq47DWVY6dTwnHf87AlIlM5iFm6Wv6CckLuwrfuxM6BOLduMKW3_ejDXvWzU5O3PJwXHI0-ipcxRbE05y0Yq160KrEAtXphbVQHlXr76-chzFtMVtQ3gY_JMla4A7Na3S939oAfgp97qGcZe4QEJiUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebfea836a8.mp4?token=qeSuevx6Kt-AZ0gjxAjhG6HbuhuoSmMYGeAgMj-KAtp_e40_TnapEsb0178VIP8c729200pCNWMHt_mIlmVF1EkkcIJUDQ9dSJcZWbeeAfeE1jkMfRQvcHXatNhzfpHzLP_zJ2eWbUzZFNR22hKmCBzDL93tcUbdr7OFl1DiaMVgvKsuX4UeE3dlGRf6pHUXq47DWVY6dTwnHf87AlIlM5iFm6Wv6CckLuwrfuxM6BOLduMKW3_ejDXvWzU5O3PJwXHI0-ipcxRbE05y0Yq160KrEAtXphbVQHlXr76-chzFtMVtQ3gY_JMla4A7Na3S939oAfgp97qGcZe4QEJiUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ویدئوبازی محبوب Chicky choice
🌟
فقط کافیه مرغ از خیابون رد کنی و پولت افزایش بدی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
betinja.bet/affiliates/?btag=2760677
⚠️
فیلترشکن‌خود را روشن‌کنید و روی‌کشور مناسب قراردهیدمانندالمان،کانادا،امریکا،ترکیه،سنگاپور.
⭐
کانال اطلاع رسانی سایت:
👇
sr24
💠
https://t.me/+K0fAOE9hCUo3OGE8</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/27770" target="_blank">📅 11:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27769">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936415b58a.mp4?token=HxlRvY3_6v1kDk37-tXT6Rzhb0V_m24CSDbANZSsTyJa0iS7ZgMMSnxqcF31wC_-zADy6c1AJbm4QpnnuNIdJvq078cXO6RLJlmxqsX_0Q6cMPzxhlpdtdrBNUb8YtiO_h7esZ6l77CRtJrfleN_DCW65CwtnyWqZ6KIPZ_AT5ZRWIrA9i3H9dJ8t6lowYMvWRXIrsOukZHpEgi8TXJy2Uy5mZbNAkoixMzmYR4S3a07OF8EQ1CMewrXwGdb5tCE5eYsjG0iXDcRSR-lKm9UIW6vPCrUm_tmBYcEz84Cx6s7K4zBtB-cIN55YG793G-anN4tDB9NifzzdFD4TippGlUQwzJC5dCZ6hAY6GhtNjmOms2mhzlTkUOVaJbgMmUDFLsY51MyfCgtoV2a4JFzn01A8Z4ePlddHxinn8amUeLFAMfhQKleymcg5ntxR-F2dWSirU-cIbI2DDrYPmeRtzm6RpnJ97yZEYNs_F_2V7JpyGb_TPKa3Vm3puUaeOr6LslEABvzId6mqBWmeq8QHVVmZRXq92s412u5_uHN8Kh-agsCNh_N_OuARE_Oml6R_kAOW4eSxfYHOG1kfvGxC6GH8eIfHGPgDGX9t-fEXQtm5MNT_HiYenvN0cQ17RoeNA_ykvyIkeFXnWNMAyci31F2dUVQPiRdRgHBkncC4ZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936415b58a.mp4?token=HxlRvY3_6v1kDk37-tXT6Rzhb0V_m24CSDbANZSsTyJa0iS7ZgMMSnxqcF31wC_-zADy6c1AJbm4QpnnuNIdJvq078cXO6RLJlmxqsX_0Q6cMPzxhlpdtdrBNUb8YtiO_h7esZ6l77CRtJrfleN_DCW65CwtnyWqZ6KIPZ_AT5ZRWIrA9i3H9dJ8t6lowYMvWRXIrsOukZHpEgi8TXJy2Uy5mZbNAkoixMzmYR4S3a07OF8EQ1CMewrXwGdb5tCE5eYsjG0iXDcRSR-lKm9UIW6vPCrUm_tmBYcEz84Cx6s7K4zBtB-cIN55YG793G-anN4tDB9NifzzdFD4TippGlUQwzJC5dCZ6hAY6GhtNjmOms2mhzlTkUOVaJbgMmUDFLsY51MyfCgtoV2a4JFzn01A8Z4ePlddHxinn8amUeLFAMfhQKleymcg5ntxR-F2dWSirU-cIbI2DDrYPmeRtzm6RpnJ97yZEYNs_F_2V7JpyGb_TPKa3Vm3puUaeOr6LslEABvzId6mqBWmeq8QHVVmZRXq92s412u5_uHN8Kh-agsCNh_N_OuARE_Oml6R_kAOW4eSxfYHOG1kfvGxC6GH8eIfHGPgDGX9t-fEXQtm5MNT_HiYenvN0cQ17RoeNA_ykvyIkeFXnWNMAyci31F2dUVQPiRdRgHBkncC4ZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ درشرایطی که ماده شش فیفا به برخی بازیکنان اجازه‌میدهد خارج‌از دوره نقل‌وانتقالات ثبت شوند بندچهارم ماده ۱۷ به صراحت می‌گوید باشگاهی که با محرومیت دو پنجره‌ای روبه‌ رو شده، نمی‌ تواند برای ثبت زودتربازیکنان‌از همین استثناها استفاده کند وبه همین دلیل‌باشگاه…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27769" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27768">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq8QY5MSJjIR5o5NDj22UTIMtAdnqDAD5r2bPuzDKQUImveJjK3PqEQnmmbNZZJMhgkiiesDXuxEt5wiWbcsL3LAfmrhzJn7QMCdPYVtVsULAiirYxA4PHSutJ6QqF0_ALHxG4S37YbAStnysW6fYOeMR4vxBxOsQKto6P3x9JjIcdN3zi9NEAnMVUnCavFVSJpXS4q5MEHkCcu8iiwv2nZVYmouE9rgCadaJG2atzCho8uxwTmi_XnJbcRZs5d3ynI-HM7KneuZRW5jNOqoCP-Hmh45FbcTYciBbiLDYbFbk0FZU4oWcPYNpr2Xn4CEcBL7ZgMCdpS4d4I75RIa1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ امیر جعفری مدافع چپ گل‌گهر در هفته‌پیش‌رو برای‌انجام‌مذاکرات نهایی و عقد قرارداد باباشگاه‌پرسپولیس‌راهی ساختمان‌این باشگاه خواهد شد. حدادی با ایجنت او مذاکرات مثبتی داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/27768" target="_blank">📅 10:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27767">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4107ef1526.mp4?token=B7p4eowpHQSoCgIxJ9LN_0o_ZswEcWNiwrhXrfAYBjf0Wm9dlHUWpw7L3RdzIjyjK1T6hv_6gD9dB75xmA2rk1LA0eFhlMMYYuBMKvAdZxT_1wBrtdSwldRUQXRne0Cm7kfJVZjsVuM6kHsQZWuRhwa_xj9cr-S2Yuf5mWNyk-L9ivn5jByWyIaYKxoUmAlQrgfX4ietgk90rlN-PRhsArcDv4tbIFRxNltoDlPOIJWGuezjBcyHTY-FA8utu2YKxVuV1-R_a2g8T56BMXAKWxho7tYW7e5K-kdgDvY6hl3zpAsEtLLkmX5_PTpdquLUXyxUslAaokSiXyemgJzjVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4107ef1526.mp4?token=B7p4eowpHQSoCgIxJ9LN_0o_ZswEcWNiwrhXrfAYBjf0Wm9dlHUWpw7L3RdzIjyjK1T6hv_6gD9dB75xmA2rk1LA0eFhlMMYYuBMKvAdZxT_1wBrtdSwldRUQXRne0Cm7kfJVZjsVuM6kHsQZWuRhwa_xj9cr-S2Yuf5mWNyk-L9ivn5jByWyIaYKxoUmAlQrgfX4ietgk90rlN-PRhsArcDv4tbIFRxNltoDlPOIJWGuezjBcyHTY-FA8utu2YKxVuV1-R_a2g8T56BMXAKWxho7tYW7e5K-kdgDvY6hl3zpAsEtLLkmX5_PTpdquLUXyxUslAaokSiXyemgJzjVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🇦🇷
کریستین رومرو با سران اتلتیکو مادرید برای عقد قراردادی چهار ساله با این باشگاه به توافق کامل رسید. رومرو در دوهفته‌گذشته پیشنهادات دو باشگاه آرسنال و بارسلونا رو رد کرده و گفته بود به سیمئونه قول داده بعد از جام‌جهانی‌راهی اتلتیکومادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/27767" target="_blank">📅 10:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27766">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVzZ5R7um3-BfDCPfT2tpEyVEXZvHQrWR_PU1J3GefrZPIFrSWTDTKNynobnKQYDzqPP1FfIvPmDJutzvwnwAczPxd7xEfEsH1HWfM0EmGeb9NuGqjJcnxaJffkTcNrqm1_xLIRyzqIKXmhGxDq5dSkhWJD1FClz2AMa6U5nVi7x3f217Wqjp0EBVStyzAYzZHo79r5JiSRUfyB2Dz-Z3FdRdK30VJmlQnU0LkdgZj2PZyU913qANHlyv42ZUsc4EikCmPyliYYzhV5k4ZpCRKn32zTwdM9Y_P4w_0sOQSYX6mJaxMYr1m3YPiesvv_pPljjnzvqwdJmXGTjcncArw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعضی‌از دوستان این تصویر از بسته بودن پنجره فرستادن و میگن‌که‌صحت‌داره پنجره نقل و انتقالات نیم فصل نیز بسته خواهد بود؟ جواب خیره! فیفا از نیم‌فصل سال‌گذشته آبی‌هارو به‌بسته‌شدن دو پنجره محکوم کرد به این شکل یعنی پنجره نیم فصل سال گذشته و پنجره تابستونی امسال؛ پنجره آبی‌ها نیم فصل بازخواهدشد. تاریخ بسته شدن رو نگاه کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27766" target="_blank">📅 10:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27764">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_JL1NPFeJZt4laWIMpM0aiCeUX12nIGPWtIvr675Mhl_e8H0p0eo6rmukvPmmNrKxTl2oUyhxTGir24pa6jMZRSjN3HRtL9D5qKp9H3zVPWtvP8-RSGOTs6sCu4IWQHkz-a-vWFbaPF1OBILPI9PvFuyv2QIGPCkrzvZI_O82CPlf6SxAzIJ4GIRhMKv7tEpFTqebVcOvK8hFLMhahYfeAGycX-FBE5bRI74vD7a8p4igDz_v5H_KtdIHK57Ty19NOXAnfLCHBzQQ3vnYtTMBJfHyBae64drHwYCsZ0tKEi14-ADtc0iTHfo22kMuuQlaoG3kwTVhMzY9ho2idOYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CYri7D_bRWu-FnICbutanl8Vl-9eahtBhnCaefymrLp65Jnps_bZjkVYyefcloMTJNnlVOlLbH7__qDBKdUTXjnDspm31wZgtgYx8oVKYy9aDCSmJTjDh8ju4rMFTLnSusSn5BE5tsuN8NQXUdrdd9kWDS-T0vIjhsYaKQNXPFocub3-57BFJhN4bfjJzIH0deLFGHArAMNye4I19m9tz8WXogKbd0uv2DBeWfQhzGO8UGyoCHJ2b836oH1yGvHYZJ7MqErNnuU12K-cEsTlpg2Fg88RA0_1_z3LW8wtn5eO9Brcf3l922h-qOe-SOMhyHyMKL5hOERb4HryrzsAzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال و دوست دخترش در پارتی شب گذشته؛ به محض اینکه تمرین بارسا تموم میشه دست این بچه رو میگیره میبره پارتی‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/27764" target="_blank">📅 10:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27763">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBWIhe-KzSKPiKlSc3YCX1UEHod7vOkXQul-pWMKiQIGDEqTdsQa7R2rB-8kHCwr9dVndrSep6ujPsIym33kqRYYHgZU5sJlEn1Y-RIuYfap92rTjsgn0V7bLVA1AHjOywBxz5h6-rbd2zbiN9WcDnybEiOtcetfwUJnZBapoP27gP23dTGWvEjQ3LJPrnRBbQAxy0s2_CApvCTP5nmpRBRSL1n73DX_faxsOcnYEp10y2l5GgEd4XUF3k8NN4Z38wkEA9WGDgwiQO6luiYzIFn1fJ5i2ofX3cGzAyc0VcCTcWjV6AVRqQn5j2D29_fXm2rVSKbRsPOBQasSD6MQ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
حضور هر 3 پسر لئومسی درآکادمی اینترمیامی؛ طبق گفته نشریه‌آاس قراره که بزودی هر سه بازیکن باعقدقراردادی‌بلندمدت به آکادمی لاماسیا بپیوندند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27763" target="_blank">📅 09:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27761">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1Y73LJbIoNkPjW1xaD2rC8Z5Oyoxc2uk1EY02-gQZqexJpzrld6PkqjNzjl3RCIhWSI8F6gu3ZglUKxw-f6bARtWSn5AKP-17UuWDU4jjJ-dSTY6Ysqf28arhGbmLNGwbSW1ytWlZNB5Eu7GhlBJLMX8cBI0uPPAIzx4DaT8j37-BGb8hOyY0pqhv13ogsse5G1yCx2eP7cyi6C10O6hapeZQ06OAcObr-8CX7Ss5TtgSfvrEf9GdG-6uvWP9iglUuIO2SbR1hpsotUF7t6ir4UyvaPgrskx_sPsPQjDP55mbSGVX0kq1TsKaAPEzcmabr23QnOGJAI8V_MXN9HDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌برتر؛ استارت آبی‌ها در فصل جدید با برد قاطع مقابل مسی‌ها با دبل سعید سحرخیزان؛ فرعباسی با کلین شیت فصل جدید رو شروع کرد.
🔵
استقلال
4️⃣
-
0️⃣
مس شهر بابک
🟠
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27761" target="_blank">📅 09:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27760">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljvGZtsJ-Ob7hSbo_IJqZndI1V1jsSXl6W-ih1pF3cU-b1k4LS6knppEzAvScQXzsJfMVq7H4bbtq8DYl6Z9vi1fiE_DlL3SDiuD26NHtx9FHTmh2pTZM3pJjp8dNC3W_mwF9cAbzDBlRZIhbVmNE0GZnuz1NwIwtMS8R6Yum3QlqftTgQezUgN1Gstznj837LbqaZz4pYCWuU_AvSb6aE71aqkfh5SE90d71qOHoitTv9ZFDCLpnio2aopYBsGYY1LHUV0FPqDLXLPDgGvavovlQtD7RZJQObqVgyLbWR1oohqDraZrSB1TSOdl37LcrMA1sDmkHq0YNXr3j3X15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مدیرعامل بانک‌شهر فرداصبح بودجه لازم رو برای جذب محمد قربانی دراختیار باشگاه پرسپولیس قرار خواهد داد. مدیریت‌باشگاه پرسپولیس‌آماده‌اندتاسقف 800 هزار دلار برای محمدقربانی هزینه‌کنند. این احتمال هست که مدیریت الوحده یه مقداری مبلغ…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27760" target="_blank">📅 09:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27759">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3eb80a731.mp4?token=IfcuoAD-0yJPdnzws-Kv-BkEf5saHHsa3a7vnvkO0JffX46HUT1WP8TK-_3L-MQZneYGi8OrWNaxIsEaRpcyjqbqyvAj-oqZ3mI6Vcn1bqvc6qg8nvHoqD0OL_5dbnVbP2Eu_ICIxvsOQ6dc4F6enD1qjdBo_ZZdPxOO1R7fH3v-guGJuSs0lx0zXVvROvD4sAKVxvc07XRnMc82DF-DDjyuvuMipVKSHywwd8_7GrCBMW_U-XZelVT8xLhZlAhYnpnUpT6B4VaRUKLxFzQpcKQDZ7PJ0MNSOt5xthZIRC610UKd7FO3QtNf7I0OuAFYdfxNb53D8UBam7IiS5xTRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3eb80a731.mp4?token=IfcuoAD-0yJPdnzws-Kv-BkEf5saHHsa3a7vnvkO0JffX46HUT1WP8TK-_3L-MQZneYGi8OrWNaxIsEaRpcyjqbqyvAj-oqZ3mI6Vcn1bqvc6qg8nvHoqD0OL_5dbnVbP2Eu_ICIxvsOQ6dc4F6enD1qjdBo_ZZdPxOO1R7fH3v-guGJuSs0lx0zXVvROvD4sAKVxvc07XRnMc82DF-DDjyuvuMipVKSHywwd8_7GrCBMW_U-XZelVT8xLhZlAhYnpnUpT6B4VaRUKLxFzQpcKQDZ7PJ0MNSOt5xthZIRC610UKd7FO3QtNf7I0OuAFYdfxNb53D8UBam7IiS5xTRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پریچارد کولون بوکسورسابق‌توسال 2015 آسیب‌ بسیار شدیدی به مغزش وارد شد و پس از گذشت یک دهه‌سختی‌دیروز درسن 33 سالگی درگذشت پریچارد در تمام این سال‌ها توسط مادر و پدرش نگهداری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27759" target="_blank">📅 01:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27758">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Op3NNYK1fmzkyDnyaKOKoL3167H0bBki0_uj9SC5-3P6_b7hpI6iVFzl1ieDHUnFhE4Zr61LgtxQaeknIs08ipBBB3Wwdj4qwfR2hKAYFgVf-JInwSnZhfjHIexBcmU7vtOTBfZypKZ0sym2A_iADdGMY_z3QUtWKmnDYOqzIePLtTh05CSuSZ70xgmKAxNYVfYHOfw_ZUg-JdU7EvtpVq9ocWPd_iRpHKqRvPufVL26sT_NMl92kS60zncafQ2gojtvka8p0CX4sW6YE94bJuUIPgUZM-A8XcYfiB2t7rJDvvAqxFMsxn-JzR2fykmr-cEOf0ipb2OJT6tlqylqyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اگه‌میخوایدواقعیت‌ماجراروبدونید کسری‌طاهری و دانیال ایری هیچ مشکلی برای عقد قرار داد با هیچ باشگاهی درهمین‌پنجره ندارند. دیگه از فیفا بالاتر که نداریم. استعلام‌گرفتند گفته‌مشکلی برای عقد قرارداد با باشگاه جدید نیست اما چون مثل انتقال پوریا شهر آبادی و پوریاپورعلی…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27758" target="_blank">📅 01:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27756">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl-su2kF-lvuzP3244zvdTXx4GA66qG8s_FDSrbFloBn08Kg4ZDO-ci1iCwUzIxK9_kyiWqS7DSHuGxAH1Ms83_RHxK2xelCyCK49J2ksAP-pukWTJDqcS4raxLV0asnp-1g5bUq303NYYVU9HrrXbFOtYEqZlKhfep2EYxo2yKWnnxvGrvNHffRu16mWmmY76B4qWiC5tAULgWOP8E7jmTy82Xm9SXl2z3ELoath3tJLMpFr6EHKD3RKwlJbCalJOVduyky2vp-rgNKZukhd5ObX6okMpOIHpAZ5JSrVnSDgb8ZjDw_d3MPoG5xV5sP9fJRZMMGBhugSRc3g1dCZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛
از مصاف شاگردان تارتار با نماینده قزوین تا دوئل کلاسیک میلان و منچستر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27756" target="_blank">📅 01:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27755">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvyReSWjKoDgwtGhxPZuB52ZGjw_upWT93FbYsOP8tVvjammlcPuSq4SRnKX2obPyuMVGibfuNFSSfFrH_Q2nztPJOZjWJNfAAihMQ45Qfcp9qA8P-qjaLWgZQjg01Rw1t3tHxeBYxAfRVTy2Vj7Fa0FNc32XeDekkBOIAywR60Vhy7uCyL84pZ4HKP9XN39O9wheSQgKG7jSjR8JwZeyuCSTjFE5q7mkhUxHL0mWcOJo_kQIV_WIxsuMK5W5bk4mCVp3UqEQff4q54yXmhK9NQJPQZBs-TgIIbh9rWfvB4LKPzh-ByoclHuglXBIYOH88G-BEhsp7D9rWA-SacZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌ دیروز؛
از برد پرگل آبی‌ها با دبل سحرخیزان تا برتری تراکتور و سپاهان در گام اول
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27755" target="_blank">📅 01:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27753">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuiOT7FBZ4EZ5-ncpovnASrctCvJIgMVZWDjwx_LIT6xXQgiI1qqbM-nIs0mUIKiiZywZi-MISg0Q1IYQRuT3X92DpWQqFN2BL0EdMolY8wi0kxpRr5btbk8Z5LZQX8YCRHU8Tj7Cy1qLwe1Ue7I5v7oIEPj6AwgS2isxQvQHOxEkfonW0I-haruUWN5LEdfPMCS4Ha3NE0K7Ng7qRNnB85NYRsOi0OVl7aW-8XmNAmda5dA5tUJWTFIQJPv7zehw4_OxPvGUezust3TmoMulX86sPo8yTaAl4N6t8kTyws8t2PRswtDPEvh-LtXAbhCFxf7Z_7Y3rbqiRYc6SQoNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#افشاگری؛ علی رغم تاییدیه فیفا مبنی بر اینکه یاسر آسانی هیییچ مشکلی برای همراهی استقلال در فصل جدید نداره و کارت بازی او نیز صادر شده اما علی خطیر مدیر عامل سابق آبی‌ها از مدیران تیم ها خواسته که در پایان هر مسابقه بابت استفاده کردن از یاسر آسانی شکایت کنند…</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27753" target="_blank">📅 00:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27752">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-xvyVi3SbLYN53iO7zERgLCDZ2ZJC99Ds8zi25LgIAMTc_4ha0HtFSy4dYVhDekxc01Ht139K6Oz1NIuU6kUZYGT0ARjJtajCpor-iU8S9dtKHEhJ2jexNrWsJOiKG35bFi0xTxAaAqwEgBpKKH48I8SdW_fCDfbYHF8JlU5jDhSjMQEWkzK6Yrkye3hs98qvtljlSPKNtdr8WZKt-P7I20bHDz41unWwg2Lk47yB3E_iSzhNMq2qAgtuVPZN4K6JsNmA82htPHTvozMWugp75xkdmRfOCXIcqRa1NsjlAx3R-KDO06YySsOAtnAFeKeoiR-5IVpPvghrv4UyvHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس پیشنهادی‌سه‌ساله به‌این صورت که فصل اول 55 میلیاردتومان،فصل دوم 90 میلیارد تومان و فصل سوم 130 میلیارد تومان به محمد قربانی داده که مورد موافقت این‌بازیکن قرار گرفته. قربانی روی گرفتن رضایت‌نامه‌اش‌از الوحده تا روز…</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/27752" target="_blank">📅 00:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27751">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLA2J1V6BrzHMFm8htXoeCZ5IIyB00QSH_CYP9vzNaspkIkglw1XUWaQavuPAY5TRACnl1CBkZu1twBYnyqoNCF8brHI9B4piosAOC-xTxSR0gCLrpaWId9oXUqWB_PIabQhaUq73tTrLrdyUhbzhptEYDm9n2TfOBamGM-T7w4f70pkFujRYEroJKZdYrqXgNCElOXOp6qgx8c4U0Sb4ytUoJ5DR2bSUJl6UOAVZfZEVQqoYP6Y0rj4c4hBYbQU1bBfMjhm_3PEO8iy_fWUC5kHbKvniYcsvf6H1dituT_KKCNctjZxjkxTTPAuj8MnOnC5aQxBjZ4KuObjrYjSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ رحمتی سرمربی گل گهر امیر جعفری مدافع چپ خود را از لیست این تیم دربازی‌امشب بانساجی خط زد و اعلام کرده این بازیکن میتونه قراردادش رو با پرسپولیس ببنده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/27751" target="_blank">📅 00:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27750">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRMsM_BZaARA7eMktjae2yZvxEVG0zovG9MAxnQVWW5ez6rqjeh9rhxtvH2fjchQ_xdUkexZbZht0gvDAw6OXfRpW4EXPNw_1_eONVL98u3jjNNQyp3TtKOTU2tuNkSJdKFM-D4DEZxhcmuLTE0n7wjkLrSHLFKnaihp-7viAQLmxUGUcQRffSkdxhRPRkWA6V7J7-Cy1v-VcmBu5ntt0iSg9_QK4VByfj6ZAfATwholike6vYbE0eYf2LfJqqZ6X8BCu56cpumh7UhxxG9DBx_YOpjMlpCnADKGpFzCaEbvTKedmQEt0rsXJhv2WYAcM6Cx2jN5_ZAv0NhxX0VkpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تصاویری از رونمایی باشگاه پرسپولیس از کیت جدید خود در فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/27750" target="_blank">📅 00:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27749">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsxTuIS7L7nsuWFNMOcMlA-yqEkRBLyuIG9fVVEd_HZhC6MIFlBHEPW4M1TKo53X8Fjb7e-LmXStm6apI4QH46HsRkfpdvT9OBaGgOBQ8kXomE_2OFSxxlwU_NvOpsErIwyVKBEggFNjmGCxzQ98m84qizJ_YYDMgUIqDV8gcTGGb_B_3FqwSI3eqth2oij-u6EeDoMfZnlK-cJxsol_4q-c1u6XQ9ltvUUKSN4i79e_4_W29jBRtzJ84HsiR1DevK3e9yEF2zPrTKoQ7TUAFMr3hg4m63Tj3JBTooshiPRPf4sj4TZRYv36n0Y7LWhJkfE4O04OVF0xRY5b_id7aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ به احتمال زیاد بخاطر بسته شدن پرونده داکنز نازون و جلوگیری‌از خطر تهدید شکایت به‌ فیفا مدیریت باشگاه استقلال هفته آینده با نازون توافق خواهد کرد و او به جمع آبی‌ها برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/27749" target="_blank">📅 23:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27748">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=AVWBDs6DnGb0FdHoVv-whh6HxgkhmK3c4vMC_yHtf3O27_QBliyX3-ZFi8_M5rEbLDAECu8Yl0bZJ2kynsv76-M3jZ-fffaTsgpqcuxu1cFvNLKsbHFwlVtTzXi8lWqYnSteleD9hv6dTFRGRFmKon531lUk7FVt4lRY-vrGc1PYAPSo86uQCVipM1jKel5x7MZEqXOVsx1tBSyCdpfCl3k0DSW4cfKcCmT_HqJ7VMkFBZCTRzEGLN7eduD_vHszAdIPUmnWaRf1o9-qz-Z-zs7K9GqddYH756wVT3Yk-HVfVg1q2VLORZ645YOKP3kqqahZjutgwr6P7u0qgFkdsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=AVWBDs6DnGb0FdHoVv-whh6HxgkhmK3c4vMC_yHtf3O27_QBliyX3-ZFi8_M5rEbLDAECu8Yl0bZJ2kynsv76-M3jZ-fffaTsgpqcuxu1cFvNLKsbHFwlVtTzXi8lWqYnSteleD9hv6dTFRGRFmKon531lUk7FVt4lRY-vrGc1PYAPSo86uQCVipM1jKel5x7MZEqXOVsx1tBSyCdpfCl3k0DSW4cfKcCmT_HqJ7VMkFBZCTRzEGLN7eduD_vHszAdIPUmnWaRf1o9-qz-Z-zs7K9GqddYH756wVT3Yk-HVfVg1q2VLORZ645YOKP3kqqahZjutgwr6P7u0qgFkdsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلیل‌زاده:
اون‌عینک‌لعنتی‌مال حسین کنعانی بود و دادش به من‌که باعث این ماجراها شد اما من بازم میگم اون گل آفساید نبود؛ ویدیو رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27748" target="_blank">📅 23:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27745">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWyvciNKwdXd6ZLeHUiktHHlYZSrXl8n7bJTKRKcWCCRhFQQ79sQ8RYaaJINdhFl__GflVjEUvsuscNTUdTNsGFy8fXavizU5_tvWRLUcbNoooUqgIuh1uk7jhukZjd1Dm5foj6f6NZQVU1qiImpNmiPAXc5mpuwDKaBtLR-C1fup3TNUcoGNF7_HTnuN-oaiSNXHUMbUVpsffEc-Ni3HYD1F1ADtxRcZbMa0kGjDeME4yXG9QdHhkXdH05OgTVjkqaKuh_8VsTfVQjPwhUJ7E7ztMeOwbWGsTQEmKvjVJeTHePzbZNXAt2qOrJfc1GfVXWJBT9ceE41xBZfGYJOUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lHASf1AyKSECVI4JiHr9IldFy9fb9iRAKYcoCOyjwtC8CwhZieitnM44yeNbizEHh5R0CH0oihOdKT81GrWibnDmD1OROty7sc21rSaMIch3EsGP9CsHXLKaC2JOwSzJXUGzk0gTW_YB06ZAMUDgEofVMUCTDnZK3XfuouEFh1ixtSlnoBi4OjbdbuHiLPEtbWxvQP28oTzB_5tZkzs07zxee8xxSoKQoPu0hu9-QuE5bcyVGG0EUaTOhEbw13HWjLPpfAMZkdi5rV-G9yb7miQaTHJm8PLUamPYqjJV94q8JOwey8HvAX1vLAYZHRU8wedYVohUSVYMw0MwNF491g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
دو ویدیو زیبا از فوق ستاره‌های تیم ملی والیبال بانوان ترکیه با کاپیتانی و رهبری زهرا گونش که اخیر قهرمان لیگ ملت‌ها هم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/27745" target="_blank">📅 23:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27744">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foc8G1KxWxP9C6z8W9CXYzQsxwJ1JQcYO0Idhi25YfnN9PsxW7nFKElYhNQoD7bXP7srUwmmgw-BGbo-bi17ozxP_0esVqvZf6LawdG4M0Tp0IuXJ82Jc1arZhwDm7wefjtkGz5upQukcjlHR69nW_mW3uehxwTsQyCsmvjWb-RElBWs8_9HYibLhThIQR6tQ2z-K9EnbFNHRET4KhNfJZDpbMX41k4CTnY5lamON-C4Q9LQ3i18-GW-2GX4e6HQGSJixb-GTAetB06KPaD8GrCKlubJyRiC9uY4i-8DMNJkwTAmLd5-Ma0HoI7iVl0qLezKwAQv91C8KJb5xpQXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
🎙
محسن تنابنده: وقتی‌حال‌مردم کشورم خوب نیست سریال‌ساختن‌ارزشی نداره. دوست داریم فصل جدید مجموعه پایتخت رو بسازیم اما شرایط جامعه به شکلی ست که هیشکی حوصله سریال دیدن نداره. هر زمانی که حال همه خوب بود میسازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/27744" target="_blank">📅 23:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27743">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhqt1Jx92yzmaKr6TSUMtLvFj_BuUDbw-OJXS5-Wil1XBaIZ6r4EEW8ygur54ZTczfP6H0kBmgogiecgFM9RUSdJF0XPwMOGM7r7d0hIUQW1oGv_nYb1EAg37tQJ0-DfNeNtjIWcLDvAFevFG5vscUWF4yMUW_1lmaImml3navax0vygscB4vwzc_TpI7MyJlAdHsuzm-05s2As1aXtAGJlEV2J2h1Aj39LAICBmVDz1MX6HyGSVHLiOfjvDiQ92wrumVh-tBSvm8Z04_FoRjlR8D7Smo1GZfRK3bvfxEE7zmIdQIE8VPm1fOHxnJ0zkRExfey5N96mOEzq2mP4UAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس پیشنهادی‌سه‌ساله به‌این صورت که فصل اول 55 میلیاردتومان،فصل دوم 90 میلیارد تومان و فصل سوم 130 میلیارد تومان به محمد قربانی داده که مورد موافقت این‌بازیکن قرار گرفته. قربانی روی گرفتن رضایت‌نامه‌اش‌از الوحده تا روز…</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/27743" target="_blank">📅 22:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27742">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsoLlcVlOvFmwW_OjE4nPOl_vjc7ORxvZSk5Mj2zerYb33fhhBZYS9Da5Gs4gbbT9dizRzZr56GcMreLLIZ9nXxL_rBlSh5kYni4WwUasGGO6Y0Xutu2Q-PUSeu64YMwdHEHh9bRy7qgroaoq8YyFGj3cZzoew8QHewvP5SOfnX5zCa0DCkvMoUX5MteYH0-h0GFxXAucQEMbE86jj8Pt_UeaQop5iVN3yEcCLrKI_W9HChSKRFilP_dJoUhCbq-lt-Djnq3yYxD6eJDiUZpVjfpZzRc2UnpX5LAiIdQs6nz27NMJJa2J34XPsJsDV7GJRxx0MnTnh2x0jRXYWvPcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#افشاگری؛ علی رغم تاییدیه فیفا مبنی بر اینکه یاسر آسانی هیییچ مشکلی برای همراهی استقلال در فصل جدید نداره و کارت بازی او نیز صادر شده اما علی خطیر مدیر عامل سابق آبی‌ها از مدیران تیم ها خواسته که در پایان هر مسابقه بابت استفاده کردن از یاسر آسانی شکایت کنند…</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/27742" target="_blank">📅 22:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27740">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LslJ7I51H6UhdRX8lJgFh-c0Q9AxYHCOQS0pC7hW5qqPkRP3EgdLiTng2PbhpKzfj1vOIeeB5KCZt-4TtIzUX384jA-lq6GNC4sdnZzR-AoF0JnaBJMhmqyAayXNbB9UnJDD8ZclY1jC0gTus2p-QgWaLSgSxItv3WOaKZecA3x0ZqZeaURezCH2URQap8S6N18rfl47xQfTRPBe2ldD6s8LZRKKH7VnO15sNsTI_Huqkzo3C-f2042v6joAEX1SG4pgZkhmy1agmQQDVc0XnhJ8UEbuIaLVmmoCDzfZq4QO_xpqMofS1D6Nuz0zjujrzr18XZg3NgLM82LFhmI7gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ey2MU57BgYVEGTwUq0shWbUeyWCxrQlsfqJqd0lykAHwwnW5Tf-iu6II-PDAAEItj9sFhF1MP6aAn9h1qLAkIxtorSFExYdXt5Sa8BArhDu4sLow4tU2V-BcGsTrmhc3HrfvJb1cXoNaJOm0Rq3hdF2LC0mheXVgZoKNRacy_WVHHJwpn_4Ksqb3Hm3SuurskPQuxl9uTr_3kv2dJtisng8bkFfWoSjJQHbtWDzCnlESqj3j-APrSzuNxsdf3S31cbyhdIoTvhnX7g_FUCdciRgDq7Uwd3KB1dSUs79XB_t1vOXTx1XMLfjQga_4d_kOww42ZfM8zaICD-O6e9rV1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔴
رونمایی رسمی باشگاه پرسپولیس از کیت جدید سرخپوشان برای فصل جدید رقابت‌های لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27740" target="_blank">📅 22:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jxEOEzv9YiAnaHfbs_dIVKsPK2zf4CHGbMQKcvmNg74oybQ0jRjLHGbnh3o8lvpsWUPMkLC-99U8NYA5z_bbQyvhtc-UqeFegWnT-9Tx0-dvJVfNIyIe0i8GjiqTLPBApekwhFothp59vA3sYMY9hC9b19R_csFXmIDkqDrlggWA9YW9ozm-QtLu0Ds-tMZh6g48-QOXQzffxDqAO3ctQmVE34Yb3xM3juOJwwvwyjBJKKxeTaYWvq7gfpjCfFeIjCdcBNJhp5YZsVjh6I-NRbvtz-Moqm6Mfyo7Tuduk1WRvyGSnufmFQUt1ONMBfyDMj9U0EqbmR-XOIV4BqJ2Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICnBi2_CIUi7uTSgzyHHEMumWR6J47pkHN21PtU-uf-3hPmot_FsgWAgD83_WNZVf1Pi7l6kGJk0HaWANHTKztVrbK-bah7KpkFEMlDRB1XQm78ioKoqj8ARt7YtS5BUOP8fpXgeVdFy77Dca7ZQi3zwL9nlYhDbs5KMyDWjPpZkfpEaO_0PhG9SfoV8auJ1dx-lGN3QcO78vHw4D7aIe-TXRcNLTks_p4-Owu_FJUhSx37OyAkDT4QZ-CxIMA7-sGOFOJBei9u2sZO0Z_pIN6IxYR9DFGOfSH4q02qNCcf2rCFrdV-RX2uehGJ5Ev_SrcMrw8Uvu6NPq-PaGBQBGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ سوغات سه امتیازی و ارزش مند شاگردان محرم نوید کیا در یزد در گام نخست.
🔵
چادرملو اردکان
0️⃣
-
2️⃣
سپاهان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27738" target="_blank">📅 22:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b99364b6df.mp4?token=WlK9vq3YaY5CS7vRMu1iSUkeG_b9h3vHfxm9jXChYkxp_jG6A6DEmlVxI6WctWWHVG0yzuKIlQQpT8cyraXGI2phOPMki45QTjK3_uuapEIYLpLsQjza0N1XFfJJ1m3rq3ipWNdmGTfsbWcq8vvTZz8FO_QBDxjv0VHiTi2MYzn2jjd7__RbxRrJq74Xl3hEv1qNR0OQcQBELjya9Tx1trXDua8_1o4Fne4EDIiDUEoFSZjWy_qU73ut6N2_SjDY1bNWrR_fC2x89nKDl_2gkDNXXfMt7OWpX60Xkk_SNOzG2u4EZzgmZHcyzCkr8tH-Se6Ft51gsQUFYgLrXVYcEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b99364b6df.mp4?token=WlK9vq3YaY5CS7vRMu1iSUkeG_b9h3vHfxm9jXChYkxp_jG6A6DEmlVxI6WctWWHVG0yzuKIlQQpT8cyraXGI2phOPMki45QTjK3_uuapEIYLpLsQjza0N1XFfJJ1m3rq3ipWNdmGTfsbWcq8vvTZz8FO_QBDxjv0VHiTi2MYzn2jjd7__RbxRrJq74Xl3hEv1qNR0OQcQBELjya9Tx1trXDua8_1o4Fne4EDIiDUEoFSZjWy_qU73ut6N2_SjDY1bNWrR_fC2x89nKDl_2gkDNXXfMt7OWpX60Xkk_SNOzG2u4EZzgmZHcyzCkr8tH-Se6Ft51gsQUFYgLrXVYcEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سوپرگل برگ ریزون و فوق العاده تماشایی اللهیار صیادمنش در بازی امشب لخ پوزنان در لیگ لهستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27737" target="_blank">📅 22:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80eddbb6f7.mp4?token=F6Chqvcv-bVknGZ8SZz6-lA7Zs9-gL1QD5B0-fIbw3dsrzg7Rk_LgE_PE5xMXMRLGrIveVvOKTTJr52-PXflNdfBX93nx9sgivHeic9DWZ7S78_1m4tSG8M1SKSmSUoTl81SNiFRcXT8vnySbstl0mG-syiTNFTYSYHHxds-rGSw8dYZhaRjZON7k99uDWr3zrCcZVWzmyLP-v4582wBrR1D9xciqnFgxjVaY-JjlqzlOFgdOXyJTPuPKzAs1cgNTg_MtSGnOB1BNK58Bjwc-beizu_ft6uhwjX7JULZz15CTq2SkG_RMR37gDOwPSCKYtz8FeHnT4s1j8_ODwODig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80eddbb6f7.mp4?token=F6Chqvcv-bVknGZ8SZz6-lA7Zs9-gL1QD5B0-fIbw3dsrzg7Rk_LgE_PE5xMXMRLGrIveVvOKTTJr52-PXflNdfBX93nx9sgivHeic9DWZ7S78_1m4tSG8M1SKSmSUoTl81SNiFRcXT8vnySbstl0mG-syiTNFTYSYHHxds-rGSw8dYZhaRjZON7k99uDWr3zrCcZVWzmyLP-v4582wBrR1D9xciqnFgxjVaY-JjlqzlOFgdOXyJTPuPKzAs1cgNTg_MtSGnOB1BNK58Bjwc-beizu_ft6uhwjX7JULZz15CTq2SkG_RMR37gDOwPSCKYtz8FeHnT4s1j8_ODwODig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
🇮🇷
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس پیشنهادی‌سه‌ساله به‌این صورت که فصل اول 55 میلیاردتومان،فصل دوم 90 میلیارد تومان و فصل سوم 130 میلیارد تومان به محمد قربانی داده که مورد موافقت این‌بازیکن قرار گرفته. قربانی روی گرفتن رضایت‌نامه‌اش‌از الوحده تا روز…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27736" target="_blank">📅 22:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27735">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb2c4a260.mp4?token=cIgAtWQh3_rUz4D17fB4EK0BCUonQvimgelPNx1I4SE57ratVUYNCKNUXOcxO5iaVNtNtQIl9eKiq2oO5dgOFDLj3AYlN7HrovhRduyhIgX4v_M3k0ZeU1jrE0wTyKGc9H5bWw8s_lhsYBnNfvCpS-a1wu6HrH5DodFZqPCHlGbdbj5Zu5xNm54bBLYlSRZ3isi3dEqXObMQOo7W6HIXqS3SloicH5NXplLiQcRO0S6vdyulof-JJPCV-Uk38sQbea5rpYs-uY8FxoC8civy3l12WuMWVfaAnvNS-gfWweE5BkwIEeH1VHhfMtlWbgOrngPABa7IPrNc4A7BgmaOzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb2c4a260.mp4?token=cIgAtWQh3_rUz4D17fB4EK0BCUonQvimgelPNx1I4SE57ratVUYNCKNUXOcxO5iaVNtNtQIl9eKiq2oO5dgOFDLj3AYlN7HrovhRduyhIgX4v_M3k0ZeU1jrE0wTyKGc9H5bWw8s_lhsYBnNfvCpS-a1wu6HrH5DodFZqPCHlGbdbj5Zu5xNm54bBLYlSRZ3isi3dEqXObMQOo7W6HIXqS3SloicH5NXplLiQcRO0S6vdyulof-JJPCV-Uk38sQbea5rpYs-uY8FxoC8civy3l12WuMWVfaAnvNS-gfWweE5BkwIEeH1VHhfMtlWbgOrngPABa7IPrNc4A7BgmaOzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ ترکیب سپاهان برای دیدار امشب با چادرملو؛ ساعت 20:00 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27735" target="_blank">📅 22:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27734">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqBc0ugP3Zic515n19QGwTjgVRGEauWHLnm6kWV1GSYlWETJOQlkmPoyzmfPrnrhacJtrODVJv9hEldEBbYM0eMqMiuuioY3fUn8IHKf6UNU242AqM8jLS7zY1975_KU57cFtYi35iIojLgdsjePqjvBOBR2Rqp8EhlY5f3twZBWW6wGWMaAelryUr_fVkODyO3704zswKlIetfT-Cvpf2PfJ6_1iiL_zuUQ9Ix4m5vWf-DOzuASmDyZg6ACxAwiTCDIl6GZpVtTisb6ZCBPGSMulYGw67UVzCn6Rwv6LR9qxnhNdzTt0Wv97hAX1ysyHMid7E0_nEapX1nGAaUyvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چیرو ایموبیله مهاجم سابق ایتالیایی‌ها و باشگاه بشیکتاش که‌تابستون‌سال‌گذشته قبل از جنگ دوازده روزه چند تا از ایجنت‌ های مطرح فوتبال ایران تلاش کردند او رو به لیگ برتر بیارند در سن 37 سالگی از دنیای فوتبال و مستطیل سبز خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27734" target="_blank">📅 21:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27733">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecmlER1-TdyHzDzDFIz4ufDKEPexx4IwScCiR3YLOFjIGqVyYl4QsRiZpuma5Ug3ktQVlpcq9lGF8sgZHtFM8WvBxs1lxtceMAIM_5y20TtHaxnJ9SSswzoI69pphAkqPyE5-zX32n6NA_oAs1Gste7tqSD904NmcXvqiLIURHl10fLUI_5aZrz_oe7xBHqsfWZbkf3VJJRGRw6uUIpFFmoQ-i-HTvGJvJ-_c7rY1kxlxQt8w7HXF4qUsIHIJ2_KsI8m1nt3iKyI-xroQTyyCTCibNyLII1VdlYf6-KTphgOuZckt0m8vakTge45MJgJL1U7bvA7H4Q4bMe5GJJMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
طبق شنیده‌های رسانه پرشیانا؛ سید مهدی رحمتی سرمربی گل گهر سیرجان موافقت خود را با فروش امیر جعفری مدافع چپ 24 ساله این باشگاه به‌پرسپولیس اعلام‌کرده‌است. رحمتی در این پست قنبری شاگرد سابق خود در خیبر رو میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27733" target="_blank">📅 21:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27732">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtG50tQ32F8sCyTlS0xhdHLrl4sAukSSfHQbC7JRnA-GtdwgHdLuK1tjp1KxDPguFJn9auCAwwHJxP5NSmttAhniS1z89dIHN4ns8tCPHpMQcEcyO5qDX1BEx06VK4ymhcVS2TbiwkWnD24498dfYiUDHp4QX59WcWHZ8FwqgF6rRssZVn76-Ctbbv_C677yXMXMrFFnvaspGq-GgIpjnstOPVl0E6Qnn6ibA0TL1XWDsp4k-cclAMQh6jf4udFKS-wgi6vydslKPKPX1zWwz97ikPLYTbYhCjtyYhPOlfddGzDScBVzXswQ6S1Tu2mMW4fyhaSXnl-7ybeFTA2_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌برتر؛ استارت آبی‌ها در فصل جدید با برد قاطع مقابل مسی‌ها با دبل سعید سحرخیزان؛ فرعباسی با کلین شیت فصل جدید رو شروع کرد.
🔵
استقلال
4️⃣
-
0️⃣
مس شهر بابک
🟠
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27732" target="_blank">📅 21:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27731">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3Gnjr9hNSBWWcPxlukRnNzr4n4yXVfv3-EvED3kKDkmxRP3XP0qjdrxFjlX01CFjGlSzTFsMeZFkcF3_ld_aTiszuR1XfXBkuvOSNv99yCQHMcMXY5T76ugqbkgNm5vibv38G1CANr3hjXH5jJABDj6FyztwuPFm4ZJEJBGz8OtEQLrhTn5XIJqVjZI-TRDRFsJt6pp27-YGblFeKpICXGwq8DU97IwkNhf5_iQxcRJZ91I6ulseJdXeIHsgIbUy6ZW8nqV_45SasaAwzz8kF7a8nNbzC7YaBcErCIGb28HWCHxZhXHBZ5PIocaPuma2B4U2-kp7a2EbPiEXwSMVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دبل‌مهاجم آماده آبی‌ها؛ گل دوم استقلال به مس شهر بابک باز هم توسط سعید سحر خیزان دقیقه 56
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27731" target="_blank">📅 21:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27730">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d884286cc.mp4?token=v4BvIkLPAh59iB3-IqmiKLSRqhVp_ORV6NA7TDyAJWRC4GhDkeOR1brjX-Oqa8L03pBd0OJIQxyjfLGRjoxMSrwpCI6FiZscGpSaOlbJzvLq1ZZobGug34hdJv4rvjOrytoPqkZnT-lbHwARba_V0hsrJnyOnDPDUhD05rJrK-qxRl9RTZiTBrbgbwmKYnvg-kASC4OpXJAayUqzPqIXu_Ssopf8TJlHCv98xQUZjPJftqQdEqERyXhsANQoj3Nyb5bvelitZY6FVG8MGjNwAkg5mpD5Wmlt8JPmYP8G41aDW3UlxT8hcj48zWvPMxiaAoe1VnjqDGZTaYCmhKfTCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d884286cc.mp4?token=v4BvIkLPAh59iB3-IqmiKLSRqhVp_ORV6NA7TDyAJWRC4GhDkeOR1brjX-Oqa8L03pBd0OJIQxyjfLGRjoxMSrwpCI6FiZscGpSaOlbJzvLq1ZZobGug34hdJv4rvjOrytoPqkZnT-lbHwARba_V0hsrJnyOnDPDUhD05rJrK-qxRl9RTZiTBrbgbwmKYnvg-kASC4OpXJAayUqzPqIXu_Ssopf8TJlHCv98xQUZjPJftqQdEqERyXhsANQoj3Nyb5bvelitZY6FVG8MGjNwAkg5mpD5Wmlt8JPmYP8G41aDW3UlxT8hcj48zWvPMxiaAoe1VnjqDGZTaYCmhKfTCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تازه‌واردهاگلباران‌شدند؛ گل سوم استقلال به مس شهربابک توسط محمدحسین اسلامی دقیقه 88
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27730" target="_blank">📅 21:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27729">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3f9408f8.mp4?token=iiPmr12OgoGzNGwc5lemS6-Cfx7bW4r_pipo3-EqhfENagtMlVekV1GnDNiiEyUoEkKVkA9k32yF8iBk0l2_8NyvBg9H4mhgekr0Yp0GVUVQXCeXL86kMnBFzXR0PrwhXbllsTSYzQwBetjK6OJ2Kjt9-bZJoBwg9jXhDyzNDnWH7V6kNx5C7fP2tk6JnZL_ot68CvywnOQOTSAoqSZy7l8yC-J49LhnCKM-ZucXCI4wyQoqbu6pGWBIRe7nKyyURR_yEv8JKqycU-dMwplZIDlDQfJ05DcYRxfb4r3WLG3ycF3vqLMOD0PLaTuesCbJilQmkEkxZZ3p_XyUxUC6og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3f9408f8.mp4?token=iiPmr12OgoGzNGwc5lemS6-Cfx7bW4r_pipo3-EqhfENagtMlVekV1GnDNiiEyUoEkKVkA9k32yF8iBk0l2_8NyvBg9H4mhgekr0Yp0GVUVQXCeXL86kMnBFzXR0PrwhXbllsTSYzQwBetjK6OJ2Kjt9-bZJoBwg9jXhDyzNDnWH7V6kNx5C7fP2tk6JnZL_ot68CvywnOQOTSAoqSZy7l8yC-J49LhnCKM-ZucXCI4wyQoqbu6pGWBIRe7nKyyURR_yEv8JKqycU-dMwplZIDlDQfJ05DcYRxfb4r3WLG3ycF3vqLMOD0PLaTuesCbJilQmkEkxZZ3p_XyUxUC6og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
دبل‌مهاجم آماده آبی‌ها؛ گل دوم استقلال به مس شهر بابک باز هم توسط سعید سحر خیزان دقیقه 56
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27729" target="_blank">📅 21:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27728">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a75e1bc211.mp4?token=mqRgmoopKiCLuE9tXObbtAqZccil-Hz2Uk5V-hfUW6ukuSUsL7s1M-hcwsMjhMqKXtnAPqanJAW97HZBzkYXh_Btm7LM9j3lS_DDReyVUqNkAs8Nk03WOAqD1R-n6yO6Jbhv3RFJuR4yz9YNxa8rpn61d-kGRo_hhnulqGqfYhRqj_4c9kgyAeruBTZBCHbYb3EwtS1TuKLYNGVsPE5VuHUeFr0NyxKdPpLDMY6VNXRikFXSWg4hb-9EExWbSEZJW03K_E8bANiTiF46PnxBGFoYq2KPIqhbwzRWYlBcO_f0ZZRqRc6sFR5PVqVNDIxsutKvnn5KgVrFn546VocZMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a75e1bc211.mp4?token=mqRgmoopKiCLuE9tXObbtAqZccil-Hz2Uk5V-hfUW6ukuSUsL7s1M-hcwsMjhMqKXtnAPqanJAW97HZBzkYXh_Btm7LM9j3lS_DDReyVUqNkAs8Nk03WOAqD1R-n6yO6Jbhv3RFJuR4yz9YNxa8rpn61d-kGRo_hhnulqGqfYhRqj_4c9kgyAeruBTZBCHbYb3EwtS1TuKLYNGVsPE5VuHUeFr0NyxKdPpLDMY6VNXRikFXSWg4hb-9EExWbSEZJW03K_E8bANiTiF46PnxBGFoYq2KPIqhbwzRWYlBcO_f0ZZRqRc6sFR5PVqVNDIxsutKvnn5KgVrFn546VocZMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
رونمایی رسمی باشگاه پرسپولیس از کیت جدید سرخپوشان برای فصل جدید رقابت‌های لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27728" target="_blank">📅 20:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27727">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a0da2836.mp4?token=Xvz9cxoy087o0UHsRJIzv7FamUjvHBBZ_vkm5ylBqPbv_vyt184SK-izuQl9NpR46dsIRInuYYeGkNr4w-a_aGAGJ1BdbnYDMc9U6Mh8NUGCtb49zurylEBXnBRkviMAcfqBAfeBt6ZM-P8O6b82JvflqFEcA8oWafG1kqpdhPIMHWou3LZH_ubUrlXMp1jVcH7EZTpBNi_pDn813MC2aY_ntZO2RuV3GsmIAO6xmyx1X5zFm87_cxhVAjJco1BqRNIuu1KdW8N9diAxprskIJ96RNX7xeDmTeNvBYAD8dbFxu-IeKlnrWxAdc-SpqPeVDBM-p30BAPVS4oqFXkyDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a0da2836.mp4?token=Xvz9cxoy087o0UHsRJIzv7FamUjvHBBZ_vkm5ylBqPbv_vyt184SK-izuQl9NpR46dsIRInuYYeGkNr4w-a_aGAGJ1BdbnYDMc9U6Mh8NUGCtb49zurylEBXnBRkviMAcfqBAfeBt6ZM-P8O6b82JvflqFEcA8oWafG1kqpdhPIMHWou3LZH_ubUrlXMp1jVcH7EZTpBNi_pDn813MC2aY_ntZO2RuV3GsmIAO6xmyx1X5zFm87_cxhVAjJco1BqRNIuu1KdW8N9diAxprskIJ96RNX7xeDmTeNvBYAD8dbFxu-IeKlnrWxAdc-SpqPeVDBM-p30BAPVS4oqFXkyDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گل‌اول‌استقلال به مس‌شهربابک توسط سعید سحر خیزان در دقیقه 45 روی سوتی گلر مسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27727" target="_blank">📅 20:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27726">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQI4dyhKkFkTwI1EhZJCVZDdrhtvtrEMbHF8ncZ4_pL8a5xzyIn3XBecA2Fgl9I8sitpK4uY70waaUo_CevlDVFU-anpbwZq3tAYhpFWLJqxzOYb67Bfus4qxNILYrr4Iv4weAugYKm54bQag0yo3mEr_16zQgbHWJgHv2aXxEGm8SwfXw16bDcdpjUOh-OpUmJkZarQ6K1Uh7dI3dqBOpd9fhryKo-zl3SzYp-fVHDK8-GAk4EaM8HR7qIzzdL_9p2FoRztJMMismtb1pmlE_ved3LF-KtOFyCWmmOu63EIS1-bwv2YCUQRYCnWoaLmpaBqsGDxoIlD3igZ3c0gug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27726" target="_blank">📅 20:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27725">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e32a2d766b.mp4?token=K2A2YcKNdDikJ1JQVizmPe3mrJB91ZNRyicRiq1lBVctA8acUFSzzNqzDLI4kjqMEmkrYYSzT6eL27zK_oxuaMA18kdgltbBPINZJ4mwJ9z_PAfpS5ARPvVoHpKCtZIcMWpU6i4Q0dpOBFLoCBUbgwOIQFrtIuEicfNG7Q0ZTduyL3aMWn_-AUJsEHQ5tZ090GKHHlZWt6wu3ZA8cWazzpcpSNQgd4I8RrFt81rTvHGW3KDt_9hYBMnFlJhEN9DAglkXJk7VKwz4hXc42wfSQBAKmZjKWCV79UbslBvJN1yvI7wiY7w9aapA2ahSz3uTK2zyplJCTzhV7k0MF9wh7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e32a2d766b.mp4?token=K2A2YcKNdDikJ1JQVizmPe3mrJB91ZNRyicRiq1lBVctA8acUFSzzNqzDLI4kjqMEmkrYYSzT6eL27zK_oxuaMA18kdgltbBPINZJ4mwJ9z_PAfpS5ARPvVoHpKCtZIcMWpU6i4Q0dpOBFLoCBUbgwOIQFrtIuEicfNG7Q0ZTduyL3aMWn_-AUJsEHQ5tZ090GKHHlZWt6wu3ZA8cWazzpcpSNQgd4I8RrFt81rTvHGW3KDt_9hYBMnFlJhEN9DAglkXJk7VKwz4hXc42wfSQBAKmZjKWCV79UbslBvJN1yvI7wiY7w9aapA2ahSz3uTK2zyplJCTzhV7k0MF9wh7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گل‌اول‌استقلال به مس‌شهربابک توسط سعید سحر خیزان در دقیقه 45 روی سوتی گلر مسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27725" target="_blank">📅 20:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27724">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32b2ae1951.mp4?token=oIoUh7MKa_RjroA9WqyiWUdExTjiInLHZ1uJNklGUh18Pxa0eczCTNd3JanSQlVsYmYvhpJVvQMxQm0yfDDxrFMQvDBDziwPOI4Q_TjUQdHu_mNpQQYWrz8CwFD4yvcjp70RofjAWgFB6bSO1wZrX8LJPniNqnxlaq4-EURnPCGrJ1BP5RgbUdEqGXimsCmuIvkhhPxhGkDWmEwAhPeBBiJ2Q0-DaN95AAeNoXI5MbwL8iXnGnXFgTiVPJhI76-JAy8bwIWqFyZG3qbqueER_bfgsgbAsws6oNYGNs7Hgujngv2MJVybbQyvhI9sIDlsDYmB2vcZ2Vrc2kQ5vCnC5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32b2ae1951.mp4?token=oIoUh7MKa_RjroA9WqyiWUdExTjiInLHZ1uJNklGUh18Pxa0eczCTNd3JanSQlVsYmYvhpJVvQMxQm0yfDDxrFMQvDBDziwPOI4Q_TjUQdHu_mNpQQYWrz8CwFD4yvcjp70RofjAWgFB6bSO1wZrX8LJPniNqnxlaq4-EURnPCGrJ1BP5RgbUdEqGXimsCmuIvkhhPxhGkDWmEwAhPeBBiJ2Q0-DaN95AAeNoXI5MbwL8iXnGnXFgTiVPJhI76-JAy8bwIWqFyZG3qbqueER_bfgsgbAsws6oNYGNs7Hgujngv2MJVybbQyvhI9sIDlsDYmB2vcZ2Vrc2kQ5vCnC5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شماتیک ترکیب استقلال برای دیدار امشب مقابل مس شهر بانک در هفته اول رقابت‌های لیگ برتر.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27724" target="_blank">📅 20:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27723">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnD8hLVy8o3qZXB8OZELZNA6e8dJOasEmSbtFhpDfzwMVJsFPi2fK7E2JjmukEjr39L3hc0Q21k6Xnm2gUqq-11gB5nE6qt5D_Xz8gbqeH1y36qM1uoloQRhbdwXkLx4NWaXJnooz56KDRrhR8DSawnb2KGb5YN2cdPyeyNIjfLa9H9EF553iiJatczOW9mbU1x0GV7bzviMFpT4ZB1xDGvT57HUBZNj5Lh3pT0nWds-J4IxhMXM4RUxHrLAodOwrKMEXVE6ZrUPeVBoXJExo302pxkv3wFzXOiDziHK0zXFX7oT4rLIgZO7dlXEEMkaLNLaYOmXSFqqEm7CJGTvlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دبل‌ستاره‌بلندقامت‌پرشورها؛گل دوم تراکتور به پیکان توسط شهریار مغانلو در دقیقه 45+1
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27723" target="_blank">📅 20:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27722">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WERTnccRYL9JOYFQOQdSTvLLlqcPVps5ZUcVZvYLnLMAyLXm9eL4obMwX3-_CCw4l4iX7jZBWKhhk4x_rQHzd18T52X0RRhlMFXAdyhwmtduytP474TbL3uUxije35B9HaFfF4ZGY7fUrdM97OdqkBULdEImk-DN_8UcfRV_o_97PieoXFf7KKinWZ6Wlu1bGD51-YdJOtrlSCYdQnpVyH6TvRhD_9Co_mkxfBS_gKd5R-FdFv5I8gj5UjZVmSb4IO53K1Y-F1_SX4cJXm6h3QYUW3LhCqTMzeL65iqutAbsrUldXu2poxwDMC6_nt39boV2DkXo8xofexAn-H6wjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ علاوه بر جذب دانیال ایری و جذب احتمالی محمد قربانی؛ باشگاه پرسپولیس یک بازیکن دیگر نیز جذب خواهد کرد و پرونده نقل و انتقالات تابستانی سرخ‌ها در این فصل بسته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27722" target="_blank">📅 19:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27721">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCha2yc5UJa3OY8PqN9WP9Hd56l78Gh5V5h2G0xUiLG5gSskEeffoi6DygkqgOS_FmDxZEihJQ7n_5LjOKJdyfvdpiz8K6IFQ1VRnxSPAENx1r3AjtQGuftcLY2Ke5IPRoV-PVutYYlGfnba6BfOekeepIC9kGH25lOgaHWCUBzxCogfHdOacbj3TObgwS2QYWiM9gBtN2dcKIhfuKi-U6romJJHW-MBMuhrGJh20kjIsQU9Xr8XtSK419nAI_CLfLEvZmGmuBy_v4B5xDoDfliNlMHx6FfaiUcT0CCrjASmcwDnMw058aiRdKFd9DSJ2oRvDdVW2HUzlVKkb6H9zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
همسر رضا جعفری مهاجم جدید سپاهان که آماده دیدار امشب طلایی پوشان مقابل چادرملو هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27721" target="_blank">📅 19:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27720">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkzJ7o82-oYTNbw3tGdRk92h8oinjjFPvLlwJneG2OzwLcGcU-VsOT_kAs_FnN3nCbiEc-YFqCdyaGgiVt8keUC7EMyr6Zg7F1ATcy6Z1T3BXS_ICjEMIRve33Ok7024Zh8tEDPI77GAIQWZpTxtYtHBasKiYtIKLZhpdFWK9nnuNpWtejXWHKOD_ybDlad8DgY4Eh1QQwoTkUQvNMjW_GZbBgHEVIoFDHMjpHQbSxnr23YdBMh1uyrGm6AV0zM1JhqcIRbcPAdOd5TOIi5kKH-GFHM9t3Ly8etAF02fRJpF64v9WyOqNvTyfz8CCsqP4U28_B8m_VIFf_oKj8OXvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو قبل‌ازامضای عقدنامه؛ با جورجینا تفاهم‌نامه‌ای را امضا و حد مالکیت همسرش را مشخص کرد که چه چیزهایی به او تعلق میگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27720" target="_blank">📅 19:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27717">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_NxeBp8d-3XlQqwz8oW690imNpBK35F-CsU_8UpcC_7zAL8IWEhgQpfk5clWkQ1LM7E3DWPhWNhMCF-jOrx3rSuX_-FwtXLQ4IPGGGTV3toIa5HEqxtwOcB_hxHvmjLcVEx0X-INGVm5GZgc6cDhCB65-h9iOXkgH9BkQeR4Wz_gy-joUtVvDpvyz0qoEUR2BFzJQCBc7sbsjbPXEnXpQkVSVUd4GmwnutEYGgScWr0PvgDBB_Ttwm_StJItIZ3D4VxKenl4cNdTy-UDbQksMw4uyEBOYcHE4PP7pCusa4dUNJEJYhsPXHQWUhvUsLR1zlvVx2-QkHYTkOF2UoXbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو بمناسبت ازدواج رسمی‌اش با جورجینا یک قصر در عربستان به ارزش 22 میلیون یورو ناقابل به او هدیه داد و به نام خانومش زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27717" target="_blank">📅 19:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27716">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/342fbf13e8.mp4?token=SUrUTllpmyh5u-bOvXYgVkNFZ_7VhNDgVGm8ZvjkrYLHwfaJ5QBV905u6PO3OQaPQyP_vYuP_JA0UJrYe_yGKKPE3nI8lnJloowlO-smypcYAouPWwzMcLBaBxNzysvOy0CH3Si7EmGxDO7-0iyugMG2NbOOXtYbuqakwJY7eRLu-bQNRey9lnOwVn94rTXg3FJLgzIzEKV4_QISsu5YLyizEyFsfT8SarXAIeS6xsA16Sdp_q_Dp3d1Y1h0NcoeEbijaIa2GdeXcZf11oNfLEcRB7mjgm_eOpXnvbk_B3klrm2e-9oZF5hzUXICXUOTQZjFraZkfWwMLYlOX2HFzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/342fbf13e8.mp4?token=SUrUTllpmyh5u-bOvXYgVkNFZ_7VhNDgVGm8ZvjkrYLHwfaJ5QBV905u6PO3OQaPQyP_vYuP_JA0UJrYe_yGKKPE3nI8lnJloowlO-smypcYAouPWwzMcLBaBxNzysvOy0CH3Si7EmGxDO7-0iyugMG2NbOOXtYbuqakwJY7eRLu-bQNRey9lnOwVn94rTXg3FJLgzIzEKV4_QISsu5YLyizEyFsfT8SarXAIeS6xsA16Sdp_q_Dp3d1Y1h0NcoeEbijaIa2GdeXcZf11oNfLEcRB7mjgm_eOpXnvbk_B3klrm2e-9oZF5hzUXICXUOTQZjFraZkfWwMLYlOX2HFzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شهریار نیومده‌گلزنی کرد؛ گل اول تراکتور به پیکان روی چرخش دیدنی شهریار مغانلو در دقیقه 36
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27716" target="_blank">📅 19:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27715">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c3a29973.mp4?token=mjB4BXJL5RayI8D0-zukS_wesQv5yl6QhRF3NlFQqDt1mUfWdYsJltJeS9pAomakkKnP219r-paPgwnzDot8OqZaj1hTbKPMrazy4n19T0xhb_DMjqz7H_BfaEOUfjenkoj8ve945PBdNvu1e9rjTO2yH1fWmzhDKlt1WDhh-g-GKsJnN8zQYmMxd-uObZdbcP32vO7DkK1IEptZIyyrfMq022OMsgI1ZpBy6sr-5sUIk0woXV92QYJ1c8GXitXEgYMv4x4O2AiMS6oFKKwXgfs2sw11tpz8OpuwiCYUQ1W5TB1av2HtMl4qw0ZpibtCmNCcsdF5CIzrWzGfybREYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c3a29973.mp4?token=mjB4BXJL5RayI8D0-zukS_wesQv5yl6QhRF3NlFQqDt1mUfWdYsJltJeS9pAomakkKnP219r-paPgwnzDot8OqZaj1hTbKPMrazy4n19T0xhb_DMjqz7H_BfaEOUfjenkoj8ve945PBdNvu1e9rjTO2yH1fWmzhDKlt1WDhh-g-GKsJnN8zQYmMxd-uObZdbcP32vO7DkK1IEptZIyyrfMq022OMsgI1ZpBy6sr-5sUIk0woXV92QYJ1c8GXitXEgYMv4x4O2AiMS6oFKKwXgfs2sw11tpz8OpuwiCYUQ1W5TB1av2HtMl4qw0ZpibtCmNCcsdF5CIzrWzGfybREYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ ترکیب تراکتور برای دیدار امروز مقابل پیکان؛ ساعت 18:00 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27715" target="_blank">📅 18:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27714">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haA94MexpS3k9Ew7uK7cje55EDpKhu4YfZzrxcQpe7y0jpkY9h1tvKZfQ9_oA9TcHPARWE6dh37WjdzTQiz4CjCnj5ANXA9bjvEDZF4a3zYiMq49uJyxWXcM81S16O9MzxFvRQJRgln6z-QpjSBkYyF5RZWyyhfFpLBL0tew8Ss3VIJ56iKRnOUZcRB8-PgG_fU3C8zJlfZ_aOGFpaiBb5X1MV0-HR-DYG8TZAo21Vgm0WasWdq_LJgs7ikmmvFI9ipbBxw0Wgpdnx8EWx3KOVs8Y_63WDsquxvjkV8FyClJRAoEP8C32aVouFFzrSNCD0XIHuORfbV9HwVF2V9R-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ ترکیب دو تیم استقلال
🆚
مس شهر بابک؛ ساعت 19:30 از شبکه سه سیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27714" target="_blank">📅 18:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27713">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGWN0_9Dxxt8ZNDtTi96WATeJNZhwNb2l3s9kHXPDU4g5-NhrujAZStaAuA3SzUJD8gXqgq4yBhcwCf7vAe6n5CiZ4pGwPBCzV8Et21h62VFpHf8MIbhtccxW5vy_xiQTHWUhzBjNhQ9tc4ooDcRKBVPEJt4thNCdzm-BkcMrLLy-DpolevdeTBjJ9I0DH6qF922TioaMfBtn22YNVVlbecXDNaM16OsEvd8O6Mcol-jkoE2bXnIg0qIAc1FWH8OBzqKFZL48lUQDhd22ccrzOMWba67zbZ9VAxrjQ2ILltOPAqkJEED3_bsXv_St80kTSlvXcp0a-5UqzGIZnrggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
شماتیک ترکیب احتمالی استقلال برای دیدار امروز مقابل تیم تازه لیگ برتری شده مس شهر بابک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27713" target="_blank">📅 18:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27712">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3436fa84.mp4?token=EQ-pNBrGhEji2EXwl-ZkgtLHSKLHnJv1tUmu2AxbugXKe26dGucWbjp7cmtHcFH_RKkZPIhMfZWBIXGdFG2lEM4I43xdxUrES-ZPGpgWIpFlgiYYOBpeNyOOscMPYISwwnWeIvKIjZgpV-3sfwyAJ5OQ_aYMu-qW9S7Quj5xY5xx7QXu1XZe4viFrfq0Ljb1vtaX7KUPnDT5yDPjMZ6_WI5vcg9k3GTfpmZbbRVJ50P0JRvCsGEsRa3tSSvn6LNbx1LMCSR8GaLBQqs_EH5kXGaWoZ4DqQcjfv4SBLBMSTO9C1kPg42kAUVIz3wb5gATj--8oZFde3OO-ZT4C6N5S2-6lEyaczsMEaTtud2-MnwxiWjy7EjtafOx8UooBshePtw-voI486rCn-VgIU3jig7gEtW_klcFmM04RWNUeZrkr3z34RcS_weUuK14zsPZ42vjyDtg3bAAgf63Zr350kLuzu1XjMaPM8KjKI-nZzGRY1K7JH0yWdAQnEYESl7adN1eSNV0qpvwUBPo4jJ2M-akFn9bTfjNJjCh9R_-C16ccGB90syddNGe9Z1jSpf5flDVx6h5WqwB9eVDAAcC94s30M3HPY8vvAVSgeWVIMmYYq3mqHbVAKG8hZXF9RG3gIw3jsi8PXyvanIbdUOexBKRodCGjpipv6XQF8FABqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3436fa84.mp4?token=EQ-pNBrGhEji2EXwl-ZkgtLHSKLHnJv1tUmu2AxbugXKe26dGucWbjp7cmtHcFH_RKkZPIhMfZWBIXGdFG2lEM4I43xdxUrES-ZPGpgWIpFlgiYYOBpeNyOOscMPYISwwnWeIvKIjZgpV-3sfwyAJ5OQ_aYMu-qW9S7Quj5xY5xx7QXu1XZe4viFrfq0Ljb1vtaX7KUPnDT5yDPjMZ6_WI5vcg9k3GTfpmZbbRVJ50P0JRvCsGEsRa3tSSvn6LNbx1LMCSR8GaLBQqs_EH5kXGaWoZ4DqQcjfv4SBLBMSTO9C1kPg42kAUVIz3wb5gATj--8oZFde3OO-ZT4C6N5S2-6lEyaczsMEaTtud2-MnwxiWjy7EjtafOx8UooBshePtw-voI486rCn-VgIU3jig7gEtW_klcFmM04RWNUeZrkr3z34RcS_weUuK14zsPZ42vjyDtg3bAAgf63Zr350kLuzu1XjMaPM8KjKI-nZzGRY1K7JH0yWdAQnEYESl7adN1eSNV0qpvwUBPo4jJ2M-akFn9bTfjNJjCh9R_-C16ccGB90syddNGe9Z1jSpf5flDVx6h5WqwB9eVDAAcC94s30M3HPY8vvAVSgeWVIMmYYq3mqHbVAKG8hZXF9RG3gIw3jsi8PXyvanIbdUOexBKRodCGjpipv6XQF8FABqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ درشرایطی که ماده شش فیفا به برخی بازیکنان اجازه‌میدهد خارج‌از دوره نقل‌وانتقالات ثبت شوند بندچهارم ماده ۱۷ به صراحت می‌گوید باشگاهی که با محرومیت دو پنجره‌ای روبه‌ رو شده، نمی‌ تواند برای ثبت زودتربازیکنان‌از همین استثناها استفاده کند وبه همین دلیل‌باشگاه…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27712" target="_blank">📅 18:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27711">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkTnHnlzetQTvTJs9WDQE1CSPh4NzXntT7bBinnEL0p7Nfn5YU6VD0qW8-wNE18GtDJvywAXJOxtZspot6bt0WJ3QkODhPME7YXf_1H_2wFc10c9KZ54RHMs7nFheZhrr36P6hHe6UoZRMuiylXSLq8iKoa2N4FGMbdfUAOh72edRXA-k8U_AzedgilBB0jYetdEowrKAE7v7kzFMSrYXO2P4KZCLx4SlSHVcdG628mupHHgGCOhCkL7QrJWB9qh-ZD3DQobSOavKTYYV1jEP4M754ZDqojXCBcZQoYvBTGgUEfXTF59W_ieRATPRkjutoEubYknJjTaFJ3d26xhtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
مهدی ترابی ستاره‌تراکتور از ناحیه کشاله ران مصدوم شد و به‌احتمال‌فراوان همچون مهران احمدی یک ماه دور از میادین خواهد بود و دیدار هفته سوم باپرسپولیس در یادگار تبریز رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27711" target="_blank">📅 18:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27710">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXgLgSMqlTvL0fBev5YBrEHca8S7RZILfUNEvlNIal6Y5nzyuKhW5CA2NxFJvCdYDs-UAP2ex4KQeovzxdTfGbf9efokWbYlzJ36BUzsCmNTafBirgWO8dYbnKYkahHcV_BNZrDXPPgkvIH2Wv8D1vc1uO8PFKpwW3hOOlhAstpbiY3WX3X7RJjdhA3Xvpr_95Sfu2OEEoeuBOkWd7MrEvVjLL9Jj5tluXcEANlhS45gaNZHPEdfYWiWUnjKVON0spLa5mea4sFRCLsRlDlshbtjXHh-8-HpVktF8_n9bKVouo1sB8P_hyL7nTtvYX1fJjbYLJ-5YyDcaBW8vDBp8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
استقبال‌ویژه‌بازیکنان وکادرفنی‌تیم النصر از کریس رونالدو بعد از ازدواج رسمی‌اش با جورجینا؛ وایب صورت CR7 خیلی خوبه. حلقه دستش رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27710" target="_blank">📅 17:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27709">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcUHwFXHV9TpQP2pfdSXImlq5g3m4X6sbQJCmTKFnOF3OY9JCCCG_d3qILP0x0Fr_YU_OGsVRb55KiunxstpooBoDGIOaN6k5dGglvbOJEDosKM6c2n-vbqon13-arG01O-94mzlPWI1CxIvEsW6JnRuRH5QW2oc_nqI9QTzifSRigWnvdgVziPfPUPWvANhHmUisvwQ1DncGkx5KnEqx4BHjKfZJ5woYnH8TRN9RY0hDtMUb4Gx_D8__dxaphWWdcCn-RFm2iI_T5wRVC5K8i2g3bBkVkEVQPSOpwUPH6344dljJimbVtUGmmaSJSZNXueNpLptOj29FxZWh_52CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
الگو برداری باشگاه تراکتور از دو باشگاه بایرن مونیخ و منچسترسیتی در طراح کیت جدید این تیم برای فصل جدید لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27709" target="_blank">📅 17:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27708">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6acf648940.mp4?token=HsCZf0uYQ6P2G0QbttTxXPcGRgChaGNYoBo12mPMO9lSQhmcbxwVEixQoaM5R5NrVVmtR8eoZRJq4Qa8L2IOxPAmeuSfL_ckkW-BHC_qCKJH2mKf4qhMlOODNXpLtlwXnh9st7S1jU5fU-8mD2t8u5xRVFYZHK8hyVQomanFz1sjK44KUnUDPm_5iHJQNXm45bcCf8tGAVLaGWLgiD9kYGQ3SWYWHn5a9Lf0JoccEQ4_u0efilLjh1jPmGW0TahEntjM77Uj8g2FWOx9W13y0pgrquMQ7eldJNjxu6zXd2FKGsNqlzCDM1FWpKtzAwRFDqri1mvaVKgob6JIk04hxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6acf648940.mp4?token=HsCZf0uYQ6P2G0QbttTxXPcGRgChaGNYoBo12mPMO9lSQhmcbxwVEixQoaM5R5NrVVmtR8eoZRJq4Qa8L2IOxPAmeuSfL_ckkW-BHC_qCKJH2mKf4qhMlOODNXpLtlwXnh9st7S1jU5fU-8mD2t8u5xRVFYZHK8hyVQomanFz1sjK44KUnUDPm_5iHJQNXm45bcCf8tGAVLaGWLgiD9kYGQ3SWYWHn5a9Lf0JoccEQ4_u0efilLjh1jPmGW0TahEntjM77Uj8g2FWOx9W13y0pgrquMQ7eldJNjxu6zXd2FKGsNqlzCDM1FWpKtzAwRFDqri1mvaVKgob6JIk04hxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛شروع لیگ بیست و ششم با مسابقات استقلال، تراکتور و سپاهان مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27708" target="_blank">📅 17:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27706">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYJo6ZkLWCSIw_LPzTglezP0DLoAvKWowFIpEjGj8tRh_8N7HAoGPAuHkqOkw3vP-VpNtqzl8nyhZBl_5OA53fRujdrfxlDn5fDAxBvsF1c01i8lNu4fzPUXa5tCTAbYX_bz_hofyPpI5iNGk6l9PmYptN1OGStBikKcet06p0FDxUF7XwunrNtcXVYkb5ocJ2CyoeGnAP_4ygqpp9nSh_c7hxhuuEoipXKCTTFXptkLfNt_ES8M8P9bBv4lZcKug7FmClCqpN97pjfqyHlOykM5qlGpK7ljo95_9RM131y6nEjdsgkiv-YE4jKBGagp_J8tG1oerqAHl_23uAj3eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jgot6FwItVQmsBr3UmbCbNUJoT8GmvVtGEX9VNtjYodNdpc1qexADpv4Hu2Ne2TFlMtCbX_dVU_LkE2vrNOEHADVFQKRlZsM6JH0UcEi3wxC3GsznXIJYTNlfOvPKYDhvLDJkDj86NdSvhdIwIYQU8oGJlXQZapoypqR063QFRKhj3tRxdAsT_34McB_mXjqfghu0uM96D3IUaSrU4ysxpcDIfJgIDsvCFWruaGxroUxkGufmXUWnbxWDLyAA_VBXeTwuoWmWFq1itw4Mr9LU2HiIGrs4GGDnU9Jub60k4yXoDKtzNRBMVietDZdDarWlyKyl5INSh4z1BUce3Fnuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
الگو برداری باشگاه تراکتور از دو باشگاه بایرن مونیخ و منچسترسیتی در طراح کیت جدید این تیم برای فصل جدید لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/27706" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27705">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKPKBOpKS4F3DexDRoP0aprhnOkZN8DZXhZblz4IRpEAPB0mEl3AOAzIW-0pYwNgjvI-ktHHG0CaNz_ClWYkKDpLAXd76iUUpzLtvk6aiWLOtmZtA-y3W8IYqOqgafh6vm-UnAAjoqK6IE1t0Ogln5KMIKw0QYGP5OhKimUXAsT9MqHVVYjEG8EXnd3p_w6Fk4OJUD2ZI4O1WG4Ml86WJN7HPeTkuKGuXLEflbbqPKB-AnZlM18S3xA4pU1BJ-wQ4JnB1lpN6HYlodrQylzl7Uw2A1rZMGAVKCVvrIC3aXVP3toySpW9jjEh4MXOHXJ5qkHPNSshoaVvTEb6Eqgwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل کارتال ظرف یک سال اخیر با این دو ترکیب کارکرده. جنگ ۱۲ روزه واسه اسماعیل کارتال خیلی خوب شد. فرارکردپشت‌سرشم نگاه نکرد. الان هم به جای کار با علیپور داره با لوکاکو کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/27705" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27702">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpucZcq-FcMV7yGs9cP1EagXBw6Outx4_a-7MWCYFhq7fY8EuqxJRps9QpWXPAt-sADYZs3bDbQ4t3nVlfgOvXm89HtnfXTFpcy_bl_LaXYIrDNrQZlA5_zADvO22yPVK4ErA53YpDZ0mi-DTosRICuEJHmZh77VAph1w2_8rgE5ky4grEh7e4uRjcADh3TH9FiVeqKYeuflx7rF_cOMYTLDImbqj7UBxMgoFEUZDQxKNbcDT1cGQ9L27QVzUjpZQfafjZH_Oz7DEgnWYbiW3Fqh2iBrbpT2dAN7az9GXznUVAKWj2P1aVaGdqqsftnxV8Vnd69tAeq5Y7zTsgVVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfKwd-lY1jbNRjSEAeDF4ggC8dhT-AUChOvKXY2JSh_siiNLOWjfgf3OStDLy5YkO9scyx6qIHcfZu3HK7PQ_Rm1uLseveDzmFMc-YXT2U9ofH51qRagbomWQL6-mgr0UVrUCY7DAxfvJXs87Jui1XJ8rwYQ9QRJ_-_8u01gROnIcmbjvVyU2R_lEknDwCLO_YxoZifvh9etLLoJccCyM8EZPC6sddQcbF1ih4-LmhrTgkoQVKi2g7hwYq8sSaHSmFFefCRrXwvAZZQb2bRRaoPwnVLScyMlvXTSHC74YNPhGMPlppiW7Y3qFRfVJhH7cfGCA-4ZLVKmKdXgvroVMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📹
ویدیویی از مراسم ازدواج نادیا خمز دختر پاکو خمز؛ خودش‌خونسرده ولی پسره چه استرسی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27702" target="_blank">📅 16:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27701">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQaa_151opE3ygmn_-JC6uevFGVcoKGM_i2HR4A5EwcwHSe7cwWJALu5r9i-x8xA8y7kZ6dsUvSAlcp-E0PY3IfclbvTplxWSHIZGzVJZ6zT1kJB9cTJ24GQjLeiG_psG0l1R_sgsLZp9RlBTmfwmMM_6WpSg2GMrvanzbkQJwERjKSX3YlLnSZTukZLgRw2_GEoWTDmG8w_iinJWJl3yb9Kcxe9Vwiq6lnFL4VsuQ8e66X5OcSF4dxzvo91-J9tCX6kjHPCFC9GMyovrDHT8xTDl1C7dO0hQMU4T-NCv_ECHRIq6qHgNCWNraBSASIoQO_vVBPx2maJzVw6R6p4Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام باشگاه پرسپولیس کوروش اژدها کش پدیده 19 ساله فصل گذشته آلومینیوم با عقد قراردادی پنج ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27701" target="_blank">📅 16:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27700">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
🇪🇸
🇩🇪
#تقویم؛سال2020 درچنین شبی؛ این نتیجه رخ داد و بایرن مونیخِ هانسی فلیک بانتیجه هشت بر دو بارسلونا رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27700" target="_blank">📅 15:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27699">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRKbttdzUB-4M9JoKki_GJPwtsL4NIGt4og-8fDOPtszVADunofbGXHXM54GCNH4j7L2P_CAxFI4pB8juYjl7EOPfHslAQuVD1hLuPQcsWnVIWIwUuck1QNus0yhDZPSZjE116mB-iwxYJR6nBVTCR0IWahqLcIyPK6e8ezkUJbIBD537GK4Z2P6tJg6wXhG80wlqNkvfbMLbKU55v1JR2SQPgxixMMrDiJPjxTPZXCafWjNXINl3GEuPyRxB6qHctlPWPQmo_M_CnpwO-XaA4W7cXcuRLNhVeJNYNdB9UDhrpQzrCS_9oNyxuPFbezjZlytWGbCWi1TXuHtqPrB2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛شروع لیگ بیست و ششم با مسابقات استقلال، تراکتور و سپاهان مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27699" target="_blank">📅 15:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27696">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MU8FrHpmrAWJqhsXbAqVKhs1lp8JNo0oZx9H67fg5Y5nhFCGiGtBx6_dLbKg7TrwxqmtEd0ClK31m7TEWiRZSx61jOUcEwvktrgrJcB2m1yyqckFDmfhw5pZe0FBPz2FsK9T6gQzkr6gd4RIoIdE3zOifAFfT4_sHGNmJ-M1x59QM8tZ49xezbt3vo9HylX2q9T0QwlAg4sCUCTn2AcAmUOeis_wuiDcMcej5n8eCohApNcfo70vamDNQWXqNm6Xsb0RNVGvpWMg6NeBSx4NS7wckMWIyB7o9gfEOa7IeFEYhuu87KPF1X_S7UVObe9HKLUAvkl0HI3AKIGVpKnujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ به مناسبت شروع فصل جدید لیگ؛ تمامی قهرمانان رقابت‌های لیگ‌برتر از ابتدا تا کنون
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27696" target="_blank">📅 15:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27695">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDVe13AVAIXfrtkDiBuKv9xgJvWvYzL8aFqMyjXk6sbVM_WJTt3GBWVYVORPdDcLG3FT19RSOCIymPSFk6K34vKkgiYHQU_AauS3xM4Rw83y27K3yYhXo-OiTTx83PolKNOvVopus58q4ZHaJcXHFfow9NhFyJghSEx3RQQYFpgVzIkCXR24W9J-WIALzQ1GodyGgmRpp7R6txakxo7N3enbbf-2N0pkgcOJJXnDM4PaVhgVVK5NpDmajpBTdSEF5OY7AJE6YDRadwlneVcaYhSatx_nlO7Cscyr2SYbdPkah7gNTbxz1S_in9_iN1tb5ak-mMj7jESXpiCiGChJDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ موندو گفته:
چیندو اوزور؛ بازیکن نیجریه‌ای که در بازی دوستانه از هوش رفت و پس از معاینه، پزشکان‌مرگ اون روتایید کردن و حتی باشگاه‌ بیانیه‌ای برای‌مرگش منتشر کرد، در سردخانه به‌هوش اومد و به بخش مراقبت‌های ویژه منتقل شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27695" target="_blank">📅 14:12 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
