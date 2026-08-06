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
<img src="https://cdn5.telesco.pe/file/nAxnj0MPRgiJyS_Q0rlaa6LWj3MhChcs6lXnGVpAEmHdJOzstvXqLiUiLOvqS7El4fQDMVoM1Dp5UNWHDBty9pgSsr97HdMA8ujPOMKyDLD_oV9Hgeb6U_a5AsaTLW9LLxoBqrRtLS7pJYehS0y5U5pUWGobqUzZ88m7UZfBLB-giJ3MiXB_LwOmnUJmXZ3AB33fCA211U_OPZ1HvJchWqrNUcWolECC2Cla68crBsU9XTGtZ6iWrikvIYZJKki53_kcaY6537kYnbyXtxMY5DYWDdJqz7dG6H2Fx5WFnXk1ZtbxrtGOAeS60mbYKqABlwA4Jq0oue7INwtGaEOVHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 490K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 18:14:03</div>
<hr>

<div class="tg-post" id="msg-102893">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63cbde653e.mp4?token=EiJeSJuqD---z4vGbsxf4afFBqvJrAJNL7Z7CbxKuCxVbE2P8EO7dXjB4xcxlreuEdGpDvaWw95B-aq9aSVsL2ZJ4rYCWmEm2TO0sKmEx8WJZyr6BzQfBr9ga-6Ex_e3uoDs1TVxRP7yeRaFTEpGXD1vyoZL44ESwREiyIWFjOT5yvKHGdTlAPbl5_mYbhUIhxkVA41-s-RyKIptNQ6EsmVwV6UzyJMeAqo3BoHYhUAKElcg-NbIiWHfLLl6EtLd4EgDyXCZUBwtXre9A9dtaibWxVUOYrWbASuQg0p5_hPoAod4otw3wg8ytL26jcKRKQ2KZZTx6Bs2CjWTmJdmVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63cbde653e.mp4?token=EiJeSJuqD---z4vGbsxf4afFBqvJrAJNL7Z7CbxKuCxVbE2P8EO7dXjB4xcxlreuEdGpDvaWw95B-aq9aSVsL2ZJ4rYCWmEm2TO0sKmEx8WJZyr6BzQfBr9ga-6Ex_e3uoDs1TVxRP7yeRaFTEpGXD1vyoZL44ESwREiyIWFjOT5yvKHGdTlAPbl5_mYbhUIhxkVA41-s-RyKIptNQ6EsmVwV6UzyJMeAqo3BoHYhUAKElcg-NbIiWHfLLl6EtLd4EgDyXCZUBwtXre9A9dtaibWxVUOYrWbASuQg0p5_hPoAod4otw3wg8ytL26jcKRKQ2KZZTx6Bs2CjWTmJdmVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خشن‌ترین ضربه‌ها در زمین فوتبال رو باهم ببینیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 979 · <a href="https://t.me/Futball180TV/102893" target="_blank">📅 18:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102892">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeYYiWgRHkcPc8tON2JPoP5ql8Lcp6Jok7V05zL-1DvmMmCMiY6sX0LNPZkH-0EwZnUB616KEYCDWaLogeWJbn1FlxMPnAfp4x2HRUVe2gttBX28hKeEeLqSp3RgW7GSWqH7Ovo38Eq99oKffJbby_SLkRINFuaf1TJzPDLjJ4VZpV9KsvReCbFB-C9AEqTSAyGNgh3L8MkpENsjW59wC0JJzYkP3JM-kiDs7TNpRdDQ8gy86xPcWC_8MJhzKSKNam8dO5wxXWXfqsC6ic7PN8WpTVPOZF8SADuVdvNZZ4EjjXflaTlXV9UJyem8CIegDLw8BQ7nQNCrGXkZM1b-uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔹
بعد از ورود دیومانده ، اسکواد رئال مادرید حالا به طور کامل پر شد و برای ورود بازیکن جدید باید حتما بازیکن دیگه ای فروخته بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/Futball180TV/102892" target="_blank">📅 18:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102891">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZVYgUY5yTyGg4N90Ck-nRDhrHNIuL35zcpl22et0CkGG6AA92tLMHk4Tl-HEha98pmxHsvERga4LNSSbHE3N7RSTeS7_97ePrpgswL3eGbj64jL9t2wL1wjPj9hAH299XSxavzS2UVIfdWXUDtB_FGbc6snydEqpJ3UnKsIvGVwXETr2FHUliowwsO-DlLrMy0uz0MJOE-PMaBBkgp6-Ldhv7Cspwui5dh-LGmuHqBqDhsoVCUUisoFoOn7zZIb2pSJDfdJ8g4l-Mhhlq4-99_tLc_s8sJJ3ibP5eAbvM89YnkJqrSuqfNc3S230avEgjVivRO3yrNSr2vVOwaskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اگه تمام آپشن‌های پاداش قرارداد دیومانده فعال بشه این بازیکن تبدیل به گرون‌ترین خرید تاریخ رئال میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/102891" target="_blank">📅 17:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102890">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng4ULxHzkjagBcsTHBfhVzlX2nVwuR-xtjHUw0kKFYRMwFdH7llLlRWlYVMf_Yv-OWhBnoma5c67MG2mGwe24XCmF6cn6AUw8Sx37qBKoCP1VK-freRLsgP_nqwe94YED_W0jTmDtKDzV6fwVw8Ub5OEFiROwMhotSCMBMGdLjdCh3fTqhGE1OeahQJZaLYaOJ4bFN2SHnakeMjaD2gFyjBdllInKld0KWsxzSkUBt8nJivnPHsb3xqBk1yyxs45fRMoKgplT971Q6YmYt8BabLS18l8qTjzg0DtERFeE4mtmcD3pwNr8VW-Me4gJbZdfyEgpjrGHcJuA4wguYi_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
💥
🇪🇸
#فوووووری از جرارد رومرو: حاضرم قسم بخورم که رودری بازیکن بارساست و فقط مراحل اداری عقد قرارداد باقی‌مونده!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/102890" target="_blank">📅 17:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102889">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XT0fj4dgfU5xQTgR1QhWxh1e6Rvm1gTYLofM7kyCUEevC6oU-oe0F07S_jzplTZz1Ui0mpKxJoK6_XGTgHVITqn9UpKc4vo7aKk5NsI6zq7OnhxnjViueFs7EHv0UirFa2VF4-iLJafs1aIfVFrVAZw2WRzEecEDZ7r0ViDP6pNtTYzT4NlB5UDJaOzPjxMOwr3C4fhbycy23fwdHPUPHoJU-c9hrgVUVy12D5nUmCwy87UY50z5Ueqt76HmQDW8l3O1cBh1I2Kqw0W5ZFOw82r1ZI5lsJBDVq6_UXGYwWlV22zUYmZkvS4K1EqkqVRbrMNDn5s98Sm_MtyCMUZCKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
💥
🇪🇸
#فوووووری
از جرارد رومرو: حاضرم قسم بخورم که رودری بازیکن بارساست و فقط مراحل اداری عقد قرارداد باقی‌مونده!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/Futball180TV/102889" target="_blank">📅 17:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102888">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSm6xYQkvOCwlruC-CcWroKLU1dy1TXAZU_sy5SfEAqaDU07tD-mZ2-YYhGufuJ5-qFie310fA9AIzzMTkwweY4wpCzNIFFXWJZrESJRK3BzPeDMWPwgcjhSPv7wLMNgEFqvXIkKk49FOIIqBlshk8oX1bJPUhAoXynjcyP7s3BABk-oylSa79Ffob5A4SJILmBGBt7nOExF-zFckYscZpGH114cfzSZhjVXLPPA233Bq7LDRU1sXKOmuPqiXHAA_bFYJA64MthHe6om62YlLQlmIxO1Np1zb-KZQk3svV7GBukhFDcLEMNXTFYdmN_KNGV_1NHcgcaZ2qw4Ecl0zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
🇪🇸
#فوووووری
و
#رسمیییییی
؛ یان دیومانده با قراردادی تا سال 2033 به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/Futball180TV/102888" target="_blank">📅 17:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102887">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
🔥
👀
🇪🇸
فابریس هوکینز (بسیااااار معتبر): رودری به‌جای رئال مادرید، خواهان پیوستن به بارسلوناست! همچنین پیشنهادی در حدود ۶۰ تا ۷۰ میلیون یورو می‌تونه برای راضی کردن منچسترسیتی کافی باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/Futball180TV/102887" target="_blank">📅 17:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102886">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X69GiDpFtrm8tsBm8Uc3xKGxht8wFCUQIkTt0husZMS9s4cGGJlKmHI1tl60JPeD86lNgewtVEmeYb7nfJvebGv7dXlE2ciCzOYBpeziPX3MKDypKr3J2ZlnuTCLoEBKknPoaqFLQ1R5kpQEY5uy464EYc0O-91M4pd983JBsm3GENWesjRVpObrY67Xm7ctRPXVcG5VL1foKTF08GPNMVCl3oho_6MURrKBsOlHRUi0hj1sFwa4gpCmUP0yxwsEq5p55L1_4gOfK6_MvzgfaBdqms2a258NMfxg0MjQXtt0SvOsNqbeuChY5Bt3EgD4BU6emqj437AwwY81DH2GmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
👀
🇪🇸
فابریس هوکینز (بسیااااار معتبر): رودری به‌جای رئال مادرید، خواهان پیوستن به بارسلوناست! همچنین پیشنهادی در حدود ۶۰ تا ۷۰ میلیون یورو می‌تونه برای راضی کردن منچسترسیتی کافی باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/102886" target="_blank">📅 17:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102885">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNea-bBgsaXvDiW8n84hOVwcZllXNLcv_937MdwHJDoS28WyVV6fn7JxGH2AQTXp0uH1PH6Seu6-WmcXPT_qkMRXExbaERslWdn2EFDM9FmjY89CMXO9P3AsOkMyiCov2FLF3uEK75tLi79BA3yKRmGMMcLImBY1zJHP52JzPcw6uhr_Embn5Iwc6hhChRJBPtgyJ_o4nLySZMYGSWc98yKmN-_2ZNETI20DvcFrx6JhZHFczpENxDQ_0ZRhqRN0ETYYB3Glj7o-GyrAlMHeu0-75-ivhlxqkEFXcPmrMXSVV0iRJ8DUP0T8QaUZmrPsOT7EhRf0_lgiDYcynh_lkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
💣
💣
🔵
فوریییییییییی از جرارد رومرو: رودری به پیشنهاد بارسلونا چراغ سبز نشون داده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/102885" target="_blank">📅 17:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102884">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMnlA-ckrIxSIMzMeMlRnmg6-9ZqrXQfpU4EFcBIWI215rIwqGhDOgWUjZVMLydlD7ME4JUNkvTDLv_PJ2x-sCdPe2peSYvwk-giUc_F5koLpTK1oeJJcM_0yHuXQzTGWRij0mekm3Fi5PINV3OxB3PueoiRc5PkGaK98zT6Uky6mtkESsRn74nx_wTyOx-Ve3Gyhhbd5DfmdGrWHto3KHko2rwipvsuRYs_qQbcs3Y4r00rpFlDBj-GiQmEmFxi9n-8twilkPrEonux7tx6duPHoZWTSxIY1MXLV4VvHDI9vaugvmmXJXxdGuTC6mjXgcTtpCt-Awyk94Kci_LqHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
👀
پیشنهاداتی که گالاتاسرای برای فروش ویکتور اوسیمن ستاره خودش در روزهای اخیر رد کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/Futball180TV/102884" target="_blank">📅 16:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102883">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFZCpq7AyoJzPVDQy3brI0DniZzqQbKdO42ZPPEy1Q_Aq70XFi2pyB1zgOBU52eRgyY-_hj3cRFZ0MCPIGYaF70xwyytp4jDHfNPkP_wdJ2-008c-p9F9fBu2EXs_RAIQVYJ3_dPKLbpBNo2sRaweuVMVnluaFpeyhL3w2EPhYS6dV4tNSPdEoIXDXc3j1xFg-CMC3EkCSoMdkAUw8Cfsgl-ZSxgvzBCdvCDxTM51BJ-rHYg-FwitpqwmU7gYn5-migiRduQjoZrlJS9r5JnAhHyDB0NNmL7_Q9gB1JyT5bVXMujw-oV3QJNChd1QjZLypPaSEf5KrSEy-SSZBY2Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توان مقابله با این طوفان و این حرفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/Futball180TV/102883" target="_blank">📅 16:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102882">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f51bc68e.mp4?token=mnt5fF6iWnoTbr3Wr5lj4v5iR1AG3W9QtPmMiX9PiYfV2gGb7GX4L3LiMzTTzWdK8vuO7Gn_uof-jzoGbFDDNVV5zRWz1Zgcc3T9_klluPfNMsQlEVvpGlEbbHHwSSZtMcB5vmRzen1XiidGC-xhVLyXzXONPdwETpVTfqZbBkjnEUQ5-Tb_yz1VpVJAoKZrZJTYxODrrREAJ0jdS6iCBiMNZtFiXvWsFzd0EU3cHjbTY6G_SUSQxJzw7e6OYhkn8BmHBM2D495zo243Ga6h4nuKzCfVerBQaMphkidFB6utpdLeyv-1u7MYuuZiqwbff1Cm7JdfMJ65aUrk-opfuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f51bc68e.mp4?token=mnt5fF6iWnoTbr3Wr5lj4v5iR1AG3W9QtPmMiX9PiYfV2gGb7GX4L3LiMzTTzWdK8vuO7Gn_uof-jzoGbFDDNVV5zRWz1Zgcc3T9_klluPfNMsQlEVvpGlEbbHHwSSZtMcB5vmRzen1XiidGC-xhVLyXzXONPdwETpVTfqZbBkjnEUQ5-Tb_yz1VpVJAoKZrZJTYxODrrREAJ0jdS6iCBiMNZtFiXvWsFzd0EU3cHjbTY6G_SUSQxJzw7e6OYhkn8BmHBM2D495zo243Ga6h4nuKzCfVerBQaMphkidFB6utpdLeyv-1u7MYuuZiqwbff1Cm7JdfMJ65aUrk-opfuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
واکنش تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/102882" target="_blank">📅 16:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102881">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi4dZkK6HymG-tl6BzUVe7wDFQYevTzeiUghYfE5R11REypIKjd60X5vQJYwONyKKOZ9xfY-dvd7Y0r02immii000wGNVEmGuzBB7jtixLbUHve1WlfNCuUTe6503mJXZywRaPV1sZ8hdEzNNfFcQtjRDXqh2aEr5lBneupiw6wQwdnUo8wj2z_UwsY0hEYan9FgFc6_eqjOjMpBlx5NgM1u14xUAFsG0tLZFSgKtlB8K3Bt5MHjucCSI4b2xY_Z6PZ_bYbVpig48pcKwcwExv6M6WqavzLpAJaOkajiFad4mFkb5U6W_P6UDbDapyZijxK0VoZQ8pCSRxIOGH4-Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
رونالدو نیازی نداره واسه GTA 6 صبر کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/102881" target="_blank">📅 16:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102880">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed01098c6d.mp4?token=tt8cM-nSxGyOcvO9OX7gi2rWhimtJj-u0hx5GdPxYZd1rVrzhNxZ4LEyaeXlDcWsP59QrYc73sD6TKQ4qrdfFGYY3qNU8gfYXV7A2TYmEc8PXY68vnW54rI1iAV9yNIhCoP6hrlvC-CaNqaYOnFmwPOqGxXc-p3plewEs-zzl_HajUrE1QOZC0eEFRvraSHS1FMIIyUCvcj0N6jB8pvgWRh67991AcUGiLLuHJ1HLmnBsuku96a94IaOP9-O8TkoIIzu4pSOgm7lb2Lki1R4pUeFqIPjTSJStjOTGlT3gQhO1vJgvHyiRlnYHftqXME4r_7gWfRECgsenw1F5KEREw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed01098c6d.mp4?token=tt8cM-nSxGyOcvO9OX7gi2rWhimtJj-u0hx5GdPxYZd1rVrzhNxZ4LEyaeXlDcWsP59QrYc73sD6TKQ4qrdfFGYY3qNU8gfYXV7A2TYmEc8PXY68vnW54rI1iAV9yNIhCoP6hrlvC-CaNqaYOnFmwPOqGxXc-p3plewEs-zzl_HajUrE1QOZC0eEFRvraSHS1FMIIyUCvcj0N6jB8pvgWRh67991AcUGiLLuHJ1HLmnBsuku96a94IaOP9-O8TkoIIzu4pSOgm7lb2Lki1R4pUeFqIPjTSJStjOTGlT3gQhO1vJgvHyiRlnYHftqXME4r_7gWfRECgsenw1F5KEREw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقصد جدید پادشاه مصر: سوپرلیگ ترکیه.
👑
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/102880" target="_blank">📅 16:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102879">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLZb1tF_PJlhQufpA4aWyMIPb7tQIntS2nPOyJHBpI0IKEaMcMwt0odCvrtqGgJ-HB8R28KkpzOeRifeKhSCGplQ0VKHmfGuFn_6K83edmZ3sgyq1YacCtd4I-9ESdQTIW6AasPNet3w8bcyVLX8aHtCEUQz2hFHiH8n9yVFDmOF3CC73eMt0Ou2aH1kmMAXWO2UWv0XNiil4YvhKtE0WTRVw1VQ2GfJyot3GcMI2_Vh6Z5ADw2VCLIbCSoC_YSF86fSU9X-3ClsSOzkPA22MVLBv5pachnrvK3pmtbspf2g0_yUK84kbMoBSxSzZLpDZn6Hz2Gm0qlUvw51vo8q5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
✍️
✍️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/102879" target="_blank">📅 15:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102878">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXCefucHCx2G14GzW7k6A3a-1q4luUY8iDiaJBg8TmqECijEPDz2iY4wCS99xMfjXl6U--FFTWNpAjeUzL0t84q0OSusDsleKxdtK2ERPJsqZKx1cUweBkeUBhUBK94yqGmXNCid0cuI_nEdjYTLu4EGw1O05EbN1NheXdCNXmf15NzKMZfOw2rXBvpdyirFFuMlIauF5n400bW5lJblkyRgzSmamCIdJxRGsbAU5ITuJ2awx-ItXNRLiCeNdhpBG-JDA24kOZy12X-qjg9-DfR0ZyeJvQotqTpDjsNi0a1CzexVCr8UpHrRdEbVqquOVZQJchZsBPlsGMQ5ljGZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
فوری از کارلوس مونفرت:
هانسی فلیک خودش شخصا زنگ زده به رودری تا مخشو بزنه و به بارسلونا بیارتش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/102878" target="_blank">📅 15:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102877">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/954417f16e.mp4?token=G7piMAXizHcEtB6hcRF1UCZUFTL-WzCWArC5g1tmpCzC8UZZKbDpDv9L1HVsKziIF2chkZ0CLLiPgoi3m5uXYR7nFu3n_aVHJAr8uxMvNBSPUYcdab5VAuKkV35PySfJR_N4TcEQHfy5HLpmVSt0oKM8PpgKXR5jALazpY0W3D5Ce1Imdnb9R3Qjz6EoEkl7TkkPRS0wVGEDeqnf1ncpQcedQ7bTrO8OUukJIMPbaoI26KbRSvZUnirkST_XqjmgCV8wx4k5Y6QVCXQ8ZzQg_82qhv1XWMc3ftwtZOGy6uR-qVKhNFDUaf5TTyOvEZgXgqSHMcCZAfoIx9HyAl_02Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/954417f16e.mp4?token=G7piMAXizHcEtB6hcRF1UCZUFTL-WzCWArC5g1tmpCzC8UZZKbDpDv9L1HVsKziIF2chkZ0CLLiPgoi3m5uXYR7nFu3n_aVHJAr8uxMvNBSPUYcdab5VAuKkV35PySfJR_N4TcEQHfy5HLpmVSt0oKM8PpgKXR5jALazpY0W3D5Ce1Imdnb9R3Qjz6EoEkl7TkkPRS0wVGEDeqnf1ncpQcedQ7bTrO8OUukJIMPbaoI26KbRSvZUnirkST_XqjmgCV8wx4k5Y6QVCXQ8ZzQg_82qhv1XWMc3ftwtZOGy6uR-qVKhNFDUaf5TTyOvEZgXgqSHMcCZAfoIx9HyAl_02Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شادی کوکسال‌بابا از پیوستن صلاح به ترابوزان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/102877" target="_blank">📅 15:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102876">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpVagtYgASYL6nzwudUYKRtQJZjaRBXjwBnl1FlbowtbZDxO-eImQTu6PV_AQORVuiXUGnk0I6DTq5XgpiURBOn_Q_O9bmEQ_lK5S3hU9RrAv5LxAnaw6ZdpnwgGrOFn7ChDJoDvz7n0Xb0ty9sGKtvDspD21Vg6Jyy5BNCi9EwWo1mPMsxIbMPqSQDFaPj5Xh8phWbTRmIAiQ9iQiK2Pq0ztX7-TV2DFEhqQfGYPY9P-5PRv54b1Jph1gwj3SYBxHBes9rRkdKI4-bloZfIe0o-Va39JafgVpRUcYE6GON1Xi_IOqcjTyk0Es8wu0J5lTzV4V3H7ehfTAcIlE46LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧩
فوووووری: با اعلام راک استار گیم پلی GTAVI در تاریخ 27 آگوست (5 شهریور) از نتفلیکس منتشر میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/102876" target="_blank">📅 15:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102875">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6zSInHbmzHfFpwShl1TXmWtWzRBuXkxJfpun-FHsr8D4tZGSSY_NLIJI1GusqqfAuylJWh4npWcs6vnkPraAuXqe8p8AnTw2LVbVMHPQbv163O7RGDmsxEqPAwSRhGNMWT9G7g7e-eFJ8F-EolqbouNitUAVuDnnwpLE_xqOZJk_CNIpaLLlmzO5xy2CzJ_oD87mqgdMfAO4qaKSL-VoTFWpEj_z40DO3rw1n4m-dQwCYKFvW5FkrEukakijgvIpVMeyKrvk_4jherlSs-BdkrebcKckHCmlKSe1jcSzj-vqRG15f7YPGek-8DXXPqg4e5B9NzmblP5UfWdeLKR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسی از یان دیومانده در راه به سمت مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/102875" target="_blank">📅 15:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102874">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8a690689.mp4?token=usEsERZjhbrlZULOkf_cR3dUVd8OdKEYQ13dKpR2sSH0Vbs5bB-3_XX1bx7Wj6idob7jVKetitGZg6nZ9wgBky_diFu_2kTzQkPJA207aTgphH2GjMqkr1YFQRWF9bO40HXRSj1wfrzX2DGCzGjAhoImCvuXpOOXdnXilYP0uOJAxJG6BkXszGs1ItxgMhdRc7fphsokNOkAsWMHrLX3kEn8CQtrM3EGv2pz4jHe7dp2L34QpLsL6vnpbqUtbLicFy7vqPg1ca5QdSr2Rgd0bL7Hgzl4KhGPrIm4S4xJb2qR6tB0uv2LuHFWmcKMNPBZWMQXRr-HYjXPpgL0duV6ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8a690689.mp4?token=usEsERZjhbrlZULOkf_cR3dUVd8OdKEYQ13dKpR2sSH0Vbs5bB-3_XX1bx7Wj6idob7jVKetitGZg6nZ9wgBky_diFu_2kTzQkPJA207aTgphH2GjMqkr1YFQRWF9bO40HXRSj1wfrzX2DGCzGjAhoImCvuXpOOXdnXilYP0uOJAxJG6BkXszGs1ItxgMhdRc7fphsokNOkAsWMHrLX3kEn8CQtrM3EGv2pz4jHe7dp2L34QpLsL6vnpbqUtbLicFy7vqPg1ca5QdSr2Rgd0bL7Hgzl4KhGPrIm4S4xJb2qR6tB0uv2LuHFWmcKMNPBZWMQXRr-HYjXPpgL0duV6ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎂
🇳🇱
رابین فن‌پرسی امروز ۴۳ ساله شد.
وین رونی چند وقت پیش اعلام کرد که این گل فن‌پرسی، بهترین گل تاریخ لیگ برتر انگلیسه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/102874" target="_blank">📅 15:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102873">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d6d765b6.mp4?token=IRDlFkwQXs7-aRSfoOzqZkPRr5ce5m4eVaKslCKWM2-P35avha2e40aMC9_SpZFS9z190btQ2O7uNGxK3f5ZACQ2AxcMWMod4qQMgP600xQ6VkbdQi3co4bNLcBATW-V_Za14QRT6Pz8MrywmGUqat54xIWvq_HeWkFT4CjxFt3nyK8y021zCZahV_OIQIAccvE3Uaxk5dr-9X9TaquHRBS3fvjwwPKkPenCJ5sfEmGo60ELtvhb38Izp781NEpP-vZ2RphnqZc2JtnLR2RKXUxIHJ4PBJncxdmd3Eok0XjtL5Q1bho0lgF5ux0WC90UFSIS5cIgh2KXQJq4gUwoCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d6d765b6.mp4?token=IRDlFkwQXs7-aRSfoOzqZkPRr5ce5m4eVaKslCKWM2-P35avha2e40aMC9_SpZFS9z190btQ2O7uNGxK3f5ZACQ2AxcMWMod4qQMgP600xQ6VkbdQi3co4bNLcBATW-V_Za14QRT6Pz8MrywmGUqat54xIWvq_HeWkFT4CjxFt3nyK8y021zCZahV_OIQIAccvE3Uaxk5dr-9X9TaquHRBS3fvjwwPKkPenCJ5sfEmGo60ELtvhb38Izp781NEpP-vZ2RphnqZc2JtnLR2RKXUxIHJ4PBJncxdmd3Eok0XjtL5Q1bho0lgF5ux0WC90UFSIS5cIgh2KXQJq4gUwoCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادی ترین کاری که پسرا تو کرج و اسلامشهر واسه جلب توجه میکنن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/102873" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102872">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd9e41e0be.mp4?token=uh8lvK3SrQYRF75MZhgobpffpMfYLTRHXk8FBkw5HVCT6Ikp9Oz_8q4DhLwUT1TDidA7DPYalQS0l-m_9A0seoFS5KdRuSzF8r048XTTNSgod2-_kZccYkrq8cLV64QOrXRHMMW0jZu2bhkLpg6RQKpCu0kYLdi3FA7OSsSpIOFiESIRs-kxjnvOvA-0b7QcA6b61sDCL-pb8y18jDasuCO38nXb7UcCUdcjxxQt_7Md7bzUPdB-sLXNSrtm-Xla7bWFWfR_Hmlu-308kKMjiWxgrAAmGKu32jnCAnRwWAq2kwwb9mGCNG9_ySRIZWheMrSlnPsZgnpLYQJcIYGhIxFPMNebiHYd1tvvH0KRrxnaqzkuW2ZDDX7EC6zoQzx848NMD0EVp03JbPdGYSM1ygc2QzK-UkUzUxJYpX3fit5mM-gS_9UvqyRFkqVOYz7xmhTrbppuRjT9Bq3ep9xF_CWwvrXY6ncc_dlCQJVgK3NSt_MTZEjuK82JeYw-7CcuvapSEUcrV-CRVAm-drf6fkEH1pu_eI9_K0alumcPmc80BZUov0AMy7thhOgYDQGKKieRtjxMb8azpE8qeP2N-XnK2FiYn-CHECEgpnLHS_keZLCAlXQzkGlOAHiq4d8utVy1CzePbcFeNSDi1worituBPEXPAsIyP1ylUAH7rWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd9e41e0be.mp4?token=uh8lvK3SrQYRF75MZhgobpffpMfYLTRHXk8FBkw5HVCT6Ikp9Oz_8q4DhLwUT1TDidA7DPYalQS0l-m_9A0seoFS5KdRuSzF8r048XTTNSgod2-_kZccYkrq8cLV64QOrXRHMMW0jZu2bhkLpg6RQKpCu0kYLdi3FA7OSsSpIOFiESIRs-kxjnvOvA-0b7QcA6b61sDCL-pb8y18jDasuCO38nXb7UcCUdcjxxQt_7Md7bzUPdB-sLXNSrtm-Xla7bWFWfR_Hmlu-308kKMjiWxgrAAmGKu32jnCAnRwWAq2kwwb9mGCNG9_ySRIZWheMrSlnPsZgnpLYQJcIYGhIxFPMNebiHYd1tvvH0KRrxnaqzkuW2ZDDX7EC6zoQzx848NMD0EVp03JbPdGYSM1ygc2QzK-UkUzUxJYpX3fit5mM-gS_9UvqyRFkqVOYz7xmhTrbppuRjT9Bq3ep9xF_CWwvrXY6ncc_dlCQJVgK3NSt_MTZEjuK82JeYw-7CcuvapSEUcrV-CRVAm-drf6fkEH1pu_eI9_K0alumcPmc80BZUov0AMy7thhOgYDQGKKieRtjxMb8azpE8qeP2N-XnK2FiYn-CHECEgpnLHS_keZLCAlXQzkGlOAHiq4d8utVy1CzePbcFeNSDi1worituBPEXPAsIyP1ylUAH7rWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❗️
ماریو بالوتلی از عجیب‌ترین بازیکنان دهه‌اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/102872" target="_blank">📅 15:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102871">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCxGBfgwBgrz4QNU91jdGB6A0AQkN8Fv0c4XgbM3KabVOq6IGEdSCmdft07zylIbXUzpn4HXptCe3Ao9QUe1lB8hQDtYNNFEWPKu-DY3D5zoxMc1ClSMo5OsTMS7nxRv7DBrOIQdJEnqV5lexVsqzvzhpjqg4DZyj4nREJCQeGXKA5nVg8B3WbilonPYyEN94Ow0n-HiYK_jHakqzMrRPtvWsBXfSUUc5nTR_qgiiSpHdanMs262j-k7er07f88Ww3ZbojxcI8VW5aDOFJ0IGI-x-Vh3NeEZRi7MWIr5z0xQ0DP8mZDzYRo06TCF5gUVA3msSSoWad2b4eV-bsWY2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش رسانه‌ها، "کیم جونگ اون" رهبرِ کره شمالی به مردم کشورش گفته که تیم ملی‌شون برای هفتاد و پنجمین سال پیاپی قهرمان جام جهانی شده و اینو به ملتش تبریک گفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/102871" target="_blank">📅 15:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102870">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGo_-uSdhnp6SYnoFPd2Or7y2OpCQv4SU1Eha6Us948LuskK8WhideZzkNDtwwU6OoL-RjRxMMCjcn_j5ZIVSHn6VrxibzwYmBWiNQw_0k6nd3PR76w1Q5JUa3HRG91_ZTH0fzAxlv6XIm77-njr5cJgjaFcFe14OztHDzsrNAK-wShWgjXkvRLJi1YlDRJha4FDsbPoHoSpl9e76C32WckREhD5DNyLjI9vj79P4QJrwS7m_ixg-FsiwIkUCgesSM40mMSbvK5G6pQjnTwu46jVa4Y9rFZzUGQulGnIorA27gWZG0ZLKistMECfWp9TyvBP74hJGShcNfvqMyQg8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گاوی صورتی تو تمرینات بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/102870" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102868">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e46l0KcE9cj_fllvklatpDC7xBJ5FzqU79W-JgZrTYtJR88VRY-mU1Zd0zlyMD-2MVjSScQ7x_-HJh1JpPhEypwnV57Dh6kxRwBOUdt9ci0pFy5t_wJ1SGUZNHxaT97PQzkmkQgfSCiJHybFdDDTMzJH1r6J_YWG5ArS086Z_5rE-D9MVyb70BF6s5e0a0h80ydmE6TaJLC8Jh9tvf8wDduQDeE8SOHRXpGlp14QTEGZUMLj5Ve_ZvIKgF1lgVC2t_ieDsllEIbDjaRwM46Wgqbrl273erhgGpK-C2joV1UxAzp_5G5ns9IYf8fGNLsBF7FnPDnGRFD6zrFvPuYENg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IIMRzTd_RL7FhOraGcne3FYcmZcnfzpF7KB_oU1ydIMTzPafSsRKLFNKru9IG0NSTErWIgwcyw2UL9G72QapyTSHRUKeoo9kehY8J17A1-TCjBjnWd_fNhU07f52Ra0m7IClOu-6kZWg-Hm6uwSknl8BV5WSGRZtlmwCLtQJ6weNKgMyjTeXk1L1FYjFtTYRlj4sACWNtMUf3g_sv7RaxCep5QkiDtrmUEbGjhWL_tjbaIcwoxxoTXJZo33itiOZniI3aBoJK42CsCtRq7_oFlKrCrNTdXXiIkSw4SLJp6BoH6uChz2qgH98dG96AehpqoC0OV5EfcNIclv_7rfZKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جیمی کرگر معتقده محمد صلاح برای بازی در فوتبال ترکیه زیادی خوبه و میتونست به تیمی معتبرتر از ترابزون‌اسپور بره.
🎙
به نظرم اون میتونست توی سری‌آ بازی کنه. از نظر من، لیگ ترکیه یه سطح پایین‌تر از اون حدیه که صلاح باید توش بازی کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/102868" target="_blank">📅 14:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102867">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f430a769.mp4?token=kM2lFmlW42kv3AtJzFAQVxQdH-U_Kv7rlD0tdKp88Zpx9_uTcFKofYwzODWkruEIm34LMzHVGjg70-Rjxpa1l8kMNQduMRpj9BAK9khf8zEaz58_8R5qYKXheqFrRjoDiYbhC6UWs00ZAI98PPtwsbNhOBE31IkcOSqwqMG6Ghh3BUKUnTsOk3J2uOaI26e60MNlb5bD828iySOTlfmNhQSlkf2O-jOfWHywLoFKiiAqGabSG3Vnhc2PIOwUIWyQb97uciU-__hYaWng_DhK9r7_GI0awzXcK03VVgjx4m6ckTkfL03IrE2fiOz-Wc_HwpKhV8gKLb9QJxdbR_TQKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f430a769.mp4?token=kM2lFmlW42kv3AtJzFAQVxQdH-U_Kv7rlD0tdKp88Zpx9_uTcFKofYwzODWkruEIm34LMzHVGjg70-Rjxpa1l8kMNQduMRpj9BAK9khf8zEaz58_8R5qYKXheqFrRjoDiYbhC6UWs00ZAI98PPtwsbNhOBE31IkcOSqwqMG6Ghh3BUKUnTsOk3J2uOaI26e60MNlb5bD828iySOTlfmNhQSlkf2O-jOfWHywLoFKiiAqGabSG3Vnhc2PIOwUIWyQb97uciU-__hYaWng_DhK9r7_GI0awzXcK03VVgjx4m6ckTkfL03IrE2fiOz-Wc_HwpKhV8gKLb9QJxdbR_TQKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحنه آهسته از مسابقات جهانی سیلی
😐
😬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/102867" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102866">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8cd6fd12d.mp4?token=qBe8vgfvDFjgLec5WFJgETLdt6QcmVPvEkm5rf4ectyjM2MtfGUzfUMWogiUbaBrOp7byswryw5vI9HQJ-Dmdfjs0JxddaKoi1JVuvuR2STv_C__9mGhWlK7PMD_e8kLD3Ph1Pgj7-yaFiyuJ4dpqoKXM21bFrPlMsFW_dnEVgh3325d1-ZrSREM76U5OzrtNCP1_FyOJ6-Y6fDgZv5oTPQYsvQtPeXYLmFPHXNoqEEALDDFdSsfr1Y_TXFUTW2KOMpCyjx-LrKbwREog00yUyQdHriDuOmZZ4D9_umvz99VEycM0XWMWTWxLM6wG-sfPfFPc7DhIui6yED3YKgbipUQJN6l_kO8pIQEkvS8YBv5_gzyqdFRWuBZ8gCVrp00dCpsS8bWM5MU6BydD_SHHkNuCTZsEI9UqHd4L_6xiYR-cb-ub4zXh8VHieqfsK2_qGFWHfqZ1ffAfFcDBuBu8UDG8YpXnQkV9J7fEg24yhFYo8zDKWHRCwdD8CIT9ryT8UXtZFVGW3oKznbWptZZRGhIsneVJ5-kxMIIwcjxAIjKAUIUPuunT9ViPytetGhYb3W-lzL23mZQbPyz7wTcfoFEj_qu4p7a2RR9kbSTjo3Ao5n0YiiVIrnMrS-AUo3FD4SrqsxBoEohim-SRZJfmU_0YhGADlpopvb2RbO-XE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8cd6fd12d.mp4?token=qBe8vgfvDFjgLec5WFJgETLdt6QcmVPvEkm5rf4ectyjM2MtfGUzfUMWogiUbaBrOp7byswryw5vI9HQJ-Dmdfjs0JxddaKoi1JVuvuR2STv_C__9mGhWlK7PMD_e8kLD3Ph1Pgj7-yaFiyuJ4dpqoKXM21bFrPlMsFW_dnEVgh3325d1-ZrSREM76U5OzrtNCP1_FyOJ6-Y6fDgZv5oTPQYsvQtPeXYLmFPHXNoqEEALDDFdSsfr1Y_TXFUTW2KOMpCyjx-LrKbwREog00yUyQdHriDuOmZZ4D9_umvz99VEycM0XWMWTWxLM6wG-sfPfFPc7DhIui6yED3YKgbipUQJN6l_kO8pIQEkvS8YBv5_gzyqdFRWuBZ8gCVrp00dCpsS8bWM5MU6BydD_SHHkNuCTZsEI9UqHd4L_6xiYR-cb-ub4zXh8VHieqfsK2_qGFWHfqZ1ffAfFcDBuBu8UDG8YpXnQkV9J7fEg24yhFYo8zDKWHRCwdD8CIT9ryT8UXtZFVGW3oKznbWptZZRGhIsneVJ5-kxMIIwcjxAIjKAUIUPuunT9ViPytetGhYb3W-lzL23mZQbPyz7wTcfoFEj_qu4p7a2RR9kbSTjo3Ao5n0YiiVIrnMrS-AUo3FD4SrqsxBoEohim-SRZJfmU_0YhGADlpopvb2RbO-XE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یادی‌کنیم از درخشش تاریخی لیونل‌مسی مقابل منچستریونایتد در لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/102866" target="_blank">📅 14:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102865">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇫🇷
👀
برخی از موقعیت‌سازی‌های لیونل‌مسی در psg
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102865" target="_blank">📅 14:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102864">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UT35HWXvbRqIapvxUPKtKJAR6o21JWdEUy0ZIYG_dgG9s7PFKfEyXCN7rl28hDvCmTOJstndo235ZF794_2teUqVJWyHPE_-LdCSNB8n0xyQT7zne3xuy3fy37849_vXcRnf56Cnf7sH5273M6IJMrvqRX1NIz8FJf1BqK8mrBPgICvJp2u4F8kCTXDu_gNX9xVt_zh1_uWQcZZuNQ5MspvCjblMR7sjIjI6LevigcWwnM3sKh0d_YtqIa44Bex6b6x8fvqCncsFlTx-1pFjYEiOjOJdE4v-YwkxjjkmTQxY166wfLjQA-UzBdI42aK6EVK69ScYE1z0_zCUsccGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
بهترین گلزنان تاریخ فوتبال اروپا:
🇦🇷
لیونل‌مسی: 496 گل
🥇
🇵🇹
رونالدو : 495 گل
🥈
🇵🇱
لواندوفسکی: 395 گل
🥉
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/102864" target="_blank">📅 13:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102863">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3mvSleTPAt_CJW7UHxVNBatePKHF2VrMGEXNpoFH8oO2KDpEMh6q1ZYA-oe3UC8oieCMEhiKnSxNmENUn4L6Cfd1PjChsawRhNjVfLFcp6M4CUgpoVdbmrvaX9Bg0Hcf0OEcFSdjZ8iiHPzkRkOJc92co1DhA68T7tESoboqSNLduogflbrsEEo67QW7cHU_1nqb8Gyozkq7X7WcINxXU6ADxc4W7rjd-DJ54GDtzyGYWX3Y_HxKA1EpOQVOI0wY1YUJUiX3DLdzZ9OkFyd7AaxOX4Wt14ZYiauKxjwGiWyYbD55C2CZyrKcD4-OrsSlJRp3IRT7cR8vguGcRLSqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
🔵
خوزه فلیکس دیاز: رودری قطعا بازیکن رئال مادرید خواهد شد اما سران منچسترسیتی قصد بازار گرمی دارند و میخوان این‌بازیکن رو با رقم بالاتری به رئال مادرید بدهد. رودری بارها اعلام کرده جز باشگاه رئال مادرید برای هیچ باشگاهی بازی نخواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102863" target="_blank">📅 13:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102862">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSAaLwybEUyXehy1cxYvHyJmN0dHgYtyubnPxTgbjuaOmKdPzGBvv7sPArWjawl1K_-9q3z81CEP8ZLEQ1KVax5ezwB_RdpMnB7BZFKSIfZrXdZpid-D61S-dW9bc97f8TbcANY79pzRuUYL9rP7D07CFlTF2865eSiVepdOIyqk4ll6EK59xgtr54mlGV4nNiHzI78w_I8VEEnX_7r1sSdSWSBDw916si17YDgM36Vd_2V_xicnTo4TQltGaqLj96CRoVxgvsV_GUxFjHtiQlpTE6dZyemO52SDI02bxBviVfmBDUSnOKZ8pwDSzao5TFcv3KSnwnbs8XTnWNiZpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رومانو:
یان دیومانده بعد ازظهر امروز به مادرید سفر میکنه، بیانیه رسمی بزودی منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/102862" target="_blank">📅 13:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102861">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🔵
فووووری از فرناندو پولو: خبرهایی منتشر شد مبنی بر اینکه توافقی بین بارسلونا و رودری وجود دارد. ما با باشگاه تماس گرفتیم و آنها این خبر را به طور کامل تکذیب کردند و گفتند که این خبرها نادرست هستند. اگر رودری خودش مصمم به انتخاب بارسلونا نباشد، نمیتوان در…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102861" target="_blank">📅 13:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102860">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb94d33db.mp4?token=iTMa12vdL72C0y6hCeBweJP5PaIbE3iLw6sMBS9_4EeNoBwyTydaDEVHnmgAG0OoGxWjpQy3w5sF2eOzXOKypcz2h7KfjantFwujclUjYeiF7mxqc7QkeHH9tVefdPci-WcGoejQ1iXikPHKQsjLm286GumTYdbyglqaQLc_u248XlgnFBTu3h7Q6AwtHy6MuRaLdJgLXSKOrb6ctekgMvckVaCb6V8R3es1fKruT2q8jv1murpyS6MUtskAvhJZQd5P5GXdLb6XOhy9c6oAXBbKNLht3-RMN2zr6DQ51CADUOdYx3QQrNTT10or659ixIJ0AVJ0nFn7og6umT4cLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb94d33db.mp4?token=iTMa12vdL72C0y6hCeBweJP5PaIbE3iLw6sMBS9_4EeNoBwyTydaDEVHnmgAG0OoGxWjpQy3w5sF2eOzXOKypcz2h7KfjantFwujclUjYeiF7mxqc7QkeHH9tVefdPci-WcGoejQ1iXikPHKQsjLm286GumTYdbyglqaQLc_u248XlgnFBTu3h7Q6AwtHy6MuRaLdJgLXSKOrb6ctekgMvckVaCb6V8R3es1fKruT2q8jv1murpyS6MUtskAvhJZQd5P5GXdLb6XOhy9c6oAXBbKNLht3-RMN2zr6DQ51CADUOdYx3QQrNTT10or659ixIJ0AVJ0nFn7og6umT4cLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤕
⚽️
بنظر استون‌ویلا با خرید گارناچو حسابی پولشو به
کص
خر زده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/102860" target="_blank">📅 13:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102859">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری از بن جیکوبز: پیشنهاد رسمی بارسلونا به زودی ارسال میشه. رودری از جو رختکن بارسلونا خیلی خوشش میاد و مشتاقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/102859" target="_blank">📅 13:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102858">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXmh_TuM_nuVhSr947SUFq4T5I0pbOB8BTtKGxQqWRHwMhzK8Cyi2hPqozyYi0Ej-hvIVQhUZNH2xz3qY7QoggGseoZxU781AZpHgAdYGeDWIsjIywnGdFFmAQtDc1xieigwk6fJS1vCqVls9J9F3JE6KMRC_3uwSsYaEbYWt2jWAMD1YNpo3AkCOYdNvgWocUYw99ELdNbEDRqZi5oIILyiPPwquQTSkWw7EDADwgbiTMUaHBX9Wli4ICtUuN5GigD_EFmt4j3WbzANsW1lXVUQK6kVuBUx3G3K5YHFj2F6MqP4IKAVSeKgcYGLsoW9kBVDiGpl2VkN7YJqnTlzpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
فوریه 2024:
⁉️
جایگزین برای بوسکتس؟
🎙
دکو مدیر ورزشی بارسلونا:
🇪🇸
•
💬
تقریباً غیرممکن است. کسی مانند او در بازار وجود ندارد، و اگر وجود داشته باشد، باشگاهش او را نخواهد فروخت. تنها بازیکنی که کمی شبیه او است، رودری است، و باشگاهش او را نه به ما و نه به هیچ تیم دیگری خواهد فروخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102858" target="_blank">📅 12:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102857">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmdTvpIbhTLWUtkBPDAqO_1XS9g6nSqc2BrdxdhlaNqJQe8zJDYt81lxAfRYfNQOpB80Xm0R2mdvKF5lWqOJ6WO6v_vduCYJ6ooQTzUwilMfK5aPP_NMqNrWo3BxHIBGw-5UEIGY360zQSO4gk1bLzmcHvA6N14cUgBf4xXvdfM3nU3ap5jMQ6hCpCdZ4x9QjYVzOx20nI0Qs__naTycpZYVldqXKQsxtfaOzuaFX156mOZWDd2C9MJSs9f47wAyF37Lc8qZ5s5pBXgr02mX_3RdBRRChUsfgxOOIGro5pSwCTEW7s2APv6ZvXiaZ289RVAr7pltnildJYWxzzKBpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
#فوووووری
کوپه: بارسلونا پیشنهاد ۶۰ میلیون یورویی برای رودری ارائه کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102857" target="_blank">📅 12:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102855">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cIvkU8fHnXTrKvPp9XiPR8sw2B7IUrPtj3x0iqe4oADrKgs5veMeA7uJhgitOM02ceQPn9k7C-hSmAmIkDuF6AECHTlrwmFUkmAezBw9M7Fkm2O6crijwbMYjHjxmUtxejtDYh1QMQXpGSy9hhr3JQSr9gSpvn7Yhhe_rW5git3er1gFbAwRnr-jg68nr07kGRn70y2N4V354qm3Ove7ChuAfaEAw_uJFGitvMN0zhlsvzExv7ItVMo9u0THwtxcbmI_0IEHYRth-M1fWOeidGREBS-SJTERZNANTI9WIidiftWfK36b4j4yVemuGx4YRFH6x3xcU5oPr_IeCDmuoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZtRKDRabVeSIO1mqchnO6PGFm9XEB1w6jCuIfaSWoOuybADloWMynaplqFuc23PQmYD-NAGgZEkpXqpfiq_OIG0EziKZfd9wGu254t1QSolsocBu3u-KWHvp_WfYYHIRbn_J9OvWwDSdRZU83z359yPTX-BYn4-82W7D3gSQOgMIP629Hxrb5_565T6qVr1yvCzJgTm7YKVGk6QFftkZdxSctDWqNTp-TEXAePDCIE3006F-AkOK0AzOrjEePYIipvBUNNws5oUwZkUR5kYz3RQx6wmMBzzmBNbeK6czu5LSJ9NuvkugcJQagbImG_TWLE8SOsF2Oq1OatSztaeY4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⁉️
می‌دونستید؟
کریستیانو رونالدو اون‌قدر درآمد داره که می‌تونه کل کلکسیون ماشین‌های خودش رو 6 بار دیگه بخره! ارزش مجموعه ماشین‌های رونالدو حدود 50 میلیون دلاره و با داشتن بیش از 40 خودرو، یکی از خاص‌ترین و لوکس‌ترین کلکسیون‌های ماشین دنیا رو داره. گفته میشه درآمد سالانه‌اش حدود 300 میلیون دلاره؛ یعنی به‌راحتی میتونه کل گاراژ ماشین‌هاش رو با درآمد یکسالش 6 بار دیگه بخره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102855" target="_blank">📅 12:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102854">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVkqbHacfhk4hmYT1Obw_KL0pcLk7MhikqqeXYkr15VyCerZ28w27ZwPndZX9GDMvLfsQVXsP_dnVbWUZx-R4iIQXsMQvbukybv5zmtKH8oRuA5Ez4SQLJC9zPW99fgjzP1tIpeUyQOStUBiEBGW0kb3gr4zbrhFKe200nGV99Y8MjtWQJPN9u6OnxPd72Hj82Ue9S_rISIFv5euOTXzzuVVEMjlsm8T8tNGnIpxQFGW1Ph3CKrLehFfj5kyWwIdjdNjw7E3rZsalkhqRF1OxTSvHsqFGPXhB8rBukzXvlDB5-SPRnh2gTE5P4J3TSF3trw2TE8zLgqDv1XnGyPc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از بن جیکوبز: پیشنهاد رسمی بارسلونا به زودی ارسال میشه. رودری از جو رختکن بارسلونا خیلی خوشش میاد و مشتاقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/102854" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102853">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMbFvR_1EIhTMBX6WYW5ICr4upoJlu8NVSx-wLfYF6_Wh7WRuXwqK0goda-2ezHrNN0sApGgLbPQy4kIPJfJqDXq1cnVRg6QJo6sJiwz1k_UW5EBtH-tmi4J_KkoMI2RadllGacucmc4BUbU2psVa3r-oi0kq1_vXg674KpuNMf3qeKbFX6ScamUzFCfofBWltasbkm69Xww_K1DWVl5an2d0SWRtHh95HlLCC_2eyf0tNda18GOgAsxi4w-b4zWNaH_DBbNlvvJamRlJ9nxglmO0UboOphv8gh0CP4ariisTkg5OZNF06koAx9lkp8r1Y2zEOmJUSuGz9CZwabRbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از رسانه مطرح ESPN: رئال‌مادرید کاملا از جذب رودری ناامید شده و از این معامله کناره‌گیری کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102853" target="_blank">📅 12:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102852">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBmtH9muL7fbv1rk23ZMsNbLdvhlIjmYIucha36vOCrqnzEZW01zCsVAY10TE2_SAup48fFnuSEmk6B6yk4dc5eDkHu_MuxaXpjv-stDXGMkYHPzo2_lKgtjuWDUHfnNpwKnUcXvSieviItRrQwCXinE7GkEdhz93lptP-B_cxhhXq7iHkrziDvdmN-4iekpdDuJrQe80gPaHeQ09k9ns0WSEi_ohsZxny9Ys0TGm97YiAmZaIw79Yeh4lQNhcVCFgU7mlrW0cUBxR8FQ9GxZuoO1JLv4SHroYyvuR0LQ6pJno_55k4pTT4KYas0wvevHn67nbPRmTfQSWy4-uEycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
گزارش روزنامه COPE از پشت پرده نقل‌وانتقالات تابستانی رئال‌مادرید:
🔻
فروش آسنسیو برای جذب یک‌مدافع
🔻
فروش کاماوینگا برای جذب یک‌هافبک
❌
هر دو این بازیکنان از فروش خود خودداری کردند و خواهان ادامه حضور در رئال‌مادرید شدند تا پروژه تقویت تیم فعلا تا این لحظه به بن‌بست برسد و رودری در آستانه منتفی شدن باشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102852" target="_blank">📅 12:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102851">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwRfLZIJkz3oXeMvIz7QO87pROGPIM_rz2RhfKz0mC_APPq-X6OoQo7KHZy9dUn44LSzQrT9dTaa28QMxm_vQRbw78M1E8wF_OeqPeWthQKJKsVNcviYJOKD1VgCIwF2oGdtO8OXaukp6FYTnUd_q-Da5i4AoUpFK1BeI0rm9yxzk2L-lZgJ7PjMJflu4jKsUoal28CpDLUJtO6eTXY39PMfraDf6u1SQDSwZcCATxdNfKEG_jue5I0xBCm6jQJiCNXOpW3NOUHN91yYAziVgkNHvStFoFDtCyJjzP26v79BpXxGd62Zyss3P5J96KaJaHo_k4_gJa7yu58luvVfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ شایعات دقایق‌اخیر مربوط به رودری ستاره منچسترسیتی:
🔺
رامون‌آلوارز خبرنگار نزدیک به رئال: بارسا در جذب رودری پیشتاز شده
🔺
فابریزیو رومانو: بارسلونا با سیتی و رودری تماس گرفته تا شرایط انتقال رو بررسی کنند
🔺
خورخه‌پیکون: بارسلونا حقوق بسیار بهتری از رئال‌مادرید به رودری پرداخت خواهد کرد
🔺
روزنامه‌آاس: نقل‌وانتقالات رئال‌مادرید پس از جذب دیومانده به پایان خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102851" target="_blank">📅 12:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102850">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
رومانو:
باشگاه بارسلونا با  ایجنت‌رودری و همچنین منچسترسیتی در مورد انتقال احتمالی رودری تماس گرفته است.
رئال مادرید هفته‌ها با منچسترسیتی مذاکره کرده بود، اما منچسترسیتی با این موضوع موافقت نکرد زیرا احساس می‌کرد که باشگاه‌های بیشتری به رقابت می‌پیوندند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102850" target="_blank">📅 11:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102849">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc6547082d.mp4?token=KgC0rKn44bGP0EPf2n8IIbvsmzMFudLz5AaMuJO6S2N6DdB6WQNTBAmfhYpbYoGkI3t9xzPJyrrXiTAfRjWg5tJM24kyFDgtZbEQ4TlH7EqFFT5Eosmg6eDKCm4ojlRzrwJdVN409fY8iJHGgPlpzqcRG0UJuHdp9ArAQmkg-_FvYpp5oTaQpksL422Yen5CylHJAKaSGCXUe4qgqpvbV4M4BNDTkG9p73hLUUPLWGRdHIPZ-nh6oZmAVX0jm7gtgpnIuXDICsegU-eQIQQ2ZjMtggVSJ0fWtBjiD1E9KK_zTomHP993Eoj18Zi9KxfUI0-tZNf-spKGeDNXzN9IiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc6547082d.mp4?token=KgC0rKn44bGP0EPf2n8IIbvsmzMFudLz5AaMuJO6S2N6DdB6WQNTBAmfhYpbYoGkI3t9xzPJyrrXiTAfRjWg5tJM24kyFDgtZbEQ4TlH7EqFFT5Eosmg6eDKCm4ojlRzrwJdVN409fY8iJHGgPlpzqcRG0UJuHdp9ArAQmkg-_FvYpp5oTaQpksL422Yen5CylHJAKaSGCXUe4qgqpvbV4M4BNDTkG9p73hLUUPLWGRdHIPZ-nh6oZmAVX0jm7gtgpnIuXDICsegU-eQIQQ2ZjMtggVSJ0fWtBjiD1E9KK_zTomHP993Eoj18Zi9KxfUI0-tZNf-spKGeDNXzN9IiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
تمرینات نفس‌گیر ووزینیا برای فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102849" target="_blank">📅 11:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102848">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P94pdzz3CbGzrwfsLbkVMcNioKSM3YpTpOCjdfCK6hyb7ThI03ViwchTG3-ui2JcNrJOB2_Xa24mSOCwekQrrwFR6cV_xL88cnaATZs6cOQvnNyQezDGgPIFxaIKz7N10dIekHEeH5vIPDpeYZBzFpS6R1P2jAyPdkDDlbrjQRmKmwf7C0TaB3Dqnsv7c-8xgFNc1f_rlDRAqcQapSc_ZFqJiz27kqmfpgtUWUAN9-BjPuNmrZ8G538tLeyPDxBhpwx1WkjFOZv4yezP2k3kC_CLhTooSnhuogpKOX0ErwLgQ1heC34N3NbJfY4r1VWigalc5lR_COWr_jFCX3GzIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
جام‌های فوتبال دنیا بر اساس رتبه و اعتبار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102848" target="_blank">📅 11:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102847">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇹🇷
⚽️
مذاکرات فشرده بین باشگاه میلان و گالاتاسرای بر سر انتقال رافائل لیائو به سوپرلیگ ترکیه درحال انجام است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102847" target="_blank">📅 11:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102846">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AfST7p-HsAI8Me7wIctfa-q2q1xpb5E8Bu4-9J0QTZqneEy9yBfr0PQfCB_fpwdKzENlZiH5AYUI7C7_e-hYv7i3Jt9vKjPKey9MuslFs6TJPB8V5QXiy1iB9DurAbdHM3wuy8OAiNieKbBaqG1CeoBTeGbRFoDlE4mZ9V9pa1I1fBdgo0Ppto6tUQ4qfqnz8Oi8fzsbZrDbX71DD2-NtuZWnl8yo_wOva2tzZoVT_eU0wNQOQtw8zpfD2uaGnLLq8Xa5R8faNTJNo1uBdoEV3TQ_VKAKJyJk0QI0Vy9TjBRUs2a0Vj6LdIovd8_ve_yTNTagju3zHb930xfDuAqIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
❌
روزنامه‌اسپورت: مذاکرات باشگاه رئال‌مادرید با رودری در آستانه شکست قرار داره. اختلافات بر سر دستمزد و مدت قرارداد همچنان پابرجاست و تا این لحظه هیچ توافقی صورت نگرفته و طرفین از خواسته‌های خودشون کوتاه نمیان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102846" target="_blank">📅 11:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102845">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT7EpETOVcSlkVlrmY65c11-pEld7VN6ijnj-tFfrApCu89NwgTL37u3XzkOfTrbDfXHSj1s6PfL3PiVD1aD2E-7dvPriHbrba8WCHtNAJ9wJNl64yAhwcakQbns0oZhJ0QA2ZHziviQnosSxi_HBM-iipWPi_YRR4CoGogwRVXKF2s12FUw8T-wcwYcsRGKd9jzstn3oKE30XR96upvNrJrXo6GdbT1km7dfZTS5LXOntbKgTX-vaflaPUvuGxK0xOsYEPqdYq1RMauBAEO0TaAYCwlq1D_rt0Og6oWaUBdWCwX58Y3FrW3nJRLeAiG81PQNBAG0PCrGCHRadqgfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به مناسبت آغاز لیگ‌های اروپایی؛ مروری بر پرافتخارترین تیم‌های پنج کشور برتر مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102845" target="_blank">📅 11:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102844">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5d8ba0a4.mp4?token=Mrf9SNJ4jhcqZ3ZUi-g3dFhctGrumBXZF2-FhRzmnbutorNbfs9bNewyuuIoU6azT9_TD-hvVjKFjgoMKnRgXtflng0N2SDHiufL_zYhZgqdUxDdaX-SvfO0e3nWHH7r_aSlRHZ-2JjYFH0fMC2sQAOuJpvIJzZxmPd65z_g6hZHKO7YkTxUHcgRBV72mLhs6wnN7oIAidxtpgB0XnhSoox5dmpdVtKueqYZMChQ3J2O4rAU0wJiBOsRd3FjbxsWJgBRt3zXXckJiW09yr9RLlctg5GXLFHoYGINweoh0KSqHc2YnfDQfRfpsLzD9jKM9zL_5ZBlwZ_y_8KGPrvthYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5d8ba0a4.mp4?token=Mrf9SNJ4jhcqZ3ZUi-g3dFhctGrumBXZF2-FhRzmnbutorNbfs9bNewyuuIoU6azT9_TD-hvVjKFjgoMKnRgXtflng0N2SDHiufL_zYhZgqdUxDdaX-SvfO0e3nWHH7r_aSlRHZ-2JjYFH0fMC2sQAOuJpvIJzZxmPd65z_g6hZHKO7YkTxUHcgRBV72mLhs6wnN7oIAidxtpgB0XnhSoox5dmpdVtKueqYZMChQ3J2O4rAU0wJiBOsRd3FjbxsWJgBRt3zXXckJiW09yr9RLlctg5GXLFHoYGINweoh0KSqHc2YnfDQfRfpsLzD9jKM9zL_5ZBlwZ_y_8KGPrvthYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این مصاحبه در تاریخ ایران رو دستش نمیاد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102844" target="_blank">📅 11:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102843">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKXFGXr0vRO_c6vk0WQjCHxm_0hX37wZaKr4AysCuodz1-azRggrQNISUmrik8ZhYhXIYbSzRYrGOQ8thpOG7D15iN5yBcCJo5FQ0ktqih3lPuY4g_aS451HuNk_91xQYMEji3gRV8BvcuiOSnCPgeaKL_dzF4xaocsRfLvqHgd9DV3N6w1saFNq7CG-heY-TaxlkehIt0sKouNBDEILxrOERBZQOdpa7WAawi8uNXk3DAittMCDUA1JRc83UoWac0Fy-4mUXh7h1df6Ryn2Vr7_LXQ8CB5LTlcffZKlMoGD2uQrfJhylfLETpB5StiR-Gz3czNADI2Ly6XTiq_o8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
👤
#غیررسمی
؛ قرارداد وینیسیوس جونیور با رئال‌مادرید تا سال 2031 تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102843" target="_blank">📅 10:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102842">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6a1ff7af.mp4?token=DpfKJTaePITjLigulT6AVskr9PXxxbVA0uMfmNuhasYrJEp0iI251S39pjuObPQ6SQYyG-unsCPvsNLpE_1VzHzffvFHiW-blvMix8IZrNg7mOplmlemvjCvDR3lreAit0fPAJZ7w51iioBv12nm0BnSi7kA_hUJjmBcS9Kk8jPHk8DsGqx3yZfOijvmdvIUVlyEZq8z1IOH-sHxhlXeQa-a25EeOKrq8LiqQOCKYB8cxbG8q5MnOxl4KE03nRyjUDEAXK70grvG42mLNLuGi3CRmzf9-5b3ljKV-G7S6TCXA_35GqnJYflVJ1PBhp755zqaKcJ1ySPQd9GBTUZKGiBgBwIXIh4khzNnVG2wsrAF5sM-dY8ohx2FcSbIyhc0UVnlfWaDYE7eyQiGtc_UdrA_rBbP20Vtm3q52TD0KOa4mOjqqV3jxGcfd_sJB2z8nx4qcNL2j1p2gpqV2fjcjydfl89-d2jlCA8b3g166rm-PraCKDKHlAtpiViOsHDsch_4wgDI3oPrsbtmbpHZXnbuCJz6Icr6m6f05cf2hls8p1GCvXfTyjT5bq61e-nCAuFpGt_uhhOpEXy-CbqCofHaQG84W42e6F_LZnWYhN6cU6Z6YqB4FMgMZywjfzJIa4y6vvnrmSkDdvbIiVBANSRMzt4d-vQrjHRmSQe87lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6a1ff7af.mp4?token=DpfKJTaePITjLigulT6AVskr9PXxxbVA0uMfmNuhasYrJEp0iI251S39pjuObPQ6SQYyG-unsCPvsNLpE_1VzHzffvFHiW-blvMix8IZrNg7mOplmlemvjCvDR3lreAit0fPAJZ7w51iioBv12nm0BnSi7kA_hUJjmBcS9Kk8jPHk8DsGqx3yZfOijvmdvIUVlyEZq8z1IOH-sHxhlXeQa-a25EeOKrq8LiqQOCKYB8cxbG8q5MnOxl4KE03nRyjUDEAXK70grvG42mLNLuGi3CRmzf9-5b3ljKV-G7S6TCXA_35GqnJYflVJ1PBhp755zqaKcJ1ySPQd9GBTUZKGiBgBwIXIh4khzNnVG2wsrAF5sM-dY8ohx2FcSbIyhc0UVnlfWaDYE7eyQiGtc_UdrA_rBbP20Vtm3q52TD0KOa4mOjqqV3jxGcfd_sJB2z8nx4qcNL2j1p2gpqV2fjcjydfl89-d2jlCA8b3g166rm-PraCKDKHlAtpiViOsHDsch_4wgDI3oPrsbtmbpHZXnbuCJz6Icr6m6f05cf2hls8p1GCvXfTyjT5bq61e-nCAuFpGt_uhhOpEXy-CbqCofHaQG84W42e6F_LZnWYhN6cU6Z6YqB4FMgMZywjfzJIa4y6vvnrmSkDdvbIiVBANSRMzt4d-vQrjHRmSQe87lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇭🇺
فرانس‌پوشکاش اسطوره تاریخ فوتبال دنیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102842" target="_blank">📅 10:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102841">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d755c0e765.mp4?token=KrmHWlyvjao63jIVozIF4mMNofYAPOct_AtY4P6NRCXC99M4gsNth1qTYn6zQtvb9HcLQzwzCdKPy5MvIhn-xmYVvbzqvBLeC0TMGzOGOgKBavSzN3RQTOOydyMjdU6TVJR-yMqgYfpSE10A49ekVESwR-xiAoNck_0xK-XUVcqyrrvkBKjdYXrJE7FdEzk581sNQtF0f1eNUGYSN7HfbreaY8zYOlRP97O-WxxTi47dYEfUFejftX9a40nOunyW7hBYBMzD6z-SBsF4afh4yECVx0I6XQC4D7225JuYK2mc3YrT8_4sgaoO10ILlDJl3cL6QriNsLpJWgeINfYWDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d755c0e765.mp4?token=KrmHWlyvjao63jIVozIF4mMNofYAPOct_AtY4P6NRCXC99M4gsNth1qTYn6zQtvb9HcLQzwzCdKPy5MvIhn-xmYVvbzqvBLeC0TMGzOGOgKBavSzN3RQTOOydyMjdU6TVJR-yMqgYfpSE10A49ekVESwR-xiAoNck_0xK-XUVcqyrrvkBKjdYXrJE7FdEzk581sNQtF0f1eNUGYSN7HfbreaY8zYOlRP97O-WxxTi47dYEfUFejftX9a40nOunyW7hBYBMzD6z-SBsF4afh4yECVx0I6XQC4D7225JuYK2mc3YrT8_4sgaoO10ILlDJl3cL6QriNsLpJWgeINfYWDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
🔥
⚽️
سوپرگل دیشب بتیس به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102841" target="_blank">📅 10:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102840">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe450fda7.mp4?token=h3xtCqtQ4D_M9LwjRsMyE-AvM6b8nLnfZtUvdL35zAD4McSRLvytJim-QG-e_0t3sZmeiKDJnbLDc8PYZ-cNplgMBztkwSrfbMvmp8beZ6t3vGH94WvCoq7OlOrXHcI-0JtW6ojgwLDD8vA1-QYlC-Ewm0ZwYo02KoRmJsNU6VdR_ckGrcrTAbkxaTH-FQOAa30qjzB5VnTPsv7jAM9XtxNG6jGbwF9xdCwUiMfdmCsGTNE5BtpfiPSEznFBXhVx_Ee8iigkpABLX32HFA3TOWxyGQOa8EcohnFXcgbt95LaXeI-ZdKkGwlv-ZajdBSd7IUMy53HgmMe37Q29ox8gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe450fda7.mp4?token=h3xtCqtQ4D_M9LwjRsMyE-AvM6b8nLnfZtUvdL35zAD4McSRLvytJim-QG-e_0t3sZmeiKDJnbLDc8PYZ-cNplgMBztkwSrfbMvmp8beZ6t3vGH94WvCoq7OlOrXHcI-0JtW6ojgwLDD8vA1-QYlC-Ewm0ZwYo02KoRmJsNU6VdR_ckGrcrTAbkxaTH-FQOAa30qjzB5VnTPsv7jAM9XtxNG6jGbwF9xdCwUiMfdmCsGTNE5BtpfiPSEznFBXhVx_Ee8iigkpABLX32HFA3TOWxyGQOa8EcohnFXcgbt95LaXeI-ZdKkGwlv-ZajdBSd7IUMy53HgmMe37Q29ox8gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
۶ سال پیش، "انفجار بیروت" که یکی از قدرتمندترین انفجارهای غیرهسته‌ای مصنوعی در تاریخ محسوب می‌شود، اتفاق افتاد. این انفجار معادل حدود ۱.۱ کیلوتن تی‌ان‌تی بود و زلزله‌ای با قدرت ۳.۳ ریشتر ایجاد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102840" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102839">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP9TY2OY81nRZsJdU7QDhq119gc825tRAAGtK3b23vPDW9z8a1fckRslo_6i4D07Be5BGwKhS5-2wKLYupMXtu_fXu2pjDX4F9CGmxJ1BoaBrS2zze3rtwlNJdy3oV9TEAgQuX7GWg9cPYzXXexWA9nnXfqVoEKlStuTFKNP1TPA6FWgJkpzWdRroFAUvibNw5qB1-tOhRzZAqAEUrQGrDEaLe0grqnbtxtId59gamTPPDCGRnKC5v6_u4gtnLmR-rw5A3D2ADcYvaAv-kYCyQp9WHGYKxGVip1Fr9qFG9DjoV-ediEzzAO9ZjLbBoO_dodPPXfoiiUomhiq0FvQbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇫🇷
⚽️
#فوووووری
از اسپورت: فران‌تورس به پیشنهاد پاریس بله گفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102839" target="_blank">📅 10:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102838">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/102838" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پنالتی
راحترین بازی پولساز
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید راحتو سریع برنده شو
👌🏼
💖
مرجع
بازی های روز دنیا در ‌پلتفرم جهانی بت اینجا
⭐</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/102838" target="_blank">📅 10:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102837">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58d65b8db.mp4?token=nqNs8y0637-m0W4YYJyr8e7gB0f3bSN5siztWBvwV5PmoHeAxYSdAA0jdaoBeoMl05aBbTcL_1Lz5GVf6eCxUgn7QsxcT3DJprNKVo4KBN04MWyHy7p6wNp5jUKDXJMayvMR00s6DGPv0Ka7goerf43sTGyG9cO0v9v6HffMyMc91CDi6fVpXjfip96p4P0F5rhSPoeoCK2hTN63hu-3vkpQgyrTEGxYVVh5Zd2EEtCI94VQEdmgb97bDaUUrwvJQZH14y-GiRX-SM1-tTTJkKu-Bz6Ss6R3TwXgquEI3S5lEhXoOMiXlY2NuNOJ_8NHvcJ9eO94-LctJOKMcemcDzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58d65b8db.mp4?token=nqNs8y0637-m0W4YYJyr8e7gB0f3bSN5siztWBvwV5PmoHeAxYSdAA0jdaoBeoMl05aBbTcL_1Lz5GVf6eCxUgn7QsxcT3DJprNKVo4KBN04MWyHy7p6wNp5jUKDXJMayvMR00s6DGPv0Ka7goerf43sTGyG9cO0v9v6HffMyMc91CDi6fVpXjfip96p4P0F5rhSPoeoCK2hTN63hu-3vkpQgyrTEGxYVVh5Zd2EEtCI94VQEdmgb97bDaUUrwvJQZH14y-GiRX-SM1-tTTJkKu-Bz6Ss6R3TwXgquEI3S5lEhXoOMiXlY2NuNOJ_8NHvcJ9eO94-LctJOKMcemcDzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آقاآآ این بازی
#پنالتی
چقدر خفنه
⚽
🟢
بازی خیلی حرفه ای و‌
#پولساز
پنالتی فقط‌ پلتفرم جهانی و معتبر
#بت_اینجا
✊
همین الان ویدیو
#آموزش
پنالتی زدن ‌رو ببین و با شارژ اضافی
🤩
🤩
درصدی که سایت بهت میده.
💖
حتما ویدیو
#آموزش
رو ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r15
@betinjabet</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102837" target="_blank">📅 10:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102836">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac92224ed.mp4?token=tcAkSDwdwoBdz2APZhPp0EYASthhoBxPm_ayR0oRdVzjm7h02ScHH__2FPsCVxBlML3slf1Hmahnni8fYDFYbJzwzJFAQZfy5fS_49mRdPkGYmYPdcXSN5bBwrKfWvkREVP_Pu39e3vHNv4PinTYutyA-9DxW1-sc2sP38V4UmOjbBWSqE45yv2nJSQN6S6vCRV_J0ycCDB6uiAnTDzE1ixhRffBH6q1WUpNfP0IU9W6ozik0KXpREXQyiQgDoCsjiNMM43W33bvCFcopyjhm0TjPPvKcIWAMc42vSjDSqc1AF3UHJnqnipmqq0QYo8EvqV0x42NEIlY9_pCrDaEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac92224ed.mp4?token=tcAkSDwdwoBdz2APZhPp0EYASthhoBxPm_ayR0oRdVzjm7h02ScHH__2FPsCVxBlML3slf1Hmahnni8fYDFYbJzwzJFAQZfy5fS_49mRdPkGYmYPdcXSN5bBwrKfWvkREVP_Pu39e3vHNv4PinTYutyA-9DxW1-sc2sP38V4UmOjbBWSqE45yv2nJSQN6S6vCRV_J0ycCDB6uiAnTDzE1ixhRffBH6q1WUpNfP0IU9W6ozik0KXpREXQyiQgDoCsjiNMM43W33bvCFcopyjhm0TjPPvKcIWAMc42vSjDSqc1AF3UHJnqnipmqq0QYo8EvqV0x42NEIlY9_pCrDaEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
👀
🔥
مروری بر آسان‌ترین پاس‌گل تاریخ فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102836" target="_blank">📅 09:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102835">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nz-Sqsu64lErmRGJJEblsckSBnlXqf3uUotE-IP0VpuiFUWC0OJI2F_ch3zxgIuSuIOyDzct5LYT-erbymNEZGUMosertrArPMgNsdghBedW2Uby62FEJGIb-rmRoGhxBaTroyT989wCeXGwbNZCKnhaXmFomklYmkexn9eoI5ad8yMZ_QuG4A3TWJZ0TpFUSnPa1G6o_JMlMTmUzQCjmljVPWJIt0h8CUySR1Di0ffEZwHU-l7EQeR1IuswE7hBja3FXlHOcH4IY3Zv3GCVexvMA2Wecr4w1P4VYAMVlinJ7mGpz1Ilqalm2n2t6JMzHCXXUgETvjY1hAge1AgnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامون آلوارز:
وینیسیوس و رئال مادرید برای تمدید قرارداد به توافق رسیدند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102835" target="_blank">📅 09:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102833">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f753cf0933.mp4?token=rjXDe1-15FTanlxIGTlzFSoanSPk-C7p3hGrSxbgi6xk2RIvuiyigbttYUlLRS2pQ13tsKJLSC_9U0_ZvNyeGuJ5xRvJCQr7Mv6X4_2ShIUdheFmL7mZAQjekM1yjPN3gsnVRGHGuGI4tRdLYgIgeglRBn_a-wvB7vF6D2bCtC2U4MRSinL74Ftz3M-_PzgUH70oaPtTO-2ZHypH9IoGxabUmoPcgbzO9kqnGGWuNQxLa2p95jSeUDlPPqZ1spZ1EP70Zmg96GS6IzjXPZU61xjMELqcq_e0BEfie3LmsrU70FVZgDd7flWp_BUzSblmL439jeYRJVuvWIxcJqglDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f753cf0933.mp4?token=rjXDe1-15FTanlxIGTlzFSoanSPk-C7p3hGrSxbgi6xk2RIvuiyigbttYUlLRS2pQ13tsKJLSC_9U0_ZvNyeGuJ5xRvJCQr7Mv6X4_2ShIUdheFmL7mZAQjekM1yjPN3gsnVRGHGuGI4tRdLYgIgeglRBn_a-wvB7vF6D2bCtC2U4MRSinL74Ftz3M-_PzgUH70oaPtTO-2ZHypH9IoGxabUmoPcgbzO9kqnGGWuNQxLa2p95jSeUDlPPqZ1spZ1EP70Zmg96GS6IzjXPZU61xjMELqcq_e0BEfie3LmsrU70FVZgDd7flWp_BUzSblmL439jeYRJVuvWIxcJqglDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💝
مراحل‌صورتی‌شدن گاوی بعد از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102833" target="_blank">📅 09:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102832">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqzM3FCI3i6xP5UbAVohlP2XtoXMLj2WcXlTHk67zk2MZAmvqoX8Qh0_agd9lR5vpqzJxrfuVtf6gXxwxSGfArVQKY3yHrmfHWEqkGvAZZfXWHnMvC33LIsX6WC7_USVVEtGnp1E5kin3Wy_O6xCCF_pyqKa8QsPAQnxnaPeW-1Huv43832oMzloJ1jpWuzzBa0LDZFW8tQu_7bMDb-mOWFMe0NAEKG2wdjWNQ98WSbhsiiYQrGQLmobATmCEQSlCHSwv47UpZz2P5YM8dMv97on-qjx0YjrK2LuQUWKoUCb8mfuzd4CUQWdAM5qzpSqBL8wL9k3QtDYxQExtl7ttA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سرمربیان تیم‌های پریمیرلیگ در فصل‌جدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102832" target="_blank">📅 09:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102830">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e40774ac.mp4?token=uO7PinmAqu-fDEcn7nrSl97hQmwV1sY-Dkt5RbbPXMMwSSiJdUPJGUiago5pzycm94UrhM9kKZe4A4xWiPp64QB_mYSygeJ1m8Buqdbn_7Df_cERHVBK5UjExnq-j0RbgqRoDZoUcqSXJ-3jjuYmkKMCa5ZZEt1VvndvlUaikrkZeuZLZ258WfY-b6JIhjt9OEKHf08vfiwgzFpwN-mt2B882W1GM6oimOd2eAUCQl2Ra3peEthF0dNrF8NN0z4WEJJdYXldXPNEbcnazaYq4wR-No6Wc-wa9IpKnTHWTGj21p7FClU9AyajMTM8hM4rPO1EgQ-U98qRMVA8cn53wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e40774ac.mp4?token=uO7PinmAqu-fDEcn7nrSl97hQmwV1sY-Dkt5RbbPXMMwSSiJdUPJGUiago5pzycm94UrhM9kKZe4A4xWiPp64QB_mYSygeJ1m8Buqdbn_7Df_cERHVBK5UjExnq-j0RbgqRoDZoUcqSXJ-3jjuYmkKMCa5ZZEt1VvndvlUaikrkZeuZLZ258WfY-b6JIhjt9OEKHf08vfiwgzFpwN-mt2B882W1GM6oimOd2eAUCQl2Ra3peEthF0dNrF8NN0z4WEJJdYXldXPNEbcnazaYq4wR-No6Wc-wa9IpKnTHWTGj21p7FClU9AyajMTM8hM4rPO1EgQ-U98qRMVA8cn53wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
🚀
🔥
🔥
🔥
دبل اسطوره لیونل‌مسی در بازی بامداد امروز تیمش اینترمیامی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102830" target="_blank">📅 08:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102829">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e3b409b3d.mp4?token=YbDSsCc-bvar8vw7fk8EJD_XOIi7zS0tg0eyFHb6fVVZCnYgn_oy1d0rrTt8ASDIEP8x8kCku6xUWMv8LOowRvndKcY8c4Uf2i0iFRrctz_KL18bTxVMEb7ZlItUOOTpg6nN8Utm6v66e8mEeTIDzhsBWa5xnyYaikg0InCnxeHE9WkR0iwuAjo7mQaiJGJlRCcseD4tC-7D--mfFRTaj2-5OrA0KsNW_JG4_er22ZZwwJmYEfKFRL9iT3LGHLcaLZVpV84dzCuSXYX5r1qMYKOcPU05Jc0evsSsv9s7ARvc9hsuTyY_BTjzfMEdGiDw8S3F-Nj2qWe1CL_Vmw_2Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e3b409b3d.mp4?token=YbDSsCc-bvar8vw7fk8EJD_XOIi7zS0tg0eyFHb6fVVZCnYgn_oy1d0rrTt8ASDIEP8x8kCku6xUWMv8LOowRvndKcY8c4Uf2i0iFRrctz_KL18bTxVMEb7ZlItUOOTpg6nN8Utm6v66e8mEeTIDzhsBWa5xnyYaikg0InCnxeHE9WkR0iwuAjo7mQaiJGJlRCcseD4tC-7D--mfFRTaj2-5OrA0KsNW_JG4_er22ZZwwJmYEfKFRL9iT3LGHLcaLZVpV84dzCuSXYX5r1qMYKOcPU05Jc0evsSsv9s7ARvc9hsuTyY_BTjzfMEdGiDw8S3F-Nj2qWe1CL_Vmw_2Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
رئال‌مادرید و وینیسیوس در آستانه تمدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102829" target="_blank">📅 03:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102828">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a87de8fd.mp4?token=qBKHoXP1eZNxqs6eApqQFMtAtBu9qKdt8thywvbnOolbv4vwjRJEi7sCRcDg5bi-vU6MtZYpCQym_hBKPUvu8J4zvjw7qbSO49f4MQbJTwhaqQ2L-pQHzBSiv_y8cglT_gj2l1sNdM8iNAeCy0ih124NvE0b4KjW9AErdEIB8hthsopTz8tuHAM2wQRA3BBVoIlaoFjUBm0kafcoDC4Juh0ZfEA6_u_xfqLX9l6pQhKsDxAnQ9dUKT7jrEt-R3IxOcD7WtuB6NW_GJgjpwRho0mo0rxz1nkQ8NAnxkX7GFbWbgeVM8trGxAarZCjtGWPwL28gQW_9tdZ1kbm06k1oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a87de8fd.mp4?token=qBKHoXP1eZNxqs6eApqQFMtAtBu9qKdt8thywvbnOolbv4vwjRJEi7sCRcDg5bi-vU6MtZYpCQym_hBKPUvu8J4zvjw7qbSO49f4MQbJTwhaqQ2L-pQHzBSiv_y8cglT_gj2l1sNdM8iNAeCy0ih124NvE0b4KjW9AErdEIB8hthsopTz8tuHAM2wQRA3BBVoIlaoFjUBm0kafcoDC4Juh0ZfEA6_u_xfqLX9l6pQhKsDxAnQ9dUKT7jrEt-R3IxOcD7WtuB6NW_GJgjpwRho0mo0rxz1nkQ8NAnxkX7GFbWbgeVM8trGxAarZCjtGWPwL28gQW_9tdZ1kbm06k1oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
حسن‌روحانی: «یک اقلیتی هستند که می‌گویند اگر این جنگ گسترش بیابد، امام زمان زودتر ظهور می‌کند و برای ظهور امام باید جنگ را تشدید کنیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102828" target="_blank">📅 02:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102827">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJwrgxg3oS5JT4MyXRuCiPmdBqOnjSZnkw5VN6yuMXSyA7KiSnUmkmThVWguOJciCNwL3X0JLWB1b0mROS6DpThTo-TBsLhKGwGnE5gI87NwOm9qCkryk-DFruiQZ_4qVXN5Nh21oEfGTjpi_thKF-Y0AFi2EcrD6K0tzRiV3pyJ871_hOCN6mLHbnuOsw4ABbDUaKDUC6X-f-rQoMO_lFQygmzx2fTBxtRRZ4bTYmxKa09fSn2_JCAYEagWByT3IQTYydt3ndk1N-ygzcpOanhCVgOD4i9OOLrv8MhvedpjqvYnw8LSNw9SSxtCNbm4oJieT7FxTpygE0R8b4x-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
✅
🇦🇷
لیونل‌مسی در ترکیب اصلی بامداد امروز اینترمیامی برای بازی با سن‌لوئیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102827" target="_blank">📅 02:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102825">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFqNgtHCuBoU-89-qF2pXCCc2cmx-QSXIVPD-FeomgjD4hfzyN_wDZrS5KierSau3-Wq_9xP8UWraoyRzanoS4VMOgy94gTNdy75ukUuCurTiHHA0e2_UsihXPmh9S8DDoJ83HcwzXUCxke7smcpvuAQuy7cUAp9_OUsyGE_oWGwRYLdxkHXgH-x6sRCf5cGLtCNy3yQYzv9W8mgAxY_YT4PZJFbabaAkBN5TcKC0o_HiAAGFhkfDQIwgRU2H4eHDNQFyqAoCBTkbHIrr3OSXhS5ewNoODLsc6-7xVmkn31Bb6Hr7hukxqH5WSlLk55y6xXCsaRc1vppSC5TBxjzvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
اعلامیه‌رسمی انتقال دیومانده به رئال‌مادرید طی ساعات‌آینده منتشر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102825" target="_blank">📅 01:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102823">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec57fa35e5.mp4?token=ukh5rD2zb-hPMw_IsMMhy7HTMOOlo-3Jvm9zdztEeaCyVg0YGt-O_7GlpJtB2bcJsOCjfg3YKanJfmx0I80p3wj24djs_zGZtvrQG6wWrGy6pMkiIA3H8J9fe8mLxvTLRhYwinNphvlh9TnVCtMn0hcBMDr8fXGYDES7CbNVBl5ZpPylFrOycI4idmPLG6NI1cBSwt0WNl_7rQMAGtnv2tkB7f2yDnuyj9vOEOBhiLfDXpqIonJ4WJXbTrwCc6M9Iax4CMKXI9tTscMu8-N-NovN_vpDr-tFiqmiVfNfvLqsizrHoh1EesaujPdStkdsmKtQhNZnwH-Et5Ht5IL7HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec57fa35e5.mp4?token=ukh5rD2zb-hPMw_IsMMhy7HTMOOlo-3Jvm9zdztEeaCyVg0YGt-O_7GlpJtB2bcJsOCjfg3YKanJfmx0I80p3wj24djs_zGZtvrQG6wWrGy6pMkiIA3H8J9fe8mLxvTLRhYwinNphvlh9TnVCtMn0hcBMDr8fXGYDES7CbNVBl5ZpPylFrOycI4idmPLG6NI1cBSwt0WNl_7rQMAGtnv2tkB7f2yDnuyj9vOEOBhiLfDXpqIonJ4WJXbTrwCc6M9Iax4CMKXI9tTscMu8-N-NovN_vpDr-tFiqmiVfNfvLqsizrHoh1EesaujPdStkdsmKtQhNZnwH-Et5Ht5IL7HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😐
‼️
خرازی دبیرکل حزب‌الله ایران و برادرزن مسعود خامنه‌ای:
ما باید از جمهوری اسلامی گذر کنیم و به حکومت اسلامی برسیم. علت اینکه این الدنگ (پزشکیان) رئیس جمهور شده و بی‌حجابی کشور رو گرفته اینه که هنوز از جمهوری اسلامی گذر نکردیم! خدا لعنت کنه شورای نگهبان رو که این آشغال رو توی پاچه ملت کرد. چهل ساله که با آقا مجتبی رفیقم و خیلی تندتر از پدرشه اما یار نداره. باید به نیت حضرت فاطمه از هر شهر 530 نفر جمع کنیم به تهران بریم و کار دولت پزشکیان رو تمام کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102823" target="_blank">📅 01:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102822">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb48689a3.mp4?token=ewoUxdBq8HhXS7gKbQqYdL1f-WnEx7mTaGL5iYM1PpZ2MBbBU6-5AiGKxwV9uEJKb2rwgqXwnEU7pVNymwJ5BslRSg3VZetVjQmM-odb0b-S-OhMUxVMBKA3lN2z86i01-FD_YSIhs0nxkvxT80I_z9tWGY_gH_iUnpXtWvn7BH7QH1_oA-3J8e6btYZdEuL5h_5RiPUzGQDzoId7_reHf7scxbUBybNyc4_pNehhh09C6O9uXNrD6_RiJo01yWOAVDoVn7PvnepAvzay1ndinghqE8P-Myyyd2CbDI8e1kUEvRAN1KjeGRKqoSeofsX5gBaFYY1ATF6hA1BB1OqAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb48689a3.mp4?token=ewoUxdBq8HhXS7gKbQqYdL1f-WnEx7mTaGL5iYM1PpZ2MBbBU6-5AiGKxwV9uEJKb2rwgqXwnEU7pVNymwJ5BslRSg3VZetVjQmM-odb0b-S-OhMUxVMBKA3lN2z86i01-FD_YSIhs0nxkvxT80I_z9tWGY_gH_iUnpXtWvn7BH7QH1_oA-3J8e6btYZdEuL5h_5RiPUzGQDzoId7_reHf7scxbUBybNyc4_pNehhh09C6O9uXNrD6_RiJo01yWOAVDoVn7PvnepAvzay1ndinghqE8P-Myyyd2CbDI8e1kUEvRAN1KjeGRKqoSeofsX5gBaFYY1ATF6hA1BB1OqAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
تفریحات علیرضا فغانی در ایام‌تابستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102822" target="_blank">📅 01:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102821">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2yLURWYy-q6zUWJkY6qtjQZGpglzncEu9K-Fbu81yDA2U_nyB303jxntSxuzK33tp0qVvL3wv3TNgcUNK8tnpeH8TgRRLDuccdtf2Yw3V42a5HM4y6_ppT7CW08JFC1yXh5um0qMv2XfZ66BFVpfZcjLvpTT4WLAE-pQ8qTcXfW1pm80rllgbFy-0vUf9wWia3dnSGs93D68f-QE_7X6bIkwWJr5wtqpU2SRMpDc62LY0AhqBA1fY4L5UetXsFsfrlBjlQWJ4tE2H3d6tasEMHK3wXV-MrPZhgU5sPP-sx-LCTtTgHZILqFhNFcmlzn2UMnOdazj62Fa6dE74Tw_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پایان‌بازی‌دوستانه؛
🇪🇸
مایورکا
😆
-
😏
PSG
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102821" target="_blank">📅 00:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102820">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j42ej9UIebNIKXjyfc1rUKdIRj19c7OtVReT2fo4x_7exteLoivfIMvOzTLcbuJ7DlO85Ylr_MFFKZ1OpT7VMt_TVH-HQHHQm8Rkhn2hT-Ig1cRZ6fsWcvWS9Ab3AI8qYN6mdhO4wPvb5vU6TJDh1hytE6W9hpeIK1uZ9PmI_3VuixR392hmr-nuedoqjFFti54zAHqRgVdSvW76M5ns4pVXPURcCLJI-wjhazQ9bMP8sqJsJ8BAZrUWGzwhfpcOCo9aM0fJ8EYZJSflc5N5RZYM20Yk2WY7u1YZ4dpR53hAe7h8saLlPIAUFf9-kXaUZNQpMo95Frz8Iw-55DRjyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🗞
اصلانی‌با عقد قراردادی راهی لایپزیگ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102820" target="_blank">📅 00:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102819">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGAAjlPrFdSJU9rDRNXqvwkl9wHPzGXjdbq_R0XRZONchNJ5SelZsvkzT6DIWveKIDTLLy0AyJvdL2qfPKn_khIb_e5NuJ1W0XHbNNtgRP7gy5uD4A7NsmKBsJQFyggbeTfMVirp5MrDutmsfR7tbBmjxzknTtFM2WbRWunQxwVSpCnlHkKfsrt-WhjozE6-lkWjhl1X9XsCZK1jd5dpFFLHMiB4yUC60xfbcYvgCbTo8282tHnpP6bJGKTNd_QfYwpFn62s_BFissTcxhepCwLjcUe8qeAkAuLgqc-q-ofBTc2AIWbg13XHWHo93HtKZvwyAdze87HJ5K7AVKZVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پایان‌بازی دوستانه؛
⚽️
آرسنال
😃
-
😆
بتیس
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102819" target="_blank">📅 00:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102818">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/102818" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102818" target="_blank">📅 00:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102817">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=ffWc7xoUxaz6HDO88lISxh-QbZEa6dmvXoFEerbzehp9K6xHyjQQPqyBBx6tOMhY53pi9_xVpK6inMwhUFVD8m6hJMV4aOFYJBo0DDBjRs--6futSeR7fJBsSiymezlEqMAkzI_T3eDFw4RrpOjHpCF4Hbwz1eB-_pAbzWN0GpjMa4kimIDWOO67F35JYPB9_MUc0I24ftrr1MEUgzrCSePoyZ8Rk5BEsQNbGbfaZHLH32Vxoq_ELHx2ucw4fdISAbTzzxbN22JvApoxqwpwTqB9Qc1JScYoiNCALRLB9JNToYX1N508CjrQyjy-YOAoIvBVTMel43_cPDnNvrnmqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=ffWc7xoUxaz6HDO88lISxh-QbZEa6dmvXoFEerbzehp9K6xHyjQQPqyBBx6tOMhY53pi9_xVpK6inMwhUFVD8m6hJMV4aOFYJBo0DDBjRs--6futSeR7fJBsSiymezlEqMAkzI_T3eDFw4RrpOjHpCF4Hbwz1eB-_pAbzWN0GpjMa4kimIDWOO67F35JYPB9_MUc0I24ftrr1MEUgzrCSePoyZ8Rk5BEsQNbGbfaZHLH32Vxoq_ELHx2ucw4fdISAbTzzxbN22JvApoxqwpwTqB9Qc1JScYoiNCALRLB9JNToYX1N508CjrQyjy-YOAoIvBVTMel43_cPDnNvrnmqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a14
@betinjabet</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102817" target="_blank">📅 00:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102816">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNlhH5YgosaGgeApi1v6NtLYYLTKkGAncMi194xY-zlBNaXrTaEya1WGE-fxXZCC_VGiC3taRN0CHc4j9yUfTF2ccq8qFZTthfdUcCHJfCVTlKyKJPyl4jOF771mq-L_4brwMrL2oPI92t4_sE9311jS77d7Qtti5UCnRb9y-NTL54TqyB37hqFkdoNVUfnrn_U5lJatzaNmupox-IYwZhgrYyheRu6AwxiJjutmiWSbfB7exRzRswM2YIMHgc8RsTE8akJ7KueZIqGduHNCrbJJsSbGqZbAuwYg4d0i1zIlvUGunowlz3V7m4jmSbJ46vCsj3dU5vJ6WAhNDlpAiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💭
کامنت یه کاربر زیر پست تلگرام:
من آدرس مخفیگاه پاول دروف رو می‌خوام.
‼️
📱
اکانت رسمی تلگرام:
اونو که نمی‌دونم ولی منو می‌تونی تو خونه مامانت پیدا کنی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102816" target="_blank">📅 00:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102815">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56fd322bcb.mp4?token=fBrc4yGgX0hnmCUeo2xn5LaWYp75cnStmju3r-MVs25AmkHIilz4X4B2S2Y6n4ax8TrDvVrkBw5dNeTn6aRZoRCrTfxOovTQWtgf8KdVMamlsVCc99YoxrChwzCCxW_drQKIaDF5AItd4Y7GlfiWYXDAyAm3ODRWs1d02ojNEoYelDMsThnU-NHR1ovgWSAPmpje6vaeBzIBIgpqQcYWkSmJH4A0wVjNILI-urp6DtzXJCCZfaB5ATLLCjWUGfNA33Ndz1Da3B4JAlwREIzTI0GoFesoVP9W9jhYL302-TbKcQFXiFEjWCWjRZw8TZzpYdpgKJyVK46KSX7cLIQTvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56fd322bcb.mp4?token=fBrc4yGgX0hnmCUeo2xn5LaWYp75cnStmju3r-MVs25AmkHIilz4X4B2S2Y6n4ax8TrDvVrkBw5dNeTn6aRZoRCrTfxOovTQWtgf8KdVMamlsVCc99YoxrChwzCCxW_drQKIaDF5AItd4Y7GlfiWYXDAyAm3ODRWs1d02ojNEoYelDMsThnU-NHR1ovgWSAPmpje6vaeBzIBIgpqQcYWkSmJH4A0wVjNILI-urp6DtzXJCCZfaB5ATLLCjWUGfNA33Ndz1Da3B4JAlwREIzTI0GoFesoVP9W9jhYL302-TbKcQFXiFEjWCWjRZw8TZzpYdpgKJyVK46KSX7cLIQTvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
تاجرنیا مدیرعامل باشگاه استقلال: از عملکردم در مدت اخیر رضایت ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102815" target="_blank">📅 00:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102814">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8DxJRMRkgQdsEx1FQKnmf38GPjaHtyR8u5YDKZE-eL4sDCBNVjR-Y0agIONR-LX0LawqK5y2NmaSvDW6F2ZWinbHQv8nZNNGwn1i-3IM_7gAKALsTkvixu3F5DmpoDY6OTlAoxnXYJiMNtPYK6-2tbKlV8xwhazLj07twhCj-Km7qLUa6vaS-qZG7Dx_GNFt9Z0ujceIhpk9ab_L9JYpz5ZqYwzosVm4yeNWan2xf6YbRJW4npQhvBg3iTq4kt6301fozcgGL0cL7RASSK7NLPFX4fpDf4pcWHJaYiJ-ov90cAdPgN_Ffev0SD3guX8WLkTU03mDAuDmeVsRtPTGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد صلاح:
من تو زندگیم تاحالا همچین چیزی رو ندیده بودم، 25 هزار نفر فقط برای خوش‌آمدگویی به من اینجا حاضر شده بودن، این باور نکردنیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102814" target="_blank">📅 00:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102813">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102813" target="_blank">📅 23:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102812">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gmv_I07vkprNZhVXVx7hZ-HPwO8QEmWsJiBq3XwBbS7E3wun1H0BoKZ-UBkp_iugictscZNzKx7l68zr6PvGoghJvcFihJ1ha4uGwfIBckC3-MJtY27GN7hx6EhA1dMDloVAEE_9bFOz70rYbv83JQz5W-K_c4W3U9xOYL5ZOuk8DK7wzL-SsNNZhc2bQwbgC5YF9sZkpTmaUB2UdD2XlNCSFBhbcwMHi43ibrCHrdWVj80pubjIwX9xhjtHqAw-TbRFBMsKX9-vHuXyZ1-egDwdYu5x-tA6XXDCL65xxNikC67w5CRMVNk3btnaufPZmdevnAv6c_A2E9_O9KwYCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه تلاش و پشتکار:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102812" target="_blank">📅 23:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102811">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHd43QaKi-7T-_OnBAf4wpKdu7D04W3Ldm6sP5U3Tfd0cDdYiXphH16Qr-NMyRWw0eZ5zYG0vsYp3FsLg9fzDC9JW6hS65L2x5kby18M76amOSVgic_lEU6Z-F-ueHXDiYN2dmjWpp61xXyEbRfTEYnpiYBxCGcgtMS1idWo2GitJHlMnPk_A0vCdPz1fSVMJwI1S9hDlhQRpgoCuAHtDCLQx-c5ywh-NCOoDgYZFghoKGpU6Rshof9Y1lCOVzoXosT1GIPEa1Tfbzt13V4Ib3lFg9VBee_jhbtK64XvRYKjYC9GQ2-3e6AKm5lX79DczH78BptjuPuflKDT9z4zAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد صلاح:
من سخت تلاش میکنم تا در لیگ و در اروپا به موفقیت برسیم، چون من تو هر تیمی که بازی کردم، موفق بودم و همیشه یک بازیکن فوق العاده بودم، و این چیزیه که باید اینجا انجام بدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102811" target="_blank">📅 23:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102810">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Esgard-VPN.apk</div>
  <div class="tg-doc-extra">42.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/102810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پیشنهاد_ویژه
