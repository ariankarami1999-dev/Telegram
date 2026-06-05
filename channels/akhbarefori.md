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
<img src="https://cdn4.telesco.pe/file/DGShUanv8_LWDxyF8PR0FrPs1WjMxZyO4rPM1U5RMu0Zv7SL6Y73mjygwN7OfSNE69SMQ6NSEXslUJBgNdFjRjAEepWsdCUijUfUBpKrmLWAfsJNZk8WYywg_VfU7hqcP_FP1UEdb6fyEEz9ZWLEb9oiyY5NVJx8NJzPdtJYKTilhTv3skObCLNSSpxDVNmouCEKNmIIxOJjYXbofnan4D5swVqAOQIO1cUCdpJTUxoaDvU5k5RBo9rdkChHNbHy_bUsmR3A4JjaxJkVHngBWN38_LlzvLbu-uvvkiTux1bC2W6rLKZcXt_a_D4Nap2Gt2YBnazfEgwHk2fOHQ7zSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.14M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 11:58:49</div>
<hr>

<div class="tg-post" id="msg-656306">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8jbFtc9aNlnQH715DLO2AqzUNGFuw9oTPAbBN_yzRfmFs7Dlm2XwlGiR1rvl6XbPPedAY8lsx0TNk09e10Cf-oeCtwDeuCHKTtJ966OHP4OZVUOkehSbb72WcbIaSon2YWx84e-3exuiVMM80-xdTSxaHyPhtgKVwMJNJ7HuZmP3Lk_KvQgT5HFuIjie3ChHS28NgZllBGeDLPFfBGsnU7ov0TEsP2W-yJt93b3bf20_fwu96VdlNSIvOX4erY2UZV6UBy9r-x5_U5OT9vozpXrvvygEzxiBFMuL5xwedEWNCDJJDpZ3xOuMOs_YjuG75GZ2xufaZoxQkeBsaIMww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*
♦️
سوتی اطلاعاتی نیروی هوایی آمریکا*
🔹
نیروی هوایی آمریکا عکسی از عملیات سوخت‌گیری جنگنده‌های خود در اواسط ماه می منتشر کرده و مکان آن را «افشا نشده» اعلام کرده است.
🔹
این درحالیست که در پس زمینه آن جزیره مصنوعی پالم جمیرا مربوط به دُبی کاملا مشخص کرده که این عملیات در آسمان امارات در حال انجام است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/akhbarefori/656306" target="_blank">📅 11:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656305">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
اسرائیل برای سه منطقه در جنوب لبنان دستور تخلیه صادر کرد
🔹
با وجود آتش‌بس جدید در لبنان که از سوی ترامپ اعلام شد، ارتش رژیم صهیونیستی برای سه شهر و روستا در جنوب لبنان هشدار تخلیه فوری صادر کرد.
🔹
به گزارش الجزیره، در پیامی در شبکه اجتماعی ایکس از ساکنان…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/akhbarefori/656305" target="_blank">📅 11:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656303">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/COcJbpb6qHa0SSQjkixMTkfajpKn4WqCmARB0XFoCLSa_BvDjDuxcx28gTelWozV5ernBeHTOX86YDzOX_xTtoVoqbnF8GWzL9iPDWIEDxtJ9qGkm2eA-GXI87KgcG2ou4c96FsYlUvbYaA3bnU7R_KIwEW0l92lrW8jviDP-xmFIjBiYLpUv7zhtcQG3IPySmOVvCviV3dCeTEVXFOtH1ATIGtTHi2ddVK5TuT7sfAd0jVWMD0wpr083n114NuOWCyp7FiV76kvD5nzsQgEw5KcNiVEKOj0Rf-zIdhLSk0KGKnmIXgjJr43nqW2u3zhG8ISxIJTK9vfkNeSmlLO5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zr4jHf9MVTqpoFwcGvfh8k4Vcux8okk8KMr4ZhK5NTaL4p_-TW3oGvMvK_K7eFXbueFs3R8JXbPIcrL5QVlyKCjPH-qqmWZHb-Ks2OTVeLRHMaEC7ydDpgwO8TKIpgaEwoJGIFcuRQwcGBcDiWl4AYdklnvfB2uPCAD3Z0vMa4UwLLD5HyXfItVzvlWphXWBDxeNjcNAjxyXfj3GkOeNJgMYoigLvjkFHUjtvOtJFnOco5Mv27UzYA48t3mJiH7HrzK9KCXVNCKEhQTWpriLtf4s9yNukmi8ZzowJmmHDzBZj9iByNOJhvRGDOwW0qeINsc8WKwNToCUHcytzP8nIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خلاصه اخبار سیاسی، اقتصادی و اجتماعی هفته در یک نگاه
#مرور_هفته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/akhbarefori/656303" target="_blank">📅 11:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656302">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JldT1X_SeyM0_k0RVsggXhuG81YObPwsTytYCVLlajtR6rHdW3RL2ELPv0J6ILySvG28cddPq-zTrPQt4JYxX4uruREVzsh0zWwT6Nq-cyfNiMwFUZHd51koKQf7kjKx9jexJpn86O3z5g4XFHdj6hGNIi7h_1S_hUtMRnppWTYFBKr-oB47R0-4srsqHTB51mokr_nBnQR5n7wUmuliANQ0anyAKcOIGObpyTNhcFY1qZryJr325KlgLI2yrwi3RgDd0ny_mQzyR_KHQXOPHYqdZseYyBhOsG-8MGNl1YEsEjpjYfexUHL-bdgoyXwj_eiPqMbRLCdUCn-EwCl-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعرض رئیس جدید موساد به مسجدالاقصی
🔹
رومان گوفمان، رئیس جدید موساد، برای نخستین بار پس از تصدی این منصب، به دیوار براق در مجاورت مسجد الاقصی تعرض کرد و آیین‌های تلمودی را به‌ جا آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/akhbarefori/656302" target="_blank">📅 11:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656301">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndrxDNCi6Ypy2rRaevMuc66R3aSX0RKHC4U-LvDsgujDbaHW-qIt6kx4VoETnOMrOXw3NY0OmP33orbRzuTDN9jzkkNR2KN1nNqez2-JQ25cCmQAjAB3nXJ3AjauXRev_5Mw4QBnyiqLUJ6RRyiVUr10G1CmqLmIhbcCqJ-UXxW9pPxci62Oq1dr3TKTiUFwjfuS6QvivWlh-JThhl26J8dL70PS3dcHidUzuhDkGlLPvQigArXZPuRCfEKwswJbPh1FMUijq9hpHLb4_vCaDRsW-rM5PVG1EZ8mkz0FiOYkcsr8imUV7qjhbySIw3SgjppIQhYNzFT5N6EwiQUr6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/akhbarefori/656301" target="_blank">📅 11:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656300">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b1f3b02d.mp4?token=mNakMuWE0qDkljF1LdIcG6_abF6wQByBGe9nn8yrsnUgxs4DHiDlaQpJQbG1Hlw-aTKlym_EPvUkPM6EijF7gVLD-wlAF98F6ni3lzhSp9EsOTddfos5yh-VaIHgHnHmGPzMFGb3hMmYjURqAEQionUKMy5cjaRo8OVPXDIkzfHtCjSpu0cn8KQ19PiZKCNEjRdO5iL9veQLO3RAq4dC3vOMHLdvEvb5HYsLxFEK8TiMl6vjhUAsQboPLTx0brOVVRk3gNJ_R3w_w4RC-MpxsGYfi5oPHlvGwncEQAwyyG59R0vnLoG4C_fZnPjTKfoz5DpVI38lv7LtqjueeU19xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b1f3b02d.mp4?token=mNakMuWE0qDkljF1LdIcG6_abF6wQByBGe9nn8yrsnUgxs4DHiDlaQpJQbG1Hlw-aTKlym_EPvUkPM6EijF7gVLD-wlAF98F6ni3lzhSp9EsOTddfos5yh-VaIHgHnHmGPzMFGb3hMmYjURqAEQionUKMy5cjaRo8OVPXDIkzfHtCjSpu0cn8KQ19PiZKCNEjRdO5iL9veQLO3RAq4dC3vOMHLdvEvb5HYsLxFEK8TiMl6vjhUAsQboPLTx0brOVVRk3gNJ_R3w_w4RC-MpxsGYfi5oPHlvGwncEQAwyyG59R0vnLoG4C_fZnPjTKfoz5DpVI38lv7LtqjueeU19xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ربات انسان‌نما در جریان نمایش کونگ‌فو در باغ گیاه‌شناسی ارومچی در منطقه سین‌کیانگ، هنگام اجرای حرکت «لگد پرشی» به شکم یک پسربچه تماشاگر لگد زد و او را نقش زمین کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/akhbarefori/656300" target="_blank">📅 11:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656296">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKwfXJO54a5EoX9g1GTU6CacFvEJRyQqB0qdNAUhMrBbvJVGr-fkFNq7EPxMAp2TP4MndI5t8HwIgrSAzJU0kOl8VCTONwQARyotwwWPIntQ-RK-2xnGOsMhTNvOEE6HuEKsZq5ql3NsZ-f2i327i4d-zofsTgKRjP4Dbbh-0ZaIYWwWxuYkS8SSLqxlk1AfVLLjhtac5SP_R71IGcAcd4VFmWLupsSemcFRTB8hZQhLXWD3Lj4t8PpQf9Wu-PCLI5buCONa1_3H4p8Mx2_59iNIo7o-VCabPE4G86jxGxMTsu3GrMFMnGQXk1D2fMBIoELth9p2qKLAtJUp9luX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntUgxLUXFTXt3_TNSmZVeGvSufO2M4d9WT7uqqIblQOYXAq9k0piObkkkdVb922Iz3CfKC4o3r237XYuvv-wqOrqeB3ILkmRec2OWGqg-7Mlm5DLXDeIMmjWYO6OeYZE-qC3J3_OgTTRXeDUmDfoqjAPNon2zZuzonLRerOe-hQ41asPs6z2xoEIRvGu-D3lCNwYQgOw39qaionPzL9nGOk5nrbQ7wbImglOW8Dp39dT3a11mA7Ip_jNBhDzJePkUXiL3GHiNnm_2BqU7uLKVQoHOf7OEgeM2H9QRXP_r9L3m5yDNKYitVETdJwkyGzN3u8Gb5uUvvhjRNgUakobMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hYNzx3xBJsIbteLe0caM3CS7wXdAXS4ekP8Spq5miFyT7JvzPzg-_7GeJyLvtnfxEzk7-_54JCTxL80OZxOWPwwHoJE8iP1jiEo6GP4TxUhVZx0rJa3YrpkrfAWyntSzOls2JgpTGK-xnXA6qUbqkJeJ7wld6JEhpTpinXtfhlNrAx2V6UNxYyk7QcREWs_GJgb57ZB4ufxw3aoTSmIz7vk6NYskX7tv1uy_k0D9ShAgRVS2lieCr5ejgTzWAxV3dIOKepiDkcE4qJ-PWvcofra3FwmyihxiDCMaSX2_P2APHQ-QFKBFMyf8fbQJ6BBSXUDgxkOXRf7laSsXx0PxSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZLf7cWcfOTMbA8ZLX0i1b5RhqzhoPnO3WBQH-8K_Q9UunkyJqN1o_q_qlLTEuFyFVUDWtCk3vd_HYXWgaQjMXtEiNppd53VCEjONwC46ZF5o9OQQdGK1HFfVkwWDULHL0qHCpWieaTbEf2kmPu7VfGu5OjpWxixbcyx9sNI6DOTWwF5AX-ZBEXlDSfAa9Kb2BsGoxQKbcGbZFwp8JYdVUG_Rzz-koSOFOADxgV5-smbqRW5LcdvQycA8Kntt7QdLl31HkN_qKQZ_0Dkb52xQiQjtqFJzPGydHtWPCvwp5SzZOetlFdppfyqYwfdH3JTxz9A0N5Y2hj5vpWrE_F_ung.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نمایی تماشایی از وقوع طوفان در داکوتای جنوبی آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/656296" target="_blank">📅 11:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656295">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
اسرائیل برای سه منطقه در جنوب لبنان دستور تخلیه صادر کرد
🔹
با وجود آتش‌بس جدید در لبنان که از سوی ترامپ اعلام شد، ارتش رژیم صهیونیستی برای سه شهر و روستا در جنوب لبنان هشدار تخلیه فوری صادر کرد.
🔹
به گزارش الجزیره، در پیامی در شبکه اجتماعی ایکس از ساکنان چندین منطقه در جنوب لبنان خواست فوراً محل سکونت خود را ترک کرده و دست‌کم یک کیلومتر از این مناطق فاصله بگیرند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/656295" target="_blank">📅 11:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656294">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c003bf26.mp4?token=a3824weWZBYHZpQHX-3l50e__wraiN1K6UQks6a1Wi7k5LKarjiGBUfv5EL4XGVWBOeBgdtsjSr9mSM_o_Y1PMAT3dgOjsAgDU0Sn7yd_NcjqZ9kSK4yItDR8jO0_6B47TlZouvTFNqfW5raVRvMvJok8kxt4BsRH9USIKz9ojnPNSqVRQsdvxYG1-Zw7ara0jSgT4les6omiE3pX19-ezjy-Ln3H1CRa0NgZua9TBl8QGnUse3qzYpHrvHCa39OJtVggikTGnaUvB7qziFSuzcWQ1LSXw_BS8mGhbu3Q7iDFZo6He5YXZkOBSzOrmjXr4cflBfR14320DGW3b4nAgLrhZjLpVS-sBJKQiQGmhadFUUwZY5bcUWcvaH7aJq36oXY0Tz9bcncDp_XUXUc2qRWjffCV2tbOvgsfjLQazMAnbvcZeey-uGjjF4tf3qShrdVhD7J5ULSGms5nGUa8hR6W7gracIT1vvsHk7nzsM5nksrfh8fcHy-zysuEEQ7d5OyfgcutbacwCYeG4vTISDaoeK1Q4Z21UxrdIgrIQ3LB6pnsouwHCxS4Px-aG_qI_KpAy9CQ96sfea-IrWrdrzp9EG5JlumwuN0HLLgV8JmohDAiqKLXzWG5yuKXDGDhlPE3YIN4IioJf9JW4l62X7POjxXu66_YPhLf0LOCj0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c003bf26.mp4?token=a3824weWZBYHZpQHX-3l50e__wraiN1K6UQks6a1Wi7k5LKarjiGBUfv5EL4XGVWBOeBgdtsjSr9mSM_o_Y1PMAT3dgOjsAgDU0Sn7yd_NcjqZ9kSK4yItDR8jO0_6B47TlZouvTFNqfW5raVRvMvJok8kxt4BsRH9USIKz9ojnPNSqVRQsdvxYG1-Zw7ara0jSgT4les6omiE3pX19-ezjy-Ln3H1CRa0NgZua9TBl8QGnUse3qzYpHrvHCa39OJtVggikTGnaUvB7qziFSuzcWQ1LSXw_BS8mGhbu3Q7iDFZo6He5YXZkOBSzOrmjXr4cflBfR14320DGW3b4nAgLrhZjLpVS-sBJKQiQGmhadFUUwZY5bcUWcvaH7aJq36oXY0Tz9bcncDp_XUXUc2qRWjffCV2tbOvgsfjLQazMAnbvcZeey-uGjjF4tf3qShrdVhD7J5ULSGms5nGUa8hR6W7gracIT1vvsHk7nzsM5nksrfh8fcHy-zysuEEQ7d5OyfgcutbacwCYeG4vTISDaoeK1Q4Z21UxrdIgrIQ3LB6pnsouwHCxS4Px-aG_qI_KpAy9CQ96sfea-IrWrdrzp9EG5JlumwuN0HLLgV8JmohDAiqKLXzWG5yuKXDGDhlPE3YIN4IioJf9JW4l62X7POjxXu66_YPhLf0LOCj0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دست برتر پهپادهای ایرانی در برابر سامانه‌های پدافند هوایی آمریکا
«محمد الصمادی» تحلیلگر نظامی و استراتژیک:
🔹
ایران راهبرد خود را بر فرسایش، پراکنده‌سازی توان دفاعی دشمن، تحمیل یک نبرد استهلاکی طولانی‌مدت و همچنین ایجاد فشار اقتصادی، روانی و سیاسی بر طرف مقابل بنا کرده‌است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/akhbarefori/656294" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656293">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
دبیرکل سازمان ملل در بیانیه‌ای خواستار عقب نشینی رژیم صهیونیستی از مناطق اشغالی جنوبی لبنان و احترام به حاکمیت این کشور شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/akhbarefori/656293" target="_blank">📅 11:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656292">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef77db9be.mp4?token=cCb07-n44sdvi3wvWsqGJ5zyQK1QS-_tnxLLH6-uk3EMwl5YmUEQfRICTlModIo6WKQYesV-kLns9BUT6JdtYVgcyBWSXlX4OgXcC9iChkmlQ77_bxTN67a9Ayx5ADiFZdN1cNfCz8AHqxTohM77W-I5sX_JVwYEzkjfRemfR88nhpKDwswKbTCvvfjI5nULnk9G7IpKvaNM_J3AZfcEJR4HBkWYJFvU0Jt8Qaq-qDAxF8DIxjN33VeaPP9EEtYeFNoKfSGnZYMMP61YjfDIbu-bFugGugL3c1_ai9b50oWf9mPW_JPnxT3rMr0grKkPVlh32JSfrY-a1dyk5_2LZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef77db9be.mp4?token=cCb07-n44sdvi3wvWsqGJ5zyQK1QS-_tnxLLH6-uk3EMwl5YmUEQfRICTlModIo6WKQYesV-kLns9BUT6JdtYVgcyBWSXlX4OgXcC9iChkmlQ77_bxTN67a9Ayx5ADiFZdN1cNfCz8AHqxTohM77W-I5sX_JVwYEzkjfRemfR88nhpKDwswKbTCvvfjI5nULnk9G7IpKvaNM_J3AZfcEJR4HBkWYJFvU0Jt8Qaq-qDAxF8DIxjN33VeaPP9EEtYeFNoKfSGnZYMMP61YjfDIbu-bFugGugL3c1_ai9b50oWf9mPW_JPnxT3rMr0grKkPVlh32JSfrY-a1dyk5_2LZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقال هندوانه با پهپاد در منطقه کوهستانی چین
🍉
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/akhbarefori/656292" target="_blank">📅 11:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656291">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
نشست مشترک نمایندگان ایران، چین و روسیه با گروسی
🔹
سفرا و نمایندگان دائم، ایران، چین و روسیه در نشستی مشترک با رافائل گروسی، مدیرکل آژانس اتمی، موضوعات مربوط به موارد مطرح در نشست بعدی شورای حکام آژانس بین‌المللی انرژی اتمی را مورد بحث و بررسی قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/akhbarefori/656291" target="_blank">📅 11:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656290">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7WhixmSKPdT49vw1GeEft-rec-CAUKK_MZI4BHN9jsUII3Vr1ChDipRVEwcBGlSGWE1l3kIRNrhRoYnlBgR4k7sCb_RRzkxhM57jjmR5FlH1wfhFb3JYY0_WJIW0z2KfnA0lTwLQnenn682pu0uMGZandRBLbqGtXb-CBpZWNAu6yX7iavRtls3Sn4IoNrnku8o_0do-3-wKn14UVUrwwLdfHMeDRW0J7qG59VNsBvs7IO664uCz2meLly3NYiObvEd3y02lkWLJb_bl4HPvzGNV1yZu-B2zj-DHUsWAPtJJet0tE4A2BLR04ri9wRpjOPxajOYPSYS7Ta0yySy0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های لبنانی خبر از ترور حاج آدم عبد الحلیم حرب،از فرماندهان یگان مرکزی نبطیه حزب‌الله خبر دادند
🔹
پیشتر ارتش اسرائیل اعلام کرده بود یک فرمانده واحد مهندسی حزب‌الله را ترور کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/akhbarefori/656290" target="_blank">📅 11:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656289">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f4873087b.mp4?token=o3RoKjVi4Qs24I6eUKyASNYBTuXVLhbBSCcew9mcnA1bIQYsUTRD1tOtrC4gQ3tCj8OJWHKOTq6CsfmwXyGHXKDFXVECbkT48GRlYzXc5ssdyrZbbvayYpBrAF5IartzGsJuwidHxKor7XAfemr3g-ckkCjVAi0zV-YsyHRq99Mj4XC_hiIYtXhyO8D65I7azpqplbtCgw2oyo4DPSgulA-GY_F1-27-_m2N00vsHkK87J1DmLhShts353GQmhw_D258ozpCQvBNb_6zgbwCmDsOqhHIPN3QSbb0O7BVKgj9wuqqVGU353QI1XNFwzrsKNF9GJZseTwpuDhRjbEHag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f4873087b.mp4?token=o3RoKjVi4Qs24I6eUKyASNYBTuXVLhbBSCcew9mcnA1bIQYsUTRD1tOtrC4gQ3tCj8OJWHKOTq6CsfmwXyGHXKDFXVECbkT48GRlYzXc5ssdyrZbbvayYpBrAF5IartzGsJuwidHxKor7XAfemr3g-ckkCjVAi0zV-YsyHRq99Mj4XC_hiIYtXhyO8D65I7azpqplbtCgw2oyo4DPSgulA-GY_F1-27-_m2N00vsHkK87J1DmLhShts353GQmhw_D258ozpCQvBNb_6zgbwCmDsOqhHIPN3QSbb0O7BVKgj9wuqqVGU353QI1XNFwzrsKNF9GJZseTwpuDhRjbEHag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش جالب امام خمینی(ره) به تمجید آیت‌الله مشکینی از ایشان
🔹
ما آن قدری که گرفتار به نفس خودمان هستیم کافی است، دیگر مسائلی نفرمایید که انباشته بشود در نفوس ما و ما را به عقب برگرداند. شما دعا کنید که آدم بشویم. دعا کنید به ظواهر اسلام حداقل عمل کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/656289" target="_blank">📅 11:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656288">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bead13e540.mp4?token=bcAoCnrTzRZiRCs1FbmW2NMW2sHZMkIKM8oypuEMIKdN-fGxVNnB3uRDSyKBipBVN_Oq164-DMcpl_VjazyrekjoV7hmgG3JAbUOVThi88n89OHkK5UvFrfj5rs__R-6ikK-Odt3EN0JW2CEjwdcl9XdYMDtiDzQt2sZO4BPsACEB_GwTDAT1uwkhZaV66t-OmeCTTBdwU0pL2NIVdqoxRIwZ9qajlZ84LJUKXDOCPP5ChrjRYW_xWJcafP8OGlpgnusUPaI23sea4N5jXlqEdxXXmcmwqQvSxr7QUVS9VxkSsvRXH2QXnBwJOSNYPH1_le5f3AH4yM14q72IFS10w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bead13e540.mp4?token=bcAoCnrTzRZiRCs1FbmW2NMW2sHZMkIKM8oypuEMIKdN-fGxVNnB3uRDSyKBipBVN_Oq164-DMcpl_VjazyrekjoV7hmgG3JAbUOVThi88n89OHkK5UvFrfj5rs__R-6ikK-Odt3EN0JW2CEjwdcl9XdYMDtiDzQt2sZO4BPsACEB_GwTDAT1uwkhZaV66t-OmeCTTBdwU0pL2NIVdqoxRIwZ9qajlZ84LJUKXDOCPP5ChrjRYW_xWJcafP8OGlpgnusUPaI23sea4N5jXlqEdxXXmcmwqQvSxr7QUVS9VxkSsvRXH2QXnBwJOSNYPH1_le5f3AH4yM14q72IFS10w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از این دسر سالم و خوشمزه که ترکیب سیب و شکلاته درست کنین و لذت ببرین
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/656288" target="_blank">📅 10:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656287">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
العربیه: وزیر کشور پاکستان برای دومین بار در عرض ۲۴ ساعت با همتای ایرانی خود در بیشکک دیدار کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/656287" target="_blank">📅 10:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656286">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqIdcdVAQVTr-UaJLAz-3dyMGw-A9d20OgsKDjurVjOKDSoDhs7e2yJZjzMXKsPVM6G954IqWuJTWjtJ6dCGcaCo77LIZRUXVi_lMd_eyCm1Dt6PH_RaqC4m5iEMNm34QAL4hQayXnr0xpbzpmg92JRlVaUICBNFf33hjy0eJQc0KT5Ict5Dtd6E_AElBiD_qNQyhNQvyYca8MO95qbjT_I_H7n0sE3SmJbk3S2zzwShp8NZAB-KhgIQGuATr2UpFXrwIJPwl6SJDZkwu7X9ryonJbMqldu0KR3x9tZ2LB4toxZ2bVVBj7eYJNDcR7zdAqrdkCXkWEYkkDQ6OYZJZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس پلیس راهور تهران بزرگ: تردد اسکوتر‌های ایستاده و نشسته بدون پلاک در خیابان‌ها و معابر به جز بوستان‌ها و مسیر‌های ویژه ممنوع است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/656286" target="_blank">📅 10:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656285">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نتایج آزمون EPT خرداد دانشگاه آزاد اسلامی اعلام شد.
🔹
وزیر خارجه روسیه: آمریکا و ایران باید گفتگوها را ادامه دهند
🔹
پاکستان: تلاش‌های دیپلماتیک برای صلح پایدار در منطقه ادامه خواهد یافت
🔹
فعالیت در بندر الفحل به روال عادی برگشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/656285" target="_blank">📅 10:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656284">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea408e562.mp4?token=nfjEIecc10UQaczbIhwzD-miqAGnPPvq7bsju0iIJSKIEyWWYLjEB86fHve-cfvEHEs5yJThR9wsygC-i2kAfSPWgReEl9qLQsBz968kFZKDHLySWAA0j3j-PsRvwINuNfPP7zhQGkxwK13sGl8aP5mGvxcwyln9wa7fm5JDQWriI1NnbUZCcAn0u4cl-vkg8atHWaY5KJUUN6VEp8gKBqvFHioNA2RWj8r82E8_1kui16N8RqF4OPtzz9mfqkwPxRJ-0TzIcTXKJtSGv3HczaOUcApXqlDXMblbwfb_7YyKlC11fk64pEOXYs1nUC-HfsAlAwGMfXj13HKDiaPxuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea408e562.mp4?token=nfjEIecc10UQaczbIhwzD-miqAGnPPvq7bsju0iIJSKIEyWWYLjEB86fHve-cfvEHEs5yJThR9wsygC-i2kAfSPWgReEl9qLQsBz968kFZKDHLySWAA0j3j-PsRvwINuNfPP7zhQGkxwK13sGl8aP5mGvxcwyln9wa7fm5JDQWriI1NnbUZCcAn0u4cl-vkg8atHWaY5KJUUN6VEp8gKBqvFHioNA2RWj8r82E8_1kui16N8RqF4OPtzz9mfqkwPxRJ-0TzIcTXKJtSGv3HczaOUcApXqlDXMblbwfb_7YyKlC11fk64pEOXYs1nUC-HfsAlAwGMfXj13HKDiaPxuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از اشترانکوه زیبا و باشکوه
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/656284" target="_blank">📅 10:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656281">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4UgZSc45aCGZQyI6nWK6VXtIcGCvsfrv987GqhY-ebU_q4f9LtKtJcipmKzpTlro7ABc3gXIPO5WQE3HgzomXYFUnL3f6lKKOEsdimxVqonUmWmf3wckOnwTKG8AFA8nb36qs9bvGBZnVkLmsUGKeTrUMi-VUqRFGjAiajlaVe7T6G96Cv06GuvYMzWM4ZOvLlVZnNaQ9wIz8xFfVHhLdmudPM8E3yWw-O0QKDo5ZHxT3NfWbpSy6zdS2YhUpvuDtF-X3rDzheal_ILUuCWtsBcmV7noUFHvkXZ--ESf2Sm25ash2TOYo-mCbJGqDKBgRPjAwHXGVeKKuXN_pgQdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f540d5f5.mp4?token=SFiC1owhvqHhyxOGlt7nhCpz-fUDyCXUtXkqz_rB9CdsWvl2ljjduOlFUjPLYEA-ljH8v5Avnjx6S0Ty8fDlnL8Kzi3hmCbx4NqVhmNBZyjAIm7tgxkdTR7Urfq9UhcIUM2IlLLUmqqo4grlEmSkRt97PUSd4wi0uke4z7_LdNQs1haxZGkV8so8rBRK2V7kuNGFx-F0wLZgpqJoqJp8T3iwdcYXwMAfivrUZvuO-wUZR3SbzPSxTgH5uatEEZw5UYa1EyfrP8BaO_hcZr5LAPuWx273YrwI-DyZHdqjVORenPf17kzWuvkqriB17MmxzDTI8WYUE_-MW-xoj5zvAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f540d5f5.mp4?token=SFiC1owhvqHhyxOGlt7nhCpz-fUDyCXUtXkqz_rB9CdsWvl2ljjduOlFUjPLYEA-ljH8v5Avnjx6S0Ty8fDlnL8Kzi3hmCbx4NqVhmNBZyjAIm7tgxkdTR7Urfq9UhcIUM2IlLLUmqqo4grlEmSkRt97PUSd4wi0uke4z7_LdNQs1haxZGkV8so8rBRK2V7kuNGFx-F0wLZgpqJoqJp8T3iwdcYXwMAfivrUZvuO-wUZR3SbzPSxTgH5uatEEZw5UYa1EyfrP8BaO_hcZr5LAPuWx273YrwI-DyZHdqjVORenPf17kzWuvkqriB17MmxzDTI8WYUE_-MW-xoj5zvAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنجال بزرگ پروژه لوکس کوشنر و ایوانکا در سواحل آلبانی
🔹
پروژه تفریحی لوکس با حمایت جرد کوشنر و ایوانکا ترامپ در نزدیکی تالاب حفاظت‌شده نارتا در آلبانی، با موجی از اعتراضات مردمی و فعالان محیط‌زیست روبه‌رو شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/656281" target="_blank">📅 10:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656280">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlSbN6JuGHq9M9Hwu-GnsBz0R9zcHS4J1kiXBFbTw5_6tauYwK-KorJEMUakDlyabiwxwGEtZ71nKMm6EYojyl1x7BBiW_HrhlJ6racx9oZDcdF4hdA53_k-WGlZRv6qCQF9zO9ZO91tyB9Z-5ld1QgvOdsV-LJ09rJMjdlsvp0a4qUv8OFfkGsOfJqg0TrS-LV_Qxg54ih4zBxvNGbXoqae6LsSTdicyE8l_GLdpjTQBXUD6cxA5UK9VZ080RR0nL9wwQF04Wc3KahB34VHAlAbo4FtkuAeJP46yKIZliBm2xD2X947du-HcRlaxtc_IG0L7GRp8OpWNytx39P3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تغییرات عجیب و بزرگ فیفا برای جام جهانی ۲۰۲۶؛ از آرایش جدید بازیکنان تا پرچم‌های غول‌آسا!
‌
آرایش جدید:
🔹
هر ۲۶ بازیکن + داوران هنگام سرود در زمین حاضرند و دو تیم رودررو می‌ایستند (نه پشت هم).
🔹
پرچم‌های غول‌پیکر: قبل از سوت شروع، پرچم‌های بزرگ تمام زمین را می‌پوشانند.
🔹
هدف اینفانتینو: نماد غرور و اتحاد با نگاه روبروی بازیکنان و داوران در مرکز زمین.
#جام_جهانی_۲۰۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/656280" target="_blank">📅 10:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656279">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b234d7bd0.mp4?token=W5oiMubNxaeq-ggyiMIVGAkAZQmTEKRks57iiGPpic3sp-_AZeM1QKdBNIWhgn13SM95Z90428bjwnI5qouk46GtmA-xKDWgQoWrFNr9l4gLzMmLXRlFk3F-FFBRu5xNvlttsz7n1Kgqvt812F17266NlbMDx_PcLWMCDGFv_X4OCvuaah3pLb8MpG-7ioGDeZ-4ygzXLog80zswDCG8PuWmK5mMxBdJVcxmjVRbggKKsLXif0awPoHl3Np2RPpXGaUqoOlnTbPA2vTvXeNitsvbP0xhmedLIUYfIhfZzhkh1-DJZoP-BViXR5nMvuhI7YEEy6LZo4a2cvwgr8oQYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b234d7bd0.mp4?token=W5oiMubNxaeq-ggyiMIVGAkAZQmTEKRks57iiGPpic3sp-_AZeM1QKdBNIWhgn13SM95Z90428bjwnI5qouk46GtmA-xKDWgQoWrFNr9l4gLzMmLXRlFk3F-FFBRu5xNvlttsz7n1Kgqvt812F17266NlbMDx_PcLWMCDGFv_X4OCvuaah3pLb8MpG-7ioGDeZ-4ygzXLog80zswDCG8PuWmK5mMxBdJVcxmjVRbggKKsLXif0awPoHl3Np2RPpXGaUqoOlnTbPA2vTvXeNitsvbP0xhmedLIUYfIhfZzhkh1-DJZoP-BViXR5nMvuhI7YEEy6LZo4a2cvwgr8oQYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گربه‌ ایرانی، فرش ایرانی و موشک ایرانی
🔹
یه خانم در بحرین این ریلز رو از حمله موشکی چند روز پیش ایران گذاشته، اما بهترین کامنتش این بود: گربه‌ ایرانی، فرش ایرانی و موشک ایرانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/656279" target="_blank">📅 10:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656278">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPjwTDRyN3MXzt1nwhzcdRPpg3YQYD9zWYUsAKyvmteSXXn6eYMuvTchf69H2WCkppGqB70yhjbg3SzcI4CSSnyKvcWRaiMF5lVUh4CHox38m6Ho3Vyq7fuhIDryftzG66VgiMROUZrlNz2d6Oy8AaCNIC5q7thBWrrQj-RsIT1Uam-5bywJHE-TnLqrVN5597zM2ZnLdYj_1B25Ni3kBGFVG7KTbkGZveJJvW_2AQwtCv12uiq0nsjiMvcy8-lXT26f1VH68Y_6-cNJ7oEKFrqtMK3xm7tQOXxy7QyCsslV2I2GJcJtiST6B8mb4b-KSNj7cNYpzKTqy_hb4VoMMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر جدید منتشر شده از میرحسین موسوی در بیمارستان قلب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/656278" target="_blank">📅 10:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656277">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ff8fa43c.mp4?token=aODbV-E5zZ0-CWTu5KtHVRcHuQLFpiTD87fgMDOwWsnPlwkzs5sVhIcdBrsHM6Xnd7p0zbXZStlts8Fl-fZBb-xPAHacZ-lNr6x32lIdPo0yPrgzvgOcRXRy0jEIsIuxbKLp6s-uO8YbAN4iEyIThDQyH4Ffu3hrSFYt6qDrvimKEpKFNIFTzrQT06pFai05rkKQxA6sdy08pGNvFoL6blrv57zVJp2wqVpB2SKzNKYpo4jkgPyhwWEQzqXwWjA7PpfLxWs2O7Sga1cnoPQVHRLE5WoPO1_BzN-nURzDZFvhTpD_Vl0yPxlUHxILjFKrg-br2kZOGean2oUcasm3kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ff8fa43c.mp4?token=aODbV-E5zZ0-CWTu5KtHVRcHuQLFpiTD87fgMDOwWsnPlwkzs5sVhIcdBrsHM6Xnd7p0zbXZStlts8Fl-fZBb-xPAHacZ-lNr6x32lIdPo0yPrgzvgOcRXRy0jEIsIuxbKLp6s-uO8YbAN4iEyIThDQyH4Ffu3hrSFYt6qDrvimKEpKFNIFTzrQT06pFai05rkKQxA6sdy08pGNvFoL6blrv57zVJp2wqVpB2SKzNKYpo4jkgPyhwWEQzqXwWjA7PpfLxWs2O7Sga1cnoPQVHRLE5WoPO1_BzN-nURzDZFvhTpD_Vl0yPxlUHxILjFKrg-br2kZOGean2oUcasm3kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرتاب کفش و زباله روی سر کاپیتان اسرائیل
🔹
تیم فوتبال رژیم صهیونیستی در یک بازی دوستانه مهمان آلبانی بود که تماشاگران این کشور در جریان بازی با پرتاب کفش و زباله روی سر کاپیتان اسرائیل از صهیونیست‌ها پذیرایی کردند.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/656277" target="_blank">📅 10:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656275">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHAgzhPneHXl0Kfdfb9a7vtLF9-Slvwg9WH_brIEKG74LjDH07bP4oH-yimCN6qtvSMiZcRj3ULeGUqCGMSFI_CSSIh347FqMFpNW7mEqssGs7jbcZjS7zTxniJDXYAvHNo2CdhmDNimkZ5xQ21ql7H4VQyOWQavW-AYBIdStQj8NbHE93OC922x5geqSv8o8dB4xdg43rCqTRGkDuU9w7JTpbBa25bIdeQ3EJSKZIv7GI4hYxizzUW7b5uv9WTR2WMcdGqaglMw1DqScyCY3rftj7SJ3l0htSrf7ibOUUs5ZamAR268cCCmP49vKoX5GyU7m37__bGHLsdMnAHwfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس‌جمهور چین بعد از ۷ سال به کره‌شمالی می‌رود
‌
دولت کره‌شمالی:
🔹
رئیس‌جمهور چین به دعوت کیم جونگ اون، رهبر این کشور در روزهای ۸ تا ۹ ژوئن (۱۸ و ۱۹ خرداد) به پیونگ یانگ سفر خواهد کرد.
🔹
این سفر در شصت‌وپنجمین سالگرد معاهدۀ همکاری‌های چین و کره‌شمالی انجام خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/656275" target="_blank">📅 09:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656274">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
مرحله یازدهم کالابرگ الکترونیکی از امروز آغاز شد و حساب سرپرستان خانوارهایی که رقم پایانی کد ملی ۰، ۱ و ۲ و همچنین خانوارهای تحت پوشش نهادهای حمایتی و نیروهای مسلح شارژ شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/656274" target="_blank">📅 09:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656273">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osc9pSHtpj1ifnJHXL7eS-r4zZ2Di9Et8pOaTmZfQs63l6YD9QvdtSZ6u5yaPCRpWUtzCct8wKNXV5lUE5LMcD2QaLHHwipfx-U18Z8u4nN1wnjz02KgMjku416XKR8e0wZjPPaB5hHOafQAXOabsdPe2ckWhYHQd3a6vdJ-nupMStUgYEcP9sVqJiLeAjP4CoMbPVBG_z-ZPVGtOFQbY9uouEjYyKgKRrxZmDVRL-AjT-URUb3Vyc8btI8BV1AisuYr177YdlPXnCheitwILvrV4udNz3q_j6vd8Rg2JuOkdmq1DJDFPUJbro8NvNSJ3n67vWwsGzQpzBanUZA1Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دماوند با شکوه
🔹
امیرحسین گوهردهی
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/656273" target="_blank">📅 09:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656272">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c003bf26.mp4?token=pixPHAg4bL_FMcyntG3_B6yyL7cwuU3db6A3Gc_6ZBkJRgBoYJuZ77hALmg3Z4ofM6WJbFf2_ta5ipsbg7iR6bLvT4hBodjrabmRkGSurEs1jJDiOhWMd4h7jU5k9fRhV3q8DKHPyYC1F35ReB-whq0ugHlsWX3tiDJhJcsEfRVKJCBK0SMPIy1s54SfoZ7neiYuITtZ1DayFljyoIEWEm7t5zZGStfU-hnquE04AxYLZ_e8YEVJV72DWs1ZT6WEriZevKcTVcYovxVMKBlqXPGDZv0vEB8r92aBc9gJV91tIH8NAY2wNTo6ojE8Op4gBxF5NsVO7rcE0E8wHDJWQWsfyKM2-V2U6UGdKGTzBYuOnAHmQoMExNMW3VBe_E7_q6cqHM5XSTmoMAGJmh-PuFXGWzqFccnpvGfwFKaq4bcVGeQHnYvhwBgbH1a3Ac94k5NZ-EUm1V6-5nUT5LLyAYpO2CZLw5IYoZ-0rhzgiSxq8ofEub8WrqHF5iolkU0LhYr6bb4bnNDiqaMSsu1j5QqV-SxX-1rLtM36MOz3iYiuiB8yQDpSYZ3YZ8vPxtXzBwwYDjnH5Rt2vczuTKmaULcQXokFkH6W5Xk0mG9OMNP1_0Rt_2iUDIgI3qZkqM5W_7rT8VBJqHGbMc46gzzq54XIokqZjeCLmITUU7rBZ7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c003bf26.mp4?token=pixPHAg4bL_FMcyntG3_B6yyL7cwuU3db6A3Gc_6ZBkJRgBoYJuZ77hALmg3Z4ofM6WJbFf2_ta5ipsbg7iR6bLvT4hBodjrabmRkGSurEs1jJDiOhWMd4h7jU5k9fRhV3q8DKHPyYC1F35ReB-whq0ugHlsWX3tiDJhJcsEfRVKJCBK0SMPIy1s54SfoZ7neiYuITtZ1DayFljyoIEWEm7t5zZGStfU-hnquE04AxYLZ_e8YEVJV72DWs1ZT6WEriZevKcTVcYovxVMKBlqXPGDZv0vEB8r92aBc9gJV91tIH8NAY2wNTo6ojE8Op4gBxF5NsVO7rcE0E8wHDJWQWsfyKM2-V2U6UGdKGTzBYuOnAHmQoMExNMW3VBe_E7_q6cqHM5XSTmoMAGJmh-PuFXGWzqFccnpvGfwFKaq4bcVGeQHnYvhwBgbH1a3Ac94k5NZ-EUm1V6-5nUT5LLyAYpO2CZLw5IYoZ-0rhzgiSxq8ofEub8WrqHF5iolkU0LhYr6bb4bnNDiqaMSsu1j5QqV-SxX-1rLtM36MOz3iYiuiB8yQDpSYZ3YZ8vPxtXzBwwYDjnH5Rt2vczuTKmaULcQXokFkH6W5Xk0mG9OMNP1_0Rt_2iUDIgI3qZkqM5W_7rT8VBJqHGbMc46gzzq54XIokqZjeCLmITUU7rBZ7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژنرال بازنشسته اردنی: پهپاد ۳۵ هزار دلاری ایران رادار ۵۰۰ میلیون دلاری پدافند تاد آمریکایی را منهدم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/656272" target="_blank">📅 09:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656271">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNAYWa40l9nmadme9Zpd2P28-TtEKErGwwSIY4-HgqldI8gLrwRlM9wGytnLMrQqnb3GngM5XVK-FuxpzWedN9hCKap2dAcQqKz1vAvveGd3beZS2WBkt0Qcm6VJiQR3BcMMHxRt7vCINxs2BCB-UFSWq7uGVFuA9nZcklqX4OJy6DM1m_iDtMxv2JzEHQmlfbGJmJEvAdciAQHJJ1uhIjSGM2b31OXLb3LlJj_y0vLSS-dbE6oJtO0hHCYqABlMywXWVWnCtzdrc_95XgcjqwILQhmTG2IqfQeNI7XLHC6my1_mjltpU_Wy57HDBWOptgQpHqYtRQpiMreVCs68vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir/
نوشهر
📍
دریابیشه
۶۰۰ متر زمین
۷۰۰ متر بنا
تعداد خواب ۴
استخردار با تاسیسات
شهرک با نگهبانی ۲۴ ساعته
سند تکبرگ و مجوز ساخت
دسترسی عالی تا دریا و جنگل
🔻
برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir/</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/656271" target="_blank">📅 09:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656270">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نائب‌رئیس مجلس: غنی‌سازی حق ملت ایران است
🔹
آژانس اتمی: اطلاعی از ذخایر اورانیوم ایران نداریم
🔹
رایزنی قطر با کویت و فرانسه درباره مذاکرات ایران و آمریکا
🔹
روزنامه یدیعوت: نتانیاهو طرح آتش‌بس لبنان را ارائه نکرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/656270" target="_blank">📅 09:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656269">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFTq9tWHnV7hEgfU5fgc_zD_gG8KqtDjclGfKvEV7dSSfeUFicniKjEXzu7VEzvD9gpNxUblmMeXY8kNPNZBx4EpKEew9gIsrsGlfavRnAtIWh8eM4PqKp145SCbePqGueLY_w-gUYUexA4URtlpJ-JATGsi-5J4jTdBr0VSq5O0l74wF8AmCZokkj3kL6ZvXV2BFzd55xzQgCKDUxxbkLjhrG0x6OY7jfCyDgF8UyZErVs_pZiTGguQU_gaufdED-44T3PdRsxdNMW1pQ9dYJFSMnb7ixP4dq0pd7qCNjcIRx6QjVtNavzmlatcGRwPuBYOgeUSdgpTyikKFDbIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس تیمی جالب نروژی ها قبل از سفر به آمریکا به سبک وایکینگ‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/656269" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656268">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpMDlj-Bvr39MQkbpr0ReD-Sw7stbbJm87T_WQeFgpuNQQ3_ejP2jwdyuI5Vk0uu9ziOQ6_u64Z-yaIJIq0F_AMahOvYJbhtNaC_jgBIsLfMF_2XNHOWieIWxxjCiV30Mv72Qu8BSaxcDAlEwa-WW8Te6TQGjJuwVxo_zwRUq0gtfnRQdEceQzrsewis_pSGPfzbpnWlJDq8bTNtfyIV-ZzvyG0_TOZdKXTg1e585Ge6rQw1F-UHBfwBwIVn2u7RQHZdGKtJwsUtgojWELY64PWbyBMBTU4dA01GKBO3ezzzZjXuLkwDfXzY1-joPIIEX0W8jAI5ibJP5fBKBSt53w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش بقائی به ناکامی آلمان در عضویت در شورای امنیت
‌
سخنگوی وزارت امور خارجه:
🔹
ناکامی آلمان در کسب کرسی غیردائم شورای امنیت سازمان ملل برای اولین بار پس از دهه‌ها، نشانه اعتراض جامعه جهانی به رویکرد ریاکارانه و غیرمسئولانه این کشور در قبال نسل‌کشی فلسطینیان و تجاوز نظامی رژیم صهیونیستی به ایران است. وی افزود: آلمان سلاح به رژیم صهیونیستی می‌فروشد، نسل‌کشی را توجیه می‌کند و تجاوز به ایران را «کار کثیفی که اسرائیل برای همه ما انجام می‌دهد» توصیف کرد.
🔹
بقائی همچنین به سکوت آلمان در قبال کشتار ۱۷۰ دانش‌آموز در شهر میناب توسط موشک‌های آمریکایی اشاره کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/656268" target="_blank">📅 09:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656267">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAzA1ShcyjfxJzk4bfmYb2Gf4EkprLA2VWfLnT-jYbezoVZZ53eCsejV3poXUPA7Elw2qjpjuCiVB8ig40ckDUEp1N_mdHUff3QgmgJfyXreiQR_xBX4PQJ5xbKhP-mv5QepfCq9hJBpmbJCHESOodmOSgH8qOCeW5e1nUPyWAGWJMwG29L5FMafqJfUfB_IJI4a1eoDomambr6mFUVzRd2pYC8_o3ckO9AyJ2crH_aAqppB4fwkCwlyEJu2F6PyVFxqVN0inYAeWPvS0uV_ECim94B1DBohftXa_DcAX49TxXWpafYiLOYUJXVRHSyvy9YxgSvQ6_EYOryRWrht8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: با دیکتاتورهای منطقه به جرم تامین مالی و نظامی آمریکا برخورد کنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/656267" target="_blank">📅 09:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656266">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95f26bbeb2.mp4?token=M5kBo6WJxADVUiUta3hWexVWLuAME5tAZgVsfYSmevBo0Tx6qBst0zkKHkiOqhHTkWJPtThzh1PI3aP51qYTj-omCiIDtzM022shNfs0p3EP3qKhRf46oHpbX7zISXaZEQBZ1nl0LHf7UQzahCeMmKAi1v5iYXMokKVi8pmX0mkUnYjM6rnORpD1LiJtwyd3kfab25VjAekC-w9dgFAS6e7axPo-mMEQt3RU46Z2xbMBp7S5X-m-EVA4bvB-0cLmIawCweIxTOEnLHVHRenJKVLqmXHFtuRUnGc3q8svuuN0yIYDdLgvmMARUmSd65mnVE6Vak3Y3jVDE0d_cgBM6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95f26bbeb2.mp4?token=M5kBo6WJxADVUiUta3hWexVWLuAME5tAZgVsfYSmevBo0Tx6qBst0zkKHkiOqhHTkWJPtThzh1PI3aP51qYTj-omCiIDtzM022shNfs0p3EP3qKhRf46oHpbX7zISXaZEQBZ1nl0LHf7UQzahCeMmKAi1v5iYXMokKVi8pmX0mkUnYjM6rnORpD1LiJtwyd3kfab25VjAekC-w9dgFAS6e7axPo-mMEQt3RU46Z2xbMBp7S5X-m-EVA4bvB-0cLmIawCweIxTOEnLHVHRenJKVLqmXHFtuRUnGc3q8svuuN0yIYDdLgvmMARUmSd65mnVE6Vak3Y3jVDE0d_cgBM6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگترین نقشه سه بُعدی تهیه شده از جهان هستی، شامل بیش از ۴۷ میلیون کهکشانِ کامل
🔹
هر نقطه نورانی در تصویر یک کهکشان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/656266" target="_blank">📅 09:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656265">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
مرحله یازدهم کالابرگ الکترونیکی از امروز آغاز شد و حساب سرپرستان خانوارهایی که رقم پایانی کد ملی ۰، ۱ و ۲ و همچنین خانوارهای تحت پوشش نهادهای حمایتی و نیروهای مسلح شارژ شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/656265" target="_blank">📅 09:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656262">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dt4SE8LP1O8rHxJKBBR6Aq1a_86oOhDmnkNlkl2129pfl5EiI6la9j9IAQGG-XClusO9VZYhfGzS9HWOKYT7HqRoVsqq22KT3QieuacIh7a_ANBxtj3sIHt5oSfxxsmyaW6tJ1LhcWOHFZIkeMD4gOM_vaAbpoMU8vK4SrTr43C0gcHMJaNfud6sokHT3i0xVVSpvPG9DNh4dKXmpXdQ5SPZo41Spk4GmpFPBT60CPi_8WCoMPfzJ3n9M2916JFzIRgn7WGzGqEoA1jPlEEyNgPRQAnUvF1yzOk7WBgZpO-XPoU9LC_PuAIqHjChEPcgFKsx6khGCCE-3-ANaFk5UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqhaqeapn3C813_IdKoYML2lKQbMirgFiWqkrlRXrzIsv-Rq1csc5dI4k1tegeDcLSn8aaF0KFNj0Jzep4wEfi3wVeV372KATH2pYker0OKc34ZL7mP0mIogBqXojblLa9SyWARcrgtUpuPQbGFA91w1JJfEepx8RriRpgYAVjFVInieKIYcfu6sDue-5Bb5CbZsnHbEpI1ryOFCGqTy899LtFe8MW_1H1VJR9Uv6TIqdeb7llDbXGo7T5fPzWA2NUDB_oiwGif2PHBAtBansvBJfNkHNDFBCZODnF9AlfT9T42ge89jPKElPv8RGE7E485TA74JIKzCbUEkDSeGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqZ3Gty7e5lK_kZMQRcTcFBTg7P3u1ChhSrRghZNCQnwAFl6vbwr2MTRdKzk-r_M2E0vCojNMzVp4KjWsuBaaUe9jBmIOIbNBw9eEQNXPlz2L-8FtmUl4IPFv8ubNtyYw6cgdyxJc-uMu1xYF5i_9qKS44LJR_kIPVhNaa1YKzk1GKkLuppCQu_VqLpMD_Apodx0JswT8c6JPTjXJMSTc0tqC61ZMaS25CQRnv59qXP7CFrnR_eMAAGTFe0-6lE_Sd-GSjltkw2Y8TO5cr_EEnBf-H-y-GOBOgfOXnqLyWcUQmwnsCFMaPALYWquPS0OsJA1CYB8sH2x-wIfK9Z4FA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری دیدنی از لحظه وقوع طوفان در منهتن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/656262" target="_blank">📅 09:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656261">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
روزنامه عبری یدیعوت آحارانوت: کابینه امنیتی دیشب به پیش‌نویس توافق آتش بس در لبنان رأی نداد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/656261" target="_blank">📅 08:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656260">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون عراقچی: اصرار ما این است که ۵۰ درصد از وجوه بلوکه شده بلافاصله با امضای یادداشت تفاهم، در اختیار ایران قرار گیرد؛ مابقی آن هم بعد از طی یک یا دو ماه
‌
🔹
رفع تحریم‌ها و مباحث مرتبط با هسته‌ای در مرحله دوم مذاکرات قرار دارند./ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/656260" target="_blank">📅 08:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656259">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
نقش استارلینک در تسهیل حمله به ایران
🔹
به گزارش رویترز و بر پایه اسناد افشاشده پنتاگون، استارلینک با تکیه بر دیش‌های قاچاق‌شده به ایران، زیرساخت ارتباطی هدایت پهپادهای انتحاری مانند «لوکاس» را فراهم کرده است.
🔹
این پهپادها از طریق ترمینال‌های استارلینک، تصویر زنده و فرمان هدایت دریافت کرده و حتی بدون اجازه مالک به دیش‌ها متصل می‌شوند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/656259" target="_blank">📅 08:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656258">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a2ca91df.mp4?token=FpNntAhoigT-mjDUYDEnzR8j_0C8WlTPc3CH7IoDLUvGzDqeKlypUHnOL2cAfbq_5cGa1OuwDxUpBx5Pi7oxqYiM1PRJpEFNWHp4b7eHLz9PUSLTALBG50Ul9WC-NFCza-i9_G38Dzz5VdYoa1oBM0C1NVNDgQVNmqWkSGWQR3h0rfr9BfzI7Xa0dzOyTIAC7Vbx0XhZPufdgh4D0LirAcz5deyqdPM4BYFz2wCLLj37hU_nz190MJH1o8R6jrEjYH-CPwyGOYwAMfxiQFU6ZTxbsr6_5YMoPlKZcuLj5j2V__I-pXyFlViJE6wYaTbljFH2z3cLwKufmoU8acZIqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a2ca91df.mp4?token=FpNntAhoigT-mjDUYDEnzR8j_0C8WlTPc3CH7IoDLUvGzDqeKlypUHnOL2cAfbq_5cGa1OuwDxUpBx5Pi7oxqYiM1PRJpEFNWHp4b7eHLz9PUSLTALBG50Ul9WC-NFCza-i9_G38Dzz5VdYoa1oBM0C1NVNDgQVNmqWkSGWQR3h0rfr9BfzI7Xa0dzOyTIAC7Vbx0XhZPufdgh4D0LirAcz5deyqdPM4BYFz2wCLLj37hU_nz190MJH1o8R6jrEjYH-CPwyGOYwAMfxiQFU6ZTxbsr6_5YMoPlKZcuLj5j2V__I-pXyFlViJE6wYaTbljFH2z3cLwKufmoU8acZIqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرت ترامپ در کاخ سفید سوژه شد؛ بایدن رقیب پیدا کرد!
🔹
ویدئوی چرت زدن ترامپ در نشست رسمی کاخ سفید سوژه فضای مجازی شده و کاربران با طعنه می‌گویند او که بایدن را «جو خواب‌آلود» خطاب می‌کرد، حالا خودش رقیب جدی بایدن در این زمینه شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/656258" target="_blank">📅 08:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656256">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
آژانس بین‌المللی انرژی اتمی در گزارش جدید خود اعلام کرده  که ایران به جز نیروگاه بوشهر، اجازه دسترسی به هیچ تأسیسات هسته‌ای دیگری را نداده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/656256" target="_blank">📅 08:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656254">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6145ccd1e6.mp4?token=GxpCgp7jwzG_S4PZepsIlRKpnlYOimEngtXD2wJIBCRdLV3F6feLxDHhfd-XBUMgZFLj3ZVHB0sxDaKMKock2sD_ZENzu0sb_7rvF1weIvLlvqtEmrD_2Q_0ze_OAIO9CAKxv2zNfhab1uZ-hVQG6Q0vpdu2oZe60FkO55Icd17eaHYTL6MgCOJauZkZu2gHpG3L4C7UFLN_BMCoWg_E_mgkEthAn_gfLr0YAqbAbsOZHLtMiVcG10t9rt9ZcbiSKioA29auBFswxDmhfjJJZ-0myAbrTVK0Tc_iaC3FOlSK_ZV4ZMXHKqxTXEzFJ07X9tUpYZpM4gQAbe5Bc9mCjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6145ccd1e6.mp4?token=GxpCgp7jwzG_S4PZepsIlRKpnlYOimEngtXD2wJIBCRdLV3F6feLxDHhfd-XBUMgZFLj3ZVHB0sxDaKMKock2sD_ZENzu0sb_7rvF1weIvLlvqtEmrD_2Q_0ze_OAIO9CAKxv2zNfhab1uZ-hVQG6Q0vpdu2oZe60FkO55Icd17eaHYTL6MgCOJauZkZu2gHpG3L4C7UFLN_BMCoWg_E_mgkEthAn_gfLr0YAqbAbsOZHLtMiVcG10t9rt9ZcbiSKioA29auBFswxDmhfjJJZ-0myAbrTVK0Tc_iaC3FOlSK_ZV4ZMXHKqxTXEzFJ07X9tUpYZpM4gQAbe5Bc9mCjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقام سابق آمریکا: جنگ ما با ایران از سال ۱۹۷۹(سال پیروزی انقلاب ایران) آغاز شده است
«برت مک‌‌گورک» نماینده سابق آمریکا در امور غرب آسیا:
🔹
ایدئولوژی ایران که تا حد زیادی سالم باقی مانده این است که آمریکا را از خاورمیانه بیرون رانده و اسرائیل را حذف کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/656254" target="_blank">📅 08:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656252">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
خبرنگار الجزیره در تهران: یادداشت تفاهم در مرحله نهایی خود قرار دارد و در انتظار موضع نهایی، چه مثبت و چه منفی، است/ تهران هنوز تصمیم خود را نگرفته
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/656252" target="_blank">📅 08:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656251">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08f96b91ae.mp4?token=HhSkYVttHJZs4_FWZPtV3LfpyEExVi1QZpdG4vuvyEOPtS00M_vsKAiOnk5hR3epHezGXuohXAquGK1oeAFGLb0irogMgFWS5KzWUEJ70YM7l9FVgecm3Z2kuRrR48qd4QaWu3mumt_8iE1PA-Fnbrdk0kEESCXJjLXll3IND_mXZ1ivpW_g8Jfxq5npxBPPh56JjFte75G7Tf2NB6QR7blZ_xS1uUUzFKYw5J8IS7qgeHAiCY16t33EMkx2qs827AgTz-KTZykvbZ0J1TO2fn1XZ1ApPBLMa6v4e_T-pxkHZRiMzm0SbDtkR-FkVyZG5zqjvjIPhahmIm_iNTpPHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08f96b91ae.mp4?token=HhSkYVttHJZs4_FWZPtV3LfpyEExVi1QZpdG4vuvyEOPtS00M_vsKAiOnk5hR3epHezGXuohXAquGK1oeAFGLb0irogMgFWS5KzWUEJ70YM7l9FVgecm3Z2kuRrR48qd4QaWu3mumt_8iE1PA-Fnbrdk0kEESCXJjLXll3IND_mXZ1ivpW_g8Jfxq5npxBPPh56JjFte75G7Tf2NB6QR7blZ_xS1uUUzFKYw5J8IS7qgeHAiCY16t33EMkx2qs827AgTz-KTZykvbZ0J1TO2fn1XZ1ApPBLMa6v4e_T-pxkHZRiMzm0SbDtkR-FkVyZG5zqjvjIPhahmIm_iNTpPHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: در ۳۰ تا ۴۰ سال آینده چین، روسیه، آمریکا و غرب آسیا، ۴ قدرتی هستند که جهان و منطقه را اداره می‌کنند
🔹
اگر آمریکا مدعی حمایت از تجارت است، روزانه ده‌ها کشتی تجاری از تنگه هرمز عبور می‌کنند پس باید محاصره دریایی را کنار بگذارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/656251" target="_blank">📅 08:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656249">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ترامپ: در رابطه با ایران نمی‌خواهم به سرنوشت جیمی کارتر دچار شوم  رئیس دولت تروریستی آمریکا:
🔹
موضوع اعزام نیروهای ویژه برای انتقال مواد هسته‌ای از ایران مورد بررسی قرار گرفته، اما نخواستم در شرایطی مشابه وضعیت جیمی کارتر قرار بگیرم.
🔹
اشاره ترامپ به شکست…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/656249" target="_blank">📅 08:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656248">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
عراقچی: با توجه به ملاحظات امنیتی، دستگاه‌های اطلاعاتی حضور علنی رهبر انقلاب را توصیه نمی‌کنند
🔹
سطح اطاعت و پیروی که نسبت به رهبر شهید وجود داشت، اکنون نیز عیناً نسبت به رهبر جدید انقلاب وجود دارد.
🔹
ارتباط ما با رهبر انقلاب برقرار و مستمر است و رهنمودهای…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/656248" target="_blank">📅 08:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656244">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUEU1p-LbHBBa-JJoK-M0et8c7U-ynJSpGYf2syyfGMrQxJBKdiDLf67hTQ_dp6hdE17rL2LehCJbjELTHCImcN9Ny4GLErQ5NTXAaIGsD-Q0MxQ9LKJELuBHsG99ZDGBS8IyX-jnlsFxpv_PQXKNW2n50txDWE9DaTFcr4o4YdKY3O2PKwZYY_tdautSqulezes_WFqj8zDSHS0UwV516dcuQ78uQCoCQ0VEe0R2dBDDSB6HS4EHBRavCA3Dj8LnoRJQihnNp9yQa-9p89fDjPxcVAJ56prinCx9nILClqvQWtIaAW8ePF-sPWQGSDEikdQHA83V32WHzPpF-2MQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4hFpaEcRetBn3kmmub98cE3c6N2ieICqjUHGEXjUl_8lfhqVDX7NLcj9u9HohZFw5J2TduyXGw_7GLvRn-xnOM4QdrkelcJ9qDI35dVEH_VpC1WBeY-kiaO71MVuqIpGZJmBWmX-wGfClonsHphCdy3gdgUoukbHFKtUWr8gyYOVNPuk7yh4XUTdhb1KmPuN_1I5y68FuaJfI_guJHe8R-hPUhGq5bryf6pQwUwFZbZVPoVRx-i5jDpmaMdXx6GgklhyNiBwH77JuUsn5idJHqsB1hvoYTajg7Mc-Zfa-_Cju_1GhP1AGxJ9z4Z55Or_TUKM_PZ7-WbYCpgYHHR3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87279c03a8.mp4?token=H_kujMlr7PxtwR1N5cHVI4rcdNdnY3bl8VK1I9hWhq6k1LTCcLgzjIr1AvMhz3oGs2zclty59VcUYtKkwuGmS8mK63Yvi9roZBPQsTWK9JpYS3q1tit8j8djPYkMwO79k2rffRdZoNCFN5qyR27qjq8a-l-_UZJ82AS_5dq46iBnZLjZt6jq8bRN3Bu98TkoqQTM1XtAkud9LdzUqs8AejFfgMDPCc4DEIJ-GpfoAQNxciVh0e7M4WwuazyhfdVC-FTjoctMnNX531kVTWapALkiWB8lrMl0yTu03lrqCCpCj_Q279dZ15UvHCchA1fETZayvZdJzEWSP4Zv-MSzdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87279c03a8.mp4?token=H_kujMlr7PxtwR1N5cHVI4rcdNdnY3bl8VK1I9hWhq6k1LTCcLgzjIr1AvMhz3oGs2zclty59VcUYtKkwuGmS8mK63Yvi9roZBPQsTWK9JpYS3q1tit8j8djPYkMwO79k2rffRdZoNCFN5qyR27qjq8a-l-_UZJ82AS_5dq46iBnZLjZt6jq8bRN3Bu98TkoqQTM1XtAkud9LdzUqs8AejFfgMDPCc4DEIJ-GpfoAQNxciVh0e7M4WwuazyhfdVC-FTjoctMnNX531kVTWapALkiWB8lrMl0yTu03lrqCCpCj_Q279dZ15UvHCchA1fETZayvZdJzEWSP4Zv-MSzdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سی‌ان‌ان: آتش‌سوزی ناو «جرالد آر فورد» شدیدتر از اعلام رسمی بود
سی‌ان‌ان:
🔹
برخلاف اعلام نیروی دریایی آمریکا، آتش‌سوزی ماه مارس در ناو هواپیمابر «یواس‌اس جرالد آر فورد» شدیدتر بوده و به گفته منابع این شبکه، سامانه اطفای حریق کشتی نیز در زمان حادثه عمل نکرده است.
🔹
در جریان جنگ رمضان ناو هواپیمابر جرالد فورد بر علیه ایران در دریای سرخ فعالیت می‌کرد؛ در تاریخ ۲۰ اسفند سال گذشته سنتکام در بیانیه‌ای مدعی شد که ناو جرالد فورد دچار یک آتش سوزی جزئی شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/656244" target="_blank">📅 08:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656243">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaIz4uGAm156bLwORl4Yvpziq2u41lJ2Bv-wxISk_qWKPH3zTzeEkJ83Q10akXrkpIjT4bgw_WqMiHfNpryQz_C6y6iCBbbcnDb79dAswXwY3XHy7l2n3PY2tGFcHhmaGjOxhSq4xzYm6qmRlvv4GjI4TiwTAHq5IVduQWg67HKiMemm9ZbF7XxPzEsPeDb5XrdGMFdhHOoaaq8aU2teKEt3asGql8ZF_3gmPI8-jCMVtw8jS4JeYFWNCz7_yLsUdMb4jQ2HgkXfOXf1t0zVJds3MzrrjFwveexnzlevfIic3EOti0s2gqmYiYP_4dIu6qP9Bo3TVk3BBJRCJ_J87g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۱۵ خرداد ماه
۱۹ ذی‌الحجه ۱۴۴۷
۵ ژوئن ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/656243" target="_blank">📅 08:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656242">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpWl-gWwHzG1EUa-aOdPRZruQIKYqg0ouybt7CUSONgWyAz3jCJiM_J9chHUH5zTsxJg89tAJMa0bWkHFZBvA5JXw_oT4BtS3Srga0snODS5dFHjViQ11A3G9Wqx_VfT_Y4sqAuhJpjzS6nHGnH5FwL0c2mY4K8zaolUapOB9yPg6THtxQnL-9VbN_UiFDWWNjpyHWzXgJjot2rcdBrz4oui3Jai0JpgeZEP7t4uH7TcpyMDIa1nDYN-GY0j89We7akJLJVz7a7vX5Fen5LE3zO-EWEwM4_BxFZCDramHG5smORmcdNbV_SCrtod275jgNBGG3_LztF1wA1kVAK-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦷
ایمپلنت کره‌ای با روکش
💰
فقط ۲۴,۶۰۰,۰۰۰ تومان
🎯
ویژه ۱۰۰ نفر اول
✅
ثبت‌نام و استفاده از این شرایط ویژه فقط با:
عضویت در کانال تلگرام
و ارسال *نام و شماره تماس* به آیدی زیر
👇
📩
ادمین:
@robindentalclinic
📌
کانال:
https://t.me/RobinClinic</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/656242" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656241">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKsowoENSRlUgjBGAFbuCCImM8j4yhPRk-sQgO-FMS3_inu4-fafuZEB0ylKhqkmQy5NYUztPpauN1YZdFWDoPOGmaFy_PrBr9zDYFjooCRppgrY42evBdso0xI62nc4_HVpOtucgeuxrWC256Xi6ITozUZJyASOgA22ySUk7DV3_8ibHehqF_19BOzUyIVPEUVpnfItG9Qkc0V9a4sIknHUtOXSMgLlmjaCruoeEjaVXy2j9h407rFYjUpjfbdATeK317_71aKoBqHrukEV1Axh4_vtCj9ndfhR3xVs2oCr54tUeIyiBNt1gZG6WDZMHl762NsKCBolra3OXzq_qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فراخوان نجات محمدحسن ۶ ساله
، محمدحسن برای بار دوم دچار عودِ مجدد سرطان چشم شده و برای درمان، نیاز به شیمی‌درمانی و جراحی فوری دارد
😭
💔
پدرِ کارگرش، با درآمدی بسیار ناچیز توان پرداخت هزینه‌های درمانِ سنگینِ کودکش را ندارد. هیچ مبلغی کم نیست. نگذاریم به خاطر «پول» نورِ چشمانِ محمدحسن خاموش شود
🙏
😭
🌹
💳
برای کپی کارت/شبا کلیک کنید
6037691990480709
5892107047084630
IR420190000000216756895002
پرونده بیمار
|
مجوزها
|
پرونده‌های تسویه‌شده
|
تلگرام مهرآمن
|
سایت خیریه
|
برای گزارش پرونده های درمان زیر ۱۸ سال پیام دهید
@PoshtibaniDarman
👈🏻
خیریه مهرآمن با هدف کمک به کودکان بیمار، تهیه دارو و درمان، و حمایت از کودکان بی‌سرپرست و کودکان کار فعالیت می‌کند. مازاد کمک‌های مردمی صرف امور مؤسسه و یاری به سایر کودکان محروم می‌شود.
💚
کانال ما
👈🏻
https://t.me/mehreamencharityy</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/656241" target="_blank">📅 00:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656240">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T4F1aisunp4n-dhxOO5UPSA81cPtTMP48qdZNyKWbidBU6EdLAKEALsofcfArTflQlV283feeFarnuhqtxQ0iSVhusVJPG0OUQ8AFtnU9GO-nWJPYVReCX3QsSKfjncOwoAunzqJZqFwtiFK8QHMOgJj7HS15Jcv1z97P7IQUTLZezkkBLzOBfwpi5EgyI6DqyhewhRyVGybg0I1Ry-FQ6qwCPf3iytxeUtBf2hQTVEu75QScd69Pb8DvReYB-2vIyURJvbhNaXHVCBvlecl_tVYf7_zRE7FZU1bzHegFugZR0SDOfSG16kg3aVXa-ZKZyRJJN7HDTOIQPn2m9h6WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🪄
🌟
از تخیل تا واقعیت: با هوش مصنوعی و برنامه‌نویسی، ایده‌هایتان را زنده کنید
🪄
🌟
🎓
مدرسه‌ تابستانی هوش مصنوعی روبوآموز
🚀
آموزش‌ پروژه‌محور و مرحله‌به‌مرحله
🧒
دوره نونهالان ۷-۹ سال:
🔹
اسکرچ جونیور
👧
دوره های کودکان ۹-۱۴ سال:
🔹
برنامه نویسی مقدماتی و پیشرفته اسکرچ
🔹
دوره تخصصی هوش مصنوعی و ابزارها
📲
کانال آکادمی:
@roboamoozacademy
🔗
لینک ثبت نام:
www.roboamooz.com
☎️
پشتیبانی:
09105253867
@roboamooz_admin</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/656240" target="_blank">📅 00:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656239">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOR666XjV-R-5-ZtE6hLyS4Qag1M2fACo00BykzkuYdKeM203U_rwtti44Mojkgc65biGoZkNxr5w4noV1j-pcBIjlmLKXaHCxKIvIXO9jf-rj5F37plKvKchJ2WYAIZ1ew2jHAUj0tLVgLDQYvWPqwAIY1LQKROc1vyoCG9uom07944lbw_KzI7H_FbgiABnNBNA0o4B2W3nxNMV0fg62H5e2-HJB70xd1JI5JlE5_biLGHikwsF8Vcj7ROEIefSfgGMKG_fndOXPY70SvmTUaCnDj0q4kJDwKgYKqUlK5YZen7RNNIOow8VuEfxgNUhB0NaJNlBdzLnt5mGKUGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/656239" target="_blank">📅 23:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656238">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
عراقچی: با توجه به ملاحظات امنیتی، دستگاه‌های اطلاعاتی حضور علنی رهبر انقلاب را توصیه نمی‌کنند
🔹
سطح اطاعت و پیروی که نسبت به رهبر شهید وجود داشت، اکنون نیز عیناً نسبت به رهبر جدید انقلاب وجود دارد.
🔹
ارتباط ما با رهبر انقلاب برقرار و مستمر است و رهنمودهای ایشان در زمان مناسب به دست ما می‌رسد و دقیقاً براساس آن‌ها عمل می‌شود.
🔹
رهبر انقلاب کنترل کامل امور را در دست دارند و با توجه به ملاحظات امنیتی، دستگاه‌های اطلاعاتی حضور علنی ایشان را توصیه نمی‌کنند./اعتماد آنلاین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/656238" target="_blank">📅 23:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656237">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qq-PBUKxoGzFyZAF0ZC01qU-d4d7ZvrfV-W-pN-5Gq6NPufcM1imCkMk2-c2lSl-v0Lc5VfhD7V01TED0ELJl3lwdjXkCOqN2qbGkgKjVaXgZ04lCnRJTrtSnnOXsvkOPbTM6NJvJT4_uN0AijXfe4PmIz6Ch2Y9Kri5BaexPRmrQsqB7D_vU_RIIi7r6SZq5ruYDTso2a7z14MaujecKAT15YVebsqwSup6NA1xCOtBet1Y12Ix2rizNKuqCT9bqH8zEnnzgLnV09yULrXGlgbfldHYlwhgo939lJuL-C2cYGLz_6MvS1uTSJxl-8mp8jyNcMEwF6oxQgB76QXj9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاب خاص مهمونی کیلومتری غدیر تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/656237" target="_blank">📅 23:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656234">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae25f2633a.mp4?token=sIJQHVs7jf6J9GV-7NCSRqq-teMyLk_afxJhbyj55m4ElLBoVPfFnXECrJ4dIbLmvyq0ovb6ffTWPmai3VeLABcR1RCqjldIajHPBppY1QIR8GAIYQD3PC6jv34K0JT2UhAEMIekWMoNkMWtKB5qdYjLP9JhtrRaj0CEddS3VtuVOrWzi1_UifIVAut9Fo8X_HaHUxzwdL6m0G-v3p2J2RWy9dZavaue2_dZk53-q1JbHavYs33a2L_DfWLKAwQ8Dv_6kS5D5vUzBCmE3HirjSXH37HkfhiyPQm53wG1gEKkFVw4EyW-f11YH8Lc8dIeTq-zyqhfoGW5Qxsfwx99YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae25f2633a.mp4?token=sIJQHVs7jf6J9GV-7NCSRqq-teMyLk_afxJhbyj55m4ElLBoVPfFnXECrJ4dIbLmvyq0ovb6ffTWPmai3VeLABcR1RCqjldIajHPBppY1QIR8GAIYQD3PC6jv34K0JT2UhAEMIekWMoNkMWtKB5qdYjLP9JhtrRaj0CEddS3VtuVOrWzi1_UifIVAut9Fo8X_HaHUxzwdL6m0G-v3p2J2RWy9dZavaue2_dZk53-q1JbHavYs33a2L_DfWLKAwQ8Dv_6kS5D5vUzBCmE3HirjSXH37HkfhiyPQm53wG1gEKkFVw4EyW-f11YH8Lc8dIeTq-zyqhfoGW5Qxsfwx99YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قدیمی‌ترین کتاب ریاضی جهان با قدمت ۱۳۰ سال در زمان مظفرالدین شاه!!!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/656234" target="_blank">📅 23:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656233">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔹
خبرهای داغ امروز و امشب را از دست ندهید
🔹
🔹
رأی کنگره آمریکا علیه جنگ ایران
👇
khabarfoori.com/fa/tiny/news-3220428
🔹
علی کریمی داماد کیست؟/ چرا پدرزنش اعدام شد؟
👇
khabarfoori.com/fa/tiny/news-3220492
🔹
اولین واکنش «محمدرضا شهبازی» به جنجال های دیروز/ ویدئو
👇
khabarfoori.com/fa/tiny/news-3220475
🔹
عراقچی: هنگام شهادت رهبر انقلاب، در دفتر ایشان بودم
👇
khabarfoori.com/fa/tiny/news-3220486
🔹
حضور قیصر خواننده در تجمع میدان امام حسین/ ویدئو
👇
khabarfoori.com/fa/tiny/news-3220529
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/656233" target="_blank">📅 23:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656232">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbcf6abb0f.mp4?token=Zl_EySCFEsk9RYeft2atw4mR9CPBVhP7Lf32orNwK0Bat2acuAJnGre_rW1Ho_8GSul3-tQ1VdKgCH9bU7Z48JTYrVxNbUtFJGx0j6Aj82Iz5ZDYx-EzsQDz-riwITjJ9zbAsG5wqAhUF4c09H5zuN4JU4TjXfjzT7P4jXGsR5HA_0uKinQNj8tyR72UuJlkoQ7XKzVMrbg4AnQOAylQFsARoMtNxE8n8OEo6DBEYMOOxuTXfYvlnpYBcc-6gjbm9WKKm_ivK75D4ZmSuLG91mSA02f-iOqHDfdpi8ZDlcHGKmDx3yHFAy5rD-97rjnF7FFpns_caP9HVzmE-CEDMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbcf6abb0f.mp4?token=Zl_EySCFEsk9RYeft2atw4mR9CPBVhP7Lf32orNwK0Bat2acuAJnGre_rW1Ho_8GSul3-tQ1VdKgCH9bU7Z48JTYrVxNbUtFJGx0j6Aj82Iz5ZDYx-EzsQDz-riwITjJ9zbAsG5wqAhUF4c09H5zuN4JU4TjXfjzT7P4jXGsR5HA_0uKinQNj8tyR72UuJlkoQ7XKzVMrbg4AnQOAylQFsARoMtNxE8n8OEo6DBEYMOOxuTXfYvlnpYBcc-6gjbm9WKKm_ivK75D4ZmSuLG91mSA02f-iOqHDfdpi8ZDlcHGKmDx3yHFAy5rD-97rjnF7FFpns_caP9HVzmE-CEDMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور محمود کریمی، وحید شمسایی و سالار آقاپور، مرد فوتسال آسیا، امشب در تجمع مردم در میدان انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/656232" target="_blank">📅 23:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656231">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ادعای ترامپ درباره توافق با ایران
🔹
ترامپ در یک مصاحبه خطاب به خبرنگاران گفت که آنها به زودی متوجه خواهند شد که توافق با ایران چیست.
🔹
بخش اصلی این توافق این است که تنگه هرمز به سرعت باز خواهد شد و دستیابی ایران به سلاح هسته‌ای هرگز نخواهد بود.
🔹
بعد از «به پایان رساندن موضوع در ایران» سراغ کوبا می‌روم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/656231" target="_blank">📅 23:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656230">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">✨
بلاگردون بلاگردون بلاگردون ایرانم
به درگاه رضا شاه خراسانم رضا جانم
▫️
اجرای قطعه «بلاگردون ایرانم» با صدای حسین حقیقی در برنامه غدیر
@Heyate_gharar</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/656230" target="_blank">📅 23:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656229">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK_bWVjvBOoW1VJiMNBxUcaMpQAdpyklUQSH2HZm5o7NfggN_PL2SLYLEjFJrltpkmn5tFfhN9cYhHNbxLjMgfIYFi-0y4E43wctirApl-h_F_45IBYl_GwJ0UJW6_hnY4y1IXMBAJhBbOODgIG_LlNd32G5shb3hllq_zYjjGLAzZXtWGJe2IHawku_pHPfQ2N8--ZVa_dlanl2GjJBPD1AS0VdPUfZwRFKTmbW0604aPI1dlrkOa6sFamBVyAMhzPnfUlqrQhjcl3N-ngiwt19vc3CGetRK63GzMrFSYDq00LqwLs5sRp9q2DRk7T_qEH8sxuTZdU1DDFStHF3Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شرط ترامپ برای ازسرگیری جنگ با ایران مشخص شد
🔹
نشریه «وال استریت ژورنال» بامداد پنجشنبه ادعا کرد که رئیس جمهور آمریکا گفته فقط در صورت کشته‌شدن نظامیان این کشور، حملات به ایران را دوباره از سر می‌گیرد.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3220519</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/656229" target="_blank">📅 23:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656227">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikCwk-EsfFnCWjBCCo6UWcqajcgKYJwU2938MXrqYXMJVuGIz8-XWo8mVHSQ6vSG6SVB2Asn8Q_VmmMffMMVFbSejikPAlEI7tGewnr4QMjhEjJyUibukuaLkQxHVCjbu_yVNNO1GZ191KH5bZMCF1AxNqnnrWWrQtiiPn5Y8p-RSRRHRLdGcDeB21x9Szz3Lr3MSarsx9Q_vArT_Dv6MdY1WMcGBuMR0bUm6hwcoppB4IWgr7eQK01__ikgQs6ptaoK1-w4uF9yNtt-OZqszAG9obULwyVGGKJFwt7zaURl8qnRe0Yuyv_J_gLHwzRmY63SXmIfMkuNpvABvKRb2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراف ترامپ به شکست طرح ربودن اورانیوم از ایران
🔹
ترامپ درباره طرحی که آمریکایی‌ها برای ربودن اورانیوم غنی‌شده از ایران داشتند گفته که جابجا کردن مواد هسته‌ای مستلزم حضور در مناطق درگیری به مدت یک تا دو هفته بوده است. ایالات متحده به همین دلیل آن طرح را پیش نبرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/656227" target="_blank">📅 23:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656226">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b22c0e31dd.mp4?token=G7agVVTWAiS9k050_hbLfb1Ym1pcjLnj4ryWMy6ioZuZF7sdnGLDc0NTxHrWwaj-gaTKFWqzzkLq6VYud3WShjJwVaN3LJSIt1ltkV2XWqLdYCEOmhHKfQFXyqX96HdtgLvQNQEz-sCWbt_InEsPVCMR6CMdKN5CQL6uZGoCgLy-tl2yKlOYHaaUSyA8uh215qC-C5GVW5L7XCxiix5fhen_DuNifdDeHr7hWXWsEQMUvKzcUf2Xy54EHQyXQOSTZCSOlmxTl9PkXt00ID3AiXcRtsmYdV5FhH6NoQ5pnFljrKQglSQpsaH3X5p_uBrwZPb-jmWl3dLd9xARxlrmCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b22c0e31dd.mp4?token=G7agVVTWAiS9k050_hbLfb1Ym1pcjLnj4ryWMy6ioZuZF7sdnGLDc0NTxHrWwaj-gaTKFWqzzkLq6VYud3WShjJwVaN3LJSIt1ltkV2XWqLdYCEOmhHKfQFXyqX96HdtgLvQNQEz-sCWbt_InEsPVCMR6CMdKN5CQL6uZGoCgLy-tl2yKlOYHaaUSyA8uh215qC-C5GVW5L7XCxiix5fhen_DuNifdDeHr7hWXWsEQMUvKzcUf2Xy54EHQyXQOSTZCSOlmxTl9PkXt00ID3AiXcRtsmYdV5FhH6NoQ5pnFljrKQglSQpsaH3X5p_uBrwZPb-jmWl3dLd9xARxlrmCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور خانواده فرماندهان شهید موشکی ایران در میدان انقلاب
تجلیل از خانواده سرداران شهید طهرانی‌مقدم، حاجی‌زاده و محمود باقری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/656226" target="_blank">📅 23:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656225">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">✨
در طالع امسال برایم بنویسید
یک روز نجف باشم و یک روز کنارت
▫️
شعرخوانی زیبای حسین حقیقی در برنامه پناه غدیر، دل هارا هوایی کرد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/656225" target="_blank">📅 23:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656224">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ce4a6e0c1.mp4?token=MPvBy_8e4ikIv11SMHohwZwR5iSKJTqx_xw5asbhJZB_KbI34FB2c3Fy6rfljRpbyqL8sD-60WVkTZ4nOr9dA1rB6i96ebOo4cT8Zpp5rqe6jjJ4eapRrM3u-BYCHeLBFH4o-ip2vLlNG77oDNiIbEcSbORQ0DeApgJpqAdYT1HFiDhkkxS8YD23-1fJnK87VTVoElpsCNwfu3yoxQQ_M3IiTxXpZh6G2rNeLfwL8Q4NnPuc9aTB4yadMnzv4bM7LGpwC5qiXomqIBw2hHAkneOkz3gvwsC-cH4lMOEXQQDOjTI-72RVf3XnRtGCYb9_i5OLZEVl14uCo_YLd3vS-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ce4a6e0c1.mp4?token=MPvBy_8e4ikIv11SMHohwZwR5iSKJTqx_xw5asbhJZB_KbI34FB2c3Fy6rfljRpbyqL8sD-60WVkTZ4nOr9dA1rB6i96ebOo4cT8Zpp5rqe6jjJ4eapRrM3u-BYCHeLBFH4o-ip2vLlNG77oDNiIbEcSbORQ0DeApgJpqAdYT1HFiDhkkxS8YD23-1fJnK87VTVoElpsCNwfu3yoxQQ_M3IiTxXpZh6G2rNeLfwL8Q4NnPuc9aTB4yadMnzv4bM7LGpwC5qiXomqIBw2hHAkneOkz3gvwsC-cH4lMOEXQQDOjTI-72RVf3XnRtGCYb9_i5OLZEVl14uCo_YLd3vS-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار برای اولین بار | تصاویر جذاب و دیدنی از اولین دیدار مردم ایران و امام خمینی پس از ۱۵ سال در سال ۱۳۵۷
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/656224" target="_blank">📅 23:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656223">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✨
فهرست بهترین نماهنگ‌های  ویژه
#عید_غدیر
💚
👈🏻
جهت دسترسی به هر یک از مطالب زیر، روی اسم مولودی (آبی‌رنگ) کلیک کنید.
شرف المکان وحید شکری
بارون نجف محمدرضاطاهری
ولی الله حسین طاهری
خوشگل آرین اسمش حسین عطایی
حیدر حیدر سجاد محمدی
به به نجف امیر برومند
فوق بشر محمدرضا نوشه ور
ازل آید یکتا آسد حسین ستوده
اعلی حضرتا امیر کرمانشاهی
بیعت با تو محمود کریمی
المنت الله ابوذر بیو کافی
حیدر مولا حسین ستوده
مست نجف علی اکبر حائری
مقام والا سجاد محمدی
اسدالله حسین طاهری
الصبوح الصبوح حسن عطایی
نقش انگور محمود کریمی</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/656223" target="_blank">📅 23:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656222">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ادعای سنتکام درباره تغییر مسیر ۱۲۷ کشتی تجاری
🔹
ستاد فرماندهی مرکزی آمریکا موسوم به سنتکام، به رغم وعده دونالد ترامپ رئیس جمهور این کشور برای لغو محاصره دریایی علیه ایران، به بدعهدی خود ادامه داده و مدعی شد که تاکنون مسیر ۱۲۷ کشتی تجاری را تغییر داده است.
🔹
این فرماندهی افزود، ۶ کشتی را نیز که از این محاصره تبعیت نکردند، غیرفعال کرده و در راستای «حمایت از کمک‌های بشردوستانه» به ۳۶ کشتی نیز اجازه عبور دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/656222" target="_blank">📅 23:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656219">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd978bc00.mp4?token=popfQSEHNAw_YEz-PbDOEvnFkTj-cnDRAvFFYDnb8i48b3F4WfhIW0NMg_mZ7PL8BAK5umOcLcQkrD0vXpEJr0Oycz7THUdy107TvfHP1N5JK6ZHqOgLEZ2RqzuJMwM6rVd2sSxAU4uTi3gmtER1o1UdekGQlWP7xlThkIAozD_dBNNMZw_Dm9ta01aolxUaMV16KOMk0f6si8Wl6_A3UMOYC7O8rDRZ9yqcfJXKe-WStgPdTsQ9RWwR8AY7zSV37TQ9tqbeyemJe0usKcmlCs0lwyCggMAuAFE_D1M1tC0gYDLwm6fT7gHwAxw3bNoEs3uqkqB4LF-ZfTr8wlhrPKsh0upfdUb0px0rIqScm-vBdf2h6vYmZ8xjtVN9jFxXr6Zwt6V6K_3WmpIZBOxDXoRA5AcSQKGJsGxsyGUAwt57A3t_caghvaUVhzKJ7X-JW_4IxfurYdUgdBider6Wp3wEPYLiCtCD8BSkYpCvWuzZAYeB3IMwq59RgbvG6AQKD1nNoOYDj6OULAakmGEhe3SuqF62GGuCWrQ2HG79ourNWGHhRU49z14HfvC9AHZ1XgfgzOKHgGN7JYvuNYSuSRh0OJKMtN_MjLCuiq9olVol2Yh_ZEdRiOSvdCt78y5wu5ognqba-CkPWRbS6dwOlGrQsJfvPGYclQwg3pMOpcE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd978bc00.mp4?token=popfQSEHNAw_YEz-PbDOEvnFkTj-cnDRAvFFYDnb8i48b3F4WfhIW0NMg_mZ7PL8BAK5umOcLcQkrD0vXpEJr0Oycz7THUdy107TvfHP1N5JK6ZHqOgLEZ2RqzuJMwM6rVd2sSxAU4uTi3gmtER1o1UdekGQlWP7xlThkIAozD_dBNNMZw_Dm9ta01aolxUaMV16KOMk0f6si8Wl6_A3UMOYC7O8rDRZ9yqcfJXKe-WStgPdTsQ9RWwR8AY7zSV37TQ9tqbeyemJe0usKcmlCs0lwyCggMAuAFE_D1M1tC0gYDLwm6fT7gHwAxw3bNoEs3uqkqB4LF-ZfTr8wlhrPKsh0upfdUb0px0rIqScm-vBdf2h6vYmZ8xjtVN9jFxXr6Zwt6V6K_3WmpIZBOxDXoRA5AcSQKGJsGxsyGUAwt57A3t_caghvaUVhzKJ7X-JW_4IxfurYdUgdBider6Wp3wEPYLiCtCD8BSkYpCvWuzZAYeB3IMwq59RgbvG6AQKD1nNoOYDj6OULAakmGEhe3SuqF62GGuCWrQ2HG79ourNWGHhRU49z14HfvC9AHZ1XgfgzOKHgGN7JYvuNYSuSRh0OJKMtN_MjLCuiq9olVol2Yh_ZEdRiOSvdCt78y5wu5ognqba-CkPWRbS6dwOlGrQsJfvPGYclQwg3pMOpcE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر حیرت‌انگیز از برگزاری جشن بزرگ غدیر در شب گذشته یمن همراه با نورافشانی، روشن کردن شعله غدیر در کوه‌ها، ارتفاعات و سقف منازل و جشن و پایکوبی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/656219" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656218">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">✨
«عشق من حیدر کراره... آقایی که توی شهر نجف یه حرم داره»
▫️
حالا و هوای برنامه غدیر با این نوای علی اکبر حائری که حسابی رنگ و بوی علوی گرفته...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/656218" target="_blank">📅 22:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656217">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/148dbf71a8.mp4?token=R5L3jBeaSxGLoB3gHRyOfHttm5CcOUk1PIS7GzWfNaXDnB7CTn20WDZdRddR7D1QHLN8UDzt7nhonZql9CY3BaVmK5nkEc9keQk_45T-w80IoABT9bv5ozFerVRVYH6rXgd5nQmNHaLvH9Tv77Jj1cuxtcTMfXxMCUrirTP8p3Fz7WqWIbvtbkNnLP54oJkSDxK-vnIvMx8axagKSMobsyN8JVc_P0zCiEb1YwQzmm9t-Tz6vhRlsoDIEVPn5ZX8NuCtyivii5Cx3u-9bUpTr1IYMaSw_vhqnUjc6GH3COsW6VDe80ZU04EHMUGjDqwNWRuoD-xQJ_VCwPhuwxcohQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/148dbf71a8.mp4?token=R5L3jBeaSxGLoB3gHRyOfHttm5CcOUk1PIS7GzWfNaXDnB7CTn20WDZdRddR7D1QHLN8UDzt7nhonZql9CY3BaVmK5nkEc9keQk_45T-w80IoABT9bv5ozFerVRVYH6rXgd5nQmNHaLvH9Tv77Jj1cuxtcTMfXxMCUrirTP8p3Fz7WqWIbvtbkNnLP54oJkSDxK-vnIvMx8axagKSMobsyN8JVc_P0zCiEb1YwQzmm9t-Tz6vhRlsoDIEVPn5ZX8NuCtyivii5Cx3u-9bUpTr1IYMaSw_vhqnUjc6GH3COsW6VDe80ZU04EHMUGjDqwNWRuoD-xQJ_VCwPhuwxcohQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت آب سد کرج، امروز
#اخبار_البرز
در فضای مجازی
👇
@akhbare_alborz</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/656217" target="_blank">📅 22:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656216">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_um_4aA0pMvK0plUChVDobxsTSMMC9nF0Czrn2CvotZUkB9M27xu7DCVJWoDYcwUujLWnuBI42iB53PVDLiUTYmERXUbEI3UrcIvRvepwHjH5j9vE35nl40mwvWMHYuk3-9-Q_XMR-LUHKm0aln9bnDi8h-wvGi3G2JNv0sGAbsYwU8kITiaf2aJG3F6_aHv7Gv4-GCq88EAYJqjo3Bip4HyL2O71MUb579ehy6bg24FzlArmfax6NP257VWJvV1XVPnups09wiuAvZrR263kmVvPziQdU-P1eEp218tN2eM4IvylF3BSRfiQV-ap6J7cx9Fs0hU3d8tjT-SKyqrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف گروه خونی عجیب؛ فقط یک نفر در جهان آن را دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/656216" target="_blank">📅 22:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656215">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ حیدر حیدر</div>
  <div class="tg-doc-extra">سجاد محمدی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/656215" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
