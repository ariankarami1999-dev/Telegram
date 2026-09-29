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
<img src="https://cdn4.telesco.pe/file/B2g8qpBPbOZbGgIEA7yodNbMZg4prkUUAeC9QXOkjivxfkCHT9Nc6eK5CwE0ybva8XB4N3agcRYRzlaAe9t0IQkgxkS9nTmT5HhF25D6EjgnbT91HyGuQNCCYf7Y1AcFLAHPEwm0qsRGQm6pDatlTdMZ5V3jhSAuClSczCbUMZtIhVfNwAepEA2ePUtKBrVEBPwmc6YOn_fVxgJO_IrFrz7ltvW48n-6N_bdTl53Ml0AX9KosOfKAhqJ3TnFZmGLwEpnQ0de9f28XXu0NOmkQ5aNz7S0gnU_k2C6wwke5K9_4C4E2xyDAtjCGyBqxeD-LMYG19JPPMAdhIveLtjLzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 251K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 23:34:57</div>
<hr>

<div class="tg-post" id="msg-84204">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فرمین لوپز تو کیر شانسی میتونه با ما ایرانیا رقابت پایاپایی داشته باشه واقعا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/funhiphop/84204" target="_blank">📅 23:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84203">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پشمام از یامال</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/funhiphop/84203" target="_blank">📅 22:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84202">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-_fjFytvuqIzA2YJ30Rwq59zxDAfJu1sZCDjNhH7GZt_kpnceDm8trwGsTwsL9zdDs1HXgQkAedHlcUibpIr4PSgr_xlsPWRjj_VSKGC-X_y-LDy-TNG8BmzRKKI3x3btjtqhv7BtBhxnyeCNYsxkLYsV5Df1bM71W46DGGf7wcw8zn3AmFIFp7xOsKS2Gc2SpIaS3on8-Vm9SpUwDhNq28krOCc8p92kihQF_dQ-1qcv3Gx7l1IWUKEoUdxzsI_Qn6zbqCIXIw_ycGMSV1p56amlwIos8whoq7k7ADqBL8-AFfcG5nWw0h28tVnBHeTo3bBIKbW9Sw6tJt37n9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز همزمان با پلمپ شدن مغازه های ربکا عکس دوس پسر جدیدشم لیک شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/funhiphop/84202" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84201">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گیگی 2 هزار تومن
🥶
بدون محدودیت کاربر و زمان
🔥
- 10 گیگ - 40,000 تومان - 20 گیگ - 80,000 تومان - 30 گیگ - 120,000 تومان - 40 گیگ - 160,000 تومان - 50 گیگ 100 گیگ - 200,000 تومان
💎
- 100 گیگ 200 گیگ - 400,000 تومان
💎
- نامحدود (1 کاربر) - 150,000 تومان - نامحدود…</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/funhiphop/84201" target="_blank">📅 20:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84200">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bl79nM-kdcZ_zqGkKmaGcMtp7D4N2DsYxxPXNkqc36JXbaGpXLLBWRbL4y9yZWLAIQ_S-hyVkUoJj3dJMg3JpiOrL9CRQdJWmeCdm6PkjgdXym64yorilwkCIsr6Qa4CS9aJO9tweP0Bm3bjRg0a_2bu-4K-BME_Do8mPaZEXSi40H-V1BwXIN8Oo00U02FsEGckvttBhq6DD7bJ94EzlrdFTfNVTUNd2CkiDQuh8sKLalUlcg3Q-4dFQw-jMZoSKrY3MNlojVitkc2ft2dof83CPaG08K8Sl0JwIuVAUd7ACLU4Vm1__9VIWyfzqabTmYsNCPd1gvZjmuisvGPXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گیگی
2 هزار تومن
🥶
بدون محدودیت کاربر و زمان
🔥
-
10 گیگ
-
40,000
تومان
-
20 گیگ
-
80,000
تومان
-
30 گیگ
-
120,000
تومان
-
40 گیگ
-
160,000
تومان
-
50 گیگ
100 گیگ - 200,000 تومان
💎
-
100 گیگ
200 گیگ - 400,000 تومان
💎
-
نامحدود (1 کاربر)
-
150,000
تومان
-
نامحدود (3 کاربر)
-
200,000
تومان
-
نامحدود (5 کاربر)
-
250,000
تومان
🧨
📍
سرورهای حجمی
بدون محدودیت زمانی
و
کاربر
میباشند.
.
برای دریافت سرویس تست و خرید کلیک کنید
🛍
🆔
@VintraVPN
|
فروشگاه
🆔
@VintraSup
|
خرید اشتراک</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/funhiphop/84200" target="_blank">📅 20:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84198">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یاسر بختیاری در یک لایو ۴ نفره اعلام کرد فیت سه نفره او با رضا پیشرو و tech 9 قطعا در کمتر از ۱۲ سال آینده منتشر خواهد شد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/funhiphop/84198" target="_blank">📅 20:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84196">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بر جرعت میتونم بگم رضا پیشرو درحال حاضر رپر هایپ تریه تا تک ناین
و رضا پیشرو انقد هایپه سه روز آلبوم داده و بعنوان یه ادمین رسانه رپی هنوز گوشش نکردم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/84196" target="_blank">📅 20:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84195">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یاسر بختیاری در یک لایو ۴ نفره اعلام کرد فیت سه نفره او با رضا پیشرو و tech 9 قطعا در کمتر از ۱۲ سال آینده منتشر خواهد شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/84195" target="_blank">📅 20:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84193">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tguMdOZveqBjPq2gfKrJ00m4_uqViPK81y6NeL7UxrCI5-Ul6UwyhGSmWLgvbD6GHmbqD1-U72ndBZg44wynz73EEVRbAkXqjiAYyS6HZc9o3U-Rmd_vX7yQXDu7HdWFWFbuR6ERVPRD5ShESqmFS0J40-fyb38mS3zlhx8XBYay6KDlqYOuCQLgryTi4DBiOVNxc28qcKqfidmBKlJ8xM2AfeHBUNPY52p2Sz0oQReu9ID4iegjcV333alYpuONkCsJS0NaqR2l7ZqaYb22iqaPK0yyEbvRJJ_X4ee8hlk8YSlcnhkWjG021SSaACWoMmhxMXzvY3MKDaBy678G5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا باید صبح بیدار شیم از شیک زدن زنمون فیلم بگیریم بزاریم توییتر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/84193" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84190">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سیتی محکوم شد و بزودی حکمش میاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/84190" target="_blank">📅 19:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84189">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfSR-boixScPlwen9McCa34o2DJxbbmIoF-jc2e4dm_IcnjEPEK0VN7xR9dPLpcsJvh0Uk5K3uJsKxzp28JPSo_SK5gN9WqjN8BXxZT0zVMHc0lot8_IalH1ICgXrtI3sRSyCvfSs8-pWC5-R_3KFFEmQeX-lVp5lqPAKKrKOgWHpcV9ZRT6npEOtuNfNawuhQosJZfitYUSGnVHqPE9U8jN6r9Z8GqJWNwbryJyBYPAVOdcHWWjq1rspfRkX7FhOSeJOzDlUcm58hM3iwLUdov2hbS2MWZ7DPROevS7TVy1Og15AcMk6lar2MNuObO-DS07HbVjsOUUp6kigV_msw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید آرون و کاگان به نام "انکار" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/84189" target="_blank">📅 18:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84188">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترک جدید بهزاد لیتو و بیگ شگی به نام "1.6" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/84188" target="_blank">📅 18:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84187">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udlPWh5c-TZjraFKua5GVggXvwSICsDk0ImM-wo5qpkasoCudGALdj7wJBflNlXYEprAo0bFK8jltHW85WiTJhTfEwE7mb_YTJhADkbwJbmz420JS3bR4y40_AIqelG6oK9oEci5gT55-1bXHWPkQoZE9Ac72sThYG7NIhxeVRkqUlTQ7mojT8nq16dnD4oRidwrRfeoZd0rMAKgh2ewpTN0eeBWhYmDBqVtiiFarWHTCIjOw-MvE4JzrrqmHWpu47Ww0ei20Hb_6dVdlojwxOAlrcxplqjtI9Niz3HwssaahXTQqREP9gBnGNUrrMu5FxuqWIvUKDrGfdwYpGN7oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید بهزاد لیتو و بیگ شگی به نام "1.6" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/84187" target="_blank">📅 18:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84186">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4Pz6UITZwjxvHgmW5davWDS6pneLB8wjEjTZzjJgXp44Xe4Lt4vGnHge0L9c6cKBDcP-mzrlzW1KnxLKokM9yUribl-R9dcRDsnCXL-bUimXkWNIeqR4h5mCeMOiyyTE_s1YAMuosIUJwAFLrC5djGtg9yfW9lSF-vZxoE2F8_Bl2POm3L2Mlh_-w8vTNvK0z1mhA3vSK_w1YSKYA0tQZozfVW7pg3c6gB1jWIUbOf4zTfW-X__AeAPlubOOKmAZuN8TbldwELZe0kKuA-b1VBC0aMquOX929-XChYncQOvHJnLva5jKTxzHQC_ir2G65t61sXcJjCI4H4SvQWPrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاره شدم این چرا اینجوریهههه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/84186" target="_blank">📅 18:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84185">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862ec698b.mp4?token=dt78gj6XlN0EUM5xAmpOIIJzvVg0_CQs5f8FWNWw7-AI1rtoizDcqax5N2rz2UqxqVsD2G2qoZw-PE01qdcqAR1iD2YUlw8t5eJtCnZ8SVu6UnODA84sO6Zpu242WwDPk9TQyVQ2b0mBJtvIST8IXBR8GIu3-vZhTLKTQT30n3PbYLiKpqJGNWV-Icq9VhGOharFHXvZxBOBPTImf61RkNioDlzyCoYKXi4EJ61GoAeToUDj09dnGL4saeG0MaiHAr6W6yLYSGsXNVAhs3myt7B9s1qslbfN8_dP7euRX2gI_BQjPYQ27W2HNpc3q9C7UfacWKJxahTbxfrR8i23Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862ec698b.mp4?token=dt78gj6XlN0EUM5xAmpOIIJzvVg0_CQs5f8FWNWw7-AI1rtoizDcqax5N2rz2UqxqVsD2G2qoZw-PE01qdcqAR1iD2YUlw8t5eJtCnZ8SVu6UnODA84sO6Zpu242WwDPk9TQyVQ2b0mBJtvIST8IXBR8GIu3-vZhTLKTQT30n3PbYLiKpqJGNWV-Icq9VhGOharFHXvZxBOBPTImf61RkNioDlzyCoYKXi4EJ61GoAeToUDj09dnGL4saeG0MaiHAr6W6yLYSGsXNVAhs3myt7B9s1qslbfN8_dP7euRX2gI_BQjPYQ27W2HNpc3q9C7UfacWKJxahTbxfrR8i23Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی چوپان: یه ساله دارم کابوس میبینم؛ باورم نمیشه دیگه محبوبیت قبلو ندارم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/funhiphop/84185" target="_blank">📅 18:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84184">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84184" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/funhiphop/84184" target="_blank">📅 18:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84183">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxZZqxLBDM28LFfnUKl7i1if3nI-XvquDSBiA53WBdDIO2hpkGQmPjKFR1LE84F5dUVXOXU91TESy8QxLfwlRRrsKAKcqzTD0HPJtfcrDN4e9ucXMLbnFXWBel65_srXl0G08W4x0YNyEAe6ir0ZvFLgCcv5tBLb8XXcjFERsFEfqBX1hHP0QsOR7-1aa-ZQ8ZvUQVOcCvnY_v_AUlzo8EJd0S8yKdiqFlS-CW5UI-gwfeX3psRCExiGruLXg7TVl4gW8OIf8KRstJrkb8Pfo_E812FTaYf-_BeZaM-Qe9I9QdbSYQazF-oLKd5woomAXG6RSYq-y8NbtVQDbRiFdw.jpg" alt="photo" loading="lazy"/></div>
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
g7
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/84183" target="_blank">📅 18:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84182">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ادم اخه طلا رو مجازی میخره</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/84182" target="_blank">📅 17:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84181">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">معلوم نیست کی خورده ولی نزدیک ۲۰۰ میلیون دلار اموال مردم تو میلی گلد بگا رفته و هیشکی پاسخگو نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/84181" target="_blank">📅 17:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84179">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf73bf24d.mp4?token=k3sGGbOBvN0q5ADJPowy5E7UzV4l54BeAGtPFQGERije3PJTknfNOD29yuR1rfStFDtVl-btoBvG2U8Lp3eldd1YqkrDI1CDIXYdFzN-R1xk1vDk6niJTnPCvIOJ-pFOW2-vZaW37SAhPy4JypLkVOZdZHEbNKyJo1JNrXL0U3Epw2ftNjjcW4REj6LMmQ-boHDIN_VAFLp9kBvIWQ2Acq2vEfDGLOqA9dcXqfUpxYasJehkyc9A2HlXMj4t3tQYy0lPRaZ5HHLWGiMbQVElQLg5OzUL6_J0J5zmnp-FXQAI908wXKlqh4PgnZmL8IRJXBtwUQboW-4G_ieCL7Csxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf73bf24d.mp4?token=k3sGGbOBvN0q5ADJPowy5E7UzV4l54BeAGtPFQGERije3PJTknfNOD29yuR1rfStFDtVl-btoBvG2U8Lp3eldd1YqkrDI1CDIXYdFzN-R1xk1vDk6niJTnPCvIOJ-pFOW2-vZaW37SAhPy4JypLkVOZdZHEbNKyJo1JNrXL0U3Epw2ftNjjcW4REj6LMmQ-boHDIN_VAFLp9kBvIWQ2Acq2vEfDGLOqA9dcXqfUpxYasJehkyc9A2HlXMj4t3tQYy0lPRaZ5HHLWGiMbQVElQLg5OzUL6_J0J5zmnp-FXQAI908wXKlqh4PgnZmL8IRJXBtwUQboW-4G_ieCL7Csxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خارکسه حداقل بدون لهجه فارسی حرف بزن بعد بحث وطن و وطن پرستی بکن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/84179" target="_blank">📅 16:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84178">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یه زمانی خارجی ها مسخرمون  میکردن بخاطر کالا برگ ۷ دلاری الان چطوری بگیم  شده ۱.۱۷ دلار
سخنگوی دولت: خبر خوش دارم اونم اینه که الحمدالله بحث کالابرگ حل شد و از نیمه دوم مهر کالابرگ رقمش میره بالاتر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/84178" target="_blank">📅 16:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84177">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">در همین حینی که قالیباف گفته اگه ما نفت نفروشیم هیچ کشوری نمیتونه بفروشه تو ۴۸ ساعت گذشته ۲۲ میلیون بشکه نفت از تنگه هرمز خارج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84177" target="_blank">📅 16:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84176">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvNIQN3aS53vUI64aoC6KYa31wTXinA3X2ETLBG_oO3IHLUZSwRgymmJG8YcVc2gxSk8rWOhUcR6Kz4Q4CMHbEND8TOuszAiOtQnEZ5RxYgxYbLT4p79QClWIPYyJY-DmcJPrXlBVCVufl7bJHj8G9FIKNH56SwOJuLH4H-JneSgrXMCGwZaJ4OLRgTpRAAxba8GXG-5K6oCC1-nhLreLVEtCmOqG7oqh0V6f3UN2kdrEXqeY9NyQ4P_SaOlhpsGBduUbB5t76Cuqe8VUW3E1xO5GS-z9wOaJkmtpFroDD3wvPJBTkD_YCkh3fMKa3cCn9iLpkazA9_tL23uQ6mHbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار دیگ ترکراری شده لیر رفته بالا ۵ هزار تومن انشالا تا اخر ماه دیگ ۱۰ هزارتایی شدنش رو جشن میگیریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/84176" target="_blank">📅 15:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84175">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تو این دوسال آنچلوتی که سرمربی تیم ملی برزیله بیشتر از سرمربی های رئال به رئال خدمت کرده با مصدوم کردن رافینیا   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/84175" target="_blank">📅 15:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84174">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آمریکا بعد از تحریم کل خطوط هواپیمایی ایران، الان فقط یه مجوز یک ماهه برا پروازای ایران و عراق با کلی شرط صادر کرده که توش فقط می‌تونه مسافر زیر نظارت کامل آمریکا بره نجف برا زیارت و باید از همون نجف هم برگرده ایران.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84174" target="_blank">📅 14:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84173">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">به کسی که حمایت نمیکنه ازتون فحش میدید به کسیم که حمایت میکنه ازتون و بگا میره میخندید
واقعا آدمای کصخلی هستید</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84173" target="_blank">📅 13:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84172">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هردو فروشگاه لوازم آرایشی بهداشتی ربکا قادری داخل ایران پلمپ شد و تمام اموالش داخل ایران مصادره شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84172" target="_blank">📅 13:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84171">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDCSrTO59RIujVOvfmXYvaU2nSF6qAPr1MsAhUCJ42vLa9JEosgd2neWvBXs-wpxFnoJ38Fei_eZYGx1q9UtbUUNL7ThM4ALp3-QMb7ouai9SzeBhw5dKPclJuHeVIqgwqc6nKX8KwMxv1cVi0O1jFUGc9zO7I0JXzUDdg46GLLsvWnu7drGsbkBKrNcqgG6BOhzFWWznKuynB7mYerKLOI7AUFoAU4bSTkwbJLVS4inN1CVcimnuAXRS_b6-lFdzJo3wd04xp6js11T4leL8_ubjucSnjUrc1thsfEKrl0aQLmSAebeEMzBcMm520L79eKYVM8n5pbGww3NAtOO4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هردو فروشگاه لوازم آرایشی بهداشتی ربکا قادری داخل ایران پلمپ شد و تمام اموالش داخل ایران مصادره شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84171" target="_blank">📅 13:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84170">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
مردم آمریکا تحمل کنید کمک در راه است
سپاه یه نامه زده خطاب به مردم آمریکا: حساب خودتان را از اشغالگران فلسطین که خواه ناخواه باید آنجا را ترک کنند و به کشورهایشان برگردند، جدا کنید، ما می‌توانیم همزیستی مسالمت‌آمیزی با هم داشته باشیم.
دولت یاغی، کودک‌کش، شهوتران و بی‌خرد را کنار بگذارید، امور خود را به‌جای اراذل به اندیشمندان بسپارید و به آنها یادآوری کنید که دنیا عوض شده است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/84170" target="_blank">📅 13:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84169">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e6ffd31df.mp4?token=UW8OzQLvXAnpAXjR_mUCfwX9kAlM1NVxwWK609wsbZbWHUVcZSeRKZFPxZQktEhtW4m-riTWRT9CmFueZbdHlxQWffgENHZ4Kud_RuvX0gV8egKKNYy3dX_MngwJPNyioVbJr3vPg4oqtSvd12UE666K34H3ME8oFh59p4WJQ58dxczjZ-f7nRajOZz4vHyqQLjKs0nodPE6dc_XmR561YzXXrPuhJuPE21-6ezy0IIV8qokG6pK4U5mvVItjlZMBHdpZBBg9bFVeRyavfV9VsRo12XdPl6FXx39gcaFHQPtjjXSm5tQSDhRvRtHom4LOlhhcpFZAW-ReVzwjwKrug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e6ffd31df.mp4?token=UW8OzQLvXAnpAXjR_mUCfwX9kAlM1NVxwWK609wsbZbWHUVcZSeRKZFPxZQktEhtW4m-riTWRT9CmFueZbdHlxQWffgENHZ4Kud_RuvX0gV8egKKNYy3dX_MngwJPNyioVbJr3vPg4oqtSvd12UE666K34H3ME8oFh59p4WJQ58dxczjZ-f7nRajOZz4vHyqQLjKs0nodPE6dc_XmR561YzXXrPuhJuPE21-6ezy0IIV8qokG6pK4U5mvVItjlZMBHdpZBBg9bFVeRyavfV9VsRo12XdPl6FXx39gcaFHQPtjjXSm5tQSDhRvRtHom4LOlhhcpFZAW-ReVzwjwKrug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#شرمنده_بابت_پست_رپی
به نظرتون ویناک به داریوش چی داده که داریوش حاضر شده چنین شاهکاری رو خلق کنه؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84169" target="_blank">📅 13:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84168">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تو این دوسال آنچلوتی که سرمربی تیم ملی برزیله بیشتر از سرمربی های رئال به رئال خدمت کرده با مصدوم کردن رافینیا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/84168" target="_blank">📅 13:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84167">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mfw5-QTJrVRqglykazqEIipyKuXVkkMmpREFZBF4mfIuYnoEvFzbgn52qTSvYMa-7tksdzlf5C36GLb00ErjOJel0xu4sUZm01oW_dXn4_L5z_wiCIgjTfbG9o0QckKPrqxvahl8Gd_H8vOLU6EXvMzX5U74CCw5J0hrQS_JUDvRIzZkSmuc3Vsl2CPsLrINHPcrKUpsECtxIgIswASmPF9Uc3cJfCAPLTzlGzadHFdSN2fdsDhdfMpsPI4vZOpxm-YzaCPlfQxhk0aTaQhEkAtHNoKpOdG5tpvACzfDyFYpbEzJJIyc4h7vurJwwD4K8A36-c_mTUQhKIih3z301Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو دین یهودیت چیزی به نام تغییر دین از دین دیگری به یهودی وجود نداره، هرکی یهودیه باید تو خونش باشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84167" target="_blank">📅 12:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84166">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84166" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/84166" target="_blank">📅 12:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84165">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBumJgzxc5h-haNafgKnpCVnk3h084v8H1e3dRGxUhKzA5qvO6OWFB9PUWfRNP4amfNK8Bqo4CQtP4nuOSfSK447wQMY8I2R9QMAMmpZx77zsvwn_oiO5HENFyB3pR4hpiUVZWqx44-AlRjA4V5F58nbRC2pMNJRV15qI3zx33Xab10jjhV6ZTXd2RD-m8YLLPzkh9sI2t3nJ_4stLpn0r2HPaVI2W7vzp2pu3w2_-K2ZBuBjiaG1lY-dIdqx1yRsPkvEcrHokg4TIqlFMER0lFMbYfk6dUEauRHOTlo2_6H_xSF1Aiv3FwUxB9DY65reM0k02zr4ln-8ld48d8Abg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
نبرد حساس یوزها مقابل روسیه در دیداری دوستانه
‼️
🇮🇷
ایران
🆚
🇷🇺
روسیه
🕔
ساعت 20:00 به وقت ایران
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
r7
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84165" target="_blank">📅 12:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84164">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سخنگوی قوه قضاییه:پرونده حقوقی ترور سردار سلیمانی در دادگستری تهران تشکیل شد که سه هزار و ۳۱۷ نفر شاکی داشت
رأی این پرونده دو سال و نیم پیش صادر شد و بر اساس آن، سردمداران دولت آمریکا به پرداخت ۴۸ میلیارد دلار محکوم شدند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84164" target="_blank">📅 12:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84163">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ما میگیم اعدام فوری بیرانوند دور میدون آزادی شما میگید بره سربازی؟</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84163" target="_blank">📅 11:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84162">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/398fe520da.mp4?token=rxxQyj7JwOyk7fX1ihdlr4PY57f919_lzLZFL1m7ZINmjBknf7eio9jtfM95_b74ZNcAtLbULPMQS7uxUYkIQQVowr5peVWO0ABzawOMMfluKUefxbxI-0scN884PsN30gWg9H8blIrEWN6Xs25a_qQfG_aGDTt9o0U2VgqE1GV74ttXR75Fk9HOipLIrouNKUxM4bI94ST4Yse8LDMVB6tfVHEbaAntHM6ti33YZIDgF2xIW_ruzXHkBDzW9K94cknk_peJPJAOzTu-3P1bIVGic5KZq6zEDiXi83JK9O0_1Matq8BYY-7QumCQGnRJCnUFP5_wW7bnCaWYJe7RrrUFHcK_zX6XFIAUjeVmqbhlaSuZ2VshiWgnXdFTgf0WnLT-Ls1-PioHmg4lH7bcMF1YPfK2tc8VmjZLTC4_3aMafhzBJfr7HowaXQrECVTgw0L1SDf1XgS6TStwKGv2w4J4NmqDPmq4OEt7K8Bt3rl5pulQFHxdImb__mktLuz0NsUvXZLNixdanev6OC8BqM3hnoKOeeh_2jKO8zDz_SLCKjd6JwsrlXkAFpsfpxoBgQczQI87WfgMighnoNKO-MrzmdFnet6qhCTgCR7UAfOdhXoVBsvKINWAGD5jMsmkvzXIc0hPH9lmnpCMtZsT7t5mS9Wcy4hafo4PmH6mpbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/398fe520da.mp4?token=rxxQyj7JwOyk7fX1ihdlr4PY57f919_lzLZFL1m7ZINmjBknf7eio9jtfM95_b74ZNcAtLbULPMQS7uxUYkIQQVowr5peVWO0ABzawOMMfluKUefxbxI-0scN884PsN30gWg9H8blIrEWN6Xs25a_qQfG_aGDTt9o0U2VgqE1GV74ttXR75Fk9HOipLIrouNKUxM4bI94ST4Yse8LDMVB6tfVHEbaAntHM6ti33YZIDgF2xIW_ruzXHkBDzW9K94cknk_peJPJAOzTu-3P1bIVGic5KZq6zEDiXi83JK9O0_1Matq8BYY-7QumCQGnRJCnUFP5_wW7bnCaWYJe7RrrUFHcK_zX6XFIAUjeVmqbhlaSuZ2VshiWgnXdFTgf0WnLT-Ls1-PioHmg4lH7bcMF1YPfK2tc8VmjZLTC4_3aMafhzBJfr7HowaXQrECVTgw0L1SDf1XgS6TStwKGv2w4J4NmqDPmq4OEt7K8Bt3rl5pulQFHxdImb__mktLuz0NsUvXZLNixdanev6OC8BqM3hnoKOeeh_2jKO8zDz_SLCKjd6JwsrlXkAFpsfpxoBgQczQI87WfgMighnoNKO-MrzmdFnet6qhCTgCR7UAfOdhXoVBsvKINWAGD5jMsmkvzXIc0hPH9lmnpCMtZsT7t5mS9Wcy4hafo4PmH6mpbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با یه پست رپی ناب روزمون رو شروع کنیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84162" target="_blank">📅 09:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84161">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">صبح دلار ۲۵۰ تومنیتون بخیر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84161" target="_blank">📅 09:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84160">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یسری رسانه میگن عراقچی قبول کرده تسلیم بشن و اورانیوم هارو بدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84160" target="_blank">📅 00:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84159">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مادر ترکیه گاییده شد که</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84159" target="_blank">📅 22:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84158">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قوه قضاییه: حمید رسایی به بند ویژه روحانیت زندان اوین منتقل و رسما زندانی شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84158" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84157">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A394lCyQkbKj1KpmiUycfwtblj8V8fMAgA9QjZ3hftp1B5KcAzRbC_xgL-cl0k-AspwVfQTPTVJMMYht2V4Y8Di0OZuf0yyqHfs4qpFVQfHu3Kv6YpJ-OCzTR9HkBdXobLPydjWhi46rDaPnFK5q4YYZgw60rjL1OysR2d1_SGQgbOmPcFJUcWtQ8Hojx5OBzNBv6jHA8bsvlM4v1jTlFf5m2ENHZKbwp5hSoQlcogHEl6Ov6QgR69vlGRdLfb3loXCVAQRuTTLsLNOBpCY7zTEUgrgqj95VIYDhO5cMwUYfY_JFh623iW3UJavz6QslxArNm0RGmMLZLAdFByEvBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه:
حمید رسایی به بند ویژه روحانیت زندان اوین منتقل و رسما زندانی شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84157" target="_blank">📅 21:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84156">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BF17SPY_3yF1fMIz9TVr6lOBI6weWDQukCShWPPY6X_uphsn5zAYAf5Bm7Yi_mS-6RZui7-gcwpiOSIDgSQmY0BcUVKX73FYI18axi8-LizrcKhJkvRICa6wK8bgYAlh4NfemocLD8ittIzOaaTM-LaJoeYzAfAGNvPxyEW3PejFYZvOk_tM0881tfxIhTh61sIM89nSujhAvqKtHQN8O_3Fr-rmNMx1FRG2fK6EX5M6uvGf36nQ55gXS23ikZ1Bq87Oc7ZFJm6837bc1mPRESiS0ERz_KTQOpf1Oxa7Tl5DmOUGptj0o1ggR0P-IlD9gLXNhqHf7DV1Knp0ANbVBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من وقتی یبار تصمیم میگیرن رو فرانسه بزنم بعد عمری
واکنش زیدان:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84156" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84155">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oR-1eDZtHH3AhqZo5wctiutBS22cQPQmFmJ9TMs9cmEslZrJ1qTLUNfjyWl9fg81X4OcV6usIB2EocXmxvPj3-p-bbEQf_xX0Kzjb_r8U0pqmDkprPMFzA3ZC_WV_Cjussb_vHNHb1Abl207zYRTRuj9kxVSF1GPUTZf86uEZ0HfgYJ4lUEDPhKToLLQsTsBLIq2eXEbBUz2tnNxOm1_i9o6GkNdaSNPrJNqUAozDVjg4fVX7ivyimYFekvwVvh6UBCL8gTlmOo8qtumw-dRYohrPTqcrGI_50xh_DApenaEJ3SHbs9bGRxHrO_6vvjand9sXVIFv3rUqhNG1dEH5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلیت به دخترا
ایسم عکسش با زیدشو استوری کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84155" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84154">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بهترین کیفیت کانفیگ V2RaY با تخفیف و قیمت استثنایی
☑️
فروش ویژه کانفیگ های تانل با کمترین قیمت تلگرام همراه با ارائه  نمایندگی ویژه جهت فروش
❤️‍🔥
🟢
گیگی 2200 تومان
⭕
با تست رایگان + زیر مجموعه گیری با هر دعوت شما 10هزار تومان هدیه هم به شما و هم به طرف مقابل…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84154" target="_blank">📅 21:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84153">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3bE_8TSx6FgQSmHtTX6aQVpKrngo5F-Q8k2-yoW9oFQl4IQ6XvPbtrFW5CfaOM4bZXK0YjB0KfIpGvuSJAELs41n97hCbz_Dlh8IOtMmPL-Ox2BgFuGlkfOcOET4L0iG619tqVw_RHh8tdWW30CAtmk2EgEZFFkXjgRKVVxlwWCtI-mUdO_SBj6oXAvlNtP5fL2PSkXCeqtqBJ14I2tfZfgz9ne7uYCUqrxn21nrMwvOhcPZYt3j_Jngg9Zx-sXLTTSagu7kdgQpaB2wwbA7HsrityPv4CEcSBCY7CgsY_ATB_OzhG4af1Pi0MMp9zlNV1qjlGHcMeeCHJYsBkB2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین کیفیت کانفیگ V2RaY با تخفیف و قیمت استثنایی
☑️
فروش ویژه کانفیگ های تانل با کمترین قیمت تلگرام همراه با ارائه  نمایندگی ویژه جهت فروش
❤️‍🔥
🟢
گیگی 2200 تومان
⭕
با تست رایگان + زیر مجموعه گیری با هر دعوت شما 10هزار تومان هدیه هم به شما و هم به طرف مقابل تعلق میگیره
🤩
🔖
جهت خرید و مشاهده محصولات:
@HyperPing_VPNBOT</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84153" target="_blank">📅 20:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84152">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff9d6bc22.mp4?token=XrU7lhm7C9OF6uBdlcn6X7yCFzeTxcezZTOwUhPJ4-PqkUBEWylakkro4SfHQT-DFCPNW_UVpLwTz6tSDlt-NAKrWZHDmO-T8vmARe_yp4smw14eHqepPLA613CAySkDR1sekRFmwN6z8_sYFlDgmnoy5nnmqlAsg3NiGvtjpI9Z08BtZv5cdv0gtqgo0RWhuTK4pHKZASjp5-kLqyMe3aS4FuSANFsYCLvoKH7nsAKTWlhH2kUadK9_h0lXAvmVDL1WtTLQGXn9d9fZhp84hqc1bQshn2Yd0jvx8IaPGTIIPY9u9xuF3RYE9YUZrTQdumIg9CPG_-5Ohfk5Lm3R1zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff9d6bc22.mp4?token=XrU7lhm7C9OF6uBdlcn6X7yCFzeTxcezZTOwUhPJ4-PqkUBEWylakkro4SfHQT-DFCPNW_UVpLwTz6tSDlt-NAKrWZHDmO-T8vmARe_yp4smw14eHqepPLA613CAySkDR1sekRFmwN6z8_sYFlDgmnoy5nnmqlAsg3NiGvtjpI9Z08BtZv5cdv0gtqgo0RWhuTK4pHKZASjp5-kLqyMe3aS4FuSANFsYCLvoKH7nsAKTWlhH2kUadK9_h0lXAvmVDL1WtTLQGXn9d9fZhp84hqc1bQshn2Yd0jvx8IaPGTIIPY9u9xuF3RYE9YUZrTQdumIg9CPG_-5Ohfk5Lm3R1zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حلال ترین استفاده از هوش مصنوعی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84152" target="_blank">📅 20:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84151">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اسنپ پی روح و روان سالم چهار قسطه نمیفروشه؟</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84151" target="_blank">📅 19:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84150">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آلبوم جدید ناجی به نام "استار بوی" ریلیز شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84150" target="_blank">📅 19:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84149">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgVeAJklj7QIdAgROBYIgv3SfpUvgY3Ek20wfX9Isif6oYhOvS9PW8k-PI0Zhotep4L7U3GdGefF0DcUTiByLtl78cibOMXZw6j3jzPjdkF9XbDtyc6kKC8yWVLUsRi4MPB5V5uIEWHnKnzGp53ucz_XPAvEf2B6cj3kyX89V898pJKf653lptd7uogsZK4GHwF4GpP-AHG7rzPa1qo5PPGZ3xVTKTOKxATJXgf_ljNNBPzjBU579J-O3kl6HLu8lhIhF1Tis2W29y3OwequstA3Yf_wqwYlgtUEj8bC0i_R3DXlKIEAvjrnWExQGNt_Y9iNuBNwRhLIYRUIR1dE7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید ناجی به نام "استار بوی" ریلیز شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84149" target="_blank">📅 19:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84147">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQfBktLklesjR50NFCeTfPRccp4C-m3tpZp6N8Gpt0QZQLU1zM0W1OI4yXjOt6i4MwNh-1KlpUzD8oanUXMCZHyte_7sZJFeyT06RPsUR7rC8T4Mv21mkaRXqrE_J81Pa9_I7e9wk61ZX6TGxjRUeef19TCq8giQXDkmTN9J9JIpVOQMm-EFAorXpX08FPE2YanRESam79HlQCXjFZ3X3VOAusDO19SYrg_clDx97bwLSKaUuiagmDAjNJ_zDj1e0RFqEm2oIZIRcAxRJXS7Hw-rPQVCwprbFrDF4E-FXMd8Z4EaV_4y5miARnsfUgKGsrhtfwivC_4KVfxRi8CszA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213569f829.mp4?token=fHKcSYhLt7TaxGqQPnuc5AQzU3A_VroHoRDvmJawsuGEVOn5-JWxKk5fu8ipiR0yK6ZJELF-q1wdcsQka3jjEPGM42cP9iAsWiHxCKd-B14xxmrdTjAO8Rc-ImZk_8dyiOPiaiDv8neRCA2VHmisyidQJF6izG6wdAS2Ledv4ticviV_7y5ELdPiO7wTaQIJh4PPDDGQhgZ4lWjSPz6cWwsIoHs87zTR-u-FgMjSXT1tfjKVTZ9F-kaHbmbo3--LQiQVU80wNhO4Kn10nZaUWLWaFREvFD_c8VMPQOdp85pkm6kL4FTRF64_lbypu1h0A54qrHAT4cSLJnV8dVvf5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213569f829.mp4?token=fHKcSYhLt7TaxGqQPnuc5AQzU3A_VroHoRDvmJawsuGEVOn5-JWxKk5fu8ipiR0yK6ZJELF-q1wdcsQka3jjEPGM42cP9iAsWiHxCKd-B14xxmrdTjAO8Rc-ImZk_8dyiOPiaiDv8neRCA2VHmisyidQJF6izG6wdAS2Ledv4ticviV_7y5ELdPiO7wTaQIJh4PPDDGQhgZ4lWjSPz6cWwsIoHs87zTR-u-FgMjSXT1tfjKVTZ9F-kaHbmbo3--LQiQVU80wNhO4Kn10nZaUWLWaFREvFD_c8VMPQOdp85pkm6kL4FTRF64_lbypu1h0A54qrHAT4cSLJnV8dVvf5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این داداشمون دابمسش های دخترا با موزیکا علی گرامی و سجاد شاهی رو نشون ندید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84147" target="_blank">📅 18:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84146">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84146" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84146" target="_blank">📅 18:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84145">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6e0HgVvRvtGkU9boiIcuHmi7vt2Z86CE9dpemwENai_scVBLJ3Xyzddhv-iu3z4ioIXz3iSS8txOv6FrgjVOImkxGHEDOaD09pQWperyHZiyaE0aMqovHffsJ6htA1RALZyesdJCMx_R-BJ9FCQ4uvbBlcEGst4-q2Fd0ENRvM4fOSMDZ3eqg4sPHYhyxiqh0OoYN9l7t5vp4VCLZ3jP82b2MHuOccAhny63BOpPceRFklxuyC8VDnGQ5b361OAYyrExvx5Wy7YBNguqbb3aDrIExOEUT8wi-yZXXzh5gBX9rWzviKhbkuc9_3YBrfMaNAtU-_sPpaV2S7ObCQSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
برتری با کیست
⁉️
شاگردان زیدان کبیر در فرانسه یا کوین و رفقا در بلژیک
❓
🇧🇪
بلژیک
🆚
🇫🇷
فرانسه
🕔
ساعت 22:15 به وقت ایران
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
g6
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84145" target="_blank">📅 18:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84144">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">باز قیمت دلار رند شد ملت یادشون افتاد دلار گرونه</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/84144" target="_blank">📅 18:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84142">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نمیشه به دلیل تقلب های سیتی یدونه قهرمانی آسیا هم به پرسپولیس بدن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84142" target="_blank">📅 18:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84141">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ولی این انصاف نیست کانیه وست کیر خورد پسر عموش کیرش خورده شد کاسه کوزه ها سر من شکست</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84141" target="_blank">📅 18:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84140">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNo happy</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzL7M0xoocwvuvASOYGxTM63qFyXZffGY_0UC_ZNd4CxV6atFfe6vA9IwYg8yojChqfPozzlzkmcwJm61GJPx8z6JWu1OqXVheq6yRff79dfX8WdoVVn60h7usICc9s-GMYA5kBm4o_NaGC25XJCUDswIP4HoN01JKUl88Qmq3b695oHjv5bC3PG4pvWs1EFBGTcpUF8lw07Teq3GMTxTnRkBNJrhfbDR2w_MwNSyi_YNECdyD96W5M2-hruVeIG0TsSU5_favxGpX4SIvM5q9icKelOB8o1iKrLta-iUf_KJNKTaebeZoUtiFxQBmgUlR1hLt4GmPAHnt-d5WlBkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلم مهدی رسیدددددد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84140" target="_blank">📅 18:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84139">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مجتبی خامنه ای: امروزه، برخی ما را به عنوان چهارمین ابرقدرت جهان معرفی می‌کنند. البته، آن‌ها این را بر اساس محاسبات دنیوی می‌گویند.  اما از نظر محاسبات الهی، ما به عنوان قدرتمندترین کشور جهان شناخته می‌شویم   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84139" target="_blank">📅 18:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84137">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مجتبی خامنه ای:
امروزه، برخی ما را به عنوان چهارمین ابرقدرت جهان معرفی می‌کنند. البته، آن‌ها این را بر اساس محاسبات دنیوی می‌گویند.
اما از نظر محاسبات الهی، ما به عنوان قدرتمندترین کشور جهان شناخته می‌شویم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84137" target="_blank">📅 17:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84136">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f73abc8dd.mp4?token=TsBFDqIcYe6gEaGuyp8wkx0hft8-eRk6uXM9-XvHUjuIdweTOLLEEiV0thxF8mMyBuuMfuvlTh_lgPbmIVx9Wl3vDstH74Argn5xJ4rM7CYIpvm5zfK5dI03iyYvHq6_wzm6_WGSQnoMgdcchHqNjsa7sugC2lnNNAl_O6s_Cf4QbpfOi3bQWhmj3PytN6ZJuhEmIoPezqflZlFZtL1KXovPeu_Avi5pJGyRZGUqM2T4TcTXKElv47xh0CjYq1uFUDkTTi30BMLba9Yv9kpn68ujqnTDxv3yV5Uvxq9k06ymMvbQB4FdyC37cpJPz-fc8Qlbu1g0Uk5AiYCjuc0kMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f73abc8dd.mp4?token=TsBFDqIcYe6gEaGuyp8wkx0hft8-eRk6uXM9-XvHUjuIdweTOLLEEiV0thxF8mMyBuuMfuvlTh_lgPbmIVx9Wl3vDstH74Argn5xJ4rM7CYIpvm5zfK5dI03iyYvHq6_wzm6_WGSQnoMgdcchHqNjsa7sugC2lnNNAl_O6s_Cf4QbpfOi3bQWhmj3PytN6ZJuhEmIoPezqflZlFZtL1KXovPeu_Avi5pJGyRZGUqM2T4TcTXKElv47xh0CjYq1uFUDkTTi30BMLba9Yv9kpn68ujqnTDxv3yV5Uvxq9k06ymMvbQB4FdyC37cpJPz-fc8Qlbu1g0Uk5AiYCjuc0kMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پول دونیته ها
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84136" target="_blank">📅 17:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84135">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">۶ تا F35 دیگه جهت استحکام سازی پایه های مذاکرات از آمریکا به خاورمیانه اعزام شدن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84135" target="_blank">📅 17:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84134">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دلار ۲۴۵
ترکوندی مذاکره، عالی بودی مذاکره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84134" target="_blank">📅 16:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84133">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">استاد بیژن مرتضوی اعلام کرد که نه بابا ایران کجا بود و نمی‌خوام حتی یک نت از موسیقی من... و از این حرفا.
ولی خبرنگاری که امروز صبح خبر برگشت استاد رو منتشر کرده بود خیلی اصرار داره که استاد همون‌جوری که تو اجرای جام‌جهانی تونست خیلی خفن بین جمعیت پنهان بشه، الان هم داره خیلی خوب پنهان کاری می‌کنه و همین خبرنگاره قراره ساعت ۹ شب یه سری عکس و سند از استاد پخش کنه که ثابت می‌کنن استاد ایرانه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84133" target="_blank">📅 16:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84132">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZphRnGdxtJvfYaXaq1FUtIgVjTSqWph8VaMYY9_G6M_gw1MF-CoS3IxlPRNrcracCHoaZeRU20kEOzC-1JpQXmLvceo28jQblCYzJJ4koZXb1ydKQCek8MyyxEPpXkpREXKmPySB7wVh0NeZ_1BL85X6HZDI6F8ruSsaLNBKeYJ0FfPIIbq15j89cyuMzLxd1JbphO4m5g7RL2-1L6P3_ku4lTaEzb7CDAJtL0Mf90edPlCVFIpcjc3iddzFVa5aKbhbqgCYD7H3FHHEPNQcE8sgUuKTkFsObTu0W-G3XiZzHJsbe-AxCcGzlerFwiroClrfp_HZiwZsvTLfpvk8Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم کشوری که ای کیو چهارم جهان هست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84132" target="_blank">📅 15:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84130">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">به نمایندگی خبرنگاری فان هیپ هاپ سه نفر اول به این بازیکن ها رای دادم
1 بلینگهام
2 مسی
3 کواراتسخلیا</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84130" target="_blank">📅 15:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84129">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee4b03712b.mp4?token=NBlaYedZaGk73GAaVJS8NdhkKKfTCdYbscLBRgFIahQ0ZV3uR9MLoTleyA7APNIFjeiCRXWgT-gHtuR0xTdc_Jpk8O6LZhTpxhqolRlrmvKMdf1hJBuik_kb-L2HyaZMVO2eVyi8nq9j0vOLpeId_I8vwod2hvV3IUwdUesNIKy4vMiJMudzAUsppLGwv0Zezf3YIAJH-zVKJqIIocVv7Hsb3e1ayOYE-4Yc4AmjPldlegGFAkcFkyaH0LRG-GDT4chulqZoAbTdWLulTU20ZKgJ4S8JKeAPbh7XxtAECnh_QFAFyCI5Bla6xTYCl_3na8BYjQoKHdchHagbL2EzNhLvBBVpCx4E_3HP1psHxsGOqRMibR_k9AmEP0JZQ6MKi-i3DvcfmdkEJCVX3qr8i3qRFWG7hFIqwFVm9UQSS_EYph3xqxWS832O-fQXy7s2FH_u1E5Woj1XI5ZQT9hy4nffdGUQQa8NaeHwNIFEeyYVsEQ4sZnXgFSGdGMVSKB0XXKLUJw8-OTZPbNq6xWCopuR-CLU0VUkab4Qa4xEUBBwieDBt3dzKXazEpLPLC53fn0GqUm_e8yKB-9gra9l-OyRZzTybGTuukPHvDYswAeHl8cIJtn_wf1lyv3eqkj2EH7WTXRjUIqeCUOEWEKlfb-y3n7Tyb-2LCzt0ugBrSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee4b03712b.mp4?token=NBlaYedZaGk73GAaVJS8NdhkKKfTCdYbscLBRgFIahQ0ZV3uR9MLoTleyA7APNIFjeiCRXWgT-gHtuR0xTdc_Jpk8O6LZhTpxhqolRlrmvKMdf1hJBuik_kb-L2HyaZMVO2eVyi8nq9j0vOLpeId_I8vwod2hvV3IUwdUesNIKy4vMiJMudzAUsppLGwv0Zezf3YIAJH-zVKJqIIocVv7Hsb3e1ayOYE-4Yc4AmjPldlegGFAkcFkyaH0LRG-GDT4chulqZoAbTdWLulTU20ZKgJ4S8JKeAPbh7XxtAECnh_QFAFyCI5Bla6xTYCl_3na8BYjQoKHdchHagbL2EzNhLvBBVpCx4E_3HP1psHxsGOqRMibR_k9AmEP0JZQ6MKi-i3DvcfmdkEJCVX3qr8i3qRFWG7hFIqwFVm9UQSS_EYph3xqxWS832O-fQXy7s2FH_u1E5Woj1XI5ZQT9hy4nffdGUQQa8NaeHwNIFEeyYVsEQ4sZnXgFSGdGMVSKB0XXKLUJw8-OTZPbNq6xWCopuR-CLU0VUkab4Qa4xEUBBwieDBt3dzKXazEpLPLC53fn0GqUm_e8yKB-9gra9l-OyRZzTybGTuukPHvDYswAeHl8cIJtn_wf1lyv3eqkj2EH7WTXRjUIqeCUOEWEKlfb-y3n7Tyb-2LCzt0ugBrSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رای گیری توپ طلا هم تموم شده ۴ ابان برنده رو اعلام میکنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84129" target="_blank">📅 15:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84128">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dduh8uLbdsmuGh3pHjj4q0OHeGo_N2uUuzypY-xx2DLwfDj87maa_B3oiukdsR_tvBWYIlcTNNr9UQnc8WtjOpNTNjYJFSV7wgb9tyRWRmU4j-kvAVAMhG3hAFRCKx06sxGzqoqXLTrqW10sPn6f1xQq5zzyuZ6cAeXa2TxV1A-lv-_4hiyrdLSid0fYhL-Phg6aK_weBALm6KzqpdwrdTTLwn7Hr2kekoSHnRx8flphThDhBYSYUaLChu7bnC8iOJRAB76BPd6QRHrJC8Dou1PvbkFjDM3-aoKV3Z9rlppRR-KkvwsmFp-DVET18d4vIBI88vBksF4wRZE4bnfQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما که راضی هستیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84128" target="_blank">📅 14:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84127">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e988dd3baa.mp4?token=IZEFXncTCc0Pl4UhnBBEce2EjX-gVpgZwI4F1XVPmfsaoDMjS-5_SCAtLfw0zlcq81xHArMsWBy0_NsDR22ek93HHLqYERYPiy0NG9TgPIdIV6CSq2ZhuY96Y3jcoHrOVAO1OEmiT1cltDfhQJGXi31q8FmeB4Lasp_-4k7KK2ZGsF591npkXkSSO8p7H-HjcH5ketaq89eH2vh3A-6oa4jnBbACDRWe6nPBXG5cIyzxTgqHQgSPGpHRaMYZPZH6W8ZxxWue54cI1CCBe_ixu3DwPz5mVK2jwS40JRG9av1Fczb31TM7mZThHKTHu1xG880OZcomk5aO9DOkm66IJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988dd3baa.mp4?token=IZEFXncTCc0Pl4UhnBBEce2EjX-gVpgZwI4F1XVPmfsaoDMjS-5_SCAtLfw0zlcq81xHArMsWBy0_NsDR22ek93HHLqYERYPiy0NG9TgPIdIV6CSq2ZhuY96Y3jcoHrOVAO1OEmiT1cltDfhQJGXi31q8FmeB4Lasp_-4k7KK2ZGsF591npkXkSSO8p7H-HjcH5ketaq89eH2vh3A-6oa4jnBbACDRWe6nPBXG5cIyzxTgqHQgSPGpHRaMYZPZH6W8ZxxWue54cI1CCBe_ixu3DwPz5mVK2jwS40JRG9av1Fczb31TM7mZThHKTHu1xG880OZcomk5aO9DOkm66IJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش امین تیجی به گل کاشته‌ی دیشب مسی و فحاشی ناموسی وی به کیرستانو رونالدو
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84127" target="_blank">📅 13:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84126">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSHmwty01cQ3GVamw1b1RB_k1HayTvNOEx5_m6z_pWvQihvfhBcFhRPSlybFOq6SwtifQCex_wsKrxxaTBzOZsMbZHatKXhFxyTkeAQsdFlna1YlaYVOzI9OjMjEPhS-amOE2fzlXE1Z0w8Mnkh9cSFP02S6Fqnwukfx9remh5BkO4PwSF_gxc3uFnGMQZeF7t9WPFjI2xMBJbVTWV1XyX2kz6mJMxlBedE6LE4OSdsndmmYTMyj7j6RixRrIDbXf9ppujiLawYKtlkLYHAHc-79tpEC2PcP-44q1C8KAOfvWIrKsoojqbFF0lse7KB-c425x0bGkW-H-1kwITiHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخجون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84126" target="_blank">📅 13:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84124">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e46577007d.mp4?token=bCfPsubdu278zoUN94Zykcuk14XLRLWQJVdd1pBk7CXGZdIRP1hQfr1hn6V6dY1EGkLAjv4g0si-0SKaKh_YFIlKys4ebJZwExGBsAhB395Npmv7aWa32LcGIbkT_MIUKm9g97TfKnrcuVMXQgye0uHDGQZF4rPZL6PJa1AOTPYKerAOj9gK0wtbdMLjTvEqsltSMXnZEQqGIwNkKoWOyRwC2h0U21A0vufEA3WcWhhGaf-ma2M9Eay7tfEJNhtNwxR_FpPmiCWNCXD07TldDB8RaYlg9AJGTzOyxeERdN0WoA5QohFUJ3VC8rOCPk1LLf-GH0VEgg2xzyQpsyrJdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e46577007d.mp4?token=bCfPsubdu278zoUN94Zykcuk14XLRLWQJVdd1pBk7CXGZdIRP1hQfr1hn6V6dY1EGkLAjv4g0si-0SKaKh_YFIlKys4ebJZwExGBsAhB395Npmv7aWa32LcGIbkT_MIUKm9g97TfKnrcuVMXQgye0uHDGQZF4rPZL6PJa1AOTPYKerAOj9gK0wtbdMLjTvEqsltSMXnZEQqGIwNkKoWOyRwC2h0U21A0vufEA3WcWhhGaf-ma2M9Eay7tfEJNhtNwxR_FpPmiCWNCXD07TldDB8RaYlg9AJGTzOyxeERdN0WoA5QohFUJ3VC8rOCPk1LLf-GH0VEgg2xzyQpsyrJdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوس دخترای چرسی و تیجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84124" target="_blank">📅 13:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84123">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=jwG5jL_8xDDB-wPXskPnq5LC-kMN4kEIf81lY919JqG248xADHLkHbDoSIQl24breKJeAcNCDe4ZIKPJiA1TCpvKvKzX7WNlzpMBYmpvSbJuUU95EJ1WpHJETP43I25mwH8VQk_QaPAqqk0IPASDu4q2wx1zf6pLbYHfRl4ZR8kg5vFfrT85MGJ3yK_e9GCJ2TwZ6IxWYSMUbJNQFFksSWaIlpttMZjHDssxU0DwYvEjfEJObj7IK9tN4E3F-PV-3AMZrTEOfEMitJ6fv1nLFNmhwGqWq15FGPggxS3iac_Uc5KnKMbpsjUUlFMJT0Q_630qYrAguqGB41LhIeN64g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=jwG5jL_8xDDB-wPXskPnq5LC-kMN4kEIf81lY919JqG248xADHLkHbDoSIQl24breKJeAcNCDe4ZIKPJiA1TCpvKvKzX7WNlzpMBYmpvSbJuUU95EJ1WpHJETP43I25mwH8VQk_QaPAqqk0IPASDu4q2wx1zf6pLbYHfRl4ZR8kg5vFfrT85MGJ3yK_e9GCJ2TwZ6IxWYSMUbJNQFFksSWaIlpttMZjHDssxU0DwYvEjfEJObj7IK9tN4E3F-PV-3AMZrTEOfEMitJ6fv1nLFNmhwGqWq15FGPggxS3iac_Uc5KnKMbpsjUUlFMJT0Q_630qYrAguqGB41LhIeN64g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از ۵۰۰ بیلبورد دیجیتال در خیابان های منهتن نیویورک خطرات ایران هسته ای رو نشون میدن،
احتمالا این اقدام برای آماده سازی افکار عمومی و برای شروع یه جنگ بزرگ صورت گرفته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84123" target="_blank">📅 13:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84122">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ناو هواپیمابر یو اس اس تئودور روزولت CVN-71 راهی خاورمیانه شد
تئودور روزولت قرار است جایگزین ناو هواپیمابر یواس‌اس جورج واشنگتن شود. مدت این استقرار بیش از ۷ ماه پیش‌بینی شده و خدمه برای مأموریتی طولانی‌تر از حد معمول آماده شده‌اند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84122" target="_blank">📅 13:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84121">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwAFJFNYDg6WJjPqSncVZ5BmnqKFue5_-EDdSPJamKtWLOJk_LwdPkl-dvjIbuGKbOw2EtrQBe_Z3d-bY7jZSLYIshU5XPepoY2a1Z7wMvEl2hZk95Zu3f4bJTSN2O6n5CLxEnoGDOLCg6W8KmKlvYU4ggCHYaGimgkTLUwnzS6-dua_pKmMiNCt6NwyoDKZtJlyQ-slKQhuC35biAqxOIn84WV0xCu3fzNwpY915PH_BGstiS5F-H1Qw5lnYZge51sXEkmtk9uWAWioO_v8Jebx6ab9NemdnOdTVLTWKfQwH5ulraanL9MZ2KlrryQXb89TXCqM6FDI72USlXB66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوی جنگ میاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84121" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84120">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84120" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/84120" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84119">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMlCRcw5SxKbme5NqWI_UQa5us6EG1CKZd_NnF1VpHM9NKJhepiMceU2PtFkl5AIRLa9rVnpt27QUhhTQVXtUoDx30ubHMtl8UL95HxF6EiRZ83vK9hJ1s1s7QnNfrQOx6ZTtT0zd4qz2u3rFdHNKBxC11mimnnV9NNpf6Lz8Bs_fB2vQfKNkgOaMoCgfm7X2Sgo1LuF2NT4BvjZd1aYbiIIDeZNxTUcTLnlFAF6jDEgDGgwtBDOHFMdyYDDB3MdnyE0ku7A8XW0LrgufbSAJ4s6S0BraB7drxe1S83qz0cUdSM6HzhoRbaRcQDjheNHo82xfSrJpj1q7iLvRlM2IA.jpg" alt="photo" loading="lazy"/></div>
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
r6
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84119" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84118">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حتی تصور نوازندگی بی‌نظیر و پشت صحنه‌ی استاد بیژن مرتضوی تو کنسرت مشترک استاد نامجو و قیصر با حضور افتخاری مینا نامداری، چشمام رو اکلیلی می‌کنه.
🥹
🫠
همیشه می‌دونستم آقای پزشکیان از خودمونه
❤️
#فرق_می‌کنه_کی_رئیس‌جمهور_باشه
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84118" target="_blank">📅 12:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84117">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3_lHCjKYtZzd7qWqvlo1yd9F9I8Do73o7Tr30-GMyoH9lQR95gZkuMRxkp5bZtsqxh5wLXjdBBIkaO_2cNFDFazMnhddyjmXynfOnxACyl0AUdvev-qGN-6ucdJSzr5P5yvl2US5CZLXmgG6MDXiKj9iDZUMvXm_LqR5_N7Iw-tVVjrjh6OADdwM82JVXqq9pOT-TP30Tl1p7sbF44CtpAac5sH--PeYuOq0Gct8fllzHj8-BWL1aMwPV7egcKVJS1k4p9KFjXL5QfIsYjdQK9OzlBJemrmjChgBKtwiwMvd6DDoVpVDIDkl15nZ6dXm4K6P8bS7ZEBCokDKgHwHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری و حمایت هیپ‌هاپولوژیست از کنسرت اخیر بیگ‌شگی که خبر از احتمال همکاری این دو نفر در آینده‌ای نزدیک می‌دهد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84117" target="_blank">📅 11:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84116">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUammC28xBzYU3f4I54FB1P_h3gXFh3Aqf33poiYLUcFj99vc-aVkbSmUZCY_DoaKZ_pVGYNgBF52_Z4NUtst2XG5hcrQfHBoGvbBFcA58S6fAcsdsUA1PvFgSLk4FEuXREsR2ou_l-ElcIPaWJg9sbap2LxzKa0ODmodmenxnH9O6yUzXArPgEkh8F89JszwBgTOvnql2pGOM0fSO8EqZ7uEggwZfJvE63a4OKu8Psgm--v4X_rnoqp3UXUsRuVE2xmSkoE6QSCRZr9waAzXtqgsWanGuVaO9HtSoW5Ou1-oOo1-joV-B9kbGf7ZMIvMEqGalitmOe63s-WgzwZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که نگران مهاجرتشون هستند ذره‌ای نگران نباشند و گول تبلیغات رسانه‌ای دشمنان رو هم نخورند.
دریای خزر هنوز با پذیرش خطرات کاملا احتمالی تقریبا باز هستش.
در کنار کلاس‌های آیلتس و تافل و خوردن ۸ لیوان آب و قوز نکردن، کلاس شنا رو هم با جدیت پیگیری باشید به زودی تورهای فرار و استتار در اعماق خزر با امکانات و قیمت‌های ویژه موجود میشه می‌تونید بدون محدودیت شرکت کنید.
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84116" target="_blank">📅 11:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84115">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ناو هواپیمابر تئودور روزولت آمریکا هم پس از نهایی شدن مراحل آماده‌سازی راهی خاورمیانه شد تا نشون بده دکتر عراقچی حتی تو نیویورک هم با تعهد کاری و تکنیکال عمل می‌کنه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84115" target="_blank">📅 10:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84114">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iztAFQJJ8Pr9dgoFLCUYNwDe_mGBRIJ4eb9Q3pVXVFg3LfovHhlllVSskWI5-SvEa-yYkNtgnaDJLANV1fm2NCTsYgTPO8pzjY0zNmtajBWFV4SR21_DRjtaB9bMdThuYDad3NhwcJcNnxfmuuq56CCJ51VbntNkgrz4W-1RDBJZbyO1cvzgdstRdaq6nXXZ4UoVQMZdjHMrxynoLpTBvx9mCEPLIg6br_q4i3CZrCKyvud_McwaOj4sbf1aKjSb4zkC0Yme53BIY9H-AJdBqIEeQguGP5BaQsnRM4Oyuvhu-vCicgHlA6E3rcMSBpOdRJcY2VjbFOBPsVFfwnHVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر حیف شد وارد مارکت ترکیه نشدی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84114" target="_blank">📅 01:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84112">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سلام بیایید چنلم
https://t.me/+q5Ml6Hl1Af5lMTI0</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84112" target="_blank">📅 00:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84110">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f7eiK8jUODZonKFFqhlvfAmKgt8W_-DyPW547O8RmZFVwSsiKtBAmekZAQaVjnUCTLdu-q1XFG5SiFKU7ta8m8U5yO3XtAaGRZPHtmZejT7e4z79DbE1EyB1na2li_PzOP5rMwVFQjjARqtq4FMBh-eZMi-qM7XjKTHy3zOaExlusSmJJoCTtZ-laTY0VQELHhY6qECZ8qEJ20n9bfqhcxUjJVIxNQ5mbajdl7SJKa643ThA19ZUzRtltnWwiEVkRqHozut3IZoaSuY4_uz4G_JWDIy1AG8xQIi2X0lht4Sp9m7GpzhVqCJ6jDvaEdyZ9yLc7MkDLIqdQtqtVrC1Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iqt7UUckG8Ab_oprkUaRrsXDbF5ZYV3sbdXtrvGgEHCS7h7dCdq8DjZp1ypvP_6j7gdBzeBJzed3bstR1zG-i_C4jcXZgD0u5gZ-B-z8uEDI4NVg8MSPs0sHWnJZAZRkGgBy8uQe0NZ6VcFzc4-tqjdIr3T47x6j_NGYRREEhT5xMyjSKh8tP5c1QyVF2eyLUQr2Rkjeyu60emWt4Mk22tEu0P4A9d6caUY_BHrXFs-nG9zCzMAcuo-opaXaK3Lj0OHsbwVgvSAIUIGbWUExickbi5i1zJ5bTVx7iR57F_eLYPeNAupZk8hHLqtkvZsqHfEpYJJU_2nGLHyYzma_Aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به مناسبت شاتای جدید سیدنی سوئینی موافقید کیری اورریتده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84110" target="_blank">📅 23:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84109">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yb5EG8fSNjHbmcjPOXgXeIvhI5XNZkuOT1sz0ZC8UFOp17guu9Y5XcJ40VbxegO3_QLe4rqgT1rQze6W3h3hO1O9MoBXMcC2nVu4hxEYO0zjl3THjNLxbYgvcXsdwTdDh1yRzV9UOlKSrQ8Db_DNy0Tgaj3v7MHpFmVNKV0pBdJHN5EX3okjGzIi31wUUr4ka-pnZupp0dzWKGBWj8u9DwQfTulfoFHZHb3YCyND6sTAzsmzKbl2ztBWAN9qypsVUepIVTFVTb-RjgRe2ttJq0lV4sAV1HhAEPBaUNFrtIC-yGuC3sV_R3F8AD0cvbFKFsxxy2hPlMZm2LGJNzwjLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشبینی ایلان ماسک از آینده‌ هوش مصنوعی:
2029: ربات های اپتیموس از بهترین جراحان جهان پیشی میگیرند.
2030: هوش مصنوعی از هوش ترکیبی تمام بشریت پیشی میگیرد.
2031: ربات های انسان نما از صد میلیون فراتر میرود.
2032: اقتصاد جهان دوبرابر میشود.
2035: درآمد تضمین شده بدون نیاز به کار کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84109" target="_blank">📅 22:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84105">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">عراقچی:
غنی‌سازی ۶۰٪ غیرقانونی نیست و برای اهداف صلح‌آمیزه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84105" target="_blank">📅 21:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84104">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">از روزی که وزیر نیرو گفته ناترازی برق نداریم و دیگه قطع نمیشه بجای روزی یبار روزی دوبار برقمون میره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84104" target="_blank">📅 19:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84103">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ce0419e2.mp4?token=rabeLEjH1B2GQCkIV27V-C4gz3iQvhGa0_fnjhwb2IJQCdr7C2dKjSjHdHQzItZ_7CgCZ3u0ZxvzDRx_G8cDPkX1Rbs3dhOMaeGniJgimyVxcaLFZ_VPjEZJVCHMrB9LzkQiUBmZQEJ9BqSPiGPrSYFRu1Wk3Of_2stNTUh1DBU3W1-NeWwjMRcmfVHI8PRKwQ0ogw-Dyh3kQscHZRexi1b6TABdAzQHnXZxY_tW1CFTZGkXrt2oPkAxC9qG2bjP4dFzAD4em60KSpOVFfUFtunSk6Q5n-iA7sIM8ElCVHPJCZa7KXFmGKy317n6ddwPp2f5eQqDudyZ_U4PxxLhrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ce0419e2.mp4?token=rabeLEjH1B2GQCkIV27V-C4gz3iQvhGa0_fnjhwb2IJQCdr7C2dKjSjHdHQzItZ_7CgCZ3u0ZxvzDRx_G8cDPkX1Rbs3dhOMaeGniJgimyVxcaLFZ_VPjEZJVCHMrB9LzkQiUBmZQEJ9BqSPiGPrSYFRu1Wk3Of_2stNTUh1DBU3W1-NeWwjMRcmfVHI8PRKwQ0ogw-Dyh3kQscHZRexi1b6TABdAzQHnXZxY_tW1CFTZGkXrt2oPkAxC9qG2bjP4dFzAD4em60KSpOVFfUFtunSk6Q5n-iA7sIM8ElCVHPJCZa7KXFmGKy317n6ddwPp2f5eQqDudyZ_U4PxxLhrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی برنامه دیت ناشناس، یه دختر مدعی شد بلده یه طوری نگاه کنه، که باهاش می‌تونه مخ هر پسری رو بزنه
و در نهایت این شاهکار رو خلق کرد:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84103" target="_blank">📅 19:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84100">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdiyar</strong></div>
<div class="tg-text">کاش اسم منو میذاشت</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84100" target="_blank">📅 17:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84099">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEP3nJbKaEzwJJLUe5FvrtnG4UZnFhyFgC_NC7g_F-s6dBT0eCpNQw3upvX5hRUE9HM1d3du7jes8ikpBbyO4cnrgr8mPQ0ZcCQYOp6NA1OOcdEc7FcH3vwhY_UmRqVGBAX9yNxkFSPd4F7cCqikAS7y0It24Oo7neBPDf8y-9ORpFxZOwZ9t8nVks615we3dKTliIEBijq8Cr6kBYuJ6t1R747CoLaTpzW6CnXWgQ7VgS2VXNP0KAV6hUPbIijbkzQAN1y5-W_C0uxb1Atx2EX6hbbUui6ZLrgvKWvjy2bthJ_3yg6mEh-C4V1PhNa5duQmRTaLxOqyCuRhWc7HsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممد ناراحت نمیشه لنا اسم پتشو گذاشته تونی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84099" target="_blank">📅 17:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84096">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCUp5FAEZ436jrnEQcEBymmzgQCV3ELQsu7Ekqi26s-DkHbIfEMcXXZWF7GH8YPVhNH1GnY0WmihAUWNXIRKReDJ_WFOAGdOg9qSSowF277yeEglYyco2yjOQhy00ZfERPzYIZadnGRQ2gxXLHf7NOX0Jeh9tvSOSBCMuEmkUB9vVCMposrTYc_ntXXmbNdii9jhiyVISuSMSMcNUem6-x_RlGr81I4Y_bFOmhiNpfy_2RAIY2ICjqC8IyYGFL3BXkcyc8W65j7JiPh3dPBd87NkaV1bjygif0Rz7o3FdmHWLxv0ak-yEjsMDL-FbPi00rJMQQWUl9PITRmYRt7bvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfbiorYpznRFtq6MGtoa-dXsyOw-Pz1VImU_Wq4zDidYLTefSy2xZ7dLPHzo4licpLg_OHXmkFObHx9hIl6mY1brTyF1asx5bBQdkF7_DsNgtO9wo_ibnI0mHeEp1Nz5fc-PiHLeNgdK-Iz3Zer1-fjy8j6jxcggw8UpHLU-lCLMH-CT5yhyc8ywqXjpP9bF-EhGxFI7HQjek3-YfoFjzW5kjOZ3Sx2Gfv8QuSW1hvEefNqHyiqey4sSIMLeVDveXH_Nsm0_oaFH8QkR8ZmW924I2QhZUytSmKkl9d3bwarZnGxCx5JPnlAw2z82MlxIOLyfMEca2WCLn3UC-9r_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ESjB3f3jg0VTzQgvuW88bYLAA09UGNcM00N7-ka4JVHxfdr5B1ywRKNUfFd6ozLswScNYsnUam8cLs90TVIuuliug1eN4l0gQr-Yxy8fzK86iLkjH44fJoMb7CafqMq2ZK0GH6A0E1O66PglEdPxgItkMOavSRPrWQf8SMPPGA6mz_FX_qvfEEcvvaPJrqKbCHyp21G_HUYQDjKs_NSsPGevc5DPtfAxcgrVqqO7t3MI8nhlPlVfRWF3ZAA_W86hRR2b60knK7UfWL6azPFT1XEt6uMW6Yq45qncKoxn3anRo4NM64b4_FljYkqYUFcrdWrkg42H3j1QlP-5ma88aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید ریری و کامنت های فرزندان فهیم کوروش زیر پستش:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84096" target="_blank">📅 16:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84095">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">هانی رامبد تو دایرکت هادی چوپان:  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84095" target="_blank">📅 15:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84094">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPdY60oCj4ieMYGlqA1CHY3IvISdUDP0WSw775sPT3s7go1ez2qzzhZR9F4ie36IKkYAAd-fukk0VUNN_VwmXKep3f8zqpJb9xZoSpl7EuXUxc45mVa0XXnBftPrw7Op2FNHevz4I54r5Ka-TGdIO_HTltfKszDF89zWRHRANwWJ-dHy1Ygl1kikkGspDW0rnZJrOHtXsKVegI4g4c_qtxU1aU1uj6Te3IFT5OJXfPTkThZh_k-ZttWHNw-yU4p6S1EtOsjQ6nfU5j5N5F-JGR7f3SKKqXGWL3eQ7vgYnjf4dh4OilOOZwOHQeYZh_fGWD65vPbyXsQ-MOMikshufQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هانی رامبد تو دایرکت هادی چوپان:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84094" target="_blank">📅 15:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84093">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b331c3393f.mp4?token=JadLw-hXkpG5iWvlMHDmarE4PfOQnT2KCyG_KL2eS4tnqeKf60_2x5sQSNgjDM-Pi5W13-OyiMjSSYwmxuJvs-MuKzOFRH8DqG_WnJJ7K6tU2IsPOqTMxzQKBihwgploZKnTFJqy-v1B3U1mNOE_25J2h0Di7R6XJ9UZEAe4iYU8hpIoV_gLOCLdb6OCMKdQGDXC5YiFBTlJkTYCz81cR_3E32Itxr4SuMiIXeEY6hD6rzXvUIR8JQaH7Gv_8Dkf8vNS_O2i5pVfXRxCCshPJ6vwSIz0hkczDFATt5S9RUqKmSSGObq1XGIGYp-SYoXFqcJfeX8cEaySWOv7LrrCQ16scN-3GUI9ob1Clr4KVHEEUlxJwfHfEcIOK1Ib1XPwEGTG8tEkEyRwbMVe7KPCMw10UGmtiw32Q9zkhWTLFCxN7AcwDBWwJ6eNwvnSbCbT4dw0pLHPujP1ZJQGntBfXvNkZOYTgcr26mkRNOc-BxVuflQmrgu43OBF4QkUVtwt_umchqsCNUgHLhIosyLzrBoC5CC5gS4x0NYZG1S7o9LBBEaoV_AqHsNwHVLi7j7gvtxz9vfwDK874FYfJtdRL-WWtvbkEHAOwLJ5m62INrdtAnqvsZxBZ2wbI_JpQervxnhuwt3DGA5iXHn9e3ek-h54oR8gveSUS3xSVAzeFHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b331c3393f.mp4?token=JadLw-hXkpG5iWvlMHDmarE4PfOQnT2KCyG_KL2eS4tnqeKf60_2x5sQSNgjDM-Pi5W13-OyiMjSSYwmxuJvs-MuKzOFRH8DqG_WnJJ7K6tU2IsPOqTMxzQKBihwgploZKnTFJqy-v1B3U1mNOE_25J2h0Di7R6XJ9UZEAe4iYU8hpIoV_gLOCLdb6OCMKdQGDXC5YiFBTlJkTYCz81cR_3E32Itxr4SuMiIXeEY6hD6rzXvUIR8JQaH7Gv_8Dkf8vNS_O2i5pVfXRxCCshPJ6vwSIz0hkczDFATt5S9RUqKmSSGObq1XGIGYp-SYoXFqcJfeX8cEaySWOv7LrrCQ16scN-3GUI9ob1Clr4KVHEEUlxJwfHfEcIOK1Ib1XPwEGTG8tEkEyRwbMVe7KPCMw10UGmtiw32Q9zkhWTLFCxN7AcwDBWwJ6eNwvnSbCbT4dw0pLHPujP1ZJQGntBfXvNkZOYTgcr26mkRNOc-BxVuflQmrgu43OBF4QkUVtwt_umchqsCNUgHLhIosyLzrBoC5CC5gS4x0NYZG1S7o9LBBEaoV_AqHsNwHVLi7j7gvtxz9vfwDK874FYfJtdRL-WWtvbkEHAOwLJ5m62INrdtAnqvsZxBZ2wbI_JpQervxnhuwt3DGA5iXHn9e3ek-h54oR8gveSUS3xSVAzeFHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی یه ویدیو از پابندش گذاشته با کپشن"یادگار دی ماه"
و حالا کامنت های مردم:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84093" target="_blank">📅 15:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84092">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بانک کارگشایی یک تن طلای مردم که دست میلی گلد بود رو بالا کشیده و میگه دست ما طلایی نیست، حالا میلی اومده به محسن رضایی نامه زده که پیگیری کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84092" target="_blank">📅 14:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84091">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2l6_sOvcVWt21d-VKd3tuWO2KZUGmvDARfaSJ06Bh4ST8FD0FKRH370okf6-i_wiS8AJ0TkUTVTxBaYv7Hs7EqdL5qFzceIoE29QG9hakHecPXn63SF8WlFd2jkE2Vvyz_yC1fqBPppYamiib_dLr02XeOES98KrkOlGbdN7yOnLdBPDmPiCnSSzBwyqxConAk8aJfZp6BpzpoILakEkAq0GZmBM66dtQvywmR4biEvsrdNZRGl2_UXb003ydo1fY9ecNeAKyJpz8Ksnz7ncMsHMJcBD5jARN7Wdp5-XIEfiiEZ1f9ls4HzIbit5Uf9dcATr8I8EC5g9AiqXX9Mcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک کارگشایی یک تن طلای مردم که دست میلی گلد بود رو بالا کشیده و میگه دست ما طلایی نیست، حالا میلی اومده به محسن رضایی نامه زده که پیگیری کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84091" target="_blank">📅 14:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84090">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lfq1gMt_dPMp61QzxHhecT3a-ar-to0sV24q_Y3yK8jmM5PH0wWHWybJnFAb1fR2W5gevJk3aSkGz3QDqKXt8scQ1qlR62OZtJbZz1j3K08wCwmTLTPdreAQMPCjU3sXfDpPYFoqQEoO0lYXFiKUd26-i_PjGTMvsHsNK5VMiPT8OtyVTK_Xzb39cf0irZWbuBb2ifJ0Qj-gm0rhFZxO_KvOyMEvhK5LeEMOvYiitqL3txRun3Y8iQaR0jMhHHLF3BBBNqkUL9HVCXl3DiHBzjE4VQrU3pruGxbomHLOIi7JMn-woBy-Ktb9r55dkY1iQOfwXX70-ZnqWznzCxjDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد همین نیما و دارو دستش تا یه چیزی به آرتیستاش میگیم میان میگن نه هیت ندید و فلان، وقتی ما میگیم هیته وقتی اینا میگن انتقاد سازندس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84090" target="_blank">📅 14:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84089">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6331f6cc.mp4?token=LyeI_1kzfbxHYpa6w-r_8TNa-5hsRTLgewpos_canwVwhmI4R9z49Gj-bJU5q46NvGQFIzydEQbCbZXZBaFowWbl5oVyC8V3rqUW4WfSz22lB_LT5BUe7tA5RlKcDgzQDVtVwdwu1EuwveCr5zWBdVdXlvXAkbc5NznLLQtdKDanvVlP8-GO4CtVdG2iv1dyXBMIQtOslyUOkwRofF9TfWJVYJXIZ_PH9vM1GAgG-lpepSpi9F_NHXXj4G9iIXAoVt_TSJKZCTzYm1k7vYkQoPhdGesQFvg6bh7U0HdnnHV7GbXU5-Jrp0-JknB_Gpc_S74So7q-paGY2tMEXwZWdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6331f6cc.mp4?token=LyeI_1kzfbxHYpa6w-r_8TNa-5hsRTLgewpos_canwVwhmI4R9z49Gj-bJU5q46NvGQFIzydEQbCbZXZBaFowWbl5oVyC8V3rqUW4WfSz22lB_LT5BUe7tA5RlKcDgzQDVtVwdwu1EuwveCr5zWBdVdXlvXAkbc5NznLLQtdKDanvVlP8-GO4CtVdG2iv1dyXBMIQtOslyUOkwRofF9TfWJVYJXIZ_PH9vM1GAgG-lpepSpi9F_NHXXj4G9iIXAoVt_TSJKZCTzYm1k7vYkQoPhdGesQFvg6bh7U0HdnnHV7GbXU5-Jrp0-JknB_Gpc_S74So7q-paGY2tMEXwZWdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسئولین لیگ برتر به تاجرنیا گفتن خب قهرمانی فصل پیشو میدیم به استقلال ولی به کسی نگو تا موقع اهدای جام که نتونن اعتراض کنن
تاجرنیا چیکار کرده باشه خوبه؟ اومده مصاحبه کرده گفته به من قول دادن جامو بدن به استقلال، حالا کل تیما دارن اعتراض میکنن و احتمالا دوباره کنسل میشه و جامو نمیدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84089" target="_blank">📅 13:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84086">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4ew9L5Sm_2Q-XfTdbdmk6Btwy00Roo_YrYNeNArYkztuv6PcUkL3uHTY-CQM-Hg7vpx1BtpI1TIbSQznSDh2tZwb4WDDnMb49sAs9Ms4qCZtzmERDAiF5kP9HfF9fO6TG6mTf3624O-wcl1o04WUayzRT6TrA-mVKcPLkedvZFGfA_HpsFiN9CXTO6meC9NjqdJV3mHwiKhbUJTLh4q_kuc9t72r6j9Jv0m4KdeKxrm_ox2g869Tufp_s0YkTa98wKWKCPTsQ5lHGJqd00_i04bGuytdUoxYyvNu2w0UDaJCuG24kUNxVRitTTbK8IVPr77qsgEqMrvECC6kd5Alg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطوره حمید رسایی برای اینکه سال ۱۴۰۲ تو کانال تلگرامش به محمدباقرشاه گفته بود دیکتاتور، الان داره می‌ره زندان.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84086" target="_blank">📅 12:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84085">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6182180c47.mp4?token=nQAf95AcIRXGPkgsRSou9WjZAl_uqmjqD5UclAg174WjqRrgHDEv19HJ5C3ksRsc9FoWuhfPzfTmzXEVjGhWsjR-q69hXzBwEdlbeAUCZBWvVwJ4R8DtJlI_rwF4HtKjP42LUyTzdG12gLuzZ7VX-Lodk2vfifWGQ9-utDkNTNkDOpF-HnSH-Ov5l6jxyYAalDK1w5XOoquCHtUmahsZNE_9fr33h7Os6kLVWnHg1le4kO20DkJze1-YbfLWzxBjzcU7eWVno4KEK5iyLaLUjjvmbGdbhcl9Mn9uoTsIFiKHvO09hdks1MD2s5fMdsjCKT2W25I8wcZ5RM74Ai7wbSZEAfDBgodNlPYQJmA28rLSRh7heL6iuKTzidpQo2N8WcKPVjSNJ-SbslZZeRu0qzG9hxGYl0p83oXOyKq5KqtrEYj_DOjmn_Wlh8ms5JwHXRH43zsOh0OQBW7X-G5QDSmFrlE2F_I-vWiruntfNvCb8tRmpyDa6nyGGfWt6kr2iP0fssh-8kpshZAF9TNv9T-gC_pRtbUOkWEAIcpMtwAbPVyV79lK7SGD9qdI_clo8ITRCmSa9yZgTzBWzBmupDNVgsd7jHsma5EOG7jIrwhzyDsffzWCGhddYHO-fgEH5XUD1XDEIst-vXw0Fs06-cGrvL5mgHHmnbzK9PrZ2G8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6182180c47.mp4?token=nQAf95AcIRXGPkgsRSou9WjZAl_uqmjqD5UclAg174WjqRrgHDEv19HJ5C3ksRsc9FoWuhfPzfTmzXEVjGhWsjR-q69hXzBwEdlbeAUCZBWvVwJ4R8DtJlI_rwF4HtKjP42LUyTzdG12gLuzZ7VX-Lodk2vfifWGQ9-utDkNTNkDOpF-HnSH-Ov5l6jxyYAalDK1w5XOoquCHtUmahsZNE_9fr33h7Os6kLVWnHg1le4kO20DkJze1-YbfLWzxBjzcU7eWVno4KEK5iyLaLUjjvmbGdbhcl9Mn9uoTsIFiKHvO09hdks1MD2s5fMdsjCKT2W25I8wcZ5RM74Ai7wbSZEAfDBgodNlPYQJmA28rLSRh7heL6iuKTzidpQo2N8WcKPVjSNJ-SbslZZeRu0qzG9hxGYl0p83oXOyKq5KqtrEYj_DOjmn_Wlh8ms5JwHXRH43zsOh0OQBW7X-G5QDSmFrlE2F_I-vWiruntfNvCb8tRmpyDa6nyGGfWt6kr2iP0fssh-8kpshZAF9TNv9T-gC_pRtbUOkWEAIcpMtwAbPVyV79lK7SGD9qdI_clo8ITRCmSa9yZgTzBWzBmupDNVgsd7jHsma5EOG7jIrwhzyDsffzWCGhddYHO-fgEH5XUD1XDEIst-vXw0Fs06-cGrvL5mgHHmnbzK9PrZ2G8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیک واکر با شکست سامسون داودا به مقام اول مستر المپیا رسید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84085" target="_blank">📅 10:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84084">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dva3iq6NOmpAZIPnrspZDQAeNPapouNztQJjxdN3_I2Fw0snJalQ5woQsWUpC8XhuHyW2UsOmm8CvzpDbImDWThj-rVr78kECfDmwpdoBuqaKZ5n7bn8k-FdLGbPhkL-S5YsVdRYUPRQrfJxpy4T7wOm9PoVNTOxBvy2FhKqVO0jTsffus-Pz1Zqgg_Nm7qVAYYrfwfSFYWwERuuKXbub7QF6jQb7i0-uTWdxC5730ERH6G17zb39R5idmGxMM_vl-G45MHnzIOyyNO9yjPsaBsp0ZsmEyVVRXJIk4HYQuZtRGkwcxbc7pj7FBL9Zkp9AcK40ODQ5t5h848U4AcVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلخون بد جلوعه حاجی
ناخوناشو تتو کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84084" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84083">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گوگل ایران رو تحریم کرد و دیگه نمیتونید جی‌میل جدید بسازید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84083" target="_blank">📅 03:06 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
