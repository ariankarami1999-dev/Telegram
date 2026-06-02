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
<img src="https://cdn4.telesco.pe/file/G1yguFHtk8vNXSAuAdBmBbfuaN7jTXYnxN1lwvANXL-S5CNCbPqvZOTisKlYgZ393raMwPFicou7xXIsj7CvFI6mDm2hhTAoUZ1A6uC_5IDl1cO-OfMkvKbkXo8Ztm8ei9WZEx39iAbfeVcNDXfKZGEVAk_SwfMSrz207YXNxbo7h91B3xAvxds7owsYdg2xU1cpFUIYyqVSmRrXyvAbKcmuA3d_CsgnoeS0LA5003FDDCevjRR3zu_t4wWWYTnkPpNV1oGaqjF1VI2qDv3XBDtHxJ3UeJLOX8ztiWaN06fK97qruLTjSty2Ku0Q3HISLEyNbh7Y_xD-9q6vJ11b5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 17:23:10</div>
<hr>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzvzQg1_t2hbOwZ8E7EaiomDRkRaPDZ04KwNq2whN0IfWA6xUzamD5XD3IGXfPuyfr6mQhy70-gAWJarEskaUpdlLr6Ch5v6aMKgIfFGCMj42oJIjp0N188y9jWuKPYor10CH0hTlXCWBhm38VxIKBqR8m3hyE4BOaJlnysMZPflzSSlmkYeAO7gYPkPwSguimGimPq7NST-GuIs-ZSf__xlgd2KrZVAu-vRnOhc4TYwbSXveBV0-jbppuA-m4I8BqunM89c6n9seNerh_cNL2FDDJQSAC7ccRu0-L5XJPx679vYWRWp7BbNEfw-a7do-ui4xtY7YAcTBlGy4Y3w-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aa1SUO_3erGCcGeODvn4X6O6Nn81h2Q_rsCh_Jvw7YwQ0ashMqAkztc1xj72AxFq4KbJlYzaOiRSj79amKdKk8Cj_iX2SmsY9x8H0QBXbb3b7q4qf4jTU23k31cDJy5W0a9vrV2yNSCWzwYWEki3DMMpOJqdqzgAKdWfCWO5Mn0b0ODDKc0e9qPfgdYw0Hy5WXUUggDFqOLB79KQONtiU7G-drjgqamt-KVKLzKv13H74vnaHeFvKHL90CKxf7PFdfg9g6xFynD96ZLchL_CaDOlnkEHtpiaE5kxixjHoSp8KkdoBD16GTE5vPMCECdaODE2SMYH1NW8v_IoTh_2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etJkcshiWs8rQ-v4V7DNLi15Au2s8gRTO0H8RhSch2JcFzBr0II7u0qw71xaAPTVChTndRR_ueX0zLdLYMso3l9T8nEdB9RiIMj4ekH0PurtxCSJBD5uprqfAUX3xZoJmG1Xx9vGfXoP1CBxCHoy8kfUWKhuK7ns8ccKvtRNYNsjN6Cha1kUuWqvSFatUo1shFBnxk7Vu8uH4GXKnpzTWR_tpqfADg1E4nFiqWUg_z9VHIQq0LL_OiUiSFtIAGFQr2O58rOQrdQMtg42ke7sxbXLrO_v1zxr1cN5Si4n-xX4hxOosQ5WvTp1lQn9P2wmkPOEnMOn347e8ppFoMP0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،
وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.
منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!
یعنی از زمان هخامنشینیان این بخش
یهودی نشین بود! و ربطی به اسرائیل به عنوان یک کشور جدید نداشت!
دولت اردن نه تنها همه یهودیان رو اخراج کرد
بلکه ۵۸ کنیسه یهودیان رو هم با گذاشتن مین
منفجر کرد! فقط و فقط «یک کنیسه» رو نابود نکرد
که البته غارتش کردن و فضای داخلی اش رو نابود کردن ولی دیوارهای ساختمان سالم ماند!
۲۰ سال بعدش چه اتفاقی افتاد؟؟</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWelbRb8XSFqxIrc_vTotVmbN2n4QPda70hcD3dfSHGMOYGKrSyYEzk_9Jws-Hz3Z8dTyNXMJZ0epkxcGZ2BUl5M7uoqV-faeL_O-7wh2WMxFP-dTIl9YGv-qE6BnqsaG4iIFsmxMMjAYTVzWAF07GsxNwiC30S1DzvF37kI2eDW6mS9ZHxErCltbSfdmQFlATje3UiNZQvuYDkPIKQYLWq25A4Zv2q0THv5Bq28Kng9z3KoXg1W_1NJC_oKPu_x2jjjPqAhbA3IHol0N6Was_JzGOIgPQgEvoGtvBmTR4PkZhdVzJUG-N1W0neNf1z2-LA_d13f6gTUVxkxUrD0fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GH68NWPUAfl87xVgUdOTn0HP4e7NotuhIylwY8d1A0BbSa0IHY_Nsuj-vgKIQsq9Gsuqrqt03zGKG-58XMXXePWVLuyRLpLH_K4Sv_WTZF40nRDOOMyf5YENUjmUXLw06f0XQo4yBz3xAseLiZtvhQcEhPjxmp4H0tNMTztUrwMLmO97_N4fj6kLAeD88A46uup82Cx_kXA_V7JulJg5MdOp9YRhsbMkVQ3gZF5tRdwCgq08oUqhB5vApteuwHLiNooIxCQ_AdFk4r9bxaZMW0F54bL31nfttuCg73K1kqy6vBk8TbJjb_KqK8eR951DLfGyLe6CJAOI3pn0qzLGiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJNChKs8UX-xwTz_nykgmipLJes__i3DWZqKtPaGjHicjYxD8SGlHekrG4AOHGSDZw2dwu6jkUBfTpaEzWRQ3goSKY0xQrAkSR5E77xtC-eLnkJlM85mLNYwsHIKh5Anab6mhU3L9OR4XO4C72HIrV3ZLFUgqw0WLc3kYVkCdQU9tL650gY4bepLFtMjmIiDpv81aKhozdAnT6-vWyvBAYKl7sMS1Aknub75YCHAW79ThPE7K-847a1Ut68QcJKFG0lfR3HMUQWfwHp1m5KqGqFrhM4xae5Kew_vttmavqZCLNbgkr6LgoCdyS-XldqrWrgvKxkXuhwy1c3v1-HZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITXA13_oTN4uV2FBVjfUB70-sG8QzriTPbq9LCSgZLFwYU0CfOZSuO99RiCi-KuFbITSgDKcgebqHaR8Ll8wrxloaZTQtvfAewGEQ6yLn5cz1O5Q_uZ_Ol2SBhyRN98JcSR1wttc01Q5LRWB9c2pDmx2nzWcHRO_PlE0GPBUis8rRi3f-CP2Xe6lzw0lx6og8TWqOE7d1HJTWP-dvEhJqa7iT3X_1wnIBAS8lXJx89v6I4W_PKA_hQZnrQSJDDMwRd8mL9SO4sHhFluTFBkDUNjveoFwDTfIAYBLHZ0fKUZQTYX5N5ISAsEAmmM6HuMInR_aTPXdwrzMVyjjLgNNYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=ui1YE3hFK3ltp9ixQdKAkoqUoAUGBFhIwe4hlAi9EK0mhQ6Ri0g-u5k2rP-FNmS2jVZRW2PjZe-icKoT5cxH-bI0cgaZoLflMAM0uH3n0kDyCl6EMdbMYdTWtusO_ONReYI_w08-7omhC_OVdLZfIRS0ehXJ4CbzcNmm3gQCdK5FIfbo3AzdLjAjzXx50w4USEbYkitR0K1F5vCyw1n-pcuVa5S5JS3BqrMra_5khTfNP3CqPlt4RD8RJ6OjNV_t5SV3WR7x-2Go3ZuslPgfnvd72e0LTpHd5YVzcTFEcU4TNZpeGiVCZSChtuaHgWj7T0Xb9G4tl75TYVlq90M0Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=ui1YE3hFK3ltp9ixQdKAkoqUoAUGBFhIwe4hlAi9EK0mhQ6Ri0g-u5k2rP-FNmS2jVZRW2PjZe-icKoT5cxH-bI0cgaZoLflMAM0uH3n0kDyCl6EMdbMYdTWtusO_ONReYI_w08-7omhC_OVdLZfIRS0ehXJ4CbzcNmm3gQCdK5FIfbo3AzdLjAjzXx50w4USEbYkitR0K1F5vCyw1n-pcuVa5S5JS3BqrMra_5khTfNP3CqPlt4RD8RJ6OjNV_t5SV3WR7x-2Go3ZuslPgfnvd72e0LTpHd5YVzcTFEcU4TNZpeGiVCZSChtuaHgWj7T0Xb9G4tl75TYVlq90M0Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5mSTAiHyMaE1tPBs1YQq3Bb9i9HqpRUS9WrC-DXUyBy8dAYmVw1z5hWcZvrel0TiUKf65b-CZemdVdg8mnDPk4YJfV8mamxaZFhKdMlZLbxhulyOdTB-RrTuB0zfhuUc7bDKtqd3JO6eU6cq3zeWpocFUhFV1VaaV7WHgciRoYp9uEDqaiMMuGciOl00WbeE64v3EOzB3aJAV4phy2nm0LV44hHwKEaVmXalXvJ033GWcMXAIAcZrds8BsMOVayrcX1xVfDcIWDwM27J4ItzjFzbR85bhIVt0pNSncZ8mdaRnYCGAo_oPB2dZoI0jCNVXuTp3q46dCeX1Se_Ow2IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OpDXtwlerrqaTW6TweJou17vaR-Y7JbhhRBc52SQKt6ja-BnRMNTYgq-GH0f77ICLA-gtxQNfTqHbRAZMoII25okY-gyMc0omQaJecdRNgc57hwCSUS1oFOl3CxitUQtHy4gN98jMBg31TnU51UzYD860PNJHOEwMCyiCV1bB2BSdG1GVIYyK8BgbmX_CA5g9H_TmLEZpZ8NrL7eYJsrkpBlR_EEFITSIvHEKcx0xE1Wa0NYx3HdRAWKYZCYyFUNangkeomruDGCjLbk1uSsX3mdINFynHZVOW_epm860ROxjcrE7GkxDt06PKYWXQ-aXinTjeKluA5SqGVaBvvi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UlSCLkafqLOGjA90ur_0xp8S3dpMoUlGeehJgAy-FlRStnfGTxXQ000D_G5zbkUePKkjY51TH7WEpMtGFP7XYOwpZBIPWkz6ifcST1FRnCUG9WAWrCVa7BQKHphzLdSVLX7SQLi7EEhbt6l4TPrrkr4AIxR849keuaAxc4Z8025K2eMQbNTUswxBEJD80cVhQOXfgv9D7HulQ-Aqy3D38c4h98wlIb9eyRZU7hUnS86l_IOu6a4GVyuI4iyxTA5gd_dy95xqM1JumqUWPYCydNLDYBmCOmIB0iEPwP-1BtCK2H4eMM3lGXTQqXxVbUJSiP5Vqv0F169LT421NV9kKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flmsoJJ9lkcp98hsmgYyz1Cq4iH-1gUuYD5eC1-GUdE7_3SvX9P6uLsK5SduEske3uPgzk0fK9Mj6WFhMABIjSiku098T8aKjQColm16Y7UyYwpOS0vwrb9wmgEpxFaECHGS_CfjdOZJyP5uyLPHjzybu9JbU4WRQ6lC2_2PMn1OG0ORP3AhJEVwpKlL35Kza0jMipXb2RddSbbMLpIVw5HS4o0792UhitYBHrgtBLbQU1jqOQtUOJSNLNuRO7GZAfUtFfs7vf_S65OKBLQpcDNqviu2MKRTrp1zGt6qio-MgzZ_a-lgpdKzZHFi1iNWFZdB-3JsNOaOjLPzd_OJcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1nyaWc_y_tHnytXZe9Xzxfneo6UDlI_VeZBZj42wnDYoVz4UpiPDLXwDqwickG9TfjpYR5vjfgMuSiMUuQBHcekoP41dW59-PnD4nEtaj6Mq4VQF6iOdW7T9785EyODkXtA4Xg7rFVaOLoYXEd8HU3a0F3Pm-X1fbp6ISjKobmZENjTT440azKiL2Hq5j6DOVHabI76HGWSyE7xlura2sU6SkVgb8jK7Ef8rMeW0KssSrI2T2ta3rsihD7SzH4gKrvXxkoy2NPxHq5h8MoFFaejWJRX8javc-mMpxniCl1DAmfI9fjniwY1b1fBCd8w-5WPUtJy1jyssom9NxIvWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XeXxdLrRNMz1usORlDK1iffYbnOKusK1UdrKaKSSacPSKONLcPP676WMgEG8feTQBh3FTTIab4vwfyeBeo4QBwnYlid9-ZrtSKPnIAaCBNd6cYLruyQ3TjvXrK_GE0j1Czdb03xhESpT22Covzbi3CQB1Y47o1jhP8TONk5-gXyB92E7GhqmVJqzpeB4e0wc5QaqYcYeJOl4s97nNZ_lYT8Cq3EKBg7pIfToAnb4-32o7-d4oV-ku1-PQM99_3xWdBHenbKQmsVgqVpPPbrROWxraP64sLY99yiQDEcwproE6AsQqrcLfVIkEgnV7qz-5yOr6lCrfGMg7PRtN9ZDOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhtJ2jYjj_8eiWbstmWo4cDW7WzZoXowYNP5dgg7P5DlDkEDOXVJ0O5M_XltkgtKihGV5pyMU0ATM21n1SybU8g6wz12OHHgMFs7ZqLqbOTwNbVXz7Mh_Tagd4-EP8Gh0Ruo4RtkgyAxuSUODOzw2TL3Q9LYY6TgTF1fPR4AIjWl6OUqcLW-aThKZpbR_NAvKPJR_VS3dvgsT2AZakmqVPBDyg_TDkz5aWSwCJkdnHkgcE8zVisriZ5DMvSfeEDdkHwwdMFLQQDjongX1-BvCVdsk53Lf--5pIW7T9aXRwe0IQZoIDsHCbBVsZdCNPikV_4jjgyxZe5xl1y_Tz7GEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l5ctTG4wQkKzMfWcMvAx5Alf5vkLuGNPFDf-UNYAnDrm_hRTBH1ftSdkah_-c_meAdamc59n96rd9qfu7r4_D06EFI7Gw_EBZkjOkugkdsx3ItsX0f4j51taWlj3uOuk4hrP9WeLXH9wZUObXy0mi6DpbYXp6S57LAcIMyCGmlL04CX-DtyJzUMiqHV7ASI31A3HHfVp4L7UM-KeMN2tK-_dEOwBwM8jnBuj7EJ-rw89e3J6vh95m-gZmnh9nGzfvAgiejmW_EFUDb29BK5sqQpfMvTTtQPdfQj_pubXnx06puYNQ8fqDPq1agzZnMHIbozTG4qnKhIfC1RaFHBnEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">و بعله! خامنه‌ای و پسرهاش
خیلی ساده زیست «بودن»!
فقط در زمان رهبری خامنه‌ای، برای خمینی مقبره‌ای ساخته شد که هیچ کدام
از اهرام فرعون‌های مصر،
حتی فرعون‌های مصر!
به این  هزینه و گرانبهایی ساخته نبودن و نیستن!
این فقط و فقط «یک قلم»! از ولخرجی
اینها از اموال ملت ایران بود!
در کشوری که هزاران مدرسه‌اش توالت نداره!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=k5XMzNxXoKxL5FjSE1ku02JvcZF9GXOO3EukrVWV_7z0qxK-zgbMrGAQuw242-7S6-YbnPE9aU_wKEu6JbWFxP2CHZER6xoincWc6t2hyWN5G-NDNxEH4GAaSiMhI78DDGcwpYhf2zQ0evVX-9_ss-g9PTSe0--Hi1T-81DXCKnd4XhsKnr6CKv-avhga3BQr3r5V0ZCuXYwrPc73Qh8JKOPK9S151A0M7lhyzO72QeaRKCjch1j-vDAHwZ2AboUqPTuDBA4M7wRAsID2HFvMWo_3sHd7bb3a7q-ZkYYzfG-W9lqc7PP_CY6EUIuKAohOJibVPCggfHIqqxd1hIdog7QAeGtqn_rPH6_qXwl1_b38hq3jceC94Ys2DIr6W5vQCb00xiBX6LKNnVEox6z4XY8Qn4w4CUUCcSxfD1hGhNjEtlJFWO0cKs_bZfdEAOg9GdFgI3nPIB0cfnq5M3JVcI4ZHXTe2YDPpoSZ-xw06rFDxC9ltFz48pbu6G6NDbRCGeLSuw7YqCcvsAxuW0YrEnflsW62Lq_0fPXMSaEZRUBY8ses6Q2sk2dr3Pe57ODjSyyqCgobWYJFuDV8nq0wOilRgKA_i5u0i_mv4k1knr9RodhKxnhT0rLGgW2oSMQSiy_rYBlhF6WKSMDITHe-6WykEUTqRYbd-KYVzsKpWk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=k5XMzNxXoKxL5FjSE1ku02JvcZF9GXOO3EukrVWV_7z0qxK-zgbMrGAQuw242-7S6-YbnPE9aU_wKEu6JbWFxP2CHZER6xoincWc6t2hyWN5G-NDNxEH4GAaSiMhI78DDGcwpYhf2zQ0evVX-9_ss-g9PTSe0--Hi1T-81DXCKnd4XhsKnr6CKv-avhga3BQr3r5V0ZCuXYwrPc73Qh8JKOPK9S151A0M7lhyzO72QeaRKCjch1j-vDAHwZ2AboUqPTuDBA4M7wRAsID2HFvMWo_3sHd7bb3a7q-ZkYYzfG-W9lqc7PP_CY6EUIuKAohOJibVPCggfHIqqxd1hIdog7QAeGtqn_rPH6_qXwl1_b38hq3jceC94Ys2DIr6W5vQCb00xiBX6LKNnVEox6z4XY8Qn4w4CUUCcSxfD1hGhNjEtlJFWO0cKs_bZfdEAOg9GdFgI3nPIB0cfnq5M3JVcI4ZHXTe2YDPpoSZ-xw06rFDxC9ltFz48pbu6G6NDbRCGeLSuw7YqCcvsAxuW0YrEnflsW62Lq_0fPXMSaEZRUBY8ses6Q2sk2dr3Pe57ODjSyyqCgobWYJFuDV8nq0wOilRgKA_i5u0i_mv4k1knr9RodhKxnhT0rLGgW2oSMQSiy_rYBlhF6WKSMDITHe-6WykEUTqRYbd-KYVzsKpWk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=oTC67vHCJiJkXI5KKYB8O9S5m2pSCVJ-_DmJdEjzg1cRz3VBbGJ_GaGZXVCa1zHAi72SrE9e2hsiK6HgmhogScQDZO7EYgryS7jZnUg0No0skL644ZTF8E9D8-X-AUVBwOgp2msRe0ojS8Y_vbiasLihLNWWJgSpU4GwYVpIfFgqwRD7GSumAYVY6OJBs6tuhm81W-XKm9IgqdjmRwNeK_4e8vcJeIWRJ6UkY8TbRqNW37xzaPR1rehpwrRXbMOaoWAlEBR4Q497ZSWtW8IrBRoH4oieh6yz3-48JTTttC_CuoEw1n7YBxDv11x2ykca-lHEK2BioOFvYUdY-iX4zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=oTC67vHCJiJkXI5KKYB8O9S5m2pSCVJ-_DmJdEjzg1cRz3VBbGJ_GaGZXVCa1zHAi72SrE9e2hsiK6HgmhogScQDZO7EYgryS7jZnUg0No0skL644ZTF8E9D8-X-AUVBwOgp2msRe0ojS8Y_vbiasLihLNWWJgSpU4GwYVpIfFgqwRD7GSumAYVY6OJBs6tuhm81W-XKm9IgqdjmRwNeK_4e8vcJeIWRJ6UkY8TbRqNW37xzaPR1rehpwrRXbMOaoWAlEBR4Q497ZSWtW8IrBRoH4oieh6yz3-48JTTttC_CuoEw1n7YBxDv11x2ykca-lHEK2BioOFvYUdY-iX4zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoQwPKY0GMayoDIB_z3m4ikzgkkesTNaNYW5Ai442AgqpMSkyVkUctP89CkXBa62psNw6h3J51bWkj6QkiVUCToli0flnp3F1uVyyDRImwTr7WSu5RuykDVui72yGrPLeM_B3IbOdvzFXr-o0Z8sHe_wZ62PGx4Hxwpg7bvviGnKDoFKMtARqRQPeFsqls1lafUr6-cYl4szGWmosE4eB7xeCNrGatHGDe6hD2uuG4kgW-2vP_APiWszUt2yh3Id8i-s23wTl4mn4qiUAHNk0rWNndgXtnDjTM-22eTsk93AFsemhiw33FZo3Sa-mx0a9lPxbb2NdSuHaBnbrQeOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف گفته که اگر حملات اسرائیل
به لبنان ادامه پیدا کنه، در مقابل
اسرائیل خواهند ایستاد
‌ و «زنده باد دفاع از سرزمین مادری»!!
میخوان وارد جنگ بشن
برای دفاع از سرزمین مادری!
حزب‌الله برای چی وارد جنگ با اسرائیل شد؟
برای خونخواهی خامنه‌ای! که
هیچ ربطی به لبنان و سرزمین لبنان نداشت!
اینها فقط برای فرقه خودشون میجنگن!
نه ایران و نه لبنان!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بیانیه سفارت لبنان در واشنگتن در خصوص توافق
بر
سر
آتش‌بس
متقابل
:
حزب‌الله با پیشنهاد آمریکا برای توقف متقابل حملات موافقت کرده است؛ به این صورت که حملات اسرائیل به ضاحیه بیروت متوقف شود و در مقابل، حزب‌الله نیز حمله‌ای علیه اسرائیل انجام ندهد.
اسرائیل به ضاحیه در بیروت حمله نکنه
حزب‌الله به اسرائیل!
یعنی : اسرائیل می‌تونه به حملاتش در جنوب لبنان ادامه بده، اما حزب‌الله نمی‌تونه به اسرائیل حمله کنه !</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
ترامپ :
«من تماس بسیار سازنده‌ای با نتانیاهو داشتم.  هیچ نیروی نظامی به بیروت اعزام نخواهد شد و تمام نیروهایی که در راه بودند، همین حالا بازگردانده شده‌اند. همچنین، از طریق نمایندگان عالی‌رتبه، تماس بسیار خوبی با حزب‌الله داشتم و آن‌ها موافقت کردند که تمام تیراندازی‌ها متوقف شود؛ یعنی نه اسرائیل به آن‌ها حمله خواهد کرد و نه آن‌ها به اسرائیل حمله می‌کنند.»
🔺
ادعاهای ترامپ شبیه برخی ادعاهاش در خصوص ایرانه.
اساسا اسرائیل قصدی برای ارسال نیرو به بیروت نداشت! بلکه نیروهاش در جنوب لبنان هستن!
🔺
دوم : بر اساس قرارداد آتش‌بس اسرائیل قرار بود که به بیروت حمله نکنه! ولی داره حمله میکنه
و در نوشته ترامپ هم اشاره نشده
به حملات هوایی اسرائیل به بیروت!
گفته : نیروی زمینی به سمت بیروت نره و برگشت کرده و…!
گویی ترامپ دست اسرائیل رو باز کرده که به‌ حملات هوایی‌اش به بیروت ادامه بده و به پیشروی‌اش در جنوب لبنان ادامه بده.
همزمان گفته بله من مانع شدن‌ نیروی زمینی ارتش اسرائیل به بیروت بره!
🔺
سوم:  ترامپ گفته با نماینده های حزب‌الله در تماس بوده و… عجیبه! بعیده!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rY6JpDty7VUJFIOLmL0KcT2Vh0n9fUgHLP7gPrln1K4lGVPDV77EnITuUx1CafRdHspILuRiRac5EI15azQlXuBYVEB9wVViqEhE8s4agXFdAD1QEDCXIC_0dVUoMVivT3ROvgDVn4koq-AX0-1CFpHNoPpxos2yhOGaWiev0Tx7b7zYZk7m2oajd9s-uuIWKcqWfjUFJOUP1Sbcj05tuHnRMn2Gno-VPP3D3nZJgcybj5BFPwjIv9cBt5IoxXFW3q8DVeRaMNaK2s4cdVM1elYin4xBN5cytZd05qYJ5Hqo98q--4YI4N-DoWXpq15aHGNNWDEu-J9J98rKwnHJow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSOpFFn6a2Mw0Mm8fZgXelhAqahlFxDk_e3LcF3kg0e4ooVEkEGFHfiJ-MRzqntObyotXxSDMV7p2Iz6iYD_PNhLnf4p9N16R-GaJozm_Xiyu3tX85zDBlnQEnS-rk2OQvY_pN9Q3sPxvEYXnFwIt7LPUKN2bb8bepMoD0SOAmoD8YsRPVHOeSWLuTeBKknzQtUhcsyWfYwbUYmMvgmhP3QDi1b1QoC2-X6VPM92cJWO1xtsSxG37oXv7nRz3mqfX5E33hEbcX4Wf63UMJ47TtrLP-SSmM3z_oCY8xnjRORu2oPhdywZFVgx-9is9YIirhQ9CVTDy0kIhr76oC6gXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8rf1hCzDHO237d2K3Gg-uAyFIVzd82QrsySSgFl_QJ7rUsyzsQVwm2ZeT0MLt7tPufsV7-I-A3EJHUxyiDThBQsFBmxSL-vy5XQmmRG46IAGJ82vFaj2BntkF9w2DbNZ_T8w2U8odxC9RQy6Qs8S4IWRrrIb850L0flNNs23sSmv3ZZjhSrq80pOQt-40lDj8Rr8rcT_CfnMHo_16QuN-4MWNT5fskt0C-0qzbBQMFyOIVqtmiu6G2cacrm-SyymbIm1-lCeFZylRe2i9mAjamGYVdLPSBFP4M-m69sH5h5HJQaNRy12fE3GuI1v4Qn91xWqiMFWX56S8A07miGxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsG8zgvVptbneeqHSokSL7QfGU5opxujn_tBK8OS34g67LRR-7w1pJiJ3mMNSOpOgJvm649Kt1qCQrSavsYKy-QkuDG6WjeLo4F0LgzIM0BK49SI5AhiecTo1B2Bb9WfEUdxNMi6CExXpVfixVXQLWRdZIfiNvQV8KQt9gaeaz0at2VULhiJHMHqGSfpt4mmlwSixE0fBls0in-009kGuItXUJK6HtR6l1KZQFuBHVHz4YN6pRaK9oQmqJDp9B4Anxbr7CkyIM_Di87zs3OxwZTID9LH4fJhlfgN31anyNp3or_NAB0jmCjKIEAzKq-V8z6NDq8LeAWDwq-rMDhETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_RBKoSFkUIpH8l85VrYr2y-ilFthVxPo1lcls59yul7ArlIGNuPv65zDsm-d7LEFhotzI_pvdmnqmZSkBo483PK_OsKgacFRZG_NRq-kKzF2BSl-4kQcxCjpCQZzY6HdBnLW_MbegnMuTsNUS2LLt5aYmIjIChlHhYRzyJPz_ocV55-2g3b7GsgVK4DGM9YAcwWcOjSj7xNv8gIkAOju-IqlfTzlTR6vdnkZv0AGvaU3ZOfQr-u4dKabSz7hwSNUTbDtTOw3hSUIRoQViYaBITFZrZsRhRR5YCQZLiwA93TCm-r_Zkf6MaGuE8gkioBhEX0P6xcXX2SvVgiYBfsMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4bMmFwIpswNo6VQLb207bpBvX7FhauNdvaOLODRhLDw_dND9HsHXd8r63hxDoprZriEQ9E7_IZbQEL0WhIss4mfkU-vaGdmvBP059TLNDRvVMgphYZGYaypdubmXauAdYRtnxLYkAr3C9A3u6nCDNyxhV_6fJ-Z8KnRNxsqvlnaKSzx4FYbyRog8StUQk7pj5znJXaMYNJZ_ngsxGElSliPLAs6AmSZcn5f1Qoty3i3O_fFePsastS8SqLCgo3iCsDQ0qQjd7RmwfGYyKJqyWFRtIaas9bC4ZWym8y1WESI29NiwguOGZ7JmqjxzXI7ooIZb9FZwuINfcCpsbI55A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rk-SlwCR1FEaHkn1yqIekU2tlxC25LfGEJS_dQuMMi6dd_adNC85GdaQVGwFBJAPgWxeY2CJCpOgRvaBbDveKOPU7ODRzWqPRuVHqBvU30AT1LvNEEecibIESruassjajuJKdg2cyoeWk8kZ7Tz4KeGXkzcJsGUhLrx91wTbk_tuebjGP-cVaIAFOw-QO5zy-T0P71St64w-NL_YrWVevL5S6QI95G5VcOB2ICxC10IHf3R4KKZfEcLGHjnncFDuIEBwak9AwuWUmRe-LRrR6CsrikkddaJCjxvddd-VqCTOaLiLHxWd7kJgAQiSX7v0fID9Oyt1YDUnRp0DBqzQeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WN1hvYsQJyn5UWMjylSchOLxvPWf-zUPKs7Uk9RZ7AGbEY-pNxaXR5KCBDUL-KK_9Tuidoh0e8Ksr5MzulvtiUsGSd2Hsv5JVw_smTpWngEryIeujRcfD6BQ40gVg4JufYqdQJwe_XTlApjwBph5h-Gv5rwNTOoi-KHu-Hs2NkOklEgyIusmbADYbkIDdXyJUxjzOsvVcR_LlVQC68rJD8fD5ttYKk5Ne63D62ptd-jcU7B6xHbEmYRnLJb-Qtqe-4hSd9sWzRlYtI8wPpkCvB2X_sn4J8UwMsXP4C8IANV_2Arcg0AZvepgIk5s5F7vgkUPfmnTbzQvnuKh5LWGJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=jkc775KoqJLBIfVs_dEBeWWIR8JAukiWFWBpLg2xgf8gHHAnvMES5s1L4MxhGXKRLnwM5ob3otGf2Sv7cx4MtjuqgxCZIs-8cKDHcn-KJGgBBji-6INYzyQmbVugrUvaZJQ3hF1b_4ioq9OsI0BnLCpS5SfUQTriyw6qNm6NSGoQUYYD0qdP0BTaI9JgoC4fsBauIOU25imvfyenWDN8meDclDgxyYUpLZ7NjRAnFC9MtnD5revIDDjM_AzADSvnTLiO_h1B6ZWuZ4op0qJbVYrY4q5T8YJC1CUo8g2-PwDqnT8VByC9PeSEt2fuYGik1p1r89zY7JdNhiffqzETEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=jkc775KoqJLBIfVs_dEBeWWIR8JAukiWFWBpLg2xgf8gHHAnvMES5s1L4MxhGXKRLnwM5ob3otGf2Sv7cx4MtjuqgxCZIs-8cKDHcn-KJGgBBji-6INYzyQmbVugrUvaZJQ3hF1b_4ioq9OsI0BnLCpS5SfUQTriyw6qNm6NSGoQUYYD0qdP0BTaI9JgoC4fsBauIOU25imvfyenWDN8meDclDgxyYUpLZ7NjRAnFC9MtnD5revIDDjM_AzADSvnTLiO_h1B6ZWuZ4op0qJbVYrY4q5T8YJC1CUo8g2-PwDqnT8VByC9PeSEt2fuYGik1p1r89zY7JdNhiffqzETEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blhNHlVLLHXPsYYrwbwfUwi82O2cHpjZASFwN23w0BXY2MIw9lJV258yPDHbEgRJ33s7dlqBpPotaj1RCnX5ygC8ty-Ty8YscDEpeUnAVuWcVq2SZwVwKRaG2fl18Nw8CsZBpzcz9308JCYalAFO8nY72RkOfuEvidG8ARAxMe4MIjj-DEF0nPy1mzEV1bfS4JAnWqAx6OoP09duzj3UIKZJa65XxLwTkyT18nzkVGBW_vOq-h2wufB9tNBuLl2nPz3LkYMgCloyCOOnMxnaJ8jK3WdNAXcj9EPYzLvcBnG1C2LH-fhwetEBWbiGEIuWDxfuY-Z8njPRQHzCM9smcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=QFRPbiFlpVav9FM-a_zHf1QyPwrpuV-krdpGuPsxGcbOjDIHpUoxzOJhRBCyb0MEsEF6zh0sXL4kjeeKexsZyOoVYqQ0EwKt5PEO_N7GUpEWWuq16x0GJfKVFL3s0wNp1zRR9qjGS-eHCUl5x0i2wXdZa6pYaf3PW1zkkx-ppuxWWunPJ3cWxNeaiPMaRcR4KFqH0PkckMjq_2hkK-I2FT5qUOMZNOYjsR3ZQygpVGwC1zKTqit1yXCTy5MaXFoEzRjqDPY5ZQvONnMvgraD6ntR11wqF1AA5QKbz6f-2-jMDF3371jwqZnkbh3VOt5uPdX_KSj7GKcrtPvy0t-2Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=QFRPbiFlpVav9FM-a_zHf1QyPwrpuV-krdpGuPsxGcbOjDIHpUoxzOJhRBCyb0MEsEF6zh0sXL4kjeeKexsZyOoVYqQ0EwKt5PEO_N7GUpEWWuq16x0GJfKVFL3s0wNp1zRR9qjGS-eHCUl5x0i2wXdZa6pYaf3PW1zkkx-ppuxWWunPJ3cWxNeaiPMaRcR4KFqH0PkckMjq_2hkK-I2FT5qUOMZNOYjsR3ZQygpVGwC1zKTqit1yXCTy5MaXFoEzRjqDPY5ZQvONnMvgraD6ntR11wqF1AA5QKbz6f-2-jMDF3371jwqZnkbh3VOt5uPdX_KSj7GKcrtPvy0t-2Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=PzR6pydxhggl_NO8kmtSShGa8SEbQAI8JI-DigOGiUjZdk-buXSjV2CF8UVxfzSa6dXROsbfI9q_tqp9Sml87O6YjD5W0IAfr5iVQHjThzZggWdz3LZ-BRVfLEYrqJlRnjY9Y9e2RR3xyWCwNqzdNWWW_g0Vtsls9ZsEzG1zopnAXwLMtH2fBskVvo1kp25Mvgld3R2VWWslMzVZ9eb2EDu_S4PPVnSaX34QGdnKXfzh9yubYMZhCgWZ0eEMUIjyQqBk8z8YXTLCjjWTx2leW_x3qajMKAvhhsjDPVpRLO5fQT7FJnyWByp-pFncJDeqEwpJAgogVgGxchzCZDRkbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=PzR6pydxhggl_NO8kmtSShGa8SEbQAI8JI-DigOGiUjZdk-buXSjV2CF8UVxfzSa6dXROsbfI9q_tqp9Sml87O6YjD5W0IAfr5iVQHjThzZggWdz3LZ-BRVfLEYrqJlRnjY9Y9e2RR3xyWCwNqzdNWWW_g0Vtsls9ZsEzG1zopnAXwLMtH2fBskVvo1kp25Mvgld3R2VWWslMzVZ9eb2EDu_S4PPVnSaX34QGdnKXfzh9yubYMZhCgWZ0eEMUIjyQqBk8z8YXTLCjjWTx2leW_x3qajMKAvhhsjDPVpRLO5fQT7FJnyWByp-pFncJDeqEwpJAgogVgGxchzCZDRkbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QibT7s5nhcNC_W3k-eVFvJOtPRrskBC-5c8ZpDP6srzfqQeu51q_zjpQcGjZLqhJyItLlpl2JGgB4wI_PkJu5GVVMLPdtI_tBBnt9QHlAr_gTRfvANx5_CQY9Pi_gwtojO9yZbqiJcmfnKOa-jgyShhSYeEYfgmkjOg6rVXXtQlVZ9AxVoYz7O-izLIN2ZmlzFGl6gK10oYltr1SFUpraVUMBGByfXx_Z0jGNMoy08N7wKm-W7JO1nvYvHTSnNE249U1PIyFAGnkhpGV93fJc_B6_7DPXq6eO2tM1gtPGIulcl05zovSzkmgGyhJ1-HDAM6jG39oHYFWm83BVXvrCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=l2uHFczX1DclaOjZu-kdW45o05fpZm4EqVQ5yM5qdaEo4oeIY-timlBLPFqG6EMVZmHMqwzhjXbkiqMIfRYVLzFvPMShX8JS2ezcncQqSnm-Sc8nI-NpolzUmHpzjc_Qt_i4VZ5iM7CHMhj9dbpz0NVxQ4Hz3YTUbr0vCPsMlg0T1__NPLxmN2fzWzByS6kt170DLKiKENYQiGcYpr5IPDjBKT4N_WbR51clsyK0ryFpqwNEXNc692i_szYsNL7w-kNKWQKDBgPnXgSf5GvJi4Y4RUFaaIbwkvkUZPI9KC-_cLIF_9LYrb_GAjlN5RetTCWio3g_NeXhg0v_CxnDfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=l2uHFczX1DclaOjZu-kdW45o05fpZm4EqVQ5yM5qdaEo4oeIY-timlBLPFqG6EMVZmHMqwzhjXbkiqMIfRYVLzFvPMShX8JS2ezcncQqSnm-Sc8nI-NpolzUmHpzjc_Qt_i4VZ5iM7CHMhj9dbpz0NVxQ4Hz3YTUbr0vCPsMlg0T1__NPLxmN2fzWzByS6kt170DLKiKENYQiGcYpr5IPDjBKT4N_WbR51clsyK0ryFpqwNEXNc692i_szYsNL7w-kNKWQKDBgPnXgSf5GvJi4Y4RUFaaIbwkvkUZPI9KC-_cLIF_9LYrb_GAjlN5RetTCWio3g_NeXhg0v_CxnDfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.
به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.،
مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!
یا شهر‌ نجف!
برخی از شهرها را اساسا به صورت شهرهای پادگانی عربی در وسط مناطق فارسی زبان و ایرانی ساختند،
پادگان شهرهایی چون : بصره و کوفه!
در قم اینقدر عرب ساکن کردند (از قبایل یمنی اشعری و از کوفه)  که برای چند قرن یک شهر با هویت عربی بود!
اصفهان اغلب یهودی بودند، یک شهر تجاری، عربها حتی بهش میگفتن دارالیهود
عربها شهر «جی» رو کنارش ساختند و اعراب رو ساکن اون کردن. تا نیمی از منطقه شهری اصفهان عرب باشه.
نیمی از قزوین، محلات عربی بود.
این حجم از استقرار قبایل عرب در قم، مرو، قزوین، اصفهان و… اغلب به خاطر قیام مردم در این شهرها علیه حکومت عربها و مسلمین بود. قیام های قم بسیار معروفه، اما اینقدر عرب ساکن قم کردند. که شهر برای قرن‌ها هویت عربی گرفت!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6sMdjTsNvb4WyGGQ_EYy7BrlYA4RcFs1-_GS2iTmewMR_0n8Dt87H0stltsLnitCkHRA-dLMrZ_6CfXk4Gw_IEsK3S2n1wFsZuCh-K0iST6yXKhSc8t9EF72M-0Im6I8lppQ71AV9Ilf6-7ncYfYkV9_13BRtkI6TVLH5e-IPDzNjZ0grrbacGlNfLDi7AdDW115nsl920NL1bLaRIRVfXADq5KG7pBOT6SMpOSasu7sT3La8CIu_UxaplW1IEGZ-Ol-F4kqOw_fGKjeoGEm5_2kucYYWHsjVRlAdUUCCOzzQdJEEQiuvNEfiqlw06o9mkD33bKKP73VXkm58r0zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtAcAMbVK_sQoBxDbq3HxuOzvsRVrb_5XVUwSEXu2Q1rsADyGox--tA2ERVTxT89ef0PFcWJP4p_gNB0aaSisasVFYkmne74tAV9U2jCa4QiXuLn3cPlJNcFL1ROpLoAYrM6kvH2ZgDMgorxwgMiU-h2dXLEXxlOGVBOBrxmIIFg08THCIqUa-xWG7xRZmD1GAis0YYsEW3vxOgHL5RcIQQV8Pjo2gcR2i8yihoJjbP0iWrvrMQqMkU9XJDH5EYtEuonotutoEhiJWeHF0o48BAIMqAkpBUDW5kUEdewQRjazTpS82DlW6Xoc67tK-q7xrT7ksLbFCIUytEMzFDQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QBj64NQSvNAqRLfRmsISjWM_hpO5Hbp0Xg4PkbFCu5sJPOdp2SW6BLqwP_a6eTc1jsLgcv9sbsWd15lPKz8UbpsxDFNPK0pgMPFl93Wxh1BS4RJdWhEB3I8euzccxtLJ55rqF4X4eiJD9vlaSlEfj7bZs58P2XM3tHoNiwXsMFxXVZbrCowEKWXCeDKySN65pzRYVWMcZB64ugpdyvYx88JUfWX7VtFvuhLs5W8F996JZfaSrLxkmPVSXtLRyJEc4lbPY8a7JIGQXjwwszOwBTBqI3SYuNA4fFJ3XIvvYzw-Ndsjlnn6yDNke_W9i_oiJmFvkx5TEUgCkE6Nft5m_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQc2xeqIPyZfdHT-4zgo88wVynjKOwAKtGo0nRc2CCSc7wSuidtLMnlicMABrMq0lPlUCasCnFvjtAGmmb7GykicBWQjOkBk_DyJ8W_3K8dJ93k92_cjhuts_ERV1bw9BZ2y0KXfMmrcswHkGGRAXGYIYiWExH6D2mNjQjLDuE7kKOx6yV4P87E7Y9Dwy8uPT-eNrlBe-U2u5uB3Jn5r4P2wh87zFY7ueV7WDlkhYN1pU3DEdZi-U97hURLo38N8nVtLcRnsbmXYGJIDjvczS8PyrPfmIxk98PGKPfKxx1ZjD4v_mvqbHZyKEwpR7RstDdUQ6vBoWE1GE1z7AIk_sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShjWkN56QFWOysiQ4Onf9PhF3fOnjTui_SSEGLR6LzioWwzffAuLi3b4EGd_pU9uR60NEQ_8cJmsDlNRIOTr1YQ1Tz6H4kD2toLrotZf3HILfl5SW8QP6JDd1ykzwP6Ur3FQk9mbgeWukqLgJdusE9q-BZjNjdPBU5FFxiBS0uxLsJ5a2peZS5lAHdw050zaXGk_uZiIwmMgCCQ-MXtTSuQdtSr5AQkQKR3dtmiU8Hx6U57ib_2WZQJpqXB0oUxgR51F98fT_CUtM-V8XksiQWuIMYfXJPPE8W8nHj-ui8BFl_n5xVUn0nSGEeP8ROay2-udHEYA5qXBJi6iOJYV2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kpjm0z34QAcPQdKH7Gr_9ptnHtTETseCzZt2AxFvH8p64HvNBOW6OP4sEHkGtEAf-bjDJ0f4uAkGFVs871HxbVjRvbN5f9Lbb_a5iwzzcM_vntqOF501w4nFpceqhUV84rSTX2l1qYIxPN06vzpa1WHKU4giBSH57Az-zc0RSkB-Crd89FuUSFVGGWAijo61hbnVTlJsvy-3MPzoqsXryhj5xWof88epz-EUDQo-VCAUp-Lem41-fOfZ-csRF-dqo1LXU_RuTA4nMXNWbaAxtdlHwXMvhN_TfpLVbqCydqoB641pP1ueBjUCq4XASCZpipi_DPK0zQuDX2pvu_qQzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzuJOD5WNTJU1D8I4dhoARGRCsLDkbl-HexdviHxzJA-5rI7xsj2QI7B0a6XGwfxYs6HgUd1UT-vieg_rYzxM8ADJT5jhP5i42ZyhbyPZKC0xDvI9chqR2z2w48twc-N_F9JLkTUa_Uz0uE7xlKt_6OAZCfLoQ9StQMFBTCUgQ7qDpVTO00o5o8lWzyFFYKFPKyRJtoiVU1VXa0IBw2nS1CC8GV_FfLWf1GGXdrLPQuXKWRTMwkBIdRplhc32pVdeEghqpSOb02HJQsuxJeiySTjwAIcBr7ezFzTvNCb8UbDoSz8dME0LRnp7rKP1VdMEEU5iyAM--yhmMNKBzmoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mdBWQECi3AevtCb8G-Z9Mi2iMu6maAisYQmxj66AXoyp40qVFmqhGsQ2EGC-Sfxfx_LC0JpIDqDg0Jw0YCcXo3Oz32Xn9EztcPiv6jBfUsKm94fq3bTQ8YKocKMcWyokV8yTkdjYcHNAVlE63KGmXWapShHXyu8rs_2tWfMK2Zh2c4EVdF7wSIGzS79bhxRAgQQ7E1nwv0gt3aD22AoziKkig_qtUfXpR3q5le55Ss_rpg-WetihSnmHMHCT3UCTWlrqZgx4TLX0ViBNIYBLwGdIr83dr7CXlOB6bzDCT92KhQFwZmfRVvqsYqv4kbmE1auDwV2OPzGCUh0DUl2gCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=q8H_xReaddRdiBbBoNwQEnxU5RSDYopnfwwGko28osZu1eybzwrGDdv4shywONWRw_0GadXXgFK34kxjMdQm4PsCzMN1aX-5L46cCvg0dOfEe-xUYIs0Kr3DDdWbSF_1XSQOxaHKf6U1y9mlyh71ETtLlWqpxhpCfyvk7G6_LBaZCaL2wx9el4I529q_gFzaR2HC6pxwEI3GTJOaRxWu9JT_9IbpO0bFbcanAsKflfBaFLhNSWEm6VC4UCVI7U_He6Gc2g6EAEmIMHQIoTk8IY9A59-xXgwHNHAonja_xnEiU2Aa0QxBAkqM_W9BCilNFoqOU5sG49RQLEabXuNecw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=q8H_xReaddRdiBbBoNwQEnxU5RSDYopnfwwGko28osZu1eybzwrGDdv4shywONWRw_0GadXXgFK34kxjMdQm4PsCzMN1aX-5L46cCvg0dOfEe-xUYIs0Kr3DDdWbSF_1XSQOxaHKf6U1y9mlyh71ETtLlWqpxhpCfyvk7G6_LBaZCaL2wx9el4I529q_gFzaR2HC6pxwEI3GTJOaRxWu9JT_9IbpO0bFbcanAsKflfBaFLhNSWEm6VC4UCVI7U_He6Gc2g6EAEmIMHQIoTk8IY9A59-xXgwHNHAonja_xnEiU2Aa0QxBAkqM_W9BCilNFoqOU5sG49RQLEabXuNecw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=oKSus2miIb8iXsiIvtLWFOCYaLyy28OdwLG74u-nkSkH-CVUSaBzS5_1EpmYz4XEP4Q3AY2raNbNkBJDkylCwSRw3dPsmt6_sy639-whigjp_p_evcf16y4-Q3RXTKAvkdSyafKwIDQzNJj7LPXIM2GVWevmthW1cJlItWreBoPsO1dHbJV8xD6fq9aK4w1reE5x2OoT_sKGAgufMpEB0d8YGUKU8_EicV84zF2HPO5a7fQz_3JPG3tUg0_cbaYvBcG9gm1AUvJETyrgq1763mhrIKwheVHGG3mK-PUi3Ccds_TB7oo94ToRjCHQdH47mEG1oysfe30gq9qgDWYVfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=oKSus2miIb8iXsiIvtLWFOCYaLyy28OdwLG74u-nkSkH-CVUSaBzS5_1EpmYz4XEP4Q3AY2raNbNkBJDkylCwSRw3dPsmt6_sy639-whigjp_p_evcf16y4-Q3RXTKAvkdSyafKwIDQzNJj7LPXIM2GVWevmthW1cJlItWreBoPsO1dHbJV8xD6fq9aK4w1reE5x2OoT_sKGAgufMpEB0d8YGUKU8_EicV84zF2HPO5a7fQz_3JPG3tUg0_cbaYvBcG9gm1AUvJETyrgq1763mhrIKwheVHGG3mK-PUi3Ccds_TB7oo94ToRjCHQdH47mEG1oysfe30gq9qgDWYVfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=UKqoZmD3uv38jFjBEy_50pDeG-ZlgLXI8zZESd25aAnUos63cyB0tfhNptFict8P6qVoDXuC79HaO89sk1J8g3_1O0sYTPWiVVsZ-28zlorvm7Yfq9xddeAYv9762VRiA46akoYM5EwWMD_VqC3YkOH6xtmbt9EQ3VnWccOPfzXPWCSgyeth1OwPuPkjl_nS1GMTq0uZ9cVGX91GAFO6VZjiY9pWSDeJWxVqA2hb0hfHzIiSDhZ30EJEnfxxOMaylQdQVU5ZqidVgeztaniskXnuCSxsd3JXTW9PEyX2c7MmAERIe12Q1GqeI6UWdgUDazGZXUV_832jYf5Stg_yig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=UKqoZmD3uv38jFjBEy_50pDeG-ZlgLXI8zZESd25aAnUos63cyB0tfhNptFict8P6qVoDXuC79HaO89sk1J8g3_1O0sYTPWiVVsZ-28zlorvm7Yfq9xddeAYv9762VRiA46akoYM5EwWMD_VqC3YkOH6xtmbt9EQ3VnWccOPfzXPWCSgyeth1OwPuPkjl_nS1GMTq0uZ9cVGX91GAFO6VZjiY9pWSDeJWxVqA2hb0hfHzIiSDhZ30EJEnfxxOMaylQdQVU5ZqidVgeztaniskXnuCSxsd3JXTW9PEyX2c7MmAERIe12Q1GqeI6UWdgUDazGZXUV_832jYf5Stg_yig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idIC7zLtSKykaAzs7cRt1a4Tys7ZzxwXX60YCbC5kh3rsMdX6uVsenr6HkgoVlLEjT8H4O3-057PXnyvy0nkNDckb9F2kQAPkb6tB9k3J2Cr6xcDb0tBkuYOc3GPl4GJjPV9YtCwnUXwnD3IqS7V90evU-FbOK9ryu72VV4jLHAnxJmbu0Mbj7cU_5yQZREZPkclHrxuV78pFzHGp-XY8Zz0ZXDdGloX4i0K06g-Ezeqlshc4-tLH2mlh8u09j1IV2FvmhV085nwJ8-aAlCeHvN6QQzQku3ZS3VmeshYnzdV8CRtyVgmF_DUW9GdFFUNn-Lnfke02ar6hgdztx2suQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9F7bsbqCQuT8AVoFQ1dtU6fs5TD1f7zRalS1eClTnBsOizazpZIfamSOrHTosTh96qG9TK1MConL3Xwl8WrGdrFlQOu2tkLnSHf260FPFzi521W9_KF7WCtT2F_EoNW9Yv0cNl4WwDWxM1sy8Na3UL3wH25-uYE05WIuPUQbmL3GLcIwpQLnq8PXZsGiu326MXgSpXsGH3qecrCUJmQWF8eDYOZvb5ioKMhEqT6JJSbn6J1xi4EbLMe74dZRf7qXINAqcsv64P_DXXK9oXHhHQxQhP9pisNTO4D_97EoVEyBucB18nLwbWQ_Z1quVJycJbybssybNB4K-7Eq3MKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ  ۴۰ روزه به خاطر ایران اینترنشال بود و‌ دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های
ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های
جمهوری اسلامی  و ۴۷ سال آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات
هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات سر اینهاست!
خوش به حال  آخوند که چون شمایانی رو داره!
هر بلایی که سرتون ببره،
آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی
و کره شمالی رو نمی‌رفتید! راه صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgaWPr3phWtk_rRdCzVVacP-hQZ2ov_lHe5t2j36I7sZL4JFmwbMQI5drM_lmy5sMpFgS315Pp_9c9V93BDldyPpoDsWa1jvizuTDZMvB7AiteAFwLpKAOTw8unWGsrSsBOuCn4v6Kwg7GSQWh2t5G0QWmMeM_4XF94YmldI1LCRXD4Vs6PoRUFue-PUqLtoqHkmt5tWwnHvTtAvNS1zEua-2g9S6V31xWwI8EDumojpYGfieXBrbjubv9AGpIoYTuNSOT3ozFl8KslooQj6qDabF_dnLTx4R7woQ50f1MLeN8zD9kLglFGlOpIe1uaepzGhCJfxn6PclBYQ3m8o3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqrTp3K_cQ1gEtzI8F2EgajSZ0a2Uz9eKkYGcUdVEjL4oE_z6x8vDpCU1Je_TgP0oRF8IWpmx55yoa33tFHqKFm3v5_S0TW_lhllH6MiuMGhIpuTlmFfCrlKauK_XZGi6fVySCgiS6w001bL1MchKuS-SY4CPGv4ZeJfPHDRge6lOWRVZrKK1EVHZCmhCqWVZUYWwfPI-5-3hCP19rh7Tt-J3YRu3qUi66y7YfWfpWYXuBXPcGMTI-dwyLTnOtG_jMxyw2iXpCmy6oIWDBcXWVXPDM7XKMt2eATK9ljNtZzCB8pZn4FYXkpnu5vLf3hnBydEGIAIXZwNxX9PclY5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=pC-uLFlaxq437C9CNxry0n2Gd6peVNsZDeHFhhXBX44jc14P6anyYFq-D4pIBgYrSquviaaShxQNpL8UDUsi25ijAMndGUw4Af75aD1L8B4a4PhKdxBXldsJ94dBE8Nsh4jBjjM4aV7ha0C-2CTxnTKQ_R7WqmycJW48p87TzlWfBbrndkglt1rwPvyhq7Q5RWrHMVR3E3t_aBzAWjZnsJe0kWWH3ffy82mB9sTU2OBs49Ja0FUnzHQQDabRsdB5IayhPo-NeUkl7-uPa3CZfcLKBeI-vJlbESgDE3qNYRJ2zAMTFitp0nKf2j3DoAYiHqublf5KLQXSBQXB2PwWJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=pC-uLFlaxq437C9CNxry0n2Gd6peVNsZDeHFhhXBX44jc14P6anyYFq-D4pIBgYrSquviaaShxQNpL8UDUsi25ijAMndGUw4Af75aD1L8B4a4PhKdxBXldsJ94dBE8Nsh4jBjjM4aV7ha0C-2CTxnTKQ_R7WqmycJW48p87TzlWfBbrndkglt1rwPvyhq7Q5RWrHMVR3E3t_aBzAWjZnsJe0kWWH3ffy82mB9sTU2OBs49Ja0FUnzHQQDabRsdB5IayhPo-NeUkl7-uPa3CZfcLKBeI-vJlbESgDE3qNYRJ2zAMTFitp0nKf2j3DoAYiHqublf5KLQXSBQXB2PwWJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=UzFsztmubli4vr4jyEdrDAggOOMHIcHEiuvsDZRSw3rffI8IZLVy7EgcbTG_BOHKyRI1KuozgqsaCz5E0wxjlVD4pkIv2tYa_IuVIgi5VxhwufYQ7TbJa2lPvalGfURqIi9MA5b9xIsRXugv9DYttyA2GqplMf1Zqg8nV8xjrXsqh5wv3qkJBKfHoRied9QohwoKIpuPxdEYyGtQCTC1GH0IMFZYQlHWW2Rw-qAo-Vt3WwB8XnPIjeqmhe4eebw0P4jdVfzwd04KjUdC2_Mg6qQTroPZFz5JsLDeA4POrro57kw5mFyrgfowRguXDRf99FU3F3RMv4fhc-GTmdwAsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=UzFsztmubli4vr4jyEdrDAggOOMHIcHEiuvsDZRSw3rffI8IZLVy7EgcbTG_BOHKyRI1KuozgqsaCz5E0wxjlVD4pkIv2tYa_IuVIgi5VxhwufYQ7TbJa2lPvalGfURqIi9MA5b9xIsRXugv9DYttyA2GqplMf1Zqg8nV8xjrXsqh5wv3qkJBKfHoRied9QohwoKIpuPxdEYyGtQCTC1GH0IMFZYQlHWW2Rw-qAo-Vt3WwB8XnPIjeqmhe4eebw0P4jdVfzwd04KjUdC2_Mg6qQTroPZFz5JsLDeA4POrro57kw5mFyrgfowRguXDRf99FU3F3RMv4fhc-GTmdwAsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZbwzHPOMeqlAzXHZxXcVAMj5BRWF7M-QjeSOgo4_8FDARru5RlZb7KjV7Ru3nk2WVolSpJj9of2_51VP9CkX_chBRpwDB1PutoxrT6knegnB9KyYldPBriu2TfPmz3X8mcu8BdQL5iSzq1rsy3qghpIzWcBSWIJdkoLH-Dgn6wPMW7O0d91oYZFuYmDDZMWxQ34PtDbSs6Ytz3wc50TPK6iFY5clf-5TQn6uLGfxU3HxMvId8BKQ0VaHBPNUbBs5rKJDydz-XxGbFZPUnLx_b3mD6ejjUz0jYrDCFzzjOiUXQATffJfTQed6KxgUxyKzBo5_5iLzRSlDImMNlMIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی با آب و تاب می‌گفت
به امارات حمله موشکی و پهپادی کرده،
حملاتی که ۹۵ درصدشون توسط
سیستم دفاعی امارات خنثی میشدن!
اما امارات در عوض پنهانی با جنگنده‌هاش
حمله می‌کرد و جمهوری اسلامی هیچ سیستم تدافعی نداشت!
یعنی اگه به ایران ۱۰۰ جنگنده، یا ۱۰۰ موشک حمله می‌کرد، میشه با اطمینان گفت ۹۹٪ ماموریتشون
رو انجام میدادن و اهدافشون رو میزدن!
کما اینکه اسرائیل ۸۵۰۰ سورتی پرواز در آسمان ایران انجام داد حتی یک هواپیماش آسیبی ندید.
آمریکا هم ۱۳ هزار سورتی پرواز انجام داد.
آمریکا همچنین ۱۰۰۰ موشک تاهاماک به ایران شلیک کرد، جمهوری اسلامی قادر نبود حتی جلوی یکی از اونها رو بگیره! یک در هزار رو هم‌ نتونست!
جنگ با امارات رو جمهوری اسلامی کلید زد
و هنوز هم کامل مشخص نشده چه آسیب‌هایی
ایران در این جنگ متحمل شده!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v15tr-Hp9rPIryrgycFMRMIMYGzK6mYxIv89818mNOm8hf0F1aHJS8wrE_LPTSa7BTVbFhBOJbSx_Q-69Qo_8jh9hP-zRhw0BvV1k_2C_NwXFLlHf_Vzc_zJkZtPUPw2YuSyMmz78vejq39gldwON_pyN-x8zgsDtT1Na0NxxZH6wVkPEMaDtW0PaOG2GYlT-WR6wKLRJYp2uEBRQ0T6Sfv7r0AKOzG8EK3lC-CNuY8LDpeLGDPWs0DU281V-zDyzbRs3GmVd8OQIchtYHAiLyNOLyVamp0hzgc6Ae3QEGL34E2354ydfOBBigoF2ORtAe2-arAbTWcPfBZYYHwDeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q59PTvq0qFHQdhQ9Gq9H7EhJYR9ixEup98VZxzmAfdE1EOetM0uaLKo1jxiaANp9kDa7eaHjl20J-swbsY-lNZYwGDT3aqel_B6Sa1BCtzD437vv1JCH7L3Z9eaUXrG0CPttGxUckokGASJeDJurwpj4MELo7mxxF-AlKRAn3teoLYnDij3dT7_nNgtEHmrdGBiima7I5iUkW4gXVrv_2fSVpvtcL2RKWRDkd8mXwpSf4gBJtUg1oRjvMlU7dVV4PHMQdqoXFhpZKjh9_9zNRx4pGcn4-b4RTfBF-WFJcjkJRpsRNUGitJhqzsPOUOke6uXMHLD5IzJqxY1gG9MFnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKoi5eYORZOxc8IJhfc2FXHKNwm5gl2dM3-R0FlGvr730CbjKShyrB7fAFqrVvFSVKmw4lVZWO7j8QWouPl_N_dL0-mswyQ2s1vE0woEN-5vhxQw1_4jg3-pXXEZ_fwz5byhkNq4-tm9lmC9CHEnDU2CPKiBLWJPtCbLV-XAzrpDKnMJTK6omqud3NccUv1v4X_YNLwFM7BhapU8MziVXTQ1YowNgIKMsAVYeTn5BiXEtZA3s_3sEwhv5xyfzYF3y7afDzd-MtgzXQrY5hXS1YQZq3ao4tJGWcqx0P7ey155nk3XXrzlUVi4sBGF6IthTtBguOErSfmvZguJZh-t8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : برای اتخاذ تصمیم نهایی اکنون به اتاق وضعیت می‌روم.
«ایران باید موافقت کند که هرگز به سلاح یا بمب هسته‌ای دست نخواهد یافت.
تنگه هرمز باید فوراً باز شود؛ بدون دریافت هیچ‌گونه عوارض یا هزینه‌ای، و رفت‌وآمد کشتی‌ها در هر دو جهت به‌صورت آزاد و بدون محدودیت انجام گیرد.
تمام مین‌های دریایی (بمب‌ها)، در صورت وجود، باید از بین برده شوند. ما با استفاده از تجهیزات پیشرفته مین‌روب زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده را جمع‌آوری یا منفجر کند؛ البته تعداد آن‌ها زیاد نخواهد بود.
کشتی‌هایی که به دلیل محاصره دریایی بی‌سابقه و فوق‌العاده ما در تنگه متوقف شده‌اند ــ محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند بازگشت به خانه را آغاز کنند!
از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده‌اند ــ زیر کوه‌هایی که تقریباً در نتیجه حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند ــ توسط ایالات متحده از زیر زمین بیرون آورده خواهند شد. (طبق توافق، تنها آمریکا و چین توانایی فنی انجام چنین کاری را دارند.)
این عملیات با هماهنگی نزدیک جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و این مواد به طور کامل نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی میان طرف‌ها رد و بدل نخواهد شد.
در مورد سایر موضوعات ــ که اهمیت بسیار کمتری دارند ــ نیز توافق حاصل شده است.
اکنون برای اتخاذ تصمیم نهایی به اتاق وضعیت می‌روم.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vep4E0TF7izCLiAUZKakQfOQuw3lGfGtHetxiBucjZJ_8QiArLWONXS_pvxqo2Y31x6JiKiYr98ZaK7ok7ym52Zjf_y_pnHHGs_BKF76Zv8FEd_6UHa4NNSLVfgZoym9CmXdz8JFaut86dP_5zNRXyxFn93nR090rGy1OV_ZiQt4weHoz6PA8Acw2AFON5NXbcHpAzbMrEgFalFoubNsi4UCCfHqOIN1BamzFVNvBQFcvf_eUb_6ninyYANIV3V1ACz2DZY9CU6Zf3amZ8_tBFwIh_afXUhGoRp-k25AcULRbGmC9KR_bHxRsFf_ULsQx2FdnsOe5x_qKVjKV0X3pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eTpp6Np64ASKkyTnyQummMctHhlK0TCoZ8NlwsSJ1W8GdKOVuzcPEMTTl7rmmWggln_NvD2KNhlHXrhozNkrazH7FlD1cJkzpQV83ld6BMQpdUR36p0S1Fdjmnb_KdypIZurZ3bhSOoKcttni88WNYa5a-YpGS7jJ_p1iTWKGYud7W7w9eg43yR6tHIz8ZwSP6mg5n4sMW2Ndfad7qRAeIWh3lay9uhfQOfTD7Ov0NGxbu3SNpiKeuuWYHKXRzIe3YXuuOpoch4CbRnN9kRzzHX0BDDzIFznhlnAxMCv-k6hJbRH4G5l47xrd_au4TrzJNhE9o0bAe9F2cP1BtxX_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V856ecrmonbL58TuWZ-GHzlhfUOtXNGaq9BlZMer0_4OxuDyA9JPQP3OYl4XEv66uSvQwAjdxqFOWCxvpvuUwiphieFKHpnLf9a1fFnVcYPUMJHP1DVMKH9TIAK49FXW4fMR23rgeuNTuigzI-b5mXKSzerit8lSC4iKYWa0w6h57mnfOWAFgOioxEVp1SMrKSPTquK2_s7GXDf2SwXNyEHy-IkvLC3njub9hyvhKnVL8edC0kiDZrqULuceGo1-yEGA-ZFaLRnEcg-sz_au-VKlVIVUYlb3k4uEriqZnYp1MqArHW6uEXFtVpXe37ek9PwQfM-i9op7O4GjAzeqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHFJDnXU-BIYWoq6uQfIHA8axXU_opzaEjLTIx-yHnB5lKv5NtNl-Y3U2NB_06SLhVduN9Lg4Sij9kbjiFzrTeRinMk_MFxLpdWE_MT-G9MH35HMTB8vhFB1K41qgoZ52TapwYAz4RxD0WIGnppmVrS21yQ7y7Dv-Dw54UvEPP3Z3DhS32KzwDkf7jVsgVL2Zu07qkCzehQgy0jz4yOIX1X_wAH8ShjdZtzXuFBOFO8DSXtjzJf0e7YNgWamkDtv_yj1Enb-x68E4_sOZTEw_Y_2k7iIgAXu0zJVXGDDZSwcb0gwxcUH4KAotD1ua_QFIrdrNuktmM-EUyBDKKlIKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=l-g-DtUAkclTbABFeA39Mjs5nUfEwvxn5nwn71zE4jLb_z8OvNDry-JkpstekVzfxQYmgzNu_cDJSdgvKPaaXOJI8V3_0asi0ipjZ_BHQtRatm9hGrYb5LIMFJjnS1DaPmsLKWHz3WM3FreZNtiqWxgN8Rdb638cSSj0_wQcXSbHOylFx_wTwC62zunxLyT1OFCL67FZKDv9xsVv2b93TUtwOozTz-5-dA3ONpB88Vp9-LFEUQfUIkXQU72cLhOpLtTyFI9srMBgVTKK1nEOHoORI3ZBATXwIGKmc20L8WytyS1Cs5LdktgSg4qWVwhEIKNbu_6S0K7YbetV_NPbMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=l-g-DtUAkclTbABFeA39Mjs5nUfEwvxn5nwn71zE4jLb_z8OvNDry-JkpstekVzfxQYmgzNu_cDJSdgvKPaaXOJI8V3_0asi0ipjZ_BHQtRatm9hGrYb5LIMFJjnS1DaPmsLKWHz3WM3FreZNtiqWxgN8Rdb638cSSj0_wQcXSbHOylFx_wTwC62zunxLyT1OFCL67FZKDv9xsVv2b93TUtwOozTz-5-dA3ONpB88Vp9-LFEUQfUIkXQU72cLhOpLtTyFI9srMBgVTKK1nEOHoORI3ZBATXwIGKmc20L8WytyS1Cs5LdktgSg4qWVwhEIKNbu_6S0K7YbetV_NPbMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=bvRXoypPL5OtMd9kDyAzsNGCRjd6K9oMFIpFgxN-azg-K7rjw4bxgHY7UVSniSfIJvNdnwLFTHPh9JtgxIk09LBw1NRPpYy_LI1628gv1QD2Tew-RY0NctXQoX84ZJEmRDvggT8y7IQXjg_VNcUap7uMRfJv7gHOkkCCAia1Uxtbr7wav8dLmW2jV-hbBsQAOt_tXgmljVFagoqmOy5leSFq8allPEyU9TM6ShTLwQJNfAESAAltm_LUKxc_j3yQwlXT0azzV3JKvMJq4hanUbjt4HkEudzzwV9Jjx3ytyabWFZ531rR0oMLwAW2JifYH02UsGtQIKfMdRcG9TA_gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=bvRXoypPL5OtMd9kDyAzsNGCRjd6K9oMFIpFgxN-azg-K7rjw4bxgHY7UVSniSfIJvNdnwLFTHPh9JtgxIk09LBw1NRPpYy_LI1628gv1QD2Tew-RY0NctXQoX84ZJEmRDvggT8y7IQXjg_VNcUap7uMRfJv7gHOkkCCAia1Uxtbr7wav8dLmW2jV-hbBsQAOt_tXgmljVFagoqmOy5leSFq8allPEyU9TM6ShTLwQJNfAESAAltm_LUKxc_j3yQwlXT0azzV3JKvMJq4hanUbjt4HkEudzzwV9Jjx3ytyabWFZ531rR0oMLwAW2JifYH02UsGtQIKfMdRcG9TA_gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m2m8Vi8dP9AohP-w6bS3NEGFhQrdDSVlQSz1nW0PigW14ndMg0_YRshfHdDufA1WR4BVgQZEzdGMnRgIYjUtRssW-vZ84YaUjDFTywUncMC_1hLOKDQ5jDxnCHbilfIoTMnoPZdh_u3P5zitty6nFDcMxgC84gk_Ere3chuWhPAfkb5xoWLtH9g7POQmpbCo_n-c-wGCGGm94ZMtcG7bFxRmSWqA5qdtHQV4jyzwl65dwpefXTWuKCgnZfuCZTIWL5C9sjZy3wctZTFJjI7NBDot0f9-0V5Tb_el38QpYVF_3xtMdPeOvAZUwVleNhLgcTG74IB-lxbqpsmWSdSpqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i3yJb-Rg-8_Ti_uCq0OoqIJkploI79lzHjZi46w6zYCZQLVDrAAliBpH3XLLk9--czcZGhw5cJSXJFZHwlmBcFgRLCV2pmySLV_zLSgiYdi2NMdh7el2M9c9iJaLs2BZEEklkEhrZLvj_BNWUyo8B1ktY--o3i68m3WVqCwlTELMW9y5r3Qrvmdz3Tojzd7_92_FgdoJ08vGC5-q4Hk7qNqpNgCNx-BI3mrwzSmX7Miysayg6FQUzz_Nogq6G3pS-QGsPHCWe75O7WGqfrwGCKAngZ3cQoWpyxfymBhssutjnkKkQOLKzyCQpInRUP1k934uZ_U1jYZcZneuq2txHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،
پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!
حتی زودتر از پیام‌ شهردار تهران!
حتی زودتر از پیام جوادی آملی :)
پوتین در پیامش نوشته بود :
«اطمینان دارم شما راه پدرتان
را با افتخار ادامه خواهید داد.»
پوتین راه پدر مجتبی خامنه‌ای رو دوست داره :)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=onsDlKf4Df8-pbUyUYzCOgZhhu4_8o8l4tcuvI6-Jhymr8-A6_5Lr7OQCilF2eh7hhu7JI85CindVYjJ6XoSS3TmaMZiZtATVDbZKvRbEOXhP-Qi2A4gQgObLTQxLoaCFhx69pH96sg_MfgCCJSHRMsgsAn6RHNyAq3qPYR9319qmxjncMzXHjqtYhyMZJ6fCvIEUJHq81kOkbhS-q4Lpk31OIuSwDiTNc4Hz637ypxn-CyZO6TuM83eBAmeRzIKnanHCUUt_skYumwzpS1g5Z1Ihc8zdQxEd2Zp3JlUIZ7a2ZEJ9G-FFUEOsCjKa81pS3jjuJHyImlVMzOR9XPrwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=onsDlKf4Df8-pbUyUYzCOgZhhu4_8o8l4tcuvI6-Jhymr8-A6_5Lr7OQCilF2eh7hhu7JI85CindVYjJ6XoSS3TmaMZiZtATVDbZKvRbEOXhP-Qi2A4gQgObLTQxLoaCFhx69pH96sg_MfgCCJSHRMsgsAn6RHNyAq3qPYR9319qmxjncMzXHjqtYhyMZJ6fCvIEUJHq81kOkbhS-q4Lpk31OIuSwDiTNc4Hz637ypxn-CyZO6TuM83eBAmeRzIKnanHCUUt_skYumwzpS1g5Z1Ihc8zdQxEd2Zp3JlUIZ7a2ZEJ9G-FFUEOsCjKa81pS3jjuJHyImlVMzOR9XPrwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iON85Z_CqDR9G2X85DWpuPAI8rGRNGFUXm5PCRImpWRbmrM-VsKHLlS3BPpg7G5ZMh_amDRAlQfs-BN1Yz5AnI_Ytp43Pis2ZYXCe8JdDitel_GnwCyKqUY1-evksitBV6ptcVgvZ38U0LIKtzNZgzlJJAl_Iz2tdXS1EV846DRparYDHTbueK_5Kew8nPARGfX-twVrKhd1zj8VbarYWr6km4JSW2K8PkGtns2zQgMDKK9BL7VyjIDLLxIqRhcYqgwmAf-xglIkVOSxcbbPrWm2vkIhqdlm0Sqb3zTI4dopn-j1YYV_odqO1JMFjag-bRsVpvL-ko4gjcTyYovXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=IjNUdbbaGxm8w78VM1I6s9-OwaOUNTofagW0rGE9bDiAY9kLK4nj0VkPK6Rt1TbRlvRRN54XHVRqxxuPtX9Goe3h-3C0hDidUmsTXL1wkPzTDvwd0zmhi84kYcyDwGe9X366vcxCeXbWKm6Nlo0PvecpDk82KmxC1TRBdoBs-UtGQ50loChlLFbCozhtOgr3n4inBnUopvbkDCGcie1lGehm3A4BQOFAB-ZEjI0vLlb9zM4v_Jb6JoHYme15GTqYtpxAUJN5apUCJCKRWHRc_YegokxVEFm4zB7FG6smhy54DK6w9ArTgCM6Xzoo0O2gplpLD-7F_6tMuqbua_1fTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=IjNUdbbaGxm8w78VM1I6s9-OwaOUNTofagW0rGE9bDiAY9kLK4nj0VkPK6Rt1TbRlvRRN54XHVRqxxuPtX9Goe3h-3C0hDidUmsTXL1wkPzTDvwd0zmhi84kYcyDwGe9X366vcxCeXbWKm6Nlo0PvecpDk82KmxC1TRBdoBs-UtGQ50loChlLFbCozhtOgr3n4inBnUopvbkDCGcie1lGehm3A4BQOFAB-ZEjI0vLlb9zM4v_Jb6JoHYme15GTqYtpxAUJN5apUCJCKRWHRc_YegokxVEFm4zB7FG6smhy54DK6w9ArTgCM6Xzoo0O2gplpLD-7F_6tMuqbua_1fTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=QLWTf_rBOxiDB9SMxweH82G--joixSmXPtS4d9msTNMcFiN63ulmoPFkNCtdPa7FYyqGsKdA58HaFH2tm6vprhURUr0mGt-DnNV6ZB0a4_cc_oPL4dlImWVTZdike5N-yt_d0GubBhGrk1-7d5DA4TKUfe-74h96HD8U1Oj834L6e_U_qGWke9JWg8m0omPBDb0wY4CxOlCNe1jAPez01DWVVL89iRjiIYjMG8U01w8GZ2u1hq9SBPkRKey9VagJwAPueCQBIVtfzHiMP5uRhO8-aprdp8TZMUHCa2aNXSiASiYPPRsvwwE9FHm1dDQw72IftLZVsvZcoclIbYghbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=QLWTf_rBOxiDB9SMxweH82G--joixSmXPtS4d9msTNMcFiN63ulmoPFkNCtdPa7FYyqGsKdA58HaFH2tm6vprhURUr0mGt-DnNV6ZB0a4_cc_oPL4dlImWVTZdike5N-yt_d0GubBhGrk1-7d5DA4TKUfe-74h96HD8U1Oj834L6e_U_qGWke9JWg8m0omPBDb0wY4CxOlCNe1jAPez01DWVVL89iRjiIYjMG8U01w8GZ2u1hq9SBPkRKey9VagJwAPueCQBIVtfzHiMP5uRhO8-aprdp8TZMUHCa2aNXSiASiYPPRsvwwE9FHm1dDQw72IftLZVsvZcoclIbYghbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=p3hSFNP5XBWaoSyQZGSqxbJWr8ucVq1DbxhcGWXquIlCMTE8gI4Ai4lzINzC57Ren-FkHvcH5AYbLDqDm1-HP3RejW5LkS-OQSiqNZt2mvC6IGBdOXqthCPIYJVdtIOD4htLyuIn2qFL6WAk3vg8gMB1ixt7YEgvvn4GcNJGIbDERzjX6uylXtJ535X7z6NeVVOvL3Q43QiUEIP2ADIU2Yvqp0suaFJoA7thGwJWKIJYhP-Q3NfXncig3V4SCWTAKiOXFt4DnkoiInfSxnQJTQ7xYA-NEhyik-95DswVMt43vVEa4I2wq-i9kBOQl_vwAulP49yYQDJ55QS70iCuwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=p3hSFNP5XBWaoSyQZGSqxbJWr8ucVq1DbxhcGWXquIlCMTE8gI4Ai4lzINzC57Ren-FkHvcH5AYbLDqDm1-HP3RejW5LkS-OQSiqNZt2mvC6IGBdOXqthCPIYJVdtIOD4htLyuIn2qFL6WAk3vg8gMB1ixt7YEgvvn4GcNJGIbDERzjX6uylXtJ535X7z6NeVVOvL3Q43QiUEIP2ADIU2Yvqp0suaFJoA7thGwJWKIJYhP-Q3NfXncig3V4SCWTAKiOXFt4DnkoiInfSxnQJTQ7xYA-NEhyik-95DswVMt43vVEa4I2wq-i9kBOQl_vwAulP49yYQDJ55QS70iCuwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=m6hdh5cTlO7HvIXL2d-JgYIDYuRH-3eMHUPpo3UDC3ihA093Eh_0N2bsiVRcvk9Dj4Is5e-VCbexEEevNx8ZpOVASYc6DCGL4dUadaEo2Qio8cXwZSqKYnyahZQILoC0PgwkIMul2koDHBNMqAIkR9hfhr2_3mPzn8P_PbUSf7EDfnaAtrG5iymHu7S5XJBaEV6MUYbf3DOlcJlEZk2timQ733naRaZ-DwwkNC8BAM6MAWzL5Q6R1bXp3NPCKvZiehUHILgzolXjuKjcLnV-jaK9pQ-jVRXXW9KLdQBDzfJdxDVIYE63dNHFPlipGs4gRnLSJ5nNI2e0U36UdMjJZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=m6hdh5cTlO7HvIXL2d-JgYIDYuRH-3eMHUPpo3UDC3ihA093Eh_0N2bsiVRcvk9Dj4Is5e-VCbexEEevNx8ZpOVASYc6DCGL4dUadaEo2Qio8cXwZSqKYnyahZQILoC0PgwkIMul2koDHBNMqAIkR9hfhr2_3mPzn8P_PbUSf7EDfnaAtrG5iymHu7S5XJBaEV6MUYbf3DOlcJlEZk2timQ733naRaZ-DwwkNC8BAM6MAWzL5Q6R1bXp3NPCKvZiehUHILgzolXjuKjcLnV-jaK9pQ-jVRXXW9KLdQBDzfJdxDVIYE63dNHFPlipGs4gRnLSJ5nNI2e0U36UdMjJZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=Q8B-btN-PwnuWzpwltl95mz8Rvx4Tbv-CJ_5lw023-vzL39hIpxXeRhb4kOjbUJyv3mDD1DeerzTcMSuPsTEx13ljdtbDWfezoHQ4zjahcC3SXtHQFEqetoJHmsZcS6tuWyoiazYoxVMo5QyvyIL0U81xcHwzJof3HGRXHHou_gAAWW-a_LxRwqqxtvdzOuLu25kGLyIlFGfAGzlQOE8bP6pKArapYA7fv4Y2lkQYXvyAn-QMKWwPeSICG_QjBNj9IrjFWNKuvHOXxX01zlDzpk4y6krGXidbU6ORfMlpJpGrt9p_m-wpA2k6cFg9HitCnVxz2P78u8gJcfnquta3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=Q8B-btN-PwnuWzpwltl95mz8Rvx4Tbv-CJ_5lw023-vzL39hIpxXeRhb4kOjbUJyv3mDD1DeerzTcMSuPsTEx13ljdtbDWfezoHQ4zjahcC3SXtHQFEqetoJHmsZcS6tuWyoiazYoxVMo5QyvyIL0U81xcHwzJof3HGRXHHou_gAAWW-a_LxRwqqxtvdzOuLu25kGLyIlFGfAGzlQOE8bP6pKArapYA7fv4Y2lkQYXvyAn-QMKWwPeSICG_QjBNj9IrjFWNKuvHOXxX01zlDzpk4y6krGXidbU6ORfMlpJpGrt9p_m-wpA2k6cFg9HitCnVxz2P78u8gJcfnquta3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=q5JsZ0veNMfKw5EnJBAZYu277WMy3PkqDPJVq9vdTsDTmOac07BypDZyWX9BoS-SQ65UvUdzVu5uWm-PUi8Y9tK6wgMvCq7FdXERFw3oQnLCAUsUoUUnzL5yHBc5N6i2zI7gcgMnDwcar9VPk9hbaNQeITDnfN1pOEFBj0nBUnHQ2SnqmLaSZD2P2g2J4YMrRvrTXt-hb4UkZLWjbcec_ueHi_f5cqPG_V2WD66qi9f50TQkyfNBZ7AR6GtpTcpRlXSwGPYYNZkobj3kSsKJgFjtJw6vvJ2oFVtSruapp6VNu56Vf2n5twdheN1AfoT6WYyZyxStgdHiG7ej62kGSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=q5JsZ0veNMfKw5EnJBAZYu277WMy3PkqDPJVq9vdTsDTmOac07BypDZyWX9BoS-SQ65UvUdzVu5uWm-PUi8Y9tK6wgMvCq7FdXERFw3oQnLCAUsUoUUnzL5yHBc5N6i2zI7gcgMnDwcar9VPk9hbaNQeITDnfN1pOEFBj0nBUnHQ2SnqmLaSZD2P2g2J4YMrRvrTXt-hb4UkZLWjbcec_ueHi_f5cqPG_V2WD66qi9f50TQkyfNBZ7AR6GtpTcpRlXSwGPYYNZkobj3kSsKJgFjtJw6vvJ2oFVtSruapp6VNu56Vf2n5twdheN1AfoT6WYyZyxStgdHiG7ej62kGSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYXFkDfmt4qRRnNtsPaUktz7diMPvjNH1AlLiS9CI5icRBFEdhDB5x1u7lG-MyDwbO3-8lLRvG0YaiR9d_4pvvMAEOXl4euWuDFoPkTkBSuBMKgPfZmgxVZZw2WgnMEOJrHxbuze8OU5tqhIfvvpfjjLTw7TAHf2bnf4gf-04Ky30s-uPUOD2pULo2xsjkiOopdNCABDaFdwEVetXTDmiWosfuFgqXC4xuwwPYEvPf543ZLpFIbVCvlq9zp6mbF3UUH4JxPVBaZ3Oun4QEtjL3XKMBRv_yooWQWR0rZmpvIl-93ke1HmF3KXTskXAqhZFLDW1tJ1wJMT4J280JL8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=oFBBJZddumFZUkDpl1-t7psOEW2FNXSfWiZ-Oh8vCPSzxf0VaqPWwaZiySd03nGukjCZLC_xHRpz0KfQw9BD52-INxrbV1lGjMBNa8Tbd6AQB2WQUDvXk-khdml-d576n_BUxRk_xVnYCWvqyYZZHEGC8pXWNCnLSm12HzFq7iGCORBnRaY3HdxHna4GoOh8d5P379lzVhOrghrJzl9f2xW3caXLyh_YQqTZQsoe6gEAIvZi6uuaEDqyXzHnxX7aPkCInzPyZKOr7Yy4yQcE-Wbm66YX0hRvBg-8Mjx17wHCOcoZ1Yg-oGJ3xOj3eSBFSFME6GjzB8NewKD2zgzbEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=oFBBJZddumFZUkDpl1-t7psOEW2FNXSfWiZ-Oh8vCPSzxf0VaqPWwaZiySd03nGukjCZLC_xHRpz0KfQw9BD52-INxrbV1lGjMBNa8Tbd6AQB2WQUDvXk-khdml-d576n_BUxRk_xVnYCWvqyYZZHEGC8pXWNCnLSm12HzFq7iGCORBnRaY3HdxHna4GoOh8d5P379lzVhOrghrJzl9f2xW3caXLyh_YQqTZQsoe6gEAIvZi6uuaEDqyXzHnxX7aPkCInzPyZKOr7Yy4yQcE-Wbm66YX0hRvBg-8Mjx17wHCOcoZ1Yg-oGJ3xOj3eSBFSFME6GjzB8NewKD2zgzbEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYG6QGfZpCfp5px93QLFbw-71VATDBvCy7pk3tTdWkLHVJ-fJ4TshiiR3hxkQXe4_k-QRF833obFbsNO3zW7dUqB3FLNp9w9aBEmZp2HdISC5ZZCVSyxtpvg7w5xLTAZhHBFypsPwg6_PNAai0dXlnxdjg5ly2BGU5d1Bf6swvWBWlVlaXW05hSm_GFVNEN8IxnqhD1kKxCHqd8Ef47P15GMKD6sMgJoiHyw4Xn_WzD8ikBBqry1KjVzC8fck-A6WDlUJAsppAVOmK-p39zdKBLRNk9Y0OVc873-H5vohWFzSFfFjsQOEfYGDmKg_bxiBWSk1RmmaZOUMUUYOd3aOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=Od6JymJrziNU1zmxfQ2H_RrHyaKq2GRYb3Um1tZ3lKLxqeBECcaZkudm2kEtaWIGwYw21JYPyIc16lm34HBqwTQFKhLDZ1uKTg40byf70c7zng2r2TVT42IMfQ26QOZC1PdjNaquLPRa5HOugHP2STNUhnkM1K7tj8q8AaSXiCT9eQcDGbwUNzFv75IeGucNEuKqcLcLsL4EsDurr5wysyzBfo6UcOzBunuKEJA5NIQ_Pal6Ym1_cpAsgVd3NuTL1bU5Kwb3tpv8hpzP_UI_G1OOH81zPCOOxCmCyBsmJdDkmJxOnxT5cVLgIkNdVSVqjF8e-aVcze3iPWvc27b3MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=Od6JymJrziNU1zmxfQ2H_RrHyaKq2GRYb3Um1tZ3lKLxqeBECcaZkudm2kEtaWIGwYw21JYPyIc16lm34HBqwTQFKhLDZ1uKTg40byf70c7zng2r2TVT42IMfQ26QOZC1PdjNaquLPRa5HOugHP2STNUhnkM1K7tj8q8AaSXiCT9eQcDGbwUNzFv75IeGucNEuKqcLcLsL4EsDurr5wysyzBfo6UcOzBunuKEJA5NIQ_Pal6Ym1_cpAsgVd3NuTL1bU5Kwb3tpv8hpzP_UI_G1OOH81zPCOOxCmCyBsmJdDkmJxOnxT5cVLgIkNdVSVqjF8e-aVcze3iPWvc27b3MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvN2LUdkgDpZD4y9xNpzW3RHS9oCayxaZwFMdXqSWvaDJTJCT6gJ_vFpgc0vUUvl2ZY5Cb1okvYHHwLTVhtenGfABdtajvT-1FxxpB6pH53Bw_l8V8bkizIiYlGRENxqQhUdnqMr3mm0keXQocfU_YSeSvp88OzqSatIAB-vBkhgIf_KpkNh0bn6usQUxz0isVRjTSK1MVFjhr-eKVyECYPS_sUPRpBVTkOqsnoIO6R3FgDHT4Rw9ZEfBj6p5JzrkVz_vwamjIZsPX7RqvEEAPRxvlpH6EX4lUK5EruPcdMawGtel4ui1P8sZ5ifRnwV3B8SiLEeyGvXJSLHsfNyAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaBBpchJc90SajQKRU_Y5kLqFyziPt0xC7szo71erD1-sZOPbYF7Q7TL44xuo_o4BdqNapC4eLE3k17DptZvimU8mDuDBDYI2lqOA9Nu-KgLVEg6qf-lHv_ifjJakPwj_zyAiv6Z5jjA3PBMmkalaSl7h0ekbBaIMW5vEfgWT1divnirblwpmm1GzQ84lUwnGOqf8bwgt9rycuo1_1kQyop20kohyW9Oqg-I-wYTGOazmYSrFA2yGDhsUfznX1OSjyoqyKHGOCdqi41aaXW5L5usKNtF0NwLsL1QFwE7qsk7fYm8Xn58SNCqczcehGgjcJfu7ai0_36zeho_jcj_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOMelusxOeCsVu1hQw875gPL2o0fBanynmnUpHH8XFzRmLcXzk5oAYrbfFYpREdAO4ZsJNVFYlfTzPiv6uV2XC8M9emL3QjuOYf7WDFqX5a3o60Cmp8MpSCgjUbFoY0m3yOlc-3-AX4vJ2HDxiE6DNEzVUKFcxcwJ2McK1TZ33cmvQ-HcjtltjheDHVbTVJwcTSAcqeH26bisoW5aBdgsMAGRjuNSlIb7w9FRjghKekY2ET2OYgDHiS5Sg-dEKLyKXLgpoO0aRIgsSnOpzMa3TaTnAkzSirAdi22zvPfb3vZje2dLnRxVRBuRG2wTrajC3CxVgK1VFoV1Y3zu3Ae9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WD0E_neyq2mrA2i6yzUfpWzlR-Xlc6Tek3Wse-0Fn6dUExQyASOGWBhvpgaKC_IqgJnnxJdPG-t95u5YPX55Ax0p91MfV0beDMRqfsVxCguH6QUKhgbWU-vrsy6L2ZHtbP55q6S-VgE_PNL_2ClIfH_0fn04nZaHTkLjjCKntv4lselFMLVx16Y4DrYtsu-MJZT5p567VhsgRAU1AGiRLVj7MDxKJvOEbxuInTc3AalvtcMVzET89b-HGtst0K_fvmHRIBLKA1SHx-q0ATeYokrztfrmUsUGv36LoPsTKMSmfiysHntUjSashABRWwvNI0VU4tWDsxkMSL6vmGMQzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4aneOJ-8d7C7mVFUe3ekZKKpuSRs9Df1OJ-0PT1P5Ej9iOv2jWPpGbrP9EOfaKvnsT1olixcGrTyoX8kOGa3ADqeyWbtKQfmjLYsji9jgUnRbUEDOvlyLlK6TCG_WfwPBuGisLHYzcV-uWNh1Lz-_tMvfvubWkngd9N66L18qvf68gBLcQfQJCZz1_Hy8LcYGUUxTKmfzjEteTsKV4z0oGEgQAIPFR0R6UXJb_J1-m_oQmG47CGXIxl_29lBD7zAt1qhQtyMQf3vMdwbzAX-o3Ty0zywmD39wo1go-xyFMnSWnkq6UMOr_DMTu7VEB10V-iuTqLPBpLaazQA596-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sN6VX-i8_tA0h5xUClQTa_cNOBoxc88-qshXH4jwpOtkr3FQ2XcrYcsOy0UFCNXmHiLXrsVG5YNrpx9paYtpWBvC1xanNfw7FmXFrf0arorzQgrjsFD_uc50_Qm0pLONARgRNgWCU2OfBgn1ElzsWHt9YZSz9Adb9__8TeaO4HoSoRifTUMXZ9YOECnWcHOFdgeXf6srnXpljx35uvbFXAebKgaqwHNf33PJPpl8E_JpAJijeKmhM-_d1RTUURXfYTA6op_rwaXANero7jL_tkWKlXHLMzdKBlztuEfP92oDXsWz8IPWoFYG-fpTNhMxbmgGb57I67duVNKgmCE5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WS1NQrEdPb7VmgiG6zZcooI1fKRpN96fyORneQ3iZNkqCRqNVxlhLANSPzE4qdYjrI1nfppHMHyu3p5IgD59SJoXrULotduYJiv9spLrGYjszw8cDFDg_Ib-DDZ7lY1jjgQr2w86WBtjox5WvgYZyl0vQwUbAiiwdcxGqNoBNSlI8SZSkSGL4V5tEDr-7wahJpdFYsDpVbIF92FeP_UfMhWFC7N0B-rnfGwB1WlRmxubxWzPg7Ug9PfeP0_oe-0ZJ7F-uS23p0nufpjrxkcoL8MRgoxfDRGKxdQPUsIY5eS06B4MXovMykyZv2zT0bnXv30T2FI6RwaJn7L4kC9WJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyLkUx0jGr4KxdUGY0JsOjVedgnBSx3yzpotagHZ6Gf4ES4Q--oNOGC88N2-WFQ3X8wSSZMN0WZrHbaU6DeB98U5fUm3_6Eyn8HvYTUbn_ME_7zfwDhj0s6ijgIXVe004HayDDEKDCu-pOe8jkV_f8qMcGunBVoig5BPa3JRh6Q0QP52Ggsz9Oomi-KpTVRMVV71sRvxSavgscrUrjXC5xMm--8hAoOZzQ5UK8k8nNDUzyLMdQhfBegfsSdEkLvYEzQvsBrSTnAH4EKMIes6x0cJ6wbXpWm3pPOrn5FMCOsh-09isPCmBPsXcfuu7uWAPFcNyNCU1SraSTh-KAfkIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=b9VQLP0i8KRVp3Rc9WxS0qEGJ3ootRKinypuBe6eHlbOXl9o3ThJWEoU41OSoUx6IYvYcp7e8IWfhKyPrAe7NEC1GFF5J6aLcQOnNkTmupjQfurmdyBdToFe5S4d2XKUPl_bi8VR4b6o0MCHT9NTCKNRsam57emvjDE8s23oal__0PTP2G5EhydZ_umBvOdNSeFlFhD_uDuZO8sn984ClfPQj41Nx1RFY-7-7w7gEgQtn9mYUkFvBiom0tdJOse1BBuQuuvbHMyT0armkECxwGeVHbzSyWNW0Pa-gNuMvcjj5lBI6Z2QyI6neUA2YJ5v6CeQHKB891iUAt5dq8uDMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=b9VQLP0i8KRVp3Rc9WxS0qEGJ3ootRKinypuBe6eHlbOXl9o3ThJWEoU41OSoUx6IYvYcp7e8IWfhKyPrAe7NEC1GFF5J6aLcQOnNkTmupjQfurmdyBdToFe5S4d2XKUPl_bi8VR4b6o0MCHT9NTCKNRsam57emvjDE8s23oal__0PTP2G5EhydZ_umBvOdNSeFlFhD_uDuZO8sn984ClfPQj41Nx1RFY-7-7w7gEgQtn9mYUkFvBiom0tdJOse1BBuQuuvbHMyT0armkECxwGeVHbzSyWNW0Pa-gNuMvcjj5lBI6Z2QyI6neUA2YJ5v6CeQHKB891iUAt5dq8uDMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9pRO9fLMVbg1cDp6OAwvFSaxJnX7JRB0ueHD5Y74RVZX6F-9m1xXZOOUZnso9IvxpwLS6kyNT7wudp5xUIucfd_lZmxZZpX5_8Q2QPQ_IvHXc9Rs7KfNt0a6MpuccV65Ux4DpbD3YSWChzmtlTP1KI3sJHlwuBxBOyKMg2f2Sa71fa3Q4BySZGXSzbb0hYOaeRO3ARGEirwAlaKwGFUpeAeTmU66BfLduMIs-6ZgfjNI_DRKNKMt2_Oi05_HCqPxUtXqWuR4UQAjO8GGq_jvtU7EZdnVqN1KPBkS5_x2cPl2D047CsYoRXdXrXqLrOmTHAvpqa8T_S030wPZwNWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