بر دشمن مرتضی علی لعنت حیدر حیدر
یا ضیغم المهمهم و ای نور منجلی حیدر حیدر
یا مظهر العجائب و یا مرتضی علی حیدر حیدر
🎙
#سجاد_محمدی
#عید_غدیر
💚
مرجع رسمی مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/656215" target="_blank">📅 22:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656213">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a5e53b53a.mp4?token=u5vVk3l-4H0NzroQ6u797yRV6S1p0LGoONYMYEy_9O3NQwtQhQ_ypDlSrW8yiVbd3zs_2ktLzFjxYBNfu-g966c_EJCwJCazmFKO_mdLVazB-9ZKdvVA2Qc6ZFTeUrMqn7OziqMKm4Mnv7NPtQ4jWZcTNNR8QOz-LHqBrVD37P5V4rRdrmzNmf8Dbu_mDzyIo7y70N-3uEU-pdH8jgH4kaI537nv0k6oOUkuTb5aj2mG9DRG4znJZ3EyKRx6D79T045BmmHypce27RIT_VwIAmPWsbVH36f48-JVdGulXDLXxznmYhe9sdGJOldWHiwrOyFNAwWxOEirj3rF8q_4Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a5e53b53a.mp4?token=u5vVk3l-4H0NzroQ6u797yRV6S1p0LGoONYMYEy_9O3NQwtQhQ_ypDlSrW8yiVbd3zs_2ktLzFjxYBNfu-g966c_EJCwJCazmFKO_mdLVazB-9ZKdvVA2Qc6ZFTeUrMqn7OziqMKm4Mnv7NPtQ4jWZcTNNR8QOz-LHqBrVD37P5V4rRdrmzNmf8Dbu_mDzyIo7y70N-3uEU-pdH8jgH4kaI537nv0k6oOUkuTb5aj2mG9DRG4znJZ3EyKRx6D79T045BmmHypce27RIT_VwIAmPWsbVH36f48-JVdGulXDLXxznmYhe9sdGJOldWHiwrOyFNAwWxOEirj3rF8q_4Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرائت زیارت مطلقه امیرالمؤمنین(ع) توسط مردم در میدان انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/656213" target="_blank">📅 22:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656206">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWSCSBF0NY5LQ0TtHa6KhvjyVxlQ7Q30BXflVShRYx1m_yQHZgVNhMVUtFY6b20uRl06MOa_r0vT4RIBNrVUEAHInZKa3NajPLSBVlYBlPdrPvELoJR2UAbQQMl3fNypBvrGUv9rz9N9pG0rlotAXLEo7WtSS_EDW2Okp3cBceAoF6psoo9Rl0QpQPg4g1lu7pjK3rvgpSG1bHJ_86JEhZN5FDhCmX0YGUKLy50SgPmi3YRPH15yXyibEg44SE7-IbRURmNL2CF1AgX2I-Mp4dr2I_q8UUGDXOA7UFF5Ad3ArkUGldNQG_fmiXWm_HkMvLUzr27LyOfplsFcyiWWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEsmWA3eoKol9J-357QyjAsIBZFpid2ZD5-lG9zbLqxWmwkBlHJUdjml8ff8TKKrye554c8TdWzj1GEIwgzTJmyM_ckAsF5uc2YDqnHvCvwdr-eD77FsPxD3oo6aBf4mP7YNIgE5NlhJaOF1HpjSeslW5tY87tBpaus5Z6L16edrEXEy95hxZjQPT5yK2wgnlm7JJmEIYFucLeiVR8xtZkGzWgnjt3ZSrUGkj3i1zOZD2AEihSkr6eCVpIxyYtdR0C0GN4hHie9iZxvnz67SrOmez-4P_kio_pw6Nt19MCQranvwwTCfx_IlAC9KS6nOGU7jUD1iV_FNZYMAzT-yHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mtT2O4Wrpd2xeAyHJq_Z0xTCnU55EkyfByzZAD9E_U8ET_tgMzsrOlc2k2vSh1DRZd6jVWlZs-rBwXXxQpteOOAp4u6On2SO3IZ5JNNefanZ9yRM0ufWbFGpqKGAi125GuxWqiq1-nmZqAj0h2FSEDdFl2qODsOGrt18z7OAhlnF1lRom3fBkG8pqdFGyMaWojhNeARvDrC2-IyY7omakD3bZZy0NnzuLwOcBCK1mQ4djm2aS9gy6DOTUQlllTB5XIhaiTDCRPCqSrna-CijszpECHTQvJiZq_KfjcnGb5h1XIkiabk09ZrbZ5kz5yQK6_tlXyPNtlpd9ma3N1BPzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGYGR1agnR8i4YN_9gXRW_aLMbPQwKv3Y3JlMxXejyJJtUIfygtpEey5mrfMqU9y01aIsdKEOqQ5oceVIyPozhcPYVKn9JIJkINLRd4TQxCXSeFTcyc6Mcu1ppaTbjDkrOoF-EOpgHuw__Jo_-cDEFRmguRlpFcRePaSAFaxUG0rGw8fwsEDMF1VJCdN3zwVBJmscH3tmiwz5OWz_kLFMagxLqQE-roU52yolUj1JUxdxCyIqogwIqT2A1EkX5mdt5yu3kb1kFaf8yJu6QBNVZcrAil2PAycDwtvce7jwSkf6fgjNieuoIx7kbcO4jv5LRz6ut7aLTN8txd8WJCNtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWzvcwI-8vUGzBdqML_z06u-dTHg5ZEd8b77cPP7bTYssyeihFwg_cvV6vb3g1goec8KOhfviBfYyl9xgxSTWTtd00kELe1QEmbCrSjUcepFHZ5I15MaWoPMnQMXOMaPCrpl0AB8DahFf_VjEXvHTn-oGxGDztY_AQlVakto56HzdChxVqiApeVWzXfvYU303fw0p2K48dW2-3nsIIqUGeKnXrmlyAC3ZZDj9lZx5szSptdkHl1CEO54Y4hMPRN7_w51Ly7FzEuElhpDts2iiO2fMCHnqNB1PGvkBiTZJylQsHvfyRDa_Y4XFdWECGRCj_zjTKY-EkWyz4yivyZgJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YAS7W1qFma4gRsyrMdcoD2WPQQoJAV8xyr14_HgQezyP6AJIX5PRPUb3DOx0MHtQ0TTdNhLJw_9Dy_RS9ckcVSMqb4aui12vbHvpBdqCA8zhtJW-w5V2zxZ_oHHSzjj4c7m2cX2ryKALuhfTi7yhak2UUI1aTt5N_66vN3DrO_fVXqVdMyjPg6k9lxb7HpYlIbTI-a1wF279-xDi0BASBcLI6PoatEQH2NlzsY9OHQotMhi5lIfJXpsRarhjLanomvJXRSbDUrjck9av6McO3whcMV3HfnTC7JAEEPQc188Zli3aa2QcAfJyrdoBhjPfwRWA6cqC7NqJLG-PRlrX7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yu8Bx2Gf0ej-wc1SlTQ63uD6RopqxBFRo4NqrtAZCr1Zk-WEkj68MTZMc1mfGNUeXLw3Ff7rQUK1kyY-QGnQvemOQS8kE28UXdjTQpZ0P_1oZ_ehHZP-Ti04T81AayHI9DSoCaAkNGM_p1BR2zVvk51dZDfuXBlQA0fO78HPOt2G8ELeNhYRCWS0hLW0YBVWHM2Yg3USFkxtrrfrL7bV6DCTEDDWs51knpO6Xj4barR4iS-n9pJ530XbzO8gdpUX68L3a6qaqEkDJ4DSO8YM9EILuQB7egWCl3ItEz8TuvnsIu2Nh3IpD5u_F5dCOO4WBJ-F7O8HMzEGoQVZUxVPIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💚
دنیا محو اقتدار ماست
اسم حیدر ذوالفقار ماست
▫️
این برنامه به همت هیئت قرار و مجتمع فرهنگی امیرالمومنین در حال برگزاری است
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/656206" target="_blank">📅 22:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656205">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
عراقچی: ما در طول جنگ اخیر شواهد بسیاری داشتیم مبنی بر اینکه آمریکا و «اسرائیل» از آسمان و خاک امارات علیه ما استفاده کردند
🔹
‌اسناد و مدارکی وجود دارد که نشان می‌دهد خود امارات نیز در برخی مواقع در عملیات‌های نظامی علیه ما مشارکت داشته است.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/656205" target="_blank">📅 22:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656204">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a09ff6e8.mp4?token=csg6B_GzmjFUJF08nH4OGHA4z3jG9C7rT6_AatX9HbJ5GbJdC20njAM-s4fYo26mRRxRP75ANpDOWS6UMTQro0LUD1JudNCflHVTGQgAQoK7Gv53zftgR-NWcRH3DmWTOdtZxl__tgXL_JjTTtf0Z__bErgeR6UCy_wCWex9BrCMflWKP_PUMWmABU1J-2OqiWHYzYdt-6AFFuVHM3i31TCle0vtAF2iUzYsaA1ShJHPlA3DYDJwwGIi2O2z5S8qn010JIMf9BJfYparHiAkunSfnMWqPeCsmESPDY9_WCLzB957EhPvHrHPitWS4q_al7MNsWdU_vdaFBZB-rjkDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a09ff6e8.mp4?token=csg6B_GzmjFUJF08nH4OGHA4z3jG9C7rT6_AatX9HbJ5GbJdC20njAM-s4fYo26mRRxRP75ANpDOWS6UMTQro0LUD1JudNCflHVTGQgAQoK7Gv53zftgR-NWcRH3DmWTOdtZxl__tgXL_JjTTtf0Z__bErgeR6UCy_wCWex9BrCMflWKP_PUMWmABU1J-2OqiWHYzYdt-6AFFuVHM3i31TCle0vtAF2iUzYsaA1ShJHPlA3DYDJwwGIi2O2z5S8qn010JIMf9BJfYparHiAkunSfnMWqPeCsmESPDY9_WCLzB957EhPvHrHPitWS4q_al7MNsWdU_vdaFBZB-rjkDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نذر باحال مغازه جیگرکی در مهمونی ده کیلومتری غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/656204" target="_blank">📅 22:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656203">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1992f9d726.mp4?token=L5iVU-m5un0lZoW66-NFl84wcX1wl08e4Fy-R32ELJiY9q419JFRNuQCwtY2IdzUqI0Q18ZTgLy9j-AfRLQ2Jqc_xhZyDOR0nzbM3oQiW1Cuphzut-1Me0AFAL5xHutUZHJTpcRvt3kPBelhBb-5scLSj8srsZ3qr3gFXWjbtGqOfN5Vo5DdMdxSCL61yuBfMmM_1dIHJ04p-RxeGD84WFNuNVxDYlPok0QdFmTg0jNTvQe9qLQfBmpdQ5BueJJmlQVqm-cOczCMf6gg8-tff7ugHPCkPRinkMpPdwMSLeRsPVz7aBJKQiWI0jBDv-3IdLuKCQ1c9BY6GxKH9j930g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1992f9d726.mp4?token=L5iVU-m5un0lZoW66-NFl84wcX1wl08e4Fy-R32ELJiY9q419JFRNuQCwtY2IdzUqI0Q18ZTgLy9j-AfRLQ2Jqc_xhZyDOR0nzbM3oQiW1Cuphzut-1Me0AFAL5xHutUZHJTpcRvt3kPBelhBb-5scLSj8srsZ3qr3gFXWjbtGqOfN5Vo5DdMdxSCL61yuBfMmM_1dIHJ04p-RxeGD84WFNuNVxDYlPok0QdFmTg0jNTvQe9qLQfBmpdQ5BueJJmlQVqm-cOczCMf6gg8-tff7ugHPCkPRinkMpPdwMSLeRsPVz7aBJKQiWI0jBDv-3IdLuKCQ1c9BY6GxKH9j930g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کار هنری و احساسی مردم در همبستگی با شهدای حزب‌الله
با شعار با هم مقاومت کردیم....
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/656203" target="_blank">📅 22:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656201">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1caea1f3.mp4?token=phPyUZNQBjAQRFcBTJlyIjYN1aCoSA5uDC75GWyML16KCZaCO2zjiWUlrRunbOIXiEBd5Y6tQw9kS6H4_D_9LcGLutVjV5QdueGnVNqvu25XtUgp--MXEH97y-0X_yPrzxmdmHhBgFk6v262fR9S8DtG7lsppRwjXmGsN-wC5i6KBuC3LLxmoDOpBaT9a56dGWPdbhgMg06nb9H82TLaWku47EZ7MXK-mi4DVwq4F5Apdoe358vNSQo0fb5i-nsQM0eWs3iDRHUETj844ZtDttuyQsxrOdxzu0bDcINzI_lbRKuQbCdA5EDptrkqKOSt3sndpOFYPfESByu0trsAKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1caea1f3.mp4?token=phPyUZNQBjAQRFcBTJlyIjYN1aCoSA5uDC75GWyML16KCZaCO2zjiWUlrRunbOIXiEBd5Y6tQw9kS6H4_D_9LcGLutVjV5QdueGnVNqvu25XtUgp--MXEH97y-0X_yPrzxmdmHhBgFk6v262fR9S8DtG7lsppRwjXmGsN-wC5i6KBuC3LLxmoDOpBaT9a56dGWPdbhgMg06nb9H82TLaWku47EZ7MXK-mi4DVwq4F5Apdoe358vNSQo0fb5i-nsQM0eWs3iDRHUETj844ZtDttuyQsxrOdxzu0bDcINzI_lbRKuQbCdA5EDptrkqKOSt3sndpOFYPfESByu0trsAKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برافراشته شدن ابر پرچم ۵۰۰ متری حزب‌الله لبنان بر فراز برج آزادی تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/656201" target="_blank">📅 22:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656200">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/827e4e7f2f.mp4?token=cyS5gJ0EHR3GIRBl4ir77Jgm47zJkEB7IkG6z28xdSzby3zzFU92KHZfy3LLUkaP7T9TrbJYw8OZ8zQ2sCyxjKPiGsfgkp2ui43sjwjd4jMJd6TQzgVJcW-2rZsB6aKWdxaATqsic1Z2u8Ia9rd3qLn4W_W3kCdE5nAfj9mU6QkEEMVBG4fCGWzsbJawVXjwDvFdwwc5JU22F2mb5wKiCyNcD0cqYMESkZ-LNPoJibIH8DpjsvIp8PF5z-iTCcv-JvOH1KGQQVFk4pReAbkUrhC5PGerdJBXrYFqs0Kqm0Al84teKb_VfLMLj_YcqfdIs5OL0DIDT4MOWd6k5b0RXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/827e4e7f2f.mp4?token=cyS5gJ0EHR3GIRBl4ir77Jgm47zJkEB7IkG6z28xdSzby3zzFU92KHZfy3LLUkaP7T9TrbJYw8OZ8zQ2sCyxjKPiGsfgkp2ui43sjwjd4jMJd6TQzgVJcW-2rZsB6aKWdxaATqsic1Z2u8Ia9rd3qLn4W_W3kCdE5nAfj9mU6QkEEMVBG4fCGWzsbJawVXjwDvFdwwc5JU22F2mb5wKiCyNcD0cqYMESkZ-LNPoJibIH8DpjsvIp8PF5z-iTCcv-JvOH1KGQQVFk4pReAbkUrhC5PGerdJBXrYFqs0Kqm0Al84teKb_VfLMLj_YcqfdIs5OL0DIDT4MOWd6k5b0RXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای متفاوت عبدالرضا هلالی/ خواندن به زبان چینی در میدان انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/656200" target="_blank">📅 22:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656199">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">✨
«مست نجف» این بار با صدای عاشقان امیرالمؤمنین (ع)
▫️
اجرای قطعه مست نجف توسط کربلایی علی‌اکبر حائری در اجتماع در پناه غدیر مردم مشهد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/656199" target="_blank">📅 22:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656198">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
عراقچی: پیش‌تر به کشورهای منطقه درباره استفاده آمریکا از پایگاه‌هایشان هشدار داده بودیم  وزیر امور خارجه کشورمان:
🔹
به کشورهای منطقه هشدار داده بودیم که پایگاه‌های آمریکا در صورت مشارکت در تجاوز به ایران هدف مشروع ما خواهند بود.
🔹
پاسخ ما متوجه پایگاه‌های…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/656198" target="_blank">📅 22:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656197">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
رویت زندگی ۲۰ سال آینده در حالتی وحشتناک
🔹
06:10 نیمه تاریکی که از کودکی همراه من بود
🔹
14:00 ارزش قائل نبودن و آسیب رسانی به دیگران
🔹
28:20 رویت زندگی ۲۰ سال آینده ام در حالتی وحشتناک
🔹
33:00 درک کامل احساس افراد در زمان خوبی یا بدی کردنم به آنها
🔹
37:50 کسب آگاهی در تجربه نزدیک به مرگ، باعث نجات من شد
🔹
39:45 پرسش بانوی پهلو شکسته
🔹
44:45 درک لذتی عجیب در اولین تجربه نماز خواندن
🔹
50:50 تفاوت مهم پدیده توهم با تجربه نزدیک به مرگ از نظر علم پزشکی
🔹
قسمت اول، (منفی هفت)، فصل چهارم
🔹
#تجربه‌گر
: دانیال قاسمعلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/656197" target="_blank">📅 22:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656196">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
عراقچی: پیش‌تر به کشورهای منطقه درباره استفاده آمریکا از پایگاه‌هایشان هشدار داده بودیم
وزیر امور خارجه کشورمان:
🔹
به کشورهای منطقه هشدار داده بودیم که پایگاه‌های آمریکا در صورت مشارکت در تجاوز به ایران هدف مشروع ما خواهند بود.
🔹
پاسخ ما متوجه پایگاه‌های آمریکاست و نه خاک کشورهای منطقه و در همین راستا ارتباط مستمر با وزیر خارجه عربستان داشتیم.
🔹
بسیاری از کشورهای منطقه مخالف استفاده از حریم هوایی و خاکشان علیه ایران بودند اما متأسفانه آمریکا از این امکانات علیه ما استفاده کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/656196" target="_blank">📅 22:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656195">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqrexIXbNK0-JJ14pFD5WoiM2zVYLN3E4XEiJmd8IiOlJwzlWHKopy82C4gwHP6hKHggtmmMXOlSTx0vPYLSEQi_UDaytUpulWrjDiEM0IMKjCQD2vXD2tr3dkm0iX8-_r4peT4a_Z7dIUjQHzvC04mWQKQxHbMHE_rIEhLjP5URagXoDtAnhfY1qrtPIvjzadq2ZApqKVrCXx7m58QD6lypwH0ZXb2BVbhsnM49Px8Lq6oGUj0sh3eCh9Az6O1YEyFaQYeNa721cKHLuNBr6czaMsjGQxrxNb6XEJRJBAqaBc0CFS70-D_QUXfKYSej3W2a7wasTlL-fSA7dJaS9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشاگری یک منبع امنیتی درباره مشاور ویژه رئیس امارات
‌
🔹
یک منبع امنیتی ارشد در حوزه مقاومت، اطلاعات جدیدی را درباره انور قرقاش، مشاور رئیس دولت امارات در امور دیپلماسی، در میان گذاشته است.
‌
🔹
این منبع امنیتی فاش کرد که اگرچه انور قرقاش از حدود ۲۰۰۷ به دلیل نوع مواضع خود تحت رصد نیروهای امنیتی اسرائیل قرار داشت، اما از سال ۲۰۱۵ این مسئله وضعیت جدیدی به خود گرفت.
🔹
کشف اصلی قرقاش، در بخش امنیتی ساختار وزارت خارجه اسرائیل صورت گرفت؛ امّا نهادی که این مهم را انجام داد، ماماد המרכז למחקר מדיני (Mamad) بود که در واقع سرویس اطلاعاتی وزارت خارجه اسرائیل و عضو جامعه اطلاعاتی این رژیم محسوب می‌شود.
🔹
ماماد، یکی از سه نهاد اصلی ارزیابی اطلاعاتی اسرائیل (در کنار موساد و آمان(اطلاعات ارتش اسرائیل) است که در بیرون با نام پوششی و غیرواقعی «مرکز پژوهش‌‌های سیاسی» معرفی می‌شود، درحالیکه در واقع رکن امنیتی و اطلاعاتی وزارت خارجه اسرائیل است./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/656195" target="_blank">📅 22:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656194">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d4399aa8.mp4?token=RwTzVVo-um-ATAtgrP1QC8Niab_wDr2Z5Imh1m2F1H5tlkW06rLNHCe3bLyQ8XCQcTZo4DzsG2k6355FKjbjHlGFGyTlsy7n3zQBXHMYApb1ZxnCHTvrirBHJ52S77lYHE3j3js6iTkkEsYgFnKdd7kVUjCqjM5GU_x58rC2GXPA7C3DVikiEKb52EwAoHtxLcwRyvbQt42_AzRxPP6WISUD2dMTuXjD8Y4IuLP_UHnAsDQC9nEA06vJZsoCT1kV22jzhrCTB7GoYj3lcg7gtIIKTu_0hZpTekGzKWRdnIh-uk5cP5-_YB3Rh8ZWN0cD83gcbG16SOTasxCfAXdlig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d4399aa8.mp4?token=RwTzVVo-um-ATAtgrP1QC8Niab_wDr2Z5Imh1m2F1H5tlkW06rLNHCe3bLyQ8XCQcTZo4DzsG2k6355FKjbjHlGFGyTlsy7n3zQBXHMYApb1ZxnCHTvrirBHJ52S77lYHE3j3js6iTkkEsYgFnKdd7kVUjCqjM5GU_x58rC2GXPA7C3DVikiEKb52EwAoHtxLcwRyvbQt42_AzRxPP6WISUD2dMTuXjD8Y4IuLP_UHnAsDQC9nEA06vJZsoCT1kV22jzhrCTB7GoYj3lcg7gtIIKTu_0hZpTekGzKWRdnIh-uk5cP5-_YB3Rh8ZWN0cD83gcbG16SOTasxCfAXdlig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: به نفع آمریکا است زودتر حقوق ملت ایران را بدهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/656194" target="_blank">📅 22:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656193">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7c682f9c.mp4?token=ozm_1f5dg7evUyVqrXU6UuFBpjSYSik2LGy_molduD5KkEvtp30fK2NM3eQ1ZHyUr1QXi-TAjYIViFebo5CqhmbMFHvlJ0cUKTumIT4xS40oS2XVU6nO_NrUti1kQ2NwcTR48Rb0T59UyRJDE6QR8lXvsl-ef-YI751huFx3c4KPhZbWkSq7a3HvB_mw7sBDYUpkULS4V1OPsrvnKobdugacNg_ytA8C3XAx5c6YiRoj05fJvhgsnlloUFxalO6L76-nSj0X9BEN1TKYurDnuhNRB2ACeXLkf4RBJL--8N2h1JxAZdQ8waczZdeQTk8sCniOsPm9rD89PPcB3WOWGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7c682f9c.mp4?token=ozm_1f5dg7evUyVqrXU6UuFBpjSYSik2LGy_molduD5KkEvtp30fK2NM3eQ1ZHyUr1QXi-TAjYIViFebo5CqhmbMFHvlJ0cUKTumIT4xS40oS2XVU6nO_NrUti1kQ2NwcTR48Rb0T59UyRJDE6QR8lXvsl-ef-YI751huFx3c4KPhZbWkSq7a3HvB_mw7sBDYUpkULS4V1OPsrvnKobdugacNg_ytA8C3XAx5c6YiRoj05fJvhgsnlloUFxalO6L76-nSj0X9BEN1TKYurDnuhNRB2ACeXLkf4RBJL--8N2h1JxAZdQ8waczZdeQTk8sCniOsPm9rD89PPcB3WOWGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اجرای قطعه مست نجف توسط کربلایی علی‌اکبر حائری در اجتماع در پناه غدیر مردم مشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/656193" target="_blank">📅 21:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656192">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3dU3twq8YT3l531ttzjNr5hqibzpaSWJaVykwRdwxJV7j68ZRftklbNYj_9gm2hhCUG3BAc4CKmvCBauqsUV9bMcKLi9t7-dwVb-sXp11P6fd8cbxQObMAL_Wcx7-ROuGtPq0Svw_EAhAoSBJyZRuHLh2F6Z7prrTsnYW7oZkivUxUQCt_aB9MArTW3A-Ll1FdBVXQvmNy8n7t5h8NX79JHheAS19WRRGy4JkNpJEh2Q8YvcisKFjvoyaZP1gS6qk7uAdgmHPf2ootK7zfvT0nT_5ZkcZaWaHr-fLiyLNZZPlGy1Bc5JRgkwMm-bRhgx9l8Td-k01DqJVTIdamfqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین تصویر از سردار شهید امیرعلی حاجی‌زاده در شب عید غدیر ۱۴۰۴
🔹
ساعاتی قبل از شهادت به همراه شهید سینا سهامی از محافظین ایشان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/656192" target="_blank">📅 21:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656191">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ بارون نجف</div>
  <div class="tg-doc-extra">حاج محمدرضا طاهری قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/656191" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
دل بیتاب دل بیچاره
سر زلف تو اسیره
شب عشق و شب مستی شد
دلم آروم نمیگیره
شب عقد اخوته بازم عید غدیره
🎙
#حاج_محمدرضا_طاهری
#عید_غدیر
💚
مرجع رسمی مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/656191" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656190">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
گل دوم برای ایران توسط رامین رضاییان در دقیقه ۵۵
🔹
ایران ۲ - مالی صفر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/656190" target="_blank">📅 21:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656188">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ادعای یک مقام آمریکایی در گفتگو با الجزیره: آتش‌بس با ایران برقرار است، اما ما به حفاظت از نیروهای خود و اعمال محاصره بر بنادر آن ادامه خواهیم داد
🔹
یک مسیر کشتیرانی آزاد از طریق تنگه هرمز وجود دارد، اما این به کشتی‌ها بستگی دارد که تصمیم بگیرند آیا عبور کنند یا خیر.
🔹
از زمان اجرای آتش‌بس با ایران در ۸ آوریل، تقریباً ۱۰۰۰ کشتی از تنگه هرمز عبور کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/656188" target="_blank">📅 21:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656187">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca617cbb1.mp4?token=gj0eRvssAf_mDgf3iTzdNvnj07H1MmYsnPPw7fS_xKVJW6ETaadBVnLdf_F29bkEMKwMsgO3FXX32zVGxNBMi7237cpHyoSdiF--9T3CxhnQWrY-w-0aQhfRIUXZk-j-_FeBazFWmd17glXdm1NZ62xFVH47Nod87iqsHl8tnCnZ2cFKW78eoccbKzQYCCMLITHC_t4ALlLNafQNxf9UIC3u9FqrrljYAXnDF4BzTQHUuUKku8qBLakda9gYg2ZKd_9qvCbcvn4kwxVlLPkiFotdlNnwLvX8jSvl9MbHlC5kygnCYTUCsjl-EkJrzplvHrXyJtjnjeGEYdSV309-ElBOg7HzGSARZ7GgSrOEUQu9zuzmT51OvQ_818JxFuPbKYociv7sUU7PyyaDyvq9485cRNzCHp_JH5Pps5DmWJiW6-CWeuAnP1HXh0NO-R2yRujcgCWhf5p_dZ092CNN9hUCUx2ECCrvHnCeBvvK9uUD6fI1Pi_EYLGMKRtIUsmmSF-cIEg13kmlLLLLY5rzqmJMvOSlyOCMVFWrUuOJWXfnu2XSo83YcLHFWWed6gCs_mYXsa06nwg5cUcyzzhxMQTn1FSM0EMlX1-mfGVvhvg6CXzDlTtKi9z4SB9EN6uiUtonoy4C9l9c2KnhbdFDIdIdRXpBEy8Ji_8aKfzKfXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca617cbb1.mp4?token=gj0eRvssAf_mDgf3iTzdNvnj07H1MmYsnPPw7fS_xKVJW6ETaadBVnLdf_F29bkEMKwMsgO3FXX32zVGxNBMi7237cpHyoSdiF--9T3CxhnQWrY-w-0aQhfRIUXZk-j-_FeBazFWmd17glXdm1NZ62xFVH47Nod87iqsHl8tnCnZ2cFKW78eoccbKzQYCCMLITHC_t4ALlLNafQNxf9UIC3u9FqrrljYAXnDF4BzTQHUuUKku8qBLakda9gYg2ZKd_9qvCbcvn4kwxVlLPkiFotdlNnwLvX8jSvl9MbHlC5kygnCYTUCsjl-EkJrzplvHrXyJtjnjeGEYdSV309-ElBOg7HzGSARZ7GgSrOEUQu9zuzmT51OvQ_818JxFuPbKYociv7sUU7PyyaDyvq9485cRNzCHp_JH5Pps5DmWJiW6-CWeuAnP1HXh0NO-R2yRujcgCWhf5p_dZ092CNN9hUCUx2ECCrvHnCeBvvK9uUD6fI1Pi_EYLGMKRtIUsmmSF-cIEg13kmlLLLLY5rzqmJMvOSlyOCMVFWrUuOJWXfnu2XSo83YcLHFWWed6gCs_mYXsa06nwg5cUcyzzhxMQTn1FSM0EMlX1-mfGVvhvg6CXzDlTtKi9z4SB9EN6uiUtonoy4C9l9c2KnhbdFDIdIdRXpBEy8Ji_8aKfzKfXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
حضور پرشور مشهدی‌ها در جشن عید غدیر
▫️
این برنامه به همت هیئت قرار و مجتمع فرهنگی امیرالمومنین در مشهد در حال برگزاری است
@Heyate_gharar</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/656187" target="_blank">📅 21:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656186">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c9c8c965.mp4?token=RFMYAb7RJp8EAIrSuvHPjJuJF9X59gLOGTOvifvJAV4bIU37h-qcFkXKOigCqQXmtJf5CyyQUFfzR_Tty6K-ar330D7ORylLaVb06knnbbG6DJP4KoenhesDxgQ6ccgL4TEfJiIOs-v0503ht8LoVMYIdN8tayCTio24qlv6S30mSTkhrDby21S5Fa9b3VzaKvYmnZLH7XOw0GWnN0k-Mke9eaPt1bJGzQnQeSSiJQwjBJFNEpKg4btleDPhpLCrxw-0QMS8v6PkHzd8jSmOwmjGhOjhny7SC7ngMeeczYjWNuWczHJYeN3LqK1tJ5VZaioz5GkuYwOuKduT1Rz0irCt3Uqhou4NvBTSMmMeptbUY4cbuqaJBQmC2Hz1dkKkgnHyvNMOu4VBNX7a18JDeqD_XrxVu7tE8XA_Dgp1ru2Y5UyCtShsCyYoYfwLYakKE-qzcICzH20Uf1litySHeQgR9GYWjY3oaLLoT-Jol2F4MwbH5cLwriQ8w_mYhJ9HseQoKhFztfsi_WGLDdDBfo-SzCk9GGHbhHGzW6apTBIrt0EwHf5gYeq08D-EnrHozVD__ZFJjuoCkXfIfFdoL2ftqeXvcrVhEIV15UwnPreU7xRilPnYH_Fk_GZDmz4HKSt7dPvGxkofEuAejhLd5ibO84du5Lw8eoYZXs02i64" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c9c8c965.mp4?token=RFMYAb7RJp8EAIrSuvHPjJuJF9X59gLOGTOvifvJAV4bIU37h-qcFkXKOigCqQXmtJf5CyyQUFfzR_Tty6K-ar330D7ORylLaVb06knnbbG6DJP4KoenhesDxgQ6ccgL4TEfJiIOs-v0503ht8LoVMYIdN8tayCTio24qlv6S30mSTkhrDby21S5Fa9b3VzaKvYmnZLH7XOw0GWnN0k-Mke9eaPt1bJGzQnQeSSiJQwjBJFNEpKg4btleDPhpLCrxw-0QMS8v6PkHzd8jSmOwmjGhOjhny7SC7ngMeeczYjWNuWczHJYeN3LqK1tJ5VZaioz5GkuYwOuKduT1Rz0irCt3Uqhou4NvBTSMmMeptbUY4cbuqaJBQmC2Hz1dkKkgnHyvNMOu4VBNX7a18JDeqD_XrxVu7tE8XA_Dgp1ru2Y5UyCtShsCyYoYfwLYakKE-qzcICzH20Uf1litySHeQgR9GYWjY3oaLLoT-Jol2F4MwbH5cLwriQ8w_mYhJ9HseQoKhFztfsi_WGLDdDBfo-SzCk9GGHbhHGzW6apTBIrt0EwHf5gYeq08D-EnrHozVD__ZFJjuoCkXfIfFdoL2ftqeXvcrVhEIV15UwnPreU7xRilPnYH_Fk_GZDmz4HKSt7dPvGxkofEuAejhLd5ibO84du5Lw8eoYZXs02i64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت الاسلام محمد برمایی در برنامه در پناه غدیر با حضور جمعی از مردم مشهد: حتی یک نفر هم در شهر میناب نمی‌خندد چون از هر خانواده یک نفر شهید شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/656186" target="_blank">📅 21:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656185">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fec7f8a30a.mp4?token=hr4mLDwuoYg5XTbGpQCGcj07jojOtno-sBjcRBEatDT1AY8w-1g8u8tBhn0DSVmLDGQWonp92LtYl7r1nsy7s4WHBVelO4QfSMg7OSCxXreAxXfhGJIhFhP4RBBc01a4-L5hAKJr47FxJ_ixB4pqaPTuP_NyN1Zu-yJ-bLFNnManHSc6JCNzEI1UIsUv22kbgE25PEA8RLb9txfhTncXND8Hh75JxGhdgY5HCnqhF438AUc_u8ah-HtJJmivocRQVsfrPnPK5EeqiJ1PaIAKNcN6B8sFZTO5ruhUYUJaqZe4rAY_RyjfVGVwn0UEyMzIKOfO2esPuJapwL1Kt1QjNTUoB-Us9HPVAvP1rCfxIpd8Il2M4bWeZvVxDgQTqRsRBfaNxdqEVvOAR2cew9OZgsYvlfvBGfctWA5UJYlGCtcW93n5dWtBf9dqrPtj9-4HS8Ter1VaEyyRliLaxalhQmB4Kqpu5TPmsv0hhIe4kwgAFZyH8HsipeUWOYLWYnmSqwAPZXB7ZxThnWe9D3zjHovaX7xIEHcwYWe9Mcty-7nz6GYCl3MnnLrLEb0VVjkan82pIKLCBfu93g0gPLVlwzr2TmjnW3nVQLf0Eiinih3nfkvjpHvlPrD0pbtb83rF3kpbvwr216hRbBRmC6d7J98mh4HPtONU22JcGXqW5OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fec7f8a30a.mp4?token=hr4mLDwuoYg5XTbGpQCGcj07jojOtno-sBjcRBEatDT1AY8w-1g8u8tBhn0DSVmLDGQWonp92LtYl7r1nsy7s4WHBVelO4QfSMg7OSCxXreAxXfhGJIhFhP4RBBc01a4-L5hAKJr47FxJ_ixB4pqaPTuP_NyN1Zu-yJ-bLFNnManHSc6JCNzEI1UIsUv22kbgE25PEA8RLb9txfhTncXND8Hh75JxGhdgY5HCnqhF438AUc_u8ah-HtJJmivocRQVsfrPnPK5EeqiJ1PaIAKNcN6B8sFZTO5ruhUYUJaqZe4rAY_RyjfVGVwn0UEyMzIKOfO2esPuJapwL1Kt1QjNTUoB-Us9HPVAvP1rCfxIpd8Il2M4bWeZvVxDgQTqRsRBfaNxdqEVvOAR2cew9OZgsYvlfvBGfctWA5UJYlGCtcW93n5dWtBf9dqrPtj9-4HS8Ter1VaEyyRliLaxalhQmB4Kqpu5TPmsv0hhIe4kwgAFZyH8HsipeUWOYLWYnmSqwAPZXB7ZxThnWe9D3zjHovaX7xIEHcwYWe9Mcty-7nz6GYCl3MnnLrLEb0VVjkan82pIKLCBfu93g0gPLVlwzr2TmjnW3nVQLf0Eiinih3nfkvjpHvlPrD0pbtb83rF3kpbvwr216hRbBRmC6d7J98mh4HPtONU22JcGXqW5OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت الاسلام محمد برمایی در برنامه در پناه غدیر با حضور جمعی از مردم مشهد: مادرم می‌گفت تو برای آخوند شدن خیلی قرتی هستی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/656185" target="_blank">📅 21:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656184">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCvNG9fwxc8Z3Ha3zqDQJ51H4zyxq3ht1MoznjinzdbGOlf9PEGBV1sN1nJMRMMxU77wg4yDYEYXqGk0hhin9IZB95ojY5VzgPaN1mc2iXVOVtdSt5C802ovYwkqtdTeb_SSYUBupsvF9bVUlFTYN6KvOc7iQKnLIjjHpOM0MuoUK3WErFpSOj0tcp5wblswJxSB5xmc6N3rBagD8jtOfhx-Q_mVXNCxkEjcxJwTkTHtaek8yChwsCzo3RGQWhNVkHJX0vuetpNd48o82Q-erSb8FxP5JiibIrqWMvx_QZ4QNMf4aR2fWq6kEMCc_XJGCAyhHggC1P1MOgOJl4LJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قرآن به ما می‌گوید؛ راه خدا همان محبت اهل‌بیت (ع) است
🔹
قرآن با دو تعبیر آنچه ما بای به عنوان مزد پیامبری رسول خدا (ص ) انجام دهیم را بیان می‌کند: یک‌بار «پیمودن راه خدا» و بار دیگر «مودّت اهل‌بیت(ع)». از آنجا که هر دو به‌عنوان تنها پاداش پیامبر معرفی شده‌اند،…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/656184" target="_blank">📅 21:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656183">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMe6xgXfkhJsOvBWL8uO0YY62YaQi1WT93RAIVcX7ZKoiBgPueazVXE0kDB5E_Ob2yxCBpboKboIeK7FcehURc4S149oYqCUhNXFceXDxzCeuPightWJrs5tTZrzOj6jKytJ--KUozvtJY_LpYDk0o95ZExr83oKjDu526SgD3_S5tN3KRNEv_o9jf22SWYPA_3fWg23PFkDon1YACWN045Pdq4cNbiLwspc5G7TTrj8azWL9r-i42k_LDggk_pJ4cr9SOfw-7UGlHG4xm_xXDZ4gzzWKxMXixKipeMDlP3z-W9mn2Dh57eJNVGv9PtPOw0F7rG25Nrpbk_rN1KMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استایل جدید محمدرضا گلزار سوژه شبکه‌های اجتماعی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/656183" target="_blank">📅 21:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656182">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf15e7412.mp4?token=Lfiv185N8UDQh0nJJQQWDmNS6214TwqT3F3NtZtj3bzSXViDM3yQLXMSHR0pbx9hHAfi5DwJXwSEmoHoEiBL0lp12vGG3D_67hnuliTAzuZYAYc0IxpoJhN4wyhMhF-jksdzVJ2D1bcOwONpm0UJh23dgO8KNdfDIANhmIsM0Hc0wjzVunvizu5QEhM3Ihvm556sV5etqSMUt644Xl9plkwfVgTJQsEckeWr1LjJej7cKAFFcvLIoYlwVX4mHF5rjfgR9c9Ye5ktMgtdDoSIk5B60cA4-wFpXoBJKi3qsqSdMzi0xS_nBNRy_hFih9z-5AWd18TKp_afA3JDk8Pn7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf15e7412.mp4?token=Lfiv185N8UDQh0nJJQQWDmNS6214TwqT3F3NtZtj3bzSXViDM3yQLXMSHR0pbx9hHAfi5DwJXwSEmoHoEiBL0lp12vGG3D_67hnuliTAzuZYAYc0IxpoJhN4wyhMhF-jksdzVJ2D1bcOwONpm0UJh23dgO8KNdfDIANhmIsM0Hc0wjzVunvizu5QEhM3Ihvm556sV5etqSMUt644Xl9plkwfVgTJQsEckeWr1LjJej7cKAFFcvLIoYlwVX4mHF5rjfgR9c9Ye5ktMgtdDoSIk5B60cA4-wFpXoBJKi3qsqSdMzi0xS_nBNRy_hFih9z-5AWd18TKp_afA3JDk8Pn7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور ارسلان قاسمی بازیگر معروف سینما در مهمونی ده کیلومتری غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/656182" target="_blank">📅 21:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656181">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d60a9878.mp4?token=elRtoSQZ6v6dwwBttWXHD65W67tD1GSL0qmCnmqeerIv0tQvHoPhFwEOy4LXJRB2jy9OgKwnpv98jWBRLAu1AWmuMv0k1oRnq_5WKet1CewczVer4iq9jG3MW_WFYQDKDYuubCpzQ2xeJdFTyV6Og4HHZSWljQn-I5Jbzv5kSRUm_iRwkGjS3Bguj3-PbkAxm8qo1a0rYskupTCVmT9hr9HW7_okwSVQttNQ_mTcXsGZSWQGx-L8RJXBSNBzwk__T4me1FBEoDCJ35jOhADCOjUSpJtAGA9y8lN-pHabNggPO4UEoVlZQCTR512sFFwtNjCCgVSCr2ewXRLqi3DIJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d60a9878.mp4?token=elRtoSQZ6v6dwwBttWXHD65W67tD1GSL0qmCnmqeerIv0tQvHoPhFwEOy4LXJRB2jy9OgKwnpv98jWBRLAu1AWmuMv0k1oRnq_5WKet1CewczVer4iq9jG3MW_WFYQDKDYuubCpzQ2xeJdFTyV6Og4HHZSWljQn-I5Jbzv5kSRUm_iRwkGjS3Bguj3-PbkAxm8qo1a0rYskupTCVmT9hr9HW7_okwSVQttNQ_mTcXsGZSWQGx-L8RJXBSNBzwk__T4me1FBEoDCJ35jOhADCOjUSpJtAGA9y8lN-pHabNggPO4UEoVlZQCTR512sFFwtNjCCgVSCr2ewXRLqi3DIJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هفته حقوقمو جمع کردم امروز بیارم نذر امام علی (ع) کنم
نذری یک پاکبان در مهمونی ده کیلومتری غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/656181" target="_blank">📅 21:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656180">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dbf214dc5.mp4?token=WtCm31XkitCyucfA_4FpJIyJMLMX3kvSOiagWF39sbaww3UbCbGVlP6lsIHjanlovIoUcE5z5pNmGpE9jOGXbC3BBNLD9cxi3RSbGHZ3lYjCcWqRh_fKpOLju9LQljXqKhXIGlgjxknEitt4vA6oSXtsW7LkTUtnoQ1pQALmf5YOgB4n5VKE5_91d_kSIWgmcBhbpgVr3TcULhw6y4krvw2xZUgbtMJ9Lirxmt2ICQEIz4N3Z7RoKnr21FB2_brXmQ04QMU6AbN9cNLm7NJGF_asDCs5R5oqei_ozJL3yYMUKOfEODRzfRc1kmoGYU8Gw_dJ2mqg6VZDh4xexMWWYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dbf214dc5.mp4?token=WtCm31XkitCyucfA_4FpJIyJMLMX3kvSOiagWF39sbaww3UbCbGVlP6lsIHjanlovIoUcE5z5pNmGpE9jOGXbC3BBNLD9cxi3RSbGHZ3lYjCcWqRh_fKpOLju9LQljXqKhXIGlgjxknEitt4vA6oSXtsW7LkTUtnoQ1pQALmf5YOgB4n5VKE5_91d_kSIWgmcBhbpgVr3TcULhw6y4krvw2xZUgbtMJ9Lirxmt2ICQEIz4N3Z7RoKnr21FB2_brXmQ04QMU6AbN9cNLm7NJGF_asDCs5R5oqei_ozJL3yYMUKOfEODRzfRc1kmoGYU8Gw_dJ2mqg6VZDh4xexMWWYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نذر بستنی قیفی ایتالیایی در مهمونی ده کیلومتری غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/656180" target="_blank">📅 21:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656178">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46290c09c.mp4?token=HZG4Cp8Q8MPryrnbIO4fdvJg6mlbQYYqxzqb6xl1iBpFs9RMv7ZJWMzRhzTGkgSas7ijL8xp1Z-j0Ahws8sKk6c27fDBbQPu00yXNZSRhpxb2kKH0O2n9LKtFVM9ZppN6TS6k7w6HfO83TI9kWNegfS3iciJcje3ZAW4SW9DWLgWFW6DkPDtSXZOIhnXxN71kgd4y7Mb8HiiPOZDNqfF94KD3DiKMD560C-NNQVoY-10b2708imI3SqvuUK4c4yTYedXrmt3XPEShECpsHYfmeIOY4h5uMbhv8NEIBc6OSVo3yzC18_t4VrutL4C9fiR1ZZc8IVKsvhf-_H7BBVJlkQnvIsgQ-ocGGLlsefh8SNoRB7rY7rZGKp7vUs2aOkWGodf3_LFUBrgFIT9pPEbskBYLPr2AydOJH2T_9hVGrJ-c_q9Z_j-_5usf1Uk5bkvUfCJGhaNAz1fHYVenYPR88O_d4esvvWr9CPt-kG69VQ3TD7RJymO7_aIj9whXq-jZt6dfAqAB8bN5ZhtE9jUcZXuDViTeaMJpxKsCbAGwC1O-WlDxXEgtLwM1LGJK0XmcFI7-T5rdJeqY4nrYUyfVzIgbYYXnnqEwLyvaQSl5gHoAgV_326sFDyyFitiFWQpgyBl1sNG-ekokZgw2UWlLHTJbUTojzfuhWin_HyZxTU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46290c09c.mp4?token=HZG4Cp8Q8MPryrnbIO4fdvJg6mlbQYYqxzqb6xl1iBpFs9RMv7ZJWMzRhzTGkgSas7ijL8xp1Z-j0Ahws8sKk6c27fDBbQPu00yXNZSRhpxb2kKH0O2n9LKtFVM9ZppN6TS6k7w6HfO83TI9kWNegfS3iciJcje3ZAW4SW9DWLgWFW6DkPDtSXZOIhnXxN71kgd4y7Mb8HiiPOZDNqfF94KD3DiKMD560C-NNQVoY-10b2708imI3SqvuUK4c4yTYedXrmt3XPEShECpsHYfmeIOY4h5uMbhv8NEIBc6OSVo3yzC18_t4VrutL4C9fiR1ZZc8IVKsvhf-_H7BBVJlkQnvIsgQ-ocGGLlsefh8SNoRB7rY7rZGKp7vUs2aOkWGodf3_LFUBrgFIT9pPEbskBYLPr2AydOJH2T_9hVGrJ-c_q9Z_j-_5usf1Uk5bkvUfCJGhaNAz1fHYVenYPR88O_d4esvvWr9CPt-kG69VQ3TD7RJymO7_aIj9whXq-jZt6dfAqAB8bN5ZhtE9jUcZXuDViTeaMJpxKsCbAGwC1O-WlDxXEgtLwM1LGJK0XmcFI7-T5rdJeqY4nrYUyfVzIgbYYXnnqEwLyvaQSl5gHoAgV_326sFDyyFitiFWQpgyBl1sNG-ekokZgw2UWlLHTJbUTojzfuhWin_HyZxTU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حجت الاسلام محمد برمایی در برنامه در پناه غدیر با حضور جمعی از مردم مشهد: جوانانی که در دی‌ماه کف خیابان بودند نامه می‌نویسند و می‌گویند رهبر شهید ما را حلال کن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/656178" target="_blank">📅 21:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656177">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
گل در دقیقه ١٢ برای ایران توسط سعید عزت‌اللهی
🔹
ایران یک - مالی صفر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/656177" target="_blank">📅 21:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656176">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
شبکه ۱۴ اسرائیل از آغاز نشست مهم کابینه امنیتی این رژیم با هدف بررسی سناریوهای مختلف جهت دستیابی به توافق آتش‌بس در جبهه لبنان خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/656176" target="_blank">📅 21:10 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
