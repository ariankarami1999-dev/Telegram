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
<img src="https://cdn4.telesco.pe/file/U3MfJiXJ6lyJ-mSvlAvGo1gTMsKafdfL3tuwCJ7tC-VfMv-0FYjL9mKoUssHD-f-3MuCsn4NpqaVjPueQshbAEk-Yusl9nt3V1fZxUk829e79LlE4n9rLyRtSnVuqkfg5B-5pb3ckDpVHxZmY5xCSHlGHB3qp3MgU_vpLuIH78fEt0GsJOM1dLOTvwo6rgI4MEf4q6bnBbNDbCahq61vvAsRUmTal4jdluFOZOCsMB1q4Q1WXcxMNOgdE9rartWPTf_Lctklo_p1EPwC_SVl4XD1dXmR50zZPLWLzcp4x5K6NDr1tHdY62clUBFrIq-87QNByfkggNtxY3YwQGhhyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 20:43:45</div>
<hr>

<div class="tg-post" id="msg-66880">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LG-5sqZX1xQBmZW5c3NWWez7I749Bp0nnvfe30Prm4GleJehkcM6oPeUHhoLeM27sHa4g9pNOrDKt4CyjG0Ft5SvdJcnpUKSWQtgb63mcEDYGnrsd6RjFvY2U8iIK3SUTD-BQELaY4-cHq8wnvoRCZ9etkYCTF0eDnEy-kRIowWOWav_UkeJNCfU7Sm5PN6GYAvjSV4sUfLC6Zx1lBhpsiEml_gyIk8QFddUOKIyzbXMVz4AF4XL048NSe3MueZbL5zVBM2keDLXhO-jybmwJrEZ86eoGcG5S23zLeTt0UpxqnVJ0jRKgtgSxfJlaSaI7ESe5hV6T6lj0EfSa8TeWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید اکسیوس:
مقامات اسرائیلی و لبنانی به من می‌گویند که انتظار دارند پس از چهار روز مذاکره در واشنگتن، امروز توافقی کلی بین دو دولت اعلام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/news_hut/66880" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66878">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FsHKqb_La8m_yyO26AyQT6qASjMDPTr8_5eT-qtWr5WpFsdyE87azjqgXTAyZwsHgjpP4jIzN1SHCFCEvs1LUU2hpmZ5Wf18j03q-Y-MFtjl8n4cCyZ-CStrGXZs-Epacj7bd6eQpr0ar8-7023tYYx5S6TbacozT0jn2_uF5pOvw7Mj6_3KEl5KLQhwVOqKVOBusi2rkEND4gGbF8Qrko8RNZPVclWolU0BNkiCst9sxoP5BT0177BsivmWF8ThHlTc81Px6yxMCaqqsM70gjbww8o_Fb4wv1NZV62tsIjTwklc31zH3SVFSCiD88l9qij8S3gNVm9XkCy8RWtUcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FC5ZRQdOHVYFW6-raQ7qbkHYmgLrtVsDhur_vZGBjpii03a74u84a7BDTwyST3nLpqBEanB-AhUmMOj8AG6OXw58UttWDLsm3sDErD_l57t0SkOAlHXj8mk3XiTeLTaM18ZGSqfYLlde6yBDZVCdZ7F-QBJ3UwXk8a8d2gNZQltqHPy_EJ_3O20IG62TfX7HEtdr1AKMz90l5DyIqMSveEbhaQ6-UxYCb-iq5mm3f-3djA6x0BR4SvTmx81Xer5ElWwH3nApZijhVhTHc9enQVKSvGJ0plXHYghFf-qmUo_b6BRkLsF8CSvgQxUouKpAIvp7FtIvlBRJMeSvU3faiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در فاصله چند ساعت مانده تا آغاز بازی حساس جمهوری اسلامی و مصر رژه‌‌ی همجنسگرایان در شهر سیاتل آمریکا آغاز شد!!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/news_hut/66878" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66877">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jisNc-GuII3jgAhWpUFfEh8_DkmhJpAbVbNipvktTQPIMAGqKrsWTuoQpMX5cpxdAtQHguCkHWDcBXeZ3PdY9xI1DsafwKSvpzUBCNnAMP7kk4t6fHFBuw47VPVOw9D0ezIawTbIzlwT0vFBHBBKHxYLjS0uGDxp-l--z5zNuP9-U4-bIBg7WMX0f6mUvNNsH6pPCH5XCIEkUuqQGo-fHNDzsaEUnY3gnb8-86aAuMjhPPNjUkR6TGZT5qR4QIHo7ADouJUDoyG5eBn9G6jxFPqFzfN-CBYPXXsqScvd8kifQe5lgZVOzA2SCrIBVx8G1Z9bF0j1Bxxvbaj_d8ca9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد.
خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد. ما سه پهپاد دیگر را سرنگون کردیم.
بدیهی است که این نقض احمقانه توافق آتش‌بس ما است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/news_hut/66877" target="_blank">📅 19:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66876">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1yqSKDWR0Bv6ahAGlnWbRraAdHbTvkN_2842ibZPmSPE-06xgLfhpSxPY8hLHSFYnQYbzIxONNs5dsTmIrQ5esuEwNVycaLKgouKI9A6IpmNEPFzCLe2MW1XnVYY69kceI3B0I6aWNbNHS5tXnDRTQfFEBPHUYudvbqderK7WaRE0kkPrBSXQbid4MyTZihOwaK6SnnVxmvQmK-PY2hVEQ621bJ4CJwcDfqEr8d9SiqzXTcI20JgfqMSS7i885qe0DHyEfN8OM3dwtyBARgxWWHEpvJ67F1W57__8LKNi7Eb3CdvF58MN0cx2LVI1RIKzqOoS8PS2ODKoy4GWcX5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ:عمان هشدار داد تنگه هرمز به شرایط پیش از جنگ باز نخواهد گشت، کشتی‌ها ممکن است مجبور به پرداخت عوارض عبور شوند
عمان به متحدان اروپایی خود هشدار داده است که تنگه هرمز به وضعیت پیشین خود قبل از جنگ باز نخواهد گشت، که این امر نشان‌دهنده احتمال اعمال عوارض عبور جدید برای کشتی‌ها است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/news_hut/66876" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66875">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYBRVtc_ofzWPFR4BTiR-rJwZcjIuU-eBXaVTO5I1cFhFZM49PNXO0UG9izG2sZpLZaQCOaZSNiXF4LB7NzOSW7DIG130sq_DPELtbsRyy_pQBnlkC7GESPJcBGwog0S0vJG5jvC8pwo-SAxaWsFGvAbvmc0ebJ3HGWjDAuw_gFUI072PTqNPArs0Q1ISRkkjasZhJEtpci9XebvHM858yMkatiqSpzafWbNZ5TIcSTln-o3uxa79mN935l80WF6wxj27giVqJO61FGtvHkeM7DXGgH3rE7IhjeL1Pz1cvYfgVtsdt9H6UIJXUg243q4e9yUHBal00NRUr7pMtEdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
رونالدو تو جام جهانی گریه می‌کنه؟
پلی مارکت می‌گه ۶۵٪ بله. احتمالاً آخرین تورنمنت ملیشه و دوربین‌ها منتظرن. البته رونالدو رو که می‌شناسی، شاید حتی با قهرمانی هم گریه کنه!
قبل از اولین اشک رونالدو، پیش‌بینی‌ات رو توی 30 ثانیه روی پلی مارکت از تلگرام ثبتش کن
👇
https://t.me/PolyBaaz_Bot</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/news_hut/66875" target="_blank">📅 19:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66874">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=qWd6rbHpA3Le4b9EHhBeSoJ1TAC9XTTczaAqSAI389W9YGwsR91vYig3uL4Sl3zySKlkuORY_QPOCfO7G8Zr0cYZwiWaLhX0a3YKop9pNUjZKEhQmCPnEszw3UoRLBRfe5XYJ9bPEyXU-uRS81tDet24k6lQEyhVo7rax7ZVlR-6EtItHk79uw9j2FyWrNFtSIpxKQNF34dBZweLo-Wjcv46_6M0yyVRUcohs1hIcFcUl0iwbLcioze-OnyjCg21MXIoIQ_hsitSbpB18EyEgbmiEaQ1rJzESdwLE3NxrHBYB5ggjw8pULAnAGsXbAl1dxg-1ClH-vsQUzPRipgyPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=qWd6rbHpA3Le4b9EHhBeSoJ1TAC9XTTczaAqSAI389W9YGwsR91vYig3uL4Sl3zySKlkuORY_QPOCfO7G8Zr0cYZwiWaLhX0a3YKop9pNUjZKEhQmCPnEszw3UoRLBRfe5XYJ9bPEyXU-uRS81tDet24k6lQEyhVo7rax7ZVlR-6EtItHk79uw9j2FyWrNFtSIpxKQNF34dBZweLo-Wjcv46_6M0yyVRUcohs1hIcFcUl0iwbLcioze-OnyjCg21MXIoIQ_hsitSbpB18EyEgbmiEaQ1rJzESdwLE3NxrHBYB5ggjw8pULAnAGsXbAl1dxg-1ClH-vsQUzPRipgyPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قاسمیان:
به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/news_hut/66874" target="_blank">📅 18:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66873">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU1OWhfM8N0SaZAh-Y5yeieVZjEdV3q65BCJIFksxXudlwziIFfTtAtfTRCh4c7U3BiXrPUYr8sfnuBNBaq2T5OeMeqDSLXM0vTbbshy93x_IKDiPJHfGFVMrxfOv2CnKJZYcd8S5aI3WbnBy1wjdC2XhuLO2WWwEjDz1qJ2IybUjrZNX7VZ6YjRc5Ae0TpRUxg5Yn7YV4EymSVg-se2SXlM9I5ymBW2w0bmmgxQ9iUZtJHD54VxXYOpljofOI04_BVoannKeyHgqtdBAJ9hMkzXjtjnOL91nhgV3sdx-Yfq2CU-nE7qR17k0Rk46slMBD7r9EQGZ3tRV2NR3nsofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
توییت کاتز وزیر جنگ اسرائیل که قالیباف و عراقچی و پزشکیان رو تگ کرده:
فرمانده نیروی قدس، قاآنی، این روزها مدام اسرائیل را تهدید می‌کند.
به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحکِ تهدید به او می‌آید.
در هر صورت اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.
نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان، هیچ‌‌چیز ما را متوقف نخواهند کرد.
نیروهای ما آماده‌اند تا کار را به پایان برسانند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/66873" target="_blank">📅 18:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66872">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=CWIGrBnjgfKVpN8dm7e7jfnNgTP9MsuZh80R-B7582cc0sQ9u1UD3A0eEDEBBpiyQeyYbyG4IK4A4hVrmJB00A3peASuDuRVc5xpitSllP8SqBedv_VNaZooMsW_E6mpCTymdMhL8LYKX_FJQFFJ2X6BZstaGXPgtzp_Dp2WxBb7YVus-uKNsZMxfxS7zulp0yxL8JSVxWbF7SJxwEGYNbe4HOsX2OOMgRCLRBlx8JF_rjOTvs2yHPdFNwT8e_ZzCLE3GZeImVuiNTyc4ORpob6ViZOK-uJyvz70Qe48T_Vla2ZlqfWRq7Mwl5s8ky9mNL3GrObu7gbvQQa8TAvwVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=CWIGrBnjgfKVpN8dm7e7jfnNgTP9MsuZh80R-B7582cc0sQ9u1UD3A0eEDEBBpiyQeyYbyG4IK4A4hVrmJB00A3peASuDuRVc5xpitSllP8SqBedv_VNaZooMsW_E6mpCTymdMhL8LYKX_FJQFFJ2X6BZstaGXPgtzp_Dp2WxBb7YVus-uKNsZMxfxS7zulp0yxL8JSVxWbF7SJxwEGYNbe4HOsX2OOMgRCLRBlx8JF_rjOTvs2yHPdFNwT8e_ZzCLE3GZeImVuiNTyc4ORpob6ViZOK-uJyvz70Qe48T_Vla2ZlqfWRq7Mwl5s8ky9mNL3GrObu7gbvQQa8TAvwVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای وایرال شده‌ی یه آخوند تو یکی از هیئتای مملکت :
حضرت آدم دید هر عضوی از بدنش به درد یه کاری میخوره که یهو یه نگاه به وسط پاش کرد دید یه تکه گوشت اون وسط اضافه اس٬ گفت این دیگه چیه؟ هرچی دست بهش مالید دید اضافس بدرد نمیخوره؛
حضرت آدم خنجر یمنی رو کشید که کیر خودشو قطع کنه که یه دفعه حضرت حوا ظاهر شد گفت آی آدم چرا میخوای بیچاره‌مون کنی که یه دفعه آدم دید کیرش راست شد؛ بعد با خودش گفت این مال کس دیگه ایه٬ این تو اختیار ما نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/66872" target="_blank">📅 17:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66870">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5BhspcJvWsUHX1l_ZSYx4BLbOVS6NIKr1ZiUlW-0WrO697-hC_lJ-kpoKxfLSTVwjNOb0ik0kv_Ww3wN34HHUpC-OQ4KchX8LX8UzRbc-22AiW6Bh0BpXI1c0d25PVLjd8ObxX5aZoFyHsQc9aog595GIsCCEdzn7dGlbKrPxgI0L-6DS5AK8qI8X7RXR1-RGPHT5obwGalHPNNN-noqKQ5EvRTnFIhPxAgqR0PrTdjwXVcXht2R5JK-simj_R_EDkVafF6GOYIjgAyeBOIKkNG7jAdJynwVR4dH9tGMo_sWQLxWw6DQfwx__NyknA5UnevSAj0A4mU_MINzdII7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-wfIfJA9gB7FOkniKShwI1dK3lPW5NHbA0uBcFQzWeCE5VuU7STcl_P7r7n38nDIbXFDJdh8BfgOjgZCL5-IIe17uJz9hPeOfCDtzw4diMvPZqTbXByU39PdsNI-CELEbpXmudMQXDVQy-rsxXPj10tNeDouoUOGIWQT-K0fHRqqNSyjgIiaq-zia7Xoo_oTFxGLuijp5SaSUVX9j5QIVTTPNR1BqnHEkqSOARNN5lF23QPhOrvUSRRxT_gsqRy47M4l3yeqXO5be8v3mxr2pVXyvtCaZFVCIeWY3mDL4i7ZVKHG9NXvwL-nuZsLuC61tJq13ZPAXWyHRG13gB7NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
‏
بر اساس تصاویر ماهواره‌ای که روزنامه وال‌استریت ژورنال تحلیل کرده، حملات موشکی و پهپادی ایران خسارات گسترده‌ای به پایگاه نیروی دریایی آمریکا در بحرین، از جمله مقر ناوگان پنجم، تأسیسات ارتباطی، انبارها و ساختمان‌های پشتیبانی وارد کرده است .
با وجود اینکه پنتاگون اعلام کرده عملیات ادامه داشته و تلفات انسانی ناچیز بوده، این حملات آسیب‌پذیری قابل‌توجه پایگاه‌های آمریکا در خلیج فارس را آشکار کرده و موجب بازنگری گسترده در آرایش نظامی ایالات متحده در منطقه شده.
مقام‌های آمریکایی در حال بررسی انتقال یا بازطراحی تأسیسات کلیدی به نقاطی دورتر از برد موشک‌های ایران هستند. گزینه‌های مورد بررسی شامل پراکنده‌سازی نیروها، تقویت استحکامات پایگاه‌ها و گسترش استقرار در مکان‌هایی مانند اسرائیل است.
برآورد می‌شود هزینه بازسازی خسارات واردشده به پایگاه بحرین حدود ۴۰۰ میلیون دلار باشد و مجموع خسارات واردشده به پایگاه‌های آمریکا در منطقه از ۲ میلیارد دلار فراتر رود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/66870" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66869">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=cEQC29bSzRPs-ULVhZ9NZ5GaHMCbloToKLv-FVQNLZwzjnq6GtcLh9xfgUd7fOtZJKzXpQSZS2RLjQHpTtJJTyyw-d7FSKnjy6_xU1x4TF7AwOjK25IBMC6MiS55ly-CC-G2sefcnF5MGQzK-Yr4WU3ze6ovX6lpdBS8mtkZBytGLiWHiNt1pq7KwfxCg0ueZnDhstltjUdoho1Ziv7Dikwj_I2N8PvjNqLQ6OiHawK-Mhc3lLmhl9FxENi8UO3UECtat9hwkEGD54vsROxMMJaKyr9fxmUEcWnh2E_YfUKuFJB9uUBFFHY-j6QA7sKTsHdSssheb0RPo9Nni8Ji7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=cEQC29bSzRPs-ULVhZ9NZ5GaHMCbloToKLv-FVQNLZwzjnq6GtcLh9xfgUd7fOtZJKzXpQSZS2RLjQHpTtJJTyyw-d7FSKnjy6_xU1x4TF7AwOjK25IBMC6MiS55ly-CC-G2sefcnF5MGQzK-Yr4WU3ze6ovX6lpdBS8mtkZBytGLiWHiNt1pq7KwfxCg0ueZnDhstltjUdoho1Ziv7Dikwj_I2N8PvjNqLQ6OiHawK-Mhc3lLmhl9FxENi8UO3UECtat9hwkEGD54vsROxMMJaKyr9fxmUEcWnh2E_YfUKuFJB9uUBFFHY-j6QA7sKTsHdSssheb0RPo9Nni8Ji7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟥
فاکس نیوز:
دبیر کل ناتو  فاش کرده در جنگ اخیر فقط ۵۰۰ جنگنده آمریکایی از مبدا ایتالیا به سمت ایران پرواز کرده اند؛
«اگر ایتالیا را به‌عنوان مثال در نظر بگیرید، ۵۰۰ جنگنده آمریکایی از پایگاه‌های آمریکا در ایتالیا برای پشتیبانی از عملیات “Epic Fury” به پرواز درآمدند.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/66869" target="_blank">📅 16:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66868">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=Bno6dqFGbg5gGeG4E7PFD8BoIrQv_vhe_Cypp27SuEy9fEMJQhYuNmX10aRBHeKbN0Zs6Url_YSId55ruIKJCbeaiiydlY3HnT8lKeGQDIJh829ex6khDsWNxEaBp2ebA9ggwNzraHNLpPGEpdXOP8juueW51lV2GEI5NZRNhI6cXmJldmC2m4FDFhd4qx_xU63BdDvmkVP4Sktew7-JW5EUvXwGLokHRyefUiUYx31HDACdA1vD8Gw0WvZaeSNJuKjZEqG_MIGwfPRUWc8Q02kQOD7aj7sTMji5zpKPME6Qm5ZvuXEEJHtvbjCjuToeah_tnPvPqN4Wb-wJ1chpGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=Bno6dqFGbg5gGeG4E7PFD8BoIrQv_vhe_Cypp27SuEy9fEMJQhYuNmX10aRBHeKbN0Zs6Url_YSId55ruIKJCbeaiiydlY3HnT8lKeGQDIJh829ex6khDsWNxEaBp2ebA9ggwNzraHNLpPGEpdXOP8juueW51lV2GEI5NZRNhI6cXmJldmC2m4FDFhd4qx_xU63BdDvmkVP4Sktew7-JW5EUvXwGLokHRyefUiUYx31HDACdA1vD8Gw0WvZaeSNJuKjZEqG_MIGwfPRUWc8Q02kQOD7aj7sTMji5zpKPME6Qm5ZvuXEEJHtvbjCjuToeah_tnPvPqN4Wb-wJ1chpGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاسخ سخنگوی وزارت خارجه به دست ندادن تیم مذاکره کننده با ونس با شعر مولانا:
چون بسی ابلیس آدم روی هست
پس به هر دستی نشاید داد دست
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/66868" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66867">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/66867" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66866">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=HmhlsvLs2aoaWWWlO_Bjy4uwWJE0N_9B2zpI0GlEO4awMfhyzwkE_WfjrfDvmc7yC3Tbmblb5xY9ZvvCLceNHreOe1n9p0yj240QWMUjpjQal0gGry0fCsMLHjCEy_VIp3Jt00IPq_CpBq4nQpu0kaRFBvLnH2uP4VtwTGGlKex-HDg6bysO57oj0W44j1zAqDRn_KKES-_VbJtNpKmzUizJggZfh2DNp2HN2fJcGIt5BX9Zgg-ItoI0JHAjk1J21ewIPxCTJbQywlueTeCzGuZUr5Gh0a1LT0Nj3cVC7MH3Kn_64wQHjC3EvxDrkrs82jB5qEqmCXE4LzFAocO0M3vwAMWhhoU7cMTb3rLXDCjujP9JRo4cNJvg1cgjUfoznE9VT6L8aMZstB6D25HkF8Q1GidzAcBKVCmGsolxazQ3iLdz5umakFZ2PgRtOtjQwcSFExaqnO4HJ8DZBwER34ohif9WDnDW5tisv_8oghDKCSU_EQ7Yv4la9o6ehbakaLnE_G38xCMTFBvFeFKs9djaI5_0Lhm1XW4PN2iIBOEW5461H4n0_R5aJRv9Kd5dFu8ujN9hTCHLyNfNSrqzfblG4_z48j9PDW0OlTVGu4fWMxL-tTY92Fgb3334oevBUF68QXXBqxvXbH_hJaHKlmF6M6udzaX3jrARA7y9JRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=HmhlsvLs2aoaWWWlO_Bjy4uwWJE0N_9B2zpI0GlEO4awMfhyzwkE_WfjrfDvmc7yC3Tbmblb5xY9ZvvCLceNHreOe1n9p0yj240QWMUjpjQal0gGry0fCsMLHjCEy_VIp3Jt00IPq_CpBq4nQpu0kaRFBvLnH2uP4VtwTGGlKex-HDg6bysO57oj0W44j1zAqDRn_KKES-_VbJtNpKmzUizJggZfh2DNp2HN2fJcGIt5BX9Zgg-ItoI0JHAjk1J21ewIPxCTJbQywlueTeCzGuZUr5Gh0a1LT0Nj3cVC7MH3Kn_64wQHjC3EvxDrkrs82jB5qEqmCXE4LzFAocO0M3vwAMWhhoU7cMTb3rLXDCjujP9JRo4cNJvg1cgjUfoznE9VT6L8aMZstB6D25HkF8Q1GidzAcBKVCmGsolxazQ3iLdz5umakFZ2PgRtOtjQwcSFExaqnO4HJ8DZBwER34ohif9WDnDW5tisv_8oghDKCSU_EQ7Yv4la9o6ehbakaLnE_G38xCMTFBvFeFKs9djaI5_0Lhm1XW4PN2iIBOEW5461H4n0_R5aJRv9Kd5dFu8ujN9hTCHLyNfNSrqzfblG4_z48j9PDW0OlTVGu4fWMxL-tTY92Fgb3334oevBUF68QXXBqxvXbH_hJaHKlmF6M6udzaX3jrARA7y9JRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/66866" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66864">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzAlNAuqqwSgXqo8NvmErGWn7enByHW8GRYhiXiKN-CS_a7OpbXtNvNyWBELH_und9x2t9cokX2yvYW7Yvkem9F2vconDE--oCR3eWK6u8CfR2AkJVXmmZGvL2910oOL-bQO0WEhjFP_KqDxrygyUN6KwWDDsdYcBO2LDWFXM33Aurf1u7vuvnVtWfADO1if9bj4GyKRatj3e87rxpFyk9UIQZJKONf4A3THfNahMwuCuQHCLck3lmPVyKjHceAcGjzCxAD8d3GpX7krns8nKSJhA6jH7ltD3PqVi0imRp4QDYbfYuKoUw3mMm8T5pC2CEgVGT1Qlib04rvIJwEe5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=K3fXCXlqSWhH1d0hwhiYuvSUvmEVOQuYRcwm3FV-cH5wfgW6Ky4f01aEDl6X_yFoLtk2t57Ho_09T_rSz-mIxbwZYAocp5fUFlth1zELr0EMptBJ8EU4Kvj4s5j_H6-OYq1msV91nOLo75aIAcg0SfXggnxWlnX0BDobYxz-JQRdNSau8raZzI21ALnCIKeg3uPn314KLUo2lPZigRGpdU-r57kSY39Y_iIKkXg3-RFro9iXgjF8fyDGm4O4hYBOdrY40k3GIrQKxcodBz4YS7CA-Emv2DbOGthfBi-WdhelhlviiA65sYnYLbf9LZMFOXVgvbuevoa_dHFc46za5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=K3fXCXlqSWhH1d0hwhiYuvSUvmEVOQuYRcwm3FV-cH5wfgW6Ky4f01aEDl6X_yFoLtk2t57Ho_09T_rSz-mIxbwZYAocp5fUFlth1zELr0EMptBJ8EU4Kvj4s5j_H6-OYq1msV91nOLo75aIAcg0SfXggnxWlnX0BDobYxz-JQRdNSau8raZzI21ALnCIKeg3uPn314KLUo2lPZigRGpdU-r57kSY39Y_iIKkXg3-RFro9iXgjF8fyDGm4O4hYBOdrY40k3GIrQKxcodBz4YS7CA-Emv2DbOGthfBi-WdhelhlviiA65sYnYLbf9LZMFOXVgvbuevoa_dHFc46za5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌های لبنانی گزارش می‌دهند که یک پهپاد ارتش اسرائیل، اعلامیه‌هایی را بر فراز شهر منصوری در جنوب لبنان، نزدیک صور، رها کرده است.
روی این اعلامیه‌ها نوشته شده است: «منطقه خطر! دور بمانید! هرگونه نزدیک شدن به نیروهای ارتش اسرائیل شما را در معرض خطر قرار می‌دهد.»
هنوز تأیید فوری از سوی ارتش اسرائیل وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/66864" target="_blank">📅 15:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66863">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=HyciqR9ojR75gyeIv1CfKQxS8Hv5FKNjuov7Mpqq6IRvXZ4Q1PgfB6z_tiX9FjE0Jle6VHvO28QBBUmSRIXlhTmki7cVqqqDFNx_iAqtIYxvElWUDsRf-YtsYsyPMYrRfClu78Gpl-_D-34HHwdJZgz3DrmkxyIPD_lckp59dB_G4Gqn142p_WFxrHvcfbzJtCSu5EgcPet_UISyI1vVWuX9Ipc0QOdibhqMHjsuxzaBVvkIryn3wFdY4lWOVkVL64ookuDrrBWIh2gXm-Tu7AS2DBKAOOuDcLAUac3j5rn4bjZdocWwap80VRvsV6wAACMCDeLDk4GDDIN9T22Wfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=HyciqR9ojR75gyeIv1CfKQxS8Hv5FKNjuov7Mpqq6IRvXZ4Q1PgfB6z_tiX9FjE0Jle6VHvO28QBBUmSRIXlhTmki7cVqqqDFNx_iAqtIYxvElWUDsRf-YtsYsyPMYrRfClu78Gpl-_D-34HHwdJZgz3DrmkxyIPD_lckp59dB_G4Gqn142p_WFxrHvcfbzJtCSu5EgcPet_UISyI1vVWuX9Ipc0QOdibhqMHjsuxzaBVvkIryn3wFdY4lWOVkVL64ookuDrrBWIh2gXm-Tu7AS2DBKAOOuDcLAUac3j5rn4bjZdocWwap80VRvsV6wAACMCDeLDk4GDDIN9T22Wfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
اکثر مردم نمی‌دانند که حرف B در کلمه dumb وجود دارد
😢
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66863" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66862">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⚠️
خبرگزاری فوق معتبر فارس:
درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66862" target="_blank">📅 14:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66861">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=GS_o9lYqhihINSJvMvIgyBWS4DwOSq1UhsGVIqwzfC9_RmbAv3MKuKFC3dJs78MHMCr70ZcqnKS0n5s-QEBI-tR-DuAaRjws5oYQ-MPPvPgWYMRLQGDdnGFhcV123feI2qaNfF7i4BxkUlEoMlzs52j4SuxmHWPDLJqt2SQjaZ8KIy5Wv2bL5ptHHXGTx35r7kczO_elgvoyXWv_lX-drzmEMxTNQyy8YA8y1pR3kM083Wm4PswRITlkdNzCmcNKU_2yRBF9nMsWfnqiJKYIehNfz4IioqjQF93tG3jP47SuSsGjl7PFWonkRTcuJUQedzUmpDE50mSC0XYCrdQvsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=GS_o9lYqhihINSJvMvIgyBWS4DwOSq1UhsGVIqwzfC9_RmbAv3MKuKFC3dJs78MHMCr70ZcqnKS0n5s-QEBI-tR-DuAaRjws5oYQ-MPPvPgWYMRLQGDdnGFhcV123feI2qaNfF7i4BxkUlEoMlzs52j4SuxmHWPDLJqt2SQjaZ8KIy5Wv2bL5ptHHXGTx35r7kczO_elgvoyXWv_lX-drzmEMxTNQyy8YA8y1pR3kM083Wm4PswRITlkdNzCmcNKU_2yRBF9nMsWfnqiJKYIehNfz4IioqjQF93tG3jP47SuSsGjl7PFWonkRTcuJUQedzUmpDE50mSC0XYCrdQvsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسمای محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66861" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66860">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
قرارگاه مرکزی خاتم الانبیا:
🔴
پرواز هواپیماهای نظامی اسرائیل در نزدیکی حریم هوایی ایران یک تهدید مستقیم محسوب می‌شود و اگر ایالات متحده اسرائیل را مهار نکند، ایران این تهدیدها را تحمل نخواهد کرد و حق پاسخ را برای خود محفوظ می‌داند
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66860" target="_blank">📅 13:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66857">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oo9oZVqERXKjmwXTpesSOcxfIK3aYviuAMHyDSiybq3cAD88M8EkFNjBou2OEMxQgawpJETCZBi_KOYPFCUkXYojrWD2Qz_wfk0gQat4aRY97uS5XuTmg_ZcD-QbXX1GmjEgu8INxsMgo-bu-CSy2CM1jdLhSh00Mano3jbR9X158m7A3nM9emv05alybIA524LNRuJlxjBJytZijWS2odW4x_H4Y3epDDyvISN-kS1PdlrtMnT0m-kuLQgFbHKvoIAEpxafc6xiQZqXZVL5iJLi1tRc-zW__3I4-CbYo9AGHC_TKO57IVccZasJG6s2buhPzzfNZ5mGcJDoRZTouQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7GizzHGf8hvvaBAEApqeqCRlR2ZJeOgigwCWvJutssSZOSOlhWJxBZiVfC4fDfjSVAGrbBEEruiVAgHvqtphLpqv6YlxmYIqeC-H51h7KaQQ2hq7lIto07jji0ukbnYh4MxxeZSS-dLMz1vTPnZHyjMpMZCDgfF37-ASghRIinvQE9mgB2AlhiAPLyVUEOLvieZ_bE7k8TZ8i9qOBlvn7iEsEtxFHMRsrlxwHkvR-Br4dhoFQ1ZvPs_8mjfF2ekIGILwJdG-_yW2l3UfasHw0AMuAEhXDmJNPYY-FuJQtQIM3YdRdbPAfKDOMzxcZkIh4_2absD8FCF58KiajXuWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URih0d8VX1o8K7N46CIbvO4OH4PgK9l9tpn6x4kZnELTLrvpbM3SC7kCoOYfLBc4RcXDUyATDbcvmxFJ0W4rJE1j29p5pyQ2Om_WUcWplPjKx4uJyyYc7WuAiUmb4KbY4WMEFsvvJKxErARC9jAbaNewRqXOR0QUOw-HB8MU66oqaqNWEtRceD-K4yg_CaumXlUUuf-Mp0zGuZ_KAIfeRWrXXYDtyFXCdGAvf9m_EbiirsDVNhEg7idDTBPLtYEOleFiq0Y_Sk6aCg4pRoaE96SB-wV44GavelJHFLLJqsu2Z-XiNUCc2IRb1Q9rR_Sm0YBPq-q0HHsdvzc5zqjsPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حملات هوایی صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66857" target="_blank">📅 12:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66856">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=lAf6jOf4_85WDzYRyCrMHBCu2m79MxePKfOgxW_aXTUIagQ59yQlIHxyUtH7HPdSKFEdXd6w8bvEpTBwBNfepmeIwIJu_W7C9YfxdilaXn53IvHpJiYz00lyIQYRUVofRj33c-S18WBcHuVfQokzPjC-8IYFqtUdC5xtAdKLejdfxVRvTgiJpwqBEjtjIKvlcVvvGLJRlBSij8V2wFaEKmUwl6m77EtdYEYIHvq-g0NG0dy4Ape5D-eUO_U8rDwRdZOwqUxUhFqPenibKKoMaJIHly34Qx6CpLedBH2MuJKGeBq7J_LoVLc-hXn_RAxMc4LIWBaqBhIXsa7wv0JpHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=lAf6jOf4_85WDzYRyCrMHBCu2m79MxePKfOgxW_aXTUIagQ59yQlIHxyUtH7HPdSKFEdXd6w8bvEpTBwBNfepmeIwIJu_W7C9YfxdilaXn53IvHpJiYz00lyIQYRUVofRj33c-S18WBcHuVfQokzPjC-8IYFqtUdC5xtAdKLejdfxVRvTgiJpwqBEjtjIKvlcVvvGLJRlBSij8V2wFaEKmUwl6m77EtdYEYIHvq-g0NG0dy4Ape5D-eUO_U8rDwRdZOwqUxUhFqPenibKKoMaJIHly34Qx6CpLedBH2MuJKGeBq7J_LoVLc-hXn_RAxMc4LIWBaqBhIXsa7wv0JpHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
«یک بازار جدید دیگر هم در راه داریم و آن، کشور دوست‌داشتنی ایران است.
ایران کشور زیبایی است. کسی دوست دارد به آنجا برود؟ جمهوری اسلامی ایران با مشکل تأمین مواد غذایی روبه‌رو است و ما قرار است بخشی از پول آن‌ها را بگیریم و آن را خرج کنیم. همچنین قرار است مقدار زیادی گندم، سویا و ذرت خریداری کنیم و این روند به‌زودی آغاز خواهد شد.
این برنامه هم بسیار بزرگ خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66856" target="_blank">📅 12:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66855">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v96mXKCX8_KFSe_M54XW81CFadzE43DzePNe_6Bcvsfue8QbqF0T4wqjIt1HIWv3dBeeZ5j2ETzvszRfEJkk8hDZ8j4g-L1YSGK6OXczWIwltfb3BKZVfXfSbofakWA-mDbMjKJcfPkA433XV9FlBDpDZnJUkRUhadudJO2Z40CmlphQojQqkU1RSHyZVd-h9S_X58nbk9id9TWQVGeX2Qkj7X9CQ9XKZfxeOg4_SW1Lcz_lzI_e68llyKwNw3xmRowd6q1-K_PeiI4cSHVtwFfld48F2KaIGaIgaC7gx35eOG67j7Zwz7h63QbDzOj7dGIlCQZc_EPadIhdnSmDgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ:
روند خرید محصولات کشاورزی ایران از ما خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66855" target="_blank">📅 11:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66854">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
جی‌دی ونس درمورد ایران:
🔴
آن‌ها دائماً سعی دارند مأموریتی که دونالد ترامپ برای ما تعیین کرده است را تغییر دهند.
🔴
او در ابتدا چه گفت؟ «من می‌خواهم ارتش متعارف آن‌ها را نابود کنم. من می‌خواهم توانایی آن‌ها برای اعمال قدرت را از بین ببرم. و من می‌خواهم تضمین کنم که هرگز سلاح هسته‌ای نداشته باشند.»
🔴
آنچه دیده‌ام این است که برخی افراد سعی می‌کنند بگویند: «خب، این عالی است، اما شما باید هدف متفاوتی داشته باشید.»
🔴
به نظر من دلیل موفقیت رئیس‌جمهور این است که او از تسلیم شدن در برابر آن تمایل خودداری می‌کند.
🔴
او می‌گوید: «ما کاری را که قصد انجامش را داشتیم انجام دادیم. ما اهرم‌های دیپلماتیک، اقتصادی و نظامی باورنکردنی ایجاد کردیم. بیایید از این اهرم‌ها برای کسب پیروزی بزرگ‌تری برای مردم آمریکا استفاده کنیم.»
🔴
این همان چیزی است که او از ما خواسته است انجام دهیم. هنوز تمام نشده، اما تا اینجا همه چیز خوب پیش رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66854" target="_blank">📅 10:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66853">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=vrN1P1BDMs52dj7hDhH3pjQeJLn7IStnTLa33u5OIIWOkJRUTpvo6_FCR9lL75tNoQxInhL3_m2r26KSoJCvEtsqlczZh_WjygvR_xTYmgGbQa0BmEOLULM_1l_ielMO-46nmY-1zH-Cq82FWHYfd10wVe_1kYsiaDIGzCstPtVvntt5pDvfcSfUFniO9z8IflyaT6KDg63SBSPXO1bX8p6IaBqJMs3Vq3gXAegSIQQZvWirYtox4zKV__tAaA8vzMHFJ2qFJqr36Oso2vyiJn5zukYBSKpPG3MVSNWyVSz9X4chwSLsf77oU7qSppVXBxV51RjJPGOrnkzteIdIsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=vrN1P1BDMs52dj7hDhH3pjQeJLn7IStnTLa33u5OIIWOkJRUTpvo6_FCR9lL75tNoQxInhL3_m2r26KSoJCvEtsqlczZh_WjygvR_xTYmgGbQa0BmEOLULM_1l_ielMO-46nmY-1zH-Cq82FWHYfd10wVe_1kYsiaDIGzCstPtVvntt5pDvfcSfUFniO9z8IflyaT6KDg63SBSPXO1bX8p6IaBqJMs3Vq3gXAegSIQQZvWirYtox4zKV__tAaA8vzMHFJ2qFJqr36Oso2vyiJn5zukYBSKpPG3MVSNWyVSz9X4chwSLsf77oU7qSppVXBxV51RjJPGOrnkzteIdIsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
ارتش اسرائیل: ۶ عضو حزب‌الله را در جنوب لبنان ترور کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66853" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66851">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=sa5Ip_DbgcwoZqwD-AcC4GsrApaWmKzIU32EKYIkiHVfdyi79lHQSbcpVTeWmggG_dm8dKk4qxxLkVtpjt90LmWu_WTqQq5kLhhlhMPJaUcl03rkTcdsaEM18ZJVz1hpW6YZmFiZI77u3XvwXvp-xWfxRvOXDqvZPr-0v4bq87NDQPxEH9WgdAjJNpC26QMtWqQ79-fauLUdUiI0QJUgPvfcqAQgMVHJ8WpuLtupeE29j0GyF7zyf1BegPgo_dgF2c6D9RM5u3mU5_CDSbVUkDVc3XJPNbDktmUQ5P4xSgA8e277nsw6Juz1FmL_MVfSMGd6RD8R59CUe4DbpL2T1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=sa5Ip_DbgcwoZqwD-AcC4GsrApaWmKzIU32EKYIkiHVfdyi79lHQSbcpVTeWmggG_dm8dKk4qxxLkVtpjt90LmWu_WTqQq5kLhhlhMPJaUcl03rkTcdsaEM18ZJVz1hpW6YZmFiZI77u3XvwXvp-xWfxRvOXDqvZPr-0v4bq87NDQPxEH9WgdAjJNpC26QMtWqQ79-fauLUdUiI0QJUgPvfcqAQgMVHJ8WpuLtupeE29j0GyF7zyf1BegPgo_dgF2c6D9RM5u3mU5_CDSbVUkDVc3XJPNbDktmUQ5P4xSgA8e277nsw6Juz1FmL_MVfSMGd6RD8R59CUe4DbpL2T1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسری و ماسک اومده بوده هیئت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66851" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66850">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=ZCb80iiSKmgTcfDWQdhIoE1q0eCCju9Gp0FV58IeIjAHUPeTwl_oGEzwluyVBFdjojFAiWOys036jLOgBC6RlXH-9_FIoRBnMHo4_PzLqsOTfK3nEbYaTDR_Ltfy5O3vGSqWQSICO-C0ztKkTuwXRES7dXuankJzUGBwvfgi84Q2_WoQjOh4ss1HWdcY5pHIaNza1jUMksJPidn3cG5IETBIJu3kh-ogsI-mKFK4ERIWLGGsbcGKJaEsN_a0uCTUuUe1FlsCRCWZbih92gXfnYvvmeA4k5IFSerRZdJK2UMJdNYsLSOu0akoVBCF4xCa8aRRvo1P-pV38LlOKe9AUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=ZCb80iiSKmgTcfDWQdhIoE1q0eCCju9Gp0FV58IeIjAHUPeTwl_oGEzwluyVBFdjojFAiWOys036jLOgBC6RlXH-9_FIoRBnMHo4_PzLqsOTfK3nEbYaTDR_Ltfy5O3vGSqWQSICO-C0ztKkTuwXRES7dXuankJzUGBwvfgi84Q2_WoQjOh4ss1HWdcY5pHIaNza1jUMksJPidn3cG5IETBIJu3kh-ogsI-mKFK4ERIWLGGsbcGKJaEsN_a0uCTUuUe1FlsCRCWZbih92gXfnYvvmeA4k5IFSerRZdJK2UMJdNYsLSOu0akoVBCF4xCa8aRRvo1P-pV38LlOKe9AUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرماندهی مرکزی ایالات متحده:
جت‌های جنگنده اف-۳۵ بر روی ناو هواپیمابر یو‌اس‌اس تریپولی  (LHA 7)، ناو پرچمدار گروه آماده آبی-خاکی تریپولی/یگان سی و یکم اعزامی تفنگداران دریایی، در حال برخاستن و فرود هستند. ملوانان و تفنگداران دریایی ایالات متحده در دریای عرب در حال عملیات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66850" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66849">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66849" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66848">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndZyia4nc5xR68Boyn9jLKEphX46ZHxSjrP9NwHXQ7dyaS_uKjtjUjwqUFl5AfswT-I_TKR_Dn5JmlxNLUXru2HIc2mQt491lJddOPkaFZnYXOfX2FWcqPPDL1R5OLKCKbXMTWiiVYDBjg0dzgj0S8aHAWbhbdESuvEY4-YGZrjMzRy16jQqLDWGvALifmenKdkyeKRYIUojDxVUG2x9iXnyqVUANgMZB7skE9CCf-W1mmxLWDPKqAQFZG8M0jzh88tz0Cmdx2YOyse3I_O5yvSvXfTZ7w1ZE2XcjTls9N18fVIs2r51Ig4e6bybzlMzw_GxwJsNLEKNEMrA5PA9lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
@Palang_Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
@Palang_Bet
@Palang_Bet</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66848" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66847">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFodfH1BHMEeLUV-gksrkOwWv90cafYgEer2CSI_7_-ESLtNepEXYAi0Bor2TlW1tqeBar5_MWNWf_rRLK4gMGOeYmuEvl1WRQ4uCFVKoL1WcmYDCiK2Y7kHnQI7ZifrOmbPIEKo3j40ltCe8fYbcu0O0h2yfvC6dJ2ePVUXh3XSqOAnBI9qVOAJzdxS49xptvs_N9kBTxPSrPsm1bNvmr3UHolhzOKouIBt8gfbXMj0wIa0p8eYGlyh5o7QbWnp9DuKZA84MsTkTUzR9Moru-_14xh8pLaSFTliWO9Ut8NDVZUqwnPFi3FDMJll1W-eHxRbNg9l3jadud5r5v7arQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏بر اساس گزارش وال‌استریت ژورنال (WSJ):
🔴
ایران روز پنج‌شنبه به یک کشتی باری با پرچم سنگاپور در تنگه هرمز حمله کرد؛ اقدامی که به‌عنوان آزمونی برای توافق هفته گذشته میان آمریکا و ایران جهت بازگشایی این مسیر حیاتی کشتیرانی تلقی می‌شود.
این حمله به پل فرماندهی کشتی آسیب زد، اما هیچ تلفات جانی در پی نداشت.
این حادثه چند ساعت پس از آن رخ داد که ایران به کشتی‌ها هشدار داده بود از مسیرهایی که مورد تأییدش نیست استفاده نکنند
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66847" target="_blank">📅 01:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66846">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رسانه های اسرائیلی اعلام کردند طی درگیری ارتش اسرائیل و نیروهای حزب الله در منطقه بیت یاحون در جنوب لبنان چند نفر از سربازان ارتش اسرائیل از تیپ ۷۶۹ مجروح شده و با بالگرد از منطقه تخلیه شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66846" target="_blank">📅 00:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66845">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">با بحرانی تر شدن وضعیت ونزوئلا و مفقود شدن بیش از پنجاه هزار نفر گویا به نظر می‌رسد مثل زلزله سال ۲۰۱۰ هائیتی که ایالات متحده آمریکا به این کشور نیروی امدادی/نظامی ارسال کرد دولت ترامپ هم به سمت همچین سناریویی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66845" target="_blank">📅 00:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66844">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
وقتی نت ملی بود ، تنها سرویسی که برامون قطع نشد همین بود
🔥
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66844" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66843">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRJafWZC0gW4xafnLy2iqIfR_ceC0a7t0HFhnMICbxCJOVPAoe_zysSyqpvVUWsuXxcOv2h4BnhhgRaxrc-cb2nRMXiSNdSiJ1yYqLmWDI_NaCyZ34rw_S4bYsyx7nnh9LTDG4th17HEKBinIJkXhRTra2__SsuO7rqAj0hCr6R886B35tjayMOP1Nfiol9XzmvZxY9_hPxrx94SxVC8lFJQxKAxWH_EI7mKIEsGfwrgrViHevZDasUgTYcXwxt61sOh5VO0jOfq0iYDuxREed_hOblFeLVTK_l6p57mqYHEea6snNzmuqR7Z4Z7h114qqVIrIeN3eQJ_TAU6l-lPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کانفینگ نامحدود برای همه اپراتورها
🔥
⚡
سرعت بالا | بدون قطعی | تحویل آنی
💵
یک‌ماهه: 380
❗️
پشتیبانی 24 ساعته واقعی
❗️
✅
سازگار با تمام خطوط
🚀
اگه سرعت مهمه، همین الان پیام بده
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66843" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66842">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4mL7GTp1V23oFY9q4z0x4ZuDNLE2u-jiJTjY01K__72hn2wrfKMYiC-stgV3ljSeFP2t1W9_1nE16VcVL-oLkzLIwWOusMYp_TGm1OiVsyYilJYhY5ojXxyEVJS2wFqu_dfYlmuBFLBLpb7RHBRwLFgCWWWJE9zxNTD1qqifHAjdPdhpRQL5wjr_tI_iIubhR706cUgo6IVlrAf0jN4w85cFmiSsomHvp1pE-Tb4FtIC7q9diM-DEi_-l_eLwE-xAXwYwLIwF9ls6IIBMOS71QdD2R-lFeZTnvf8dT8LJCAvZQngl4GL50-dldh3RV7tAPgTu3kXlg1KkCIEUS5Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش از لبنان: جت‌های اسرائیلی به بیت یانون در جنوب لبنان حمله کردند.
این پس از تهدید امروز سپاه پاسداران علیه اسرائیل صورت می‌گیرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66842" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66841">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=P2qUy96XyZOYhxUWdA_isHljWQsVuU6QylA-kc_5xJjimKjbm5Abrz7Tt4qMHGmWfApwgZFNWwcxP2PoiyxsU3dtHjDf4HGD53JkTTZsQwUqeWw_oOfnt7kcT5rvewheM6TwpgMY5RqdBGzSmC6MzsuSFp17yHgEPBHjfadll31VHbaJw0z58tt60fDIDp0h-WFMGohrKLNB3pOHQ-m13k5ppHDOnuWZ4tqlLzTsccCMxhrOYRZc5PXOJX094pv3GaBaT9UhCTzRX3SHPcLHEbcWFQsHRPwZOsCZV9XK9yVerURqmUr0K6ihFRDehoTIil1-wr72q_o9zc4eNWZ-LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=P2qUy96XyZOYhxUWdA_isHljWQsVuU6QylA-kc_5xJjimKjbm5Abrz7Tt4qMHGmWfApwgZFNWwcxP2PoiyxsU3dtHjDf4HGD53JkTTZsQwUqeWw_oOfnt7kcT5rvewheM6TwpgMY5RqdBGzSmC6MzsuSFp17yHgEPBHjfadll31VHbaJw0z58tt60fDIDp0h-WFMGohrKLNB3pOHQ-m13k5ppHDOnuWZ4tqlLzTsccCMxhrOYRZc5PXOJX094pv3GaBaT9UhCTzRX3SHPcLHEbcWFQsHRPwZOsCZV9XK9yVerURqmUr0K6ihFRDehoTIil1-wr72q_o9zc4eNWZ-LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
«شما قبلاً آن‌ها را «دیوانه‌های دین‌سالار مذهبی» می‌نامیدید. آیا هنوز هم فکر می‌کنید این توصیف دربارهٔ رهبری کنونی هم صدق می‌کند؟»
🔴
مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ببینید، موضوع این نیست که من باور دارم این‌طور است؛ واقعیت همین است. نظام ایران توسط روحانیون، یعنی روحانیون تندرو، اداره می‌شود. همیشه هم همین بوده است... البته در بخش‌های سیاسی حکومتشان هم افرادی هستند که ظاهراً انعطاف‌پذیرترند یا تمایل بیشتری برای همکاری با ما دارند. ما در حال مذاکره با همان افراد هستیم. باید ببینیم نتیجه چه خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66841" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66840">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345e633380.mp4?token=bjmCyKpod0FvrEZTqNqs7gBTpPlzQ4ACvFsD3gC7e3iIMcAfg4kf96tOf3eDB_oDn3uQYQRPxQ_8c1XiLZ4BeTiH-EQTh3u0qy2W0riBkGOTfGKj8QoEOEZja-OfXg53rZNkhUQlQOp1VjM6SPQKctqsWRZU_lm3x9d0zoKpCTPzyrKNg4b6GQLXI-WEv8iucFPEfqQgvTxNGoXofdfnDtWAiJlnbWcGLFe3DkDbCtqE8yn2w_A8SUUlcWJ5BsvhNr6gQrdYAyn3yRgSc4KPhSLjEQpZcLwq4xzZF6ZvOJtk3KeFRE-np0ERcqIPcRo9i5iupaNH4Mh_63NGW0Tpmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345e633380.mp4?token=bjmCyKpod0FvrEZTqNqs7gBTpPlzQ4ACvFsD3gC7e3iIMcAfg4kf96tOf3eDB_oDn3uQYQRPxQ_8c1XiLZ4BeTiH-EQTh3u0qy2W0riBkGOTfGKj8QoEOEZja-OfXg53rZNkhUQlQOp1VjM6SPQKctqsWRZU_lm3x9d0zoKpCTPzyrKNg4b6GQLXI-WEv8iucFPEfqQgvTxNGoXofdfnDtWAiJlnbWcGLFe3DkDbCtqE8yn2w_A8SUUlcWJ5BsvhNr6gQrdYAyn3yRgSc4KPhSLjEQpZcLwq4xzZF6ZvOJtk3KeFRE-np0ERcqIPcRo9i5iupaNH4Mh_63NGW0Tpmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری:‏بهای بسیار سنگینی.
رئیس‌جمهور ترامپ این جنگ را آغاز کرد،
و وعده‌های بزرگی دربارهٔ تغییر رژیم داد
و وعده‌های بزرگی به مردم ایران داد.
آیا ازنحوه‌ای که آن را به پایان رسانده،ناامید شده‌اید؟
شاهزاده رضا پهلوی:خب، نمی‌دانم هنوز تمام شده یا نه.چون همان‌طور که می‌دانید، هر چند ساعت یک‌بار ما یک توییت متفاوت از این
رئیس‌جمهور دریافت می‌کنیم و ناگهان موضع
از یک چیز به چیز دیگر تغییر می‌کند.
بنابراین من خیلی به هیچ اظهارنظری
که مطرح شده، وزن نمی‌دهم.
و در واقع، من فقط، می‌دانید،
کمی دنبال می‌کردم که
در به‌صورت زنده چه می‌گذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66840" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66839">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">#فوتبال جام جهانی فوتبال
📊
2 گل آلمان و ساحل عاج  کد:YXA6P ضریب:2.3
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دانلود برنامه ملبت @Palang_bet</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66839" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66838">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=o8BAnV8FQlHAGJ3tdQWp4K5TFjFIvmidraQjrshzqWm7df3-WTBk3hy3LT-zaSnLHD5-Uu9gSv4XQF05CvmnDsTlWnHG_OAUNcN6wZbj_gkzk8GcQ29XN9sYYmL4HyMqszMcB-g4KdNHyYqrm3LCIZn1hbkyBsrIfHXAqD4FPGkD7ofyCQubCj5Pr_qhWDyTfkMjLo6y-1ZDWrPPXSufMp5tM2yTRccWwonnJCcLkJBRDgxXtwttQ9d8OFI8uct2fID6kk3IVSHe5YDcdK5qqqWc8LvtLe0UndgfXf0PSHfAHZRGPmyp0Qpx4yRYZKxWSMX9EFhJPdGbJE-D4bPWVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=o8BAnV8FQlHAGJ3tdQWp4K5TFjFIvmidraQjrshzqWm7df3-WTBk3hy3LT-zaSnLHD5-Uu9gSv4XQF05CvmnDsTlWnHG_OAUNcN6wZbj_gkzk8GcQ29XN9sYYmL4HyMqszMcB-g4KdNHyYqrm3LCIZn1hbkyBsrIfHXAqD4FPGkD7ofyCQubCj5Pr_qhWDyTfkMjLo6y-1ZDWrPPXSufMp5tM2yTRccWwonnJCcLkJBRDgxXtwttQ9d8OFI8uct2fID6kk3IVSHe5YDcdK5qqqWc8LvtLe0UndgfXf0PSHfAHZRGPmyp0Qpx4yRYZKxWSMX9EFhJPdGbJE-D4bPWVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مفقود شدن بیش از ۲۱ هزار نفر در پی زلزله‌های ویرانگر ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66838" target="_blank">📅 23:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66837">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFm06uSYg6159Puts4R1f_fpEhfqXtoJ7eyjgLVjtnMxjCLgrh9Lb-btuuY3_h-vV6xwg7H75UQSxhg_2dAuKDJbgb_seP1ty53gdBFDuY0mGyWxIxZs8fM0K1XGHSfJmaS5Sja1UimKL-chjGK1RkRXWkx197oI9cAl8xQ5WzG-a27Y-BBcwW7s01gOKlZpRHiJp08NJ1zljPzQ9E21hAag39Y2bjgb65f6VU6XfivzUmA5YyIQEpm781NvGvs3CbBOHOGV_nQcxLd_5dRXqDV0yrFuA6RPWy1Zm-LItURLndxvGmD88GxL09x55nvbD7pXZxljl72xUGtO84A8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
پس از بیانیه مشترک اخیر در مسقط، تماس تلفنی سازنده‌ای با وزیر امور خارجه عمان داشتیم. ما مجدداً تأکید کردیم که ایران و عمان «برای تعریف مدیریت آینده و خدمات دریایی در تنگه هرمز» گفتگو خواهند کرد. ما مصمم هستیم و این کار را با همسایگان خود انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66837" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66836">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=oSmrcDH3bi__OqeZLupTGPKauVojLwNvDZn0_AncEwRo6JSMe5TqDC53UKXvQWc1zHzMWiGLe_0TRQL-0-0GrKELQT71uRTgxFOA42BcH6rBGa-Wx3Khpz31EhWjWYX2UWpMNfmI019aA5rb3VDt69ZPs2hqx_GWqi9-fAd2b_4GreaOiT4E6mq-x4WQ1WNSMi_xNQYE9WIsUe46FRD3RJIHCVfsvlTNVAvyacZHSchnIcXD-kzfSmynuLzEwENgXQ_zarPJKBwMTAzsVNB6JpNy8-l_KNlWOmxHSWVHYiGWQJCU0WaZZiZUN2mjldOAk_dPTYLwHuhvm7qrsV4bLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=oSmrcDH3bi__OqeZLupTGPKauVojLwNvDZn0_AncEwRo6JSMe5TqDC53UKXvQWc1zHzMWiGLe_0TRQL-0-0GrKELQT71uRTgxFOA42BcH6rBGa-Wx3Khpz31EhWjWYX2UWpMNfmI019aA5rb3VDt69ZPs2hqx_GWqi9-fAd2b_4GreaOiT4E6mq-x4WQ1WNSMi_xNQYE9WIsUe46FRD3RJIHCVfsvlTNVAvyacZHSchnIcXD-kzfSmynuLzEwENgXQ_zarPJKBwMTAzsVNB6JpNy8-l_KNlWOmxHSWVHYiGWQJCU0WaZZiZUN2mjldOAk_dPTYLwHuhvm7qrsV4bLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
روبیو درباره ایران:
ما می‌دانیم افرادی که هنوز در بالاترین سطوح آن حکومت حضور دارند، همان کسانی هستند که به همان ایدئولوژی و همان طرز فکری پایبندند که رهبران پیشین آن حکومت به آن باور داشتند.
نظام ایران همچنان توسط روحانیون تندرو رهبری می‌شود.
همیشه همین‌طور بوده و همچنان نیز همین‌طور است
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66836" target="_blank">📅 22:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66835">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=BRuj3x6ARAPp7zMP_wB_A2tiW6YjGhacu3xqvC4RHpT3vBChRpXlxD1x8Zub29qPRnynPdDc7a9l6nkqZvz95e4xTaidxRkaAQ2VNkab8ThvVEYJ_ZdPYWR2ObyYP2Ud57H2SUvjNORJuZbJsyS_DNmYaR46DiBIlVMEGBswaxNr20KU7GbTLfRZPb2az0vIwTOLJGUZ6ZpU0ZutICh187e0L0dQwQv4hXmidb4KPII4cmh9qAUc9j72N7jy51c0ysqlMYn48-Zx9foYFRWtuoP8CpEg0lyZSGnhHziUapvSQaPp0x8Xwq79f5LWElnkcgCxtAjMewkHKLtFVSxaAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=BRuj3x6ARAPp7zMP_wB_A2tiW6YjGhacu3xqvC4RHpT3vBChRpXlxD1x8Zub29qPRnynPdDc7a9l6nkqZvz95e4xTaidxRkaAQ2VNkab8ThvVEYJ_ZdPYWR2ObyYP2Ud57H2SUvjNORJuZbJsyS_DNmYaR46DiBIlVMEGBswaxNr20KU7GbTLfRZPb2az0vIwTOLJGUZ6ZpU0ZutICh187e0L0dQwQv4hXmidb4KPII4cmh9qAUc9j72N7jy51c0ysqlMYn48-Zx9foYFRWtuoP8CpEg0lyZSGnhHziUapvSQaPp0x8Xwq79f5LWElnkcgCxtAjMewkHKLtFVSxaAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66835" target="_blank">📅 21:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66834">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaMrAMSbnV3FT-mM-xxwHQ3amFfNakz27PkmkZE8fFHqQdWCtI9THx-4RZxMHffieIm16Kyttponq9GBj1h0Cslxk-QVkWwEb5VeWhttNK1fVKbRJxo7e0kpiHsv9WREnG7i8h7cXepEDoqJCLQ5AEFbvvZQjQWOjGDlOJwERwIUP8mTzBC3jCSnzAanpetUBKomgYHDuPdsP1dYKgdzXpM0Yt7wfNjnFx1FrpyyzmWkHJ2jdMEhjF-E0LV290_eQ5rqdlMD2-tXD4BJrqZoH4XQuqeJdYxuMsNEZFX2wGdApxq-cEOLLy0c2n7bL81XgFMiKaNhpp7C6ST25iyEXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه پایانی نشست مشترک شورای همکاری خلیج‌فارس و آمریکا:
🔴
تاکید بر اهمیت بازگشایی تنگه هرمز بدون محدودیت و بدون اخذ عوارض عبور.
🔴
تاکید این که هر گونه تجارت یا سرمایه گذاری با ایران باید به انجام تعهدات آن به موجب توافق منوط شود.
🔴
تاکید بر لزوم خلع سلاح همه گروه های مسلح در غزه.
🔴
تاکید بر ادامه حمایت از دولت سوریه در بازگرداندن خدمات، فراهم کردن زمینه های بازگشت داوطلبانه پناهندگان سوری و مبارزه با تروریسم.
🔴
مذاکرات لبنان نباید به نتایج دیگر نزاع ها مشروط شود
🔴
حملات متجاوزانه گروه های شبه نظامی مورد حمایت ایران در عراق علیه کشورهای خلیجی محکوم شده و از تلاش های دولت عراق برای حصر سلاح در اختیار دولت این کشور اعلام حمایت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66834" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66833">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965348f417.mp4?token=AtTQKXhE17j5vi7mJz1Wy7jylGrA6aNY6HbW-PqFH2zcsdCXVNXBLqRKaR9vL7EfjcSy2u9Wsazp_uwb1DV3uECRNxpdqEuqTpc9y9mFdR-W-e0jkbH_wEfShOy67EU4himKk9hVpNlHIAmtr5_02V1iTTu2eiSW7_7HGQirU1DKiHf9_lo-hU4mP3_6urwUfFwFiTb-g5_G35__ldTYqscmaZvvukvbcaiSwDz55zvX0wQ_6nUm95NBCsC54tnlMErO4UB7i5Ayla36AkwMkL4cH3z6XgriudmHYwMAP4gBtx7soj1Do3Z9UjCjqIAr0WTRdhWj5qCt2WtSUVv8rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965348f417.mp4?token=AtTQKXhE17j5vi7mJz1Wy7jylGrA6aNY6HbW-PqFH2zcsdCXVNXBLqRKaR9vL7EfjcSy2u9Wsazp_uwb1DV3uECRNxpdqEuqTpc9y9mFdR-W-e0jkbH_wEfShOy67EU4himKk9hVpNlHIAmtr5_02V1iTTu2eiSW7_7HGQirU1DKiHf9_lo-hU4mP3_6urwUfFwFiTb-g5_G35__ldTYqscmaZvvukvbcaiSwDz55zvX0wQ_6nUm95NBCsC54tnlMErO4UB7i5Ayla36AkwMkL4cH3z6XgriudmHYwMAP4gBtx7soj1Do3Z9UjCjqIAr0WTRdhWj5qCt2WtSUVv8rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
فقط یک آدم کور می‌گوید هیچ دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
من همه آنها را فهرست نکرده‌ام چون می‌خواهم شما را نجات دهم. شما اینجا زیر آفتاب سوزان ایستاده‌اید - فهرست کردن همه آنها زمان بسیار زیادی می‌برد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66833" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66832">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_aoGu43WVXjR1dPu3ZEs939j67d2NFi7aTfOzZ2hTwvducRzSu8Suw-iZcCvs7xyhfO5FH5WS2bJynJG6NTUSdvw6jGbM9jQsuHZ49xAWPVf29xTYo_8I8CQkp2W1eGq5vdnGPcQxgTGmSqDlTGK-1lOTE9nuiQ0OnGxCgT7nk1yqv6SA5WjUeWgiESxLwvofDwLUnyf4t4_5fvtO9E6sb2X5rJ_y_KGSws-8ked9XGRh39B1wuTCmS8PSemoaEZwRzIPvSyCb7lcVGagfH51BAICrpThYZP7flQXsB5Kyrb9r-vu0vK0yvl0UKmbR_xm-_D55iBnluN0rsVkjreQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
با نهایت تاسف از وقوع زلزله در ونزوئلا. مراتب تسلیت خود را به دولت و مردم ونزوئلا، به ویژه خانواده‌های قربانیان، ابراز می‌داریم و برای مجروحان آرزوی بهبودی سریع داریم. جمهوری اسلامی ایران با مردم ونزوئلا ابراز همبستگی می‌کند و آماده ارائه کمک‌های کامل است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66832" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66831">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">این آمار فقط مال روز اول جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو پلنگ بت جویین شو بهت آموزش میدم چطور پول دربیاری و تا اخر جام جهانی سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet @palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66831" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66830">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llxYNhNIWIaU4MiAMeKCVvXebzsr4r3CqJZmbcR1Gt4K6tz6EwuwGz-sWxcIIne1doBxcikKsgQBhhwyF78fb1n4dvOwGCMaj6xZPVSQ6-P4GOjivO37M6GfTRkJ5GDXhiAsm-81eDHJFl447XLrpELnleUJRCNtOTuJAclyLsVG3NjrTpz-bjFzV_SSm8eo3tnqUYo9xbeNlch0gMzY-PlJAZVg3MskdAHKnEowuUwl50VLS-TUJWlgrC4D-Sg_mQFmHkeIVoNzb2Qem_LDzEYKAjiNPeCpxoQjgRs4ADj6YjOeCekRNASUsZmlx7ersOQthC7pCHlD5LaONPl_TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66830" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66829">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=dDxMCm1-fJS-8SNWQYOG3i1d0yDYY8Wyb2vGZKs_-3500OYimRpetVubco4I93FQHfPqSmpZqfYuvxcRdxdOYowTfwzBYH_tIPTajbNx_odgz1yNLfV8YFBb06SdVySd57IFGm2O7-T3TGVfXYODWCcrt8np6iMCxMFdsq7RlyNqBARTUS-4jkVPsGg-i3Oc7s9uGZyLgFqoUGaAJLxzdPG4mzHaZx7sjCxanc1jSjioBNhNE0O9QGivJmASWSb-SUJlP5j6ty-3QvCAGrwCfjlXW6VSeaiFBbtOj1ZSArenO-vtNka8Fibxy4P1a2pOZwI9nMcOYUq0eb6s23-mvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=dDxMCm1-fJS-8SNWQYOG3i1d0yDYY8Wyb2vGZKs_-3500OYimRpetVubco4I93FQHfPqSmpZqfYuvxcRdxdOYowTfwzBYH_tIPTajbNx_odgz1yNLfV8YFBb06SdVySd57IFGm2O7-T3TGVfXYODWCcrt8np6iMCxMFdsq7RlyNqBARTUS-4jkVPsGg-i3Oc7s9uGZyLgFqoUGaAJLxzdPG4mzHaZx7sjCxanc1jSjioBNhNE0O9QGivJmASWSb-SUJlP5j6ty-3QvCAGrwCfjlXW6VSeaiFBbtOj1ZSArenO-vtNka8Fibxy4P1a2pOZwI9nMcOYUq0eb6s23-mvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من ادعا نمی‌کنم که پیامبر هستم.
اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقهٔ ما ـ و به‌طور فزاینده در سراسر جهان ـ تعیین می‌کند:
قوی‌ها زنده می‌مانند.
برای ضعیف‌ها جایی وجود ندارد.
آن‌ها طعمه می‌شوند.
و از میان می‌روند
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66829" target="_blank">📅 20:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66828">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=OvLB5gIUsTw49g1Nqjhc8yqZHaqx7rqRCUIPvDsAzL2BP4vpxJKnJEWaOLORO5yK3JSs5j1pNZ3u_LY3pTccSYsJnm84OELxv0MXugX5Tp7dcHz6v4BsGr8ntBEitpVuKmoCbEBb-5xqeUbT7Viox94_eXttJSs8NVv6Z8udK0fqTgR4YZDXFwRxJvi2fToGw8pzM_Evn003oj2eSq8SJZ-i4xE1_LZXKqne-A3Y5SurhhNNvRiX9nJwctm1NqnhqCB1Edb6b2O3x1zSFIIZZbMBgVZRyENdz6G4lwska2e_8eEbpCCzmvIp3SmCbSkSss9R7mqKYz_uQpyVAnBO9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=OvLB5gIUsTw49g1Nqjhc8yqZHaqx7rqRCUIPvDsAzL2BP4vpxJKnJEWaOLORO5yK3JSs5j1pNZ3u_LY3pTccSYsJnm84OELxv0MXugX5Tp7dcHz6v4BsGr8ntBEitpVuKmoCbEBb-5xqeUbT7Viox94_eXttJSs8NVv6Z8udK0fqTgR4YZDXFwRxJvi2fToGw8pzM_Evn003oj2eSq8SJZ-i4xE1_LZXKqne-A3Y5SurhhNNvRiX9nJwctm1NqnhqCB1Edb6b2O3x1zSFIIZZbMBgVZRyENdz6G4lwska2e_8eEbpCCzmvIp3SmCbSkSss9R7mqKYz_uQpyVAnBO9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت. به هیچ وجه اجازه نخواهیم داد ایران بمب‌های هسته‌ای توسعه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66828" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66827">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66827" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66826">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_-HevtFZO-1f_K0SfqINcCjw_upTjHC2_1y0CJM2z94Gwx5VPdx1TvgLwikSLXFwhfApwKfw38HUb_BjS4s6bTIPaZeAit1EkD6YUr_SlkHOuji39OUkduWyLkwJQ8J6sIfdGPSGsnkrB4y8tBO8-0dmIYiWMlPj6_k41Yo78U1THST-eN9x-PtHAf7QIV47PUzFd1ic-BjN7dVAWfxMDHbbAjTMLDjdswEEsczdvLgNRt2_KkBAtky0Rt_BQdpZfRlhTd3kSdwk2rUGmVvYSvnHPwze9aRvbN_M4ssOtl_OkFSvqMofAUzEUGWTiV5KIa0TY-NBBLQ8JcZW5MjSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66826" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66824">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_OPUm93Ik-QpjsxsyS6EU6Lv2QsZgOgS0aUaxwEeW1j_eg_cG60jOxFSEP1pwkO_C0bt9ajYF3Xz208iLkrZkFcwwu7V1_oBSME6-ERn0GCRGX3oRizxdi8O1BPq15RRlg74H6Obq5-IpU0Zz_h-LpYI-QolaIIAHd9E0c5QdYnbyqjxkQ6TLGRG9bzGN5c3FNpxPtap-4ShGsH4nciRkDmTJegVlKsQuAgXUvsaFCakDlJFTvIQCvE6KK-AeUBlMwQHclP7RBPwBjQNOh9Q2ZMZWW6YfVVtuxhGIQ20Zu4rRjNGljhEs-CR48H6QrWt7k4VaSOvBX-8vEOXGGyBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=ihuWcx9p8jyfSY_vaDi139_lg4O1H1PJloO3ziPqrowthV5dCvq_3JXxpp6-GCjH1rOPWzu6wt2Jziao9mxy6YNKVVx_FA_R8fDccdKBwoDINEZSUvjczLSLyThG_wJP1XG1IoRDn8BRQxhGpg8K0o5EKggzrtgZr6oaUlwkgCAHQxWBdLUCX0Bn7L6gDyAWq94nWIQ8p_WLQaOyNjXdxh4WRML8UDjEvsBaVWFmFmsKT7hlNfGlgotKUqL_oYlrSbKl0LzJakYlXyXXmSGfZ2jHWKAloRRYDh9syncPZX6B4rvo5ROblPwVw6yFzs3f1RGDw2T-gQlNe7sJX8UiXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=ihuWcx9p8jyfSY_vaDi139_lg4O1H1PJloO3ziPqrowthV5dCvq_3JXxpp6-GCjH1rOPWzu6wt2Jziao9mxy6YNKVVx_FA_R8fDccdKBwoDINEZSUvjczLSLyThG_wJP1XG1IoRDn8BRQxhGpg8K0o5EKggzrtgZr6oaUlwkgCAHQxWBdLUCX0Bn7L6gDyAWq94nWIQ8p_WLQaOyNjXdxh4WRML8UDjEvsBaVWFmFmsKT7hlNfGlgotKUqL_oYlrSbKl0LzJakYlXyXXmSGfZ2jHWKAloRRYDh9syncPZX6B4rvo5ROblPwVw6yFzs3f1RGDw2T-gQlNe7sJX8UiXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فستیوال محرم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66824" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66823">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=tl8k0S2-N8lvq2fRwTxKY7LllDUIPO1GOGv_pHBVWJMSDAYJUl9ZbWnaZL-lCMsqy_DQ97ncZa5jqBts8x9XIBvJETyYwlHr2odAJ9X-ER5-a_655lWrQebAQZS5s66yOEYD8buqBUktQNLWj6_pbqDmmZG03X-Cc8RobZe6tF0-AYSbkDQMcLt4tSe26y0eEkmo9BWQXiwSotadOeqvpaGi5HgTFKRJG3QfTQD83NUA4ZqHr0qg-0ZATMt15Su32HxouboVwcltE821kwAXCGuiQ-6hIE_ud_1r8Sxw8wNqrnupuaAS9a6TCJA0vwTi6Dyhq-kYrJGsKGmR0TfMjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=tl8k0S2-N8lvq2fRwTxKY7LllDUIPO1GOGv_pHBVWJMSDAYJUl9ZbWnaZL-lCMsqy_DQ97ncZa5jqBts8x9XIBvJETyYwlHr2odAJ9X-ER5-a_655lWrQebAQZS5s66yOEYD8buqBUktQNLWj6_pbqDmmZG03X-Cc8RobZe6tF0-AYSbkDQMcLt4tSe26y0eEkmo9BWQXiwSotadOeqvpaGi5HgTFKRJG3QfTQD83NUA4ZqHr0qg-0ZATMt15Su32HxouboVwcltE821kwAXCGuiQ-6hIE_ud_1r8Sxw8wNqrnupuaAS9a6TCJA0vwTi6Dyhq-kYrJGsKGmR0TfMjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف پاسخ مجری صدا و سیما رو داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66823" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66822">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0453856b46.mp4?token=VYZq9ox-wyf-EbCg6SevJYEKhghCH2SrpaWr7UvCblDQxKI3Ycc3Iy4EL4TylnaLnmoplyaYzWlB3WmL_1IkWCHVkuzy3fDr-RLQ5cnK8ruDseTH4DSs_qlcPMT5xBxFMTQGOrX3d8IjlT0oElr_-jcDJAXOnpQoADgof5LouFVJ86a-A2wQfCDP_5jISSbDaS8u0sOr8sbrQ7rOD7gNmMNnNmH1sxeVcvhQZK_1-pmTtRtFvq1sUOZKNe6yOkhTFy0zHUE4r7mNflhUw2GzlxMgOZwXS5Y9qL7Q2muzlTKUElhciDLjUnbej2N7kxnGBs0wXQT4zy2Ut_Hjp196SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0453856b46.mp4?token=VYZq9ox-wyf-EbCg6SevJYEKhghCH2SrpaWr7UvCblDQxKI3Ycc3Iy4EL4TylnaLnmoplyaYzWlB3WmL_1IkWCHVkuzy3fDr-RLQ5cnK8ruDseTH4DSs_qlcPMT5xBxFMTQGOrX3d8IjlT0oElr_-jcDJAXOnpQoADgof5LouFVJ86a-A2wQfCDP_5jISSbDaS8u0sOr8sbrQ7rOD7gNmMNnNmH1sxeVcvhQZK_1-pmTtRtFvq1sUOZKNe6yOkhTFy0zHUE4r7mNflhUw2GzlxMgOZwXS5Y9qL7Q2muzlTKUElhciDLjUnbej2N7kxnGBs0wXQT4zy2Ut_Hjp196SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
اگر کشتی‌ها در حال حرکت باشند، واکنش ما هم بر همان اساس خواهد بود.
اما اگر کشتی‌ها حرکت نکنند، این نقض توافق محسوب می‌شود و در آن صورت با یک مشکل جدی روبه‌رو خواهیم شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66822" target="_blank">📅 17:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66821">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50938460f0.mp4?token=it6zfZIdUlklKBMaFIXQFcnkxyZysxwCOgYE-ZuF2ZsGkUmXJOB8f1HhKJXZQLQ8rIrECYIYw-cFDoQr4QR19bIzLek1Um1GeYj_NnU31Xq4xhuoqFZvJrrsHSJ4-bn3W2R2w973mbZp267R2xkqOZLn4QrzyNyzrPLQPcU5EDSRGhPmtz7RmoAjbU3dKbJIKCGDQKscRUUAepPaiOfQ_QVAcXOaYhqERp0UEeeMJrWipbpNk6CwkF59cvnrjW-0-kgjOuWZLzrfa6IcXnetXyUNk_wTpQxK1mjVfGa2t7b9eRAXQNnhnfyzdgxkF6_EGhSQstiO2jnGHEt-46fuNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50938460f0.mp4?token=it6zfZIdUlklKBMaFIXQFcnkxyZysxwCOgYE-ZuF2ZsGkUmXJOB8f1HhKJXZQLQ8rIrECYIYw-cFDoQr4QR19bIzLek1Um1GeYj_NnU31Xq4xhuoqFZvJrrsHSJ4-bn3W2R2w973mbZp267R2xkqOZLn4QrzyNyzrPLQPcU5EDSRGhPmtz7RmoAjbU3dKbJIKCGDQKscRUUAepPaiOfQ_QVAcXOaYhqERp0UEeeMJrWipbpNk6CwkF59cvnrjW-0-kgjOuWZLzrfa6IcXnetXyUNk_wTpQxK1mjVfGa2t7b9eRAXQNnhnfyzdgxkF6_EGhSQstiO2jnGHEt-46fuNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
فرض کنیم که ما کاملاً دیوانه شده‌ایم و عقل‌مان را کاملاً از دست داده‌ایم و تصمیم گرفته‌ایم با ایجاد یک سیستم عوارض یا دریافت هزینه موافقت کنیم.
این قرار است چطور کار کند؟ اصلاً شدنی نیست. چون اگر کسی هزینه را نپردازد، چه اتفاقی می‌افتد؟
فرض کنید یک کشتی بگوید: “من این هزینه را نمی‌پردازم.” این مثل عوارضی یک جاده نیست که بعداً یک قبض جریمه برایش ارسال شود. به آن شلیک می‌کنند.
اگر به یک کشتی شلیک شود یا یک کشتی غرق شود، دیگر هیچ کشتی دیگری حرکت نخواهد کرد.
بنابراین چنین سیستمی نه‌تنها غیرعاقلانه است، بلکه اصلاً نمی‌تواند اتفاق بیفتد.
حتی قابل اجرا هم نیست. پس بهتر است همین حالا این خیال‌پردازی را کنار بگذارید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66821" target="_blank">📅 17:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66820">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZ9qpO-i7pWC4sGDBTzerD1lc3Z7ipkLFVMDUZc2t9rOCB9e2Y7jmRpRdQHNDwCcDbxHtaqDfRvYiJczawbgBYDp_zCD2HTN9J8cyHnbc9up-noIDlCoWunbUX0tEeRzneHUSQG6miW6C5AlI3XGJBydFJ8DOmuOO-XBEEqriv-Tao4vlzrqKQ1FCI2eXtqTQk1-t1YMC374WhUzWE-bmUUmkEbOBgTI77ZmgGP6zmAW-k6nVhYLGhQRsYonlUG4vtJVjZaok3zBwz3-TKs-90cvXFV69Brg49GdfdPYE1fD38F6HKXSEh9Z0D0pz0iQKIxRfNcnfopphxDxFiAhhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما، کشاورزی آنها را می‌خرد. جالب است. تنها محصولی که ما برداشت می‌کنیم همان چیزی است که شما کاشتید: دهه‌ها بی‌اعتمادی. این محصول ارگانیک، فراوان و تولید داخل است. اما ظاهراً ایالات متحده فقط سویای تراریخته، وعده‌های عمل نشده و حرف‌های بی‌اساس صادر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66820" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66819">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477cde7837.mp4?token=YYGrNxj2lvCAb89WCM5WLdPjQcnt4oPn54-TfJY8laEQk33_R3zELABsaStox4qsd6WaeF96SxCcD53EXYlYEQ6D4N4ZroFiZoGlFBf64UFwoSpJZSRgIU4DzOB0KMHZWmCmLOH3hLN3-h5i5DD06XiPcjIjOzKNgLMdzjgUiEDg4vB5zSK56Hq3VzTQ3B8HTakfU4K8uGWWFlkfwVeljtlNC7faSHHZK_4Q0DuDqeg1OOG738EKHf2uGmZ-GIroYJxxZpPQinFvw9zK2RfJxCCrybWyptY4Pgft8UrY1wWjhOR29f0vHT4g79coWMftB8AWe4PUeQXtMbOr2d5P4Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477cde7837.mp4?token=YYGrNxj2lvCAb89WCM5WLdPjQcnt4oPn54-TfJY8laEQk33_R3zELABsaStox4qsd6WaeF96SxCcD53EXYlYEQ6D4N4ZroFiZoGlFBf64UFwoSpJZSRgIU4DzOB0KMHZWmCmLOH3hLN3-h5i5DD06XiPcjIjOzKNgLMdzjgUiEDg4vB5zSK56Hq3VzTQ3B8HTakfU4K8uGWWFlkfwVeljtlNC7faSHHZK_4Q0DuDqeg1OOG738EKHf2uGmZ-GIroYJxxZpPQinFvw9zK2RfJxCCrybWyptY4Pgft8UrY1wWjhOR29f0vHT4g79coWMftB8AWe4PUeQXtMbOr2d5P4Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویرانی‌های بر جای مانده از زلزله مهیب ونزوئلا در شهر کاراکاس
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66819" target="_blank">📅 17:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66818">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DafAwHGAeBQEpdDKXF6Gs0ZwhBvvJQtLWKvUtsIooCqDt0-cum0wWUMbPYBcSFnMy5YIr_T_xVY-BjJs04fKNYXJ0jR7RbVwneTut2jJZ3Hwa5UPpN43kRd2FW4-luqbKG6UfkAkckjPWaaciN8oQlCDbFydFovn6i47pE9oj9wi4YjvYjWsyK26Gv7JkanY-EHFiQRnBcsTyXSrzNM_kCdEAPCFbJHnkwKhG3Y04tFc3Xc5JEHwecIw28VI6zdsCTjLPlslL7vqjzhSlLctdSjRs23j0icDewF9uY8sErlsrW1E4eMJR97x1HfAFp1t6P-cgIin-o2xZg911wMcGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل قاآنی فرمانده نیروی قدس سپاه پاسداران:
اگر اسرائیل امروز داوطلبانه از جنوب لبنان عقب‌نشینی نکند، فردا مجبور به فرار با تحقیر و شکست خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66818" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66817">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=JCs_n_gONWPccUK4gopH5gX6KKIxMc44Iu0J-KkD-PE0jfvIV5gGYNEYNgxuq57v5paE2Uj8mmWWy0D2l41_4Lj3FhDeR-hXUHS4HPzf9KHYgI9gyaJylWRTKVqphGKjiFtaTyawGm6H0JLkDuWe3k-BSUS_xDO32H6CYvPNxvn3XACXyMqk4x-W3-HEo9uBiOzUAIFFFk9VAf9swyC_Usid_Lsbl5RfhzihiW48Eq0DVwRM13S_i9yq-heydr1xNG9hQL75LHXP0GVGwnV19mUc27nE3OoU0Lq9ZwJ8tsB3v2Mc1VggVsIyTjrxX7hNsKmaRMDinj2dAa0E3YPpjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=JCs_n_gONWPccUK4gopH5gX6KKIxMc44Iu0J-KkD-PE0jfvIV5gGYNEYNgxuq57v5paE2Uj8mmWWy0D2l41_4Lj3FhDeR-hXUHS4HPzf9KHYgI9gyaJylWRTKVqphGKjiFtaTyawGm6H0JLkDuWe3k-BSUS_xDO32H6CYvPNxvn3XACXyMqk4x-W3-HEo9uBiOzUAIFFFk9VAf9swyC_Usid_Lsbl5RfhzihiW48Eq0DVwRM13S_i9yq-heydr1xNG9hQL75LHXP0GVGwnV19mUc27nE3OoU0Lq9ZwJ8tsB3v2Mc1VggVsIyTjrxX7hNsKmaRMDinj2dAa0E3YPpjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
تنها کشتی هایی که از تهران مجوز دریافت کرده اند حق عبور از تنگه هرمز را دارند و با هر شناوری که از این دستور تبعیت نکند برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66817" target="_blank">📅 16:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66816">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auiBK5OGpXw5wxJAJ6xcUL5COGVUHcl900c0y2enWotwN3IWIdgsfvFLxbnhKyfUHS-6ZlGpv0Tew6NiDi0aoI2p1WVTeSAaPB3sfVk0wheNsRdPJ0SGPSaMIlz6MNih1UON4fWFAldFrqIwKzUBbCXQ60wETG_-0H7qY-Ey3pGtqCtwcjH0CcQGBT0zANUWzZB_5pmeNvfv1tmagyN1cm-WeyDCMeXV9cuBjKbiqXmv9RV5hKkGcuVTLw7fCDeFERMnKPv1e434W3L7VzFAia9uC2NRgF4ui9QfoI29ZoAONT5_ozIz80l-Wyg9F3i0-twwDY69elbx8_SjK91Cjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت
ترامپ در تروث سوشال:
«شگفت‌انگیز! سنا رای خود درباره ایران را از ۵۰ در برابر ۴۸ مخالف، به ۵۰ در برابر ۴۷ موافق تغییر داد. رند پال و بیل کسیدی رای خود را تغییر دادند. از جان تون، لیندزی گراهام، برنی مورنو و همه سپاسگزارم. این رای به ایران هشدار می‌دهد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66816" target="_blank">📅 15:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66815">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
خبرگزاری رسمی عمان:
وزیر خارجه عمان اعلام کرد ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض از کشتی‌های عبوری نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66815" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66814">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=uOj9DFl3bG_7FhjLQ-vg0He8YHZ_JwHyTjDNBGODLCjXs729zYKUVy04Pr1SGcBl4NB3oECBif3xzhJfldZSItNYK4CbWb4wQfr5ixZEkOlU4a-u5rxH-bjFKKtvE7q3C1NpopsPTN0K3jgMvORKAcJlzP41SyocVZTCTYEWyGEeKr9LEVe9A2EP2R3K_nZWSDWuBLS__CuMhRIGO83n3alhPl3dlGUUMLmuxcusyqmAbrjd6XQbLOJS50AQuZztdtxZ8ZZXFuGuR2qSeKt0k9f6_YN7iJwhBLPKTbKqlxP3LY3SMcZBXz4oMU5A27QiVE7fYeMMjcUPpA83KjzhUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=uOj9DFl3bG_7FhjLQ-vg0He8YHZ_JwHyTjDNBGODLCjXs729zYKUVy04Pr1SGcBl4NB3oECBif3xzhJfldZSItNYK4CbWb4wQfr5ixZEkOlU4a-u5rxH-bjFKKtvE7q3C1NpopsPTN0K3jgMvORKAcJlzP41SyocVZTCTYEWyGEeKr9LEVe9A2EP2R3K_nZWSDWuBLS__CuMhRIGO83n3alhPl3dlGUUMLmuxcusyqmAbrjd6XQbLOJS50AQuZztdtxZ8ZZXFuGuR2qSeKt0k9f6_YN7iJwhBLPKTbKqlxP3LY3SMcZBXz4oMU5A27QiVE7fYeMMjcUPpA83KjzhUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره اردوغان:
🔴
او دوست من است و از جنگ دور ماند.
می‌دانید، او یکی از اصلی‌ترین گزینه‌ها برای ورود به جنگ با ایران بود.
شاید هم در طرف ایران، چون همان‌طور که می‌دانید، او طرفدار  اسرائیل نیست.
و من از او خواستم که وارد جنگ نشود. او هم وارد نشد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66814" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66813">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTIvpIHU1Lm6_Qby1kLOMTPyYYKDFj-VQGNl18X2N6Y1nfAP_t0X1PkhRMi9_W6CadcK5y6wZMhhbXKoqJFoWZWFRZGDHizPqolIxD8xYnmsY3suVfyG6il1pGHBUgBvOUU3tQAGKSZVWvSWQ-StlbxLmG9fMrJn3K-yr4P9RrNcgkS_F36GZVFiDHmyFmiYu0yc-TpJmkZkeSlICG05yU5Uo953TZaMgxZs6815nX1fTiUzjL1zFYU0GtxmqetR3qjiKB9PhE02h46dXt1G87JAIqhjuEN6hrulUmwTn3par0gMXMrg2MXF0QVuyox4S_3deXcFNMWwR8SIiV47rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
🔴
واشینگتن خواهان توافق با رژیم  جمهوری اسلامی است، اما نه به هر قیمتی.  هر توافقی باید واقعی، قابل راستی آزمایی و همراه با پایبندی کامل به تعهدات باشد. اگر رژیم جمهوری اسلامی به جای صدور ایدئولوژی بر رفاه مردم ایران تمرکز کند، آمریکا و شرکایش آماده همکاری خواهند بود، اما انتخاب مسیر کنونی نتیجه مثبتی نخواهد داشت. هیچ توافقی نباید امنیت، ثبات و شکوفایی شرکای آمریکا در منطقه خلیج فارس را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66813" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66812">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=Tu-nAc-75PQ-J2Nae3X-RNB4qg-PIfA6HDa63J1jBnTMnYiDzM8_2BmybAyfyDajsUULtf9SPDq8qL0YRELicm_RjeVg38nQW6YLBj2LUPl5m-mYsnLhvCfMD75HPwZlCe9J6_mpsVAj3AxtEhzR0tbBAByAG-x_BHOSBDWAC5q6ZA1gcBx3EF3SWknW4AlDnGap3z3tUPmC6pnP72hjibaIc17_trTF7BYnCguYTDqbRF4tagZ7bjg8iZg43gAuu4Vr1VHp6M8Rwv9v5kAfOPxDmnhpYP9E2r2Wn100QCeXxLbqBtnjyfKKpQlYe5_UqSHqp9ynZmU3txyWu_BZfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=Tu-nAc-75PQ-J2Nae3X-RNB4qg-PIfA6HDa63J1jBnTMnYiDzM8_2BmybAyfyDajsUULtf9SPDq8qL0YRELicm_RjeVg38nQW6YLBj2LUPl5m-mYsnLhvCfMD75HPwZlCe9J6_mpsVAj3AxtEhzR0tbBAByAG-x_BHOSBDWAC5q6ZA1gcBx3EF3SWknW4AlDnGap3z3tUPmC6pnP72hjibaIc17_trTF7BYnCguYTDqbRF4tagZ7bjg8iZg43gAuu4Vr1VHp6M8Rwv9v5kAfOPxDmnhpYP9E2r2Wn100QCeXxLbqBtnjyfKKpQlYe5_UqSHqp9ynZmU3txyWu_BZfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتی در کیس بیماری هم عجیبیم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66812" target="_blank">📅 14:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66811">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=Xvd1oYB-rNZrr3HAXfGyqQ_Gfq7H_tVVtxR3hb4xEC_3F8Q1cDCXxev-ZDqATwHzuKpETPwvGVAhZzFWSJF_Vq-XvKYodcoMKaA7l3wMjTnu2eJvnXXB4FXF14-d7LE9aPLbEr5GheOhBOv5-y-xJ8rNDpxY--Knk6Fom6s1sw9wULkJagcV1GdLqMkjELewiKhOTDq-68Fx-x-GvQkOLvFLDQ98xwkw_QXuxTBdgJfRdb6QWUH67ksDwQDy-g_yLKM_m30hyYPkstlO0z1mA0FHAe8CPdX3gcWYz08-lZIJLXxcMta3dicN4Qz9O2qydI7XwsGTvJlIoLcWtb-8eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=Xvd1oYB-rNZrr3HAXfGyqQ_Gfq7H_tVVtxR3hb4xEC_3F8Q1cDCXxev-ZDqATwHzuKpETPwvGVAhZzFWSJF_Vq-XvKYodcoMKaA7l3wMjTnu2eJvnXXB4FXF14-d7LE9aPLbEr5GheOhBOv5-y-xJ8rNDpxY--Knk6Fom6s1sw9wULkJagcV1GdLqMkjELewiKhOTDq-68Fx-x-GvQkOLvFLDQ98xwkw_QXuxTBdgJfRdb6QWUH67ksDwQDy-g_yLKM_m30hyYPkstlO0z1mA0FHAe8CPdX3gcWYz08-lZIJLXxcMta3dicN4Qz9O2qydI7XwsGTvJlIoLcWtb-8eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود ۷۰کشتی در ۳۶ساعت گذشته از تنگه هرمز عبور کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66811" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66810">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.2 MB</div>
</div>
<a href="https://t.me/news_hut/66810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
نسخه آپدیت شده اپلیکیشن ملبت
🔶
• لینک سایت مخصوص کاربران خارجیMELBET:
🌐
t.me/ConnectMELBET
🔶
• آدرس سایتMELBET
🌐
bitly.uk/connectmelbet
🟠
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66810" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66809">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kw_yqYhGEiU_RqYUFrpySChMSN03ZKqnVE65G7IvwR-xkmLBw81Ol_dcXY0RvoRPcknVidXpE5YeYv9k-1RgwFY0KQMTQSU9_imIMOjicTmpDQ4tU5Xxf2ZVDXDiRRtkvC9xzb49TzM19PykMozanZQIcPV942NB1ZBECr7USc_UZhMqeT34jZavvTP_xkZclNZ82D0Sr67gbmPuojxbhVSbyoq2OExEDqdz4J7FUMBhHVGX-5bDMEB_8LmKsCJnzts_WiJaNNCzlNAr5ZqxTDYmiEI-6P51KfqWWdsuUs_RxdYOawi0_8Uya_k_5d0mZoc28elWdA9ynJs_cB-M6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهترین سایت برای بت زدن سایت MELBET هست که مورد تایید ماست و خودمونم چندین ساله توش بت میزنیم
💸
با اولین واریز اگر با کد هدیه
ml_459049
ثبت نام کنید تا سقف 100 دلار 130% بیشتر شارژ میشید
واستون لینک و اپلیکیشن ملبت رو میزارم که ثبت نام کنید
🌐
https://refpa3665.com/L?tag=d_3312431m_45415c_&site=3312431&ad=45415</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66809" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66808">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=UHOxOyW2Pu_FIDtdDkXLYmfD0KekYBnDGsYnjRkEnEiYLdCJOM2Re9B2s7XPWGZ9sjwXdrAno90tdKhsaUmJQ7EjUsw0oDto08JMnPaSRLu9K-aFYbXA4uhF4r2rwLLgA7zWHOHM7wvdMXGyFqphu0MCu2pzt6XICRAakVc1U3SfDLQUzMVbHh1Gb6rWTpXnyi1hJYoukMTg405K0wfWqrbLz1_PThGm6wq5RKTdiuYqXDlu4AiLsNn290jIO1Jmfx1PzsgEib0TlEd-YI3X4fIQ-7iGbgj3-j8HNce9bWzwoYteT6qxf_fwrU72j_-C7oIQmNcMPHQUbgqrip6M9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=UHOxOyW2Pu_FIDtdDkXLYmfD0KekYBnDGsYnjRkEnEiYLdCJOM2Re9B2s7XPWGZ9sjwXdrAno90tdKhsaUmJQ7EjUsw0oDto08JMnPaSRLu9K-aFYbXA4uhF4r2rwLLgA7zWHOHM7wvdMXGyFqphu0MCu2pzt6XICRAakVc1U3SfDLQUzMVbHh1Gb6rWTpXnyi1hJYoukMTg405K0wfWqrbLz1_PThGm6wq5RKTdiuYqXDlu4AiLsNn290jIO1Jmfx1PzsgEib0TlEd-YI3X4fIQ-7iGbgj3-j8HNce9bWzwoYteT6qxf_fwrU72j_-C7oIQmNcMPHQUbgqrip6M9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بسیجی‌های صادراتی دیشب تو میشیگان آمریکا نذری بین آمریکایی‌ها پخش کردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66808" target="_blank">📅 13:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66807">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=bo-HlljdU1j4ABi4HplYYcsTv0FzW-nIc95yHV-UaZ-_Uf_blaEkpqFV0XLs8cCAkKiqEKfwiXsGX2-Ijo2jLPvob0FH5QOqslBo7qrFtyEztn0D_sPmP8CjErk-ytvW6zCOd_WnHIILweJCWOLNvr2PLfSuPjGcJU4hFPJO1OPL8ym1f0vbCGjdn9mDHtl7CPZwYHewNOp-vREqr5LG8hsAdOEIh3_2_NJY3fG6ApL4oU0Kyvfldgjxq9Iq51I9Yos5l0HLAJKcvrl79lJaR0niL4YyWT9zhRWTnGheo1zl0dhXMhHskWa5r4YG4N9sTt64p0JQEyO-A0w0P8hPnjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=bo-HlljdU1j4ABi4HplYYcsTv0FzW-nIc95yHV-UaZ-_Uf_blaEkpqFV0XLs8cCAkKiqEKfwiXsGX2-Ijo2jLPvob0FH5QOqslBo7qrFtyEztn0D_sPmP8CjErk-ytvW6zCOd_WnHIILweJCWOLNvr2PLfSuPjGcJU4hFPJO1OPL8ym1f0vbCGjdn9mDHtl7CPZwYHewNOp-vREqr5LG8hsAdOEIh3_2_NJY3fG6ApL4oU0Kyvfldgjxq9Iq51I9Yos5l0HLAJKcvrl79lJaR0niL4YyWT9zhRWTnGheo1zl0dhXMhHskWa5r4YG4N9sTt64p0JQEyO-A0w0P8hPnjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنوز تو این دوره و عصر مدرن یه سری کسخل وجود دارن که با عقاید عصر حجر خودشونو بگا میدن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66807" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66806">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=VCRswmemrWj1lKUVJGhMJXA1KOKtir_2doLEu9BLxabb2HPnX0_wT5vUREa5aZBWf9hzsDfFRa0V2kAEJTgdCtFtxjzcWEVvbAGhvcyzzmxjkHQSWWatHGg8qwUxJ7S1iOotDTYVyKWvECpkzVsuwV2ONYr22QyylmzX4lSVRSPRqipbWhc4FOpQmgivswSRKrf6xdMiAUVcKHvXM7sUFMaPQOMbHgAPuM458KD8yHr3soHyP9ndy5B4_HYa7RIkFi9FJ0bdbrCro9ZHvMueTz_KvbiYtRpsddMw2Nnd243q9Ftb4kiUKscT6JsjExWP9KL9RLdM06P0Iv-7TuBd0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=VCRswmemrWj1lKUVJGhMJXA1KOKtir_2doLEu9BLxabb2HPnX0_wT5vUREa5aZBWf9hzsDfFRa0V2kAEJTgdCtFtxjzcWEVvbAGhvcyzzmxjkHQSWWatHGg8qwUxJ7S1iOotDTYVyKWvECpkzVsuwV2ONYr22QyylmzX4lSVRSPRqipbWhc4FOpQmgivswSRKrf6xdMiAUVcKHvXM7sUFMaPQOMbHgAPuM458KD8yHr3soHyP9ndy5B4_HYa7RIkFi9FJ0bdbrCro9ZHvMueTz_KvbiYtRpsddMw2Nnd243q9Ftb4kiUKscT6JsjExWP9KL9RLdM06P0Iv-7TuBd0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرستو نظام با کلی عمل زیبایی که البته هرچیزی شد بجز زیبا: قلب من با امام حسینه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66806" target="_blank">📅 12:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66805">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f836563943.mp4?token=axPuZAkAXgDWaKhHUtnkzaGt_rTy-hmhrOPhGaqz2aOE3Orh-WAuUgfKRhWOqEDLChQywJMlM-iGEsI8KA2vV1MifyyLmHPYwd6VLNperuh8xZbm6Dgqg7NOI3kk9OlotdVPqyQL8efrff9oxnQGD4coo2Ikmo7e4PSHqGCMgvwPf7ySdcKopsp6G5Ptw_7tXJpzX8HcZAyITGy1IJOGMowyUJfR1xhoOcs4nrbnQkE-V9mahrzksPDqneCYW_eY1w3P-3p3KaPfbK_rSIdf2dU4OrSMd06-zaXsSqqzHJBSjjwCSSVCuxsARcniO13b6_hvsk4xFSbgEIfSaN60Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f836563943.mp4?token=axPuZAkAXgDWaKhHUtnkzaGt_rTy-hmhrOPhGaqz2aOE3Orh-WAuUgfKRhWOqEDLChQywJMlM-iGEsI8KA2vV1MifyyLmHPYwd6VLNperuh8xZbm6Dgqg7NOI3kk9OlotdVPqyQL8efrff9oxnQGD4coo2Ikmo7e4PSHqGCMgvwPf7ySdcKopsp6G5Ptw_7tXJpzX8HcZAyITGy1IJOGMowyUJfR1xhoOcs4nrbnQkE-V9mahrzksPDqneCYW_eY1w3P-3p3KaPfbK_rSIdf2dU4OrSMd06-zaXsSqqzHJBSjjwCSSVCuxsARcniO13b6_hvsk4xFSbgEIfSaN60Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از هیئت‌های گناوه بوشهر یه مداح به این شکل از جاویدنام‌های وطن یاد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66805" target="_blank">📅 12:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66804">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=pBVZQk8jlHqdG6GtilJsDz-AoI1qddAp8pgzjaO0t_frSkC8puckL0-MPZQ-EHEzhdQkyXVFqt4l7UlNKrvDPFkaL19kQBHyRVeiYlCfFDwqM4MEPOwDImreUBJ3N5kUmNkTnseI-e26kNR1aqJTiplBqQ2RzDF6tAuOiZz1ZLTIxGK9dvvZ8uxPhk89OfjfNHC4Zw7Ns1jN0L9Crr4ooRKA5GOWlMEqG3uAxh_yc70b0h-qxb3gDL7eM7B85SV5B02PVg9oP8qK4c5rra6ZquduZi71rDNwvQf5v18fqoyxEvNIoWXc-7JVrAy7HUH6uYvF5SLAHfl6bsJ9C8O5PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=pBVZQk8jlHqdG6GtilJsDz-AoI1qddAp8pgzjaO0t_frSkC8puckL0-MPZQ-EHEzhdQkyXVFqt4l7UlNKrvDPFkaL19kQBHyRVeiYlCfFDwqM4MEPOwDImreUBJ3N5kUmNkTnseI-e26kNR1aqJTiplBqQ2RzDF6tAuOiZz1ZLTIxGK9dvvZ8uxPhk89OfjfNHC4Zw7Ns1jN0L9Crr4ooRKA5GOWlMEqG3uAxh_yc70b0h-qxb3gDL7eM7B85SV5B02PVg9oP8qK4c5rra6ZquduZi71rDNwvQf5v18fqoyxEvNIoWXc-7JVrAy7HUH6uYvF5SLAHfl6bsJ9C8O5PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیره چرا شبیه یارو خپله تو آل زبیر نشسته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66804" target="_blank">📅 11:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66800">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=ut7ymN3lZku0L-nWn7eqrM1TG-AVNcsfxwujW0CFBsG6hbZ4rIF6iEvQ1HSvcn1jW9CQRPdF1kcsEeSlpfdupOVLRr8_UIx6tvBFxt_q6_98DO3KXUJErRzGC4HpNkHJdjtRdU3QXcgPxEc0Y0D3SUQuR1_2BoCBFAo5_Y-6qNwyQWXp-nzICWZeuA9OhPzd6Y6X6c1PRyFb8JmhWhHhy9DYe_IASkJCOkOx8YVNiW92w2CRf3GrLH-8Fe40h5Hqb6C2N4Szl_3JeQdYVURptRzIIk8bInv-4EtAcfi_nbHr4nwvloubV8i_sZfEFhkBnXga16CZfh8CfFiaAtXuzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=ut7ymN3lZku0L-nWn7eqrM1TG-AVNcsfxwujW0CFBsG6hbZ4rIF6iEvQ1HSvcn1jW9CQRPdF1kcsEeSlpfdupOVLRr8_UIx6tvBFxt_q6_98DO3KXUJErRzGC4HpNkHJdjtRdU3QXcgPxEc0Y0D3SUQuR1_2BoCBFAo5_Y-6qNwyQWXp-nzICWZeuA9OhPzd6Y6X6c1PRyFb8JmhWhHhy9DYe_IASkJCOkOx8YVNiW92w2CRf3GrLH-8Fe40h5Hqb6C2N4Szl_3JeQdYVURptRzIIk8bInv-4EtAcfi_nbHr4nwvloubV8i_sZfEFhkBnXga16CZfh8CfFiaAtXuzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تخریب آخرالزمانی در کاراکاس ونزوئلا پس از زلزله7.5 ریشتری
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66800" target="_blank">📅 10:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66799">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghqxUnobUIOqHxpImE6dXBDu4dyk2ZgEsB6O4_GezwuZAWYjHiEQo_CqJJ6h6ocQ9i0bEoj9qV4nyn85EFM56xGhtNgA72Uh5jJU6ichvdCGHWkGYLgiAKLez0-NjHjVBH6UPIWWCmlekrBaC_etD5AHm8WVDkl-RkEWQXb3BtZH_i52d4lymb9zwdMyAPO-5ZCI4zGyWvDfUNiTkrULTIVFBFWSuSU_uwzdxqhfKmvLEJOKi30SwuEbpjfBAmaenfq9HkpaGa6jYakw1r0o4_IilKip5w_a5KE-EZrepXLdSARrVhqeVKlEGTJrXcLeFYBQdcpjXqnlZrtDkG_jLaDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghqxUnobUIOqHxpImE6dXBDu4dyk2ZgEsB6O4_GezwuZAWYjHiEQo_CqJJ6h6ocQ9i0bEoj9qV4nyn85EFM56xGhtNgA72Uh5jJU6ichvdCGHWkGYLgiAKLez0-NjHjVBH6UPIWWCmlekrBaC_etD5AHm8WVDkl-RkEWQXb3BtZH_i52d4lymb9zwdMyAPO-5ZCI4zGyWvDfUNiTkrULTIVFBFWSuSU_uwzdxqhfKmvLEJOKi30SwuEbpjfBAmaenfq9HkpaGa6jYakw1r0o4_IilKip5w_a5KE-EZrepXLdSARrVhqeVKlEGTJrXcLeFYBQdcpjXqnlZrtDkG_jLaDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان اجنه و فرشتگان:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66799" target="_blank">📅 10:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66798">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/638875c442.mp4?token=GAbs1jrh495sgSNcCy0nc7qxiZjfcdr2UQHMPo22ptNYbzY0IdAmgLVcGyFkV2_MYdrC_fC0FvAb73iR5dXutYCCJIWUD-v5LEf8VvaRD88oPFJj0jZ5gDYBjveOyYtF5figIS7OWWckRErUy6JyrWnQt8HZNrKxuCAhCJmhSOeZaoysvFRW-OEm7CR_z7peR3AfOYhfRyODNMn1d6tc7ejMIxsWwvrzsWCpBsqSNeTyM9yxKEfxlXXC5ka9wQziA5LcO6Z93zWm8rUkEG4gAmuVK3HVWjJZZCFAi-FMhIYXYB3cY-kWNVCbCAsLMzS1ec0imv2avSjsxYSG4YduWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/638875c442.mp4?token=GAbs1jrh495sgSNcCy0nc7qxiZjfcdr2UQHMPo22ptNYbzY0IdAmgLVcGyFkV2_MYdrC_fC0FvAb73iR5dXutYCCJIWUD-v5LEf8VvaRD88oPFJj0jZ5gDYBjveOyYtF5figIS7OWWckRErUy6JyrWnQt8HZNrKxuCAhCJmhSOeZaoysvFRW-OEm7CR_z7peR3AfOYhfRyODNMn1d6tc7ejMIxsWwvrzsWCpBsqSNeTyM9yxKEfxlXXC5ka9wQziA5LcO6Z93zWm8rUkEG4gAmuVK3HVWjJZZCFAi-FMhIYXYB3cY-kWNVCbCAsLMzS1ec0imv2avSjsxYSG4YduWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه سریزد  ، یزد
شاهکاری از معماری باستان
جایی که قرن ها پیش مردم اشیاء ارزشمند خود را در اتاقک‌های امن آن نگهداری می‌کردند
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66798" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66797">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzWPMO4z5zUPJoEGMbxvWF0mFKvyn27k-WI5nrdWNJUbqxXqkD5MlYNjQrkkmNtSo7KS5w6uFAI-a-G5SO5acpFrox0qMvUTWyiJPJLfA5wYpEYMRpuHFJKTV2YBGSIfh1nGmdxr3ZvZdvrnGMtgNKfzExtKpAUyO9E7FmOCMlRwuATGvCTRCeLeH8jpqrx8jL2UZ4UYrCgRhVewFR31MSTglSCXlwFApV0ybjxklwYzSB38n7njrO9WbSKVOG9fVZrbf0x0qqbR0XBObscivO48OxyKIu1S_4Iriw7SUVr9TGZuR1z59fk-uClmtC6LJSs-ozW0b01fZK8POGRGIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
دونالد ترامپ:
دو زلزله بزرگ که اخیراً ونزوئلا را لرزاندند، بسیار عظیم بودند و تعداد زیادی قربانی برجای گذاشتند. ایالات متحده آمریکا آماده ارائه کمک است!
16;من دستور داده‌ام که تمام دستگاه‌های دولتی ما برای اقدام سریع آماده باشند. ما برای حمایت از دوستان جدید و فوق‌العاده‌مان حاضر خواهیم بود. گزارش‌های اولیه امیدوارکننده نیستند!
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66797" target="_blank">📅 09:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66796">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
از ناوشکن هسته‌ای کره شمالی رونمایی شد
🔴
رسانه‌های دولتی کره شمالی گزارش دادند کیم جونگ اون اعلام کرده است نیروی دریایی این کشور به سلاح هسته‌ای مجهز می‌شود و کشتی چوئه هیون رسماً وارد خدمت شده است.
🔴
این ناوشکن ۵۰۰۰ تنی به سلاح‌های ضد هوایی و ضد کشتی مجهز است و قابلیت حمل موشک‌های کروز و بالستیک با توان حمل کلاهک هسته‌ای را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66796" target="_blank">📅 09:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66795">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66795" target="_blank">📅 03:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66794">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66794" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66793">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cP8QTPBkAOV7uv1RD9lk0NyMViy5tht6T0R5aAm-H-96PuLqgqyhrmglE3L7xVyNpsSzGVG-lUDkoxDfNZ6Ma5PyD7WDTfwzQ5AjICqVgjw3WvZZXI7bbzTR_5HhcGf3USFNsdV838Fi_VtdK3Q7XfQ_LHoe-ihdLxZHrbuWlA6CN-zarFcDE3qJJzHU-SwZmrQd3Yy3gQ6U_G7CxDazq9oeb_LRXvvYwy903IRS_BHZsMPZXYVqJgZUfE_WCiw3h8134fIaOhI2YoqAokqIdt0C6d-4-fxeYEST2hMB7oSwwtKD10FMVojzlZM8Um2WW9d6mxYiKk03IWT9-YGReQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66793" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66792">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=jAPFNyyTsziK_cFLYL716l4gYm3wSSD-pUfnKhwtyESisDAxSSRRimJzbeJ1oLIK45jjaz-JpPO-s7W-9-KkhTU3wFt7vLXBpsyr9cInGQrqsRtv8xuC0YJkvQtV5RrKahvy9NQH2o2oby1qBkXzI-LPr8ZkpbjwYRGH-Np3EImHivXq-HdobA_9kpJFw3vMwyn_1qYw557OSDErLeYlg24MeWdT1sj-ATkDEhgY0GNTPzSlc6Yjnbr2vUe7m0roAniPGH1R1BAE09Nj2-2uR0vFR45OpzTKnwv0yyTx_5M_R7pQgeZKLopOOXEhL5bYE-Z0ZPSCu57mdSMHjcHjsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=jAPFNyyTsziK_cFLYL716l4gYm3wSSD-pUfnKhwtyESisDAxSSRRimJzbeJ1oLIK45jjaz-JpPO-s7W-9-KkhTU3wFt7vLXBpsyr9cInGQrqsRtv8xuC0YJkvQtV5RrKahvy9NQH2o2oby1qBkXzI-LPr8ZkpbjwYRGH-Np3EImHivXq-HdobA_9kpJFw3vMwyn_1qYw557OSDErLeYlg24MeWdT1sj-ATkDEhgY0GNTPzSlc6Yjnbr2vUe7m0roAniPGH1R1BAE09Nj2-2uR0vFR45OpzTKnwv0yyTx_5M_R7pQgeZKLopOOXEhL5bYE-Z0ZPSCu57mdSMHjcHjsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
درست در میانه یکی از مهم‌ترین مسائل، ناگهان خبر فوری منتشر می‌شود: “سنا رأی داده است که می‌خواهد ترامپ جنگ را متوقف کند.”
ایران این را می‌بیند و می‌گوید: این دیگر چیست
؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66792" target="_blank">📅 01:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66791">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=MF1czl__MAfyooS71zEVHCQ2ksTrfmro7e7CT0edBPQLN1fXyM97GRPumMR3mZ5j-o7Z1KelVCqmeGtsC6bEv7sYu_aosB7tJFhtMOgrrXnSoCXmZ79tRAblUDdX659fODE4x9pYu48LBdlHL5XYU7d_6XCMK5aYrAuHBJS1XJGFOWVIx3naOLAQsoFFmyxUih9z6CiVAbMhetA4jueFDU-9jUbSC-lCR9hs0s4NkEFOUOfpP_-9aAnqKTgfiwXLu1GvIQ_kM8EAwG2brf_SH0lbpTOFf4l8WhWHq2v1_hGyoNZ5xlkXJVzY1lTJeUUOBvtMiX8rrpHb52DTZ8cIzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=MF1czl__MAfyooS71zEVHCQ2ksTrfmro7e7CT0edBPQLN1fXyM97GRPumMR3mZ5j-o7Z1KelVCqmeGtsC6bEv7sYu_aosB7tJFhtMOgrrXnSoCXmZ79tRAblUDdX659fODE4x9pYu48LBdlHL5XYU7d_6XCMK5aYrAuHBJS1XJGFOWVIx3naOLAQsoFFmyxUih9z6CiVAbMhetA4jueFDU-9jUbSC-lCR9hs0s4NkEFOUOfpP_-9aAnqKTgfiwXLu1GvIQ_kM8EAwG2brf_SH0lbpTOFf4l8WhWHq2v1_hGyoNZ5xlkXJVzY1lTJeUUOBvtMiX8rrpHb52DTZ8cIzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره حمله به مدرسه میناب:
«نمی‌دانم که آیا آن‌ها هرگز خواهند توانست این مسئله را حل کنند یا نه.
موشک‌ها از هر طرف در حال پرواز بودند.
کسی گفت که آن موشک متعلق به ما بوده است. شاید بوده باشد، اما من هیچ چیزی ندیده‌ام که مرا به این باور برساند که واقعاً موشک ما بوده است.
موشک‌های فراوان دیگری هم توسط افراد و طرف‌های دیگر شلیک شده بودند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66791" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66790">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66790" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66789">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=ZcOXGLjfztHCY5e3U4YyAspD-YruYO5R78yGwgZxdiWkrSdTiS65sTlLvNlzGWwtCosF4u4XWnYtnLtkgavE4MHt8d569zBo7VcwV7uebF8c8D3wqVT7MbkgSBXKgMEd5OMocKddxalHxZhrF25pZNF3Rkh-ZzL4Rii0YWGhRQ7gvzdYdkWWj3KiNht6e-X-PAnEBLE_T5ejl3GCpBHzrVkH36dsKRG_4lUEd39agwkKSPP4mYJWgnDq4M58Gqk8FwsuIZWiiDXz92rf0jcZBgMxEJzLK4v1hq3OhCWodI_LnQ3rU75jzsO0PqhmykBAtLVuvH1lilS0scvvmTEXzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=ZcOXGLjfztHCY5e3U4YyAspD-YruYO5R78yGwgZxdiWkrSdTiS65sTlLvNlzGWwtCosF4u4XWnYtnLtkgavE4MHt8d569zBo7VcwV7uebF8c8D3wqVT7MbkgSBXKgMEd5OMocKddxalHxZhrF25pZNF3Rkh-ZzL4Rii0YWGhRQ7gvzdYdkWWj3KiNht6e-X-PAnEBLE_T5ejl3GCpBHzrVkH36dsKRG_4lUEd39agwkKSPP4mYJWgnDq4M58Gqk8FwsuIZWiiDXz92rf0jcZBgMxEJzLK4v1hq3OhCWodI_LnQ3rU75jzsO0PqhmykBAtLVuvH1lilS0scvvmTEXzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم نروژ فقط یک طرح ساده نیست
🇳🇴
...
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66789" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66788">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=PXOewzmn5LugdDLSSRpmREWKoMGwlxuzZjMHZBtcjc83QK7LkMcfuauiQT0WAodeJIoI1huwbt7RF_5yu8Hu9gP2RQkhNgKtwgFR3ojLCMYAjGkcpaOuJwpfOk-Fpl8E6-L0OzzShrziuut4_V0hf6YlzfV9ipMY7TmPiYj5dhS1SbQ-b4A_91uIwzIzypkuNHl61bLd5kleB0bQt5UAGmHA2SoN5q0cIq4Lg1HostxVl-xyHFjpl9SWDO4bK_ptRBTPVC5wGp_gOkePVvYGLN-rb3zVoR0kRXJajIfF4nSolFSaVPcHLTg0Yy_aB-tkpTWu7ERQCwtkRPY9jIOBl1qwc8O0weBY6DOah90gpUteSiyAyslefXt_eXFBPADyoCwFAjS_GevGuJ2xIFQr6dZSgkf3cz-osk9sx59eE2Bz980-d6AIZj_gQtdHHPgQnp1xd_9LA0EvK30o4o54AicEmPS-EOUcvFcrlx_ogtar4QOMTUD9ff8MqtxYYOgw_dR4z8_9KGqlaAf7H3SRp8ldb2G-wkNnzoLG1kJwk-EQ88dCVdi2zi30-TJuLF5LU1D3JVy6MjSzFSFML0QELkFxJzuM0dC8tlMVahlhtr9PFzeeKmmHMjjQ7DXqRmJHnEtAmpZgjtOhYBaXlln5bhvp1PFzwA7JT9GnVZawN1E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=PXOewzmn5LugdDLSSRpmREWKoMGwlxuzZjMHZBtcjc83QK7LkMcfuauiQT0WAodeJIoI1huwbt7RF_5yu8Hu9gP2RQkhNgKtwgFR3ojLCMYAjGkcpaOuJwpfOk-Fpl8E6-L0OzzShrziuut4_V0hf6YlzfV9ipMY7TmPiYj5dhS1SbQ-b4A_91uIwzIzypkuNHl61bLd5kleB0bQt5UAGmHA2SoN5q0cIq4Lg1HostxVl-xyHFjpl9SWDO4bK_ptRBTPVC5wGp_gOkePVvYGLN-rb3zVoR0kRXJajIfF4nSolFSaVPcHLTg0Yy_aB-tkpTWu7ERQCwtkRPY9jIOBl1qwc8O0weBY6DOah90gpUteSiyAyslefXt_eXFBPADyoCwFAjS_GevGuJ2xIFQr6dZSgkf3cz-osk9sx59eE2Bz980-d6AIZj_gQtdHHPgQnp1xd_9LA0EvK30o4o54AicEmPS-EOUcvFcrlx_ogtar4QOMTUD9ff8MqtxYYOgw_dR4z8_9KGqlaAf7H3SRp8ldb2G-wkNnzoLG1kJwk-EQ88dCVdi2zi30-TJuLF5LU1D3JVy6MjSzFSFML0QELkFxJzuM0dC8tlMVahlhtr9PFzeeKmmHMjjQ7DXqRmJHnEtAmpZgjtOhYBaXlln5bhvp1PFzwA7JT9GnVZawN1E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی که یه عده از طرفداران حکومت با هوش مصنوعی از «مختارنامه» جدید درست کردن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66788" target="_blank">📅 23:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66787">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKkDNkpzzoY0vf7qhl5bzhuor5X_AOeDSzpeRT0YmKbc8FHjY9ihVzTYj3QaWRYA8lCIJ2Y3MDJuBWP0QUjrwf9nleyrjZO36Q7kwf6TqnxzFyk2X5huDJkqyH-Bk3JU_z2fDvj4TdGspqPJ9WQP10KZ-GqaQp8eQu-lvw7wATo09tmY1gZ1zugI_K_LP8p4QVh2tk4Ub8Y3MHbMIFNBpvp7oCW7XxdvJQRGmeA_Vv6ueU3JmaCp0taDuaZA9q8agn7rC_ez7NPRtbyZFfMiHTJJ1RBma5w_aYXeudVsqe-TNLuV9Nia2BnERow8SjeZz-QERqhQ-ckuJYh2xWQ_Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی وزارت امور خارجه:
اظهارات متناقض آمریکا درباره یادداشت تفاهم برای پایان جنگ به کاهش بی‌اعتمادی ایرانیان کمک نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66787" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66786">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66786" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66785">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EC-u-W7jApdCmzuBaIoJ1G8i50Hew2GxURf8OfC9kY55wSktg_2C3KXd8V30qkLpLJrbWTYi5-A5jvopt1z7QXeL5bG3iuOp08MarWJiq6kfHO5DXR3_u6ao4zXudJUbPVoyUI6L3HhrvZYvIEJyA1k0r-trhrLoGp0yhhYopTeFj2sJIbJO4qWE18b1PL7ZxWEGqfMS230CAbjniDON38p3giK-OahQwAfae1YdKy7QT3Of68oxYrKiFPVaV7ld1aDBY1NtYTzhCHHZvp1YfFVXEhFSVDiKdlVbd4Hu3bRiLG--e3HmVJtEHo6AzS_MppiSNVeDE1mTWy802FUyrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66785" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66783">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f56950043.mp4?token=Hu5TBuv_jTMno_K7qeJBTaRmfZWM2wBihjoVu6pDtgLE5X9reHZV51O-GmERMmVnMY4xwxW9WOnXaDJTu_JWXupuZrKPmkKGLeK0qSNTe9zNsd1crDBiXpY99pJb2WmgCa7Lr9nJl7TsLhCWToP7C632Mr8leBDoQnTfrNpS3fVP9YE7YvI45Nl_Ul4_khND1qaAhNtikBgwkSCD_4VU80UCPgXl1Na5cwwPYCqb5jIPcj3I1jKIf7_Bw9UPNFSxznAJuFCjNRQAgpRc4Z_Zwc7B8BjisnGqEg3v_YMjr-k6bU81DFIgjSBy039pfstesqOP3Jkl3NTp97b2yO6dCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f56950043.mp4?token=Hu5TBuv_jTMno_K7qeJBTaRmfZWM2wBihjoVu6pDtgLE5X9reHZV51O-GmERMmVnMY4xwxW9WOnXaDJTu_JWXupuZrKPmkKGLeK0qSNTe9zNsd1crDBiXpY99pJb2WmgCa7Lr9nJl7TsLhCWToP7C632Mr8leBDoQnTfrNpS3fVP9YE7YvI45Nl_Ul4_khND1qaAhNtikBgwkSCD_4VU80UCPgXl1Na5cwwPYCqb5jIPcj3I1jKIf7_Bw9UPNFSxznAJuFCjNRQAgpRc4Z_Zwc7B8BjisnGqEg3v_YMjr-k6bU81DFIgjSBy039pfstesqOP3Jkl3NTp97b2yO6dCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ازای شهادت مقام معظم رهبری چی از آمریکا گرفتید؟
قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66783" target="_blank">📅 23:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66782">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=ntpo49eKJpZUiw7StUYmnD83dbXNh67tUfBTfRQJQfckOsjFq4PrCGd5GnImk7w9saOI4N1dqnjsWUCRZ7BwMT_XC9mt76E02S_0yLq_4gUdLvnApm9ZtmM46gHOH129HCFUM5GHvR0gE7q9vpQw2qcPR389Bdwfh5hUw0gc5vhbrfRzI8gLKC031G7zI2lpitpcFFVSFKUZsO52aira1gX9pulryydqn6EIxZLHX5yByDi12u6M5CUIVTgddqE0mjRhjNoDE35kPni1NhcNx-RWYbbGi06gP8gnm5gChOdpedMw3h6V6v-u-G_sR1FvUwbAcSOXZ2sv3GlI8SY4uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=ntpo49eKJpZUiw7StUYmnD83dbXNh67tUfBTfRQJQfckOsjFq4PrCGd5GnImk7w9saOI4N1dqnjsWUCRZ7BwMT_XC9mt76E02S_0yLq_4gUdLvnApm9ZtmM46gHOH129HCFUM5GHvR0gE7q9vpQw2qcPR389Bdwfh5hUw0gc5vhbrfRzI8gLKC031G7zI2lpitpcFFVSFKUZsO52aira1gX9pulryydqn6EIxZLHX5yByDi12u6M5CUIVTgddqE0mjRhjNoDE35kPni1NhcNx-RWYbbGi06gP8gnm5gChOdpedMw3h6V6v-u-G_sR1FvUwbAcSOXZ2sv3GlI8SY4uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ایران خیلی خوب رفتار می‌کند. آنها با هر چیزی که من می‌خواهم موافقت می‌کنند و باید هم موافقت کنند.
در غیر این صورت، ما فقط برمی‌گردیم و کاری را که باید انجام دهیم، انجام می‌دهیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66782" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66781">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=O1jEzpQMwF2WNJpEcuIsF7ICqcLxg4nZTq9JJvES9TaANWaS3UL1RVN9bbLabw2Yej8RXKoPg6ibQPrDQio4QlY2KDsjPjInrlm7CEouT-Hf2j2nwOkrehJ6nWNycyw3QEp4oXkETugqTpp3zfib6I5pkSyi7X1Ireu5g8M77AHpEEqxZgG0tW6TSAWsF0MO3XisjwX4xAo47s7t3A4iVSm8rsSoW_8BZ8nu5RDzGRqQXy90rBlPT1TPNO0vxwsi1-Ac5CE459miTAtSGFbwOx1MA-u_pefTxD3RHOr6hQN5aq5Yty1Hgz25X-Nw7jqxZSMNk9PDCOBUTwwuHmx9Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=O1jEzpQMwF2WNJpEcuIsF7ICqcLxg4nZTq9JJvES9TaANWaS3UL1RVN9bbLabw2Yej8RXKoPg6ibQPrDQio4QlY2KDsjPjInrlm7CEouT-Hf2j2nwOkrehJ6nWNycyw3QEp4oXkETugqTpp3zfib6I5pkSyi7X1Ireu5g8M77AHpEEqxZgG0tW6TSAWsF0MO3XisjwX4xAo47s7t3A4iVSm8rsSoW_8BZ8nu5RDzGRqQXy90rBlPT1TPNO0vxwsi1-Ac5CE459miTAtSGFbwOx1MA-u_pefTxD3RHOr6hQN5aq5Yty1Hgz25X-Nw7jqxZSMNk9PDCOBUTwwuHmx9Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«جنگ خیلی خوب پیش می‌رود. همانطور که
می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم. ایران امتیازات بسیار بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد، اما بسیار، بسیار، بسیار قدرتمند بوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66781" target="_blank">📅 22:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66780">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=i0KK7pQEaFgWvI7F118X3UJ1XKPvuC0ykBH-Y0CDotrQgcM_ra0I4j3k1NcKpNFUwAUM1OoCZxfXf2IMtlTfJ3LaznX7zfF_lPkeLlRcI-iCEP4HmhyhsDdB1rTwCflz_0-LDvx7EBus6bZoZAct0MgMU8ZgPzOVNtpki3NcUt8G_uIsgJHh7llLMzBlvM-OmPeEQkfpOThYk53pCR6viEQiDsmjbuEDLlcdigU9vgs1sTVoDeqWlJVNikMwaoEc4TWDPQCQNKATOsozYc3mLNsoIgxhS8CgyHIK9sP6nAAzMyQCpnYssh8hprUv9wMlwSZNXbpyFO1CREjOMWegHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=i0KK7pQEaFgWvI7F118X3UJ1XKPvuC0ykBH-Y0CDotrQgcM_ra0I4j3k1NcKpNFUwAUM1OoCZxfXf2IMtlTfJ3LaznX7zfF_lPkeLlRcI-iCEP4HmhyhsDdB1rTwCflz_0-LDvx7EBus6bZoZAct0MgMU8ZgPzOVNtpki3NcUt8G_uIsgJHh7llLMzBlvM-OmPeEQkfpOThYk53pCR6viEQiDsmjbuEDLlcdigU9vgs1sTVoDeqWlJVNikMwaoEc4TWDPQCQNKATOsozYc3mLNsoIgxhS8CgyHIK9sP6nAAzMyQCpnYssh8hprUv9wMlwSZNXbpyFO1CREjOMWegHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالناصر همتی:
اگه کیفیت ذرت و گندم آمریکا خوب باشه ازشون میخریم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66780" target="_blank">📅 22:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66779">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD7xFD0iCwx5dTp_SqJMk_U8jb3Vrh_XhZFrt5F11GbbvAvuVHrM248eBeWeu-koo1edqJoKAeijRrQyha7cEUZjo2cz91iOynADWYJti7DGHjZZLnZGArK5ZbwKy0lQeqYhpG8rVeadaXddN43CwEXlG3y6q4nNLuR8ugzJAKBQiRkZH7OfxFi4BUHDpiZ_mP9hupgXPMqRCjkXDJkpjLXMqjyenrNlLqYtJnZqP3Gnhuoj55Y2NYEkh9bjLEuVVEun85suA5BmuTymEZfK2s1aj-QwowhRAvic7lOppJFSPjmgsjFTWIcc6wHqTUDlxlicbEg_G6ZRkRRpgQ_IfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل به مارکو روبیو:
رژیم جمهوری اسلامی و حامیانش در عمان در تنگه هرمز هزینه دریافت میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66779" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66778">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=tutrEL1Q7xuKAxjtt0XP0qECbSBL0eb7cprmdgO32LJhd570Whc6rQmE5_wKB_JyNJIm6SKaVNY-S9ypawxAji_CPTeeuEHiv_vDRlmd3YOxY6nUxkQR6BjpBXgwkX97Z8Mdiak6AFQ0aCYoCRrwKmFQbrlQiUMf1pEvwEle8G3v0TVak36BzzNBq6BmEBgdU5XvLu_fPmwmtMPYfZNtn5JfNPm7ZYeVh-p5_ARvRAR2_6g8oSMqdv6LCkKDKTr7maRwLI1cEOsnRgZi-hCTMrZmXz9fgFqlgUHG4X8FxrRH7XYXhfiHYavbbGVhWdV25C64Uo_NwBkEeZt1MjgzSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=tutrEL1Q7xuKAxjtt0XP0qECbSBL0eb7cprmdgO32LJhd570Whc6rQmE5_wKB_JyNJIm6SKaVNY-S9ypawxAji_CPTeeuEHiv_vDRlmd3YOxY6nUxkQR6BjpBXgwkX97Z8Mdiak6AFQ0aCYoCRrwKmFQbrlQiUMf1pEvwEle8G3v0TVak36BzzNBq6BmEBgdU5XvLu_fPmwmtMPYfZNtn5JfNPm7ZYeVh-p5_ARvRAR2_6g8oSMqdv6LCkKDKTr7maRwLI1cEOsnRgZi-hCTMrZmXz9fgFqlgUHG4X8FxrRH7XYXhfiHYavbbGVhWdV25C64Uo_NwBkEeZt1MjgzSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
توافقات اخیر با رژیم جمهوری اسلامی بخشی از یک روند مذاکره‌ای و یک اقدام موقت ۶۰ روزه است.واشینگتن انتظار دارد تهران به تعهداتی که در سوئیس پذیرفته پایبند بماند و در غیر این صورت، پرزیدنت ترامپ ابزارها و گزینه‌های مختلفی از جمله بازگرداندن تحریم‌ها را در اختیار خواهد داشت.این تعهدات به صورت روشن و صریح مطرح شده‌اند و ادامه مسیر مذاکرات به میزان پایبندی رژیم جمهوری اسلامی به آن‌ها بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66778" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66777">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=YZmsILzNq5qHZiUJTnz-dBrJU_mJBKqDIPV7FPYX8c1nL7bF5SlRkOCHZgeC6c3UNMorTZTgJqZ3Qgz63x3tX2cLXWCEi9w2Xt4Jq2hXmQHxuAx-mdz98xZFN9dkbFJM31RScIynjcO1idUjfRXWkAxmnsyB0_YSME-z05cTk0xRMehWRSVwiJ7SyzUEMXIDkiUNnlRjpyHi2Jka5wwiW2HI4E9r_rnopdW0SUGn3aHJe-cXFsRgt3SCKL6861xZM-0uSLATlIGkdsy9ZhSLxfuX3SwQt928UvgCTKicCe2PNs9jv-lJFNE9Lm036GvOSeB7dA9w70j5yjTstKNoCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=YZmsILzNq5qHZiUJTnz-dBrJU_mJBKqDIPV7FPYX8c1nL7bF5SlRkOCHZgeC6c3UNMorTZTgJqZ3Qgz63x3tX2cLXWCEi9w2Xt4Jq2hXmQHxuAx-mdz98xZFN9dkbFJM31RScIynjcO1idUjfRXWkAxmnsyB0_YSME-z05cTk0xRMehWRSVwiJ7SyzUEMXIDkiUNnlRjpyHi2Jka5wwiW2HI4E9r_rnopdW0SUGn3aHJe-cXFsRgt3SCKL6861xZM-0uSLATlIGkdsy9ZhSLxfuX3SwQt928UvgCTKicCe2PNs9jv-lJFNE9Lm036GvOSeB7dA9w70j5yjTstKNoCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: برخی از عناصر اطلاعاتی ایالات متحده ارزیابی کرده‌اند که اسرائیل علاقه‌مند به تضعیف تفاهم‌نامه فعلی است.
🔴
روبیو: نمی‌دانم در مورد چه اطلاعاتی صحبت می‌کنید. نمی‌دانم این اطلاعات را از کجا می‌آورید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66777" target="_blank">📅 20:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66776">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=WL-MDHPTJGRmxX2Z-Jh9UFMSAOR3itgyArPAky8o82g29_5SaqoZNjFFxmda09eRBiOJyHkt1GSTDgn9oknHfH8dMNAW0Cm9cLFUtaB44lwzB9FL5B0k5AxrKgt5AeZcuk67gHczUcmBySp0jWl6Z4UYVs1jSroyyJS_napbDnMz0VU2bIG5G0pI7BT9FVU9t8c5cz-6P9p0Nr3-e-wXSBgq13vAQSHge5FyAoO-PCxWxqYcI2_uQ3oIZrEa0Jp36Ep23cXbwA738J3Caj8NdLiP5WR1oNORb5f97SC796SyBNc6VN-ilfzpYxj2snzzBnT0cDsBtFlqGO8vgaW_HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=WL-MDHPTJGRmxX2Z-Jh9UFMSAOR3itgyArPAky8o82g29_5SaqoZNjFFxmda09eRBiOJyHkt1GSTDgn9oknHfH8dMNAW0Cm9cLFUtaB44lwzB9FL5B0k5AxrKgt5AeZcuk67gHczUcmBySp0jWl6Z4UYVs1jSroyyJS_napbDnMz0VU2bIG5G0pI7BT9FVU9t8c5cz-6P9p0Nr3-e-wXSBgq13vAQSHge5FyAoO-PCxWxqYcI2_uQ3oIZrEa0Jp36Ep23cXbwA738J3Caj8NdLiP5WR1oNORb5f97SC796SyBNc6VN-ilfzpYxj2snzzBnT0cDsBtFlqGO8vgaW_HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
وقتی می‌گوییم تنگه‌ها را باز کنید، منظورمان این است که تنگه‌ها را آزاد باز کنید. آنها آبراه‌های بین‌المللی هستند.
هیچ کشوری روی کره زمین از گرفتن عوارض در تنگه‌ها حمایت نمی‌کند. این اتفاق نخواهد افتاد. ترامپ این را به روشنی بیان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66776" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66775">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=QQkXR30BHadQrpcvxaHzJeLpgJWQzzNTacU-SyccWQLoYmEp2JjDTcN_0geOH4iLxcn_J3-X-PA9zU76ve_rR9Hw4LpkS4S2IWBFAM_XM_K9bNpun1ygpDhKR7Q7IfcC8ZtMLkrGX_tAvVZ7nossyQh7UeqNOXCk9tvq-j1wJlcXASsnm3rlLEiQlFhws_uDMSuE9_K2bpoRYk-sl25fUkiDhmvccVXkTqwTukdx-Xh-gIeG5MILcWDd1iSbRlze_7hbEE7ZIPR_m7sHzA5oOGRoGRVpzDsWR3mYmC7WBo6Ne4CjXWi3w44xV_1egcTo9Zl8olo4beJJHb0B3_PMYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=QQkXR30BHadQrpcvxaHzJeLpgJWQzzNTacU-SyccWQLoYmEp2JjDTcN_0geOH4iLxcn_J3-X-PA9zU76ve_rR9Hw4LpkS4S2IWBFAM_XM_K9bNpun1ygpDhKR7Q7IfcC8ZtMLkrGX_tAvVZ7nossyQh7UeqNOXCk9tvq-j1wJlcXASsnm3rlLEiQlFhws_uDMSuE9_K2bpoRYk-sl25fUkiDhmvccVXkTqwTukdx-Xh-gIeG5MILcWDd1iSbRlze_7hbEE7ZIPR_m7sHzA5oOGRoGRVpzDsWR3mYmC7WBo6Ne4CjXWi3w44xV_1egcTo9Zl8olo4beJJHb0B3_PMYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
به من گفتند: «وارد رفح نشو.»
می‌دانید چرا این را گفتند؟
چون رئیس‌جمهور ایالات متحده گفته بود ارسال سلاح را متوقف خواهد کرد.
من گفتم: «احترام زیادی برای او قائلم. او در آغاز جنگ کنار ما ایستاد. اما ما چاره‌ای نداریم. وارد رفح خواهیم شد. و اگر لازم باشد، حتی با ناخن‌هایمان هم خواهیم جنگید.»
گاهی باید بدانی چگونه حتی به رئیس‌جمهور ایالات متحده هم «نه» بگویی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66775" target="_blank">📅 19:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66774">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=amTDZxY1G8OpWCZZ0DUT30L1Rcj0y9a4kxeRi4moT5H7W3bz-NJKG7DH_mMXJwnd99sWiJngKr7KxLSydAcvErd1EyozBZXVCniZ8nFcYGY4orK6Ecr49SPAWJyFeKaupVLco6F3VyelJCE6JuEVJVDeqb6LQwajOc_i4fq8SijojYVW_sQ1rBeLze8EOcriBmwdVsSz5zLal7Z5nWtzM0-w_RCClwAD6Q46AuKzwh1LWqzJKHgRtpRHo20jn9X-XgGt9Vvv5vhdeB8zcDX2u_18u_iU_ExI53T4KurW4Dk6wtD72OiQhWLy-L4_P67q8biBLyAABTg_7PveCZ33gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=amTDZxY1G8OpWCZZ0DUT30L1Rcj0y9a4kxeRi4moT5H7W3bz-NJKG7DH_mMXJwnd99sWiJngKr7KxLSydAcvErd1EyozBZXVCniZ8nFcYGY4orK6Ecr49SPAWJyFeKaupVLco6F3VyelJCE6JuEVJVDeqb6LQwajOc_i4fq8SijojYVW_sQ1rBeLze8EOcriBmwdVsSz5zLal7Z5nWtzM0-w_RCClwAD6Q46AuKzwh1LWqzJKHgRtpRHo20jn9X-XgGt9Vvv5vhdeB8zcDX2u_18u_iU_ExI53T4KurW4Dk6wtD72OiQhWLy-L4_P67q8biBLyAABTg_7PveCZ33gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
در عملیات غرش شیران بود که من به ترامپ حمله در ایران را اطلاع دادم و هیچ اجازه  گرفتنی در کار نبود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66774" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66773">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=OkWS9sFX_O_XWHokf8BLI3TYv05eRg200zzYmySnmnserm0L65chVyeibozBl2CpQOryRBH3b0E87QUMf9PQeP_452culdf5afvo7mgjDTJ-7ir7GeHsXbB0zc-NiBXiAgC_ubez3s3T9usapDG8-iYMen26kVML-Aiq6j-ObxVNSUGCcRmvoEuw66a0_el6HN1AQ-gp9CFww4uZCp4XQdA4xaWWYQPZZ46MWE1mXk4Kkc6mCh6aTNGtVP8WA8SZZZkItAlz-YA1o0iO-WVbasXMWdPw1CQtYs6n1Tq-ilZovIur6VLyJTRiZEVSDPm-EuOPWrLf5asLd3giWeLUCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=OkWS9sFX_O_XWHokf8BLI3TYv05eRg200zzYmySnmnserm0L65chVyeibozBl2CpQOryRBH3b0E87QUMf9PQeP_452culdf5afvo7mgjDTJ-7ir7GeHsXbB0zc-NiBXiAgC_ubez3s3T9usapDG8-iYMen26kVML-Aiq6j-ObxVNSUGCcRmvoEuw66a0_el6HN1AQ-gp9CFww4uZCp4XQdA4xaWWYQPZZ46MWE1mXk4Kkc6mCh6aTNGtVP8WA8SZZZkItAlz-YA1o0iO-WVbasXMWdPw1CQtYs6n1Tq-ilZovIur6VLyJTRiZEVSDPm-EuOPWrLf5asLd3giWeLUCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66773" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66772">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66772" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66772" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66771">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=fy-UNusv5b8jSixJOtxkiTv9Wq2iRpVdp4N9cf9MTj8NUPUQqmtAC9MTCNBjcvZk9vJQj-wD8S0a6HmRBpqPKOJ8_udWaxnyMLeSkJh3afzfTtl8JAT4RtrPmhGthbDPt1IAV744dPfL_aJzLRpduif4BbnR1n330d1nDItZd7IoEHTaQG6t4bGiSl9GMMfZQFXZF49pbqN-4ehHzjw58-5CVvr0CJMNXWXzm8n5KtSjmVRE_xY9rna1_Gpn6G6E0eNjwGlkdsue4vdyUqkcOdJ3Wnvt0eabllEkvsfXfautxwp-Qc7N7UJSdwOPmF0RwMWRKRk799_DqhtT78MSqi6bmYClwXArweG4pJTpZugnVwJV7a3STV-vsNZK-h58x2PZsBWEijzis63C7qtprDjha5Lw7Al8RIn_qylsVH_MDWQ6RtGiKdniUenZyhQb2BPAphA5VTccidlUrqIOgIFcWaqPPehu37ldi55A7hoXK_1ADq4dYu-2GFARjlYXN9X64awIlskk2p1Pw_nUnwhPFEkLzNlMJMvT3dDHmgD39FNCDWIooPfJt4061PqJIyt_Uox_tDPqSsOAHv3WaLOPw336lA0IH-bj2m2_9WXvRddDpopU1uNniuDmyi2s5X83GQI5D2DwYaW6f9hfhr865Wf6aX-7Rg5d-mpGWYM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=fy-UNusv5b8jSixJOtxkiTv9Wq2iRpVdp4N9cf9MTj8NUPUQqmtAC9MTCNBjcvZk9vJQj-wD8S0a6HmRBpqPKOJ8_udWaxnyMLeSkJh3afzfTtl8JAT4RtrPmhGthbDPt1IAV744dPfL_aJzLRpduif4BbnR1n330d1nDItZd7IoEHTaQG6t4bGiSl9GMMfZQFXZF49pbqN-4ehHzjw58-5CVvr0CJMNXWXzm8n5KtSjmVRE_xY9rna1_Gpn6G6E0eNjwGlkdsue4vdyUqkcOdJ3Wnvt0eabllEkvsfXfautxwp-Qc7N7UJSdwOPmF0RwMWRKRk799_DqhtT78MSqi6bmYClwXArweG4pJTpZugnVwJV7a3STV-vsNZK-h58x2PZsBWEijzis63C7qtprDjha5Lw7Al8RIn_qylsVH_MDWQ6RtGiKdniUenZyhQb2BPAphA5VTccidlUrqIOgIFcWaqPPehu37ldi55A7hoXK_1ADq4dYu-2GFARjlYXN9X64awIlskk2p1Pw_nUnwhPFEkLzNlMJMvT3dDHmgD39FNCDWIooPfJt4061PqJIyt_Uox_tDPqSsOAHv3WaLOPw336lA0IH-bj2m2_9WXvRddDpopU1uNniuDmyi2s5X83GQI5D2DwYaW6f9hfhr865Wf6aX-7Rg5d-mpGWYM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66771" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66770">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwlflJmp5nHixyS-1MlszE4NAjUal7ylRVCf1nhFGwphV7lt5LwK-hBCMI4JCn-666AVkdU846hLcTxhky762Ehdm_UskBsnrzJisX-YHGvUKzYY3MVKgZF2m9aXJM_zpaq0HyPJTDk2iTUA8AT7JZCeUk-3Ka08uZJjd06TZ_KGgcM3rtTPMHRmusbVMVkZClJN-AGC4RH2va6dBAESt0VvE34GOiSJNSpiIbvasxIY1wyd10DIAPhUYNmQXMWg5hWym8iLsz-JeSTpEoaTA6BD8YDGXkb_1uWYecfdDdkARHIpoxHYMViD6o5VpQNRp96y9bIa36z6GNiAI23xJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
ایران به آمریکا اطلاع داده که، برخلاف گزارش‌های دردسرساز رسانه‌های فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای و هیچ نوع هزینه دیگری از هیچ کشتی‌ای که از تنگه هرمز عبور می‌کند، توسط ایران درخواست یا دریافت نمی‌شود. اگر این خبر نادرست باشد، مذاکرات فوراً پایان پیدا می‌کند!
همچنین، آمریکا هیچ پولی به ایران نداده و هیچ بخشی از پول‌های ایران را هم آزاد نکرده است. ما بخشی از پول‌های ایران را که کاملاً تحت کنترل خودمان است، برای حمایت از کشاورزان و دامداران آمریکایی آزاد خواهیم کرد تا با آن ذرت، گندم، سویا و محصولات دیگر خریداری شود. ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد را منحصراً از آمریکا برای آن‌ها خریداری خواهیم کرد.
از توجه شما به این موضوع متشکرم!
— دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66770" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
