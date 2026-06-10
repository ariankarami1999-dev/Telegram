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
<img src="https://cdn5.telesco.pe/file/m7C5MkWIvgY_2OSkIc2S5LWwZzmxepfG_r5vhUHNV-ZLeWKAKULt7jwxK40y5OuFioqr1mKyhDXv2-Edh2SZaJRGXBprZElMeguQ_38XBNBVr9UxKE5JbnaOkNtqN55RaF1yv7UsJGihDH9zwpaC1BgHXo0nk0VDQKccryTX8pdNSgpv0Zp0EPsaiKm82K7dPmKyccU7OQ4_M3_1SCXloFJ78LSExnm0H8S6hfDk3QYYo16jS7it4HsoX-HSzhrI_CNTIr6LPObh0xCMfwi1I1qp3hnJ8vIo0uJq-7TwYpA4X35nREfBO1BcORgxfnbgBVgeKwVZLQF0ERTtT1USTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 325K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 23:44:16</div>
<hr>

<div class="tg-post" id="msg-91898">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73ffd2bfee.mp4?token=qagiKvUfsM8hUd6TT6PRZ-UW4PaKWrxMLjkG93MD9TiII5lR4IzL_sZwzoTUGRk-9ePz1xrYw9SQwhcx-Dd9qsBYmI6JFv50WE9A-iG2_qiBiQ8GmPvTnpGBBuA7VVgPABZQRJeBRZj6GxgvjDgZCpS0k_G5bUrq8FQPib208BstGL5NQo8ftd9EFyKuPLQsmKRA_URYb2dB675Ov0RGAwpgcGwqbF0F4_w-z7lHHIRuYQAXXZOL_0vQodwDfFn3XDBYa4os_1g0pSKdWwWZnZqWkzP-BEkuH5CTKoUDUJkcmW0vzC9AKJfIY3x4r_TQ-VgU13eDgGUoRMWvzdnM0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73ffd2bfee.mp4?token=qagiKvUfsM8hUd6TT6PRZ-UW4PaKWrxMLjkG93MD9TiII5lR4IzL_sZwzoTUGRk-9ePz1xrYw9SQwhcx-Dd9qsBYmI6JFv50WE9A-iG2_qiBiQ8GmPvTnpGBBuA7VVgPABZQRJeBRZj6GxgvjDgZCpS0k_G5bUrq8FQPib208BstGL5NQo8ftd9EFyKuPLQsmKRA_URYb2dB675Ov0RGAwpgcGwqbF0F4_w-z7lHHIRuYQAXXZOL_0vQodwDfFn3XDBYa4os_1g0pSKdWwWZnZqWkzP-BEkuH5CTKoUDUJkcmW0vzC9AKJfIY3x4r_TQ-VgU13eDgGUoRMWvzdnM0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
عجب موقعیتییی رونالدو امشب رید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/Futball180TV/91898" target="_blank">📅 23:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91897">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZJamwkeRREqDEGur-XSce7Bt531eTPYGvKsxHYxLBbmjmdPM7nc3yCmtaHyO1KJEfm9CPVqrKZdMu7JqAwv2tA9985Y8Sg0HHEcqPcbmwwkxdiEjFNwHwCfNgYqNQ5-lVBFU52anKiz3McS4VrVvK9omCtDXKX3DeT-Ff6mUpHeG0usRM5kdQ9MSJs8eqdzr4_g6IrYT-QNepbC5leGAcmg7GKR8nBodJa_memWY1rgNeafNV0_X3J5dRDk5vUi2L04cgJP_fFmG__-1WJJjJpPr3vuEIbcAL7teRwngrHcAxFI6sCMNBT1_MAgpcm2blPliJSjFad4pSkUPiKytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی:
🔵
در حال حاضر پس از رسیدن به هرچیزی که آرزو داشتم، سعی میکنم با آرامش بیشتر بازی کنم و از آن لذت ببرم.
🔵
درسته که وقتی زمان مسابقه فرا میرسه برای من دشواره که آن را به شیوه ای متفاوت زندگی کنم، زیرا در طول دوران حرفه ای ام همیشه می خواستم بازی کنم، برنده بشم و رقابت کنم.
🔵
اما این تیم مدام ثابت می‌کنه که با همین  ذهنیت برنده وارد هر مسابقه ای میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/91897" target="_blank">📅 23:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91896">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKUIvZ1LdYnEVnM4jwwDQwK4WTQTctRtVLkCistx6_tBZ3TY5YrR1A4tM838B9Xfu6sUtN8sdZzmhE4g4MUBNAeHM_b_kQPFf7FYEYG_jZtp3hi8XMVF2j-L393Wq3RjYesusPym1Vbf_2hlf3HdukGGFuvBp8shL3mUB6nbITEjufq-97RXdtRG405hvbZLt4cZJnFgogZGVnNymcqFoQ2Hgow2-XyLpV2hDXCCk8qXGN636tjcsvAhFYxnZ6GoTUsIe7KyMaiKHnfxWT-wohHjCLviWt3lRzij6Tdl9Lnfqcw4XSVadSi3Ap8sCNA2KpU4N7Q031ep9HOobI5EdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیانی اینفانتینو:
آیا از انتخاب ایالات متحده به عنوان یکی از کشورهای میزبان پشیمانم؟ نه. از هیچ چیز پشیمان نیستیم. اون‌ها قطعا میزبان بسیار خوبی برای جام جهانی خواهند بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/Futball180TV/91896" target="_blank">📅 23:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91895">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
نیویورک تایمز: ایالات متحده رسماً از مذاکرات کنار کشید و راه های دیپلماسی رو به خاطر اتلاف وقت طرف ایرانی بست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/91895" target="_blank">📅 23:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91894">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrvNZe8BUKaMMEIOFf__nxXQUvTiTkCImdmog2fI7iQkirK6hYFhjx8lsvtSFfkqpaWBiTVrrH6-l-7Dor-pQ7czBoz5oNt4paDsl9FOFeViWvh1GRt4zRSLxR6Js8qddYT-8hk9uhTkBY2KjKo_3H8oRinK71ybzL-gwxS320NVjAsJAHdqHfW8vOFbs7N8rqXSuc5AIuBWgJMuJTp-NRzj4UeQQP08e-xTjxr2xbpQVFrhsZFyUrr0w8JroR2wba9IPp51oS_u1gAMylM1AcRlfpv754ki6xLTtNJyPSHhrR9Gvwg7h-cBAO1BWMvEYiZ-0bKj4ieHncKu2WmsOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
اعلام ترکیب پرتغال مقابل نیجریه؛ عجب خط هافبکی داره پرتغال
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/91894" target="_blank">📅 22:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91893">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1eCnnwa1ZeXRnJJ2Zr2dz3FRozgd95jxOONK1Yk3hKfndunbwBek_ouvsVzQwHQ7wbdWqXzy9NTxr-Nh9zDj3QnnqJEMwSTa92DYT8jQwOUyC1VCFuieaDYrzV7bfZsfyvoagNg9EShEL9kzDvCHwgFRdCuLNVkQ1svz-Cjt5Pi8KdbMaPJ8jxgQ1OOcA5i9Y_J86jNdFRx6vOKqfPwkq0hdeHXbZJXyxAAJ18SufE4dQkFAC2_Lb6hiJ-iCoGlrKc_XIIv_gORRmInYzj1jY_ZszYRViqhis3PWLm0T4BC2jWLfv26pNAxbxLtwstaRMZ2Wy_Om7jyBvH80eMLeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فورییی
:
🔵
منچستر سیتی پیشنهادی به ارزش 106 میلیون پوند + 15 میلیون پوند برای قطعی کردن قرارداد الیوت اندرسون ارائه داده!!
🔺
با این حال ناتینگهام فارست 140 میلیون پوند بدون پاداش برای اندرسون درخواست کرده
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91893" target="_blank">📅 22:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91892">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0zvdsTHdGn1DpcdoklMOQVUgzCFdyw24BBH0cMRjOSFSSWhGoVCoRewAivuUNLs4XN_pDX6jnaXhOOfVY4sdUiHXs3qW51y4lS39EoLPFHH3xAaRaz9Hc3CPh1aS5lwNerTzwq5c2Ecz-UdIwlu8ycbeX9-aJcWucexFeXX7rRpCQKrrUscdhBGibl4jJRjdYjB8UFhz-RTb2DBpXAnU9A0ww0hvJZFqPGGCrs4akaZaZL5VKHXhw5EX8YIXzUqo53VH5w-LkaU4tuq8i9v97ljfQWlqpBNO4ToBD1DckBWbWg_W49kd1BW5xO49yiIoCQNvfzosN60Ijvo4EKyIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبات و استمرار اگه عکس بود یه همچین چیزی میشد:
❤️‍🔥
❤️‍🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91892" target="_blank">📅 22:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91891">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922b907be6.mp4?token=U4kUxPMUHTrehl0fAI27YmpHiV3sfoPG6ddgnlJpKuVBK4UkBAI-jO0o5iJMPklYg89pE5xM_hBnbAVJ5FNwFafnqUlh1ET8867AYKUZ0Xzmt0FFrKiE6RmLywVnTWzFvPUhsLPhmqGDdk_31FsRNVnokK5aqwARSgFFghDwVOg96r9_wssZWlR77pJNYI1mwUo45aEVhtzFyZRBYdkecI0i3gq_rUdWuPtEoWDeQQaJQyFHpPNe91aAbLvk7T1JuOxdW7qdFEuQnh7z8qMIN_FjaVaUqrO6IgCq6hDJnynY2_7KWrK3fCztPDshREx0dQGSUGmAa67QbUiT7CM3iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922b907be6.mp4?token=U4kUxPMUHTrehl0fAI27YmpHiV3sfoPG6ddgnlJpKuVBK4UkBAI-jO0o5iJMPklYg89pE5xM_hBnbAVJ5FNwFafnqUlh1ET8867AYKUZ0Xzmt0FFrKiE6RmLywVnTWzFvPUhsLPhmqGDdk_31FsRNVnokK5aqwARSgFFghDwVOg96r9_wssZWlR77pJNYI1mwUo45aEVhtzFyZRBYdkecI0i3gq_rUdWuPtEoWDeQQaJQyFHpPNe91aAbLvk7T1JuOxdW7qdFEuQnh7z8qMIN_FjaVaUqrO6IgCq6hDJnynY2_7KWrK3fCztPDshREx0dQGSUGmAa67QbUiT7CM3iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
رامین رضاییان مدافع راست تیم قلعه‌نویی: ژرمی دوکو؟ نمی شناسم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91891" target="_blank">📅 21:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91890">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
🚨
جواد خیابانی پس از 36 سال از صداوسیما خداحافظی کرد و اعلام کرد با بازنشستگی از این سازمان جدا شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91890" target="_blank">📅 21:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91888">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FmxVztm-hIgM-nbxwMnA2BzetzaxNz7kF0T5F8HD-60rJ3LFx_Px0Q71lFBn4aJAQn5HZqhTAJMcoKTq3YsdIhynO43kflO3zFo2OOPvSLEbkrkto4ZdFHZMexCUakxJvxpFDr9UV6gqM23M_oFEcRniK2PmCSCPdsg0amMd7aXZft2DWcfEPmxs8T_C5iTc8b5zQOIQwpgL1OEFR8znHonnYzVMovVQ2vLcDR-wvuEuA6ne_h-WoKMgcZTREcbRQY8XN0SvOqZc95xYm1JAF9WnSwkg5jT6-u7vFhzz78FTi_ApMrie8Knl4ogIVf54v1wwKYFSMyRC28w6rqBMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FHps6SJsk3R58DmfNEyO6Ayjl2SOjKYE9nBNAgX6fmCpinWXbWZLGXP1w10N9l5wXzN6NeHNSBxC6EChlGQFnPKRcSNyQQTYsTUYFxlnmCP1YQBCIZAi9TnMkiPApGhsHxNeXEuj5cuqzA8nXt8Cxr92U0NvBFxMRGit8tGGeK7aFF8crgl2RXwZ2ekuGED-i1-sdtaZktAe0cuemhu0j1B89Hp5xqyozVuKeJPS0NW9eXtrUKb_QZlRAk7GTX3fhQRTMPeKFsb2XAxpf0cK5Q12FDg_bYjC9lbMXY73QRTmJ5F6NN5--N5bErRX-xp9eu9u5848ly0qpoC_m4GWkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
فووریییی
بمب افکن B2 در حال حرکت به سمت ایران!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/91888" target="_blank">📅 21:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91887">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6GsOcQko0QZN2ABR5ay6Yk31gcH1qYZIThg-SGrOy1A5FBC1cWV-tRJFDi6jEyzuq3qRPKQtQrH6LpuGnDVKiB_VTayYoG_kgV7qHTw8PABHhdSsl7g3PCO9XmWhZc6VaFTkpdtNa7AVMCg_nw9rMVnUf6H5VO4EGvEET9QhC65dtsuvZRw_gtvyEmNywRCFT9BtWttK4hx_l_k5hE322zxduRiKaUA9WI6K1apup5IjgTHrHgmrVLDsEPOKaNUwgJn44I3SneKzLZ4cYc6eQE6kgzjlse69b02cvs6xXgLPthU1L_AQCpOd5hXc-gOG7Gp5--YaXGZy4XvzMzYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
سپ‌بلاتر (رئیس سابق فیفا): "هیچ‌کس رسمی‌تر از داور نیست، و اگر کشوری از ورود داور جلوگیری کند، نباید جام جهانی در آن کشور برگزار شود.
"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91887" target="_blank">📅 21:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91886">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5zLeB-kLbJPrnSjcnmV-RHdsDr3R5E9Y-A9QkctfGCcyJsiV1bZbG18JB7MHsFeOeG57jBXpJLllAmMvl3Een2I_yRtyt5D12TKBFkRy6SwsdK1U9VdTjYqAvzJAO7PP8bKeky404TIaZsBKwYHiwsUOaGIkjh7pJUEtQFw0iabojfyIBgRFZUFpAS11N6L9g4l4G5jc9c-RXpAj1ORrWNacqpkPbe00egbbDXFCOj58Y-syQAq-nC-SQhdx0INTxwAQyNkocgK81H2PRoY-rHiGJ2riW76W1yEQf_SFtS_syJUOgueNepmbb1PWsvjl7viwvHhY-YwJErytla19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇺🇸
دونالد ترامپ: "جام جهانی ۲۰۲۶ موفق‌ترین جام جهانی در تاریخ خواهد بود."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/91886" target="_blank">📅 21:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91884">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
❌
باشگاه استقلال مهمانی اعضای تیمش به مناسبت پایان لیگ‌برتر رو بخاطر شرایط جنگی و احتمال بالای حملات آمریکا و اسرائیل لغو کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91884" target="_blank">📅 21:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91882">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQ1rDWlVYu3SqEeqe22jeVQ_wuFoJ-2xPNM1_XFmkpivcSC8dpb4eTXhu57Vf2dYzUr_Qq4HzB3moGinuHR2WX7fDUpk_vL6IQVe4HSxdYc-GEMFBUEGG0WiXE2mfYetXep4wI1lh1YnhgX--mNHlxJOY23xzd274OZz8BrbU7vqQQmaNNIYAwtWWwc1kX9CiEYaW4LCOstVHx-JvzciR6tpTEMRxFlRzgIcE76TEqUWN6l0JutwteUwr0uBH57HLjG3hQiJxMfF_276XVtAjh412WJ_mH0ZI9bXbs8B3gXVg649giEWizvvQ28W5vA6yXAdNAXGIbTvlvbhluH-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQO09vmAcfnmfi7NCzTQ4mDEjuCSeWTIDMFhBPOwxO2QO_uGz8SB1XqLLjHb5HyKyLOuJax6HMOXvU7nqPJH3pPLCfSMh_VvvOBiVq48OB_TH4R45eqqHFD_NlceshI4TlHiCtRvOD3KNU0VaiGGPZYnMUo7ubsUOJ1FUROlSb160CfsgWz_2RssOHRMYRjRHnsrXwUixcNxKGohbJItB7A2w5DRUpOOryvn4-TYomzabOajl2_gMNLVqo0n_JKGkk4mjvwUzh2f_fxVfw9oAn1xvBA6A9IdkgyW9iS_NaE4OCX4wUUazpSWzBjhkrrH0jSTtmGH3y5WDS_JSgOMkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
این یک اشتباه در طراحی نیست
🇵🇱
🇭🇹
پرچم لهستان روی پیراهن هائیتی
در سال ۱۸۰۲، ناپلئون سربازان لهستانی را برای سرکوب انقلاب هائیتی فرستاد، اما بسیاری از آن‌ها به جای جنگیدن، به انقلابیون هائیتی پیوستند و در راه استقلال این کشور جنگیدند.
پس از استقلال هائیتی در ۱۸۰۴، ژان ژاک دسالین به لهستانی‌ها تابعیت اعطا کرد.
اکنون و بیش از ۲۰۰ سال بعد، هائیتی با قرار دادن پرچم لهستان روی پیراهنش در جام جهانی ۲۰۲۶، یاد این دوستی تاریخی را زنده نگه می‌دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91882" target="_blank">📅 20:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91881">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c979a7db.mp4?token=tOm1cExGMO893Gl3BvgTP247J93BA-faZmh2TGJDlWs02U-slf398Fh7sa_pS807QnKblGyF80y5Kv6xYS1wGVmC3bU5aSeJl9jqKM8rPkI6YY8KGbVr4YXPDnZbnc4Vj8tTpRB3y3ROiENZLH5ljsD9mL23SAtNZzE3lwKGZGCJgGiE16yix1NVwu-rIImZiHJbpHnfsqGLJsdzcx3uulyj4_xgcWU65FgSDk0t62uMcwgz8Q-ANWxFA-Gb6njNWjtEw-TYlFAO-Opuy1_3T03_u65myZLlDZErAkv80WosRrl2iX2Dqwbg02M1Pm2BiTbsuwlIsZfM0sr8FjbjQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c979a7db.mp4?token=tOm1cExGMO893Gl3BvgTP247J93BA-faZmh2TGJDlWs02U-slf398Fh7sa_pS807QnKblGyF80y5Kv6xYS1wGVmC3bU5aSeJl9jqKM8rPkI6YY8KGbVr4YXPDnZbnc4Vj8tTpRB3y3ROiENZLH5ljsD9mL23SAtNZzE3lwKGZGCJgGiE16yix1NVwu-rIImZiHJbpHnfsqGLJsdzcx3uulyj4_xgcWU65FgSDk0t62uMcwgz8Q-ANWxFA-Gb6njNWjtEw-TYlFAO-Opuy1_3T03_u65myZLlDZErAkv80WosRrl2iX2Dqwbg02M1Pm2BiTbsuwlIsZfM0sr8FjbjQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سنتکام ویدیو ای از هدف قرار گرفتن یک نفتکش مرتبط با ایران منتشر کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91881" target="_blank">📅 20:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91878">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKKmzUfV4_6_wd2qVFLPSC7kg2DwwR7X_HN7ir0OLgZmvUYX7VkyIVTWEkFuuQqTLBzqqufBtnqa5onTdLbnKz3o3Pv8FaGy-j_QCrGOOMoZApgU0l21fR5-9OvuXpnVY67FwNvcyiZJtIpy_7gPRFq6fB6oNph9zquL3EDyp6OGYG_bi9uRVwxOrYDyA71CDP9S2uHSTVWkkuttf3aUNOw4D2MMA3BbjaeA7sZPVlknMkBQ1uYUTHyZFSp6uoVMVMxrerdsm0OTmSJYPFia6fos_55YGje6VJlUxiynx1mBxLGXq6GDEAbARuTVUOkovEjdLTqHoQcDoe8gsiv8uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qiX1Z7OAfDi3WnGO6hngKrimC117DyMS27yV2H53CoV-w9sYU7TRN-2aY5-2T3jg1CV0HQIEap6Rk5XoxiOZNLFACEUWHZScpPeKwiTtW-zXz-E3nAZ52J10HFqigx4QXZ9uK7qkfs_ul_RKA_H9G73ICUM7SO30nw0zJTzsPnxqj21JuNwAE6Dd3sKcTG07GJcwC5aNRzGI_TqyC1JePYQwx4xHPNgwFwI_nPGc6GO2TT5srJKWH6ufrB4JRIFtgVweSueBvqRiti_3p-6Hj3cZbg2n1DAWsYjW9Phmki--GAvkI7hvwGQihM_1yA7MV82s7zELxUpvYs0V-s1EaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mP3RYnI1MkGwE4U4oy0DLLOZGdpD2VCs6Yi3Z8KqUhgnl65HAyAfGHkx8uJgdJ7xu-5WPXt3zCy3h8EGEyMAknf0wzIniFMZJYe79lnsiVpecPp5nM7E6q7mOpuaEejW8ecVKrR4kUIq7hL7JRQyNenI0n6Q3aQg0yQaJS87GFAtG6PwnlKJRu35PVuT9Bf8EsP8LjAmoq4wNYobizBd7CW757V-vjvm7inYLP7Luz-mxzaZSnF7121n8y4ZNPtWV3cClyJz4zzwcUQ2b9jGOg5XLXR7iKB0dJtJfFVJXlenHfgGgRXYEyUHo5CVSNlD2G-1I6Ba-JaiNJvp8le-Rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فنای جذاب و دوست داشتنی آرژانتین
🇦🇷
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91878" target="_blank">📅 20:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91877">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l81nCQfInd5RD0vUGYviZt25tKvvELQ1gRtlQUF2GUGerZF39Z6itqgHkhOnLU7IaNP3YWEUsj0tJqhWVepncfZoVmDerXoTcReA20ddxqbCX3ujwj2YxR_BeDYq9IrDJ2VhF_HUG2FYv9sMmrhFjkjyAxg6fFSimKDaXOEx8H1a08iqFKPLy51eHeTPJG0IaYTOqm8nj5yFp_W9wvEKp0TUSIoKQism57UNvnTta4RclqYdZfI-EQK3Z7TZYZOpXWnnGwjiKMCXQfGUjlwhWr6EC4VSuaawFkyEMoZFcC3aCpMlbEnlcPKtYmitRRZGIkmGvKkYJyCmJvGtAQoeyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
توییت پزشکیان: زیرساخت‌های حیاتی شریان حیات مردم هستند. تهدید به هدف قرار دادن آن‌ها (حمل‌ونقل، برق، آب) نشانه قدرت نیست، بلکه نشانه‌ای از ناامیدی در برابر اراده ملت است. ایران با تکیه بر دانش متخصصان، وحدت ملی و همبستگی، در برابر هر فشار یا تهدید استوار خواهد ایستاد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91877" target="_blank">📅 20:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91876">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8c0TElCXBvpARAewfG84LActA58gzeX2Xh5UzcNI-FGc495e7UXrkgIO6vfRapove5yH67tGHDml3DYtPBitHQBcjS_EgeirE00-QrAYNm9GNnHUaefvBSPOsmeIql9XoR9i2fikKBGZPAh6kjg_uSdl_z05Z0AZ7by9o-jHK7Fm2TJ_dszm2qnAVoyPKtAhhmxJ_pndIlE51vUX-qVISJdBtCp7AaC3RECRQxVqteImjdW7C-ZeQ0Fq7OC_d7jIvi9ScB_U1OZ1AClYB7pIu9NKxPh9yA1nUFo3eUdrZtjpCiWAf6L8qS5x3_-lcRY80TrZjqHFVbo8ZrZLaRFlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رنکینگ تیم‌های حاضر در جام‌ جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/91876" target="_blank">📅 20:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91875">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
قسمت آخر صحبت‌های کله زرد خردادی: فکر می‌کنم ایران می‌خواهد توافقی را منعقد کند، اما خواهیم دید چه میشود، فک‌ میکنم اونا میخوان مذاکره کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91875" target="_blank">📅 19:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91874">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/S1EmxeI0jlePKmJ0M2eQ6ZlwU9271ulIIwnkD_MM0e-D1QpenywRUXDoB5nzWIdDte507Kl5kNzWjxTiNiImUrz1mivqcvwpTBzAfnfIPKTVBoGTI_JVfaVRpGDSRgeQFQCa6OeF2CO3Icj-FYPsBvyDSGyr3HdvauyB8Klow2xSvdRCoj7yvvQrqsxfCgBqZEhXkuGNZR3Q3ZOQY0ziaKna0N_VOkLieB7rQEWyXWWXWGTo5mrZZ7AfQtYdqm5CxDF4aOAGecoVuZinXdQOO2_0iqNpnHJ_4QbByoXMsu8bNzxe0MraCplt2ZdVyv5YDFt_JQKaPEPn_wxIoE8n6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیگ پیش‌بینی جام جهانی در «همراه من» آغاز شد
در لیگ پیش‌بینی «همراه من»، نتیجه بازی‌ها را حدس بزنید، تیم قهرمان را انتخاب کنید و برای صعود در جدول امتیازات رقابت کنید.
💰
هر روز یک میلیارد تومان جایزه
🎮
یک دستگاه PS5 به قید قرعه
⚽️
اگر فکر می‌کنید فوتبال رو بهتر از بقیه می‌شناسید، وقتش رسیده وارد همراه‌من شوید و پیش‌بینی‌تان را ثبت کنید.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91874" target="_blank">📅 19:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91873">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
ترامپ: تا زمان امضای توافق به ایران با قدرت حمله خواهیم کرد. یا راه حلی پیدا خواهیم کرد. یا آنها را از بین خواهیم برد. آن‌ها ما را احمق فرض می‌کنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91873" target="_blank">📅 19:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91872">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
ترامپ یک ساعت بعد: با خودم تماس تلفنی برقرار کردم تا جلوی حمله رو بگیرم چون به توافق بسیار نزدیک هستیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91872" target="_blank">📅 19:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91871">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: چندبار داشتیم توافق میکردیم ولی ایرانیا همش لحظه اخر گولمون میزدن
.
اونا فقط بلدن وقت تلف کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91871" target="_blank">📅 19:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91870">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
ترامپ: چند ماهه داریم باهاشون مذاکره میکنیم. توافق براشون خیلی خوب بود ولی امضاش نکردن. کار اشتباهی کردن فاش نمی‌کنم که آیا پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91870" target="_blank">📅 19:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91869">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
ترامپ: چند ماهه داریم باهاشون مذاکره میکنیم. توافق براشون خیلی خوب بود ولی امضاش نکردن. کار اشتباهی کردن فاش نمی‌کنم که آیا پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91869" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91867">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ما به آنها حمله خواهیم کرد و بسیار شدید حمله خواهیم کرد. ما بمباران رو از سر خواهیم گرفت. ما حق انجام این کار رو داریم. آنها هلیکوپتر ما رو ساقط کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91867" target="_blank">📅 19:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91866">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
فووووووری؛ ترامپ: به شدت به ایران حمله خواهیم کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91866" target="_blank">📅 19:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91865">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
فووووووری؛ ترامپ: به شدت به ایران حمله خواهیم کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91865" target="_blank">📅 19:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91863">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4T52Sjr0AFskIRrX5e0L3BLKdj9Ln4HjEJWc5WT8aWs_H6SOwGfQPHnFEgLng4Wi9OJxOTXYiIrxQCapMO2S99f2__UKroTdIyRYvDhYsm94vqJVdhHdlAAmgvVoH8VqUAhVlXv8Dhui2IAV9t3IOnQtV9Ac4zaA0sOI47FraRHFNT6dQDsbCvsuz4PFoQHHtLgDQNzjBrrFNCCIFUAxfeHr0UT3318Yq05ieGEv9V15jLVkdIcX-_qGmZBHX84wfazd96kutnfzMHCAcSAgjaQbq72qdOxxRR7OC2Xq9ZjQ9XwP6TwFODKxSEY60zyNNCnGAWkx1TqHebQkWwc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوست داری تو فینال جام جهانی با کدوم تیم روبرو بشی؟
برونو فرناندز:
فرقی برام نداره، هر تیمی باشه. اگه به فینال برسیم، اون موقع بهش فکر می‌کنم. مراکش؟ خب، دوستم نصیر مزراوی اونجاست. هنوز از جام جهانی قبلی یه چیزی تو دلمون مونده، برای همین دوست دارم این دفعه شکستشون بدیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/91863" target="_blank">📅 19:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91862">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b88d7249a.mp4?token=KQ08Y55S8tbvEbT95j79dfoghoHqGoz6pb4BB1BHzNrYZXivZaoL33S4LHCXh8tPQAmjfvRrwNjzB3vSWvlZMsMnj-fgk8wE1eykMyMXISPchpmgQrvWnQaEgyVQ0R-LOIu_qyIenp6LwYiSq6H18L4qx7wlC-ohTrw6L6H_H-j6Zn3mkjGVQFZMMvPSMMrdrHtWjGe1a8aDruOK0fAoiyOF4DmIKCM11a9OEHL2tUmjEiLJfXX--ImZLN96tOlG1NvxC9wtApbivT3h7B63HzskFDzraDgKRKaAaO2FTOcbKeqxmmlNHnwcq0pKHqC-2bvaIWt6hqbUem-7qIWWFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b88d7249a.mp4?token=KQ08Y55S8tbvEbT95j79dfoghoHqGoz6pb4BB1BHzNrYZXivZaoL33S4LHCXh8tPQAmjfvRrwNjzB3vSWvlZMsMnj-fgk8wE1eykMyMXISPchpmgQrvWnQaEgyVQ0R-LOIu_qyIenp6LwYiSq6H18L4qx7wlC-ohTrw6L6H_H-j6Zn3mkjGVQFZMMvPSMMrdrHtWjGe1a8aDruOK0fAoiyOF4DmIKCM11a9OEHL2tUmjEiLJfXX--ImZLN96tOlG1NvxC9wtApbivT3h7B63HzskFDzraDgKRKaAaO2FTOcbKeqxmmlNHnwcq0pKHqC-2bvaIWt6hqbUem-7qIWWFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد نصرتی درباره شادی گل جنجالی با شیث رضایی: قسم می‌خورم با او شوخی هم نداشتم! یک دفعه‌ای شد! گفتند شرط‌بندی کردیم! بی‌بی‌سی با من تماس گرفت تا یک چیزی از آن دربیاورد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91862" target="_blank">📅 19:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91861">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMEBlSjplfy1LaSFu8mK2Lwgq1u_RY5zA113R-paeEVXRghy7Cgd1dv3-zKWvAavHzshoJyMwS80PKT8slxkJIQgEs9PZBTcgJmAi7V-CXXJ9CBzUeW42z0hDwKs7HjIHHwy-fCiO4FozzlNrCP8cOA2WCIHJazbqTXRkx7TeboRpC7SGaZsLw-zPpGXcx5QaXy51GSfimfA60NbsMJBY6Dc_yY2kCdRgZuvKsDeJGHmKa0ZpQuLA9vCx7XYhRXMRm-doXHDBabezsoPzL1yJFMAZJe0lc-UbFXrTtxHnDO5pFiVwKXkOEUvI5V3GozR3zvQG84oK10dRGJtCKrnOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برند چایکین به تازگی ساعتی طراحی کرده که زمان رو با ممه‌های یه خانم نمایش میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91861" target="_blank">📅 18:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91860">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18d10dfe8d.mp4?token=ihxCwqhUeB1tj45eERclJi7_wOyvCOMdQUcJn-AEE6vf-piw1JEoSlaakNYufYetsvm3FsdNhlhq9lMKAtekITN3SK1OGHb5mM_cNOxOXx3a1a29eANdMBlx8FZw-UNNTXylTlFyeNY1i19kKK-5U9IJDuuFW6c4RYVY4VnxzFhaKuwCo9sASxPpqq5G4MuEYFYL3_kc1pjHEB1MpA77JzE7npiVM6fuXBPVq5zqE9DdfkxI740Jg8ipO4sjAQWoBYDkYf3M5BO3aAW2akCICeCDgBxhHKgujLyPN3XMD1XqpzSQ0fMgkgTHX95EQmh2GX-o1h2wFS_OpTeoQdnDfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18d10dfe8d.mp4?token=ihxCwqhUeB1tj45eERclJi7_wOyvCOMdQUcJn-AEE6vf-piw1JEoSlaakNYufYetsvm3FsdNhlhq9lMKAtekITN3SK1OGHb5mM_cNOxOXx3a1a29eANdMBlx8FZw-UNNTXylTlFyeNY1i19kKK-5U9IJDuuFW6c4RYVY4VnxzFhaKuwCo9sASxPpqq5G4MuEYFYL3_kc1pjHEB1MpA77JzE7npiVM6fuXBPVq5zqE9DdfkxI740Jg8ipO4sjAQWoBYDkYf3M5BO3aAW2akCICeCDgBxhHKgujLyPN3XMD1XqpzSQ0fMgkgTHX95EQmh2GX-o1h2wFS_OpTeoQdnDfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
تمامی تغییرات داوری در طول جام‌جهانی. برای اینکه هنگام بازی مغزتون ریپ نزنه، از دستش ندید
👆🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91860" target="_blank">📅 18:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91859">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
💥
🏆
با اعلام فیفا، ۳۵۰ شبکه تلویزیونی که حق پخش جام‌جهانی رو خریداری کردن، فرداشب این بازیکن رو پوشش میدن.
🤡
البته فیفا در نظر نداره که صداوسیما جمهوری اسلامی بدون حق پخش بازیارو با تاخیر یک تا دو دقیقه‌ای و تبلیغات مورد علاقه خودش با بدترین کیفیت ممکن پخش میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/91859" target="_blank">📅 18:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91858">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQG49dURKXYBrRbxsGip8xtLu6g3KYUzih37rQu3BmGqXE0plYUE2-VGgF9utbWKMeRxtdMAA3jVRdks1_DbPSXiIubwKkOhEe02edjBPnvtSRTIQWWabIDjqYuCjMn3eBm6anOKHSYbWDD8J8oH2k2D3fN2BSSw56IFZgC6yiUdTDtpqMAFaHKTnNuNbhbrCjtifpblRBh6OmpHlpPniHPGWYxCvCC8_x5cUsVNtpBcmFfMoyflQf7lu7uG57l_7zfhwFoUTk3fi0lf4vfSbZXwB4xBpT0FDEvpmKi2xB60448XYemsdsvxd5KggE8M2vdczl0YHn73tIrZQKPdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فیلیپه لام درباره پیروزی 7-1 آلمان مقابل برزیل:
🔹
بعد از اینکه در نیمه اول 5-0 از برزیل جلو بودیم، مربی‌مان یواخیم لوو ما را در رختکن جمع کرد و گفت در نیمه دوم «آرام‌تر بازی کنیم» چون گل های بیشتر برای میزبان‌ تحقیرآمیز خواهد بود.
🔹
متأسفانه، آندره شورله گوش نکرد چون در زمان صحبت های یواخیم لوو در دستشویی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/91858" target="_blank">📅 18:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91857">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP5mA42V8q94fAdlZoKuakr1l1WXxA2LVb8cAwOZpCM2BUy7aX53EfqYrV0KO52LLesYVirXbAI1qd1tN8hy2BUD636Yx1o-FtAq5l6qYChII0xIlz2NnUZeibdEETEmuwezwQHmZNl6RuaWuhksfMEfDlvpO103baD9W4hhuAs-b1pN9Imm-fAHs5bmJysWyrxAh6Hsj0OHEzw_BkN-9YhVNqUu6L67dKOTM3C-Xaz4Rx_SbVj1hWUmWhttEsBPEGOS5nqNEG1caEz6kz5e546Lfu62CkXIFgmQYdy2f014IWx2fbcqQ9-4VlIXjZKmMzmyMWvaWqHl42wPAdm1Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکتر صدر همیشه میگفت هیچ وقت دوست نداره وسط یه تورنمنت بمیره، این که مسابقاتی رو دنبال کنی ولی تا آخرش زنده نباشی و ندونی چه تیمی قهرمان میشه، آزار دهندست.
جام جهانی ۲۰۲۶، یک روز دیگه آغاز میشه و ما از همیشه بیشتر دلتنگ تحلیلای دکتر صدر هستیم
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91857" target="_blank">📅 17:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91856">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgwtkcfeEA57xQm7wk8lsMi7O3gRNuPGh5u5u18ety9W97h9HQ_aPwRYWT3O0RPTAVxQLlYgbi-LF-juXH9mCTWo6_yWLZQo86Lx5Y5HaJq6N1R6HRz1-ivbsYc7NQ0h3bwm4c0Kvbg4EaM5xSoNn1b3LrvW7d_aTyLvQi5F38xpLLNtMpJKRmo_s-IK5wPoIlMjXVaOmN0ouTBZgniOYt3hp_S6pON93ZMMdoxup-1ewUddjTeuLznC2ligEqZAT0GyIliBvtzNuSgxCvo0lCsecFBvusVozEK4LRATt_0V_RDQYx3wAvvnv0nZa6Sl2_Ut-nvAUOwPwnok1Dr7Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام بر حرام بال
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91856" target="_blank">📅 17:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91855">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🏅
یاسر آسانی به باشگاه استقلال نوتیس داد که اگه تا ۷ روز دیگر مطالباتش پرداخت نشود فسخ میکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91855" target="_blank">📅 17:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91854">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tj-gbw7p6vbhEn_hQ0BnkIAK1DCHeP02FW1gT9shW1siVTBtULSOWngxifMtwoCjx3aUKPp7XKsC4UzXYmetLzs10Cji8vjG7snn7HIeFi3rQh92T1sZYH-HTA6veh0IHR371OpqPPyd9XYkxgUigw-4T00ZwPOhh4EY0iNSBwzU0cAqbBuIJkWGPfxGka_w6hkZcxxiGG449tysE4myiCaYxwt17rBGikCNwg2rsHNg54GrGwqEYaGfGiM2oNkWAE2nr_ujRc1OrhEpVzvPFlk5SUqoyAaVNYaYo5pxVaY2wbmll6IJV9TbZaoag45-1JmHXD1P-BUDaYm_j7azFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
امروز تولد ۶۷ سالگی کارلتوست.
مردی که یکی از بدترین رئال های تاریخ رو از مرداب بیرون کشید و ۲ بار قهرمان سی‌ال شد.
اون بدون مهاجم نوک، وینگر راست، دفاع راست و چپ، سیتی و بایرن رو برد و چمپ زد!
پس اگر فکر می‌کنید برزیل مدعی جدی و مهم جام‌جهانی محسوب نمیشه، شما هنوز دون کارلو رو نشناختید.
🤌🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91854" target="_blank">📅 17:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91853">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5KvYlnuH1czjnTUfYB6pyCS8__5KAuppy1CMGH7HPVkSygvw_Rq6GcGpY-8OmmnMiY_2lOFsoMITo1dEcxThkSme0gf2TuYLV3bJNxelpeE60tZEx05scqbIGmj0j504-zfg27jmTQwTjvbkf3mzHnKQQluncW6Pu6FgyYprQO6rZllRkN5IVLS6T_XDdtieulHLc40g9bUzLEsjJw-2c7Dc07tdQeb4qXXm__EAMy4x6JUwGXE3SkJGYxmJlilCqHzv3nhOQdM58_BUjFUF0fBdDo5B34FMIyzQS5FdSjujoY73h4YxaDd9pLfUnlupaWR5Y4jkleEMZip90ZAPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌موی فن‌دایک‌در آستانه جام‌جهانی
🎀
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91853" target="_blank">📅 17:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91852">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMHWzyWpNd8jb-eiZaGGRLN3gYAwTxGxPrVKK-Q-nherb2FNvojIiI1ijNMIceHnXSPCxGRH2DEoceR_Foony1lsych_M2Xy3V73q-99XATddG7juhYYAOCALRgPeMISml4s2gd0o0JkJjDA76GQ-zW4ePik1MGf3wwPUTyjjiaRwL0fiQeuaflEe189WLsyR9h5SB4YjXqmTziahtFeDv4scbwQfJ7gne01gaKl9ApuNT53HxOz09KvIZiiyorq62N20axgSaNNHnV5fweclUShT5rkKVEMtQE4Tw4UX7aSX6KsUsvHmHz7C10U6ArrQAtfjWDZaoxtlATFSkErgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
🏆
#فکت
پشم‌ریزون؛ در تاریخ جام‌جهانی هر کشوری که موفق به قهرمانی شده، با سرمربی بومی و داخلی بوده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91852" target="_blank">📅 17:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91851">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: اتلتیکومادرید خودش میدونه که رئال اصلا آلوارز رو نمی‌خواست و صرفا بخاطر شعار پرز در انتخابات، دست به بیانیه دیشب زد. سیمئونه و تیمش اعتقاد دارن بارسا واقعا ستاره تیمشون رو میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91851" target="_blank">📅 17:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91850">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0sK3CjBB_qS3FfepfV7uPv4RK8RnY_botH_jR9q6aclpRqNWdg1CjqJcTA1-Acngl7Gz_7ZtCNWsYjLlugzQvRcSFTJN_xC1tv7RZRkn8HyRZrfeytbutNlH_GvaE73fbyeS1F5KsH-7UyCKSAAj3aXObLM6_iPmX44SZEs5KICpTaOQA5cJagYB4PYRlTytiJQmd-5ZvUQJR91MY9bok-piQrcSpC0a-wcof4QyTdBW7jDOi1Z8tXeH6bH2iTU9RmjvCkq1kpcPnNO3nitAjximyRWe3Xrn_lGoXkV989Cnvxv-yZMe5ViLwWJIcSZ00DHwGZp29w8smQwz56lRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇷
🇲🇦
وینچیچ اسلوونیایی داور دیدار برزیل و مراکش شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91850" target="_blank">📅 16:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91849">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb9a592196.mp4?token=YZINWndBz-nkeE2bB5d_J_ALCybo_H5O3u8TSEpbTG1jQjZt0M4KAWCIRtM0YiWMLU5--HZxjwoFpsEWLE2ZPJofid7alAK0rUusYE7pVa5r3_mp1tKnUnINSamNrjS5g3Ub34smg9a1Ug_FcGu5ScKzkEOUZZfso2T0xMH6v6Re50E6XW49MlD0qsjbs4whGSlkuF8OicAE65tXxhy8NyoKXnP_QvES5v4D4n_lOIvDkuZIHsZ2-ugrmopDAy7hrtChfjPuTE9JhJrbU4wYQVewKggMZY_YO2-5SWlTqiy50H4CNOlnQFM7mssDWUemyJx38deHU6w1jALDnuxCog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb9a592196.mp4?token=YZINWndBz-nkeE2bB5d_J_ALCybo_H5O3u8TSEpbTG1jQjZt0M4KAWCIRtM0YiWMLU5--HZxjwoFpsEWLE2ZPJofid7alAK0rUusYE7pVa5r3_mp1tKnUnINSamNrjS5g3Ub34smg9a1Ug_FcGu5ScKzkEOUZZfso2T0xMH6v6Re50E6XW49MlD0qsjbs4whGSlkuF8OicAE65tXxhy8NyoKXnP_QvES5v4D4n_lOIvDkuZIHsZ2-ugrmopDAy7hrtChfjPuTE9JhJrbU4wYQVewKggMZY_YO2-5SWlTqiy50H4CNOlnQFM7mssDWUemyJx38deHU6w1jALDnuxCog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
پرستاره ترین جام‌جهانی تاریخ با اختلاف؛ مملو از استعداد، جذبه، کاریزما و aura
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91849" target="_blank">📅 16:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91848">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/946cc3e4e9.mp4?token=b7C7o04mzejovio2aVrc3_6h48hDaMxuy5uEiQOObTfk4Hjw3mGpE-7EQyc40pYEyqbHFqRXvwFdT5kBOWuj3IcrV3jmJ6q6R2b31UNsB4qOY4amPurdnDiUDRATtJWL2xHDuBcyM7w5AjDCbfvIWp2d1DHkwne1r-mraoKVjb40rg6UhK_dR25VB2wEk0j6R5WUJf5g46rMGLr1Hqq2R_3EUvIUdFNzP2msBZ4QBRNKbqhRjFtugrPnhGzi8RIKA8ZQSXZojw8x6mHSGWV2lxiR-7ENV9JlwrTBlVHU7nT1YGUQPUmbfcILGpsIlv38wYvzkk9gzuOARoL-2Kl2_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/946cc3e4e9.mp4?token=b7C7o04mzejovio2aVrc3_6h48hDaMxuy5uEiQOObTfk4Hjw3mGpE-7EQyc40pYEyqbHFqRXvwFdT5kBOWuj3IcrV3jmJ6q6R2b31UNsB4qOY4amPurdnDiUDRATtJWL2xHDuBcyM7w5AjDCbfvIWp2d1DHkwne1r-mraoKVjb40rg6UhK_dR25VB2wEk0j6R5WUJf5g46rMGLr1Hqq2R_3EUvIUdFNzP2msBZ4QBRNKbqhRjFtugrPnhGzi8RIKA8ZQSXZojw8x6mHSGWV2lxiR-7ENV9JlwrTBlVHU7nT1YGUQPUmbfcILGpsIlv38wYvzkk9gzuOARoL-2Kl2_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
این ترک و اجرا جنیفر لوپز انقدر شاهکاره که بدون هیچ شک و تردیدی تا روز قیامت لقب «بهترین آهنگ تاریخ افتتاحیه جام‌جهانی» رو یدک میکشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91848" target="_blank">📅 16:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91845">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZrHMX3dlZNTjn-IplX9if1kuGIz_iaV4N9PTtz1ytykgBALNnXIH772Mjeo63XqQpen8vv4eXURu07-9nl0JqwU_lGPMCrCA8Zw4F5N1PhksmjJjlf4jNNC7jYH1x7cEk9_-kls86seadvaLoFx79G1sdVGoMiEsM-xEzaSSFXqmyQTxrkDDdq_6PkKYYl--gvZFsN6LTd_5giPV0pS_Tv6dnTS4_Nlb27rnuiKgkTj7WB-ZXKARijRJsW0Ntug_zwVlcF3Pux6XZVR0sz5md5oZOydy9dVO7jOGuzNl825SnOo4j1igWUFNAzpl6bWfbMr1Z5fTHM7rc2J70aOW7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlXfT4LLMM9lR12TX580RW9p6QQ6FP9U-sE_pM2NurCkQXdMnc0k0jRWE0yQlLpJ2kA2cNsBOpCXZeFM0qkgtfUlrbyzHUjGeX45-0L3mB9daDE5HflegX9RyGrefgwXy3rwmkdAM_SleSyZX2bMZYLlrk3Ov3RfTSw68b5vhggBqkw6jLxQAH2YKcy3j8R6sENcqzZQKxLmF18J1q9x7IhJrevjjzoz8I7DSPySlYR0ETQrGXsDfprsDS8dVCWfPf-nxckLI0oKWQy8KjfdDfDyLSOm1D4t24nur-3oQj9-quRQ519R4-78WKomVn1buEaNFctGASb6n6-lVqnLSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tmn-k_iqQla07NAeYpkcod1sGSLGXCyOh7_zTyBJh4jyCViIqwe_ntj5ij9ygAsqhOYFLBZdexUWQnU4BRFrrp4Iu2rXwRxHCizm0yiQHnmeZUCU1JvA9oxroO-qGKdKgTXnyFCUH3MK9BR-hxMHeJICyhab-STc_sx2T1uJYdtBa5oxiJycRYaJYHLHVsqMbqQYcKG7c4aB3ES6clObSHgsJu1T4T9OhPDd5uCNHWTnSbUFfVjeCxBTRIAe6rcfJUNPUTpSTkyaoA2WuK_HpaGAtLP53sUSXH-DMcErgiw6U9vCvCduV8WNpAEONRxnWFObzUe0QlIe2FHtNg0wzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">10 ژوئن روز جهانی تکست دادن به کراش یا عشق زندگیه، برید تکست بدید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91845" target="_blank">📅 16:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91844">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPM9tsM5mszX5xVBG3XGSWPIDwRlEe0TXiqgFYFA_paQjAItuHxR15O3AKnt3ku4_EvsxS765yunbBV4hCctIBJgY-qTmv3r1DFcmDKYIjqEWiFEfzrSUdDu3JIrxjL70CQu-wxCYw5bzMw1Hc27AWGJX6KE8JBlcldpeMQMjxQgSTYWYM1oKF_N6SDqO4zhBNBzFAaFdDB5tGMZXe-KfAlmd6toJ8R755bUKCvhhwFsC-oebvkwgRA5K62myFStJivAELOnvUlUIrxx9cGmRvPfog-TY0Wq6KK8Wj-Mhty-69uNW6JBGqNVmMzFKnzb0Cug6YyyihdARiBwZT8ZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی رو به هر قیمتی نخواستن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91844" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91843">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb43e1318.mp4?token=TGWr4V1dzBob-XtzBxaaIwnfNNJmEEaMbdE7NZ3d6uD7XvTq81_QttSjZC2tlXfn4tcJuDmWlajPTWRQQXxh0Ko640zKPzcs7_NxQjenlrZjhk31YsKkIPfEc6X-tc10Uwg2AUsiooFCS-rab-RpO1P2rmubv1Z-YW-KybQy2_0NGJy2pWDr-1eG8EPge9-mQpcDQyWXgy8vn4FwF_aUHtCh9kUvRF9O3zoGxNE-5nUR3ilx2a1P3IHcaah9my2yqVymOv-1B2T_4HvePClMmg_klQg7j2K8RrL-94Lzi6L7NvcuBEyiXBy5gDpiYDeNE9gH9kg1aOpPZ_fT76F-dzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb43e1318.mp4?token=TGWr4V1dzBob-XtzBxaaIwnfNNJmEEaMbdE7NZ3d6uD7XvTq81_QttSjZC2tlXfn4tcJuDmWlajPTWRQQXxh0Ko640zKPzcs7_NxQjenlrZjhk31YsKkIPfEc6X-tc10Uwg2AUsiooFCS-rab-RpO1P2rmubv1Z-YW-KybQy2_0NGJy2pWDr-1eG8EPge9-mQpcDQyWXgy8vn4FwF_aUHtCh9kUvRF9O3zoGxNE-5nUR3ilx2a1P3IHcaah9my2yqVymOv-1B2T_4HvePClMmg_klQg7j2K8RrL-94Lzi6L7NvcuBEyiXBy5gDpiYDeNE9gH9kg1aOpPZ_fT76F-dzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇳🇱
جمیعت فوق‌العاده هلندی‌ها در آمریکا برای حمایت از کشورشون در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91843" target="_blank">📅 15:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91842">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
#فوووووووری از اسرائیل هیوم: وقت تمام شد مذاکرات شکست خورده و پاکستان از میانجیگری دست کشیده. ترامپ بعد از حادثه بالگرد و حملات دیشب بسیار عصبانی شده و میخواهد هرچه زودتر به جنگ باز گردد. پنتاگون طرح های حمله جدید راه به ترامپ گزارش داده و اسرائیل را نیز…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/91842" target="_blank">📅 15:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91841">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
#
فوووووووری
از اسرائیل هیوم: وقت تمام شد مذاکرات شکست خورده و پاکستان از میانجیگری دست کشیده. ترامپ بعد از حادثه بالگرد و حملات دیشب بسیار عصبانی شده و میخواهد هرچه زودتر به جنگ باز گردد. پنتاگون طرح های حمله جدید راه به ترامپ گزارش داده و اسرائیل را نیز مطلع کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/91841" target="_blank">📅 15:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91840">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
ترامپ به فاکس نیوز: به صدور دستور برای حمله‌های جدید به نیروگاه‌ها و پل‌های ایران نزدیک شده‌ام.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/91840" target="_blank">📅 15:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91839">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
#فووووری از ترامپ:   نیروی نظامی ایران کاملاً به هم ریخته است. بخش زیادی از آن، مانند نیروی دریایی و نیروی هوایی‌شان، دیگر وجود ندارد - آنها کاملاً شکست خورده‌اند. ایران فقط حرف می‌زند و هیچ اقدامی نمی‌کند. قلدر خاورمیانه مُرده است!!! آنها برای مذاکره بر…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/91839" target="_blank">📅 15:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91838">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m36wAGXJ9C1MvbkHKYnZm9DnhfDKypwmSlIS6SraIYaqEIJ_hEf5s3-6CDE9CFYVzWW3Z8vPUrwjLeRtw2-FTdGayYdS4HTSdQBt-6nBMYVX9Kqld_ljx2sYV1cDHSSBPa68IU07klBk59wyuCLrzZPTeJQP75Ly19oyMCEPt2qF45H04IuBddneM-h3in6tLmX8wq3guAJPX1tUN2iBwtWXEEPLmURWvHS4R08EYunyFNSnPUfLbhhdWCZ0yV-hU1dblbuMWs83hEf_7eoB3CGB6qsiluASfgey1PDziMA7kPV7Y9dY7YK2csBLjQSkHe9fbazT8ThMZ3KQOjpGjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#
فووووری
از ترامپ:
نیروی نظامی ایران کاملاً به هم ریخته است. بخش زیادی از آن، مانند نیروی دریایی و نیروی هوایی‌شان، دیگر وجود ندارد - آنها کاملاً شکست خورده‌اند. ایران فقط حرف می‌زند و هیچ اقدامی نمی‌کند. قلدر خاورمیانه مُرده است!!! آنها برای مذاکره بر سر توافقی که می‌توانست برایشان عالی باشد، خیلی دیر کرده‌اند، حالا باید بهای آن را بپردازند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/91838" target="_blank">📅 14:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91837">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMyj-mMZOiqC6swhm3T7LEmZhGWufhDOkc6yEbv_kkyW3v6C4KWglBLUGmAP5GAMdGjT5viYEp4bvxIC8x9pTAePMgjwyeSC1tSEc7B_pOZwpSTBFzYLIkdAEbimE52vybMFJVSbyTUrdjYqXm0q23AuTKkKJrLhr9Od7SQl9gJHhg96uc4WujgYOT1e5gXT9wFvEOX3q_z0uMu83M9d41ETtBAIj-C1W0K4EC7CWleUJnUWHG9LBx3nmrYrCic8zCYXUb7uyD8ctJZk4AdWJu5SO9hbcOpt7eLrx5c263nV0k6AhVYiW4OkJR5CNWJKPKWk0yag87E2pOEP8d4org.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکتیک‌های ناشناخته ژنرال جواب داد و دوکو امروز 1 ساعت تمرین کرد و بدلیل مصدومیت تمرین و ترک کرد. هنوز میزان مصدومیتش مشخص نیست‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/91837" target="_blank">📅 14:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91836">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-v-nYaz3tHOwSf3HORhxrZ0S4i3Ts16ZIZ8IDdlXzfFgRiJ5W2sgZwFxQAsm51Afyi2NYcMirnsbq_Ty9ko27sL58UcIlXmBV0I5qwaG7ocoRVF_y8xHeyyQhmGrVi_hCvVXyaZHZseuV4Ln58IGC7gFRN588PiZq9L6ifzxzebySP8-ioxyL7V8QWv7o2NDQ4NXLqDDnDMtF9MVGHFTVEDbm5nsz3-6KcggjUbOUA1mAgXpjdOfXUBpm0smT8AUQ474zc669o3FrETwYgyJzOnVMjucL_stqyiJm5NWyqmNwHmIG2ovdxwQ6Psp5KfrVZHW_915gFp1p_8OP_FMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عمق اسکواد فرانسه برای جام‌ جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91836" target="_blank">📅 14:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91835">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlcvsJd7MX-FnmKccSU2MMdy33zQ6huqt7xQjc0M1QDo8G3Tt-o4F0tU27doLewRJ7AwP-O8RTRJFPFxB7f8n_iO_yWufmhKt9F5qr47wyX_C1YVbry67YC5V0H4k_U_p1UC2VST3neoVZcMT61vXugasutQVKZt_n2nBIZImMIHMoTgB_R5hXB3ssHLYmeai1fSo3sY_LggYfmxRgIDAPkiitmQvs6toYQuFNdh_yYnAQUqtJ7Xfg3XhtDFczOssqY0qdyPqm97hinoecSWBslk86u5zODTDgsI_Nu3mR-HUvxbHYNrA9_kAThQNCzVBV1kNvZ-qWIQY9X3VlrUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گرون ترین بازیکنان افتتاحیه جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/91835" target="_blank">📅 14:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91834">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_QNHOZJ8NLLp5CpbugPxlzAqeUxQ7cJdErd8mt17fYJRjRD3DBP-2-jIGR7bFWgsBI79OauaYt6HQmKfFq5ymnzeRtt_v8IZFMtoUL6bNhFg-n1kIJ6hNivmy2rBmssGT5YQltP1y7yeY7_1-xk9PjB21d4zZF-yLNJkxsB9cNpgaUjBnWd5_u0IVeij7GwPAMfhyZpiOesVKam2hyYa-BMuJ5Hs2hdhe7wK0LleX2iWn15kuhdzcrKfOq-jqqSa0cSGjNkce2M4Kae7_jBOdMSVoGrvBoHlKHUXwfb7aoK_XJayhlyK9DYzanq7B4KrY1roe1bz6hreUxQb-jT3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوین دی‌بروینه:
اون موقع که دوست‌ دختر سابقم کارولین رفت مادرید، با تیبو کورتوا به من خیانت کرد. وقتی فهمیدم، انگار دنیا رو سرم خراب شد. اون هم‌تیمیم تو تیم ملی بود و هر روز باهم چشم تو چشم میشدیم،، تو زمین فوتبال باهم چشم تو چشم میشدیم ولی دیگه هیچوقت باهاش رفیق نشدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/91834" target="_blank">📅 13:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91830">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzE_kmQXSaAMalwwWgp6ripSgNd_0Pjg5OfVuWztt3tI0n1LZ9PNZJOSEGp8MLExJ4yAVMgcE5nEMeAjoWWvOsqMxA8N7sygkzZQ2zxAmLkGPtdzBWtHwy498WEGya5grQ2mbJEScKpTqtfRRI6GKX70qlo66xUgTNIVQYH8mbWwsAXp_8mDYVzApgUW4twB0p597PSBagi7kNoG9W7lQC-aJkdpCmb2J3a4WOE2ohPthjNUAie_0JYFN9KVLFs8-lbgpY18CczoHhqHTfxHu6apoLMN6MTTNEk0cXOi3cy7d0PgcrheIXwMWFHwqhqe0lUOuXODNkMthtqOYbU7wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
مارکوس رشفورد لوگوی بارسلونا رو از بیوی پیج اینستاگرامش پاک کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/91830" target="_blank">📅 13:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91829">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/334ebe9810.mp4?token=pbQT3RjGgyqdJpAwxNI2EIo5PSsGdlZooBSX_yoA0GQ-VMVFOf3sSCmLuHLcUdsYfRr-V3jL1wBGKd6kRIQOdrCSe98NBIXRRkPN_gL4SkadWlW5w1E0TKhAuwhIKm7aCbDohlvaUCM4RkiLTAs0Lj9nx8roni_AwUasSBd_2VaWfsydBdQVjoXyGltGCZkC4tgNSynr8Zm78OQe0n53gv5GTjGelzGpvmXFGr6IneT7wYJ97nfE70x1JL91b8KKDslGTY2YMbZ2JkN5gj-jIMgZtYJMVKfvmQwKrBxR-v1c1t0qS8WIRphwVjwWjECCvT709gRhd2NnY_jVIvPgXUFa7JRIkkOK3OgBbGQBwGZLy3YJLqGAzVjX_rR5lG26gESsY_hB01bXbINXF4DWoVRNPevrt1LP0cDAc01gk4Oax7Y8HC97qplv4aUPmt1BF6qFhZ45MZXrTGhnxVFOoHTUtmGjAcgFHny3UU5Q1f2QElp2tAWiIFreJNiy_ky_pt5lguN033Cs-A6mG5sGz1N2mX3cHXtp9PgVQ2Hco5PH-_aMNBYQmIXZfasSzEBkBe1THgDCPj94qZ_5NuxO_guRpFEpoAO1nVS7iNJoBDbY7M9BuQxWXATQPkw6gEiqJFJz4_7loukEME7ue7UUCg1G-gAKE0khITW5cYwc8Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/334ebe9810.mp4?token=pbQT3RjGgyqdJpAwxNI2EIo5PSsGdlZooBSX_yoA0GQ-VMVFOf3sSCmLuHLcUdsYfRr-V3jL1wBGKd6kRIQOdrCSe98NBIXRRkPN_gL4SkadWlW5w1E0TKhAuwhIKm7aCbDohlvaUCM4RkiLTAs0Lj9nx8roni_AwUasSBd_2VaWfsydBdQVjoXyGltGCZkC4tgNSynr8Zm78OQe0n53gv5GTjGelzGpvmXFGr6IneT7wYJ97nfE70x1JL91b8KKDslGTY2YMbZ2JkN5gj-jIMgZtYJMVKfvmQwKrBxR-v1c1t0qS8WIRphwVjwWjECCvT709gRhd2NnY_jVIvPgXUFa7JRIkkOK3OgBbGQBwGZLy3YJLqGAzVjX_rR5lG26gESsY_hB01bXbINXF4DWoVRNPevrt1LP0cDAc01gk4Oax7Y8HC97qplv4aUPmt1BF6qFhZ45MZXrTGhnxVFOoHTUtmGjAcgFHny3UU5Q1f2QElp2tAWiIFreJNiy_ky_pt5lguN033Cs-A6mG5sGz1N2mX3cHXtp9PgVQ2Hco5PH-_aMNBYQmIXZfasSzEBkBe1THgDCPj94qZ_5NuxO_guRpFEpoAO1nVS7iNJoBDbY7M9BuQxWXATQPkw6gEiqJFJz4_7loukEME7ue7UUCg1G-gAKE0khITW5cYwc8Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادار زیبای عربستان‌در آستانه جام‌جهانی
💚
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91829" target="_blank">📅 13:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91826">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2045d7e9e1.mp4?token=Voo_Tt22_qWpGaraTIr5dPG9DG8nAt9M2XkrlIO7dsqX9h7bqPMfamPwrSKlTZT6Npv_p86lYF6WKPTOCUVwSdHoquBr2zZrHlJHjHkdS6PZ7FdQy51Gj3MjBlYifskS3932WRGJXG4VczsU6wjXRaD1UFqspJhXH5GiNSBK8KCGAF-mN1uGWdRkag-hf1dqIWxkEG1SOjOTC93nWfsJV8chMpAuUEM8RgqO1UxwMSaVWhHTQz3LnmQVgXEMyiPNDO3HeRgayC22ZfMAEvC1mMIUCxLtQLbKppCgh2FvoBFhk5jlwqgHPOl9GTUfJIqjbYTF7Y197_D1qqlZTvdRYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2045d7e9e1.mp4?token=Voo_Tt22_qWpGaraTIr5dPG9DG8nAt9M2XkrlIO7dsqX9h7bqPMfamPwrSKlTZT6Npv_p86lYF6WKPTOCUVwSdHoquBr2zZrHlJHjHkdS6PZ7FdQy51Gj3MjBlYifskS3932WRGJXG4VczsU6wjXRaD1UFqspJhXH5GiNSBK8KCGAF-mN1uGWdRkag-hf1dqIWxkEG1SOjOTC93nWfsJV8chMpAuUEM8RgqO1UxwMSaVWhHTQz3LnmQVgXEMyiPNDO3HeRgayC22ZfMAEvC1mMIUCxLtQLbKppCgh2FvoBFhk5jlwqgHPOl9GTUfJIqjbYTF7Y197_D1qqlZTvdRYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
جام جهانی 2026 ساعت ۴ صبح در خاورمیانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/91826" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91825">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Riet4fkungJt5v34J9S9NtZN1ECiocembPPQuKDD-CP4dRK44vRWJxrUcF-kfpEUtRDMMRE434NgBe8OG75PB6j4pGLWiZOfk7ftYB1gQyGc3TrFEcO8onAReqW1lIKFPR9lEhDaKo9iDjNrAjf3eYCLNZgm7VGAQb9oPJEV-vLNhkDMI4ZbAnUVJ0HZm7kRj93BAK5ayahPWGv3LrAzqHlC4xoprACsxUrD7JPtdIMHwMgnTk5nGfmRm751qJ0WFpfpc_-ovyKUQZezt-JG0ZOD3AIOtMIzIcxwT_5KQMNKrmSMnbBNZCWGThGPBUmOAGJrbBZdbEFAjR1FYSwnig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
مارکوس رشفورد لوگوی بارسلونا رو از بیوی پیج اینستاگرامش پاک کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91825" target="_blank">📅 12:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91824">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
ایان رایت: رفتار میزبان جام‌جهانی نباید اینطور باشه. این جام‌جهانی، جام هرج و مرجه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91824" target="_blank">📅 12:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91823">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPv_0VJTO4mCM0lREodjKovaSQ5wdnGXFgvneNtvEOMq6RGRR6a5Zf1HjlRFsmXol6QRt1k9VMaYMcRx8zMePxo_MHZyxhQ1qepyKuVUZ_rM_8JH6hp6eveTYJEevV1Z30Ql-mGKqAytBr_MgdhavoR0l0fmaww8YFO8OJ7e9npoJsnt5E2aRqtZImWIbIjjpm4CiZYL7yOSy1nN__WoGU0RfWCz2Q5LEuzRFPTbe1C0jpFGCQZZJ-5MxD6s2LSFh3djuKGSOjfO5TC2i8JY9pym03qxUjEEAcCTk9NKShmp8Tv833lUwXRd9FfvXrqQpBDs7evIKfbWzp8ZhEnuGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خامس رودریگز:
🔺
وقتی به قطر رفتم، پول فوق‌العاده‌ زیادی به من دادند اما زندگی خصوصی‌ام کاملاً به کابوس تبدیل شد. فرهنگ آنجا آنقدر متفاوت بود که نتوانستم خودم را وفق دهم.
🔺
با دست غذا میخوردند و به من هم می‌گفتند «بیا، تو هم با دست بخور». در آنجا دوش گرفتنِ…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91823" target="_blank">📅 12:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91822">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de86721b1d.mp4?token=eO8SYkZ8Ziw7RC-TIhaxcddRsSOgRPZW1JNo_VYaGSJUHFInSbM0vog313_0n24pV7IctN_SLqEmYPZdknCQVQxaSsyEoNBcTVHN9RTsoq0rA_g_h84JWcEvIG177557qE3qsHKArg1TpVgPJY3dZDWOr16JarFRs69KyfQvFA-CXf7KmHQ_2jT9AglIVHVrZH_Ma7JQhUZ1SmWSuKZTG77rX5xZ4-8yHnwkCT56NBnq1VdzUdvKXRpx5OxxrP5dWPEZRGu_As0plbiSTlYjykSToWCZc5BFHJtvXZRq004XlIOf19-Jtnt7Gat9d7bczbSqUpXfNIYu5RN8LYYDjK92vtr2Uab5TOaex8-2PWPMVJ7LpUo5HuQXrF7vh5sS2BGoN1fpX2s3Uj1_szK9LlZtraNZ_sCRiMSuKGwp1sz4uxbp0wrmdLa8ruCFjEcdUMItUig66PtOFrOK3OpGFYbcW8Qp7TepopaqTDFv9pUkDscpHg8PgaFjXPkWCHEK6kh3_S-BI9TKxCoSFUI9_l_7zczpVzbarmtWtFoWCUoFsscJuSkfELtLn9vmXm6XmMQp1RXKM87DNBwsAHBL7L9kn05H3Lxzj25kT_Sb1FeeU4BWc3Qub3AhsaY6vsDUYe_GYKRYGd08bW-Pv6nN_IjDpkjOrZpUBRNxXdaDnOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de86721b1d.mp4?token=eO8SYkZ8Ziw7RC-TIhaxcddRsSOgRPZW1JNo_VYaGSJUHFInSbM0vog313_0n24pV7IctN_SLqEmYPZdknCQVQxaSsyEoNBcTVHN9RTsoq0rA_g_h84JWcEvIG177557qE3qsHKArg1TpVgPJY3dZDWOr16JarFRs69KyfQvFA-CXf7KmHQ_2jT9AglIVHVrZH_Ma7JQhUZ1SmWSuKZTG77rX5xZ4-8yHnwkCT56NBnq1VdzUdvKXRpx5OxxrP5dWPEZRGu_As0plbiSTlYjykSToWCZc5BFHJtvXZRq004XlIOf19-Jtnt7Gat9d7bczbSqUpXfNIYu5RN8LYYDjK92vtr2Uab5TOaex8-2PWPMVJ7LpUo5HuQXrF7vh5sS2BGoN1fpX2s3Uj1_szK9LlZtraNZ_sCRiMSuKGwp1sz4uxbp0wrmdLa8ruCFjEcdUMItUig66PtOFrOK3OpGFYbcW8Qp7TepopaqTDFv9pUkDscpHg8PgaFjXPkWCHEK6kh3_S-BI9TKxCoSFUI9_l_7zczpVzbarmtWtFoWCUoFsscJuSkfELtLn9vmXm6XmMQp1RXKM87DNBwsAHBL7L9kn05H3Lxzj25kT_Sb1FeeU4BWc3Qub3AhsaY6vsDUYe_GYKRYGd08bW-Pv6nN_IjDpkjOrZpUBRNxXdaDnOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تمرینات تیم‌ملی انگلیس در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/91822" target="_blank">📅 12:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91819">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cD_Bvq0MmKTuzIge2yFIUp5cBiiJDnoATZFEBO5jH6lV8E4vzwAmwdV6lR5y2O_DueaBJKjKxE7IjC3izcrLj-LIabnaMqVEAcUeOm1B0uWDIzQS7GR-iH4uzSB4TicNS57eb3M6eF8xyuO9-OJKscQaE1nqI7ktSwicGgrUjfo5ymGIgK6eOJMtiKK1v_xG_GfwRMaNNh1yl4D6lXuebjSI9GTHseiGzlCI7Fr2AzazBjcyabxG9hRcXXr-6cQEz4Qk7oDQjsGeJRNhU69V6PsBXwCQIwYU3kILEq_YgWAtGM8ugbmHZESuOoppSEjavu-cQ0VETN8LrZLHuR5YUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJd6Ru8b52ztG-BO_D9JyA0Bjs8Woa4uIgzH2ZR2Bj7H-tBLOP9HI4yjPgtDvH5LvCc30pB2PgSEr3Qwj2PZPo3L4d5h9W8eO459ZCDBe_cDqDuu2dV90CZhGKRdeazdaF3vE6fa7BueqaRRGfPfG2EQIQP8L80uHAmJXK_IsKsxWFW977At2Mv-5x-YorQimYO_9mzna_c1qKUimkhtgrSoMpo-AiMotm0Lu0H3TqqiTNeoRojhwR_qygDfX5i0mxo5ULKyS4SsNFX-G2Y1jpGLVyEz2ehyhAD7AZ5XZq7ttYFhlmhsuffbuksLak4WkL-QJegC06bqR2Y1hxrQAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AA5uqv9TRT_aSeFagK8OvFGb4BuQx6aFY3Owxn3XMfgLp2xLDktM_CZbilWKlwrcxCl0yfUPoakHBeo_iQRiLfKA7f34tFpWzRLvAf91yP__amnEWN2GaS9xN4NSK4fpp9eQOXO5gcQhzr0k2lz4kJLAhZoHVgV1k3k9qh2NJNpDaCzWlwjq37fUAtQ-6tJ5JFJDf1BUywGh3DISPIdFboayfawjWUUMTjqI4sI5B-efCpCQlGLq6PFHqd1zSQYglCH3sgtKzvNl4zUrFh-RGpN98iWLnvJzryuYDCdSUmBdzGkYiRiZtdmuOB_7xRFCGWQKLdtxtHXOZqmiqyvHfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اندریک و همسرش و بچه‌ای که تو راهه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91819" target="_blank">📅 12:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91817">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tI-tW34yCVEAWxz2lOjdWiaBRED1HtvE4k4c_SHTXG3MrihHw4aQifAUYdS7h_aeL3XI8wJG6ZfFLHuyYF-n-P3LsP2H78FDhe5UXm8EhRl7o9Wr1VXMJbaUhQ4EUX3mMl5O_NXGzNutzx9UkTS_AXb30vkhURwvuRfeF3pjM60He6azYWV9lI8it8C1ws-0P0-e7EaqP-KYb_Rzrr00js91Z30Fo4g6L3d6GhYZERORAyj1cGmegd3Q8vuer3AmBkddUCQWNolrQEfrHJPPCLvXomeWamNTM2b-m8aXksAQt9GWNpCTmKAUAY2VPs5nM3FbAq2A-r3YZXJAy2YRmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/goADTslQhzfGu-0C3pClFVslL_-7FEghCuFbaCPnB6Enun9XGZH7QIWfdLnU-DGoKbXaSNPtn_tXsMUwnMAQtSSRlkXtuM5tTkv5RXHaPfB0vNBbL72cEpJwEap5YXCOCUaNa6wFzCjbw4of3qxXdLkXDfWs20-rZW3NO1nHicVQFR3-l562XEneBKM-_b0IR9nRZZVe9wuc4Vand3zOZR-tSSkxGL9E6XcgwwnbWbSEL901BVQyMv7fOc_GfOnSO1Kk13T058nwpR1IUViqXEmJp8so6yfgmpkuNHgSsFBd5sjdt02abX0iT49OaMvMV2xLe8PQsgepU9Bb0ghPOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حاجی دیبالا چرا هیچ تغییری نمیکنه؟ لاشی هر روز داره جوون‌تر میشه انگار نه انگار که 32 سالشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91817" target="_blank">📅 12:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91816">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4dUzZhiyS2eFaokB3Ziw9Surl8PIjgbzTJ-WhzyGwtysv1J3JRmQfsCD5CPNwXu5YHpqAIOEPiqlb1MULzAlCUI6P_BQxt0tOEdjtIup_QJx15Ij8faioAPRDAJUzzS1hOxhoD6lG5Vif8PisgTKuExTp2tnd8WNqGjB9pxFKIbq3Obs-AEWyOn0obrgwnCtakx0YopUkss9819c7JxA9snBiCQI7aqwD2b_8G3vbVSvEh5bQyPYDTnL-boWtBX8HhbOuQk4ix_YpCiJzb3fISVMnAwN_BWzdHcs_vPpSRdGwGDPZapnKvW1I6pOSUCwF5-NsXUmlkutGZYWSlyEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پوستر فدراسیون فوتبال جمهوری اسلامی به مناسبت یک روز تا آغاز جام جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91816" target="_blank">📅 11:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91814">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWgLiRJJmsoendnpoMgQzRBAEm3-eDXT6TkK4j5daY0hcM9RJ7nnQKpDhYTIXTkGgW3kj3t4iZFoURefFrg7sjyGDw3RnLXvwIZqtPwR3QPWBOSzAluNmTSTS6UnNLW0CQlCVCHkKTIWbiyRx5rg0I3YauAM7B5X_bh4h47mMtMjmBh1PMXRDuo1RIkT8f_KCZ6PjKEygct9aukHTGIvxDqgZtH2IuJfYjaRD0aseqo8CvqYQq9535Au7xrSaytqohJI7bzTkUPh0ipZyfxt9N6yh2FMD4-HGxarG9JEJnilzNeQcvq9Nr7L9qULkY1JsGtjqaaD14-C0PgwBWXGlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
وقتی در آستانه برگزاری ششمین جام جهانی دوران حرفه ای خود هستید، چه احساسی دارید
⁉️
🇦🇷
مسی:
🔵
بله، من واقعاً از همان ابتدا از جام جهانی لذت می برم امروز می خواستم مدتی بازی کنم زیرا با این مصدومیت کوچک وارد اردو تیم شدم.من خوشحالم، از هر لحظه لذت می برم و مثل همیشه هیجان زده هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91814" target="_blank">📅 11:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91812">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0475ab9a4f.mp4?token=Jc4jso94F74OJYWV44MwO4fNVG_ej29Y43TiDV2LHRH298tCIDkMqxc-oYBwqxfCgOWWp0BvWs73SVBmI62raCUQdAghw8hxVRHhBjJjroqttfrKcd-LO_TyqWOm-NPUXq4wWGeucRV2EE84c6NRSObGq5qmcH1XJerBV1WVlvW5HyIqIhAROqnQGVj3WJLHzbQ6cJEgpoMHPdbCsOCYeZTMO_4fXfS9h1sCy3a8qbfOZzLqLeTLhsMAh_LPUB4oGOMTz5ytYY7YXDKWL4Q5SLrsYP9_k3g4PJEmNcnNAHmrmynNexBQk9Mmn7COJN_Y2JDtjSpfwZbSBvUnkxNZ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0475ab9a4f.mp4?token=Jc4jso94F74OJYWV44MwO4fNVG_ej29Y43TiDV2LHRH298tCIDkMqxc-oYBwqxfCgOWWp0BvWs73SVBmI62raCUQdAghw8hxVRHhBjJjroqttfrKcd-LO_TyqWOm-NPUXq4wWGeucRV2EE84c6NRSObGq5qmcH1XJerBV1WVlvW5HyIqIhAROqnQGVj3WJLHzbQ6cJEgpoMHPdbCsOCYeZTMO_4fXfS9h1sCy3a8qbfOZzLqLeTLhsMAh_LPUB4oGOMTz5ytYY7YXDKWL4Q5SLrsYP9_k3g4PJEmNcnNAHmrmynNexBQk9Mmn7COJN_Y2JDtjSpfwZbSBvUnkxNZ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
رایان چرکی و دلبری‌های قبل بازیش:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91812" target="_blank">📅 11:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91811">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iux2fh10BKxayeE6adTv8p1G6QCAOYWk5zYHeKmK7-sbqpxOHXDxQOrbCxVGN1HgfCa_kc6IWS-b4MSVvNLLTtXWtuCNIA3cLrjJgfMzz8q13Q8oeDjRkUU0kQ-ZgjMFJKZT_Sf39zY5gQa54wtq_gsfdtnnShzbGgXIxwhnR1vANRz6TBF-tEWQ1BiellGNcax4_joJlAPR91jeXeAXjHsOZWhTCvMhn-XIUReaa-ILg2DxhFCa1XAG2XHL_NSTqtVbzuspwd-KDmHMI2swNj3ytX4DE7F-d16i2EM1FopuQWUZuGF10IETbI46RXuX12GW5frLWV5iN5ovkeHTng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال مادرید همکاری خود با آدیداس را تا سال 2034 تمدید کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91811" target="_blank">📅 11:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91810">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27028dcf2c.mp4?token=EeSB0Fy3bq2mQ0uK2tcdNnUpdP-EM5-jDt0NNArZ2D_b5ugVqml6p-CtnGXU4VZ4j0MuuNB8ANiklcOlvC0aWQHNhHFUpPADKMNtPVLmf2QSl2mgNDYUckRRL8wmuiQbQJ9ym-OsTvIBtwMC3AckswN1C-ED-wfqySEjpWvDU4K6naCpVGF9iFC0aIAsDhLHGdUbwTkogWs6SNIE8zbnY77TUj6o7Adqiv4JwTYC_3jieyT3qfAGS2Iq76psQeLSfjBd5A96vBOAehVDLVGGNTXV4Eg9QJgwW2ThQBpbA1TayH93hP5A4P-sUy3elDVjR4G28iotL7aA6SmXhxQMBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27028dcf2c.mp4?token=EeSB0Fy3bq2mQ0uK2tcdNnUpdP-EM5-jDt0NNArZ2D_b5ugVqml6p-CtnGXU4VZ4j0MuuNB8ANiklcOlvC0aWQHNhHFUpPADKMNtPVLmf2QSl2mgNDYUckRRL8wmuiQbQJ9ym-OsTvIBtwMC3AckswN1C-ED-wfqySEjpWvDU4K6naCpVGF9iFC0aIAsDhLHGdUbwTkogWs6SNIE8zbnY77TUj6o7Adqiv4JwTYC_3jieyT3qfAGS2Iq76psQeLSfjBd5A96vBOAehVDLVGGNTXV4Eg9QJgwW2ThQBpbA1TayH93hP5A4P-sUy3elDVjR4G28iotL7aA6SmXhxQMBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حین‌بازی رو گذشته قزاقستان، دوربین عنکبوتی معروف از سقف ورزشگاه ول میشه و با خوش شانسی، یه تصویربردار جون سالم به در میبره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91810" target="_blank">📅 11:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91809">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So01EibIUDbDlZH6jO4mnb7mBLAmDDKfYKqC9IzXrodJ5LtOp_av1TeTXOVZHuqNqNAL-ay5tG6xoWKBWJ8mbFGD9XeavGvHZLHVDe7AEbsC7Ea4Oz4krmV6iJtBe5m2_NJwZRkg9BNj8Bi1Y4O26plA6WsptyBGkoX-k0aJxyYfXOXu4ydAhO6rmCCsW7w8ZQlzJXvQOMin07tPHnD1VbPdiR2lVYHb32mY_CTPG_tjovWxyoxW3oZBHEV_JwD1-TnhTSgp4FC1kimmnZM3X3dBysVsdG6QEsGTd8tbwD8FDmVW7RARgGaMMOchSb970AshDEkQcE-HHgeJ_Z8ZvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد مسی و کوارتسخلیا در پاریس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91809" target="_blank">📅 11:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91808">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYFw8cvxELzw2fpdpW8KXgO-E0sOH6LsZ77b46mZwvlSlvfOMeHm20KjMj8bBdf22X2N8mXIgs7JluXt6-euvYT2XrijtPCK6ixzgJZjYotu8zrzvlDuuVy2GKTDMHhvXT7_emVF2szSeKEytm1M75e1RxvGPG-u9OjEQouhqwIO1_5ohO8L6gvCyUp8NdwFlUCnkztYZhQaTeasUIuu8RztDccWyZeUYQxxpv1Vl6KKsqYzO3BfYM4OZEdyIORYKn9GnZDxOiLHQcfnlZC8_C3mFFqsmQvEPpaS-teNYH4hridYuPuFEAIk0JeyIiNGpNfPFfH8hr3GY311Ep9Guw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
کیت جذاب نیوکاسل برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91808" target="_blank">📅 10:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91807">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03756286c7.mp4?token=hCAljfr7krfaQNs7lKvWqw-otI8iI980rh2YWWD-T0v2W_FgYPbCbBbz7T3lUCxda4VMNDQpnyNFqkbtVCSk1Vnor-D3jUJaHjEIqC1mebSp9Eduqg8lme47R1BoyXvhQYJxtnWvbWfraKAecZSUSsNvrk1uxV18rlDMLO_X49GiOeGhdjAfXiK6LPMVSJAuoPa8AnveobUFvow11kFqVQpUgW7b3zY0YDI8xaIbeJaqApPaKzsLBK-qTywtBwX8RL5k89VlxmqnrZRCGfCDizHSk9pFH57NS50dzbuwOkAFRps1Y-kDjdQXpiCRRTvetJgoDyyUp1t40vXsvoa49g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03756286c7.mp4?token=hCAljfr7krfaQNs7lKvWqw-otI8iI980rh2YWWD-T0v2W_FgYPbCbBbz7T3lUCxda4VMNDQpnyNFqkbtVCSk1Vnor-D3jUJaHjEIqC1mebSp9Eduqg8lme47R1BoyXvhQYJxtnWvbWfraKAecZSUSsNvrk1uxV18rlDMLO_X49GiOeGhdjAfXiK6LPMVSJAuoPa8AnveobUFvow11kFqVQpUgW7b3zY0YDI8xaIbeJaqApPaKzsLBK-qTywtBwX8RL5k89VlxmqnrZRCGfCDizHSk9pFH57NS50dzbuwOkAFRps1Y-kDjdQXpiCRRTvetJgoDyyUp1t40vXsvoa49g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بارندگی در استادیوم آمریکا حین بازی تدارکاتی آرژانتین؛ جام‌جهانی با این روند ریدمان خالصه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/91807" target="_blank">📅 10:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91806">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESPScS0Sy8eOMagP8staA79g5AvpocyDS1qTWduOi07_oYuztreWGbK_DN8NeGpE6ctAOWDilvg6TpycnSgn6eWhgtIzUn3cYBSyggk7l0zK8rJXdfc6MopLlQPEhlTIrWlhbP_HDO1mkxu9Hh1j8As_D1IRnU_xd6-IRsoZOufH5p0nbMMnOxgq76lHRiYrxfYEiKYC4RvqLkcTHOhqoP9W0aWJPaP5LVMvslgrXZ9kjbqaQ1sJlv8czjeeG2NYjZUuEBYBAFv0G4SdfcbHgeUn_oIKwNeJyLkxlRszkIm639fFf0lyIgtOEUot93Aqvjz_ScTtxeZ7dk86PoXLiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی با 38 سال و 11 ماه و 14 روز مسن ترین بازیکن تاریخ تیم ملی آرژانتین شد
🔥
او رکوردی را که از سال 1957 در اختیار آنجل لابرونا بود که در 38 سال و 9 ماه و 8 روز به برزیل گلزنی کرد، پشت سر گذاشت.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/91806" target="_blank">📅 10:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91804">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hevt1reVKCHrZ1cP0ho5pp2oETVYkTzeVYlj9wPpb_93oE8C_YqxW5dG98_WNXjdjx3DHWSloY3Rj2Q0qF22xERCZKwX8hbjoxuaSPX9N1n4bkAkAr4gKotk90riBTcnKCo0z1ObjnlJQxhHZuEbF3y8La5XPIDhEfgYmNHCpplluloMNbc9uf6r_YDv3t9nZ3BhVY3zt6jt44_1W_lnMlRGiM43xhYKpt9RKgpkRxtUCdhjMeyq-fEsxNpx-F5RrvH0xvGuCxpWLZwn7ELowo99GcgNkrFno-p82xihg6bOQVyAWruwdYDPFbEQuIW8NXWrZaUumdq7jN06RDRUtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2uz1_oFN4jTmnKUsId9cFX03sCCB6yIXhRhtL1tTOhjhuFrkOPOT-Z-sACgGOFJuzm7X01EC_bpLSsKjjsYFizsjE0QOcC6c8RHIFks1K9vsHx3cBHLsMPHLV8woXc43R0w4SOtSZTRgwt2AIfCsNPnkItWeKT7xtQYDqTtJOwAHM5Um17UJplYBjAW05N_rbAdsONkf_wdyq2Fb_9ix6zyX1uhhYoMA4mjIakJqOAlFVvA3QRD76GqqoBqwya6bdqpVhmNqOJTH1dhucb7_rALL2v2nIb98l4i_uQBqIcwic4vHf6__Js47K5lDYGPIewRFk2BelXB3dhEJYu3Lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خامس رودریگز:
🔺
وقتی به قطر رفتم، پول فوق‌العاده‌ زیادی به من دادند اما زندگی خصوصی‌ام کاملاً به کابوس تبدیل شد. فرهنگ آنجا آنقدر متفاوت بود که نتوانستم خودم را وفق دهم.
🔺
با دست غذا میخوردند و به من هم می‌گفتند «بیا، تو هم با دست بخور». در آنجا دوش گرفتنِ کاملا لخت ممنوع بود و این موضوع من را خیلی عقب می‌انداخت. میلیون‌ها دلار داشتم، بهترین ماشین‌ها زیر پایم بود اما تنها در خانه مینشستم و گریه می‌کردم.
🔺
شهرت و پول از بیرون عالی به نظر می‌رسد اما وقتی تو را در جایی که به آن تعلق نداری کاملاً تنها می‌گذارد، آن پول هیچ ارزشی ندارد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/91804" target="_blank">📅 10:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91802">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UeHxOYKCG2UC1uurnWbo-hZ9ULvwl137j80elRTIp5TaFDeV5zhmKCs9BMlx7YcNgEAoJbFxQvOV4-TtsIRTfGTZgliAIkthk_Xj48mzAewhEUb1EkO9aHLe1SbnJ_MTO3V5AUZshG0Jik8969aQ5QwDq2r12DN96dC4o4Cmxaxo4vd-aSH2sjAZ9gHMY3d7d5zbWj1Nc_2spZlprHlmWNgjQvKHUOcFsgKDr6GjWzbBCXgf9UGegeoL5h19xVlnJTSPc8Qpdl7vgliZL0MjJnqwH1ey66Hu1Tk4ogaaFj9iJqvrvhtmBvCLwEiUBKvPp4449a7RQzvo6OaQaUeMUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRvjFoMIdaPxoYbGYLZoDq8tpAU-FJC20pIE1wmxOaoBsujHbQril4P1kTeMQdeP6mNmCr2K4MBlWN-_NLHgGDijYimTSgtTn3L00Wasms047RKn5ymYgpPW7qmD98Nq4z0B4BAVnmL6j3GrXwRmG_3VMe9nRrE18AokIKmKRIrdg4ozizhbApKKS8QY4LzEb34cO9dn2YZCA78R7BTZVdv47GZfVz33TYrm4-7GcD4M4q9JoFboLr2s2KTW5tIzDlU0lg3CWrkzVReLMjmj02AQz0GJvmPkIjwsVKKxZv4YyonxnB3mXT97E2FLrwMWzrwK1aLRElJJ_d1MItxtTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
🏆
-
ورزشگاه سیاتل (Seattle Stadium):
مکان: سیاتل، ایالت واشنگتن
🇺🇸
افتتاح: سال 2002
ظرفیت: حدود 69 هزار نفر
🗣
پر سر و صدا ترین ورزشگاه به دلیل طراحی سقف که صداهای تماشاگران را در داخل ورزشگاه محبوس می‌کند.
🔻
برنامه‌ریزی شده بود تا میزبان بازی‌های بزرگ مانند مسابقات جام جهانی باشد.
🔺
6 بازی را در جام جهانی میزبانی خواهد کرد (۴ بازی در مرحله گروهی + مرحله یک‌شانزدهم نهایی + مرحله یک‌هشتم نهایی).
🔹
مهم‌ترین بازی‌هایی که میزبانی خواهد کرد:
🇪🇬
مصر × ایران
🇮🇷
🇧🇦
بوسنی و هرزگوین × قطر
🇶🇦
😀
بلژیک × مصر
🇪🇬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/91802" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91801">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a3bc142ec.mp4?token=fenU5_0k0FRhAqhLefep30S2LnUitd6ev9lka-VhnCOfwObHp_itddbg0a_0EKz-zAvauMSOyD8lhKo8rjAmr_h96FlAgpl63f4ogqkOiKv0uT_8iXPC09aL_W34vMqMZR5lUKmm7pas3AR_4fM6ba2zlt5D5wDjNDGglNOvedDRwQN9YSHjDcIo8IqLwntaCxud5ld-uf0pfRSjYAGouH5LZrUC3N66_X_5Ayf5sdux4Vld9qeOKmxAG1LfPUGM7I4UzXM1gyhDWW-Gzw8ZU7qlnmKJbLglULbtv_CjZhoZ19RpqtL_bCQwcCvkyhAvBuXSbADoRr1ljS4MFBJ8cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a3bc142ec.mp4?token=fenU5_0k0FRhAqhLefep30S2LnUitd6ev9lka-VhnCOfwObHp_itddbg0a_0EKz-zAvauMSOyD8lhKo8rjAmr_h96FlAgpl63f4ogqkOiKv0uT_8iXPC09aL_W34vMqMZR5lUKmm7pas3AR_4fM6ba2zlt5D5wDjNDGglNOvedDRwQN9YSHjDcIo8IqLwntaCxud5ld-uf0pfRSjYAGouH5LZrUC3N66_X_5Ayf5sdux4Vld9qeOKmxAG1LfPUGM7I4UzXM1gyhDWW-Gzw8ZU7qlnmKJbLglULbtv_CjZhoZ19RpqtL_bCQwcCvkyhAvBuXSbADoRr1ljS4MFBJ8cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
گل‌دیشب لیونل‌مسی از این زاویه جذاب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91801" target="_blank">📅 09:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91799">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAaDReBbqdMfBEyhCc8q4sopQDyMHipbfNsuKLAznpR0TvkEgL0zLE34rMOhxRTLnjNoZm_pTUQ8lib__h1BJctbee3ACBXmAAAlPjNm8HpUdQPhxQy4tZIchDmk_mAKwN1jHx43FGx0KVDPzKo3yy9hGTlwBEsI9VCKoEV9SIMaoQraGi9wyedZy5lewlVhjJfcKxY6A6qUEo_p_zNpNXBP3x8iLvGD5NtlhNZvBbo3i8nYqe46Ma_LnQB_T0lx45tZ70tpl8S82VWSK8TIZEjFddcWVpAwI4P4LDdN-Jsl9PG_mVY4iMTehUcYkSWrtqLCPt-sfNjBr6GalFkZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSbiDQj5Q0jSfEiDpCLT-lSZfmo-3Q4q9JYVQ8-HZo3C4YE30FrmO7Onrp8PVxnmHAGrMkigpPdbApWO3q59V2CwRIilN45xcxrUsHgvGt8RjxR3aVOqgSXZ4GIf3sfxqISTpde3rDfqeowIv-_WfktEblztamlqqfwVNY6lx6WisDipr3ZBA1IkWwkRaH-wanlEgHrOv-trY_sGhPKT2du4Mrac9AETbhTFHo5VitzU8282v6xiMxGUylh3yeUp80SoDKhjL7mQDrT0-Utlz9uBWU8bxxUJv63s6GRpeBcoNKvsGBLXvPWDmJffufxjRfBLzzl82uvTqPO-Ts8NaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سوفی رین مدل معروف اونلی فنز: هر کس تو جام‌جهانی آقای گل بشه یه شب میتونه با من بخوابه‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/91799" target="_blank">📅 09:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91798">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwvLB8tAFdPDp1LHKHT81yX_bIJD_7EywuTWqNiaFeKljsSdbi0tWb2QKGWjJC5_xBKow44On4hs8RbkAH824DEmu52RB4_5AgT4jCQgFwZVDwniNkH3MA9xp-i9CS2AbkVdCFD8Yncy3tr_FM_B_xgOij6Pn3bOruGezh1aOGusIuxpE3iVxMHQYdFswzt2TEcKHG9ZyXjgLpgharHDWMnEbrPOP7bYL89FlsurdTkw8j-OHk7_jKea4E8aSYRaLSR5h-AMLMM7gl_QPGj-BUkQn5BGcN0QuRAzJl7n2Y6FU1TbQ6aoZscG5OJbX8OSYOXrel7tQpmcQmtM7czpqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
در ادامه بازگشت سلیبریدی‌های بی‌خاصیت، دیشب پیام صادقیان هم بعد کلی کسکلک بازی در ترکیه و کارای عجیبش به ایران برگشته و در تجمعات شبانه حاضر شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/91798" target="_blank">📅 09:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91797">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
سپاه در جواب حمله دیشب آمریکا؛ حداقل چهار موشک بالستیک ایرانی به سمت پایگاه‌های نظامی آمریکا در بحرین، کویت و اردن شلیک کرد. ولی خب همچنان آتش بس برقراره و مشکلی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91797" target="_blank">📅 09:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91796">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPN-bjOCkW96xym1lsjrcBKQyDVKsmkGT2UfSuoYf2Zanqe59LnEU6D2w8DKVFfTcseUxpSTw7wbl3CQ0tTXT2su0aTs3I-YQu2n7b08wGWO5BHc3BrQ77zSAIZBLzehxHgxiAc-yMdEZw694rhmn0V-_zoZuHS62XqqwR_iQVIk2F3tCf3Xr7OHAYsr1fNEZVsllbaZKVQYCKC8_BU_CMMdM7DpbpkFGocSl-dMss8TEjznldS78vsOFRME9xggsurLB1je-AnPpe8iAlnX8lpBxLXzVSE7IJrYhI6MJcQJ9V-0Es-E0IfCbEtEJXK3xU7U5cyxTJ45RVcySISgYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رودریگو دی پائول: میخواهیم با جام قهرمانی به کشورمان برگردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91796" target="_blank">📅 08:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91795">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNfL6xdzo_NxmWkwZ_A7gITEkrtIl7liXcinmLYZXYYW1YA3lPr3XK6AOmXBWuZz8Idfu3g_jnRo0LYORBRSoKNhGhzv2W_jF9w4fHwyg6gW-k1Xx3Iwyws-XttlbAK36BoDcCLLSCHJflxhOCkTsq6JqjjpqVEFecg3Ojp-ygoYuefqKSRMSvUk6iBdd1U4m10q_HnIMKfYwb9pCYceGLsTfcQQVsyw3im61fdxqwVnwhfFdCTGkPGEugjlXhtT_rMeYPOJtRMZJvemfjwqKug1B6LnXHvJI2aUrj8yub-fsDkhj2MYlB3dGYAXWYz7r56PIOu1Nc7oI-zAL_OXyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی با 38 سال و 11 ماه و 14 روز مسن ترین بازیکن تاریخ تیم ملی آرژانتین شد
🔥
او رکوردی را که از سال 1957 در اختیار آنجل لابرونا بود که در 38 سال و 9 ماه و 8 روز به برزیل گلزنی کرد، پشت سر گذاشت.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/91795" target="_blank">📅 08:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91794">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=Dl7WYN4rHnJX8KA5gCZMe-NI207Bb8bZkFUiOHn1GYjKB6B0aagm2Vu0sGUo8bedAXQjdOJwqFeFgc9eIJfBCIWBxFlSsFkI9cDCZvDyDdjv4Z3MtjnXhU3KlRP-jMzZySyweZoxL-OjyeMAXhO5KJoZu-O9k1Ve6XJU1EFlDtVXCtMM3v4isNZN5x2bjH-Z6y4cj2Z4BZGzrjsYNUJml4t-GZ3EqPirdjGvAhtsBB_RPV_ozA7fAde_k2PThs1QAKZfC7epPvhWP8MWYNZMEnbrZEW4uAxy6sGcF2hb7ud1ngnXV4g7J59ltk9pRLtT13FgoHfp51XE24ARjkU-cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=Dl7WYN4rHnJX8KA5gCZMe-NI207Bb8bZkFUiOHn1GYjKB6B0aagm2Vu0sGUo8bedAXQjdOJwqFeFgc9eIJfBCIWBxFlSsFkI9cDCZvDyDdjv4Z3MtjnXhU3KlRP-jMzZySyweZoxL-OjyeMAXhO5KJoZu-O9k1Ve6XJU1EFlDtVXCtMM3v4isNZN5x2bjH-Z6y4cj2Z4BZGzrjsYNUJml4t-GZ3EqPirdjGvAhtsBB_RPV_ozA7fAde_k2PThs1QAKZfC7epPvhWP8MWYNZMEnbrZEW4uAxy6sGcF2hb7ud1ngnXV4g7J59ltk9pRLtT13FgoHfp51XE24ARjkU-cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گلزنی مسی در بازی دوستانه بامداد امروز مقابل ایسلند که با نتیجه 3_0 به سود آرژانتین به پایان رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/91794" target="_blank">📅 08:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91793">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAC8yRipCD04Fur9KCH393SsIkpVnXJe1VJyuFWvq6X9o6la7hNEVodvFa0xid2upV9Kf_xHOAPwS53UKY3iZ_cjT5dJytSNuK2QYMhPxiSSoeEhyHRbVqb3chuVL3n8NIv5oEeHe9pJ4UkLmg_U5mtmkS-tqBq-HiKOj5B_pE12l4MdvrVuz2_CFyqGoeNYZQ1fJ-IqvWJeYvnq3kN_lfbQfI2fABxIDaw22yDzeEfuliTIPwLCdcL5hHuZsAEZtKg1EmFYuo4sps2tmIrQxrJ1BozNGID3MzJENJxnk07CLpb9E-9G19I47n7eSwnQ2FKGwC3SWlBhqN_jwbTS_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرزو رئیس اتلتیکو مادرید:
کون خودتونم پاره کنید آلوارز فروشی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/91793" target="_blank">📅 03:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91792">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07800c01b2.mp4?token=KbbrZBJCGyZE3yxqZWudPtrhyvPP33gofOJdYV_F9jnqHFOyE4vIu1Y1GGmi8hkC9cyboKBTZLqx8no5SrN-AULdtY2y1mtP8ajJ6DQIBGH3k-wsJvp3gwRqErQc-mZz63ZtEjPoE7eBP8Dgs9Oa9bFTmjQMk4Gd4R-Ph7IEr6lYNKemUMbJe9vKOr671gLgCEftJrMrJGMCe4suuDwfk22R4IXPyQ4GgmOOp9xoPpHZXv0zol1TB3ilNhJmK_Y8soiO9PHsdog-7wl5JL8Gsg7NcSiaDAUM4rtAtQUOONIiTNDEqC_0cd01uREGITXd9-0S_IizG1CmdBgN27-56w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07800c01b2.mp4?token=KbbrZBJCGyZE3yxqZWudPtrhyvPP33gofOJdYV_F9jnqHFOyE4vIu1Y1GGmi8hkC9cyboKBTZLqx8no5SrN-AULdtY2y1mtP8ajJ6DQIBGH3k-wsJvp3gwRqErQc-mZz63ZtEjPoE7eBP8Dgs9Oa9bFTmjQMk4Gd4R-Ph7IEr6lYNKemUMbJe9vKOr671gLgCEftJrMrJGMCe4suuDwfk22R4IXPyQ4GgmOOp9xoPpHZXv0zol1TB3ilNhJmK_Y8soiO9PHsdog-7wl5JL8Gsg7NcSiaDAUM4rtAtQUOONIiTNDEqC_0cd01uREGITXd9-0S_IizG1CmdBgN27-56w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که بغض تتلو بعد تقریبا 3 سال حبس، پشت میله‌های زندان و درحال خوندن آهنگ شکست
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/91792" target="_blank">📅 02:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91791">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8s7ryRJToesketZ01MGrHE0YsP35GOvU6EqvPLWGh95H6jbY28y255pSA-ev34P37oXqJEb1X02y2j2kcXwzQhSBHCERZSC3tFfjQMvlekwgizqw03q9_kbyT3EDPjn-00KdsSsIzybQKhi9VjycYtpEMugDQXF7gYp2hfw3tLEIHLr9TGKx6Ia2tuxaMHFBeTab-OIz6lk1RQ3TQdGYT3yodZYJI9137_Kttlv_y2XV8Mcg22iiG1W8LclPRD-i47dvFktUqCe2yeXVvLuB1QG5PHQIhXBby5w90LkLn4cS4SyE5cKdicg8iEtsPgaBQ_eEmYTSMK3Xh-TG2oUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔻
خوزه آلوارز خیلی نزدیک به لاپورتا:
🔻
آلوارز شخصا با یکی از مسئولین رده بالای بارسا تماس گرفته و گفته:
من نه با رئال مادرید مذاکره کرده‌ام و نه قصدی برای مذاکره با آنها دارم و فقط میخواهم برای بارسلونا بازی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/91791" target="_blank">📅 02:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91789">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201d3221ec.mp4?token=hlh3gGwcD8qkKJSRNh4kJTOqWBM47FlZKScNHQYl6sEDxcm7lTsLV1S1LlWrm_dkK6PcZN3h5D5yaMg8aANeY25v2XOhmTSJunQ_xMzQ_y40Fh9b_-6FtvF-446ng67DiiRa_U2RENbrVSozHgW8_SXo036KJvcrtbAIIHPzphGazO7Kj9TeHNY64h-W4pp2DfJAAYwl4QtO1T6MUAr7Ui6gFW3LJu93VDkAHaw9xTO-87EtWMq6AuAkKKlwVhCiyTPT6M1EiqI8xGMYek_2uCind1qUjOyBKhZJzezbytW9e98vUUlZRQRECmOrpA3o00sRlMTDptwONeodP5Hztg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201d3221ec.mp4?token=hlh3gGwcD8qkKJSRNh4kJTOqWBM47FlZKScNHQYl6sEDxcm7lTsLV1S1LlWrm_dkK6PcZN3h5D5yaMg8aANeY25v2XOhmTSJunQ_xMzQ_y40Fh9b_-6FtvF-446ng67DiiRa_U2RENbrVSozHgW8_SXo036KJvcrtbAIIHPzphGazO7Kj9TeHNY64h-W4pp2DfJAAYwl4QtO1T6MUAr7Ui6gFW3LJu93VDkAHaw9xTO-87EtWMq6AuAkKKlwVhCiyTPT6M1EiqI8xGMYek_2uCind1qUjOyBKhZJzezbytW9e98vUUlZRQRECmOrpA3o00sRlMTDptwONeodP5Hztg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات دیوانه وار اوکراین به خط لوله گاز اصلی روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/91789" target="_blank">📅 02:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91788">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
وضعیت الان اینجوریه که:  آمریکا داره ایرانو میزنه ایران داره پایگاه های آمریکا رو میزنه پاکستان داره افغانستانو میزنه اسرائیل داره لبنان رو میزنه ترکیه داره عراقو میزنه یمن داره اسرائیل رو میزنه اوکراین هم داره روسیه رو میزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/91788" target="_blank">📅 01:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91787">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
وضعیت الان اینجوریه که:
آمریکا داره ایرانو میزنه
ایران داره پایگاه های آمریکا رو میزنه
پاکستان داره افغانستانو میزنه
اسرائیل داره لبنان رو میزنه
ترکیه داره عراقو میزنه
یمن داره اسرائیل رو میزنه
اوکراین هم داره روسیه رو میزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/91787" target="_blank">📅 01:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91786">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
حملات هوایی پاکستان به پاسگاه مرزی افغانستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/91786" target="_blank">📅 01:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91784">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🇺🇸
آکسیوس: نوبت بازی آمریکا تموم شد و دیگه خبری نیست. حالا منتظریم ایران بازیو از سر بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/91784" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91783">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🇺🇸
آکسیوس: نوبت بازی آمریکا تموم شد و دیگه خبری نیست. حالا منتظریم ایران بازیو از سر بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/91783" target="_blank">📅 01:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91782">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
حملات هوایی پاکستان به پاسگاه مرزی افغانستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/91782" target="_blank">📅 01:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91781">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
حملات هوایی پاکستان به پاسگاه مرزی افغانستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/91781" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91780">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-JZ2IS0TZlIRg4xX2BVe1PKNXZCAB6c5KSgnNnwFomJJY-tLr1ZWCYdy0tTmB3gWV1Tc9kBqoY8zZAqPp3MiOrs7PCuIAy2EsHLE_CGOArvZR78ZDGQquQOTEZsbsiiqZlunE4mtRJcVu_H_EEmeegHOpuSpj_K0hhsYNPkKpwftRQkC6AAYQ5hnKkGAPA5lMBPNaGrWOQBVEjkTD_71voWBRqlIro9okRqITCw6Bk6mWCAiGppk6p-qDt1g_je1R8oSqBqXJ5Htek4p8lmQfW-ay-kgV0t1EO8ukMJyJNy5sJ9jKktZPh1kgaamBMeR5fUUjPqluUxMyaEwYYyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙁
سید مجید خواب بود کی بیدارش کرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/91780" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91779">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
فهرست اولیه اهداف آمریکا در حملات فعلی به ایران:
-پایگاه دریایی سیریک
-پایگاه دریایی جاسک
-موقعیت پدافند هوایی بندرعباس
-موقعیت موشکی ساحلی میناب
-موقعیت موشکی ساحلی قشم
-بندر تجاری قشم
-کوه مبارکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/91779" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91778">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
خاورمیانه امشب تو اوجه : اسرائیل دقایقی پیش به لبنان حمله کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/91778" target="_blank">📅 01:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91777">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه خبر از آلوارز بریم؟
🙁
🙁
🙁</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/91777" target="_blank">📅 01:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91776">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یه خبر از آلوارز بریم؟
🙁
🙁
🙁</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/91776" target="_blank">📅 01:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91775">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aca6ef1dd.mp4?token=YTRrbmC4mBegQv4ci_3oI56YC1SSkQthfBfhZkWJ68lAmM-UAfofaQdumrh2GCt8ewSfvCNHn2Eas4wvfxFoFu3NPAvHtVLG7nQWBjLjIeCRlJF1hugSUMVunhxlrDXooRi2TWzIfg8_Okh-oJRmIq_WVl7aMc7WJ3IEOLBzLhAeGuxUDV4wvhNe5QLDlaNJ3iZUgsE6J46_sZona_ztqnWQjRsT8D5zObK4k_JvzP5u1umex_C-82rLVuJfsqHzIxvLYcB8hdTBR0Yp_Y5hYPRCXu-jnlA-mxMH4iCB_daR0EEiD4n_cor9Bo8UkC7hQImI8G_H4UsxErj6fQrhcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aca6ef1dd.mp4?token=YTRrbmC4mBegQv4ci_3oI56YC1SSkQthfBfhZkWJ68lAmM-UAfofaQdumrh2GCt8ewSfvCNHn2Eas4wvfxFoFu3NPAvHtVLG7nQWBjLjIeCRlJF1hugSUMVunhxlrDXooRi2TWzIfg8_Okh-oJRmIq_WVl7aMc7WJ3IEOLBzLhAeGuxUDV4wvhNe5QLDlaNJ3iZUgsE6J46_sZona_ztqnWQjRsT8D5zObK4k_JvzP5u1umex_C-82rLVuJfsqHzIxvLYcB8hdTBR0Yp_Y5hYPRCXu-jnlA-mxMH4iCB_daR0EEiD4n_cor9Bo8UkC7hQImI8G_H4UsxErj6fQrhcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی از بحرین و کویت هم‌اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/91775" target="_blank">📅 01:11 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
