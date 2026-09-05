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
<img src="https://cdn4.telesco.pe/file/bUxLiqYNY9FWnBSm-5mTiVe4_uNrypgL_JLB5ixY64XXOTAWwwrtEer0V5mqWce5Tud9nH2FMsHRRVWnbGOnGLO2JD5B-rEVkLQjfRNkVQHLeSZP9U-KPQFnDeJ46nTo9vUmgbZU2EaprMTLl5C5bWyFXSeYoVUM4R_DqA9mp5Y2YvrMLrGgYG8TRw_Yb1ab4xG4Mw3cRScsNzE5JqisvGmQeizDmxHLc_UW71-FiOINcMxiyVXGU3frgEbB6ppb00pF0fDix2k9GG-lUkdlJJWZH7yZZUVMBEV6COe4Z63Sn41dWhf5ZoIH_HEtc_wGkmKw_QMSlRhK6mwmVQIMfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 939K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 17:26:02</div>
<hr>

<div class="tg-post" id="msg-145745">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (CENTCOM):
🔴
نیروهای آمریکایی در تاریخ ۵ سپتامبر، به سه نفتکش حامل نفت خام ایران حمله کردند، این در حالی است که سپاه پاسداران انقلاب اسلامی (IRGC) موشک‌های بالستیک را به سمت دو ناو جنگی نیروی دریایی ایالات متحده که در آب‌های منطقه گشت‌زنی می‌کردند، شلیک کرد./الونیوز
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/alonews/145745" target="_blank">📅 17:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145744">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ND_nXvcEMQzse1RZHF6mpgvkUEE1FEJjkt1jx3tDDlI42EKnLSWsN7_5sbiwQ4-lgEYlk5zL8cNV9lM5uOY5O9SMbD5B537P1ISjGfzyGGZCFUNUWdvyIFOhz8ELlIE-57LT3X4vVUpBsYU3nHPQJMK5wwz9iOdVIoarQFugUMuoKj6qxMiIB-iNbXz2YrKVbH7uU-AYPv5WkIVAXKzQZEwCjGV-KveMf7mSLRCqrY9RLdmiZ1GnE1bAZvIisixFwUJYnia8kF9sUr92SWxNG3GxIWX4YMLf1oJPt6gjdWz50KWvWyGky16HkL-BpOYC_Y6HfQONvafWLcxpwSnN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: ایده تغییر رژیمِ ایران دوباره تو واشینگتن جدی شده، چون توافق و همزیستی با جمهوری اسلامی دیگه ممکن به نظر نمی‌رسه و فشار اقتصادی + محاصره دریایی میتونه به «پیروزی واقعی» منجر بشه/الونیوز
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/145744" target="_blank">📅 16:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145743">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b0d105013.mp4?token=MSZyJmTLrbi8JUESrRwryuuBhHvIWmQFtQs2yc9wXNZc-_ZXPqNxtUw3cPSkuuQgcerD3DXbkLqySlKqdCYOKt-Rr4RDbu24p5qK7EMH-SbomBXzyFc8kGt8aV863oq63VmlNv6xEneAigbFBtxOh8LotVpZCzMR-CrRUQ1nfFKwJzNRgJFBYBUxo_h6458yxFi3GytVQfGZA2CTZvnUu6ZPLAtZX5jv0BWzSv1slEf_HzCcgUrnBmA5P-R9BqD4KV-fYOrZhFJElhhcuT7AS3gn5NV7UrFjhCQIoX40eBKFYbiHoq1SHAeXbwtFECrWqHaE7QN6gbC4Krbu_fIWdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b0d105013.mp4?token=MSZyJmTLrbi8JUESrRwryuuBhHvIWmQFtQs2yc9wXNZc-_ZXPqNxtUw3cPSkuuQgcerD3DXbkLqySlKqdCYOKt-Rr4RDbu24p5qK7EMH-SbomBXzyFc8kGt8aV863oq63VmlNv6xEneAigbFBtxOh8LotVpZCzMR-CrRUQ1nfFKwJzNRgJFBYBUxo_h6458yxFi3GytVQfGZA2CTZvnUu6ZPLAtZX5jv0BWzSv1slEf_HzCcgUrnBmA5P-R9BqD4KV-fYOrZhFJElhhcuT7AS3gn5NV7UrFjhCQIoX40eBKFYbiHoq1SHAeXbwtFECrWqHaE7QN6gbC4Krbu_fIWdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
لحظه حمله آمریکا به تأسیسات هسته‌ای ایران در قسمت جدید سریال سیلو/الونیوز
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/145743" target="_blank">📅 16:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145742">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ul_fw0GER8AjOdE5p301FkGcwrw_vGia9oNvaOaSFCceKOVbcmYonWys1ac0KPl_EoPbIKY83h81RLkHSextfnLN1dJoueVGGpBGyHGO3F7ocUo-URj8PLs8HTeiDipP2xmpVPvPhxRmR6b7zgWOztlHb9WBNIpKjzKoQvOAgofDx1lrYrzAKcuN6Odu0qlFFqrFTFQTJ10NPzmEfQOHOsVnMuWeVY8uPah2iKTQIoTHCOaR3bUqd63tGw9ebmrUiDdrWG9OEK8WdHlvCTR2gumwomAHkLG7EuqodLOO2pnhlDq6l1UtGjOeeIsxHHZOrlY6bj8tToy4wAu3aY2YWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی چمران: باید با یه حمله پیش دستانه دشمن رو نابود کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/145742" target="_blank">📅 16:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145741">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
طبق گزارش رسانه‌های داخلی، قیمت دارو حسابی بالا رفته و انگار این گرونی سرسام‌آور دیگه از کنترل خارج شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/145741" target="_blank">📅 16:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145740">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=WSYFN00yqf-Tfzzz8HMIpEL70w_TswOmqFf7yYByN_bXT1uge8xMXKcr3gZaQ6PhfTpRwyER5vX-tE62XpA57X2kZH4KxG0gFrz76SclIdu9htH3_fBWdGNJiFOBOv5lRr_aCcmBJgmSbe4IcYsVdGPHhcVOCTcFvhZi4qeFsTnymqAZripD-X2n1sEPloKtxfWx8XZuFjPDRroq6VcOPEAp_6NVxl72m8t_K8aM37GKL5iWTcFAH4jSrimqLoDVZ14r-Z7EubFRyBXlDwJunqO---h0K03cbhHEsZ-WDKBsmj0O7uoCzafMByFJ5YNbnjdnga1_At0SIQ3WoniINw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=WSYFN00yqf-Tfzzz8HMIpEL70w_TswOmqFf7yYByN_bXT1uge8xMXKcr3gZaQ6PhfTpRwyER5vX-tE62XpA57X2kZH4KxG0gFrz76SclIdu9htH3_fBWdGNJiFOBOv5lRr_aCcmBJgmSbe4IcYsVdGPHhcVOCTcFvhZi4qeFsTnymqAZripD-X2n1sEPloKtxfWx8XZuFjPDRroq6VcOPEAp_6NVxl72m8t_K8aM37GKL5iWTcFAH4jSrimqLoDVZ14r-Z7EubFRyBXlDwJunqO---h0K03cbhHEsZ-WDKBsmj0O7uoCzafMByFJ5YNbnjdnga1_At0SIQ3WoniINw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار 228هزار تومان
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/145740" target="_blank">📅 16:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145739">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CavtyyUiKykcvmpMYzScNVH7p74jOGzHn0CT74DgkRbtfN4XxYdZDmkiPtG7eE_DTg8mKSM5GGBdJqcM1AX5PZXiDz6qhVRMcfs8sR4cb31Xm83I05aSfgVvWAWgn46djiY_MgsF1Fwi0f6rP57oXZNeATE0coCt14NVMzEigi06o_OkR_JxR_BT0PtlpnuVX_257j2ts0irurKiOGHvItbTPwTj5lGgeJNy7ysoiLfObhJxqDpfOouI4x81XLeK-M951lA7ZFgyPlBZ6SzIHvM4xA6GScbb5xz0YKWuEHAkIy_NFAVVVKPyzj5A3NnEfhkIcJt6S4t2tUzlJpHk8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: گرونی‌ها تقصیر دشمنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/145739" target="_blank">📅 16:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145738">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
قالیباف: اقتدار ملی بدون رضایت عمومی پایدار نمی‌ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/145738" target="_blank">📅 16:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145737">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63de3fe24.mp4?token=cAPhd3OQ6S8rSxr9gaS2cALMAAMQ9-HQbJ-Ggxt6SdVn-3XtHrvcTzg2il7ANsaSD560-ipsQ1JOSUHxs6uSDKyN7No3IKeTIFb0A76QFF5T8kppoX4eovhtC7o1Idubyr3lMmqi-dLKg1wBX9v3KsCmY8XWW7Q9AidngxlHqeoGd9FPP-TDbSmw_qOPX1mu1hqh6VWdcCl-4-rn_13s8yUnUww-PvHLSTYe-YSQRYN6lHhwkPKFRoN6DvSh2kmcrBC2zcr20yjfcIUL95_uytmVvePc8IIrnDWPp8mSPiAn_4qLR0JXYiClIQShkj8Ewyua5x8Z0ddNXv88-R9zpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63de3fe24.mp4?token=cAPhd3OQ6S8rSxr9gaS2cALMAAMQ9-HQbJ-Ggxt6SdVn-3XtHrvcTzg2il7ANsaSD560-ipsQ1JOSUHxs6uSDKyN7No3IKeTIFb0A76QFF5T8kppoX4eovhtC7o1Idubyr3lMmqi-dLKg1wBX9v3KsCmY8XWW7Q9AidngxlHqeoGd9FPP-TDbSmw_qOPX1mu1hqh6VWdcCl-4-rn_13s8yUnUww-PvHLSTYe-YSQRYN6lHhwkPKFRoN6DvSh2kmcrBC2zcr20yjfcIUL95_uytmVvePc8IIrnDWPp8mSPiAn_4qLR0JXYiClIQShkj8Ewyua5x8Z0ddNXv88-R9zpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اقدام عجیب در استفاده از خط ویژه و توقف آمبولانس پشت ماشین های متخلف!
🔴
اینجا، تهران، تونل نیایش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/145737" target="_blank">📅 16:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145736">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9440ae83.mp4?token=OnMfNNHrmdGQVLjhOsH1hoHV0lKBLjGt7aiz3Qf6GtFtBfm0BaFLeQaG0C06c1b7NrTNH09A0tZFueuNqjwfhfCoX_44gvmuPT_twpjda9fF3gtYfx8h7w4I7SIhGbCur1EZdy_domTzGIL130G_bBp2USqZtV_R1W-d9Q-14LdjRM2c0igIZg6VBAZlfc05c-XWNurnUgZLdt-9vg_N5Zcd15vBIWUMVeRaOVDyBTrtDs0noT6NZjitXuGSMmr5oIX7Yir80X2fZHG-bVIxXrt0rwC-lfRiGtY21lhVxIyV_LVz6jcjyDjRoW9nVnYY3SPYagoqaPjrSiQ7YFvZlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9440ae83.mp4?token=OnMfNNHrmdGQVLjhOsH1hoHV0lKBLjGt7aiz3Qf6GtFtBfm0BaFLeQaG0C06c1b7NrTNH09A0tZFueuNqjwfhfCoX_44gvmuPT_twpjda9fF3gtYfx8h7w4I7SIhGbCur1EZdy_domTzGIL130G_bBp2USqZtV_R1W-d9Q-14LdjRM2c0igIZg6VBAZlfc05c-XWNurnUgZLdt-9vg_N5Zcd15vBIWUMVeRaOVDyBTrtDs0noT6NZjitXuGSMmr5oIX7Yir80X2fZHG-bVIxXrt0rwC-lfRiGtY21lhVxIyV_LVz6jcjyDjRoW9nVnYY3SPYagoqaPjrSiQ7YFvZlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک فروند هواپیمای جنگنده F-4 Phantom متعلق به نیروی هوایی یونان در پایگاه هوایی تاناگرا در حین برگزاری رویداد "هفته پرواز آتن" سقوط کرد.
🔴
هنوز هیچ اطلاعات رسمی در مورد وضعیت خدمه یا علت سانحه منتشر نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/145736" target="_blank">📅 16:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145734">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMSn9GDx9rMj2UCDnheZgLHm4YwBDF055hXw_v3kTDswDymggBI3g9f-Wjg5lWreT1GzCvPpiEVxGY3z6LLsYANLc-DFUUqf3CLLN-MxpzBTd5DTxFw0IH67yDyD8f-d9ZuBNpCeA8AXD0kJNnEPFrY4Ja7ZPggKM6yCJG4J1pZJpwHnNFdOWRF_y_HwSYEhtbLRn_p-6IgXPicQo0rxb_cHz5py7Hft66QjcMEW073GjpAL0R6cO1VY3PiuCRYlxK9BF1DE0aTsnt6pgg2qeDpeMwPRYPHG_DpSZFBMu1LUHleBXNXozJZtbHDMMpatue1ZKLzoqfkyDex0GLmRqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b238e634e.mp4?token=LOxlmmo7Z62nsbDFBLT41CFxvXXO9Pn_ML2OVmfhbeSw4C7Akajxeglgsfxojj9x7Fee0Uik459MO9ypYSYDOL9vIczVmTeTLewDOXPXCvtxJ_U9txCu_JlQe8Hjqg2SDaYoUhG7Qx1dcaFbutStrsyV7vRAgdYVXNZuoky02nFfH4V1hnIrnTZEs2HBc9LOPV7GVhg3pVu84wJYdF1uE1ajxCbygqLSlrax--N4Ka7JPFvz7r0UslEpVt8E2FXazOaCn7IK1AnhG3UgFOvPzncV_staLa6E49wnmlkoKiBtvWyWlYvxMpI0YSMQKiOLFK3HIJ9sHQLsMJY4hyjz0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b238e634e.mp4?token=LOxlmmo7Z62nsbDFBLT41CFxvXXO9Pn_ML2OVmfhbeSw4C7Akajxeglgsfxojj9x7Fee0Uik459MO9ypYSYDOL9vIczVmTeTLewDOXPXCvtxJ_U9txCu_JlQe8Hjqg2SDaYoUhG7Qx1dcaFbutStrsyV7vRAgdYVXNZuoky02nFfH4V1hnIrnTZEs2HBc9LOPV7GVhg3pVu84wJYdF1uE1ajxCbygqLSlrax--N4Ka7JPFvz7r0UslEpVt8E2FXazOaCn7IK1AnhG3UgFOvPzncV_staLa6E49wnmlkoKiBtvWyWlYvxMpI0YSMQKiOLFK3HIJ9sHQLsMJY4hyjz0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی در حال انجام عملیات تخریب گسترده‌ای در منطقه بانی هایان، در جنوب لبنان، هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/145734" target="_blank">📅 16:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145733">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
از سرگیری پرواز تهران - تونس پس از توقف چندماهه
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/145733" target="_blank">📅 16:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145732">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9207fdfe3e.mp4?token=jrVmJdWF-OfbYRkuy6rxOpNtRu0VhoRp2xv5tMjHS0QhejpeYUfJG5YRooN71nYLHjJcqYdbgISaN3C5msA8XsHA5IT83c9pYlq3XGkEl9gERsMwYO6NllRoi9eNNtblA6-F-JtR9BTXyeRk8Z_VbO5sA2oRd0hTrZA8KTh-sFgf8arVM8iFbI4XqgDwDo5rslBpWH9eSG4NlhdUBGpzJqzWO_tDK55m3c58gNsP-qFlW0nlyNDSWdDEuTrzun97I32khkQyECuBwK8Y0sW3MY-JMiBALk0OQHsTKQzI5RIFGPzjOfxGQt6VOYm_kgSb3iXD4DRoX-blkw2hgT2HfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9207fdfe3e.mp4?token=jrVmJdWF-OfbYRkuy6rxOpNtRu0VhoRp2xv5tMjHS0QhejpeYUfJG5YRooN71nYLHjJcqYdbgISaN3C5msA8XsHA5IT83c9pYlq3XGkEl9gERsMwYO6NllRoi9eNNtblA6-F-JtR9BTXyeRk8Z_VbO5sA2oRd0hTrZA8KTh-sFgf8arVM8iFbI4XqgDwDo5rslBpWH9eSG4NlhdUBGpzJqzWO_tDK55m3c58gNsP-qFlW0nlyNDSWdDEuTrzun97I32khkQyECuBwK8Y0sW3MY-JMiBALk0OQHsTKQzI5RIFGPzjOfxGQt6VOYm_kgSb3iXD4DRoX-blkw2hgT2HfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: من به قطر حمله کردم
🔴
من هم آن را بمباران کردم و در طول جنگ به آنها حمله کردم، و آنها به من حمله کردند.
🔴
کل این ماجرای قطر یک بلوف بزرگ است. قطر یک کشور متخاصم است، اما قطر کشوری نیست که چیزی را به اینجا دیکته کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/145732" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145729">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T95Rk6w9Dd34NDyaL46UV4xH3mmiKJAGjL-j_ugWB4a1Uogtc8Lnz2AJDiMHgPSPYFCyyrtr1fqR00EtvZzvcHCk_U1SNmeUkWJs0bk1zgZ1-tVlEvWinBHOVG60G7ixUYrh7TJH5groCoEwcMSjHdFSsmWT6E50sX3U062v8YO6xUafVqOTlkGM7DouG1l0Ma6BA4Y4YpYcQO730jwd1JnTlvdS0FEE1bE47amuJZKd0K0f_gd90ghnWII9h-mDASz9cbK2bHWaICArjvFd13j7t7nQ5AxfwgqctTtUAaIwo0pvkhrPsqEO_ugOCCHM6FNKEIwiP5sRbjca9gL24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXQIRAFN7BYHtfF5vVhU95m8Of1XwD_xpy-pVo5E6Dq7qIf2qju_uBk1ygf3EpnFWayxLaiq5UatwrUhS_C5_i5WbKmeNvr_B1T6IPZO2WXzbaqYYVDPcYTUBzY419dtsFv0WPs4OGebBPXKITi0Zy1JCF909ZPYskSMIXPUIROkGxtoxf2EcDpI6GelK3Ib8n_YaqmblbaeJajFvcCy41p7jrigYd8M7F6PW1-e49SJzk9dOuUuX5fOlto9C4ae4T0yEZzauZjbZXJwv6UoKlEFaNbmzBID1Zh8dkIhx0tO3jY_dd_Es8AepCeCMUyqQ0LK6NovDB2qP5eBEJM4fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1_ssWakZDYD4pYTP0qpwMtZ6vRVYPEbuk9d2Mz9dfZy0UhQfYL1gS-N_1cr0g8rvb-u7mN3HMeS2TjuGM_JBXv_6Tk1fw79-1fkTkZsLs1JwUo26dYuNVOyS1So-yorj8fHwiuldNXKlElp6H_MDrGSYgOtlB3r7a0V9Db_QHEaA98AjA1hAgTUHUeluzPL8UojBEq52DO5nQuZdBToEBT7c4OQzmAI3H7lKM4Agk-uwCtXZufSyz7RYeIfdhNEM-UbJm8-glOymZf5lQfYGFjXHWCwA9g6fv88vO6b4I18vKrbzGJNNBJQlgtUxBqZB4OdnOHAJ5zpKi84AJBDXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
استقبال نماینده روسیه از جرد کوشنر و استیو ویتکاف هنگام ورودشان به مسکو
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/145729" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145728">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سپاه : آمریکا و نیروهاش تو نظم جدید منطقه جایی ندارن و باید جمع کنن برن
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/145728" target="_blank">📅 15:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145727">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78ee8f011c.mp4?token=qC-p7-TLep_st3mgplAElRAxmnIqzzDSLZBTlAiko3aCjmzTgUu4KO4rRPerUrnm0tYLDzEErTeqA9ERcnXyvRfMq0oXTHIQreDwFn5-kxHoYmQjYg2WgkaxRhLVliMv-i-AtVDuFJcg00_bWU1Cxc_NNFsON1berIHKpuLAd4CqppHIU-HQ7R69fr0jWq5ZPIfEcwGcW07rCYQlQX6wCdPtxJthnIWNpXDIK8AXVZg1dOb6IimhTdHI1KRqUsdXlGGl3XKGNjaVlMOcRoTB5bM6NrRMfDnsDt_qPy0DQCK84BhwDGJOm-azG0Hv6e4RazXBK02UQoCSGkkkBHacUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78ee8f011c.mp4?token=qC-p7-TLep_st3mgplAElRAxmnIqzzDSLZBTlAiko3aCjmzTgUu4KO4rRPerUrnm0tYLDzEErTeqA9ERcnXyvRfMq0oXTHIQreDwFn5-kxHoYmQjYg2WgkaxRhLVliMv-i-AtVDuFJcg00_bWU1Cxc_NNFsON1berIHKpuLAd4CqppHIU-HQ7R69fr0jWq5ZPIfEcwGcW07rCYQlQX6wCdPtxJthnIWNpXDIK8AXVZg1dOb6IimhTdHI1KRqUsdXlGGl3XKGNjaVlMOcRoTB5bM6NrRMfDnsDt_qPy0DQCK84BhwDGJOm-azG0Hv6e4RazXBK02UQoCSGkkkBHacUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات مداوم اسرائیل به جنوب لبنان؛ این نهمین انفجار در این منطقه‌اس
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/145727" target="_blank">📅 15:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145726">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPRIJxmOvAkkpg8oMX94am4p9mz6U8AQVGBSCWcLWHTyz-y8l1Ed6u81kX1woS8Ng3UCnLT6jvlr380ZVAbDNY_pyQ0hoIpW7Fr3thUQwUx0vxTqOoUbSDJ1Y5v3_ciY8y-CYn4rHgFoB4LEzqsrxVU1scd4T3T7cQXuwWgcUBzAZnUKUyU2m3RqXZ3BI-oteJGZFYDnUpSVSYkIg01mu_YNuLcrVWMnhwYeXQ8OMUNykaMOxCWwquZmpfyPBvkyOkzgltnrR3hAEuxIarzmljzZR8nb7LSYSzwRgJ-2cCzUD-fNEcU8CZGQVaQBfdYXcUS3ygvxOiy40m0gnns3FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زمین لرزه در سقز و بانه احساس شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/145726" target="_blank">📅 15:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145725">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
خبرگزاری تاس: ویتکاف و کوشنر، فرستادگان ترامپ، با پوتین گفت‌وگو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/145725" target="_blank">📅 15:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145724">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
پوتین دستور توقف حملات به اوکراین را صادر کرد
🔴
به‌مدت سه روز هیچ حمله‌ای به کی‌یف انجام نشود؛ این تصمیم در چارچوب مقدمات سفر هیئت آمریکایی اتخاذ شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/145724" target="_blank">📅 15:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145723">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
قیمت دلار به 227 هزارتومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145723" target="_blank">📅 15:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145722">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
کاتز وزیر دفاع اسرائیل: ما منتظریم جمهوری اسلامی به تصرف ارتفاعات علی‌الطاهر واکنش نشان دهد تا از تعهد و محدودیت‌های ایجاد شده توسط ترامپ رها شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145722" target="_blank">📅 15:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145721">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409efd6aed.mp4?token=WJFY-n8QHBjAML1EnGm-ZyG9B8HjgZVKeu0ana-uuJwd1PE2TQ9znWc4jzGTKqWy_RQnel32marBCVRycCHFF6CzmFj99XvWu7_RiJAlQV7eUOW2zc671bKUncWxecH02gT1t4IIeayl9_PfG5npYhDDGJ8WjdW86Ag3rA5kcD-Fre7VOcEQN1R89zuZanxUKgoKrFF9UdWf6RYE4_WSLEsgzHYvY-7J-OfPnut1KaRSIlgtbG7CMyB7O0-HHZkriwXvvTnPFUWiQzEb8d2j4mjIg6RCGB3dIA5vEN4d6OY-1ey2yPuSgdtw4igg7W4e63jCcdUvQnPYWBksPtX5sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409efd6aed.mp4?token=WJFY-n8QHBjAML1EnGm-ZyG9B8HjgZVKeu0ana-uuJwd1PE2TQ9znWc4jzGTKqWy_RQnel32marBCVRycCHFF6CzmFj99XvWu7_RiJAlQV7eUOW2zc671bKUncWxecH02gT1t4IIeayl9_PfG5npYhDDGJ8WjdW86Ag3rA5kcD-Fre7VOcEQN1R89zuZanxUKgoKrFF9UdWf6RYE4_WSLEsgzHYvY-7J-OfPnut1KaRSIlgtbG7CMyB7O0-HHZkriwXvvTnPFUWiQzEb8d2j4mjIg6RCGB3dIA5vEN4d6OY-1ey2yPuSgdtw4igg7W4e63jCcdUvQnPYWBksPtX5sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: شب عید قراره کجا باشید؟
🔴
نتانیاهو: محرمانه‌ست، نمی‌تونم بگم.
🔴
خبرنگار: تا جایی که من فهمیدم، ظاهراً برنامه مهمی در پیشه؟
🔴
نتانیاهو: یه چیزی هست که داریم دنبالش می‌کنیم و زیر نظرش داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/145721" target="_blank">📅 15:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145720">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8e20512d8.mp4?token=omkciopy8wPtT5CcTDqRzLnn-xdCDeHie1OzRgcaYUGUaRUkvQFCcxK4uxjsQwBFlyqYGKR2EaVpNV2D4N2EbmRvrVvKs_Ozx3WoQo-8U-tuSc4Scv-VJCfqd4lhTG0ifTLVyh8zG2W4VArMfpOO4MYwCxYlsLqeE7EfvNhgpRAmy9i2Fy3_mz_u8qx6XZsWc4xd9IHKozT4cmdA3MO75Sbi59MvYz1S-Z5uPc8VCB-zSikxaDdK22NXpFSqobpi3fd4V6IPJ6tPC16jndl_2oyAbldIsLt729uHVn3U_d8H2Kb213tSv_eIYxZkD6ps-M9U-4Y1akFq-xIONCIi_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8e20512d8.mp4?token=omkciopy8wPtT5CcTDqRzLnn-xdCDeHie1OzRgcaYUGUaRUkvQFCcxK4uxjsQwBFlyqYGKR2EaVpNV2D4N2EbmRvrVvKs_Ozx3WoQo-8U-tuSc4Scv-VJCfqd4lhTG0ifTLVyh8zG2W4VArMfpOO4MYwCxYlsLqeE7EfvNhgpRAmy9i2Fy3_mz_u8qx6XZsWc4xd9IHKozT4cmdA3MO75Sbi59MvYz1S-Z5uPc8VCB-zSikxaDdK22NXpFSqobpi3fd4V6IPJ6tPC16jndl_2oyAbldIsLt729uHVn3U_d8H2Kb213tSv_eIYxZkD6ps-M9U-4Y1akFq-xIONCIi_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری نشان می‌دهد که نیروهای اسرائیلی در حال نصب مواد منفجره در داخل خانه‌ها در منطقه منصوری، واقع در جنوب لبنان، به منظور تخریب آن‌ها هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145720" target="_blank">📅 15:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145719">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/788ad0d7b0.mp4?token=N_qXsJDs2Rc5yQQ0jE5UKoDxqzqWnHWvFjbnVzwjjYQTjMq8UdFPW54165Y2HNeXvmYWXEXGVHoaLX_ag-97mAa4d2Q4rKbRjPWQJ5h7U_SRwJraJhkOyZKuOsG60aXxuiBR2OkSyO6DckjwJx1vE9-pqvq9pP5hVVuEjdzidi-T3YGesm5rXPIpQcfEJ5_EaM5C3srj8FaEN-W0JM2INsZo0tSjMfNe8POUo9shsKwawUrfHuGUUR8r3Ih78YeTRMX4iH-vwTW65dDcIcLcC0MBxWrgtrh8y3Dlln4PdDVJF8cuSZwFVCPhYpHO1x9wKVf-FZI7pR7T-zSR08pytw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/788ad0d7b0.mp4?token=N_qXsJDs2Rc5yQQ0jE5UKoDxqzqWnHWvFjbnVzwjjYQTjMq8UdFPW54165Y2HNeXvmYWXEXGVHoaLX_ag-97mAa4d2Q4rKbRjPWQJ5h7U_SRwJraJhkOyZKuOsG60aXxuiBR2OkSyO6DckjwJx1vE9-pqvq9pP5hVVuEjdzidi-T3YGesm5rXPIpQcfEJ5_EaM5C3srj8FaEN-W0JM2INsZo0tSjMfNe8POUo9shsKwawUrfHuGUUR8r3Ih78YeTRMX4iH-vwTW65dDcIcLcC0MBxWrgtrh8y3Dlln4PdDVJF8cuSZwFVCPhYpHO1x9wKVf-FZI7pR7T-zSR08pytw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: سوال اصلی در این انتخابات این است: چه کسی کارهایی را که باید انجام شوند، به پایان خواهد رساند؟ چه کسی بالاخره این رژیم را در ایران نابود خواهد کرد؟ چه کسی بالاخره حزب‌الله را نابود خواهد کرد؟ چه کسی بالاخره حماس را نابود خواهد کرد؟
🔴
مخالفان سیاسی من در برابر هر فشاری تسلیم می‌شوند. آمریکا به آنها می‌گوید "نه"، و آنها بلافاصله می‌لرزند.
🔴
آیا آنها این کار را انجام خواهند داد؟ نه. آنها این کار را انجام نخواهند داد. ما این کار را انجام می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145719" target="_blank">📅 14:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145718">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نیویورک‌تایمز: بنابر گزارش‌های اطلاعاتی آمریکا، ایران به توانایی خود برای حمله به اهدافی در خاورمیانه اعتماد بیشتری پیدا کرده و مصمم است برای تحت فشار قرار دادن ایالات متحده، این درگیری را ماه‌ها ادامه دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145718" target="_blank">📅 14:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145717">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1fae30cd0.mp4?token=PQjITn6NvOGSEdAfVyl52cL4rQDNZ3oQAXHEgOGBQF7dEY0QludEkDEwDbLo5tJqxZog7mVuBUAphG-vGKpLdeRZSdhnLP1vwZGq_hE0KLg4yOmOQnyUFJLfkbXVK5LZWKNVBGtTovsgDQMWM_XznvbK5p65XYhcSR2TNbp--zGcqEWOP69lZdt9AVgaCCk235Ha68Ff110VnBLHY0pLp-wOxJDmMuNv43PiF-6-eUxKJos6VXxZbbQrS7TZQp4AFUoP7QecWp9EvdimF_SDyONv0ieFCVMCoqT8sSEcH_C1GSeL2GcJG2zqifH7bc753XPJzfGgzTnrwpmTbRQUbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1fae30cd0.mp4?token=PQjITn6NvOGSEdAfVyl52cL4rQDNZ3oQAXHEgOGBQF7dEY0QludEkDEwDbLo5tJqxZog7mVuBUAphG-vGKpLdeRZSdhnLP1vwZGq_hE0KLg4yOmOQnyUFJLfkbXVK5LZWKNVBGtTovsgDQMWM_XznvbK5p65XYhcSR2TNbp--zGcqEWOP69lZdt9AVgaCCk235Ha68Ff110VnBLHY0pLp-wOxJDmMuNv43PiF-6-eUxKJos6VXxZbbQrS7TZQp4AFUoP7QecWp9EvdimF_SDyONv0ieFCVMCoqT8sSEcH_C1GSeL2GcJG2zqifH7bc753XPJzfGgzTnrwpmTbRQUbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نِتانیاهو درباره ایران: چه کسی در تاریخ ۷ اکتبر فکر می‌کرد که ما چهره‌ی خاورمیانه را تغییر خواهیم داد؟ من فکر می‌کردم.
🔴
نیت من این بود که در نهایت با ایران درگیر شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145717" target="_blank">📅 14:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145716">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
دریادار سیاری: ملت ایران به خود ببالد که مقابل دشمن مسلح به همه فناوری‌ها؛ ایستادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/145716" target="_blank">📅 14:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145715">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
نتانیاهو درباره غزه: بازسازی غزه فقط در صورتی امکان‌پذیره که ابتدا خلع سلاح انجام بشه. هنوز نمی‌تونم بگم چه نوع بازسازی‌ای انجام خواهد شد، چون در حال گفت‌وگو با دوستان آمریکایی‌مون درباره این موضوع هستیم.
🔴
گاهی اوقات دیدگاه ما با آمریکا یکیه، اما گاهی هم اختلاف نظر داریم. وقتی اختلافی وجود داشته باشه، آمریکا منافع خودش رو مطرح می‌کنه و من هم از منافع اسرائیل دفاع می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/145715" target="_blank">📅 14:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145714">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50080ba6b7.mp4?token=ZL54G5aQ2xf2eZ5b8iekfY6b7o9vgPJAXWRyRNuyuYaPOiQSzP-AVO_U6igenWgca4QUFgCgj73Q43_S7CSNRMJl5RdEnEOoQbijVVhXTFeAd3USqyZIqSLGwoo8jgUpX6JXIa5uS9vVmySDFaExYbc8NN6jGjeMpsUJMdtz55FQ5wLKqjTv6eObngoUnUnoDRFrUio5m48h-L6ClrEosZlBsSxD9oLg2-g9FqkgUa1JZQyUquamHujdbwYhYSdIAXXosY6inEEErNHgzN2m_Qb29YN171cGKOzXJWUR669A_6d6dqUy1Q8bzDnJJ0jf66wQBeBxvOCjxzbhw2eCiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50080ba6b7.mp4?token=ZL54G5aQ2xf2eZ5b8iekfY6b7o9vgPJAXWRyRNuyuYaPOiQSzP-AVO_U6igenWgca4QUFgCgj73Q43_S7CSNRMJl5RdEnEOoQbijVVhXTFeAd3USqyZIqSLGwoo8jgUpX6JXIa5uS9vVmySDFaExYbc8NN6jGjeMpsUJMdtz55FQ5wLKqjTv6eObngoUnUnoDRFrUio5m48h-L6ClrEosZlBsSxD9oLg2-g9FqkgUa1JZQyUquamHujdbwYhYSdIAXXosY6inEEErNHgzN2m_Qb29YN171cGKOzXJWUR669A_6d6dqUy1Q8bzDnJJ0jf66wQBeBxvOCjxzbhw2eCiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسن روحانی: به مردم بگوییم قرار ما این است با قدرت‌های بزرگ بیست سال دیگر بجنگیم، اگر مردم قبول کردند برویم ادامه بدهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145714" target="_blank">📅 14:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145713">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63fa90f779.mp4?token=PMKavym1ARQYCRZDwl06LoLUiMFQsC-X7tVOdnbTKeuWKZsftrohVCgiwGCqP5638AfQxqwRkqpmpd-mUTgZI92zmElEqPz1ZuIUczqio42xOV06QjO64LTL4WKl10oJHM6029qzt53UoabJIycmtoGsg4v18XwpPCacfj89iW8KMK3dr8tFHaeNzvhKkfWCmxCwYZgsaEXlb0IftJOHjgtTDz9AL2FxAMz16MlPMLpNNk2ZxK6zgbIu0fER0jlxr9pKRSEogWOzMqrQZ_NrlqnhQLaNk3HYyjJp2dE4r0HgWtDQXJWyu6sZx42blf2ZpBv9GJhHxzR24GGdS9Qyhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63fa90f779.mp4?token=PMKavym1ARQYCRZDwl06LoLUiMFQsC-X7tVOdnbTKeuWKZsftrohVCgiwGCqP5638AfQxqwRkqpmpd-mUTgZI92zmElEqPz1ZuIUczqio42xOV06QjO64LTL4WKl10oJHM6029qzt53UoabJIycmtoGsg4v18XwpPCacfj89iW8KMK3dr8tFHaeNzvhKkfWCmxCwYZgsaEXlb0IftJOHjgtTDz9AL2FxAMz16MlPMLpNNk2ZxK6zgbIu0fER0jlxr9pKRSEogWOzMqrQZ_NrlqnhQLaNk3HYyjJp2dE4r0HgWtDQXJWyu6sZx42blf2ZpBv9GJhHxzR24GGdS9Qyhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرود یک فروند هواپیمای نظامی آمریکایی در فرودگاه بین‌المللی اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/145713" target="_blank">📅 14:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145712">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec68e65f4.mp4?token=NpzhexPKLRN-CNfZei_HFYFY2TXIDOccpFGESqfxbYHaFg5TzE2g_-cKp3U9wjd9T4PUUKhHCjSPDSIqM7hTzjQkIYmDPTlgM7fgrolrnW81Zcr1rMNvDelFTCCiE3K__eESBbuvTiiFsCt7XbV9okHasKfVgcvO-f3xRPY986v_HQaidvDATMVMfSsSPv8TnGXMVDz8CAo5_n8dKLuyFa45GzFyoBp70_YPQNJGxmZfSTXa31jzwL5Rnnbo_SgRC5H8ajYh-zZHyrjmgGrzObbIsuZj0isi0x7dU9hKESqrYkXrQ4Pl5SSLFDSD7mr48jqVumF4qNWgaAyrsS7igw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec68e65f4.mp4?token=NpzhexPKLRN-CNfZei_HFYFY2TXIDOccpFGESqfxbYHaFg5TzE2g_-cKp3U9wjd9T4PUUKhHCjSPDSIqM7hTzjQkIYmDPTlgM7fgrolrnW81Zcr1rMNvDelFTCCiE3K__eESBbuvTiiFsCt7XbV9okHasKfVgcvO-f3xRPY986v_HQaidvDATMVMfSsSPv8TnGXMVDz8CAo5_n8dKLuyFa45GzFyoBp70_YPQNJGxmZfSTXa31jzwL5Rnnbo_SgRC5H8ajYh-zZHyrjmgGrzObbIsuZj0isi0x7dU9hKESqrYkXrQ4Pl5SSLFDSD7mr48jqVumF4qNWgaAyrsS7igw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: اونا می‌تونن به ما حمله کنن و ما هم پاسخ می‌دیم.
🔴
متوجه شدید ایران داره به همه شلیک می‌کنه؟ به کی شلیک نمی‌کنه؟ فقط اسرائیل.
🔴
چرا؟ چون دقیقاً متوجه حرف من هستن؛ تا وقتی من نخست‌وزیرم، چنان ضربه‌ای بهشون وارد می‌شه که حتی نمی‌خوام جزئیاتش رو بگم. این ضربه از قبل آماد
شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/145712" target="_blank">📅 14:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145711">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
زاکانی: به دنبال تولید برق با انرژی اتمی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/145711" target="_blank">📅 14:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145710">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
پارلمان پاکستان برای نخستین بار به عاصم منیر اختیار قانونی فرماندهی هر سه نیروی ارتش، نیروی دریایی و نیروی هوایی را اعطا کرد
🔴
دوره فرماندهی او دست‌کم تا سال ۲۰۳۰ ادامه خواهد داشت
🔴
وی در مقام «فیلد مارشال»، مصونیت قانونی خود را تا پایان عمر حفظ می‌کند و برکناری او تنها با رأی دو سوم پارلمان امکان‌پذیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145710" target="_blank">📅 13:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145709">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وال استریت ژورنال: تحریم‌های اعمال‌شده توسط آمریکا از تیرماه گذشته، ایران را از صادرات نفت بازداشته است.
🔴
مسدود کردن تنگه هرمز توسط ایران، ترامپ را مجبور به پذیرش شرایط آن نکرد.
🔴
رهبران ایران انتظار دارند که این وضعیت (احتمالاً تحریم‌ها یا بحران اقتصادی) تقریباً به مدت پنج ماه ادامه داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145709" target="_blank">📅 13:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145708">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
پزشکیان: وقتی جوان ما در خیابان مشکل دارد مقصر ما هستیم/ درنگاهی که داریم باید تجدید نظر کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145708" target="_blank">📅 13:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145707">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ccdbf8531.mp4?token=s94PBPEFk2W1Lxt8Sd5rzDgjCk-8XxPqCow_ol3kQBIsa413J1eM2KPC5UKtwVbvjdn6XCtRDDsIVukvsh_lyiFUDtV923HO-uy5J0WyMkY7feV3w3IIbRuoa_Ci36V4hLBOwEiDnEi5Kp8A3ETSjycp9foH6MN1S24VD8vMzAATP34F1gv54XE5m6ozw7a9g1pxpc32yDBFU3cpGB2x6uUYO_LAoo14NV3ckaKDh53ekE6HyqdrmfYR4npoh76QCaDqpBRk6NW26oVRIAowhRJPXxZsoelAucFqGBCBTBLIR3zt7uMYGedwIhe-exEsPvOR1o4r3gDQBngnOd6ADA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ccdbf8531.mp4?token=s94PBPEFk2W1Lxt8Sd5rzDgjCk-8XxPqCow_ol3kQBIsa413J1eM2KPC5UKtwVbvjdn6XCtRDDsIVukvsh_lyiFUDtV923HO-uy5J0WyMkY7feV3w3IIbRuoa_Ci36V4hLBOwEiDnEi5Kp8A3ETSjycp9foH6MN1S24VD8vMzAATP34F1gv54XE5m6ozw7a9g1pxpc32yDBFU3cpGB2x6uUYO_LAoo14NV3ckaKDh53ekE6HyqdrmfYR4npoh76QCaDqpBRk6NW26oVRIAowhRJPXxZsoelAucFqGBCBTBLIR3zt7uMYGedwIhe-exEsPvOR1o4r3gDQBngnOd6ADA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: همیشه می‌شود بهتر شد، بهتر دید، بهتر فکر کرد، بهتر مدیریت کرد، بهتر کار کرد و با هزینه کمتر، باکیفیت‌تر عمل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145707" target="_blank">📅 13:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145706">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
مدیرعامل شرکت ملی گاز: ایران در میان تنها ۶ کشور جهان با روند افزایشی شدت مصرف انرژی قرار دارد و باید حساسیت نسبت به مصرف حامل‌های انرژی در بخش خانگی افزایش یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/145706" target="_blank">📅 13:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145705">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5747cd754f.mp4?token=D6JPVDTwUGfu5obNAxKnuCCdrVV5p2c39A-rEG858AXnSiIz69h2A853GiClK4srRtNESpNAESC3hLzdTZv1nGwxIJD5D2Mg9J9s3m80ITHizYDLH93uJSlbEp9V3ZzFXCcj1AJfpp6Eb_NejdoMzn_McTSfbTfZca9sfmNmvG9akE3VNFYCEN1LpEcEBHh7DxpDrzQMDMMqGsQhf4zp-kcxdT8fiNE_ubG2qSnJhqrxoNfbUkUHnR_cmgK787W2j-joVsbs32HQ32eja6muTqw4H9m4V3PS5dT6Yvs_BhaXrPPOamZRvneXZfkDtbXq7L0nSEiAZOkV-l4x6nsZFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5747cd754f.mp4?token=D6JPVDTwUGfu5obNAxKnuCCdrVV5p2c39A-rEG858AXnSiIz69h2A853GiClK4srRtNESpNAESC3hLzdTZv1nGwxIJD5D2Mg9J9s3m80ITHizYDLH93uJSlbEp9V3ZzFXCcj1AJfpp6Eb_NejdoMzn_McTSfbTfZca9sfmNmvG9akE3VNFYCEN1LpEcEBHh7DxpDrzQMDMMqGsQhf4zp-kcxdT8fiNE_ubG2qSnJhqrxoNfbUkUHnR_cmgK787W2j-joVsbs32HQ32eja6muTqw4H9m4V3PS5dT6Yvs_BhaXrPPOamZRvneXZfkDtbXq7L0nSEiAZOkV-l4x6nsZFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای یمنی (حوثی ها ) در حال حاضر به سمت مواضع و تجمع‌های نیروهای وفادار به عربستان سعودی در حرکت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/145705" target="_blank">📅 13:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145704">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBrhLWvWURK4QRmWxnGTq8XyNE3htmVbPFQ2fuZFkX7Jbzr76UEgIU_0VoeUJ9ZcghZluIHR-WZAiU0oixrWdrsUMjutyrE2NFhpcQvrwXr-pAQ3AgHZUT4FQWMgu2L6QLpANb0h7TPKlUpmb3g8U2erYLpqfgpgbaDdjt9eMtj0pbP9YtJtuCdWDrRa_5G5Gb0bHkIHmnwKJ_ntPKyxqkBcno0dbgONHxayZmCy4nav6NlW5L-kQRjckt7YXp3bRAdfsvrZC-4HvEtE3D9BAVGr5eUSn7KrS6Vmo4DJrtBhzmgPfwxHv6z5yeZ5QLuLkXiRKB6xtbcLSYRH4LOIzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر جدید از چین، یک پهپاد بزرگ و پنهانکار با نام غیررسمی WZ-X را نشان می‌دهد که دهانه بال آن حدود ۵۲ متر، هم‌اندازه بمب‌افکن B-2 آمریکا، برآورد شده است
🔴
این پهپاد احتمالاً برای ماموریت‌های شناسایی و مراقبت در ارتفاع بالا و پروازهای طولانی‌مدت طراحی شده است. گفته می‌شود این پرنده توانایی پرواز در ارتفاع بیش از ۱۸ کیلومتر را دارد و برد آن به حدود ۱۹ هزار کیلومتر می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/145704" target="_blank">📅 13:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145703">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
عارف، معاون اول پزشکیان: مشکلات اقتصادی قابل حله؛ مفتخریم که در تمامی زمینه‌ها به خودکفایی رسیدیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/145703" target="_blank">📅 13:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145702">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8814fb781.mp4?token=BvsZaJZRtRwn7AaWplzuWny1oLcxLls8W1FwJS3hEuenTDOfbum49QkCEcPVL83sGDPTBtlj9Xkes7HEG6xwK-6YwbCnduXe2-rZpx9UD6xceEeXo98ZBQT7inEQn6N0pcLglWGZvEtMVkFEH-xYpKRXCLnM0c9k-f_rxodTIftUp6TKSVOTMU0Lg2b1Q9HRaY3fZCqw4zOss2aFEpFODZcI_I9af93JBpJDqUR2PqmxAcmIyv4GAyr8gA9gG6-WJ6Cdgml21xeSHfnHHCyd6tshCgp3GC54P-ZGPTofW9N1dbE1JywuCbe7ei1MmMUZGaRcSRQA4KYjtkkAMtGHu7O6I6qT3sOIIE8vlO9DPJ0upNNkuS5V37GuJKi8coPNGX1sWhOoTYe-LOVuFxsdVTNkhQCxm3ai37JAbAD4ZNXkXsWW8d6hOHLyqu_KEOYveD1yWs8tUXBneBwzHr59K6KFrxc6kZKIywOKdxms1Ye17DqGItGcWAfs7hDkyyX6p-aYEy4C9Hq3TZLe2byGhuivCY48iQhFaZaw5l1vp8jOETkn689g7_3ihLdD0T3cuuNyk4mII1GDKcXjVBiAvODMQpewXH8U_q8XMVaPj5GoJ-SkFchLkRnbpClxPGjJ0ajUylrV9i6kQLkvrEkQxcface-nfZKzfpQ2uwjx9Wo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8814fb781.mp4?token=BvsZaJZRtRwn7AaWplzuWny1oLcxLls8W1FwJS3hEuenTDOfbum49QkCEcPVL83sGDPTBtlj9Xkes7HEG6xwK-6YwbCnduXe2-rZpx9UD6xceEeXo98ZBQT7inEQn6N0pcLglWGZvEtMVkFEH-xYpKRXCLnM0c9k-f_rxodTIftUp6TKSVOTMU0Lg2b1Q9HRaY3fZCqw4zOss2aFEpFODZcI_I9af93JBpJDqUR2PqmxAcmIyv4GAyr8gA9gG6-WJ6Cdgml21xeSHfnHHCyd6tshCgp3GC54P-ZGPTofW9N1dbE1JywuCbe7ei1MmMUZGaRcSRQA4KYjtkkAMtGHu7O6I6qT3sOIIE8vlO9DPJ0upNNkuS5V37GuJKi8coPNGX1sWhOoTYe-LOVuFxsdVTNkhQCxm3ai37JAbAD4ZNXkXsWW8d6hOHLyqu_KEOYveD1yWs8tUXBneBwzHr59K6KFrxc6kZKIywOKdxms1Ye17DqGItGcWAfs7hDkyyX6p-aYEy4C9Hq3TZLe2byGhuivCY48iQhFaZaw5l1vp8jOETkn689g7_3ihLdD0T3cuuNyk4mII1GDKcXjVBiAvODMQpewXH8U_q8XMVaPj5GoJ-SkFchLkRnbpClxPGjJ0ajUylrV9i6kQLkvrEkQxcface-nfZKzfpQ2uwjx9Wo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استقبال و بوسیدن دست اژه ای توسط هندیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145702" target="_blank">📅 13:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145701">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
پزشکیان:باید کاری کنیم دشمنان طمعی در این مملکت و آب‌وخاک نداشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/145701" target="_blank">📅 13:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145700">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
زنسکی:روسیه امروز به فرودگاه‌های کیف و بوریسپیل در اوکراین حمله کرد، این در حالی است که قرار بود نمایندگان ترامپ از این کشور بازدید کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145700" target="_blank">📅 13:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145699">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1acc0d88.mp4?token=VayU75M1N_4CkqtBcp3L8xT9fbboo0TrAUgvY2psFx53bn6pU_eY7bZswQmqkZHeTJO49cjGtFE1-F_53MnB2FqRpheSHeDVWpt7TWPk1y8jBOVTIenB5DYr_mkvTxR9qoCWnbydOBRejijVs07iyCJxn8yhHGJ179kdD3roQ_YPXDc-KMtk5E7vF5rYPcyfj58zEYpADm-4VM-L3HWUN5vy5n51twGaUq_pEIQXNHIyIeerBr35FPix4pPFHMxZKhFXwFPGkH17dwuzC76FqkhaHosGtGdMgjJ4imuSE6l31ijw7bHTZg1aUUdj6Zy-OZzBXPapkw9p8BBN-tbQ5JQslc_WRDW07OnwYONjcJrN41h3gG5V-TTRDOhPkgyRBczwTdbG-v5-V2wg3zhJWzKwn3jOH8Tp7pgn2wInX_6zXlgIpahKi0gN-evZ-sxvcqqso6_Z1Li0NFeOtdKxLycbeIlmRTnv8MKl7kGH0t8cRMXrXU2RizuYbDRaB_IQCv4PaJIAttj7AsJqlXZB5pb7Qh9pP5XN5qSaxJC2ftvdlCqr112_lf2pi4munzafCK63L0Jt_zipq92RB0Sz7mY0yHoj4CKTXimrrv2n5yUHvemxeFNs1GF9Be_ZSsGZOLJbtx_AlARRaYlK_La61i_O_e9zOpSOZ6rOjbVagw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1acc0d88.mp4?token=VayU75M1N_4CkqtBcp3L8xT9fbboo0TrAUgvY2psFx53bn6pU_eY7bZswQmqkZHeTJO49cjGtFE1-F_53MnB2FqRpheSHeDVWpt7TWPk1y8jBOVTIenB5DYr_mkvTxR9qoCWnbydOBRejijVs07iyCJxn8yhHGJ179kdD3roQ_YPXDc-KMtk5E7vF5rYPcyfj58zEYpADm-4VM-L3HWUN5vy5n51twGaUq_pEIQXNHIyIeerBr35FPix4pPFHMxZKhFXwFPGkH17dwuzC76FqkhaHosGtGdMgjJ4imuSE6l31ijw7bHTZg1aUUdj6Zy-OZzBXPapkw9p8BBN-tbQ5JQslc_WRDW07OnwYONjcJrN41h3gG5V-TTRDOhPkgyRBczwTdbG-v5-V2wg3zhJWzKwn3jOH8Tp7pgn2wInX_6zXlgIpahKi0gN-evZ-sxvcqqso6_Z1Li0NFeOtdKxLycbeIlmRTnv8MKl7kGH0t8cRMXrXU2RizuYbDRaB_IQCv4PaJIAttj7AsJqlXZB5pb7Qh9pP5XN5qSaxJC2ftvdlCqr112_lf2pi4munzafCK63L0Jt_zipq92RB0Sz7mY0yHoj4CKTXimrrv2n5yUHvemxeFNs1GF9Be_ZSsGZOLJbtx_AlARRaYlK_La61i_O_e9zOpSOZ6rOjbVagw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF): حملات هوایی علیه آنچه «مراکز نگهداری تسلیحات متعلق به حزب‌الله» در جنوب لبنان خوانده شده، انجام داده است
🔴
ارتش اسرائیل مدعی شد این حملات یک «تهدید فوری» را از بین برده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/145699" target="_blank">📅 12:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145698">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7425ddc2e6.mp4?token=arcr82_2d8z-45zIWNMModgd1apfVLPugnmEw2VPDRDRg3PB1vaOyL1_vMwFPCtHUdRpK9hAPdRPUBxFkDKbOTxYYDLa4taNlV0tJyqF6yO_H2APml2R9jwz3W8bS4xTwUPW5VSH3p4eCNJWml4bMQl9sgNUUqBP7AIeSEgIIg2z8X3_wdmS035xZPEz36cDpdMk4du-U99Apj2Utxg_luXhx4G5TzT8Iei73jw9hC_dl5BLP_8N7ps5bNvgT6wiPaHZRSw414Ii5tNY7QTY6L3sh7wHBfqIK-kLeEfWBwLRqILwhI6PQo52BUHSS7MmHij0h-q-feStUNqkSPQuVAhjSsxoX_YPF3JwWvsT8NgPsWEp8-IWQATyEfqe8oLMog3NH9dvByj5aysaCXZDcscRMLlmAOvZaK3GsG3ct1WGASPnHkZrcp1SozsdxmrBcyeCpDrCQ6GUcUCIk_t8eMZPpyYB6UfWJ6Dhgx9ZI9831VWV6G3Y-GOdvZ6SZQ_qnYEdnhJV12OmnIgFaUJS4O84WLobYpfx0_MWaBr0kNiEqItC5JV9ksZgdDK11rxtUeaJG-hNhiT45lvzv5J2IxAmgZ4ryTnd13gt2FtnluLwtcXH5wsjjBHQyeP52go_9E2lDkCir-X3OcnP7sOpcA399JnAcfLWVV5DWermwu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7425ddc2e6.mp4?token=arcr82_2d8z-45zIWNMModgd1apfVLPugnmEw2VPDRDRg3PB1vaOyL1_vMwFPCtHUdRpK9hAPdRPUBxFkDKbOTxYYDLa4taNlV0tJyqF6yO_H2APml2R9jwz3W8bS4xTwUPW5VSH3p4eCNJWml4bMQl9sgNUUqBP7AIeSEgIIg2z8X3_wdmS035xZPEz36cDpdMk4du-U99Apj2Utxg_luXhx4G5TzT8Iei73jw9hC_dl5BLP_8N7ps5bNvgT6wiPaHZRSw414Ii5tNY7QTY6L3sh7wHBfqIK-kLeEfWBwLRqILwhI6PQo52BUHSS7MmHij0h-q-feStUNqkSPQuVAhjSsxoX_YPF3JwWvsT8NgPsWEp8-IWQATyEfqe8oLMog3NH9dvByj5aysaCXZDcscRMLlmAOvZaK3GsG3ct1WGASPnHkZrcp1SozsdxmrBcyeCpDrCQ6GUcUCIk_t8eMZPpyYB6UfWJ6Dhgx9ZI9831VWV6G3Y-GOdvZ6SZQ_qnYEdnhJV12OmnIgFaUJS4O84WLobYpfx0_MWaBr0kNiEqItC5JV9ksZgdDK11rxtUeaJG-hNhiT45lvzv5J2IxAmgZ4ryTnd13gt2FtnluLwtcXH5wsjjBHQyeP52go_9E2lDkCir-X3OcnP7sOpcA399JnAcfLWVV5DWermwu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از آتش‌سوزی روز گذشته کوچه برلن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145698" target="_blank">📅 12:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145697">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY1eB6cPNPM2LEXRN7m-NUlmYNufX5yS5TA0oFfW9rkHcCWEckYvyhabm_mB0tpBJvF6xZfEdsAmgfXbiCnnsnEz1S0XYxeFaavBSbTCfWsr04FMeL03GITqXg3fzrl_MWLwhJQxap5Bspogv6iS9PsI0Fe7rH8WvV2qmcoCuU97K0N7ZivQJZLXBgaAZvSEosxPsqOAZD8nIpiWy4aMl9SwwhPOIaFWr4pdGWWNMeWPUZdlH5p6XJxUzMYGWW85FQUYpr7XUbDoaK79OpfWNVUCtETXswFTn4vTTAX7BdsBt58TXddOh5zrHxYF4d_8AQQP9IzUCktkBsDLbT8FEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی ایالات متحده به سرعت در حال بررسی گزینه‌های جایگزین برای هواپیماهای بدون سرنشین MQ9 است، زیرا گزارش‌ها نشان می‌دهند که این نیرو حدود 50 فروند از این هواپیماها را، معادل 25 درصد از کل، در جریان جنگ با ایران از دست داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145697" target="_blank">📅 12:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145696">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWudpCOJAKY0c1TYNuvZTYgJ3mpNBHmtJb7D9QWni7ekp1o2QI3fe4hXTOFXxuZRLjWHbP3pgeHcCbHbBWjViYELEJ6NkdDCpr7tyN6WRist61Mo_9Rl4Lggz2ynmC-5Fhv5xHA-lvj2W3gNC75YWhUotj0dM1_vGLknD2U3QuFpU_boNo9kZiHSKuXI5mSa8GO5WL4K5_gp8Lbyc-Elsdg6N0Wli4UOCLwg_P2YXDhHikROAOKQQLmnh8y3Kh3K8psZ6lWVH4x-MxP3U318tgAKpzBQl_Vzchn48TR-zCSQIj_sivp1lC_K1zOHwnpeUX8lN0hX1D1ui5aucIB3TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رصدهای تانکر ترکرز نشان میدهد که دیروز روز بسیار شلوغی در  انتقال نفت خلیج‌فارس از تنگه هرمز بوده است ، ۲۴ میلیون بشکه نفت ، LNG و LPG با روش کشتی به کشتی در دریای عمان تحویل داده شدند. تانکرهای حامل نفت دیگری هم در دریای عمان رصد شده‌اند که در انتظار یک کشتی برای تخلیه بودند. همچنین حداقل ۷/۲۵ میلیون بشکه نفت به اضافه دو تانکر LNG در خلیج‌فارس در انتظار چراغ سبز سنتکام بودند تا با اسکورت آن‌ها از تنگه هرمز عبور کنند. در مجموع چیزی حدود ۴۰ میلیون بشکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/145696" target="_blank">📅 12:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145695">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ویتکاف و کوشنر، دو فرستاده رئیس‌جمهور آمریکا وارد مسکو شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145695" target="_blank">📅 12:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145693">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=kulchPVVnd4dFbRyrVpCRkcG6JtPd9Q8vZucW73JOW6GQiJxSnoCPHW18nr8mnE10bTK56cWWakzi4TVInYhuPCSZ9TfuGdpr6zYu4gTJbOL-sX2nCd6jCED3vsiFwcCQlO20fvQkXpV1XeBE4SfcFLMF-IIypLi1SXmU46NvVDfk1rTamKe5c3RQDgyMGVo-hVClRd3jlTanB-4lv5HFAMZ1-hqp3zMAo6CW3X3GIWOo1CxzSXiNiBHu94gy5g2nGXdxkisMIk1892Xm3WdwHvjokQVN9jwYpfcUDpmiFNPRhmyA9lFuJNuJwqNPeQtsYANM1_N1VJCA1L-qHQ2dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=kulchPVVnd4dFbRyrVpCRkcG6JtPd9Q8vZucW73JOW6GQiJxSnoCPHW18nr8mnE10bTK56cWWakzi4TVInYhuPCSZ9TfuGdpr6zYu4gTJbOL-sX2nCd6jCED3vsiFwcCQlO20fvQkXpV1XeBE4SfcFLMF-IIypLi1SXmU46NvVDfk1rTamKe5c3RQDgyMGVo-hVClRd3jlTanB-4lv5HFAMZ1-hqp3zMAo6CW3X3GIWOo1CxzSXiNiBHu94gy5g2nGXdxkisMIk1892Xm3WdwHvjokQVN9jwYpfcUDpmiFNPRhmyA9lFuJNuJwqNPeQtsYANM1_N1VJCA1L-qHQ2dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از نفتکش هدف قرار گرفته توسط آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145693" target="_blank">📅 12:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145692">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سپاه: صدای انفجار در دماوند استان تهران مربوط به برنامه‌های رزمایشی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/145692" target="_blank">📅 11:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145691">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de9af4ecb.mp4?token=Z13bVTpBGDvLbrws6HPQrWVkedAkIw3tuULJ9G1szisVRqAEspndLz54cDF-y_osiqvjsCQdMj_UTN84I6ydGYhIOrZdoMxgXBkjWhHrTZBXHYPAwfbDqZYlM2D_SESW1C5SdjC3-ox7AcMm1x8_AuMq0yTIeKkzQKy89BTyi2_SaF0t25v9om_HCJxJAzPkQAoZ_L9Pa8sv-x4hOSqPpKf47x5NKztpG6YdfKkN9sPtUyXLj2mX1PdR0-KfA-5-0Aa_tMRroE-BJwl0gcnmh_Fg4eMIXFb7QsBUuK-f2f7hcywNFNcggdzhbqd8eVGARvRWeih30_Oh2pPzUj0g3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de9af4ecb.mp4?token=Z13bVTpBGDvLbrws6HPQrWVkedAkIw3tuULJ9G1szisVRqAEspndLz54cDF-y_osiqvjsCQdMj_UTN84I6ydGYhIOrZdoMxgXBkjWhHrTZBXHYPAwfbDqZYlM2D_SESW1C5SdjC3-ox7AcMm1x8_AuMq0yTIeKkzQKy89BTyi2_SaF0t25v9om_HCJxJAzPkQAoZ_L9Pa8sv-x4hOSqPpKf47x5NKztpG6YdfKkN9sPtUyXLj2mX1PdR0-KfA-5-0Aa_tMRroE-BJwl0gcnmh_Fg4eMIXFb7QsBUuK-f2f7hcywNFNcggdzhbqd8eVGARvRWeih30_Oh2pPzUj0g3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری‌هایی بین نیروهای مسلح یمن و نیروهای وفادار به عربستان سعودی در جنوب شهر حدیده در جریان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/145691" target="_blank">📅 11:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145690">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری / فارس: دقایقی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارک شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145690" target="_blank">📅 11:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145689">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سخنگوی شورای نگهبان: طرح جدید مهریه در نوبت بررسی شورای نگهبان قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/145689" target="_blank">📅 11:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145688">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
این شخص غلامرضا قاسمیان است کسی که یه مکانی درست کرده به نام پناهگاه زنان خیابانی که اونجا زنان رو جمع میکنه تا خدمات جنسی بدن! و اسمشم گذاشته شلتر
🔴
قاسمیان در این ویدیو میگه خودمم اینجا میرم و میام
🔴
صدا و سیما هم یه هفته هست اینو هی میاره تو آنتن زنده…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/145688" target="_blank">📅 11:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145687">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
راه آهن کشور اعلام کرد ترکمنستان و قزاقستان با تبعیت از تحریمهای جدید آمریکا مانع انتقال ریلی کالا از چین و روسیه به ایران شده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/145687" target="_blank">📅 11:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145686">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
خبرگزاری المعلومه: منابع امنیتی اعلام کردند روند خروج نیروهای آمریکایی از پایگاه هوایی الحریر در اقلیم کردستان ادامه دارد و انتظار می‌رود این پایگاه تا پیش از هشتم مهر ماه آینده به طور کامل تخلیه شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145686" target="_blank">📅 11:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145684">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
روحانی: الان مردم در تعیین سیاست‌ها و آینده هیچ نقشی ندارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/145684" target="_blank">📅 11:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145683">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=OQNOJpszzSP39hVAm-5rFiob9GMgNmnWp1xjZ2KI2k4EfsDtaHigPCQlFESdVFJKjN5GtCa8HJq1-HNt5uJJpPHboGJ6CtImHvIxFcSdmghTIp_xUTDSThBRudP8EdaKl7rkXiA9uIL2noadp1A1KDY3j4toMz-qrK_DSawn99K65ESNCt4tVzsk2ioyi065fvvo8C0al-A_d0cEosDBmZJoXqQTvctQuMe8UczRhGzevFMhgFfMQ-Gc3Ggzya2QXAAHyFSTYOpPjUVGk6YTuwroSe26U_a4-_sTYCsD4F_m8JJ5nLbpVJV2sZFhjm0I-mJCJJKq-EoJnU_fnps15w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=OQNOJpszzSP39hVAm-5rFiob9GMgNmnWp1xjZ2KI2k4EfsDtaHigPCQlFESdVFJKjN5GtCa8HJq1-HNt5uJJpPHboGJ6CtImHvIxFcSdmghTIp_xUTDSThBRudP8EdaKl7rkXiA9uIL2noadp1A1KDY3j4toMz-qrK_DSawn99K65ESNCt4tVzsk2ioyi065fvvo8C0al-A_d0cEosDBmZJoXqQTvctQuMe8UczRhGzevFMhgFfMQ-Gc3Ggzya2QXAAHyFSTYOpPjUVGk6YTuwroSe26U_a4-_sTYCsD4F_m8JJ5nLbpVJV2sZFhjm0I-mJCJJKq-EoJnU_fnps15w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار 223000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/145683" target="_blank">📅 10:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145682">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وال‌استریت ژورنال: در بحبوحه افزایش تنش‌های تجاری میان آمریکا و کانادا، به بخش ضدانحصار وزارت دادگستری آمریکا برای مدت کوتاهی دستور داده شد همکاری با مقام‌های کانادایی را متوقف کند.
🔴
در یک ایمیل داخلی از کارکنان خواسته شده بود همکاری در پرونده‌های مشترک و تعاملات سیاست‌گذاری با کانادا را متوقف کنند؛ اما وزارت دادگستری بعداً اعلام کرد این دستور ناشی از یک سوءتفاهم بوده و دستور اولیه تنها مربوط به تعویق یک جلسه برنامه‌ریزی‌شده بوده است.
🔴
مقام صادرکننده این دستور بعداً آن را اصلاح کرد و به کارکنان اعلام شد که همکاری با کانادا می‌تواند ادامه پیدا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145682" target="_blank">📅 10:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145681">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سازمان غذا و دارو: واکسن آنفلوانزا از اواخر شهریور و اوایل مهر در دسترس قرار می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145681" target="_blank">📅 10:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145680">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رویترز: کاخ سفید گزینه‌هایی را برای جایگزینی استیو فاینبرگ، معاون وزیر دفاع آمریکا بررسی کرده است
🔴
با این حال، هنوز تصمیمی گرفته نشده و کاخ سفید و پنتاگون می‌گویند فاینبرگ در حال برکناری یا کنار گذاشته شدن نیست.
🔴
کناره‌گیری احتمالی او می‌تواند به موج اخیر تغییرات در رهبری پنتاگون اضافه شود؛ آن هم در شرایطی که نگرانی‌ها درباره کمبود تسلیحات و ظرفیت تولید مهمات افزایش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145680" target="_blank">📅 10:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145679">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
یورونیوز: نظرسنجی‌ها نشان می‌دهد سیاستمدار راست‌افراطی مارین لو پن در مسیر تبدیل شدن به رئیس‌جمهور بعدی فرانسه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145679" target="_blank">📅 10:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145678">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
بانک ترکیه: علیه تحریم‌های آمریکا اقدام قانونی خواهیم کرد
🔴
الجزیره اعلام کرد: پس از آنکه وزارت خزانه‌داری آمریکا بانک ترکیه‌ای «گلدن گلوبال» و دو نهاد زیرمجموعه آن را به بهانه ارتباط با ایران تحریم کرد، این بانک اعلام کرد که علیه این تحریم ها اقدام قانونی انجام خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145678" target="_blank">📅 10:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145677">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
طبق گزارش منابع محلی : نفتکش هدف قرار گرفته‌شده در جزیره خارک، یک نفتکش کوچک بوده است.
🔴
بر اساس این گزارش، این حادثه تلفات جانی نداشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145677" target="_blank">📅 10:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145676">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری / فارس: دقایقی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارک شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/145676" target="_blank">📅 10:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145675">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری / فارس: دقایقی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارک شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145675" target="_blank">📅 10:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145674">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
تتلو: مردم منو فراموش کردن، چطور دلتون اومد؟ حتی اونایی که تو پلی لیستشون هستم هم فراموشم کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/145674" target="_blank">📅 10:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145673">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4411422981.mp4?token=gMl7H-o24Qj3tHT2yw9g0xaMUPUY7tTwHONtUmlhIOQLoFKGfztsTPbG08CUYyaCPm6CCsW0ZXKd4PZvdLeJfFJNEyf3JMiPKDMVbHEF9Kz6Tk05SKV3WQmvbnBOc6gpuskMViU9Z0xepapadG2_i_LBMSryURpKwgp5Vk9e0hQzZAYKWDrMlCy7yd2qB4G0pWMq-Ht_n9iCpPLZecLFtX_iXLN_Jk1MG1Z48PSxv8AE84YB0UDEt9ABtSypQ6Gb9fzeyxk4uqiYe-lpek8R-u3LIVZtGvvLSIs1PhiQ9vOrl7zKRcaWY-XooDBiEme8gAHFStCHfUj2Wr9Av-YShUDh0_eyTNyEwKdZBbKHo3CxVZAa-GWWHIeZwXLeAZhsW0pTFIEP0EsHuzR2JXNJRH2hZO7aA9r64YlmHYoZ0Fn_8YR36z1QafdA3nVSfIA34VtmZBXtizG1-Yz9kDC7sAuKU4gup66pZ9x7flzs3JXsnwRlN5rBB_FDBY-_rqNY_mqRWJLULgYoETo1JIOQriqWYgLq9ii6cml8_WLB--YSPAVsV_Ne3dMuAa7dcUsLHYzeLRzqqf05D4-i2ZXVZSkc8HMPQrGcmMld0K1XtooPrUgDx2itPlriZuaT1TS5oEw2ApqpJVbbvWuM_z__pH7Z8kC2JX8YeYszybNbxRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4411422981.mp4?token=gMl7H-o24Qj3tHT2yw9g0xaMUPUY7tTwHONtUmlhIOQLoFKGfztsTPbG08CUYyaCPm6CCsW0ZXKd4PZvdLeJfFJNEyf3JMiPKDMVbHEF9Kz6Tk05SKV3WQmvbnBOc6gpuskMViU9Z0xepapadG2_i_LBMSryURpKwgp5Vk9e0hQzZAYKWDrMlCy7yd2qB4G0pWMq-Ht_n9iCpPLZecLFtX_iXLN_Jk1MG1Z48PSxv8AE84YB0UDEt9ABtSypQ6Gb9fzeyxk4uqiYe-lpek8R-u3LIVZtGvvLSIs1PhiQ9vOrl7zKRcaWY-XooDBiEme8gAHFStCHfUj2Wr9Av-YShUDh0_eyTNyEwKdZBbKHo3CxVZAa-GWWHIeZwXLeAZhsW0pTFIEP0EsHuzR2JXNJRH2hZO7aA9r64YlmHYoZ0Fn_8YR36z1QafdA3nVSfIA34VtmZBXtizG1-Yz9kDC7sAuKU4gup66pZ9x7flzs3JXsnwRlN5rBB_FDBY-_rqNY_mqRWJLULgYoETo1JIOQriqWYgLq9ii6cml8_WLB--YSPAVsV_Ne3dMuAa7dcUsLHYzeLRzqqf05D4-i2ZXVZSkc8HMPQrGcmMld0K1XtooPrUgDx2itPlriZuaT1TS5oEw2ApqpJVbbvWuM_z__pH7Z8kC2JX8YeYszybNbxRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سریع‌القلم: آمریکایی‌ها بعد از انتخابات کنگره به سراغ عملیات گسترده نظامی علیه ایران می‌آیند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/145673" target="_blank">📅 09:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145672">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c9a950b3d.mp4?token=AdAgrrczryIPSndCDd3YP-ie8CY5DtzfY6a5lpUmRUIrk4fsn1v9dYmL_X3CYLPDl3uxTt8FYQmMBR6xIKydcbrrTac6AV2BNW_GvSMq5sh-9qY_qRVU_lKRHP_TtONtrKQ-3qgxWGIdCqVv4FgTuFjXJRZ2BcR1e11UL2NI96bduzeIQpPE0WXpeiS8kKXtSQ3DigTf8RoRmDKDTY78JRuY7QE6a6RP52W_X8Ice0fKCsMoEAv8XN_Z5oGHrNifne6Yd3PuMs6R7jrD2RKMSqHN2XYae-TyUik19jNuEWXu3XGPVnM0cyRfTym2huqBsyjnu8fJZdS1OnPiiVpgXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c9a950b3d.mp4?token=AdAgrrczryIPSndCDd3YP-ie8CY5DtzfY6a5lpUmRUIrk4fsn1v9dYmL_X3CYLPDl3uxTt8FYQmMBR6xIKydcbrrTac6AV2BNW_GvSMq5sh-9qY_qRVU_lKRHP_TtONtrKQ-3qgxWGIdCqVv4FgTuFjXJRZ2BcR1e11UL2NI96bduzeIQpPE0WXpeiS8kKXtSQ3DigTf8RoRmDKDTY78JRuY7QE6a6RP52W_X8Ice0fKCsMoEAv8XN_Z5oGHrNifne6Yd3PuMs6R7jrD2RKMSqHN2XYae-TyUik19jNuEWXu3XGPVnM0cyRfTym2huqBsyjnu8fJZdS1OnPiiVpgXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در پی سیل‌های ناشی از طوفان به جنوب چین، خانه‌ها زیر باران‌های سیل‌آسا تخریب می شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145672" target="_blank">📅 09:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145671">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
یک نماینده کنگره آمریکا: اگر درگیری با ایران پیش از انتخابات میان دوره‌ای پایان نیابد، آمریکا در معرض گرفتار شدن در «یک جنگ بی‌پایان دیگر» قرار می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145671" target="_blank">📅 09:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145670">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
مکرون خواهان آتش بس در جنوب لبنان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/145670" target="_blank">📅 09:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145669">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رئیس‌جمهور چین، قصد دارد در سفر آتی خود به واشنگتن، هیأتی بزرگ از مدیران و فعالان اقتصادی این کشور را همراه خود ببرد؛ اقدامی کم‌سابقه که در بحبوحه تنش‌های اقتصادی میان پکن و واشنگتن انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145669" target="_blank">📅 09:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145668">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bd7d8bb1c6.mp4?token=XZDorzoidJTp5FigEe1fCtV9MhMDammredtxBgbOdvOZ96AmXpuoUhVjmPKCM3IVxo9wQijk3UQZTfaKBQwN1NZ2-RFuqO1yVcTDmZIdX7jql3qIP6tt5DOsN6ChC7TkVBS5mvYJXT10bEpmjRfZIExC2h9M055Jl1X7EDbRAHr6kZk7bhBIr8bjsBtK6Lv121uWC1dvZe0-25K9TXNObPYPpnycocntySwtPjCNh5RJBx5g1OxQPI6SU0jVy5VmE5E9CPVg4orpFmHmuGDLdt1M6nLOx_Gcr96K49hs6cjLAkQ5gQrHwLtA6OXwFHzi2b5rZgknQPYf-vyCzYx3dg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bd7d8bb1c6.mp4?token=XZDorzoidJTp5FigEe1fCtV9MhMDammredtxBgbOdvOZ96AmXpuoUhVjmPKCM3IVxo9wQijk3UQZTfaKBQwN1NZ2-RFuqO1yVcTDmZIdX7jql3qIP6tt5DOsN6ChC7TkVBS5mvYJXT10bEpmjRfZIExC2h9M055Jl1X7EDbRAHr6kZk7bhBIr8bjsBtK6Lv121uWC1dvZe0-25K9TXNObPYPpnycocntySwtPjCNh5RJBx5g1OxQPI6SU0jVy5VmE5E9CPVg4orpFmHmuGDLdt1M6nLOx_Gcr96K49hs6cjLAkQ5gQrHwLtA6OXwFHzi2b5rZgknQPYf-vyCzYx3dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رانش زمین، رودخانه‌ای در نپال را مسدود کرد
🔴
رانش زمین گسترده در منطقه «آپی هیمال» در شهرستان دارچولا در غرب نپال، بخشی از رودخانه چاولانی را مسدود کرده و نگرانی‌ها درباره وقوع سیلاب ناگهانی در مناطق پایین‌دست را افزایش داده است.
🔴
مقام‌های محلی از ساکنان حاشیه رودخانه خواسته‌اند در حالت آماده‌باش باشند، زیرا ادامه رانش زمین می‌تواند مسیر رودخانه را به‌طور کامل مسدود و در صورت شکسته شدن این انسداد، موج ناگهانی آب ایجاد کند.
🔴
گزارش‌ها حاکی است جریان آب در حال عبور دوباره از میان توده رانش‌کرده است و این حادثه ارتباطی با فاجعه بزرگ سیلابی اخیر در دیگر مناطق نپال ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/145668" target="_blank">📅 09:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145667">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
نیویورک پست: تا دو ماه دیگر ذخایر سوخت ایران جوابگوی نیاز درون ایران است
🔴
۳ حالت پیش رو است:
🔴
۱-سهمیه بندی شدید
🔴
۲- گران کردن بنزین
🔴
۳-بازار چند نرخی
🔴
(با محاصره اقتصادی٫ برای کسری بنزین از ترکیه و امارات و ونزوئلا سوخت وارد نمی‌شود،  روسیه نیز خود کمبود بنزین دارد)
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145667" target="_blank">📅 09:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145666">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1a3ab30eb.mp4?token=eTfMB8iA36E9F_tRQGWiv7MdQqDm9tG-e3EFIHkASybHvaKijPdiIzEqUiZKGUUPTCBS1rl39No-WS103ORgV3hlVlDKvCQGZtLIENYZPmMIErqLlGkK6OLhvDOAfFEhBzHzAlnJmxZw4xgHKrgR7GUsRxhURVFEc-Md-eqX8tk4T_-d1S6N7SfzrDUPkkR5EcAjGvQd2IALtpKB5zU0rmv_hIqn7IaCw5wztqvOR8ON1GtyDVkOqO2-89UTX6Uuqb3IwJyS64LadPeRF0pp5j4483HzMJyB9QYu8Yu_aDNRUmXs_nZVfxXt8qkgxvVTIzbRQYVOpz_budjUbYGWsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1a3ab30eb.mp4?token=eTfMB8iA36E9F_tRQGWiv7MdQqDm9tG-e3EFIHkASybHvaKijPdiIzEqUiZKGUUPTCBS1rl39No-WS103ORgV3hlVlDKvCQGZtLIENYZPmMIErqLlGkK6OLhvDOAfFEhBzHzAlnJmxZw4xgHKrgR7GUsRxhURVFEc-Md-eqX8tk4T_-d1S6N7SfzrDUPkkR5EcAjGvQd2IALtpKB5zU0rmv_hIqn7IaCw5wztqvOR8ON1GtyDVkOqO2-89UTX6Uuqb3IwJyS64LadPeRF0pp5j4483HzMJyB9QYu8Yu_aDNRUmXs_nZVfxXt8qkgxvVTIzbRQYVOpz_budjUbYGWsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امارات به لنج‌های ایرانی اجازه بارگیری نمیدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/145666" target="_blank">📅 08:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145665">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
تانکرترکرز: ۷ میلیون بشکه نفت آماده عبور از هرمز با حفاظت آمریکا است
🔴
داده‌های کشتیرانی TankerTrackers مدعی است تانکرهای حامل حدود ۷ میلیون بشکه نفت و گاز در آستانه عبور از تنگه هرمز تحت حفاظت ایالات متحده قرار دارند.
🔴
این مجموعه همچنین اعلام کرده روز گذشته ۱۷ مورد انتقال کشتی‌به‌کشتی نفت و گاز در خلیج عمان شناسایی کرده که حجم محموله‌های آنها در مجموع به حدود ۲۴ میلیون بشکه می‌رسد.
🔴
این ارقام نشان می‌دهد با وجود ریسک‌های امنیتی، تلاش برای حفظ جریان صادرات انرژی از مسیر هرمز همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/145665" target="_blank">📅 08:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145664">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از منابع مطلع:
بازجویی از حدود 50 عضو ستاد مشترک ارتش در رابطه با افشای اطلاعات به رسانه‌ها درباره جنگ ايران.
🔴
این تحقیقات با نظامیان بر نشت اطلاعات مربوط به کاهش ذخایر مهمات حیاتی ارتش متمرکز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/145664" target="_blank">📅 08:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145663">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=XdQei2QokCsJWPTiUrEAeI9cLYwDNxqdvYxaKnJ54AP180yShIP8q4e7Gkmp6iKok6mq2p_X7URMB9jryvhomq3ytv87IU0H5q8PaA8ir4VQOEfdgYKBH32ROdUWYv53n_cYoOMuHz7V5yvxDNuXjbxVUQ7XXguLrjNTB3Diy-rbHRGvJuueZQe9vLtjIwtSVMwUwZiqGQot-oxTq5_UaSmaIucQnfqyjDAKa07gV4jIccHfjBxXCt7u8OnMpc_8_5O2C7ngBq_I6nmOk4HvtcqsmYGALJr1YEzacMJ0jboo52iqIzK0BjVbPGiBawNYxjOShyMAyNhGaYLScaoJSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=XdQei2QokCsJWPTiUrEAeI9cLYwDNxqdvYxaKnJ54AP180yShIP8q4e7Gkmp6iKok6mq2p_X7URMB9jryvhomq3ytv87IU0H5q8PaA8ir4VQOEfdgYKBH32ROdUWYv53n_cYoOMuHz7V5yvxDNuXjbxVUQ7XXguLrjNTB3Diy-rbHRGvJuueZQe9vLtjIwtSVMwUwZiqGQot-oxTq5_UaSmaIucQnfqyjDAKa07gV4jIccHfjBxXCt7u8OnMpc_8_5O2C7ngBq_I6nmOk4HvtcqsmYGALJr1YEzacMJ0jboo52iqIzK0BjVbPGiBawNYxjOShyMAyNhGaYLScaoJSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون وزارت ارتباطات :
حتی اگه جنگ بشه هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/145663" target="_blank">📅 08:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145662">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
کپلر: کشتی الغشامیه که حامل گاز طبیعی مایع بود و در کریدور جنوبی تنگه هرمز، تحت اسکورت آمریکا حرکت می‌کرد، از ادامه عبور انصراف داد
🔴
بر اساس داده‌های رهگیری کشتی‌ها از شرکت تحلیل کپلر که در اواخر مرداد ماه منتشر شد، کشتی الغشامیه به همراه چهار نفتکش دیگر حامل محموله‌های LNG از تأسیسات صادراتی رأس لفان قطر، به سمت شرق و تنگه هرمز در حرکت بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/145662" target="_blank">📅 08:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145661">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c61211abd.mp4?token=ivhGoULXc2elMltS2LXzLPYLqJD87jzF87gLP06SPbHMdPUC2LO_YuEOJIZvPyBzATrKRyNBKmK9hvFeApzl5UNSLVfrTvEIRGq0ZbXSXocm8GJbIupN2PzGfvQ14E9P54uS2A8K2DhrJuXiik2czUcBC85GyOkmQyOOk-I26VlRBHuQ8FOKVYL9_lzajFjh1Gm8UhWDaUQsfEKzV2zhs44Nc8XDfEZO9dhJhULexz4uvJXS9sq_twKiYeZyk2GIDX0zG5ELFWuUAS_TcgyinquVTx7NobcCgnov0UcjxIIIVV_4G4AVTVyRJ-t50OvejtOaB0ot--5BtOXEWlFe9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c61211abd.mp4?token=ivhGoULXc2elMltS2LXzLPYLqJD87jzF87gLP06SPbHMdPUC2LO_YuEOJIZvPyBzATrKRyNBKmK9hvFeApzl5UNSLVfrTvEIRGq0ZbXSXocm8GJbIupN2PzGfvQ14E9P54uS2A8K2DhrJuXiik2czUcBC85GyOkmQyOOk-I26VlRBHuQ8FOKVYL9_lzajFjh1Gm8UhWDaUQsfEKzV2zhs44Nc8XDfEZO9dhJhULexz4uvJXS9sq_twKiYeZyk2GIDX0zG5ELFWuUAS_TcgyinquVTx7NobcCgnov0UcjxIIIVV_4G4AVTVyRJ-t50OvejtOaB0ot--5BtOXEWlFe9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از منطقه میفادون، جنوب لبنان، پس از حملات سنگین اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/145661" target="_blank">📅 08:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145660">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a9c103ed7.mp4?token=CqA-n0KFl1OHZpsDHymuOqSp_DGgdvmY39z-Kx3640R-kdZVGrT6rNhPqd6A1xkjKWHpRp3rzXpP16n63tZ_oTZmvS8RaP3RFIXWpQJ5JB7hokUwVJUr9nT44a64K3rJkAsgP8f4V8r0apw6Bi40Cofd5DD7x9Q8Wa3evQeN1bOFIPvk0eqI45ExlyCInx0f6WkzdY0CMXfMVtuDLNj465e1bjY7DkPIv6UGxY-xl7zwVqCqtbDZenPEB9N11_trKh5kUrg8fboItlgyLMvHsKU2UjSUJm3zzEJSJ60l_FQgUxt6XH2tn1imzKaOaVoJzRaMm0W475NNR1zkEAAkDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a9c103ed7.mp4?token=CqA-n0KFl1OHZpsDHymuOqSp_DGgdvmY39z-Kx3640R-kdZVGrT6rNhPqd6A1xkjKWHpRp3rzXpP16n63tZ_oTZmvS8RaP3RFIXWpQJ5JB7hokUwVJUr9nT44a64K3rJkAsgP8f4V8r0apw6Bi40Cofd5DD7x9Q8Wa3evQeN1bOFIPvk0eqI45ExlyCInx0f6WkzdY0CMXfMVtuDLNj465e1bjY7DkPIv6UGxY-xl7zwVqCqtbDZenPEB9N11_trKh5kUrg8fboItlgyLMvHsKU2UjSUJm3zzEJSJ60l_FQgUxt6XH2tn1imzKaOaVoJzRaMm0W475NNR1zkEAAkDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روحانی: اگر قرار است با قدرت‌های جهانی ۲۰ سال دیگر بجنگیم، باید قبلش از مردم بپرسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/145660" target="_blank">📅 08:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145659">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f34f2cc3.mp4?token=P1NcC6g7faea-O_1ljmVI6KZeRARZyO_WZf9__Hqxpl88rjwhrNyMpPRP-dx3bBXZmTKlt74KjGzrgd_oZQeG-XjgyAR_JnJ7MF3F_lcAlWxA6ZQCm5WWXOFow6rOtdhaPDl0y9R6Gh5MIb4uWvA1upm71cOf8yAxYapqK2vNXjN687Ql_MRWvCoGSsHg_JBla2hT95_KO8Oc_i0WtVdBKedAYoizO30kB1ZgdJPa3vz_3E8QuXh46bMFcPA1PDshmEIhrLCfkFdwzHxxfJ7GiYMCxZ6IHbNpRmck006NY3VDZTCG4E6GU1IZHDsP0pXDoNjY5nbeAv9PZ2wlK4zgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f34f2cc3.mp4?token=P1NcC6g7faea-O_1ljmVI6KZeRARZyO_WZf9__Hqxpl88rjwhrNyMpPRP-dx3bBXZmTKlt74KjGzrgd_oZQeG-XjgyAR_JnJ7MF3F_lcAlWxA6ZQCm5WWXOFow6rOtdhaPDl0y9R6Gh5MIb4uWvA1upm71cOf8yAxYapqK2vNXjN687Ql_MRWvCoGSsHg_JBla2hT95_KO8Oc_i0WtVdBKedAYoizO30kB1ZgdJPa3vz_3E8QuXh46bMFcPA1PDshmEIhrLCfkFdwzHxxfJ7GiYMCxZ6IHbNpRmck006NY3VDZTCG4E6GU1IZHDsP0pXDoNjY5nbeAv9PZ2wlK4zgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موتور نیسان پاترول 2026 تو حالت عادی ۵۰ سال بدون مشکل کار میکنه و باز نمیشه
🔴
بنزین بی کیفیت باعث شد ۷۰ میلیارد تومن ماشین، سوپاپش ذوب بشه و موتورش بیاد پایین!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/145659" target="_blank">📅 07:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145658">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/145658" target="_blank">📅 01:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145657">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9kvvw6crS5ahAVuHvJupGvMAnm3kBi8G3gv4hIr3_LGwZH_yW2e-41AaSiIGAiOgMDVackJrhEOyjr8_SimRcjw4B4jtP24-2Vcv3vxE8Y0u1hfvB6T18eIzdYcprfYpr_Z5k5e643sRgbVZLIZtNumHhYZmdslEKfpeep6pC2jG7Rl23EM3V8jQo-kGxwi7UQV3yYWnDXmn7jfeNr2cGbVKIqB7hmK-Scx2A7JNiiYG77fDFJv4C2fQNZd1CEhDpprqKj3oacNGIF0jaemM8Mcuo69nRqC3PnKHbxbtng3JgbEAxP3OL3wk0MWTVEad6QXshY-z7r9Ug-PiWDAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
اگه اجازه بدن من فردا عازم لبنان میشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/145657" target="_blank">📅 01:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145655">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=dB5iiObzVLnNKQXKLJtn8q49qc0WLH24nlky8fUfNaBHOIQdLTd9l0ukNC6tUY11XDkcpjGY8wITtwfhkos7nGskBbgWol5O_lEVNo3tZ-o_BlfrtxhsMkOp1qZgRaViAGffoi5WHP7hlsSOPwMtq3-UgZYN9n_VZOsWuWKwGYc8VmojNIkSQ-ldLdEPdLje3vVCHQlxzEoNTFYtJPub1lxDBvn9FyH9-dAtXQHmc2-kIpgn5XD-ZPYR5ztL5apWwhgo_iM263eqW7B8Vf7jPdjV1xcpHD1bDb1AHkRrk2DlTB36yjLwnNb3p8I5LT0Efs_qcs5jOr49bPctH9NkLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=dB5iiObzVLnNKQXKLJtn8q49qc0WLH24nlky8fUfNaBHOIQdLTd9l0ukNC6tUY11XDkcpjGY8wITtwfhkos7nGskBbgWol5O_lEVNo3tZ-o_BlfrtxhsMkOp1qZgRaViAGffoi5WHP7hlsSOPwMtq3-UgZYN9n_VZOsWuWKwGYc8VmojNIkSQ-ldLdEPdLje3vVCHQlxzEoNTFYtJPub1lxDBvn9FyH9-dAtXQHmc2-kIpgn5XD-ZPYR5ztL5apWwhgo_iM263eqW7B8Vf7jPdjV1xcpHD1bDb1AHkRrk2DlTB36yjLwnNb3p8I5LT0Efs_qcs5jOr49bPctH9NkLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
معاون وزارت ارتباطات :
حتی اگه جنگ بشه هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/145655" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145654">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
نتانیاهو: جمهوری اسلامی سقوط میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/alonews/145654" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145653">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">خواستیم روزیمان حلال باشد
جوانیمان حرام شد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/alonews/145653" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145652">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
فعالیت پدافند هوایی اسلامشهر تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/alonews/145652" target="_blank">📅 00:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145651">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imoTaeeZPPXcPyX_xHCYKitGN7eOEHc2JaRRtXN1X7T0Og9YLKxT1WbBYrFCut7w9_khbNX03d3Wu9AUZwLJE30uayoZZkdO8grI4wfQjlSfZWnkhcmAUoVhLbzjBYFzMTWrs-36SJksYv3mgBmAmrMgp6apg1BXMASLffcvbtojLpVa4awOz27vrThYUASYakAtutEVMeHKrwYN1TGhIDbn4UD5L-UxB-2dwsa8wZbRlAtm5_LggkCBhprpd6DbzAGtm01l_O0J1mMOBAnDN6WwdLNBVfJCAlbuxWm398oqotvvmgfAxAdMCouoagcj6TE_UI00AHY0sfbm_ZKMfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
این وسط گروه هکری عدل علی تصاویر برهنه و منشوری مسیح علینژاد رو منتشر کرد
😐
😐
😐
😐
😐
🚨
مشاهده فوری عکس‌ها</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/alonews/145651" target="_blank">📅 00:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145650">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=oSJm97JuqrM5HKz9fBvKgzHNYsMxCinmiKf3p4RZFzPL8ip9L8wUguJR_0k6YEkake2vbA-s2kfIGb2VifQf4LiyUf5Pg0aUgfC8hi9Ppt8IwZFDC4kVDLGZ5yUy2P52mnjlfgOPXKRwonMkSH4200JKoRBB5g7FS9lng4goSs8VmvqlGK682-J7qZWjzhECvU_XRCsvk8CgOnPkmnVnMBcYH007QsB_-kEKmYu-YvypslYr4ON2ov5e-eYesD4gK06rIuJB8TQgEfPMjf3tCErmuA6KeyTOT2npp274mA0pofB0JpqsYAvGREPtBUraFioj7NuQo5_DSkZEkec4jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=oSJm97JuqrM5HKz9fBvKgzHNYsMxCinmiKf3p4RZFzPL8ip9L8wUguJR_0k6YEkake2vbA-s2kfIGb2VifQf4LiyUf5Pg0aUgfC8hi9Ppt8IwZFDC4kVDLGZ5yUy2P52mnjlfgOPXKRwonMkSH4200JKoRBB5g7FS9lng4goSs8VmvqlGK682-J7qZWjzhECvU_XRCsvk8CgOnPkmnVnMBcYH007QsB_-kEKmYu-YvypslYr4ON2ov5e-eYesD4gK06rIuJB8TQgEfPMjf3tCErmuA6KeyTOT2npp274mA0pofB0JpqsYAvGREPtBUraFioj7NuQo5_DSkZEkec4jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری شبکه خبر:
گازوئیل ۳سنت تو آمریکا گرون شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/alonews/145650" target="_blank">📅 00:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145649">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ارتش اسرائیل: نبطیه(از شهرهای حزب الله) را هم بزودی تصرف میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/alonews/145649" target="_blank">📅 00:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145648">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بچه‌ها این گردونه صراف رو چک کنید، من الان شانسی زدم ۵ دلار بهم داد
😐
😂
انگار اصلاً پوچ نداره و به همه یه چیزی میده.
برید بچرخونید ببینید شانس شما چیه
👇
https://r.saraf.app/s/agrd277</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/alonews/145648" target="_blank">📅 00:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145647">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ارتش اسرائیل: پهپادی را که حزب‌الله به سمت نیروهایمان در منطقه امنیتی پرتاب کرد رهگیری کردیم و هم‌اکنون با حملاتی پاسخ می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/145647" target="_blank">📅 00:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145646">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا روز جمعه اعلام کرد که فروش احتمالی مهمات تهاجمی با برد افزایش یافته به عربستان سعودی به ارزش تقریبی ۵ میلیارد دلار را تأیید کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/alonews/145646" target="_blank">📅 00:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145645">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/945968d3e7.mp4?token=tfA9wiul457xn4FbJzCl2xX70RvXMHKj6CloDZrSsZt0-_jbJNtpk4xeMnzbJ_h-MYmtBELoglYGgjXglHjI94dvjksWy-pvtDEZ3TB5qD3WlfTlBBa9oCvp_KQyHXzD9EzRfYLRbQO-QoSkmZPfEj69g0kqskkVEKMba_dQuW1NPCRuH_8nAko-vou3NuOWkh6WQvt75pR7CbtYhutAHkCpJBCNbdIS_blsGuG-O-S4R6TBjuDkmZLnhzIUouvJl73hor0RdU_FDxy7asyHDFtsFGJhpv6JvIyLpBKoRb44ZsV5aBXX92PXSBfjfFgIvlVoTSj-AFQnNXM31YoajA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/945968d3e7.mp4?token=tfA9wiul457xn4FbJzCl2xX70RvXMHKj6CloDZrSsZt0-_jbJNtpk4xeMnzbJ_h-MYmtBELoglYGgjXglHjI94dvjksWy-pvtDEZ3TB5qD3WlfTlBBa9oCvp_KQyHXzD9EzRfYLRbQO-QoSkmZPfEj69g0kqskkVEKMba_dQuW1NPCRuH_8nAko-vou3NuOWkh6WQvt75pR7CbtYhutAHkCpJBCNbdIS_blsGuG-O-S4R6TBjuDkmZLnhzIUouvJl73hor0RdU_FDxy7asyHDFtsFGJhpv6JvIyLpBKoRb44ZsV5aBXX92PXSBfjfFgIvlVoTSj-AFQnNXM31YoajA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: مردم آمریکا چه زمانی باید منتظر حل‌وفصل مسئله ایران باشند؟
🔴
ترامپ: چی؟ انقلاب؟
🔴
خبرنگار: منظورم حل‌وفصل بود.
🔴
ترامپ: فکر کردم میگی «انقلاب» جالب‌تر بود. حل‌وفصل؟ نمی‌دونم
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/alonews/145645" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145644">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
فرزند سردار تنگسیری: تاکید می‌کنم امکان ندارد بتوانند تنگه هرمز را به صورت نظامی باز کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/145644" target="_blank">📅 23:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145643">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
المیادین به نقل از مقام ارشد ایرانی: به کره جنوبی هشدار می‌دهیم که هرگونه مشارکت این کشور علیه ایران در تنگه هرمز را به منزله مشارکت نظامی در تجاوز تلقی خواهیم کرد
🔴
سئول منافع و اعتبار خود را فدای سیاست‌های بی‌ثبات‌کننده آمریکا نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/145643" target="_blank">📅 23:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145642">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
اعرافی، امام جمعه قم: آمریکا با روش‌های جدید جنگ نامتقارن و چریکی جمهوری اسلامی آشنا نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/145642" target="_blank">📅 23:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145641">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c61211abd.mp4?token=JMpn-HHMYnTEpKqdDlvX51hFQN9JGDSy3g2iwPfMnb-wJ3uBPqMmtXDV5Lzq3bnE_9CHSw3zen1b0_QKCKvTBIh4scNdT-1JQr5fwBZC42IYBEMMmbiT7rLzwXYtZYYG-_L6pmm_sdb6XoTpKbuDIZBfuRFCiRlR1TJbCdCZO10u3hOw06uT0SAm2irGnisD_flUXYixo3Hk71ZrgOk865Tm0D27hSuCkQ8HY-L10lIFOjAuL3TraC6LrGZZZE9nx96ZM5muPuxX8ypuQoXFh-kHIQ3N5zp_oQrCdeE-IScacGkhNg-c3WizkZmbpgMKLjHbGjxSDxWpGVvTYU5i3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c61211abd.mp4?token=JMpn-HHMYnTEpKqdDlvX51hFQN9JGDSy3g2iwPfMnb-wJ3uBPqMmtXDV5Lzq3bnE_9CHSw3zen1b0_QKCKvTBIh4scNdT-1JQr5fwBZC42IYBEMMmbiT7rLzwXYtZYYG-_L6pmm_sdb6XoTpKbuDIZBfuRFCiRlR1TJbCdCZO10u3hOw06uT0SAm2irGnisD_flUXYixo3Hk71ZrgOk865Tm0D27hSuCkQ8HY-L10lIFOjAuL3TraC6LrGZZZE9nx96ZM5muPuxX8ypuQoXFh-kHIQ3N5zp_oQrCdeE-IScacGkhNg-c3WizkZmbpgMKLjHbGjxSDxWpGVvTYU5i3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از منطقه میفادون، جنوب لبنان، پس از حمله اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/alonews/145641" target="_blank">📅 23:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145640">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDA74Gx9mi8DHKsR5PQAP_dmx8PailaP9SraOvyVUJKEserpYlqn_ehEmnD9UmnIx7RputNK4aiXRpPDlKecFoDBAk2YHxwacUT7mInMV2eQVh0fXGgWxJbSAAWrqcuSXo0qgxDRFAEjmO4QhewTFqL05Y9XP4q2RIiD0UVli25VBs_1Zb1fjCxjYZcaRxOWhnF-3PDFqdaTTdys7EtgoogQ6B5wsUfb6o-gwNKjPJAHdrLIrUvGbtU2j1dW75DMyR9K2teghaSkNzffN_JStwj-wOQxBu2Rp_zFnxhiheMChrTwoK1KpcBcRLCrcUzaRbZ-XQHU1f8-rInop9sFGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایید حمله پیشدستانه ایران توسط رئیس کمیسیون امنیت ملی
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/alonews/145640" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
