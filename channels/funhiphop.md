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
<img src="https://cdn4.telesco.pe/file/K0TdvlDyrlflgUanRmE1jNKVxbAFJCy0iFNyTEzE6dnL51eG1_dty_FYKoJgYXNpHLreza9LCvpcCQReBQZVXP2vAiHxbSnUfBIWb6b9v3yDPIJYbRpWzuVLR77tUHy_Dq8Zh4hvTLLqdHG_zB1mKMlGqwPZ4CJcHo5JRYdrkswt56qzv0RwFbUmMN3HAEFc95axDkrGkKo_s7NMoWdhhnmJDsy-8Q1c3hdrgoEM7fiSsDJnjTUwTbuZd993BgZn0jPtLyfJr2Y9OwcMlcbQd8JXx6Oi3IP5JdXI9SN_fumJ6A6dVHk8YsljlNi1eOUNLOdDn7gWbGEpF5Jd8kL7dA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 198K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 18:23:08</div>
<hr>

<div class="tg-post" id="msg-79729">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خبرنگار:
هیچ برنامه‌ای برای اعزام نیروهای زمینی به ایران ندارید؟
ترامپ:
چرا باید الان وارد عمل شوم؟ وقتی آن‌ها کاملاً از بین بروند یا زمانی که توافقی حاصل شود، آن وقت اینکار را خواهم کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/funhiphop/79729" target="_blank">📅 18:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79728">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فعلا تحلیل نکنید تا پیشرو شیشه رو بکشه، میاد پیش‌بینی میکنه برامون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/funhiphop/79728" target="_blank">📅 18:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79727">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ:   محل نگهداری مواد هسته‌ ای ایران را شناسایی کرده‌ ایم؛ این مواد در زیر کوه‌ ها دفن شده‌ اند و ما تجهیزات لازم برای خارج کردن آنها را در اختیار داریم.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/funhiphop/79727" target="_blank">📅 18:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79726">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ:
محل نگهداری مواد هسته‌ ای ایران را شناسایی کرده‌ ایم؛ این مواد در زیر کوه‌ ها دفن شده‌ اند و ما تجهیزات لازم برای خارج کردن آنها را در اختیار داریم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/funhiphop/79726" target="_blank">📅 18:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79725">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">زودتر به این ترامپ تریاک برسونید آروم شه</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/funhiphop/79725" target="_blank">📅 18:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79724">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2PSk8DZe2ltyPjJFUp9H_XPupUlZnarEP8-o0DeqMZgm5762uH21YI-dvckvl0ZyG4nJPF8JbdrQQkf000ZUkbeOCspF2-t8gPO7aUmvfd2JNYc6wGsTaFXBcBQyU0VFM8qZeMMbBrATRLHC3J4FA0C9eAYRp_OS1vKm0YVKpYa4x054xd7Z4GoMx7bShl96yPhhIPaHER8aSv8XMi7Ypq5EnzDFHqrSfdkCbOWnJYHUJOkiVJ2o1eZUptzeut2IUJ_VGN0gTyaU_EO0o5zAJDMAH_gYmX9k2Jg7n19yOapASi0z4sLlXvv7TtkkCG6A_HvbamrHS3wMLXJYdOREg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه.
آره.
به تو ربطی نداره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/funhiphop/79724" target="_blank">📅 17:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79723">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJQFA-60X21xF6QP461MZ5Wmd4OM3azbntM_bIs1p5u623aRuXn7uA_SofRXsfcaZZfoLl1azSNxrCxGWVChYCTPZS6kw8r27k_v3VX1cMhee-aytTBq0_im6EV6TXXgc4N1COS-W2Xi80SIGhu3Skn2kRfw3FYAe_FmLBHCLgaBEZJ9-qXTquGKj6vU2TBeqrCeZCazDhsvl3gLfSvBUDoUL4G9tSFlYJszTmSMRpTpUwoo2WXYd-Hul3wlJpjwHkh6mIGZAkGYThy3hw9QpqTSjx9up1M-_yhR3KxO4JGGJkW9Igqx4r5qmxAeMSkbuQMmhoGdXE3zU6nRmYLw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کاگان و آرون به نام "Geek" منتشر شد.
SoundCloud
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/funhiphop/79723" target="_blank">📅 17:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79722">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ویناک میخواد ترک "بلاد۲" رو بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/funhiphop/79722" target="_blank">📅 17:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79721">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐀𝐦𝐢𝐫</strong></div>
<div class="tg-text">صدف چاق تره
احتمالا مادر صدفه</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/funhiphop/79721" target="_blank">📅 17:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79720">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WesO_UFaQC9XdfuTvhODMMU5mXAAaAPsDtNEbr4hedreX1hMiI88H740r37HA70D3D9VsIysp8mJF3RFnjd0eYNN_9Dyq3b5q5nwhK6VjIuUYh1EPmEbcLmRkoVbuSq6ta-dogXS5TZU5jUocDWA6ludOpq-jg0URHPwc32a-NwyTND8K74bHqigt4PVKD3SOVfceMrDTgETymx5OiRymPs47ZGABYJ3WwYghY0VlWLNM48nUXWJ8C6whQpXmhExOnZLz0R4QOG9EZwP7g3qGF7rgnlPCUf4kIpU_rxKrUyZIyjsHf8XY8RH-aKEGbydvrVb3o8-ePv08DF42FKV6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی یه کاری کرده کاور صدف باشه هم تعجب نمیکنم   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/funhiphop/79720" target="_blank">📅 17:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79719">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ هربار اینطوری تهدید کرده هیچکاری نکرده، خبری نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/funhiphop/79719" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79718">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ: امکان تصرف جزیره خارگ هست.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/funhiphop/79718" target="_blank">📅 17:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79717">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b6fceb66a.mp4?token=F1yGb40nV7q8sz2fMwE1IGUiVDhOWsIE5cn5v0gsA2nNS1AlIKr9S3Q7ZPm21ihD2gMV4T0g0WqzmZRjx8IaHTYuvODumj9IxutrkN8JjQM1Kt9bbcxaXLy4luuT3Dw0VdP3jmfm6FRP7od6tb_tvB_cHOgDfAGFzRRK1WupwRZ5VcMis2lLV_kiDCdfVXlLtSLFEcxdYeXd6PYjTzTeq1JWvVwHk6og9nbfHkUXoSaDhikeyEAbgztxrnvQVOMlDHrp-HCmmJgbqS78u-n1R3yA0d3Y9HLEBxZ9V2ivY318do5cXX9bg1Y43wkjSouPr4d9onEIs6srJI2grW9Gjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b6fceb66a.mp4?token=F1yGb40nV7q8sz2fMwE1IGUiVDhOWsIE5cn5v0gsA2nNS1AlIKr9S3Q7ZPm21ihD2gMV4T0g0WqzmZRjx8IaHTYuvODumj9IxutrkN8JjQM1Kt9bbcxaXLy4luuT3Dw0VdP3jmfm6FRP7od6tb_tvB_cHOgDfAGFzRRK1WupwRZ5VcMis2lLV_kiDCdfVXlLtSLFEcxdYeXd6PYjTzTeq1JWvVwHk6og9nbfHkUXoSaDhikeyEAbgztxrnvQVOMlDHrp-HCmmJgbqS78u-n1R3yA0d3Y9HLEBxZ9V2ivY318do5cXX9bg1Y43wkjSouPr4d9onEIs6srJI2grW9Gjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی ژاپن به ناو هواپیمابر ما حمله کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/funhiphop/79717" target="_blank">📅 16:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79715">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست به نام "بار آخر" منتشر شد.    Spotify   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/funhiphop/79715" target="_blank">📅 16:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79714">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ: دوباره امشب میزنم.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/79714" target="_blank">📅 16:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79713">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست به نام "بار آخر" منتشر شد.    Spotify   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/79713" target="_blank">📅 16:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79712">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست به نام "بار آخر" منتشر شد.    Spotify   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/79712" target="_blank">📅 16:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79711">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhe92pgGtRIPoK2o9shpLAATdZNcicoAqH8Ph2VT62a9GoSirWwYGu9TCfR8TH7YDIrEkj1OqWDTjg-6QfwLL5WVdeg4LsV3uHC1_-hd0JFPD2FhSprc9vhQ5kjg-_xhLOa8Wlktz17zc7M3ZKHLoJ9Rds86CzFrT9Xp3BG-MhjEPIhHzb0HWDSW3MhXTELUgoYGlOROHjIp0fZGMRIola3jV4fcrH3X1MMeIPYMDQwbEwrekD4Jd-Vproq21gAFQ2UuBeOOz43OpwZKfPB06iM1m2KM6ZG_87r08xV6TLU5IZcXDxKeRP--ALvyIJSGMTvlIHfwiKLn_Duoa54KLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هیپهاپولوژیست به نام "بار آخر" منتشر شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/79711" target="_blank">📅 16:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79710">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5fXjpU7dvHehaNrsnqQ-DcTuvv71GAYDh1KfFrr8bXPstuDxoWMm_YJWZQMNgcWy0pvSRQRtKIH9Mrj87AQNa-Zo_G37m-I_EFfFMXikmSnMA8hZ2yFAS9B3258Z5YqIXL-JN6fSMCfbglvn9_r24BeqkuZDCfBwfEnvtO8ngwVCUfOaUCeJ3eEAUpKWZfdS4T-8GSPHBh571zTjz7yL7fRup7fgLt-_bq6LVCLbbmWDxfuzJ319oRMXJVK-elQf9eGS8DnVmAHLpnV7488Ux8ACy-WwOE-RfyN0TzIGKjl9CIF1BH88d0Ue9G5S5E_W2TXHn_TdDSX2yDJq3kQKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی ارتش در بیانیه‌ای اعلام کرد علی معینی، پرسنل واحد نگهداری و تعمیرات نیروی هوایی در پایشگاه ششم شکاری، در حملات شب گذشته آمریکا به بوشهر کشته شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/79710" target="_blank">📅 16:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79709">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">راستی اینجا(شمالغرب) یه ساعت پیش داشت صدا پهپاد میومد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/79709" target="_blank">📅 15:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79708">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qY668lZcIw2CLNzMz9sGk3Ieat9AHawvJ0P7EY4BlqWI9TnhzJ0cmlLrc8MiW6ldalxpWAht0_BDAd9gutkKFROVXYvZsowF_EiZZEpcEm2bpHZvToCHqFzq3mCgRBtbolBJLs74mpL6L8TGl2sdJzuYlJW3ywLrFlQO1uifotod9IyqXkyTLQbqRPOtcKOfNB-aUz3Z7haXzxzofGU3TRp4old2JVBR4GZtxbFu0iM5K5Em2uJBvWLACT3sJkEWk4uni7jsgPaKLefWaX-9dGaaSotxYVkGgbPjm96ZwZrGVpsl6qMuB3zFgPsKdqv9Nj3tMWccWkr_0dJ6TFgTGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمااااااام
😐
😐
😐
(من تروث سوشیال برام بالا نمیاد، لطفا یه نفر چک کنه ببینه اونجا هم گذاشته یا نه)
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/79708" target="_blank">📅 15:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79707">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bbb43a3fb.mp4?token=iB88aTsaOfAciY4vYFl_HR19USb02B5w9TcKnbObHYbAI3o_sErHvRYdOav9a_GaC0jz-evIDc_BPAuJE0JFpQXSKlcKD4XbNqjSiaTrvNz8Zlj1ebFjeg0vQoLGKX6PBXYBHH4sa1cia_08pfTDKWQaFfmwVJptXKPQ0dNN4wyVkeJF5dUYuGcaqV_qwoFYlZTOyq-L6VXMR_rHoiQxPc-niGB0750J9envPgT5sDISSleKYu7Rn2q1kdFv6O6yruHzR9uKUV8HcyuuP9feZQx9szxIb6KyQLvwPAjyRKZksVmSUQJUrqhrg_qTSqTXsMi2dty1I4B6m2wpCdgFNzBd9E8AutVjM7kheKX_7PBT1GSC_HG7huRJcpRul0uOGcowDMTPnchvqOkA7xtm_TWq1OZoDUUjEy3yp99OlUtw_ATTqcX0m7dNEfTZfKE9D8Z9J1XK-Yo1IHNI7DP3q2yH4zfQOdd41u8Z9KjR0Ax2XqsF7gv0Tzd_uVXvA3GKhqCZy0Dc9fXMzqAX___oOyNwcJ63e3TQNQYxjGBvFSzvldk9NPx_hhqAC6RT6Fc6NsydvJqGtvfBCGT6kKpIrA55dBz977cu9TnZRkXrDqXAylpl8orBR35ZE22bNDCIqVVpWoWhFpWGu8X8hrl6Z8evl7WvwdIKoeBddfhIw80" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bbb43a3fb.mp4?token=iB88aTsaOfAciY4vYFl_HR19USb02B5w9TcKnbObHYbAI3o_sErHvRYdOav9a_GaC0jz-evIDc_BPAuJE0JFpQXSKlcKD4XbNqjSiaTrvNz8Zlj1ebFjeg0vQoLGKX6PBXYBHH4sa1cia_08pfTDKWQaFfmwVJptXKPQ0dNN4wyVkeJF5dUYuGcaqV_qwoFYlZTOyq-L6VXMR_rHoiQxPc-niGB0750J9envPgT5sDISSleKYu7Rn2q1kdFv6O6yruHzR9uKUV8HcyuuP9feZQx9szxIb6KyQLvwPAjyRKZksVmSUQJUrqhrg_qTSqTXsMi2dty1I4B6m2wpCdgFNzBd9E8AutVjM7kheKX_7PBT1GSC_HG7huRJcpRul0uOGcowDMTPnchvqOkA7xtm_TWq1OZoDUUjEy3yp99OlUtw_ATTqcX0m7dNEfTZfKE9D8Z9J1XK-Yo1IHNI7DP3q2yH4zfQOdd41u8Z9KjR0Ax2XqsF7gv0Tzd_uVXvA3GKhqCZy0Dc9fXMzqAX___oOyNwcJ63e3TQNQYxjGBvFSzvldk9NPx_hhqAC6RT6Fc6NsydvJqGtvfBCGT6kKpIrA55dBz977cu9TnZRkXrDqXAylpl8orBR35ZE22bNDCIqVVpWoWhFpWGu8X8hrl6Z8evl7WvwdIKoeBddfhIw80" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله‌ی عده‌ای اغتشاشگر و آشوبگر با سنگ و کلمات زشت به دکتر سید عباس عراقچی. تقاضای برخورد با این اعمال زشت و تخریبگران اموال عمومی را داریم. #منم_به_این_مذاکرات_اعتراض_دارم_ولی_الان_بحث_بحث_سویا_و_ذرته #منم_به_این_مذاکرات_اعتراض_دارم_ولی_به_این_مدل_اغتشاش_هم_انتقاد_دارم…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79707" target="_blank">📅 15:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79706">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3gUgacTuCrUPuwAvt75hfjbeJNNK2kTQtLmKH9EYJJRrF7zGiRXOuc8PW0aAbxF_l_G7nk5KTamyEWbxChiZlVhpHIwvmI5k8mto5RdCYsn6dmvrxBBPdH8bKtk3rwOciHzZU3-3zdAOQ3EjTR0OzBUy4dt2oj09HBBGg0EQgdSPUgXvRIJXHG32vnXJ8CfDyISlpFWZv87TzGZirHQ8z0DRNW3bymb0AU_q-r4_vw1Frt-OJgoDf5ckvrGVCLYAWVLZ4wfbvcIKXw1ke3OPn3JV-kGR8sOanfwz8_f8V6YjclQ7ZCkefRiToeGMuWPJmb0Qg5bIizkyYUm0gRRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتما باید مثل نیمار چارتا حرکت نمایشی میزد که یکمم به این توجه کنید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/79706" target="_blank">📅 14:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79705">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ بزودی، به درخواست یانگ آرش ادمین محترم فان هیپ هاپ آتش بس را دوباره برقرار میکنیم و فرصتی دیگر به افراد باهوش در ایران میدهیم.
از توجه شما به این مطالب متشکرم.
پرزیدنت دونالد مادر جی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/79705" target="_blank">📅 14:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79704">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دسخوش  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79704" target="_blank">📅 14:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79703">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvx5TpNr_tn91-xJKmO4T5wib8Fh4tVjw2kU-joHJpcbPbPn3AEsPUadT3IPKia0HeJp_0efgTgn1ZquoDALg2p7GtQy95WVCs-i8LGM1uD9IXwpDz1CzDxGSd0Gi6SlTf9hb4LZa6krSO54Pi8Lkb1OZ42srqhR8eY-RS92MastLhHqvirMucowrPHhSCZAPxO2zYkcRrj45JkxhudbJ5qJHue6UaHrsLtXPXSt8geaPzWHiCRDEEwCaf-o7ChzlZmGRaq2vK9BwbIqfRk-TmfWJo8UaubZfOgt1AHh55zi9XcD5w768ZtXMwFEOb-1nDiBm11kflxcxl4UciJsBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسخوش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79703" target="_blank">📅 14:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79702">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O83PNc2PIVJDi-kDOygEDVe-BCvixB5hNJxV_9tD9JGh7TRcefNlRkohuiiN66tofqOb9mzPi_-RlcLP9IYLMQH0kK4PwtgCtOb5hjSWfml5yAW7KimJ8NRdvAP2Cde8MHcHdlvRMz6ecHw9dYEBFH52a_d5RD7G5NMpY0jRgucUU1UPwK4iMnkmwkMNIBUQuA77oYen44MnziB58fQwKq0tLBH-sX1Z_SKkGNRFAt9Fl06Ac53ML90Sp6Dwcce8vYJJXKpKkq3jaXOlJ-Z5vJlF1Fybj7LK96auYQCPBwoBAJaMg9cx08tJDdydVEFPZgfY5BBRjsaZwsaFO9PkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب ساعت ۴ صب وقتی شما داشتید اخبار میخوندید من داشتم این شاهکار رو میدیدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/79702" target="_blank">📅 13:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79700">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBveTpZGdZfVE4NrNAmYEzD0pG7kqUdxk5FIbZP9-Cu7I2G6yNeaF5JJ0Vqy8IRWDMI0Dl4GOFNYJjWdVIpG2JzAvq2FDNqj_pMTRn1ReCKj-D6MK4zu5fd-drngZJG9SsNQObdG4zqPve3Ts81D5ZApwUOpGQFLe63sOdE-KqAW8PLnHeEdp5ck5L76VvuKhI1kHEELUS_L257OIzRJ7ZRMDA8ScaXEPOVOAm4BB8w5dOvRBJ8yEYMsShr9qADR2ySXXn4v5zcch6F1gBR2j2T1raIVZZh-KdAxVyHs_rjKEnV8d1YSBM-c-M1c5WWAlRlXNStVKYSP5YMXiE-zGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاره شدمممممم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79700" target="_blank">📅 13:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79698">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbb4956b2d.mp4?token=tyZkCxYB-LpoORRXe7vVwgC-pLwmm5lC-Xd-ktZKgpPTGy9bs9hpsuxQMUXVySeSRTCskh15tni0joBlFUeeKRtCG1NnDxHmeBx9FxXCbt1lbfc2EzjxGtHmEtw-wK8PSSe0GQzQJ4LkRTyeRTaLnxNvqUQtZv_W4GY6WnaYTtP27qh-e_AtgWm_ewl0QXVdJlunebACwoPPi7AHCHwJNcYM7F05uCssxAidONjioQNz2aIt7CrxAMHRaydYw3Ry-cpIUP8TbuHH4TdXHTlDoe16Rp_U3wbibpPouwf-VT0jZ9NrbH296N7YJzxfuBeWsuH4hsNfrzT5DVjyDv3AOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbb4956b2d.mp4?token=tyZkCxYB-LpoORRXe7vVwgC-pLwmm5lC-Xd-ktZKgpPTGy9bs9hpsuxQMUXVySeSRTCskh15tni0joBlFUeeKRtCG1NnDxHmeBx9FxXCbt1lbfc2EzjxGtHmEtw-wK8PSSe0GQzQJ4LkRTyeRTaLnxNvqUQtZv_W4GY6WnaYTtP27qh-e_AtgWm_ewl0QXVdJlunebACwoPPi7AHCHwJNcYM7F05uCssxAidONjioQNz2aIt7CrxAMHRaydYw3Ry-cpIUP8TbuHH4TdXHTlDoe16Rp_U3wbibpPouwf-VT0jZ9NrbH296N7YJzxfuBeWsuH4hsNfrzT5DVjyDv3AOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
آتش بس با ایران به نظرم تموم شده!
دیگه هم هیچ علاقه‌ای ندارم باهاشون سر و کار داشته باشم؛ اونا کثافت، مریض، خشن و وحشی هستن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79698" target="_blank">📅 13:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79697">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJ2EIzrRM_22VYCsqq7mfIdyixi2OWQIwmJUdeE37jV824t6U02t7TviImPxLkZC9qL99uIzrLh8YhxkqKcvZRSRRyC9p1R6iLNmTEThzEGCUvRNW42FnBkM65LTnrZ4MFevBoWj3wbLidLCE4N4387-lURiMw7OO1fk484wYymmMV_NSopTe5rTlSticnqmXf8sxPOKi1aViyTEY7RNzHPkxaBSDlc9oQUXT9KvE4B6HiYlxhRIIlNm4c6afhNggW16mAhR6uxeIxDzyHK4Ysv517CQZ_6OcmEd--cxy3Zz4boTgNDu-C6FK3Yww3LDxg9xijlR4PnMUAbqo67PMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حیف شد واقعا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/79697" target="_blank">📅 13:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79696">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ccec9119.mp4?token=DK_QDY8JXhPjlHp7UsP8gyQROceZWoQwDvyin8HaNKvwZOzdwGh78yLwc4YZbHVO6gbtYb4RBljp6FyrQAXBH1rcmRahAMy8ukeh5Bs7fuTl1nsGYi0SbM5e4707-FpY59ATr4Gl1sKaCYfejor8p1UpX-XO_aV9f1HH6VWKbmeWNXmdR7B_KNqUs4nPKWGT8bQRmi9v0ipXrJRP_EYwtUEgpYxoZN0x907TekG-oEj2anPRBVgNWw1N4j1MO8E7zZtf9JWoqTeOZ-XMNQTrvtj8tMpWgGjghE8Gji5J8S3ZUE9MZk9x9euOZ6WMeK2YVZUp9ABN2lZosQ44uH-sxl6s_yHGA8Jgnc1rTaok8DDXPlXOLCUTMNruq7H3rdk65NBKZiT2tEjx0_v85V2pJDh4ngzhdkuItYmUjWtvgCOWUaLePdxhEjc8UKsthqhPHk-wFx0SegytLtVGEMNm-rW2x3Omlr9ISS8MqCKgDaUZV5SfR5KATqQXo5jNuFivCfnxo2ZzGhhkRaOh1LcZ1M6aSJk4iY_pcH-Rw0k1Ek_1W0UiVZeOWmNJGAaYJqLYHd4XXbPm8ILcbVpox402ccdvMEK99CIKpM1Rmek5UfgrolGgqUzHuM52-fHRJ0JuoWqS2a6HhKZLUPOaVYJJgbo-7a3MXGd_caJCLhgz0Jc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ccec9119.mp4?token=DK_QDY8JXhPjlHp7UsP8gyQROceZWoQwDvyin8HaNKvwZOzdwGh78yLwc4YZbHVO6gbtYb4RBljp6FyrQAXBH1rcmRahAMy8ukeh5Bs7fuTl1nsGYi0SbM5e4707-FpY59ATr4Gl1sKaCYfejor8p1UpX-XO_aV9f1HH6VWKbmeWNXmdR7B_KNqUs4nPKWGT8bQRmi9v0ipXrJRP_EYwtUEgpYxoZN0x907TekG-oEj2anPRBVgNWw1N4j1MO8E7zZtf9JWoqTeOZ-XMNQTrvtj8tMpWgGjghE8Gji5J8S3ZUE9MZk9x9euOZ6WMeK2YVZUp9ABN2lZosQ44uH-sxl6s_yHGA8Jgnc1rTaok8DDXPlXOLCUTMNruq7H3rdk65NBKZiT2tEjx0_v85V2pJDh4ngzhdkuItYmUjWtvgCOWUaLePdxhEjc8UKsthqhPHk-wFx0SegytLtVGEMNm-rW2x3Omlr9ISS8MqCKgDaUZV5SfR5KATqQXo5jNuFivCfnxo2ZzGhhkRaOh1LcZ1M6aSJk4iY_pcH-Rw0k1Ek_1W0UiVZeOWmNJGAaYJqLYHd4XXbPm8ILcbVpox402ccdvMEK99CIKpM1Rmek5UfgrolGgqUzHuM52-fHRJ0JuoWqS2a6HhKZLUPOaVYJJgbo-7a3MXGd_caJCLhgz0Jc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
کانال گزارشگر زنده بت‌فوروارد
🎤
⏩
جام‌جهانی ۲۰۲۶ را لحظه‌به‌لحظه دنبال کنید.
⚽️
گل‌ها، نتایج، آمار، ترکیب‌ها، لحظات حساس و مهم‌ترین حواشی مسابقات را به‌صورت زنده در «بت‌فوروارد لایو» دنبال کنید.
● پوشش لحظه‌ای تمامی مسابقات توسط تیم بت‌فوروارد
● همراه با جوایز، برنامه‌های ویژه
● سریع‌تر از همه در جریان مهم‌ترین اتفاقات بزرگ‌ترین رویداد فوتبال جهان قرار بگیرید.
👍
برای ورود به کانال گزارشگر کلیک کنید
کلیک کنید BetForward.com
کلیک کنید BetForward.com
🅰
r17
💻
@BetForwardLive</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/79696" target="_blank">📅 13:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79695">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الاناس که عاصم و شهباز بیان تهران
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79695" target="_blank">📅 12:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79694">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ:
آن‌ها دروغ‌گو، متقلب و بیمار هستند. به مردم خودشان آسیب زده‌اند. تا امروز ۵۴ هزار نفر از معترضان را کشته‌اند.
می‌دانید بعضی‌ها می‌پرسند چرا مردم حکومت را سرنگون نمی‌کنند؟ چون دیگر زنده نیستند؛ آن‌ها را کشته‌اند.
مردم سلاحی ندارند، اما طرف مقابل مسلسل دارد و آن‌ها را به گلوله می‌بندد. رسانه‌ها هم این را پوشش نمی‌دهند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/79694" target="_blank">📅 12:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79693">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اوه اوه ترامپ: این‌ها گروهی از بدترین افراد هستند، من آن‌ها را دوست ندارم. ما وقت زیادی را با آن‌ها تلف کردیم. آن‌ها اصلاً نمی‌دانند چه می‌کنند. آن‌ها مثل سرطان هستند و باید این تومور را هرچه سریع‌تر از بین برد. این احساسی است که امروز دارم. ایرانی‌ها رهبران…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79693" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79692">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اوه اوه ترامپ:
این‌ها گروهی از بدترین افراد هستند، من آن‌ها را دوست ندارم. ما وقت زیادی را با آن‌ها تلف کردیم. آن‌ها اصلاً نمی‌دانند چه می‌کنند.
آن‌ها مثل سرطان هستند و باید این تومور را هرچه سریع‌تر از بین برد. این احساسی است که امروز دارم.
ایرانی‌ها رهبران آمریکایی، از جمله خود من را هدف قرار دادند.
فکر می‌کنم تمام شده است.
نمی‌خواهم با ایرانی‌ها معامله کنم.
ایرانی‌ها دروغ می‌گویند و تقلب می‌کنند.
من دیگر نمی‌خواهم با ایران سروکار داشته باشم. افرادی بیمار بر آن حکومت می‌کنند و از نظر من، این پرونده دیگر تمام شده است.
«از نظر من، تفاهم‌نامه تمام شده است. دیگر نمی‌خواهم با آنها معامله کنم. و اگر سلاح هسته‌ای دارند... دروغگو هستند... به نظر من، ادامه مذاکره با آنها اتلاف وقت است.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79692" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79691">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQ-UOr0RAJbP-3DCOczswVRIlbbPZNuNifRaIPF6AmNGkFqQu9ySlIGy9fANRWFPVO6ejQp_33ibpjN9voW8YR1TlGnjZbu8X-8MLFnYmpqSLC8Q3Hu1GNw4_teeQShfMDXcVDK8oiiucC2cHwoF5QozEIMmTM5qA1HZfkue7oPFHUGAZKJkCb_0TeVBMl_inyydjvmDUMaYds0i0wO5u7qMMuS3ijMK8PQePA2kIbmgd-VqNE2dswuwTqKCMYUAG5JxwtIi4xGl8cqvVN7fcIbyAwYFSei1XHeWw_U68kS10QlGFKmGzH8Bbx864lDv3H8mUaFPHbD2aXews3SLFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب هواداران آرژانتین با نشون دادن پرچم اسرائیل سرمربی مصر رو فشاری کردن
😂
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79691" target="_blank">📅 11:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79690">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fab96f279.mp4?token=cii83K-Wcfl54G5VYUZYETtKMcDYlnd5B4KsMpEhhcoN5wj6tdQYghxSXGA5TMc3Cojk4tboFd9QNaN82sGN7D9N9xVFraR_OWCxPYwO2RBuh4gFi40MwGh3_34djDiau383CUrtyDQ0VQOfPMDhD1uw0zsOyyJAH3Svs6rjJgGFLMyyYt-Y0pk0eHu27Q2bXn8M6JCVymBwVBmQ4oOBrAYZBB83TsweD4Wleh6uH09MIsOUfelNwI0P8tqJGIXtPAvLDgZNDp2SYq-IYPYgTN4W5tx1el7pD7AWnOfjHGfHcZL4jHFDMFQD4KnJOEFP8SMO87VV59QrLzwWHlVKqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fab96f279.mp4?token=cii83K-Wcfl54G5VYUZYETtKMcDYlnd5B4KsMpEhhcoN5wj6tdQYghxSXGA5TMc3Cojk4tboFd9QNaN82sGN7D9N9xVFraR_OWCxPYwO2RBuh4gFi40MwGh3_34djDiau383CUrtyDQ0VQOfPMDhD1uw0zsOyyJAH3Svs6rjJgGFLMyyYt-Y0pk0eHu27Q2bXn8M6JCVymBwVBmQ4oOBrAYZBB83TsweD4Wleh6uH09MIsOUfelNwI0P8tqJGIXtPAvLDgZNDp2SYq-IYPYgTN4W5tx1el7pD7AWnOfjHGfHcZL4jHFDMFQD4KnJOEFP8SMO87VV59QrLzwWHlVKqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر. 3
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79690" target="_blank">📅 06:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79689">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دوباره انفجار و دوباره جنوب کشور.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79689" target="_blank">📅 03:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79688">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حمله‌ی عده‌ای اغتشاشگر و آشوبگر با سنگ و کلمات زشت به دکتر سید عباس عراقچی. تقاضای برخورد با این اعمال زشت و تخریبگران اموال عمومی را داریم. #منم_به_این_مذاکرات_اعتراض_دارم_ولی_الان_بحث_بحث_سویا_و_ذرته #منم_به_این_مذاکرات_اعتراض_دارم_ولی_به_این_مدل_اغتشاش_هم_انتقاد_دارم…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79688" target="_blank">📅 03:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79687">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">در مقابل دوتا کشتی اینهمه اسکله و جزیره یکم اور ریکت نیست؟
@Funhiphop
| Erfan</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79687" target="_blank">📅 02:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79686">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خاورمیانه داره برمیگرده به نسخه پرایمش.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79686" target="_blank">📅 02:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79685">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خاورمیانه داره برمیگرده به نسخه پرایمش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79685" target="_blank">📅 01:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79684">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=Na5Z-eKYoJ03Seg6nEfUZOf1tggXrMPRJ16RqBSHHROPpTjrB4dKSt1MQxXgV9pkHfQD-obDdmgBDY9AvuIIty_yjGGYVerHBkwQfdHAeVPpjBQG-vAcj_LYR_XXd6stYjU8rLJO7LH0HbYewa3ufx1F8L1FnjSjANA4pMa7ucgAOwn9QEjUcuDmBD6qBAGUv_nTeVyZ1TRUKsQinDqXFcyuHKklbdrl_jmQEqUdDi_sKh7jPGkSI1z4k-dAxugCTAaNAiVDarC8uUxi2tHkzeySyD_p5ETTAKK3bZuJn6TNKHKjPRr5cPrIeIbJqKp7jhvTYCQpkJ6y7aaNEItBfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=Na5Z-eKYoJ03Seg6nEfUZOf1tggXrMPRJ16RqBSHHROPpTjrB4dKSt1MQxXgV9pkHfQD-obDdmgBDY9AvuIIty_yjGGYVerHBkwQfdHAeVPpjBQG-vAcj_LYR_XXd6stYjU8rLJO7LH0HbYewa3ufx1F8L1FnjSjANA4pMa7ucgAOwn9QEjUcuDmBD6qBAGUv_nTeVyZ1TRUKsQinDqXFcyuHKklbdrl_jmQEqUdDi_sKh7jPGkSI1z4k-dAxugCTAaNAiVDarC8uUxi2tHkzeySyD_p5ETTAKK3bZuJn6TNKHKjPRr5cPrIeIbJqKp7jhvTYCQpkJ6y7aaNEItBfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط اونجا که یارو میگه خارشه گانوم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79684" target="_blank">📅 01:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79683">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سد مجید بیدار شد
ابوالفضل ناصری، عضو فراکسیون مجلس:
‏ ‏آغاز موج های جدید و بی پایان سپاه
‏تا دقایقی دیگر…!
‏شدیدتر-ویرانگر! ‏
﻿
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79683" target="_blank">📅 01:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79682">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کان نیوز: در آمریکا برای احتمال چند روز نبرد با ایران آماده میشوند؛ این موضوع با کشور های عربی خلیج‌فارس نیز درمیان گذاشته شده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79682" target="_blank">📅 01:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79681">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5fd7843a1.mp4?token=gjRXCHLxSoOETP_12WjJannqpZ2SlICwn-ltjG0o59nXWCmsPA4323v7lzKL7ZwkRZneX3GiY200iViM1r6EismnCjqUcYZdGgOKhBzG2A1t-OuYsHgFZTWDKmSCNRvsB4Cd9thauJ0vTVu5CVQgH-T3NH0LqTIpQQ4A648NlLfi6lOkEsvP-5z3CGSlGtUgnRjBZctkoDRAkUXamI7_272Yb-Xv1_nQPj-LjctI2F7_NH5hiGFj2FBxp6SPmP8Vcqxsr-IWVovXHVaO2l1_1bQTCUbe1PXh2s_LZxEcZk_IU7tI-IUK8IKDna7DiiAQwFeKwYrFIQJCeAyEKv0fpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5fd7843a1.mp4?token=gjRXCHLxSoOETP_12WjJannqpZ2SlICwn-ltjG0o59nXWCmsPA4323v7lzKL7ZwkRZneX3GiY200iViM1r6EismnCjqUcYZdGgOKhBzG2A1t-OuYsHgFZTWDKmSCNRvsB4Cd9thauJ0vTVu5CVQgH-T3NH0LqTIpQQ4A648NlLfi6lOkEsvP-5z3CGSlGtUgnRjBZctkoDRAkUXamI7_272Yb-Xv1_nQPj-LjctI2F7_NH5hiGFj2FBxp6SPmP8Vcqxsr-IWVovXHVaO2l1_1bQTCUbe1PXh2s_LZxEcZk_IU7tI-IUK8IKDna7DiiAQwFeKwYrFIQJCeAyEKv0fpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم دیگه ای از حمله امریکا به بندرعباس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79681" target="_blank">📅 01:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79680">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087708ce6d.mp4?token=teDfDjkVfi1HwmnPj2yL9Mp_sS5-oZypbC7P2_o_4zugxByjvTLpWwxl2FR9cqGLxjGPo_jWFJAJCRSiTDQpACRNHK_wzAaly4ZVMsrbHf-5OipgcFqEfFL10FWqM4WnTDdH9Ku3lGFEMIMaGa2lvyYyRFDYEEHuy_Y1SJXyop1W-n8lQME3O_HklpSqQose9d3-lOiOi5inE5v2UIW11yjJev7Du-G4Uaez9JDUhwfjS778LWEEOeFTKqRgusleL9P9iJOs_9MCgqKYX8CUb4s3LeBhVrYm4Llvh_TzMqwhi4pozmpGLDYO2WpHG0tEdoV_RqQSn9wkrKQ4C34gpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087708ce6d.mp4?token=teDfDjkVfi1HwmnPj2yL9Mp_sS5-oZypbC7P2_o_4zugxByjvTLpWwxl2FR9cqGLxjGPo_jWFJAJCRSiTDQpACRNHK_wzAaly4ZVMsrbHf-5OipgcFqEfFL10FWqM4WnTDdH9Ku3lGFEMIMaGa2lvyYyRFDYEEHuy_Y1SJXyop1W-n8lQME3O_HklpSqQose9d3-lOiOi5inE5v2UIW11yjJev7Du-G4Uaez9JDUhwfjS778LWEEOeFTKqRgusleL9P9iJOs_9MCgqKYX8CUb4s3LeBhVrYm4Llvh_TzMqwhi4pozmpGLDYO2WpHG0tEdoV_RqQSn9wkrKQ4C34gpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا پایان جام‌جهانی ای که پیش بینی میکردن، برای ترامپ حذف شدن آمریکا بود نه فینال
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79680" target="_blank">📅 01:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79679">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قیمت نفت به واسطه ناامن شدن تنگه هرمز دوباره کشید بالا
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/79679" target="_blank">📅 01:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79678">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f8b205f33.mp4?token=ZU1J6cHpa0s6_XzorlTLbgeoHpdSyXmUWQuur10ZWWoBgXuxwP8opiHMQoCBHL3juj_xQUnOUG1zDxgVwTps47jTM-RKf-WGRB_3ACHE_qDF78PVe4PIOBqv6WP_X141Sr8pPpDi6-FUugCmG_I_8Ml-7nV3W5D7SPK2o1J8YDVi883k2725wSE4qYT52qRlcbXihtuyGn22oW2GN3PW_TAZBpYMUD9uDSHJHlgh5Uf1hnOic01_M4YVzezmPwxk1MMQ7V6eU1OjIL68QSBYea6IK6K8D3jonv1XYgzBJfY51r4WxWcnw5nNUcoojN8qsFEHsHEVG-vYZvqnL6la2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f8b205f33.mp4?token=ZU1J6cHpa0s6_XzorlTLbgeoHpdSyXmUWQuur10ZWWoBgXuxwP8opiHMQoCBHL3juj_xQUnOUG1zDxgVwTps47jTM-RKf-WGRB_3ACHE_qDF78PVe4PIOBqv6WP_X141Sr8pPpDi6-FUugCmG_I_8Ml-7nV3W5D7SPK2o1J8YDVi883k2725wSE4qYT52qRlcbXihtuyGn22oW2GN3PW_TAZBpYMUD9uDSHJHlgh5Uf1hnOic01_M4YVzezmPwxk1MMQ7V6eU1OjIL68QSBYea6IK6K8D3jonv1XYgzBJfY51r4WxWcnw5nNUcoojN8qsFEHsHEVG-vYZvqnL6la2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید امریکا به بندرعباس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79678" target="_blank">📅 01:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79677">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سیریک و قشمو باز زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/79677" target="_blank">📅 01:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79676">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تنگه هرمز ارزونیتون، ذرت نمیدیم بهتون.
@FunHipHop
| USA</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79676" target="_blank">📅 01:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79675">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انقدر اسکله زدن که از بندرعباس فقط عباسش مونده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/79675" target="_blank">📅 01:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79674">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این دیگه بخاطر کشتیا نیست
داره حرص حذف شدن از جام جهانیو خالی میکنه
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79674" target="_blank">📅 01:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79673">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سی‌ان‌ان گزارش می‌دهد که حملات نیروهای سنتکام علیه ایران ادامه خواهد داشت.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79673" target="_blank">📅 01:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79672">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فعلا اوضاع ارومه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79672" target="_blank">📅 01:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79671">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آکسیوس:
به گفته مقامات آمریکایی، این حملات به سیستم‌های پدافند هوایی ایران، سامانه‌های نظارتی ساحلی، سامانه‌های موشکی زمین به هوا، پایگاه‌های موشک‌های کروز ضدکشتی، محل‌های پرتاب پهپاد و تاسیسات بندری هدف قرار گرفتند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79671" target="_blank">📅 01:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79670">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وال استریت ژورنال: کشتی های جنگی آمریکا در حالت آماده باش برای احتمال شروع احتمالی محاصره دریایی با دستور ترامپ تا ساعات آینده هستند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79670" target="_blank">📅 01:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79669">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بندر لنگه انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79669" target="_blank">📅 01:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79668">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdbU1nVWbmw2_M24AAfp8DqNSfn5D_JV7l_vu1NNL0ojPg2ZvFMfpa1sLR1xVEDLFk9gLbwCu2QTrCcCC26U4xGN2Diff7xGtMxO8NLlX7C-DUhLZVZxCNfyz-bBQsuYKUifEn92Jb890MsPlVY7Kk5SBCaqwChY9PxY9Y7eTdLQmqKArR-WO3jTAdUeAqwZslLV-0LoQEfvqCozHQ2TtE1BGARhxCk3TgU6_zjKW8hj9T4SJHLgDYbgKjhrm-PafFzI9ofZDirxV9jtMY3byMDwmeeHLxZDCd0pZZhNb1r5VSUCNdb-InFQnG6oo4E67H7l7oXCS87dgZoCD_zfbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوبیا صبحتون بخیر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79668" target="_blank">📅 01:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79666">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c80819d7cf.mp4?token=hKvBrf9RgVsnSp-cYLPsi0v5iBxYqckVgp0xY0h4xPCAzk3zIARBQUhlOzfBxF5SEL8YZfM6SHxjES9nhhtSRo3wI690r__6_yTKhYNX2Y-rGl9LKTLKjEPYxB_DQmmJfZ3Mq9LSfCcNJF1lnhf_f-3NPdRknWgB4CaCkhIJKHNtBwQtdw1A8wSGjrXqTSqP4F41hH2XcBU85eE_R3jIK9QZwn38cJ7_apGoX-X7CR0iVl9XR85_QgJ08bi_MbTrSvAmDUuLUPZrQmI0158mx0Xlbu8YcKsdN1okBcu4LDzNHK25rdFBe7cqZiax_DvipQ7W69PMYgvRs-EpFw9t1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c80819d7cf.mp4?token=hKvBrf9RgVsnSp-cYLPsi0v5iBxYqckVgp0xY0h4xPCAzk3zIARBQUhlOzfBxF5SEL8YZfM6SHxjES9nhhtSRo3wI690r__6_yTKhYNX2Y-rGl9LKTLKjEPYxB_DQmmJfZ3Mq9LSfCcNJF1lnhf_f-3NPdRknWgB4CaCkhIJKHNtBwQtdw1A8wSGjrXqTSqP4F41hH2XcBU85eE_R3jIK9QZwn38cJ7_apGoX-X7CR0iVl9XR85_QgJ08bi_MbTrSvAmDUuLUPZrQmI0158mx0Xlbu8YcKsdN1okBcu4LDzNHK25rdFBe7cqZiax_DvipQ7W69PMYgvRs-EpFw9t1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا کی قراره در ازای ۴ تا کشتی یه زیرساخت پتروشیمی و چنتا رادار شوهر بدیم و آتش بسم برقرار بمونه خدا میدونه</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/79666" target="_blank">📅 01:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79664">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بندرعباس هم زدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/79664" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79663">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سنتکام بیانیه داد که مهم نیس توش میگه اونا زدن مام زدیم اصن هم اتش بس نقض نشده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79663" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79662">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بندرعباس هم زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79662" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79661">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دوباره صدای انفجار از قشم و اطراف روستای تهرویی شهر سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79661" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79660">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سلام فرید جان وقتت بخیر اول بابت برد پروردگار فوتبال حضرت لیونل مسی بهت تبریک میگم دوم اینکه ما قشمیم و صدای انفجار اومد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79660" target="_blank">📅 00:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79659">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اسرائیل هم حزب الله رو انگشت کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79659" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79658">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سلام فریب جان توپی که یامال دیروز شوت کرد همین الان افتاد تو جزیره هنگام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79658" target="_blank">📅 00:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79657">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پایگاه دریایی سپاه تو سیریکو کوبیدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79657" target="_blank">📅 00:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79656">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دوستان نیاز به تعجب نیست، آمریکا خیلی شفاف گفته با خوردن هر یدونه کشتی تو تنگه هرمز یدونه زیرساخت جنوبو میزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79656" target="_blank">📅 00:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79655">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">قشم هم سلام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79655" target="_blank">📅 00:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79654">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">امشب سیریکو میزنن بماند به یادگار  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79654" target="_blank">📅 00:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79653">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmV57226drOldZXPOWzbb9VcsvzhUdPa7pKHT9tneBMQBnxOdP7leI2goflmXgL0df5qgMNRzMUG62OxN0XUCoUuR8W5W7pMDyOdCDjK0hBvACzWDP319BvIZaKyuTKWJ8-9qnQBR74B3-O9CDH2Lu9XQTk25Hgg2HyEaFY5dza-Z3TpuN8pjJw7Gh9xJ3nNr1am7jT3yP8VHDYOhZxItncF1u3i8R7iwqBEO0qZ4dfza3wsNLxM2opYABCb4o7f8livjuxnMhMwYFRcFaoPtzvH0BNRcv11euZpGCnVhX5l1hA57Q55CdOloefK7Q2ngHn3NjCQN_YKsrjB7sTscg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسنپ چت هالند و چک کنید ببینید خایمالی مسیو نکرده</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79653" target="_blank">📅 00:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79652">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLc3aPQUSqv0yPA0Cw_ogYazrT3wAUZe8NvTTDA5buBAKenhDNyw0zfpmq8hutBAqMXP6d0rZlKi4aV-6Y7u8IU4IUEXVQZfHcsXd2wp6RynweqaHodWwIBaceL5tT751kSNK8ShRFq9hL-zHqGDJxjY9clmG2wj9jcJ4TF1U6dGxY7iOIeM58hN5jpHJRrDdqANqFp1o_5WA4o5TjZ2dY5kZlr8LhYYhDOXPk6L7rx2VhgRZmRuBZu9pSTLVDZB8wi5t2MHKLkALFw-FuLHLRpnsZGZOyMFBSnesHwQ_iDCEqtDZxs4EDRegEYHPqAbp5XDfVcj4kg1utbS6BX45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید "پاکار" به نام CML منتشر شد
🟠
SoundCloud
✅
Download</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/79652" target="_blank">📅 00:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79651">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خامس چرا دیگه خوشگل نیست</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79651" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79650">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">زیر این پست آهنگای رندوم بفرستید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79650" target="_blank">📅 23:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79649">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">امروز سپاه 4 تا کشتی رو زد امریکا هم معافیت تحریم نفتیو لغو کرد و یکی از مقاماش گفت که بزودی چند تا سایت نظامیشونو مورد حمله قرار میدیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79649" target="_blank">📅 22:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79647">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cX5ygXl1tpGncKWkxHeqZ8Me6KNaWC4UPE1rMFNt2FuCtZ5XgUWeVRFNYePe41k12sU2-k3_ep7omnW_l9Nx1ZhAjJ2evZVyrxa4jxZFa8-IdOvUuItzxuoxNGHvI139wdSvnQJ9K3qyP-z06JqoRqhufomWlY13KQlYPCnWekmdYxRrxCgRs1Y0d6WX-w34F7vtXcn9TKLjA5NyTGEzeMnrASCU_ulD8uk_mGL4FOG3Eo6M676QCq-xmOt6VGV6c7AZ5IfGClzuRu2HXxTcm1xNNUKvC2CPtZccTbO__5mZyrYCTtty8rCWctk2R_4JJS2ZkB3StP5yQoYos3h7Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ixfa6mHPtOo6qmsmZf-UCt_rzfzKtGeZzPbfma-bBLQBZhQf0_qASE1MqxfcxcwAiYaT2mmeHP5FBDTzBbxdofl9q0R-d7f8gZTdD2ne1TiszJqind5t32gMGhP5zWoWI4BHY481swLqQmv5YO1dOrmYxmnJc-RRBvcFT3gdf3OUSqLs0rkMUS_UfzzD_DA5lsxaNYipcmszHqufAsQOUqnk_0Duw0hDfm5kWQmtxwYC15jiTp3FQI2b7a5qGnxiSdn_pfhEP1OH8vYFa2Kgx2kRuiXFsTcMhNxWrKYUZwWJ7WgzhLGGNJap6KckQe1c2vhi-mMEx4KW0qjtkKhu0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این صحنه چندتا فحش به برونو و نوس تو ذهنتون پلی میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79647" target="_blank">📅 22:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79646">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حالا به رونالدو فنا ربطی نداره ولی بنظرم آرژانتین یا یک چهارم یا نیمه نهایی حذف میشه، خیلی کیرین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79646" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79645">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسرویس رفع محدودیت و کاهش پینگ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mg7YmMBoEI-1WlqCi6Wa4OWqc8NX_VjFvlRbkHc4p2Ki1ZBK7k0k35_0B5WgAK9S5sbCHR9_eClSLENcQWyimeHC_ans9PH23zJz9pM9RB4rEswkp2InxOs6zj0L2BiFKb1iXKY4OlQ6nrb4aHQlUVvEDPEW1hZUiXuyUIfqHmYw8trVrbzJ1ihPApK30rejlGHiD44qCJPi3yq7erb1_J6nNGMTRLCqo-QbSrs62tl3zv91geDo9eA34wT74_4l-JX1KPjWay0eAooWRbj5AVMAaCbsvn2rzitb__rCexr4ctSKj_dqsOGhqZjaLoS-5n56YuCBW7H1yjA83HZ-xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
یه اینترنت پایدار، تفاوتش رو از همون دقیقه اول حس می‌کنی
😎
✅
سرعت بالا
🌎
سرورهای متنوع
🎮
سرورهای Gaming
🛡
اتصال پایدار و امن
🚀
اگر هنوز از هاب شل اشتراک تهیه نکردی، وقتشه تفاوتش رو تجربه کنی.
🤖
خرید آنی از طریق
ربات
🧑‍💻
پشتیبانی تلگرام
@HUBSHELL</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79645" target="_blank">📅 22:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79644">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اسنپ چت هالند و چک کنید ببینید خایمالی مسیو نکرده</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/79644" target="_blank">📅 22:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79643">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝒉𝒔𝒂𝒏</strong></div>
<div class="tg-text">ایران چی میگه؟
😂
سوئیس</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79643" target="_blank">📅 22:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79642">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حریف ارژانتین امشب تو بازی کلمبیا ایران مشخص میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79642" target="_blank">📅 22:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79641">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYM2M5m8JCOiuWQEcGqLruNk1O24lH1LMB1LNtebPlUdCtwMfp10iM0MgkmeM7TL5-6HgYWCf7hGRlWWDMORavYTtXOQzVv24Y_ctl93Z-UbgrgezlBViaCHipvoKPmEbM44IJB_r0CNSJiiXAXC2gWXKJdfOaRgeCZ983DCeZbtRVKv1oTv_jgEx9rbNu_F4g4r3elR1O5ujyXV6s5d1LJxPgVY1hpE3zLssl6Vg-FXFqYrq57i60YZyII-Ya7C2TauKvD6UWzYCZ30_dX1WF7iOpvgbZEyQOAVBtckQge7WXTAd917SwpopQCzbIAOVslr0relva1IVKP-Ghr39Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی روزگار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79641" target="_blank">📅 21:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79640">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ولی دیگه مثل قدیما استرس بازیا مسی رو ندارم، فینال ۲۰۲۲ تا نزدیک سکته رفتم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79640" target="_blank">📅 21:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79639">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آره دوستان، مسی منتظر نمیمونه پاس بدن، خودش پاس میده گل بزنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79639" target="_blank">📅 21:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79638">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LITxH5S4jjid8vG8TnHgQZ6oTNHHM9OJLEJqisxMLKfRs4gdVE4Qd5ZAwiLNeEdgvULtoFfBsC_ECJ3GmpbNCGgZbcrUJIRDUQ1DAT5cIfi632IPIbNDsh2yooOiMdAN2ZN9n7rhtp9rOdBK_JIDIFFkLlRNoJyTjL-JiG8HCqtwaD91VEiyfeFLeETjtYnCVx9pbkP9FcL1HplFDtqRTZsXRC9u6WaJOpAYrL0ArgxpBacBbHUHBMGVTXcqMvsUb9uA2wILcG2NHMcbjtqhNZgGUBhBRKj5x4F9kz-vLvIG0AEY6OKt5yTyrZx5wuoQPXvKbsSHVXUl2c2Q9z6Efw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیبایی خالص
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79638" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79637">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پروردگارم
💙
🤍
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79637" target="_blank">📅 21:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79636">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEXR0aZju2v-hciA3MuRmF75QR6jCUT2MSmhee1VLwWzbrFVTTzO09hWTQeYhXmxtDSUwaVfk1-z1_Ee3XWkq6A8LjmdRVnGwUJ36YylbfAlmA20uZzs0Fi6a_rHkhnSJNBn8wH-xQnb0aWZFDl5HQRm1zvC7098RIv3gu-G5CahfT1SP4ssveivSN2WOFNmLMUWSXqlF3fpSnL2PpVErG2jL3q1PK3qR8B1ehRIluIFYeVQxO7-Z9b14a-DPS9W3DC6QAPzouSY7ocpyjcmNLh2DAWmEynYIuoA-xFoH25QWkcAw61gBShmdLXKgtfTeN8RuZKI6S0Fg_dJHKy8Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی فنای رونالدو رو نا امید نکرد، داره گریه میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79636" target="_blank">📅 21:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79625">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6V6U_G0B5Rq5kaWMKGElzMJ-utCnAHY9gHhe8oYtxgO2ET8UdDGKV9H5XoKqBm5Gy-rI-0TFCuqYLUGjZxO_sjX6NBFn22Qok1B6AZHfTbHdlKdrv22WEU35fVEubIelT5x3Nmw3w2YzjKSlOHxCy6eWnsYof_yGiHHoh3-b3O9jgYPOrA-tJpCiyksT8N0HjrJULdPFQlzDbATTnQf5wed5eaJt251T4NjHVwmFIwcVmaib6-dU2QSUQlGPz1_IIyMpXtqczRsElwUqTz-1jGupHSKyGIKwolY5paWmH2fUXtE9A1rgqyL141vIgVXClE80Lh9091RYxEESOyI3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79625" target="_blank">📅 21:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79622">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">عجب کیری خوردی
😂
😂</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79622" target="_blank">📅 21:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79621">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9531c4e029.mp4?token=TXz56AyOYNmzM4nV-z9Fpc7ep8t9GQDmp_cY-BZ93FGd7URYBOYFialek8ZO5CQ-0XpJwQh9gN5xF-hGNlHvlRym6FluCmu6QQdxYClBhIp2tWLvQBrynpePxFeFAQnGPcXkQ630nnOlfSbiyGdmYSOf6IV9UO3LCrPCHf0ZwmtPh8wAYISGdOVTii-akUJdfxw2i1QoGuM6J4E6TUo8ynGd6jERt-torTm2IwSfDcoNyp-78YcyUYpguLzuDstu3eFJpufgqJrkAqP7yZ-qVRe6BSeqossdG_QUbUm0u_LvJi-ujRAFVCFw5bi-skF0AXlo77-wXStIEZ1j9KztIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9531c4e029.mp4?token=TXz56AyOYNmzM4nV-z9Fpc7ep8t9GQDmp_cY-BZ93FGd7URYBOYFialek8ZO5CQ-0XpJwQh9gN5xF-hGNlHvlRym6FluCmu6QQdxYClBhIp2tWLvQBrynpePxFeFAQnGPcXkQ630nnOlfSbiyGdmYSOf6IV9UO3LCrPCHf0ZwmtPh8wAYISGdOVTii-akUJdfxw2i1QoGuM6J4E6TUo8ynGd6jERt-torTm2IwSfDcoNyp-78YcyUYpguLzuDstu3eFJpufgqJrkAqP7yZ-qVRe6BSeqossdG_QUbUm0u_LvJi-ujRAFVCFw5bi-skF0AXlo77-wXStIEZ1j9KztIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79621" target="_blank">📅 21:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79618">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مصر آورده میگه ببر، صد بار گفتم فقط کیپ ورد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79618" target="_blank">📅 21:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79617">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یه گل یه پاس گل</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79617" target="_blank">📅 21:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79611">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مسیییی</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79611" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79610">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79610" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79607">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">لاشی
امام
حافظ
زیکو
چیزی نیس اسم بازیکنای مصره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79607" target="_blank">📅 21:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79606">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مصر آورده میگه ببر، صد بار گفتم فقط کیپ ورد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79606" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79602">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آرژانتین بخواد اینطوری بازی کنه قطعا حذف میشه</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79602" target="_blank">📅 21:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79598">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3bqlo-qzW_dh0Nw2cPn83Rp6SeInT4EFBGqG7pdI1wOIiBH8bIf1SPLucCWswiR2w4YVz_AuCZN8w8X1ZQuMxA3hPISiS2WqXL4po_sz5OdCZZDOd_4xhotclXKqxaouNBJY-6N7fVtwYnIZhUkfzB5wNFSFj_s26aNFZzk9wlHCUe-qAZMCH9opwNFRZ3ArhPcfw42dx5KzlJv63qkhD8t0BGmvdmfBb8TY82I1TdXClK-WS_0CKWKj1PVEpPWR4Sz-_SqATxO14Eq0jXa_mPcx5lzxmpH5NTekTaEg8C5Jhe_Y0MlLzqoWbEtUE_16F_cHqSgh_BnU31jA4PthQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی تو ادوار جام جهانی 8 تا پنالتی زده که 4 تا رو گل کرده و 4 تا رو خراب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79598" target="_blank">📅 20:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79597">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حوصلم سر رفته بود این گردونه صراف رو زدم، 5 دلار داد
😐
😂
گفتم لینکشو بذارم شما هم بیکارید یه تستی بکنید ببینید چی میده بهتون
👇
https://r.saraf.app/s/agrd042</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79597" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
