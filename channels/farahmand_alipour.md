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
<img src="https://cdn4.telesco.pe/file/rwRXE1YMoSXfC3MCErMvgNjK2GwHN0_EXer3tsTz3_mxciHhyoE8kfc-KZA3-h3z1P3H3FdaFH4DJJnU_8DAfDFKQ6ZZ8sqzm41S_URoeYDOKH_dlgqo1R0R3X3nBlGHaM3VMvYB94R59THqH9_dpVY8EGFjMM66JF9xpkbW2NNH_sKSAMrninP45rSflDU0UL4tbc4OsQGs88TfuPUJanoHK0Cy0x4TOe1vOoL-OlCWSjQzt0SgH_wjUuUpLXLpnXTKCG1ogteTACxxo-qn6Y3SWHuj5ei3o48Sr3sI2WXPBBvaHKBk1kZUP74gp8oj0M2vKZPCKoREWKqDfyC8aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 13:13:50</div>
<hr>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=OwyF9utrGm83req8IWl1KhrT3qy4kGlYjYhjKh6Jh9fbAn_K857Avq6ByVznMPRfqCP88aRGQK2MtVrOUcgmUbMdYKkDsGpCQUn70Of6mKT8Hg1tc5OeJ8hF3y5rfQFTwL3iA4QZ1BV8Lo6A8VBtsZRMZagK4bQ3TrbPgVu_rKYV5laTUdFVPUx1JA7f2T4-8MUQeOn-W2YVkhDe1r2v5lslS4vl6890ua-k0uZ0RsRaWw0TiJMMITErpQKEPzCeDgKaJYGiv7s_s4eW2Sx72RkRlC8pFHiBU9Uqz_0ynC7myUi-j6o8qKjUG9XtgQ-Q6iM1BNRe3_9tdMBs03qWZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=OwyF9utrGm83req8IWl1KhrT3qy4kGlYjYhjKh6Jh9fbAn_K857Avq6ByVznMPRfqCP88aRGQK2MtVrOUcgmUbMdYKkDsGpCQUn70Of6mKT8Hg1tc5OeJ8hF3y5rfQFTwL3iA4QZ1BV8Lo6A8VBtsZRMZagK4bQ3TrbPgVu_rKYV5laTUdFVPUx1JA7f2T4-8MUQeOn-W2YVkhDe1r2v5lslS4vl6890ua-k0uZ0RsRaWw0TiJMMITErpQKEPzCeDgKaJYGiv7s_s4eW2Sx72RkRlC8pFHiBU9Uqz_0ynC7myUi-j6o8qKjUG9XtgQ-Q6iM1BNRe3_9tdMBs03qWZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwio9t5C9X3LQdA3Tfgk8XL4aHUAAgQB5Jmf46RJGRUqs58Qk658mjwptzZSI92TA2iHI_JrcOW6Hh8MJkXRa5PlHh5DhxC4Ou9OS7AdGjPfGktRM57V9gpGGlWyuVsEkal3zCKxf5InmSrRNH1hRHUzhV31P7_lzLcjt8moPI9pJQmgM1asj8bur7wzOoXZ5gmhjTvLFQrcXQt3N-zHltQkFvwRYixz0gNNzbgAmGRqIJNeYdk-ExgZwwEDlWgfpMamyW7mZTJbbaYCd8ys36Erw2sice0WrTmTYH_-ReA2VXampyUbg-Q-s6qne8HM1LtQeSLm9OlKpd3td_p9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3eMdtcErg7lfvLaHY-V7WmcqeyLesbBKHy1DFiYHjziIPe3ofpy8thW_eG0t2tCC8pybs0pgy2HlTl6hhyNsJN9dt7MQS8USIJOgmA8ekrqoB6NZAbE-PK3gXEF4wQl25TmiFTzhwWYA6hQAhA_7vTzNqKWvEzXVuqQvoyAXoTIuIcQ6hQeGb48Phd76PaS5kU-gaGtE9XSkPjjkhhIZLYWnf7nxvoNvYkIi_Br4yudumGsd4VrOlKw53xtuzzf5rgD9TIUCUZO8AA0vDmcVj-t5Jsuz6IKIhZwcNjvjNr2kLkYglwCqHd36C3eqz7JHj-bKCXx8fxvvlBnv_25uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcPULsn7ddD5ww8HjOBCHMQuR_rNAJi8vrB_P7u9Qety7Bz7iZ_CdxEmjn58KV1SPwiwp5V3iGcbUO8dUwezDRLoyWGXTJi-m1PGaddqon_VWEcFy3AT60SJBOYJ0vYLdFS8qKQAA2n_QeFvNs47wr7OY2W_8HvFjU9563zB50nK1l6nCJgZ2k2JK6n_KeBlbNwyVM4KpLzTzswL4oWyNzoVWlUECeYBMM8LkFFgXQ1qBkjfB-9DPOs7Mmtye5MYeHTXLHWuSC2p8B-DvSMcM_LbmGaVa3cT9wg-0MG2VsnUrmPKZ7bW4JZOqfyPAb8q_8jQSjKvWhrXcpWAEoKqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7IkecagwPNTwX3YevLrB9Ozv0giPuDryIny7MRDP8V8w4KCxTsOr2YXFNTwcWHMPcUlAOzAPn6kKtwRjVkXmQnY7Da2taeGmeyT2IxGKKjhLYawTj4FwRqJFGEgTOLvFlgJpdP5U1phv5dtM4hxKTJplmmLByfMLGFF9ZubYMQwApIIXXVVOyqQcr31ZoJ9Yq4UXUhjlGLauOoAdoal6T9I96sez6xidAS8YxnQ0tXEj43TLVJcSLWQuamHkuj8VEPCOfAW8yi8R8DC7eVG9l0GYX37wUF7BSswHcHK4uEwKOZbPm9aXABxorAsz8z6Lhaw2Ff9iNOueUEfsVxmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bkd21A56mnjRl6zQ4T67xpO1kTusTrS4S8_V2nfycRZeg6ACOscBp_i2GIpvTayMp3K7osmYDWk151e1BMJoXw8OAKH79Hb-vfTe5Ir3CwhpFrJwABgTc6xhaphxWNEyZm0bBlEQoHp-FicbMpxDcVdZCo66syJKCXzI4OxFsOhTtSffmSGAsi0xyL6FcC7X_8yOyKtk_TZrfFw3ISKWYEKoaoJ7MXChRnXSCzbGLjcWoHlmiZRnyH_p2PSZYwb55m3uOYqg12pNX_xVxW5QXnTCSSweybFV-j3Fh6RLJ05n6NUbXOhf1L84Ct9hB3W5KW8ppps50yX-Z7MFR9TOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8d-Apnj4uCZFyZGMa795bUq3dw_otqwNiFa8b7__2frfG84DTtQVJwds4dh4M91BY5WzUdqUHq_8kqQel3QIb_moQQrNUoS5r9FoYDY18Q2pVbF0xbAOa4tHHeplG0dtK3PmTIyzkoQccD6rk6_Yh9ieXgjyCbkearMvl5Ds1F9M8mA0egxKlr_Gw2cUE1u3dAZc29LxvjqPAdlW-QL2t3V4zW5GTUObIAeVRl7-YGuhcebFufgXTc-1R-p2jQTyuXSmsmlU9ujvDAyeXBwQ_r0xrEjm1-L3B7JKlhUr3-Fs6umxTzwqpF2p1w_Wo09OywCPlecSY6UdJcx9wuz_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By8Lhzh4SMe-tfd52BcnBg9W8Slt-Pw4ifHa1_i6wsghk2FLgyEtKCphRK_1UlRbJhYzBHWtoKYFff4e4CPhiEuBDJkgNtDchKBwSP4Sjjq4Ucn32j9NIPxfe4ekqs1kPbWVwzzTIdjoCTiVw5UdV1-EqayZu6lPGtv12YXGrCj_dREHy3_xcN44DM4-R2kpdY5B4d9WY5pA7HEojD_HSSm2BajKK-ZitAYwgZjbcHmJWnM1RSsJfRewZjx9gKDNwSw-PkaWENUeDc32WE-0MkCULcvKeSTDp10ETrskcUAi4HNwAFSSqYUKgZm1Q1QHZMVN8WZPtw2lASfTt_T1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prw8Ygxxr191XrhUD3ZK7CNTqgHS7Kx4tB_v1pmAwgtN4v6FxAq3EUm_eDPaWyvKbSHCJ2dm3KB-SfABpv3gf_5wYrDCA1fyDMFHbYrzzIMF5XY_1B_6IirPXeudayEo67yPAjhqntq7tahzK0_SuFVlKHImLbOpvdVUOY6eiZKow6SH4CZL0gBKMO4_whNNEE1CDwUQDXhVOueJ9hdhVMTz7O_gN3BnhKLuvM3YWhvdsaDKX8VR_hVbavXJGh-PYm-v4LmNrUSVIMrfv4cB2Awk-OZCCy-zbmhnZj5WivM1PBmR2ULmDpP5nZr-WhhVajpHpKlMLalc8XfM7Sc0Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVI-IOdvEAZx6-9-CopNdi5IZCOxhXNsw9SnoT5dEYcsf9LtT8Qg0FWn8moSQL__-sE2n0qhox37_dHUgn1F_IfWlunkm3PG4FYSvEMuF7XxdUof_lNIYqxkCDGHcLmnmKgPWmcEbjmz5i3FTWHacDdbnwFFGhqTmVOzbxKuYy7fy5lAQsXGQ6UE6oWFMZjzxUI3RIqZSvY3y_1IKMvtq-eRuEUJ7cmtY-TdqbvA-u4fsj8-q4qFKl3nRLLQEYfQrKKeB4rh3vvcrntoXfSsAbcd3tSj68IvWLIM55HLMm2AjaAZ60w_qR0XT88G3iZJkU2W7rAyx97I1X6YvIQrSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b23JA1V-CUObD6TwsH0RRZ5uUMT3GPFPlu8-Ear75DGj3Dify3JlWq8Pl8-QxvZXuUgcw0tQb-3Hjt8QDWru6E6a-YCBxcDtcSptuUZWy8I5yHtbAWx5m6cRcP2WXFd35rF3YAZ2jw1fIwR11r8q_iZ1FbVInjo3zu12LOhg6uQqFHka6XRpBEB2BNC86F7q-1MCzjuqTeBHf94Ui8gTdFXCzs9R4KUBPeV4fQU0FnYyv1JQheOE4zzsFokjQ3_-rWVB4UagcPau8qToGGQ1SOKEfDbnAm_kZ6huOR424klAvZAD5pN2yjmCbJu2AshOo03ovnPRIKhYmCehAAI32A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kmu9B_s9vTvyGj2zrTe2Se3chjW2pVp_c2Bn-1El-QP9_jMVDGuE8_juGijtDpMgRtXTEQnvMhxqeCIt2l-5hb5cq5AwyewDBxzvb1uqXXDBbmKBkSxT7-Pu4ApO654kjS1l8LwE2_d0RGI4Y47P35pSif4QVhBQlK7Tfy3ApU0b7jtfRRcD2X8nfBk8rmssW4K96l51gzutnV3p3QnINZEIsDH6eP0ZEpnMUEDm-h85JtuCMMxclxDhNWztnwbXFB_9vSJQc_QPt2iqGkwzsP2TkW-EESCrmodrHUzBt0WQqiUEs93kL8FOaJD-GwGEoiYlKhvvtkuKirTpS-JJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=cZLuP9V2_XSRxmGZpnEvA-VvgXEoV2kqzvFn8YMZDPooamEs8IE0tWvNUlf5TRW96ONOfwjbFXAjPiqgkSb4RwNgKb48Xktq-n94w4yS4ZwhstuseoEMZJD1xuksITDTJEPQKhbD2aYXwObvdaL4wmTmkVI_anshkcClHLC4J-AICkaD8xLQsL4XKvGZZc64yaVdSJliuPA9EvOrU10odOIGxuc1lhukEzz_viNkl1OQX_EXcUsFfZQZt-dI7G-iPPwBKn7n_8Zl1duy02WTCN3c4YIJbHDVi7ObAPsh4Uy5TvAUeSDJsVt8b8L030TiOPiNXktGXAGMd5ChWt2x1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=cZLuP9V2_XSRxmGZpnEvA-VvgXEoV2kqzvFn8YMZDPooamEs8IE0tWvNUlf5TRW96ONOfwjbFXAjPiqgkSb4RwNgKb48Xktq-n94w4yS4ZwhstuseoEMZJD1xuksITDTJEPQKhbD2aYXwObvdaL4wmTmkVI_anshkcClHLC4J-AICkaD8xLQsL4XKvGZZc64yaVdSJliuPA9EvOrU10odOIGxuc1lhukEzz_viNkl1OQX_EXcUsFfZQZt-dI7G-iPPwBKn7n_8Zl1duy02WTCN3c4YIJbHDVi7ObAPsh4Uy5TvAUeSDJsVt8b8L030TiOPiNXktGXAGMd5ChWt2x1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
سپاه: تنگه هرمز بسته شد / به سمت یک کشتی موشک شلیک کردیم.
در بیانه دقایق پیش سپاه آمده است که : «در اطلاعیه قبلی گفته بودیم تعیین مسیر غیرقانونی حرکت کشتی ها در تنگه هرمز، برخورد قاطع ما را به دنبال خواهد داشت.
ساعاتی قبل، این تذکرات نادیده گرفته شد و
چند کشتی تلاش کردند از مسیر غیرمصوب حرکت کنند
و به اخطارها و تذکرات ما در اصلاح مسیر و حرکت در مسیر مصوب بی اعتنایی کردند.
به ناچار یک فروند از کشتی‌ها مورد اصابت شلیک‌ِاخطار واقع و متوقف شد
.»
🔺
جمهوری اسلامی به زور میخواهد که کشتی‌ها از مسیر آبی ایران از تنگه هرمز عبور کنند و نه از مسیر آبی
عمان.
🔺
آمریکا از جمهوری اسلامی خواسته بود که شنبه - که دقایقی پیش تمام شد - ‌به روشنی و علنی اعلام کند که تنگه هرمز برای عبور و مرور باز است، ج‌ا اما دقایقی پیش آنر‌ا بست
.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZ-sDB5zcow3tHahFcCKRVfTd3JXC3Vf9xzWU20huTZRpFmgEPQkXbxE-EP1LnPf039HeeAdMjB0StRXT3I4-LSj_Xwx068tf3s5DxiV7IkOZ6P0z1j-t8UeU2KHnavB2FZD4si16zIe38xhrLEKDSVpoYL6b1iOQYQayCnn0_ue0N3XEjuaGPf4Cfr91dw4l0sI4lMUk4nAmqp0IYG-jbMwx7tkaao4Dls163rpPVEjQAUKTv_CBqRrZ34L1IAtYaD4qWqAKk64IZtqmy_J40ze_lV_IGMPXs-e-um4xU4vfoYv4m8HKOY5HRWRu8oeJ_zxMOXjqzEQxqxYb1J5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=WwVzLNIL4KTowOTsFZjTk5RSmUWzgvuASplQ9u2zOj4TkVOQME-NoQP8YOhy_i3Ik8GuDgDmUO_cnYEy3B66h99JnLPVUtdYXI87Ae3S_5WrRuBv5RRslZfia3HJ-QZwLhi0n6L4qdLGqNROmMAg_6Vu8CzbCqfKwUJlV_zgwY4BeB7KOCyWidNcEDromSzJt5RLZOFq2TaomqOEKGRMNNVypSB-c3glSgCR-lEdJD49ISbJJUGD-PvsFo_u3RmzeknXHnLYb8Vypz4O4DAw8JKpBkM-WOxHzeU5H6-XTVQXhHUEUt9uo7No2meJ5q2MtpADNPixH6WCMfId0WI4zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=WwVzLNIL4KTowOTsFZjTk5RSmUWzgvuASplQ9u2zOj4TkVOQME-NoQP8YOhy_i3Ik8GuDgDmUO_cnYEy3B66h99JnLPVUtdYXI87Ae3S_5WrRuBv5RRslZfia3HJ-QZwLhi0n6L4qdLGqNROmMAg_6Vu8CzbCqfKwUJlV_zgwY4BeB7KOCyWidNcEDromSzJt5RLZOFq2TaomqOEKGRMNNVypSB-c3glSgCR-lEdJD49ISbJJUGD-PvsFo_u3RmzeknXHnLYb8Vypz4O4DAw8JKpBkM-WOxHzeU5H6-XTVQXhHUEUt9uo7No2meJ5q2MtpADNPixH6WCMfId0WI4zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoJFMn7j3NJm0MwjlYz_u7IpsvklAx2PRDCRN3kxSn6jZRXJQ4UANTVp9MXprcceg_luEGUW8MI8eTHq3gu89GI2UbuyMW7dkW1DEVCu74nQn1FvYSmqlfFe_YmKHquU9TnHRTKSazLw_aAGKOD17rxI2hRMMPLkzGxTtVVtsoIz4_hkBsNj43L8Dne5Kb_ga4AbqyOnwlq5wZEHQF8emXGXfGh232AgwBUspaOrCqjPZ81EjKsMY9qIWkZMeCWwd5jCUtVcHLHs9ze2U44Yn_QOntVUNXBScv7xTqydO8cw2EwLwfAZYopGyW8TbKEhDdyWcRsOcJS-69Aqe_lTEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxqzJsY3Us-3sSVT9app5F30Oz9lGNFhdV3O_2xLvxsxjqjsevHp4-8N_yXeSD_SEYUdQ9bFrJnS1XfXuEiShxbAlkuWUVbi3HkiQX06f_etNLT-qBkQJHomfZVxbdMS8gdGa6Mb1CnM15e3VSlME2bBIUvxVqpuUNQk1Ws-XPApkjFzeyXpq9GknkdyMcb7_EHk5scG-_yHcGGN2YOuv_NJLjZKOaSX3qDu-m9tV38Kcx4oVgU4Gz1PoihEjHCz609cZq41Z2sM15ILuESFhqHaMV-UA60Nf4Cn_Ihvz6YKKEP6_AJ0BNCR4a3UeHyP-A6ifSezvH4-Ky4k6o_TsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر یک مجله ژاپنی
در آستانه جنگ عراق
که پیش‌یینی می‌کرد جنگ جهانی سوم راه بیفته و…..! رسانه‌های غربی هم پیش از جنگ، ارتش عراق رو باد کرده بودن و بهش میگفتن : چهارمین ارتش قدرتمند جهان!
رسانه‌ها عامدا اینگونه می‌نوشتند
تا خطر رژیم صدام‌ رو پررنگ‌تر هم کنند،
اما این باد کردن‌ها، در عراق هم باعث میشد
که فکر کنن بسیار بسیار قدرتمند هستند
و جهان به قدرت اونها اذعان کرده.
رسانه‌های غربی با «قاسم سلیمانی» هم همین کار رو کردن!
و بعد ترور شد.
تروری که ترامپ هر روز یادآور میشه
که اون دستور کار رو داده!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=E6smCBjJEYnnMNocs3Z8UZygwGW5l2SwaQp6H9qa5ubCCxNhITGbXzOtEbYfHwmwAYxtVrZhj6LfMw8WBOQbvB8jUvCealElKMQxRJp6LZgVDdLzAcXVY1PftjK8Us-UMgP1l-p3vnN2SYcHgCWrKdMMOPUQIbEwfig-NphkMyC4GfPjV8INm5_LVnzFKXQGEX_gbbLSqVJ3kXAb-SzbLDkFxuxjuh8maqGzvEixQOimu2yqWO43tiJk3jkthumF5gAhf4A4m46yEP9KFdiEboNlxTvk4UDKGzw5xmfH8BU8cLV3G3z4di1lc-_SkjqOR_sNBxAUtEwM2y6cvLpnVWTpvqeMm_frJ6HP5LXji4OJ1o_ALqUcDhfh02H0Om-NPBC-YJXVY_JehJFfg8qq37oPcQN-uLp9ZtaQ4wfnmxiiF3KKstLtym_7XOznt119qsXLsgqxyWdGSouB9HmqiOmsLX5TPSEcLhE0VCDyw-hisqBaXLzVwRg_Yss0ql79ThuwpznlWwsH56VvBRWPjz3atQ0gTyKml-TXXLBhy3BVlwdJH3gEEtB2vS9DTv-pYDR400ntp94qd2bggR2sSD3JtM-Ly02P17el90GHXoUl10ywj31g70GtudfL1GxzhIQMx5V10IEwTOG4M6ffGzF2mA1-umqLP4bKPOig7-s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=E6smCBjJEYnnMNocs3Z8UZygwGW5l2SwaQp6H9qa5ubCCxNhITGbXzOtEbYfHwmwAYxtVrZhj6LfMw8WBOQbvB8jUvCealElKMQxRJp6LZgVDdLzAcXVY1PftjK8Us-UMgP1l-p3vnN2SYcHgCWrKdMMOPUQIbEwfig-NphkMyC4GfPjV8INm5_LVnzFKXQGEX_gbbLSqVJ3kXAb-SzbLDkFxuxjuh8maqGzvEixQOimu2yqWO43tiJk3jkthumF5gAhf4A4m46yEP9KFdiEboNlxTvk4UDKGzw5xmfH8BU8cLV3G3z4di1lc-_SkjqOR_sNBxAUtEwM2y6cvLpnVWTpvqeMm_frJ6HP5LXji4OJ1o_ALqUcDhfh02H0Om-NPBC-YJXVY_JehJFfg8qq37oPcQN-uLp9ZtaQ4wfnmxiiF3KKstLtym_7XOznt119qsXLsgqxyWdGSouB9HmqiOmsLX5TPSEcLhE0VCDyw-hisqBaXLzVwRg_Yss0ql79ThuwpznlWwsH56VvBRWPjz3atQ0gTyKml-TXXLBhy3BVlwdJH3gEEtB2vS9DTv-pYDR400ntp94qd2bggR2sSD3JtM-Ly02P17el90GHXoUl10ywj31g70GtudfL1GxzhIQMx5V10IEwTOG4M6ffGzF2mA1-umqLP4bKPOig7-s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPYFaiWIu78asI61PPYJHATM_TJJ9gdKWYBy6CGsKWBV5YEGENDlm3kyhUwCXnIfOzPSqRRz3DCXyC6eOPEaNi93cDi5Lyah97BA8c1tV7OwumP0ZTTyqFulRF2HKl0Crs_xeA3dStiaijPBEEh5RUCAf1vPxhec_Ur6f2MNvWDZE_MYm2rme9IzpSSzvB7GbNHeH4Clv2QHbY3zPt5XXYY2A6qrWQwXRy4nsoHdWHSQQDtmf3AGHyBnpblkLCPbAJ9k-V2oxkfHB-2Y6PyOLpdL0kUPbnXNff8uuC0ZaWFTk5Ibu8V6NkFHXvcmSkfGOioJkSb4LNSGJILHGx3YJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vM7IDcEJp6fOBQEtvrMC_oV2J2Lruzar1Wa-Phi5cLOjxTwQY9uHMHknj83kv0vo8WxNg6XGjjtI6A8LfAB5uXb-O108RsZMvp9v4_x_BhIPeP1WFN60_9-ynoyJgnwaqTLfKI9pB8zzMk-MFLQkOH12e2sGSHD0IhfQWg4GKgMBcSc2lttPQtke14Uo8es8EBgpdylhHGVGGkMIK8SNmRlCXGjM63GOlEhoFTioUNvEWixbMQpvEGpK_YKjW2E8UK4Junp4JPWEwIvnan8ef-ot6Zz_vFWnN3Pcrb8PAsny0w0r3t8Z1u4eXr1GoW5ihub9LPJppTos07yJcxyVaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py5pVBAHjciZdQDxDeXlebKT_mn0hToihK0H8ZD-O-vPCxzgWarx6Wwpy284gXP_I5pInK_xlh2jMO0sR2aqbOEkeQNcjvoMrANxhTgZ25q7x5NVERH0a7bF7aivhuOMq3p4epzR0c5klumgmFuuJav2INbmZq57RzGV50zgnwAHyYYFIm0CoVWCg09v_HYeeF4oEwmj9fe-TLVE-2SV6AoQ4oDGTLUcMsAQw72EEMJPJQe5ZxHodwLvnOOmY9-ot1VtbEBS4NUKurcI7xVFd0BjnA1HpLQlUuQBCa1ezLq5lQJD-dv38ZnyMyO_cfy9wWVcSeWwqWTv-UB9OhweBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=cz-iMrQTsTLwLpJjtIvGEpnwD2C4JOiDRGxtu-diHSm5_cWJrBm92-nVtyRBUIV2GWqJliQ8jUXtSW6-p0WLp5DKFaKfbSVFGqh0aC7p3Nmz0OlwOmkVtZip0bYn1qJRwtRP1BvN-_ooW4-rG6QBfhPy3fi6SEBiI4A3iuowupXxg2lyWtaKQGyaUU3IsBnWJnHeFAyw5HtiJ1tjXKpdQCOopmC9bE4vhQmdhuoT_Gr8fryvdapq5PLn8x3KYV_ilPczezZsLc4_WXiHTT1ae5gdqUiGSBeT1d125TaJhrkWVWIMSgHudFusVTgoor9T-TinWtMLO8lztTpZD8YWtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=cz-iMrQTsTLwLpJjtIvGEpnwD2C4JOiDRGxtu-diHSm5_cWJrBm92-nVtyRBUIV2GWqJliQ8jUXtSW6-p0WLp5DKFaKfbSVFGqh0aC7p3Nmz0OlwOmkVtZip0bYn1qJRwtRP1BvN-_ooW4-rG6QBfhPy3fi6SEBiI4A3iuowupXxg2lyWtaKQGyaUU3IsBnWJnHeFAyw5HtiJ1tjXKpdQCOopmC9bE4vhQmdhuoT_Gr8fryvdapq5PLn8x3KYV_ilPczezZsLc4_WXiHTT1ae5gdqUiGSBeT1d125TaJhrkWVWIMSgHudFusVTgoor9T-TinWtMLO8lztTpZD8YWtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp8e0oCWM5NV-sXMjzkShxDsQwaUEcTBAAGQiLyewAH8czz_heGfKeR_oQUqZiBjjZ5ZaZ_H2hv7qe-n99j3qJBtxYTBEUAXWLSCRgEoLZ4BE4P8d45DXQZQH3bKmOYrs7JOX7xG63lR0P8FjCQEc7ts9C0peANFp8u8unnKTbNERa6mHgkOi4TzOQjQQwreBiHoBbs7zt7jDR5dByrehLimuhJvxDM4Ra9cSnFBHvstHixB_4qZKrV6LHdi4-T3WHDbONJzGEjXRHk63FzDYz3P38eXVLu-HuFNOPyXKGIUmQXUF3645Q6FmQo5aIVKNnjdXnmmUgGwoX-ZHOxSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYIdk1iltY5SNLHPE87u7cWosWTRooL5q_Z_-nAtsg3cNUv6hnm-XidzdOT2QWpebkpcpmN1crrrXJSq-5joaF5dficum095ezmytw5_QGi_idENIHunJK6aEDRePGYpTi3KfHMNZta7O6VU-7s6-xrEVU-7n0HuBqi87PyXVpB4cc3yI_nwnjVh-1EaAGGHrMd2__uHPJMTRyu4MJA4UfqTCGTcA7aw67NHVr2ICM-Xs-u2O0cYpA8EAVvN-5_nHR8WUvImqdsizupBdRzaQihRW-BlEbVuasi-A2bbSTz3U8bqzruYPZXi-WMMjqBuD0Wqnc7Iy6YWHvlHLWByQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJqeGgnUgFsLYEGoF0wjtOZjP2qe_2TP2VRrv97QhG6uTnpybpsTh3HXKgsPeGpT7TMYYMsg38-9U4z4BMNk_8LXPoTRe-rzqkp1cWcai0W2sdfpYvKAMfkTMdCFATiKyAJt5aXrHdmA9pFsjm5nKy4Q_vIzFB8GsHxaHi00LyGzkC3Geehz9yYc0sTLGLNopQz1WU9wEwZiJZXrg5lgw5dqXpQ3g1BYKq-kI9ULJql5MF-pV_zMbQ4z7LPYiCCOMKsdhJGuTHi6A4eOeEL6dS7kszNlZz3O0yckf6_rQjbODb-zn6U34E5CjjgKoauQ7Vf-UpnvUbBzuv4iIry7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScmS-alc4jh_vNO7O29lwv9g0iMh7uuwJAzCZosr_Av8a5RQKhpcOTdQx8PPBU3djc_ZhvfbmFOg-EchuikBV9FrN9LklD4AvyvsyJOZBgQzlRKPJqm8DP9pt4kFkjb2d4TsZ8e0pcs9QiCrtPNSre2xq7_djaFg9rzJmRHTVUcQWx5vRnklw35-HkjIGeCsPCGri4Dmoxx27TX3q67fMQUYWVKElkFCHB6-Xz0ksBjN0YfmrGlwfxT7I87_0t45lc69ykxEUpsww_O7M5DHRKEmm53Gwmsdey9L6MzFRYmgyuIK-hf3KQmUdVrFQF_-8pG-WVt8dHpKmYwqZ308cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6e3EMTxUL_Ng3Ifw8Cu7RuhfDQU53Fp0O5Jb5tC8Oj3aAvBhFgc8_mJTIUpX_D0Ixvu9JbsQY8GiH1mExO_NG97sx4q8XwYdxd4ZCMhKLXVw3Rmj2L9XtXgUdzyfd3nRMEDJpuS6wRmi-WrXGky-NyTVHXdaUSngrcMYLXpNSGDRirigA8VfydiDIYvEIQgJdc2Q_1DOLP6PLZJqjhNfn9jpNwTbKGlbLlCFj3y7aOuSoAm14aBTovp7r_Cylhl-qhGthgaTHoyu4QqlNoHKq2h2mqO0V9pbRHXkph35pBlifugI9O3_PsKaBDd_Ie5aJAmqmwqMLsJvN5ROquKdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzGOTBVTIwGaHH_-c80oMn4m8t88DAXdI8c9eiZoToETChTvuKcEJCXrPhPqcnfNR7bZ-JLpMYK-EkRK0X2znEQ5GzfKDFH559DqXn4ibmFzJeVsfXeh9LlHwo2zCGhn8T9rg7M84tHr-_RObJQdOsYUdIQGEoshmh0iMFihTTNaUPhnq27_buCDOpDUPAuoNvWTzxwPaOGn6FC1J7Z3a9O2lI_52BkE9cGQossPeEmd4DIWOGK5MiAsWTYUrG0shK6dF8lBdD84AfliF88F-NrRIT33FywoqMHHoFeo6wk-q7zcWv9zTj2aDrgZnetB0WiDr-mTybX6zsL5efBUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrOoTHTy-uS2SYARQF9Qt-VTcBbo4yOYUgOrosziDTv_kl1Tflmyv_Gmw79TXXn7YcKyqBirPjP4c5wKPLC58N1nQzousLszQIc8w0Nns76aykQcSqf9Bef7vLQw6ivkp4Tl9SJpax5zrdl1ymFWFE9yE3PzP0CZqymgz2f2FAwadj_jo9bYaxOA_xu34Ni8oJxYBp7Rzvj2FBVscO9MM244VtjvwUzjKfqCv9kAdoiM4LqhWLJe1AqIaEe8A7Xzd_fxIS4DOn3RPRKfgOs2h18KoXstJkk9yuaQ4lzMvSNVd3iFiGKas516ZbBJqQYaOmjuxPGUoF_Ym-ESERdMVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiY2Vc7Pdotih8rjOu96YNQMQioNMkw4MUuzLwoiISao0LqUg_rGOuM4HFf9SlyToO0BhjhcV8KxhlN-Z97ZCysakp-09gx8fpZxFGS0TKMicOiJiwkT3nthIOHSItREUbVfBBgieRKcAi69JQoEQ3TsjzrEBl65f9rUe4CEuEfrg1BFdXCj7Nac7OqKJAmrtt_8cJRSwLVDu_Rns4akYqWdcq-Ecknvmdb43YCdUGOVZzmXfZFLNvytkblRpJWle89fAFM-iS8VVpSHg-aJku6tTmhhUoDkh-ZTcMzyUv0rAhEjMkqs5cZqv44fnvzQKTieRk546z9VllnnvR4HLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/owAOMACdwcNiswzURmOBRaQZJ-GejKVfSciG64F94ZLCN9f7khvwN5zzcxB1xuvTPGKtFsb2DsEY8wt9rphskjCNrsDmGlv7Wsbt4gRp3LQy7cUKl9phYv3NymPWLrCEkhtqeTaup-CegimpfraLQAPfohE-FJ8IosQQYzrKNA9-kPSIAHjcCjRcL794iqobW2w2lZ5h6ybTe4544h-YDGbj5U5G44aewbmE7dBVP1P6wcyZOqzvS9wbxPC5c3RYwX2rlWJo4xkhcibJVFjIyMfLgXo-KarCs_o7a-Fngll7qgLVjduDe0qeySomoMYQElthuftwx2hB5Ld0E9wY6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PZG9MR-8GzTPcRP3143Sq1rnzRc5q2FkhpFYl552v_Ft8sxrBGRUFN1MCCMA9G4s65CjtU97yDceQlAQ9kEUaxkx8H8lH7ocQ9qcuOkONJc1Xi7gi1WVrmwdw9mdkE6zAz2ClNokorEYZvhrpBDWd5xjav5_rCVEQa0VmEfMULbUjvpLpMjUN8f6mFv44Ht6cjPCxWALBOmOoWPxqhxcFoLKGF_OWxeV8qbO9nmHDleu36NG2lHTB1v6E697Tdag7xeLHf1wBoLqhhoxlOeAQX_l6ODIeNKz9tWG4fYrMz1fkH-VCcarRPvr__BSYjwR_IE_HEt6iMw84Xvv3Xh38g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=j-dUTRlaQBL-TUNF3AplaXglhQBfl2kRYVnS3lQKOm33fXfrXGdQp9c3J5BQbh5GueMOkQNKiWMo0Lg-zTRdB6_PJ1fdnINpOPZkQ0MNLuY5pmmxDJqvNCTgLiL_vl3wZ-bL8GKTrDvGqkO3RpoZkWiMarNPX_2YWrfmwHzqs_PN_jx7TAOLRe2BV6PHe8s6-A3U9-1O-hgwuARhnqfy85dglj_g4dptkRSZ2t_cBOcVNTcnTr1StnyGzHPcQz0xlRZS1h6vsB4YJc8YDijjiBYUE43bSFieQumHXlAYorqemgbwNA3qwwgxlbBMiWEaOs3BdY9v7PflkdxmFCbXKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=j-dUTRlaQBL-TUNF3AplaXglhQBfl2kRYVnS3lQKOm33fXfrXGdQp9c3J5BQbh5GueMOkQNKiWMo0Lg-zTRdB6_PJ1fdnINpOPZkQ0MNLuY5pmmxDJqvNCTgLiL_vl3wZ-bL8GKTrDvGqkO3RpoZkWiMarNPX_2YWrfmwHzqs_PN_jx7TAOLRe2BV6PHe8s6-A3U9-1O-hgwuARhnqfy85dglj_g4dptkRSZ2t_cBOcVNTcnTr1StnyGzHPcQz0xlRZS1h6vsB4YJc8YDijjiBYUE43bSFieQumHXlAYorqemgbwNA3qwwgxlbBMiWEaOs3BdY9v7PflkdxmFCbXKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=CWHBLn63TfyTMRSu0PNVPjaQ0A4-xbXJrGM-Z4g3V2zYRPfRc6poOIlEpWZonCFMwGgQCUwVZITGrXZKW0Sec_Wz-FP1ApXqKKV69URbm-y0ie-KV-qmJUKtDRng0vRcyB75RdNzGJ2ki0v-4-5zl2DiJHXcaten9EiKFbUl4ektd-YOld1ozU_Kt3eX_73UG2WyAi-ur0OLwsXmC6O3Md9JDAoxCBdll2cq_9HTrdPXLKNs7gsjcIIMLL3OFgV5ZJgSTk_N-NJea-sYxjFsj0domILRH-niWoUzsQA6zQ49uPirCjTOjOOpOEwUow3VhCeOAhBily-oAnpzdwTa5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=CWHBLn63TfyTMRSu0PNVPjaQ0A4-xbXJrGM-Z4g3V2zYRPfRc6poOIlEpWZonCFMwGgQCUwVZITGrXZKW0Sec_Wz-FP1ApXqKKV69URbm-y0ie-KV-qmJUKtDRng0vRcyB75RdNzGJ2ki0v-4-5zl2DiJHXcaten9EiKFbUl4ektd-YOld1ozU_Kt3eX_73UG2WyAi-ur0OLwsXmC6O3Md9JDAoxCBdll2cq_9HTrdPXLKNs7gsjcIIMLL3OFgV5ZJgSTk_N-NJea-sYxjFsj0domILRH-niWoUzsQA6zQ49uPirCjTOjOOpOEwUow3VhCeOAhBily-oAnpzdwTa5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYHPT-MCPxiaZ9bl6cDrh5SyiiggLRDLdsVbgp2Cu9_gv9ODnWYZuVt65CqoleCFuBOtwguuosLccLeu2hdY0wirDttNQt4IRy3d-TQxzQeILvzwAqvMyiPKNIKY_4EBUIeg5XjAZn5psYw_dmdfnhszusA0rIU1Lj_cXHvqjob1O_WglYBYS_AfxAxA-dsfnyPzdThpxA7HyNvOVdpwZn-fWadt1ir0d7mgqIwBEl5Jws4WYGtHOLQMApppewUtvj06Aw17z7Bpbrx-Cs8vYCC6Gx7XRad6VR1YhkGZ5y5PvNqt1zqZXDamfvT6TcXIc5Jxw192Hqa3ubu7cXcgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D5wOhtxoCo5fwY_24abfpxd4r6sHGHpz75_M5FzkEVBQ-xYD8sw7e2opxMMffTk-h1Q_m1OIZH4moxCqD-n3Dry6giQ3EKBQy1XgkkLR4ddvCegc7cbRW2NdXxH5KguALhuCDRLc11ohbM9ZPhNEsLvPSl3pUOCBFSsQvdDJAP_j1A3X9zG2TOVhRIkJ0O9E0A7LDYl-cD056frpcQ07D61u80DXC4TdKUodmUk_8n8SJ3rGScyMvKVUkIbA7v26KTKy6NkatNBVn7PHPSndBohFGPi9zxNPPIppqlR69bUSsVBNp9xLqt4QjBb42zBiKljqJ6ysl0pOz-nnWkOnhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP0Yp3UX8ha9hRJxhuhJTAMIQDajgYSwSseOQK2x_gka_2DPd9oLMnpEOuYugkBRPq75PlxtsfmFKKeU8FTSh1fpsgYpZi4YKOINLfobHKQEb6a0HnmFWumQc1897uPjEzjH8xNFY2fpecDFNbH_KKY0Sch66xIibWhcRH_wH0SFAItQvEg94yY5Ob1rgI_33vwQUCl1Kzy_4bNPo-_uGkTx3aSFzV93Fv_Ayt3e4dq1PebOxMvqlFv2-9n-X1rdEyA1RRXCU04ED5yAzdIYHukDxFW_a09XcbSjibkw95Y9obREd3ZuF0kWRI_YxSPFr3di26AAb3EVdD1EL7TPhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lYHxrzuxuyAc7yZ1ty48UHwc8atSTGeXzpkd0WJ81bSxkrU_MUanS9_eCmRezRW6Fz9oLrQYP7eCB7566IZa90wW57bE3qV7k85ElVziCB9x-eeZPe3qkBB4IgSY24u7RX21r-4-rYjwbIdRU_fdQ3Nr-hvUHh5EFXcL-LA3W6aTz8eUijQ7dOQ1DPCKJp8itfDvKqZS4txoItnRiG7FuTepeBI8OeC1yWA1gXyTLeqqs1mTLB6TkFHge16lDmj-0elfN1u0rKhQL1lXg7JUNjzijqPBBISkCoaU7k765BvfyrvEMyqYI2vmq3zxTIrrp04UxAsVNY7sr6KTtg1ezds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lYHxrzuxuyAc7yZ1ty48UHwc8atSTGeXzpkd0WJ81bSxkrU_MUanS9_eCmRezRW6Fz9oLrQYP7eCB7566IZa90wW57bE3qV7k85ElVziCB9x-eeZPe3qkBB4IgSY24u7RX21r-4-rYjwbIdRU_fdQ3Nr-hvUHh5EFXcL-LA3W6aTz8eUijQ7dOQ1DPCKJp8itfDvKqZS4txoItnRiG7FuTepeBI8OeC1yWA1gXyTLeqqs1mTLB6TkFHge16lDmj-0elfN1u0rKhQL1lXg7JUNjzijqPBBISkCoaU7k765BvfyrvEMyqYI2vmq3zxTIrrp04UxAsVNY7sr6KTtg1ezds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما
که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!
همونجایی هستن
که بهش گفته بودن
نفت آمریکا در ۲۰۲۱ تموم میشه امروزه
در ۲۰۲۶ آمریکا بزرگ‌ترین تولید کننده
نفت جهانه!!
سال ۱۳۸۷ گفت بر اساس محاسبات کارشناس‌ها تا چند سال دیگه  دلار و یورو نابود میشن، در عوض و در عمل این ریال بود که نابود شد!
کلا محاسبات و آمارهای شما همیشه خیلی دقیقه!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=Tb2h1FBI2cgsRNH-UCLhRtvJ0yu4XZOLZVpM6JjH3Upo9TRoUKrP98dYdmB-bA8UFe7lZuZlwcvEMKZA51ec-OCjTAfR4-Gy2c8RlPHQmCdV_jU6SXpEMFuzwWAvCULEl0QmMQnxZzJ8dAhGf-uz5XLubEhRLXSpjNjcL5qSUWLBw14u5dgxkgD-gYBQIFgjHh5LDZIMGLw9g9ec1GcjZJgQgtAZrsDukkzXLyBeVpO58N2yA24lYknQV29Lt5ZtayqwK0JzQUUdZSKpZ13scip1rDKI82rLJAldhpHFL2tXy7VNtPtOxyhISGZN5uIh3iqgpjZab45hszNJzcNJKBcBtfjdGKHYU9Sf7e8m8Z9OOscxX1uwjPbz3ptq4YaReqTTJ8RlSLlG-mo7bn21fzKwDQAgkSci63lpMquAb-YYXds7fdyMG0Dct2qhnWJvpX4zoZIXGjjsXYqKznXxufnYVCUt2K00Pbi2GmxIWY5FgOZMUHFG21UpeR1xima__bJ1XmJjUAbG9ZtC1Qb82CUGHyUD05qL5Vtvi1vNJH82IdmmMipJ7W20VrElZxZuEwpmXQFnQ7498OWquFYv-ytUiC-wPTzCgAnI3EfAk11-mlE5ZlToKjivclTh_R1j5L1lcZDOn9nDywCFmAM9k9nl9-4pKmGPVdmhgeMJzbY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=Tb2h1FBI2cgsRNH-UCLhRtvJ0yu4XZOLZVpM6JjH3Upo9TRoUKrP98dYdmB-bA8UFe7lZuZlwcvEMKZA51ec-OCjTAfR4-Gy2c8RlPHQmCdV_jU6SXpEMFuzwWAvCULEl0QmMQnxZzJ8dAhGf-uz5XLubEhRLXSpjNjcL5qSUWLBw14u5dgxkgD-gYBQIFgjHh5LDZIMGLw9g9ec1GcjZJgQgtAZrsDukkzXLyBeVpO58N2yA24lYknQV29Lt5ZtayqwK0JzQUUdZSKpZ13scip1rDKI82rLJAldhpHFL2tXy7VNtPtOxyhISGZN5uIh3iqgpjZab45hszNJzcNJKBcBtfjdGKHYU9Sf7e8m8Z9OOscxX1uwjPbz3ptq4YaReqTTJ8RlSLlG-mo7bn21fzKwDQAgkSci63lpMquAb-YYXds7fdyMG0Dct2qhnWJvpX4zoZIXGjjsXYqKznXxufnYVCUt2K00Pbi2GmxIWY5FgOZMUHFG21UpeR1xima__bJ1XmJjUAbG9ZtC1Qb82CUGHyUD05qL5Vtvi1vNJH82IdmmMipJ7W20VrElZxZuEwpmXQFnQ7498OWquFYv-ytUiC-wPTzCgAnI3EfAk11-mlE5ZlToKjivclTh_R1j5L1lcZDOn9nDywCFmAM9k9nl9-4pKmGPVdmhgeMJzbY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMyKPdSqrYSBbMR4V1gyeC74yXkVXOZyD2iBNJvtGJbLh_O-nWbJQ2GW0F39dYXIHEQZDsKUVJh2VTP4BuaVRmdqeIfZdLytqjBcFnEtA1bCqEVtu-g3GX6MktXw82Stp-ONtD7kleh5YrgA_D0YWGOICEcxW_n1E8Ru0e-XBuro2cFMIZRYKF6mM_HfHJI-mo-ofXCSlPq1tWWspx9JuGBEVK9TOmAuDm1zzAp8ULZX-mbL-aBQA805HVGCecdtAHPZFyGdPvbfOync1Q9xbENRnAY9lYRQghxXzKxOhETU_Pc3xSXzr2pWgwwJ4I3QDcYGDxsZLyqbj0ymrqvksA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwXrLhwdi3gPrR0_Vl7gI2nsi567ITjUMjUiHDYAKBWHF2mqKJ3gwQJd8iFu7hS623OnB94y7JEXIEGkbcKEyQBUol3ZgElQwqzG7Y1pkn2dj0hYs9RibMw4ljdavLYmW7nfaZaXRfzNws8T8qQzvBMa3Zangs8wbD2Oz9_saervnKjYSRut1vJD8HJuoj5rVEhb7G1AGmqN6h-HAmFuqR6SUCrRVp_QgkZNnt__19K8S8WXHmGW_Kv91BFlXVHXe5IuS4AMBmuNmL_0dt2uq9CmA5-W7Y4UaBzErPwbQYMNNl-_eBde61M02-nzmJV3iUqeTF1ontUfbTkmbjMTOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Po28AvhEpc30loaUM-sbN_hWFel1XuW1xBetx_TYhGeQfx_3LdEkZOhOhpcsSg2QmAQS_D-YEa-Vw1Jj18mn8D5NbZHjww39_FoQEi1YlP_MHcSACbRYkzKMtKmrQH-x5qDpIzkVKEH23w6Bx7Rsj6TeGXAspeVVznSeQfUJz38_LgQJwrSHi_R5ANQEasNhaZvXNuCA8iJM7X0TIvohodFP67X4VFhgue329rAyT24WxXHUa-6bSGwe6m3c_3piUs9OTDB2dnFCLHpFGEo60Rz07ecueT_txJnzI-6kOQCOMEYZFk9VVCoD3N__ZtxtfFUi7oQ5TIIWdYLIfkXdkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=e5MNuxoSO11AinUtHnqf57B9lz_yOad5Sf7r3J4LHgf19Eha5-tK9yp-D_r_z_Jt0ZiIbSuawC742KVIty65IoTHugWbK8WhKD0RudqGNew-EGw6xEFzNLtiIFGVmIPqPZpBlo8WtdcbOZtDSy36dm5yQaRDt4vTY4vBCUW_Nce7gyoQfRj22Ub-2YWvXuOmJ3maKH86BkVVJfCeFeSam7kOCjSePm9awU5EPxEQw06HDn_9a044q9q6ZnszqHTT2oIQTgA_hRP_wSERjHbzXcfkT97vsQFYP7UFvIXBcXkVdeYyDPCM98UrulBmfHs71te6Twdp27UGilGdbQy5Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=e5MNuxoSO11AinUtHnqf57B9lz_yOad5Sf7r3J4LHgf19Eha5-tK9yp-D_r_z_Jt0ZiIbSuawC742KVIty65IoTHugWbK8WhKD0RudqGNew-EGw6xEFzNLtiIFGVmIPqPZpBlo8WtdcbOZtDSy36dm5yQaRDt4vTY4vBCUW_Nce7gyoQfRj22Ub-2YWvXuOmJ3maKH86BkVVJfCeFeSam7kOCjSePm9awU5EPxEQw06HDn_9a044q9q6ZnszqHTT2oIQTgA_hRP_wSERjHbzXcfkT97vsQFYP7UFvIXBcXkVdeYyDPCM98UrulBmfHs71te6Twdp27UGilGdbQy5Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrJrQhowQMFGZ5Ho-lfjDUjClrNboOwkD716mTWyuEYmTgDbDNeWsUxPwf9lmZ4ORW9c6PFJcFAxHLbGjAFuDshupgd6Kw_BorYyVhB637560Lz43C_nojvucN5kVL80gl0xdb63zpMhiRl8jYeCof4S51k2dQbfEoADz1F2No8BXP0uG1WnOc9ZPlCllm2oxEOGVw5cJnJiQ0x9CzIeSpMSJek2QWDAONzZW_Ms9b4GpKrGaS91UXuCW6TpNGtG-tLgPg9YkMs-srknT2yJq8i_lDX8mjlZQqL8GjQhlHMSipWScznNWlkk-vt4v1rPnEjjyEdKvVmOUN-TVn8vHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=LkVvKHBEqN9IF6V9UUvOLLcISK7CA0ToGFV92BXzvUJw7HhiLEOFgsrT_Tf8RsRASTbjPLJo1b-TqysBt0i9FnXlkOcazr6UG3N3ewuOSI-anxmYDokeJSI1mh8lFBA3wC2lX_KxbOlNWgnp2qdxbMs0ZJLZykzaATm41j9MJ5TUyJ5DRgDJm7hYh1b7Q88hRtofWcA4uE9x9Sa-dDUgwzEBgwYOcduJ4vdVLZ9o9rs2EQ3l7wu9QM2HllPdmLzoOukGkdDryGWwNNEYNJAKuo6XdLkSuruNrEgXyd_fju_NJZUx_OKyWgL0-WfP9yf_tq_fUzevfmYlPsSbvViHhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=LkVvKHBEqN9IF6V9UUvOLLcISK7CA0ToGFV92BXzvUJw7HhiLEOFgsrT_Tf8RsRASTbjPLJo1b-TqysBt0i9FnXlkOcazr6UG3N3ewuOSI-anxmYDokeJSI1mh8lFBA3wC2lX_KxbOlNWgnp2qdxbMs0ZJLZykzaATm41j9MJ5TUyJ5DRgDJm7hYh1b7Q88hRtofWcA4uE9x9Sa-dDUgwzEBgwYOcduJ4vdVLZ9o9rs2EQ3l7wu9QM2HllPdmLzoOukGkdDryGWwNNEYNJAKuo6XdLkSuruNrEgXyd_fju_NJZUx_OKyWgL0-WfP9yf_tq_fUzevfmYlPsSbvViHhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXT89Q1rK6I9t5_Q_Ml8L3UHU-95aBt7Nu_JMmHNwodqVyofECPcXEqYA68ySMFo0hEhLDmpUPCrpgU7hPjgDb_1xYfEa5MIEVUb5aMQU_vy7Zk3YqeFov7nWZGwJwoXYIybjQKBJPzWR2oo_MU62nym7r5VUkb_MxxSIJv_b3ro6GZE7XFQE1RRpyPP5dmBySpxBD86K1mn0b5xVTPjbmOd4nTUP1JPTP_wj-k9sGOkOOAF4GkaxiSb77OqMnPilPor4x7gJFy9Yr458cpJsT4JoIT9qeLxh70zqKXxu_C1A-QR4EKvsC_R-R2lxN-Ibb0jvwUV_WE66yzBGP1SWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkHhKtMYtw--tv-u90kcfCg76t4TS1Sf0Onm5fQYb2YX3ZBTV_AzQuAcnYyl21SVkrq5WLWVDvSaytOZaTywLKpHJb_JlufQ29xgGrZRVbwcr8L5yAN0hLYuR4tvuUrTHfWRfSNH0UUu9V_gT5bfOg6dBNyHqu0B6R197KGYE3zsyE7WCeW3kdA7tsv80NIgubzfrqsT2AUMa-LGCAOf8rjqY56RU9iKICQ1EEz0OwadnQxkTe_7i2T3BEXXQ6TF4ZUZxiOxM__NFPeFW4OVcs7A9vTyIP1wjHhpeQggDHYmW1IRWZbrrZU3g3_zsL3zX4j25OcK69QaLfbgjNKKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=WvjhcMcvxSwPtAuhZH6EP30YKWTnnkME3K7wcvZaQbbrI6csWjev_Z1JRZGKaOh0LuGByj3IQfAEvRAlSWkV9yA5Ko02Gui6KEdQSMToWUeXtEv7E59noGytj60KdSJQMFXSKNApW0oEfCW0UJfmRWqwOG75doo1FHugZ5Dw-WeXq3cjKbZpdUKY0wII4fWRf4-DtrasIpGuECrLaZhDrz-_-RQUo6OJitsI1t9VYxlsjCb4dGtFLMboic2F1f1XdFxSN763kp-XjfJg8zJa8raIgVPyDG-xjxkyKIX8aDzLx2YD8LO4rYN1CRQWtYbTT-8p-sEFJj-MHa2zKfR3FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=WvjhcMcvxSwPtAuhZH6EP30YKWTnnkME3K7wcvZaQbbrI6csWjev_Z1JRZGKaOh0LuGByj3IQfAEvRAlSWkV9yA5Ko02Gui6KEdQSMToWUeXtEv7E59noGytj60KdSJQMFXSKNApW0oEfCW0UJfmRWqwOG75doo1FHugZ5Dw-WeXq3cjKbZpdUKY0wII4fWRf4-DtrasIpGuECrLaZhDrz-_-RQUo6OJitsI1t9VYxlsjCb4dGtFLMboic2F1f1XdFxSN763kp-XjfJg8zJa8raIgVPyDG-xjxkyKIX8aDzLx2YD8LO4rYN1CRQWtYbTT-8p-sEFJj-MHa2zKfR3FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=LmC4Cy4KAo5PqfsAIdkcwD_dFiC60bViWwXaw2T9_EpCxZ0eqbclXDqQf5bxWeiq4ypZCVZMrd8YNmnR4ucO69j-Xo1tE2GUdaij7DAB_LWB318y1vjyBjjmp2SxUcnFur3N2yTAiYw2N9ho-5qYxO2UPxgWetU9h2Asn1SVS5rH8lC2Z6piUJnWk84SCfm9AYkN5g5zBOxz9TPhBFrCnSV9AaBuOT_9aG-2TaaAsdpbrQweb356FCfedMPO1tscJroWLCl5cVn5AynJQLYJiYyFtWScHcUwGUF_ig5NVeou8RIlUh2eOPtOCnDBqHEtsf88MB5_PBjSaRcC-_vn3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=LmC4Cy4KAo5PqfsAIdkcwD_dFiC60bViWwXaw2T9_EpCxZ0eqbclXDqQf5bxWeiq4ypZCVZMrd8YNmnR4ucO69j-Xo1tE2GUdaij7DAB_LWB318y1vjyBjjmp2SxUcnFur3N2yTAiYw2N9ho-5qYxO2UPxgWetU9h2Asn1SVS5rH8lC2Z6piUJnWk84SCfm9AYkN5g5zBOxz9TPhBFrCnSV9AaBuOT_9aG-2TaaAsdpbrQweb356FCfedMPO1tscJroWLCl5cVn5AynJQLYJiYyFtWScHcUwGUF_ig5NVeou8RIlUh2eOPtOCnDBqHEtsf88MB5_PBjSaRcC-_vn3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=eqMqJ-rrZV-OHJTP4LzD6EJQtJ-Upt0e76a7iXrp4UXFMhHViiIB1dWlhhXKzoJh0ewyW0siTpRqaoVtp8ZNVGG8aelQ6y_2fACWl0Nt2Ue764ECsStJmQGXn6ry1w47Qh-zlGfPYPknHSPOCUH7CyuV3jvh4fm9IuE8gGLfgDU14DsRqGDUnsbJfB3yrXprAFh9JLvk5xxGFL1mPx2pp_9vYxoxAfWD4-qOY4eaxJbquDohuiXPkOxMXpDlJlfbQhEX8mhwdvxiqxn_lhkQQFzQbhNGD4puZERLqbc69_E7Jv6CsQkut0iAKKTybgeHsjbw52_RzvII3bXT5HJGwDqV_G4bo876lvk0DIvjizq6VuuCBMKArVGwwO1m6t9eqc1GP3TVvjZIkMcJQ9sVFcC5QFV2V3rj8Vy_FSNy_ao-u31Bc5BUmLKdn5hm-vKGPAEdFXTxyyVShLjXpic6MBE5iN-38MRInufFdBlgtwXyrQVPWx00VCUcQzBO3V4Tqr1l0Yu2w0gw8439iehXvFxyAvlV8ekP8fokZRC2HBkVm2VBgWa3NPpI5RohfOlaUVtheujNK4cO5Vgo27ltCKGCkyrQ6qKx4l4RzTfshTwv617XnLQf9lpD_RF3rYRbIZEZ1XtoP-OK6ZLn_gbmQeoM3xcLjqIm-_ymqfXT1ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=eqMqJ-rrZV-OHJTP4LzD6EJQtJ-Upt0e76a7iXrp4UXFMhHViiIB1dWlhhXKzoJh0ewyW0siTpRqaoVtp8ZNVGG8aelQ6y_2fACWl0Nt2Ue764ECsStJmQGXn6ry1w47Qh-zlGfPYPknHSPOCUH7CyuV3jvh4fm9IuE8gGLfgDU14DsRqGDUnsbJfB3yrXprAFh9JLvk5xxGFL1mPx2pp_9vYxoxAfWD4-qOY4eaxJbquDohuiXPkOxMXpDlJlfbQhEX8mhwdvxiqxn_lhkQQFzQbhNGD4puZERLqbc69_E7Jv6CsQkut0iAKKTybgeHsjbw52_RzvII3bXT5HJGwDqV_G4bo876lvk0DIvjizq6VuuCBMKArVGwwO1m6t9eqc1GP3TVvjZIkMcJQ9sVFcC5QFV2V3rj8Vy_FSNy_ao-u31Bc5BUmLKdn5hm-vKGPAEdFXTxyyVShLjXpic6MBE5iN-38MRInufFdBlgtwXyrQVPWx00VCUcQzBO3V4Tqr1l0Yu2w0gw8439iehXvFxyAvlV8ekP8fokZRC2HBkVm2VBgWa3NPpI5RohfOlaUVtheujNK4cO5Vgo27ltCKGCkyrQ6qKx4l4RzTfshTwv617XnLQf9lpD_RF3rYRbIZEZ1XtoP-OK6ZLn_gbmQeoM3xcLjqIm-_ymqfXT1ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxax6um_9tZTNqtyAQDZtXIbNlAtwBrkX5bs5V8Y7095lpJ3TQbYjOK96kkkLemQdm7LuLG3ncvipNwMpgFMLOWZLso0wyRn3xiH9-e3FswKHTECetvrBDOJaa2HQl40x1H3-xB23LuMhcIsmJBjYgAdo7k8dndsgGyFSQjHjdIqzTPzumrdAcD7dDOHkqaT2TR5w23ZWcF9py1b5v9pbshmYYR6z9JQBVvvPux2XfL-ORGt0BFm_JvO3uktlDuf2Aimj7Sm2eQbB8VY5RywVMoNv7YYzBaYdRoT_vXlCXMj3xO4ECxqB1XUzhWO8zizHk2e6jZxt4iFAxlEv3ovww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQMWmB6YKscR9sm0ysQu5AkeLSqQZQ76yYjZs06Fi0ruNGZ-BnOcRiJyKXbSiS6YY1s23C23Hc9QWfgraqbI0_PnNvyc8UOVPcRCH36D6yaTI1r6_mLRDh2HpXlgxBcXlXrWqFLld6LmIlBkFrK8UJ0QqE15PC3tAc9PWPv4XtY_aeJAhXG4USKFAXFETnAuWN9prvI0pE2MgrLRw5D9Q6TqaVuDi6eIUyNEOuzhFNnoBoqj0VxO1O57q5WoMxbIO3gg9wRHZIwvR9wdpqgeWReDdwS7KKNkPw3aJoeO7ilNGVOc3u2_1x3Q8EiIh81m_3iO4-qaR02By4vCRb_Mkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIBX1NIX6IiinOlkFXz3LRE3cYIvF3rsqLc3jN8szZiw6Rk2UtLgJvcD7rCBLxaRBRQEvlPm5fMUr_QkEoEr7av3Usba03uiRGJPiOiLaWQ29cZgx2CFInV-5gL3Cxde5WcHp7q5hI5fAyErLlrCknR5SlCrecobW1Rac3lIWOP3sqhRM55rf3bG6Ggz2Ns6f3HWtBV9SFtiODYRKDNLkcfMkWdFnFZn-QAVZ-eZ1HEukukEvWorIP9y8snrpSSP9eIIjkxZWbOoAt7HyrGypaKIKsFju3RZBvWHdMPprvd6VZChVXNxaLYmLcwTYQ8CjAskAwbEUvldlYPR-uQNmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=Sz0C_dYhxZ1tyC4fI0HrzQNkgBn62IxGq4ogPl-YS5yemloFKKD_Ph2HZwJYMc2zbCzUyb_i5Y_TUVNXcT3cTv3CpOyx7hGQw90q6gQqKF9tFwbeWXx9R4c92qUGygA1PHjTj-aUH1xSMLxqjmUiYYJllPkyaSLq8z77mcxfBT97JbinTY5cOIZxESfwvvshIf_rEvGo_AqTVE-VyZJNJPQDjgqBQKvv7J7-_oKNJJayNWZ_eLWuestZaKC-ZIi3aZJMTm3oLb51wnExqtocZsAXjRxauB42uViy_COELSmlGoSMF2QDbs3jRAbvyfbY7bJeIfdh-H_b0s8p-Wf7FjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=Sz0C_dYhxZ1tyC4fI0HrzQNkgBn62IxGq4ogPl-YS5yemloFKKD_Ph2HZwJYMc2zbCzUyb_i5Y_TUVNXcT3cTv3CpOyx7hGQw90q6gQqKF9tFwbeWXx9R4c92qUGygA1PHjTj-aUH1xSMLxqjmUiYYJllPkyaSLq8z77mcxfBT97JbinTY5cOIZxESfwvvshIf_rEvGo_AqTVE-VyZJNJPQDjgqBQKvv7J7-_oKNJJayNWZ_eLWuestZaKC-ZIi3aZJMTm3oLb51wnExqtocZsAXjRxauB42uViy_COELSmlGoSMF2QDbs3jRAbvyfbY7bJeIfdh-H_b0s8p-Wf7FjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=L38h0_pr9QoYoSUnWraDcV3G8jwa24lhxgz3fKrNlns4qt0TDYh3xiIDLs7vIPDnZ0iTmxvnTe8FHlVBzKcCp2Fyopbo4e0nI0GfJrvCW_wYRXzCNpEFVYrRYheDyAqhTWL6r4DqOWLPGtzLQxM3tIJIllflRos6hqegXckF7CBStA9DJ94J4wfs_je0h61Ap7lGifOTUG7lUKNQC0Ab20kvmmQVHOz_aoL6hOnXf3_LjklJY5wSkiARGVdNeF0Faii4sJnfZUXyECozZ4u2CIgwmxQpN-L2XoLxY_3sIyqKrzTTfpW-wDNCE_AbWrzfOqxQH3SfZFASMvt78fDKpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=L38h0_pr9QoYoSUnWraDcV3G8jwa24lhxgz3fKrNlns4qt0TDYh3xiIDLs7vIPDnZ0iTmxvnTe8FHlVBzKcCp2Fyopbo4e0nI0GfJrvCW_wYRXzCNpEFVYrRYheDyAqhTWL6r4DqOWLPGtzLQxM3tIJIllflRos6hqegXckF7CBStA9DJ94J4wfs_je0h61Ap7lGifOTUG7lUKNQC0Ab20kvmmQVHOz_aoL6hOnXf3_LjklJY5wSkiARGVdNeF0Faii4sJnfZUXyECozZ4u2CIgwmxQpN-L2XoLxY_3sIyqKrzTTfpW-wDNCE_AbWrzfOqxQH3SfZFASMvt78fDKpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=chOJ_7QA0-dN_PO_L1sF4hNiwJ7xBY-T9IGXIm19d-yrrD495s984XtCaYoWwCMceTN4e93zgklg4-jppDuowqykR04VHNC00wJQdk9NgEXBb1mwAUue7gnCqFEl4AJl871ZxamagcKxTCbTuRQIBHOjpKZHhmY8MnWpiCuyDAJNtiWpVMN_7oK7f9FY7Gp9FPEfz8Qkaxmy1lLKWERa5p-Ec5EKiFt-cSc1EhugEWEWgFyf0SUQeodI6qhhO5ZtCSuH5jtrytr98RfokWt1bqeLIjQ0tpmbEirxowgoTz4a5B8wZnVBRGraTvUUeRPQy-2Jz0IwpWcOY-wr2VTwwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=chOJ_7QA0-dN_PO_L1sF4hNiwJ7xBY-T9IGXIm19d-yrrD495s984XtCaYoWwCMceTN4e93zgklg4-jppDuowqykR04VHNC00wJQdk9NgEXBb1mwAUue7gnCqFEl4AJl871ZxamagcKxTCbTuRQIBHOjpKZHhmY8MnWpiCuyDAJNtiWpVMN_7oK7f9FY7Gp9FPEfz8Qkaxmy1lLKWERa5p-Ec5EKiFt-cSc1EhugEWEWgFyf0SUQeodI6qhhO5ZtCSuH5jtrytr98RfokWt1bqeLIjQ0tpmbEirxowgoTz4a5B8wZnVBRGraTvUUeRPQy-2Jz0IwpWcOY-wr2VTwwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=FZLITLVaLf0qlUDO56UYxzHt0yPcMzMQhNQiHL8rrFANFjPo6AktNt5oGT1_S94YMwhiWmII2NxC_tAa6nSre93CDfn3PC1fEdfUkeDXQtZswLUldd4mS_xHwgJG3erK0fvQ1ddVPfMiipmxNNEB860lZ6ftHQw-CqslkWKdEA01ITkBloxYtURvLG2dENE63hL7loSygS-R1vWA2opM1z29vZZ5gclKWdS2MGtg2kdzj-GivymXmdZJC_-Z7i0gwKKlHsEzTv3JQXOTyKuOG5yGcXy4KR0OLV7ChNwKsZt6K0Z6FY-9oMaDI1UtGGiHzbWLswJQZOIW4cNgk00EJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=FZLITLVaLf0qlUDO56UYxzHt0yPcMzMQhNQiHL8rrFANFjPo6AktNt5oGT1_S94YMwhiWmII2NxC_tAa6nSre93CDfn3PC1fEdfUkeDXQtZswLUldd4mS_xHwgJG3erK0fvQ1ddVPfMiipmxNNEB860lZ6ftHQw-CqslkWKdEA01ITkBloxYtURvLG2dENE63hL7loSygS-R1vWA2opM1z29vZZ5gclKWdS2MGtg2kdzj-GivymXmdZJC_-Z7i0gwKKlHsEzTv3JQXOTyKuOG5yGcXy4KR0OLV7ChNwKsZt6K0Z6FY-9oMaDI1UtGGiHzbWLswJQZOIW4cNgk00EJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWsb1gWmvpFqtCiLDuGKysaWoLaZiv3Bd7XXPEwlTyXOMTvcnFAElfgIghps1jUx5_6in7en9o1yKciEgHAV79IZXfYzEhJxjVycZSTY6MIhKj5kP6SB3Bt2u9Km2WRIKxoIn05n-UZPTmxdDiblVZ7wBcleWT5AyeDQxwRAWeAw_hBhkaHuFH-DvNPUyF21aGUYw3_eIr9s0dh4vmrmreZtlq7uHCS1B73lJZ3_yF7E2E__EGL53NCEpNi_NkA4No8zx-JYsrWFWAWMc7onYOb82MPgYtv0zoPNJI4242mZvy5NI0l0o6Rb9UqAH8-gl2Jx1I3ofiBRgZSYidICcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=rA2NO2iHH3GK1osdIaBWJqvhQS3Y3GZYQZmcux-cn5MaMIrgj7cHLDkoJOD0e4a0QiWZANlZXuLtntBGuZFJdA6kJS37YAOj34jBaJp8rTZyZH5MtlbdVYD3433-Xe1EESJensirQsW7lgqRWe0gP2eqMNJtuc7WVSfHb6OtT4vsgjUkeod6Jrchcv-9NWQ7FPoYCFZyaItiwYAA4Wko4bkbhFT3ZxcYNpuL7STm-SwyhqVPYDj6nxATqi1gpt4PzYLX7vmi8Z-0m_7RhhbcJJIEBS9lje1lm7grC27GSZg1N_3Gc7JLmFxaf6yFO61_xN-RdHS0cycbmu5idXctYXYRnJiOTG_-V9xFaN9F7TZhNZNsv-LcGm7tHVF3H7DEnceyNnLz2SHigQoLOOFFSUo1N0MU9qODdbYY3un9Pq4aJIDW_XY6jdMCMgsY8hcskYDLJ7t-vCKu3DaOpA6CNnAEsPzALt2t-idcu7LkqigTXdywR8BSaOkc9Ye-HhnsCS2srRz4o56gTQodKEX3eq4qqkwIZNLWHf6PFyLnyky5zsUydJopFeNikA04sk6P77MLSVU_svG_F2bOdleXEa9IqMyYIRpxZhbtLiUym-yk1euiurRibY-5SsW-uDuMYzCigaZWNa04uFWkhsXWKS7FEzzN87m2dHBStK271YI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=rA2NO2iHH3GK1osdIaBWJqvhQS3Y3GZYQZmcux-cn5MaMIrgj7cHLDkoJOD0e4a0QiWZANlZXuLtntBGuZFJdA6kJS37YAOj34jBaJp8rTZyZH5MtlbdVYD3433-Xe1EESJensirQsW7lgqRWe0gP2eqMNJtuc7WVSfHb6OtT4vsgjUkeod6Jrchcv-9NWQ7FPoYCFZyaItiwYAA4Wko4bkbhFT3ZxcYNpuL7STm-SwyhqVPYDj6nxATqi1gpt4PzYLX7vmi8Z-0m_7RhhbcJJIEBS9lje1lm7grC27GSZg1N_3Gc7JLmFxaf6yFO61_xN-RdHS0cycbmu5idXctYXYRnJiOTG_-V9xFaN9F7TZhNZNsv-LcGm7tHVF3H7DEnceyNnLz2SHigQoLOOFFSUo1N0MU9qODdbYY3un9Pq4aJIDW_XY6jdMCMgsY8hcskYDLJ7t-vCKu3DaOpA6CNnAEsPzALt2t-idcu7LkqigTXdywR8BSaOkc9Ye-HhnsCS2srRz4o56gTQodKEX3eq4qqkwIZNLWHf6PFyLnyky5zsUydJopFeNikA04sk6P77MLSVU_svG_F2bOdleXEa9IqMyYIRpxZhbtLiUym-yk1euiurRibY-5SsW-uDuMYzCigaZWNa04uFWkhsXWKS7FEzzN87m2dHBStK271YI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=cLaDfMUlge_b-dDN5VEz9auDCJvsYsfV6eSQ3ADMjmhOfZDWCwOlxsAjRjnWa06E5HdA8U7Dz6PfN5L0l-Fums5Tp3eUQCT5o6va_p4bKHmRY2p2uId10_HdpUUj25iGAT2U5X0eD5SPDSMsAM_7ZXHRSoSVgeBicSd-y16-0UhaYRHJhLnvyEf4HPO01pOvv1bbz3d1HYaPnKTQnO8_LJw3Qb74g6C0Ir1SidhQqdpFA9DBAFi3MCVjnALLDCovS6zcj4Fznn2QtmXwV84wsCNS4OUm8pUe8qss9XCcJIVEMi_88smiZ5IM-Q56kmwReTvRFAR0D9Le2rcjvcBjpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=cLaDfMUlge_b-dDN5VEz9auDCJvsYsfV6eSQ3ADMjmhOfZDWCwOlxsAjRjnWa06E5HdA8U7Dz6PfN5L0l-Fums5Tp3eUQCT5o6va_p4bKHmRY2p2uId10_HdpUUj25iGAT2U5X0eD5SPDSMsAM_7ZXHRSoSVgeBicSd-y16-0UhaYRHJhLnvyEf4HPO01pOvv1bbz3d1HYaPnKTQnO8_LJw3Qb74g6C0Ir1SidhQqdpFA9DBAFi3MCVjnALLDCovS6zcj4Fznn2QtmXwV84wsCNS4OUm8pUe8qss9XCcJIVEMi_88smiZ5IM-Q56kmwReTvRFAR0D9Le2rcjvcBjpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4xbHWMZf3_uhDo5rARm0_n_lf5rRAdMQB_OwEebj5wurrAg2cpd64obWwOgc8WPL9KFIGiq4HWomAGRt_t5vpYdXBnOyx4V0nFNHYV3M1vBAXI9lwjAPW--ELkyF4A7EWxbhPJoBWrPUBVhTothSapdeldGs22VoyO6zfV3jiYVbSopoBEiH1sISVASy63GSxWApQuj3vkAYNwco5_kaaQjIlsZN8xwASjIWZ3CVmB5jfTUoojKdvSFGVKmik3LhTpzid4wEzk8M2UikLml7u1yInLmL6Qgiq0HLKeIzMTHYGxjCOYOynqknSPO2wNhPksUTEp53Xy782OtrGeKWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=UfQvPHgOp5M16t8I8NR7-4UJRrn6yvBct8UsNIAbASoddEtWYbtdmCCTu2ywYnSDK65SY6rbQIq26nNs9jyk5I8WOO8yyznmopJygoUZcZdbHZXpNSLQgkx02XKJY_JRdVf3hcb6rlFYpfjyLVZ6_T_8wMTcOITRAttTuZYKO9VDx7mArXCXtZS55jIGAiUnDKvPq-2JvcNLw7rrCIaVBHPvDezpcmcL1w6OBbuFw6p3Lyl2JePBP42_j1dxYeUtASXgwLE3pVAowhdtTy1b048NmJCkWphlKgoQrShbWetRH9LQb2GWbBSKmmbY08oCK2x_5Eoh78KWAvgL516TfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=UfQvPHgOp5M16t8I8NR7-4UJRrn6yvBct8UsNIAbASoddEtWYbtdmCCTu2ywYnSDK65SY6rbQIq26nNs9jyk5I8WOO8yyznmopJygoUZcZdbHZXpNSLQgkx02XKJY_JRdVf3hcb6rlFYpfjyLVZ6_T_8wMTcOITRAttTuZYKO9VDx7mArXCXtZS55jIGAiUnDKvPq-2JvcNLw7rrCIaVBHPvDezpcmcL1w6OBbuFw6p3Lyl2JePBP42_j1dxYeUtASXgwLE3pVAowhdtTy1b048NmJCkWphlKgoQrShbWetRH9LQb2GWbBSKmmbY08oCK2x_5Eoh78KWAvgL516TfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=XFATxboP8BeSndwijihLJXkb-VaDdIDH4vX5Zq7GAs3ussw0-t7duoks9hrcm0JbXKIIi7_gYB8RI5Bmh24A2WqQjk1qmroJvTqHaNsTNOuH8VNatR11thO0ouF3BMy4popH5qS2QLmCV_-6bQRp44hgEnYjAduYIp4PjXOG0abQGbAKsQX8v5A9r-2qxq55RHs--yepuUXbx2AgTcMkUb6cGRDRhQY-z-Crw2JP526jNALBQ9pQRnNNxZ52XDPXZkmF3eSkHNJVFKiu_gNffZ8MOXPtjyzae4nRWOoGj9JxkeOMig6hwZDa0Ajq7Z1bWYfNbIstckPHGf5uZIgVFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=XFATxboP8BeSndwijihLJXkb-VaDdIDH4vX5Zq7GAs3ussw0-t7duoks9hrcm0JbXKIIi7_gYB8RI5Bmh24A2WqQjk1qmroJvTqHaNsTNOuH8VNatR11thO0ouF3BMy4popH5qS2QLmCV_-6bQRp44hgEnYjAduYIp4PjXOG0abQGbAKsQX8v5A9r-2qxq55RHs--yepuUXbx2AgTcMkUb6cGRDRhQY-z-Crw2JP526jNALBQ9pQRnNNxZ52XDPXZkmF3eSkHNJVFKiu_gNffZ8MOXPtjyzae4nRWOoGj9JxkeOMig6hwZDa0Ajq7Z1bWYfNbIstckPHGf5uZIgVFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3SgyqJVHBc3e-QkXTx0DTrRn2zuNDRRfPsJ97aaphFIRV1e5F1X6ZnwwT7q9Eq1qtt4rfspzFtuXb7TV1UhKMSifdsfmJZr4B3FK9nu9I2ZDD8I8fsFM3Ymw5_m3wh5kzxT_cejJhJgFvRE1QLYvmz0Z6lOH9dSXpVpbBoAlutr4x2hL-MXeT_xgaoxMJ6gmspATcq-l0_mImmy6DFccaTOgFCDTsHYpngvcSTwiibgcbSr7BuLRcrGgnXu_ET1PAMZKw-SUuCfC7SfH4C5tEHFdEJslC6xPht7iMYJ7rzmTNP0B1i8_EhvvnpfovsNiV9wWnlAhzdPa0EbNSG8rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=T1lEl9kksPzQMWytpxNax6rjSbL8haHBh-nMaq6gvsZs3fNQwHOHI9I0a-AjQ-_GAwQe6xbPfVQRoKVSdfX-3eiV0w06BouOfnBji6RU7PPqcf2ykilQpUPvS6kTNuGzs_BxZRsUZeU-7bmeLCLdHE4yTnr3uCGEU6J2vqgISKi09jbwxvuBpIBKTejd7Q54W_nzsCnOZF8Wocu0WB0OSaElO3tUrrey-aswALenNM4cmiVADRXl604DxUDRZZnGFkSEIb6d36nIdPlMaSd48IY7R3OOsrPRAy-RNOFLv2IdHyvmdle5RPQ9Bf8bvR3UujoN-A-yQgLGUNavGSpFnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=T1lEl9kksPzQMWytpxNax6rjSbL8haHBh-nMaq6gvsZs3fNQwHOHI9I0a-AjQ-_GAwQe6xbPfVQRoKVSdfX-3eiV0w06BouOfnBji6RU7PPqcf2ykilQpUPvS6kTNuGzs_BxZRsUZeU-7bmeLCLdHE4yTnr3uCGEU6J2vqgISKi09jbwxvuBpIBKTejd7Q54W_nzsCnOZF8Wocu0WB0OSaElO3tUrrey-aswALenNM4cmiVADRXl604DxUDRZZnGFkSEIb6d36nIdPlMaSd48IY7R3OOsrPRAy-RNOFLv2IdHyvmdle5RPQ9Bf8bvR3UujoN-A-yQgLGUNavGSpFnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nS2NBkOLtI0o2dFt2eVM_ZBeynhNQ8YwF7QUvu0r3_tYRdUHM54B5Yiv9XUi8vKA-pAN-2f_F5wS0ZW7UmFK-1M3LfTHfAXq4BTGlJIGmljWqwNSAKJA5sab-3fQ11ZfHDH2Ymbw7ygNBUUt1Hj2-RepS9Fjebc5-yD9wGdDd_OeK8JXeB7A_BkiLn_unDeAIjhGM4-ZfCO0pb242oOIrzQP3tCrngcb-jKYFg_Ow3cSJt8arKtEzFa6kIK9BAh8Hy356P2JjaqCOZckbR3USVLUegUVSubpdxM7c-KiMSOdd92KGh_XEr3u9DHRAkXQlUx4MFvYzO3gOUi_4A1q-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=ayHBg3dy2DVedWvzoKieuG-IeiYzjcdLGRw2inF4R1IF8x8i0EXI1ozPtqqkrA513Ex88LMP8ev1xMjA_eCdA5fVj909sY3iJ8KJTrXU-mOuXCITYf8Sja3Toj6xYsiP4vgd1oVD3qV9eZxWzKFKGI2_6Cu0u85ofEVjP5XQ9zoheAYa9evebgr9xQBFRyQnbmiFhO7JJYnTgJkJdtBSSsIGxuw5_ULX_I7QubVPGopNxDnvLD2OITqSMrBia89u6Z-bAK6y6tpvE3euB2Cy2zgJyDDjTnH916InCCKj7H7sN3btd9OZSVyO6xdKZNueCA4V4WSPu0HDhRrlK8G9lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=ayHBg3dy2DVedWvzoKieuG-IeiYzjcdLGRw2inF4R1IF8x8i0EXI1ozPtqqkrA513Ex88LMP8ev1xMjA_eCdA5fVj909sY3iJ8KJTrXU-mOuXCITYf8Sja3Toj6xYsiP4vgd1oVD3qV9eZxWzKFKGI2_6Cu0u85ofEVjP5XQ9zoheAYa9evebgr9xQBFRyQnbmiFhO7JJYnTgJkJdtBSSsIGxuw5_ULX_I7QubVPGopNxDnvLD2OITqSMrBia89u6Z-bAK6y6tpvE3euB2Cy2zgJyDDjTnH916InCCKj7H7sN3btd9OZSVyO6xdKZNueCA4V4WSPu0HDhRrlK8G9lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paPIH2KE3uGQ0e73-BX9OU4F9OWThLzbQkCwx9oePa0nFXl-quDHfZFW9TvoXpYznflVRTq-A94EIqsqLiOL3DGE46j6uLh4APTNiJlo3JMeHX1L_rI-3oEa2P6Um5ulTgdAB_n6ywVIpy3XnOU24pSUAQBC9U80DZiXd1p_hZ0EjUZBTCbsT6QVCkO2NQkGPoQBz4JRQe0KvxyaE-IDxTgBG3IYRqbeqEUV0JtNINexbNyy5y7T16RRWswMwtAa7aWaDirEG_V18SPwg01k9ez_hGS7v_WRnDLFhaqKUo_rz7NI5omQIdNPQkcFxOryjrAB8iANhzeA2_mrkTwaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
