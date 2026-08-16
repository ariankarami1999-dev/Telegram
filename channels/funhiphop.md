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
<img src="https://cdn4.telesco.pe/file/V61L43q0nImIsHRYq_7RCc-ncKEqHkzfC0Fm0BL1WmzxTMLE5DRQmYV7J6-kQh-liRw466den72GUPIVqC0P9vrozOi--QFzApqvpwKmTM4XYCU2LAosmaAkRuDXsko0pvQw1qY7ThWoFXQ6rBJSJBI4aTe70ooD0O4mDX5w5nnmExERxPB3VaIwSMWfxI9Z1uEFyiBIE9ZxWjME_9Ohg1mS8atRmhbovkHsUCR_LDIPEVcFfFEwFh1EWlK70vJMdrW3gfljAVn7qIAwX6HV_TuCflvjpCC7QTOP1phNaA7jcZE1bDV7fNg3da9sbAsJfUa4h3KAI2qm7AjMkAhmHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 02:13:46</div>
<hr>

<div class="tg-post" id="msg-82291">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/funhiphop/82291" target="_blank">📅 02:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82290">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/funhiphop/82290" target="_blank">📅 02:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82289">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToJZK73h9eo9VH34CPstdycFIvsMOa6a9oT4kR_bOufaVxzd0n3xIOpaocjkUr4cAuER36AvllO3qB3bFLPdlu82n9ohlt-UKOLHckrIw8Xurx_7RACEhQsYTkhPkvfqkUgs47lE0NxUQd5bjToHvuBzGu8uAcbKKay8VQG_8XaYugRXkVFcPxPH5UcuJdvJ_1ERgOKqaBABKPlrl2_07KGD11lSiCXDlt9c81QyC00aVBkVdGFsibIRsA0xaQA6HiS0bnTZQxkBv3LWpkYeXg5FTKdZGpoRnxK5Yo27SVwrXViyBex0bW7iabux61PrgSN69goz89f991BngAdEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اثرات تمرین با فران تورس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/funhiphop/82289" target="_blank">📅 00:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82288">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">5 ساعت و 45 دقیقه دیگه آتش بس تموم میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/funhiphop/82288" target="_blank">📅 23:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82287">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYV4PrWc3XEHiqB7LdVLyPOX58JSG1bQzRNW6zqCVmQWkkiqXRDik-PrGTDjfhuheUQO05YuXDYQCITUqZxlN6E942fHwNLWJDjQx6B3a2QB5Z0m6upN6C1NT0G-5U-VY8MWrqZJtAACmlPK28kf3ukxaByy-0DpsByCv5RzjiaogMge8cxS6yLiLTA0PueoInE5WwAOS8-mhb2eU27fE3Dy4HD-pjpLM9nkf2RO--Rg7xdDWBp7aL40ywrsfB3QaPdc4PNWto_7RFte67LOjmMh4e54K1G7ldThGnLGoSMOaxWUothiGbMJHYFYS4unFjpMFuicmgheoZ6X7TLmWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیمی رو معرفی کنید که توانایی مقابله با این خط هافبک رو داشته باشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/82287" target="_blank">📅 22:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82286">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqsUonu4OxHp1wPph0bPEhySduKahESoPbjDmVrZGrBCC4vKlkDJB2SvC1lWZyBVRdEdsfGfDIY2Qvdou-gV8x2j9UnClwx1zsyaekkCrwSIh9QUIqAvgc3FGcsHnucvwGQOkb3SsskKjFf5bfW9dicbvIw-DXE2lprdfvyrH17ALfc-nix8P_4KJs0vqo4Q93aLQy-wA1_l1wo4WOJrUhptOoiikddV5l0krQQIeYboITa7hzguaXoRoi5oNg-UsBd7fs1EcvFJ4H9C9C31cZ6k7Evu78Jstg_D1g6Z_Pd8W29p9gemqMNMxyIW2grZtNmoMTQqdd1P1fq-9eB2zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیر وی گووو
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/82286" target="_blank">📅 22:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82285">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIMjKUn4Gf0n8G102I8wT1couF-_YjQMXkA2a1ujKbBRPSH6D6x38RNwfXloPV7dnClutQ1LxGGiXcAVyKNkA0Nli00758Tf7Iuvr8t1yifWDzV2n0niWu8riN0rxp7Fp_X6NnJtISDGfcXBT_C8Gp-a9y04Mc9wTciiO5Wm83hcWJHcFBYWVyANKzvJIDmpD2mGUOiqSoAkVeJ3rL0XjcqAY0o5J13ZkemY6O3-gSlzScrg1rIYTAeUfpkUGJ3CpHsheYhFmzJazXm0CqpfKEsgo2pklpM6ZXYtsdly8KQdUGm5L2BTn6rDL-1SosuePC5R6rIloEKHphyX-hHyjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخرین تلاش های مردم برای حفط آبرو
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/82285" target="_blank">📅 21:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82284">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd9bdf52c.mp4?token=AFlzWyjQoVG1vnJSxXRTKWaPAa6AoMWzdp4fc47hKDdKNWdTjdm0Cu7r5edQidgceLVsPOElnjAuFUKhl4G6IFqcUfn6dzy750D9bXHrRLS5v7bQqDd5lgPJdJ1lSTj-xdrZfHqqmugPd-OgwVzLb3NRbyG1HG-2u6Q-iw1dheFSA6-VoOIPswPJ5TLojfy0Cz-haNfDPQKY9ZBrfH_AwxoocpAVaGaY4IRKb2ARQdK17ITRf_15J9TuEvKH_Lq7B_I6QkYM2KYdScbVxHAwQlADmBfyv1ZreHUDZ2g8mz1PTFyPHN6_iBqYFy_5yq6hfEQd_g6DqaJr_nb1fBcBRLwTplJgcyc68Jw41m65j6VQ6asONH6WOtdp_zctZEhQrrgtWTPJbN0B1eRo_yWh9CUjjPYBTf-04ZNYZk635YwibDrsVBoL9TJmpB1HEqCT4XgkBAm0YK06hymAoi7J-VX_rE6Z2cXoxlRvgUVrjA_xkNbolptBpMb_wppDO0p3Gi31Au_JEourvc2ehn1LfBRLa4iDWuBD4YbHVoNcliAc398xBiwFTHMEpbLnQ0JInbTnqk6svdrWotgAZTLJ8m79KV2V9sxNuw3-LrcNaj2L-gH4C2Dw6dD9hU7ZQsI2lbgWSSrVPNPqGzhc9UtaumwE8tmrRHXe7WMJYeOFMkM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd9bdf52c.mp4?token=AFlzWyjQoVG1vnJSxXRTKWaPAa6AoMWzdp4fc47hKDdKNWdTjdm0Cu7r5edQidgceLVsPOElnjAuFUKhl4G6IFqcUfn6dzy750D9bXHrRLS5v7bQqDd5lgPJdJ1lSTj-xdrZfHqqmugPd-OgwVzLb3NRbyG1HG-2u6Q-iw1dheFSA6-VoOIPswPJ5TLojfy0Cz-haNfDPQKY9ZBrfH_AwxoocpAVaGaY4IRKb2ARQdK17ITRf_15J9TuEvKH_Lq7B_I6QkYM2KYdScbVxHAwQlADmBfyv1ZreHUDZ2g8mz1PTFyPHN6_iBqYFy_5yq6hfEQd_g6DqaJr_nb1fBcBRLwTplJgcyc68Jw41m65j6VQ6asONH6WOtdp_zctZEhQrrgtWTPJbN0B1eRo_yWh9CUjjPYBTf-04ZNYZk635YwibDrsVBoL9TJmpB1HEqCT4XgkBAm0YK06hymAoi7J-VX_rE6Z2cXoxlRvgUVrjA_xkNbolptBpMb_wppDO0p3Gi31Au_JEourvc2ehn1LfBRLa4iDWuBD4YbHVoNcliAc398xBiwFTHMEpbLnQ0JInbTnqk6svdrWotgAZTLJ8m79KV2V9sxNuw3-LrcNaj2L-gH4C2Dw6dD9hU7ZQsI2lbgWSSrVPNPqGzhc9UtaumwE8tmrRHXe7WMJYeOFMkM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها دو هفته پس از هجوم قبلی، دوباره هزاران مهاجر از مراکش سعی کردند وارد سئوتای اسپانیا شوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/82284" target="_blank">📅 21:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82283">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔥
دنبال یه VPN واقعی می‌گردی؟
⚡
سرعت بالا
⚡
اتصال پایدار
⚡
بدون قطعی‌های آزاردهنده
⚡
پینگ پایین برای گیم
💎
مناسب اینستاگرام، تلگرام و وب‌گردی
📩
برای دریافت کانفیگ ریپلای کن یا پیام بده: @wizard_0061
📲
همین الان عضو چنل شو: @v2ray_configw</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/82283" target="_blank">📅 19:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82282">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRKiALihZSDJrKvpUDQG3AYQBUapj3T9el_IjytxIkjpwgsT42EdLneiYeuWrFvf1VNELazNxT_MefgnYhTkGM46YQg88_ALP8pejA1ArA-O635FL1vABMz8EQTpal1XMiJnF-NCIv_NzwRpQr_68vhIboVhcP_EffT8aTIvm5xZAQ65vp8WzSWos8klUNlAY0vhR87EU0cLwcy-uqdCnCgItlPBHL0vRCwvl3pXsPFZJK6Le7ndtQ9OHj1y81bgRbb4SU6nWIPXzlTocuipUJZuLqoB_InWw5AEiQN7ty9eT4k8XXDxv8lOt9uTO5d5B4FY6gjBstQ7yIQ7xCaldA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید چرسی تو چنلش  تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/82282" target="_blank">📅 18:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82281">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پست جدید چرسی تو چنلش  تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/82281" target="_blank">📅 18:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82278">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VXz6SGaG1sAaCHfEv96El6hf-6VpqccIkMhvYwhBDTdqHsF9IUjH0K0kah_ELv29eIJEKJ4OjMGi-E9DqVAwOwSRFFWGXskI-UIpNczTfr3itTfcZ9p_qB4BHIVa9idMi4Xz0dArqqYmALTdzaGPlBrPA8Nf6s03K5AkRqYOOqzxB_YPxmR8Kzy7GX9LFU7-QkVka501EBXAfpEyJWjMMbD3n51D6X6dkE7Gh5_oN5sI_DfVldKeXz_cK7z4GxP0S4lgHQRdkRvkGzbQWVIPOYF3hvG8QLHx_KOOCzK08W-BM-E7WikAXdxzniEBLGBQr_1Hz_Xx9upB66_WVKE7eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RxY5CXgOK4PydZSAg3SHHY1sMdAXitIQTKsG6gpbR5Q-FVa0ZBcZyt9AsLueDweLYzSUWAzmIORg66ig4R_uvZ_-Ucb44VRLsAO9o0omqpXL7PgpSs6_75jTf5EjZ5_A1XRzB2B7A9vBODxSgQFdhfSyIQCsR1FckMVLVQI0AAk7d2IcyBXam6S_ocaKfxvQLLqMadPJTKrS59ThHE8ScPzBW5JlOA8DeE3ymIP7wgIidjkFTQVAVVpmv4ai2fzh9z5RqIboDt2EJxgLsDvonHZuXOY_KOQodtKS5xZsyStjGSTkzu9CeLdE_XfQV3_ejhshwOFtM2JqD8MZRoe-Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید چرسی تو چنلش
تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/82278" target="_blank">📅 18:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82277">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQIptDoKqaEIPbp7TLAw8NkJge_w05aLArzNSbNQYdcL03z9l1wWpea1DNvfn39w81zoUd_N-OaIFCHaMKxahjdANhEdNvO-kg4tNQdbYBO5KGE22p_xcrEp47fbUawl1QV-ppVRyH3meA3jopfImP6Q2n4ntMETzIy4Mp3T3V1VDNfuL5W1s5ZfWiekAXe5jkzKoZ7z3c-f5Xu1q8B-xesnFKLPnGuDsZzAdG4OvuAk1jWzujbGLYMvM8BF_bf9UMNiJOGMHgOZXAFxL_A8_d_QHilL2asRRhUT8nD4ZmPChLEyDGxCyZXRjg3gLI2uatn9tYj_lf3Wa3Das7CeBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامیار این کارو نکن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/82277" target="_blank">📅 18:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82276">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCsje9QCwQ_nDd2oEJjc1PE_rgneKQ839nnmKzqyVEZvNWB5nFjckUigOxSgvOTjmeVZ5HxEja6WL5vyTry0Plcq_oF_KgPuxKSolscBWE0GTncZBlpOvfT0J2Qv7ic2pIV5gWSLLV_n3Vc0oko6F3ufJlWBTi4u--oyvfipn0NWnkYI1_pFqHiz6dfaA7QN0mQUcX_Q0_-xSN0AJdiDt6G7phZGv-6EpeXCe7kKMCcF-vnuW-r_vKyxO20KqDQ5yKvUgMgtMB-R-p3H9nTgVaVXpdpM_7x_4mue-uTt3CfSHhA1ueGie8ZDopTKhRGoRHDl7J5_TWDs-yD1CYjRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
لانس
🇫🇷
-
🇫🇷
پاری سن ژرمن
🏆
فینال سوپر جام فرانسه
🇫🇷
🕔
یکشنبه ساعت ۲۲:۱۵
🏟
ورزشگاه بولارت-دللیس
🎲
با بیش از ۵۰۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
لانس در ۱۰
دیدار اخیر خود، ۶ برد و ۲ تساوی کسب کرده و در ۲ بازی شکست خورده است.
✅
پاری سن ژرمن در ۱۰
دیدار اخیر خود، ۴ برد و ۴ تساوی کسب کرده و در ۲ بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر لانس ۳.۳ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر پاری سن ژرمن ۳.۱ گل در هر بازی بوده است.
🧠
خستگی یعنی توقف، نه تصمیم تازه.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r25
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/82276" target="_blank">📅 18:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82275">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عربستان جملات ضد اسرائیلی رو از توی کتابای درسیش حذف کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/82275" target="_blank">📅 17:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82274">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpC9hJtVwDeJdgD0iQA0qK7pGYyoXpU2VY-giKgpFOh510PCokpbSbSJJDyEu5C0iXYE_bULmrA4BPb2fpY7m9YysF93VrEHETlHHvuc_OnEa-CadDK6wvjNl0ndwEZeDGjinX1CuRe7h3CobaD7khgHBr3UlMyO3QDFP5tIOvZy8rZLg7FCQ5_IFL-ThBaPseV7Tyb8KsC8S3mouU7CEDonH8uo1ldCzusQv5JqmCuaHeReFq3JOOIzMl4TuRRf77bDkeU7t1dQHy9s6H3jWFTXQhu18soWgiB8NdgfinIwYcWKU0t16_CBK0sNkz749bqKOVKRYlGQKGZ2IMSKWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82274" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82273">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuETjOu2j3hJhIrAevh4POEVULIde0KR9_6PI0uya3vd6ytmKGnsGfGPn5qoj6w0FbRCGvwYnC3gcETCjxcxREEYiGky_zcuDSgMI4U8tVHgx06nXS9OmuPxydlGshOnxY4N5srei_XtrOhRp2CTMMpIDuMRA3l2LPGMnD4F7KXqBGIV8SVlvCRE48Sa7LAXSmocGXE-Nhpt-cZ04HeRMM-nA_0UMDY-AiLRPn0g0jTTd_AdzjiqZhg6D6l0W6igrILm4gkL1EMoya9abTkH8CqFzQk7QQhUVr1zUIg7TFl4DHlj5okwdVVcXSEYxuqe2lim28VccofDAVKE4kVdHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید متین فتاحی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82273" target="_blank">📅 15:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82272">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGsx3Ugt1aaQ2zrA0uRyszJ2pk5ueFfM9ID5P-o_8qjRHyY2KTD4kmwj2FRZh0uolEVF_hjHw3jdFLra1uxZeGLoqPNVoZ_Lh3NVKsBZwJ7eH2whs6-AZ8gctUVnninivFicYhz9L5I_qRWh306sZGuAlAsNPW5voV4rJyOAjArRR9MqN3EAcOBAgA4w9cBmp9kMofjVW7Ge030SMZQm7fGNk62E4QD7LpqRvF5tm6nitUEYqe9Ug6JkK-nlnSZpulIYuxau--IqluJfq47IyiEtwn1g-GyZEVs2mYz_-vKFVVqyAJ1qNUzuWw1SNQGEiBSjJsyssG5xZwnKrhmw1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرامو از مراکشیا یاد بگیرید، اسپانیا چون عاشق اسلام بود بهش تزریق کردن که احساس کمبود نکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82272" target="_blank">📅 15:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82271">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIV82dwevXQyjPHikbzN3EckVSrM00y8kdYpjU5zw1b--ElbhyqCewFpe5WZFr5yMbxrd0vGSQVbfOoOsFEjNIl9DqeUHDblN5uR2605DDvfI0sIEAi20qZkexurfL8AfVGKcb_1sXKXo7VyIhY2falXRb9n7itl_Yv3ZwFaykp8pA737QeO7fGiRcrJx-98hw9KBBYw2a2K16aA9V8EVO74rjrMN9fY7m9QBXa0WeL7XnTRTH0Xq-ge2Uvqwrj2hjEFwCON4-8nStvM3Tu2yJYvJOM4AvyP5u7scB6Ssu5hQKVmikf5K_i_NKPAkGIRbidOISzByRvcBqeroZ0dDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح اطلاعات و نگرش آرتیستی که خودشو یک شخص با سوادِ سیاسی و تاریخی میدونه:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82271" target="_blank">📅 14:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82270">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فرمانده کل ارتش:
هر ایرانی بتونه یه سرباز آمریکایی رو اسیر کنه یا بکشه 30000 دلار میدیم بهش.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82270" target="_blank">📅 13:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82269">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1569dd1b49.mp4?token=c014wRQ_2uE9O4hNcNGwBN2hAipvoHf_rZ05gkReJIAvsDn5WSrrSI0pf5QMVldf1aPOjuoKRLS2JaouGmCsmq1K-JFcdi3RnVKVBFsd9_gH9aKFhQ1_2Ofi8nWUnkL7Y7kB47TJFTN-njGgfItS0eg1Uun6J2qomWayJ24HvAEdpVAZqdVw_TqLJhl2AM89iqnOVLw3fQKKhH5LFsEeSmXnId4a9yhM9U4tJdLpriN2ymO-Ukj1N7UEznOENtz-kRpZAo05MRge2Mw844dX7Xu2r7vMYWPqJQQquCUUtmVrmWr8oKy2F-wHHz8vmG_RLEQCvwc9EDSFI4gDBAT2XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1569dd1b49.mp4?token=c014wRQ_2uE9O4hNcNGwBN2hAipvoHf_rZ05gkReJIAvsDn5WSrrSI0pf5QMVldf1aPOjuoKRLS2JaouGmCsmq1K-JFcdi3RnVKVBFsd9_gH9aKFhQ1_2Ofi8nWUnkL7Y7kB47TJFTN-njGgfItS0eg1Uun6J2qomWayJ24HvAEdpVAZqdVw_TqLJhl2AM89iqnOVLw3fQKKhH5LFsEeSmXnId4a9yhM9U4tJdLpriN2ymO-Ukj1N7UEznOENtz-kRpZAo05MRge2Mw844dX7Xu2r7vMYWPqJQQquCUUtmVrmWr8oKy2F-wHHz8vmG_RLEQCvwc9EDSFI4gDBAT2XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تهی دیشب با زنش رفتن کنسرت د ویکند.
یه i love you هم تو استوریش نوشته که من متوجه نشدم با د ویکنده یا با زنشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82269" target="_blank">📅 12:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82268">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOrUquRyIyH0tgwktvXFtuKD8v8GhgckSIiUqJiaUpq0I6ECXwj3OyKa3g_VNUuzhgJI2nCMnmkC9nxXJW5vfxt_U8HGOt6GqkqBvl9KPd8gzMB3igFXXLsbDadaawonUoO3eixQQRhmF-ryQ3dIHDz7AdAFxiVbYTATRQSzf7j0ZvSDpeg0g2xZ2CDbHSG65xLo1Xf5EljDvmGI8ZD2hT0JL5Cn0OkMANjtcxZEzWO6S-ST28IFyKQCEIarqha8yLJz6zbJqOejAHrGd5eJLiPDHVHidu0UIqwtMaDvOeURIDRxssBX_zS-8b6wI2l9Gz9AHLw3c6B8I4XFqJqC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دیگه کم کم بریم سراغ ایونت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82268" target="_blank">📅 11:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82267">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkiCH7IHGb48LXkSajCiEJdtYANGbhyo7edakcB2aZ2TCfn6vY3vhhZIBcMZyYLg9NSz375Mi5ZiZR-JMq2rxCh--LellJQAHZ3Ii_9ItCcqSmsD5aUXABbzB6GmhNFwee7kOcGRQO6M-AnO6wWAkeME2dcl64UbUOg3iGksSDKPOVyucthKmliO0XbZF_JGvbSK8IChnsdfnBBQnwABlp8iNaH7WyVHrLvuql9DMBKe6sy3CZ_gPXR9Zp65gy81eLsvsK7x3rxISN7pjGq0yuAOl_xz4csouVzZOxH7oc09EqJYhwj39Ic_RpGEEMoaqeBLKJQHlSl1elpj2ZH1hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
لانس
🇫🇷
-
🇫🇷
پاری سن ژرمن
🏆
فینال سوپر جام فرانسه
🇫🇷
🕔
یکشنبه ساعت ۲۲:۱۵
🏟
ورزشگاه بولارت-دللیس
🎲
با بیش از ۵۰۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
لانس در ۱۰
دیدار اخیر خود، ۶ برد و ۲ تساوی کسب کرده و در ۲ بازی شکست خورده است.
✅
پاری سن ژرمن در ۱۰
دیدار اخیر خود، ۴ برد و ۴ تساوی کسب کرده و در ۲ بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر لانس ۳.۳ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر پاری سن ژرمن ۳.۱ گل در هر بازی بوده است.
🧠
خستگی یعنی توقف، نه تصمیم تازه.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r25
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82267" target="_blank">📅 11:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82266">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iu0v2cQbN6u94gwZwjh4R3eC0ebiQj6SGYyDc44KndmMRHAReomhXSGJZpsu53SwS5YgYC1-OcpJhgGmwVs4P4azTIAyqD6btN6evmrcKPhQcaxu69BaW_ziver3RbwDUjb6N0zUjpdsa_5n5bxJW6S_BnbMPvAP-uJXskVkm8MUst-zFEFuXCTMQei1Yae6MoIFSNhn9qPAQthL00ry05kyDJ-lQb3dWcTMF82IaBlBlXwSXsx5tsV5msWwiZ_cpVXTMHhtED0SCscePlXHzdy96vtdGZAq85NjpRtfTvrd4MjHpmwICh-qi79n5mJRxFBIgHLV7SFKV1N7kdgOBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرام صادقی یکی از معترضان در اعتراضات 18 و 19 دی در کرج اعدام شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82266" target="_blank">📅 10:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82265">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYctcevTSOFYyt1nGuchapWsadPcrBk2YZOzmYuejv4IU8HvVWsndaWNVzjqeiHcEL8c9ewOn06lqxBlUTkqPeYw6sQAyJ88YsDEioGaE36XJktCdVWCDecba2dI3LEPjp-TMPx_at2I7QXsZRgrkU5JNJ-_n30szBIa00I241FDQDGQRs0tr4VJCLTM90JBsJkzTbmTeefkyx44_i0X9c7JXtbqquh4X_XSwDQXkTwlYcr7cKMzD4LisVjAwj3G_--Q1iZ20ta0y8LqLXmVAJkFkAFU9g99X6P84iWJUm9kP3pEAMH6iwcHWbq--jMuUDe_Rmffp63so1xyT8-QeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی پیشرو سیک سینابو زده و سیناب برگشته ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82265" target="_blank">📅 08:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82263">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFscdgy_JMihCpGVWPs8NeANhTS5Kq3lzH9UCOtPhjf15FjQwQUh32sGmiiEj7x-EUw8AuKoI0BVb0ZomKc_9dxzuTj2tA922CINECpuX8NsL3LCRcAr0O4rMYgUiRAxm2EUo-_ksJVuqd66yMjCfbAoP2AprJnZrKxueIK2PgrAR4IyPIS2lfC4VyuMKB2RrygzP34UsaYuGN3nZI8-k5Tlnp-lMEXTYw9Wypxbanfqd1VNrYnRcrLAyKV4bJb9YdVlstKI6mfBQ7-rO_ka1X6yyhpezp8JgjO4LtVoVHrhXB9Fim1Q6IqROr4-ilGmb7PZ_qdCb6yUMwzExC5e2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دیگه کم کم بریم سراغ ایونت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82263" target="_blank">📅 03:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82262">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">توروخدا به ملتفت دیس بده یکم بخندیم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82262" target="_blank">📅 02:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82261">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نمیدونم براتون مهمه یا نه ولی دلو فردا ترک میده، اگه دوست خودتونم بود باز بکیرتون بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82261" target="_blank">📅 00:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82260">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFeGg68kg_ibVO2ZWrjk-swYOtJJClaThZaIL-drzNTRdJhUONbAHF2gCq6Phix-sHEoR3JZXpQ1S88wAH_fw-DQ7JrxpRi7D8yqa39iBD_MzPw1lgm78bLaPfEb2SsBGGE4ogtgZA5sFlY7s6fEeQLQcvSQ7z17TRvY3gEkY9ksR7n-eUm6gTasBy6JlUSXt8BB2oSOeOt9M2qSuPsb4i5-PGcF8rDrZUd-3VEkLzP_I_qfWgzMOPfaPe9bbkNi3rqeQykDPEF3zsHoYRgGQXjiNkkTn4b1br2ieRssRQ7AZ9M08eGvqiax0i6pFYORXAQih7zICYPlKGlsAVzkZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظرم انتخاب خیلی بدی کرده و رو چیز اشتباهی نشسته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82260" target="_blank">📅 00:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82258">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NmE2AXTyx7oM6JIquaqNh8KU7J-IMiPI3LqlYkRQYlTjY5cOCpGpt2iDmsiu5tvNTLXDtRCbrUx0sl6fU635COsKWHU-wsnnK25DzxoKSRFghYS3FfRm8hxRh-a4FhY6sToSVL2GHdG2LtvX5ZxAjwBGj_I2aVeWuAygNAojv6W3YLgxeiIfOIl-GfF9HWPloFN4MnYK21QsMOFEEOMFGg03VwM5KAFG6jXzKQBsSZjPvB_rrX8YiVHJspUpBUCYsJFYE1MjsM_IxcIqu-9iV1cLU0CS14VOnW5NI9j4RhzeON8MEMd1-22OrUlj1YPBCM3zV8zr5vPum2j1mWFwyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYpa63JfVWjjMu5_AUA-GRs_uaLJSsMoHIeOX0PlIv5-CSylPfnPONRQA8uDlM1aI8O96qKy9PlOMOcnOnmh4TuiQhTc822SW4xI-gSXaLNm7IDJtah8qcglBzhl1le7Rf-M1AxFJRdE-lZC2fqBA0ZC65k8Q1CfGAF9zcASz15FikegjpnD0Wamr1RLUDX_ZXYLSl-H7V-kuVlYQGJmQckdj0N0Tzl_SBSi8ovkxhlFD8bY2XHxv7eFrUIwyAQoiYSbJNSyzKKgFjRdk7xgFOham2H24RMjvuMqnCe3rkAa7hiBmKnEeT_hMcaGVR_WOQd_jhDAe40f0MBGDMnOGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این اوبی میرفته دایرکت ملت میگفته عکس با کارت ملی بدید عضو گارد جاویدانتون کنم و اسلحه بدم بهتون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82258" target="_blank">📅 00:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82257">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
احتمالا همتون داستان جدید رامین رضاییان با کیس جدیدش (گوهر فرشاد) که چت‌هاش رو پخش کرده رو شنیدین یا دیدین؛ + حالا به همین مناسبت یادی کنیم از زمانی که دوست دختر سابقش طی یه حرکت منطقی عکس و فیلم شومبولِ رامین خوشگله رو پخش کرد :)))
📥
مشاهده عکس و فیلم‌ها…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82257" target="_blank">📅 00:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82254">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gicmrBpw7xiMVJG0l3mox0LetMw2ktgr67Rwyx9ClkcW4RKGJYBQ882AZ70dNDNqjl_OhlABmcpqxYHv3bfwcXjUGzZuHoUO9sDTPMRDXi_UEOyWhKRKNlJd6UiOSjMDqhBZti56j7KDfLH9MMRmNFXvRXvuU4nTlexNjLEA6ugRtmah-I4HrHzkpPgEMNEkE54oRLyUgAA63p5lnk_zDpwsjLCwTB8mmoGy_cm_9MQh03KCDslNud5kSgpi5x8fwXilF3QSX3SvdT6ajQlg_rHWtcPS-x9_FrOdCsBBnPwKjablaNGx0ITByZrc88EbeXuq63X9L47sVEm9FSBlyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LneDQ-gZPOaQmFY7JwSGFxmbA5HmcTiFlABmPl7PKZIDG7-TW3J0lSfX1om_2ZmnoVBVzFtKT387mHxZTf1AImxAU8Ks2qIReg3046O-wSHxNf7MhE_M-m0L9h5q_5AlxxJvjQkO7LN2mItjWhlU89Y6_ryLd2ZzEGmll8ITvNxCtpzVjCYF5m3PDWmQyUCON2LZD6NtS5LS5eyKAZU6cG5fBq4PogP9dKho3KEdjyCsEojKzRgw3BlxG8-nZncgkKdjyf6xyDHEhnkMy3KXGIiUyLHTSmlUVXSECqfwJHx5oZsqwvnK8P3ZKkTY3LwrzYR2TaplzfzefJh8TC1WYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FZywgVyqp3irDeujqTwrKj_tJ41jHB9vid8F4AU7RZ36j1nefGga7rtXig7JlS7iV31Pra9lbs7-vE33o-c_yyasAbx4bNgWFfhqj_mdh7SOYHDKXnqbdIkdVr4bYHFWkMWvs4crm-kCNgg0n_n3_MDp2ze7i-QozbmO8-GoFcW__pPObTXlnWmcDilC-mv8NWvvrhiC5YC6VbwlNZPXyu2uFlvA2R2F1BuecCa2WbGbdY7sGkSCZctfyZqIVP2dINW9B50xG9vDBEI3NRSzu4EIV0Xf0uityz6FAotb0ldZ8xw0mfAl7y7qvHryM1jKpN2Fe-Rtzo_j-y5FKQVCww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
احتمالا همتون داستان جدید رامین رضاییان با کیس جدیدش (گوهر فرشاد) که چت‌هاش رو پخش کرده رو شنیدین یا دیدین؛
+ حالا به همین مناسبت یادی کنیم از زمانی که دوست دختر سابقش طی یه حرکت منطقی عکس و فیلم شومبولِ رامین خوشگله رو پخش کرد :)))
📥
مشاهده عکس و فیلم‌ها
@TopTel</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82254" target="_blank">📅 23:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82253">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">روسیه بصورت فوری تا زمستان ۲۰۲۷ صادرات بنزین و دیزل خودش رو ممنوع کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82253" target="_blank">📅 23:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82252">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d727b7c564.mp4?token=A5bQFNjAfhfaZL-U0Am54sPyxbM5Rp_Fv1eD39ZeR22oF-NY5X8kQ26bgFPHlVkddiJJO0ZIHNCt57nbIelHuedZfPNiWsJKOueaeaudWohY29_iM_NNMwR5vAKu-z6yYNniKY7TkECAwZhDmdbfbAYLHkGXRnhSoMvNEiX9JyKJ7f8m2T1VrQONcca0bv4xuRqLipIxx1uJmoOiaimNwWW-rk0XZ8PKBrZKNi_6HN2KbVhXM521pKzje1O_WqZj4hg7cYORQ6ZK0gab-HMGv2tANYLhEz9wrTYIbsBELjS7KIN02dBlhmWauw7KIBpMhG1bkdteS5a95dNdHU-RIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d727b7c564.mp4?token=A5bQFNjAfhfaZL-U0Am54sPyxbM5Rp_Fv1eD39ZeR22oF-NY5X8kQ26bgFPHlVkddiJJO0ZIHNCt57nbIelHuedZfPNiWsJKOueaeaudWohY29_iM_NNMwR5vAKu-z6yYNniKY7TkECAwZhDmdbfbAYLHkGXRnhSoMvNEiX9JyKJ7f8m2T1VrQONcca0bv4xuRqLipIxx1uJmoOiaimNwWW-rk0XZ8PKBrZKNi_6HN2KbVhXM521pKzje1O_WqZj4hg7cYORQ6ZK0gab-HMGv2tANYLhEz9wrTYIbsBELjS7KIN02dBlhmWauw7KIBpMhG1bkdteS5a95dNdHU-RIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کصکش فقط یک دقیقه‌ کیر گوزیدی، چطوری تو راند اول ناک اوت شدی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82252" target="_blank">📅 22:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82251">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">راستی این یارو امیر علی اکبری تو راند 1 ناک اوت شد اونم با ضربه جب
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82251" target="_blank">📅 22:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82250">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سلام فریب جان سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82250" target="_blank">📅 22:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82249">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سلام فریب جان سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82249" target="_blank">📅 22:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82248">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXfKXspcs9QDLxBr5I_z9JikW-aQVDVXx53QC7l0pAmZAYuEEzcC4UJ6_Vvh-BHUW7L_cNT0fFF-0HbPIU9UpVziR6x9hK0JCIn9vOAHwcgXubpUp3DbwPCuuQcwKR1q3VqV012mJpJQPCCQlQSJsnMZ2Q3bzDKsArzfXBgW_wh1d2VodvVRdR88ud2QSEZrCOfV-vgNrBhmxobTMibyZRFJWYIwdRKAD2nU2FTRZBocBiTYxZBxmqQc1rJoaoqZo6QZgyVgpm4gRucVdIf8bQK0dF3-VN8xj82fChFPrk2TDq93kxONGByOndG7ZxxCrpgM2c9l5b8p6wmboetchQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82248" target="_blank">📅 21:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82244">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaj1bHk37v-Bi3MxxxdD-5Q8JLhp0KFWhOISgVpG7leu1YhsbUndYO_fnQFFiS0d_eTCeczwPPr8YW6cwwm6jcViO1aXQyH-3jxcWMIiyeMUAbKANzcnS7VdqXRyiTB1depJMsN-Kn_wzZG0-4vSEZbw6KK9ORsLp_ylOLzZVTCeG1Z7yx2dugBcqYb5ESjY9wjzbShbVHyjy5diJeI82vPOqizcCeC_7QL83xrh0iPpGJINfnD6SXJn3rTlPM9mfR0wni42UnTmJmRAOvKIBmKWxVN2p7DALbmWa1iq51_aLB-GQnx3tD12cEjQHPX-MEo8jA6JAlSEO8fvfk1z6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل نصف حیوون آزاری های جامعه این بازیه، فک کن وقتی بچه بودی اینو بدن دستت بگن کتکش بزن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82244" target="_blank">📅 21:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82243">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔥
دنبال یه VPN واقعی می‌گردی؟
⚡
سرعت بالا
⚡
اتصال پایدار
⚡
بدون قطعی‌های آزاردهنده
⚡
پینگ پایین برای گیم
💎
مناسب اینستاگرام، تلگرام و وب‌گردی
📩
برای دریافت کانفیگ ریپلای کن یا پیام بده: @wizard_0061
📲
همین الان عضو چنل شو: @v2ray_configw</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82243" target="_blank">📅 21:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82241">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AbIVUnhTl6g0J8tpfJY0Bl1Z5Og7ys5_vxIIcS8wVbCX5M2Dz05azLgesQkxzq1wEpJLTy3EyaetNqK44OypvMIxeXlrU2upf4vKSTeOVeIktZIZ5sIBTkcfMc2ZQ9bg-lUwinBV13JpB9r8ewTQneOVVzziuVfNHkNsLC5yl_cWg6gK9h8g7IMEz7QHrdxSHJ2HF91oMO-2bnkDdvzH0rUKfi_l7Y2qoxW71Wk0StGJBFnPzSuJTub0QGIWa40-YOllaVnl0rY3qHNt_aNMlmM8XgbbR0tKhr8nIprQgGApi-cNBj6iQ8EDStAD6lazBJYIFS37h2VxBTJzpSiULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دنبال یه VPN واقعی می‌گردی؟
⚡
سرعت بالا
⚡
اتصال پایدار
⚡
بدون قطعی‌های آزاردهنده
⚡
پینگ پایین برای گیم
💎
مناسب اینستاگرام، تلگرام و وب‌گردی
📩
برای دریافت کانفیگ ریپلای کن یا پیام بده:
@wizard_0061
📲
همین الان عضو چنل شو:
@v2ray_configw</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82241" target="_blank">📅 21:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82240">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یارو بهترین کص ها ایران اشاره کنه زیرشن بعد بره دایرکت یکی نود بگیره جق بزنه روش؟
میفهمی حالا سطح تفکر من و شما و دلیل اینکه میگم نادون و احمقید؟</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82240" target="_blank">📅 21:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82239">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCgove5GJDf6rwIbtUb5j9tGgF5QabIe_zuO277k7MgPl9yyehacjBIFVwzf9Ec0Qat5O7Lp2e4agJYMNQ9dPVbrDuH7xqYwlyOzJCne93PEyxiS3eEAcfkSna8IM44cBok2xvdXtmLJrDMKFVWTOyNdTw3hxAiJvK3V9oDz2dYoSSVTKfDy8VH3V0JMXlO7gUnYBS9BC8NPnyxcHdTjiENpidaHrv6VJWN2w4gLT0kCfDqtQqN4GAtoTigykHZtpWgTDXdpeZJjrbcVlinmG4GZr90JvRQ9BrnRBjCdMyvP1BY70UBWgm6WuUKofkV4C0PvEb5EWqpuVHLnMmkUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه همه‌چیز رو میگه و آبروشو میبره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82239" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82238">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پرسپولیس تارتار بوی سه گانه میده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82238" target="_blank">📅 19:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82235">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QZIWXUT3q3Bhvs6TK1qtqSDaouFPNQSUDfOMbAcV3PO2s7DDF6p569ad7JObdNQ4MkzTnuONCdCPm6_bT_Po0rw5ipftN8oYr-LOQGqheTqbNJCApcwK4PTW_yZTeehs28mqZxBrzClwtBKqzNd5C4T7CfJIlb1J27jFqSEX-jswZKnEglaYZVRbGNR0dxrXSi71q5Z8m62nUKYm_Y61Pva3noFZjAuP7PSeXTfi-PchoNUV9W8_4xAXICEoQdJlYGrJAjp3dMpNlh0n1yUSgznDD-Df_sAamksmu71sol582k_BU1g_YGWdK2D-tR0kSAl3KmA7ES07hSOE5q_QOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5Lk-vudGaEgWDvJqsAil8Y0SIWufGXke934-4x4MgRgTbX_FulYjy-iYCkCAmjIEpWC4A6yi6ICleMul5lfsXfjylqbZXiM0x3oQKEXsYDrzJY-5uHTXrKP6jbbb4G6Rq3bPUCK9iC25_LfJykUe8uuYy-DMwSJoa-h54NeGlGL6Ug7pbCmaXj5YSyYbaYcyZOL8DnbpcJzdC4d43gKMHKfpUL0Z4V9tKB5N89l0nMBoWs_r53dpOtDxAExZ7hKP3OVj1HUPVTMKFXh4P0zaDIqO2Uc4es0Ict4ZGbnCRRvbLXbAK2NfFQGjX1QqSjV0h9BVvj8_L8PUJ1ZFswqIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-H7k0EI7gd6ArAKdS4y2POHgJCogxIEcWd5mS0gkqBGeX69toFdSQ739uzxcrMTHKBUgXAfSSf52m4__lJ-1dX0SyADYcrm06UyPf4TgHh-kj521AzSCkrqX2t9JF5aNG_nJWugOMv9OGgWKtezTQ1Rl9MbL_xmt4iJGIH6xHMpgaSQiGng2Esjwc_dPpfrD9mZH_QNRAqPLfDEK8oC3Xd75gq40xVbfrQwBvTufbxsrhLrLj3bdC0T3kfuHLCbxb0QNsIeO84Nnkp3N3ZvlfgQhck7CpkEs-Pr4UVDEyose0VQo3NKCJYHRzjIujbridB_5YnpKMolk_K7W5m6Dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">افغانستان
🤝
فلسطین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82235" target="_blank">📅 19:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82234">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8lEHcALkIKNeZXNrDGhqwTB4MiLX6rooo38Z75UyYNwjqZw4OJs6Gd6NdW4659-zLidnT_jdbaWhpQQ3UQr6FAHucJ9MPp9FFm4ZMN8JNZZYcT6_SpxeI7t2pN5t8y9O0bAgh9Qc7Hrt3U47HuPOqN5pr0UsECqpmozTyedl1uaV-c6Pq75FWDVzQSCQE3rW9SA8LYpFhmho5D16GNPVD6xBIiZk1hZ4qFsw3yimmcFoP-6HgFHg-_lvFytWLurhXiziaWBxQCVR3WFgYgpwNYwDvccWzrCuzXesY_SNnUZpf1vUHZguygI3yPIo8f2jDPCEC00dGDkyMo03khHCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه دیگه محمود خستمون کردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82234" target="_blank">📅 18:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82233">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d93334e9d.mp4?token=mr_itw6brPxxYRS1gwuwORRG7qyIAU8-ewkPLNp_D8SVQZdBfrXqRil9p2jaYvqPw0Tc6MgvDw7zodoQvFvWcJjpVm2nblGVB5KSlmGGhELrblLYZQ-ewrL_BdO7sRcvpSc0z3dTMQf6WhDQ2I4SWtnLD6JVKKRwLyBLG1mLP8GFhn4FmoaI8sBKXe90pYMoRD7ZmhJA0LJXwsTUA4dh9e4c-OJ7yqO9TOuvOeiYc-Bhs8o-_0xwNXiYcD89IK5r5hunn5DU4BXs74vbQz2r4zF-Ar4iN97F_bZm6UpTK_FVA9qTkBznl8cIApPCEbNGqwJraZza4TuXDhmiWwxQEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d93334e9d.mp4?token=mr_itw6brPxxYRS1gwuwORRG7qyIAU8-ewkPLNp_D8SVQZdBfrXqRil9p2jaYvqPw0Tc6MgvDw7zodoQvFvWcJjpVm2nblGVB5KSlmGGhELrblLYZQ-ewrL_BdO7sRcvpSc0z3dTMQf6WhDQ2I4SWtnLD6JVKKRwLyBLG1mLP8GFhn4FmoaI8sBKXe90pYMoRD7ZmhJA0LJXwsTUA4dh9e4c-OJ7yqO9TOuvOeiYc-Bhs8o-_0xwNXiYcD89IK5r5hunn5DU4BXs74vbQz2r4zF-Ar4iN97F_bZm6UpTK_FVA9qTkBznl8cIApPCEbNGqwJraZza4TuXDhmiWwxQEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدم دیشب یکی از هوادارای استقلال داشت مصاحبه می‌کرد که یهو رفیقش جلو دوربین انگشتش کرد
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82233" target="_blank">📅 17:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82232">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B55Y2hvw9Iuz8GDSVlfrsHuAnmSuW08NMy1vsX4Oon2xY0-x3vr9UjQcOSrLM4Lpb0MnxMfJAFOe2gbrElqZ6Enniih_m3ngE0EHDkX51QGnQKUtuxJ_OjsP6n7sJz8YSjnR5X_XjMZDSAgEE8noIYsGOqme1cRLBgPdpac3WbTNOcPXUYLXMqJhZbGILjkEhxOGVyN0Hu4lDb9xfbEPzXFhuh9ECLWNnxx1BGTrKRVHWz4kBQli9AddAZfZkt6zw3Mky01xhdXEg0L3gm7Pph-6rysoXdWP7-4eD55UAvbBghgvW8nNymK6473or0yiu7uQzh_EpBa9AiN6CFhRsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
نشویل - اینتر میامی
🏆
لیگ ام‌ال‌اس ایالات متحده آمریکا
🇺🇸
🕔
بامداد یکشنبه ساعت ۰۴:۰۰
🎲
با بیش از ۴۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📝
حقایق مسابقه:
‌
1️⃣
اینتر میامی در ۷ بازی اخیر خود در لیگ شکست نخورده است.
2️⃣
اینتر میامی در ۱۴ بازی اخیر خود در لیگ حدأقل ۱ گل زده است.
3️⃣
نشویل ۴ بازی اخیر خانگی خود در لیگ را برده است.
4️⃣
نشویل در ۱۰ بازی اخیر خانگی خود در لیگ شکست نخورده است.
5️⃣
اینتر میامی ۶ بازی اخیر خارج از خانه خود در لیگ را برده است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r24
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82232" target="_blank">📅 17:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82231">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXwcCKlMsTtFAbUuGZ4oG60m2fpsEIkQ0G-WsiOtOOG-1OHNrT9yvxE5VtyFABupMlaNdz60yhRTPFO6L7Tbm4EVb1SflAYEPHZDbDfVd9bPX3GgtHmIDGsSqlYm4ejtjvDmp3Foqpn6XNAhkFZTIqPAE_hLsRbFyhAxYIOmnNELFSe8t9oefZ_KnxDMz_lgtbxLJVAGa1pr8hfRWvS_Pqji2ayKZfXfhsPC4O5v1Er0gv9g8oBdb8f2Z9m3oxcPR6D7zn9ze3GNqxnMO8y6nfmJ0xKNpWMGa9r2uRZXPJVEga-7taTL0PNDg21w6MhBPNi5w5MGOxNdAdoQVjClQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده بعدی توپ طلا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82231" target="_blank">📅 16:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82230">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حال ندارم عکسای خیانت بیگ شگی رو بزارم برید چنلای دیگه ببینید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82230" target="_blank">📅 15:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82229">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تیجی چرا آلبومشو نمیده، گایید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82229" target="_blank">📅 14:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82228">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گزارش اسنپ از وسایل جامونده تو اسنپ تو سال۱۴۰۴: ۲۶۱ هزار کارت بانکی، ۱۷۸ هزار کیف، ۱۳۷ هزار موبایل، یه کنسول PS5، لباس عروس، ۲۷ هزار ایرپاد، یک نوزاد شیر خوار.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82228" target="_blank">📅 12:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82227">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=j22XPvtksDGZfCL01JdHFrRBqjXVTx_z0krfsH_22F_HHieDYUg2aH6J34vM38TiiE9pln5QC8LUEZmMASvwaXb4RfUoHjdW0orqPtxGt6-XCBLCZ0sgARPZfFH0q_X4VAvS-witqvtnpquggIuAmglXIpSRJLdo4qC-CN5gdBs-8shDeQOC5f3aF9hi3oyJ8h7yKkRaaz0zFrmT462cRiMy6Ndt8z_k_RegyjZqVkgFYcxMM1zzsiwsXc7itFixyQan28B8k7XmD9Tx8iuUruQfj0lVyJHcpxFleJUO6soCoDxsMdEVSrxFMRI4lkTAc-w-Z74Lilibz9al4OupJ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=j22XPvtksDGZfCL01JdHFrRBqjXVTx_z0krfsH_22F_HHieDYUg2aH6J34vM38TiiE9pln5QC8LUEZmMASvwaXb4RfUoHjdW0orqPtxGt6-XCBLCZ0sgARPZfFH0q_X4VAvS-witqvtnpquggIuAmglXIpSRJLdo4qC-CN5gdBs-8shDeQOC5f3aF9hi3oyJ8h7yKkRaaz0zFrmT462cRiMy6Ndt8z_k_RegyjZqVkgFYcxMM1zzsiwsXc7itFixyQan28B8k7XmD9Tx8iuUruQfj0lVyJHcpxFleJUO6soCoDxsMdEVSrxFMRI4lkTAc-w-Z74Lilibz9al4OupJ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش اسنپ از وسایل جامونده تو اسنپ تو سال۱۴۰۴
: ۲۶۱ هزار کارت بانکی، ۱۷۸ هزار کیف، ۱۳۷ هزار موبایل، یه کنسول PS5، لباس عروس، ۲۷ هزار ایرپاد، یک نوزاد شیر خوار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82227" target="_blank">📅 12:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82226">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31aaa49746.mp4?token=HTyHIheKoVF5N4VdwPNyL0e2rdZiEsAr_I2r5dzbsILR_7yhgvRNFv1yXxHLl5rh4nZy6uHZSiLPmbOx6B2B_CGCm7OWtNxLNShJL5f4PkhwEJvv3PzcvAVC2r0i7HZ8N__tlyO6fWgjgxv1zx33ZdJREzZQs7aKUKUT0H1BgObKmxbDqAbnPxU7zNFEjKzd059EQawgpA67tyj1TqJ7MqB3ULUO9J3dVWkOK682J6Y8WEBHN3hjUt6ZhOPZ-NXu9PHvYweArZnyRY_UsyQY_MdC2SaGeqEzFpUFRylJsQXSKdFkZmFXn0Xkj6xbBt_MUXJNyKnazZOTQl2TP-aPgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31aaa49746.mp4?token=HTyHIheKoVF5N4VdwPNyL0e2rdZiEsAr_I2r5dzbsILR_7yhgvRNFv1yXxHLl5rh4nZy6uHZSiLPmbOx6B2B_CGCm7OWtNxLNShJL5f4PkhwEJvv3PzcvAVC2r0i7HZ8N__tlyO6fWgjgxv1zx33ZdJREzZQs7aKUKUT0H1BgObKmxbDqAbnPxU7zNFEjKzd059EQawgpA67tyj1TqJ7MqB3ULUO9J3dVWkOK682J6Y8WEBHN3hjUt6ZhOPZ-NXu9PHvYweArZnyRY_UsyQY_MdC2SaGeqEzFpUFRylJsQXSKdFkZmFXn0Xkj6xbBt_MUXJNyKnazZOTQl2TP-aPgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید مامان ددان تو اینستا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82226" target="_blank">📅 12:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82225">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خلسه میگه دیس خشی آمادس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82225" target="_blank">📅 11:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82223">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a989fde7d.mp4?token=DpNXHEAyfGbJiVF5rEhCmlOYn3I8br_n5s8O6Cw45kzGhi0ZNW5ps3BgpsgIUb7nmIUOLek0CVxKwxsf6fN-vil4fY8BN7IEQBMBVr_H3kpUJspeT6ZhgPoQif62pecDuL_tefHgWpsIU4SUCyqa6KGU-X-DurvSRX9BzsFHmhzpGUaFJWblAlWIis4p2r35hMtQxEuGl5Y0xihCua6ItIGqWaOFVXUsQzBouMXDFJr_cyY6yxIdgbgcLhYrnQ-R0sKcsILQpzxfurnbDxWi8496AJgRFN3uy9S1jLPzMtUkufofUSdIfFwd--2S2joZCi7wcNGupOC2zmFWY2HaLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a989fde7d.mp4?token=DpNXHEAyfGbJiVF5rEhCmlOYn3I8br_n5s8O6Cw45kzGhi0ZNW5ps3BgpsgIUb7nmIUOLek0CVxKwxsf6fN-vil4fY8BN7IEQBMBVr_H3kpUJspeT6ZhgPoQif62pecDuL_tefHgWpsIU4SUCyqa6KGU-X-DurvSRX9BzsFHmhzpGUaFJWblAlWIis4p2r35hMtQxEuGl5Y0xihCua6ItIGqWaOFVXUsQzBouMXDFJr_cyY6yxIdgbgcLhYrnQ-R0sKcsILQpzxfurnbDxWi8496AJgRFN3uy9S1jLPzMtUkufofUSdIfFwd--2S2joZCi7wcNGupOC2zmFWY2HaLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلر فیلم Avengers: DoomsDay منتشر شد
۴ ماه مونده تا انتشار خود فیلم، این یعنی تعویق
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82223" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82222">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKuyvOKuGBxYeQCnG3zOsuifBcTh822S_EUjqrvBKSTtKPRI1dvxGzGDs42Rpko-bCtx94eYgHyVK5IwtEiCOmX2jQOxWzzB6yDq9dpPkO6a-XFj_fZ5nmTfU9euw7j1GIHgvYAbQWJT2j34qPgS8dSTQJ7islMLUMYBD-bDAQxR9CWL901qyOjSEInZrfvkMnbDeAjY0eU3ge2aADEU_Rkc1gU8B5kBagJsbnLQr18tiFTAVAeo4T8jPamnRkt4IK1RIvGqrJJ9DxFxlVs0bHw1tk0zL5Vwtj3MMPZ5CppL-JNzGUtHqzSW_pKp-5A5KE8-8qL9-64XnUqU9MXdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری شیپ استیلر و کوروشو کجای دلم بزارم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82222" target="_blank">📅 10:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82221">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEFFN67EEOvdMpdfSox0xRU0CEGIc83VR5ieEkYXQ62o34VqBZ2o4U8Gns4SJtPmz6r_J8Lg9yB-qLguLSsQkSAoC6h5-HMaIiw71Pz0Ywn2rfOL49rhdgK1712S0W95ZcbTsDbR6wLeksoGFScFsdMr290FVDDM6GM8jZvDEajQyFZAdxKuh23sukEWk4p-EBLfn-F9u8RSJRcv-oHOv-OsuFJKGpS-bi3cuGBs-l1rTIglkHV7W6k1xi9LxqGgweU4bsaX1oaMB6GczP869AiwGpzINUh5VNP2t05lEO-PZ-t66wUGr5UKmNoA-cxRqGArGNFu0TlCuVsLIbRYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
نشویل - اینتر میامی
🏆
لیگ ام‌ال‌اس ایالات متحده آمریکا
🇺🇸
🕔
بامداد یکشنبه ساعت ۰۴:۰۰
🎲
با بیش از ۴۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📝
حقایق مسابقه:
‌
1️⃣
اینتر میامی در ۷ بازی اخیر خود در لیگ شکست نخورده است.
2️⃣
اینتر میامی در ۱۴ بازی اخیر خود در لیگ حدأقل ۱ گل زده است.
3️⃣
نشویل ۴ بازی اخیر خانگی خود در لیگ را برده است.
4️⃣
نشویل در ۱۰ بازی اخیر خانگی خود در لیگ شکست نخورده است.
5️⃣
اینتر میامی ۶ بازی اخیر خارج از خانه خود در لیگ را برده است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r24
💻
@BetForward</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82221" target="_blank">📅 10:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82220">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">من بعد اینکه فهمیدم منو لک لکا نیاوردن:
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82220" target="_blank">📅 03:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82218">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MBWgsZyWdbEonRWID7COUUe77LBWHfTzFvVv1XXydOv5raC1KwrqC9bA7QEPQVar7ib3RpDtWpz_me4HiyTUflyg5tfwvFp2wkbO4469j-gBtHW7preBm3q6qchgloQ4OQhVwXYyAlLibQECOQvjfJ4U4xktstr7yYorMPyAam32uXfd4un47hse_BhloGrZmikMUeHFB_74HPzCuaWN333ZX0pZjSbjy5KIYXjmMY3tuZg5lKGhbHpT1NPrMYwx8dCAjlbv1R8_weTyFqX6t96RbnLPUN7V48-rKL-5xfTGubfSCtIVPf1WY5C6G9mSrKy8R36ZIxXInIw2suMIbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYF9_zoPCim8AdUpqJazU3_pBGFLdnJRcvAkZPiSua8sjvPiLYxEILJSMkteZr2c_6Ny04dq-9u0eAUzUY-LxUm4uvusTgAxdcixj3naj3ZHNpT9XADcLuYuZK-ydQgaTw_KfX8tWRaZruMq1P8qKfhPqK698s7aowKkF_rc5muLJ5XM47Zi1LadzZJkvEVEmzti4jtKMZOpx8ki3bvhC5v5kvHrvPR9Sttkdu4wsiP5uQpwA8IxkfFpmTAOAn68Rp0hBDAqv287_mntWqrdz7ZdmjmYFmhla6uoUun1VGKL7ub1p1CQiDbUG1Njit7N-ST9j_n69VP_vRb_s25UWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آخه کی ظهر مست میکنه پوتک جان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82218" target="_blank">📅 03:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82217">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6oARNXKHbT6Ykx_cMJe6bZHyWRdSND7iRw64lh0YVgVh1pZAUGrcT_cON5_l3ebvDfHC2Pkm1d-UwMNeDIeZN-Fb-rFqMow0gqTSI1-DbScrTEdcsgHyx0xh2v_Afrhf_r5pW_HTIRGHh_IiAWZfYlZTyGjaLzOfI-qAfXpoGc6zOpQwc5FwiGjXND2wwp9oMPbadAwgeD7oas5-El91Z_pjGzXplJbiUTeBcRxtKlOtWn6Rr2-Ue4pXrdBr4h2Y7HRr13fODFQleeqOxuSTc5lKToaCNYrVP2pwQFb_MGORIbPcJCrssWlGvbYG2JykUDKhptseSpA1UKrUm8quQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته بود: بچها زن نگیرید، خوراکیاتونو میخورن استیکر گول زننده هم میفرستن هیچی نمیتونید بهشون بگید.
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82217" target="_blank">📅 02:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82216">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ: تنگه هرمز تو کون ملانیا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82216" target="_blank">📅 01:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82215">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiiUoaPm4Bfq6dTooG9yM3hw-pvVIWBFmm4etUuu02uhHg1koReK0DuQXhGPntSNKhMaDGw_G-Y-PDWx7pBGA67QMpzIn5sPhBFrx96BhEbtFqo-qDR457zOi3CefHU_RUAk7UDTbviOP5i8cgMu6By5EostZTxpXth4v3o3q-dty2CqQe1Mt_J1MZ8iWz_OvudLaCN0cAXC40yK_vpTrff6ITcK0W2eiEG60DdgOBt_66pthbraeTJkXr08JSLyAVszUmwV0QnnvPDVtHdQuHzu7bmIxL1Jho1P9vm0t0Vngrlvc-Ydz5Kmy9EYOGhVoAc8Gc6Ww23VsfVFolHXWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا همینقدر موجودات ساده ای ان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82215" target="_blank">📅 00:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82214">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پاریس یدونه مهاجم از دست داد سه تا گرفت، بارسا دوتا از دست داده یدونه هم نگرفته
رئال یدونه وینگرو ۱۴۰ میل خرید پاریس ۳ تارو انقد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82214" target="_blank">📅 00:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82213">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1OUf_S_EVbTv-Cq2QreNMzwSsIxOB2k-8MUSl4y9wnvxeCPMVcMpBP3woZgBcdCfmxiI8U93ncGDWamrVdGt9pKy8ZLTMRT0zgMrkBcm7pb-HjwU9k1lfE7DMu-7WS4huxPfsKfWC-04loyOQ52Ws0XRbecA1-RJViZqdbS362b4K0rWkD44YUTxNLHXlVWO77wPdMGuzxXpfb8egVMAD029VEEo5NruR2dDqBu2IhXOpIEsGMW-fE80rZx1cm7njdSz79USRs7AOsevBzen1jvYKsgWR26qyLvcGqCf0MsHFAGL7PimeznUCPhs9CvDv087LRPRcKwqO9f4YqeSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش و جیدال تو یه حرکت انتحاری مادر ددان رو هدف قرار دادن و دارن یه نسخه دیگه از همکاری هاشون با ددان منتشر میکنن و نسخه اصلی رو از پلتفرما میکشن پایین که کردیتش به اونا نرسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/82213" target="_blank">📅 23:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82211">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ به فاکس نیوز:
ما یک ضربه اقتصادی قوی به ایران وارد خواهیم کرد و برایم مهم نیست که این قبل از انتخابات میان‌دوره‌ای باشد یا نه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82211" target="_blank">📅 23:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82210">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3EdBrUtVEuc08UVuxW4zNPsC02cFCeN3UB8oeptgiw43yvtFtJYtXucLIGhnVq7SZpgJlx1Ztc-cMAfPnYN7e8NiFS2pF11sn2B9uU1IKq_8jJZ_DDPyEPQdeUIhSnfX-SXXQM8sgGpLGHsNOJcOPM3cUefjl4Pw7xkxDlWtdCZYbE5vMPndQ9mNWEvHvgZ9flflm0MJk5iWxPwpGMipWvmTu4yw4LuRNYnZ83YwV1XBtvWj5J_NzQfyEug1w2-v5J8lqPaRNDAPdSJqQP27k-Co6KQoq_8sC5GENhxxdanXHEKJEbPAvD_vHnqoiaOppNfUw9Ou9vsZCMwi2uzVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت کشورو تروقران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82210" target="_blank">📅 23:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82209">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/407c0f01c8.mkv?token=UDmSdrmqoPJ0ylT-8P5eP6_sQdoAYjRj1A9d4wG88AxilcBpLZLXbziwxdRxPsRwoiFqmylrMkPAG7BL2lZq3vGPj0lf7qbp3ZwMHisUtaCht1LDc8hQXHqnyhFVvEC6pwz5Oe6y0tCpcR2d4YM0gP4jD_3q0Ve5GJhmFeY_H28WGKE8mXMigG7OxEPBwUxZzYlGozWrbCVa1smrQfPPY4h2talvgeTdt29Ry0JOYF1DzWyitveyM-Vuco_tBGfu982qV40ndlpdyty_EbkqarfknzlZ0QpcIBIj0SJ3s064yr0Cwp5xuEmLmo5Ip8Nm0b8ONEsGfPGSHhGYQJkftVInnX3gz8qyEixPPYJqpwkGfk9qW3J1hbCBi0LdkrwUIUzsV0BT0pDMYiKeSscEpxCIJWhF6BY8TIF6n95F9eeI2Rx1FlolIk8YZn6kH0vTk6WVta244taVlkkxl0NRaay410h_tuLCG8uBaysVdrsG0KMzoMP7hra2hP4-JiZVwsggtYWOvIcBZzAa_XBpbpcz1CdRDWon9_feqTtVhUO94V71Hh_mC5z0QfjpoILtLsTk-FkFLWiAVvTLnotk0-eMhlFteq_Ge07hFuZ0qKoixyCSRii8RWkIq4ftXjbrNdh8ssiIKG0mN0ld_EwCuWtTAwFpmFT4chytcpD0wjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/407c0f01c8.mkv?token=UDmSdrmqoPJ0ylT-8P5eP6_sQdoAYjRj1A9d4wG88AxilcBpLZLXbziwxdRxPsRwoiFqmylrMkPAG7BL2lZq3vGPj0lf7qbp3ZwMHisUtaCht1LDc8hQXHqnyhFVvEC6pwz5Oe6y0tCpcR2d4YM0gP4jD_3q0Ve5GJhmFeY_H28WGKE8mXMigG7OxEPBwUxZzYlGozWrbCVa1smrQfPPY4h2talvgeTdt29Ry0JOYF1DzWyitveyM-Vuco_tBGfu982qV40ndlpdyty_EbkqarfknzlZ0QpcIBIj0SJ3s064yr0Cwp5xuEmLmo5Ip8Nm0b8ONEsGfPGSHhGYQJkftVInnX3gz8qyEixPPYJqpwkGfk9qW3J1hbCBi0LdkrwUIUzsV0BT0pDMYiKeSscEpxCIJWhF6BY8TIF6n95F9eeI2Rx1FlolIk8YZn6kH0vTk6WVta244taVlkkxl0NRaay410h_tuLCG8uBaysVdrsG0KMzoMP7hra2hP4-JiZVwsggtYWOvIcBZzAa_XBpbpcz1CdRDWon9_feqTtVhUO94V71Hh_mC5z0QfjpoILtLsTk-FkFLWiAVvTLnotk0-eMhlFteq_Ge07hFuZ0qKoixyCSRii8RWkIq4ftXjbrNdh8ssiIKG0mN0ld_EwCuWtTAwFpmFT4chytcpD0wjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلر فصل دوم سریال Mobland که ۲۷ شهریور منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82209" target="_blank">📅 22:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82208">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6Fit9_JXakElfTnFRPEKUzmA8GQUIyM1_rDizyZfvRKoGHcw0Wc3LrRY7egixDdl5_-Nou1ZorcJKKXKXYIGp1EgEK_N48vc4xv0Ce4W6enynB0aHW5ZOXoQ3kHpfDxeOHITqWRdffYp6tYD6JdBaUGFODr_MNi2YBFNWsuLBry8SgDQySHOm8W_8JvQlTgjNasQMcgu7GpQ8bjtzzy8Xg41dJXO_1-aHPBW8wvSyxOaTCF2_j39TvZQu4WI43tCl21tNdBQRPDhx9fG-g1H5x-hQXDsBdV6_thc7STrjS409FoRPYH3DSDdisspWH-5Ne-nvpSwOSE1E691yGyEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم نفت رها شده در اطراف هنگام و قشم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82208" target="_blank">📅 22:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82207">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مایکل اولیسه :
با تشکر از رئالِ مادرید، فصل آینده اگه مقابل این تیم گلزنی کنم به احترامِ حضوری که در فتوشاپ‌های این باشگاه داشتم خوشحالی نمیکنم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82207" target="_blank">📅 21:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82206">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بازیارو
🔥
جذابیتو
🔥
گلارو
🔥
@FunHipHop | TemSah</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82206" target="_blank">📅 21:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82205">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSFAwyDX0vicW9UBpVQDrfxNzTigpkxurppFLHfpyrDAvKH3M84ZapxApmiWTr_oXWwpI-GegyILUUVGYAmtsHoqTJY3eR78UXrXe0iwwt5fr5cR0SEw0IpCt5-BQji-FeXtOG3zaB_PTlMj2eCND4Sq1hSapY9JE8bbLvKNlEmfjiQvaX7mNn3SXD2acRE0ayBsaCW3bpZYVM3Pg4FF4t2lAajMhVev2hUv26o9Y0c5j-R6Umjsv_hSokDpQ0knPW86eCN5w5h4SrMDtV6Vsqtx6bf72Y2DGyVkWE1o38_LNSS2TTqQzGfvuGNADS3xoXmHQ9Kds-7S-6QIjGfdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیارو
🔥
جذابیتو
🔥
گلارو
🔥
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82205" target="_blank">📅 20:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82204">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLjxdmMsFGcrSUhwtdiVTvs_oPk3Ms9Z6NuHZPTa31nv9MCYyil-lqTSNfrlOoPBTUO2bSIJnkwUW7qKz58v27D0KM18HOFHWp82n4lAHoup6-Q6R67R5435fT_lfXoBeU3wtUiQLSlaROGZcnvAeVY_9BIgMWkdc68Pp2eg1lYDLZtwrSfOctMCV4NSmUQuJLsPH9EA_HcWKyoCKTRE5V_8syLcCAXmCMBGR6JN1q8EJeP54qi1rFfxDNEtvilGRquHoiV9ZcV2fAPavW998DFN14LFB-i5mfykCV-J3TgRXH_cTe4DqNWSCJpppdXLNMmhYC6VhkHTNepx2OBgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
از نسخه افغانی دیجیکالا به نام افغان بازار رونمایی شد :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82204" target="_blank">📅 20:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82203">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aT0tZaYCLkybqMCe_ivwUHwJbARcUrSlURV_eYMIJ3VBsTIJVuAIuqnDVhU9Hakx5-2tBNXwEpDP_nlbFECPn88sAGLr88CXPdxDL--AHXig8Ed8BazCisniUxUb_d0cvBowYQ45qovhBRdbrs_wd6qJIKxgYQ-j4LIXDJ5zsy09bIpjevffggZi5K5D1WXS672nzTFIx2NFlqR_Bqo5hSZuDupMGjhTmXj9biMz7dQlOaxDSUnRtSermbuQQoO16h2hhGGYi0fNnLK9p8L_a6ojojMf9tXZ4NURsidjHwZeC4vmbCjZSX5ylu0tcYcLaHwBzuS5xDaLSC34sE4i3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قسمتی از وضعیت جامعه از زبان پرستار بیمارستان :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82203" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82201">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ بزن که باز این لیگ کیری ایران شروع شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82201" target="_blank">📅 20:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82198">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrIAFuvHyLSqHxdzZKFacgqkwBrt-Esl524Om_QwRGsDHv6lHhvMKnik3WSQ_1kr3a1xopkHMsauWZjDu3vupMKk90L-4fdH-KPnNAwjzOIRarQzakwm16_Xh6QWPa0NbO8AG5UBPGFAn62TJcQPSeACps8hRdw3aojp2OmEh3NFWYKignHxAOrGzH9cFiW9DWYcMs12zMGWzT_p9gD4NCRE-VfzYXgvr7lzzBrPM-Re5ApfYWCOaYYmVd5181qJuBUFeMk5Q8c3z1ALkXM3a7HvmhB5lNpbnVmdb4qrNOkc8gCCLX5Px98U-tzhzAm8KCixAJ1Wf6J43nvrzoQgyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82198" target="_blank">📅 19:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82197">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daLvOD3kJtjeJQLImvx8YgdxD0Bf3j2dtEvQMLBo3sICuqf7jF3RyXFjY-kpElkRclAPFZNJT-d9Us-VIrAEm3Fv81cX0gMaD64T7JbeFKP69Ld1qMV3GEk4rKwpiGed4D1XxeU6QBe6C5pqzAlAw0gqNcZquLwEuVGAFGeUSGwD6RKYXinM5mbScyZCxERGwdEMcOmyXkC45_vuPGec1cPMWF05oNrIqL4GFzIzfuOnQ46NjxTh8gtb0O6CDMY2WDxRYt090ZKSU68YquTtDXqce8U1iGu_ds_QxIkFDPZ_b_VHNyjvn-EQstsKXNWNdmSNV9CFhX5X8w979dd9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه قهرمان‌ها شنل نمی‌پوشن
بانی بلو گفته موقع ضبط فیلم سوپرش با 1000 تا مرد تو کمتر از 24 ساعت، وقتی یکی از اون مردها شلوارشو میکشه پایین، بقیه شروع میکنن به مسخره کردن سایز کیرش و بهش میگن دول موشی ولی ایشون که تحمل همچین محیط کاری سمی و تمسخرآمیزی رو نداشته فورا دستور میده تا اونایی که مسخره میکردن رو از اتاق بیرون کنن و بعد به اون مرده دلداری میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82197" target="_blank">📅 17:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82196">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDz5Nm_QGr0ta832TGUWyN6sQoOiFhK96EQxuJFWgHTdo9duDd92gDLPQw4lxRrHvJGWW9KCPWTkUfpUZmVPUfdSkfQ48HiN_ylcI3hi0DfcLImQZFWqm3q3-3AFTxELzR2Cd4vN8K4aQ1q_G_OGPFid_ARyB-Xq3dUIkyxpnpVY0ogMzGPno_QYEeif0buoCzyaRFQ85xiqryu9_CJIS4MIxIDGudBxdy96I69eze5_51H5f0dXLz8y-En4lW_XlhEtmHteCkKS29haaEEkJVY8JrUh1pcgd09XQvDyZfYpY-gISlRzv8rxQeIkhzPFLCBm3f3B30rx07nSlV8aEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس اکوادور ۵۴۰ کیلو کوکائین کشف و ضبط کرده که تصویر هالند روشون چاپ شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82196" target="_blank">📅 16:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82195">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a38487cf4.mp4?token=ZKlEmLYNwHEn9Lbm_Vn_HxigtHwZnRau6PwQiFM_pRwM7YjKs2lrWdVvQhUyjngbNsxYvK1M1aIfD8_ds8sosoMri36AVpVPVoy_nrvqe2S-ufE-v4YmrK3ULEKtzvrLofpxBpY6iytvKwU8j4nRulurTH5GQovauipEAcZ1GNUzWgVf3HYvsPZO3GiNXosGC0PfqIaNb4XsxzXlKY_G96xUv-slGHwzCx_Gf7BcdPATt5kGWQGkaH3rD9_L680puRAbfmCEcQbE45n7nQ6ydGbksZoS0aCRB1ryZ4dj3AT0e68mYRughs6ffkvgPITlPji4TMz6jpwYa-r3WOKMNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a38487cf4.mp4?token=ZKlEmLYNwHEn9Lbm_Vn_HxigtHwZnRau6PwQiFM_pRwM7YjKs2lrWdVvQhUyjngbNsxYvK1M1aIfD8_ds8sosoMri36AVpVPVoy_nrvqe2S-ufE-v4YmrK3ULEKtzvrLofpxBpY6iytvKwU8j4nRulurTH5GQovauipEAcZ1GNUzWgVf3HYvsPZO3GiNXosGC0PfqIaNb4XsxzXlKY_G96xUv-slGHwzCx_Gf7BcdPATt5kGWQGkaH3rD9_L680puRAbfmCEcQbE45n7nQ6ydGbksZoS0aCRB1ryZ4dj3AT0e68mYRughs6ffkvgPITlPji4TMz6jpwYa-r3WOKMNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدایا ببین من نمیخوام برم جهنم، ولی یارو اینجوری پوستر درست کرده حق ندارم بخندم؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82195" target="_blank">📅 15:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82194">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بنزین آزاد قراره ۱۰هزارتومن بشه، فدایی حرومزاده رو دیس کنید همش تقصیر اونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82194" target="_blank">📅 14:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82193">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbcxIJOzF8K1UC82Z2C9j_TsJ6Fw4fZeMJbTuFlf-w3l-QvZNmWtNkMk1JiwTgmKuuxqSvLgChoJushbEUDN61xP8Zt-GEkpLAbXTI9Lll_KREa_h3ex-k-JZTGp5VORSYstG6nWkgYXrcL7vVEzahX8POYg948s3ursHabGuHtKl1w_Ro9_ISqGYvkacbOnJFVZhLQXhjNUisCCFKrATUM2H743S6dmsY88GBeeASfPxJwrNq5SKZ1kJTRV2Ceg_5z-eb4gncYGrz0a54zfpknjmwpMGMsq4NI6X5mRLla0EqP6VVxlPSC_o2NytBgDhSVGdsZfAZqZmPBt_sPf6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیش سال از این شاهکار گذشت و اما بارسای قدرتمند اون دوران با حضور مسی که نذاشت بایرن گل نهم رو بزنه
🔥
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82193" target="_blank">📅 14:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82192">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تو اگه منو میخواستی و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82192" target="_blank">📅 14:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82191">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">7Khat – Maye Bede ( ft. Hichkas & Makhmase )(2007) - @SCDownbot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82191" target="_blank">📅 13:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82190">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Maye Bede ( ft. Hichkas & Makhmase )(2007) - @SCDownbot</div>
  <div class="tg-doc-extra">7Khat</div>
