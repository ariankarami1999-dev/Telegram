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
<img src="https://cdn5.telesco.pe/file/PWwb8sLpbgY0ZCNmZQLYm9Zam3CDDTGTgSh341yY00As8IFeXc6Yz9kjw5PFeDoH0cPDDlDtyh0ATYIOUffxHGM8t1B_6FtOKz1dyC7PT8JRLj6euAFG1xQVFpkM30LbnEdVI7VljHokLPFTyhQWMsZzL4z--roudc2rmR1jTVvzaJKc6HjbX_d3ePqCWvp36MaaCOmpBlk4qXzWXZhurtzXp_nfiP9xXfgSIF38tHfxV_jESyY-3PuSEPayEwAcTupwZBiw6z4rPuaH0qkwe9cM8SkxwXr2khVWdUNDBc0vnvP0shln7v-omG2DzjFs89dUres9r3_EiCpxqx7CMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 538K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 19:50:12</div>
<hr>

<div class="tg-post" id="msg-101687">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
فوووری و رسمی؛ تریلر FC 27 منتشر شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/101687" target="_blank">📅 19:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101686">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVInxnkaj2L1xYQkevoVZcOhWIZzyT9FViRKK-NYtKoFOxgrfwJJxyKC7ZgJhRZiflWcUHHbIgMNFmYwBmo6uF78UVdiafYa4zXw0-cN4ZI7pE8ThrYpZbqyv0tKaIK8ccaRvxAjYZgK_zr6-X1EOzevoBYydVOfO3vf8RGppKuZ_AuEUXS8OwdG6bjj_j93DTPA3KKGS8ekT4BrVVMpLAYDdILwe-21ZtRnH3tNmU_IcRat31_dFB4_yFbvUqDYEP3ZkddGvBlOk0Mf0yDLIrDFxq5cHzIQ4YgiokSE_I9ZVnwumuOIpFCBNIzM3vGmSanep-fvmAIsYdVr7xVOSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی: الیوت اندرسون ستاره تیم‌ملی انگلیس به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/101686" target="_blank">📅 19:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101685">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBAdYAfTvDPpPSBVbe1x_7BBbmtjzHPkx26MtIPZMjD301yyJtls7mOk4uRGrDxUq3946Qj88jjyEz1AcQlvPU-utcSKFHGjCHuccvVvMCenXrWVCKnBKG8PiuDxUPQNFh9VzMfqcVUT98uPQmg2MoGnPPbAbWbhCZS7WyLST35lVLxORDYoGDgF0lb1bGC3kVVdfKzFrF4zQFg1LJFjGo0Q3ZgmDblqz5z_YrSO4qM3N4HxBToQVC-pmj0r3VPZtD55z0v9Tsr1d9KqMmhMlXOsn095X9DT30o_hS1L0reYeJIePS3pcjMbOfXtToAzlpkcJ1XomueFB2b1lBx90Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
: الیوت اندرسون ستاره تیم‌ملی انگلیس به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/Futball180TV/101685" target="_blank">📅 19:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101684">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfvRiurjBmkmc_PgbBdICH33E7aBs8bjV7JyXbcf9fS88FIT2dUq2lBl1RcLFW81HLdliQWbyBJP8OkEzVrCLeNjyEv7ZId2W8_5mAEe90Q_OWw9BRDCCiaE-1-pD0e1bqjoGpJ5uBguYCIspmEMwkp_HBfNXtksYvfukcjA97s_52bVUSKqohZe1XbQ32WySyTKEuvXHzkbtJY14BfICMcBpZ3WgKHUVm9a9uu5JPquAl73fWSlWGcUjqgpLplH_fxRCGtrowOiEKJXo3BpdTi2GhZzGN22vD86b8QEpzjtofIUV1hSCeRb0ikRUvZdaUCl9dOc4BTzQeb8zZHZzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسمیرو رویاهای همتونو داره زندگی میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/Futball180TV/101684" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101683">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEiljS4vHyiit-kHamXfMhgjnaTCAatHey93LLepEHz1lHAFyf5b2VgQIBClCYWNQ_qX0EtglWaYkpBlj8_zFxxNn6fN6Nq59_gINMpj7jjxp8ubkbhThrW0zMH5CwOHi4OCJz4WBl890HhQoQqiNuZ-nMw7gPjoCK-vSZbbCoxYIGqxZbQHYTwAoK971haD2thQQimf4pj5k5F3erIJ1C8XzZfuwdwJrV3nDL3RNOaPALXWcgzgcE48BRs8url7i8kA3y_AYsUEh2kreRc1_dZTWTEVfGQTiS5fcMbbXIoCAh5bdHRAP97LZEOv-jFoir5zFp8F53tU84twC3RCmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#رسمیییییی
: قرارداد لوکا مودریچ با میلان به مدت یک‌فصل دیگر تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/Futball180TV/101683" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101682">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf1Fos93-C8uyhHG5LdSPvMieoQbnXMPTGFQY7I3gImqqnbpT-kyF4xrN4dJwu9Hkrw9R2HRqracN746SkkGEjkgFdLcAGjUrTUN-oGKueit3bk7XjK3auT0DE94dO_ptRa3DxvF5EQu8z2pB1BTQs0tTg8R2vS5t2XMPi2uRks3en_EyU8fZBxnRE3gEdZhn9c6SwXfaQKaN90X72DZW8mqPuAG1XYgjPF_GuDuQi9MACtJ3MzwHg9ZPT0DBLle3iEgQQi4A6Cty6qCEYT2oHL-JB0OQIlo-wyLfNMTfsTOTczyIaaZzQYO_4UQrvcnn1Ja4wBG2ZtMAjesuVP3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/Futball180TV/101682" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101681">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=YPOxpb9DuJPAqIDmwoZ6T8YmaGKHtEyoJtIaNRfi_9giFBH4ZMcY-k4UmXHxeHAiC0IgjqayWkplquux1mmHUDEiLpOCEZxW3bwc7ykYz0Z4dbumtsweKv9TvKgrU45ELOBhTZVRuCEGmnbhWAYTvioRLerX8mFKtBNQQdiEsbsWAHJKOldH77w6nCwqwpK_oHxCJT1hRlTaTtbHF_Zd_sLrOtKOhWQfBJH1q8G1mMX2v3OGvJQNjgwbzICRNoOIUNhdX3pjqthhOa_s1DQhwNAkUroNAUhvXt2gqHVdogqvxU2BSIulVrj2wdRwh3X9mzCK6_tfw7jc2sjhS4ndYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=YPOxpb9DuJPAqIDmwoZ6T8YmaGKHtEyoJtIaNRfi_9giFBH4ZMcY-k4UmXHxeHAiC0IgjqayWkplquux1mmHUDEiLpOCEZxW3bwc7ykYz0Z4dbumtsweKv9TvKgrU45ELOBhTZVRuCEGmnbhWAYTvioRLerX8mFKtBNQQdiEsbsWAHJKOldH77w6nCwqwpK_oHxCJT1hRlTaTtbHF_Zd_sLrOtKOhWQfBJH1q8G1mMX2v3OGvJQNjgwbzICRNoOIUNhdX3pjqthhOa_s1DQhwNAkUroNAUhvXt2gqHVdogqvxU2BSIulVrj2wdRwh3X9mzCK6_tfw7jc2sjhS4ndYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سوال: آیا مسی بهترین بازیکن تاریخ است؟
🇮🇱
نتانیاهو: باید بگویم، در کنار پله. اما در دوران ما و در دهه‌های اخیر قطعا مسی. او چند سال پیش به اسرائیل سفر کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/101681" target="_blank">📅 19:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101680">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
فوووری ترامپ: من در حال بررسی یک حمله گسترده هستم؛ بزرگ‌تر از هر حمله‌ای که تاکنون انجام داده‌ایم. به تصمیم‌گیری نزدیک شده‌ام. ما برای انجام آن کاملاً آماده هستیم.
اگر از اسرائیل بخواهم، ظرف دو دقیقه به این عملیات ملحق خواهد شد. ایران به اندازه کافی احساس درد نکرده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/101680" target="_blank">📅 19:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101679">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae47457bbd.mp4?token=MxmhuXRZ3K4XVbM0H4DMA9WfE3vEXqVMn-OpaEBhUjTiZmVVYb5Y0cJRMP-7Ewwt9SbA7BZwjXWG7B5DPlxdL_4G0BOYQky8130Ig-FpQ16JLelsFJGXRROhlOXm97F5AO_QbgodcqgoWtgTIidhJSmi42BRJcIZJJ3iqqfUIJgZVvy8YIHZHUOvf8WfgMKM45tFa-nkYo9Wbj5xItulYLfPDIUe0qhS8pJz3mrtXsR68LsLewoKSYdtPFkx8n_P9XCj-AWexrGktWpi51bLr3rZer3KABcDg8SWIPD7PgoGDcrHRLEBOy5VHdQuAfNdeGezEWjgTNVQBPizKO3HTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae47457bbd.mp4?token=MxmhuXRZ3K4XVbM0H4DMA9WfE3vEXqVMn-OpaEBhUjTiZmVVYb5Y0cJRMP-7Ewwt9SbA7BZwjXWG7B5DPlxdL_4G0BOYQky8130Ig-FpQ16JLelsFJGXRROhlOXm97F5AO_QbgodcqgoWtgTIidhJSmi42BRJcIZJJ3iqqfUIJgZVvy8YIHZHUOvf8WfgMKM45tFa-nkYo9Wbj5xItulYLfPDIUe0qhS8pJz3mrtXsR68LsLewoKSYdtPFkx8n_P9XCj-AWexrGktWpi51bLr3rZer3KABcDg8SWIPD7PgoGDcrHRLEBOy5VHdQuAfNdeGezEWjgTNVQBPizKO3HTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تنها جمله درست گفته شده از صداوسیما در سال جاری خطاب به امیرحسین ثابتی: ‏مگه تنگه هرمز مال ننت بوده که بدیم بره:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/Futball180TV/101679" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101677">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBvBU9UvZ53UrRA77PoQTnoi5VwF04uCG2BZoiKHpFAR-7Ry2byf3XWqJiUDVLKCOLTSzb5RAqdYI_QB0QcIi0ZU3VY9aRUdLK_J3Ebm4UBSY13tTHGp2PRlIxYf4uyTfn0PMan9mbiN5EW39vXUgDe6wSZuhtW8BiD3wIs7RDtAxX5tnXgPpxjiVJ6K7gBGCNfTyJyI1zixgTo8mqi-B7xQvDMu9ABT0-clUk73d2FNRzr5BUAmMMkbj62uf5dGgDXVEp3RCu1nVqbFCvjo2s1DEWjf2tOi6rd9tFEkg7O1Rc6y09YaTuFCIhzcpPjJ0_SMgh7EPd2BuA6G9A59XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4cstiVUr2mWlDfsIZ0LugzXVIRuxfvMof9lxiKDWqr9w2alY5OrwWF0l8sIFJfG1OAi2LCEwyw5V8GrqAmrTcZs2kE4fHd4WErYrHwjkAJjP0tEaJZ0VKrHbGx-w0iJmikqV0B4ydzbALpRU309kQwHCS4YNRHfZSpt3QAz5-Il1P1LmKRtqiOxq-Bnu03GlkhG13PK0J9GXRIWOfmzBer_C6swwcVsc_hRvv8rICJayuFKz0ZBSI56My8vk0fll9l51SXtI-EMyAOdhhyAehpM7OCoQwSIKBaqeNnUUMSmjMF--SEPOvxwH6L1hjlrwxyMK_Zd8LhHicOpSj8g7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تبلیغات جورجینا واسه برند خودش Mimoa
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/Futball180TV/101677" target="_blank">📅 19:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101676">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw8HNr0feMR04p14iPj-ew_zusvFoQq5MfRbzm_i5rDae5RI3NSSy41JfXOnEUy7jaKsmpqwJg-8kJTGgrH03zxn2I8R-DHgixrHsksvrQ7lMPSvuwu40-V-vIeCB2m3zbXVRheS068dQgKLXrFD_PpXkCML6HkJw82M3Epsd-lnxWuZ2y2PTfGF23Klt0PpqnTx1N_coNVonNlwUkTOacwf-JQyeQMj5Go18B1GGojeFU1lJe7eoNykv3QNNWu4RwDSWTYZR0lG45Ud3Fq_I19tfpD2FMgCe3xWznL1n5KxpTRDatU2EaiijIgORStluKvchKmqmelMeRf-Nwm3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
منتخب بازیکنان آزاد فوتبال جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/Futball180TV/101676" target="_blank">📅 19:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101675">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d6746099.mp4?token=Hb8z6I2Qetg-zk_BpHXgRiltOzXNQcm70NEjaujLTD0U5LObyUHjdJx7i0qrN7ZPHdsncxPNj67e4kBSKP5x2NPdKhOaJkprAJ0NCfUvQkmWRm_TBeATq9OM3EZLBsfMO5njDwI-8XRKbnMauZd8HiZsH9CFk-ylVPnsG8sXwCKk5ZQJQWWx1Tj2f7f1MuNjSKpbWiWYeLd31VMnk71sTyaAXbDLSBVoNREsOp-uKna3jcyoA_9W0a2sAMevwE_UkpPRf4lvaHHlkqeCpFLcCp1-pj0_fh48PQNzUXz3maglZVdNDwql73NSXOR8dpbmnwlOlKkNGZudduRuO5AuYTkSzCkG6c4wlBtCa5LMNJIIlmbIYoK8ocAGUi9brWf9D5cCVQ2VqEx82FkgNiO7NgTP_BSUk4O4lq_3OhtxpEInNKg4So85tv8Oj8ifLtZizoLOfjhnrh1E8MBSK9JyuStbCn9Kl8o_vVzCJ3OrdbwkV-te9v6SBthJ3uTKwt-p8HemYrObffAMB3HOz6Y5x8yMZtYDXJXADcVOrkVLClwZTPo7DlUGUcFoG85NjN0_6NNxHv1Z7Pd4TKiJ4YQb-1lSxJl-1KZH6B_VUzS9rWk4R44xkFlc6FvyvSM9KPhSFLULs4cvjFF2wByJgbzhtH9SpMnfnxBsSEfFMy2zE08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d6746099.mp4?token=Hb8z6I2Qetg-zk_BpHXgRiltOzXNQcm70NEjaujLTD0U5LObyUHjdJx7i0qrN7ZPHdsncxPNj67e4kBSKP5x2NPdKhOaJkprAJ0NCfUvQkmWRm_TBeATq9OM3EZLBsfMO5njDwI-8XRKbnMauZd8HiZsH9CFk-ylVPnsG8sXwCKk5ZQJQWWx1Tj2f7f1MuNjSKpbWiWYeLd31VMnk71sTyaAXbDLSBVoNREsOp-uKna3jcyoA_9W0a2sAMevwE_UkpPRf4lvaHHlkqeCpFLcCp1-pj0_fh48PQNzUXz3maglZVdNDwql73NSXOR8dpbmnwlOlKkNGZudduRuO5AuYTkSzCkG6c4wlBtCa5LMNJIIlmbIYoK8ocAGUi9brWf9D5cCVQ2VqEx82FkgNiO7NgTP_BSUk4O4lq_3OhtxpEInNKg4So85tv8Oj8ifLtZizoLOfjhnrh1E8MBSK9JyuStbCn9Kl8o_vVzCJ3OrdbwkV-te9v6SBthJ3uTKwt-p8HemYrObffAMB3HOz6Y5x8yMZtYDXJXADcVOrkVLClwZTPo7DlUGUcFoG85NjN0_6NNxHv1Z7Pd4TKiJ4YQb-1lSxJl-1KZH6B_VUzS9rWk4R44xkFlc6FvyvSM9KPhSFLULs4cvjFF2wByJgbzhtH9SpMnfnxBsSEfFMy2zE08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
ویرجیل فن‌دایک مقابل بازیکنان بزرگ فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/Futball180TV/101675" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101674">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e54bda82.mp4?token=f2pCn4L9-tBkk7ONXAXARFiZ6oDL47w-18UWhBbK9zQ39Txc3r3pAV__WrjItu9PbhStZCGQbi3-fEOJAy6kuMPcFrFx12_cNnPJ3bBFlG1wsHA8pD3I2pSFZzoXuLs2_qvqm0gU5VrjvDnVOuHObeFJj8Pl02U1v8Q_IRdRmoEh3VFOZ92F0OIeF_p--QVu2OuPgW45jZzEJ2OE7XDk3bxvNUkTR_59379DUov34CM19xcj0i5K2nXdlzxt0zFU6arXyhavXI1ke8urwZG86M6qnaAJ-8N2KFVyFe7kdNe32IuVuxphnaFq15xjdNJPrN8jxipuNUX3_PkUL6fhTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e54bda82.mp4?token=f2pCn4L9-tBkk7ONXAXARFiZ6oDL47w-18UWhBbK9zQ39Txc3r3pAV__WrjItu9PbhStZCGQbi3-fEOJAy6kuMPcFrFx12_cNnPJ3bBFlG1wsHA8pD3I2pSFZzoXuLs2_qvqm0gU5VrjvDnVOuHObeFJj8Pl02U1v8Q_IRdRmoEh3VFOZ92F0OIeF_p--QVu2OuPgW45jZzEJ2OE7XDk3bxvNUkTR_59379DUov34CM19xcj0i5K2nXdlzxt0zFU6arXyhavXI1ke8urwZG86M6qnaAJ-8N2KFVyFe7kdNe32IuVuxphnaFq15xjdNJPrN8jxipuNUX3_PkUL6fhTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
داستان دختربازی افشین قطبی
😂
😐
محمدرضا مامانی، بازیکن پرسپولیس در دهه ۸۰ با یه دختره دوست بوده، افشین قطبی خبر نداشته از رابطه‌شون، قطبی به دختره شماره میده، دختره به مامانی میگه، بعد نیکبخت کثافت‌کاری میکرده و چاق شده بوده میخواستن بهش گیر بدن، این با آتویی که از قطبی گرفته بوده گروکشی میکنه
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/Futball180TV/101674" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101673">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601e0d1ecd.mp4?token=RyfTUKBmqK8Clx2fQueQugKySoW2psDJLzxMpqtghUo1LJjMtU9fozwz9vuc1toC0UKE8m4TnQKAWSM8TsorOAU_IwtyR81CILb_YXOC9gvEtoQmNBiv0CSxvOKvMkpLSdeMSc_sSsX0D7jCmPAQXbHhHLI5mFzkrdn3DfZDsgY25mVJWPaUtypTgMpHKbRF3jDOJVvcULYg3xEyflyYw8NLrZVZrD8WMpyOTkJZpW7Oa1Bp5ozJqA6EimPGGLdw7meeCFatIL1vybP_Jx4DPe1Vyrmy8Kl7t_IusnrItT3EGPbdXDaahMkDYHVfteFB3RYfLviS1eOEhMsmT7B1yhTW4089XtxYVAxIB1B6Jz2hUdyRxPIwzECMw-RwjQfUJEUuNJ3aDtCq5w-Q1EFNPlrZP0O5i589WGBZakLp2IuS6c-5p_lzoRbbRmyj8fatxP5ne4xRKJAG1uMBCDRxrHik6LBOIkjLtLPpRQHzUWgfRils4pq0_4Tn8UkTqjibCs553PcpJGDeeeJscXHGkYyd1h0ykTcu3NXalfoGdMzJz2pgNhCZSTyV3eOEPqIWt_zr0pNU5fS77Qz3N_QBmoeqf21mcgIRBJkQkhIJsR8YCbOs-0nBe_RM5JoL1QT_0AnoT42uIYdhUTwCGOGmUJJu28kqjRxin9JvH3gTXlI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601e0d1ecd.mp4?token=RyfTUKBmqK8Clx2fQueQugKySoW2psDJLzxMpqtghUo1LJjMtU9fozwz9vuc1toC0UKE8m4TnQKAWSM8TsorOAU_IwtyR81CILb_YXOC9gvEtoQmNBiv0CSxvOKvMkpLSdeMSc_sSsX0D7jCmPAQXbHhHLI5mFzkrdn3DfZDsgY25mVJWPaUtypTgMpHKbRF3jDOJVvcULYg3xEyflyYw8NLrZVZrD8WMpyOTkJZpW7Oa1Bp5ozJqA6EimPGGLdw7meeCFatIL1vybP_Jx4DPe1Vyrmy8Kl7t_IusnrItT3EGPbdXDaahMkDYHVfteFB3RYfLviS1eOEhMsmT7B1yhTW4089XtxYVAxIB1B6Jz2hUdyRxPIwzECMw-RwjQfUJEUuNJ3aDtCq5w-Q1EFNPlrZP0O5i589WGBZakLp2IuS6c-5p_lzoRbbRmyj8fatxP5ne4xRKJAG1uMBCDRxrHik6LBOIkjLtLPpRQHzUWgfRils4pq0_4Tn8UkTqjibCs553PcpJGDeeeJscXHGkYyd1h0ykTcu3NXalfoGdMzJz2pgNhCZSTyV3eOEPqIWt_zr0pNU5fS77Qz3N_QBmoeqf21mcgIRBJkQkhIJsR8YCbOs-0nBe_RM5JoL1QT_0AnoT42uIYdhUTwCGOGmUJJu28kqjRxin9JvH3gTXlI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
روایت عادل فردوسی پور از الکس فرگوسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/Futball180TV/101673" target="_blank">📅 18:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101672">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB70JOf1odqxzkYOu6FDTPTFHJbWe8mDCQ6pJkRrH6qdMKjF3vFJgzW14N8kMeIZpFw5YIWb8V3twGlrP2Kpg3xreOSqfP2CPECot1HelVNvWGiPb7dZ11VkYgcX3zOlcUTZ5GhXOzmi7w7ClOOADFwVsQXabcK_tMCropmI4pcvDgqZHy9EU4Lf0280AOuL87kjMx-UFj92i9y1RZPeCJNsMCXZ4rh4pTFP3XPUBX83DnsEBZPYv9kBwQVKWEOCKXd1V9uA2nIXqwsmdO2KlZhgPa5YaEgMEP6VNyEqS-PmpPg-2VSCjCvkw31hAjWGiFgapHoPaGpBunSe0r4P7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_فوتبال‌180
؛ باشگاه نساجی مازندران با ارائه پیشنهادی خواستار جذب محمد خلیفه به صورت قرضی به مدت نیم فصل از استقلال شد. این درخواست از سوی مجتبی‌حسینی به شهاب‌زندی مدیرعامل این تیم منتقل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/101672" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101671">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815514f088.mp4?token=VXxUUX_kinZ2wdmNjcN694nTBiyonrspYBbogDFIjW-ShBZ9QzHM1q33nrak90xuLBxg39xiOY8wL39b4Vtx7wAO1R3jT6ye6KJ3zzgewmIok6KYWR-q_x6vRzGE4_m1g20SQn-ZSDhxhewkr-VtPBKFIZyVU9hbp8KIWIpZgQgl_0v_q3uV8liaiuiwckcKS3Sw3w0tJeH5YYYVp5HnYLwEgskwMj6qc0DJeAZ_QX_ljgZ1zCOAKbdv8T04A74X6NIMuAmhVg2nnETLhdj9vLjkuwdwtVRgn7ahtOZvIEr_YkdJELuhGT_ZQMoK8UXNuZIHjnHmPrtvPbM2kAcKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815514f088.mp4?token=VXxUUX_kinZ2wdmNjcN694nTBiyonrspYBbogDFIjW-ShBZ9QzHM1q33nrak90xuLBxg39xiOY8wL39b4Vtx7wAO1R3jT6ye6KJ3zzgewmIok6KYWR-q_x6vRzGE4_m1g20SQn-ZSDhxhewkr-VtPBKFIZyVU9hbp8KIWIpZgQgl_0v_q3uV8liaiuiwckcKS3Sw3w0tJeH5YYYVp5HnYLwEgskwMj6qc0DJeAZ_QX_ljgZ1zCOAKbdv8T04A74X6NIMuAmhVg2nnETLhdj9vLjkuwdwtVRgn7ahtOZvIEr_YkdJELuhGT_ZQMoK8UXNuZIHjnHmPrtvPbM2kAcKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مارک کوکوریا موهای بلندش را فقط به خاطر استایلش نگه نداشته است. پسر بزرگ او، «ماتئو»، مبتلا به اوتیسم است و در تشخیص چهره‌ها مشکل دارد. کوکوریا می‌گوید موهای بلندش کمک میکند پسرش هنگام تماشای مسابقه بتواند او را راحت‌تر بین ۲۲ بازیکن پیدا کند. به همین دلیل هم قصد ندارد موهایش را کوتاه کند؛ چون برای پسرش فقط یک مدل مو نیست، بلکه نشانه‌ای است که باعث می‌شود پدرش را گم نکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/101671" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101668">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ST6eo3B34Xj0ZeqX6Z3tSRbqDchYBiINa-qHASR8aMpOltYsx-9OKR0nD0i2kvw8xmvieaOKmTLXwrfefmHgpdP85m5nFQE8VMeIQgXS1lZuVGbkCTBwSAS64Dgl0YQpVAfWoqN0eEA9xkdhO8B3G80dHz8BD5uVF6mp42QRRs3K_P7UvNVgqzeFaKr140cJI1lJBIg6CKs2Ul-_tYiteRUJ58QKcCsdo-Cdl8lcPS_ApmUJB_bex7T9F1Yrgxd29qYJ217O8hwzUd8O1CfoIoJQ4fDfmwm2EmDCHIad0GVJbf4so-1h4XUmXvEFWKuFFcJVcVSx27Gv1HMN7CA1Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1vkkjs21BmP7MfMcuyhV9smh1ODH-wqkd1bziKOL0-Pp5ZP6xSvKdRdsc9Qcanv0joIyy3EIN8GYdaBLxhKKrJIaIcgRGQeAK1vHUPDuAiWfCbekfu08ZaHyy01sBs9DkCA-olyU9ymp_zo9nU2RvbvH-Q6sFbuDUsF7Op2xAbycf_NPvHLRi3I3yIUUT29ebq7b8bZLNczV2WAoYXlZXhX7VqmKttJJZVLnVOJvmUqcvqP_k5LOlQk4HeCJRTZo9s6cv41h2k7G1VajipBagkFPM_10SHzind16vwJOBLmeKA6aXm-ppG4g2vQdDNPYlrkWNAc9C7gnntr5uu4Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BRrsPW05O3pwcUa82LJIda_m4qdtmLo4Y-wSmfelMnxaMHDajlA35i_8drW5F5zE7LaBDUWtSMiirTHq0xyiJZ5T1Q31gvEs3m10CUE0ioEF1N977Or1FwqmCUO8hykF3vNr8tAfR0dBN6uxKhkke2PetmyziMefOLqW7RIKMPCtGipe6a-1zGfjtpyWbGZr86veFxRcTzhuyEQaeRzW3DEWXgKot2654zUED9KK2OAwPEyPz2XW0KzMeq1jSJEckzXus65btVowV2T-TQXHZUuQFpjWOO8H7hALMtBTne-iVI6tHe4Y9FnZDSUWc3Ms0_GVZbdyVPIOugKivXij7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
رونمایی الهلال عربستان از کیت‌دوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/101668" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101667">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGaeFby7uG2mrVSxh2Vi9NGZf5NOb_CHsP23AMWJqsFpp0Bl6EAVKm1OXp9lnchcuLvm8-HQ33PZLS7Z832YC0liB8JYC3_dq2E2qLozbsSSAjmVhTue4zcsbRbynPsjjG4Wqel4CBxdDzt0gEXNddKSGbe-poL07Uw4d1YtBDdKCqUWoKBm5lh21KMv4r2sqwUfbNXQvUkuoAohf3VQ1_MYz66HfEbbhH09940tJMtoKKRx72sYuV-YL2e3qS94adKcYgdYKmB-NheoNwXG3Bzw_PWWY78O0iuK2fAQiJvUUwMiY1RRV5NJH24ftVFnCIWzL58eKJEzm7Bhk6S4yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
جلد نهایی بازی FC27
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101667" target="_blank">📅 18:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101666">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7937bcbd97.mp4?token=h31z2uhBPigjGoLQYEi9zAnAItFRDVlvPc03CsZlBM_Ux5MnRV0yBxYg7IfWnpTpTUGK2xUZl1tmjdrQsytYfkLfaX6U-BR0c_M_q4yo5Ye1zBs84yi5YwldDYtttpP2l5SiaMdALCQlwOjUMqXzRMiQ7SRrXcH_ZSs8l5CymW_Gw4xi2cnk_hzEVcK4XEGHL19Z3FJLeRznfA5jJaDg3l2JlDME2Q0bFIzT7j-6eJP_8qiJVHUX8Hbc8zW4X-ziI0tZFqOxbl9yJwUry0xsCPI8EwWJ56d2Tua_Xc19epYnqd1MjKZvj8oUJ2cJv7uKriY2Wo2NJVqzoRxNyGx4ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7937bcbd97.mp4?token=h31z2uhBPigjGoLQYEi9zAnAItFRDVlvPc03CsZlBM_Ux5MnRV0yBxYg7IfWnpTpTUGK2xUZl1tmjdrQsytYfkLfaX6U-BR0c_M_q4yo5Ye1zBs84yi5YwldDYtttpP2l5SiaMdALCQlwOjUMqXzRMiQ7SRrXcH_ZSs8l5CymW_Gw4xi2cnk_hzEVcK4XEGHL19Z3FJLeRznfA5jJaDg3l2JlDME2Q0bFIzT7j-6eJP_8qiJVHUX8Hbc8zW4X-ziI0tZFqOxbl9yJwUry0xsCPI8EwWJ56d2Tua_Xc19epYnqd1MjKZvj8oUJ2cJv7uKriY2Wo2NJVqzoRxNyGx4ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔵
خاطره قایدی از اولین بازی در استقلال: جمله‌ای که بعد چند سال هنوز از ذهن قایدی پاک نشده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/101666" target="_blank">📅 17:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101665">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f40a1d01f.mp4?token=kJvFWe3mZCGG68cTqHQ2uFqZMqDQ37LZDHlek1YO5aqW2nrQdKW9Ww7_BpkQAJbJEJlE6Si2sp0ThWHFVSW20p8U3jNCofIR58XL9jX1ISgd_kAvIMpikuw8aUsE5WQnCFcrf9wxawysz5HSLC55q5qyP1VZO_VwP89vwRNfJSjbljm-wTJUpTi7EfdVhfS-Pb9-umSImbl2CUEBobmRgBF4maR5mM5AwsWNvPuAtFvj1WyIzKxC-4B0bnwiqYAR4PI-yfbHiBWF3mOYOLHE3Xa-llRHssXiymloOUv-gmT7rY3s_DSbNRU2iDEBWKT1KHZSXvJW3lm9BjcHAYpyvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f40a1d01f.mp4?token=kJvFWe3mZCGG68cTqHQ2uFqZMqDQ37LZDHlek1YO5aqW2nrQdKW9Ww7_BpkQAJbJEJlE6Si2sp0ThWHFVSW20p8U3jNCofIR58XL9jX1ISgd_kAvIMpikuw8aUsE5WQnCFcrf9wxawysz5HSLC55q5qyP1VZO_VwP89vwRNfJSjbljm-wTJUpTi7EfdVhfS-Pb9-umSImbl2CUEBobmRgBF4maR5mM5AwsWNvPuAtFvj1WyIzKxC-4B0bnwiqYAR4PI-yfbHiBWF3mOYOLHE3Xa-llRHssXiymloOUv-gmT7rY3s_DSbNRU2iDEBWKT1KHZSXvJW3lm9BjcHAYpyvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
صحبت‌های چندی‌پیش مهدی‌مهدوی‌کیا اسطوره فوتبال ایران درباره تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/101665" target="_blank">📅 17:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101664">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PB6aURjh67VKJhAhNBy9vyaTrFb3BVsUtIe9XkvHlJ1FyUvXKiR-s6qgBYIqRj9OUkl6JcTgd0vPtTYadAeuvKC4Akg-lNny8TiRMkkTOlWmKubcg3thbQdGCSiZrNCDNuiM5F1IgQM1IKe61rE2Hkbkh3I2lIkCw7M9U9X4QirgVQFyOTdl0yaWHyzxwiuomxtGvI29Ndyd_uITtmrsXU4daVd4Yz-3f_WuDlrZ2oDRToXzWudkZ0LaYMDDbKcM2XWEOKpgICko6Mj93D6mj2atqceE6L4gxSWsWxXJK8RSrGhLuNoRCVcq_itl56qHrdyamqq25IxufwSw-s8ebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گارناچو رسماً به صورت قرضی با بند خرید اجباری به استون ویلا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/101664" target="_blank">📅 17:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101663">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUoWVDp1wJ2xdYE1idcnFrBSYzyEvdEL9EQu7JwCxwlyc93YpfbSRPtCFQZ70296OALQB2uBRAI0mDqsP0y-YG-2Gz9lLoKjHryfzLqhCp9RykDMNmt8cE9eLY_sCcdCl1g--XcBrMaVEI-cIk1OK0L4BNqDCx0U_ICMi3Wmo56XNuOPwgj6A1ciYD_eDQO6LjMFIiUjw3xPLaLwGMMaBNakmSMW8i5Rij8pGnh2d1jOOVgw4ARM1azTAruqp4qJzNPi38kscIA-2B0Bw1jXveEW99c8SNv2ZAFVO7678OnjH8tWri22CLFrN38O8t2mLKjwMOdpAHLRwhNvdR9mDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🔥
آمار ۶ مهاجم برتر این‌فصل اروپا:
🇫🇷
دمبله ۲۶ گل‌ و ۱۴ پاس‌گل
🇩🇪
هری‌کین ۷۳ گل و ۸ پاس‌گل
🇪🇸
یامال ۲۵ گل‌ و ۲۰ پاس‌گل
🇩🇪
اولیسه ۲۷ گل‌ و ۳۴ پاس‌گل
🇪🇸
امباپه ۵۶ گل‌ و ۱۳ پاس‌گل ‌
🇫🇷
کوارتسخلیا ۲۳ گل‌و ۱۰پاس‌گل‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101663" target="_blank">📅 17:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101662">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb77439ac7.mp4?token=UrS997TzuZJOYvpAJypwo2CjCsqREHKG1OO6Ho-mJ6zlE-b8FykqPNlCqRGzJPC5F9zLYxzc3LlvbsbBtHJa1mi817NmFSHs9pjUFmhp3BshXaAoIr4SMZL00GC0DbmG-zeIubRHQZKm1wiFOEen1Z9EacZlE5DmSsj4-_2dAy-em0wW0pSbE_oOwLUISPXOSRwA7fl36XXf7LfZcP3dDubNXnQRqby_uaLuU69HQd5__cME94MSXtlvhSIv0KOLhdAoEw2n7ae2PO4nQrAdqQKWbSIelrysuY8ZvIV3ONiEzMaIwOdKdkcO7uT0zR5jYmrTo86Su0CEc21uvDvrVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb77439ac7.mp4?token=UrS997TzuZJOYvpAJypwo2CjCsqREHKG1OO6Ho-mJ6zlE-b8FykqPNlCqRGzJPC5F9zLYxzc3LlvbsbBtHJa1mi817NmFSHs9pjUFmhp3BshXaAoIr4SMZL00GC0DbmG-zeIubRHQZKm1wiFOEen1Z9EacZlE5DmSsj4-_2dAy-em0wW0pSbE_oOwLUISPXOSRwA7fl36XXf7LfZcP3dDubNXnQRqby_uaLuU69HQd5__cME94MSXtlvhSIv0KOLhdAoEw2n7ae2PO4nQrAdqQKWbSIelrysuY8ZvIV3ONiEzMaIwOdKdkcO7uT0zR5jYmrTo86Su0CEc21uvDvrVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمایت سید جلال و قیاسی از علی دایی و کنایه‌شان به بیرانوند: بعضی‌ها اصلا نمیدونن احترام چیه، هیچی دیگه سَر جاش نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/101662" target="_blank">📅 16:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101661">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098313b0c4.mp4?token=DSE3HdPOFMH0eypkvXK3igm_Wvs1UUa43lnv464WxEMPIsQaODGRxcrMKR2H27gEmQEiyPiQN_zZkwN2rYQleRWxWjU1a3dMI3mgrFy44itNXRjM_2IuNV7dDaX8EURXVH9im8yUnwLQACZ8Xd7hGUC9mTybEUtg5DuCGmHfGVeXyN3I1FRZxpahDl6KwOT3rMQzwoKjeuLNv2kK4ZSt6D2qRyX9lYVWHl1mOSdyCtk8_F7gqzzH_Cv95cBYvWwOWZt5YgT0zY_X72EVN5dEU-TWfYIEfyevX9WqoX381qjqNSOjseshBKWQCjbDY1i7m9FFna4gayYLM1Pq3GpNPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098313b0c4.mp4?token=DSE3HdPOFMH0eypkvXK3igm_Wvs1UUa43lnv464WxEMPIsQaODGRxcrMKR2H27gEmQEiyPiQN_zZkwN2rYQleRWxWjU1a3dMI3mgrFy44itNXRjM_2IuNV7dDaX8EURXVH9im8yUnwLQACZ8Xd7hGUC9mTybEUtg5DuCGmHfGVeXyN3I1FRZxpahDl6KwOT3rMQzwoKjeuLNv2kK4ZSt6D2qRyX9lYVWHl1mOSdyCtk8_F7gqzzH_Cv95cBYvWwOWZt5YgT0zY_X72EVN5dEU-TWfYIEfyevX9WqoX381qjqNSOjseshBKWQCjbDY1i7m9FFna4gayYLM1Pq3GpNPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⛔️
نگرش متفاوت دو سرمربی؛ یکی شکست را پذیرفته و با قبول واقعیت به فکر آینده‌ست؛ دیگری زمین و زمان را بابت عدم صعود از گروه در جام‌جهانی ۴٨ تیمی مقصر می‌داند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/101661" target="_blank">📅 16:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101660">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2eee7743d.mp4?token=McoEZ5_BQRDembH1ZNyXeV5lEngGZp1x5N2B1-YYGYMudDA2qLjlEW28lnYFScAZ1DooPgcsb_nr2F22yDoYW3LqTmLTdFiCmpSbWCHxbSf0PAiAalVcsqj92FoNLOVZ-LRo6DOEpKq8co2FIloUqHA1Vj-viUQBpUVJWF3LEar3aMjPgH4uBTdBUx8vPddqpkz10U_rTlFCnQaPBMsSxCkK7CR8LCfnJOf_8RdHhECrCfL8lxtWnIqBHC3rtWneQOizXi-kCIr7e0HxH7Yxuuh3g1JYp0fCa7PoZN8oqrB39rrbTIqKTdAWuxoymmxz-T5ZfqtatYlibzznQjvzKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2eee7743d.mp4?token=McoEZ5_BQRDembH1ZNyXeV5lEngGZp1x5N2B1-YYGYMudDA2qLjlEW28lnYFScAZ1DooPgcsb_nr2F22yDoYW3LqTmLTdFiCmpSbWCHxbSf0PAiAalVcsqj92FoNLOVZ-LRo6DOEpKq8co2FIloUqHA1Vj-viUQBpUVJWF3LEar3aMjPgH4uBTdBUx8vPddqpkz10U_rTlFCnQaPBMsSxCkK7CR8LCfnJOf_8RdHhECrCfL8lxtWnIqBHC3rtWneQOizXi-kCIr7e0HxH7Yxuuh3g1JYp0fCa7PoZN8oqrB39rrbTIqKTdAWuxoymmxz-T5ZfqtatYlibzznQjvzKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
مهدی‌قایدی: حسرت خیلی زیادی دارم که چرا بهم در جام‌جهانی بازی نرسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101660" target="_blank">📅 16:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101659">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
فرانسه کارکنان سفارت خود در تهران را تخلیه کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101659" target="_blank">📅 15:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101658">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca9e664c4.mp4?token=pDg6-wT3h_hqXaXduX-EgTvruowFfNu7IJVbklCPhendsL4OktX6XRBIWscmXMvNP2o4eEk9Hvs21ST-lO-K2OLazh_viNnGPxZ2ZHmtd2QzYy1snKRoJVMw0k7OYNTXerQ8wuPQcwO_oncOJZ3stLlzfUU6_rlooSSpMjhsWGe12F72hD9XAUocgrmUbuDJvaUx0vBOchMfQPqCWqjALf-J6Y5mBYxUEPwfzTGVio7y4Hx78BWx9K3u49WbOAT1xdc3p0RzIyjiKGmWU0D-wb5sI-Z53kksZPU6_TJYqxKZERay3265Kxo2jQOsYcMKoovig7t63I3CB-Xf9tIwgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca9e664c4.mp4?token=pDg6-wT3h_hqXaXduX-EgTvruowFfNu7IJVbklCPhendsL4OktX6XRBIWscmXMvNP2o4eEk9Hvs21ST-lO-K2OLazh_viNnGPxZ2ZHmtd2QzYy1snKRoJVMw0k7OYNTXerQ8wuPQcwO_oncOJZ3stLlzfUU6_rlooSSpMjhsWGe12F72hD9XAUocgrmUbuDJvaUx0vBOchMfQPqCWqjALf-J6Y5mBYxUEPwfzTGVio7y4Hx78BWx9K3u49WbOAT1xdc3p0RzIyjiKGmWU0D-wb5sI-Z53kksZPU6_TJYqxKZERay3265Kxo2jQOsYcMKoovig7t63I3CB-Xf9tIwgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجراى مريم اميرجلالى و حميد لولايى در بين ٢ نيمه جام جهانی‌سمه خالص
🤣
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101658" target="_blank">📅 15:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101657">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔥
▶️
چند سوپرسیو دروازه‌بان در فصول‌گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101657" target="_blank">📅 15:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101656">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a89e53e52e.mp4?token=DfKOWMRJcQVnfVqhYDDtFfE-fat9g_Zd3CKqNiC-WFPmKonhckqnfXG7vIBqFAdVbzKEukRkq-MYUVWdEvsVdqcuec-xHr6Pt_WjVWXIbVg8ZHoZE9Ix91PaCUO_sCX5Dyq5luXSNgflpDPPfCh1HlgAn3of2Gu8CwIUfDek9e8E24dgSscR80xcHQV5QvNJzPKWHK43w2OzeybnkBhc1jPJZf6GvJDsuYvSyBmeI0_lBZt6FOwIDzpTu8dyUybpciSpYP6EdPq97O-NwiY6qEcu_N3tFQeVS31IoPwiQYk4-ii2KPFrExwOZ0HeZ7zeI4NZkR_EE00XfKef5G0z7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a89e53e52e.mp4?token=DfKOWMRJcQVnfVqhYDDtFfE-fat9g_Zd3CKqNiC-WFPmKonhckqnfXG7vIBqFAdVbzKEukRkq-MYUVWdEvsVdqcuec-xHr6Pt_WjVWXIbVg8ZHoZE9Ix91PaCUO_sCX5Dyq5luXSNgflpDPPfCh1HlgAn3of2Gu8CwIUfDek9e8E24dgSscR80xcHQV5QvNJzPKWHK43w2OzeybnkBhc1jPJZf6GvJDsuYvSyBmeI0_lBZt6FOwIDzpTu8dyUybpciSpYP6EdPq97O-NwiY6qEcu_N3tFQeVS31IoPwiQYk4-ii2KPFrExwOZ0HeZ7zeI4NZkR_EE00XfKef5G0z7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❗️
علی‌قلی‌زاده: امیر‌ عابدزاده استعداد بی‌نظیری در نوشتن و رپ داره؛ از او خیلی چیزها یاد گرفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101656" target="_blank">📅 15:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101655">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEXta4jOvFS0jlo8G5qtenvAOSz1qbROLwkgaHVUi9u_Y5fnlOzhZt63E0x_MNUgxnaH1OI9HcYgS8k_rbYdQXapwCi1pPYzh0qqBnTxxanODtl6tl_Fc0GXuR97k4WOGF4MW_CHy2yT1ithKLnItzJLP5Nu5mpypUopM8E6NXoiB6-a6BKXJDphBwa1q1Q6qpua3zjEq0Jc22qeBSCVW3-bUyvtNAkDBwNj0VFHRluGR6OVoeBfKGxzT85zrfxhK-3BhRPQAotr2Cu80t0mc6-mvWiIQKq5z1TvP7ZZb23gAEytyUff0D8gs2NMBxmmOwav47yWZWPx6B3_8xqeGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت گاوی زیر پست یامال
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101655" target="_blank">📅 15:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101654">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c5973b07.mp4?token=mtxO93sMBvOhGgrxo0fbzTNaWK6XOr0RaS_iItNlzmUEu1B_8hzNWfBFb9lTAv_Xg8J-iFY4ZDBcy2z19hyHVcveYeNS4xHtxCNkR1_zqqCR2rc7EZox4m-u1uxta6yvj4G7_YaiIt7Hq9NMPWvS8rXxtT0cQQkGfjgo6w8FnrvGw0vzEBvLZt1QkUzjjGJItME_nbfCR7v5BVvJ8iRtSVL9vkgQoNPMvJtj2mb7DLYzjkLoqjCW3Knj5n4p4t8GX1UnPaS_gMMdeerp0YBS8h0oNvjQA3Xoz8JiAvorVE7xVyg4lDu9Rf_mqYwthVakZmH83oatO1YGCrZrf7FBdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c5973b07.mp4?token=mtxO93sMBvOhGgrxo0fbzTNaWK6XOr0RaS_iItNlzmUEu1B_8hzNWfBFb9lTAv_Xg8J-iFY4ZDBcy2z19hyHVcveYeNS4xHtxCNkR1_zqqCR2rc7EZox4m-u1uxta6yvj4G7_YaiIt7Hq9NMPWvS8rXxtT0cQQkGfjgo6w8FnrvGw0vzEBvLZt1QkUzjjGJItME_nbfCR7v5BVvJ8iRtSVL9vkgQoNPMvJtj2mb7DLYzjkLoqjCW3Knj5n4p4t8GX1UnPaS_gMMdeerp0YBS8h0oNvjQA3Xoz8JiAvorVE7xVyg4lDu9Rf_mqYwthVakZmH83oatO1YGCrZrf7FBdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ینی چه بلایی سر اون تیم پرانگیزه اومده بود؟! ببینید قبل از بازی با فرانسه همگی بمب انرژی و انگیزه بودن ولی تو فینال امسال انگار همگی از مراسم ختم اومده بودن.
بازیکنان تیم آرژانتین تو بازی انگلیس داشتن به معنای واقعی کلمه میجنگیدن و بعد از بازی مثل دیوونه ها جشن گرفتن اما یهو نمیدونم چی شده بود که اونا از لحظه شروع فینال هیچ تلاشی برای بردن نکردن!
بحث تئوری توطئه نیست و هیچ خدشه ای به قهرمانی شایسته اسپانیا وارد نمیکنم اما مطمئنم تو رختکن یه خبر بد یا یه اتفاق ناگوار برای آرژانتین افتاده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101654" target="_blank">📅 14:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101653">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d995b135a.mp4?token=GKgzqka4zAmt4kQ2f2VkNIg-uqpUvgWn_yyNWzzW1o0ngjz_yJRLXIPMEO9U2e5j_w75dFAVCfc5NaMaiEryeM25pT3jsGeYca3DQ5-tUjCdMlw-MLALC02ISWI9tHi0NyiGrIh9pLiVOjcvhwMrJKe_W9uO9vYN1LPDgP8NGft3QMqFEfwb0JScLM1xGCCalry-_BVZgMdJVXThTnbZZp2ybotQM2QLAzTBi3CBEQntju-b9f9NlJs6R5tNmJxJaK5WGygOgssVTzjf2w5lOyp8SBSoVanpk3vNQU60S-piqLWoYR18tNqn_QKptu3U8_1WJmLAsBR-uat3HgndLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d995b135a.mp4?token=GKgzqka4zAmt4kQ2f2VkNIg-uqpUvgWn_yyNWzzW1o0ngjz_yJRLXIPMEO9U2e5j_w75dFAVCfc5NaMaiEryeM25pT3jsGeYca3DQ5-tUjCdMlw-MLALC02ISWI9tHi0NyiGrIh9pLiVOjcvhwMrJKe_W9uO9vYN1LPDgP8NGft3QMqFEfwb0JScLM1xGCCalry-_BVZgMdJVXThTnbZZp2ybotQM2QLAzTBi3CBEQntju-b9f9NlJs6R5tNmJxJaK5WGygOgssVTzjf2w5lOyp8SBSoVanpk3vNQU60S-piqLWoYR18tNqn_QKptu3U8_1WJmLAsBR-uat3HgndLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
رضا جاودانی در جواب نگرانی عادل فردوسی‌پور، به جای فکر کردن به خودش، با آرامش گفت: «بذار بیکار بشم... مهم نیست.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/101653" target="_blank">📅 14:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101652">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7be59d405.mp4?token=sICydQOO5cVaECNUgbqIj7ncQt7112iwEnVaJwEgV638kvPwf4sK3kpbrq-kohukodmjjTJHrOvQ3UJG1ZE-_ca8IsqoaScz-pNA56E2w1wZBl20E_-6J1wQ-unvv-JhBPYqYNw71JgZzYAXRGeBHrBvJrWkb_JS0cENCst-x0HkisT1hqJy4_3mmQfx_x-wxiYPpEIA_KGa3E8cL1iAOn5rE-GZCP0uasBHC8cxzLofA1K0ir4yXjfO_w9Axpj8hLA7LQQ3Toh3QfVB_9MCZRpDPvghCCS8EccY_K26tJNG_bQSMRwXNnIknoHqgG11JPaYPCRTzd11qp8A6K7cTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7be59d405.mp4?token=sICydQOO5cVaECNUgbqIj7ncQt7112iwEnVaJwEgV638kvPwf4sK3kpbrq-kohukodmjjTJHrOvQ3UJG1ZE-_ca8IsqoaScz-pNA56E2w1wZBl20E_-6J1wQ-unvv-JhBPYqYNw71JgZzYAXRGeBHrBvJrWkb_JS0cENCst-x0HkisT1hqJy4_3mmQfx_x-wxiYPpEIA_KGa3E8cL1iAOn5rE-GZCP0uasBHC8cxzLofA1K0ir4yXjfO_w9Axpj8hLA7LQQ3Toh3QfVB_9MCZRpDPvghCCS8EccY_K26tJNG_bQSMRwXNnIknoHqgG11JPaYPCRTzd11qp8A6K7cTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇹
شیروانی، مافیا ایرانی فوتبال ایتالیا: به اینزاگی گفتم طارمی را جذب کن، اما طارمی در اینتر جواب نداد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101652" target="_blank">📅 14:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101651">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxg6-eUGn7x1rflQlMmMP5_EvvWdqBLfhpKpf91FB9bXzmJhR0O0ny8n6CfJYMdC4ejeazW5-d2srtAOqfCrYZGGYF2F19-ifY0VakzHuD5dIouCmuSY8SAAvnbmPpGD7qtOmkHM2Ck0fUJRrWP9gHehuoo0jg3htxLMAZeewPZEGAlWTKwqNyWw0RB-aP8xpwoxmqTOih4HgqsRMTlC8eeQQDMDkL1s-fz7-vjvDo_SyMqoerT05fJa49_YDJzkHZ_2b1VjunELmpOX_0-ZQsdPcqZxyXW2pTeHGn_M2AYkfB-BpT7_iea94BjgJSCn1pG23CvpqkI2GgtisRRVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
کریم‌آدیمی برای عقد قرارداد رسمی با باشگاه بارسلونا راهی دفاتر نیوکمپ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101651" target="_blank">📅 14:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101650">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d13a0e1e37.mp4?token=RHLffNks4NSwJq8Uh08sLfREwTYdNZ9YL9rK7Yabqx26ns-4ENsnQXSdp9nmoGQYaouv7La-ywTmx-hXLtc9TLX2Lzick_7183tR5iavC3jQzCgQiW1sH4wQIp3396xKRWOgE6o53AL6ACUwHMmkA0--L6tP7XUZP5G0kzIkQKODNbUUyJS93IgFJvDFFY5Jwl1mt8AEM07GPSvRmBZ7qiVaq9vNdnRI-ETiQmoSD-Dc_8dAjT99gmQfCDisrUc7d6e9oczsnCArF8AztX9Q4M4Y2ZOVBzIh_YcUKHv4YzLUA8hA8l6oCaUW7T2Ygf3y-iik6b9SDiJqzDwQ0ScePw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d13a0e1e37.mp4?token=RHLffNks4NSwJq8Uh08sLfREwTYdNZ9YL9rK7Yabqx26ns-4ENsnQXSdp9nmoGQYaouv7La-ywTmx-hXLtc9TLX2Lzick_7183tR5iavC3jQzCgQiW1sH4wQIp3396xKRWOgE6o53AL6ACUwHMmkA0--L6tP7XUZP5G0kzIkQKODNbUUyJS93IgFJvDFFY5Jwl1mt8AEM07GPSvRmBZ7qiVaq9vNdnRI-ETiQmoSD-Dc_8dAjT99gmQfCDisrUc7d6e9oczsnCArF8AztX9Q4M4Y2ZOVBzIh_YcUKHv4YzLUA8hA8l6oCaUW7T2Ygf3y-iik6b9SDiJqzDwQ0ScePw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
محمد شیروانی از اعضای ایرانی مافیای فوتبال ایتالیا: با دیگو مارادونا رفیق صمیمی بودم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101650" target="_blank">📅 14:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101649">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upBZPL2xfmD_clXboUDnPXVc3cV_AlrezYImCHaPn7D6_Ck39dYHj7bgETF4e0Eijctsuv5nC6qQf5v0nyjVt91_ViKPQrdQv5MsX7ArZAt0ahPs7SfNqc61g4ydiyCMLyv5GyICeVX5wl7rKhtBha4NABZujQyI0zxkDqyRDxCVkpL32x4XrKDIlmPJQwOYij-3CiieyM4rtvSq9AMB476-m0xgQMo2eJzsE-uxT3wAuabRGF_T7erj-dTe-0DcBiTCzCMpcMY-tY4yXWf1H0Hi9DmWaWNQ3bJcLPsGH7U1Ahe5nIsqMFgjxmYL6dBoTERbhUF4c1dJCHP1uK8gpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
⚽️
#فوووووری
از مارکا: انریکه در روزهای اخیر با فران‌تورس تماس گرفته و پروژه آینده تیمش با حضور این بازیکن رو توضیح داده. قراره تورس نظر نهایی خودش رو بزودی اعلام کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101649" target="_blank">📅 13:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101648">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f57cc284b.mp4?token=oDVqJ3RRcte5oFMyzlb4BeTgbZLd1BQx9dB3t9YHOS-l2-7ssTp-72DxgMXpXyXHT5p-RubXsGo12PaxXwqC_ufAap9-OZ--_GsLaFNmEZ_pcCHI9lB4AHl9Tw8sLz0SQwYxhYbSkYy83t1iaiXfFeUSK3vNTXfR7QokvCR9DbD-CcMvxRKOHAntlTmWVT1KMrkHihoRL-mzni8hYqaqO-6FQa2q6Lj7D90R6pjHm8Bmr0GEVoGtx3Dac3oC0940l-_DFUIGXDgW7-WsnqugdOwulswahSZJNXp5v_TT_oRzeERqMQuOGNfUN9yTP8jXVUMZkIe4F7CpnQ5oAuVwPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f57cc284b.mp4?token=oDVqJ3RRcte5oFMyzlb4BeTgbZLd1BQx9dB3t9YHOS-l2-7ssTp-72DxgMXpXyXHT5p-RubXsGo12PaxXwqC_ufAap9-OZ--_GsLaFNmEZ_pcCHI9lB4AHl9Tw8sLz0SQwYxhYbSkYy83t1iaiXfFeUSK3vNTXfR7QokvCR9DbD-CcMvxRKOHAntlTmWVT1KMrkHihoRL-mzni8hYqaqO-6FQa2q6Lj7D90R6pjHm8Bmr0GEVoGtx3Dac3oC0940l-_DFUIGXDgW7-WsnqugdOwulswahSZJNXp5v_TT_oRzeERqMQuOGNfUN9yTP8jXVUMZkIe4F7CpnQ5oAuVwPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیدجلال‌حسینی: بدترین خاطره دوران فوتبالم بازی معروف با اولسان‌هیوندای کره‌جنوبی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101648" target="_blank">📅 13:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101647">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b841d71bb3.mp4?token=CAtDMgG3bK66nW1k08a-C-NBFL2614JAk1MqQaDkzzRV-SDG0NEZypTrjb9imHaBRzAvm0ty3F4Fz79S6eSE3uXrCLlyKQiwFlg6xoDTLm-DBEkSezVExMquAAJTaf_shQI1yQLYNJnxDasf7pnELm_PJ1KmGjJL6NrymcENpEIzQTdoazFUcV3Zr1dxBSBFMF29SGx4WvnwVceAUttFOqfeXdHSVwjCcYI2QVgI7LyMFcmTcIzqy7kIaC6rlpvBNWMvO10jm0IPs2xAII8oB8Asv-OM7ujTeLPFX3jrE6KVB_TfdVdvKDUXL0P50Z1Oa5YIUzpYh0YWG9Ydo5zatQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b841d71bb3.mp4?token=CAtDMgG3bK66nW1k08a-C-NBFL2614JAk1MqQaDkzzRV-SDG0NEZypTrjb9imHaBRzAvm0ty3F4Fz79S6eSE3uXrCLlyKQiwFlg6xoDTLm-DBEkSezVExMquAAJTaf_shQI1yQLYNJnxDasf7pnELm_PJ1KmGjJL6NrymcENpEIzQTdoazFUcV3Zr1dxBSBFMF29SGx4WvnwVceAUttFOqfeXdHSVwjCcYI2QVgI7LyMFcmTcIzqy7kIaC6rlpvBNWMvO10jm0IPs2xAII8oB8Asv-OM7ujTeLPFX3jrE6KVB_TfdVdvKDUXL0P50Z1Oa5YIUzpYh0YWG9Ydo5zatQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
کریم‌آدیمی برای عقد قرارداد رسمی با باشگاه بارسلونا راهی دفاتر نیوکمپ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101647" target="_blank">📅 13:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101646">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c225ae4bf.mp4?token=U51ZKINFePFwrQVHwmsUxQAvYk2uTU1KiBPJxIjbS9ByDVRMvbATbTCLEbkY1FTp_rSxVM7IB2qgojkKgI5wK8tuAqQIGqSIqtv15F8K6ErW5tOwdAC2uJgbIjhql3FK6a5oyvELOp6OM76G4UpneNFufF39qrjbXJZ-fjSNTOxIKdnyJ-XsImV051cs2_aRNuXLzxLWJuzsKsNzwM7isWOHlCNGiCl_p5RSS9ZSx5p43QDvlOFzlz8g354hYhIMjw4Lpe2zFm3um-IU00NyDGU3fBKkyutN6ksA7clBYhkIFpSAZXSoom3fPqspOHKP5PkggB5tIsAp8zjVbVTQtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c225ae4bf.mp4?token=U51ZKINFePFwrQVHwmsUxQAvYk2uTU1KiBPJxIjbS9ByDVRMvbATbTCLEbkY1FTp_rSxVM7IB2qgojkKgI5wK8tuAqQIGqSIqtv15F8K6ErW5tOwdAC2uJgbIjhql3FK6a5oyvELOp6OM76G4UpneNFufF39qrjbXJZ-fjSNTOxIKdnyJ-XsImV051cs2_aRNuXLzxLWJuzsKsNzwM7isWOHlCNGiCl_p5RSS9ZSx5p43QDvlOFzlz8g354hYhIMjw4Lpe2zFm3um-IU00NyDGU3fBKkyutN6ksA7clBYhkIFpSAZXSoom3fPqspOHKP5PkggB5tIsAp8zjVbVTQtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یادی‌کنیم از دوران درخشان سادیو‌مانه سنگالی در ایام حضورش در لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101646" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101645">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rz1CGS4okc5UYu7is-lnn4GcmYksVPLa1AnUWYouh542SlrNWXxdH02GZIV2b5341iZrruGn09kzJuWNZpuACFP5LC-9WIftezFZzy4G4cJVaWcyUmlc4NjOKPCzTGBsk2d-_lMgYUzOJcCnBS_L3a64DTeVBYe0YrvRpqYQR838wyCL4YiPUQzea2HzKFTxURAUAZkVoaszaoY5PimJbcNXc4cZLsm4TfMFKF63UGjYz7lNV7tr7Bv4BlrNKRrru2-jA5SsGNp85CgDMNFMR0A58qVM6sEemvxIJ94PxYIeJX6SitkuW9ItxE8f_PS-1NPaZVbCDtIUluIGD3Ug1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101645" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101644">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBtRQo9OEdYxmG1gDsfBVeiYKOBp7Neg1uvPNV5e4nQIO_pcMoWOVDdVPyhdt5VAqUdq5Xx2cP1LylpHgpUpjYd2SdEqg9gRw5orkgK1DPL5wdS-PQDT993CVlJwl3wiAw7THbZr4NLg-5cXpqcBXXs_Z2eOKJ3EvOgbpwGMVidgns3vgrH8L7ZAWtABaDsxJrlluSWgQg1Oc92E5TPzn-kuD7eSG50sRztUnjZQJ9LO3j9VBX5Ogp8QJ3eo0fs8cpwny6bA7QmUbY3s36rVIcnQMjcaFaP-I_kFdTPpiz9pROk3hcYwQrN140uwy4hbxyM2xn-_8mlzQDkG9B0Zvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: رئال‌مادرید فارغ از جذب رودری، تمام تلاش خودشو برای جذب اولیسه به کار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101644" target="_blank">📅 13:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101643">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXLyt0tUn4ZPLEQgm3llE6JYnGmYUla3mlwYB0PvCwqSiqTqZmoIRmg_1-2Lfxg9FkcjyGYfV1lOIguDDKX-LL5Sh-rkRvQDHpI4GPtHoqaTyPP906SlEO6ODosaq58qOBY60vYsarRE3YHTz59sw5RFu5C7ZSc8J2QXUEVw2j5eudaQRtvg-GLkJrAUPPNuUuYUavJWrFQXQm9HORf7XN9qm4n_gX3OZbNQ-N3XOFNiTDHrH9z0pFx3vw8qZw3BbG_2yl_G16IW6DKqh5jfP1psMOltbSvBFw0aDBgjvqKIFThtW87KLEeu56vWWKLIo-QQ7HVVLjD2NqdZFn62hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: رئال‌مادرید فارغ از جذب رودری، تمام تلاش خودشو برای جذب اولیسه به کار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101643" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101642">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c46077059.mp4?token=iW8KNdKeyjip4w_FVUQeqGB8VBwCnXq26sFT-4ppfGPrzNgACL0bhanqEGNcjWGn77lZ9HVMuBWYB-iKk_k_g1Lr-SSz6gSjwg_a5zVJQGvWt42XFyvUaRJp5e3aYUP0t2NyLB8A2Nt4d3kUkjqfRNzuKqhnHfagCexlJYuBLFiabbWVK8yeJ1u814c85UXbZJl1oOCBD5cHCcnJOoAfAdVTJehcNbpsCRdxKQs3syadx3bfQzWbLs_vPvIAteBt1aJznmvowZEavhJmBmIkaY71wksjXyyEBaBbku5uVmGW2osK4_MEKM3eUJ4B-wKKCGSgrZLyAjAz7MMyYifuyKKgbv44bgwmvjAneB6_oUp2Rs2GWm2iesLwuWBdJgZcQL6PmQQxk9zgFbBDOsW6EB9bkRcDytS5iZwW61t9xOI-HO8y12QEeBhgZTnPg_z2UZmb6WL6TJ5dkwR2A2y1HrIh7LpEwMGeali0cv6MPiUy_coSnnh9hpX-UHXOaMWDybsz_thVHcaeUtJ2hQseSByRUIF4FSRmX7-7on-0VGvT9sQ2cx96zzbaLLVjmw8XH3ujAy_a4u_bjmoVRDS8LkFu3eb4HIXjFZ5mJVt-B5twb5qDBq5swO5LUez-RBdcJ6HwG9D9xhcMnLku_9ntKde_pXCoxFtlVtf34uWXBXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c46077059.mp4?token=iW8KNdKeyjip4w_FVUQeqGB8VBwCnXq26sFT-4ppfGPrzNgACL0bhanqEGNcjWGn77lZ9HVMuBWYB-iKk_k_g1Lr-SSz6gSjwg_a5zVJQGvWt42XFyvUaRJp5e3aYUP0t2NyLB8A2Nt4d3kUkjqfRNzuKqhnHfagCexlJYuBLFiabbWVK8yeJ1u814c85UXbZJl1oOCBD5cHCcnJOoAfAdVTJehcNbpsCRdxKQs3syadx3bfQzWbLs_vPvIAteBt1aJznmvowZEavhJmBmIkaY71wksjXyyEBaBbku5uVmGW2osK4_MEKM3eUJ4B-wKKCGSgrZLyAjAz7MMyYifuyKKgbv44bgwmvjAneB6_oUp2Rs2GWm2iesLwuWBdJgZcQL6PmQQxk9zgFbBDOsW6EB9bkRcDytS5iZwW61t9xOI-HO8y12QEeBhgZTnPg_z2UZmb6WL6TJ5dkwR2A2y1HrIh7LpEwMGeali0cv6MPiUy_coSnnh9hpX-UHXOaMWDybsz_thVHcaeUtJ2hQseSByRUIF4FSRmX7-7on-0VGvT9sQ2cx96zzbaLLVjmw8XH3ujAy_a4u_bjmoVRDS8LkFu3eb4HIXjFZ5mJVt-B5twb5qDBq5swO5LUez-RBdcJ6HwG9D9xhcMnLku_9ntKde_pXCoxFtlVtf34uWXBXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
هنر استپ‌ و گلزنی از برخی ستارگان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101642" target="_blank">📅 13:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101641">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNx_OFNMZU8kMSl1Za8n4mCqcsb2k9pOXuRXUMXWFyWSiuYQbwDAsfzopaqxd6l48LbcJ8z13srDXVAmr2tbjSKh3616BjeGrfCP5ieHlONtkmOS9160mYZwMvvF4Z2oIfyB22bdcFcSOOeSj_hJ9AsTCWQgri8XdR_6gUvXUovVYlOCSlW907mXfUGFewKAZBvgrCkBcOr-pGPL0TUuQ69QSDGqmBdT4vywqrV4jfEEORMSFifvD9IbTI3BPPw6pYQ-HaW5_9jdUViCMGmyOvLoY9hjwp-OcD1XApBfmYaIqsZrKtnDb_EAHjpZTVcGZv60yM7ihFHem5uWqleU5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
باشگاه بارسلونا در صورت عدم جذب آلوارز، داروین نونیز مهاجم الهلال را زیر نظر دارد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101641" target="_blank">📅 12:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101640">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOpv4Keaig7FyZf6KOhuQGFpVdxWBhxKWdbLsiOuNl-qylPE72iB7joryNsAK_ihGDYFziXydPzn3r0RBSDSAs1H4LYnA_i7TjD0jZZpWsW-gq5EKNiqS1vGh2srOpzTJ143KNOYHVQutkSzOv_Pzvzwin4rRUvzpPXKIiw1SItKSY7lRH8N8P4U7RUHA8wcg9slEjjbsRX70WtcW5SjzqkeCuI61cGQPDgHJZSCrqZOXbe0DSJLLqZrWWx9EqZBcCbqfHw0Zd-1NdEvkslu5qOdURgvoRZFYihCaEQ6shvMoaWH_wPnKLGACbMrbUViNbn6vas9zdU8JtzL70pclA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
😢
خانم‌شکیرا و چنتا از اساطیر NBA
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101640" target="_blank">📅 12:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101639">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fa0ff87b.mp4?token=MPSkptROD978aMcMc-uerBYUyYK8avo5vyIh3dWb4iRX079PV_hgBKDmnuxqOT_mvDmuncZDNDKYY8j9TTM05GuYOSfHGgBzpgaLPuAd0KHG9BfoqM5rGjgXrIiJcs0IZmgfGFHpIMzRt3o8Mw3HvLjXZzRgQQZc3JHz8lbOkrHlQ1LpTGcgb6Qn1TW8FoGBn38b9HwJgrs2IiCNqNXC-oNWSNudtMnZ6MfcGGjvpBIuVxUUewj5YKA5xQGzQLeMNnUjhzwvWco23QnyUfBERtHamnL1wDm16rKP-KpHo3aRL2duYrCM8lZMg5lfwIfoGEgRVuLfvS5F4B4cE4AKrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fa0ff87b.mp4?token=MPSkptROD978aMcMc-uerBYUyYK8avo5vyIh3dWb4iRX079PV_hgBKDmnuxqOT_mvDmuncZDNDKYY8j9TTM05GuYOSfHGgBzpgaLPuAd0KHG9BfoqM5rGjgXrIiJcs0IZmgfGFHpIMzRt3o8Mw3HvLjXZzRgQQZc3JHz8lbOkrHlQ1LpTGcgb6Qn1TW8FoGBn38b9HwJgrs2IiCNqNXC-oNWSNudtMnZ6MfcGGjvpBIuVxUUewj5YKA5xQGzQLeMNnUjhzwvWco23QnyUfBERtHamnL1wDm16rKP-KpHo3aRL2duYrCM8lZMg5lfwIfoGEgRVuLfvS5F4B4cE4AKrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
سید جلال حسینی: اشتباه کردم همه زندگیم رو برای فوتبال گذاشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101639" target="_blank">📅 12:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101638">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcOeZRsfSPQ7CARpj5LT2ONZWjOceN3r4CoBpDYUJxcDXqTo07R_m1uH2NMl-RcmMTZqRTiZlHoMVMePERYDhssQUl-NLlsLvbx84PpNLputDIc1hOp8XC6PE_5_7TSMuuFDleWpOMwZrOcbXC0FEGoiXLENvUgo2JzL7BMN-dttGqsXr3nAnwgxTUxcodvuJQeopR577u9p-Um45hFggy3Gx4dP8HP1ik1J7jSKKPiPevEepFYyh6QhDTYdX4Qu2oGhg7P2jWnj5EqlsYEY0eclZ2VfX89_ZElF4vRW-_M4qRnqAYxgHsvgXgxaJm-sRSe-omQOgsrFA7nO1Gmamg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📰
بیلد‌آلمان: آرسنال حاضر است برای جذب دیامانده ستاره ساحل‌عاج مبلغ ۱۰۰ میلیون یورو پرداخت کند اما این بازیکن خواستار حضور در پاری‌سن‌ژرمن شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101638" target="_blank">📅 12:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101637">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e657d4048f.mp4?token=HtdMqQ1S46hWzVepHLJHG5jCBDmJ3iasMxkboArj4NEEQ58MVz3-tqd2c3bMquyXtd1j-3ItIVm9MU4o1UOhr0HZYU4W-Atvm9BaRlddlqInzNOJRZkiMO70-yoaihMO_Z1-vUJB5xXwWMxWAT_o3Iw76A3TsRVTFtj9K0mMe2zaIxzMz6UAkZnEO9vd024m4NPjU4CYN1vvFiOVZtEcynYMtBclwhCO3HtR4jIcjuc-7uP9QTUx26rkS5dHcS0d5awRzZLC3l7lMjlnMvk2XJsss2CeCnvBb-ul-RLhYjFqRm2hd0hNMSFnT6ovrvILfjH8gYrjSVJJ477Ge7m6H1-uTSBZQG1l2fUcvP4PWiRUVtCUYJMizUmPk7txe6lbXafDxQUFrxIxmmMrihOYcwq_OKHJmnLqeyJpV4e_8q8tRUToOD7nyjK11HlhPy2p7O3FKsOGj1uklS9LKTHRUnKTsMR9oCHHHxf0jwUxKD14tsUWjjI5E1bPWM3tSyd4PW-XpUrfc3wQ5KY3pGWEyOBAGT0x14KwWoAK9iqzi-lq2Ii9DUOeUgiZ0At8AEPsbTcHVt24d7TPfsR-WAQhKNOSw0X6L1knlWvKIc8eIza8ksjeebCRB9XL7D5NOihzz2x6nMWxDTAtrdDBoHZ2T9hJCM_KRaC2SrhsAJmP188" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e657d4048f.mp4?token=HtdMqQ1S46hWzVepHLJHG5jCBDmJ3iasMxkboArj4NEEQ58MVz3-tqd2c3bMquyXtd1j-3ItIVm9MU4o1UOhr0HZYU4W-Atvm9BaRlddlqInzNOJRZkiMO70-yoaihMO_Z1-vUJB5xXwWMxWAT_o3Iw76A3TsRVTFtj9K0mMe2zaIxzMz6UAkZnEO9vd024m4NPjU4CYN1vvFiOVZtEcynYMtBclwhCO3HtR4jIcjuc-7uP9QTUx26rkS5dHcS0d5awRzZLC3l7lMjlnMvk2XJsss2CeCnvBb-ul-RLhYjFqRm2hd0hNMSFnT6ovrvILfjH8gYrjSVJJ477Ge7m6H1-uTSBZQG1l2fUcvP4PWiRUVtCUYJMizUmPk7txe6lbXafDxQUFrxIxmmMrihOYcwq_OKHJmnLqeyJpV4e_8q8tRUToOD7nyjK11HlhPy2p7O3FKsOGj1uklS9LKTHRUnKTsMR9oCHHHxf0jwUxKD14tsUWjjI5E1bPWM3tSyd4PW-XpUrfc3wQ5KY3pGWEyOBAGT0x14KwWoAK9iqzi-lq2Ii9DUOeUgiZ0At8AEPsbTcHVt24d7TPfsR-WAQhKNOSw0X6L1knlWvKIc8eIza8ksjeebCRB9XL7D5NOihzz2x6nMWxDTAtrdDBoHZ2T9hJCM_KRaC2SrhsAJmP188" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
▶️
عادل و جاودانی؛ دو مجری، دهه‌ها داستان!
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101637" target="_blank">📅 12:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101636">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ5hUl9cjlapW0Tw33AvrPHk37Jg_b8f9OLqAMMxT_mcBOoTKlbwO3wHCmHOU5Qchc1Y6va1DOOp-FrFaO_XaIlDSGr4bBl3YM-3MjTzoEWiCw9L7HVXbFRvf5Ds8Ayj-scBMmEvRN7iHxyYceF3eTPN4XGd3XhX6nBtuT4hdoaOe3JaGVwb1K-rKmWrg_4VEVqeZKEZ-aKpbGu05HdBYpyLeTqNSAdeeA5BX_0MFW3iSq66Uq8hpSHh7i07FDzlZbAuhnlogpEfVLclxgCMOXaeaKtn2p0qCBik0ky-iMwilNy78ndtrlDyokeaXA-WSGt5Jrjj0Vdmh8yOVsjlWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه پس از تعطیلاتش باید به دنبال خانه جدیدی در مونیخ باشد. او از سپتامبر ۲۰۲۴ ویلای ژروم بواتنگ در گرونوالد را اجاره کرده. بواتنگ اکنون می‌خواهد ملک لوکس خود را بفروشد، بنابراین اولیسه باید تا پایان ماه اوت از آنجا نقل مکان کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101636" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101632">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kS5y848SXOv9evl7NIne9BA9ENRvvs_piXSYxidSCLFvFRcw1tCF-5yn23VG8xesK_flpboQzaxQ_VMhB_ti2HP0yOqsFE9Y-uTWNQ01cOD41-xRzsu9BzDBn0K7RDzFZQqwjVTiAf5hpDZTgMRWctMixI-5d5kHVyHMOzwLconqHxo9nLJU4QUQHGO0xHFhPNeJDED6mq8b-m0qU7qrbtKDkkBJfAfa7UYFoyOF_mrHxQaFayq_R6ibjB42p2UZJTiIX_EIPSnhVQI2L6ClMLmGVLlVlXPrNbfBe0Inc9nalQdEa2pVFnJHMnoFME0j81LUXN3hju_6-nqJ4SrTGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWefBkHZoeJKLLEYmg3vIQzkVqrZ1KQUdyThS5PQS9ch8FbcLrgrENldba9a7EGmXgIvjqhe4q0GrUU47mNsyVHrJ2_qDGW_0tam5McR3ng-kDt3ek2MsHScQ-HCBzr66VxzspOSVRKg-Mkr2CZZjmYZuu1JJQoQvOfGggk3mrqXbBbLx_XC6ZD6RU--jKAysOmWo_tC3BKvc9hh5GAew9BP12l3swLTnma3-tCk4PtTsCfbQFj1Wzmur4HeSP4sEASu_sI548qkmrzYEV6bJdugZBbd1jECFIMcrxdU44YXprBoSjIVxuSKi-DpQU57FwmLzAKrf1n5xWfK4Ll_eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRyaZ53Ax19ZBuY6jmC5ObGF2Eiz93E0XxEws2SGm8OXkmRIYiNcZfT4swubTlD0--sAZcqOeHj0tWTy7dHVaKsiOnRakxeyKwaLpOtXt3sjxKSI_j06eLzmCKR9WQpPPpboD1YHbVn-OB0-hVcfcSva3J3C24Pp8A4-zs0J6OYt0bnHtLpzyo_0-Ka3CnAZwDvKuf3fyVm-9SC2XasSWjBf7W7FfblV7ZachYjNjhrzRbi0Wdr2tV_VTcGRz_up3edJ1yHWRYPlxX0H2F109eQS9D49RVOvfB-JiX9fU84nj9OskUjykzPzIp8T6Bobd1fm0V7MXcxKP2hMTqzr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0VMedGpnNsnPfMkVXPAOJerk_Jqf1phUGkJDjFRbrjYawfOFDr11aq3T6C5jYquvQaJA-ay9Izh9TuVBtIHpWLd54wg7hemHhsRPMPm23rq4NM8TFN104m5BMjXb8I8Jtw52YZvIjBSEJUUMasgioNhlIx_cC4RbArF6y3PKsHHLrBtmsp1a5jxoiHcAh9rUmrtWoYz6QEFaXHQMC74_Ib363rBXAV00wY2AxVgSKo56QX88gQR3LmDT__sLhos1HifHe2GSDPQYZTmsOrt0w9IdG96ss0OmfZQF1oGFV67H-0hB1fYtT-YC5D4jXGlWl8ffHg4G_kqd7pSsSEWAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
کیت‌لورفته جدید رئال‌مادرید که قراره فردا رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101632" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101631">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n83DOo3cqeodZ-5wIv66U-ekY2GZILbOeGlk10VGp87aR4aPemVKEFQ37qpLvmhTh9o9_rnhnAc0VM2lEW0HGho2ATYb8X-ZfH8L-WvmLM95kGKAUmMtFCQblvn08S_9KVZv4lxTWpMx_HPZExyzPdI_NC3RLeD7rDPhTTLJSw5gYj7zZ515jP4Cjtv7VK2d_XkJNP4bE2CDKiFiuZCCQkhg7ZVu48Mi0dlnL8yeUGQwcMXk8yG576I5a_jNLfKRYZPeQtf3sDibT6jGaSLPalS8LOUUeWB2darfh_nV2fQA2p6lDZ5BjAfdOHPROl7IkJXziGuB65o3CXzHzARrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
هواداران آرژانتین بعد از شکست مقابل اسپانیا در فینال جام جهانی 2026، یک دادخواست برای تکرار بازی فینال راه‌اندازی کرده‌اند. تا امروز بیش از 61 هزار و 500 نفر این درخواست را امضا کرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101631" target="_blank">📅 11:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101630">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZQAjaNzwgr2DU1dI5oDmZ0c8Cbp7BEnGzI8adIZActkKZnZyPbdh4u4Sr4nGDGmhetDTrE3s8Aj1kooclIiW1bq42hVsFn9h20Uk0mQKK2ts9RIui3RINDWRjdv0HZkRepvwPvscDOGkP2dpWwXUNc7pDCNsxbysilLj8eTJC0XcW0SOE5msnuWq6pmH4g-vvV-uWV9xLcCtteGs3o4NfySnieoa3DbxY2wkssE88yP-wqD10-V4nTLQrTfb0IC_iAF0ikMo8BYmcBgqDPYNkzLRwTxpUtth07S8PbY2L4B88qb61djPLFuJ2unPeSdpirMZILV2LvOhgoiF4CL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
❌
لاگاتزتا: پپ‌گواردیولا پیشنهاد تیم‌ملی ایتالیا برای نشستن روی نیمکت را رد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101630" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101629">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fde3785bf.mp4?token=V_7fw83h2Wh_JG-aOliwl_pPVtttZunSTchLGv83yqrx8kXEODhJatExKRda3ifsvAzKIDFaMBdMlVrBy9lamQBZnQwP-4H-3_uJOOc8SYt0-qFYwoZ2aCseXyeoHUUe6UHhmY3y_YFMdxLWC5OpGOjgmMx_uPyVDKCCXb3OijPoFCT0_2jh_9F8Q-AG4QcJe5vxB3y6SSRdGnJKRVIzsZQ8KeheOnD5v4IEwUID0V1EsE6yOCl2lKc-hhaE5s2Va6prLcoxNO8-MHJKHJyI4B6YUE0NNmZZYcvt-q6C0JloWQAEEhMhAzG5na-41Z8j7KerNuas3oi6TheBm5wd1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fde3785bf.mp4?token=V_7fw83h2Wh_JG-aOliwl_pPVtttZunSTchLGv83yqrx8kXEODhJatExKRda3ifsvAzKIDFaMBdMlVrBy9lamQBZnQwP-4H-3_uJOOc8SYt0-qFYwoZ2aCseXyeoHUUe6UHhmY3y_YFMdxLWC5OpGOjgmMx_uPyVDKCCXb3OijPoFCT0_2jh_9F8Q-AG4QcJe5vxB3y6SSRdGnJKRVIzsZQ8KeheOnD5v4IEwUID0V1EsE6yOCl2lKc-hhaE5s2Va6prLcoxNO8-MHJKHJyI4B6YUE0NNmZZYcvt-q6C0JloWQAEEhMhAzG5na-41Z8j7KerNuas3oi6TheBm5wd1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
📊
▶️
آنالیز‌بازی رودری ستاره تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101629" target="_blank">📅 11:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101628">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuRON65BMHpSK4XXXXIzCRkMuEhAAmcDLAzyVecUHYSBBpbKHhHmGa3QD1LeiArP3Kp-m_4P50WZRhdWipoel-c68sgBhlL0fm0TUpfhPMkBjoEIjmNZ6V86O4Zd6Rd3_iU29-Wxu-0evsY2h8grcXkYx_C_-Vrp524FU3qSEJdXJInOhi6AfxY58ulZMnMxdJGDgGKhnCXIMx31n4VXm9PDr51nX61a5riZtVhTLfkdylg_UvQPSME7I1ojEyk7Y9TjaDauKU9xVvg8EIlwTHSdjqcUkA5VStYwP1jN3jmQ-W9okcpwMb2WKpQxrtypn-15DPUqMf9PecB-kS3Gtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🇦🇷
اسکواد احتمالی آرژانتین در جام‌جهانی بعدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101628" target="_blank">📅 11:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101627">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbNbY9bMmj89xmu73f2WUUqoZWtxxFfNxxPSl3eG2MpIkVINjzerVqRZeWmPC_ybjg99b1JE36xZ4E_EVFO5Ckv0K-EidK221JYWJzp_EA5Usqv3CZYVD031R8SvidWsAIOyUbHaaGBK0TuaJMkUJ-h52cYGQbUEWz1Qf47CHjQthNPyfI1QpHApZfI5aiLNPaZ1KRbkj8xIckC8p7Lh4hYtsdv1WpzusY2Evop-l6P87pVRx-DQjWNM2anur_bU0zel3xufwDtmN1XrFfmzVzV8OJXt_qvac6yv5XuwM2-23I7C0u9R8Uf5xWhmr0HHxzPLg3uXNNqANuqdFv7cCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ نیمار بعد حذف برزیل از جام خیلی افسرده بنظر میرسه
- نیمار :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101627" target="_blank">📅 11:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101626">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezc6m6MS0zicqu-rkstoMWLOraDn5auAdSDcTqLoSpdj2585lMBEpK0FBKbV7lFWxiujmrBqjEWY40a7AR238Yxb87nJGRnX2iGck5qbyDotfkqXyZ4o5L0o2UUY5u_WMEO5sujW5bi-vwSAZUeyzdOmMeZKgBXbxHV001c-X2xpujzIJk3EkbZ8_dSwGS5DZNBw3kzXSL-CdS6615YIjnoWtRhKpN52xzj2xW_deXR6F66lbFEEObpLK2JPcKXBZ1IfjfC_tQub5X-yzDh9ENJrQViPxx9uLJvFH6lPEZUAMjB0pD7Y4dVm9GOLUFMCZJjZkExYyF_mo1Fk5C0ABQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
😢
خانم‌شکیرا و چنتا از اساطیر NBA
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101626" target="_blank">📅 11:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101625">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCyeBtKX7I0aNae-gKHJJCjrwZAF10qvKhUToo0ZCR7A4eC2V90exPPUkdY3-h9mCfF3C-GeH8a3iDFXyt3lxe5jB-SX3gB17K3dUIi1Rl5bLDdBSLlk4JasdyJt1j4yHSrSQNdcNfL3b7fvTY428ycOpvwJopm7793X-tWvkvp2xgLxrhvGZsIvNPWDxeIC3w4443rl30eP7EzzNsUzmzKOUrqiSlU-jnV34SnLqNFlzohVZuTlaQDCaY9M9BKSTdyC07jpzuULYyl7H_pzq6Cs8DCpUhjsnZnRH88Wi0HobcuP9ojNFgN3zi455A-tWHV03nitAOy0pOwRKE3OQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
لکیپ: انریکه و پاریس تا 2030 برای تمدید قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101625" target="_blank">📅 10:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101624">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9443946ca4.mp4?token=t5JD0K7jc_J4-N5GkSwkjsYpKcgPeI9ceuDDj6qaqBOSXKpwU43zyAkBUz_TyIs9sXgYGRAqMvMBSabg54pCQOzVx5GdXCq4h9A5tIvprxFB0HV7Fs3Yhye82CojfMQEjC1J3EsDluJWY8KcJ0hGLtnKqsOIHhwb-kzQ42DPDqLXSTTOP-v4RkR9XkcbN9Btpe4QGnIWmfs2T_cFNUqCpMWi9YaYEaSFO1JUB29IA5CdkSVRg7-T3NzfY45kOvIzwRC1L5vvr3LZGLIKlbTXeatAra4eNXqP1pn6HE6Lc0smfrURTDlpII34Xz_LcFkobzXUVGnJYwedkjiUkHs1Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9443946ca4.mp4?token=t5JD0K7jc_J4-N5GkSwkjsYpKcgPeI9ceuDDj6qaqBOSXKpwU43zyAkBUz_TyIs9sXgYGRAqMvMBSabg54pCQOzVx5GdXCq4h9A5tIvprxFB0HV7Fs3Yhye82CojfMQEjC1J3EsDluJWY8KcJ0hGLtnKqsOIHhwb-kzQ42DPDqLXSTTOP-v4RkR9XkcbN9Btpe4QGnIWmfs2T_cFNUqCpMWi9YaYEaSFO1JUB29IA5CdkSVRg7-T3NzfY45kOvIzwRC1L5vvr3LZGLIKlbTXeatAra4eNXqP1pn6HE6Lc0smfrURTDlpII34Xz_LcFkobzXUVGnJYwedkjiUkHs1Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
سید جلال: حسین‌ماهینی واقعا بازیکن‌نفهمی بود. همیشه منو عصبی میکرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101624" target="_blank">📅 10:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101623">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/509c49999b.mp4?token=RYw3FgLqDiP_O2zqU89xpms89g2I5Pe5fTOKOUm7Zq_HvWPUXtrVPy4Eg27_254sM6W8YnyKqugQY6qDi0PnVXzUb1LTKqa8u7dHm_KD6qWiIyV8j_hRhYJvlr09SxfDAM__Bntftd7Xsm3N9fy4cjsDvGn5JhqxsA4kEGXDjCFnV__OKS2zHD8zNFRUhfDvDFrHgkRn8TvZW1vt4HXy7FrVOMaQ_lbzmBDfOo38BsrPcUfOSIGie2Wc3ZMyooGWmEI50mE2YPKsK1-ssAUEE9SdE7IOYVFw-mquDhdtRqEBb9qedIB5RjUSltx-U9UBiUAAEiWbbSgJMsKRROt2VFWFlVLMoMAGzA3s25uKhLrUXS_d54vubcb4IonxClaDNBQOu99K77Oxsj6bvhcFaB218yjAUh992NBQ91BkXWEpBXYciHR-qDr0RuznIAw83XOe6WDtxl1lixmmKUBmEerw8SQbscx-nssHhNoduy5jeUTn8Do6oYayMAIQJTkzVtDzs91M_LAburQn6_oiD_-lXlbz5NC65JOJZGiFLKHvqmlw45oDv3zPYzIn7Ct1fFRKKAJHXt2v9XvuvHDFBv3P7Ya1zC5pQDoGenT0XCB4Fg6EsfpffZuE-C7TI_-VOC_gr-jkcs80G9Bfa3XmG04wQ_-Nzkt3XJSQp70cpqU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/509c49999b.mp4?token=RYw3FgLqDiP_O2zqU89xpms89g2I5Pe5fTOKOUm7Zq_HvWPUXtrVPy4Eg27_254sM6W8YnyKqugQY6qDi0PnVXzUb1LTKqa8u7dHm_KD6qWiIyV8j_hRhYJvlr09SxfDAM__Bntftd7Xsm3N9fy4cjsDvGn5JhqxsA4kEGXDjCFnV__OKS2zHD8zNFRUhfDvDFrHgkRn8TvZW1vt4HXy7FrVOMaQ_lbzmBDfOo38BsrPcUfOSIGie2Wc3ZMyooGWmEI50mE2YPKsK1-ssAUEE9SdE7IOYVFw-mquDhdtRqEBb9qedIB5RjUSltx-U9UBiUAAEiWbbSgJMsKRROt2VFWFlVLMoMAGzA3s25uKhLrUXS_d54vubcb4IonxClaDNBQOu99K77Oxsj6bvhcFaB218yjAUh992NBQ91BkXWEpBXYciHR-qDr0RuznIAw83XOe6WDtxl1lixmmKUBmEerw8SQbscx-nssHhNoduy5jeUTn8Do6oYayMAIQJTkzVtDzs91M_LAburQn6_oiD_-lXlbz5NC65JOJZGiFLKHvqmlw45oDv3zPYzIn7Ct1fFRKKAJHXt2v9XvuvHDFBv3P7Ya1zC5pQDoGenT0XCB4Fg6EsfpffZuE-C7TI_-VOC_gr-jkcs80G9Bfa3XmG04wQ_-Nzkt3XJSQp70cpqU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
به‌بهانه صحبت‌های اخیر قلعه‌نویی؛ یادی‌کنیم از روزی که مایلی‌کهن با شدیدترین الفاظ علیه سرمربی فعلی تیم‌منتخب ایران صحبت و افشاگری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101623" target="_blank">📅 10:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101622">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1802ff2c96.mp4?token=ZJarrBwbUI_LYYpUhfov1c0oTYecsD6du9Jax2UKo3hZPJHy4485x6Th81iXHRgpHHkAc1e0JJc9NCX5yqtraVvkUfZEmD1nnQ8-GPSs7qeqLQrzr9pjgttVoX4C_Z3vyzxOpWm2fU0LuoE9hOKfnPHLMd3UfVRJDuv--37exHtTBgteP144c69ofOfqdVjIw8uDV_CNLRzNbhL5Z0irDx1AUm7zzwtYcag0pFewdgbmxIwGAii7FqTdM7kvuQM7UjefcaRCX749IEQ7sw1s_vd8SRMBHZmyMrQo7bUQg7vxm8WHm1JcZbxtsCrC9QQnnw0eZI0OoqxynJ7f5ofgBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1802ff2c96.mp4?token=ZJarrBwbUI_LYYpUhfov1c0oTYecsD6du9Jax2UKo3hZPJHy4485x6Th81iXHRgpHHkAc1e0JJc9NCX5yqtraVvkUfZEmD1nnQ8-GPSs7qeqLQrzr9pjgttVoX4C_Z3vyzxOpWm2fU0LuoE9hOKfnPHLMd3UfVRJDuv--37exHtTBgteP144c69ofOfqdVjIw8uDV_CNLRzNbhL5Z0irDx1AUm7zzwtYcag0pFewdgbmxIwGAii7FqTdM7kvuQM7UjefcaRCX749IEQ7sw1s_vd8SRMBHZmyMrQo7bUQg7vxm8WHm1JcZbxtsCrC9QQnnw0eZI0OoqxynJ7f5ofgBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
مهدی قایدی:
۲ سال دیگر قراردادم تمام میشود، اگر آن موقع استقلال من را خواست، برمی‌گردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101622" target="_blank">📅 10:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101621">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db54c4d205.mp4?token=cRJpPdDQIpJWQh7-FIAtVhoYJdxquLmjZnFu1YkGMMAP2U4bcNurbztOYeEvnPLNkEvyyel5CXFUhbGBQztUQxHUrocjVqT-bdPAbJ2uBn3kNol8Is6oO_Ni-R_9jl83kAPMmUg6jZ8T6fWm674nTDjEI4qLyX0MzflqNMrj8If4xBzzZQLzDdTvrJHHqt362Pp8CUa3q2NhLjcNamMg1HpU53VnMSv5S6_NfGepPJ-gUechNeslO97AqoXNrR97DNk4ds9z7NPNOQxfN-PciaSlCT2V5M0tkfO9qXEc4bUAKvnRLsxLu-4Ov1yhM3Kz8JnFGoQ6wAKjzkcsvhz9qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db54c4d205.mp4?token=cRJpPdDQIpJWQh7-FIAtVhoYJdxquLmjZnFu1YkGMMAP2U4bcNurbztOYeEvnPLNkEvyyel5CXFUhbGBQztUQxHUrocjVqT-bdPAbJ2uBn3kNol8Is6oO_Ni-R_9jl83kAPMmUg6jZ8T6fWm674nTDjEI4qLyX0MzflqNMrj8If4xBzzZQLzDdTvrJHHqt362Pp8CUa3q2NhLjcNamMg1HpU53VnMSv5S6_NfGepPJ-gUechNeslO97AqoXNrR97DNk4ds9z7NPNOQxfN-PciaSlCT2V5M0tkfO9qXEc4bUAKvnRLsxLu-4Ov1yhM3Kz8JnFGoQ6wAKjzkcsvhz9qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
سیدجلال: بیرانوند رو مخ‌ترین همبازی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101621" target="_blank">📅 10:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101620">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvU0zA8VPoRNCfyzYs_8pnqxHRxpBUE1SGtETrHngcwyEawLhXEBh9RfjRSQmOyH4ZHVa5kV2-E91sy9O3qsFsQvR43fHOuTuHQabuJQBFqLaOJxACwRZo25y7M8jYni4k7urd3GdTU5ov4K8oScCoa0yMybGFvtrUSs3Cjz5B0g62IkSnPL68uuuOslzHlXJcEFoK4nMEhnAcjhc-CQ8RPIkdVgrbE2nZFdUKng55Vw6W3LN1rPpt6JZuTNf-ycgwazTbpTC4RRdAdfd66qDZ2lfx5oz5p45bx73YnRgN8FhI0zWBEF4R61lF1IosVQ92xyOzLph6I424qaltyeNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
استوری رسول خادم برای عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101620" target="_blank">📅 09:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101619">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46845c1eb0.mp4?token=t38Pruhybvzf0zEYEJs6l-wwxRRnoaq_jbx3Vj9VfVoAMW7hVQkp71JbS5ul7CPl4vuLju_lcausfS3OA8SvMkkS7dY2eo-oMaryVOQjIAqsTX2geA2MPIkCkv7GIEb6o8QtIG23k1iZgtIlCl5VRj_hRHGNO55AScLkCu0T7py8SuvcLxx6dHLeq0qH-_K8OfQB2_fHQCfv_75ZreEq4EeHa8vUvKIoomDgheU5_eefxRQhusfA1SPYwMDusiN_zb3yR2pE0mhjr0h2TgPlpYWLY_6slRbAM7vd_VD7Jv8puuoPKCaMqGEFBAcP6ovLU62FVnBmlc65Y7hprzA9tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46845c1eb0.mp4?token=t38Pruhybvzf0zEYEJs6l-wwxRRnoaq_jbx3Vj9VfVoAMW7hVQkp71JbS5ul7CPl4vuLju_lcausfS3OA8SvMkkS7dY2eo-oMaryVOQjIAqsTX2geA2MPIkCkv7GIEb6o8QtIG23k1iZgtIlCl5VRj_hRHGNO55AScLkCu0T7py8SuvcLxx6dHLeq0qH-_K8OfQB2_fHQCfv_75ZreEq4EeHa8vUvKIoomDgheU5_eefxRQhusfA1SPYwMDusiN_zb3yR2pE0mhjr0h2TgPlpYWLY_6slRbAM7vd_VD7Jv8puuoPKCaMqGEFBAcP6ovLU62FVnBmlc65Y7hprzA9tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
صحبت‌های جالب علی‌قلی‌زاده بازیکن تیم‌ملی درباره همسرش که فوتبالیست هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101619" target="_blank">📅 09:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101618">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ae48d98ae.mp4?token=pk8eGC3lr-5tUQ5UT6xLTvCqDcQXpPNlbcRfMJDurQvURVFLOojhxjUT-SQtIA-1ZwrI-dujzwZ1kR2So7yfZhF321FvlrleE10ndw_j_YOeRx6KvNcuCrdHwibv_Nsb9zNfNzI-YfS7H-VmPSZoZsRiFp1FGhFMQJYV_h4f907MQ3SOn_xX91heSH41sCRqvBewK9EAMlZLBvgxbPH4vpwj_HmYGLXag7xuEllnu5gSmrwdQPlVqA-16E0JK23K266R0I0dxku6CiMIm1xxMjXcrIXqQUkaBBwqAfP5SeLl-0U1uaMauSB4sDqXtwW7wn3JD7cJ2sip7cMSCIfVIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ae48d98ae.mp4?token=pk8eGC3lr-5tUQ5UT6xLTvCqDcQXpPNlbcRfMJDurQvURVFLOojhxjUT-SQtIA-1ZwrI-dujzwZ1kR2So7yfZhF321FvlrleE10ndw_j_YOeRx6KvNcuCrdHwibv_Nsb9zNfNzI-YfS7H-VmPSZoZsRiFp1FGhFMQJYV_h4f907MQ3SOn_xX91heSH41sCRqvBewK9EAMlZLBvgxbPH4vpwj_HmYGLXag7xuEllnu5gSmrwdQPlVqA-16E0JK23K266R0I0dxku6CiMIm1xxMjXcrIXqQUkaBBwqAfP5SeLl-0U1uaMauSB4sDqXtwW7wn3JD7cJ2sip7cMSCIfVIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
سیدجلال‌حسینی اسطوره پرسپولیس: رپر مورد علاقم تتلو هست. بعضی وقتا هم شایع!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101618" target="_blank">📅 09:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101617">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKHmOMeFnZsPJf1T-_7965mZmVBdskzFjU-PlbUekMGDlDP9CKnJiniqaJmz3Y5gziu7D5UyCb2PcLsCL91FMwsZiP8lS9ir-jgne3ygqXhiOEdpg9oVZFIn0Qtn5Pa--GwxjmPnQgGAar3cq360af2MOnxKlPteTGu4ve_AUPVYfS_GVwEsAO76K3gnE367hdlXEeKRhd3YaSf6q8Blhyxz1xEjhKpNQxJrEI9jkFuFZ4tJjxW8rx02SMCVidJrFlA-RpwEFK0HflxA5SyUECRK8K06q5AOhrmLCMpg-3K3ItfzJq_7nAhY4dnq5nkNZj5y351H1MO19RdqT6P2Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🔵
⚪️
منچستر سیتی احتمالا مبلغ زیادی رو برای انتقال رودری به رئال‌مادرید درخواست خواهد کرد. حتی اگر فلورنتینو پِرز موافقت کند، باید دید که آیا این انتقال از نظر مالی برای رئال مادرید امکان‌پذیر است یا خیر.
🔹
🔺
رودری هنوز قراردادش را با منچسترسیتی تمدید نکرده است، زیرا منتظر پیشنهادی از رئال مادرید است.
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/101617" target="_blank">📅 04:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101616">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2512ad65.mp4?token=WVUbEt4b0M7-xtQGt6BBDXFzdbnqJB6pBULmHpUNX0q10cPtCH-H1SvFHUIYPg7WLEdifWCQjzuyhfPTtruabJqaFrScON8OnZpw9oMz61zWsx1M8JmnLD9cp6q4nFLu4eWNcl8_VpbsrBTCclfpeaz5Ek4dETMGriiVS2lHAK4LpMUrf0IDoAfwVrveYhyn5a7GAYHLIcgQzPGMQXg505qgjrmaSpOyQaV3Iadtme7fdocjnth1QoKvVwHATF8d8vfd5pT6WJkt8BVLFl8tpI9B2WkcLTkwLKNu1lfjZFk3Js2oviQt-6YQBCi9pPeRe1MWXODl4ZhLNADsUJ7Lqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2512ad65.mp4?token=WVUbEt4b0M7-xtQGt6BBDXFzdbnqJB6pBULmHpUNX0q10cPtCH-H1SvFHUIYPg7WLEdifWCQjzuyhfPTtruabJqaFrScON8OnZpw9oMz61zWsx1M8JmnLD9cp6q4nFLu4eWNcl8_VpbsrBTCclfpeaz5Ek4dETMGriiVS2lHAK4LpMUrf0IDoAfwVrveYhyn5a7GAYHLIcgQzPGMQXg505qgjrmaSpOyQaV3Iadtme7fdocjnth1QoKvVwHATF8d8vfd5pT6WJkt8BVLFl8tpI9B2WkcLTkwLKNu1lfjZFk3Js2oviQt-6YQBCi9pPeRe1MWXODl4ZhLNADsUJ7Lqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
⚽️
خاطره مهدی قایدی: بیرانوند خیلی خسیسه. یه روز زنگ زد بستنی آوردن خوردیم و خودش رفت، گفتیم چرا حساب نمیکنی گفت فقط دعوت کردم نگفتم حساب میکنم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/101616" target="_blank">📅 02:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101615">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXaRNbl_vKPORiwIio9rZP5XiyomdFM5-7JMaxasIyufvr2sFyIn20sd8D40cbUznYUU9lU2-TilUcydGHK1HKq7yvgTlz78KbsucaU6qquxRHEOsKyaYRrbJOW7FrF9qaeiBy6gJJuWSI6PxZMt3BjxphvSeMgrpLJbZStg1Anc2820txPLI7WGhCMtFuZGmryIXbCQSHmY62rfU8qJ3OSSklTC9aeXRqU2u5Uvm8CMkFBTCtgBG8I3WxA37pMzFEWO6lkleQddqlvngeIrGThr9gmWMPHbpgoo9DvgsMaXTlSOq5WntjUAbSRblyhGHgp_QjSwjufoZx4mgzR6EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
منچسترسیتی درخواست اولیه 100 میلیون یورو برای فروش رودری داشته. با توجه به مدت‌کم باقی‌مانده تا پایان قرارداد این بازیکن، رئال‌مادرید می‌تواند با رقمی کمتر ستاره اسپانیا را جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/101615" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101614">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvNOZrgo7UcRqZnLYCdLkA2ykqjNoqChoXwskqkS7WRjZFzCWhVKroWfBYCan6cjGfBxLB0uppkU7Qi3zWViCmiWXOx-ys8x8KBTOxLIxzM0mY0YyLVseeV23_D_-c4nkcFmxFebc7T1fcmwTN5srOl0psev1byrkGMNaqS-Y-xiCqgWLsebDdP-QX-a4f8Ua0aQd5xpvQ03gq1hPsmi_1RtkaIDtJaRC-nmZdBTkGcP10rA9MCKQul9kCZS9oOB11CJ2SWJEpwz_oS58S009sJ4G2NxYHhxNAjk8eFUPwD1Dn4jQKUSzbKrRBtTMSrZoTtxAvG9259WP0HCyoyXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
منچسترسیتی درخواست اولیه 100 میلیون یورو برای فروش رودری داشته. با توجه به مدت‌کم باقی‌مانده تا پایان قرارداد این بازیکن، رئال‌مادرید می‌تواند با رقمی کمتر ستاره اسپانیا را جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/101614" target="_blank">📅 01:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101613">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TY9lqfODgUs9JLPIQTY6TyfCQR3bgAfrxHG2BEUoJ0ajYhhRBPOQTIYwZC4zXv2f2LGEUuaeo4XJV8eDz4OhXj9SjS8ZTYDKAsvd5mZf-V5RcqAyeKgdVVVlKHM9sEcWb9R8_jMZ6-BxsVKGHoO3YfyScoickaLW6JnZMFgcqb6eA0OUVHtURQVKn-P-Zs4iPAMPVU9nbKxkQYQr79ZHiQ4EhIO0KRvuXlsFyu6q1Y4Q8DXXsFRwS4YysNdydKXRC1XCIglbT49RX__tfWju9us9FSFyjX6uxBM9wY1EUDs2xWVIdWj4ChVUYKtPt4I0iOpYNU_SV66kCitr9aZBYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام از تبلیغات تو جام جهانی 22 میلیون دلار درامد داشت و شکیرا 17.5 میلیون دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/101613" target="_blank">📅 01:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101612">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPkMGpzqKXKxvGMsKZuCsNSFqsnMIl4N92oIcwBlND7Kb8-hSf4V8KV8mcQZv1I1RypZcUmFqFbWh_94YMttMGDdjyGOgD8h-knMcOmqcBNdZLjd16NewbM_p3O4CztS2DCe4wlGtmMax31ss98quQSwnPKS2i0DCWdDOK2ajeh9DhOO1FpyratDuJwEiq265NFoeL4gUjAZOsCBKs4ZaC5Ba-AvI6aIOy-X0O_muI4naXbtqsSc5Aboi30tdbbU2KVh59QnHfbh4AntqQfhvri14uT7yZTLvSwoT1pb-Da--VosVhXjq5Ua6HblITIs-67MdRfcizfdSw2kvfCQFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط 3 بازیکن فعال حال حاضر فوتبال این افتخارات رو دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/101612" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101611">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-fS2oT8AEXhLY3x2t9FEqDzhuSYJ1PHAsrzDsEq1qiFkMVm6wIE65pK6qz24B23NsHR6AFaR0Uil5gtuZODALbgOrCXGDxG4nx6tFza8LsIgC8YhX9J3-XcQgGXvJPbpEzeLSDnXzO67iRUBrxloBx4hGVKT1TeTsPkmUsG4nhne5y0uPOEMo7rUmMlnJTVDOtfL1gHuobey9H4E_zSGvUzfWooaptKKXXwy87yAgbf65zzI3Jv6o317ZWPeRpqPVG7G3fw8n4HZl9V2aIyuijI0GRoPxY0tsNvpyl6LVOpknJ-ep3cauBq01NK-c6jhKpbskpx9hcwc1rGAk1_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/101611" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101610">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NPng-uf61HS_qh0b5vkzLzuG2k1l-aYhTYNxM_6xvA-zdbounFngbHkVT5EZwUrjP4_xP-R8z8dAdHzHQoumyVvpTW5CivWBBee1FYenv47Hx6wycDPicvli9jPKy5tsRcWAgaSg59ifcCndivwkRLcSLzeSCiEVTnKh6hO7tExDiT6MKh45hPBVUxTjJgHdL0UhrNlhSN7CKDpKWNekz0KXn2EmTXRTtDvMG9aRVdMGIhVXgiR3V65a3IoTcZJ36S7XmLLOxhpGXQtz5BZYB8EXtji0yVRJ6EstSSeKL4jbpOfxoUp8XLF7aVqywKCql4CCcI6KE6BHbQFurxlg5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
کیت‌لورفته جدید رئال‌مادرید که قراره فردا رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/101610" target="_blank">📅 01:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101609">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
⚪️
فووووری از پپه آلوارز: رودری با قراردادی 4 ساله به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/101609" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101608">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DexPXy9aj73ZjhNPBusiT2dYh7Qqz_ZCR7SZbU01tkHdjDdjr2mYkhNoOgc7fAKLrFgJ9yZnV1iHFfR73RtTElXTzkW1Tpi19o0Do2DQnIH6_zjk6NYc5i7ioNG4sXZw-ZfRJxEe7UaK7pWzJJ6sZRopG3pcYhcUqF-4dO5zpdOG490lbsHGTMwSZwDK5qOqw99GLIW83LWXQcBPprFVkovDaaM8c-1oY9pQgRVxJKuEYlcazz-9t6GqC0vRoP0rdIlcFQR-MRHZgLBK5mkorzBvpMWQK28ZnznQbARBwyFOasxK8eFgHvHXSLVYCsmBEumftekFX09Y1biZxn7wfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
والنتین بارکو با قراردادی به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/101608" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101607">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
▶️
👤
حمایت‌جمعی از مردم فارسی زبان آفریقایی از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/101607" target="_blank">📅 00:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101606">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی؛ باشگاه آرسنال رسماً اعلام کرد که با کریستوس تزولیس، وینگر یونانی، از باشگاه کلوب بروژ قرارداد بسته است. مبلغ این انتقال ۴۰ میلیون یورو است و قرارداد او برای پنج فصل اعتبار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/101606" target="_blank">📅 00:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101605">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HDhC0bHkd-gGTvZHsLt7rM3YTTKq8wDlzpiWegtEeRkicRppgpDiFT2Yg8oWJvjZkKDZ1MBspaRcodCR6fOYddBMbTQiB_MTX2N_YXktllsI61NO368APdiE0_uVNFnn2BqmOa0oQuE7xX_5IC5wZiT9kQYtpgPL5-07PJDbxcQ9KvFPqffKrl0sofPZzFzjoQyEf8-D3RoEB5vwuG7LHn46asmepwsmluC19Uqh3Xxwk-PRfGnBozIlXqV1ID5TWcPys29wMrVAelQnOb4cE6DvxdCjSXKnusbL0jss06UWY0a2L9TDeKIkbkj_AZrkzs7tAlLcx36aWVT5vUf0Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ باشگاه آرسنال رسماً اعلام کرد که با کریستوس تزولیس، وینگر یونانی، از باشگاه کلوب بروژ قرارداد بسته است. مبلغ این انتقال ۴۰ میلیون یورو است و قرارداد او برای پنج فصل اعتبار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/101605" target="_blank">📅 00:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101604">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ot0mEmWZR278V8fyoCG_t4NK5LdoRylCixncEuwotcDLcjXmGciIC854NCEyjniOeIe5uQZjT9RbQTzzM5REtQGerrJZp03RHZPBpLMrFlSjXIz_wHJ-0OjQHnQ70kngbiFB-wS10SphDg5PXsHY9xYNPnUNZnkK9Tkw_5WniFr4hzf42Mskt0eTeePY-AAA5SFVnx5EI8cgWNXLBc1JbPMBoE7McNw6ktqql2In_xFHJDv4aT3AlieGB7pa0HpiAhAuuvMBXFLFScQd4wHelifqL4cAFFJMLbsjoXTbbdnAQVQVJDo5Ck_j7ekK-yc1SYsJo1NsZTwsVKWYAoKdbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
ده‌مسابقه برتر جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/101604" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101603">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r2d4BLg9QkzbjI2C4RjWTSo15VHW8MfDgGvmw9Cx1R5ZuT4UCTa8XbbVrIMxUBQPBmU1Vn6_Jsdv4Qrh1pqN5Q3mIkGGPmom_Q701H3_XsvWi0-sHrfesueZJrWK_ZsTB8ivO4sFfNji17RB9XQyY9v_KWtG5Us5N1xV9Y2KEkYZ4OzIwGtsG24Q7ufj6ZIhKIppCJ2DxPttDQRNarDpDyER_55loulQYY-NpGAIPE_Pdgds5EZI67PQ99_D15h0AKqqzXryVgx50GElCRMDCxDtt9i1rR48B-ha0RcabV6jEGlu_Hg5g4Q5OSima7EHVZEIze7AHtfQycBB6M2oSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بیانیه آرسنال: ویلیام‌سالیبا به دلیل آسیب‌دیدگی در ناحیه کمر برای مدت طولانی قادر به بازی نخواهد بود، اما تحت درمان قرار خواهد گرفت و جراحی برای او ضروری نیست. او فیزیوتراپی خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/101603" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101602">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfupcJZfOw9eMX9QBDiYtlJ9CchmgaKF7mw-mA-HFg8ecoyIMugeAXlq6QCZQviVkqZpyjCwj5fR6SLNCH0ec2jUhxft-WToIi-3-R13OQOyOhQeWFNsmP1iS8S7e5K9DtE7CvvX4683K74uQClKAOyJzWiE4kH_i0GoBjDpq5YcAU9B3J4AW7HD644Gs6BT5wEyGCU-wiORaZhdGH0cUPlyZ_5EXZDGMQ1x8n_J1odyQZ8gdWfQf9u_O3DOVOnu2Yk1ibcOwVM6rIXDl9E8fTZskVAdOjW-HdcQTx5DHPAw2y8VQSNeSUVEdXBD4DCzQMNce8vau1wo2sZGcesFsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
توصیه‌مهم صداوسیما به مردم ایران؛ فقط کاش تجهیزات هم تحویل مردم بدن تا خوب بزنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/101602" target="_blank">📅 23:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101601">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-0quQT3u6M9kd6I6UucawJHX8Da05Epmrgxa58H7npsrCi28_lonDPJsRMfEbPJ-0uK4ghBfIENGiITpY5zf8BJ-vcHo1Wb-24lgPz5GR_iTs2DcjXjfNTe6LXSy6gv-axVRaMfp5_dyGkR2YxIoNR8qcfOp4BOkjV7x6ceZTZ86VNYhMAhXccVmHwzlYTTgtRjeTbZAThPku_RinNBXHxcF2V0AI-i1Fjyg4jkugtsZVi-ZDtk8DgOBUeKrPWam-2MSinDppX0GkeNKZaUe1L1lW8gUZ62Ik5yfqHv951OXf5ipIwgB8gQtwgwuCJwJRAaeSD-QQyXijprEma3tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔝
ستاره‌های حاضر در لیگ MLS آمریکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/101601" target="_blank">📅 23:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101600">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQ7ov3OSwBCpahJu-odYlPWdCCCnY6m3PyxamneRRJqUccLYf669W5SoO3VWtUrr5l3leiO-Fd2_nPyEJSt4q9I62ugny2-DRCr2OBgd0NzjuAKzs5YRD6sqMTRZoBeJg-l-L-WXHFD03ycQlbHLarnpuvufmn6oVjOuPGIMsrkhof4Ui5SuzkobrE3ucXD7kM8ZrZzz_IOd9cQuIBqXL5Pb30ncYG3WQOUZCDQd2ecOVM-fkpbkqfmbvStNyiFv5d7Nvnuj_ARlwmWRm5uXRd79SJkWkHZnSXLLcXVDjczKQYYLc4OCA2NcazGtLVUZfwKAqjF-AYvzor1A6XZ2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فووووری از پپه آلوارز:
رودری با قراردادی 4 ساله به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/101600" target="_blank">📅 22:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101599">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEgCWH0GnbtUu7Op0tmj3PvqHCpOw-lbsKlYgIQPXv6x5-LC0315GgJTI8Uev-cGq_LAEPHpnp1C-StfxXpkJaCt9n-9rfPnUvXZkd5sZDG4g2FUB36qpT_cSSDsjpqd4kaZ36h-PFF5t9A6sjMx_i4o1GuwRnoC_4J3TrCn4aNn7_WlnUNpqVHB_3dt_9HOa9kXMtZTEz5b7emKvmKv91hA_q2gkUm2DPAiAPJSYMssu8LQxRzUzw4NBo92HTCM9r3R7nYvOzS8NCQa-UeubLj0lD5Iy7v0ljIfYXKrLZXc0GrM_ullzwLJscXFwkPZF18VsMeSpfKTFUax3RNogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووووری از بیلد آلمان: کیلیان امباپه به فلورنتینو پرز اطلاع داده که موفق شده مایکل اولیسه را برای پیوستن به رئال مادرید متقاعد کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/101599" target="_blank">📅 22:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101598">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtb1GGACjmsEZgXD1ZpWsldzQcQ7g60qnb8Oh6JuBdGjPvTv61PxZ2-2yKG-nr-tMFmd533zqyXh1Y99sKqwhM3H2vrZBy-VOgpCMDQfVXqmvgdW3UtxBK5AEGs_oaVDR0pMYLUP8Hylgl7GG5iR0A0FjUbqN3-3WriF9zCTW9uZJtzCseSAUH8H_HQ7viRUurADObkc6g7xPmCa4Ct3lAEW4iDPG8gAOoWkSgE5B06X7TBxiL5fHWaeKY_nq7q4NJxbFndCNTJpdrCAwJHr0_HmLOsjxt49K-O_GaI5x-XJuU74yKm5Y4aIBbxIVjV0FSjNU74oV7te6iGFCcL--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکلی که وینیسیوس این روزا باهاش سروکله میزنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/101598" target="_blank">📅 22:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101597">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9RZcAV1AUVJCuPTshxb8yYUD0SaAlNu-yG7jy2T5dfOP61OdyPXXZ_NPQL_rx5NO25HFMAe5BSK-NOqYRckOC91HLDnkt4YIWjcDKhljtFhqhME--0zdyytO1hD2ubBsz5__SzLMIwkT0eXffXhDt6RprxGDyN-tu6hJCvwK4eoGZr-F0Yl2oHPISKQ7pYcJcdWjOnYz2Qfw3WtYYwUTyrOVpgy0KLh_BqES6bA2_J-OOHyT2lRK-Gd3piPwTuB3TMRvY1MtjPGQgLey073isMoXnEYe3s5VFVL3Sxv91xjwXzexjFgYePDmqW5Ow9_sBJyntcoAD_QH1gkNuMXog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فابیو کاناوارو:
اگر من بعد از قهرمانی در جام جهانی و کسب عنوان قهرمانی لیگ، توپ طلا را بردم، چرا پائو کوبارسی نتونه این کار رو انجام بده؟ به نظر من، کوبارسی فصل و جام جهانی حتی بهتری نسبت به چیزی که من در سال ۲۰۰۶ داشتم، پشت سر گذاشته. فکر میکنم او بیش از هر کسی شایسته بردن توپ طلاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/101597" target="_blank">📅 22:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101596">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTo8UiXbrQSEeXsLhcHjMPON6cCFCWdl7QKq1AImNVSEZmnsCxh_FE41dxFpzY1vVNohRs6DlMG8IbqUzjFaLlW-UAXEA9EfQDwtyQg3UABe-FBohozsI6Xp0AVQWmDugKxV7J1Fo3oh-swT8lTVyPHexe2_C39FHErn9vXCQYDQIQCpHqlyepLg1WI6JP6u2E2ftX7eKKonNqtW0LKmqBMlQyZFg89MUAa12dwTJRnAgeFQXvUd_u7rQaCj59Y9ahIG0iUWK05WXvi1wwZpi64OPx31QXLv0fifGTWhmw28a6MICBSBvr8Burolt4XRRJqHOuqSMsGtO90DDgRn0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🗞
رومانو: سامرویل ستاره وستهم با مبلغ ۵۵ میلیون یورو راهی الهلال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101596" target="_blank">📅 21:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101595">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNaf-ylmlic3quReONj0hLnPe82gQ07SGkl0TSfIfPNRbz_elN8fNDGEbbsixNZQyhpMeZ5WkfYzJ0sMdh0s7VQNk1J3yvyQ1Ao67bzsShncyMi_V7o7NK1pa9amMgz4-nHyuk3fY_9_0jwBv5HEqySTqCNezpgXA82cg0bpHqgWTd5ZFazL9CYPgk7y9XazDeNeQRfZjOMzF6_3PXiJSykcwuT352DWCW0mcvpmiYYN2tAJPoeAlz3jV2CIhiojW3xRbyz2hYMzJGBE6Mos0OhQHAGhXaK8XsVYXLwewCTh2cmkdcPWj-AwzUSHl_1T66ixJcnKy-fsc26yBc-fBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
لامین یامال ناخواسته بعد از فینال جام جهانی یه تبلیغ خفن برای یه برند لباس جور کرد! او چند بار توی بازی پیراهنش رو بالا زد و لوگوی برند آلمانی 6PM رو جلوی چشم حدود یک میلیارد بیننده نشون داد؛ اتفاقی که باعث شد شورت‌های این برند خیلی زود بعد از فینال کاملاً فروش بره.
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101595" target="_blank">📅 21:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101594">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vn5WvDscJCpnKC0wzNO-Zzvp9jZCbBZ6OMdSfIiqFB70U0GGd-nMiMNRh0iZpKtGLx1BsrjzymM9_kzEtl2Lw_uhSv-YIlcXidoQixX68uzLrZ-O4jP6JmWwCMAZc51jx_6yf4j29lg8zbS3QpSIY3r3kvLPq4sEXTaZTRUc4rBOTuIR06MQWA0wV22ke8GbwOzRN33Jp74xDl6_1nVP2rgtfaksWfv0L-PTcPYyGaiQ79NqKOgIWOWqd0Do2PLUOhn-ic0F-RE4d-KkBzX4-kyGG36jfIWDbW4V0-N2G_HXjb22mq0Ghw_a1LpRktojujXtNv56x8vijxj-qaxJbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶۰ سال بعد، او انجامش داد!
✅
📊
کیلیان امباپه حالا:
⚽️
🥇
آقای گل جام جهانی ۲۰۲۶
⚽️
🥇
آقای گل لیگ قهرمانان اروپا ۲۰۲۵/۲۶
⚽️
🥇
آقای گل لیگ داخلی در فصل ۲۰۲۵/۲۶
تنها اوزه‌بیو
🇵🇹
پیش از این موفق شده بود در یک فصل، آقای گل هر سه رقابت باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/101594" target="_blank">📅 21:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101593">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
#فوووووری
؛ دیلی‌میل: نیکو ویلیامز ستاره تیم‌ملی اسپانیا پس از تعطیلات احتمال بسیار زیاد از بیلبائو جدا میشه. آرسنال از مشتریان جدی این بازیکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101593" target="_blank">📅 21:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101592">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76aa3864d3.mp4?token=Q3LLRIAVnH3gUTidoSKGgihEP4FH7J2_mG2msVJtyY-jAtCKeE_Nu_KdrcLuVkiZBRVrZig88okNIFPv3-vP1N8L-XI96_0VzKPPfIf1k6ytlEma1Fty6sWixUfSa-7tFTbUq8qKSuWcjpFH3G01nue3fmgrASfmWua95dzDDihtzOu7BGGM2VEGmrgZnFbXh7tn6PJaP4-WTR7ZxjQLkICKEzAUgjYZixHVWiduSsabCS9AN8MMY-vNFqycOCZWJMRPyIIZyAMDIU33_5w85xOlCE0BvaQA-TMXbL_I74ckVUHFGSwC00CLtq_dCNT1qtqlYeEeI5JFRdZm2d112g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76aa3864d3.mp4?token=Q3LLRIAVnH3gUTidoSKGgihEP4FH7J2_mG2msVJtyY-jAtCKeE_Nu_KdrcLuVkiZBRVrZig88okNIFPv3-vP1N8L-XI96_0VzKPPfIf1k6ytlEma1Fty6sWixUfSa-7tFTbUq8qKSuWcjpFH3G01nue3fmgrASfmWua95dzDDihtzOu7BGGM2VEGmrgZnFbXh7tn6PJaP4-WTR7ZxjQLkICKEzAUgjYZixHVWiduSsabCS9AN8MMY-vNFqycOCZWJMRPyIIZyAMDIU33_5w85xOlCE0BvaQA-TMXbL_I74ckVUHFGSwC00CLtq_dCNT1qtqlYeEeI5JFRdZm2d112g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
در اتفاقی عجیب، امروز تو پلی آف صعود به پرمیرلیگ مملکت مس رفسنجان تو زمین حاضر نشد و صنعت نفت آبادان با پیروزی 3_0 صعود کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/101592" target="_blank">📅 21:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101591">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdOJaoJou7BI4tALd2SNJwcFcn2E1YRJBqQ2vHcoYRwokqDnScY5jASkShyZ9F7o3fWaV3rhn6fWqQ8d312qi2TV2pznphIw5ixQfFvCKqzZT1Qv0JhHb1010_4tnYca5qnVQj3MnM9A56G-5rfiMpYUr4CRgOYuxZzjDikMvooWPKQWUkfxHR-P2MhqLrL-L-eWwrSAREyTPPSmNny9hEnJ_KRiL8BzbR_P8D5_4xyRW9GBUhwuNkmJG_iUGEmhu8h2T4d1xLdI95MXnQ0dXTLwzatUu6Xr-3C51BVmEHiRsNkClv_Qd2f1U2ObcnsBXm957KRejxQ-v_gniN2wYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ یه پستی رو گذاشت که توش نوشته : پس از کشته شدن سربازان امریکایی، ترامپ به سنتکام دستور «دروازه جهنم رو باز کنید» و حمله به ایران رو آغاز کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101591" target="_blank">📅 20:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101590">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdfyczEB-1JZ5N4bdwnE3wDLXeD18sOQePQ4ck9GUJvXn2uTT7LMTXFOWSKIvQYlm9el-gWceRX7SGeRxviMCxDxd0MzwhhL0t0991b9T4fb1EA7XwOJsXmeK2HssMXcMz9ULLDIHAGaG7Fv1BJsafooTmc9rTHlDbg06nOjXIj_Gzoy8XBb40Ies95J2Xl8mUqhSE-Yd2vQqsPdUcHx241CrbTa3murI5BExR70-rECM6qHz2rJSQFhU4IESySMCC7GxZObM5Mf7wsDhOdAC17z1mfYzkAFoJKNLiQlPv5qvdXYQmvzwruO2sGY6F6SNzt_AS2t7NvFgWQVVAU6EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
کنفدراسیون فوتبال آفریقا اعلام کرد که این مسابقات از سال ۲۰۲۷ با حضور ۲۸ تیم برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101590" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101588">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rz0CBkHLkQp5W8dnMijM1FpqYsgTchuBmHP0_wrO2URpM6XYAroW6Of4ix6i877ObuUTmNjn2cCGemBvDMHJ2XyNvcfZU87KXPxZeVSvKp1nXkk2LWSuOGupbXNPj3mmTpzMZMD6nLfPq_pRgQs-KygblNAUXI6WOROEfLeJUCFDmIGbq7LO4xOeK88WjjdesRlX0XEuBmlx5d2_1lz_OZ3he1Oor00OHBoTqwEVbOvAuCd6XcUTj6-wP0p4KXkbmHM_mu7bOcvkmfUPge_ZnfPnk1fCELy-FR7Q3FBPSP2LQqqG9fPCKBaT80lT2-XHCiA1Pc7vBVpwECTZd9DoJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7SUmvM_E25ic-Mf6OC8REfzA2TEEgnszplx9EoNb0N6K8APHWv8nIfn6EZ7UwXxL7JaQ0-BCzzrU3R4T6weX-zwCZPq7q3el17-Wtuf9ZstfonkWJod7Y_l7zKOiSnFOhB5gm3LRrjwCE-joyuDI3xiQXjlVJppLAsihkBan8_wtoY2xpNhQwmx1G-g4w6k2hpduI4i2JYsmh0sv4Dp0OQkhqbKJJX10lta-Uzk2ymOwq_gpfcy_HPRXhDovrFPYC9_3nqNj0E4ZPX6lixkJ0mw3AzPj9p3qYDOQrlfX7pgS_H8kjx3fL26Qd633h5oB2zxeyui4Y1oSDAtaaiYfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کاور رسمی نسخه استاندارد FC27
🔺
تریلر بازی فردا 23 جولای منتشر میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101588" target="_blank">📅 20:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101586">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQwpcz4wjDJ4ZyPD-BzPqKs5qvq9sqrrBUs0-N4wsG3Y8gxq_1hRHRCfeqwSnZuwMBfPhnycEZWi-wafCxsYq5zz6ef59RhegDPW3WjmDb2Sm2ENbCihko-KjtcdFRIo2edDJsmptCGzROhlrrD-W11BYynexY37Q1Hy-ucRpDrlSgdDLTPTyp4aQ_DP-PGwp_-pCmqG9s7nHkqo2prqMX43vMbNGjNJjz0Qe-lVN49OpzN9RTJQtZDn3_JaiBz-MQM4ouQ31A2cpMf50v5FM6rpPPvV8NdZOA3vB1tq0H5BrKhXSK4YY0ySze2fdnjoBbkr1SGG4gokDsUDYdo2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6db999500.mp4?token=C78X1PzTQZ8S2v1eRGoTScyYVSskWgUGg4TfWshCM2v9aba3xmYIHtIp6ZNnfM2XT58cVlkmL0fv1ejZLIkRf-uxSMe28k7QIuhHzFeOyu8IK3UpL19bWivrTg1cN1_pp_perZu-Be_Bfrgi_UoWAZhreglCefxyPJIka1T_jrpxItAtXAyFw2GiLz5v8bIc6cmnkv5jI-xBF3DmGFuuIkyXqULqbWwfQrK_Kfc-N1AOrHMPne7FBfhxLg6rTcQqDkfksfItXY2COsW_p2BgCL3-fqd6iSSEcAJ0_yuCf3AwzjluVK6jyBrFJpkqAkDfNpH-LzVYdtg8RPjUXgZYKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6db999500.mp4?token=C78X1PzTQZ8S2v1eRGoTScyYVSskWgUGg4TfWshCM2v9aba3xmYIHtIp6ZNnfM2XT58cVlkmL0fv1ejZLIkRf-uxSMe28k7QIuhHzFeOyu8IK3UpL19bWivrTg1cN1_pp_perZu-Be_Bfrgi_UoWAZhreglCefxyPJIka1T_jrpxItAtXAyFw2GiLz5v8bIc6cmnkv5jI-xBF3DmGFuuIkyXqULqbWwfQrK_Kfc-N1AOrHMPne7FBfhxLg6rTcQqDkfksfItXY2COsW_p2BgCL3-fqd6iSSEcAJ0_yuCf3AwzjluVK6jyBrFJpkqAkDfNpH-LzVYdtg8RPjUXgZYKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📅
🔴
24 سال پیش در چنین‌روزی ریو فردیناند یکی از بهترین مدافعان تاریخ پریمیر لیگ به منچستریونایتد پیوست و با 30 میلیون پوند، گران‌ترین بازیکن تاریخ منچستر یونایتد شد.
🏟️
455 بازی
⛔️
203 بازی بدون گل خورده
✅
🔻
پرمیرلیگ [x6]
🔥
🔻
جام اتحادیه انگلیس [x2]
🚀
🔻
سوپرجام انگلیس [x4]
🔵
🔻
لیگ قهرمانان اروپا [x1]
✔️
🔻
جام باشگاه‌های جهان [x1]
🥇
🔻
عضو تیم منتخب فصل پرمیرلیگ [x6]
🥇
🔻
عضو تیم منتخب فصل فیفا [x1]
🥇
🔻
بازیکن فصل 1997/98 وستهم
🥇
🔻
عضو تالار مشاهیر فوتبال انگلیس
🥇
🔻
عضو تالار مشاهیر پرمیرلیگ
🎙
🔻
مایکل کریک:
به‌طور خلاصه، بهترین مدافع میانی‌ای که تا به حال دیده‌ام.
🎙
🔻
کریستیانو رونالدو:
واسه من افتخار بزرگیه که با یکی از بهترین مدافعان تاریخ همبازی بودم. فوتبال و شخصیت او داخل و خارج از زمین بی نظیر بوده. واقعاً خوش شانس بودم که کنار او بازی کردم نه مقابلش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/101586" target="_blank">📅 20:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101585">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG4gIRQkRyXjnzwg1EnpWJnFFg4Y5mt8D3zX1J70uAn1gL-pDnFQic-WdOkvBL95XpxyS7JSSKP984EwcvvCapi3s5zdbsicjaASSi7AQsOyHk3YKI677pA39SvyVWhVn0IfdfyNa8er5DPrYGGpPoojc3lWmZ9d9W2Eyy6oJpfpjYqg4EwGrnWCY_ABJMUuTyQKyg_UZnWkj_MKfXb_GKfn9Hqw-sP-fxUdL__v1ZHEwKFFuX0lVmkOyyi3__826NOq4Um9DtzjCGC-Z3wue3dde-3ZtglmpVJqp-kDrPAaJLzrtjzeyShN68ZYZ1c5hd-vflK-T1ZuDcFw8whw2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کاسمیرو در انتقالی آزاد با قراردادی تا سال 2029 به اینترمیامی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101585" target="_blank">📅 19:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101584">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mllVHclMyJ8F0f7R3Fco2NCcfMPDTSl7MZu-vKz_BGlI0oXfif5aSwHBKQg6i0Gy2aOdtVmqxPiJMjD7LWzbny8OeB86jGcvBJUXiP8F2H9nBLnGWWMXX9_d03K1Ub3Rj0bIUl2qsLRkWrE1GGGD1yl3DA_xddfP0BOLqDtwm4Q42VI1BAzKktwTSu5BDcLQVAUb0F9pN1nO7RdyIL2Ud_rcPhzwxR77UI-5JDXmiWfgeTRlhgodS-67VvuIx2UlWQ1rwlIdLx900tuwr8lgmVND-UAOPe1QQPvPSwkdxSYKtjTj1XHUoruljyodGiRsSNsrQAxMoncvTCnU4EbQFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: گارناچو با عقد قراردادی قرضی راهی استون‌ویلا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101584" target="_blank">📅 19:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101583">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b963f629b0.mp4?token=ZqBcXegryRxWEF_2JjmCWHnWLdoTM7i4eBhMREzERhdRfxB7AxTWEuUJtRzi6tX78KQPcSELU8hbVq19gWeX6lBYb-X7_7p80xVZ4SGTDhTYTnncmWJFdTXPfBGtSkIqjWr_RdBY5rJqGRNdwhH8rKypRyDiTAHqkgJ5A-vFPxopY1jSKOzTC43aYmeTRvycs-kKkZwsMFe4qxqypStPY9V63crIF4E3LeDG7D6miGY7IYiT8mr1kf_hMycKDDzgUXeR8g4MUSuHuWoNjQ4t22wkheaCTm7NnoRv5tj_e8oU3mzYSzu9D_oUZL6_75TBxX46G-2grY2W2Q3FjvmB4GaZ7Etk90SUjU1zLR_6imCYv99PqwnSQFz2ANb2J1j-QTv4iEmrNHj04YPhAkWggMNGoX23PNL8LeMTAvtKGQFdPQ7zrqRX9y3t5wdZkw2JtjNRVdjX6p2cj_sVXoQjMym0Q2t8_-0azQkTplxY9QOhusDWF7F2VmJGLeJ7SZGOBXxCTw_Rx_zt-IJu8cJ77tnKIV6EJobYUQ4hIPCfIxbga84Y_xJ9RVFzdt17O6ZryxGlFCOYXsA_9g8dCAr1FhGCupCQHwFN9FqzuluZTeI0tVIKFagLoU21tUG6FSuzjnMU4q2WqpslUf5SWmkJ6Zjfsmk0YsOvxEdcg1XtEIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b963f629b0.mp4?token=ZqBcXegryRxWEF_2JjmCWHnWLdoTM7i4eBhMREzERhdRfxB7AxTWEuUJtRzi6tX78KQPcSELU8hbVq19gWeX6lBYb-X7_7p80xVZ4SGTDhTYTnncmWJFdTXPfBGtSkIqjWr_RdBY5rJqGRNdwhH8rKypRyDiTAHqkgJ5A-vFPxopY1jSKOzTC43aYmeTRvycs-kKkZwsMFe4qxqypStPY9V63crIF4E3LeDG7D6miGY7IYiT8mr1kf_hMycKDDzgUXeR8g4MUSuHuWoNjQ4t22wkheaCTm7NnoRv5tj_e8oU3mzYSzu9D_oUZL6_75TBxX46G-2grY2W2Q3FjvmB4GaZ7Etk90SUjU1zLR_6imCYv99PqwnSQFz2ANb2J1j-QTv4iEmrNHj04YPhAkWggMNGoX23PNL8LeMTAvtKGQFdPQ7zrqRX9y3t5wdZkw2JtjNRVdjX6p2cj_sVXoQjMym0Q2t8_-0azQkTplxY9QOhusDWF7F2VmJGLeJ7SZGOBXxCTw_Rx_zt-IJu8cJ77tnKIV6EJobYUQ4hIPCfIxbga84Y_xJ9RVFzdt17O6ZryxGlFCOYXsA_9g8dCAr1FhGCupCQHwFN9FqzuluZTeI0tVIKFagLoU21tUG6FSuzjnMU4q2WqpslUf5SWmkJ6Zjfsmk0YsOvxEdcg1XtEIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
میلاد کرمی: بخاطر چند میلیون پول بیشتر تصمیم گرفتم یه حرکت وحشتناک بزنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101583" target="_blank">📅 19:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101582">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEXxJUB_RiL2DWbJtGuZJLaYh-HisNP3Hub_cdPYHQYdtoc9VU2U8XosrX1SiGr-E5IKSyejl-jIFg90nV-_zK9z71zgikcHdoFfGSbYxevULGWRS06aGN78n7KDTzHnLaVeNV0cdxMtK195RUHcuo3VHpfnjfjRP0WixD_QeD2-JJBhnKd_rt_mto0MJmica6iV4xpjncyXHJDK8PEVKIE2gBqfukCRNLdHSiAZZpgkDdyySA4ql_ljErvjOJsEcTbwJ1dqUPr18BLVViHmthzFwEuwq8b813XkRrvXZzcY-ofKbe9g4BaNqXfIkgyT04laJoN3JIVifOyYKZCodQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏امباپه در این فصل آقای گل لالیگا، چمپیونزلیگ و جام جهانی شد و در نهایت هیچ جامی برنده نشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101582" target="_blank">📅 19:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101581">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723401c013.mp4?token=X5Nrm5cxEYS21DII9Fw-BxDHlhCDRhrKjjZ2xr7PNns5HiIs-m7nqHm2R0GYNemQsHunBgcp8Q1mMO0ESIlZFVEAWpOUvwMWFS3yl9AEEQNhTPajFoJAuP4IEwCrPtwer87NInlXd_V_WU-4NDJzyejA34-ZJDPub3IIcq3pP0gCccZbqG3kA_0SIJq9fL19m1tknCdyqdki1JZ2gFjjy29osu0vsYqnBIusooOZ42ED4iFRBg2QEAX-ASQeXOdZrm7zoIcRarGxPdZoLdpCzsliFDEUUUuK9-imw_XV85mJsILgJAyl1sWyc-zYmcglFV4a4LDZTtyBIBUvmMb0Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723401c013.mp4?token=X5Nrm5cxEYS21DII9Fw-BxDHlhCDRhrKjjZ2xr7PNns5HiIs-m7nqHm2R0GYNemQsHunBgcp8Q1mMO0ESIlZFVEAWpOUvwMWFS3yl9AEEQNhTPajFoJAuP4IEwCrPtwer87NInlXd_V_WU-4NDJzyejA34-ZJDPub3IIcq3pP0gCccZbqG3kA_0SIJq9fL19m1tknCdyqdki1JZ2gFjjy29osu0vsYqnBIusooOZ42ED4iFRBg2QEAX-ASQeXOdZrm7zoIcRarGxPdZoLdpCzsliFDEUUUuK9-imw_XV85mJsILgJAyl1sWyc-zYmcglFV4a4LDZTtyBIBUvmMb0Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
علی‌قلی‌زاده: در عمل جراحی رباطی که داشتم، از یک‌عضو جسد برای پیوند استفاده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101581" target="_blank">📅 19:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101580">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pe40cPrIsnX0PIA-z6qSpiC-6Ja8o6FPBbuzKb_zPYPI1nD55nUzVkeByqWO6vUaU7hbqtE-d3GYFtFUiCMpI1IOvXxTPVNEFU9A23M6iuMkKjdlwxrXErus5xcqRQNwykRszQUAlhR86H7woxQxRNYH7wZCx6lUCIBIVUIFCadbVvSAgiCw1BUBxImSgwKJJzzAEgGprRee76J9jg_G_AclXPjQOpYDnFTQZonhlNi-GIfZ2PBdh4IjdJncYey1kdZHgSjUIBLCw-RcktD2W_lq11fYo_Tvs3t3Ho2DLB_i1u2rYRljOlRL9ZAQq0kusIqoTaRNg35KuJd9vLOuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پزشکیان:
دستور ویژه دادم که سایت عادل فردوسی‌پور از فیلتر خارج بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101580" target="_blank">📅 19:14 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
