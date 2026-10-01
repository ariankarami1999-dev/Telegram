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
<img src="https://cdn4.telesco.pe/file/NaYoYDcsHZBrbwZvF_zML-F2Rh2bSDSk0egR5SWZ_orfqIl0yISySiD_zx0POliqOsvB4lHGSnCSW6_V9mcKa_G9lnYrRVy35oHzS5Z7WoERH_eEjf543qkFFygV8RAEL_Tkx5c57TKwadLX56Z5PjT_1qo1E4trpvpQPddPw13Ki0eCDwYSxXrJz3QalIMCK10JQe082LLGPRO3gWkuZjZ3RNVlRriyal-VpqsiZ_RAeYjqtnqONvpGbhq-g-GTAX2iZsYNWeEYFbSVQ1D_xKVvCCoOo9PDL4wv8gnBpU8uqHmZZTxZNEdAuHwIMCA-hNqElbR9b2DFh1ulErgZrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 254K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 02:47:57</div>
<hr>

<div class="tg-post" id="msg-84308">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خسته نشدی این همه پول VPN دادی و آخرشم فقط یه روز درست کار کرد؟
😕
لومس نت اومده تا نهایت سرعت و پایداری واقعی رو بهت بده. نه وعده الکی، نه حرف بی‌خود!
👌
🎁
تست رایگان
💵
تضمین بازگشت وجه
🌐
اتصال پایدار و پر سرعت
🤖
همین حالا ربات رو استارت کن و تست رایگان…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/funhiphop/84308" target="_blank">📅 02:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84307">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ka1aLnDxzPabQ2aW10HZ51YXqO6n702or6M-26xxQpqeF8eF3bnmdWAM2ROFQrbf9l5-CelNagLvDTQDgScr79_tICNVMoxMPz-aoXCFZoGbAUKeSJ2-kOTLwmnPiIYbDJnjcoVSOKEz4z8KmiLWBJqmjAT7n9tL9K1WKr6mGB55Oyc4yAzDgzGs1TNuettzPz7YUWcFnOzfbkB34yrj1lBNxUZEh_3MHujohYoGu36FmvzrUA3CrIf98j2CAr27Czq4XZo1qKkwU8E4FvZr96fE-cmsXhxcHJLgOVTCx0nZEttbqemimitfrYU7bQgXfPx5TYVc-iJKzrY5AxAg5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته نشدی این همه پول VPN دادی و آخرشم فقط یه روز درست کار کرد؟
😕
لومس نت اومده تا نهایت سرعت و پایداری واقعی رو بهت بده. نه وعده الکی، نه حرف بی‌خود!
👌
🎁
تست رایگان
💵
تضمین بازگشت وجه
🌐
اتصال پایدار و پر سرعت
🤖
همین حالا ربات رو استارت کن و تست رایگان بگیر:
👉
@LomesNetBot</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/funhiphop/84307" target="_blank">📅 01:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84306">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a90438c76b.mp4?token=mAyK_Ra6D3_BYLN8tioCKjgd_CiDrEmpgz7NTE9eVBvn-vVStQVDabHsB55muEEOo8UVyTWHH484wDOzlYPlWrPwlePGE-q0zCdZyTwoS-HXx0GcI9d45h9NWLgdvayfmHVsyAg-QR5_hcVWDX0mUry5dhsmqGEFUCZck67Kjo7iS6oAt0nSqpynEpfdvFwatSCT-Jcl2I8x_Svd0b9ngUX0Np_UkXmrYVZQUlZO6kYzdTyNO9DsjK8RjqAHG5bvCRlGukKB4G527HUTInubQkVBCpR1QjN2rBGEomwmR7ZoVhtDjywdeVHodUqQB3yYipJJRjDD2FpZxamSrxUfVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a90438c76b.mp4?token=mAyK_Ra6D3_BYLN8tioCKjgd_CiDrEmpgz7NTE9eVBvn-vVStQVDabHsB55muEEOo8UVyTWHH484wDOzlYPlWrPwlePGE-q0zCdZyTwoS-HXx0GcI9d45h9NWLgdvayfmHVsyAg-QR5_hcVWDX0mUry5dhsmqGEFUCZck67Kjo7iS6oAt0nSqpynEpfdvFwatSCT-Jcl2I8x_Svd0b9ngUX0Np_UkXmrYVZQUlZO6kYzdTyNO9DsjK8RjqAHG5bvCRlGukKB4G527HUTInubQkVBCpR1QjN2rBGEomwmR7ZoVhtDjywdeVHodUqQB3yYipJJRjDD2FpZxamSrxUfVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو حاجی  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/funhiphop/84306" target="_blank">📅 00:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84305">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8253be66.mp4?token=EWmkQgu_QNF2OB_I-tHTHLPB7TlplF7-EvYTWaiXf57zOmtYYZ9epolLvwmkG-myoDheC-88PWfSmoVkUwKFU3Ji4Bal7N7QmNYTQtfKe2VCezpERKeMvNPy5kglSUsFUcaIGqVJ302aiHDkoRPV8Vqghs-eBAIhGZw8_hPD9lTD6c4-KiUAaemHmONq33Wbwvr9ODYcRra2yn8Bg8bQiqzVMxHd03_SUU0cyY3WRZjlciBLWUmpU24Hh7KaiEUjMnNl2fuoDJFf_VQtsp_wYbcNl3IJGYntfdXqCO1E4cW2WsM2G3kFgyVtP5IZv-2CWeXipuqPu9I8DxwB-FlzwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8253be66.mp4?token=EWmkQgu_QNF2OB_I-tHTHLPB7TlplF7-EvYTWaiXf57zOmtYYZ9epolLvwmkG-myoDheC-88PWfSmoVkUwKFU3Ji4Bal7N7QmNYTQtfKe2VCezpERKeMvNPy5kglSUsFUcaIGqVJ302aiHDkoRPV8Vqghs-eBAIhGZw8_hPD9lTD6c4-KiUAaemHmONq33Wbwvr9ODYcRra2yn8Bg8bQiqzVMxHd03_SUU0cyY3WRZjlciBLWUmpU24Hh7KaiEUjMnNl2fuoDJFf_VQtsp_wYbcNl3IJGYntfdXqCO1E4cW2WsM2G3kFgyVtP5IZv-2CWeXipuqPu9I8DxwB-FlzwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/funhiphop/84305" target="_blank">📅 00:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84304">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aunxO-5JKYDim1R64chmxeIAf_qy75dUim19WZT8vhdxgiBbvPvWubzgnadh82v_xVfcR3F3WnqV1rtZGiKpI6Z7F3zrZEC9qtFuhSrJf7QaWJXtAsC64sGTC1Ar3H7C-FERWHCkbrTlDU5TiCar62jGJ9tMAjA2KHLlPacXSfkuRX2nSMIinivwMIpHUFX53W31OhVlBl-0nWBhNrNiLznGsWsh2d_feW72usjXn0LEKEnGB6BYuAxFLM5uHdAxdTMoK6sojAg_RHzLfsYTKUk4v86lDaRFxfYEjPMbmJqhocfewmEbx0zYrvAUuaxqVu5sWzPBOpKoq4V9mqS8Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکشا دیدید بدون رونالدو هیچی نیستید؟ رونالدو بود دفاع میکرد دوتا نخورید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/funhiphop/84304" target="_blank">📅 00:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84302">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دقایقی پیش وزارت خزانه‌داری آمریکا شرکت های ایران‌خودرو، ایران‌خودرو دیزل، سایپا، پارس‌خودرو، زامیاد، هپکو، راه‌آهن ملی ایران و شرکت قطارهای مسافری رجا را در فهرست تحریم های سراسری خود قرار داد و اعلام کرد بیش از 30 درصد درآمد صادراتی ایران را هدف قرار داده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/84302" target="_blank">📅 22:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84298">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43faf33322.mp4?token=ibhJjQeE9evCxflg-WIKdvO3AC2RqaU80Ixy5_aG47cQRE7A7FoWFE7L9bXA_FRvchIP4fBNtK1SltFxD_2nLeegsSA7XXBIEr43ShmZst0SkozbHAUy5dTufjJMr7INMbzOJEWuaHnyfDCw6oUqkDxrXDxsc-fsvQRZMq78vZKlLIry2QEgjqY1Ar1IsdwTsxBJGIxNfbgsarpmWZFskE-WWDigd7WYUYrwW_HOAuHilqDspcVW7V4VZjpDy1VLsLAinybXayc7o1zyK4XbKtRNb9cxjulIyVbyCIFbh1tgSe3XTJ5BkHadFpUUtGVhx8vgp90O_i6GIy15LkwNsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43faf33322.mp4?token=ibhJjQeE9evCxflg-WIKdvO3AC2RqaU80Ixy5_aG47cQRE7A7FoWFE7L9bXA_FRvchIP4fBNtK1SltFxD_2nLeegsSA7XXBIEr43ShmZst0SkozbHAUy5dTufjJMr7INMbzOJEWuaHnyfDCw6oUqkDxrXDxsc-fsvQRZMq78vZKlLIry2QEgjqY1Ar1IsdwTsxBJGIxNfbgsarpmWZFskE-WWDigd7WYUYrwW_HOAuHilqDspcVW7V4VZjpDy1VLsLAinybXayc7o1zyK4XbKtRNb9cxjulIyVbyCIFbh1tgSe3XTJ5BkHadFpUUtGVhx8vgp90O_i6GIy15LkwNsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید میلی گلد بعد از حواشی و شکایت های متعدد مردم با کپشن: این طلا، بخشی از طلای میلی است که خارج شده و حالا با آن، تسویه کاربران در حال انجام است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/84298" target="_blank">📅 21:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84297">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">لیائو کصکشو تا ۱۰۰ سال پیش ۷ دلار میخریدن الان شاخ شده شماره ۷ رونالدو رو میپوشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/84297" target="_blank">📅 21:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84295">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sw7BbeL60sW7sDyyN6Occc1ylDWZ7ZuK4Sv4OyX7UJKlqrcrE5H6OkfmAzZInmeKW1AmLuFabAiHhQysJ3G-6bT4SyLv7iAnm6k4tt9FEXwQbHJAjbr-r4R_hGTN08Y-VSSg0416DZUCPI8JhJX2ATd7bgJO0WUxDoRh64DC4FfaIkbG3ZkthjlrsE5teMsl4dqzcYYmxUfZ4S-mzIpZAFPFHTiME-QxcvhFP3MGBz4on_B5cmpvsYns2vJoGcrecBRPBQnu11Z0yQAbEQFkVwUveYKsmH1-srCXu4juVCLQmYwlYLMpK6NqV0mg15bOy1zk3CAgDKlk_Okt09zl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا جای این کصشرا یه شیر چای تریاک نمیزنن این شرکتا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/84295" target="_blank">📅 21:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84294">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پوتین رسما ناتو رو به حمله اتمی تهدید کرد، ورژن ۲۰۲۷ کره زمین قراره هیجان انگیز تر باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/84294" target="_blank">📅 21:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84293">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پوتین: کسمادر هر کی که به ما حمله کنه نقض هم نداریم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/84293" target="_blank">📅 20:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84292">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مهدی چند ماه اینده این ناوی که زدن چند میلیارد دلاره
یک مقام آمریکایی به الجزیره: تا پایان نوامبر آینده، ۳ ناو هواپیمابر و دو گروه آبی‌خاکی در اطراف ایران مستقر میشن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84292" target="_blank">📅 20:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84291">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝖕𝖆𝖐𝖍𝖆𝖜</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aochIbWIZPaPPkKaxATl4behlVnoAoD9IKY3yVYhKnokI6meUGzPH2ekDvnJZ1NdbJe7XuFE64bykLM1xEeAZKL64RgmHiKZxMSghFonJtdUZGQ7H4_spfSd0adM9hEGdc1tYjNNescQVNQgTv6qVMTUUBBpZODXvNAPngnXgefZpLdx6b_EvBFdPvg8UKEorvF9UpyVznGJn10R7nljg1Km4OU7qXxdxn60SLp3lfC0Qjd9TsMdbvQwAnto3mK_oku_WYOjCgn3zLzCFGKm6P35F3ZDSduw0UwuhUN3OpNxPr_RAtjytzqwUObHH_i7QGd5QkVPQ47aU1CdJ4MsZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیه</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/84291" target="_blank">📅 19:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84290">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPnp0C9WHLTa0i7NpEnmxLurMKQKKtedCaZao-7YwLpIEcDpYsmcqkLXRi2LKBQyM1BqjEuB1izmvPMowOeWRmgJe5zJtA2vIXAODI8dgoYEpKBTCAW0ZxkaNiIayT0w4rAYkIm-nf8z751V-qpIZd8P-xDIliRtYUKHB793T7-V-_lXcXTVclhh6CdaJEEEUvclFmgT1veGE99CIUQLgCcvhw-iJeDXe1DYPd1fo0gaJgqipIWm1KYoiySlmR3m6v7mWYKCCXG7y9ARqEbMXKtIYxypUXFLmNkR-kr10-ZXxpv-w-l2Q4ybZKR5IfMQ5y0xm-2RjoDULz0_YcMv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به این فکر کردید امیرمحمد هرچی دلش بخواد میتونه بخوره بدون این که نگران چاق شدنش باشه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/84290" target="_blank">📅 19:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84287">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eiDyvp4kWlo2ty8oGYlyoZ-WrKaZGfuJSjZfE-7B5nzCM9LxPcx3vYV6cHS-jz7h3Bk55DnxhWXgl3KHmuHLg_3q8I47CQFF5NkS3ASHfSptS2X_RKvGCpnMrbnhlgSM5VQgO-vVVGvETHCfsceFmiOsOd_DaDw1Sd1fYnoklSlrJYR1nB-jwPmYsE-N21_5dj4vwwy1avYz9y1pDLHI0M-jn7897mPSnbtiDY0W1ptm8sfDPMeAPcaDzOwP9ll2lrmf_Ng6WQBUC4eQFftTEHxjtY5q7XT6BgizfPzxlth81nAS-uCZ9QmlGw5UDXKxRN6KzUr9uvjXrLxD-mcf0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bY-ZvNYloWksL0EWA7jwCQGx6R9iwoNXueQepi_CuuIe75Tb7Jz7lnyd3eFELPJJCCAeWw-6P2WWQFHSoYQ2BCcNg0zpjx0O9jm6AtDSStscClJYLKBKvW4FYmnHENYOKx_Aj11Bbni32shgIpYfhokalDTsZ3dWtKIuU8neqskFllQcs3Fkbxq-HJmFjMlZFARcVTAf2S-dqPA1pw3RM6Ab2fZoKcWofkWerD8RpHHZnbVivqLheoLEA7USagGWrcAoolkuot8GJjugnZKNaIk4am65DCgxy_11-MnlOSsj4-VjSNCMnaY5OAGkz5y_rSvDwcWhBXRrrn2gg9jg2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NE91RClQDYOOSkQjABOeHnBkSIP8fyFSYDGAyg-R2eajdQCaiO_3Sq75u55foECF1bqtQrBh0JNgd3R_6UiNnslzCWfSZTviFC5wdr1jIbrMcVObVHfHvXrJoeGgZ9dF8tmh23_myM2EZfYxSWCfTsogx7PRtudrZ7Qmv0NiyIn5gPHNCr42i-g-qsJzbcnKk9A2ayk89uppjDZYzOK49NLQMv2bRsbk_nBvDEuuqmg__pYI9O16__uh1SuW7kowmH3pFNoYCzgibaklaUR-EnhGt94LreekFLPPiz2aqxdVuvwp5u0i_443jndk0cLNO1X99eXmVQV06gkM4bVd7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ریری یه جزیره رفته، ۹۲۹۱۹۹۱ تا ازش پست گذاشته اینستاگرامش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/84287" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84286">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84286" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/84286" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84285">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E66dxv0lCwN0JHEO3tAXDvvHqwjeINniQwZkRkgW7LS7xGI9P4OWMIJ4lGzzhQZF5jLvAupBplXsEiclowYSthEIgiwTmLsUtvwpG5iuEc8bcuzIz5wea_KOhINsIRW7J1Z5OCnS7ge6qc8OQ1gIFHMIqNqvSxc7V_LNrRn1BoJ3TFRafSKSDgqHJZ-Q0VudrybByqCDmWsHIKBdVH-ImzSWvZpMs4LnJ7DjxsHeE2VN-rod3TDCsQkbUD0DkBAcMPTxfmYoz28vLR7aEfLziJNY6QIu7lTp_GiMDNxIch8wP8yA-FNAtHSLL0OFNw3DC5AYE_dUJ1q8kx0q9KxMKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
اولیتت برای انتخاب سایت چیه
❓
امنیت مالی مهم ترین چیزیه که یه سایت پیشبینی باید داشته باشه
⚡️
ریتزوبت با انواع  درگاه های شارژ و‌ در گاه مخصوص و اختصاصی کارت به کارت امنیت مالی رو به کاربراش عرضه میکنه
⚡️
از همه‌مهم‌تر واریز و برداشت در ریتزوبت کاملا خودکار و اتوماتیک انجام میشه تمام پرداخت جوایز زیر 15 دقیقه س
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
g9
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/84285" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84284">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ناو هواپیمابر تئودور روزولت آمریکا هم پس از نهایی شدن مراحل آماده‌سازی راهی خاورمیانه شد تا نشون بده دکتر عراقچی حتی تو نیویورک هم با تعهد کاری و تکنیکال عمل می‌کنه.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/84284" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84282">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">جدی باورم نمیشه یسری آدم هستن که موزیکای قدیمی گوش نمیدن و پاپ جدید یا رپ گوش میدن فقط.
فک کن حس فاز گرفتن با موزیکای سیاوش قمیشی رو درک نکنی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/84282" target="_blank">📅 17:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84281">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترک جدید ویناک به نام "سرت میاد" منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84281" target="_blank">📅 17:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84280">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R90WhbHV3VhxxFujewAahQgMxgmhPh2uq6O-LPCFrWa4sGOE0hTA0WWv9euYnZu7Rqf69wh7zjl0zF07KGeDApTlHoxl64QY-FgTotoyLBsAUksrVfS_Xs_eadvQPaTZU67Et_2K1_gQApNlL7dCkPulTk38bxKJCMqbNi8gfQ3_sJmskH49ONYolsaOzKv0-8AmD_Pzu2zCc7f50jc3Ay0x8Y71fIQLVpG_D8geYw3m3Qt-dzWcrC-rywLJERmSF62CZ3JBc1-Hsqu2p7ZDa5UWGNVP1TJCShvdIE7-IDPj5uSPABIyLaVAgpMWGLe2_XTQIljgKFrfZCfwSLZgCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "سرت میاد" منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/84280" target="_blank">📅 17:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84279">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEPv6bJcuZ7vbKZEhubjFQG5AVI2oZ95F2hB0NtWb33t1RIKuodKeu-HDFHgFYzvt9az7dpeiqSJxV87Aer_VseSKNPIPDoRAKdtaCb_YtrVsmGM2vcMR-JtMegZPO-HGBLJav6cvBd2rbfUJA1_XSCWbssUy2qXHxoMB3eOG4xgGRFtLpiXI4TAWNsPf-vRNAHloKJyk-53QfyISZytuE2oLv04dkktV-dDzHh3MtwQqiz0ajYv89682GdOrOEaz-kZu0fREaYGenR-UTW_At-s0KMFlVC_crvaxFRQgKbGfgr9yD94Y6FahszGgz4v7QoST-Lyuo9LZYxOJPfeNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی انقد شاهکار شوخی کردی که مردم با شماره ناشناس زنگ میزنن ازت تشکر کنن:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/84279" target="_blank">📅 17:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84277">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzU3qmmh6WpCE36F4brIVwTBWiO6U9YYnS11t3mN_B4yBHV1YdOv4ojbUW-ZNRvVdWCaMsdwmpL06rEvgd7iuO85ma6dz3DBh-cmGM1XIVETbtPwlxeblQ_u0Kt6r1PTa5r02SnxXerByOfb8BvPPyVnntyzhMO6BbVGmQ0a1vSyo9O1CRamfLBeyZp2Kn5K-ZrGa8hn9qUSv1ie-9hHor2M_Qr_l0dspvTkBe0hoNWVNXmu4QO4mJkqoEgS5b-CxE0ohrlvQJZlEalpzWNlQjPzkgjISoMVb1iTz-UFoAltLljvld7jUbjIvFMOZSNtrCu3DpgTvm68OFvBWEfe8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f25717c9e4.mp4?token=MWpItvlKN0cdHmbdQ9aLp8qWAycWUuUHaVASi2IDOzjngR_O6AQ-QFAkgHKu7yOThhnNSxVzKpfS2qdV9P0kIx2HrrMG3_tboO4W_Q6hy_MBm-5akq583EwNjpbLHtmYGqVNdPXtGWeg9LX5HN8v5xVBMnwDkVDZ8fliArVHIyD4f5c4efIIQm1Xc91DTP5KEk_dXmdfIeldMd03jyF0TjZw1PEGy_fK7r53b03n5Xs5GwBluNt_RW1xquuL-rYuSbEoRodzH0GbUGRrrH6PZZzLqP_Fy328y2dguO9g7C0RGaK3gYc5hAem5LwOQwgjGdltlc8gjTszudig39H5qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f25717c9e4.mp4?token=MWpItvlKN0cdHmbdQ9aLp8qWAycWUuUHaVASi2IDOzjngR_O6AQ-QFAkgHKu7yOThhnNSxVzKpfS2qdV9P0kIx2HrrMG3_tboO4W_Q6hy_MBm-5akq583EwNjpbLHtmYGqVNdPXtGWeg9LX5HN8v5xVBMnwDkVDZ8fliArVHIyD4f5c4efIIQm1Xc91DTP5KEk_dXmdfIeldMd03jyF0TjZw1PEGy_fK7r53b03n5Xs5GwBluNt_RW1xquuL-rYuSbEoRodzH0GbUGRrrH6PZZzLqP_Fy328y2dguO9g7C0RGaK3gYc5hAem5LwOQwgjGdltlc8gjTszudig39H5qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید جان ناموسا تو یکی دیگه بیا برو کونتو بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84277" target="_blank">📅 16:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84276">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مارکو روبیو، دیشب هیئت ایرانی که احتمالا برای مذاکره مونده بودن تو آمریکا رو از خاک این کشور اخراج کرد  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84276" target="_blank">📅 16:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84275">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">واقعا فید کردن موها یه کلک مارکتینگی بود که آرایشگرا پیاده کردن، مجبوری هر هفته بری پول بدی بهشون وگرنه شبیه جنگلیا میشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84275" target="_blank">📅 15:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84274">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کصکشا انقد به پر و پای بلو بانک نپیچید و نگید بزودی اونم پول مردم رو میدزده، یهو عصبی میشن فیلمای ثبت ناممون رو پخش میکنن بدبخت میشیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84274" target="_blank">📅 14:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84273">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4XmltXoFCCQ6pi3wY1eVQQuGLE2kZdnE98auO9eVeYeK9EwmzgCycjTKlRYddX4gYWMBrgyi3FpP7zxaEbSGzcyqfmr-jbW5qwrGg0nfGGlsxA6nq0IjuuqG18QNjtTBFnXSAmozohEGFNLeZMgwAI-5yYhnqNXpyRT4w_8tPIkDaixsFJZBodBOS_O_oGkEQSiphEuK1DIu2Am3JJLZwPjNGLp9cpoRkC_KUmn3IoXcLpoQCT7-8Qj5xMxUKKBS_wI3SaAseBGufG8I8DHtlEAwRJ7is_9v2C-2YFUtS7GBCUf5TXKeUSJ0UOAMRjo0wRc_pMyqAUHUZ_SmCD6BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو بازی دوستانه دیروز کونیا اسپور و تیم ملی فلسطین بازی رو دقیقه 89:59 متوقف کردن و گفتن ادامه بازی زمانی برگزار میشه که فلسطین آزاد بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84273" target="_blank">📅 13:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84272">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e053e973a0.mp4?token=eb5_OuvDdDKVYZ3pKNaYgVRgp610TIOP_Lnx7_8MPh5KVWqRuYKhnCA64YvLhQb0Y3SBEx0y3qpcj5d6Z91pm_2xgdgEdzRSQjZ_7qzI4W0YnshLvCwGcP9wSK7iMN37YamQioz4NyPsxDx2P062tbKwQiFMSqgQUpQc9Xq9SensS3K4EW4ZmCEVi0BY3Z2sxZEKNmVJ1TizhAY9fMb2RNvBbdKpl97d9A9WAgbFnv01IE-Trq7O2xy5yYAjPYqOQEzIjRYLm3G-vFzyUkyU4pCrFzAYB1HydOmHJu0PgqccTTJ4w5TBsHNnFmGXF5ZrJgSq-hQ0mgqaWHqJNoJ4SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e053e973a0.mp4?token=eb5_OuvDdDKVYZ3pKNaYgVRgp610TIOP_Lnx7_8MPh5KVWqRuYKhnCA64YvLhQb0Y3SBEx0y3qpcj5d6Z91pm_2xgdgEdzRSQjZ_7qzI4W0YnshLvCwGcP9wSK7iMN37YamQioz4NyPsxDx2P062tbKwQiFMSqgQUpQc9Xq9SensS3K4EW4ZmCEVi0BY3Z2sxZEKNmVJ1TizhAY9fMb2RNvBbdKpl97d9A9WAgbFnv01IE-Trq7O2xy5yYAjPYqOQEzIjRYLm3G-vFzyUkyU4pCrFzAYB1HydOmHJu0PgqccTTJ4w5TBsHNnFmGXF5ZrJgSq-hQ0mgqaWHqJNoJ4SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آ
مریکای جنایتکار با انتشار این کلیپ و نحوه شناسایی و منفجر کردن آدما با پهپاد، ایران رو به جنگ زمینی تهدید کرد
.
تو این کلیپ سربازای آمریکایی وارد خاک ایران میشن، و دو نفرو با پهپاد میکشن!
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84272" target="_blank">📅 12:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84271">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مارکو روبیو، دیشب هیئت ایرانی که احتمالا برای مذاکره مونده بودن تو آمریکا رو از خاک این کشور اخراج کرد
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84271" target="_blank">📅 12:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84270">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">محسن رضایی: قبل از اینکه انتقام آقا را بگیرم شهید نمیشوم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84270" target="_blank">📅 11:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84269">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
خبرنگار حوادث : دیشب تو تهران یه مرد جوون بخاطر اینکه زنش قصد داشته ازش طلاق بگیره با یه گالن بنزین وارد پاگرد طبقه اول شده و آتیش بپا کرده
تو این اتیش سوزی، خودش و خانمش و مادر زنش کشته شدن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84269" target="_blank">📅 11:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84268">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUAciDp5feGZPrWJSNNdqrpG6aMLO-aS2WsXMBS0JdO4TRbW10sI27CR0l3xqfboXkMVYxWfcYUwrxFWKv55CkVjmIdUDjODqp_1GMeNW4nTR4S49BH9jT1VehRj89EDdS1hvr5MMH98i5ZQl38BSLJeUNW4maGNessrJbi1ZXhJ0B5jh3AUdYdOMc42zZpaGhHIEbUPqmWL4-h02K9OdbBnPtLdSTAlUCzVQzyjxoyZOaqBn1hWzIl2cYRhgTw8uth79A4J23qqjsNOyL6dkBR80nQl9jiECWKkEE2PDI65xG8J-HCTNe6f8-Gs1shNKupHzbTSW4vDlPRMR58SRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط بوراک میتونه نجاتش بده
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84268" target="_blank">📅 10:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84264">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGSP-jZ4ohTXyQ88RFBD6ETNQD_mpkmzlnTadBiPgz9LMyAwjVDyY0xGAZ9dNIViU7tS5aFeiv6tw9c-Q2FppfiDfMUggrvC906cSZPxkiwBpweR5oTMmR4YbJwVBTQW-H1RqNuFYJ7G4JNNNKyP-mTk9d0tuN2i0T5__W8PmzxRPgAQcgxSV09nmX8hoKHeQ_VTesT_j7i62kgRhg95W9ClKUseXISKIO-8S6xptGvmzDw5MJt-Ije5zDJ6QpPkxFjKvKHdFK4c77rnKvkzrhclHbtRyX-83E5hLsOF5IuE5n9vlKLNGaWmklb5NAwMOu1L7-XBTw3YFxiZ2tQPYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEJ4Y2ytRHKikfG9bdUejlHTuCBNlpol-38uPKiGg8pYB9SUNeTyA6ftBznFIsNMNJUsWoX9k-5CQCFivOkwVg0-DSyS3PbRp_ZtoW1mZtoSEnKpXNP-HezoPfPyjQex8jco_jFKjpHkHFBDmV4PANe56O9MHrvUH9-1ahJjCYB1idQ1xz7JGJxrjFpdDhRcaByJXmOyAIM9SysqfCvOGGzIc8PJ9NtkXAn6qsD4XZd3OnTaI_EeFA6w4zO9cAj1ds3I4Hjv6_GulsHrHl-YkNjVn8BTPC3ZPZidv6z0wQT9od6mnaFpEyrwfD9goNZEN2uxj8aiXXT0Q1KJZmj8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kzIQ9F65nYF2OS7bCF5lWJcA-LMB_Fs_h69QQPZevBb-0xchGcWP-1cXADnnEzHCVwji2jDU0CNB4uxUxCZLbJrCsSG64B5m51s-Ww6lPW4tKsU6n-V3HvMWi63emF3ABHY8u2BoREHUoymOh2jKI-lr1rWD7zPdHEIBUULNjkk8x9q_ygqwIjx0gHaLyRPJaqJvaobjqvr8EjRKEkA9h4q8IWLKPKbRZoqzR_DD0ufMKL53wwvHhEguiEVQ-12cAvqLT6Z7fvCnZw4oJNnR7RljEWHhBGpOwiavQiYjSWvOcFe1QejF3CVMh0W-4vPwlfyJnC_p-tdHwPQqoJOFcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zkuk6ccth-FLyjV5hH90WzRNwqiz3we4tZFrew1g6mfS8jKkLpQ-sg8kYjOBbc37oNxtnlBWUPHGU63PWeWQ3-XyS6hwu3qaBmbLu-Ebf_X3LWQ8vDWOZm5HGGhftIz-k2mTM_0NSOAhHt24JiqLfh09PMIHgaPDowPVl6eCFVLczgNyIS7yqzKpqNneJiBXtplU_Pg7vT_-oWa041NLsuH2aBkUXjBw4Augx1LIZQbTXY32CfyspV-rQayRNmaNwohsC_VgM7-IuC3bIYX7dIX-20gACewZblh3am0Tb1QJH1nd3FB19a497WOA-2ZAait-B2EFSPLJHp7l6CaL6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های جدید بوراک
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84264" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84263">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84263" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/84263" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84262">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4obcY16zwjZUg3-kJSDhSM0ULa9sRcycxojdwmAQ05csBG0e-uHXThnXhkupXtpA480DPS1-4sCP60D4UHd0rqPbTlxijPpRF_tixSv-nYi_U-2fB-P4EMSVcr3l1bTAU-s-XM_B9Z9eX5ItdD0Whg1_DbUdexm049azxtZqyseykYYsd1O_TSfMTpfK12vy6cWveiG3I_umTyn5Sn8gn4EqCUT1V8cExb-tW9NbbKxo2a1a5BJNInpiiHtnZ0MuTDZWMeXYrzvqirBiKSzTRix3dKj5wqlbK8C_7pampyPoLXLstYrgXtVt5A22-h4da6QagE74qVNwcLZSdGbZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👏
یک بار شارژ کن ، دوبار شارژشو‌ این طرح اختصاصی ریتزوبت برای کاربرای فارسی زبان خودش رو از دست نده
🔵
اولین پلتفرم جهانی و اسپانسر لیگ هلند محیط امن و حرفه ای برای عاشقان شرط بندی فوتبال
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
r9
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84262" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84261">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">در بازگشایی مدارس امسال جای خالی یک نفر شدیداً حس میشد، شهید رییسی اگر زنده بود امروز بعد از انتخاب رشته مشغول به تحصیل در دبیرستان میشد
💔
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84261" target="_blank">📅 08:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84260">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49c29e72a9.mp4?token=FgU8jGALX6lq2Vmrc34xAh-IBo1qOxPUNtErqzc0aNWRHs9WIfJ5ZZP_V80ZaBd_B2Px1R5kv1WF5LrRC3vGNBGcQS9I3DYBGRHmpv5KXhxYEbEqcYQ7lN2PLqcUUJ98wzdrOOLMqiB_MSpcaPL19cSNlbqTLAzmNVM1_WKrLf6tC8gWmlZ1rl03q2TQeJzqZtWXnIZhfcVCZTFiuEBv1n4nIKc1EQ7MlEx1KZ8EmpqCKawaq2teV1kiV7jECRBezbnEfxDilLzFKZrbfOMlCtxGMQXaFpfd7486eodkDR0l4GM36JFhxEUr7JDEFdINEPTXrBe7M-TgjpVyhegZ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49c29e72a9.mp4?token=FgU8jGALX6lq2Vmrc34xAh-IBo1qOxPUNtErqzc0aNWRHs9WIfJ5ZZP_V80ZaBd_B2Px1R5kv1WF5LrRC3vGNBGcQS9I3DYBGRHmpv5KXhxYEbEqcYQ7lN2PLqcUUJ98wzdrOOLMqiB_MSpcaPL19cSNlbqTLAzmNVM1_WKrLf6tC8gWmlZ1rl03q2TQeJzqZtWXnIZhfcVCZTFiuEBv1n4nIKc1EQ7MlEx1KZ8EmpqCKawaq2teV1kiV7jECRBezbnEfxDilLzFKZrbfOMlCtxGMQXaFpfd7486eodkDR0l4GM36JFhxEUr7JDEFdINEPTXrBe7M-TgjpVyhegZ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده امارات در سازمان ملل: «تنب بزرگ، تنب کوچک و ابوموسی، جزایری هستند که بخشی از امارات محسوب می‌شوند و تحت اشغال ایران قرار دارند»
پ‌ن: بیا برو کونتو بده ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84260" target="_blank">📅 01:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84259">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ: میخایم بزنیم ،بزودی تصمیم میگیریم
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84259" target="_blank">📅 00:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84257">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85208a1d9e.mp4?token=rSBUk6Q4WXyCPasaAtEqXkR9c9d08sjQz5ib0Br80TrJXfpnsACo1v99SfoKcLoouMvmpZAM35HZHAgnoFhnHBRlZs6L0bEbO-z3ZSUNSYXft7Rxi0Hfrz0bWWypqRaYCJZ13CwuxAfbra59aWHcgiiZUMYFIEhMgJR696pjYsWo1cGbtEILYoV8mR-M-M05kIyRwSiZs_qBWPG6XiLw0n5_efKCOq7LnEcVsPg2n5634bWJS3Y91qo3eR_eQnIVjVs9luJlO_Fva75b40JUXsptOND01xV0EorEr38UaWbVdHLcNqGTy2YvjSTG4eUFfjmpGxZjszljTmm-4yn5sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85208a1d9e.mp4?token=rSBUk6Q4WXyCPasaAtEqXkR9c9d08sjQz5ib0Br80TrJXfpnsACo1v99SfoKcLoouMvmpZAM35HZHAgnoFhnHBRlZs6L0bEbO-z3ZSUNSYXft7Rxi0Hfrz0bWWypqRaYCJZ13CwuxAfbra59aWHcgiiZUMYFIEhMgJR696pjYsWo1cGbtEILYoV8mR-M-M05kIyRwSiZs_qBWPG6XiLw0n5_efKCOq7LnEcVsPg2n5634bWJS3Y91qo3eR_eQnIVjVs9luJlO_Fva75b40JUXsptOND01xV0EorEr38UaWbVdHLcNqGTy2YvjSTG4eUFfjmpGxZjszljTmm-4yn5sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یجور هرکی که فکرشو بکنی خایمال داره فک کنم اگه استالین هم زنده بود خایمال داشت، یسری بودن که میگفتن قضاوتش نکنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84257" target="_blank">📅 00:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84256">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وقتی از زندگی خسته شدید به این فکر کنید یسری هستن که بصورت جدی موزیکی که توش میگه "بِچه ارچره من بربر" گوش میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84256" target="_blank">📅 23:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84255">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9caab26da7.mp4?token=iiH3ouOgA7CiGGC-ojS3zKduzsnJECoX5jAnrmKkJmlRWO1xf4PfIBkQNl-MZWhprjDuH0j_sbE5FkPm4DRJZ6gTFXw8LF4TE1iXFlBCY5drPf4j4z_VQ4Ns04HKXJsL6jUB8pCu82cPdtVcLvtPDUh39EbN_NsSg9g5FYKRpIapT9nbbdpsnnOgfYWYAtpBddzaN5RNKnovDKaM7proL2bnBvS5z06uUOgi0Dk1adym3tnMAQU3B2HPotAhzK40eolFuLnLWJ_i0TYtcKp2MW3MoGa3PBCFKIsDeafhL5Vb697xmRbvAjNihjVTa8TfIoTzbvCYx5Oi8aiZpdjJIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9caab26da7.mp4?token=iiH3ouOgA7CiGGC-ojS3zKduzsnJECoX5jAnrmKkJmlRWO1xf4PfIBkQNl-MZWhprjDuH0j_sbE5FkPm4DRJZ6gTFXw8LF4TE1iXFlBCY5drPf4j4z_VQ4Ns04HKXJsL6jUB8pCu82cPdtVcLvtPDUh39EbN_NsSg9g5FYKRpIapT9nbbdpsnnOgfYWYAtpBddzaN5RNKnovDKaM7proL2bnBvS5z06uUOgi0Dk1adym3tnMAQU3B2HPotAhzK40eolFuLnLWJ_i0TYtcKp2MW3MoGa3PBCFKIsDeafhL5Vb697xmRbvAjNihjVTa8TfIoTzbvCYx5Oi8aiZpdjJIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این رفتار ها در شان مردمی که چهارم جهان هستن نیست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84255" target="_blank">📅 23:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84254">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کاش شرکتی جز دلپذیر سس فرانسوی تولید نکنه، خر میشم میخرم بعد پشیمون میشم</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84254" target="_blank">📅 22:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84253">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNFwgm48tsQDwRqlG74A8jsif0pu_K68UM2lvjpb6GNuvw-cip6ANhZHY-Dg7_uYnKQ-JaVQJHQHkR58RSu9XxuIymQwv9XSS7j6y7icVBlRUsGd9oYfigJnt5NlzF5IPDfVb5cfi6LzF3H-NHlEFH3oFYVTPTcswwBNTaKvgYQakxUO3wNMvGjGQzXUIIELTWe73leqaeeo2TDzcRw7jhcNPWzvpc3ClIY4wr7M4OXzOUI2x_2Zn_e_q2bMglfiFDvBqn0_Dmc7FfHKCdcUltT-wNP0lWam5gX87eGKFrHgGIE-MVNlRCOwfKxuWOXykdlM_0jxCXkiWsmTVCbHZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین موسوی مگه مجبورت کردن آخه؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84253" target="_blank">📅 22:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84252">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شاید همه اینا امتحانه خدا داره رونالدو رو میکنه</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84252" target="_blank">📅 22:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84251">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رونالدو رسما خودش اعلام کرد که کمپ تیم ملی پرتغالو ترک کرده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84251" target="_blank">📅 22:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84250">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رونالدو رسما خودش اعلام کرد که کمپ تیم ملی پرتغالو ترک کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84250" target="_blank">📅 22:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84249">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xbdwso7tvWMN_firoc_UPpq-16oLxLmPnT_7UrQP9oXNcYA-pSVzP6Lt6-1eCCfurjBNnqHFqWNEMpSsUAqQr8CpE1amKD6qLkfuBOtje9FDRuW1KyxEXIaaPlLzvHGqDvsL5ArvgGSPZyN6BQvzxF9BBKrT51d-baWuyWh8d-MNW34m8ubbcgWKOyoiBambcceeGJiIlUJFGjDeezNmHEWoCxm3sgsZYK50b7PosWqlOp4VZ7vI-FKi346AD-nK7HZ_U0Yj_0-RSE-8I70fRqhdCTap3sHK8F6kKLrLZ0y6RT4jYCmsoIIUYkNPlJOYqbZAszj8SeWc6xqIfJjVzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
🤣
🤣
🤣
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84249" target="_blank">📅 22:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84248">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSfSB7HNiGGhe_Gdb2RertAY0mJcIDEGoC3KR-b6BWEjfxjB8yrVNcrrg6P0REvmxPthlQhE2k5qkVnhosHNtw983TTX1Hd4dwV6yCNl0I4mX_X4OZnS1ExWSbMElj4CCntJn7oqFCJFzsUbE77fzMstSZ6UUisaVRg-pGkMiu9JhEYBSo0s9AInv2suaMyf5ATItdGjWFwf5iYfVrDVId2MLswKPVQD8lWE_oDSQRCYZLkwFMubKdZuwGkDRC1VdM1jHtOBluu0_8v0amEPcVIHpn83pzJbuMJMeaZzq0UAbdQiIheLOY8Pmrdj1lAE1y38gsBF6WazKDXLnwLWZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعی که من پذیرش گرفتم با دلار اون موقع شد ۳۰۰ تومن که رفیقمم میخواست بیاد نیومد الان بخواد پذیرش بگیره باید ۲ میلیارد بده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84248" target="_blank">📅 21:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84247">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRiz3qx55_aKe_S8r3af2Q76nRqXzSaeQDobYXpIlUy7LwyZfpKMSR3XhCFh-8gJsbK7PwEFZJs02SLHFZ8xyPbjpeHvhUgFo0sVL0OQigZruQOpoScaootZfSJJPnUp54HxjkaAAQLDDCdDaM2uMqOaewethOJorkG4fbiR1QQs5kaAU43VHsXRAdAhMw_1-3mjmA0Vq-oVtIe3lo4fWFgwe0e5857sz22BX4wnZhTf7_L7nToMIuuZFjNnk03_Ner7FXF04Cnxk5dfep2-B6ag0_CtXVvoH_2DjU0aBi2Nuk7G-uX4XqHtkYI7yjTgSn0VM1XoratW8khmm1prmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار میخواد بشه 420000 حالا اپلای کن ببینم چاقال.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84247" target="_blank">📅 21:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84243">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رونالدو چون تو بازی قبلی بازیش ندادن قهر کرد و از کمپ تیم ملی پرتغال زد بیرون  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84243" target="_blank">📅 21:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84242">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رونالدو چون تو بازی قبلی بازیش ندادن قهر کرد و از کمپ تیم ملی پرتغال زد بیرون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84242" target="_blank">📅 21:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84241">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwqgMg2w_qensTWKuwZeyYBUCn8RwYSry0jir3SVGwANZtDCX8jHHGbOzg-jePZ8ZXXUdhv61-2sDXo8u9BmCrBJu8RORuJEQJiEXf-ebP54YokBQA4j0J5k3LOPSTt8yTGeLS_cmSdsntO6wXtXe3-574mslIGV-Wg1f_F5Yzd4t3e7ru2usVxCzrzejVyC45dGVL1nm1Eo-T0C5Hy9asJsMpcddk24z1enZqR7KLfTC0rm1hOqwJXx-8lxl8vwS1_8rk1Om68KvmdvdL8NVgDxf-OHLFdOf6Em07vCKb1KX1ejJH_jjfS_CnA5pG8q_T50rihsVZ6J4lHystYfsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش تا حالا شده تو آینه نگاه کنی و از خودت خجالت بکشی؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84241" target="_blank">📅 20:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84240">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بادوم زمینی کیلو یتومن کجای دلم بزارم</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84240" target="_blank">📅 20:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84238">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5Mx-46a_IzUSju6LsxvUmBZCrTk-i4Lb0wdVjselTyqNjRzHhJQy_MQwVCPNJ1Gw_XSpuTGjH_I3iZxXTCuo9yxAqyuGDvfcw3kWfcB21NJ3z2CmB8x_ilz6PFSVCoCtYqPJ4Frrh9vvwHUTyizY1dGxDjTpavpm-pqhQXeApUPmpWHoFdbmVkRWbiJ0U1dsFg2OhAqw8keQe2Akv_y87Yo3bW97mRG_FdG8hZG94kmVO9bHDfzvi68sVUar9PleGrSdk8P4pDhEyV6u-sfrVbFOLJd2q3SSe3SiV8wJiaA_D1NeykdDT7RiwPp63TNvJv85rio34b3oyod3FXMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونم اتفاقی عادی تو خاورمیانه اس ولی خب تعداد بیشماری پهپاد جاسوسی تو آسمون تهران مشاهده شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84238" target="_blank">📅 19:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84236">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VA1vE1MOTbIxWsipSSPYOuGiVP6Jcs-5PQeT9lKqacEvtvdTuzBuLgviBh3zPQD4uN04K49_EEEDaCFZLknYgyKjSjHuZlPx0ufV5pspM4I6WZK1pwL2_oLV-mo6vlLbm2j82qQyHsBOGFB3SfDOSeNWSagcWJMqCU0yzsPxaXItEYJR0ggISRfLEeqZmmKMRPQdPk5HRR3534Z4uWGHaMudC1xGGF1Jj8jARjjBbVafaStmECNQ6nkL0ToBZ0kXewd2UjFXW-Vlq4_ZebXh9GNs80Bts0c-LZROZaGZnRJgifOe1tHQZPafbGMcoy0xrvJfvb0XRDSlVXXIB9Jg0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی خیلی بیشعورید
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84236" target="_blank">📅 19:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84234">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvgFuZYxpjQa-sVeFD5vBaTwez9hD0Ii3osCLTsvNnFePJr_xxAl2pRNpqFH8Y4pOds5M2unuvT5joME5TVnL0cXh54ZinkMnvBfZPhOxDdICSzwgPyrxDNQTwAcIJKTgGBPG_kTtFmEto2AHqakudt2ibl5xLCsf838EEnfec6FD_wVv5zHYLR8xR_c89cWJsm6nsY4hl3pKx1SHGnYtu2e0skhJbNjCe4n-EbMXtznrIFhY72wYvtVRzkgPU9PvKKMbkS7Q-OlP59aOVqzPIi1G8dzu_CDzUZJrrQnCi99BaxDPGU1lH6sXZItaPZ8GQ9Hf-NSm_psKg6BwLuiXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدای همه دلقک بازیا واقعا دلم برا این بچه میسوزه، شده بازیچه دست چهارتا حرومزاده منفعت طلب.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84234" target="_blank">📅 18:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84233">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/142f9f8326.mp4?token=gDDyVZoMoaGinC8HhQmd2mBndTwtV99wY1PSEGe7lzxiIJjNytTJwK6Eikpne4gYz1HLL0fE0SccoV2_KQKDUEh-sZubBD7xL1LFXEwV4kMbQpVM823FQS-AV1hLkUTfzbGk7L8D2gE8LWIAVfxqJxxCIyiQdA_qcMQT2r7sXkdH6k9lEQ2XmbaQ-zFlsdauFpx8fpVRersGCr8YdYt0aW-2wTC_WmbBYfhNZtA11JFqw4oa4BdGuIm7GL32_IOiwOoLCNs980Urz4aZrD4FFtxfUwolzxNyFo0XshhPytdO9PFdtRcxABhtdWYIbqRUyfAkSeOXdDj8y9r2rgDZsRNAPmIbuy6b3d900t6vSD3f_HX22-Ww3vXtYRl_S-a1iU72k3HxmejNIPbo_3vW6BssPqLiOuSYLhuhP8SruZAz89KvDiIwlztEG2agAJC-sIzk1zB-HHLbQbtO-35aq5SWlPCRM5sWv25MbvR8t39EJ2NmHF24NO_kvU3sakEkgEZsYoovuTQ_TrrD9bvm1568cWd85IrIW5CG0lv7rMPZnBGG-UajTOe2NLOjugYsI7QSot8JAbH-9qQwdoibrkd5xZLp-6-ImKftoYwCO1bIHoGxmNvNFz6TQSnrIf-XeHe3_iJDIlnnBj1W0kA4SZq8fY9-BnnCqmnY4spKE_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/142f9f8326.mp4?token=gDDyVZoMoaGinC8HhQmd2mBndTwtV99wY1PSEGe7lzxiIJjNytTJwK6Eikpne4gYz1HLL0fE0SccoV2_KQKDUEh-sZubBD7xL1LFXEwV4kMbQpVM823FQS-AV1hLkUTfzbGk7L8D2gE8LWIAVfxqJxxCIyiQdA_qcMQT2r7sXkdH6k9lEQ2XmbaQ-zFlsdauFpx8fpVRersGCr8YdYt0aW-2wTC_WmbBYfhNZtA11JFqw4oa4BdGuIm7GL32_IOiwOoLCNs980Urz4aZrD4FFtxfUwolzxNyFo0XshhPytdO9PFdtRcxABhtdWYIbqRUyfAkSeOXdDj8y9r2rgDZsRNAPmIbuy6b3d900t6vSD3f_HX22-Ww3vXtYRl_S-a1iU72k3HxmejNIPbo_3vW6BssPqLiOuSYLhuhP8SruZAz89KvDiIwlztEG2agAJC-sIzk1zB-HHLbQbtO-35aq5SWlPCRM5sWv25MbvR8t39EJ2NmHF24NO_kvU3sakEkgEZsYoovuTQ_TrrD9bvm1568cWd85IrIW5CG0lv7rMPZnBGG-UajTOe2NLOjugYsI7QSot8JAbH-9qQwdoibrkd5xZLp-6-ImKftoYwCO1bIHoGxmNvNFz6TQSnrIf-XeHe3_iJDIlnnBj1W0kA4SZq8fY9-BnnCqmnY4spKE_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جانی دپ
❌
محمود احمدی‌نژاد
✅
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84233" target="_blank">📅 18:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84229">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">میگن میرحسین موسوی مرد.
@Funhiphop
| Mehrdad</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84229" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84228">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بابا حداقل یه خبر از رشید مظاهری بدید بدونیم زندس این بدبخت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84228" target="_blank">📅 17:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84227">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgdRXmSRdteFqtj0yO_BsYD_kKs2o6Wpx-sfYNaQuLivrNHYO7yy3M6VpTx25w9XT2ch8OltDdmdSjrKPyOhO476aAXMGCqO261StGsFkUy4isiEI5w1ZDY_X4vPeIEkETFSHPmAY2djhT7kf2emlmMJCSWuYNkP2la0xSHK4P8vn9kuo9y1NupT6XmuDJVe1A0dz-QAQ5tHyLDFdL6b7Y0NKwZLXFTHE9Xv4DGXjRdA92SrWv9kT68SgtpxRJ6ZJgnz1Yw3waLkUupeIpU2G5RdQmzvr_clA-PcpQyJg4pnRnKowzX1ThEjJNYxOCN-CMuQHOy4fsX434iufzA0tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبریک به پسر بچه های عشق گوز
برای سریال ترکی "اشرف رویا" یه اسپین اف ساختن که اتفاقات قبل از سریال اصلی رو نشون میده و بزودی منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84227" target="_blank">📅 17:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84226">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">زن بیژن مرتضوی: بیژن برگشت ایران تو این شرایط سخت جنگی کنار مردمش باشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84226" target="_blank">📅 17:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84225">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvDFJcqzIbTO7WS-OjyTCkCqAvvSqHJWpUmfSZI4Qk7usSvJ0BRjLW7pZLigr5hD4PQuyXx9KutPIf8skrcswT4SgkxSKR--OCrifS1WwOr-QwRSe_xvnLtRkLEN8bIJN1TgSohiKdA6H-4CkyMFKNSQtRDr2N3t7OwKLhN3pNQdZ2xfACVJEop8OuYlRND2RrIBjWqhJhU1YZlaviYkUZBL7lOhmsGsseOAHFefCMrzTNK_oyrAclS16nK9yYDLEGP8DJpVdX5qfnDSI9w_s0zh1O51Yevo1a7SaZ6ofgpigIwwFYF7dtykaG2blowA-rWA3uDtdLkNr25_1ABHOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84225" target="_blank">📅 17:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84224">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بیژن مرتضوی که چند روز پیش می‌گفت میخوان منو بدنام کنن و برام شایعه درست کردن که ایرانم و با شرایط فعلی ایران نمیام امروز برای اثبات حرفش اومد فرودگاه امام و لایو گرفت.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84224" target="_blank">📅 16:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84223">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بیژن مرتضوی که چند روز پیش می‌گفت میخوان منو بدنام کنن و برام شایعه درست کردن که ایرانم و با شرایط فعلی ایران نمیام امروز برای اثبات حرفش اومد فرودگاه امام و لایو گرفت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84223" target="_blank">📅 16:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84222">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آتش‌نشانا دیگه شغل دومشون آتش نشانیه، شغل اولشون بلاگریه
از در و دیوار داره بلاگر آتش‌نشان می‌ریزه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84222" target="_blank">📅 14:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84221">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یک فروند هواپیمای مسافربری که از دبی به مقصد تلاویو درحال پرواز بود. اول از مسیر تل آویو دور شد بعد از کد اضطراری ۷۵۰۰ که نشون دهنده دزدیده شدن هواپیما هست استفاده کرد  @Funhiphop  | Mehrdad</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84221" target="_blank">📅 13:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84218">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2003caf7.mp4?token=fOQde5F_8N7C8xCiJHf8A3WVYzhq3lC9-e-B8-far4BjnGFLK5cjWhMTWU2DD6V-XhDGQmWrPbfHzMC0z3L4LiVuA6lORDoF1OYhwsP0GTxhekMwl5wnGPjxjdSzhfJgkOAfX58KWKr7ArCxd5TI5q-AnIQKa8hyFuLUZ97_kinsd3i__mqLA-iscxEojmBuG0isdEzsBO0F5CzLBjGw5dpeRqYqW4Qhg8qL4UK8VurJGaPFKaXwpXEtFDohk91IZwDYUhSWmV9TXVvJECyr--YE4krBiNF38cDk_lpYoDFZe0NWmAicH5JK4f7Ed0Dp78a4wg_1ZrSpmi1faLACOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2003caf7.mp4?token=fOQde5F_8N7C8xCiJHf8A3WVYzhq3lC9-e-B8-far4BjnGFLK5cjWhMTWU2DD6V-XhDGQmWrPbfHzMC0z3L4LiVuA6lORDoF1OYhwsP0GTxhekMwl5wnGPjxjdSzhfJgkOAfX58KWKr7ArCxd5TI5q-AnIQKa8hyFuLUZ97_kinsd3i__mqLA-iscxEojmBuG0isdEzsBO0F5CzLBjGw5dpeRqYqW4Qhg8qL4UK8VurJGaPFKaXwpXEtFDohk91IZwDYUhSWmV9TXVvJECyr--YE4krBiNF38cDk_lpYoDFZe0NWmAicH5JK4f7Ed0Dp78a4wg_1ZrSpmi1faLACOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میخوام برم استانبول کنسرت.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84218" target="_blank">📅 11:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84217">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1244f53d60.mp4?token=SfxBTM7LhMUVBuMdZXHhQ8H1QFAP65R0kNvmEsctPOisa4VbM6UCA03yoq-9C7D0GsYsM6i1ooLgBGeUD_0hkhilPE6KQA2sEP9POZbAVtFlkNBJSuUcvLkqJnPoHrQ9dbo7s2bG5T56sZF17R7K9ezsCM4Bj-oo1Au2rLkpiKcHdWZRqdPDegKyQwrirYDX5V30Q190dtSMecYz24uZqzM8U1YqGDeRttmM6mTn1Sk9AkJADc6hfENd9gqXOp9NQpI-Rke1NjxLKSQ5Z5me-cRAwpVTBKi6MuVj6rda4PBfiGKDpF5b8SXNgGs024W6luSbOfwMKwRR9hASY8SvJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1244f53d60.mp4?token=SfxBTM7LhMUVBuMdZXHhQ8H1QFAP65R0kNvmEsctPOisa4VbM6UCA03yoq-9C7D0GsYsM6i1ooLgBGeUD_0hkhilPE6KQA2sEP9POZbAVtFlkNBJSuUcvLkqJnPoHrQ9dbo7s2bG5T56sZF17R7K9ezsCM4Bj-oo1Au2rLkpiKcHdWZRqdPDegKyQwrirYDX5V30Q190dtSMecYz24uZqzM8U1YqGDeRttmM6mTn1Sk9AkJADc6hfENd9gqXOp9NQpI-Rke1NjxLKSQ5Z5me-cRAwpVTBKi6MuVj6rda4PBfiGKDpF5b8SXNgGs024W6luSbOfwMKwRR9hASY8SvJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پسره برای اینکه علاقشو به دوس دخترش ثابت کنه، رو گردنش تتو زده و نوشته: من سگ دوست دخترمم.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84217" target="_blank">📅 10:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84214">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یک فروند هواپیمای مسافربری که از دبی به مقصد تلاویو درحال پرواز بود. اول از مسیر تل آویو دور شد بعد از کد اضطراری ۷۵۰۰ که نشون دهنده دزدیده شدن هواپیما هست استفاده کرد  @Funhiphop  | Mehrdad</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84214" target="_blank">📅 10:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84213">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یک فروند هواپیمای مسافربری که از دبی به مقصد تلاویو درحال پرواز بود. اول از مسیر تل آویو دور شد بعد از کد اضطراری ۷۵۰۰ که نشون دهنده دزدیده شدن هواپیما هست استفاده کرد
@Funhiphop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84213" target="_blank">📅 10:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84211">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZ1dD7blyIJiFvMGuZWJd1T4Oq4vUltKY_jI3irf6RdiupNsu4KYnj6UIOvqShvg17Ib6EroTHvNoV9pAAAu6hwG3tBQor402VWui3J6JG7mfqb6pyF32z58-sQQw8u4jIvSrJwu8ctHR06EKM8GppsG-UUq9V0wb71JwQqZa1Sci859XI6vX2Zg_aJpgN3iiHB6xFz6CikcQw5_yB4bxVxTZVu2mw3KalH_ZsgVw7zAScrlF3y7cVD8XgVeXNiT0QJM5QyFqCfisW48YJOpj9o8GIDPd1-R77XqKR4ACZgYRG8brIL2S9y0-7Hez15d1W5CdnXpEQ5I8ZGRfKhAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dacdc1485a.mp4?token=SqaTRTNOig1wd_W4qsyyVo-2PhjtFMa-VzY2UA4xuAw-b3buAy6hGPNO4lxaZ-3-EC5U-hHcbDvwIC6oHI2zqzt_3MBBWH8kdhjW1PwCktOTxBTpLQSE7FUwIWqRZCXF5cEd7wqBWzoyrnuOWj1A4kg6ArdBouJYCUBUtdZY2JVaQidN-vnLiy9OtHaLiddAurMUrM4hb5SmdKLVvzSpqtCrRdvdtm3IGcDlbj00h8ht4rsr2fLN3H1itIQnsX-HVTsiRhPFCSa3ps4mC8ATuncm8msGytV5uSYk0qxXunKscgeGsf8BbiXZJLEPG1rhgHXSf2xho96iXoXsvGLNsmNtt15NUqsjd0YNSocCHmqlHe6bX-EwA6zTVJS2wzzbMKU0nk-zQ9f0pBfcE9MZ_ir9E6IAcJJNuFO5fNqP8ZH7UZtSXWucQ7uaanmKkztKpto8UyBhdR4BGxdxtxFZMNtYdaPSWBH2_FnXnbPC0V71EgtRtq20DTm1ESpeqxNhhNYx8DcEYDiOW-qPGAglFIpcZ90c3h2ZpSiOp1UV6GeU-77t-QKp7vEJVjWY5k6XVSVBiWdad1unduNxHNaWxaa0r2zPk_LwWXZt5uvW_tgsoTVsEOakgXahmYlL4DjkXQA6yAViCmXpB3trV19hWXq7Lx3vindgHeg1k-DJSXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dacdc1485a.mp4?token=SqaTRTNOig1wd_W4qsyyVo-2PhjtFMa-VzY2UA4xuAw-b3buAy6hGPNO4lxaZ-3-EC5U-hHcbDvwIC6oHI2zqzt_3MBBWH8kdhjW1PwCktOTxBTpLQSE7FUwIWqRZCXF5cEd7wqBWzoyrnuOWj1A4kg6ArdBouJYCUBUtdZY2JVaQidN-vnLiy9OtHaLiddAurMUrM4hb5SmdKLVvzSpqtCrRdvdtm3IGcDlbj00h8ht4rsr2fLN3H1itIQnsX-HVTsiRhPFCSa3ps4mC8ATuncm8msGytV5uSYk0qxXunKscgeGsf8BbiXZJLEPG1rhgHXSf2xho96iXoXsvGLNsmNtt15NUqsjd0YNSocCHmqlHe6bX-EwA6zTVJS2wzzbMKU0nk-zQ9f0pBfcE9MZ_ir9E6IAcJJNuFO5fNqP8ZH7UZtSXWucQ7uaanmKkztKpto8UyBhdR4BGxdxtxFZMNtYdaPSWBH2_FnXnbPC0V71EgtRtq20DTm1ESpeqxNhhNYx8DcEYDiOW-qPGAglFIpcZ90c3h2ZpSiOp1UV6GeU-77t-QKp7vEJVjWY5k6XVSVBiWdad1unduNxHNaWxaa0r2zPk_LwWXZt5uvW_tgsoTVsEOakgXahmYlL4DjkXQA6yAViCmXpB3trV19hWXq7Lx3vindgHeg1k-DJSXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی اومده یه سکانس از برنامه فان ۳۶۰ که ژوله اجرا میکنه گذاشته و گفته خیلی خفنه و اینا کاش قیاسی و ابوطالب اینا جای جلف بازی ازش یاد بگیرن و همچین شوخیایی بکنن
حالا قیاسی اومده کامنت گذاشته کصخل چی میگی این شوخی رو خود من نوشتم برا ژوله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84211" target="_blank">📅 10:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84210">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64cf794cfa.mp4?token=aJ7SZGC2sWBv4qQLv_xgBFPyKCRzsfrqkBeWjjArvQmIAbkWpzXi4CIZEgQ915kHq5t27O1oWKG5eNCXvPAyiJxy9kdah0y135HoRJl6_wICg-6Ng96ZQuNr9WC0bl4WJ4uroWtj2XkFUD14AHucmwdn4BqYsqaGr6ogZWAB48etQlv5_pIbEPFdkYBcEUklYxP7w2Zhw3fvYwTbQ6aeZUQypcAmYFgIhtMNyQESnVsfSmKEJCutiEF9xkw1_YyDpvBzViSEcMDctsDNH5wUBL9UFo3WSpl7ay3FrsUhxEJbzWA-FnQ7i7P-nBmf-cXSrgvoJ5NJ4iDUunPt_4htgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64cf794cfa.mp4?token=aJ7SZGC2sWBv4qQLv_xgBFPyKCRzsfrqkBeWjjArvQmIAbkWpzXi4CIZEgQ915kHq5t27O1oWKG5eNCXvPAyiJxy9kdah0y135HoRJl6_wICg-6Ng96ZQuNr9WC0bl4WJ4uroWtj2XkFUD14AHucmwdn4BqYsqaGr6ogZWAB48etQlv5_pIbEPFdkYBcEUklYxP7w2Zhw3fvYwTbQ6aeZUQypcAmYFgIhtMNyQESnVsfSmKEJCutiEF9xkw1_YyDpvBzViSEcMDctsDNH5wUBL9UFo3WSpl7ay3FrsUhxEJbzWA-FnQ7i7P-nBmf-cXSrgvoJ5NJ4iDUunPt_4htgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بلاگر ایرانی تو خارج که اتفاقا فن کوروش وانتونز هم بوده، می‌ره یه ویدیو می‌سازه که توش نظر خارجی‌ها رو درمورد ظاهر سلبریتی‌های ایرانی می‌پرسه و عکس پارتنر کوروش وانتونز هم اون لابه‌لا بوده که کوروش برمی‌گرده به این بلاگره فحاشی خیلی سنگینی می‌کنه.
بلاگره هم برمی‌گرده می‌گه زنت ۹۰۰ کا فالوور داره هر روز از خودش عکس می‌ذاره بعد حالا من عکسشو به چهار نفر نشون دادم اینجوری فحاشی می‌کنی؟
به نظرتون بلاگره مقصره یا کوروش زیاده‌روی کرده؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84210" target="_blank">📅 03:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84209">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpqTncmWv7eKBnz2ZS8ure87uGLO7FHPGzziEeF3DLcWVA6qsS9DFCCt-u4YyMcHmxjJJjpMlpkBCEox477TTVPeFece1q0Vcmff7RoJxmXSF3j8cYwhDYdQH9yxpY2pncpOd0QTsZiRaGoBGqO9RorSWQO7JFXklt2sO9VzeAgoxbanWBy3eqU2GiVvbkETo4-UiBC-zC6Vn53ywkcs7L5PERtTQjlr5CRlsfKREhpVnDByZOqddEFNTrCCi2isqm-PV5dYtYh5jPkfKhaM0hdpoiZnP-oEsgKkj-88ACcPJ8w97ZKdcUxrfwBydKZj1-6-JLZH8uT9fgAyhzhizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواب از کلم پرید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84209" target="_blank">📅 00:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84208">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/of9tj9BDjKNoXYQ7xB-Whf8kqzElkwVLEC3RGn-_e__BhXOlD0NOiy3fDbX8fnX-V1CNFcnphBb-PVAd5N2wAPUv2BfVjPxesUNse3kNleVPLIh3Iy4G9FaO5cSPwszLjWXZQh6359xNaDjXfJJ21MvF_q4X3IkKFEmau39PDbWOXYOV6HI-K8jWzQEHV0PG0TwUxmeu1Za7VQGzOrjbEjO2pI0NkxsuTB-A3gG1GuePrFo8R9VKpqEAcxEAgvRelY_vfi4p442dRDf7A7Hxbjjn8DQPA7HDW3hBR24KL9_BPIDLXOstcSWGegOiEfviX5kkzDeMOPWYLXp9pfpwBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بیانیه میلی‌گلد: بعد از پیگیری‌های میلی دستور آزادسازی طلاهای میلی از بانک کارگشایی صادر شد
خدمت تسویه و تحویل که به علت مسدودی دارایی‌های میلی در بانک کارگشایی مختل شده بود، فردا عصر پس از دریافت طلا از بانک کارگشایی به روال طبیعی بازخواهد گشت.
همچنین طبق دستور دادستان، محدودیت‌های اعمال شده بر درگاه میلی رفع خواهد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84208" target="_blank">📅 00:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84207">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رسام سهرابی جان مادرت وقتایی که جیحونی پنجره کیریو ببند بعد داد و بیداد کن سری بعد زنگ میزنم 110 میگم پرونده هم داری
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84207" target="_blank">📅 00:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84205">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">به وقت سم های عشق ابدی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84205" target="_blank">📅 23:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84204">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فرمین لوپز تو کیر شانسی میتونه با ما ایرانیا رقابت پایاپایی داشته باشه واقعا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84204" target="_blank">📅 23:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84203">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پشمام از یامال</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84203" target="_blank">📅 22:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84202">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rsp9OZDtIHTq1asvBFPco7_rRJwbaYiblpNTKjGr6ALuR2p6esfWygOcbwu8kWPHwl4dM80VykcVPkghz2nuDhYiTFzLTXdMetQ4bQv3hq4HyT4W9G6WpJQsIZCkhnq2mkFimtKGH7Lb5qlV-rOgPHRno_GMiF0oKkLtS8opqInpVP1WKqaOnIywua9QxCe2RLuFBuJcTZFZoahBGdINyK3zxWF9m-Q3_AjQh9pnJ9ZVMGh4FPupwmEFBzUkXRkjzE_KsJR8T84sTu2iRpUaLFNeTqyPIP5ChsbLeTpHJlVoU7rLgwQKzB7RN0utLQN0lTsnSdgPwa3oGj0k3-sA4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز همزمان با پلمپ شدن مغازه های ربکا عکس دوس پسر جدیدشم لیک شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/84202" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84198">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یاسر بختیاری در یک لایو ۴ نفره اعلام کرد فیت سه نفره او با رضا پیشرو و tech 9 قطعا در کمتر از ۱۲ سال آینده منتشر خواهد شد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84198" target="_blank">📅 20:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84196">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بر جرعت میتونم بگم رضا پیشرو درحال حاضر رپر هایپ تریه تا تک ناین
و رضا پیشرو انقد هایپه سه روز آلبوم داده و بعنوان یه ادمین رسانه رپی هنوز گوشش نکردم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84196" target="_blank">📅 20:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84195">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یاسر بختیاری در یک لایو ۴ نفره اعلام کرد فیت سه نفره او با رضا پیشرو و tech 9 قطعا در کمتر از ۱۲ سال آینده منتشر خواهد شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84195" target="_blank">📅 20:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84193">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbubouJl2im__rkZf8XXon0HTsfXArJGRtQCUM0snc1eSp-Re6yNx4e_a3uv-rkGt1lcRImpIAYAMZJg2IRoFoPkMNd-vAAFX2ejuJd0I5z0flLvwbLokiulGarD7-sS069hjihZeO_W409FEvXpil2-PPnU32lTYSRr8r3iSCLFKZsqE551LUES9dZn9KdcpeJq0DHCHYhNR_lZ1UfzZPE1xGWqJLpcHjm8FiTA7yiGCfGwHflzOnJovW1-6htaYaUfYebevw6IYd2lmG6-qSDlEVmV2AIg3TPNWZzipcfcP1hiXIvNhMYrRdEIGad_W-DeLNMvLeGf6P3zvAbtFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا باید صبح بیدار شیم از شیک زدن زنمون فیلم بگیریم بزاریم توییتر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84193" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84190">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سیتی محکوم شد و بزودی حکمش میاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84190" target="_blank">📅 19:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84189">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PO08BD1k9ALANO6PZWwEhfncveqvJ9gAf5LirN1Mg5vC5WZEJYszWc0tkslayq93BKr3SN4VtvWjZ0uo6PkCCfW6g2IAkvDUbABDR3tPQ6h_NUqCPD1Jwv3pSHbUghza-6UauGUM9ED87IA-0i_gtRxTnSpbGq11frBREyYTS31EJjcFqWupnoY5u6Z7BlldSui9HZCEbjgg7l8b3kZoP0mOFR_qz_x0pGjSHA-dN44KczYlmMUen3lbrgrYDvyWYePkLgYNA8wxK3en15fmAcnBlArIjxILG55LPtgWycZW34dpO0TQab5tN83RryQqbjJOmOk1PrFIImr-TqOWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید آرون و کاگان به نام "انکار" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84189" target="_blank">📅 18:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84188">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترک جدید بهزاد لیتو و بیگ شگی به نام "1.6" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84188" target="_blank">📅 18:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84187">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZheQyhRrPKl4qqcVZqzseTCwmX2YjKKWdIMipoVHRWZBO5lw04e0FmnlgR1PjHPwwDcnVjAr9fn0JJbbyduVyoiZFFYUHFRzfEMQquJmJl4qiT34_fdgqp-__3cOHChtLToLLJLEWhVJlI_Chu0D4JTZyx96HOPzZL-K3Brmj_bAQHgqF6nptyznAJ1AlpffV8LCBBeIr6QKuUDhmH-g7VGEU447XN54NrUw8P39oAhOpX4aNsfRN7uoJgcQKK2d1rNjd7WXANw2OHeIaW7Pkxo_hWS74xqa7WF2DmdYQRg6nCePFbYpztUe08mkmwzsYCsPKBR3k4kbfPsMbdAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید بهزاد لیتو و بیگ شگی به نام "1.6" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84187" target="_blank">📅 18:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84186">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJ8G0C3Q71K2ERMYV_e3WD8vR7ULsdEsgX-EsSHhoISISnv97c6RBkMNFFhFc1g_KFuH30drcyXZxZDeG7N2MumD61NwS6-GtpOW_pgS7WDbgUfZJ6wxcKKPx-hwgRgXHZsdnBKReYxCAXqjFJ55GEclavae4YogldVpYuzGSOIyz1uX-psRB8muoNsy2fak10Vvefj2ZHPR5WNln5pItRpVGuX5JaszABldejT7D_jQsEbRkmln3P7p6azI3L9OEL0S2u0eLNLgYIKZhZ94owntFPAsB8Egc9pyvEDe3XcPSnxojqSJijiZV8e9jtuc-Pb_qlEBXZQ86oQ1sPCp_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاره شدم این چرا اینجوریهههه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84186" target="_blank">📅 18:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84185">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862ec698b.mp4?token=kK7ybMhzEg0jvWwf9oEhBeZjZ9bDm6AIPVWfWMtY-A0NvdEDbeUDpGcxhIYyTi_qu8Tat_qXjLUMI2NXpWOUANEhqQ0HxZwPbBQh6NXr3shcpFG1lSWpO5Espdhs7RNWWmCeDJELLkb45oxUklQOVnvnBEpWZx5IBvybgzvuJ9XMfqaxAcVmwhEOdk-BC7_BE1vvxiUbc-uHdSWmOEQzoMKXAkVNeq7-WsAbEqns0IbDSWGqIFxPdBLXYrK1lMl-j4cyi5gK6UutHZizqAUk2GYHgfhtdNqEpFsAceOzGpWCk-Sr9rV0VVHJ_NQzsTp28GtRHtfKnhoE30a3VkCrsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862ec698b.mp4?token=kK7ybMhzEg0jvWwf9oEhBeZjZ9bDm6AIPVWfWMtY-A0NvdEDbeUDpGcxhIYyTi_qu8Tat_qXjLUMI2NXpWOUANEhqQ0HxZwPbBQh6NXr3shcpFG1lSWpO5Espdhs7RNWWmCeDJELLkb45oxUklQOVnvnBEpWZx5IBvybgzvuJ9XMfqaxAcVmwhEOdk-BC7_BE1vvxiUbc-uHdSWmOEQzoMKXAkVNeq7-WsAbEqns0IbDSWGqIFxPdBLXYrK1lMl-j4cyi5gK6UutHZizqAUk2GYHgfhtdNqEpFsAceOzGpWCk-Sr9rV0VVHJ_NQzsTp28GtRHtfKnhoE30a3VkCrsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی چوپان: یه ساله دارم کابوس میبینم؛ باورم نمیشه دیگه محبوبیت قبلو ندارم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84185" target="_blank">📅 18:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84182">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ادم اخه طلا رو مجازی میخره</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84182" target="_blank">📅 17:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84181">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">معلوم نیست کی خورده ولی نزدیک ۲۰۰ میلیون دلار اموال مردم تو میلی گلد بگا رفته و هیشکی پاسخگو نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84181" target="_blank">📅 17:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84179">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf73bf24d.mp4?token=pzGsU4bxNiaQGfFk10ZiucIEOeIhP00XlLHZOlOJ02FcYQC6HBdNgW_k-GvGfzzZQjW6ZZm8kWmBXYk-8Z3Ri472pVzAKLD_IS77pZOQ_GRz-mvZMBwDoydU5PVU53JuTUGDyx-8zgsm6diKE48Y_QXh0MJkvC2_pLN3ONUwU6VdEEu2ZPkxFNH9udc0YgvXPtZCu2GSCnfrGRJr9HXsiRr8CuhXexCeWGIDAyh5IIvLhVM_p72SvZZeIbf0_Ga6gTt8V_S3N7iyKqBQy4rs1xZYVhBlHHkVLdxW8lf54OX0NGnq4BakZ_REjcyZvU5liHMZTYnHWhUHbg-dMm3G0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf73bf24d.mp4?token=pzGsU4bxNiaQGfFk10ZiucIEOeIhP00XlLHZOlOJ02FcYQC6HBdNgW_k-GvGfzzZQjW6ZZm8kWmBXYk-8Z3Ri472pVzAKLD_IS77pZOQ_GRz-mvZMBwDoydU5PVU53JuTUGDyx-8zgsm6diKE48Y_QXh0MJkvC2_pLN3ONUwU6VdEEu2ZPkxFNH9udc0YgvXPtZCu2GSCnfrGRJr9HXsiRr8CuhXexCeWGIDAyh5IIvLhVM_p72SvZZeIbf0_Ga6gTt8V_S3N7iyKqBQy4rs1xZYVhBlHHkVLdxW8lf54OX0NGnq4BakZ_REjcyZvU5liHMZTYnHWhUHbg-dMm3G0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خارکسه حداقل بدون لهجه فارسی حرف بزن بعد بحث وطن و وطن پرستی بکن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84179" target="_blank">📅 16:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84178">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یه زمانی خارجی ها مسخرمون  میکردن بخاطر کالا برگ ۷ دلاری الان چطوری بگیم  شده ۱.۱۷ دلار
سخنگوی دولت: خبر خوش دارم اونم اینه که الحمدالله بحث کالابرگ حل شد و از نیمه دوم مهر کالابرگ رقمش میره بالاتر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84178" target="_blank">📅 16:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84177">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">در همین حینی که قالیباف گفته اگه ما نفت نفروشیم هیچ کشوری نمیتونه بفروشه تو ۴۸ ساعت گذشته ۲۲ میلیون بشکه نفت از تنگه هرمز خارج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84177" target="_blank">📅 16:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84176">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKudwMFOPCgo-_zwG4CwBwlCOwyTyL0MquthX4nf4PM75zWiS8BMYzq5ChklQY5FpPdp8K9t5UuOGjsN09FeOCcj4itZBJkRb5RIDgmtt4CIziqs5xv7QF5PYgvynwwdixiFFPeDmwtUhxiaA4CfaNvXp4sDoWi-FDYmtDuydgb6ruMGzp7uryBKal1eRpC1BB8tiVdlC2u9kjdyhCR3JGvuFvr5rgYYMNafLmZYzoniC5SrqCiE8pyCLRrBJ_PYh2vUZlQaOojoIGp6mtsI2NNhN7alSLW7t9M3tNrQhlOyiU6xKBOpNKfXVqNv7kM6xxz_aAMrQr1dt0WtdI1eyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار دیگ ترکراری شده لیر رفته بالا ۵ هزار تومن انشالا تا اخر ماه دیگ ۱۰ هزارتایی شدنش رو جشن میگیریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84176" target="_blank">📅 15:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84175">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تو این دوسال آنچلوتی که سرمربی تیم ملی برزیله بیشتر از سرمربی های رئال به رئال خدمت کرده با مصدوم کردن رافینیا   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84175" target="_blank">📅 15:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84174">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آمریکا بعد از تحریم کل خطوط هواپیمایی ایران، الان فقط یه مجوز یک ماهه برا پروازای ایران و عراق با کلی شرط صادر کرده که توش فقط می‌تونه مسافر زیر نظارت کامل آمریکا بره نجف برا زیارت و باید از همون نجف هم برگرده ایران.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84174" target="_blank">📅 14:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84173">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">به کسی که حمایت نمیکنه ازتون فحش میدید به کسیم که حمایت میکنه ازتون و بگا میره میخندید
واقعا آدمای کصخلی هستید</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84173" target="_blank">📅 13:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84172">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هردو فروشگاه لوازم آرایشی بهداشتی ربکا قادری داخل ایران پلمپ شد و تمام اموالش داخل ایران مصادره شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84172" target="_blank">📅 13:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84171">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOoR6SSgr68qX81LyUVFGbyIzAMeAAgaYBz3mvZtchd82A0VB2mnZ4OULMoJLM6wmhIbMpz76Q_2UT0L-q8rT7lTgV1kceYcpBCVW4QfBYUd_qp6Cerbw_moYMpaqDBxtqGY7gDk3VtImXydjknmwMpbANyoTz48BrHYux5aMhhoSKg_Ak_OdWiBcdmzw44ZwbZ523N9ZbC5oGCV1mjlJ0xjHCbfjeQkFa3Ml3_9s2x2pHCtPQ8XyljdSLbPfiNq0BUypSMrNNrYJ01KkgdeVn84BIYCIeqAPiXnfTnC1VeHTEEpDIG_YElUUqGh5crF0eFVtppKD_8ikhiTrOeANg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هردو فروشگاه لوازم آرایشی بهداشتی ربکا قادری داخل ایران پلمپ شد و تمام اموالش داخل ایران مصادره شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84171" target="_blank">📅 13:55 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