</div>
<a href="https://t.me/funhiphop/82190" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بخدا خود هیچکس یادش نبود همچین ترکی داره، بعد ممد ازش سمپل کرده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82190" target="_blank">📅 13:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82189">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترک جدید ممد تونی به نام "مایه بده" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82189" target="_blank">📅 13:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82188">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzaIoZfpe_F3pFyB12wO7F27lc4kSQ2hJNK6yh7PFl8jXWSsenlxb5_NtVouRJebeR7Mg84-uhKvNaN6rAuM88P9JYmUFQv8MQRNdHCcq9Bd9Scsygd94o4tB7TF7duvy2VSb7oA-GjrDCRy8sJvJ9YLCD3um8usPm5QTZiSTIzMRJmjgS4eXSFEsEH-fhHNfTrt07Y_AiG3Qp82HHo9SPX2vFAjqrMCEdA49uev0C4Bb8emFdfCUO4vzNZOpDjgmHAvkOKTTVtZ4RoJHUv1KD8wORDQJBpT1np5cHovUi3fTVhKjWHB5TGcGc0fJzZ0Up4kEczMX0gw93wI0O_mFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد تونی به نام "مایه بده" منتشر شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82188" target="_blank">📅 13:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82187">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2Z265bYt4ocSk2NF18Xz4ulFQHIDrS2Y6kNr3MMxY92aAEalrHcWnds7ee1Fvri2_VTMBcYPTwMCJu6q9Y4QeG_B66VLet9yG4LWMsbCm9Gxy_PnwNNVJDuzmBVvE82Fy_WyibXek2MjJ_NJW8bF5nB47I4dvuWYco7mIyDlEGmXgANrW2pRH4P_pJDNPcWDe8dQUQOZiE4v9ZBJmGJgyc49BrmwjixJJveqwMX24Q_YUjakiYvIi9J7F4h4RRGHCqXudiAkH-euVDbQKYfMA8prZM1OyPN_NdFT0XNJdmJ9oqZmFy_M4Af1C5mhiTZRvWvBKgsK-ViVuIIc950cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد روبیو و ونس  ترامپ مسائل ایران رو سپرده به این یارو که در عین حال گی هم هست و شوهر داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82187" target="_blank">📅 11:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82186">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWrnwKG5MU-GkWNF1wugAOZE3oyY7yHiwgSRyQlnMFw-ayjv6BClmX-BoK8UGZJlHj5sorCF6aC8fybWBw5EuicpKcpbRwsbkaHhEDmpYqKjICoR2pj6DhKWar1Ret5v0ojVHF5LKwdJ-x1qIRUmZecCKf9XfHvjfBOQUJdPWIOjm9-rnwh17_fNIs4K004Ydzp78U1ghzHI8J3Bcd4v7go04-f6ZZWfYAM6dx47f9hniwSBX1hCNAg2hEPqOdButyLVgwDpD-_wRPPpDa3ws6tmNGQjZDjX78kvRyiZxym71j03lgiacalhHu3TtxPZT96Az6FK09l4S9cd_XL-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون یه پلشت بی فرهنگ کون اینو نداره ۱۰۰ متر جلوتر پارک کنه و پیاده برگرده عقب، ماشینو ول میکنه وسط خیابون میره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82186" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82184">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lpkk55AeZyq3TyFPmTYIsY9ubG8oouPurVD5tHObCOGJO99QjLOmGEBCs0QrhQbcvdjQoFLAovDfi6fpWuqxR9wioVL_22L8HCu7km5JiA1qan23wV836WpEBEmR7v1j4gdr-gkc_nr3shzjitwiEkWJMx2BAZP4iHTKYcKIjxPbQpQqV0ALMZayk-CwepC7Vjcw_kZKGukz4nQx4be8-efQivWduMXVS8mXIGt8B0va8aCeapUa44neTJ_8Zq5s-G2S_bt_OGrmrrNHFIglXYfG9nSIPINBJ9B_4stO6Uqpgy2vhr8TbrOaPqrwErQyReLj6YOo1GQNgBlJh_mnhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز بیشتر پشمام می‌ریزه از ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82184" target="_blank">📅 10:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82183">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCCvrSg7EHG_N_mrunDlVnzZf8UPY3Crf0c-ZTEcnz0AtJRBKfDlBvy4m7TIhgeGVQT-SttLvB6UyTpTkqLwIpTebLN-bI0kQSZl-hPKvnogA_KMCCuJlxLXoAiDJRjFxsk3uhKSpsYKx_krvLPczy-_hma76bKsUKTXXrKfTubkxCcbEciz7MCIHw7EaXUD4JOnBv3JIZGu6HfJ4nJJ6EaypFIpV8i_bER3gH3e2E7RTt1wvNZuLSjNTSs2iPVIo-WZyDzD6l02dKm9_zpfkRA_Zd2TsabvSdyBIMzxdDxsteCxOfWhySCwFo4uEHRq_YTTVTUtrlGE8JIcpvrmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا که جای مغز تو کلتون ریدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82183" target="_blank">📅 10:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82182">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82182" target="_blank">📅 04:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82181">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdQNBxS-DgeNDvS6pDsvNVFMbwxsRs0ARFDTjMjNr5kJbWwuqVGlP9fAx2zWw4wHWbB8MgfNVwqMj2F_xA-1cSPFKAE_FtNDnyaw_EULAGrEsG9-s0EmHqpKgn5-BqZYhtLppcbXp0oBYy1V_c1rpUB-6x9MTBZQlB2MGyloh7CydbAyq2WMS71PakExQQy5ARorUy2h_E3C8OqjamNM9T2hN0W7UbzAsUSZIfgz2PJC1BUoQA6NiHbEb0YxXD2xSQEaXGbXTAUuIU9QlPm4nbnaKBCFdWqaQgDhxXDN-bnsFdGyeBsvdSBuRLcAQ78yR50JlXYqwjlfkq141zNT8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اگه رستوران بزنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82181" target="_blank">📅 02:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82180">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fzpy6CG0LWJCYWt01Uh5z0JWKAplwMYrgMSZgOu397hrYeOo_-2tqf9ehDeWgh4qV_xjLTxBF0wHtDLz8ak_GA5r9Vg5Lid83OD5Uco0dAuPQf7CkFq38Hvktp_FS0v4pdohM9QJtI2wFTQ_q1pSXcK7DohLvASOJ4upRFAR2YkjVJBxg_FyWqP-s6xVjTO_ciBrgg7LccwHxsmG2qUgROLt7hiiK2Q2lokZXRTjsmMr2fedQQCu2_zCh8x15k3_xmPuTV31gpFNaUcPsHoicaFq4EAiBmOnumhD-iHkalmra62Kq3adCR6fK7DLG54QFEqs95Qgwd7lgxeaMVXyEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوسه شکار شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/82180" target="_blank">📅 23:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82179">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpctKvVp6kgAevY6N1CoLCqbZeiuBEpOlkL-q0LYtre_D8b1Ld8ORY1_Je2p0i7CysPUFj1ihau3CF-M8h14RBl-Cf9EeWZDYhixpPeczY3e-A_AmQ7llaqhW_kQj2EpCRpR6ZIVbdBL5xBilTZHelwj1qQa0oWC-q8zj9Y4MC7vALASM-l1BWPwyleELWZmqyzvTzq170AARAFfdsCh0uAYJ-ue0hQiJINoXPoeigjC_UU8YPTgXzJhm1_nofZjcmbMAJ53oRKxq6VcZUi8YJLXukLfSGNDhUzDV8ZRs5M2R3NVzun5JE_mbO4h6_JF4YAJW13vky2zr14GPBtQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیری پلشتی کیانوش  @FuunHipHop | Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82179" target="_blank">📅 23:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82178">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5782494606.mp4?token=jJ1vhyt9NM-Q9sBr6FmKzwfbD8ljjkxjRz_nJ1tjT5b5BvAjXr74ATYHckL8-IzmVlH0LEpwTVaJcTpGyVaDhdbDZuDi0THb0W71LvG9USaDupioYyNheqeOlwpimkNAn_UzMCLBEVRF4IdbE0cHCZRMUqWfO2_kQEkUd4heoYEYgD6J1IWrXEBNdu5wRIegUxGWubANiQbJp-VgCnybCbKTgPY_moXXKAdqZ4DauXPLhZ-zMug5rZBmwzmk3ndzKJXz27Q7VlMONJ6gGRxgJ0hC4u41h0rpFj1VkslYtlc3s8XrZl5tbyXa5WIftxU6M2GtJx7iBlKvBScU0KRHV7NdRtap0SnQBLjBo94w3JQHrVjWnlQ5kb2VdX_eZ_zschTL4jCd0NICHI0ItlQzrGBjXyBSrS3H7_EE9dLw4e_ClUSgrujb9FQ2zC42VgiENxUe-hU5GcE0XGGPtbqJPS4gZQRd7sIsUir4cK69HDxGL9Hq63BUOTDjwK8Z4ZkgifCAVb2CDisrcmRbzPQJVL-Y1kwBzC-me8WJB8oB1igwOuql4srLo2sE86NGhDBfcHTTsUVLKF-0ndEyfQxJtFqjNF9fmzUZVj8EjwyJ-iY4YZOAd1oNlzg_q1VXakKkGxsc3ulSNpLGd0BdRSA-E4xIYxRQyN3V39WUOMBWYAs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5782494606.mp4?token=jJ1vhyt9NM-Q9sBr6FmKzwfbD8ljjkxjRz_nJ1tjT5b5BvAjXr74ATYHckL8-IzmVlH0LEpwTVaJcTpGyVaDhdbDZuDi0THb0W71LvG9USaDupioYyNheqeOlwpimkNAn_UzMCLBEVRF4IdbE0cHCZRMUqWfO2_kQEkUd4heoYEYgD6J1IWrXEBNdu5wRIegUxGWubANiQbJp-VgCnybCbKTgPY_moXXKAdqZ4DauXPLhZ-zMug5rZBmwzmk3ndzKJXz27Q7VlMONJ6gGRxgJ0hC4u41h0rpFj1VkslYtlc3s8XrZl5tbyXa5WIftxU6M2GtJx7iBlKvBScU0KRHV7NdRtap0SnQBLjBo94w3JQHrVjWnlQ5kb2VdX_eZ_zschTL4jCd0NICHI0ItlQzrGBjXyBSrS3H7_EE9dLw4e_ClUSgrujb9FQ2zC42VgiENxUe-hU5GcE0XGGPtbqJPS4gZQRd7sIsUir4cK69HDxGL9Hq63BUOTDjwK8Z4ZkgifCAVb2CDisrcmRbzPQJVL-Y1kwBzC-me8WJB8oB1igwOuql4srLo2sE86NGhDBfcHTTsUVLKF-0ndEyfQxJtFqjNF9fmzUZVj8EjwyJ-iY4YZOAd1oNlzg_q1VXakKkGxsc3ulSNpLGd0BdRSA-E4xIYxRQyN3V39WUOMBWYAs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه عزيزانى كه از رفتن خانم کارولین لیویت سخنگوى كاخ سفيد ناراحت بودند ، مثل اينكه ايشون مى خواد بشه سخنگوى جديد كاخ سفيد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82178" target="_blank">📅 22:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82177">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9Yf_yRw4alEBqY3_Y9hCbJzcQ0uXRgmTeg6wRyZ_ThLcNMeQ3vrNZXgay8QcjD1IShnuOOoADSfF108iIRSE1TC9CP-LLYSxusMDiWc-k3xi93ntwNLzplbBqihOFAC9P48AtZzCpXFB0UxdUlF2enZnK9YKn4EHpDWXBNrf3Z4dRkPcIwCtEVoSrZxP4Ge22rY-B5MeF_hwVJw7PynSGLzlNNOo_qRlzB7YdxVddZeGeklCJLzTL-3lb0BGVEWNRD3Yyi1Fg9iEWMKCLwR4UwiRH-Dl8m2mHjSEPSYVQIGGOK4fCWX29rRm1omDz4DHlJLl-rUdXTmHhyNInijsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "قبلنا" منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82177" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82176">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403c217675.mp4?token=QEXi6ynx1XtaLUCWNCQlbCRMhjKQV1rSRioO5Z6zkVnttdrAL2OvO6V7haBOEa7Wh5qUaZPAlGUGkIZbSWmzXa3CzKhPgnZFw5k9lUiN8mwIkNWYYTxtGjrXwVHPN870GKlCVKIuvs2kWbfDnW-2LZPYyNcKaBcaxo5ud0GL_Ft8LRDRsgEX1Cd6LLf7fPuq4XaRzmKQ1jMLOgYXN8xv9g3qbWYrGJZjLZObN0gHu7Y9gyfL_rVSxhiYsckCFzv5XVNODgpJ7G4HUyOREe9IvOu5h-XrTDB30D8Bl8ItmzmQbmwgjc4z9EJJb8YeO4ndNuDRFJxoG0zuKh7ZfW3ltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403c217675.mp4?token=QEXi6ynx1XtaLUCWNCQlbCRMhjKQV1rSRioO5Z6zkVnttdrAL2OvO6V7haBOEa7Wh5qUaZPAlGUGkIZbSWmzXa3CzKhPgnZFw5k9lUiN8mwIkNWYYTxtGjrXwVHPN870GKlCVKIuvs2kWbfDnW-2LZPYyNcKaBcaxo5ud0GL_Ft8LRDRsgEX1Cd6LLf7fPuq4XaRzmKQ1jMLOgYXN8xv9g3qbWYrGJZjLZObN0gHu7Y9gyfL_rVSxhiYsckCFzv5XVNODgpJ7G4HUyOREe9IvOu5h-XrTDB30D8Bl8ItmzmQbmwgjc4z9EJJb8YeO4ndNuDRFJxoG0zuKh7ZfW3ltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آروم بخندید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82176" target="_blank">📅 19:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82171">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAqpQ3wBNMoD72YiSut4zy7CAoq-hknmM5UYsDwZ8XYAE1XrW_bu2vzp9Dxd3PVgp6k0zFOZclZwDjNTLANcOuMIXI2H9CWsY6vnFdXhY5MPdEDl0eVHL2ogtUJZ7dj0MG7ut2ktK2hwSN4ac5OYZuavGT9dalDEGM1mR47MvuyeqtmjU7r-2S-JEZKlqKGiADBgiHq4EW0HUQrl6I2C0-PAfgdTOPL88ZszEOtjUXhI4oxyhtHhOYongPTyEu9icEJi_6mCe3i57_H71tb52h3FD4Kszeoql5TstBzfD-CQCwseaoA_Uwp64IT6BXQs5aDSrRU4PX5W5ywNmhZ4jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KkiiPV3hhCv68--zresIpq4SI3LQXSr1oi-1mNQN00aqfgneyPrMASrsXllw_QOHYuGwf-lS4RPlXVavqnd7c2iFPAwYJ-GaZzebTofPjH-V8hP4R4RMbQYM0zIx8Om25I8xCbX2BFjw8I1Yw8hbMs16smzaGz3a5jchZ7ooLj7GLGgojlIzc4pbYP0_joUfrOsdlwi_dDf-qKhNdPRAcAH8smcBLOZjJB7a4YOgOvzUgAaZJheJHlgp6YSNI5CXfCh4TndogsWPkaNB2Gam_197F6zKbOn2CCF7SU7ocgmp3mmuCM0kLZaIIP7dKsXhfnFD7XQsWMycrTqb4F9dkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBHH1PEd03BzJnD0kB3E4Jjea9qQyDPo8LoEu8OuHIlLpnixzp6WgSPQofYh5dhSB75hzDmv24rWaiGf11QSVDpSHL_sw89SLA7-6-pSIiTHWyJeXbtilmVf-wMVBL096rVDbJQ5pB_iN0KUzvwj9IGihBwFWkvimZbgkmdVGfgu2Lp2-D-iS4eddCblH-B3n-SZ98Fcwf7zXanBV_qRrCUJXWm9V7PpO6nKQbYbOTj0Dg74I3J9tw7RVWcoR6OSx6jHkn4KU3zyesD-h7XFNN8LPSYq7DAzqmjpWH6L3Zzz3AF6F5ed6T2uRx7xtVwLmgWLnmmGp7h7eijrRVOZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PqXvYpTMMXXipY-3jP2mdwDLdUU8eNdrNm6AFPAgiu_r2zlMObMGYD6ZMlO5GnAOqD9BTQv0qAqQxKD70-ffOZ61t1SdxGP3kUZ5wenra0DxXHBfWL39rGigW-WXmE0WlWRcQPRXk_dEbY2Bx4gZ8Hwm3Gi4M-tPUItemOFhxXHNOnNAasELb8VZ_FyQzEyPZlhvpGZqYutWACkBhnDq_O-8PvEcnahLY_xeUCOZO_BgOp7GpJoSHW-L8mazFWSNCUDE8ZaTs0XlyXjxGJ8u8ExkN18PBYCvh-bY6dnT5DINiAowuZ2bYNTPg1YtoMeve3XhKlmvxnIlDcQQ7X6Y2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa705dcf0.mp4?token=kFj0KVl03ZHA0qS766K7owq1aucH0xcRujsfJZClEfzJCqptHZiLfRyL9CzDt8ZXmRHpB94FM18ZGDvwXn8Y38Ab7D4GD8WVbmspe9AScpEcufFBWVC4bf1e6bvJmmjiA_snQD6vJKZGPFFIsTxgGEWuJ6GwYFZRKWidKVAIzyUJ7LxlHHHO4ZRpQuSZOSkEXQVFiOTmS4habYKih7jt-zfiGK5QNXvdqT2faPQ1GVvBTNnfqepBM-tLSheuUHzea8qJ01Bfqc6fv1cdDHsVkmAdOJFs6VSQS6aChmnHT_1PSLkLz1ItjlaGFBbWeJxxh9AK6FFIRzUHdPvDHmTQ0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa705dcf0.mp4?token=kFj0KVl03ZHA0qS766K7owq1aucH0xcRujsfJZClEfzJCqptHZiLfRyL9CzDt8ZXmRHpB94FM18ZGDvwXn8Y38Ab7D4GD8WVbmspe9AScpEcufFBWVC4bf1e6bvJmmjiA_snQD6vJKZGPFFIsTxgGEWuJ6GwYFZRKWidKVAIzyUJ7LxlHHHO4ZRpQuSZOSkEXQVFiOTmS4habYKih7jt-zfiGK5QNXvdqT2faPQ1GVvBTNnfqepBM-tLSheuUHzea8qJ01Bfqc6fv1cdDHsVkmAdOJFs6VSQS6aChmnHT_1PSLkLz1ItjlaGFBbWeJxxh9AK6FFIRzUHdPvDHmTQ0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامنتای اینستا واقعا جذابه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82171" target="_blank">📅 19:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82170">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWIeZqq5J0uL5pWx-3iMma_1y5ev25FZIOq-3i1_WIFZyqtZevh6GB1AtiBiKADyHOirwKvO3cfSSyWrbKHB60XeFEw9NoA5_E61uFiYW51ORoCD0aoBoXNC4UMrLXf6qTv8bcEAyjjKdInGS848EQkf6nl0e-UFv7OpgwpL_DTUOu0nyYQzANA1fpcwqpqzF-evd7EXuCeqKx84kESr37ktQm2U1ZkenGugI7OZqv6D1C2NzKMNznlU7mxm6m-aDMXOQdRFIhJ-Gf4a4-Yp_IAragu7av6KIJQiKrQ4jI6ggzdnjkeT4HZ13_FEpKKBjn8z8Rhanin1V-1gzD1Xwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودتو گول نزن ارسام کیر کاگانم نمیشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82170" target="_blank">📅 18:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82169">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پس دابل آلبوم و این کصشرا چی بود
این چه کصشریه</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82169" target="_blank">📅 18:26 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
