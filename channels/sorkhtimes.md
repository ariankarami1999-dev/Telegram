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
<img src="https://cdn4.telesco.pe/file/CKawrJCraXn_laf-JfYxej7ahsO6Zv1A93hmySS74ymwtxOUp71WnmNJu3h0lAk4wMKQx_V7PKPX5K4OS2kKEfelm4_pbdflydq5rtNQErJRYSgBUSfbohVQGSoqcAUu7ii3C2o8d3nSov_3kPqKkEiW-LYFKOKp3KK_X17Ell_JwRWNTlcesOzWJ5JcjidxECZx7ci8wqO6CkCT5OZRO62kjTQ9fjkqdbxTg_elXWNQ9wBuv5jj3hHexVL8OqWGjDTIokb0rBP-8S07MnuMxCb3A9rFUB-OyrVqJjTaXyp3CKuhoVgx5lI1-2zIGJClDR3ShbwCx30FcPc4dsbo5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 14:35:32</div>
<hr>

<div class="tg-post" id="msg-135573">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2255e438bf.mp4?token=aV41ni80lF51M0TKXZv5yLMAqRgSR-I-nbJ4x2PEJQFme_JJXAL0ot419TuzUtO3bDsLCm1Fyf4Rkr9fkS_CWJkt-15KCtDcINNddvWW2KMxvIAc8gMPo0Ni_mM1SJBlIEC2G200x5F1PzN-Sf-gxZQUdJkAhCrTr32693FYuMiYvxe1bikKW5KycZvfxZIordm662z5q1BD61xcj3nLDuri1CWK3fe1oSCBOVlgJrS0SvrHRGU8Bz1WAxR84KAh2Zkmnphexz_lh4O8iW2XWEFBdjCDGZunSA0y91CFhLItmUuEenu_8eyLcsRC9JyWpdO-5SMA87FlOAFQJUZZpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2255e438bf.mp4?token=aV41ni80lF51M0TKXZv5yLMAqRgSR-I-nbJ4x2PEJQFme_JJXAL0ot419TuzUtO3bDsLCm1Fyf4Rkr9fkS_CWJkt-15KCtDcINNddvWW2KMxvIAc8gMPo0Ni_mM1SJBlIEC2G200x5F1PzN-Sf-gxZQUdJkAhCrTr32693FYuMiYvxe1bikKW5KycZvfxZIordm662z5q1BD61xcj3nLDuri1CWK3fe1oSCBOVlgJrS0SvrHRGU8Bz1WAxR84KAh2Zkmnphexz_lh4O8iW2XWEFBdjCDGZunSA0y91CFhLItmUuEenu_8eyLcsRC9JyWpdO-5SMA87FlOAFQJUZZpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مرصاد سیفی دفاع چپ شباب الاهلی:
❗️
پرسپولیسی هستم / قائمشهری ها اول طرفدار نساجی بعدا طرفدار پرسپولیس هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/135573" target="_blank">📅 12:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135572">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6644fa24f4.mp4?token=QBoEX9zHiIfrr9Hr1F7kEPIukGhrj6Gf8G5Xy__t5Vx6mUdLs14tphNxQzzfVKA4ryaUW3Z4iCdRnCzmbBloOIJxzh1kbWZMhCCjm5sfGpNUQcZxy67bhtaSxYPvm_WjV-2CA0zLOlvI43KVJPAmaET3U0DIDWyZz5GHYx0hK7AauDQseT0UTUv7c6py-QUjKhPLyBTidiDqdj3-tp-ac9_07TcphwyjkNjpHJkTCZsHmFKXaCFZmfN6SsprTWjOFjTNupWy8hAVJiDkO_m2fIu3Iy6Txcx2r8GfJlF_21SSeckIt6q5iUtuMQdHwBAZ8jzdxb5-3KrhfCT7_stMrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6644fa24f4.mp4?token=QBoEX9zHiIfrr9Hr1F7kEPIukGhrj6Gf8G5Xy__t5Vx6mUdLs14tphNxQzzfVKA4ryaUW3Z4iCdRnCzmbBloOIJxzh1kbWZMhCCjm5sfGpNUQcZxy67bhtaSxYPvm_WjV-2CA0zLOlvI43KVJPAmaET3U0DIDWyZz5GHYx0hK7AauDQseT0UTUv7c6py-QUjKhPLyBTidiDqdj3-tp-ac9_07TcphwyjkNjpHJkTCZsHmFKXaCFZmfN6SsprTWjOFjTNupWy8hAVJiDkO_m2fIu3Iy6Txcx2r8GfJlF_21SSeckIt6q5iUtuMQdHwBAZ8jzdxb5-3KrhfCT7_stMrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ادعای جنجالی فرهیختگان!
🔴
روزنامه فرهیختگان با انتشار این ویدیو مدعی شد یکی از بازیکنان یک تیم مطرح لیگ برتر در حاشیه تمرین، در حال تزریق ماده‌ای ممنوعه بوده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/135572" target="_blank">📅 12:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135571">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
❗️
مهدی ترابی در آستانه بازگشت به پرسپولیس / 360
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/135571" target="_blank">📅 11:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135570">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/135570" target="_blank">📅 11:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135569">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/135569" target="_blank">📅 11:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135568">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
رضا جباری به کادر مهدی تارتار اضافه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/135568" target="_blank">📅 11:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135567">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQ9NO6BfBXwnqmJogaiUtXZKZ7-9x_jBu4ZV35B7YQeIsf9p66fUriPKuy_6-c0xHTC4VLDAwkGZ5pD7TQ23ECvu_99o2o6BA-JHUm8e5uoABfS9uGCSTolDTMU5ZsOED5Y-IT5T9BjQfKN_WxlCFvyXNW9bAv-JuNoKo9luANivkdL11AX03JnVlbGUJZLzjweYoQZA3MGXN1YmY0P9rNHyPSNKYH0y8WkSyuvEf496xK-jahlk0KoB2gBMxluGOvP6Tr54bgtp0vHkD09BLdJo7jS0TThC7Qn0fqpdVJw9KedgJzny9nrNFCO0Cj0zHVe6L4vhpCxJY2COSaUcJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رضا جباری به کادر مهدی تارتار اضافه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/135567" target="_blank">📅 11:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135566">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
اگر پرسپولیس همزمان مهدی زارع و مسعود محبی را جذب کند، پرونده انتقال علی نعمتی به‌طور کامل بسته خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/135566" target="_blank">📅 11:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135565">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iodG5hsLQM6Kzd_x2dxLT5sp6sDDiF-gpqIMDuUEG3TNzf_CgkuXp1ji2KQQ4C3klFDkI92KG23R_upldlIEb_HPOOT0goczk7B4iOApMYhphbDpa6HcvWROW0SUohK_A9DUeA9z7pmq9_PY1ZMYo56O4rg98Haod8C-st3RZiz9RkZdUhUZYomTbgu84aK4fnOmPw3YQEuXOi_gSEOsPphqVj0BOhuUqozdV6XIpG8dLxYOGUS53Q4Majgj-GtLy_rZ_hkKDTyYIJMwsLrYrt3_IPSyR26jHprHlxk3BZWHdx-NU2flryx7vIg-SPixhQywz7iri2nP7kzItqAaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ترانسفر مارکت: رضا شکاری از پرسپولیس جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/135565" target="_blank">📅 09:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135564">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❗️
❗️
باشگاه امروز به شکل رسمی نامه زد تا پورعلی گنجی، عالیشاه و سرلک در این تمرین شرکت نکنند!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/135564" target="_blank">📅 09:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135563">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
محمدرضا احمدی مجری فوتبال برتر از صداوسیما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
🔴
🔴
او قرار است فردا شب بازی نروژ-انگلیس را در آپارات‌اسپرت گزارش کند تا برای همیشه تلویزیون را کنار بگذارد.
❗️
❗️
فردوسی‌پور، احمدی و محمدی مرام بهترین گزارشگرای فوتبالی…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/135563" target="_blank">📅 09:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135562">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVhZaAmN15YAZcN6dmivzYBU9nyItmqTiOOg-aHqMGwRUgB9_lmGV_ssDlPt2y85LRlRUS-ZvW07idfHMSD7t2QviBMQHn1EmyqRN4Nbn_NPao8VrOrEfoTNOr_3RGeEjdojuagihsXmuzTOri5o0eDElbVA8YDKx4LH44lf9rmuIv2GxPnJVbqz42QgkkbtIV9fU85kvvxmfxMxzrT9-0vTXVZfym3VBq6vFo_cuX9bRsbU68rGhXlFEm9xdfLupkNv8PguyNg_Yax0G9IJrLuKW0yeLI46UlKdByjNgW1dufUWE5a695J4SaUWGN6-KeTRHFKsfzNPcjzRBi08Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/135562" target="_blank">📅 09:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135561">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135561" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/135561" target="_blank">📅 02:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135560">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmEdJkmSppptPpYbzZuPTr_xkUXnfnkSiVhmYFQYnnnnh1LHIW-6EXLBJIMNa0hOlEHH-Acw3K9oakXoY9dnBDiVBzqiD9QZx6W1hZTIoOolizK-5mjUReGmJldv1hWFZXOV4dtzcsniLfLXggr33P-Uz4PfZhFUubhwhD29JQ_rmzNOO0EXn4n9ld9ZAPZT7R9_ljFM_py6W-B9paVt0pFvqu5uIl_MFylsrHk0HfQ_uATLqc3oxPl1_qgEtA7_6bHiqWrwFsfT4uKwJwHNyDlukvSngMpmaSgCkLO5NIxdc51weWOxkT1EdMWhsEYLceP5f60ODoGeV9Vye56RjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://t.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/135560" target="_blank">📅 02:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135559">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfZNQ548fas3E0Wmiu_Ik4DPU_cwsiTLuwpUSEBk20R9DYQHKie0nvP57wRCDrDgYNzVl01mMbwpYpNgdUzVO8D4Xe-4eg2cw-1h8Y_MQh7MSYQuOxTDBQR9oV-pHWqInDWhzgBXQ5oo_Ko6ZNdgrNgChuGEi3hupJ1ebjW7DhzR_8YE0s-_h1Avm8Xbo5fkKqgp3tqO9bCAZ8h9QFqboNTNLcknvt8koOrh20qi7LjvgPaWuDJMWlvOQpGSu0BbLJz-M5SKK9LskrLYRqpL3atX1YC-1vCYRSg6cZEhmor6PJV6jQwlLWX44miR_BZIslF6uHBO0bVBFNo9qvlzFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/135559" target="_blank">📅 01:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135558">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
دو بازی آخر یک چهارم امشب ساعت ۳۰ دقیقه بامداد و 4/30 بامداد انجام میشه ..چه فوتبالیه نروژ و انگلیس ساعت 12/30 شب امشب
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/135558" target="_blank">📅 01:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135557">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
باشگاه سپاهان که تمایل به جذب نعمتی داشت، طی روزهای اخیر مذاکراتی با این ملی‌پوش ایران انجام داد و به توافق نهایی دست یافت تا خط دفاعی‌اش را با جذب او تقویت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/135557" target="_blank">📅 00:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135556">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
فوری؛ شنیده ها: رضا شکاری از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/135556" target="_blank">📅 00:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135555">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
حدادی: هی میگن چرا از گلگهر بازیکن میخری؟ مگه تراکتور از ما بازیکن نخرید چنتا رفت قهرمان شد؟ گل گهر با سه امتیاز کمیته انضباطی نایب قهرمان لیگ برتر و جام سه جانبه هم در آستانه قهرمانی بود
😕
😕
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/135555" target="_blank">📅 00:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135554">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
🔴
مهدی رحمتی :از امیر قلعه‌نویی تعجب میکنم، اولین چیزی که او به من گفت، این بود که به هیچ‌کس هیچ قولی نده، اما خود او قول صعود داد.
🔴
🔴
اولین هدف آن ها صعود از گروه بود اما اتفاق نیوفتاد، پس بیایید عذرخواهی کنید، تاج و قلعه نویی باید حداقل از مردم عذرخواهی…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/135554" target="_blank">📅 00:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135553">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
دو بازی آخر یک چهارم امشب ساعت ۳۰ دقیقه بامداد و 4/30 بامداد انجام میشه ..چه فوتبالیه نروژ و انگلیس ساعت 12/30 شب امشب
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/135553" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135552">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❗️
برنامه کامل مرحله ¼نهایی جام‌جهانی
😀
فرانسه
🆚
مراکش
😀
🗓
پنجشنبه ۱۸ تیر ساعت 23:30
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
😀
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
😀
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/135552" target="_blank">📅 23:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135551">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2012e42d0b.mp4?token=ePpGLldYlxE_E6UiR6jozcn2QFWJSDnx9_x4P9_BN8FaZ0wk4uJMwZcnHBNINXjJdiARwCSa2iljMfsQKf0XYQPm5ZjWvJvBV7ZorBRr4H_o64oRRLsh9em9oG_uBmMKZBYaZLNaj2H_cK8S_zk8MESY1NAIsVCfoPAZYmh0rwJAJRVcJi8vv-WSn8a9Hc2MqbUnov_CeE45TcnowcesUxpfLwokYY3n42SR5IsDgmydXahNtSoRfJCK1RfN-XBu0NFn8TMHychEUnno7GfFzLNs7jkGj1LxyLY3kt3HKNh6rHSnZSPF2lVr2GsNqwtp9rNTL-CzKc6Z2FrNAL5BiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2012e42d0b.mp4?token=ePpGLldYlxE_E6UiR6jozcn2QFWJSDnx9_x4P9_BN8FaZ0wk4uJMwZcnHBNINXjJdiARwCSa2iljMfsQKf0XYQPm5ZjWvJvBV7ZorBRr4H_o64oRRLsh9em9oG_uBmMKZBYaZLNaj2H_cK8S_zk8MESY1NAIsVCfoPAZYmh0rwJAJRVcJi8vv-WSn8a9Hc2MqbUnov_CeE45TcnowcesUxpfLwokYY3n42SR5IsDgmydXahNtSoRfJCK1RfN-XBu0NFn8TMHychEUnno7GfFzLNs7jkGj1LxyLY3kt3HKNh6rHSnZSPF2lVr2GsNqwtp9rNTL-CzKc6Z2FrNAL5BiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
پیمان حدادی: تارتار درخواست اردوی ۱۰ الی ۱۲ روزه خارجی در ترکیه داشته است/ اینکه به ما مجوز بدهند یا نه مشخص نیست/ در این شرایط شاید مجوز گرفتن سخت باشد/ فردا جلسه‌ای حضوری با سید شروین اسبقیان در این خصوص خواهیم داشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/135551" target="_blank">📅 23:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135550">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lojuujlz3CnhdcUUpxkk8vMeAYQChCbuYKLJlL318NwHB5pUMaDgqIzfQFnvP05exjnCsPDB04hHhhsYw3jTJAlNuB-xLDQuH1azL-UCyWkLyehA971dFclpMpIyvG8spMpZl6A4FeSmbrISZBU3Ew2Vwyh51Zhu_jolHyEE6AQ7ED4njucPbvQFWzMgqMDt7OmZpJxHJYUBsCyiEk8PUB1jCZI8vN2NPBmSGm5RaO3hT-CcvExXtOC-q_JKHAVmdaQ1d_XzG6GolwLEY-iOWiU2puzHBazhdgxStOeAvaK7pC5BJg-yKMDVZoNmsAfo0dxhUoL6A8SftGmzKpoMxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوستن اورنوف طبق گفته خودش در پرسپولیس موندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/135550" target="_blank">📅 23:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135549">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">💢
#شایعات
🔴
میلاد سرلک با عقدی یکساله به فولاد خوزستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/135549" target="_blank">📅 23:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135548">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc20504608.mp4?token=G3RxZr9Jb5w3rHjrgeROtjR6ZhNmX8BMCw-fjR1RYPyU0CegF1QIzCP8dCoeha_CCY2PuWnh9cQ2q2tujlMkw6QOZUNJVE3B-VzoGPO0oZLojLbKdzb7iDUNcqcGDEOZX6VfJVuVx72LLFy8q4i1VrJcu5LSBSOzM6W9CxN5INkecHOFpETNGr3Z9ghr4GJrRqoKJ7nPf9D53pyUh5ap8mD43TNJrN1hw_uuKjAPyeSkULlPWLiWyUXEUUusfUzaAHNuZ9KkbX04yGU84N0N-yUFXF3XLMCRwWcPux98Wh5pC3xqhWissWrBboK_UEbgSJUR4n8vl_D_olywAmn0ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc20504608.mp4?token=G3RxZr9Jb5w3rHjrgeROtjR6ZhNmX8BMCw-fjR1RYPyU0CegF1QIzCP8dCoeha_CCY2PuWnh9cQ2q2tujlMkw6QOZUNJVE3B-VzoGPO0oZLojLbKdzb7iDUNcqcGDEOZX6VfJVuVx72LLFy8q4i1VrJcu5LSBSOzM6W9CxN5INkecHOFpETNGr3Z9ghr4GJrRqoKJ7nPf9D53pyUh5ap8mD43TNJrN1hw_uuKjAPyeSkULlPWLiWyUXEUUusfUzaAHNuZ9KkbX04yGU84N0N-yUFXF3XLMCRwWcPux98Wh5pC3xqhWissWrBboK_UEbgSJUR4n8vl_D_olywAmn0ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مهدی تارتار: پرسپولیس چیزی برای قهرمانی کم ندارد/ من تشنه بردن جام هستم/ از هواداران می‌خواهم من را بپذيرند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/135548" target="_blank">📅 22:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135547">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
تارتار: وحید امیری تمرین میکنه اگه خوب بود به تیم اصلی اضافه میشه یا نهایتا به کادرفنی اضافه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/135547" target="_blank">📅 22:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135546">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
فوتبالی: وحید امیری از باشگاه خواسته یه فصل دیگه بمونه تا با پیراهن پرسپولیس خداحافظی کنه. خودش هم گفته حتی اگه بیشتر نیمکت‌نشین باشه، مشکلی نداره. حالا همه‌چیز به تصمیم تارتار بستگی داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/135546" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135545">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
❗️
حدادی : آقا کریم امروز با من جلسه داشتن که اگه کادرفنی ایشون رو نمیخواد بهشون بگن، آقای تارتار ایشون رو میخواد و بزرگتر تیم هستن و از فردا سر تمرین هستن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/135545" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135544">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
تارتار : تلاش میکنیم یه تیم قابل احترام و باغیرت و جنگجو درست بکنیم. من تو این سالا با هیچکس لابی نکردم، لابی من خداست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/135544" target="_blank">📅 22:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135543">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
تارتار : من تو مکتب بزرگ پرسپولیس و پاس یاد گرفتم باید برای جایی که هستی واس پیراهنش بجنگی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/135543" target="_blank">📅 22:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135542">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
تارتار : فضای مجازی کاملا با جامعه فرق داره، من وقتی به خیابون میرم یک نفر از هوادارای پرسپولیس به من نگفته چرا اومدی؟
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/135542" target="_blank">📅 22:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135541">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
تارتار : من یه مسئولیت بزرگ رو قبول کردم، میدونم‌ پشت این پیراهن تاریخ و هوادارای چند آتیشه هست و هوادارا بدونن انتظاراتی که دارن رو در جریانیم، با توجه به شرایط کشور هم پرسپولیس به من میتونه کمک کنه و هم من به پرسپولیس، من تشنه جام هستم و تو بعضی تیما نمیشه…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/135541" target="_blank">📅 22:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135540">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
مراسم رونمایی از مهدی تارتار امشب ساعت ۲۱.۰۰ برگزار خواهد شد و از شبکه اینترنتی باشگاه پخش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/135540" target="_blank">📅 22:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135539">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗️
حدادی : پول اسکوچیچ رو میدم بازیکن با کیفیت میگیرم
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/135539" target="_blank">📅 22:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135538">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
حدادی : اسکوچیچ زیاد پول میخواست بیخیالش شدیم!
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/135538" target="_blank">📅 22:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135537">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
حدادی: جلسه گذاشتیم خلیلی تارتار رو پیشنهاد داد گفت خیلیم خوبه
😆
😆
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/135537" target="_blank">📅 22:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135536">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
حدادی: اسکوچیچ وسط فصل تیم خوب و پر هوادار تراکتور و ول کرد و رفت و باعث شد تراکتور بدون جام بمونه و برای من جای سوال بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/135536" target="_blank">📅 21:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135535">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b795de8c95.mp4?token=JB2LjPu7zda_jajCBhRuVQu6PTavY9Pn8MwJfI44JU6KMuGob4QrD0YsYTgfv03DkFfujbAXq_zKV4u-oSmDvvSQoGUIOXBM0h2mjMUxgLpgYxnm8DzCmvlJe8CCeqTy_rcETK0B2H2o5RrskflIxmfoZEAz9z4Ludxav852Dr78qwtrRqsHPBn52oBDswBB5BARWskyofU2v31KCMHQf1E5SWVYW7m152CHQODYnyg7lRkgSxMxWwC300Jz6eDdk1xRFJDWKoyhTlSeIcVLvXaLS9fR2yDjiBv2_rFyBFzydssj1S06ajqg1Xyo22C_6Tym2uGBssNqiOm13pIPiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b795de8c95.mp4?token=JB2LjPu7zda_jajCBhRuVQu6PTavY9Pn8MwJfI44JU6KMuGob4QrD0YsYTgfv03DkFfujbAXq_zKV4u-oSmDvvSQoGUIOXBM0h2mjMUxgLpgYxnm8DzCmvlJe8CCeqTy_rcETK0B2H2o5RrskflIxmfoZEAz9z4Ludxav852Dr78qwtrRqsHPBn52oBDswBB5BARWskyofU2v31KCMHQf1E5SWVYW7m152CHQODYnyg7lRkgSxMxWwC300Jz6eDdk1xRFJDWKoyhTlSeIcVLvXaLS9fR2yDjiBv2_rFyBFzydssj1S06ajqg1Xyo22C_6Tym2uGBssNqiOm13pIPiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهاب زندی: دانیال ایری بازیکن ماست و دیگر قابل فروش نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/135535" target="_blank">📅 21:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135534">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
حدادی: هی میگن چرا از گلگهر بازیکن میخری؟ مگه تراکتور از ما بازیکن نخرید چنتا رفت قهرمان شد؟ گل گهر با سه امتیاز کمیته انضباطی نایب قهرمان لیگ برتر و جام سه جانبه هم در آستانه قهرمانی بود
😕
😕
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/135534" target="_blank">📅 21:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135533">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
طبق سیاست مون بازیکن بالای 30 سال نمیگیریم
🔴
آخر هفته از سرلک و عالیشاه قول گرفتم بیان سر تمرین تا مراسم خداحافظی داشته باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/135533" target="_blank">📅 21:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135532">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
فوری از فرشید حقیری: پرسپولیس با وحید امیری قرارداد بسته!!!!
❗️
پ.ن جونم به این جوان‌گرایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/135532" target="_blank">📅 21:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135531">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
پیمان حدادی : فردا یا پس فردا با آقای علی علیپور برای تمدید جلسه داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/135531" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135530">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❗️
پیمان حدادی : ما به میلاد محمدی پیشنهادمونو دادیم فردا آخرین فرصته که قرارداد رو امضا کنه اگه نکنه از لیست تیم خارج میشه این پرسپولیسه که واس بازیکن تعیین تکلیف میکنه نه بالعکس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/135530" target="_blank">📅 21:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135529">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
پیمان حدادی : صحبت از مهدی ترابی، دانیال اسماعیلی فر، آریا یوسفی، رامین رضاییانه آیا تیم رقیبمون به ما بازیکن میده وقتی قرارداد دارن؟
✅
مثل اینه من اورونوف رو به اون تیما بدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/135529" target="_blank">📅 21:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135528">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
پیمان حدادی : این معقول نیست من برم دفاع ۲۱ ساله رو ۲ میلیون دلار بگیرم؟ اگه این دفاع رو ۲ میلیون بگیرم به بازیکن ملی پوشم چقدر بدم؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/135528" target="_blank">📅 21:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135527">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
پیمان حدادی : بازیکن های ۲۶ تا ۲۹ رو قصد داریم طوری جذب کنیم که رضایتنامه براشون پرداخت نکنیم
❗️
بازیکن های زیر ۲۵ سال هم با قرارداد ۴ یا ۵ ساله جذب کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/135527" target="_blank">📅 21:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135526">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
پیمان حدادی : تیمی که داریم میبندیم تو ذهنمون هست که میانگین سنی بازیکنا بین ۲۵ تا ۲۶ باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/135526" target="_blank">📅 21:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135525">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
❗️
پیمان حدادی : یکی از اشکالات ما در فصل های قبل این بود که در پست های مختلف بازیکن رقیب نداشته و بازیکنایی رو میاریم که انگیزه داشته باشه، بازیکنی که ۴،۵ جام گرفته دیگه اون انگیزه سابق رو نداره، قصد جوونگرایی داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/135525" target="_blank">📅 21:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135524">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
پیمان حدادی : تو نیم فصل با اون شرایط کشور ۳ تا بازیکن جذب کردیم ولی هوادار از این پنجره نقل و انتقالاتی باید از عملکرد مدیریت انتظار داشته باشه با تموم محدودیت هایی که وجود داره، از این به بعد کارنامه مدیریت تو نقل و انتقالات مشخص میشه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/135524" target="_blank">📅 21:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135523">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
پیمان حدادی : شما بهترین سرمربی رو هم بیارین وقتی ابزار لازم رو نداشته باشه نمیتونه نتیجه بگیره، اون سالی که آقای اوسمار تیمو قهرمان کرد اورونوف رو ساعت ۳ و نیم شب آوردیم عبدالکریم حسن و آل کثیر رو آوردیم ولی تو این ۲ فصل ابزار لازم رو سرمربی هامون نداشتن…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/135523" target="_blank">📅 21:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135522">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
پیمان حدادی : ما به درخواست هوادار آقای اوسمار رو آوردیم ولی اون چیزی که انتظار داشتیم نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/135522" target="_blank">📅 21:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135521">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
پیمان حدادی : خیلی سعی میکنیم که دچار هیجانات فضای مجازی تو تصمیماتمون نشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/135521" target="_blank">📅 21:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135520">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
🏅
تفاهم نامه همکاری بین باشگاه پرسپولیس و فدراسیون کشتی توسط پیمان حدادی و علیرضا دبیر امضا شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/135520" target="_blank">📅 21:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135518">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
امروز اقا کریم با باشگاه جلسه داره و تکلیفش مشخص میشه/ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/135518" target="_blank">📅 21:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135517">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/135517" target="_blank">📅 21:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135516">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
باشگاه پرسپولیس خبر داد: امید عالیشاه با توافق دوجانبه از پرسپولیس جدا شد
❌
باشگاه ضمن قدرددانی از فسخ توافقی خبر داد و برای او و سرلک آرزوی موفقیت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/135516" target="_blank">📅 21:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135515">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
ویدیوی باشگاه پرسپولیس برای جدایی میلاد سرلک، هافبک این
تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/135515" target="_blank">📅 21:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135514">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join
Join Join Join</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/135514" target="_blank">📅 21:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135513">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Na16ZPUx4UC_wtPrBydAhOFSEMN46ZOru3e1V-Sc3AXhp6TPa92PxXQ5LTZ1zhuCe89j-ODImmTH__rEaEKFfJaZenozr9Ft0C77dHxX171vov2Uz3voT_Yl9Y3icCz6UuLmiD8IPQDp0T6B_6K5zo_LPOQSWwmuycXrrHmi9KRJZco5KQKUyW0E0IGh2h4yJhUolYwc8sjGtLWVkCQq42-NvNWMyArokiB_DjfWZZAzDGD2s1UAHZw9Gc8omPK9PAvfAwK-QqGkwPbQPP5CkZfvYe4wqWQ19UH0XUkQ72eGSpHYfhITvy9WdIAu49yuKrpbUPAOnCZhaBzdOP1YZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکسمون عالی برد شد
✅
💵
✈️
@Bet_Giantss</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/135513" target="_blank">📅 21:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135512">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlYt3Jv5QL8p-qGZHSclVmP32A6EWQKU9BlUYAakwPwmGm3voQ5e7UHD3aomYuB7nC9bPn0UeSuwLsnNh0KogjJWm4BA0OY9ilCQ0JDNfxbIg5Iftnncx2gXeq3fqDm43skJwhlQ2vG0CSNR626BwGfk6s8RNJFFBzZfrut0Lju4DZYeKVnj11yzV0WnZYahpVWvssBes0YxC-AkyQik8mOWbKth_6uJujCyx82J2oqW1Ajv1pEGeC23lXMCv8AYscprvyvmYMU-41yyVOvNms2kmKQT6RAqJcHlENJL4gaa0aJdBkRnol3DNFiDCWp9fSnrxB5E-X0dlvm2R-Dzxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔴
امید عالیشاه.. کاپیتان پرافتخارترین پرسپولیس . پس از 13 سال از پرسپولیس جدا شد
😭
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/135512" target="_blank">📅 20:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135511">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
باشگاه پرسپولیس خبر داد:
امید عالیشاه با توافق دوجانبه از پرسپولیس جدا شد
❌
باشگاه ضمن قدرددانی از فسخ توافقی خبر داد و برای او و سرلک آرزوی موفقیت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/135511" target="_blank">📅 19:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135510">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2uYS0MK_PHlCOw3oAYe5x7ECj83NvTGfXV0gxjzixr-0nq6Zh2T8cTjpdLzakcBrE8urqleIkJ-3dqujOJfKZzd-kF-a3YKIAl6UR0-lE7hr3Y7KpKjq101cpjNdM1qgoU58wASlMnrE5iVTaSHJ0YLIk0m3wmVRsAuTqr1ozQQdPuAly2rP86O0ub-d1S6JswfLwhbC9kyRfQukEJbQHReTOu20rNU9UcErlqk8KHGJ_dvGibBGZ8-0ATlzTTD50nIrZ3-niFKtORX7JW5MsSY_xhti20l2Y_FFnFkKNU1BNnce6UfeFtlV8k1-fY7AGgR3CGKIizo4YzYU8QW3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/135510" target="_blank">📅 19:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135509">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
میلاد سرلک به شکل توافقی از پرسپولیس جدا شد
🔴
پس از مذاکرات انجام‌شده بین مدیریت باشگاه و میلاد سرلک، هافبک تیم فوتبال پرسپولیس، طرفین به توافق نهایی برای فسخ توافقی قرارداد دست یافتند.
❌
در جلسه‌ای که امروز برای بررسی وضعیت قرارداد وی برگزار شد، با موافقت دو طرف، درنهایت قرارداد میلاد سرلک فسخ گردید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/135509" target="_blank">📅 19:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135508">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFJLYyxgtKZaBpjzgfZbvNqmt33CKy4eLuE3l9-AGD7wezOq4wUY8lhZUdWnQJf8Bm7j_kZpYxd6VBz5PiDScfz3VBB91lLF6enLFfLxScZqyoCRPRqzwajYL0NN9tjXqALiNOmSism2bSYymHq1JK9IxJKAPX0j6R4iXe3o5OV_kXo1Tr766Ug6QX3Gi2WfxLbzdQPnE9vznRyvfP7GGqEHGtMdoqaMAeuBWf2HraHym00NtoZAWLYdK5LLl8KluC1bOG2n3_kmyP67s0Zc960Um3QzDBKgY1L9M_54LhSndggRJTNdOdKY7N8TGrkhIeQVOUxDeOtNBSQSGf1ccA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
❗️
سرلک بخشی از قرارداد فصل بعدش رو دریافت میکنه و بعد جدا میشه/ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/135508" target="_blank">📅 19:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135507">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/135507" target="_blank">📅 18:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135506">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135506" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135505">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
بنظر میرسه امشب پورعلی هم رونمایی شه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135505" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135504">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
✅
پوریا پورعلی با خداحافظی از گل گهر یک قدم  به پرسپولیس نزدیک شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135504" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135503">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
فوری از فرشید حقیری: پرسپولیس با وحید امیری قرارداد بسته!!!!
❗️
پ.ن جونم به این جوان‌گرایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/135503" target="_blank">📅 18:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135502">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KFgLFUziEDg7ypR-6MNVUH98ILdzJQPHb1GhN2SVJeBhhTRJ6Dn8m7r9KNmQcOjNGUoQxSJ5UaUOAVDJAo7Y67A-8ANOb9WOb-BuOd9ancMSf4KG4lvo8Va9lafu-7M99rTOssdaKvqi2vfMoHSkDKj_k_tviEKu4Ez3Rs6HzOLHHldNqyrBHILZ3C-tG-_9b6QG9Lxdy5OBAtpbaIqbt3VYpRji6P5T8EzQL8rZbpcDKP2vI0wf9Iq9qBkxpUsw5b5eHTp2RXwOsFaSUyTKg9dMq73uJsG5fol0eLNIvMkQwNruijbe6Y3rB9PPrF7FUp2puKktnJHVWoxSJr-isA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ادعای فرهیختگان: محمد عمری از لیگ قطر و امارات پیشنهاد داره و ممکنه باشگاه با دریافت ۶۰۰ هزار دلار از این تیم‌ها رضایت‌نامه عمری رو صادر کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/135502" target="_blank">📅 18:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135501">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❗️
❗️
سرلک بخشی از قرارداد فصل بعدش رو دریافت میکنه و بعد جدا میشه/ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135501" target="_blank">📅 17:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135500">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔘
🔘
🔘
باشگاه پرسپولیس فردا یعنی روز شنبه مذاکرات نهایی و پایانی خود با دانیال ایری و باشگاه نساجی را انجام خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/135500" target="_blank">📅 17:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135499">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
🔴
🔴
تارتار گفته چون فعلا تو جذب هیچ وینگری موفق نبودید اجازه نمیدم بجز عالیشاه وینگر دیگه ای جدا شه و هروقت جذب کردید میزارم جدا شن
🔴
بدین ترتیب بیفوما و شکاری فعلا با تیم میمونن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135499" target="_blank">📅 17:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135498">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
برگام فیروز کریمی شده کارشناس بازی های جام جهانی کانال  gem tv
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135498" target="_blank">📅 17:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135497">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
فوررررریییی با اعلام ترانسفر مارکت علی علیپور از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135497" target="_blank">📅 16:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135496">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4YcU2MPmJGBeI8s2W7zn4IF4VXNb6lp8_4tFHgYlUYQjYTCDsttVTdWovZHOoagmGK0d3OxnZXMJVZHlBtlByT_DOU-0LE8quBJ4Da1w9Ovk_D_e01QdfiRIUn6WHXPuHntdFqZeedRnRpJLxQ9SF3nWEWZsNainR70n795lfkOs6OlnYv0-uaymNYXsohFLVjArIXslHq7mPqXecA4ccQy4Y_dzZ742HdzYJ8APaX1aDN-Sh4ja-d32OLj83bD3AtCdclPkjE2iTg251EwOHWy5DGlkj8F5u9IafzVTksK2y_M68sIeDyxCzpk9sdrSJbhe4ErIYeN7vPxEYqjLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری؛ شنیده ها: رضا شکاری از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135496" target="_blank">📅 15:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135495">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dOcJf5RKXQlu_Zye0iTrCm9jKYzeroNXXeYbSesva640ByVLIKsFIqVYfjV3drQyy9ZjIC6oZ-z3VAnxQxHKme62uCft21VvsiATLe8PgtSkNryArX8u78LVKm9QMRh-eBOR7GzCNq2aBMbKfSSmciOU9rImUr588jGBS-Exi1cp4yBcFt1qGPXkbRadZ_X5h_S9kdUvNO8NV3Ae2ySFeWsquaZStjYpQRitrPcc-KybYWT46pW9sTubPmKK7cuY7-an5cDfqZhgEFgmddOVNY4zoGlW-0mbE2fGMR2m-rCodl9rO4qvelmiJhQJRT5OmEnnTVnDCLbuVup9POLaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری از فرشید حقیری: پرسپولیس با وحید امیری قرارداد بسته!!!!
❗️
پ.ن جونم به این جوان‌گرایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/135495" target="_blank">📅 15:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135494">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyww_RFmH9nkD1wcZVensLsMKVRMcaUPeBqEl6z_h70Iv0EKnY5jLV1JRABzjdSE7araSIyrYATrKrQUdg6CRoizMtY_BE-ddGU7hWGh4wY1tfR0CJ2Q_wR1ePx6-v4MzxejBQEE_MXnp69ixRaMEt0TvQ6FLuCurwCvIDeeNkg4QuHYEGK3tuPg8Kjc5E7_jHVgVYMnDONc7G-DtWrMn47SFPMNEbhLY9-AstQ0zsnKYrvfELRX-fK7L9YogIRL6aSqsGyiOqwEOmKMl2Rw2hCXyR3YzqOPVKnaR6awW7WSKf1GBxHvHr4scsSN0Il5TNPrDVvmr75Kq6MibdBKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏅
تفاهم نامه همکاری بین باشگاه پرسپولیس و فدراسیون کشتی توسط پیمان حدادی و علیرضا دبیر امضا شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135494" target="_blank">📅 15:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135492">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🏅
پس از امضای تفاهنامه با باشگاه پرسپولیس؛
🎤
صحبت‌های علیرضا دبیر، رئیس فدراسیون کشتی
❓
دخالتی در قضیه خداداد و پرسپولیس نداشتم
❓
ما فقط معرف بودیم
❓
من نوکری ورزش ایران را میکنم
❓
از ایرانی‌های آمریکا تشکر میکنم
❓
بهترین ایرانی‌های خارج از کشور در آمریکا هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/135492" target="_blank">📅 15:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135491">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
🔴
🔴
ورزش سه در خبری اختصاصی مدعی شد استقلال به سپاهان و پرسپولیس هایجک زده و علی نعمتی رو به خدمت گرفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135491" target="_blank">📅 14:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135490">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
کریم باقری از شنبه یا یکشنبه به تمرینات برمی‌گرده و مشکلی برای حضورش نیست.
✍
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/135490" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135489">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس می‌خواهد برای کاپیتان مراسم خداحافظی بگیرد؛
✅
✅
باشگاه در تدارک برگزاری مراسم خداحافظی برای امید عالیشاه است؛ اتفاقی که در سال‌های اخیر برای هیچ بازیکنی رخ نداده و نشان می‌دهد باشگاه قصد دارد با احترام از کاپیتان سابقش تقدیر کند.
❗️
❗️
حالا…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/135489" target="_blank">📅 14:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135488">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
مجتبی فخریان بصورت قرضی راهی گلگهر شد تا پوریا پورعلی بصورت رایگان به پرسپولیس بپیوندد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135488" target="_blank">📅 14:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135487">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135487" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/135487" target="_blank">📅 14:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135486">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s5CqwJCKpqxcHX8YO6yE8lBHxW0CeQnvVQsohjz9U5Gsay9iVKfu9oFU69FrJax7E98c1No7qwQ_md3LzvB0TYrpsb_gG5BTqRUs8ejFmRd2m23ZjYld3FoSDde--rX9pnFsjav_kn32ZMBIHiKf1yOEhu08DpURcSZf_0DDvv0_HiNsNzGP70foSqm6yVhfry0ivvujcSsWn0hBbtQcLRV_vAVnQq6dHdNt5__JHTOWikbbVLBi0Hi0Uf8oDbVMmKh-Kq_bnmshiuV7a19KS1eFAcTAheD__CUfk_DZ9HPKRfWJ7dZ338UDUz7LOPR767yOBcXtJ749-_lhC8hatw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135486" target="_blank">📅 14:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135484">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ST4p3YHNsL5pXcnrXgEoeSycU3tpI6udSHXAUWOrdVDx_HQUknhWwCYWe6aSJij7uskvzxMO3TmRP05VrAyyNrP252l-H-UQaQD8MaQAj6VR8DyU0Vi5co2Ii2YV1skfnn6c2NsEgPKnZwnJ0DVMwyIcSKKau-LhUXlqfIDG1eQsmIIibVJ5pM8Wx0d6AV2LowVudat8rP9UIb4M_LyG27bQjbHCsWXmDb0jI9Pikniop83wu69_uwYqQYUZr08GAVrQ2RdMtY7YbXa4lkMQ3XLMfUsPKj-AUkKOiyJeKv3dAtNyQeMxGVzIV7dt0oUERd2JI92Vfcd3pCg9dEdG9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
میعاد قاسمی، آنالیزور و دستیار تارتار تو گل گهر سیرجان به عنوان آنالیزور جدید پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135484" target="_blank">📅 13:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135483">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
❗️
باشگاه امروز به شکل رسمی نامه زد تا پورعلی گنجی، عالیشاه و سرلک در این تمرین شرکت نکنند!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135483" target="_blank">📅 13:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135482">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPcVKyPvZ0uFTTyfoPSY2Y8OYzvXciL77uevE9aZG0CZ9bMEYOI2wu2n1V8_kgEnGAoBbBdNN20w6OW0aD7cyBfYTietAmhI1kVzN0BjK4dHAiE0mvK3krKH9kTUnzu3Jl8mmkC3_BLYq_gBkz1JNO5C2ibyU54XooC9rymxVbv_r5ZAORlrqcZ-f_BzYsKA2W33Y7AVtpdcarhJQrNUiAhWBb0Mj6hFE4U0fMKtOI_OtP1VQMnLp_NwrU4gPAG9Ms7HlXnIsu8g6WNm_FkM6a7oRf_Vs-2lHRIIohMvzjnczOKTcdiIh_AeCJ0KNQ612GK1e9Tu91tYVVkCU9ZPPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تمرین امروز سرخپوشان در سالن وزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135482" target="_blank">📅 13:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135481">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
🔴
علیرضا بیرانوند در پایان شهریور 1405 یعنی حدود 2 ماه دیگر سرباز است و دیگر مجوز بازی در لیگ برتر را ندارد؛ مگر اینکه راهی یک تیم نظامی شود.
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135481" target="_blank">📅 13:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135480">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
مجتبی فخریان بصورت قرضی راهی گلگهر شد تا پوریا پورعلی بصورت رایگان به پرسپولیس بپیوندد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/135480" target="_blank">📅 13:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135479">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
فووووووووووووووووووری
📊
محمدمهدی زارع در تلاش است تا رضایت نامه اش را برای پیوستن به پرسپولیس بگیرد /فرهیخگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/135479" target="_blank">📅 11:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135478">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
فوووووری / ایسنا
🔴
پیشنهاد پرسپولیس به اسلامی و کوشکی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135478" target="_blank">📅 11:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135477">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
📊
علیرضا کوشکی وینگر استقلال تهران در لیست خرید پرسپولیس نیست/تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/135477" target="_blank">📅 11:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135476">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDuJ8GACqbKzq5XiVjfg32fcO0nfVot277cOdE_qasTIH9osT5mgQnQJwWTyAVpYmY6mkDelFbwSPd8FlDEd6FI_fp9gw8mGRLhuczfcpYoZtR-T6Ztno0q74yEj9yMDmmBzGVBIOgp7kEhzIGgjcDEuK3tRC7dFHjT7L2zgiPj6pqIxQxeNxdYMm3Vimv0iL2MO-IhhxKbEpbyRa20oDmJK29zFkkPxOoMbdbDmO16a_FFtHRp8hqZgTnwGOzwXJ-e6ERsn1s69zOu-7nW-JMVFE_Q2SqCrjhthKd3ypOvz-hD_2vxhDZyZGBjqKOWucR_X7qUM0GjNGRqsexPKYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
مراسم رونمایی از مهدی تارتار امشب ساعت ۲۱.۰۰ برگزار خواهد شد و از شبکه اینترنتی باشگاه پخش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/135476" target="_blank">📅 11:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135475">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
پرسپولیس میخواد برای جذب احمد نور به کلبا نامه بزنه/فوتبال 360
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/135475" target="_blank">📅 11:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135474">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">💢
مدیران باشگاه‌ موفق شدند با محمد مهدی زارع به توافق شخصی برسند و قرار است مذاکرات با باشگاه اخمت گروژونی انجام شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/135474" target="_blank">📅 10:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135473">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
✅
پرسپولیس برای برگزاری اردو پیش فصل جمعه هفته آینده به مدت یک هفته تا ده روز راهی ترکیه خواهد شد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/135473" target="_blank">📅 10:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135472">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
فرهیختگان: تارتار درمورد این تصمیم خواهد گرفت که آیا وحید امیری در پست مربی در جمع پرسپولیسی ها خواهد بود یا به عنوان بازیکن؛ چرا که هم وحید امیری با تجربه است هم چند پسته است هم از آمادگی بدنی خوبی برخوردار است و ممکن است به عنوان بازیکن به پرسپولیس اضافه…</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/135472" target="_blank">📅 10:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135471">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
پرسپولیس؟باز هم نه؛ترابی بازیکن آزاد نیست!
🔴
فرهیختگان: در شرایطی که در روزهای اخیر اخباری منتشر شده که مهدی ترابی بازیکن آزاد است تا دوباره جنجال‌های بازگشتش به پرسپولیس برای چند فصل متوالی تکرار شود، براساس شنیده‌های «فرهیختگان» او یک فصل دیگر با تراکتور…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/135471" target="_blank">📅 09:30 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
