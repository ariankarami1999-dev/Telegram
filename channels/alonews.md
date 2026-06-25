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
<img src="https://cdn4.telesco.pe/file/JV41u49pICKvxhtDZUmkLpYUSvjOzg2peqlHugpy8sLZ7cnVeQil0gqkQ8gaD0G3KFCDAzTqiaCoPDQD5cxfUBXEuODQHdq0BI7Zq2vMWw5LfXu10RRY2jg0ChA4jnFPgjtbFxfYb6m1rIjovPlgvipke9PWJPyQ7tWHVkaOgPUW9BNsmoMLDuVEkcxdP5nFhNgN_KEUfIV43tWA05hHob9TdvXzxCFXYbneMgHlWm06pAkKqdfFda_CagrRRMqVKYT-ik0uA2fKUoRGt8GLRnNQ10CLkWOWJ9aQ0iPJFEb4t9O0xFVC9WNkQzTHO5NwtUs6E6q96VISXCRTYF4NxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 943K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 11:10:51</div>
<hr>

<div class="tg-post" id="msg-130133">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
روبیو: ایران در سوئیس تعهدات بسیار صریحی داد و اگر به آنها پایبند نباشد، گزینه‌های دیگری پیش‌روی ماست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/alonews/130133" target="_blank">📅 11:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130132">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7905e956.mp4?token=aksLw8pNm5Y2A9mDFlkObpEIyJUzY8PV9Gy2EdC1CV5JRZeUJ2sbuX1aoehwNOCgKsZCgUn93J7-q1abjmvNuLiuZMltbXRkrffXvUi3GJcJxMo7uGoOEjHCY6sVrq07CVe9d7XMnc8nZsNTliGWwN5pMWEXL4tspaY6Aha6e8wPFrh_xEeEr9oZ_fyzmz2n8RgCkmUcDgd-o7pu4QolSBukl1zJkur01eah_sCK63TgSJ3tXGXJvi9xWtMm4yKlqjos2_U3V3hvpYr_Sg5fmRbWDznmdhIT6EvOU-Jtq2MNueYlHJf1s2D91Se5P9f6a1ZOBoVSf6vzUrftEUkAE68ViBdLTChlM7X8I4gcQoSR5Fbcg5elJ7nmwzk9pOz_1TLNLkowsBaeKXvtHfuAyjhL3FZXtVfVL3Ejgm3Iz1a1fO__lHN7_aifQDCWAisW0p9ev236jqIg2wRQb6KMr6IcF5SQPuXVYOTCIKwufawexCFFRHcgWwm_8mWE2JCExg-KYR5tcUX-dxnLu9zCa32hoO-TGd4i9LsQdMJm_spPirJesgGqTZrseE4m_K2TFLpIV-Qmh_1usgQI4TsIbfDBBToOHz2NO08afbMEtV-L01i2gFcWgolMqbjQbj_nfOUfv5s1sYSJTMy4RnK9NVkRoCWFkverY-0UgryE4mo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7905e956.mp4?token=aksLw8pNm5Y2A9mDFlkObpEIyJUzY8PV9Gy2EdC1CV5JRZeUJ2sbuX1aoehwNOCgKsZCgUn93J7-q1abjmvNuLiuZMltbXRkrffXvUi3GJcJxMo7uGoOEjHCY6sVrq07CVe9d7XMnc8nZsNTliGWwN5pMWEXL4tspaY6Aha6e8wPFrh_xEeEr9oZ_fyzmz2n8RgCkmUcDgd-o7pu4QolSBukl1zJkur01eah_sCK63TgSJ3tXGXJvi9xWtMm4yKlqjos2_U3V3hvpYr_Sg5fmRbWDznmdhIT6EvOU-Jtq2MNueYlHJf1s2D91Se5P9f6a1ZOBoVSf6vzUrftEUkAE68ViBdLTChlM7X8I4gcQoSR5Fbcg5elJ7nmwzk9pOz_1TLNLkowsBaeKXvtHfuAyjhL3FZXtVfVL3Ejgm3Iz1a1fO__lHN7_aifQDCWAisW0p9ev236jqIg2wRQb6KMr6IcF5SQPuXVYOTCIKwufawexCFFRHcgWwm_8mWE2JCExg-KYR5tcUX-dxnLu9zCa32hoO-TGd4i9LsQdMJm_spPirJesgGqTZrseE4m_K2TFLpIV-Qmh_1usgQI4TsIbfDBBToOHz2NO08afbMEtV-L01i2gFcWgolMqbjQbj_nfOUfv5s1sYSJTMy4RnK9NVkRoCWFkverY-0UgryE4mo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: همه به ما احترام می‌گذارند. دیگر کسی به ما نمی‌خندد. دو سال پیش، آنها می‌خندیدند.
🔴
حالا، ما محترم‌ترین در هر کجا هستیم. به آن فکر کنید. در هر کجای دنیا
🔴
دو سال پیش کجا بودیم؟ ما مورد احترام نبودیم. ما یک شوخی بودیم. ما دیگر یک شوخی نیستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/alonews/130132" target="_blank">📅 11:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130130">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLPDKaCc2sQm_4x_SZLKFHGucW0CqSZu0vB_4ZKkgEjfXoUMTFW9Yyw4MXSPZsIWp7Fmqh0dqNLs5yKJaF7HGfdnRsV9Io9Bhx9YLhZSlJXYkSnVg5aRannxvQDHFwvM75NlWYw6n8LCTgYhWA7A_tp8Sv20slLZzK47qhA2BXdNXP9NfWIQbhkCGNyXUkB-Vuf1cATMeY410SHb-op_9aeW5PdlNcyAplLqa55YLo066fwqetFpi6-82wsIdQhZg4bUU38Kw0mXsEaPL9yTVw-Ss_gwt_Qr2L6DiYtqTIpDo_5AGXUDyQC5BEgoeJ1-KOd061hF_sTqpErswWoPCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZNzJvX7taOF_Dqt4tpCfy47i_ItQ-03IVd1e2hrAxPh237jD-jD6SvO_fToSnTLb-ZH8pwrsDlR9oMJWTaH4m5V9xg36lPWipblTkpjtl2cUUcCvRLe87e47Aojoio27e1UGCzd_6iwimPXa_SFAp2uHpE2982LwlvVBpShOeNga68eyE7_u9OOs5Nz9n0920Xko9l8x-lpFnXFYNqI9sPQko7tghlc44WZ2frV3inxHiNLStz6mkSCesDrLMuAmUBF41gGipfeje2mK38t-D4dNodUEclCjW6IEXs5cK4kdgJlhExY9mATqyy8gFfc-Jj1wuJsKAgLYIlgMn9cqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ایران از عمان به دلیل صدور مسیرهای کشتیرانی برای تنگه هرمز بدون دخالت تهران انتقاد کرده است.
🔴
نیروی دریایی سپاه پاسداران انقلاب اسلامی در بیانیه‌ای اعلام کرد که «برخی مقامات» - بدون نام بردن مستقیم از عمان - بدون هماهنگی با ایران «مسیر جدیدی برای تردد کشتی‌ها» از طریق این تنگه اعلام کرده‌اند. این بیانیه افزود که «تنها مسیرهای مجاز تردد» مسیرهایی هستند که توسط تهران تعیین شده‌اند و هشدار داد که هرگونه مسیر دیگری «بسیار خطرناک» است.
🔴
این اظهارات پس از آن مطرح می‌شود که عمان با هماهنگی سازمان بین‌المللی دریانوردی، «کریدور دریایی موقت» در تنگه هرمز را اعلام کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/alonews/130130" target="_blank">📅 11:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130129">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRX_LOpvEUnVHR9DlXDfY9FAgWPbkxrSvSoWZUC4EWzt80VcvPj4511GkpblsD_1OVkri6WDYjr39LUoWAY_hA6BeOt2eOnKa5ZPDCW74QVCoFmwan6T_VAH1lH9--wtVWWpSH5z2lAF6T5mLGKCnq594U5Sg2vlds_F8yeNXVDEApNZFkI8Hhq0n9q1xUK_QpuBsNPSFdgWPt65w6EoPqTogfxQ9SgDcBwPdIGSkdPkRR_NCPxUfA0yTqEGkTNASFcae8kQvakE9XUQY77Z9kFcM8EVFKnA8GcW4x3iGz3ljgM2J-5MFDpRs6y_lCsVLgk_mbjDbNUYVpVKS7pq0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:وای! سنا رأی خود در مورد ایران را از ۵۰ به ۴۸ مخالف به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر کردند. از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه متشکرم.
🔴
این رأی، ایران را در معرض توجه قرار می‌دهد! رئیس جمهور دونالد جی ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/alonews/130129" target="_blank">📅 10:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130128">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ارتش اسرائیل از کشته شدن یک سرباز و زخمی شدن سرباز دیگر در لبنان خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/alonews/130128" target="_blank">📅 10:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130127">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fcd190313.mp4?token=bBKU1xjNidGFZcLRIWmGDYxfH_CpfkA9MeEpXxQo4rN6YpXWPzXoccAODjc2SYtj2T2Py2KLwd60SftiYXk5gZA6XnNxhis43WAtvEqHGb8BiibWuCyuZWe3wLlzv1_CxrKCsz_5Lc0sX3VKxxEoM7nOaCiln9WAWxVfePeNS-KrL4lhp9EDAcwLMFCsrSEmZESSbyYFd9TfGSOsmUrltKVYSHw_4PAqZC256Uh-G_aEeYHa6FMLQrRawSlvnYR4iHoAvb__nMFP58hjWvbNtuKhudkadnqcRw8UUNNXmuZibZf2-aBHcQ0H_9GQap-NqvQDN10pzka3WRAWGHQ_JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fcd190313.mp4?token=bBKU1xjNidGFZcLRIWmGDYxfH_CpfkA9MeEpXxQo4rN6YpXWPzXoccAODjc2SYtj2T2Py2KLwd60SftiYXk5gZA6XnNxhis43WAtvEqHGb8BiibWuCyuZWe3wLlzv1_CxrKCsz_5Lc0sX3VKxxEoM7nOaCiln9WAWxVfePeNS-KrL4lhp9EDAcwLMFCsrSEmZESSbyYFd9TfGSOsmUrltKVYSHw_4PAqZC256Uh-G_aEeYHa6FMLQrRawSlvnYR4iHoAvb__nMFP58hjWvbNtuKhudkadnqcRw8UUNNXmuZibZf2-aBHcQ0H_9GQap-NqvQDN10pzka3WRAWGHQ_JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما در دو جنگ جهانی پیروز شدیم، فاشیسم و ​​کمونیسم را شکست دادیم.
🔴
ما باید دوباره این کار را انجام دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/130127" target="_blank">📅 10:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130126">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd225af94c.mp4?token=RwKOaSUQvzvE8xlwXbaUNx2nksgxIBW7Rf2CqXYTyvEfAKPWk0M9sYbcG2CHcGl8uTvAZnWdS8-Z6fZP6WevaTcQouu7HRcyBoG_1fzaqlh4lAoXgrTPNPT-EJ_hP2lbZBBuCvVeiTG_Zbps9eeI7CHmHny8a603huVl4v-xIesjIKgl9xs_yO9NL2VCs_wNE3JwVzZl8k3ZR-DGl_rmJ8tZgdOK5U8Xtp2tTukX2-9ZMK-boE28Ej4GdMTJzZiNhPkBXcKPlnPZN3NEKIAlxYGpfgMFVOu5N0mkpiwjBWppCczJS70jFQwSIlBN8uwqtSrWmjbVTDLT9Y8ZqtNERw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd225af94c.mp4?token=RwKOaSUQvzvE8xlwXbaUNx2nksgxIBW7Rf2CqXYTyvEfAKPWk0M9sYbcG2CHcGl8uTvAZnWdS8-Z6fZP6WevaTcQouu7HRcyBoG_1fzaqlh4lAoXgrTPNPT-EJ_hP2lbZBBuCvVeiTG_Zbps9eeI7CHmHny8a603huVl4v-xIesjIKgl9xs_yO9NL2VCs_wNE3JwVzZl8k3ZR-DGl_rmJ8tZgdOK5U8Xtp2tTukX2-9ZMK-boE28Ej4GdMTJzZiNhPkBXcKPlnPZN3NEKIAlxYGpfgMFVOu5N0mkpiwjBWppCczJS70jFQwSIlBN8uwqtSrWmjbVTDLT9Y8ZqtNERw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما در حال ارائه بزرگترین کاهش قیمت دارو در تاریخ با اختلاف قیمت ۴۰۰، ۵۰۰ و حتی ۶۰۰ درصدی هستیم
🔴
اگر نیم درصد کاهش قیمت را انجام می‌دادید، کسی می‌گفت شما نابغه هستید - ۴۰۰، ۵۰۰، ۶۰۰، ۷۰۰، ۸۰۰ درصد. هیچ‌کس چیزی شبیه به این ندیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/130126" target="_blank">📅 10:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130125">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
کاسبی جدید با محدود شدن تعداد و ظرفیت کارت‌های سوخت آزاد: برخی متصدیان در ازای «شیرینی» کارت جایگاه را در اختیار رانندگان قرار می‌دهند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/130125" target="_blank">📅 10:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130124">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a188028b7e.mp4?token=C2-pmaenlKgJ1gyJ4Q8maf5T1jqwkmRbHwtvZw_sNLyghZscFYQBRREz3j8bVRCLxCb5ip3UjPJARTxY2rswFgXBPmJiAo7P5kLZW0npdS1endaWJvHo-zgrvlJWowuH5zPWomyY9MPUJiDJh2D6z3N2UYEcdNC0QDJnU-9DJ3LLIOBfVeuVFNsx0kTNdQqRdTDpNYxtyyB3VtHayEs76BIWSjIa4yo4z-rSHEGLkSP8FzET5MAgROspFXoQRqF7e2PZfbijnMW_QUoxRvRBx94x8Sf4qCs3m7drxiusozJmoGa-7z-ZdCC8GlYstJ3n6S9v0wZAopGI87BZU4KFFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a188028b7e.mp4?token=C2-pmaenlKgJ1gyJ4Q8maf5T1jqwkmRbHwtvZw_sNLyghZscFYQBRREz3j8bVRCLxCb5ip3UjPJARTxY2rswFgXBPmJiAo7P5kLZW0npdS1endaWJvHo-zgrvlJWowuH5zPWomyY9MPUJiDJh2D6z3N2UYEcdNC0QDJnU-9DJ3LLIOBfVeuVFNsx0kTNdQqRdTDpNYxtyyB3VtHayEs76BIWSjIa4yo4z-rSHEGLkSP8FzET5MAgROspFXoQRqF7e2PZfbijnMW_QUoxRvRBx94x8Sf4qCs3m7drxiusozJmoGa-7z-ZdCC8GlYstJ3n6S9v0wZAopGI87BZU4KFFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آسیب به ساختمان رادیو تلویزیون دولتی ونزوئلا در دو زلزله ۷ ریشتری امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/130124" target="_blank">📅 10:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130123">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
اسکات بسنت وزیر خزانه‌داری آمریکا روز پنج‌شنبه مدعی شد که معافیت از تحریم‌های نفتی ارائه شده به ایران قابل بازپسگیری است‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/130123" target="_blank">📅 10:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130122">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
🔴
جمهوری‌خواهان و ترامپ استدلال کرده بودند، تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/130122" target="_blank">📅 10:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130121">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رئیس‌جمهور موقت ونزوئلا در مورد وقوع دو زلزله پیاپی ۷.۱ و ۷.۵ ریشتری در این کشور:
🔴
کشته شدن دست‌کم ۳۲ تن و زخمی شدن ۷۰۰ نفر
🔴
طبق اعلام رئیس‌جمهور موقت ونزوئلا دلسی رودریگز، دو زلزله پیاپی ۷.۱ و ۷.۵ ریشتری در این کشور، دست‌کم ۳۲ کشته و ۷۰۰ زخمی بر جای گذاشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/130121" target="_blank">📅 10:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130120">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ترامپ درباره ایران: هفته گذشته، ما یک توافق تاریخی برای پایان دادن به درگیری با ایران امضا کردیم، تنگه هرمز را کاملاً باز کردیم و کاری را انجام دادیم که هیچ رئیس‌جمهوری قبلاً نتوانسته بود انجام دهد.
🔴
ایران هرگز سلاح هسته‌ای نخواهد داشت. این موضوع تمام شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/130120" target="_blank">📅 10:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130118">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9dc303a2.mp4?token=atMS5HPfVCLNgJzClvc3p8JGJ5mSPGw5dd0O5TQpm4zRGEt2hK7yNjujWIen8-sfG0bzYFq36cUnp84-RDsro18cis4_1P7W9VmaDvVke_oEAQJsrB6DTAUNh9XSX5xW3Kn4wAE7pkJmjlYEEqq1AI-YYvOxPgBZULI_0yJcBo3-h395CzUi6HE-b3brnxODUiWYNP0vQBVIIkY4F9Cu-yhEyEebCZYqpPnXF20wqTzuQwaO8d7RAL_4oSYgnBVl4WmIlzDO1bU2awYAVBVAcZlL_1fQmQ8mm11jwYf_lRLGUxK8ckp4HYC409zUv-IkAxiDuueMdoEe7g7Fpbq7hCGpz1DG0mVMTxW-4iblUlfLtyRL1JQ1ef0USENY81AHTsWnwiOBHITcZh0GgRncH1pfrP8DNwt8mfO6Uf6Vqb_qeeEHe4LKoB7tA9hM7e1TwTM3fZPL9N9uunclJIHkSa2AnbGvd7HwKy9nT9fV5rvwTYXdXiJ5MtqdbzLRoKAfj8M5UOel7v3d7Q3pfKnNc-RfFEXkqBgMrtIxeihT-8dfsgNfdUiTn05d-1C4qOZJYljHbrUvvz0aC535P5HUeVrJQmacE14RzXonEXrMdCZEOZJbALn_IXKOx0A7_zt6jcVGBMKOA3YkufVg_YqTxR5kq9j17ywp_zPKzDdPM4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9dc303a2.mp4?token=atMS5HPfVCLNgJzClvc3p8JGJ5mSPGw5dd0O5TQpm4zRGEt2hK7yNjujWIen8-sfG0bzYFq36cUnp84-RDsro18cis4_1P7W9VmaDvVke_oEAQJsrB6DTAUNh9XSX5xW3Kn4wAE7pkJmjlYEEqq1AI-YYvOxPgBZULI_0yJcBo3-h395CzUi6HE-b3brnxODUiWYNP0vQBVIIkY4F9Cu-yhEyEebCZYqpPnXF20wqTzuQwaO8d7RAL_4oSYgnBVl4WmIlzDO1bU2awYAVBVAcZlL_1fQmQ8mm11jwYf_lRLGUxK8ckp4HYC409zUv-IkAxiDuueMdoEe7g7Fpbq7hCGpz1DG0mVMTxW-4iblUlfLtyRL1JQ1ef0USENY81AHTsWnwiOBHITcZh0GgRncH1pfrP8DNwt8mfO6Uf6Vqb_qeeEHe4LKoB7tA9hM7e1TwTM3fZPL9N9uunclJIHkSa2AnbGvd7HwKy9nT9fV5rvwTYXdXiJ5MtqdbzLRoKAfj8M5UOel7v3d7Q3pfKnNc-RfFEXkqBgMrtIxeihT-8dfsgNfdUiTn05d-1C4qOZJYljHbrUvvz0aC535P5HUeVrJQmacE14RzXonEXrMdCZEOZJbALn_IXKOx0A7_zt6jcVGBMKOA3YkufVg_YqTxR5kq9j17ywp_zPKzDdPM4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حداقل ۳۲ کشته و صدها زخمی در زلزله‌های ونزوئلا
🔴
طبق اعلام رئیس‌جمهور موقت ونزوئلا، ۲ زلزلهٔ پیاپی ۷.۱ و ۷.۵ ریشتری در این کشور، دست‌کم ۳۲ کشته و ۷۰۰ زخمی به‌جا گذاشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/130118" target="_blank">📅 09:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130116">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c90021fcf.mp4?token=p8SPZvgkHbJ5DTCewxUiSEyynpE0CaPv65yspBLWc71dBL9TGcyw9Ns_wzO_esPTDYHaSRYDK7wK16pbhgIK0xEmVmisKGMM9ylBbTGo2zQZ108N9Qc_OUF1RE93qdJ8fD5Jb8B6wrok6rLAA2sMT4LeswGQEl9kuJrgX660uvbadkFe7FlhlBEeZ9RZbHl-sTkq1y0W0aeajjZcdUrQbpo9LKlT07yaEIk4ahJDW0qYhq06k-7Ss8VIfPiP-v1g7YPjWQMKY1pUknlj5WtMZeAqrBuO9W5mWO5Avc-d92TKEqhJPwiV4NFaduvDb78j-lisyJF9bvJANbOBJB1BfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c90021fcf.mp4?token=p8SPZvgkHbJ5DTCewxUiSEyynpE0CaPv65yspBLWc71dBL9TGcyw9Ns_wzO_esPTDYHaSRYDK7wK16pbhgIK0xEmVmisKGMM9ylBbTGo2zQZ108N9Qc_OUF1RE93qdJ8fD5Jb8B6wrok6rLAA2sMT4LeswGQEl9kuJrgX660uvbadkFe7FlhlBEeZ9RZbHl-sTkq1y0W0aeajjZcdUrQbpo9LKlT07yaEIk4ahJDW0qYhq06k-7Ss8VIfPiP-v1g7YPjWQMKY1pUknlj5WtMZeAqrBuO9W5mWO5Avc-d92TKEqhJPwiV4NFaduvDb78j-lisyJF9bvJANbOBJB1BfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت کاراکاس پس از زمین لرزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/130116" target="_blank">📅 09:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130115">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l47ulkMvztclfhZbJt8KOhc8WkXUB-BddYs8IGljllBj6cDOqMDl9AFL7WejKGmxO8ayhIdOGKuYIFg_jcOI41nm0U_PbAfkKzMwI9vRJECpC3nJe5uHswE-0K3AtmZNrDBtKf8MrEg15z3PBG_igB52gHplizL6_-szCOktAEdT7m8B7HZ0pL1T-8wSQcUwOKeT94zYDS6BV-WkN92PYhZxl-ssw4M2stSQ4uXDOE5Fna86-_fohgzFPsIgTJZIklcKuAzPIJwxsLRHphk-jI7wj3gHZKd9nSIRawSYdjIjzLUqUOs_McIm2qHN-H0ir5UsMKoPXklv6-BfEp1qPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارکو روبیو
:
آمریکا در این دوران سخت در کنار مردم ونزوئلا ایستاده است
و به دستور رئیس جمهور ترامپ، وزارت امور خارجه بلافاصله تیم‌های جستجو و نجات، منابع پزشکی و کمک‌های بشردوستانه را به ونزوئلا اعزام می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/130115" target="_blank">📅 09:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130114">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ta-o0yBGPlLyosRkAbIQerHdgIc0TYIh7xYncSBY9aPsPjuOONbapSWNP_OZGwOF0BwKfZTQvaU3CBs6_4AoManyQY5tm_l6CNu_-GL3dlE_HqgVwC5WoUO4s42amIyNaWHE5SAXuEge95Ou-xgDQvnazXVby3fuoip6euRpI7K_8qs7lp3P9NrqjnbWg5g-VdzETrCf0_dKEMKFp_t9xqjxLwPbpvdRpuuqsG1W-NXLCcUDRvJGq5syx5Wod4-vk5GTLFiXfwD9_kgIQZRXHDTWxH1fuL-TxYziFFUUXz2E4m5aGqJiYKMxQ60BhsmMUEcYvD6_LQKW0eGqwkUuNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور: نه ظلم کنیم، نه ظلم بپذیریم و نه مقابلش سکوت کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/130114" target="_blank">📅 09:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130113">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUcpLkxASYM0OLiPHXYnjMLKN_bcQs5YiRs93xy4_q9hVVPwms-Q2W-K8gpC2xMvX5Gp3yf0GdcLirFDtXE3yHcqxPiYTb_a3Iyfa-Ca9--cC7PQfIEbdncgvVWUP_bp4hp3YyGV__aMv_Bg5Lpx2lBkE1dCi-XNajVx4G8YeckeeN98_vpOWsoCL_nG1zZwMEh5sujpAT3OkzXuEIlkUxhT7AWilKcH7JCqgejiVVtInN8P8xU-zVC8wVtECpuQpocTZUS3wy8fsfVthB8sBsW-8hWOkLnMkT3l-LM4ZZsYJnpSdBx5sdlQIwZ-SatuEKzytSgUbpjKhDaxOMXJiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: دو زلزله بزرگ که به تازگی مردم بزرگ ونزوئلا را لرزاندند، هر دو در مقیاس وسیع بوده و تعداد زیادی کشته به جا گذاشته‌اند. ایالات متحده آماده، مایل و قادر به کمک است! من به تمام نهادهای دولتی دستور داده‌ام که برای اقدام سریع آماده باشند. ما در کنار دوستان جدید و بزرگ خود خواهیم بود. گزارش‌های اولیه خوب نیستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/130113" target="_blank">📅 09:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130112">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzJKMGyoV2NjOpGI3iFvfPDqP2VxnLNnz06jbyAYHbG4t5Dud4WeoqFF-w9nbMxCIGlxKpbLOA7yVZzpiVlMqW6ZqthqWCRuk9DJ2O1QLKe6pvLd3H0eoHb-ym-kzszHlfuqdCXRHy0bdsx18Pl1Wjkn_B1yEq9TEpZahR-9LFeQLFtidYOuAwUHKjRi8LFNALDEKRXlV7od4NTuqeHPLtd5zibbB3MqNCXAC3VR6WYXrgStU8JHVIXhVU202KQboeArQjKyF4JIQGmHPSjr309uvN5AAbRgzFiTHTaRQ_4eLGVwmmzz7ybcJn1Tf8VlccSyhhNOV3rGyeaP4ubFrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت تنها ۲ دلار با قیمت خود پیش از آغاز جنگ فاصله دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/130112" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130111">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
دولت ترامپ از کنگره ۸۷٫۶ میلیارد دلار برای جبران فرسایش منابع ناشی از جنگ با ایران درخواست کرد
🔴
شبکه آمریکایی سی‌ان‌ان به نقل از نامه‌ای که به دست آورده است گزارش داد که دولت ترامپ درخواست بودجه تکمیلی به ارزش ۸۷٫۶ میلیارد دلار از کنگره کرده است.
🔴
هدف از این بودجه، جایگزینی منابعی است که در نتیجه جنگ با ایران مصرف شده‌اند و همچنین تکمیل پروژه‌های بازسازی در پایتخت آمریکا، واشنگتن، عنوان شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/alonews/130111" target="_blank">📅 08:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130110">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a33b09c4.mp4?token=jL3QVZW1T_Wn30M_XI0J2PMT4sZqMJ2pxH0w7GdNPbRMIUJs4StkWX0FAexRRer8-mbiHfQwhJzU3kgfdvCWQC462VvCMChMsa1_YMwuVWI3FCxmYW7IfrQatM9BwG9lPOelJNKn8Om4B9cD0u66YPpD0eiU95rzV0r9pNHId4NahPVG59IcNbzauw4Y23iOGX7zgywQTcXSEhVM-qgmnOR4UltOOufy74BmUN8a4Apzbdb2VAsY6z9T5QymuZDq3N_N87KYGLnnigbUchE3I2hat3onj9484l3RUOvCWYJc9GEeGZizXeOmLVELMrmq2o19bkoTVfuUOXfUp6vtrTBoojxcI9E8BYL8o7CfTF48I9GG98rsEZQwhaHkz9XQQiOcpiMtVFN563hli5mcz3YTNe29Eyh5qQh9S8EJazAjYKpcCIKTcplwxIDTSqZud8xqpf6bXVoXZr24v0ZKvaHnghlNr7lRFc6KEx5dx9uZQznpuyEnZaVTPiQqw_bMdc2Eon-fGKtipuMYfLOeD9ljvqQVxb3j1wTq-ka7my2w4821Wfu5vRmZN3rQjfXWlHXf79AD8V4bidjDPq7-k30m6FL-hHF8eAkOwluAS91WymKJLGF1BlT7cNDW6brCCx07Zd23n9PXXpA3FW-DJ-XdmUAe-BhN2xy3KJc6zgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a33b09c4.mp4?token=jL3QVZW1T_Wn30M_XI0J2PMT4sZqMJ2pxH0w7GdNPbRMIUJs4StkWX0FAexRRer8-mbiHfQwhJzU3kgfdvCWQC462VvCMChMsa1_YMwuVWI3FCxmYW7IfrQatM9BwG9lPOelJNKn8Om4B9cD0u66YPpD0eiU95rzV0r9pNHId4NahPVG59IcNbzauw4Y23iOGX7zgywQTcXSEhVM-qgmnOR4UltOOufy74BmUN8a4Apzbdb2VAsY6z9T5QymuZDq3N_N87KYGLnnigbUchE3I2hat3onj9484l3RUOvCWYJc9GEeGZizXeOmLVELMrmq2o19bkoTVfuUOXfUp6vtrTBoojxcI9E8BYL8o7CfTF48I9GG98rsEZQwhaHkz9XQQiOcpiMtVFN563hli5mcz3YTNe29Eyh5qQh9S8EJazAjYKpcCIKTcplwxIDTSqZud8xqpf6bXVoXZr24v0ZKvaHnghlNr7lRFc6KEx5dx9uZQznpuyEnZaVTPiQqw_bMdc2Eon-fGKtipuMYfLOeD9ljvqQVxb3j1wTq-ka7my2w4821Wfu5vRmZN3rQjfXWlHXf79AD8V4bidjDPq7-k30m6FL-hHF8eAkOwluAS91WymKJLGF1BlT7cNDW6brCCx07Zd23n9PXXpA3FW-DJ-XdmUAe-BhN2xy3KJc6zgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زمین‌لرزه‌ای شدید به بزرگی ۷.۱ بعدازظهر چهارشنبه در غرب کاراکاس، پایتخت ونزوئلا، رخ داد و لرزش آن در کلمبیا نیز احساس شد. ساکنان کاراکاس به خیابان‌ها گریختند و گزارش‌ها از خسارت به ساختمان‌ها و اختلال در برق و اینترنت حکایت دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/130110" target="_blank">📅 08:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130109">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ: بعد از 3000سال من صلح رو به خاورمیانه آوردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/alonews/130109" target="_blank">📅 06:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130108">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ: قیمت‌های نفت به شدت کاهش یافته‌اند، اما ما در پمپ‌ها چیزی متناسب با آنچه باید باشد، نمی‌بینیم. به نظر من، قیمت باید در حال حاضر ۲.۲۵ دلار در پمپ باشد، اما ما بالاتر از آن هستیم. ما در حال انجام یک تحقیق بزرگ در این مورد هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/130108" target="_blank">📅 01:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130107">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ:خیلی وقت ها وقتی با اردوغان مشکل دارند می گویند می توانی به من لطف کنی و با او صحبت کنی؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/130107" target="_blank">📅 01:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130106">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ترامپ درباره زهران ممدانی: ممدانی دو بار اینجا بود. او مرد بسیار خوبی است. او مردی جذاب و خوش‌تیپ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/130106" target="_blank">📅 01:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130105">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ: کشورهای ناتو خوش‌شانس هستند که روته را دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/130105" target="_blank">📅 01:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130104">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237a076aa9.mp4?token=vRvNl68wDmBDAzH-sGjZIaV7aXO8ZqsVURk25uaX-i31ZeOP4-YrYZn-vo7JRXsXMFsaDolMPMzorRgdqS_E5heoEduVLYk3u2DV2QGmbAPM2QWj_cKwe-ZiBRPXll-ErWR0c9OaN1eRes0pCeDQORlK1iR8HWu193FX5AMTvUW2WBC5FY0tdHRsZiMF9ONhLZhcYezKUhZ0Ub-LUS82-N4e2R0TpLyH4avaZPswXwabxbQiwNxljEDQtz2viEZBWkchLc580sSPbJ2zyh_unJ8LIgjV65CaVqgWtNCYdO7_MlNKoBR06UHO4f1cHaSAYup1YHuWQsPQ1v5aiG-utg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237a076aa9.mp4?token=vRvNl68wDmBDAzH-sGjZIaV7aXO8ZqsVURk25uaX-i31ZeOP4-YrYZn-vo7JRXsXMFsaDolMPMzorRgdqS_E5heoEduVLYk3u2DV2QGmbAPM2QWj_cKwe-ZiBRPXll-ErWR0c9OaN1eRes0pCeDQORlK1iR8HWu193FX5AMTvUW2WBC5FY0tdHRsZiMF9ONhLZhcYezKUhZ0Ub-LUS82-N4e2R0TpLyH4avaZPswXwabxbQiwNxljEDQtz2viEZBWkchLc580sSPbJ2zyh_unJ8LIgjV65CaVqgWtNCYdO7_MlNKoBR06UHO4f1cHaSAYup1YHuWQsPQ1v5aiG-utg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا می‌خواهید اولین فردی باشید که در لیست نخست‌وزیر جدید بریتانیا برای بازدید قرار می‌گیرد؟
🔴
ترامپ: خیر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/130104" target="_blank">📅 01:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130103">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ: درست در میان یکی از موارد کلیدی: «ما اخبار فوری داریم. سنا رای داده که می‌خواهند ترامپ جنگ را متوقف کند.» ایران این را می‌بیند و می‌گوید: «این همه ماجرا چیست؟»
🔴
من احتمالاً کاری انجام خواهم داد که اردوغان را بسیار خوشحال کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/130103" target="_blank">📅 01:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130102">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4db3d1db8.mp4?token=sUjtczzYivZzmlECHNemVzeS-3h6w_tlf4wcG1aKv8Z7NGW7DdWKMmJDD3MAfYCzQCe6eWSRt0hNLxrbLQ6Ndh4cuKjX5AZgAC-O9eAVDTYPh_RhYzTPlLJ1oZwYcQjocw6EHyV7JosbrWqrac6dumevoWWIQINytz6y-IJfv74VrTjhy1k4Y4mnEIF3jPnBPNV5p5bsL9n1njdBXqFEKyZ95Sh-I7eGqo0Hi_Dedi6YEb897VvcdWROZTqwvNjS-AFOcVTdQgoRQrBGQnMRXzssHaF49WxJLSR2GU6IRvMt7FtGRIl9GD5iRS1vL19oVzGiJ792mdlhRavG79j-hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4db3d1db8.mp4?token=sUjtczzYivZzmlECHNemVzeS-3h6w_tlf4wcG1aKv8Z7NGW7DdWKMmJDD3MAfYCzQCe6eWSRt0hNLxrbLQ6Ndh4cuKjX5AZgAC-O9eAVDTYPh_RhYzTPlLJ1oZwYcQjocw6EHyV7JosbrWqrac6dumevoWWIQINytz6y-IJfv74VrTjhy1k4Y4mnEIF3jPnBPNV5p5bsL9n1njdBXqFEKyZ95Sh-I7eGqo0Hi_Dedi6YEb897VvcdWROZTqwvNjS-AFOcVTdQgoRQrBGQnMRXzssHaF49WxJLSR2GU6IRvMt7FtGRIl9GD5iRS1vL19oVzGiJ792mdlhRavG79j-hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا اگر یک توافق نهایی با ایران شامل هر نوع هزینه‌ای برای حمل و نقل باشد، آن را می‌پذیرید؟
🔴
ترامپ: خیر. برای من غیرقابل قبول خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/130102" target="_blank">📅 01:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130101">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e8734849.mp4?token=kQD9n0nwoxNgTTnK8stDCBKA-WYsCeSdQwF-N5WED1AHOVyRnYJGbRR95Q2mNPijCM7y5qUEWtxPfrogv3UsZSZ1a2ngy0IorObcd9MXgOAdbCrWjfukG8Xzl7MMTY5TiD2co8In9D1ElUAW76oGUAJ1w-Z_SbC2cmUxzUA_j9TbVukFLVllraw55cMbUrf50zEavtRNfPCif-XYI1Tx0Q32amscqQG1dTqBhlKV9IacjgesSJC5DbX8wZckGmUMQYEXTRdUg97d_Hp0fAeJKfwzx1nVasHlrLpujUmeeHJAJEzBDFUiTO9mCsG3CiGXjwK64BATfHbHaSVyXZ_yaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e8734849.mp4?token=kQD9n0nwoxNgTTnK8stDCBKA-WYsCeSdQwF-N5WED1AHOVyRnYJGbRR95Q2mNPijCM7y5qUEWtxPfrogv3UsZSZ1a2ngy0IorObcd9MXgOAdbCrWjfukG8Xzl7MMTY5TiD2co8In9D1ElUAW76oGUAJ1w-Z_SbC2cmUxzUA_j9TbVukFLVllraw55cMbUrf50zEavtRNfPCif-XYI1Tx0Q32amscqQG1dTqBhlKV9IacjgesSJC5DbX8wZckGmUMQYEXTRdUg97d_Hp0fAeJKfwzx1nVasHlrLpujUmeeHJAJEzBDFUiTO9mCsG3CiGXjwK64BATfHbHaSVyXZ_yaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا فکر می‌کنید زلنسکی در حال حاضر برنده است؟
🔴
ترامپ: خب، او کارش را نسبتاً خوب انجام می‌دهد. ببینید، هرطور که به آن نگاه کنید، او کارش را نسبتاً خوب انجام می‌دهد.
🔴
او حداقل از پس کارش برمی‌آید - بسیاری از مردم در هر دو طرف می‌میرند. اما فکر می‌کنم او کارش را نسبتاً خوب انجام می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130101" target="_blank">📅 00:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130100">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ درباره ترکیه: مردم نمی‌دانند که ترکیه از نظر نظامی چقدر بزرگ است
🔴
ارتش بسیار قدرتمندی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/130100" target="_blank">📅 00:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130099">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff1dea6d4d.mp4?token=YRx5_JnQGeZL68yJ7WOKDvOaxu3t_kO1sJdd8MiNK0-jM5tQN7dJdXJc_BRQhcVXN9YlBlEQZuq6JedCrwk7goREMsY9xQRE6iwKwA_zRRoqeQPrOzZuK-oU6WOQXEUCcSedut6C42uxw7oOKFFdhfP8Wn7fw-M9lp9xlLY3khWiyYX_FXjIhgrVKkfYekF5-gdtwt2xCWgjiEhK2YYczrsYPlyWEyyJWDei3k1mKavvtz4l_erYXFoeiFkSXG5koWIsw0lVfwToxvuRneYpz2WghLqbFHydr1JJtATum4VWzLrfl4QCm1SznduxwT07vytkIImF90RF5RcVr42zFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff1dea6d4d.mp4?token=YRx5_JnQGeZL68yJ7WOKDvOaxu3t_kO1sJdd8MiNK0-jM5tQN7dJdXJc_BRQhcVXN9YlBlEQZuq6JedCrwk7goREMsY9xQRE6iwKwA_zRRoqeQPrOzZuK-oU6WOQXEUCcSedut6C42uxw7oOKFFdhfP8Wn7fw-M9lp9xlLY3khWiyYX_FXjIhgrVKkfYekF5-gdtwt2xCWgjiEhK2YYczrsYPlyWEyyJWDei3k1mKavvtz4l_erYXFoeiFkSXG5koWIsw0lVfwToxvuRneYpz2WghLqbFHydr1JJtATum4VWzLrfl4QCm1SznduxwT07vytkIImF90RF5RcVr42zFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ: شهردار لندن ناکارآمد است، یک فرد بد و نماینده‌ای فاجعه‌بار برای کشور شما.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/130099" target="_blank">📅 00:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130098">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ترامپ درباره ترکیه: مردم نمی‌دانند که ترکیه از نظر نظامی چقدر بزرگ است.
🔴
ارتش بسیار قدرتمندی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/130098" target="_blank">📅 00:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130097">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9afbb8ef64.mp4?token=jXy4kK5xG7Fo8gm8o5EOvviBBNFg5TDFhDlW9l9IvgPD9r8-N5TEvWDPqd_AgYHG5DfLdvryNf1igZveAoMRMcwxOEGbTcXfdn7y0EfQeBTxkebt9x8zDZ1TSWIl_3s2EDAh-ITw1As7BQnWOG9F1IB7-2cB7_p27gQ1Rlr7kqt_3hc5lxFnG7c_ljdjtwSdz3IYvbCgWzsWPx_25Aev5KYnB0Btx8IzDeO0GoaN5DzUZMATYwAM5olY2g1-j1KMnh2YP4ymBRGlnQ_IeEZRC4Qmz4NXmZZsodo_9CnL4qIfMlloaorCwWWYJASBH-SUWQNfO6QSpV46-tnL7LnCC19HVQWe6DjjVQ-I03CWhNiH3dDyGEM0GCzGrW5WEbwSmrc-6e_3HcSgs9MeIQb7yhuH4tEzb2Sbo-INyZOwpSuTfYHeH0qoZyDfUg3UaGc_c8SqDehJ1RSj_t4W8J4Iad_P850d7S2mcqRbaECcJBXFUhGwp2wOdgnU_vzPEHvgCq2GvAkQXgUK5NdBUS2DAA5YifZiHOiM-Qc3TDr2srHwu6m-1VzMxKFTUCv7b6Wo3q8VzkbngJwD1JEGCnuEUcBFd38qHA_qPjyZ1mZZ4NIxn8MJ7VWMXFZv7B6A40YrKwUr2kfFXWhKmlryTpJmiEjHiPyVQT3OH_hlxoVFsUc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9afbb8ef64.mp4?token=jXy4kK5xG7Fo8gm8o5EOvviBBNFg5TDFhDlW9l9IvgPD9r8-N5TEvWDPqd_AgYHG5DfLdvryNf1igZveAoMRMcwxOEGbTcXfdn7y0EfQeBTxkebt9x8zDZ1TSWIl_3s2EDAh-ITw1As7BQnWOG9F1IB7-2cB7_p27gQ1Rlr7kqt_3hc5lxFnG7c_ljdjtwSdz3IYvbCgWzsWPx_25Aev5KYnB0Btx8IzDeO0GoaN5DzUZMATYwAM5olY2g1-j1KMnh2YP4ymBRGlnQ_IeEZRC4Qmz4NXmZZsodo_9CnL4qIfMlloaorCwWWYJASBH-SUWQNfO6QSpV46-tnL7LnCC19HVQWe6DjjVQ-I03CWhNiH3dDyGEM0GCzGrW5WEbwSmrc-6e_3HcSgs9MeIQb7yhuH4tEzb2Sbo-INyZOwpSuTfYHeH0qoZyDfUg3UaGc_c8SqDehJ1RSj_t4W8J4Iad_P850d7S2mcqRbaECcJBXFUhGwp2wOdgnU_vzPEHvgCq2GvAkQXgUK5NdBUS2DAA5YifZiHOiM-Qc3TDr2srHwu6m-1VzMxKFTUCv7b6Wo3q8VzkbngJwD1JEGCnuEUcBFd38qHA_qPjyZ1mZZ4NIxn8MJ7VWMXFZv7B6A40YrKwUr2kfFXWhKmlryTpJmiEjHiPyVQT3OH_hlxoVFsUc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: ترکیه موتورهای جت F-110 را می‌خواهد و همچنین جنگنده‌های F-35 خود را. آیا با یک کیسه هدیه بزرگ به ترکیه می‌روید؟
🔴
ترامپ: فکر می‌کنم بله. او عضو ناتو است. برخی افراد او را به عنوان عضو نمی‌دانند، اما واقعاً عضو است. او عضو قدرتمندی در ناتو است. بله، احتمالاً کاری انجام خواهم داد که او را بسیار خوشحال کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/130097" target="_blank">📅 00:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130096">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39188d729e.mp4?token=AuqCJCQ4W6F6NbaFO9nz0nA5FQxWllM6EFXX8KKt-_Nc8FC3C_sVsqVC9gnukwwxNZkq3m_M2xHg-HHvztTpBt_wZEuKojJExDfIuHwRyBd3hW9oq2qBUav9vj-1_85O1inTRwlwlJvdkqhCxtSpUiZD09h2ke6ZNoXVtb5TR6Ez2vUOEcK0K0y8PYj6_UFmSQsCrtxfxDeI7FIk-S2wbHLYQJSvQDQq1If5sSbIcPmKkMohF5quVoXuQGGxOMO2kottebSSGeejr85sUfVDo9lnCgLTHB1Xqc740B88JcYWfvvpAz63xRI_RtzeO_ljP7E9liHRaw9Tjly90l2rFhRGSWARn6KTv_bXQqQ_sRuUrTskpWBQZ1xswyNn2ZW0ry5GlkpeYedBVk9vJLN2PMcA1WR2NSlIfJAc7iY5lMccb3jNTTjG-GsHzraaSbNAwYaMp0NY3Xraa7Fz4rLVWv1Mt2PcD2RCeJ3h-thj9gOvj0EXShUssuoXgSSrUkhOPOQkHSOMHTCrWtAIQ8cZ6iVNBYN5e-MXkO1ZcB-lhn9YJalRoFBVoGei8kr15wuW-S8RFgTR5TgY7W-D2FYR2uPKHegWBFSTsb4jNumGMfQklz4j2wxwTH5JqqE2FGUqBXYee0xMlBn13waM8zfKUwb5YdSXrrQgSZwpKoJn53w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39188d729e.mp4?token=AuqCJCQ4W6F6NbaFO9nz0nA5FQxWllM6EFXX8KKt-_Nc8FC3C_sVsqVC9gnukwwxNZkq3m_M2xHg-HHvztTpBt_wZEuKojJExDfIuHwRyBd3hW9oq2qBUav9vj-1_85O1inTRwlwlJvdkqhCxtSpUiZD09h2ke6ZNoXVtb5TR6Ez2vUOEcK0K0y8PYj6_UFmSQsCrtxfxDeI7FIk-S2wbHLYQJSvQDQq1If5sSbIcPmKkMohF5quVoXuQGGxOMO2kottebSSGeejr85sUfVDo9lnCgLTHB1Xqc740B88JcYWfvvpAz63xRI_RtzeO_ljP7E9liHRaw9Tjly90l2rFhRGSWARn6KTv_bXQqQ_sRuUrTskpWBQZ1xswyNn2ZW0ry5GlkpeYedBVk9vJLN2PMcA1WR2NSlIfJAc7iY5lMccb3jNTTjG-GsHzraaSbNAwYaMp0NY3Xraa7Fz4rLVWv1Mt2PcD2RCeJ3h-thj9gOvj0EXShUssuoXgSSrUkhOPOQkHSOMHTCrWtAIQ8cZ6iVNBYN5e-MXkO1ZcB-lhn9YJalRoFBVoGei8kr15wuW-S8RFgTR5TgY7W-D2FYR2uPKHegWBFSTsb4jNumGMfQklz4j2wxwTH5JqqE2FGUqBXYee0xMlBn13waM8zfKUwb5YdSXrrQgSZwpKoJn53w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ: آن‌ها توافق کردند که ۵ درصد هزینه کنند، و آن‌ها آن را پرداخت نمی‌کنند.
🔴
روته: شما نمی‌توانید آن را در یک سال هزینه کنید.
🔴
ترامپ: تو میتونی. تو میتونی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/130096" target="_blank">📅 00:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130095">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ: بریتانیا در حال مردن است. باید دریای شمال را باز کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/130095" target="_blank">📅 00:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130094">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ : تو مذاکرات، پیشرفت‌های خوبی به دست اومد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/130094" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130093">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ درباره اردوغان، ترکیه : خب، من باهاش رفیقم و ازش خوشم میاد
🔴
توی جنگ هم قاطی نشد می‌دونید، اردوغان یکی از محتمل‌ترین آدم‌ها بود که می‌تونست وارد جنگ با ایران بشه
🔴
حتی شاید سمت ایران رو بگیره، چون همون‌طور که می‌دونید خیلی دلِ خوشی از اسرائیل نداره. من ازش خواستم وارد ماجرا نشه و اونم قبول کرد
🔴
یه نفر دیگه هم که خیلی خوب رفتار کرد رئیس‌جمهور چین بود
🔴
اونم می‌تونست وارد قضیه بشه؛ بالاخره کلی از نفتش رو از اون منطقه تأمین می‌کنه
🔴
کاملاً قابل تصور بود که بخواد دخالت کنه، ولی ازش خواستم وارد نشه و اونم وارد نشد
🔴
خلاصه، کارمون رو خوب جمع کردیم. اون هم کنار کشید. اردوغان آدم فوق‌العاده‌ایه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/130093" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130092">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
خبرنگار : گزارش حمله به مدرسه دخترانه در ایران رو دیدید؟
🔴
ترامپ : نه، ندیدم
🔴
خبرنگار : چرا نه؟
🔴
ترامپ : باید صبر کنم گزارش کامل بشه
راستش نمی‌دونم اصلاً هیچ‌وقت بتونن این موضوع رو حل کنن یا نه. می‌تونی از پیت بپرسی. شاید اصلاً کار موشک ما نبوده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130092" target="_blank">📅 00:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130091">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ: هیچ حمایتی از سوی اروپا در رابطه با جنگ ایران دریافت نکرده‌ام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130091" target="_blank">📅 23:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130090">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
از ناوشکن هسته‌ای کره شمالی رونمایی شد
🔴
رسانه‌های دولتی کره شمالی گزارش دادند کیم جونگ اون اعلام کرده است نیروی دریایی این کشور به سلاح هسته‌ای مجهز می‌شود و کشتی چوئه هیون رسماً وارد خدمت شده است.
🔴
این ناوشکن ۵۰۰۰ تنی به سلاح‌های ضد هوایی و ضد کشتی مجهز است و قابلیت حمل موشک‌های کروز و بالستیک با توان حمل کلاهک هسته‌ای را دارد.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/130090" target="_blank">📅 23:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130089">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e98be8e64b.mp4?token=KYFez1R1nHe-y6d_wzsB_xMzE7HkVz1ToTh5gZZLuvi4vYcWr4DtcYQIkL0f_nx4Rl4QPg2nCcPttNjXy8oeM2aF9t3PYdy8LKeVX4IVSbyL4EI3dpgOr0uSQsYsohw6iyG5JwAx8GZj2-UA4Hw_xWEC463ys-rNcZg5ztnc7_Hxu4hARx50V9ElUExLLRBWqVNkUiLGeDREz2udXfjclpoerhl-wi10BSO3r6cbD_6oYx7FYMb_7LM5iiuLqabjpVAGn0altW5UyZ3vkZYwMtPBAfCMKI82THO7qFKP6QNjtknZ6Q06F77cIlQwALdaoFcV8XipKoD35bC07kulUR-6BUVGmp1zE1ZG0vsl_2zChKdIw_dZqRtbDxUzlh4_nSzk3VcHaYwxFRLO8N__fbnR5iEyHGwVgexQUQQGuwSNTGOrTuuN7Ge-cYEDfsog1vd7tIdlwnhsfrz3eWeL9fep5_ULd6fDbIOT29lEyXqgN7G6DMFrcPvbio4srq4ezna1qBNrGWCNrwBX9mTOn65jYegbaaPfJyVyGqX0WycdOLuhdGno8aTLT_cxZ2HdqlX41pn037UDle7a1RVYgkftqyeeXC3zailOZd87xIMm-iMS_4MNxvNKIYHyiToCJc_svIyyPjEX26p8s3D8WGgLnWyIPY8qOxUEE-IRmy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e98be8e64b.mp4?token=KYFez1R1nHe-y6d_wzsB_xMzE7HkVz1ToTh5gZZLuvi4vYcWr4DtcYQIkL0f_nx4Rl4QPg2nCcPttNjXy8oeM2aF9t3PYdy8LKeVX4IVSbyL4EI3dpgOr0uSQsYsohw6iyG5JwAx8GZj2-UA4Hw_xWEC463ys-rNcZg5ztnc7_Hxu4hARx50V9ElUExLLRBWqVNkUiLGeDREz2udXfjclpoerhl-wi10BSO3r6cbD_6oYx7FYMb_7LM5iiuLqabjpVAGn0altW5UyZ3vkZYwMtPBAfCMKI82THO7qFKP6QNjtknZ6Q06F77cIlQwALdaoFcV8XipKoD35bC07kulUR-6BUVGmp1zE1ZG0vsl_2zChKdIw_dZqRtbDxUzlh4_nSzk3VcHaYwxFRLO8N__fbnR5iEyHGwVgexQUQQGuwSNTGOrTuuN7Ge-cYEDfsog1vd7tIdlwnhsfrz3eWeL9fep5_ULd6fDbIOT29lEyXqgN7G6DMFrcPvbio4srq4ezna1qBNrGWCNrwBX9mTOn65jYegbaaPfJyVyGqX0WycdOLuhdGno8aTLT_cxZ2HdqlX41pn037UDle7a1RVYgkftqyeeXC3zailOZd87xIMm-iMS_4MNxvNKIYHyiToCJc_svIyyPjEX26p8s3D8WGgLnWyIPY8qOxUEE-IRmy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره دبیرکل ناتو روته:
او در سراسر جهان مورد احترام است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/130089" target="_blank">📅 23:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130088">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
نماینده آمریکا در سازمان ملل: پول آزاده شده ایران صرف خرید محصولات کشاورزی اضافی آمریکا می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/130088" target="_blank">📅 23:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130087">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9wL0-i3SjYh-XKJOtM3QrP5ILFClxgsH0e9DFmw081_FOPdek9W7wUK3MVbTgh_w1OgRqYu2TgKC5YanBD15aqsFBlaFqYjgphE4_vRauHFESnWP4Fr1V6arzln3zNcFxjE_XLU3-62i0YibSws_gHyHeddOyGMUt7NF4NzWyqiC3oj_kT_w1BhcEcHdNxPnaVWLwBMLyIG1R7j5EO-2IKgmkfMSoe-u0noI4EfyTGPXALzvOCt57bF0PcrKRZH69sfZjRE8jPW0A9oMRPoaJuYxkg_dVqCS4JLrg8kyfWRRx22hzegQcr3QlyDwblmfxqPC6jjCAFzng12q6SVwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: اظهارات متناقض آمریکا درباره یادداشت تفاهم برای پایان جنگ به کاهش بی‌اعتمادی ایرانیان کمک نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/130087" target="_blank">📅 23:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130086">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
نیویورک تایمز: سبک ترامپ این است که نتایج مطلوب خود را به‌عنوان توافقات فرعیِ کاملاً مذاکره‌شده توصیف کند، به این امید که ایران را به هر بخش از توافق متعهد کند
🔴
ایران این موضوع را دریافته‌ و استراتژی رسانه‌ای خود را دارد؛ اظهارات آمریکا را تکذیب می‌کند تا در تنگنا قرار نگیرد
🔴
هم واشنگتن و هم تهران درگیر یک نبرد رسانه‌ای برای شکل‌دهی به روایت و پیشبرد نتیجهٔ مطلوب خود در مورد عناصر خاصی از مذاکرات هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/130086" target="_blank">📅 23:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130085">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
پزشکیان: امروز هم در سران قوا، هم در شورای امنیت و هم در مجموعه سیستم یک نگاه مشترک داریم
🔴
اگر دستاوردی داریم دستاورد این مجموعه، رهبر بزرگ و مردم عزیز است.
🔴
امروز ایران را در منطقه به عنوان یک قدرت می‌بینند
🔴
فکر می‌کردند کار جمهوری اسلامی سه روزه تمام است و مثل سوریه یک شخصی از خودشان را سر کار می‌آورند.
🔴
سپاهیان و ارتشیان ما با جان فشانی کاری کارستان کردند.
🔴
من نمی‌توانم مسئول مملکتی باشم که مملکت شیعه و علی باشد و یک عده بیکار باشند و گرسنه باشند. خدا از من نخواهد گذشت، از دولت نخواهد گذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/130085" target="_blank">📅 23:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130084">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9TfnyoYI63UbTGAp0ialz2jwzTQolJ_-rKEb8DvlXzuf7fz1kE-jn9NL4B4UkjB0eQO46SMfUBInlCUOklxvM4l6zWhB1enG5E4DjtM4GbBS7EmYNyonfyyKvzGpkgnsp5CJ9oUuSAQ8siuRsmd7lm40YPLIJ-cdtj2MlohpG24hqnUk0UyO79QPQ07gVWkCSYo0DCXN6DgTflXX63VHW1VShyRGF6P_EIt0wKdahOGzMYcgVKEFFjTjv2ZSpvOhIgnc2h3Z5JSejOwx3NWwsRcHDPhD6lY6tlJP24JFiY187zRnzQiqrFxqXNmfivu4FbrV6lsgU928ZWLYKTD-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدراعظم آلمان فریدریش مرز:
پیام ما به روسیه روشن است: اوکراین قوی باقی می‌ماند. ما در حمایت خود کوتاه نخواهیم آمد. و در ائتلاف ترانس‌آتلانتیک، ما به‌طور نزدیک کنار هم ایستاده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130084" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130083">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
بقائی: اظهارات ضد و نقیض مقامات آمریکایی درباره تفاهم خاتمه جنگ تحمیلی، کمکی به کاهش بدگمانی متراکم ایرانیان نسبت به آمریکا نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/130083" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130082">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
کانال 14 اسرائیل :اسرائیل در حال آماده‌سازی برای احتمال حمله دوباره به حوثی‌های یمن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/130082" target="_blank">📅 22:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130081">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0DGaSLjgxdxnqSn4OugbEFnQYTxNSCsC3qUACuKUckTQmFpfYRkUOr8Q6tnv1pAFhl6VLVHgEluM2EGArTCxk2eyc0IcXxRUyhvumu1hlSBm7W5ME1Xd_h9Jvzh2M0z_l4rAcbDGOIMC2xIqOyCmgIuZ_WE7cwUVf3bd2j6mOUfBNaYYoDSTz1J0ew9-oqfpnSIP9_sqm7Ay4YyS0CdlJb86-e5jvD-BS2GjCgkaYQUEKOO5n8PX8dCqihIlvhsBnvPjMTi77w3ABC4oLonrAx4BmLnXC80JJVqT9ja7tNICTqdipg1MeYmsCfOP2ujr39IN8d-1qJMHv6wItRyDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ مشاور وزیر ارتباطات به معاون آقامیری(دبیر شورای عالی فضای مجازی)  که از مخالفان بازگشایی اینترنت بودند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/130081" target="_blank">📅 22:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130080">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
در نشست ناهار امروز ترامپ با سناتورهای جمهوری‌خواه در کنگره، بیل کَسیدی بر سر تفاهم‌نامه مربوط به ایران با ترامپ درگیر بحث شد.
🔴
به گفته یک منبع، لحن کَسیدی آن‌قدر تند بود که عملاً سر ترامپ فریاد می‌زد. این خبر را MS NOW گزارش کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/130080" target="_blank">📅 22:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130079">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ: ایرانی ها خیلی مهربان بودند و هر چیزی که خواستم موافقت کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/130079" target="_blank">📅 21:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130078">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOfsLKAFk-hX-zlitWiLvP63hLZzHF22ph3RgSkDx43_glQfg5J4rJ0usweCTuEAuj70iw6sN-DKoe0Exk6zPA8Sb3laI6KkYODHeKE3j50a42dvbD44g9KHBunpPfEPV5hnLXTx4Nub1-uroOAm_TwPvyUtsEshjtJDcuGquzo-XkFm7GuUGZHUZ2vJH15iGRP_pzyBy30-SNufUcqYUXbbA1Pdec1G4eR7M8gN6Vih9f_oA802nKO3aIOGQWPeKy2Y5JzDXqNXEEtTyfUBYXCJu0eHkXCfIn0L9QT_iV0KAQt60qHMdo5N0qCySR317zQrmmkbXDE5_FyX8xjoAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کارشناس صدا و سیما: باید فرعون زمان را سرنگون و تحقیر کنیم و دنیا را آزاد کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/130078" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130077">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
مارک روبیو  در سومین ایستگاه از سفر به جنوب خلیج فارس، بعد از امارات و کویت، وارد پایتخت بحرین شد.
🔴
او در فرودگاه مورد استقبال همتای بحرینی قرار گرفت. بحرین میزبان پایگاه دریایی آمریکاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/130077" target="_blank">📅 21:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130076">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزیر انرژی آمریکا مدعی شد: بازگشت جریان نفت به حالت عادی به دلیل مین‌های ایران به تأخیر افتاده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/130076" target="_blank">📅 21:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130075">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
یدیعوت آحارونوت: فرمانده سنتکام به زودی وارد اسرائیل می‌شود و با وزیر جنگ و رئیس ستاد ارتش دیدار می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/130075" target="_blank">📅 21:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130074">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/450a87f549.mp4?token=D9DrBxqcxbSNCjNgVNbNsRQd91WMxhR0Vg1c5_toOdlrKWgJn1IiYkiu63uvG1KxQuuKGk96wEIJVJezArRxVMfKTIDM8vGzQju9oyPR2ofJXkxUW40_GqiC8cA0B9vcBUuLd56BddYKXqImNA7rcDzGVHtUheULAiUU1qNW1jDK6mOcrVhEXiDbjClcfylUWY4lx0xgNwvX_bh08Pnw_yZ3P0P4lYbnA8EcCNRz92hx4QZMkY5z_5uf9-zZBQS9k-p6iUHf2rJLqyOiGDc0srTOZ4WVTI1v2cs74J2Qr8AmXguyr0FVcxUBysNgkpByHoma76j69hIdfqEyhMY5nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/450a87f549.mp4?token=D9DrBxqcxbSNCjNgVNbNsRQd91WMxhR0Vg1c5_toOdlrKWgJn1IiYkiu63uvG1KxQuuKGk96wEIJVJezArRxVMfKTIDM8vGzQju9oyPR2ofJXkxUW40_GqiC8cA0B9vcBUuLd56BddYKXqImNA7rcDzGVHtUheULAiUU1qNW1jDK6mOcrVhEXiDbjClcfylUWY4lx0xgNwvX_bh08Pnw_yZ3P0P4lYbnA8EcCNRz92hx4QZMkY5z_5uf9-zZBQS9k-p6iUHf2rJLqyOiGDc0srTOZ4WVTI1v2cs74J2Qr8AmXguyr0FVcxUBysNgkpByHoma76j69hIdfqEyhMY5nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دسته های عزاداری تو انگلیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/130074" target="_blank">📅 21:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130073">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
تانکر ترکرز: ایران از ۱۵ ژوئن (۲۵ خرداد) تاکنون ۴۰ میلیون بشکه نفت خام صادر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/130073" target="_blank">📅 21:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130072">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز گفت که برای دسترسی به آن مواد عجله‌ای وجود ندارد، زیرا در پی عملیات «چکش نیمه‌شب» در زیر زمین دفن شده‌اند.
🔴
رئیس‌جمهور آمریکا ادعا کرد: «آنها با این موضوع موافقت کرده‌اند، با بازرسان موافقت کرده‌اند.»
🔴
ترامپ به فاکس نیوز گفت که بازرسان آمریکایی در بازرسی از تأسیسات هسته‌ای ایران، به آژانس بین‌المللی انرژی اتمی ملحق خواهند شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130072" target="_blank">📅 21:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130071">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
آکسیوس: اولین دور مذاکرات اسرائیل و لبنان در واشنگتن بدون نتیجه پایان یافت و گفت‌وگوها در فضایی به شدت پرتنش برگزار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/130071" target="_blank">📅 20:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130070">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
یک منبع آمریکایی به العربیه گفت: «در مذاکرات مربوط به سازوکارهای اجرای خروج اسرائیل از لبنان و استقرار مجدد نیروها، پیشرفت حاصل شده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/130070" target="_blank">📅 20:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130069">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
خبرنگار: آیا شما هم مثل برخی از بخش‌های نهادهای اطلاعاتی آمریکا معتقدید که اسرائیل به دنبال تضعیف یادداشت تفاهم فعلی است؟
🔴
روبیو: من نمی‌دانم از کدام ارزیابی اطلاعاتی صحبت می‌کنید؟
🔴
خبرنگار: این موضوع گزارش شده. آیا واقعیت دارد؟
🔴
روبیو: نه، من اصلاً نمی‌دانم این حرف‌ها را از کجا می‌آورید. اسرائیلی‌ها دقیقاً می‌دانند که ما داریم روی چه چیزی کار می‌کنیم. تمام شرکای ما در منطقه هم باخبرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/130069" target="_blank">📅 20:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130068">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ : ایران امتیازات بسیار مهمی می‌دهد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130068" target="_blank">📅 20:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130067">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ : ایران امتیازات بسیار مهمی می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/130067" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130066">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
تلگراف: ترامپ ممکن است پس از انتخابات خواستار توافق جدیدی با ایران شود
🔴
روزنامه تلگراف به‌نقل از منابع نزدیک به ترامپ مدعی شد که رئیس‌جمهور آمریکا احتمالاً پس از انتخابات میان‌دوره‌ای کنگره، توافق فعلی با ایران را کنار می‌گذارد و به‌دنبال توافقی جدید خواهد رفت.
🔴
به‌گفته این منابع، ترامپ برای مهار فشارهای اقتصادی و حفظ موقعیت جمهوری‌خواهان در انتخابات، به توافق کنونی با ایران نیاز داشته است.
🔴
منابع آگاه به تلگراف گفته‌اند بازگشایی تنگه هرمز و دستیابی به تفاهم با تهران، نگرانی بخشی از جمهوری‌خواهان را کاهش داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/130066" target="_blank">📅 20:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130065">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
مارکو روبیو : کمیته فنی در تاریخ ۲۹ این ماه (پنج روز دیگر) برای ازسرگیری مذاکرات با ایران به سوئیس بازخواهد گشت. به گفته روبیو، گفت‌وگوهای فنی با ایران دربارهٔ تحریم‌ها و مسئله هسته‌ای است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/130065" target="_blank">📅 20:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130064">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
روبیو ، وزیر خارجهٔ آمریکا: تمام دنیا با هر سازوکاری که برای استفاده از یک آبراه بین‌المللی [یعنی تنگهٔ هرمز] هزینه دریافت کند، مخالفت خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/130064" target="_blank">📅 20:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130063">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkRiDDKJjn0nDBQ9fyGuWvBQk_ww9CbsvGRt4bqLsaspbG-km-q2U2zK_g9NXy-1DuA0BrdVGCuKfbucRFXFD2o3KMiFslmE3L1xrmBeds7RJdBCTSaAq87K5NGZGJqr9NS6S7_yPyRQZGUuggLg1eI-mGlJddmANs173mTsEE69H_HQvrNWqhLDpr-lV6PYe1GyWBIVDwrQ8smlEedEl8WxVXCcw1lVw4m9Ss-N3DmqEiL4iQCGrAH9YnwY1BQUeq4wB-S--81kFIstzILySnfAjS-rXsto_e0K-AyEY9v-_p_WYPu1vGpx1WGVuE4jKU4MtXfweWu-mab2YLCpIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعاتی قبل زمین‌لرزه‌ای به بزرگی ۳.۴ ریشتر و در عمق ۹ کیلومتری زمین در منطقه انابد رخ داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/130063" target="_blank">📅 20:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130062">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZq0z0jg6w24havMeIsXRHwDSh2BSQ5Aq6iYI-9Xbl49hMYRFM-LQL0vWo9pdZzGOpXigVUwVIGDJl9S-9_-Cv6KXYxCKgiqui7zZt2bEBnob9fpR3IqbuDMtcz-0RyBmfbaaUaG3uvZqcob31gucVBXLLK-94odiRvOcUgk7ayIbvZcIgqeaetxVvvdsyU1Ani68cVoaDbgcannEGzNbtU7-37Q-Ootv8mAotABeW156ooEA_ji57VnNBivKd3l7rLQrL2HqQ94uFeujaa3PuAXApe_1Ejj7DGOzGU5zrhM1UJ7qhilgJ1TOLRc_ZEJcF1qC6oshM8ecku9lR1vqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت تتر به ۱۶۶ هزارتومن افزایش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/130062" target="_blank">📅 20:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130061">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
شبکه سی‌بی‌اس: ده‌ها کشتی پس از اعلام عمان و سازمان بین‌المللی دریانوردی مبنی بر گشایش مسیر موقت برای خروج کشتی‌ها، از تنگه هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/130061" target="_blank">📅 20:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130060">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
دبیر انجمن واردکنندگان گوشت و فرآورده‌های دامی: با حذف ارز ترجیحی شاهد جهش قیمت گوشت در شهریور ماه خواهیم بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/130060" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130059">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MU3KdusPoka_z9t9VfJPt_Cj18droUf2tmOi1tLQRc34me3GfcMyeaxS4gQYrjGoSrdDtMavLpWQ_MIWU80q_pCVyGoqkBNVMqReZpECEYJ9NPEY5aWiOdu8VaAG8kk28_0j3IwA3rEwFmM6ctx6Df2_ApskGcg95mKpBhv1iD9uzyegKdsiCOH7GohGoGSXNiLdm6PkZfMxMJWYaRcEv9qPwwM1f90zLJuTU3NCKB34Dow1OZ9Atm1jNN2LItiVCAQGTC-Bftx2yJELW8cqnhvsLnabbSLX8_syxDM2020QM5mkaCP2bt3XMiXukAgQ8xSZMfq4ak9Rm_VhbRDBMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در سال ۱۹۹۰ میلادی، اسرائیل و ایران تقریباً سرانه تولید ناخالص داخلی یکسانی داشتند. امروز، سرانه تولید ناخالص داخلی اسرائیل تقریباً ۲۰ برابر بیشتر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/130059" target="_blank">📅 19:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130058">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
روبیو: ما گزینه‌های زیادی داریم، از جمله اعمال تحریم علیه ایران در صورت عدم پایبندی به توافق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/130058" target="_blank">📅 19:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130057">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmJS6DQwq0zS9BqVcKHQ1RBByxQ1OoeA3xq1EyidFUTi3XeRoSPLnvjEug3f2db_H_cwo0av8JSUiNYWYVHb43Jkx2ds2RqsjDL5_G2lapXLIWr3lqwMITZJvfdWiHVrHzI9xTR-lM0lL382HkWfDwAXUJRw-U8nDAdU46lvA6rAQpmw2xA4pj8OZk6V4WdahiSGMrlKKhQYkhHvK_i3m-b8qjV_8Pm5lOqg-UWTlmvwUlS0ulmeLNPw_Opfb2isrO5K-gsFK5zfrQjDX2wn9zoHdVzBbdAVelyU81gPWfjEvcoiPFBN_KbPft6ZTrHHeuGkdTdLZY-scQx6_Tofjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه حمله پهپادی اسرائیل به النبطیه الفوقا، لُبنان انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/130057" target="_blank">📅 19:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130056">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: نتانیاهو امشب جلسه امنیتی در مورد لبنان و سوریه برگزار خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/130056" target="_blank">📅 19:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130055">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAwU879NtT0yF35SQYQicT9E7JhaHwvjhVx_Uuwa4NTU3h3TqXMJA48qPSk2EEX7ehJsCNAbedPyMI5b0OMibeAOKiCcA17QKfzyiLa2G8vaXhrHH6oreOiYgcZ2stgh5UdxGBO4fYQ-DKErlPMG_bn6UgkXJFWF3RjdqVR-XButRiIRI8udwt7bJAn7YV57WFhmzmL7Yef-baD4gRT5b6kdxJs-qKHi2Kv_w1H2JsSfm1yEJG9TU6NGT2amXQyW0HcTMM_3Diwg1EUE6_GzSP6cdWE_x5BfGPxCi3qvm-RyeQGrrhFRVoaIKs-DPIWUsG2sVDYOEXa6pdglivR4ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ جونیور: قیمت‌های آتی نفت اکنون به زیر ۷۰ دلار رسیده است به دلیل توافق صلح رئیس‌جمهور ترامپ برای پایان دادن به جنگ در ایران.
🔴
قیمت‌های پایین‌تر بنزین در راه است برای آمریکایی‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/130055" target="_blank">📅 19:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130054">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ابراهیم رضایی: تنگه هرمز را با مذاکره فتح نکردیم که با مذاکره واگذار کنیم
🔴
تنگه هرمز تا ابد ایرانی است، ما این تنگه را با مذاکره فتح نکرده‌ایم که اکنون با مذاکره واگذار کنیم، والسلام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/130054" target="_blank">📅 19:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130053">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزیر اقتصاد: در جنگ میدان پیروز شدیم اما جنگ اقتصادی تازه شروع شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/130053" target="_blank">📅 19:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130052">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmL79kjckp4s7_5JZoH63IA5z_NK2GKfwQ6-c-vGj6PxhDrJLbbY5S2-iLbei01G7AWxCw_zjck_2_TlRHkU934Ik2lQsWx3RFuCSLcxCDW3kpF-5ulCJ5JjH6FWB6ukXslaH5BvXkIiX1_AAqv1fAl-Kx20YLq8C-RyOpeFgCQhYs-ah1PaJOFIa-BNuOGO-MgA19upMjmSGjtZIPY_i4BffCdT4HWt-L5whqEYXGtnrJikZKCgy1WQl2kyuAnejIzf4Q6pbUfi8DeuZsN_hmSETrAK6OeYV_C7erc8MxPGl4z2f9o7HzBw8E2VPrrThJUWSGTORM76dl28lUhD2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: برنامه‌ای برای دسترسی به تاسیسات هسته‌ای مورد حمله قرار گرفته نداریم
🔴
معاون وزارت خارجه نوشت: هیچ نشستی با گروسی در سوئیس برگزار نشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/130052" target="_blank">📅 19:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130051">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a25fe3090.mp4?token=g4zk7LOEGtyh0uKKYNNIHRvNmwpY9Njuyics0NK-VC4R8RBx55wJB_JzTereYtH5ZQcaJwSJZsz8U-VS_4p_KgmDnREjzsIOiNnJikBcZcPLHnkipq48hyxgYQ8AWUd_pWnGtE_K0zetgvepkYe38XNdH6n375e6iDILGyJq4V5aAnnIIdDaMTpF6RdtSMvfDUC__fyT8Ae8RqtRuu9hOaze7Lznb36-IndzbBOs_t9pMljzA71EV9zwR_0UmAVndKNQHdb4C-9J_aovH1jhbvRfJVmD7X8hTt3IyKBIOCnA-gfQ1CDMpAn4JGxH83HVfLoDmnuII0qPA2jf9Mm6Z2WXdMenCD-ts0kt1SVXhkjHND8GNYltAvRuERNETqBraXvxu31iuWPWFSBidNBW7Xoa4VyTl44Etk2g7wjuj9JlkvNcFzvuhHWgrLlTmupK7OSTASWpeqtZwTZggxsgHjDEOn2q28ardNuqml4Fme1KB05LXL_A7lUzDut-HqpQgrmYKzEXOSGLnDtPowsNz6HB_n6fUsmscd9tiB6dW6bm5eoHF7qKnRV7POQ51UWTNt85llkysfCc3fcDu9oqckJ4JrJI0eJtqczOAAcPMnRYDJ4kXFFVmwGQvR3El0XIdVnkXo6IjyFQ_sL9ew-tvaDA7XxWl6I3eC0d8o3qQOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a25fe3090.mp4?token=g4zk7LOEGtyh0uKKYNNIHRvNmwpY9Njuyics0NK-VC4R8RBx55wJB_JzTereYtH5ZQcaJwSJZsz8U-VS_4p_KgmDnREjzsIOiNnJikBcZcPLHnkipq48hyxgYQ8AWUd_pWnGtE_K0zetgvepkYe38XNdH6n375e6iDILGyJq4V5aAnnIIdDaMTpF6RdtSMvfDUC__fyT8Ae8RqtRuu9hOaze7Lznb36-IndzbBOs_t9pMljzA71EV9zwR_0UmAVndKNQHdb4C-9J_aovH1jhbvRfJVmD7X8hTt3IyKBIOCnA-gfQ1CDMpAn4JGxH83HVfLoDmnuII0qPA2jf9Mm6Z2WXdMenCD-ts0kt1SVXhkjHND8GNYltAvRuERNETqBraXvxu31iuWPWFSBidNBW7Xoa4VyTl44Etk2g7wjuj9JlkvNcFzvuhHWgrLlTmupK7OSTASWpeqtZwTZggxsgHjDEOn2q28ardNuqml4Fme1KB05LXL_A7lUzDut-HqpQgrmYKzEXOSGLnDtPowsNz6HB_n6fUsmscd9tiB6dW6bm5eoHF7qKnRV7POQ51UWTNt85llkysfCc3fcDu9oqckJ4JrJI0eJtqczOAAcPMnRYDJ4kXFFVmwGQvR3El0XIdVnkXo6IjyFQ_sL9ew-tvaDA7XxWl6I3eC0d8o3qQOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
یک چالش خاص وجود دارد—آنچه من «پروژه منهتن» می‌نامم.
ما اولین کسانی خواهیم بود که مشکل پهپادهای انفجاری (FPV) را در جهان حل می‌کنیم. این یک مشکل جهانی است.
اما ما آن را حل خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/130051" target="_blank">📅 19:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130050">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cbc84ad96.mp4?token=dSZSn4qjhLAq9EgzJ1ZYAAYiOF3V5arh6lnmnK-F4HrQpFNc-f2Ha2yCYWt7bQfidp_IHtt-JZSBSozsXSTk1wTNO9E6NfOnqh2QJVpPens1iV83qDvCkPTMKqh8WSqFDW5xcY1dE4SqUwJzSS0r0Aqjx20-5vJbXVdVZ4d9pWcNIHg2uIZBPgN0lSzqS_Dy-_Y3wSFnZLwa-6nv8HkTCcrJUgYr71DdZ5YqmEQYi3hgHlpaXurVht2wWUCwIzKk1G5-VUP2AECVjhDbTMm62WhUgOmZSxhqjjXWzNGfgtrNB3FCRmXc7N4z8i_HbdrPsYisgaiuHqGSZqeWiiLwqG2zzyaehX1njtPKekju8kJ240qV2redWyDDnpuGeHPnho73MeC47XBhToM9u-nhzkb-b828_WwOlzZ8FFVhxxTzEZAMjYbRUUt6bkhQ-dU2S9spHCxeK-4rlm7XB7A6svWHBHnKXyTBmE28q-EM8nUqxAkJw7XO384fQ2PXEiJ9GpCtrzH7yIJ549Uzyz1Hv8_zJW_hEUgEDYq0oVJmT-TXpy9CcfKaBSxek4QDS2-el3BxyW8KI0tjuBNUijR0eUtBHgTb-cpa30KUWecAK9Ek4CpEJgSNRznMFkgu_bBtI2cK9f1wZOLPEFvMV507YssvEsXvVOaiiswehqiJm6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cbc84ad96.mp4?token=dSZSn4qjhLAq9EgzJ1ZYAAYiOF3V5arh6lnmnK-F4HrQpFNc-f2Ha2yCYWt7bQfidp_IHtt-JZSBSozsXSTk1wTNO9E6NfOnqh2QJVpPens1iV83qDvCkPTMKqh8WSqFDW5xcY1dE4SqUwJzSS0r0Aqjx20-5vJbXVdVZ4d9pWcNIHg2uIZBPgN0lSzqS_Dy-_Y3wSFnZLwa-6nv8HkTCcrJUgYr71DdZ5YqmEQYi3hgHlpaXurVht2wWUCwIzKk1G5-VUP2AECVjhDbTMm62WhUgOmZSxhqjjXWzNGfgtrNB3FCRmXc7N4z8i_HbdrPsYisgaiuHqGSZqeWiiLwqG2zzyaehX1njtPKekju8kJ240qV2redWyDDnpuGeHPnho73MeC47XBhToM9u-nhzkb-b828_WwOlzZ8FFVhxxTzEZAMjYbRUUt6bkhQ-dU2S9spHCxeK-4rlm7XB7A6svWHBHnKXyTBmE28q-EM8nUqxAkJw7XO384fQ2PXEiJ9GpCtrzH7yIJ549Uzyz1Hv8_zJW_hEUgEDYq0oVJmT-TXpy9CcfKaBSxek4QDS2-el3BxyW8KI0tjuBNUijR0eUtBHgTb-cpa30KUWecAK9Ek4CpEJgSNRznMFkgu_bBtI2cK9f1wZOLPEFvMV507YssvEsXvVOaiiswehqiJm6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
امروز ما در تقریباً ۷۰٪ از نوار غزه حضور داریم. ما حماس را خفه کرده‌ایم. یکی از آخرین رهبران ارشد آن، عزالدین الحدّاد را از بین بردیم. او دیگر نیست.
و می‌دانید بعد از اینکه او را از بین بردیم چه اتفاقی افتاد؟ هیچ چیز.
نه راکتی، نه موشکی، نه حتی یک شلیک.
بله، حماس هنوز آنجاست. و ما با آن هم برخورد خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/alonews/130050" target="_blank">📅 19:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130049">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qjjM9q7jwZE8StQHnpmP43Eb1P-3FDUbTgKOnMrfBjQ54T6UHQaD9QKei7ismM9WsbQlNqbl15qI9gjdTB1xKxeQvIuYgE_hbTxO6JAkYa-Pd3knB7vmMZflStlRzGW5UIMkbC4Dxvdm_MLZf9yhTbJJ-DmKcE6jT5kT5c08Gr_4lWfmTxJqT1_mcM7JIu_hBqsYkRZlP5ZLouQZkg_7v-f5RecadLIfCDCxVcVpK1CxQOFnL275BcmF9BI7cYEj4UMsxcWC1RHUTsY8LyMCND5HW4ebs8E3pnh83MKsBzx93jFhlqFBtys7Gk-ZAEEVJ1Pa74LTXir1WYbMPcNopQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت هر اونس طلا که در آبان 1404 به 5300 دلار رسیده بود، امروز با افت شدید به کمتر از 4000 دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/130049" target="_blank">📅 19:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130048">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
الجزیره از حمله پهپادی اسرائیل به خودرویی در نزدیکی شهرک کفر رومان در جنوب لبنان خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/130048" target="_blank">📅 19:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130047">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزارت خارجه پاکستان:
مذاکرات بین آمریکا و ایران هفته آینده از سر گرفته می شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/130047" target="_blank">📅 18:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130046">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWE-Ld-zaXjzH8FqZhEOovppCFoxq92JKy8sCMzdfwI9_pq2sngK4NLeITH4aegJ_EhxjDl4XMh7zBbMdZnMKNnHQ28eYYPQZ219DGjpklFrBT5GEQm6RAvGl9W3LwLmhVQyzaIfn0Hh_cFew7bQlKjp4U4_oqn4hgOZMwd6bvD2kFa7WMTG4RQI8JP3JZpF9WEK76bd7VW6RzHRbp3zmXlcLrqomuL7XvF4qhUhoN3D-Xs4EiU9sqzqB1Dt89JfRPnP4AHQCTHk8cMzGWUs__7EKzWKs2wK3KahgnKBHbXpNQBPIHr2Rp5YZzLUkIgRrSMeGWtwC-QoWKknJXxRhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: داماد ترامپ به جمع میلیاردرها پیوست
🔴
منبع اصلی این ثروت افسانه‌ای، همانطور که در گزارش فوربس آمده، شرکت سرمایه‌گذاری "افینیتی پارتنرز" (Affinity Partners) است که کوشنر در ژانویه ۲۰۲۱، یعنی درست پس از پایان دوره اول ریاست جمهوری ترامپ، تأسیس کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/130046" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130045">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/130045" target="_blank">📅 18:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130044">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس:
تنگه هرمز رو با مذاکره فتح نکردیم که با مذاکره واگذار کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/alonews/130044" target="_blank">📅 18:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130043">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/130043" target="_blank">📅 18:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130042">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/130042" target="_blank">📅 18:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130041">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/130041" target="_blank">📅 18:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130040">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/130040" target="_blank">📅 18:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130039">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwU9r7Zpdr05MXOJ29vZ08-OwOOgCloBU5oYTdhCPk11hnSmbtZQL8IiF-FJ2h1JPrnRtuIFd15hLt3n9BAaGETpxRnAuPArc8yYUiEl7n83nBnsex8yy8i5ixLyIticzEYlIg3S2IGui2SD77FRq6_zkCvZqfSff25gjVjiKoBYsSnzqDmKziYxywp_ouohRWCx8fEZh6HIn5vXPuJkGA__2iiiLf94ywYrwYzAH81xT12zcHIfuxYTwlzIUVzhB0gOIu6CLrPHbZ12s8mOiGF2nvxk6RIy9uz7MRlHp00n5PoagJwFRxEoR-gPyc_gP6cONb1R0W3G3uEhTXu-bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/alonews/130039" target="_blank">📅 18:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130038">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، در گفت‌وگو با فاکس‌نیوز
: اوکراین در میدان نبرد عملکرد خوبی دارد.
آن‌ها هر ماه حدود ۳۰ تا ۳۵ هزار نیروی روسی را کشته یا به‌شدت زخمی می‌کنند.
این اعداد واقعاً شگفت‌انگیز هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/130038" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130037">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa3c9d8282.mp4?token=RrREUHoJF1yngg5DOgpYIZk6T3kBFihNuqNmtE7LHlctlBoBHIUM2tLERqXQRoxkoBwx9n6riG-EIYUBiddtflnngx8FJ009yrwRJ3pJFH5bSKPqu6NkEBeTBUsu05Y7JKskowVqiRlkw0jd5SCDdfCuFN_oEZR3j_HwqPyOQ5JBo6GUQOqbDE7RVA9d-fevlc1lYXoWtJ-LW2J5dUB35im1jlBNL3pEk2B2V8QKSmCOKCxrrr12uSEIsQ6s9v4PUOu5aqGV5ar2Uu9BR9tjRQjlhKMWVuiY3OrE6-xqCTviKKjSWHGgteGYyLQ2aK43izao7mwIMF9A7WNdUMWMk4IJPD5dv0PqT3A9HM8baES50x23rc5gwwzaBfExqn1DqVsgJSyvo4XQLN5MNDjlI3-KEZLQwtH-WSuwS6aSbDbdBFgKspUahX-zM7lWFqpOENIow3TvxkvnStG3-LqMS2XuAMzP_Ujwm4RocThDKexbd79uckaPmDtz52-m3XPpW-HGAYcKM8ULiegm9Ba_vpeSiAM68zmi0-Dr7cbE-ghz6LmjCBtl2en8RGCbNzIG7HOZPihd89dOJDBB5wOPjyTT6QY5PjnLkOvQH_jBXrdriZh9t9VZbG7PP5xl41OOSCLOYxa_c7D2J8zL2TIvhrKyWEUQ7bg_BnnSQJhv3VE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa3c9d8282.mp4?token=RrREUHoJF1yngg5DOgpYIZk6T3kBFihNuqNmtE7LHlctlBoBHIUM2tLERqXQRoxkoBwx9n6riG-EIYUBiddtflnngx8FJ009yrwRJ3pJFH5bSKPqu6NkEBeTBUsu05Y7JKskowVqiRlkw0jd5SCDdfCuFN_oEZR3j_HwqPyOQ5JBo6GUQOqbDE7RVA9d-fevlc1lYXoWtJ-LW2J5dUB35im1jlBNL3pEk2B2V8QKSmCOKCxrrr12uSEIsQ6s9v4PUOu5aqGV5ar2Uu9BR9tjRQjlhKMWVuiY3OrE6-xqCTviKKjSWHGgteGYyLQ2aK43izao7mwIMF9A7WNdUMWMk4IJPD5dv0PqT3A9HM8baES50x23rc5gwwzaBfExqn1DqVsgJSyvo4XQLN5MNDjlI3-KEZLQwtH-WSuwS6aSbDbdBFgKspUahX-zM7lWFqpOENIow3TvxkvnStG3-LqMS2XuAMzP_Ujwm4RocThDKexbd79uckaPmDtz52-m3XPpW-HGAYcKM8ULiegm9Ba_vpeSiAM68zmi0-Dr7cbE-ghz6LmjCBtl2en8RGCbNzIG7HOZPihd89dOJDBB5wOPjyTT6QY5PjnLkOvQH_jBXrdriZh9t9VZbG7PP5xl41OOSCLOYxa_c7D2J8zL2TIvhrKyWEUQ7bg_BnnSQJhv3VE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، در گفت‌وگو با فاکس‌نیوز:
۵۰۰ هواپیمای آمریکایی از پایگاه‌های آمریکا در ایتالیا به پرواز درآمدند تا از عملیات Epic Fury حمایت کنند.
این یک عملیات بسیار بزرگ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/alonews/130037" target="_blank">📅 18:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130036">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95dd83e81c.mp4?token=Cbq13EZ2s6MeUIraDbxEFs9T6aVelEm8Mm0eXVPDcMWmKL04R7__MQR70cG7WCunlwHlJF769VP4cBVdvVirgt-hUPSMFFJUDi45b-W6V-RZLJ6u_Tb1ZBv_zZgOtmuXTOBfEjHY-S2a56TY2njzUVcrOiMQ7Es59mJcf-etjgfSPB9z3URbvOuUZPSMtyEEZAYrXzwMp7BuvUoAj07iBmxN--PYY-4UNNM4t9jHhYc4kXRPNDMzmncxiDoLQqrzCEAWOI_nWHOX8DKXH8-2z1rXtEx6hRMRY-i9sL_XVV-6aKJfLm-i6rV2QLpahkpv_QUNHSVmZBuS7a884EeTB6Qk1WF35e4jC_cWSi5k6XjQlVc-9va7sKiaeGkVB7MeBOczBxsZ7e9lvqX4597O2zlPsdqsfoZ6X3A7Ub_OA6lXK6BgDFWnhilXTBpxDZ_swKnagiMz9JL63FH8yGPIkRUKdKSKXBXIzYMIhA5Hj5G9mSnSnl9b20b0AM8h_vLbmcF4NQ2UDdTAPLGNxBaTs8pA2JGqNAUaBlHXtarkmPAgDdxAvSsUtp_4r0nzN0-MQj450aN6Ai3sz5DogN_puM1i3OYz-JMuJY_LOYZoB1nz5CpwprzcfQhWxtoa9pvlrm5Xy9ZpaWuIOFNl6o6LF2B4tU0vAnq139rMts0bhrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95dd83e81c.mp4?token=Cbq13EZ2s6MeUIraDbxEFs9T6aVelEm8Mm0eXVPDcMWmKL04R7__MQR70cG7WCunlwHlJF769VP4cBVdvVirgt-hUPSMFFJUDi45b-W6V-RZLJ6u_Tb1ZBv_zZgOtmuXTOBfEjHY-S2a56TY2njzUVcrOiMQ7Es59mJcf-etjgfSPB9z3URbvOuUZPSMtyEEZAYrXzwMp7BuvUoAj07iBmxN--PYY-4UNNM4t9jHhYc4kXRPNDMzmncxiDoLQqrzCEAWOI_nWHOX8DKXH8-2z1rXtEx6hRMRY-i9sL_XVV-6aKJfLm-i6rV2QLpahkpv_QUNHSVmZBuS7a884EeTB6Qk1WF35e4jC_cWSi5k6XjQlVc-9va7sKiaeGkVB7MeBOczBxsZ7e9lvqX4597O2zlPsdqsfoZ6X3A7Ub_OA6lXK6BgDFWnhilXTBpxDZ_swKnagiMz9JL63FH8yGPIkRUKdKSKXBXIzYMIhA5Hj5G9mSnSnl9b20b0AM8h_vLbmcF4NQ2UDdTAPLGNxBaTs8pA2JGqNAUaBlHXtarkmPAgDdxAvSsUtp_4r0nzN0-MQj450aN6Ai3sz5DogN_puM1i3OYz-JMuJY_LOYZoB1nz5CpwprzcfQhWxtoa9pvlrm5Xy9ZpaWuIOFNl6o6LF2B4tU0vAnq139rMts0bhrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، در گفت‌وگو با فاکس‌نیوز
: می‌دانم که درباره ناتو انتقادها و نارضایتی‌هایی وجود دارد.
اما باید توجه کنیم که این موارد، استثنا هستند، چون واقعیت بزرگ‌تری هم وجود دارد.
کشور پشت کشور، متحد پشت متحد، پایگاه‌های خود را برای عملیات Epic Fury در اختیار آمریکا قرار داده‌اند.
هزاران پرواز عملیاتی از پایگاه‌های اروپایی انجام شده تا از این عملیات حمایت شود.
بنابراین اروپا عملاً به سکوی پرتاب قدرت آمریکا تبدیل شده و امکان اجرای این عملیات را برای ایالات متحده فراهم کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/alonews/130036" target="_blank">📅 18:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130035">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acce89e784.mp4?token=dqJVzgbjyeCQbXOXL_BucbvZFptWTA69bLXFpNFDwhH2f0yanbB8i0llamp8d-8223wYDCwh_ARiH8Y8xtPSaxkUmq1ytSvt_n_sKhxwxKVR3UvozRAcUXTssPMPddHJ75wbsZ2ptlij85TiCuz-fLoS66MGOsC4Ie903xfpRNbdPHNPN373h-lsajmjEJSLHMJp1pOFWp7i_8rQEH3Eicv_2R3NkEtVOHmtyaeSC92_TREWwquZdMS8vkKTYEBvTm-1x5hhPQGCegwOUae5JAhW2ytFMXkLc-L-qcLqLTU6cMkfRQsAqsa9D2Aa8kGMpEBf59J0FhaCtWgFsvzCEFkQYsob08DumEA8HwN09NAL2hWtoW5ilw6hxqvI6yWtmUWBVLLmNJ4uKJbujJuRaFcqywVbzRQRKFjFdK6typ8_2iQQnNsoFsQgD3ZVrp7gEc-fi1_xgcJD8s4b_G-MCXQo7mnwOFRuOTGQ9sPL1PvlLwSzUPq9dtcRMnJup3qcb9xOMBwB-CLoepIiKZm54PhBn86TcC4SLt9ImPdU7jqvlvLNvJ6xzOeIBRd4J5Qad9MrizhYGKNpYWkJZPM5eW-cRyYE9cJprTwoAtg18qPA5TGbE3spGzojIDabrGBmFXx-Z9sFDDH2V08LOZi4h98eN60SCqMsyfw4wFbEZGc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acce89e784.mp4?token=dqJVzgbjyeCQbXOXL_BucbvZFptWTA69bLXFpNFDwhH2f0yanbB8i0llamp8d-8223wYDCwh_ARiH8Y8xtPSaxkUmq1ytSvt_n_sKhxwxKVR3UvozRAcUXTssPMPddHJ75wbsZ2ptlij85TiCuz-fLoS66MGOsC4Ie903xfpRNbdPHNPN373h-lsajmjEJSLHMJp1pOFWp7i_8rQEH3Eicv_2R3NkEtVOHmtyaeSC92_TREWwquZdMS8vkKTYEBvTm-1x5hhPQGCegwOUae5JAhW2ytFMXkLc-L-qcLqLTU6cMkfRQsAqsa9D2Aa8kGMpEBf59J0FhaCtWgFsvzCEFkQYsob08DumEA8HwN09NAL2hWtoW5ilw6hxqvI6yWtmUWBVLLmNJ4uKJbujJuRaFcqywVbzRQRKFjFdK6typ8_2iQQnNsoFsQgD3ZVrp7gEc-fi1_xgcJD8s4b_G-MCXQo7mnwOFRuOTGQ9sPL1PvlLwSzUPq9dtcRMnJup3qcb9xOMBwB-CLoepIiKZm54PhBn86TcC4SLt9ImPdU7jqvlvLNvJ6xzOeIBRd4J5Qad9MrizhYGKNpYWkJZPM5eW-cRyYE9cJprTwoAtg18qPA5TGbE3spGzojIDabrGBmFXx-Z9sFDDH2V08LOZi4h98eN60SCqMsyfw4wFbEZGc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، در گفت‌وگو با فاکس‌نیوز
: فکر می‌کنم ترامپ دقیقاً همان کاری را انجام می‌دهد که لازم است؛ یعنی تضعیف توانایی هسته‌ای ایران.
می‌توانید تصور کنید اگر ایران به سلاح هسته‌ای دست پیدا کند؟
ایران صادرکننده آشوب است. صادرکننده تروریسم است.
این مسئله برای منطقه فاجعه‌بار خواهد بود و برای کل جهان هم فاجعه‌بار خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/130035" target="_blank">📅 18:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130034">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghjMVZqTk5Ju5tF3Fmj9QToJpiRaVarimcfZKg63UwcuDQQc7_-sm4smOVTSz80yDZRe-qdl71ybJHtcf01o8u0kkonppn0ZIW88S2UYdD4PSBIPlXYzLSMc_aKx4qFUfoOoY6nbfE4RQrjfg22f9Sfa6Fy_iJw88Ms2Iqk1x5g8lAPS7K0Z2-8sKKE1KZt2z02cO4E2c92FsW15QTc1qJB0FX6ZitJZXhYDB6wLPcrijv5W1AlqR5hzaGvXhx0f4X3FRtzE7zB9Oabv3IeLfLFf0pUo6AL5nrQJjH5AX_HRSEG-Js2kj9KY9fMsbMZC7t6-Cz5hnqlZFuIOcH9DUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ
: کنفرانس خبری و مراسم امضای مربوط به مسکن که قرار بود امروز برگزار شود، تا زمانی که قانون بسیار ضروری SAVE AMERICA ACT تصویب نشود، لغو می‌شود.
من این موضوع را یک وضعیت اضطراری ملی می‌دانم.
از توجه شما به این موضوع متشکرم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/alonews/130034" target="_blank">📅 18:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130033">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGvce1CImMnwagT78W6ewNS_rSexe71bvctLdTMkpGmZjnrbS2hzxbOET0RE6pLgN1u2YZxUGVhn4yPFphK0Akz2RVt4VI-V3zkBe6W7KEk_bxRifRpruLAQgqrkb_JEMVgznB8TEJy67e_T9oOGYpJZdYlq0LofFiYKZOYPbPbFvMKlWLDNFCNul103kOkIEpZxy2RpjAHDnNo-lDGcI_Zq4pU0Mx9qGVNbsEt6hKiqdQ_aXSZc3Yer7xksxiZzg0rsJvHb0PeI8y6Nvm7szftc5OlJLBLtA479-gtk5RPA1aEY_Ea8CIt2pIEDIbKf4RzkfrrDG9BBgDhIivBNGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت انواع سکه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/130033" target="_blank">📅 18:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130032">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHuFhqBfVAnZPEyrJQhA5h1EL41XR6GdER7OT_O7QrGV1RQZ9IRApRBhqQhaBNi5202_QrPZPh_9p6cOp686FjCVRGlS02xPDxw2xZ3u4Eb7n3b8D4wlo3JnMPh6yzqxmZZT828DZUzyx7ATxwsvxXgXM1U7RXyCF8VaEDkMiWFVL5tOAlzaH51Ju-yXFh2zJgui0l_flu7YaVaa56n2l9bLbGjtefcxXpSQSAMQIUywthIB2okh3zunZQj2GcrrjFHvFx5RDHhLtyBKdmAyaubJB6K2JiCYisNSKzvcK6-1_W4gkFAolJ65rtWoBGyRURonTczHHWrYHCIHxZsWHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت طلا و نقره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130032" target="_blank">📅 18:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130031">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkEpc6uwlPFJzpM6X3b9k9N3Ap6_oaq8tXejztR3LTbCLgQf0yFiIFg7dYedmQ_Jp6du1eih737kbNEEDgVGB98rxcSUkQ4dndmNO5I0ZU-nPJha4ZRWGS7db6ndtp5juASsyD960OkjgNM4DgQenFUCU3ML_7m54rsH2Da3V9CMuA_HveL-nJObjLMovFN69GG-INH0Uv9nDYVH2pNpHUkUE9qkE21-lqwORNbT1Q5MnqXzbMg4FSyDs3YZs_u-jEXTpXgBFRm2WjLt67Gzesmupdq7UVzEMhH22Ed4gcRgu-pLU8ZL3ZXg-RxZ82dPwh5Dplhaf48TjIdW_j-E-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت انواع ارزها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/alonews/130031" target="_blank">📅 18:05 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