فیلترشکن محبوب اسگارد ‌وی‌پی‌ان
تقریبا با همه‌ی اینترنت‌ها کیفیت اتصال و سرعت خوبی داره. حتما امتحانش کنید
لینک گوگل پلی:
https://play.google.com/store/apps/details?id=com.vpn.esgard&referrer=628035</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102810" target="_blank">📅 23:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102807">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uw7QlchT-_UEDMzZMw0R11FUhGFFnpCVCwrlv2Y0E7_k4rnHbg_y8BQJ50l2Od9ZIWiU6R_yCGQ7NGCnRaT4u0pr4p7lHMP6K7CxYbIGn9vWNsFTImTzEjGZmujXkVrHPfzHe3RT17eltd2YzRGaO_tMnt-VhHGkwZ7yiaGpfx9CAevPmdlvtE85TXB9AvHVaaTW9aVyGLzBrFdZlIsUSNHBSOW92sHmy8PU_KqVy3zvQxkYxRrOHIhhsrJIxIEYzh3HAMZYLK_tUgez9Do6zo1FjuWffo_3AoZaIikzRnWfwV7uINgCmojA2rLoEqVwg83QkUggGvbngH8Fip3kjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lwOYxVcjJPuPk0QeZis651wMZ57aKmmrIxtS7f5BZlIimqgIlbuTJBh8pecSgy1awSQeWcqNMDfzYe8hIFvOFXxy4Ba7QNDpwDmim1KL7q1UJdtCXx-IAIXhfEa3Vc5effday0qu2SeuMYD8onQm0eXY4Z2FT6B3REH2Dc9B_jJIrTVE1n_dEnPpUiywLKbKJWbatIk7I7eIF9VkKA4gEP-rJjcV_Oy1NzqQ8Jae2IBh7G7aADSMb6oASufKrRkcAK5haYw52S88SZBH6IcOOyv19LE4AkIskIdixs5Gcs338_e6ACP6KF8RR8YUJh9FGKp2KkoVOIqpYIaYnlouLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AA9qqdr6_47B-lMMEe_FB7Mj2Fe-OMlnadLLGfJ9xxyub_7Vh74jn1yLPI2sxV6vp2gU4VUz3S4pp-Ci7Gjdb6C3OvnnXURo4CZ_MPpJwfaRn7H1193nMYHpl6jx_ZcfmSR_HBeOZfk2l-1jhDf9OEuWw1Lhv1SspePOrUdla7qqmMxK6jnqQFWOeLt5B0RslB_lKwgW5TuzWX7NzWKHDAcT2bTDD6PMl_MriGvmMDTh-V487aGm31F4l27mniXDDVOreGV-YwzpCvL9hCiKkU6L5kWq5Ig6_LnQuyDXhtoNV4NMli-XkhoxT1KTUjY9lzmZwmc6DDSXnlECULUeDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استقبال برگ ریزون هوادارای ترابزون از صلاح رو ببیند و کیف کنید.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102807" target="_blank">📅 22:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102806">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cr1M9lf8abern3R4sSwYUlhEMTN1ZPfntrPPYYaN0-EDg3vIn9IApkWTbB5tG2MOjRmKTP7EBnIqwcc8HCd6SvOnRChLGdVOc7TDunzFKrRj-9gMykhw5e13Lf3FCipVrX_Js_oA3cp1V7GGo7kaD7FhMs5bFrEAw4yJATOX6SDhxIT3PPZbRPf4CvnFp3gfY9hYclzP6yuM7nLVwuPkTE0MmlEG_7a_-oSJqjUAjXeMYB2y7CCJKZKq8x2-beH1VhDnhDEPCnLJkqu291LoEKzrBUFAebrJ_Y5q2lB-8VZuB4nzPOzJgscMlebxpCa26TiO9eLDyKMuNoCPXOlrQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
‼️
وینیسیوس در اقدامی ایرانی طور تمامی پست‌های صفحه اینستاگرام خودش رو حذف کرد و عکس پروفایلش رو هم برداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102806" target="_blank">📅 22:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102805">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjcfsZqI74U4pZTEDKTDeNsG8_a0CVEXASv55S12jiDx_ZN1ExLLXHFzfVDbBQqfCys7VOz_oWXJj4m6ry-h8bBq9oX6VNb0jMh3BcePQQuGgxkgTCV4jOO7zbOJ20s9LQjudPPx1pkQwwoUlZMFLwpZMR2ovvKGhRr-btrrpdrFXQHoWGOauYVjo6EwYHj2yDp6Wg9nSZS6BuzM8geFnwTVJcd1SBNB2bq8pVvp6COWkrU7zUD32KCnISZ2Cp3aWFYshVwy4REMrQ06N81Fsovd4rS6vFQsryanH3OtjI9KbnE29cBi7aSwA2NvThQ9CEDWtPeqduDXToc9X1GZeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
رومانو: ژوزه‌مورینیو شخصا در پرونده تمدید قرارداد وینیسیوس جونیور وارد عمل شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102805" target="_blank">📅 21:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102804">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoiJ6qJU3xeHvSELjqVauv6yIFNUB4ppMEp5rovTnrhcZLdQPKUShu7wOO3GcHyTrZ5K2sb_ha8IQOBtqQ4Wol7QXRGUFKYnx56FRqho47kcRcccRp7sZx1K8XNPhKvjJoFaiZqd3Ro61IPjRvVVBRK-qT75ECSCsP_K0WlPFdEROtiIO7H5DvEI4WxRx699kkL7vv0QYVa5keqA4PRSXeCI7cfFfRS9UBjf7djBrSSZYSVwoFW9Xdy2HNAJZ9RPnXJGV0YFPeVP0zySTIzrb8Pvip_8N2R4qxFTxYddmq0Auh8YmEpSibde1UCIegLW6y0XRRmMCz36pYKBpkjhjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
کوکوریا و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102804" target="_blank">📅 20:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102803">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti6nymLlHbHagfrFW0aRFgBST7NSaou7CtpoztfSkOh2KiKZLz-lCSwRMuTFWR5Ss42TM2Y0SddMeX0q_CP3rsBh3vXhx51JVIqvNpnGXi8CmQto-XiBUlmvNvzZ3xudlL38EymKRL0SCc5Lc0ze1xDO_D_UNqYaatZ6qDbT60aa8srBoBckFmKkk-yUPA1WiEEYAxmgVGbsF4iLaVfULs6Fn2izJsDGvujfrs0Wu94tzTOssK33x4vugtqHi2PXktVmmz7k2rBkiXWXQnXCHPDoyfkJFlTMXOq_tFyRJa-ul2GbEtbvg4BX6RW3NIne8LQi_mSJaEitJ8eBUmw9BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
تاریخ
مرحله گروهی لیگ قهرمانان اروپا:
هفته اول: 8 تا 10 سپتامبر 2026
هفته دوم: 13/14 اکتبر 2026
هفته سوم: 20/21 اکتبر 2026
هفته چهارم: 3/4 نوامبر 2026
هفته پنجم: 24/25 نوامبر 2026
هفته ششم: 8/9 دسامبر 2026
هفته هفتم: 19/20 ژانویه 2027
هفته هشتم: 27 ژانویه 2027
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102803" target="_blank">📅 20:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102802">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdjKJF3e4zRW_7Rf5ktEhe6LFRBkTrezXvW8VypRlxLPUPrHLXHMNE7xpyMR_4Bmr5HzwM8G-MNIyW5SKTBpsJpGan1z3umdFnwaLrDW25pC1tw-GghAdCD5fHNosKXkg7wOmkHGTXc3RljlRz2ry1u6rVpaj8RkXi_rzcj5V_ysS8yOn5yKfVAliWvapodhThknUMPUAAjTnBKU4-rgwz5_TBGqkJ0Y7R55yCbVuR22TrAqk0ObG8ooHdVTW3eEtzGuN_sYU0HM1OOovVuRoYRI1g8KlDMSM9xvJArO2B1NXb4OMc-aZQlbDP3tKPng6-94vtds5geZjwV9rpNkoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇲🇦
جیانی اینفانتینو به مراکش پیشنهاد داد که در صورت حمایت این کشور برای ابقای او به عنوان رئیس فدراسیون بین‌المللی فوتبال (فیفا)، میزبان فینال جام جهانی 2030 باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102802" target="_blank">📅 20:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102801">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e865a76e80.mp4?token=NtAsAS_NIMyorwP_j2bKNvUYmX71LRBu51xAYVP2pX3Bc3L6r_QQnl93AiGvJziCrZedZFI4XY8gtI2ZYLDRtdXIb7JqMS-CMo8WyhrxCAFBeVt7Xd-gEazjv5JwDoSB6-RR2BmCnl04gZgDFcz9RtU9VEfkzG6yeDF0MxDNNpwRxzxt6bKlglhCeJY9NPhTi24_kFS6UXMItYu9Bj6qosGHQfJ_Qo9Y_4FQ5GJp7-SOLbBFeEV5EuqJ-B_k-JPTKwW7hCTmx-Jk38vXaXBKWs8S9FVlU0pf7iNc-N5Yl7EWDfC1w9g_iGgy367J8KlYj7SfnaTL8GgrQuDRAWbjDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e865a76e80.mp4?token=NtAsAS_NIMyorwP_j2bKNvUYmX71LRBu51xAYVP2pX3Bc3L6r_QQnl93AiGvJziCrZedZFI4XY8gtI2ZYLDRtdXIb7JqMS-CMo8WyhrxCAFBeVt7Xd-gEazjv5JwDoSB6-RR2BmCnl04gZgDFcz9RtU9VEfkzG6yeDF0MxDNNpwRxzxt6bKlglhCeJY9NPhTi24_kFS6UXMItYu9Bj6qosGHQfJ_Qo9Y_4FQ5GJp7-SOLbBFeEV5EuqJ-B_k-JPTKwW7hCTmx-Jk38vXaXBKWs8S9FVlU0pf7iNc-N5Yl7EWDfC1w9g_iGgy367J8KlYj7SfnaTL8GgrQuDRAWbjDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">8/5/2021
💔
🇪🇸
🗓
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102801" target="_blank">📅 20:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102800">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgLxinY_jTTWhwBxvMu5JX7fUrEZIpBtA1ZWt16EPDksdirL7Nv-JMfdsrTXWq1Oybc_RhDI7zP09Pgltrn2MAlu3FsOsHUmKfWg_l7pp0easQ_2_H7DTgBw5u6pcFizvbVsHvoHQ4sOK-samquz4xUKnY052B68X4XgMMIqV-wTeURk6Ih1mCsATmuSbXXK1vdJTMxTR9dN8q2xZ1Lb0z33OYRQjrf-eHYm96fLTk9bkeo7rw8WpRSqi6X3l1I4-U1EhFu1iZw-RbU4ScFIDr6e6y0m2a08fAeNKtVunrD7Yr7a8nLSqmzki5DjpIouIFWf0G7aBGCH1e979L2hEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
استوری جدید رونالدو در حال صفا و آرامش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102800" target="_blank">📅 19:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102799">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b7936557.mp4?token=XPk74YydE-psMuRJRm6CCQdIXektuy150_3FjDSeeow-qiABK0RxEp5PAFMFkXzmxxcgg4iiEsGWoUvxhlVoNVcb2R1-1MsXDRjf8XNYaG2fPRKuJXCjk0DFUeh3J2Q7pLpWh76NsIc1Mks0s3xulHj2KRCAcY7MiYcjABN88LzlOKtsKcsaKpGjTCsZruRCC-dCy4PN90eAoHwaUepWAvPSjfu3ieZpc_JMnA9rCGG-OwVhh3vgxBjE8uXUU2SA018IbfXV_MVKEnw_BhZxK7w1fzwwzfZ5WbRzhXAP2UYuhQkSHa24SkX0dtatMKpjocW4ZZ-8Na0UaG5oPQRQXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b7936557.mp4?token=XPk74YydE-psMuRJRm6CCQdIXektuy150_3FjDSeeow-qiABK0RxEp5PAFMFkXzmxxcgg4iiEsGWoUvxhlVoNVcb2R1-1MsXDRjf8XNYaG2fPRKuJXCjk0DFUeh3J2Q7pLpWh76NsIc1Mks0s3xulHj2KRCAcY7MiYcjABN88LzlOKtsKcsaKpGjTCsZruRCC-dCy4PN90eAoHwaUepWAvPSjfu3ieZpc_JMnA9rCGG-OwVhh3vgxBjE8uXUU2SA018IbfXV_MVKEnw_BhZxK7w1fzwwzfZ5WbRzhXAP2UYuhQkSHa24SkX0dtatMKpjocW4ZZ-8Na0UaG5oPQRQXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادمین صفحه رئال‌مادرید بازیکناشو اسکل کرده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102799" target="_blank">📅 19:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102798">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFJ6u1CZGco354IDEIfzQXOBXsTjU_50AkzMSknTtnNAp96QEVRRtV0ry8rksveAhOR3DYOXiqZtTIWey-IbEskAaHTseii9lPX24BfvVnTTLdE3jKijQWgzmagnRZYpVANGhQ4LjQvX5ZpZU8HeOtARjOTrfGqmDTHfjZmUKzpiE8PzE63FyVBEp6Rt78ORyp9YvAm1owIH86yPAtlCibM9Ynj36BT20wIAI7lTAQs0rt35Z46ifli-UmNZWTJKMoD3y08LsDOKdZcaoikKGQCZMc1OBMNvrhNodTHElVJkJhk8qb0hWlM3Rnn_tWLJZpOYHulYMc93msNwGR1xrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🗞
با اعلام رومانو، مولینا مدافع راست اتلتیکومادرید راهی آا‌س‌رم شد
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102798" target="_blank">📅 19:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102797">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a21bec45c.mp4?token=q5HpApMzfo4T4Vwv7fNJV02r632OGrhAmatjbSTfls89eTtuNXSVc1jrfbaVdDljQF6osKJFgWdXr8g6QcI_KoHegooNHi29nbhr1etKI9Js_llz82COXn7VTvkGd8gUcTuoGrqF6ABnGKvek0hIX-STr6dx3Z1AVeNDTqVH0loz5wmzrgfd60nQz9ht-rDBB-FrH5PjP9PySlLK_bZ_-_AF0YaebKGy5gcyBMUPEe21awNC83s0LBqL14_hNGiw33EZyarhbWdWnErOhKLSYwdR6LAiToVV6C1d2xeW_lvbeCggGglkeNiu-n47g5pqrrJqZkclGS6hdw8NsOhyRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a21bec45c.mp4?token=q5HpApMzfo4T4Vwv7fNJV02r632OGrhAmatjbSTfls89eTtuNXSVc1jrfbaVdDljQF6osKJFgWdXr8g6QcI_KoHegooNHi29nbhr1etKI9Js_llz82COXn7VTvkGd8gUcTuoGrqF6ABnGKvek0hIX-STr6dx3Z1AVeNDTqVH0loz5wmzrgfd60nQz9ht-rDBB-FrH5PjP9PySlLK_bZ_-_AF0YaebKGy5gcyBMUPEe21awNC83s0LBqL14_hNGiw33EZyarhbWdWnErOhKLSYwdR6LAiToVV6C1d2xeW_lvbeCggGglkeNiu-n47g5pqrrJqZkclGS6hdw8NsOhyRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚠️
هشدار، ویدیو حاوی صحنه دلخراش می باشد: صاعقه یک بازیکن فوتبال را در حین مسابقه در تایلند کشت
❌
تلاش‌ها برای احیای او در زمین بی‌نتیجه ماند. به گزارش رسانه‌های محلی، ۱۲ نفر دیگر نیز مجروح شدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102797" target="_blank">📅 19:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102796">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbYAzjSuY4vATTPfospxOSbbmZgrEdgoUkkEMixmWfCMA6v0s_Grw1bqYoO0ngTL0TXR2ZXQ1Y23HuuIHH_uxFvv6LHTuZ4ZV-0MlpTnJOhGkigNv7zK6iD-tGvWoir7aiKTfOsE3OqHQ5zJO_zi_d4gS4gV4ZBB1KFT9dvlm1_y-PaT2AuBVtHowQtl_FhpAWPhBByW5o4nSgeDgWwPz5LT48U8Vx7CVVtC5sawqSgJMxvxVDF8H4KpwZGvFbKdI6SMo7GetqmDJZfFjl0StpTqyS6VKNs1DVxs4jDNxD1sAtquqDXMQGQREEayTUugvhe3cmnIkocYM4qbdCt3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
💥
جزئیات انتقال دیومانده از لایپزیگ به رئال‌مادرید به نقل از فلوریان پلتنبرگ:
🥶
مبلغ اصلی ۱۲۵ میلیون یورو
🫣
مبلغ اصلی با آپشن حدود ۱۳۵ میلیون یورو
✅
۵ درصد از حق فروش به لگانس‌اسپانیا تعلق داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102796" target="_blank">📅 19:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102795">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpvWQ1_PE-78GmFtZS6kgtnN2msyn5VCuYbFRoRi1uW0_2N2MrOc3fXYAwL_r0-oeU2377B1qWblglyaXyLwopCQlEJog6wXh1Uo5KC-PNyvfErCsHhHNFY3b3X_t_4C8TOH6ijG2xG99Pd-geE3RTpGfF1E8VmsywsZPqRz3UpfdVxZCKtIsaVf_D49CVXstwoTOKMBlxYj4feWE6RP_9k7Azg16Q5ypX0waP_Bn-17hotMLoFTMtfIlig6qpolhgYvegmmY23f5m36jrmn0QJekKVh3C0kHBwNf2g-eYwwxWu8O025u_rEv4O0H2cdUjNt5raQE5q20nMERsw4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
#فوووووری
از اسکای‌اسپورت: وینیسیوس جونیور پس از مذاکرات امروز با رئال‌مادرید شانس بسیار زیادی برای تمدید قراردادش دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102795" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102794">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/833c1a2554.mp4?token=tMajNWlYKerCmrretdSZktG4dXkhICcU9S26Jsyxvaj-fwmuDl9RdJ1pAzMLIWeVelt-s1VDFJx3rGZbAoNtnlSWMxs1N_LKxTkT0P3eV8XDW7E2jLiPvAZdflXlocH_l1GDLbK1RL3CuPlPD97YX6vWa6_XwgklnS09d1VxY7zK8xwx8CJfwl48MvLwrwQL5RKNgdMXvP5g13oEQ_1hBcwrFTTgACqGVM37t4BxgSF2dQo0t5Z3kVCSgKzNHcDGTjfGb0_f1P53vD0eFdHdLL2Ahe0gMyvuWMOKAC3CLbsqaNlhFoLptVMdmeNMvktMsgACEkdGtZba9qARyYB9JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/833c1a2554.mp4?token=tMajNWlYKerCmrretdSZktG4dXkhICcU9S26Jsyxvaj-fwmuDl9RdJ1pAzMLIWeVelt-s1VDFJx3rGZbAoNtnlSWMxs1N_LKxTkT0P3eV8XDW7E2jLiPvAZdflXlocH_l1GDLbK1RL3CuPlPD97YX6vWa6_XwgklnS09d1VxY7zK8xwx8CJfwl48MvLwrwQL5RKNgdMXvP5g13oEQ_1hBcwrFTTgACqGVM37t4BxgSF2dQo0t5Z3kVCSgKzNHcDGTjfGb0_f1P53vD0eFdHdLL2Ahe0gMyvuWMOKAC3CLbsqaNlhFoLptVMdmeNMvktMsgACEkdGtZba9qARyYB9JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
وینیسیوس گذشته خودشو فراموش کرده؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102794" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102793">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خفن ترین تیپستر های ایران با هم جمع شدن و TRUST BET رو تشکیل دادن
👍
هیچ سایت بتی دوست نداره شما این کانال رو پیدا کنین
رایگان بهترین شرط هارو براتون میذاره
حتی هزار تومن هم دریافت نمیکنه
سریع از این لینک جوین بدین کانالشون
👇
(این پست پاک میشه)
g14
https://t.me/+cBQ8n7zLQiUzN2U0
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102793" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102792">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLfrWNQJdwgOEDcbDNVP1DZoFVCPkPA1eqEsux5fzgZxB_sFvMEjA2xHBk_uFZ89a0x9sfykJmwZb2RzB8WXgevLdmDUYSX54J_S5wCr9HN60TeXQ99KKcO5AZgGHnnEKiixUo38w2ZADJXVJhmILY91WZCI3Rt2bNgzp5CXm1z4oOMTC3uhCr8fxk-rVA7SShUWCdd-GUB14Gwn-gAHcKR9ip44MvBxXsma434xNxx-ljr3fQ9BO8pJ79-VdpQFUkImCAN0Nj5UoG7aDpqNVwa41KweE-HV2C03RQNIm5JOY8QQkrfYZnQGocmWuoaUPAs7fVay8bLwkmw-Ee0EuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 میلیون تومن برداشت روزانه ی کانال تراست بت
🎁
پول دراوردن از بت تجربه و استراتژی میخواد نه ادعا
برایند ماه تیر توی کانال تراست بت: 78 درصد رشد سرمایه بود
✅
40 بازی اخیر 34 برد
📊
💠
https://t.me/+cBQ8n7zLQiUzN2U0
g14
💠
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102792" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102791">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a91c5460c.mp4?token=bSZvINoJP_9GtkU61qJI15tU5CF8jHV82g9iHpwVmN6kow3K4kTsL_Hd0uic3SyMaqYZLRuWtapH65TU9B5iY9r9eSt_tuRp-pWWplv8aX_SEGje7pufVXXYrZPWiMegbfxa4tjCYrC-tKC7P8-Ss2fFQI-NVsUUa22j3wJcnlVlpevxQDm3vIvS0MUCtPxP0eyUDCE1TfNN9EyfORLjXOmzAZnpzYavktBUJT0kcp6wAFU8XkYNEPEDKEtJZ1qvcTRihr3xsrRhyGDV9y8flD4o602uQLEFC0hRFqrmQiEiRtUmDfvBVZg_pPAzibH6Pn3r7PwwJ7kO_VZU0vEc6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a91c5460c.mp4?token=bSZvINoJP_9GtkU61qJI15tU5CF8jHV82g9iHpwVmN6kow3K4kTsL_Hd0uic3SyMaqYZLRuWtapH65TU9B5iY9r9eSt_tuRp-pWWplv8aX_SEGje7pufVXXYrZPWiMegbfxa4tjCYrC-tKC7P8-Ss2fFQI-NVsUUa22j3wJcnlVlpevxQDm3vIvS0MUCtPxP0eyUDCE1TfNN9EyfORLjXOmzAZnpzYavktBUJT0kcp6wAFU8XkYNEPEDKEtJZ1qvcTRihr3xsrRhyGDV9y8flD4o602uQLEFC0hRFqrmQiEiRtUmDfvBVZg_pPAzibH6Pn3r7PwwJ7kO_VZU0vEc6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚽️
برادر گارناچو که فوتبال‌بازی‌کردن یادش رفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102791" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102790">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59768147dc.mp4?token=P6ueERHNiFolUajE3UxcKd4UA8neDCB5TpMmikuFVUuQVGgwEPNlWoKLrWds4DrroZcgisR4otA06pbEMtd7X4WjtGRz2kfLo01k5EDQXQZJQo0E9yMa5I0R9vWnoA275VNn6tUBhhFPGtSbd7aO5DcdDGQBu7Wgex1MK6b4Llr1Zn3GR3IwOZis9bFNgk2flipyhKngehuUoKttr63Qp85aKV2UEv0LYiANJdKpHWmJ2wpouuFSSlxCgJ0kdFTFpeUjGUlqZJzr2SdVslOtAvwhBZmGO8jawGsEf79AVRrQeCQKoYiyPxmegdLQZyGUCJbmnjqlkLVdZCWhRQyvZz1kCDc3hAGut38l4rIHYEvDN45SKVFtbONtBXa-7HjhtGuy_I2LhBw6PUsTvvzC5xpAE2rMw-v_4Z_bxCMZO87EkOY_us6ljSnTEeslWl92yPdIMAho_-vjQAvplPKwjmOSytbw0B71Blhm5jHtPw5Dv5FeEn658FYraPUr533UVK26_BUP3xN-evFIwGh4Cpe5ZN1gNCgh_9qJ09epTaa6A72QKXya_azPqUYv-8hkWmBx3gKluModNEiqfQ1DtjLmq79_4v-EQxK17XoW3nEs5AEAlTXCT3UorVlJptfqLDs8eNE67HK1UAfne9oSPpY_tYms47xohNCvIMCC81A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59768147dc.mp4?token=P6ueERHNiFolUajE3UxcKd4UA8neDCB5TpMmikuFVUuQVGgwEPNlWoKLrWds4DrroZcgisR4otA06pbEMtd7X4WjtGRz2kfLo01k5EDQXQZJQo0E9yMa5I0R9vWnoA275VNn6tUBhhFPGtSbd7aO5DcdDGQBu7Wgex1MK6b4Llr1Zn3GR3IwOZis9bFNgk2flipyhKngehuUoKttr63Qp85aKV2UEv0LYiANJdKpHWmJ2wpouuFSSlxCgJ0kdFTFpeUjGUlqZJzr2SdVslOtAvwhBZmGO8jawGsEf79AVRrQeCQKoYiyPxmegdLQZyGUCJbmnjqlkLVdZCWhRQyvZz1kCDc3hAGut38l4rIHYEvDN45SKVFtbONtBXa-7HjhtGuy_I2LhBw6PUsTvvzC5xpAE2rMw-v_4Z_bxCMZO87EkOY_us6ljSnTEeslWl92yPdIMAho_-vjQAvplPKwjmOSytbw0B71Blhm5jHtPw5Dv5FeEn658FYraPUr533UVK26_BUP3xN-evFIwGh4Cpe5ZN1gNCgh_9qJ09epTaa6A72QKXya_azPqUYv-8hkWmBx3gKluModNEiqfQ1DtjLmq79_4v-EQxK17XoW3nEs5AEAlTXCT3UorVlJptfqLDs8eNE67HK1UAfne9oSPpY_tYms47xohNCvIMCC81A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
روایتی شنیدنی و جذاب از لوکا مودریچ افسانه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102790" target="_blank">📅 18:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102789">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
⚪️
دیوید اورنشتین:
🔹
وینیسیوس جونیور برای موندن تو رئال مادرید 28 میلیون یورو درخواست کرده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102789" target="_blank">📅 18:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102788">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fw-z0gmrx8G68s5E4zQaAQKuAk6ZXvvcYO7HLR7mXrPSMWmcWWy_K1sivQcd8JKmBYizDbg-LjbSEoCf_2xQqPAEmT2T-syK3tHRegpj0J0TGgXe3UKF2PQp-qaQVqMk-B9cbC0QkokClNNGtgSJLAPmqyKjUSaBM5267qi99h-RR_-sDj_hcCKIueUuXad-SE2lJoJ0tZz2gsTbTJQHTZPvcNTt2BWH4qPK_kTpJPNrhCjv--nasjMEA7b1OrnfiauvOuc1-EccNVUP_4BD_0DhwsUioxhVaY2q-49V-2usTue_5jtC4En0jqCWK24zrLQobS6Nih1HsI1A3Hdyzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
دیوید اورنشتین:
🔹
وینیسیوس جونیور برای موندن تو رئال مادرید 28 میلیون یورو درخواست کرده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102788" target="_blank">📅 18:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102787">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egvTtw2yOM4nTbuThfJrOBjCCDlxQsxWyq2eYw5dNotVfQokdGQNLQ-sfG7BU0cd8Xpc6YKkUlaGCYMrE9oHOraGqUo-r9TWTgy7isL_1cu6Wjz5WjNJyVilzSqK0FAUu8lYuXrXg9PAmkGrFt6dXb-OrSKIAKkYlo0u44EfyVQXRh-YXfNhKYmjygvf_NW3ezngWfR7Dy3_TK_4WIIYzD7UIKtgPQ0DUjTwJqPwnejq0yFNdVjaAAOJIy8cyIyz_vqghetUTGuX-g00mRqULF7labIuwqTLTYHpE1-QgM_OxvUZDTml6-_glf7-Fc4lu2Bg-ESwom2MEIg9IPiP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیس فیگو:
اینفانتینو همین الان باید کنار بره! رفتار او پست‌ترین، فریبکارانه‌ترین و خودخواهانه‌ترین رفتاریه که تا بحال دیدم، او برای خوشحال کردن رفقاش از هیچ کاری دریغ نمیکنه. ما باید شرافتمندانه زندگی کنیم و به یک قانون متعهد باشیم، فیفا هزاران مشکل داره، اما فقط یه راه‌ برای حلش وجود داره اونم رفتن اینفانتینوعه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102787" target="_blank">📅 18:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102786">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d841566422.mp4?token=iGRYpE74U1GLZil_UtLZnwMzV9XjpK4evGiBrIEcCkbeaMW_cSNbocDw5UYu8dSoHsMZqHpCYAHMos-YLK7HysYwPpKQDZ-YXFH8jFtWVtynhuXPoP3N7mIn-0pjpBITRG3-5VWGqhGJWK6245XOwSLJlkMdO01hs1NJYPiCrZQKHq5nXnbNOIVLtTIgn-Sx5Vo5Kn5F94RdD9U6037bhK-NFgpikQ578__c6_96TP0kcYMkR21shGrhgfPXgxCdzYg8pA_tCnZBmGOsiNbVTeR3BFIqstDXNcKbqtpcketc9GwXkjyj0QIyD8oQEM_QC4Ws3Mp4veXFzkGUYlgLBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d841566422.mp4?token=iGRYpE74U1GLZil_UtLZnwMzV9XjpK4evGiBrIEcCkbeaMW_cSNbocDw5UYu8dSoHsMZqHpCYAHMos-YLK7HysYwPpKQDZ-YXFH8jFtWVtynhuXPoP3N7mIn-0pjpBITRG3-5VWGqhGJWK6245XOwSLJlkMdO01hs1NJYPiCrZQKHq5nXnbNOIVLtTIgn-Sx5Vo5Kn5F94RdD9U6037bhK-NFgpikQ578__c6_96TP0kcYMkR21shGrhgfPXgxCdzYg8pA_tCnZBmGOsiNbVTeR3BFIqstDXNcKbqtpcketc9GwXkjyj0QIyD8oQEM_QC4Ws3Mp4veXFzkGUYlgLBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
سکانس‌های تاریخی ورزش ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102786" target="_blank">📅 18:05 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
