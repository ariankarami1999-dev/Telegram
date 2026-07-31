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
<img src="https://cdn4.telesco.pe/file/FwMbNfb0YRK5Kkw3STtzOUI1UI0qPGYSPc0YFo35a4GV0d15W1TRHU3huPKx5RS6TOW8j79_nvfmcIOr1kOHY2FOfgZEGm3esyOn3OgH784j3D5C8g_VgtrELnOwkzQPjqIoJAEBsWFUzIlfjiJGR-zka4bYktWgq_CPDiOQG9ZBWXOhFMeWnaaq64zbvwSTjLEz965Vfh87TUjQnrDMpnGhfGp3abHnfKzQQVyU3s4GJQBZEUHrUC_cJaE1xlzF-ubH9Qgaebgo4b15clP5D06b49dEn2wujftBBhscnljvA_b1OEv4RDYM_20icnU38osiYlB1aXPAWeUXDTlsKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 22:19:56</div>
<hr>

<div class="tg-post" id="msg-81594">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrJ6QlXFpbXvGHEJ4IaDOsPbsPdTytcfA81VVCqivhOekrpFeora7MXW2xbl2SCPf2SJIwQ9GBvm-CaLVREfrzwcNFq_6JgerQxB_1gZia-LhJ-jTYfpJ9IoJrkL9ji5y2OWt-dXaIwlTbTPGjzTiL6EDnSta4TnGqedgq1Vod5eUcCkGcZy8jo9_b7zcwjVQV8X2wu9VJlxUMtkLmd8T-lrHDdGLzv4QNh_Tlk1TzCNCUuuhw2pKp_j9Kv_59KWaFWBhiINnu8nMm3pX0mwU6B4ILWj1BzMJOGHW1FLp2Pb6d1ZgNwXNoWfrX0dNbUuBq6MI2LsRlVtXqQ34sjGkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وول استریت جرنال:
ترامپ از دیپلماسی ناراضی است و وعده داده که ایران را با قدرت مورد حمله قرار خواهد داد.
ترامپ روز جمعه گفت که قصد دارد حملات نظامی سنگین علیه ایران را از سر بگیرد تا رژیم را مجبور به آمدن به پای میز مذاکره کند و قول داد که به این کشور «بسیار سخت» ضربه بزند و پیش‌بینی کرد که رژیم تندرو در نهایت «از صحنه خارج خواهد شد».
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/funhiphop/81594" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81593">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">#شرمنده_بابت_پست_رپی ترک جدید سوگند و سجیل به نام وقتی رفت ریلیز شد.
🎵
SoandClaud
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/funhiphop/81593" target="_blank">📅 21:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81592">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2I9Y9PomhAVnMgc3nI5eJnddaTU6gizVanxzBufNtNOAe6_9lDQuncloUxkI7NSOwVmTIch_y2XHlh-BzZcfOnWXY7iZ-xFgtZWyfMLPslUqRVzdL5RYq_n2Ff8OGTu9ZEEMPq2XK_Ai5sW96INa6QJwKe-u1LA9YGb1wF0ONNms4DcpCyTANVkRKW3R2BCLzYsPQqKADesIksrO2-EcW3ndY_P0adSxD2SWXYP_TBP130m1cIOFSfVfcFc-LR6sAn_QfjNZasrQ7J1CLYEN6awY1oXMffeMTnmuvkjpVYHU16fwN1kfuyKIxOlu7AZtJfJOi0zcBatv8pjWHUhZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#شرمنده_بابت_پست_رپی
ترک جدید سوگند و سجیل به نام وقتی رفت ریلیز شد.
🎵
SoandClaud
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/funhiphop/81592" target="_blank">📅 20:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81590">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGxl3y7opa5FLyxD9CY-cczLEmWN0Cv8PQW2XFIxGW-0r-0F8D3oABQWqXpvEcrLSvdsanBAxKde-7PpL0mnubmzXzS9_CgviBpcIKsLT5Rcae2oQBfUxUi91c0gmAZC3viDCYBGvqfHjb5tZZWAhKsjJvyt5MpAfpEayKbx_IRUqlXKroEy70EbRGMMBwTBUFEqDvArKTAd35J03cd5tTGuuEez6Re-e7TK0L51vP2hEpv9wqkB5_XdqR3Ph61EUDnlD9ltl0OWjakdGWwsASheVms_iPhcrlmgw5oUDJiFPS8VLHYOw7H9LHY_Nk8NvPA88J10-r_gqoGjRRaQ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست خدا عیان شد
آقا تو کربلا رویت شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/81590" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81589">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4m9FWZOIY1hqPXQ0wZgVUz_sJuWH2uhSRunaTjf27LskbH_eGOlAp4A3xMK1tYp1S-JwgqbZrGAPE7lbOHlzWcnBKsghlQ77thTmo5QJB6oIlyEkZfs29mT-fh1v1VS5J2M7ad1YbwY5wIXsioA43EdMki41BZKlGEb2aO0v0gbXPV78HI3_mzXpPBBnywoKihylX88fLd86Qp-JQI2G_alqQaHDVfMn_jVifeJ2Ssh3MLI9X-VgVCB4j3KeKDwjcBTyRwqB-d2vcLr3QmB7EXKjdD5XiTtnWZccN3Veq5Qd2ZFs8KXqFBKw0JHphC70pELJzMaU7DNZPopeU3PEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیپهاپولوژیست هم لایک کرده بود
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81589" target="_blank">📅 18:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81588">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDr-fP0bUB9YyTohQsBsuAZizvJNzT9-UU3cd_4oTOkH-mp4a_vPIXDoLBZswaqfuDGRO_q5_S48ulbkDFb6xwEiiWHKb8Ffvf5KZmbziwxvrObrXZWamdlw-DxzZM8Vzu_lcdIHpQW-ZOhTIjosjAdFIMC5RbPvIFNPxUqXuAqk2XX8mirk6jzbDxgYpLHz3WuCHmiYdUqhxK6UmRCR_9FPcw9UCOnWu8AffzcMMdr5wk5D0Oc8i2jizgMAR6j4WP8v-D7dfGbRPIFDr12xaJ_egCgquql2c2FL6J-K4MYDhf5ftHGa3BDdiSRW5gsaG5S7ya0F1wIjn7DCGuEYmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81588" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81587">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsUktVtJ7zSHIWH5uUu0TFRbzRGLTb5-lC2XVLWOiaMV920_csuyrwSLPmZQ_1T5u83t1MwKp8uz7Gm-9PkjrDJPPDlA8Sj8dc5itQG4-PUG7CezuqpxagcA_OVmPXDSAe0Ikg3pi_Dk5TpE7ofHmwOMzzPnXXNp_whJv1w0rYAftiSDDQMue5ig6VlfMsX5nuEQYL6Qxtu5Y0RIGGbMHg0BMTTW0GAoIjFqtj318iIDmoDeFoV1Zkv5qTSyY_D7fomrqHZigy6eK2DO9zs7U3T-2MxxVijDarJXGZnrQ2VNgYsJf12eM57lTMs5JJA1L3jT_Qyk97wVHxanfjgRpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بیرمنگام سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇪🇸
بارسلونا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
جمعه ساعت ۲۲:۱۵
🏟
ورزشگاه سنت اندروز
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بیرمنگام در ۹ بازی اخیر خود شکست نخورده است.
✅
بارسلونا در ۱۵ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر بارسلونا ۳ گل در هر بازی بوده است.
🧠
مسیر حرفه‌ای از نظم شروع می‌شود، نه از شانس.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r9
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/81587" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81586">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗥𝗮𝗽𝗶𝗪𝗮𝗿</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f78835d85.mp4?token=RYXHQeZs2ywxE-ixSoaRTxWS8EyqRZIJ5atQ5khzPaMhjYWiW38DQo1D8mwMALz3rLXqDn6M8wK7StU1lFYYuF0mySNTIKAbCVMzX0_Yu9Q66t6xi4d_SINZZRnv3fOn8CJcMFiR8i6N2ElvSj3i1SXz6riS71pbh-A5z8XCJXfH1wQymX-Qx1LfqUQ_SRe-9jiUCKgIZ0y0IC22-GcCdv9AjssIV9Kqmm7cSsdbF-itjkJTcZt4g6Dv0M3Y7pbIjc63LYRvyVNM7udDQfRPr2GUBqICxkOhdDkBFxYDDgN4g-L4ECJYtHvrj8CMDhg2k04Vzk6HT6VzZFDyu0NdOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f78835d85.mp4?token=RYXHQeZs2ywxE-ixSoaRTxWS8EyqRZIJ5atQ5khzPaMhjYWiW38DQo1D8mwMALz3rLXqDn6M8wK7StU1lFYYuF0mySNTIKAbCVMzX0_Yu9Q66t6xi4d_SINZZRnv3fOn8CJcMFiR8i6N2ElvSj3i1SXz6riS71pbh-A5z8XCJXfH1wQymX-Qx1LfqUQ_SRe-9jiUCKgIZ0y0IC22-GcCdv9AjssIV9Kqmm7cSsdbF-itjkJTcZt4g6Dv0M3Y7pbIjc63LYRvyVNM7udDQfRPr2GUBqICxkOhdDkBFxYDDgN4g-L4ECJYtHvrj8CMDhg2k04Vzk6HT6VzZFDyu0NdOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجام جلوی خود خلسه دست میزنه به اندام خصوصی جی جی
@RapiWar</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/81586" target="_blank">📅 17:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81585">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a90b7fcb9.mp4?token=WUrz-VsnWqPvl0hhMLAa6KrarzdjA2SdZDCvEsMa8A0lDEiuUjaFkhsHeqZE2OCxhNam3ajQpl3aYEWYNCR8VeG_ZHikYCMK-V3stcL9yLy4082_EOq_-eanDCctxrdI3YW_jvU7W2iio6k_iJXIO1wqnQG5qbETzkbj84qo7Ym2j__ZofPoOmdRwCqvqDR3MJ7mr3OXVLCH6yBmKgPiZkjnrw7haU3HoDqwOapRqWND2L_GOJgbvl7uKZ4_-3J8LsinfSEjMARDInXr7_WIs5DPoBfG8G3XicdgXeLhIqx9PXesu1JUp9Ihp3Nbh08r1fHm7Ft01kooLc9oKzpdGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a90b7fcb9.mp4?token=WUrz-VsnWqPvl0hhMLAa6KrarzdjA2SdZDCvEsMa8A0lDEiuUjaFkhsHeqZE2OCxhNam3ajQpl3aYEWYNCR8VeG_ZHikYCMK-V3stcL9yLy4082_EOq_-eanDCctxrdI3YW_jvU7W2iio6k_iJXIO1wqnQG5qbETzkbj84qo7Ym2j__ZofPoOmdRwCqvqDR3MJ7mr3OXVLCH6yBmKgPiZkjnrw7haU3HoDqwOapRqWND2L_GOJgbvl7uKZ4_-3J8LsinfSEjMARDInXr7_WIs5DPoBfG8G3XicdgXeLhIqx9PXesu1JUp9Ihp3Nbh08r1fHm7Ft01kooLc9oKzpdGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دسته جمعی مسلمانان به خانه های مردم در اسپانیا
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81585" target="_blank">📅 16:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81584">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8_Wan5D_ReetptSN6YKibw22z0RXSnL4WnQulzksTTMd90jUzHvjvKnz9aUW32tjBfBHJEh9jLdbx6eEFttUfG_kiMM6_0YE97aB5iDLTExYPCgZgoPy_K3ZnygrFY7xycHOdTuXxwzpRWmmOB7OFecgK6Exsdcyn05YLLvGF-VuLHhcQGr2R4deGFsXw_QbR5YiaEPpX3PLYestOelfzEBtVyagOP9WdbjQUotX6Ng5KRJOkerGdATNnU9KGXJeY3KJozJvezZ7SoLA2F6LW44BajoYvi9OFvJwjv0QCErwCP5f1T2t6k0RuJxFx00CG5qBe9bBK7v5FSVafoREw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینترنت استارلینک از دیروز در کشور عراق فعال شده.
۹ میلیون برای سرعت ۱۰۰ مگابیتی و دانلود نامحدود.
۱۵ میلیون برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81584" target="_blank">📅 16:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81582">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFUWObYEUHFWvNL0BQz3IzvBAWupgaHdKBCRXZP_gqwdol61FgUJCWAEnpwNozsJ1ngzhvObCFg2dl6n_7OH_ZV_vLAXA2JjyNM57NPy_uGRIzub7juvAu99SGVw3tR9oUcATjHdAjUDB6mnZqVZvwdc6YP5H9hPEmUjHDA6olWmdzECjpyTPTcqk4KzuNuOpfe4vpZGPyVKvNS46RhM2moG1iZ1wqKfEO4nw1um1k17S3h4rkEy4jGPFvDXyPel6aCMKj2vWuUrJ8BOH9SrjkhfPmrkn3Z0IPJpvUkip2s1I5bRC7F2j3yRVz8cy5NJ1AZ8xT7FRL5QQ1VxrVnCXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tvsmp8kDBD0I93RurBaukJP-ujodWR3LLl4IIXZJpuffZJU3bi8qU59RUsVjB6mwhf0dHm7Za5Ai4KyZ4H0sX-WIy6S2yN3ppV2gKMVdTcaJzYFYBb0QfpymG5t0NcVX-JpnEH_sM47yu6yW5B5DS1SEekSi6IvmY618RMEqQuEbhV03DfFLbPR4RqOiP0kccxaG4Y5iysqNHmTHjg4Pytyl3etBzSzG0jmeh08urUnBeBLGTWgJ9joPYwFDJh1ymocRXq0BRi5VSzC6YU3ewJhKS4ZXWwEVqzrYe6DXT330a007Lrz7I1rDgFBVo6LlKVU7a-z3GTKpGM1SDWEVrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اصلا حواستون هست داریم چه بلایی سر اسطوره‌های ایرانمون میاریم یا نه؟؟؟
🥲
💔
#free_toomj
#تتلو
# اکسپلور
#پرامپت
پروکسی
پروکسی
پروکسی
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81582" target="_blank">📅 15:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81580">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ao4B4vB_SDqNGVshHEsqmJXdvapmKf_XPY65D1k8O_Msc1fqmPPsqNdSOuUVHtXqIY5jEH7AP24awiJJORZLj5jiHzjR7iCs3hpBhnCdojm2VI3j4redWGpzIQdMS1bsTY05uWM6e6npSeN9mYJg3NizyRo9VX0Yf_5Xgt-bsvtKiXnKSs1P7aqPhmK7DPHPuarhoNo_jIs94AJWPizDujjeWOtA9o7_1IcCHgUA4govbLjEiimpoytgYtAYN_FIzlXSBmtBrqCdAbvQm_s1g__dfEYJoDxG9oHVsvM0AwsJ2kwRV1anh2FtZeOcIKQnG7giAB1tE16oDxs7lidIIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHlTF1B3fdTf9tvFINdU4armj9prefj1YF03aent8tHB_oZcV9ZeZWu-y9cRXmYhYVOPduZaIB2H0vDKq6Nna2rXlyBrOOK78PblsBP3Hee7ATGdTEifXlqn5K4L5AQtK_idR_h1HW0E59Df46bgE0wPsOIOLELSjUzS_6cmFD1dXpDfFK-_d217To-9Jgvs4aEMpE7ikIIAaF0P5FVxBeWbBCVsdgsOp9jhka1ATrgdDS6OoddXQGGBn57NnjrpTLFTVAmfIqcQa6oR5qYSuKm4vOYC68zI7dMPOLyvcFvsHoI1eP09yBsPZdRtYsrxK0qW40TRL_vc7hyOtW0f8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عاقبت استروئید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81580" target="_blank">📅 15:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81579">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMtu6cFMLGPOVOOizdvJBofZDikZUU2XViDaWbg5fOGYUtVK760BEs3m15Gf25esuVfpWOD855DL0BZ-RUxXwtO-gt-eY3RdNq1m8ZmkEB7FODGdUfqo3ndLcKb1o2YvJfPsaY76yUkOedbksVmHXn4jmC7qMfTAh2dTblrHBFHG6gBakwe2MvuomfGBSDracO8eBVPpETG2E80gg3Ig9GBhKhvEY_yTiNLE_41q2AyjtEfarNDVARf_xUaB5S5V2-1WrqNZNX5pr7rcXURFaGwqUzdXF9KoXr-DQYgtkXEbFmhu7zyBw_-aKTRoRTG1phsWc9stqPfQBk0aLcimhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم میگم تایماز چرا انلاین نمیشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81579" target="_blank">📅 14:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81578">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ امروز با کابینه امنیتی خود در مورد ایران جلسه می‌گذارد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81578" target="_blank">📅 14:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81576">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دوتا کشتی تو تنگه هرمز زدیم، امشب آتیش بازی داریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81576" target="_blank">📅 14:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81575">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آقا تبریک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81575" target="_blank">📅 14:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81573">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMJvIefQcaSLs3zV_drbpssAdjJpzXtm1fDmqtEf6kyQgmKtON6XK7MKu3h--h4nTxQ1pP1hxi4CRQ4848HFdwVmdRHY1yvCAaTq02NyLRsgPfMt-Vp7o_YL6h9g97oMhJc3enQyWgl-4V_SUpHlF2xUxeguVwS4jMbtRHrEp6fdmz7No1Nq5EMN5Vqy1zqJnhohD0-q7we1jBx_uBLDX7dlk5B7EcBbptRjAjofQh0HTEs_-I_Zfpfknnq0VBRt5-NaI4Z9IgVT0OOBXLbzoimZKujNwafSPRkuUgVHVYvmV5SXurJVO8ciQT2o2rGSKAo3IgZlY9VZ0Pf60M8eOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم میگم تایماز چرا انلاین نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81573" target="_blank">📅 13:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81572">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY7FNfH6fw7y3Oem-H9V6El7FfNwMN_NoTMW6i_FDRl70WS-_KyKQqKOKIqEgdip7M9POTy41kTBUIkT1YGrMfjPbKn11gyn8KcGlGX2nuHyBKlAmxDJeQ7jjakcSXif9IKFab5OXvLnauiElBYUcowsQWGTVime6v3UdzNPR-gQe27bA4ybcz-GYzuPr7IuCEVqexiKvtbB2tvBT0vXqI5m4K07G7o6sB2cyiTxoe3v7Aq0_46CLfFUvzhnTmKotqFDguvnbzfZlxlOv7HOk4WUxcTJXYylnz7Mt3WNxcwexpXItl1ZtRw511IbbSrpx43s2yJBk_YEF_iz5MXCgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر وینی چقدر شبیهشه
(پسر دوست دخترشه، پسر خودش نیست)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81572" target="_blank">📅 13:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81571">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEIy4qIUlJstEQ-m2UbW7CKohM4OSH9SJBIU4J751Rv8OClvDxX-xR4NBBLQxu3kSz2DyVQ-2g_jrGM58L88Y6GEXryM_TRB1-3QzrAhkmqF5zXT7SYyxBMzDKUmF7eMmcww7zhP2z9NVzuTnlM7fkfnhtLueuOQeh9hU-LnRbP0NNLvqldokDYUNgeqs2lbOQcT13rUnhNjxrkXqZDohFVwAjVuv-AISQR7z7pWicQ9fernMDAKb2wZqcYWtDPGnNPpHGnRrn529yi14Ar4TiofZgz1OCTANwN4D7xTLPpL_u8qUhOTv4Fx_sDA1xQOChSQzMQNajQ-sBz8knF8Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب دستتونه بزارید زمین برید این سریالو ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81571" target="_blank">📅 13:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81570">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mh96iNGHp5nYhlkCIObJKP_-PzEONESFmW8gVTpNcHIayZePNXu-O0-ShDy5-5-5TNXPV1X9BGZo47VrFHkpMiTa6DIxQUDhfr7HlU_2jt-ndiAUgznh4zfgNBXiPIsqm2pa6bb47mkFZOP69qoNgRrNJbwbsGcRjd9l56RgJZwZ6kmFDIu9c_WmmEkeh6qfnoAyajSZK0shC_golesb5GEogIBlRwfM3dUxrlgY4_FEDPZiqc0LH8VLBcU6wIK9cPeXerhgtB1jLR-Y3_uZBdw_p6hL4IvERXGrW3zIJ__egaRcgXnQE0zBpL58HIU5SKCLdnRGPloWgurwNr9UYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیبایی ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81570" target="_blank">📅 12:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81569">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMRSjBm8C4O34uq8DYzBKndV3LU9Zp_zuYTCNUHj8FrtW7EAma4jB4VjFjkXlmGRFgBuHZ4vR4Qrr3PHOhdCyFKcgFKJn0H25arj2Ax3ypj3gCldw5oYi6c5AZZukQDShIkKw3M0QpGoxhNxrod3l7KJSmFPuky8lZ332UbWoE2qJIig2lh1T_gKysN18qXcvG7Y_DNK6nQFctomCAXKKVqU9AdQKa-P6_Mp0i14lfjHBtGI2DxlvDHxxhXl8WvOgp7YRz-gmGmxmn0Otrbsb_Bv8hJLM0aAT8W5FDYmrpuvgN3-G5iTY4euF4T0po3mP-HiB4igzwTTCh6WgXtbRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بیرمنگام سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇪🇸
بارسلونا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
جمعه ساعت ۲۲:۱۵
🏟
ورزشگاه سنت اندروز
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بیرمنگام در ۹ بازی اخیر خود شکست نخورده است.
✅
بارسلونا در ۱۵ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر بارسلونا ۳ گل در هر بازی بوده است.
🧠
مسیر حرفه‌ای از نظم شروع می‌شود، نه از شانس.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r9
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81569" target="_blank">📅 12:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81568">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbEGlqyCSK-eBefgqKXsXt4h4RF4jKjv52updaXCSEagSYYEmycynmSykoY4xPh6Hm9J-zKImZaC1kn8iGe4T2FaPb5QJiQ8iVpHQolINajsnUNn30QTgpjybg1nl2xkUYXPSoGBb-Nw3F1DzEtJgQklOZWWSM3eaYVG8uLAxeuGlUA7rAQiURKW6MG0myxQa1TSzKsZog_oES-zTwwUSCEn8MHkvTgMuqrvdF1B35D7pzpdScojxxx9ZGxJQWnFBQ6XujBBltiXgpzN2fMgkAwuAGWK3a0JhhaKeVfozpNJir61qY-s_ozumz_mcAUSbuNFB14uzQ6yOqYqM6qY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81568" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81567">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یتیم گیر اوردن کصکشا  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81567" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81566">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf580585ef.mp4?token=guPP7APb64vuBgaf-PW-QscrTFZJ-G_88bv-Zlj9gjuQ3fT__25-0EboiNW7W32cZeKlUr-4BR9FiQGCOf3KkixzLd-AmFir_v6grf-rYUAGYHgb773-XGpWNx9KcLm7batUmv4ZmFkqZhK0-Q83NXaMKSK7JeWYkmsvt8Vn7pfl51uqh90fpukBL9ZnS2_EvSBrhIIX9xITNj2h4ctYCb_IYmDbvOI2JgiU2_orvxB5ohVJf9ISz15zzt7jih8PTy4apBf-7cz-OmQzpLBiJeG2mnA1jSwuH9F4uJnqGlIZWiwPpV6WslBiB4kot25JMIM1dfc6p4T40HJLVx8N1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf580585ef.mp4?token=guPP7APb64vuBgaf-PW-QscrTFZJ-G_88bv-Zlj9gjuQ3fT__25-0EboiNW7W32cZeKlUr-4BR9FiQGCOf3KkixzLd-AmFir_v6grf-rYUAGYHgb773-XGpWNx9KcLm7batUmv4ZmFkqZhK0-Q83NXaMKSK7JeWYkmsvt8Vn7pfl51uqh90fpukBL9ZnS2_EvSBrhIIX9xITNj2h4ctYCb_IYmDbvOI2JgiU2_orvxB5ohVJf9ISz15zzt7jih8PTy4apBf-7cz-OmQzpLBiJeG2mnA1jSwuH9F4uJnqGlIZWiwPpV6WslBiB4kot25JMIM1dfc6p4T40HJLVx8N1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مسلمانان مراکشی بعد از نفوذ غیرقانونی و حمله به اسپانیا: الله و اکبر، ما اروپا را اشغال خواهیم کرد، زنان و کودکانتان مال ما خواهد شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81566" target="_blank">📅 10:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81565">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvTuze2-1YFuxDrlyUWy1BpaX2MYSJeUbRWnn4ZHq_T5fDZKjdbKw-jpmSjloU0IrMKQphhQS_dKcjCBFOsZsm8al9SKHr9KFbhdjTVU0lz9of8JijB6kLV60c4Z_HmsAcQGLeT5rGaJIkalxpCdasddygFx_zTGgMvPw_-ChCeIEAhkHUo9dhQaiL8g9X8ZBiNVtOEcfVnSQvK5Xr2ADet0b4SX_7SEWAbcKSe_auOUvajKj8mQWlqm_4clGCYl7E7XN8u62vtnoswpXEJNYVWNzMQzD9RUf-qgb99gqlFN1IAEV2cd3avzCgxeMcpEG0NU1GRv7xik2bI0uRQ1Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از این تحلیل کارشناسی شده‌ی رائفی‌پور، خبر اومده که عربستان داره برای حمله زمینی به یمن آماده میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81565" target="_blank">📅 09:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81564">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76336c1936.mp4?token=TQO9_xIyKKDOizh_hxBevgZvUc9Haj4SLNUfCHK2UVTz3gHI1PQ9-0tw_qBAX_WTT73l4ERgExkcsDSM55_ze714_vUjpGzo-nQAVPZQrKIKNeQMp7GjgbqX-IXjdJ1adwdRzjujPXk59R-bYbor0JF52ZSC1AMlncujuZc8QPcLEv2by569XKwErgOwBOvF1i17IyvhWjwHakA3j2eGHHHEob628JwUMXSYrnQ0cAdsFpywjMVNogwiSArJmO4HhujGEBnCyeDayuY0elhiyf94UEV3-wO0donB9Bsq9y_jDqvgkDPrRn8McXQJ-cJq65klt0Qja0EUii-OneE0Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76336c1936.mp4?token=TQO9_xIyKKDOizh_hxBevgZvUc9Haj4SLNUfCHK2UVTz3gHI1PQ9-0tw_qBAX_WTT73l4ERgExkcsDSM55_ze714_vUjpGzo-nQAVPZQrKIKNeQMp7GjgbqX-IXjdJ1adwdRzjujPXk59R-bYbor0JF52ZSC1AMlncujuZc8QPcLEv2by569XKwErgOwBOvF1i17IyvhWjwHakA3j2eGHHHEob628JwUMXSYrnQ0cAdsFpywjMVNogwiSArJmO4HhujGEBnCyeDayuY0elhiyf94UEV3-wO0donB9Bsq9y_jDqvgkDPrRn8McXQJ-cJq65klt0Qja0EUii-OneE0Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون سر شوخیو باز می‌کنن بعد تا ما چیزی می‌گیم میان می‌برنمون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81564" target="_blank">📅 06:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81563">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اسپانیا داره شبیه سوریه میشه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81563" target="_blank">📅 03:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81562">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اسپانیا داره شبیه سوریه میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81562" target="_blank">📅 03:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81561">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حماس خلع سلاح می شود   ترامپ: شورای صلح امروز به توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81561" target="_blank">📅 02:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81560">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حماس خلع سلاح می شود
ترامپ: شورای صلح امروز به توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81560" target="_blank">📅 01:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81559">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81559" target="_blank">📅 01:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81558">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fc3e48dc.mp4?token=uPUPFDJDEGTYEIUB5zvLCG__xxIPI05eKXm7p1_8T15wcG1jmSKCJkfrcdhq6duwXbCf1OpivGJd8B2c8xFcYAM053yK7vWAslN-bt4MfrlP-8ZhmDFFTIHIS0DucADjNcX0BwSiAmKA2FGcdmdNBZQrmQkUfYedj45DV0HscAnW1iBjWyR1Er6sI9BOJkDf9HBxjqvDoaq5BkFAOz3tGDdZ85odbuvVokRM05IbfM0mFFn_X6ohwt3dAPh44JRCWpHMmMbrHc5kJV-Pt4EdjI0fXB5mKpVJSFG--9cQyrqGbhcfX3yI6cUxmFFaA3urRY3lydN4R1CPnuJ58QdT-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fc3e48dc.mp4?token=uPUPFDJDEGTYEIUB5zvLCG__xxIPI05eKXm7p1_8T15wcG1jmSKCJkfrcdhq6duwXbCf1OpivGJd8B2c8xFcYAM053yK7vWAslN-bt4MfrlP-8ZhmDFFTIHIS0DucADjNcX0BwSiAmKA2FGcdmdNBZQrmQkUfYedj45DV0HscAnW1iBjWyR1Er6sI9BOJkDf9HBxjqvDoaq5BkFAOz3tGDdZ85odbuvVokRM05IbfM0mFFn_X6ohwt3dAPh44JRCWpHMmMbrHc5kJV-Pt4EdjI0fXB5mKpVJSFG--9cQyrqGbhcfX3yI6cUxmFFaA3urRY3lydN4R1CPnuJ58QdT-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های جالب پژمان جمشیدی درمورد شایعه‌ی جنجالی
بوسیدن دست وزیر ارشاد توسط ایشان:
آقا حالا ما نشسته بودیم یهو رندوم خیلی اتفاقی وزیر ارشاد اومد کنار ما نشست منم یکم چیز شده بودم با هم گرم گرفتیم و داشتیم می‌خندیدیم درحالی که دستم تو دست ایشون بود یه ذره خسته هم بودم یهو سرم خم شد ایشونم تیک عصبی داشتن دستشون یه ذره تکون خورد یهو دیدم رسانه‌ها دارن تیتر می‌زنن من دست این بزرگوار رو بوسیدم.
😐
این تیترای زرد و سخیف و مشمئز کننده چیه می‌زنید.
😐
چجوری می‌تونید نبینید من همیشه در کنار مردم بودم و برا همینه یک هفته‌ست باید با فیلترشکن وارد سایتم بشید دیگه مشکلتون چیه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/81558" target="_blank">📅 01:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81557">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">این پست مربوط به رپ فارسی است  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81557" target="_blank">📅 00:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81556">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm57RPV4WBZdTb3JwOwe1Gxzq4G4thhlEjuUatImOVRTwOvREN1bGNp8jNmLmXlpGD0XaCid4ZcPJsxEqecFMlOHZdFe-rIlewpeAfA6541jbL7GnQYemcTMUQ2YSGM9KZJqB6RmPKfkpsssumkcHGyqnE0dKHstl5NLwT0uXtEy9mMwiRHzaeTNol7srE4bBKdknB_kpdOy-SyDhz3o8HnKBRxzBxL7Z1D7EFhosJtcpTBq8sZIlnNCrwTteUeqMV49EIbJmuJBBSeAm8QSDWdGWErM4azBAd3pR5QzWkwYo_EX6v4-FiLv2-qJDZk3uI6qjn6Jd8SNFpacEaABJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست مربوط به رپ فارسی است
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81556" target="_blank">📅 00:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81555">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دادستانی تهران علیه افراد حامی محکومین اعدام دی‌ ۱۴۰۴ اعلام جرم کرد.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81555" target="_blank">📅 23:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81554">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWjpACKztfPUpE6NM0EFTD9kgEJt4EsQkrou6hPIx5Z4FkOxDISsCIOLuSOFkuYRZNMekOKuUn_IFF_0nj-CWzbcvbD_3H_C-sgQKAxKw3f40lemtmZhvOyxAs_HM7RctBHxZQccCGviQx4EQrwcONmDPH_8Aiews6Anu_UTbRTrgsfb63CMoEsJg6pg3tNp91xquu7NMFBM16fZVQXQIYMpZfvtLTers9kk1u5MWeE7T9ypDIDTiTOahEy5pJY5N1eej4YZv5kgneCAVzOyVV_4efQ4v9UIDyR4t-oTqFrAX4ga_8YZM0Z9aIxdqQ8Kyb3ZKABQHWO0aq7ULMePqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها ده سال تحمل کنید تمومه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81554" target="_blank">📅 23:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81553">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37370edf56.mp4?token=ATZT46I9pbbp9C21UE7rK99GvL7Vhh7liZbfggkRZXvhXAaCRa3pclDLAsLZKoPBCIL3JZ6m5CsMccNOEru2tHFC0XQGbQKZJq11b7V03F3GgCVN4JbC4iQvhaxTuv8_s_5EKtrusLVHggpWI2NYP2zm3msqHKLDLahzK1ps35b1i2LM3ARjQ8-2CtHuxz7nVYe_J_DIqiB4UoNPFgowhf0EPK4hiQOLYputulaRchZ-bCAmKhQBkaP6UqDNvz7EdsuTref0EG58rcK3W6ntwQlWNMbzoMp8JkXQRwSyVK-guYliFZ5bO1BAVPHX5fpRijs6NMz3HIpyoeXL7vZt9SXvRAjtGNZcEemXJ8YGj3HXSMEsnFvZuiHfqvQg19Aokn2yxVYYF8YsQm3BFga8afJndOG5tNyFfBzDzWSF_iWIxuxyZLydQX0vOMxM1SDaep6PPSC1sTtxqL0E09-gOQggRJOIQeA59t0SUKnASJ05Lyn6jYZQLAnt12iczuwk2rhU3_vhyLTdn-_I90QvI98ou2Vw-DQ67sfkGEV9jSX4jU2Mzmj84Gm7r-5hbkW67taWnuz90J5CSOc3p5XkHlcT7oIVG5nodjp_3_R-jaUgLcbkwTqybr9Ylk0zxMEmk-bLw_NPehv60ZCPpHZXepAAc0-O8cOhcqnYIAAJOQY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37370edf56.mp4?token=ATZT46I9pbbp9C21UE7rK99GvL7Vhh7liZbfggkRZXvhXAaCRa3pclDLAsLZKoPBCIL3JZ6m5CsMccNOEru2tHFC0XQGbQKZJq11b7V03F3GgCVN4JbC4iQvhaxTuv8_s_5EKtrusLVHggpWI2NYP2zm3msqHKLDLahzK1ps35b1i2LM3ARjQ8-2CtHuxz7nVYe_J_DIqiB4UoNPFgowhf0EPK4hiQOLYputulaRchZ-bCAmKhQBkaP6UqDNvz7EdsuTref0EG58rcK3W6ntwQlWNMbzoMp8JkXQRwSyVK-guYliFZ5bO1BAVPHX5fpRijs6NMz3HIpyoeXL7vZt9SXvRAjtGNZcEemXJ8YGj3HXSMEsnFvZuiHfqvQg19Aokn2yxVYYF8YsQm3BFga8afJndOG5tNyFfBzDzWSF_iWIxuxyZLydQX0vOMxM1SDaep6PPSC1sTtxqL0E09-gOQggRJOIQeA59t0SUKnASJ05Lyn6jYZQLAnt12iczuwk2rhU3_vhyLTdn-_I90QvI98ou2Vw-DQ67sfkGEV9jSX4jU2Mzmj84Gm7r-5hbkW67taWnuz90J5CSOc3p5XkHlcT7oIVG5nodjp_3_R-jaUgLcbkwTqybr9Ylk0zxMEmk-bLw_NPehv60ZCPpHZXepAAc0-O8cOhcqnYIAAJOQY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مسلمانان مراکشی بعد از نفوذ غیرقانونی و حمله به اسپانیا: الله و اکبر، ما اروپا را اشغال خواهیم کرد، زنان و کودکانتان مال ما خواهد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/81553" target="_blank">📅 22:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81552">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fLH3G_bevqsm662fRESWM97rUeSxoouXX1_KYSwbBPIF5deGS-kv9gP6YLCohPejMYKPE--mRY-VvYELo7iymf0w2T73s9MB-kcL22LqMrr5NjoNj3tCng4rkX64t0psdkj92BR6IuNOGJn8G4wgCLTrtxDcEsHcugZuitcLKgnB0yB07pyfdkn8BMwlgDdqtNXh-IFDqquv4BWHUS6Ol8IzOmL0bDxVjgcRQaY3KpUocvvEFnkJMpI_A1fF63U_AQ1dWZQCukeRs5CPMXRWQGRi2Hh2c_PogGMGBKPKCnqeLkyWNdIrVzQO4dq_vtiUYR3AbDReyTaU7vvh1G2moQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
پشمامممممممممممم
نیکی نیکول دوست دختر سابق لامین یامال پورن استار بوده ، فک کنم یامال وقتی فهمیده ازش جدا شده 4 تا از فیلم هاشو پیدا کردم براتون گذاشتم ربات چه
کصی
هم میده لامصب
چه ناز و خوشگلهههه این دختر
😍
مشاهده فیلم:
https://t.me/Footballi_Dark_bot?start=get_tbcbmlqhfqdjyaew</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81552" target="_blank">📅 22:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81551">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترک جدید مهیاد به اسم چشات میگاد ۲  ریلیز شد    SoundCloud  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81551" target="_blank">📅 22:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81550">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCIAc7gCmYZGn4iLO082IzeUDRVJefECAF8kk9UbsWPDW-1JonFesolhyyhgAKXVBJXoXus_mGP6U0QLTGbJVGRcwCU_AsYqgoI_p6JukPv3HA4DQFrLlyXj3G6qVOTLiVQHXvzmEoQvyLEjq_RVcBCM2vOETkty7bu0VxQ8X6A7HQbvAQ2YnRD2OlKqPlseRIJDLz-rcwSlGIGrCflal4SVl8BP8Kap4PKIJKrFdskG5kUOlwqtV5diXbSUndlK6Q8wV7hrJqnPMAkSfYC1g0xc0MCjz09z7TIp59J1Kl1N11MoygFO3PdqYtQMMJ6RHGLVEp1lH24C_fYLeOedKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید
مهیاد
به اسم
چشات میگاد ۲
ریلیز شد
SoundCloud
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81550" target="_blank">📅 22:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81549">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjInOxFbjhTGcN_Be4F_-QkkiE__3XrUP2yWa2gcFf-Pdk80BGsdyp7cQLar6_FxpcPt4Lvd34eEnqPmjeF12tDghr1rruUexkzEaXdPN0PjmQMkGSODxyj8tvFvJEY08YFCsQBurvVqbgTCUy7Z1AONuoSLTzp-ManRXDl1v7JFBd6uWOYShghyDkEeFqOdAZkcQ8em6oqiO9rTja3EzPDOpJiWRBca_CAikS1lwo1vnLnJqcf0u0ERZHfFzp_qFj_-vH2VJvrGUCk_oDCLaHGstQzqACRbYifDNrJyB8wW16dvuZvHe8haaOUaW2X1iHvZABccApgjt-yEq4faIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یتیم گیر اوردن کصکشا  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81549" target="_blank">📅 20:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81548">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پیج اصلی سروش ولی زاده برگشت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81548" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81547">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUkvExeNoj-BToviBGHegDfvqjQbeWnYdUkTJNK2OdVUY0a9y6ouIzcsaDOl1XlMYS_m3X89rmVVqjRNLrZuYFIYdWJa7jPgIKrfLlwhU5fDoO2a5huuhS6vC2ZIn4dplfau6_TlGokJpnTxqQzw2jEDO9z6OiGmBUhHXl2jh7LnUXNoPrfI0ycThzoQmNKvkz3m8McgyIEdLxL6rzP1A186BDu_00-yF0-eSYMy4BfX1aTk9ZSgQihn56g7TVibqT6VHh0VDizbEmtYyp9Sot4XlP1Ac-djSXeYwBDYfPmxPQNbhwZ_Ml_LRo7JTz3sMZKvCisRWRiRo_VCrRMzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81547" target="_blank">📅 19:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81546">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwOMSHXRnRfAl92NWKulDnqFajZhgOP6iuJrJZpDjKAQCnJiSkR1afcHqnuDY3Qq7wqhGrOK9RSD8anRGLBaROZhZb_uBkASiV4tMuuwIcDjtCkWgY8QFep9Cnsa9VPBHltZeOzYJJuWfTRRReHLTD5yZKEGSiOgpj9ibcXh-3BLjNPN5ivhjGui998Mssk0XWY5ZzDefVoLDFGWSRwiY36qkYIJqviNLzKGksYzQu9tGECnLAsX5nm-xZgBrOZRZmXyy130H7e1L13C_lPC2j8Vam1bqJ9V6ea5WGwkFIY_i6lCfNJYG3KxxNzI6doA_CKSnXOcnEIowzR0HcDjSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81546" target="_blank">📅 19:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81545">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJMZOJaBVfXKblUTegngJbFWeg0WdobmQINhNPpF9L1WOYkvZ005P5DdVeh5v2joN8VMKqDB4tjvNGLf8_YkqnFIO_WsTr19-6sST3hZfYLgr4xRAWNiCa2H-CwaEbOMwWaDiKtrbJbRCdAiLRzyBtzJzWg4kyfrb4l4nQhX_4T9LhPlH6sc_8qJHUjsWJJC6FyzbOTJ0PnExIUSAsdQk7zb6R7fqv9jZe1Vx26rMeyJEzKnLhnkRPy3cveTr0hasvZd23psU1PtjDtLhR9AuD9EencXQT-D6lKsy2cfBVdQ5yCPHMm940fRRKR5KyLXf4aesQAKmGzHWYFIt4ZAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81545" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81544">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFLvpTNxt78sVVG_9qAactNj32IgUHFzrscVbnYl1U-7Ozku8gTULT75JI3TNVAv3BWqhHud-RjHbOjssIR40N_33wdQPzfg-GBUPvVRJJXhqVrqRCbmGM-1VVx22KU4dfFmjdOTfU6UOWXyyRwAH3VHmqg8w7jCNL_kYYchtuzcbOu4W-_fO4zsoSbQSUWSfnI0zzFXnkAL7l2dUOKFkgnS3uIoijOjgbhFgywYEvPnCyKBY8ve9BZzHyODn14Lw3Ws1OSDV41zU9KiRiLXbX5CpebNwGMuhEAQfEigH8PGwzgdgJYeBBXBbYSuy5cDgkoMKS2LTwoTRAzna3pNDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بنفیکا
🇵🇹
-
🇨🇭
سنت گالن
🏆
مرحله مقدماتی لیگ اروپا‌
🇪🇺
‌
🕔
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه استادیو دا لوز
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بنفیکا در ۵ بازی اخیر خود مساوی نکرده است.
✅
سنت گالن در ۷ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳.۶ گل در هر بازی بوده است.
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در دیدار رفت، نماینده سوئیس موفق شد با نتیجه دو بر یک بنفیکا پرتغال را شکست دهد.
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r8
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81544" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81543">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxnk1Ga_2JLwBxY4QDXVIKSak-vReO8Rbn5hEXqL30xSDrq_YDxD_wiW0P74aFmCzm-q8z4BBWXRcj4yWArcZfVcNRCEt-_QuGJL_diauTCM2evWUpKbpt-36482S8KRWwyiBoRq2Rwwx6Od5BWTGzkOJlIG2IfmhOSV7uJ6fY8x6Zq7uSYKdwOs2vpODluRWB0X_h7tLkZFEGDcaepCPL7G7e4Y2b3X_uckSP2S1Nfm7Zhs4RSnJakN0GhZD-Tsv9TRt4nc6OG66raXnzbIgBgKhKnXkhfnMp5cN4HjCMgHj1vH5So7tFt-mrPDRa_fcum1KlrNwWq5p1EB10n54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران:
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81543" target="_blank">📅 19:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81542">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2bMqgnMDHmj7msL1YJd6qsqlvbGCsKbiyT9-QstXXBYKEbLUmFKnC20ZH2AprS15cvGjpgzPqe1uOT8OxYdlXI5YlcraW91U3zj9hWk1AzytV-D7oeFiU5x-fZUOQeds1O3_V96TU0tSHFSV07dXjqeohO6zlKCpR1wlXR2zm5xduxJQIQVo5bdsDQmd18dF-wkm98m877JsE_RbPSdPRzdca6imBesP9plNh-InJ1AGT_WhK26H_wkCsJOTTMll54MEuXSmf5LkFFMO769fG6003p1mqjRGeKjF--xDAIe61Ox96Khg0m03ZkBmX5i5pyfIFxmvSUBluUF1v_aVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلشیفته چقد ترسناک شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81542" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81541">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMcd--23l3v7upJK0bvmu322_YHaDLRvY0N-WghEfDI2WtdSQXJe8FjUktMafC-radpVC3WhImhbc5DEioAsWxyvG4WN2FnnF83vUWUsIyNE188TTKHDFFXbfDnJ7807o7XcwDPwAMT59j2aeIJomZtxjxiZbPpDsvB0xvz_oW6UGGhGS2lETCXN3ydFrLE35VYLoua5SDK3bcMxpsklVyWaiLi3hbZe6f4PIV3jIDCHvUhJ_sldXliIwaEmyXwJgFEJU9w4v8xI09gt9VMdLhNlpyEWNqCpkM9U8-5oH9LbaHyEHnwfnjOK2Jv1wx9tcv4oGOFm7X1lFRr1Xlwexw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام بنیامین نقدی، جوون 26 ساله و از معترضین دی ماه صادر شد.‌
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81541" target="_blank">📅 16:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81540">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a45eyf7BlQDXu3Oqx7idSTbnI8naR8k3habqPJNva7SIUPY9WMwufsGOZbg6hKwyTH9M54H5DTyjckZeW9Kiiwq5Zv7sgzy_8TyWntjESAM4dE_hPkqNW8lxnAbvFWbkVQFIbQt0iMZ17ML29F_cn_i89-XPcx1G-VEJF24hF2cpZw2bndyZEuUV6_NJh-HrvfJlgpBMJANLv94nkGXnOmGKevaJKsf8kZ0wKFYrNyQwcqlwRMldb_X6pwRvUdHo3pn5R6hFNo-AnWyX5kHCoqPK6V8x34FU3isQqEMZDNBBOr7sAHOQw2FCK4ROFHw7uRLp77etMGbjxxxleYUVeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیج افشین فدا بلاگر مازنی بخاطر استوری که برای سه جاوید نام اعدام شده تو اصفهان گذاشته بود بسته شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81540" target="_blank">📅 16:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81539">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">از نیرو های مسلح درخواست دارم کره‌ی زمین رو منهدم کنن دیگه زندگی کافیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81539" target="_blank">📅 16:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81537">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khTOQjU42qSFIOVJqe1hWHMfqhCDERBWQVze3cTiKx00xwy4D7BX-3B_DYgFDuDcOg9cQEU2NL82d3gG1YahzcIrT_Ys23UG1t4YeYialCUEYYlJmWtQhOR2i81H_K03m9vJUXNYgm3qVFYclz4SDaLMi3PNpdzKeUwyeJQtCMCIe8otvWBNdeR4M3xyXcdn8ohuJi6E-h14PZcbtdm8czBBl8JBR4GdrLiD7HLsb5RYtwSvNVrCSVzwKIrUK1pdkRniSNfrZ0b6An4NgM_ZCKJdGsY2xB-CjCb0JYUJrZjRRtsXNO6KCLZLp6i5hvCfSfZ_h7XBJ3aNVX4QH0pLlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفرود سواری در کشور ممنوع شد
تصویرم از وضعیت یه پیج آفرود که این تصمیم دولت رو به تمسخر گرفته بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81537" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81536">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اشکال نداره چین میاد بهترشو میسازه
🔴
چین گزارش‌های منتشرشده درباره برنامه‌ پکن برای تجهیز ایران به سامانه‌های پدافند هوایی را رد کرد و نادرست دانست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81536" target="_blank">📅 15:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81535">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiVCWsa69TBEwph9ZcAAilsmve6VJSsd1ghTOdSWJTsZE3awL1IlA1wH3ANp0xrwXttjwZRuhXZYRgJ3_P32mi2iSGNKbExpv3R5Bij5uC8LR-fZkEUr-V0KD6FIxeOv_nCsaT78Binq0dXiFKtRvLkwUjPqHd5kZKKoR3GT5V3WNKRgJf_1esgQsQsmWJlbbl1oeERVnmSkROcI3jb-ziVHF_j4z1bFjcFaGjMDx3SJOPHboZErnywldGu0SpeLhdVLr5KopA6xt-t2rCtf2DhkCdBVG73TaXCec7CboN6lWBo6HYHcS9fYyCJVF_D6o_-xdv44FqvkyH6QQzZ0XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده اید؟
صداوسیما: امروز صبح در پاسخ به حملات آمریکا به ایران، 6 تا جنگنده F-35 رو زدیم 3 تاشون کامل منهدم شدن، 3 تاشون هم خسارت دیدن چند تا از خلبانان جنگنده هم کشته شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81535" target="_blank">📅 14:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81534">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0zzJDQpwzuWQb4M73ZgT1X_ucXWWw8pvjloIED3spLP1wX6MX-_GyFhYMle5beT5v2vo3CDAJavTKOwhB0Vb6YL0O0fZcpflDFzLlzomqJkbg5oQp_ktEOVmBfrvfYZaB4Vk97CrSQ55bI7e99XXq3qbRPLKmrsWBI1dtQwczsoUqBk00DGhyVBHyJfuoU6BK3THfYFmKBR13cv_T9K7Z_s6haCR69IArO-4EZUpFWJU2SQ2o9ZZbksboD1n4-rXkwi_mlPmJoX1T9fs-xedB6syrNtiMfvwtqsvjZj1XMKJv-OWgfoYfWWCmq_0eOEjquSisx45N1XIjrsMC6LiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دایرکت یه وکیل دادگستری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81534" target="_blank">📅 14:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81533">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=kxiEJJkp6QoB9DHYgB-GAi6wEcsUaoNqtuVZcgADqDD8RRnXwlGwm4bDBx8lCpcJ1HVBdsb4yFtgTbYOdW6lE4ysdQqlRPjeQYPf2StBK0-idLR9gondG6AIgBh6W20TZJuWHfVWwGvOEDoUXB4rT1jSeRyS4B7XEIOORVzyxsigJjbr0LLAlyYvALs9SXcVjIIb7pKlVMDEL_SmHmHIGbSlf5GVLEEfWSmh04IdeW0BLujTTlrrVVY-U6bBvIuIqyUdV3d06Gfl1ihX8a7WQPLZnjWejyfDM4Z2yeOugZjN0iyegA0noAr0G1xcml6_RVwrUuLP2FOXpvYf3IpwRzzTS4l2adKhZ-SIIz9uL6oHgtulpMvfWdTFQvYjFvFkEv8VYRw0EXiRepGg1BDshkhn7zxLdjYdkFo0hqlTYrBfJ9AVQsP_eVSXDXW4VNQF-SbJdzFJR1E8HBYD8XjQ8bXJWneE3qoE8Qa13gmoNWVnQB6YeVjvbA5Rjdsqb0Dm4KQ0qEmKPkXqg4zVFhNYPLNDRCa4tF5iFuvIwHZwwxOQ6XZ2yZcE1i9xsgo21nW20Yb1Da2BM1tIzuLeCXHiByNGafzPu0WpVrivUBfLB_e3ljzcoFkYQcUGybg_mzno9pN_OkKzfmQG86E9W8RJdIouaKc8AF6JJwwy7ngFn3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=kxiEJJkp6QoB9DHYgB-GAi6wEcsUaoNqtuVZcgADqDD8RRnXwlGwm4bDBx8lCpcJ1HVBdsb4yFtgTbYOdW6lE4ysdQqlRPjeQYPf2StBK0-idLR9gondG6AIgBh6W20TZJuWHfVWwGvOEDoUXB4rT1jSeRyS4B7XEIOORVzyxsigJjbr0LLAlyYvALs9SXcVjIIb7pKlVMDEL_SmHmHIGbSlf5GVLEEfWSmh04IdeW0BLujTTlrrVVY-U6bBvIuIqyUdV3d06Gfl1ihX8a7WQPLZnjWejyfDM4Z2yeOugZjN0iyegA0noAr0G1xcml6_RVwrUuLP2FOXpvYf3IpwRzzTS4l2adKhZ-SIIz9uL6oHgtulpMvfWdTFQvYjFvFkEv8VYRw0EXiRepGg1BDshkhn7zxLdjYdkFo0hqlTYrBfJ9AVQsP_eVSXDXW4VNQF-SbJdzFJR1E8HBYD8XjQ8bXJWneE3qoE8Qa13gmoNWVnQB6YeVjvbA5Rjdsqb0Dm4KQ0qEmKPkXqg4zVFhNYPLNDRCa4tF5iFuvIwHZwwxOQ6XZ2yZcE1i9xsgo21nW20Yb1Da2BM1tIzuLeCXHiByNGafzPu0WpVrivUBfLB_e3ljzcoFkYQcUGybg_mzno9pN_OkKzfmQG86E9W8RJdIouaKc8AF6JJwwy7ngFn3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛ بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده! مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81533" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81532">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC5QMzbzjuGwMaYKPxttxnl9z07wOgzNUWnnk42xgFj2472lplm1cUCU_YwA2SM76dshbdLGmU1qEkwhyJ8wXYHyJZLdVCycmfLBpG0-qE85PFQYcLFFVlsOB1tMxnssxPsQAEd1yNlyqq8RabjQupLAIBMe6B8p8kvtuN70p9KK0QtV_NOC04ls1j0oY6I2aWlHbCB-hDplGiiaApPEzDrpAow7glNEwJZ4dPMTk_mnJZl0ohvWAWY3RRpbsdTbUuk5Jx95dpNG88nt2lPpC4m-QzfJrNJ8IAzpcZLeFYTBIsZHZ-dA4x7JpqnHWuGtUpTZ_IkcoV-dj-lJi7qeog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛
بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده!
مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و دست چپ نوید زیادخان شلیک کردن و این گراز بالاخره زمین‌گیر شد.
این مادرقحبهِ 36 ساله، قبلا به اتهامِ "ایجاد مزاحمت، دعوا و درگیری، سرقت، ضرب و جرح، مزاحمت از طریق فضای مجازی و تهدید به قتل" زندانی شده بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81532" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81531">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUQg3njsnvlF0n4Ix8SwCEvt6WeRhZ3lTFPjj0MTgHpQkQgof3Hh7wgowCjpnXje-k_iDlO3ApTtcQU-8ET6JqA6yIQk1EMfsbMqLtVrsJVuCXlZQlh5ECgnWc2fn26_2FjlOOQIvbk66mQGjLz_AmVgLp3q9MQhKtbzXNT_-L8GzO_xH1ASghpd0pVx5E1-sUmkWU0EBJXXB-psKUshUSZ2zFjLGevBaEUJXpW33QTcTlX8kRq-4KO8ADzauiZB2X4yrz5Ll3Y_msfis9Xs4yQAytZbU8xbmt4cI9S53zNTR6rVnp0EoP_TzdBCHCS08kiRoWa5-i5KRhiBtft-lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بنفیکا
🇵🇹
-
🇨🇭
سنت گالن
🏆
مرحله مقدماتی لیگ اروپا‌
🇪🇺
‌
🕔
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه استادیو دا لوز
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بنفیکا در ۵ بازی اخیر خود مساوی نکرده است.
✅
سنت گالن در ۷ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳.۶ گل در هر بازی بوده است.
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در دیدار رفت، نماینده سوئیس موفق شد با نتیجه دو بر یک بنفیکا پرتغال را شکست دهد.
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r8
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81531" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81529">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یک منبع آمریکایی به شبکه "i24NEWS" گفت:
حمله شب گذشته گسترده بود و تأثیر قابل توجهی داشت. این حمله تقریباً دو برابر قوی‌تر و گسترده‌تر از عملیات‌های قبلی بود.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81529" target="_blank">📅 10:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81528">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81528" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81527">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81527" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81526">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81526" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81525">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C54pgU9QrWwYWjf4dSP0GjQXu-98QXyI7Tyc9eKRE-2OzlZpoxFAV3QEBvLhgssf2NG9cuSZqqNWRgb27vgqreZeLguAuOiscnUdkjTLoPOXmsY1c9dpKJxclnb4jdcz9V2zDf-H1Oh_10zjgFJ4EmYh8YtNkBuhAmE4bFA1gONUi5mKGhSl3rMFcHCP0cTG2ktHwi6FKaDNO4Qjv2rs9U0iSeK2MbIUldcX_duWNmfeiX0sF9Q1ZIHBVtHv8KPoKSHb9PR4QkVjstOsNrb-qo53oc8P64ol9fVZV6QETbeLN0Tm52OiWjiaA8WltXRDpVrPeL7Po1EBIsWsvxQ-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کیرم تو این اکسپلورم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/81525" target="_blank">📅 08:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81524">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اینکه شب گذشته آمریکا مسکونی زده احتمال داره یه پیامی باشه برای ایران واسه جنگ های بعدی که احتمال داره رخ بده، که امیدوارم کصشر باشه و این برداشت صحت نداشته باشه. (اگرم انقدر اورانگوتانید که فکر میکنید آمریکا کصدسته و مختصات اشتباه به بمب و موشک داده و صرفا اسرائیل نقطه زنه نظر ندید کلا)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81524" target="_blank">📅 08:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81523">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=N3FEbwvujvVj9AfdMqVSafICljBgqO2P2Gmul3feHDRpc2AL3a-0Ohjkzz-SFOllLWUhszxg074uVccjykKqz4eEH3a8Sd5R9cj5eaH16ZAvAm-U-mLsa-Ctmr3OsdFcO6WRDWlHTNMZ9ZScMBGRjuKWyMb6vazbKH7PGw3xwcjA7po0GOke8ccWWfc9C50fCgxqptKqJHJm_i_lWpQjWJiMefBfNVmBTSt4A3mCEO7KiPp1BLsT57glz8K6-61GD6u625-gIdf7qB-EO6V0t6hCMA0P2uxzUDhx4ryfn-vdjHwaE7gutWFWX2VN_wdcY7hjYe-SzdPEqHaNXxF5fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=N3FEbwvujvVj9AfdMqVSafICljBgqO2P2Gmul3feHDRpc2AL3a-0Ohjkzz-SFOllLWUhszxg074uVccjykKqz4eEH3a8Sd5R9cj5eaH16ZAvAm-U-mLsa-Ctmr3OsdFcO6WRDWlHTNMZ9ZScMBGRjuKWyMb6vazbKH7PGw3xwcjA7po0GOke8ccWWfc9C50fCgxqptKqJHJm_i_lWpQjWJiMefBfNVmBTSt4A3mCEO7KiPp1BLsT57glz8K6-61GD6u625-gIdf7qB-EO6V0t6hCMA0P2uxzUDhx4ryfn-vdjHwaE7gutWFWX2VN_wdcY7hjYe-SzdPEqHaNXxF5fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متاسفانه شب گذشته هم:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81523" target="_blank">📅 06:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81522">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نتانیاهو:
نمیدونم دیپلماسی چقدر ممکنه اتفاق بیفته، اما نسبت به شیوه رفتار ایران بدبین هستم.
اونا همیشه دروغ میگن، همیشه تقلب میکنن و همیشه برای خریدن زمان بازی میکنن.
آیا ممکنه این رفتار با اعمال فشار کافی، از جمله فشار دیپلماتیک و اقتصادی، تغییر کنه؟ باید این رو امتحان کرد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81522" target="_blank">📅 06:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81521">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تسنیم:
برق برخی نقاط اهواز قطع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81521" target="_blank">📅 05:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81519">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انفجار های پی در پی قشم و بوشهر و بندرعباس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81519" target="_blank">📅 03:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81518">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بوشهر آبادان کیش
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/81518" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81516">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=ezuuUMMxVEy9NNHrMo2KFpiYh6he6d4JhKXjH0Szpd2h40vJFMsp83SUJdLEqzQTyog_5UanPKTKM4A_UBe0YPQM3i2Iu6lfiMmVYNp2zfrA5vUUSUu9Vnf2Y6dbOV5lcitzbtD34a_JG-Bd7xFIQaUjOmlriHhHcDWsgSsFh7i0YkFkvYxfYS5w-MfFy5i2JNVuV2b-zTwYC-oPUBWBUCv3tb8bHBz0RjNlwx9oIhj9OehWeFk776WnrZxpISHwKiX2oZzKVk8GTxlNMS7GkpXwJWpRGqkw7P5fNvBC7zQd0RTPEK6ych0tQN31tgA_JtE0fwaCul6xjCrcZfKp3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=ezuuUMMxVEy9NNHrMo2KFpiYh6he6d4JhKXjH0Szpd2h40vJFMsp83SUJdLEqzQTyog_5UanPKTKM4A_UBe0YPQM3i2Iu6lfiMmVYNp2zfrA5vUUSUu9Vnf2Y6dbOV5lcitzbtD34a_JG-Bd7xFIQaUjOmlriHhHcDWsgSsFh7i0YkFkvYxfYS5w-MfFy5i2JNVuV2b-zTwYC-oPUBWBUCv3tb8bHBz0RjNlwx9oIhj9OehWeFk776WnrZxpISHwKiX2oZzKVk8GTxlNMS7GkpXwJWpRGqkw7P5fNvBC7zQd0RTPEK6ych0tQN31tgA_JtE0fwaCul6xjCrcZfKp3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان مراسم اکبر عبدی، عادل فردوسی‌پور در کنار عباس صالحی وزیر فرهنگ و ارشاد جمهوری اسلامی نشسته بود میخواست دستشو ببوسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/81516" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81515">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81515" target="_blank">📅 02:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81514">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81514" target="_blank">📅 02:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81513">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بابا کصخل بمب افکن نیست که رادار خاموش کنه، سوخت رسانه</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81513" target="_blank">📅 02:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81512">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بخواد بزنه ردیاب سوخت رسانا رو روشن میزاره که مهدی ادمین فان هیپ هاپ بفهمه؟</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81512" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81511">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حاج زدن حاج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81511" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81510">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81510" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81509">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کصخل سوخت رسانا بلند نشدن که باهم بندازن، بالاخره میزنه دیگه</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81509" target="_blank">📅 02:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81508">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81508" target="_blank">📅 02:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81507">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81507" target="_blank">📅 02:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81506">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فعلا چیزی جز صدای پدافند شنیده نشده به فیک نیوزا توجه نکنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81506" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81505">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پست آدرویت تو چنلش: این روزا انقدر اتفاقای بد و عجیب میوفته تو ایران آدم نمید‌ونه از کدوم ناراحت باشه
🤧
🤐
🫤
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81505" target="_blank">📅 01:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81504">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81504" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81503">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تنها اپی که سپاه و نیروهای نیابتیش میتونن آزادانه توش کار کنن تلگرامه</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/81503" target="_blank">📅 00:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81502">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ این جواب سخت ما چیشد خوابمون میاد</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/81502" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81501">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQofxBGhtmK9-1DIlQIIudWcPiI9BdtONuxpFlogm4ecWav82sY2eMPWnlMKZKG9gtkFkmG69004vf8P-aqKG5xxbSOqoGLIzHVIYP_GxeQgSzzXPJq0fAfhzTX3gf18WgOEOW_xeQxwxlB-G6pU-yOoIg1IrIZHXdVFErjW7P74sf3ygGagrvrTED6VScwC_wdvsCylVPB6JF9OUdgDYcLQ3Tsb2wY2ElMLtTOy-Buxvury0nkgpkXdInXzWXvXeAS7x1BJFvrZbFo2YkOIRXJkgsKNaPZAQTrfRqtQVxlrzgO8vs49mlW2UutJLFQRWNFshGcPpVbfRKbdT2FmLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دزد شدنم ۲۵۰ میلیون سرمایه اولیه نیازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/81501" target="_blank">📅 22:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81499">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نتانیاهو امروز با رضا پهلوی دیدار داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81499" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81497">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2gZg2-3ZCvYRDazdgwG5RbPa4bs80GLozYLupqm3pPuxbj4BbIh4Nzd4uxS2uPpojeNm9udLEqcYX9jXfwoN5iPrj2p59dz5WuQLlSmilHLy0cqjkxIhHxH6-588IS2Wz60bJ4MEjXtW-xgReMOglb6Dwjcby00onng_Z56zeMPkxqMFm6d3NUB_1fH3xKhEmCo26K_Iezyj3_6aaMNzzFzckMqLmnt40B2OvXG3AWGnOnPKjN9WIpTBsn5busGS18JBOoyE_ie7BRsDnJ_qvEe9Z1ESknnRjb7VmI1cPNzDDrpLKs-TNzZbMa63mnFDd0AxImmw38wu0OqDrIuQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام چه بامزس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81497" target="_blank">📅 20:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81495">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DD87Azx4hXo1veEvADpsES6F2FxnNGBvKAafWhSkDI7gJdp2fkL-_I0nMIwq7Cq51W9FaZd8BwABSyh_1HOMBnElteH2fZVXWUFynEPRev_DGhWzzKSgYOzLI3d_2rfr7cKHcMb_Gt-R4BogvV_tb1TFow-siRcdsXOZrVk2N7PfgmcjOnQTAiidDtKAoDXI1S4fLsrkq_9IUlyRoQeO08_gkH4gsL3PFZ9WPEitfWZZYyUuFOQIxpIf5SbEBLuTMmSvpmjHPK26g16U2j2zkkowvLKU3J0s4h3bsBCHSsIZth6AHPRGkh6p3iFM7q6YkffcocpfmjkpCPzdt7dvUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی بچه اش رو دوماه زودتر بدنیا اورده با عمل که فقط تاریخ تولدش روز رند بخوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81495" target="_blank">📅 20:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81494">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlQIf0KePVNem78B8qLKa1LoVoZez4GiYG7n2_2H8JFPYL0trMw73qzkTX3arx60_kiJ6gQ93iukd74dV60k_KzHWrZ8ncM4kUoe9HPfrwYHcyvwdCR8W-U8-Qel_f7MioZMeGL2DZgB1PNT3ZRigBLt6YmeyAW9lzfHVZG0NWzpcCxrYVWzZFLhTBZMncZyQSt092_p9Un0ZzvqN4UZ6kpbOyUiIYKCWweCgqaP5RMzs5D6RNNTtJ4SWty-ROF1g6FBJWGZSQfsb2ySdLMdMmFAnm5R8kUq7jGyWgD-FK8ncBns7JAmQsKrJZw9ooDKJRDfMtr_IPrhF3NiE4pdjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوتیسم پسر کوکوریا عود کرده، بخاطر همین دیکه موی بلند جواب نیست و باید ببافه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81494" target="_blank">📅 20:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81493">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پرایم هیچ بازیکنی اندازه رافینیا ۲۰۲۴ بهم نچسبید</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81493" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81491">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">از وقتی تلاش نکردم برا باز کردن پیچ خوردگیا هندزفری سیمی کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81491" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81490">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پول ایرپاد نداره؟</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81490" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81488">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCa1Nd82uMzqLfPdkPsTeIbm9BLPl5fgRa_-n-hhUT7nXgZq2dC6B-mo4VxHSG0tKGl-u-PBAlCyQe4knT7W6yXoHEMOrfLjzHXaM1-NsCU1E0l6d78lhK3FnUgNONlXUsnNB1cwMaJoVOuybMk4qwYkgp0sMI4CeutaD2ismCXruC3jVOYr-hRliwuJ94N9YBS6VMfxVXrKfYtx4aj_OEfqAK50l5Ii-OyMwMPa9L4mGJbl5NW3EvafID8fR2MaAcfkwpo7Hvs5fSUTWtUUbnOrmX9tVyWLIjURhlJtl3BEuq4e5csrxeILJFK19_XgarTJXfEXx5_cSwLjewTJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0EUg6LdEvRJBlgtUD54GB__TmlH_QSaN_LdcgUYSAclMtJihDJ0UzcuRHNNR14IuRxxfUaF9DkumZ3k2Cm8ODAcaV226SsA6pNOTz2IaQECpQhM5Ijkw1mOdTFnToaAa-sldC6AXfZXeK_NN4bL9RNu4Zlkw1MAuzKbFlsQYFEPEkNzq1JwDO8VWdBE094k_JyjtiF7RXSKsspv2zDPBSYdK47JCeg_7V75rPErBUvBqgW1x0rHiUUyqYmjWcyPal6Osz_1PzZGsvQWSyjnq5SPle_z6U6-MCgoejX7_mmZjXIab6w7bu462lwOuPJ50YC3PpSHw0Xq2t1XIQ3RsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رافینیا شبیه زن جنده ها شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81488" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81486">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkK7W-Vb6mxAHk20XBXDfSO0x-Si_RnC0M-L91v5M8Ty-DMMcjfY9dw1uYXDVcLKOAQkxQZjkDRfHSfhhS9K8JtCRswPtsPyd_HfqPxwh_fE8Dx3sSMuIJ6fnlZykdNnmWkQBhHuoR1et5_9_Lpmyk6hmJIshr0Dmh4vUXJmMNpRLPqlw8eUWIXclkeare6m89NwrYYGnJxR1IC4VV4gSE0NMMRwxhsv7e0tW5YHvv9nFp0oPFKsxrgQ6zC1qLjtNU1i8A_yHwnY2kgPJ6G-SbBnue8SYMLzraMGV0VHsu4c8CD_XV7Xr3VqueoF-R4Heogl9seEBHXNSmq1kByBAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tXu4kmehMoGiuByIzpx245pMQRke_8a5eesnCKYM8MdliNCY9wDt_85nfyxynSJFVycpQ-LVgyAiOA0fuoAIhhC8JhuZOsSQsPRS4rjizXXnmCPfu0v6YDuhv6SXLRr_hDYaGGN9I87d5XVa3IkCuYYbLyxu1lVqLYlvylYHmo6Ay-_rBcSrGBch0gJHimgBt6RslCgA8mtJhtx5J79B5X_yBb6WzasuUA4_LC6pAvRq312AKovc5j9mUDBSl_zww-Ll04XEPDpI4b4cYTxD7EBKdA5RWTlldIWlzE735oJZSiDFnpI_jdDVzTJwOS5WXF4bexJirqrXrAEzwIX_Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرکاری میکنم نمیتونم با قیافه جدید وینیسیوس کنار بیام.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81486" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81485">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0eCmSJCbzycDCmnXOKZcbxXYoSmT6DfSX1sNwdD-SGBTOkfZkEdRWK_XpTJggEXQ0w2yVCm_gLb6daBD1oeQEnGXRJiRIX3-bC72n57MMnMc79R3iDiEnpU0x-rLy4aNn5oeioSY9D1pukNc-jpuO5xpm1bertkS8l2sIL4ZeIEUKrR-WtUzh1HrjBi-UE69aiTTVDbWqc5EpZOFBHKSBetWoYFsCf7FPu3E7BJ2TBqQn7M-i53Rr_dTjWGcw4_FWg5oHS6ku10gvx53UGC2wu7PChJbPyykjFVszKolcUJv5pbJUxZaIEg6SEKv-BdmNVXtSddEFx4TJ2U5bu9ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81485" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81483">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9qS-5E2il3C6ON5plEX54euOQGEEX8IiB15O7ei2g1yh3ka479OYFiaK6mfUpRDb9nGie4c0Rcp329kVkQjJa-1xnbe3AiL01T3fgkS6jhEUtaQqAkXoTvGjGQVNlTXXh0L9ARYJwxv3PUE-0w_P7AghAseWAx4OiVgARF-Ba9YjXA9Q31tn7tcKEGofRWVpEY4GUZ0r7heHglDjHzltyRy-ctpJI0dIXTwEddNaH6rxIeOxs0x35SVzddh1i-HzvCJN83J74gp71aFavQsX5-0buXGvyqyl27JCJdgWQlKE3S09IMm53ApafddWbqODFXGriDh7ZkBEIyZbrKgsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس جدید صابر‌ ابر و دوست پسرش.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81483" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81482">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZLBTxrHKJIuU0_w9AGtdz0833_GZC_KHXQSR2XFKOiFryCWBEHwmDBNG1wGu19wIzelZdCpRQ5cIIZcaga0ZuizAt_orxYnSsblXUsNzlDpzhnWGehhKfE-FypY_3W9vWy4Y6dt4sHCgt7PNYRuqji_cV1Rg8ZoZPnZvaX_pAO6V5lPbrqgPoy9e51fUbLWoD1dFD9r_rodH_UuH4fz7w_yqcsRlExr5bvy83tZz4LehxwVhwHp4lhxqIzksyef9DG-PXipLFYTF8ah2WYuln0QAqvPxPMnhEkfRI2W-lYMPiXGuJkEkXHR1iIIDkKXUD-OCHyR9O0_EHxFN_fsOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81482" target="_blank">📅 18:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81481">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKiIGo0L-bAV7LdJALQx1zB7_3_qQIOd9YpJzDPUYhmnFfpoDlXtsEK6d6ywQskNswEGnc-T_nVdRWMdtt6vMXMdqJ4e49Cxl1bbCXfzdhRlB-tVnGc-MD3MApQ2AaxUgpW9t7FESWsuyT-fytApZdkQy868ogN8bq3xxTf0rjrFaUfwUUZ6lC7Nxw2hh9D2xzy9Ft-c-IWNL3ZtgLxMGywdbbJXlKfghZFEIKPgK2V2MdEwcHGzgIO-mKkdWzNlnvCbck749HEMT6JdVP8KKw4S3Kw2f-WXzxQWGeZiDml5SGTbY0d0b8nDG833tOuOaqu8UI4WGlX1cSs9KXYz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش دورف:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81481" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81480">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81480" target="_blank">📅 17:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81479">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIUF258Vkpzma2XEfypJq89xJeTpndwGLNcogD7wuTnUBkuirXrjSNCwEwaUaHwq0_iyYDPREUiPTv8dJmnd0GoEXzkRaVKKOoVOo_YdGUAwOttNdEhU3EjVKBXSUQEkAVf1tLRl1jwP0TwFFhyHLq0BgL5z6jKAWqoLv8IJPi6hQZYeFzoToVVt2by957EFga6RhAyNkv4XMxl8BUcIBZF8cMg5ILquNVfGznsqybxcFx7Y0AfewNKMHyTLJVRZ3DMmye24gcmJLR_8Te4Q4chLs-Rc2HFnE6spWwANceqWr9D5xJl5qv9RdbnxuY9IUf5Asf-MJgzcCQodmWbJ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81479" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
