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
<img src="https://cdn4.telesco.pe/file/dZgscLsOJWDZJWaENpraM0Vmeti-gSV910qZ7AmchnSSzfgu5t1fm_WcOp3yVF_zQea3eJPGaBK8R2DKsUmTSgIDeJPYpYVEuuNTj_7bcUg5IPEm-j_uEWLBQIV9zNWSygz-zyE07ICylBZK_R6TY-s97Bz3gn4BFOo6kMM1udyxh3e23EYJJoE2Xf1T8L5xUu-C-gE-iIpYJUJWe4KKDjp_GhKDA0sZvSV_ULbQFGUI42J5CcOqWPN-m79qldGh451HsOZD4ELIgHcycADi3_PYervWGfulEAKfj0FTWjCwHtI5XFIO3uJivAPewBXS9xP-VVDdTYGaJArHWm99YQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 214K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 09:53:06</div>
<hr>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=fy1a_g45Vf9_wtm16U5e8IeK3483oQQM8OgT7xvO3k_VaJTl0HmPWgzxSURFuGe2wFv_N9t2K6g1lpp0708Pxt4-62p-rv3HRIXH5W7eiJQ_pozgU0NxVsTJPfwT5TzP_SR8xwkSwRI1ZiQK-ebovyOVaCkxlRBxU0REQjtGYmQ9hM6ttSG08Qkx05_giypbZWgHyGVmrZn5X6VtHNtMyeZF-CFwbllUVfKOp80ILofr47GnpOzbPiz4ioRV5RxotFuSXj2A3xf70jy6jdUxEkolmpVymWIZrz-T93Zv0j0l3mdM5csvc7vnwE7NXcoxlBozM73UZWOCtD3KU5VNe4FmGtvSGfz6b1wh7-v9Ho7Z_eOwhz98Cxs9VlaUBFa3rvMkX-7tobDuT7H2OH0jSu7u58CKmOTIwibJ4CqbDLk9ySfdgDReTwvkh6xE3z2CX2BAQSIf5aZOxo0gK1kmwcdRRhv_6EnePJIXVE1DL70vGME6A2gjDonbKOHUnYgFw7TNT1MzbVEQ7vGK9FPctlwYTlawJDj9Q9K2kqEKhDpAdXgDOsG2fqxDDD8NtUgZOI85xqJo_ieUpSNHJNtpOdXZbdT1O0Nfr8psy_k270iyN9KZuXW3kblKwIAqGYKeyE1VqXM173qC2gxUbil4OBTQgcY-xKFNk1AWhHW1TWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=fy1a_g45Vf9_wtm16U5e8IeK3483oQQM8OgT7xvO3k_VaJTl0HmPWgzxSURFuGe2wFv_N9t2K6g1lpp0708Pxt4-62p-rv3HRIXH5W7eiJQ_pozgU0NxVsTJPfwT5TzP_SR8xwkSwRI1ZiQK-ebovyOVaCkxlRBxU0REQjtGYmQ9hM6ttSG08Qkx05_giypbZWgHyGVmrZn5X6VtHNtMyeZF-CFwbllUVfKOp80ILofr47GnpOzbPiz4ioRV5RxotFuSXj2A3xf70jy6jdUxEkolmpVymWIZrz-T93Zv0j0l3mdM5csvc7vnwE7NXcoxlBozM73UZWOCtD3KU5VNe4FmGtvSGfz6b1wh7-v9Ho7Z_eOwhz98Cxs9VlaUBFa3rvMkX-7tobDuT7H2OH0jSu7u58CKmOTIwibJ4CqbDLk9ySfdgDReTwvkh6xE3z2CX2BAQSIf5aZOxo0gK1kmwcdRRhv_6EnePJIXVE1DL70vGME6A2gjDonbKOHUnYgFw7TNT1MzbVEQ7vGK9FPctlwYTlawJDj9Q9K2kqEKhDpAdXgDOsG2fqxDDD8NtUgZOI85xqJo_ieUpSNHJNtpOdXZbdT1O0Nfr8psy_k270iyN9KZuXW3kblKwIAqGYKeyE1VqXM173qC2gxUbil4OBTQgcY-xKFNk1AWhHW1TWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67172">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmLkMlisL9Lh8vG3w12oCoM1P0OTvaKT7nSzLJQl4FjjA0gxQA0ikvaa8LsKbVPyqjSU0kwdm_TcPzcWkpf7niEtqO7NjjexK8L2p-K67wwP0OL0SXl3dBYpVtY3EID-pjcKofm07ijxV1tBmaLNNA6gEl4GAAbfxZaDo2Nio4GmcjLvV_2sCTkUaImgLp4oWcuy7gdcK2kYD8RDDX5R5vYwZEr5SrkHfbvaeg8nVXVL6t8g58v9x3XZ1v1kL9949HpL5r58Myss1vbORtJOC4vlWaT9JSoshXqT_evy5GAf3FoxVji_4eu3FkqvAfW8rcc-J-Zf5V1HWOrlI0XAkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
‏اطلاعیه ناوگان پنجم دریایی آمریکا در بحرین در پی یک سانحه برای یک بالگرد امریکا که طی آن یک تن از پرسنل مفقود شده اند:
🔴
در ساعت ۳:۳۰ بامداد به وقت شرق آمریکا (ET) در اول ژوئیه، خدمه یک بالگرد MH-60S Sea Hawk که به ناو هواپیمابر USS George H.W. Bush (CVN-77) اختصاص دارد، در دریای عرب فرود اضطراری روی آب انجام دادند.
🔴
در حال حاضر هیچ نشانه‌ای وجود ندارد که این وضعیت اضطراری ناشی از اقدام خصمانه یا حمله دشمن بوده باشد.
🔴
سه نفر از چهار خدمه بالگرد نجات یافته‌اند و هم‌اکنون در وضعیت پایدار در ناو جورج اچ. دبلیو. بوش هستند.
🔴
نیروهای دریایی آمریکا در منطقه همچنان در حال جست‌وجوی چهارمین خدمه هستند که هنوز مفقود است.
🔴
علت وقوع این حادثه همچنان در دست بررسی است
@News_Hut</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/news_hut/67172" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67171">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f10MIMpcOz0kGdTQbmkTzry4i1l4gRfUf8gtOELDdqeIdfZF36YTSDY9LZkyLn35Iabmq66whEmSwMgMK55z8aOnCi2dQv1F1bDNxcVTibRMkIfUx8sjfiL9NFJoCRdlMQxRVKzix4Er-OxPUEsf8cifWpb7LZeBUjjdEt8ffUVeSvZ6trFAHCqEjJBAjgNOTksf2AF-nwBmtCHT618CThl2ZQZ3tve8KM9WMd7tovCuJosfd5TOSDWV2LtZIyBOB2nn4bcDa1EsGWb16DTamj7o3ukvz7yGWPTUOM6p3puoPvOU2jeFjwC4N8InoHqKba-MUYFKw0xRiFAbgj0Isw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/67170" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OteJF0hYRGEzUIQ9egwX3RlFqS2WK8-hIEknzis_US2kKPDCpMNNGP31P9WgUwAKhdT5oFSlr-Jk_pbP5kHnuPuuYlAtAUDxHJABLeR0nkEem9E3Sf9S5Tn6ImyqnHMJSgoyekC7SVMuV_XCyho9M2vaMjwAmk15ynYVpDUbbsX_yLZ__qRRo2mI3XyJmPjY9xEjtstM1JAO3nkuDLflgafviO2znihGK_KfUU9y7yDlmJpGrCk6zQp-lpYw5eaH95Y8U3ghLZ-LoDjmDoLDNwad43MPE70Mun1QLp7M6K76toYv7CjDF3epUzv0GV0LHIVcBFDU9on2BNXXqLbU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=HK0c4nagj3XPa-KGgzZDpgOmvlkyVl_hVLgrLI7SJKy6UP0R12QRO92HV_Stz-IJxHQuEQGrblFZ1ShjfH37chUhOH3IfUQ3L4NXep__CGENT2hwpV7zyqU6_-VEbMtYBPGmAHlVpCP85swXB-B5dhQuOpxoBITGBS8aYqed_40BbxrpPIHvakkMHidAvcK4iq3lzH7OnDpQ6RRn-6095Yu7N_dMe9MrHxjOEez2zKAA-E-qJMxp0u0GH3bqWOk9X-mhy2c9iqrsxyB6J9Q2s34awFkApKxBK92kxlWmCp6v74gY96rsdJDtn_udBCVwutKLILxIYewsfNOwlNwbNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=HK0c4nagj3XPa-KGgzZDpgOmvlkyVl_hVLgrLI7SJKy6UP0R12QRO92HV_Stz-IJxHQuEQGrblFZ1ShjfH37chUhOH3IfUQ3L4NXep__CGENT2hwpV7zyqU6_-VEbMtYBPGmAHlVpCP85swXB-B5dhQuOpxoBITGBS8aYqed_40BbxrpPIHvakkMHidAvcK4iq3lzH7OnDpQ6RRn-6095Yu7N_dMe9MrHxjOEez2zKAA-E-qJMxp0u0GH3bqWOk9X-mhy2c9iqrsxyB6J9Q2s34awFkApKxBK92kxlWmCp6v74gY96rsdJDtn_udBCVwutKLILxIYewsfNOwlNwbNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه به مواضع کردها درمنطقه کویا در استان اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=R5x7Kg1hk-VbrCkqTUYO_dIqJbhkXUKoCGQDd1SXOAEP7rfDxSyU9qBD_SK1Ngbb2BDcis7j_cCgQUr8x6KmwARdbfOkjSU_fV7k-xSFZF59F8rUmssACO7TBL6wIR7iEHEpBMA1JZ5ob3nWS2OidR2oRDzq8DiyfqVmX27qC3T7SrrypxVqIJubV68Xg9Jse1bv_JpE9KZT-XWMN2ili8vj0MkGR9ZrSFGUnqTBw-BCdokYPVu8-dlJDVS5Ar9akhZU8oPWXE9gwBH9RkAHZzfvPwT2o9bYG5S869ACmiLF-ZyObH_z96iIHOuwA9ih4coARjGbEytAorrvWI1aUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=R5x7Kg1hk-VbrCkqTUYO_dIqJbhkXUKoCGQDd1SXOAEP7rfDxSyU9qBD_SK1Ngbb2BDcis7j_cCgQUr8x6KmwARdbfOkjSU_fV7k-xSFZF59F8rUmssACO7TBL6wIR7iEHEpBMA1JZ5ob3nWS2OidR2oRDzq8DiyfqVmX27qC3T7SrrypxVqIJubV68Xg9Jse1bv_JpE9KZT-XWMN2ili8vj0MkGR9ZrSFGUnqTBw-BCdokYPVu8-dlJDVS5Ar9akhZU8oPWXE9gwBH9RkAHZzfvPwT2o9bYG5S869ACmiLF-ZyObH_z96iIHOuwA9ih4coARjGbEytAorrvWI1aUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=tF9i-9Gv0_PBo7O9E4j_8cMZsDOuOgOm2v2hEXWZ6nmjpRuscDWGs2hty4-ptL5SANvJKMZChAabFX4uwJvdx-F-aK0Ppz-s8zgabY0Y_Qo1fUbVRiai11X7WlWz-czHgBeAl-3H65ipX5brbCdyySx24nVZrgzZL6iCUKq6H8-S8XX3KIyQu2tQ2aUrWD2yBQdyt_Yxp2RceN3Vg1tZ9_ac1-oG7t1XQTwQeAdm7Egro2PUzsJLyLE30p8IjUFEE_LTyWHTzlvRWDzAy9K6yPQg1MBTGNzQVyOSFMVczO0EOyW9oWBUpX2P7CpcaYShGw9ebU_Ql3egQ9JWgt7rsw7og210w_Lmw6RP6XkW8zokDRjoauo_vMr7xV_MCf8IWNOmKYsdE-A4bFSJu7SYypHz5ZZ_0MClvp7Xyu939YwZG7rCt4SLY3chgwEhcOvk5zDqZI_z5_krD4TkYoWi2-AbNYYhA90hBNn7SFw03JxHNZfnjFlu_Pt-zmvYwnIMkdyX2UqE1pE5a9xAJRVCx6Gn6WUA0qnlm9lfVw6OAqQAUkpqJiVdsYN_t_l_D2xUX5TqaJ5R6Wr5HOQjzRxoLglujGg4qb05vCfH3bef2Sg7rINDeZOHYT-bxLOt1Gp8eClgP9JvIDFCo0ilSiMw-Fs-OqIG6YAfEjQudhk9XHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=tF9i-9Gv0_PBo7O9E4j_8cMZsDOuOgOm2v2hEXWZ6nmjpRuscDWGs2hty4-ptL5SANvJKMZChAabFX4uwJvdx-F-aK0Ppz-s8zgabY0Y_Qo1fUbVRiai11X7WlWz-czHgBeAl-3H65ipX5brbCdyySx24nVZrgzZL6iCUKq6H8-S8XX3KIyQu2tQ2aUrWD2yBQdyt_Yxp2RceN3Vg1tZ9_ac1-oG7t1XQTwQeAdm7Egro2PUzsJLyLE30p8IjUFEE_LTyWHTzlvRWDzAy9K6yPQg1MBTGNzQVyOSFMVczO0EOyW9oWBUpX2P7CpcaYShGw9ebU_Ql3egQ9JWgt7rsw7og210w_Lmw6RP6XkW8zokDRjoauo_vMr7xV_MCf8IWNOmKYsdE-A4bFSJu7SYypHz5ZZ_0MClvp7Xyu939YwZG7rCt4SLY3chgwEhcOvk5zDqZI_z5_krD4TkYoWi2-AbNYYhA90hBNn7SFw03JxHNZfnjFlu_Pt-zmvYwnIMkdyX2UqE1pE5a9xAJRVCx6Gn6WUA0qnlm9lfVw6OAqQAUkpqJiVdsYN_t_l_D2xUX5TqaJ5R6Wr5HOQjzRxoLglujGg4qb05vCfH3bef2Sg7rINDeZOHYT-bxLOt1Gp8eClgP9JvIDFCo0ilSiMw-Fs-OqIG6YAfEjQudhk9XHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67163">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeEbQi8T2PC_sQqd4hKtH5vzOSgidP3JASufOrlidF1eEZaY4o-yRsCLKsjT_3fsH-K5zptddt4LtVRZ-ioni_Y9E6UbclXyeuRixzMGabj5ChOKHV5V5qSkdn0mX4IzM34HopQfn2DffcN59hq_qWfbvHSs4ExMnLPsIbYkDB2xUeBWhE4SuJUDLWvuoIXfaK7bpN1TYEtJ616qILHX7IStR-60MRKgkqH0wkfyobryJ0wKaeGm8K8fk40BzqS-ypFN8nSHfGw4wBiinMsnt70YY-MhmmaOhguLJFvOs7KgtfgDp5_HeiGHf_G0NkheESvTscOdaiPUnpa41kv0uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67162">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=XDFDKIXpOjeRpaQCs5lqIhMbjDJf2S6fPFf1Z12CkBVOIxHnAlkzXs2zkGci3tYawplQ-3J5HPlKCNo1pkq0hkL_a_CHqBTGfegG4103-zxJGyf0gk6BNBq1mvxmWc_voQUGzwZQOdNcuTrYQxVGY5Jt6nDt2NQW9AT3hucP2j0C_3E8GffqEmONerOMULdTJToCDqrSlu2ufgRM88jqjOEW-Clewjw-CmL3VxkSCxyESx__s-Q1iJYx0ZcULGU2KLJHA4pgNHgr9tGLN6pX0kBTBSzdNGNhEzcyf_Hzi-p4vF0KWPV-YlCKiqCM-zK-xFFHka83-xNn73uyrvM-5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=XDFDKIXpOjeRpaQCs5lqIhMbjDJf2S6fPFf1Z12CkBVOIxHnAlkzXs2zkGci3tYawplQ-3J5HPlKCNo1pkq0hkL_a_CHqBTGfegG4103-zxJGyf0gk6BNBq1mvxmWc_voQUGzwZQOdNcuTrYQxVGY5Jt6nDt2NQW9AT3hucP2j0C_3E8GffqEmONerOMULdTJToCDqrSlu2ufgRM88jqjOEW-Clewjw-CmL3VxkSCxyESx__s-Q1iJYx0ZcULGU2KLJHA4pgNHgr9tGLN6pX0kBTBSzdNGNhEzcyf_Hzi-p4vF0KWPV-YlCKiqCM-zK-xFFHka83-xNn73uyrvM-5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله پسر سردار طاهری به پزشکیان:
مگه نفت بابات بود که می‌گی ۲۰میلیون بشکه نفت دادیم به نیروهای مسلح تا بجنگن؟ اگر نیروهای مسلح نبودن ما نمی‌تونستیم اینجا شعار بدیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=rZudH1BrsrnPKWAgesSDejGtQsB1lakyDOPWRMo4LAkycWr-amMHuihK4NPc1UMXyEJO_FcC6ZH0bs9KWinjrliIc0qnu5fYdPhnzZLgG7ZRHn3pxibbJKE4u50o22a9URMGyafVQAJJxcBapu3_q7i2Mwe1a4leKiyXUHBEY3K_nPUJp0LIwTdgny2TLwxiMWtzCJyLFNudV8y3X2s0iGYaQR23pLcsAV-SK253moRkajXdYyRLMfLSbXjxLXd30ZAVDKSzUWktksLyqDwEZK8s0pujO0yfI5nrptisYS5uugR_7aQPgzccUzQr9IqorYUXRJAlYhBFHm_s9HFmsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=rZudH1BrsrnPKWAgesSDejGtQsB1lakyDOPWRMo4LAkycWr-amMHuihK4NPc1UMXyEJO_FcC6ZH0bs9KWinjrliIc0qnu5fYdPhnzZLgG7ZRHn3pxibbJKE4u50o22a9URMGyafVQAJJxcBapu3_q7i2Mwe1a4leKiyXUHBEY3K_nPUJp0LIwTdgny2TLwxiMWtzCJyLFNudV8y3X2s0iGYaQR23pLcsAV-SK253moRkajXdYyRLMfLSbXjxLXd30ZAVDKSzUWktksLyqDwEZK8s0pujO0yfI5nrptisYS5uugR_7aQPgzccUzQr9IqorYUXRJAlYhBFHm_s9HFmsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیروز کریمی:
قلعه نوعی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد، 30 سانت رو دیگه کجاش بذاره
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67161" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67160">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=G2hmaQQMk6cm6Mu-h0cBwmJs-BDvwrbVkRO6MpiSVhZMIzVKS3lNhhAdFTAItTVf_HR5d-elmbQRuLvV1XWr0bzDEuhI_VGTtQZH4EfriPttgIwiMC-ixRGx88AqSGMGFKM88G6qHfoQ8aaTjyfi38mtlFPUmpkSM1XV_yc0ZROPbCCrHsLGVb8leT4hObhoN6ZJVYFEsU6J5Y046cQ97-Dfius3VZUe2AP_j3hCxHkSRL-KY4odabqDKTam2jGSTr0EVjQOeLaQA3r_KeNUMdkeS2SwcAsjx7xIrEmJ_tRjEGAyR2bNAXCts1cDccNjJ7tVn7M2EN1YZddiVk-raw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=G2hmaQQMk6cm6Mu-h0cBwmJs-BDvwrbVkRO6MpiSVhZMIzVKS3lNhhAdFTAItTVf_HR5d-elmbQRuLvV1XWr0bzDEuhI_VGTtQZH4EfriPttgIwiMC-ixRGx88AqSGMGFKM88G6qHfoQ8aaTjyfi38mtlFPUmpkSM1XV_yc0ZROPbCCrHsLGVb8leT4hObhoN6ZJVYFEsU6J5Y046cQ97-Dfius3VZUe2AP_j3hCxHkSRL-KY4odabqDKTam2jGSTr0EVjQOeLaQA3r_KeNUMdkeS2SwcAsjx7xIrEmJ_tRjEGAyR2bNAXCts1cDccNjJ7tVn7M2EN1YZddiVk-raw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7lhaT-Ic-nzi2RP-gJ6aoXDmytJ48npqmADdjt_pvuZlI8GynlaWq6dyaWY-_xvo4RMN9JfbPQoPMz5JwlivucEEubEBlXAYXwg2KOySckxSlw7Pn2vdl0puQoqOIM9E7mOKZ_GupbKhCPNE8zeVeL9xeRXpsnw2njNO3SAMAzs1kd2h-7Oy0wwwh8pTZHH6sR9bvrZgBPthyLAxM1Z_WaAFuSF_fj4OvLgeeCG2GU8BF3gM4B2Le2gl125KkXy2nghuWQJOKQIKvXeHPUEtJJ4o1a1r586EFLAMY2UNP3uBZWm0firfaUUaTrBPIUilhXZokXyNV9dLizrUNmPBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=XsgOeTfRZNAtgj1_2wzfhS15JGFW5YsLBTtdna1h08tYT7GoFF4OsROpk13MficBFPbR3zL49Z273nSAaprgaAWoyO0hwMATzqshhFq2wj5SqDq_J-vcE2ujbdGSfm-c567HHY8OP-kTbusnApPG5jd7c_Q21K-1ZypcjQTohNJa2JMw0-tMrEXk3QM9piqeZ4SdQBytcp3XXBjLZ7S4kFYj6KuUZyetEihcFbTYmsHOROJr1r49HSdAqJbHqlPDA_mbGrxLz2zEvM1fy55w31wnPtzx3hkePkOPeaW1gkuXOvvoeQUNMmr10ERLGLlN3azw7A3SF5Q_8AOP6CZ4_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=XsgOeTfRZNAtgj1_2wzfhS15JGFW5YsLBTtdna1h08tYT7GoFF4OsROpk13MficBFPbR3zL49Z273nSAaprgaAWoyO0hwMATzqshhFq2wj5SqDq_J-vcE2ujbdGSfm-c567HHY8OP-kTbusnApPG5jd7c_Q21K-1ZypcjQTohNJa2JMw0-tMrEXk3QM9piqeZ4SdQBytcp3XXBjLZ7S4kFYj6KuUZyetEihcFbTYmsHOROJr1r49HSdAqJbHqlPDA_mbGrxLz2zEvM1fy55w31wnPtzx3hkePkOPeaW1gkuXOvvoeQUNMmr10ERLGLlN3azw7A3SF5Q_8AOP6CZ4_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«روند خلع سلاح هسته‌ای ایران به‌خوبی پیش می‌رود... بازار سهام تقریباً هر روز در حال ثبت رکوردهای جدید است. قیمت نفت به‌شدت کاهش یافته است... و اکنون از زمانی که من حمله به ایران را برای جلوگیری از دستیابی آن به سلاح هسته‌ای آغاز کردم نیز پایین‌تر است.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67157" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=YdVFFGXbuGn3SnZrpmnwSsiSVmS0ZtltsLbQ7DLbM7-KGJxZOr_6gXto7KdaeRUI-8WILn3bj2ddifVrRlXpYVhuFG9RwsGooP-AIyK1TsnHhCqPoBvcKQZgxQZcgS3sqnWRZwuUFEo-YrPHiKEGEoa5proFsCPciQGjU6ZDkMh9Pwoic-sd4BBMEOIzoOs5x1tExvFKuQ4HarK8hxbGMxhHPeILjbXKwU-fdMFV9boteggfkVylzYAKwJ1ak-cEpIh4l7wIYxDQcZ0yL_ZGgfJ1wWkBfTkSFt1cZV7x0uIWU5a9NvhWs5ARfv6SOptzU_i6L6VgIm3ymV9u0TvMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=YdVFFGXbuGn3SnZrpmnwSsiSVmS0ZtltsLbQ7DLbM7-KGJxZOr_6gXto7KdaeRUI-8WILn3bj2ddifVrRlXpYVhuFG9RwsGooP-AIyK1TsnHhCqPoBvcKQZgxQZcgS3sqnWRZwuUFEo-YrPHiKEGEoa5proFsCPciQGjU6ZDkMh9Pwoic-sd4BBMEOIzoOs5x1tExvFKuQ4HarK8hxbGMxhHPeILjbXKwU-fdMFV9boteggfkVylzYAKwJ1ak-cEpIh4l7wIYxDQcZ0yL_ZGgfJ1wWkBfTkSFt1cZV7x0uIWU5a9NvhWs5ARfv6SOptzU_i6L6VgIm3ymV9u0TvMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قائم‌پناه، معاون پزشکیان:
اگر قرار باشد هر آنچه رهبری می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67156" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67155">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=u6yLzMW0FIlFugXaN476XM-9Y-9U2ikHLmne3vpdT9sp4Jgm46xVZrvdMwBySyI5q7Hhpxj2SfezHpSZI_AsFN7lpKmoSiDqQ3X4eFXeqagYY8uq46rZ1xQMaGEITi2ulEqHOJaCTj5th6zQGQ2srb3caYSqBarjkeFCS9OXGe82cwUkcl5Oic9puslo1glcdzclP7nPYEVoeiCYhI4byVFrqnO9rBllOPM-uIS7IPAN0amwn4z0nohl5F7il3JlAdXU8sdrxeaA36g7Df-dD7G2Zn0UxJaLYrvyOsN37wBbC3HQrvgM7biFrGNsK11UL9NlytSEbIfaXxcyrzpKOaIvdZZqFnowEZrloLWKMmpHhb6YjWNEFg0pTRedWFoNcfAhMrct9pMtQrOnPWSfp8wn26lN5wZqCINYZzJZYgxilWZGVQzYn4zU__p9WXsnvFh6ci3a0w-yU7cPGJWTHi5xB_GfB_dcyI-FvIRpaEZFCSvukSlWjW_Mcysevz9oWQ1cgKXc6vHFbW0nRAeMOu_UWwOlBsVgUPm5p979bNbZ1A4oJzRjfqpm7Mq9WooX7WprgRB4T0Ka6W66wgQiEBXqnGZQ5ImKnTm9z8C9N_B2-b02iM_LZJprwbP5pxxl1v1RFxpDhOKMedtWzXRnmRiSMqxXNhUew9PbZWIAVoY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=u6yLzMW0FIlFugXaN476XM-9Y-9U2ikHLmne3vpdT9sp4Jgm46xVZrvdMwBySyI5q7Hhpxj2SfezHpSZI_AsFN7lpKmoSiDqQ3X4eFXeqagYY8uq46rZ1xQMaGEITi2ulEqHOJaCTj5th6zQGQ2srb3caYSqBarjkeFCS9OXGe82cwUkcl5Oic9puslo1glcdzclP7nPYEVoeiCYhI4byVFrqnO9rBllOPM-uIS7IPAN0amwn4z0nohl5F7il3JlAdXU8sdrxeaA36g7Df-dD7G2Zn0UxJaLYrvyOsN37wBbC3HQrvgM7biFrGNsK11UL9NlytSEbIfaXxcyrzpKOaIvdZZqFnowEZrloLWKMmpHhb6YjWNEFg0pTRedWFoNcfAhMrct9pMtQrOnPWSfp8wn26lN5wZqCINYZzJZYgxilWZGVQzYn4zU__p9WXsnvFh6ci3a0w-yU7cPGJWTHi5xB_GfB_dcyI-FvIRpaEZFCSvukSlWjW_Mcysevz9oWQ1cgKXc6vHFbW0nRAeMOu_UWwOlBsVgUPm5p979bNbZ1A4oJzRjfqpm7Mq9WooX7WprgRB4T0Ka6W66wgQiEBXqnGZQ5ImKnTm9z8C9N_B2-b02iM_LZJprwbP5pxxl1v1RFxpDhOKMedtWzXRnmRiSMqxXNhUew9PbZWIAVoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=pTZleJ4O-YnTke34vt2LDWdZ4JlnC7Gmen3tB56fTkVVhCX2QQvX48fmpbM75avOdOt8E2AM4tuaqBHUJTPpsM1SxRgLNXRo1qhwKVugskbHLvD4kefTZn8UhrkNU_kmVVstOiz2BWNIXptW0ykNjQ2UosNYn5FZugkYze8jJJXYbLZ5Wl_vEVU3hsl_cqnqTbglOVWrddFoHMrPCi6ETUJ-CS8k3C6pEMH05xVQBHeg1KiOmcwQqmKOmOLt_qiqmrb5p-_zRSRS3LkGtCggSE9oDtPHN1W0WL0iYZ5lg6vGcYOZFvnOrhPxKgEq66oJdQdpjvsJfdvdoEP0H91DRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=pTZleJ4O-YnTke34vt2LDWdZ4JlnC7Gmen3tB56fTkVVhCX2QQvX48fmpbM75avOdOt8E2AM4tuaqBHUJTPpsM1SxRgLNXRo1qhwKVugskbHLvD4kefTZn8UhrkNU_kmVVstOiz2BWNIXptW0ykNjQ2UosNYn5FZugkYze8jJJXYbLZ5Wl_vEVU3hsl_cqnqTbglOVWrddFoHMrPCi6ETUJ-CS8k3C6pEMH05xVQBHeg1KiOmcwQqmKOmOLt_qiqmrb5p-_zRSRS3LkGtCggSE9oDtPHN1W0WL0iYZ5lg6vGcYOZFvnOrhPxKgEq66oJdQdpjvsJfdvdoEP0H91DRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDJsvY-k3nQIop3kZT_kC77Fat9Mw5L827i1q2iH6STE7m1C4SqKsTLKAowN3o6jE_foJ9Ur1Bcbs3BpjpGC3Du-xidc_Mx2QroNjumzy6e_TB5Ppjgs-L0O8XrZZh-MfZAn36qJk5QDxYQX1VtiGdqF_PcQe-gbz_WVst-fKsh7fxrg1fxHh5kOXtsPUSzhx4i12LMH2he5Z5nwKW4W6Xc5T6i3Ea4MDPpmAjbPMJ5Pc_JqnXKcO1ekxxgSbxmDP-GiuGy0yZaBU24Kik0bi1O63fKjtReqmvkFTQAPVmyKQK6L4xGBiBa8lqseBQuA-MSgCqLn5mVQDtCigd35SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=BviUrXP9ErR23H58UynfnTn3cXI6U0q-dsGpzvBJ9FjXJV1XiZ9G0HvIiSsP3n8QLJXln9F_xPlcGQq-B6GwC4hdq-8gimfPRMbZH9vq3eKYbv2nkY0edVDs34VpGOGH-teYpCDnzmpB5wddZ4j4FKXhRjmEcRNdrdkJgsSr3SNmWhQtopR8N4EitbHk8Ft1YjOk3ZH8UohW0l5mP8s_kHO6femCwxSVep_AeUEgRLGfQlhXscfKPpAE_llABhWPv8qP28D1OvEXTO36iQ_Qs6oflif0uqODpFHTf0JYwZxVGLGUSqAXTioa_DL14_JsTW5jRdmPZaUdezY67bttLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=BviUrXP9ErR23H58UynfnTn3cXI6U0q-dsGpzvBJ9FjXJV1XiZ9G0HvIiSsP3n8QLJXln9F_xPlcGQq-B6GwC4hdq-8gimfPRMbZH9vq3eKYbv2nkY0edVDs34VpGOGH-teYpCDnzmpB5wddZ4j4FKXhRjmEcRNdrdkJgsSr3SNmWhQtopR8N4EitbHk8Ft1YjOk3ZH8UohW0l5mP8s_kHO6femCwxSVep_AeUEgRLGfQlhXscfKPpAE_llABhWPv8qP28D1OvEXTO36iQ_Qs6oflif0uqODpFHTf0JYwZxVGLGUSqAXTioa_DL14_JsTW5jRdmPZaUdezY67bttLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس:
ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی، بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67152" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67151">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=qEkiBpCl94BgqLWLK6Gqp6_5Ig76bL5vnSjDjZ74uX46ZdUIwHiy7QmZg2mVVjh_rIf57Rev5zG3WTrxzaHv-uxoIaNAuMf_L-MyMiaCgt-oGv_YOivHT-Ad2PE9PlZ7yjkCn_pHdSx1uTPNR1hbBtJeSWlycIhgQI43ZcFTaMbZ5rFKaoc2V-IWKaZ0D2ug6jRkZ1VNeH5BWyPLpde21gOOOuKzwLeaW1mGNjhqIvKpv84geph8D7YyUS-n3YLP_gvZrxDd6rISnLxpx3vAWb5yRlGd2J--0Z9bAIJ89uPkVICcdoc7SOO8bRTZY2bmBSvgISXyZEKuQgUuujWCJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=qEkiBpCl94BgqLWLK6Gqp6_5Ig76bL5vnSjDjZ74uX46ZdUIwHiy7QmZg2mVVjh_rIf57Rev5zG3WTrxzaHv-uxoIaNAuMf_L-MyMiaCgt-oGv_YOivHT-Ad2PE9PlZ7yjkCn_pHdSx1uTPNR1hbBtJeSWlycIhgQI43ZcFTaMbZ5rFKaoc2V-IWKaZ0D2ug6jRkZ1VNeH5BWyPLpde21gOOOuKzwLeaW1mGNjhqIvKpv84geph8D7YyUS-n3YLP_gvZrxDd6rISnLxpx3vAWb5yRlGd2J--0Z9bAIJ89uPkVICcdoc7SOO8bRTZY2bmBSvgISXyZEKuQgUuujWCJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت‌ترامپ :
روند خلع سلاح هسته‌ای ایران به‌خوبی
پیش می‌رود… بازار سهام تقریباً هر روز رکورد تازه‌ای ثبت می‌کند.
برای سه شب هم محکم بهشون حمله کردیم
الان هم روند مذاکرات خیلی خوبه.
قیمت نفت به‌شدت کاهش یافته، حتی نسبت به  زمانی که حمله به ایران را آغاز کردم ،
الان نفت رسیده به ۶۷ دلار،  پایین آمده.
هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67151" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67150">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/67150" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67149">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67148">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=Nz__s-OFi_l4sTUUKBxcylz16-WkM53oFZCMUs7uGJZAHUlMHor7il12h4s-i7lBHUld5dBYROJijG8OT45sxuQjqVNEQgJPyfulBJ5gFy_sySejFJ3OAWbrOIg1fvulpHczG1VStpPcOCeIOkkvBn3ZmM_8-HEuQQglWJEIdo-tbLgKLqCoGd1C1CKcXG6HpA57YQEgz9SAXJrVqpWQ5Yq6hf5mUTrHCmpydso_jcJSBTIve-0NTbps1CpUUTNoD-Fu2lp_CVvZy9S8JpCjxIOGNm8mGXDB1-YXvngvp84jbMMclspc7Fig-IQGDdBhn5IkbtFod1bmAJmOhlQQvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=Nz__s-OFi_l4sTUUKBxcylz16-WkM53oFZCMUs7uGJZAHUlMHor7il12h4s-i7lBHUld5dBYROJijG8OT45sxuQjqVNEQgJPyfulBJ5gFy_sySejFJ3OAWbrOIg1fvulpHczG1VStpPcOCeIOkkvBn3ZmM_8-HEuQQglWJEIdo-tbLgKLqCoGd1C1CKcXG6HpA57YQEgz9SAXJrVqpWQ5Yq6hf5mUTrHCmpydso_jcJSBTIve-0NTbps1CpUUTNoD-Fu2lp_CVvZy9S8JpCjxIOGNm8mGXDB1-YXvngvp84jbMMclspc7Fig-IQGDdBhn5IkbtFod1bmAJmOhlQQvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله امروز اوکراین به پالایشگاهی در حاشیه مسکو
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/67148" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67147">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/67147" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67146">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCu1k6_CBFWvEBSCbc-fgQTC28w0DJmH-UbYVHbjL79WyHCw-rJGO0LKCleZre3h-NVE6rFb3_vQ7GBEcdNZrAqjzqYYaQBB8CPjD4ksTVdl69LIpjMjMGXhWwy5ouF3Cl_ex8FYcgM3tMoU7iv5E0F-Kd9c3N3rDvH5CeXVN1qCv5-tw8ThLvyGFxrVdAvh82AM3btac-c2CsbTWFLUpRYmEs5NJtpp4QPivw2gXLbbBPUuHtOVg9VM82ytdFmOFMdCQS2mn5yzixH9XPX4m_4bZ5Y5xkV-l6hMThYPsOISrhcNev8kG0Rg3z5c-MJpP_yIlYrU7_VkHA2kQMCCrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67146" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67145">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=hZ46eJ8lFm6RYcCmsi8YfRSU6qpvjeIEiTccpSw45F3fxYqUER-wXQEMIduN4iwpP3G7eJPPDx3MRD4AVXrUslVbUWWSKk-9VkrGzLg1x38kwIs92puRTHVYN-QBJ_t7olKqGpDiyEKUmi58fP5kEXJvTvgP9b79xmx5Jl3vpuLth6HSujYmDB_4oGpFfUMTHd8mEBQLciQWasWrGblyAPWLuYc7VeD52G7ehdkuvGF1pEjEz7mNCdnsnP043O5XtqTrlbSIQ2pVwNs1OthkbudsVEb37lGq5Y12zcIvK2WfVEe7goc1gFpxspIfFYtaIB6lVTzNxe-9sHSxv5Ul7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=hZ46eJ8lFm6RYcCmsi8YfRSU6qpvjeIEiTccpSw45F3fxYqUER-wXQEMIduN4iwpP3G7eJPPDx3MRD4AVXrUslVbUWWSKk-9VkrGzLg1x38kwIs92puRTHVYN-QBJ_t7olKqGpDiyEKUmi58fP5kEXJvTvgP9b79xmx5Jl3vpuLth6HSujYmDB_4oGpFfUMTHd8mEBQLciQWasWrGblyAPWLuYc7VeD52G7ehdkuvGF1pEjEz7mNCdnsnP043O5XtqTrlbSIQ2pVwNs1OthkbudsVEb37lGq5Y12zcIvK2WfVEe7goc1gFpxspIfFYtaIB6lVTzNxe-9sHSxv5Ul7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=FnFkAQxb4oCcIJvrxvIP3OOZ_43E0Q5vdmdBtCprb3brc9SdqDx3agFGcjIEDKToslRD06JhqEXxewF4E70HyT5f5WrTy3kkXHqgc76stJanZXqnNGQsYn1Mv1FWMGHhviVDdbJoB-EjVvFJsIhQ1ZxhyRxUsgcIL9271twnhb_0FJSgKpdmpxtM0_LKx3-w2aRLmUCMYWlYzv9azqXUi-UPKGsbysxnW0SvO5IyyfFMNoERBa7eMCodzpik8DxtdJIeyoB2pwemKRqPAzVXWhpPhHONLsd8avQVSCafKlnN7xKL8_CTDbXUqTex0gL07His88MTVX0qxJC0BkZvhA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=FnFkAQxb4oCcIJvrxvIP3OOZ_43E0Q5vdmdBtCprb3brc9SdqDx3agFGcjIEDKToslRD06JhqEXxewF4E70HyT5f5WrTy3kkXHqgc76stJanZXqnNGQsYn1Mv1FWMGHhviVDdbJoB-EjVvFJsIhQ1ZxhyRxUsgcIL9271twnhb_0FJSgKpdmpxtM0_LKx3-w2aRLmUCMYWlYzv9azqXUi-UPKGsbysxnW0SvO5IyyfFMNoERBa7eMCodzpik8DxtdJIeyoB2pwemKRqPAzVXWhpPhHONLsd8avQVSCafKlnN7xKL8_CTDbXUqTex0gL07His88MTVX0qxJC0BkZvhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
🔴
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
🔴
پسر بچه: آره، جونم مهم تره
🔴
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
🔴
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
🔴
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
🔴
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67144" target="_blank">📅 17:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67143">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=e8sRXfng7OXUJWO7Q1s5avrmBwXXIunhscvWkXpUoGGSvjhnnCPe2NEb4hFmAAW3P7I4Ix0DYM8NQ4zp6U5kOdl9iMYEG71GCBL7rehx0wfezR3YOtITGcaQ2dOFm0JEOxpU_ETFxh37SaGz9bXWc3oHPrRxrdqsTmOiIuOiV0QbeGCWqvo6cN5E0Sa0e4cjavOpP7TXxQeQn2CObPx4JDPgcTy2h9zSHb6B5FjkXi3lagegxeNUYuEyhFjMZVy42qBmPVm90Jg4wv496ZjfN_OThS7-QbUc57j4s08SElwkwHmXdq6Uv-HmMZy4Lj3mvmMgvZYyXodTXrbU7s11dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=e8sRXfng7OXUJWO7Q1s5avrmBwXXIunhscvWkXpUoGGSvjhnnCPe2NEb4hFmAAW3P7I4Ix0DYM8NQ4zp6U5kOdl9iMYEG71GCBL7rehx0wfezR3YOtITGcaQ2dOFm0JEOxpU_ETFxh37SaGz9bXWc3oHPrRxrdqsTmOiIuOiV0QbeGCWqvo6cN5E0Sa0e4cjavOpP7TXxQeQn2CObPx4JDPgcTy2h9zSHb6B5FjkXi3lagegxeNUYuEyhFjMZVy42qBmPVm90Jg4wv496ZjfN_OThS7-QbUc57j4s08SElwkwHmXdq6Uv-HmMZy4Lj3mvmMgvZYyXodTXrbU7s11dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67142">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=NaycmCbFmC9nVBvhHS4hYSkjnXFS8OZBZ13WumO7pvfyRLZyj_ou0GfBzv3_0U_vug9PBnWoRxlgv6B1zWIpRQZZ2gwFD9ZdAWCBD9C8h8yjpx5Nl61KuyFy6_ZCTQRTPfOFKYkjS-82ll_75pkjZvPhF4klTKoCziQfjbVT7KJKankeVV7ZyCAo25fHt3d1A0MQSeLyMreILiPBeLVatdI95Fa7mYx-s7Gbis92c8fP3Wu8bHvHWriFH64apwuJe0anBcTfKkJ1ziC86ipItaykiFpdCHe4sYprYg_cBAPtl93KgKwDnL2734P8yZwkvE6qJDzzcImypGlCMaiR0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=NaycmCbFmC9nVBvhHS4hYSkjnXFS8OZBZ13WumO7pvfyRLZyj_ou0GfBzv3_0U_vug9PBnWoRxlgv6B1zWIpRQZZ2gwFD9ZdAWCBD9C8h8yjpx5Nl61KuyFy6_ZCTQRTPfOFKYkjS-82ll_75pkjZvPhF4klTKoCziQfjbVT7KJKankeVV7ZyCAo25fHt3d1A0MQSeLyMreILiPBeLVatdI95Fa7mYx-s7Gbis92c8fP3Wu8bHvHWriFH64apwuJe0anBcTfKkJ1ziC86ipItaykiFpdCHe4sYprYg_cBAPtl93KgKwDnL2734P8yZwkvE6qJDzzcImypGlCMaiR0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_jEtGYWCzgQ2e02VjZUSlQp6k9f6qfQqxbtoIzwrlJq4RJHFipl697geJkdnmoMa7Ale_dh7-9FzM8uBNSFGyZXpWLeyEZpysfa12cmDydoCBJ5GtLjai5P1LUD8KkyJGYtYlKYhfpy_283gbM1Vq0_GVqsQYcRO22HxPC1HsXEW7P4zlXkL3BsrdlNoMxhKNu8Ww1rVtPX6ASAWc-i7aRBjZtBtZjIpHLNc0fXX-FiJxZA_MNys2QXteSvDy-omurkWh4aoa_nfVQ8-9fH12CqE2uGKMueXFbzfyzoMBuwLwz6MixH6RtrW4Q247TL_ZZR5JRxKghJQe7Y3IZx_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_LFiH9y5ZAQHCZXRanWkzKPOlkUrb1rMF3bYrlrJc_UrqvZr3aJZ-gd8d0EzN19aNS5clo1754tKCylA3jE8OlbaB8MH3jcNN0HcJBo5-J8r_BU49cv8WDhDvawf4vPDdq8chuFFrDzuVYTG-91Xi3ZchFtOU88yTaZrHHQUKCckynvAqIL0gYjpc7NbOKPLeXyr5j18MAFX_E6GGUk48g0C_pYgOEsbQTuPEW_oz6l4A5PJGEEIBbJQR6RyUg2BCB1Z3c_3WUL0YioaQlzzLPQU9CE5-qNljzeoxhpkSBlGkYDb1KsEc0w6Otq40FJXLdKD3BSvRenRqruKLEe4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کاتز وزیر دفاع اسرائیل:مجتبی خامنه ای برای کشته‌شدن نشان‌گذاری شده.
عباس عراقچی:هر تهدیدی علیه مردم و رهبری ما، پاسخی قدرتمند و فوری دریافت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67140" target="_blank">📅 15:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67139">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSmRWcu8XKr3y4DZnzklLtgbRDKJc7k0R9zZ4O9UMlGJgfZeIjZOcvQj2GXfdDRIPFe57-brMzjqsJ0p7PaegkyBeW_cy-Mn6C8BGCClRdJ7hjrQ9K0-YFd6zEIGkcICorrptIGHv6mqj3vEXdoLYTnz_zc8f0sMSp2Kvny7weRruN-hx5Q9BAiDuxbP-3l4Ia6S1yDh8XRWAjF7B-SYd-bhrjQEzLnvr4sjZ7pSthOQtMADC8_SVGxA5go7jMbubs4DShC3jU41lkig_lhgZJLhBotl8DL2Ontgz3zbjFcUqwBJYPdtOPmi4LhZKXISJEApsMhwDnxWEXgHtRX5Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwVH9uneR8NwtWsGmXJJEYUunc00Ei58pxZFaWPMUe72c77oViv5WDXDwkJxmPMrBTyaNRcQPdnYKaqhRKKJ_7nxXno_inAnaJhTJyI4HlwbdVmqwqoZsZ8x3Ax_pGjHl733dRfZq8UinUwdSBLxZam6xLG7QqmXENT7JfOnHzGNA7XmQKGX_kcBid6f2A85IIloy0eOQmSHcQwEYzwEKyMm6a3oCE16yiWRLfcypisXxJ0EHO8MY4t0ES9lJv3Lk63IMlaPxrF7HQsZLkDWzV2_gTx_4DLddWuB0qgzbaF7l3aNbBw549pSPPbzyXMTHMQT1bNUp6a_lm2Y_mjIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I723br4XHDi_yxde7aAc5FFIZFbc_SZVf9O-NcL9ZkfGUPVpzoutJyg2n1Vv0MjhoogRLIWpJ4y2rROMkg4rgUgdKZrBB-hk9MgrTRfUaAuRVaL-lWwWAMgoJpj5wp9-FLBXMp2W_n0AyrrKAcv1j27mToBihV304gqLXgse-wihbJCKSTyL8NRzC5K6ogTpr9LGn0pAw9oGZXXXkKUDwJgT322CY8bD7Qi3edpJgX-SYBlSeF1wkNm1YyYBheIfvChdsldG5FTRhyjM3XJ-GseOecBgNIL9KLuDpwC6wJs3BOs_HE9lETXTZg7urh2OYAkDnuexL8K7Y0ht_TQUUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران به سرعت در حال بازسازی زیرساخت‌های غیرنظامی خود، ذخیره سازی منابع حیاتی، پیشرفت سیستم‌های تسلیحاتی جدید، جایگزینی هزاران تله نابود شده، به کارگیری فناوری‌های نوظهور و گسترش شبکه پایگاه‌های زیرزمینی و مراکز فرماندهی و کنترل خود است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67137" target="_blank">📅 13:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67136">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک منبع آگاه:
گفت‌وگوهای فنی غیرمستقیم میان آمریکا و جمهوری اسلامی در دوحه آغاز شده است
قطر و پاکستان میانجی این مذاکرات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67136" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67135">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=no01sl3No3x0fvFWZaboTIe2jg5R7zqvdg9ofL5x21K7CeDQ1UtmZhqp3uOYiROt-pIfLoUtd23hj95mFqAcLlZimCLxGuIXXkMzgH5_KQroz0KqZX2gBGjD3V5PZ00CahT7NVd2zuFhevW74gHFt5iSpqg13BpPcqdUvB6TfyOqoaHfsvHTKaoWQRuBX4XaG8S94FbobuxPh0YKBElYaj0oSZBZ4KccfIt1vSBxSkzyRJHKBT24CD2jxoaHrNJXYxlHPJQl4OOwNZviSIYNeEUwIaLkSbsSi7L2OqHTQGAKWnRIHEGlEyZr9J4c85PkkDmm0noxqijRxh-cysnmfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=no01sl3No3x0fvFWZaboTIe2jg5R7zqvdg9ofL5x21K7CeDQ1UtmZhqp3uOYiROt-pIfLoUtd23hj95mFqAcLlZimCLxGuIXXkMzgH5_KQroz0KqZX2gBGjD3V5PZ00CahT7NVd2zuFhevW74gHFt5iSpqg13BpPcqdUvB6TfyOqoaHfsvHTKaoWQRuBX4XaG8S94FbobuxPh0YKBElYaj0oSZBZ4KccfIt1vSBxSkzyRJHKBT24CD2jxoaHrNJXYxlHPJQl4OOwNZviSIYNeEUwIaLkSbsSi7L2OqHTQGAKWnRIHEGlEyZr9J4c85PkkDmm0noxqijRxh-cysnmfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این کلیپای محرم چرا تموم نمیشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67135" target="_blank">📅 12:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2xGXFdI7Y3cwzHiwB7JP-nkWOnO_Pec4TPTpY4vgeTHEgZe__ebQGVBj9250TQreW7pzLrTZGutI2p16xHKYDbO3a0g770hmy_LW9rVPT0OF6wVJIXq3nPfDc3J33pBKW5ZghFNy9doyLA2z-iyHJr3esIcybdTt32B0Av4bHLNOPtu8zxOBaqrrKDhZ75ywBDa5xoH9mO8tE6CW9GLaChxNL6PEuZg756wl86zMvKA_u90UvqMyATykQ-uNaOKE5Feuqi7lE-zPlvFkaHlp6BO30njLED4zAy7Cwclck6LH-ZYo0oG9en6sn4zMzRRkdiek8_woVPtMtuKNUn59Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keS6jGkL6B6U22J5n8bveyscwpzTNFp_kBn9dBZ1SbFRH0zrEzWvVckz3ovdjsFBf9LakOAxrN310vIUQNiAOuaGHIYWdsrT2SHD7cfjIzwlMrhY6zAnoMnYTap53cCo2vPg0bAuZAqe2JxbmWU4aPUQGXU7-jL4jsNlaY6Vih5sTMv0RbIO-Ifdk3a3fH7SDv-qXPKjD-xHfcXjqg4kfrZfHCWvKXdav9RTIr44svnzqs-oCHekiMWPS2z9on4d8axGiiaRHlFEw8MPUOCiQf7Q_O_p2Hp1PLoWJZjnZCh2DeaBDP6yZEyOhaR_Ea64gobmW8VHExrIvoGhSG7fvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=hjOWuPkrxmEOP191dF6ez5QohKiqARhrO-MtV3q9nsmcUTu7rcFKiav6qrdXp7WmDvPLR9aT62hJEsjxduusrQs6FqkeXJaKyFASLaSwuMT6YcIcyO4FKfqm-n4CJ0Xv6VdF6BN_ZRbpM3IfCyi4ZKenqn-uhBUV9iJrno_JEwU-xWAP0XVx3t2moHp6oAUyCmNbvBXmm2BTqCnWnfmeGBTtqmFKOM6UU51xMCP_gz0oFwiIUi7vXjzDSWU9w_UzVDAHKjLVdc3YbAmQzNoH_OzgkVEtxBI1P5HoZkZcP6NhyToRii46RYKTGdNaCQZznpHvdnhO8iAW0ByiO-X05A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=hjOWuPkrxmEOP191dF6ez5QohKiqARhrO-MtV3q9nsmcUTu7rcFKiav6qrdXp7WmDvPLR9aT62hJEsjxduusrQs6FqkeXJaKyFASLaSwuMT6YcIcyO4FKfqm-n4CJ0Xv6VdF6BN_ZRbpM3IfCyi4ZKenqn-uhBUV9iJrno_JEwU-xWAP0XVx3t2moHp6oAUyCmNbvBXmm2BTqCnWnfmeGBTtqmFKOM6UU51xMCP_gz0oFwiIUi7vXjzDSWU9w_UzVDAHKjLVdc3YbAmQzNoH_OzgkVEtxBI1P5HoZkZcP6NhyToRii46RYKTGdNaCQZznpHvdnhO8iAW0ByiO-X05A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=JHDR9BmGkt-89H0E1E0VehACd_TbS9Ux8rLO321CZvkWlMyk1-VtxRKtC4L4PPsoY3atmJhpa_QcL2hT-b0yMcPp8wPJeWI6nAn9lxMFZc1SdC9YgCtlFFKIowF8OU5UqaQeJXi8ZRjTfUrU1IRMiFgrv8Wn4gNoMB1WjMUzMFd4gFYsE3bPSh59bBuJ1l_ujKWJRxIX6aDuyA9NKyU_aIuQk7820e-1nP6iM1lplL0YUaYhuA15rzwuaUsxGGlqd3Yx9_ldIvf4TimQLQ1ab_cHvRVRF6mJU6cx9wBaaEAIkBIERdFKdAweLrEKZuh8Yc4I1dZfvt9hoPbNAGVYwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=JHDR9BmGkt-89H0E1E0VehACd_TbS9Ux8rLO321CZvkWlMyk1-VtxRKtC4L4PPsoY3atmJhpa_QcL2hT-b0yMcPp8wPJeWI6nAn9lxMFZc1SdC9YgCtlFFKIowF8OU5UqaQeJXi8ZRjTfUrU1IRMiFgrv8Wn4gNoMB1WjMUzMFd4gFYsE3bPSh59bBuJ1l_ujKWJRxIX6aDuyA9NKyU_aIuQk7820e-1nP6iM1lplL0YUaYhuA15rzwuaUsxGGlqd3Yx9_ldIvf4TimQLQ1ab_cHvRVRF6mJU6cx9wBaaEAIkBIERdFKdAweLrEKZuh8Yc4I1dZfvt9hoPbNAGVYwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی
:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67129" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67128">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=iwPG1JL01CWR3IgBG7JJ17WeylKW2uI0FzcJ09I2jv02TJbntSFGJA9_9cVmN_7lo1Qthj58v_8qryS3kB4AzwG4xq_0-jp522XUP8a3xzKHu160lAP1xBIGopKsP6VCk0qG3O5RlZnqZk901rwwNFYuCgDgW4zMcJqPVXzUudScP-1jiHpDMz6ghJL9MKc5UMqEbIWrcll5oEM2sUzlnk_KD4rNeLYPHIzx_VIyWsQfl7bBQBtL_xvVvD7QMVb9mzKC1zgpEnSY3HX_JN17ByxDcnyN3meThLCF-fIcj4MuQOEwr-BlP4NvXoBOaUvsWEDlW6h3Czg5d3zAbW-BMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=iwPG1JL01CWR3IgBG7JJ17WeylKW2uI0FzcJ09I2jv02TJbntSFGJA9_9cVmN_7lo1Qthj58v_8qryS3kB4AzwG4xq_0-jp522XUP8a3xzKHu160lAP1xBIGopKsP6VCk0qG3O5RlZnqZk901rwwNFYuCgDgW4zMcJqPVXzUudScP-1jiHpDMz6ghJL9MKc5UMqEbIWrcll5oEM2sUzlnk_KD4rNeLYPHIzx_VIyWsQfl7bBQBtL_xvVvD7QMVb9mzKC1zgpEnSY3HX_JN17ByxDcnyN3meThLCF-fIcj4MuQOEwr-BlP4NvXoBOaUvsWEDlW6h3Czg5d3zAbW-BMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
سازمان انتقال خون باید خون‌های زنانه و مردانه را از هم جدا کند زیرا قاطی شدن این خون‌های نامحرم با هم در رگ‌ها موجب ازدیاد گناه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67128" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67127">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=ZL1-wCuttuft4O71_Np8JjRK5fkBJ2Nm0VLuJ6cffZvZ5y4KxAit1byr-OXv2PfxP-J-c6kpWlsT_dM_rLxHRO3r9giWGDIWgshnW_Bh3Z21nLqthrFRyYQiEmYOIBXOSMjrYa2w75uXurSVyWPCcX3LsrL9r2U0AToc_ssRAEXdAnENqJwQfNNcDC3oMtZg8x7ULRMEuo2knw9ITc5Mbcf1YlpnhmCBAPsf4PqYWjLbpO45t2ECM-qcHj0vQ5y6qCJkJk5i8khlw6eaeBpECuiwhVumUeZRCaEBg1uFF9YKsA_w1yR_S35Qq2GTiMyZQl-aFQ1xK1XNbWH22OdOtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=ZL1-wCuttuft4O71_Np8JjRK5fkBJ2Nm0VLuJ6cffZvZ5y4KxAit1byr-OXv2PfxP-J-c6kpWlsT_dM_rLxHRO3r9giWGDIWgshnW_Bh3Z21nLqthrFRyYQiEmYOIBXOSMjrYa2w75uXurSVyWPCcX3LsrL9r2U0AToc_ssRAEXdAnENqJwQfNNcDC3oMtZg8x7ULRMEuo2knw9ITc5Mbcf1YlpnhmCBAPsf4PqYWjLbpO45t2ECM-qcHj0vQ5y6qCJkJk5i8khlw6eaeBpECuiwhVumUeZRCaEBg1uFF9YKsA_w1yR_S35Qq2GTiMyZQl-aFQ1xK1XNbWH22OdOtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر ممدانی شهردار مسلمان نیویورک درباره مرگ خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67127" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67126">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=Y4U8b7yqnbim53fKRsnapCW0bY-PBGjkn1VB_UhGucKV3REcnBGbAv3O_sqljCVA97S5XpithB2C4nGfqtCB7F9SnN-nYG59v-8kbYZRTVFTJrNuitodeM2WXlNCG6MbciNEKMaSaGba3qvl9vdK8H4yUuv9DGH-LLR_wsGaMvm5rENnKsHjSPNoF1d-WkM45nJv9Oshwi-QOXoLUZgEWDON1Fftrre0u6yIaiU5rh9HH5AUltor5eTOqVPpBtSqcHk8Uy-F5Y7_80Q8tnOehVdzPCrU5FbX-6qlHkcNCrhGxVOVMyCbcPjkER56DAgb5btT_wnZ52dHry1SxwPAHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=Y4U8b7yqnbim53fKRsnapCW0bY-PBGjkn1VB_UhGucKV3REcnBGbAv3O_sqljCVA97S5XpithB2C4nGfqtCB7F9SnN-nYG59v-8kbYZRTVFTJrNuitodeM2WXlNCG6MbciNEKMaSaGba3qvl9vdK8H4yUuv9DGH-LLR_wsGaMvm5rENnKsHjSPNoF1d-WkM45nJv9Oshwi-QOXoLUZgEWDON1Fftrre0u6yIaiU5rh9HH5AUltor5eTOqVPpBtSqcHk8Uy-F5Y7_80Q8tnOehVdzPCrU5FbX-6qlHkcNCrhGxVOVMyCbcPjkER56DAgb5btT_wnZ52dHry1SxwPAHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oyoyic4pDF9vLJaThCy-OYejg2Wav5x23XMPzg0MXpAYaRf424klWhZtS4vFyQSxqCPFQvctfQXMRBlMtJZHhujN1ix09FEg8Mr0N2Oy2GSDHn8RGIoqES8ehf9W6I-I2yaHaKw1cTOCdNF_vqBe1HqL_mRTocSDnwZNELULNIuC3Bmp2bh7U_FCF9mdqS6Yx27CK0gkgNs75hoCuLh-Oo9ly0IABe9Jsh3c6tlhyZ6B5nPs4u79fmMcmAkIT8SyvvjT2nQ_aVpNLw9PPJw5lIZzs5oXbode2l9igWoVwz7I5z8Qoc5LBckRHqpnX-eDWm_6UeFrrT3i1jo0ftTT7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luhOTDh2OjzONcc2euueewgZkT0tR2cg___eoTl1G8y-177AVatfhSTjGJYUTiZ75zYvyFKCku_AEqa47UBmma9ODp5zwd0qDAyOe9arCLRKLRTOqwNIPNEq7MgOfsKDOEynTqeDs2Ev7Ku0V2k_aDR9bO_flYiWZ9gCLsEEMTdw7_oW-paWT711IEDOmdoqAf3MfrRB_0Xf-wjK5_TYM5-xnNNHWYCrZvBSSW3EQEmaUrQhBBE7x4sR4xOemVhgqAmSbczst5r_Woj0Y1d-2r170_munQR3MHq9TC2JD5Ci9wDtdhKezdr58avQEQwRMroM3N3GB5I5hq9nDWVmhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
فرماندهی مرکزی ایالات متحده:ناو آبی خاکی USS Boxer آمریکا شامل ۲۲۰۰ تفنگدار دریایی وارد منطقه خاورمیانه شد.
گروه آماده به خدمت آبی-خاکی Boxer (ARG) و یازدهمین واحد اعزامی تفنگداران دریایی در حال حاضر به عنوان بخشی از یک استقرار برنامه‌ریزی شده در خاورمیانه فعالیت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67124" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67122">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T21Obh3Lh9TKDFvnaZW3Dc3we2Gx6uFjqsdIJdO30ccXbxplR49imdpjAF3ikhMXwQiXDPpABKH-y19-ld9tj4xgOJGZqrE_Tl77QwcRN_N6dZeUe5pkPR6AxhQEyd81_XzQ_Cys2HXF0c9k8lc_PzvLgJpToIpoqVird-wtjFmVgX1GsGzK_eHBAZSiHSKcMWpYDKZ9mk0P2zneh3RFT_rPnEmdDvmneWwtfEtxPdtr-3r_w7ZqPYd7FF85anrXQ0XXw2DtZD_w229SxmFqa__7LRbcjOlq86aj1BPKz8nRSkQ7klbQh450M4hAA2uSS5DcDA_Powr-vyEQxQggcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67122" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67121">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=vGFwo5QafSftHnGOC5P3cMYmMagD2QEq5FlrpGqCmWs9oMWH__k3Qg87oH4sOqKFBiAr9vYEhY48kepzF8wZRsQ2DJexYv5Hd7gjWpGQIqZahxtHIEiuVz3QHoMjSAvcTRINojGPp-HF5-gvGm3oJc5eFBRiFoelMVViq-Wf5VdqQnXd9-pz9SW-Q10UwmHlAPuUZ9PEqdrZyRnBiz5cdkpbOhJZK2vQQDa7ugY4wPRzHQNrsZu3WnTasMF7AcX75X0ayWn3hSslRQqFzbk2fgCuqdeZq9YdZOXt8PrGb0rOgdhsarcw2oAdzWawqVM13V9uI057TOrH3ARQuO0k7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=vGFwo5QafSftHnGOC5P3cMYmMagD2QEq5FlrpGqCmWs9oMWH__k3Qg87oH4sOqKFBiAr9vYEhY48kepzF8wZRsQ2DJexYv5Hd7gjWpGQIqZahxtHIEiuVz3QHoMjSAvcTRINojGPp-HF5-gvGm3oJc5eFBRiFoelMVViq-Wf5VdqQnXd9-pz9SW-Q10UwmHlAPuUZ9PEqdrZyRnBiz5cdkpbOhJZK2vQQDa7ugY4wPRzHQNrsZu3WnTasMF7AcX75X0ayWn3hSslRQqFzbk2fgCuqdeZq9YdZOXt8PrGb0rOgdhsarcw2oAdzWawqVM13V9uI057TOrH3ARQuO0k7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
کریس رایت، وزیر انرژی ایالات متحده:
ایران هنوز به هیچ وجه همکاری نکرده است.
جریان نفت از طریق تنگه هرمز به لطف ارتش ایالات متحده است. هنوز هیچ همکاری از سوی ایران صورت نگرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Inxa9Iyu_a7jmvEoZM_lrhSQswsxyDHSD3Jy1gmF3tRX2m6-ihdOT-2oH09nMXeWzPPvjMF7MO2s8q_kGL7mseAaNiOj03GZ97mgnyaMaFG99Jjn8rnyGy5Bfb232-Bz4Xuh-PoXgQ4VyC2oVL3a6OROhedUGRBWBIFpGN6lt--TsSpxbuyvne8ofwY2Cuefh4k2b7kKsXCZtFkH5zC_dP7WSsLXkBlyQQQOYocbuudfJgQPQmcSkO0ccQPePNODWeOyDNrb1xSnYzzIpHKWJrmMepX5GE1nqdH1U28fhqVzs9f40Fa37iegPcf4Ku2bSNbk-sIyan8V2Sr3gHKiIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67119">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=qJbE-NUgMTFlBY3Qq_NkdEMyA4ukurmiJ5ewd0q3n2Pp-EdvL8urEoZVFZcvxFugW3BWmV5GxdlniMhe7LhOUHZ-_zabjdk0T0UqItk_KEAK3r6QIqa4UxnB3UtUn02KrKt0pzi-EXJAE8R8iyQbdCfsFjJO_1JkG7xiuSgEYbkVRgJ-EmfqfuShp49Woz46CWclRvF4j-KS7CMOQGt3cil4TMOssFjA_7Xf_RDxbpBMJLx9QZmBc3ymMSWDP5rPIkDh96Eqi6cEOe1bWcUB-G7KnTz52aBFskdPes7iTV4eN8kClXCh0LeS7BLLHKXAH8BVLZ3ZY1dMf8ofux5seQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=qJbE-NUgMTFlBY3Qq_NkdEMyA4ukurmiJ5ewd0q3n2Pp-EdvL8urEoZVFZcvxFugW3BWmV5GxdlniMhe7LhOUHZ-_zabjdk0T0UqItk_KEAK3r6QIqa4UxnB3UtUn02KrKt0pzi-EXJAE8R8iyQbdCfsFjJO_1JkG7xiuSgEYbkVRgJ-EmfqfuShp49Woz46CWclRvF4j-KS7CMOQGt3cil4TMOssFjA_7Xf_RDxbpBMJLx9QZmBc3ymMSWDP5rPIkDh96Eqi6cEOe1bWcUB-G7KnTz52aBFskdPes7iTV4eN8kClXCh0LeS7BLLHKXAH8BVLZ3ZY1dMf8ofux5seQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بخش سانسور شده صحبت‌های قالیباف در صداوسیما:
قالیباف در قسمت پخش نشده این سوال، می پرسد: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوفک صادرات نفت انجام می‌شود.
​
🔴
این قدرت جمهوری اسلامی است به آن افتخار کنید و پای آن بایستید. این سند شکست آمریکاست و ما با عزت آن را انجام دادیم.
​
🔴
گویا حداقل ۲۰دقیقه از این مصاحبه پخش نشده که نکات مهمی را در خود داشته است.
​
🔴
برخی قطع صحبت رییس مجلس را با بازگشت روزی‌طلب به معاونت سیاسی مرتبط می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67119" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67118">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=HQONhDcIjv4ZUgxBUMWP0N9lmGP3BpSWKU1hu1Am0hjyajkLqaTy-qXVsMl8IeNDj0TppvzdbEm9H778R2Y9OPVrvj_NlZHmU5lx4AaJwfgKwQ51gVukxBDl1fWOqVE81AxdNh60Ij8OA9wY0eEJ_RfwsWjFCh4PpvpvXY_CJC5y98EKfhvvnfGMSYMIS32qReNf-MG188Sh0TVk-F8wp7XVk4JXIu9Z0D21bp8Ty9eEg7Z8ZGR1AfInhtM2g-YbtKe_RPJr6lbNQVj2dXLVq9U8MHYj_MUeqct0rvJvJjsjnOJw9-iDJ0KP1TIkZHVM1flzpcjGjuiTIZc0WgUY7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=HQONhDcIjv4ZUgxBUMWP0N9lmGP3BpSWKU1hu1Am0hjyajkLqaTy-qXVsMl8IeNDj0TppvzdbEm9H778R2Y9OPVrvj_NlZHmU5lx4AaJwfgKwQ51gVukxBDl1fWOqVE81AxdNh60Ij8OA9wY0eEJ_RfwsWjFCh4PpvpvXY_CJC5y98EKfhvvnfGMSYMIS32qReNf-MG188Sh0TVk-F8wp7XVk4JXIu9Z0D21bp8Ty9eEg7Z8ZGR1AfInhtM2g-YbtKe_RPJr6lbNQVj2dXLVq9U8MHYj_MUeqct0rvJvJjsjnOJw9-iDJ0KP1TIkZHVM1flzpcjGjuiTIZc0WgUY7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پول های بلوکه شده برای دولت سیزدهم بوده است، مصاحبه اش در صداوسیما قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67118" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67117">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640225b559.mp4?token=YeA66VMXvjgoNKAUXcYOwLnYAKi0CmjbnuCsHEAnMndIVLKIZa9GwAee0cISLipsHNEyedtWSvHef84WBKRypYrfB8XQbhRWo05_OPq74tu3CJwR8jCfM0NOkBDjNKvsAXjgdsSchTsm_xNlurssS5n-8WKxrzMXy5gWKMwIdogpiQWD0G2uTEsfvrVxdCB_t7c1izoE-JGXzg7h6OPBxucGTfY5P59zPnl9jmAaHSQjV43GgJ5VRA3JnLVhY3Z7h6uthPRqfxPfjF5FGPpUemfYlOviyLLIX2ZjZ6ndZfTYkq0fUyvTJoMvb0FbvzKzORrxaMmRJeL3F1sc0zD_ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640225b559.mp4?token=YeA66VMXvjgoNKAUXcYOwLnYAKi0CmjbnuCsHEAnMndIVLKIZa9GwAee0cISLipsHNEyedtWSvHef84WBKRypYrfB8XQbhRWo05_OPq74tu3CJwR8jCfM0NOkBDjNKvsAXjgdsSchTsm_xNlurssS5n-8WKxrzMXy5gWKMwIdogpiQWD0G2uTEsfvrVxdCB_t7c1izoE-JGXzg7h6OPBxucGTfY5P59zPnl9jmAaHSQjV43GgJ5VRA3JnLVhY3Z7h6uthPRqfxPfjF5FGPpUemfYlOviyLLIX2ZjZ6ndZfTYkq0fUyvTJoMvb0FbvzKzORrxaMmRJeL3F1sc0zD_ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظه قطع شدن گفتگوی محمد باقر قالیباف، توسط صدا و سیما
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67117" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67116">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=VOeJorW4p4sug3xOmlad3hKgxKtKLcG7rxz0w_1wwOIBhh7F-ApgRzJM9lWbJpzGypmqvwiqUQrmclDOVILKniVlIDI7ufdr38PbcYUaq7yN0Ea_JzjhCR8HvYsr_caydt2_DizPU3qA8Y9Ug9aJXe85MnLQZiccBfQB39g3nOVDc8zy53vd4IIfIehyGVKdZqpYb3kP0ThQlvVEbSHX8t1G5YUeTitUTZRLRLKOpGnYgmCE5bOLOtSmq4pxqg6ZMaWgPBuzsY5EGneqox2pfO77MabF-VY-bJMLP0IUYhzzHai7z4_9dNbEGZd99pngBmfP9G4FXoZlhNxvxuDpsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=VOeJorW4p4sug3xOmlad3hKgxKtKLcG7rxz0w_1wwOIBhh7F-ApgRzJM9lWbJpzGypmqvwiqUQrmclDOVILKniVlIDI7ufdr38PbcYUaq7yN0Ea_JzjhCR8HvYsr_caydt2_DizPU3qA8Y9Ug9aJXe85MnLQZiccBfQB39g3nOVDc8zy53vd4IIfIehyGVKdZqpYb3kP0ThQlvVEbSHX8t1G5YUeTitUTZRLRLKOpGnYgmCE5bOLOtSmq4pxqg6ZMaWgPBuzsY5EGneqox2pfO77MabF-VY-bJMLP0IUYhzzHai7z4_9dNbEGZd99pngBmfP9G4FXoZlhNxvxuDpsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
این خانم، عالیه نصیف از چهره های وابسته به رژیم جمهوری اسلامی، شش دوره بدون وقفه نماینده پارلمان عراق است، او در رقابت‌های پارلمانی چند ماه پیش گفت: «کاری می‌کنیم فاسدان از پنجره فرار کنند». حالا خودش به دلیل فساد کلان دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67115">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=EBdEJnIMlUr9bbtC1bCwUwNIEuO3p4ZisN_theBC2I1XQNAJ1fWPKsM6sg7v10iBEjH2S624BNmQULzRtfd5-UELUzdBvkWez6CgBEpFUMnuJdcWre6xoEfI6cvzHCqfdly7mXyU3ojTMTXVNMRk4m2JFTEcIQjVWXN9V1_Sjfiw4FHqegvP0yahWXKh1AsGmE-6YYZaM52nNDGYiyBtcp2gXd9Z4xEaPqZ-o6NJdJQQlQKfeFzC7-h-MZahw4bXeKRNiTBWepxTq_8VCEjuwWzeRjxYS3bKHmckAMNNZA0OsRvvNYmNXXUnGud0rruwhsjyVQ681KXHAI5x63O4Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=EBdEJnIMlUr9bbtC1bCwUwNIEuO3p4ZisN_theBC2I1XQNAJ1fWPKsM6sg7v10iBEjH2S624BNmQULzRtfd5-UELUzdBvkWez6CgBEpFUMnuJdcWre6xoEfI6cvzHCqfdly7mXyU3ojTMTXVNMRk4m2JFTEcIQjVWXN9V1_Sjfiw4FHqegvP0yahWXKh1AsGmE-6YYZaM52nNDGYiyBtcp2gXd9Z4xEaPqZ-o6NJdJQQlQKfeFzC7-h-MZahw4bXeKRNiTBWepxTq_8VCEjuwWzeRjxYS3bKHmckAMNNZA0OsRvvNYmNXXUnGud0rruwhsjyVQ681KXHAI5x63O4Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYL9v5z0xB8s5qrZ3EINW-jTl1cHdtXAmQLqv0wE83yxKmR7Xyx1AMcc6FsyEzUJM3p634qT2a0Kcwo3hd5sN4TmvaPlWVuf388N-667lDe7u4b86V5w_wuXS9vzoaiEXFj_RQfjwMmuRE3I5Y0yA8Pz2N4Wh4EQIyNARRRys3VFzr_oYMvRLL5a-wItNWgO57iWw6MDiJj2nGUCcLw04qqU_Ebtrmd9w2T0QKc7g5BT9BBW_8pT3THbB5KGtAkxkFuvHMvuRZzDWwsZIKziNVqI1vQYXkkb-7DHqt-wyF3_yK9r5SVUij1RTQWOKORKhdsHmM7CfBNR2asXBAeStQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
جدیدترین روش ترک اعتیاد  گیاهی
بدون درد، بدون خماری، با انگیزه‌ای نو برای زندگی
🌟
✅
ترک فقط در ۵ روز
✅
درمان کاملاً طبیعی
✅
بدون داروهای شیمیایی
✅
بدون بازگشت
✅
همراه با پشتیبانی روانی و انگیزشی
💚
بازگشت به آرامش، بازگشت به خود واقعی‌ات
💪
تو می‌تونی! ما کنارت هستیم تا دوباره بدرخشی…
♦️
جهت مشاوررایگان فرم زیررا پر کنید
👇🏻
https://app.epoll.ir/74570725
عدد 6 را به شماره زیر ارسال کنید
👇🏻
🆔
@Sahar77631
☎️
09923413672</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67114" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67113">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSYwLdf5YY4YpY7XXvFWv1Xc_qi4ax-CpE_mpCoQZ-LoIyg-M1RCZDFqZled6O5YK4AGl1ybQMB-ghs0EHQokOKfhnHL_c0qWQs1pcw1cmHE6wS83-C7lAJ2V14c0Ux6J1nyu48s90XJwtkwODVE-GEyb6uphnQRtyxOmew7IIFQzSdzg2NgC5yc7fphPmDUEnemue8rlyHMMX4JmDxJXEKARe64rbf-jIxxi2MXx4D9LUJMQRn6CHG3i2M006yDvv8N56AzyFPYfKMwgVos3fDEDmXU4MMsITjR8_8CyWNdxEg_1Xx0G6nVrZ5MxQ9dFTmaD3Bi5v4h4VYRrJYSsDCZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSYwLdf5YY4YpY7XXvFWv1Xc_qi4ax-CpE_mpCoQZ-LoIyg-M1RCZDFqZled6O5YK4AGl1ybQMB-ghs0EHQokOKfhnHL_c0qWQs1pcw1cmHE6wS83-C7lAJ2V14c0Ux6J1nyu48s90XJwtkwODVE-GEyb6uphnQRtyxOmew7IIFQzSdzg2NgC5yc7fphPmDUEnemue8rlyHMMX4JmDxJXEKARe64rbf-jIxxi2MXx4D9LUJMQRn6CHG3i2M006yDvv8N56AzyFPYfKMwgVos3fDEDmXU4MMsITjR8_8CyWNdxEg_1Xx0G6nVrZ5MxQ9dFTmaD3Bi5v4h4VYRrJYSsDCZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحاتی روسیه در ولگوگراد اصابت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67112">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=oHQWy2uanP4HYzKW8UZ2EPfG1jqJHstn3CNlFKKbkE7P1rgeiLHOdaLlwz-hgC4-VgX7w7vz3UACJeJDeG8NneZ8I5KI1FT6MxJFL9-xuIDGiQqX6tYf6POG4XgD-ZUW-NOlysL4IwHZleTyFfTVXdZVXnrLJXjw0lwueOvX4XlkZtADDVURxVeFjCYV6phsVZtuQl24Wru5DDs2p9eaDaG6Oq8yHJggfeUSTzF_Cy1UuxxOeCRdw9vHle0xDj4nakCHY_jRH-LW6z214BmaBaFj90TzTOZuxiV7JShT3_AYdENW_DpLL8wBBO-n5Lq9WpeoidspMTF_LbJN8jRonw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=oHQWy2uanP4HYzKW8UZ2EPfG1jqJHstn3CNlFKKbkE7P1rgeiLHOdaLlwz-hgC4-VgX7w7vz3UACJeJDeG8NneZ8I5KI1FT6MxJFL9-xuIDGiQqX6tYf6POG4XgD-ZUW-NOlysL4IwHZleTyFfTVXdZVXnrLJXjw0lwueOvX4XlkZtADDVURxVeFjCYV6phsVZtuQl24Wru5DDs2p9eaDaG6Oq8yHJggfeUSTzF_Cy1UuxxOeCRdw9vHle0xDj4nakCHY_jRH-LW6z214BmaBaFj90TzTOZuxiV7JShT3_AYdENW_DpLL8wBBO-n5Lq9WpeoidspMTF_LbJN8jRonw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازدید بنیامین نتانیاهو از منطقه امنیتی در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67111">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=l6IRFzDrohZQl1I_RlP-dJ4KmBbhroxab6RTJIkrcoJBaWLEos-xhkK_aWN5Lq3BV_e_SVaSm32MsPLR5XGWN7nJlFsWgvPN-aYxz_TYw3-4NWeael82piWX68X_gdzCDZ_stPPmPs7_bvTjuY7R37A6IxIhEcxIvUV908JE08pbhbf79Gpr0_YhhGT05PPvCDMe0nrkOgLgC6mquc_olXJUr7IZUsL27iXXYiQRR2j-FhxgRep2zLmncaBkD0FTjZNyPZ2qZpALkr6JYJnACEDqKE8LAy0MrLPG_tL6wVnwb1LAbhrOGYCGxoNOwtKdzRnp211xvBVGXpDRxuhp7oPXZIcrmNb16GtkwxdhXIZ1Dw51vKcePYN1R6NsTW0x3JQwaJkN7PC2od6Z_-JK8KkF30of8v9W47isDYNZensjbrA9u_zs4m2biR2tNt151ZyyLCrsiDONmEGnhWRv-l_aZPZS075sAiIqa5759pSmYgYg2nN9ywt5lMumy7cQhalGsFYL2giizxCL1vcrPhrr2Eb6uIRzfBkW-TuJvuYhUQf9ct7xznRNl3QwNAeh6JM4HLkzGceO3-n5uqDxp49VdhXDwnvdJllnwJUwBsWe3B2Pch3SnwbHigPlIVRkl3CT9Znojvgok7jJY2LDpXcls63fGSFx_ciYeWKJfVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=l6IRFzDrohZQl1I_RlP-dJ4KmBbhroxab6RTJIkrcoJBaWLEos-xhkK_aWN5Lq3BV_e_SVaSm32MsPLR5XGWN7nJlFsWgvPN-aYxz_TYw3-4NWeael82piWX68X_gdzCDZ_stPPmPs7_bvTjuY7R37A6IxIhEcxIvUV908JE08pbhbf79Gpr0_YhhGT05PPvCDMe0nrkOgLgC6mquc_olXJUr7IZUsL27iXXYiQRR2j-FhxgRep2zLmncaBkD0FTjZNyPZ2qZpALkr6JYJnACEDqKE8LAy0MrLPG_tL6wVnwb1LAbhrOGYCGxoNOwtKdzRnp211xvBVGXpDRxuhp7oPXZIcrmNb16GtkwxdhXIZ1Dw51vKcePYN1R6NsTW0x3JQwaJkN7PC2od6Z_-JK8KkF30of8v9W47isDYNZensjbrA9u_zs4m2biR2tNt151ZyyLCrsiDONmEGnhWRv-l_aZPZS075sAiIqa5759pSmYgYg2nN9ywt5lMumy7cQhalGsFYL2giizxCL1vcrPhrr2Eb6uIRzfBkW-TuJvuYhUQf9ct7xznRNl3QwNAeh6JM4HLkzGceO3-n5uqDxp49VdhXDwnvdJllnwJUwBsWe3B2Pch3SnwbHigPlIVRkl3CT9Znojvgok7jJY2LDpXcls63fGSFx_ciYeWKJfVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف: اگر می‌توان گره ای را با دست باز کرد چرا با دندان باز کنیم؟
🔴
کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد.
🔴
ما در شرایطی با جنگ و آتش اقدامات تلافی جویانه ای را علیه رژیم انجام داده ایم.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67110">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c10065584.mp4?token=ABzqqUNuKWb28rFfgL5o26VppBqXg8BePQdmVK9EZlC2Nh5ok0ci6eqIE-ES4anmihNcD5kIOUR7SDU-GlwRGmQHc_NmfSvddbYxy3ZRc7Q21mfUZbXnX9ETcj4GWRDWgmU-39cxEJlnoC7xmOMllm6JRJLM-oiP8HI8JP3lhfZzOOZllZtE8-flqLhTVzRxDJAXePah3euAaOQEtmVjHCATJ5KNItehv5OXumQIvdlR2TqL0hyRtZcrEZuZgCNOW2Pa3qOQLmIF3rcTwFeQVq1IdGpndeAA_Iq-QFg15izcBee0T1o8NYE_RwIrDqpYtOzIw1GGf-nVfikvy2Bg8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c10065584.mp4?token=ABzqqUNuKWb28rFfgL5o26VppBqXg8BePQdmVK9EZlC2Nh5ok0ci6eqIE-ES4anmihNcD5kIOUR7SDU-GlwRGmQHc_NmfSvddbYxy3ZRc7Q21mfUZbXnX9ETcj4GWRDWgmU-39cxEJlnoC7xmOMllm6JRJLM-oiP8HI8JP3lhfZzOOZllZtE8-flqLhTVzRxDJAXePah3euAaOQEtmVjHCATJ5KNItehv5OXumQIvdlR2TqL0hyRtZcrEZuZgCNOW2Pa3qOQLmIF3rcTwFeQVq1IdGpndeAA_Iq-QFg15izcBee0T1o8NYE_RwIrDqpYtOzIw1GGf-nVfikvy2Bg8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
تعهد ما نسبت به باز کردن تنگه هرمز و ادامه مذاکرات منوط به پایان جنگ در لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67110" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67109">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
قالیباف:
غنی‌سازی حق ماست و خط قرمز ما در این زمینه مشخصه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67109" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67108">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=NREYnkuov1y4yiI27WKms75T7lJSFqm-GMoZMlOyDCLgCd_OPorgaw-Pdelx55QIUfLbKUETd8FBnf0NQloyyWFlDOd3Qo1EVxeOPC9pdp-gXm8nA4Xdz9qDkgBNO16r8DMwXGACfBsilEPs-uyQrDZsmSgsK_6ZCxfGuuETOpZO0zY82vntzIVJEDC82sDTSYheixcdaL8d3XXaQuGQR4Hc_5pfzdKl_-pFhV0LjqaQwNAjqS3YzA7ZQt7-AmsS47VH6ogU6gs2lXaJb6wvWEVNi_nIwNbfSXsOmiugPA-gXuG7SHxc1-7jRXSHofmzzs_F8busypuZ3GSl3DmD6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=NREYnkuov1y4yiI27WKms75T7lJSFqm-GMoZMlOyDCLgCd_OPorgaw-Pdelx55QIUfLbKUETd8FBnf0NQloyyWFlDOd3Qo1EVxeOPC9pdp-gXm8nA4Xdz9qDkgBNO16r8DMwXGACfBsilEPs-uyQrDZsmSgsK_6ZCxfGuuETOpZO0zY82vntzIVJEDC82sDTSYheixcdaL8d3XXaQuGQR4Hc_5pfzdKl_-pFhV0LjqaQwNAjqS3YzA7ZQt7-AmsS47VH6ogU6gs2lXaJb6wvWEVNi_nIwNbfSXsOmiugPA-gXuG7SHxc1-7jRXSHofmzzs_F8busypuZ3GSl3DmD6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم.
🔴
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش بس می‌دانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67108" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67107">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=hZQ6hNI0YMAu28RuoDkkhttkxyzGHYg0t9I-wy2iBjnVvQNAMI-Sp5zVpyeeok3ihCWrGO__xX-mnGjB1Ju8eibg0uOnWxWfjGabKotnBUO8Uv5gL_NJ0ivho4kBRsWeMPTawtEN8ZKgq_DSt7Orb9bbuXTuEafAZIfd8104JW6S170JllP_HYfQA_X4zapzKdxQE1nlWa2zQDYUVjt1LI8zIKJ3errvlJ1C9glxGAmu9LCSOa7BaCiMXico4k9OSRh_YboDsup5BvbSV8T65bgPhO_PI5cUMlnnHnlQKJZGDR7w2JMqw4JK4osMs1JJcs6XWEC07FZTgpdmW6_Bpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=hZQ6hNI0YMAu28RuoDkkhttkxyzGHYg0t9I-wy2iBjnVvQNAMI-Sp5zVpyeeok3ihCWrGO__xX-mnGjB1Ju8eibg0uOnWxWfjGabKotnBUO8Uv5gL_NJ0ivho4kBRsWeMPTawtEN8ZKgq_DSt7Orb9bbuXTuEafAZIfd8104JW6S170JllP_HYfQA_X4zapzKdxQE1nlWa2zQDYUVjt1LI8zIKJ3errvlJ1C9glxGAmu9LCSOa7BaCiMXico4k9OSRh_YboDsup5BvbSV8T65bgPhO_PI5cUMlnnHnlQKJZGDR7w2JMqw4JK4osMs1JJcs6XWEC07FZTgpdmW6_Bpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
دو اقدامی که پس از امضای تفاهم‌نامه، در شامگاه ۲۴ خرداد رخ داد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود که از اتفاقات مهم تفاهم‌نامه به شمار می‌رود.
ما در حال دنبال کردن دوران گفت‌وگو برای تحقق ماده ۱۳ تفاهم‌نامه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67107" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67105">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SpVkAdJl3QiLlH83PiyamO-q0p8BvFaMtkO4Rnu5zkJVnAFublVRA09irTTCiAzPReriI9obFMmL8fjFV30rmfMbIfoEhMTxEU_WUWXD1BiI9xQsfHoINZ1poW_920E9QUGtezb1z--zcDZ3s-gcrASjgVeOA7nqWN1zjh7_Th4abLvIsC0aGMDGLK3sKSvFA9g3B42JFPWULZrATlXxQKSFnMsuf32yZ9UQ1pyBbJ7wAh4dyor7uGq7vlVR0XhyNwRoTO0ova7ET6DteM8tGiLk-gi7kBT9ENsTkU8CzucfGcTPUFQkbzKjkpmWTROfjZYCDbtO9HO_i_1PbVbuFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F9M5E8uE7hcFQC1S1d_euUmPSZztMCSQEKAZ9YJDPRfP2DvjMAK6f43-9xVoKtvRsKAUA8dYyx6CuYccWR0pvohjwiAGzyW7Zp4yMue9_NhnGyFG1hvH6TERAP0VjedBIa-OBH4oMLyoXc5AuXAdSU_PS5X7glPHEwb7sCP1F7wfX_g-nKvjxhmkbD1ZgVvazwkTRLl99R2KaHANrg-IsM-VVGZaiF0dLJlbHh9qL_XRfgy3Ph_LUD96xrmZMJrE0P7-rSyDfVpzYo2hcnI84PQXxKzvXFDegBtKGjYhl0FNK4jJx8cSlP3i-hNmHK5LwCJHpbzDp85H0tv2f9EwHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صفحه اسرائیل به فارسی:
چرا هر کجا این تصاویر به دیوار است، دزدی و فساد هم هست؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67105" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67104">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kd8ztYu4dHZK8662llp6OU4UyqgmvdvTcha0qrrU-_SCfpVD7INYrI4mqyucHy06D21AaeRL8Ti2xsOI3AV8CZs-CNwHnhmbbLPzZsr-P_BUvGqf_ksg5o0qUJ9wOsNVwENnQW_DP4yYWb_O32gHR5lcACUNzBI98o-j_YB5_JrcdNLN69n11xYPG3YJA1sf4bcQmGJlc13rb6GNYRtmBMAy-ti59QKqwxZl9nGE_zIiFGJglmPGxWD9HF8cQurQ6KVLlVsexvlllhmySJNzE62k2LxE8jWnW-cW0wt-ce5gUmV-SzaDlBjswzR6sZB3CPcP5Shwp7hfCxs2x3_GfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وال استریت ژورنال:
اختلاف نظر میان میانه‌روها و تندروهای ایران بر سر اهدافشان در مذاکرات با آمریکا، پیشرفت آنها را کند کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67104" target="_blank">📅 21:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67101">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GLaW7vxeWdqek5bM5VOBMr-oTLe90jD_6Zvn2w5cjfDwTqkGhfJnW0z82rD0pkLfsV52SrV9be1e_W5g0IKIbIh-rninN2B413cRIB89fUXcA81ZMNMzSEMdG75s36tu6paY3_dFNaVYuRkrGkt7uOwqv8zqX27ZU7kXy3rRNUGAmTG-StrvWqTR4sJLtlCxRDeWnnknYvEAoI_I5YA9uZjJGv3yeSZDCOgSa4BWVWAti8sIo0PLT8pn3f7NIxAgsuxtzsMDYgAYV283IaAyepajUMm4HEAehdLYfv5FFVHUipFUcDQCqznimfGBdOmgsWQoAvuYRq2klZJyO995yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-73hm_A93aHWO_HfexxjhNF1l2E-6yf1kgywMaKlD-0fIaRfSq5fEL3c9ispz9gFkinvhJmIDpTPKEQkuQB9kSbM48aW2tjIP88ARnCIYp9LdSWTTikcVRbOyGyk_HFYYUwIo1JArmpt7T0mPbaDSbt1nDgIvl4rKYioNCd48UvzM9crJdNr7zxfSmCvXXSijHv1-SOepYHZkmctP9SVIDnIUmD76Ke4-tNhyJPtWteajZ9JLRta7UnoG2pmZ7qm0OfOKLJuILH4T8yiXXibfy6dPaD1foPADYwWrZpgnVWCuSPNRIsDW98iu5Bt94zTJ1tgiYQWROsLWXhZIEftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AfKprmbTT6EuImVQ56ajwIoUDftJjlO3p8DhVEfiyoSwvMP2tE3I1YqwBFBuIs2JOXktO7kQmuX-PLmmJQjY27LUrhs4BrfQ91uje1u-f6wYTKyic_APoeD2eVZAhYBVllUvathPQiPScJN9LTcEQ-_7O6z4xu0_dXasj8zleScbdiMxrIlkImSR_NC-lJFZiS1Q4KrBqRMFtbcDRVvqyiUvOdt2rloph2uxHIgnr0Wp-9SLp8JLK-UG2ENud2NV37KQkmPAboN7N2GyCHOYwxbnoCDzdW2JwmP5yJl9ibeLot63PkSeTJHrmpRjL7j1UK0abnEVLCDH_eAEm1AdDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سنتکام تصاویری از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67101" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67100">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=SXs7JZ9I9abHcCFtPD5eRADJ6aXP3zPVhJEUe7vetG_i5xUXcigLqZwb1qOx9CxfhrAQ7zMbM9xb-bF99_ERR4l_9LmGW6NsHtWLlY0jXgn3m6L6FnjFX3Rs2Phnti9-bKSFzUXJm2TEKPuXhgp-YHhSKdLEZhoXvXteacNDHDyW2IpAg_dLFbzRYn23_R4Ackz4N5z1cWe3Q-zfXicJKtOyCt45WB3Lz7Iahbr5i9ykUFMHSsT44FSslduSe102B1ljIDJW89UI05o9o1VaoO3zYcyD5xTLf8ZpRXPHw9mT7XQDplswtShaTwHgs0nDC9ES_RUXPHjOSNkQ9oKKJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=SXs7JZ9I9abHcCFtPD5eRADJ6aXP3zPVhJEUe7vetG_i5xUXcigLqZwb1qOx9CxfhrAQ7zMbM9xb-bF99_ERR4l_9LmGW6NsHtWLlY0jXgn3m6L6FnjFX3Rs2Phnti9-bKSFzUXJm2TEKPuXhgp-YHhSKdLEZhoXvXteacNDHDyW2IpAg_dLFbzRYn23_R4Ackz4N5z1cWe3Q-zfXicJKtOyCt45WB3Lz7Iahbr5i9ykUFMHSsT44FSslduSe102B1ljIDJW89UI05o9o1VaoO3zYcyD5xTLf8ZpRXPHw9mT7XQDplswtShaTwHgs0nDC9ES_RUXPHjOSNkQ9oKKJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با مدیر داخلی بهشت
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67100" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67099">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=tkyGbfagG3AoRTQfnxrB10ynxnOp6wVwiZ4IiHH0Fn9086bEbezjglsNhtsOmEPrKJzpPyDyLtbG3WMI_mGImvRtIqvGDvzLddtpoiB8GabUgrCZ_u4pi8VrxALCgd5OKsi6H1ShG3yW7uX8oFhHHTo-Pk4qAvQhrpF9Wieh-8SugoLZDi-q06QrkcIFe8rZkoh3_o3LSUxcOQQMsNvRAR2TfkInEzS2ueickKj0dNTWKMOUjnaVsFXKOBSWFc4L-MN9R3ZNXqWFvg5qIHGUuXVZd9l15fsfYfvB7CAyQfCygp4leiw6pCtmaNs7GrasTVwPI3msSbdECD6BQqs8AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=tkyGbfagG3AoRTQfnxrB10ynxnOp6wVwiZ4IiHH0Fn9086bEbezjglsNhtsOmEPrKJzpPyDyLtbG3WMI_mGImvRtIqvGDvzLddtpoiB8GabUgrCZ_u4pi8VrxALCgd5OKsi6H1ShG3yW7uX8oFhHHTo-Pk4qAvQhrpF9Wieh-8SugoLZDi-q06QrkcIFe8rZkoh3_o3LSUxcOQQMsNvRAR2TfkInEzS2ueickKj0dNTWKMOUjnaVsFXKOBSWFc4L-MN9R3ZNXqWFvg5qIHGUuXVZd9l15fsfYfvB7CAyQfCygp4leiw6pCtmaNs7GrasTVwPI3msSbdECD6BQqs8AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏در فضای مجازی این ویدیو به عنوان لحظه‌ی ترور خالد خالدی نیروی جمهوری اسلامی در پاوه منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67099" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67098">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qj1Up29scGpLnEGQSGuE8MyOWFHISi2lDte9q1rWkDxXfsydVnLW28qJFNtolEOBP5ujP_JOpsNWQAhPvJWeZJLPJxPCIRFN1IqyZLShMrJFIUXfFUNbySGeDbFwNnBaiplabpJjk_SbjrD7uu-kwW75M8OiJTZrIIgdt73UxRBMM18PjnPNJ6ijtYTiB9DNaXaTNIgqbNBYRKBloXrlpo3r5YdnLutYBZU0Lt-9ZvP4lr5Sb30Hg27pbsDiNv2bXykhjjAdQDZxAYQDPjkeYwFamDK5FmSOCvE_J5zCiH7rLJC07QbA9uyxxEMe9cOq6i_bZPb5YlM3pEKUL7lyxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علی حسین قاضی زاده تحلیلگر اینترنشنال:
‏ایران اینترنشنال نسخه‌ای از دستورالعمل محرمانه شورای عالی امنیت ملی را مشاهده کرده است که از مدیران رسانه‌ها می‌خواهد طی ۴۸ ساعت منتهی به آغاز مراسم تشییع جنازه علی خامنه‌ای اخبار مرتبط با مذاکرات و توافق را از اولویت پوشش خارج کنند و بر پوشش مراسم متمرکز شوند.
ساده اینکه از بازماندگان نظام می‌خواهد که چند روز تکه‌تکه‌ کردن یکدیگر برای تصاحب حکومت را رها کنند و به چال کردن رهبر ملعون‌شان مشغول شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67098" target="_blank">📅 19:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67097">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9uvLcOqIsr-tmb49ktlguqMSv2kqelO5MKATgPS3UnVrAElKzhEHz_y3nutYNNcUuo8BO7ahNt3wbT7F_hT65-4OqCBhcKw2xhN2jFuA5J0gsp8C6B1C-CN9J3L5_zfwCbAP5QLKQi5jdGzNmRio5TZ0nFtmYYndPHb2x819ZxFFWrqAoZJeAcaU5yqFwI9Jqm7FU32E9HhGrquLg1OmhScMtnzU_KyxY072JBThCrV_98CpnEth-nZr-5CjlvR-TDzBG-kMqiQjOrwIuVMquNzz3uJ4Qu-xrKNIfSp9BxPsYswOUgRFYgKUo-Me2dNP_mWC3fVwwx4tN9omvzacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ناو آبی خاکی «یو‌اس‌اس باکسر» آمریکا در حال نزدیک شدن به منطقه
🔴
بر اساس گزارش‌های منتشرشده، ناو آبی خاکی «یو‌اس‌اس باکسر» نیروی دریایی آمریکا در حال نزدیک شدن به منطقه خلیج فارس و آب‌های پیرامون رژیم جمهوری اسلامی است. تاکنون مقام‌های آمریکایی جزئیات بیشتری درباره ماموریت یا مقصد نهایی این شناور نظامی منتشر نکرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67097" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67096">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=m-RANSJ83J_igPGgCHv-oyJS3abbys5lJy4ogkJObXYqsOf7dIujEpUCgfTTYbkUjkXbGH2aXs9aiHenoD8QQ6SDr3Re9UA_ZxeVBa3HOProYONLz5aOcs9oyg32l2Dm5QXwbnieBEHgHxSIUHjt_PHKpHqdIGSoswRpITYo8NkaNA7wPUni43bDYJ3iGrOrhJ7atNBnsesbOr80Q-hPCQWEiIb0nKkrSzIF6sIjdbE6-bRlLb3gB-0TyIV7acHUfP87QADjojlJDLXYgL6BOMppwhjiuytY08_X73FuvGbkEwheAuFsFb0yDW8OA-ar6ba3XMlKzGSQ_Yx4txnnLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=m-RANSJ83J_igPGgCHv-oyJS3abbys5lJy4ogkJObXYqsOf7dIujEpUCgfTTYbkUjkXbGH2aXs9aiHenoD8QQ6SDr3Re9UA_ZxeVBa3HOProYONLz5aOcs9oyg32l2Dm5QXwbnieBEHgHxSIUHjt_PHKpHqdIGSoswRpITYo8NkaNA7wPUni43bDYJ3iGrOrhJ7atNBnsesbOr80Q-hPCQWEiIb0nKkrSzIF6sIjdbE6-bRlLb3gB-0TyIV7acHUfP87QADjojlJDLXYgL6BOMppwhjiuytY08_X73FuvGbkEwheAuFsFb0yDW8OA-ar6ba3XMlKzGSQ_Yx4txnnLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
مارکو روبیو:
تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود،
اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛
متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67096" target="_blank">📅 18:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=Xxra8KjncunNfyLArxbk587pjbwmVU8bxL7dlHGci2rm-6zxMxBpNQRQLScxGgvOXnTu5zt-i5XohEeMVYEo5HuUfvXVjzPBipseK_4Dnd08XVIk8CzB6TDxNOdQ2G16LIlILmanFsqNEZDCSG3BLi50AYgxkrFCKVJAbusGvHJVcqzEFpr1AdfbPigOOcgRyduv0YhqS7Eer0zCAINVMQfeza0506HlpZYHRopl6siHtWMCTrq4audJnoCqcb70fE1n3DL6KnXYZm1pQSAx9u3_B4oaPSx4FTFyaOxe8UmsbnzWUzMXqwM10BlpbQ6GrekVExpZLVzsZH5dXPJ4qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=Xxra8KjncunNfyLArxbk587pjbwmVU8bxL7dlHGci2rm-6zxMxBpNQRQLScxGgvOXnTu5zt-i5XohEeMVYEo5HuUfvXVjzPBipseK_4Dnd08XVIk8CzB6TDxNOdQ2G16LIlILmanFsqNEZDCSG3BLi50AYgxkrFCKVJAbusGvHJVcqzEFpr1AdfbPigOOcgRyduv0YhqS7Eer0zCAINVMQfeza0506HlpZYHRopl6siHtWMCTrq4audJnoCqcb70fE1n3DL6KnXYZm1pQSAx9u3_B4oaPSx4FTFyaOxe8UmsbnzWUzMXqwM10BlpbQ6GrekVExpZLVzsZH5dXPJ4qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=VVzXddvhcztMDdC1TLS6J02I9sEV5bZgDE52kE56xX8PqPThjnWw7SdcR3ZD5yCFoJN1ebOmhcYSUVLOpTCp0VepCbhOQj5P1ropTgfFrEH0_rnLLK9-1265GawiXwf__GzqMEp1Ie2F0z1xP3wABbovSzK1Y3P2FTIH99WVwav04a2zXfkSc_0J5vBO-vJIGVvfeLHe_V0uxqnJv4NZmlq6MYyHD3cOcOEby1Wa7-6fOubNVoC5G69H5IL7hshBu9kIQNKYXfKaJ3mn-MXAjJyg6NcZ_hKNWVEsyWORUcnAv2p1dqzJIyGfaBeVf-gZh1J0U9qBU6MddcFEpxg8bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=VVzXddvhcztMDdC1TLS6J02I9sEV5bZgDE52kE56xX8PqPThjnWw7SdcR3ZD5yCFoJN1ebOmhcYSUVLOpTCp0VepCbhOQj5P1ropTgfFrEH0_rnLLK9-1265GawiXwf__GzqMEp1Ie2F0z1xP3wABbovSzK1Y3P2FTIH99WVwav04a2zXfkSc_0J5vBO-vJIGVvfeLHe_V0uxqnJv4NZmlq6MYyHD3cOcOEby1Wa7-6fOubNVoC5G69H5IL7hshBu9kIQNKYXfKaJ3mn-MXAjJyg6NcZ_hKNWVEsyWORUcnAv2p1dqzJIyGfaBeVf-gZh1J0U9qBU6MddcFEpxg8bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67093">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⏸
🇺🇸
نوه‌ترامپ رفته کاخ‌سفید گردی و با این ویدیو مکان‌های مختلف استقرار بابا بزرگش رو نشون مردم داده
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67093" target="_blank">📅 17:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67092">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c791837da.mp4?token=bhz-rShI97ZH_72DThhO151i6oHXLHmIgt2hbloHSId6Y9tsq10gFHcjXfJIE-J1x4aTo0ktxcQccHpQcjKPJabkW1jvDQu8WWIRPC3M1XhkRrVaB3ucpaaH6sXM9QamPfshSK4BLDZIrC6BmVtgw-zTFInXG-h0kw79prgWfXbL1KeLMOEGOImXNuGzO-5jRarrKfJvxDQL47qimRoa3IL9qfybEOESGn14SK76W1cs0RJZtMGGwePdWiodgGc6WM28LNBp0QAi_13t2hjkL9P5ZV2xHWguYjXJHNHldW250BIK05TO1B6UK3oTOaftHafH6Ap--8-HgP4n-342H44RPTu1hYFHMMqryBXbJXcAq1K9y_p5CwHcE_hRdZIvyQ7yvKhvQA9yTNA3fzfbR2OksHNpA7eaegWp1zU4-5fIn7YFW8dda0HIZMh0iRupshx0w4lwAGkpw2AojAL1i6flNc4nXxvUKe4xiVbJbRuIdjFdWNe_PxqvVBTQrS7wJwTC2BmdWdr4XVocZBK-JImZKyawlPvtvxvmYPJ6FsYxhlfY_9HfkxQRUzbUKVTuSjXsfhlR9q4uNg3KsF6ilxxcpk4aROgFnW0fVQa66NrcxzpOn9Tn1iUCa4GgMORTRDNRD_JYoCY6ZZPI6eOBo1WRfYM6S3qROJZHGnfw37E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c791837da.mp4?token=bhz-rShI97ZH_72DThhO151i6oHXLHmIgt2hbloHSId6Y9tsq10gFHcjXfJIE-J1x4aTo0ktxcQccHpQcjKPJabkW1jvDQu8WWIRPC3M1XhkRrVaB3ucpaaH6sXM9QamPfshSK4BLDZIrC6BmVtgw-zTFInXG-h0kw79prgWfXbL1KeLMOEGOImXNuGzO-5jRarrKfJvxDQL47qimRoa3IL9qfybEOESGn14SK76W1cs0RJZtMGGwePdWiodgGc6WM28LNBp0QAi_13t2hjkL9P5ZV2xHWguYjXJHNHldW250BIK05TO1B6UK3oTOaftHafH6Ap--8-HgP4n-342H44RPTu1hYFHMMqryBXbJXcAq1K9y_p5CwHcE_hRdZIvyQ7yvKhvQA9yTNA3fzfbR2OksHNpA7eaegWp1zU4-5fIn7YFW8dda0HIZMh0iRupshx0w4lwAGkpw2AojAL1i6flNc4nXxvUKe4xiVbJbRuIdjFdWNe_PxqvVBTQrS7wJwTC2BmdWdr4XVocZBK-JImZKyawlPvtvxvmYPJ6FsYxhlfY_9HfkxQRUzbUKVTuSjXsfhlR9q4uNg3KsF6ilxxcpk4aROgFnW0fVQa66NrcxzpOn9Tn1iUCa4GgMORTRDNRD_JYoCY6ZZPI6eOBo1WRfYM6S3qROJZHGnfw37E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
قمه کشی ارازل اوباش میان مردم در شب عاشورا رودبند دزفول که با دخالت پلیس خاتمه یافت
😐
😂
تاریخ ویدیو 1405/3/4 امامزاده رودبند
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67092" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67091">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=ibmMmFuShm1J8CiICJ4YaGW23sxTER_BpwiU7aOx_btcaUf7q8bn4bDlghVxch4x9nlDi8ReAYgez8gGj4toIEcHFUjD_X5p3j5e0EctTEuNOVYyDoVQ6et-qDrp40QnbvlxNksVnKfwx0omUWIpUNouP_HrsAh01dZ5Lq03krAA1VI0J0G996Sdd0UcJgxmZBbD7AI2_3OKE5y_ABlGVT7tLEe5d0ZX8zT9jB6YirBjXjJsNM34sTUAavJ81g3Z-5cLa2sE_uschDusdtOjY2SCdRHgUpjL7AMua-L3dixWb3Zu49Ri9NFt01el63-Z1YkWx_PINYUva0hGDxutzHqCndoCgZi5qO6Qac9sjhpApTZGvR25d1pKS8XIlZA2D3QFRN4fUF_lEieTB1AXyBtnlnZXI7NUB5lkbjYdG14emvPJRlBPZXm4u9P7ZgnwtN1QLsF1N9W2qZWD4d0Yu5WjKBMFBgFyfHhbmto_R2RHdIt8Yq_zD_Xk-SsSuSTixtRkf_A5yP-JabqsCLjYEbuzZpTr9EGDLYEao1PpYa6J27WkVyhR06d5nCoX3BatjuaSrss-92KW1GvMfEdVzMNIHIGfoMAx1eVlEtBIq-P2YdU6CFXCZLNi-hJqu83Y01cuLdL5SChBB0hkbe-lMHcAmce0lKisKtdV5Ft2uu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=ibmMmFuShm1J8CiICJ4YaGW23sxTER_BpwiU7aOx_btcaUf7q8bn4bDlghVxch4x9nlDi8ReAYgez8gGj4toIEcHFUjD_X5p3j5e0EctTEuNOVYyDoVQ6et-qDrp40QnbvlxNksVnKfwx0omUWIpUNouP_HrsAh01dZ5Lq03krAA1VI0J0G996Sdd0UcJgxmZBbD7AI2_3OKE5y_ABlGVT7tLEe5d0ZX8zT9jB6YirBjXjJsNM34sTUAavJ81g3Z-5cLa2sE_uschDusdtOjY2SCdRHgUpjL7AMua-L3dixWb3Zu49Ri9NFt01el63-Z1YkWx_PINYUva0hGDxutzHqCndoCgZi5qO6Qac9sjhpApTZGvR25d1pKS8XIlZA2D3QFRN4fUF_lEieTB1AXyBtnlnZXI7NUB5lkbjYdG14emvPJRlBPZXm4u9P7ZgnwtN1QLsF1N9W2qZWD4d0Yu5WjKBMFBgFyfHhbmto_R2RHdIt8Yq_zD_Xk-SsSuSTixtRkf_A5yP-JabqsCLjYEbuzZpTr9EGDLYEao1PpYa6J27WkVyhR06d5nCoX3BatjuaSrss-92KW1GvMfEdVzMNIHIGfoMAx1eVlEtBIq-P2YdU6CFXCZLNi-hJqu83Y01cuLdL5SChBB0hkbe-lMHcAmce0lKisKtdV5Ft2uu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
😳
عاشورا برا این اراذل هرچه نداشته باشه یه خوبی داره و اونم اینه که تا سال‌ها سوژه میتونن دست مردم برا خنده بدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67091" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67090">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=ogLIjBE7SPQJZHn-ORA0HF79141tA7Dvd9x-M4t4nbGGe-7sT5HWyJhoZHDUmcO-Nxj_U2l4UnmdB3DrscCuL-fkt2xH4jrckYfrU03cN-c--2iktl_aJP1UDPxZJsFRAhOcfNNbtaazTGg_MyzMZ4_GgkoP1trjsT8mnccp0lkFCV2pn9bjrG4v8t_HYhFLt917RvCqKhhh2EbdnvUUouKJZT7gnXBDCb0RoTCOxPhu5U0H-peZUlNJiBYy0wjtbtLmUf81J14uQ4tBk4zDaZUPRn2s-aKEeYjhp434IZJjazxymi-7CiXx6ez3aTMIBcih7SGgaiDt31A5BvAadg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=ogLIjBE7SPQJZHn-ORA0HF79141tA7Dvd9x-M4t4nbGGe-7sT5HWyJhoZHDUmcO-Nxj_U2l4UnmdB3DrscCuL-fkt2xH4jrckYfrU03cN-c--2iktl_aJP1UDPxZJsFRAhOcfNNbtaazTGg_MyzMZ4_GgkoP1trjsT8mnccp0lkFCV2pn9bjrG4v8t_HYhFLt917RvCqKhhh2EbdnvUUouKJZT7gnXBDCb0RoTCOxPhu5U0H-peZUlNJiBYy0wjtbtLmUf81J14uQ4tBk4zDaZUPRn2s-aKEeYjhp434IZJjazxymi-7CiXx6ez3aTMIBcih7SGgaiDt31A5BvAadg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔴
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔴
اجرای بند آزادسازی دارایی‌های ایران در حال انجام است و امیدواریم کار به نتیجهٔ مطلوب برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67090" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67089">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hN2m2i9gUD-6oBDlHQu7mP0FGyzxPWDDPmGZ3G7FFXvx9yQMBHkwGk1bckhDMdepfbil-IR4O5honTnoiWgU_imCRHkFETynX-OhP06jp8UCIdnRRaQQNfMt35xZdoLN_QZvSF4pwhWj9qHtROJJIhEJmWpYJVlumFgkkP2ygzVIHI1wK24Iq6wtDt9GJcOEGVDCYC310tPbhKcp2Cq5DhtmBCWVGj-9WmPDbxa9O6tkksD5gAHXlu5xTjhWz4hENKKKiPF2vfAY4dkef_LjmflWPku4FThStTG1HeKVEnWmriticOWjWvMajWg2KW9XWQx-hG6Vj5JaMY2bWuZGLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
مذاکرات غیرمستقیم میان هیئت‌های آمریکا و ایران فردا با حضور میانجی‌ها در قطر برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67089" target="_blank">📅 15:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67088">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzL4n_PcHVAMm_M5d73z_jyJnl1pP08TbbCrmqZH2a0sf8Lpw0pN18kOIgdQ02FQu6e_PJChhIk3zMj8NhawultXakosI9aMIAwfyhTKjrFTbkgxep53p1EVt1DBBtN6pv0TTtVPrXy7s0wUA134RUYk5CtPpd2CxmXdo3BBLsrKutw00M9YIS_zTnko-M8CXNGzFkdBq4WASF1XXtbnvLUyyNegpbegjRgCMhyrylUy0IAFaHqifYqjQ7Fj2HcvDOnzj_5QSfW2s3LxzjHfM-OsvBFtEb-J0kQ18oUglMOB4pW1Dw7VrwDImsmgTQoyuDd0OVkxFciGpydnzFnkfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67088" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67087">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=dhxso22g0tm0wyC87U0_h_slLZvxEj-Gvks1EBOycq52w-gzyK-ky2LhVFx2BVFLULIlUN4hUM7ZZTu-t5g21Ya-ja89-gtfqKcJBIvPKtZfGSoAud6yK-ja7bs7ZSiW00VqI53TtdxqKmo0N5f3jgxDj14xpJsUOy7BC9PlwF97Fl3Nrygh6at6A4O02_PCV4UKHilPiO9ZrO11IwcuzbfcXTtN-smcDUwh1ppwVE5r6Jw_VReUMqqwnk60Xx8itpYbrB8kSkPvj4G0elusqu1DVDrO5MeZprS2Iheh6Bw_Vz5A9NuijG-wx3-OFRJptbl6lMXDfnMWL8muGze-qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=dhxso22g0tm0wyC87U0_h_slLZvxEj-Gvks1EBOycq52w-gzyK-ky2LhVFx2BVFLULIlUN4hUM7ZZTu-t5g21Ya-ja89-gtfqKcJBIvPKtZfGSoAud6yK-ja7bs7ZSiW00VqI53TtdxqKmo0N5f3jgxDj14xpJsUOy7BC9PlwF97Fl3Nrygh6at6A4O02_PCV4UKHilPiO9ZrO11IwcuzbfcXTtN-smcDUwh1ppwVE5r6Jw_VReUMqqwnk60Xx8itpYbrB8kSkPvj4G0elusqu1DVDrO5MeZprS2Iheh6Bw_Vz5A9NuijG-wx3-OFRJptbl6lMXDfnMWL8muGze-qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ویدیوهای جدید از زلزله ۷.۸ ریشتری که در ۸ ژوئن ونزوئلا را لرزاند، در ساعات اخیر به سرعت در فضای مجازی پخش شده‌اند و لحظات پرتنشی را که در طول این لرزش قدرتمند تجربه شده است، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67087" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67083">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkOUWft8FbtCC5OY8567A03c1hh0P2Nvi5VTAE5mJNGZrSOI5Z0Tfxz7ONyU9rYBHATzHkMbUZqzZs7I0mnVIshR5ETlb07tZGcenF-piLn3G2sIHWq6RVmoL3QcFV5jIId-w7gxKp84ViYgaNWuaTg8d8DB6S1CzPu2nF42dpsNiXh2gCR6DhvQi7noxlFy1hCZeGiunThE2sudX5Jb4dedBRX_9PNx3ghHPR0GrgiaLpMrzou5A5oC5E4h-8yZjLj_krFMW6zGxTOVvdaG7fat1S9BRpjlrJx9r4t7SoewGqhyX1sNTS7hDx1_i4l8BRENHs_ZEngd2BdXRSV4tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RVzlPXmgAKlAHlKnOi6eCb0zTbVuTIwJuOnbkVf70gZDYlqzKjOh96YcWIXAaV8MlTwBg6LKG7QCfcNJsTBRZWyzP5KCcEp-G8FNhQ8_HLfl1Dg_588XTUfMTaJIyzzzY5pyiKwBU6HYq0WDGdchVSKzr4QR9RmRNhQuFzRkedDgTsbTVYqmIYpSPQgT0rqigwP4FB-O8p38-7GTPtHPfi0oG9XXHmHiUVil8ywW3fK6VLVpTZwiwDfydhMrCgKPW9hJta_VB3mkrW5y-wKfkZrm0tj_YNYYSbmXYrOCm7sX0u5c57xKupfmqwMGCAjyB-A17-ZKLFDnO3cRnGSh4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S1eWzd4vkedQMyl-wMKXnjaJzfNjTHwGJp2_SENJ0kbGJ0Eu-nw8nM4geom3o0s4SZ5b6hBrPvTlM4RgSptQ4yz2YAsB37KIxlnIEa1ysK30wmvlXnRNdotZ0HMK1awRbrUdw2lPq4W8E-tlV8doH5OC4cUxBh4NtywvRVyvYnF0zukA6eW3pMWuLxTEhqFKBpVTcmJe1kF5x1h40Us8yHCXN64zwUn61y8rhceqaPNSZiPSctzFsAF8t85xXUkMIM-cZ1E3Mq4Ayiydd_66kqGP_FInKKJmtcQPQC8u8PEHdaSC6wVyGuH-vUG_4cCylkmZtnVa8ez-xOOMydV6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOXveuDZPGgPuKO0yRTVwWbAIlC92eWhLgFKluKCPppumo1ZJfE3GYrG_IIv9uzLtFmBvT0mmUZ6K-o7LlZZzJ85KElYs-tfumogZlfX0K36ZvLRD2o3xv6wxa5SBHDfv1crtrqWE5WbESjVQLU31pYNPuUwkFp9_c_JqW_ftBFRrogXZabntnBkvT9V0ax9nP1iMV7eEeAPdduV5-m5uyg4Uo1_7F21Kq_3ZrR5C_iE2LC7sgzNYJRq-flfuBHWC5V_PC8oQ1_CYHCyPUUxNjlI5C_ykO19wqz3UwRZMg5zDwuCecdS6exe8Ka6NbjKHiR4EwXm6TuMwuec7DvGrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
یه پسر 19ساله به اسم آقا سامیار، اومده چندتا عکس از تولد خودش به همراه دوستاش تواینستاگرام پست کرده؛
حالا به دلایلی نامعلوم، این پست تولد آقا سامیار تو اینستاگرام فارسی به شدت وایرال شده و بیش از چندمیلیون بازدید گرفته:
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67083" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67082">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
⚠️
قالیباف: سوپرانقلابی هایی که هیچ غلطی برای این انقلاب نکردند، ازهمه طلبکار هستند
این ویدیو از قالیباف مربوط به سال ۱۴۰۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67082" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67081">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی وزارت خارجه قطر :
هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67081" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67080">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
جرد کوشنر و استیو ویتکاف، فرستادگان آمریکا، در دوحه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67080" target="_blank">📅 14:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67079">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
هیچ نشستی در سطح عالی میان آمریکا و ایران برنامه‌ریزی نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67079" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67078">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bv3ysO1i34hxr95bOFA84m_mkCIAwYvsn4l4hxyQai2AaXbDfYZBALPzcvyF-TVBS323y1Yt5Tu_Z-2-33_qpT4Ueo8UaZ9oVYo9PsBOz7fWByTxMaCj2OXYdwQMMSRGhCMwvARmNwvF1-Mq2szjsZEkuhMsUBI-N7Uhom8e1xaRUC932CoTaYmNoBH4Ty4Bv74LAvMdnmjRc7C8gnq3Z_rkj11XOTJVa9ToWm96KPPor3u1Iuv8roc1Dzt4kFZdYjdzJzvssb0j_E8Do9UjniVeWtL7gFO8HkfsHthGfZ_vTe18RUBWXkbzmZu_aaxYtESWXYFfs60e-GCZQJlkQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افت رتبه همه دانشگاه‌ های ایران در رتبه‌بندی کیواس ۲۰۲۶.
این فقط یک خبر آموزشی نیست؛ گزارشی از هزینه انزوای علمی کشور است.
رشد دانشگاه‌ها را با قطع اینترنت ، فیلترینگ، دیوارکشی دیجیتال و انزوای دانشجویان متوقف کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67078" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67077">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohHGX15OuGBrDn5fRKH2YMmAglJhT0L2qXVoP4C7_gZFXo5cMU0UB6oZXiw68RBIcWVQPDWTcQxdBkbt90GxgfZzsG0GREY3BIGh11u68oYFXo1ZX7jWPyb2uvR0mmyo7-WxtG5FLoUAFnsOd2nuIibAmxda1MM71q8zKNhdmJjEHeYsFvgUA4mKw5Ay33FrsH0FOJdquv-SjbXD2cf49n-uvybpDz8GLKQzBfDKVDvUp-9nQq4jSzH33abteKggn_ggpXedygD8zpc7WsniWhwzA185RYumqDwSYDRe2dGE1Qm5DkSG1PzyzLvgXu4ewZnChooN6zBSbKqAcNDEPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
💢
فرماندهی حمله جهانی نیروی هوایی ایالات متحده برای اولین بار تایید کرد که یک بمب‌افکن پنهان‌کار B-2 یک موشک ضد کشتی برد بلند (LRASM) را بر فراز اقیانوس آرام شلیک کرده است. ادغام جدیدترین موشک ضد کشتی آمریکا در این بمب‌افکن تاکنون برای عموم ناشناخته بوده است.
💢
نیروی هوایی ایالات متحده اکنون توانایی انجام حملات اشباعی ضد کشتی را مستقیماً از قاره اصلی ایالات متحده دارد، در حالی که پروفایل پنهان‌کاری خود را حفظ می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67077" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67074">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPw5p5teEZ0mr1a4QPwlNxQoKqYNYlO5djj8PifES3ZTzSX-hXsW0gvC03A6yLHhrGBEtRCwVtp6L2ZjoE2to94AmJAx5Felrz3UCiBd80WETpCD4jlIcIo_bcimXlI2gL9G_hQ1-LxYT0-B1yzKQw9s7nck7ux-T2UmEEFjMwtcbI_FMxVb40cCM-QC39aKafH1f3aWxtVh-py9GhrVp1cPSBq589ExbqHFkGjXbOs17Zgt2i0fRNu_yRylMiqSDuIFEgCbWGLnCjmsOPH7wSrZi1Nn0o5mwHAZXhkb74Xe3Xf7nUjbBxQPiA7KoretbNJaKFrZhT01n4Ua57_eag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
🇺🇸
مولین، وزیر امنیت داخلی آمریکا: خیلی خوشحال شدم ایران از جام جهانی حذف شد. انقدر خوشحال شدم که رقصیدم. نصف اعضای تیمشون سپاهی بودن و هربار برای ورود و خروجشون کلی اذیت میشدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67074" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67071">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOli0KVq6OtFevFVXxenhhIn5OTCWRHj7tR19m0zz40nLnZyd-PFtm7O_XSKGVpkwtjQcAdVZLM1oiiLfTUd2J1vQOiWUh5x__C9WigU-ouDe0D-ernS9CaUvdvDxrTnKV9SYhcmjp5u-x6D8Tl1Sp0y1T4hD8OlZDDQKOzS_7ZdfvWaKwLTbqao7k2OPkobTfy1FH4VDYPwUI-5wc45-dI0AwEKWOjGfT2sy_078J4haXKpIG9W0SGyO4rCIV27GxxthmnIzqcs0CLZV8U4O05ne3Eds8tK61vcDZPtBM0VTq-wi108XwLWimz-4dgF4QMfunyQgBkJXYXaEQ0OQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f1KxxrgE9iXsZQjJdEZPWAvOquqTpY_E4VNog-nPNmvBMf7eLUkB0TznB0vVvQlVt_-zLjCSlxkpF2gJ4pnE9Pj1PskNDsPwKsoBVFFaeg2s_z8C7ty_mswL9K66y9byl_SIVMxZDJ50QKV7DLJxZOeri5sazFMVO3N7wOPjFSctd48SH8uO5T8FXB8XNW2x1KN8Og4W3hSmucXARvkPEcIL5-ZfEj0LfmtMCT_J2FohE8NMtzHxvEfh8zqD_AYHv3ubN7AL2wn7cs49x_OHMsqxb9xfSIrxt7DhvPqDupDOt3tfxOClbsp8vZbS-aMt3QEWzgSbIkStxkSQnnLC5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1tmuqU-Ye9optMIpiaa3-eBzW1YoFbItalzi3UoAL4c6LMs5CuI4lnSiYhTvlhNkTpU9AuZ0X7xgI9C___uk1eqbrDzo2JMwFQVlLat0mdstIvfRq_6S_z0BkG3gU1Tz_e5QhhIEhMBtGcjKdH3jqha8RKmIuDFjCsfpMG-IXYIsGSVnleRk11mAMEaTsaEBUyfMy0R_S6dY0FbxPzWAkQ7bhLBbAdnaaNky-Bxa01lhOwnJo4mURfBasfbW7WwP8QZRs2gq1Caaj5vuh24xmHm-lWiNjiRihxS7rGGmHlkhMgs3vOPN9oPfGJhgeaPY7TXurNG9aYe0CyCVE0ygA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اشتباه نکنید، این زیرزمین خونه والتر وایت نیست، این بخشی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراقه. حالا شما به این فکر کن توی جمهوری اسلامی از دون‌پایه‌ترین عضو  تا کله‌گنده‌ترین فرد چه اموال و میراثی از مملکت رو چپاول کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67071" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67070">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksKgnOuGbywJ_5dusrHzLSSm9TP_o7087sOuX9Pe2_uyfCp0BSAN8jOcdAq-ZvL1iWTrMpoNcFRfPJhUqherF__IqUwPFsy0NwJ0rjyr5WRHBYUHvqfhUiX-CejkYDVICwFHAfEUZWhgC0cpD75GA-Bjtm0Nztmo7gPdIqnpnG5NfuuUMC4FO2bz1kgvz5e3Vc425iCka20Ss3EFl88FZUB1ikDsnJZ2ID-a-5fBcCWG-TuKdBou7tLGY-eIw2E1d8viykxN3qemAb4_V0-Sd8yVbTjwDkPniLVadpmdR2DVrvLvtePN-2O9BnW-PG0VvrOP04eufXYDqF-GLJOesw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
اموال کشف شده تو خونه یکی از نماینده های مجلس عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67070" target="_blank">📅 10:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67069">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=W99_JngT9nPh_uP1h-z6DebAcF6NvibT4G7buEGdIT9k_89b4xF7C-e-bY-FQPUo7iF-0C6lviGFVhk1_7-e7TIrSqna_R0Fzp1SvDQ5YzdcELOPq5JS96ANzG5X76q-j7OiQvT5qK7hbwNp_nvveQCNlSyJAsH42Lxfr-2xy0XCP5p_8fIz1ODA6EUYs0EIs69HdIWm67csd1xkXORZGF1e7vXj4VdzErT4xnQjSIwjm3MtLoUTb5uBe2QmxJS6jBZi18OS_kJmrAtzk0jHT2Vmt8NJINK3MRF6aZD5zaxd6UJGChcBZfqEq_BIaRNE9ushkKUTthG23iGSUUemLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=W99_JngT9nPh_uP1h-z6DebAcF6NvibT4G7buEGdIT9k_89b4xF7C-e-bY-FQPUo7iF-0C6lviGFVhk1_7-e7TIrSqna_R0Fzp1SvDQ5YzdcELOPq5JS96ANzG5X76q-j7OiQvT5qK7hbwNp_nvveQCNlSyJAsH42Lxfr-2xy0XCP5p_8fIz1ODA6EUYs0EIs69HdIWm67csd1xkXORZGF1e7vXj4VdzErT4xnQjSIwjm3MtLoUTb5uBe2QmxJS6jBZi18OS_kJmrAtzk0jHT2Vmt8NJINK3MRF6aZD5zaxd6UJGChcBZfqEq_BIaRNE9ushkKUTthG23iGSUUemLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مداح:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید.
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67069" target="_blank">📅 10:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67068">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=phrtzVNSC1sHrcxW75oulWX56v4Haie1DtF6Tqk2I3c_xWvN3sR2eL9FvZuU4osaeYwPIBz6NY1ASegS8UQFuLJfwZVGqe_jABh5f5Pe3YePBXsB__-coojb3f4K9FqkaIhBqOfAbmWGut-PtskDyAZfYOIDZUdrztnCoJ8eikxNJAm6VY-qq-tcEVbSVcrwYdkrMB_Vha_v-pfbOEOBt_zgzsalXlp8nATBF29uIKeuIgDZqD38qFdtfgYTRmUtTySmOPImryuCsZ1PGy4rX_3Hp_LMM7apOfZR5_N01hgtLlcu1a2m-3gA-_PZ1RHhJT6zQIGq9TpApBIMMvNNpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=phrtzVNSC1sHrcxW75oulWX56v4Haie1DtF6Tqk2I3c_xWvN3sR2eL9FvZuU4osaeYwPIBz6NY1ASegS8UQFuLJfwZVGqe_jABh5f5Pe3YePBXsB__-coojb3f4K9FqkaIhBqOfAbmWGut-PtskDyAZfYOIDZUdrztnCoJ8eikxNJAm6VY-qq-tcEVbSVcrwYdkrMB_Vha_v-pfbOEOBt_zgzsalXlp8nATBF29uIKeuIgDZqD38qFdtfgYTRmUtTySmOPImryuCsZ1PGy4rX_3Hp_LMM7apOfZR5_N01hgtLlcu1a2m-3gA-_PZ1RHhJT6zQIGq9TpApBIMMvNNpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سخنگوی‌زن‌قرارگاه خاتم‌الانبیا هم‌رونمایی‌شد
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67068" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67067">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=SZZ8mv_tvUTWqYcB4f0j4oeq4YhyV3W-7sGJVSyyto2kWAbcmdBfR7UbLAHyJBQ24FjAvl7vD5U-Sgz1XwKnrxOT2ifdrg3fMMj_mB3iOKBZ2rxWqbwCIFIV-vVZ2ybAIMi1hA7tooC7Xpyyod-5nkG_DmimDZ02_mpnYoPzdqZgoUrC1UeKSnmlNjkiBqh1oaVe5uZjWd3iSZdZMfou5LuzLsK2aPGv885VHPTH1FFHs0NTRu4lONqOUQrwr0aLjqM7fNDLVixsVfEym_v4sHnyB5PFDOXfJkUAY3xdQ11_2rTKlPBbEuxZkzbBiFzLjIdpXBRcNgoSDBBewEWDIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=SZZ8mv_tvUTWqYcB4f0j4oeq4YhyV3W-7sGJVSyyto2kWAbcmdBfR7UbLAHyJBQ24FjAvl7vD5U-Sgz1XwKnrxOT2ifdrg3fMMj_mB3iOKBZ2rxWqbwCIFIV-vVZ2ybAIMi1hA7tooC7Xpyyod-5nkG_DmimDZ02_mpnYoPzdqZgoUrC1UeKSnmlNjkiBqh1oaVe5uZjWd3iSZdZMfou5LuzLsK2aPGv885VHPTH1FFHs0NTRu4lONqOUQrwr0aLjqM7fNDLVixsVfEym_v4sHnyB5PFDOXfJkUAY3xdQ11_2rTKlPBbEuxZkzbBiFzLjIdpXBRcNgoSDBBewEWDIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس تلویزیون:
جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67067" target="_blank">📅 09:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67066">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=SGTnBRRG96GCizVrx2AarIrFPQUKlbjkfVitQ8hLg_ikYHCfYq3_AVNKSM6Sf4xxUpap2P1uxcWIe7CoeSXMyg7TqMWmrE0UuVfK6ZSaFCHLv_fQ1BMvYLM-hyH7hUkuYlVXnpnbsdFi3o8xZh3focLeisCvgSEo_fGspLtKY_GlncdnfYtxkRyWDr7jpJa27V-uFDyOuAjIPtp0Q-pPCZgQYBnhWmxEVEYGEuDtRAD_qgx979xzrIFm7m5smK4iAynmOfwrJOEPes3xJ0kpRECsnSfBHNJnCL8XU0qQUZo2oZtOlAyUeigWnwzN8ca08ljOgZ0TtR_7WvhjxZAH4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=SGTnBRRG96GCizVrx2AarIrFPQUKlbjkfVitQ8hLg_ikYHCfYq3_AVNKSM6Sf4xxUpap2P1uxcWIe7CoeSXMyg7TqMWmrE0UuVfK6ZSaFCHLv_fQ1BMvYLM-hyH7hUkuYlVXnpnbsdFi3o8xZh3focLeisCvgSEo_fGspLtKY_GlncdnfYtxkRyWDr7jpJa27V-uFDyOuAjIPtp0Q-pPCZgQYBnhWmxEVEYGEuDtRAD_qgx979xzrIFm7m5smK4iAynmOfwrJOEPes3xJ0kpRECsnSfBHNJnCL8XU0qQUZo2oZtOlAyUeigWnwzN8ca08ljOgZ0TtR_7WvhjxZAH4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعود پزشکیان در جریان مناظره‌های انتخابات ریاست‌جمهوری ۱۴۰۳ با مقایسه وضعیت امروز و دوران قبل از انقلاب گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67066" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67065">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67065" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67064">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VUBb9Wbi-c6g6YCtgS2zQ9GhBZb4DsxQTf8WqIU5wGSJJFry5txJAQnQYCOuUx3ysuhPiQgqXpm06VhWwVfckJ0LegvJM3DkOwWQEVlPqoWrsTf1i2P3Mi9VCvDzGBtphdOOjmo9xPKyDE2sFhtdQi17xepO3O4efW-rfyJHIQj0OtxPIy-fi_F8NTEEm8xNHvvRttMnlbwj_9c-Fvs9JSghkMUdDgJFdSh-46JbCW3VKtOT86vMPu8CcA2PgTjGmVuZJbswItaB3gvyIHFEAScGQLRm70fdbMksbJzLl7lFC6K3_T5Wj3eK6ln3ULhgGa0d4UmTkfzm1kX99sDUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67064" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67063">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر جنگ اسرائیل:
احتمال دارد جنگ مجدد با ایران طی دو روز رخ دهد.
وی اعلام کرد که نیروهای دفاعی اسرائیل آماده عملیات و هدف قراردادن ایران در صورت استفاده ایران از موشک‌های بالستیک خود در راستای دفاع از لبنان هستند.
او از آماده‌باش کامل نیروهای اسرائیل خبر داد  اما خاطرنشان کرد در مذاکره و اقدامات آمریکا در راستای ایرانی‌ها دخالت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67063" target="_blank">📅 02:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67061">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBSg0DyWDQ2HsOX8Z-oPMSKc9cMHpRkzrkBTg3Mt9S5kqs7sP2_vv0q4C5TfxoGSsukVwJrU3WMvBkD0qdJPSo1fV9X1r9_M-1m76X5_iqNaZEncbbJHxU5HW1-E0TvKCRVsvyNGjEqWtMPoQ8slMhhblI3wy6N38A6IPN5Naw4UdCen8ZylSCE0qA4WIFvL0PKmuqTskdRs5umcyc66Q0oCOX8q8V4RnEiz8qQfdz7XmMlFdcooSMjwQgAXz36qdhMYmwkB2OhYaItsMLBHH8BxF12F1lQ8dtc_OOXJ9uDBBiJk0NRJWSAA-HP8QsPmaVsOFrVHVWGtl3oiSkXz9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری از بیمارستان پاوه و هجوم خانواده های نیرو های امنیتی به این بیمارستان،به نظر تلفات و زخمی ها بالاست.
«کشته شدن سه پاسدار تا کنون تایید شده است.
سیروس درویشی،خالد خالدی،برهان کریسانی»
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67061" target="_blank">📅 01:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67060">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
گزارش‌ها از درگیری و حادثه امنیتی بین نیروهای کرد و نیروهای نظامی در شهر پاوه ارسال شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67060" target="_blank">📅 01:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67059">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHdZle-w1oz_jQE35ly0OQr2rLO3OrQtUsPTQFNJZz2SZH9SeHuDVhfaK7plTlE4CpjPQsFkelsDntfoO_qsjoTSMXbL4v-KC0oy3YMsbhQU51EwVbOfW4wM7Xji9kvfyaPhtxcVPxfdJmY2RiRyt6BJlDgmSfJnXliOKlE5tIoR5cia3InLtU7uumraSygl9xAmTDzZERlPwONpwA0vjrP6LlfsXCmielpzFHOuhUByB3QT-cf3UA1-DNNGNRZrJXV4kq2GgQ0-DCO5xpLyFFptBHgPFCclocLwNAuKOvaKH3HwSEkBUpctrndtgSHApctxHqrce9du3eTXPeytJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
تفاهم امری طرفینی است. اگر طرف آمریکایی به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم.
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67059" target="_blank">📅 01:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67058">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این نشست در دوحه شاید مهم باشد، شاید هم نه.
خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67058" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67057">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a452960e.mp4?token=kE71uCnqnrRl0DCHjeFveDjkCOIaxWZHCJ4BSs4X2dN4Jf8geVhp5YqjdRDk7ImEXiQCfakyP80TdbqruPNpea9TKwxLgXC-qOmLvj8cEDZMgdQRL3ZA6V9sx4WqG6Xbpe8MffaxvYyGIQ1-6C0oGfKw-Wr0P8sx2DLPGBGKTkVXHGhb7Kh1mQIdrqTi7RQPZKqYBsU0he3JdA33xEKoK857Tt4-RgUWTZc4bnCmLvJQaZ0zKSAbsH0mKX3BHzjz9OzkY2cogjhsL9HK0Wtfk_zit7mQR3ViCRyxWexwpsPEvygSOfPfGBdkFwXbl015NdcsvcfpjFdnogB4KGQVHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a452960e.mp4?token=kE71uCnqnrRl0DCHjeFveDjkCOIaxWZHCJ4BSs4X2dN4Jf8geVhp5YqjdRDk7ImEXiQCfakyP80TdbqruPNpea9TKwxLgXC-qOmLvj8cEDZMgdQRL3ZA6V9sx4WqG6Xbpe8MffaxvYyGIQ1-6C0oGfKw-Wr0P8sx2DLPGBGKTkVXHGhb7Kh1mQIdrqTi7RQPZKqYBsU0he3JdA33xEKoK857Tt4-RgUWTZc4bnCmLvJQaZ0zKSAbsH0mKX3BHzjz9OzkY2cogjhsL9HK0Wtfk_zit7mQR3ViCRyxWexwpsPEvygSOfPfGBdkFwXbl015NdcsvcfpjFdnogB4KGQVHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ درباره کمونیسم:
این سوسیالیسم نیست؛ در واقع کمونیسم است. آن‌ها از واژه “سوسیال دموکرات” استفاده می‌کنند چون خیلی خوش‌آهنگ به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، حملات ۱۱ سپتامبر و حمله پرل هاربر هم می‌شود.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست. بعضی‌ها وقتی این را می‌گویم می‌خندند، اما افراد آگاه خواهند گفت: “می‌دانید، احتمالاً حق با اوست.”
این در واقع وارد کردن کمونیسم به ایالات متحده آمریکا است. هیچ‌چیز تا این حد خطرناک نبوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67057" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
