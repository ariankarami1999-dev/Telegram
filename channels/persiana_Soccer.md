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
<img src="https://cdn4.telesco.pe/file/mhddfIF3UZKE9MMdSea_W9XeWiN2X-PfYZhxvkIO5zXSVO0j1dOYskuhDb0HvGT6H_pXNGgNHXup8ueXqzWKJQ1eHL2Krx4VP6bjyjXIsMIuRw9fAjnwGYgQGcRLX81TlsJ75MS84c87V_-_rDfhcC0KLfLg-QSlotV7z8El8LuyXhnxM7QI9_XLHs155cLAD-dwZlKby8bV6DxTAm_cTuuGekOe4f1qbk88rejd-vwh6p4Tv7yZ8_YzbxUrGZ1WY2Wps145AhpkBs2xUr_CQcVQl4g3VCtMMrjMBJ9quHNIzkwzgpF4QjDQBq27NJpqpaYnzBkCCGh0Fxy8MBgrvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 513K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 12:02:17</div>
<hr>

<div class="tg-post" id="msg-25920">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuB7Lo870jOcZb50bu1Vo58KumfxWoSD-Yh7kjXx9wQIf6Ga2QV837EKTcL_AnXTUF0idw8CEdc8KUrjtvamdlWhcEPRoZRnGUQo42BKb9tvDStEI2iCBat0tIIoXqg-tu-ORDW4jOdXZOBNUE440HlaVJNocESV4MynO8hTyEimPx4BFgt4bqf4zgLO9LsZgnfhboAA4_0d53fKamZc59NWumCT_HD0hMuXXp0-bPmSS2jTPW9EKOXbd-zrzGIOKBdt7wylimFiuMWyYr0t75VNdTa2V2GjRMBcL5UhwMDrxL-xc4Js5DdCXFRlZULO1ERVLmc2wpriASb8c3_whQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/persiana_Soccer/25920" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25919">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
جلسه اول برنامه تمرینی حرفه ای در خانه برای ساختن یک‌بدن‌خوب؛ این تمرینات برای دوستانیه که بنا به هر دلایل دسترسی به باشگاه ندارند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/25919" target="_blank">📅 11:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25918">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epQydzNd9EDjoDb2RPdC8iHTJ7qhWlUAFyf1n7YK6-1GJYmZiQ4KD2SmSfWjPzS86Ky28bf2TXGOke4Yj7Y4TQybUBiZiYg-66VSy46lwe8r5NeehC1aJACiW5Ma66Qyrnq_Nn_WwjJjmVPwwNAuDWsP8i9QSngNcvHDcr2K5fNo4vzxVk2ZAZoEkjKO4pizW1BGk1wifzYVUrK4jBpFlDmpRhOOzJfliRMxkhw3XbjOBFYHGnaldL3pTi21HfpJHkGbKCuShSuh6IsUH2Sea3VGPGV1GRGtrBA-MftOiP5vPNHUBYr5ioMx32cx96IAjcu2_wIC9Y3uM64qDKkUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در۲۴ساعت‌اخیرسرچِ‌جمله «لغو عضویتِ جانفدا» بیش از ۵۰۰۰ درصدافزایش‌داشته‌و به سرچ اول گوگل تبدیل شده! چی شد اوزگل؟ ترسیدی خجسته؟!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/25918" target="_blank">📅 11:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25917">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/polHdQ935e_pGQv67DLjP14UAZLTUGvokZKJcjn_fNLIziDmoAZg1sDPxKSIxfO2Mc8tSCWIFPDl7PJJTHa_5izIpNd7II_-iR5lqRLiwL7rD8lvnlhF3cAIbkQAHIn84c3iu36qsqZTKbKhgGOKPbHCqzBePngrsg5gxfqmYvaBELDWPV7uauJfmZCUHkDJhITPQP00fIByJrf1x9jk2N-qspE_HSG7SPd5mhBAZC0dOVB-ZDyKZ3uXNElgjT6xNjBxUnvdy1yl4BALOPiTielEn4qyhjAuV9ezpIeGVvHP1gNf6clOGCHTOkUko_qeCO5f755ok5LId3DoJiZdAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/persiana_Soccer/25917" target="_blank">📅 11:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25916">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHaH7sOlZTbg7UGZ68QquuZ2zkymAw6AKGIGIJrT0px1lNU8U77IY17s4_o4LwgaLQpoV4BLtsNS_piiosA0S-UA0X7VD2Ldu61Lz3Soedmm8u3vzhrcMSww41x1o3GQqBFs2vmsM-_RyLmYZmx_bHfcdohyVFmOpa5jIfuuLyTfAX05DBmqhbw7actU6xMvedo0GQewbxqhlmTT7YG-AqXkMzFf9m-GGwDgJ1o6O6luWeXX5Z2M9cKmsX8QNckhlYT2gAspiGN86N7m1p_QCJWwtJvK8w3IuyxdnAOfXgxEhXrKh8hGxbnnSUTkLb5Cl9rnQJ6M-gz8ThAJgVbNGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
عملکرد خیره‌کننده لیونل مسی 39 ساله در هفت مسابقه‌جام‌جهانی2026؛ بجز یه بازی که نمره 7.7 گرفت بقیه بازی‌ها نمرشم بالای 8.0 بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/25916" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25915">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPIX-1M9xIfafJz5sO_zlFDNv2vQ7yOQMozrmPvjEFdGgj2b2wiFypFqmvDbtrT8aOxP3av9TQ6fa2zXY-k6TIOemG7d1ZgPg0wf_8aIP8Om0phXg4aL8CE-TPpvfaP4unQPhL0rTuHjqiYwbWNV_qopfaG5icDx6pYpv-IkfaLBslrC8zlNoV39OtmwraVMShVunAkZ1L_jmVUm5zSEgpCAO_j1mGuKYjN7EPm9Bif5xT5aHrkOeT8c0652aLRRGK0s8agN57TXucsD968wA3ub_f0vbJjmsD4l9HLivk71ZnZIVUq-YQveOGxA_mV8zz204Esn-92Fq6-89CWWmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/25915" target="_blank">📅 10:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25914">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25924a633.mp4?token=i9SYRDD5NySkn1-vIsrrNllPeSZEeT7WvNglD3ssESkxFlAzdJPBYRe7qQ8sQPMxpxVsoJX4ODCzxT-bJTeR8rgpZlku5I6HzLeXBYoxzVGv4MYkYRtNWisSus78iEX6d_L_1Lo83-JHo50dT4PbOMP2z0t2N3ddfIZ56ifeeDmq2vBqOg8ZqOvm0nKeTfyzX0nLZcwPVWEfuSudIYuDv1cEKXMnNgBu3550tO7a9vCGMO_TJPxheDy5jmKE8QjA4la_lM_ge9f9S-aRRnwVQtBQgpkXYu8rrXA7gA0VRriik46KtnT1vDK_uJBh3uWOspyuZjZlaKoXSYZj5bEiWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25924a633.mp4?token=i9SYRDD5NySkn1-vIsrrNllPeSZEeT7WvNglD3ssESkxFlAzdJPBYRe7qQ8sQPMxpxVsoJX4ODCzxT-bJTeR8rgpZlku5I6HzLeXBYoxzVGv4MYkYRtNWisSus78iEX6d_L_1Lo83-JHo50dT4PbOMP2z0t2N3ddfIZ56ifeeDmq2vBqOg8ZqOvm0nKeTfyzX0nLZcwPVWEfuSudIYuDv1cEKXMnNgBu3550tO7a9vCGMO_TJPxheDy5jmKE8QjA4la_lM_ge9f9S-aRRnwVQtBQgpkXYu8rrXA7gA0VRriik46KtnT1vDK_uJBh3uWOspyuZjZlaKoXSYZj5bEiWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضا بیرانوند خودش‌دست‌به‌کار شد و به این شکل مجسمه ژنرال رو در تهران پایه گذاری کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/25914" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25913">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=rPyP6vVenDLlfbkzbKkQytSsZTVhv98nzxOyctHGzySEMGbquIFCXNSq-I_h3efZa_aLrDQwU8KG0r-WpbC1rDEPgCzeeksxLJMTbNJHpWIVMIV4kaQHPkdebAWoPossyNma6tcerINeSz_KoSblv1NSJ-7v5V1Tk_8HkH4PkPER7xGKCzNZ-0nwXUo-E4KrLMy13tLCCLu1O29PPsAxbGzkE6AEmLesbUcrU1Z294ZWunCJSpJfb84RpPi3b8FhbAiyWgIDzGtkfuCroQ9LPbY1k6x-dtaLFCVQGiZd6WLXuG6vs1Mr3DiiW33Y61_OSxB_4bY9F-OG2pgbn7S2L3BXblxB-SCzGYwTY6WLgzVWTE8aat0mAb-MTjhFRjR2xiUZygFr7Gb_5snHNaeX098CPWmH9kVQ6I4iBOGWMxjde3zHAk2pho1QOnipUljaBJpCxJLuv7GJl50GZucQOd6aAhgJkazAaRqQmWrkdy7RfX9LsKr0EzPQfNDBhgP5tNGLHIUb5346txXeDG8pCpzDtrvE3xQsigY03alTkYhhzDvI1IAfzQpH-frjYI800VZGD6uRPulZdVQuvLvF7g1Och0G39rxnRnUG9ikrzd0A7FBiT4YIEzjyjpK1yWzz60XB1aPmCI9OyKmu9zzVPnq-SBMp2A5KfTDXQYjcWc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=rPyP6vVenDLlfbkzbKkQytSsZTVhv98nzxOyctHGzySEMGbquIFCXNSq-I_h3efZa_aLrDQwU8KG0r-WpbC1rDEPgCzeeksxLJMTbNJHpWIVMIV4kaQHPkdebAWoPossyNma6tcerINeSz_KoSblv1NSJ-7v5V1Tk_8HkH4PkPER7xGKCzNZ-0nwXUo-E4KrLMy13tLCCLu1O29PPsAxbGzkE6AEmLesbUcrU1Z294ZWunCJSpJfb84RpPi3b8FhbAiyWgIDzGtkfuCroQ9LPbY1k6x-dtaLFCVQGiZd6WLXuG6vs1Mr3DiiW33Y61_OSxB_4bY9F-OG2pgbn7S2L3BXblxB-SCzGYwTY6WLgzVWTE8aat0mAb-MTjhFRjR2xiUZygFr7Gb_5snHNaeX098CPWmH9kVQ6I4iBOGWMxjde3zHAk2pho1QOnipUljaBJpCxJLuv7GJl50GZucQOd6aAhgJkazAaRqQmWrkdy7RfX9LsKr0EzPQfNDBhgP5tNGLHIUb5346txXeDG8pCpzDtrvE3xQsigY03alTkYhhzDvI1IAfzQpH-frjYI800VZGD6uRPulZdVQuvLvF7g1Och0G39rxnRnUG9ikrzd0A7FBiT4YIEzjyjpK1yWzz60XB1aPmCI9OyKmu9zzVPnq-SBMp2A5KfTDXQYjcWc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تعداد گل و پاس گل‌های کریس رونالدو، لیونل مسی و نیمار جونیور در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/persiana_Soccer/25913" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25912">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY2MKYIAXiuARXdtk7km3z6Q0zFKNOCOyRC62mnSzXsJMzcbLnHmmiuA5v163Xcen_nq4R1SGDLGYnsc2y4mCzFv_J5lYwT4YkpUgOjpsjq-6QPRdKnOGz3z6hwL0If72gT5r2GvNVSRP6szYVu3HVS9IamTitJ_GIbjW_Khft4MVFT0KJlSpcWENeOOfeq2o_Ja8NAcFf5uhuHUezOSGdOyAZKHwbhQ2IY3j1EXcyrNcE3iMnm2wlRLC3F8JCy-4OHt_lDx7t2h45Wa8joHfpALzw32M-rgYJbep2NS59YMoZN5j9_Qz4mUvEPhv4kutVbmzrOURLPYlnT4fJttkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سوپر بونوس
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎲
💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr26
📩
@winro_io</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/25912" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25911">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ficCt0PD-5C9tJRZTes-CL3upWOzzniZonKoLLX77SrgQ7CrSqmq19MeTEsvf3F1sJruMlQmlUDYi2I6loKP_eP8f2J2M7NPWFUKeJ1ZMq6T9TT3SySWqQHEgnmwxq0TsEUVVN_w4Y87WjP4YMG7Blp2SxXY7fHTc78HsMXq8UJOU3EEfrYhcdmFlxTRVlPabVU1lKYkyABCPo1YxFpoLYTi25AIclj7TasEE2bg5QUjc25cDjoTGcYExyPr8a2j0pg4StF24cvsnNRubp6mrFJyAvRkpP5O3-1j35_TAki5M8sTmqYq1hFHPLfHRAZSQFsLSWWW5xuV5TQOpVY3dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/25911" target="_blank">📅 10:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25910">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=RemqubOsOavW61tQqKP766Q4Tg16LksJPAKfY1lg54517rpaNJbLchr5H2uF-_PMzUb9nu_c_UASogcT3dPYK02C3cBfGShSWHMMikT82UzawvNJQVNjy3SrdKRdHcnN_OTXxGhirDs3QTWAI-_hs8JwYMWVrNviA-DjoFpUxmpLMMaiqWJRkVonEchnf3UwiHXgbSDV6F9y2MsZbkU6qsJ2gRrN9SNgLcv3ssaxsoKC7-sOtfjXHIOmf3EmzfWzxVhuISZ9Og0vhMflmJoSs-lITo0XiVn8Z2_3C-el5t6a-pR_QFFFONZk4RK9jZWQbfwGAyT5q9E55E6nxqGVzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=RemqubOsOavW61tQqKP766Q4Tg16LksJPAKfY1lg54517rpaNJbLchr5H2uF-_PMzUb9nu_c_UASogcT3dPYK02C3cBfGShSWHMMikT82UzawvNJQVNjy3SrdKRdHcnN_OTXxGhirDs3QTWAI-_hs8JwYMWVrNviA-DjoFpUxmpLMMaiqWJRkVonEchnf3UwiHXgbSDV6F9y2MsZbkU6qsJ2gRrN9SNgLcv3ssaxsoKC7-sOtfjXHIOmf3EmzfWzxVhuISZ9Og0vhMflmJoSs-lITo0XiVn8Z2_3C-el5t6a-pR_QFFFONZk4RK9jZWQbfwGAyT5q9E55E6nxqGVzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجریه به عمو رشید میگه از فوتبالیست میبودی و‌گل میزدی شادی‌بعدگلت به چه صورت بود؟ ببینید چه حرکتی زد. جمعش‌کردگفت منظورم قلب بوده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/25910" target="_blank">📅 10:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25909">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=e7BA2dlp6XHHlVR3Pu3vmjjQwuBD_xhrG_s6395RdnuHIRCBK0qVqA3M-My27NehISwCbMW5pgqa6Z84pODvISlr0qYuvRecgJbpg6Eadz7laC6ETTso5643BAqg06dHtF20M4TDyO536rYGR8uyEo3fLVpC6AwodV9Gn44Gb3lvvF2WihJIjEXi3Gg5r8XtN0jiqiT_my_yV23F5PBkVseoCpG6cD_y_4T8MZdugj8-eIM-Oo8c8rHhvw11h21xXPuLzX2ekIyg5nI0IcWkvH6y-_GQyPVL4ndSFEVh-d02WH0exBDt9SfiOfLvRMkyQ-uCtSncnaxDU2pwDG3BUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=e7BA2dlp6XHHlVR3Pu3vmjjQwuBD_xhrG_s6395RdnuHIRCBK0qVqA3M-My27NehISwCbMW5pgqa6Z84pODvISlr0qYuvRecgJbpg6Eadz7laC6ETTso5643BAqg06dHtF20M4TDyO536rYGR8uyEo3fLVpC6AwodV9Gn44Gb3lvvF2WihJIjEXi3Gg5r8XtN0jiqiT_my_yV23F5PBkVseoCpG6cD_y_4T8MZdugj8-eIM-Oo8c8rHhvw11h21xXPuLzX2ekIyg5nI0IcWkvH6y-_GQyPVL4ndSFEVh-d02WH0exBDt9SfiOfLvRMkyQ-uCtSncnaxDU2pwDG3BUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/25909" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25908">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=BTKegEayNS-sY-VlkgllDL0j6oqa4BlHxaH_bgMkOwMHkSvyTXL37ucBFwOsveG9x_d5870Jj8vp7f9mLcy-3VbEK1M9eFqZhFtFm6jVwyMQ9szBC5ucUzpn-To0H1JuMOY-7obsSH6f9okh3NA3R2gq6oZa3fun4PL5TC0YM4eCrcf6h1kjilmJucvp9zo3Fl5tXfLuXMaY45IfraUPtFOVGNIR-axOLYdFeCwV-lXPNapzcSaMQJPhjqExD6hSQNkUoqv8fO-kJXF6QaO2oicEgBeW21eHRxxZqJyjQ-lF3HiFjnJklP-OLwfunaNsH_2gv2rMEXnyf-uTdtVKSL5-dEEkBqsa03stfr6lsr5qSAIE232I95-kfR51utB0s4-TNG3V2iSy9iPCPwzZZSBmri3f-W6TArJekP4y3ne6Mj4cyly55UT6kIbjzJWPUnMBfpeZMoXQznN-pAn1N-IQqghQkzgNGdJt9J5IFx79Kxz05hGM7BVCGFGeb1kPK9EwI6XJveLsBGbgfVy16SAbBOd5g_g-5wUYUZSmSG-43r4MvfrpEIHKWbRq0j1v8T9mgCrUJ1GZUSE5WhOZJxvMWdcRtbbxlQsimwOJ62ReON0jHr-t0AOQIJXVCY7TJHdDe3HxyXhDdrlFg9KjbV8AKdZbpZN_MjykGZknRNs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=BTKegEayNS-sY-VlkgllDL0j6oqa4BlHxaH_bgMkOwMHkSvyTXL37ucBFwOsveG9x_d5870Jj8vp7f9mLcy-3VbEK1M9eFqZhFtFm6jVwyMQ9szBC5ucUzpn-To0H1JuMOY-7obsSH6f9okh3NA3R2gq6oZa3fun4PL5TC0YM4eCrcf6h1kjilmJucvp9zo3Fl5tXfLuXMaY45IfraUPtFOVGNIR-axOLYdFeCwV-lXPNapzcSaMQJPhjqExD6hSQNkUoqv8fO-kJXF6QaO2oicEgBeW21eHRxxZqJyjQ-lF3HiFjnJklP-OLwfunaNsH_2gv2rMEXnyf-uTdtVKSL5-dEEkBqsa03stfr6lsr5qSAIE232I95-kfR51utB0s4-TNG3V2iSy9iPCPwzZZSBmri3f-W6TArJekP4y3ne6Mj4cyly55UT6kIbjzJWPUnMBfpeZMoXQznN-pAn1N-IQqghQkzgNGdJt9J5IFx79Kxz05hGM7BVCGFGeb1kPK9EwI6XJveLsBGbgfVy16SAbBOd5g_g-5wUYUZSmSG-43r4MvfrpEIHKWbRq0j1v8T9mgCrUJ1GZUSE5WhOZJxvMWdcRtbbxlQsimwOJ62ReON0jHr-t0AOQIJXVCY7TJHdDe3HxyXhDdrlFg9KjbV8AKdZbpZN_MjykGZknRNs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/25908" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25907">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNaPvHacwpkONmEjfN2bRCaVKumIQEdf9e1u83_jpMATT_27AwNhN4xfRrfesUecteKDdSHczIwZv1U3aoKtR_IwG87eotZqVvuVva0yhvCON7mCwK94GwCoOTF3r6eUnG2o51rBvLZDwwftp7AagcMWIcU6mJSOMK92w8J8CwILnZ2vSYqpXwzP_I_hIaWsDxEtjeWvKPhGZASEYQ8qP1NKkNv4BBCqyHf3sStlqDVlFuSAhtNaeJqHy91wqUyMpOjlGhNiWBiD81aOL9TWZOwunFtZ1zvYncAVvrizWtW72j9tuc-iVCPUJM735CXZ2sSbFKRknGXBeCPXfjY-Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی
؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/25907" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25906">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=lbZGUJ1IE9vrXjDzZ4N-cvmW1YMYNG3jDf0GjoEXv9MI6DNhXcHePSTYt9TDnAJDGelM8rAQFWdK2691YBoSY2Cyz58RO2jnOFH0sR8wPsH9w25konzl-D6nrZRpPqoFuwaMrBxZdl2c018Y6pHtA9H30joHV-VzRiQejSI6m2DclFyve6Z1a3-60LpuD4OqY_kEcdZ3jVFJivYNy049a3TcKW_V9EzEATTK3JP5QIGNjSCv1tV1uUCgkbdY1056ObdfBGGr2exj3AAlFOjk3dlSOvZ-pvcHFEJq8oLCOw3_MGO1Vr1CdPZ2KHGAKpR_sToEw6Ak004y8_JKlYeKUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=lbZGUJ1IE9vrXjDzZ4N-cvmW1YMYNG3jDf0GjoEXv9MI6DNhXcHePSTYt9TDnAJDGelM8rAQFWdK2691YBoSY2Cyz58RO2jnOFH0sR8wPsH9w25konzl-D6nrZRpPqoFuwaMrBxZdl2c018Y6pHtA9H30joHV-VzRiQejSI6m2DclFyve6Z1a3-60LpuD4OqY_kEcdZ3jVFJivYNy049a3TcKW_V9EzEATTK3JP5QIGNjSCv1tV1uUCgkbdY1056ObdfBGGr2exj3AAlFOjk3dlSOvZ-pvcHFEJq8oLCOw3_MGO1Vr1CdPZ2KHGAKpR_sToEw6Ak004y8_JKlYeKUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/25906" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25905">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=KTZhLVcTAPthEMobUczpJo_QlTnYDs3DgYZkmmZhnCW6r_hoGus_mJ_eNxOVaai8IOJjQoiPi0XKwoslY-eJAu1K-J4Jd0fS77DzeUgcO-ttauFRGDa4eB61IntgpZUr6lV8FarZEsQca8Xjjsspznzx26zgzN0K3GHQE8-MhE-d5XAeeANB51q9-I3dLJF5FAb8W1GgJrvRj30nLolNqT2olt7vKMHS11uS3XIOeFm498Y7J5kxzKQMDA0s1333EzXPVTwYaxs4nszkprLhwWW8afH8fFaoefdFbFaBw6kPBzoKMz1PK_ZNy7l8cH-Stv4uIH7sMDYu3FZ7H8niXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=KTZhLVcTAPthEMobUczpJo_QlTnYDs3DgYZkmmZhnCW6r_hoGus_mJ_eNxOVaai8IOJjQoiPi0XKwoslY-eJAu1K-J4Jd0fS77DzeUgcO-ttauFRGDa4eB61IntgpZUr6lV8FarZEsQca8Xjjsspznzx26zgzN0K3GHQE8-MhE-d5XAeeANB51q9-I3dLJF5FAb8W1GgJrvRj30nLolNqT2olt7vKMHS11uS3XIOeFm498Y7J5kxzKQMDA0s1333EzXPVTwYaxs4nszkprLhwWW8afH8fFaoefdFbFaBw6kPBzoKMz1PK_ZNy7l8cH-Stv4uIH7sMDYu3FZ7H8niXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
روایت‌جالب‌ابوطالب‌از تقابل‌حساس و سرنوشت ساز روز یکشنبه هفته پیش‌ رو آرژانتین
🆚
اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/25905" target="_blank">📅 09:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25903">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pPyQIbhUlMw3va5KLg9T68ftGr3921_SruzpP03dz7S1HACfYA2rAiEbh3LV_0shLs0MCb1GSif61-6KMsfUBFrivuv5OZiJAvTekNwSNE8W_GichLX69lViaViUrUKPmvAAXPhbqmeCSSe3qtxEw1h5uNC9bzRk9V49v4DYQD5_HvR1_yAsVLDeqdC4c3b5LqtGgDCCwja4dwKqAdVUyXI0l8HMu6PPAhc7k-KCh7OPpfC-fjhQdsC4GtHWH3TBq9iEAQyVVqcnmK5uIzs5MIVFWh-P_yc0QKpxwTNnFys0uRfpifGC48u6MsolrMjU5WG4HpseL1NrzBReezzwDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O3_RNVqRgLPGZzdF3adMM_9mBb3EMhKQq99700pW8Ac0G_wibCsoIaDLbMt0OcTCB6APF8CA9f_buyUQ4yr97XatakhQNUFvuTyIEoxh6N431vs-BLBti_LOeGc_zdkqEHgo0bVJSlzlEuLyVT05suvvpAP3ToPCKYb2DDA-_jorBekxKaHpL9xKrHT6f9j6txRSTd3pcZ6kKVVdt9q7kI47wj9aURYu9CpPlonSmto0sl58Jibdsi9dV5O826PMtd_3fqak2b88I6-vWSSjEVFAau0-Myo_3pfYsSLTkL7OpwbUw3RLkQJkGcwHR8219NQnDuJ1OLwEoASniLhIXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25903" target="_blank">📅 04:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25902">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCNqxZPG_0Uc8foZxABW9jHZDKdE2nvxaaxGKdpmu2OngD60yua-2fNik_Y0jcDikc2_gfBL28ZxCUqzOtrfh-X1QINeJ0C60rc9Inph4ErbFpvfZxsGYv2P1Axlxl2eU0i918DCNlrIzFo7Sj21ns8asAtumVPwc1Enc3DN3gDNbfMs74bg6cMHPCdk6fuKaA4oti6u35wzT4Tzx3sv-t7IK9FFIh3UUDVIXDXpE61HS-9LBiAr7k_LAuyEW9cvyoSwGsvUuWJM8JqNcw5pdnp_lNe0OY3Zcaw7j_s7xAXamPCYngPg5mx0bgSDABeRDNPZnRt0UZVqc7W61R9x3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های رسانه پرشیانا از سیرجان؛ مدیریت باشگاه‌ پرسپولیس با علیرضا علیزاده هافبک میانی 33 ساله تیم گل‌گهر سیرجان مذاکرات مفصلی داشته و احتمال عقد قرار داد با علیزاده وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25902" target="_blank">📅 02:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25901">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1Z6oWxCPqa26FJ7zd_6zGsGlRjIDoP8KeG3EqimPjhPfPR39a103BhbsMtkI84F0i9JfbZbL4WVW5DBlG98aRWKCexOW_hDCuDVs2ERTz53tGFqyHWtzMHwH3oyn6BJEnKvo0iWfFonNJBGDBD8D475znIPZt2mrleG4-vUexnZg265xk0_fNelhjWxJHAci0bcGBDr_SSSPRJJO0AjR5Ri3mc88aTXYWTj_Jw6w4IUpj2Azn7jCEsZC-qRX-Kq9giSRP58noMEEQlCwaJBznUH0EqvaGMXMY9kWv2LFq6SBWY5OHtsmXKD-QEOpDPwyIjZ36yZPTc_B0IrNR0F-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مجموعه‌ای‌از تمرینات حرفه‌ای شکم و پهلو برای ساختن یک‌سیکس‌پک‌شیک و واقعی؛ چون پست‌های قبلی استقبال‌زیادی‌شد سعی میکنیم هر از گاهی پست های مفید این مدلیم بزاریم که انگیزه‌ای هم بشه برای دوستانی که ورزش نمیکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25901" target="_blank">📅 02:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25900">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En15T6WFDAADPb09wlyLOPy3hluChgq4efIv8E9oi0JKe2g_HQ-u5tx4L5Mn_fMRm2-j3fXrZyQHlmBW1Jqo9iljk0C7883fvhl2rgSucW-tjLLvZ1gmBAhj2ggHRjXKU8mYvxhiV8kdRZrEJHz-9N70N_9mq3ML8JifOmmEkcnxaQlld4fhha6GQQfF1eOfjanOfqj4jVWayxSmBh-uopd9Ys5p4pc8ORGVql_cH-lk5eonjN4RgQHAHkzLhewFnZM21kedr60xEVbRvIbTGxgGGT4fHwzy_b2xDMmXd4Kw1yZlyKftK7Y2h9DQ1yh3H9hq28PLn1fKGBnWJ-KbaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25900" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25899">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TULa37vp4qsL7vTbj15a2hrop8b-4lMX6mLivjo0wCB31gqAbmIAnbkMaQjJIlgO6RK0Gfa1qGAgTkT6SPCnwHdVbm2ggyhLHOnfrRZvfTPo68cy2GQLGU8Awv8DarQIUbcsNuDprxLLTBwBoQAvzcR-REi1kFIpxzycwq7vdVS2am_rmCKf4ZpeSkJnc01ehDr81OHb8swkJ_T_TLujbYC6dLpbapL9326hymtfvKf5ZiS957a_LZZ2Ao4q2wk-RIHTn26qXYcxrrboPfvisPjsJLayvmUQCuSMopY0Ku8hC5por1X3iy_N7msVi6TM5fbJ4qeRqJpI7HGZybGU9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این‌پست‌برای‌رفقایی‌که علاقه دارند بدنسازی کار کنند یا کارمیکند؛ برنامه‌تمرینی برای ساختن یک بدن خوب و قدرتمند؛ سیوش کن و برای رفقات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25899" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25898">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=CgYQUhIICDLHn8-VR7274BwlynJWwVsTefj7H05YI_G8E3F5McMwhcasjO_EZ7TkCbYFhfHxKJXr1bI0OQOIuuKpYaAlL0D0XpjUNdjgGg6kwylTq0kTZYHFNYurMnKg1LI5XiJ5v-X8dzVO73hEiJO5ZSUJ50MCDKRi7XzT8lSpYHApaILqCfD3w-dCulhAy4iYhaxm4D0eNScnamgoFD3VB19AirxMIw34sA0Yi2iVnjn40KyXkN3bzutATM1-oF-ThkRFSMnGX-6EFYIXvHMjJGo03WeQnocC-EL8jpg1uYNddoSG5e9nWASBllVvT3UpccF1TT3AouIwahOqSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=CgYQUhIICDLHn8-VR7274BwlynJWwVsTefj7H05YI_G8E3F5McMwhcasjO_EZ7TkCbYFhfHxKJXr1bI0OQOIuuKpYaAlL0D0XpjUNdjgGg6kwylTq0kTZYHFNYurMnKg1LI5XiJ5v-X8dzVO73hEiJO5ZSUJ50MCDKRi7XzT8lSpYHApaILqCfD3w-dCulhAy4iYhaxm4D0eNScnamgoFD3VB19AirxMIw34sA0Yi2iVnjn40KyXkN3bzutATM1-oF-ThkRFSMnGX-6EFYIXvHMjJGo03WeQnocC-EL8jpg1uYNddoSG5e9nWASBllVvT3UpccF1TT3AouIwahOqSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
دو ویدیو جذاب از خوشجالی هواداران تیم ملی آرژانتین بعد از صعود به فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25898" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25896">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbZTEJOvAve_DeK6MdngYPDoDLCjXNc7a8I6Q5VeXilDKw9jFf7_vvxeeJmDHxGUY-QrRC90btukKsoSMdkp2hYxJiZK_vMgPH99McyBJt8h5Ck-oDHq3xFoWpKuFbksfSZSvSQ0m7IpalAQ6D9QZAPwIs5icZdzrvYp2awmAywz_r8B1G4xm2Czc6Egh0w5QdhhAivDJ2kmzL4dGbMfZTbvCNVV01vD6IxCSTQkBx2Uoat6Duu4GOt2t6P3fL-A1N7-V5MjHgmvSKvkStnluR0ow12-eEM9NkVfvqhgAcSShIqxKEtJnx2hCaCeG4-58u1iykGJZKfTDT-pXYFMTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25896" target="_blank">📅 01:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25895">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAQd_ESjnt1p9FIv1zkWHX-TB8K9os_vTr-KwD_C2-Aa7Bex6LntjKUO9YC2c2HkC4ZIxEgDiCnC9vm8JsDk1b00JBLye3lC5JLkOb34TNUuNx1QfzzdqjCfq4KUPK54tOeBjpxSUQOUJhbpgMuzBfcxdHA7RCpRY7EZXtgr4iyzKaTo816ctPHzm1Nq7PUCRIK2EkPRVYTbz0jBmspnesBl1sU9GYyFWkbXmbqUXe1RBpUu7EF_JJvreSWRLYFRGRODPutcKmkY5clYxG-u0ErrMqWaRDKqGSIfhGN8WaPvqusou7cB5VQYcVbtPUx5KP0QEBqDFFWxwRr-N5n1ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25895" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25894">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-JQPybbvYNRB8yX6MUEbDK9q3p1I1z9k-Suav1DerDtapY00NqEFadKy2Tm7e_2XwIcuLjDSEFVglMzu3TuxxibJNa7EfX4zmaOViJ27_tBALy4nH2RImgh4ada1X7eJHYirHplKT3kg7vWT1fJZrRqXF4hvG2BCzdiZ0m5EnkOskXpoocB3es1JsG6-5_X3TN9O0jfYnamQcV4JqDckihwUZG6jVJfqMG3d9t_dVexh9JkJlXO8jWJhyQQJnWJESclIH4ohZgmzrq9n8qjrNJTMWgExdM7xXRubJTwYvg9oGTTOY6EvnKm8JW0y31uyL0UznVDCf-_ptP4EzAu6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|سامان قدوس، هافبک ایرانی اتحاد کلبا قراردادش را برای ۲ فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25894" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25893">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anm8LmrokRKhiTGpiTAGvyKplRmfhL9SHipoHT6_0hmfXTfEVdwjdcHCDvotxpb06rfyNETVndDXRcZq52D44bnhY3O-eX_qT4goae90YiORGgUMuSZ2a2qD1V8kZ-u16-43-wOIpj7SJ8ST3ikzwPGs0YYyauUbOhMm2vD3XxYSUHYEXskHbV-Sh7MmRxNXQpI3d-eeQdzQtpJTCYLC3ksGTP-4PQVKi5OOcUxiNf6Op-iITs5UhtLTeHNEGxSz-PtqRRtIPht2rp12vPFYbQOVVLkQMxriBDS9SRxwOQfzdudxjmm1MBjMljK3X3cgouuV7fUdMQZDQJM53cZAxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌‌های پرشیانا از مدیریت پرسپولیس؛ نقل‌وانتقالات تیم‌پرسپولیس با جذب چهار بازیکن در پست‌های‌دفاع‌میانی و هافبک میانی به پایان میرسد. دوسوپرایز هم ممکنه داشته باشند که منتظر پاسخ نهایی بازیکن + حل شدن مشکل سربازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/25893" target="_blank">📅 00:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25892">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgJx4pTwn0hZEPrkjLrFgw8EAq_0puVgnZVknh4LU-Su00gtKd7rj0kXdMqbmJH0w7RWQ_mFz_Fbx5PXAoMs1o9TJNRBt3w45EKhtAwA7hJCQCUmkf_FNREqfpEWnj65CfdK9xLRqqbp2HfqoH89gYjh8I3jYLFHNa6wMaOtHzSOq30DqV_UHRUWk2lTObdLC9vzUyzo-Llmc2Qy0QV2ittrp4IEt3b5WyfCb6fVI0UXsCjID2NTClreBkrJlaMh_PakYst7hXhC_2yaj29pls-qfdD6rJ765GE7-yuQJXdnQwbuVqDKdl-LRiCBvAHTA9VSRElxSkma-OZ5_EV_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25892" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25891">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=IXi1rgN4bPOz41qQgIisz7cmBsrB8q25IiA5XfntQKTOaA1kXZo9cXYtTBp_sIWGq1vXQ9B9s35MuSRD0H9sjT5o9s-q_-mbeKImQG5YyKm4cfB9FwgAVotu3vHBkOLYNYHtcy_pKFB6blmLRzceq3E-HR-R1-QrCrdkigdPVj80w8KL1XQeDp2UEpEdzqxgSZ87qFRb9vD6CiwdUeMttBMg4owUZPlPayZctyTYkhAQFEFCHgzEFOCSn1XpSNXcT7kOnls2QBDKN2ts5lE44YfVWtF3WyMq070WbxlZDCmY412CqtLoVwBgxgSVhmQQOmnkcJPvrJ2TPY5aNLrGsG0AewqmIU-uWPIdhv9tvnFMBWAqv0UFT3lTT5oAHU0xOqqD3iAEzVJC4o0fvzPyhi95qY2MEl-ROZRBiSBLjJbYxl53bBG-p4-iY4ykUq7qK3sEED3WSGpYG5rs_d5EYDBi38cHrGz6RN3NjteBeklnddJ6AuuvM-zq8z2A-Kgl2cx8Q8UH0fR52yl0WIGOGyz6GIxjV3TW3ANHUP9dHUFjUr8NIFmSYb3cywznRY1rVcx5WsOqJwxYsrksIw6jR6nMhnZdw72Fsc3lSyCM9C6T-W_Gei3azz30R97Qnv9WeExgSrOkXJjAMT_2wcJLj5tzgfjRaLFYJB9D5AHeYgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=IXi1rgN4bPOz41qQgIisz7cmBsrB8q25IiA5XfntQKTOaA1kXZo9cXYtTBp_sIWGq1vXQ9B9s35MuSRD0H9sjT5o9s-q_-mbeKImQG5YyKm4cfB9FwgAVotu3vHBkOLYNYHtcy_pKFB6blmLRzceq3E-HR-R1-QrCrdkigdPVj80w8KL1XQeDp2UEpEdzqxgSZ87qFRb9vD6CiwdUeMttBMg4owUZPlPayZctyTYkhAQFEFCHgzEFOCSn1XpSNXcT7kOnls2QBDKN2ts5lE44YfVWtF3WyMq070WbxlZDCmY412CqtLoVwBgxgSVhmQQOmnkcJPvrJ2TPY5aNLrGsG0AewqmIU-uWPIdhv9tvnFMBWAqv0UFT3lTT5oAHU0xOqqD3iAEzVJC4o0fvzPyhi95qY2MEl-ROZRBiSBLjJbYxl53bBG-p4-iY4ykUq7qK3sEED3WSGpYG5rs_d5EYDBi38cHrGz6RN3NjteBeklnddJ6AuuvM-zq8z2A-Kgl2cx8Q8UH0fR52yl0WIGOGyz6GIxjV3TW3ANHUP9dHUFjUr8NIFmSYb3cywznRY1rVcx5WsOqJwxYsrksIw6jR6nMhnZdw72Fsc3lSyCM9C6T-W_Gei3azz30R97Qnv9WeExgSrOkXJjAMT_2wcJLj5tzgfjRaLFYJB9D5AHeYgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۷۳۰ سال حقوق یک کارگر، پاداش یک ماه آمریکا گردی و حذف شدن در جام‌جهانی ۴۸ تیمی برای امیر قلعه نویی! ۱۴۰ میلیارد تومان معادل ۷۳۰ سال حقوق یک‌کارگر، پاداش امیر خان قلعه‌ نویی برای حذف در مرحله گروهی‌جام‌جهانی ۴۸ تیمی. ژنرال جان باز بیا بگو خدا با من ناسازگاری…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25891" target="_blank">📅 23:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25890">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUWqcfVnmGl5TwIu7bvbOWDEffMC5uc6wrCcNoOYd9Ou-tYBF5GIN8txhs0okxtCScqEK9v3qzRuzZsJgeyjj7_Wq9O2AYx1AIvERaoACCMrW9sTy8sHF-7PkI2SfkuFPhdPeeNmJ45bmEEPRIRtcvyR3Kj0ArgYP-k5xaTYt7bECc9GvfpbhG2gJLHYdgBZbZO3qj8fBsM7_TqmKFR5roCV0bneVBnAkoLOepyBx1Q16bLiRXpcxAJCsGTvTyXeAkGV3da1THSFlCKmnW8B9Vyfi4SVzJgSul6JIeCbMOW2qVGVGvIO5kLwUfH-Si_2IKrMnO23gmDSJcZS97VEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این پست هم تقدیم به دوستانی که بدنسازی کار میکنن؛ بهترین‌تغذیه‌ها برای قبل و بعدِ تمرین. بفرس برای رفیقت که بدنسازی رو تازه شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25890" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25889">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EF52F6v7MPjLFZEnIFHIyQaYZ47YYdbelVpev4SLClFx-0oMFvnIheMP5F7_ORqmmsu5NbjEyCh6fx-1HKTq7_kuq5_4iMnSJ-LJUnhMmYLHKNDaZ9-VI2F22aeynrM8PTQ8WAm9uYoF2Ais1m3FQvoGfZpA_Aequ0DLTAV6ODQ-_98jceX35uTuRD5JJRW0UscxlbzF49OrbMkfHglF1xtIG6rVBaNtOWCmf3aVe_Qmr1lrMJJXEXHIgddJ1Wu1emZCtepgWj8L6AAZSce3CLADHxgisWFXYjxcBFrlWzuvc_BDpiVAMZc3foe3RISC7xmyQuQGePGaahPDJySIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25889" target="_blank">📅 23:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25888">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=ct038Oi5BZT4Wpt9cjnypK8tR41JfONxCtRDY2SQhhUl1Hp4uiaGhfnfv9z_CfHypONlhE0-uJV3vgBO5NCqax3I55n37zfVC8qSGlR7QuPqmME0Hp2tDEYm2IwlrTY87X3Gj-fi_FuEv5kGyM53nb7WvTB1A-O0B6WJTvKiIGVMFlpNqUtkrT2Z4Y_W8jo8AUtVvMFPXjiQ8NrLNLN9-RDCvEgzFpObw7OzGMyTAsPoJ7Wph9V8aT1Lg3b5UiFQN2FF8yPbB7AY4UL6f8l97nzs076NQu9Z_ytQGgYGC2j5mVM5BL9sRY_A1YFtADC9mSrPQJH_QLNHqyTVjRgRwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=ct038Oi5BZT4Wpt9cjnypK8tR41JfONxCtRDY2SQhhUl1Hp4uiaGhfnfv9z_CfHypONlhE0-uJV3vgBO5NCqax3I55n37zfVC8qSGlR7QuPqmME0Hp2tDEYm2IwlrTY87X3Gj-fi_FuEv5kGyM53nb7WvTB1A-O0B6WJTvKiIGVMFlpNqUtkrT2Z4Y_W8jo8AUtVvMFPXjiQ8NrLNLN9-RDCvEgzFpObw7OzGMyTAsPoJ7Wph9V8aT1Lg3b5UiFQN2FF8yPbB7AY4UL6f8l97nzs076NQu9Z_ytQGgYGC2j5mVM5BL9sRY_A1YFtADC9mSrPQJH_QLNHqyTVjRgRwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌قانون‌نانوشته در تاریخ فوتبال حرفه‌ای و بین بازیکنان باتجربه‌ای که‌حداقل‌یکبار مقابل لیونل مسی بازی کردند وجوددارد که میگه: هیچ وقت نه در قبل از بازی و در نه در جریان بازی با مسی کَل کَل نکنید و اجازه دهید که در جریان مسابقه حل بشود.
‼️
اشتباه‌مهلکی‌که‌برای‌بلینگهام، شماره ۱۰ انگلیس به قیمت از دست‌دادن‌تجربه‌بازی در فینال جام جهانی و یک شکست دیگر انگلیس در مقابل آرژانتین تمام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25888" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25887">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKWegOwoJ4CXCU_tbjfYoXdjRwIJXC-t5SeEDfXthHvkHDfNgJcbZKVGiPRMLXXs7IEbLdfombzBhC0b4Chig34bpzSlC0sqiuGzr__BFr6r7V0nly_g24-YmX3La_If5qU_zafwIKIqTkW7DC7iv6GFBu5U7hyfr06b7ZsyAO2V1J81gVMGt3uQtVQnhrg91WLjlPa242_kZ2MnK7257bnsQBupTWsUAtCdfj_7CJjOocItVWtApeaOusX52FVKNtPUlUy3Yda-hM1EY7XSVy4Xp8RCITJgmAJfXgG9qrmZp-o-WjFtngu0OyHAb0MP0tl4ALF8mVhphnjwd-Vtjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25887" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25886">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=YXV-ChlYQZD7f0jD-GB624jGk_FkVhPaC8H0mc3bT0AB3VC_5BNtm5N6o57KQ6rjTQSEWWJ1wJaGeEGd0l6HoBujwX0c5vVGUWxDUK5pzh2tDdd0JIGUHBJlKrRIUa0ItXxL7VwasO2ERFcW3LZN9m6m7VHcW-4XPfujNQP3NIDPMsmIc3kAi0uluFfhZedP_uf78F1wKt9VP5EW3DoyG_EHricJ9ClEdIh9RjQzHdjHhIuDci8N6GTKOjnb1Ouf2X9kTATAJ_C9ZAGM0fATlLwswZNTdRROC3SIY7Q0diVsJpL54PY-GLkEgy16zI55eMbrUtB7TdyskaUUctow8Q35QJ267obDdfmsBKKHzH4EjFE7ZTG63sQy8c2asPSyPVGzds85FHkzfj4Xk6VGDJ0RxuvSMM1CeCoDesvoC9dgCe3ZXnVU9rVZqVHYPr15dEa6OC8STfe7cUbIa1GvJq3tAn0p_Wh1IWv8VbbXi59UeWhlW_mQNg3atZohKkDplJfB8LkvzqBTDP_eYyBY93iKaNlBo3ZvaPBPr2gxQ9aJx5XJWPre8iVwSM_Ig9dG9MtBtB8w1_XKTKfyUIQ-a39HlTjWArLe37zmZ9dfDv_aVWi5HKQz8eKMAauRapn7FVowO830oRSJG425EiAnL_Vom8Xme5n-_Au-f1UkpF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=YXV-ChlYQZD7f0jD-GB624jGk_FkVhPaC8H0mc3bT0AB3VC_5BNtm5N6o57KQ6rjTQSEWWJ1wJaGeEGd0l6HoBujwX0c5vVGUWxDUK5pzh2tDdd0JIGUHBJlKrRIUa0ItXxL7VwasO2ERFcW3LZN9m6m7VHcW-4XPfujNQP3NIDPMsmIc3kAi0uluFfhZedP_uf78F1wKt9VP5EW3DoyG_EHricJ9ClEdIh9RjQzHdjHhIuDci8N6GTKOjnb1Ouf2X9kTATAJ_C9ZAGM0fATlLwswZNTdRROC3SIY7Q0diVsJpL54PY-GLkEgy16zI55eMbrUtB7TdyskaUUctow8Q35QJ267obDdfmsBKKHzH4EjFE7ZTG63sQy8c2asPSyPVGzds85FHkzfj4Xk6VGDJ0RxuvSMM1CeCoDesvoC9dgCe3ZXnVU9rVZqVHYPr15dEa6OC8STfe7cUbIa1GvJq3tAn0p_Wh1IWv8VbbXi59UeWhlW_mQNg3atZohKkDplJfB8LkvzqBTDP_eYyBY93iKaNlBo3ZvaPBPr2gxQ9aJx5XJWPre8iVwSM_Ig9dG9MtBtB8w1_XKTKfyUIQ-a39HlTjWArLe37zmZ9dfDv_aVWi5HKQz8eKMAauRapn7FVowO830oRSJG425EiAnL_Vom8Xme5n-_Au-f1UkpF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25886" target="_blank">📅 22:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25885">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OO4zHKgpdcAPKgS5ngMBgupqSsSZMk0ma1xikJ-DXD5jY8L5is0W3mMZHt0iVc3i4QgH2zc2wUw3pSmVorl878wRNaO2AjvENnKxgSuw5MW6l4X0T6zIPvwHrQuO_3GGh2MWEhyKNREedYap2SN_eYUognr-SBA06-Mq3EtP8XplO-PnofK1fhcHtamsojKZKYFNat9pTxBHTUyIDfZCgRVsfpkOF4QGgo7Y--L328IPvFkqFKuMmfgpzbEXuk90FTZiW7zrkymyUUpqjOQKkaNLu6VLs26mBVKvgU0wvf-V4JMcK5VPiaPyP0yj2-tzuWZ5-K-278cQmjll_MUfUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25885" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25884">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlD4icmYAlhAAVodz-kQ_bjfJUkOZKsrwr30042FDcXcg21NsYClJmteKEnJHNHIBJAwd3kGQHIq5khxL5lUjhw3W1t-d3qFFqAwlRTSqgz5PpuqjEeXvjokTwM3h60pkj85QRTYJRP_AlwSiBjpK7gYD4vstX5KZX18LaEIBLaEQVfSoDMxrZxM6WEwEL-z7fs_wQIuaGxnrimQ2kMNRtaZR9x7UqdnfAu4MK2IcFiYWW9-mhHfKYnW2MtjItsb78yweOX9vF-uBuMIeDrWjaq-iGIahuOOdxu62hl8OOH-lb2rDko0q4BhyW_1Xs0QV4gpB2HVVhkC_gO_5Z1l-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25884" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25883">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlard4F-Xn_E8N2v_8xeaM4F1C5ISlyF-6a8vuXk7iIAF2k3k5K56F46i1sw592pUxBHkNPdBNCG8-FcWCVeHLQdKQGIU0KmS62cD67OW7ed0LiLbToIoAUZ3qHB-91ixY6prBzy-1WaT8wsSprpBJpLljUAt022KVAIR3vpE8XC2BcRSZ9KQxwBm2Dx09OjvnCk5cRUKxdsBPk5oLPUqsX5uz4Ge2m854mdr3kBg_ZaRyeJYNVwBQ88aKkZGIMEHbYEv20SDSlRWuhsFTvDM8t0E695ZujlX3nJX81fAEhDFNXifBnX-c-sGQwqgaogSKr9cuTgwQosl07McUEGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25883" target="_blank">📅 21:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25882">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=HiKHcTDwwb8K29gaD8am3ARqxwKHZgBkvaCt9J-Ho2efC4dowoq1IXE_WJrfOMPadAMniWvhHHWESwWBAPW5oQ-IBCotuRfX4d31WjqIVz_FhIw1uD4ITGup_Q41D2Z5YVO0T983RYdj91nTiQo5WxlDXdEIRaqWn-NFQRAebuiqxxg-3ZohvNXMAPVSxvpmPKYc2gNxzk21a-LTUoyJj8OfZjZOi591GkbMy4Jnb3gMVG0EK4pZqxB11X0NE33D9M7MgVmnbHSHMcBz3xhx1YUG5AHvmzumc0LOKL9zyc17eA1tI8q4eHLY9Mvo7St-qq3wdYJsNj6akKG3aoJPsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=HiKHcTDwwb8K29gaD8am3ARqxwKHZgBkvaCt9J-Ho2efC4dowoq1IXE_WJrfOMPadAMniWvhHHWESwWBAPW5oQ-IBCotuRfX4d31WjqIVz_FhIw1uD4ITGup_Q41D2Z5YVO0T983RYdj91nTiQo5WxlDXdEIRaqWn-NFQRAebuiqxxg-3ZohvNXMAPVSxvpmPKYc2gNxzk21a-LTUoyJj8OfZjZOi591GkbMy4Jnb3gMVG0EK4pZqxB11X0NE33D9M7MgVmnbHSHMcBz3xhx1YUG5AHvmzumc0LOKL9zyc17eA1tI8q4eHLY9Mvo7St-qq3wdYJsNj6akKG3aoJPsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25882" target="_blank">📅 21:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25881">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESZvkYWNDEFsm4AP0XzcipJ_KWj7-LG3jLd1A2kX9CrfWqiqx4YqXfJ1Qh_YUr7w5F5bGIBt_H9eeMd-bnkL_Wh7ec8pY2qdy_CWeRs52JkjafkAmdK-334kkTzIm9JuKdHxoGHYFtdVh6dE2h1u6MxM02Z41WrCipPaF3D_ByKLnKqhmUKNSNUTdQXfZndAHI31X-c85yqYtbWA1dJRW0_dsFq-M9w7GOmxcwZBYEOyWBOYfduAi71cNtk8z4iQoXaJK5uwIulVeLoq98OkZErL8z7rXFncHZjsMGnkumlt1WVV77ilRzIO47TqjucNxKQrlpd6VO2EY0XtWkfLbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت‌بریتانیاازفیفاخواسته‌بازیکنان‌آرژانتین رو که پس از دیدار باانگلیس بنرهای جزایر فالکلند رو نشون دادن، تحریم‌ومجازات کنه. دولت از فیفا خواسته این بازیکنان رو ازحضور درفینال‌جام‌جهانی محروم کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25881" target="_blank">📅 21:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25880">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uw-0wEMO6p44o2rzBJhc0cValDcD-NwO9j6qaC_-sgxEAGfaQGdZMnkJO--o4b7J1d32lTYyiSZ1TssGDm5ukay1gKrQiNFlEcG7F2-PgSFIVGpDVqMtxqzXINgel4naz7f3H7cvTaR9fLmtGnyZzmOLgIsnknyuhvM5YOZQhd-Z6hKb2Nu2rdsBf6LT7q7Kk_dsOsKBFp8X4n2vaSSWiaCzOHe6qaVS0zJ6-NQtVhwC-lFKZDQ1H1BHced9q16ibiPUp3agVM24xCZYvGoxtxk7AOCXh4jdcHh-ljck3cFnEFmHoNMh0gN9O9rtg8iBbwXc_RP5StGD_qLV29bogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو
؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه که اونم در پست وینگر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25880" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25879">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eItgYnP1AqGJg3-_vYaTuTh5yzFZe5IEW4__FDExbqD7Cubrd7Ue4-WmlQC17okay4WIIdpOX5daJ3TKiTn3jEdNq7iZHveLMtV0uATQnCtjY2AK4FdIcLfd1K7f9IHtmLHnk4TBayJ_I_gS-v3AqXxkC5zvdPoV7imexB_FwiivkdtOWyaunTsndJtQwsZnszuSjD34PueW_Zoj0HJc2e16UbPkJcDjEfPWFlWh0Z1FwGqDJhUVgo7armcxlkGfCmy5pVBSFBQ6Wr-1ZrHtIaFFezWeHrGTPokrR-G_xEC5GvKKlmGUgTxzBTa9UiF7xx1b0Y0aoj1o32ZtBIIjYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عارف غلامی مدافع سابق استقلال: در بهترین فرم بدنی خودم‌هستم‌. میخوام در استقلال بمانم و با هیچ‌باشگاهی‌مذاکره‌ای نکردم و نمیخوام مذاکره کنم‌. ازسهراب‌بختیاری زاده و علی‌تاجرنیا خواهش میکنم که مشکلم رو برطرف کنند تا در استقلال بمانم.
‼️
این درحالیه که بختیار‌ی‌…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25879" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25878">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqM82S0Dn6re_rGzLaQmOYaq2PKWNgcIB5b-GySZLNg4Tbso07Z77WjmT379RyMQxOe1lpPPz4lLsnH4a92ji3pMFacczf6VsaYwvPxECeO853aftEzb2OY4_L4pI04tAqWZm9Gj4P07h3NXsLPRlt496Ii9yVtLQwUuNKJYaqmE42T17aHzW7q2WcxKXkHXnz4dDIFg0n9_XyVyX6GBWA6QosPtYodO_bxKmoPDejthrZ2bER8dizPc4N4rQeTvlFpiIsA7NE38mQ2YylJ3_FR9MuRhCImh_R-yzVIPK9xxyaYQ1aAAXk0juumrNdIH3yAF4iDXaYQXGXZBjKn1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">�
جدیدترین پیش‌بینی Polymarket برای قهرمان جام جهانی ۲۰۲۶
بعد از برد ارژانتين در برابر انگلستان
🇪🇸
اسپانیا:
۵۸.۱٪
🇦🇷
آرژانتین:
۴۱.۹٪
حالا نوبت توئه؛ از داده‌های بازار ایده بگیر و پیش‌بینی خودت رو در
Betegram
ثبت کن.
🎁
۱۰۰٪ بونوس رایگان اولین واریز
⚡
واریز و برداشت سریع
🏆
بهترین ضرایب بازار
👇
همین حالا ثبت‌نام کن:
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/25878" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25877">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=OUR2VXZOYORGT2Ht31dOhSeVCLj1AxUOw_Fhmwz6coVqomQ4nF-pOzkQJRIi_sqcnERF6JxHyrj2nlMFaVsFeyOtbOC25M27T1gKj1S6NTrs5OTaImk4T-fDEUJah9WRliFCTGOBAIAhA6WrwJZEwZYeZsUez4imwUjRzoZjdPJX3SZEy_ZKuEM8dWnzYt6afI-12gi0s2Ef1q9f78Sma4F4J4XxdPLpPv7IvNbLw6afN5hA47eUj8nSmhEORQ6yFsE4heM1FADav6mjfmnIQqBch59sBO1mvik6ZmciaO7nZ89kyxpkkhHgEvhH_IH_6jBHFfFoDWqTSLlQAjELuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=OUR2VXZOYORGT2Ht31dOhSeVCLj1AxUOw_Fhmwz6coVqomQ4nF-pOzkQJRIi_sqcnERF6JxHyrj2nlMFaVsFeyOtbOC25M27T1gKj1S6NTrs5OTaImk4T-fDEUJah9WRliFCTGOBAIAhA6WrwJZEwZYeZsUez4imwUjRzoZjdPJX3SZEy_ZKuEM8dWnzYt6afI-12gi0s2Ef1q9f78Sma4F4J4XxdPLpPv7IvNbLw6afN5hA47eUj8nSmhEORQ6yFsE4heM1FADav6mjfmnIQqBch59sBO1mvik6ZmciaO7nZ89kyxpkkhHgEvhH_IH_6jBHFfFoDWqTSLlQAjELuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز این‌خبری‌که‌این بلاگر آرژانتینی منتشر کرد ممکنه لیونل مسی در فینال گل نزنه و پاس گل بده. پست ریپلای شده رو بخونید. رفقای اخبار +18 رو در کانال دوم میزاریم. دوس داشتین جوین شین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25877" target="_blank">📅 21:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25876">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tf359SrnPcMbNMnzbK-yYMDCvZ9s3v4SNVwnmn4uKDFi7skhMGGtHKVfaHimoV9Ll4nYa07VZy2FssMDpoYQv5cfubFhvSos6TbMRg2e_r5ugZoAI-YipFJxxnkeEfmQDLguwKDRaABPwxsDrNROTbQrIquGzyn3vlYMwzA9eew-2LzWvxxzNlRlrZ8eUVcKzqA01f8H6el9_s6AdLEuvgFGS3ZZ5GYJTITOErcs4xCSm1Rt203BZSOt1jmb9hSpUKXcSo3EdurguDM2VT2mgcWfP7sFCEU4AU1UV0xXkUzCLNevidcKhFY-9OBoZrUrZnvIeeUNayVc4WYy8ht0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پدرو پورو مدافع لاروخا با گلزنی‌ در بازی دیشب به‌رکورد دو گل‌زده رامین رضاییان در این جام رسید؛ تنها 3 مدافع‌راست‌درجام‌جهانی 2026 موفق به ثبت دو گل شده‌اند: پورو، رامین رضاییان و دنیل مونیوز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25876" target="_blank">📅 20:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25875">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2kS-OqDCwga4iA2I_evu88QFhdaIgNBBTLV5XnSKWT9OcDU_XryXe7gQCgsBETo4FYQV7Y3GvvP6U6lHoNTa3X6mvbuYH7igz34kWNb5q5GSg-Mr-92AtroKc79u3smVysQUbhCvC-yDXNMlZffhzIUX3FJ9QyJcDHQm9nm9plICOvEL-nZF6hqGU7BXdDFQOenIWcv9GKq8QSVsGIpVn8-lchyO94ohwPkqc_uRWFLNSeSnxWIHCH5bwZYFb5o2pkYBc65PI8sEaxWXhQA9sIXCNEEbiptvkVPh4IsV5kCXmGwanFKmYZyF7RZ85fFSY8DJVHcPMqrZ70OUE8rvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌های والیبال؛ استارت شاگردان روبرتو پیاتزا در هفته سوم با شکست مقابل اوکراین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25875" target="_blank">📅 20:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25874">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kpg0uvlB4SPhNvcn_FTjx3l6Q2wM9tjdi1DcgaUZ0ouPoS1HKhG5affL0mbqWrIjs4CUTB1fmlnxT5TK3M3mWNgQcwWh3ed14m5nhgYC7Z9mJoqAY3_wcUe5QZHQU_chx2hhDQc_AkvED24oe_T6e49BgQznyHEI4T4pt1gv6rkLKr5GBtjkOgNCVVcI2cZHX55_864Lp67zkEY6vccLpOKVBf8RQUeqc_GjhP-zD4v8_bDOKFURwHdvpxjotDF8HAcm6WdPGxQHueRpsG3Wypqc-Amuf-mz8y767I5cMjVPePm7gMogsDB9d-l6nesvGimtIEzk207cDl_weVfacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25874" target="_blank">📅 20:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25873">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArTkZcuUVIDXX-4BWkP7FHLxUD1qIhFrN0Y5mY5xZ2McE2C_EhLiEGaCTHzg7FdXuJlivYX4GtT49CSYYA5Q4COtj2vnhAYsr3r0tGjex5X7XLVnDeXEh8JJR3icqNIzSlUNSnifEW0xEnprf9YJqOu2A5HCweF2ZL9qpUAZmRnrPlWLAB9K7e_6jIsEG7rSPbXrZWeSNQ5cyYLUhYV1dYEnIDo5XMgIO5rJh2nb7thnuwkKDCFd5xDbAIpAljRaBShy_uqYglY2T06IJEsh9lv_8Po5R8UHQW34KWX8_9DE8WQxAAsIWBMbourh9VaHEqkJ7vQgnVtS0JGjUDGzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیونل‌مسی بخاطر آنتونلا قرارنیست تو فینال گل بزنه؛ این بانوی پاکدامن گفته اگر بازیکنی از آرژانتین درفینال‌جام‌‌‌جهانی‌گل‌بزنه یک شب باهاش میخوابه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25873" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25871">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_JFtDeThjS6eBLbAF5D4dlklL4Jzug1pj7Cm2Eq3J1j-9HyY7vplR3TZzrfwbSLjJfCii1PMlqZ8XrqCB2xOJfqdJvAl2XOsk4UcBZzkLxK0C9OUtcI7-uaFIqWJUpSViULQlIxWBKvTdBdA5NvvxxUweCuho58B0Y65NUylibtoMNZ3gbXgdCk-6AY-9MX029AnMh0zzwT1PqKaHA8Z6d7rkotHV5BJJyq85HesgbzfUC2NZaB5XD0969hKliLsFwfMAyz93Jw15wkuW6gVe4S76sjeXio7OUW2XCR0bzzuyuc-pJX7V4nK6Me-kxjPHnJHUp_ACTR-SViiVMpnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjFhuAenKQM89fzTmSfhmwjlFxnnUWDjiy35sgFHrh38DjSdqHRzzM1xmNQ8Y6NE8QJNnQfZ8x9VBViKhOauOdkX7CY0hdSwHf2huvgSzBRUCzjAtWtahyhccsQtzNYdL3thW1hSzG4nEw8Y-UW-PtGNku5L3iTimikbMZVx4oj2oWVjRQJbxeKi_q8AYeElinh6AkxRE832j8rjhOJOGhANfcJ6TPNvV5QD8FexoDVkVxUF6YCk0h0aT8Horz7vwpDh6wdYqk6IYWPaXJIKLiwg3u6T9SSI7BOQzru87yAFg-wz4VAKqNxoW10jy4WNBPJyJkaeDdYykm9yPLidUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25871" target="_blank">📅 20:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25870">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7Q51dFsqObWHSRbeqtN_a6bYbivquWTq36EV_BZE88cAYdGkJg4cCupzoH9uPTyABQRtesQIZvvM0IpgTbdcUy87cE_6sk9AP-KYREXu_MgNDebw2Esu59xj_4eZRJgGqq3-s1MkfaWVyBu288SYhgpL6fiZlqCZZesnWDgQuEQZ6X5j_q3sePYX8c_NvMea3TSP8T6hPxzSOsi00pZ-qbFSR_4rf6OE8g4A7l_YeRN6FGcGBd0O5DfKbYGkSVH5_DANoXhcequk1ozWA1iLmGs277WYyTzUPpcS0is7ef5vWERNnm-wWgFxD4CgQpAfaDh8l-tysGqAbm6YlHLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25870" target="_blank">📅 20:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25869">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇦🇷
شوروهیجان این زوج مسن آرژانتینی حین بازی دیشب‌ با انگلیس درجام‌جهانی عالی‌بود حتما ببینید. ما هم آرزوی‌ همچین شادی‌جمعی داریم و اینکه فک میکنم اون روززیاددور نیست و نوبت ما هم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25869" target="_blank">📅 19:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25868">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
دور دور ستاره‌ های حذف شده از جام جهانی؛
فقط‌اونجاش‌که‌دیکتاتورامباپه‌دستور داد که هری کین و جود بلینگهام برن تو صندوق ماشین. عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25868" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25867">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=d9BI8maFX827cKl1kfurJAvaX-kT3AYKferLj8xb_g2pqhZfxKLXZu84bLtS70NndT6DCFruVVrKqw5lYPB4fb45XqS1mJykxfgyoOrYS4nHLJqgTk27bAWuPRHSM8mQ7NRzCXTMHXWYQfoNDgEO1BneKzJEomFW4_6saJK36bMHrNr_AV1kzPHwsfpDSgzCbtL0bdd4QSoDEYOk5oSwVtWVw6muiMAlreHJTNBcoCRHRKyQX3cHVuyaJT_rIWNVQidpi-D4TmHv5puzKK7oyQM-6uKXWdX6SheMvqlJjKUrdxg9OtNXMQknahj2PJGquL2GiGF-f46SzGz9tpt6Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=d9BI8maFX827cKl1kfurJAvaX-kT3AYKferLj8xb_g2pqhZfxKLXZu84bLtS70NndT6DCFruVVrKqw5lYPB4fb45XqS1mJykxfgyoOrYS4nHLJqgTk27bAWuPRHSM8mQ7NRzCXTMHXWYQfoNDgEO1BneKzJEomFW4_6saJK36bMHrNr_AV1kzPHwsfpDSgzCbtL0bdd4QSoDEYOk5oSwVtWVw6muiMAlreHJTNBcoCRHRKyQX3cHVuyaJT_rIWNVQidpi-D4TmHv5puzKK7oyQM-6uKXWdX6SheMvqlJjKUrdxg9OtNXMQknahj2PJGquL2GiGF-f46SzGz9tpt6Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دقایقی‌قبل‌بایکی‌از مدیران استقلال تماس گرفتیم و ایشان‌گفت که تا این لحظه هیچ‌گونه نامه و ایمیلی ازسوی‌فیفا و دادگاه عالی ورزش مبنی بررای نهایی پنجره نقل و انتفالات آبی‌ها به ما ارسال نشده. لینک زیر رو داشته باشید فقط نام باشگاه رو سرچ‌کنید اگ تو…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25867" target="_blank">📅 18:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25866">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoPlbqhFqECZq8hx09ERitieaXS7pSaNsoL_MLCGFBMfu1wlaI5AmT0DySCZQ1uTztSHpi5GkbOCvph4Xk664JG3Of__2iKd4KD8yQRpSkabOCwaIYu5_3bR2SvZ2i97afu8pweqDxOTtzrg8Bg4uEa3oRaCxViX55GTPH2DLdA1LaTZKDfxZww7L7STI1s7VV79MKa8_pg4qrhegzarw1Ysz_ERWKuF9JaLWOUO6MXelt4K0k4pwteovhfKQ2tI7-hFJ7JUnvVBXXBBFNFXGVD7v2OPzu4fqIZq-NMzwKUIW-OaV0PXK96G5kUtR7p5mlraxLW20uGBIBboNrRL1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی: ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25866" target="_blank">📅 18:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25865">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv2MjEQTHVNucdUo0fM_-vOTYOutnugm0qdmMqdI4GVDylfNcs-MvpkaJwHEM2hVSInKqcX-Ow20mabh7pUK0ZpNT2vNqKnF7JZ-_ozf76kjwW3r6QU43vLqUqcl_J0m8TbSSLOgdkANXC4csKfynTXSGE4w2tkGjWZtHOUlWRdrdQy0EwgIoVmW-vGSLyhHjCE6i-1XdeT5xYZpzC2mAddMqjJI9NvIp_f0czhelpWO2iy2LLF1JPo5PhgGn1JKJ_oMSkmTd9cdPkpd7zBU9vcLq44Le09Beqaf8_WtD2NL3MTk-Ip8i057FOAtrt7htnXt27Qx2hLM9iQTG79i6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌پیگیری‌های‌پرشیانااز مدیریت استقلال: وکیل ایتالیایی باشگاه استقلال به علی تاجرنیا اعلام کرده که دادگاه عالی ورزش CAS تاپایان امشب رای‌ نهایی خود را در باره پرونده آبی‌ها خواهد داد. طبق گفته خودِ وکیل احتمال باز شدن پنجره آبی‌ها زیاده. این صحبتی که خودِ…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25865" target="_blank">📅 18:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25864">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpZlYrGSPXmzxUemkMHD0mvjBC3J-zlrpBculJ1asBANbNVp4n2qO5ok_8RIITfZC1xrCI4dUPIUwPEwdl72kYWvTwbFZmODO_aa8TUCeKAJyd6Nei0gvcsVI4EMWEUUq2wZEBdUX6f0pLePa31cGezEszEJ3xsvMRLs_2dcMOoAb04JdSsJEC3S-bnZbmghC1BoZoC0a-otYTE5EvhhY6CpBIv892fccaT4yb3SZWsICHL5y0VFxzPqa5dvPp4I8nloJNEmMtlYG006WmjcqZOllfSWaYyvFmnuVmuq5o4pSlBuxn8Mechlqc2q9o43ZrgRJ9TqQWP2SwcUSyBFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25864" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25863">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=OIzd_qy9IT9qzXW7ddyZpTz4GNPxjHtQ2FYUwTTc_vkFfdmNAj79sBZB39UMnRSIFLnK2yws5BkW5jKd3bq4Wpkyfem-qh_6aHI8S_9pybnrYmaoC9eQuCxFUi4Idwj8V0Lhh8yRm5pjq3c0XYc1O8dhRg-LEdgprwP_ZeL3WLwtl5Stg62dObgWWiXZVxnBcy2aOUyVeUbQFWGtaojUdAKHuG_WWoQRU74kBhJSOx_S4cWQ61zbseu0mn9RsATPB8r2JunlhGnwRaDyjvu3-0n3h9aEJhqboNuBtHtXWsqfpuXzIU3PzwqO42YasMhXUnVv0M5CYHbdRdUJV20Uwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=OIzd_qy9IT9qzXW7ddyZpTz4GNPxjHtQ2FYUwTTc_vkFfdmNAj79sBZB39UMnRSIFLnK2yws5BkW5jKd3bq4Wpkyfem-qh_6aHI8S_9pybnrYmaoC9eQuCxFUi4Idwj8V0Lhh8yRm5pjq3c0XYc1O8dhRg-LEdgprwP_ZeL3WLwtl5Stg62dObgWWiXZVxnBcy2aOUyVeUbQFWGtaojUdAKHuG_WWoQRU74kBhJSOx_S4cWQ61zbseu0mn9RsATPB8r2JunlhGnwRaDyjvu3-0n3h9aEJhqboNuBtHtXWsqfpuXzIU3PzwqO42YasMhXUnVv0M5CYHbdRdUJV20Uwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25863" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25862">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC329C4PkdJ9QJsIzVxeAkbY3G4bDjkeV4lTQjo8f0garbB5q-NrTIIv3zRtTD517qOZbwQY3TMpSIHfVfwjSmFj0lwxHEnXm4lTlDW6b3-1mWcSxic_sstlp_Opb4qY6MF_BvQeF1R9scfzVmOrKFKX3lcOtDiZoEN88Rk78OniyZxaFBsgkXobsGIp9D6rCTks71NWfGuq1ZcVXZGO_JJ442xCN6UqEkvpFSr4qslGMK0_QT9t9HH9c36LcMztyR8cCazzwj1KcPyxsdt-VIukppWDpM4WmKNwR9RRIcHYdI6yULUeBf-R1femigkjQEYc5brvOeO9wrW47clm3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ تو ۸۸ سال اخیر هیچ سرمربی نتونسته از عنوان قهرمانی خودش تو جام جهانی دفاع کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25862" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25860">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlQnAIy5QRMl8YdKYdvnfvFfcgoPIDbCW3z7aX_iPC9ubuT43uOzRVmB9SSMNNQomVNfswXysmO65vyS_57tL-uOOWu4A7gj_RFZeMk-2n53vp5CYg-aDDiupGS5RD6E3WReU91S_N7kgpxPcNk0FNdiXP4tzkBBFPCEr440lp8KpKRt3ocouf5gaGuAhir-_DZTZRrJ5ygG-XuSochTYo1oUD3NNKkdMILBeVKR_SVFEVEnew4rShjAxKwVb-gMeSehDd4wD7M-wEX2ZBUSwHvRkWkrt1ObLQO6OLSwtZ-38gkIlOF2thrak6UswXTZbyRwgNcaWaWl33R3f2CYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25860" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25859">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orT5BhV9JypTjcXI7rC_nm83Fp16pv9ugnVK4993wz5vz1MTkywzhDuHH0Gn3fIsUoEDt8Ri0O2tDguSi5iVBY0_tiPyl7lgB5P8jwtHeaHSA5oecBml3TFScN3telQ-ZIrymp6viIJvHUYI2fLc40Wnacq0bEMrvwh4okHy1i7tSP6BnVJzOjLpLHzAPdF4awFEACnlAOTAAQNqQ7NfCtYmY1XQIrMzR5H5tR1zgFHMgAXPMUVB4kV48WlOn8vNJzgcDM-3A4aQ_VrljZC252ltwiRHEo0s448XpNzhiw8uFTQTBc0-hbV0wnTIUvgwr7H3dWNS0omI0zx6v8zGqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
جادوگری و هرنمایی لیونل مسی 39 ساله برابرستارگان‌انگلیس؛ این صحنه از بازی دیشب بود که یه لحظه کرک و پرم ریخت که چجوری نتونست چهار نفری توپ دو از این پیرمرد دوست داشتنی بگیرند. تهش هم مجبور شدن روش خطا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25859" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25858">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLwk_Nx67jgfhr9aPurVZE2HJj_tt9a73xYuy5mp4Q_OzAuoWdd7YTlXlsbfQTpnQKHYmoZxSRY8Xqou08bTRf43weL4kwtB94OEz-v_cjG21pepC8MKy4tLgMZ4bk2kzNYYu2m_2K5Z58EDI45hJL3PkvpcWAFi4TDX_LVU9fPmmnZ2THIII11npRgEcIjJz6HSJmXfEymm4MHCF1EfDCk0-PfqjCUQrFqhEQrnQjsskK-Tgs2ovOeMW0QhWnEnvL_JWwMwa9boc-jFfgwCMMxRnr3Pcd7Fwq96ROtMW_Gi1C_KLb8zulRjbkLrXZ1D8JWruMpY2Z4lx3jHojZdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25858" target="_blank">📅 16:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25857">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ai_D3IGFnDtHKHNClyayj23kdjSSdUAoCv3-s8ydNx2Fq9pi9GVxVixnCU3TBUgqSXqSKEZmZ_k6-oGjnxIJFWZ09ywBvVYhYSQSlnvV-GeVbG4RH6-KQFutcRT3Rk4_GsrYe7mg1REmm1fnSAxJR3kIgJMZRHBftibBqQboYmNd4_P7K7-n9_OnJkltrsKKdU7RjRYKzd3u1HeDWw1zt4L3ynm5jLnlQ9CqCTsQ51iixBVK30aaL5R5fsWnOjsU3EPZpSyh7N2vwEFGtFFl9yB6uQ82oQ5Cbv2PHagaDmmUCNBMLmyg-wNL5PvN5xFUp1zZCNQR4tCtbr1pab-pNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25857" target="_blank">📅 16:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25856">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOnxfhVRZODyRfRhUpR2rFKhSVLGTiEmvl63cYh5k0HdmcYBcdelx-XWoEwp-MRKZv3aWhq1-_MMcF40fmCYYrF6Vw_8Ku-azJGz-XpSswe1yKWGuXbD9_QVryiLw-h5Q97RL8ESG0SW7Bvlrl-6aJVnonYZg-7P0hpwc-STtokGAdSjvKYFvMOuhXuUpFDEueDdF9NW9dxKGKW76WoBKbnvyWYVsj83O3OA9A4wAt1AZneNxdAHRRZrUgZp7lTVPEjhVnlDUjjhflPqfoS5YsSSfHROuD1gpg0smMmSABFEMNpqFz2g7NrwyLlq74rqjyaE6vPAUfr7BQbpIJSUgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25856" target="_blank">📅 16:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25855">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4hXJ_W-HuuvSMsOCcQ4huBfch6dtOjRy8ZIc0l8V6NKB5pHOWFbkyHBHphe3ioUTI7_HUJwIULrSLtg1Ojul2x0wIyF4q0KdGFLPP4r2QBEk1eOl8kC_FVUPZIF74ryiJAFVwbB8PHch320XLaZFwc-DbMeUw5S8yNTYxPypPD83Bw8QVu460wveY5HqP5lj4_MZUVgXjj6k62QOGiadr4Alxj-jmLRGrPxF_0ishVlL1RJcGFlALhEjq24u0pxzWtPIGw2216-ciDkui6V8O6dC8rWHOxchBkpAS1lru6FSMtSpuTeUlcGv9_lRjG4V0yKFrw27dXh5bEDagbKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
دریک رپر‌ معروف‌‌آمریکایی‌در دیدار با کریس رونالدو به او اعلام‌کرده‌روی قهرمانی تیم ملی پرتغال درجام جهانی مبلغ 5 میلیون یورو شرط بسته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25855" target="_blank">📅 15:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25854">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxDbIbChLS4Mx_M2DCgkppf09HnysYWA1TcyMkMteYZucWSxRupYEMyUqoXJ0I7z8rlUNRlyHeK_FMJ0CQ3qkxXeSlMxh7d2-JHHBjri8vcRASOuV9WkSu4rCDhAdZh-cKWOzrPKJHUu0g9Bw-97xy5vNadxcKIacHZkaAjjFy-ZI-l2K2plmMxJ1aN-F8xu-oK6dkx_z589sP84I47mdbakyxyM-q5B1cZXyLnyjmAFkMR24k9KfA7Rs0iTx1SWJburaUuTq80yd4fwq1OI3r2bC6D2XvGnSVFYVIEwagpdJVy1wPzJuWI7xzclrpIIN3NASdq3BjwsB0Phmh3eVkeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxDbIbChLS4Mx_M2DCgkppf09HnysYWA1TcyMkMteYZucWSxRupYEMyUqoXJ0I7z8rlUNRlyHeK_FMJ0CQ3qkxXeSlMxh7d2-JHHBjri8vcRASOuV9WkSu4rCDhAdZh-cKWOzrPKJHUu0g9Bw-97xy5vNadxcKIacHZkaAjjFy-ZI-l2K2plmMxJ1aN-F8xu-oK6dkx_z589sP84I47mdbakyxyM-q5B1cZXyLnyjmAFkMR24k9KfA7Rs0iTx1SWJburaUuTq80yd4fwq1OI3r2bC6D2XvGnSVFYVIEwagpdJVy1wPzJuWI7xzclrpIIN3NASdq3BjwsB0Phmh3eVkeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25854" target="_blank">📅 15:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25853">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkdD15MIsvbkgB-Mq_rQtT9JTWb6tjooCAvNy-RGtYaWYcaet6uqfP1c4HAW8WD5tq39_mzq6hII7qUD458jHDxeq1QLnwrXS6pTaKfF7MeLwPCSOuTi5okK9H_feQ5Rjek_y4u7QMWAYa9yNSv2MrFOiNCVWIty3BUtkE-6KiH5pznUAUd35KZzU6j45FhrXlb9D5-UrhyxXiO0bsH6T2RHdUwSQBlf4FY9btMV-lSDQJpSKP9X0vCazpIi_g7mI6zAGy6rvJ1sUaIQnyHqhj5xy1nCd2IxI7XmKsAen9CbuE6-z2w8foU5QYzTcDmgfVOAh2QKzI8vNkyWFe_KvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#فوری؛ اکثر خبر گزاری‌ های معتبر خارجی خبر از قضاوت علیرضا فعانی اسطوره داوری فوتبال ایران دربازی‌فینال‌جام‌جهانی 2026 بین تیم‌های ملی اسپانیا
🆚
آرژانتین میدن. امیدوارم‌نخوره‌تو ذوقمون وفیفا هم به زودی پوستر رسمی اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25853" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25852">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kjeg933ARNNzgP0JXC_rjXw8aTAH7q0Ci32-IwUIfqFpIkjEHVn8EWHk5UKOsyDBcwodYuUeEQnbQdMsL7jkIJm-4eYbAS2TXxKHXkMYHT-If6uVckBeFM0MVTKcp4ASQY1NyRhT4SsMNI4414yTs38qb0iT4j98XnwsU9KGgPbiEnpMIwrGGK1QHF05uFPyn7lik_mrcZBY9HT7282sfqwVbanoofwtEKAaIL6SUqEXcA0Dzy80JNgt4V_Kus62SJJImlo1Ui1Wjc--fcEc1tGz6oc47XUEaybvzo2KSJ0mj1nYeTXPlP9OiO3QGViKT5GqeWjXflshFUjtSWzFwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوریا پور علی هافبک سابق تراکتور و گل‌گهر باعقدقراردادی دوساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25852" target="_blank">📅 14:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25851">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIGhCEYurPjWJypDYEYp5dZpnuUp6ScZ5sVyzVX1Em3Kd5DPJonMlEfi1FFjg784O2xL3CaqDCj0dGIg0RdjRrdDHjK0kiuNKGO_Z35NXqhnTo-zelnr6wqs8HYRHLcNExWo9r00Q9y1e5nN_T7WAFzS3pf7g9pTkFNm_lmU6r025EqvmZLBnFiPU1pfKyosti02i52FsE2pqTRJvI0zSNE9jDzGEr3C5qaRU66Zq81zaNW3BkFkkQLH-c_FynwYLDcYlbEPQcV54JFeyuetrDon4NvkI4ozriHPTed8ewReWsp50wTO4RDr2dReYnf6QaNjEbJJpsHvBgtGsZAEfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25851" target="_blank">📅 14:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25850">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rumEVDGwY5BykwSmAhTFUbNWZe_OIUDBoeLYLZ-jTrx7Gcys5hFty_QyvT488ZgqlodSNcu4HVjTg2z1u0HL7wGO3tJ4AZI8HN1nH-sH5nydDkI6E9Fal34mSMmLWT5mAoFofq8mjLMJVptxcG0_N1L1CXJL-JCi7j9rWIdgqZRnkbjbDSwAhA3cZJAAv3xICJvn9FqvEtTmAnOhFFvJQzu-O_XxW0gZeCtdAFfe4Jn34R286VEkcMIenVjnIuEh2iBBXk8tFLHXHFuz0Sm50uONw05oxxaTMZHvBtxZJnxUMK-tzVqEL7_60_21R4NZkS7xrn4neUmH_LcBGHMt6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25850" target="_blank">📅 14:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25849">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNHRcdNzHUzQo_heopm7RLYzf-JDuIS5WVeSzQ5ZO4rObc5n1xn3nagHHYyVLLKIVtycfDIAKp-BMx1Dws584B0ErPiRaN5ZqwPJBgWvOv6gYu_c51NOoOU_L7At7aoJ-RPHlFUZey8qA7tpUG2RXHA74PjULNmr2wBcQSP_NHoSF9y0vf50v2o-afidDnZWScPfITO-nuMxj15AoSW5IAAP-S9xDFwthjmxCQOKCbXiDZhjqaAXJuxZO0zdKjSpnHdKX4CH67sGW7RfmgPG4oXGrqk7H4HT-9PfqA_VZPhkNSHO_0fIZuPjirjZQB_faa6H-2d1ikdEkO5zLQmeBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25849" target="_blank">📅 13:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25848">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiILj1TebE0YM1MOHr7rqLsd8YYrU_8MWBgxa72kzne35zP_c2kf6c0d4AZW4Z_aMdy2vqPzuHFw8dGbsHWR0KjVxIi-D30-ve7y4NQ5grtozHemORd0J7qsi1UkyiXRUp7DiyDHMApaVGaT7bjknRtZchGIu5yCt0D8PXMLuW3cHLer5BDcnccTXWrVYDN8q21bL7oimnqVS_AWUNUGq3yxDQM2VY33W_bTSVLJKSa8bEkcwuLY94CeX1qUoUqmBtecbKZDWKfc4ybc37vcGrWcQRmkwkVGhDTTKfKPM2XvVtanbSvAWqBkKZr8W-8QkTiV0P1xcSdl1_pZLp5gzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار سرمربی پرسپولیس امروز عصر جلسه‌ای‌سه‌ساعت بصورت ویدیو کال با مهدی زارع داشته و بالاخره او رو مجاب کرده که به آفر باشگاه پرسپولیس پاسخ‌مثبت بدهد. مهدی زارع به‌تارتار اعلام‌کرده رضایت‌نامه‌ام رو بگیرید می‌آیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25848" target="_blank">📅 13:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25847">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6RlFXlCYAW34ScvkP1q1HJHql9Pq-dDNU9P5kC6P3qcYDs1ocIw9wkoXd5v97_VAtNCKULuWfddGa060m-0rkkIDgCHl6qgDI2H-n7oZhr8IQQAn2nAWJh40DNQI7iDsizgbv7WtskBdYjM12pWWZ-Um9vdUgfjT6xVe3WVj4z-JCW_OmxSZzpV3IzXIRdWAH2QgeJPTP5mUFzzYkUbI9HjJmiUUUL_SiAhPuMC_U-HKJSOTKPFbE5pyJQ6pTntJIO9lx4llnc0k0WuqpfU26L9-Hoac8b2CFpg3h-dx_wG2TUGBxXI0mSL04CaNAgBxmmVrOYOnaJ7Eo8rYgpPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25847" target="_blank">📅 13:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25846">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuIhD8bHAiNHSSZUj_NlitL_Lz02w8IT7iga1wY0GYcGMDVcswOA9OfR3VLkw6jDp6mHJUPrsnRYA1mx3RLbdvuz1xM1-jcIFmlEwzEVFqZlDqT_huQP3ylSbgq8owikQVeTaS1TRARg1UHaErNjzqJW1Cc_bkRGQpiOH4S7B6TKiKTJgTT0Nx_mqJOf43-tJPVFykPibR7c-05HplMInrnBFokpv7gRMpK35X8Thr5ngFYAeOV4LCifWWGM31FwwaXdZZVK8RkIgSG2Dz3uCW-nDzDt7a45Fs-_m679zao9U6s1TitAWrc-H22gEH8UduDbOtxilYtbfOVEWeIiIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
‏دلیل موفقیت‌اسپانیا مشخص شد! نهار قبل از هر بازی آنها را یک سرآشپز ایرانی برای بازیکنان تیم ملی اسپانیا کباب کوبیده، جوجه و چنجه درست میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25846" target="_blank">📅 13:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25845">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=CSrJbidmvJc7jOo2GRG0DETZSIrRsAMbYjVSLl4gKhSnwfNGbeXXvFOrz1uIjtOMXa0EOStU31fUxNOmRCUiR5w_CjcK05lDo12yCZwEV3Oha-j1qMPULnJxgdxifJGWr-RAZmU_oleh25taS7iFtoj61m1pWU_3EXFfU16v4dk8seWn08P8tg-0v2jMQC2Q-8M8KO7IuJe6Y-S5H6PFR5ehpnfzn0rnzRXkWtnOp2KY_7bS2OoMj_XPk9nRTXMfNvx13tcqrKXfkSHdoWNWYkhLS_aBsKqrU6BrxI0U5PdlbKQwd9pzj3-CH1KqGF70I-2rBxlI-ihGLesLJ6L8ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=CSrJbidmvJc7jOo2GRG0DETZSIrRsAMbYjVSLl4gKhSnwfNGbeXXvFOrz1uIjtOMXa0EOStU31fUxNOmRCUiR5w_CjcK05lDo12yCZwEV3Oha-j1qMPULnJxgdxifJGWr-RAZmU_oleh25taS7iFtoj61m1pWU_3EXFfU16v4dk8seWn08P8tg-0v2jMQC2Q-8M8KO7IuJe6Y-S5H6PFR5ehpnfzn0rnzRXkWtnOp2KY_7bS2OoMj_XPk9nRTXMfNvx13tcqrKXfkSHdoWNWYkhLS_aBsKqrU6BrxI0U5PdlbKQwd9pzj3-CH1KqGF70I-2rBxlI-ihGLesLJ6L8ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇪🇸
تصور کنید توی اوج هیجان و استرس فینال جام‌جهانی‌بین‌ تیم‌های آرژانتین و اسپانیا؛ نتیجه بازی دو-دو مساویه و بازیکن ها رفتن برای استراحت بین دو نیمه؛
همون لحظه بیژن مرتضوی وسط زمین:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25845" target="_blank">📅 13:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25844">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQ-rwi79TU57k-nz2_B3MiM1GB1Z1X7fZcLjPYX4fJs-1EMfqfy5dWd7GlcqNldqqzW-k1HTMQwCua1oHyqBH-Iz5mE7pMeGJdarKx4rlUgNIA2BRa7U6CPLW4j6Scf8LZG5LBmBmMQV2urdyzc9eA5OOV2pHwaXzZ5bkrPTOsgeJmiluqgDHkLx4gEibW1cFTGay293PODryfqIcP0555ae6GU839DqyBPlQpuHC-5qRYMj93fiVNsr6S3oj9ibIWKB6ECdeCQDQxED9R8cFKIx8_iCt9QO6NjBqNhcStczA7SkGtcWX6_aFw4oW7kvwcWe1JCdzN6YM4Ec2vSZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25844" target="_blank">📅 13:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25843">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=ldvVtKYgvYvYciaz4WsZbSEdz4joF0JjUlC-294LTyJ196UnTmZPF75f3juWPHgLO_6-Qw-PgrPHpkg5Pd-m6gxFJH4EQIE-B-tMk2Key0IKaXw890IC4F9_0DRfDyCBUaC2S5hZUd929ZlLF5KnYUa-uD0NX-PrGreF6SZbpgkGIycDHKg1Jan-o_AtBYAh975kYFNIiJ8bzBWNLBgVojz1YBX4x1EVRTuabR8QL2W9x2Xeq5bpnZebIETtwhyiyti9GuLis6QzhlfVCb9XgJBQCvzuVnx3AgyVlNtaF5G1-3vti7bgKDG8uCqZB_goOESFvzkf1IEI6d_AyNPXe0x9t25VKKZ9FMO_YHn_k4CCKG6b3k1SJn9mTzbimetpOXfKp33E6qR820LErcSJRCytaRIgR32l6qsf2SwNdzj6CCG5eNTXQ1jTMn5kEF1GZUA17iy_6vtPfAYHpoh5ev69dE0SDTvp9SdCRDG2XsJXZ6p8H2nFhgqc_6aGh1DBorJZYPJsodVO3silWpKYjJtw0sJlm7bXYoiCYoqtgnJFxo6LO4r4EL9NadXYlUdo6znxTNuVI-CxFg6oAfdEOYDXfe6njVj2W_SBxv5Om6oAEL7FNLgoDGYt1vPZESqs95HvsCD8H8XobdUhQb6qm6CryIdGHKNC-Jl8tEZH2lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=ldvVtKYgvYvYciaz4WsZbSEdz4joF0JjUlC-294LTyJ196UnTmZPF75f3juWPHgLO_6-Qw-PgrPHpkg5Pd-m6gxFJH4EQIE-B-tMk2Key0IKaXw890IC4F9_0DRfDyCBUaC2S5hZUd929ZlLF5KnYUa-uD0NX-PrGreF6SZbpgkGIycDHKg1Jan-o_AtBYAh975kYFNIiJ8bzBWNLBgVojz1YBX4x1EVRTuabR8QL2W9x2Xeq5bpnZebIETtwhyiyti9GuLis6QzhlfVCb9XgJBQCvzuVnx3AgyVlNtaF5G1-3vti7bgKDG8uCqZB_goOESFvzkf1IEI6d_AyNPXe0x9t25VKKZ9FMO_YHn_k4CCKG6b3k1SJn9mTzbimetpOXfKp33E6qR820LErcSJRCytaRIgR32l6qsf2SwNdzj6CCG5eNTXQ1jTMn5kEF1GZUA17iy_6vtPfAYHpoh5ev69dE0SDTvp9SdCRDG2XsJXZ6p8H2nFhgqc_6aGh1DBorJZYPJsodVO3silWpKYjJtw0sJlm7bXYoiCYoqtgnJFxo6LO4r4EL9NadXYlUdo6znxTNuVI-CxFg6oAfdEOYDXfe6njVj2W_SBxv5Om6oAEL7FNLgoDGYt1vPZESqs95HvsCD8H8XobdUhQb6qm6CryIdGHKNC-Jl8tEZH2lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#تکمیلی؛ بازیکنان آرژانتین بعداز بازی بطری آب جردن پیکفورد پیدا کردند؛ بطری‌ ای که روش نوشته شده هر بازیکن حریف پنالتی‌ به کدوم سمت میزنه.
‼️
خنده‌های‌انزو که‌مقابل اسمش‌نوشته شده بود که “وسط بایست”یعنی پنالتی‌رو به‌وسط دروازه می‌زنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25843" target="_blank">📅 12:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25842">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nm3xTju0jthahOAlnbasp4nOYVzuG9Kfc2quKvWnoeWzJssblwvdy1IGcUyov8-Yt-3SPRocXBtnyMq50c3BufpPeSbEr91RveSEpP_UDzfAbTjh6KwS3SOYw6ba-kFG5v_bKQpl6Le6_UEQ9AbzBDXo5EBB_IOCgOVB5v75KsI94QXI3pP02SnrF3a16UMrASGbAHa0xBPJX91ERrAbuaEffppwvE9WUEKvYeoRVwdZZrQQ6_vYmPxwWSBt01Rty0JiLipXALxvKvIlnVEhpbyL52sLGYkRssgvVYW5R6aGr9bqtwMSbE9CnmuNEHRt9qcU5C_K1JOX1eFvhYVVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25842" target="_blank">📅 12:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25841">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeU85scRUck8Gu6zP3Bfl6BqgyDNCN93CSd5OjsjpqDTxf6xDCIEwPZ3OLoppbBwKaYClugg_rQk0O1IyQKtKjRWfIJjtLK_J3BoWOCM-Gq4hmdnQUj5a-Evitfbuxzs1hx49sD1c9VyhH9HeklTgqQ3CB-AmZvrMGUmez2kzr2KYBTqliEN-W5TTsicXoWg78JkOu29dWFUpgWJoE48vustaZKf0xjxvewQeZLBb72eM8o6vnWHZxr8FK-xfjOCM66kgcs1h81VY_rsDYXGh09mJhnfNgAKGXZbTsApdecbaTmsp5ejQbY5G46Hl95Tm_cpb7QKn4rJwZvUjvB1OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25841" target="_blank">📅 12:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25840">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ov4YUcEGJp4nvQ6Ery7OdQW7naJNyPjLl1mEZsjyMGufKV0zvSqt0GszH8yTf97_AXYmeeCl1bAGTlKbXs_BbTA_cgMe7jOCpXQF_9VUc0bGcyX5iCXd19It8qabYP4Ffr4vou57GedxpsGseAgXRcd0eo8FU54HDCT_ZB62WDChLLVppVrBjatX9sSu1MpZn5aSkfBxDUo5VULcPbg6a5u2VmTKANqLHC2KDCe51_bhibQCjsyMgyfnW9o4vIs5xt5w5LbgnipDJgmsV1pTiD1zfPjsgGLwYlWxs4ffuqJ0_-YYEnxstb13H0_juXXfiADjrCXlRbaVIGYQVb55ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25840" target="_blank">📅 12:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25839">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8168388efd.mp4?token=amItO_M1mHubDd1hpWVLCM3zpzXlx6Y89NZ7VInC5-EW51yxP66_sk1bIplGUt3e4EzpydPvHoSOOGPPEnOWIpwnGp3ZNCkXQKLjPsihClhVNPEhLS58QCYR33csJcCVEW5H-UtaltZKC5nSPXK1DB7jlOXSz7T-LSU2l9_XRLqDZ0P4y-FqMoqRCMiq6Ob1bFlclJA4dIFvapHRs1WrheKtmmZiTQLTAMccD4QwG63nM10ibVGjGPJ2Id8yar35YjJbl3uH-lbF6b5eopWvbN6F6lyi8_4ccnogpTyr1zZg8_SBHmzJ92Jxr1O37RiFmy3fRpOIQ0ueFcs0-5N5PzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8168388efd.mp4?token=amItO_M1mHubDd1hpWVLCM3zpzXlx6Y89NZ7VInC5-EW51yxP66_sk1bIplGUt3e4EzpydPvHoSOOGPPEnOWIpwnGp3ZNCkXQKLjPsihClhVNPEhLS58QCYR33csJcCVEW5H-UtaltZKC5nSPXK1DB7jlOXSz7T-LSU2l9_XRLqDZ0P4y-FqMoqRCMiq6Ob1bFlclJA4dIFvapHRs1WrheKtmmZiTQLTAMccD4QwG63nM10ibVGjGPJ2Id8yar35YjJbl3uH-lbF6b5eopWvbN6F6lyi8_4ccnogpTyr1zZg8_SBHmzJ92Jxr1O37RiFmy3fRpOIQ0ueFcs0-5N5PzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شش پاس گل تاریخی و حساس لیونل مسی در شش جام جهانی که در ان حضور داشته رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25839" target="_blank">📅 11:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25838">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KP5QLCK9Eo-89ENZcqdYmOHD0olbQkRT14wKj7UG2w4831hw2bulabZjLmvnLgGaiovM7CrkXOBKi3e2NdMVevTHsrdnb-qLE0Yrm3I7NfEYT3qQSInrvOFeJ6qcvIrbSSiOxpUSBl0Ie55aCos2iLLR0MbYEw6wIKP9rxNwRUfC6r_dKQ1Aku8uVqnjcw2ND7fyABTaY7JR4K1XuObiHlQpOspzDhUfFdBVEaCervxIFCYyf44R-cxPECZlVfUTauH3FCurR0Z18aiK2UikUccA2YmpPusEfcfdW_K9BycaaXhz6DkTo7ajR32Ykt2cvN-qFoReVf8Ml32zyx43ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25838" target="_blank">📅 11:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25837">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇦🇷
شادی‌کارمندان‌خبرگزاری آرژانتینی در طول بازی با انگلیس؛ دولت آرژانتین گفته اگه قهرمان بشیم یک هفته تعطیلی رسمی در کشور اعلام خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25837" target="_blank">📅 10:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25836">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=m0LJ8dggSBovkyxpzpynBHF1EoNCS5dtyzL2C4DH8ISA_SWCjoNEJQ0mXTBV5EJ_Dmxikb8URTzSzDWP5DLu6tqSIUIohNXWCW8vuI03cKTc3dxjtIlqf63p0nOCuVm_B1Ah3zwn5mq1QMd0Ye4q0C2abQE1IdWX_qfCioDj3y9FKY5O77ci8LjEVtmJTm1MvTX0IBlBSAFKGQCpLfYPXrdYpyoBPJHxhl0SqGCeycS7b-PYStKGRaySUNIrr6rl9xZYa2ZR5rejg4tgEcgc5knFWijGgsb1MapH7b-sq_FZELyl2zf4joFMH6c_Y8AZiVc8lHyscvwfDZn8QS8i0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=m0LJ8dggSBovkyxpzpynBHF1EoNCS5dtyzL2C4DH8ISA_SWCjoNEJQ0mXTBV5EJ_Dmxikb8URTzSzDWP5DLu6tqSIUIohNXWCW8vuI03cKTc3dxjtIlqf63p0nOCuVm_B1Ah3zwn5mq1QMd0Ye4q0C2abQE1IdWX_qfCioDj3y9FKY5O77ci8LjEVtmJTm1MvTX0IBlBSAFKGQCpLfYPXrdYpyoBPJHxhl0SqGCeycS7b-PYStKGRaySUNIrr6rl9xZYa2ZR5rejg4tgEcgc5knFWijGgsb1MapH7b-sq_FZELyl2zf4joFMH6c_Y8AZiVc8lHyscvwfDZn8QS8i0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌توویژه‌برنامه دیشب جام جهانی پدر تشریفات‌ایران رواورده میگه تو دیت اول چیکار کنیم طرف خوشش بیاد و مخش طرف رو بزنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25836" target="_blank">📅 10:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25835">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsuoVr5x3NQJAUJZ19JLVxLphD1wnYf38EsvbLKwu67Ex7UeCnXrUgUcvIFTC7JVku47TSWB0zasqqlN7wP5dWYEHsYLh5AAblo5RGRBfsDJBlhakduQNIKkO4kAHgWNCLrXbuI_j7PI5_EwITOCrqQpBNnnkzVGVV7rKX3K8d3dnxqp7Ox_VQm9LQ-b9QUJXHCoTZ-XFLNicFPc3RE6tS3UvwI9655nS68ZEU2SvH0MmCLbD1LiVMTiLVSknLmaz7peN7ZWleGYswVWFXu8SpoHXOYOie7RgchO6BlR6LMGeOfeRUQUqLyOhLuKmXTt5G7ahB0eoyKjSCWde2GOJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درآمد تیم‌های ایرانی از جام جهانی
2026
🔵
استقلال: ۱.۱۶ میلیون دلار
🔴
پرسپولیس: ۱.۰۶ میلیون دلار
🔴
تراکتور تبریز: ۸۸۰ هزار دلار
🟡
سپاهان اصفهان: ۵۲۵ هزار دلار
🟠
فولاد خوزستان: ۱۷۵ هزار دلار
🟢
ذوب‌آهن اصفهان: ۱۷۵ هزار دلار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25835" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25834">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=PAz8QJXc7Z-vJELANlGCUrrNay5_aKYdxptioAOjpuCiev1bTdExo3nVDEZDI3u3zFYwbYNHP4ULegCl8CeRHjp9QErnQRcCTqtNdFQmMsJjsOAtTyvlkoOXEoo_zJwCPhH12mmUS1EkESF_6-QpPrnurdYOlpoPIK76tM6qNYKNkGlh-EYtyfvsCkhNOgNU_SEuX4h3oaowgZsO-1exhnidKBgJjfPIwxsfimn6Hz3_VDa9BnrjRBRJ4SqmpTnm0ZFPZhPbGxN3Z4T7pxVlYUiZQ2RqaQjC65WHiuani9R5vDxtDecxg-hv3GQRhcMXSVu56k0MWr8f3re4Df8dyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=PAz8QJXc7Z-vJELANlGCUrrNay5_aKYdxptioAOjpuCiev1bTdExo3nVDEZDI3u3zFYwbYNHP4ULegCl8CeRHjp9QErnQRcCTqtNdFQmMsJjsOAtTyvlkoOXEoo_zJwCPhH12mmUS1EkESF_6-QpPrnurdYOlpoPIK76tM6qNYKNkGlh-EYtyfvsCkhNOgNU_SEuX4h3oaowgZsO-1exhnidKBgJjfPIwxsfimn6Hz3_VDa9BnrjRBRJ4SqmpTnm0ZFPZhPbGxN3Z4T7pxVlYUiZQ2RqaQjC65WHiuani9R5vDxtDecxg-hv3GQRhcMXSVu56k0MWr8f3re4Df8dyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25834" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25833">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=F3ZriTarckNoJHLGF1BsEg9pNNlZK6qLKk0uIaZ7BLFpXt5rGoE4dtlOBtGxWlRpldBGQMX8vU08OPZicWhfO67fJnYytAOw2uIe1hnXfMnIJsd1ZpY_eKb0q6X0AsU6V7iK54jpl1AdGqca90TPNGxcx719yP5m81lO-l5DoHhPbOpNfDrGX2G-aWY0q_SHdoNqm4-SitpuWwewAWqFkuP864Q-Os3eSPyZSC1GgigeEr-0LPivCRGNfhoF8yz4U1n7QObqdsTotD3AjGgHjj9IGLStZrJlB7QMPXpl3K8ksDgpmn5sV1LEqgoGBErIgb4Z4jmyqiSFpi4bBM1glQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=F3ZriTarckNoJHLGF1BsEg9pNNlZK6qLKk0uIaZ7BLFpXt5rGoE4dtlOBtGxWlRpldBGQMX8vU08OPZicWhfO67fJnYytAOw2uIe1hnXfMnIJsd1ZpY_eKb0q6X0AsU6V7iK54jpl1AdGqca90TPNGxcx719yP5m81lO-l5DoHhPbOpNfDrGX2G-aWY0q_SHdoNqm4-SitpuWwewAWqFkuP864Q-Os3eSPyZSC1GgigeEr-0LPivCRGNfhoF8yz4U1n7QObqdsTotD3AjGgHjj9IGLStZrJlB7QMPXpl3K8ksDgpmn5sV1LEqgoGBErIgb4Z4jmyqiSFpi4bBM1glQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25833" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25831">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQAUh56XAVS7AHG2SdWb4yinTNoFzkHbXeOwcjdHS-6vRUMYoG96evWOCc8KxyQe9MkuWTw8GbB8qe0j_w0LEcWNl26bP2ZJzX7lOJ61qIKIpCpAwFjM3UmS7WWKFs05wgR6Xc7mps02PBxXQ1jk1vK17U1hZXm_9FCFCZidber4xPkKX7PsWq8q81RGAELH66dxe8TbN6Lu4wxENgwup0eDfl45V8tICwQDrWvll60Plby9cvjLQdVwkSITvQaIlbsBIb69C6rKRl0l8ZrLhW2ikZxfLQoq5AS4npryGAwzhz3yDtDtHSOE5kCeWluM7YvyuIWWPZf1mMZ_KTNO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌مسی‌داره باخودش‌فک‌میکنه که کاش همونجا تو تشت خفش میکردم که الان برا خودم آدم نشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25831" target="_blank">📅 10:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25830">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25830" target="_blank">📅 09:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25828">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOmivcLzE-41VOTXUQlll3Z-TmtlwIP-rfeK4XoEGKXDTVFXXf2NroYXCPaHkPk7FHoY6AvNBtT-9dI5YlPBO5aYOeXfCh1i-iPLjcFjUdzbL_ATJ4hXV5smYJzDowX9RHaXo3lbp_Qww8Kh0xpdYMmlRQ6LUDdBASF_Xc_u5tK1H-FK8-17ym5Zzg5QE9Kh59YJGIeh5LjFNKv8WuiUKRuNADv67sclA15PGqiH0bfN170KPbw2coblSJf4ZM3-oAztoEqArPD7PzD17p2IoVjpLAW5rm5pwCX6Iluz_4xasGIuHSQ2B1iAUoBnwbO_0YRaC3jRkfNsHYSm_oAE6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5vxW_T3Y9kqSAPKjrKmkb7YLSJuN9s79wV02REEaryOndNSWqkECRtE3ao6xKmaF0tBo_B0UXv0ka4kd5KB1e4jshaDfiiNpsxansFQLJuTlsqXYPO1VMfM1m4J5lgJ_7dLeT3CqXBdNxLnyXdPWFehlU6-foOBO4F_lOjmYjddrFw804vX7GwRv_5Z0EPxvtRvisJihdcdPrF3qTf5jJJ1sd45VaItLDQ2X_Z4ZkZnR6bFFS7X-dPLtX8X-zCKPC5WufoePyIzKkAiYKu7hb_3-DNlsgvzs8jzvjYkQ__1ckaFn8obS5-UHXNF8J3fVNX6LFKITS_F6aLukMP1-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رده‌بندی برترین گلزنان و پاسورها رقابت‌ها پس‌از پایان مرحله نیمه‌نهایی‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25828" target="_blank">📅 09:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25827">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FavWZxLs6WE77cQL65Skd0aU2MSZpvOM-gF5WUgAlIqfRj72YKfGbx3hZmX5bdsy-x_djXNWNOs5Pb4lj1IC12zFLMCXcbKEvY_BEobFy-R8NYg-ir10aLTkD3igX0R_8A4UzK0KVBA8VUkorDhryqNJ3MqECLyUqIWP8HgMMihgHXh1Mpu3OTIhZXnpRrQMFwcibzsMVJzvmKpX-G_9ToL6cGQLJQQPLobTLiCdJepXvIW831YIqVUukx_QJyrk6rrwbPSsLTiXJrfRBx9EnJrHEYIAZRcQZanbYP7QaUrLPlzwFwgO1wAx5gmRYSHBxNsaQOFHfmo39ZAHhQ3vGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
هری کین:
باحذف‌ما من دوست دارم لیونل مسی برای دومین بار قهرمان جام جهانی بشه. من طرفدارش هستم اون سزاوار قهرمانی دوم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25827" target="_blank">📅 09:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25826">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7c3766c7.mp4?token=R6F63FhccrAZ50mlYQgwPFycbjEk5SPLJeX90D-5PeIVX3Vr54Tq5XMLtdAQKOzul-ar5R4kbdQs-89yWvqv7ixW7TY3bvti8TjyMmTQ5b84W2vGG7mYgItCLdGz0x6whW1XLBpg_lSKagWHYb6UXR4pWy2vTZkj0ah4zGWpFzognJk8pL8qI_rz9FWRu6yo6Y0WohlXqIWXtY1rG4-HJooLsDU5M8CmbWvF4K8rbti9jO1DkKPWo9QPcfyrimPGBPC867kj3jfxap1dWcBJFyoOl29nSytnF4Fhka5lJE1aWXz6GbejY5Q1W_AcrKlSSxwYC33bXSmxaekVjY56lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7c3766c7.mp4?token=R6F63FhccrAZ50mlYQgwPFycbjEk5SPLJeX90D-5PeIVX3Vr54Tq5XMLtdAQKOzul-ar5R4kbdQs-89yWvqv7ixW7TY3bvti8TjyMmTQ5b84W2vGG7mYgItCLdGz0x6whW1XLBpg_lSKagWHYb6UXR4pWy2vTZkj0ah4zGWpFzognJk8pL8qI_rz9FWRu6yo6Y0WohlXqIWXtY1rG4-HJooLsDU5M8CmbWvF4K8rbti9jO1DkKPWo9QPcfyrimPGBPC867kj3jfxap1dWcBJFyoOl29nSytnF4Fhka5lJE1aWXz6GbejY5Q1W_AcrKlSSxwYC33bXSmxaekVjY56lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25826" target="_blank">📅 09:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25825">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAYxUuTUrQyBy1oKlmTiZJ-yEZUagYtYDGn_UJ_BQoUABJIi1mH2BJDmW9wrNG3D4G5i-9-RlLLbf0ZuDYYgOczJb8kfjfVy2iva1seAhX7OfbQUeXAVRvTaGPmf8M0Lpn_KDafBX0wp23lhT30HeF5bU5dZO8OeFSGQLq8IA8LqgDFrqsWKfNhHkCBKsOrIMcEhtyhSLLpHmcZLyMaRNpCxeUGtKLzKYQBoIMAVZvOp2Byhhx4uGHE5xgSaVv93GfyJBwqND6ueeC2c9qJOgXLGX3h51QT6Ar-qWjJOomiK3yuDL52mS2MMheb1QvQ8AprIPQ5HqRggLkmBYlmG-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#فکت؛ تو تاریخ بنویسین، مسی 39 ساله، پرایم هالند، امباپه، کین و بلینگهام رو گذاشت تو جیبش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25825" target="_blank">📅 02:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25824">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZdglBDy6avwvaqL2ekv7Id3Q_7Aaryudi51rGoK0AYay1-2a2wo1bHFRlyGMix9MKI8iqPWtBj1ZxX6bMJGUCz3GXLNhRvp_hFzAOWix23Qxo_g2mwDxQ0MIrZtsi_VAqr6t1yz3LiQWClsPPhKGBDMT3z_MOn-BcpcfGVznqjS7dImo6N02UvLrj8lBVc-sPxtTZj7aJcSm_bDfBH3FdjugsL7to8Rs3mKkOHycvcNVS6eSoTgGjnkiZbL9TgRUibwQnuKzy8N4uu2ZWptqxzcwKqPT_xAf2EQq-EZr8Hm1s4lqyq-BLnV-g7Ip7d-6WXazHTM2xmeAoFoDbg-bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه ‌تنها دیدار‌ دیروز؛
کامبک دیوانه‌ وار آلبی‌ سلسته مقابل انگلیس بادبل‌پاس‌گل لیونل مسی؛ جام جهانی 2026هم به‌آخرش رسید. روز یکشنبه 22:30 فینال و قبلشم بازی رده بندی. بعدش یکم استراحت و آغاز داغ رقابت های باشگاهی در فصل جدید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25824" target="_blank">📅 01:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25823">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=HLWDuJtVQUgn1EHC9YjQ6w2diqN1OSPA9eW59BQMnQcQ2DD4KscSbBpQQWg5NulvfL2_3J-0O4BTGy00uiGaqX30IuHg7oDj_AjPtAP3p0c_F0KNpysy5OyUjeqb46ICdZFgPXQhRSEcRmsNSf7soSdyaQnIFP4ik8b7HjkPdJMDDJC84yi80VBhT4YCHA65rSvn5Zfb0LNWJ2F16SE1t1GxiOmVaIhckr1Y1zItIJQVgFIbAYmIIQqJR0640wCI3phq9uWoe072Et1LIYa4W7nk-8LQG4KJSgBTHYko_R7em02S7w0RMxqEhZNEgq1nLPJPtzuOHLKr2JhHJjZCRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=HLWDuJtVQUgn1EHC9YjQ6w2diqN1OSPA9eW59BQMnQcQ2DD4KscSbBpQQWg5NulvfL2_3J-0O4BTGy00uiGaqX30IuHg7oDj_AjPtAP3p0c_F0KNpysy5OyUjeqb46ICdZFgPXQhRSEcRmsNSf7soSdyaQnIFP4ik8b7HjkPdJMDDJC84yi80VBhT4YCHA65rSvn5Zfb0LNWJ2F16SE1t1GxiOmVaIhckr1Y1zItIJQVgFIbAYmIIQqJR0640wCI3phq9uWoe072Et1LIYa4W7nk-8LQG4KJSgBTHYko_R7em02S7w0RMxqEhZNEgq1nLPJPtzuOHLKr2JhHJjZCRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25823" target="_blank">📅 01:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25822">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🏆
تصویرجالبی‌که ESPN با عنوان " لیونل مسی و بادیگاردهایش" از بازی امشب با انگلیس منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25822" target="_blank">📅 01:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25821">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHXDv0kKRZ-Jf27X23fwL2etujfemlUwPEbbXGDM8H5Gbg1gBQFI7PGadejX6Rsem2OwGkhQ9Ut2gH2ZJMUPiI6h1E0gwOu_DdwYU1OwfF5BgPYHh4z2Gv25hheOm13hOj6RJ-uD7bwLnBSOTT3IWWA6ioE6vxeVKsYRgA-4KNuIZBusEqSV152CMZ4S17zIaIrsqRLoDIWQYfZH4l5TAr9J7QB5WBMUwCbtpM-Ekd0mLZXgggFH_wuo0vM2RsrPkGCfTlXjDapYs3mYcHa26NaHdnH124P7SIY36shQ0KLffUDkSxhxxHAleqF4gxQy900f_F6O7Y1m8FUZWlWldA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25821" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25820">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=nguCgkpTc9a96QJYefZRvyIdNPQMvbMFZFvONLu7_oSwr2KIPpbiKJeUg000DVMbxJHWOMXAmcNWgwj0ij_n_PdEfoV3MHAPiQejDircQ2StnTeZkIPs9NPqwJ74tkgQ57PIilOsAswYzLWNWo3ccliipvRlodVF0EVHpz2VnC0w41egAhjm3tTFC2J6JvSj-gvCl06X4M0XE2K8xt8n3VufTWTAmTruXly47grSmpJMup3nrwAAbOWo2huLUJdDcuguMmlTw39yrv47LvFLiHm1h0oakikjNryn-g1XKtVefuENlJUbvUUILHAI9Kpu4H_9GMBCzMZQHirzVTBdIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=nguCgkpTc9a96QJYefZRvyIdNPQMvbMFZFvONLu7_oSwr2KIPpbiKJeUg000DVMbxJHWOMXAmcNWgwj0ij_n_PdEfoV3MHAPiQejDircQ2StnTeZkIPs9NPqwJ74tkgQ57PIilOsAswYzLWNWo3ccliipvRlodVF0EVHpz2VnC0w41egAhjm3tTFC2J6JvSj-gvCl06X4M0XE2K8xt8n3VufTWTAmTruXly47grSmpJMup3nrwAAbOWo2huLUJdDcuguMmlTw39yrv47LvFLiHm1h0oakikjNryn-g1XKtVefuENlJUbvUUILHAI9Kpu4H_9GMBCzMZQHirzVTBdIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرخیو اگوئرو که امشب بازی دو از نزدیک دید گفته اگه آرژانتین‌قهرمان‌بشه به هرکدوم از بازیکنان این تیم یه گوسی آیفون 17 پرومکس هدیه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25820" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25818">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEKcLWppLxgLTS4A1YWgRO3_N431YsvrfwyhUaXTa5JaU3CVMlQFDUQehIR-WOs5n88vSCebdXmmif0MHpSQUfihDYJcdZsqFvJ-H6DRqvasTvQnc-ZVj6wIpkpAYv8dN6ld24EPtENDjM2DN7LMHn_3JOY8Ccm4KYBijOMrgbb8QV9REegVONeoxemr78UqA_4-5AbMbjjY6ewX9FqN4VLsq79xg3y05xaqzC8ygA2LMwXwG5EJtM9e869NHbOa4qqCvryw_m-pJRD0ge9Yg0jvUWY-8PdfJldZRZbSPWstCFddiK3axh8AfQFiDO33ABoKH2uuMmO-4GYUmTyPkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگلیس‌دقیقه۵۵جلو افتاد و توخل درجا تیمشو تا منتها الیه باسن‌جردن‌‌پیکفورد عقب کشید و ۶تا مدافع گذاشت تو زمین‌چون میخواست تاخودسوت پایان تو محوطه خودش دفاع کنه. تمام این باخت گردن خود توخله. حتی اینکه بعد از عقب افتادن هم میخواستن سانتر کنن هم تقصیر خودشه…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25818" target="_blank">📅 01:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25816">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klk3BrJmZMk-Gr3eLEL8S_1zZrJhfJrXpVmYWKtFhiJ2P9hx7Om-jm7EXEtOVSbnr7Y4fBiV0uOKaVEp2udNkvXEOcp01JKjWqgJqZJsEb0ro5fL-mj8goJHH4Hpvkdpkfj9-qaN0lSjxAw6mAgkHLEGQj0slmotvc3DijagVWX1zjGhK3BXr2oyBcKemISQWjEIeHrh8RroxSFfDPNjvP-Dj8GLq3Dj9znHHZlFQWQeC9RfqI8AnshveVRBWz4jM_3O8lRgae3Tuxeucvq6OHKTyJCFrb54qq7nwgW2r0dv7gVM7UgbAwp4gaFmjMZeb1KqDM0VG63iMrguYBUWZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بهترین‌بازیکن‌جهان؛ اون‌حتی از جام جهانی ۲۰۲۲ قطر هم‌قویتره. لیونل‌ مسی همچنان به نوشتن تاریخ فوتبال ادامه میده. عملکردش رو ببینبد فقط.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25816" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25815">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-lJUwE5Unrel_wy-a4GuSTehHlSn8Twx2cKVAYm0u3oAL8qKDo2_DoxO0ry9pROpYNaPiByXKslvKgF1vfYDtkX9ggfmCXhFtFDoMbQoTPg__w93pISCMswYk3cLXrGVS6cI7NHrFPp0wyggClAjQtSKRMrzzztw0SNZ1Fuf9gffSVlTKX7lfPgfbBLAE7RNjiLPxbL6gu-eewJdqQdg0nd1AyMMyFZAIlL2ptZM0-v9Q7aiNafsDE9F5v05LDSX9w6c7kR2P1WABdXXGbuEUBfOfzF-sQw7saEhpzduPKfQid-0dfaGvEHEGsqPjok-1aMPU6D2R2EECZS3cD50A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25815" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25813">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNyqCXt4E4txOaa9ugsJO5f7uXiXDV6BMfC___iTcw8PZL7vq19lMipucOq6PDTYvNgLZBQ2Bz_kagL977CpMnzNYD1G2mqMNAZsKshjApjro_Bqwt7VpiJ8XwH0evd68aSoKRzNYEN3sCSqTyMAI8wk-1MCXYdf0r_uKBe1s6VgPyVhNVC2SF9TKhAaKQBjo-vRjtTiNSHDOLu78j_1tbHRrNT86VSL_GYMK9rJ2emripBqR7XU2P0rgf4X6N4n98I1NzaB1Svnb9GualM4Yus7pHlkHT-IDMOxlWJdkbOz3LKQMm176OLIqK3wAzhgQlAFf1Jo3Wi-7JVYIHDFUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25813" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25812">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKeFucKw8s-vs6-Vn5vfWFv9ItCcRO35YjgWytnG8grHNz_X2crXm-IFKiBjuK51mapmBeWq3TfGklppQwTpD1zAj1vXLId6T4wG9QIdQLvH8zPL5xkhzz8FRYj2nrKycGvQjfbMUUDN-T8HdKcSyW4IhXcfILxoJMmfm8xy87hrdma_avbJHJ4ApbIGsTm_Lp_iixmSSorsnEhx-bTEQM7cfVtMoUuf4VJOPnIqvXA2Aj_lW4sRGunf97IyQ4ZOdIoIePBhhP9HZtydHHnPBAq5NVS1smpq2gYcy3sTKugshB9708JMVHdlOZCLaxpDhaZgYU6PKSNHLYaC5xUWeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25812" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
